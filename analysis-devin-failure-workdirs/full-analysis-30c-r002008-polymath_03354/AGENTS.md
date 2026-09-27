# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In a rock-paper-scissors round robin tournament, any two contestants play against each other exactly $n$ times in a row. Each contestant has a favorite strategy, which is a fixed sequence of $n$ hands (from $\{R, P, S\}$), which they play against every other contestant. At the end of the tournament, it turned out that for any two players $A$ and $B$, $A$ won at least one hand (out of the $n$) against $B$. If $n = 10$, what is the maximum possible number of contestants that could have participated in the tournament?       — 题目文本
#   The problem can be modeled by representing each contestant's strategy as a vector $A \in \{0, 1, 2\}^n$ where $0, 1, 2$ represent Rock, Paper, and Scissors. Player $A$ wins a hand against $B$ at index $i$ if $a_i - b_i \equiv 1 \pmod 3$. The condition is that for any two distinct players $A$ and $B$, there is some $i$ such that $a_i - b_i \equiv 1 \pmod 3$. As shown in the solution, this implies the number of contestants is at most $2^n$. For $n=10$, the maximum number is $2^{10} = 1024$.  — 标准解答
#   Let me analyze this problem carefully.

We have a rock-paper-scissors round robin tournament. Each contestant has a fixed strategy: a sequence of n=10 hands from {R, P, S}. Any two contestants play against each other exactly n=10 times in a row. Each contestant plays their fixed sequence against every other contestant.

The condition: for any two players A and B, A won at least one hand (out of the n) against B.

Note: this is asymmetric in the sense that "A won at least one hand against B" must hold for BOTH directions (for any two players A and B). So for every pair {A, B}, A wins at least one of the 10 hands against B, AND B wins at least one of the 10 hands against A.

Wait, let me re-read. "for any two players A and B, A won at least one hand (out of the n) against B." This means for every ordered pair (A, B) with A ≠ B, A wins at least one hand against B. So yes, both directions.

Now, when A plays against B: A plays their sequence $a_1, ..., a_{10}$ and B plays their sequence $b_1, ..., b_{10}$. At position i, A plays $a_i$ and B plays $b_i$. A wins hand i if $a_i$ beats $b_i$ (R beats S, S beats P, P beats R). A ties if $a_i = b_i$. A loses if $b_i$ beats $a_i$.

The condition: for every ordered pair (A, B), there exists at least one i where $a_i$ beats $b_i$.

Equivalently: there is no pair (A, B) such that A never beats B in any of the 10 hands. A never beats B means: at every position i, either $a_i = b_i$ (tie) or $b_i$ beats $a_i$ (B wins). In other words, A never wins means at every position, $a_i \neq$ the hand that beats $b_i$... let me think differently.

Let me encode R, P, S as 0, 1, 2 where (i+1) mod 3 beats i. So 1 beats 0, 2 beats 1, 0 beats 2.

A wins at position i iff $(a_i - b_i) \mod 3 = 1$.
A ties iff $a_i = b_i$.
A loses iff $(a_i - b_i) \mod 3 = 2$.

A never beats B means: for all i, $(a_i - b_i) \mod 3 \in \{0, 2\}$. Equivalently, $(a_i - b_i) \mod 3 \neq 1$ for all i.

So the condition is: for every ordered pair (A, B) of distinct players, there exists i with $(a_i - b_i) \mod 3 = 1$.

We want to maximize the number of players (sequences) such that this holds for every ordered pair.

This is related to the concept of a "covering code" or a combinatorial design.

Let me think of it as: we have a set S of sequences in $\{0,1,2\}^{10}$. For every ordered pair (A, B) with A ≠ B in S, there exists a coordinate i where $(a_i - b_i) \mod 3 = 1$.

