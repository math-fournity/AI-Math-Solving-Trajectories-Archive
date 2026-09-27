# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $N \geqslant 3$ be an odd integer. $N$ tennis players take part in a league. Before the league starts, a committee ranks the players in some order based on perceived skill. During the league, each pair of players plays exactly one match, and each match has one winner. A match is considered an upset if the winner had a lower initial ranking than the loser. At the end of the league, the players are ranked according to number of wins, with the initial ranking used to rank players with the same number of wins. It turns out that the final ranking is the same as the initial ranking. What is the largest possible number of upsets?
(United Kingdom)       — 题目文本
#   Answer: $\frac{(N-1)(3 N-1)}{8}$.
Suppose the players are ranked $1,2, \ldots, N=2 n+1$, where 1 is the highest ranking.
For $k \leqslant n$, the player ranked $k$ could have beaten at most $k-1$ players with a higher ranking. Thus the top $n$ players could have made at most $\sum_{k=1}^{n}(k-1)=\frac{n(n-1)}{2}$ upsets. On the other hand, the average score of all $2 n+1$ players is $n$, so the average score of the bottom $n+1$ players is not more than $n$, which implies that these $n+1$ players have at most $n(n+1)$ wins in total. Hence the total number of upsets is at most

$$
\frac{n(n-1)}{2}+n(n+1)=\frac{n(3 n+1)}{2}=\frac{(N-1)(3 N-1)}{8} .
$$

An example can be constructed as follows. Suppose that, for $1 \leqslant i \leqslant 2 n+1$, the player ranked $i$ beats the players ranked $i-1, i-2, \ldots, i-n$ (the rankings are counted modulo $N)$ and loses to the rest of the players. Thus each player has exactly $n$ wins. The player ranked $i$ for $i \leqslant n$ made $i-1$ upsets, whereas the player ranked $i$ for $i>n$ made $n$ upsets, so the total number of upsets is exactly $\sum_{i=1}^{n}(i-1)+(n+1) n=\frac{n(3 n+1)}{2}$.  — 标准解答
#   Let me analyze this problem carefully.

We have $N \geq 3$ odd tennis players. Initial ranking $1, 2, \ldots, N$ (1 = highest). Each pair plays, one winner. An upset is when the lower-ranked player (higher number) beats the higher-ranked player (lower number).

Final ranking is by number of wins, with initial ranking as tiebreaker. Final ranking = initial ranking.

We want to maximize the number of upsets.

Let me denote players $1, 2, \ldots, N$ where $1$ is top-ranked. Player $i$ has $w_i$ wins. Total wins = $\binom{N}{2}$.

Final ranking same as initial means: $w_1 \geq w_2 \geq \cdots \geq w_N$ (with ties broken by initial rank, so if $w_i = w_{i+1}$, then $i$ ranks above $i+1$, consistent).

An upset is when player $j$ beats player $i$ with $j > i$ (lower initial rank wins).

The number of upsets = number of pairs $(i,j)$ with $i < j$ where $j$ beats $i$.

Let me think about what constraints we have.

If there were no upsets, player $i$ beats everyone below, loses to everyone above. So $w_i = N - i$. That's $N-1, N-2, \ldots, 0$. Strictly decreasing, final = initial.

Now we want upsets but final ranking preserved.

Let me think about small cases. $N = 3$. Players 1, 2, 3. Matches: (1,2), (1,3), (2,3).

No upsets: 1 beats 2,3; 2 beats 3. $w = (2,1,0)$. 0 upsets.

Can we have 1 upset? Say 3 beats 2 (upset). Then $w_1 = 2, w_2 = 0, w_3 = 1$. Final ranking: 1 (2 wins), 3 (1 win), 2 (0 wins). That's 1,3,2 ≠ 1,2,3. No good.

Say 2 beats 1 (upset). Then 1 beats 3, 2 beats 3. $w = (1, 2, 0)$. Final: 2,1,3 ≠ 1,2,3. No.

Say 3 beats 1 (upset). Then 1 beats 2, 2 beats 3. $w = (1, 1, 1)$. Tie broken by initial: 1,2,3. Yes! Final = initial. 1 upset.

Can we have 2 upsets? Say 3 beats 1 and 2 beats 1. Then 2 beats 3 or 3 beats 2.
- 2 beats 3: $w = (0, 2, 1)$. Final: 2,3,1. No.
- 3 beats 2: $w = (0, 1, 2)$. Final: 3,2,1. No.

Say 3 beats 1 and 3 beats 2. Then 1 beats 2 or 2 beats 1.
- 1 beats 2: $w = (1, 0, 2)$. Final: 3,1,2. No.
- 2 beats 1: $w = (0, 1, 2)$. Final: 3,2,1. No.

Say 2 beats 1 and 3 beats 2. Then 1 beats 3 or 3 beats 1.
- 1 beats 3: $w = (1, 1, 1)$. Final: 1,2,3. Yes! 2 upsets.

Can we have 3 upsets (all reversed)? 2 beats 1, 3 beats 1, 3 beats 2. $w = (0,1,2)$. Final: 3,2,1. No.

So for $N=3$, max is 2.

Hmm, let me think about the pattern. $N=3$: 2 upsets out of 3 matches.

Let me think about $N = 5$.

The answer for this problem... let me think. This is a UK competition problem. The answer is likely $\frac{(N-1)^2}{4}$ or $\frac{N^2-1}{8}$ or something.

For $N=3$: $(N-1)^2/4 = 1$. But we got 2. So not that.

$\frac{N^2-1}{8} = 1$ for $N=3$. No.

Let me reconsider. For $N=3$ we found 2 upsets.

Let me think more carefully about the structure.

Key insight: We need $w_1 \geq w_2 \geq \cdots \geq w_N$.

The number of upsets $U$ relates to the win counts. Let $w_i$ = wins of player $i$. In the "no upset" scenario, player $i$ would beat all $j > i$ and lose to all $j < i$, giving $w_i^{(0)} = N - i$.

Each upset involving pair $(i,j)$ with $i < j$ (j beats i) changes: $w_i$ decreases by 1, $w_j$ increases by 1 compared to no-upset.

So $w_i = (N - i) - u_i^{\text{out}} + u_i^{\text{in}}$ where $u_i^{\text{out}}$ = number of upsets where $i$ loses to someone below, $u_i^{\text{in}}$ = number of upsets where $i$ beats someone above.

Actually, let me define: for pair $(i,j)$, $i < j$. Normal: $i$ beats $j$. Upset: $j$ beats $i$.

$w_i = \#\{j > i : i \text{ beats } j\} + \#\{j < i : i \text{ beats } j\}$
$= (N - i - u_i^-) + u_i^+$

where $u_i^-$ = upsets where $i$ loses to someone below (i.e., $j > i$ beats $i$), and $u_i^+$ = upsets where $i$ beats someone above ($i$ beats $j < i$).

Note $u_i^-$ counts pairs $(i, j)$ with $j > i$ that are upsets, and $u_i^+$ counts pairs $(j, i)$ with $j < i$ that are upsets.

Total upsets $U = \sum_i u_i^+ = \sum_i u_i^-$ (each upset counted once in each sum... no). Actually each upset $(i,j)$ with $i < j$ contributes to $u_j^+$ (j beats someone above) and $u_i^-$ (i loses to someone below). So $\sum_i u_i^+ = \sum_i u_i^- = U$.

$w_i = (N - i) - u_i^- + u_i^+$.

We need $w_1 \geq w_2 \geq \cdots \geq w_N$.

We want to maximize $U$.

Let me think about this differently. Consider the "score sequence" $w_1, \ldots, w_N$. We need it non-increasing and it must be a valid score sequence of a tournament, plus the upset structure must be consistent.

Actually, any non-increasing sequence that's a valid tournament score sequence works, and then we need to check if we can realize it with the right upset count.

Hmm, this is getting complex. Let me think about it from the perspective of maximizing upsets.

Let me consider the construction. For $N = 3$, the optimal was: 2 beats 1, 3 beats 2, 1 beats 3. This is a cyclic tournament (rock-paper-scissors), $w = (1,1,1)$. Upsets: (1,2)→2 wins, (2,3)→3 wins. That's 2 upsets. (1,3)→1 wins, not upset.

So the cycle $1 \to 3 \to 2 \to 1$... wait let me recheck. 2 beats 1 (upset, since 2 > 1), 3 beats 2 (upset, since 3 > 2), 1 beats 3 (not upset). Yes, 2 upsets.

For general odd $N$, maybe we can make all players have the same number of wins $(N-1)/2$, which is a regular tournament. In a regular tournament on odd $N$ vertices, every vertex has out-degree $(N-1)/2$.

If all $w_i = (N-1)/2$, then final ranking = initial ranking (all tied, broken by initial rank). 

Now, can we find a regular tournament that maximizes upsets? The number of upsets in a regular tournament... we want to maximize the number of edges $(i,j)$ with $i < j$ where $j \to i$ (j beats i).

Total edges = $\binom{N}{2}$. In a regular tournament, each vertex has out-degree $(N-1)/2$.

The number of upsets = number of "backward" edges. We want to maximize backward edges while keeping the tournament regular.

Hmm, but is regular tournament optimal? Maybe we can do better with non-regular.

Let me think about upper bounds.

Claim: $U \leq \frac{N^2 - 1}{8}$? For $N = 3$: $(9-1)/8 = 1$. But we found 2. So no.

Let me reconsider. For $N = 3$, $U = 2$, total matches = 3. So $U$ can be close to total.

Let me think about $N = 5$ more carefully.

Let me try to construct a good solution for $N = 5$.

Players 1,2,3,4,5. No-upset wins: $w^{(0)} = (4,3,2,1,0)$.

Idea: Try to make all $w_i = 2$ (regular tournament). Then we need a regular tournament on 5 vertices maximizing upsets.

In a regular tournament on 5 vertices, each has out-degree 2. Total edges = 10. We want to maximize backward edges (edges $(i,j)$, $i < j$, where $j \to i$).

The "canonical" regular tournament on 5 vertices: arrange 0,1,2,3,4 in a circle, each beats the next 2. Edges: $i \to i+1, i \to i+2$ (mod 5).

Let me map: players 1,2,3,4,5 → 0,1,2,3,4.
- 0 beats 1, 2; loses to 3, 4.
- 1 beats 2, 3; loses to 4, 0.
- 2 beats 3, 4; loses to 0, 1.
- 3 beats 4, 0; loses to 1, 2.
- 4 beats 0, 1; loses to 2, 3.

Now count upsets (edges where higher-numbered player beats lower, i.e., $j > i$ and $j \to i$):
- (1,2): 0→1, not upset. (1,3): 0→2, not upset. (1,4): 3→0, upset! (1,5): 4→0, upset!
- (2,3): 1→2, not upset. (2,4): 3→1, upset! (2,5): 4→1, upset!
- (3,4): 2→3, not upset. (3,5): 2→4, not upset. Wait, 2 beats 4? Yes. Not upset (3 < 5, 3 beats 5, not upset).

Wait, I need to recompute. Player 3 = vertex 2, player 5 = vertex 4. Edge (3,5) = (2,4): 2→4, so player 3 beats player 5. Not upset.

- (4,5) = (3,4): 3→4, player 4 beats player 5. Not upset.

Upsets: (1,4), (1,5), (2,4), (2,5). That's 4 upsets.

Can we do better? Let me try a different regular tournament or even non-regular.

Actually, let me think about whether non-regular can give more upsets.

Let me try to maximize upsets directly. We want as many "backward" edges as possible while maintaining $w_1 \geq w_2 \geq \cdots \geq w_5$.

Extreme: try to reverse as many as possible. If we reverse all edges, $w = (0,1,2,3,4)$, which is increasing, not non-increasing. Bad.

Let me think about it as: we start from the transitive tournament (no upsets, $w = (4,3,2,1,0)$) and flip edges. Each flip of edge $(i,j)$, $i < j$ (from $i$ beats $j$ to $j$ beats $i$) decreases $w_i$ by 1 and increases $w_j$ by 1.

We want to maximize the number of flips while keeping $w_1 \geq w_2 \geq \cdots \geq w_N$.

After flipping a set $S$ of edges, $w_i = (N-i) - d_i^- + d_i^+$ where $d_i^-$ = number of flipped edges going down from $i$ (i.e., $(i,j)$ flipped, $j > i$) and $d_i^+$ = number of flipped edges coming up to $i$ (i.e., $(j,i)$ flipped, $j < i$).

We need $w_i \geq w_{i+1}$ for all $i$.

$w_i - w_{i+1} = [(N-i) - d_i^- + d_i^+] - [(N-i-1) - d_{i+1}^- + d_{i+1}^+]$
$= 1 - d_i^- + d_i^+ + d_{i+1}^- - d_{i+1}^+$.

We need this $\geq 0$ for all $i = 1, \ldots, N-1$.

So $d_i^- - d_i^+ - d_{i+1}^- + d_{i+1}^+ \leq 1$ for all $i$.

Let $f_i = d_i^+ - d_i^-$. Then $f_{i+1} - f_i \leq 1$, i.e., $f_{i+1} \leq f_i + 1$.

Also $w_i = (N-i) + f_i$. We need $w_i \geq 0$ (can't have negative wins) and $w_i \leq N-1$ (can't have more than $N-1$ wins). Actually $w_i \geq 0$ is automatic-ish, and $w_i \leq N-1$ too, since wins are between 0 and $N-1$.

Now, $U = \sum_i d_i^- = \sum_i d_i^+ = $ total flips.

We have $d_i^+ = $ number of flipped edges $(j, i)$ with $j < i$ = number of $j < i$ such that $i$ beats $j$ (upset). $d_i^- = $ number of flipped edges $(i, j)$ with $j > i$ = number of $j > i$ such that $j$ beats $i$ (upset).

