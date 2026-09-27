# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Ingrid and Erik are playing a game. For a given odd prime $p$, the numbers $1, 2, 3, ..., p-1$ are written on a blackboard. The players take turns making moves with Ingrid starting. A move consists of one of the players crossing out a number on the board that has not yet been crossed out. If the product of all currently crossed out numbers is $1 \pmod p$ after the move, the player whose move it was receives one point, otherwise, zero points are awarded. The game ends after all numbers have been crossed out.

The player who has received the most points by the end of the game wins. If both players have the same score, the game ends in a draw. For each $p$, determine which player (if any) has a winning strategy       — 题目文本
#   
To analyze this problem, we need to determine the strategy and scores for each player based on the prime number \( p \).

### Step 1: Game Description and Point Calculation

In the game, if Ingrid or Erik crosses out a number and the product of all crossed-out numbers modulo \( p \) is \( 1 \pmod{p} \), that player earns a point.

### Step 2: Understanding the Structure for Small Values of \( p \)

Let's consider small values of \( p \) to see how the scores may develop:

#### Case: \( p = 3 \)

- Numbers: \( 1, 2 \).
- Ingrid starts and can immediately cross out \( 1 \), making the product \( 1 \equiv 1 \pmod{3} \). She scores 1 point.
- The game then requires crossing out \( 2 \). Regardless of who plays next, no point can be scored.
- Ingrid wins because she has 1 point and Erik has 0.

#### Case: \( p = 5 \)

- Numbers: \( 1, 2, 3, 4 \).
- Ingrid starts and crosses out \( 1 \). Product is \( 1 \equiv 1 \pmod{5} \), scoring 1 point.
- The numbers \( 2, 3, 4 \) remain. No further single move results in a product of 1 modulo 5 without coordination from both players.
- Ingrid wins by initial advantage and strategic plays.

#### Case: \( p = 7 \)

- Consider the numbers \( 1, 2, 3, 4, 5, 6 \).
- Ingrid can start by crossing out \( 1 \) for a point.
- No immediate pair combination among \( 2, 3, 4, 5, 6 \) allows creating a product modulo 7 equal to 1 without back-and-forth strategy.
- Ultimately, both players may end up having the same number of points if they play optimally, leading to a draw.

### Step 3: General Strategy Analysis for \( p > 7 \)

- As \( p \) increases, the more possibilities emerge for creating products equalling 1 modulo \( p \) later in the game.
- Erik can strategize to create modulo 1 situations more frequently due to more available numbers after initial movements, likely outscoring Ingrid for \( p > 7 \).

### Conclusion

- For \( p = 3 \) and \( p = 5 \), Ingrid has a clear winning strategy.
- For \( p = 7 \), optimal play for both leads to a draw.
- For \( p > 7 \), Erik can implement strategies to ensure more scores than Ingrid, thereby winning.

Thus, we conclude:
\[ \boxed{\text{Ingrid for } p = 3 \text{ and } p = 5, \text{ Draw for } p = 7, \text{ Erik for } p > 7.} \]
```  — 标准解答
#   Let me analyze this problem carefully.

We have a game where two players A and B take turns choosing positive integers $k \le n$. Rules:
(i) Can't choose a number already chosen by either player.
(ii) Can't choose a number consecutive to any number the player has already chosen (on their own previous turns).
(iii) Draw if all numbers chosen; otherwise the player who can't move loses.

A goes first. Determine the outcome with optimal play.

Let me think about this carefully.

Each player has their own "set" of chosen numbers. The constraint (ii) is personal: a player cannot choose a number consecutive to any of THEIR OWN previously chosen numbers. So if A chose 3, A can't choose 2 or 4 later, but B can choose 2 or 4.

Constraint (i) is global: no number can be chosen twice.

So the game: numbers 1 to n. Players alternate. A player picks an unclaimed number that is not adjacent to any number they personally already hold.

Let me think about small cases.

n=1: A picks 1. All numbers chosen → draw.

n=2: A picks 1 (or 2). B picks 2 (or 1). All chosen → draw.

n=3: A picks 1. B picks... B can pick 2 or 3. If B picks 3, A can pick 2 (2 is not adjacent to A's 1? 2 is consecutive to 1, so A can't pick 2). Wait, A has {1}, so A can't pick 2. A can pick 3? No, 3 taken. So A can't move. A loses. So if A picks 1, B picks 3, A loses.

What if A picks 2? B picks 1 or 3. Say B picks 1. A has {2}, can't pick 1 or 3. A can't move. A loses. If B picks 3, same. So A loses with n=3.

Wait, but can A pick 2 and then... A has {2}, forbidden for A: 1,3. Both taken or... 1 and 3 available. A can't pick either. So A loses.

So n=3: B wins (A loses).

Hmm wait, let me reconsider. After A picks 2, B picks 1. Now A needs to pick from {3} (since 2 taken, 1 taken). 3 is adjacent to A's 2. So A can't. A loses. Yes.

n=3: Second player B wins.

n=4: A picks 1. B picks... Let's see. A has {1}. B wants to win. Available: 2,3,4. B can pick 2,3, or 4 (none adjacent to B's empty set).

If B picks 4: A has {1}, forbidden 2. Available: 3. A picks 3 (not adjacent to 1). A has {1,3}. B has {4}, forbidden 3,5. Available: 2. B picks 2 (not adjacent to 4). All chosen → draw.

If B picks 3: A has {1}, forbidden 2. Available: 2,4. A picks 4 (not adjacent to 1). A={1,4}. B={3}, forbidden 2,4. Available: 2. B can't pick 2 (adjacent to 3). B loses!

So if A picks 1 and B picks 3, then A picks 4, B loses. So B shouldn't pick 3.

If B picks 2: A={1}, forbidden 2. Available 3,4. A picks 4 (not adj to 1). A={1,4}. B={2}, forbidden 1,3. Available 3. B can't pick 3 (adj to 2). B loses!

So if A picks 1, B's best is pick 4 → draw.

But can A do better than draw? A picks 1, B picks 4 → draw as shown. Let me check other A first moves.

A picks 2: B picks 4 (symmetry-ish). A={2}, forbidden 1,3. Available 1,3,4. A can't pick 1 or 3. A picks 4. A={2,4}. B={}? B picks next... wait order: A,B,A,B,...

Let me redo. n=4. A picks 2. B's turn. Available 1,3,4. B picks 4. A's turn. A={2}, forbidden 1,3. Available 1,3. A can't pick either. A loses!

So A picking 2 is bad. A picks 3 similar by symmetry. A picks 4 symmetric to picking 1.

So A picks 1 (or 4), B picks 4 (or 1), draw.

n=4: draw.

n=5: Let me think. A picks 3 (middle). A={3}, forbidden 2,4. B picks from {1,2,4,5}. 

Hmm this is getting complex. Let me think about the structure more generally.

Actually, let me think about this game more cleverly.

Key insight: Each player's chosen set must be an "independent set" in the path graph (no two consecutive). And the two players' sets are disjoint and together with unclaimed form a partition.

The game ends in a draw if all numbers are chosen, meaning the two players partition {1,...,n} into two sets, each being an independent set (no two consecutive within each player's set).

Wait, is that the condition for draw? Draw if all numbers chosen. For all numbers to be chosen, each player's set must be an independent set. So a draw is possible iff {1,...,n} can be partitioned into two independent sets, i.e., {1,...,n} is 2-colorable, i.e., bipartite. The path graph is bipartite! So a draw is always possible in principle (color by parity: odds to one, evens to other).

But the question is whether players can force a draw or force a win, with optimal play.

Actually the game might not end in a draw even though it's possible, because players make choices.

Let me reconsider. The path graph P_n is bipartite with the parity coloring. If both players cooperate, draw is achievable. But with optimal (adversarial) play, one player might force the other into a position where they can't move.

Let me think about it as: the game is a normal-play game where a player who can't move loses, but if all numbers get chosen it's a draw.

Let me reconsider small cases and compute more carefully, maybe write a mental minimax.

Actually, let me think about the structure. Let me consider the game state as (available numbers, A's set, B's set, whose turn). The constraint for the current player: pick an available number not adjacent to any in their own set.

This is complex. Let me try to find a pattern by computing small n.

Let me define the game value: from the perspective of the player to move, outcome is Win (current player wins), Lose, or Draw.

n=1: A picks 1, all chosen, draw. So outcome = Draw.

n=2: A picks 1, B picks 2, all chosen, draw. Or A picks 2, B picks 1, draw. Draw.

n=3: computed above, A loses (B wins). So outcome for A = Lose.

n=4: draw.

n=5: Let me compute.

A's options: pick 1,2,3,4,5. By symmetry pick 1,2,3.

Case A picks 3: A={3}, A forbidden {2,4}. Available {1,2,4,5}. B's turn.
  B options: 1,2,4,5 (none adjacent to B's empty set, all available).
  Subcase B picks 1: B={1}, B forbidden {2}. Available {2,4,5}. A's turn. A forbidden {2,4}. A can pick 5 (available, not forbidden). A picks 5. A={3,5}, A forbidden {2,4}. Available {2,4}. B's turn. B={1}, B forbidden {2}. B can pick 4 (available, not forbidden). B picks 4. B={1,4}. Available {2}. A's turn. A forbidden {2,4}→2 forbidden. A can't pick 2. A loses. So this line: A loses.
    Wait, could A have done better? After B picks 1, A's turn with available {2,4,5}, A forbidden {2,4}. A can only pick 5. So forced. Then B picks 4 forced? B={1}, forbidden{2}, available{2,4}. B can pick 4. Then A stuck. Alternatively B picks 2? B forbidden {2} so can't. So B picks 4. A stuck. A loses.
  Subcase B picks 2: B={2}, B forbidden {1,3}. Available {1,4,5}. A's turn, A forbidden {2,4}. A can pick 1 or 5.
    A picks 1: A={1,3}, A forbidden {2,4}. Available {4,5}. B's turn. B={2}, B forbidden{1,3}. B can pick 4 or 5. B picks 5: B={2,5}, forbidden{1,3,4,6}. Available{4}. A's turn, A forbidden{2,4}→4 forbidden. A can't. A loses. B picks 4: B={2,4}, forbidden{1,3,5}. Available{5}. A forbidden{2,4}. A can't pick 5? 5 not in A's forbidden (A forbidden is 2,4). So A can pick 5! A={1,3,5}. All chosen → draw. So B picks 5 → A loses. So B picks 5. A loses.
    A picks 5: A={3,5}, forbidden{2,4}. Available{1,4}. B={2}, forbidden{1,3}. B can pick 4. B={2,4}, forbidden{1,3,5}. Available{1}. A forbidden{2,4}. A can pick 1. A={1,3,5}. All chosen → draw. So B picks 4, then draw. Alternatively B picks 1? forbidden. So B picks 4 → draw. Hmm so if A picks 5, draw. But A wants to win or at least draw; A picking 5 gives draw, A picking 1 gives loss. So A picks 5 → draw in this subcase.
    Wait but B is the one choosing subcase. B wants A to lose. In subcase B picks 2, A can force draw (by picking 5). So from B's perspective, picking 2 leads to draw (A gets draw). But subcase B picks 1 leads to A losing. So B prefers picking 1. 
  So if A picks 3, B picks 1, A loses. So A picking 3 → A loses (B can force).

Hmm, so A picking 3 is losing for A.

Case A picks 1: A={1}, A forbidden {2}. Available {2,3,4,5}. B's turn.
  B options: 2,3,4,5.
  Subcase B picks 5: B={5}, B forbidden{4}. Available{2,3,4}. A's turn, A forbidden{2}. A can pick 3 or 4.
    A picks 3: A={1,3}, forbidden{2,4}. Available{2,4}. B's turn, B={5}, forbidden{4}. B can pick 2. B={2,5}. Available{4}. A forbidden{2,4}→4 forbidden. A can't. A loses.
    A picks 4: A={1,4}, forbidden{2,3,5}. Available{2,3}. B={5}, forbidden{4}. B can pick 2 or 3. B picks 3: B={3,5}, forbidden{2,4}. Available{2}. A forbidden{2,3,5}→2 forbidden. A can't. A loses. B picks 2: B={2,5}, forbidden{1,3,4}. Available{3}. A forbidden{2,3,5}→3 forbidden. A can't. A loses. So A picks 4 → A loses.
    So after B picks 5, A loses (both A options lose). 
  So A picks 1, B picks 5 → A loses.

Hmm. So A picks 1 also losing?

Wait, but B picking 5 — is that B's best? B wants A to lose, and picking 5 achieves that. So yes.

Case A picks 2: A={2}, A forbidden{1,3}. Available{1,3,4,5}. B's turn.
  B options: 1,3,4,5.
  Subcase B picks 5: B={5}, forbidden{4}. Available{1,3,4}. A forbidden{1,3}. A can pick 4. A={2,4}, forbidden{1,3,5}. Available{1,3}. B={5}, forbidden{4}. B can pick 1 or 3. B picks 1: B={1,5}, forbidden{2,4}. Available{3}. A forbidden{1,3,5}→3 forbidden. A can't. A loses. B picks 3: B={3,5}, forbidden{2,4}. Available{1}. A forbidden{1,3,5}→1 forbidden. A can't. A loses. So A loses.
  So A picks 2, B picks 5 → A loses.

So for n=5, A loses in all cases? Let me double check A picks 1 more carefully — maybe A has a better response.

A picks 1, B picks 5. Available{2,3,4}, A forbidden{2}. A can pick 3 or 4.
  A picks 3: A={1,3}, forb{2,4}. Avail{2,4}. B={5}, forb{4}. B picks 2. B={2,5}. Avail{4}. A forb{2,4}→ can't. A loses. Could B pick 4? forb. So B picks 2, A loses. 
  A picks 4: A={1,4}, forb{2,3,5}. Avail{2,3}. B={5},b{4}. B picks 3 (or 2). Either way A loses as shown.
So yes A loses.

So n=5: A loses (B wins).

n=1: draw, n=2: draw, n=3: B wins, n=4: draw, n=5: B wins.

Let me guess the pattern. Maybe: draw when n is even, B wins when n is odd? But n=1 is odd and draw. Hmm. n=1 draw, n=3 B wins, n=5 B wins.

Let me reconsider n=1. n=1: only number is 1. A picks 1. All chosen → draw. Yes draw.

So odd: n=1 draw, n=3 B wins, n=5 B wins. Even: n=2 draw, n=4 draw.

Hmm, maybe n=1 is special. Let me compute n=6.

This is getting complicated. Let me think more structurally.

Actually, let me reconsider. Maybe there's a strategy-stealing or pairing argument.

Let me think about the parity coloring. Color odds black, evens white. Note: a player's set being an independent set means... actually no, independent set means no two consecutive, which is exactly that within the player's set, no two adjacent in path. The path is bipartite with parity, so each parity class is an independent set. But a player's set can mix parities as long as no two are consecutive (e.g., {1,4} has 1 odd, 4 even, not consecutive, fine).

Hmm. Let me think about the total number of moves. The game ends when either all chosen (draw) or current player can't move (current player loses).

Let me think about maximum number of picks. Each player picks an independent set. The two independent sets are disjoint. Total picks = |A| + |B|. Draw iff total = n.

For the game to be a draw, need to partition {1..n} into two independent sets. Always possible (parity). But adversarial play might prevent it.

Let me think about a strategy for B when n is odd and ≥3.

Idea: B uses a "mirror" strategy around the center. For n odd, center is (n+1)/2. Pair numbers symmetrically: (i, n+1-i). When A picks i, B picks n+1-i.

Let me check: does this maintain B's constraint? B's set would be {n+1-i : i in A's set}. B needs no two consecutive in B's set. If A's set has no two consecutive (which it must, by A's own constraint), then is {n+1-i} also having no two consecutive? Reflection preserves adjacency: n+1-i and n+1-j are consecutive iff i and j are consecutive. So yes, B's set is also an independent set. Good, B's constraint maintained.

Also need n+1-i available and not equal to i (so that B doesn't pick same). If i = n+1-i, i.e., i = (n+1)/2 (the center), then B can't mirror. So if A picks the center, B needs a different response.

Also need n+1-i not already chosen by A. Since A's set is independent and we're mirroring, could A have both i and n+1-i? Those are symmetric positions; they're consecutive only if... i and n+1-i consecutive means |i - (n+1-i)| = 1, i.e., |2i - n - 1| = 1, i.e., 2i = n or n+2, i even cases. E.g., n=5: i and 6-i. i=2,4: 2 and 4 not consecutive (diff 2). i=3 center. So A could pick both 2 and 4? They're not consecutive, so allowed. Then B can't mirror 2→4 since 4 taken.

Hmm, so the mirror strategy has issues when A picks symmetric pairs.

Let me reconsider. Let me think about n=5 with mirror strategy. Center 3. 
A picks 1 → B picks 5. A picks 2? A={1}, forb{2}. Can't pick 2. A picks 3? A={1,3}, forb{2,4}. B={5}, forb{4}. B mirrors: A picked 3 (center), no mirror. Hmm.

Actually in n=5, we saw B wins. Let me see the winning strategy. B picks 5 in response to A's 1 (that's the mirror!). Then A picks 3 or 4. If A picks 3: B={5}, mirror of 3 is 3 (center), can't. B picks 2 (we found B picks 2 → A loses). If A picks 4: mirror is 2, B picks 2 or 3 → A loses.

So mirror works mostly; center is the issue but B handles it.

Let me think about whether B always wins for odd n ≥ 3, and draw for even n.

For even n, mirror strategy: pair (i, n+1-i), no center. B mirrors A. Then B's set = reflection of A's set, independent. At the end, if A has picked set S, B has picked reflection. Total = 2|S| if S and reflection disjoint. They're disjoint since no fixed point (n even, n+1-i ≠ i always... wait n even, n+1 odd, n+1-i = i means 2i = n+1, no integer solution). So S and reflection always disjoint. So after A picks k numbers and B mirrors k numbers, 2k numbers chosen. Game continues until... A can't move → A loses? But we said even n is draw. Contradiction?

Wait, the mirror strategy for B: whenever A picks i, B picks n+1-i. This ensures B always can move (as long as A just moved and the mirror is available). The game ends when A can't move (A loses) or all chosen (draw). 

If B mirrors perfectly, the number of chosen numbers is always even after B's turn. A moves on odd-count states. A can't move when all available numbers for A are forbidden/taken. 

Hmm, but does mirror guarantee A eventually can't move, or draw? Let me check n=4 with mirror.

n=4: pairs (1,4),(2,3). A picks 1, B picks 4. A={1}, forb{2}. Available{2,3}. A picks 3 (not forb). A={1,3}, forb{2,4}. B mirrors: A picked 3, mirror 2. B picks 2. B={4,2}={2,4}. All chosen → draw. 

So n=4 mirror → draw. A picked 1 then 3, B picked 4 then 2, all 4 chosen, draw. Good, consistent.

But could A deviate to make B's mirror fail? A picks 1, B picks 4. A picks 3 (only non-forbidden available besides... available {2,3}, A forb{2}, so A must pick 3). So forced, draw. Good.

n=4 is draw confirmed.

Now for even n generally, does mirror always lead to draw, and can A do better? Mirror guarantees B can always respond, so B never gets stuck. The game ends with either A stuck (A loses) or all chosen (draw). For B to win, A must get stuck. For draw, all chosen.

With mirror, after each pair of moves, 2 numbers removed (i and n+1-i). The remaining available numbers form a symmetric set. A's forbidden set is A's own numbers' neighbors. 

Hmm, actually with mirror, does A always have a move until all are chosen? Not necessarily. Let me think about n=6.

n=6: pairs (1,6),(2,5),(3,4). 
A picks 1, B picks 6. A={1},f{2}. Avail{2,3,4,5}. A picks 3. B picks 4 (mirror of 3). A={1,3},f{2,4}. Avail{2,5}. A picks 5 (not forb, 5 not in {2,4}). B picks 2 (mirror of 5). All chosen → draw.

A picks 1, B picks 6. A picks 5. B picks 2. A={1,5},f{2,4,6}. Avail{3,4}. A picks 3 (not in f). B picks 4 (mirror of 3). All chosen draw.

A picks 1, B picks 6. A picks 4. B picks 3. A={1,4},f{2,3,5}. Avail{2,5}. A can't pick 2 or 5 (both forbidden). A loses!

Oh! So if A picks 4 (after 1,6), A gets stuck. But A wouldn't pick 4; A wants to win/draw. A picks 3 or 5 → draw. So with optimal A, draw. But this shows mirror doesn't always lead to draw; A can blunder. With optimal play A avoids losing moves. So n=6 draw (A can guarantee at least draw by good play, B mirrors guaranteeing B doesn't lose).

But wait — can A force a WIN in even n? For A to win, B must get stuck. With mirror strategy, B always has a response (mirror available), so B never gets stuck. So A can't win. And A can avoid losing (pick moves that don't get stuck). So even n → draw (with optimal play, A avoids loss, B avoids loss via mirror).

Hmm, but I need to verify A can always avoid getting stuck in even n. Let me think: is there always a "safe" move for A that doesn't lead to A getting stuck later?

Actually, let me reconsider. The claim "B's mirror is always available" — is it? When A picks i, is n+1-i always available (not already chosen)? B's set is the reflection of A's set so far. n+1-i could be in B's set already if A previously picked the mirror of i, i.e., A picked n+1-i before. But A's set is independent; can A contain both i and n+1-i? They're consecutive iff |2i-n-1|=1. For even n, 2i-n-1 is odd, can be ±1. E.g., n=6: 2i-7=±1 → i=3 or 4. So A could pick 3 and 4? 3,4 consecutive — not allowed (A's constraint). So A can't pick both 3 and 4. So A can't pick both i and n+1-i when they're consecutive. When they're not consecutive (|2i-n-1|>1), A could pick both. E.g., n=8: i=2, n+1-i=7, not consecutive, A could pick 2 and 7. Then when A picks 7, mirror is 2, but 2 already in A's set, so not available... but wait B would have mirrored earlier: A picks 2 first, B picks 7. Then 7 is taken by B, A can't pick 7 later. So A can't pick both 2 and 7 because B takes 7.

Right! Because B mirrors immediately. After A picks 2, B picks 7. So 7 is taken. A can never pick 7. So A's set and B's set: A picks i, B immediately takes n+1-i. So A can never pick n+1-i for any i A picked. So A's set S and B's set = reflection(S) are disjoint by construction. And B's mirror is always available because: when A picks i, is n+1-i free? n+1-i is in B's set iff A previously picked i' with n+1-i' = n+1-i, i.e., i'=i, no. n+1-i in A's set iff A picked n+1-i before, but A can't have because... actually A could pick n+1-i only if it were free, but B took it when A picked i... no wait, A picks i, then B picks n+1-i. So n+1-i becomes taken right after A picks i. So A can't pick n+1-i later. But could A have picked n+1-i BEFORE picking i? If A picked n+1-i first, then B would pick i (mirror), so i would be taken, A couldn't pick i now. Contradiction with A picking i now. So no. Therefore n+1-i is always free when B needs it. 

So B's mirror strategy is always executable for even n. B never gets stuck. So A can't win. Now does the game always end in draw (all chosen) or can A get stuck? A gets stuck if at A's turn, all available numbers are forbidden for A. With mirror, after B's turn, the available set is symmetric (reflection-closed) minus... hmm. Let me think: total chosen = 2k after B's k-th move. Available = n - 2k numbers, symmetric set. A needs an available number not adjacent to A's set.

Could A get stuck while numbers remain? That would mean A loses. A wants to avoid this. The question is whether A has a strategy to always reach draw, or whether B can force A to get stuck.

For even n, I'll conjecture draw: A can always ensure draw. Let me think about A's strategy: A also mirrors? No. Let me think: A wants to ensure all numbers get chosen. 

Actually, maybe A can also use a strategy to guarantee not getting stuck. Alternatively, maybe for even n it's a draw because both can avoid losing.

Hmm, but actually maybe for even n ≥ some value, B can force a win? Let me check n=6 more carefully — can B force A to lose (not just A blundering)?

n=6. A picks first. Let me see if B has a winning strategy (not just mirror→draw, but something better).

A picks 1: B's options. Let me explore B picks 6 (mirror) → we saw A can draw by picking 3 or 5. Can B do better than mirror?
  B picks 5 instead? B={5},f{4}. Avail{2,3,4,6}. A={1},f{2}. A picks 3,4,or 6.
    A picks 6: A={1,6},f{2,5}. Avail{2,3,4}. B={5},f{4}. B picks 2 or 3. B picks 3: B={3,5},f{2,4}. Avail{2,4}. A={1,6},f{2,5}. A can pick 4 (not in f). A={1,4,6},f{2,3,5}. Avail{2}. B={3,5},f{2,4}. B can't pick 2. B loses! So B shouldn't pick 3. B picks 2: B={2,5},f{1,3,4}. Avail{3,4}. A={1,6},f{2,5}. A picks 3 or 4. A picks 3: A={1,3,6},f{2,4,5}. Avail{4}. B={2,5},f{1,3,4}. B can't pick 4. B loses. A picks 4: A={1,4,6},f{2,3,5}. Avail{3}. B can't pick 3 (f{1,3,4}). B loses. So A picks 6 → B loses. So B picking 5 is bad for B (A picks 6 wins for A).
  So after A picks 1, B picking 5 lets A win. B should mirror (pick 6) for draw.

This is getting deep. Let me just try to establish the pattern computationally for more n, but I can't run code easily... actually I can use exec to run a Python minimax!

Let me write a quick minimax solver.

Actually, let me just code it up and run it.

Let me think about the state representation. State: (available bitmask, A's set bitmask, B's set bitmask, turn). But that's 3 bitmasks up to n. For small n (up to ~16) feasible.

The constraint for current player P (with set S_P): can pick k if k available (not in A or B) and k not adjacent to any in S_P, i.e., k-1 not in S_P and k+1 not in S_P.

Let me code minimax returning outcome from current player's perspective: W (current wins), L (current loses), D (draw).

Memoize on (avail, Aset, Bset, turn). Actually turn is determined by parity of moves = n - popcount(avail). And whose turn: A starts, so turn = A if (n - popcount(avail)) even, else B. But Aset/Bset differ. Actually we need to know whose set is whose. State (avail, Aset, Bset), turn derived from popcount. Memoize.

Let me write it.

Let me just run it.
Interesting! Pattern:
- n=1: Draw
- n=2: Draw
- n=3: B wins
- n=4: Draw
- n=5: B wins
- n=6: Draw
- n=7 onwards: B wins

So draws at n=1,2,4,6 and B wins for n=3,5 and n≥7.

Let me check more to be sure about larger even n.
Larger n is slow. Let me wait a bit.
Too slow for larger n. The pattern up to n=18 is clear enough: Draw for n ∈ {1,2,4,6}, B wins for n ∈ {3,5} ∪ {n ≥ 7}.

Let me kill it and think about the proof.

So the answer:
- Draw for n = 1, 2, 4, 6.
- B wins for n = 3, 5, and n ≥ 7.

Wait, let me double-check n=6 is draw and n=7 B wins, n=8 B wins. Yes from output.

Hmm, that's an interesting pattern. Let me reconsider: draws at 1,2,4,6. B wins at 3,5,7,8,9,...

So for n ≥ 7, B always wins. And small exceptions: 1,2,4,6 draw; 3,5 B wins.

Let me re-examine. Actually wait, let me reconsider whether the pattern is "B wins for all n ≥ 3 except n=4,6". Or "draw for n ∈ {1,2,4,6}, B wins otherwise (n≥3)".

n=1: draw, n=2: draw, n=3: B, n=4: draw, n=5: B, n=6: draw, n≥7: B.

So draws: {1,2,4,6}. B wins: {3,5} ∪ {7,8,9,...}.

Let me make sure about the proof. I need to:
1. Show draw for n=1,2,4,6 (exhibit strategies / it's easy for small).
2. Show B wins for n=3,5 (explicit).
3. Show B wins for n≥7 (general strategy).

For n≥7, B has a winning strategy. Let me think about what strategy.

Let me think about the structure. The key idea: B wants to force A into a position where A can't move but numbers remain.

Let me think about a pairing/mirror strategy for B that forces A to get stuck.

For odd n, mirror around center: B picks n+1-i in response to A's i. The center c=(n+1)/2 is special. Let me think: with mirror, after all non-center numbers are paired off, the center remains. 

Actually let me think about what happens with mirror for odd n. n=7: center 4. Pairs (1,7),(2,6),(3,5). A picks i, B picks 8-i. If A ever picks 4 (center), B picks... some response.

Let me simulate n=7 mirror. A picks 1, B picks 7. A={1},f{2}. Avail{2,3,4,5,6}. A picks 3, B picks 5. A={1,3},f{2,4}. Avail{2,4,6}. A picks 6, B picks 2. A={1,3,6},f{2,4,5,7}. Avail{4}. A's turn? Wait count: moves so far: A(1),B(7),A(3),B(5),A(6),B(2) = 6 moves, 1 left (4). A's turn (move 7). A={1,3,6}, f{2,4,5,7}. Avail{4}. 4 in f. A can't move. A loses! 

But wait, A didn't have to pick 6. Let me see if A could avoid. After A={1,3},f{2,4}, avail{2,4,6}. A can pick 6 only (2,4 forbidden). So forced. Then B picks 2 (mirror of 6). Avail{4}. A can't. So A loses. But A's earlier choices: after A picks 1, B picks 7, A={1},f{2}, avail{2,3,4,5,6}. A could pick 3,4,5,6. 
  A picks 4 (center): A={1,4},f{2,3,5}. B's turn, B={7},f{6}. Avail{2,3,5,6}. B mirrors 4→4 (center, can't). B needs other move. B picks... B wants to win. Hmm, mirror breaks at center.

So for odd n, the center is a problem for pure mirror. But B still wins (computed). Let me find B's strategy.

Actually, let me reconsider. Maybe B's strategy for odd n: mirror, and if A takes center, B takes some specific move.

Let me think differently. Let me reconsider the general winning strategy for B for n≥7.

Alternative: think of it as B trying to leave A stuck. 

Let me think about the "pairing strategy" more carefully. Consider pairing consecutive numbers: (1,2),(3,4),(5,6),... When A picks one from a pair, B picks the other. But B's constraint: B picking the other of the pair — is it adjacent to B's existing? B's set would be the "partners". If pairs are (1,2),(3,4),..., B picks 2 when A picks 1, picks 1 when A picks 2, etc. B's set: could contain 2 and 1? No, only one per pair (B picks the partner of whatever A picked). B's set has at most one from each pair. Are B's numbers non-consecutive? B could have 2 (from pair (1,2)) and 3 (from pair (3,4)) — consecutive! So B's constraint violated. So this pairing doesn't work for B.

Let me think about pairing (1,n),(2,n-1),... the reflection pairing. For B's constraint: B's set is reflection of A's set. Reflection preserves non-consecutiveness (A's set is independent → B's set independent). Good. So reflection pairing keeps B legal. The only issue is the center for odd n.

For even n, reflection pairing has no center, B always legal, B never stuck. So B can force at least draw (B never loses). And we saw even n=2,4,6 draw, n≥8 B wins. Wait n=8 B wins! So for even n≥8, B wins, meaning B forces A to get stuck. But mirror only guarantees B doesn't get stuck; it doesn't guarantee A gets stuck. For n=8, B wins, so B has a strategy to make A stuck. Mirror might be that strategy (A gets stuck eventually) or B plays differently.

Wait, for n=4,6 mirror leads to draw (A can avoid getting stuck). For n=8, B wins — does mirror make A stuck, or does B need a different strategy?

Let me check n=8 with mirror. Pairs (1,8),(2,7),(3,6),(4,5). 
A picks 1, B picks 8. A={1},f{2}. Avail{2,3,4,5,6,7}. A picks 3, B picks 6. A={1,3},f{2,4}. Avail{2,4,5,7}. A picks 5, B picks 4. A={1,3,5},f{2,4,6}. Avail{2,7}. A picks 7 (not in f). B picks 2 (mirror of 7). All chosen → draw.

Hmm, so this line draws. But B wins for n=8, so B shouldn't just mirror; B should play to win. Let me find B's winning strategy via the solver — extract the optimal move.

Let me modify the code to show B's optimal first response and the game tree for n=8.

Actually, let me reconsider. The result says B wins for n=8. So B has a strategy. Let me extract it.
Pattern: Draw for n ∈ {1,2,4,6}, B wins for n ∈ {3,5} ∪ {n≥7}.

Let me extract optimal strategies to understand the structure. Let me get the optimal first moves and key lines for n=7,8.
Wait, the value shown is "value(from A)" but it's computed as bestmove for B's turn, returning best from B's perspective (current player = B). So v2 = value from B's perspective. value(from A) = -v2. Let me recheck the print. It prints `v2` directly but labels "value(from A)". The bestmove returns (bm, best) where best is from current player (B) perspective. So v2 is from B's perspective. So "value(from A)" label is wrong; it's actually from B's perspective. v2=1 means B wins. So all lines B wins. Good, consistent: n=7,8 B wins regardless of A's first move.

Interesting: for n=7, when A picks 1, B's best response is 7 (mirror!). For n=8, A picks 1 → B picks 8 (mirror). For other A first moves, B picks 1. Let me look deeper — let me trace a full optimal game for n=7 and n=8 to see B's strategy.

Let me trace the game tree following optimal play (A tries to win/draw, B tries to win).
Interesting. Let me look at the patterns. For n=7, A first=1: B plays 7, then A plays 3, B plays 2, A plays 5, B plays 4, A stuck. 

Note B's strategy isn't pure mirror. For n=7, A=1,B=7 (mirror), A=3, B=2 (not mirror of 3 which is 5). Hmm.

Let me look at the structure differently. Let me observe: in all these traces, A gets stuck after 3 moves each (6 total moves), with 1 number remaining. So A makes 3 picks, B makes 3 picks, 1 left, A can't take it.

For n=7: 7 numbers, 6 picked, 1 left, A stuck. A's 3 picks + B's 3 picks = 6.
For n=8: 8 numbers, 6 picked, 2 left, A stuck. A's 3 + B's 3 = 6, 2 remaining.

So B wins by getting A stuck after A's 3rd move (B's 3rd move leaves A stuck).

Let me look at the structure of A's set and B's set when A gets stuck.

n=7, A=1,B=7,A=3,B=2,A=5,B=4: A={1,3,5}, B={7,2,4}={2,4,7}. Remaining={6}. A's forbidden from {1,3,5}: {2,4,6}. 6 is forbidden. A stuck. 

n=8, A=1,B=8,A=3,B=5,A=6,B=2: A={1,3,6}, B={8,5,2}={2,5,8}. Remaining={4,7}. A's forbidden from {1,3,6}: {2,4,7}. Both 4,7 forbidden. A stuck.

Interesting. So B's strategy creates a situation where A's own set blocks all remaining numbers.

This is complex. Let me think about a cleaner structural proof rather than reproducing B's exact strategy.

Let me think about the problem in terms of "the player who is forced to break the parity coloring loses" or some invariant.

Key observation: For a draw, the final partition must be A's set and B's set, both independent sets, partitioning {1..n}. Since the path is bipartite with the unique 2-coloring (up to swap) being parity, ANY partition into two independent sets must be exactly the parity coloring (odds to one player, evens to the other)!

Wait, is that true? Is the 2-coloring of a path unique? A path P_n is connected and bipartite, so it has exactly 2 proper 2-colorings (swap the two colors). So yes, the only way to partition {1..n} into two independent sets is {odd} and {even} (one player gets all odds, the other all evens).

So a draw requires: one player has all odds, the other all evens. 

So for a draw to occur, A must end with exactly {odd numbers} or {even numbers}, and B the complement.

Now, the game: A moves first. Total moves = n (all chosen). A moves on turns 1,3,5,...; B on 2,4,6,... Number of A's moves = ceil(n/2), B's moves = floor(n/2).

For a draw: A's set = odds or evens. |odds| = ceil(n/2), |evens| = floor(n/2). A has ceil(n/2) moves, B has floor(n/2) moves. So A's set size = ceil(n/2) = |odds|. So A must get all odds, B all evens. (For both odd and even n, A gets odds, B gets evens, since A has the larger-or-equal count.)

Wait for even n: |odds|=|evens|=n/2. A has n/2 moves, B has n/2 moves. So A could be odds or evens. For odd n: |odds|=(n+1)/2=ceil, |evens|=(n-1)/2=floor. A has ceil moves. So A=odds, B=evens.

So for a draw, the partition is forced: A=odds, B=evens (for odd n), or A=odds,B=evens OR A=evens,B=odds (for even n).

Now here's the key: A moves first. A picks some number. For a draw to happen, A must eventually collect exactly all odds (or all evens). 

Now think about B's strategy to PREVENT a draw and instead win. B wins if A gets stuck (can't move) while numbers remain. B wants to force A into a position where A's own set blocks the remaining available numbers.

Hmm, let me think about a cleaner invariant/strategy.

Let me reconsider. The condition for draw is very rigid (parity partition). So B's goal: prevent the parity partition from being completed, AND ensure A is the one who gets stuck (not B).

Let me think about "who gets stuck". 

Alternative framing: think of it as a game where both players are building independent sets. The game ends when current player can't extend. 

Let me think about a strategy for B based on the parity insight.

Claim: For n ≥ 7 (and n=3,5), B wins. For n ∈ {1,2,4,6}, draw.

Let me think about B's strategy for n ≥ 7. 

Idea: B tries to "steal" one number of A's required parity, forcing A to either get stuck or deviate.

Hmm, let me think more concretely. Let me consider the parity classes O (odds) and E (evens). For a draw, A needs all of one class and B the other.

B's strategy: B will claim a number from the class that A is "supposed" to take, breaking the draw. But B must also ensure A gets stuck (not B).

Actually, let me think about it as: B plays to make A stuck. 

Let me look at the traces again for a structural pattern.

n=7, A=1,B=7,A=3,B=2,A=5,B=4: 
A's picks: 1,3,5 (all odd!). B's picks: 7,2,4. B picked 7 (odd!) and 2,4 (even). 
Remaining: 6 (even). A needs 6 but 6 adjacent to A's 5. Stuck.
So A took odds 1,3,5; B took 7 (an odd!) plus 2,4. By B taking 7 (odd), A can't complete all odds. And A's own 5 blocks 6.

n=8, A=1,B=8,A=3,B=5,A=6,B=2:
A: 1,3,6. B: 8,5,2. Remaining 4,7. A's forbidden {2,4,7}. Both remaining blocked.
A took 1,3 (odd) and 6 (even). B took 8,2 (even) and 5 (odd).

Hmm, the structure isn't simply "B steals parity." Let me think differently.

Let me think about a cleaner strategy. Let me consider the following B strategy for n ≥ 7:

Actually, let me reconsider. The problem is from a competition (looks like an ISL/shortlist problem). Let me think about what the clean answer is.

The pattern: Draw for n ∈ {1,2,4,6}, B wins otherwise.

Hmm wait, let me double check n=6 is really a draw and reconsider. And reconsider whether maybe I have the pattern right. Let me re-examine n=6 thoroughly and also n=10,12 to be sure B wins for even n≥8. The computation up to 18 confirms. Let me trust it.

Actually, let me reconsider — maybe the pattern is cleaner: Draw iff n ∈ {1,2,4,6}, i.e., n ≤ 6 and n ≠ 3,5. Or: B wins iff n ≥ 3 and n ∉ {4,6}. Equivalently B wins for n=3,5 and n≥7.

Hmm, is there a cleaner characterization? n=1,2,4,6 draw. These are n where... 1,2,4,6. Differences: 1,2,2. Not obvious. Maybe n=2^k or n=2k? 1,2,4 are powers of 2, but 6 isn't. n=1,2,4,6 = n where n≤6 and n even or n=1? 1 (odd),2,4,6 even. 3,5 odd ≥3. So: draw iff (n=1) or (n even and n≤6). B wins iff (n odd and n≥3) or (n even and n≥8). 

Hmm, let me double-check n=6 is draw and n=8 B wins by re-examining. The code is trustworthy I think. But let me re-verify n=6 by hand to be safe, since it's a boundary.

n=6. A picks 1. B's responses:
We need to check if B can force win, or A can force draw.

Let me just trust the minimax but verify the code logic once. The value function: returns from current player's perspective. 1=win, -1=lose, 0=draw. cv = -child (negamax). Looks right. Draw when avail==0 and no legal moves. A player with no legal moves and avail != 0 → loses (returns -1). Good.

Let me also double check: when avail==0, all numbers chosen → draw (return 0). And if avail != 0 but no legal moves → current loses. Correct per rules.

I'm fairly confident: Draw for n ∈ {1,2,4,6}, B wins for n ∈ {3,5} ∪ {n ≥ 7}.

Hmm, but this is a somewhat ugly answer. Let me reconsider whether the problem might have a cleaner answer that I'm missing due to a bug. Let me re-examine the rules once more.

"(ii) A player cannot choose a number consecutive to any of those the player has already chosen on any previous turn."

Yes, personal constraint. My code: myset adjacency. Correct.

"(iii) The game is a draw if all numbers have been chosen; otherwise the player who cannot choose a number anymore loses."

Yes. Correct.

Let me re-verify n=6 by hand more carefully to be sure it's a draw, because the boundary matters.

n=6. A picks 1. 
B's options: 2,3,4,5,6.
We want to know if B has a move that forces A to lose, or if A can always force draw.

By symmetry A could also pick other things, but let me check if A picking 1 leads to draw or win for someone, assuming optimal play. Actually A will pick the move that's best for A. The code says n=6 is draw, so A's best is draw.

Let me verify A picks 1, B's best response leads to draw (A can force draw), and no B response leads to B win.

A picks 1: A={1},f{2}. Avail{2,3,4,5,6}. B's turn.
  B picks 6 (mirror): B={6},f{5}. Avail{2,3,4,5}. A's turn, f{2}. A picks 3 or 4.
    A picks 3: A={1,3},f{2,4}. Avail{2,4,5}. B={6},f{5}. B picks 2 (or 4). 
      B picks 2: B={2,6},f{1,3,5}. Avail{4,5}. A={1,3},f{2,4}. A picks 5 (not in f). A={1,3,5},f{2,4,6}. Avail{4}. B={2,6},f{1,3,5}. B can't pick 4? 4 not in B's f{1,3,5}. So B picks 4. All chosen → draw.
      B picks 4: B={4,6},f{3,5}. Avail{2,5}. A={1,3},f{2,4}. A picks 5 (not in f). A={1,3,5}. Avail{2}. B={4,6},f{3,5}. B picks 2. All chosen draw.
    A picks 4: A={1,4},f{2,3,5}. Avail{2,3,5}. B={6},f{5}. B picks 2 or 3.
      B picks 2: B={2,6},f{1,3,5}. Avail{3,5}. A={1,4},f{2,3,5}. A can't pick 3 or 5. A stuck! A loses.
      B picks 3: B={3,6},f{2,4}. Avail{2,5}. A={1,4},f{2,3,5}. A can't pick 2 or 5. A stuck! A loses.
    So if A picks 4, A loses. So A picks 3 → draw. So after B picks 6, A picks 3 → draw.
  So B picks 6 → draw (A plays correctly). Can B do better?
  B picks 5: B={5},f{4,6}. Avail{2,3,4,6}. A={1},f{2}. A picks 3,4,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{2,3,4}. B={5},f{4,6}. B picks 2 or 3.
      B picks 2: B={2,5},f{1,3,4,6}. Avail{3,4}. A={1,6},f{2,5,7}. A picks 3 or 4. A picks 3: A={1,3,6},f{2,4,5,7}. Avail{4}. B={2,5},f{1,3,4,6}. B can't pick 4. B stuck! B loses. A picks 4: A={1,4,6},f{2,3,5,7}. Avail{3}. B={2,5},f{1,3,4,6}. B can't pick 3. B loses. So A picks 6 → B loses. 
    So B picks 5 is bad (A picks 6, B loses).
  B picks 4: B={4},f{3,5}. Avail{2,3,5,6}. A={1},f{2}. A picks 3,5,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{2,3,5}. B={4},f{3,5}. B picks 2. B={2,4},f{1,3,5}. Avail{3,5}. A={1,6},f{2,5,7}. A picks 3. A={1,3,6},f{2,4,5,7}. Avail{5}. B={2,4},f{1,3,5}. B can't pick 5. B loses. So A picks 6 → B loses.
  B picks 3: B={3},f{2,4}. Avail{2,4,5,6}. A={1},f{2}. A picks 4,5,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{2,4,5}. B={3},f{2,4}. B picks 5. B={3,5},f{2,4,6}. Avail{2,4}. A={1,6},f{2,5,7}. A picks 4. A={1,4,6},f{2,3,5,7}. Avail{2}. B={3,5},f{2,4,6}. B can't pick 2. B loses. So A picks 6 → B loses.
  B picks 2: B={2},f{1,3}. Avail{3,4,5,6}. A={1},f{2}. A picks 3,4,5,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{3,4,5}. B={2},f{1,3}. B picks 4 or 5.
      B picks 4: B={2,4},f{1,3,5}. Avail{3,5}. A={1,6},f{2,5,7}. A picks 3. A={1,3,6},f{2,4,5,7}. Avail{5}. B={2,4},f{1,3,5}. B can't. B loses.
      B picks 5: B={2,5},f{1,3,4,6}. Avail{3,4}. A={1,6},f{2,5,7}. A picks 3 or 4. A picks 3: A={1,3,6}. Avail{4}. B={2,5},f{1,3,4,6}. B can't pick 4. B loses. A picks 4: A={1,4,6}. Avail{3}. B can't pick 3. B loses.
    So A picks 6 → B loses.
  So after A picks 1, every B response either draws (B picks 6) or loses for B (B picks 2,3,4,5). So B's best is pick 6 → draw. So A picks 1 → draw.

Now I should check A's other first moves to ensure A can't WIN (force B to lose). If A could win with some first move, n=6 would be "A wins" not draw. Code says draw, so A's best is draw (can't win). Let me trust that. Actually let me verify A can't win: A picks 2,3 etc. need B to have a drawing response. This is a lot. I'll trust the code.

OK so the pattern holds. Now I need to PROVE it.

The answer: 
- Draw for n = 1, 2, 4, 6.
- B wins for n = 3, 5, and n ≥ 7.

Hmm, this is a somewhat irregular answer. Let me reconsider if maybe I'm wrong about n=6 or n=8. Let me re-examine by re-running with a sanity check / different method for n=6 and n=8.

Actually the code is straightforward negamax, I trust it. Let me also verify n=5 B wins and n=4 draw by hand (done n=4, n=5 partially). And n=3 B wins (done). Good.

Now, the proof. This is the hard part. Let me think about how to prove B wins for n ≥ 7 and draw for {1,2,4,6}.

Let me think about a clean strategy for B for n ≥ 7.

Let me look at the traces more to find B's strategy pattern.

n=7 traces (B's moves):
A=1: B=7,3→2,5→4. (B:7,2,4)
A=2: B=1,4→3,6→5. (B:1,3,5)
A=3: B=1,5→4,7→6. (B:1,4,6)
A=4: B=1,2→3,6→5. (B:1,3,5)
A=5: B=1,2→3,7→6. (B:1,3,6)
A=6: B=1,2→3,4→5. (B:1,3,5)
A=7: B=1,2→3,4→5. (B:1,3,5)

Hmm, for A=2,3,4,5,6,7 B's first move is 1. For A=1, B's first move is 7.

Let me see: when A picks a (a≠1), B picks 1. Then A's f includes a±1. 

This is getting complicated. Let me think about a higher-level strategy.

Alternative approach: Let me think about the problem as a known competition problem. The answer "draw for n∈{1,2,4,6}, B wins otherwise" — let me see if this matches a known result. Actually this looks like it could be ISL 2018 C8 or similar. Let me think...

Actually, let me reconsider. Let me reconsider the possibility that the answer is cleaner and I have an off-by-one. Let me re-examine n=6 super carefully with the code by printing the full game value and also checking n=6 with A picking each first move and the value.

Let me also extend the computation with a more efficient approach (symmetry + memo) to confirm n=10,12,14 are B wins (already have up to 18). I'm confident.

Hmm, the irregular answer {1,2,4,6} is suspicious. Let me reconsider: maybe the intended answer is "B wins for all n ≥ 3" and my n=4,6 are wrong? But I hand-verified n=4 draw and n=6 draw (A picks 1 → draw). Let me re-examine n=6: is there an A first move that wins for A, or does B have a winning response to every A move? I showed A picks 1 → draw (B can't win, A can't win). For n=6 to be "B wins", B would need to win against every A first move. But A picks 1 → draw at best for B. So n=6 is NOT B wins. And A can't win either (need to verify but trust code). So n=6 draw. Confirmed.

So the answer really is irregular. Let me reconsider—maybe the problem is from a specific competition and the answer is indeed this irregular set. Let me search memory: This looks like IMO 2018 Shortlist C4 or similar... Actually the problem statement "Let n be a positive integer. Two players A and B play a game..." with these exact rules — I recall this might be from IMO Shortlist 2017 C6 or 2018. The answer might indeed be "B wins for n≥3 except n=4,6" or similar. Hmm.

Actually, wait. Let me reconsider. Let me re-examine: maybe the answer is "A wins" for some n? The code never says A wins. Let me check larger... all B wins or draw. So A never wins. That makes sense by strategy-stealing-ish reasoning? Not obviously.

Let me reconsider the draw cases. n=1: trivial draw. n=2: draw. n=4: draw. n=6: draw. And B wins for n=3,5,7,8,9,... So for n≥7 always B wins.

Let me reconsider: is it possible that for very large even n, it becomes draw again? The code confirms B wins up to 18. I'll conjecture B wins for all n≥7.

Now I need to construct B's winning strategy for n≥7 and drawing strategies for {1,2,4,6}, plus B's wins for {3,5}.

This is a hard proof. Let me think about a clean strategy for B for n ≥ 7.

Let me think about the structure. The crucial fact: a draw requires the final position to be the parity partition (A=odds, B=evens, or swapped). 

B's winning idea: B will make a move that "breaks" the parity partition in a way that leaves A stuck.

Let me think about a specific clean strategy. Consider B adopting the following: B always responds to keep the game within a "trap."

Let me think about the traces for n=7 again, specifically A=1: B=7 (mirror), then A forced to 3 (only non-forbidden available: avail{2,3,4,5,6}, A f{2}, so A can pick 3,4,5,6 — not forced!). Wait A picked 3 in the trace but could pick 4,5,6. The trace follows optimal A (which still loses). Let me see all A options after A=1,B=7.

Hmm, the trace just shows one optimal line. Let me get the full picture: for n=7, A=1,B=7, what are A's options and B's responses.

This is getting really involved. Let me step back and think about whether there's a clean structural strategy.

Clean strategy idea for B (n ≥ 7): 

Reflection strategy with a twist. Let me consider the reflection pairing (i, n+1-i). B mirrors A. As shown, for even n this keeps B legal and B never stuck. But does it make A stuck? For n=4,6 it leads to draw (A not stuck if A plays well). For n≥8, does mirror make A stuck?

Earlier for n=8, A=1,B=8,A=3,B=6,A=5,B=4,A=7,B=2 → draw (all chosen). So pure mirror → draw for n=8, but B can do better (win). So mirror is not B's winning strategy for n=8.

So B needs a different strategy. Let me look at B's actual winning strategy for n=8, A=1: B=8, then A=3 (optimal A), B=5 (not mirror of 3 which is 6!). So B deviates from mirror at move 2.

n=8, A=1,B=8,A=3,B=5: B picked 5 instead of 6. Then A=6,B=2, A stuck.
A={1,3,6}, B={8,5,2}. Remaining{4,7}. A's f from {1,3,6}: {2,4,5,7}. 4,7 both in f. Stuck.

Interesting. So B's strategy: after A=1,B=8,A=3, B plays 5 (not 6). Why 5? This blocks A from taking 6's neighbor... hmm. Actually B taking 5 means A can later take 6 (6 not adjacent to A's {1,3}). A takes 6, then A's set {1,3,6} blocks 4,5,7. Remaining after B=2: {4,7} both blocked.

Let me think about this as B setting a trap. This is quite intricate. 

Given the complexity, maybe the cleanest proof approach is:

1. Establish the parity-partition characterization of draws.
2. For n ∈ {1,2,4,6}: exhibit explicit drawing strategies (or just verify small cases).
3. For n=3,5: explicit B winning strategies.
4. For n ≥ 7: give a general B winning strategy.

For part 4, I need a clean general strategy. Let me think harder.

Let me think about n ≥ 7 and try to find a uniform strategy. Let me consider B's strategy based on reducing to a smaller game.

Idea: B's first move creates a situation that splits the board into independent components, and B can mirror within components.

When a number k is taken (by anyone), it doesn't split the board for the adjacency constraint directly, because the constraint is about a player's OWN set, not all taken numbers. Hmm, but availability is global.

Let me reconsider. The "available" numbers shrink globally. A player's legal moves = available numbers not adjacent to their own set.

Let me think about the endgame condition for A getting stuck. A is stuck when every available number is adjacent to some number in A's set. I.e., A's set is a dominating set of the available numbers (in the path). 

For A to be stuck with remaining numbers R (available), A's set must dominate R: every r in R has a neighbor in A's set.

B wants to engineer: after B's move, the remaining available R is dominated by A's set, and it's A's turn.

Conversely B must avoid being in the symmetric situation.

This is a complex combinatorial game. Given the difficulty, let me reconsider whether the intended answer might actually be simpler and I should re-examine.

Wait, actually, let me reconsider the problem. Let me re-read: "determine the outcome of the game." Maybe the answer is meant to be piecewise and the proof uses the parity-partition insight plus casework. Competition problems can have piecewise answers.

Let me reconsider: maybe the answer is "B wins for n ≥ 3 except n = 4, 6" — i.e., draw for n=1,2,4,6 and B wins otherwise. Let me see if this is a known problem. 

Actually I now recall: this is IMO 2018 Shortlist C4 (or C5). Let me recall the answer... I think the answer for this problem is: "B wins for n ≥ 3, except n = 4 and n = 6 where it's a draw." Hmm, or maybe the answer involves n mod something.

Actually, let me just go with the computed answer and construct a proof. Given the complexity of a fully general strategy for n≥7, let me think about a clean inductive or structural strategy.

Let me reconsider the traces to find a pattern for B's strategy for general n≥7.

Let me get traces for n=9,10,11 to see the pattern.
Now I see a clear pattern for B's strategy when A picks 1 (or generally picks an endpoint-ish number).

For n=9, A=1: B=9, A=3, B=2, A=5, B=4, A=7, B=6, A stuck. 
A's picks: 1,3,5,7 (arithmetic progression, all odd!). B's picks: 9,2,4,6. Remaining: 8. A's f from {1,3,5,7}: {2,4,6,8}. 8 blocked. Stuck.

For n=11, A=1: B=11, A=3, B=2, A=5, B=4, A=7, B=6, A=9, B=8, A stuck.
A: 1,3,5,7,9. B: 11,2,4,6,8. Remaining: 10. A's f: {2,4,6,8,10}. 10 blocked. Stuck.

So for odd n, A=1: B=n, then A forced into 3,5,7,... (A picks all odd numbers 1,3,5,...,n-2), B picks n,2,4,6,...,n-1. Wait B picks n first then 2,4,6,...? B: 11,2,4,6,8 for n=11. So B picks n (odd) then evens 2,4,6,8. Remaining 10 (even). A={1,3,5,7,9}, f={2,4,6,8,10}. 10 blocked. A stuck.

But wait, is A forced to pick 3,5,7,9? After A=1,B=11: avail{2,3,4,5,6,7,8,9,10}, A f{2}. A can pick 3,4,5,6,7,8,9,10. A picked 3 (optimal). But could A pick something else to avoid the trap? The trace shows optimal A still loses, but via this line. Let me check: the trace follows optimal play meaning A picks the move that maximizes A's outcome; all lead to loss, so it picks the first found (3). But A might have other losing lines. The point is B has a winning strategy regardless.

Let me understand B's strategy for the line A=1:
- B picks n (the far endpoint).
- Then whatever A picks, B responds to keep A trapped.

Actually in the n=9,11 traces, after B=n, A picks 3, then B picks 2, A picks 5, B picks 4, ... So B picks the number just below A's pick (A picks 3, B picks 2; A picks 5, B picks 4; etc.). And A keeps picking the next odd number.

Why does A pick 3 then 5 then 7? Because after B picks 2, A's f={2} (from A's 1) ∪ ... A={1}, f={2}. After A picks 3, A={1,3}, f={2,4}. B picks 2. Now avail excludes 1,3,11,2. A's turn, f={2,4}. Available: 4,5,6,7,8,9,10. A can't pick 4. A picks 5 (or 6,7,8,9,10). A picks 5. A={1,3,5},f={2,4,6}. B picks 4. Avail: 6,7,8,9,10. A can't pick 6. A picks 7. Etc.

So A is being pushed: each time A picks the smallest available non-forbidden, which is the next odd. And B picks the even just below. This continues until A picks n-2 (odd), B picks n-3? Wait for n=9: A picks 7, B picks 6, then remaining 8, A f includes 8 (from 7). Stuck. For n=11: A picks 9, B picks 8, remaining 10, A f includes 10 (from 9). Stuck.

So the trap: A is forced along odds 1,3,5,...,n-2, B takes n and evens 2,4,...,n-3, and the last even n-1 remains but A's n-2 blocks it.

But this requires A to cooperate by picking 3,5,7,... What if A deviates, e.g., after A=1,B=9, A picks 5 instead of 3? Let me check B's response. The trace shows A's optimal (which still loses). B must have responses to all A deviations. Let me check by computing B's best response for n=9 after A=1,B=9,A=5.

Actually, the key question for the proof: does B have a uniform strategy? Let me think about it as: B's strategy is "reflection around the center" but with the center handled, OR B's strategy is "always play adjacent to A's last move on the side toward the center" or something.

Hmm, let me look at the n=9, A=1 line: B=9 (reflection of 1). Then A=3, B=2 (NOT reflection of 3=7). So B switches strategy. After B=9, the remaining board is {2,3,...,8} (a path of length 7, numbers 2..8). B's move 2 in response to A's 3... 

Actually, here's a cleaner idea: After A picks 1 and B picks n, the remaining available numbers are {2,3,...,n-1}, which is a path of length n-2. Now it's A's turn, A's set={1}, so A is forbidden from 2. Effectively A can't use 2. 

Hmm, let me think recursively. The sub-game on {2,...,n-1} with A forbidden at 2 (because A owns 1) and B forbidden at n-1 (because B owns n). 

This is like the original game but with both endpoints blocked for the respective players. 

Let me define a more general game: a path of consecutive integers [a, b], where A has a "forbidden zone" near a (owns a-1 or a is blocked) and B near b. Hmm, this is getting complicated.

Let me think about a cleaner inductive strategy.

Conjecture/Strategy for B (n ≥ 7): 
B's strategy: "Reflect A's move across the center; if A plays the center (only when n odd), B plays 1 (or some fixed move)."

Wait, but we saw for n=8 (even), B does NOT always reflect (A=1,B=8 reflect; A=3,B=5 not reflect of 3=6). So reflection isn't the strategy for even n≥8.

Let me look at n=8, A=1: B=8, A=3, B=5, A=6, B=2. 
After A=1,B=8: remaining {2,3,4,5,6,7}. A=3. B=5. Why 5? 
After A=3: A={1,3}, f={2,4}. Available {2,4,5,6,7}. A can't take 2,4. B's turn, B={8}, f={7}. B can take 2,3,4,5,6 (3 taken). B takes 5. 
Then A's turn: A={1,3},f={2,4}. Avail{2,4,6,7}. A can take 6 or 7. A takes 6 (optimal). A={1,3,6},f={2,4,5,7}. Avail{2,4,7}. B={8,5},f={4,6,7}. B can take 2. B=2. Avail{4,7}. A f{2,4,5,7} → 4,7 blocked. Stuck.

Alternatively A takes 7 instead of 6: A={1,3,7},f={2,4,6,8}. Avail{2,4,6}. B={8,5},f{4,6,7}. B takes 2. Avail{4,6}. A f{2,4,6,8}→4,6 blocked. Stuck. So either way A stuck.

So B's strategy after A=1,B=8,A=3 is B=5. The idea: B takes 5 to "split" and then A is forced into a trap.

This is genuinely intricate. I think reproducing the exact optimal strategy in a proof is hard. Let me think about whether there's a cleaner high-level argument.

Let me reconsider the parity-partition insight, which is the cleanest structural fact:

**Fact**: A draw occurs iff the final position is a 2-coloring of the path, i.e., one player has all odds and the other all evens. (Because the path's only proper 2-colorings are the parity coloring.)

Now, here's a cleaner way to think about who wins:

Consider the parities. A moves on odd turns (1st, 3rd, 5th, ...). 

Hmm, let me think about a potential function or a "pairing" that B uses.

Alternative clean strategy for B for n ≥ 7: 

Let me consider B playing to force A to take consecutive-ish positions. 

Actually, let me reconsider. Let me think about the following B strategy for ALL n ≥ 3:

B's strategy: After A's first move a, B plays to set up a "trap." 

This is really a casework-heavy problem. Given that this is a competition problem with an irregular answer {1,2,4,6}, the official solution likely does significant casework. Let me try to find the cleanest proof I can.

Let me reconsider the structure. Let me think about the game in terms of "gaps."

Actually, let me reconsider the parity argument more carefully, because I think it's the key to a clean proof.

**Parity Lemma**: The game is a draw iff the final sets are {odds} and {evens}. 

Now, consider this: A moves first. Suppose A wants a draw. Then A must end up with exactly the odds (or evens). 

Consider B's strategy: B will "steal" one number of each... no.

Let me think about it as: B wants to force A to take two numbers of the same parity that are "too close" or force A to take a number that blocks A's own future required numbers.

Hmm. Let me think about a specific clean strategy for B for n ≥ 7, then handle n=3,5 separately, and draws separately.

Let me look at the strategy for n=9,11 (odd, A=1): B plays n, then "just below A's move." Specifically, after A plays x (an odd number going up), B plays x-1. This pushes A up the odds. Let me verify this is a valid general strategy for odd n ≥ 7.

B's strategy for odd n ≥ 7 (against A=1, but need general A):
Actually let me focus on a general strategy. Let me consider:

**B's Strategy S (for n ≥ 7)**: 
- If A's first move a ≤ (n+1)/2, B plays n. Then B continues with strategy: whenever A plays x, B plays x-1 if available and legal, else x+1, else some default.

Hmm, this is ad hoc. Let me think more carefully and verify with the traces.

For n=9, A=1: B=9. A=3,B=2(=3-1). A=5,B=4(=5-1). A=7,B=6(=7-1). Yes "play x-1."
For n=11, A=1: B=11. A=3,B=2. A=5,B=4. A=7,B=6. A=9,B=8. Yes "play x-1."

For n=7, A=1: B=7. A=3,B=2(=3-1). A=5,B=4(=5-1). Yes.

For n=8, A=1: B=8. A=3, B=5 (NOT 3-1=2!). So the strategy differs for even n. Hmm.

Wait, for n=8, after A=1,B=8,A=3: if B played 2 (=3-1), then A={1,3},f{2,4}, avail{2,4,5,6,7}, B={8,2},f{1,3,7}. A's turn: avail{4,5,6,7}, A f{2,4}. A picks 5 or 6 or 7. If A picks 5: A={1,3,5},f{2,4,6}. avail{4,6,7}. B={8,2},f{1,3,7}. B picks 4 or 6. B picks 6: B={8,2,6},f{1,3,5,7}. avail{4,7}. A f{2,4,6}→4 blocked, 7? 7 not in A's f{2,4,6}. A picks 7! A={1,3,5,7},f{2,4,6,8}. avail{4}. B={8,2,6},f{1,3,5,7}. B can't pick 4? 4 not in B's f. B picks 4. All chosen → draw! 

So if B plays 2 (x-1 strategy) for n=8, A can force draw. That's why B plays 5 instead. So the "play x-1" strategy works for odd n but not even n.

So odd and even n need different strategies. For odd n ≥ 7, "B plays n then x-1" seems to work (when A starts at 1). But I need it to work for any A first move, and need to verify A can't deviate.

Let me check: for odd n, A=1, B=n, then B plays x-1. Does A have a deviation that escapes? Let me check n=9, A=1,B=9, A deviates to 5 (instead of 3).

n=9, A=1,B=9,A=5: A={1,5},f{2,4,6}. avail{2,3,4,6,7,8}. B={9},f{8}. B's strategy "play x-1" → B plays 4. B={9,4},f{3,5,8}. avail{2,3,6,7,8}. A's turn, f{2,4,6}. A can pick 3,7,8. 
  A picks 7: A={1,5,7},f{2,4,6,8}. avail{2,3,6,8}. B={9,4},f{3,5,8}. B plays x-1=6. B={9,4,6},f{3,5,7,8}. avail{2,3,8}. A f{2,4,6,8}. A can pick 3. A={1,5,7,3}={1,3,5,7},f{2,4,6,8}. avail{2,8}. B={9,4,6},f{3,5,7,8}. B plays x-1=2. B={9,4,6,2},f{1,3,5,7,8}. avail{8}. A f{2,4,6,8}→8 blocked. A stuck! 
  A picks 8: A={1,5,8},f{2,4,6,7,9}. avail{2,3,6,7}. B={9,4},f{3,5,8}. B plays x-1=7. B={9,4,7},f{3,5,6,8}. avail{2,3,6}. A f{2,4,6,7,9}. A can pick 3. A={1,5,8,3},f{2,4,6,7,9}. avail{2,6}. B={9,4,7},f{3,5,6,8}. B plays x-1=2. B={9,4,7,2},f{1,3,5,6,8}. avail{6}. A f{2,4,6,...}→6 blocked. A stuck!
  A picks 3: A={1,5,3}={1,3,5},f{2,4,6}. avail{2,6,7,8}. B={9,4},f{3,5,8}. B plays x-1=2. avail{6,7,8}. A f{2,4,6}. A picks 7 or 8. A picks 7: A={1,3,5,7},f{2,4,6,8}. avail{6,8}. B={9,4,2},f{1,3,5,8}. B plays x-1=6. avail{8}. A f{2,4,6,8}→8 blocked. stuck. A picks 8: A={1,3,5,8},f{2,4,6,7,9}. avail{6,7}. B={9,4,2},f{1,3,5,8}. B plays x-1=7. avail{6}. A f{2,4,6,...}→6 blocked. stuck.

So for n=9, A=1,B=9, A=5 deviation, B's "play x-1" strategy still traps A. 

So the strategy "B plays n, then always x-1 (A's last move minus 1)" seems robust for odd n. But I need to verify B's moves are always legal (x-1 available and not adjacent to B's set).

B's set after playing n and then x-1's: B's set = {n} ∪ {x_i - 1}. The x_i are A's moves (after the first). A's moves x_i: A's set is independent, and includes 1 (first) and then x_2, x_3, ... B plays x_i - 1.

Is x_i - 1 available? x_i - 1 could be taken by A (if A picked x_i - 1) — but A's set is independent, A has x_i, so A doesn't have x_i - 1 (consecutive, forbidden). Could x_i-1 be taken by B already? B has {n} and {x_j - 1 : j < i}. x_i - 1 = x_j - 1 → x_i = x_j, no. x_i - 1 = n → x_i = n+1, impossible. So x_i - 1 not taken by B. Could be taken by A? Only if A picked it, but A can't pick x_i-1 (adjacent to x_i) — but A might have picked x_i-1 BEFORE picking x_i? No: if A picked x_i-1 earlier, then A's set has x_i-1, so A can't pick x_i now (adjacent). Contradiction. So x_i-1 not in A's set. So x_i-1 is available. 

Is x_i-1 legal for B (not adjacent to B's set)? B's set = {n, x_2-1, x_3-1, ...}. B needs x_i-1 not adjacent to any of these. x_i-1 adjacent to x_j-1 iff x_i adjacent to x_j. A's set is independent, so x_i, x_j not adjacent (for i≠j, both in A's set). So x_i-1, x_j-1 not adjacent. Good. x_i-1 adjacent to n iff x_i-1 = n±1, i.e., x_i = n or n+2. x_i ≤ n, so x_i = n. But n is taken by B (B's first move), so A can't pick n. So x_i ≠ n. So x_i-1 not adjacent to n. 

So B's move x_i-1 is always legal and available. So B can always execute "play x-1" after the first move (where B played n).

Now, does this strategy guarantee A gets stuck? Let me think about the end. A's first move is 1 (we're analyzing this case). Then A picks x_2, x_3, .... B picks n, x_2-1, x_3-1, ....

A's set: {1, x_2, x_3, ...}. A's forbidden set (neighbors): {0,2} ∪ {x_i ± 1}. Since 0 not in range, A's forbidden = {2} ∪ {x_i - 1, x_i + 1}.

Note B took x_i - 1 for each i. So A's forbidden includes x_i + 1 and 2 (and x_i - 1 which B took anyway).

The game ends when A can't move. A can move if there's an available number not in A's forbidden set.

Total numbers: n. A takes ceil... let me count moves. A moves: 1, x_2, x_3, ..., x_k (k moves). B moves: n, x_2-1, ..., x_k-1 (k moves). Total 2k numbers taken. Remaining n - 2k.

For A to be stuck on move k+1: all remaining numbers are in A's forbidden set.

Hmm, let me think about when A "runs out." A's available non-forbidden numbers. Initially after B plays n, A can pick from {2,...,n-1} minus {2} (forbidden) = {3,4,...,n-1}. A picks x_2. Then B picks x_2-1. A's forbidden grows by {x_2-1, x_2+1}. Available shrinks.

Let me think about the "frontier." This is like A is exploring and B blocks just behind.

Actually, let me think about the total count. A and B each make k moves, 2k total. The game ends with A stuck when remaining = n - 2k > 0 and all remaining are A-forbidden.

A's forbidden numbers (within [1,n]): neighbors of A's set. A's set = {1, x_2, ..., x_k}. These are k independent numbers. Their neighbors: each a in A's set contributes a-1, a+1 (within range). Total distinct forbidden ≤ 2k (but overlaps possible). Plus A's own numbers are taken (not available anyway).

Numbers not available = A's set ∪ B's set = 2k numbers. Numbers available = n - 2k. A is stuck iff available ⊆ forbidden(A).

Forbidden(A) ⊆ [1,n] \ A's set (since A's set is independent, neighbors aren't in A's set). |forbidden(A)| ≤ 2k. Available = n - 2k. 

Hmm, this counting doesn't immediately give stuck.

Let me think about it differently for the specific strategy. Let me reconsider: with B playing x_i - 1, B's set = {n, x_2-1, ..., x_k-1}. 

Let me think about which numbers are NOT taken and NOT forbidden for A. A number y is "playable by A" if y not taken and y not adjacent to A's set.

y taken: y ∈ A's set ∪ B's set.
y adjacent to A's set: y = a±1 for some a in A's set.

A is stuck iff no playable y.

Let me think about the structure of A's set under this strategy. A picks 1, then must pick from numbers not adjacent to 1 and not taken. After B takes n and x_2-1, etc.

This is getting complicated. Let me just verify the strategy works for odd n ≥ 7 by a cleaner argument, and check even n separately.

Actually, let me reconsider. Maybe there's a much cleaner unified strategy. Let me look at even n traces again.

n=8, A=1: B=8, A=3, B=5, A=6, B=2. 
n=10, A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4.
Hmm n=10: B=10, then A=3,B=2 (x-1!), A=5,B=7 (NOT x-1=4!). 

Wait n=10 A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4. Let me re-examine. After B=10,A=3,B=2: A={1,3},f{2,4}. avail{4,5,6,7,8,9}. A picks 5. A={1,3,5},f{2,4,6}. B={10,2},f{1,3,9}. avail{4,6,7,8,9}. B picks 7. Why 7? Then A={1,3,5},f{2,4,6}, avail{4,6,8,9}. A picks 8 (not in f). A={1,3,5,8},f{2,4,6,7,9}. avail{4,6,9}. B={10,2,7},f{1,3,6,8,9}. B picks 4. avail{6,9}. A f{2,4,6,7,9}→6,9 blocked. stuck.

Hmm so for n=10, B's strategy is more complex. The "x-1" doesn't uniformly apply.

This is getting really messy for a clean proof. Let me step back and think about whether there's a fundamentally cleaner approach.

Let me reconsider the parity partition insight and think about a strategy based on parity directly.

**Key Insight (Parity)**: A draw requires A to hold exactly one parity class and B the other. 

Now, here's a strategy idea for B: B ensures that A is forced to take a number that "collides" with the parity requirement, OR B takes a number of A's parity to break the draw, while maintaining a position where A gets stuck.

Hmm. Let me think about a "strategy stealing" or "Tweedledum" type argument.

Actually, let me reconsider. Let me think about B's strategy as: B always takes a number of the OPPOSITE parity to A's last move, adjacent to it. I.e., when A takes x, B takes x-1 or x+1 (opposite parity, adjacent). This is legal for B (B's set: are x_i ± 1 mutually non-adjacent? (x_i+1) and (x_j+1) adjacent iff x_i, x_j adjacent — no since A independent. (x_i+1) and (x_j-1) adjacent iff x_i+1 = x_j-1±1, i.e., x_i = x_j - 2 or x_i = x_j. If x_i = x_j - 2, then x_i, x_j differ by 2, not adjacent, allowed in A's set. Then x_i+1 = x_j - 1, so B would have x_i+1 and x_j-1 = same number! Conflict. Hmm.)

So B taking x±1 has conflicts. The "x-1" strategy avoids this (always x-1, no ±1 mixing).

Let me reconsider the "x-1" strategy for odd n and figure out the clean proof that A gets stuck.

**Odd n ≥ 7, B's strategy: B plays n first (in response to A's first move 1), then always plays (A's last move) − 1.**

Wait, but this assumes A's first move is 1. I need a strategy for any A first move. Let me handle general A first move for odd n.

By the traces, for odd n, when A's first move a ≠ 1, B plays 1. Let me look:
n=7, A=2: B=1. A=4,B=3,A=6,B=5. So B=1, then B plays x-1 (A=4→B=3, A=6→B=5). 
n=9, A=2: B=1. A=4,B=3,A=6,B=5,A=8,B=7. B plays x-1.
n=9, A=3: B=1. A=5,B=4,A=7,B=6,A=9,B=8. B plays x-1.

So for odd n, B's strategy: 
- If A's first move a is "small" (a ≤ center?), B plays n; if a is large, B plays 1? Let me check. n=7: A=1→B=7, A=2→B=1, A=3→B=1, A=4→B=1, A=5→B=1, A=6→B=1, A=7→B=1. Hmm, only A=1 gives B=7; all others B=1. That's strange. Let me check n=9: A=1→B=9, A=2→B=1, A=3→B=1. (only checked 1,2,3). 

Wait, that's asymmetric. For A=1, B=9 (the far end). For A=2, B=1 (the near end). Let me check A=5 (center) for n=9.

Let me get more traces for odd n with various A first moves to understand B's first response.
Interesting! For odd n, B's first response: if A picks 1, B picks n; otherwise B picks 1. (By symmetry, if A picks n, B should pick 1 — yes. And if A picks 1, B picks n. So B "completes the endpoint pair": B picks the endpoint far from A, unless A picked 1 in which case B picks n... wait that's the same. B picks the OPPOSITE endpoint. If A picks 1, B picks n. If A picks anything else (including n), B picks 1.)

Hmm, actually: A=1→B=n; A=n→B=1; A=other→B=1. So B picks 1 unless A picked 1 (then B picks n). Equivalently: B picks an endpoint (1 or n) different from A's move if A picked an endpoint; if A didn't pick an endpoint, B picks 1.

Actually simpler: B always picks 1, unless A picked 1 (then B picks n). I.e., B picks the smallest available endpoint, preferring 1.

Wait, but why not symmetric? If A picks n, B picks 1 (not n-1 or something). And if A picks 1, B picks n. So B picks the endpoint NOT chosen by A, when A chose an endpoint; and picks 1 when A chose an interior point.

Hmm, actually it's: B picks 1 if available, else n. Since if A picked 1, then 1 not available, B picks n. If A picked anything else, 1 is available, B picks 1. That's the rule! "B picks 1 if available, otherwise n."

Let me verify: A=1→1 not available→B=n. ✓. A=2→1 available→B=1. ✓. A=n→1 available→B=1. ✓.

So B's first move: pick 1 if available, else n. I.e., B grabs the leftmost endpoint (or rightmost if leftmost is taken).

Then subsequent: B plays x-1 (A's last move minus 1). Let me verify this holds for the case A=2,B=1 for odd n.

n=9, A=2, B=1: A={2},f{1,3}. avail{3,4,5,6,7,8,9}. B={1},f{2}. A's turn. A picks 4 (optimal, from trace). A={2,4},f{1,3,5}. B plays x-1=3. B={1,3},f{2,4}. avail{5,6,7,8,9}. A picks 6. A={2,4,6},f{1,3,5,7}. B plays x-1=5. avail{7,8,9}. A picks 8. A={2,4,6,8},f{1,3,5,7,9}. B plays x-1=7. avail{9}. A f{1,3,5,7,9}→9 blocked. stuck! 

So B's strategy for odd n ≥ 7: 
1. First move: pick 1 if available, else n.
2. Subsequent: pick (A's last move) − 1.

Let me verify legality of "x-1" in this context. B's set = {first} ∪ {x_i - 1}. Need x_i - 1 available and not adjacent to B's set.

Available: x_i - 1 not in A's set (A has x_i, independent, so A doesn't have x_i-1). Not in B's set: B has {first, x_j-1 for j<i}. x_i-1 = x_j-1 → x_i=x_j no. x_i-1 = first. first is 1 or n. If first=1: x_i-1=1→x_i=2. But if A picked 2 as first move, then B picked 1 (first). Then later A picks x_i=2? No, A already picked 2 as FIRST move. The x_i here are A's moves AFTER the first. So x_i ≠ 2 (A's first was 2, can't repeat). Hmm wait, actually in this branch A's first move is 2, B's first is 1. Then A's subsequent moves x_2, x_3,.... Could x_i = 2? No, 2 already taken by A. So x_i ≠ 2, so x_i - 1 ≠ 1 = first. Good. If first = n (this happens when A's first move is 1): x_i - 1 = n → x_i = n+1, impossible. Good.

Not adjacent to B's set: x_i-1 adjacent to x_j-1 iff x_i,x_j adjacent — no (A independent). x_i-1 adjacent to first(=1): x_i-1=2 → x_i=3. first=1, adjacent to 2. So if x_i=3, then x_i-1=2 is adjacent to B's 1. Illegal! 

Hmm. So when first=1 (A's first move ≠ 1), and A later picks 3, B can't play 2 (adjacent to B's 1). Let me check the trace: n=9, A=2,B=1. Did A ever pick 3? A picked 4,6,8 (evens). A's first was 2 (even), and A continued with evens. So A never picked 3 in that line. But could A deviate to pick 3?

A=2 (first), B=1. A={2},f{1,3}. avail{3,...,9}. A can't pick 3 (forbidden, adjacent to A's 2). So A can't pick 3! Great. So x_i=3 never happens because A's first move 2 blocks 3 for A.

More generally: if A's first move is a, A is forbidden from a-1, a+1. B's first move is 1 (when a≠1). B's set has 1, so B can't play 2 (adjacent to 1). B wants to play x-1; conflict only if x-1=2, i.e., x=3. Is A ever able to pick 3? A is forbidden from a±1. If a=2, A forbidden 1,3 → can't pick 3. If a=3, A forbidden 2,4 → can pick 3? No, 3 is A's first move (a=3), already taken. If a=4, A forbidden 3,5 → can't pick 3. If a≥4, A forbidden a-1,a+1; 3 is forbidden only if a=2 or 4. For a=5: A forbidden 4,6; 3 not forbidden, 3 available (not taken). So A could pick 3 later! Then B wants to play 2, but 2 adjacent to B's 1. Illegal.

Let me check: n=9, A=5 (first), B=1. A={5},f{4,6}. avail{2,3,4,6,7,8,9}. A's turn. Could A pick 3? 3 available, not in f. Yes A could pick 3. Then B's "x-1"=2, but 2 adjacent to B's 1 → illegal. So the strategy breaks?

Let me check the actual trace for n=9, A=5.
Now I see the pattern clearly for odd n. Let me analyze.

For odd n, B's strategy:
- First move: pick 1 if available, else n (i.e., pick 1 unless A took 1, then pick n).
- Then: B plays (A's last move) − 1.

Let me verify the "x-1" legality concern I raised. When A's first move a ≠ 1, B plays 1. Then A's subsequent moves. The concern was A picking 3 (so B plays 2, adjacent to B's 1). But looking at traces, when a ≠ 1, A's second move is never 3. Let me see why.

When a ≠ 1, B=1. A's set={a}, A forbidden {a-1,a+1}. A's second move options: available numbers in {2,...,n}\{a} not in {a-1,a+1}. 

In the traces, A's second move: 
- a=2: A picks 4 (not 3, since 3 forbidden). 
- a=3: A picks 5 (4 forbidden). 
- a=4: A picks 2 (3,5 forbidden; picks 2). 
- a=5: A picks 2 (4,6 forbidden; picks 2). 
- a=6: A picks 2.
- a=7: A picks 2.
- a=8: A picks 2.
- a=9: A picks 2.

So A's second move is never 3 when a≠1. But that's the OPTIMAL A. A could deviate and pick 3 (if legal). When is 3 legal for A's second move? 3 must be available (not taken: taken are {a, 1}; so 3 available iff a≠3) and not in A's forbidden {a-1,a+1} (so a≠2 and a≠4). So for a ≥ 5 (a≠3), 3 is available and not forbidden. So A could pick 3 as second move when a ≥ 5!

E.g., n=9, a=5, B=1. A could pick 3 (available, not forbidden since A forbidden {4,6}). Then B's "x-1" = 2, adjacent to B's 1 → ILLEGAL.

So the "x-1" strategy as stated doesn't work if A deviates. But the minimax says B still wins. So B must have a different response to A's deviation. The trace only shows the optimal A line (which avoids 3). I need to check B's response to A=5,B=1,A=3.

Let me check that specific line.
The strategy "B first plays 1 (or n if 1 taken), then plays x-1 if legal else x+1" works for n=9 against optimal A (A always gets stuck). But "optimal A" here means A plays to maximize its own outcome given B's fixed strategy. Since A always gets stuck, B's strategy is winning. But I should test against ALL A deviations, not just optimal. The minimax with B's fixed strategy and A optimal captures the worst case for B (A tries hardest to escape). If A still gets stuck in all lines, B's strategy wins. The trace shows one line per A-first-move, but A is playing optimally against B's strategy, so if A could escape, the trace would show escape (draw or A win). All show A stuck. 

But wait, "optimal A" against a FIXED B strategy: A plays to maximize A's outcome assuming B follows the fixed strategy. If the result is always "A stuck" (A loses), then B's strategy is winning. Yes. But I should double-check the code: when A is "optimal", it uses bestmove which uses `value` — but `value` assumes BOTH play optimally, not B-follows-fixed-strategy! That's a bug. The `value` function computes minimax with both optimal, so A's "bestmove" is the minimax best, NOT the best against B's fixed strategy.

So this test is flawed: A's moves are minimax-optimal (assuming B also optimal), not optimal-against-B's-fixed-strategy. So the traces just reproduce the minimax lines (which is why they match the earlier traces). This doesn't validate B's fixed strategy against A deviations.

I need to properly test B's fixed strategy against A's best response to THAT strategy. Let me write a proper tester: A plays optimally against B's fixed strategy (A does minimax assuming B follows fixed strategy).

Let me write that.
The strategy fails (returns None) in some case, causing ERROR. Let me handle the ERROR and report where B's strategy is illegal. Let me also make bstrat return a fallback so I can see if the strategy itself is sometimes illegal.

Let me debug: find where bstrat returns None.
Need to handle STRAT_FAIL in avalue's comparison. Let me fix: if any child is STRAT_FAIL, propagate. Let me just treat STRAT_FAIL specially.
So strategy v1 (B first plays 1 or n, then x-1 or x+1) FAILS (becomes illegal) when A's first move is ≥ 6 (for odd n). The "non_loss_for_B" is empty, meaning whenever the strategy is legal, A loses. But the strategy becomes illegal for A first moves in the upper half.

The issue: when A picks a large first move (e.g., a=7 in n=9), B plays 1. Then A plays 2 (small), B plays 3 (x+1 since x-1=1 taken). Then A plays 4, B plays 5. A plays 6, B plays 7? But 7 is A's first move (taken). So B can't play 7. x-1=5 (taken by B), x+1=7 (taken by A). Both unavailable. Strategy fails.

So the strategy needs refinement. The problem is when A's first move is in the upper half, B should mirror differently. By symmetry, if A picks a in upper half, B should pick n (the far end) and play x+1 (push A downward). 

So the strategy should be symmetric: B picks the endpoint FAR from A's first move, then pushes A away.

Let me reconsider. For A's first move a:
- If a ≤ (n+1)/2 (lower half including center), B picks n, then plays x-1 (push A down/left? no, x-1 is below x). Wait, in the n=9, A=1 case, B picks 9 (n), then A goes 3,5,7 (upward), B plays 2,4,6 (x-1). So B pushes... A goes up, B takes the number just below each A move. The trap is A reaches n-2 and B takes n-3, leaving n-1 blocked by A's n-2.

Hmm wait, but B picked n (the top). A goes up toward n. A can't reach n (taken). A reaches n-2 (since n-1 is adjacent to... no, n-1 is adjacent to n which B has, but that's B's, doesn't affect A). A can pick n-1? A's set has n-2, so n-1 adjacent, forbidden. So A stops at n-2. Then remaining n-1, blocked. 

For A's first move in upper half, by symmetry B picks 1, A goes downward 2,4,...wait no. Let me think symmetrically: reflect the board (i → n+1-i). If A picks a in upper half, reflect: A' picks n+1-a in lower half. B's strategy on reflected board: pick n (=1 in original), play x-1 (= (n+1-x)+1 -1... hmm let me just think directly.

Symmetric strategy: B picks the endpoint on the opposite side from A's first move. If A picks a ≤ center, B picks n (opposite, far). If A picks a > center, B picks 1 (opposite, far). Then B pushes A toward the far end (where B's endpoint is), playing the number just behind A (between A and A's start).

Wait, in A=1 (lower), B=n (upper, far). A moves upward (3,5,7). B plays x-1 (just below A, i.e., between A's current and A's start). A is pushed up toward n.

In A=n (upper), by symmetry B=1 (lower, far). A moves downward. B plays x+1 (just above A). 

In A=middle-ish, say A=5 in n=9 (center). B picks... center is (n+1)/2=5. A picked center. B picks 1 (per traces). Then A moves... trace shows A=5,B=1,A=2,B=3,A=7,B=6,A=9,B=8. Hmm A went 5, then 2 (down), then 7,9 (up). Mixed. B played 1 (first), then 3 (x+1, since A=2, x-1=1 taken), then 6 (x-1, A=7), then 8 (x-1, A=9). So B switches between x-1 and x+1.

This is getting complicated. The strategy "x-1 or x+1 (whichever legal)" with B's first move = endpoint far from A. Let me redefine:

B's strategy v2:
- First move: if A's first move a ≤ (n+1)/2, B picks n; else B picks 1. (Pick the far endpoint.)
  - But traces showed for odd n, A=1→B=n, A=2..n→B=1. That's NOT "far endpoint" for A=2 (a=2 ≤ center=5, far endpoint=n=9, but B picked 1!). 

Contradiction. Let me re-examine. n=9, A=2: B picked 1, not 9. But 2 is in lower half, far endpoint is 9. Yet B picked 1 (near). Hmm.

So my "far endpoint" theory is wrong. Let me reconsider. B picks 1 if available, else n. That's "near-left endpoint if available." For A=1, 1 taken, so B=n. For A=anything else, B=1.

Then the push direction: B plays x-1 or x+1. For A=2,B=1: A goes 4,6,8 (up), B plays 3,5,7 (x-1). So A pushed up, B takes just below. Trap: A reaches 8 (=n-1), B takes 7, remaining 9 (=n), but 9 adjacent to A's 8 → blocked. Wait n=9, A=2: A={2,4,6,8}, B={1,3,5,7}, remaining {9}. A's f from {2,4,6,8}: {1,3,5,7,9}. 9 blocked. Stuck. Yes.

So for A=2, B=1 (near left), A pushed rightward to n-1=8, B takes just-below, A stuck at 9 (=n) blocked by 8.

For A=1, B=9 (far right, since 1 taken), A pushed rightward (3,5,7), B takes just-below (2,4,6), A stuck at 8 (=n-1) blocked by 7.

So in both cases A is pushed rightward (toward n) and stuck near n. The difference is whether B occupies n or 1 first.

For A in upper half, e.g., A=7 in n=9: B=1. Then A pushed... trace: A=7,B=1,A=2,B=3,A=4,B=5,A=9,B=8? Wait trace was A=7,B=1,A=2,B=3,A=4,B=5,A=9,B=8,STUCK A. Let me recompute. A={7,2,4,9}, B={1,3,5,8}. Remaining {6}. A's f from {7,2,4,9}: {1,3,5,6,8,10}→ in range {1,3,5,6,8}. 6 blocked. Stuck. 

Hmm so A went 7, then 2,4 (down-left), then 9 (up). B played 1, then 3,5 (x+1 for A=2,4), then 8 (x-1 for A=9). Mixed directions. The trap: remaining 6, blocked by A's 7.

This is genuinely complex. The strategy isn't a simple "push one direction." 

Given the complexity, maybe I should abandon trying to find a clean closed-form strategy and instead think about the proof differently.

Let me reconsider. This is a competition problem; the official solution likely has a clean structure. Let me think about the parity argument as the core.

**Core Parity Argument**: 
- A draw ⟺ final position is the parity partition (A=odds, B=evens or swap).
- This is the unique 2-coloring of the path.

Now, think about it from B's perspective. B wants to prevent the draw AND make A the one stuck.

Here's a cleaner idea based on parity:

Consider the parities. A moves on turns 1,3,5,... (odd turns). For a draw, A must collect exactly one parity class. 

Key: A's first move determines A's "target parity" for a draw. If A picks an odd number, then for a draw A must collect ALL odds (and B all evens). If A picks even, A must collect all evens.

Now B's strategy: B will "steal" one number of A's target parity, breaking the draw. But B must also ensure A (not B) gets stuck.

Hmm, but stealing one parity number doesn't directly make A stuck.

Let me think about a cleaner invariant. 

Actually, let me reconsider the problem from the perspective of "the game is equivalent to both players building independent sets, draw = perfect 2-coloring."

Let me think about B's strategy as: B always plays a number of the SAME parity as A's last move, adjacent to it. Wait, adjacent numbers have opposite parity. So B can't play same parity adjacent. 

B plays opposite parity (adjacent to A's move). B's set = {neighbors of A's moves}. For B's set to be independent: B's numbers are a_i ± 1. Two such, a_i+1 and a_j+1, adjacent iff a_i,a_j adjacent (no). a_i+1 and a_j-1 adjacent iff a_i+1=a_j-1±1 → a_i = a_j-2 or a_i=a_j. a_i=a_j-2: then a_i,a_j differ by 2, both in A's set (independent, allowed). Then a_i+1 = a_j-1, so B would pick the same number twice — but actually B picks a_i+1 after A's move a_i, and a_j-1 after A's move a_j. If a_i+1 = a_j-1, that's the same number; B can't pick it twice (already taken). So B's strategy must avoid this conflict.

This is the issue. The "x-1" strategy avoids it by always picking the same side. But then B's set might not be independent if... we showed x-1 keeps independence (since A independent → x_i-1 independent). And x-1 always available (shown). The only issue was x-1 adjacent to B's FIRST move (the endpoint).

So the clean strategy: B picks an endpoint e (1 or n), then plays x-1 (if e=n) or x+1 (if e=1) — always the side toward e. Wait:
- If B picks e=n, B plays x-1 (toward... x-1 is away from n if x<n). Hmm. Let me reconsider. B picks n. Then plays x-1. B's set = {n, x_2-1, x_3-1,...}. Is x_i-1 adjacent to n? Only if x_i-1 = n-1, i.e., x_i = n. But n taken by B, A can't pick n. So no. Good, B's set independent. And x_i-1 available (shown). So strategy "B picks n, then x-1" is ALWAYS legal (for any n, any A moves)!

Wait, is that right? Let me re-examine the availability of x_i - 1. x_i - 1 could be 0 (if x_i = 1). If A picks 1 as a later move, x_i - 1 = 0, invalid. When would A pick 1? Only if 1 is available and not adjacent to A's set. If B picked n (first), 1 is available (unless A's first move was 1). If A's first move was 1, then 1 taken, A can't pick it again. If A's first move ≠ 1, then 1 is available, and A might pick 1 later. Then B wants x-1 = 0, invalid.

So the strategy "B picks n, then x-1" fails if A ever picks 1 (as a non-first move). When does A pick 1? A picks 1 if 1 available (A's first ≠ 1, and B didn't take 1 — B took n, so 1 available) and 1 not adjacent to A's set (A has no 2). 

So if A's first move is, say, 5 (n=9), B picks 9. Then 1 is available. A could pick 1 later (if A has no 2). A's first move 5, A forbidden {4,6}. 1 is available and not forbidden. A could pick 1 as second move! Then B's x-1 = 0, invalid.

So "B picks n, then x-1" fails when A's first move ≠ 1 and A later picks 1.

Hmm. So the strategy needs B to also block 1, OR B picks 1 first (then plays x+1).

Let me reconsider: B picks 1 (if available), then plays x+1. B's set = {1, x_2+1, x_3+1,...}. x_i+1 adjacent to 1? Only if x_i+1=2, i.e., x_i=1. But if B picked 1, then 1 taken, A can't pick 1. So x_i≠1, x_i+1≠2. Good. x_i+1 available? x_i+1 not in A's set (A has x_i, independent, so no x_i+1). Not in B's set: x_i+1 = x_j+1 → x_i=x_j no. x_i+1 = 1 → x_i=0 no. So available. x_i+1 could be n+1 (if x_i = n). If A picks n as later move, x_i+1 = n+1 invalid. When does A pick n? If n available (B took 1, so n available unless A's first = n) and not adjacent to A's set (A has no n-1). If A's first move ≠ n, A might pick n later. Then x+1 = n+1 invalid.

So "B picks 1, then x+1" fails when A's first move ≠ n and A later picks n.

So: 
- "B picks n, then x-1" fails if A picks 1 later (possible when A's first ≠ 1).
- "B picks 1, then x+1" fails if A picks n later (possible when A's first ≠ n).

Combine: If A's first move = 1, use "B picks n, then x-1" (A can't pick 1 again, and A can't pick n (B has it), so x-1 always valid? x_i = 1 impossible (taken), x_i = n impossible (taken by B). So x_i - 1 ∈ [1, n-1] always valid. And x_i-1 ≠ n (since x_i ≠ n+1). And x_i-1 not adjacent to n (shown). So strategy legal!). 

If A's first move = n, use "B picks 1, then x+1" (symmetric). Legal.

If A's first move a is interior (1 < a < n): both strategies have issues. B picks 1, then x+1: fails if A picks n later. B picks n, then x-1: fails if A picks 1 later. 

Hmm. But maybe B can pick 1 AND the strategy handles A picking n? Let me think: B picks 1, plays x+1. If A picks n (later move), x+1 = n+1 invalid. But wait, if A picks n, then n is taken by A. Before that, was n available? B has 1, A has a (interior) and now n. B's response to A=n would be x+1=n+1, invalid. So B needs a different response when A picks n.

Alternatively: B picks 1, and plays x+1 EXCEPT when A picks n-1 (then x+1 = n, which is fine, B takes n). Wait if A picks n-1, B plays x+1 = n. That's fine (n available, not adjacent to B's set? B has 1 and previous x_j+1. n adjacent to n-1 (A's) — doesn't matter. n adjacent to B's set? B has 1 (far) and x_j+1. n adjacent to x_j+1 iff x_j+1 = n-1, i.e., x_j = n-2. So if A previously picked n-2, B took n-1, then A picks n-1? No, n-1 taken by B. Conflict... hmm.

This is getting complicated. Let me reconsider.

Actually, the cleanest: B picks 1, then plays x+1. This works as long as A never picks n. Can B prevent A from picking n? A picks n only if n available and n not adjacent to A's set (A has no n-1). 

If B's strategy is "pick 1, then x+1", B takes 1, then takes x_2+1, x_3+1, .... Does B ever take n? B takes x_i+1 = n when x_i = n-1. So if A picks n-1, B takes n. Then n is taken by B, A can't pick n. Good. But if A never picks n-1, then n stays available, and A might pick n.

When would A pick n? A picks n if available and A has no n-1. If A avoids n-1 (to keep n available for itself), A could pick n. Then B's x+1 = n+1 invalid.

So B's strategy "pick 1, then x+1" fails if A picks n without first picking n-1.

Hmm. So A can deviate by picking n directly. Let me check: does A picking n actually help A escape? Let me test the strategy "B picks 1 (or n if 1 taken), then x+1 (or x-1 if n taken)" against optimal A.

Actually, let me reconsider. Let me define strategy v2:
- If A's first move a = 1: B picks n, then plays x-1.
- If A's first move a = n: B picks 1, then plays x+1.
- If 1 < a < n: B picks 1, then plays x+1; BUT if A ever picks n, switch to... hmm.

This is getting messy. Let me just test a cleaner combined strategy and see if it works:

Strategy v2: B picks 1 if available else n. Then B plays x-1 if B's first was n, else x+1. I.e., B always pushes toward the side OPPOSITE its endpoint. If B has endpoint n, push A left (x-1). If B has endpoint 1, push A right (x+1).

Wait, that doesn't match. Let me re-examine n=9, A=1: B picks n=9 (since 1 taken). Then plays x-1. A goes 3,5,7 (rightward!), B plays 2,4,6. So A moves rightward (toward n), B takes just-below. But B's endpoint is n (right). A is pushed toward n (right). B plays x-1 (below A, left of A). Hmm, so B takes the number just LEFT of A's move. A moves right, B fills in just left. 

n=9, A=2: B picks 1 (available). Then plays x+1. A goes 4,6,8 (rightward), B plays 3,5,7 (x+1, just right of A... no, x+1 = 5 for A=4, that's right of A). Wait A=4, B plays 5 (x+1). 5 is right of 4. Then A=6, B=7. A=8, B=9? But 9 = n. B plays x+1=9. Then remaining... A={2,4,6,8}, B={1,3,5,7,9}? Wait that's 5 B moves and 4 A moves, but they alternate. Let me recount: A=2(1),B=1(2),A=4(3),B=3(4)? 

Hold on. n=9, A=2, B=1. Then A's turn. A=4. B's turn, plays x+1 = 5? But trace showed B=3 (x-1) for A=4! Let me recheck the trace: "A first=2: [('A', 2), ('B', 1), ('A', 4), ('B', 3), ('A', 6), ('B', 5), ('A', 8), ('B', 7), ('STUCK', 'A')]". So B plays 3,5,7 = x-1 (4-1=3, 6-1=5, 8-1=7). So B plays x-1, NOT x+1, even though B's endpoint is 1 (left). 

So B plays x-1 here, pushing... A goes right (4,6,8), B takes just-left (3,5,7). So B takes x-1 (left of A). A moves right toward n=9. B's endpoint 1 is on the left. So A is pushed RIGHT (away from B's endpoint 1, toward n). And B takes just-left of each A move.

And for A=1, B=9 (endpoint right), A moves right (3,5,7) toward B's endpoint 9, B takes just-left (2,4,6). Here A moves toward B's endpoint.

These are inconsistent in direction relative to B's endpoint. Let me reconsider: in BOTH cases, A moves rightward and B takes x-1 (just left of A). 

For A=1: B=9, A:3,5,7 rightward, B:2,4,6 = x-1.
For A=2: B=1, A:4,6,8 rightward, B:3,5,7 = x-1.

So actually in both, B plays x-1 and A moves right! The endpoint choice (9 vs 1) just depends on availability. So maybe the strategy is simply: B plays x-1 always (after first move), and first move = 1 if available else n. And A is pushed right.

But we saw this fails for A's first move in upper half (A picks small numbers later, going left). E.g., A=7 (n=9), B=1, then A=2 (leftward), B should play x-1=1 (taken) → fail. That's why strategy v1 failed for a≥6.

So when A goes left (picks small numbers), x-1 fails. B needs to play x+1 when A is on the left side moving... 

OK here's the real structure: B wants to push A toward an endpoint where B has placed its first piece, trapping A against it. The direction depends on where A goes.

Let me reconsider. Maybe the strategy is: B's first move at an endpoint. Then B always plays the number adjacent to A's last move on the side TOWARD B's endpoint. This pushes A away from B's endpoint... no.

Hmm, let me think about it as B "herding" A. 

Actually, let me reconsider the traces for upper-half A first moves:
n=9, A=7: B=1, A=2, B=3, A=4, B=5, A=9, B=8, stuck.
A went 7 → 2 (jump left) → 4 (right) → 9 (jump right). B: 1, 3, 5, 8.
B's moves: 1 (endpoint), 3 (=A2+1), 5 (=A4+1), 8 (=A9-1). 
So B plays x+1 when A is small (2,4), x-1 when A is large (9). I.e., B plays the adjacent number toward the center / away from the nearest endpoint? 

A=2: nearest endpoint 1 (taken by B). B plays 3 (away from 1, toward center). 
A=4: B plays 5 (away from 1, toward center/right).
A=9: nearest endpoint 9 itself (it's an endpoint). B plays 8 (away from 9's edge, toward center). 

Hmm, B plays the side toward the center? Let me check A=2,B=3: 3 is toward center from 2. A=4,B=5: toward center (center=5). A=9,B=8: toward center from 9. A=7 (first), B=1: 1 is... away from center. Hmm, that's the first move (endpoint), different rule.

Let me reconsider with the herding idea: B's first move = 1 (left endpoint). Then B herds A toward the RIGHT (toward n). B plays the adjacent-to-A number on the LEFT side (x-1) when A is moving right, but if A jumps to the left of B's "frontier," B plays x+1 to push it back right.

This is like B maintaining that A's numbers are all ≥ some frontier, and B fills in just below. But A can jump left...

This is genuinely a complex strategy. I don't think I'll find a super-clean closed form easily. 

Let me step back and reconsider the proof strategy. Given this is hard, maybe the intended solution uses a different, cleaner idea that I'm missing. Let me think about the problem from a higher level.

**Alternative approach: Think about the game as two interleaved games on parity classes.**

Hmm. Let me think about the following: color numbers by parity. A's set must be independent, so within A's set, no two consecutive — but A can have both parities (e.g., {1,4}). 

Let me think about the "gap" / interval structure.

**Another idea**: Let me think about when A is stuck. A is stuck iff A's set dominates all remaining numbers. 

Let me think about a potential function: the number of "available non-forbidden for A" minus something.

This is really a hard combinatorial game. Let me reconsider whether the answer might be cleaner than {1,2,4,6} and maybe I should reconsider the problem.

Actually, wait. Let me reconsider the problem statement once more. "determine the outcome." Maybe the expected answer is just "B wins for n ≥ 3 except n=4,6; draw for n=1,2,4,6." And the proof is casework-heavy. Competition problems can have such answers (e.g., IMO 2017 C6 about a game had a mod-based answer).

Let me just go with constructing a proof that:
1. States the parity characterization (draw ⟺ parity partition).
2. Handles small cases n=1,...,6 directly.
3. For n ≥ 7, gives B's winning strategy.

For part 3, I need a working strategy. Let me find one that I can prove works, even if not the minimax-optimal one. Let me search for a clean strategy by testing candidates programmatically against optimal A.

Let me test: B's strategy = "pick 1 if avail else n; then play x-1 if legal else x+1 if legal else (any legal)." But we saw it fails (illegal) for upper-half A. The "else any legal" fallback — does it still win? Let me test with fallback to a specific rule.

Actually, the issue is the strategy becoming illegal (no x±1 available). Let me add a fallback and test if B still wins. But fallback "any legal" might not win. Let me test fallback = optimal (to see if there's always a winning move, just not x±1). Actually that's just minimax again.

Let me think about a better strategy. Let me reconsider the herding.

Let me reconsider: B's strategy should keep A's set confined to an interval and shrink it. 

Here's a cleaner idea based on the traces: B maintains the invariant that A's numbers are all within some interval [L, R] and B "controls" L-1 and R+1 (or the endpoints), herding A.

Hmm, let me look at the n=9, A=7 trace again: A={7,2,4,9}, B={1,3,5,8}. A's numbers span [2,9]. B has 1 (left of 2), 3,5,8. Not a clean interval herding.

Let me try yet another approach: maybe prove B wins for n≥7 by reducing to n=7 or n=8 via a strategy that "ignores" extra numbers.

**Reduction idea**: For n ≥ 7, B's strategy: respond to A within a 7-element window, treating the rest as "already resolved" in B's favor.

Hmm, but the rest interacts.

Let me think about a cleaner reduction. 

Actually, let me reconsider the parity argument for a WINNING (not just non-losing) strategy.

**Parity-based winning strategy for B**: 

Claim: For n ≥ 7, B can force A to be the one who cannot complete a parity class, AND get stuck.

Let me think about B's strategy: B always plays a number of opposite parity to A's last move, specifically adjacent. This "claims the neighbor." Over time, A's set is surrounded.

Hmm, I keep going in circles. Let me just try to find a clean provable strategy by testing several candidates programmatically. Let me test:

Strategy A: B picks 1 if avail else n. Then B plays x-1 if (x-1 legal) else x+1 if legal. If neither, B plays... let me test with fallback "smallest legal" and "largest legal" and see if either wins.

Actually, let me reconsider. The traces for upper-half A first moves show B playing x+1 when A is small. So maybe the rule is: B plays x-1 if x > (n+1)/2, else x+1. I.e., push A toward the center? No...

Let me look again:
n=9, A=7: B=1(first). A=2→B=3 (x+1, since 2 < center=5). A=4→B=5 (x+1, 4<5). A=9→B=8 (x-1, 9>5). 
n=9, A=5 (center): B=1. A=2→B=3 (x+1). A=7→B=6 (x-1, 7>5). A=9→B=8 (x-1).
n=9, A=6: B=1. A=2→B=3(x+1). A=4→B=5(x+1). A=8→B=7(x-1).

So the rule seems: B plays x+1 if x ≤ center-ish, x-1 if x > center. Specifically x+1 when x < (n+1)/2, x-1 when x > (n+1)/2. What about x = center? n=9, A=5(center) was first move. Later A picks... in A=5 trace, A picks 2,7,9. None is center. 

Hmm, let me reconsider: maybe the rule is "B plays the adjacent number on the side of the NEARER endpoint to x." Wait:
x=2: nearer endpoint 1 (taken by B). Other side: 3. B plays 3. ✓ (play away from nearer endpoint, since nearer is blocked)
x=4: nearer endpoint 1. Other side 5. B plays 5. ✓
x=9: nearer endpoint 9 (it's endpoint). Other side 8. B plays 8. ✓
x=7: nearer endpoint 9 (distance 2) vs 1 (distance 6). Nearer=9. Other side 6. B plays 6. ✓ (A=7,B=6 in A=5 trace)

So rule: B plays the adjacent number on the side AWAY from the nearer endpoint. Equivalently, B plays x-1 if x is in the right half (closer to n), x+1 if x in left half (closer to 1). The boundary is the center.

But wait, this is the same as "push A toward the center"? No: x=2 (left half), B plays 3 (right of 2, toward center). x=9 (right half/endpoint), B plays 8 (left of 9, toward center). x=7 (right half), B plays 6 (toward center). So YES: B plays the adjacent number toward the center! B pushes A toward the center.

Hmm, but that seems to trap A in the middle. Let me reconsider n=9,A=1: B=9. A=3 (left half, center=5). B plays toward center = x+1=4? But trace shows B=2 (x-1)! Contradiction.

Wait n=9, A=1: A=3, B=2. 3 is in left half (3<5). Toward center would be 4 (x+1). But B played 2 (x-1, away from center). So the rule "toward center" fails for A=1 case.

Ugh. The A=1 case: B=9 (right endpoint). A=3, B=2 (x-1, toward LEFT endpoint, away from center). So here B pushes A LEFT (toward 1)? But A is moving right (3,5,7). 

I'm confusing myself. Let me re-examine: in A=1 case, A moves 1,3,5,7 (rightward, toward n=9). B moves 9,2,4,6. B's non-first moves: 2,4,6 = x-1 (A=3→2, A=5→4, A=7→6). So B takes the number just LEFT of A's move. A moves right, B fills left-behind. The trap: A reaches 7, B takes 6, remaining 8 (right of 7, blocked by 7) and 9 (taken by B). A stuck.

In A=7 case, A moves 7,2,4,9. B moves 1,3,5,8. B's non-first: 3,5,8. A=2→B=3 (x+1, right of 2). A=4→B=5 (x+1). A=9→B=8 (x-1, left of 9). So B takes the number on the side... A=2 is left, B takes right (3). A=4 left-ish, B takes right (5). A=9 right endpoint, B takes left (8). 

So in A=7 case, B's first move is 1 (left endpoint). A jumps to 2 (near B's endpoint). B takes 3 (right of 2, pushing A right/away from endpoint 1). Then A=4, B=5 (push right). A=9, B=8 (A went to far right, B takes left of it). 

So the herding: B has endpoint 1. B pushes A rightward (away from 1) by taking the right-adjacent number. When A reaches the far right (9), B takes 8 (left-adjacent), and A is stuck because... remaining 6, blocked by A's 7. 

Hmm wait, A={7,2,4,9}, remaining {6}. 6 is between A's 4 (no, 4's neighbors 3,5) and A's 7 (neighbors 6,8). 6 is neighbor of 7. So 6 blocked by A's 7. Also 6 is neighbor of... B's 5 (doesn't matter). So 6 blocked. A stuck.

So the trap here: A's own 7 blocks 6, the last remaining number.

OK the strategies are genuinely intricate and depend on A's choices. I think finding a single clean closed-form strategy is hard. 

Let me reconsider the proof approach. Maybe I should:
- Prove the parity characterization.
- Prove draw for n=1,2,4,6 by explicit strategies (A can force draw).
- Prove B wins for n=3,5 explicitly.
- For n≥7, prove B wins by a strategy that I CAN prove, even if complex. 

For n≥7, let me consider a strategy based on B "mirroring with respect to the center" but handling the center, OR an inductive strategy.

**Inductive strategy**: Show that if B wins for n, then B wins for n+2 (adding two numbers, one at each end). And base cases n=7,8 (or n=7,8,9,10). 

How would the induction work? If B wins on [1,n], then on [1,n+2], B's strategy: ... A picks some number. If A picks within [1,n], B responds as in the n-game (treating n+1, n+2 as "extra"). But the extra numbers interact (A could pick n+1, n+2).

Hmm, induction is tricky because A can use the new numbers.

Let me think about a different induction: B's strategy on n+2 is to first "neutralize" the two new endpoints then play the n-strategy on the middle.

Actually, here's a cleaner idea. Let me think about B's strategy for n ≥ 7 as follows:

B's strategy: B picks 1 (if A didn't) or n (if A picked 1). Then B plays the "reflection" of A's move... no.

Let me try to just find ANY strategy that works for all n≥7 by testing, then prove it. Let me test the "herding toward far endpoint" strategy more carefully:

Strategy: B's first move = 1 if available, else n. Then B maintains a "frontier": B always plays the adjacent-to-A's-last-move number on the side toward B's endpoint... no I showed that's inconsistent.

Let me just brute-force search for a simple strategy of the form "B plays f(avail, aset, bset, lastA)" among simple rules, testing against optimal A for n=7..15. Let me test the strategy: "B plays x-1 if x-1 legal and (x-1 ≥ B's endpoint or ...)"... 

Actually, let me reconsider. Let me look at ALL the traces and find the common rule for B's non-first moves.

Let me collect B's non-first moves and see the rule relative to A's last move and B's first endpoint.

n=9:
A=1,B_first=9: (A=3,B=2),(A=5,B=4),(A=7,B=6) — all x-1.
A=2,B_first=1: (A=4,B=3),(A=6,B=5),(A=8,B=7) — all x-1.
A=3,B_first=1: (A=5,B=4),(A=7,B=6),(A=9,B=8) — all x-1.
A=4,B_first=1: (A=2,B=3),(A=6,B=5),(A=8,B=7) — x+1, x-1, x-1.
A=5,B_first=1: (A=2,B=3),(A=7,B=6),(A=9,B=8) — x+1, x-1, x-1.
A=6,B_first=1: (A=2,B=3),(A=4,B=5),(A=8,B=7) — x+1, x+1, x-1.
A=7,B_first=1: (A=2,B=3),(A=4,B=5),(A=9,B=8) — x+1, x+1, x-1.
A=8,B_first=1: (A=2,B=3),(A=4,B=5),(A=6,B=7) — x+1, x+1, x+1.
A=9,B_first=1: (A=2,B=3),(A=4,B=5),(A=6,B=7) — x+1, x+1, x+1.

So the pattern: B plays x-1 when x is "large" (right portion) and x+1 when x is "small" (left portion). The threshold seems to be around B's first move position or the center.

Specifically: B plays x+1 when x < B_first, and x-1 when x > B_first? Let me check:
A=4,B_first=1: A=2 (2>1, so x-1=1? but B played 3=x+1). No. 2 > B_first=1, rule says x-1=1, but B played 3. ✗.

Let me try: B plays x+1 when x ≤ some threshold T, x-1 when x > T.
A=4: A=2→x+1, A=6→x-1, A=8→x-1. So T between 2 and 6. 
A=5: A=2→x+1, A=7→x-1, A=9→x-1. T between 2 and 7.
A=6: A=2→x+1, A=4→x+1, A=8→x-1. T between 4 and 8.
A=7: A=2→x+1,A=4→x+1,A=9→x-1. T between 4 and 9.
A=8: A=2,4,6 all x+1. T ≥ 6.
A=9: A=2,4,6 all x+1. T ≥ 6.
A=1,B_first=9: A=3,5,7 all x-1. So T < 3 (all x > T). 
A=2,B_first=1: A=4,6,8 all x-1. T < 4.
A=3,B_first=1: A=5,7,9 all x-1. T < 5.

Hmm, the threshold varies. For A=1 (B_first=9), T<3. For A=8 (B_first=1), T≥6. So T depends on the game state, not fixed.

This really is a complex adaptive strategy. I don't think there's a simple closed-form.

Given the difficulty, let me reconsider the possibility that the intended solution is structured differently — perhaps using the Sprague-Grundy-like analysis or a clever invariant, OR the answer is actually simpler and I have a bug.

Wait, let me reconsider. Let me re-examine whether the answer might be "B wins for all n ≥ 3" and my n=4,6 results are due to a subtle bug. Let me re-verify n=4 and n=6 with a totally independent simple script.

n=4: I hand-verified draw. Let me re-verify n=6 is draw with extra care, and n=8 B wins, using an independent implementation.

Actually I already hand-verified n=6 draw (A picks 1 → B can't win, A can't win → draw; and A has no winning first move). And n=4 draw hand-verified. And n=3,5 B wins. So the pattern {1,2,4,6} draw is solid.

Hmm, let me reconsider — maybe the problem is from a specific olympiad and the answer is known to be this. Let me just search my memory: I believe this is **IMO 2018 Shortlist C4** or **IMO 2017 C6**. Actually, I recall a problem "A and B choose numbers, can't choose consecutive to own" — this might be from **IMO 2018 C5** (game). The answer... I genuinely don't remember the exact answer.

Let me just go with the computed answer and construct the best proof I can. For the n≥7 case, I'll give a strategy and prove it works. Let me find a strategy I can actually prove.

Let me reconsider a cleaner strategy: **B mirrors A across the center, and if A plays center (odd n), B plays 1 (or handles specially).** Let me test this reflection strategy for n=7,8,9 against optimal A.

Reflection: B plays n+1-x in response to A's x. For even n, no center issue. For odd n, if A plays center c=(n+1)/2, reflection is c itself (taken), so B needs a fallback.

Let me test: B plays n+1-x; if that's illegal/unavailable, B plays optimally (or some fallback). Actually let me test pure reflection (with fallback to optimal when reflection unavailable) and see if it wins or draws.

For even n, pure reflection → we saw n=4,6 draw, n=8... let me test. Earlier n=8 with reflection (A=1,B=8,A=3,B=6,A=5,B=4,A=7,B=2) → draw. So reflection gives draw for n=8, not win. So reflection is not B's winning strategy for even n≥8.

So for even n≥8, B must deviate from reflection to win. The traces confirm (n=8, A=1, B plays 5 not 6 at move 2).

OK. I think the cleanest path is to give a proof that's somewhat case-analytic but correct. Let me structure it as:

**Proof outline:**
1. **Parity Lemma**: Draw ⟺ final partition is {odds}/{evens}.
2. **Small cases**: n=1,2 draw (trivial); n=3 B wins; n=4 draw; n=5 B wins; n=6 draw. (Explicit strategies.)
3. **n ≥ 7, B wins**: Give B's strategy and prove it.

For part 3, let me find a provable strategy. Let me think about a strategy based on "B always responds adjacent to A's move, on a fixed side relative to A's first move."

Let me reconsider the successful traces and find the invariant. 

Let me reconsider the strategy: **B's first move is the endpoint nearest to A's first move's opposite... ** ugh.

New idea: Let me consider B's strategy as maintaining that A's set is contained in an interval, and B "eats" from one side.

Let me look at the n=9 traces and track the interval containing A's numbers and B's "wall":

A=1: A's set grows {1},{1,3},{1,3,5},{1,3,7}... interval [1,7]. B has 9 (right wall) and 2,4,6 (filling gaps below A). 
A=7: A's set {7},{7,2},{7,2,4},{7,2,4,9}. interval [2,9]. B has 1 (left wall), 3,5,8.

Hmm. In A=1 case, B's first move 9 is the RIGHT wall, and A is pushed right toward it, B fills in just-left. In A=7 case, B's first move 1 is the LEFT wall, A jumps around, B fills in.

Let me think about it as: B picks the endpoint on the side where A's first move is NOT, then herds A toward that endpoint. 

A=1: A's first move at left endpoint. B picks right endpoint (9). Herd A rightward (toward 9). 
A=7 (n=9): A's first move in right portion. B picks left endpoint (1). Herd A leftward (toward 1)? But A went 7→2 (left, yes), then 2→4 (right!), →9 (right). So not purely leftward.

Hmm, A doesn't cooperate. B herds but A can jump.

I think the real strategy is adaptive in a way that's hard to state simply. 

Let me take yet another step back. Given the time I'm spending, let me consider just presenting the answer with the parity lemma and computational verification for the strategy, giving B's strategy as an explicit algorithm (decision tree) that I verify works. But a proof should be human-checkable.

Actually, let me reconsider. Let me look for a strategy that's clean AND provable, even if not minimax-optimal, as long as it wins for n≥7. Let me test the following clean strategy:

**Strategy H (herding)**: B's first move: if A's first move a ≤ (n+1)/2, B plays n; else B plays 1. (B takes the endpoint on the opposite side.) Then B always plays the number adjacent to A's last move on the side TOWARD B's endpoint (i.e., if B's endpoint is n, B plays x+1; if B's endpoint is 1, B plays x-1). Wait that pushes A toward B's endpoint. Hmm, but then A gets squished against B's endpoint. Let me reconsider — actually B wants to push A AWAY from B's endpoint so A gets trapped against the OTHER endpoint (which is open)? No...

Let me just test several clean strategies programmatically and find one that wins for all n=7..15. Let me test:

H1: B_first = n if a ≤ center else 1. Then B plays x+1 if B_first=n else x-1. (Push A toward B's endpoint.) With fallback to x∓1 if preferred side illegal, else any legal.

H2: B_first = n if a ≤ center else 1. Then B plays x-1 if B_first=n else x+1. (Push A away from B's endpoint.)

Let me test both.
H1 and H2 both win for odd n (7,9,11,13: all A_loses). But for even n (8,10,12), they only draw for some A first moves. So H1/H2 work for ODD n ≥ 7 but not even n.

So for odd n ≥ 7, H1 (or H2) is a clean winning strategy:
- B_first = n if A's first a ≤ center else 1.
- Then push toward B's endpoint (H1) or away (H2).

Both work for odd n. Let me pick one and prove it. Let me use H2 (push away from B's endpoint) — wait both work, let me check which is cleaner to prove. Actually let me reconsider what they do.

H1: B_first = n if a ≤ center else 1. Push toward B's endpoint (if B_first=n, play x+1, pushing A right toward n; if B_first=1, play x-1, pushing A left toward 1).

H2: B_first = n if a ≤ center else 1. Push away from B's endpoint (if B_first=n, play x-1; if B_first=1, play x+1).

For odd n both win. Let me focus on proving one for odd n. Let me reconsider which is more natural.

Actually, let me reconsider H2 for odd n with A=1: B_first = n (since 1 ≤ center). Push away from n: play x-1. A=1, B=n. A=3, B=2 (x-1). A=5,B=4. A=7,B=6. This matches the minimax trace! Good.

For A=2 (n=9): B_first = 1 (since 2 ≤ center=5? yes 2≤5, so B_first=n=9??). Wait center=(9+1)/2=5. a=2 ≤ 5, so B_first = n = 9. But the minimax trace for A=2 had B_first=1! 

Hmm, so H2 with A=2 gives B_first=9, but minimax gave B_first=1. Let me check if H2 still wins. The test says n=9 all A_loses, so H2 wins even with B_first=9 for A=2. Let me see the line: A=2, B=9 (H2). Then push away from 9: play x-1. A's turn: A={2},f{1,3}. avail{1,3,4,5,6,7,8}. A picks something. A picks 4 (say). B plays x-1=3. A={2,4},f{1,3,5}. avail{1,5,6,7,8}. B={9,3},f{2,4,8}. A picks 6. B plays 5. A={2,4,6},f{1,3,5,7}. avail{1,7,8}. B={9,3,5},f{2,4,6,8}. A picks 8? 8 not in A's f{1,3,5,7}. A=8. A={2,4,6,8},f{1,3,5,7,9}. avail{1,7}. B plays x-1=7. B={9,3,5,7}. avail{1}. A f{1,3,5,7,9}→1 blocked. stuck. 

So H2 works for A=2 too (with B_first=9). Good. So H2 is a valid winning strategy for odd n≥7, even though B_first differs from minimax in some cases.

Now I need to PROVE H2 works for all odd n ≥ 7. Let me understand H2 and prove it.

H2 strategy (odd n ≥ 7):
- Let c = (n+1)/2 (center).
- B's first move: if A's first move a ≤ c, B plays n; if a > c, B plays 1.
  (B takes the endpoint on the same side as... a ≤ c means a in left half, B takes right endpoint n. a > c means a in right half, B takes left endpoint 1. So B takes the endpoint on the OPPOSITE side from a.)
- Subsequently: if B's endpoint is n (so A's first was ≤ c), B plays x-1 (where x = A's last move). If B's endpoint is 1, B plays x+1.
  (B plays the adjacent number on the side AWAY from B's endpoint, i.e., toward A's side.)
  Fallback: if the preferred side is illegal, play the other side; if both illegal, play any legal move.

Wait, but the fallback "other side / any legal" — does it ever trigger for odd n? The test shows no STRAT_FAIL and all A_loses, so the strategy (with fallback) wins. But for a clean proof, I'd prefer the preferred side always legal. Let me check if the preferred side (x-1 for B_first=n, or x+1 for B_first=1) is ALWAYS legal for odd n≥7.

From the test, H2 had fails=[] for odd n, meaning the strategy never hit STRAT_FAIL. But the fallback might have been used (preferred side illegal, other side legal). Let me check if the preferred side is always legal, or if fallback is needed.

Let me modify to track whether fallback is used.

Actually, for the proof, let me reconsider. Let me check: is the preferred-side move always legal for odd n ≥ 7?

Preferred: x-1 (if B_first=n) or x+1 (if B_first=1).

Case B_first=n (A's first a ≤ c): B plays x-1 for each A move x (after first). 
- x-1 available? x-1 not in A's set (A has x, independent). Not in B's set: B has {n, x_j-1 for j<i}. x-1 = x_j-1 → x=x_j no. x-1 = n → x=n+1 impossible. So available. 
- x-1 ≥ 1? x ≥ 2 needed. Could A pick x=1? A's first move a; if a=1, then 1 taken, A can't pick 1 again. If a > 1 (but a ≤ c), then 1 is available. Could A pick 1 later? A picks 1 if 1 available and 1 not adjacent to A's set (A has no 2). So A could pick 1 as a later move! Then x-1 = 0, invalid.

So if A's first move a is in {2,...,c} (so B_first=n), A might later pick 1, breaking x-1. Let me check: does A picking 1 actually happen / does the strategy handle it?

Let me test: n=9, A=2 (a=2 ≤ c=5, B_first=9). Could A pick 1 later? A={2}, f{1,3}. 1 is forbidden (adjacent to 2)! So A can't pick 1. Good. 

n=9, A=3 (a=3 ≤ 5, B_first=9). A={3},f{2,4}. 1 available, not forbidden. A could pick 1. Then x-1=0 invalid. Let me check if the strategy handles A=1 via fallback. Let me test this specific line.

Actually the test already covers all A optimal responses, and H2 won for n=9. So even if A picks 1, the fallback handles it. But for a clean proof, I need to handle this case explicitly.

Hmm. Let me check: n=9, A=3, B=9 (H2). A's turn, A={3},f{2,4}, avail{1,2,4,5,6,7,8}. A could pick 1 (available, not forbidden). If A picks 1: A={1,3},f{2,4}. B plays x-1=0 invalid → fallback. Preferred side x-1=0 invalid, other side x+1=2. 2 available? yes. 2 adjacent to B's set? B={9}, 2 not adjacent to 9. So B plays 2. B={9,2},f{1,3,8}. avail{4,5,6,7,8}. A={1,3},f{2,4}. A picks 5,6,7,or 8. ... continues. Does A still lose? The test says yes (n=9 A=3 → A_loses under H2). 

So the fallback (play x+1 when x-1 invalid) handles A picking 1. But this complicates the proof.

Let me reconsider. Maybe I can choose the strategy so the preferred side is ALWAYS legal. The issue is A picking the endpoint near A's side. 

Alternative: B_first = the endpoint on the SAME side as A's first move. I.e., if a ≤ c, B_first = 1; if a > c, B_first = n. Then push... let me reconsider. If B takes the endpoint on A's side, then A can't pick that endpoint later. Then push away from B's endpoint.

Let me define H3: B_first = 1 if a ≤ c else n (same side as A). Then play x+1 if B_first=1 (push right, away from 1) else x-1 (push left, away from n). 

Wait, if a ≤ c (left half), B_first=1 (left endpoint). A's first move a is in left half. A might want to pick 1 later — but B took 1, so A can't. Good. And A might pick n later (right endpoint, available). Then x+1 = n+1 invalid. So same problem on the other side.

Hmm. Unless B also blocks n. But B only gets one first move.

So no single-endpoint strategy avoids the "A picks the far endpoint" problem. The far endpoint remains available, and if A picks it, the push-direction strategy breaks.

But the fallback handles it. Let me just prove the strategy WITH fallback, handling the "A picks far endpoint" case as a special sub-case.

Actually, let me reconsider. Let me check: when A picks the far endpoint (the one B didn't take), does A actually escape or does B still win? The test shows B still wins (with fallback). Let me understand the fallback behavior in that case and prove it.

This is getting long. Let me reconsider the overall proof structure and whether there's a fundamentally cleaner approach for odd n.

**Cleaner approach for odd n via reflection:**

For odd n, reflection (B plays n+1-x) has the center problem. But maybe handle center: if A plays center c, B plays... Let me test reflection with center-handling.

Reflection strategy R: B plays n+1-x. If n+1-x is unavailable (A played center, or A played a number whose reflection was already taken), B plays... hmm.

Actually for odd n, the center c=(n+1)/2 is a fixed point. If A plays c, reflection c is taken (by A), B can't. So B needs a response. Let me test: B plays n+1-x normally; if that's unavailable/illegal, B plays 1 (or some fixed). Let me test reflection with fallback.

Actually, let me reconsider. For odd n, the minimax B_first for A=1 is n (=n+1-1, reflection!). For A=2, minimax B_first=1, but reflection of 2 is n-1=8 (n=9). So minimax doesn't use reflection for A=2. So reflection isn't the minimax strategy. But maybe reflection still wins? Let me test.

Let me test reflection (B plays n+1-x, fallback to optimal or 1 if unavailable) for odd n.

Hmm, but if reflection leads to draw (like even n), it won't win. Let me just test.

Actually, let me step back and think about the proof structure for odd n using H2, and handle the edge cases. Let me first check: for H2 with odd n, is the PREFERRED move always legal except when A picks the far endpoint? And when A picks the far endpoint, what's the situation?

Let me instrument H2 to report when fallback (non-preferred) is used.
H2 wins for all odd n from 7 to 21 (all A_loses), but fallback IS used in some lines. So the preferred move isn't always legal. I need to handle the fallback cases in the proof.

Let me figure out exactly when the fallback triggers. The fallback triggers when the preferred move (x-1 for B_first=n, or x+1 for B_first=1) is illegal. Preferred illegal when:
- x-1 < 1 (x=1), i.e., A picked 1 (only possible if B_first=n, meaning A's first a ≤ c and a≠1, so 1 was available and A picked it later).
- x-1 unavailable (taken): x-1 in B's set (only n or previous x_j-1; x-1=n impossible, x-1=x_j-1 impossible). x-1 in A's set: A has x, independent, so no x-1. So x-1 available unless x=1.
- x-1 adjacent to B's set: x-1 adjacent to n (x-1=n-1, x=n, but n taken by B, A can't pick n) — impossible. x-1 adjacent to x_j-1: iff x adjacent to x_j — no (A independent). So not adjacent.

So for B_first=n, preferred x-1 is illegal ONLY when x=1 (A picked 1). Similarly for B_first=1, preferred x+1 illegal only when x=n (A picked n).

So the fallback triggers exactly when A picks the "near" endpoint (the endpoint on A's own side, which B didn't take):
- B_first=n (A's first a ≤ c): fallback when A picks 1 (the left endpoint).
- B_first=1 (A's first a > c): fallback when A picks n (the right endpoint).

So the only complication: A picks the endpoint on A's side. Let me handle this.

When B_first=n and A picks 1 (as a later move): B's preferred x-1=0 invalid. Fallback: other side = x+1 = 2. Is 2 legal? 2 available? 2 not in A's set (A has 1, independent, no 2... wait A has 1 now, and A's set is independent so A doesn't have 2; but is 2 taken by B? B has n and x_j-1's. 2 = x_j-1 → x_j=3, so if A previously picked 3, B took 2. Then 2 unavailable.). Hmm, so 2 might be unavailable if A previously picked 3.

This is getting complicated. Let me think about the structure more carefully to find a clean proof.

Let me reconsider. Maybe instead of pushing "away from B's endpoint," I should push "toward B's endpoint" but with B's endpoint on the FAR side from A. Wait, that's H1. H1 also only won odd n. Let me reconsider H1's fallback structure. Actually both H1 and H2 have the same issue.

Let me think differently. Let me reconsider the actual minimax strategy structure for odd n and find the clean invariant.

Let me reconsider the minimax traces for odd n:
n=9:
A=1: B=9,3→2,5→4,7→6. (B: 9,2,4,6)
A=2: B=1,4→3,6→5,8→7. (B: 1,3,5,7)
A=3: B=1,5→4,7→6,9→8. (B: 1,4,6,8)
A=4: B=1,2→3,6→5,8→7. (B: 1,3,5,7)
A=5: B=1,2→3,7→6,9→8. (B: 1,3,6,8)
A=6: B=1,2→3,4→5,8→7. (B: 1,3,5,7)
A=7: B=1,2→3,4→5,9→8. (B: 1,3,5,8)
A=8: B=1,2→3,4→5,6→7. (B: 1,3,5,7)
A=9: B=1,2→3,4→5,6→7. (B: 1,3,5,7)

Observation: In ALL cases, B's first move is 1 (except A=1 where it's 9). And B's set ends up being {1 or 9, and then a mix}. 

Let me look at A's final set and B's final set:
A=1: A={1,3,5,7}, B={9,2,4,6}. Remaining {8}. 
A=2: A={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=3: A={3,5,7,9}, B={1,4,6,8}. Remaining {2}.
A=4: A={4,2,6,8}={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=5: A={5,2,7,9}={2,5,7,9}, B={1,3,6,8}. Remaining {4}.
A=6: A={6,2,4,8}={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=7: A={7,2,4,9}={2,4,7,9}, B={1,3,5,8}. Remaining {6}.
A=8: A={8,2,4,6}={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=9: A={9,2,4,6}={2,4,6,9}, B={1,3,5,7}. Remaining {8}.

Hmm interesting. In many cases A ends up with {2,4,6,8} (all even except...) and B with {1,3,5,7}, remaining 9. That's the parity partition MINUS one number! A has evens 2,4,6,8, B has odds 1,3,5,7, remaining 9 (odd). For a draw, A would need all evens {2,4,6,8} and B all odds {1,3,5,7,9}. But B only has 4 odds, missing 9. And 9 is remaining but blocked (A's 8 blocks 9). So A can't take 9, and B already... wait it's A's turn and A is stuck. So the draw is broken because B didn't take 9 (the last odd), and A can't take it either (blocked by own 8). So 9 remains unclaimed → not a draw, and A can't move → A loses.

So the structure: B forces the game to ONE number short of the parity partition, where the last number is blocked by A's own piece. 

Specifically: A ends with all of one parity class except the game stops one short. The remaining number is of B's parity, blocked by A's adjacent number.

This is the key insight! B's strategy: force A to take all numbers of one parity (say all evens or all odds except boundary), while B takes the other parity, leaving exactly one number of B's parity that A can't take (blocked by A's neighbor) and it's A's turn.

Hmm, but in A=1 case: A={1,3,5,7} (odds except 9), B={9,2,4,6} (9 is odd! plus evens 2,4,6). Remaining 8 (even). So here A took odds {1,3,5,7} (missing 9 which B took!), B took 9 (odd) + evens {2,4,6}. Remaining 8 (even), blocked by A's 7. So B "stole" odd 9, breaking A's parity collection, and the remaining even 8 is blocked by A's 7.

So B's strategy: B steals one number of A's "natural" parity (the parity of A's first move), then fills in, leaving A blocked.

This is subtle. Let me think about the clean invariant.

A's first move a has parity p. For a draw, A would need all numbers of parity p. B's first move: B takes a number of parity p (the endpoint of parity p on the far side)! 
- A=1 (odd): B takes 9 (odd). B stole an odd. ✓
- A=2 (even): B takes 1 (odd)? No, 1 is odd, A's parity is even. B took 1 (odd), not A's parity. Hmm. 

Wait A=2, B=1. A's parity = even. B took 1 (odd). So B did NOT steal A's parity here. But A ended with {2,4,6,8} (all evens), B with {1,3,5,7} (all odds), remaining 9 (odd). So A got ALL evens, B got odds except 9. The remaining 9 (odd, B's parity) is blocked by A's 8. So here B did NOT steal A's parity; instead, A completed its parity class (evens), but B is one short on odds (missing 9), and 9 is blocked by A's 8. It's A's turn, A can't take 9 (9 is odd, but also 9 adjacent to A's 8 → blocked). So A stuck.

So in this case, A successfully collected all its parity (evens), but the game isn't a draw because B didn't collect all odds (9 remains). And A can't take 9 (blocked). So A is stuck.

So the trap: A collects all of parity p, B collects all of the other parity except one number (an endpoint), and that endpoint is blocked by A's adjacent number. A is stuck because the only remaining number is of the other parity and adjacent to A's piece.

So B's strategy ensures: A is forced to collect ALL numbers of parity p (A's first move's parity), while B collects the other parity except one endpoint, which remains and is blocked by A.

How does B force A to collect all of parity p? By B always taking the other parity. If B always plays opposite parity to A, then A is forced to take parity p numbers (since B takes the others). But A might take a number of the opposite parity too... 

Hmm wait. Let me reconsider. If B always takes numbers of parity opposite to A's first move, then B claims all numbers of that opposite parity that it can. A claims parity p numbers. But A could also claim opposite-parity numbers (if available and legal). 

Let me reconsider. The key mechanism: B plays adjacent to A's moves (x±1), which are of opposite parity. So B's numbers are all opposite parity to A's numbers. Since A's numbers are all parity p (if A only picks parity p), B's numbers are all parity 1-p. 

But does A only pick parity p? A could pick opposite parity. Let me check: in A=1 case, A picked 1,3,5,7 all odd (parity p=odd). In A=2 case, A picked 2,4,6,8 all even. In A=5 case, A picked 5,2,7,9 = {2,5,7,9}: 5,7,9 odd, 2 even. So A picked mixed parity! So A doesn't always stick to one parity.

Hmm. So the "A collects one parity" isn't universal. Let me re-examine A=5 (n=9): A={2,5,7,9}, B={1,3,6,8}, remaining {4}. 4 is even, blocked by A's 5? 5's neighbors 4,6. Yes 4 blocked by 5. Also 4 blocked by... A's set {2,5,7,9}: 2's nbrs 1,3; 5's nbrs 4,6; 7's nbrs 6,8; 9's nbrs 8. So 4 blocked by 5. 6 blocked by 5,7. 8 blocked by 7,9. So remaining {4}, blocked. A stuck.

So in this case remaining is 4 (even), A's set has 2 (even), 5,7,9 (odd). B's set {1,3,6,8}: 1,3 odd, 6,8 even. So both players have mixed parity. The remaining 4 is blocked by A's 5.

So the clean "parity partition minus one" structure only appears in some cases. The A=5 case is messier.

OK, I think a fully clean proof of the n≥7 case is genuinely difficult and the official solution likely uses a clever but non-trivial strategy. Given my time constraints, let me construct a proof that:
1. Proves the parity characterization (clean).
2. Handles n=1..6 by explicit analysis.
3. For n≥7, presents B's strategy (H2 with the endpoint-fallback) and proves it works via a careful invariant argument.

Actually, let me reconsider and try to find a cleaner strategy for odd n that avoids fallback. The fallback is only triggered when A picks the near endpoint. What if B's strategy PREEMPTIVELY blocks the near endpoint?

For B_first=n (A's first a ≤ c): the near endpoint is 1. A might pick 1 later. What if B, instead of always x-1, plays x-1 but if x would be 1... A can't be forced not to pick 1. 

Alternatively: B_first = n, and B's strategy: play x-1, BUT if A ever picks 1, then B switches to a "sub-game" strategy on the remaining. When A picks 1, A's set has 1 (and previous A numbers). B has n and (x_j - 1)'s. After A picks 1, the number 2 is... B should play 2? But 2 might be taken (if A previously picked 3, B took 2). 

Hmm. Let me think about when A picks 1 in the B_first=n case. A picks 1 only if 1 is available (B didn't take it — correct, B took n) and 1 not adjacent to A's set (A has no 2). A has no 2 means A never picked 2, and B never... B could have 2 (if A picked 3, B took 2). If B has 2, then 1 is adjacent to B's 2 — but that's B's, doesn't affect A. A can still pick 1 (1 not adjacent to A's set). Wait, but if B has 2, is 1 still available? 1 available iff not taken. B has 2, not 1. So 1 available. A can pick 1 if A has no 2 (A's set). 

So A picks 1 when A's set has no 2. In the B_first=n strategy, B plays x-1. If A picks 3, B takes 2. Then A's set has 3, B has 2. A can't pick 2 (taken). Can A pick 1? 1 available, 1 adjacent to A's 3? No (1,3 not adjacent). 1 adjacent to A's other numbers? Depends. If A only has 3 (and first move), 1 not adjacent. So A could pick 1. Then B's x-1 = 0, fallback to x+1 = 2, but 2 taken by B! So fallback other side also unavailable. Then fallback to "any legal." 

So the strategy gets complicated. Let me just test: does the "any legal" fallback still win? The test said yes (H2 wins all odd n). But "any legal" is not a clean rule to prove.

Let me refine the fallback. When A picks 1 (near endpoint) in B_first=n case: B should play... let me look at what minimax does. Let me find a specific line where A picks 1 and see B's response.

Let me construct: n=9, A=3 (a=3 ≤ c=5, so B_first=9 under H2). A=3, B=9. Now A picks 1 (deviation). A={1,3}, f{2,4}. B's turn. What does minimax B play?

Let me compute.
So when A picks 1 (near endpoint) after B=9, B plays 2 (the other side, x+1=2). And it works: A={1,3}, B={9,2}, then A=5,B=4,A=7,B=6, A stuck (remaining 8, blocked by 7).

So the fallback "play x+1 when x-1 invalid" works here (2 = x+1 for x=1). And 2 was available (A hadn't picked 3 yet... wait A had picked 3 first! A={3,1}. So A has 3. B plays 2. 2 adjacent to A's 3? Yes but that's A's, doesn't matter for B. 2 adjacent to B's set {9}? No. So B plays 2 legally. Good.

But what if A picked 3 first (so B would have taken 2 in normal play)? In this line, A=3 was the FIRST move, B=9 (B didn't take 2). Then A=1, B=2. So B takes 2 now. Fine.

But consider: A=3, B=9, A=5, B=4, A=1. Now A={1,3,5}, B={9,4}. B wants to respond to A=1. x-1=0 invalid. x+1=2. 2 available? A has 1,3,5; B has 9,4. 2 not taken. 2 adjacent to B's set {9,4}? 2 adjacent to 4? No (2,4 not adjacent, diff 2). 2 adjacent to 9? No. So B plays 2. Then trace: A=7,B=6, stuck. Good. (Matches the second exploration: B=2, A=7, B=6, stuck.)

So the fallback "x+1 when x-1 invalid" works. But is x+1 always legal when x-1 is invalid (x=1)? x+1=2. 2 available? 2 taken iff A or B has 2. A has 2? A has 1 (just picked), A's set independent so A doesn't have 2. B has 2? B has {n, x_j-1 for previous}. B has 2 iff some x_j - 1 = 2, i.e., A previously picked 3. So if A previously picked 3, B has 2, and now A picks 1, B can't play 2 (taken). Then fallback to "any legal."

When would A have picked 3 before picking 1? A=3 (first), B=9, then A picks 1 (not 3 again). Here A's first is 3, B=9. A didn't pick 3 "before" in a way that B took 2 — B took 9, not 2. So B doesn't have 2. So B can play 2. 

But what if: A=3 (first), B=9, A=5, B=4, A=7, B=6, A=1. Now A={1,3,5,7}, B={9,4,6}. B respond to A=1: x+1=2. 2 taken? B has {9,4,6}, no 2. A has {1,3,5,7}, no 2. So 2 available. B plays 2. Then remaining {8}. A's f from {1,3,5,7}: {2,4,6,8}. 8 blocked. A stuck. 

But wait, in this line, after A=7,B=6, it's A's turn with A={3,5,7}, B={9,4,6}, avail{1,2,8}. A's f{2,4,6,8}. A can pick 1 (not in f). A=1. Then B=2. A stuck. But could A have picked 8 instead of 1? A=8: 8 in A's f{2,4,6,8}? 8 is in f (adjacent to 7). So A can't pick 8. A can only pick 1. Forced. Then B=2, A stuck. Good.

So actually in this line A is forced to pick 1 (only legal move), and B plays 2, A stuck. The fallback works cleanly.

Now the question: is there a case where A picks 1 and B's x+1=2 is ALSO unavailable (B already has 2)? B has 2 only if A previously picked 3 (B took 2 = 3-1). But if A picked 3 and B took 2, then for A to later pick 1: A has 3 (so 1 not adjacent to 3, ok), 1 available (B has 2, not 1), A has no 2 (A's set). So A can pick 1. Then B wants 2, but 2 taken by B. Fallback to "any legal."

Let me construct: n=9, A=3 (first), B=9, A=5, B=4, A=1? Wait B took 4 (=5-1), not 2. B takes 2 only if A picks 3 as a NON-first move (B_first=n case, B plays x-1=2 for x=3). But A=3 as first move → B plays 9 (first move), not 2. So B takes 2 only when A picks 3 as a later move (after B's first). 

When does A pick 3 as a later move in B_first=n case? B_first=n means A's first a ≤ c. If a=1: A=1, B=9. Then A picks 3 (later). B plays 2 (=3-1). So B has 2. Then could A later pick 1? No, 1 is A's first move (taken). So A can't pick 1. So no conflict.

If a=2: A=2, B=9 (H2, since 2 ≤ c). A={2}, f{1,3}. A can't pick 1 or 3 (forbidden). So A never picks 3, B never takes 2 via x-1. So B never has 2. So if A later picks 1... A can't (1 forbidden by A's 2). So A never picks 1. No conflict.

If a=3: A=3, B=9. A picks 3 first. B doesn't take 2 (B took 9). Later A picks 5, B takes 4. A picks 7, B takes 6. A picks 1 (forced, as shown). B takes 2. B didn't have 2 before. Good.

If a=4: A=4, B=9 (H2, 4 ≤ 5). A={4},f{3,5}. A can pick 1,2,6,7,8. If A picks 2: B plays x-1=1. B takes 1! Then A can't pick 1 later. Good, no conflict (A picks 1 is now impossible). If A picks 6: B plays 5. etc. If A picks 1: B plays x-1=0 invalid → fallback x+1=2. 2 available? B has {9}, no 2. A has {4,1}, no 2. So B plays 2. Then A={1,4},f{2,3,5}. B={9,2},f{1,3,8}. avail{3,5,6,7,8}. A picks 6 or 7. ... Let me trust it works.

So the conflict (B already has 2 when A picks 1) requires A to have picked 3 as a later move AND B took 2, AND then A picks 1. But if A picked 3 (later), A has 3, and for A to pick 1: 1 not adjacent to 3 (ok), 1 available. But also A has 3 means A's set includes 3; does A have 2? No (independent). So A can pick 1. And B has 2 (took it when A picked 3). So B can't play 2. Conflict!

When does this happen? B_first=n (a ≤ c). A picks 3 as a LATER move (not first). So a ≠ 3, a ≤ c, a ∈ {1,2,4,5} (for n=9, c=5). 
- a=1: A=1 first. A can't pick 1 again. A picks 3 later? A={1},f{2}. 3 available, not forbidden. A could pick 3. B plays 2. B has 2. Then A picks 1? Can't (taken). No conflict.
- a=2: A=2, f{1,3}. A can't pick 3. So A never picks 3. No conflict.
- a=4: A=4, f{3,5}. A can't pick 3. No conflict.
- a=5 (center): A=5, f{4,6}. A can pick 3 (available, not forbidden). A=3 (later). B plays 2. B has 2. Then A picks 1? A={5,3}, f{2,4,6}. 1 available, not in f. A picks 1. B wants 2 (taken by B). Conflict! 

So n=9, A=5, B=9 (H2: 5 ≤ 5, B_first=9). A=3 (later), B=2. A=1, B wants 2 (taken). Fallback. Let me check this line with the strategy.

Actually wait, the H2 strategy for A=5 (n=9): B_first = 9 (since 5 ≤ c=5). But the minimax B_first for A=5 was 1, not 9! So H2 deviates from minimax here. Does H2 still win for A=5? The test said n=9 all A_loses under H2, so yes. But the fallback must handle the conflict. Let me trace H2 for n=9, A=5.

Let me trace H2 explicitly for n=9, A=5, with A playing optimally against H2.
A's avalue returns bestk=None when no legal moves (terminal). But in the loop, if A has legal moves, bestk should be set. The issue: when A has legal moves but all lead to... bestk should be set. Let me check: avalue initializes bestk=None, sets it when a better move found. If ALL moves give 'A_loses' (order 0), and best starts at 'A_loses' (0), then `order[r]>order[best]` is `0>0` False, so bestk never set! Bug. Let me fix: use >= or set bestk on first.

Let me fix to always pick a move (prefer the first that achieves best).
Now I see the H2 strategy clearly for odd n. Let me analyze the pattern.

For odd n, H2 strategy:
- B_first = n if A's first a ≤ c else 1 (c = (n+1)/2).
- Then B plays x-1 (if B_first=n) or x+1 (if B_first=1), with fallback to the other side.

Looking at the traces, the fallback (other side) is used in a few cases:
- n=9, A=3: B=9, A=1 (A picks near endpoint 1!), B=2 (fallback: x+1=2 since x-1=0 invalid). Then A=3? No A already has 3. A=5,B=4,A=7,B=6. 
  Wait A=3 first, then A=1. A={3,1}. B=9, then B=2. Then A=5,B=4,A=7,B=6. A={1,3,5,7}, remaining 8, blocked. 
- n=9, A=4: B=9, A=1, B=2 (fallback). A=6,B=5,A=8,B=7. A={1,4,6,8}? wait A=4 first, then A=1, A=6, A=8. A={1,4,6,8}, B={9,2,5,7}, remaining {3}. A's f from {1,4,6,8}: {2,3,5,7,9}. 3 blocked. stuck. 
- n=9, A=5: B=9, A=1, B=2 (fallback). A=3, B=4 (fallback? x-1=2, but 2 taken by B; so other side x+1=4). A=7,B=6. A={1,3,5,7}? wait A=5 first, A=1, A=3, A=7. A={1,3,5,7}, B={9,2,4,6}, remaining 8, blocked. 
  Here B=4 is fallback (x-1=2 taken, x+1=4). 

So the fallback to "other side" is used, and it works. Now I need to prove this strategy works for all odd n ≥ 7.

This is still complex but let me try to find the invariant. Let me look at the structure of the traces:

For B_first=n case (a ≤ c): 
- A's moves: a (first), then a sequence. B: n, then x-1's (with fallbacks).
- In many traces, A ends up with {1, 3, 5, ..., n-2} (all odd numbers from 1 to n-2) and B with {n, 2, 4, ..., n-1} (n plus all evens), remaining n-1? No wait.

Let me look at n=11:
A=1: A={1,3,5,7,9}, B={11,2,4,6,8}, remaining {10}. 10 blocked by 9. 
A=2: A={2,4,6,8,10}, B={11,3,5,7,9}, remaining {1}. 1 blocked by 2. 
A=3: A={3,1,5,7,9}={1,3,5,7,9}, B={11,2,4,6,8}, remaining {10}. 
A=4: A={4,1,6,8,10}={1,4,6,8,10}, B={11,2,5,7,9}, remaining {3}. 3 blocked by 4. 
A=5: A={5,1,3,7,9}={1,3,5,7,9}, B={11,2,4,6,8}, remaining {10}. 
A=6: A={6,1,3,8,10}={1,3,6,8,10}, B={11,2,4,7,9}, remaining {5}. 5 blocked by 6. 

So in all B_first=n cases (a ≤ c=6 for n=11), A ends with a set, B ends with a set, and ONE number remains, blocked by A's adjacent number.

Pattern for B_first=n: A's final set = {1,3,5,...,n-2} (all odds from 1 to n-2) OR a set containing 1 and some structure. B's final set = {n} ∪ {2,4,...,n-1} (n plus all evens) OR similar. Remaining = n-1 (even, blocked by A's n-2) in the clean cases.

Wait, A=1: A={1,3,5,7,9}, B={11,2,4,6,8}, remaining 10. 10 = n-1. Blocked by A's 9 = n-2. 
A=2: A={2,4,6,8,10}, B={11,3,5,7,9}, remaining 1. 1 blocked by A's 2. Here remaining is 1 (the near endpoint), blocked by A's 2.
A=3: same as A=1 (A={1,3,5,7,9}), remaining 10.
A=4: A={1,4,6,8,10}, B={11,2,5,7,9}, remaining 3. 3 blocked by A's 4.
A=5: A={1,3,5,7,9}, remaining 10.
A=6: A={1,3,6,8,10}, B={11,2,4,7,9}, remaining 5. 5 blocked by A's 6.

So the remaining number is always blocked by an A number adjacent to it. And it's always A's turn when stuck. Total moves: 5 A + 5 B = 10, remaining 1. n=11, 10 moves, 1 remaining. A's 5th move is the last A move, then B's 5th, then A stuck (6th A move attempted). Wait: moves 1(A),2(B),...,10(B), then A's 6th turn, stuck. So A made 5 moves, B made 5 moves, 11-10=1 remaining. A stuck.

So the strategy ensures: after 5 rounds (A and B each move 5 times), exactly 1 number remains, and it's blocked by A's set, and it's A's turn. 

The invariant: B's strategy ensures A is forced to "fill in" a contiguous-ish block such that one number remains blocked.

This is still complex. Let me try to find the precise invariant for the B_first=n case.

Let me define the B_first=n case (A's first a ≤ c). B plays n, then x-1 (fallback x+1).

Let me think about it as: B is building the set {n, 2, 4, 6, ..., n-1} (n plus evens) and A is forced into {1, 3, 5, ..., n-2} (odds except n), with n-1 remaining blocked by n-2.

But A doesn't always cooperate (A=4,6 cases show A takes some evens). Yet B still wins. So the invariant is more robust.

Let me think about it as a "pairing" argument. B's strategy (B_first=n, play x-1): B pairs each A move x (after first) with x-1. So B claims {n} ∪ {x_i - 1}. 

Hmm, let me think about the "shadow" of A's set. B's set (excluding n) = {x-1 : x ∈ A's set, x ≠ first move}. So B's set = {n} ∪ (A's set minus first move, shifted down by 1).

A's set = {a} ∪ {x_2, ..., x_k}. B's set = {n} ∪ {x_2-1, ..., x_k-1}.

For A to be stuck after k A-moves: remaining numbers all blocked by A. Remaining = [n] \ (A's set ∪ B's set) = [n] \ ({a, x_2,...,x_k} ∪ {n, x_2-1,...,x_k-1}).

This is getting algebraic. Let me think about the total count. n odd. A makes k moves, B makes k moves (B moves after each A move; game ends on A's (k+1)th attempt). Total 2k taken, n - 2k remaining. For n=11, k=5, 2k=10, 1 remaining. For n=9, k=4, 2k=8, 1 remaining. For n=7, k=3, 2k=6, 1 remaining. So k = (n-1)/2, remaining = 1. 

So for odd n, the game ends with A making (n-1)/2 moves, B making (n-1)/2 moves, 1 number remaining, A stuck. So B's strategy ensures A is stuck after exactly (n-1)/2 rounds with 1 number left.

So I need to show: B's strategy ensures (a) B always has a legal move for (n-1)/2 rounds, (b) after (n-1)/2 rounds, exactly 1 number remains and it's blocked by A, (c) A is forced to keep moving (can't get B stuck).

Hmm, this is a lot. Let me reconsider whether there's a cleaner high-level proof.

Actually, let me reconsider the whole approach. This problem is clearly quite hard (irregular answer, complex strategy). Let me reconsider whether the intended answer might be different and cleaner, and my computation has an error.

Let me re-verify the computation independently with a different code style, especially n=6 (draw) and n=8 (B wins), since these are the surprising boundary cases.

Actually, I hand-verified n=6 draw carefully. And n=3,4,5. Let me re-verify n=7 and n=8 with a clean independent check.

n=7: B wins. Let me verify A=1 → B can force win. A=1, B=7 (mirror). Then A's options {3,4,5,6} (not 2, forbidden). 
  A=3: B=2 (per trace). A={1,3},f{2,4}. avail{4,5,6}. B={7,2},f{1,3,6}. A picks 5 (4 forbidden). A={1,3,5},f{2,4,6}. avail{4,6}. B={7,2},f{1,3,6}. B picks 4 (not in B's f). B={7,2,4},f{1,3,5,6}. avail{6}. A f{2,4,6}→6 blocked. stuck. 
    But wait, could A pick 6 instead of 5? A={1,3},f{2,4}. avail{4,5,6}. 6 not in f. A=6. A={1,3,6},f{2,4,5,7}. avail{4,5}. B={7,2},f{1,3,6}. B picks 4 (not in B's f{1,3,6}). B={7,2,4},f{1,3,5,6}. avail{5}. A f{2,4,5,7}→5 blocked. stuck. 
    A=4: A={1,4},f{2,3,5}. avail{3,5,6}. B={7,2},f{1,3,6}. B picks 5 (not in f). B={7,2,5},f{1,3,4,6}. avail{3,6}. A f{2,3,5}→3 blocked, 6? 6 not in A's f{2,3,5}. A=6. A={1,4,6},f{2,3,5,7}. avail{3}. B={7,2,5},f{1,3,4,6}. B can't pick 3 (in f). B stuck! B loses!
    
Uh oh. So if A=1, B=7, A=4, then B=5 (trace) leads to B getting stuck? Let me recheck. A={1,4}, B={7,2}. avail{3,5,6}. B's turn. B's f = neighbors of {7,2} = {1,3,6,8} → in range {1,3,6}. B can pick from avail{3,5,6} minus f{1,3,6} = {5}. So B MUST pick 5. B=5. B={7,2,5},f{1,3,4,6}. avail{3,6}. A's turn. A={1,4},f{2,3,5}. A can pick from avail{3,6} minus f{2,3,5} = {6} (3 in f). A=6. A={1,4,6},f{2,3,5,7}. avail{3}. B's turn. B={7,2,5},f{1,3,4,6}. B can pick from avail{3} minus f{1,3,4,6} = {} (3 in f). B stuck! B loses!

So A=1,B=7,A=4,B=5,A=6 → B stuck. So B=7 is NOT winning against A=4?! But the minimax said n=7 A=1 → B=7 wins (value from A = -1, B wins). Contradiction?

Wait, let me recheck. Maybe B shouldn't play 2 after A=1,B=7,A=4. Let me recompute. A=1, B=7, A=4. Now B's turn. B={7}, f{6}. avail{2,3,5,6}. B can pick 2,3,5 (not 6, in f). The trace said B=2. Let me check B=2: B={7,2},f{1,3,6}. avail{3,5,6}. A={1,4},f{2,3,5}. A picks 6 (only option, as 3,5 in f). A=6. A={1,4,6},f{2,3,5,7}. avail{3,5}. B={7,2},f{1,3,6}. B picks 5 (3 in f). B={7,2,5},f{1,3,4,6}. avail{3}. A={1,4,6},f{2,3,5,7}. A can't pick 3 (in f). A stuck! A loses.

Wait, I made an error before. Let me redo. After A=1,B=7,A=4,B=2,A=6: A={1,4,6}, B={7,2}. avail{3,5}. B's turn (move 6). B={7,2},f{1,3,6}. B can pick from {3,5} minus {1,3,6} = {5}. B=5. avail{3}. A's turn (move 7). A={1,4,6},f{2,3,5,7}. A can pick from {3} minus {2,3,5,7} = {}. A stuck. A loses. 

I previously wrote "B picks 4" which was wrong (4 already taken by A). Let me recheck: after A=1,B=7,A=4,B=2, avail = {3,5,6} (1,4,7,2 taken). A=6. avail={3,5}. B's turn. B={7,2}, f={1,3,6}. avail{3,5}. B can pick 5 (3 in f). B=5. avail{3}. A stuck. Yes A loses. I made an arithmetic error before (said B picks 4, but 4 taken). So B=7,A=4 line: A loses. Good, consistent with minimax.

OK so my hand analysis had an error; the code is right. Good.

Let me also double-check n=8 B wins independently for one line. n=8, A=1, B=8 (trace), A=3, B=5, A=6, B=2, A stuck. Let me verify A can't escape. A=1,B=8. A's options {3,4,5,6,7} (not 2). 
  A=3: B=5. A={1,3},f{2,4}. avail{2,4,6,7}. B={8,5},f{4,6,7}. A picks 6 or 7 (2,4 in f; 6,7: 6 not in A's f, 7 not in A's f). 
    A=6: A={1,3,6},f{2,4,5,7}. avail{2,4,7}. B={8,5},f{4,6,7}. B picks 2 (4,7 in B's f). B={8,5,2},f{1,3,4,6,7}. avail{4,7}. A f{2,4,5,7}→4,7 blocked. stuck.
    A=7: A={1,3,7},f{2,4,6,8}. avail{2,4,6}. B={8,5},f{4,6,7}. B picks 2. B={8,5,2},f{1,3,4,6,7}. avail{4,6}. A f{2,4,6,8}→4,6 blocked. stuck.
  A=4: A={1,4},f{2,3,5}. avail{2,3,5,6,7}. B={8},f{7}. B's best? trace says B=5 (for A=3). For A=4, let me compute B's best. Actually the trace for A=1 was A=3 (optimal A). A=4 might be different. Let me trust minimax: n=8 A=1 → B wins (value -1). So all A responses lose. 

OK I'm confident in the answer. Now let me also handle even n ≥ 8. H1/H2 only draw for even n. I need a different strategy for even n ≥ 8.

Let me find a strategy for even n ≥ 8. Let me look at the minimax traces for even n again:
n=8:
A=1: B=8, A=3, B=5, A=6, B=2. 
A=2: B=1, A=4, B=3, A=6, B=8.
A=3: B=1, A=5, B=4, A=7, B=6.
A=4: B=1, A=2, B=3, A=6, B=8.
A=5: B=1, A=2, B=3, A=7, B=6.
A=6: B=1, A=2, B=4, A=8, B=7.
A=7: B=1, A=2, B=3, A=4, B=5.
A=8: B=1, A=2, B=4, A=5, B=6.

n=10:
A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4.
A=2: B=1, A=4, B=3, A=6, B=5, A=8, B=10.
...

Hmm, even n strategies are more complex. Let me look at the structure for even n. 

For even n, the parity partition has |odds| = |evens| = n/2. A and B each make n/2 - 1 moves before A gets stuck? Let me count n=8: A makes 3 moves, B makes 3 moves, 2 remaining, A stuck. n=8, 6 moves, 2 remaining. n=10: A makes 4, B makes 4, 8 moves, 2 remaining. So for even n, A makes (n-2)/2 moves, B makes (n-2)/2 moves, 2 remaining, A stuck.

So B's strategy for even n ≥ 8: force A stuck with 2 numbers remaining.

Let me find a clean strategy for even n. Let me test some candidates. 

Looking at n=8 traces, B's first move: A=1→B=8, A=2..8→B=1. Same as odd: B picks 1 if available else n. Then B's subsequent moves vary.

Let me look at n=8, A=1: B=8, A=3, B=5 (not x-1=2, not x+1=4). B=5. Hmm. Then A=6, B=2 (x-4? no). 

n=8, A=1: B=8. A=3. B=5. Why 5? After A=1,B=8,A=3: A={1,3},f{2,4}. avail{2,4,5,6,7}. B={8},f{7}. B can pick 2,4,5,6 (not 7). B picks 5. 

Then A={1,3},f{2,4}. avail{2,4,6,7}. A picks 6 or 7. A=6 (trace). A={1,3,6},f{2,4,5,7}. avail{2,4,7}. B={8,5},f{4,6,7}. B picks 2. avail{4,7}. A stuck.

So B's strategy for even n is different and more complex. Let me try to find a pattern by testing strategies.

Let me think about even n differently. For even n, maybe B uses a strategy based on the center two elements.

Actually, let me reconsider. For even n, the reflection strategy gives a draw. B needs to deviate to win. The deviation seems to involve B taking a "central" number to break symmetry.

Let me look at n=8, A=1, B=8, A=3, B=5: B took 5, which is center-right (center of 8 is between 4 and 5). So B takes a central number to break the draw.

Hmm. Let me try to find a strategy for even n by testing. Let me consider strategy: B_first = 1 if avail else n. Then B plays... let me look at the pattern of B's moves relative to A.

n=8, A=1: B: 8, 5, 2. A: 1,3,6. 
n=8, A=2: B: 1, 3, 8. A: 2,4,6.
n=8, A=3: B: 1, 4, 6. A: 3,5,7.
n=8, A=4: B: 1, 3, 8. A: 4,2,6.
n=8, A=5: B: 1, 3, 6. A: 5,2,7.
n=8, A=6: B: 1, 4, 7. A: 6,2,8.
n=8, A=7: B: 1, 3, 5. A: 7,2,4.
n=8, A=8: B: 1, 4, 6. A: 8,2,5.

This is quite irregular. Let me see if there's a reflection-like structure. For A=1: A={1,3,6}, B={8,5,2}. Reflection of A={1,3,6} in n=8 is {8,6,3}. B={8,5,2}. Not reflection. 

Hmm. Let me try: is B's set = reflection of A's set minus something plus something? A={1,3,6}, refl={8,6,3}. B={8,5,2}. B has 8 (=refl of 1), 5 (not refl of 3=6, not refl of 6=3), 2 (not refl). No.

This is really irregular. Let me try a different approach: maybe for even n, B's strategy is to reduce to the odd (n-1) game by "sacrificing" one number.

Idea for even n ≥ 8: B's first move takes n (or 1). Then B treats the remaining n-1 numbers as an odd game? But n-1 is odd, and B's first move is one of the endpoints...

Actually, here's an idea: For even n, B's first move = 1 (if A didn't take 1) or n. This removes one endpoint. The remaining numbers {2,...,n} (if B took 1) or {1,...,n-1} (if B took n) form a path of length n-1 (odd). Now it's A's turn, and A has already made 1 move (a). B has made 1 move (endpoint). 

Hmm, but the odd game strategy requires B to move second in the sub-game. Let me think.

Actually, let me reconsider. After A's first move a and B's first move (endpoint), the remaining available numbers form a set. If B took 1 and a ≠ 1, remaining = {2,...,n} \ {a}, which is n-1 numbers (odd count) but not contiguous (a removed). If a is interior, it splits into two intervals.

This is getting complicated. Let me just try to find a working strategy for even n by testing more candidates, or accept that the even n case needs a more complex strategy and try to construct one based on the odd case.

**Key idea for even n**: B's first move takes an endpoint (1 or n). Then B plays the odd-n strategy on the remaining n-1 numbers, treating A's first move as the "first move" of the sub-game and B's endpoint as already placed.

Wait, the odd-n strategy for n-1 (odd) requires B to respond to A's first move in the sub-game by taking the opposite endpoint of the sub-game. But B already took an endpoint of the original board...

Let me think concretely. Even n. A picks a. B picks 1 (assume a ≠ 1; if a=1, B picks n, symmetric). Now remaining = {2,3,...,n}\{a}. B has {1}. A has {a}. A's turn. 

Now B wants to apply an odd-game strategy on the interval [2, n] (length n-1, odd). In this sub-game, the "numbers" are 2,...,n. A has already placed a (in this interval). B has placed 1 (outside, but 1 is adjacent to 2, so B's piece at 1 affects B's legality for 2). Hmm, B's piece at 1 means B can't play 2 (adjacent). 

In the odd strategy on [2,n] (length n-1), B's first response should be the opposite endpoint. The endpoints of [2,n] are 2 and n. A placed a in [2,n]. If a ≤ center of [2,n] = (2+n)/2 = (n+2)/2, B takes n; else B takes 2. But B can't take 2 (adjacent to B's 1)! So B takes n (if a is in lower part) — that's fine. If a is in upper part (a > (n+2)/2), B would want to take 2, but can't (adjacent to 1). Problem.

So this only works if A's first move a is in the lower part of [2,n], i.e., a ≤ (n+2)/2, i.e., a ≤ n/2 + 1. For a > n/2+1, B can't take 2. 

By symmetry, if a is in the upper part, B should take n first (not 1), then apply the strategy on [1, n-1]. Let me reconsider: B takes the endpoint NEAR a? Or FAR?

Let me reconsider. If a is in lower half (a ≤ n/2), B takes n (far endpoint). Remaining [1, n-1]\{a}, B has {n}. B's piece at n affects n-1 (B can't play n-1). Sub-game on [1,n-1] (length n-1, odd). A placed a. B's response: opposite endpoint of [1,n-1] = endpoints 1 and n-1. If a ≤ center=(n)/2, B takes n-1; else B takes 1. But B can't take n-1 (adjacent to n)! So B takes 1 (if a > n/2) — but a ≤ n/2 (lower half), so a ≤ n/2, B would take n-1, can't. Problem again.

Hmm. The issue: B's endpoint piece blocks the adjacent sub-game endpoint.

Let me reconsider. Maybe B takes the endpoint on the SAME side as a, then plays the odd strategy pushing A toward the far (open) side.

If a ≤ n/2 (lower), B takes 1 (same side, near). Remaining [2,n]\{a}. B has {1}, blocks 2 for B. Sub-game [2,n] (odd length n-1). A placed a (in [2,n], lower part since a ≤ n/2 ≤ (n+2)/2). B's odd-strategy first response: opposite endpoint of [2,n] = n (since a in lower part). B takes n. OK! B can take n (not blocked). Then B plays x-1 (push toward... in odd strategy, B_first=n means play x-1, pushing A right toward n). Wait, in the odd strategy on [2,n] with B_first=n, B plays x-1. But x-1 could be 1 (if x=2), which is taken by B (B has 1). Or x-1 could be a-1... 

This is getting complicated but might work. Let me just test it: even n strategy = "B takes 1 if a ≤ n/2 else n (same-side endpoint); then apply odd-strategy H2 on the remaining interval."

Actually, let me just directly test a strategy for even n: B_first = 1 if a ≤ n/2 else n. Then B plays x-1 if B_first=n else x+1 (push away from B's endpoint), with fallback. Wait, that's H1/H2 which only drew. 

Hmm. Let me reconsider. The issue is even n needs a genuinely different approach. Let me look at the n=8 minimax more carefully and reverse-engineer.

n=8, A=1: B=8. (B took FAR endpoint, since a=1 ≤ 4.) Then A=3, B=5. 
n=8, A=2: B=1. (B took NEAR endpoint? a=2 ≤ 4, but B took 1, the near/same-side.) 
n=8, A=3: B=1. (a=3 ≤ 4, B took 1, same-side.)
n=8, A=4: B=1. (a=4 = n/2, B took 1.)
n=8, A=5: B=1. (a=5 > 4, B took 1, opposite-side.)
n=8, A=6: B=1.
n=8, A=7: B=1.
n=8, A=8: B=1. (a=8, B took 1, opposite.)

So for n=8, B takes 1 unless a=1 (then takes 8). So B_first = 1 if available else 8. Same rule as odd n! "B takes 1 if available, else n."

Then subsequent moves. Let me look at n=8, A=1, B=8, A=3, B=5: B's second move is 5. A=3, B=5. 5 = ? Not x-1=2, not x+1=4. 5 is... reflection of 3 in n=8 is 6. Not 5. 5 = 3+2. Hmm.

Let me look at all of B's second moves for n=8:
A=1,B=8: A=3→B=5. 
A=2,B=1: A=4→B=3. (x-1)
A=3,B=1: A=5→B=4. (x-1)
A=4,B=1: A=2→B=3. (x+1)
A=5,B=1: A=2→B=3. (x+1)
A=6,B=1: A=2→B=4. (x+2? no. 2+2=4. or reflection of 2 in [1,8] is 7. no.) Hmm B=4 for A=2. 
A=7,B=1: A=2→B=3. (x+1)
A=8,B=1: A=2→B=4. (x+2)

So mostly x±1, but A=1 case B=5 (x+2), A=6 and A=8 cases B=4 (x+2). Irregular.

This even-n strategy is genuinely complex. I'm spending a lot of time. Let me reconsider the proof approach.

Given the complexity, maybe the cleanest proof for the even n ≥ 8 case is to reduce to the odd case via a different mechanism, OR to use a strategy I can verify computationally for a base case and then use induction.

**Induction idea for even n**: Show B wins for n ≥ 8 by induction, reducing n by 2. Base cases n=8, 10 (verified computationally). Induction: if B wins for n, B wins for n+2.

How to reduce n+2 to n? B's strategy on n+2: B's first move takes one of the new endpoints (n+1 or n+2), and "pair off" the two new numbers, reducing to the n-game.

Concretely: for n+2 (numbers 1..n+2), B's strategy: 
- If A's first move a is in [1, n], B plays n+2 (or n+1), and then plays the n-game strategy on [1,n], treating n+1, n+2 appropriately.
- If A's first move is n+1 or n+2, B plays the other, and... 

Hmm, the new numbers n+1, n+2 interact with n (adjacency). 

Let me think about a cleaner reduction. Pair (n+1, n+2). B's strategy: whenever A plays in {n+1, n+2}, B plays the other. And B plays the n-strategy on [1,n]. But A playing n+1 or n+2 affects A's legality for n (if A takes n+1, A can't take n later, and A can't take n+2). 

This is getting complicated. Let me think about whether induction can work cleanly.

Actually, let me reconsider. Let me think about the structure: for even n ≥ 8, B wins with 2 numbers remaining. For odd n ≥ 7, B wins with 1 number remaining. 

Let me try to find a unified strategy that works for BOTH odd and even n ≥ 7. Let me test the minimax-style "B takes 1 if avail else n, then play adaptively" — but that's just minimax.

Let me try a different unified strategy: B takes 1 if avail else n. Then B plays to "mirror A's move in the sub-board excluding B's endpoint." Hmm.

Actually, let me reconsider. Let me try the strategy: B takes 1 if avail else n. Then B plays (A's last move) reflected in the remaining board... 

Let me just try to find ANY clean strategy for even n by testing a few more candidates.

Candidate E1: B_first = 1 if avail else n. Then B plays x-1 if legal else x+1 if legal else any. (This is "push left" primarily.) Test for even n.

Candidate E2: B_first = 1 if avail else n. Then B plays x+1 if legal else x-1 if legal else any. (Push right.)

Let me test these for even n.
All these simple strategies only draw for even n. The even-n winning strategy is genuinely more complex. 

Let me think about the even n case differently. The minimax for n=8, A=1: B=8, A=3, B=5. B's second move 5 is the KEY deviation. 5 is the "center-right" number. For even n, the center is between n/2 and n/2+1. B taking 5 (=n/2+1 for n=8) breaks the symmetry.

Let me hypothesize: for even n, B's strategy involves taking a central number at some point to break the draw.

Let me look at n=8 traces and find where B takes a central number (4 or 5):
A=1: B=8,5,2. B took 5 (central).
A=2: B=1,3,8. B took 3 (not central), 8.
A=3: B=1,4,6. B took 4 (central).
A=4: B=1,3,8. 
A=5: B=1,3,6. B took 6 (not central).
A=6: B=1,4,7. B took 4 (central).
A=7: B=1,3,5. B took 5 (central).
A=8: B=1,4,6. B took 4 (central).

So B often takes a central number (4 or 5). The strategy seems to be: B takes 1 (or 8), then takes a central number to break symmetry, then cleans up.

This is complex. Let me think about a cleaner conceptual approach for even n.

**Conceptual approach for even n ≥ 8**: 

For even n, a draw requires A to take all of one parity and B the other. B's strategy: B takes 1 (or n) first. This is a number of some parity. Then B plays to force A into a trap.

Hmm, let me think about the parity. For even n, |odds| = |evens| = n/2. A and B each make (n-2)/2 moves before A gets stuck (2 remaining). Wait, n=8: A makes 3 = (8-2)/2 moves. B makes 3. 2 remaining. For a draw, A would make n/2 = 4 moves and B n/2 = 4 moves, all chosen. But A gets stuck after 3 moves. So B prevents A from making the 4th move.

Let me think about the parity partition for even n. Draw requires A = odds (n/2 numbers) and B = evens, OR A = evens, B = odds. A makes n/2 moves in a draw. B prevents A's n/2-th move by making A stuck after n/2 - 1 moves.

B's strategy: B takes 1 (odd). Now for a draw, if A wants odds, A needs all odds including 1 — but 1 taken by B. So A can't get all odds. So A must get all evens for a draw. A needs {2,4,6,...,n}. B needs to prevent this.

B took 1 (odd). For a draw, A = evens = {2,4,...,n}, B = odds = {1,3,5,...,n-1}. B already has 1 (odd, good for B's parity). B needs to take all other odds {3,5,...,n-1} and prevent A from taking all evens.

A's first move a. If a is even, A is going for evens (consistent with draw). If a is odd, A already deviated from "A=evens" (A took an odd), so draw would require A=odds, but 1 taken by B, so A can't get all odds → no draw possible already! So if A's first move is odd (and B took 1), draw is impossible. Then someone wins. B needs to ensure A loses (not B).

If A's first move is even, draw is still possible (A=evens, B=odds). B needs to break it.

So B's strategy depends on parity of A's first move. Let me consider:

Case 1: A's first move a is odd (B took 1). Draw impossible (A can't get all odds since B has 1, and A has an odd a so A≠evens). So the game must end in a win for someone. B needs to win.

Case 2: A's first move a is even (B took 1). Draw possible (A=evens, B=odds). B needs to break the draw and win.

This is still complex. Let me just try to find a working strategy by testing a smarter candidate.

Let me try: B takes 1 if avail else n. Then B plays to take the "reflection" of A's move but shifted, OR play adjacent. Let me look at the actual minimax B moves for n=8 and try to find the rule.

n=8, A=1, B=8: then A=3, B=5. A=6, B=2.
Let me think: after A=1, B=8, the remaining is {2,3,4,5,6,7}. A=3. B=5. 5 is the reflection of 3 in {2,...,7}? Reflection in [2,7]: 2+7-3 = 6. Not 5. Reflection in [2,8]: 2+8-3=7. No. 

Hmm. 5 = 3 + 2. Or 5 is the center of [2,7] is 4.5, and 5 is center+0.5. 

Let me think about it as: B takes the number that is "opposite" to A in the remaining board, but the remaining board excludes B's piece at 8. The remaining available is {2,3,4,5,6,7}. Center is 4.5. A took 3 (left of center). B takes 5 (right of center, symmetric: 3 and 5 are symmetric about 4.5? 4.5-3=1.5, 5-4.5=0.5. No.). 3 and 6 are symmetric about 4.5. So B should take 6 by symmetry, but takes 5. 

I can't find a simple rule. Let me just accept that the even-n strategy is complex and try the induction approach, or find a strategy by more extensive search.

Let me try a strategy based on "B maintains A's set within a shrinking interval." Or let me try strategies with more complex rules and test.

Actually, let me try the strategy: B takes 1 if avail else n. Then B plays (A's last move) ± 1, choosing the side that is NOT adjacent to B's existing pieces and pushes A toward the larger gap. 

Alternatively, let me try: B plays the reflection of A's last move in the CURRENT available set's "center of mass"... too complex.

Let me try a cleaner idea: for even n, B's strategy is the same as odd n strategy but on n-1 (treating one endpoint as already taken). Specifically:

Even n strategy: B takes 1 if A's first move a ≠ 1, else n. (B takes an endpoint.) Now consider the sub-board excluding B's endpoint. If B took 1, sub-board is {2,...,n} (n-1 numbers, odd). A has made 1 move (a, which is in {2,...,n} if a≠1, or a=1 means B took n and sub-board {1,...,n-1}). Now apply the ODD strategy on the sub-board, where A's first move is a (in the sub-board), and B's "first move" in the sub-board is the opposite endpoint of the sub-board.

But B already used its first move on the original endpoint (1 or n). In the sub-board {2,...,n}, B's odd-strategy first move should be the opposite endpoint: if a ≤ center of sub-board, B takes n; else B takes 2. But B already took 1 (outside sub-board). B's piece at 1 blocks 2 for B. So if the odd strategy says "B takes 2," B can't. 

When does odd strategy say "B takes 2" in sub-board {2,...,n}? When a > center of {2,...,n} = (n+2)/2 = n/2 + 1. So if a > n/2+1, B can't take 2. 

So this works only if a ≤ n/2+1 (then B takes n in sub-board, which is fine). For a > n/2+1, by symmetry B should take n first (original), sub-board {1,...,n-1}, and odd strategy takes 1 if a > center of {1,...,n-1} = n/2. If a > n/2, B takes 1 in sub-board — but B already took n (original), and 1 is in sub-board, B can take 1 if not blocked. B's piece at n blocks n-1, not 1. So B can take 1. Good. But wait, if a > n/2+1, is a > n/2? Yes. So B takes n (original first), sub-board {1,...,n-1}, odd strategy: a > n/2 → B takes 1. B takes 1. OK.

But what about a = n/2+1 exactly? a ≤ n/2+1 → B takes 1 (original), sub-board {2,...,n}, a = n/2+1 = center of sub-board. Odd strategy: a ≤ center → B takes n (opposite endpoint of sub-board). B takes n. Fine.

And a = n/2? a ≤ n/2+1 → B takes 1 (original), sub-board {2,...,n}, a = n/2 ≤ (n+2)/2 = n/2+1. a ≤ center → B takes n. Fine.

So the strategy: 
- If a ≤ n/2 + 1: B takes 1 (original endpoint). Sub-board {2,...,n}. Apply odd strategy on {2,...,n} with A's first move a: B's sub-first-move = n (opposite endpoint, since a ≤ center). Then B plays x-1 (odd strategy, B_sub_first = n → play x-1).
- If a > n/2 + 1: B takes n (original endpoint). Sub-board {1,...,n-1}. Apply odd strategy on {1,...,n-1}: B's sub-first-move = 1 (since a > center of {1,...,n-1} = n/2). Then B plays x+1 (B_sub_first = 1 → play x+1).

Wait, but B's "original first move" and "sub-first move" are TWO moves. B only gets one move per A move. Let me reconsider. B's first move (response to A's first) = the original endpoint. Then B's SECOND move (response to A's second) = the sub-board's opposite endpoint. Then B's subsequent moves = x±1.

So:
- B move 1 (response to A's first a): take 1 if a ≤ n/2+1, else n.
- B move 2 (response to A's second): take the opposite endpoint of the sub-board. If B took 1, sub-board {2,...,n}, B takes n. If B took n, sub-board {1,...,n-1}, B takes 1.
  But wait, B taking n on move 2: is n available? B took 1 on move 1, so n available (unless A took n). A's first move a ≤ n/2+1 < n (for n≥8), so A didn't take n. So n available. B takes n. But is n legal for B? B has {1}, n not adjacent to 1 (n ≥ 8). Yes. Good.
  Similarly B takes 1 on move 2 if B took n on move 1: 1 available (A's first a > n/2+1 ≥ 5, so a ≠ 1), 1 legal (B has {n}, 1 not adjacent). Good.
- B moves 3+ (response to A's third+): play x-1 (if B's sub-first was n) or x+1 (if B's sub-first was 1), with fallback.

So B takes BOTH endpoints (1 and n) in its first two moves! Then plays x±1 to push A.

Let me reconsider. After B takes 1 and n (two endpoints), the remaining board is {2,...,n-1} (n-2 numbers, even). A has made 2 moves (a and a2). B has {1, n}. Now B plays x-1 or x+1 to push A toward... 

Hmm wait, this is now an even-length board {2,...,n-1} with B holding both endpoints. Let me reconsider whether this reduces to the odd strategy.

Actually, let me reconsider. The odd strategy on a board of length m (odd) has B taking one endpoint and pushing A toward the other end, trapping A with 1 number remaining. Here, after B takes both endpoints of the original board, the sub-board {2,...,n-1} has length n-2 (even for even n). That's not odd. So the reduction isn't clean.

Let me reconsider. Maybe B takes only ONE endpoint and the sub-board is {2,...,n} (odd length n-1). Then B's sub-first move is the opposite endpoint n. So B takes 1 then n. After that, sub-sub-board {2,...,n-1} (even). Hmm.

Wait, I think I'm overcomplicating. Let me reconsider the odd strategy. In the odd strategy on {1,...,m} (m odd), B takes one endpoint (say m), then plays x-1 for each A move. The game ends with A stuck, 1 number remaining. B takes m and (n-1)/2 - 1 other numbers (x-1's), total (n-1)/2... let me recount. m odd, A makes (m-1)/2 moves, B makes (m-1)/2 moves, 1 remaining. B's moves: 1 (endpoint) + (m-1)/2 - 1 (x-1's) = (m-1)/2. Yes.

For even n, I want A stuck with 2 remaining. A makes (n-2)/2 moves, B makes (n-2)/2 moves. B's moves: 2 (endpoints) + (n-2)/2 - 2 (x±1's) = (n-2)/2. So B takes both endpoints and then (n-6)/2 push moves. 

So the strategy: B takes both endpoints (1 and n) in first two moves, then pushes A with x±1, trapping A with 2 remaining.

Let me formalize and test:
- B move 1: take 1 if a ≠ 1, else n. (Take an endpoint not taken by A.)
  Actually, if a = 1, B takes n. If a = n, B takes 1. If a interior, B takes 1 (say).
- B move 2: take the other endpoint (n if B took 1, or 1 if B took n). Available (A's second move a2 ≠ endpoints? A might take an endpoint as second move!). 

Hmm, A's second move could be an endpoint. If B took 1, A's second move could be n. Then B can't take n (taken by A). Problem.

When would A take n as second move? A's first a (interior or =1). If a=1, B took n. A's second can't be n (taken). If a interior, B took 1. A's second could be n (if n available and legal for A). A takes n if n not adjacent to A's set (A has no n-1). 

So A could take n as second move, blocking B's plan to take n. Let me handle: if A takes an endpoint, B adapts.

This is getting complicated again. Let me just test the "B takes both endpoints then pushes" strategy with fallback and see if it wins for even n.

Let me define strategy E4:
- B move 1: take 1 if available else n.
- B move 2: take n if available (and legal) else 1 if available else (the endpoint not yet taken by anyone)... actually take the other endpoint if available.
- B move 3+: take x-1 if B's "push direction" is left, else x+1. Push direction: if B has both 1 and n, push toward... hmm. 

Actually, let me reconsider. After B takes both endpoints, A is confined to {2,...,n-1}. B pushes A toward one side. But which side? In the odd strategy, B pushes A toward B's endpoint (the one B took first). Here B has both endpoints. 

Let me just test: B takes 1 (move1), n (move2), then plays x-1 (push A right toward n) with fallback. Or x+1 (push left toward 1). Let me test both.

Actually, let me reconsider the direction. In odd strategy with B_first=n, B plays x-1 (takes the number just LEFT of A's move), and A is pushed RIGHT toward n. The trap: A reaches n-2, B takes n-3, n-1 remains blocked by n-2, and n is B's. Wait, for odd n, B_first=n, A pushed right, A reaches n-2 (odd), remaining n-1 (even) blocked by n-2.

For even n with B holding both 1 and n: A is in {2,...,n-1}. If B pushes A right (plays x-1, taking left of A), A moves right toward n-1. A reaches n-2 (even), B takes n-3, remaining n-1 (odd) blocked by n-2, and n is B's. So A stuck with n-1 remaining. But also 1 is B's. So 2 numbers remain? Let me count. Even n, A makes (n-2)/2 moves, B makes (n-2)/2 moves. B's moves: 1, n, and (n-2)/2 - 2 push moves. Total B moves = (n-2)/2. A moves = (n-2)/2. Total = n-2. Remaining = 2. 

Hmm, 2 remaining. For A to be stuck, both remaining must be blocked by A. In the odd-style trap, only n-1 is blocked by n-2. The other remaining number (somewhere on the left) must also be blocked. 

Let me think. B holds 1 and n. A is pushed right. A's set = {a, a2, ..., } moving right. B's push moves take x-1 (left of each A move). The leftmost region: B has 1. The numbers near 1: 2 is adjacent to B's 1 (but that's B's, doesn't block A). A's leftmost move is a (first). If a > 2, then 2 is... available? 2 not taken (B has 1, n; A has a > 2). 2 adjacent to A's set? If A has no 3, then 2 not blocked. So 2 might be available and unblocked → A could play 2. Hmm.

This isn't clean. Let me just test computationally.

Let me test strategy E4: B takes 1 (m1) if avail else n; B takes n (m2) if avail&legal else 1 if avail&legal else any; then push x-1 (or x+1) with fallback. Test both push directions.
Still only draws. The "take both endpoints then push" doesn't win for even n. The even-n winning strategy is genuinely more subtle.

Let me reconsider. The minimax for n=8, A=1: B=8, A=3, B=5. B does NOT take 1 on move 2. B takes 5 (central). So B's strategy is NOT "take both endpoints." B takes 8, then 5 (central), then 2.

Let me reconsider the structure. n=8, A=1, B=8, A=3, B=5, A=6, B=2. Final: A={1,3,6}, B={8,5,2}, remaining {4,7}. Both 4,7 blocked by A (4 adj to 3, 7 adj to 6 and 8-B but 7 adj to A's 6). 

So B's set = {8, 5, 2} = {2, 5, 8}. These are spaced by 3. A's set = {1, 3, 6}. Remaining {4, 7}. 

Interesting: B's set {2,5,8} are all ≡ 2 mod 3. A's set {1,3,6} = {1,3,6}. Hmm, 1≡1, 3≡0, 6≡0 mod 3. Not clean.

Let me look at n=10, A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4. A={1,3,5,8}, B={10,2,7,4}={2,4,7,10}, remaining {6,9}. 6 blocked by A's 5 (and B's 7). 9 blocked by A's 8 (and B's 10). So both remaining blocked by A.

B's set {2,4,7,10}. A's set {1,3,5,8}. Hmm.

This is really irregular. I'm not finding a clean pattern for even n.

Let me step back and think about whether there's a fundamentally different, cleaner approach to the whole problem that I'm missing.

Let me reconsider the problem from the parity perspective for a potential clean proof.

**Parity Lemma**: Draw ⟺ A's final set = {odds}, B's = {evens} (or swap). [Because path's only 2-coloring is parity.]

Now, here's a key observation: **A moves first, so A makes ⌈n/2⌉ moves and B makes ⌊n/2⌋ moves in a full game (draw). For a draw, A must hold exactly one parity class.**

- If n odd: |odds| = ⌈n/2⌉ = A's move count, |evens| = ⌊n/2⌋ = B's move count. So A MUST hold odds, B MUST hold evens. (A can't hold evens since |evens| < A's move count.)
- If n even: |odds| = |evens| = n/2 = both move counts. So A holds odds or evens.

**Consequence for odd n**: For a draw, A must hold ALL odd numbers. In particular, A must hold 1 (if 1 is odd, yes) and n (n odd). 

B's strategy for odd n: B takes 1 or n (an odd endpoint) on its first move! Then A can't hold all odds → no draw. And B's pushing strategy ensures A gets stuck.

Wait, but for odd n, B's first move (minimax) is 1 (if A≠1) or n (if A=1). Both 1 and n are odd (n odd). So B takes an ODD number first. This breaks A's ability to hold all odds → no draw. Then B's push strategy traps A. 

For even n: A can hold odds OR evens. B taking one number doesn't immediately break both. B takes 1 (odd) → A can't hold all odds (missing 1), but A could still hold all evens. So B needs to also break A=evens. B would need to take an even number too. But B's first move is 1 (odd). B's second move... in minimax n=8, A=1, B=8 (even!), then B=5 (odd). So B took 8 (even) on move 1 (since A=1, B takes n=8, even). So B took an even. Then A=1 (odd), so A holds an odd → A can't hold all evens. And B holds 8 (even) → A can't hold all evens (8 missing). So draw broken both ways.

Hmm wait, for even n, A=1 (odd first move). For draw, A=odds (needs 1,3,5,7) or A=evens (needs 2,4,6,8). A has 1 (odd). If A=odds: A needs {1,3,5,7}, B={2,4,6,8}. B took 8 (even) — consistent with B=evens, but B needs ALL evens {2,4,6,8}. If A=evens: A needs {2,4,6,8}, but A has 1 (odd) → impossible. So A must be =odds for draw. A needs {1,3,5,7}, B needs {2,4,6,8}. B took 8. For draw, B needs all evens. B's strategy: prevent B from completing evens? No—B wants to break the draw. B took 8 (even). For draw, B needs {2,4,6,8}. B has 8. B will take more evens? No, B wants to NOT complete the draw. 

Hmm, this parity analysis says: for even n with A=1, A must collect {1,3,5,7} (odds) for a draw, B must collect {2,4,6,8} (evens). B took 8. If B then takes only evens, B completes {2,4,6,8} → draw (if A completes {1,3,5,7}). So B must take a NON-even at some point to break the draw. B's move 2 = 5 (odd!). So B takes 5 (odd), breaking B's ability to complete evens. Now draw impossible. Then B traps A.

So for even n: B's strategy is (1) take an endpoint, (2) take a number of the "wrong" parity (the parity A would need) to break the draw, (3) trap A.

This is the parity-breaking insight! Let me formalize:

For even n, A's first move a has parity p. For a draw:
- If a is odd: A must hold all odds (since A can't hold all evens — A has an odd). B must hold all evens.
- If a is even: A must hold all evens. B must hold all odds.

B's strategy: B takes an endpoint (1 or n). Then B takes a number of A's parity p (to break A's collection). Then B traps A.

Wait, B takes a number of A's parity → A can't complete its parity class → no draw. Then trap.

For n=8, A=1 (odd, p=odd): B takes 8 (even, endpoint). Then B takes 5 (odd = A's parity p). This breaks A's odds collection (A needs {1,3,5,7}, B took 5). No draw. Then trap.

For n=8, A=2 (even, p=even): B takes 1 (odd, endpoint). Then B takes... A's parity = even. B takes an even to break A's evens. B's move 2 = 3 (odd)?! Trace: A=2, B=1, A=4, B=3. B=3 is odd, not even. Hmm. So B took 3 (odd), not an even. But A's parity is even. So B took opposite parity. 

Wait, that contradicts my theory. Let me reconsider. A=2 (even). For draw, A=evens={2,4,6,8}, B=odds={1,3,5,7}. B took 1 (odd, consistent with B=odds). B's move 2 = 3 (odd, consistent with B=odds). So B is collecting ODDS, which is B's parity for the draw. So B is NOT breaking the draw by parity... 

But the game ends with A stuck, not a draw. Let me see: n=8, A=2, B=1, A=4, B=3, A=6, B=8. Wait trace: A=2,B=1,A=4,B=3,A=6,B=8,STUCK. A={2,4,6}, B={1,3,8}, remaining {5,7}. 5 blocked by A's 4,6. 7 blocked by A's 6. A stuck. 

So B took 8 (even!) on move 3. B's set = {1,3,8} = {1,3,8}: 1,3 odd, 8 even. So B took an even (8), breaking B's odds collection. For draw, B needs {1,3,5,7} (all odds), but B took 8 (even) → B can't complete odds → no draw. And A={2,4,6}, A needs {2,4,6,8} for draw, but B took 8 → A can't complete evens either. So both can't complete → no draw. A stuck.

So B's parity-breaking move is taking 8 (move 3), not move 2. The timing varies.

OK the parity-breaking is real but the timing/mechanism is adaptive. This is genuinely a complex strategy.

Given the extensive complexity, let me reconsider my approach to writing the proof. I think the honest path is:

1. State and prove the Parity Lemma (draw ⟺ parity partition). This is clean and is the key structural insight.
2. Verify small cases n=1..6 directly (draw for 1,2,4,6; B wins for 3,5). These can be done by explicit strategy.
3. For n ≥ 7, give B's winning strategy. For odd n, give the clean H2 strategy and prove it. For even n, give a strategy and prove it (or reduce to odd).

For even n, let me try harder to find a clean reduction to odd n.

**Reduction even → odd**: For even n ≥ 8, B's strategy: B takes 1 (if A≠1) or n (if A=1) — an endpoint. Then B takes the OTHER endpoint on move 2 IF possible, reducing to an odd sub-game. But we saw A might take the other endpoint. 

Alternatively: B takes an endpoint, then plays the odd strategy on the remaining n-1 board, with B's endpoint serving as the odd-strategy's first move. Let me reconsider this carefully.

Even n. A's first move a. B takes endpoint e (1 or n). Remaining board = {1..n}\{e}, which has n-1 numbers (odd). But it's not contiguous if a is interior. Hmm, but actually the "board" is the available numbers, and the odd strategy works on a path. If a is interior, the available numbers form two intervals. The odd strategy might not directly apply.

Wait, but in the odd strategy, A's moves can be anywhere; B just plays x±1. The strategy doesn't require contiguity. Let me reconsider.

Odd strategy H2 on board {1,...,m} (m odd): B takes endpoint (n if a ≤ center else 1), then plays x∓1. The key properties: B's moves always legal, A gets stuck with 1 remaining.

For even n, after B takes endpoint e, the remaining available is {1..n}\{e, a} (n-2 numbers, even). That's even, not odd. So the odd strategy (which needs odd length for 1 remaining) doesn't directly apply.

Hmm. Let me think about even n differently. 

Actually, let me reconsider: maybe for even n, B takes an endpoint, then the game on the remaining n-1 numbers (with A having 1 piece and B having 1 piece at the endpoint) is equivalent to an odd game where B is "ahead." 

Let me think about it as: after B takes endpoint 1 (and A has a), the remaining numbers {2,...,n}\{a}. B has piece at 1 (which blocks 2 for B). Now it's A's turn. This is like a new game on {2,...,n} where A has a pre-placed piece at a, B has a pre-placed piece at 1 (outside, but blocking 2), and A moves first in this sub-game. 

The sub-board {2,...,n} has n-1 numbers (odd). If it were a fresh odd game on {2,...,n}, B (moving second) would win (by odd strategy). But here A has a pre-placed piece and B has a pre-placed piece (at 1, outside). And it's A's turn (A is "moving first" in the sub-game, but A already has a piece). 

In a fresh odd game on {2,...,n}, A moves first (places first piece), B responds. Here, A already has piece at a, and it's A's turn to place a SECOND piece. So A is "ahead" by one move. That changes things — A has 2 pieces before B's 2nd... 

Hmm, this doesn't cleanly reduce.

Let me try yet another approach for even n: induction from odd n.

**Claim**: B wins for even n ≥ 8 by reducing to odd n-1.

Strategy: B's first move takes 1 (if A≠1) or n (if A=1). Now the board {2,...,n} (or {1,...,n-1}) has n-1 (odd) numbers, with A having 1 piece (a) in it and B having 0 pieces in it (B's piece is at the endpoint outside). It's A's turn.

Now B pretends this is a fresh odd game on {2,...,n} where "A" has just played a as the FIRST move. B applies the odd strategy: B's response = opposite endpoint of {2,...,n}. If a ≤ center of {2,...,n} = (n+2)/2, B takes n; else B takes 2. But B can't take 2 (blocked by B's piece at 1)! So if a > (n+2)/2, B can't take 2. 

So this works only if a ≤ (n+2)/2, i.e., a ≤ n/2 + 1. For a in the lower part, B takes n (fine), then plays x-1 (odd strategy). For a in upper part, by symmetry B should take n first (not 1), sub-board {1,...,n-1}, B takes 1 (fine), plays x+1.

So:
- If a ≤ n/2 + 1: B takes 1 (move 1), then n (move 2, = odd-strategy first response in {2,...,n}), then x-1 (push right).
  Wait, but B taking 1 then n is "both endpoints." We tested E4 (both endpoints then push) and it only drew. But E4 took 1 then n ALWAYS (move 2 = other endpoint). The issue was A might take n on move 2. Let me reconsider: here B takes n on move 2 only if a ≤ n/2+1. A's move 2 (a2) — could A take n? A's first a ≤ n/2+1. A's second move a2: A could take n if n available and legal. If A takes n, B can't take n. Then B falls back. 

Hmm, but actually if A takes n on move 2, that's GOOD for B maybe (A took an endpoint, limiting A's own options). Let me just test this refined strategy.

Actually, the difference from E4: E4 pushed in a fixed direction. Here the push direction depends on which side A is. And the "take other endpoint" is the odd-strategy's first response, which is conditional. Let me also handle the case a > n/2+1 (B takes n first, then 1, push left).

Let me also reconsider: maybe the issue with E4 was the push direction. Let me test the strategy that exactly mimics the odd strategy on the sub-board.

Let me define strategy E6 (even n, reduce to odd):
- B move 1: take 1 if a ≠ 1 else n. (endpoint; if a=1 take n, if a=n take 1, if a interior take 1.)
  Actually, to make the sub-board work: if a ≤ n/2+1, B takes 1 (sub-board {2,...,n}, a in lower part, B will take n). If a > n/2+1, B takes n (sub-board {1,...,n-1}, a in upper part, B will take 1).
  But if a=1: a ≤ n/2+1, B takes 1? But 1 taken by A. So B takes n. Then sub-board {1,...,n-1}, a=1 in lower part. B's odd-response = opposite endpoint of {1,...,n-1} = n-1 (if a=1 ≤ center n/2). B takes n-1. Hmm, but B already took n (move 1). B's piece at n blocks n-1 for B! So B can't take n-1. Problem.

Ugh, the endpoint blocking issue again.

Let me reconsider. The fundamental issue: B's first move (endpoint) blocks the adjacent number for B, which is often the sub-board's endpoint.

Let me try: B's first move takes the endpoint FAR from a. If a ≤ n/2, B takes n. Sub-board {1,...,n-1}, a in lower part. B's odd-response = n-1 (opposite endpoint of {1,...,n-1}). B's piece at n blocks n-1. Can't. 

If a ≤ n/2, B takes n. Sub-board {1,...,n-1}. B's odd-response should be the endpoint of {1,...,n-1} opposite to a. a ≤ n/2 ≤ center of {1,...,n-1} = n/2. So a ≤ center, B takes n-1 (far endpoint of sub-board). Blocked. 

Alternatively, B takes the NEAR endpoint. If a ≤ n/2, B takes 1. Sub-board {2,...,n}. a in lower part (a ≤ n/2 ≤ (n+2)/2). B's odd-response = n (far endpoint of {2,...,n}). B's piece at 1 blocks 2, not n. So B takes n. Fine! Then push x-1 (B_sub_first = n → push right, play x-1).

So: B takes NEAR endpoint (1 if a ≤ n/2, n if a > n/2). Then B takes FAR endpoint of sub-board. Then push.

If a ≤ n/2: B takes 1, then n, then x-1.
If a > n/2: B takes n, then 1, then x+1.

This is exactly E4/E5 but with the condition based on a's position! E4 always took 1 then n then push right. Let me test E6: take near endpoint, then far endpoint, then push away from near (toward far).

Wait, "push away from near" = push toward far. If B took 1 (near) then n (far), push A toward n (far) = play x-1? No. In odd strategy, B_first=n (far), play x-1, A pushed right toward n. So push toward far = play x-1 (take left of A, A moves right toward far endpoint n). Yes.

So E6: 
- a ≤ n/2: B takes 1, then n, then x-1 (fallback x+1).
- a > n/2: B takes n, then 1, then x+1 (fallback x-1).

But this is symmetric to E4/E5 essentially (E4 was take 1 then n then x-1, regardless of a). The difference: E6 takes near endpoint based on a. For a > n/2, E6 takes n first then 1 then x+1 (push left). E4 took 1 first then n then x-1 (push right). 

Let me test E6.
Still draws. The "take both endpoints then push" approach fundamentally only draws for even n. The even-n winning strategy requires the more subtle "take a central number to break parity" move.

Let me reconsider. The minimax for n=8, A=1: B=8, A=3, B=5. B takes 8 (endpoint), then 5 (central, NOT endpoint). So B does NOT take both endpoints. B takes one endpoint and one central.

Let me reconsider the parity-breaking insight more carefully and try to build a strategy around it.

For even n, A's first move a with parity p. For a draw, A must collect all of parity p (the parity of a), and B all of parity 1-p. 

B's goal: (1) break the draw by taking a number of parity p (so A can't complete parity p), AND (2) trap A.

B's first move: take an endpoint of parity 1-p (B's parity for the draw). This is consistent with B collecting parity 1-p. So B's first move doesn't break the draw; it's "cooperating" with the draw parity. Then B's SECOND move breaks the draw by taking a number of parity p.

For n=8, A=1 (p=odd): B's parity for draw = even. B takes 8 (even, endpoint) — cooperating. Then B takes 5 (odd = p) — breaking! Then trap.

For n=8, A=2 (p=even): B's parity for draw = odd. B takes 1 (odd, endpoint) — cooperating. Then B takes 3 (odd) — still cooperating?! Trace: A=2,B=1,A=4,B=3. B=3 is odd (cooperating). Then A=6, B=8 (even = p!) — breaking on move 3. 

So the parity-breaking move timing varies. For A=1, B breaks on move 2 (takes 5, odd). For A=2, B breaks on move 3 (takes 8, even). 

Hmm. So the breaking move isn't always move 2. Let me reconsider.

For A=2 (n=8): A={2,4,6}, B={1,3,8}, remaining {5,7}. B took 8 (even) on move 3, breaking A's evens (A needs {2,4,6,8}, B took 8). And B took 1,3 (odds). For draw, B needs {1,3,5,7} (odds). B has {1,3}, missing 5,7. But 5,7 are remaining and blocked by A. So B can't complete odds either. No draw. A stuck.

So in this case, B cooperated with the draw parity (odds) for moves 1-2, then broke on move 3 by taking 8 (even). The trap: remaining {5,7} both blocked by A.

Let me reconsider the pattern. It seems B mostly "mirrors" A's parity (takes opposite parity, cooperating with draw) but at a key moment takes A's parity to break, and the structure leaves A blocked.

This is really the reflection strategy (which gives draw) with a KEY deviation. The reflection strategy: B takes n+1-x (opposite parity, since n even → n+1 odd → n+1-x has opposite parity to x). Reflection gives draw. B deviates at one point to take same-parity, breaking the draw, and the deviation is chosen to trap A.

For n=8, A=1: reflection of 1 is 8. B takes 8 (reflection). A=3, reflection is 6. But B takes 5 (NOT reflection 6). This is the deviation. B takes 5 instead of 6. 5 is adjacent to 6 (the reflection). So B takes the number NEXT TO the reflection.

Hmm, 5 = 6 - 1 = reflection(3) - 1. Or 5 = 3 + 2. 

For n=8, A=2: reflection of 2 is 7. But B takes 1 (not reflection). Hmm, B takes 1, not 7. So not reflection-based.

Wait, n=8, A=2, B=1. 1 is not reflection of 2 (=7). So B's first move isn't reflection here. 

I'm not finding the pattern. Let me just try to find a working strategy by more extensive search, testing strategies that include a "central break" move.

Actually, let me step back and think about the time I'm spending. This is a very hard problem. Let me reconsider whether I should just present the answer with the parity lemma and a strategy that I verify computationally for a range, giving the strategy as an explicit (if complex) procedure, and proving the key lemmas.

Actually, let me reconsider the even n case via a cleaner reduction: **even n ≥ 8 → odd n-1 game with a pre-placed piece.**

Here's a cleaner idea. For even n, B's first move takes 1 (or n). Now REMOVE the number 1 and n from consideration... no.

Let me think about the "extra number" idea. Even n = odd (n-1) + 1 extra. The odd game on n-1 numbers is a B win. The extra number... 

Concretely: even n. B's strategy: take 1 (endpoint). Now consider the sub-game on {2, 3, ..., n} (n-1 numbers, odd). In this sub-game, A has a piece at a (if a ∈ {2,...,n}), B has no piece in the sub-game (B's piece at 1 is outside). It's A's turn. 

Now, IF this sub-game on {2,...,n} were a fresh odd game (A to move first, no pre-placed pieces), B would win. But here A has a pre-placed piece at a, and it's A's turn (A places 2nd piece). So A is one move ahead. 

In the odd game, the first player (A) makes (m-1)/2 moves and gets stuck. Here A has 1 pre-placed + will make more moves. Total A moves in sub-game = 1 (pre) + k. B moves = k. For A to get stuck in sub-game: ... 

Hmm, the pre-placed piece changes the count. Let me think. Sub-game {2,...,n}, m=n-1 odd. Fresh: A makes (m-1)/2 = (n-2)/2 moves, B makes (n-2)/2, 1 remaining, A stuck. With A pre-placed (1 piece already): A will make (n-2)/2 - 1 more moves? Total A pieces = 1 + (n-2)/2 - 1 = (n-2)/2. B pieces = (n-2)/2 - 1? Hmm, the counts shift.

This is getting too complicated. Let me just try a computational search for a clean even-n strategy by testing strategies with a "break" move.

Let me test: B takes 1 if avail else n (move 1). Move 2: B takes the reflection n+1-(A's 2nd move) if legal, ELSE takes (A's 2nd move)-1 or +1. Move 3+: reflection. I.e., mostly reflection but with a deviation. Hmm, but reflection gives draw.

Actually, let me reconsider. The minimax DEVIATES from reflection to win. The deviation is the key. Let me look at where minimax deviates from reflection for even n.

n=8, A=1: reflection would be B: 8, 6, 4, 2 (reflecting 1,3,5,7). Minimax B: 8, 5, 2. So minimax deviates at move 2 (5 vs 6) and move 3 (2 vs 4). 
n=8, A=2: reflection of 2,4,6,8 is 7,5,3,1. Minimax B: 1, 3, 8. Reflecting A={2,4,6}: B should be {7,5,3}. Minimax B={1,3,8}. Completely different. So minimax doesn't use reflection for A=2.

Hmm. So reflection is only used for A=1 (and A=n by symmetry). For other A, minimax uses a different strategy.

Let me look at n=8, A=2 more carefully. A=2, B=1. A=4, B=3. A=6, B=8. So B: 1, 3, 8. A: 2, 4, 6. B plays 1 (=2-1), 3 (=4-1), 8 (=6+2?). Hmm, 8 = 6+2. Or 8 = reflection of 2 in {1..8} = 7? No. 

Actually B: 1, 3, 8. 1=2-1, 3=4-1, 8=6+2. The first two are x-1. The third is x+2 (6+2=8). Why? Because x-1=5, but is 5 legal? After A={2,4,6}, B={1,3}, avail{5,7,8}. B's turn. B={1,3}, f{2,4}. B can pick from avail{5,7,8} minus f{2,4} = {5,7,8}. B picks 8. Why not 5 or 7? 
  B=5: B={1,3,5},f{2,4,6}. avail{7,8}. A={2,4,6},f{1,3,5,7}. A picks 8 (7 in f). A={2,4,6,8}. All chosen → draw! So B=5 → draw. 
  B=7: B={1,3,7},f{2,4,6,8}. avail{5,8}. A={2,4,6},f{1,3,5,7}. A picks 8 (5 in f). A={2,4,6,8}. draw. 
  B=8: B={1,3,8},f{2,4,7}. avail{5,7}. A={2,4,6},f{1,3,5,7}. A can't pick 5 or 7 (both in f). A stuck! B wins. 
So B picks 8 to win (not 5 or 7 which draw). So B's move 3 = 8 (the endpoint) to trap A. 

So the strategy for A=2 (n=8): B plays x-1 (1, 3) for moves 1-2, then on move 3 plays the FAR endpoint 8 to trap A. 

Interesting. So B pushes A right with x-1, and when A reaches the right side, B takes the far endpoint to block, trapping A.

Let me reconsider: A=2, B plays x-1: A=2→B=1, A=4→B=3, A=6→B=5? But B played 8 not 5 on move 3. Because B=5 leads to draw (A takes 8, all chosen). So B deviates to 8 (endpoint) to prevent A from completing.

So the strategy: B plays x-1 (push A right), but when A is about to complete the parity partition (A would take the last even 8), B takes 8 first to block, leaving A stuck.

This is the parity-breaking at the right moment! B cooperates (takes odds, opposite parity) until A is about to complete evens, then B takes the last even (8) to break the draw, and A is stuck because the remaining odds (5,7) are blocked by A's evens (4,6).

So the strategy for even n: B plays the "reflection/push" strategy (cooperating with draw parity) but at the critical moment, B takes the number A needs (an endpoint of A's parity), breaking the draw and trapping A.

This is a clean conceptual strategy! Let me formalize:

**Even n strategy for B**: 
- B takes 1 if A's first move a ≠ 1, else n. (B takes an endpoint.)
- B then plays "adjacent to A on the side toward B's endpoint" (push A away from B's endpoint), which means B takes numbers of opposite parity to A (cooperating with the draw partition).
- At the critical moment (when A is about to take the last number of A's parity class), B takes that number instead, breaking the draw and trapping A.

But "the critical moment" is hard to formalize cleanly. Let me think about it as: B pushes A toward the far endpoint. A collects numbers of parity p (A's parity) as A moves. The far endpoint has parity... For even n, endpoints 1 (odd) and n (even). If B took 1 (odd), the far endpoint n is even. A is pushed toward n. A collects parity p numbers. If p = even, A is collecting evens including n. B blocks A from taking n by taking n at the end. If p = odd, A collects odds, pushed toward n (even) — A can't take n (wrong parity, but also A might take it if legal). Hmm.

This is getting complicated. Let me just test a specific clean strategy: B takes 1 (if a≠1) else n. Then B plays x-1 (if B took 1, push A right) — wait, B took 1 (left endpoint), push A right means B plays... to push A right, B takes the left side of A (x-1), forcing A right. But B has 1, so x-1=1 is blocked for B. So B plays x-1 only when x-1 ≠ 1. 

Hmm. Let me reconsider. For A=2 (n=8), B=1, then B plays x-1: A=4→B=3, A=6→B=5. But B played 8 on move 3, not 5. So B plays x-1 EXCEPT when x-1 would lead to a draw, then B takes the endpoint.

Let me define: B takes 1 (or n if a=1). Then B plays x-1 (push right) as long as it's "safe" (doesn't lead to draw); when taking x-1 would let A complete the partition, B takes n (the far endpoint) instead.

This is still hard to formalize as a simple rule. Let me just test "B takes 1 (or n), then x-1 (or x+1 if B took n), but if the far endpoint is available and taking x-1 would leave A able to complete, take far endpoint." Too vague.

Let me try a different clean strategy: B takes 1 (or n). Then B plays x-1 (push right) ALWAYS, with fallback. EXCEPT B never plays the move that would be "reflection-completing." Hmm.

Actually, let me just test: B takes 1 if a≠1 else n. Then B plays x-1 (fallback x+1, then any). This is E1 which drew. The problem is E1 plays x-1 always, including the move where it should take the endpoint. Let me modify: B plays x-1, BUT if x-1 is the "second-to-last" and taking it leads to draw, take the far endpoint instead. 

I think the cleanest testable strategy is: B takes 1 (or n if a=1), then plays x-1 (push right, fallback x+1), BUT prefers the far endpoint n when available and x ≥ n-2 (A near the far end). Let me just test a strategy where B takes the far endpoint when A is near the far end.

Let me test: B takes 1 if a≠1 else n (move1). Move 2+: if (far endpoint n is available and legal) and (A's last move x ≥ n-2 or taking x-1 leads to draw), take n; else take x-1 (fallback x+1).

This is getting too ad hoc. Let me take a completely different approach: just compute the full minimax strategy table for even n and present it, OR find the strategy by testing "B plays optimally among {x-1, x+1, near endpoint, far endpoint}."

Actually, let me reconsider. Let me test the strategy: B takes 1 if a≠1 else n. Then B plays x-1 if legal, ELSE if x-1 illegal, B takes the far endpoint if legal else x+1. I.e., when x-1 is illegal (x=1 or x-1 taken), B takes the far endpoint. Let me test.

Hmm, but x-1 illegal happens when x=1 (A picks 1, but if B took 1, A can't) or x-1 taken. 

Let me just test several "take far endpoint at the right time" strategies. Let me test: B takes 1 (or n). Then B plays x-1 (push right). When A's move x is such that x+1 = n (i.e., x = n-1), B takes n (far endpoint) instead of x-1. Because A at n-1 is about to take n. Wait, A at n-1 can't take n (n-1 adjacent to n, A's constraint). So A at n-1 doesn't threaten n. Hmm.

Let me reconsider the n=8, A=2 case. A={2,4,6}, B about to move. A's last move x=6. x-1=5. B takes 8 (far endpoint) instead of 5. Why? Because taking 5 would let A take 8 (draw). Taking 8 blocks A. 

When does taking x-1 lead to a draw? When after B takes x-1, A can take the far endpoint and complete the partition. 

Let me think: B takes x-1, then A's turn. A takes the far endpoint n if n available and legal (n not adjacent to A's set). A's set has x (=6), so n=8: 8 adjacent to 6? No (diff 2). So 8 legal for A. A takes 8, completing A's parity class (evens {2,4,6,8}) → but is it a draw? Only if B also completes. B has {1,3,5} (odds, missing 7). 7 remaining, B's turn, B takes 7 (if legal). B={1,3,5,7}, all chosen → draw. So yes, B taking 5 leads to draw (A takes 8, B takes 7, draw). 

So B should take 8 (preventing A from completing evens). Then A stuck (5,7 blocked).

So the rule: B takes x-1 normally, but if taking x-1 allows A to take the far endpoint and complete the partition (leading to draw), B takes the far endpoint instead.

Formally: B takes x-1, UNLESS the far endpoint (n) is available and A can legally take n on the next move (i.e., n not adjacent to A's current set), in which case B takes n.

Wait, but B also needs n to be legal for B. n adjacent to B's set? B has {1, x_j-1's}. n adjacent to x_j-1 iff x_j-1 = n-1, i.e., x_j = n. A can't pick n (if B is about to take it, n available, A hasn't taken it). So x_j ≠ n, so n not adjacent to B's set (except via 1, but 1 far). So n legal for B. Good.

So the rule: B takes x-1, unless (n available AND n not adjacent to A's set), then B takes n.

"n not adjacent to A's set" = A has no n-1. 

Let me test this strategy for even n. But this is for the case B took 1 (push right). For B took n (a=1), symmetric: B takes x+1, unless (1 available AND 1 not adjacent to A's set), then B takes 1.

Let me formalize and test.

Strategy E7:
- Move 1: B takes 1 if a ≠ 1, else n.
- If B took 1 (push right): B takes x-1 if legal, UNLESS (n available and A has no n-1) then B takes n (if legal). Fallback: x+1, then any.
  Wait, "n available and A has no n-1" → B takes n. But also need x-1 legal normally. Let me structure: 
  - If n is available and legal for B and (A has no n-1 in aset): take n.  [preempt A from completing]
  - Else: take x-1 if legal, else x+1 if legal, else any.
- If B took n (a=1, push left): symmetric with 1.
  - If 1 is available and legal for B and (A has no 2): take 1.
  - Else: take x+1 if legal, else x-1, else any.

Hmm, but "A has no n-1" — initially A might not have n-1, so B would take n immediately on move 2. That's the "take both endpoints" which drew. Let me reconsider.

The condition for B to take n (preempt) should be more specific: B takes n only when A is "about to" take n, i.e., when taking x-1 instead would lead to a draw. That's when A can complete its parity class by taking n. 

A can complete parity class by taking n only if A already has all other numbers of parity p (A's parity). For even n, A's parity p. If p = even (n even), A needs {2,4,...,n}. A taking n completes it iff A has {2,4,...,n-2}. If p = odd, A needs {1,3,...,n-1} (but B took 1, so A can't have 1, so A can't complete odds — n is even, not in odds). Wait, if p=odd, A's parity class is {1,3,...,n-1}, which doesn't include n. So A taking n doesn't complete A's parity. So the preempt matters only when p = parity of n = even (n even). I.e., A's first move a is even.

So for even n:
- If A's first move a is even (p=even): A's parity class = {2,4,...,n} (includes n). B must prevent A from taking n after collecting {2,4,...,n-2}. B preempts by taking n when A has collected all of {2,4,...,n-2}.
- If A's first move a is odd (p=odd): A's parity class = {1,3,...,n-1} (doesn't include n). B took 1 (odd), so A can't complete odds. Draw already broken! So B just needs to trap A. B pushes A and traps.

So for a odd (B took 1, draw already broken since A can't get all odds), B just needs to trap A. The push strategy should trap A. But E1 (push with x-1) only drew for a odd. Why? Because the push doesn't trap A; A avoids getting stuck.

Hmm. So even when draw is broken, trapping A requires the right strategy. Let me reconsider.

For n=8, a=1 (odd): B took 8 (n, since a=1). Draw: A needs odds {1,3,5,7}, B needs evens {2,4,6,8}. B took 8 (even, cooperating). A has 1 (odd). Draw still possible (A=odds, B=evens, B has 8 which is in evens). So draw NOT broken by B taking 8. Because 8 is B's parity (even). So B taking 8 cooperates. Then B takes 5 (odd) on move 2 — THIS breaks the draw (B took an odd, B can't complete evens; and A needs 5 for odds, A can't complete odds). So draw broken on move 2.

So for a=1 (odd), B's first move 8 (even, cooperating, draw still possible), then B's second move 5 (odd, breaking draw). 

For a=2 (even), B's first move 1 (odd, cooperating, draw still possible: A=evens, B=odds, B has 1 in odds ✓). Then B's move 2 = 3 (odd, cooperating). Move 3 = 8 (even, breaking draw). So B breaks on move 3.

So B cooperates for a while then breaks. The break timing: B breaks when A has collected enough that breaking traps A.

For a=1 (odd): A collects odds. B cooperates (takes evens) until A has {1,3} (after A's 2nd move), then B takes 5 (the next odd A would want), breaking. Then A is forced: A={1,3}, B={8,5}. A's f{2,4}. avail{2,4,6,7}. A takes 6 or 7. Either way A gets stuck (as computed).

For a=2 (even): A collects evens. B cooperates (takes odds) until A has {2,4,6}, then B takes 8 (the last even), breaking. A stuck.

So the break happens when A has collected all-but-one of its parity class, and B takes the last one. Specifically:
- a=1 (odd), A collects odds {1,3,5,7}: B breaks when A has {1,3} by taking 5? But A needs {1,3,5,7}, A has {1,3}, missing 5,7. B takes 5. A can still take 7. So A hasn't collected "all but one." Hmm. After B takes 5, A={1,3}, avail{2,4,6,7}. A takes 6 or 7. If A takes 7: A={1,3,7},f{2,4,6,8}. avail{2,4,6}. B={8,5},f{4,6,7}. B takes 2. avail{4,6}. A f{2,4,6,8}→4,6 blocked. stuck. If A takes 6: A={1,3,6},f{2,4,5,7}. avail{2,4,7}. B={8,5},f{4,6,7}. B takes 2. avail{4,7}. A stuck. So A stuck after 3 moves regardless. 

So B breaks at move 2 (taking 5) and A is trapped after move 3. The break is early.

For a=2 (even), B breaks at move 3 (taking 8), A trapped after move 3.

The break timing differs. This is hard to formalize as a simple rule.

OK, I've spent a very long time. Let me make a decision: I'll write a proof that:
1. Proves the Parity Lemma (clean, key insight).
2. Handles n=1..6 explicitly.
3. For n ≥ 7: 
   - Odd n: give the H2 strategy (B takes far endpoint, pushes with x∓1, fallback) and prove it works (I'll prove the key properties: B always has a legal move, A gets stuck with 1 remaining).
   - Even n: give a strategy based on "B cooperates with the draw parity via reflection/push, then breaks at the critical moment by taking the last number of A's parity." I'll formalize the break condition and prove it.

Actually, for even n, let me try to find a clean strategy by testing the "break at critical moment" idea precisely. Let me test:

Strategy E8 (even n, B took 1, a even so A's parity = even = parity of n):
- B cooperates: plays x-1 (opposite parity, push right). 
- B breaks: when A has collected all evens except n (i.e., A's set ⊇ {2,4,...,n-2}), B takes n instead of x-1.

But detecting "A has collected all evens except n" is complex. Let me simplify: B takes n when n is the only even number A hasn't taken and A's last move was n-2. Hmm.

Actually, let me reconsider. Let me just test: B takes 1 (or n if a=1). Then B plays x-1 (or x+1 if a=1), BUT if the far endpoint (n or 1) is available and A's last move x is adjacent to the far endpoint minus 1 (i.e., x = n-2 for far=n), B takes the far endpoint. Let me just test "B takes far endpoint when A's last move = n-2 (or 2 for far=1)."

Hmm, let me just test a strategy where B takes the far endpoint when x-1 would be the "completing" move. Let me think about when B should take n instead of x-1.

B takes n instead of x-1 when: taking x-1 leads to draw, but taking n leads to win. Taking x-1 leads to draw when A can then take n and complete. A can take n after B takes x-1 iff n available (yes) and n not adjacent to A's set (A has no n-1). So B takes n when (n available) and (A has no n-1) and (taking n is legal for B). But "A has no n-1" is true for most of the game (A hasn't reached n-1). So B would take n too early.

The real condition: B takes n when A is about to take n on the NEXT move if B doesn't. A takes n next if n available and legal for A and A has no better... but A plays optimally. Hmm.

Actually, the issue is: if B takes x-1 and then A takes n, does that lead to a draw or does B still win? If A taking n completes A's parity class AND B can still complete B's parity class, it's a draw. If A taking n doesn't complete (because B already broke), then A taking n is fine for B.

So B should take n (break) only when A taking n would complete A's parity class (i.e., A has all other members of parity p). For a even, p=even, A needs {2,4,...,n}. A taking n completes iff A has {2,4,...,n-2}. 

So B takes n when A's set ⊇ {2,4,...,n-2} (all evens except n). Equivalently, when A has taken every even number below n. 

Let me test this precise strategy.

Strategy E9 (even n):
- B move 1: take 1 if a ≠ 1, else n.
- Case B took 1 (a ≠ 1): 
  - If a is even (p=even): B plays x-1 (push right, cooperate). BUT if A's set contains all of {2,4,...,n-2} (all evens except n), B takes n (if legal) instead. Fallback x-1, x+1, any.
  - If a is odd (p=odd): A can't complete odds (B has 1). Draw broken. B plays x-1 (push right) to trap. But does x-1 trap? For a odd, let me check n=8, a=3 (odd): B took 1. Then... let me see minimax. n=8, A=3: B=1, A=5, B=4, A=7, B=6. A={3,5,7},B={1,4,6},remaining{2,8}. 2 blocked by A's 3. 8 blocked by A's 7. stuck. So B plays 1, 4, 6. B's moves: 1 (endpoint), 4 (=5-1), 6 (=7-1). So x-1 push right. A={3,5,7} (odds, but missing 1 taken by B). remaining {2,8} blocked. So for a odd, B pushes right with x-1 and A gets trapped (A collects odds 3,5,7, but 1 taken by B, so A is "short" and the evens 2,8 remain blocked by A's 3,7). 

So for a odd (B took 1), the push x-1 traps A (A collects odds except 1, evens remain blocked). Let me verify this is general. For a odd, B took 1 (odd). A collects odds {a, a+2, ...} moving right. A can't take 1 (B has it). A reaches n-1 (odd, since n even → n-1 odd). A's set = {a, ..., n-1} (odds from a to n-1). B pushed with x-1, taking evens. Remaining: the odds below a (i.e., {1,3,...,a-2} minus 1 taken by B = {3,5,...,a-2}) and evens above n-1 (none, n-1 is the top odd, n is even). Wait, remaining also includes n (even). Hmm.

Let me reconsider n=8, a=3: A={3,5,7}, B={1,4,6}, remaining {2,8}. 2 (even, below A's 3), 8 (even, above A's 7). Both blocked by A (2 adj 3, 8 adj 7). So remaining are evens, blocked by A's odds at the boundary. 

So for a odd, A collects odds {a, a+2, ..., n-1}, B collects {1} ∪ {evens that are x-1 for A's moves} = {1, a-1, a+1, ..., n-2}. Remaining = {2,4,...,a-2} ∪ {n} (evens below a and n). These are blocked by A's a (blocks a-1... no, a blocks a-1 and a+1, both odds... wait a is odd, a-1 and a+1 are even). A's a blocks a-1 (even) and a+1 (even, but a+1 taken by B). So a-1 blocked by A. And n blocked by A's n-1. And the evens below a: {2,4,...,a-2}, are they blocked? A's lowest is a. a blocks a-1. a-2 is not adjacent to a (diff 2). So a-2 NOT blocked by A. So a-2 is available and unblocked → A could take it. Problem!

Wait, n=8, a=3: remaining {2,8}. 2 = a-1 (blocked by A's 3). 8 = n (blocked by A's 7). So remaining are a-1 and n, both blocked. Not {2,4,...,a-2}. Let me recompute. n=8, a=3. A={3,5,7}. B={1,4,6}. Taken: {1,3,4,5,6,7}. Remaining: {2,8}. 2 = 3-1 = a-1. 8 = n. So remaining = {a-1, n}. a-1=2 blocked by A's 3. n=8 blocked by A's 7. Both blocked. 

So remaining is {a-1, n}, not all evens below a. Because B took the evens a-1? No, B took 4,6 (=5-1,7-1). B took a+1=4, a+3=6. B did NOT take a-1=2. So a-1=2 remains. And it's blocked by A's a=3. And n=8 remains, blocked by A's n-1=7. So remaining {2,8} = {a-1, n}, both blocked. 

So the count: n=8, A makes 3 moves, B makes 3 moves, 6 taken, 2 remaining. A's 3 moves = {3,5,7} (odds from a=3 to n-1=7, that's 3 odds). B's 3 moves = {1,4,6} (1 + 2 evens). Remaining = {2,8} (a-1 and n). 

So A collects (n-1-a)/2 + 1 odds from a to n-1. For a=3, n=8: (7-3)/2+1 = 3. Yes. B collects 1 + (n-1-a)/2 evens... B's evens = {a+1, a+3, ..., n-2} = {4,6}, that's (n-1-a)/2 = 2 evens. Plus 1. Total B = 3. Remaining = n - 6 = 2 = {a-1, n}. 

For this to work (A stuck), a-1 and n must be blocked. a-1 blocked by A's a. n blocked by A's n-1. Yes. And A must be forced to collect exactly {a, a+2, ..., n-1} (no deviations). Is A forced? A is pushed right by B's x-1. A's options at each step: A can take any available non-forbidden. A's f = neighbors of A's set. As A collects {a, a+2, ...}, A's f includes a-1, a+1, a+3, .... A can take a+2 (next odd, not in f) or jump. If A jumps right (takes a+4 instead of a+2), then a+2 remains available... 

Hmm, A might deviate. Let me check: does the push strategy force A to take consecutive odds? Let me test n=8, a=3, B pushes x-1. A=3, B=1. A's turn: A={3},f{2,4}. avail{2,4,5,6,7,8}. A can take 5,6,7,8 (not 2,4). A takes 5 (cooperate) or deviates (6,7,8). 
  A=6 (deviate): A={3,6},f{2,4,5,7}. avail{2,4,5,7,8}. B={1},f{2}. B plays x-1=5. B={1,5},f{2,4,6}. avail{2,4,7,8}. A={3,6},f{2,4,5,7}. A takes 8 (not in f). A={3,6,8},f{2,4,5,7,9}. avail{2,4,7}. B={1,5},f{2,4,6}. B plays x-1=7. B={1,5,7},f{2,4,6,8}. avail{2,4}. A f{2,4,5,7,9}→2,4 blocked. stuck! 
  A=7 (deviate): A={3,7},f{2,4,6,8}. avail{2,4,5,6,8}. B={1},f{2}. B plays x-1=6. B={1,6},f{2,5,7}. avail{2,4,5,8}. A={3,7},f{2,4,6,8}. A takes 5 (not in f). A={3,5,7},f{2,4,6,8}. avail{2,4,8}. B={1,6},f{2,5,7}. B plays x-1=4. B={1,6,4},f{2,3,5,7}. avail{2,8}. A f{2,4,6,8}→2,8 blocked. stuck!
  A=8 (deviate): A={3,8},f{2,4,7,9}. avail{2,4,5,6,7}. B={1},f{2}. B plays x-1=7. B={1,7},f{2,6,8}. avail{2,4,5,6}. A={3,8},f{2,4,7,9}. A takes 5 or 6. A=5: A={3,5,8},f{2,4,6,7,9}. avail{2,4,6}. B={1,7},f{2,6,8}. B plays x-1=4. B={1,7,4},f{2,3,5,6,8}. avail{2,6}. A f{2,4,6,7,9}→2,6 blocked. stuck. A=6: A={3,6,8},f{2,4,5,7,9}. avail{2,4,5}. B={1,7},f{2,6,8}. B plays x-1=5. B={1,7,5},f{2,4,6,8}. avail{2,4}. A f{2,4,5,7,9}→2,4 blocked. stuck.

So for a=3 (odd), B's push x-1 traps A regardless of A's deviations. So for a odd, the push strategy works (draw already broken by B taking 1, and push traps A). 

So the issue with E1 (which drew for a odd) must be something else. Let me reconsider why E1 drew for a=1 (odd). E1: B takes 1 if avail else n. For a=1, B takes n=8. Then push x-1. A=1, B=8. A=3, B=2 (x-1). A=5, B=4. A=7, B=6. All chosen → draw! 

So for a=1, B took 8 (n, even, cooperating), and pushed x-1, leading to draw (A={1,3,5,7}, B={8,2,4,6}, all chosen). So the push cooperates and completes the partition → draw. B needs to BREAK by taking an odd at some point.

So for a=1 (odd), B's first move 8 (even) cooperates. B must break by taking an odd. The minimax breaks at move 2 (takes 5, odd). 

So the difference between a=1 and a=3 (both odd): for a=3, B took 1 (odd) on move 1, which BREAKS the draw immediately (A can't get all odds). For a=1, B took 8 (even) on move 1 (cooperating, since 1 taken by A), so B must break later.

So the key: B's first move should take a number of A's parity (to break the draw immediately) when possible. For a=1, A's parity=odd, B should take an ODD. But B took 8 (even) because... 1 is taken (by A), and the "endpoint" rule says take n=8 (even). Instead, B should take an ODD endpoint or odd number.

But the only odd endpoint is 1 (taken) and... n=8 is even. So there's no odd endpoint available (1 taken). So B must take an interior odd to break. Minimax takes 5 (interior odd) on move 2. But move 1 is 8 (even). Why not take an odd on move 1?

n=8, a=1: B's move 1 options (odd numbers available): 3,5,7. Let me check if B taking an odd on move 1 wins. B=3: B={3},f{2,4}. A={1},f{2}. avail{2,4,5,6,7,8}. A takes 4,5,6,7,8 (not 2). ... Let me just test B's first move = 3,5,7 for a=1 via minimax.

Actually, the minimax said B's best first move for a=1 is 8 (not an odd). So taking an odd on move 1 is NOT better; 8 is optimal. So B takes 8 (even, cooperating) on move 1, then breaks on move 2. Why is 8 better than breaking immediately? 

Maybe because taking 8 (endpoint) gives B a structural advantage (controls the endpoint) that helps trap A later, and breaking on move 2 is sufficient.

So the strategy isn't "break immediately." It's "take endpoint, then break at the right moment."

OK. I think the even-n strategy is genuinely subtle and I can't easily find a clean closed form. Let me make a decision: I'll write the proof with:
1. Parity Lemma.
2. Small cases.
3. Odd n ≥ 7: H2 strategy with proof.
4. Even n ≥ 8: A strategy based on "B takes the endpoint of A's parity if available, else takes the other endpoint and breaks on move 2 by taking a central number of A's parity." And I'll prove it by reducing to the odd case or by direct analysis.

Actually, let me reconsider the even n case via reduction to odd n-1 more carefully, because I think there's a clean reduction I'm missing.

**Clean reduction for even n**: B's first move takes 1 (if a ≠ 1) or n (if a = 1). Wait, but for a=1, B takes n=8 (even), and we need to break. 

Hmm, let me reconsider. For even n, let me consider B's strategy: take 1 if a ≠ 1, else n. Then the remaining board (excluding B's endpoint) has n-1 numbers. Now apply the ODD strategy on this n-1 board, treating A's first move a as the first move of the odd game, and B's NEXT move as the odd-strategy's first response.

For a ≠ 1 (B took 1): sub-board {2,...,n} (n-1 odd). A's first move in sub-board = a (a ∈ {2,...,n}). Odd strategy: B takes opposite endpoint of {2,...,n}. If a ≤ center=(n+2)/2, B takes n; else B takes 2. But B can't take 2 (blocked by B's 1). So if a > (n+2)/2, B can't take 2 → problem.

For a > (n+2)/2 (a in upper part, a ≠ 1): B took 1, but odd strategy wants B to take 2 (blocked). So instead, B should take n first (not 1). I.e., B's first move depends on a's position:
- a ≤ (n+2)/2: B takes 1. Sub-board {2,...,n}. Odd strategy: B takes n (opposite endpoint). Then push x-1.
- a > (n+2)/2: B takes n. Sub-board {1,...,n-1}. Odd strategy: B takes 1 (opposite endpoint). Then push x+1.

But wait, for a=1: a ≤ (n+2)/2, B takes 1? But 1 taken by A. So B takes n. Then sub-board {1,...,n-1}, a=1 in lower part. Odd strategy: B takes n-1 (opposite endpoint of {1,...,n-1}). B's piece at n blocks n-1! Can't. Problem.

For a=1: B takes n. Sub-board {1,...,n-1}. a=1. Odd strategy on {1,...,n-1}: center = n/2. a=1 ≤ n/2. B takes opposite endpoint = n-1. Blocked by B's n. Can't.

So a=1 is problematic. By symmetry a=n is too. 

For a=1, the minimax takes 8 (n) then 5 (central odd). The "central" move 5 is the break. 5 = (n/2 + 1) for n=8? n/2+1 = 5. Yes! So B takes the central number n/2+1 on move 2. For n=8, that's 5. For n=10, A=1: B=10, A=3, B=2 (not central 6). Hmm, n=10 A=1 trace: B=10, A=3, B=2, A=5, B=7, A=8, B=4. B's moves: 10, 2, 7, 4. B took 10 (n), then 2 (x-1), then 7 (not x-1=4, not x+1=6). 7 = ? Then 4. 

So n=10, A=1: B doesn't take the central number on move 2. B takes 2 (x-1, cooperating). Then breaks at move 3 (takes 7, odd = A's parity). 7 = ? A={1,3,5}, B={10,2,7}. 7 is odd (A's parity), breaks. Then A=8, B=4. A={1,3,5,8},B={10,2,7,4},remaining{6,9}. 6 blocked by 5, 9 blocked by 8. stuck.

So for n=10, A=1, B breaks at move 3 (takes 7). For n=8, A=1, B breaks at move 2 (takes 5). The break timing depends on n.

I really can't find a clean pattern. Let me just go with a computational-verification-based proof for the even case, OR find the strategy by testing the "cooperate then break" with a precise break condition.

Let me test the strategy: B takes 1 if a≠1 else n. Then B plays x-1 (if B took 1) or x+1 (if B took n) [cooperate/push], BUT B takes the far endpoint (n or 1) when A is about to complete its parity class. Precisely, B takes the far endpoint when A's set contains all numbers of A's parity except the far endpoint.

For a=1 (odd, B took n=8): A's parity=odd={1,3,5,7}. Far endpoint from B's perspective... B took n=8, push x+1? No wait. Let me reconsider. For a=1, B took n. The minimax then plays x-1 (push right) — A=3,B=2. Wait, B took n=8 (right endpoint), and plays x-1 (take left of A). A moves right toward 8. So push right. But B's endpoint is 8 (right). A pushed toward 8. 

Hmm, for a=1, B took 8 (right), push right (x-1). A moves right: 1,3,5,7. A collects odds. B takes 2,4,6 (evens, cooperating). This leads to draw (A={1,3,5,7},B={8,2,4,6}). So B must break. B breaks by taking an odd instead of an even at some point. Minimax breaks at move 2 (takes 5 instead of... wait B's move 2 is 5, but x-1 of A=3 is 2. So B takes 5 instead of 2. 5 is odd (A's parity), 2 is even (B's parity). So B breaks by taking 5 (odd) instead of 2 (even).

So the break: instead of taking x-1 (cooperate), B takes a number of A's parity. Specifically, B takes x+2 (5 = 3+2) instead of x-1 (2). 

For n=10, A=1: B=10, A=3, B=2 (cooperate, x-1). A=5, B=7 (break! 7 = 5+2, odd). So B breaks at move 3, taking x+2=7 instead of x-1=4. 

For n=8, A=1: B=8, A=3, B=5 (break, 5=3+2). Break at move 2.
For n=10, A=1: break at move 3 (7=5+2).
For n=12, A=1: let me predict. B=12, A=3, B=2, A=5, B=4, A=7, B=9 (break, 9=7+2)? Let me check the trace.

Let me get the n=12, A=1 trace.
Now I see the pattern for even n, A=1.

n=8, A=1: B=8, A=3,B=5(break),A=6,B=2. Break at B's move 2 (5 = 3+2).
n=10, A=1: B=10, A=3,B=2, A=5,B=7(break), A=8,B=4. Break at B's move 3 (7 = 5+2).
n=12, A=1: B=12, A=3,B=2, A=5,B=4, A=7,B=9(break), A=10,B=6. Break at B's move 4 (9 = 7+2).
n=14, A=1: B=14, A=3,B=2, A=5,B=4, A=7,B=6, A=9,B=11(break), A=12,B=8. Break at B's move 5 (11 = 9+2).

So for A=1 (even n), B cooperates (x-1) for the first few moves, then breaks by taking x+2 (an odd, A's parity) at a specific move. The break move is x+2 where x is A's last move.

Break timing:
- n=8: break at B-move 2, A's last move x=3, break=5=3+2. A has {1,3}.
- n=10: break at B-move 3, A's last move x=5, break=7=5+2. A has {1,3,5}.
- n=12: break at B-move 4, A's last move x=7, break=9=7+2. A has {1,3,5,7}.
- n=14: break at B-move 5, A's last move x=9, break=11=9+2. A has {1,3,5,7,9}.

So B breaks when A has collected {1,3,...,n-5} (odds up to n-5), and A's last move is n-5... wait:
- n=8: A has {1,3}, last x=3. n-5=3. Yes, x=n-5=3.
- n=10: A has {1,3,5}, last x=5. n-5=5. Yes.
- n=12: A has {1,3,5,7}, last x=7. n-5=7. Yes.
- n=14: A has {1,3,5,7,9}, last x=9. n-5=9. Yes.

So B breaks when A's last move x = n-5, by taking x+2 = n-3. Then:
- n=8: break=5=n-3. Then A=6, B=2. A={1,3,6}, remaining{4,7}. 
- n=10: break=7=n-3. Then A=8, B=4. A={1,3,5,8}, remaining{6,9}.
- n=12: break=9=n-3. Then A=10, B=6. A={1,3,5,7,10}, remaining{8,11}.
- n=14: break=11=n-3. Then A=12, B=8. A={1,3,5,7,9,12}, remaining{10,13}.

After break, A takes n-2 (6,8,10,12 = n-2), B takes... 2,4,6,8 = ? 
- n=8: B takes 2 after A=6. 2 = 6-4? or just the leftover. 
- n=10: B takes 4 after A=8. 4 = 8-4.
- n=12: B takes 6 after A=10. 6 = 10-4.
- n=14: B takes 8 after A=12. 8 = 12-4.

So after break, A takes n-2, B takes n-6. Then remaining {n-4, n-1} (e.g., n=8: {4,7}; n=10: {6,9}; n=12: {8,11}; n=14: {10,13}). n-4 and n-1. n-4 blocked by A's n-5? n=8: 4 blocked by A's 3 (n-5=3). Yes. n-1 blocked by A's n-2. n=8: 7 blocked by 6. Yes. So remaining {n-4, n-1} blocked by A's {n-5, n-2}. 

So the strategy for A=1 (even n): B cooperates (x-1) while A collects odds 1,3,...,n-5. When A plays n-5, B breaks by taking n-3 (=x+2). Then A is forced to take n-2, B takes n-6, and A is stuck with {n-4, n-1} remaining, both blocked.

But why does A cooperate (take 1,3,5,...,n-5 in order)? A is pushed by B's x-1. After A=1, B=8. A=3 (A's f={2}, so A takes 3 or higher; A takes 3 as the "natural" push). But A could deviate. The minimax shows A still loses with deviations. But for the PROOF, I need to handle deviations.

This is the same issue as odd n. The push strategy with break handles deviations, but proving it requires care.

OK, I've spent an enormous amount of time. Let me now just WRITE the proof, using:
1. Parity Lemma (clean proof).
2. Small cases (n=1..6) by explicit analysis.
3. For n ≥ 7, I'll present B's strategies and prove them. For odd n, the H2 strategy (clean-ish). For even n, the "cooperate-then-break" strategy. I'll prove the key invariants.

Actually, given the complexity, let me reconsider whether I can give a UNIFIED strategy for all n ≥ 7 that I can prove. 

Let me reconsider the odd n H2 strategy and the even n strategy. They're different. Let me see if there's a unified view.

Unified view: B's strategy is to "push A in one direction, and at the right moment, take a number that blocks A's completion, trapping A."

For odd n: B takes far endpoint, pushes A toward it, A gets trapped against it (1 remaining).
For even n: B takes far endpoint, pushes A toward it, cooperates with parity, then breaks at the right moment (2 remaining).

Hmm. Let me reconsider if the odd strategy H2 actually has a clean proof. Let me re-examine.

Odd n H2: B_first = n if a ≤ c else 1. Then play x-1 (if B_first=n) or x+1 (if B_first=1), fallback to other side.

I showed the preferred move x∓1 is always legal EXCEPT when A picks the near endpoint (1 for B_first=n, or n for B_first=1). In that case, fallback to x±1 (other side).

Let me prove H2 works for odd n ≥ 7. Actually, let me reconsider whether the fallback is even needed, i.e., whether A picking the near endpoint can actually happen in a way that requires fallback, and handle it.

For B_first=n (a ≤ c): A might pick 1 (near endpoint) if 1 available (yes, B took n) and 1 not adjacent to A's set (A has no 2). A picks 1. Then B's x-1=0 invalid, fallback x+1=2. 2 available? 2 taken by B iff A previously picked 3 (B took 2). If A didn't pick 3 before, 2 is available, B takes 2. If A picked 3 before (B has 2), then 2 unavailable, fallback to "any legal."

When does A pick 3 before picking 1? A's first move a ≤ c, a ≠ 3 (else 3 is first). If a ∈ {1,2,4,5,...,c}. a=1: A can't pick 1 again. A picks 3 as 2nd move? A={1},f{2}. 3 available, legal. A=3. B takes 2. Then A picks 1? Can't (taken). So no issue. a=2: A={2},f{1,3}. A can't pick 3. So A never picks 3. a=4: A={4},f{3,5}. A can't pick 3. a=5 (c=5 for n=9): A={5},f{4,6}. A can pick 3 (available, legal). A=3 (2nd move). B takes 2. Then A picks 1? A={5,3},f{2,4,6}. 1 available, legal. A=1. B's x-1=0, fallback x+1=2, but 2 taken by B! So fallback to "any legal." 

So for a=5 (center), n=9, the strategy hits the "any legal" fallback. Let me check what B should play. A={5,3,1}, B={9,2}. avail{4,6,7,8}. B's f={1,3,8}. B can pick 4,6,7 (not 8). "Any legal" — minimax picks 4 (per trace: A=5,B=9,A=1,B=2,A=3,B=4). So B=4. Then A=7,B=6. stuck.

So the "any legal" fallback works but isn't clean. For the proof, I need to handle this case. 

This is getting really messy. Let me reconsider: maybe choose a DIFFERENT strategy for odd n that avoids the fallback entirely.

The fallback is needed because A can pick the near endpoint. What if B's first move takes the near endpoint instead of the far one? Then A can't pick it.

For a ≤ c: near endpoint = 1. If B takes 1 (near), A can't pick 1. Then push... but push direction? If B takes 1 (left), push A right (x+1? or x-1?). Let me reconsider. If B takes 1 and pushes A right (play x+1, taking right of A), A moves right toward n. A might pick n (far endpoint). Then x+1 = n+1 invalid. So same problem on the other side.

So no matter which endpoint B takes, A can pick the OTHER endpoint, causing the push to fail. The fallback handles it.

Alternatively, B takes BOTH endpoints (first two moves). Then A can't pick either endpoint. But for odd n, B taking both endpoints uses 2 moves, and the remaining n-2 (odd) numbers... Let me test "B takes both endpoints then push" for odd n.

Wait, I tested E4/E5 for even n (both endpoints then push) and it drew. Let me test for odd n.

Actually for odd n, let me test: B takes 1 (move1, if avail else n), then n (move2, if avail&legal), then push x-1 or x+1. Let me test this for odd n.

Hmm, but B taking both endpoints for odd n: remaining n-2 (odd) numbers {2,...,n-1}. A has 2 pieces (a, a2). B has {1,n}. Push A. A trapped with... n-2 numbers, A makes (n-2-1)/2 = (n-3)/2 more moves? Total A = 2 + (n-3)/2. Hmm.

Let me just test computationally: odd n, B takes both endpoints then push.
The "near-then-far-then-push" strategy (B takes near endpoint, then far endpoint, then push toward far) works for ALL odd n from 7 to 21, with NO fallback failures (fails=[]) and NO non-loss (all A_loses). 

And importantly, this strategy takes BOTH endpoints, so A can never pick an endpoint, avoiding the fallback issue! Let me verify the preferred push move is always legal (no fallback needed).

For odd n, ODD_both:
- move1: near endpoint (1 if a ≤ c else n).
- move2: far endpoint.
- move3+: push toward far (x-1 if far=n, else x+1).

After B takes both endpoints (1 and n), A is confined to {2,...,n-1}. B pushes A toward far. 

Push move: x-1 (if far=n) or x+1 (if far=1). 
- x-1 legal? x ∈ {2,...,n-1} (A confined, since endpoints taken). x-1 ∈ {1,...,n-2}. x-1 = 1? Only if x=2. But 1 is taken by B. So x-1=1 unavailable. So if A picks x=2, B's x-1=1 is taken. Fallback. Hmm.

Wait, but fails=[] means the strategy never failed (no STRAT_FAIL). So the fallback (other side / any legal) handled it. But I wanted NO fallback. Let me check if fallback was used.

Actually, fails=[] just means no STRAT_FAIL (strategy always had a legal move via fallback). The fallback might still be used. Let me check if the PREFERRED push move is always legal.

For far=n, push x-1. A confined to {2,...,n-1}. A picks x. x-1: if x=2, x-1=1 (taken by B). So preferred illegal when x=2. When does A pick 2? A can pick 2 if 2 available (yes, B took 1 and n, not 2) and 2 not adjacent to A's set (A has no 1 (taken by B, but that's B's; A's constraint is A's own set) and no 3). So A picks 2 if A has no 3. 

So A can pick 2, causing fallback. So the preferred move isn't always legal. But the strategy still wins (with fallback). 

Hmm. So even this strategy needs fallback. But maybe the fallback is cleaner here: when A picks 2 (near B's endpoint 1), B plays x+1=3 (other side). 3 available? 3 taken iff A or B has 3. B has {1,n}, no 3. A has 3? A has 2 (just picked), A's set independent, no 3. So 3 available. 3 legal for B? B has {1,n}, 3 adjacent to 1? No (diff 2). 3 adjacent to n? No. So B plays 3. Clean fallback.

So the fallback is "play x+1 when x-1 unavailable (x=2)", and x+1=3 is always available and legal. Similarly for far=1, push x+1, fallback x-1 when x=n-1 (x+1=n taken), play x-1=n-2 (available, legal).

So the fallback is clean and deterministic: when A picks the number adjacent to B's near endpoint (x=2 for near=1, or x=n-1 for near=n), B plays the other side (x+1=3 or x-1=n-2), which is always available and legal.

Wait, but what if A picks 2 AND 3 is somehow taken? 3 taken by B only if B previously played 3 (as a push move x-1=3, i.e., A previously picked 4). If A previously picked 4, B took 3. Then A picks 2: B's x-1=1 (taken), x+1=3 (taken by B). Both unavailable! Fallback to "any legal." 

When does A pick 4 then 2? A's first move a, then 4, then 2? Or a=4 (first), then 2. Let me think. This requires A to pick 4 (B takes 3) and then pick 2. A picks 2 if A has no 3 (A's set). A has 4, so A has no 3 (independent, 3,4 adjacent, so A can't have both). So A can pick 2 after picking 4. Then B's push for x=2: x-1=1 (taken), x+1=3 (taken by B). Both unavailable. Fallback "any legal."

So the fallback "any legal" CAN be needed. Hmm. But the test shows the strategy still wins. So "any legal" works but isn't clean to prove.

Let me check: does this scenario (A picks 4 then 2, both push sides unavailable) actually occur in optimal play? The test uses A optimal against the strategy, and the strategy won. So even if it occurs, "any legal" suffices. But for a clean proof, I'd want to avoid "any legal."

Let me reconsider. Maybe the push direction should be AWAY from the near endpoint, not toward the far. I.e., if near=1 (B took 1 first), push A RIGHT (toward far=n) by playing x-1 (take left of A). Wait, that's toward far. Hmm. Let me reconsider what "push toward far" means.

If B took near=1 and far=n, and pushes toward far=n (rightward), B plays x-1 (take left of A, A forced right). A moves right. A won't pick 2 (left, near B's 1) because... actually A could pick 2 early. 

Alternatively, push AWAY from far (toward near). If B plays x+1 (take right of A, A forced left toward near=1). A moves left. A picks decreasing. A won't pick n-1 (near far=n) unless... A could.

Hmm, symmetric issue.

Let me reconsider. The cleanest would be: B takes both endpoints, then A is confined to {2,...,n-1}. Now it's a sub-game on {2,...,n-1} (length n-2, which is ODD for odd n). In this sub-game, A has 2 pieces (a, a2) and B has 0 pieces (B's pieces are at endpoints outside). It's B's turn (move 3). 

Wait, this is like a fresh odd game on {2,...,n-1} where A has already placed 2 pieces and B 0, and it's B's turn. That's weird (B is "behind"). 

Actually, let me reconsider the move counting. Odd n. B takes near (move1), far (move2). A has made 2 moves (a, a2). B has made 2 moves. Now move 5 = A's 3rd move. Wait no: move1=A, move2=B(near), move3=A(a2), move4=B(far), move5=A(a3), move6=B(push), ... So after B takes far (move4), it's A's turn (move5). A has 2 pieces, B has 2 pieces (both endpoints). Sub-board {2,...,n-1} has n-2 numbers (odd). A has 2 pieces in it (a, a2, assuming both in {2,...,n-1}; a could be 1 or n if A picked endpoint, but B took endpoints so a ∈ {2,...,n-1}). 

Hmm, A has 2 pieces, B has 0 in sub-board. It's A's turn. This isn't a standard odd game.

Let me just abandon trying to get a no-fallback strategy and instead PROVE the strategy with the clean fallback (x+1 when x-1 unavailable due to endpoint, and handle the rare double-unavailable case separately).

Actually, let me reconsider the whole proof approach. I've spent way too long. Let me just write a proof that:
1. Parity Lemma.
2. Small cases.
3. For n ≥ 7, describe B's strategy and prove it via a careful invariant, handling the push and the break.

Let me reconsider and find the CLEANEST possible strategy to prove. 

For ODD n ≥ 7, the "near-then-far-then-push-toward-far" strategy works. Let me prove it. The push toward far: B plays x-1 (if far=n) or x+1 (if far=1). The issue is A picking the number adjacent to the near endpoint.

Actually, let me reconsider: push AWAY from far (toward near). If far=n, push left: B plays x+1 (take right of A, A forced left toward near=1). Then A moves left, toward 1 (taken by B). A gets trapped against 1. A won't pick n-1 (right, near far=n) because A is moving left. But A COULD pick n-1 early (before moving left). Hmm.

Let me just test "push away from far" (toward near) for odd n.

Actually, both directions had issues. Let me just go with "push toward far" and handle the fallback in the proof.

Hmm, let me reconsider. Actually, let me reconsider the push direction more carefully for the trap.

For odd n, near=1, far=n. A confined to {2,...,n-1}. 
- Push toward far (right): B plays x-1. A forced right toward n. A collects numbers moving right. Trap: A reaches n-2 (or n-1), B takes the adjacent, A stuck with 1 remaining near n.
- Push toward near (left): B plays x+1. A forced left toward 1. A collects moving left. Trap: A reaches 3 (or 2), B takes adjacent, A stuck with 1 remaining near 1.

For push toward far (right), A might pick 2 (left, near 1) early, causing x-1=1 unavailable. For push toward near (left), A might pick n-1 (right, near n) early, causing x+1=n unavailable. Symmetric.

The fallback handles both. Let me just prove the strategy with fallback, arguing that the fallback move (other side) is always available and legal EXCEPT in a rare case that I handle.

Actually, let me reconsider the rare case (A picks 4 then 2, both push sides taken). Let me check if this can actually happen under the strategy, and if so, what B does.

Let me just instrument the strategy to detect when "any legal" (third fallback) is used.        — AI历史解题过程（thinking）
#   omni_math_004190         — 题目ID

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
  <problem_id>omni_math_004190</problem_id>
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

Ingrid and Erik are playing a game. For a given odd prime $p$, the numbers $1, 2, 3, ..., p-1$ are written on a blackboard. The players take turns making moves with Ingrid starting. A move consists of one of the players crossing out a number on the board that has not yet been crossed out. If the product of all currently crossed out numbers is $1 \pmod p$ after the move, the player whose move it was receives one point, otherwise, zero points are awarded. The game ends after all numbers have been crossed out.

The player who has received the most points by the end of the game wins. If both players have the same score, the game ends in a draw. For each $p$, determine which player (if any) has a winning strategy

## Standard Solution


To analyze this problem, we need to determine the strategy and scores for each player based on the prime number \( p \).

### Step 1: Game Description and Point Calculation

In the game, if Ingrid or Erik crosses out a number and the product of all crossed-out numbers modulo \( p \) is \( 1 \pmod{p} \), that player earns a point.

### Step 2: Understanding the Structure for Small Values of \( p \)

Let's consider small values of \( p \) to see how the scores may develop:

#### Case: \( p = 3 \)

- Numbers: \( 1, 2 \).
- Ingrid starts and can immediately cross out \( 1 \), making the product \( 1 \equiv 1 \pmod{3} \). She scores 1 point.
- The game then requires crossing out \( 2 \). Regardless of who plays next, no point can be scored.
- Ingrid wins because she has 1 point and Erik has 0.

#### Case: \( p = 5 \)

- Numbers: \( 1, 2, 3, 4 \).
- Ingrid starts and crosses out \( 1 \). Product is \( 1 \equiv 1 \pmod{5} \), scoring 1 point.
- The numbers \( 2, 3, 4 \) remain. No further single move results in a product of 1 modulo 5 without coordination from both players.
- Ingrid wins by initial advantage and strategic plays.

#### Case: \( p = 7 \)

- Consider the numbers \( 1, 2, 3, 4, 5, 6 \).
- Ingrid can start by crossing out \( 1 \) for a point.
- No immediate pair combination among \( 2, 3, 4, 5, 6 \) allows creating a product modulo 7 equal to 1 without back-and-forth strategy.
- Ultimately, both players may end up having the same number of points if they play optimally, leading to a draw.

### Step 3: General Strategy Analysis for \( p > 7 \)

- As \( p \) increases, the more possibilities emerge for creating products equalling 1 modulo \( p \) later in the game.
- Erik can strategize to create modulo 1 situations more frequently due to more available numbers after initial movements, likely outscoring Ingrid for \( p > 7 \).

### Conclusion

- For \( p = 3 \) and \( p = 5 \), Ingrid has a clear winning strategy.
- For \( p = 7 \), optimal play for both leads to a draw.
- For \( p > 7 \), Erik can implement strategies to ensure more scores than Ingrid, thereby winning.

Thus, we conclude:
\[ \boxed{\text{Ingrid for } p = 3 \text{ and } p = 5, \text{ Draw for } p = 7, \text{ Erik for } p > 7.} \]
```

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a game where two players A and B take turns choosing positive integers $k \le n$. Rules:
(i) Can't choose a number already chosen by either player.
(ii) Can't choose a number consecutive to any number the player has already chosen (on their own previous turns).
(iii) Draw if all numbers chosen; otherwise the player who can't move loses.

A goes first. Determine the outcome with optimal play.

Let me think about this carefully.

Each player has their own "set" of chosen numbers. The constraint (ii) is personal: a player cannot choose a number consecutive to any of THEIR OWN previously chosen numbers. So if A chose 3, A can't choose 2 or 4 later, but B can choose 2 or 4.

Constraint (i) is global: no number can be chosen twice.

So the game: numbers 1 to n. Players alternate. A player picks an unclaimed number that is not adjacent to any number they personally already hold.

Let me think about small cases.

n=1: A picks 1. All numbers chosen → draw.

n=2: A picks 1 (or 2). B picks 2 (or 1). All chosen → draw.

n=3: A picks 1. B picks... B can pick 2 or 3. If B picks 3, A can pick 2 (2 is not adjacent to A's 1? 2 is consecutive to 1, so A can't pick 2). Wait, A has {1}, so A can't pick 2. A can pick 3? No, 3 taken. So A can't move. A loses. So if A picks 1, B picks 3, A loses.

What if A picks 2? B picks 1 or 3. Say B picks 1. A has {2}, can't pick 1 or 3. A can't move. A loses. If B picks 3, same. So A loses with n=3.

Wait, but can A pick 2 and then... A has {2}, forbidden for A: 1,3. Both taken or... 1 and 3 available. A can't pick either. So A loses.

So n=3: B wins (A loses).

Hmm wait, let me reconsider. After A picks 2, B picks 1. Now A needs to pick from {3} (since 2 taken, 1 taken). 3 is adjacent to A's 2. So A can't. A loses. Yes.

n=3: Second player B wins.

n=4: A picks 1. B picks... Let's see. A has {1}. B wants to win. Available: 2,3,4. B can pick 2,3, or 4 (none adjacent to B's empty set).

If B picks 4: A has {1}, forbidden 2. Available: 3. A picks 3 (not adjacent to 1). A has {1,3}. B has {4}, forbidden 3,5. Available: 2. B picks 2 (not adjacent to 4). All chosen → draw.

If B picks 3: A has {1}, forbidden 2. Available: 2,4. A picks 4 (not adjacent to 1). A={1,4}. B={3}, forbidden 2,4. Available: 2. B can't pick 2 (adjacent to 3). B loses!

So if A picks 1 and B picks 3, then A picks 4, B loses. So B shouldn't pick 3.

If B picks 2: A={1}, forbidden 2. Available 3,4. A picks 4 (not adj to 1). A={1,4}. B={2}, forbidden 1,3. Available 3. B can't pick 3 (adj to 2). B loses!

So if A picks 1, B's best is pick 4 → draw.

But can A do better than draw? A picks 1, B picks 4 → draw as shown. Let me check other A first moves.

A picks 2: B picks 4 (symmetry-ish). A={2}, forbidden 1,3. Available 1,3,4. A can't pick 1 or 3. A picks 4. A={2,4}. B={}? B picks next... wait order: A,B,A,B,...

Let me redo. n=4. A picks 2. B's turn. Available 1,3,4. B picks 4. A's turn. A={2}, forbidden 1,3. Available 1,3. A can't pick either. A loses!

So A picking 2 is bad. A picks 3 similar by symmetry. A picks 4 symmetric to picking 1.

So A picks 1 (or 4), B picks 4 (or 1), draw.

n=4: draw.

n=5: Let me think. A picks 3 (middle). A={3}, forbidden 2,4. B picks from {1,2,4,5}. 

Hmm this is getting complex. Let me think about the structure more generally.

Actually, let me think about this game more cleverly.

Key insight: Each player's chosen set must be an "independent set" in the path graph (no two consecutive). And the two players' sets are disjoint and together with unclaimed form a partition.

The game ends in a draw if all numbers are chosen, meaning the two players partition {1,...,n} into two sets, each being an independent set (no two consecutive within each player's set).

Wait, is that the condition for draw? Draw if all numbers chosen. For all numbers to be chosen, each player's set must be an independent set. So a draw is possible iff {1,...,n} can be partitioned into two independent sets, i.e., {1,...,n} is 2-colorable, i.e., bipartite. The path graph is bipartite! So a draw is always possible in principle (color by parity: odds to one, evens to other).

But the question is whether players can force a draw or force a win, with optimal play.

Actually the game might not end in a draw even though it's possible, because players make choices.

Let me reconsider. The path graph P_n is bipartite with the parity coloring. If both players cooperate, draw is achievable. But with optimal (adversarial) play, one player might force the other into a position where they can't move.

Let me think about it as: the game is a normal-play game where a player who can't move loses, but if all numbers get chosen it's a draw.

Let me reconsider small cases and compute more carefully, maybe write a mental minimax.

Actually, let me think about the structure. Let me consider the game state as (available numbers, A's set, B's set, whose turn). The constraint for the current player: pick an available number not adjacent to any in their own set.

This is complex. Let me try to find a pattern by computing small n.

Let me define the game value: from the perspective of the player to move, outcome is Win (current player wins), Lose, or Draw.

n=1: A picks 1, all chosen, draw. So outcome = Draw.

n=2: A picks 1, B picks 2, all chosen, draw. Or A picks 2, B picks 1, draw. Draw.

n=3: computed above, A loses (B wins). So outcome for A = Lose.

n=4: draw.

n=5: Let me compute.

A's options: pick 1,2,3,4,5. By symmetry pick 1,2,3.

Case A picks 3: A={3}, A forbidden {2,4}. Available {1,2,4,5}. B's turn.
  B options: 1,2,4,5 (none adjacent to B's empty set, all available).
  Subcase B picks 1: B={1}, B forbidden {2}. Available {2,4,5}. A's turn. A forbidden {2,4}. A can pick 5 (available, not forbidden). A picks 5. A={3,5}, A forbidden {2,4}. Available {2,4}. B's turn. B={1}, B forbidden {2}. B can pick 4 (available, not forbidden). B picks 4. B={1,4}. Available {2}. A's turn. A forbidden {2,4}→2 forbidden. A can't pick 2. A loses. So this line: A loses.
    Wait, could A have done better? After B picks 1, A's turn with available {2,4,5}, A forbidden {2,4}. A can only pick 5. So forced. Then B picks 4 forced? B={1}, forbidden{2}, available{2,4}. B can pick 4. Then A stuck. Alternatively B picks 2? B forbidden {2} so can't. So B picks 4. A stuck. A loses.
  Subcase B picks 2: B={2}, B forbidden {1,3}. Available {1,4,5}. A's turn, A forbidden {2,4}. A can pick 1 or 5.
    A picks 1: A={1,3}, A forbidden {2,4}. Available {4,5}. B's turn. B={2}, B forbidden{1,3}. B can pick 4 or 5. B picks 5: B={2,5}, forbidden{1,3,4,6}. Available{4}. A's turn, A forbidden{2,4}→4 forbidden. A can't. A loses. B picks 4: B={2,4}, forbidden{1,3,5}. Available{5}. A forbidden{2,4}. A can't pick 5? 5 not in A's forbidden (A forbidden is 2,4). So A can pick 5! A={1,3,5}. All chosen → draw. So B picks 5 → A loses. So B picks 5. A loses.
    A picks 5: A={3,5}, forbidden{2,4}. Available{1,4}. B={2}, forbidden{1,3}. B can pick 4. B={2,4}, forbidden{1,3,5}. Available{1}. A forbidden{2,4}. A can pick 1. A={1,3,5}. All chosen → draw. So B picks 4, then draw. Alternatively B picks 1? forbidden. So B picks 4 → draw. Hmm so if A picks 5, draw. But A wants to win or at least draw; A picking 5 gives draw, A picking 1 gives loss. So A picks 5 → draw in this subcase.
    Wait but B is the one choosing subcase. B wants A to lose. In subcase B picks 2, A can force draw (by picking 5). So from B's perspective, picking 2 leads to draw (A gets draw). But subcase B picks 1 leads to A losing. So B prefers picking 1. 
  So if A picks 3, B picks 1, A loses. So A picking 3 → A loses (B can force).

Hmm, so A picking 3 is losing for A.

Case A picks 1: A={1}, A forbidden {2}. Available {2,3,4,5}. B's turn.
  B options: 2,3,4,5.
  Subcase B picks 5: B={5}, B forbidden{4}. Available{2,3,4}. A's turn, A forbidden{2}. A can pick 3 or 4.
    A picks 3: A={1,3}, forbidden{2,4}. Available{2,4}. B's turn, B={5}, forbidden{4}. B can pick 2. B={2,5}. Available{4}. A forbidden{2,4}→4 forbidden. A can't. A loses.
    A picks 4: A={1,4}, forbidden{2,3,5}. Available{2,3}. B={5}, forbidden{4}. B can pick 2 or 3. B picks 3: B={3,5}, forbidden{2,4}. Available{2}. A forbidden{2,3,5}→2 forbidden. A can't. A loses. B picks 2: B={2,5}, forbidden{1,3,4}. Available{3}. A forbidden{2,3,5}→3 forbidden. A can't. A loses. So A picks 4 → A loses.
    So after B picks 5, A loses (both A options lose). 
  So A picks 1, B picks 5 → A loses.

Hmm. So A picks 1 also losing?

Wait, but B picking 5 — is that B's best? B wants A to lose, and picking 5 achieves that. So yes.

Case A picks 2: A={2}, A forbidden{1,3}. Available{1,3,4,5}. B's turn.
  B options: 1,3,4,5.
  Subcase B picks 5: B={5}, forbidden{4}. Available{1,3,4}. A forbidden{1,3}. A can pick 4. A={2,4}, forbidden{1,3,5}. Available{1,3}. B={5}, forbidden{4}. B can pick 1 or 3. B picks 1: B={1,5}, forbidden{2,4}. Available{3}. A forbidden{1,3,5}→3 forbidden. A can't. A loses. B picks 3: B={3,5}, forbidden{2,4}. Available{1}. A forbidden{1,3,5}→1 forbidden. A can't. A loses. So A loses.
  So A picks 2, B picks 5 → A loses.

So for n=5, A loses in all cases? Let me double check A picks 1 more carefully — maybe A has a better response.

A picks 1, B picks 5. Available{2,3,4}, A forbidden{2}. A can pick 3 or 4.
  A picks 3: A={1,3}, forb{2,4}. Avail{2,4}. B={5}, forb{4}. B picks 2. B={2,5}. Avail{4}. A forb{2,4}→ can't. A loses. Could B pick 4? forb. So B picks 2, A loses. 
  A picks 4: A={1,4}, forb{2,3,5}. Avail{2,3}. B={5},b{4}. B picks 3 (or 2). Either way A loses as shown.
So yes A loses.

So n=5: A loses (B wins).

n=1: draw, n=2: draw, n=3: B wins, n=4: draw, n=5: B wins.

Let me guess the pattern. Maybe: draw when n is even, B wins when n is odd? But n=1 is odd and draw. Hmm. n=1 draw, n=3 B wins, n=5 B wins.

Let me reconsider n=1. n=1: only number is 1. A picks 1. All chosen → draw. Yes draw.

So odd: n=1 draw, n=3 B wins, n=5 B wins. Even: n=2 draw, n=4 draw.

Hmm, maybe n=1 is special. Let me compute n=6.

This is getting complicated. Let me think more structurally.

Actually, let me reconsider. Maybe there's a strategy-stealing or pairing argument.

Let me think about the parity coloring. Color odds black, evens white. Note: a player's set being an independent set means... actually no, independent set means no two consecutive, which is exactly that within the player's set, no two adjacent in path. The path is bipartite with parity, so each parity class is an independent set. But a player's set can mix parities as long as no two are consecutive (e.g., {1,4} has 1 odd, 4 even, not consecutive, fine).

Hmm. Let me think about the total number of moves. The game ends when either all chosen (draw) or current player can't move (current player loses).

Let me think about maximum number of picks. Each player picks an independent set. The two independent sets are disjoint. Total picks = |A| + |B|. Draw iff total = n.

For the game to be a draw, need to partition {1..n} into two independent sets. Always possible (parity). But adversarial play might prevent it.

Let me think about a strategy for B when n is odd and ≥3.

Idea: B uses a "mirror" strategy around the center. For n odd, center is (n+1)/2. Pair numbers symmetrically: (i, n+1-i). When A picks i, B picks n+1-i.

Let me check: does this maintain B's constraint? B's set would be {n+1-i : i in A's set}. B needs no two consecutive in B's set. If A's set has no two consecutive (which it must, by A's own constraint), then is {n+1-i} also having no two consecutive? Reflection preserves adjacency: n+1-i and n+1-j are consecutive iff i and j are consecutive. So yes, B's set is also an independent set. Good, B's constraint maintained.

Also need n+1-i available and not equal to i (so that B doesn't pick same). If i = n+1-i, i.e., i = (n+1)/2 (the center), then B can't mirror. So if A picks the center, B needs a different response.

Also need n+1-i not already chosen by A. Since A's set is independent and we're mirroring, could A have both i and n+1-i? Those are symmetric positions; they're consecutive only if... i and n+1-i consecutive means |i - (n+1-i)| = 1, i.e., |2i - n - 1| = 1, i.e., 2i = n or n+2, i even cases. E.g., n=5: i and 6-i. i=2,4: 2 and 4 not consecutive (diff 2). i=3 center. So A could pick both 2 and 4? They're not consecutive, so allowed. Then B can't mirror 2→4 since 4 taken.

Hmm, so the mirror strategy has issues when A picks symmetric pairs.

Let me reconsider. Let me think about n=5 with mirror strategy. Center 3. 
A picks 1 → B picks 5. A picks 2? A={1}, forb{2}. Can't pick 2. A picks 3? A={1,3}, forb{2,4}. B={5}, forb{4}. B mirrors: A picked 3 (center), no mirror. Hmm.

Actually in n=5, we saw B wins. Let me see the winning strategy. B picks 5 in response to A's 1 (that's the mirror!). Then A picks 3 or 4. If A picks 3: B={5}, mirror of 3 is 3 (center), can't. B picks 2 (we found B picks 2 → A loses). If A picks 4: mirror is 2, B picks 2 or 3 → A loses.

So mirror works mostly; center is the issue but B handles it.

Let me think about whether B always wins for odd n ≥ 3, and draw for even n.

For even n, mirror strategy: pair (i, n+1-i), no center. B mirrors A. Then B's set = reflection of A's set, independent. At the end, if A has picked set S, B has picked reflection. Total = 2|S| if S and reflection disjoint. They're disjoint since no fixed point (n even, n+1-i ≠ i always... wait n even, n+1 odd, n+1-i = i means 2i = n+1, no integer solution). So S and reflection always disjoint. So after A picks k numbers and B mirrors k numbers, 2k numbers chosen. Game continues until... A can't move → A loses? But we said even n is draw. Contradiction?

Wait, the mirror strategy for B: whenever A picks i, B picks n+1-i. This ensures B always can move (as long as A just moved and the mirror is available). The game ends when A can't move (A loses) or all chosen (draw). 

If B mirrors perfectly, the number of chosen numbers is always even after B's turn. A moves on odd-count states. A can't move when all available numbers for A are forbidden/taken. 

Hmm, but does mirror guarantee A eventually can't move, or draw? Let me check n=4 with mirror.

n=4: pairs (1,4),(2,3). A picks 1, B picks 4. A={1}, forb{2}. Available{2,3}. A picks 3 (not forb). A={1,3}, forb{2,4}. B mirrors: A picked 3, mirror 2. B picks 2. B={4,2}={2,4}. All chosen → draw. 

So n=4 mirror → draw. A picked 1 then 3, B picked 4 then 2, all 4 chosen, draw. Good, consistent.

But could A deviate to make B's mirror fail? A picks 1, B picks 4. A picks 3 (only non-forbidden available besides... available {2,3}, A forb{2}, so A must pick 3). So forced, draw. Good.

n=4 is draw confirmed.

Now for even n generally, does mirror always lead to draw, and can A do better? Mirror guarantees B can always respond, so B never gets stuck. The game ends with either A stuck (A loses) or all chosen (draw). For B to win, A must get stuck. For draw, all chosen.

With mirror, after each pair of moves, 2 numbers removed (i and n+1-i). The remaining available numbers form a symmetric set. A's forbidden set is A's own numbers' neighbors. 

Hmm, actually with mirror, does A always have a move until all are chosen? Not necessarily. Let me think about n=6.

n=6: pairs (1,6),(2,5),(3,4). 
A picks 1, B picks 6. A={1},f{2}. Avail{2,3,4,5}. A picks 3. B picks 4 (mirror of 3). A={1,3},f{2,4}. Avail{2,5}. A picks 5 (not forb, 5 not in {2,4}). B picks 2 (mirror of 5). All chosen → draw.

A picks 1, B picks 6. A picks 5. B picks 2. A={1,5},f{2,4,6}. Avail{3,4}. A picks 3 (not in f). B picks 4 (mirror of 3). All chosen draw.

A picks 1, B picks 6. A picks 4. B picks 3. A={1,4},f{2,3,5}. Avail{2,5}. A can't pick 2 or 5 (both forbidden). A loses!

Oh! So if A picks 4 (after 1,6), A gets stuck. But A wouldn't pick 4; A wants to win/draw. A picks 3 or 5 → draw. So with optimal A, draw. But this shows mirror doesn't always lead to draw; A can blunder. With optimal play A avoids losing moves. So n=6 draw (A can guarantee at least draw by good play, B mirrors guaranteeing B doesn't lose).

But wait — can A force a WIN in even n? For A to win, B must get stuck. With mirror strategy, B always has a response (mirror available), so B never gets stuck. So A can't win. And A can avoid losing (pick moves that don't get stuck). So even n → draw (with optimal play, A avoids loss, B avoids loss via mirror).

Hmm, but I need to verify A can always avoid getting stuck in even n. Let me think: is there always a "safe" move for A that doesn't lead to A getting stuck later?

Actually, let me reconsider. The claim "B's mirror is always available" — is it? When A picks i, is n+1-i always available (not already chosen)? B's set is the reflection of A's set so far. n+1-i could be in B's set already if A previously picked the mirror of i, i.e., A picked n+1-i before. But A's set is independent; can A contain both i and n+1-i? They're consecutive iff |2i-n-1|=1. For even n, 2i-n-1 is odd, can be ±1. E.g., n=6: 2i-7=±1 → i=3 or 4. So A could pick 3 and 4? 3,4 consecutive — not allowed (A's constraint). So A can't pick both 3 and 4. So A can't pick both i and n+1-i when they're consecutive. When they're not consecutive (|2i-n-1|>1), A could pick both. E.g., n=8: i=2, n+1-i=7, not consecutive, A could pick 2 and 7. Then when A picks 7, mirror is 2, but 2 already in A's set, so not available... but wait B would have mirrored earlier: A picks 2 first, B picks 7. Then 7 is taken by B, A can't pick 7 later. So A can't pick both 2 and 7 because B takes 7.

Right! Because B mirrors immediately. After A picks 2, B picks 7. So 7 is taken. A can never pick 7. So A's set and B's set: A picks i, B immediately takes n+1-i. So A can never pick n+1-i for any i A picked. So A's set S and B's set = reflection(S) are disjoint by construction. And B's mirror is always available because: when A picks i, is n+1-i free? n+1-i is in B's set iff A previously picked i' with n+1-i' = n+1-i, i.e., i'=i, no. n+1-i in A's set iff A picked n+1-i before, but A can't have because... actually A could pick n+1-i only if it were free, but B took it when A picked i... no wait, A picks i, then B picks n+1-i. So n+1-i becomes taken right after A picks i. So A can't pick n+1-i later. But could A have picked n+1-i BEFORE picking i? If A picked n+1-i first, then B would pick i (mirror), so i would be taken, A couldn't pick i now. Contradiction with A picking i now. So no. Therefore n+1-i is always free when B needs it. 

So B's mirror strategy is always executable for even n. B never gets stuck. So A can't win. Now does the game always end in draw (all chosen) or can A get stuck? A gets stuck if at A's turn, all available numbers are forbidden for A. With mirror, after B's turn, the available set is symmetric (reflection-closed) minus... hmm. Let me think: total chosen = 2k after B's k-th move. Available = n - 2k numbers, symmetric set. A needs an available number not adjacent to A's set.

Could A get stuck while numbers remain? That would mean A loses. A wants to avoid this. The question is whether A has a strategy to always reach draw, or whether B can force A to get stuck.

For even n, I'll conjecture draw: A can always ensure draw. Let me think about A's strategy: A also mirrors? No. Let me think: A wants to ensure all numbers get chosen. 

Actually, maybe A can also use a strategy to guarantee not getting stuck. Alternatively, maybe for even n it's a draw because both can avoid losing.

Hmm, but actually maybe for even n ≥ some value, B can force a win? Let me check n=6 more carefully — can B force A to lose (not just A blundering)?

n=6. A picks first. Let me see if B has a winning strategy (not just mirror→draw, but something better).

A picks 1: B's options. Let me explore B picks 6 (mirror) → we saw A can draw by picking 3 or 5. Can B do better than mirror?
  B picks 5 instead? B={5},f{4}. Avail{2,3,4,6}. A={1},f{2}. A picks 3,4,or 6.
    A picks 6: A={1,6},f{2,5}. Avail{2,3,4}. B={5},f{4}. B picks 2 or 3. B picks 3: B={3,5},f{2,4}. Avail{2,4}. A={1,6},f{2,5}. A can pick 4 (not in f). A={1,4,6},f{2,3,5}. Avail{2}. B={3,5},f{2,4}. B can't pick 2. B loses! So B shouldn't pick 3. B picks 2: B={2,5},f{1,3,4}. Avail{3,4}. A={1,6},f{2,5}. A picks 3 or 4. A picks 3: A={1,3,6},f{2,4,5}. Avail{4}. B={2,5},f{1,3,4}. B can't pick 4. B loses. A picks 4: A={1,4,6},f{2,3,5}. Avail{3}. B can't pick 3 (f{1,3,4}). B loses. So A picks 6 → B loses. So B picking 5 is bad for B (A picks 6 wins for A).
  So after A picks 1, B picking 5 lets A win. B should mirror (pick 6) for draw.

This is getting deep. Let me just try to establish the pattern computationally for more n, but I can't run code easily... actually I can use exec to run a Python minimax!

Let me write a quick minimax solver.

Actually, let me just code it up and run it.

Let me think about the state representation. State: (available bitmask, A's set bitmask, B's set bitmask, turn). But that's 3 bitmasks up to n. For small n (up to ~16) feasible.

The constraint for current player P (with set S_P): can pick k if k available (not in A or B) and k not adjacent to any in S_P, i.e., k-1 not in S_P and k+1 not in S_P.

Let me code minimax returning outcome from current player's perspective: W (current wins), L (current loses), D (draw).

Memoize on (avail, Aset, Bset, turn). Actually turn is determined by parity of moves = n - popcount(avail). And whose turn: A starts, so turn = A if (n - popcount(avail)) even, else B. But Aset/Bset differ. Actually we need to know whose set is whose. State (avail, Aset, Bset), turn derived from popcount. Memoize.

Let me write it.

Let me just run it.
Interesting! Pattern:
- n=1: Draw
- n=2: Draw
- n=3: B wins
- n=4: Draw
- n=5: B wins
- n=6: Draw
- n=7 onwards: B wins

So draws at n=1,2,4,6 and B wins for n=3,5 and n≥7.

Let me check more to be sure about larger even n.
Larger n is slow. Let me wait a bit.
Too slow for larger n. The pattern up to n=18 is clear enough: Draw for n ∈ {1,2,4,6}, B wins for n ∈ {3,5} ∪ {n ≥ 7}.

Let me kill it and think about the proof.

So the answer:
- Draw for n = 1, 2, 4, 6.
- B wins for n = 3, 5, and n ≥ 7.

Wait, let me double-check n=6 is draw and n=7 B wins, n=8 B wins. Yes from output.

Hmm, that's an interesting pattern. Let me reconsider: draws at 1,2,4,6. B wins at 3,5,7,8,9,...

So for n ≥ 7, B always wins. And small exceptions: 1,2,4,6 draw; 3,5 B wins.

Let me re-examine. Actually wait, let me reconsider whether the pattern is "B wins for all n ≥ 3 except n=4,6". Or "draw for n ∈ {1,2,4,6}, B wins otherwise (n≥3)".

n=1: draw, n=2: draw, n=3: B, n=4: draw, n=5: B, n=6: draw, n≥7: B.

So draws: {1,2,4,6}. B wins: {3,5} ∪ {7,8,9,...}.

Let me make sure about the proof. I need to:
1. Show draw for n=1,2,4,6 (exhibit strategies / it's easy for small).
2. Show B wins for n=3,5 (explicit).
3. Show B wins for n≥7 (general strategy).

For n≥7, B has a winning strategy. Let me think about what strategy.

Let me think about the structure. The key idea: B wants to force A into a position where A can't move but numbers remain.

Let me think about a pairing/mirror strategy for B that forces A to get stuck.

For odd n, mirror around center: B picks n+1-i in response to A's i. The center c=(n+1)/2 is special. Let me think: with mirror, after all non-center numbers are paired off, the center remains. 

Actually let me think about what happens with mirror for odd n. n=7: center 4. Pairs (1,7),(2,6),(3,5). A picks i, B picks 8-i. If A ever picks 4 (center), B picks... some response.

Let me simulate n=7 mirror. A picks 1, B picks 7. A={1},f{2}. Avail{2,3,4,5,6}. A picks 3, B picks 5. A={1,3},f{2,4}. Avail{2,4,6}. A picks 6, B picks 2. A={1,3,6},f{2,4,5,7}. Avail{4}. A's turn? Wait count: moves so far: A(1),B(7),A(3),B(5),A(6),B(2) = 6 moves, 1 left (4). A's turn (move 7). A={1,3,6}, f{2,4,5,7}. Avail{4}. 4 in f. A can't move. A loses! 

But wait, A didn't have to pick 6. Let me see if A could avoid. After A={1,3},f{2,4}, avail{2,4,6}. A can pick 6 only (2,4 forbidden). So forced. Then B picks 2 (mirror of 6). Avail{4}. A can't. So A loses. But A's earlier choices: after A picks 1, B picks 7, A={1},f{2}, avail{2,3,4,5,6}. A could pick 3,4,5,6. 
  A picks 4 (center): A={1,4},f{2,3,5}. B's turn, B={7},f{6}. Avail{2,3,5,6}. B mirrors 4→4 (center, can't). B needs other move. B picks... B wants to win. Hmm, mirror breaks at center.

So for odd n, the center is a problem for pure mirror. But B still wins (computed). Let me find B's strategy.

Actually, let me reconsider. Maybe B's strategy for odd n: mirror, and if A takes center, B takes some specific move.

Let me think differently. Let me reconsider the general winning strategy for B for n≥7.

Alternative: think of it as B trying to leave A stuck. 

Let me think about the "pairing strategy" more carefully. Consider pairing consecutive numbers: (1,2),(3,4),(5,6),... When A picks one from a pair, B picks the other. But B's constraint: B picking the other of the pair — is it adjacent to B's existing? B's set would be the "partners". If pairs are (1,2),(3,4),..., B picks 2 when A picks 1, picks 1 when A picks 2, etc. B's set: could contain 2 and 1? No, only one per pair (B picks the partner of whatever A picked). B's set has at most one from each pair. Are B's numbers non-consecutive? B could have 2 (from pair (1,2)) and 3 (from pair (3,4)) — consecutive! So B's constraint violated. So this pairing doesn't work for B.

Let me think about pairing (1,n),(2,n-1),... the reflection pairing. For B's constraint: B's set is reflection of A's set. Reflection preserves non-consecutiveness (A's set is independent → B's set independent). Good. So reflection pairing keeps B legal. The only issue is the center for odd n.

For even n, reflection pairing has no center, B always legal, B never stuck. So B can force at least draw (B never loses). And we saw even n=2,4,6 draw, n≥8 B wins. Wait n=8 B wins! So for even n≥8, B wins, meaning B forces A to get stuck. But mirror only guarantees B doesn't get stuck; it doesn't guarantee A gets stuck. For n=8, B wins, so B has a strategy to make A stuck. Mirror might be that strategy (A gets stuck eventually) or B plays differently.

Wait, for n=4,6 mirror leads to draw (A can avoid getting stuck). For n=8, B wins — does mirror make A stuck, or does B need a different strategy?

Let me check n=8 with mirror. Pairs (1,8),(2,7),(3,6),(4,5). 
A picks 1, B picks 8. A={1},f{2}. Avail{2,3,4,5,6,7}. A picks 3, B picks 6. A={1,3},f{2,4}. Avail{2,4,5,7}. A picks 5, B picks 4. A={1,3,5},f{2,4,6}. Avail{2,7}. A picks 7 (not in f). B picks 2 (mirror of 7). All chosen → draw.

Hmm, so this line draws. But B wins for n=8, so B shouldn't just mirror; B should play to win. Let me find B's winning strategy via the solver — extract the optimal move.

Let me modify the code to show B's optimal first response and the game tree for n=8.

Actually, let me reconsider. The result says B wins for n=8. So B has a strategy. Let me extract it.
Pattern: Draw for n ∈ {1,2,4,6}, B wins for n ∈ {3,5} ∪ {n≥7}.

Let me extract optimal strategies to understand the structure. Let me get the optimal first moves and key lines for n=7,8.
Wait, the value shown is "value(from A)" but it's computed as bestmove for B's turn, returning best from B's perspective (current player = B). So v2 = value from B's perspective. value(from A) = -v2. Let me recheck the print. It prints `v2` directly but labels "value(from A)". The bestmove returns (bm, best) where best is from current player (B) perspective. So v2 is from B's perspective. So "value(from A)" label is wrong; it's actually from B's perspective. v2=1 means B wins. So all lines B wins. Good, consistent: n=7,8 B wins regardless of A's first move.

Interesting: for n=7, when A picks 1, B's best response is 7 (mirror!). For n=8, A picks 1 → B picks 8 (mirror). For other A first moves, B picks 1. Let me look deeper — let me trace a full optimal game for n=7 and n=8 to see B's strategy.

Let me trace the game tree following optimal play (A tries to win/draw, B tries to win).
Interesting. Let me look at the patterns. For n=7, A first=1: B plays 7, then A plays 3, B plays 2, A plays 5, B plays 4, A stuck. 

Note B's strategy isn't pure mirror. For n=7, A=1,B=7 (mirror), A=3, B=2 (not mirror of 3 which is 5). Hmm.

Let me look at the structure differently. Let me observe: in all these traces, A gets stuck after 3 moves each (6 total moves), with 1 number remaining. So A makes 3 picks, B makes 3 picks, 1 left, A can't take it.

For n=7: 7 numbers, 6 picked, 1 left, A stuck. A's 3 picks + B's 3 picks = 6.
For n=8: 8 numbers, 6 picked, 2 left, A stuck. A's 3 + B's 3 = 6, 2 remaining.

So B wins by getting A stuck after A's 3rd move (B's 3rd move leaves A stuck).

Let me look at the structure of A's set and B's set when A gets stuck.

n=7, A=1,B=7,A=3,B=2,A=5,B=4: A={1,3,5}, B={7,2,4}={2,4,7}. Remaining={6}. A's forbidden from {1,3,5}: {2,4,6}. 6 is forbidden. A stuck. 

n=8, A=1,B=8,A=3,B=5,A=6,B=2: A={1,3,6}, B={8,5,2}={2,5,8}. Remaining={4,7}. A's forbidden from {1,3,6}: {2,4,7}. Both 4,7 forbidden. A stuck.

Interesting. So B's strategy creates a situation where A's own set blocks all remaining numbers.

This is complex. Let me think about a cleaner structural proof rather than reproducing B's exact strategy.

Let me think about the problem in terms of "the player who is forced to break the parity coloring loses" or some invariant.

Key observation: For a draw, the final partition must be A's set and B's set, both independent sets, partitioning {1..n}. Since the path is bipartite with the unique 2-coloring (up to swap) being parity, ANY partition into two independent sets must be exactly the parity coloring (odds to one player, evens to the other)!

Wait, is that true? Is the 2-coloring of a path unique? A path P_n is connected and bipartite, so it has exactly 2 proper 2-colorings (swap the two colors). So yes, the only way to partition {1..n} into two independent sets is {odd} and {even} (one player gets all odds, the other all evens).

So a draw requires: one player has all odds, the other all evens. 

So for a draw to occur, A must end with exactly {odd numbers} or {even numbers}, and B the complement.

Now, the game: A moves first. Total moves = n (all chosen). A moves on turns 1,3,5,...; B on 2,4,6,... Number of A's moves = ceil(n/2), B's moves = floor(n/2).

For a draw: A's set = odds or evens. |odds| = ceil(n/2), |evens| = floor(n/2). A has ceil(n/2) moves, B has floor(n/2) moves. So A's set size = ceil(n/2) = |odds|. So A must get all odds, B all evens. (For both odd and even n, A gets odds, B gets evens, since A has the larger-or-equal count.)

Wait for even n: |odds|=|evens|=n/2. A has n/2 moves, B has n/2 moves. So A could be odds or evens. For odd n: |odds|=(n+1)/2=ceil, |evens|=(n-1)/2=floor. A has ceil moves. So A=odds, B=evens.

So for a draw, the partition is forced: A=odds, B=evens (for odd n), or A=odds,B=evens OR A=evens,B=odds (for even n).

Now here's the key: A moves first. A picks some number. For a draw to happen, A must eventually collect exactly all odds (or all evens). 

Now think about B's strategy to PREVENT a draw and instead win. B wins if A gets stuck (can't move) while numbers remain. B wants to force A into a position where A's own set blocks the remaining available numbers.

Hmm, let me think about a cleaner invariant/strategy.

Let me reconsider. The condition for draw is very rigid (parity partition). So B's goal: prevent the parity partition from being completed, AND ensure A is the one who gets stuck (not B).

Let me think about "who gets stuck". 

Alternative framing: think of it as a game where both players are building independent sets. The game ends when current player can't extend. 

Let me think about a strategy for B based on the parity insight.

Claim: For n ≥ 7 (and n=3,5), B wins. For n ∈ {1,2,4,6}, draw.

Let me think about B's strategy for n ≥ 7. 

Idea: B tries to "steal" one number of A's required parity, forcing A to either get stuck or deviate.

Hmm, let me think more concretely. Let me consider the parity classes O (odds) and E (evens). For a draw, A needs all of one class and B the other.

B's strategy: B will claim a number from the class that A is "supposed" to take, breaking the draw. But B must also ensure A gets stuck (not B).

Actually, let me think about it as: B plays to make A stuck. 

Let me look at the traces again for a structural pattern.

n=7, A=1,B=7,A=3,B=2,A=5,B=4: 
A's picks: 1,3,5 (all odd!). B's picks: 7,2,4. B picked 7 (odd!) and 2,4 (even). 
Remaining: 6 (even). A needs 6 but 6 adjacent to A's 5. Stuck.
So A took odds 1,3,5; B took 7 (an odd!) plus 2,4. By B taking 7 (odd), A can't complete all odds. And A's own 5 blocks 6.

n=8, A=1,B=8,A=3,B=5,A=6,B=2:
A: 1,3,6. B: 8,5,2. Remaining 4,7. A's forbidden {2,4,7}. Both remaining blocked.
A took 1,3 (odd) and 6 (even). B took 8,2 (even) and 5 (odd).

Hmm, the structure isn't simply "B steals parity." Let me think differently.

Let me think about a cleaner strategy. Let me consider the following B strategy for n ≥ 7:

Actually, let me reconsider. The problem is from a competition (looks like an ISL/shortlist problem). Let me think about what the clean answer is.

The pattern: Draw for n ∈ {1,2,4,6}, B wins otherwise.

Hmm wait, let me double check n=6 is really a draw and reconsider. And reconsider whether maybe I have the pattern right. Let me re-examine n=6 thoroughly and also n=10,12 to be sure B wins for even n≥8. The computation up to 18 confirms. Let me trust it.

Actually, let me reconsider — maybe the pattern is cleaner: Draw iff n ∈ {1,2,4,6}, i.e., n ≤ 6 and n ≠ 3,5. Or: B wins iff n ≥ 3 and n ∉ {4,6}. Equivalently B wins for n=3,5 and n≥7.

Hmm, is there a cleaner characterization? n=1,2,4,6 draw. These are n where... 1,2,4,6. Differences: 1,2,2. Not obvious. Maybe n=2^k or n=2k? 1,2,4 are powers of 2, but 6 isn't. n=1,2,4,6 = n where n≤6 and n even or n=1? 1 (odd),2,4,6 even. 3,5 odd ≥3. So: draw iff (n=1) or (n even and n≤6). B wins iff (n odd and n≥3) or (n even and n≥8). 

Hmm, let me double-check n=6 is draw and n=8 B wins by re-examining. The code is trustworthy I think. But let me re-verify n=6 by hand to be safe, since it's a boundary.

n=6. A picks 1. B's responses:
We need to check if B can force win, or A can force draw.

Let me just trust the minimax but verify the code logic once. The value function: returns from current player's perspective. 1=win, -1=lose, 0=draw. cv = -child (negamax). Looks right. Draw when avail==0 and no legal moves. A player with no legal moves and avail != 0 → loses (returns -1). Good.

Let me also double check: when avail==0, all numbers chosen → draw (return 0). And if avail != 0 but no legal moves → current loses. Correct per rules.

I'm fairly confident: Draw for n ∈ {1,2,4,6}, B wins for n ∈ {3,5} ∪ {n ≥ 7}.

Hmm, but this is a somewhat ugly answer. Let me reconsider whether the problem might have a cleaner answer that I'm missing due to a bug. Let me re-examine the rules once more.

"(ii) A player cannot choose a number consecutive to any of those the player has already chosen on any previous turn."

Yes, personal constraint. My code: myset adjacency. Correct.

"(iii) The game is a draw if all numbers have been chosen; otherwise the player who cannot choose a number anymore loses."

Yes. Correct.

Let me re-verify n=6 by hand more carefully to be sure it's a draw, because the boundary matters.

n=6. A picks 1. 
B's options: 2,3,4,5,6.
We want to know if B has a move that forces A to lose, or if A can always force draw.

By symmetry A could also pick other things, but let me check if A picking 1 leads to draw or win for someone, assuming optimal play. Actually A will pick the move that's best for A. The code says n=6 is draw, so A's best is draw.

Let me verify A picks 1, B's best response leads to draw (A can force draw), and no B response leads to B win.

A picks 1: A={1},f{2}. Avail{2,3,4,5,6}. B's turn.
  B picks 6 (mirror): B={6},f{5}. Avail{2,3,4,5}. A's turn, f{2}. A picks 3 or 4.
    A picks 3: A={1,3},f{2,4}. Avail{2,4,5}. B={6},f{5}. B picks 2 (or 4). 
      B picks 2: B={2,6},f{1,3,5}. Avail{4,5}. A={1,3},f{2,4}. A picks 5 (not in f). A={1,3,5},f{2,4,6}. Avail{4}. B={2,6},f{1,3,5}. B can't pick 4? 4 not in B's f{1,3,5}. So B picks 4. All chosen → draw.
      B picks 4: B={4,6},f{3,5}. Avail{2,5}. A={1,3},f{2,4}. A picks 5 (not in f). A={1,3,5}. Avail{2}. B={4,6},f{3,5}. B picks 2. All chosen draw.
    A picks 4: A={1,4},f{2,3,5}. Avail{2,3,5}. B={6},f{5}. B picks 2 or 3.
      B picks 2: B={2,6},f{1,3,5}. Avail{3,5}. A={1,4},f{2,3,5}. A can't pick 3 or 5. A stuck! A loses.
      B picks 3: B={3,6},f{2,4}. Avail{2,5}. A={1,4},f{2,3,5}. A can't pick 2 or 5. A stuck! A loses.
    So if A picks 4, A loses. So A picks 3 → draw. So after B picks 6, A picks 3 → draw.
  So B picks 6 → draw (A plays correctly). Can B do better?
  B picks 5: B={5},f{4,6}. Avail{2,3,4,6}. A={1},f{2}. A picks 3,4,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{2,3,4}. B={5},f{4,6}. B picks 2 or 3.
      B picks 2: B={2,5},f{1,3,4,6}. Avail{3,4}. A={1,6},f{2,5,7}. A picks 3 or 4. A picks 3: A={1,3,6},f{2,4,5,7}. Avail{4}. B={2,5},f{1,3,4,6}. B can't pick 4. B stuck! B loses. A picks 4: A={1,4,6},f{2,3,5,7}. Avail{3}. B={2,5},f{1,3,4,6}. B can't pick 3. B loses. So A picks 6 → B loses. 
    So B picks 5 is bad (A picks 6, B loses).
  B picks 4: B={4},f{3,5}. Avail{2,3,5,6}. A={1},f{2}. A picks 3,5,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{2,3,5}. B={4},f{3,5}. B picks 2. B={2,4},f{1,3,5}. Avail{3,5}. A={1,6},f{2,5,7}. A picks 3. A={1,3,6},f{2,4,5,7}. Avail{5}. B={2,4},f{1,3,5}. B can't pick 5. B loses. So A picks 6 → B loses.
  B picks 3: B={3},f{2,4}. Avail{2,4,5,6}. A={1},f{2}. A picks 4,5,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{2,4,5}. B={3},f{2,4}. B picks 5. B={3,5},f{2,4,6}. Avail{2,4}. A={1,6},f{2,5,7}. A picks 4. A={1,4,6},f{2,3,5,7}. Avail{2}. B={3,5},f{2,4,6}. B can't pick 2. B loses. So A picks 6 → B loses.
  B picks 2: B={2},f{1,3}. Avail{3,4,5,6}. A={1},f{2}. A picks 3,4,5,or 6.
    A picks 6: A={1,6},f{2,5,7}. Avail{3,4,5}. B={2},f{1,3}. B picks 4 or 5.
      B picks 4: B={2,4},f{1,3,5}. Avail{3,5}. A={1,6},f{2,5,7}. A picks 3. A={1,3,6},f{2,4,5,7}. Avail{5}. B={2,4},f{1,3,5}. B can't. B loses.
      B picks 5: B={2,5},f{1,3,4,6}. Avail{3,4}. A={1,6},f{2,5,7}. A picks 3 or 4. A picks 3: A={1,3,6}. Avail{4}. B={2,5},f{1,3,4,6}. B can't pick 4. B loses. A picks 4: A={1,4,6}. Avail{3}. B can't pick 3. B loses.
    So A picks 6 → B loses.
  So after A picks 1, every B response either draws (B picks 6) or loses for B (B picks 2,3,4,5). So B's best is pick 6 → draw. So A picks 1 → draw.

Now I should check A's other first moves to ensure A can't WIN (force B to lose). If A could win with some first move, n=6 would be "A wins" not draw. Code says draw, so A's best is draw (can't win). Let me trust that. Actually let me verify A can't win: A picks 2,3 etc. need B to have a drawing response. This is a lot. I'll trust the code.

OK so the pattern holds. Now I need to PROVE it.

The answer: 
- Draw for n = 1, 2, 4, 6.
- B wins for n = 3, 5, and n ≥ 7.

Hmm, this is a somewhat irregular answer. Let me reconsider if maybe I'm wrong about n=6 or n=8. Let me re-examine by re-running with a sanity check / different method for n=6 and n=8.

Actually the code is straightforward negamax, I trust it. Let me also verify n=5 B wins and n=4 draw by hand (done n=4, n=5 partially). And n=3 B wins (done). Good.

Now, the proof. This is the hard part. Let me think about how to prove B wins for n ≥ 7 and draw for {1,2,4,6}.

Let me think about a clean strategy for B for n ≥ 7.

Let me look at the traces more to find B's strategy pattern.

n=7 traces (B's moves):
A=1: B=7,3→2,5→4. (B:7,2,4)
A=2: B=1,4→3,6→5. (B:1,3,5)
A=3: B=1,5→4,7→6. (B:1,4,6)
A=4: B=1,2→3,6→5. (B:1,3,5)
A=5: B=1,2→3,7→6. (B:1,3,6)
A=6: B=1,2→3,4→5. (B:1,3,5)
A=7: B=1,2→3,4→5. (B:1,3,5)

Hmm, for A=2,3,4,5,6,7 B's first move is 1. For A=1, B's first move is 7.

Let me see: when A picks a (a≠1), B picks 1. Then A's f includes a±1. 

This is getting complicated. Let me think about a higher-level strategy.

Alternative approach: Let me think about the problem as a known competition problem. The answer "draw for n∈{1,2,4,6}, B wins otherwise" — let me see if this matches a known result. Actually this looks like it could be ISL 2018 C8 or similar. Let me think...

Actually, let me reconsider. Let me reconsider the possibility that the answer is cleaner and I have an off-by-one. Let me re-examine n=6 super carefully with the code by printing the full game value and also checking n=6 with A picking each first move and the value.

Let me also extend the computation with a more efficient approach (symmetry + memo) to confirm n=10,12,14 are B wins (already have up to 18). I'm confident.

Hmm, the irregular answer {1,2,4,6} is suspicious. Let me reconsider: maybe the intended answer is "B wins for all n ≥ 3" and my n=4,6 are wrong? But I hand-verified n=4 draw and n=6 draw (A picks 1 → draw). Let me re-examine n=6: is there an A first move that wins for A, or does B have a winning response to every A move? I showed A picks 1 → draw (B can't win, A can't win). For n=6 to be "B wins", B would need to win against every A first move. But A picks 1 → draw at best for B. So n=6 is NOT B wins. And A can't win either (need to verify but trust code). So n=6 draw. Confirmed.

So the answer really is irregular. Let me reconsider—maybe the problem is from a specific competition and the answer is indeed this irregular set. Let me search memory: This looks like IMO 2018 Shortlist C4 or similar... Actually the problem statement "Let n be a positive integer. Two players A and B play a game..." with these exact rules — I recall this might be from IMO Shortlist 2017 C6 or 2018. The answer might indeed be "B wins for n≥3 except n=4,6" or similar. Hmm.

Actually, wait. Let me reconsider. Let me re-examine: maybe the answer is "A wins" for some n? The code never says A wins. Let me check larger... all B wins or draw. So A never wins. That makes sense by strategy-stealing-ish reasoning? Not obviously.

Let me reconsider the draw cases. n=1: trivial draw. n=2: draw. n=4: draw. n=6: draw. And B wins for n=3,5,7,8,9,... So for n≥7 always B wins.

Let me reconsider: is it possible that for very large even n, it becomes draw again? The code confirms B wins up to 18. I'll conjecture B wins for all n≥7.

Now I need to construct B's winning strategy for n≥7 and drawing strategies for {1,2,4,6}, plus B's wins for {3,5}.

This is a hard proof. Let me think about a clean strategy for B for n ≥ 7.

Let me think about the structure. The crucial fact: a draw requires the final position to be the parity partition (A=odds, B=evens, or swapped). 

B's winning idea: B will make a move that "breaks" the parity partition in a way that leaves A stuck.

Let me think about a specific clean strategy. Consider B adopting the following: B always responds to keep the game within a "trap."

Let me think about the traces for n=7 again, specifically A=1: B=7 (mirror), then A forced to 3 (only non-forbidden available: avail{2,3,4,5,6}, A f{2}, so A can pick 3,4,5,6 — not forced!). Wait A picked 3 in the trace but could pick 4,5,6. The trace follows optimal A (which still loses). Let me see all A options after A=1,B=7.

Hmm, the trace just shows one optimal line. Let me get the full picture: for n=7, A=1,B=7, what are A's options and B's responses.

This is getting really involved. Let me step back and think about whether there's a clean structural strategy.

Clean strategy idea for B (n ≥ 7): 

Reflection strategy with a twist. Let me consider the reflection pairing (i, n+1-i). B mirrors A. As shown, for even n this keeps B legal and B never stuck. But does it make A stuck? For n=4,6 it leads to draw (A not stuck if A plays well). For n≥8, does mirror make A stuck?

Earlier for n=8, A=1,B=8,A=3,B=6,A=5,B=4,A=7,B=2 → draw (all chosen). So pure mirror → draw for n=8, but B can do better (win). So mirror is not B's winning strategy for n=8.

So B needs a different strategy. Let me look at B's actual winning strategy for n=8, A=1: B=8, then A=3 (optimal A), B=5 (not mirror of 3 which is 6!). So B deviates from mirror at move 2.

n=8, A=1,B=8,A=3,B=5: B picked 5 instead of 6. Then A=6,B=2, A stuck.
A={1,3,6}, B={8,5,2}. Remaining{4,7}. A's f from {1,3,6}: {2,4,5,7}. 4,7 both in f. Stuck.

Interesting. So B's strategy: after A=1,B=8,A=3, B plays 5 (not 6). Why 5? This blocks A from taking 6's neighbor... hmm. Actually B taking 5 means A can later take 6 (6 not adjacent to A's {1,3}). A takes 6, then A's set {1,3,6} blocks 4,5,7. Remaining after B=2: {4,7} both blocked.

Let me think about this as B setting a trap. This is quite intricate. 

Given the complexity, maybe the cleanest proof approach is:

1. Establish the parity-partition characterization of draws.
2. For n ∈ {1,2,4,6}: exhibit explicit drawing strategies (or just verify small cases).
3. For n=3,5: explicit B winning strategies.
4. For n ≥ 7: give a general B winning strategy.

For part 4, I need a clean general strategy. Let me think harder.

Let me think about n ≥ 7 and try to find a uniform strategy. Let me consider B's strategy based on reducing to a smaller game.

Idea: B's first move creates a situation that splits the board into independent components, and B can mirror within components.

When a number k is taken (by anyone), it doesn't split the board for the adjacency constraint directly, because the constraint is about a player's OWN set, not all taken numbers. Hmm, but availability is global.

Let me reconsider. The "available" numbers shrink globally. A player's legal moves = available numbers not adjacent to their own set.

Let me think about the endgame condition for A getting stuck. A is stuck when every available number is adjacent to some number in A's set. I.e., A's set is a dominating set of the available numbers (in the path). 

For A to be stuck with remaining numbers R (available), A's set must dominate R: every r in R has a neighbor in A's set.

B wants to engineer: after B's move, the remaining available R is dominated by A's set, and it's A's turn.

Conversely B must avoid being in the symmetric situation.

This is a complex combinatorial game. Given the difficulty, let me reconsider whether the intended answer might actually be simpler and I should re-examine.

Wait, actually, let me reconsider the problem. Let me re-read: "determine the outcome of the game." Maybe the answer is meant to be piecewise and the proof uses the parity-partition insight plus casework. Competition problems can have piecewise answers.

Let me reconsider: maybe the answer is "B wins for n ≥ 3 except n = 4, 6" — i.e., draw for n=1,2,4,6 and B wins otherwise. Let me see if this is a known problem. 

Actually I now recall: this is IMO 2018 Shortlist C4 (or C5). Let me recall the answer... I think the answer for this problem is: "B wins for n ≥ 3, except n = 4 and n = 6 where it's a draw." Hmm, or maybe the answer involves n mod something.

Actually, let me just go with the computed answer and construct a proof. Given the complexity of a fully general strategy for n≥7, let me think about a clean inductive or structural strategy.

Let me reconsider the traces to find a pattern for B's strategy for general n≥7.

Let me get traces for n=9,10,11 to see the pattern.
Now I see a clear pattern for B's strategy when A picks 1 (or generally picks an endpoint-ish number).

For n=9, A=1: B=9, A=3, B=2, A=5, B=4, A=7, B=6, A stuck. 
A's picks: 1,3,5,7 (arithmetic progression, all odd!). B's picks: 9,2,4,6. Remaining: 8. A's f from {1,3,5,7}: {2,4,6,8}. 8 blocked. Stuck.

For n=11, A=1: B=11, A=3, B=2, A=5, B=4, A=7, B=6, A=9, B=8, A stuck.
A: 1,3,5,7,9. B: 11,2,4,6,8. Remaining: 10. A's f: {2,4,6,8,10}. 10 blocked. Stuck.

So for odd n, A=1: B=n, then A forced into 3,5,7,... (A picks all odd numbers 1,3,5,...,n-2), B picks n,2,4,6,...,n-1. Wait B picks n first then 2,4,6,...? B: 11,2,4,6,8 for n=11. So B picks n (odd) then evens 2,4,6,8. Remaining 10 (even). A={1,3,5,7,9}, f={2,4,6,8,10}. 10 blocked. A stuck.

But wait, is A forced to pick 3,5,7,9? After A=1,B=11: avail{2,3,4,5,6,7,8,9,10}, A f{2}. A can pick 3,4,5,6,7,8,9,10. A picked 3 (optimal). But could A pick something else to avoid the trap? The trace shows optimal A still loses, but via this line. Let me check: the trace follows optimal play meaning A picks the move that maximizes A's outcome; all lead to loss, so it picks the first found (3). But A might have other losing lines. The point is B has a winning strategy regardless.

Let me understand B's strategy for the line A=1:
- B picks n (the far endpoint).
- Then whatever A picks, B responds to keep A trapped.

Actually in the n=9,11 traces, after B=n, A picks 3, then B picks 2, A picks 5, B picks 4, ... So B picks the number just below A's pick (A picks 3, B picks 2; A picks 5, B picks 4; etc.). And A keeps picking the next odd number.

Why does A pick 3 then 5 then 7? Because after B picks 2, A's f={2} (from A's 1) ∪ ... A={1}, f={2}. After A picks 3, A={1,3}, f={2,4}. B picks 2. Now avail excludes 1,3,11,2. A's turn, f={2,4}. Available: 4,5,6,7,8,9,10. A can't pick 4. A picks 5 (or 6,7,8,9,10). A picks 5. A={1,3,5},f={2,4,6}. B picks 4. Avail: 6,7,8,9,10. A can't pick 6. A picks 7. Etc.

So A is being pushed: each time A picks the smallest available non-forbidden, which is the next odd. And B picks the even just below. This continues until A picks n-2 (odd), B picks n-3? Wait for n=9: A picks 7, B picks 6, then remaining 8, A f includes 8 (from 7). Stuck. For n=11: A picks 9, B picks 8, remaining 10, A f includes 10 (from 9). Stuck.

So the trap: A is forced along odds 1,3,5,...,n-2, B takes n and evens 2,4,...,n-3, and the last even n-1 remains but A's n-2 blocks it.

But this requires A to cooperate by picking 3,5,7,... What if A deviates, e.g., after A=1,B=9, A picks 5 instead of 3? Let me check B's response. The trace shows A's optimal (which still loses). B must have responses to all A deviations. Let me check by computing B's best response for n=9 after A=1,B=9,A=5.

Actually, the key question for the proof: does B have a uniform strategy? Let me think about it as: B's strategy is "reflection around the center" but with the center handled, OR B's strategy is "always play adjacent to A's last move on the side toward the center" or something.

Hmm, let me look at the n=9, A=1 line: B=9 (reflection of 1). Then A=3, B=2 (NOT reflection of 3=7). So B switches strategy. After B=9, the remaining board is {2,3,...,8} (a path of length 7, numbers 2..8). B's move 2 in response to A's 3... 

Actually, here's a cleaner idea: After A picks 1 and B picks n, the remaining available numbers are {2,3,...,n-1}, which is a path of length n-2. Now it's A's turn, A's set={1}, so A is forbidden from 2. Effectively A can't use 2. 

Hmm, let me think recursively. The sub-game on {2,...,n-1} with A forbidden at 2 (because A owns 1) and B forbidden at n-1 (because B owns n). 

This is like the original game but with both endpoints blocked for the respective players. 

Let me define a more general game: a path of consecutive integers [a, b], where A has a "forbidden zone" near a (owns a-1 or a is blocked) and B near b. Hmm, this is getting complicated.

Let me think about a cleaner inductive strategy.

Conjecture/Strategy for B (n ≥ 7): 
B's strategy: "Reflect A's move across the center; if A plays the center (only when n odd), B plays 1 (or some fixed move)."

Wait, but we saw for n=8 (even), B does NOT always reflect (A=1,B=8 reflect; A=3,B=5 not reflect of 3=6). So reflection isn't the strategy for even n≥8.

Let me look at n=8, A=1: B=8, A=3, B=5, A=6, B=2. 
After A=1,B=8: remaining {2,3,4,5,6,7}. A=3. B=5. Why 5? 
After A=3: A={1,3}, f={2,4}. Available {2,4,5,6,7}. A can't take 2,4. B's turn, B={8}, f={7}. B can take 2,3,4,5,6 (3 taken). B takes 5. 
Then A's turn: A={1,3},f={2,4}. Avail{2,4,6,7}. A can take 6 or 7. A takes 6 (optimal). A={1,3,6},f={2,4,5,7}. Avail{2,4,7}. B={8,5},f={4,6,7}. B can take 2. B=2. Avail{4,7}. A f{2,4,5,7} → 4,7 blocked. Stuck.

Alternatively A takes 7 instead of 6: A={1,3,7},f={2,4,6,8}. Avail{2,4,6}. B={8,5},f{4,6,7}. B takes 2. Avail{4,6}. A f{2,4,6,8}→4,6 blocked. Stuck. So either way A stuck.

So B's strategy after A=1,B=8,A=3 is B=5. The idea: B takes 5 to "split" and then A is forced into a trap.

This is genuinely intricate. I think reproducing the exact optimal strategy in a proof is hard. Let me think about whether there's a cleaner high-level argument.

Let me reconsider the parity-partition insight, which is the cleanest structural fact:

**Fact**: A draw occurs iff the final position is a 2-coloring of the path, i.e., one player has all odds and the other all evens. (Because the path's only proper 2-colorings are the parity coloring.)

Now, here's a cleaner way to think about who wins:

Consider the parities. A moves on odd turns (1st, 3rd, 5th, ...). 

Hmm, let me think about a potential function or a "pairing" that B uses.

Alternative clean strategy for B for n ≥ 7: 

Let me consider B playing to force A to take consecutive-ish positions. 

Actually, let me reconsider. Let me think about the following B strategy for ALL n ≥ 3:

B's strategy: After A's first move a, B plays to set up a "trap." 

This is really a casework-heavy problem. Given that this is a competition problem with an irregular answer {1,2,4,6}, the official solution likely does significant casework. Let me try to find the cleanest proof I can.

Let me reconsider the structure. Let me think about the game in terms of "gaps."

Actually, let me reconsider the parity argument more carefully, because I think it's the key to a clean proof.

**Parity Lemma**: The game is a draw iff the final sets are {odds} and {evens}. 

Now, consider this: A moves first. Suppose A wants a draw. Then A must end up with exactly the odds (or evens). 

Consider B's strategy: B will "steal" one number of each... no.

Let me think about it as: B wants to force A to take two numbers of the same parity that are "too close" or force A to take a number that blocks A's own future required numbers.

Hmm. Let me think about a specific clean strategy for B for n ≥ 7, then handle n=3,5 separately, and draws separately.

Let me look at the strategy for n=9,11 (odd, A=1): B plays n, then "just below A's move." Specifically, after A plays x (an odd number going up), B plays x-1. This pushes A up the odds. Let me verify this is a valid general strategy for odd n ≥ 7.

B's strategy for odd n ≥ 7 (against A=1, but need general A):
Actually let me focus on a general strategy. Let me consider:

**B's Strategy S (for n ≥ 7)**: 
- If A's first move a ≤ (n+1)/2, B plays n. Then B continues with strategy: whenever A plays x, B plays x-1 if available and legal, else x+1, else some default.

Hmm, this is ad hoc. Let me think more carefully and verify with the traces.

For n=9, A=1: B=9. A=3,B=2(=3-1). A=5,B=4(=5-1). A=7,B=6(=7-1). Yes "play x-1."
For n=11, A=1: B=11. A=3,B=2. A=5,B=4. A=7,B=6. A=9,B=8. Yes "play x-1."

For n=7, A=1: B=7. A=3,B=2(=3-1). A=5,B=4(=5-1). Yes.

For n=8, A=1: B=8. A=3, B=5 (NOT 3-1=2!). So the strategy differs for even n. Hmm.

Wait, for n=8, after A=1,B=8,A=3: if B played 2 (=3-1), then A={1,3},f{2,4}, avail{2,4,5,6,7}, B={8,2},f{1,3,7}. A's turn: avail{4,5,6,7}, A f{2,4}. A picks 5 or 6 or 7. If A picks 5: A={1,3,5},f{2,4,6}. avail{4,6,7}. B={8,2},f{1,3,7}. B picks 4 or 6. B picks 6: B={8,2,6},f{1,3,5,7}. avail{4,7}. A f{2,4,6}→4 blocked, 7? 7 not in A's f{2,4,6}. A picks 7! A={1,3,5,7},f{2,4,6,8}. avail{4}. B={8,2,6},f{1,3,5,7}. B can't pick 4? 4 not in B's f. B picks 4. All chosen → draw! 

So if B plays 2 (x-1 strategy) for n=8, A can force draw. That's why B plays 5 instead. So the "play x-1" strategy works for odd n but not even n.

So odd and even n need different strategies. For odd n ≥ 7, "B plays n then x-1" seems to work (when A starts at 1). But I need it to work for any A first move, and need to verify A can't deviate.

Let me check: for odd n, A=1, B=n, then B plays x-1. Does A have a deviation that escapes? Let me check n=9, A=1,B=9, A deviates to 5 (instead of 3).

n=9, A=1,B=9,A=5: A={1,5},f{2,4,6}. avail{2,3,4,6,7,8}. B={9},f{8}. B's strategy "play x-1" → B plays 4. B={9,4},f{3,5,8}. avail{2,3,6,7,8}. A's turn, f{2,4,6}. A can pick 3,7,8. 
  A picks 7: A={1,5,7},f{2,4,6,8}. avail{2,3,6,8}. B={9,4},f{3,5,8}. B plays x-1=6. B={9,4,6},f{3,5,7,8}. avail{2,3,8}. A f{2,4,6,8}. A can pick 3. A={1,5,7,3}={1,3,5,7},f{2,4,6,8}. avail{2,8}. B={9,4,6},f{3,5,7,8}. B plays x-1=2. B={9,4,6,2},f{1,3,5,7,8}. avail{8}. A f{2,4,6,8}→8 blocked. A stuck! 
  A picks 8: A={1,5,8},f{2,4,6,7,9}. avail{2,3,6,7}. B={9,4},f{3,5,8}. B plays x-1=7. B={9,4,7},f{3,5,6,8}. avail{2,3,6}. A f{2,4,6,7,9}. A can pick 3. A={1,5,8,3},f{2,4,6,7,9}. avail{2,6}. B={9,4,7},f{3,5,6,8}. B plays x-1=2. B={9,4,7,2},f{1,3,5,6,8}. avail{6}. A f{2,4,6,...}→6 blocked. A stuck!
  A picks 3: A={1,5,3}={1,3,5},f{2,4,6}. avail{2,6,7,8}. B={9,4},f{3,5,8}. B plays x-1=2. avail{6,7,8}. A f{2,4,6}. A picks 7 or 8. A picks 7: A={1,3,5,7},f{2,4,6,8}. avail{6,8}. B={9,4,2},f{1,3,5,8}. B plays x-1=6. avail{8}. A f{2,4,6,8}→8 blocked. stuck. A picks 8: A={1,3,5,8},f{2,4,6,7,9}. avail{6,7}. B={9,4,2},f{1,3,5,8}. B plays x-1=7. avail{6}. A f{2,4,6,...}→6 blocked. stuck.

So for n=9, A=1,B=9, A=5 deviation, B's "play x-1" strategy still traps A. 

So the strategy "B plays n, then always x-1 (A's last move minus 1)" seems robust for odd n. But I need to verify B's moves are always legal (x-1 available and not adjacent to B's set).

B's set after playing n and then x-1's: B's set = {n} ∪ {x_i - 1}. The x_i are A's moves (after the first). A's moves x_i: A's set is independent, and includes 1 (first) and then x_2, x_3, ... B plays x_i - 1.

Is x_i - 1 available? x_i - 1 could be taken by A (if A picked x_i - 1) — but A's set is independent, A has x_i, so A doesn't have x_i - 1 (consecutive, forbidden). Could x_i-1 be taken by B already? B has {n} and {x_j - 1 : j < i}. x_i - 1 = x_j - 1 → x_i = x_j, no. x_i - 1 = n → x_i = n+1, impossible. So x_i - 1 not taken by B. Could be taken by A? Only if A picked it, but A can't pick x_i-1 (adjacent to x_i) — but A might have picked x_i-1 BEFORE picking x_i? No: if A picked x_i-1 earlier, then A's set has x_i-1, so A can't pick x_i now (adjacent). Contradiction. So x_i-1 not in A's set. So x_i-1 is available. 

Is x_i-1 legal for B (not adjacent to B's set)? B's set = {n, x_2-1, x_3-1, ...}. B needs x_i-1 not adjacent to any of these. x_i-1 adjacent to x_j-1 iff x_i adjacent to x_j. A's set is independent, so x_i, x_j not adjacent (for i≠j, both in A's set). So x_i-1, x_j-1 not adjacent. Good. x_i-1 adjacent to n iff x_i-1 = n±1, i.e., x_i = n or n+2. x_i ≤ n, so x_i = n. But n is taken by B (B's first move), so A can't pick n. So x_i ≠ n. So x_i-1 not adjacent to n. 

So B's move x_i-1 is always legal and available. So B can always execute "play x-1" after the first move (where B played n).

Now, does this strategy guarantee A gets stuck? Let me think about the end. A's first move is 1 (we're analyzing this case). Then A picks x_2, x_3, .... B picks n, x_2-1, x_3-1, ....

A's set: {1, x_2, x_3, ...}. A's forbidden set (neighbors): {0,2} ∪ {x_i ± 1}. Since 0 not in range, A's forbidden = {2} ∪ {x_i - 1, x_i + 1}.

Note B took x_i - 1 for each i. So A's forbidden includes x_i + 1 and 2 (and x_i - 1 which B took anyway).

The game ends when A can't move. A can move if there's an available number not in A's forbidden set.

Total numbers: n. A takes ceil... let me count moves. A moves: 1, x_2, x_3, ..., x_k (k moves). B moves: n, x_2-1, ..., x_k-1 (k moves). Total 2k numbers taken. Remaining n - 2k.

For A to be stuck on move k+1: all remaining numbers are in A's forbidden set.

Hmm, let me think about when A "runs out." A's available non-forbidden numbers. Initially after B plays n, A can pick from {2,...,n-1} minus {2} (forbidden) = {3,4,...,n-1}. A picks x_2. Then B picks x_2-1. A's forbidden grows by {x_2-1, x_2+1}. Available shrinks.

Let me think about the "frontier." This is like A is exploring and B blocks just behind.

Actually, let me think about the total count. A and B each make k moves, 2k total. The game ends with A stuck when remaining = n - 2k > 0 and all remaining are A-forbidden.

A's forbidden numbers (within [1,n]): neighbors of A's set. A's set = {1, x_2, ..., x_k}. These are k independent numbers. Their neighbors: each a in A's set contributes a-1, a+1 (within range). Total distinct forbidden ≤ 2k (but overlaps possible). Plus A's own numbers are taken (not available anyway).

Numbers not available = A's set ∪ B's set = 2k numbers. Numbers available = n - 2k. A is stuck iff available ⊆ forbidden(A).

Forbidden(A) ⊆ [1,n] \ A's set (since A's set is independent, neighbors aren't in A's set). |forbidden(A)| ≤ 2k. Available = n - 2k. 

Hmm, this counting doesn't immediately give stuck.

Let me think about it differently for the specific strategy. Let me reconsider: with B playing x_i - 1, B's set = {n, x_2-1, ..., x_k-1}. 

Let me think about which numbers are NOT taken and NOT forbidden for A. A number y is "playable by A" if y not taken and y not adjacent to A's set.

y taken: y ∈ A's set ∪ B's set.
y adjacent to A's set: y = a±1 for some a in A's set.

A is stuck iff no playable y.

Let me think about the structure of A's set under this strategy. A picks 1, then must pick from numbers not adjacent to 1 and not taken. After B takes n and x_2-1, etc.

This is getting complicated. Let me just verify the strategy works for odd n ≥ 7 by a cleaner argument, and check even n separately.

Actually, let me reconsider. Maybe there's a much cleaner unified strategy. Let me look at even n traces again.

n=8, A=1: B=8, A=3, B=5, A=6, B=2. 
n=10, A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4.
Hmm n=10: B=10, then A=3,B=2 (x-1!), A=5,B=7 (NOT x-1=4!). 

Wait n=10 A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4. Let me re-examine. After B=10,A=3,B=2: A={1,3},f{2,4}. avail{4,5,6,7,8,9}. A picks 5. A={1,3,5},f{2,4,6}. B={10,2},f{1,3,9}. avail{4,6,7,8,9}. B picks 7. Why 7? Then A={1,3,5},f{2,4,6}, avail{4,6,8,9}. A picks 8 (not in f). A={1,3,5,8},f{2,4,6,7,9}. avail{4,6,9}. B={10,2,7},f{1,3,6,8,9}. B picks 4. avail{6,9}. A f{2,4,6,7,9}→6,9 blocked. stuck.

Hmm so for n=10, B's strategy is more complex. The "x-1" doesn't uniformly apply.

This is getting really messy for a clean proof. Let me step back and think about whether there's a fundamentally cleaner approach.

Let me reconsider the parity partition insight and think about a strategy based on parity directly.

**Key Insight (Parity)**: A draw requires A to hold exactly one parity class and B the other. 

Now, here's a strategy idea for B: B ensures that A is forced to take a number that "collides" with the parity requirement, OR B takes a number of A's parity to break the draw, while maintaining a position where A gets stuck.

Hmm. Let me think about a "strategy stealing" or "Tweedledum" type argument.

Actually, let me reconsider. Let me think about B's strategy as: B always takes a number of the OPPOSITE parity to A's last move, adjacent to it. I.e., when A takes x, B takes x-1 or x+1 (opposite parity, adjacent). This is legal for B (B's set: are x_i ± 1 mutually non-adjacent? (x_i+1) and (x_j+1) adjacent iff x_i, x_j adjacent — no since A independent. (x_i+1) and (x_j-1) adjacent iff x_i+1 = x_j-1±1, i.e., x_i = x_j - 2 or x_i = x_j. If x_i = x_j - 2, then x_i, x_j differ by 2, not adjacent, allowed in A's set. Then x_i+1 = x_j - 1, so B would have x_i+1 and x_j-1 = same number! Conflict. Hmm.)

So B taking x±1 has conflicts. The "x-1" strategy avoids this (always x-1, no ±1 mixing).

Let me reconsider the "x-1" strategy for odd n and figure out the clean proof that A gets stuck.

**Odd n ≥ 7, B's strategy: B plays n first (in response to A's first move 1), then always plays (A's last move) − 1.**

Wait, but this assumes A's first move is 1. I need a strategy for any A first move. Let me handle general A first move for odd n.

By the traces, for odd n, when A's first move a ≠ 1, B plays 1. Let me look:
n=7, A=2: B=1. A=4,B=3,A=6,B=5. So B=1, then B plays x-1 (A=4→B=3, A=6→B=5). 
n=9, A=2: B=1. A=4,B=3,A=6,B=5,A=8,B=7. B plays x-1.
n=9, A=3: B=1. A=5,B=4,A=7,B=6,A=9,B=8. B plays x-1.

So for odd n, B's strategy: 
- If A's first move a is "small" (a ≤ center?), B plays n; if a is large, B plays 1? Let me check. n=7: A=1→B=7, A=2→B=1, A=3→B=1, A=4→B=1, A=5→B=1, A=6→B=1, A=7→B=1. Hmm, only A=1 gives B=7; all others B=1. That's strange. Let me check n=9: A=1→B=9, A=2→B=1, A=3→B=1. (only checked 1,2,3). 

Wait, that's asymmetric. For A=1, B=9 (the far end). For A=2, B=1 (the near end). Let me check A=5 (center) for n=9.

Let me get more traces for odd n with various A first moves to understand B's first response.
Interesting! For odd n, B's first response: if A picks 1, B picks n; otherwise B picks 1. (By symmetry, if A picks n, B should pick 1 — yes. And if A picks 1, B picks n. So B "completes the endpoint pair": B picks the endpoint far from A, unless A picked 1 in which case B picks n... wait that's the same. B picks the OPPOSITE endpoint. If A picks 1, B picks n. If A picks anything else (including n), B picks 1.)

Hmm, actually: A=1→B=n; A=n→B=1; A=other→B=1. So B picks 1 unless A picked 1 (then B picks n). Equivalently: B picks an endpoint (1 or n) different from A's move if A picked an endpoint; if A didn't pick an endpoint, B picks 1.

Actually simpler: B always picks 1, unless A picked 1 (then B picks n). I.e., B picks the smallest available endpoint, preferring 1.

Wait, but why not symmetric? If A picks n, B picks 1 (not n-1 or something). And if A picks 1, B picks n. So B picks the endpoint NOT chosen by A, when A chose an endpoint; and picks 1 when A chose an interior point.

Hmm, actually it's: B picks 1 if available, else n. Since if A picked 1, then 1 not available, B picks n. If A picked anything else, 1 is available, B picks 1. That's the rule! "B picks 1 if available, otherwise n."

Let me verify: A=1→1 not available→B=n. ✓. A=2→1 available→B=1. ✓. A=n→1 available→B=1. ✓.

So B's first move: pick 1 if available, else n. I.e., B grabs the leftmost endpoint (or rightmost if leftmost is taken).

Then subsequent: B plays x-1 (A's last move minus 1). Let me verify this holds for the case A=2,B=1 for odd n.

n=9, A=2, B=1: A={2},f{1,3}. avail{3,4,5,6,7,8,9}. B={1},f{2}. A's turn. A picks 4 (optimal, from trace). A={2,4},f{1,3,5}. B plays x-1=3. B={1,3},f{2,4}. avail{5,6,7,8,9}. A picks 6. A={2,4,6},f{1,3,5,7}. B plays x-1=5. avail{7,8,9}. A picks 8. A={2,4,6,8},f{1,3,5,7,9}. B plays x-1=7. avail{9}. A f{1,3,5,7,9}→9 blocked. stuck! 

So B's strategy for odd n ≥ 7: 
1. First move: pick 1 if available, else n.
2. Subsequent: pick (A's last move) − 1.

Let me verify legality of "x-1" in this context. B's set = {first} ∪ {x_i - 1}. Need x_i - 1 available and not adjacent to B's set.

Available: x_i - 1 not in A's set (A has x_i, independent, so A doesn't have x_i-1). Not in B's set: B has {first, x_j-1 for j<i}. x_i-1 = x_j-1 → x_i=x_j no. x_i-1 = first. first is 1 or n. If first=1: x_i-1=1→x_i=2. But if A picked 2 as first move, then B picked 1 (first). Then later A picks x_i=2? No, A already picked 2 as FIRST move. The x_i here are A's moves AFTER the first. So x_i ≠ 2 (A's first was 2, can't repeat). Hmm wait, actually in this branch A's first move is 2, B's first is 1. Then A's subsequent moves x_2, x_3,.... Could x_i = 2? No, 2 already taken by A. So x_i ≠ 2, so x_i - 1 ≠ 1 = first. Good. If first = n (this happens when A's first move is 1): x_i - 1 = n → x_i = n+1, impossible. Good.

Not adjacent to B's set: x_i-1 adjacent to x_j-1 iff x_i,x_j adjacent — no (A independent). x_i-1 adjacent to first(=1): x_i-1=2 → x_i=3. first=1, adjacent to 2. So if x_i=3, then x_i-1=2 is adjacent to B's 1. Illegal! 

Hmm. So when first=1 (A's first move ≠ 1), and A later picks 3, B can't play 2 (adjacent to B's 1). Let me check the trace: n=9, A=2,B=1. Did A ever pick 3? A picked 4,6,8 (evens). A's first was 2 (even), and A continued with evens. So A never picked 3 in that line. But could A deviate to pick 3?

A=2 (first), B=1. A={2},f{1,3}. avail{3,...,9}. A can't pick 3 (forbidden, adjacent to A's 2). So A can't pick 3! Great. So x_i=3 never happens because A's first move 2 blocks 3 for A.

More generally: if A's first move is a, A is forbidden from a-1, a+1. B's first move is 1 (when a≠1). B's set has 1, so B can't play 2 (adjacent to 1). B wants to play x-1; conflict only if x-1=2, i.e., x=3. Is A ever able to pick 3? A is forbidden from a±1. If a=2, A forbidden 1,3 → can't pick 3. If a=3, A forbidden 2,4 → can pick 3? No, 3 is A's first move (a=3), already taken. If a=4, A forbidden 3,5 → can't pick 3. If a≥4, A forbidden a-1,a+1; 3 is forbidden only if a=2 or 4. For a=5: A forbidden 4,6; 3 not forbidden, 3 available (not taken). So A could pick 3 later! Then B wants to play 2, but 2 adjacent to B's 1. Illegal.

Let me check: n=9, A=5 (first), B=1. A={5},f{4,6}. avail{2,3,4,6,7,8,9}. A's turn. Could A pick 3? 3 available, not in f. Yes A could pick 3. Then B's "x-1"=2, but 2 adjacent to B's 1 → illegal. So the strategy breaks?

Let me check the actual trace for n=9, A=5.
Now I see the pattern clearly for odd n. Let me analyze.

For odd n, B's strategy:
- First move: pick 1 if available, else n (i.e., pick 1 unless A took 1, then pick n).
- Then: B plays (A's last move) − 1.

Let me verify the "x-1" legality concern I raised. When A's first move a ≠ 1, B plays 1. Then A's subsequent moves. The concern was A picking 3 (so B plays 2, adjacent to B's 1). But looking at traces, when a ≠ 1, A's second move is never 3. Let me see why.

When a ≠ 1, B=1. A's set={a}, A forbidden {a-1,a+1}. A's second move options: available numbers in {2,...,n}\{a} not in {a-1,a+1}. 

In the traces, A's second move: 
- a=2: A picks 4 (not 3, since 3 forbidden). 
- a=3: A picks 5 (4 forbidden). 
- a=4: A picks 2 (3,5 forbidden; picks 2). 
- a=5: A picks 2 (4,6 forbidden; picks 2). 
- a=6: A picks 2.
- a=7: A picks 2.
- a=8: A picks 2.
- a=9: A picks 2.

So A's second move is never 3 when a≠1. But that's the OPTIMAL A. A could deviate and pick 3 (if legal). When is 3 legal for A's second move? 3 must be available (not taken: taken are {a, 1}; so 3 available iff a≠3) and not in A's forbidden {a-1,a+1} (so a≠2 and a≠4). So for a ≥ 5 (a≠3), 3 is available and not forbidden. So A could pick 3 as second move when a ≥ 5!

E.g., n=9, a=5, B=1. A could pick 3 (available, not forbidden since A forbidden {4,6}). Then B's "x-1" = 2, adjacent to B's 1 → ILLEGAL.

So the "x-1" strategy as stated doesn't work if A deviates. But the minimax says B still wins. So B must have a different response to A's deviation. The trace only shows the optimal A line (which avoids 3). I need to check B's response to A=5,B=1,A=3.

Let me check that specific line.
The strategy "B first plays 1 (or n if 1 taken), then plays x-1 if legal else x+1" works for n=9 against optimal A (A always gets stuck). But "optimal A" here means A plays to maximize its own outcome given B's fixed strategy. Since A always gets stuck, B's strategy is winning. But I should test against ALL A deviations, not just optimal. The minimax with B's fixed strategy and A optimal captures the worst case for B (A tries hardest to escape). If A still gets stuck in all lines, B's strategy wins. The trace shows one line per A-first-move, but A is playing optimally against B's strategy, so if A could escape, the trace would show escape (draw or A win). All show A stuck. 

But wait, "optimal A" against a FIXED B strategy: A plays to maximize A's outcome assuming B follows the fixed strategy. If the result is always "A stuck" (A loses), then B's strategy is winning. Yes. But I should double-check the code: when A is "optimal", it uses bestmove which uses `value` — but `value` assumes BOTH play optimally, not B-follows-fixed-strategy! That's a bug. The `value` function computes minimax with both optimal, so A's "bestmove" is the minimax best, NOT the best against B's fixed strategy.

So this test is flawed: A's moves are minimax-optimal (assuming B also optimal), not optimal-against-B's-fixed-strategy. So the traces just reproduce the minimax lines (which is why they match the earlier traces). This doesn't validate B's fixed strategy against A deviations.

I need to properly test B's fixed strategy against A's best response to THAT strategy. Let me write a proper tester: A plays optimally against B's fixed strategy (A does minimax assuming B follows fixed strategy).

Let me write that.
The strategy fails (returns None) in some case, causing ERROR. Let me handle the ERROR and report where B's strategy is illegal. Let me also make bstrat return a fallback so I can see if the strategy itself is sometimes illegal.

Let me debug: find where bstrat returns None.
Need to handle STRAT_FAIL in avalue's comparison. Let me fix: if any child is STRAT_FAIL, propagate. Let me just treat STRAT_FAIL specially.
So strategy v1 (B first plays 1 or n, then x-1 or x+1) FAILS (becomes illegal) when A's first move is ≥ 6 (for odd n). The "non_loss_for_B" is empty, meaning whenever the strategy is legal, A loses. But the strategy becomes illegal for A first moves in the upper half.

The issue: when A picks a large first move (e.g., a=7 in n=9), B plays 1. Then A plays 2 (small), B plays 3 (x+1 since x-1=1 taken). Then A plays 4, B plays 5. A plays 6, B plays 7? But 7 is A's first move (taken). So B can't play 7. x-1=5 (taken by B), x+1=7 (taken by A). Both unavailable. Strategy fails.

So the strategy needs refinement. The problem is when A's first move is in the upper half, B should mirror differently. By symmetry, if A picks a in upper half, B should pick n (the far end) and play x+1 (push A downward). 

So the strategy should be symmetric: B picks the endpoint FAR from A's first move, then pushes A away.

Let me reconsider. For A's first move a:
- If a ≤ (n+1)/2 (lower half including center), B picks n, then plays x-1 (push A down/left? no, x-1 is below x). Wait, in the n=9, A=1 case, B picks 9 (n), then A goes 3,5,7 (upward), B plays 2,4,6 (x-1). So B pushes... A goes up, B takes the number just below each A move. The trap is A reaches n-2 and B takes n-3, leaving n-1 blocked by A's n-2.

Hmm wait, but B picked n (the top). A goes up toward n. A can't reach n (taken). A reaches n-2 (since n-1 is adjacent to... no, n-1 is adjacent to n which B has, but that's B's, doesn't affect A). A can pick n-1? A's set has n-2, so n-1 adjacent, forbidden. So A stops at n-2. Then remaining n-1, blocked. 

For A's first move in upper half, by symmetry B picks 1, A goes downward 2,4,...wait no. Let me think symmetrically: reflect the board (i → n+1-i). If A picks a in upper half, reflect: A' picks n+1-a in lower half. B's strategy on reflected board: pick n (=1 in original), play x-1 (= (n+1-x)+1 -1... hmm let me just think directly.

Symmetric strategy: B picks the endpoint on the opposite side from A's first move. If A picks a ≤ center, B picks n (opposite, far). If A picks a > center, B picks 1 (opposite, far). Then B pushes A toward the far end (where B's endpoint is), playing the number just behind A (between A and A's start).

Wait, in A=1 (lower), B=n (upper, far). A moves upward (3,5,7). B plays x-1 (just below A, i.e., between A's current and A's start). A is pushed up toward n.

In A=n (upper), by symmetry B=1 (lower, far). A moves downward. B plays x+1 (just above A). 

In A=middle-ish, say A=5 in n=9 (center). B picks... center is (n+1)/2=5. A picked center. B picks 1 (per traces). Then A moves... trace shows A=5,B=1,A=2,B=3,A=7,B=6,A=9,B=8. Hmm A went 5, then 2 (down), then 7,9 (up). Mixed. B played 1 (first), then 3 (x+1, since A=2, x-1=1 taken), then 6 (x-1, A=7), then 8 (x-1, A=9). So B switches between x-1 and x+1.

This is getting complicated. The strategy "x-1 or x+1 (whichever legal)" with B's first move = endpoint far from A. Let me redefine:

B's strategy v2:
- First move: if A's first move a ≤ (n+1)/2, B picks n; else B picks 1. (Pick the far endpoint.)
  - But traces showed for odd n, A=1→B=n, A=2..n→B=1. That's NOT "far endpoint" for A=2 (a=2 ≤ center=5, far endpoint=n=9, but B picked 1!). 

Contradiction. Let me re-examine. n=9, A=2: B picked 1, not 9. But 2 is in lower half, far endpoint is 9. Yet B picked 1 (near). Hmm.

So my "far endpoint" theory is wrong. Let me reconsider. B picks 1 if available, else n. That's "near-left endpoint if available." For A=1, 1 taken, so B=n. For A=anything else, B=1.

Then the push direction: B plays x-1 or x+1. For A=2,B=1: A goes 4,6,8 (up), B plays 3,5,7 (x-1). So A pushed up, B takes just below. Trap: A reaches 8 (=n-1), B takes 7, remaining 9 (=n), but 9 adjacent to A's 8 → blocked. Wait n=9, A=2: A={2,4,6,8}, B={1,3,5,7}, remaining {9}. A's f from {2,4,6,8}: {1,3,5,7,9}. 9 blocked. Stuck. Yes.

So for A=2, B=1 (near left), A pushed rightward to n-1=8, B takes just-below, A stuck at 9 (=n) blocked by 8.

For A=1, B=9 (far right, since 1 taken), A pushed rightward (3,5,7), B takes just-below (2,4,6), A stuck at 8 (=n-1) blocked by 7.

So in both cases A is pushed rightward (toward n) and stuck near n. The difference is whether B occupies n or 1 first.

For A in upper half, e.g., A=7 in n=9: B=1. Then A pushed... trace: A=7,B=1,A=2,B=3,A=4,B=5,A=9,B=8? Wait trace was A=7,B=1,A=2,B=3,A=4,B=5,A=9,B=8,STUCK A. Let me recompute. A={7,2,4,9}, B={1,3,5,8}. Remaining {6}. A's f from {7,2,4,9}: {1,3,5,6,8,10}→ in range {1,3,5,6,8}. 6 blocked. Stuck. 

Hmm so A went 7, then 2,4 (down-left), then 9 (up). B played 1, then 3,5 (x+1 for A=2,4), then 8 (x-1 for A=9). Mixed directions. The trap: remaining 6, blocked by A's 7.

This is genuinely complex. The strategy isn't a simple "push one direction." 

Given the complexity, maybe I should abandon trying to find a clean closed-form strategy and instead think about the proof differently.

Let me reconsider. This is a competition problem; the official solution likely has a clean structure. Let me think about the parity argument as the core.

**Core Parity Argument**: 
- A draw ⟺ final position is the parity partition (A=odds, B=evens or swap).
- This is the unique 2-coloring of the path.

Now, think about it from B's perspective. B wants to prevent the draw AND make A the one stuck.

Here's a cleaner idea based on parity:

Consider the parities. A moves on turns 1,3,5,... (odd turns). For a draw, A must collect exactly one parity class. 

Key: A's first move determines A's "target parity" for a draw. If A picks an odd number, then for a draw A must collect ALL odds (and B all evens). If A picks even, A must collect all evens.

Now B's strategy: B will "steal" one number of A's target parity, breaking the draw. But B must also ensure A (not B) gets stuck.

Hmm, but stealing one parity number doesn't directly make A stuck.

Let me think about a cleaner invariant. 

Actually, let me reconsider the problem from the perspective of "the game is equivalent to both players building independent sets, draw = perfect 2-coloring."

Let me think about B's strategy as: B always plays a number of the SAME parity as A's last move, adjacent to it. Wait, adjacent numbers have opposite parity. So B can't play same parity adjacent. 

B plays opposite parity (adjacent to A's move). B's set = {neighbors of A's moves}. For B's set to be independent: B's numbers are a_i ± 1. Two such, a_i+1 and a_j+1, adjacent iff a_i,a_j adjacent (no). a_i+1 and a_j-1 adjacent iff a_i+1=a_j-1±1 → a_i = a_j-2 or a_i=a_j. a_i=a_j-2: then a_i,a_j differ by 2, both in A's set (independent, allowed). Then a_i+1 = a_j-1, so B would pick the same number twice — but actually B picks a_i+1 after A's move a_i, and a_j-1 after A's move a_j. If a_i+1 = a_j-1, that's the same number; B can't pick it twice (already taken). So B's strategy must avoid this conflict.

This is the issue. The "x-1" strategy avoids it by always picking the same side. But then B's set might not be independent if... we showed x-1 keeps independence (since A independent → x_i-1 independent). And x-1 always available (shown). The only issue was x-1 adjacent to B's FIRST move (the endpoint).

So the clean strategy: B picks an endpoint e (1 or n), then plays x-1 (if e=n) or x+1 (if e=1) — always the side toward e. Wait:
- If B picks e=n, B plays x-1 (toward... x-1 is away from n if x<n). Hmm. Let me reconsider. B picks n. Then plays x-1. B's set = {n, x_2-1, x_3-1,...}. Is x_i-1 adjacent to n? Only if x_i-1 = n-1, i.e., x_i = n. But n taken by B, A can't pick n. So no. Good, B's set independent. And x_i-1 available (shown). So strategy "B picks n, then x-1" is ALWAYS legal (for any n, any A moves)!

Wait, is that right? Let me re-examine the availability of x_i - 1. x_i - 1 could be 0 (if x_i = 1). If A picks 1 as a later move, x_i - 1 = 0, invalid. When would A pick 1? Only if 1 is available and not adjacent to A's set. If B picked n (first), 1 is available (unless A's first move was 1). If A's first move was 1, then 1 taken, A can't pick it again. If A's first move ≠ 1, then 1 is available, and A might pick 1 later. Then B wants x-1 = 0, invalid.

So the strategy "B picks n, then x-1" fails if A ever picks 1 (as a non-first move). When does A pick 1? A picks 1 if 1 available (A's first ≠ 1, and B didn't take 1 — B took n, so 1 available) and 1 not adjacent to A's set (A has no 2). 

So if A's first move is, say, 5 (n=9), B picks 9. Then 1 is available. A could pick 1 later (if A has no 2). A's first move 5, A forbidden {4,6}. 1 is available and not forbidden. A could pick 1 as second move! Then B's x-1 = 0, invalid.

So "B picks n, then x-1" fails when A's first move ≠ 1 and A later picks 1.

Hmm. So the strategy needs B to also block 1, OR B picks 1 first (then plays x+1).

Let me reconsider: B picks 1 (if available), then plays x+1. B's set = {1, x_2+1, x_3+1,...}. x_i+1 adjacent to 1? Only if x_i+1=2, i.e., x_i=1. But if B picked 1, then 1 taken, A can't pick 1. So x_i≠1, x_i+1≠2. Good. x_i+1 available? x_i+1 not in A's set (A has x_i, independent, so no x_i+1). Not in B's set: x_i+1 = x_j+1 → x_i=x_j no. x_i+1 = 1 → x_i=0 no. So available. x_i+1 could be n+1 (if x_i = n). If A picks n as later move, x_i+1 = n+1 invalid. When does A pick n? If n available (B took 1, so n available unless A's first = n) and not adjacent to A's set (A has no n-1). If A's first move ≠ n, A might pick n later. Then x+1 = n+1 invalid.

So "B picks 1, then x+1" fails when A's first move ≠ n and A later picks n.

So: 
- "B picks n, then x-1" fails if A picks 1 later (possible when A's first ≠ 1).
- "B picks 1, then x+1" fails if A picks n later (possible when A's first ≠ n).

Combine: If A's first move = 1, use "B picks n, then x-1" (A can't pick 1 again, and A can't pick n (B has it), so x-1 always valid? x_i = 1 impossible (taken), x_i = n impossible (taken by B). So x_i - 1 ∈ [1, n-1] always valid. And x_i-1 ≠ n (since x_i ≠ n+1). And x_i-1 not adjacent to n (shown). So strategy legal!). 

If A's first move = n, use "B picks 1, then x+1" (symmetric). Legal.

If A's first move a is interior (1 < a < n): both strategies have issues. B picks 1, then x+1: fails if A picks n later. B picks n, then x-1: fails if A picks 1 later. 

Hmm. But maybe B can pick 1 AND the strategy handles A picking n? Let me think: B picks 1, plays x+1. If A picks n (later move), x+1 = n+1 invalid. But wait, if A picks n, then n is taken by A. Before that, was n available? B has 1, A has a (interior) and now n. B's response to A=n would be x+1=n+1, invalid. So B needs a different response when A picks n.

Alternatively: B picks 1, and plays x+1 EXCEPT when A picks n-1 (then x+1 = n, which is fine, B takes n). Wait if A picks n-1, B plays x+1 = n. That's fine (n available, not adjacent to B's set? B has 1 and previous x_j+1. n adjacent to n-1 (A's) — doesn't matter. n adjacent to B's set? B has 1 (far) and x_j+1. n adjacent to x_j+1 iff x_j+1 = n-1, i.e., x_j = n-2. So if A previously picked n-2, B took n-1, then A picks n-1? No, n-1 taken by B. Conflict... hmm.

This is getting complicated. Let me reconsider.

Actually, the cleanest: B picks 1, then plays x+1. This works as long as A never picks n. Can B prevent A from picking n? A picks n only if n available and n not adjacent to A's set (A has no n-1). 

If B's strategy is "pick 1, then x+1", B takes 1, then takes x_2+1, x_3+1, .... Does B ever take n? B takes x_i+1 = n when x_i = n-1. So if A picks n-1, B takes n. Then n is taken by B, A can't pick n. Good. But if A never picks n-1, then n stays available, and A might pick n.

When would A pick n? A picks n if available and A has no n-1. If A avoids n-1 (to keep n available for itself), A could pick n. Then B's x+1 = n+1 invalid.

So B's strategy "pick 1, then x+1" fails if A picks n without first picking n-1.

Hmm. So A can deviate by picking n directly. Let me check: does A picking n actually help A escape? Let me test the strategy "B picks 1 (or n if 1 taken), then x+1 (or x-1 if n taken)" against optimal A.

Actually, let me reconsider. Let me define strategy v2:
- If A's first move a = 1: B picks n, then plays x-1.
- If A's first move a = n: B picks 1, then plays x+1.
- If 1 < a < n: B picks 1, then plays x+1; BUT if A ever picks n, switch to... hmm.

This is getting messy. Let me just test a cleaner combined strategy and see if it works:

Strategy v2: B picks 1 if available else n. Then B plays x-1 if B's first was n, else x+1. I.e., B always pushes toward the side OPPOSITE its endpoint. If B has endpoint n, push A left (x-1). If B has endpoint 1, push A right (x+1).

Wait, that doesn't match. Let me re-examine n=9, A=1: B picks n=9 (since 1 taken). Then plays x-1. A goes 3,5,7 (rightward!), B plays 2,4,6. So A moves rightward (toward n), B takes just-below. But B's endpoint is n (right). A is pushed toward n (right). B plays x-1 (below A, left of A). Hmm, so B takes the number just LEFT of A's move. A moves right, B fills in just left. 

n=9, A=2: B picks 1 (available). Then plays x+1. A goes 4,6,8 (rightward), B plays 3,5,7 (x+1, just right of A... no, x+1 = 5 for A=4, that's right of A). Wait A=4, B plays 5 (x+1). 5 is right of 4. Then A=6, B=7. A=8, B=9? But 9 = n. B plays x+1=9. Then remaining... A={2,4,6,8}, B={1,3,5,7,9}? Wait that's 5 B moves and 4 A moves, but they alternate. Let me recount: A=2(1),B=1(2),A=4(3),B=3(4)? 

Hold on. n=9, A=2, B=1. Then A's turn. A=4. B's turn, plays x+1 = 5? But trace showed B=3 (x-1) for A=4! Let me recheck the trace: "A first=2: [('A', 2), ('B', 1), ('A', 4), ('B', 3), ('A', 6), ('B', 5), ('A', 8), ('B', 7), ('STUCK', 'A')]". So B plays 3,5,7 = x-1 (4-1=3, 6-1=5, 8-1=7). So B plays x-1, NOT x+1, even though B's endpoint is 1 (left). 

So B plays x-1 here, pushing... A goes right (4,6,8), B takes just-left (3,5,7). So B takes x-1 (left of A). A moves right toward n=9. B's endpoint 1 is on the left. So A is pushed RIGHT (away from B's endpoint 1, toward n). And B takes just-left of each A move.

And for A=1, B=9 (endpoint right), A moves right (3,5,7) toward B's endpoint 9, B takes just-left (2,4,6). Here A moves toward B's endpoint.

These are inconsistent in direction relative to B's endpoint. Let me reconsider: in BOTH cases, A moves rightward and B takes x-1 (just left of A). 

For A=1: B=9, A:3,5,7 rightward, B:2,4,6 = x-1.
For A=2: B=1, A:4,6,8 rightward, B:3,5,7 = x-1.

So actually in both, B plays x-1 and A moves right! The endpoint choice (9 vs 1) just depends on availability. So maybe the strategy is simply: B plays x-1 always (after first move), and first move = 1 if available else n. And A is pushed right.

But we saw this fails for A's first move in upper half (A picks small numbers later, going left). E.g., A=7 (n=9), B=1, then A=2 (leftward), B should play x-1=1 (taken) → fail. That's why strategy v1 failed for a≥6.

So when A goes left (picks small numbers), x-1 fails. B needs to play x+1 when A is on the left side moving... 

OK here's the real structure: B wants to push A toward an endpoint where B has placed its first piece, trapping A against it. The direction depends on where A goes.

Let me reconsider. Maybe the strategy is: B's first move at an endpoint. Then B always plays the number adjacent to A's last move on the side TOWARD B's endpoint. This pushes A away from B's endpoint... no.

Hmm, let me think about it as B "herding" A. 

Actually, let me reconsider the traces for upper-half A first moves:
n=9, A=7: B=1, A=2, B=3, A=4, B=5, A=9, B=8, stuck.
A went 7 → 2 (jump left) → 4 (right) → 9 (jump right). B: 1, 3, 5, 8.
B's moves: 1 (endpoint), 3 (=A2+1), 5 (=A4+1), 8 (=A9-1). 
So B plays x+1 when A is small (2,4), x-1 when A is large (9). I.e., B plays the adjacent number toward the center / away from the nearest endpoint? 

A=2: nearest endpoint 1 (taken by B). B plays 3 (away from 1, toward center). 
A=4: B plays 5 (away from 1, toward center/right).
A=9: nearest endpoint 9 itself (it's an endpoint). B plays 8 (away from 9's edge, toward center). 

Hmm, B plays the side toward the center? Let me check A=2,B=3: 3 is toward center from 2. A=4,B=5: toward center (center=5). A=9,B=8: toward center from 9. A=7 (first), B=1: 1 is... away from center. Hmm, that's the first move (endpoint), different rule.

Let me reconsider with the herding idea: B's first move = 1 (left endpoint). Then B herds A toward the RIGHT (toward n). B plays the adjacent-to-A number on the LEFT side (x-1) when A is moving right, but if A jumps to the left of B's "frontier," B plays x+1 to push it back right.

This is like B maintaining that A's numbers are all ≥ some frontier, and B fills in just below. But A can jump left...

This is genuinely a complex strategy. I don't think I'll find a super-clean closed form easily. 

Let me step back and reconsider the proof strategy. Given this is hard, maybe the intended solution uses a different, cleaner idea that I'm missing. Let me think about the problem from a higher level.

**Alternative approach: Think about the game as two interleaved games on parity classes.**

Hmm. Let me think about the following: color numbers by parity. A's set must be independent, so within A's set, no two consecutive — but A can have both parities (e.g., {1,4}). 

Let me think about the "gap" / interval structure.

**Another idea**: Let me think about when A is stuck. A is stuck iff A's set dominates all remaining numbers. 

Let me think about a potential function: the number of "available non-forbidden for A" minus something.

This is really a hard combinatorial game. Let me reconsider whether the answer might be cleaner than {1,2,4,6} and maybe I should reconsider the problem.

Actually, wait. Let me reconsider the problem statement once more. "determine the outcome." Maybe the expected answer is just "B wins for n ≥ 3 except n=4,6; draw for n=1,2,4,6." And the proof is casework-heavy. Competition problems can have such answers (e.g., IMO 2017 C6 about a game had a mod-based answer).

Let me just go with constructing a proof that:
1. States the parity characterization (draw ⟺ parity partition).
2. Handles small cases n=1,...,6 directly.
3. For n ≥ 7, gives B's winning strategy.

For part 3, I need a working strategy. Let me find one that I can prove works, even if not the minimax-optimal one. Let me search for a clean strategy by testing candidates programmatically against optimal A.

Let me test: B's strategy = "pick 1 if avail else n; then play x-1 if legal else x+1 if legal else (any legal)." But we saw it fails (illegal) for upper-half A. The "else any legal" fallback — does it still win? Let me test with fallback to a specific rule.

Actually, the issue is the strategy becoming illegal (no x±1 available). Let me add a fallback and test if B still wins. But fallback "any legal" might not win. Let me test fallback = optimal (to see if there's always a winning move, just not x±1). Actually that's just minimax again.

Let me think about a better strategy. Let me reconsider the herding.

Let me reconsider: B's strategy should keep A's set confined to an interval and shrink it. 

Here's a cleaner idea based on the traces: B maintains the invariant that A's numbers are all within some interval [L, R] and B "controls" L-1 and R+1 (or the endpoints), herding A.

Hmm, let me look at the n=9, A=7 trace again: A={7,2,4,9}, B={1,3,5,8}. A's numbers span [2,9]. B has 1 (left of 2), 3,5,8. Not a clean interval herding.

Let me try yet another approach: maybe prove B wins for n≥7 by reducing to n=7 or n=8 via a strategy that "ignores" extra numbers.

**Reduction idea**: For n ≥ 7, B's strategy: respond to A within a 7-element window, treating the rest as "already resolved" in B's favor.

Hmm, but the rest interacts.

Let me think about a cleaner reduction. 

Actually, let me reconsider the parity argument for a WINNING (not just non-losing) strategy.

**Parity-based winning strategy for B**: 

Claim: For n ≥ 7, B can force A to be the one who cannot complete a parity class, AND get stuck.

Let me think about B's strategy: B always plays a number of opposite parity to A's last move, specifically adjacent. This "claims the neighbor." Over time, A's set is surrounded.

Hmm, I keep going in circles. Let me just try to find a clean provable strategy by testing several candidates programmatically. Let me test:

Strategy A: B picks 1 if avail else n. Then B plays x-1 if (x-1 legal) else x+1 if legal. If neither, B plays... let me test with fallback "smallest legal" and "largest legal" and see if either wins.

Actually, let me reconsider. The traces for upper-half A first moves show B playing x+1 when A is small. So maybe the rule is: B plays x-1 if x > (n+1)/2, else x+1. I.e., push A toward the center? No...

Let me look again:
n=9, A=7: B=1(first). A=2→B=3 (x+1, since 2 < center=5). A=4→B=5 (x+1, 4<5). A=9→B=8 (x-1, 9>5). 
n=9, A=5 (center): B=1. A=2→B=3 (x+1). A=7→B=6 (x-1, 7>5). A=9→B=8 (x-1).
n=9, A=6: B=1. A=2→B=3(x+1). A=4→B=5(x+1). A=8→B=7(x-1).

So the rule seems: B plays x+1 if x ≤ center-ish, x-1 if x > center. Specifically x+1 when x < (n+1)/2, x-1 when x > (n+1)/2. What about x = center? n=9, A=5(center) was first move. Later A picks... in A=5 trace, A picks 2,7,9. None is center. 

Hmm, let me reconsider: maybe the rule is "B plays the adjacent number on the side of the NEARER endpoint to x." Wait:
x=2: nearer endpoint 1 (taken by B). Other side: 3. B plays 3. ✓ (play away from nearer endpoint, since nearer is blocked)
x=4: nearer endpoint 1. Other side 5. B plays 5. ✓
x=9: nearer endpoint 9 (it's endpoint). Other side 8. B plays 8. ✓
x=7: nearer endpoint 9 (distance 2) vs 1 (distance 6). Nearer=9. Other side 6. B plays 6. ✓ (A=7,B=6 in A=5 trace)

So rule: B plays the adjacent number on the side AWAY from the nearer endpoint. Equivalently, B plays x-1 if x is in the right half (closer to n), x+1 if x in left half (closer to 1). The boundary is the center.

But wait, this is the same as "push A toward the center"? No: x=2 (left half), B plays 3 (right of 2, toward center). x=9 (right half/endpoint), B plays 8 (left of 9, toward center). x=7 (right half), B plays 6 (toward center). So YES: B plays the adjacent number toward the center! B pushes A toward the center.

Hmm, but that seems to trap A in the middle. Let me reconsider n=9,A=1: B=9. A=3 (left half, center=5). B plays toward center = x+1=4? But trace shows B=2 (x-1)! Contradiction.

Wait n=9, A=1: A=3, B=2. 3 is in left half (3<5). Toward center would be 4 (x+1). But B played 2 (x-1, away from center). So the rule "toward center" fails for A=1 case.

Ugh. The A=1 case: B=9 (right endpoint). A=3, B=2 (x-1, toward LEFT endpoint, away from center). So here B pushes A LEFT (toward 1)? But A is moving right (3,5,7). 

I'm confusing myself. Let me re-examine: in A=1 case, A moves 1,3,5,7 (rightward, toward n=9). B moves 9,2,4,6. B's non-first moves: 2,4,6 = x-1 (A=3→2, A=5→4, A=7→6). So B takes the number just LEFT of A's move. A moves right, B fills left-behind. The trap: A reaches 7, B takes 6, remaining 8 (right of 7, blocked by 7) and 9 (taken by B). A stuck.

In A=7 case, A moves 7,2,4,9. B moves 1,3,5,8. B's non-first: 3,5,8. A=2→B=3 (x+1, right of 2). A=4→B=5 (x+1). A=9→B=8 (x-1, left of 9). So B takes the number on the side... A=2 is left, B takes right (3). A=4 left-ish, B takes right (5). A=9 right endpoint, B takes left (8). 

So in A=7 case, B's first move is 1 (left endpoint). A jumps to 2 (near B's endpoint). B takes 3 (right of 2, pushing A right/away from endpoint 1). Then A=4, B=5 (push right). A=9, B=8 (A went to far right, B takes left of it). 

So the herding: B has endpoint 1. B pushes A rightward (away from 1) by taking the right-adjacent number. When A reaches the far right (9), B takes 8 (left-adjacent), and A is stuck because... remaining 6, blocked by A's 7. 

Hmm wait, A={7,2,4,9}, remaining {6}. 6 is between A's 4 (no, 4's neighbors 3,5) and A's 7 (neighbors 6,8). 6 is neighbor of 7. So 6 blocked by A's 7. Also 6 is neighbor of... B's 5 (doesn't matter). So 6 blocked. A stuck.

So the trap here: A's own 7 blocks 6, the last remaining number.

OK the strategies are genuinely intricate and depend on A's choices. I think finding a single clean closed-form strategy is hard. 

Let me reconsider the proof approach. Maybe I should:
- Prove the parity characterization.
- Prove draw for n=1,2,4,6 by explicit strategies (A can force draw).
- Prove B wins for n=3,5 explicitly.
- For n≥7, prove B wins by a strategy that I CAN prove, even if complex. 

For n≥7, let me consider a strategy based on B "mirroring with respect to the center" but handling the center, OR an inductive strategy.

**Inductive strategy**: Show that if B wins for n, then B wins for n+2 (adding two numbers, one at each end). And base cases n=7,8 (or n=7,8,9,10). 

How would the induction work? If B wins on [1,n], then on [1,n+2], B's strategy: ... A picks some number. If A picks within [1,n], B responds as in the n-game (treating n+1, n+2 as "extra"). But the extra numbers interact (A could pick n+1, n+2).

Hmm, induction is tricky because A can use the new numbers.

Let me think about a different induction: B's strategy on n+2 is to first "neutralize" the two new endpoints then play the n-strategy on the middle.

Actually, here's a cleaner idea. Let me think about B's strategy for n ≥ 7 as follows:

B's strategy: B picks 1 (if A didn't) or n (if A picked 1). Then B plays the "reflection" of A's move... no.

Let me try to just find ANY strategy that works for all n≥7 by testing, then prove it. Let me test the "herding toward far endpoint" strategy more carefully:

Strategy: B's first move = 1 if available, else n. Then B maintains a "frontier": B always plays the adjacent-to-A's-last-move number on the side toward B's endpoint... no I showed that's inconsistent.

Let me just brute-force search for a simple strategy of the form "B plays f(avail, aset, bset, lastA)" among simple rules, testing against optimal A for n=7..15. Let me test the strategy: "B plays x-1 if x-1 legal and (x-1 ≥ B's endpoint or ...)"... 

Actually, let me reconsider. Let me look at ALL the traces and find the common rule for B's non-first moves.

Let me collect B's non-first moves and see the rule relative to A's last move and B's first endpoint.

n=9:
A=1,B_first=9: (A=3,B=2),(A=5,B=4),(A=7,B=6) — all x-1.
A=2,B_first=1: (A=4,B=3),(A=6,B=5),(A=8,B=7) — all x-1.
A=3,B_first=1: (A=5,B=4),(A=7,B=6),(A=9,B=8) — all x-1.
A=4,B_first=1: (A=2,B=3),(A=6,B=5),(A=8,B=7) — x+1, x-1, x-1.
A=5,B_first=1: (A=2,B=3),(A=7,B=6),(A=9,B=8) — x+1, x-1, x-1.
A=6,B_first=1: (A=2,B=3),(A=4,B=5),(A=8,B=7) — x+1, x+1, x-1.
A=7,B_first=1: (A=2,B=3),(A=4,B=5),(A=9,B=8) — x+1, x+1, x-1.
A=8,B_first=1: (A=2,B=3),(A=4,B=5),(A=6,B=7) — x+1, x+1, x+1.
A=9,B_first=1: (A=2,B=3),(A=4,B=5),(A=6,B=7) — x+1, x+1, x+1.

So the pattern: B plays x-1 when x is "large" (right portion) and x+1 when x is "small" (left portion). The threshold seems to be around B's first move position or the center.

Specifically: B plays x+1 when x < B_first, and x-1 when x > B_first? Let me check:
A=4,B_first=1: A=2 (2>1, so x-1=1? but B played 3=x+1). No. 2 > B_first=1, rule says x-1=1, but B played 3. ✗.

Let me try: B plays x+1 when x ≤ some threshold T, x-1 when x > T.
A=4: A=2→x+1, A=6→x-1, A=8→x-1. So T between 2 and 6. 
A=5: A=2→x+1, A=7→x-1, A=9→x-1. T between 2 and 7.
A=6: A=2→x+1, A=4→x+1, A=8→x-1. T between 4 and 8.
A=7: A=2→x+1,A=4→x+1,A=9→x-1. T between 4 and 9.
A=8: A=2,4,6 all x+1. T ≥ 6.
A=9: A=2,4,6 all x+1. T ≥ 6.
A=1,B_first=9: A=3,5,7 all x-1. So T < 3 (all x > T). 
A=2,B_first=1: A=4,6,8 all x-1. T < 4.
A=3,B_first=1: A=5,7,9 all x-1. T < 5.

Hmm, the threshold varies. For A=1 (B_first=9), T<3. For A=8 (B_first=1), T≥6. So T depends on the game state, not fixed.

This really is a complex adaptive strategy. I don't think there's a simple closed-form.

Given the difficulty, let me reconsider the possibility that the intended solution is structured differently — perhaps using the Sprague-Grundy-like analysis or a clever invariant, OR the answer is actually simpler and I have a bug.

Wait, let me reconsider. Let me re-examine whether the answer might be "B wins for all n ≥ 3" and my n=4,6 results are due to a subtle bug. Let me re-verify n=4 and n=6 with a totally independent simple script.

n=4: I hand-verified draw. Let me re-verify n=6 is draw with extra care, and n=8 B wins, using an independent implementation.

Actually I already hand-verified n=6 draw (A picks 1 → B can't win, A can't win → draw; and A has no winning first move). And n=4 draw hand-verified. And n=3,5 B wins. So the pattern {1,2,4,6} draw is solid.

Hmm, let me reconsider — maybe the problem is from a specific olympiad and the answer is known to be this. Let me just search my memory: I believe this is **IMO 2018 Shortlist C4** or **IMO 2017 C6**. Actually, I recall a problem "A and B choose numbers, can't choose consecutive to own" — this might be from **IMO 2018 C5** (game). The answer... I genuinely don't remember the exact answer.

Let me just go with the computed answer and construct the best proof I can. For the n≥7 case, I'll give a strategy and prove it works. Let me find a strategy I can actually prove.

Let me reconsider a cleaner strategy: **B mirrors A across the center, and if A plays center (odd n), B plays 1 (or handles specially).** Let me test this reflection strategy for n=7,8,9 against optimal A.

Reflection: B plays n+1-x in response to A's x. For even n, no center issue. For odd n, if A plays center c=(n+1)/2, reflection is c itself (taken), so B needs a fallback.

Let me test: B plays n+1-x; if that's illegal/unavailable, B plays optimally (or some fallback). Actually let me test pure reflection (with fallback to optimal when reflection unavailable) and see if it wins or draws.

For even n, pure reflection → we saw n=4,6 draw, n=8... let me test. Earlier n=8 with reflection (A=1,B=8,A=3,B=6,A=5,B=4,A=7,B=2) → draw. So reflection gives draw for n=8, not win. So reflection is not B's winning strategy for even n≥8.

So for even n≥8, B must deviate from reflection to win. The traces confirm (n=8, A=1, B plays 5 not 6 at move 2).

OK. I think the cleanest path is to give a proof that's somewhat case-analytic but correct. Let me structure it as:

**Proof outline:**
1. **Parity Lemma**: Draw ⟺ final partition is {odds}/{evens}.
2. **Small cases**: n=1,2 draw (trivial); n=3 B wins; n=4 draw; n=5 B wins; n=6 draw. (Explicit strategies.)
3. **n ≥ 7, B wins**: Give B's strategy and prove it.

For part 3, let me find a provable strategy. Let me think about a strategy based on "B always responds adjacent to A's move, on a fixed side relative to A's first move."

Let me reconsider the successful traces and find the invariant. 

Let me reconsider the strategy: **B's first move is the endpoint nearest to A's first move's opposite... ** ugh.

New idea: Let me consider B's strategy as maintaining that A's set is contained in an interval, and B "eats" from one side.

Let me look at the n=9 traces and track the interval containing A's numbers and B's "wall":

A=1: A's set grows {1},{1,3},{1,3,5},{1,3,7}... interval [1,7]. B has 9 (right wall) and 2,4,6 (filling gaps below A). 
A=7: A's set {7},{7,2},{7,2,4},{7,2,4,9}. interval [2,9]. B has 1 (left wall), 3,5,8.

Hmm. In A=1 case, B's first move 9 is the RIGHT wall, and A is pushed right toward it, B fills in just-left. In A=7 case, B's first move 1 is the LEFT wall, A jumps around, B fills in.

Let me think about it as: B picks the endpoint on the side where A's first move is NOT, then herds A toward that endpoint. 

A=1: A's first move at left endpoint. B picks right endpoint (9). Herd A rightward (toward 9). 
A=7 (n=9): A's first move in right portion. B picks left endpoint (1). Herd A leftward (toward 1)? But A went 7→2 (left, yes), then 2→4 (right!), →9 (right). So not purely leftward.

Hmm, A doesn't cooperate. B herds but A can jump.

I think the real strategy is adaptive in a way that's hard to state simply. 

Let me take yet another step back. Given the time I'm spending, let me consider just presenting the answer with the parity lemma and computational verification for the strategy, giving B's strategy as an explicit algorithm (decision tree) that I verify works. But a proof should be human-checkable.

Actually, let me reconsider. Let me look for a strategy that's clean AND provable, even if not minimax-optimal, as long as it wins for n≥7. Let me test the following clean strategy:

**Strategy H (herding)**: B's first move: if A's first move a ≤ (n+1)/2, B plays n; else B plays 1. (B takes the endpoint on the opposite side.) Then B always plays the number adjacent to A's last move on the side TOWARD B's endpoint (i.e., if B's endpoint is n, B plays x+1; if B's endpoint is 1, B plays x-1). Wait that pushes A toward B's endpoint. Hmm, but then A gets squished against B's endpoint. Let me reconsider — actually B wants to push A AWAY from B's endpoint so A gets trapped against the OTHER endpoint (which is open)? No...

Let me just test several clean strategies programmatically and find one that wins for all n=7..15. Let me test:

H1: B_first = n if a ≤ center else 1. Then B plays x+1 if B_first=n else x-1. (Push A toward B's endpoint.) With fallback to x∓1 if preferred side illegal, else any legal.

H2: B_first = n if a ≤ center else 1. Then B plays x-1 if B_first=n else x+1. (Push A away from B's endpoint.)

Let me test both.
H1 and H2 both win for odd n (7,9,11,13: all A_loses). But for even n (8,10,12), they only draw for some A first moves. So H1/H2 work for ODD n ≥ 7 but not even n.

So for odd n ≥ 7, H1 (or H2) is a clean winning strategy:
- B_first = n if A's first a ≤ center else 1.
- Then push toward B's endpoint (H1) or away (H2).

Both work for odd n. Let me pick one and prove it. Let me use H2 (push away from B's endpoint) — wait both work, let me check which is cleaner to prove. Actually let me reconsider what they do.

H1: B_first = n if a ≤ center else 1. Push toward B's endpoint (if B_first=n, play x+1, pushing A right toward n; if B_first=1, play x-1, pushing A left toward 1).

H2: B_first = n if a ≤ center else 1. Push away from B's endpoint (if B_first=n, play x-1; if B_first=1, play x+1).

For odd n both win. Let me focus on proving one for odd n. Let me reconsider which is more natural.

Actually, let me reconsider H2 for odd n with A=1: B_first = n (since 1 ≤ center). Push away from n: play x-1. A=1, B=n. A=3, B=2 (x-1). A=5,B=4. A=7,B=6. This matches the minimax trace! Good.

For A=2 (n=9): B_first = 1 (since 2 ≤ center=5? yes 2≤5, so B_first=n=9??). Wait center=(9+1)/2=5. a=2 ≤ 5, so B_first = n = 9. But the minimax trace for A=2 had B_first=1! 

Hmm, so H2 with A=2 gives B_first=9, but minimax gave B_first=1. Let me check if H2 still wins. The test says n=9 all A_loses, so H2 wins even with B_first=9 for A=2. Let me see the line: A=2, B=9 (H2). Then push away from 9: play x-1. A's turn: A={2},f{1,3}. avail{1,3,4,5,6,7,8}. A picks something. A picks 4 (say). B plays x-1=3. A={2,4},f{1,3,5}. avail{1,5,6,7,8}. B={9,3},f{2,4,8}. A picks 6. B plays 5. A={2,4,6},f{1,3,5,7}. avail{1,7,8}. B={9,3,5},f{2,4,6,8}. A picks 8? 8 not in A's f{1,3,5,7}. A=8. A={2,4,6,8},f{1,3,5,7,9}. avail{1,7}. B plays x-1=7. B={9,3,5,7}. avail{1}. A f{1,3,5,7,9}→1 blocked. stuck. 

So H2 works for A=2 too (with B_first=9). Good. So H2 is a valid winning strategy for odd n≥7, even though B_first differs from minimax in some cases.

Now I need to PROVE H2 works for all odd n ≥ 7. Let me understand H2 and prove it.

H2 strategy (odd n ≥ 7):
- Let c = (n+1)/2 (center).
- B's first move: if A's first move a ≤ c, B plays n; if a > c, B plays 1.
  (B takes the endpoint on the same side as... a ≤ c means a in left half, B takes right endpoint n. a > c means a in right half, B takes left endpoint 1. So B takes the endpoint on the OPPOSITE side from a.)
- Subsequently: if B's endpoint is n (so A's first was ≤ c), B plays x-1 (where x = A's last move). If B's endpoint is 1, B plays x+1.
  (B plays the adjacent number on the side AWAY from B's endpoint, i.e., toward A's side.)
  Fallback: if the preferred side is illegal, play the other side; if both illegal, play any legal move.

Wait, but the fallback "other side / any legal" — does it ever trigger for odd n? The test shows no STRAT_FAIL and all A_loses, so the strategy (with fallback) wins. But for a clean proof, I'd prefer the preferred side always legal. Let me check if the preferred side (x-1 for B_first=n, or x+1 for B_first=1) is ALWAYS legal for odd n≥7.

From the test, H2 had fails=[] for odd n, meaning the strategy never hit STRAT_FAIL. But the fallback might have been used (preferred side illegal, other side legal). Let me check if the preferred side is always legal, or if fallback is needed.

Let me modify to track whether fallback is used.

Actually, for the proof, let me reconsider. Let me check: is the preferred-side move always legal for odd n ≥ 7?

Preferred: x-1 (if B_first=n) or x+1 (if B_first=1).

Case B_first=n (A's first a ≤ c): B plays x-1 for each A move x (after first). 
- x-1 available? x-1 not in A's set (A has x, independent). Not in B's set: B has {n, x_j-1 for j<i}. x-1 = x_j-1 → x=x_j no. x-1 = n → x=n+1 impossible. So available. 
- x-1 ≥ 1? x ≥ 2 needed. Could A pick x=1? A's first move a; if a=1, then 1 taken, A can't pick 1 again. If a > 1 (but a ≤ c), then 1 is available. Could A pick 1 later? A picks 1 if 1 available and 1 not adjacent to A's set (A has no 2). So A could pick 1 as a later move! Then x-1 = 0, invalid.

So if A's first move a is in {2,...,c} (so B_first=n), A might later pick 1, breaking x-1. Let me check: does A picking 1 actually happen / does the strategy handle it?

Let me test: n=9, A=2 (a=2 ≤ c=5, B_first=9). Could A pick 1 later? A={2}, f{1,3}. 1 is forbidden (adjacent to 2)! So A can't pick 1. Good. 

n=9, A=3 (a=3 ≤ 5, B_first=9). A={3},f{2,4}. 1 available, not forbidden. A could pick 1. Then x-1=0 invalid. Let me check if the strategy handles A=1 via fallback. Let me test this specific line.

Actually the test already covers all A optimal responses, and H2 won for n=9. So even if A picks 1, the fallback handles it. But for a clean proof, I need to handle this case explicitly.

Hmm. Let me check: n=9, A=3, B=9 (H2). A's turn, A={3},f{2,4}, avail{1,2,4,5,6,7,8}. A could pick 1 (available, not forbidden). If A picks 1: A={1,3},f{2,4}. B plays x-1=0 invalid → fallback. Preferred side x-1=0 invalid, other side x+1=2. 2 available? yes. 2 adjacent to B's set? B={9}, 2 not adjacent to 9. So B plays 2. B={9,2},f{1,3,8}. avail{4,5,6,7,8}. A={1,3},f{2,4}. A picks 5,6,7,or 8. ... continues. Does A still lose? The test says yes (n=9 A=3 → A_loses under H2). 

So the fallback (play x+1 when x-1 invalid) handles A picking 1. But this complicates the proof.

Let me reconsider. Maybe I can choose the strategy so the preferred side is ALWAYS legal. The issue is A picking the endpoint near A's side. 

Alternative: B_first = the endpoint on the SAME side as A's first move. I.e., if a ≤ c, B_first = 1; if a > c, B_first = n. Then push... let me reconsider. If B takes the endpoint on A's side, then A can't pick that endpoint later. Then push away from B's endpoint.

Let me define H3: B_first = 1 if a ≤ c else n (same side as A). Then play x+1 if B_first=1 (push right, away from 1) else x-1 (push left, away from n). 

Wait, if a ≤ c (left half), B_first=1 (left endpoint). A's first move a is in left half. A might want to pick 1 later — but B took 1, so A can't. Good. And A might pick n later (right endpoint, available). Then x+1 = n+1 invalid. So same problem on the other side.

Hmm. Unless B also blocks n. But B only gets one first move.

So no single-endpoint strategy avoids the "A picks the far endpoint" problem. The far endpoint remains available, and if A picks it, the push-direction strategy breaks.

But the fallback handles it. Let me just prove the strategy WITH fallback, handling the "A picks far endpoint" case as a special sub-case.

Actually, let me reconsider. Let me check: when A picks the far endpoint (the one B didn't take), does A actually escape or does B still win? The test shows B still wins (with fallback). Let me understand the fallback behavior in that case and prove it.

This is getting long. Let me reconsider the overall proof structure and whether there's a fundamentally cleaner approach for odd n.

**Cleaner approach for odd n via reflection:**

For odd n, reflection (B plays n+1-x) has the center problem. But maybe handle center: if A plays center c, B plays... Let me test reflection with center-handling.

Reflection strategy R: B plays n+1-x. If n+1-x is unavailable (A played center, or A played a number whose reflection was already taken), B plays... hmm.

Actually for odd n, the center c=(n+1)/2 is a fixed point. If A plays c, reflection c is taken (by A), B can't. So B needs a response. Let me test: B plays n+1-x normally; if that's unavailable/illegal, B plays 1 (or some fixed). Let me test reflection with fallback.

Actually, let me reconsider. For odd n, the minimax B_first for A=1 is n (=n+1-1, reflection!). For A=2, minimax B_first=1, but reflection of 2 is n-1=8 (n=9). So minimax doesn't use reflection for A=2. So reflection isn't the minimax strategy. But maybe reflection still wins? Let me test.

Let me test reflection (B plays n+1-x, fallback to optimal or 1 if unavailable) for odd n.

Hmm, but if reflection leads to draw (like even n), it won't win. Let me just test.

Actually, let me step back and think about the proof structure for odd n using H2, and handle the edge cases. Let me first check: for H2 with odd n, is the PREFERRED move always legal except when A picks the far endpoint? And when A picks the far endpoint, what's the situation?

Let me instrument H2 to report when fallback (non-preferred) is used.
H2 wins for all odd n from 7 to 21 (all A_loses), but fallback IS used in some lines. So the preferred move isn't always legal. I need to handle the fallback cases in the proof.

Let me figure out exactly when the fallback triggers. The fallback triggers when the preferred move (x-1 for B_first=n, or x+1 for B_first=1) is illegal. Preferred illegal when:
- x-1 < 1 (x=1), i.e., A picked 1 (only possible if B_first=n, meaning A's first a ≤ c and a≠1, so 1 was available and A picked it later).
- x-1 unavailable (taken): x-1 in B's set (only n or previous x_j-1; x-1=n impossible, x-1=x_j-1 impossible). x-1 in A's set: A has x, independent, so no x-1. So x-1 available unless x=1.
- x-1 adjacent to B's set: x-1 adjacent to n (x-1=n-1, x=n, but n taken by B, A can't pick n) — impossible. x-1 adjacent to x_j-1: iff x adjacent to x_j — no (A independent). So not adjacent.

So for B_first=n, preferred x-1 is illegal ONLY when x=1 (A picked 1). Similarly for B_first=1, preferred x+1 illegal only when x=n (A picked n).

So the fallback triggers exactly when A picks the "near" endpoint (the endpoint on A's own side, which B didn't take):
- B_first=n (A's first a ≤ c): fallback when A picks 1 (the left endpoint).
- B_first=1 (A's first a > c): fallback when A picks n (the right endpoint).

So the only complication: A picks the endpoint on A's side. Let me handle this.

When B_first=n and A picks 1 (as a later move): B's preferred x-1=0 invalid. Fallback: other side = x+1 = 2. Is 2 legal? 2 available? 2 not in A's set (A has 1, independent, no 2... wait A has 1 now, and A's set is independent so A doesn't have 2; but is 2 taken by B? B has n and x_j-1's. 2 = x_j-1 → x_j=3, so if A previously picked 3, B took 2. Then 2 unavailable.). Hmm, so 2 might be unavailable if A previously picked 3.

This is getting complicated. Let me think about the structure more carefully to find a clean proof.

Let me reconsider. Maybe instead of pushing "away from B's endpoint," I should push "toward B's endpoint" but with B's endpoint on the FAR side from A. Wait, that's H1. H1 also only won odd n. Let me reconsider H1's fallback structure. Actually both H1 and H2 have the same issue.

Let me think differently. Let me reconsider the actual minimax strategy structure for odd n and find the clean invariant.

Let me reconsider the minimax traces for odd n:
n=9:
A=1: B=9,3→2,5→4,7→6. (B: 9,2,4,6)
A=2: B=1,4→3,6→5,8→7. (B: 1,3,5,7)
A=3: B=1,5→4,7→6,9→8. (B: 1,4,6,8)
A=4: B=1,2→3,6→5,8→7. (B: 1,3,5,7)
A=5: B=1,2→3,7→6,9→8. (B: 1,3,6,8)
A=6: B=1,2→3,4→5,8→7. (B: 1,3,5,7)
A=7: B=1,2→3,4→5,9→8. (B: 1,3,5,8)
A=8: B=1,2→3,4→5,6→7. (B: 1,3,5,7)
A=9: B=1,2→3,4→5,6→7. (B: 1,3,5,7)

Observation: In ALL cases, B's first move is 1 (except A=1 where it's 9). And B's set ends up being {1 or 9, and then a mix}. 

Let me look at A's final set and B's final set:
A=1: A={1,3,5,7}, B={9,2,4,6}. Remaining {8}. 
A=2: A={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=3: A={3,5,7,9}, B={1,4,6,8}. Remaining {2}.
A=4: A={4,2,6,8}={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=5: A={5,2,7,9}={2,5,7,9}, B={1,3,6,8}. Remaining {4}.
A=6: A={6,2,4,8}={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=7: A={7,2,4,9}={2,4,7,9}, B={1,3,5,8}. Remaining {6}.
A=8: A={8,2,4,6}={2,4,6,8}, B={1,3,5,7}. Remaining {9}.
A=9: A={9,2,4,6}={2,4,6,9}, B={1,3,5,7}. Remaining {8}.

Hmm interesting. In many cases A ends up with {2,4,6,8} (all even except...) and B with {1,3,5,7}, remaining 9. That's the parity partition MINUS one number! A has evens 2,4,6,8, B has odds 1,3,5,7, remaining 9 (odd). For a draw, A would need all evens {2,4,6,8} and B all odds {1,3,5,7,9}. But B only has 4 odds, missing 9. And 9 is remaining but blocked (A's 8 blocks 9). So A can't take 9, and B already... wait it's A's turn and A is stuck. So the draw is broken because B didn't take 9 (the last odd), and A can't take it either (blocked by own 8). So 9 remains unclaimed → not a draw, and A can't move → A loses.

So the structure: B forces the game to ONE number short of the parity partition, where the last number is blocked by A's own piece. 

Specifically: A ends with all of one parity class except the game stops one short. The remaining number is of B's parity, blocked by A's adjacent number.

This is the key insight! B's strategy: force A to take all numbers of one parity (say all evens or all odds except boundary), while B takes the other parity, leaving exactly one number of B's parity that A can't take (blocked by A's neighbor) and it's A's turn.

Hmm, but in A=1 case: A={1,3,5,7} (odds except 9), B={9,2,4,6} (9 is odd! plus evens 2,4,6). Remaining 8 (even). So here A took odds {1,3,5,7} (missing 9 which B took!), B took 9 (odd) + evens {2,4,6}. Remaining 8 (even), blocked by A's 7. So B "stole" odd 9, breaking A's parity collection, and the remaining even 8 is blocked by A's 7.

So B's strategy: B steals one number of A's "natural" parity (the parity of A's first move), then fills in, leaving A blocked.

This is subtle. Let me think about the clean invariant.

A's first move a has parity p. For a draw, A would need all numbers of parity p. B's first move: B takes a number of parity p (the endpoint of parity p on the far side)! 
- A=1 (odd): B takes 9 (odd). B stole an odd. ✓
- A=2 (even): B takes 1 (odd)? No, 1 is odd, A's parity is even. B took 1 (odd), not A's parity. Hmm. 

Wait A=2, B=1. A's parity = even. B took 1 (odd). So B did NOT steal A's parity here. But A ended with {2,4,6,8} (all evens), B with {1,3,5,7} (all odds), remaining 9 (odd). So A got ALL evens, B got odds except 9. The remaining 9 (odd, B's parity) is blocked by A's 8. So here B did NOT steal A's parity; instead, A completed its parity class (evens), but B is one short on odds (missing 9), and 9 is blocked by A's 8. It's A's turn, A can't take 9 (9 is odd, but also 9 adjacent to A's 8 → blocked). So A stuck.

So in this case, A successfully collected all its parity (evens), but the game isn't a draw because B didn't collect all odds (9 remains). And A can't take 9 (blocked). So A is stuck.

So the trap: A collects all of parity p, B collects all of the other parity except one number (an endpoint), and that endpoint is blocked by A's adjacent number. A is stuck because the only remaining number is of the other parity and adjacent to A's piece.

So B's strategy ensures: A is forced to collect ALL numbers of parity p (A's first move's parity), while B collects the other parity except one endpoint, which remains and is blocked by A.

How does B force A to collect all of parity p? By B always taking the other parity. If B always plays opposite parity to A, then A is forced to take parity p numbers (since B takes the others). But A might take a number of the opposite parity too... 

Hmm wait. Let me reconsider. If B always takes numbers of parity opposite to A's first move, then B claims all numbers of that opposite parity that it can. A claims parity p numbers. But A could also claim opposite-parity numbers (if available and legal). 

Let me reconsider. The key mechanism: B plays adjacent to A's moves (x±1), which are of opposite parity. So B's numbers are all opposite parity to A's numbers. Since A's numbers are all parity p (if A only picks parity p), B's numbers are all parity 1-p. 

But does A only pick parity p? A could pick opposite parity. Let me check: in A=1 case, A picked 1,3,5,7 all odd (parity p=odd). In A=2 case, A picked 2,4,6,8 all even. In A=5 case, A picked 5,2,7,9 = {2,5,7,9}: 5,7,9 odd, 2 even. So A picked mixed parity! So A doesn't always stick to one parity.

Hmm. So the "A collects one parity" isn't universal. Let me re-examine A=5 (n=9): A={2,5,7,9}, B={1,3,6,8}, remaining {4}. 4 is even, blocked by A's 5? 5's neighbors 4,6. Yes 4 blocked by 5. Also 4 blocked by... A's set {2,5,7,9}: 2's nbrs 1,3; 5's nbrs 4,6; 7's nbrs 6,8; 9's nbrs 8. So 4 blocked by 5. 6 blocked by 5,7. 8 blocked by 7,9. So remaining {4}, blocked. A stuck.

So in this case remaining is 4 (even), A's set has 2 (even), 5,7,9 (odd). B's set {1,3,6,8}: 1,3 odd, 6,8 even. So both players have mixed parity. The remaining 4 is blocked by A's 5.

So the clean "parity partition minus one" structure only appears in some cases. The A=5 case is messier.

OK, I think a fully clean proof of the n≥7 case is genuinely difficult and the official solution likely uses a clever but non-trivial strategy. Given my time constraints, let me construct a proof that:
1. Proves the parity characterization (clean).
2. Handles n=1..6 by explicit analysis.
3. For n≥7, presents B's strategy (H2 with the endpoint-fallback) and proves it works via a careful invariant argument.

Actually, let me reconsider and try to find a cleaner strategy for odd n that avoids fallback. The fallback is only triggered when A picks the near endpoint. What if B's strategy PREEMPTIVELY blocks the near endpoint?

For B_first=n (A's first a ≤ c): the near endpoint is 1. A might pick 1 later. What if B, instead of always x-1, plays x-1 but if x would be 1... A can't be forced not to pick 1. 

Alternatively: B_first = n, and B's strategy: play x-1, BUT if A ever picks 1, then B switches to a "sub-game" strategy on the remaining. When A picks 1, A's set has 1 (and previous A numbers). B has n and (x_j - 1)'s. After A picks 1, the number 2 is... B should play 2? But 2 might be taken (if A previously picked 3, B took 2). 

Hmm. Let me think about when A picks 1 in the B_first=n case. A picks 1 only if 1 is available (B didn't take it — correct, B took n) and 1 not adjacent to A's set (A has no 2). A has no 2 means A never picked 2, and B never... B could have 2 (if A picked 3, B took 2). If B has 2, then 1 is adjacent to B's 2 — but that's B's, doesn't affect A. A can still pick 1 (1 not adjacent to A's set). Wait, but if B has 2, is 1 still available? 1 available iff not taken. B has 2, not 1. So 1 available. A can pick 1 if A has no 2 (A's set). 

So A picks 1 when A's set has no 2. In the B_first=n strategy, B plays x-1. If A picks 3, B takes 2. Then A's set has 3, B has 2. A can't pick 2 (taken). Can A pick 1? 1 available, 1 adjacent to A's 3? No (1,3 not adjacent). 1 adjacent to A's other numbers? Depends. If A only has 3 (and first move), 1 not adjacent. So A could pick 1. Then B's x-1 = 0, fallback to x+1 = 2, but 2 taken by B! So fallback other side also unavailable. Then fallback to "any legal." 

So the strategy gets complicated. Let me just test: does the "any legal" fallback still win? The test said yes (H2 wins all odd n). But "any legal" is not a clean rule to prove.

Let me refine the fallback. When A picks 1 (near endpoint) in B_first=n case: B should play... let me look at what minimax does. Let me find a specific line where A picks 1 and see B's response.

Let me construct: n=9, A=3 (a=3 ≤ c=5, so B_first=9 under H2). A=3, B=9. Now A picks 1 (deviation). A={1,3}, f{2,4}. B's turn. What does minimax B play?

Let me compute.
So when A picks 1 (near endpoint) after B=9, B plays 2 (the other side, x+1=2). And it works: A={1,3}, B={9,2}, then A=5,B=4,A=7,B=6, A stuck (remaining 8, blocked by 7).

So the fallback "play x+1 when x-1 invalid" works here (2 = x+1 for x=1). And 2 was available (A hadn't picked 3 yet... wait A had picked 3 first! A={3,1}. So A has 3. B plays 2. 2 adjacent to A's 3? Yes but that's A's, doesn't matter for B. 2 adjacent to B's set {9}? No. So B plays 2 legally. Good.

But what if A picked 3 first (so B would have taken 2 in normal play)? In this line, A=3 was the FIRST move, B=9 (B didn't take 2). Then A=1, B=2. So B takes 2 now. Fine.

But consider: A=3, B=9, A=5, B=4, A=1. Now A={1,3,5}, B={9,4}. B wants to respond to A=1. x-1=0 invalid. x+1=2. 2 available? A has 1,3,5; B has 9,4. 2 not taken. 2 adjacent to B's set {9,4}? 2 adjacent to 4? No (2,4 not adjacent, diff 2). 2 adjacent to 9? No. So B plays 2. Then trace: A=7,B=6, stuck. Good. (Matches the second exploration: B=2, A=7, B=6, stuck.)

So the fallback "x+1 when x-1 invalid" works. But is x+1 always legal when x-1 is invalid (x=1)? x+1=2. 2 available? 2 taken iff A or B has 2. A has 2? A has 1 (just picked), A's set independent so A doesn't have 2. B has 2? B has {n, x_j-1 for previous}. B has 2 iff some x_j - 1 = 2, i.e., A previously picked 3. So if A previously picked 3, B has 2, and now A picks 1, B can't play 2 (taken). Then fallback to "any legal."

When would A have picked 3 before picking 1? A=3 (first), B=9, then A picks 1 (not 3 again). Here A's first is 3, B=9. A didn't pick 3 "before" in a way that B took 2 — B took 9, not 2. So B doesn't have 2. So B can play 2. 

But what if: A=3 (first), B=9, A=5, B=4, A=7, B=6, A=1. Now A={1,3,5,7}, B={9,4,6}. B respond to A=1: x+1=2. 2 taken? B has {9,4,6}, no 2. A has {1,3,5,7}, no 2. So 2 available. B plays 2. Then remaining {8}. A's f from {1,3,5,7}: {2,4,6,8}. 8 blocked. A stuck. 

But wait, in this line, after A=7,B=6, it's A's turn with A={3,5,7}, B={9,4,6}, avail{1,2,8}. A's f{2,4,6,8}. A can pick 1 (not in f). A=1. Then B=2. A stuck. But could A have picked 8 instead of 1? A=8: 8 in A's f{2,4,6,8}? 8 is in f (adjacent to 7). So A can't pick 8. A can only pick 1. Forced. Then B=2, A stuck. Good.

So actually in this line A is forced to pick 1 (only legal move), and B plays 2, A stuck. The fallback works cleanly.

Now the question: is there a case where A picks 1 and B's x+1=2 is ALSO unavailable (B already has 2)? B has 2 only if A previously picked 3 (B took 2 = 3-1). But if A picked 3 and B took 2, then for A to later pick 1: A has 3 (so 1 not adjacent to 3, ok), 1 available (B has 2, not 1), A has no 2 (A's set). So A can pick 1. Then B wants 2, but 2 taken by B. Fallback to "any legal."

Let me construct: n=9, A=3 (first), B=9, A=5, B=4, A=1? Wait B took 4 (=5-1), not 2. B takes 2 only if A picks 3 as a NON-first move (B_first=n case, B plays x-1=2 for x=3). But A=3 as first move → B plays 9 (first move), not 2. So B takes 2 only when A picks 3 as a later move (after B's first). 

When does A pick 3 as a later move in B_first=n case? B_first=n means A's first a ≤ c. If a=1: A=1, B=9. Then A picks 3 (later). B plays 2 (=3-1). So B has 2. Then could A later pick 1? No, 1 is A's first move (taken). So A can't pick 1. So no conflict.

If a=2: A=2, B=9 (H2, since 2 ≤ c). A={2}, f{1,3}. A can't pick 1 or 3 (forbidden). So A never picks 3, B never takes 2 via x-1. So B never has 2. So if A later picks 1... A can't (1 forbidden by A's 2). So A never picks 1. No conflict.

If a=3: A=3, B=9. A picks 3 first. B doesn't take 2 (B took 9). Later A picks 5, B takes 4. A picks 7, B takes 6. A picks 1 (forced, as shown). B takes 2. B didn't have 2 before. Good.

If a=4: A=4, B=9 (H2, 4 ≤ 5). A={4},f{3,5}. A can pick 1,2,6,7,8. If A picks 2: B plays x-1=1. B takes 1! Then A can't pick 1 later. Good, no conflict (A picks 1 is now impossible). If A picks 6: B plays 5. etc. If A picks 1: B plays x-1=0 invalid → fallback x+1=2. 2 available? B has {9}, no 2. A has {4,1}, no 2. So B plays 2. Then A={1,4},f{2,3,5}. B={9,2},f{1,3,8}. avail{3,5,6,7,8}. A picks 6 or 7. ... Let me trust it works.

So the conflict (B already has 2 when A picks 1) requires A to have picked 3 as a later move AND B took 2, AND then A picks 1. But if A picked 3 (later), A has 3, and for A to pick 1: 1 not adjacent to 3 (ok), 1 available. But also A has 3 means A's set includes 3; does A have 2? No (independent). So A can pick 1. And B has 2 (took it when A picked 3). So B can't play 2. Conflict!

When does this happen? B_first=n (a ≤ c). A picks 3 as a LATER move (not first). So a ≠ 3, a ≤ c, a ∈ {1,2,4,5} (for n=9, c=5). 
- a=1: A=1 first. A can't pick 1 again. A picks 3 later? A={1},f{2}. 3 available, not forbidden. A could pick 3. B plays 2. B has 2. Then A picks 1? Can't (taken). No conflict.
- a=2: A=2, f{1,3}. A can't pick 3. So A never picks 3. No conflict.
- a=4: A=4, f{3,5}. A can't pick 3. No conflict.
- a=5 (center): A=5, f{4,6}. A can pick 3 (available, not forbidden). A=3 (later). B plays 2. B has 2. Then A picks 1? A={5,3}, f{2,4,6}. 1 available, not in f. A picks 1. B wants 2 (taken by B). Conflict! 

So n=9, A=5, B=9 (H2: 5 ≤ 5, B_first=9). A=3 (later), B=2. A=1, B wants 2 (taken). Fallback. Let me check this line with the strategy.

Actually wait, the H2 strategy for A=5 (n=9): B_first = 9 (since 5 ≤ c=5). But the minimax B_first for A=5 was 1, not 9! So H2 deviates from minimax here. Does H2 still win for A=5? The test said n=9 all A_loses under H2, so yes. But the fallback must handle the conflict. Let me trace H2 for n=9, A=5.

Let me trace H2 explicitly for n=9, A=5, with A playing optimally against H2.
A's avalue returns bestk=None when no legal moves (terminal). But in the loop, if A has legal moves, bestk should be set. The issue: when A has legal moves but all lead to... bestk should be set. Let me check: avalue initializes bestk=None, sets it when a better move found. If ALL moves give 'A_loses' (order 0), and best starts at 'A_loses' (0), then `order[r]>order[best]` is `0>0` False, so bestk never set! Bug. Let me fix: use >= or set bestk on first.

Let me fix to always pick a move (prefer the first that achieves best).
Now I see the H2 strategy clearly for odd n. Let me analyze the pattern.

For odd n, H2 strategy:
- B_first = n if A's first a ≤ c else 1 (c = (n+1)/2).
- Then B plays x-1 (if B_first=n) or x+1 (if B_first=1), with fallback to the other side.

Looking at the traces, the fallback (other side) is used in a few cases:
- n=9, A=3: B=9, A=1 (A picks near endpoint 1!), B=2 (fallback: x+1=2 since x-1=0 invalid). Then A=3? No A already has 3. A=5,B=4,A=7,B=6. 
  Wait A=3 first, then A=1. A={3,1}. B=9, then B=2. Then A=5,B=4,A=7,B=6. A={1,3,5,7}, remaining 8, blocked. 
- n=9, A=4: B=9, A=1, B=2 (fallback). A=6,B=5,A=8,B=7. A={1,4,6,8}? wait A=4 first, then A=1, A=6, A=8. A={1,4,6,8}, B={9,2,5,7}, remaining {3}. A's f from {1,4,6,8}: {2,3,5,7,9}. 3 blocked. stuck. 
- n=9, A=5: B=9, A=1, B=2 (fallback). A=3, B=4 (fallback? x-1=2, but 2 taken by B; so other side x+1=4). A=7,B=6. A={1,3,5,7}? wait A=5 first, A=1, A=3, A=7. A={1,3,5,7}, B={9,2,4,6}, remaining 8, blocked. 
  Here B=4 is fallback (x-1=2 taken, x+1=4). 

So the fallback to "other side" is used, and it works. Now I need to prove this strategy works for all odd n ≥ 7.

This is still complex but let me try to find the invariant. Let me look at the structure of the traces:

For B_first=n case (a ≤ c): 
- A's moves: a (first), then a sequence. B: n, then x-1's (with fallbacks).
- In many traces, A ends up with {1, 3, 5, ..., n-2} (all odd numbers from 1 to n-2) and B with {n, 2, 4, ..., n-1} (n plus all evens), remaining n-1? No wait.

Let me look at n=11:
A=1: A={1,3,5,7,9}, B={11,2,4,6,8}, remaining {10}. 10 blocked by 9. 
A=2: A={2,4,6,8,10}, B={11,3,5,7,9}, remaining {1}. 1 blocked by 2. 
A=3: A={3,1,5,7,9}={1,3,5,7,9}, B={11,2,4,6,8}, remaining {10}. 
A=4: A={4,1,6,8,10}={1,4,6,8,10}, B={11,2,5,7,9}, remaining {3}. 3 blocked by 4. 
A=5: A={5,1,3,7,9}={1,3,5,7,9}, B={11,2,4,6,8}, remaining {10}. 
A=6: A={6,1,3,8,10}={1,3,6,8,10}, B={11,2,4,7,9}, remaining {5}. 5 blocked by 6. 

So in all B_first=n cases (a ≤ c=6 for n=11), A ends with a set, B ends with a set, and ONE number remains, blocked by A's adjacent number.

Pattern for B_first=n: A's final set = {1,3,5,...,n-2} (all odds from 1 to n-2) OR a set containing 1 and some structure. B's final set = {n} ∪ {2,4,...,n-1} (n plus all evens) OR similar. Remaining = n-1 (even, blocked by A's n-2) in the clean cases.

Wait, A=1: A={1,3,5,7,9}, B={11,2,4,6,8}, remaining 10. 10 = n-1. Blocked by A's 9 = n-2. 
A=2: A={2,4,6,8,10}, B={11,3,5,7,9}, remaining 1. 1 blocked by A's 2. Here remaining is 1 (the near endpoint), blocked by A's 2.
A=3: same as A=1 (A={1,3,5,7,9}), remaining 10.
A=4: A={1,4,6,8,10}, B={11,2,5,7,9}, remaining 3. 3 blocked by A's 4.
A=5: A={1,3,5,7,9}, remaining 10.
A=6: A={1,3,6,8,10}, B={11,2,4,7,9}, remaining 5. 5 blocked by A's 6.

So the remaining number is always blocked by an A number adjacent to it. And it's always A's turn when stuck. Total moves: 5 A + 5 B = 10, remaining 1. n=11, 10 moves, 1 remaining. A's 5th move is the last A move, then B's 5th, then A stuck (6th A move attempted). Wait: moves 1(A),2(B),...,10(B), then A's 6th turn, stuck. So A made 5 moves, B made 5 moves, 11-10=1 remaining. A stuck.

So the strategy ensures: after 5 rounds (A and B each move 5 times), exactly 1 number remains, and it's blocked by A's set, and it's A's turn. 

The invariant: B's strategy ensures A is forced to "fill in" a contiguous-ish block such that one number remains blocked.

This is still complex. Let me try to find the precise invariant for the B_first=n case.

Let me define the B_first=n case (A's first a ≤ c). B plays n, then x-1 (fallback x+1).

Let me think about it as: B is building the set {n, 2, 4, 6, ..., n-1} (n plus evens) and A is forced into {1, 3, 5, ..., n-2} (odds except n), with n-1 remaining blocked by n-2.

But A doesn't always cooperate (A=4,6 cases show A takes some evens). Yet B still wins. So the invariant is more robust.

Let me think about it as a "pairing" argument. B's strategy (B_first=n, play x-1): B pairs each A move x (after first) with x-1. So B claims {n} ∪ {x_i - 1}. 

Hmm, let me think about the "shadow" of A's set. B's set (excluding n) = {x-1 : x ∈ A's set, x ≠ first move}. So B's set = {n} ∪ (A's set minus first move, shifted down by 1).

A's set = {a} ∪ {x_2, ..., x_k}. B's set = {n} ∪ {x_2-1, ..., x_k-1}.

For A to be stuck after k A-moves: remaining numbers all blocked by A. Remaining = [n] \ (A's set ∪ B's set) = [n] \ ({a, x_2,...,x_k} ∪ {n, x_2-1,...,x_k-1}).

This is getting algebraic. Let me think about the total count. n odd. A makes k moves, B makes k moves (B moves after each A move; game ends on A's (k+1)th attempt). Total 2k taken, n - 2k remaining. For n=11, k=5, 2k=10, 1 remaining. For n=9, k=4, 2k=8, 1 remaining. For n=7, k=3, 2k=6, 1 remaining. So k = (n-1)/2, remaining = 1. 

So for odd n, the game ends with A making (n-1)/2 moves, B making (n-1)/2 moves, 1 number remaining, A stuck. So B's strategy ensures A is stuck after exactly (n-1)/2 rounds with 1 number left.

So I need to show: B's strategy ensures (a) B always has a legal move for (n-1)/2 rounds, (b) after (n-1)/2 rounds, exactly 1 number remains and it's blocked by A, (c) A is forced to keep moving (can't get B stuck).

Hmm, this is a lot. Let me reconsider whether there's a cleaner high-level proof.

Actually, let me reconsider the whole approach. This problem is clearly quite hard (irregular answer, complex strategy). Let me reconsider whether the intended answer might be different and cleaner, and my computation has an error.

Let me re-verify the computation independently with a different code style, especially n=6 (draw) and n=8 (B wins), since these are the surprising boundary cases.

Actually, I hand-verified n=6 draw carefully. And n=3,4,5. Let me re-verify n=7 and n=8 with a clean independent check.

n=7: B wins. Let me verify A=1 → B can force win. A=1, B=7 (mirror). Then A's options {3,4,5,6} (not 2, forbidden). 
  A=3: B=2 (per trace). A={1,3},f{2,4}. avail{4,5,6}. B={7,2},f{1,3,6}. A picks 5 (4 forbidden). A={1,3,5},f{2,4,6}. avail{4,6}. B={7,2},f{1,3,6}. B picks 4 (not in B's f). B={7,2,4},f{1,3,5,6}. avail{6}. A f{2,4,6}→6 blocked. stuck. 
    But wait, could A pick 6 instead of 5? A={1,3},f{2,4}. avail{4,5,6}. 6 not in f. A=6. A={1,3,6},f{2,4,5,7}. avail{4,5}. B={7,2},f{1,3,6}. B picks 4 (not in B's f{1,3,6}). B={7,2,4},f{1,3,5,6}. avail{5}. A f{2,4,5,7}→5 blocked. stuck. 
    A=4: A={1,4},f{2,3,5}. avail{3,5,6}. B={7,2},f{1,3,6}. B picks 5 (not in f). B={7,2,5},f{1,3,4,6}. avail{3,6}. A f{2,3,5}→3 blocked, 6? 6 not in A's f{2,3,5}. A=6. A={1,4,6},f{2,3,5,7}. avail{3}. B={7,2,5},f{1,3,4,6}. B can't pick 3 (in f). B stuck! B loses!
    
Uh oh. So if A=1, B=7, A=4, then B=5 (trace) leads to B getting stuck? Let me recheck. A={1,4}, B={7,2}. avail{3,5,6}. B's turn. B's f = neighbors of {7,2} = {1,3,6,8} → in range {1,3,6}. B can pick from avail{3,5,6} minus f{1,3,6} = {5}. So B MUST pick 5. B=5. B={7,2,5},f{1,3,4,6}. avail{3,6}. A's turn. A={1,4},f{2,3,5}. A can pick from avail{3,6} minus f{2,3,5} = {6} (3 in f). A=6. A={1,4,6},f{2,3,5,7}. avail{3}. B's turn. B={7,2,5},f{1,3,4,6}. B can pick from avail{3} minus f{1,3,4,6} = {} (3 in f). B stuck! B loses!

So A=1,B=7,A=4,B=5,A=6 → B stuck. So B=7 is NOT winning against A=4?! But the minimax said n=7 A=1 → B=7 wins (value from A = -1, B wins). Contradiction?

Wait, let me recheck. Maybe B shouldn't play 2 after A=1,B=7,A=4. Let me recompute. A=1, B=7, A=4. Now B's turn. B={7}, f{6}. avail{2,3,5,6}. B can pick 2,3,5 (not 6, in f). The trace said B=2. Let me check B=2: B={7,2},f{1,3,6}. avail{3,5,6}. A={1,4},f{2,3,5}. A picks 6 (only option, as 3,5 in f). A=6. A={1,4,6},f{2,3,5,7}. avail{3,5}. B={7,2},f{1,3,6}. B picks 5 (3 in f). B={7,2,5},f{1,3,4,6}. avail{3}. A={1,4,6},f{2,3,5,7}. A can't pick 3 (in f). A stuck! A loses.

Wait, I made an error before. Let me redo. After A=1,B=7,A=4,B=2,A=6: A={1,4,6}, B={7,2}. avail{3,5}. B's turn (move 6). B={7,2},f{1,3,6}. B can pick from {3,5} minus {1,3,6} = {5}. B=5. avail{3}. A's turn (move 7). A={1,4,6},f{2,3,5,7}. A can pick from {3} minus {2,3,5,7} = {}. A stuck. A loses. 

I previously wrote "B picks 4" which was wrong (4 already taken by A). Let me recheck: after A=1,B=7,A=4,B=2, avail = {3,5,6} (1,4,7,2 taken). A=6. avail={3,5}. B's turn. B={7,2}, f={1,3,6}. avail{3,5}. B can pick 5 (3 in f). B=5. avail{3}. A stuck. Yes A loses. I made an arithmetic error before (said B picks 4, but 4 taken). So B=7,A=4 line: A loses. Good, consistent with minimax.

OK so my hand analysis had an error; the code is right. Good.

Let me also double-check n=8 B wins independently for one line. n=8, A=1, B=8 (trace), A=3, B=5, A=6, B=2, A stuck. Let me verify A can't escape. A=1,B=8. A's options {3,4,5,6,7} (not 2). 
  A=3: B=5. A={1,3},f{2,4}. avail{2,4,6,7}. B={8,5},f{4,6,7}. A picks 6 or 7 (2,4 in f; 6,7: 6 not in A's f, 7 not in A's f). 
    A=6: A={1,3,6},f{2,4,5,7}. avail{2,4,7}. B={8,5},f{4,6,7}. B picks 2 (4,7 in B's f). B={8,5,2},f{1,3,4,6,7}. avail{4,7}. A f{2,4,5,7}→4,7 blocked. stuck.
    A=7: A={1,3,7},f{2,4,6,8}. avail{2,4,6}. B={8,5},f{4,6,7}. B picks 2. B={8,5,2},f{1,3,4,6,7}. avail{4,6}. A f{2,4,6,8}→4,6 blocked. stuck.
  A=4: A={1,4},f{2,3,5}. avail{2,3,5,6,7}. B={8},f{7}. B's best? trace says B=5 (for A=3). For A=4, let me compute B's best. Actually the trace for A=1 was A=3 (optimal A). A=4 might be different. Let me trust minimax: n=8 A=1 → B wins (value -1). So all A responses lose. 

OK I'm confident in the answer. Now let me also handle even n ≥ 8. H1/H2 only draw for even n. I need a different strategy for even n ≥ 8.

Let me find a strategy for even n ≥ 8. Let me look at the minimax traces for even n again:
n=8:
A=1: B=8, A=3, B=5, A=6, B=2. 
A=2: B=1, A=4, B=3, A=6, B=8.
A=3: B=1, A=5, B=4, A=7, B=6.
A=4: B=1, A=2, B=3, A=6, B=8.
A=5: B=1, A=2, B=3, A=7, B=6.
A=6: B=1, A=2, B=4, A=8, B=7.
A=7: B=1, A=2, B=3, A=4, B=5.
A=8: B=1, A=2, B=4, A=5, B=6.

n=10:
A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4.
A=2: B=1, A=4, B=3, A=6, B=5, A=8, B=10.
...

Hmm, even n strategies are more complex. Let me look at the structure for even n. 

For even n, the parity partition has |odds| = |evens| = n/2. A and B each make n/2 - 1 moves before A gets stuck? Let me count n=8: A makes 3 moves, B makes 3 moves, 2 remaining, A stuck. n=8, 6 moves, 2 remaining. n=10: A makes 4, B makes 4, 8 moves, 2 remaining. So for even n, A makes (n-2)/2 moves, B makes (n-2)/2 moves, 2 remaining, A stuck.

So B's strategy for even n ≥ 8: force A stuck with 2 numbers remaining.

Let me find a clean strategy for even n. Let me test some candidates. 

Looking at n=8 traces, B's first move: A=1→B=8, A=2..8→B=1. Same as odd: B picks 1 if available else n. Then B's subsequent moves vary.

Let me look at n=8, A=1: B=8, A=3, B=5 (not x-1=2, not x+1=4). B=5. Hmm. Then A=6, B=2 (x-4? no). 

n=8, A=1: B=8. A=3. B=5. Why 5? After A=1,B=8,A=3: A={1,3},f{2,4}. avail{2,4,5,6,7}. B={8},f{7}. B can pick 2,4,5,6 (not 7). B picks 5. 

Then A={1,3},f{2,4}. avail{2,4,6,7}. A picks 6 or 7. A=6 (trace). A={1,3,6},f{2,4,5,7}. avail{2,4,7}. B={8,5},f{4,6,7}. B picks 2. avail{4,7}. A stuck.

So B's strategy for even n is different and more complex. Let me try to find a pattern by testing strategies.

Let me think about even n differently. For even n, maybe B uses a strategy based on the center two elements.

Actually, let me reconsider. For even n, the reflection strategy gives a draw. B needs to deviate to win. The deviation seems to involve B taking a "central" number to break symmetry.

Let me look at n=8, A=1, B=8, A=3, B=5: B took 5, which is center-right (center of 8 is between 4 and 5). So B takes a central number to break the draw.

Hmm. Let me try to find a strategy for even n by testing. Let me consider strategy: B_first = 1 if avail else n. Then B plays... let me look at the pattern of B's moves relative to A.

n=8, A=1: B: 8, 5, 2. A: 1,3,6. 
n=8, A=2: B: 1, 3, 8. A: 2,4,6.
n=8, A=3: B: 1, 4, 6. A: 3,5,7.
n=8, A=4: B: 1, 3, 8. A: 4,2,6.
n=8, A=5: B: 1, 3, 6. A: 5,2,7.
n=8, A=6: B: 1, 4, 7. A: 6,2,8.
n=8, A=7: B: 1, 3, 5. A: 7,2,4.
n=8, A=8: B: 1, 4, 6. A: 8,2,5.

This is quite irregular. Let me see if there's a reflection-like structure. For A=1: A={1,3,6}, B={8,5,2}. Reflection of A={1,3,6} in n=8 is {8,6,3}. B={8,5,2}. Not reflection. 

Hmm. Let me try: is B's set = reflection of A's set minus something plus something? A={1,3,6}, refl={8,6,3}. B={8,5,2}. B has 8 (=refl of 1), 5 (not refl of 3=6, not refl of 6=3), 2 (not refl). No.

This is really irregular. Let me try a different approach: maybe for even n, B's strategy is to reduce to the odd (n-1) game by "sacrificing" one number.

Idea for even n ≥ 8: B's first move takes n (or 1). Then B treats the remaining n-1 numbers as an odd game? But n-1 is odd, and B's first move is one of the endpoints...

Actually, here's an idea: For even n, B's first move = 1 (if A didn't take 1) or n. This removes one endpoint. The remaining numbers {2,...,n} (if B took 1) or {1,...,n-1} (if B took n) form a path of length n-1 (odd). Now it's A's turn, and A has already made 1 move (a). B has made 1 move (endpoint). 

Hmm, but the odd game strategy requires B to move second in the sub-game. Let me think.

Actually, let me reconsider. After A's first move a and B's first move (endpoint), the remaining available numbers form a set. If B took 1 and a ≠ 1, remaining = {2,...,n} \ {a}, which is n-1 numbers (odd count) but not contiguous (a removed). If a is interior, it splits into two intervals.

This is getting complicated. Let me just try to find a working strategy for even n by testing more candidates, or accept that the even n case needs a more complex strategy and try to construct one based on the odd case.

**Key idea for even n**: B's first move takes an endpoint (1 or n). Then B plays the odd-n strategy on the remaining n-1 numbers, treating A's first move as the "first move" of the sub-game and B's endpoint as already placed.

Wait, the odd-n strategy for n-1 (odd) requires B to respond to A's first move in the sub-game by taking the opposite endpoint of the sub-game. But B already took an endpoint of the original board...

Let me think concretely. Even n. A picks a. B picks 1 (assume a ≠ 1; if a=1, B picks n, symmetric). Now remaining = {2,3,...,n}\{a}. B has {1}. A has {a}. A's turn. 

Now B wants to apply an odd-game strategy on the interval [2, n] (length n-1, odd). In this sub-game, the "numbers" are 2,...,n. A has already placed a (in this interval). B has placed 1 (outside, but 1 is adjacent to 2, so B's piece at 1 affects B's legality for 2). Hmm, B's piece at 1 means B can't play 2 (adjacent). 

In the odd strategy on [2,n] (length n-1), B's first response should be the opposite endpoint. The endpoints of [2,n] are 2 and n. A placed a in [2,n]. If a ≤ center of [2,n] = (2+n)/2 = (n+2)/2, B takes n; else B takes 2. But B can't take 2 (adjacent to B's 1)! So B takes n (if a is in lower part) — that's fine. If a is in upper part (a > (n+2)/2), B would want to take 2, but can't (adjacent to 1). Problem.

So this only works if A's first move a is in the lower part of [2,n], i.e., a ≤ (n+2)/2, i.e., a ≤ n/2 + 1. For a > n/2+1, B can't take 2. 

By symmetry, if a is in the upper part, B should take n first (not 1), then apply the strategy on [1, n-1]. Let me reconsider: B takes the endpoint NEAR a? Or FAR?

Let me reconsider. If a is in lower half (a ≤ n/2), B takes n (far endpoint). Remaining [1, n-1]\{a}, B has {n}. B's piece at n affects n-1 (B can't play n-1). Sub-game on [1,n-1] (length n-1, odd). A placed a. B's response: opposite endpoint of [1,n-1] = endpoints 1 and n-1. If a ≤ center=(n)/2, B takes n-1; else B takes 1. But B can't take n-1 (adjacent to n)! So B takes 1 (if a > n/2) — but a ≤ n/2 (lower half), so a ≤ n/2, B would take n-1, can't. Problem again.

Hmm. The issue: B's endpoint piece blocks the adjacent sub-game endpoint.

Let me reconsider. Maybe B takes the endpoint on the SAME side as a, then plays the odd strategy pushing A toward the far (open) side.

If a ≤ n/2 (lower), B takes 1 (same side, near). Remaining [2,n]\{a}. B has {1}, blocks 2 for B. Sub-game [2,n] (odd length n-1). A placed a (in [2,n], lower part since a ≤ n/2 ≤ (n+2)/2). B's odd-strategy first response: opposite endpoint of [2,n] = n (since a in lower part). B takes n. OK! B can take n (not blocked). Then B plays x-1 (push toward... in odd strategy, B_first=n means play x-1, pushing A right toward n). Wait, in the odd strategy on [2,n] with B_first=n, B plays x-1. But x-1 could be 1 (if x=2), which is taken by B (B has 1). Or x-1 could be a-1... 

This is getting complicated but might work. Let me just test it: even n strategy = "B takes 1 if a ≤ n/2 else n (same-side endpoint); then apply odd-strategy H2 on the remaining interval."

Actually, let me just directly test a strategy for even n: B_first = 1 if a ≤ n/2 else n. Then B plays x-1 if B_first=n else x+1 (push away from B's endpoint), with fallback. Wait, that's H1/H2 which only drew. 

Hmm. Let me reconsider. The issue is even n needs a genuinely different approach. Let me look at the n=8 minimax more carefully and reverse-engineer.

n=8, A=1: B=8. (B took FAR endpoint, since a=1 ≤ 4.) Then A=3, B=5. 
n=8, A=2: B=1. (B took NEAR endpoint? a=2 ≤ 4, but B took 1, the near/same-side.) 
n=8, A=3: B=1. (a=3 ≤ 4, B took 1, same-side.)
n=8, A=4: B=1. (a=4 = n/2, B took 1.)
n=8, A=5: B=1. (a=5 > 4, B took 1, opposite-side.)
n=8, A=6: B=1.
n=8, A=7: B=1.
n=8, A=8: B=1. (a=8, B took 1, opposite.)

So for n=8, B takes 1 unless a=1 (then takes 8). So B_first = 1 if available else 8. Same rule as odd n! "B takes 1 if available, else n."

Then subsequent moves. Let me look at n=8, A=1, B=8, A=3, B=5: B's second move is 5. A=3, B=5. 5 = ? Not x-1=2, not x+1=4. 5 is... reflection of 3 in n=8 is 6. Not 5. 5 = 3+2. Hmm.

Let me look at all of B's second moves for n=8:
A=1,B=8: A=3→B=5. 
A=2,B=1: A=4→B=3. (x-1)
A=3,B=1: A=5→B=4. (x-1)
A=4,B=1: A=2→B=3. (x+1)
A=5,B=1: A=2→B=3. (x+1)
A=6,B=1: A=2→B=4. (x+2? no. 2+2=4. or reflection of 2 in [1,8] is 7. no.) Hmm B=4 for A=2. 
A=7,B=1: A=2→B=3. (x+1)
A=8,B=1: A=2→B=4. (x+2)

So mostly x±1, but A=1 case B=5 (x+2), A=6 and A=8 cases B=4 (x+2). Irregular.

This even-n strategy is genuinely complex. I'm spending a lot of time. Let me reconsider the proof approach.

Given the complexity, maybe the cleanest proof for the even n ≥ 8 case is to reduce to the odd case via a different mechanism, OR to use a strategy I can verify computationally for a base case and then use induction.

**Induction idea for even n**: Show B wins for n ≥ 8 by induction, reducing n by 2. Base cases n=8, 10 (verified computationally). Induction: if B wins for n, B wins for n+2.

How to reduce n+2 to n? B's strategy on n+2: B's first move takes one of the new endpoints (n+1 or n+2), and "pair off" the two new numbers, reducing to the n-game.

Concretely: for n+2 (numbers 1..n+2), B's strategy: 
- If A's first move a is in [1, n], B plays n+2 (or n+1), and then plays the n-game strategy on [1,n], treating n+1, n+2 appropriately.
- If A's first move is n+1 or n+2, B plays the other, and... 

Hmm, the new numbers n+1, n+2 interact with n (adjacency). 

Let me think about a cleaner reduction. Pair (n+1, n+2). B's strategy: whenever A plays in {n+1, n+2}, B plays the other. And B plays the n-strategy on [1,n]. But A playing n+1 or n+2 affects A's legality for n (if A takes n+1, A can't take n later, and A can't take n+2). 

This is getting complicated. Let me think about whether induction can work cleanly.

Actually, let me reconsider. Let me think about the structure: for even n ≥ 8, B wins with 2 numbers remaining. For odd n ≥ 7, B wins with 1 number remaining. 

Let me try to find a unified strategy that works for BOTH odd and even n ≥ 7. Let me test the minimax-style "B takes 1 if avail else n, then play adaptively" — but that's just minimax.

Let me try a different unified strategy: B takes 1 if avail else n. Then B plays to "mirror A's move in the sub-board excluding B's endpoint." Hmm.

Actually, let me reconsider. Let me try the strategy: B takes 1 if avail else n. Then B plays (A's last move) reflected in the remaining board... 

Let me just try to find ANY clean strategy for even n by testing a few more candidates.

Candidate E1: B_first = 1 if avail else n. Then B plays x-1 if legal else x+1 if legal else any. (This is "push left" primarily.) Test for even n.

Candidate E2: B_first = 1 if avail else n. Then B plays x+1 if legal else x-1 if legal else any. (Push right.)

Let me test these for even n.
All these simple strategies only draw for even n. The even-n winning strategy is genuinely more complex. 

Let me think about the even n case differently. The minimax for n=8, A=1: B=8, A=3, B=5. B's second move 5 is the KEY deviation. 5 is the "center-right" number. For even n, the center is between n/2 and n/2+1. B taking 5 (=n/2+1 for n=8) breaks the symmetry.

Let me hypothesize: for even n, B's strategy involves taking a central number at some point to break the draw.

Let me look at n=8 traces and find where B takes a central number (4 or 5):
A=1: B=8,5,2. B took 5 (central).
A=2: B=1,3,8. B took 3 (not central), 8.
A=3: B=1,4,6. B took 4 (central).
A=4: B=1,3,8. 
A=5: B=1,3,6. B took 6 (not central).
A=6: B=1,4,7. B took 4 (central).
A=7: B=1,3,5. B took 5 (central).
A=8: B=1,4,6. B took 4 (central).

So B often takes a central number (4 or 5). The strategy seems to be: B takes 1 (or 8), then takes a central number to break symmetry, then cleans up.

This is complex. Let me think about a cleaner conceptual approach for even n.

**Conceptual approach for even n ≥ 8**: 

For even n, a draw requires A to take all of one parity and B the other. B's strategy: B takes 1 (or n) first. This is a number of some parity. Then B plays to force A into a trap.

Hmm, let me think about the parity. For even n, |odds| = |evens| = n/2. A and B each make (n-2)/2 moves before A gets stuck (2 remaining). Wait, n=8: A makes 3 = (8-2)/2 moves. B makes 3. 2 remaining. For a draw, A would make n/2 = 4 moves and B n/2 = 4 moves, all chosen. But A gets stuck after 3 moves. So B prevents A from making the 4th move.

Let me think about the parity partition for even n. Draw requires A = odds (n/2 numbers) and B = evens, OR A = evens, B = odds. A makes n/2 moves in a draw. B prevents A's n/2-th move by making A stuck after n/2 - 1 moves.

B's strategy: B takes 1 (odd). Now for a draw, if A wants odds, A needs all odds including 1 — but 1 taken by B. So A can't get all odds. So A must get all evens for a draw. A needs {2,4,6,...,n}. B needs to prevent this.

B took 1 (odd). For a draw, A = evens = {2,4,...,n}, B = odds = {1,3,5,...,n-1}. B already has 1 (odd, good for B's parity). B needs to take all other odds {3,5,...,n-1} and prevent A from taking all evens.

A's first move a. If a is even, A is going for evens (consistent with draw). If a is odd, A already deviated from "A=evens" (A took an odd), so draw would require A=odds, but 1 taken by B, so A can't get all odds → no draw possible already! So if A's first move is odd (and B took 1), draw is impossible. Then someone wins. B needs to ensure A loses (not B).

If A's first move is even, draw is still possible (A=evens, B=odds). B needs to break it.

So B's strategy depends on parity of A's first move. Let me consider:

Case 1: A's first move a is odd (B took 1). Draw impossible (A can't get all odds since B has 1, and A has an odd a so A≠evens). So the game must end in a win for someone. B needs to win.

Case 2: A's first move a is even (B took 1). Draw possible (A=evens, B=odds). B needs to break the draw and win.

This is still complex. Let me just try to find a working strategy by testing a smarter candidate.

Let me try: B takes 1 if avail else n. Then B plays to take the "reflection" of A's move but shifted, OR play adjacent. Let me look at the actual minimax B moves for n=8 and try to find the rule.

n=8, A=1, B=8: then A=3, B=5. A=6, B=2.
Let me think: after A=1, B=8, the remaining is {2,3,4,5,6,7}. A=3. B=5. 5 is the reflection of 3 in {2,...,7}? Reflection in [2,7]: 2+7-3 = 6. Not 5. Reflection in [2,8]: 2+8-3=7. No. 

Hmm. 5 = 3 + 2. Or 5 is the center of [2,7] is 4.5, and 5 is center+0.5. 

Let me think about it as: B takes the number that is "opposite" to A in the remaining board, but the remaining board excludes B's piece at 8. The remaining available is {2,3,4,5,6,7}. Center is 4.5. A took 3 (left of center). B takes 5 (right of center, symmetric: 3 and 5 are symmetric about 4.5? 4.5-3=1.5, 5-4.5=0.5. No.). 3 and 6 are symmetric about 4.5. So B should take 6 by symmetry, but takes 5. 

I can't find a simple rule. Let me just accept that the even-n strategy is complex and try the induction approach, or find a strategy by more extensive search.

Let me try a strategy based on "B maintains A's set within a shrinking interval." Or let me try strategies with more complex rules and test.

Actually, let me try the strategy: B takes 1 if avail else n. Then B plays (A's last move) ± 1, choosing the side that is NOT adjacent to B's existing pieces and pushes A toward the larger gap. 

Alternatively, let me try: B plays the reflection of A's last move in the CURRENT available set's "center of mass"... too complex.

Let me try a cleaner idea: for even n, B's strategy is the same as odd n strategy but on n-1 (treating one endpoint as already taken). Specifically:

Even n strategy: B takes 1 if A's first move a ≠ 1, else n. (B takes an endpoint.) Now consider the sub-board excluding B's endpoint. If B took 1, sub-board is {2,...,n} (n-1 numbers, odd). A has made 1 move (a, which is in {2,...,n} if a≠1, or a=1 means B took n and sub-board {1,...,n-1}). Now apply the ODD strategy on the sub-board, where A's first move is a (in the sub-board), and B's "first move" in the sub-board is the opposite endpoint of the sub-board.

But B already used its first move on the original endpoint (1 or n). In the sub-board {2,...,n}, B's odd-strategy first move should be the opposite endpoint: if a ≤ center of sub-board, B takes n; else B takes 2. But B already took 1 (outside sub-board). B's piece at 1 blocks 2 for B. So if the odd strategy says "B takes 2," B can't. 

When does odd strategy say "B takes 2" in sub-board {2,...,n}? When a > center of {2,...,n} = (n+2)/2 = n/2 + 1. So if a > n/2+1, B can't take 2. 

So this works only if a ≤ n/2+1 (then B takes n in sub-board, which is fine). For a > n/2+1, by symmetry B should take n first (original), sub-board {1,...,n-1}, and odd strategy takes 1 if a > center of {1,...,n-1} = n/2. If a > n/2, B takes 1 in sub-board — but B already took n (original), and 1 is in sub-board, B can take 1 if not blocked. B's piece at n blocks n-1, not 1. So B can take 1. Good. But wait, if a > n/2+1, is a > n/2? Yes. So B takes n (original first), sub-board {1,...,n-1}, odd strategy: a > n/2 → B takes 1. B takes 1. OK.

But what about a = n/2+1 exactly? a ≤ n/2+1 → B takes 1 (original), sub-board {2,...,n}, a = n/2+1 = center of sub-board. Odd strategy: a ≤ center → B takes n (opposite endpoint of sub-board). B takes n. Fine.

And a = n/2? a ≤ n/2+1 → B takes 1 (original), sub-board {2,...,n}, a = n/2 ≤ (n+2)/2 = n/2+1. a ≤ center → B takes n. Fine.

So the strategy: 
- If a ≤ n/2 + 1: B takes 1 (original endpoint). Sub-board {2,...,n}. Apply odd strategy on {2,...,n} with A's first move a: B's sub-first-move = n (opposite endpoint, since a ≤ center). Then B plays x-1 (odd strategy, B_sub_first = n → play x-1).
- If a > n/2 + 1: B takes n (original endpoint). Sub-board {1,...,n-1}. Apply odd strategy on {1,...,n-1}: B's sub-first-move = 1 (since a > center of {1,...,n-1} = n/2). Then B plays x+1 (B_sub_first = 1 → play x+1).

Wait, but B's "original first move" and "sub-first move" are TWO moves. B only gets one move per A move. Let me reconsider. B's first move (response to A's first) = the original endpoint. Then B's SECOND move (response to A's second) = the sub-board's opposite endpoint. Then B's subsequent moves = x±1.

So:
- B move 1 (response to A's first a): take 1 if a ≤ n/2+1, else n.
- B move 2 (response to A's second): take the opposite endpoint of the sub-board. If B took 1, sub-board {2,...,n}, B takes n. If B took n, sub-board {1,...,n-1}, B takes 1.
  But wait, B taking n on move 2: is n available? B took 1 on move 1, so n available (unless A took n). A's first move a ≤ n/2+1 < n (for n≥8), so A didn't take n. So n available. B takes n. But is n legal for B? B has {1}, n not adjacent to 1 (n ≥ 8). Yes. Good.
  Similarly B takes 1 on move 2 if B took n on move 1: 1 available (A's first a > n/2+1 ≥ 5, so a ≠ 1), 1 legal (B has {n}, 1 not adjacent). Good.
- B moves 3+ (response to A's third+): play x-1 (if B's sub-first was n) or x+1 (if B's sub-first was 1), with fallback.

So B takes BOTH endpoints (1 and n) in its first two moves! Then plays x±1 to push A.

Let me reconsider. After B takes 1 and n (two endpoints), the remaining board is {2,...,n-1} (n-2 numbers, even). A has made 2 moves (a and a2). B has {1, n}. Now B plays x-1 or x+1 to push A toward... 

Hmm wait, this is now an even-length board {2,...,n-1} with B holding both endpoints. Let me reconsider whether this reduces to the odd strategy.

Actually, let me reconsider. The odd strategy on a board of length m (odd) has B taking one endpoint and pushing A toward the other end, trapping A with 1 number remaining. Here, after B takes both endpoints of the original board, the sub-board {2,...,n-1} has length n-2 (even for even n). That's not odd. So the reduction isn't clean.

Let me reconsider. Maybe B takes only ONE endpoint and the sub-board is {2,...,n} (odd length n-1). Then B's sub-first move is the opposite endpoint n. So B takes 1 then n. After that, sub-sub-board {2,...,n-1} (even). Hmm.

Wait, I think I'm overcomplicating. Let me reconsider the odd strategy. In the odd strategy on {1,...,m} (m odd), B takes one endpoint (say m), then plays x-1 for each A move. The game ends with A stuck, 1 number remaining. B takes m and (n-1)/2 - 1 other numbers (x-1's), total (n-1)/2... let me recount. m odd, A makes (m-1)/2 moves, B makes (m-1)/2 moves, 1 remaining. B's moves: 1 (endpoint) + (m-1)/2 - 1 (x-1's) = (m-1)/2. Yes.

For even n, I want A stuck with 2 remaining. A makes (n-2)/2 moves, B makes (n-2)/2 moves. B's moves: 2 (endpoints) + (n-2)/2 - 2 (x±1's) = (n-2)/2. So B takes both endpoints and then (n-6)/2 push moves. 

So the strategy: B takes both endpoints (1 and n) in first two moves, then pushes A with x±1, trapping A with 2 remaining.

Let me formalize and test:
- B move 1: take 1 if a ≠ 1, else n. (Take an endpoint not taken by A.)
  Actually, if a = 1, B takes n. If a = n, B takes 1. If a interior, B takes 1 (say).
- B move 2: take the other endpoint (n if B took 1, or 1 if B took n). Available (A's second move a2 ≠ endpoints? A might take an endpoint as second move!). 

Hmm, A's second move could be an endpoint. If B took 1, A's second move could be n. Then B can't take n (taken by A). Problem.

When would A take n as second move? A's first a (interior or =1). If a=1, B took n. A's second can't be n (taken). If a interior, B took 1. A's second could be n (if n available and legal for A). A takes n if n not adjacent to A's set (A has no n-1). 

So A could take n as second move, blocking B's plan to take n. Let me handle: if A takes an endpoint, B adapts.

This is getting complicated again. Let me just test the "B takes both endpoints then pushes" strategy with fallback and see if it wins for even n.

Let me define strategy E4:
- B move 1: take 1 if available else n.
- B move 2: take n if available (and legal) else 1 if available else (the endpoint not yet taken by anyone)... actually take the other endpoint if available.
- B move 3+: take x-1 if B's "push direction" is left, else x+1. Push direction: if B has both 1 and n, push toward... hmm. 

Actually, let me reconsider. After B takes both endpoints, A is confined to {2,...,n-1}. B pushes A toward one side. But which side? In the odd strategy, B pushes A toward B's endpoint (the one B took first). Here B has both endpoints. 

Let me just test: B takes 1 (move1), n (move2), then plays x-1 (push A right toward n) with fallback. Or x+1 (push left toward 1). Let me test both.

Actually, let me reconsider the direction. In odd strategy with B_first=n, B plays x-1 (takes the number just LEFT of A's move), and A is pushed RIGHT toward n. The trap: A reaches n-2, B takes n-3, n-1 remains blocked by n-2, and n is B's. Wait, for odd n, B_first=n, A pushed right, A reaches n-2 (odd), remaining n-1 (even) blocked by n-2.

For even n with B holding both 1 and n: A is in {2,...,n-1}. If B pushes A right (plays x-1, taking left of A), A moves right toward n-1. A reaches n-2 (even), B takes n-3, remaining n-1 (odd) blocked by n-2, and n is B's. So A stuck with n-1 remaining. But also 1 is B's. So 2 numbers remain? Let me count. Even n, A makes (n-2)/2 moves, B makes (n-2)/2 moves. B's moves: 1, n, and (n-2)/2 - 2 push moves. Total B moves = (n-2)/2. A moves = (n-2)/2. Total = n-2. Remaining = 2. 

Hmm, 2 remaining. For A to be stuck, both remaining must be blocked by A. In the odd-style trap, only n-1 is blocked by n-2. The other remaining number (somewhere on the left) must also be blocked. 

Let me think. B holds 1 and n. A is pushed right. A's set = {a, a2, ..., } moving right. B's push moves take x-1 (left of each A move). The leftmost region: B has 1. The numbers near 1: 2 is adjacent to B's 1 (but that's B's, doesn't block A). A's leftmost move is a (first). If a > 2, then 2 is... available? 2 not taken (B has 1, n; A has a > 2). 2 adjacent to A's set? If A has no 3, then 2 not blocked. So 2 might be available and unblocked → A could play 2. Hmm.

This isn't clean. Let me just test computationally.

Let me test strategy E4: B takes 1 (m1) if avail else n; B takes n (m2) if avail&legal else 1 if avail&legal else any; then push x-1 (or x+1) with fallback. Test both push directions.
Still only draws. The "take both endpoints then push" doesn't win for even n. The even-n winning strategy is genuinely more subtle.

Let me reconsider. The minimax for n=8, A=1: B=8, A=3, B=5. B does NOT take 1 on move 2. B takes 5 (central). So B's strategy is NOT "take both endpoints." B takes 8, then 5 (central), then 2.

Let me reconsider the structure. n=8, A=1, B=8, A=3, B=5, A=6, B=2. Final: A={1,3,6}, B={8,5,2}, remaining {4,7}. Both 4,7 blocked by A (4 adj to 3, 7 adj to 6 and 8-B but 7 adj to A's 6). 

So B's set = {8, 5, 2} = {2, 5, 8}. These are spaced by 3. A's set = {1, 3, 6}. Remaining {4, 7}. 

Interesting: B's set {2,5,8} are all ≡ 2 mod 3. A's set {1,3,6} = {1,3,6}. Hmm, 1≡1, 3≡0, 6≡0 mod 3. Not clean.

Let me look at n=10, A=1: B=10, A=3, B=2, A=5, B=7, A=8, B=4. A={1,3,5,8}, B={10,2,7,4}={2,4,7,10}, remaining {6,9}. 6 blocked by A's 5 (and B's 7). 9 blocked by A's 8 (and B's 10). So both remaining blocked by A.

B's set {2,4,7,10}. A's set {1,3,5,8}. Hmm.

This is really irregular. I'm not finding a clean pattern for even n.

Let me step back and think about whether there's a fundamentally different, cleaner approach to the whole problem that I'm missing.

Let me reconsider the problem from the parity perspective for a potential clean proof.

**Parity Lemma**: Draw ⟺ A's final set = {odds}, B's = {evens} (or swap). [Because path's only 2-coloring is parity.]

Now, here's a key observation: **A moves first, so A makes ⌈n/2⌉ moves and B makes ⌊n/2⌋ moves in a full game (draw). For a draw, A must hold exactly one parity class.**

- If n odd: |odds| = ⌈n/2⌉ = A's move count, |evens| = ⌊n/2⌋ = B's move count. So A MUST hold odds, B MUST hold evens. (A can't hold evens since |evens| < A's move count.)
- If n even: |odds| = |evens| = n/2 = both move counts. So A holds odds or evens.

**Consequence for odd n**: For a draw, A must hold ALL odd numbers. In particular, A must hold 1 (if 1 is odd, yes) and n (n odd). 

B's strategy for odd n: B takes 1 or n (an odd endpoint) on its first move! Then A can't hold all odds → no draw. And B's pushing strategy ensures A gets stuck.

Wait, but for odd n, B's first move (minimax) is 1 (if A≠1) or n (if A=1). Both 1 and n are odd (n odd). So B takes an ODD number first. This breaks A's ability to hold all odds → no draw. Then B's push strategy traps A. 

For even n: A can hold odds OR evens. B taking one number doesn't immediately break both. B takes 1 (odd) → A can't hold all odds (missing 1), but A could still hold all evens. So B needs to also break A=evens. B would need to take an even number too. But B's first move is 1 (odd). B's second move... in minimax n=8, A=1, B=8 (even!), then B=5 (odd). So B took 8 (even) on move 1 (since A=1, B takes n=8, even). So B took an even. Then A=1 (odd), so A holds an odd → A can't hold all evens. And B holds 8 (even) → A can't hold all evens (8 missing). So draw broken both ways.

Hmm wait, for even n, A=1 (odd first move). For draw, A=odds (needs 1,3,5,7) or A=evens (needs 2,4,6,8). A has 1 (odd). If A=odds: A needs {1,3,5,7}, B={2,4,6,8}. B took 8 (even) — consistent with B=evens, but B needs ALL evens {2,4,6,8}. If A=evens: A needs {2,4,6,8}, but A has 1 (odd) → impossible. So A must be =odds for draw. A needs {1,3,5,7}, B needs {2,4,6,8}. B took 8. For draw, B needs all evens. B's strategy: prevent B from completing evens? No—B wants to break the draw. B took 8 (even). For draw, B needs {2,4,6,8}. B has 8. B will take more evens? No, B wants to NOT complete the draw. 

Hmm, this parity analysis says: for even n with A=1, A must collect {1,3,5,7} (odds) for a draw, B must collect {2,4,6,8} (evens). B took 8. If B then takes only evens, B completes {2,4,6,8} → draw (if A completes {1,3,5,7}). So B must take a NON-even at some point to break the draw. B's move 2 = 5 (odd!). So B takes 5 (odd), breaking B's ability to complete evens. Now draw impossible. Then B traps A.

So for even n: B's strategy is (1) take an endpoint, (2) take a number of the "wrong" parity (the parity A would need) to break the draw, (3) trap A.

This is the parity-breaking insight! Let me formalize:

For even n, A's first move a has parity p. For a draw:
- If a is odd: A must hold all odds (since A can't hold all evens — A has an odd). B must hold all evens.
- If a is even: A must hold all evens. B must hold all odds.

B's strategy: B takes an endpoint (1 or n). Then B takes a number of A's parity p (to break A's collection). Then B traps A.

Wait, B takes a number of A's parity → A can't complete its parity class → no draw. Then trap.

For n=8, A=1 (odd, p=odd): B takes 8 (even, endpoint). Then B takes 5 (odd = A's parity p). This breaks A's odds collection (A needs {1,3,5,7}, B took 5). No draw. Then trap.

For n=8, A=2 (even, p=even): B takes 1 (odd, endpoint). Then B takes... A's parity = even. B takes an even to break A's evens. B's move 2 = 3 (odd)?! Trace: A=2, B=1, A=4, B=3. B=3 is odd, not even. Hmm. So B took 3 (odd), not an even. But A's parity is even. So B took opposite parity. 

Wait, that contradicts my theory. Let me reconsider. A=2 (even). For draw, A=evens={2,4,6,8}, B=odds={1,3,5,7}. B took 1 (odd, consistent with B=odds). B's move 2 = 3 (odd, consistent with B=odds). So B is collecting ODDS, which is B's parity for the draw. So B is NOT breaking the draw by parity... 

But the game ends with A stuck, not a draw. Let me see: n=8, A=2, B=1, A=4, B=3, A=6, B=8. Wait trace: A=2,B=1,A=4,B=3,A=6,B=8,STUCK. A={2,4,6}, B={1,3,8}, remaining {5,7}. 5 blocked by A's 4,6. 7 blocked by A's 6. A stuck. 

So B took 8 (even!) on move 3. B's set = {1,3,8} = {1,3,8}: 1,3 odd, 8 even. So B took an even (8), breaking B's odds collection. For draw, B needs {1,3,5,7} (all odds), but B took 8 (even) → B can't complete odds → no draw. And A={2,4,6}, A needs {2,4,6,8} for draw, but B took 8 → A can't complete evens either. So both can't complete → no draw. A stuck.

So B's parity-breaking move is taking 8 (move 3), not move 2. The timing varies.

OK the parity-breaking is real but the timing/mechanism is adaptive. This is genuinely a complex strategy.

Given the extensive complexity, let me reconsider my approach to writing the proof. I think the honest path is:

1. State and prove the Parity Lemma (draw ⟺ parity partition). This is clean and is the key structural insight.
2. Verify small cases n=1..6 directly (draw for 1,2,4,6; B wins for 3,5). These can be done by explicit strategy.
3. For n ≥ 7, give B's winning strategy. For odd n, give the clean H2 strategy and prove it. For even n, give a strategy and prove it (or reduce to odd).

For even n, let me try harder to find a clean reduction to odd n.

**Reduction even → odd**: For even n ≥ 8, B's strategy: B takes 1 (if A≠1) or n (if A=1) — an endpoint. Then B takes the OTHER endpoint on move 2 IF possible, reducing to an odd sub-game. But we saw A might take the other endpoint. 

Alternatively: B takes an endpoint, then plays the odd strategy on the remaining n-1 board, with B's endpoint serving as the odd-strategy's first move. Let me reconsider this carefully.

Even n. A's first move a. B takes endpoint e (1 or n). Remaining board = {1..n}\{e}, which has n-1 numbers (odd). But it's not contiguous if a is interior. Hmm, but actually the "board" is the available numbers, and the odd strategy works on a path. If a is interior, the available numbers form two intervals. The odd strategy might not directly apply.

Wait, but in the odd strategy, A's moves can be anywhere; B just plays x±1. The strategy doesn't require contiguity. Let me reconsider.

Odd strategy H2 on board {1,...,m} (m odd): B takes endpoint (n if a ≤ center else 1), then plays x∓1. The key properties: B's moves always legal, A gets stuck with 1 remaining.

For even n, after B takes endpoint e, the remaining available is {1..n}\{e, a} (n-2 numbers, even). That's even, not odd. So the odd strategy (which needs odd length for 1 remaining) doesn't directly apply.

Hmm. Let me think about even n differently. 

Actually, let me reconsider: maybe for even n, B takes an endpoint, then the game on the remaining n-1 numbers (with A having 1 piece and B having 1 piece at the endpoint) is equivalent to an odd game where B is "ahead." 

Let me think about it as: after B takes endpoint 1 (and A has a), the remaining numbers {2,...,n}\{a}. B has piece at 1 (which blocks 2 for B). Now it's A's turn. This is like a new game on {2,...,n} where A has a pre-placed piece at a, B has a pre-placed piece at 1 (outside, but blocking 2), and A moves first in this sub-game. 

The sub-board {2,...,n} has n-1 numbers (odd). If it were a fresh odd game on {2,...,n}, B (moving second) would win (by odd strategy). But here A has a pre-placed piece and B has a pre-placed piece (at 1, outside). And it's A's turn (A is "moving first" in the sub-game, but A already has a piece). 

In a fresh odd game on {2,...,n}, A moves first (places first piece), B responds. Here, A already has piece at a, and it's A's turn to place a SECOND piece. So A is "ahead" by one move. That changes things — A has 2 pieces before B's 2nd... 

Hmm, this doesn't cleanly reduce.

Let me try yet another approach for even n: induction from odd n.

**Claim**: B wins for even n ≥ 8 by reducing to odd n-1.

Strategy: B's first move takes 1 (if A≠1) or n (if A=1). Now the board {2,...,n} (or {1,...,n-1}) has n-1 (odd) numbers, with A having 1 piece (a) in it and B having 0 pieces in it (B's piece is at the endpoint outside). It's A's turn.

Now B pretends this is a fresh odd game on {2,...,n} where "A" has just played a as the FIRST move. B applies the odd strategy: B's response = opposite endpoint of {2,...,n}. If a ≤ center of {2,...,n} = (n+2)/2, B takes n; else B takes 2. But B can't take 2 (blocked by B's piece at 1)! So if a > (n+2)/2, B can't take 2. 

So this works only if a ≤ (n+2)/2, i.e., a ≤ n/2 + 1. For a in the lower part, B takes n (fine), then plays x-1 (odd strategy). For a in upper part, by symmetry B should take n first (not 1), sub-board {1,...,n-1}, B takes 1 (fine), plays x+1.

So:
- If a ≤ n/2 + 1: B takes 1 (move 1), then n (move 2, = odd-strategy first response in {2,...,n}), then x-1 (push right).
  Wait, but B taking 1 then n is "both endpoints." We tested E4 (both endpoints then push) and it only drew. But E4 took 1 then n ALWAYS (move 2 = other endpoint). The issue was A might take n on move 2. Let me reconsider: here B takes n on move 2 only if a ≤ n/2+1. A's move 2 (a2) — could A take n? A's first a ≤ n/2+1. A's second move a2: A could take n if n available and legal. If A takes n, B can't take n. Then B falls back. 

Hmm, but actually if A takes n on move 2, that's GOOD for B maybe (A took an endpoint, limiting A's own options). Let me just test this refined strategy.

Actually, the difference from E4: E4 pushed in a fixed direction. Here the push direction depends on which side A is. And the "take other endpoint" is the odd-strategy's first response, which is conditional. Let me also handle the case a > n/2+1 (B takes n first, then 1, push left).

Let me also reconsider: maybe the issue with E4 was the push direction. Let me test the strategy that exactly mimics the odd strategy on the sub-board.

Let me define strategy E6 (even n, reduce to odd):
- B move 1: take 1 if a ≠ 1 else n. (endpoint; if a=1 take n, if a=n take 1, if a interior take 1.)
  Actually, to make the sub-board work: if a ≤ n/2+1, B takes 1 (sub-board {2,...,n}, a in lower part, B will take n). If a > n/2+1, B takes n (sub-board {1,...,n-1}, a in upper part, B will take 1).
  But if a=1: a ≤ n/2+1, B takes 1? But 1 taken by A. So B takes n. Then sub-board {1,...,n-1}, a=1 in lower part. B's odd-response = opposite endpoint of {1,...,n-1} = n-1 (if a=1 ≤ center n/2). B takes n-1. Hmm, but B already took n (move 1). B's piece at n blocks n-1 for B! So B can't take n-1. Problem.

Ugh, the endpoint blocking issue again.

Let me reconsider. The fundamental issue: B's first move (endpoint) blocks the adjacent number for B, which is often the sub-board's endpoint.

Let me try: B's first move takes the endpoint FAR from a. If a ≤ n/2, B takes n. Sub-board {1,...,n-1}, a in lower part. B's odd-response = n-1 (opposite endpoint of {1,...,n-1}). B's piece at n blocks n-1. Can't. 

If a ≤ n/2, B takes n. Sub-board {1,...,n-1}. B's odd-response should be the endpoint of {1,...,n-1} opposite to a. a ≤ n/2 ≤ center of {1,...,n-1} = n/2. So a ≤ center, B takes n-1 (far endpoint of sub-board). Blocked. 

Alternatively, B takes the NEAR endpoint. If a ≤ n/2, B takes 1. Sub-board {2,...,n}. a in lower part (a ≤ n/2 ≤ (n+2)/2). B's odd-response = n (far endpoint of {2,...,n}). B's piece at 1 blocks 2, not n. So B takes n. Fine! Then push x-1 (B_sub_first = n → push right, play x-1).

So: B takes NEAR endpoint (1 if a ≤ n/2, n if a > n/2). Then B takes FAR endpoint of sub-board. Then push.

If a ≤ n/2: B takes 1, then n, then x-1.
If a > n/2: B takes n, then 1, then x+1.

This is exactly E4/E5 but with the condition based on a's position! E4 always took 1 then n then push right. Let me test E6: take near endpoint, then far endpoint, then push away from near (toward far).

Wait, "push away from near" = push toward far. If B took 1 (near) then n (far), push A toward n (far) = play x-1? No. In odd strategy, B_first=n (far), play x-1, A pushed right toward n. So push toward far = play x-1 (take left of A, A moves right toward far endpoint n). Yes.

So E6: 
- a ≤ n/2: B takes 1, then n, then x-1 (fallback x+1).
- a > n/2: B takes n, then 1, then x+1 (fallback x-1).

But this is symmetric to E4/E5 essentially (E4 was take 1 then n then x-1, regardless of a). The difference: E6 takes near endpoint based on a. For a > n/2, E6 takes n first then 1 then x+1 (push left). E4 took 1 first then n then x-1 (push right). 

Let me test E6.
Still draws. The "take both endpoints then push" approach fundamentally only draws for even n. The even-n winning strategy requires the more subtle "take a central number to break parity" move.

Let me reconsider. The minimax for n=8, A=1: B=8, A=3, B=5. B takes 8 (endpoint), then 5 (central, NOT endpoint). So B does NOT take both endpoints. B takes one endpoint and one central.

Let me reconsider the parity-breaking insight more carefully and try to build a strategy around it.

For even n, A's first move a with parity p. For a draw, A must collect all of parity p (the parity of a), and B all of parity 1-p. 

B's goal: (1) break the draw by taking a number of parity p (so A can't complete parity p), AND (2) trap A.

B's first move: take an endpoint of parity 1-p (B's parity for the draw). This is consistent with B collecting parity 1-p. So B's first move doesn't break the draw; it's "cooperating" with the draw parity. Then B's SECOND move breaks the draw by taking a number of parity p.

For n=8, A=1 (p=odd): B's parity for draw = even. B takes 8 (even, endpoint) — cooperating. Then B takes 5 (odd = p) — breaking! Then trap.

For n=8, A=2 (p=even): B's parity for draw = odd. B takes 1 (odd, endpoint) — cooperating. Then B takes 3 (odd) — still cooperating?! Trace: A=2,B=1,A=4,B=3. B=3 is odd (cooperating). Then A=6, B=8 (even = p!) — breaking on move 3. 

So the parity-breaking move timing varies. For A=1, B breaks on move 2 (takes 5, odd). For A=2, B breaks on move 3 (takes 8, even). 

Hmm. So the breaking move isn't always move 2. Let me reconsider.

For A=2 (n=8): A={2,4,6}, B={1,3,8}, remaining {5,7}. B took 8 (even) on move 3, breaking A's evens (A needs {2,4,6,8}, B took 8). And B took 1,3 (odds). For draw, B needs {1,3,5,7} (odds). B has {1,3}, missing 5,7. But 5,7 are remaining and blocked by A. So B can't complete odds either. No draw. A stuck.

So in this case, B cooperated with the draw parity (odds) for moves 1-2, then broke on move 3 by taking 8 (even). The trap: remaining {5,7} both blocked by A.

Let me reconsider the pattern. It seems B mostly "mirrors" A's parity (takes opposite parity, cooperating with draw) but at a key moment takes A's parity to break, and the structure leaves A blocked.

This is really the reflection strategy (which gives draw) with a KEY deviation. The reflection strategy: B takes n+1-x (opposite parity, since n even → n+1 odd → n+1-x has opposite parity to x). Reflection gives draw. B deviates at one point to take same-parity, breaking the draw, and the deviation is chosen to trap A.

For n=8, A=1: reflection of 1 is 8. B takes 8 (reflection). A=3, reflection is 6. But B takes 5 (NOT reflection 6). This is the deviation. B takes 5 instead of 6. 5 is adjacent to 6 (the reflection). So B takes the number NEXT TO the reflection.

Hmm, 5 = 6 - 1 = reflection(3) - 1. Or 5 = 3 + 2. 

For n=8, A=2: reflection of 2 is 7. But B takes 1 (not reflection). Hmm, B takes 1, not 7. So not reflection-based.

Wait, n=8, A=2, B=1. 1 is not reflection of 2 (=7). So B's first move isn't reflection here. 

I'm not finding the pattern. Let me just try to find a working strategy by more extensive search, testing strategies that include a "central break" move.

Actually, let me step back and think about the time I'm spending. This is a very hard problem. Let me reconsider whether I should just present the answer with the parity lemma and a strategy that I verify computationally for a range, giving the strategy as an explicit (if complex) procedure, and proving the key lemmas.

Actually, let me reconsider the even n case via a cleaner reduction: **even n ≥ 8 → odd n-1 game with a pre-placed piece.**

Here's a cleaner idea. For even n, B's first move takes 1 (or n). Now REMOVE the number 1 and n from consideration... no.

Let me think about the "extra number" idea. Even n = odd (n-1) + 1 extra. The odd game on n-1 numbers is a B win. The extra number... 

Concretely: even n. B's strategy: take 1 (endpoint). Now consider the sub-game on {2, 3, ..., n} (n-1 numbers, odd). In this sub-game, A has a piece at a (if a ∈ {2,...,n}), B has no piece in the sub-game (B's piece at 1 is outside). It's A's turn. 

Now, IF this sub-game on {2,...,n} were a fresh odd game (A to move first, no pre-placed pieces), B would win. But here A has a pre-placed piece at a, and it's A's turn (A places 2nd piece). So A is one move ahead. 

In the odd game, the first player (A) makes (m-1)/2 moves and gets stuck. Here A has 1 pre-placed + will make more moves. Total A moves in sub-game = 1 (pre) + k. B moves = k. For A to get stuck in sub-game: ... 

Hmm, the pre-placed piece changes the count. Let me think. Sub-game {2,...,n}, m=n-1 odd. Fresh: A makes (m-1)/2 = (n-2)/2 moves, B makes (n-2)/2, 1 remaining, A stuck. With A pre-placed (1 piece already): A will make (n-2)/2 - 1 more moves? Total A pieces = 1 + (n-2)/2 - 1 = (n-2)/2. B pieces = (n-2)/2 - 1? Hmm, the counts shift.

This is getting too complicated. Let me just try a computational search for a clean even-n strategy by testing strategies with a "break" move.

Let me test: B takes 1 if avail else n (move 1). Move 2: B takes the reflection n+1-(A's 2nd move) if legal, ELSE takes (A's 2nd move)-1 or +1. Move 3+: reflection. I.e., mostly reflection but with a deviation. Hmm, but reflection gives draw.

Actually, let me reconsider. The minimax DEVIATES from reflection to win. The deviation is the key. Let me look at where minimax deviates from reflection for even n.

n=8, A=1: reflection would be B: 8, 6, 4, 2 (reflecting 1,3,5,7). Minimax B: 8, 5, 2. So minimax deviates at move 2 (5 vs 6) and move 3 (2 vs 4). 
n=8, A=2: reflection of 2,4,6,8 is 7,5,3,1. Minimax B: 1, 3, 8. Reflecting A={2,4,6}: B should be {7,5,3}. Minimax B={1,3,8}. Completely different. So minimax doesn't use reflection for A=2.

Hmm. So reflection is only used for A=1 (and A=n by symmetry). For other A, minimax uses a different strategy.

Let me look at n=8, A=2 more carefully. A=2, B=1. A=4, B=3. A=6, B=8. So B: 1, 3, 8. A: 2, 4, 6. B plays 1 (=2-1), 3 (=4-1), 8 (=6+2?). Hmm, 8 = 6+2. Or 8 = reflection of 2 in {1..8} = 7? No. 

Actually B: 1, 3, 8. 1=2-1, 3=4-1, 8=6+2. The first two are x-1. The third is x+2 (6+2=8). Why? Because x-1=5, but is 5 legal? After A={2,4,6}, B={1,3}, avail{5,7,8}. B's turn. B={1,3}, f{2,4}. B can pick from avail{5,7,8} minus f{2,4} = {5,7,8}. B picks 8. Why not 5 or 7? 
  B=5: B={1,3,5},f{2,4,6}. avail{7,8}. A={2,4,6},f{1,3,5,7}. A picks 8 (7 in f). A={2,4,6,8}. All chosen → draw! So B=5 → draw. 
  B=7: B={1,3,7},f{2,4,6,8}. avail{5,8}. A={2,4,6},f{1,3,5,7}. A picks 8 (5 in f). A={2,4,6,8}. draw. 
  B=8: B={1,3,8},f{2,4,7}. avail{5,7}. A={2,4,6},f{1,3,5,7}. A can't pick 5 or 7 (both in f). A stuck! B wins. 
So B picks 8 to win (not 5 or 7 which draw). So B's move 3 = 8 (the endpoint) to trap A. 

So the strategy for A=2 (n=8): B plays x-1 (1, 3) for moves 1-2, then on move 3 plays the FAR endpoint 8 to trap A. 

Interesting. So B pushes A right with x-1, and when A reaches the right side, B takes the far endpoint to block, trapping A.

Let me reconsider: A=2, B plays x-1: A=2→B=1, A=4→B=3, A=6→B=5? But B played 8 not 5 on move 3. Because B=5 leads to draw (A takes 8, all chosen). So B deviates to 8 (endpoint) to prevent A from completing.

So the strategy: B plays x-1 (push A right), but when A is about to complete the parity partition (A would take the last even 8), B takes 8 first to block, leaving A stuck.

This is the parity-breaking at the right moment! B cooperates (takes odds, opposite parity) until A is about to complete evens, then B takes the last even (8) to break the draw, and A is stuck because the remaining odds (5,7) are blocked by A's evens (4,6).

So the strategy for even n: B plays the "reflection/push" strategy (cooperating with draw parity) but at the critical moment, B takes the number A needs (an endpoint of A's parity), breaking the draw and trapping A.

This is a clean conceptual strategy! Let me formalize:

**Even n strategy for B**: 
- B takes 1 if A's first move a ≠ 1, else n. (B takes an endpoint.)
- B then plays "adjacent to A on the side toward B's endpoint" (push A away from B's endpoint), which means B takes numbers of opposite parity to A (cooperating with the draw partition).
- At the critical moment (when A is about to take the last number of A's parity class), B takes that number instead, breaking the draw and trapping A.

But "the critical moment" is hard to formalize cleanly. Let me think about it as: B pushes A toward the far endpoint. A collects numbers of parity p (A's parity) as A moves. The far endpoint has parity... For even n, endpoints 1 (odd) and n (even). If B took 1 (odd), the far endpoint n is even. A is pushed toward n. A collects parity p numbers. If p = even, A is collecting evens including n. B blocks A from taking n by taking n at the end. If p = odd, A collects odds, pushed toward n (even) — A can't take n (wrong parity, but also A might take it if legal). Hmm.

This is getting complicated. Let me just test a specific clean strategy: B takes 1 (if a≠1) else n. Then B plays x-1 (if B took 1, push A right) — wait, B took 1 (left endpoint), push A right means B plays... to push A right, B takes the left side of A (x-1), forcing A right. But B has 1, so x-1=1 is blocked for B. So B plays x-1 only when x-1 ≠ 1. 

Hmm. Let me reconsider. For A=2 (n=8), B=1, then B plays x-1: A=4→B=3, A=6→B=5. But B played 8 on move 3, not 5. So B plays x-1 EXCEPT when x-1 would lead to a draw, then B takes the endpoint.

Let me define: B takes 1 (or n if a=1). Then B plays x-1 (push right) as long as it's "safe" (doesn't lead to draw); when taking x-1 would let A complete the partition, B takes n (the far endpoint) instead.

This is still hard to formalize as a simple rule. Let me just test "B takes 1 (or n), then x-1 (or x+1 if B took n), but if the far endpoint is available and taking x-1 would leave A able to complete, take far endpoint." Too vague.

Let me try a different clean strategy: B takes 1 (or n). Then B plays x-1 (push right) ALWAYS, with fallback. EXCEPT B never plays the move that would be "reflection-completing." Hmm.

Actually, let me just test: B takes 1 if a≠1 else n. Then B plays x-1 (fallback x+1, then any). This is E1 which drew. The problem is E1 plays x-1 always, including the move where it should take the endpoint. Let me modify: B plays x-1, BUT if x-1 is the "second-to-last" and taking it leads to draw, take the far endpoint instead. 

I think the cleanest testable strategy is: B takes 1 (or n if a=1), then plays x-1 (push right, fallback x+1), BUT prefers the far endpoint n when available and x ≥ n-2 (A near the far end). Let me just test a strategy where B takes the far endpoint when A is near the far end.

Let me test: B takes 1 if a≠1 else n (move1). Move 2+: if (far endpoint n is available and legal) and (A's last move x ≥ n-2 or taking x-1 leads to draw), take n; else take x-1 (fallback x+1).

This is getting too ad hoc. Let me take a completely different approach: just compute the full minimax strategy table for even n and present it, OR find the strategy by testing "B plays optimally among {x-1, x+1, near endpoint, far endpoint}."

Actually, let me reconsider. Let me test the strategy: B takes 1 if a≠1 else n. Then B plays x-1 if legal, ELSE if x-1 illegal, B takes the far endpoint if legal else x+1. I.e., when x-1 is illegal (x=1 or x-1 taken), B takes the far endpoint. Let me test.

Hmm, but x-1 illegal happens when x=1 (A picks 1, but if B took 1, A can't) or x-1 taken. 

Let me just test several "take far endpoint at the right time" strategies. Let me test: B takes 1 (or n). Then B plays x-1 (push right). When A's move x is such that x+1 = n (i.e., x = n-1), B takes n (far endpoint) instead of x-1. Because A at n-1 is about to take n. Wait, A at n-1 can't take n (n-1 adjacent to n, A's constraint). So A at n-1 doesn't threaten n. Hmm.

Let me reconsider the n=8, A=2 case. A={2,4,6}, B about to move. A's last move x=6. x-1=5. B takes 8 (far endpoint) instead of 5. Why? Because taking 5 would let A take 8 (draw). Taking 8 blocks A. 

When does taking x-1 lead to a draw? When after B takes x-1, A can take the far endpoint and complete the partition. 

Let me think: B takes x-1, then A's turn. A takes the far endpoint n if n available and legal (n not adjacent to A's set). A's set has x (=6), so n=8: 8 adjacent to 6? No (diff 2). So 8 legal for A. A takes 8, completing A's parity class (evens {2,4,6,8}) → but is it a draw? Only if B also completes. B has {1,3,5} (odds, missing 7). 7 remaining, B's turn, B takes 7 (if legal). B={1,3,5,7}, all chosen → draw. So yes, B taking 5 leads to draw (A takes 8, B takes 7, draw). 

So B should take 8 (preventing A from completing evens). Then A stuck (5,7 blocked).

So the rule: B takes x-1 normally, but if taking x-1 allows A to take the far endpoint and complete the partition (leading to draw), B takes the far endpoint instead.

Formally: B takes x-1, UNLESS the far endpoint (n) is available and A can legally take n on the next move (i.e., n not adjacent to A's current set), in which case B takes n.

Wait, but B also needs n to be legal for B. n adjacent to B's set? B has {1, x_j-1's}. n adjacent to x_j-1 iff x_j-1 = n-1, i.e., x_j = n. A can't pick n (if B is about to take it, n available, A hasn't taken it). So x_j ≠ n, so n not adjacent to B's set (except via 1, but 1 far). So n legal for B. Good.

So the rule: B takes x-1, unless (n available AND n not adjacent to A's set), then B takes n.

"n not adjacent to A's set" = A has no n-1. 

Let me test this strategy for even n. But this is for the case B took 1 (push right). For B took n (a=1), symmetric: B takes x+1, unless (1 available AND 1 not adjacent to A's set), then B takes 1.

Let me formalize and test.

Strategy E7:
- Move 1: B takes 1 if a ≠ 1, else n.
- If B took 1 (push right): B takes x-1 if legal, UNLESS (n available and A has no n-1) then B takes n (if legal). Fallback: x+1, then any.
  Wait, "n available and A has no n-1" → B takes n. But also need x-1 legal normally. Let me structure: 
  - If n is available and legal for B and (A has no n-1 in aset): take n.  [preempt A from completing]
  - Else: take x-1 if legal, else x+1 if legal, else any.
- If B took n (a=1, push left): symmetric with 1.
  - If 1 is available and legal for B and (A has no 2): take 1.
  - Else: take x+1 if legal, else x-1, else any.

Hmm, but "A has no n-1" — initially A might not have n-1, so B would take n immediately on move 2. That's the "take both endpoints" which drew. Let me reconsider.

The condition for B to take n (preempt) should be more specific: B takes n only when A is "about to" take n, i.e., when taking x-1 instead would lead to a draw. That's when A can complete its parity class by taking n. 

A can complete parity class by taking n only if A already has all other numbers of parity p (A's parity). For even n, A's parity p. If p = even (n even), A needs {2,4,...,n}. A taking n completes it iff A has {2,4,...,n-2}. If p = odd, A needs {1,3,...,n-1} (but B took 1, so A can't have 1, so A can't complete odds — n is even, not in odds). Wait, if p=odd, A's parity class is {1,3,...,n-1}, which doesn't include n. So A taking n doesn't complete A's parity. So the preempt matters only when p = parity of n = even (n even). I.e., A's first move a is even.

So for even n:
- If A's first move a is even (p=even): A's parity class = {2,4,...,n} (includes n). B must prevent A from taking n after collecting {2,4,...,n-2}. B preempts by taking n when A has collected all of {2,4,...,n-2}.
- If A's first move a is odd (p=odd): A's parity class = {1,3,...,n-1} (doesn't include n). B took 1 (odd), so A can't complete odds. Draw already broken! So B just needs to trap A. B pushes A and traps.

So for a odd (B took 1, draw already broken since A can't get all odds), B just needs to trap A. The push strategy should trap A. But E1 (push with x-1) only drew for a odd. Why? Because the push doesn't trap A; A avoids getting stuck.

Hmm. So even when draw is broken, trapping A requires the right strategy. Let me reconsider.

For n=8, a=1 (odd): B took 8 (n, since a=1). Draw: A needs odds {1,3,5,7}, B needs evens {2,4,6,8}. B took 8 (even, cooperating). A has 1 (odd). Draw still possible (A=odds, B=evens, B has 8 which is in evens). So draw NOT broken by B taking 8. Because 8 is B's parity (even). So B taking 8 cooperates. Then B takes 5 (odd) on move 2 — THIS breaks the draw (B took an odd, B can't complete evens; and A needs 5 for odds, A can't complete odds). So draw broken on move 2.

So for a=1 (odd), B's first move 8 (even, cooperating, draw still possible), then B's second move 5 (odd, breaking draw). 

For a=2 (even), B's first move 1 (odd, cooperating, draw still possible: A=evens, B=odds, B has 1 in odds ✓). Then B's move 2 = 3 (odd, cooperating). Move 3 = 8 (even, breaking draw). So B breaks on move 3.

So B cooperates for a while then breaks. The break timing: B breaks when A has collected enough that breaking traps A.

For a=1 (odd): A collects odds. B cooperates (takes evens) until A has {1,3} (after A's 2nd move), then B takes 5 (the next odd A would want), breaking. Then A is forced: A={1,3}, B={8,5}. A's f{2,4}. avail{2,4,6,7}. A takes 6 or 7. Either way A gets stuck (as computed).

For a=2 (even): A collects evens. B cooperates (takes odds) until A has {2,4,6}, then B takes 8 (the last even), breaking. A stuck.

So the break happens when A has collected all-but-one of its parity class, and B takes the last one. Specifically:
- a=1 (odd), A collects odds {1,3,5,7}: B breaks when A has {1,3} by taking 5? But A needs {1,3,5,7}, A has {1,3}, missing 5,7. B takes 5. A can still take 7. So A hasn't collected "all but one." Hmm. After B takes 5, A={1,3}, avail{2,4,6,7}. A takes 6 or 7. If A takes 7: A={1,3,7},f{2,4,6,8}. avail{2,4,6}. B={8,5},f{4,6,7}. B takes 2. avail{4,6}. A f{2,4,6,8}→4,6 blocked. stuck. If A takes 6: A={1,3,6},f{2,4,5,7}. avail{2,4,7}. B={8,5},f{4,6,7}. B takes 2. avail{4,7}. A stuck. So A stuck after 3 moves regardless. 

So B breaks at move 2 (taking 5) and A is trapped after move 3. The break is early.

For a=2 (even), B breaks at move 3 (taking 8), A trapped after move 3.

The break timing differs. This is hard to formalize as a simple rule.

OK, I've spent a very long time. Let me make a decision: I'll write a proof that:
1. Proves the Parity Lemma (clean, key insight).
2. Handles n=1..6 explicitly.
3. For n ≥ 7: 
   - Odd n: give the H2 strategy (B takes far endpoint, pushes with x∓1, fallback) and prove it works (I'll prove the key properties: B always has a legal move, A gets stuck with 1 remaining).
   - Even n: give a strategy based on "B cooperates with the draw parity via reflection/push, then breaks at the critical moment by taking the last number of A's parity." I'll formalize the break condition and prove it.

Actually, for even n, let me try to find a clean strategy by testing the "break at critical moment" idea precisely. Let me test:

Strategy E8 (even n, B took 1, a even so A's parity = even = parity of n):
- B cooperates: plays x-1 (opposite parity, push right). 
- B breaks: when A has collected all evens except n (i.e., A's set ⊇ {2,4,...,n-2}), B takes n instead of x-1.

But detecting "A has collected all evens except n" is complex. Let me simplify: B takes n when n is the only even number A hasn't taken and A's last move was n-2. Hmm.

Actually, let me reconsider. Let me just test: B takes 1 (or n if a=1). Then B plays x-1 (or x+1 if a=1), BUT if the far endpoint (n or 1) is available and A's last move x is adjacent to the far endpoint minus 1 (i.e., x = n-2 for far=n), B takes the far endpoint. Let me just test "B takes far endpoint when A's last move = n-2 (or 2 for far=1)."

Hmm, let me just test a strategy where B takes the far endpoint when x-1 would be the "completing" move. Let me think about when B should take n instead of x-1.

B takes n instead of x-1 when: taking x-1 leads to draw, but taking n leads to win. Taking x-1 leads to draw when A can then take n and complete. A can take n after B takes x-1 iff n available (yes) and n not adjacent to A's set (A has no n-1). So B takes n when (n available) and (A has no n-1) and (taking n is legal for B). But "A has no n-1" is true for most of the game (A hasn't reached n-1). So B would take n too early.

The real condition: B takes n when A is about to take n on the NEXT move if B doesn't. A takes n next if n available and legal for A and A has no better... but A plays optimally. Hmm.

Actually, the issue is: if B takes x-1 and then A takes n, does that lead to a draw or does B still win? If A taking n completes A's parity class AND B can still complete B's parity class, it's a draw. If A taking n doesn't complete (because B already broke), then A taking n is fine for B.

So B should take n (break) only when A taking n would complete A's parity class (i.e., A has all other members of parity p). For a even, p=even, A needs {2,4,...,n}. A taking n completes iff A has {2,4,...,n-2}. 

So B takes n when A's set ⊇ {2,4,...,n-2} (all evens except n). Equivalently, when A has taken every even number below n. 

Let me test this precise strategy.

Strategy E9 (even n):
- B move 1: take 1 if a ≠ 1, else n.
- Case B took 1 (a ≠ 1): 
  - If a is even (p=even): B plays x-1 (push right, cooperate). BUT if A's set contains all of {2,4,...,n-2} (all evens except n), B takes n (if legal) instead. Fallback x-1, x+1, any.
  - If a is odd (p=odd): A can't complete odds (B has 1). Draw broken. B plays x-1 (push right) to trap. But does x-1 trap? For a odd, let me check n=8, a=3 (odd): B took 1. Then... let me see minimax. n=8, A=3: B=1, A=5, B=4, A=7, B=6. A={3,5,7},B={1,4,6},remaining{2,8}. 2 blocked by A's 3. 8 blocked by A's 7. stuck. So B plays 1, 4, 6. B's moves: 1 (endpoint), 4 (=5-1), 6 (=7-1). So x-1 push right. A={3,5,7} (odds, but missing 1 taken by B). remaining {2,8} blocked. So for a odd, B pushes right with x-1 and A gets trapped (A collects odds 3,5,7, but 1 taken by B, so A is "short" and the evens 2,8 remain blocked by A's 3,7). 

So for a odd (B took 1), the push x-1 traps A (A collects odds except 1, evens remain blocked). Let me verify this is general. For a odd, B took 1 (odd). A collects odds {a, a+2, ...} moving right. A can't take 1 (B has it). A reaches n-1 (odd, since n even → n-1 odd). A's set = {a, ..., n-1} (odds from a to n-1). B pushed with x-1, taking evens. Remaining: the odds below a (i.e., {1,3,...,a-2} minus 1 taken by B = {3,5,...,a-2}) and evens above n-1 (none, n-1 is the top odd, n is even). Wait, remaining also includes n (even). Hmm.

Let me reconsider n=8, a=3: A={3,5,7}, B={1,4,6}, remaining {2,8}. 2 (even, below A's 3), 8 (even, above A's 7). Both blocked by A (2 adj 3, 8 adj 7). So remaining are evens, blocked by A's odds at the boundary. 

So for a odd, A collects odds {a, a+2, ..., n-1}, B collects {1} ∪ {evens that are x-1 for A's moves} = {1, a-1, a+1, ..., n-2}. Remaining = {2,4,...,a-2} ∪ {n} (evens below a and n). These are blocked by A's a (blocks a-1... no, a blocks a-1 and a+1, both odds... wait a is odd, a-1 and a+1 are even). A's a blocks a-1 (even) and a+1 (even, but a+1 taken by B). So a-1 blocked by A. And n blocked by A's n-1. And the evens below a: {2,4,...,a-2}, are they blocked? A's lowest is a. a blocks a-1. a-2 is not adjacent to a (diff 2). So a-2 NOT blocked by A. So a-2 is available and unblocked → A could take it. Problem!

Wait, n=8, a=3: remaining {2,8}. 2 = a-1 (blocked by A's 3). 8 = n (blocked by A's 7). So remaining are a-1 and n, both blocked. Not {2,4,...,a-2}. Let me recompute. n=8, a=3. A={3,5,7}. B={1,4,6}. Taken: {1,3,4,5,6,7}. Remaining: {2,8}. 2 = 3-1 = a-1. 8 = n. So remaining = {a-1, n}. a-1=2 blocked by A's 3. n=8 blocked by A's 7. Both blocked. 

So remaining is {a-1, n}, not all evens below a. Because B took the evens a-1? No, B took 4,6 (=5-1,7-1). B took a+1=4, a+3=6. B did NOT take a-1=2. So a-1=2 remains. And it's blocked by A's a=3. And n=8 remains, blocked by A's n-1=7. So remaining {2,8} = {a-1, n}, both blocked. 

So the count: n=8, A makes 3 moves, B makes 3 moves, 6 taken, 2 remaining. A's 3 moves = {3,5,7} (odds from a=3 to n-1=7, that's 3 odds). B's 3 moves = {1,4,6} (1 + 2 evens). Remaining = {2,8} (a-1 and n). 

So A collects (n-1-a)/2 + 1 odds from a to n-1. For a=3, n=8: (7-3)/2+1 = 3. Yes. B collects 1 + (n-1-a)/2 evens... B's evens = {a+1, a+3, ..., n-2} = {4,6}, that's (n-1-a)/2 = 2 evens. Plus 1. Total B = 3. Remaining = n - 6 = 2 = {a-1, n}. 

For this to work (A stuck), a-1 and n must be blocked. a-1 blocked by A's a. n blocked by A's n-1. Yes. And A must be forced to collect exactly {a, a+2, ..., n-1} (no deviations). Is A forced? A is pushed right by B's x-1. A's options at each step: A can take any available non-forbidden. A's f = neighbors of A's set. As A collects {a, a+2, ...}, A's f includes a-1, a+1, a+3, .... A can take a+2 (next odd, not in f) or jump. If A jumps right (takes a+4 instead of a+2), then a+2 remains available... 

Hmm, A might deviate. Let me check: does the push strategy force A to take consecutive odds? Let me test n=8, a=3, B pushes x-1. A=3, B=1. A's turn: A={3},f{2,4}. avail{2,4,5,6,7,8}. A can take 5,6,7,8 (not 2,4). A takes 5 (cooperate) or deviates (6,7,8). 
  A=6 (deviate): A={3,6},f{2,4,5,7}. avail{2,4,5,7,8}. B={1},f{2}. B plays x-1=5. B={1,5},f{2,4,6}. avail{2,4,7,8}. A={3,6},f{2,4,5,7}. A takes 8 (not in f). A={3,6,8},f{2,4,5,7,9}. avail{2,4,7}. B={1,5},f{2,4,6}. B plays x-1=7. B={1,5,7},f{2,4,6,8}. avail{2,4}. A f{2,4,5,7,9}→2,4 blocked. stuck! 
  A=7 (deviate): A={3,7},f{2,4,6,8}. avail{2,4,5,6,8}. B={1},f{2}. B plays x-1=6. B={1,6},f{2,5,7}. avail{2,4,5,8}. A={3,7},f{2,4,6,8}. A takes 5 (not in f). A={3,5,7},f{2,4,6,8}. avail{2,4,8}. B={1,6},f{2,5,7}. B plays x-1=4. B={1,6,4},f{2,3,5,7}. avail{2,8}. A f{2,4,6,8}→2,8 blocked. stuck!
  A=8 (deviate): A={3,8},f{2,4,7,9}. avail{2,4,5,6,7}. B={1},f{2}. B plays x-1=7. B={1,7},f{2,6,8}. avail{2,4,5,6}. A={3,8},f{2,4,7,9}. A takes 5 or 6. A=5: A={3,5,8},f{2,4,6,7,9}. avail{2,4,6}. B={1,7},f{2,6,8}. B plays x-1=4. B={1,7,4},f{2,3,5,6,8}. avail{2,6}. A f{2,4,6,7,9}→2,6 blocked. stuck. A=6: A={3,6,8},f{2,4,5,7,9}. avail{2,4,5}. B={1,7},f{2,6,8}. B plays x-1=5. B={1,7,5},f{2,4,6,8}. avail{2,4}. A f{2,4,5,7,9}→2,4 blocked. stuck.

So for a=3 (odd), B's push x-1 traps A regardless of A's deviations. So for a odd, the push strategy works (draw already broken by B taking 1, and push traps A). 

So the issue with E1 (which drew for a odd) must be something else. Let me reconsider why E1 drew for a=1 (odd). E1: B takes 1 if avail else n. For a=1, B takes n=8. Then push x-1. A=1, B=8. A=3, B=2 (x-1). A=5, B=4. A=7, B=6. All chosen → draw! 

So for a=1, B took 8 (n, even, cooperating), and pushed x-1, leading to draw (A={1,3,5,7}, B={8,2,4,6}, all chosen). So the push cooperates and completes the partition → draw. B needs to BREAK by taking an odd at some point.

So for a=1 (odd), B's first move 8 (even) cooperates. B must break by taking an odd. The minimax breaks at move 2 (takes 5, odd). 

So the difference between a=1 and a=3 (both odd): for a=3, B took 1 (odd) on move 1, which BREAKS the draw immediately (A can't get all odds). For a=1, B took 8 (even) on move 1 (cooperating, since 1 taken by A), so B must break later.

So the key: B's first move should take a number of A's parity (to break the draw immediately) when possible. For a=1, A's parity=odd, B should take an ODD. But B took 8 (even) because... 1 is taken (by A), and the "endpoint" rule says take n=8 (even). Instead, B should take an ODD endpoint or odd number.

But the only odd endpoint is 1 (taken) and... n=8 is even. So there's no odd endpoint available (1 taken). So B must take an interior odd to break. Minimax takes 5 (interior odd) on move 2. But move 1 is 8 (even). Why not take an odd on move 1?

n=8, a=1: B's move 1 options (odd numbers available): 3,5,7. Let me check if B taking an odd on move 1 wins. B=3: B={3},f{2,4}. A={1},f{2}. avail{2,4,5,6,7,8}. A takes 4,5,6,7,8 (not 2). ... Let me just test B's first move = 3,5,7 for a=1 via minimax.

Actually, the minimax said B's best first move for a=1 is 8 (not an odd). So taking an odd on move 1 is NOT better; 8 is optimal. So B takes 8 (even, cooperating) on move 1, then breaks on move 2. Why is 8 better than breaking immediately? 

Maybe because taking 8 (endpoint) gives B a structural advantage (controls the endpoint) that helps trap A later, and breaking on move 2 is sufficient.

So the strategy isn't "break immediately." It's "take endpoint, then break at the right moment."

OK. I think the even-n strategy is genuinely subtle and I can't easily find a clean closed form. Let me make a decision: I'll write the proof with:
1. Parity Lemma.
2. Small cases.
3. Odd n ≥ 7: H2 strategy with proof.
4. Even n ≥ 8: A strategy based on "B takes the endpoint of A's parity if available, else takes the other endpoint and breaks on move 2 by taking a central number of A's parity." And I'll prove it by reducing to the odd case or by direct analysis.

Actually, let me reconsider the even n case via reduction to odd n-1 more carefully, because I think there's a clean reduction I'm missing.

**Clean reduction for even n**: B's first move takes 1 (if a ≠ 1) or n (if a = 1). Wait, but for a=1, B takes n=8 (even), and we need to break. 

Hmm, let me reconsider. For even n, let me consider B's strategy: take 1 if a ≠ 1, else n. Then the remaining board (excluding B's endpoint) has n-1 numbers. Now apply the ODD strategy on this n-1 board, treating A's first move a as the first move of the odd game, and B's NEXT move as the odd-strategy's first response.

For a ≠ 1 (B took 1): sub-board {2,...,n} (n-1 odd). A's first move in sub-board = a (a ∈ {2,...,n}). Odd strategy: B takes opposite endpoint of {2,...,n}. If a ≤ center=(n+2)/2, B takes n; else B takes 2. But B can't take 2 (blocked by B's 1). So if a > (n+2)/2, B can't take 2 → problem.

For a > (n+2)/2 (a in upper part, a ≠ 1): B took 1, but odd strategy wants B to take 2 (blocked). So instead, B should take n first (not 1). I.e., B's first move depends on a's position:
- a ≤ (n+2)/2: B takes 1. Sub-board {2,...,n}. Odd strategy: B takes n (opposite endpoint). Then push x-1.
- a > (n+2)/2: B takes n. Sub-board {1,...,n-1}. Odd strategy: B takes 1 (opposite endpoint). Then push x+1.

But wait, for a=1: a ≤ (n+2)/2, B takes 1? But 1 taken by A. So B takes n. Then sub-board {1,...,n-1}, a=1 in lower part. Odd strategy: B takes n-1 (opposite endpoint of {1,...,n-1}). B's piece at n blocks n-1! Can't. Problem.

For a=1: B takes n. Sub-board {1,...,n-1}. a=1. Odd strategy on {1,...,n-1}: center = n/2. a=1 ≤ n/2. B takes opposite endpoint = n-1. Blocked by B's n. Can't.

So a=1 is problematic. By symmetry a=n is too. 

For a=1, the minimax takes 8 (n) then 5 (central odd). The "central" move 5 is the break. 5 = (n/2 + 1) for n=8? n/2+1 = 5. Yes! So B takes the central number n/2+1 on move 2. For n=8, that's 5. For n=10, A=1: B=10, A=3, B=2 (not central 6). Hmm, n=10 A=1 trace: B=10, A=3, B=2, A=5, B=7, A=8, B=4. B's moves: 10, 2, 7, 4. B took 10 (n), then 2 (x-1), then 7 (not x-1=4, not x+1=6). 7 = ? Then 4. 

So n=10, A=1: B doesn't take the central number on move 2. B takes 2 (x-1, cooperating). Then breaks at move 3 (takes 7, odd = A's parity). 7 = ? A={1,3,5}, B={10,2,7}. 7 is odd (A's parity), breaks. Then A=8, B=4. A={1,3,5,8},B={10,2,7,4},remaining{6,9}. 6 blocked by 5, 9 blocked by 8. stuck.

So for n=10, A=1, B breaks at move 3 (takes 7). For n=8, A=1, B breaks at move 2 (takes 5). The break timing depends on n.

I really can't find a clean pattern. Let me just go with a computational-verification-based proof for the even case, OR find the strategy by testing the "cooperate then break" with a precise break condition.

Let me test the strategy: B takes 1 if a≠1 else n. Then B plays x-1 (if B took 1) or x+1 (if B took n) [cooperate/push], BUT B takes the far endpoint (n or 1) when A is about to complete its parity class. Precisely, B takes the far endpoint when A's set contains all numbers of A's parity except the far endpoint.

For a=1 (odd, B took n=8): A's parity=odd={1,3,5,7}. Far endpoint from B's perspective... B took n=8, push x+1? No wait. Let me reconsider. For a=1, B took n. The minimax then plays x-1 (push right) — A=3,B=2. Wait, B took n=8 (right endpoint), and plays x-1 (take left of A). A moves right toward 8. So push right. But B's endpoint is 8 (right). A pushed toward 8. 

Hmm, for a=1, B took 8 (right), push right (x-1). A moves right: 1,3,5,7. A collects odds. B takes 2,4,6 (evens, cooperating). This leads to draw (A={1,3,5,7},B={8,2,4,6}). So B must break. B breaks by taking an odd instead of an even at some point. Minimax breaks at move 2 (takes 5 instead of... wait B's move 2 is 5, but x-1 of A=3 is 2. So B takes 5 instead of 2. 5 is odd (A's parity), 2 is even (B's parity). So B breaks by taking 5 (odd) instead of 2 (even).

So the break: instead of taking x-1 (cooperate), B takes a number of A's parity. Specifically, B takes x+2 (5 = 3+2) instead of x-1 (2). 

For n=10, A=1: B=10, A=3, B=2 (cooperate, x-1). A=5, B=7 (break! 7 = 5+2, odd). So B breaks at move 3, taking x+2=7 instead of x-1=4. 

For n=8, A=1: B=8, A=3, B=5 (break, 5=3+2). Break at move 2.
For n=10, A=1: break at move 3 (7=5+2).
For n=12, A=1: let me predict. B=12, A=3, B=2, A=5, B=4, A=7, B=9 (break, 9=7+2)? Let me check the trace.

Let me get the n=12, A=1 trace.
Now I see the pattern for even n, A=1.

n=8, A=1: B=8, A=3,B=5(break),A=6,B=2. Break at B's move 2 (5 = 3+2).
n=10, A=1: B=10, A=3,B=2, A=5,B=7(break), A=8,B=4. Break at B's move 3 (7 = 5+2).
n=12, A=1: B=12, A=3,B=2, A=5,B=4, A=7,B=9(break), A=10,B=6. Break at B's move 4 (9 = 7+2).
n=14, A=1: B=14, A=3,B=2, A=5,B=4, A=7,B=6, A=9,B=11(break), A=12,B=8. Break at B's move 5 (11 = 9+2).

So for A=1 (even n), B cooperates (x-1) for the first few moves, then breaks by taking x+2 (an odd, A's parity) at a specific move. The break move is x+2 where x is A's last move.

Break timing:
- n=8: break at B-move 2, A's last move x=3, break=5=3+2. A has {1,3}.
- n=10: break at B-move 3, A's last move x=5, break=7=5+2. A has {1,3,5}.
- n=12: break at B-move 4, A's last move x=7, break=9=7+2. A has {1,3,5,7}.
- n=14: break at B-move 5, A's last move x=9, break=11=9+2. A has {1,3,5,7,9}.

So B breaks when A has collected {1,3,...,n-5} (odds up to n-5), and A's last move is n-5... wait:
- n=8: A has {1,3}, last x=3. n-5=3. Yes, x=n-5=3.
- n=10: A has {1,3,5}, last x=5. n-5=5. Yes.
- n=12: A has {1,3,5,7}, last x=7. n-5=7. Yes.
- n=14: A has {1,3,5,7,9}, last x=9. n-5=9. Yes.

So B breaks when A's last move x = n-5, by taking x+2 = n-3. Then:
- n=8: break=5=n-3. Then A=6, B=2. A={1,3,6}, remaining{4,7}. 
- n=10: break=7=n-3. Then A=8, B=4. A={1,3,5,8}, remaining{6,9}.
- n=12: break=9=n-3. Then A=10, B=6. A={1,3,5,7,10}, remaining{8,11}.
- n=14: break=11=n-3. Then A=12, B=8. A={1,3,5,7,9,12}, remaining{10,13}.

After break, A takes n-2 (6,8,10,12 = n-2), B takes... 2,4,6,8 = ? 
- n=8: B takes 2 after A=6. 2 = 6-4? or just the leftover. 
- n=10: B takes 4 after A=8. 4 = 8-4.
- n=12: B takes 6 after A=10. 6 = 10-4.
- n=14: B takes 8 after A=12. 8 = 12-4.

So after break, A takes n-2, B takes n-6. Then remaining {n-4, n-1} (e.g., n=8: {4,7}; n=10: {6,9}; n=12: {8,11}; n=14: {10,13}). n-4 and n-1. n-4 blocked by A's n-5? n=8: 4 blocked by A's 3 (n-5=3). Yes. n-1 blocked by A's n-2. n=8: 7 blocked by 6. Yes. So remaining {n-4, n-1} blocked by A's {n-5, n-2}. 

So the strategy for A=1 (even n): B cooperates (x-1) while A collects odds 1,3,...,n-5. When A plays n-5, B breaks by taking n-3 (=x+2). Then A is forced to take n-2, B takes n-6, and A is stuck with {n-4, n-1} remaining, both blocked.

But why does A cooperate (take 1,3,5,...,n-5 in order)? A is pushed by B's x-1. After A=1, B=8. A=3 (A's f={2}, so A takes 3 or higher; A takes 3 as the "natural" push). But A could deviate. The minimax shows A still loses with deviations. But for the PROOF, I need to handle deviations.

This is the same issue as odd n. The push strategy with break handles deviations, but proving it requires care.

OK, I've spent an enormous amount of time. Let me now just WRITE the proof, using:
1. Parity Lemma (clean proof).
2. Small cases (n=1..6) by explicit analysis.
3. For n ≥ 7, I'll present B's strategies and prove them. For odd n, the H2 strategy (clean-ish). For even n, the "cooperate-then-break" strategy. I'll prove the key invariants.

Actually, given the complexity, let me reconsider whether I can give a UNIFIED strategy for all n ≥ 7 that I can prove. 

Let me reconsider the odd n H2 strategy and the even n strategy. They're different. Let me see if there's a unified view.

Unified view: B's strategy is to "push A in one direction, and at the right moment, take a number that blocks A's completion, trapping A."

For odd n: B takes far endpoint, pushes A toward it, A gets trapped against it (1 remaining).
For even n: B takes far endpoint, pushes A toward it, cooperates with parity, then breaks at the right moment (2 remaining).

Hmm. Let me reconsider if the odd strategy H2 actually has a clean proof. Let me re-examine.

Odd n H2: B_first = n if a ≤ c else 1. Then play x-1 (if B_first=n) or x+1 (if B_first=1), fallback to other side.

I showed the preferred move x∓1 is always legal EXCEPT when A picks the near endpoint (1 for B_first=n, or n for B_first=1). In that case, fallback to x±1 (other side).

Let me prove H2 works for odd n ≥ 7. Actually, let me reconsider whether the fallback is even needed, i.e., whether A picking the near endpoint can actually happen in a way that requires fallback, and handle it.

For B_first=n (a ≤ c): A might pick 1 (near endpoint) if 1 available (yes, B took n) and 1 not adjacent to A's set (A has no 2). A picks 1. Then B's x-1=0 invalid, fallback x+1=2. 2 available? 2 taken by B iff A previously picked 3 (B took 2). If A didn't pick 3 before, 2 is available, B takes 2. If A picked 3 before (B has 2), then 2 unavailable, fallback to "any legal."

When does A pick 3 before picking 1? A's first move a ≤ c, a ≠ 3 (else 3 is first). If a ∈ {1,2,4,5,...,c}. a=1: A can't pick 1 again. A picks 3 as 2nd move? A={1},f{2}. 3 available, legal. A=3. B takes 2. Then A picks 1? Can't (taken). So no issue. a=2: A={2},f{1,3}. A can't pick 3. So A never picks 3. a=4: A={4},f{3,5}. A can't pick 3. a=5 (c=5 for n=9): A={5},f{4,6}. A can pick 3 (available, legal). A=3 (2nd move). B takes 2. Then A picks 1? A={5,3},f{2,4,6}. 1 available, legal. A=1. B's x-1=0, fallback x+1=2, but 2 taken by B! So fallback to "any legal." 

So for a=5 (center), n=9, the strategy hits the "any legal" fallback. Let me check what B should play. A={5,3,1}, B={9,2}. avail{4,6,7,8}. B's f={1,3,8}. B can pick 4,6,7 (not 8). "Any legal" — minimax picks 4 (per trace: A=5,B=9,A=1,B=2,A=3,B=4). So B=4. Then A=7,B=6. stuck.

So the "any legal" fallback works but isn't clean. For the proof, I need to handle this case. 

This is getting really messy. Let me reconsider: maybe choose a DIFFERENT strategy for odd n that avoids the fallback entirely.

The fallback is needed because A can pick the near endpoint. What if B's first move takes the near endpoint instead of the far one? Then A can't pick it.

For a ≤ c: near endpoint = 1. If B takes 1 (near), A can't pick 1. Then push... but push direction? If B takes 1 (left), push A right (x+1? or x-1?). Let me reconsider. If B takes 1 and pushes A right (play x+1, taking right of A), A moves right toward n. A might pick n (far endpoint). Then x+1 = n+1 invalid. So same problem on the other side.

So no matter which endpoint B takes, A can pick the OTHER endpoint, causing the push to fail. The fallback handles it.

Alternatively, B takes BOTH endpoints (first two moves). Then A can't pick either endpoint. But for odd n, B taking both endpoints uses 2 moves, and the remaining n-2 (odd) numbers... Let me test "B takes both endpoints then push" for odd n.

Wait, I tested E4/E5 for even n (both endpoints then push) and it drew. Let me test for odd n.

Actually for odd n, let me test: B takes 1 (move1, if avail else n), then n (move2, if avail&legal), then push x-1 or x+1. Let me test this for odd n.

Hmm, but B taking both endpoints for odd n: remaining n-2 (odd) numbers {2,...,n-1}. A has 2 pieces (a, a2). B has {1,n}. Push A. A trapped with... n-2 numbers, A makes (n-2-1)/2 = (n-3)/2 more moves? Total A = 2 + (n-3)/2. Hmm.

Let me just test computationally: odd n, B takes both endpoints then push.
The "near-then-far-then-push" strategy (B takes near endpoint, then far endpoint, then push toward far) works for ALL odd n from 7 to 21, with NO fallback failures (fails=[]) and NO non-loss (all A_loses). 

And importantly, this strategy takes BOTH endpoints, so A can never pick an endpoint, avoiding the fallback issue! Let me verify the preferred push move is always legal (no fallback needed).

For odd n, ODD_both:
- move1: near endpoint (1 if a ≤ c else n).
- move2: far endpoint.
- move3+: push toward far (x-1 if far=n, else x+1).

After B takes both endpoints (1 and n), A is confined to {2,...,n-1}. B pushes A toward far. 

Push move: x-1 (if far=n) or x+1 (if far=1). 
- x-1 legal? x ∈ {2,...,n-1} (A confined, since endpoints taken). x-1 ∈ {1,...,n-2}. x-1 = 1? Only if x=2. But 1 is taken by B. So x-1=1 unavailable. So if A picks x=2, B's x-1=1 is taken. Fallback. Hmm.

Wait, but fails=[] means the strategy never failed (no STRAT_FAIL). So the fallback (other side / any legal) handled it. But I wanted NO fallback. Let me check if fallback was used.

Actually, fails=[] just means no STRAT_FAIL (strategy always had a legal move via fallback). The fallback might still be used. Let me check if the PREFERRED push move is always legal.

For far=n, push x-1. A confined to {2,...,n-1}. A picks x. x-1: if x=2, x-1=1 (taken by B). So preferred illegal when x=2. When does A pick 2? A can pick 2 if 2 available (yes, B took 1 and n, not 2) and 2 not adjacent to A's set (A has no 1 (taken by B, but that's B's; A's constraint is A's own set) and no 3). So A picks 2 if A has no 3. 

So A can pick 2, causing fallback. So the preferred move isn't always legal. But the strategy still wins (with fallback). 

Hmm. So even this strategy needs fallback. But maybe the fallback is cleaner here: when A picks 2 (near B's endpoint 1), B plays x+1=3 (other side). 3 available? 3 taken iff A or B has 3. B has {1,n}, no 3. A has 3? A has 2 (just picked), A's set independent, no 3. So 3 available. 3 legal for B? B has {1,n}, 3 adjacent to 1? No (diff 2). 3 adjacent to n? No. So B plays 3. Clean fallback.

So the fallback is "play x+1 when x-1 unavailable (x=2)", and x+1=3 is always available and legal. Similarly for far=1, push x+1, fallback x-1 when x=n-1 (x+1=n taken), play x-1=n-2 (available, legal).

So the fallback is clean and deterministic: when A picks the number adjacent to B's near endpoint (x=2 for near=1, or x=n-1 for near=n), B plays the other side (x+1=3 or x-1=n-2), which is always available and legal.

Wait, but what if A picks 2 AND 3 is somehow taken? 3 taken by B only if B previously played 3 (as a push move x-1=3, i.e., A previously picked 4). If A previously picked 4, B took 3. Then A picks 2: B's x-1=1 (taken), x+1=3 (taken by B). Both unavailable! Fallback to "any legal." 

When does A pick 4 then 2? A's first move a, then 4, then 2? Or a=4 (first), then 2. Let me think. This requires A to pick 4 (B takes 3) and then pick 2. A picks 2 if A has no 3 (A's set). A has 4, so A has no 3 (independent, 3,4 adjacent, so A can't have both). So A can pick 2 after picking 4. Then B's push for x=2: x-1=1 (taken), x+1=3 (taken by B). Both unavailable. Fallback "any legal."

So the fallback "any legal" CAN be needed. Hmm. But the test shows the strategy still wins. So "any legal" works but isn't clean to prove.

Let me check: does this scenario (A picks 4 then 2, both push sides unavailable) actually occur in optimal play? The test uses A optimal against the strategy, and the strategy won. So even if it occurs, "any legal" suffices. But for a clean proof, I'd want to avoid "any legal."

Let me reconsider. Maybe the push direction should be AWAY from the near endpoint, not toward the far. I.e., if near=1 (B took 1 first), push A RIGHT (toward far=n) by playing x-1 (take left of A). Wait, that's toward far. Hmm. Let me reconsider what "push toward far" means.

If B took near=1 and far=n, and pushes toward far=n (rightward), B plays x-1 (take left of A, A forced right). A moves right. A won't pick 2 (left, near B's 1) because... actually A could pick 2 early. 

Alternatively, push AWAY from far (toward near). If B plays x+1 (take right of A, A forced left toward near=1). A moves left. A picks decreasing. A won't pick n-1 (near far=n) unless... A could.

Hmm, symmetric issue.

Let me reconsider. The cleanest would be: B takes both endpoints, then A is confined to {2,...,n-1}. Now it's a sub-game on {2,...,n-1} (length n-2, which is ODD for odd n). In this sub-game, A has 2 pieces (a, a2) and B has 0 pieces (B's pieces are at endpoints outside). It's B's turn (move 3). 

Wait, this is like a fresh odd game on {2,...,n-1} where A has already placed 2 pieces and B 0, and it's B's turn. That's weird (B is "behind"). 

Actually, let me reconsider the move counting. Odd n. B takes near (move1), far (move2). A has made 2 moves (a, a2). B has made 2 moves. Now move 5 = A's 3rd move. Wait no: move1=A, move2=B(near), move3=A(a2), move4=B(far), move5=A(a3), move6=B(push), ... So after B takes far (move4), it's A's turn (move5). A has 2 pieces, B has 2 pieces (both endpoints). Sub-board {2,...,n-1} has n-2 numbers (odd). A has 2 pieces in it (a, a2, assuming both in {2,...,n-1}; a could be 1 or n if A picked endpoint, but B took endpoints so a ∈ {2,...,n-1}). 

Hmm, A has 2 pieces, B has 0 in sub-board. It's A's turn. This isn't a standard odd game.

Let me just abandon trying to get a no-fallback strategy and instead PROVE the strategy with the clean fallback (x+1 when x-1 unavailable due to endpoint, and handle the rare double-unavailable case separately).

Actually, let me reconsider the whole proof approach. I've spent way too long. Let me just write a proof that:
1. Parity Lemma.
2. Small cases.
3. For n ≥ 7, describe B's strategy and prove it via a careful invariant, handling the push and the break.

Let me reconsider and find the CLEANEST possible strategy to prove. 

For ODD n ≥ 7, the "near-then-far-then-push-toward-far" strategy works. Let me prove it. The push toward far: B plays x-1 (if far=n) or x+1 (if far=1). The issue is A picking the number adjacent to the near endpoint.

Actually, let me reconsider: push AWAY from far (toward near). If far=n, push left: B plays x+1 (take right of A, A forced left toward near=1). Then A moves left, toward 1 (taken by B). A gets trapped against 1. A won't pick n-1 (right, near far=n) because A is moving left. But A COULD pick n-1 early (before moving left). Hmm.

Let me just test "push away from far" (toward near) for odd n.

Actually, both directions had issues. Let me just go with "push toward far" and handle the fallback in the proof.

Hmm, let me reconsider. Actually, let me reconsider the push direction more carefully for the trap.

For odd n, near=1, far=n. A confined to {2,...,n-1}. 
- Push toward far (right): B plays x-1. A forced right toward n. A collects numbers moving right. Trap: A reaches n-2 (or n-1), B takes the adjacent, A stuck with 1 remaining near n.
- Push toward near (left): B plays x+1. A forced left toward 1. A collects moving left. Trap: A reaches 3 (or 2), B takes adjacent, A stuck with 1 remaining near 1.

For push toward far (right), A might pick 2 (left, near 1) early, causing x-1=1 unavailable. For push toward near (left), A might pick n-1 (right, near n) early, causing x+1=n unavailable. Symmetric.

The fallback handles both. Let me just prove the strategy with fallback, arguing that the fallback move (other side) is always available and legal EXCEPT in a rare case that I handle.

Actually, let me reconsider the rare case (A picks 4 then 2, both push sides taken). Let me check if this can actually happen under the strategy, and if so, what B does.

Let me just instrument the strategy to detect when "any legal" (third fallback) is used.
