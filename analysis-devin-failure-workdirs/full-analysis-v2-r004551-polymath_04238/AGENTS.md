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
  <problem_id>polymath_04238</problem_id>
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

Players \( A \) and \( B \) play a game on a blackboard that initially contains \( 2020 \) copies of the number 1. In every round, player \( A \) erases two numbers \( x \) and \( y \) from the blackboard, and then player \( B \) writes one of the numbers \( x+y \) and \( |x-y| \) on the blackboard. The game terminates as soon as, at the end of some round, one of the following holds:
(1) one of the numbers on the blackboard is larger than the sum of all other numbers;
(2) there are only zeros on the blackboard.

Player \( B \) must then give as many cookies to player \( A \) as there are numbers on the blackboard. Player \( A \) wants to get as many cookies as possible, whereas player \( B \) wants to give as few as possible. Determine the number of cookies that \( A \) receives if both players play optimally.

## Standard Solution

Solution. For a positive integer \( n \), we denote by \( S_{2}(n) \) the sum of digits in its binary representation. We prove that, if a board initially contains an even number \( n>1 \) of ones, then \( A \) can guarantee to obtain \( S_{2}(n) \), but not more, cookies. The binary representation of \( 2020 \) is \( 2020=\overline{11111100100}_{2} \), so \( S_{2}(2020)=7 \), and the answer follows.

A strategy for \( A \). At any round, while possible, \( A \) chooses two equal nonzero numbers on the board. Clearly, while \( A \) can make such a choice, the game does not terminate. On the other hand, \( A \) can follow this strategy unless the game has already terminated. Indeed, if \( A \) always chooses two equal numbers, then each number appearing on the board is either \( 0 \) or a power of \( 2 \) with a non-negative integer exponent, which can be easily proved using induction on the number of rounds. At the moment when \( A \) is unable to follow the strategy, all nonzero numbers on the board are distinct powers of \( 2 \). If the board contains at least one such power, then the largest of those powers is greater than the sum of the others. Otherwise, there are only zeros on the blackboard, in both cases the game terminates.

For every number on the board, define its range to be the number of ones it is obtained from. We can prove by induction on the number of rounds that for any nonzero number \( k \) written by \( B \), its range is \( k \), and for any zero written by \( B \), its range is a power of \( 2 \). Thus, at the end of each round, all the ranges are powers of two, and their sum is \( n \). Since \( S_{2}(a+b) \leq S_{2}(a)+S_{2}(b) \) for any positive integers \( a \) and \( b \), the number \( n \) cannot be represented as a sum of less than \( S_{2}(n) \) powers of 2. Thus, at the end of each round, the board contains at least \( S_{2}(n) \) numbers, while \( A \) follows the above strategy. So \( A \) can guarantee at least \( S_{2}(n) \) cookies for himself.

A strategy for \( B \). Denote \( s=S_{2}(n) \).
Let \( x_{1}, \ldots, x_{k} \) be the numbers on the board at some moment of the game after \( B \)'s turn or at the beginning of the game. Say that a collection of \( k \) signs \( \varepsilon_{1}, \ldots, \varepsilon_{k} \in\{+1,-1\} \) is balanced if

\[
\sum_{i=1}^{k} \varepsilon_{i} x_{i}=0
\]

We say that a situation on the board is good if \( 2^{s+1} \) does not divide the number of balanced collections. An appropriate strategy for \( B \) can be explained as follows: Perform a move so that the situation remains good, while it is possible. We intend to show that in this case \( B \) will not lose more than \( S_{2}(n) \) cookies. For this purpose, we prove several lemmas.

For a positive integer \( k \), denote by \( \nu_{2}(k) \) the exponent of the largest power of \( 2 \) that divides \( k \). Recall that, by Legendre's formula, \( \nu_{2}(n!)=n-S_{2}(n) \) for every positive integer \( n \).

Lemma 1. The initial situation is good.
Proof. In the initial configuration, the number of balanced collections is equal to \( \binom{n}{n / 2} \). We have

\[
\begin{aligned}
\nu_{2}\left(\binom{n}{n / 2}\right) & =\nu_{2}(n!)-2 \nu_{2}((n / 2)!) \\
& =\left(n-S_{2}(n)\right)-2\left(\frac{n}{2}-S_{2}(n / 2)\right)=S_{2}(n)=s
\end{aligned}
\]

Hence \( 2^{s+1} \) does not divide the number of balanced collections, as desired.

Lemma 2. \( B \) may play so that after each round the situation remains good.
Proof. Assume that the situation \(\left(x_{1}, \ldots, x_{k}\right)\) before a round is good, and that \( A \) erases two numbers, \( x_{p} \) and \( x_{q} \).

Let \( N \) be the number of all balanced collections, \( N_{+} \) be the number of those having \( \varepsilon_{p}=\varepsilon_{q} \), and \( N_{-} \) be the number of other balanced collections. Then \( N=N_{+}+N_{-} \). Now, if \( B \) replaces \( x_{p} \) and \( x_{q} \) by \( x_{p}+x_{q} \), then the number of balanced collections will become \( N_{+} \). If \( B \) replaces \( x_{p} \) and \( x_{q} \) by \(\left|x_{p}-x_{q}\right|\), then this number will become \( N_{-} \). Since \( 2^{s+1} \) does not divide \( N \), it does not divide one of the summands \( N_{+} \) and \( N_{-} \), hence \( B \) can reach a good situation after the round.

Lemma 3. Assume that the game terminates at a good situation. Then the board contains at most \( s \) numbers.
Proof. Suppose one of the numbers is greater than the sum of the other numbers. Then the number of balanced collections is \( 0 \) and hence divisible by \( 2^{s+1} \). Therefore, the situation is not good.

Then we have only zeros on the blackboard at the moment when the game terminates. If there are \( k \) of them, then the number of balanced collections is \( 2^{k} \). Since the situation is good, we have \( k \leq s \).

By Lemmas 1 and 2, \( B \) may act in such a way that they keep the situation good. By Lemma 3, when the game terminates, the board contains at most \( s \) numbers. This is what we aimed to prove.

\(\boxed{7}\)

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We start with 2020 copies of the number 1 on a blackboard. Each round:
- Player A erases two numbers x and y
- Player B writes either x+y or |x-y| on the blackboard

So the count decreases by 1 each round (remove 2, add 1).

The game terminates when:
(1) one number is larger than the sum of all others, OR
(2) all numbers are zeros.

Then B gives A as many cookies as there are numbers on the blackboard.

A wants to maximize cookies (keep many numbers), B wants to minimize (few numbers).

Let me think about invariants.

The sum of all numbers: if B writes x+y, sum unchanged. If B writes |x-y|, sum decreases by 2·min(x,y).

The parity: sum mod 2 is invariant! Because x+y and |x-y| have the same parity as x+y. Actually x+y ≡ |x-y| (mod 2) since x+y and x-y have same parity, and |x-y| ≡ x-y (mod 2). So sum mod 2 is invariant.

Initial sum = 2020, which is even. So sum is always even.

Number of numbers: starts at 2020, decreases by 1 each round. After k rounds, we have 2020-k numbers.

Termination condition (2): all zeros. Sum = 0, even. OK consistent.

Termination condition (1): one number > sum of others. Let total = S, largest = m, others sum = S - m. Condition: m > S - m, i.e., 2m > S.

A wants to maximize the number of numbers when game terminates. B wants to minimize.

Let me think about what B can force. B controls whether to add or subtract. B wants to reach a terminal state quickly (fewer rounds = more numbers remaining... wait, fewer rounds = more numbers remaining, but B wants fewer cookies = fewer numbers = more rounds).

Wait: more rounds = fewer numbers remaining = fewer cookies. So B wants to prolong the game (more rounds), A wants to end it quickly (fewer rounds = more numbers).

Hmm, actually A wants to end the game as quickly as possible to keep more numbers. B wants to prolong.

But A chooses which two numbers to erase. B chooses the operation.

Let me reconsider. A wants the game to terminate ASAP (to have many numbers left). B wants to avoid termination as long as possible (to have few numbers left).

But the game must terminate eventually (number of numbers decreases each round, and eventually... well if we reach 1 number, condition (1) is automatically satisfied since one number > sum of others = 0). Actually with 1 number left, that number > 0 (sum of others = 0), so condition (1) holds. Unless that number is 0, then condition (2) holds. Either way game ends with 1 number = 1 cookie.

So the game always terminates with at least 1 cookie. The question is how many.

Let me think about small cases and the structure.

Key insight: B wants to prevent condition (1) from happening. Condition (1) happens when one number exceeds the sum of all others. This is like the "triangle inequality" failing — if the largest number ≤ sum of all others, no number exceeds the sum of others (since largest is the candidate). So condition (1) is equivalent to: largest > (total - largest), i.e., 2·largest > total.

So as long as 2·(max) ≤ total, condition (1) doesn't trigger. B wants to keep the configuration "balanced" (no dominant number) to avoid (1), and avoid all-zeros to avoid (2).

A wants to create a dominant number or all zeros.

Let me think about the strategy.

A's tool: A picks two numbers to combine. If A picks x, y, B either makes x+y (a bigger number, potentially dominant) or |x-y| (smaller).

So A wants to create a dominant number. A would pick two large numbers and hope B is forced to add them. But B will subtract to keep things balanced.

Hmm, but |x-y| could be 0, contributing to condition (2).

Let me think about invariants more. 

Total sum S is even always. 

Consider the sum modulo something else? 

Let me think about the maximum possible value. Initially all 1s, sum 2020. The maximum any number can be is 2020 (if everything adds up). 

Let's think about what A can force. 

Suppose A repeatedly picks the two largest numbers. B subtracts to keep them small. But subtraction of two equal numbers gives 0.

Strategy for A: A wants to force a dominant number. 

Let me think differently. Let's consider the quantity: can A force condition (1)?

Consider A's strategy: always pick two equal numbers. If x = y, then x+y = 2x or |x-y| = 0. B chooses. If B adds, we get a bigger number (doubling). If B subtracts, we get 0.

If A keeps pairing equal numbers and B keeps subtracting, we get lots of zeros. Eventually all zeros → condition (2). But that takes many rounds (B wants many rounds, so B might prefer this... but A wants few rounds).

Wait, A wants the game to end quickly. So A wants to trigger a condition fast.

Hmm, let me reconsider who wants what:
- A wants many cookies = many numbers = game ends quickly (few rounds)
- B wants few cookies = few numbers = game lasts long (many rounds)

So A wants to trigger termination quickly, B wants to avoid termination.

A's move: pick two numbers. B's move: choose operation to avoid termination.

The game ends when either a dominant number appears or all zeros.

Let me think: B wants to avoid both. B wants to keep the game going as long as possible. The maximum number of rounds is 2019 (leaving 1 number, which is automatically terminal). So worst case for A is 1 cookie. But can A do better?

A wants to force termination early. 

Let me think about a potential function or invariant that limits how long B can avoid termination.

Let me consider: the number of odd numbers. Initially 2020 odd numbers (all 1s), 0 even. 

When we combine x, y: 
- x+y has parity (parity of x) XOR (parity of y)... no, x+y parity = (x mod 2 + y mod 2) mod 2.
- |x-y| has same parity as x+y.