Constraints:
- $0 \leq d_i^+ \leq i - 1$ (at most $i-1$ players above)
- $0 \leq d_i^- \leq N - i$ (at most $N-i$ players below)
- $f_{i+1} \leq f_i + 1$ for $i = 1, \ldots, N-1$
- $w_i = (N - i) + f_i \geq 0$ and $\leq N - 1$.
- The score sequence must be realizable as a tournament (Landau's condition).

We want to maximize $U = \sum d_i^+ = \sum d_i^-$.

Note $\sum f_i = \sum d_i^+ - \sum d_i^- = 0$. So $\sum f_i = 0$.

We want to maximize $U = \sum d_i^+$. Since $d_i^+ = f_i + d_i^-$ and $d_i^+ \leq i - 1$, $d_i^- \leq N - i$...

This is getting complicated. Let me think about it more cleverly.

We want to maximize $U$. Note $U = \sum d_i^+$. We have $d_i^+ \leq i - 1$ (player $i$ can upset at most $i-1$ players above them). Also $d_i^- \leq N - i$.

Also $d_i^+ = f_i + d_i^-$, so $d_i^+ \leq f_i + (N - i)$, meaning $f_i \geq d_i^+ - (N-i)$. And $d_i^- = d_i^+ - f_i \leq N - i$, so $f_i \geq d_i^+ - (N - i)$, same thing. Also $d_i^- \geq 0$ so $f_i \leq d_i^+$. And $d_i^+ \leq i - 1$.

So $U = \sum d_i^+ \leq \sum (i - 1) = \binom{N}{2}$. That's trivial (all edges flipped, but that violates constraints).

The binding constraint is $f_{i+1} \leq f_i + 1$ and $\sum f_i = 0$ and $w_i = (N-i) + f_i \geq 0$.

$w_i \geq 0 \Rightarrow f_i \geq -(N-i) = i - N$.
$w_i \leq N - 1 \Rightarrow f_i \leq N - 1 - (N - i) = i - 1$.

So $i - N \leq f_i \leq i - 1$.

Also $d_i^+ \leq i - 1$ and $d_i^+ = f_i + d_i^- \leq f_i + (N - i)$. So $d_i^+ \leq \min(i - 1, f_i + N - i)$.

And $d_i^- \leq N - i$ and $d_i^- = d_i^+ - f_i \leq (i-1) - f_i$. So $d_i^- \leq \min(N - i, i - 1 - f_i)$.

$U = \sum d_i^+$. To maximize, we want $d_i^+$ as large as possible. $d_i^+ \leq \min(i-1, f_i + N - i)$.

If $f_i \geq 2i - 1 - N$, then $f_i + N - i \geq i - 1$, so $d_i^+ \leq i - 1$.
If $f_i < 2i - 1 - N$, then $d_i^+ \leq f_i + N - i < i - 1$.

So to maximize $d_i^+$, we want $f_i$ large. But $\sum f_i = 0$ and $f_{i+1} \leq f_i + 1$.

Also we need the tournament to be realizable. Let me set that aside and first find the maximum of $U$ subject to the constraints, then check realizability.

We want to maximize $\sum_i \min(i - 1, f_i + N - i)$ subject to:
- $\sum f_i = 0$
- $f_{i+1} \leq f_i + 1$
- $i - N \leq f_i \leq i - 1$

The function $\min(i-1, f_i + N - i)$ is increasing in $f_i$ (until it saturates at $i-1$). So we want $f_i$ as large as possible. But $\sum f_i = 0$ means we can't have all large.

The constraint $f_{i+1} \leq f_i + 1$ means $f$ can increase by at most 1 per step. Since $\sum f_i = 0$, and $f$ is somewhat constrained...

Let me think about what $f$ sequence maximizes $\sum \min(i-1, f_i + N - i)$.

Since the objective is concave (piecewise linear, increasing then flat), and we have a sum constraint, this is like a resource allocation problem.

Let me think about the "marginal" value. For player $i$, increasing $f_i$ by 1 increases $d_i^+$ by 1 if $f_i + N - i < i - 1$, i.e., $f_i < 2i - 1 - N$, and by 0 otherwise.

But increasing $f_i$ means we need to decrease other $f_j$'s (to keep $\sum = 0$), which might decrease their $d_j^+$.

Also the constraint $f_{i+1} \leq f_i + 1$ links them.

Let me try a specific form. Suppose $f_i = c - (i - 1)$ for some constant $c$ (i.e., $f$ decreases by 1 each step). Then $f_{i+1} = f_i - 1 \leq f_i + 1$. ✓. $\sum f_i = Nc - \sum_{i=1}^N (i-1) = Nc - \binom{N}{2} = 0 \Rightarrow c = \binom{N}{2}/N = (N-1)/2$.

So $f_i = (N-1)/2 - (i-1) = (N+1)/2 - i$.

Then $w_i = (N - i) + f_i = (N - i) + (N+1)/2 - i = (N + (N+1)/2) - 2i = (3N+1)/2 - 2i$.

For $N = 5$: $w_i = 8 - 2i$: $w = (6, 4, 2, 0, -2)$. But $w_5 = -2 < 0$. Not valid.

So this linear decrease is too steep. We need $w_i \geq 0$, i.e., $f_i \geq i - N$.

$f_i = (N+1)/2 - i \geq i - N \Rightarrow (N+1)/2 + N \geq 2i \Rightarrow (3N+1)/2 \geq 2i \Rightarrow i \leq (3N+1)/4$.

For $N = 5$: $i \leq 4$. So $f_5$ violates. We need to adjust.

Let me try a different approach. Let me think about the problem more directly.

Actually, let me reconsider. The constraint $f_{i+1} \leq f_i + 1$ allows $f$ to increase by at most 1. It can decrease arbitrarily fast. So we could have $f$ decrease rapidly and then stay flat.

Let me think about the optimal shape. We want $f_i$ large for small $i$ (to allow large $d_i^+$... wait, for small $i$, $i - 1$ is small, so $d_i^+$ is limited by $i - 1$ anyway).

Actually, for player $i$, the max $d_i^+$ is $i - 1$ (can't upset more than $i - 1$ players above). This is achieved when $f_i \geq 2i - 1 - N$.

For large $i$ (near $N$), $i - 1$ is large, so the binding constraint is $f_i + N - i$. We need $f_i$ large enough.

$\sum d_i^+ \leq \sum (i - 1) = \binom{N}{2}$, but we also need $\sum d_i^- = \sum d_i^+$ and $d_i^- \leq N - i$.

So $U = \sum d_i^+ = \sum d_i^- \leq \sum (N - i) = \binom{N}{2}$. Both give the same trivial bound.

The real constraint is the non-increasing $w_i$.

Let me try to think about it as: we want $w_i = (N - i) + f_i$ non-increasing, $\sum f_i = 0$, $f_{i+1} \leq f_i + 1$, and $U = \sum d_i^+$ where $d_i^+ \leq \min(i - 1, f_i + N - i)$.

To maximize $U$, ideally $d_i^+ = \min(i - 1, f_i + N - i)$ for all $i$. This requires that we can actually realize such $d_i^+$ and $d_i^-$ with a valid tournament. Let me first find the upper bound assuming we can.

$U \leq \sum_i \min(i - 1, f_i + N - i)$.

We want to maximize this over valid $f$.

Let $g_i = \min(i - 1, f_i + N - i)$. We want $\sum g_i$ max.

For $f_i \geq 2i - 1 - N$: $g_i = i - 1$ (saturated).
For $f_i < 2i - 1 - N$: $g_i = f_i + N - i$.

To maximize, we want all $g_i = i - 1$, i.e., $f_i \geq 2i - 1 - N$ for all $i$. Then $U \leq \binom{N}{2}$, but we also need $\sum f_i = 0$ and $f_{i+1} \leq f_i + 1$ and $f_i \leq i - 1$.

$f_i \geq 2i - 1 - N$ and $f_i \leq i - 1$. For $i$ near $N$, $2i - 1 - N \approx i - 1$, so $f_i \approx i - 1$. For $i = N$, $f_N \geq N - 1$ and $f_N \leq N - 1$, so $f_N = N - 1$. Then $f_{N-1} \geq f_N - ? $... wait, the constraint is $f_{i+1} \leq f_i + 1$, i.e., $f_i \geq f_{i+1} - 1$. So $f_{N-1} \geq f_N - 1 = N - 2$. And $f_{N-1} \leq N - 2$. So $f_{N-1} = N - 2$. By induction, $f_i = i - 1$ for all $i$. Then $\sum f_i = \sum (i-1) = \binom{N}{2} \neq 0$ (for $N \geq 2$). Contradiction.

So we can't have all saturated. We need $\sum f_i = 0$, which means some $f_i$ must be negative (for large enough $N$).

OK so the problem is: maximize $\sum \min(i - 1, f_i + N - i)$ subject to $\sum f_i = 0$, $f_{i+1} \leq f_i + 1$, $i - N \leq f_i \leq i - 1$.

Let me substitute $f_i = (i - 1) - h_i$ where $h_i \geq 0$ (since $f_i \leq i - 1$) and $h_i \leq N - 1$ (since $f_i \geq i - N$, so $h_i \leq N - 1$). Then:

$g_i = \min(i - 1, (i - 1) - h_i + N - i) = \min(i - 1, N - 1 - h_i)$.

$\sum f_i = \sum (i - 1) - \sum h_i = \binom{N}{2} - \sum h_i = 0 \Rightarrow \sum h_i = \binom{N}{2}$.

$f_{i+1} \leq f_i + 1 \Rightarrow (i) - h_{i+1} \leq (i - 1) - h_i + 1 \Rightarrow -h_{i+1} \leq -h_i \Rightarrow h_{i+1} \geq h_i$.

So $h$ is non-decreasing! And $0 \leq h_i \leq N - 1$, $\sum h_i = \binom{N}{2}$, $h$ non-decreasing.

$g_i = \min(i - 1, N - 1 - h_i)$.

$U \leq \sum g_i = \sum \min(i - 1, N - 1 - h_i)$.

We want to maximize this. Since $h$ is non-decreasing and $\sum h_i = \binom{N}{2} = \frac{N(N-1)}{2}$, and $h_i \leq N - 1$...

Note $\sum (N-1) = N(N-1) = 2\binom{N}{2}$. So $\sum h_i = \binom{N}{2}$ means on average $h_i = (N-1)/2$.

$g_i = \min(i - 1, N - 1 - h_i)$. We want to maximize $\sum g_i$.

Since $h$ is non-decreasing, $N - 1 - h_i$ is non-increasing. And $i - 1$ is increasing. So $g_i = \min(\text{increasing}, \text{non-increasing})$. The min is maximized when the two cross as late/high as possible.

$\sum g_i = \sum \min(i - 1, N - 1 - h_i)$.

To maximize, we want $h_i$ small for small $i$ (so $N - 1 - h_i$ is large, but $i - 1$ is the binding constraint there) and... actually for small $i$, $i - 1$ is small so $g_i = i - 1$ regardless (as long as $N - 1 - h_i \geq i - 1$, i.e., $h_i \leq N - i$). For large $i$, $N - 1 - h_i$ might be binding.

Let me think about it. $g_i = i - 1$ if $h_i \leq N - i$, and $g_i = N - 1 - h_i$ if $h_i \geq N - i$.

Since $h$ is non-decreasing and $N - i$ is decreasing, there's a crossover point. For $i \leq k$, $h_i \leq N - i$ (so $g_i = i - 1$), and for $i > k$, $h_i \geq N - i$ (so $g_i = N - 1 - h_i$).

$U \leq \sum_{i=1}^{k} (i - 1) + \sum_{i=k+1}^{N} (N - 1 - h_i) = \binom{k}{2} + (N - k)(N - 1) - \sum_{i=k+1}^{N} h_i$.

We have $\sum h_i = \binom{N}{2}$, so $\sum_{i=k+1}^{N} h_i = \binom{N}{2} - \sum_{i=1}^{k} h_i$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + \sum_{i=1}^k h_i$.

To maximize, we want $\sum_{i=1}^k h_i$ as large as possible. But $h$ is non-decreasing and $h_i \leq N - i$ for $i \leq k$ (to stay in the $g_i = i-1$ regime). So $h_i \leq N - i$ for $i \leq k$, and $h$ non-decreasing means $h_1 \leq h_2 \leq \cdots \leq h_k \leq N - k$ (the tightest constraint is $h_k \leq N - k$).

So $\sum_{i=1}^k h_i \leq k \cdot (N - k)$ (since all $\leq N - k$ and non-decreasing, max is all equal to $N - k$... wait, non-decreasing means $h_1 \leq \cdots \leq h_k$, and each $\leq N - i$. The binding constraint is $h_i \leq N - i$. Since $h$ is non-decreasing, $h_i \leq h_k \leq N - k$ for $i \leq k$. But also $h_i \leq N - i \geq N - k$ for $i \leq k$. So the binding constraint is $h_k \leq N - k$, and $h_i \leq N - i$ which is $\geq N - k$. So actually $h_i \leq N - i$ for each $i$, and since $h$ is non-decreasing, the max of $\sum_{i=1}^k h_i$ is achieved when $h_i = N - i$ for $i = 1, \ldots, k$? No, that's decreasing. $h$ must be non-decreasing.

Hmm, $h$ non-decreasing and $h_i \leq N - i$ (decreasing bound). So $h_k \leq N - k$ is the tightest. And $h_i \leq h_k \leq N - k$ for $i \leq k$. But $h_i \leq N - i \geq N - k$ is automatically satisfied if $h_i \leq N - k$. So the constraint is $h_i \leq N - k$ for $i \leq k$ (from non-decreasing + $h_k \leq N - k$).

Wait, no. $h_i \leq N - i$ is required for $g_i = i - 1$. For $i \leq k$, we need $h_i \leq N - i$. Since $h$ is non-decreasing, $h_i \leq h_k \leq N - k \leq N - i$ (for $i \leq k$). So if $h_k \leq N - k$, then automatically $h_i \leq N - i$ for all $i \leq k$. Good.

So $\sum_{i=1}^k h_i \leq k(N - k)$ (each $h_i \leq N - k$, and they're non-decreasing, so max sum is $k(N-k)$ when all equal $N - k$).

But wait, we also need $h_i \geq 0$ and $h$ non-decreasing overall, and $\sum h_i = \binom{N}{2}$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + k(N-k)$.

$= \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + k(N-k)$

$= \binom{k}{2} + (N-k)(N-1+k) - \binom{N}{2}$

$= \binom{k}{2} + (N-k)(N-1+k) - \binom{N}{2}$

Let me expand: $(N-k)(N-1+k) = N^2 - N + Nk - Nk + k - k^2 = N^2 - N + k - k^2$. 

Hmm let me redo: $(N-k)(N-1+k) = N(N-1+k) - k(N-1+k) = N^2 - N + Nk - kN + k - k^2 = N^2 - N + k - k^2$.

$\binom{k}{2} = k(k-1)/2$. $\binom{N}{2} = N(N-1)/2$.

$U \leq \frac{k(k-1)}{2} + N^2 - N + k - k^2 - \frac{N(N-1)}{2}$

$= \frac{k^2 - k}{2} + N^2 - N + k - k^2 - \frac{N^2 - N}{2}$

$= \frac{k^2 - k - N^2 + N}{2} + N^2 - N + k - k^2$

$= \frac{k^2 - k - N^2 + N}{2} + \frac{2N^2 - 2N + 2k - 2k^2}{2}$

$= \frac{k^2 - k - N^2 + N + 2N^2 - 2N + 2k - 2k^2}{2}$

$= \frac{-k^2 + k + N^2 - N}{2}$

$= \frac{N^2 - N - k^2 + k}{2}$

$= \frac{N(N-1) - k(k-1)}{2}$

$= \binom{N}{2} - \binom{k}{2}$.

So $U \leq \binom{N}{2} - \binom{k}{2}$ where $k$ is the crossover point. To maximize, we want $k$ as small as possible.

But $k$ can't be too small. We need the constraints to be satisfiable. Specifically, we need $h$ non-decreasing, $0 \leq h_i \leq N - 1$, $\sum h_i = \binom{N}{2}$, and $h_k \leq N - k$ (for the crossover to be at $k$).

Also, for $i > k$, $h_i \geq N - i$ (to be in the regime $g_i = N - 1 - h_i$). And $h_i \leq N - 1$.

$\sum_{i=k+1}^N h_i = \binom{N}{2} - \sum_{i=1}^k h_i$. With $\sum_{i=1}^k h_i = k(N-k)$ (max), $\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k) = \frac{N(N-1) - 2k(N-k)}{2} = \frac{N(N-1) - 2kN + 2k^2}{2} = \frac{(N-k)(N-1-2k) + 2k^2 - k... }$. Let me just compute: $\frac{N^2 - N - 2kN + 2k^2}{2} = \frac{(N-k)^2 - (N - 2k) \cdot ... }$. Actually $\frac{N^2 - N - 2kN + 2k^2}{2} = \frac{(N - 2k + ?)... }$. Let me factor: $N^2 - 2kN + 2k^2 - N = (N - k)^2 + k^2 - N$. Hmm, not clean. Let me just leave it.

For $i > k$, we need $h_i \geq N - i$ and $h_i \leq N - 1$, and $h$ non-decreasing. The number of terms is $N - k$.

$\sum_{i=k+1}^N h_i \geq \sum_{i=k+1}^N (N - i) = \sum_{j=0}^{N-k-1} j = \binom{N-k}{2}$ (where $j = N - i$, $i$ from $k+1$ to $N$, $j$ from $N-k-1$ to $0$).

Also $\sum_{i=k+1}^N h_i \leq (N - k)(N - 1)$ (each $\leq N - 1$).

We need $\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k)$ (when $\sum_{i=1}^k h_i = k(N-k)$).

Check feasibility: $\binom{N}{2} - k(N-k) \geq \binom{N-k}{2}$?

$\frac{N(N-1)}{2} - k(N-k) \geq \frac{(N-k)(N-k-1)}{2}$

$\frac{N(N-1) - (N-k)(N-k-1)}{2} \geq k(N-k)$

$N(N-1) - (N-k)(N-k-1) \geq 2k(N-k)$

$N^2 - N - (N^2 - 2kN + k^2 - N + k) \geq 2kN - 2k^2$

$2kN - k^2 - k \geq 2kN - 2k^2$

$-k^2 - k \geq -2k^2$

$k^2 - k \geq 0$

$k(k-1) \geq 0$, true for $k \geq 1$. ✓

Also need $\binom{N}{2} - k(N-k) \leq (N-k)(N-1)$:

$\frac{N(N-1)}{2} - k(N-k) \leq (N-k)(N-1)$

$\frac{N(N-1)}{2} \leq k(N-k) + (N-k)(N-1) = (N-k)(k + N - 1) = (N-k)(N + k - 1)$

$\frac{N(N-1)}{2} \leq (N-k)(N+k-1) = N^2 + Nk - N - kN - k^2 + k = N^2 - N - k^2 + k$

$\frac{N(N-1)}{2} \leq N(N-1) - k(k-1)$

$k(k-1) \leq \frac{N(N-1)}{2}$

True for $k \leq N - 1$ (roughly). ✓

Also need $h$ non-decreasing across the boundary: $h_k \leq h_{k+1}$. $h_k = N - k$ (we set it to max), and $h_{k+1} \geq N - (k+1) = N - k - 1$. So we need $h_{k+1} \geq N - k$. But $h_{k+1} \leq N - 1$. So $N - k \leq h_{k+1} \leq N - 1$. This requires $N - k \leq N - 1$, i.e., $k \geq 1$. ✓

But we also need $h_{k+1} \geq h_k = N - k$ and $h_{k+1} \geq N - k - 1$ (the regime constraint). The binding one is $h_{k+1} \geq N - k$.

So the crossover $k$ can be as small as... we need $k \geq 1$ and the sum constraints to work. Let me check $k = 1$:

$U \leq \binom{N}{2} - \binom{1}{2} = \binom{N}{2} - 0 = \binom{N}{2}$. That would mean all edges are upsets, but that gives $w = (0, 1, \ldots, N-1)$, which is increasing, not non-increasing. So something's wrong.

The issue is that when $k = 1$, we need $h_1 = N - 1$ (max), and $h_i \geq N - i$ for $i \geq 2$, with $\sum h_i = \binom{N}{2}$. $h_1 = N - 1$, $\sum_{i=2}^N h_i = \binom{N}{2} - (N-1) = \frac{N(N-1) - 2(N-1)}{2} = \frac{(N-1)(N-2)}{2} = \binom{N-1}{2}$. And $\sum_{i=2}^N (N - i) = \binom{N-1}{2}$. So $h_i = N - i$ for $i \geq 2$. But $h$ must be non-decreasing: $h_1 = N - 1$, $h_2 = N - 2 < N - 1$. Not non-decreasing! ✗

So $k = 1$ doesn't work because $h$ must be non-decreasing but $h_1 = N - 1 > h_2 = N - 2$.

The non-decreasing constraint on $h$ is crucial. Let me redo the analysis.

$h$ non-decreasing, $h_i \leq N - i$ for $i \leq k$, $h_i \geq N - i$ for $i > k$. Since $h$ is non-decreasing and $N - i$ is decreasing, the condition $h_i \leq N - i$ for $i \leq k$ and $h_i \geq N - i$ for $i > k$ means the crossover happens where $h$ crosses $N - i$ from below.

Since $h$ is non-decreasing and $N - i$ is strictly decreasing, they can cross at most once. So there's a unique crossover point $k$ where $h_k \leq N - k$ and $h_{k+1} \geq N - k - 1$... actually $h_{k+1} \geq N - (k+1) = N - k - 1$.

But we also need $h_k \leq h_{k+1}$ (non-decreasing). And $h_k \leq N - k$, $h_{k+1} \geq N - k - 1$.

Now, the key constraint I missed: $h$ non-decreasing means $h_1 \leq h_2 \leq \cdots \leq h_k \leq N - k$ (since $h_k \leq N - k$ and non-decreasing means all earlier are $\leq h_k \leq N - k$). But also $h_i \leq N - i$ for each $i \leq k$, which is $\geq N - k$, so the binding constraint is $h_k \leq N - k$.

For $i > k$: $h_i \geq N - i$ and $h_i \leq N - 1$ and non-decreasing. The minimum values are $h_i = N - i$ but these are decreasing, contradicting non-decreasing. So we need $h_i \geq h_{i-1}$ for $i > k$.

Actually, for $i > k$, $h_i \geq \max(N - i, h_{i-1})$. Since $h$ is non-decreasing, $h_{k+1} \geq h_k$, $h_{k+2} \geq h_{k+1}$, etc. And $h_{k+1} \geq N - k - 1$.

The minimum non-decreasing sequence with $h_i \geq N - i$ for $i > k$ is: $h_{k+1} = \max(N - k - 1, h_k)$, $h_{k+2} = \max(N - k - 2, h_{k+1})$, etc. Since $N - i$ is decreasing and $h$ is non-decreasing, once $h_{k+1} \geq N - k - 1$, the non-decreasing property ensures $h_i \geq h_{k+1} \geq N - k - 1 \geq N - i$ for $i \geq k + 1$ (since $N - i \leq N - k - 1$). So the binding constraint is just $h_{k+1} \geq N - k - 1$ and non-decreasing.

So for $i > k$, the minimum is $h_i = h_{k+1}$ for all $i > k$ (constant), with $h_{k+1} \geq \max(N - k - 1, h_k)$.

Now, $\sum h_i = \sum_{i=1}^k h_i + \sum_{i=k+1}^N h_i = \binom{N}{2}$.

To maximize $U = \binom{N}{2} - \binom{k}{2}$, we want $k$ minimal. But we need feasibility.

Let me set $h_1 = \cdots = h_k = a$ (constant, non-decreasing, $\leq N - k$) and $h_{k+1} = \cdots = h_N = b$ (constant, non-decreasing, $\geq N - k - 1$). With $a \leq b$.

$\sum h_i = ka + (N-k)b = \binom{N}{2}$.

$U = \binom{N}{2} - \binom{k}{2}$ (from the formula, assuming the crossover is exactly at $k$).

Wait, but I need to re-derive $U$ more carefully with the non-decreasing constraint.

Actually, let me reconsider. The formula $U \leq \binom{N}{2} - \binom{k}{2}$ was derived assuming $\sum_{i=1}^k h_i = k(N-k)$ (maximum). But with the non-decreasing constraint, the maximum of $\sum_{i=1}^k h_i$ is $k \cdot \min(N-k, \text{something})$. Since $h_i \leq h_k \leq N - k$ and non-decreasing, max is $h_i = N - k$ for all $i \leq k$, giving $\sum = k(N-k)$. But we also need $h_k \leq h_{k+1}$, and $h_{k+1} \leq N - 1$. So $h_k = N - k \leq h_{k+1} \leq N - 1$, requiring $N - k \leq N - 1$, i.e., $k \geq 1$. Fine.

But we also need $\sum h_i = \binom{N}{2}$ and $h_{k+1} \geq N - k$ (from $h_{k+1} \geq h_k = N - k$). And $h_{k+1} \leq N - 1$.

$\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k)$. With $h_{k+1} = \cdots = h_N = b$, $(N-k)b = \binom{N}{2} - k(N-k)$, so $b = \frac{\binom{N}{2} - k(N-k)}{N-k} = \frac{\binom{N}{2}}{N-k} - k = \frac{N(N-1)}{2(N-k)} - k$.

We need $b \geq N - k$ (from non-decreasing + $h_k = N - k$):

$\frac{N(N-1)}{2(N-k)} - k \geq N - k$

$\frac{N(N-1)}{2(N-k)} \geq N$

$N(N-1) \geq 2N(N-k)$

$N - 1 \geq 2(N - k)$

$N - 1 \geq 2N - 2k$

$2k \geq N + 1$

$k \geq \frac{N+1}{2}$.

So $k \geq (N+1)/2$. Since $N$ is odd, $(N+1)/2$ is an integer. So the minimum $k$ is $(N+1)/2$.

Then $U \leq \binom{N}{2} - \binom{(N+1)/2}{2}$.

$\binom{N}{2} - \binom{(N+1)/2}{2} = \frac{N(N-1)}{2} - \frac{\frac{N+1}{2} \cdot \frac{N-1}{2}}{2} = \frac{N(N-1)}{2} - \frac{(N+1)(N-1)}{8} = \frac{4N(N-1) - (N+1)(N-1)}{8} = \frac{(N-1)(4N - N - 1)}{8} = \frac{(N-1)(3N - 1)}{8}$.

For $N = 3$: $\frac{2 \cdot 8}{8} = 2$. ✓ (matches our finding)

For $N = 5$: $\frac{4 \cdot 14}{8} = 7$. So max upsets = 7 out of 10 matches.

Let me verify: $k = 3$, $h_1 = h_2 = h_3 = N - k = 2$, $b = \frac{10}{2} - 3 = 2$. So $h = (2, 2, 2, 2, 2)$. All equal. $f_i = (i-1) - 2 = (−2, −1, 0, 1, 2)$. $w_i = (N-i) + f_i = (4,3,2,1,0) + (−2,−1,0,1,2) = (2, 2, 2, 2, 2)$. Regular tournament! All wins = 2.

$U = \sum d_i^+ = \sum \min(i-1, f_i + N - i) = \sum \min(i-1, (i-1) - 2 + 5 - i) = \sum \min(i-1, 2)$.

$i=1$: $\min(0, 2) = 0$. $i=2$: $\min(1, 2) = 1$. $i=3$: $\min(2, 2) = 2$. $i=4$: $\min(3, 2) = 2$. $i=5$: $\min(4, 2) = 2$.

$U = 0 + 1 + 2 + 2 + 2 = 7$. ✓

So the upper bound is $\frac{(N-1)(3N-1)}{8}$, achieved by a regular tournament where all $w_i = (N-1)/2$.

But wait, I need to verify that such a tournament actually exists (i.e., the upset pattern is realizable). We need a regular tournament on $N$ vertices (odd) where the number of backward edges is exactly $\frac{(N-1)(3N-1)}{8}$.

In the construction above, $d_i^+ = \min(i-1, (N-1)/2)$ and $d_i^- = d_i^+ - f_i = \min(i-1, (N-1)/2) - ((i-1) - (N-1)/2)$.

For $i \leq (N+1)/2$: $d_i^+ = i - 1$, $d_i^- = (i-1) - (i - 1 - (N-1)/2) = (N-1)/2$. So player $i$ upsets all $i - 1$ players above and is upset by $(N-1)/2$ players below. Total wins: $(N - i) - (N-1)/2 + (i - 1) = (N - 1)/2$. ✓

For $i > (N+1)/2$: $d_i^+ = (N-1)/2$, $d_i^- = (N-1)/2 - (i - 1 - (N-1)/2) = (N-1) - (i-1) = N - i$. So player $i$ upsets $(N-1)/2$ players above and is upset by all $N - i$ players below. Wins: $(N-i) - (N-i) + (N-1)/2 = (N-1)/2$. ✓

So the structure is:
- For $i \leq (N+1)/2$: player $i$ beats everyone above (all upsets), and beats $(N-1)/2 - (i-1) = (N+1)/2 - i$ players below (non-upsets), loses to $(N-1)/2$ players below (upsets). Wait, let me recount. Player $i$ has $N - i$ players below. $d_i^- = (N-1)/2$ of those are upsets (they beat $i$), so $i$ beats $(N - i) - (N-1)/2 = (N - 2i + 1)/2$ players below. For $i = 1$: $(N-1)/2$. For $i = (N+1)/2$: $0$.

- For $i > (N+1)/2$: player $i$ beats $(N-1)/2$ players above (upsets) and $0$ players below (all below beat them, all upsets). $d_i^- = N - i$ (all below are upsets).

So the tournament structure:
- Players $1, \ldots, (N+1)/2$: each beats all players above them, and beats some players below.
- Players $(N+1)/2 + 1, \ldots, N$: each beats $(N-1)/2$ players above, loses to all below.

This is a specific kind of regular tournament. We need to verify it exists.

Let me think of it as: the "upper half" $A = \{1, \ldots, (N+1)/2\}$ and "lower half" $B = \{(N+1)/2 + 1, \ldots, N\}$. $|A| = (N+1)/2$, $|B| = (N-1)/2$.

Within $A$: player $i$ beats all players above (in $A$). So within $A$, it's a transitive tournament: $1 \to 2 \to \cdots \to (N+1)/2$. Player $i \in A$ beats $i - 1$ players in $A$ (those above) and loses to $(N+1)/2 - i$ players in $A$ (those below).

Between $A$ and $B$: Player $i \in A$ needs total wins $(N-1)/2$. Within $A$, wins = $i - 1$. So wins against $B$ = $(N-1)/2 - (i-1) = (N+1)/2 - i$. Player $i$ beats $(N+1)/2 - i$ players in $B$ (out of $|B| = (N-1)/2$).

For $i = 1$: beats $(N-1)/2$ players in $B$, i.e., all of $B$. For $i = (N+1)/2$: beats $0$ in $B$.

Within $B$: player $j \in B$ needs total wins $(N-1)/2$. Against $A$: player $j$ beats $(N-1)/2 - (\text{wins in } B)$ players in $A$. Wins in $B$: player $j$ loses to all below in $B$ (all upsets, $d_j^- = N - j$), so wins in $B$ = $|B| - 1 - (N - j) = (N-1)/2 - 1 - N + j = j - (N+1)/2 - 1 + 1 = j - (N+1)/2 - 1$... let me recompute.

$|B| = (N-1)/2$. Player $j \in B$, $j > (N+1)/2$. Within $B$, player $j$ beats those below in $B$... no, $d_j^- = N - j$ means all $N - j$ players below beat $j$. Players below $j$ in $B$: those in $B$ with index $> j$, count = $N - j$. So all of them beat $j$. Players above $j$ in $B$: $j - (N+1)/2 - 1$ players. $j$ beats all of them (since within $B$, lower index beats higher index, transitive). So wins in $B$ = $j - (N+1)/2 - 1$.

Hmm, for $j = (N+1)/2 + 1$: wins in $B$ = $0$. For $j = N$: wins in $B$ = $N - (N+1)/2 - 1 = (N-1)/2 - 1 = |B| - 1$. So within $B$, it's transitive: $(N+1)/2 + 1 \to \cdots \to N$.

Wins against $A$ = $(N-1)/2 - (j - (N+1)/2 - 1) = (N-1)/2 - j + (N+1)/2 + 1 = N - j + (N+1)/2 + 1 - (N+1)/2 = N + 1 - j + (N-1)/2 - (N+1)/2$... let me just compute directly.

Player $j \in B$, total wins = $(N-1)/2$. Wins in $B$ = $j - (N+1)/2 - 1$ (beats all above in $B$, which is a transitive tournament). So wins against $A$ = $(N-1)/2 - (j - (N+1)/2 - 1) = (N-1)/2 - j + (N+1)/2 + 1 = N + 1 - j$.

For $j = (N+1)/2 + 1$: wins against $A$ = $N + 1 - (N+1)/2 - 1 = (N-1)/2 = |A| - 1$. So beats all of $A$ except one.
For $j = N$: wins against $A$ = $1$. Beats 1 player in $A$.

Now, between $A$ and $B$: player $i \in A$ beats $(N+1)/2 - i$ players in $B$. Player $j \in B$ beats $N + 1 - j$ players in $A$.

Check: $\sum_{i \in A} (\text{wins against } B) = \sum_{i=1}^{(N+1)/2} ((N+1)/2 - i) = \sum_{k=0}^{(N-1)/2} k = \binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$.

$\sum_{j \in B} (\text{wins against } A) = \sum_{j=(N+1)/2+1}^{N} (N + 1 - j) = \sum_{k=1}^{(N-1)/2} k = \binom{(N-1)/2 + 1}{2} = \binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$.

These should be complementary: wins of $A$ against $B$ + wins of $B$ against $A$ = $|A| \cdot |B| = \frac{N+1}{2} \cdot \frac{N-1}{2} = \frac{(N+1)(N-1)}{4}$.

$\frac{(N+1)(N-1)}{8} + \frac{(N+1)(N-1)}{8} = \frac{(N+1)(N-1)}{4}$. ✓

Now we need to verify that a bipartite tournament between $A$ and $B$ with these degree sequences exists. Player $i \in A$ beats $r_i = (N+1)/2 - i$ players in $B$. Player $j \in B$ beats $s_j = N + 1 - j$ players in $A$ (equivalently, loses to $|A| - s_j = (N+1)/2 - (N + 1 - j) = j - (N+1)/2 - 1$... wait, $|A| = (N+1)/2$, $s_j = N + 1 - j$, so loses to $(N+1)/2 - (N+1-j) = j - (N+1)/2 - 1 + (N+1)/2$... let me recompute: $(N+1)/2 - (N+1-j) = (N+1)/2 - N - 1 + j = j - (N+1)/2 - 1$. For $j = (N+1)/2 + 1$: loses to $0$ in $A$... no, $s_j = N + 1 - (N+1)/2 - 1 = (N-1)/2 = |A| - 1$. So beats $|A| - 1$ in $A$, loses to $1$ in $A$. For $j = N$: $s_j = 1$, beats 1, loses to $|A| - 1 = (N-1)/2$.

So the "losses in $A$" for player $j \in B$ is $|A| - s_j = (N+1)/2 - (N+1-j) = j - (N+1)/2 - 1 + 1 - 1$... ugh. $(N+1)/2 - N - 1 + j = j - (N+1)/2 - 1$. For $j = (N+1)/2 + 1$: $0$. For $j = N$: $(N-1)/2 - 1$.

And $r_i = (N+1)/2 - i$ for $i \in A$. For $i = 1$: $(N-1)/2 = |B|$. For $i = (N+1)/2$: $0$.

So player 1 beats all of $B$, player $(N+1)/2$ beats none of $B$. Player $(N+1)/2 + 1$ loses to none of $A$ (beats all of $A$ except... wait, $s_j = |A| - 1$, so beats $|A| - 1$ players in $A$, loses to 1). Player $N$ beats 1 in $A$.

The bipartite tournament: We need a bipartite graph where $i \in A$ has degree $r_i$ (beats $r_i$ in $B$) and $j \in B$ has "loss degree" $|A| - s_j$ (loses to that many in $A$). 

The loss degrees from $B$ side: player $j$ loses to $j - (N+1)/2 - 1$... hmm wait, I think I need to be more careful. Let me re-derive.

Player $j \in B$ beats $s_j = N + 1 - j$ players in $A$. So $j$ loses to $|A| - s_j = (N+1)/2 - (N+1-j) = j - (N+1)/2 - 1$... 

$(N+1)/2 - N - 1 + j = j - (N+1)/2 - 1$. For $j = (N+3)/2$ (smallest in $B$): $(N+3)/2 - (N+1)/2 - 1 = 1 - 1 = 0$. For $j = N$: $N - (N+1)/2 - 1 = (N-1)/2 - 1 = (N-3)/2$.

So the "losses to $A$" for $B$ players: $0, 1, 2, \ldots, (N-3)/2$. These are $r_i$ values reversed!

$r_i$ for $A$ players: $(N-1)/2, (N-3)/2, \ldots, 1, 0$ (for $i = 1, 2, \ldots, (N+1)/2$).

Losses to $A$ for $B$ players: $0, 1, \ldots, (N-3)/2$ (for $j = (N+3)/2, \ldots, N$).

So we need a bipartite graph between $A$ (size $(N+1)/2$) and $B$ (size $(N-1)/2$) where $A$-side degrees are $(N-1)/2, (N-3)/2, \ldots, 0$ and $B$-side degrees (losses) are $0, 1, \ldots, (N-3)/2$.

Sum of $A$-side degrees: $\sum_{k=0}^{(N-1)/2} k = \binom{(N+1)/2}{2}$. Sum of $B$-side degrees: $\sum_{k=0}^{(N-3)/2} k = \binom{(N-1)/2}{2}$. 

Wait, these should be equal (each edge counted once from each side). $\binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$ and $\binom{(N-1)/2}{2} = \frac{(N-1)(N-3)}{8}$. These are NOT equal! 

$\frac{(N+1)(N-1)}{8} \neq \frac{(N-1)(N-3)}{8}$ for $N \geq 3$.

I think I made an error. Let me recheck.

The $A$-side degree $r_i$ = number of $B$-players that $i$ beats. The $B$-side "loss degree" = number of $A$-players that beat $j$ = number of $A$-players that $j$ loses to. These should sum to the same total (number of $A \to B$ edges).

$\sum_{i \in A} r_i = \sum_{i=1}^{(N+1)/2} ((N+1)/2 - i) = \sum_{k=0}^{(N-1)/2} k = \frac{((N-1)/2)((N+1)/2)}{2} = \frac{(N-1)(N+1)}{8}$.

$\sum_{j \in B} (\text{losses to } A) = \sum_{j=(N+3)/2}^{N} (j - (N+3)/2 + 1 - 1)$... let me just recompute. Losses to $A$ for player $j$ = $|A| - s_j = (N+1)/2 - (N+1-j) = j - (N+1)/2 - 1$.

Wait: $(N+1)/2 - (N + 1 - j) = (N+1)/2 - N - 1 + j = j + (N+1)/2 - N - 1 = j - (N-1)/2 - 1 = j - (N+1)/2$.

Let me be very careful: $(N+1)/2 - (N + 1 - j) = (N+1)/2 - N - 1 + j = j + (N+1)/2 - N - 1 = j - N + (N+1)/2 - 1 = j - N + (N-1)/2 = j - (N+1)/2$.

So losses to $A$ for player $j = (N+3)/2$: $(N+3)/2 - (N+1)/2 = 1$. For $j = N$: $N - (N+1)/2 = (N-1)/2$.

So losses to $A$ for $B$ players: $1, 2, \ldots, (N-1)/2$ (for $j = (N+3)/2, \ldots, N$). That's $(N-1)/2$ values.

Sum: $\sum_{k=1}^{(N-1)/2} k = \binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$. ✓ Now they match!

I made an arithmetic error before. Let me redo: $j$ ranges from $(N+3)/2$ to $N$, that's $(N-1)/2$ players. Losses: $j - (N+1)/2$ for $j = (N+3)/2, \ldots, N$, giving $1, 2, \ldots, (N-1)/2$.

And $r_i$ for $i = 1, \ldots, (N+1)/2$: $(N+1)/2 - i$ for $i = 1, \ldots, (N+1)/2$, giving $(N-1)/2, (N-3)/2, \ldots, 1, 0$. That's $(N+1)/2$ values, sum = $\binom{(N+1)/2}{2}$.

And $B$-side losses: $1, 2, \ldots, (N-1)/2$, sum = $\binom{(N+1)/2}{2}$. ✓

But the $A$-side has $(N+1)/2$ vertices with degrees $(N-1)/2, (N-3)/2, \ldots, 0$, and $B$-side has $(N-1)/2$ vertices with degrees $1, 2, \ldots, (N-1)/2$.

Hmm, the $A$-side has a vertex with degree 0 (player $(N+1)/2$ beats no one in $B$), and the $B$-side has a vertex with degree $(N-1)/2 = |A|$ (player $N$ loses to all of $A$... wait, no, losses to $A$ = $(N-1)/2 = |A|$, so player $N$ loses to all of $A$). And player $(N+3)/2$ loses to 1 in $A$.

Wait, but player $N$ beats $s_N = 1$ in $A$, and loses to $|A| - 1 = (N-1)/2$ in $A$. But I said losses = $(N-1)/2 = |A|$. That's $|A|$, not $|A| - 1$. Contradiction! If losses = $|A|$, then $s_N = 0$, not 1.

Let me recheck. $s_j = N + 1 - j$. $s_N = N + 1 - N = 1$. Losses = $|A| - s_N = (N+1)/2 - 1 = (N-1)/2$. And $j - (N+1)/2 = N - (N+1)/2 = (N-1)/2$. ✓ So losses = $(N-1)/2 = |A| - 1$. And $|A| = (N+1)/2$. So $(N-1)/2 = (N+1)/2 - 1 = |A| - 1$. ✓

I confused myself. Losses to $A$ for player $N$ is $(N-1)/2 = |A| - 1$, not $|A|$. Good.

So the bipartite degree sequences are:
- $A$-side (beats in $B$): $(N-1)/2, (N-3)/2, \ldots, 1, 0$ (for players $1, 2, \ldots, (N+1)/2$).
- $B$-side (losses to $A$): $1, 2, \ldots, (N-1)/2$ (for players $(N+3)/2, \ldots, N$).

$B$-side has $(N-1)/2$ vertices with degrees $1, 2, \ldots, (N-1)/2$. $A$-side has $(N+1)/2$ vertices with degrees $(N-1)/2, \ldots, 1, 0$.

By Gale-Ryser / bipartite graph realization theorem, we need to check if this is realizable. The $A$-side degrees sorted descending: $(N-1)/2, (N-3)/2, \ldots, 0$. The $B$-side degrees sorted descending: $(N-1)/2, (N-3)/2, \ldots, 1$.

Actually, a simple construction: connect player $i \in A$ to the first $r_i$ players in $B$ (or use a Ferrers diagram). Since the degree sequences are "conjugate" in some sense, this should work.

Actually, let me think of a concrete construction. $A = \{1, \ldots, m\}$ where $m = (N+1)/2$, $B = \{m+1, \ldots, N\}$, $|B| = m - 1$.

$r_i = m - i$ for $i = 1, \ldots, m$. So $r_1 = m - 1 = |B|$, $r_m = 0$.
$B$-side losses: $l_j = j - m$ for $j = m+1, \ldots, N$, i.e., $l_{m+k} = k$ for $k = 1, \ldots, m-1$.

Construction: player $i \in A$ beats players $m+1, m+2, \ldots, m + r_i$ in $B$. So player $i$ beats the first $r_i = m - i$ players in $B$.

Player $j = m + k \in B$ is beaten by players $i$ with $r_i \geq k$, i.e., $m - i \geq k$, i.e., $i \leq m - k$. So players $1, 2, \ldots, m - k$ beat player $m + k$. That's $m - k$ players. And $l_{m+k} = k$... but we need $l_{m+k} = k$, and we got $m - k$.

Hmm, that doesn't match. $m - k \neq k$ in general.

Let me try the other direction: player $i$ beats the LAST $r_i$ players in $B$. Player $i$ beats $m + (m-1) - r_i + 1, \ldots, m + (m-1)$, i.e., players $2m - r_i, \ldots, 2m - 1 = N$. Since $r_i = m - i$, player $i$ beats players $2m - (m-i) = m + i, \ldots, N$. So player $i$ beats players $m+i, m+i+1, \ldots, N$ in $B$, which is $N - (m+i) + 1 = N - m - i + 1 = (m - 1) - i + 1 = m - i = r_i$. ✓

Player $j = m + k$ is beaten by players $i$ with $m + i \leq j \leq N$, i.e., $i \leq j - m = k$. So players $1, \ldots, k$ beat player $m + k$. That's $k$ players. And $l_{m+k} = k$. ✓✓

So the construction works. Player $i \in A$ beats players $m + i, m + i + 1, \ldots, N$ in $B$ (and loses to $m + 1, \ldots, m + i - 1$ in $B$).

Let me verify the full tournament for $N = 5$, $m = 3$.

$A = \{1, 2, 3\}$, $B = \{4, 5\}$.

Within $A$: transitive. $1 \to 2, 1 \to 3, 2 \to 3$.
Within $B$: transitive. $4 \to 5$.

Between $A$ and $B$: player $i$ beats $m + i, \ldots, N$.
- Player 1 beats $4, 5$ (i.e., $m+1 = 4$ to $N = 5$). 
- Player 2 beats $5$ (i.e., $m+2 = 5$). Loses to $4$.
- Player 3 beats nobody in $B$ ($m + 3 = 6 > 5$). Loses to $4, 5$.

So edges:
- $1 \to 2, 1 \to 3, 1 \to 4, 1 \to 5$ (4 wins)
- $2 \to 3, 2 \to 5$, $4 \to 2$ (2 wins: 3 and 5)
- $3$: loses to 1, 2; $3 \to ?$ in $B$: loses to 4, 5. So 0 wins? But we need 2 wins!

Wait, that's wrong. Player 3 should have 2 wins. Let me recheck.

Player 3 is in $A$. Within $A$, player 3 loses to 1 and 2 (0 wins in $A$). Against $B$, player 3 beats nobody (loses to 4 and 5). So total wins = 0. But we need $(N-1)/2 = 2$ wins!

Something is wrong with my construction. Let me recheck.

Oh wait, I think the issue is that within $A$, it's NOT transitive in the way I described. Let me re-examine.

For players in $A$ ($i \leq m$): $d_i^+ = i - 1$ (beats all above) and $d_i^- = (N-1)/2 = m - 1$ (loses to $m - 1$ players below). But player $i$ has $N - i$ players below total. Of those, $m - i$ are in $A$ and $m - 1$ are in $B$. So $d_i^- = m - 1$ means player $i$ loses to $m - 1$ players below. But there are only $m - 1$ players in $B$ below, plus $m - i$ in $A$ below.

For $i = 1$: $d_1^- = m - 1 = 2$ (for $N = 5$). Players below 1: 2, 3, 4, 5 (4 players). $d_1^- = 2$ means 2 of these beat player 1. Wins against below: $4 - 2 = 2$. Plus wins against above: 0. Total: 2. ✓

For $i = 3$ (= $m$): $d_3^- = m - 1 = 2$. Players below 3: 4, 5 (2 players). $d_3^- = 2$ means both 4 and 5 beat player 3. Wins against below: 0. Wins against above: $d_3^+ = 2$ (beats players 1 and 2). Total: 2. ✓

Ah, I see! Player 3 beats players 1 and 2 (upsets!), not the other way around. I had the within-$A$ tournament wrong.

Let me redo. Within $A$, player $i$ beats all $i - 1$ players ABOVE (lower index). So it's the REVERSE transitive tournament: $m \to m-1 \to \cdots \to 1$. Player $i$ beats $1, 2, \ldots, i - 1$.

For $N = 5$, $m = 3$:
- Within $A$: $3 \to 2, 3 \to 1, 2 \to 1$. (Player 3 beats 1 and 2, player 2 beats 1.)
- Within $B$: $5 \to 4$ (reverse transitive: $N \to N-1 \to \cdots$). Player $j$ beats all above in $B$: $j$ beats $(N+1)/2 + 1, \ldots, j - 1$.

Wait, within $B$, player $j$ beats all above in $B$ (lower index in $B$). So $5 \to 4$. Player 5 beats 4.

- Between $A$ and $B$: player $i \in A$ beats $m + i, \ldots, N$ in $B$.
  - Player 1 beats 4, 5.
  - Player 2 beats 5, loses to 4.
  - Player 3 loses to 4, 5.

Let me compute wins:
- Player 1: beats 4, 5 (from cross), loses to 2, 3 (within $A$). Wins = 2. ✓
- Player 2: beats 1 (within $A$), beats 5 (cross), loses to 3 (within $A$), loses to 4 (cross). Wins = 2. ✓
- Player 3: beats 1, 2 (within $A$), loses to 4, 5 (cross). Wins = 2. ✓
- Player 4: beats 2, 3 (cross), loses to 1 (cross), loses to 5 (within $B$). Wins = 2. ✓
- Player 5: beats 3, 4 (within $B$ and cross: 5 beats 4 within $B$, and 5 beats 3 cross), loses to 1, 2 (cross). Wins = 2. ✓

All have 2 wins. Now count upsets (higher index beats lower index):
- (1,2): 2 beats 1? Yes (within $A$, 2 → 1). Upset! ✓
- (1,3): 3 beats 1? Yes. Upset! ✓
- (1,4): 4 beats 1? No, 1 beats 4. Not upset.
- (1,5): 5 beats 1? No, 1 beats 5. Not upset.
- (2,3): 3 beats 2? Yes. Upset! ✓
- (2,4): 4 beats 2? Yes. Upset! ✓
- (2,5): 5 beats 2? Yes. Upset! ✓
- (3,4): 4 beats 3? Yes. Upset! ✓
- (3,5): 5 beats 3? Yes. Upset! ✓
- (4,5): 5 beats 4? Yes. Upset! ✓

Upsets: (1,2), (1,3), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5) = 8 upsets!

But we computed the upper bound as 7! Something is wrong.

Wait, let me recount. That's 8 upsets out of 10 matches. But the upper bound was 7. Let me recheck.

Hmm, let me recount the upsets:
- (1,2): 2 beats 1. Upset.
- (1,3): 3 beats 1. Upset.
- (1,4): 1 beats 4. Not upset.
- (1,5): 1 beats 5. Not upset.
- (2,3): 3 beats 2. Upset.
- (2,4): 4 beats 2. Upset.
- (2,5): 5 beats 2. Upset.
- (3,4): 4 beats 3. Upset.
- (3,5): 5 beats 3. Upset.
- (4,5): 5 beats 4. Upset.

That's 8 upsets. But $w = (2, 2, 2, 2, 2)$, non-increasing. Final ranking = 1, 2, 3, 4, 5 = initial. ✓

So 8 upsets is achievable, but my upper bound said 7. I must have made an error in the upper bound derivation.

Let me recheck. $U = \sum d_i^+$. $d_i^+$ = number of upsets where $i$ beats someone above = number of $j < i$ that $i$ beats.

- $d_1^+ = 0$ (nobody above).
- $d_2^+ = 1$ (beats 1).
- $d_3^+ = 2$ (beats 1, 2).
- $d_4^+ = 2$ (beats 2, 3).
- $d_5^+ = 2$ (beats 3, 4).

$U = 0 + 1 + 2 + 2 + 2 = 7$.

But I counted 8 upsets! Let me recheck which are upsets.

An upset is when the winner had a LOWER initial ranking, i.e., higher number. So for pair $(i, j)$ with $i < j$, it's an upset if $j$ beats $i$.

- (1,2): $j = 2$ beats $i = 1$. Upset. This contributes to $d_2^+$.
- (1,3): 3 beats 1. Upset. Contributes to $d_3^+$.
- (1,4): 1 beats 4. Not upset.
- (1,5): 1 beats 5. Not upset.
- (2,3): 3 beats 2. Upset. $d_3^+$.
- (2,4): 4 beats 2. Upset. $d_4^+$.
- (2,5): 5 beats 2. Upset. $d_5^+$.
- (3,4): 4 beats 3. Upset. $d_4^+$.
- (3,5): 5 beats 3. Upset. $d_5^+$.
- (4,5): 5 beats 4. Upset. $d_5^+$.

$d_2^+ = 1$ (beats 1). $d_3^+ = 2$ (beats 1, 2). $d_4^+ = 2$ (beats 2, 3). $d_5^+ = 3$ (beats 2, 3, 4).

Wait, player 5 beats 2, 3, and 4. That's 3 upsets for player 5, not 2!

Let me recheck player 5's wins. Player 5 beats: 4 (within $B$), 3 (cross: 5 beats 3), 2 (cross: 5 beats 2). And loses to 1 (cross: 1 beats 5). So wins = 3, not 2!

I made an error earlier. Let me recompute all wins.

Edges:
- Within $A$ (reverse transitive): $3 \to 2, 3 \to 1, 2 \to 1$.
- Within $B$ (reverse transitive): $5 \to 4$.
- Cross: player $i \in A$ beats $m + i, \ldots, N$.
  - Player 1 beats 4, 5.
  - Player 2 beats 5, loses to 4.
  - Player 3 loses to 4, 5.

So:
- Player 1: beats 4, 5 (cross). Loses to 2, 3 (within $A$). Wins = 2.
- Player 2: beats 1 (within $A$), beats 5 (cross). Loses to 3 (within $A$), loses to 4 (cross). Wins = 2.
- Player 3: beats 1, 2 (within $A$). Loses to 4, 5 (cross). Wins = 2.
- Player 4: beats 2, 3 (cross). Loses to 1 (cross), loses to 5 (within $B$). Wins = 2.
- Player 5: beats 3, 4 (cross: 5 beats 3; within $B$: 5 beats 4). Loses to 1, 2 (cross). Wins = 2.

Wait, does 5 beat 2? Cross edges: player 2 beats 5 (player 2 beats $m + 2 = 5$). So 2 beats 5, not 5 beats 2!

Let me recheck. Cross: player $i \in A$ beats $m + i, \ldots, N$. Player 2 beats $m + 2 = 5$. So 2 → 5. Player 5 does NOT beat 2.

So player 5's wins: beats 4 (within $B$), beats 3 (cross: player 3 loses to 5, since player 3 beats nobody in $B$). Loses to 1 (1 beats 5), loses to 2 (2 beats 5). Wins = 2. ✓

Let me recount upsets:
- (1,2): 2 beats 1. ✓ Upset.
- (1,3): 3 beats 1. ✓ Upset.
- (1,4): 1 beats 4. Not upset.
- (1,5): 1 beats 5. Not upset.
- (2,3): 3 beats 2. ✓ Upset.
- (2,4): 4 beats 2. ✓ Upset.
- (2,5): 2 beats 5. Not upset.
- (3,4): 4 beats 3. ✓ Upset.
- (3,5): 5 beats 3. ✓ Upset.
- (4,5): 5 beats 4. ✓ Upset.

Upsets: (1,2), (1,3), (2,3), (2,4), (3,4), (3,5), (4,5) = 7. ✓

I made an error before (said 5 beats 2, but actually 2 beats 5). So 7 upsets, matching the upper bound. 

So the answer is $\frac{(N-1)(3N-1)}{8}$.

Wait, but I need to double-check my upper bound derivation more carefully, since I want to make sure it's correct.

Let me re-derive. We have $h$ non-decreasing, $0 \leq h_i \leq N-1$, $\sum h_i = \binom{N}{2}$, and $U \leq \sum \min(i-1, N-1-h_i)$.

$g_i = \min(i-1, N-1-h_i)$. Since $h$ is non-decreasing, $N-1-h_i$ is non-increasing. $i-1$ is increasing. So $g_i$ first increases (bounded by $i-1$) then decreases (bounded by $N-1-h_i$).

Let $k$ be the largest index where $i - 1 \leq N - 1 - h_i$, i.e., $h_i \leq N - i$. For $i \leq k$, $g_i = i - 1$. For $i > k$, $g_i = N - 1 - h_i$.

$U \leq \sum_{i=1}^k (i-1) + \sum_{i=k+1}^N (N-1-h_i) = \binom{k}{2} + (N-k)(N-1) - \sum_{i=k+1}^N h_i$.

$\sum_{i=k+1}^N h_i = \binom{N}{2} - \sum_{i=1}^k h_i$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + \sum_{i=1}^k h_i$.

Now, $\sum_{i=1}^k h_i \leq ?$. Since $h$ is non-decreasing and $h_k \leq N - k$ (by definition of $k$), we have $h_i \leq h_k \leq N - k$ for $i \leq k$. So $\sum_{i=1}^k h_i \leq k(N-k)$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + k(N-k) = \binom{N}{2} - \binom{k}{2}$ (as computed before).

Now, to minimize $k$ (maximize $U$), we need the constraints to be feasible. The key constraint is that we need $h$ non-decreasing with $h_k \leq N - k$ and $h_{k+1} \geq N - (k+1) = N - k - 1$ (by definition of $k$, $h_{k+1} > N - (k+1)$... actually $h_{k+1} \geq N - (k+1) + 1$? No, $k$ is the largest where $h_k \leq N - k$, so $h_{k+1} > N - (k+1)$, i.e., $h_{k+1} \geq N - k$).

And $h_k \leq h_{k+1}$ (non-decreasing), so $h_k \leq h_{k+1}$, with $h_k \leq N - k$ and $h_{k+1} \geq N - k$. So $h_k \leq N - k \leq h_{k+1}$. This is consistent.

Now, $\sum h_i = \binom{N}{2}$. We need to find the minimum $k$ such that a non-decreasing sequence $h$ exists with $h_k \leq N - k$, $h_{k+1} \geq N - k$, $0 \leq h_i \leq N - 1$, and $\sum h_i = \binom{N}{2}$.

To minimize $k$, we want to push as much "mass" to the first $k$ terms as possible (making $k$ small) while keeping $h$ non-decreasing and $h_k \leq N - k$.

The maximum $\sum_{i=1}^k h_i$ with $h$ non-decreasing and $h_k \leq N - k$ is $k(N-k)$ (all equal to $N - k$). Then $\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k)$.

