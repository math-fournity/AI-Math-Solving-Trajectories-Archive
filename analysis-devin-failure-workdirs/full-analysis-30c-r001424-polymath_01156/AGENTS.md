# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Problem 10.8. Two bandits stole 300 gold coins. They decided to divide them as follows: the first bandit puts some coins (possibly all) into a bag, and the second bandit chooses who gets this bag; then this action is repeated several times. The division ends when

- either all the money is gone,
- or someone gets 11 bags - in this case, all the remaining money immediately goes to the other bandit.

What is the maximum number of coins that the first bandit can guarantee to get?       — 题目文本
#   Answer: 146.

Solution. First, we will show that the first bandit can get at least 146 coins. His strategy will be to put 14 coins in each bag. First, note that he will always be able to do this: since $21 \cdot 14=294$, he will do this at least 21 times, and when the coins start to run out, the process will certainly be over (one of the bandits will get 11 bags).

Let's analyze how the game can end. If the first bandit has accumulated 11 bags, that's already 154 coins. In the other case, the second bandit, on the contrary, has no more than 11 bags, that is, no more than 154 coins. Therefore, the remaining coins are with the first bandit, which is at least 146.

Now we will show how the second bandit can guarantee himself 154 coins. His strategy is as follows: take bags with 14 coins or more for himself, and give bags with 13 coins or less to the first bandit.

Similarly, let's analyze how the game can end. If the second bandit finishes with 11 bags, he will have at least 154 coins. In the other case, the first bandit will finish with no more than 11 bags, which is no more than $11 \cdot 13=143$ coins. Then the second bandit will have at least 157 coins.

Remark. Let's indicate how to get the answer in the general case. Suppose there are $N$ coins in total, and each bandit can get no more than $k$ bags ($N \geqslant 2 k$). We will divide the coins into $2 k$ almost equal groups, so that either all groups have the same number of coins (if $N \vdots 2 k$), or the number of coins in the groups differs by no more than 1 (such a division is unique). We will order the groups in ascending order. By reasoning similar to the one provided above, we can show that the first bandit can guarantee himself the sum of the $k$ smaller groups of the division, and the second bandit can guarantee the sum of the $k$ larger groups.

## 11th Grade  — 标准解答
#   Let me solve this problem. This is a game theory problem about two bandits dividing 300 gold coins.

Let me understand the rules:
- First bandit puts some coins (possibly all) into a bag
- Second bandit chooses who gets this bag
- This action is repeated several times
- Division ends when:
  - All money is gone, OR
  - Someone gets 11 bags - in this case all remaining money goes to the other bandit

Question: What is the maximum number of coins the first bandit can guarantee to get?

Let me think about this carefully. The first bandit (let's call A) chooses how many coins to put in each bag. The second bandit (B) chooses who gets each bag. B will always give each bag to the person for whom it's worse (from A's perspective), i.e., B minimizes A's total.

The game ends when:
1. All coins are distributed, or
2. Someone reaches 11 bags, and the other person gets all remaining coins.

A wants to maximize his guaranteed coins. B wants to minimize A's coins (equivalently maximize B's own).

Let me think about the structure. A controls the bag sizes. B controls the allocation. The constraint is the 11-bag limit.

If A puts coins in bags and B allocates them, B will try to make one person reach 11 bags quickly. If A reaches 11 bags, B gets all remaining coins. If B reaches 11 bags, A gets all remaining coins.

So B wants to give bags to A (to make A reach 11 first, so B gets the remainder). But B also wants to keep the valuable bags for himself.

Wait, let me reconsider. B chooses who gets each bag. B wants to maximize B's own coins. 

Strategy for B: For each bag, B can either take it himself or give it to A. 

If B gives a bag to A, A's bag count increases. If A reaches 11 bags, B gets all remaining coins.
If B takes a bag, B's bag count increases. If B reaches 11 bags, A gets all remaining coins.

So there's tension: B wants to take large bags for himself, but taking too many bags means B reaches 11 first and A gets the remainder.

Let me think about this as a sequential game. A chooses bag sizes one at a time (or all at once?). Actually, the problem says "this action is repeated several times" - so it's sequential. A puts coins in a bag, B allocates, repeat.

Actually, A can adapt based on previous allocations. So it's a sequential game with perfect information.

Let me think about what A can guarantee.

Let's say at any point, A has $a$ bags and $x$ coins, B has $b$ bags and $y$ coins, and $r$ coins remain. $a + b$ bags have been given out, $x + y + r = 300$.

A's turn: A puts $c$ coins in a bag ($1 \le c \le r$). B chooses who gets it.

If B gives to A: A now has $a+1$ bags, $x+c$ coins. If $a+1 = 11$, B gets all $r - c$ remaining coins.
If B gives to B: B now has $b+1$ bags, $y+c$ coins. If $b+1 = 11$, A gets all $r - c$ remaining coins.

A wants to maximize his final total. B wants to minimize A's final total.

Let me think about the endgame. When someone has 10 bags, the next bag they receive gives them 11, and the other person gets the remainder.

Key insight: A controls bag sizes. B controls allocation. A can try to make bags of specific sizes to create dilemmas for B.

Let me think about small cases first to build intuition.

Let me think about the state as $(a, b, r)$ where $a$ = A's bags, $b$ = B's bags, $r$ = remaining coins. A's accumulated coins don't matter for the decision (only final total matters), but actually they do matter because the game could end with all coins distributed.

Hmm, actually this is complex. Let me think about it differently.

Let me define $V(a, b, r)$ = the maximum coins A can guarantee from state $(a, b, r)$, assuming A has already collected some coins (which we track separately). Actually, let me think of it as: from state $(a, b, r)$ with A having collected $x$ and B having collected $y$ ($x + y + r = 300$), A wants to maximize his final total.

Actually, the coins already collected don't affect future decisions - only $a$, $b$, and $r$ matter for the future. The coins already collected are sunk. So let $f(a, b, r)$ = additional coins A can guarantee from this state (beyond what he already has).

A chooses $c \in \{1, 2, ..., r\}$.
B then chooses:
- Give to A: A gets $c$ from this bag. If $a+1 = 11$, game ends, A gets $c$ total (no more). So A gets $c$.
  - If $a+1 < 11$: A gets $c + f(a+1, b, r-c)$.
- Give to B: A gets $0$ from this bag. If $b+1 = 11$, game ends, A gets all $r - c$ remaining.
  - If $b+1 < 11$: A gets $f(a, b+1, r-c)$.

B minimizes A's gain, so B chooses the option giving A less.

$f(a, b, r) = \max_{c} \min(\text{give to A}, \text{give to B})$

where:
- give to A = $c + f(a+1, b, r-c)$ if $a+1 < 11$, else $c$
- give to B = $r - c$ if $b+1 = 11$, else $f(a, b+1, r-c)$

Base case: $f(a, b, 0) = 0$ (no coins left).

We want $f(0, 0, 300)$.

This is a complex dynamic program. Let me think about the structure more.

When $a = 10$ (A has 10 bags): If B gives a bag to A, A reaches 11 and B gets the remainder. So B would give to A only if giving to A is worse for A than giving to B.

When $a = 10$: A chooses $c$. 
- Give to A: A gets $c$ (game ends, B gets $r-c$).
- Give to B: B gets bag, $b+1$ bags. If $b+1 = 11$, A gets $r - c$. Otherwise, $f(10, b+1, r-c)$.

B minimizes, so B gives to A if $c \le$ (give to B value), and gives to B otherwise.

When $b = 10$ (B has 10 bags): If B gives a bag to B, B reaches 11 and A gets the remainder. So:
- Give to A: $c + f(a+1, 10, r-c)$ if $a+1 < 11$, else $c$.
- Give to B: A gets $r - c$ (game ends).

B minimizes: gives to B if $r - c \le$ (give to A value), gives to A otherwise.

This is getting complex. Let me think about it more cleverly.

Let me think about the total number of bags. The game ends when someone has 11 bags or all coins are gone. The maximum number of bags is 21 (10 each + 1 more to someone). Actually, if both have 10, the next bag goes to someone making them 11, so max 21 bags.

Actually, the game can end earlier if coins run out. With 300 coins, if each bag has at least 1 coin, we can have at most 300 bags, but the 11-bag rule caps it at 21 bags.

So the game lasts at most 21 rounds (bags). With 300 coins, coins won't run out before 21 bags (since each bag needs at least 1 coin, 21 bags need at least 21 coins, and we have 300).

Wait, but A could put all remaining coins in one bag. So the number of bags is at most 21 (since someone will reach 11 bags before coins run out, given 300 coins >> 21).

Actually, A controls the bag sizes. A could put many coins in few bags. The game ends when someone has 11 bags OR all coins are gone. If A puts all 300 coins in one bag, then 1 bag is given out, 0 coins remain, game ends. But that's bad for A because B chooses who gets it.

So A wants to spread coins across bags strategically.

Let me think about the key strategic consideration. A wants to maximize his guaranteed coins. B allocates each bag to minimize A's coins.

The critical tension: B wants to give bags to A (to make A reach 11 first, so B gets the remainder). But if B always gives bags to A, A gets all the coins in those bags. B would only give bags to A if the coins in those bags are small, and B would take bags with many coins.

So A's strategy: make bags of specific sizes so that B faces a dilemma. If B takes a bag (large), B's bag count increases, bringing B closer to 11. If B gives to A, A gets the coins but A's bag count increases.

Let me think about the endgame more carefully.

Suppose A has $a$ bags and B has $b$ bags, with $r$ coins remaining. The game will last at most $11 - a + 11 - b - 1 = 21 - a - b$ more bags (until someone reaches 11). Actually, it could end sooner if coins run out, but with enough coins, it lasts until someone reaches 11.

Let me think about the case where coins are plentiful (won't run out). Then the game always ends with someone reaching 11 bags.

If A reaches 11 first (after receiving the $k$-th bag where $k = 11 - a$ more bags to A), B gets all remaining coins.
If B reaches 11 first, A gets all remaining coins.

So the question is: who reaches 11 first, and how many coins are distributed before that?

B controls allocation. B will try to reach a state where B gets the most coins. 

Let me think about it from B's perspective. B wants to maximize B's coins = 300 - A's coins. 

If the game ends with A reaching 11 bags, B gets all remaining coins at that point. B's coins = coins in bags B received + remaining coins.
If the game ends with B reaching 11 bags, A gets all remaining coins. A's coins = coins in bags A received + remaining coins.

So B wants to either:
1. Make A reach 11 first (B gets remainder), while keeping the bags B received large, OR
2. Make B reach 11 first (A gets remainder), but only if the bags B received are so large that even giving up the remainder is worth it.

Hmm, this is a complex game. Let me try to think about it with the DP approach but for specific small cases.

Let me try to compute $f(a, b, r)$ for small values and see if I can find a pattern.

Actually, with 300 coins and at most 21 bags, the state space is manageable: $a \in \{0,...,10\}$, $b \in \{0,...,10\}$, $r \in \{0,...,300\}$. That's $11 \times 11 \times 301 \approx 36000$ states. But computing this by hand is infeasible.

Let me think about the structure more cleverly.

Key observation: Since 300 >> 21, coins will never run out before someone reaches 11 bags (as long as A puts at least 1 coin per bag, which A must). So the game always ends with someone reaching 11 bags.

Wait, A could put all remaining coins in one bag. But that would mean fewer bags. If A puts all $r$ coins in one bag, the game gives out 1 bag, and if no one reaches 11, continues with 0 coins remaining, so game ends with all coins distributed. But this is only relevant if $a + b < 10$ (i.e., neither is close to 11).

Actually, A must put at least 1 coin per bag (some coins, possibly all). So if A always puts exactly 1 coin per bag, after 21 bags (someone reaches 11), 21 coins are distributed and 279 go to the other person. That's terrible for A if A reaches 11 first.

Let me think about what happens when A reaches 11 first. A has 11 bags, B gets all remaining coins. A's total = sum of coins in A's 11 bags. B's total = sum of coins in B's bags + remaining.

If B reaches 11 first. B has 11 bags, A gets all remaining coins. A's total = sum of coins in A's bags + remaining. B's total = sum of coins in B's 11 bags.

So A wants B to reach 11 first (so A gets the remainder), and A wants the bags B takes to be small (so B's total is small, meaning A's is large).

B wants A to reach 11 first (so B gets the remainder), and B wants the bags A gets to be small.

But B controls allocation. So B will try to give bags to A (to make A reach 11 first) unless the bag is too valuable.

Let me think about the equilibrium. A chooses bag sizes to create the worst dilemma for B.

Let me consider a simplified version: suppose the game must end with someone reaching 11 bags (coins are plentiful). A has $a$ bags, B has $b$ bags. The game will last exactly $\min(11-a, 11-b) + $ some more bags until someone reaches 11.

Actually, the number of bags until someone reaches 11: if B always gives to A, A reaches 11 after $11 - a$ bags. If B always takes, B reaches 11 after $11 - b$ bags. B will mix to optimize.

Let me think about the last few bags.

When $a = 10, b = 10$: A puts $c$ coins. 
- Give to A: A reaches 11, A gets $c$, B gets $r - c$. A's gain = $c$.
- Give to B: B reaches 11, A gets $r - c$. A's gain = $r - c$.
B minimizes A's gain: $\min(c, r-c)$. A maximizes: $\max_c \min(c, r-c) = \lfloor r/2 \rfloor$ (by choosing $c = \lfloor r/2 \rfloor$ or $\lceil r/2 \rceil$).

So $f(10, 10, r) = \lfloor r/2 \rfloor$.

When $a = 10, b = 9$: A puts $c$ coins.
- Give to A: A reaches 11, A gets $c$. A's gain = $c$.
- Give to B: B has 10 bags. $f(10, 10, r-c) = \lfloor (r-c)/2 \rfloor$.
B minimizes: $\min(c, \lfloor (r-c)/2 \rfloor)$.
A maximizes: $\max_c \min(c, \lfloor (r-c)/2 \rfloor)$.

Let me find the optimal $c$. We want $c \approx \lfloor (r-c)/2 \rfloor$, i.e., $c \approx (r-c)/2$, so $3c \approx r$, $c \approx r/3$.

$f(10, 9, r) \approx r/3$.

When $a = 10, b = 8$: 
- Give to A: A gets $c$.
- Give to B: $f(10, 9, r-c) \approx (r-c)/3$.
$\min(c, (r-c)/3)$. Set $c = (r-c)/3$: $4c = r$, $c = r/4$.
$f(10, 8, r) \approx r/4$.

Pattern: $f(10, b, r) \approx r / (11 - b)$.

Let me verify: $f(10, 10, r) = r/2 = r/(11-10)$. ✓
$f(10, 9, r) = r/3 = r/(11-9)$. ✓
$f(10, 8, r) = r/4 = r/(11-8)$. ✓

So $f(10, b, r) \approx r / (11 - b)$.

Now let's go to $a = 9$.

$f(9, b, r)$: A puts $c$.
- Give to A: $c + f(10, b, r-c) \approx c + (r-c)/(11-b)$.
- Give to B: $f(9, b+1, r-c)$.

B minimizes. Let me compute $f(9, 10, r)$ first.

$f(9, 10, r)$: A puts $c$.
- Give to A: $c + f(10, 10, r-c) = c + \lfloor (r-c)/2 \rfloor \approx c + (r-c)/2 = (r+c)/2$.
- Give to B: B reaches 11, A gets $r - c$.
B minimizes: $\min((r+c)/2, r-c)$.
Set $(r+c)/2 = r-c$: $r + c = 2r - 2c$, $3c = r$, $c = r/3$.
$f(9, 10, r) \approx (r + r/3)/2 = (4r/3)/2 = 2r/3$.

Alternatively, $r - c = r - r/3 = 2r/3$. ✓

$f(9, 9, r)$: A puts $c$.
- Give to A: $c + f(10, 9, r-c) \approx c + (r-c)/3 = (3c + r - c)/3 = (r + 2c)/3$.
- Give to B: $f(9, 10, r-c) \approx 2(r-c)/3$.
B minimizes: $\min((r+2c)/3, 2(r-c)/3)$.
Set equal: $r + 2c = 2r - 2c$, $4c = r$, $c = r/4$.
$f(9, 9, r) \approx (r + 2 \cdot r/4)/3 = (r + r/2)/3 = (3r/2)/3 = r/2$.

Check: $2(r - r/4)/3 = 2 \cdot 3r/4 / 3 = r/2$. ✓

$f(9, 8, r)$:
- Give to A: $c + f(10, 8, r-c) \approx c + (r-c)/4 = (r + 3c)/4$.
- Give to B: $f(9, 9, r-c) \approx (r-c)/2$.
Set equal: $(r + 3c)/4 = (r-c)/2$, $r + 3c = 2r - 2c$, $5c = r$, $c = r/5$.
$f(9, 8, r) \approx (r + 3r/5)/4 = (8r/5)/4 = 2r/5$.

Check: $(r - r/5)/2 = (4r/5)/2 = 2r/5$. ✓

Pattern for $f(9, b, r)$:
- $f(9, 10, r) = 2r/3$
- $f(9, 9, r) = r/2 = 2r/4$
- $f(9, 8, r) = 2r/5$

So $f(9, b, r) \approx 2r / (12 - b)$.

Let me check: $f(9, 10) = 2r/2 = r$? No, $12 - 10 = 2$, $2r/2 = r$. But we computed $2r/3$. That doesn't match.

Let me recompute. $f(9, 10, r) = 2r/3$. $12 - 10 = 2$. $2r/2 = r \neq 2r/3$.

Hmm, let me reconsider. Let me tabulate:
- $f(9, 10, r) = 2r/3$
- $f(9, 9, r) = r/2 = 2r/4$  (wait, $r/2 = 2r/4$? No, $r/2 = 2r/4$? $2r/4 = r/2$. Yes.)
- $f(9, 8, r) = 2r/5$

So the denominators are 3, 4, 5. The pattern is $f(9, b, r) = 2r / (b + 3)$? 
- $b=10$: $2r/13$? No, that's $2r/3$.

Wait: $b=10 \to 3$, $b=9 \to 4$, $b=8 \to 5$. So denominator $= 13 - b$.
$f(9, b, r) = 2r / (13 - b)$.

Check: $b=10$: $2r/3$ ✓. $b=9$: $2r/4 = r/2$ ✓. $b=8$: $2r/5$ ✓.

And for $f(10, b, r) = r / (11 - b)$, which we can write as $1 \cdot r / (11 - b)$.

Let me see if there's a general pattern. Let me define $f(a, b, r) = \alpha(a, b) \cdot r$ where $\alpha$ is some fraction.

$f(10, b) = 1/(11-b)$. So $\alpha(10, b) = 1/(11-b)$.
$f(9, b) = 2/(13-b)$. So $\alpha(9, b) = 2/(13-b)$.

Let me compute $f(8, b, r)$ to see the pattern.

$f(8, 10, r)$: A puts $c$.
- Give to A: $c + f(9, 10, r-c) \approx c + 2(r-c)/3 = (3c + 2r - 2c)/3 = (2r + c)/3$.
- Give to B: B reaches 11, A gets $r - c$.
Set equal: $(2r + c)/3 = r - c$, $2r + c = 3r - 3c$, $4c = r$, $c = r/4$.
$f(8, 10, r) \approx (2r + r/4)/3 = (9r/4)/3 = 3r/4$.
Check: $r - r/4 = 3r/4$ ✓.

$f(8, 9, r)$:
- Give to A: $c + f(9, 9, r-c) \approx c + (r-c)/2 = (r + c)/2$.
- Give to B: $f(8, 10, r-c) \approx 3(r-c)/4$.
Set equal: $(r + c)/2 = 3(r-c)/4$, $2(r+c) = 3(r-c)$, $2r + 2c = 3r - 3c$, $5c = r$, $c = r/5$.
$f(8, 9, r) \approx (r + r/5)/2 = (6r/5)/2 = 3r/5$.
Check: $3(r - r/5)/4 = 3 \cdot 4r/5 / 4 = 3r/5$ ✓.

$f(8, 8, r)$:
- Give to A: $c + f(9, 8, r-c) \approx c + 2(r-c)/5 = (5c + 2r - 2c)/5 = (2r + 3c)/5$.
- Give to B: $f(8, 9, r-c) \approx 3(r-c)/5$.
Set equal: $(2r + 3c)/5 = 3(r-c)/5$, $2r + 3c = 3r - 3c$, $6c = r$, $c = r/6$.
$f(8, 8, r) \approx (2r + 3 \cdot r/6)/5 = (2r + r/2)/5 = (5r/2)/5 = r/2$.
Check: $3(r - r/6)/5 = 3 \cdot 5r/6 / 5 = r/2$ ✓.

$f(8, 7, r)$:
- Give to A: $c + f(9, 7, r-c)$. Need $f(9, 7, r)$.
$f(9, 7, r) = 2r/(13-7) = 2r/6 = r/3$.
So give to A: $c + (r-c)/3 = (r + 2c)/3$.
- Give to B: $f(8, 8, r-c) \approx (r-c)/2$.
Set equal: $(r + 2c)/3 = (r-c)/2$, $2(r + 2c) = 3(r-c)$, $2r + 4c = 3r - 3c$, $7c = r$, $c = r/7$.
$f(8, 7, r) \approx (r + 2r/7)/3 = (9r/7)/3 = 3r/7$.
Check: $(r - r/7)/2 = (6r/7)/2 = 3r/7$ ✓.

Pattern for $f(8, b, r)$:
- $b=10$: $3r/4$
- $b=9$: $3r/5$
- $b=8$: $r/2 = 3r/6$
- $b=7$: $3r/7$

So $f(8, b, r) = 3r / (14 - b)$.

Check: $b=10$: $3r/4$ ✓. $b=9$: $3r/5$ ✓. $b=8$: $3r/6 = r/2$ ✓. $b=7$: $3r/7$ ✓.

Now I see the pattern:
- $f(10, b, r) = 1 \cdot r / (11 - b)$ → numerator 1, denominator offset 11
- $f(9, b, r) = 2 \cdot r / (13 - b)$ → numerator 2, denominator offset 13
- $f(8, b, r) = 3 \cdot r / (14 - b)$ → numerator 3, denominator offset 14

Wait, let me recheck the offsets:
- $f(10, b)$: denominator $= 11 - b$. When $b = 10$, denom $= 1$, but $f(10, 10) = r/2$. That's $r/2$, not $r/1$.

Hmm wait, $f(10, 10, r) = \lfloor r/2 \rfloor \approx r/2$. And $11 - 10 = 1$. $r/1 = r \neq r/2$.

I think I made an error. Let me recheck.

$f(10, 10, r) = \lfloor r/2 \rfloor \approx r/2$. Denominator should be 2, not 1.

$f(10, b, r)$:
- $b=10$: $r/2$
- $b=9$: $r/3$
- $b=8$: $r/4$

So $f(10, b, r) = r / (12 - b)$. Check: $b=10$: $r/2$ ✓. $b=9$: $r/3$ ✓. $b=8$: $r/4$ ✓.

$f(9, b, r)$:
- $b=10$: $2r/3$
- $b=9$: $r/2 = 2r/4$
- $b=8$: $2r/5$
- $b=7$: $r/3 = 2r/6$

So $f(9, b, r) = 2r / (13 - b)$. Check: $b=10$: $2r/3$ ✓. $b=9$: $2r/4$ ✓. $b=8$: $2r/5$ ✓. $b=7$: $2r/6$ ✓.

$f(8, b, r)$:
- $b=10$: $3r/4$
- $b=9$: $3r/5$
- $b=8$: $3r/6 = r/2$
- $b=7$: $3r/7$

So $f(8, b, r) = 3r / (14 - b)$. Check: $b=10$: $3r/4$ ✓. $b=9$: $3r/5$ ✓. $b=8$: $3r/6$ ✓. $b=7$: $3r/7$ ✓.

Now the pattern is clear:
- $f(a, b, r) = (11 - a) \cdot r / (11 - a + 11 - b)$

Let me verify:
- $f(10, b, r) = 1 \cdot r / (1 + 11 - b) = r / (12 - b)$ ✓
- $f(9, b, r) = 2 \cdot r / (2 + 11 - b) = 2r / (13 - b)$ ✓
- $f(8, b, r) = 3 \cdot r / (3 + 11 - b) = 3r / (14 - b)$ ✓

So the general formula is:
$$f(a, b, r) = \frac{(11 - a) \cdot r}{(11 - a) + (11 - b)} = \frac{(11 - a) \cdot r}{22 - a - b}$$

Let me verify this with one more case. Let me compute $f(7, 10, r)$.

$f(7, 10, r) = 4r / (4 + 1) = 4r/5$.

Let me verify by computation:
$f(7, 10, r)$: A puts $c$.
- Give to A: $c + f(8, 10, r-c) \approx c + 3(r-c)/4 = (4c + 3r - 3c)/4 = (3r + c)/4$.
- Give to B: B reaches 11, A gets $r - c$.
Set equal: $(3r + c)/4 = r - c$, $3r + c = 4r - 4c$, $5c = r$, $c = r/5$.
$f(7, 10, r) \approx (3r + r/5)/4 = (16r/5)/4 = 4r/5$ ✓.

Let me also verify $f(7, 9, r) = 4r / (4 + 2) = 4r/6 = 2r/3$.
- Give to A: $c + f(8, 9, r-c) \approx c + 3(r-c)/5 = (5c + 3r - 3c)/5 = (3r + 2c)/5$.
- Give to B: $f(7, 10, r-c) \approx 4(r-c)/5$.
Set equal: $(3r + 2c)/5 = 4(r-c)/5$, $3r + 2c = 4r - 4c$, $6c = r$, $c = r/6$.
$f(7, 9, r) \approx (3r + 2r/6)/5 = (3r + r/3)/5 = (10r/3)/5 = 2r/3$ ✓.

The formula is confirmed:
$$f(a, b, r) = \frac{(11 - a) \cdot r}{22 - a - b}$$

Now, the answer to the problem is:
$$f(0, 0, 300) = \frac{11 \cdot 300}{22} = \frac{3300}{22} = 150$$

So the first bandit can guarantee 150 coins.

Wait, but I need to be more careful. The formula assumes coins are always plentiful (game ends with someone reaching 11 bags, not coins running out). With 300 coins and at most 21 bags, each bag has at least 1 coin, so at most 21 coins are used, and 279 remain. The game always ends with someone reaching 11. But actually, A could choose to put all remaining coins in one bag, which would end the game early (coins run out). Let me check if this could be better for A.

Actually, in the DP, A chooses $c$ (the bag size) optimally, including the possibility of $c = r$ (all remaining coins). The formula I derived assumes the optimal $c$ is $r / (22 - a - b)$, which is less than $r$ as long as $22 - a - b > 1$, i.e., $a + b < 21$. Since the game starts with $a + b = 0$, and the formula gives $c = r/22$ at the start, this is fine.

But wait, I need to also check that the formula is exactly correct, not just approximately. The issue is the floor function from $f(10, 10, r) = \lfloor r/2 \rfloor$.

Let me think about whether the exact answer is 150 or could be slightly different due to rounding.

Actually, let me reconsider. The formula $f(a, b, r) = (11-a) \cdot r / (22 - a - b)$ assumes that A can choose $c$ to be any real number, but $c$ must be a positive integer. With $r = 300$ and the denominators being at most 22, the rounding effects should be small.

Let me trace through more carefully. At the start, $f(0, 0, 300) = 11 \cdot 300 / 22 = 150$.

The optimal first bag size is $c = 300 / 22 \approx 13.6$, so $c = 14$ or $c = 13$.

Let me check: if $c = 14$:
- Give to A: $14 + f(1, 0, 286) = 14 + 10 \cdot 286 / 21 = 14 + 2860/21 \approx 14 + 136.19 = 150.19$.
- Give to B: $f(0, 1, 286) = 11 \cdot 286 / 21 = 3146/21 \approx 149.81$.
B minimizes: $\min(150.19, 149.81) = 149.81$.

If $c = 13$:
- Give to A: $13 + f(1, 0, 287) = 13 + 10 \cdot 287 / 21 = 13 + 2870/21 \approx 13 + 136.67 = 149.67$.
- Give to B: $f(0, 1, 287) = 11 \cdot 287 / 21 = 3157/21 \approx 150.33$.
B minimizes: $\min(149.67, 150.33) = 149.67$.

If $c = 14$: A gets $\approx 149.81$.
If $c = 13$: A gets $\approx 149.67$.

So $c = 14$ is better. But the exact value depends on the integer constraints throughout the game.

Hmm, but the formula gives 150 exactly. The question is whether the integer constraints reduce this.

Let me think about this differently. The formula $f(a, b, r) = (11-a) r / (22 - a - b)$ is exact when $r$ is divisible by $(22 - a - b)$ and the optimal $c = r / (22 - a - b)$ is an integer. 

At the start, $r = 300$, $22 - 0 - 0 = 22$, $300 / 22$ is not an integer. So the exact answer might differ from 150.

Let me think about this more carefully. The key insight is that the formula gives the continuous relaxation, and the integer version might be slightly less.

Actually, let me reconsider the problem. The formula says A can guarantee approximately 150. The question asks for the maximum number of coins A can guarantee. This should be an integer.

Let me think about whether A can guarantee exactly 150 or slightly less.

Actually, I think the answer is 150. Let me think about why.

Consider the continuous version: A can guarantee exactly $11 \cdot 300 / 22 = 150$. In the discrete version, A might guarantee slightly less, but the problem likely has a clean answer.

Hmm, but actually let me reconsider whether the formula is exactly right or just approximately right. Let me re-derive more carefully.

The recurrence is:
$$f(a, b, r) = \max_{1 \le c \le r} \min\left(\text{give to A}, \text{give to B}\right)$$

where:
- give to A = $c + f(a+1, b, r-c)$ if $a+1 < 11$, else $c$
- give to B = $r - c$ if $b+1 = 11$, else $f(a, b+1, r-c)$

In the continuous version (where $c$ can be any real in $(0, r]$), the formula $f(a,b,r) = (11-a)r/(22-a-b)$ is exact.

In the discrete version, we need $c$ to be a positive integer. The question is whether the rounding losses accumulate.

Let me think about it from a different angle. Let me consider the total number of bags given to A and B.

If the game ends with A receiving $p$ bags and B receiving $q$ bags, where either $p = 11$ or $q = 11$, and the remaining coins go to the person who didn't reach 11.

A's total = (coins in A's bags) + (remaining coins if B reached 11).
B's total = (coins in B's bags) + (remaining coins if A reached 11).