So the parity of the new number = (x+y) mod 2.

Number of odd numbers: let's see. If both x, y odd: new number even (odd+odd=even). Number of odds decreases by 2.
If one odd one even: new number odd. Number of odds: -1 +1 = 0 change.
If both even: new number even. Number of odds unchanged.

So number of odd numbers mod 2 is... let's see: both odd → -2 (even change). One odd → 0. Both even → 0. So number of odd numbers mod 2 is invariant? -2 is even, 0 is even. Yes! Number of odd numbers mod 2 is invariant.

Initially 2020 odd numbers (even). So number of odd numbers is always even.

Hmm, that's a mod 2 invariant on count of odds.

Also total sum mod 2 = (number of odd numbers) mod 2 (since evens contribute 0 mod 2, odds contribute 1 each). So sum mod 2 = (count of odds) mod 2. Both even. Consistent.

Let me think about the endgame. The game ends with some configuration. Let's think about what configurations are "terminal" and how many numbers.

Terminal (1): max > total/2. Terminal (2): all zeros (total = 0).

For A to maximize, A wants to force a terminal state with many numbers.

Idea: Maybe A can force the game to end with all numbers being small and one dominant, or some specific structure.

Let me think about a cleaner invariant. 

Consider the sum S. It's even, starts at 2020, non-increasing (since |x-y| ≤ x+y, and x+y keeps it same). S decreases only when B chooses subtraction with unequal numbers.

B wants to prolong. B choosing subtraction reduces S, bringing closer to 0 (condition 2) but also potentially creating dominant numbers (condition 1). B choosing addition keeps S same but creates bigger numbers (risking condition 1).

Hmm. Let me think about the maximum number M. Condition (1) is M > S - M, i.e., M > S/2.

A wants M > S/2 or S = 0.

Let's think about A's strategy to force M > S/2.

Suppose A always picks the two smallest numbers. Then B... if A picks two 1s, B makes 2 or 0. If B makes 2, now there's a 2 among 1s. If B makes 0, there's a 0.

This is getting complex. Let me think about known results or think more structurally.

Let me consider the problem from B's perspective: B wants to maintain 2·max ≤ S (no dominant) and S > 0 (not all zero) for as long as possible.

Claim: B can maintain 2·max ≤ S as long as... hmm.

Let me think about a specific A strategy and compute.

Actually, let me think about the invariant related to the answer. The answer is likely a specific number. Let me guess it might be related to powers of 2 or 2020's properties.

2020 = 4 · 505 = 4 · 5 · 101. Hmm. 2020 in binary: 11111100100. Not a clean power of 2.

Let me think about small cases to find a pattern.

Case n = 1 (one copy of 1): Already... is the game terminal? One number 1, sum of others = 0, 1 > 0, condition (1) holds. So 1 cookie. But the game starts and is already terminal? The problem says game terminates "as soon as, at the end of some round". If initial state is already terminal, does the game end immediately with 1 cookie? Probably the game requires at least... hmm, actually with 1 number there are no rounds played. Let me assume the game must play rounds. Actually with n=1, no round possible (need 2 numbers). So game is already over, 1 cookie.

But our problem has n = 2020 ≥ 2.

Case n = 2 (two 1s): A picks both 1s. B writes 1+1=2 or |1-1|=0. 
- If B writes 2: now one number 2. Condition (1): 2 > 0. Terminal, 1 cookie.
- If B writes 0: now one number 0. Condition (2): all zeros. Terminal, 1 cookie.
Either way, 1 cookie. B chooses to minimize, both give 1. So answer for n=2 is 1.

Case n = 3 (three 1s): A picks two 1s. B writes 2 or 0.
- B writes 0: state {0, 1}. Now A picks 0 and 1. B writes 1 or 1. State {1}. Terminal, 1 cookie. Total 2 rounds, 1 number left.
  Wait, but after first round state is {0,1} (2 numbers). Is this terminal? max=1, sum others=0, 1>0, condition (1)! So terminal after round 1 with 2 cookies!
  Hmm so if B writes 0, we get {0,1}, and 1 > 0, terminal, 2 cookies.
- B writes 2: state {2, 1}. max=2, sum others=1, 2 > 1, condition (1)! Terminal, 2 cookies.

So for n=3, regardless of B's choice, after 1 round we get a terminal state with 2 cookies. A gets 2.

Interesting. So n=3 → 2.