For $i > k$, $h$ is non-decreasing with $h_{k+1} \geq N - k$ and $h_i \leq N - 1$. The minimum sum for $i > k$ is $(N-k)(N-k)$ (all equal to $N - k$). We need $\binom{N}{2} - k(N-k) \geq (N-k)(N-k)$, i.e., $\binom{N}{2} \geq (N-k) \cdot k + (N-k)^2 = (N-k)(k + N - k) = N(N-k)$.

$\binom{N}{2} \geq N(N-k) \Leftrightarrow \frac{N-1}{2} \geq N - k \Leftrightarrow k \geq N - \frac{N-1}{2} = \frac{N+1}{2}$.

So $k \geq (N+1)/2$, and the minimum is $k = (N+1)/2$.

At $k = (N+1)/2$: $h_i = N - k = (N-1)/2$ for all $i$ (constant). $\sum h_i = N \cdot (N-1)/2 = \binom{N}{2}$. ✓. And $h$ is non-decreasing (constant). ✓. $h_k = (N-1)/2 = N - k$. ✓.

$U \leq \binom{N}{2} - \binom{(N+1)/2}{2} = \frac{N(N-1)}{2} - \frac{(N+1)(N-1)}{8} = \frac{(N-1)(4N - (N+1))}{8} = \frac{(N-1)(3N-1)}{8}$.