A controls bag sizes, B controls allocation. 

In the continuous analysis, the equilibrium is that A gets fraction $(11-a)/(22-a-b)$ of the remaining coins at each state. At the start, A gets $11/22 = 1/2$ of all coins = 150.

The key question: can A guarantee 150 exactly, or is it 149 due to integer constraints?

Let me think about a strategy for A that guarantees 150.

A's strategy: At each step, put $c = \lceil r / (22 - a - b) \rceil$ coins in the bag (or some appropriate integer choice).

Actually, let me think about this problem differently. 

The formula suggests the answer is 150. Let me verify this is achievable and that B can't do better (i.e., B can prevent A from getting more than 150).

Upper bound (B can prevent A from getting more than 150): B's strategy is to always give the bag to the person who minimizes A's expected gain. By the analysis, B can ensure A gets at most 150.

Lower bound (A can guarantee 150): A's strategy is to choose bag sizes that create equal dilemmas for B. 

But with integer constraints, can A guarantee exactly 150?

Let me think about a simpler approach. Consider A's strategy: always put exactly 1 coin in each bag. Then B allocates 21 bags (someone reaches 11). A gets some number of 1-coin bags, and the remainder (279 coins) goes to whoever didn't reach 11.

If B gives all bags to A: A gets 11 bags (11 coins), B gets 279 coins. A gets 11. Bad.
If B gives all bags to B: B gets 11 bags (11 coins), A gets 279 coins. A gets 279. But B won't do this.

B will balance: give just enough bags to A to reach 11 first, while keeping the valuable bags. With 1-coin bags, B gives 11 bags to A (A gets 11 coins, B gets 279). Or B takes 11 bags (B gets 11, A gets 279). B prefers the former. So A gets 11. Terrible.

So A needs to use larger bags to create dilemmas.

Let me think about the problem from the perspective of the continuous solution. At each state $(a, b, r)$, A puts $c^* = r / (22 - a - b)$ coins. B is indifferent between giving to A and giving to B.

In the discrete case, A puts $\lfloor c^* \rfloor$ or $\lceil c^* \rceil$ coins. The rounding error is at most 1 coin per step, and there are at most 21 steps. So the total error is at most 21 coins. But the errors might not all go against A.

Actually, I think the answer is 150. Let me think about why more carefully.

Consider the following strategy for A: at each state $(a, b, r)$, A puts $c = \lfloor r / (22 - a - b) \rfloor$ or $c = \lceil r / (22 - a - b) \rceil$ coins, choosing whichever gives a better guarantee.

The continuous value is $V = (11-a) r / (22 - a - b)$. With integer $c$, the discrete value is at least $V - 1$ (roughly), because the rounding error is at most 1 per step.

But actually, the errors compound. Let me think about this differently.

Hmm, let me try to think about whether the answer is exactly 150.

Actually, I think the key insight is that 300 is divisible by 22? No, $300 / 22 = 13.63...$. Not divisible.

But $300 = 22 \times 13 + 14$. Hmm.

Let me try a different approach. Let me think about what happens if A uses the strategy of always making the bag size such that B is exactly indifferent.

At state $(0, 0, 300)$: optimal $c = 300/22 \approx 13.6$. A chooses $c = 14$.
- If B gives to A: A gets 14, state becomes $(1, 0, 286)$. Continuous value: $10 \times 286 / 21 = 2860/21 \approx 136.19$. Total: $14 + 136.19 = 150.19$.
- If B gives to B: state becomes $(0, 1, 286)$. Continuous value: $11 \times 286 / 21 = 3146/21 \approx 149.81$.
B gives to B (A gets 149.81).

State $(0, 1, 286)$: optimal $c = 286/21 \approx 13.6$. A chooses $c = 14$.
- Give to A: $14 + 10 \times 272 / 20 = 14 + 136 = 150$.
- Give to B: $11 \times 272 / 20 = 11 \times 13.6 = 149.6$.
B gives to B (A gets 149.6).

Hmm, this is getting complicated. The continuous approximation gives 150 but the discrete version might give slightly less.

Let me try to think about this problem from a higher level. 

Actually, maybe I should think about it differently. Let me consider the problem where A pre-commits to all bag sizes (instead of adapting). This is a weaker strategy for A but might be easier to analyze.

If A pre-commits to bag sizes $c_1, c_2, \ldots, c_n$ (where $n \le 21$ and $\sum c_i \le 300$), then B allocates each bag to minimize A's total. B will give bags to A or B strategically.

Actually, the adaptive version is stronger for A. Let me think about the adaptive version.

Let me try to think about whether 150 is exactly achievable.

Consider the following: A's strategy is to always put $c$ coins where $c$ is chosen so that both options for B give A at least 150 total (including what A already has).

At the start, A has 0 coins, 0 bags. A needs to guarantee 150 more coins from 300 remaining.

A puts $c$ coins. 
- If B gives to A: A has $c$ coins, 1 bag, $300 - c$ remaining. A needs $150 - c$ more from $f(1, 0, 300-c)$.
- If B gives to B: A has 0 coins, 0 bags, $300 - c$ remaining. A needs 150 more from $f(0, 1, 300-c)$.

For A to guarantee 150: need $c + f(1, 0, 300-c) \ge 150$ AND $f(0, 1, 300-c) \ge 150$.

From the formula: $f(1, 0, r) = 10r/21$ and $f(0, 1, r) = 11r/21$.

$c + 10(300-c)/21 \ge 150 \Rightarrow 21c + 10(300-c) \ge 3150 \Rightarrow 21c + 3000 - 10c \ge 3150 \Rightarrow 11c \ge 150 \Rightarrow c \ge 150/11 \approx 13.6$.

$11(300-c)/21 \ge 150 \Rightarrow 11(300-c) \ge 3150 \Rightarrow 3300 - 11c \ge 3150 \Rightarrow 11c \le 150 \Rightarrow c \le 150/11 \approx 13.6$.

So $c = 150/11$, which is not an integer. $c = 14$ gives:
- $14 + 10 \times 286/21 = 14 + 2860/21 = 14 + 136.19 = 150.19 \ge 150$ ✓
- $11 \times 286/21 = 3146/21 = 149.81 < 150$ ✗

$c = 13$ gives:
- $13 + 10 \times 287/21 = 13 + 2870/21 = 13 + 136.67 = 149.67 < 150$ ✗

So with $c = 14$, the "give to B" branch gives 149.81 < 150. With $c = 13$, the "give to A" branch gives 149.67 < 150.

So A cannot guarantee 150 in the continuous relaxation either! Wait, but the formula says $f(0, 0, 300) = 150$. Let me recheck.

$f(0, 0, 300) = \max_c \min(c + f(1, 0, 300-c), f(0, 1, 300-c))$
$= \max_c \min(c + 10(300-c)/21, 11(300-c)/21)$

Setting equal: $c + 10(300-c)/21 = 11(300-c)/21$
$c = (300-c)/21$
$21c = 300 - c$
$22c = 300$
$c = 300/22 = 150/11$

Value: $11(300 - 150/11)/21 = 11 \cdot (3300 - 150)/(11 \cdot 21) = (3300 - 150)/21 = 3150/21 = 150$.

So the continuous value is exactly 150, achieved at $c = 150/11 \approx 13.636$.

But $c$ must be an integer. With $c = 14$: $\min(14 + 2860/21, 3146/21) = \min(150.19, 149.81) = 149.81$.
With $c = 13$: $\min(13 + 2870/21, 3157/21) = \min(149.67, 150.33) = 149.67$.

So the best is $c = 14$, giving $149.81$ in the continuous relaxation of the sub-problems. But the sub-problems also have integer constraints, so the actual value might be different.

This is getting very complex. Let me think about whether the answer is 150 or 149.

Actually, I realize the continuous formula gives a value of exactly 150, but the integer constraints might reduce it. The question is by how much.

Let me think about this more carefully. The formula $f(a, b, r) = (11-a)r/(22-a-b)$ is the continuous relaxation. The discrete version satisfies $f_{\text{disc}}(a, b, r) \le f_{\text{cont}}(a, b, r)$.

But also, $f_{\text{disc}}(a, b, r) \ge f_{\text{cont}}(a, b, r) - \epsilon$ for some small $\epsilon$ depending on the number of remaining steps.