Case n = 4 (four 1s): A picks two 1s. B writes 2 or 0.
- B writes 2: state {2, 1, 1} (3 numbers). max=2, sum others=2, 2 > 2? No. Not terminal. Continue.
  A picks two 1s. B writes 2 or 0.
  - B writes 0: state {2, 0}. max=2 > 0, terminal, 2 cookies.
  - B writes 2: state {2, 2}. max=2, sum others=2, not terminal. Continue. A picks 2,2. B writes 4 or 0. Either way 1 number, terminal, 1 cookie. B chooses to minimize: B prefers 1 cookie. So B writes 4 or 0, both 1 cookie. So from {2,2}, 1 cookie.
  So from {2,1,1}, A picks two 1s. B chooses: 0 → 2 cookies, 2 → eventually 1 cookie. B minimizes → B writes 2, leading to 1 cookie. So {2,1,1} → 1 cookie (B's choice).
  
  Hmm wait, but A chooses which two to pick from {2,1,1}. A could pick {2,1} instead of {1,1}.
  A picks 2 and 1. B writes 3 or 1.
  - B writes 3: state {3, 1}. 3 > 1, terminal, 2 cookies.
  - B writes 1: state {1, 1}. Not terminal (1 = 1). Continue. A picks 1,1. B writes 2 or 0. 1 cookie.
  B minimizes: 3 → 2 cookies, 1 → 1 cookie. B writes 1, → 1 cookie.
  So from {2,1,1}, picking {2,1} → 1 cookie (B minimizes). Picking {1,1} → 1 cookie (B minimizes). Either way 1.
  
- B writes 0: state {0, 1, 1} (3 numbers). max=1, sum others = 0+1=1, 1 > 1? No. Not terminal. Continue.
  A picks two 1s. B writes 2 or 0.
  - B writes 2: {0, 2}. 2 > 0, terminal, 2 cookies.
  - B writes 0: {0, 0}. all zeros, terminal, 2 cookies.
  Either way 2 cookies. So {0,1,1} → 2 cookies.
  But A could pick {0,1} instead. A picks 0,1. B writes 1 or 1. {1,1}. Not terminal. Then → 1 cookie as before. So A prefers picking {1,1} → 2 cookies.
  So {0,1,1} → A picks {1,1} → 2 cookies.

So back to n=4: A picks two 1s. B chooses: write 2 → {2,1,1} → 1 cookie; write 0 → {0,1,1} → 2 cookies. B minimizes → B writes 2 → 1 cookie.

So n=4 → 1 cookie.

Hmm. n=2 → 1, n=3 → 2, n=4 → 1.

Case n=5: A picks two 1s. B writes 2 or 0.
- B writes 2: {2,1,1,1} (4 numbers). max=2, sum others=3, 2 > 3? No. Continue.
- B writes 0: {0,1,1,1} (4 numbers). max=1, sum others=2, no. Continue.

This is getting complicated. Let me think more structurally.

Let me hypothesize the answer relates to the binary representation or the largest power of 2 dividing something.

n=2 → 1, n=3 → 2, n=4 → 1. 

Let me compute n=5,6,7,8 by more careful game tree or find a pattern.

Actually, let me think about it differently. Let me define f(n) = cookies A gets with n ones initially, both optimal.

f(1) = 1 (already terminal or trivially 1).
f(2) = 1.
f(3) = 2.
f(4) = 1.

Let me think about a general principle. 

Key observation: A wants to reach a terminal state fast. The fastest is 1 round if A can force terminal in 1 round.

After 1 round from n ones: A picks two 1s, B writes 2 or 0. State has n-1 numbers: either {2, 1^(n-3)} (one 2 and n-3 ones) or {0, 1^(n-2)} (one 0 and n-2 ones).

Terminal check for {2, 1^(n-3)}: max=2, sum others = n-3. Terminal iff 2 > n-3, i.e., n < 5, i.e., n ≤ 4. For n=3: 2 > 0 yes. n=4: 2 > 1 yes. n=5: 2 > 2 no.

Terminal check for {0, 1^(n-2)}: max=1, sum others = n-2 (the ones) + 0... wait sum of others = (n-2 ones) = n-2, but max is 1 (a one), sum of others = (n-3 ones) + 0 = n-3. Terminal iff 1 > n-3, i.e., n < 4, n ≤ 3. For n=3: 1 > 0 yes. n=4: 1 > 1 no.

So for n=5, neither immediate result is terminal. Game continues.

This suggests the game length grows. Let me think about the general structure more cleverly.

Let me think about B's strategy to prolong and A's strategy to end.

Alternative approach: think about what's the minimum number of numbers B can force the game down to (i.e., maximum rounds), and whether A can force termination earlier.

Actually since A moves first each round and chooses the pair, and B responds, let me think about A's power.

Let me reconsider. Let me think about the quantity T = sum of all numbers. And the maximum M.

A's goal: make M > T/2 or T = 0.

Insight: A can try to "concentrate" the sum into one number. If A always picks the largest number and another number, and B is forced to add... but B will subtract.

If A picks M (largest) and x (some other), B writes M+x or |M-x| = M-x (assuming M ≥ x).
- B writes M+x: new max = M+x, new T = T. Now (M+x) vs T/2... T unchanged, M increased. Closer to dominant. But B won't choose this if it causes terminal.
- B writes M-x: new number M-x. T decreases by 2x. New max could be M-x or the second largest.

B will choose to avoid terminal. 

Hmm, let me think about the problem from the perspective of: what is the maximum k such that A can guarantee termination with at least k numbers?

Let me think about a clever invariant that gives both upper and lower bounds.

Let me consider the sum T and think about B maintaining "balance" (no dominant). 

B's balancing strategy: B wants 2·max ≤ T always. 

When can B maintain this? Suppose current state has 2·max ≤ T. A picks x, y. 

Case 1: B writes x+y. New T' = T. New max' = max(M, x+y) where M is old max. Need 2·max' ≤ T. If x+y ≤ M, then max' = M, still 2M ≤ T. OK. If x+y > M, need 2(x+y) ≤ T. Not always true.

Case 2: B writes |x-y|. New T' = T - 2min(x,y). New max' = max(M, |x-y|) but also M might be removed if x or y was M.

This is complicated. Let me think about whether B can always maintain balance until few numbers remain.

Let me think about a known technique: the "greedy" balancing.

Actually, let me think about the problem in terms of the following: 

Claim: B can force the game down to a small number of numbers, and A can force it to stop at some point. The answer is the value of this game.

Let me think about upper bound on what A can guarantee (i.e., B has a strategy to limit A).

B's strategy idea: maintain the invariant that all numbers are "balanced" — specifically maintain that the multiset can be partitioned or has some structure.

Let me think about the invariant: T mod 4 or the number of numbers with certain properties.

Hmm, let me think about parity more. T is always even. Number of odd numbers is always even.

When the game is terminal by condition (1): M > T/2, i.e., M ≥ T/2 + 1 (since integers, T even so T/2 integer, M > T/2 means M ≥ T/2 + 1).

Let me think about the final number of numbers when A plays optimally and B plays optimally.

Let me try to compute f(n) for more small n by reasoning, to find a pattern.

This is quite involved. Let me think about it as: A wants to minimize rounds, B wants to maximize rounds (subject to game being finite).

Actually, the game is finite regardless (numbers decrease by 1 each round, minimum 1). So B's goal is purely to maximize rounds = reach 1 number if possible. But A tries to force termination earlier.

So the question: what's the fewest rounds A can force termination in, given B tries to avoid it? Then cookies = 2020 - rounds.

Wait, but B might not always be able to reach 1 number; A might force termination earlier. And B tries to avoid termination. So:

f(n) = n - (minimum rounds A can force termination, with B delaying).

Hmm, but it's a game: A minimizes rounds, B maximizes rounds. f(n) = n - R(n) where R(n) is the game value of rounds.

Actually let me reframe: let R(n) = number of rounds when both play optimally (A minimizing rounds, B maximizing). Then cookies = n - R(n). Wait no: after R rounds, numbers = n - R. Cookies = n - R. A wants to maximize cookies = minimize R. B wants to minimize cookies = maximize R. Yes.

So f(n) = n - R(n), where R(n) is the minimax number of rounds.

But careful: the game might terminate at different points. R(n) = the round at which game terminates under optimal play.

Let me recompute small cases:
- n=2: R=1, f=1. ✓
- n=3: R=1, f=2. ✓
- n=4: R=3, f=1. Let me verify: from n=4, we found B can force 1 cookie, meaning R=3. Let me recheck. From {1,1,1,1}, A picks two 1s. B writes 2 → {2,1,1}. Not terminal. A picks (best for A, minimize rounds). From {2,1,1}: A picks {2,1} → B writes 1 → {1,1} (not terminal, round 2) → round 3: {1,1} → A picks → B writes 2 or 0 → 1 number terminal. R=3. Or A picks {1,1} → B writes 2 → {2,2} (not terminal) → round 3 → 1 number. R=3. Or A picks {1,1} → B writes 0 → {2,0} terminal! R=2, f=2. But B minimizes cookies = maximizes R, so B writes 2 not 0. So R=3, f=1. ✓.

OK so my analysis holds.

Let me try to find the pattern by computing more. This requires careful game tree analysis. Let me write a small mental program... actually I can't run code per constraints (no tools). Let me reason.

Hmm, the constraint says don't use tools. But I can reason in my head. Let me try to find structure.

Let me think about the problem via a key invariant or via the "potential" that B maintains.

Alternative idea: Think about the sum T and the fact that B wants to avoid both M > T/2 and T=0.

B's strategy to maximize rounds: Keep T > 0 and 2M ≤ T.

Let me think about when B is forced into a terminal state.

Suppose the state has all numbers equal to some value v > 0, with count c. T = cv, M = v. 2M = 2v ≤ cv iff c ≥ 2. So balanced for c ≥ 2. 

A picks two v's. B writes 2v or 0.
- 2v: state {2v, v^(c-2)}. T = cv. M = 2v (if c ≥ 3, there are other v's; 2v vs v). 2M = 4v ≤ cv iff c ≥ 4. So for c ≥ 4, still balanced. For c = 3: {2v, v}, T=3v, 2M=4v > 3v, terminal! For c=2: {2v}, 1 number, terminal.
- 0: state {0, v^(c-2)}. T = (c-2)v. M = v. 2v ≤ (c-2)v iff c ≥ 4. For c=3: {0,v}, T=v, 2M=2v > v, terminal. For c=2: {0}, all zeros terminal.

So from c equal numbers (c ≥ 2), after one round:
- If c ≥ 4: B can maintain balance (both choices keep balanced for c ≥ 4). B chooses to maximize future rounds.
- If c = 3: terminal after 1 round (both choices terminal), 2 cookies.
- If c = 2: terminal after 1 round, 1 cookie.

Interesting. So if A can drive the state to "all equal", then with c=3 A gets 2, with c=2 A gets 1.

But A doesn't necessarily drive to all equal. Let me think about A's optimal strategy.

Let me reconsider. Maybe think about the problem as: A wants to reach a state with few numbers that is forced terminal.

Let me think about the structure of B's optimal play and find the answer via an invariant.

New idea: Consider the quantity Q = (number of numbers) and the sum T. 

Let me think about the maximum number of rounds B can survive. 

Claim: B can survive (avoid terminal) as long as the number of numbers is ≥ some threshold related to T or the structure.

Let me think about a specific B strategy: "always keep all numbers equal if possible, otherwise maintain balance."

Hmm. Let me think about the problem from the answer's perspective. The answer for 2020 ones. Let me guess the pattern from small cases and extrapolate.

Let me compute f(5).

n=5: {1,1,1,1,1}. A picks two 1s. B writes 2 or 0.
- B writes 2: {2,1,1,1}. T=5, M=2, 2M=4 ≤ 5. Balanced. Not terminal.
- B writes 0: {0,1,1,1}. T=3, M=1, 2M=2 ≤ 3. Balanced. Not terminal.

B chooses whichever leads to more rounds (fewer cookies). Let me compute both branches.

Branch {2,1,1,1} (4 numbers): A's move (minimize rounds).
A's options:
(a) Pick {1,1}: B writes 2 → {2,2,1} or 0 → {2,0,1}.
  - {2,2,1}: T=5, M=2, 2M=4 ≤5. Balanced. 3 numbers.
  - {2,0,1}: T=3, M=2, 2M=4 > 3. Terminal! 3 cookies.
  B minimizes cookies → B writes 2 → {2,2,1}. 
(b) Pick {2,1}: B writes 3 → {3,1,1} or 1 → {1,1,1}.
  - {3,1,1}: T=5, M=3, 2M=6 > 5. Terminal! 3 cookies.
  - {1,1,1}: T=3, M=1, balanced. 3 numbers. From {1,1,1} (c=3 equal), next round terminal, 2 cookies. So {1,1,1} → 2 cookies (R from here = 1).
  B minimizes → B writes 1 → {1,1,1} → 2 cookies. So picking {2,1} → 2 cookies.

So from {2,1,1,1}, A chooses: (a) → {2,2,1} (3 numbers, continue), (b) → 2 cookies. A minimizes rounds (maximizes cookies). (a) leads to {2,2,1} which we need to evaluate, (b) leads to 2 cookies in 1 more round (total R from {2,1,1,1} = 1 + 1 = 2, cookies = 4 - 2 = 2). 

Wait I need to be careful. From {2,1,1,1} (4 numbers), if A picks {2,1} and B writes 1 → {1,1,1} (3 numbers, balanced), then from {1,1,1} it takes 1 more round to terminate with 2 cookies. So total from {2,1,1,1}: 2 rounds, ending with 4-2 = 2 cookies.

If A picks {1,1} and B writes 2 → {2,2,1} (3 numbers). Need to evaluate {2,2,1}.

{2,2,1}: T=5, M=2, balanced. A's move:
- Pick {2,2}: B writes 4 → {4,1} (T=5, M=4, 2M=8>5 terminal, 2 cookies) or 0 → {0,1} (T=1, M=1, 2M=2>1 terminal, 2 cookies). Both terminal, 2 cookies. R from {2,2,1} = 1, cookies = 3-1 = 2.
- Pick {2,1}: B writes 3 → {3,2} (T=5, M=3, 2M=6>5 terminal, 2 cookies) or 1 → {2,1} (T=3, M=2, 2M=4>3 terminal, 2 cookies). Both terminal, 2 cookies.
So {2,2,1} → 2 cookies, R=1.

So from {2,1,1,1}: 
- (a) pick {1,1} → {2,2,1} → 2 cookies, total R = 2, cookies = 4 - 2 = 2.
- (b) pick {2,1} → {1,1,1} → 2 cookies, total R = 2, cookies = 2.
Both give 2 cookies. So {2,1,1,1} → 2 cookies.

Branch {0,1,1,1} (4 numbers): T=3, M=1, balanced. A's move:
- Pick {1,1}: B writes 2 → {0,2,1} (T=3, M=2, 2M=4>3 terminal! 3 cookies) or 0 → {0,0,1} (T=1, M=1, 2M=2>1 terminal, 3 cookies). Both terminal, 3 cookies! R=1, cookies = 4-1 = 3.
- Pick {0,1}: B writes 1 → {1,1,1} (balanced, → 2 cookies) or 1 (|0-1|=1). Both same → {1,1,1} → 2 cookies. R = 1 + 1 = 2, cookies = 4 - 2 = 2.
A minimizes rounds (max cookies): pick {1,1} → 3 cookies. So {0,1,1,1} → 3 cookies.

So back to n=5: A picks two 1s. B chooses: write 2 → {2,1,1,1} → 2 cookies; write 0 → {0,1,1,1} → 3 cookies. B minimizes → B writes 2 → 2 cookies.

So f(5) = 2.

n=2→1, n=3→2, n=4→1, n=5→2.

Let me compute n=6.

n=6: {1^6}. A picks two 1s. B writes 2 → {2,1^4} or 0 → {0,1^4}.
- {2,1^4}: T=6, M=2, 2M=4 ≤ 6. Balanced.
- {0,1^4}: T=4, M=1, 2M=2 ≤ 4. Balanced.
B chooses the branch with fewer cookies (more rounds).

This is getting very tedious. Let me look for a pattern with the values I have: f(2)=1, f(3)=2, f(4)=1, f(5)=2.

Hypothesis: f(n) = something like the largest power of 2 dividing... or f(n) = n mod something.

f(2)=1, f(3)=2, f(4)=1, f(5)=2. 

Maybe f(n) = 2^k where 2^k || (n-1)? Let's check: n=2: n-1=1, 2^0=1. f=1 ✓. n=3: n-1=2, 2^1=2. f=2 ✓. n=4: n-1=3, 2^0=1. f=1 ✓. n=5: n-1=4, 2^2=4. f=2 ✗. Doesn't match.

Maybe f(n) = 2^k where 2^k || n? n=2: 2^1=2, f=1 ✗.

Maybe f(n) related to n mod 3? n=2→1, 3→2, 4→1, 5→2. Pattern 1,2,1,2,...? So f(n) = 2 if n odd, 1 if n even? n=2 even→1 ✓, n=3 odd→2 ✓, n=4 even→1 ✓, n=5 odd→2 ✓.

Let me check this hypothesis with n=6 (even → predict 1) and n=7 (odd → predict 2).

But wait, that seems too simple and the answer for 2020 (even) would be 1. That feels too small for a competition problem. Let me verify n=6 more carefully, because the pattern might break.

Actually, let me reconsider. Let me recompute n=6 to test the "even→1" hypothesis.

n=6: A picks two 1s. B writes 2 → {2,1,1,1,1} or 0 → {0,1,1,1,1}.

B wants fewer cookies. Let me evaluate both.

This is complex. Let me think about whether B can always force 1 cookie for even n.

B's strategy for even n: maintain all numbers even? Let's see. Initially all 1s (odd). Hmm, that doesn't start even.

Alternative B strategy: maintain the invariant that the state is "balanced and can be reduced to 1."

Let me think about it more carefully with a cleaner invariant.

Let me reconsider the parity invariant: number of odd numbers is always even (starts at 2020, even). 

For the game to terminate with condition (2) (all zeros), all numbers even eventually... 

Let me think about the following B strategy: "Always choose the operation that keeps the number of odd numbers even and maintains balance." Since number of odds is always even automatically, B just needs balance.

Hmm, let me think about the "even → 1" hypothesis differently. 

Let me reconsider n=4 → 1. And think about whether for even n, B can always force down to 1.

B's strategy idea for even n: pair up numbers and always subtract to make zeros, but that leads to all zeros which is terminal with many cookies. No, B wants few cookies.

Wait, B wants few cookies = few numbers = many rounds = reach 1 number. B wants to reach exactly 1 number.

To reach 1 number without early termination, B must maintain balance (2M ≤ T) throughout until 1 number left (which is auto-terminal).

So B's goal: maintain 2M ≤ T until only 1 number remains. Can B always do this for even n? Not necessarily; A might force imbalance.

Let me think about A's strategy to force imbalance (terminal early).

A's strategy: create a large number. A picks two numbers hoping B adds. But B subtracts.

Hmm, let me think about the case where all numbers are equal to v, count c (even). We showed for c ≥ 4, B maintains balance. A picks two v's, B writes 2v → {2v, v^(c-2)}, balanced for c ≥ 4. Then A faces {2v, v^(c-2)}. 

A could pick {2v, v}: B writes 3v → {3v, v^(c-3)} (T = cv, M = 3v, 2M = 6v ≤ cv iff c ≥ 6) or v → {v, v^(c-3)} = {v^(c-2)} (back to all equal with count c-2). 

B chooses to maximize rounds. Going back to all-equal with c-2 reduces count by 2 per 2 rounds... 

This is getting complicated. Let me just try to carefully compute n=6.

Actually, let me reconsider. Let me think about whether the answer might be larger, like related to 2020 = 4·505, maybe the answer is 5 or 10 or 505 or something.

Let me reconsider my small cases and think about whether I made errors, then compute n=6,7,8 carefully.

Let me re-examine n=6 by trying to find A's best strategy and B's response.

State {1,1,1,1,1,1}. 

A picks two 1s. B's choices: {2,1,1,1,1} or {0,1,1,1,1}.

Let me evaluate {0,1,1,1,1} (5 numbers, T=4, M=1, balanced):
A wants to minimize rounds. A picks two 1s: B writes 2 → {0,2,1,1} (T=4, M=2, 2M=4 ≤ 4, balanced, not terminal since 2 > 4-2=2? No, 2 > 2 is false, so not terminal) or 0 → {0,0,1,1} (T=2, M=1, 2M=2 ≤ 2, balanced, not terminal).
Hmm wait {0,2,1,1}: M=2, sum others = 0+1+1 = 2, 2 > 2? No. Balanced.
{0,0,1,1}: M=1, sum others = 1, 1 > 1? No. Balanced.

A could pick {0,1}: B writes 1 → {1,1,1,1} (4 numbers all 1). 
So from {0,1,1,1,1}, A picking {0,1} → {1,1,1,1} which is f(4)=1 cookie, but with 4 numbers and R(4)=3, so from {0,1,1,1,1} (5 numbers) → 1 round → {1,1,1,1} → 3 more rounds → total 4 rounds → 6 - 4 = 2 cookies. Hmm wait, but we're evaluating the subgame from {0,1,1,1,1} which has 5 numbers. If it takes 4 rounds to terminate, cookies = 5 - 4 = 1. 

Hmm, I need to be careful: cookies = number of numbers at termination = (initial count) - (rounds played). From {0,1,1,1,1} (5 numbers), if 4 rounds played, 1 cookie.

But A wants to minimize rounds. Let me see if A can do better from {0,1,1,1,1}.

A picks {1,1}: 
- B writes 2 → {0,2,1,1} (4 numbers). 
- B writes 0 → {0,0,1,1} (4 numbers).
B chooses to maximize rounds (minimize cookies). Need to evaluate both.

{0,2,1,1} (4 numbers, T=4, M=2, balanced): A's move.
- Pick {1,1}: B writes 2 → {0,2,2} (T=4, M=2, 2M=4 ≤ 4, balanced) or 0 → {0,2,0} (T=2, M=2, 2M=4 > 2, terminal! 3 cookies). B minimizes → writes 2 → {0,2,2}.
- Pick {2,1}: B writes 3 → {0,3,1} (T=4, M=3, 2M=6 > 4, terminal, 3 cookies) or 1 → {0,1,1} (T=2, M=1, 2M=2 ≤ 2, balanced). B minimizes → writes 1 → {0,1,1}.
- Pick {0,1}: B writes 1 → {2,1,1} (T=4, M=2, 2M=4 ≤ 4, balanced) or 1 → same. → {2,1,1}.
- Pick {0,2}: B writes 2 → {2,1,1} (T=4, M=2, balanced) or 2 → same. → {2,1,1}.

A minimizes rounds. Options lead to: {0,2,2}, {0,1,1}, {2,1,1} (all 3 numbers, balanced, continue). A picks whichever leads to fewest total rounds.

{0,1,1} (3 numbers, T=2, M=1, balanced): A's move.
- Pick {1,1}: B writes 2 → {0,2} (T=2, M=2, 2M=4 > 2, terminal, 2 cookies) or 0 → {0,0} (all zeros, terminal, 2 cookies). Both terminal, 2 cookies. R=1.
- Pick {0,1}: B writes 1 → {1,1} (T=2, M=1, balanced) → next round terminal 1 cookie. R = 1 + 1 = 2, 1 cookie.
A minimizes rounds → picks {1,1} → 2 cookies, R=1. So {0,1,1} → 2 cookies (from 3 numbers, R=1, cookies=2).

{2,1,1} (3 numbers, T=4, M=2, balanced): A's move.
- Pick {1,1}: B writes 2 → {2,2} (T=4, M=2, 2M=4 ≤ 4, balanced) or 0 → {2,0} (T=2, M=2, 2M=4 > 2, terminal, 2 cookies). B minimizes → writes 2 → {2,2}.
- Pick {2,1}: B writes 3 → {3,1} (T=4, M=3, 2M=6 > 4, terminal, 2 cookies) or 1 → {1,1} (T=2, M=1, balanced, → 1 cookie). B minimizes → writes 1 → {1,1} → 1 cookie.
A minimizes rounds: pick {1,1} → {2,2} (continue), or pick {2,1} → 1 cookie (R=2 from {2,1,1}). 
{2,2} (2 numbers, T=4, M=2, balanced): A picks {2,2}: B writes 4 → {4} (terminal, 1 cookie) or 0 → {0} (terminal, 1 cookie). R=1, 1 cookie. So {2,2} → 1 cookie, R=1. From {2,1,1}, pick {1,1} → {2,2} → 1 cookie, total R = 2, cookies = 3 - 2 = 1.
So from {2,1,1}: pick {2,1} → 1 cookie (R=2), pick {1,1} → 1 cookie (R=2). Both 1 cookie. So {2,1,1} → 1 cookie.

{0,2,2} (3 numbers, T=4, M=2, balanced): A's move.
- Pick {2,2}: B writes 4 → {0,4} (T=4, M=4, 2M=8 > 4, terminal, 2 cookies) or 0 → {0,0} (terminal, 2 cookies). Both 2 cookies. R=1.
- Pick {0,2}: B writes 2 → {2,2} (→ 1 cookie, R=1) or 2 → same. → {2,2} → 1 cookie, R=2.
A minimizes rounds → pick {2,2} → 2 cookies, R=1. So {0,2,2} → 2 cookies.

So from {0,2,1,1} (4 numbers), A's options:
- pick {1,1} → {0,2,2} → 2 cookies (R from {0,2,1,1} = 1 + 1 = 2, cookies = 4 - 2 = 2).
- pick {2,1} → {0,1,1} → 2 cookies (R = 1 + 1 = 2, cookies = 2).
- pick {0,1} or {0,2} → {2,1,1} → 1 cookie (R = 1 + 2 = 3, cookies = 4 - 3 = 1).
A minimizes rounds (maximizes cookies) → picks {1,1} or {2,1} → 2 cookies. So {0,2,1,1} → 2 cookies.

Now {0,0,1,1} (4 numbers, T=2, M=1, balanced): A's move.
- Pick {1,1}: B writes 2 → {0,0,2} (T=2, M=2, 2M=4 > 2, terminal, 3 cookies) or 0 → {0,0,0} (terminal, 3 cookies). Both 3 cookies! R=1.
- Pick {0,1}: B writes 1 → {0,1,1} (→ 2 cookies, R=1) → total R=2, cookies = 4-2 = 2. Or 1 → same.
A minimizes rounds → pick {1,1} → 3 cookies, R=1. So {0,0,1,1} → 3 cookies.

So from {0,1,1,1,1} (5 numbers), A picks {1,1}: B writes 2 → {0,2,1,1} → 2 cookies; B writes 0 → {0,0,1,1} → 3 cookies. B minimizes → writes 2 → 2 cookies. (R from {0,1,1,1,1} = 1 + 2 = 3, cookies = 5 - 3 = 2.)

A could pick {0,1} from {0,1,1,1,1}: → {1,1,1,1} → f(4) = 1 cookie (R=3 from {1,1,1,1}), total R = 1 + 3 = 4, cookies = 5 - 4 = 1.
A could pick {1,1} → 2 cookies (as computed).
A minimizes rounds → picks {1,1} → 2 cookies. So {0,1,1,1,1} → 2 cookies.

Now evaluate {2,1,1,1,1} (5 numbers, T=6, M=2, balanced): A's move.
Options:
- Pick {1,1}: B writes 2 → {2,2,1,1} (T=6, M=2, 2M=4 ≤ 6, balanced) or 0 → {2,0,1,1} (T=4, M=2, 2M=4 ≤ 4, balanced). 
- Pick {2,1}: B writes 3 → {3,1,1,1} (T=6, M=3, 2M=6 ≤ 6, balanced) or 1 → {1,1,1,1} (→ 1 cookie, R=3) → total R = 1+3 = 4, cookies = 5 - 4 = 1.

B minimizes cookies. Let me evaluate the branches.

This is getting really deep. Let me step back and think about the pattern differently.

Given f(2)=1, f(3)=2, f(4)=1, f(5)=2, and the hypothesis f(n) = 2 if n odd, 1 if n even.

But for n=6 (even), I need to verify f(6)=1. The computation is getting unwieldy. Let me think about a cleaner argument.

Let me think about B's strategy for even n to force 1 cookie, and A's strategy for odd n to force 2 cookies.

B's strategy (even n): I conjecture B can always maintain balance until 1 number remains. 

A's strategy (odd n): A can force a terminal state with 2 numbers.

Let me think about A's strategy for odd n. 

For odd n, the number of odd numbers is even (invariant), but n is odd... hmm, n is the count, not the number of odds.

Wait, actually let me reconsider. Let me think about A's strategy to force termination with exactly 2 numbers for odd n.

Hmm, let me think about the invariant: T mod 2 = 0 always (T even). Number of numbers = n - rounds.

For terminal with condition (1) and 2 numbers {a, b} with a > b: a > b (since a > sum of others = b). T = a + b. a > b means a ≥ b+1. T = a + b ≥ 2b + 1. T is even, so T ≥ 2b + 2, i.e., a ≥ b + 2... no wait, T even and a > b: a + b even, a > b. E.g., a=2, b=0: T=2. a=3,b=1: T=4. etc.

For terminal with 2 numbers, we need the two numbers unequal (if equal, a = b, a > b false, not terminal; then A picks them, B writes 2a or 0, 1 number terminal).

Hmm OK. Let me think about the parity argument for why odd n gives 2 and even n gives 1.

Actually, let me reconsider. Let me reconsider whether the pattern is really 1,2,1,2,...

Let me reconsider n=6. Let me think about B's strategy to force 1 cookie.

B's strategy: maintain 2M ≤ T until 1 number left.

Initially {1^6}: T=6, M=1, 2M=2 ≤ 6. ✓.

A picks two 1s. 
- If B writes 2: {2,1,1,1,1}, T=6, M=2, 2M=4 ≤ 6. ✓.
- If B writes 0: {0,1,1,1,1}, T=4, M=1, 2M=2 ≤ 4. ✓.

B needs to choose and continue maintaining. The question is whether A can ever force 2M > T.

Let me think about a general B strategy. 

B's strategy: "Always respond so that 2M ≤ T is maintained, and prefer the choice that keeps more 'flexibility'."

Claim: If T ≥ 2·(number of nonzero numbers), then B can maintain balance. Hmm, not sure.

Let me think about a potential function. Let me consider the number of nonzero numbers, call it c. And T.

If all nonzero numbers are ≥ 1, then T ≥ c. And M ≤ T. 2M ≤ T iff M ≤ T/2.

Hmm. Let me think about the worst case for B: A tries to make M large.

Let me think about A's most aggressive strategy: A always picks the two largest numbers.

If A picks the two largest, say M1 ≥ M2. B writes M1+M2 or M1-M2.
- M1+M2: new max = M1+M2 (likely). T unchanged. 2(M1+M2) ≤ T? T ≥ M1 + M2 + (rest). If rest is small, might violate.
- M1-M2: new number M1-M2. T decreases by 2M2. 

B chooses whichever maintains balance (or if both maintain, the one leading to more rounds; if neither maintains, A wins).

Hmm. Let me think about the specific structure for even n.

Actually, let me reconsider the whole problem. Maybe the answer isn't 1 for 2020. Let me reconsider my small cases; maybe I made an error and the pattern is different.

Let me recheck n=4 very carefully.

n=4: {1,1,1,1}. A picks two 1s.
B writes 2 → {2,1,1} (T=4, M=2, 2M=4 ≤ 4, balanced, not terminal). 
B writes 0 → {0,1,1} (T=2, M=1, 2M=2 ≤ 2, balanced, not terminal).
B chooses to maximize rounds.

From {2,1,1}: A picks.
- {1,1}: B writes 2 → {2,2} (T=4, M=2, 2M=4 ≤ 4, balanced) or 0 → {2,0} (T=2, M=2, 2M=4 > 2, terminal, 2 cookies). B minimizes cookies → writes 2 → {2,2}.
- {2,1}: B writes 3 → {3,1} (T=4, M=3, 2M=6 > 4, terminal, 2 cookies) or 1 → {1,1} (T=2, M=1, balanced) → next round 1 cookie. B minimizes → writes 1 → {1,1} → 1 cookie (R from {2,1,1} = 2).
A minimizes rounds: {1,1} → {2,2} → 1 cookie (R from {2,1,1} = 2); {2,1} → 1 cookie (R=2). Both R=2, 1 cookie. So {2,1,1} → 1 cookie.

From {0,1,1}: A picks.
- {1,1}: B writes 2 → {0,2} (T=2, M=2, 2M=4 > 2, terminal, 2 cookies) or 0 → {0,0} (terminal, 2 cookies). Both 2 cookies, R=1.
- {0,1}: B writes 1 → {1,1} (→ 1 cookie, R=2 from {0,1,1}). 
A minimizes rounds → {1,1} → 2 cookies, R=1. So {0,1,1} → 2 cookies.

So n=4: B writes 2 → {2,1,1} → 1 cookie; B writes 0 → {0,1,1} → 2 cookies. B minimizes → writes 2 → 1 cookie. f(4) = 1. ✓.

OK so f(4)=1 confirmed.

Now the key question: is the pattern really 1,2,1,2,1,2,...? Let me think about why.

For even n: B writes 2 (addition) when A picks two 1s, getting {2, 1^(n-2)}... and somehow forces down to 1.
For odd n: A can force 2.

Let me think about the invariant that distinguishes even/odd.

The number of numbers n decreases by 1 each round. The parity of n flips each round. 

Terminal states: 
- 1 number: n=1 (odd).
- 2 numbers with one dominant: n=2 (even).
- More numbers with one dominant: various parities.
- All zeros: any n.

Hmm. Let me think about T mod 4 or some other invariant.

Let me reconsider. T is always even. T mod 4?

When B writes x+y: T unchanged.
When B writes |x-y|: T decreases by 2·min(x,y). So T mod 4 changes by 2·min(x,y) mod 4.

Not invariant mod 4.

Let me think about the number of odd numbers mod 4 or something.

Hmm, let me think differently. Let me consider the quantity: (number of numbers) + (T/2) mod 2, or similar.

Actually, let me think about the following. Let me consider the "excess" E = T - 2M (how far from terminal condition 1). B wants E ≥ 0 (balanced). When E < 0, terminal.

And T = 0 is terminal (condition 2).

Let me think about n mod 2 and the terminal condition.

Actually, let me just try to prove the pattern 1,2,1,2,... by induction, or find where it breaks.

Let me hypothesize:
- For even n: B can force 1 cookie (reach 1 number).
- For odd n: A can force 2 cookies (reach 2 numbers with one dominant), and B can prevent more than 2.

Wait, but for large odd n, can A really force termination at 2 numbers? That requires A to force imbalance when down to 2 numbers. With 2 numbers {a,b}, terminal iff a ≠ b (and the larger > smaller). If a = b, not terminal, A picks them, 1 number, 1 cookie.

So for odd n, A wants to reach 2 numbers that are unequal. B wants to reach 2 equal numbers (then 1 cookie) or prolong.

Hmm, let me reconsider. Let me think about whether for odd n, A can guarantee 2, and for even n, B can guarantee 1.

Let me think about the parity of T and the count.

At 2 numbers {a, b}: T = a + b (even). If a ≠ b, terminal (2 cookies). If a = b, not terminal, → 1 cookie.

At 3 numbers: terminal iff one > sum of other two.

Let me think about the invariant: T/2 mod 2 = (number of numbers) mod 2?

T/2 mod 2: initially T=2020, T/2 = 1010, even. Number of numbers = 2020, even. So T/2 mod 2 = 0 = n mod 2. 

When B writes x+y: T same, n decreases by 1. So T/2 mod 2 same, n mod 2 flips. So the relation T/2 ≡ n (mod 2) breaks... unless it was never an invariant.

Let me check: initially T/2 = 1010 (even), n = 2020 (even). After 1 round with addition: T/2 = 1010 (even), n = 2019 (odd). So T/2 mod 2 ≠ n mod 2. So not invariant. Scratch that.

Let me think about T mod 4 and n mod 2 together.

Initially T = 2020 ≡ 0 (mod 4), n = 2020 (even).
After addition: T same (≡ 0 mod 4), n odd.
After subtraction (|x-y|, x=y=1): T = 2018 ≡ 2 (mod 4), n odd.

Hmm. Let me think about T mod 4 vs n mod 2:
- Initially: T ≡ 0 (mod 4), n even.
- Addition: T mod 4 same, n flips. So if T ≡ 0, n was even → n odd. T ≡ 0, n odd.
- Subtraction by 2·min: T decreases by 2m (m = min). T mod 4 changes by 2m mod 4. n flips.

Not obviously invariant.

Let me try yet another approach: think about the quantity T - n. 
Initially T - n = 2020 - 2020 = 0.
Addition: T same, n decreases by 1. T - n increases by 1.
Subtraction: T decreases by 2m, n decreases by 1. T - n changes by -2m + 1.

Not invariant.

Let me think about T - n mod 2: 
Addition: +1 (flips).
Subtraction: -2m + 1 = 1 - 2m ≡ 1 (mod 2) (flips).
So T - n mod 2 flips every round regardless! So T - n mod 2 ≡ (rounds) mod 2. Initially 0. After k rounds, T - n ≡ k (mod 2). Not super useful but consistent.

Hmm. Let me think about the answer differently. Let me reconsider whether the pattern might be more complex, like f(n) = 2^(v_2(n)) or similar, and my small cases just happen to give 1,2,1,2.

v_2(n) = exponent of 2 in n:
n=2: v_2=1, 2^1=2. f=1. ✗.

n=2: f=1, n=3: f=2, n=4: f=1, n=5: f=2.

What about f(n) = 2 - (n mod 2)? n even → 1, n odd → 2. Same as before.

Or f(n) = 1 + (n mod 2)? n=2→1, n=3→2, n=4→1, n=5→2. Yes.

Let me try to verify n=6 → 1 more carefully, or find that it breaks.

Actually, let me think about B's strategy for even n more cleverly.

B's strategy for even n: "Mirror" strategy. Pair up the numbers. Maintain that the state can be partitioned into pairs that sum equally, or some symmetric structure.

Hmm, let me think. Initially 2020 ones. Pair them: 1010 pairs of (1,1).

B's strategy: whenever A picks two numbers, B responds to maintain a "paired" structure.

Actually, let me think about the following B strategy for even n:

B maintains the invariant: the multiset of numbers can be partitioned into pairs (a_i, b_i) with a_i = b_i for all i. I.e., every number appears an even number of times.

Initially: 2020 ones, each 1 appears 2020 times (even). ✓.

A picks two numbers x, y. 
Case 1: x and y are "partners" (the two copies of the same value from one pair). Then B writes x+y = 2x or |x-y| = 0. 
- If B writes 0: we removed two copies of x, added one 0. Now the count of x is even - 2 = even, and 0 appears once (odd). Invariant broken (0 appears odd times).
- If B writes 2x: removed two x's, added one 2x. Count of x: even - 2 = even. Count of 2x: +1 (odd). Invariant broken.

So this invariant doesn't hold easily. Hmm.

Let me think about a different invariant: every value appears an even number of times EXCEPT possibly... no.

Let me reconsider. The invariant "number of odd numbers is even" holds. For even n initially with all 1s, number of odds = n (even). 

Let me think about B's strategy to reach 1 number for even n. 

Alternative: think about A's strategy for odd n to force 2.

For odd n, A wants to force termination at 2 numbers (unequal). 

Hmm, let me think about the endgame more. When we're down to 2 numbers {a, b}, T = a+b even. Terminal iff a ≠ b. 

When we're down to 3 numbers {a, b, c} (sorted a ≥ b ≥ c), terminal iff a > b + c.

A picks two, B responds, → 2 numbers.
- A picks {b, c}: B writes b+c → {a, b+c} or |b-c| → {a, |b-c|}. 
  - {a, b+c}: terminal iff a ≠ b+c. 
  - {a, |b-c|}: terminal iff a ≠ |b-c|.
- A picks {a, b}: B writes a+b → {a+b, c} or a-b → {a-b, c}.
  - {a+b, c}: terminal iff a+b ≠ c (always true since a+b ≥ a ≥ c, and a+b = c only if... a+b = c impossible since a ≥ c, b ≥ 0, so a+b ≥ c, equality iff a=c and b=0... a+b=c with a≥b≥c: a+b ≥ a ≥ c, so a+b = c iff a = c and b = 0, but b ≥ c = a ≥ b so b = a = c = 0, all zeros already terminal). So a+b > c always (if not all zero), terminal. 2 cookies.
  - {a-b, c}: terminal iff a-b ≠ c, i.e., a ≠ b+c. If a = b+c (was balanced/non-terminal at 3), then a - b = c, so {a-b, c} = {c, c}, not terminal! → 1 cookie.
- A picks {a, c}: similar.

So at 3 numbers {a,b,c} with a ≤ b+c (non-terminal, balanced):
- A picks {a, b}: B writes a+b → terminal (2 cookies); B writes a-b → {a-b, c}. If a-b = c i.e. a = b+c (but a ≤ b+c, so a = b+c means a = b+c, but we said a ≤ b+c; if a < b+c then a - b < c... wait a - b vs c: a - b could be < c or = c or... a ≤ b + c so a - b ≤ c. If a - b < c: {a-b, c} with c > a-b, terminal (2 cookies). If a - b = c: {c, c}, not terminal (→ 1 cookie). a - b = c iff a = b + c, but a ≤ b + c and if a = b + c then a > b + c is false (it's equal), so non-terminal. So if a = b+c exactly, B writes a-b = c → {c,c} → 1 cookie. If a < b+c, B writes a-b < c → {a-b, c} terminal 2 cookies, OR B writes a+b → terminal 2 cookies. So if a < b+c, both B choices give 2 cookies. If a = b+c, B can choose a-b → 1 cookie.

So at 3 numbers: if a < b+c (strictly balanced), A picks {a,b} → 2 cookies regardless. If a = b+c (boundary), B can force 1 cookie.

Wait, but A chooses which pair. Let me reconsider. At {a,b,c}, a ≥ b ≥ c, a ≤ b+c (non-terminal).

If a < b+c (strict): 
- A picks {a,b}: B writes a+b (terminal, 2) or a-b. a-b < c (since a < b+c → a-b < c). So {a-b, c}, c > a-b, terminal, 2 cookies. Both 2 cookies.
- A picks {b,c}: B writes b+c → {a, b+c}. a < b+c (strict), so b+c > a, terminal, 2 cookies. B writes |b-c| → {a, |b-c|}. a ≥ b ≥ c ≥ 0, a vs |b-c| = b-c. a ≥ b > b - c (if c > 0) or a ≥ b = b-c (if c=0). If c > 0: a ≥ b > b - c, so a > b - c, terminal, 2 cookies. If c = 0: a ≥ b = b - 0, a vs b: if a > b terminal 2 cookies; if a = b then {a, a} = {b, b}, not terminal → 1 cookie. But a < b + c = b + 0 = b, so a < b, contradicting a ≥ b. So c = 0 and a < b impossible (a ≥ b). So c > 0, and a > b - c, terminal, 2 cookies.
  So A picks {b,c}: both B choices → 2 cookies.
So if a < b+c (strict), A can force 2 cookies from 3 numbers. ✓.

If a = b+c (boundary, still non-terminal since a = b+c not a > b+c):
- A picks {a,b}: B writes a+b → terminal 2; B writes a-b = c → {c, c} → 1 cookie. B chooses 1 cookie.
- A picks {a,c}: B writes a+c → {a+c, b}. a+c = b+c+c = b + 2c > b (if c > 0), terminal 2. B writes a-c = b → {b, b} → 1 cookie. B chooses 1.
- A picks {b,c}: B writes b+c = a → {a, a} → 1 cookie. B writes b-c → {a, b-c}. a = b+c > b-c (c > 0), terminal 2. B chooses b+c → {a,a} → 1 cookie.
So if a = b+c, B can force 1 cookie from 3 numbers.

So at 3 numbers: A gets 2 if strictly balanced (a < b+c), B gets 1 if boundary (a = b+c).

Interesting. So the boundary case a = b+c is bad for A.

Now, the question is whether A can avoid reaching a boundary 3-state, and whether B can force a boundary 3-state.

Let me think about 4 numbers and when B can force a boundary 3-state (leading to 1 cookie) vs A forces strict (leading to 2).

At 4 numbers {a,b,c,d} sorted, balanced (a ≤ b+c+d). A picks two, B responds → 3 numbers.

A wants to reach a strict 3-state (a' < b'+c'). B wants boundary (a' = b'+c') or to continue.

Hmm, this is getting complicated but let me think about the parity/invariant that determines whether B can force boundary.

Let me think about the invariant T mod 2 = 0 (always). At a boundary 3-state {a,b,c} with a = b+c: T = a + b + c = 2a = 2(b+c). T/2 = a = b+c. 

At a strict 3-state: T = a + b + c, a < b+c, T/2 = (a+b+c)/2 > a/2... hmm. T/2 vs a: a < b+c → 2a < a + b + c = T → a < T/2. So strict means a < T/2, boundary means a = T/2.

So at 3 numbers: terminal (condition 1) iff a > T/2, boundary iff a = T/2 (then B forces 1), strict iff a < T/2 (A gets 2).

So A wants a < T/2 at 3 numbers, B wants a = T/2 (or a > T/2 which is terminal but that's 3 cookies for A, so B avoids; B wants a = T/2).

Wait, if a > T/2 at 3 numbers, that's terminal condition (1) with 3 cookies. B wants to avoid that. B wants a = T/2 (→ 1 cookie) or a < T/2 (→ 2 cookies). B prefers a = T/2 (1 cookie) over a < T/2 (2 cookies). And a > T/2 (3 cookies) is worst for B.

So at 3 numbers, the value is: 3 if a > T/2, 1 if a = T/2, 2 if a < T/2.

Now, can B force a = T/2 at 3 numbers? This depends on the 4-number state.

Let me think about 4 numbers {a ≥ b ≥ c ≥ d}, T = a+b+c+d, balanced a ≤ b+c+d = T - a, i.e., 2a ≤ T.

A picks two, B responds → 3 numbers. A wants the 3-state to have max < T'/2 (strict, → 2) or max > T'/2 (terminal, → 3). B wants max = T'/2 (→ 1) or to continue if possible... but at 4 numbers if A can force terminal, A will.

Hmm wait, at 4 numbers, can A force terminal (condition 1) directly? A picks two, B responds → 3 numbers. The 3-number state might be terminal (if its max > its T/2). 

This is a complex game tree. Let me think about the general invariant.

Let me hypothesize: the answer depends on T/2 mod 2 or the parity of n.

Let me reconsider. At 3 numbers, B can force 1 cookie iff a = T/2, i.e., the largest equals half the total. 

At 2 numbers {a, b}, a ≥ b: terminal iff a > b iff a > T/2 (since T = a+b, T/2 = (a+b)/2, a > T/2 iff a > b). Boundary a = b = T/2 → not terminal → 1 cookie. Strict a > b → terminal 2 cookies.

So at 2 numbers: 2 cookies if a > b (a > T/2), 1 cookie if a = b (a = T/2).

Pattern: at k numbers, the "boundary" a = T/2 gives B the advantage (forces fewer cookies), and A wants to avoid boundary.

Now the key invariant: can B always force the boundary a = T/2 when reaching a small number of numbers?

Let me think about T/2 and its parity. T is always even. T/2 is an integer. 

Initially T/2 = 1010. 

When B writes x+y: T/2 unchanged.
When B writes |x-y|: T/2 decreases by min(x,y).

So T/2 is non-increasing. T/2 starts at 1010.

At the boundary state with k numbers, a = T/2 where a is the max. 

Hmm, let me think about T/2 mod 2 and the number of numbers.

Let me consider the invariant: T/2 ≡ (n - 1) (mod 2)? Or T/2 ≡ n (mod 2)?

Initially T/2 = 1010 (even), n = 2020 (even). T/2 ≡ n (mod 2): 0 ≡ 0. ✓.
After addition: T/2 same, n → n-1. T/2 ≡ n-1 (mod 2)? Was T/2 ≡ n, now T/2 ≡ n-1? Only if... no, T/2 unchanged, n changed parity. So T/2 ≡ n (mod 2) becomes T/2 ≡ n+1 (mod 2). Broken.

So not invariant. Hmm.

Let me think about T/2 mod 2 alone. It changes only on subtraction, by min(x,y). 

And n mod 2 flips every round.

Let me think about (T/2 + n) mod 2:
- Addition: T/2 same, n flips. (T/2 + n) flips.
- Subtraction: T/2 decreases by m = min(x,y), n flips. (T/2 + n) changes by -m + 1 (mod 2) = 1 - m (mod 2).
Not invariant.

Let me think about (T/2 - n) mod 2:
- Addition: 0 - 1 = -1 ≡ 1 (mod 2). Flips.
- Subtraction: -m - (-1)... wait n decreases by 1 so -n increases by 1. (T/2 - n) changes by -m + 1. Same as above.
Not invariant.

Hmm. Let me think about T mod 4.
Initially T = 2020 ≡ 0 (mod 4).
- Addition: T unchanged.
- Subtraction: T -= 2m. T mod 4 changes by 2m mod 4 = 2(m mod 2).

So T mod 4 changes by 0 or 2 on subtraction. T mod 4 ∈ {0, 2} always (since T even). 

T mod 4 = 0 or 2. Initially 0.

Subtraction by 2m: if m even, T mod 4 unchanged; if m odd, T mod 4 flips (0↔2).

Hmm. Let me think about whether T/2 mod 2 is determined by something.

T/2 mod 2 = (T mod 4) / 2. So T/2 even iff T ≡ 0 (mod 4), T/2 odd iff T ≡ 2 (mod 4).

Initially T/2 = 1010 even.

Let me think about the number of odd numbers and T mod 4. T = sum of all numbers. T mod 2 = (number of odd numbers) mod 2 = 0. T mod 4 = (sum of odd numbers) mod 4 + (sum of even numbers) mod 4. Even numbers contribute 0 or 2 mod 4. Hmm complex.

Let me step back and think about the problem from a higher level.

I'll conjecture the answer is 1 (since 2020 is even) based on the pattern, but let me try to verify with n=6 or find a counterexample, and also think about whether the pattern could be different for larger n.

Actually, wait. Let me reconsider. The pattern 1,2,1,2 for n=2,3,4,5 might break for larger n. Let me think about n=6 and n=7 by considering B's strategy.

Let me think about B's strategy for even n to force 1 cookie.

B's strategy: maintain the invariant T/2 is even? No...

Let me think about B's strategy: "maintain that all numbers are even." 

Initially all 1s (odd). So can't maintain all even from the start.

B's strategy: "maintain that the number of odd numbers is 0 mod 4"? Initially 2020 ≡ 0 (mod 4) (2020 = 4·505). 

When combining x, y:
- Both odd: new number even. Odd count -= 2.
- One odd: new odd. Odd count unchanged.
- Both even: new even. Odd count unchanged.

So odd count changes by 0 or -2. Odd count mod 2 invariant (always even). Odd count mod 4: changes by 0 or 2. So odd count mod 4 can change by 2. Not invariant mod 4.

Hmm. Initially odd count = 2020 ≡ 0 (mod 4). After combining two odds: odd count -= 2 → ≡ 2 (mod 4). So mod 4 not invariant.

Let me think about odd count mod 4 vs something.

OK let me try a completely different approach. Let me think about the problem as a combinatorial game and try to find the answer via a known technique.

Reformulation: We have a multiset of positive integers (and zeros). Each round, replace two numbers x, y by either x+y or |x-y| (B's choice). A chooses which two. Game ends when max > (sum - max) or all zero. A wants to end fast (keep count high), B wants to delay.

Key insight attempt: Think about the sum T and the "defect" D = T - 2·max (how balanced). B wants D ≥ 0. When D < 0, terminal (A wins with current count). When T = 0, terminal (A wins with current count, all zeros).

B wants to keep D ≥ 0 and T > 0 as long as possible.

Let me think about the minimum count at which A can force D < 0 or T = 0.

Hmm, let me think about A's strategy: A wants to make max large. A picks the two largest numbers. B must respond.

If A picks the two largest M1 ≥ M2:
- B writes M1 + M2: new max = M1 + M2 (assuming this is ≥ all others, which it is since M1 + M2 ≥ M1 ≥ all). T same. D' = T - 2(M1+M2) = D - 2M2. So D decreases by 2M2.
- B writes M1 - M2: new number M1 - M2. New max = max(M1 - M2, M3) where M3 is third largest. T' = T - 2M2. D' = T' - 2·max(M1-M2, M3).

B chooses to keep D ≥ 0. 

If B writes M1+M2: D' = D - 2M2. If D < 2M2, this makes D' < 0 → terminal. So B won't choose this if D < 2M2.
If B writes M1-M2: need to check D' ≥ 0.

So A wants to create a situation where both choices give D' < 0 (forced terminal).

This is like the Euclidean algorithm / Stern-Brocot territory.

Let me think about the specific initial state: all 1s. A picks two 1s. B writes 2 or 0.

Let me think about A's global strategy: A wants to build up a large number while keeping the total fixed (force B to add) or reduce total strategically.

Hmm. Let me think about the answer being related to the largest power of 2 dividing n, or the Thue-Morse, or something.

Actually, let me reconsider the small cases and compute n=6 and n=7 to check the pattern, being very careful. Let me use the insights about 2-number and 3-number endgames.

Let me define V(state) = cookies A gets under optimal play.

2 numbers {a, b}, a ≥ b: V = 2 if a > b, V = 1 if a = b. (If a > b terminal; if a = b, one round → 1.)

3 numbers {a ≥ b ≥ c}: 
- If a > b + c: terminal, V = 3.
- If a = b + c: V = 1 (B forces boundary, shown above).
- If a < b + c: V = 2 (A forces strict, shown above).

Wait, I need to double check the a = b+c case gives V=1 and a < b+c gives V=2, considering A might force terminal (V=3) in some sub-branch.

For a < b+c (strict), I showed A picks {a,b} or {b,c} and both B responses give a 2-number terminal state (2 cookies). But could A do something to get 3 cookies? 3 cookies means terminal at 3 numbers, but a < b+c means not terminal. So no. V = 2. ✓.

For a = b+c, I showed B can force 1 cookie. But can A force 2? Let me recheck. A picks {a,b}: B writes a-b = c → {c, c} → 1. A picks {a,c}: B writes a-c = b → {b,b} → 1. A picks {b,c}: B writes b+c = a → {a,a} → 1. All give 1. So V = 1. ✓.

For a > b+c: terminal, V = 3. ✓.

Now 4 numbers {a ≥ b ≥ c ≥ d}, balanced (a ≤ b+c+d, i.e., 2a ≤ T). 
A picks two, B responds → 3 numbers. A wants to maximize V of resulting 3-state, B wants to minimize.

The 3-state value is 3 if max > T'/2, 1 if max = T'/2, 2 if max < T'/2.

A wants 3 (terminal at 4? no, terminal at 3 means V=3) or 2. B wants 1.

Wait, V=3 at 3 numbers means terminal (condition 1) with 3 cookies. So A wants the 3-state to be terminal (max > T'/2) → 3 cookies. Or strict (max < T'/2) → 2 cookies. B wants boundary (max = T'/2) → 1 cookie.

So at 4 numbers, A picks a pair, B chooses operation, resulting 3-state. A wants resulting 3-state to have max ≠ T'/2 (either > or <), specifically max > T'/2 for 3 cookies. B wants max = T'/2 for 1 cookie, or if can't, min (max < T'/2 for 2, or max > T'/2 for 3 — B prefers 2 over 3).

Let me enumerate. 4 numbers a ≥ b ≥ c ≥ d, T = a+b+c+d, 2a ≤ T.

A's choices:
1. Pick {a, b}: B writes a+b → {a+b, c, d}, T' = T. Max = a+b. a+b vs T/2: a+b > T/2 iff 2(a+b) > T iff 2a + 2b > a+b+c+d iff a + b > c + d. B writes a-b → {a-b, c, d}, T' = T - 2b. Max = max(a-b, c). 
2. Pick {a, c}: similar.
3. Pick {a, d}: similar.
4. Pick {b, c}: B writes b+c → {a, b+c, d}, T'=T. Max = max(a, b+c). B writes b-c → {a, b-c, d}, T' = T - 2c. Max = max(a, b-c) = a (since a ≥ b ≥ b-c).
5. Pick {b, d}: ...
6. Pick {c, d}: ...

This is a lot. Let me focus on the specific initial all-1s case and compute forward.

Actually, let me just carefully compute n=6 using the endgame values.

Let me define states by their sorted multiset and compute V bottom-up.

2-number states: V({a,b}) = 2 if a≠b, 1 if a=b.
3-number states: V({a≥b≥c}) = 3 if a>b+c, 1 if a=b+c, 2 if a<b+c.

4-number states: V({a≥b≥c≥d}) = max over A's pairs of (min over B's choices of V(3-state)), where the 3-state is the result. But also check if 4-state is terminal: if a > b+c+d, V = 4. But we assume balanced (2a ≤ T), so not terminal.

Wait, but also after A picks and B responds, we get a 3-state which might be terminal (V=3) or not (V=1 or 2). So V(4-state) = max_A min_B V(3-state-result).

Let me compute V for relevant 4-states.

Let me compute V({1,1,1,1}) = f(4). 
Pairs and results:
- Pick {1,1} (any two): B writes 2 → {2,1,1} (3-state, a=2,b=1,c=1, a=2, b+c=2, a=b+c → V=1). B writes 0 → {1,1,0} = {1,1,0}, sorted {1,1,0}: a=1,b=1,c=0, a=1, b+c=1, a=b+c → V=1. 
  So min_B = 1.
So V({1,1,1,1}) = 1. ✓ (matches f(4)=1).

V({2,1,1}) = 1 (a=2,b=1,c=1, a=b+c). ✓.
V({0,1,1}) = {1,1,0}: a=1,b=1,c=0, a=b+c → V=1?? But earlier I computed {0,1,1} → 2 cookies!

Wait, discrepancy. Let me recheck. {0,1,1}: sorted a=1, b=1, c=0. a = b + c? 1 = 1 + 0 = 1. Yes a = b+c. So V = 1 by my formula. But earlier I computed {0,1,1} → 2 cookies (A picks {1,1}, B writes 2 → {0,2} terminal 2 cookies, or 0 → {0,0} terminal 2 cookies).

Contradiction! Let me recheck the 3-state formula for a = b+c.

{1,1,0}: a=1, b=1, c=0. a = b+c = 1. 
A picks {a,b} = {1,1}: B writes 2 → {2, 0} (2-number, 2≠0, V=2). B writes 0 → {0, 0} (2-number, 0=0, V=1). B minimizes → writes 0 → V=1.
A picks {a,c} = {1,0}: B writes 1 → {1,1} (V=1). B writes 1 → same. V=1.
A picks {b,c} = {1,0}: B writes 1 → {1,1} (V=1). V=1.
A maximizes: max(1, 1, 1) = 1. So V({1,1,0}) = 1.

But earlier I said {0,1,1} → A picks {1,1} → B writes 2 → {0,2} (terminal, 2 cookies) or 0 → {0,0} (terminal, 2 cookies), both 2 cookies. 

Error! {0,0} is all zeros, terminal, but with 2 numbers → 2 cookies. {0,2}: 2 > 0, terminal, 2 cookies. So both give 2 cookies, A gets 2.

But wait, that contradicts the formula. Let me recheck. {0,2} is a 2-number state {2, 0}: 2 ≠ 0, so V = 2. {0,0} is 2-number state {0,0}: 0 = 0, V = 1 (not terminal, one more round → 1 number → 1 cookie).

OH. {0,0} is NOT terminal! All zeros means all numbers are zero. {0, 0} has two zeros. Is that "all zeros"? Yes! Condition (2): "there are only zeros on the blackboard." {0,0} is all zeros. So it IS terminal with 2 cookies!

I made an error in my 2-number formula. Let me redo.

2-number state {a, b}: 
- If a > b: condition (1), a > b = sum of others. Terminal, 2 cookies.
- If a = b > 0: not terminal (a = b, a > b false; not all zeros). A picks {a,a}: B writes 2a → {2a} (1 number, terminal, 1 cookie) or 0 → {0} (1 number, all zero, terminal, 1 cookie). V = 1.
- If a = b = 0: all zeros, terminal, 2 cookies!
- If a > 0, b = 0: a > 0 = sum of others, terminal, 2 cookies.

So V({a,b}) = 2 if a ≠ b OR (a = b = 0); V({a,b}) = 1 if a = b > 0.

Let me redo: {0,0}: all zeros → V = 2. {0,2}: 2 ≠ 0 → V = 2. {1,1}: 1=1>0 → V=1. {2,2}: V=1. {0,1}: 1≠0 → V=2.

Now redo 3-state {1,1,0}: a=1,b=1,c=0, a=b+c=1.
A picks {1,1}: B writes 2 → {2,0} (V=2); B writes 0 → {0,0} (V=2). min = 2.
A picks {1,0}: B writes 1 → {1,1} (V=1). min = 1.
A picks {1,0} (other): same, V=1.
A maximizes: max(2, 1, 1) = 2. So V({1,1,0}) = 2. ✓ matches earlier.

So my 3-state formula was wrong because I didn't account for {0,0} being terminal. Let me redo the 3-state analysis.

3-state {a ≥ b ≥ c ≥ 0}, not all zero, balanced (a ≤ b+c, non-terminal by condition 1; and not all zeros).

A picks a pair, B responds → 2-state. A maximizes, B minimizes.

A's pairs: {a,b}, {a,c}, {b,c}.

{a,b}: B writes a+b → {a+b, c}. B writes a-b → {a-b, c} (a ≥ b so a-b ≥ 0).
{a,c}: B writes a+c → {a+c, b}. B writes a-c → {a-c, b}.
{b,c}: B writes b+c → {b+c, a}. B writes b-c → {b-c, a}.

2-state V: V({x,y}) = 2 if x≠y or x=y=0; 1 if x=y>0.

For each pair, B minimizes V over the two choices. A maximizes over pairs.

Let me compute for the three cases:

Case a < b+c (strict):
- {a,b}: a+b vs c. a+b ≥ a ≥ c. a+b = c? Only if a+b=c, impossible (a ≥ c, b ≥ 0, a+b ≥ c, equality iff a=c,b=0; then a < b+c = c, so a < c, contradiction with a ≥ c). So a+b > c, V({a+b,c}) = 2. a-b vs c: a-b could be <, =, > c. 
  - If a-b > c: V=2. If a-b = c: V({c,c}) = 1 (if c > 0) or 2 (if c = 0). If a-b < c: V=2.
  - a-b = c iff a = b+c, but a < b+c, so a-b < c. So V({a-b, c}) = 2 (since a-b < c, unequal). 
  - Unless a-b = c... no, a < b+c → a - b < c. So a - b < c, V = 2.
  - But wait, what if a - b = c? That needs a = b + c, excluded. So a - b < c strictly, V = 2.
  - Edge: a - b = 0 and c = 0? a = b, c = 0, a < b + 0 = b = a, contradiction (a < a). So no.
  - So min_B for {a,b} = min(2, 2) = 2.
- {a,c}: a+c vs b. a+c ≥ a ≥ b. a+c = b iff a+c = b, but a ≥ b so a+c ≥ b, equality iff a=b, c=0. Then a = b, c = 0, a < b+c = a, contradiction. So a+c > b, V = 2. a-c vs b: a-c vs b. a-c = b iff a = b+c, excluded. a-c < b or > b. a - c vs b: a - c = b - (c - (a-b))... let me just: a - c > b iff a > b + c, excluded. a - c < b iff a < b + c, true. So a - c < b, V = 2. (Unless a-c = b, excluded.) 
  - Edge: a-c = 0 and b = 0? a = c, b = 0, a < 0 + c = c = a, contradiction. No.
  - min_B = 2.
- {b,c}: b+c vs a. b+c > a (strict, since a < b+c). V({b+c, a}) = 2 (b+c ≠ a since b+c > a). b-c vs a. b - c ≥ 0. b-c vs a: b - c ≤ b ≤ a. b - c = a iff b = a + c, but b ≤ a so b ≤ a < a + c (if c > 0), so b < a + c, b - c < a. If c = 0: b - 0 = b ≤ a, b = a iff b = a. If b = a, c = 0: then a < b + c = a, contradiction. So b < a, b - c < a. V({b-c, a}) = 2 (b-c < a, unequal). 
  - Edge: b - c = a? No (shown). b - c = 0 and a = 0? a = 0 means all zero, excluded.
  - min_B = 2.
So if a < b+c (strict), V = 2. ✓.

Case a = b+c:
- {a,b}: a+b vs c. a+b = b+c+b = 2b+c > c (if b > 0 or c > 0; not all zero so at least one > 0; a = b+c > 0 so b+c > 0). V = 2. a-b = c → {c, c}. V({c,c}) = 1 if c > 0, 2 if c = 0. 
  - If c > 0: min_B = min(2, 1) = 1.
  - If c = 0: a = b, {a-b, c} = {0, 0}, V = 2. min_B = min(2, 2) = 2.
- {a,c}: a+c vs b. a+c = b+c+c = b+2c. vs b: b+2c > b if c > 0; = b if c = 0. 
  - If c > 0: a+c > b, V = 2. a-c = b → {b, b}, V = 1 (b > 0 since a = b+c > 0 and c > 0 means b could be 0... a = b + c, c > 0, a > 0. b could be 0. If b = 0: {0,0}, V = 2. If b > 0: V = 1.) 
    Hmm, so if c > 0 and b > 0: min_B = min(2, 1) = 1. If c > 0 and b = 0: a = c, {a,c} = {c, c}, a-c = 0, {0, b} = {0, 0}, V = 2; a+c = 2c vs b = 0, V = 2. min_B = 2. But b = 0, c > 0, a = c: state {c, 0, c} = {c, c, 0}, a = c, b = c, c = 0... wait sorted: a ≥ b ≥ c, a = c (the value), b = 0... no. Let me re-set. State {a, b, c} with a = b + c. If b = 0: a = c, state {c, 0, c} sorted {c, c, 0}: a=c, b=c, c=0. a = b + c = c + 0 = c. ✓. So a = c, b = c, c = 0 (using c for both the value and third element is confusing). Let me rename: state {p, q, r} sorted p ≥ q ≥ r, p = q + r. If q = 0: p = r, but p ≥ q ≥ r means p ≥ 0 ≥ r, and r ≥ 0, so r = 0, p = 0, all zero. Excluded. So q > 0 (if not all zero and p = q + r). Actually if q = 0 and r = 0: p = 0, all zero. If q = 0, r > 0: p = r, but p ≥ q = 0 and q ≥ r means 0 ≥ r, so r ≤ 0, r = 0. Contradiction. So q > 0 always when p = q+r and not all zero. Good, so b > 0 (using b for the middle).
  - So c > 0 (the third, r > 0) or c = 0 (r = 0).
  - Subcase r > 0 (c > 0): b > 0 (shown). {a,b}: min = 1. {a,c}: a+c > b, V=2; a-c = b, {b,b}, V=1. min = 1. {b,c}: b+c = a, {a, a}, V=1 (a > 0). b-c vs a: b - c < b ≤ a... b - c = a? b = a + c, but b ≤ a, so b ≤ a < a + c (c > 0), no. b - c < a, V = 2. min_B = min(1, 2) = 1. So all pairs give min_B = 1. V = 1.
  - Subcase r = 0 (c = 0): p = q, state {p, p, 0}. {a,b} = {p, p}: B writes 2p → {2p, 0}, V = 2. B writes 0 → {0, 0}, V = 2. min = 2. {a,c} = {p, 0}: B writes p → {p, p}, V = 1. B writes p → same. min = 1. {b,c} = {p, 0}: same, min = 1. A maximizes: max(2, 1, 1) = 2. V = 2.
  
So case a = b+c: 
- If c > 0 (third element positive): V = 1.
- If c = 0 (state {a, a, 0}): V = 2.

Interesting! So {a, a, 0} (a > 0) has V = 2, not 1.

Let me recheck {1,1,0}: a=1,b=1,c=0, a = b+c = 1, c = 0. V = 2. ✓ (matches).

And {2,1,1}: a=2,b=1,c=1, a=b+c=2, c=1>0. V = 1. ✓.

Now let me also handle case a > b+c: terminal, V = 3.

And the all-zeros 3-state: V = 3 (terminal, 3 cookies).

Summary for 3-state {a ≥ b ≥ c} (not all zero):
- a > b+c: V = 3.
- a = b+c, c > 0: V = 1.
- a = b+c, c = 0 (i.e., {a,a,0}): V = 2.
- a < b+c: V = 2.

Hmm wait, a = b+c, c = 0 means a = b, state {a, a, 0}. And a < b+c with c = 0 means a < b, but a ≥ b, contradiction. So if c = 0: either a > b (terminal, V=3) or a = b (V=2). 

Let me now recompute f(5) and f(6) with corrected formulas.

First, 4-state values. Let me compute V for 4-state {a ≥ b ≥ c ≥ d}, balanced (a ≤ b+c+d), not all zero.

V(4-state) = max over A's pairs of min over B's choices of V(3-state result).

Let me compute V({1,1,1,1}):
Only pair type {1,1}. B writes 2 → {2,1,1} (V: a=2,b=1,c=1, a=b+c, c=1>0 → V=1). B writes 0 → {1,1,0} (V: a=1,b=1,c=0, a=b+c, c=0 → V=2). min_B = min(1, 2) = 1. V({1,1,1,1}) = 1. ✓.

V({2,1,1,1}): a=2,b=1,c=1,d=1, T=5, 2a=4 ≤ 5, balanced.
Pairs:
- {2,1}: B writes 3 → {3,1,1} (a=3,b=1,c=1, a=3 > b+c=2 → V=3). B writes 1 → {1,1,1} (a=1,b=1,c=1, a=1 < b+c=2 → V=2). min_B = min(3, 2) = 2.
- {1,1}: B writes 2 → {2,2,1} (a=2,b=2,c=1, a=2 < b+c=3 → V=2). B writes 0 → {2,1,0} (a=2,b=1,c=0, a=2 > b+c=1 → V=3). min_B = min(2, 3) = 2.
A maximizes: max(2, 2) = 2. V({2,1,1,1}) = 2. ✓ (matches earlier).

V({0,1,1,1}): a=1,b=1,c=1,d=0, T=3, 2a=2 ≤ 3, balanced.
Pairs:
- {1,1}: B writes 2 → {2,1,0} (a=2,b=1,c=0, a=2 > b+c=1 → V=3). B writes 0 → {1,0,0} (a=1,b=0,c=0, a=1 > b+c=0 → V=3). min_B = 3.
- {1,0}: B writes 1 → {1,1,1} (V=2). B writes 1 → same. min_B = 2.
A maximizes: max(3, 2) = 3. V({0,1,1,1}) = 3. ✓ (matches earlier, {0,1,1,1} → 3 cookies).

So f(5): A picks {1,1}, B writes 2 → {2,1,1,1} (V=2) or 0 → {0,1,1,1} (V=3). B minimizes → writes 2 → V=2. f(5) = 2. ✓.

Now f(6): {1^6}. A picks {1,1}. B writes 2 → {2,1,1,1,1} (5-state) or 0 → {0,1,1,1,1} (5-state). Need V for these 5-states.

5-state V = max over A's pairs of min over B's choices of V(4-state result). (Assuming 5-state not terminal.)

Let me compute V({2,1,1,1,1}): a=2,b=1,c=1,d=1,e=1, T=6, 2a=4 ≤ 6, balanced.
Pairs (by type):
- {2,1}: B writes 3 → {3,1,1,1} (4-state). B writes 1 → {1,1,1,1} (V=1).
- {1,1}: B writes 2 → {2,2,1,1} (4-state). B writes 0 → {2,1,1,0} (4-state).

Need V({3,1,1,1}), V({2,2,1,1}), V({2,1,1,0}).

V({3,1,1,1}): a=3,b=1,c=1,d=1, T=6, 2a=6 ≤ 6, balanced (boundary).
Pairs:
- {3,1}: B writes 4 → {4,1,1} (a=4,b=1,c=1, a=4 > b+c=2 → V=3). B writes 2 → {2,1,1} (a=2,b=1,c=1, a=b+c=2, c=1>0 → V=1). min_B = min(3,1) = 1.
- {1,1}: B writes 2 → {3,2,1} (a=3,b=2,c=1, a=3 = b+c=3, c=1>0 → V=1). B writes 0 → {3,1,0} (a=3,b=1,c=0, a=3 > b+c=1 → V=3). min_B = min(1,3) = 1.
A maximizes: max(1, 1) = 1. V({3,1,1,1}) = 1