And we showed this is achievable with the regular tournament construction. So the answer is $\frac{(N-1)(3N-1)}{8}$.

But wait, I need to also verify that the upper bound derivation is tight, i.e., that $U = \sum g_i$ is actually achievable (not just an upper bound). In our construction, $d_i^+ = g_i$ for all $i$, and we verified the tournament exists. So yes, it's tight.

Actually, I should also verify that the bound $U \leq \sum g_i$ is correct. We have $d_i^+ \leq \min(i-1, f_i + N - i) = \min(i-1, N - 1 - h_i) = g_i$. So $U = \sum d_i^+ \leq \sum g_i$. ✓

And in the construction, $d_i^+ = g_i$ for all $i$. ✓

Let me also verify for $N = 3$: $\frac{2 \cdot 8}{8} = 2$. ✓ (We found 2 upsets.)

For $N = 7$: $\frac{6 \cdot 20}{8} = 15$. Total matches = 21. So 15 upsets out of 21.

Let me also make sure the construction generalizes. For general odd $N$, $m = (N+1)/2$:

- Within $A = \{1, \ldots, m\}$: reverse transitive. Player $i$ beats $1, \ldots, i-1$.
- Within $B = \{m+1, \ldots, N\}$: reverse transitive. Player $j$ beats $m+1, \ldots, j-1$.
- Cross: player $i \in A$ beats $m+i, \ldots, N$ in $B$.

Each player has $(N-1)/2$ wins (regular tournament). The number of upsets is $\frac{(N-1)(3N-1)}{8}$.

Let me verify the cross edges more carefully. Player $i \in A$ beats $m + i, m + i + 1, \ldots, N$ in $B$. Number of such players: $N - (m + i) + 1 = N - m - i + 1 = (N - 1)/2 - i + 1 = (N + 1)/2 - i = m - i$. And $r_i = m - i$. ✓

Player $j = m + k \in B$ (where $k = 1, \ldots, (N-1)/2$) is beaten by players $i$ with $m + i \leq j$, i.e., $i \leq k$. So players $1, \ldots, k$ beat player $j$. Player $j$ loses to $k$ players in $A$ and beats $m - 1 - k$ players in $A$ (those $i$ with $i > k$, i.e., $i = k+1, \ldots, m$). Wait, $|A| = m$, and $k$ beat $j$, so $m - k$ lose to $j$, i.e., $j$ beats $m - k$ in $A$.

Player $j$'s total wins: wins in $B$ + wins against $A$. Wins in $B$: $j$ beats $m+1, \ldots, j-1$ (reverse transitive), that's $j - m - 1 = k - 1$ wins. Wins against $A$: $m - k$. Total: $(k - 1) + (m - k) = m - 1 = (N-1)/2$. ✓

Great, the construction works for all odd $N \geq 3$.

Now let me also make sure the upper bound proof is complete. I need to show that for ANY tournament with final ranking = initial ranking, $U \leq \frac{(N-1)(3N-1)}{8}$.

The key steps:
1. Define $f_i = d_i^+ - d_i^-$, so $w_i = (N-i) + f_i$.
2. Non-increasing $w$ gives $f_{i+1} \leq f_i + 1$.
3. $\sum f_i = 0$.
4. $d_i^+ \leq \min(i-1, f_i + N - i)$ (from $d_i^+ \leq i - 1$ and $d_i^+ = f_i + d_i^- \leq f_i + (N - i)$).
5. Let $h_i = (i-1) - f_i$, so $h$ is non-decreasing, $\sum h_i = \binom{N}{2}$, $0 \leq h_i \leq N-1$.
6. $d_i^+ \leq \min(i-1, N - 1 - h_i) = g_i$.
7. $U \leq \sum g_i$.
8. With crossover at $k$: $U \leq \binom{N}{2} - \binom{k}{2}$, and $k \geq (N+1)/2$.
9. So $U \leq \binom{N}{2} - \binom{(N+1)/2}{2} = \frac{(N-1)(3N-1)}{8}$.

This is rigorous. The construction achieves equality. So the answer is $\boxed{\frac{(N-1)(3N-1)}{8}}$.

Let me also sanity-check: is this always an integer? $(N-1)(3N-1)$: $N$ odd means $N - 1$ even. $3N - 1$: $N$ odd means $3N$ odd, $3N - 1$ even. So $(N-1)(3N-1)$ is divisible by 4. Is it divisible by 8? $(N-1)/2$ is an integer. $(3N-1)/2$: $3N - 1$ is even, so yes. So $\frac{(N-1)(3N-1)}{8} = \frac{(N-1)/2 \cdot (3N-1)/2}{2}$. We need $(N-1)(3N-1) \equiv 0 \pmod{8}$.

$N$ odd: $N = 2m + 1$. $N - 1 = 2m$, $3N - 1 = 6m + 2 = 2(3m + 1)$. Product: $4m(3m + 1)$. Need $m(3m + 1) \equiv 0 \pmod{2}$. If $m$ even, yes. If $m$ odd, $3m + 1$ is even, yes. So always divisible by 8. ✓

Now let me write up the proof cleanly.