The number of steps from $(0, 0)$ is at most 21. At each step, the rounding error is at most 1 (since we're rounding $c$ to the nearest integer). But the errors propagate.

Actually, let me think about this differently. Let me try to compute the exact discrete value for small cases and see if there's a pattern.

Let me compute $f(10, 10, r)$ exactly for small $r$:
$f(10, 10, r) = \max_c \min(c, r-c) = \lfloor r/2 \rfloor$.

$f(10, 9, r) = \max_c \min(c, \lfloor (r-c)/2 \rfloor)$.

For $r = 3$: $c=1: \min(1, 1) = 1$. $c=2: \min(2, 0) = 0$. So $f(10, 9, 3) = 1$. Continuous: $3/3 = 1$. ✓

For $r = 6$: $c=1: \min(1, 2) = 1$. $c=2: \min(2, 2) = 2$. $c=3: \min(3, 1) = 1$. So $f(10, 9, 6) = 2$. Continuous: $6/3 = 2$. ✓

For $r = 7$: $c=1: \min(1, 3) = 1$. $c=2: \min(2, 2) = 2$. $c=3: \min(3, 2) = 2$. So $f(10, 9, 7) = 2$. Continuous: $7/3 = 2.33$. So discrete is 2, continuous is 2.33. Loss of 0.33.

For $r = 300$ and 22 steps, the loss could accumulate. But let me think about whether the answer is 150 or something else.

Actually, let me reconsider. Maybe I should think about this problem differently.

Let me think about the problem as follows. The game has at most 21 rounds. In each round, A chooses a bag size, B allocates. The game ends when someone has 11 bags.

Let me think about the total coins A gets. A gets coins from bags assigned to A, plus any remaining coins if B reaches 11 first.

Key insight: the formula $f(a,b,r) = (11-a)r/(22-a-b)$ can be rewritten as:
$$f(a,b,r) = \frac{11-a}{(11-a)+(11-b)} \cdot r$$

This means A gets a fraction $\frac{11-a}{(11-a)+(11-b)}$ of the remaining coins. At the start, this is $11/22 = 1/2$.

The fraction represents A's "bargaining power" based on how many more bags each can receive before reaching 11.

Now, the question is whether the integer constraints change the answer from 150.

Let me think about it from a different angle. Consider the following strategy for A:

A divides the 300 coins into 22 groups as evenly as possible: 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14 — wait, $22 \times 14 = 308 > 300$. So $300 = 22 \times 13 + 14$, meaning 14 groups of 14 and 8 groups of 13. Or more precisely, 14 groups of 14 and 8 groups of 13: $14 \times 14 + 8 \times 13 = 196 + 104 = 300$. Yes.

But A doesn't pre-commit to all bags; A adapts. Let me think about whether A can guarantee 150.

Actually, let me think about the problem from B's perspective. B wants to minimize A's coins. B's optimal strategy in the continuous case is to always be indifferent. In the discrete case, B might be able to exploit rounding.

Let me try to think about upper and lower bounds.

Upper bound: A can get at most 150 (from continuous analysis, B can prevent more).
Lower bound: A can guarantee at least...?

For the lower bound, let me think about A's strategy. 

A's strategy: At each state $(a, b, r)$, A puts $c = \lceil r / (22 - a - b) \rceil$ coins in the bag (rounding up to ensure the "give to A" branch is strong enough).

Let me trace through the game with this strategy and see what A can guarantee.

Actually, this is getting very complex. Let me try a different approach.

Let me think about the problem as a "cutting" game. A is essentially cutting the pie (300 coins) into pieces, and B chooses who gets each piece. The constraint is the 11-bag limit.

This is similar to the "I cut, you choose" game but with multiple rounds and a stopping condition.

In the classic "I cut, you choose" with one round, A cuts the pie in half and gets 50%. With multiple rounds and the 11-bag constraint, the analysis is more complex.

Let me think about a cleaner approach. 

Claim: The answer is 150.

Proof sketch:
1. A can guarantee at least 150 by using a strategy that maintains the invariant that A's guaranteed share is at least half the remaining coins.
2. B can prevent A from getting more than 150 by using a symmetric strategy.

For part 1: A's strategy is to always put $c$ coins where $c$ is chosen so that both options for B give A at least half the remaining coins (accounting for what A already has and the bag count dynamics).

Hmm, but the continuous analysis shows that the exact optimal $c = 150/11$ is not an integer, so A can't perfectly balance.

Let me think about this more carefully.

Actually, let me reconsider. The formula gives $f(0,0,300) = 150$ in the continuous case. In the discrete case, the value is $\lfloor 150 \rfloor = 150$ if the rounding works out, or 149 if it doesn't.

Let me try to compute the exact discrete value by working backwards from the end, but only tracking the "loss" from the continuous value.

Define $g(a, b, r) = f_{\text{disc}}(a, b, r) - f_{\text{cont}}(a, b, r) \le 0$. This is the loss from integer constraints.

At the base case, $g(a, b, 0) = 0$.

The recurrence for $f_{\text{disc}}$ involves choosing integer $c$, while $f_{\text{cont}}$ uses real $c^*$. The loss at each step depends on how far $c$ is from $c^*$ and how the loss propagates.

This is hard to analyze in general. Let me try a different approach.

Let me think about the problem from the perspective of the answer being a nice number. The continuous answer is 150. The problem likely has answer 150.

Let me try to construct an explicit strategy for A that guarantees 150, and a strategy for B that prevents A from getting more than 150.

B's strategy (upper bound): B always gives the bag to the person who results in A getting fewer coins. By the continuous analysis, this limits A to 150. But with integer constraints, B might be able to limit A to 149.

Hmm, let me think about this differently.

Actually, let me reconsider the problem. Maybe the answer isn't 150. Let me re-examine the formula.

The formula $f(a, b, r) = (11-a)r/(22-a-b)$ assumes the game always ends with someone reaching 11 bags. But what if A can end the game early by putting all remaining coins in one bag?

If A puts all $r$ coins in one bag, the game gives out 1 bag and 0 coins remain. The game ends with all coins distributed. A gets either $r$ (if B gives to A) or 0 (if B gives to B). B will give to B, so A gets 0. So putting all coins in one bag is terrible for A.

What if A puts $r-1$ coins in one bag? Then 1 coin remains. B gives the big bag to B, and then A puts 1 coin in a bag, B gives it to A or B. This is also bad for A.

So A wants to spread coins across many bags. The 11-bag limit is the binding constraint.

OK let me try to think about this more carefully with the exact DP, but using the structure of the formula.

The formula says $f(a, b, r) = (11-a)r/(22-a-b)$, and the optimal $c = r/(22-a-b)$.

At each step, the remaining coins $r$ is divided by $(22-a-b)$, which decreases by 1 each step. So after $k$ steps, the denominator is $22-k$.

The optimal $c$ at step $k$ (0-indexed) is $r_k / (22-k)$ where $r_k$ is the remaining coins.

$r_0 = 300$, $c_0 = 300/22 \approx 13.6$.
$r_1 = 300 - c_0 \approx 286.4$, $c_1 = 286.4/21 \approx 13.6$.
...

In the continuous case, $r_k = 300 \cdot (22-k-1)/(22-1) \cdot ... $ hmm, this isn't quite right because $r$ depends on which branch B takes.

Actually, in the continuous case, B is indifferent at each step, so the value is the same regardless of B's choice. The remaining coins after step $k$ is $r_k = r_{k-1} - c_{k-1} = r_{k-1} - r_{k-1}/(22-k+1) = r_{k-1} \cdot (21-k)/(22-k)$.

So $r_k = 300 \cdot \prod_{j=0}^{k-1} (21-j)/(22-j) = 300 \cdot \prod_{j=0}^{k-1} (22-j-1)/(22-j) = 300 \cdot (22-k-1)! \cdot 21! / (21! \cdot (22-1)!) $... 

Hmm, let me just compute: $r_k = 300 \cdot \frac{21}{22} \cdot \frac{20}{21} \cdot \frac{19}{20} \cdots \frac{22-k-1}{22-k} = 300 \cdot \frac{22-k-1}{22} = 300 \cdot \frac{21-k}{22}$.

So $r_k = 300(21-k)/22$ and $c_k = r_k/(22-k) = 300(21-k)/(22(22-k))$.

At $k=0$: $c_0 = 300 \cdot 21 / (22 \cdot 22) = 6300/484 = 13.02$. Wait, that doesn't match. Let me recompute.

$c_0 = r_0 / (22 - 0) = 300/22 \approx 13.636$.
$r_1 = r_0 - c_0 = 300 - 300/22 = 300 \cdot 21/22 \approx 286.36$.
$c_1 = r_1 / (22 - 1) = 300 \cdot 21/(22 \cdot 21) = 300/22 \approx 13.636$.

Oh interesting, $c_k = 300/22$ for all $k$! Because $c_k = r_k / (22-k) = [300(21-k)/22] / (22-k) = 300(21-k) / [22(22-k)]$.

Hmm, that's not $300/22$. Let me recompute.

$r_0 = 300$, $c_0 = 300/22$.
$r_1 = 300 - 300/22 = 300 \cdot 21/22$.
$c_1 = r_1/21 = 300 \cdot 21/(22 \cdot 21) = 300/22$.
$r_2 = r_1 - c_1 = 300 \cdot 21/22 - 300/22 = 300 \cdot 20/22$.
$c_2 = r_2/20 = 300 \cdot 20/(22 \cdot 20) = 300/22$.

Yes! $c_k = 300/22$ for all $k$. The optimal bag size is constant at $300/22 \approx 13.636$.

This makes sense: in the continuous equilibrium, A puts the same number of coins in each bag, and the game lasts 21 rounds (someone reaches 11 bags), with each bag having $300/22$ coins (wait, 21 bags, but $300/22 \cdot 21 = 6300/22 = 286.36$, not 300. The remaining $300 - 286.36 = 13.64 = 300/22$ goes to the person who didn't reach 11).

Actually, 21 bags are given out, each with $300/22$ coins, totaling $21 \cdot 300/22 = 6300/22 \approx 286.36$. The remaining $300 - 286.36 = 13.64 = 300/22$ coins go to the person who didn't reach 11 bags.

A gets 11 bags (if A reaches 11 first): $11 \cdot 300/22 = 150$. B gets 10 bags + remainder: $10 \cdot 300/22 + 300/22 = 11 \cdot 300/22 = 150$. So both get 150.

Or B gets 11 bags: B gets $11 \cdot 300/22 = 150$, A gets 10 bags + remainder = 150.

So in the continuous equilibrium, both get 150 regardless of who reaches 11 first. That's the beauty of the constant bag size.

Now, in the discrete case, A wants to put $300/22 \approx 13.636$ coins per bag. Since this must be an integer, A puts either 13 or 14 coins per bag.

If A always puts 14 coins: 21 bags use $21 \times 14 = 294$ coins, 6 remain. 
- If A reaches 11 first: A gets $11 \times 14 = 154$, B gets $10 \times 14 + 6 = 146$.
- If B reaches 11 first: B gets $11 \times 14 = 154$, A gets $10 \times 14 + 6 = 146$.
B will try to make A reach 11 first (so B gets 146 instead of 154). Wait, B wants to maximize B's coins. If A reaches 11 first, B gets 146. If B reaches 11 first, B gets 154. So B prefers B reaching 11 first. But B also controls allocation...

Wait, I need to think about this more carefully. If A always puts 14 coins per bag, B allocates each bag. B wants to maximize B's total.

If B gives all bags to A: A gets 11 bags (154 coins), B gets 6 remaining. B total = 6.
If B gives all bags to B: B gets 11 bags (154 coins), A gets 6 remaining. B total = 154.
If B gives 10 to A, 11 to B: B gets 11 bags (154), A gets 10 bags (140) + 6 = 146. B total = 154.
If B gives 11 to A, 10 to B: A gets 11 bags (154), B gets 10 bags (140) + 6 = 146. B total = 146.

So B's best is to take 11 bags (give 10 to A), getting 154. A gets 146.

But wait, B doesn't have to give exactly 10 to A and 11 to B. B can adapt. The key is: B wants to reach 11 bags for B before A reaches 11. Since B controls allocation, B can always ensure B gets 11 bags before A (by taking bags). But then A gets the remainder.

Hmm, but if B takes all bags, B reaches 11 first, A gets the remainder (6). A gets 6. That's terrible for A.

Wait, no. If B takes all 21 bags... but the game ends when someone reaches 11. So after B takes 11 bags, the game ends, A gets the remainder. B has 11 bags with $11 \times 14 = 154$ coins, A gets $300 - 154 = 146$ coins.

But B could also give some bags to A. If B gives $k$ bags to A and takes $11-k$ bags (B reaches 11 first since B takes the 11th bag), then:
- A has $k$ bags with $14k$ coins, plus remainder $300 - 14 \cdot 11 = 300 - 154 = 146$.
- A total = $14k + 146$.
- B has 11 bags with $154$ coins.
- B total = 154.

Wait, that's not right either. If B gives $k$ bags to A and takes $11$ bags (B reaches 11), then $k + 11$ bags are given out, using $14(k+11)$ coins. But $k + 11 \le 21$ (since A can have at most 10 bags before the game ends). So $k \le 10$.

Remainder = $300 - 14(k + 11) = 300 - 14k - 154 = 146 - 14k$.
A total = $14k + (146 - 14k) = 146$.
B total = $154$.

Interesting! Regardless of how B allocates (as long as B reaches 11 first), A gets 146 and B gets 154.

But what if A reaches 11 first? B gives 11 bags to A and takes $k$ bags ($k \le 10$). Then:
- A has 11 bags with $154$ coins. Game ends, B gets remainder.
- Remainder = $300 - 14(11 + k) = 146 - 14k$.
- B total = $14k + 146 - 14k = 146$.
- A total = 154.

So if A reaches 11 first, A gets 154 and B gets 146.
If B reaches 11 first, A gets 146 and B gets 154.

B wants to maximize B's total, so B prefers B reaching 11 first (154 vs 146). B can ensure B reaches 11 first by taking bags (B controls allocation). So B takes 11 bags, A gets 146.

So with constant bag size 14, A gets 146. That's less than 150.

What if A always puts 13 coins per bag? 21 bags use $21 \times 13 = 273$ coins, 27 remain.
- If B reaches 11 first: B gets $11 \times 13 = 143$, A gets $10 \times 13 + 27 = 157$.
- If A reaches 11 first: A gets $11 \times 13 = 143$, B gets $10 \times 13 + 27 = 157$.

B wants to maximize B's total. If B reaches 11 first, B gets 143. If A reaches 11 first, B gets 157. So B prefers A reaching 11 first! B gives all bags to A.

If B gives all bags to A: A reaches 11 first, A gets 143, B gets 157. A gets 143.

So with constant bag size 13, A gets 143. Worse than 146.

What if A mixes bag sizes? A can adapt bag sizes based on the current state.

The key insight: with constant bag size $c$, if $21c < 300$ (remainder $> 0$):
- If B reaches 11 first: A gets $10c + (300 - 21c) = 300 - 11c$, B gets $11c$.
- If A reaches 11 first: A gets $11c$, B gets $10c + (300 - 21c) = 300 - 11c$.
B chooses the option where B gets more: B prefers B reaching 11 first if $11c > 300 - 11c$, i.e., $22c > 300$, i.e., $c > 300/22 \approx 13.6$. B prefers A reaching 11 first if $c < 300/22$.

If $c > 300/22$: B takes 11 bags, A gets $300 - 11c$.
If $c < 300/22$: B gives 11 bags to A, A gets $11c$.
If $c = 300/22$: both options give A $150$.

With $c = 14 > 300/22$: A gets $300 - 154 = 146$.
With $c = 13 < 300/22$: A gets $11 \times 13 = 143$.

So constant bag size gives at most 146. But A can do better by adapting!

The continuous optimal strategy has A putting $300/22$ coins per bag, which is between 13 and 14. A can mix: some bags with 13, some with 14, to effectively get $300/22$ per bag.

If A uses 14 bags of 14 coins and 7 bags of 13 coins: total = $14 \times 14 + 7 \times 13 = 196 + 91 = 287$. Remainder = 13. Total bags = 21.

But A needs to be strategic about which bags are 13 and which are 14, and B adapts too.

Actually, A doesn't pre-commit. A adapts based on the current state. Let me think about the adaptive strategy.

The continuous optimal is $c^* = r/(22-a-b)$ at each state. A should put $\lfloor c^* \rfloor$ or $\lceil c^* \rceil$ coins, choosing to balance the two branches.

Let me think about this more carefully. At state $(a, b, r)$, the continuous optimal is $c^* = r/(22-a-b)$. A puts $c = \lfloor c^* \rfloor$ or $c = \lceil c^* \rceil$.

The continuous value is $V = (11-a)r/(22-a-b)$.

With $c = \lfloor c^* \rfloor$: 
- Give to A: $\lfloor c^* \rfloor + V(a+1, b, r - \lfloor c^* \rfloor)$
- Give to B: $V(a, b+1, r - \lfloor c^* \rfloor)$

With $c = \lceil c^* \rceil$:
- Give to A: $\lceil c^* \rceil + V(a+1, b, r - \lceil c^* \rceil)$
- Give to B: $V(a, b+1, r - \lceil c^* \rceil)$

A chooses the $c$ that maximizes the minimum.

The loss from integer constraints is at most 1 per step (the difference between $c^*$ and the nearest integer). Over 21 steps, the total loss is at most 21. But the losses might partially cancel.

Actually, I think the answer might be 150. Let me think about why.

Consider A's strategy: A maintains a "target" for each bag. At state $(a, b, r)$, the target is $r/(22-a-b)$. A puts $\lfloor r/(22-a-b) \rfloor$ or $\lceil r/(22-a-b) \rceil$ coins, choosing to maximize the minimum of the two branches.

The key observation is that the continuous value $V = (11-a)r/(22-a-b)$ is always a rational number with denominator dividing $22-a-b$. If $r$ is divisible by $22-a-b$, then $c^*$ is an integer and there's no loss. If not, the loss is at most 1 per step.

But the losses compound. Let me think about whether the total loss can be 0.

Actually, let me think about this problem from a completely different angle.

Consider the following strategy for A: A puts coins in bags such that the total coins in any 11 bags assigned to one person is at most 150, and the total coins in any 10 bags plus the remainder is at least 150.

Hmm, this is vague. Let me think more concretely.

Let me consider the problem as a whole. A wants to guarantee 150. B wants to prevent this.

A's strategy: Divide 300 coins into 22 "shares" of $300/22$ each (in some discrete approximation). Each bag corresponds to one share. The 22nd share is the remainder. A puts coins in bags one at a time, each bag being one share. B allocates. After 21 bags (11 to one person), the 22nd share goes to the other person.

If A can ensure each share is exactly $300/22$, then regardless of allocation, A gets 11 shares = 150. But $300/22$ is not an integer.

So A needs to use integer shares. The question is whether A can arrange integer shares such that any 11 of them sum to at least 150.

If A uses 14 shares of 14 and 8 shares of 13: $14 \times 14 + 8 \times 13 = 196 + 104 = 300$. Total 22 shares.

The worst case for A is B gives A the 11 smallest shares. The 11 smallest are all 13s (8 of them) and 3 of the 14s: $8 \times 13 + 3 \times 14 = 104 + 42 = 146$. So A gets 146 in the worst case.

But A doesn't have to pre-commit to all shares. A can adapt!

The key difference between adaptive and non-adaptive: A can observe B's allocations and adjust bag sizes accordingly.

Let me think about the adaptive strategy more carefully.

At state $(a, b, r)$, A wants to guarantee $V = (11-a)r/(22-a-b)$ more coins. A puts $c$ coins. The two branches give:
- Give to A: $c + V(a+1, b, r-c) = c + (10-a)(r-c)/(21-a-b)$... wait, let me use the formula. $V(a+1, b, r-c) = (11-a-1)(r-c)/(22-a-1-b) = (10-a)(r-c)/(21-a-b)$.
- Give to B: $V(a, b+1, r-c) = (11-a)(r-c)/(22-a-b-1) = (11-a)(r-c)/(21-a-b)$.

Setting equal: $c + (10-a)(r-c)/(21-a-b) = (11-a)(r-c)/(21-a-b)$.
$c = (r-c)/(21-a-b)$.
$c(21-a-b) = r - c$.
$c(22-a-b) = r$.
$c = r/(22-a-b)$.

So the continuous optimal is $c = r/(22-a-b)$, and the value is $V = (11-a)r/(22-a-b)$.

Now, in the discrete case, A chooses $c = \lfloor r/(22-a-b) \rfloor$ or $\lceil r/(22-a-b) \rceil$.

Let me define $d = 22 - a - b$ (the "denominator"). Then $c^* = r/d$ and $V = (11-a)r/d$.

Let $r = qd + s$ where $0 \le s < d$. Then $c^* = q + s/d$.

Option 1: $c = q$ (floor).
- Give to A: $q + (10-a)(r-q)/(d-1) = q + (10-a)(qd+s-q)/(d-1) = q + (10-a)(q(d-1)+s)/(d-1) = q + (10-a)q + (10-a)s/(d-1) = q(11-a) + (10-a)s/(d-1)$.
- Give to B: $(11-a)(r-q)/(d-1) = (11-a)(q(d-1)+s)/(d-1) = (11-a)q + (11-a)s/(d-1)$.
B minimizes: $\min(q(11-a) + (10-a)s/(d-1), (11-a)q + (11-a)s/(d-1))$.
$= (11-a)q + \min((10-a)s/(d-1), (11-a)s/(d-1))$
$= (11-a)q + (10-a)s/(d-1)$ (since $10-a < 11-a$).

Option 2: $c = q+1$ (ceil).
- Give to A: $(q+1) + (10-a)(r-q-1)/(d-1) = (q+1) + (10-a)(qd+s-q-1)/(d-1) = (q+1) + (10-a)(q(d-1)+s-1)/(d-1) = (q+1) + (10-a)q + (10-a)(s-1)/(d-1) = (11-a)q + 1 + (10-a)(s-1)/(d-1)$.
- Give to B: $(11-a)(r-q-1)/(d-1) = (11-a)(q(d-1)+s-1)/(d-1) = (11-a)q + (11-a)(s-1)/(d-1)$.
B minimizes: $(11-a)q + \min(1 + (10-a)(s-1)/(d-1), (11-a)(s-1)/(d-1))$.

If $s = 0$: $c^* = q$ is an integer. No loss. Value = $(11-a)q = (11-a)r/d = V$. ✓

If $s > 0$:
Option 1 value: $(11-a)q + (10-a)s/(d-1)$.
Option 2 value: $(11-a)q + \min(1 + (10-a)(s-1)/(d-1), (11-a)(s-1)/(d-1))$.

Continuous value: $V = (11-a)r/d = (11-a)(qd+s)/d = (11-a)q + (11-a)s/d$.

Loss from option 1: $V - \text{option 1} = (11-a)s/d - (10-a)s/(d-1) = s[(11-a)(d-1) - (10-a)d]/[d(d-1)]$.
$= s[(11-a)(d-1) - (10-a)d] / [d(d-1)]$
$= s[(11-a)d - (11-a) - (10-a)d] / [d(d-1)]$
$= s[d - (11-a)] / [d(d-1)]$
$= s[d - 11 + a] / [d(d-1)]$
$= s[(22-a-b) - 11 + a] / [d(d-1)]$
$= s[11 - b] / [d(d-1)]$.

So loss from option 1 = $s(11-b)/[d(d-1)]$.

For option 2, let me compute. We need to compare $1 + (10-a)(s-1)/(d-1)$ and $(11-a)(s-1)/(d-1)$.

$1 + (10-a)(s-1)/(d-1) - (11-a)(s-1)/(d-1) = 1 - (s-1)/(d-1) = (d-1-s+1)/(d-1) = (d-s)/(d-1)$.

Since $s < d$, $d - s > 0$, so $1 + (10-a)(s-1)/(d-1) > (11-a)(s-1)/(d-1)$.

So B chooses the "give to B" branch: option 2 value = $(11-a)q + (11-a)(s-1)/(d-1)$.

Loss from option 2: $V - \text{option 2} = (11-a)s/d - (11-a)(s-1)/(d-1) = (11-a)[s/d - (s-1)/(d-1)] = (11-a)[s(d-1) - d(s-1)]/[d(d-1)] = (11-a)[sd - s - ds + d]/[d(d-1)] = (11-a)(d-s)/[d(d-1)]$.

So:
- Loss from option 1 (floor): $s(11-b)/[d(d-1)]$
- Loss from option 2 (ceil): $(11-a)(d-s)/[d(d-1)]$

A chooses the option with smaller loss:
$\min(s(11-b), (11-a)(d-s)) / [d(d-1)]$.

The total loss over the entire game is the sum of these losses at each step. But the losses at later steps depend on the state, which depends on B's choices.

This is getting very involved. Let me try to compute the total loss for the specific case $r = 300$, starting from $(0, 0)$.

At the start: $a=0, b=0, d=22, r=300$. $q = 13, s = 300 - 13 \times 22 = 300 - 286 = 14$.
- Loss from floor: $14 \times 11 / (22 \times 21) = 154 / 462 = 7/21 = 1/3$.
- Loss from ceil: $11 \times (22-14) / (22 \times 21) = 11 \times 8 / 462 = 88/462 = 4/21$.
A chooses floor (loss 1/3 < 4/21). So A puts $c = 13$.

But wait, the loss is $1/3$, which means the discrete value is $150 - 1/3 = 149.67$. That's not an integer, and the actual discrete value is an integer.

Hmm, I think the issue is that the losses at subsequent steps also involve fractional values, and the total might work out to an integer.

This is getting extremely complex. Let me try a different approach: just compute the DP numerically.

Actually, I can't run code. Let me think about this problem from a higher level.

The continuous value is 150. The discrete value is at most 150. The question is whether it's 150 or less.

Key insight: the problem asks for the maximum number of coins A can guarantee. This is a specific integer. The continuous analysis gives 150. The discrete analysis might give 150 or 149.

Let me think about whether A can guarantee 150.

A's strategy to guarantee 150: A needs to ensure that regardless of B's choices, A gets at least 150.

Consider the following strategy for A: A always puts $c$ coins where $c$ is chosen to maintain the invariant that A's guaranteed coins from this point is at least $\lfloor (11-a)r/(22-a-b) \rfloor$.

Hmm, this is circular. Let me think differently.

Let me consider a specific strategy for A and check if it guarantees 150.

Strategy: A divides the game into 22 "rounds" (21 bags + 1 remainder). A wants each round to be worth $300/22 \approx 13.636$ coins. A uses a mix of 13 and 14 coin bags.

Specifically, A needs 14 bags of 14 coins and 8 bags of 13 coins (total $196 + 104 = 300$). But the order matters, and A adapts.

The question is: can A arrange the bags (adaptively) so that regardless of B's allocation, A gets at least 150?

If A gets 11 bags: A's coins = sum of A's 11 bags. A wants this to be $\ge 150$.
If B gets 11 bags: A's coins = sum of A's 10 bags + remainder. A wants this to be $\ge 150$.

In the first case (A gets 11 bags), B chooses which 11 bags A gets (by allocating). B will give A the 11 smallest bags. So A needs the 11th smallest bag to be large enough that the sum of the 11 smallest is $\ge 150$.

With 14 bags of 14 and 8 bags of 13: the 11 smallest are 8 bags of 13 and 3 bags of 14 = $104 + 42 = 146 < 150$. Not enough.

In the second case (B gets 11 bags), B chooses which 11 bags B gets. B will take the 11 largest bags. A gets the 10 smallest bags + remainder. The 10 smallest are 8 bags of 13 and 2 bags of 14 = $104 + 28 = 132$. Remainder = $300 - 21 \times \text{avg bag}$. But the bags aren't all the same size, so the remainder depends on which 21 bags are given out.

This is getting complicated. The non-adaptive approach gives at most 146 (as we computed). The adaptive approach should do better.

Let me think about the adaptive approach more carefully.

In the adaptive approach, A observes the current state $(a, b, r)$ and chooses the bag size accordingly. The key advantage is that A can adjust based on who has how many bags.

For example, if B has been taking many bags (B has more bags), A can make the bags larger (since B is closer to 11, B will be more reluctant to take bags). Conversely, if A has many bags, A should make bags smaller.

The continuous optimal strategy does exactly this: $c = r/(22-a-b)$, which adjusts based on the state.

Let me try to trace through a specific game path and see what A gets.

Path 1: B always gives bags to B (B takes all bags).
- State (0,0,300): A puts $c = 13$ (floor of 300/22). B takes it. State (0,1,287).
- State (0,1,287): $d = 21$, $c^* = 287/21 = 13.67$. A puts $c = 14$ (ceil). B takes. State (0,2,273).
  Wait, let me be more careful. A should choose the $c$ that maximizes the minimum. Let me use the loss formulas.

At (0,0,300): $d=22, r=300, q=13, s=14$.
- Floor loss: $14 \times 11 / (22 \times 21) = 154/462 = 1/3 \approx 0.333$.
- Ceil loss: $11 \times 8 / (22 \times 21) = 88/462 = 4/21 \approx 0.190$.
A chooses ceil ($c = 14$, loss $\approx 0.190$).

Wait, I made an error earlier. Let me recompute.

Loss from floor: $s(11-b)/[d(d-1)] = 14 \times 11 / (22 \times 21) = 154/462 = 1/3 \approx 0.333$.
Loss from ceil: $(11-a)(d-s)/[d(d-1)] = 11 \times 8 / (22 \times 21) = 88/462 = 4/21 \approx 0.190$.

A chooses ceil ($c = 14$), loss $\approx 0.190$. Value $\approx 150 - 0.190 = 149.81$.

B takes the bag (give to B branch). State becomes (0, 1, 286).

At (0,1,286): $d=21, r=286, q=13, s=286-13\times21=286-273=13$.
- Floor loss: $13 \times 10 / (21 \times 20) = 130/420 = 13/42 \approx 0.310$.
- Ceil loss: $11 \times 8 / (21 \times 20) = 88/420 = 22/105 \approx 0.210$.
A chooses ceil ($c = 14$), loss $\approx 0.210$. Value $\approx 11 \times 286/21 - 0.210 = 3146/21 - 0.210 = 149.81 - 0.210 = 149.60$.

Hmm wait, the value at (0,1,286) in continuous is $11 \times 286/21 = 3146/21 \approx 149.81$. With loss 0.210, discrete value $\approx 149.60$.

B takes. State (0, 2, 272).

At (0,2,272): $d=20, r=272, q=13, s=272-260=12$.
- Floor loss: $12 \times 9 / (20 \times 19) = 108/380 = 27/95 \approx 0.284$.
- Ceil loss: $11 \times 8 / (20 \times 19) = 88/380 = 22/95 \approx 0.232$.
A chooses ceil ($c = 14$), loss $\approx 0.232$.

B takes. State (0, 3, 258).

I see a pattern: B keeps taking, and A keeps putting 14 (ceil). Let me see how long this continues.

At (0, b, r): $d = 22-b$, $r = 300 - 14b$ (if A always puts 14 and B always takes).
$q = \lfloor r/d \rfloor$, $s = r \mod d$.

$b=0$: $r=300, d=22, q=13, s=14$. Ceil loss: $11 \times 8/462 = 0.190$.
$b=1$: $r=286, d=21, q=13, s=13$. Ceil loss: $11 \times 8/420 = 0.210$.
$b=2$: $r=272, d=20, q=13, s=12$. Ceil loss: $11 \times 8/380 = 0.232$.
$b=3$: $r=258, d=19, q=13, s=11$. Ceil loss: $11 \times 8/342 = 0.257$.
$b=4$: $r=244, d=18, q=13, s=10$. Ceil loss: $11 \times 8/306 = 0.288$.
$b=5$: $r=230, d=17, q=13, s=9$. Ceil loss: $11 \times 8/272 = 0.324$.
$b=6$: $r=216, d=16, q=13, s=8$. Ceil loss: $11 \times 8/240 = 0.367$.
$b=7$: $r=202, d=15, q=13, s=7$. Ceil loss: $11 \times 8/210 = 0.419$.
$b=8$: $r=188, d=14, q=13, s=6$. Ceil loss: $11 \times 8/182 = 0.484$.
$b=9$: $r=174, d=13, q=13, s=5$. Ceil loss: $11 \times 8/156 = 0.564$.

Wait, at $b=9$: $r=174, d=13, q=13, s=5$. $c^* = 174/13 = 13.38$. Ceil = 14.
Ceil loss: $(11-0)(13-5)/(13 \times 12) = 11 \times 8/156 = 88/156 = 0.564$.
Floor loss: $5 \times (11-9)/(13 \times 12) = 5 \times 2/156 = 10/156 = 0.064$.

Oh wait, floor loss is much smaller here! $s(11-b) = 5 \times 2 = 10$, vs ceil loss $11 \times 8 = 88$. So A should choose floor ($c = 13$) here.

Let me recompute. At $b=9$: $a=0, b=9, d=13, r=174, q=13, s=5$.
- Floor loss: $s(11-b)/[d(d-1)] = 5 \times 2 / (13 \times 12) = 10/156 = 0.064$.
- Ceil loss: $(11-a)(d-s)/[d(d-1)] = 11 \times 8 / (13 \times 12) = 88/156 = 0.564$.
A chooses floor ($c = 13$), loss $= 0.064$.

So at $b=9$, A switches to putting 13 coins. B takes. State (0, 10, 161).

At (0, 10, 161): $d=12, r=161, q=13, s=161-156=5$.
- Floor loss: $5 \times 1 / (12 \times 11) = 5/132 = 0.038$.
- Ceil loss: $11 \times 7 / (12 \times 11) = 77/132 = 0.583$.
A chooses floor ($c = 13$), loss $= 0.038$.

Now $b = 10$. If B takes this bag, B reaches 11, game ends, A gets remainder $= 161 - 13 = 148$.
If B gives to A: A gets 13, state (1, 10, 148). 

B minimizes A's gain:
- Give to A: $13 + f(1, 10, 148)$. Continuous: $13 + 10 \times 148/11 = 13 + 134.55 = 147.55$.
- Give to B: A gets $161 - 13 = 148$.
B gives to A (147.55 < 148).

So B gives to A. State (1, 10, 148).

At (1, 10, 148): $d = 11, r = 148, q = 13, s = 148 - 143 = 5$.
- Floor loss: $5 \times 1 / (11 \times 10) = 5/110 = 0.045$.
- Ceil loss: $10 \times 6 / (11 \times 10) = 60/110 = 0.545$.
A chooses floor ($c = 13$), loss $= 0.045$.

If B takes: B reaches 11, A gets $148 - 13 = 135$.
If B gives to A: $13 + f(2, 10, 135)$. Continuous: $13 + 9 \times 135/10 = 13 + 121.5 = 134.5$.
B gives to A (134.5 < 135).

State (2, 10, 135).

At (2, 10, 135): $d = 10, r = 135, q = 13, s = 5$.
- Floor loss: $5 \times 1 / (10 \times 9) = 5/90 = 0.056$.
- Ceil loss: $9 \times 5 / (10 \times 9) = 45/90 = 0.5$.
A chooses floor ($c = 13$), loss $= 0.056$.

If B takes: B reaches 11, A gets $135 - 13 = 122$.
If B gives to A: $13 + f(3, 10, 122)$. Continuous: $13 + 8 \times 122/9 = 13 + 108.44 = 121.44$.
B gives to A (121.44 < 122).

State (3, 10, 122).

At (3, 10, 122): $d = 9, r = 122, q = 13, s = 122 - 117 = 5$.
- Floor loss: $5 \times 1 / (9 \times 8) = 5/72 = 0.069$.
- Ceil loss: $8 \times 4 / (9 \times 8) = 32/72 = 0.444$.
A chooses floor ($c = 13$), loss $= 0.069$.

If B takes: A gets $122 - 13 = 109$.
If B gives to A: $13 + f(4, 10, 109)$. Continuous: $13 + 7 \times 109/8 = 13 + 95.375 = 108.375$.
B gives to A.

State (4, 10, 109).

At (4, 10, 109): $d = 8, r = 109, q = 13, s = 109 - 104 = 5$.
- Floor loss: $5 \times 1 / (8 \times 7) = 5/56 = 0.089$.
- Ceil loss: $7 \times 3 / (8 \times 7) = 21/56 = 0.375$.
A chooses floor ($c = 13$), loss $= 0.089$.

If B takes: A gets $109 - 13 = 96$.
If B gives to A: $13 + f(5, 10, 96)$. Continuous: $13 + 6 \times 96/7 = 13 + 82.286 = 95.286$.
B gives to A.

State (5, 10, 96).

At (5, 10, 96): $d = 7, r = 96, q = 13, s = 96 - 91 = 5$.
- Floor loss: $5 \times 1 / (7 \times 6) = 5/42 = 0.119$.
- Ceil loss: $6 \times 2 / (7 \times 6) = 12/42 = 0.286$.
A chooses floor ($c = 13$), loss $= 0.119$.

If B takes: A gets $96 - 13 = 83$.
If B gives to A: $13 + f(6, 10, 83)$. Continuous: $13 + 5 \times 83/6 = 13 + 69.167 = 82.167$.
B gives to A.

State (6, 10, 83).

At (6, 10, 83): $d = 6, r = 83, q = 13, s = 83 - 78 = 5$.
- Floor loss: $5 \times 1 / (6 \times 5) = 5/30 = 0.167$.
- Ceil loss: $5 \times 1 / (6 \times 5) = 5/30 = 0.167$.
Equal! A can choose either. Let's say floor ($c = 13$), loss $= 0.167$.

If B takes: A gets $83 - 13 = 70$.
If B gives to A: $13 + f(7, 10, 70)$. Continuous: $13 + 4 \times 70/5 = 13 + 56 = 69$.
B gives to A (69 < 70).

State (7, 10, 70).

At (7, 10, 70): $d = 5, r = 70, q = 14, s = 0$. No loss! $c = 14$.

If B takes: A gets $70 - 14 = 56$.
If B gives to A: $14 + f(8, 10, 56)$. Continuous: $14 + 3 \times 56/4 = 14 + 42 = 56$.
B is indifferent. Both give A 56.

Let's say B gives to A. State (8, 10, 56).

At (8, 10, 56): $d = 4, r = 56, q = 14, s = 0$. No loss! $c = 14$.

If B takes: A gets $56 - 14 = 42$.
If B gives to A: $14 + f(9, 10, 42)$. Continuous: $14 + 2 \times 42/3 = 14 + 28 = 42$.
B is indifferent. Both give A 42.

State (9, 10, 42).

At (9, 10, 42): $d = 3, r = 42, q = 14, s = 0$. No loss! $c = 14$.

If B takes: A gets $42 - 14 = 28$.
If B gives to A: $14 + f(10, 10, 28)$. $f(10, 10, 28) = \lfloor 28/2 \rfloor = 14$. So $14 + 14 = 28$.
B is indifferent. Both give A 28.

State (10, 10, 28).

At (10, 10, 28): $f = \lfloor 28/2 \rfloor = 14$. A puts $c = 14$.
- Give to A: A gets 14, game ends.
- Give to B: A gets $28 - 14 = 14$.
A gets 14.

So along this path, A gets $14 + 14 + 14 + 14 + 14 + 14 + 14 + 14 + 14 + 13 + 13 + 13 + 13 + 13 + 13 + 13 + 14 + 14 + 14 + 14 + 14$... 

Wait, I need to track A's accumulated coins. Let me retrace.

Path: B takes 9 bags, then gives 10 bags to A (with B at 10 bags), then the last bag.

Actually, let me retrace more carefully.

B takes bags for $b = 0, 1, ..., 9$ (10 bags taken by B). A puts 14 for $b = 0,...,8$ and 13 for $b = 9$.
Coins used: $9 \times 14 + 1 \times 13 = 126 + 13 = 139$. Remaining: $300 - 139 = 161$.
A has 0 coins, 0 bags. B has 0 coins, 10 bags.

Then at (0, 10, 161): A puts 13. B gives to A. A gets 13, 1 bag. State (1, 10, 148).
At (1, 10, 148): A puts 13. B gives to A. A gets 13, 2 bags. State (2, 10, 135).
...
This continues. A puts 13 each time, B gives to A.

At (a, 10, r): A puts 13. 
- Give to A: A gets 13, state (a+1, 10, r-13).
- Give to B: B reaches 11, A gets r - 13.

B gives to A as long as $13 + f(a+1, 10, r-13) < r - 13$, i.e., $f(a+1, 10, r-13) < r - 26$.

From the continuous formula: $f(a+1, 10, r-13) = (10-a)(r-13)/(11-a)$. 
We need $(10-a)(r-13)/(11-a) < r - 26$.
$(10-a)(r-13) < (11-a)(r-26)$.
$(10-a)r - 13(10-a) < (11-a)r - 26(11-a)$.
$r[(10-a) - (11-a)] < 13(10-a) - 26(11-a)$.
$-r < 130 - 13a - 286 + 26a$.
$-r < 13a - 156$.
$r > 156 - 13a$.

At $a = 0$: $r = 161 > 156$. ✓ B gives to A.
At $a = 1$: $r = 148 > 143$. ✓
At $a = 2$: $r = 135 > 130$. ✓
At $a = 3$: $r = 122 > 117$. ✓
At $a = 4$: $r = 109 > 104$. ✓
At $a = 5$: $r = 96 > 91$. ✓
At $a = 6$: $r = 83 > 78$. ✓
At $a = 7$: $r = 70 > 69$. ✓ (barely)
At $a = 8$: $r = 56$. Need $r > 156 - 104 = 52$. $56 > 52$. ✓ But at $a=8$, A puts 14 (since $c^* = 56/4 = 14$ is integer).

Hmm wait, at $a = 7$, $r = 70$, $d = 5$, $c^* = 14$. A puts 14.
- Give to A: $14 + f(8, 10, 56) = 14 + 3 \times 56/4 = 14 + 42 = 56$ (continuous).
- Give to B: $70 - 14 = 56$.
B is indifferent. Let's say B gives to A.

At $a = 8$, $r = 56$, $d = 4$, $c^* = 14$. A puts 14.
- Give to A: $14 + f(9, 10, 42) = 14 + 2 \times 42/3 = 14 + 28 = 42$.
- Give to B: $56 - 14 = 42$.
B is indifferent.

At $a = 9$, $r = 42$, $d = 3$, $c^* = 14$. A puts 14.
- Give to A: $14 + f(10, 10, 28) = 14 + 14 = 28$.
- Give to B: $42 - 14 = 28$.
B is indifferent.

At $a = 10$, $r = 28$. $f(10, 10, 28) = 14$.

So along this path, A gets:
- 0 coins from the first 10 bags (B took them all).
- 13 + 13 + 13 + 13 + 13 + 13 + 13 + 14 + 14 + 14 = $7 \times 13 + 3 \times 14 = 91 + 42 = 133$ coins from the next 10 bags (given to A).
- 14 coins from the last bag.
Total: $133 + 14 = 147$.

Hmm, 147. But this is just one path. B might choose differently.

Wait, but I need to check: is this the worst case for A? B is trying to minimize A's coins. Let me check if B could do better (give A fewer coins).

The path I traced has B taking 10 bags, then giving 10 bags to A, then the last bag is split. A gets 147.

But what if B takes fewer bags early on? Let me check another path.

Path 2: B gives some bags to A early on.

At (0, 0, 300): A puts 14 (ceil). 
- Give to A: $14 + f(1, 0, 286) = 14 + 10 \times 286/21 = 14 + 136.19 = 150.19$ (continuous).
- Give to B: $f(0, 1, 286) = 11 \times 286/21 = 149.81$ (continuous).
B gives to B (149.81 < 150.19).

So B takes the first bag. Same as before.

At (0, 1, 286): A puts 14 (ceil).
- Give to A: $14 + f(1, 1, 272) = 14 + 10 \times 272/20 = 14 + 136 = 150$ (continuous).
- Give to B: $f(0, 2, 272) = 11 \times 272/20 = 149.6$ (continuous).
B gives to B (149        — AI历史解题过程（thinking）
#   polymath_01156         — 题目ID

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
  <problem_id>polymath_01156</problem_id>
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

Problem 10.8. Two bandits stole 300 gold coins. They decided to divide them as follows: the first bandit puts some coins (possibly all) into a bag, and the second bandit chooses who gets this bag; then this action is repeated several times. The division ends when

- either all the money is gone,
- or someone gets 11 bags - in this case, all the remaining money immediately goes to the other bandit.

What is the maximum number of coins that the first bandit can guarantee to get?

## Standard Solution

Answer: 146.

Solution. First, we will show that the first bandit can get at least 146 coins. His strategy will be to put 14 coins in each bag. First, note that he will always be able to do this: since $21 \cdot 14=294$, he will do this at least 21 times, and when the coins start to run out, the process will certainly be over (one of the bandits will get 11 bags).

Let's analyze how the game can end. If the first bandit has accumulated 11 bags, that's already 154 coins. In the other case, the second bandit, on the contrary, has no more than 11 bags, that is, no more than 154 coins. Therefore, the remaining coins are with the first bandit, which is at least 146.

Now we will show how the second bandit can guarantee himself 154 coins. His strategy is as follows: take bags with 14 coins or more for himself, and give bags with 13 coins or less to the first bandit.

Similarly, let's analyze how the game can end. If the second bandit finishes with 11 bags, he will have at least 154 coins. In the other case, the first bandit will finish with no more than 11 bags, which is no more than $11 \cdot 13=143$ coins. Then the second bandit will have at least 157 coins.

Remark. Let's indicate how to get the answer in the general case. Suppose there are $N$ coins in total, and each bandit can get no more than $k$ bags ($N \geqslant 2 k$). We will divide the coins into $2 k$ almost equal groups, so that either all groups have the same number of coins (if $N \vdots 2 k$), or the number of coins in the groups differs by no more than 1 (such a division is unique). We will order the groups in ascending order. By reasoning similar to the one provided above, we can show that the first bandit can guarantee himself the sum of the $k$ smaller groups of the division, and the second bandit can guarantee the sum of the $k$ larger groups.

## 11th Grade

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. This is a game theory problem about two bandits dividing 300 gold coins.

Let me understand the rules:
- First bandit puts some coins (possibly all) into a bag
- Second bandit chooses who gets this bag
- This action is repeated several times
- Division ends when:
  - All money is gone, OR
  - Someone gets 11 bags - in this case all remaining money goes to the other bandit

Question: What is the maximum number of coins the first bandit can guarantee to get?

Let me think about this carefully. The first bandit (let's call A) chooses how many coins to put in each bag. The second bandit (B) chooses who gets each bag. B will always give each bag to the person for whom it's worse (from A's perspective), i.e., B minimizes A's total.

The game ends when:
1. All coins are distributed, or
2. Someone reaches 11 bags, and the other person gets all remaining coins.

A wants to maximize his guaranteed coins. B wants to minimize A's coins (equivalently maximize B's own).

Let me think about the structure. A controls the bag sizes. B controls the allocation. The constraint is the 11-bag limit.

If A puts coins in bags and B allocates them, B will try to make one person reach 11 bags quickly. If A reaches 11 bags, B gets all remaining coins. If B reaches 11 bags, A gets all remaining coins.

So B wants to give bags to A (to make A reach 11 first, so B gets the remainder). But B also wants to keep the valuable bags for himself.

Wait, let me reconsider. B chooses who gets each bag. B wants to maximize B's own coins. 

Strategy for B: For each bag, B can either take it himself or give it to A. 

If B gives a bag to A, A's bag count increases. If A reaches 11 bags, B gets all remaining coins.
If B takes a bag, B's bag count increases. If B reaches 11 bags, A gets all remaining coins.

So there's tension: B wants to take large bags for himself, but taking too many bags means B reaches 11 first and A gets the remainder.

Let me think about this as a sequential game. A chooses bag sizes one at a time (or all at once?). Actually, the problem says "this action is repeated several times" - so it's sequential. A puts coins in a bag, B allocates, repeat.

Actually, A can adapt based on previous allocations. So it's a sequential game with perfect information.

Let me think about what A can guarantee.

Let's say at any point, A has $a$ bags and $x$ coins, B has $b$ bags and $y$ coins, and $r$ coins remain. $a + b$ bags have been given out, $x + y + r = 300$.

A's turn: A puts $c$ coins in a bag ($1 \le c \le r$). B chooses who gets it.

If B gives to A: A now has $a+1$ bags, $x+c$ coins. If $a+1 = 11$, B gets all $r - c$ remaining coins.
If B gives to B: B now has $b+1$ bags, $y+c$ coins. If $b+1 = 11$, A gets all $r - c$ remaining coins.

A wants to maximize his final total. B wants to minimize A's final total.

Let me think about the endgame. When someone has 10 bags, the next bag they receive gives them 11, and the other person gets the remainder.

Key insight: A controls bag sizes. B controls allocation. A can try to make bags of specific sizes to create dilemmas for B.

Let me think about small cases first to build intuition.

Let me think about the state as $(a, b, r)$ where $a$ = A's bags, $b$ = B's bags, $r$ = remaining coins. A's accumulated coins don't matter for the decision (only final total matters), but actually they do matter because the game could end with all coins distributed.

Hmm, actually this is complex. Let me think about it differently.

Let me define $V(a, b, r)$ = the maximum coins A can guarantee from state $(a, b, r)$, assuming A has already collected some coins (which we track separately). Actually, let me think of it as: from state $(a, b, r)$ with A having collected $x$ and B having collected $y$ ($x + y + r = 300$), A wants to maximize his final total.

Actually, the coins already collected don't affect future decisions - only $a$, $b$, and $r$ matter for the future. The coins already collected are sunk. So let $f(a, b, r)$ = additional coins A can guarantee from this state (beyond what he already has).

A chooses $c \in \{1, 2, ..., r\}$.
B then chooses:
- Give to A: A gets $c$ from this bag. If $a+1 = 11$, game ends, A gets $c$ total (no more). So A gets $c$.
  - If $a+1 < 11$: A gets $c + f(a+1, b, r-c)$.
- Give to B: A gets $0$ from this bag. If $b+1 = 11$, game ends, A gets all $r - c$ remaining.
  - If $b+1 < 11$: A gets $f(a, b+1, r-c)$.

B minimizes A's gain, so B chooses the option giving A less.

$f(a, b, r) = \max_{c} \min(\text{give to A}, \text{give to B})$

where:
- give to A = $c + f(a+1, b, r-c)$ if $a+1 < 11$, else $c$
- give to B = $r - c$ if $b+1 = 11$, else $f(a, b+1, r-c)$

Base case: $f(a, b, 0) = 0$ (no coins left).

We want $f(0, 0, 300)$.

This is a complex dynamic program. Let me think about the structure more.

When $a = 10$ (A has 10 bags): If B gives a bag to A, A reaches 11 and B gets the remainder. So B would give to A only if giving to A is worse for A than giving to B.

When $a = 10$: A chooses $c$. 
- Give to A: A gets $c$ (game ends, B gets $r-c$).
- Give to B: B gets bag, $b+1$ bags. If $b+1 = 11$, A gets $r - c$. Otherwise, $f(10, b+1, r-c)$.

B minimizes, so B gives to A if $c \le$ (give to B value), and gives to B otherwise.

When $b = 10$ (B has 10 bags): If B gives a bag to B, B reaches 11 and A gets the remainder. So:
- Give to A: $c + f(a+1, 10, r-c)$ if $a+1 < 11$, else $c$.
- Give to B: A gets $r - c$ (game ends).

B minimizes: gives to B if $r - c \le$ (give to A value), gives to A otherwise.

This is getting complex. Let me think about it more cleverly.

Let me think about the total number of bags. The game ends when someone has 11 bags or all coins are gone. The maximum number of bags is 21 (10 each + 1 more to someone). Actually, if both have 10, the next bag goes to someone making them 11, so max 21 bags.

Actually, the game can end earlier if coins run out. With 300 coins, if each bag has at least 1 coin, we can have at most 300 bags, but the 11-bag rule caps it at 21 bags.

So the game lasts at most 21 rounds (bags). With 300 coins, coins won't run out before 21 bags (since each bag needs at least 1 coin, 21 bags need at least 21 coins, and we have 300).

Wait, but A could put all remaining coins in one bag. So the number of bags is at most 21 (since someone will reach 11 bags before coins run out, given 300 coins >> 21).

Actually, A controls the bag sizes. A could put many coins in few bags. The game ends when someone has 11 bags OR all coins are gone. If A puts all 300 coins in one bag, then 1 bag is given out, 0 coins remain, game ends. But that's bad for A because B chooses who gets it.

So A wants to spread coins across bags strategically.

Let me think about the key strategic consideration. A wants to maximize his guaranteed coins. B allocates each bag to minimize A's coins.

The critical tension: B wants to give bags to A (to make A reach 11 first, so B gets the remainder). But if B always gives bags to A, A gets all the coins in those bags. B would only give bags to A if the coins in those bags are small, and B would take bags with many coins.

So A's strategy: make bags of specific sizes so that B faces a dilemma. If B takes a bag (large), B's bag count increases, bringing B closer to 11. If B gives to A, A gets the coins but A's bag count increases.

Let me think about the endgame more carefully.

Suppose A has $a$ bags and B has $b$ bags, with $r$ coins remaining. The game will last at most $11 - a + 11 - b - 1 = 21 - a - b$ more bags (until someone reaches 11). Actually, it could end sooner if coins run out, but with enough coins, it lasts until someone reaches 11.

Let me think about the case where coins are plentiful (won't run out). Then the game always ends with someone reaching 11 bags.

If A reaches 11 first (after receiving the $k$-th bag where $k = 11 - a$ more bags to A), B gets all remaining coins.
If B reaches 11 first, A gets all remaining coins.

So the question is: who reaches 11 first, and how many coins are distributed before that?

B controls allocation. B will try to reach a state where B gets the most coins. 

Let me think about it from B's perspective. B wants to maximize B's coins = 300 - A's coins. 

If the game ends with A reaching 11 bags, B gets all remaining coins at that point. B's coins = coins in bags B received + remaining coins.
If the game ends with B reaching 11 bags, A gets all remaining coins. A's coins = coins in bags A received + remaining coins.

So B wants to either:
1. Make A reach 11 first (B gets remainder), while keeping the bags B received large, OR
2. Make B reach 11 first (A gets remainder), but only if the bags B received are so large that even giving up the remainder is worth it.

Hmm, this is a complex game. Let me try to think about it with the DP approach but for specific small cases.

Let me try to compute $f(a, b, r)$ for small values and see if I can find a pattern.

Actually, with 300 coins and at most 21 bags, the state space is manageable: $a \in \{0,...,10\}$, $b \in \{0,...,10\}$, $r \in \{0,...,300\}$. That's $11 \times 11 \times 301 \approx 36000$ states. But computing this by hand is infeasible.

Let me think about the structure more cleverly.

Key observation: Since 300 >> 21, coins will never run out before someone reaches 11 bags (as long as A puts at least 1 coin per bag, which A must). So the game always ends with someone reaching 11 bags.

Wait, A could put all remaining coins in one bag. But that would mean fewer bags. If A puts all $r$ coins in one bag, the game gives out 1 bag, and if no one reaches 11, continues with 0 coins remaining, so game ends with all coins distributed. But this is only relevant if $a + b < 10$ (i.e., neither is close to 11).

Actually, A must put at least 1 coin per bag (some coins, possibly all). So if A always puts exactly 1 coin per bag, after 21 bags (someone reaches 11), 21 coins are distributed and 279 go to the other person. That's terrible for A if A reaches 11 first.

Let me think about what happens when A reaches 11 first. A has 11 bags, B gets all remaining coins. A's total = sum of coins in A's 11 bags. B's total = sum of coins in B's bags + remaining.

If B reaches 11 first. B has 11 bags, A gets all remaining coins. A's total = sum of coins in A's bags + remaining. B's total = sum of coins in B's 11 bags.

So A wants B to reach 11 first (so A gets the remainder), and A wants the bags B takes to be small (so B's total is small, meaning A's is large).

B wants A to reach 11 first (so B gets the remainder), and B wants the bags A gets to be small.

But B controls allocation. So B will try to give bags to A (to make A reach 11 first) unless the bag is too valuable.

Let me think about the equilibrium. A chooses bag sizes to create the worst dilemma for B.

Let me consider a simplified version: suppose the game must end with someone reaching 11 bags (coins are plentiful). A has $a$ bags, B has $b$ bags. The game will last exactly $\min(11-a, 11-b) + $ some more bags until someone reaches 11.

Actually, the number of bags until someone reaches 11: if B always gives to A, A reaches 11 after $11 - a$ bags. If B always takes, B reaches 11 after $11 - b$ bags. B will mix to optimize.

Let me think about the last few bags.

When $a = 10, b = 10$: A puts $c$ coins. 
- Give to A: A reaches 11, A gets $c$, B gets $r - c$. A's gain = $c$.
- Give to B: B reaches 11, A gets $r - c$. A's gain = $r - c$.
B minimizes A's gain: $\min(c, r-c)$. A maximizes: $\max_c \min(c, r-c) = \lfloor r/2 \rfloor$ (by choosing $c = \lfloor r/2 \rfloor$ or $\lceil r/2 \rceil$).

So $f(10, 10, r) = \lfloor r/2 \rfloor$.

When $a = 10, b = 9$: A puts $c$ coins.
- Give to A: A reaches 11, A gets $c$. A's gain = $c$.
- Give to B: B has 10 bags. $f(10, 10, r-c) = \lfloor (r-c)/2 \rfloor$.
B minimizes: $\min(c, \lfloor (r-c)/2 \rfloor)$.
A maximizes: $\max_c \min(c, \lfloor (r-c)/2 \rfloor)$.

Let me find the optimal $c$. We want $c \approx \lfloor (r-c)/2 \rfloor$, i.e., $c \approx (r-c)/2$, so $3c \approx r$, $c \approx r/3$.

$f(10, 9, r) \approx r/3$.

When $a = 10, b = 8$: 
- Give to A: A gets $c$.
- Give to B: $f(10, 9, r-c) \approx (r-c)/3$.
$\min(c, (r-c)/3)$. Set $c = (r-c)/3$: $4c = r$, $c = r/4$.
$f(10, 8, r) \approx r/4$.

Pattern: $f(10, b, r) \approx r / (11 - b)$.

Let me verify: $f(10, 10, r) = r/2 = r/(11-10)$. ✓
$f(10, 9, r) = r/3 = r/(11-9)$. ✓
$f(10, 8, r) = r/4 = r/(11-8)$. ✓

So $f(10, b, r) \approx r / (11 - b)$.

Now let's go to $a = 9$.

$f(9, b, r)$: A puts $c$.
- Give to A: $c + f(10, b, r-c) \approx c + (r-c)/(11-b)$.
- Give to B: $f(9, b+1, r-c)$.

B minimizes. Let me compute $f(9, 10, r)$ first.

$f(9, 10, r)$: A puts $c$.
- Give to A: $c + f(10, 10, r-c) = c + \lfloor (r-c)/2 \rfloor \approx c + (r-c)/2 = (r+c)/2$.
- Give to B: B reaches 11, A gets $r - c$.
B minimizes: $\min((r+c)/2, r-c)$.
Set $(r+c)/2 = r-c$: $r + c = 2r - 2c$, $3c = r$, $c = r/3$.
$f(9, 10, r) \approx (r + r/3)/2 = (4r/3)/2 = 2r/3$.

Alternatively, $r - c = r - r/3 = 2r/3$. ✓

$f(9, 9, r)$: A puts $c$.
- Give to A: $c + f(10, 9, r-c) \approx c + (r-c)/3 = (3c + r - c)/3 = (r + 2c)/3$.
- Give to B: $f(9, 10, r-c) \approx 2(r-c)/3$.
B minimizes: $\min((r+2c)/3, 2(r-c)/3)$.
Set equal: $r + 2c = 2r - 2c$, $4c = r$, $c = r/4$.
$f(9, 9, r) \approx (r + 2 \cdot r/4)/3 = (r + r/2)/3 = (3r/2)/3 = r/2$.

Check: $2(r - r/4)/3 = 2 \cdot 3r/4 / 3 = r/2$. ✓

$f(9, 8, r)$:
- Give to A: $c + f(10, 8, r-c) \approx c + (r-c)/4 = (r + 3c)/4$.
- Give to B: $f(9, 9, r-c) \approx (r-c)/2$.
Set equal: $(r + 3c)/4 = (r-c)/2$, $r + 3c = 2r - 2c$, $5c = r$, $c = r/5$.
$f(9, 8, r) \approx (r + 3r/5)/4 = (8r/5)/4 = 2r/5$.

Check: $(r - r/5)/2 = (4r/5)/2 = 2r/5$. ✓

Pattern for $f(9, b, r)$:
- $f(9, 10, r) = 2r/3$
- $f(9, 9, r) = r/2 = 2r/4$
- $f(9, 8, r) = 2r/5$

So $f(9, b, r) \approx 2r / (12 - b)$.

Let me check: $f(9, 10) = 2r/2 = r$? No, $12 - 10 = 2$, $2r/2 = r$. But we computed $2r/3$. That doesn't match.

Let me recompute. $f(9, 10, r) = 2r/3$. $12 - 10 = 2$. $2r/2 = r \neq 2r/3$.

Hmm, let me reconsider. Let me tabulate:
- $f(9, 10, r) = 2r/3$
- $f(9, 9, r) = r/2 = 2r/4$  (wait, $r/2 = 2r/4$? No, $r/2 = 2r/4$? $2r/4 = r/2$. Yes.)
- $f(9, 8, r) = 2r/5$

So the denominators are 3, 4, 5. The pattern is $f(9, b, r) = 2r / (b + 3)$? 
- $b=10$: $2r/13$? No, that's $2r/3$.

Wait: $b=10 \to 3$, $b=9 \to 4$, $b=8 \to 5$. So denominator $= 13 - b$.
$f(9, b, r) = 2r / (13 - b)$.

Check: $b=10$: $2r/3$ ✓. $b=9$: $2r/4 = r/2$ ✓. $b=8$: $2r/5$ ✓.

And for $f(10, b, r) = r / (11 - b)$, which we can write as $1 \cdot r / (11 - b)$.

Let me see if there's a general pattern. Let me define $f(a, b, r) = \alpha(a, b) \cdot r$ where $\alpha$ is some fraction.

$f(10, b) = 1/(11-b)$. So $\alpha(10, b) = 1/(11-b)$.
$f(9, b) = 2/(13-b)$. So $\alpha(9, b) = 2/(13-b)$.

Let me compute $f(8, b, r)$ to see the pattern.

$f(8, 10, r)$: A puts $c$.
- Give to A: $c + f(9, 10, r-c) \approx c + 2(r-c)/3 = (3c + 2r - 2c)/3 = (2r + c)/3$.
- Give to B: B reaches 11, A gets $r - c$.
Set equal: $(2r + c)/3 = r - c$, $2r + c = 3r - 3c$, $4c = r$, $c = r/4$.
$f(8, 10, r) \approx (2r + r/4)/3 = (9r/4)/3 = 3r/4$.
Check: $r - r/4 = 3r/4$ ✓.

$f(8, 9, r)$:
- Give to A: $c + f(9, 9, r-c) \approx c + (r-c)/2 = (r + c)/2$.
- Give to B: $f(8, 10, r-c) \approx 3(r-c)/4$.
Set equal: $(r + c)/2 = 3(r-c)/4$, $2(r+c) = 3(r-c)$, $2r + 2c = 3r - 3c$, $5c = r$, $c = r/5$.
$f(8, 9, r) \approx (r + r/5)/2 = (6r/5)/2 = 3r/5$.
Check: $3(r - r/5)/4 = 3 \cdot 4r/5 / 4 = 3r/5$ ✓.

$f(8, 8, r)$:
- Give to A: $c + f(9, 8, r-c) \approx c + 2(r-c)/5 = (5c + 2r - 2c)/5 = (2r + 3c)/5$.
- Give to B: $f(8, 9, r-c) \approx 3(r-c)/5$.
Set equal: $(2r + 3c)/5 = 3(r-c)/5$, $2r + 3c = 3r - 3c$, $6c = r$, $c = r/6$.
$f(8, 8, r) \approx (2r + 3 \cdot r/6)/5 = (2r + r/2)/5 = (5r/2)/5 = r/2$.
Check: $3(r - r/6)/5 = 3 \cdot 5r/6 / 5 = r/2$ ✓.

$f(8, 7, r)$:
- Give to A: $c + f(9, 7, r-c)$. Need $f(9, 7, r)$.
$f(9, 7, r) = 2r/(13-7) = 2r/6 = r/3$.
So give to A: $c + (r-c)/3 = (r + 2c)/3$.
- Give to B: $f(8, 8, r-c) \approx (r-c)/2$.
Set equal: $(r + 2c)/3 = (r-c)/2$, $2(r + 2c) = 3(r-c)$, $2r + 4c = 3r - 3c$, $7c = r$, $c = r/7$.
$f(8, 7, r) \approx (r + 2r/7)/3 = (9r/7)/3 = 3r/7$.
Check: $(r - r/7)/2 = (6r/7)/2 = 3r/7$ ✓.

Pattern for $f(8, b, r)$:
- $b=10$: $3r/4$
- $b=9$: $3r/5$
- $b=8$: $r/2 = 3r/6$
- $b=7$: $3r/7$

So $f(8, b, r) = 3r / (14 - b)$.

Check: $b=10$: $3r/4$ ✓. $b=9$: $3r/5$ ✓. $b=8$: $3r/6 = r/2$ ✓. $b=7$: $3r/7$ ✓.

Now I see the pattern:
- $f(10, b, r) = 1 \cdot r / (11 - b)$ → numerator 1, denominator offset 11
- $f(9, b, r) = 2 \cdot r / (13 - b)$ → numerator 2, denominator offset 13
- $f(8, b, r) = 3 \cdot r / (14 - b)$ → numerator 3, denominator offset 14

Wait, let me recheck the offsets:
- $f(10, b)$: denominator $= 11 - b$. When $b = 10$, denom $= 1$, but $f(10, 10) = r/2$. That's $r/2$, not $r/1$.

Hmm wait, $f(10, 10, r) = \lfloor r/2 \rfloor \approx r/2$. And $11 - 10 = 1$. $r/1 = r \neq r/2$.

I think I made an error. Let me recheck.

$f(10, 10, r) = \lfloor r/2 \rfloor \approx r/2$. Denominator should be 2, not 1.

$f(10, b, r)$:
- $b=10$: $r/2$
- $b=9$: $r/3$
- $b=8$: $r/4$

So $f(10, b, r) = r / (12 - b)$. Check: $b=10$: $r/2$ ✓. $b=9$: $r/3$ ✓. $b=8$: $r/4$ ✓.

$f(9, b, r)$:
- $b=10$: $2r/3$
- $b=9$: $r/2 = 2r/4$
- $b=8$: $2r/5$
- $b=7$: $r/3 = 2r/6$

So $f(9, b, r) = 2r / (13 - b)$. Check: $b=10$: $2r/3$ ✓. $b=9$: $2r/4$ ✓. $b=8$: $2r/5$ ✓. $b=7$: $2r/6$ ✓.

$f(8, b, r)$:
- $b=10$: $3r/4$
- $b=9$: $3r/5$
- $b=8$: $3r/6 = r/2$
- $b=7$: $3r/7$

So $f(8, b, r) = 3r / (14 - b)$. Check: $b=10$: $3r/4$ ✓. $b=9$: $3r/5$ ✓. $b=8$: $3r/6$ ✓. $b=7$: $3r/7$ ✓.

Now the pattern is clear:
- $f(a, b, r) = (11 - a) \cdot r / (11 - a + 11 - b)$

Let me verify:
- $f(10, b, r) = 1 \cdot r / (1 + 11 - b) = r / (12 - b)$ ✓
- $f(9, b, r) = 2 \cdot r / (2 + 11 - b) = 2r / (13 - b)$ ✓
- $f(8, b, r) = 3 \cdot r / (3 + 11 - b) = 3r / (14 - b)$ ✓

So the general formula is:
$$f(a, b, r) = \frac{(11 - a) \cdot r}{(11 - a) + (11 - b)} = \frac{(11 - a) \cdot r}{22 - a - b}$$

Let me verify this with one more case. Let me compute $f(7, 10, r)$.

$f(7, 10, r) = 4r / (4 + 1) = 4r/5$.

Let me verify by computation:
$f(7, 10, r)$: A puts $c$.
- Give to A: $c + f(8, 10, r-c) \approx c + 3(r-c)/4 = (4c + 3r - 3c)/4 = (3r + c)/4$.
- Give to B: B reaches 11, A gets $r - c$.
Set equal: $(3r + c)/4 = r - c$, $3r + c = 4r - 4c$, $5c = r$, $c = r/5$.
$f(7, 10, r) \approx (3r + r/5)/4 = (16r/5)/4 = 4r/5$ ✓.

Let me also verify $f(7, 9, r) = 4r / (4 + 2) = 4r/6 = 2r/3$.
- Give to A: $c + f(8, 9, r-c) \approx c + 3(r-c)/5 = (5c + 3r - 3c)/5 = (3r + 2c)/5$.
- Give to B: $f(7, 10, r-c) \approx 4(r-c)/5$.
Set equal: $(3r + 2c)/5 = 4(r-c)/5$, $3r + 2c = 4r - 4c$, $6c = r$, $c = r/6$.
$f(7, 9, r) \approx (3r + 2r/6)/5 = (3r + r/3)/5 = (10r/3)/5 = 2r/3$ ✓.

The formula is confirmed:
$$f(a, b, r) = \frac{(11 - a) \cdot r}{22 - a - b}$$

Now, the answer to the problem is:
$$f(0, 0, 300) = \frac{11 \cdot 300}{22} = \frac{3300}{22} = 150$$

So the first bandit can guarantee 150 coins.

Wait, but I need to be more careful. The formula assumes coins are always plentiful (game ends with someone reaching 11 bags, not coins running out). With 300 coins and at most 21 bags, each bag has at least 1 coin, so at most 21 coins are used, and 279 remain. The game always ends with someone reaching 11. But actually, A could choose to put all remaining coins in one bag, which would end the game early (coins run out). Let me check if this could be better for A.

Actually, in the DP, A chooses $c$ (the bag size) optimally, including the possibility of $c = r$ (all remaining coins). The formula I derived assumes the optimal $c$ is $r / (22 - a - b)$, which is less than $r$ as long as $22 - a - b > 1$, i.e., $a + b < 21$. Since the game starts with $a + b = 0$, and the formula gives $c = r/22$ at the start, this is fine.

But wait, I need to also check that the formula is exactly correct, not just approximately. The issue is the floor function from $f(10, 10, r) = \lfloor r/2 \rfloor$.

Let me think about whether the exact answer is 150 or could be slightly different due to rounding.

Actually, let me reconsider. The formula $f(a, b, r) = (11-a) \cdot r / (22 - a - b)$ assumes that A can choose $c$ to be any real number, but $c$ must be a positive integer. With $r = 300$ and the denominators being at most 22, the rounding effects should be small.

Let me trace through more carefully. At the start, $f(0, 0, 300) = 11 \cdot 300 / 22 = 150$.

The optimal first bag size is $c = 300 / 22 \approx 13.6$, so $c = 14$ or $c = 13$.

Let me check: if $c = 14$:
- Give to A: $14 + f(1, 0, 286) = 14 + 10 \cdot 286 / 21 = 14 + 2860/21 \approx 14 + 136.19 = 150.19$.
- Give to B: $f(0, 1, 286) = 11 \cdot 286 / 21 = 3146/21 \approx 149.81$.
B minimizes: $\min(150.19, 149.81) = 149.81$.

If $c = 13$:
- Give to A: $13 + f(1, 0, 287) = 13 + 10 \cdot 287 / 21 = 13 + 2870/21 \approx 13 + 136.67 = 149.67$.
- Give to B: $f(0, 1, 287) = 11 \cdot 287 / 21 = 3157/21 \approx 150.33$.
B minimizes: $\min(149.67, 150.33) = 149.67$.

If $c = 14$: A gets $\approx 149.81$.
If $c = 13$: A gets $\approx 149.67$.

So $c = 14$ is better. But the exact value depends on the integer constraints throughout the game.

Hmm, but the formula gives 150 exactly. The question is whether the integer constraints reduce this.

Let me think about this differently. The formula $f(a, b, r) = (11-a) r / (22 - a - b)$ is exact when $r$ is divisible by $(22 - a - b)$ and the optimal $c = r / (22 - a - b)$ is an integer. 

At the start, $r = 300$, $22 - 0 - 0 = 22$, $300 / 22$ is not an integer. So the exact answer might differ from 150.

Let me think about this more carefully. The key insight is that the formula gives the continuous relaxation, and the integer version might be slightly less.

Actually, let me reconsider the problem. The formula says A can guarantee approximately 150. The question asks for the maximum number of coins A can guarantee. This should be an integer.

Let me think about whether A can guarantee exactly 150 or slightly less.

Actually, I think the answer is 150. Let me think about why.

Consider the continuous version: A can guarantee exactly $11 \cdot 300 / 22 = 150$. In the discrete version, A might guarantee slightly less, but the problem likely has a clean answer.

Hmm, but actually let me reconsider whether the formula is exactly right or just approximately right. Let me re-derive more carefully.

The recurrence is:
$$f(a, b, r) = \max_{1 \le c \le r} \min\left(\text{give to A}, \text{give to B}\right)$$

where:
- give to A = $c + f(a+1, b, r-c)$ if $a+1 < 11$, else $c$
- give to B = $r - c$ if $b+1 = 11$, else $f(a, b+1, r-c)$

In the continuous version (where $c$ can be any real in $(0, r]$), the formula $f(a,b,r) = (11-a)r/(22-a-b)$ is exact.

In the discrete version, we need $c$ to be a positive integer. The question is whether the rounding losses accumulate.

Let me think about it from a different angle. Let me consider the total number of bags given to A and B.

If the game ends with A receiving $p$ bags and B receiving $q$ bags, where either $p = 11$ or $q = 11$, and the remaining coins go to the person who didn't reach 11.

A's total = (coins in A's bags) + (remaining coins if B reached 11).
B's total = (coins in B's bags) + (remaining coins if A reached 11).

A controls bag sizes, B controls allocation. 

In the continuous analysis, the equilibrium is that A gets fraction $(11-a)/(22-a-b)$ of the remaining coins at each state. At the start, A gets $11/22 = 1/2$ of all coins = 150.

The key question: can A guarantee 150 exactly, or is it 149 due to integer constraints?

Let me think about a strategy for A that guarantees 150.

A's strategy: At each step, put $c = \lceil r / (22 - a - b) \rceil$ coins in the bag (or some appropriate integer choice).

Actually, let me think about this problem differently. 

The formula suggests the answer is 150. Let me verify this is achievable and that B can't do better (i.e., B can prevent A from getting more than 150).

Upper bound (B can prevent A from getting more than 150): B's strategy is to always give the bag to the person who minimizes A's expected gain. By the analysis, B can ensure A gets at most 150.

Lower bound (A can guarantee 150): A's strategy is to choose bag sizes that create equal dilemmas for B. 

But with integer constraints, can A guarantee exactly 150?

Let me think about a simpler approach. Consider A's strategy: always put exactly 1 coin in each bag. Then B allocates 21 bags (someone reaches 11). A gets some number of 1-coin bags, and the remainder (279 coins) goes to whoever didn't reach 11.

If B gives all bags to A: A gets 11 bags (11 coins), B gets 279 coins. A gets 11. Bad.
If B gives all bags to B: B gets 11 bags (11 coins), A gets 279 coins. A gets 279. But B won't do this.

B will balance: give just enough bags to A to reach 11 first, while keeping the valuable bags. With 1-coin bags, B gives 11 bags to A (A gets 11 coins, B gets 279). Or B takes 11 bags (B gets 11, A gets 279). B prefers the former. So A gets 11. Terrible.

So A needs to use larger bags to create dilemmas.

Let me think about the problem from the perspective of the continuous solution. At each state $(a, b, r)$, A puts $c^* = r / (22 - a - b)$ coins. B is indifferent between giving to A and giving to B.

In the discrete case, A puts $\lfloor c^* \rfloor$ or $\lceil c^* \rceil$ coins. The rounding error is at most 1 coin per step, and there are at most 21 steps. So the total error is at most 21 coins. But the errors might not all go against A.

Actually, I think the answer is 150. Let me think about why more carefully.

Consider the following strategy for A: at each state $(a, b, r)$, A puts $c = \lfloor r / (22 - a - b) \rfloor$ or $c = \lceil r / (22 - a - b) \rceil$ coins, choosing whichever gives a better guarantee.

The continuous value is $V = (11-a) r / (22 - a - b)$. With integer $c$, the discrete value is at least $V - 1$ (roughly), because the rounding error is at most 1 per step.

But actually, the errors compound. Let me think about this differently.

Hmm, let me try to think about whether the answer is exactly 150.

Actually, I think the key insight is that 300 is divisible by 22? No, $300 / 22 = 13.63...$. Not divisible.

But $300 = 22 \times 13 + 14$. Hmm.

Let me try a different approach. Let me think about what happens if A uses the strategy of always making the bag size such that B is exactly indifferent.

At state $(0, 0, 300)$: optimal $c = 300/22 \approx 13.6$. A chooses $c = 14$.
- If B gives to A: A gets 14, state becomes $(1, 0, 286)$. Continuous value: $10 \times 286 / 21 = 2860/21 \approx 136.19$. Total: $14 + 136.19 = 150.19$.
- If B gives to B: state becomes $(0, 1, 286)$. Continuous value: $11 \times 286 / 21 = 3146/21 \approx 149.81$.
B gives to B (A gets 149.81).

State $(0, 1, 286)$: optimal $c = 286/21 \approx 13.6$. A chooses $c = 14$.
- Give to A: $14 + 10 \times 272 / 20 = 14 + 136 = 150$.
- Give to B: $11 \times 272 / 20 = 11 \times 13.6 = 149.6$.
B gives to B (A gets 149.6).

Hmm, this is getting complicated. The continuous approximation gives 150 but the discrete version might give slightly less.

Let me try to think about this problem from a higher level. 

Actually, maybe I should think about it differently. Let me consider the problem where A pre-commits to all bag sizes (instead of adapting). This is a weaker strategy for A but might be easier to analyze.

If A pre-commits to bag sizes $c_1, c_2, \ldots, c_n$ (where $n \le 21$ and $\sum c_i \le 300$), then B allocates each bag to minimize A's total. B will give bags to A or B strategically.

Actually, the adaptive version is stronger for A. Let me think about the adaptive version.

Let me try to think about whether 150 is exactly achievable.

Consider the following: A's strategy is to always put $c$ coins where $c$ is chosen so that both options for B give A at least 150 total (including what A already has).

At the start, A has 0 coins, 0 bags. A needs to guarantee 150 more coins from 300 remaining.

A puts $c$ coins. 
- If B gives to A: A has $c$ coins, 1 bag, $300 - c$ remaining. A needs $150 - c$ more from $f(1, 0, 300-c)$.
- If B gives to B: A has 0 coins, 0 bags, $300 - c$ remaining. A needs 150 more from $f(0, 1, 300-c)$.

For A to guarantee 150: need $c + f(1, 0, 300-c) \ge 150$ AND $f(0, 1, 300-c) \ge 150$.

From the formula: $f(1, 0, r) = 10r/21$ and $f(0, 1, r) = 11r/21$.

$c + 10(300-c)/21 \ge 150 \Rightarrow 21c + 10(300-c) \ge 3150 \Rightarrow 21c + 3000 - 10c \ge 3150 \Rightarrow 11c \ge 150 \Rightarrow c \ge 150/11 \approx 13.6$.

$11(300-c)/21 \ge 150 \Rightarrow 11(300-c) \ge 3150 \Rightarrow 3300 - 11c \ge 3150 \Rightarrow 11c \le 150 \Rightarrow c \le 150/11 \approx 13.6$.

So $c = 150/11$, which is not an integer. $c = 14$ gives:
- $14 + 10 \times 286/21 = 14 + 2860/21 = 14 + 136.19 = 150.19 \ge 150$ ✓
- $11 \times 286/21 = 3146/21 = 149.81 < 150$ ✗

$c = 13$ gives:
- $13 + 10 \times 287/21 = 13 + 2870/21 = 13 + 136.67 = 149.67 < 150$ ✗

So with $c = 14$, the "give to B" branch gives 149.81 < 150. With $c = 13$, the "give to A" branch gives 149.67 < 150.

So A cannot guarantee 150 in the continuous relaxation either! Wait, but the formula says $f(0, 0, 300) = 150$. Let me recheck.

$f(0, 0, 300) = \max_c \min(c + f(1, 0, 300-c), f(0, 1, 300-c))$
$= \max_c \min(c + 10(300-c)/21, 11(300-c)/21)$

Setting equal: $c + 10(300-c)/21 = 11(300-c)/21$
$c = (300-c)/21$
$21c = 300 - c$
$22c = 300$
$c = 300/22 = 150/11$

Value: $11(300 - 150/11)/21 = 11 \cdot (3300 - 150)/(11 \cdot 21) = (3300 - 150)/21 = 3150/21 = 150$.

So the continuous value is exactly 150, achieved at $c = 150/11 \approx 13.636$.

But $c$ must be an integer. With $c = 14$: $\min(14 + 2860/21, 3146/21) = \min(150.19, 149.81) = 149.81$.
With $c = 13$: $\min(13 + 2870/21, 3157/21) = \min(149.67, 150.33) = 149.67$.

So the best is $c = 14$, giving $149.81$ in the continuous relaxation of the sub-problems. But the sub-problems also have integer constraints, so the actual value might be different.

This is getting very complex. Let me think about whether the answer is 150 or 149.

Actually, I realize the continuous formula gives a value of exactly 150, but the integer constraints might reduce it. The question is by how much.

Let me think about this more carefully. The formula $f(a, b, r) = (11-a)r/(22-a-b)$ is the continuous relaxation. The discrete version satisfies $f_{\text{disc}}(a, b, r) \le f_{\text{cont}}(a, b, r)$.

But also, $f_{\text{disc}}(a, b, r) \ge f_{\text{cont}}(a, b, r) - \epsilon$ for some small $\epsilon$ depending on the number of remaining steps.

The number of steps from $(0, 0)$ is at most 21. At each step, the rounding error is at most 1 (since we're rounding $c$ to the nearest integer). But the errors propagate.

Actually, let me think about this differently. Let me try to compute the exact discrete value for small cases and see if there's a pattern.

Let me compute $f(10, 10, r)$ exactly for small $r$:
$f(10, 10, r) = \max_c \min(c, r-c) = \lfloor r/2 \rfloor$.

$f(10, 9, r) = \max_c \min(c, \lfloor (r-c)/2 \rfloor)$.

For $r = 3$: $c=1: \min(1, 1) = 1$. $c=2: \min(2, 0) = 0$. So $f(10, 9, 3) = 1$. Continuous: $3/3 = 1$. ✓

For $r = 6$: $c=1: \min(1, 2) = 1$. $c=2: \min(2, 2) = 2$. $c=3: \min(3, 1) = 1$. So $f(10, 9, 6) = 2$. Continuous: $6/3 = 2$. ✓

For $r = 7$: $c=1: \min(1, 3) = 1$. $c=2: \min(2, 2) = 2$. $c=3: \min(3, 2) = 2$. So $f(10, 9, 7) = 2$. Continuous: $7/3 = 2.33$. So discrete is 2, continuous is 2.33. Loss of 0.33.

For $r = 300$ and 22 steps, the loss could accumulate. But let me think about whether the answer is 150 or something else.

Actually, let me reconsider. Maybe I should think about this problem differently.

Let me think about the problem as follows. The game has at most 21 rounds. In each round, A chooses a bag size, B allocates. The game ends when someone has 11 bags.

Let me think about the total coins A gets. A gets coins from bags assigned to A, plus any remaining coins if B reaches 11 first.

Key insight: the formula $f(a,b,r) = (11-a)r/(22-a-b)$ can be rewritten as:
$$f(a,b,r) = \frac{11-a}{(11-a)+(11-b)} \cdot r$$

This means A gets a fraction $\frac{11-a}{(11-a)+(11-b)}$ of the remaining coins. At the start, this is $11/22 = 1/2$.

The fraction represents A's "bargaining power" based on how many more bags each can receive before reaching 11.

Now, the question is whether the integer constraints change the answer from 150.

Let me think about it from a different angle. Consider the following strategy for A:

A divides the 300 coins into 22 groups as evenly as possible: 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14 — wait, $22 \times 14 = 308 > 300$. So $300 = 22 \times 13 + 14$, meaning 14 groups of 14 and 8 groups of 13. Or more precisely, 14 groups of 14 and 8 groups of 13: $14 \times 14 + 8 \times 13 = 196 + 104 = 300$. Yes.

But A doesn't pre-commit to all bags; A adapts. Let me think about whether A can guarantee 150.

Actually, let me think about the problem from B's perspective. B wants to minimize A's coins. B's optimal strategy in the continuous case is to always be indifferent. In the discrete case, B might be able to exploit rounding.

Let me try to think about upper and lower bounds.

Upper bound: A can get at most 150 (from continuous analysis, B can prevent more).
Lower bound: A can guarantee at least...?

For the lower bound, let me think about A's strategy. 

A's strategy: At each state $(a, b, r)$, A puts $c = \lceil r / (22 - a - b) \rceil$ coins in the bag (rounding up to ensure the "give to A" branch is strong enough).

Let me trace through the game with this strategy and see what A can guarantee.

Actually, this is getting very complex. Let me try a different approach.

Let me think about the problem as a "cutting" game. A is essentially cutting the pie (300 coins) into pieces, and B chooses who gets each piece. The constraint is the 11-bag limit.

This is similar to the "I cut, you choose" game but with multiple rounds and a stopping condition.

In the classic "I cut, you choose" with one round, A cuts the pie in half and gets 50%. With multiple rounds and the 11-bag constraint, the analysis is more complex.

Let me think about a cleaner approach. 

Claim: The answer is 150.

Proof sketch:
1. A can guarantee at least 150 by using a strategy that maintains the invariant that A's guaranteed share is at least half the remaining coins.
2. B can prevent A from getting more than 150 by using a symmetric strategy.

For part 1: A's strategy is to always put $c$ coins where $c$ is chosen so that both options for B give A at least half the remaining coins (accounting for what A already has and the bag count dynamics).

Hmm, but the continuous analysis shows that the exact optimal $c = 150/11$ is not an integer, so A can't perfectly balance.

Let me think about this more carefully.

Actually, let me reconsider. The formula gives $f(0,0,300) = 150$ in the continuous case. In the discrete case, the value is $\lfloor 150 \rfloor = 150$ if the rounding works out, or 149 if it doesn't.

Let me try to compute the exact discrete value by working backwards from the end, but only tracking the "loss" from the continuous value.

Define $g(a, b, r) = f_{\text{disc}}(a, b, r) - f_{\text{cont}}(a, b, r) \le 0$. This is the loss from integer constraints.

At the base case, $g(a, b, 0) = 0$.

The recurrence for $f_{\text{disc}}$ involves choosing integer $c$, while $f_{\text{cont}}$ uses real $c^*$. The loss at each step depends on how far $c$ is from $c^*$ and how the loss propagates.

This is hard to analyze in general. Let me try a different approach.

Let me think about the problem from the perspective of the answer being a nice number. The continuous answer is 150. The problem likely has answer 150.

Let me try to construct an explicit strategy for A that guarantees 150, and a strategy for B that prevents A from getting more than 150.

B's strategy (upper bound): B always gives the bag to the person who results in A getting fewer coins. By the continuous analysis, this limits A to 150. But with integer constraints, B might be able to limit A to 149.

Hmm, let me think about this differently.

Actually, let me reconsider the problem. Maybe the answer isn't 150. Let me re-examine the formula.

The formula $f(a, b, r) = (11-a)r/(22-a-b)$ assumes the game always ends with someone reaching 11 bags. But what if A can end the game early by putting all remaining coins in one bag?

If A puts all $r$ coins in one bag, the game gives out 1 bag and 0 coins remain. The game ends with all coins distributed. A gets either $r$ (if B gives to A) or 0 (if B gives to B). B will give to B, so A gets 0. So putting all coins in one bag is terrible for A.

What if A puts $r-1$ coins in one bag? Then 1 coin remains. B gives the big bag to B, and then A puts 1 coin in a bag, B gives it to A or B. This is also bad for A.

So A wants to spread coins across many bags. The 11-bag limit is the binding constraint.

OK let me try to think about this more carefully with the exact DP, but using the structure of the formula.

The formula says $f(a, b, r) = (11-a)r/(22-a-b)$, and the optimal $c = r/(22-a-b)$.

At each step, the remaining coins $r$ is divided by $(22-a-b)$, which decreases by 1 each step. So after $k$ steps, the denominator is $22-k$.

The optimal $c$ at step $k$ (0-indexed) is $r_k / (22-k)$ where $r_k$ is the remaining coins.

$r_0 = 300$, $c_0 = 300/22 \approx 13.6$.
$r_1 = 300 - c_0 \approx 286.4$, $c_1 = 286.4/21 \approx 13.6$.
...

In the continuous case, $r_k = 300 \cdot (22-k-1)/(22-1) \cdot ... $ hmm, this isn't quite right because $r$ depends on which branch B takes.

Actually, in the continuous case, B is indifferent at each step, so the value is the same regardless of B's choice. The remaining coins after step $k$ is $r_k = r_{k-1} - c_{k-1} = r_{k-1} - r_{k-1}/(22-k+1) = r_{k-1} \cdot (21-k)/(22-k)$.

So $r_k = 300 \cdot \prod_{j=0}^{k-1} (21-j)/(22-j) = 300 \cdot \prod_{j=0}^{k-1} (22-j-1)/(22-j) = 300 \cdot (22-k-1)! \cdot 21! / (21! \cdot (22-1)!) $... 

Hmm, let me just compute: $r_k = 300 \cdot \frac{21}{22} \cdot \frac{20}{21} \cdot \frac{19}{20} \cdots \frac{22-k-1}{22-k} = 300 \cdot \frac{22-k-1}{22} = 300 \cdot \frac{21-k}{22}$.

So $r_k = 300(21-k)/22$ and $c_k = r_k/(22-k) = 300(21-k)/(22(22-k))$.

At $k=0$: $c_0 = 300 \cdot 21 / (22 \cdot 22) = 6300/484 = 13.02$. Wait, that doesn't match. Let me recompute.

$c_0 = r_0 / (22 - 0) = 300/22 \approx 13.636$.
$r_1 = r_0 - c_0 = 300 - 300/22 = 300 \cdot 21/22 \approx 286.36$.
$c_1 = r_1 / (22 - 1) = 300 \cdot 21/(22 \cdot 21) = 300/22 \approx 13.636$.

Oh interesting, $c_k = 300/22$ for all $k$! Because $c_k = r_k / (22-k) = [300(21-k)/22] / (22-k) = 300(21-k) / [22(22-k)]$.

Hmm, that's not $300/22$. Let me recompute.

$r_0 = 300$, $c_0 = 300/22$.
$r_1 = 300 - 300/22 = 300 \cdot 21/22$.
$c_1 = r_1/21 = 300 \cdot 21/(22 \cdot 21) = 300/22$.
$r_2 = r_1 - c_1 = 300 \cdot 21/22 - 300/22 = 300 \cdot 20/22$.
$c_2 = r_2/20 = 300 \cdot 20/(22 \cdot 20) = 300/22$.

Yes! $c_k = 300/22$ for all $k$. The optimal bag size is constant at $300/22 \approx 13.636$.

This makes sense: in the continuous equilibrium, A puts the same number of coins in each bag, and the game lasts 21 rounds (someone reaches 11 bags), with each bag having $300/22$ coins (wait, 21 bags, but $300/22 \cdot 21 = 6300/22 = 286.36$, not 300. The remaining $300 - 286.36 = 13.64 = 300/22$ goes to the person who didn't reach 11).

Actually, 21 bags are given out, each with $300/22$ coins, totaling $21 \cdot 300/22 = 6300/22 \approx 286.36$. The remaining $300 - 286.36 = 13.64 = 300/22$ coins go to the person who didn't reach 11 bags.

A gets 11 bags (if A reaches 11 first): $11 \cdot 300/22 = 150$. B gets 10 bags + remainder: $10 \cdot 300/22 + 300/22 = 11 \cdot 300/22 = 150$. So both get 150.

Or B gets 11 bags: B gets $11 \cdot 300/22 = 150$, A gets 10 bags + remainder = 150.

So in the continuous equilibrium, both get 150 regardless of who reaches 11 first. That's the beauty of the constant bag size.

Now, in the discrete case, A wants to put $300/22 \approx 13.636$ coins per bag. Since this must be an integer, A puts either 13 or 14 coins per bag.

If A always puts 14 coins: 21 bags use $21 \times 14 = 294$ coins, 6 remain. 
- If A reaches 11 first: A gets $11 \times 14 = 154$, B gets $10 \times 14 + 6 = 146$.
- If B reaches 11 first: B gets $11 \times 14 = 154$, A gets $10 \times 14 + 6 = 146$.
B will try to make A reach 11 first (so B gets 146 instead of 154). Wait, B wants to maximize B's coins. If A reaches 11 first, B gets 146. If B reaches 11 first, B gets 154. So B prefers B reaching 11 first. But B also controls allocation...

Wait, I need to think about this more carefully. If A always puts 14 coins per bag, B allocates each bag. B wants to maximize B's total.

If B gives all bags to A: A gets 11 bags (154 coins), B gets 6 remaining. B total = 6.
If B gives all bags to B: B gets 11 bags (154 coins), A gets 6 remaining. B total = 154.
If B gives 10 to A, 11 to B: B gets 11 bags (154), A gets 10 bags (140) + 6 = 146. B total = 154.
If B gives 11 to A, 10 to B: A gets 11 bags (154), B gets 10 bags (140) + 6 = 146. B total = 146.

So B's best is to take 11 bags (give 10 to A), getting 154. A gets 146.

But wait, B doesn't have to give exactly 10 to A and 11 to B. B can adapt. The key is: B wants to reach 11 bags for B before A reaches 11. Since B controls allocation, B can always ensure B gets 11 bags before A (by taking bags). But then A gets the remainder.

Hmm, but if B takes all bags, B reaches 11 first, A gets the remainder (6). A gets 6. That's terrible for A.

Wait, no. If B takes all 21 bags... but the game ends when someone reaches 11. So after B takes 11 bags, the game ends, A gets the remainder. B has 11 bags with $11 \times 14 = 154$ coins, A gets $300 - 154 = 146$ coins.

But B could also give some bags to A. If B gives $k$ bags to A and takes $11-k$ bags (B reaches 11 first since B takes the 11th bag), then:
- A has $k$ bags with $14k$ coins, plus remainder $300 - 14 \cdot 11 = 300 - 154 = 146$.
- A total = $14k + 146$.
- B has 11 bags with $154$ coins.
- B total = 154.

Wait, that's not right either. If B gives $k$ bags to A and takes $11$ bags (B reaches 11), then $k + 11$ bags are given out, using $14(k+11)$ coins. But $k + 11 \le 21$ (since A can have at most 10 bags before the game ends). So $k \le 10$.

Remainder = $300 - 14(k + 11) = 300 - 14k - 154 = 146 - 14k$.
A total = $14k + (146 - 14k) = 146$.
B total = $154$.

Interesting! Regardless of how B allocates (as long as B reaches 11 first), A gets 146 and B gets 154.

But what if A reaches 11 first? B gives 11 bags to A and takes $k$ bags ($k \le 10$). Then:
- A has 11 bags with $154$ coins. Game ends, B gets remainder.
- Remainder = $300 - 14(11 + k) = 146 - 14k$.
- B total = $14k + 146 - 14k = 146$.
- A total = 154.

So if A reaches 11 first, A gets 154 and B gets 146.
If B reaches 11 first, A gets 146 and B gets 154.

B wants to maximize B's total, so B prefers B reaching 11 first (154 vs 146). B can ensure B reaches 11 first by taking bags (B controls allocation). So B takes 11 bags, A gets 146.

So with constant bag size 14, A gets 146. That's less than 150.

What if A always puts 13 coins per bag? 21 bags use $21 \times 13 = 273$ coins, 27 remain.
- If B reaches 11 first: B gets $11 \times 13 = 143$, A gets $10 \times 13 + 27 = 157$.
- If A reaches 11 first: A gets $11 \times 13 = 143$, B gets $10 \times 13 + 27 = 157$.

B wants to maximize B's total. If B reaches 11 first, B gets 143. If A reaches 11 first, B gets 157. So B prefers A reaching 11 first! B gives all bags to A.

If B gives all bags to A: A reaches 11 first, A gets 143, B gets 157. A gets 143.

So with constant bag size 13, A gets 143. Worse than 146.

What if A mixes bag sizes? A can adapt bag sizes based on the current state.

The key insight: with constant bag size $c$, if $21c < 300$ (remainder $> 0$):
- If B reaches 11 first: A gets $10c + (300 - 21c) = 300 - 11c$, B gets $11c$.
- If A reaches 11 first: A gets $11c$, B gets $10c + (300 - 21c) = 300 - 11c$.
B chooses the option where B gets more: B prefers B reaching 11 first if $11c > 300 - 11c$, i.e., $22c > 300$, i.e., $c > 300/22 \approx 13.6$. B prefers A reaching 11 first if $c < 300/22$.

If $c > 300/22$: B takes 11 bags, A gets $300 - 11c$.
If $c < 300/22$: B gives 11 bags to A, A gets $11c$.
If $c = 300/22$: both options give A $150$.

With $c = 14 > 300/22$: A gets $300 - 154 = 146$.
With $c = 13 < 300/22$: A gets $11 \times 13 = 143$.

So constant bag size gives at most 146. But A can do better by adapting!

The continuous optimal strategy has A putting $300/22$ coins per bag, which is between 13 and 14. A can mix: some bags with 13, some with 14, to effectively get $300/22$ per bag.

If A uses 14 bags of 14 coins and 7 bags of 13 coins: total = $14 \times 14 + 7 \times 13 = 196 + 91 = 287$. Remainder = 13. Total bags = 21.

But A needs to be strategic about which bags are 13 and which are 14, and B adapts too.

Actually, A doesn't pre-commit. A adapts based on the current state. Let me think about the adaptive strategy.

The continuous optimal is $c^* = r/(22-a-b)$ at each state. A should put $\lfloor c^* \rfloor$ or $\lceil c^* \rceil$ coins, choosing to balance the two branches.

Let me think about this more carefully. At state $(a, b, r)$, the continuous optimal is $c^* = r/(22-a-b)$. A puts $c = \lfloor c^* \rfloor$ or $c = \lceil c^* \rceil$.

The continuous value is $V = (11-a)r/(22-a-b)$.

With $c = \lfloor c^* \rfloor$: 
- Give to A: $\lfloor c^* \rfloor + V(a+1, b, r - \lfloor c^* \rfloor)$
- Give to B: $V(a, b+1, r - \lfloor c^* \rfloor)$

With $c = \lceil c^* \rceil$:
- Give to A: $\lceil c^* \rceil + V(a+1, b, r - \lceil c^* \rceil)$
- Give to B: $V(a, b+1, r - \lceil c^* \rceil)$

A chooses the $c$ that maximizes the minimum.

The loss from integer constraints is at most 1 per step (the difference between $c^*$ and the nearest integer). Over 21 steps, the total loss is at most 21. But the losses might partially cancel.

Actually, I think the answer might be 150. Let me think about why.

Consider A's strategy: A maintains a "target" for each bag. At state $(a, b, r)$, the target is $r/(22-a-b)$. A puts $\lfloor r/(22-a-b) \rfloor$ or $\lceil r/(22-a-b) \rceil$ coins, choosing to maximize the minimum of the two branches.

The key observation is that the continuous value $V = (11-a)r/(22-a-b)$ is always a rational number with denominator dividing $22-a-b$. If $r$ is divisible by $22-a-b$, then $c^*$ is an integer and there's no loss. If not, the loss is at most 1 per step.

But the losses compound. Let me think about whether the total loss can be 0.

Actually, let me think about this problem from a completely different angle.

Consider the following strategy for A: A puts coins in bags such that the total coins in any 11 bags assigned to one person is at most 150, and the total coins in any 10 bags plus the remainder is at least 150.

Hmm, this is vague. Let me think more concretely.

Let me consider the problem as a whole. A wants to guarantee 150. B wants to prevent this.

A's strategy: Divide 300 coins into 22 "shares" of $300/22$ each (in some discrete approximation). Each bag corresponds to one share. The 22nd share is the remainder. A puts coins in bags one at a time, each bag being one share. B allocates. After 21 bags (11 to one person), the 22nd share goes to the other person.

If A can ensure each share is exactly $300/22$, then regardless of allocation, A gets 11 shares = 150. But $300/22$ is not an integer.

So A needs to use integer shares. The question is whether A can arrange integer shares such that any 11 of them sum to at least 150.

If A uses 14 shares of 14 and 8 shares of 13: $14 \times 14 + 8 \times 13 = 196 + 104 = 300$. Total 22 shares.

The worst case for A is B gives A the 11 smallest shares. The 11 smallest are all 13s (8 of them) and 3 of the 14s: $8 \times 13 + 3 \times 14 = 104 + 42 = 146$. So A gets 146 in the worst case.

But A doesn't have to pre-commit to all shares. A can adapt!

The key difference between adaptive and non-adaptive: A can observe B's allocations and adjust bag sizes accordingly.

Let me think about the adaptive strategy more carefully.

At state $(a, b, r)$, A wants to guarantee $V = (11-a)r/(22-a-b)$ more coins. A puts $c$ coins. The two branches give:
- Give to A: $c + V(a+1, b, r-c) = c + (10-a)(r-c)/(21-a-b)$... wait, let me use the formula. $V(a+1, b, r-c) = (11-a-1)(r-c)/(22-a-1-b) = (10-a)(r-c)/(21-a-b)$.
- Give to B: $V(a, b+1, r-c) = (11-a)(r-c)/(22-a-b-1) = (11-a)(r-c)/(21-a-b)$.

Setting equal: $c + (10-a)(r-c)/(21-a-b) = (11-a)(r-c)/(21-a-b)$.
$c = (r-c)/(21-a-b)$.
$c(21-a-b) = r - c$.
$c(22-a-b) = r$.
$c = r/(22-a-b)$.

So the continuous optimal is $c = r/(22-a-b)$, and the value is $V = (11-a)r/(22-a-b)$.

Now, in the discrete case, A chooses $c = \lfloor r/(22-a-b) \rfloor$ or $\lceil r/(22-a-b) \rceil$.

Let me define $d = 22 - a - b$ (the "denominator"). Then $c^* = r/d$ and $V = (11-a)r/d$.

Let $r = qd + s$ where $0 \le s < d$. Then $c^* = q + s/d$.

Option 1: $c = q$ (floor).
- Give to A: $q + (10-a)(r-q)/(d-1) = q + (10-a)(qd+s-q)/(d-1) = q + (10-a)(q(d-1)+s)/(d-1) = q + (10-a)q + (10-a)s/(d-1) = q(11-a) + (10-a)s/(d-1)$.
- Give to B: $(11-a)(r-q)/(d-1) = (11-a)(q(d-1)+s)/(d-1) = (11-a)q + (11-a)s/(d-1)$.
B minimizes: $\min(q(11-a) + (10-a)s/(d-1), (11-a)q + (11-a)s/(d-1))$.
$= (11-a)q + \min((10-a)s/(d-1), (11-a)s/(d-1))$
$= (11-a)q + (10-a)s/(d-1)$ (since $10-a < 11-a$).

Option 2: $c = q+1$ (ceil).
- Give to A: $(q+1) + (10-a)(r-q-1)/(d-1) = (q+1) + (10-a)(qd+s-q-1)/(d-1) = (q+1) + (10-a)(q(d-1)+s-1)/(d-1) = (q+1) + (10-a)q + (10-a)(s-1)/(d-1) = (11-a)q + 1 + (10-a)(s-1)/(d-1)$.
- Give to B: $(11-a)(r-q-1)/(d-1) = (11-a)(q(d-1)+s-1)/(d-1) = (11-a)q + (11-a)(s-1)/(d-1)$.
B minimizes: $(11-a)q + \min(1 + (10-a)(s-1)/(d-1), (11-a)(s-1)/(d-1))$.

If $s = 0$: $c^* = q$ is an integer. No loss. Value = $(11-a)q = (11-a)r/d = V$. ✓

If $s > 0$:
Option 1 value: $(11-a)q + (10-a)s/(d-1)$.
Option 2 value: $(11-a)q + \min(1 + (10-a)(s-1)/(d-1), (11-a)(s-1)/(d-1))$.

Continuous value: $V = (11-a)r/d = (11-a)(qd+s)/d = (11-a)q + (11-a)s/d$.

Loss from option 1: $V - \text{option 1} = (11-a)s/d - (10-a)s/(d-1) = s[(11-a)(d-1) - (10-a)d]/[d(d-1)]$.
$= s[(11-a)(d-1) - (10-a)d] / [d(d-1)]$
$= s[(11-a)d - (11-a) - (10-a)d] / [d(d-1)]$
$= s[d - (11-a)] / [d(d-1)]$
$= s[d - 11 + a] / [d(d-1)]$
$= s[(22-a-b) - 11 + a] / [d(d-1)]$
$= s[11 - b] / [d(d-1)]$.

So loss from option 1 = $s(11-b)/[d(d-1)]$.

For option 2, let me compute. We need to compare $1 + (10-a)(s-1)/(d-1)$ and $(11-a)(s-1)/(d-1)$.

$1 + (10-a)(s-1)/(d-1) - (11-a)(s-1)/(d-1) = 1 - (s-1)/(d-1) = (d-1-s+1)/(d-1) = (d-s)/(d-1)$.

Since $s < d$, $d - s > 0$, so $1 + (10-a)(s-1)/(d-1) > (11-a)(s-1)/(d-1)$.

So B chooses the "give to B" branch: option 2 value = $(11-a)q + (11-a)(s-1)/(d-1)$.

Loss from option 2: $V - \text{option 2} = (11-a)s/d - (11-a)(s-1)/(d-1) = (11-a)[s/d - (s-1)/(d-1)] = (11-a)[s(d-1) - d(s-1)]/[d(d-1)] = (11-a)[sd - s - ds + d]/[d(d-1)] = (11-a)(d-s)/[d(d-1)]$.

So:
- Loss from option 1 (floor): $s(11-b)/[d(d-1)]$
- Loss from option 2 (ceil): $(11-a)(d-s)/[d(d-1)]$

A chooses the option with smaller loss:
$\min(s(11-b), (11-a)(d-s)) / [d(d-1)]$.

The total loss over the entire game is the sum of these losses at each step. But the losses at later steps depend on the state, which depends on B's choices.

This is getting very involved. Let me try to compute the total loss for the specific case $r = 300$, starting from $(0, 0)$.

At the start: $a=0, b=0, d=22, r=300$. $q = 13, s = 300 - 13 \times 22 = 300 - 286 = 14$.
- Loss from floor: $14 \times 11 / (22 \times 21) = 154 / 462 = 7/21 = 1/3$.
- Loss from ceil: $11 \times (22-14) / (22 \times 21) = 11 \times 8 / 462 = 88/462 = 4/21$.
A chooses floor (loss 1/3 < 4/21). So A puts $c = 13$.

But wait, the loss is $1/3$, which means the discrete value is $150 - 1/3 = 149.67$. That's not an integer, and the actual discrete value is an integer.

Hmm, I think the issue is that the losses at subsequent steps also involve fractional values, and the total might work out to an integer.

This is getting extremely complex. Let me try a different approach: just compute the DP numerically.

Actually, I can't run code. Let me think about this problem from a higher level.

The continuous value is 150. The discrete value is at most 150. The question is whether it's 150 or less.

Key insight: the problem asks for the maximum number of coins A can guarantee. This is a specific integer. The continuous analysis gives 150. The discrete analysis might give 150 or 149.

Let me think about whether A can guarantee 150.

A's strategy to guarantee 150: A needs to ensure that regardless of B's choices, A gets at least 150.

Consider the following strategy for A: A always puts $c$ coins where $c$ is chosen to maintain the invariant that A's guaranteed coins from this point is at least $\lfloor (11-a)r/(22-a-b) \rfloor$.

Hmm, this is circular. Let me think differently.

Let me consider a specific strategy for A and check if it guarantees 150.

Strategy: A divides the game into 22 "rounds" (21 bags + 1 remainder). A wants each round to be worth $300/22 \approx 13.636$ coins. A uses a mix of 13 and 14 coin bags.

Specifically, A needs 14 bags of 14 coins and 8 bags of 13 coins (total $196 + 104 = 300$). But the order matters, and A adapts.

The question is: can A arrange the bags (adaptively) so that regardless of B's allocation, A gets at least 150?

If A gets 11 bags: A's coins = sum of A's 11 bags. A wants this to be $\ge 150$.
If B gets 11 bags: A's coins = sum of A's 10 bags + remainder. A wants this to be $\ge 150$.

In the first case (A gets 11 bags), B chooses which 11 bags A gets (by allocating). B will give A the 11 smallest bags. So A needs the 11th smallest bag to be large enough that the sum of the 11 smallest is $\ge 150$.

With 14 bags of 14 and 8 bags of 13: the 11 smallest are 8 bags of 13 and 3 bags of 14 = $104 + 42 = 146 < 150$. Not enough.

In the second case (B gets 11 bags), B chooses which 11 bags B gets. B will take the 11 largest bags. A gets the 10 smallest bags + remainder. The 10 smallest are 8 bags of 13 and 2 bags of 14 = $104 + 28 = 132$. Remainder = $300 - 21 \times \text{avg bag}$. But the bags aren't all the same size, so the remainder depends on which 21 bags are given out.

This is getting complicated. The non-adaptive approach gives at most 146 (as we computed). The adaptive approach should do better.

Let me think about the adaptive approach more carefully.

In the adaptive approach, A observes the current state $(a, b, r)$ and chooses the bag size accordingly. The key advantage is that A can adjust based on who has how many bags.

For example, if B has been taking many bags (B has more bags), A can make the bags larger (since B is closer to 11, B will be more reluctant to take bags). Conversely, if A has many bags, A should make bags smaller.

The continuous optimal strategy does exactly this: $c = r/(22-a-b)$, which adjusts based on the state.

Let me try to trace through a specific game path and see what A gets.

Path 1: B always gives bags to B (B takes all bags).
- State (0,0,300): A puts $c = 13$ (floor of 300/22). B takes it. State (0,1,287).
- State (0,1,287): $d = 21$, $c^* = 287/21 = 13.67$. A puts $c = 14$ (ceil). B takes. State (0,2,273).
  Wait, let me be more careful. A should choose the $c$ that maximizes the minimum. Let me use the loss formulas.

At (0,0,300): $d=22, r=300, q=13, s=14$.
- Floor loss: $14 \times 11 / (22 \times 21) = 154/462 = 1/3 \approx 0.333$.
- Ceil loss: $11 \times 8 / (22 \times 21) = 88/462 = 4/21 \approx 0.190$.
A chooses ceil ($c = 14$, loss $\approx 0.190$).

Wait, I made an error earlier. Let me recompute.

Loss from floor: $s(11-b)/[d(d-1)] = 14 \times 11 / (22 \times 21) = 154/462 = 1/3 \approx 0.333$.
Loss from ceil: $(11-a)(d-s)/[d(d-1)] = 11 \times 8 / (22 \times 21) = 88/462 = 4/21 \approx 0.190$.

A chooses ceil ($c = 14$), loss $\approx 0.190$. Value $\approx 150 - 0.190 = 149.81$.

B takes the bag (give to B branch). State becomes (0, 1, 286).

At (0,1,286): $d=21, r=286, q=13, s=286-13\times21=286-273=13$.
- Floor loss: $13 \times 10 / (21 \times 20) = 130/420 = 13/42 \approx 0.310$.
- Ceil loss: $11 \times 8 / (21 \times 20) = 88/420 = 22/105 \approx 0.210$.
A chooses ceil ($c = 14$), loss $\approx 0.210$. Value $\approx 11 \times 286/21 - 0.210 = 3146/21 - 0.210 = 149.81 - 0.210 = 149.60$.

Hmm wait, the value at (0,1,286) in continuous is $11 \times 286/21 = 3146/21 \approx 149.81$. With loss 0.210, discrete value $\approx 149.60$.

B takes. State (0, 2, 272).

At (0,2,272): $d=20, r=272, q=13, s=272-260=12$.
- Floor loss: $12 \times 9 / (20 \times 19) = 108/380 = 27/95 \approx 0.284$.
- Ceil loss: $11 \times 8 / (20 \times 19) = 88/380 = 22/95 \approx 0.232$.
A chooses ceil ($c = 14$), loss $\approx 0.232$.

B takes. State (0, 3, 258).

I see a pattern: B keeps taking, and A keeps putting 14 (ceil). Let me see how long this continues.

At (0, b, r): $d = 22-b$, $r = 300 - 14b$ (if A always puts 14 and B always takes).
$q = \lfloor r/d \rfloor$, $s = r \mod d$.

$b=0$: $r=300, d=22, q=13, s=14$. Ceil loss: $11 \times 8/462 = 0.190$.
$b=1$: $r=286, d=21, q=13, s=13$. Ceil loss: $11 \times 8/420 = 0.210$.
$b=2$: $r=272, d=20, q=13, s=12$. Ceil loss: $11 \times 8/380 = 0.232$.
$b=3$: $r=258, d=19, q=13, s=11$. Ceil loss: $11 \times 8/342 = 0.257$.
$b=4$: $r=244, d=18, q=13, s=10$. Ceil loss: $11 \times 8/306 = 0.288$.
$b=5$: $r=230, d=17, q=13, s=9$. Ceil loss: $11 \times 8/272 = 0.324$.
$b=6$: $r=216, d=16, q=13, s=8$. Ceil loss: $11 \times 8/240 = 0.367$.
$b=7$: $r=202, d=15, q=13, s=7$. Ceil loss: $11 \times 8/210 = 0.419$.
$b=8$: $r=188, d=14, q=13, s=6$. Ceil loss: $11 \times 8/182 = 0.484$.
$b=9$: $r=174, d=13, q=13, s=5$. Ceil loss: $11 \times 8/156 = 0.564$.

Wait, at $b=9$: $r=174, d=13, q=13, s=5$. $c^* = 174/13 = 13.38$. Ceil = 14.
Ceil loss: $(11-0)(13-5)/(13 \times 12) = 11 \times 8/156 = 88/156 = 0.564$.
Floor loss: $5 \times (11-9)/(13 \times 12) = 5 \times 2/156 = 10/156 = 0.064$.

Oh wait, floor loss is much smaller here! $s(11-b) = 5 \times 2 = 10$, vs ceil loss $11 \times 8 = 88$. So A should choose floor ($c = 13$) here.

Let me recompute. At $b=9$: $a=0, b=9, d=13, r=174, q=13, s=5$.
- Floor loss: $s(11-b)/[d(d-1)] = 5 \times 2 / (13 \times 12) = 10/156 = 0.064$.
- Ceil loss: $(11-a)(d-s)/[d(d-1)] = 11 \times 8 / (13 \times 12) = 88/156 = 0.564$.
A chooses floor ($c = 13$), loss $= 0.064$.

So at $b=9$, A switches to putting 13 coins. B takes. State (0, 10, 161).

At (0, 10, 161): $d=12, r=161, q=13, s=161-156=5$.
- Floor loss: $5 \times 1 / (12 \times 11) = 5/132 = 0.038$.
- Ceil loss: $11 \times 7 / (12 \times 11) = 77/132 = 0.583$.
A chooses floor ($c = 13$), loss $= 0.038$.

Now $b = 10$. If B takes this bag, B reaches 11, game ends, A gets remainder $= 161 - 13 = 148$.
If B gives to A: A gets 13, state (1, 10, 148). 

B minimizes A's gain:
- Give to A: $13 + f(1, 10, 148)$. Continuous: $13 + 10 \times 148/11 = 13 + 134.55 = 147.55$.
- Give to B: A gets $161 - 13 = 148$.
B gives to A (147.55 < 148).

So B gives to A. State (1, 10, 148).

At (1, 10, 148): $d = 11, r = 148, q = 13, s = 148 - 143 = 5$.
- Floor loss: $5 \times 1 / (11 \times 10) = 5/110 = 0.045$.
- Ceil loss: $10 \times 6 / (11 \times 10) = 60/110 = 0.545$.
A chooses floor ($c = 13$), loss $= 0.045$.

If B takes: B reaches 11, A gets $148 - 13 = 135$.
If B gives to A: $13 + f(2, 10, 135)$. Continuous: $13 + 9 \times 135/10 = 13 + 121.5 = 134.5$.
B gives to A (134.5 < 135).

State (2, 10, 135).

At (2, 10, 135): $d = 10, r = 135, q = 13, s = 5$.
- Floor loss: $5 \times 1 / (10 \times 9) = 5/90 = 0.056$.
- Ceil loss: $9 \times 5 / (10 \times 9) = 45/90 = 0.5$.
A chooses floor ($c = 13$), loss $= 0.056$.

If B takes: B reaches 11, A gets $135 - 13 = 122$.
If B gives to A: $13 + f(3, 10, 122)$. Continuous: $13 + 8 \times 122/9 = 13 + 108.44 = 121.44$.
B gives to A (121.44 < 122).

State (3, 10, 122).

At (3, 10, 122): $d = 9, r = 122, q = 13, s = 122 - 117 = 5$.
- Floor loss: $5 \times 1 / (9 \times 8) = 5/72 = 0.069$.
- Ceil loss: $8 \times 4 / (9 \times 8) = 32/72 = 0.444$.
A chooses floor ($c = 13$), loss $= 0.069$.

If B takes: A gets $122 - 13 = 109$.
If B gives to A: $13 + f(4, 10, 109)$. Continuous: $13 + 7 \times 109/8 = 13 + 95.375 = 108.375$.
B gives to A.

State (4, 10, 109).

At (4, 10, 109): $d = 8, r = 109, q = 13, s = 109 - 104 = 5$.
- Floor loss: $5 \times 1 / (8 \times 7) = 5/56 = 0.089$.
- Ceil loss: $7 \times 3 / (8 \times 7) = 21/56 = 0.375$.
A chooses floor ($c = 13$), loss $= 0.089$.

If B takes: A gets $109 - 13 = 96$.
If B gives to A: $13 + f(5, 10, 96)$. Continuous: $13 + 6 \times 96/7 = 13 + 82.286 = 95.286$.
B gives to A.

State (5, 10, 96).

At (5, 10, 96): $d = 7, r = 96, q = 13, s = 96 - 91 = 5$.
- Floor loss: $5 \times 1 / (7 \times 6) = 5/42 = 0.119$.
- Ceil loss: $6 \times 2 / (7 \times 6) = 12/42 = 0.286$.
A chooses floor ($c = 13$), loss $= 0.119$.

If B takes: A gets $96 - 13 = 83$.
If B gives to A: $13 + f(6, 10, 83)$. Continuous: $13 + 5 \times 83/6 = 13 + 69.167 = 82.167$.
B gives to A.

State (6, 10, 83).

At (6, 10, 83): $d = 6, r = 83, q = 13, s = 83 - 78 = 5$.
- Floor loss: $5 \times 1 / (6 \times 5) = 5/30 = 0.167$.
- Ceil loss: $5 \times 1 / (6 \times 5) = 5/30 = 0.167$.
Equal! A can choose either. Let's say floor ($c = 13$), loss $= 0.167$.

If B takes: A gets $83 - 13 = 70$.
If B gives to A: $13 + f(7, 10, 70)$. Continuous: $13 + 4 \times 70/5 = 13 + 56 = 69$.
B gives to A (69 < 70).

State (7, 10, 70).

At (7, 10, 70): $d = 5, r = 70, q = 14, s = 0$. No loss! $c = 14$.

If B takes: A gets $70 - 14 = 56$.
If B gives to A: $14 + f(8, 10, 56)$. Continuous: $14 + 3 \times 56/4 = 14 + 42 = 56$.
B is indifferent. Both give A 56.

Let's say B gives to A. State (8, 10, 56).

At (8, 10, 56): $d = 4, r = 56, q = 14, s = 0$. No loss! $c = 14$.

If B takes: A gets $56 - 14 = 42$.
If B gives to A: $14 + f(9, 10, 42)$. Continuous: $14 + 2 \times 42/3 = 14 + 28 = 42$.
B is indifferent. Both give A 42.

State (9, 10, 42).

At (9, 10, 42): $d = 3, r = 42, q = 14, s = 0$. No loss! $c = 14$.

If B takes: A gets $42 - 14 = 28$.
If B gives to A: $14 + f(10, 10, 28)$. $f(10, 10, 28) = \lfloor 28/2 \rfloor = 14$. So $14 + 14 = 28$.
B is indifferent. Both give A 28.

State (10, 10, 28).

At (10, 10, 28): $f = \lfloor 28/2 \rfloor = 14$. A puts $c = 14$.
- Give to A: A gets 14, game ends.
- Give to B: A gets $28 - 14 = 14$.
A gets 14.

So along this path, A gets $14 + 14 + 14 + 14 + 14 + 14 + 14 + 14 + 14 + 13 + 13 + 13 + 13 + 13 + 13 + 13 + 14 + 14 + 14 + 14 + 14$... 

Wait, I need to track A's accumulated coins. Let me retrace.

Path: B takes 9 bags, then gives 10 bags to A (with B at 10 bags), then the last bag.

Actually, let me retrace more carefully.

B takes bags for $b = 0, 1, ..., 9$ (10 bags taken by B). A puts 14 for $b = 0,...,8$ and 13 for $b = 9$.
Coins used: $9 \times 14 + 1 \times 13 = 126 + 13 = 139$. Remaining: $300 - 139 = 161$.
A has 0 coins, 0 bags. B has 0 coins, 10 bags.

Then at (0, 10, 161): A puts 13. B gives to A. A gets 13, 1 bag. State (1, 10, 148).
At (1, 10, 148): A puts 13. B gives to A. A gets 13, 2 bags. State (2, 10, 135).
...
This continues. A puts 13 each time, B gives to A.

At (a, 10, r): A puts 13. 
- Give to A: A gets 13, state (a+1, 10, r-13).
- Give to B: B reaches 11, A gets r - 13.

B gives to A as long as $13 + f(a+1, 10, r-13) < r - 13$, i.e., $f(a+1, 10, r-13) < r - 26$.

From the continuous formula: $f(a+1, 10, r-13) = (10-a)(r-13)/(11-a)$. 
We need $(10-a)(r-13)/(11-a) < r - 26$.
$(10-a)(r-13) < (11-a)(r-26)$.
$(10-a)r - 13(10-a) < (11-a)r - 26(11-a)$.
$r[(10-a) - (11-a)] < 13(10-a) - 26(11-a)$.
$-r < 130 - 13a - 286 + 26a$.
$-r < 13a - 156$.
$r > 156 - 13a$.

At $a = 0$: $r = 161 > 156$. ✓ B gives to A.
At $a = 1$: $r = 148 > 143$. ✓
At $a = 2$: $r = 135 > 130$. ✓
At $a = 3$: $r = 122 > 117$. ✓
At $a = 4$: $r = 109 > 104$. ✓
At $a = 5$: $r = 96 > 91$. ✓
At $a = 6$: $r = 83 > 78$. ✓
At $a = 7$: $r = 70 > 69$. ✓ (barely)
At $a = 8$: $r = 56$. Need $r > 156 - 104 = 52$. $56 > 52$. ✓ But at $a=8$, A puts 14 (since $c^* = 56/4 = 14$ is integer).

Hmm wait, at $a = 7$, $r = 70$, $d = 5$, $c^* = 14$. A puts 14.
- Give to A: $14 + f(8, 10, 56) = 14 + 3 \times 56/4 = 14 + 42 = 56$ (continuous).
- Give to B: $70 - 14 = 56$.
B is indifferent. Let's say B gives to A.

At $a = 8$, $r = 56$, $d = 4$, $c^* = 14$. A puts 14.
- Give to A: $14 + f(9, 10, 42) = 14 + 2 \times 42/3 = 14 + 28 = 42$.
- Give to B: $56 - 14 = 42$.
B is indifferent.

At $a = 9$, $r = 42$, $d = 3$, $c^* = 14$. A puts 14.
- Give to A: $14 + f(10, 10, 28) = 14 + 14 = 28$.
- Give to B: $42 - 14 = 28$.
B is indifferent.

At $a = 10$, $r = 28$. $f(10, 10, 28) = 14$.

So along this path, A gets:
- 0 coins from the first 10 bags (B took them all).
- 13 + 13 + 13 + 13 + 13 + 13 + 13 + 14 + 14 + 14 = $7 \times 13 + 3 \times 14 = 91 + 42 = 133$ coins from the next 10 bags (given to A).
- 14 coins from the last bag.
Total: $133 + 14 = 147$.

Hmm, 147. But this is just one path. B might choose differently.

Wait, but I need to check: is this the worst case for A? B is trying to minimize A's coins. Let me check if B could do better (give A fewer coins).

The path I traced has B taking 10 bags, then giving 10 bags to A, then the last bag is split. A gets 147.

But what if B takes fewer bags early on? Let me check another path.

Path 2: B gives some bags to A early on.

At (0, 0, 300): A puts 14 (ceil). 
- Give to A: $14 + f(1, 0, 286) = 14 + 10 \times 286/21 = 14 + 136.19 = 150.19$ (continuous).
- Give to B: $f(0, 1, 286) = 11 \times 286/21 = 149.81$ (continuous).
B gives to B (149.81 < 150.19).

So B takes the first bag. Same as before.

At (0, 1, 286): A puts 14 (ceil).
- Give to A: $14 + f(1, 1, 272) = 14 + 10 \times 272/20 = 14 + 136 = 150$ (continuous).
- Give to B: $f(0, 2, 272) = 11 \times 272/20 = 149.6$ (continuous).
B gives to B (149