Equivalently, define a directed graph on sequences where A → B means "A beats B in at least one coordinate". We need this to be a tournament-like structure where every ordered pair has the edge (i.e., it's a complete directed graph, both directions present).

Actually, the condition is that for every ordered pair (A, B), A → B. So we need: for every pair {A, B}, both A → B and B → A.

Let me think about when A does NOT beat B: at every coordinate, $(a_i - b_i) \mod 3 \in \{0, 2\}$.

Let me define the "difference" $d = a - b \pmod{3}$, a vector in $\{0, 1, 2\}^{10}$. A beats B in at least one coordinate iff $d$ has at least one coordinate equal to 1. A does NOT beat B iff $d \in \{0, 2\}^{10}$ (every coordinate is 0 or 2).

So the condition is: for every ordered pair (A, B) with A ≠ B, the difference $a - b \pmod{3}$ is NOT in $\{0, 2\}^{10}$.

Equivalently: for every pair {A, B}, neither $a - b$ nor $b - a$ is in $\{0, 2\}^{10}$.

Note: $b - a = -(a - b) \pmod{3}$. If $d = a - b \in \{0, 2\}^{10}$, then $b - a = -d \pmod{3}$, and $-0 = 0$, $-2 = 1 \pmod{3}$. So $b - a$ has coordinates in $\{0, 1\}$. So $b - a \in \{0, 2\}^{10}$ iff $d \in \{0, 1\}^{10}$... no wait.

Let me be careful. $d \in \{0, 2\}^{10}$ means each coordinate is 0 or 2. $-d \pmod{3}$: $-0 = 0$, $-2 = 1$. So $-d \in \{0, 1\}^{10}$. For $-d$ to also be in $\{0, 2\}^{10}$, we'd need each coordinate in $\{0,1\} \cap \{0,2\} = \{0\}$, so $d = 0$, meaning $a = b$.

So: $a - b \in \{0,2\}^{10}$ and $b - a \in \{0,2\}^{10}$ simultaneously only if $a = b$.

For distinct A, B: if $a - b \in \{0,2\}^{10}$, then $b - a \in \{0,1\}^{10}$ and $b - a \notin \{0,2\}^{10}$ (since $a \neq b$, at least one coordinate of $d$ is 2, so $-d$ has a 1 there). So B does beat A (has a coordinate with difference 1), but A does not beat B.

So the condition "for every ordered pair (A,B), A beats B" is equivalent to: for every ordered pair (A, B) with A ≠ B, $a - b \notin \{0, 2\}^{10}$.

This is a symmetric condition in the following sense: if $a - b \notin \{0,2\}^{10}$ and $b - a \notin \{0,2\}^{10}$... wait, the condition must hold for ALL ordered pairs. So we need: for all A ≠ B, $a - b \notin \{0, 2\}^{10}$.

But as shown, if $a - b \in \{0,2\}^{10}$ and $a \neq b$, then $b - a \notin \{0,2\}^{10}$. So the condition "for all ordered pairs (A,B), $a-b \notin \{0,2\}^{10}$" is actually equivalent to "for all unordered pairs {A,B}, $a - b \notin \{0,2\}^{10}$" — because if $a - b \in \{0,2\}^{10}$ then automatically $b - a \notin \{0,2\}^{10}$, but the condition requires BOTH, so we need neither $a-b$ nor $b-a$ in $\{0,2\}^{10}$.

Hmm wait. The condition is: for every ordered pair (A, B), A beats B. So for the pair {A, B}, we need A beats B AND B beats A. A beats B means $a - b \notin \{0,2\}^{10}$. B beats A means $b - a \notin \{0,2\}^{10}$.

As shown, for $a \neq b$: $a - b \in \{0,2\}^{10}$ implies $b - a \notin \{0,2\}^{10}$. So the only way both fail is impossible (for distinct). But we need both to hold. So we need: $a - b \notin \{0,2\}^{10}$ AND $b - a \notin \{0,2\}^{10}$.

Now, $b - a \in \{0,2\}^{10}$ means $a - b \in \{0,1\}^{10}$ (negating). So the condition is:
- $a - b \notin \{0,2\}^{10}$ (i.e., $a-b$ has at least one coordinate equal to 1)
- $a - b \notin \{0,1\}^{10}$ (i.e., $a-b$ has at least one coordinate equal to 2)

Combined: $a - b$ must have at least one coordinate equal to 1 AND at least one coordinate equal to 2. In other words, $a - b$ must contain both 1 and 2 among its coordinates.

Equivalently: $a - b \notin \{0,1\}^{10} \cup \{0,2\}^{10}$.

So: for every pair of distinct sequences A, B in our set, the coordinate-wise difference $a - b \pmod{3}$ must contain at least one 1 and at least one 2.

This means: $a - b$ is not all in $\{0,1\}$ and not all in $\{0,2\}$.

Equivalently: there exists a coordinate where $a_i - b_i \equiv 1$ and a coordinate where $a_j - b_j \equiv 2$.

Now, let's think about this differently. Consider the map $\phi: \{0,1,2\}^{10} \to \{0,1\}^{10}$ where we replace 2 with 1 (i.e., $\phi(x)_i = 0$ if $x_i = 0$, $\phi(x)_i = 1$ if $x_i \in \{1,2\}$). Hmm, that might not directly help.

Let me think about it differently. The condition "$a - b \in \{0,1\}^{10}$" means: at every coordinate, $a_i \neq b_i + 2 \pmod{3}$, i.e., $a_i \neq b_i - 1 \pmod{3}$. In RPS terms, $a_i$ is not the hand that loses to $b_i$... hmm, let me think in terms of the original.

Actually, let me think about this problem using a known approach. This is a covering/packing problem on $\mathbb{Z}_3^{10}$.

We need a set $S \subseteq \mathbb{Z}_3^{10}$ such that for all distinct $a, b \in S$, $a - b$ has at least one coordinate $\equiv 1$ and at least one coordinate $\equiv 2 \pmod{3}$.

Equivalently, $a - b \notin \{0,1\}^{10} \cup \{0,2\}^{10}$ for all distinct $a, b$.

Let me define two "forbidden" sets:
- $F_1 = \{0,1\}^{10}$: differences where every coordinate is 0 or 1
- $F_2 = \{0,2\}^{10}$: differences where every coordinate is 0 or 2

We need: for all distinct $a, b \in S$, $a - b \notin F_1 \cup F_2$.

Note $F_1 \cap F_2 = \{0\}^{10} = \{0\}$, and $|F_1| = |F_2| = 2^{10} = 1024$, $|F_1 \cup F_2| = 1024 + 1024 - 1 = 2047$.

The total space is $\mathbb{Z}_3^{10}$ with $3^{10} = 59049$ elements.

So we need a code $S$ in $\mathbb{Z}_3^{10}$ where the difference of any two distinct codewords avoids $F_1 \cup F_2$.

This is like a packing/clique problem. Let me think about upper bounds.

**Approach 1: Delsarte / LP bound or direct counting.**

Let me think about a graph-theoretic formulation. Consider the graph $G$ on $\mathbb{Z}_3^{10}$ where two vertices $a, b$ are connected iff $a - b \notin F_1 \cup F_2$ (and $a \neq b$). We want the maximum clique in $G$.

The complement graph $\bar{G}$ has edges when $a - b \in F_1 \cup F_2 \setminus \{0\}$. We want the maximum independent set in $\bar{G}$, which is the maximum clique in $G$.

Actually, let me think about the structure more carefully.

Consider the partition of coordinates. For a difference vector $d = a - b$, the condition is that $d$ has at least one 1 and at least one 2.

Let me think about a different approach. Consider the "type" of a sequence. 

Hmm, let me think about small cases first and look for a pattern.

**Small case: n = 1.**
Sequences are single hands. Difference must have at least one 1 and at least one 2, but there's only 1 coordinate. So the difference must be both 1 and 2 in one coordinate — impossible. So for n=1, the maximum is 1 (any single player, vacuously satisfies the condition since there are no pairs).

Wait, but actually with n=1, can we have 2 players? We need $a - b$ to have at least one 1 and at least one 2. With one coordinate, $a - b$ is a single value, which can be 0, 1, or 2. It can't be both 1 and 2. So no, max is 1 for n=1.

**n = 2.**
We need $a - b$ (2 coordinates) to have at least one 1 and at least one 2. So the difference must be one of: (1,2), (2,1). (It could also be (1,2) with no zeros, or (1,0,...) no — we need at least one 1 and at least one 2, so the possibilities for 2 coordinates are: (1,2), (2,1). That's it — both coordinates must be nonzero, one is 1 and one is 2.)

So for n=2, we need a set S in $\mathbb{Z}_3^2$ such that for all distinct $a, b$, $a - b \in \{(1,2), (2,1)\}$.

The differences (1,2) and (2,1): note (2,1) = -(1,2) mod 3. So we need $a - b \in \{(1,2), (2,1)\}$ for all distinct pairs. 

How many such elements can we have? If we have 3 elements $a, b, c$, then $a-b$, $a-c$, $b-c$ must all be in $\{(1,2),(2,1)\}$. Say $a - b = (1,2)$, then $b - a = (2,1)$. Now $a - c \in \{(1,2),(2,1)\}$ and $b - c \in \{(1,2),(2,1)\}$. We have $a - c = (a - b) + (b - c)$. If $a - b = (1,2)$ and $b - c = (1,2)$, then $a - c = (2,1)$, which is allowed. If $a-b = (1,2)$ and $b-c = (2,1)$, then $a - c = (0,0)$, not allowed (a=c). So we can have at most... let's see. 

Take $a = (0,0)$, $b = (2,1)$ (so $a - b = (1,2)$ ✓), $c = (1,2)$ (so $a - c = (2,1)$ ✓, $b - c = (1,2)$ ✓). So we have 3 elements: $(0,0), (2,1), (1,2)$. Can we add a 4th? $d$ such that $d - a$, $d - b$, $d - c$ all in $\{(1,2),(2,1)\}$. $d - a \in \{(1,2),(2,1)\}$ so $d \in \{(1,2),(2,1)\}$. But those are $b$ and $c$. So no 4th element. Max for n=2 is 3.

**n = 3.**
We need $a - b$ to have at least one 1 and at least one 2 among 3 coordinates. The forbidden differences are those in $\{0,1\}^3 \cup \{0,2\}^3$, which has $8 + 8 - 1 = 15$ elements out of 27.

Let me think about this more generally. 

Actually, let me think about the problem differently. Let me consider the following approach.

For each sequence $x \in \{0,1,2\}^n$, consider the set of coordinates where $x_i = 0$, $x_i = 1$, $x_i = 2$. 

Hmm, this is getting complicated. Let me think about the structure of the problem.

**Key insight:** Consider the "support" approach. For a pair $(a, b)$, the difference $d = a - b$. We need $d$ to have at least one 1 and at least one 2.

Consider the following: map each sequence $x \in \mathbb{Z}_3^n$ to a subset of $[n]$ by looking at which coordinates are "non-zero" in some sense... Actually, let me think about a cleaner approach.

**Approach: Consider the two "projections".**

Define $\pi_1: \mathbb{Z}_3^n \to \mathbb{Z}_2^n$ by $\pi_1(x)_i = 0$ if $x_i = 0$, $\pi_1(x)_i = 1$ if $x_i \in \{1, 2\}$. (This maps to "is $x_i$ nonzero?")

Hmm, that doesn't directly use the structure.

Let me think again. The condition is: $a - b \notin \{0,1\}^n \cup \{0,2\}^n$.

$a - b \in \{0,1\}^n$ means: for all $i$, $a_i - b_i \in \{0, 1\} \pmod{3}$, i.e., $a_i \neq b_i + 2 \pmod{3}$, i.e., $a_i \neq b_i - 1 \pmod{3}$.

$a - b \in \{0,2\}^n$ means: for all $i$, $a_i - b_i \in \{0, 2\} \pmod{3}$, i.e., $a_i \neq b_i + 1 \pmod{3}$.

So $a - b \in \{0,1\}^n$ means $a$ never "loses to $b$ shifted" — specifically, $a_i$ is never the unique value that $b_i$ beats. And $a - b \in \{0,2\}^n$ means $a_i$ is never the unique value that beats $b_i$.

Hmm, let me think about this using a different encoding. 

Let me consider the problem as a coloring/covering problem. 

**Approach: Think of it as a graph coloring / independent set problem.**

We want the maximum set $S \subseteq \mathbb{Z}_3^{10}$ such that for all distinct $a, b \in S$, $a - b \notin \{0,1\}^{10} \cup \{0,2\}^{10}$.

This is the maximum clique in the Cayley graph on $\mathbb{Z}_3^{10}$ with connection set $\mathbb{Z}_3^{10} \setminus (\{0,1\}^{10} \cup \{0,2\}^{10})$.

Equivalently, maximum independent set in the Cayley graph with connection set $\{0,1\}^{10} \cup \{0,2\}^{10} \setminus \{0\}$.

The connection set $C = (\{0,1\}^{10} \cup \{0,2\}^{10}) \setminus \{0\}$ has $|C| = 2047$.

For an independent set in a Cayley graph, a standard bound is the Delsarte / Hoffman bound, or simply $|S| \leq |G| / \chi$ where $\chi$ is the chromatic number, or $|S| \leq |G| / (1 + |C|/\lambda_{min})$ (Hoffman bound) where $\lambda_{min}$ is the smallest eigenvalue.

The eigenvalues of a Cayley graph on an abelian group are given by characters. For $\mathbb{Z}_3^{10}$, the characters are $\chi_\omega(x) = \omega^{x \cdot \omega}$ where $\omega = e^{2\pi i/3}$ and $\omega$ ranges over $\mathbb{Z}_3^{10}$.

The eigenvalue for character $\omega$ is $\lambda_\omega = \sum_{c \in C} \chi_\omega(c) = \sum_{c \in C} \omega^{c \cdot \omega}$.

Hmm, this is getting complex. Let me think about whether there's a cleaner combinatorial approach.

**Approach: Partition-based upper bound.**

Consider the map $\phi: \mathbb{Z}_3^n \to \mathbb{Z}_2^n$ defined by: $\phi(x)_i = 0$ if $x_i = 0$, $\phi(x)_i = 1$ if $x_i \in \{1, 2\}$.

If $a - b \in \{0,2\}^n$, what does $\phi$ do? $a_i - b_i \in \{0, 2\}$. 
- If $a_i - b_i = 0$: $a_i = b_i$, so $\phi(a)_i = \phi(b)_i$.
- If $a_i - b_i = 2$: $a_i = b_i + 2 = b_i - 1$. If $b_i = 0$, $a_i = 2$: $\phi(b)_i = 0, \phi(a)_i = 1$. If $b_i = 1$, $a_i = 0$: $\phi(b)_i = 1, \phi(a)_i = 0$. If $b_i = 2$, $a_i = 1$: $\phi(b)_i = 1, \phi(a)_i = 1$.

So $\phi$ doesn't behave nicely. Let me try a different approach.

**Approach: Think about it as a ternary code with specific distance properties.**

The condition is that for any two codewords, their difference has at least one coordinate $\equiv 1$ and at least one $\equiv 2 \pmod 3$.

Let me think about what structures give large sets.

**Construction idea:** Consider sequences where we use only values $\{0, 1\}$ (binary sequences in $\mathbb{Z}_3^n$). For two such sequences $a, b \in \{0,1\}^n$, the difference $a - b$ has coordinates in $\{0, 1, 2\}$: if $a_i = b_i$, difference is 0; if $a_i = 1, b_i = 0$, difference is 1; if $a_i = 0, b_i = 1$, difference is 2. So the difference has a 1 exactly where $a_i = 1, b_i = 0$, and a 2 exactly where $a_i = 0, b_i = 1$. For the difference to have at least one 1 and at least one 2, we need: there exists $i$ with $a_i = 1, b_i = 0$ AND there exists $j$ with $a_j = 0, b_j = 1$. This means neither $a \subseteq b$ (as subsets of $[n]$, treating 1 as "in") nor $b \subseteq a$. In other words, $a$ and $b$ are incomparable as subsets.

So if we restrict to binary sequences $\{0,1\}^n$, the condition becomes: the corresponding subsets of $[n]$ form an antichain (no two are comparable by inclusion).

By Sperner's theorem, the maximum antichain in $2^{[n]}$ has size $\binom{n}{\lfloor n/2 \rfloor}$.

For $n = 10$: $\binom{10}{5} = 252$.

But can we do better by using all of $\mathbb{Z}_3^n$?

**Can we beat 252?**

Let me think about whether using the value 2 as well can help.

Consider a more general construction. Partition the coordinates into two groups, or use a more sophisticated structure.

Actually, let me think about an upper bound. 

**Upper bound approach:** 

Consider the following. For each sequence $x \in \mathbb{Z}_3^n$, define two binary strings:
- $u(x) \in \{0,1\}^n$ where $u(x)_i = 1$ iff $x_i \in \{1, 2\}$ (i.e., $x_i \neq 0$)... no, this doesn't capture the structure well.

Let me think differently. 

For a pair $(a, b)$, the condition $a - b \in \{0,1\}^n$ means $a_i \in \{b_i, b_i + 1\}$ for all $i$. The condition $a - b \in \{0,2\}^n$ means $a_i \in \{b_i, b_i - 1\}$ for all $i$.

So $a - b \in \{0,1\}^n$ means: $a$ is obtained from $b$ by, at each coordinate, either keeping $b_i$ or incrementing by 1 (mod 3). There are $2^n$ such $a$'s for each $b$ (including $a = b$).

Similarly for $\{0,2\}^n$.

Now, for any fixed $b$, the set of $a$ with $a - b \in \{0,1\}^n$ is a "cube" of size $2^n$ centered at $b$, and similarly for $\{0,2\}^n$.

The condition says: no two elements of $S$ can have their difference in $\{0,1\}^n \cup \{0,2\}^n$.

So for any $b \in S$, no other element of $S$ is in the "up-cube" $b + \{0,1\}^n$ or the "down-cube" $b + \{0,2\}^n$ (excluding $b$ itself).

The up-cube and down-cube of $b$ together contain $2 \cdot 2^n - 1 = 2^{n+1} - 1$ elements (they overlap only at $b$).

So each element of $S$ "blocks" $2^{n+1} - 2$ other elements (excluding itself). A simple packing bound gives $|S| \leq 3^n / (2^{n+1} - 1)$, but this is very loose.

For $n = 10$: $3^{10} / (2^{11} - 1) = 59049 / 2047 \approx 28.8$. That's way less than 252, so this bound is too loose (it doesn't account for the structure properly; the cubes overlap a lot).

Hmm, that can't be right as an upper bound since we already have a construction of 252. Let me recheck.

Oh wait, the packing bound I used is wrong. The "blocked" sets overlap heavily between different elements of $S$, so the simple counting bound $|S| \cdot (\text{block size}) \leq |G|$ is valid but very loose. 252 > 28.8, so this bound is indeed too loose to be useful. Let me reconsider.

Actually wait, $252 > 28.8$ means the bound $|S| \leq 28.8$ would be violated by our construction, so the bound must be wrong. Let me recheck.

The issue is that the "blocked" sets for different $b$'s overlap enormously, so the counting bound $|S| \cdot |block| \leq |G|$ is not valid in general (it's only valid if the blocks are disjoint, which they're not). The correct statement is: the blocks $b + (\{0,1\}^n \cup \{0,2\}^n \setminus \{0\})$ for $b \in S$ must be disjoint from $S \setminus \{b\}$, but they can overlap with each other. So the bound is just $|S| \leq |G|$ trivially, which is useless.

Let me think about a better approach.

**Approach: Use the structure of the problem more carefully.**

Let me reconsider. The condition is: for all distinct $a, b \in S$, $a - b \notin \{0,1\}^n \cup \{0,2\}^n$.

Let me think about this in terms of a graph homomorphism or a coloring.

Consider the graph $H$ on $\mathbb{Z}_3^n$ where $a \sim b$ iff $a - b \in \{0,1\}^n \cup \{0,2\}^n \setminus \{0\}$. We want the maximum independent set in $H$.

$H$ is a Cayley graph with connection set $C = (\{0,1\}^n \cup \{0,2\}^n) \setminus \{0\}$, $|C| = 2^{n+1} - 2$.

The maximum independent set is at most $|G| / \chi(H)$ where $\chi$ is the chromatic number, and by Hoffman's bound, at most $|G| \cdot (-\lambda_{min}) / (|C| - \lambda_{min})$ where $\lambda_{min}$ is the most negative eigenvalue.

Let me compute the eigenvalues. The eigenvalues of the Cayley graph are:
$$\lambda_\omega = \sum_{c \in C} \omega^{c \cdot \omega}$$
where $\omega$ ranges over $\mathbb{Z}_3^n$ (characters) and $c \cdot \omega = \sum_i c_i \omega_i \pmod{3}$, and $\omega$ here is a primitive cube root of unity $e^{2\pi i/3}$.

Actually, let me use $\omega = e^{2\pi i/3}$. The character indexed by $\mathbf{t} \in \mathbb{Z}_3^n$ is $\chi_{\mathbf{t}}(\mathbf{c}) = \omega^{\mathbf{t} \cdot \mathbf{c}}$.

The eigenvalue for character $\mathbf{t}$ is:
$$\lambda_{\mathbf{t}} = \sum_{\mathbf{c} \in C} \omega^{\mathbf{t} \cdot \mathbf{c}} = \sum_{\mathbf{c} \in \{0,1\}^n \cup \{0,2\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} - 1$$

(the $-1$ removes $\mathbf{c} = \mathbf{0}$).

Now, $\sum_{\mathbf{c} \in \{0,1\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} = \prod_{i=1}^n \sum_{c_i \in \{0,1\}} \omega^{t_i c_i} = \prod_{i=1}^n (1 + \omega^{t_i})$.

Similarly, $\sum_{\mathbf{c} \in \{0,2\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} = \prod_{i=1}^n (1 + \omega^{2t_i})$.

And $\sum_{\mathbf{c} \in \{0,1\}^n \cup \{0,2\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} = \prod_{i=1}^n (1 + \omega^{t_i}) + \prod_{i=1}^n (1 + \omega^{2t_i}) - 1$.

(The $-1$ is for double-counting $\mathbf{c} = 0$.)

So $\lambda_{\mathbf{t}} = \prod_{i=1}^n (1 + \omega^{t_i}) + \prod_{i=1}^n (1 + \omega^{2t_i}) - 2$.

Now, for each coordinate $i$, $t_i \in \{0, 1, 2\}$:
- If $t_i = 0$: $1 + \omega^0 = 2$ and $1 + \omega^0 = 2$.
- If $t_i = 1$: $1 + \omega^1 = 1 + \omega$ and $1 + \omega^2$. Note $1 + \omega = -\omega^2$ (since $1 + \omega + \omega^2 = 0$), and $1 + \omega^2 = -\omega$. So $1 + \omega = -\omega^2$ and $1 + \omega^2 = -\omega$.
- If $t_i = 2$: $1 + \omega^2 = -\omega$ and $1 + \omega^4 = 1 + \omega = -\omega^2$.

So let $a$ = number of coordinates with $t_i = 0$, $b$ = number with $t_i = 1$, $c$ = number with $t_i = 2$. $a + b + c = n$.

$\prod_i (1 + \omega^{t_i}) = 2^a \cdot (-\omega^2)^b \cdot (-\omega)^c = 2^a \cdot (-1)^{b+c} \cdot \omega^{2b+c}$.

$\prod_i (1 + \omega^{2t_i}) = 2^a \cdot (-\omega)^b \cdot (-\omega^2)^c = 2^a \cdot (-1)^{b+c} \cdot \omega^{b+2c}$.

So $\lambda = 2^a (-1)^{b+c} [\omega^{2b+c} + \omega^{b+2c}] - 2$.

Let $s = 2b + c$ and $s' = b + 2c$. Note $s + s' = 3(b+c) = 3(n-a)$, so $s' = 3(n-a) - s$, i.e., $s' \equiv -s \pmod{3}$. So $\omega^{s'} = \omega^{-s} = \overline{\omega^s}$.

Thus $\omega^s + \omega^{s'} = \omega^s + \omega^{-s} = 2\cos(2\pi s/3)$.

If $s \equiv 0 \pmod{3}$: $\omega^s + \omega^{-s} = 2$.
If $s \equiv 1 \pmod{3}$: $\omega + \omega^{-1} = \omega + \omega^2 = -1$.
If $s \equiv 2 \pmod{3}$: $\omega^2 + \omega^{-2} = \omega^2 + \omega = -1$.

So $\omega^s + \omega^{s'} = 2$ if $s \equiv 0 \pmod 3$, and $-1$ otherwise.

Therefore:
$$\lambda = 2^a (-1)^{b+c} \cdot \begin{cases} 2 & \text{if } s \equiv 0 \pmod 3 \\ -1 & \text{if } s \not\equiv 0 \pmod 3 \end{cases} - 2$$

where $s = 2b + c$ and $b + c = n - a$.

Case 1: $s \equiv 0 \pmod 3$.
$\lambda = 2^a (-1)^{n-a} \cdot 2 - 2 = 2^{a+1}(-1)^{n-a} - 2$.

Case 2: $s \not\equiv 0 \pmod 3$.
$\lambda = 2^a (-1)^{n-a} \cdot (-1) - 2 = -2^a (-1)^{n-a} - 2 = 2^a (-1)^{n-a+1} - 2$.

Hmm, let me simplify. Let $k = n - a = b + c$ (number of nonzero coordinates in $\mathbf{t}$).

Case 1: $s = 2b + c \equiv 0 \pmod 3$.
$\lambda = 2^{a+1} (-1)^k - 2 = (-1)^k 2^{n-k+1} - 2$.

Case 2: $s \not\equiv 0 \pmod 3$.
$\lambda = (-1)^{k+1} 2^{n-k} - 2$.

For the Hoffman bound, we need the most negative eigenvalue.

Let's consider $n = 10$ and find the minimum $\lambda$.

For $k = 0$ (i.e., $\mathbf{t} = 0$): $s = 0 \equiv 0$, Case 1: $\lambda = (-1)^0 \cdot 2^{11} - 2 = 2048 - 2 = 2046 = |C|$. This is the degree, as expected.

For $k = 1$: $b + c = 1$, so either $b=1, c=0$ ($s=2$) or $b=0, c=1$ ($s=1$). Both have $s \not\equiv 0$, Case 2: $\lambda = (-1)^2 \cdot 2^9 - 2 = 512 - 2 = 510$.

For $k = 2$: $b + c = 2$. $s = 2b + c$. Possible: $b=0,c=2: s=2$; $b=1,c=1: s=3 \equiv 0$; $b=2,c=0: s=4 \equiv 1$.
- $s \equiv 0$ (b=1,c=1): Case 1: $\lambda = (-1)^2 \cdot 2^{9} - 2 = 512 - 2 = 510$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^3 \cdot 2^8 - 2 = -256 - 2 = -258$.

For $k = 3$: $b + c = 3$. $s = 2b + c$.
- $s \equiv 0$: e.g., $b=0,c=0$... no, $b+c=3$. $b=0,c=3: s=3\equiv 0$. $b=3,c=0: s=6\equiv 0$. $b=1,c=2: s=4\equiv 1$. $b=2,c=1: s=5\equiv 2$.
  - $s \equiv 0$ (b=0,c=3 or b=3,c=0): Case 1: $\lambda = (-1)^3 \cdot 2^8 - 2 = -256 - 2 = -258$.
  - $s \not\equiv 0$: Case 2: $\lambda = (-1)^4 \cdot 2^7 - 2 = 128 - 2 = 126$.

For $k = 4$: $b+c=4$. 
- $s \equiv 0$: Case 1: $\lambda = (-1)^4 \cdot 2^7 - 2 = 128 - 2 = 126$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^5 \cdot 2^6 - 2 = -64 - 2 = -66$.

For $k = 5$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^5 \cdot 2^6 - 2 = -64 - 2 = -66$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^6 \cdot 2^5 - 2 = 32 - 2 = 30$.

For $k = 6$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^6 \cdot 2^5 - 2 = 32 - 2 = 30$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^7 \cdot 2^4 - 2 = -16 - 2 = -18$.

For $k = 7$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^7 \cdot 2^4 - 2 = -16 - 2 = -18$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^8 \cdot 2^3 - 2 = 8 - 2 = 6$.

For $k = 8$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^8 \cdot 2^3 - 2 = 8 - 2 = 6$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^9 \cdot 2^2 - 2 = -4 - 2 = -6$.

For $k = 9$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^9 \cdot 2^2 - 2 = -4 - 2 = -6$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^{10} \cdot 2^1 - 2 = 2 - 2 = 0$.

For $k = 10$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^{10} \cdot 2^1 - 2 = 2 - 2 = 0$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^{11} \cdot 2^0 - 2 = -1 - 2 = -3$.

So the eigenvalues are:
- $k=0$: 2046
- $k=1$: 510
- $k=2$: 510 or -258
- $k=3$: -258 or 126
- $k=4$: 126 or -66
- $k=5$: -66 or 30
- $k=6$: 30 or -18
- $k=7$: -18 or 6
- $k=8$: 6 or -6
- $k=9$: -6 or 0
- $k=10$: 0 or -3

The most negative eigenvalue is $\lambda_{min} = -258$ (achieved at $k=2$ with $s \not\equiv 0$, and $k=3$ with $s \equiv 0$).

Hoffman bound: $|S| \leq \frac{|G| \cdot (-\lambda_{min})}{|C| - \lambda_{min}} = \frac{3^{10} \cdot 258}{2046 - (-258)} = \frac{59049 \cdot 258}{2046 + 258} = \frac{59049 \cdot 258}{2304}$.

$59049 \cdot 258 = 59049 \cdot 258$. Let me compute: $59049 \cdot 250 = 14762250$, $59049 \cdot 8 = 472392$, total $= 15234642$.

$15234642 / 2304 = ?$. $2304 \cdot 6000 = 13824000$. $15234642 - 13824000 = 1410642$. $2304 \cdot 600 = 1382400$. $1410642 - 1382400 = 28242$. $2304 \cdot 12 = 27648$. $28242 - 27648 = 594$. $2304 \cdot 0.25 = 576$. So approximately $6612.25$.

So Hoffman bound gives $|S| \leq 6612$. That's much larger than 252, so it's not tight.

Hmm. So the Hoffman bound is not useful here. Let me think about this differently.

Let me reconsider the problem. Maybe the answer is exactly $\binom{10}{5} = 252$, achieved by the binary antichain construction, and we need to prove this is optimal.

But wait, can we do better than 252 by using ternary sequences? Let me think about small cases.

**n = 2:** We found max = 3. $\binom{2}{1} = 2$. So 3 > 2! The binary antichain gives only 2, but we found 3 using ternary sequences. So the binary construction is NOT optimal!

Let me recheck. For $n=2$, the binary antichain: subsets of $\{1,2\}$ of size 1, i.e., $\{1\}$ and $\{2\}$, corresponding to sequences $(1,0)$ and $(0,1)$. Their difference is $(1,2)$, which has a 1 and a 2. ✓. So 2 elements.

But we found 3: $(0,0), (2,1), (1,2)$. Differences: $(0,0)-(2,1) = (1,2)$ ✓, $(0,0)-(1,2) = (2,1)$ ✓, $(2,1)-(1,2) = (1,2)$ ✓. All have a 1 and a 2. So 3 works.

So the binary antichain is not optimal. We need a better approach.

**n = 3:** Let me try to find the maximum.

$\binom{3}{1} = 3$ (binary antichain of size 1 or 2 subsets). But we might do better.

Let me think about what structures work. The condition is: for all distinct $a, b$, $a - b$ has at least one 1 and at least one 2.

Consider using a "constant weight" code in $\mathbb{Z}_3^n$. 

Actually, let me think about this more carefully. The key observation for $n=2$ was that we used a "coset" structure: $(0,0), (2,1), (1,2) = (0,0), (0,0)+(2,1), (0,0)+2\cdot(2,1)$. This is a subgroup (or coset) of $\mathbb{Z}_3^2$ generated by $(2,1)$, which has order 3.

For a subgroup $H$ of $\mathbb{Z}_3^n$, the condition becomes: for all nonzero $h \in H$, $h$ has at least one 1 and at least one 2. This means every nonzero element of $H$ must have both a 1 and a 2 coordinate.

If $H$ is generated by a single element $g$, then $H = \{0, g, 2g\}$. We need $g$ and $2g$ to both have at least one 1 and at least one 2. $2g$ has a 1 where $g$ has a 2, and a 2 where $g$ has a 1. So if $g$ has at least one 1 and at least one 2, then $2g$ also does. So we need $g$ to have at least one 1 and at least one 2, i.e., $g$ is not in $\{0,1\}^n \cup \{0,2\}^n$.

For $n = 2$: $g = (2,1)$ works, giving $|H| = 3$.

Can we do better with a larger subgroup? For $n = 2$, a subgroup of order 9 is all of $\mathbb{Z}_3^2$, which contains $(1,0)$ (only 0s and 1s), so it doesn't work. A subgroup of order 3 is the best we can do for a subgroup.

But maybe non-subgroup constructions do better? For $n = 2$, we showed max is 3 (can't have 4). So 3 is optimal for $n=2$.

Let me think about $n = 3$ more carefully. Can we get more than 3?

Let me try a subgroup approach. Take $H = \langle g_1, g_2 \rangle$ of order 9. We need every nonzero element of $H$ to have at least one 1 and at least one 2.

Elements of $H$: $0, g_1, 2g_1, g_2, 2g_2, g_1+g_2, g_1+2g_2, 2g_1+g_2, 2g_1+2g_2$. We need all 8 nonzero elements to have at least one 1 and at least one 2.

Let me try $g_1 = (1,2,0), g_2 = (0,1,2)$.
- $g_1 = (1,2,0)$: has 1 and 2 ✓
- $2g_1 = (2,1,0)$: has 1 and 2 ✓
- $g_2 = (0,1,2)$: has 1 and 2 ✓
- $2g_2 = (0,2,1)$: has 1 and 2 ✓
- $g_1 + g_2 = (1,0,2)$: has 1 and 2 ✓
- $g_1 + 2g_2 = (1,1,2)$: has 1 and 2 ✓
- $2g_1 + g_2 = (2,0,2)$: has 2 but no 1 ✗!

So this doesn't work. Let me try other generators.

$g_1 = (1,2,1), g_2 = (2,1,2)$.
- $g_1 = (1,2,1)$ ✓
- $2g_1 = (2,1,2)$ = $g_2$... so they're not independent. $g_2 = 2g_1$, so $H = \langle g_1 \rangle$ has order 3.

Let me try $g_1 = (1,2,0), g_2 = (1,0,2)$.
- $g_1 = (1,2,0)$ ✓
- $2g_1 = (2,1,0)$ ✓
- $g_2 = (1,0,2)$ ✓
- $2g_2 = (2,0,1)$ ✓
- $g_1 + g_2 = (2,2,2)$: has 2 but no 1 ✗!

$g_1 = (1,2,0), g_2 = (2,0,1)$.
- $g_1 = (1,2,0)$ ✓
- $2g_1 = (2,1,0)$ ✓
- $g_2 = (2,0,1)$ ✓
- $2g_2 = (1,0,2)$ ✓
- $g_1 + g_2 = (0,2,1)$ ✓ (has 1 and 2)
- $g_1 + 2g_2 = (0,2,2)$: has 2 but no 1 ✗!

Hmm. Let me try to be more systematic. The issue is that sums of generators can land in $\{0,2\}^n$ or $\{0,1\}^n$.

Let me try $g_1 = (1,1,2), g_2 = (1,2,1)$.
- $g_1 = (1,1,2)$ ✓
- $2g_1 = (2,2,1)$ ✓
- $g_2 = (1,2,1)$ ✓
- $2g_2 = (2,1,2)$ ✓
- $g_1 + g_2 = (2,0,0)$: only 0 and 2, no 1 ✗!

$g_1 = (1,1,2), g_2 = (2,1,1)$.
- $g_1 = (1,1,2)$ ✓
- $2g_1 = (2,2,1)$ ✓
- $g_2 = (2,1,1)$ ✓
- $2g_2 = (1,2,2)$ ✓
- $g_1 + g_2 = (0,2,0)$: only 0 and 2 ✗!

It seems hard to get a subgroup of order 9 for $n=3$. Let me check if it's possible at all.

For a subgroup of order 9 in $\mathbb{Z}_3^3$, we need 8 nonzero elements, all with at least one 1 and at least one 2. The total number of elements in $\mathbb{Z}_3^3$ with at least one 1 and at least one 2 is $3^3 - 2 \cdot 2^3 + 1 = 27 - 16 + 1 = 12$ (inclusion-exclusion: total minus those in $\{0,1\}^3$ minus those in $\{0,2\}^3$ plus those in both = $\{0\}^3$). Wait: $|\{0,1\}^3| = 8$, $|\{0,2\}^3| = 8$, $|\{0,1\}^3 \cap \{0,2\}^3| = |\{0\}^3| = 1$. So $|\{0,1\}^3 \cup \{0,2\}^3| = 8 + 8 - 1 = 15$. Elements with at least one 1 and at least one 2: $27 - 15 = 12$.

So we need 8 of these 12 elements to form a subgroup (minus zero). The 12 elements with at least one 1 and at least one 2 in $\mathbb{Z}_3^3$ are: all elements except those in $\{0,1\}^3 \cup \{0,2\}^3$. $\{0,1\}^3 = \{(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)\}$. $\{0,2\}^3 = \{(0,0,0),(0,0,2),(0,2,0),(0,2,2),(2,0,0),(2,0,2),(2,2,0),(2,2,2)\}$. Union has 15 elements. The 12 elements with both 1 and 2 are: everything else, i.e., elements containing at least one 1 and at least one 2.

These are: $(1,2,0),(1,0,2),(0,1,2),(2,1,0),(2,0,1),(0,2,1),(1,2,1),(1,2,2),(2,1,1),(2,1,2),(1,1,2),(2,2,1)$... let me list them properly.

Elements with at least one 1 and at least one 2: I need to enumerate. An element $(a,b,c) \in \mathbb{Z}_3^3$ has at least one coordinate = 1 and at least one coordinate = 2.

Possible patterns (multisets of values):
- One 1, one 2, one 0: permutations of (0,1,2): 6 elements.
- One 1, two 2s: permutations of (1,2,2): 3 elements.
- Two 1s, one 2: permutations of (1,1,2): 3 elements.
Total: 6 + 3 + 3 = 12. ✓

Now, can 8 of these (plus 0) form a subgroup? A subgroup of order 9 in $\mathbb{Z}_3^3$ is a 2-dimensional subspace. It's determined by 2 generators.

Let me think about which 2-dimensional subspaces work. A 2D subspace has 9 elements (including 0), so 8 nonzero. We need all 8 to be among the 12 "good" elements.

The 2D subspaces of $\mathbb{Z}_3^3$ correspond to planes through the origin. There are $\frac{3^3 - 1}{3 - 1} \cdot \frac{3^3 - 3}{3^2 - 3} / 2! = \frac{26}{2} \cdot \frac{24}{6} / 2 = 13 \cdot 4 / 2 = 26$... actually the number of 2D subspaces of $\mathbb{F}_3^3$ is the Gaussian binomial $\binom{3}{2}_3 = \frac{(3^3-1)(3^2-1)}{(3^2-1)(3-1)} = \frac{26 \cdot 8}{8 \cdot 2} = \frac{26}{2} = 13$.

Each 2D subspace has 8 nonzero elements. We need all 8 to be "good" (have both 1 and 2). The 12 good elements need to contain a full 2D subspace's worth (8 elements).

A 2D subspace is the kernel of a nonzero linear functional $\ell: \mathbb{F}_3^3 \to \mathbb{F}_3$, i.e., $\{x : \ell(x) = 0\}$ for some nonzero $\ell$, up to scaling. There are $(3^3 - 1)/(3-1) = 13$ such functionals up to scaling, giving 13 planes.

Let me check the plane $\{x : x_1 + x_2 + x_3 = 0\}$. Elements: $(0,0,0), (0,1,2), (0,2,1), (1,0,2), (1,1,1), (1,2,0), (2,0,1), (2,1,0), (2,2,2)$. Nonzero: $(0,1,2), (0,2,1), (1,0,2), (1,1,1), (1,2,0), (2,0,1), (2,1,0), (2,2,2)$. Is $(1,1,1)$ good? It has 1s but no 2. ✗. So this plane doesn't work.

Plane $\{x : x_1 + x_2 + 2x_3 = 0\}$, i.e., $x_1 + x_2 - x_3 = 0$, i.e., $x_3 = x_1 + x_2$. Elements: $(a, b, a+b)$ for $a, b \in \mathbb{F}_3$.
- $(0,0,0)$: 0
- $(0,1,1)$: only 0,1 ✗
- $(0,2,2)$: only 0,2 ✗

Doesn't work.

Plane $\{x : x_1 + 2x_2 + 0 \cdot x_3 = 0\}$, i.e., $x_1 = x_2$. Elements: $(a, a, c)$.
- $(0,0,0), (0,0,1), (0,0,2), (1,1,0), (1,1,1), (1,1,2), (2,2,0), (2,2,1), (2,2,2)$.
- $(0,0,1)$: only 0,1 ✗.

It seems like every 2D subspace of $\mathbb{F}_3^3$ contains an element in $\{0,1\}^3 \setminus \{0\}$ or $\{0,2\}^3 \setminus \{0\}$. Let me verify this claim.

A 2D subspace (plane) in $\mathbb{F}_3^3$ contains $9 - 1 = 8$ nonzero elements. The "bad" elements (in $\{0,1\}^3 \cup \{0,2\}^3 \setminus \{0\}$) number $15 - 1 = 14$. The "good" elements number 12. 

If a plane has all 8 nonzero elements good, then it uses 8 of the 12 good elements. The remaining 4 good elements and 14 bad elements are outside the plane (the plane has $27 - 9 = 18$ elements outside).

Is it possible for a plane to avoid all 14 bad nonzero elements? The 14 bad elements are in $\{0,1\}^3 \cup \{0,2\}^3 \setminus \{0\}$. 

$\{0,1\}^3 \setminus \{0\}$ has 7 elements, $\{0,2\}^3 \setminus \{0\}$ has 7 elements. A plane has 8 nonzero elements. For the plane to avoid all 14 bad elements, all 8 nonzero elements must be among the 12 good ones.

Consider the restriction of the plane to $\{0,1\}^3$. The plane is $\{x : \ell(x) = 0\}$ for some linear functional $\ell$. The elements of $\{0,1\}^3$ in the plane are $\{x \in \{0,1\}^3 : \ell(x) = 0\}$. This is a subset of $\{0,1\}^3$ that's a "subcube" intersected with a hyperplane. 

$\ell(x) = a_1 x_1 + a_2 x_2 + a_3 x_3 = 0$ for $x \in \{0,1\}^3$. The zero element is always in. We need no other element of $\{0,1\}^3$ to be in the plane (otherwise it's a bad element in the plane). So we need $\ell(x) \neq 0$ for all $x \in \{0,1\}^3 \setminus \{0\}$.

Similarly, $\ell(x) \neq 0$ for all $x \in \{0,2\}^3 \setminus \{0\}$, i.e., $\ell(2y) = 2\ell(y) \neq 0$ for $y \in \{0,1\}^3 \setminus \{0\}$, which is the same as $\ell(y) \neq 0$ for $y \in \{0,1\}^3 \setminus \{0\}$.

So we need: $\ell(x) \neq 0$ for all $x \in \{0,1\}^3 \setminus \{0\}$, where $\ell(x) = a_1 x_1 + a_2 x_2 + a_3 x_3$ and $a_i \in \mathbb{F}_3$ (not all zero).

The elements of $\{0,1\}^3 \setminus \{0\}$ are: $(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1), (1,1,1)$.

We need:
- $a_1 \neq 0$
- $a_2 \neq 0$
- $a_3 \neq 0$
- $a_1 + a_2 \neq 0$
- $a_1 + a_3 \neq 0$
- $a_2 + a_3 \neq 0$
- $a_1 + a_2 + a_3 \neq 0$

With $a_i \in \{1, 2\}$ (since $a_i \neq 0$):
- If all $a_i = 1$: $a_1 + a_2 = 2 \neq 0$ ✓, $a_1 + a_2 + a_3 = 3 = 0$ ✗.
- If all $a_i = 2$: $a_1 + a_2 = 4 = 1 \neq 0$ ✓, $a_1 + a_2 + a_3 = 6 = 0$ ✗.
- Two 1s, one 2: say $a_1 = a_2 = 1, a_3 = 2$. $a_1 + a_2 = 2 \neq 0$ ✓, $a_1 + a_3 = 0$ ✗.
- Two 2s, one 1: say $a_1 = a_2 = 2, a_3 = 1$. $a_1 + a_2 = 4 = 1 \neq 0$ ✓, $a_1 + a_3 = 0$ ✗.

So in all cases, at least one condition fails. Therefore, no plane in $\mathbb{F}_3^3$ avoids all bad elements. So no subgroup of order 9 works for $n = 3$.

So for $n = 3$, the maximum subgroup that works has order 3 (a 1D subspace with a good generator). But can we do better with a non-subgroup construction?

Let me think about $n = 3$ more carefully. We want the maximum set $S \subseteq \mathbb{Z}_3^3$ such that all pairwise differences have at least one 1 and at least one 2.

Let me try to find a large set by computer-like reasoning.

The 12 good elements (with both 1 and 2) are:
Type (0,1,2) permutations: $(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)$ — 6 elements.
Type (1,1,2) permutations: $(1,1,2), (1,2,1), (2,1,1)$ — 3 elements.
Type (1,2,2) permutations: $(1,2,2), (2,1,2), (2,2,1)$ — 3 elements.

We need a set $S$ where all pairwise differences are good (have both 1 and 2). Note that $S$ can include elements outside the 12 good ones (e.g., $(0,0,0)$), as long as all pairwise differences are good.

Actually, $S$ can include any elements of $\mathbb{Z}_3^3$; the constraint is only on differences.

Let me try $S = \{(0,0,0), (1,2,0), (2,1,0)\}$. Differences: $(1,2,0), (2,1,0), (1,2,0)$. All have both 1 and 2 ✓. Size 3.

Can we add more? Try adding $(0,1,2)$: differences with $(0,0,0)$: $(0,1,2)$ ✓; with $(1,2,0)$: $(0,1,2) - (1,2,0) = (2,2,2)$, only 2s, no 1 ✗. So can't add $(0,1,2)$.

Try adding $(1,0,2)$: with $(0,0,0)$: $(1,0,2)$ ✓; with $(1,2,0)$: $(0,1,2)$ ✓; with $(2,1,0)$: $(2,2,2)$ ✗.

Try adding $(2,0,1)$: with $(0,0,0)$: $(2,0,1)$ ✓; with $(1,2,0)$: $(1,1,1)$ ✗.

Try adding $(0,2,1)$: with $(0,0,0)$: $(0,2,1)$ ✓; with $(1,2,0)$: $(2,0,1)$ ✓; with $(2,1,0)$: $(1,1,2)$ ✓. All good! So $S = \{(0,0,0), (1,2,0), (2,1,0), (0,2,1)\}$, size 4.

Can we add a 5th? Try $(0,1,2)$: with $(0,0,0)$: $(0,1,2)$ ✓; with $(1,2,0)$: $(2,2,2)$ ✗. No.

Try $(2,0,1)$: with $(0,0,0)$: $(2,0,1)$ ✓; with $(1,2,0)$: $(1,1,1)$ ✗. No.

Try $(1,0,2)$: with $(0,0,0)$: $(1,0,2)$ ✓; with $(1,2,0)$: $(0,1,2)$ ✓; with $(2,1,0)$: $(2,2,2)$ ✗. No.

Try $(2,2,1)$: with $(0,0,0)$: $(2,2,1)$ ✓; with $(1,2,0)$: $(1,0,1)$ ✗ (only 0,1). No.

Try $(1,1,2)$: with $(0,0,0)$: $(1,1,2)$ ✓; with $(1,2,0)$: $(0,2,2)$ ✗. No.

Try $(2,1,1)$: with $(0,0,0)$: $(2,1,1)$ ✓; with $(1,2,0)$: $(1,2,1)$ ✓; with $(2,1,0)$: $(0,0,1)$ ✗. No.

Try $(1,2,1)$: with $(0,0,0)$: $(1,2,1)$ ✓; with $(1,2,0)$: $(0,0,1)$ ✗. No.

Try $(2,1,2)$: with $(0,0,0)$: $(2,1,2)$ ✓; with $(1,2,0)$: $(1,2,2)$ ✓; with $(2,1,0)$: $(0,0,2)$ ✗. No.

Try $(1,2,2)$: with $(0,0,0)$: $(1,2,2)$ ✓; with $(1,2,0)$: $(0,0,2)$ ✗. No.

Try $(2,2,1)$: already tried. No.

Hmm, seems like 4 might be the max for $n=3$ with this particular starting set. But maybe a different set does better?

Let me try a different approach. Let me try to use a "product" construction.

For $n = 2$, max = 3. For $n = 3$, let me try to see if we can get 6 or more.

Actually, let me think about this problem from a higher level. 

The problem is asking for the maximum size of a set $S \subseteq \mathbb{Z}_3^n$ such that for all distinct $a, b \in S$, $a - b$ has at least one coordinate $\equiv 1$ and at least one $\equiv 2 \pmod{3}$.

This is equivalent to: $S$ is a "clique" in the graph where two elements are connected iff their difference has both a 1 and a 2.

Let me think about this using the concept of a "covering array" or "qualitative independence."

Actually, this reminds me of the concept of **qualitatively independent** partitions. Two partitions of a set are qualitatively independent if every cell of their join is nonempty. But I'm not sure that directly applies.

Let me think about another approach. Consider the following reformulation:

For each pair $(a, b)$, define $I_1(a,b) = \{i : a_i - b_i \equiv 1\}$ and $I_2(a,b) = \{i : a_i - b_i \equiv 2\}$. We need $I_1 \neq \emptyset$ and $I_2 \neq \emptyset$.

Now, consider the "type" of a sequence: the number of 0s, 1s, and 2s. Let $n_0(x), n_1(x), n_2(x)$ be the counts.

Hmm, this doesn't directly give a clean bound.

Let me think about the problem differently. Let me consider the following approach using a "tensor/product" structure.

**Product construction:** If $S_1$ works for $n_1$ and $S_2$ works for $n_2$, does $S_1 \times S_2$ work for $n_1 + n_2$?

For $(a_1, a_2), (b_1, b_2) \in S_1 \times S_2$, the difference is $(a_1 - b_1, a_2 - b_2)$. We need this to have at least one 1 and at least one 2. If $a_1 \neq b_1$, then $a_1 - b_1$ has at least one 1 and at least one 2 (since $S_1$ works), so the combined difference does too. If $a_1 = b_1$ but $a_2 \neq b_2$, then $a_2 - b_2$ has at least one 1 and at least one 2. So yes, the product construction works!

So $f(n_1 + n_2) \geq f(n_1) \cdot f(n_2)$ where $f(n)$ is the maximum for $n$ coordinates.

We have $f(1) = 1$, $f(2) = 3$.

$f(3) \geq f(2) \cdot f(1) = 3$. But we found 4 for $n=3$, so the product construction is not always optimal.

$f(4) \geq f(2) \cdot f(2) = 9$.

$f(10) \geq f(2)^5 = 3^5 = 243$ (by taking the product of 5 copies of the $n=2$ solution).

Also $f(10) \geq f(4) \cdot f(4) \cdot f(2) \geq 9 \cdot 9 \cdot 3 = 243$.

And $f(10) \geq f(3) \cdot f(3) \cdot f(4) \geq 4 \cdot 4 \cdot 9 = 144$, which is worse.

$f(10) \geq f(2)^5 = 243$.

But we also have the binary antichain giving 252. So 252 > 243.

Can we combine these? $f(10) \geq \max(252, 243) = 252$ from these constructions.

But maybe there are better constructions. Let me think about whether we can beat 252.

Let me reconsider the $n = 3$ case. We found 4, which is better than $f(2) \cdot f(1) = 3$ and better than $\binom{3}{1} = 3$ (binary antichain). What's the actual maximum for $n = 3$?

Let me try harder to find a set of size 5 or 6 for $n = 3$.

Actually, let me think about this more carefully. Let me consider the problem as a maximum clique problem and try to reason about it.

For $n = 3$, the graph has $27$ vertices. Two vertices $a, b$ are connected iff $a - b$ has at least one 1 and at least one 2. The "bad" differences are those in $\{0,1\}^3 \cup \{0,2\}^3 \setminus \{0\}$, which has 14 elements. So each vertex has $26 - 14 = 12$ neighbors.

We want the maximum clique. By the Hoffman bound or other methods...

Actually, let me just try to find a clique of size 5 or 6 by hand.

Let me use the set $\{(0,0,0), (1,2,0), (2,1,0), (0,2,1)\}$ (size 4) and try harder to extend.

Differences from $(0,0,0)$: $(1,2,0), (2,1,0), (0,2,1)$.
Differences from $(1,2,0)$: to others: $(2,1,0), (0,2,1), (2,0,1)$ (i.e., $(1,2,0)-(0,2,1) = (1,0,2)$... wait let me recompute.

$(1,2,0) - (0,0,0) = (1,2,0)$ ✓
$(1,2,0) - (2,1,0) = (2,1,0)$ ✓ (since $1-2=-1=2, 2-1=1, 0-0=0$)
$(1,2,0) - (0,2,1) = (1,0,2)$ ✓ (since $1-0=1, 2-2=0, 0-1=2$)
$(2,1,0) - (0,0,0) = (2,1,0)$ ✓
$(2,1,0) - (1,2,0) = (1,2,0)$ ✓
$(2,1,0) - (0,2,1) = (2,2,2)$ ✗!

Wait, $(2,1,0) - (0,2,1) = (2, 1-2, 0-1) = (2, -1, -1) = (2, 2, 2) \pmod 3$. This has only 2s, no 1. So this is BAD!

I made an error earlier. Let me recheck. I claimed $S = \{(0,0,0), (1,2,0), (2,1,0), (0,2,1)\}$ works, but $(2,1,0) - (0,2,1) = (2,2,2)$ which is bad. So this set does NOT work!

Let me redo this more carefully.

$(0,2,1) - (2,1,0) = (0-2, 2-1, 1-0) = (1, 1, 1) \pmod 3$. This has only 1s, no 2. Also bad!

So my earlier check was wrong. Let me recheck: I had said "with $(2,1,0)$: $(1,1,2)$" but that's $(0,2,1) - (2,1,0) = (-2, 1, 1) = (1, 1, 1)$. I made an arithmetic error. So the set of size 4 doesn't work.

Let me be more careful. For $n = 3$, let me try to find the maximum clique.

Let me start with $\{(0,0,0)\}$ and add elements one by one, checking all pairwise differences.

The neighbors of $(0,0,0)$ are the 12 "good" elements (those with at least one 1 and at least one 2).

Good elements: 
$(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0), (1,1,2), (1,2,1), (2,1,1), (1,2,2), (2,1,2), (2,2,1)$.

Now, among these 12, I need to find a clique (all pairwise differences are good).

Take $(1,2,0)$. Its differences with other good elements:
- $(0,1,2)$: $(1,2,0)-(0,1,2) = (1,1,1)$ — bad (only 1s).
- $(0,2,1)$: $(1,2,0)-(0,2,1) = (1,0,2)$ — good ✓.
- $(1,0,2)$: $(1,2,0)-(1,0,2) = (0,2,1)$ — good ✓.
- $(2,0,1)$: $(1,2,0)-(2,0,1) = (2,2,2)$ — bad.
- $(2,1,0)$: $(1,2,0)-(2,1,0) = (2,1,0)$ — good ✓.
- $(1,1,2)$: $(1,2,0)-(1,1,2) = (0,1,1)$ — bad (only 0,1).
- $(1,2,1)$: $(1,2,0)-(1,2,1) = (0,0,2)$ — bad.
- $(2,1,1)$: $(1,2,0)-(2,1,1) = (2,1,2)$ — good ✓.
- $(1,2,2)$: $(1,2,0)-(1,2,2) = (0,0,1)$ — bad.
- $(2,1,2)$: $(1,2,0)-(2,1,2) = (2,1,1)$ — good ✓.
- $(2,2,1)$: $(1,2,0)-(2,2,1) = (2,0,2)$ — bad.

So $(1,2,0)$'s good neighbors among the 12: $(0,2,1), (1,0,2), (2,1,0), (2,1,1), (2,1,2)$. That's 5.

Now I need a clique among $\{(0,0,0), (1,2,0)\} \cup \text{these 5}$. The 5 candidates are $(0,2,1), (1,0,2), (2,1,0), (2,1,1), (2,1,2)$. I need all pairwise differences among these 5 (and with $(1,2,0)$, already checked) to be good.

Let me check pairwise:
- $(0,2,1)$ vs $(1,0,2)$: $(0,2,1)-(1,0,2) = (2,2,2)$ — bad.
- $(0,2,1)$ vs $(2,1,0)$: $(0,2,1)-(2,1,0) = (1,1,1)$ — bad.
- $(0,2,1)$ vs $(2,1,1)$: $(0,2,1)-(2,1,1) = (1,1,0)$ — bad.
- $(0,2,1)$ vs $(2,1,2)$: $(0,2,1)-(2,1,2) = (1,1,2)$ — good ✓.
- $(1,0,2)$ vs $(2,1,0)$: $(1,0,2)-(2,1,0) = (2,2,2)$ — bad.
- $(1,0,2)$ vs $(2,1,1)$: $(1,0,2)-(2,1,1) = (2,2,1)$ — good ✓.
- $(1,0,2)$ vs $(2,1,2)$: $(1,0,2)-(2,1,2) = (2,2,0)$ — bad.
- $(2,1,0)$ vs $(2,1,1)$: $(2,1,0)-(2,1,1) = (0,0,2)$ — bad.
- $(2,1,0)$ vs $(2,1,2)$: $(2,1,0)-(2,1,2) = (0,0,1)$ — bad.
- $(2,1,1)$ vs $(2,1,2)$: $(2,1,1)-(2,1,2) = (0,0,2)$ — bad.

So the good pairs among the 5: only $\{(0,2,1), (2,1,2)\}$ and $\{(1,0,2), (2,1,1)\}$.

So the maximum clique containing $\{(0,0,0), (1,2,0)\}$ is at most $\{(0,0,0), (1,2,0), (0,2,1), (2,1,2)\}$ (size 4) or $\{(0,0,0), (1,2,0), (1,0,2), (2,1,1)\}$ (size 4).

Let me verify $\{(0,0,0), (1,2,0), (0,2,1), (2,1,2)\}$:
- $(0,0,0)$ vs all: differences are $(1,2,0), (0,2,1), (2,1,2)$ — all good ✓.
- $(1,2,0)$ vs $(0,2,1)$: $(1,0,2)$ — good ✓.
- $(1,2,0)$ vs $(2,1,2)$: $(2,1,1)$ — good ✓.
- $(0,2,1)$ vs $(2,1,2)$: $(1,1,2)$ — good ✓.
All good! Size 4. ✓

Can we extend to 5? We need an element $x$ such that $x - (0,0,0)$, $x - (1,2,0)$, $x - (0,2,1)$, $x - (2,1,2)$ are all good.

$x - (0,0,0) = x$ must be good.
$x - (1,2,0)$ must be good.
$x - (0,2,1)$ must be good.
$x - (2,1,2)$ must be good.

From the analysis, $x$ must be a good neighbor of $(1,2,0)$, so $x \in \{(0,2,1), (1,0,2), (2,1,0), (2,1,1), (2,1,2)\}$. But $(0,2,1)$ and $(2,1,2)$ are already in the set. So $x \in \{(1,0,2), (2,1,0), (2,1,1)\}$.

Check $x = (1,0,2)$: $x - (0,2,1) = (1,1,1)$ — bad. ✗.
Check $x = (2,1,0)$: $x - (0,2,1) = (2,2,2)$ — bad. ✗.
Check $x = (2,1,1)$: $x - (0,2,1) = (2,2,0)$ — bad. ✗.

So can't extend to 5. But maybe a completely different starting point gives 5?

Let me try starting with a different element. Due to the symmetry of the problem (we can translate and apply certain symmetries), let me try starting with elements of different types.

Actually, the problem has a lot of symmetry: $\mathbb{Z}_3^n$ acts on itself by translation, and the automorphism group includes coordinate permutations and the map $x \mapsto 2x$ (which swaps 1 and 2). Also, we can apply independent cyclic shifts to each coordinate: $x_i \mapsto x_i + c_i$ for any $c \in \mathbb{Z}_3^n$. Wait, translation by $c$ sends $a \mapsto a + c$, and differences are preserved: $(a+c) - (b+c) = a - b$. So translation doesn't change differences. So WLOG we can assume $(0,0,0) \in S$.

Also, the map $x \mapsto Mx$ for $M \in GL(n, \mathbb{F}_3)$ that preserves the "good" property... actually, the good property depends on the specific values 1 and 2, so only specific symmetries work. The symmetry $x \mapsto 2x$ sends 1 to 2 and 2 to 1, so it preserves "having both 1 and 2." Also, coordinate permutations preserve the property. And adding a constant to a specific coordinate: $x_i \mapsto x_i + c$ for all elements — this is translation, already covered.

So WLOG $(0,0,0) \in S$, and we need a clique among the 12 good elements.

Let me try to find the maximum clique among the 12 good elements (as a graph where edges connect elements with good differences).

I already found that starting from $(1,2,0)$, the max clique is 3 (among the 12, giving total 4 with $(0,0,0)$).

Let me try starting from a type-(1,1,2) element, say $(1,1,2)$.

$(1,1,2)$'s differences with all 12 good elements (excluding itself):
- $(0,1,2)$: $(1,0,0)$ — bad.
- $(0,2,1)$: $(1,2,1)$ — good ✓.
- $(1,0,2)$: $(0,1,0)$ — bad.
- $(1,2,0)$: $(0,2,2)$ — bad.
- $(2,0,1)$: $(2,1,1)$ — good ✓.
- $(2,1,0)$: $(2,0,2)$ — bad.
- $(1,2,1)$: $(0,2,1)$ — good ✓.
- $(2,1,1)$: $(2,0,1)$ — good ✓.
- $(1,2,2)$: $(0,2,0)$ — bad.
- $(2,1,2)$: $(2,0,0)$ — bad.
- $(2,2,1)$: $(2,2,1)$ — good ✓.

Good neighbors of $(1,1,2)$: $(0,2,1), (2,0,1), (1,2,1), (2,1,1), (2,2,1)$. 5 elements.

Now find a clique among these 5:
- $(0,2,1)$ vs $(2,0,1)$: $(0,2,1)-(2,0,1) = (1,2,0)$ — good ✓.
- $(0,2,1)$ vs $(1,2,1)$: $(0,2,1)-(1,2,1) = (2,0,0)$ — bad.
- $(0,2,1)$ vs $(2,1,1)$: $(0,2,1)-(2,1,1) = (1,1,0)$ — bad.
- $(0,2,1)$ vs $(2,2,1)$: $(0,2,1)-(2,2,1) = (1,0,0)$ — bad.
- $(2,0,1)$ vs $(1,2,1)$: $(2,0,1)-(1,2,1) = (1,1,0)$ — bad.
- $(2,0,1)$ vs $(2,1,1)$: $(2,0,1)-(2,1,1) = (0,2,0)$ — bad.
- $(2,0,1)$ vs $(2,2,1)$: $(2,0,1)-(2,2,1) = (0,1,0)$ — bad.
- $(1,2,1)$ vs $(2,1,1)$: $(1,2,1)-(2,1,1) = (2,1,0)$ — good ✓.
- $(1,2,1)$ vs $(2,2,1)$: $(1,2,1)-(2,2,1) = (2,0,0)$ — bad.
- $(2,1,1)$ vs $(2,2,1)$: $(2,1,1)-(2,2,1) = (0,2,0)$ — bad.

Good pairs: $\{(0,2,1), (2,0,1)\}$ and $\{(1,2,1), (2,1,1)\}$.

So max clique among these 5 is 2, giving total $1 + 1 + 2 = 4$ (including $(0,0,0)$ and $(1,1,2)$).

Let me try $\{(0,0,0), (1,1,2), (0,2,1), (2,0,1)\}$:
- $(0,2,1) - (2,0,1) = (1,2,0)$ — good ✓.
All pairwise differences good? Let me check all:
- $(1,1,2), (0,2,1), (2,0,1)$ are all good (differences from 0).
- $(1,1,2)-(0,2,1) = (1,2,1)$ — good ✓.
- $(1,1,2)-(2,0,1) = (2,1,1)$ — good ✓.
- $(0,2,1)-(2,0,1) = (1,2,0)$ — good ✓.
All good! Size 4. Can we extend?

Need $x$ good, $x-(1,1,2)$ good, $x-(0,2,1)$ good, $x-(2,0,1)$ good.

$x$ must be a good neighbor of $(1,1,2)$: $x \in \{(0,2,1), (2,0,1), (1,2,1), (2,1,1), (2,2,1)\}$. Remove $(0,2,1), (2,0,1)$ (already in set): $x \in \{(1,2,1), (2,1,1), (2,2,1)\}$.

- $x = (1,2,1)$: $x - (0,2,1) = (1,0,0)$ — bad. ✗.
- $x = (2,1,1)$: $x - (0,2,1) = (2,2,0)$ — bad. ✗.
- $x = (2,2,1)$: $x - (0,2,1) = (2,0,0)$ — bad. ✗.

Can't extend. So size 4 again.

Let me try a type-(1,2,2) element, say $(1,2,2)$.

$(1,2,2)$'s good neighbors among the 12:
- $(0,1,2)$: $(1,1,0)$ — bad.
- $(0,2,1)$: $(1,0,1)$ — bad.
- $(1,0,2)$: $(0,2,0)$ — bad.
- $(1,2,0)$: $(0,0,2)$ — bad.
- $(2,0,1)$: $(2,2,1)$ — good ✓.
- $(2,1,0)$: $(2,1,2)$ — good ✓.
- $(1,1,2)$: $(0,1,0)$ — bad.
- $(2,1,1)$: $(2,1,1)$ — good ✓.
- $(1,2,1)$: $(0,0,1)$ — bad.
- $(2,1,2)$: $(2,1,0)$ — good ✓.
- $(2,2,1)$: $(2,0,1)$ — good ✓.

Good neighbors: $(2,0,1), (2,1,0), (2,1,1), (2,1,2), (2,2,1)$. 5 elements.

Pairwise among these 5:
- $(2,0,1)$ vs $(2,1,0)$: $(0,2,1)$ — good ✓.
- $(2,0,1)$ vs $(2,1,1)$: $(0,2,0)$ — bad.
- $(2,0,1)$ vs $(2,1,2)$: $(0,2,2)$ — bad.
- $(2,0,1)$ vs $(2,2,1)$: $(0,1,0)$ — bad.
- $(2,1,0)$ vs $(2,1,1)$: $(0,0,2)$ — bad.
- $(2,1,0)$ vs $(2,1,2)$: $(0,0,1)$ — bad.
- $(2,1,0)$ vs $(2,2,1)$: $(0,2,2)$ — bad.
- $(2,1,1)$ vs $(2,1,2)$: $(0,0,2)$ — bad.
- $(2,1,1)$ vs $(2,2,1)$: $(0,2,0)$ — bad.
- $(2,1,2)$ vs $(2,2,1)$: $(0,2,1)$ — good ✓.

Good pairs: $\{(2,0,1), (2,1,0)\}$ and $\{(2,1,2), (2,2,1)\}$.

Max clique 2, total 4.

It seems like for $n=3$, the maximum is 4. Let me try one more approach: a type-(0,1,2) element, say $(0,1,2)$.

$(0,1,2)$'s good neighbors:
- $(0,2,1)$: $(0,2,1)$ — good ✓.
- $(1,0,2)$: $(2,1,0)$ — good ✓.
- $(1,2,0)$: $(2,2,2)$ — bad.
- $(2,0,1)$: $(1,1,1)$ — bad.
- $(2,1,0)$: $(1,0,2)$ — good ✓.
- $(1,1,2)$: $(2,0,0)$ — bad.
- $(1,2,1)$: $(2,2,1)$ — good ✓.
- $(2,1,1)$: $(1,0,1)$ — bad.
- $(1,2,2)$: $(2,2,0)$ — bad.
- $(2,1,2)$: $(1,0,0)$ — bad.
- $(2,2,1)$: $(1,2,2)$ — good ✓.

Good neighbors: $(0,2,1), (1,0,2), (2,1,0), (1,2,1), (2,2,1)$. 5 elements.

Pairwise:
- $(0,2,1)$ vs $(1,0,2)$: $(2,2,2)$ — bad.
- $(0,2,1)$ vs $(2,1,0)$: $(1,1,1)$ — bad.
- $(0,2,1)$ vs $(1,2,1)$: $(2,0,0)$ — bad.
- $(0,2,1)$ vs $(2,2,1)$: $(1,0,0)$ — bad.
- $(1,0,2)$ vs $(2,1,0)$: $(2,2,2)$ — bad.
- $(1,0,2)$ vs $(1,2,1)$: $(0,1,1)$ — bad.
- $(1,0,2)$ vs $(2,2,1)$: $(2,1,1)$ — good ✓.
- $(2,1,0)$ vs $(1,2,1)$: $(1,2,2)$ — good ✓.
- $(2,1,0)$ vs $(2,2,1)$: $(0,2,2)$ — bad.
- $(1,2,1)$ vs $(2,2,1)$: $(2,0,0)$ — bad.

Good pairs: $\{(1,0,2), (2,2,1)\}$ and $\{(2,1,0), (1,2,1)\}$.

Max clique 2, total 4.

So for $n = 3$, the maximum appears to be 4. Let me see if there's a clique of size 5 by trying a different approach.

Actually, I realize I should check: is there a clique of size 4 among the 12 good elements (giving total 5 with $(0,0,0)$)?

From the analysis, the maximum clique among the neighbors of any single good element is 2 (among the 5 neighbors). But a clique of size 4 among the 12 doesn't need to include any particular element. Let me think about this differently.

Actually, I've been checking cliques that include $(0,0,0)$ and one specific good element. But maybe there's a clique of size 4 among the 12 good elements that doesn't include any of the elements I've been checking.

Hmm, but by symmetry, I've checked representatives of each type (type (0,1,2), type (1,1,2), type (1,2,2)). Due to the symmetries of the problem (coordinate permutations and the $x \mapsto 2x$ map), these cover all cases up to symmetry. And in each case, the max clique among the neighbors is 2, giving total 4.

But wait, I need to check if there's a clique of size 4 among the 12 that doesn't include any specific element I checked. The issue is that I'm checking "what's the max clique containing $(0,0,0)$ and element $x$," and for each type of $x$, I get 4. But maybe there's a clique of size 5 containing $(0,0,0)$ where the 4 good elements form a clique.

A clique of size 4 among the 12 good elements: I need 4 elements, all pairwise differences good. From my analysis, for each starting element, the max clique among its neighbors is 2. So any clique of size 4 among the 12 would need each element to have at least 3 neighbors in the clique, but each element has at most a clique of size 2 among its neighbors. Wait, that's not quite right—the clique of size 4 means each element has 3 neighbors in the clique, and those 3 form a clique of size 3 among the element's neighbors. But I showed the max clique among any element's neighbors is 2. So no clique of size 4 exists among the 12.

Therefore, for $n = 3$, the maximum is 4 (including $(0,0,0)$, so 3 good elements forming a clique of size 3 among the 12, plus $(0,0,0)$).

Wait, I showed max clique among neighbors of any element is 2, so the max clique among the 12 is 3 (an element plus 2 of its neighbors that form a pair). Then total with $(0,0,0)$ is 4. And I showed this is achievable. So $f(3) = 4$.

Hmm wait, I need to be more careful. The max clique among the 12 good elements: I showed that for any element $x$ among the 12, the max clique in $x$'s neighborhood (among the 12) is 2. This means the max clique among the 12 is at most 3 (since any clique of size 4 would have each vertex with 3 neighbors in the clique, but max is 2). And I found cliques of size 3 (e.g., $\{(1,2,0), (0,2,1), (2,1,2)\}$ — let me verify: $(1,2,0)-(0,2,1) = (1,0,2)$ good ✓, $(1,2,0)-(2,1,2) = (2,1,1)$ good ✓, $(0,2,1)-(2,1,2) = (1,1,2)$ good ✓). So max clique among the 12 is 3, and $f(3) = 4$.

So we have:
- $f(1) = 1$
- $f(2) = 3$
- $f(3) = 4$
- $f(4) \geq f(2) \cdot f(2) = 9$
- $f(4) \geq f(3) \cdot f(1) = 4$
- $f(10) \geq f(2)^5 = 243$
- $f(10) \geq f(4) \cdot f(4) \cdot f(2) \geq 9 \cdot 9 \cdot 3 = 243$

Also, the binary antichain gives $f(10) \geq \binom{10}{5} = 252$.

Can we beat 252? Let me think about better constructions.

**Better construction idea:** Combine the binary antichain with the ternary construction.

For $n = 10 = 5 + 5$, we could use $f(5) \cdot f(5)$. What's $f(5)$?

$f(5) \geq f(2) \cdot f(3) = 3 \cdot 4 = 12$.
$f(5) \geq \binom{5}{2} = 10$ (binary antichain).

So $f(5) \geq 12$, and $f(10) \geq 12^2 = 144 < 252$.

$f(10) \geq f(2)^5 = 243 < 252$.

What about $f(10) \geq f(4) \cdot f(6)$? $f(4) \geq 9$, $f(6) \geq f(3)^2 = 16$ or $f(6) \geq f(2)^3 = 27$ or $f(6) \geq \binom{6}{3} = 20$. So $f(6) \geq 27$. $f(10) \geq 9 \cdot 27 = 243$.

$f(10) \geq f(2) \cdot f(8)$. $f(8) \geq f(2)^4 = 81$ or $f(8) \geq \binom{8}{4} = 70$. So $f(8) \geq 81$. $f(10) \geq 3 \cdot 81 = 243$.

So the product constructions all give 243, while the binary antichain gives 252. Can we do better than both?

Let me think about a hybrid construction. What if we use a combination of binary and ternary coordinates?

**Hybrid construction:** Split the 10 coordinates into two groups: $k$ "binary" coordinates (using only values 0, 1) and $10 - k$ "ternary" coordinates. On the binary coordinates, use an antichain; on the ternary coordinates, use a good code.

For two elements $(a_1, a_2)$ and $(b_1, b_2)$ where $a_1, b_1$ are binary and $a_2, b_2$ are ternary:
- If $a_1 \neq b_1$: the binary part gives a difference with at least one 1 (where $a_{1i} = 1, b_{1i} = 0$) and at least one 2 (where $a_{1i} = 0, b_{1i} = 1$), as long as the binary parts are incomparable. So the combined difference is good.
- If $a_1 = b_1$: the binary difference is all 0, so we need the ternary difference to be good. So the ternary parts must form a code where all pairwise differences are good.

So the construction is: take an antichain $A$ of subsets of $[k]$ (binary part), and for each element of $A$, assign a ternary codeword from a code $T$ on $10 - k$ coordinates. Two elements with the same binary part must have good ternary differences. Two elements with different binary parts automatically have good differences (from the binary part).

So the total size is $\        — AI历史解题过程（thinking）
#   polymath_03354         — 题目ID

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
  <problem_id>polymath_03354</problem_id>
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

In a rock-paper-scissors round robin tournament, any two contestants play against each other exactly $n$ times in a row. Each contestant has a favorite strategy, which is a fixed sequence of $n$ hands (from $\{R, P, S\}$), which they play against every other contestant. At the end of the tournament, it turned out that for any two players $A$ and $B$, $A$ won at least one hand (out of the $n$) against $B$. If $n = 10$, what is the maximum possible number of contestants that could have participated in the tournament?

## Standard Solution

The problem can be modeled by representing each contestant's strategy as a vector $A \in \{0, 1, 2\}^n$ where $0, 1, 2$ represent Rock, Paper, and Scissors. Player $A$ wins a hand against $B$ at index $i$ if $a_i - b_i \equiv 1 \pmod 3$. The condition is that for any two distinct players $A$ and $B$, there is some $i$ such that $a_i - b_i \equiv 1 \pmod 3$. As shown in the solution, this implies the number of contestants is at most $2^n$. For $n=10$, the maximum number is $2^{10} = 1024$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a rock-paper-scissors round robin tournament. Each contestant has a fixed strategy: a sequence of n=10 hands from {R, P, S}. Any two contestants play against each other exactly n=10 times in a row. Each contestant plays their fixed sequence against every other contestant.

The condition: for any two players A and B, A won at least one hand (out of the n) against B.

Note: this is asymmetric in the sense that "A won at least one hand against B" must hold for BOTH directions (for any two players A and B). So for every pair {A, B}, A wins at least one of the 10 hands against B, AND B wins at least one of the 10 hands against A.

Wait, let me re-read. "for any two players A and B, A won at least one hand (out of the n) against B." This means for every ordered pair (A, B) with A ≠ B, A wins at least one hand against B. So yes, both directions.

Now, when A plays against B: A plays their sequence $a_1, ..., a_{10}$ and B plays their sequence $b_1, ..., b_{10}$. At position i, A plays $a_i$ and B plays $b_i$. A wins hand i if $a_i$ beats $b_i$ (R beats S, S beats P, P beats R). A ties if $a_i = b_i$. A loses if $b_i$ beats $a_i$.

The condition: for every ordered pair (A, B), there exists at least one i where $a_i$ beats $b_i$.

Equivalently: there is no pair (A, B) such that A never beats B in any of the 10 hands. A never beats B means: at every position i, either $a_i = b_i$ (tie) or $b_i$ beats $a_i$ (B wins). In other words, A never wins means at every position, $a_i \neq$ the hand that beats $b_i$... let me think differently.

Let me encode R, P, S as 0, 1, 2 where (i+1) mod 3 beats i. So 1 beats 0, 2 beats 1, 0 beats 2.

A wins at position i iff $(a_i - b_i) \mod 3 = 1$.
A ties iff $a_i = b_i$.
A loses iff $(a_i - b_i) \mod 3 = 2$.

A never beats B means: for all i, $(a_i - b_i) \mod 3 \in \{0, 2\}$. Equivalently, $(a_i - b_i) \mod 3 \neq 1$ for all i.

So the condition is: for every ordered pair (A, B) of distinct players, there exists i with $(a_i - b_i) \mod 3 = 1$.

We want to maximize the number of players (sequences) such that this holds for every ordered pair.

This is related to the concept of a "covering code" or a combinatorial design.

Let me think of it as: we have a set S of sequences in $\{0,1,2\}^{10}$. For every ordered pair (A, B) with A ≠ B in S, there exists a coordinate i where $(a_i - b_i) \mod 3 = 1$.

Equivalently, define a directed graph on sequences where A → B means "A beats B in at least one coordinate". We need this to be a tournament-like structure where every ordered pair has the edge (i.e., it's a complete directed graph, both directions present).

Actually, the condition is that for every ordered pair (A, B), A → B. So we need: for every pair {A, B}, both A → B and B → A.

Let me think about when A does NOT beat B: at every coordinate, $(a_i - b_i) \mod 3 \in \{0, 2\}$.

Let me define the "difference" $d = a - b \pmod{3}$, a vector in $\{0, 1, 2\}^{10}$. A beats B in at least one coordinate iff $d$ has at least one coordinate equal to 1. A does NOT beat B iff $d \in \{0, 2\}^{10}$ (every coordinate is 0 or 2).

So the condition is: for every ordered pair (A, B) with A ≠ B, the difference $a - b \pmod{3}$ is NOT in $\{0, 2\}^{10}$.

Equivalently: for every pair {A, B}, neither $a - b$ nor $b - a$ is in $\{0, 2\}^{10}$.

Note: $b - a = -(a - b) \pmod{3}$. If $d = a - b \in \{0, 2\}^{10}$, then $b - a = -d \pmod{3}$, and $-0 = 0$, $-2 = 1 \pmod{3}$. So $b - a$ has coordinates in $\{0, 1\}$. So $b - a \in \{0, 2\}^{10}$ iff $d \in \{0, 1\}^{10}$... no wait.

Let me be careful. $d \in \{0, 2\}^{10}$ means each coordinate is 0 or 2. $-d \pmod{3}$: $-0 = 0$, $-2 = 1$. So $-d \in \{0, 1\}^{10}$. For $-d$ to also be in $\{0, 2\}^{10}$, we'd need each coordinate in $\{0,1\} \cap \{0,2\} = \{0\}$, so $d = 0$, meaning $a = b$.

So: $a - b \in \{0,2\}^{10}$ and $b - a \in \{0,2\}^{10}$ simultaneously only if $a = b$.

For distinct A, B: if $a - b \in \{0,2\}^{10}$, then $b - a \in \{0,1\}^{10}$ and $b - a \notin \{0,2\}^{10}$ (since $a \neq b$, at least one coordinate of $d$ is 2, so $-d$ has a 1 there). So B does beat A (has a coordinate with difference 1), but A does not beat B.

So the condition "for every ordered pair (A,B), A beats B" is equivalent to: for every ordered pair (A, B) with A ≠ B, $a - b \notin \{0, 2\}^{10}$.

This is a symmetric condition in the following sense: if $a - b \notin \{0,2\}^{10}$ and $b - a \notin \{0,2\}^{10}$... wait, the condition must hold for ALL ordered pairs. So we need: for all A ≠ B, $a - b \notin \{0, 2\}^{10}$.

But as shown, if $a - b \in \{0,2\}^{10}$ and $a \neq b$, then $b - a \notin \{0,2\}^{10}$. So the condition "for all ordered pairs (A,B), $a-b \notin \{0,2\}^{10}$" is actually equivalent to "for all unordered pairs {A,B}, $a - b \notin \{0,2\}^{10}$" — because if $a - b \in \{0,2\}^{10}$ then automatically $b - a \notin \{0,2\}^{10}$, but the condition requires BOTH, so we need neither $a-b$ nor $b-a$ in $\{0,2\}^{10}$.

Hmm wait. The condition is: for every ordered pair (A, B), A beats B. So for the pair {A, B}, we need A beats B AND B beats A. A beats B means $a - b \notin \{0,2\}^{10}$. B beats A means $b - a \notin \{0,2\}^{10}$.

As shown, for $a \neq b$: $a - b \in \{0,2\}^{10}$ implies $b - a \notin \{0,2\}^{10}$. So the only way both fail is impossible (for distinct). But we need both to hold. So we need: $a - b \notin \{0,2\}^{10}$ AND $b - a \notin \{0,2\}^{10}$.

Now, $b - a \in \{0,2\}^{10}$ means $a - b \in \{0,1\}^{10}$ (negating). So the condition is:
- $a - b \notin \{0,2\}^{10}$ (i.e., $a-b$ has at least one coordinate equal to 1)
- $a - b \notin \{0,1\}^{10}$ (i.e., $a-b$ has at least one coordinate equal to 2)

Combined: $a - b$ must have at least one coordinate equal to 1 AND at least one coordinate equal to 2. In other words, $a - b$ must contain both 1 and 2 among its coordinates.

Equivalently: $a - b \notin \{0,1\}^{10} \cup \{0,2\}^{10}$.

So: for every pair of distinct sequences A, B in our set, the coordinate-wise difference $a - b \pmod{3}$ must contain at least one 1 and at least one 2.

This means: $a - b$ is not all in $\{0,1\}$ and not all in $\{0,2\}$.

Equivalently: there exists a coordinate where $a_i - b_i \equiv 1$ and a coordinate where $a_j - b_j \equiv 2$.

Now, let's think about this differently. Consider the map $\phi: \{0,1,2\}^{10} \to \{0,1\}^{10}$ where we replace 2 with 1 (i.e., $\phi(x)_i = 0$ if $x_i = 0$, $\phi(x)_i = 1$ if $x_i \in \{1,2\}$). Hmm, that might not directly help.

Let me think about it differently. The condition "$a - b \in \{0,1\}^{10}$" means: at every coordinate, $a_i \neq b_i + 2 \pmod{3}$, i.e., $a_i \neq b_i - 1 \pmod{3}$. In RPS terms, $a_i$ is not the hand that loses to $b_i$... hmm, let me think in terms of the original.

Actually, let me think about this problem using a known approach. This is a covering/packing problem on $\mathbb{Z}_3^{10}$.

We need a set $S \subseteq \mathbb{Z}_3^{10}$ such that for all distinct $a, b \in S$, $a - b$ has at least one coordinate $\equiv 1$ and at least one coordinate $\equiv 2 \pmod{3}$.

Equivalently, $a - b \notin \{0,1\}^{10} \cup \{0,2\}^{10}$ for all distinct $a, b$.

Let me define two "forbidden" sets:
- $F_1 = \{0,1\}^{10}$: differences where every coordinate is 0 or 1
- $F_2 = \{0,2\}^{10}$: differences where every coordinate is 0 or 2

We need: for all distinct $a, b \in S$, $a - b \notin F_1 \cup F_2$.

Note $F_1 \cap F_2 = \{0\}^{10} = \{0\}$, and $|F_1| = |F_2| = 2^{10} = 1024$, $|F_1 \cup F_2| = 1024 + 1024 - 1 = 2047$.

The total space is $\mathbb{Z}_3^{10}$ with $3^{10} = 59049$ elements.

So we need a code $S$ in $\mathbb{Z}_3^{10}$ where the difference of any two distinct codewords avoids $F_1 \cup F_2$.

This is like a packing/clique problem. Let me think about upper bounds.

**Approach 1: Delsarte / LP bound or direct counting.**

Let me think about a graph-theoretic formulation. Consider the graph $G$ on $\mathbb{Z}_3^{10}$ where two vertices $a, b$ are connected iff $a - b \notin F_1 \cup F_2$ (and $a \neq b$). We want the maximum clique in $G$.

The complement graph $\bar{G}$ has edges when $a - b \in F_1 \cup F_2 \setminus \{0\}$. We want the maximum independent set in $\bar{G}$, which is the maximum clique in $G$.

Actually, let me think about the structure more carefully.

Consider the partition of coordinates. For a difference vector $d = a - b$, the condition is that $d$ has at least one 1 and at least one 2.

Let me think about a different approach. Consider the "type" of a sequence. 

Hmm, let me think about small cases first and look for a pattern.

**Small case: n = 1.**
Sequences are single hands. Difference must have at least one 1 and at least one 2, but there's only 1 coordinate. So the difference must be both 1 and 2 in one coordinate — impossible. So for n=1, the maximum is 1 (any single player, vacuously satisfies the condition since there are no pairs).

Wait, but actually with n=1, can we have 2 players? We need $a - b$ to have at least one 1 and at least one 2. With one coordinate, $a - b$ is a single value, which can be 0, 1, or 2. It can't be both 1 and 2. So no, max is 1 for n=1.

**n = 2.**
We need $a - b$ (2 coordinates) to have at least one 1 and at least one 2. So the difference must be one of: (1,2), (2,1). (It could also be (1,2) with no zeros, or (1,0,...) no — we need at least one 1 and at least one 2, so the possibilities for 2 coordinates are: (1,2), (2,1). That's it — both coordinates must be nonzero, one is 1 and one is 2.)

So for n=2, we need a set S in $\mathbb{Z}_3^2$ such that for all distinct $a, b$, $a - b \in \{(1,2), (2,1)\}$.

The differences (1,2) and (2,1): note (2,1) = -(1,2) mod 3. So we need $a - b \in \{(1,2), (2,1)\}$ for all distinct pairs. 

How many such elements can we have? If we have 3 elements $a, b, c$, then $a-b$, $a-c$, $b-c$ must all be in $\{(1,2),(2,1)\}$. Say $a - b = (1,2)$, then $b - a = (2,1)$. Now $a - c \in \{(1,2),(2,1)\}$ and $b - c \in \{(1,2),(2,1)\}$. We have $a - c = (a - b) + (b - c)$. If $a - b = (1,2)$ and $b - c = (1,2)$, then $a - c = (2,1)$, which is allowed. If $a-b = (1,2)$ and $b-c = (2,1)$, then $a - c = (0,0)$, not allowed (a=c). So we can have at most... let's see. 

Take $a = (0,0)$, $b = (2,1)$ (so $a - b = (1,2)$ ✓), $c = (1,2)$ (so $a - c = (2,1)$ ✓, $b - c = (1,2)$ ✓). So we have 3 elements: $(0,0), (2,1), (1,2)$. Can we add a 4th? $d$ such that $d - a$, $d - b$, $d - c$ all in $\{(1,2),(2,1)\}$. $d - a \in \{(1,2),(2,1)\}$ so $d \in \{(1,2),(2,1)\}$. But those are $b$ and $c$. So no 4th element. Max for n=2 is 3.

**n = 3.**
We need $a - b$ to have at least one 1 and at least one 2 among 3 coordinates. The forbidden differences are those in $\{0,1\}^3 \cup \{0,2\}^3$, which has $8 + 8 - 1 = 15$ elements out of 27.

Let me think about this more generally. 

Actually, let me think about the problem differently. Let me consider the following approach.

For each sequence $x \in \{0,1,2\}^n$, consider the set of coordinates where $x_i = 0$, $x_i = 1$, $x_i = 2$. 

Hmm, this is getting complicated. Let me think about the structure of the problem.

**Key insight:** Consider the "support" approach. For a pair $(a, b)$, the difference $d = a - b$. We need $d$ to have at least one 1 and at least one 2.

Consider the following: map each sequence $x \in \mathbb{Z}_3^n$ to a subset of $[n]$ by looking at which coordinates are "non-zero" in some sense... Actually, let me think about a cleaner approach.

**Approach: Consider the two "projections".**

Define $\pi_1: \mathbb{Z}_3^n \to \mathbb{Z}_2^n$ by $\pi_1(x)_i = 0$ if $x_i = 0$, $\pi_1(x)_i = 1$ if $x_i \in \{1, 2\}$. (This maps to "is $x_i$ nonzero?")

Hmm, that doesn't directly use the structure.

Let me think again. The condition is: $a - b \notin \{0,1\}^n \cup \{0,2\}^n$.

$a - b \in \{0,1\}^n$ means: for all $i$, $a_i - b_i \in \{0, 1\} \pmod{3}$, i.e., $a_i \neq b_i + 2 \pmod{3}$, i.e., $a_i \neq b_i - 1 \pmod{3}$.

$a - b \in \{0,2\}^n$ means: for all $i$, $a_i - b_i \in \{0, 2\} \pmod{3}$, i.e., $a_i \neq b_i + 1 \pmod{3}$.

So $a - b \in \{0,1\}^n$ means $a$ never "loses to $b$ shifted" — specifically, $a_i$ is never the unique value that $b_i$ beats. And $a - b \in \{0,2\}^n$ means $a_i$ is never the unique value that beats $b_i$.

Hmm, let me think about this using a different encoding. 

Let me consider the problem as a coloring/covering problem. 

**Approach: Think of it as a graph coloring / independent set problem.**

We want the maximum set $S \subseteq \mathbb{Z}_3^{10}$ such that for all distinct $a, b \in S$, $a - b \notin \{0,1\}^{10} \cup \{0,2\}^{10}$.

This is the maximum clique in the Cayley graph on $\mathbb{Z}_3^{10}$ with connection set $\mathbb{Z}_3^{10} \setminus (\{0,1\}^{10} \cup \{0,2\}^{10})$.

Equivalently, maximum independent set in the Cayley graph with connection set $\{0,1\}^{10} \cup \{0,2\}^{10} \setminus \{0\}$.

The connection set $C = (\{0,1\}^{10} \cup \{0,2\}^{10}) \setminus \{0\}$ has $|C| = 2047$.

For an independent set in a Cayley graph, a standard bound is the Delsarte / Hoffman bound, or simply $|S| \leq |G| / \chi$ where $\chi$ is the chromatic number, or $|S| \leq |G| / (1 + |C|/\lambda_{min})$ (Hoffman bound) where $\lambda_{min}$ is the smallest eigenvalue.

The eigenvalues of a Cayley graph on an abelian group are given by characters. For $\mathbb{Z}_3^{10}$, the characters are $\chi_\omega(x) = \omega^{x \cdot \omega}$ where $\omega = e^{2\pi i/3}$ and $\omega$ ranges over $\mathbb{Z}_3^{10}$.

The eigenvalue for character $\omega$ is $\lambda_\omega = \sum_{c \in C} \chi_\omega(c) = \sum_{c \in C} \omega^{c \cdot \omega}$.

Hmm, this is getting complex. Let me think about whether there's a cleaner combinatorial approach.

**Approach: Partition-based upper bound.**

Consider the map $\phi: \mathbb{Z}_3^n \to \mathbb{Z}_2^n$ defined by: $\phi(x)_i = 0$ if $x_i = 0$, $\phi(x)_i = 1$ if $x_i \in \{1, 2\}$.

If $a - b \in \{0,2\}^n$, what does $\phi$ do? $a_i - b_i \in \{0, 2\}$. 
- If $a_i - b_i = 0$: $a_i = b_i$, so $\phi(a)_i = \phi(b)_i$.
- If $a_i - b_i = 2$: $a_i = b_i + 2 = b_i - 1$. If $b_i = 0$, $a_i = 2$: $\phi(b)_i = 0, \phi(a)_i = 1$. If $b_i = 1$, $a_i = 0$: $\phi(b)_i = 1, \phi(a)_i = 0$. If $b_i = 2$, $a_i = 1$: $\phi(b)_i = 1, \phi(a)_i = 1$.

So $\phi$ doesn't behave nicely. Let me try a different approach.

**Approach: Think about it as a ternary code with specific distance properties.**

The condition is that for any two codewords, their difference has at least one coordinate $\equiv 1$ and at least one $\equiv 2 \pmod 3$.

Let me think about what structures give large sets.

**Construction idea:** Consider sequences where we use only values $\{0, 1\}$ (binary sequences in $\mathbb{Z}_3^n$). For two such sequences $a, b \in \{0,1\}^n$, the difference $a - b$ has coordinates in $\{0, 1, 2\}$: if $a_i = b_i$, difference is 0; if $a_i = 1, b_i = 0$, difference is 1; if $a_i = 0, b_i = 1$, difference is 2. So the difference has a 1 exactly where $a_i = 1, b_i = 0$, and a 2 exactly where $a_i = 0, b_i = 1$. For the difference to have at least one 1 and at least one 2, we need: there exists $i$ with $a_i = 1, b_i = 0$ AND there exists $j$ with $a_j = 0, b_j = 1$. This means neither $a \subseteq b$ (as subsets of $[n]$, treating 1 as "in") nor $b \subseteq a$. In other words, $a$ and $b$ are incomparable as subsets.

So if we restrict to binary sequences $\{0,1\}^n$, the condition becomes: the corresponding subsets of $[n]$ form an antichain (no two are comparable by inclusion).

By Sperner's theorem, the maximum antichain in $2^{[n]}$ has size $\binom{n}{\lfloor n/2 \rfloor}$.

For $n = 10$: $\binom{10}{5} = 252$.

But can we do better by using all of $\mathbb{Z}_3^n$?

**Can we beat 252?**

Let me think about whether using the value 2 as well can help.

Consider a more general construction. Partition the coordinates into two groups, or use a more sophisticated structure.

Actually, let me think about an upper bound. 

**Upper bound approach:** 

Consider the following. For each sequence $x \in \mathbb{Z}_3^n$, define two binary strings:
- $u(x) \in \{0,1\}^n$ where $u(x)_i = 1$ iff $x_i \in \{1, 2\}$ (i.e., $x_i \neq 0$)... no, this doesn't capture the structure well.

Let me think differently. 

For a pair $(a, b)$, the condition $a - b \in \{0,1\}^n$ means $a_i \in \{b_i, b_i + 1\}$ for all $i$. The condition $a - b \in \{0,2\}^n$ means $a_i \in \{b_i, b_i - 1\}$ for all $i$.

So $a - b \in \{0,1\}^n$ means: $a$ is obtained from $b$ by, at each coordinate, either keeping $b_i$ or incrementing by 1 (mod 3). There are $2^n$ such $a$'s for each $b$ (including $a = b$).

Similarly for $\{0,2\}^n$.

Now, for any fixed $b$, the set of $a$ with $a - b \in \{0,1\}^n$ is a "cube" of size $2^n$ centered at $b$, and similarly for $\{0,2\}^n$.

The condition says: no two elements of $S$ can have their difference in $\{0,1\}^n \cup \{0,2\}^n$.

So for any $b \in S$, no other element of $S$ is in the "up-cube" $b + \{0,1\}^n$ or the "down-cube" $b + \{0,2\}^n$ (excluding $b$ itself).

The up-cube and down-cube of $b$ together contain $2 \cdot 2^n - 1 = 2^{n+1} - 1$ elements (they overlap only at $b$).

So each element of $S$ "blocks" $2^{n+1} - 2$ other elements (excluding itself). A simple packing bound gives $|S| \leq 3^n / (2^{n+1} - 1)$, but this is very loose.

For $n = 10$: $3^{10} / (2^{11} - 1) = 59049 / 2047 \approx 28.8$. That's way less than 252, so this bound is too loose (it doesn't account for the structure properly; the cubes overlap a lot).

Hmm, that can't be right as an upper bound since we already have a construction of 252. Let me recheck.

Oh wait, the packing bound I used is wrong. The "blocked" sets overlap heavily between different elements of $S$, so the simple counting bound $|S| \cdot (\text{block size}) \leq |G|$ is valid but very loose. 252 > 28.8, so this bound is indeed too loose to be useful. Let me reconsider.

Actually wait, $252 > 28.8$ means the bound $|S| \leq 28.8$ would be violated by our construction, so the bound must be wrong. Let me recheck.

The issue is that the "blocked" sets for different $b$'s overlap enormously, so the counting bound $|S| \cdot |block| \leq |G|$ is not valid in general (it's only valid if the blocks are disjoint, which they're not). The correct statement is: the blocks $b + (\{0,1\}^n \cup \{0,2\}^n \setminus \{0\})$ for $b \in S$ must be disjoint from $S \setminus \{b\}$, but they can overlap with each other. So the bound is just $|S| \leq |G|$ trivially, which is useless.

Let me think about a better approach.

**Approach: Use the structure of the problem more carefully.**

Let me reconsider. The condition is: for all distinct $a, b \in S$, $a - b \notin \{0,1\}^n \cup \{0,2\}^n$.

Let me think about this in terms of a graph homomorphism or a coloring.

Consider the graph $H$ on $\mathbb{Z}_3^n$ where $a \sim b$ iff $a - b \in \{0,1\}^n \cup \{0,2\}^n \setminus \{0\}$. We want the maximum independent set in $H$.

$H$ is a Cayley graph with connection set $C = (\{0,1\}^n \cup \{0,2\}^n) \setminus \{0\}$, $|C| = 2^{n+1} - 2$.

The maximum independent set is at most $|G| / \chi(H)$ where $\chi$ is the chromatic number, and by Hoffman's bound, at most $|G| \cdot (-\lambda_{min}) / (|C| - \lambda_{min})$ where $\lambda_{min}$ is the most negative eigenvalue.

Let me compute the eigenvalues. The eigenvalues of the Cayley graph are:
$$\lambda_\omega = \sum_{c \in C} \omega^{c \cdot \omega}$$
where $\omega$ ranges over $\mathbb{Z}_3^n$ (characters) and $c \cdot \omega = \sum_i c_i \omega_i \pmod{3}$, and $\omega$ here is a primitive cube root of unity $e^{2\pi i/3}$.

Actually, let me use $\omega = e^{2\pi i/3}$. The character indexed by $\mathbf{t} \in \mathbb{Z}_3^n$ is $\chi_{\mathbf{t}}(\mathbf{c}) = \omega^{\mathbf{t} \cdot \mathbf{c}}$.

The eigenvalue for character $\mathbf{t}$ is:
$$\lambda_{\mathbf{t}} = \sum_{\mathbf{c} \in C} \omega^{\mathbf{t} \cdot \mathbf{c}} = \sum_{\mathbf{c} \in \{0,1\}^n \cup \{0,2\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} - 1$$

(the $-1$ removes $\mathbf{c} = \mathbf{0}$).

Now, $\sum_{\mathbf{c} \in \{0,1\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} = \prod_{i=1}^n \sum_{c_i \in \{0,1\}} \omega^{t_i c_i} = \prod_{i=1}^n (1 + \omega^{t_i})$.

Similarly, $\sum_{\mathbf{c} \in \{0,2\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} = \prod_{i=1}^n (1 + \omega^{2t_i})$.

And $\sum_{\mathbf{c} \in \{0,1\}^n \cup \{0,2\}^n} \omega^{\mathbf{t} \cdot \mathbf{c}} = \prod_{i=1}^n (1 + \omega^{t_i}) + \prod_{i=1}^n (1 + \omega^{2t_i}) - 1$.

(The $-1$ is for double-counting $\mathbf{c} = 0$.)

So $\lambda_{\mathbf{t}} = \prod_{i=1}^n (1 + \omega^{t_i}) + \prod_{i=1}^n (1 + \omega^{2t_i}) - 2$.

Now, for each coordinate $i$, $t_i \in \{0, 1, 2\}$:
- If $t_i = 0$: $1 + \omega^0 = 2$ and $1 + \omega^0 = 2$.
- If $t_i = 1$: $1 + \omega^1 = 1 + \omega$ and $1 + \omega^2$. Note $1 + \omega = -\omega^2$ (since $1 + \omega + \omega^2 = 0$), and $1 + \omega^2 = -\omega$. So $1 + \omega = -\omega^2$ and $1 + \omega^2 = -\omega$.
- If $t_i = 2$: $1 + \omega^2 = -\omega$ and $1 + \omega^4 = 1 + \omega = -\omega^2$.

So let $a$ = number of coordinates with $t_i = 0$, $b$ = number with $t_i = 1$, $c$ = number with $t_i = 2$. $a + b + c = n$.

$\prod_i (1 + \omega^{t_i}) = 2^a \cdot (-\omega^2)^b \cdot (-\omega)^c = 2^a \cdot (-1)^{b+c} \cdot \omega^{2b+c}$.

$\prod_i (1 + \omega^{2t_i}) = 2^a \cdot (-\omega)^b \cdot (-\omega^2)^c = 2^a \cdot (-1)^{b+c} \cdot \omega^{b+2c}$.

So $\lambda = 2^a (-1)^{b+c} [\omega^{2b+c} + \omega^{b+2c}] - 2$.

Let $s = 2b + c$ and $s' = b + 2c$. Note $s + s' = 3(b+c) = 3(n-a)$, so $s' = 3(n-a) - s$, i.e., $s' \equiv -s \pmod{3}$. So $\omega^{s'} = \omega^{-s} = \overline{\omega^s}$.

Thus $\omega^s + \omega^{s'} = \omega^s + \omega^{-s} = 2\cos(2\pi s/3)$.

If $s \equiv 0 \pmod{3}$: $\omega^s + \omega^{-s} = 2$.
If $s \equiv 1 \pmod{3}$: $\omega + \omega^{-1} = \omega + \omega^2 = -1$.
If $s \equiv 2 \pmod{3}$: $\omega^2 + \omega^{-2} = \omega^2 + \omega = -1$.

So $\omega^s + \omega^{s'} = 2$ if $s \equiv 0 \pmod 3$, and $-1$ otherwise.

Therefore:
$$\lambda = 2^a (-1)^{b+c} \cdot \begin{cases} 2 & \text{if } s \equiv 0 \pmod 3 \\ -1 & \text{if } s \not\equiv 0 \pmod 3 \end{cases} - 2$$

where $s = 2b + c$ and $b + c = n - a$.

Case 1: $s \equiv 0 \pmod 3$.
$\lambda = 2^a (-1)^{n-a} \cdot 2 - 2 = 2^{a+1}(-1)^{n-a} - 2$.

Case 2: $s \not\equiv 0 \pmod 3$.
$\lambda = 2^a (-1)^{n-a} \cdot (-1) - 2 = -2^a (-1)^{n-a} - 2 = 2^a (-1)^{n-a+1} - 2$.

Hmm, let me simplify. Let $k = n - a = b + c$ (number of nonzero coordinates in $\mathbf{t}$).

Case 1: $s = 2b + c \equiv 0 \pmod 3$.
$\lambda = 2^{a+1} (-1)^k - 2 = (-1)^k 2^{n-k+1} - 2$.

Case 2: $s \not\equiv 0 \pmod 3$.
$\lambda = (-1)^{k+1} 2^{n-k} - 2$.

For the Hoffman bound, we need the most negative eigenvalue.

Let's consider $n = 10$ and find the minimum $\lambda$.

For $k = 0$ (i.e., $\mathbf{t} = 0$): $s = 0 \equiv 0$, Case 1: $\lambda = (-1)^0 \cdot 2^{11} - 2 = 2048 - 2 = 2046 = |C|$. This is the degree, as expected.

For $k = 1$: $b + c = 1$, so either $b=1, c=0$ ($s=2$) or $b=0, c=1$ ($s=1$). Both have $s \not\equiv 0$, Case 2: $\lambda = (-1)^2 \cdot 2^9 - 2 = 512 - 2 = 510$.

For $k = 2$: $b + c = 2$. $s = 2b + c$. Possible: $b=0,c=2: s=2$; $b=1,c=1: s=3 \equiv 0$; $b=2,c=0: s=4 \equiv 1$.
- $s \equiv 0$ (b=1,c=1): Case 1: $\lambda = (-1)^2 \cdot 2^{9} - 2 = 512 - 2 = 510$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^3 \cdot 2^8 - 2 = -256 - 2 = -258$.

For $k = 3$: $b + c = 3$. $s = 2b + c$.
- $s \equiv 0$: e.g., $b=0,c=0$... no, $b+c=3$. $b=0,c=3: s=3\equiv 0$. $b=3,c=0: s=6\equiv 0$. $b=1,c=2: s=4\equiv 1$. $b=2,c=1: s=5\equiv 2$.
  - $s \equiv 0$ (b=0,c=3 or b=3,c=0): Case 1: $\lambda = (-1)^3 \cdot 2^8 - 2 = -256 - 2 = -258$.
  - $s \not\equiv 0$: Case 2: $\lambda = (-1)^4 \cdot 2^7 - 2 = 128 - 2 = 126$.

For $k = 4$: $b+c=4$. 
- $s \equiv 0$: Case 1: $\lambda = (-1)^4 \cdot 2^7 - 2 = 128 - 2 = 126$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^5 \cdot 2^6 - 2 = -64 - 2 = -66$.

For $k = 5$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^5 \cdot 2^6 - 2 = -64 - 2 = -66$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^6 \cdot 2^5 - 2 = 32 - 2 = 30$.

For $k = 6$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^6 \cdot 2^5 - 2 = 32 - 2 = 30$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^7 \cdot 2^4 - 2 = -16 - 2 = -18$.

For $k = 7$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^7 \cdot 2^4 - 2 = -16 - 2 = -18$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^8 \cdot 2^3 - 2 = 8 - 2 = 6$.

For $k = 8$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^8 \cdot 2^3 - 2 = 8 - 2 = 6$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^9 \cdot 2^2 - 2 = -4 - 2 = -6$.

For $k = 9$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^9 \cdot 2^2 - 2 = -4 - 2 = -6$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^{10} \cdot 2^1 - 2 = 2 - 2 = 0$.

For $k = 10$:
- $s \equiv 0$: Case 1: $\lambda = (-1)^{10} \cdot 2^1 - 2 = 2 - 2 = 0$.
- $s \not\equiv 0$: Case 2: $\lambda = (-1)^{11} \cdot 2^0 - 2 = -1 - 2 = -3$.

So the eigenvalues are:
- $k=0$: 2046
- $k=1$: 510
- $k=2$: 510 or -258
- $k=3$: -258 or 126
- $k=4$: 126 or -66
- $k=5$: -66 or 30
- $k=6$: 30 or -18
- $k=7$: -18 or 6
- $k=8$: 6 or -6
- $k=9$: -6 or 0
- $k=10$: 0 or -3

The most negative eigenvalue is $\lambda_{min} = -258$ (achieved at $k=2$ with $s \not\equiv 0$, and $k=3$ with $s \equiv 0$).

Hoffman bound: $|S| \leq \frac{|G| \cdot (-\lambda_{min})}{|C| - \lambda_{min}} = \frac{3^{10} \cdot 258}{2046 - (-258)} = \frac{59049 \cdot 258}{2046 + 258} = \frac{59049 \cdot 258}{2304}$.

$59049 \cdot 258 = 59049 \cdot 258$. Let me compute: $59049 \cdot 250 = 14762250$, $59049 \cdot 8 = 472392$, total $= 15234642$.

$15234642 / 2304 = ?$. $2304 \cdot 6000 = 13824000$. $15234642 - 13824000 = 1410642$. $2304 \cdot 600 = 1382400$. $1410642 - 1382400 = 28242$. $2304 \cdot 12 = 27648$. $28242 - 27648 = 594$. $2304 \cdot 0.25 = 576$. So approximately $6612.25$.

So Hoffman bound gives $|S| \leq 6612$. That's much larger than 252, so it's not tight.

Hmm. So the Hoffman bound is not useful here. Let me think about this differently.

Let me reconsider the problem. Maybe the answer is exactly $\binom{10}{5} = 252$, achieved by the binary antichain construction, and we need to prove this is optimal.

But wait, can we do better than 252 by using ternary sequences? Let me think about small cases.

**n = 2:** We found max = 3. $\binom{2}{1} = 2$. So 3 > 2! The binary antichain gives only 2, but we found 3 using ternary sequences. So the binary construction is NOT optimal!

Let me recheck. For $n=2$, the binary antichain: subsets of $\{1,2\}$ of size 1, i.e., $\{1\}$ and $\{2\}$, corresponding to sequences $(1,0)$ and $(0,1)$. Their difference is $(1,2)$, which has a 1 and a 2. ✓. So 2 elements.

But we found 3: $(0,0), (2,1), (1,2)$. Differences: $(0,0)-(2,1) = (1,2)$ ✓, $(0,0)-(1,2) = (2,1)$ ✓, $(2,1)-(1,2) = (1,2)$ ✓. All have a 1 and a 2. So 3 works.

So the binary antichain is not optimal. We need a better approach.

**n = 3:** Let me try to find the maximum.

$\binom{3}{1} = 3$ (binary antichain of size 1 or 2 subsets). But we might do better.

Let me think about what structures work. The condition is: for all distinct $a, b$, $a - b$ has at least one 1 and at least one 2.

Consider using a "constant weight" code in $\mathbb{Z}_3^n$. 

Actually, let me think about this more carefully. The key observation for $n=2$ was that we used a "coset" structure: $(0,0), (2,1), (1,2) = (0,0), (0,0)+(2,1), (0,0)+2\cdot(2,1)$. This is a subgroup (or coset) of $\mathbb{Z}_3^2$ generated by $(2,1)$, which has order 3.

For a subgroup $H$ of $\mathbb{Z}_3^n$, the condition becomes: for all nonzero $h \in H$, $h$ has at least one 1 and at least one 2. This means every nonzero element of $H$ must have both a 1 and a 2 coordinate.

If $H$ is generated by a single element $g$, then $H = \{0, g, 2g\}$. We need $g$ and $2g$ to both have at least one 1 and at least one 2. $2g$ has a 1 where $g$ has a 2, and a 2 where $g$ has a 1. So if $g$ has at least one 1 and at least one 2, then $2g$ also does. So we need $g$ to have at least one 1 and at least one 2, i.e., $g$ is not in $\{0,1\}^n \cup \{0,2\}^n$.

For $n = 2$: $g = (2,1)$ works, giving $|H| = 3$.

Can we do better with a larger subgroup? For $n = 2$, a subgroup of order 9 is all of $\mathbb{Z}_3^2$, which contains $(1,0)$ (only 0s and 1s), so it doesn't work. A subgroup of order 3 is the best we can do for a subgroup.

But maybe non-subgroup constructions do better? For $n = 2$, we showed max is 3 (can't have 4). So 3 is optimal for $n=2$.

Let me think about $n = 3$ more carefully. Can we get more than 3?

Let me try a subgroup approach. Take $H = \langle g_1, g_2 \rangle$ of order 9. We need every nonzero element of $H$ to have at least one 1 and at least one 2.

Elements of $H$: $0, g_1, 2g_1, g_2, 2g_2, g_1+g_2, g_1+2g_2, 2g_1+g_2, 2g_1+2g_2$. We need all 8 nonzero elements to have at least one 1 and at least one 2.

Let me try $g_1 = (1,2,0), g_2 = (0,1,2)$.
- $g_1 = (1,2,0)$: has 1 and 2 ✓
- $2g_1 = (2,1,0)$: has 1 and 2 ✓
- $g_2 = (0,1,2)$: has 1 and 2 ✓
- $2g_2 = (0,2,1)$: has 1 and 2 ✓
- $g_1 + g_2 = (1,0,2)$: has 1 and 2 ✓
- $g_1 + 2g_2 = (1,1,2)$: has 1 and 2 ✓
- $2g_1 + g_2 = (2,0,2)$: has 2 but no 1 ✗!

So this doesn't work. Let me try other generators.

$g_1 = (1,2,1), g_2 = (2,1,2)$.
- $g_1 = (1,2,1)$ ✓
- $2g_1 = (2,1,2)$ = $g_2$... so they're not independent. $g_2 = 2g_1$, so $H = \langle g_1 \rangle$ has order 3.

Let me try $g_1 = (1,2,0), g_2 = (1,0,2)$.
- $g_1 = (1,2,0)$ ✓
- $2g_1 = (2,1,0)$ ✓
- $g_2 = (1,0,2)$ ✓
- $2g_2 = (2,0,1)$ ✓
- $g_1 + g_2 = (2,2,2)$: has 2 but no 1 ✗!

$g_1 = (1,2,0), g_2 = (2,0,1)$.
- $g_1 = (1,2,0)$ ✓
- $2g_1 = (2,1,0)$ ✓
- $g_2 = (2,0,1)$ ✓
- $2g_2 = (1,0,2)$ ✓
- $g_1 + g_2 = (0,2,1)$ ✓ (has 1 and 2)
- $g_1 + 2g_2 = (0,2,2)$: has 2 but no 1 ✗!

Hmm. Let me try to be more systematic. The issue is that sums of generators can land in $\{0,2\}^n$ or $\{0,1\}^n$.

Let me try $g_1 = (1,1,2), g_2 = (1,2,1)$.
- $g_1 = (1,1,2)$ ✓
- $2g_1 = (2,2,1)$ ✓
- $g_2 = (1,2,1)$ ✓
- $2g_2 = (2,1,2)$ ✓
- $g_1 + g_2 = (2,0,0)$: only 0 and 2, no 1 ✗!

$g_1 = (1,1,2), g_2 = (2,1,1)$.
- $g_1 = (1,1,2)$ ✓
- $2g_1 = (2,2,1)$ ✓
- $g_2 = (2,1,1)$ ✓
- $2g_2 = (1,2,2)$ ✓
- $g_1 + g_2 = (0,2,0)$: only 0 and 2 ✗!

It seems hard to get a subgroup of order 9 for $n=3$. Let me check if it's possible at all.

For a subgroup of order 9 in $\mathbb{Z}_3^3$, we need 8 nonzero elements, all with at least one 1 and at least one 2. The total number of elements in $\mathbb{Z}_3^3$ with at least one 1 and at least one 2 is $3^3 - 2 \cdot 2^3 + 1 = 27 - 16 + 1 = 12$ (inclusion-exclusion: total minus those in $\{0,1\}^3$ minus those in $\{0,2\}^3$ plus those in both = $\{0\}^3$). Wait: $|\{0,1\}^3| = 8$, $|\{0,2\}^3| = 8$, $|\{0,1\}^3 \cap \{0,2\}^3| = |\{0\}^3| = 1$. So $|\{0,1\}^3 \cup \{0,2\}^3| = 8 + 8 - 1 = 15$. Elements with at least one 1 and at least one 2: $27 - 15 = 12$.

So we need 8 of these 12 elements to form a subgroup (minus zero). The 12 elements with at least one 1 and at least one 2 in $\mathbb{Z}_3^3$ are: all elements except those in $\{0,1\}^3 \cup \{0,2\}^3$. $\{0,1\}^3 = \{(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)\}$. $\{0,2\}^3 = \{(0,0,0),(0,0,2),(0,2,0),(0,2,2),(2,0,0),(2,0,2),(2,2,0),(2,2,2)\}$. Union has 15 elements. The 12 elements with both 1 and 2 are: everything else, i.e., elements containing at least one 1 and at least one 2.

These are: $(1,2,0),(1,0,2),(0,1,2),(2,1,0),(2,0,1),(0,2,1),(1,2,1),(1,2,2),(2,1,1),(2,1,2),(1,1,2),(2,2,1)$... let me list them properly.

Elements with at least one 1 and at least one 2: I need to enumerate. An element $(a,b,c) \in \mathbb{Z}_3^3$ has at least one coordinate = 1 and at least one coordinate = 2.

Possible patterns (multisets of values):
- One 1, one 2, one 0: permutations of (0,1,2): 6 elements.
- One 1, two 2s: permutations of (1,2,2): 3 elements.
- Two 1s, one 2: permutations of (1,1,2): 3 elements.
Total: 6 + 3 + 3 = 12. ✓

Now, can 8 of these (plus 0) form a subgroup? A subgroup of order 9 in $\mathbb{Z}_3^3$ is a 2-dimensional subspace. It's determined by 2 generators.

Let me think about which 2-dimensional subspaces work. A 2D subspace has 9 elements (including 0), so 8 nonzero. We need all 8 to be among the 12 "good" elements.

The 2D subspaces of $\mathbb{Z}_3^3$ correspond to planes through the origin. There are $\frac{3^3 - 1}{3 - 1} \cdot \frac{3^3 - 3}{3^2 - 3} / 2! = \frac{26}{2} \cdot \frac{24}{6} / 2 = 13 \cdot 4 / 2 = 26$... actually the number of 2D subspaces of $\mathbb{F}_3^3$ is the Gaussian binomial $\binom{3}{2}_3 = \frac{(3^3-1)(3^2-1)}{(3^2-1)(3-1)} = \frac{26 \cdot 8}{8 \cdot 2} = \frac{26}{2} = 13$.

Each 2D subspace has 8 nonzero elements. We need all 8 to be "good" (have both 1 and 2). The 12 good elements need to contain a full 2D subspace's worth (8 elements).

A 2D subspace is the kernel of a nonzero linear functional $\ell: \mathbb{F}_3^3 \to \mathbb{F}_3$, i.e., $\{x : \ell(x) = 0\}$ for some nonzero $\ell$, up to scaling. There are $(3^3 - 1)/(3-1) = 13$ such functionals up to scaling, giving 13 planes.

Let me check the plane $\{x : x_1 + x_2 + x_3 = 0\}$. Elements: $(0,0,0), (0,1,2), (0,2,1), (1,0,2), (1,1,1), (1,2,0), (2,0,1), (2,1,0), (2,2,2)$. Nonzero: $(0,1,2), (0,2,1), (1,0,2), (1,1,1), (1,2,0), (2,0,1), (2,1,0), (2,2,2)$. Is $(1,1,1)$ good? It has 1s but no 2. ✗. So this plane doesn't work.

Plane $\{x : x_1 + x_2 + 2x_3 = 0\}$, i.e., $x_1 + x_2 - x_3 = 0$, i.e., $x_3 = x_1 + x_2$. Elements: $(a, b, a+b)$ for $a, b \in \mathbb{F}_3$.
- $(0,0,0)$: 0
- $(0,1,1)$: only 0,1 ✗
- $(0,2,2)$: only 0,2 ✗

Doesn't work.

Plane $\{x : x_1 + 2x_2 + 0 \cdot x_3 = 0\}$, i.e., $x_1 = x_2$. Elements: $(a, a, c)$.
- $(0,0,0), (0,0,1), (0,0,2), (1,1,0), (1,1,1), (1,1,2), (2,2,0), (2,2,1), (2,2,2)$.
- $(0,0,1)$: only 0,1 ✗.

It seems like every 2D subspace of $\mathbb{F}_3^3$ contains an element in $\{0,1\}^3 \setminus \{0\}$ or $\{0,2\}^3 \setminus \{0\}$. Let me verify this claim.

A 2D subspace (plane) in $\mathbb{F}_3^3$ contains $9 - 1 = 8$ nonzero elements. The "bad" elements (in $\{0,1\}^3 \cup \{0,2\}^3 \setminus \{0\}$) number $15 - 1 = 14$. The "good" elements number 12. 

If a plane has all 8 nonzero elements good, then it uses 8 of the 12 good elements. The remaining 4 good elements and 14 bad elements are outside the plane (the plane has $27 - 9 = 18$ elements outside).

Is it possible for a plane to avoid all 14 bad nonzero elements? The 14 bad elements are in $\{0,1\}^3 \cup \{0,2\}^3 \setminus \{0\}$. 

$\{0,1\}^3 \setminus \{0\}$ has 7 elements, $\{0,2\}^3 \setminus \{0\}$ has 7 elements. A plane has 8 nonzero elements. For the plane to avoid all 14 bad elements, all 8 nonzero elements must be among the 12 good ones.

Consider the restriction of the plane to $\{0,1\}^3$. The plane is $\{x : \ell(x) = 0\}$ for some linear functional $\ell$. The elements of $\{0,1\}^3$ in the plane are $\{x \in \{0,1\}^3 : \ell(x) = 0\}$. This is a subset of $\{0,1\}^3$ that's a "subcube" intersected with a hyperplane. 

$\ell(x) = a_1 x_1 + a_2 x_2 + a_3 x_3 = 0$ for $x \in \{0,1\}^3$. The zero element is always in. We need no other element of $\{0,1\}^3$ to be in the plane (otherwise it's a bad element in the plane). So we need $\ell(x) \neq 0$ for all $x \in \{0,1\}^3 \setminus \{0\}$.

Similarly, $\ell(x) \neq 0$ for all $x \in \{0,2\}^3 \setminus \{0\}$, i.e., $\ell(2y) = 2\ell(y) \neq 0$ for $y \in \{0,1\}^3 \setminus \{0\}$, which is the same as $\ell(y) \neq 0$ for $y \in \{0,1\}^3 \setminus \{0\}$.

So we need: $\ell(x) \neq 0$ for all $x \in \{0,1\}^3 \setminus \{0\}$, where $\ell(x) = a_1 x_1 + a_2 x_2 + a_3 x_3$ and $a_i \in \mathbb{F}_3$ (not all zero).

The elements of $\{0,1\}^3 \setminus \{0\}$ are: $(1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1), (1,1,1)$.

We need:
- $a_1 \neq 0$
- $a_2 \neq 0$
- $a_3 \neq 0$
- $a_1 + a_2 \neq 0$
- $a_1 + a_3 \neq 0$
- $a_2 + a_3 \neq 0$
- $a_1 + a_2 + a_3 \neq 0$

With $a_i \in \{1, 2\}$ (since $a_i \neq 0$):
- If all $a_i = 1$: $a_1 + a_2 = 2 \neq 0$ ✓, $a_1 + a_2 + a_3 = 3 = 0$ ✗.
- If all $a_i = 2$: $a_1 + a_2 = 4 = 1 \neq 0$ ✓, $a_1 + a_2 + a_3 = 6 = 0$ ✗.
- Two 1s, one 2: say $a_1 = a_2 = 1, a_3 = 2$. $a_1 + a_2 = 2 \neq 0$ ✓, $a_1 + a_3 = 0$ ✗.
- Two 2s, one 1: say $a_1 = a_2 = 2, a_3 = 1$. $a_1 + a_2 = 4 = 1 \neq 0$ ✓, $a_1 + a_3 = 0$ ✗.

So in all cases, at least one condition fails. Therefore, no plane in $\mathbb{F}_3^3$ avoids all bad elements. So no subgroup of order 9 works for $n = 3$.

So for $n = 3$, the maximum subgroup that works has order 3 (a 1D subspace with a good generator). But can we do better with a non-subgroup construction?

Let me think about $n = 3$ more carefully. We want the maximum set $S \subseteq \mathbb{Z}_3^3$ such that all pairwise differences have at least one 1 and at least one 2.

Let me try to find a large set by computer-like reasoning.

The 12 good elements (with both 1 and 2) are:
Type (0,1,2) permutations: $(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)$ — 6 elements.
Type (1,1,2) permutations: $(1,1,2), (1,2,1), (2,1,1)$ — 3 elements.
Type (1,2,2) permutations: $(1,2,2), (2,1,2), (2,2,1)$ — 3 elements.

We need a set $S$ where all pairwise differences are good (have both 1 and 2). Note that $S$ can include elements outside the 12 good ones (e.g., $(0,0,0)$), as long as all pairwise differences are good.

Actually, $S$ can include any elements of $\mathbb{Z}_3^3$; the constraint is only on differences.

Let me try $S = \{(0,0,0), (1,2,0), (2,1,0)\}$. Differences: $(1,2,0), (2,1,0), (1,2,0)$. All have both 1 and 2 ✓. Size 3.

Can we add more? Try adding $(0,1,2)$: differences with $(0,0,0)$: $(0,1,2)$ ✓; with $(1,2,0)$: $(0,1,2) - (1,2,0) = (2,2,2)$, only 2s, no 1 ✗. So can't add $(0,1,2)$.

Try adding $(1,0,2)$: with $(0,0,0)$: $(1,0,2)$ ✓; with $(1,2,0)$: $(0,1,2)$ ✓; with $(2,1,0)$: $(2,2,2)$ ✗.

Try adding $(2,0,1)$: with $(0,0,0)$: $(2,0,1)$ ✓; with $(1,2,0)$: $(1,1,1)$ ✗.

Try adding $(0,2,1)$: with $(0,0,0)$: $(0,2,1)$ ✓; with $(1,2,0)$: $(2,0,1)$ ✓; with $(2,1,0)$: $(1,1,2)$ ✓. All good! So $S = \{(0,0,0), (1,2,0), (2,1,0), (0,2,1)\}$, size 4.

Can we add a 5th? Try $(0,1,2)$: with $(0,0,0)$: $(0,1,2)$ ✓; with $(1,2,0)$: $(2,2,2)$ ✗. No.

Try $(2,0,1)$: with $(0,0,0)$: $(2,0,1)$ ✓; with $(1,2,0)$: $(1,1,1)$ ✗. No.

Try $(1,0,2)$: with $(0,0,0)$: $(1,0,2)$ ✓; with $(1,2,0)$: $(0,1,2)$ ✓; with $(2,1,0)$: $(2,2,2)$ ✗. No.

Try $(2,2,1)$: with $(0,0,0)$: $(2,2,1)$ ✓; with $(1,2,0)$: $(1,0,1)$ ✗ (only 0,1). No.

Try $(1,1,2)$: with $(0,0,0)$: $(1,1,2)$ ✓; with $(1,2,0)$: $(0,2,2)$ ✗. No.

Try $(2,1,1)$: with $(0,0,0)$: $(2,1,1)$ ✓; with $(1,2,0)$: $(1,2,1)$ ✓; with $(2,1,0)$: $(0,0,1)$ ✗. No.

Try $(1,2,1)$: with $(0,0,0)$: $(1,2,1)$ ✓; with $(1,2,0)$: $(0,0,1)$ ✗. No.

Try $(2,1,2)$: with $(0,0,0)$: $(2,1,2)$ ✓; with $(1,2,0)$: $(1,2,2)$ ✓; with $(2,1,0)$: $(0,0,2)$ ✗. No.

Try $(1,2,2)$: with $(0,0,0)$: $(1,2,2)$ ✓; with $(1,2,0)$: $(0,0,2)$ ✗. No.

Try $(2,2,1)$: already tried. No.

Hmm, seems like 4 might be the max for $n=3$ with this particular starting set. But maybe a different set does better?

Let me try a different approach. Let me try to use a "product" construction.

For $n = 2$, max = 3. For $n = 3$, let me try to see if we can get 6 or more.

Actually, let me think about this problem from a higher level. 

The problem is asking for the maximum size of a set $S \subseteq \mathbb{Z}_3^n$ such that for all distinct $a, b \in S$, $a - b$ has at least one coordinate $\equiv 1$ and at least one $\equiv 2 \pmod{3}$.

This is equivalent to: $S$ is a "clique" in the graph where two elements are connected iff their difference has both a 1 and a 2.

Let me think about this using the concept of a "covering array" or "qualitative independence."

Actually, this reminds me of the concept of **qualitatively independent** partitions. Two partitions of a set are qualitatively independent if every cell of their join is nonempty. But I'm not sure that directly applies.

Let me think about another approach. Consider the following reformulation:

For each pair $(a, b)$, define $I_1(a,b) = \{i : a_i - b_i \equiv 1\}$ and $I_2(a,b) = \{i : a_i - b_i \equiv 2\}$. We need $I_1 \neq \emptyset$ and $I_2 \neq \emptyset$.

Now, consider the "type" of a sequence: the number of 0s, 1s, and 2s. Let $n_0(x), n_1(x), n_2(x)$ be the counts.

Hmm, this doesn't directly give a clean bound.

Let me think about the problem differently. Let me consider the following approach using a "tensor/product" structure.

**Product construction:** If $S_1$ works for $n_1$ and $S_2$ works for $n_2$, does $S_1 \times S_2$ work for $n_1 + n_2$?

For $(a_1, a_2), (b_1, b_2) \in S_1 \times S_2$, the difference is $(a_1 - b_1, a_2 - b_2)$. We need this to have at least one 1 and at least one 2. If $a_1 \neq b_1$, then $a_1 - b_1$ has at least one 1 and at least one 2 (since $S_1$ works), so the combined difference does too. If $a_1 = b_1$ but $a_2 \neq b_2$, then $a_2 - b_2$ has at least one 1 and at least one 2. So yes, the product construction works!

So $f(n_1 + n_2) \geq f(n_1) \cdot f(n_2)$ where $f(n)$ is the maximum for $n$ coordinates.

We have $f(1) = 1$, $f(2) = 3$.

$f(3) \geq f(2) \cdot f(1) = 3$. But we found 4 for $n=3$, so the product construction is not always optimal.

$f(4) \geq f(2) \cdot f(2) = 9$.

$f(10) \geq f(2)^5 = 3^5 = 243$ (by taking the product of 5 copies of the $n=2$ solution).

Also $f(10) \geq f(4) \cdot f(4) \cdot f(2) \geq 9 \cdot 9 \cdot 3 = 243$.

And $f(10) \geq f(3) \cdot f(3) \cdot f(4) \geq 4 \cdot 4 \cdot 9 = 144$, which is worse.

$f(10) \geq f(2)^5 = 243$.

But we also have the binary antichain giving 252. So 252 > 243.

Can we combine these? $f(10) \geq \max(252, 243) = 252$ from these constructions.

But maybe there are better constructions. Let me think about whether we can beat 252.

Let me reconsider the $n = 3$ case. We found 4, which is better than $f(2) \cdot f(1) = 3$ and better than $\binom{3}{1} = 3$ (binary antichain). What's the actual maximum for $n = 3$?

Let me try harder to find a set of size 5 or 6 for $n = 3$.

Actually, let me think about this more carefully. Let me consider the problem as a maximum clique problem and try to reason about it.

For $n = 3$, the graph has $27$ vertices. Two vertices $a, b$ are connected iff $a - b$ has at least one 1 and at least one 2. The "bad" differences are those in $\{0,1\}^3 \cup \{0,2\}^3 \setminus \{0\}$, which has 14 elements. So each vertex has $26 - 14 = 12$ neighbors.

We want the maximum clique. By the Hoffman bound or other methods...

Actually, let me just try to find a clique of size 5 or 6 by hand.

Let me use the set $\{(0,0,0), (1,2,0), (2,1,0), (0,2,1)\}$ (size 4) and try harder to extend.

Differences from $(0,0,0)$: $(1,2,0), (2,1,0), (0,2,1)$.
Differences from $(1,2,0)$: to others: $(2,1,0), (0,2,1), (2,0,1)$ (i.e., $(1,2,0)-(0,2,1) = (1,0,2)$... wait let me recompute.

$(1,2,0) - (0,0,0) = (1,2,0)$ ✓
$(1,2,0) - (2,1,0) = (2,1,0)$ ✓ (since $1-2=-1=2, 2-1=1, 0-0=0$)
$(1,2,0) - (0,2,1) = (1,0,2)$ ✓ (since $1-0=1, 2-2=0, 0-1=2$)
$(2,1,0) - (0,0,0) = (2,1,0)$ ✓
$(2,1,0) - (1,2,0) = (1,2,0)$ ✓
$(2,1,0) - (0,2,1) = (2,2,2)$ ✗!

Wait, $(2,1,0) - (0,2,1) = (2, 1-2, 0-1) = (2, -1, -1) = (2, 2, 2) \pmod 3$. This has only 2s, no 1. So this is BAD!

I made an error earlier. Let me recheck. I claimed $S = \{(0,0,0), (1,2,0), (2,1,0), (0,2,1)\}$ works, but $(2,1,0) - (0,2,1) = (2,2,2)$ which is bad. So this set does NOT work!

Let me redo this more carefully.

$(0,2,1) - (2,1,0) = (0-2, 2-1, 1-0) = (1, 1, 1) \pmod 3$. This has only 1s, no 2. Also bad!

So my earlier check was wrong. Let me recheck: I had said "with $(2,1,0)$: $(1,1,2)$" but that's $(0,2,1) - (2,1,0) = (-2, 1, 1) = (1, 1, 1)$. I made an arithmetic error. So the set of size 4 doesn't work.

Let me be more careful. For $n = 3$, let me try to find the maximum clique.

Let me start with $\{(0,0,0)\}$ and add elements one by one, checking all pairwise differences.

The neighbors of $(0,0,0)$ are the 12 "good" elements (those with at least one 1 and at least one 2).

Good elements: 
$(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0), (1,1,2), (1,2,1), (2,1,1), (1,2,2), (2,1,2), (2,2,1)$.

Now, among these 12, I need to find a clique (all pairwise differences are good).

Take $(1,2,0)$. Its differences with other good elements:
- $(0,1,2)$: $(1,2,0)-(0,1,2) = (1,1,1)$ — bad (only 1s).
- $(0,2,1)$: $(1,2,0)-(0,2,1) = (1,0,2)$ — good ✓.
- $(1,0,2)$: $(1,2,0)-(1,0,2) = (0,2,1)$ — good ✓.
- $(2,0,1)$: $(1,2,0)-(2,0,1) = (2,2,2)$ — bad.
- $(2,1,0)$: $(1,2,0)-(2,1,0) = (2,1,0)$ — good ✓.
- $(1,1,2)$: $(1,2,0)-(1,1,2) = (0,1,1)$ — bad (only 0,1).
- $(1,2,1)$: $(1,2,0)-(1,2,1) = (0,0,2)$ — bad.
- $(2,1,1)$: $(1,2,0)-(2,1,1) = (2,1,2)$ — good ✓.
- $(1,2,2)$: $(1,2,0)-(1,2,2) = (0,0,1)$ — bad.
- $(2,1,2)$: $(1,2,0)-(2,1,2) = (2,1,1)$ — good ✓.
- $(2,2,1)$: $(1,2,0)-(2,2,1) = (2,0,2)$ — bad.

So $(1,2,0)$'s good neighbors among the 12: $(0,2,1), (1,0,2), (2,1,0), (2,1,1), (2,1,2)$. That's 5.

Now I need a clique among $\{(0,0,0), (1,2,0)\} \cup \text{these 5}$. The 5 candidates are $(0,2,1), (1,0,2), (2,1,0), (2,1,1), (2,1,2)$. I need all pairwise differences among these 5 (and with $(1,2,0)$, already checked) to be good.

Let me check pairwise:
- $(0,2,1)$ vs $(1,0,2)$: $(0,2,1)-(1,0,2) = (2,2,2)$ — bad.
- $(0,2,1)$ vs $(2,1,0)$: $(0,2,1)-(2,1,0) = (1,1,1)$ — bad.
- $(0,2,1)$ vs $(2,1,1)$: $(0,2,1)-(2,1,1) = (1,1,0)$ — bad.
- $(0,2,1)$ vs $(2,1,2)$: $(0,2,1)-(2,1,2) = (1,1,2)$ — good ✓.
- $(1,0,2)$ vs $(2,1,0)$: $(1,0,2)-(2,1,0) = (2,2,2)$ — bad.
- $(1,0,2)$ vs $(2,1,1)$: $(1,0,2)-(2,1,1) = (2,2,1)$ — good ✓.
- $(1,0,2)$ vs $(2,1,2)$: $(1,0,2)-(2,1,2) = (2,2,0)$ — bad.
- $(2,1,0)$ vs $(2,1,1)$: $(2,1,0)-(2,1,1) = (0,0,2)$ — bad.
- $(2,1,0)$ vs $(2,1,2)$: $(2,1,0)-(2,1,2) = (0,0,1)$ — bad.
- $(2,1,1)$ vs $(2,1,2)$: $(2,1,1)-(2,1,2) = (0,0,2)$ — bad.

So the good pairs among the 5: only $\{(0,2,1), (2,1,2)\}$ and $\{(1,0,2), (2,1,1)\}$.

So the maximum clique containing $\{(0,0,0), (1,2,0)\}$ is at most $\{(0,0,0), (1,2,0), (0,2,1), (2,1,2)\}$ (size 4) or $\{(0,0,0), (1,2,0), (1,0,2), (2,1,1)\}$ (size 4).

Let me verify $\{(0,0,0), (1,2,0), (0,2,1), (2,1,2)\}$:
- $(0,0,0)$ vs all: differences are $(1,2,0), (0,2,1), (2,1,2)$ — all good ✓.
- $(1,2,0)$ vs $(0,2,1)$: $(1,0,2)$ — good ✓.
- $(1,2,0)$ vs $(2,1,2)$: $(2,1,1)$ — good ✓.
- $(0,2,1)$ vs $(2,1,2)$: $(1,1,2)$ — good ✓.
All good! Size 4. ✓

Can we extend to 5? We need an element $x$ such that $x - (0,0,0)$, $x - (1,2,0)$, $x - (0,2,1)$, $x - (2,1,2)$ are all good.

$x - (0,0,0) = x$ must be good.
$x - (1,2,0)$ must be good.
$x - (0,2,1)$ must be good.
$x - (2,1,2)$ must be good.

From the analysis, $x$ must be a good neighbor of $(1,2,0)$, so $x \in \{(0,2,1), (1,0,2), (2,1,0), (2,1,1), (2,1,2)\}$. But $(0,2,1)$ and $(2,1,2)$ are already in the set. So $x \in \{(1,0,2), (2,1,0), (2,1,1)\}$.

Check $x = (1,0,2)$: $x - (0,2,1) = (1,1,1)$ — bad. ✗.
Check $x = (2,1,0)$: $x - (0,2,1) = (2,2,2)$ — bad. ✗.
Check $x = (2,1,1)$: $x - (0,2,1) = (2,2,0)$ — bad. ✗.

So can't extend to 5. But maybe a completely different starting point gives 5?

Let me try starting with a different element. Due to the symmetry of the problem (we can translate and apply certain symmetries), let me try starting with elements of different types.

Actually, the problem has a lot of symmetry: $\mathbb{Z}_3^n$ acts on itself by translation, and the automorphism group includes coordinate permutations and the map $x \mapsto 2x$ (which swaps 1 and 2). Also, we can apply independent cyclic shifts to each coordinate: $x_i \mapsto x_i + c_i$ for any $c \in \mathbb{Z}_3^n$. Wait, translation by $c$ sends $a \mapsto a + c$, and differences are preserved: $(a+c) - (b+c) = a - b$. So translation doesn't change differences. So WLOG we can assume $(0,0,0) \in S$.

Also, the map $x \mapsto Mx$ for $M \in GL(n, \mathbb{F}_3)$ that preserves the "good" property... actually, the good property depends on the specific values 1 and 2, so only specific symmetries work. The symmetry $x \mapsto 2x$ sends 1 to 2 and 2 to 1, so it preserves "having both 1 and 2." Also, coordinate permutations preserve the property. And adding a constant to a specific coordinate: $x_i \mapsto x_i + c$ for all elements — this is translation, already covered.

So WLOG $(0,0,0) \in S$, and we need a clique among the 12 good elements.

Let me try to find the maximum clique among the 12 good elements (as a graph where edges connect elements with good differences).

I already found that starting from $(1,2,0)$, the max clique is 3 (among the 12, giving total 4 with $(0,0,0)$).

Let me try starting from a type-(1,1,2) element, say $(1,1,2)$.

$(1,1,2)$'s differences with all 12 good elements (excluding itself):
- $(0,1,2)$: $(1,0,0)$ — bad.
- $(0,2,1)$: $(1,2,1)$ — good ✓.
- $(1,0,2)$: $(0,1,0)$ — bad.
- $(1,2,0)$: $(0,2,2)$ — bad.
- $(2,0,1)$: $(2,1,1)$ — good ✓.
- $(2,1,0)$: $(2,0,2)$ — bad.
- $(1,2,1)$: $(0,2,1)$ — good ✓.
- $(2,1,1)$: $(2,0,1)$ — good ✓.
- $(1,2,2)$: $(0,2,0)$ — bad.
- $(2,1,2)$: $(2,0,0)$ — bad.
- $(2,2,1)$: $(2,2,1)$ — good ✓.

Good neighbors of $(1,1,2)$: $(0,2,1), (2,0,1), (1,2,1), (2,1,1), (2,2,1)$. 5 elements.

Now find a clique among these 5:
- $(0,2,1)$ vs $(2,0,1)$: $(0,2,1)-(2,0,1) = (1,2,0)$ — good ✓.
- $(0,2,1)$ vs $(1,2,1)$: $(0,2,1)-(1,2,1) = (2,0,0)$ — bad.
- $(0,2,1)$ vs $(2,1,1)$: $(0,2,1)-(2,1,1) = (1,1,0)$ — bad.
- $(0,2,1)$ vs $(2,2,1)$: $(0,2,1)-(2,2,1) = (1,0,0)$ — bad.
- $(2,0,1)$ vs $(1,2,1)$: $(2,0,1)-(1,2,1) = (1,1,0)$ — bad.
- $(2,0,1)$ vs $(2,1,1)$: $(2,0,1)-(2,1,1) = (0,2,0)$ — bad.
- $(2,0,1)$ vs $(2,2,1)$: $(2,0,1)-(2,2,1) = (0,1,0)$ — bad.
- $(1,2,1)$ vs $(2,1,1)$: $(1,2,1)-(2,1,1) = (2,1,0)$ — good ✓.
- $(1,2,1)$ vs $(2,2,1)$: $(1,2,1)-(2,2,1) = (2,0,0)$ — bad.
- $(2,1,1)$ vs $(2,2,1)$: $(2,1,1)-(2,2,1) = (0,2,0)$ — bad.

Good pairs: $\{(0,2,1), (2,0,1)\}$ and $\{(1,2,1), (2,1,1)\}$.

So max clique among these 5 is 2, giving total $1 + 1 + 2 = 4$ (including $(0,0,0)$ and $(1,1,2)$).

Let me try $\{(0,0,0), (1,1,2), (0,2,1), (2,0,1)\}$:
- $(0,2,1) - (2,0,1) = (1,2,0)$ — good ✓.
All pairwise differences good? Let me check all:
- $(1,1,2), (0,2,1), (2,0,1)$ are all good (differences from 0).
- $(1,1,2)-(0,2,1) = (1,2,1)$ — good ✓.
- $(1,1,2)-(2,0,1) = (2,1,1)$ — good ✓.
- $(0,2,1)-(2,0,1) = (1,2,0)$ — good ✓.
All good! Size 4. Can we extend?

Need $x$ good, $x-(1,1,2)$ good, $x-(0,2,1)$ good, $x-(2,0,1)$ good.

$x$ must be a good neighbor of $(1,1,2)$: $x \in \{(0,2,1), (2,0,1), (1,2,1), (2,1,1), (2,2,1)\}$. Remove $(0,2,1), (2,0,1)$ (already in set): $x \in \{(1,2,1), (2,1,1), (2,2,1)\}$.

- $x = (1,2,1)$: $x - (0,2,1) = (1,0,0)$ — bad. ✗.
- $x = (2,1,1)$: $x - (0,2,1) = (2,2,0)$ — bad. ✗.
- $x = (2,2,1)$: $x - (0,2,1) = (2,0,0)$ — bad. ✗.

Can't extend. So size 4 again.

Let me try a type-(1,2,2) element, say $(1,2,2)$.

$(1,2,2)$'s good neighbors among the 12:
- $(0,1,2)$: $(1,1,0)$ — bad.
- $(0,2,1)$: $(1,0,1)$ — bad.
- $(1,0,2)$: $(0,2,0)$ — bad.
- $(1,2,0)$: $(0,0,2)$ — bad.
- $(2,0,1)$: $(2,2,1)$ — good ✓.
- $(2,1,0)$: $(2,1,2)$ — good ✓.
- $(1,1,2)$: $(0,1,0)$ — bad.
- $(2,1,1)$: $(2,1,1)$ — good ✓.
- $(1,2,1)$: $(0,0,1)$ — bad.
- $(2,1,2)$: $(2,1,0)$ — good ✓.
- $(2,2,1)$: $(2,0,1)$ — good ✓.

Good neighbors: $(2,0,1), (2,1,0), (2,1,1), (2,1,2), (2,2,1)$. 5 elements.

Pairwise among these 5:
- $(2,0,1)$ vs $(2,1,0)$: $(0,2,1)$ — good ✓.
- $(2,0,1)$ vs $(2,1,1)$: $(0,2,0)$ — bad.
- $(2,0,1)$ vs $(2,1,2)$: $(0,2,2)$ — bad.
- $(2,0,1)$ vs $(2,2,1)$: $(0,1,0)$ — bad.
- $(2,1,0)$ vs $(2,1,1)$: $(0,0,2)$ — bad.
- $(2,1,0)$ vs $(2,1,2)$: $(0,0,1)$ — bad.
- $(2,1,0)$ vs $(2,2,1)$: $(0,2,2)$ — bad.
- $(2,1,1)$ vs $(2,1,2)$: $(0,0,2)$ — bad.
- $(2,1,1)$ vs $(2,2,1)$: $(0,2,0)$ — bad.
- $(2,1,2)$ vs $(2,2,1)$: $(0,2,1)$ — good ✓.

Good pairs: $\{(2,0,1), (2,1,0)\}$ and $\{(2,1,2), (2,2,1)\}$.

Max clique 2, total 4.

It seems like for $n=3$, the maximum is 4. Let me try one more approach: a type-(0,1,2) element, say $(0,1,2)$.

$(0,1,2)$'s good neighbors:
- $(0,2,1)$: $(0,2,1)$ — good ✓.
- $(1,0,2)$: $(2,1,0)$ — good ✓.
- $(1,2,0)$: $(2,2,2)$ — bad.
- $(2,0,1)$: $(1,1,1)$ — bad.
- $(2,1,0)$: $(1,0,2)$ — good ✓.
- $(1,1,2)$: $(2,0,0)$ — bad.
- $(1,2,1)$: $(2,2,1)$ — good ✓.
- $(2,1,1)$: $(1,0,1)$ — bad.
- $(1,2,2)$: $(2,2,0)$ — bad.
- $(2,1,2)$: $(1,0,0)$ — bad.
- $(2,2,1)$: $(1,2,2)$ — good ✓.

Good neighbors: $(0,2,1), (1,0,2), (2,1,0), (1,2,1), (2,2,1)$. 5 elements.

Pairwise:
- $(0,2,1)$ vs $(1,0,2)$: $(2,2,2)$ — bad.
- $(0,2,1)$ vs $(2,1,0)$: $(1,1,1)$ — bad.
- $(0,2,1)$ vs $(1,2,1)$: $(2,0,0)$ — bad.
- $(0,2,1)$ vs $(2,2,1)$: $(1,0,0)$ — bad.
- $(1,0,2)$ vs $(2,1,0)$: $(2,2,2)$ — bad.
- $(1,0,2)$ vs $(1,2,1)$: $(0,1,1)$ — bad.
- $(1,0,2)$ vs $(2,2,1)$: $(2,1,1)$ — good ✓.
- $(2,1,0)$ vs $(1,2,1)$: $(1,2,2)$ — good ✓.
- $(2,1,0)$ vs $(2,2,1)$: $(0,2,2)$ — bad.
- $(1,2,1)$ vs $(2,2,1)$: $(2,0,0)$ — bad.

Good pairs: $\{(1,0,2), (2,2,1)\}$ and $\{(2,1,0), (1,2,1)\}$.

Max clique 2, total 4.

So for $n = 3$, the maximum appears to be 4. Let me see if there's a clique of size 5 by trying a different approach.

Actually, I realize I should check: is there a clique of size 4 among the 12 good elements (giving total 5 with $(0,0,0)$)?

From the analysis, the maximum clique among the neighbors of any single good element is 2 (among the 5 neighbors). But a clique of size 4 among the 12 doesn't need to include any particular element. Let me think about this differently.

Actually, I've been checking cliques that include $(0,0,0)$ and one specific good element. But maybe there's a clique of size 4 among the 12 good elements that doesn't include any of the elements I've been checking.

Hmm, but by symmetry, I've checked representatives of each type (type (0,1,2), type (1,1,2), type (1,2,2)). Due to the symmetries of the problem (coordinate permutations and the $x \mapsto 2x$ map), these cover all cases up to symmetry. And in each case, the max clique among the neighbors is 2, giving total 4.

But wait, I need to check if there's a clique of size 4 among the 12 that doesn't include any specific element I checked. The issue is that I'm checking "what's the max clique containing $(0,0,0)$ and element $x$," and for each type of $x$, I get 4. But maybe there's a clique of size 5 containing $(0,0,0)$ where the 4 good elements form a clique.

A clique of size 4 among the 12 good elements: I need 4 elements, all pairwise differences good. From my analysis, for each starting element, the max clique among its neighbors is 2. So any clique of size 4 among the 12 would need each element to have at least 3 neighbors in the clique, but each element has at most a clique of size 2 among its neighbors. Wait, that's not quite right—the clique of size 4 means each element has 3 neighbors in the clique, and those 3 form a clique of size 3 among the element's neighbors. But I showed the max clique among any element's neighbors is 2. So no clique of size 4 exists among the 12.

Therefore, for $n = 3$, the maximum is 4 (including $(0,0,0)$, so 3 good elements forming a clique of size 3 among the 12, plus $(0,0,0)$).

Wait, I showed max clique among neighbors of any element is 2, so the max clique among the 12 is 3 (an element plus 2 of its neighbors that form a pair). Then total with $(0,0,0)$ is 4. And I showed this is achievable. So $f(3) = 4$.

Hmm wait, I need to be more careful. The max clique among the 12 good elements: I showed that for any element $x$ among the 12, the max clique in $x$'s neighborhood (among the 12) is 2. This means the max clique among the 12 is at most 3 (since any clique of size 4 would have each vertex with 3 neighbors in the clique, but max is 2). And I found cliques of size 3 (e.g., $\{(1,2,0), (0,2,1), (2,1,2)\}$ — let me verify: $(1,2,0)-(0,2,1) = (1,0,2)$ good ✓, $(1,2,0)-(2,1,2) = (2,1,1)$ good ✓, $(0,2,1)-(2,1,2) = (1,1,2)$ good ✓). So max clique among the 12 is 3, and $f(3) = 4$.

So we have:
- $f(1) = 1$
- $f(2) = 3$
- $f(3) = 4$
- $f(4) \geq f(2) \cdot f(2) = 9$
- $f(4) \geq f(3) \cdot f(1) = 4$
- $f(10) \geq f(2)^5 = 243$
- $f(10) \geq f(4) \cdot f(4) \cdot f(2) \geq 9 \cdot 9 \cdot 3 = 243$

Also, the binary antichain gives $f(10) \geq \binom{10}{5} = 252$.

Can we beat 252? Let me think about better constructions.

**Better construction idea:** Combine the binary antichain with the ternary construction.

For $n = 10 = 5 + 5$, we could use $f(5) \cdot f(5)$. What's $f(5)$?

$f(5) \geq f(2) \cdot f(3) = 3 \cdot 4 = 12$.
$f(5) \geq \binom{5}{2} = 10$ (binary antichain).

So $f(5) \geq 12$, and $f(10) \geq 12^2 = 144 < 252$.

$f(10) \geq f(2)^5 = 243 < 252$.

What about $f(10) \geq f(4) \cdot f(6)$? $f(4) \geq 9$, $f(6) \geq f(3)^2 = 16$ or $f(6) \geq f(2)^3 = 27$ or $f(6) \geq \binom{6}{3} = 20$. So $f(6) \geq 27$. $f(10) \geq 9 \cdot 27 = 243$.

$f(10) \geq f(2) \cdot f(8)$. $f(8) \geq f(2)^4 = 81$ or $f(8) \geq \binom{8}{4} = 70$. So $f(8) \geq 81$. $f(10) \geq 3 \cdot 81 = 243$.

So the product constructions all give 243, while the binary antichain gives 252. Can we do better than both?

Let me think about a hybrid construction. What if we use a combination of binary and ternary coordinates?

**Hybrid construction:** Split the 10 coordinates into two groups: $k$ "binary" coordinates (using only values 0, 1) and $10 - k$ "ternary" coordinates. On the binary coordinates, use an antichain; on the ternary coordinates, use a good code.

For two elements $(a_1, a_2)$ and $(b_1, b_2)$ where $a_1, b_1$ are binary and $a_2, b_2$ are ternary:
- If $a_1 \neq b_1$: the binary part gives a difference with at least one 1 (where $a_{1i} = 1, b_{1i} = 0$) and at least one 2 (where $a_{1i} = 0, b_{1i} = 1$), as long as the binary parts are incomparable. So the combined difference is good.
- If $a_1 = b_1$: the binary difference is all 0, so we need the ternary difference to be good. So the ternary parts must form a code where all pairwise differences are good.

So the construction is: take an antichain $A$ of subsets of $[k]$ (binary part), and for each element of $A$, assign a ternary codeword from a code $T$ on $10 - k$ coordinates. Two elements with the same binary part must have good ternary differences. Two elements with different binary parts automatically have good differences (from the binary part).

So the total size is $\