Actually, wait. I want to double-check step 4 more carefully. $d_i^+ \leq f_i + (N - i)$: this comes from $d_i^+ = f_i + d_i^-$ and $d_i^- \leq N - i$ (can't lose to more than $N - i$ players below). ✓

And $d_i^+ \leq i - 1$: can't beat more than $i - 1$ players above. ✓

Also, I should verify that $h_i \geq 0$: $h_i = (i-1) - f_i = (i-1) - (w_i - (N-i)) = (i-1) - w_i + (N-i) = N - 1 - w_i$. Since $w_i \leq N - 1$, $h_i \geq 0$. ✓

And $h_i \leq N - 1$: $h_i = N - 1 - w_i \leq N - 1$ since $w_i \geq 0$. ✓

Good. The proof is complete.

Let me also think about whether I need Landau's theorem or any tournament realizability condition. In the upper bound, I only used the constraints on $d_i^+, d_i^-$, which are necessary conditions. The upper bound holds for any valid tournament. For the lower bound (construction), I explicitly constructed a valid tournament. So no need for Landau's theorem.

Let me write the proof.        — AI历史解题过程（thinking）
#   polymath_00802         — 题目ID

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
  <problem_id>polymath_00802</problem_id>
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

Let $N \geqslant 3$ be an odd integer. $N$ tennis players take part in a league. Before the league starts, a committee ranks the players in some order based on perceived skill. During the league, each pair of players plays exactly one match, and each match has one winner. A match is considered an upset if the winner had a lower initial ranking than the loser. At the end of the league, the players are ranked according to number of wins, with the initial ranking used to rank players with the same number of wins. It turns out that the final ranking is the same as the initial ranking. What is the largest possible number of upsets?
(United Kingdom)

## Standard Solution

Answer: $\frac{(N-1)(3 N-1)}{8}$.
Suppose the players are ranked $1,2, \ldots, N=2 n+1$, where 1 is the highest ranking.
For $k \leqslant n$, the player ranked $k$ could have beaten at most $k-1$ players with a higher ranking. Thus the top $n$ players could have made at most $\sum_{k=1}^{n}(k-1)=\frac{n(n-1)}{2}$ upsets. On the other hand, the average score of all $2 n+1$ players is $n$, so the average score of the bottom $n+1$ players is not more than $n$, which implies that these $n+1$ players have at most $n(n+1)$ wins in total. Hence the total number of upsets is at most

$$
\frac{n(n-1)}{2}+n(n+1)=\frac{n(3 n+1)}{2}=\frac{(N-1)(3 N-1)}{8} .
$$

An example can be constructed as follows. Suppose that, for $1 \leqslant i \leqslant 2 n+1$, the player ranked $i$ beats the players ranked $i-1, i-2, \ldots, i-n$ (the rankings are counted modulo $N)$ and loses to the rest of the players. Thus each player has exactly $n$ wins. The player ranked $i$ for $i \leqslant n$ made $i-1$ upsets, whereas the player ranked $i$ for $i>n$ made $n$ upsets, so the total number of upsets is exactly $\sum_{i=1}^{n}(i-1)+(n+1) n=\frac{n(3 n+1)}{2}$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have $N \geq 3$ odd tennis players. Initial ranking $1, 2, \ldots, N$ (1 = highest). Each pair plays, one winner. An upset is when the lower-ranked player (higher number) beats the higher-ranked player (lower number).

Final ranking is by number of wins, with initial ranking as tiebreaker. Final ranking = initial ranking.

We want to maximize the number of upsets.

Let me denote players $1, 2, \ldots, N$ where $1$ is top-ranked. Player $i$ has $w_i$ wins. Total wins = $\binom{N}{2}$.

Final ranking same as initial means: $w_1 \geq w_2 \geq \cdots \geq w_N$ (with ties broken by initial rank, so if $w_i = w_{i+1}$, then $i$ ranks above $i+1$, consistent).

An upset is when player $j$ beats player $i$ with $j > i$ (lower initial rank wins).

The number of upsets = number of pairs $(i,j)$ with $i < j$ where $j$ beats $i$.

Let me think about what constraints we have.

If there were no upsets, player $i$ beats everyone below, loses to everyone above. So $w_i = N - i$. That's $N-1, N-2, \ldots, 0$. Strictly decreasing, final = initial.

Now we want upsets but final ranking preserved.

Let me think about small cases. $N = 3$. Players 1, 2, 3. Matches: (1,2), (1,3), (2,3).

No upsets: 1 beats 2,3; 2 beats 3. $w = (2,1,0)$. 0 upsets.

Can we have 1 upset? Say 3 beats 2 (upset). Then $w_1 = 2, w_2 = 0, w_3 = 1$. Final ranking: 1 (2 wins), 3 (1 win), 2 (0 wins). That's 1,3,2 ≠ 1,2,3. No good.

Say 2 beats 1 (upset). Then 1 beats 3, 2 beats 3. $w = (1, 2, 0)$. Final: 2,1,3 ≠ 1,2,3. No.

Say 3 beats 1 (upset). Then 1 beats 2, 2 beats 3. $w = (1, 1, 1)$. Tie broken by initial: 1,2,3. Yes! Final = initial. 1 upset.

Can we have 2 upsets? Say 3 beats 1 and 2 beats 1. Then 2 beats 3 or 3 beats 2.
- 2 beats 3: $w = (0, 2, 1)$. Final: 2,3,1. No.
- 3 beats 2: $w = (0, 1, 2)$. Final: 3,2,1. No.

Say 3 beats 1 and 3 beats 2. Then 1 beats 2 or 2 beats 1.
- 1 beats 2: $w = (1, 0, 2)$. Final: 3,1,2. No.
- 2 beats 1: $w = (0, 1, 2)$. Final: 3,2,1. No.

Say 2 beats 1 and 3 beats 2. Then 1 beats 3 or 3 beats 1.
- 1 beats 3: $w = (1, 1, 1)$. Final: 1,2,3. Yes! 2 upsets.

Can we have 3 upsets (all reversed)? 2 beats 1, 3 beats 1, 3 beats 2. $w = (0,1,2)$. Final: 3,2,1. No.

So for $N=3$, max is 2.

Hmm, let me think about the pattern. $N=3$: 2 upsets out of 3 matches.

Let me think about $N = 5$.

The answer for this problem... let me think. This is a UK competition problem. The answer is likely $\frac{(N-1)^2}{4}$ or $\frac{N^2-1}{8}$ or something.

For $N=3$: $(N-1)^2/4 = 1$. But we got 2. So not that.

$\frac{N^2-1}{8} = 1$ for $N=3$. No.

Let me reconsider. For $N=3$ we found 2 upsets.

Let me think more carefully about the structure.

Key insight: We need $w_1 \geq w_2 \geq \cdots \geq w_N$.

The number of upsets $U$ relates to the win counts. Let $w_i$ = wins of player $i$. In the "no upset" scenario, player $i$ would beat all $j > i$ and lose to all $j < i$, giving $w_i^{(0)} = N - i$.

Each upset involving pair $(i,j)$ with $i < j$ (j beats i) changes: $w_i$ decreases by 1, $w_j$ increases by 1 compared to no-upset.

So $w_i = (N - i) - u_i^{\text{out}} + u_i^{\text{in}}$ where $u_i^{\text{out}}$ = number of upsets where $i$ loses to someone below, $u_i^{\text{in}}$ = number of upsets where $i$ beats someone above.

Actually, let me define: for pair $(i,j)$, $i < j$. Normal: $i$ beats $j$. Upset: $j$ beats $i$.

$w_i = \#\{j > i : i \text{ beats } j\} + \#\{j < i : i \text{ beats } j\}$
$= (N - i - u_i^-) + u_i^+$

where $u_i^-$ = upsets where $i$ loses to someone below (i.e., $j > i$ beats $i$), and $u_i^+$ = upsets where $i$ beats someone above ($i$ beats $j < i$).

Note $u_i^-$ counts pairs $(i, j)$ with $j > i$ that are upsets, and $u_i^+$ counts pairs $(j, i)$ with $j < i$ that are upsets.

Total upsets $U = \sum_i u_i^+ = \sum_i u_i^-$ (each upset counted once in each sum... no). Actually each upset $(i,j)$ with $i < j$ contributes to $u_j^+$ (j beats someone above) and $u_i^-$ (i loses to someone below). So $\sum_i u_i^+ = \sum_i u_i^- = U$.

$w_i = (N - i) - u_i^- + u_i^+$.

We need $w_1 \geq w_2 \geq \cdots \geq w_N$.

We want to maximize $U$.

Let me think about this differently. Consider the "score sequence" $w_1, \ldots, w_N$. We need it non-increasing and it must be a valid score sequence of a tournament, plus the upset structure must be consistent.

Actually, any non-increasing sequence that's a valid tournament score sequence works, and then we need to check if we can realize it with the right upset count.

Hmm, this is getting complex. Let me think about it from the perspective of maximizing upsets.

Let me consider the construction. For $N = 3$, the optimal was: 2 beats 1, 3 beats 2, 1 beats 3. This is a cyclic tournament (rock-paper-scissors), $w = (1,1,1)$. Upsets: (1,2)→2 wins, (2,3)→3 wins. That's 2 upsets. (1,3)→1 wins, not upset.

So the cycle $1 \to 3 \to 2 \to 1$... wait let me recheck. 2 beats 1 (upset, since 2 > 1), 3 beats 2 (upset, since 3 > 2), 1 beats 3 (not upset). Yes, 2 upsets.

For general odd $N$, maybe we can make all players have the same number of wins $(N-1)/2$, which is a regular tournament. In a regular tournament on odd $N$ vertices, every vertex has out-degree $(N-1)/2$.

If all $w_i = (N-1)/2$, then final ranking = initial ranking (all tied, broken by initial rank). 

Now, can we find a regular tournament that maximizes upsets? The number of upsets in a regular tournament... we want to maximize the number of edges $(i,j)$ with $i < j$ where $j \to i$ (j beats i).

Total edges = $\binom{N}{2}$. In a regular tournament, each vertex has out-degree $(N-1)/2$.

The number of upsets = number of "backward" edges. We want to maximize backward edges while keeping the tournament regular.

Hmm, but is regular tournament optimal? Maybe we can do better with non-regular.

Let me think about upper bounds.

Claim: $U \leq \frac{N^2 - 1}{8}$? For $N = 3$: $(9-1)/8 = 1$. But we found 2. So no.

Let me reconsider. For $N = 3$, $U = 2$, total matches = 3. So $U$ can be close to total.

Let me think about $N = 5$ more carefully.

Let me try to construct a good solution for $N = 5$.

Players 1,2,3,4,5. No-upset wins: $w^{(0)} = (4,3,2,1,0)$.

Idea: Try to make all $w_i = 2$ (regular tournament). Then we need a regular tournament on 5 vertices maximizing upsets.

In a regular tournament on 5 vertices, each has out-degree 2. Total edges = 10. We want to maximize backward edges (edges $(i,j)$, $i < j$, where $j \to i$).

The "canonical" regular tournament on 5 vertices: arrange 0,1,2,3,4 in a circle, each beats the next 2. Edges: $i \to i+1, i \to i+2$ (mod 5).

Let me map: players 1,2,3,4,5 → 0,1,2,3,4.
- 0 beats 1, 2; loses to 3, 4.
- 1 beats 2, 3; loses to 4, 0.
- 2 beats 3, 4; loses to 0, 1.
- 3 beats 4, 0; loses to 1, 2.
- 4 beats 0, 1; loses to 2, 3.

Now count upsets (edges where higher-numbered player beats lower, i.e., $j > i$ and $j \to i$):
- (1,2): 0→1, not upset. (1,3): 0→2, not upset. (1,4): 3→0, upset! (1,5): 4→0, upset!
- (2,3): 1→2, not upset. (2,4): 3→1, upset! (2,5): 4→1, upset!
- (3,4): 2→3, not upset. (3,5): 2→4, not upset. Wait, 2 beats 4? Yes. Not upset (3 < 5, 3 beats 5, not upset).

Wait, I need to recompute. Player 3 = vertex 2, player 5 = vertex 4. Edge (3,5) = (2,4): 2→4, so player 3 beats player 5. Not upset.

- (4,5) = (3,4): 3→4, player 4 beats player 5. Not upset.

Upsets: (1,4), (1,5), (2,4), (2,5). That's 4 upsets.

Can we do better? Let me try a different regular tournament or even non-regular.

Actually, let me think about whether non-regular can give more upsets.

Let me try to maximize upsets directly. We want as many "backward" edges as possible while maintaining $w_1 \geq w_2 \geq \cdots \geq w_5$.

Extreme: try to reverse as many as possible. If we reverse all edges, $w = (0,1,2,3,4)$, which is increasing, not non-increasing. Bad.

Let me think about it as: we start from the transitive tournament (no upsets, $w = (4,3,2,1,0)$) and flip edges. Each flip of edge $(i,j)$, $i < j$ (from $i$ beats $j$ to $j$ beats $i$) decreases $w_i$ by 1 and increases $w_j$ by 1.

We want to maximize the number of flips while keeping $w_1 \geq w_2 \geq \cdots \geq w_N$.

After flipping a set $S$ of edges, $w_i = (N-i) - d_i^- + d_i^+$ where $d_i^-$ = number of flipped edges going down from $i$ (i.e., $(i,j)$ flipped, $j > i$) and $d_i^+$ = number of flipped edges coming up to $i$ (i.e., $(j,i)$ flipped, $j < i$).

We need $w_i \geq w_{i+1}$ for all $i$.

$w_i - w_{i+1} = [(N-i) - d_i^- + d_i^+] - [(N-i-1) - d_{i+1}^- + d_{i+1}^+]$
$= 1 - d_i^- + d_i^+ + d_{i+1}^- - d_{i+1}^+$.

We need this $\geq 0$ for all $i = 1, \ldots, N-1$.

So $d_i^- - d_i^+ - d_{i+1}^- + d_{i+1}^+ \leq 1$ for all $i$.

Let $f_i = d_i^+ - d_i^-$. Then $f_{i+1} - f_i \leq 1$, i.e., $f_{i+1} \leq f_i + 1$.

Also $w_i = (N-i) + f_i$. We need $w_i \geq 0$ (can't have negative wins) and $w_i \leq N-1$ (can't have more than $N-1$ wins). Actually $w_i \geq 0$ is automatic-ish, and $w_i \leq N-1$ too, since wins are between 0 and $N-1$.

Now, $U = \sum_i d_i^- = \sum_i d_i^+ = $ total flips.

We have $d_i^+ = $ number of flipped edges $(j, i)$ with $j < i$ = number of $j < i$ such that $i$ beats $j$ (upset). $d_i^- = $ number of flipped edges $(i, j)$ with $j > i$ = number of $j > i$ such that $j$ beats $i$ (upset).

Constraints:
- $0 \leq d_i^+ \leq i - 1$ (at most $i-1$ players above)
- $0 \leq d_i^- \leq N - i$ (at most $N-i$ players below)
- $f_{i+1} \leq f_i + 1$ for $i = 1, \ldots, N-1$
- $w_i = (N - i) + f_i \geq 0$ and $\leq N - 1$.
- The score sequence must be realizable as a tournament (Landau's condition).

We want to maximize $U = \sum d_i^+ = \sum d_i^-$.

Note $\sum f_i = \sum d_i^+ - \sum d_i^- = 0$. So $\sum f_i = 0$.

We want to maximize $U = \sum d_i^+$. Since $d_i^+ = f_i + d_i^-$ and $d_i^+ \leq i - 1$, $d_i^- \leq N - i$...

This is getting complicated. Let me think about it more cleverly.

We want to maximize $U$. Note $U = \sum d_i^+$. We have $d_i^+ \leq i - 1$ (player $i$ can upset at most $i-1$ players above them). Also $d_i^- \leq N - i$.

Also $d_i^+ = f_i + d_i^-$, so $d_i^+ \leq f_i + (N - i)$, meaning $f_i \geq d_i^+ - (N-i)$. And $d_i^- = d_i^+ - f_i \leq N - i$, so $f_i \geq d_i^+ - (N - i)$, same thing. Also $d_i^- \geq 0$ so $f_i \leq d_i^+$. And $d_i^+ \leq i - 1$.

So $U = \sum d_i^+ \leq \sum (i - 1) = \binom{N}{2}$. That's trivial (all edges flipped, but that violates constraints).

The binding constraint is $f_{i+1} \leq f_i + 1$ and $\sum f_i = 0$ and $w_i = (N-i) + f_i \geq 0$.

$w_i \geq 0 \Rightarrow f_i \geq -(N-i) = i - N$.
$w_i \leq N - 1 \Rightarrow f_i \leq N - 1 - (N - i) = i - 1$.

So $i - N \leq f_i \leq i - 1$.

Also $d_i^+ \leq i - 1$ and $d_i^+ = f_i + d_i^- \leq f_i + (N - i)$. So $d_i^+ \leq \min(i - 1, f_i + N - i)$.

And $d_i^- \leq N - i$ and $d_i^- = d_i^+ - f_i \leq (i-1) - f_i$. So $d_i^- \leq \min(N - i, i - 1 - f_i)$.

$U = \sum d_i^+$. To maximize, we want $d_i^+$ as large as possible. $d_i^+ \leq \min(i-1, f_i + N - i)$.

If $f_i \geq 2i - 1 - N$, then $f_i + N - i \geq i - 1$, so $d_i^+ \leq i - 1$.
If $f_i < 2i - 1 - N$, then $d_i^+ \leq f_i + N - i < i - 1$.

So to maximize $d_i^+$, we want $f_i$ large. But $\sum f_i = 0$ and $f_{i+1} \leq f_i + 1$.

Also we need the tournament to be realizable. Let me set that aside and first find the maximum of $U$ subject to the constraints, then check realizability.

We want to maximize $\sum_i \min(i - 1, f_i + N - i)$ subject to:
- $\sum f_i = 0$
- $f_{i+1} \leq f_i + 1$
- $i - N \leq f_i \leq i - 1$

The function $\min(i-1, f_i + N - i)$ is increasing in $f_i$ (until it saturates at $i-1$). So we want $f_i$ as large as possible. But $\sum f_i = 0$ means we can't have all large.

The constraint $f_{i+1} \leq f_i + 1$ means $f$ can increase by at most 1 per step. Since $\sum f_i = 0$, and $f$ is somewhat constrained...

Let me think about what $f$ sequence maximizes $\sum \min(i-1, f_i + N - i)$.

Since the objective is concave (piecewise linear, increasing then flat), and we have a sum constraint, this is like a resource allocation problem.

Let me think about the "marginal" value. For player $i$, increasing $f_i$ by 1 increases $d_i^+$ by 1 if $f_i + N - i < i - 1$, i.e., $f_i < 2i - 1 - N$, and by 0 otherwise.

But increasing $f_i$ means we need to decrease other $f_j$'s (to keep $\sum = 0$), which might decrease their $d_j^+$.

Also the constraint $f_{i+1} \leq f_i + 1$ links them.

Let me try a specific form. Suppose $f_i = c - (i - 1)$ for some constant $c$ (i.e., $f$ decreases by 1 each step). Then $f_{i+1} = f_i - 1 \leq f_i + 1$. ✓. $\sum f_i = Nc - \sum_{i=1}^N (i-1) = Nc - \binom{N}{2} = 0 \Rightarrow c = \binom{N}{2}/N = (N-1)/2$.

So $f_i = (N-1)/2 - (i-1) = (N+1)/2 - i$.

Then $w_i = (N - i) + f_i = (N - i) + (N+1)/2 - i = (N + (N+1)/2) - 2i = (3N+1)/2 - 2i$.

For $N = 5$: $w_i = 8 - 2i$: $w = (6, 4, 2, 0, -2)$. But $w_5 = -2 < 0$. Not valid.

So this linear decrease is too steep. We need $w_i \geq 0$, i.e., $f_i \geq i - N$.

$f_i = (N+1)/2 - i \geq i - N \Rightarrow (N+1)/2 + N \geq 2i \Rightarrow (3N+1)/2 \geq 2i \Rightarrow i \leq (3N+1)/4$.

For $N = 5$: $i \leq 4$. So $f_5$ violates. We need to adjust.

Let me try a different approach. Let me think about the problem more directly.

Actually, let me reconsider. The constraint $f_{i+1} \leq f_i + 1$ allows $f$ to increase by at most 1. It can decrease arbitrarily fast. So we could have $f$ decrease rapidly and then stay flat.

Let me think about the optimal shape. We want $f_i$ large for small $i$ (to allow large $d_i^+$... wait, for small $i$, $i - 1$ is small, so $d_i^+$ is limited by $i - 1$ anyway).

Actually, for player $i$, the max $d_i^+$ is $i - 1$ (can't upset more than $i - 1$ players above). This is achieved when $f_i \geq 2i - 1 - N$.

For large $i$ (near $N$), $i - 1$ is large, so the binding constraint is $f_i + N - i$. We need $f_i$ large enough.

$\sum d_i^+ \leq \sum (i - 1) = \binom{N}{2}$, but we also need $\sum d_i^- = \sum d_i^+$ and $d_i^- \leq N - i$.

So $U = \sum d_i^+ = \sum d_i^- \leq \sum (N - i) = \binom{N}{2}$. Both give the same trivial bound.

The real constraint is the non-increasing $w_i$.

Let me try to think about it as: we want $w_i = (N - i) + f_i$ non-increasing, $\sum f_i = 0$, $f_{i+1} \leq f_i + 1$, and $U = \sum d_i^+$ where $d_i^+ \leq \min(i - 1, f_i + N - i)$.

To maximize $U$, ideally $d_i^+ = \min(i - 1, f_i + N - i)$ for all $i$. This requires that we can actually realize such $d_i^+$ and $d_i^-$ with a valid tournament. Let me first find the upper bound assuming we can.

$U \leq \sum_i \min(i - 1, f_i + N - i)$.

We want to maximize this over valid $f$.

Let $g_i = \min(i - 1, f_i + N - i)$. We want $\sum g_i$ max.

For $f_i \geq 2i - 1 - N$: $g_i = i - 1$ (saturated).
For $f_i < 2i - 1 - N$: $g_i = f_i + N - i$.

To maximize, we want all $g_i = i - 1$, i.e., $f_i \geq 2i - 1 - N$ for all $i$. Then $U \leq \binom{N}{2}$, but we also need $\sum f_i = 0$ and $f_{i+1} \leq f_i + 1$ and $f_i \leq i - 1$.

$f_i \geq 2i - 1 - N$ and $f_i \leq i - 1$. For $i$ near $N$, $2i - 1 - N \approx i - 1$, so $f_i \approx i - 1$. For $i = N$, $f_N \geq N - 1$ and $f_N \leq N - 1$, so $f_N = N - 1$. Then $f_{N-1} \geq f_N - ? $... wait, the constraint is $f_{i+1} \leq f_i + 1$, i.e., $f_i \geq f_{i+1} - 1$. So $f_{N-1} \geq f_N - 1 = N - 2$. And $f_{N-1} \leq N - 2$. So $f_{N-1} = N - 2$. By induction, $f_i = i - 1$ for all $i$. Then $\sum f_i = \sum (i-1) = \binom{N}{2} \neq 0$ (for $N \geq 2$). Contradiction.

So we can't have all saturated. We need $\sum f_i = 0$, which means some $f_i$ must be negative (for large enough $N$).

OK so the problem is: maximize $\sum \min(i - 1, f_i + N - i)$ subject to $\sum f_i = 0$, $f_{i+1} \leq f_i + 1$, $i - N \leq f_i \leq i - 1$.

Let me substitute $f_i = (i - 1) - h_i$ where $h_i \geq 0$ (since $f_i \leq i - 1$) and $h_i \leq N - 1$ (since $f_i \geq i - N$, so $h_i \leq N - 1$). Then:

$g_i = \min(i - 1, (i - 1) - h_i + N - i) = \min(i - 1, N - 1 - h_i)$.

$\sum f_i = \sum (i - 1) - \sum h_i = \binom{N}{2} - \sum h_i = 0 \Rightarrow \sum h_i = \binom{N}{2}$.

$f_{i+1} \leq f_i + 1 \Rightarrow (i) - h_{i+1} \leq (i - 1) - h_i + 1 \Rightarrow -h_{i+1} \leq -h_i \Rightarrow h_{i+1} \geq h_i$.

So $h$ is non-decreasing! And $0 \leq h_i \leq N - 1$, $\sum h_i = \binom{N}{2}$, $h$ non-decreasing.

$g_i = \min(i - 1, N - 1 - h_i)$.

$U \leq \sum g_i = \sum \min(i - 1, N - 1 - h_i)$.

We want to maximize this. Since $h$ is non-decreasing and $\sum h_i = \binom{N}{2} = \frac{N(N-1)}{2}$, and $h_i \leq N - 1$...

Note $\sum (N-1) = N(N-1) = 2\binom{N}{2}$. So $\sum h_i = \binom{N}{2}$ means on average $h_i = (N-1)/2$.

$g_i = \min(i - 1, N - 1 - h_i)$. We want to maximize $\sum g_i$.

Since $h$ is non-decreasing, $N - 1 - h_i$ is non-increasing. And $i - 1$ is increasing. So $g_i = \min(\text{increasing}, \text{non-increasing})$. The min is maximized when the two cross as late/high as possible.

$\sum g_i = \sum \min(i - 1, N - 1 - h_i)$.

To maximize, we want $h_i$ small for small $i$ (so $N - 1 - h_i$ is large, but $i - 1$ is the binding constraint there) and... actually for small $i$, $i - 1$ is small so $g_i = i - 1$ regardless (as long as $N - 1 - h_i \geq i - 1$, i.e., $h_i \leq N - i$). For large $i$, $N - 1 - h_i$ might be binding.

Let me think about it. $g_i = i - 1$ if $h_i \leq N - i$, and $g_i = N - 1 - h_i$ if $h_i \geq N - i$.

Since $h$ is non-decreasing and $N - i$ is decreasing, there's a crossover point. For $i \leq k$, $h_i \leq N - i$ (so $g_i = i - 1$), and for $i > k$, $h_i \geq N - i$ (so $g_i = N - 1 - h_i$).

$U \leq \sum_{i=1}^{k} (i - 1) + \sum_{i=k+1}^{N} (N - 1 - h_i) = \binom{k}{2} + (N - k)(N - 1) - \sum_{i=k+1}^{N} h_i$.

We have $\sum h_i = \binom{N}{2}$, so $\sum_{i=k+1}^{N} h_i = \binom{N}{2} - \sum_{i=1}^{k} h_i$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + \sum_{i=1}^k h_i$.

To maximize, we want $\sum_{i=1}^k h_i$ as large as possible. But $h$ is non-decreasing and $h_i \leq N - i$ for $i \leq k$ (to stay in the $g_i = i-1$ regime). So $h_i \leq N - i$ for $i \leq k$, and $h$ non-decreasing means $h_1 \leq h_2 \leq \cdots \leq h_k \leq N - k$ (the tightest constraint is $h_k \leq N - k$).

So $\sum_{i=1}^k h_i \leq k \cdot (N - k)$ (since all $\leq N - k$ and non-decreasing, max is all equal to $N - k$... wait, non-decreasing means $h_1 \leq \cdots \leq h_k$, and each $\leq N - i$. The binding constraint is $h_i \leq N - i$. Since $h$ is non-decreasing, $h_i \leq h_k \leq N - k$ for $i \leq k$. But also $h_i \leq N - i \geq N - k$ for $i \leq k$. So the binding constraint is $h_k \leq N - k$, and $h_i \leq N - i$ which is $\geq N - k$. So actually $h_i \leq N - i$ for each $i$, and since $h$ is non-decreasing, the max of $\sum_{i=1}^k h_i$ is achieved when $h_i = N - i$ for $i = 1, \ldots, k$? No, that's decreasing. $h$ must be non-decreasing.

Hmm, $h$ non-decreasing and $h_i \leq N - i$ (decreasing bound). So $h_k \leq N - k$ is the tightest. And $h_i \leq h_k \leq N - k$ for $i \leq k$. But $h_i \leq N - i \geq N - k$ is automatically satisfied if $h_i \leq N - k$. So the constraint is $h_i \leq N - k$ for $i \leq k$ (from non-decreasing + $h_k \leq N - k$).

Wait, no. $h_i \leq N - i$ is required for $g_i = i - 1$. For $i \leq k$, we need $h_i \leq N - i$. Since $h$ is non-decreasing, $h_i \leq h_k \leq N - k \leq N - i$ (for $i \leq k$). So if $h_k \leq N - k$, then automatically $h_i \leq N - i$ for all $i \leq k$. Good.

So $\sum_{i=1}^k h_i \leq k(N - k)$ (each $h_i \leq N - k$, and they're non-decreasing, so max sum is $k(N-k)$ when all equal $N - k$).

But wait, we also need $h_i \geq 0$ and $h$ non-decreasing overall, and $\sum h_i = \binom{N}{2}$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + k(N-k)$.

$= \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + k(N-k)$

$= \binom{k}{2} + (N-k)(N-1+k) - \binom{N}{2}$

$= \binom{k}{2} + (N-k)(N-1+k) - \binom{N}{2}$

Let me expand: $(N-k)(N-1+k) = N^2 - N + Nk - Nk + k - k^2 = N^2 - N + k - k^2$. 

Hmm let me redo: $(N-k)(N-1+k) = N(N-1+k) - k(N-1+k) = N^2 - N + Nk - kN + k - k^2 = N^2 - N + k - k^2$.

$\binom{k}{2} = k(k-1)/2$. $\binom{N}{2} = N(N-1)/2$.

$U \leq \frac{k(k-1)}{2} + N^2 - N + k - k^2 - \frac{N(N-1)}{2}$

$= \frac{k^2 - k}{2} + N^2 - N + k - k^2 - \frac{N^2 - N}{2}$

$= \frac{k^2 - k - N^2 + N}{2} + N^2 - N + k - k^2$

$= \frac{k^2 - k - N^2 + N}{2} + \frac{2N^2 - 2N + 2k - 2k^2}{2}$

$= \frac{k^2 - k - N^2 + N + 2N^2 - 2N + 2k - 2k^2}{2}$

$= \frac{-k^2 + k + N^2 - N}{2}$

$= \frac{N^2 - N - k^2 + k}{2}$

$= \frac{N(N-1) - k(k-1)}{2}$

$= \binom{N}{2} - \binom{k}{2}$.

So $U \leq \binom{N}{2} - \binom{k}{2}$ where $k$ is the crossover point. To maximize, we want $k$ as small as possible.

But $k$ can't be too small. We need the constraints to be satisfiable. Specifically, we need $h$ non-decreasing, $0 \leq h_i \leq N - 1$, $\sum h_i = \binom{N}{2}$, and $h_k \leq N - k$ (for the crossover to be at $k$).

Also, for $i > k$, $h_i \geq N - i$ (to be in the regime $g_i = N - 1 - h_i$). And $h_i \leq N - 1$.

$\sum_{i=k+1}^N h_i = \binom{N}{2} - \sum_{i=1}^k h_i$. With $\sum_{i=1}^k h_i = k(N-k)$ (max), $\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k) = \frac{N(N-1) - 2k(N-k)}{2} = \frac{N(N-1) - 2kN + 2k^2}{2} = \frac{(N-k)(N-1-2k) + 2k^2 - k... }$. Let me just compute: $\frac{N^2 - N - 2kN + 2k^2}{2} = \frac{(N-k)^2 - (N - 2k) \cdot ... }$. Actually $\frac{N^2 - N - 2kN + 2k^2}{2} = \frac{(N - 2k + ?)... }$. Let me factor: $N^2 - 2kN + 2k^2 - N = (N - k)^2 + k^2 - N$. Hmm, not clean. Let me just leave it.

For $i > k$, we need $h_i \geq N - i$ and $h_i \leq N - 1$, and $h$ non-decreasing. The number of terms is $N - k$.

$\sum_{i=k+1}^N h_i \geq \sum_{i=k+1}^N (N - i) = \sum_{j=0}^{N-k-1} j = \binom{N-k}{2}$ (where $j = N - i$, $i$ from $k+1$ to $N$, $j$ from $N-k-1$ to $0$).

Also $\sum_{i=k+1}^N h_i \leq (N - k)(N - 1)$ (each $\leq N - 1$).

We need $\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k)$ (when $\sum_{i=1}^k h_i = k(N-k)$).

Check feasibility: $\binom{N}{2} - k(N-k) \geq \binom{N-k}{2}$?

$\frac{N(N-1)}{2} - k(N-k) \geq \frac{(N-k)(N-k-1)}{2}$

$\frac{N(N-1) - (N-k)(N-k-1)}{2} \geq k(N-k)$

$N(N-1) - (N-k)(N-k-1) \geq 2k(N-k)$

$N^2 - N - (N^2 - 2kN + k^2 - N + k) \geq 2kN - 2k^2$

$2kN - k^2 - k \geq 2kN - 2k^2$

$-k^2 - k \geq -2k^2$

$k^2 - k \geq 0$

$k(k-1) \geq 0$, true for $k \geq 1$. ✓

Also need $\binom{N}{2} - k(N-k) \leq (N-k)(N-1)$:

$\frac{N(N-1)}{2} - k(N-k) \leq (N-k)(N-1)$

$\frac{N(N-1)}{2} \leq k(N-k) + (N-k)(N-1) = (N-k)(k + N - 1) = (N-k)(N + k - 1)$

$\frac{N(N-1)}{2} \leq (N-k)(N+k-1) = N^2 + Nk - N - kN - k^2 + k = N^2 - N - k^2 + k$

$\frac{N(N-1)}{2} \leq N(N-1) - k(k-1)$

$k(k-1) \leq \frac{N(N-1)}{2}$

True for $k \leq N - 1$ (roughly). ✓

Also need $h$ non-decreasing across the boundary: $h_k \leq h_{k+1}$. $h_k = N - k$ (we set it to max), and $h_{k+1} \geq N - (k+1) = N - k - 1$. So we need $h_{k+1} \geq N - k$. But $h_{k+1} \leq N - 1$. So $N - k \leq h_{k+1} \leq N - 1$. This requires $N - k \leq N - 1$, i.e., $k \geq 1$. ✓

But we also need $h_{k+1} \geq h_k = N - k$ and $h_{k+1} \geq N - k - 1$ (the regime constraint). The binding one is $h_{k+1} \geq N - k$.

So the crossover $k$ can be as small as... we need $k \geq 1$ and the sum constraints to work. Let me check $k = 1$:

$U \leq \binom{N}{2} - \binom{1}{2} = \binom{N}{2} - 0 = \binom{N}{2}$. That would mean all edges are upsets, but that gives $w = (0, 1, \ldots, N-1)$, which is increasing, not non-increasing. So something's wrong.

The issue is that when $k = 1$, we need $h_1 = N - 1$ (max), and $h_i \geq N - i$ for $i \geq 2$, with $\sum h_i = \binom{N}{2}$. $h_1 = N - 1$, $\sum_{i=2}^N h_i = \binom{N}{2} - (N-1) = \frac{N(N-1) - 2(N-1)}{2} = \frac{(N-1)(N-2)}{2} = \binom{N-1}{2}$. And $\sum_{i=2}^N (N - i) = \binom{N-1}{2}$. So $h_i = N - i$ for $i \geq 2$. But $h$ must be non-decreasing: $h_1 = N - 1$, $h_2 = N - 2 < N - 1$. Not non-decreasing! ✗

So $k = 1$ doesn't work because $h$ must be non-decreasing but $h_1 = N - 1 > h_2 = N - 2$.

The non-decreasing constraint on $h$ is crucial. Let me redo the analysis.

$h$ non-decreasing, $h_i \leq N - i$ for $i \leq k$, $h_i \geq N - i$ for $i > k$. Since $h$ is non-decreasing and $N - i$ is decreasing, the condition $h_i \leq N - i$ for $i \leq k$ and $h_i \geq N - i$ for $i > k$ means the crossover happens where $h$ crosses $N - i$ from below.

Since $h$ is non-decreasing and $N - i$ is strictly decreasing, they can cross at most once. So there's a unique crossover point $k$ where $h_k \leq N - k$ and $h_{k+1} \geq N - k - 1$... actually $h_{k+1} \geq N - (k+1) = N - k - 1$.

But we also need $h_k \leq h_{k+1}$ (non-decreasing). And $h_k \leq N - k$, $h_{k+1} \geq N - k - 1$.

Now, the key constraint I missed: $h$ non-decreasing means $h_1 \leq h_2 \leq \cdots \leq h_k \leq N - k$ (since $h_k \leq N - k$ and non-decreasing means all earlier are $\leq h_k \leq N - k$). But also $h_i \leq N - i$ for each $i \leq k$, which is $\geq N - k$, so the binding constraint is $h_k \leq N - k$.

For $i > k$: $h_i \geq N - i$ and $h_i \leq N - 1$ and non-decreasing. The minimum values are $h_i = N - i$ but these are decreasing, contradicting non-decreasing. So we need $h_i \geq h_{i-1}$ for $i > k$.

Actually, for $i > k$, $h_i \geq \max(N - i, h_{i-1})$. Since $h$ is non-decreasing, $h_{k+1} \geq h_k$, $h_{k+2} \geq h_{k+1}$, etc. And $h_{k+1} \geq N - k - 1$.

The minimum non-decreasing sequence with $h_i \geq N - i$ for $i > k$ is: $h_{k+1} = \max(N - k - 1, h_k)$, $h_{k+2} = \max(N - k - 2, h_{k+1})$, etc. Since $N - i$ is decreasing and $h$ is non-decreasing, once $h_{k+1} \geq N - k - 1$, the non-decreasing property ensures $h_i \geq h_{k+1} \geq N - k - 1 \geq N - i$ for $i \geq k + 1$ (since $N - i \leq N - k - 1$). So the binding constraint is just $h_{k+1} \geq N - k - 1$ and non-decreasing.

So for $i > k$, the minimum is $h_i = h_{k+1}$ for all $i > k$ (constant), with $h_{k+1} \geq \max(N - k - 1, h_k)$.

Now, $\sum h_i = \sum_{i=1}^k h_i + \sum_{i=k+1}^N h_i = \binom{N}{2}$.

To maximize $U = \binom{N}{2} - \binom{k}{2}$, we want $k$ minimal. But we need feasibility.

Let me set $h_1 = \cdots = h_k = a$ (constant, non-decreasing, $\leq N - k$) and $h_{k+1} = \cdots = h_N = b$ (constant, non-decreasing, $\geq N - k - 1$). With $a \leq b$.

$\sum h_i = ka + (N-k)b = \binom{N}{2}$.

$U = \binom{N}{2} - \binom{k}{2}$ (from the formula, assuming the crossover is exactly at $k$).

Wait, but I need to re-derive $U$ more carefully with the non-decreasing constraint.

Actually, let me reconsider. The formula $U \leq \binom{N}{2} - \binom{k}{2}$ was derived assuming $\sum_{i=1}^k h_i = k(N-k)$ (maximum). But with the non-decreasing constraint, the maximum of $\sum_{i=1}^k h_i$ is $k \cdot \min(N-k, \text{something})$. Since $h_i \leq h_k \leq N - k$ and non-decreasing, max is $h_i = N - k$ for all $i \leq k$, giving $\sum = k(N-k)$. But we also need $h_k \leq h_{k+1}$, and $h_{k+1} \leq N - 1$. So $h_k = N - k \leq h_{k+1} \leq N - 1$, requiring $N - k \leq N - 1$, i.e., $k \geq 1$. Fine.

But we also need $\sum h_i = \binom{N}{2}$ and $h_{k+1} \geq N - k$ (from $h_{k+1} \geq h_k = N - k$). And $h_{k+1} \leq N - 1$.

$\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k)$. With $h_{k+1} = \cdots = h_N = b$, $(N-k)b = \binom{N}{2} - k(N-k)$, so $b = \frac{\binom{N}{2} - k(N-k)}{N-k} = \frac{\binom{N}{2}}{N-k} - k = \frac{N(N-1)}{2(N-k)} - k$.

We need $b \geq N - k$ (from non-decreasing + $h_k = N - k$):

$\frac{N(N-1)}{2(N-k)} - k \geq N - k$

$\frac{N(N-1)}{2(N-k)} \geq N$

$N(N-1) \geq 2N(N-k)$

$N - 1 \geq 2(N - k)$

$N - 1 \geq 2N - 2k$

$2k \geq N + 1$

$k \geq \frac{N+1}{2}$.

So $k \geq (N+1)/2$. Since $N$ is odd, $(N+1)/2$ is an integer. So the minimum $k$ is $(N+1)/2$.

Then $U \leq \binom{N}{2} - \binom{(N+1)/2}{2}$.

$\binom{N}{2} - \binom{(N+1)/2}{2} = \frac{N(N-1)}{2} - \frac{\frac{N+1}{2} \cdot \frac{N-1}{2}}{2} = \frac{N(N-1)}{2} - \frac{(N+1)(N-1)}{8} = \frac{4N(N-1) - (N+1)(N-1)}{8} = \frac{(N-1)(4N - N - 1)}{8} = \frac{(N-1)(3N - 1)}{8}$.

For $N = 3$: $\frac{2 \cdot 8}{8} = 2$. ✓ (matches our finding)

For $N = 5$: $\frac{4 \cdot 14}{8} = 7$. So max upsets = 7 out of 10 matches.

Let me verify: $k = 3$, $h_1 = h_2 = h_3 = N - k = 2$, $b = \frac{10}{2} - 3 = 2$. So $h = (2, 2, 2, 2, 2)$. All equal. $f_i = (i-1) - 2 = (−2, −1, 0, 1, 2)$. $w_i = (N-i) + f_i = (4,3,2,1,0) + (−2,−1,0,1,2) = (2, 2, 2, 2, 2)$. Regular tournament! All wins = 2.

$U = \sum d_i^+ = \sum \min(i-1, f_i + N - i) = \sum \min(i-1, (i-1) - 2 + 5 - i) = \sum \min(i-1, 2)$.

$i=1$: $\min(0, 2) = 0$. $i=2$: $\min(1, 2) = 1$. $i=3$: $\min(2, 2) = 2$. $i=4$: $\min(3, 2) = 2$. $i=5$: $\min(4, 2) = 2$.

$U = 0 + 1 + 2 + 2 + 2 = 7$. ✓

So the upper bound is $\frac{(N-1)(3N-1)}{8}$, achieved by a regular tournament where all $w_i = (N-1)/2$.

But wait, I need to verify that such a tournament actually exists (i.e., the upset pattern is realizable). We need a regular tournament on $N$ vertices (odd) where the number of backward edges is exactly $\frac{(N-1)(3N-1)}{8}$.

In the construction above, $d_i^+ = \min(i-1, (N-1)/2)$ and $d_i^- = d_i^+ - f_i = \min(i-1, (N-1)/2) - ((i-1) - (N-1)/2)$.

For $i \leq (N+1)/2$: $d_i^+ = i - 1$, $d_i^- = (i-1) - (i - 1 - (N-1)/2) = (N-1)/2$. So player $i$ upsets all $i - 1$ players above and is upset by $(N-1)/2$ players below. Total wins: $(N - i) - (N-1)/2 + (i - 1) = (N - 1)/2$. ✓

For $i > (N+1)/2$: $d_i^+ = (N-1)/2$, $d_i^- = (N-1)/2 - (i - 1 - (N-1)/2) = (N-1) - (i-1) = N - i$. So player $i$ upsets $(N-1)/2$ players above and is upset by all $N - i$ players below. Wins: $(N-i) - (N-i) + (N-1)/2 = (N-1)/2$. ✓

So the structure is:
- For $i \leq (N+1)/2$: player $i$ beats everyone above (all upsets), and beats $(N-1)/2 - (i-1) = (N+1)/2 - i$ players below (non-upsets), loses to $(N-1)/2$ players below (upsets). Wait, let me recount. Player $i$ has $N - i$ players below. $d_i^- = (N-1)/2$ of those are upsets (they beat $i$), so $i$ beats $(N - i) - (N-1)/2 = (N - 2i + 1)/2$ players below. For $i = 1$: $(N-1)/2$. For $i = (N+1)/2$: $0$.

- For $i > (N+1)/2$: player $i$ beats $(N-1)/2$ players above (upsets) and $0$ players below (all below beat them, all upsets). $d_i^- = N - i$ (all below are upsets).

So the tournament structure:
- Players $1, \ldots, (N+1)/2$: each beats all players above them, and beats some players below.
- Players $(N+1)/2 + 1, \ldots, N$: each beats $(N-1)/2$ players above, loses to all below.

This is a specific kind of regular tournament. We need to verify it exists.

Let me think of it as: the "upper half" $A = \{1, \ldots, (N+1)/2\}$ and "lower half" $B = \{(N+1)/2 + 1, \ldots, N\}$. $|A| = (N+1)/2$, $|B| = (N-1)/2$.

Within $A$: player $i$ beats all players above (in $A$). So within $A$, it's a transitive tournament: $1 \to 2 \to \cdots \to (N+1)/2$. Player $i \in A$ beats $i - 1$ players in $A$ (those above) and loses to $(N+1)/2 - i$ players in $A$ (those below).

Between $A$ and $B$: Player $i \in A$ needs total wins $(N-1)/2$. Within $A$, wins = $i - 1$. So wins against $B$ = $(N-1)/2 - (i-1) = (N+1)/2 - i$. Player $i$ beats $(N+1)/2 - i$ players in $B$ (out of $|B| = (N-1)/2$).

For $i = 1$: beats $(N-1)/2$ players in $B$, i.e., all of $B$. For $i = (N+1)/2$: beats $0$ in $B$.

Within $B$: player $j \in B$ needs total wins $(N-1)/2$. Against $A$: player $j$ beats $(N-1)/2 - (\text{wins in } B)$ players in $A$. Wins in $B$: player $j$ loses to all below in $B$ (all upsets, $d_j^- = N - j$), so wins in $B$ = $|B| - 1 - (N - j) = (N-1)/2 - 1 - N + j = j - (N+1)/2 - 1 + 1 = j - (N+1)/2 - 1$... let me recompute.

$|B| = (N-1)/2$. Player $j \in B$, $j > (N+1)/2$. Within $B$, player $j$ beats those below in $B$... no, $d_j^- = N - j$ means all $N - j$ players below beat $j$. Players below $j$ in $B$: those in $B$ with index $> j$, count = $N - j$. So all of them beat $j$. Players above $j$ in $B$: $j - (N+1)/2 - 1$ players. $j$ beats all of them (since within $B$, lower index beats higher index, transitive). So wins in $B$ = $j - (N+1)/2 - 1$.

Hmm, for $j = (N+1)/2 + 1$: wins in $B$ = $0$. For $j = N$: wins in $B$ = $N - (N+1)/2 - 1 = (N-1)/2 - 1 = |B| - 1$. So within $B$, it's transitive: $(N+1)/2 + 1 \to \cdots \to N$.

Wins against $A$ = $(N-1)/2 - (j - (N+1)/2 - 1) = (N-1)/2 - j + (N+1)/2 + 1 = N - j + (N+1)/2 + 1 - (N+1)/2 = N + 1 - j + (N-1)/2 - (N+1)/2$... let me just compute directly.

Player $j \in B$, total wins = $(N-1)/2$. Wins in $B$ = $j - (N+1)/2 - 1$ (beats all above in $B$, which is a transitive tournament). So wins against $A$ = $(N-1)/2 - (j - (N+1)/2 - 1) = (N-1)/2 - j + (N+1)/2 + 1 = N + 1 - j$.

For $j = (N+1)/2 + 1$: wins against $A$ = $N + 1 - (N+1)/2 - 1 = (N-1)/2 = |A| - 1$. So beats all of $A$ except one.
For $j = N$: wins against $A$ = $1$. Beats 1 player in $A$.

Now, between $A$ and $B$: player $i \in A$ beats $(N+1)/2 - i$ players in $B$. Player $j \in B$ beats $N + 1 - j$ players in $A$.

Check: $\sum_{i \in A} (\text{wins against } B) = \sum_{i=1}^{(N+1)/2} ((N+1)/2 - i) = \sum_{k=0}^{(N-1)/2} k = \binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$.

$\sum_{j \in B} (\text{wins against } A) = \sum_{j=(N+1)/2+1}^{N} (N + 1 - j) = \sum_{k=1}^{(N-1)/2} k = \binom{(N-1)/2 + 1}{2} = \binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$.

These should be complementary: wins of $A$ against $B$ + wins of $B$ against $A$ = $|A| \cdot |B| = \frac{N+1}{2} \cdot \frac{N-1}{2} = \frac{(N+1)(N-1)}{4}$.

$\frac{(N+1)(N-1)}{8} + \frac{(N+1)(N-1)}{8} = \frac{(N+1)(N-1)}{4}$. ✓

Now we need to verify that a bipartite tournament between $A$ and $B$ with these degree sequences exists. Player $i \in A$ beats $r_i = (N+1)/2 - i$ players in $B$. Player $j \in B$ beats $s_j = N + 1 - j$ players in $A$ (equivalently, loses to $|A| - s_j = (N+1)/2 - (N + 1 - j) = j - (N+1)/2 - 1$... wait, $|A| = (N+1)/2$, $s_j = N + 1 - j$, so loses to $(N+1)/2 - (N+1-j) = j - (N+1)/2 - 1 + (N+1)/2$... let me recompute: $(N+1)/2 - (N+1-j) = (N+1)/2 - N - 1 + j = j - (N+1)/2 - 1$. For $j = (N+1)/2 + 1$: loses to $0$ in $A$... no, $s_j = N + 1 - (N+1)/2 - 1 = (N-1)/2 = |A| - 1$. So beats $|A| - 1$ in $A$, loses to $1$ in $A$. For $j = N$: $s_j = 1$, beats 1, loses to $|A| - 1 = (N-1)/2$.

So the "losses in $A$" for player $j \in B$ is $|A| - s_j = (N+1)/2 - (N+1-j) = j - (N+1)/2 - 1 + 1 - 1$... ugh. $(N+1)/2 - N - 1 + j = j - (N+1)/2 - 1$. For $j = (N+1)/2 + 1$: $0$. For $j = N$: $(N-1)/2 - 1$.

And $r_i = (N+1)/2 - i$ for $i \in A$. For $i = 1$: $(N-1)/2 = |B|$. For $i = (N+1)/2$: $0$.

So player 1 beats all of $B$, player $(N+1)/2$ beats none of $B$. Player $(N+1)/2 + 1$ loses to none of $A$ (beats all of $A$ except... wait, $s_j = |A| - 1$, so beats $|A| - 1$ players in $A$, loses to 1). Player $N$ beats 1 in $A$.

The bipartite tournament: We need a bipartite graph where $i \in A$ has degree $r_i$ (beats $r_i$ in $B$) and $j \in B$ has "loss degree" $|A| - s_j$ (loses to that many in $A$). 

The loss degrees from $B$ side: player $j$ loses to $j - (N+1)/2 - 1$... hmm wait, I think I need to be more careful. Let me re-derive.

Player $j \in B$ beats $s_j = N + 1 - j$ players in $A$. So $j$ loses to $|A| - s_j = (N+1)/2 - (N+1-j) = j - (N+1)/2 - 1$... 

$(N+1)/2 - N - 1 + j = j - (N+1)/2 - 1$. For $j = (N+3)/2$ (smallest in $B$): $(N+3)/2 - (N+1)/2 - 1 = 1 - 1 = 0$. For $j = N$: $N - (N+1)/2 - 1 = (N-1)/2 - 1 = (N-3)/2$.

So the "losses to $A$" for $B$ players: $0, 1, 2, \ldots, (N-3)/2$. These are $r_i$ values reversed!

$r_i$ for $A$ players: $(N-1)/2, (N-3)/2, \ldots, 1, 0$ (for $i = 1, 2, \ldots, (N+1)/2$).

Losses to $A$ for $B$ players: $0, 1, \ldots, (N-3)/2$ (for $j = (N+3)/2, \ldots, N$).

So we need a bipartite graph between $A$ (size $(N+1)/2$) and $B$ (size $(N-1)/2$) where $A$-side degrees are $(N-1)/2, (N-3)/2, \ldots, 0$ and $B$-side degrees (losses) are $0, 1, \ldots, (N-3)/2$.

Sum of $A$-side degrees: $\sum_{k=0}^{(N-1)/2} k = \binom{(N+1)/2}{2}$. Sum of $B$-side degrees: $\sum_{k=0}^{(N-3)/2} k = \binom{(N-1)/2}{2}$. 

Wait, these should be equal (each edge counted once from each side). $\binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$ and $\binom{(N-1)/2}{2} = \frac{(N-1)(N-3)}{8}$. These are NOT equal! 

$\frac{(N+1)(N-1)}{8} \neq \frac{(N-1)(N-3)}{8}$ for $N \geq 3$.

I think I made an error. Let me recheck.

The $A$-side degree $r_i$ = number of $B$-players that $i$ beats. The $B$-side "loss degree" = number of $A$-players that beat $j$ = number of $A$-players that $j$ loses to. These should sum to the same total (number of $A \to B$ edges).

$\sum_{i \in A} r_i = \sum_{i=1}^{(N+1)/2} ((N+1)/2 - i) = \sum_{k=0}^{(N-1)/2} k = \frac{((N-1)/2)((N+1)/2)}{2} = \frac{(N-1)(N+1)}{8}$.

$\sum_{j \in B} (\text{losses to } A) = \sum_{j=(N+3)/2}^{N} (j - (N+3)/2 + 1 - 1)$... let me just recompute. Losses to $A$ for player $j$ = $|A| - s_j = (N+1)/2 - (N+1-j) = j - (N+1)/2 - 1$.

Wait: $(N+1)/2 - (N + 1 - j) = (N+1)/2 - N - 1 + j = j + (N+1)/2 - N - 1 = j - (N-1)/2 - 1 = j - (N+1)/2$.

Let me be very careful: $(N+1)/2 - (N + 1 - j) = (N+1)/2 - N - 1 + j = j + (N+1)/2 - N - 1 = j - N + (N+1)/2 - 1 = j - N + (N-1)/2 = j - (N+1)/2$.

So losses to $A$ for player $j = (N+3)/2$: $(N+3)/2 - (N+1)/2 = 1$. For $j = N$: $N - (N+1)/2 = (N-1)/2$.

So losses to $A$ for $B$ players: $1, 2, \ldots, (N-1)/2$ (for $j = (N+3)/2, \ldots, N$). That's $(N-1)/2$ values.

Sum: $\sum_{k=1}^{(N-1)/2} k = \binom{(N+1)/2}{2} = \frac{(N+1)(N-1)}{8}$. ✓ Now they match!

I made an arithmetic error before. Let me redo: $j$ ranges from $(N+3)/2$ to $N$, that's $(N-1)/2$ players. Losses: $j - (N+1)/2$ for $j = (N+3)/2, \ldots, N$, giving $1, 2, \ldots, (N-1)/2$.

And $r_i$ for $i = 1, \ldots, (N+1)/2$: $(N+1)/2 - i$ for $i = 1, \ldots, (N+1)/2$, giving $(N-1)/2, (N-3)/2, \ldots, 1, 0$. That's $(N+1)/2$ values, sum = $\binom{(N+1)/2}{2}$.

And $B$-side losses: $1, 2, \ldots, (N-1)/2$, sum = $\binom{(N+1)/2}{2}$. ✓

But the $A$-side has $(N+1)/2$ vertices with degrees $(N-1)/2, (N-3)/2, \ldots, 0$, and $B$-side has $(N-1)/2$ vertices with degrees $1, 2, \ldots, (N-1)/2$.

Hmm, the $A$-side has a vertex with degree 0 (player $(N+1)/2$ beats no one in $B$), and the $B$-side has a vertex with degree $(N-1)/2 = |A|$ (player $N$ loses to all of $A$... wait, no, losses to $A$ = $(N-1)/2 = |A|$, so player $N$ loses to all of $A$). And player $(N+3)/2$ loses to 1 in $A$.

Wait, but player $N$ beats $s_N = 1$ in $A$, and loses to $|A| - 1 = (N-1)/2$ in $A$. But I said losses = $(N-1)/2 = |A|$. That's $|A|$, not $|A| - 1$. Contradiction! If losses = $|A|$, then $s_N = 0$, not 1.

Let me recheck. $s_j = N + 1 - j$. $s_N = N + 1 - N = 1$. Losses = $|A| - s_N = (N+1)/2 - 1 = (N-1)/2$. And $j - (N+1)/2 = N - (N+1)/2 = (N-1)/2$. ✓ So losses = $(N-1)/2 = |A| - 1$. And $|A| = (N+1)/2$. So $(N-1)/2 = (N+1)/2 - 1 = |A| - 1$. ✓

I confused myself. Losses to $A$ for player $N$ is $(N-1)/2 = |A| - 1$, not $|A|$. Good.

So the bipartite degree sequences are:
- $A$-side (beats in $B$): $(N-1)/2, (N-3)/2, \ldots, 1, 0$ (for players $1, 2, \ldots, (N+1)/2$).
- $B$-side (losses to $A$): $1, 2, \ldots, (N-1)/2$ (for players $(N+3)/2, \ldots, N$).

$B$-side has $(N-1)/2$ vertices with degrees $1, 2, \ldots, (N-1)/2$. $A$-side has $(N+1)/2$ vertices with degrees $(N-1)/2, \ldots, 1, 0$.

By Gale-Ryser / bipartite graph realization theorem, we need to check if this is realizable. The $A$-side degrees sorted descending: $(N-1)/2, (N-3)/2, \ldots, 0$. The $B$-side degrees sorted descending: $(N-1)/2, (N-3)/2, \ldots, 1$.

Actually, a simple construction: connect player $i \in A$ to the first $r_i$ players in $B$ (or use a Ferrers diagram). Since the degree sequences are "conjugate" in some sense, this should work.

Actually, let me think of a concrete construction. $A = \{1, \ldots, m\}$ where $m = (N+1)/2$, $B = \{m+1, \ldots, N\}$, $|B| = m - 1$.

$r_i = m - i$ for $i = 1, \ldots, m$. So $r_1 = m - 1 = |B|$, $r_m = 0$.
$B$-side losses: $l_j = j - m$ for $j = m+1, \ldots, N$, i.e., $l_{m+k} = k$ for $k = 1, \ldots, m-1$.

Construction: player $i \in A$ beats players $m+1, m+2, \ldots, m + r_i$ in $B$. So player $i$ beats the first $r_i = m - i$ players in $B$.

Player $j = m + k \in B$ is beaten by players $i$ with $r_i \geq k$, i.e., $m - i \geq k$, i.e., $i \leq m - k$. So players $1, 2, \ldots, m - k$ beat player $m + k$. That's $m - k$ players. And $l_{m+k} = k$... but we need $l_{m+k} = k$, and we got $m - k$.

Hmm, that doesn't match. $m - k \neq k$ in general.

Let me try the other direction: player $i$ beats the LAST $r_i$ players in $B$. Player $i$ beats $m + (m-1) - r_i + 1, \ldots, m + (m-1)$, i.e., players $2m - r_i, \ldots, 2m - 1 = N$. Since $r_i = m - i$, player $i$ beats players $2m - (m-i) = m + i, \ldots, N$. So player $i$ beats players $m+i, m+i+1, \ldots, N$ in $B$, which is $N - (m+i) + 1 = N - m - i + 1 = (m - 1) - i + 1 = m - i = r_i$. ✓

Player $j = m + k$ is beaten by players $i$ with $m + i \leq j \leq N$, i.e., $i \leq j - m = k$. So players $1, \ldots, k$ beat player $m + k$. That's $k$ players. And $l_{m+k} = k$. ✓✓

So the construction works. Player $i \in A$ beats players $m + i, m + i + 1, \ldots, N$ in $B$ (and loses to $m + 1, \ldots, m + i - 1$ in $B$).

Let me verify the full tournament for $N = 5$, $m = 3$.

$A = \{1, 2, 3\}$, $B = \{4, 5\}$.

Within $A$: transitive. $1 \to 2, 1 \to 3, 2 \to 3$.
Within $B$: transitive. $4 \to 5$.

Between $A$ and $B$: player $i$ beats $m + i, \ldots, N$.
- Player 1 beats $4, 5$ (i.e., $m+1 = 4$ to $N = 5$). 
- Player 2 beats $5$ (i.e., $m+2 = 5$). Loses to $4$.
- Player 3 beats nobody in $B$ ($m + 3 = 6 > 5$). Loses to $4, 5$.

So edges:
- $1 \to 2, 1 \to 3, 1 \to 4, 1 \to 5$ (4 wins)
- $2 \to 3, 2 \to 5$, $4 \to 2$ (2 wins: 3 and 5)
- $3$: loses to 1, 2; $3 \to ?$ in $B$: loses to 4, 5. So 0 wins? But we need 2 wins!

Wait, that's wrong. Player 3 should have 2 wins. Let me recheck.

Player 3 is in $A$. Within $A$, player 3 loses to 1 and 2 (0 wins in $A$). Against $B$, player 3 beats nobody (loses to 4 and 5). So total wins = 0. But we need $(N-1)/2 = 2$ wins!

Something is wrong with my construction. Let me recheck.

Oh wait, I think the issue is that within $A$, it's NOT transitive in the way I described. Let me re-examine.

For players in $A$ ($i \leq m$): $d_i^+ = i - 1$ (beats all above) and $d_i^- = (N-1)/2 = m - 1$ (loses to $m - 1$ players below). But player $i$ has $N - i$ players below total. Of those, $m - i$ are in $A$ and $m - 1$ are in $B$. So $d_i^- = m - 1$ means player $i$ loses to $m - 1$ players below. But there are only $m - 1$ players in $B$ below, plus $m - i$ in $A$ below.

For $i = 1$: $d_1^- = m - 1 = 2$ (for $N = 5$). Players below 1: 2, 3, 4, 5 (4 players). $d_1^- = 2$ means 2 of these beat player 1. Wins against below: $4 - 2 = 2$. Plus wins against above: 0. Total: 2. ✓

For $i = 3$ (= $m$): $d_3^- = m - 1 = 2$. Players below 3: 4, 5 (2 players). $d_3^- = 2$ means both 4 and 5 beat player 3. Wins against below: 0. Wins against above: $d_3^+ = 2$ (beats players 1 and 2). Total: 2. ✓

Ah, I see! Player 3 beats players 1 and 2 (upsets!), not the other way around. I had the within-$A$ tournament wrong.

Let me redo. Within $A$, player $i$ beats all $i - 1$ players ABOVE (lower index). So it's the REVERSE transitive tournament: $m \to m-1 \to \cdots \to 1$. Player $i$ beats $1, 2, \ldots, i - 1$.

For $N = 5$, $m = 3$:
- Within $A$: $3 \to 2, 3 \to 1, 2 \to 1$. (Player 3 beats 1 and 2, player 2 beats 1.)
- Within $B$: $5 \to 4$ (reverse transitive: $N \to N-1 \to \cdots$). Player $j$ beats all above in $B$: $j$ beats $(N+1)/2 + 1, \ldots, j - 1$.

Wait, within $B$, player $j$ beats all above in $B$ (lower index in $B$). So $5 \to 4$. Player 5 beats 4.

- Between $A$ and $B$: player $i \in A$ beats $m + i, \ldots, N$ in $B$.
  - Player 1 beats 4, 5.
  - Player 2 beats 5, loses to 4.
  - Player 3 loses to 4, 5.

Let me compute wins:
- Player 1: beats 4, 5 (from cross), loses to 2, 3 (within $A$). Wins = 2. ✓
- Player 2: beats 1 (within $A$), beats 5 (cross), loses to 3 (within $A$), loses to 4 (cross). Wins = 2. ✓
- Player 3: beats 1, 2 (within $A$), loses to 4, 5 (cross). Wins = 2. ✓
- Player 4: beats 2, 3 (cross), loses to 1 (cross), loses to 5 (within $B$). Wins = 2. ✓
- Player 5: beats 3, 4 (within $B$ and cross: 5 beats 4 within $B$, and 5 beats 3 cross), loses to 1, 2 (cross). Wins = 2. ✓

All have 2 wins. Now count upsets (higher index beats lower index):
- (1,2): 2 beats 1? Yes (within $A$, 2 → 1). Upset! ✓
- (1,3): 3 beats 1? Yes. Upset! ✓
- (1,4): 4 beats 1? No, 1 beats 4. Not upset.
- (1,5): 5 beats 1? No, 1 beats 5. Not upset.
- (2,3): 3 beats 2? Yes. Upset! ✓
- (2,4): 4 beats 2? Yes. Upset! ✓
- (2,5): 5 beats 2? Yes. Upset! ✓
- (3,4): 4 beats 3? Yes. Upset! ✓
- (3,5): 5 beats 3? Yes. Upset! ✓
- (4,5): 5 beats 4? Yes. Upset! ✓

Upsets: (1,2), (1,3), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5) = 8 upsets!

But we computed the upper bound as 7! Something is wrong.

Wait, let me recount. That's 8 upsets out of 10 matches. But the upper bound was 7. Let me recheck.

Hmm, let me recount the upsets:
- (1,2): 2 beats 1. Upset.
- (1,3): 3 beats 1. Upset.
- (1,4): 1 beats 4. Not upset.
- (1,5): 1 beats 5. Not upset.
- (2,3): 3 beats 2. Upset.
- (2,4): 4 beats 2. Upset.
- (2,5): 5 beats 2. Upset.
- (3,4): 4 beats 3. Upset.
- (3,5): 5 beats 3. Upset.
- (4,5): 5 beats 4. Upset.

That's 8 upsets. But $w = (2, 2, 2, 2, 2)$, non-increasing. Final ranking = 1, 2, 3, 4, 5 = initial. ✓

So 8 upsets is achievable, but my upper bound said 7. I must have made an error in the upper bound derivation.

Let me recheck. $U = \sum d_i^+$. $d_i^+$ = number of upsets where $i$ beats someone above = number of $j < i$ that $i$ beats.

- $d_1^+ = 0$ (nobody above).
- $d_2^+ = 1$ (beats 1).
- $d_3^+ = 2$ (beats 1, 2).
- $d_4^+ = 2$ (beats 2, 3).
- $d_5^+ = 2$ (beats 3, 4).

$U = 0 + 1 + 2 + 2 + 2 = 7$.

But I counted 8 upsets! Let me recheck which are upsets.

An upset is when the winner had a LOWER initial ranking, i.e., higher number. So for pair $(i, j)$ with $i < j$, it's an upset if $j$ beats $i$.

- (1,2): $j = 2$ beats $i = 1$. Upset. This contributes to $d_2^+$.
- (1,3): 3 beats 1. Upset. Contributes to $d_3^+$.
- (1,4): 1 beats 4. Not upset.
- (1,5): 1 beats 5. Not upset.
- (2,3): 3 beats 2. Upset. $d_3^+$.
- (2,4): 4 beats 2. Upset. $d_4^+$.
- (2,5): 5 beats 2. Upset. $d_5^+$.
- (3,4): 4 beats 3. Upset. $d_4^+$.
- (3,5): 5 beats 3. Upset. $d_5^+$.
- (4,5): 5 beats 4. Upset. $d_5^+$.

$d_2^+ = 1$ (beats 1). $d_3^+ = 2$ (beats 1, 2). $d_4^+ = 2$ (beats 2, 3). $d_5^+ = 3$ (beats 2, 3, 4).

Wait, player 5 beats 2, 3, and 4. That's 3 upsets for player 5, not 2!

Let me recheck player 5's wins. Player 5 beats: 4 (within $B$), 3 (cross: 5 beats 3), 2 (cross: 5 beats 2). And loses to 1 (cross: 1 beats 5). So wins = 3, not 2!

I made an error earlier. Let me recompute all wins.

Edges:
- Within $A$ (reverse transitive): $3 \to 2, 3 \to 1, 2 \to 1$.
- Within $B$ (reverse transitive): $5 \to 4$.
- Cross: player $i \in A$ beats $m + i, \ldots, N$.
  - Player 1 beats 4, 5.
  - Player 2 beats 5, loses to 4.
  - Player 3 loses to 4, 5.

So:
- Player 1: beats 4, 5 (cross). Loses to 2, 3 (within $A$). Wins = 2.
- Player 2: beats 1 (within $A$), beats 5 (cross). Loses to 3 (within $A$), loses to 4 (cross). Wins = 2.
- Player 3: beats 1, 2 (within $A$). Loses to 4, 5 (cross). Wins = 2.
- Player 4: beats 2, 3 (cross). Loses to 1 (cross), loses to 5 (within $B$). Wins = 2.
- Player 5: beats 3, 4 (cross: 5 beats 3; within $B$: 5 beats 4). Loses to 1, 2 (cross). Wins = 2.

Wait, does 5 beat 2? Cross edges: player 2 beats 5 (player 2 beats $m + 2 = 5$). So 2 beats 5, not 5 beats 2!

Let me recheck. Cross: player $i \in A$ beats $m + i, \ldots, N$. Player 2 beats $m + 2 = 5$. So 2 → 5. Player 5 does NOT beat 2.

So player 5's wins: beats 4 (within $B$), beats 3 (cross: player 3 loses to 5, since player 3 beats nobody in $B$). Loses to 1 (1 beats 5), loses to 2 (2 beats 5). Wins = 2. ✓

Let me recount upsets:
- (1,2): 2 beats 1. ✓ Upset.
- (1,3): 3 beats 1. ✓ Upset.
- (1,4): 1 beats 4. Not upset.
- (1,5): 1 beats 5. Not upset.
- (2,3): 3 beats 2. ✓ Upset.
- (2,4): 4 beats 2. ✓ Upset.
- (2,5): 2 beats 5. Not upset.
- (3,4): 4 beats 3. ✓ Upset.
- (3,5): 5 beats 3. ✓ Upset.
- (4,5): 5 beats 4. ✓ Upset.

Upsets: (1,2), (1,3), (2,3), (2,4), (3,4), (3,5), (4,5) = 7. ✓

I made an error before (said 5 beats 2, but actually 2 beats 5). So 7 upsets, matching the upper bound. 

So the answer is $\frac{(N-1)(3N-1)}{8}$.

Wait, but I need to double-check my upper bound derivation more carefully, since I want to make sure it's correct.

Let me re-derive. We have $h$ non-decreasing, $0 \leq h_i \leq N-1$, $\sum h_i = \binom{N}{2}$, and $U \leq \sum \min(i-1, N-1-h_i)$.

$g_i = \min(i-1, N-1-h_i)$. Since $h$ is non-decreasing, $N-1-h_i$ is non-increasing. $i-1$ is increasing. So $g_i$ first increases (bounded by $i-1$) then decreases (bounded by $N-1-h_i$).

Let $k$ be the largest index where $i - 1 \leq N - 1 - h_i$, i.e., $h_i \leq N - i$. For $i \leq k$, $g_i = i - 1$. For $i > k$, $g_i = N - 1 - h_i$.

$U \leq \sum_{i=1}^k (i-1) + \sum_{i=k+1}^N (N-1-h_i) = \binom{k}{2} + (N-k)(N-1) - \sum_{i=k+1}^N h_i$.

$\sum_{i=k+1}^N h_i = \binom{N}{2} - \sum_{i=1}^k h_i$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + \sum_{i=1}^k h_i$.

Now, $\sum_{i=1}^k h_i \leq ?$. Since $h$ is non-decreasing and $h_k \leq N - k$ (by definition of $k$), we have $h_i \leq h_k \leq N - k$ for $i \leq k$. So $\sum_{i=1}^k h_i \leq k(N-k)$.

$U \leq \binom{k}{2} + (N-k)(N-1) - \binom{N}{2} + k(N-k) = \binom{N}{2} - \binom{k}{2}$ (as computed before).

Now, to minimize $k$ (maximize $U$), we need the constraints to be feasible. The key constraint is that we need $h$ non-decreasing with $h_k \leq N - k$ and $h_{k+1} \geq N - (k+1) = N - k - 1$ (by definition of $k$, $h_{k+1} > N - (k+1)$... actually $h_{k+1} \geq N - (k+1) + 1$? No, $k$ is the largest where $h_k \leq N - k$, so $h_{k+1} > N - (k+1)$, i.e., $h_{k+1} \geq N - k$).

And $h_k \leq h_{k+1}$ (non-decreasing), so $h_k \leq h_{k+1}$, with $h_k \leq N - k$ and $h_{k+1} \geq N - k$. So $h_k \leq N - k \leq h_{k+1}$. This is consistent.

Now, $\sum h_i = \binom{N}{2}$. We need to find the minimum $k$ such that a non-decreasing sequence $h$ exists with $h_k \leq N - k$, $h_{k+1} \geq N - k$, $0 \leq h_i \leq N - 1$, and $\sum h_i = \binom{N}{2}$.

To minimize $k$, we want to push as much "mass" to the first $k$ terms as possible (making $k$ small) while keeping $h$ non-decreasing and $h_k \leq N - k$.

The maximum $\sum_{i=1}^k h_i$ with $h$ non-decreasing and $h_k \leq N - k$ is $k(N-k)$ (all equal to $N - k$). Then $\sum_{i=k+1}^N h_i = \binom{N}{2} - k(N-k)$.

For $i > k$, $h$ is non-decreasing with $h_{k+1} \geq N - k$ and $h_i \leq N - 1$. The minimum sum for $i > k$ is $(N-k)(N-k)$ (all equal to $N - k$). We need $\binom{N}{2} - k(N-k) \geq (N-k)(N-k)$, i.e., $\binom{N}{2} \geq (N-k) \cdot k + (N-k)^2 = (N-k)(k + N - k) = N(N-k)$.

$\binom{N}{2} \geq N(N-k) \Leftrightarrow \frac{N-1}{2} \geq N - k \Leftrightarrow k \geq N - \frac{N-1}{2} = \frac{N+1}{2}$.

So $k \geq (N+1)/2$, and the minimum is $k = (N+1)/2$.

At $k = (N+1)/2$: $h_i = N - k = (N-1)/2$ for all $i$ (constant). $\sum h_i = N \cdot (N-1)/2 = \binom{N}{2}$. ✓. And $h$ is non-decreasing (constant). ✓. $h_k = (N-1)/2 = N - k$. ✓.

$U \leq \binom{N}{2} - \binom{(N+1)/2}{2} = \frac{N(N-1)}{2} - \frac{(N+1)(N-1)}{8} = \frac{(N-1)(4N - (N+1))}{8} = \frac{(N-1)(3N-1)}{8}$.

And we showed this is achievable with the regular tournament construction. So the answer is $\frac{(N-1)(3N-1)}{8}$.

But wait, I need to also verify that the upper bound derivation is tight, i.e., that $U = \sum g_i$ is actually achievable (not just an upper bound). In our construction, $d_i^+ = g_i$ for all $i$, and we verified the tournament exists. So yes, it's tight.

Actually, I should also verify that the bound $U \leq \sum g_i$ is correct. We have $d_i^+ \leq \min(i-1, f_i + N - i) = \min(i-1, N - 1 - h_i) = g_i$. So $U = \sum d_i^+ \leq \sum g_i$. ✓

And in the construction, $d_i^+ = g_i$ for all $i$. ✓

Let me also verify for $N = 3$: $\frac{2 \cdot 8}{8} = 2$. ✓ (We found 2 upsets.)

For $N = 7$: $\frac{6 \cdot 20}{8} = 15$. Total matches = 21. So 15 upsets out of 21.

Let me also make sure the construction generalizes. For general odd $N$, $m = (N+1)/2$:

- Within $A = \{1, \ldots, m\}$: reverse transitive. Player $i$ beats $1, \ldots, i-1$.
- Within $B = \{m+1, \ldots, N\}$: reverse transitive. Player $j$ beats $m+1, \ldots, j-1$.
- Cross: player $i \in A$ beats $m+i, \ldots, N$ in $B$.

Each player has $(N-1)/2$ wins (regular tournament). The number of upsets is $\frac{(N-1)(3N-1)}{8}$.

Let me verify the cross edges more carefully. Player $i \in A$ beats $m + i, m + i + 1, \ldots, N$ in $B$. Number of such players: $N - (m + i) + 1 = N - m - i + 1 = (N - 1)/2 - i + 1 = (N + 1)/2 - i = m - i$. And $r_i = m - i$. ✓

Player $j = m + k \in B$ (where $k = 1, \ldots, (N-1)/2$) is beaten by players $i$ with $m + i \leq j$, i.e., $i \leq k$. So players $1, \ldots, k$ beat player $j$. Player $j$ loses to $k$ players in $A$ and beats $m - 1 - k$ players in $A$ (those $i$ with $i > k$, i.e., $i = k+1, \ldots, m$). Wait, $|A| = m$, and $k$ beat $j$, so $m - k$ lose to $j$, i.e., $j$ beats $m - k$ in $A$.

Player $j$'s total wins: wins in $B$ + wins against $A$. Wins in $B$: $j$ beats $m+1, \ldots, j-1$ (reverse transitive), that's $j - m - 1 = k - 1$ wins. Wins against $A$: $m - k$. Total: $(k - 1) + (m - k) = m - 1 = (N-1)/2$. ✓

Great, the construction works for all odd $N \geq 3$.

Now let me also make sure the upper bound proof is complete. I need to show that for ANY tournament with final ranking = initial ranking, $U \leq \frac{(N-1)(3N-1)}{8}$.

The key steps:
1. Define $f_i = d_i^+ - d_i^-$, so $w_i = (N-i) + f_i$.
2. Non-increasing $w$ gives $f_{i+1} \leq f_i + 1$.
3. $\sum f_i = 0$.
4. $d_i^+ \leq \min(i-1, f_i + N - i)$ (from $d_i^+ \leq i - 1$ and $d_i^+ = f_i + d_i^- \leq f_i + (N - i)$).
5. Let $h_i = (i-1) - f_i$, so $h$ is non-decreasing, $\sum h_i = \binom{N}{2}$, $0 \leq h_i \leq N-1$.
6. $d_i^+ \leq \min(i-1, N - 1 - h_i) = g_i$.
7. $U \leq \sum g_i$.
8. With crossover at $k$: $U \leq \binom{N}{2} - \binom{k}{2}$, and $k \geq (N+1)/2$.
9. So $U \leq \binom{N}{2} - \binom{(N+1)/2}{2} = \frac{(N-1)(3N-1)}{8}$.

This is rigorous. The construction achieves equality. So the answer is $\boxed{\frac{(N-1)(3N-1)}{8}}$.

Let me also sanity-check: is this always an integer? $(N-1)(3N-1)$: $N$ odd means $N - 1$ even. $3N - 1$: $N$ odd means $3N$ odd, $3N - 1$ even. So $(N-1)(3N-1)$ is divisible by 4. Is it divisible by 8? $(N-1)/2$ is an integer. $(3N-1)/2$: $3N - 1$ is even, so yes. So $\frac{(N-1)(3N-1)}{8} = \frac{(N-1)/2 \cdot (3N-1)/2}{2}$. We need $(N-1)(3N-1) \equiv 0 \pmod{8}$.

$N$ odd: $N = 2m + 1$. $N - 1 = 2m$, $3N - 1 = 6m + 2 = 2(3m + 1)$. Product: $4m(3m + 1)$. Need $m(3m + 1) \equiv 0 \pmod{2}$. If $m$ even, yes. If $m$ odd, $3m + 1$ is even, yes. So always divisible by 8. ✓

Now let me write up the proof cleanly.

Actually, wait. I want to double-check step 4 more carefully. $d_i^+ \leq f_i + (N - i)$: this comes from $d_i^+ = f_i + d_i^-$ and $d_i^- \leq N - i$ (can't lose to more than $N - i$ players below). ✓

And $d_i^+ \leq i - 1$: can't beat more than $i - 1$ players above. ✓

Also, I should verify that $h_i \geq 0$: $h_i = (i-1) - f_i = (i-1) - (w_i - (N-i)) = (i-1) - w_i + (N-i) = N - 1 - w_i$. Since $w_i \leq N - 1$, $h_i \geq 0$. ✓

And $h_i \leq N - 1$: $h_i = N - 1 - w_i \leq N - 1$ since $w_i \geq 0$. ✓

Good. The proof is complete.

Let me also think about whether I need Landau's theorem or any tournament realizability condition. In the upper bound, I only used the constraints on $d_i^+, d_i^-$, which are necessary conditions. The upper bound holds for any valid tournament. For the lower bound (construction), I explicitly constructed a valid tournament. So no need for Landau's theorem.

Let me write the proof.
