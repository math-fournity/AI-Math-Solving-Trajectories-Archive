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
  <problem_id>polymath_01696</problem_id>
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

There are $2n-1$ light bulbs in a row. Initially, the middle ($n$-th) bulb is on, and all others are off. In one step, you can choose two non-adjacent bulbs that are currently off, such that all bulbs between them are currently on, and change the state of those two bulbs as well as all bulbs between them. For $n = 10$, find the maximum number of steps that can be performed.

## Standard Solution

The maximum number of steps is given by the formula $\lfloor \frac{2^{n+1}-5}{3} \rfloor$. This formula is derived by assigning values $2^{|i-n|}$ to each bulb and observing that each step increases the total value of lit bulbs by a multiple of 3. For $n = 10$, the formula gives $\lfloor \frac{2^{11}-5}{3} \rfloor = \lfloor \frac{2048-5}{3} \rfloor = \lfloor \frac{2043}{3} \rfloor = 681$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have $2n-1$ light bulbs in a row, indexed $1, 2, \ldots, 2n-1$. Initially, the middle bulb (position $n$) is on, all others off.

In one step: choose two non-adjacent bulbs that are currently **off**, such that all bulbs between them are currently **on**, and change the state of those two bulbs AND all bulbs between them.

So we pick positions $i < j$ where:
- $j - i \geq 2$ (non-adjacent)
- bulbs $i$ and $j$ are off
- bulbs $i+1, i+2, \ldots, j-1$ are all on

Then we flip all of $i, i+1, \ldots, j$ (the two endpoints and everything between).

After the flip: bulbs $i$ and $j$ become on, and bulbs $i+1, \ldots, j-1$ become off.

For $n = 10$, we have $19$ bulbs, middle is position $10$.

Let me think about this as a combinatorial game. Let me denote the state as a binary string of length $2n-1$.

Initial state: $0000000001000000000$ (position 10 is 1, rest 0).

The operation: find a substring $0\, 1^k\, 0$ where $k \geq 1$ (so the two 0's are non-adjacent, meaning $k \geq 1$), and flip it to $1\, 0^k\, 1$.

Wait, let me re-read. "two non-adjacent bulbs that are currently off" — non-adjacent means $j - i \geq 2$, i.e., there's at least one bulb between them. "all bulbs between them are currently on" — so $i+1, \ldots, j-1$ are all on. So the pattern is $0\, 1\, 1\, \ldots\, 1\, 0$ with at least one 1 in between.

After flipping: $1\, 0\, 0\, \ldots\, 0\, 1$.

So the operation transforms $0\, 1^k\, 0 \to 1\, 0^k\, 1$ for $k \geq 1$.

This is interesting. Let me think about what invariants or potential functions exist.

Let me think of this differently. Consider the "blocks" of consecutive on-bulbs. Initially, there's one block of size 1 at position 10.

The operation $0\, 1^k\, 0 \to 1\, 0^k\, 1$: this takes a block of $k$ consecutive on-bulbs (with off-bulbs on both sides) and replaces it with two on-bulbs at the ends with $k$ off-bulbs between them.

So a block of size $k$ (with off neighbors on both sides) gets replaced by two single on-bulbs separated by $k$ off-bulbs. But wait, the two new on-bulbs might merge with adjacent on-bulbs.

Hmm, let me think more carefully. The block of $k$ on-bulbs must have off-bulbs immediately on both sides (since the endpoints of our operation are off). After the operation, the $k$ on-bulbs become off, and the two off endpoints become on.

Let me think about this as a tree/recursive structure. 

Actually, let me think about it recursively. Consider a block of $k$ consecutive on-bulbs. We can "split" it: choose the leftmost and rightmost... no wait, we need to choose two off bulbs with all on between them.

Let me reconsider. The operation requires a pattern $0\, 1^k\, 0$ in the current state. This means we need a contiguous block of on-bulbs of size $k \geq 1$, with off-bulbs on both sides.

After the operation, this becomes $1\, 0^k\, 1$. Now the two new on-bulbs are isolated (surrounded by off-bulbs, unless they merge with adjacent on-bulbs).

Now we have two blocks of size 1 (the new on-bulbs), and between them a gap of $k$ off-bulbs. But also, the new on-bulbs might be adjacent to other on-bulbs from neighboring blocks.

Wait, actually, the original block of $k$ on-bulbs had off-bulbs on both sides (that's required for the operation). After the operation, those off-bulbs become on. So if there were other on-bulbs adjacent to those off-bulbs... no, the off-bulbs were off, and beyond them could be anything.

Let me think about this more carefully with a potential function or invariant.

Let me consider the positions $1, \ldots, 2n-1$ and think about what happens.

Let me try small cases first.

$n = 1$: 1 bulb, it's on. No operation possible (need two off bulbs). Max steps = 0.

$n = 2$: 3 bulbs. Initial: $010$. We need $0\,1^k\,0$ with $k \geq 1$. The pattern is positions 1,2,3 = $0,1,0$. So $k=1$, we flip to $101$. Now state is $101$. Can we do more? We need $0\,1^k\,0$. The on-bulbs are at positions 1 and 3, off at position 2. We need two off bulbs that are non-adjacent with all on between. Only one off bulb (position 2), so no. Max steps = 1.

$n = 3$: 5 bulbs. Initial: $00100$. 
Step 1: positions 2,3,4 = $0,1,0$ → flip to $1,0,1$. State: $01010$.
Now on-bulbs at 2,4. Off at 1,3,5. 
Can we do $0\,1^k\,0$? 
- Positions 1,2,3 = $0,1,0$: yes! Flip to $1,0,1$. State: $10010$.
  Or positions 3,4,5 = $0,1,0$: flip to $1,0,1$. State: $01001$.
  
Let's follow $10010$: on at 1,4. Off at 2,3,5.
- Pattern $0\,1^k\,0$: positions 2,3,4,5 = $0,0,1,0$ — no, position 3 is off. 
  positions 3,4,5 = $0,1,0$: yes! Flip to $1,0,1$. State: $10101$.
  Now on at 1,3,5. Off at 2,4. No two off bulbs with all on between (need non-adjacent off bulbs with on between; positions 2 and 4: between them is position 3 which is on. So $0\,1\,0$ at positions 2,3,4. Yes! Flip to $1,0,1$. State: $11111$.
  Hmm wait, that gives all on. Can we continue? No off bulbs, so no.

Wait, let me recount. $10101$: positions 1,3,5 on; 2,4 off. 
Operation on positions 2,3,4 ($0,1,0$): flip to $1,0,1$. State becomes $1,1,0,1,1$ = $11011$. 
On at 1,2,4,5. Off at 3. Only one off bulb, can't do anything. 

Hmm, so that path gives 4 steps. Let me recount.

$n=3$: $00100$ → step 1: $01010$ → step 2: $10010$ → step 3: $10101$ → step 4: $11011$. Total 4 steps.

But can we do better? Let me try another path.

$00100$ → $01010$ → $01001$ (flip positions 3,4,5). On at 2,5. Off at 1,3,4.
- Pattern: positions 1,2,3 = $0,1,0$. Flip: $1,0,1$. State: $10001$. On at 1,5. Off at 2,3,4.
  - Pattern: positions 2,3,4,5 = $0,0,0,1$ — no. positions 1,...,5: need $0\,1^k\,0$. On at 1 and 5. Between 1 and 5: positions 2,3,4 all off. So we need two off bulbs with all on between. Positions 2 and 4: between is position 3, which is off. No. Positions 2 and 5: position 5 is on, not off. Hmm.
  - Actually we need both endpoints off. On-bulbs at 1,5. Off at 2,3,4. We need $i < j$ both off, non-adjacent, all between on. But all between any two of {2,3,4} are off, not on. So no operation possible. Total: 3 steps.

So the first path was better with 4 steps. Let me see if 4 is optimal for $n=3$.

Actually wait, let me try yet another path from $01010$.

$01010$ → flip positions 1,2,3 ($0,1,0$): $10010$. Then as above, 4 total.
$01010$ → flip positions 3,4,5 ($0,1,0$): $01001$. Then as above, 3 total.

From $10010$: on at 1,4. Off at 2,3,5.
- positions 3,4,5 = $0,1,0$: flip → $10101$. Then → $11011$. 4 total.
- Any other? positions 2,3,4 = $0,0,1$ — no. positions 2,3 = adjacent. So only one option.

From $10101$: on at 1,3,5. Off at 2,4.
- positions 2,3,4 = $0,1,0$: flip → $11011$. 4 total.
- That's the only option (only two off bulbs, at 2 and 4, with position 3 on between).

From $11011$: on at 1,2,4,5. Off at 3. Only one off bulb. Done. 4 total.

So for $n=3$, max is 4.

Let me also check $n=2$: max is 1. $n=1$: max is 0.

Sequence so far: 0, 1, 4, ...

Let me think about $n=4$: 7 bulbs. Initial: $0001000$.

This is getting complex. Let me think about the structure more carefully.

Let me think about this recursively. Consider a block of $k$ on-bulbs (contiguous). The operation splits it: $0\,1^k\,0 \to 1\,0^k\,1$. This creates two on-bulbs at distance $k+1$ apart, with $k$ off-bulbs between them.

Now, each of these two on-bulbs can be thought of as the "seed" for further operations, but they interact with their neighbors.

Actually, let me think about this differently. Let me consider the problem as building a binary tree.

When we have a single on-bulb at position $p$ (the middle), and we perform an operation, we're essentially "expanding" the on-bulb into two on-bulbs at the boundaries, with the interior becoming off.

Let me think of it as: we start with one "active" region. Each operation on a block of size $k$ replaces it with two blocks of size 1 (the endpoints) with a gap of $k$ off-bulbs between them.

But the two new on-bulbs can then grow by interacting with their neighbors.

Hmm, let me think about this more carefully using the concept of "intervals" or "gaps".

Actually, let me think about the total number of on-bulbs. Initially 1 on-bulb. Each operation $0\,1^k\,0 \to 1\,0^k\,1$: we had $k$ on-bulbs in the block, plus 2 off endpoints. After: 2 on endpoints, $k$ off interior. So the number of on-bulbs changes by $2 - k$. 

For $k=1$: on-bulbs increase by 1. ($0\,1\,0 \to 1\,0\,1$: 1 on → 2 on)
For $k=2$: on-bulbs stay same. ($0\,1\,1\,0 \to 1\,0\,0\,1$: 2 on → 2 on)
For $k \geq 3$: on-bulbs decrease.

To maximize the number of steps, we want to keep going as long as possible. Each step either increases, maintains, or decreases the number of on-bulbs.

Let me think about an invariant. 

Consider the sum $\sum_{i: \text{on}} i$ (sum of positions of on-bulbs). 

Operation on positions $a, a+1, \ldots, b$ where $a$ and $b$ are off, $a+1, \ldots, b-1$ are on. Block size $k = b - a - 1$.

Before: on-bulbs at $a+1, \ldots, b-1$. Sum = $\sum_{j=a+1}^{b-1} j = \frac{(b-1)b}{2} - \frac{a(a+1)}{2} = \frac{(b-a-1)(a+b)}{2} = \frac{k(a+b)}{2}$.

After: on-bulbs at $a$ and $b$. Sum = $a + b$.

Change in sum: $(a+b) - \frac{k(a+b)}{2} = (a+b)(1 - k/2) = (a+b)\frac{2-k}{2}$.

For $k=1$: change = $(a+b)/2$. 
For $k=2$: change = 0.
For $k=3$: change = $-(a+b)/2$.

Hmm, this doesn't immediately give a clean invariant.

Let me think about parity. The sum of positions of on-bulbs modulo something?

Actually, let me think about this problem differently. Let me consider the "spread" of on-bulbs.

Let me think about the leftmost and rightmost on-bulbs. Initially, both are at position $n$. 

When we do an operation on $[a, b]$ (with $a, b$ off, interior on), the leftmost on-bulb can only move left (if $a$ is to the left of the current leftmost on-bulb) or the rightmost can move right. Actually, the operation turns $a$ and $b$ on, so if $a$ is left of the current leftmost on-bulb, the leftmost extends left. Similarly for $b$.

But the operation also turns off the interior, so some on-bulbs in the interior become off.

Hmm, let me think about the leftmost on-bulb position $L$ and rightmost on-bulb position $R$. 

Initially $L = R = n$. The "span" is $R - L + 1 = 1$.

Each operation on $[a,b]$: $a$ and $b$ become on. If $a < L$, then $L$ decreases to $a$. If $b > R$, then $R$ increases to $b$. But also, some interior on-bulbs become off, which might change $L$ or $R$ if the leftmost/rightmost on-bulb was in the interior.

Wait, the operation requires $a$ and $b$ to be off, and the interior $a+1, \ldots, b-1$ to be on. So the block $[a+1, b-1]$ is a contiguous block of on-bulbs. After the operation, $a$ and $b$ become on, and $a+1, \ldots, b-1$ become off.

If this block was the leftmost block of on-bulbs, then after the operation, the leftmost on-bulb moves to $a$ (which is further left). Similarly for the rightmost.

If this block was an interior block (with on-bulbs to its left and right), then after the operation, $a$ and $b$ become on, but they might merge with adjacent on-bulbs.

This is getting complicated. Let me try to think about it as a recursive splitting process.

Let me define $f(n)$ as the maximum number of steps starting from a single on-bulb in the middle of $2n-1$ bulbs.

Actually, let me think about it more generally. Consider a configuration where we have a contiguous block of $m$ on-bulbs, with off-bulbs extending infinitely (or sufficiently far) on both sides. What's the maximum number of operations we can perform?

Let $g(m)$ = max operations starting from a block of $m$ on-bulbs (with enough off-bulbs on both sides).

For the original problem, we start with a block of 1 on-bulb in the middle of $2n-1$ bulbs, so we need the off-bulbs to extend at least $n-1$ on each side. But if $g(m)$ operations never spread beyond a certain range, we need to be careful.

Actually, let me think about what $g(m)$ looks like.

$g(1)$: We have $\ldots 0\,1\,0 \ldots$. We can do the operation: $0\,1\,0 \to 1\,0\,1$. Now we have two on-bulbs separated by one off-bulb. 

Now we have $\ldots 0\,1\,0\,1\,0 \ldots$. We can operate on the left $0\,1\,0$ (positions around the left on-bulb) or the right $0\,1\,0$.

If we operate on the left: $0\,1\,0 \to 1\,0\,1$, giving $\ldots 1\,0\,1\,0\,1\,0 \ldots$ wait, that's not right. Let me be more careful.

After first operation on a block of 1: we had $\ldots 0\,a\,0 \ldots$ where $a$ is the on-bulb. After: $\ldots 1\,0\,1 \ldots$ The two new on-bulbs are at distance 2 apart (with one off between).

Now the state is $\ldots 0\,1\,0\,1\,0 \ldots$ (assuming the neighbors beyond are off). We have two blocks of size 1, separated by one off-bulb.

We can operate on the left block: $0\,1\,0 \to 1\,0\,1$. But wait, the right neighbor of the left on-bulb is the off-bulb between the two on-bulbs, and the left neighbor is an off-bulb. So we can do $0\,1\,0$ on the left, giving $1\,0\,1\,0\,1\,0\ldots$ wait, I need to be more careful about positions.

Let me use explicit positions. Say the initial on-bulb is at position 0. Neighbors at -1 and 1 are off.

State: $\ldots 0_{-2}\, 0_{-1}\, 1_0\, 0_1\, 0_2 \ldots$

Step 1: operate on $[-1, 1]$: $0_{-1}\,1_0\,0_1 \to 1_{-1}\,0_0\,1_1$. State: $\ldots 0_{-2}\, 1_{-1}\, 0_0\, 1_1\, 0_2 \ldots$

Step 2a: operate on $[-2, 0]$: $0_{-2}\,1_{-1}\,0_0 \to 1_{-2}\,0_{-1}\,1_0$. State: $\ldots 1_{-2}\, 0_{-1}\, 1_0\, 1_1\, 0_2 \ldots$

Now positions 0 and 1 are both on, forming a block of size 2. 

Step 2b (alternative): operate on $[0, 2]$: $0_0\,1_1\,0_2 \to 1_0\,0_1\,1_2$. State: $\ldots 0_{-2}\, 1_{-1}\, 1_0\, 0_1\, 1_2 \ldots$

Now positions -1 and 0 are both on, forming a block of size 2.

Let me follow step 2a: state is $\ldots 0_{-3}\, 1_{-2}\, 0_{-1}\, 1_0\, 1_1\, 0_2 \ldots$

We have a block of size 2 at positions 0,1, and a single on at -2.

Step 3: We can operate on the block of size 2: $0_{-1}\,1_0\,1_1\,0_2 \to 1_{-1}\,0_0\,0_1\,1_2$. State: $\ldots 1_{-2}\, 1_{-1}\, 0_0\, 0_1\, 1_2 \ldots$

Now positions -2,-1 form a block of size 2, and position 2 is on. 

Or we can operate on the single at -2: $0_{-3}\,1_{-2}\,0_{-1} \to 1_{-3}\,0_{-2}\,1_{-1}$. State: $\ldots 1_{-3}\, 0_{-2}\, 1_{-1}\, 1_0\, 1_1\, 0_2 \ldots$. Now positions -1,0,1 form a block of size 3.

Hmm, this is getting complicated. Let me think about it differently.

Let me think about the recursive structure. When we have a block of $m$ on-bulbs, we can split it by operating on the whole block (endpoints off, interior all on): $0\,1^m\,0 \to 1\,0^m\,1$. This creates two single on-bulbs at distance $m+1$ apart. Then each of these can independently grow.

But we can also operate on sub-blocks. For instance, if we have a block of size 3, we could first split it into two singles (by operating on the whole block), or we could operate on a sub-block of size 1 within it.

Wait, can we operate on a sub-block? If we have $0\,1\,1\,1\,0$ (block of size 3), we can operate on $0\,1\,0$ within it? No, because the interior of the block is all 1's, so there's no $0\,1\,0$ pattern within the block. The only $0\,1^k\,0$ pattern is the whole block $0\,1\,1\,1\,0$ (with $k=3$) or we could take a sub-pattern like $0\,1\,1\,0$ (the left two 1's with the surrounding 0's), but that requires the endpoints to be off and interior on. $0\,1\,1\,0$ has $k=2$, endpoints at the 0's. But the 0 on the right is the same 0 that's the right boundary. So yes, we can operate on $0\,1\,1\,0$ (a sub-block of size 2 within the block of 3).

Wait, but the block of 3 is $1\,1\,1$ with 0's on both sides. So the pattern is $0\,1\,1\,1\,0$. We can choose:
- $k=3$: operate on the whole thing, $0\,1\,1\,1\,0 \to 1\,0\,0\,0\,1$.
- $k=2$: operate on $0\,1\,1\,0$ (left 0, two 1's, right 0 of the block). But wait, the right 0 is the same as the boundary 0. So this is valid: $0\,1\,1\,0 \to 1\,0\,0\,1$. Result: $1\,0\,0\,1\,1\,0$... no wait.

Let me be more careful. Block of 3 at positions 1,2,3. Positions 0 and 4 are off. State: $0_0\, 1_1\, 1_2\, 1_3\, 0_4$.

Option A: operate on $[0, 4]$, $k=3$: $0\,1\,1\,1\,0 \to 1\,0\,0\,0\,1$. State: $1_0\, 0_1\, 0_2\, 0_3\, 1_4$.

Option B: operate on $[0, 3]$, $k=2$: positions 0 (off), 1,2 (on), 3 (on)... wait, position 3 is on, not off. We need both endpoints off. Position 3 is on. So we can't use position 3 as an endpoint.

Hmm, so within $0\,1\,1\,1\,0$, the only off positions are 0 and 4. So the only valid operation is on $[0, 4]$ with $k=3$.

OK so for a contiguous block of on-bulbs with off on both sides, the only operation is to split the entire block. We can't split a sub-block because there are no off bulbs within the block.

But after splitting, we get two on-bulbs with off between them, and then each can be split further, and the off-bulbs between them can become part of new operations.

Let me reconsider. After splitting a block of size $m$: $0\,1^m\,0 \to 1\,0^m\,1$. Now we have two on-bulbs at the ends, with $m$ off-bulbs between them. Each on-bulb is a block of size 1, and can be split: $0\,1\,0 \to 1\,0\,1$.

But when we split the left on-bulb, we need an off-bulb to its left. If there is one, we get $1\,0\,1\,0^m\,1$ (the left on-bulb at position $a$ becomes $1_{a-1}\,0_a\,1_{a+1}$, but position $a+1$ was already off, so now it's on). Wait, let me be precise.

Say the block was at positions $1, \ldots, m$ with 0's at 0 and $m+1$. After splitting: on at 0 and $m+1$, off at $1, \ldots, m$.

Now, the on-bulb at position 0: its left neighbor (position -1) might be off (if we have room). Its right neighbor (position 1) is off. So we can split it: $0_{-1}\,1_0\,0_1 \to 1_{-1}\,0_0\,1_1$. Now position 1 is on.

Similarly, the on-bulb at position $m+1$: its right neighbor (position $m+2$) might be off. Its left neighbor (position $m$) is off. Split: $0_m\,1_{m+1}\,0_{m+2} \to 1_m\,0_{m+1}\,1_{m+2}$.

After splitting both: on at $-1, 1, m, m+2$, off at $0, 2, \ldots, m-1, m+1$.

Now we have two blocks of size 1 at positions $-1, 1$ (separated by off at 0) and two at $m, m+2$ (separated by off at $m+1$). And between positions 1 and $m$, there are off-bulbs at $2, \ldots, m-1$ (if $m \geq 3$).

Hmm wait, positions 1 and $m$ are both on now. Between them: positions $2, \ldots, m-1$ are off. So if $m-1 \geq 2$, i.e., $m \geq 3$, we can't directly operate on $[1, m]$ because the interior is off, not on.

But we can operate on the blocks of size 1 at $-1, 1$ and $m, m+2$ further.

This is getting complicated. Let me try to think about it as a tree structure.

Actually, I think this problem is related to a binary tree / Catalan number structure. Let me think about it differently.

Let me define the problem in terms of "intervals." Consider the set of on-bulbs. The operation takes a contiguous block of on-bulbs (with off on both sides) and replaces it with two on-bulbs at the ends.

Let me think about the process as building a binary tree. The root is the initial on-bulb. When we split a block of size $m$ into two on-bulbs at the ends, we create two children. Each child can then be split further.

But the key constraint is that the two children are at specific positions, and further splits of one child might interact with the other child.

Hmm, let me think about this more carefully. Let me consider the "gap" between the two children. After splitting a block of size $m$ at positions $[a+1, \ldots, a+m]$ (with off at $a$ and $a+m+1$), we get on-bulbs at $a$ and $a+m+1$, with off at $a+1, \ldots, a+m$.

Now, when we split the left child (at position $a$), we turn on $a-1$ and $a+1$. Now $a+1$ is on, which is adjacent to the gap. Similarly, splitting the right child turns on $a+m$ and $a+m+2$.

After splitting both children: on at $a-1, a+1, a+m, a+m+2$. Now positions $a+1$ and $a+m$ are on, with off at $a+2, \ldots, a+m-1$ between them (if $m \geq 3$).

If $m = 1$: after splitting, on at $a-1, a+1, a+1, a+2$... wait, $m=1$ means the block was size 1 at position $a+1$, and after splitting we get on at $a$ and $a+2$. Then splitting left child (at $a$): on at $a-1, a+1$. Splitting right child (at $a+2$): on at $a+1, a+3$. But $a+1$ is now on from both! So we get on at $a-1, a+1, a+3$ (with $a+1$ being a single on-bulb, not doubled). 

Hmm wait, let me redo this. $m=1$: block at position $a+1$, off at $a$ and $a+2$. Split: on at $a$ and $a+2$, off at $a+1$.

Split left child (at $a$): need off at $a-1$ and $a+1$. $a+1$ is off. So $0_{a-1}\,1_a\,0_{a+1} \to 1_{a-1}\,0_a\,1_{a+1}$. Now on at $a-1, a+1, a+2$.

But $a+1$ and $a+2$ are both on, forming a block of size 2! 

Split right child (at $a+2$): need off at $a+1$ and $a+3$. But $a+1$ is now on (from the previous step). So we can't split the right child anymore (at least not in this way).

Alternatively, we could split the right child first. Split right child (at $a+2$): $0_{a+1}\,1_{a+2}\,0_{a+3} \to 1_{a+1}\,0_{a+2}\,1_{a+3}$. Now on at $a, a+1, a+3$. Positions $a, a+1$ form a block of size 2.

Then split left child (at $a$): need off at $a-1$ and $a+1$. But $a+1$ is now on. Can't.

So after splitting a block of size 1 into two children (distance 3 apart), we can split at most one of the two children before they start interfering. And after splitting one child, we get a block of size 2.

OK this is really getting complex. Let me try to compute $g(m)$ for small $m$ by careful enumeration, possibly with some computational help... but the rules say I can't use tools. Let me think more carefully.

Let me reconsider the problem. Let me think about what configurations are reachable and count the maximum path length.

Actually, let me think about an invariant that bounds the number of steps.

Consider the quantity $S = \sum_{i \text{ on}} 1$ = number of on-bulbs. As computed:
- $k=1$: $\Delta S = +1$
- $k=2$: $\Delta S = 0$  
- $k \geq 3$: $\Delta S = 2 - k < 0$

Consider the quantity $P = \sum_{i \text{ on}} i$ (sum of positions). As computed:
- $\Delta P = (a+b)(2-k)/2$ where $a, b$ are the endpoints.

Consider $Q = \sum_{i \text{ on}} i^2$:
Before: $\sum_{j=a+1}^{b-1} j^2 = \sum_{j=a+1}^{b-1} j^2$.
After: $a^2 + b^2$.
$\Delta Q = a^2 + b^2 - \sum_{j=a+1}^{b-1} j^2$.

$\sum_{j=a+1}^{b-1} j^2 = \sum_{j=1}^{b-1} j^2 - \sum_{j=1}^{a} j^2 = \frac{(b-1)b(2b-1)}{6} - \frac{a(a+1)(2a+1)}{6}$.

This is getting messy. Let me try a different approach.

Let me think about the problem in terms of a potential function that decreases by exactly 1 each step.

Actually, let me think about this problem as related to the number of "gaps" or "boundaries" between on and off bulbs.

Let me define $B$ = number of boundaries (transitions between on and off) in the circular arrangement... but it's not circular. Let me define $B$ = number of $01$ or $10$ transitions in the string.

For a block of $m$ on-bulbs surrounded by off: the boundaries are at the two edges, so $B$ contribution is 2 (assuming the block is interior).

Operation $0\,1^k\,0 \to 1\,0^k\,1$: 
Before: boundaries at $0|1$ and $1|0$ (left edge) and $1|0$ and $0$ (right edge). Actually, the pattern $0\,1^k\,0$ has 2 boundaries (one at each end of the 1-block). After: $1\,0^k\,1$ has 2 boundaries (one at each end of the 0-block). So $B$ doesn't change! That's not helpful.

Hmm. Let me think about this differently.

Let me consider the "weight" $W = \sum_{i \text{ on}} f(i)$ for some function $f$.

For the operation on $[a, b]$ with $k = b-a-1$:
$\Delta W = f(a) + f(b) - \sum_{j=a+1}^{b-1} f(j)$.

If we want $\Delta W$ to be constant (say $-1$) for all valid operations, we need:
$f(a) + f(b) - \sum_{j=a+1}^{b-1} f(j) = -1$ for all $a, b$ with $b - a \geq 2$.

For $b = a + 2$ (i.e., $k = 1$): $f(a) + f(a+2) - f(a+1) = -1$.
For $b = a + 3$ (i.e., $k = 2$): $f(a) + f(a+3) - f(a+1) - f(a+2) = -1$.
For $b = a + 4$ (i.e., $k = 3$): $f(a) + f(a+4) - f(a+1) - f(a+2) - f(a+3) = -1$.

From the first: $f(a+2) = f(a+1) - f(a) - 1$.
From the second: $f(a+3) = -1 - f(a) + f(a+1) + f(a+2) = -1 - f(a) + f(a+1) + f(a+1) - f(a) - 1 = 2f(a+1) - 2f(a) - 2$.
From the third: $f(a+4) = -1 - f(a) + f(a+1) + f(a+2) + f(a+3) = -1 - f(a) + f(a+1) + (f(a+1) - f(a) - 1) + (2f(a+1) - 2f(a) - 2) = -1 - f(a) + f(a+1) + f(a+1) - f(a) - 1 + 2f(a+1) - 2f(a) - 2 = 4f(a+1) - 4f(a) - 4$.

But also from the first equation applied to $a+2$: $f(a+4) = f(a+3) - f(a+2) - 1 = (2f(a+1) - 2f(a) - 2) - (f(a+1) - f(a) - 1) - 1 = f(a+1) - f(a) - 2$.

So we need: $4f(a+1) - 4f(a) - 4 = f(a+1) - f(a) - 2$, which gives $3f(a+1) - 3f(a) = 2$, so $f(a+1) - f(a) = 2/3$.

Then $f$ is linear: $f(i) = \frac{2}{3}i + c$ for some constant $c$.

Check: $f(a) + f(b) - \sum_{j=a+1}^{b-1} f(j) = \frac{2}{3}(a+b) + 2c - \sum_{j=a+1}^{b-1} (\frac{2}{3}j + c) = \frac{2}{3}(a+b) + 2c - \frac{2}{3}\cdot\frac{(a+1+b-1)(b-a-1)}{2} - c(b-a-1)$
$= \frac{2}{3}(a+b) + 2c - \frac{2}{3}\cdot\frac{(a+b)(b-a-1)}{2} - c(b-a-1)$
$= \frac{2}{3}(a+b)\left(1 - \frac{b-a-1}{2}\right) + c(2 - (b-a-1))$
$= \frac{2}{3}(a+b)\cdot\frac{2-(b-a-1)}{2} + c(3-(b-a))$
$= \frac{(a+b)(3-(b-a))}{3} + c(3-(b-a))$

For this to equal $-1$ for all $a, b$: we need $\frac{(a+b)(3-(b-a))}{3} + c(3-(b-a)) = -1$.

This depends on $a+b$, so it can't be constant for all $a, b$. So a linear function doesn't work. The potential function approach with a single linear function doesn't give a constant decrease.

Let me try a quadratic function. $f(i) = \alpha i^2 + \beta i + \gamma$.

$f(a) + f(b) - \sum_{j=a+1}^{b-1} f(j)$

$= \alpha(a^2 + b^2) + \beta(a+b) + 2\gamma - \alpha \sum_{j=a+1}^{b-1} j^2 - \beta \sum_{j=a+1}^{b-1} j - \gamma(b-a-1)$

$\sum_{j=a+1}^{b-1} j = \frac{(a+b)(b-a-1)}{2}$, $\sum_{j=a+1}^{b-1} j^2 = \frac{(b-1)b(2b-1) - a(a+1)(2a+1)}{6}$.

Let me denote $k = b - a - 1$ (the block size) and $m = a + b = 2a + k + 1$.

$a^2 + b^2 = (a+b)^2 - 2ab = m^2 - 2a(a+k+1) = m^2 - 2a^2 - 2a(k+1)$. Hmm, this is getting messy. Let me just try $f(i) = i^2$.

$\Delta W = a^2 + b^2 - \sum_{j=a+1}^{b-1} j^2$.

$\sum_{j=a+1}^{b-1} j^2 = \frac{(b-1)b(2b-1)}{6} - \frac{a(a+1)(2a+1)}{6}$.

Let me compute for $k=1$ ($b = a+2$): $\Delta W = a^2 + (a+2)^2 - (a+1)^2 = a^2 + a^2+4a+4 - a^2-2a-1 = a^2 + 2a + 3$.

This depends on $a$, so $f(i) = i^2$ alone doesn't work.

Let me try $f(i) = i^2 - i = i(i-1)$.

For $k=1$: $\Delta W = a(a-1) + (a+2)(a+1) - (a+1)a = a^2-a + a^2+3a+2 - a^2-a = a^2 + a + 2$. Still depends on $a$.

Hmm. Let me try a different approach entirely. Maybe I should think about this combinatorially.

Let me reconsider the problem. The operation $0\,1^k\,0 \to 1\,0^k\,1$ can be seen as: a block of $k$ consecutive 1's (surrounded by 0's) is replaced by two 1's at the boundaries with $k$ 0's between them.

This is like a "reflection" or "inversion" of the block. The 1's and 0's swap roles within the block (including the boundaries).

Let me think about the "complement" view. If we look at the positions of 0's instead of 1's, the operation takes two 0's with all 1's between them and flips everything. So two 0's become 1's, and the 1's between become 0's.

Hmm, let me think about this as a game on a binary tree.

Actually, let me try to think about this problem recursively. Consider the initial state: a single 1 at position $n$ in a string of $2n-1$.

The first operation must be on the whole thing: $0\,1\,0$ at positions $n-1, n, n+1$. This gives $1\,0\,1$ at positions $n-1, n, n+1$. State: on at $n-1$ and $n+1$.

Now we have two on-bulbs at $n-1$ and $n+1$, with off at $n$ between them, and off everywhere else.

The left on-bulb at $n-1$ can be split: $0\,1\,0$ at $n-2, n-1, n$. This gives on at $n-2$ and $n$. Now on at $n-2, n, n+1$. Positions $n, n+1$ form a block of size 2.

Similarly, the right on-bulb at $n+1$ can be split: $0\,1\,0$ at $n, n+1, n+2$. This gives on at $n$ and $n+2$. Now on at $n-1, n, n+2$. Positions $n-1, n$ form a block of size 2.

So after the first split, we choose left or right. Let's say we split left: on at $n-2, n, n+1$.

Now we have a block of size 2 at $n, n+1$ and a single at $n-2$.

We can split the single at $n-2$: $0\,1\,0$ at $n-3, n-2, n-1$. On at $n-3, n-1$. Now on at $n-3, n-1, n, n+1$. Block of size 3 at $n-1, n, n+1$.

Or we can split the block of size 2 at $n, n+1$: $0\,1\,1\,0$ at $n-1, n, n+1, n+2$. On at $n-1, n+2$. Now on at $n-2, n-1, n+2$. Block of size 2 at $n-2, n-1$.

Hmm, I see a pattern emerging. Let me think about this more carefully.

Let me think about the process as follows. At any point, the on-bulbs form a set of contiguous blocks. Each operation takes one block and splits it into two single on-bulbs at the boundaries. But these singles might merge with adjacent blocks.

Actually, I think the key insight is that this process is equivalent to building a binary tree, and the maximum number of steps is related to the number of internal nodes.

Let me think about it this way. Consider the "span" of the on-bulbs: the interval $[L, R]$ where $L$ is the leftmost on-bulb and $R$ is the rightmost. Initially, $L = R = n$, span = 1.

Each operation on a block $[a+1, \ldots, a+k]$ (with off at $a$ and $a+k+1$) turns on $a$ and $a+k+1$. If $a < L$, the span extends left. If $a+k+1 > R$, the span extends right. The interior becomes off, but the span only grows (or stays the same if the block was interior).

Actually, the span can only grow or stay the same. It grows when we operate on the leftmost or rightmost block. It stays the same when we operate on an interior block.

The maximum span is $2n-1$ (all bulbs). The span starts at 1 and can grow to at most $2n-1$.

But each operation that extends the span... hmm, this doesn't directly bound the number of steps.

Let me try yet another approach. Let me think about the problem as a variant of the "chip-firing" or "splitting" game.

Actually, let me try to find the pattern by computing small cases more carefully.

For $n=1$ (1 bulb): 0 steps.
For $n=2$ (3 bulbs): 1 step.
For $n=3$ (5 bulbs): 4 steps (computed above).

Let me try $n=4$ (7 bulbs). Initial: $0001000$ (position 4 is on).

This is complex. Let me think about it recursively.

Let me define $f(n)$ = max steps for $2n-1$ bulbs with middle on.

I'll try to find a recurrence. 

Consider the first move: we must split the middle bulb. $0\,1\,0 \to 1\,0\,1$ at positions 3,4,5. Now on at 3,5.

Now we have two "independent" subproblems: the left side (positions 1,2,3 with on at 3) and the right side (positions 5,6,7 with on at 5), with position 4 off between them.

But they're not fully independent because operations on one side can affect the other through the shared boundary.

Actually, let me think about it this way. After the first split, we have on at positions 3 and 5 (in a 7-bulb system, positions 1-7). The left on-bulb at position 3 has off-bulbs at positions 1,2 (to its left) and position 4 (to its right). The right on-bulb at position 5 has off at position 4 (left) and positions 6,7 (right).

The left on-bulb can grow leftward into positions 1,2, and the right can grow rightward into 6,7. But they share position 4.

When the left grows, it might turn on position 4 (by splitting at position 3: $0_2\,1_3\,0_4 \to 1_2\,0_3\,1_4$, turning on position 4). Similarly, the right growing might turn on position 4 ($0_4\,1_5\,0_6 \to 1_4\,0_5\,1_6$).

If position 4 gets turned on by the left side, then the right side's left neighbor is now on, which might create a larger block.

This is getting really complicated. Let me try to think about it as a tree.

I think the key insight is that the process corresponds to a binary tree where each internal node represents a split operation, and the maximum number of operations is the number of internal nodes in a binary tree with certain constraints.

Let me think about it differently. Consider the "lifetime" of each position. A position starts off (except the middle), and can be turned on and off multiple times.

Actually, let me think about the problem in terms of the following: each operation $0\,1^k\,0 \to 1\,0^k\,1$ can be seen as "expanding" the boundary. The two new 1's are at positions that were previously 0, and they're at the boundary of the current "active region."

Let me try to think about the problem as a recursive splitting process on intervals.

Consider an interval $[l, r]$ of bulbs. Initially, the "active" interval is $[n, n]$ (just the middle bulb). 

When we perform an operation on a block of on-bulbs within $[a, b]$ (where $a$ and $b$ are the off endpoints), we're essentially "claiming" the interval $[a, b]$ and splitting it into two sub-intervals $[a, a]$ and $[b, b]$ (the two new on-bulbs) with a gap $[a+1, b-1]$ of off-bulbs.

But then the two new on-bulbs can grow into the gap and beyond.

Hmm, I think I need to think about this more carefully. Let me try a different approach: think about the total number of on-off transitions or some other combinatorial quantity.

Let me try to think about what the final state looks like. The process ends when there's no $0\,1^k\,0$ pattern with $k \geq 1$. This means every on-bulb is either:
- Adjacent to another on-bulb on both sides (interior of a block of size $\geq 3$), or
- At the boundary of the string, or
- Part of a block of size $\geq 2$ at the boundary.

Actually, the process ends when there's no block of on-bulbs of size $\geq 1$ that has off-bulbs on both sides. So every block of on-bulbs must touch at least one boundary of the string (positions 1 or $2n-1$), or all bulbs are on, or all bulbs are off (but we always have at least one on-bulb... actually, can all bulbs become off? $k \geq 3$ decreases the number of on-bulbs, so potentially. But let's check: $0\,1^3\,0 \to 1\,0^3\,1$ gives 2 on-bulbs from 3, so we still have on-bulbs. Actually, the number of on-bulbs is always at least 1? No, $k=3$ gives $2-3 = -1$ change, so from 3 to 2. From 2, $k=2$ gives 0 change. From 1, $k=1$ gives +1. So the minimum is... well, we could go from 2 to 2 (k=2) repeatedly, or from larger to smaller. But can we reach 0? $k$ on-bulbs → $2$ on-bulbs (for $k \geq 3$). From 2 on-bulbs, if they're in a block of size 2, $k=2$ → 2 on-bulbs. If they're separate, we might be able to do $k=1$ on each. So I think we can't reach 0 on-bulbs. The minimum is probably 1 or 2.)

OK let me try a completely different approach. Let me think about the problem as a combinatorial game on a binary tree.

I'll think of the process as follows. We start with a single "node" (the middle bulb). Each operation on a block of size $k$ creates two new "active" positions at the boundaries. This is like a binary tree where each internal node has exactly 2 children.

The total number of operations equals the number of internal nodes in the tree. The leaves are the final on-bulbs (or the positions that can't be split further).

But the constraint is that the tree must "fit" within the $2n-1$ positions, and the splitting must respect the geometry.

Let me think about the maximum number of internal nodes in such a tree.

Consider a perfect binary tree of depth $d$. It has $2^d$ leaves and $2^d - 1$ internal nodes. The total number of nodes is $2^{d+1} - 1$.

If the tree has depth $d$, the span of the leaves is $2^d$ (each split doubles the span). So we need $2^d \leq 2n-1$, giving $d \leq \log_2(2n-1)$.

For $n = 10$: $2n-1 = 19$, $2^4 = 16 \leq 19 < 32 = 2^5$. So $d \leq 4$, and the max internal nodes would be $2^4 - 1 = 15$? But for $n=3$, $2n-1 = 5$, $2^2 = 4 \leq 5 < 8 = 2^3$, so $d \leq 2$, max internal nodes $= 3$. But we computed $f(3) = 4$, which is more than 3. So this simple tree model is wrong.

Let me reconsider. The tree doesn't have to be balanced. An unbalanced tree can have more internal nodes for the same span.

Actually, let me reconsider the tree model. When we split a block of size $k$ at positions $[a+1, \ldots, a+k]$, we get on-bulbs at $a$ and $a+k+1$. The "left child" is at position $a$ and the "right child" is at position $a+k+1$. The distance between them is $k+1$.

The left child can then be split, creating on-bulbs at $a - l$ and $a + 1$ (for some $l \geq 1$), where $l$ is the size of the block to the left. Wait, this depends on the context.

Hmm, I think the tree model is more nuanced. Let me think about it differently.

Let me consider the process as building a binary tree where each node corresponds to a position that gets turned on at some point. The root is position $n$. When we split a block containing position $p$ (which is on), we create two children at positions $p - d_1$ and $p + d_2$ for some distances $d_1, d_2$.

Actually, this isn't quite right either because a block might contain multiple on-bulbs.

Let me go back to thinking about it as splitting blocks. 

Key observation: at any point, the state is a set of contiguous blocks of on-bulbs. Each operation takes one block (with off on both sides) and replaces it with two on-bulbs at the boundaries. These two on-bulbs might merge with adjacent blocks.

Let me think about the "expansion" process. Define the "frontier" as the set of positions that are on. Initially, the frontier is $\{n\}$.

When we split a block $[l, r]$ (on-bulbs at $l, l+1, \ldots, r$ with off at $l-1$ and $r+1$), we turn on $l-1$ and $r+1$, and turn off $l, \ldots, r$. The new on-bulbs at $l-1$ and $r+1$ might merge with adjacent blocks.

If the block $[l, r]$ was the leftmost block, then $l-1$ is a new leftmost position. If it was the rightmost, $r+1$ is a new rightmost. If it was interior, $l-1$ and $r+1$ might merge with the blocks to the left and right.

Let me think about the "span" $[L, R]$ (leftmost and rightmost on-bulbs). The span can only grow. It starts at $[n, n]$ and can grow to at most $[1, 2n-1]$.

Each operation either:
1. Extends the span (if operating on the leftmost or rightmost block), or
2. Doesn't change the span (if operating on an interior block).

When operating on the leftmost block $[L, \ldots]$: we turn on $L-1$, extending the span left by 1. But we also turn off the block, which might change the leftmost on-bulb. Wait, $L-1$ becomes on, so the new leftmost is $L-1$ (or further left if there was already an on-bulb there, but $L-1$ was off by definition of $L$). So the span extends left by 1.

Similarly, operating on the rightmost block extends the span right by 1.

If we operate on an interior block $[l, r]$ (with $L < l$ and $r < R$), the span doesn't change. We turn on $l-1$ and $r+1$, which are within the span. The block $[l, r]$ turns off.

So the span grows by at most 1 per step (left or right), and the total span growth is at most $2(n-1)$ (from span 1 to span $2n-1$). But we can also have interior operations that don't grow the span.

The total number of span-growing operations is at most $2(n-1)$. The total number of interior operations is bounded by... what?

Hmm, let me think about the number of interior operations. An interior operation takes a block and splits it, creating two on-bulbs that might merge with neighbors. This can create larger blocks, which can then be split again.

Actually, I think the key is to think about the total number of "splits" possible. Each split creates two on-bulbs from a block. The total number of on-bulbs is bounded by $2n-1$ (the total number of bulbs). But on-bulbs can be turned on and off multiple times, so this doesn't directly bound the number of operations.

Let me try to find a potential function. 

Let me consider the following: assign to each on-bulb at position $i$ a "weight" that depends on its context. 

Actually, let me try thinking about this problem in terms of the "Zeckendorf" or "Fibonacci" representation, since the splitting process has a Fibonacci-like flavor.

Hmm, let me try another approach. Let me think about the problem as a variant of the "peg solitaire" or "Conway's soldiers" type game.

Actually, let me try to compute $f(n)$ for small $n$ by careful reasoning, and look for a pattern.

$f(1) = 0$.
$f(2) = 1$.
$f(3) = 4$.

Let me try to compute $f(4)$ (7 bulbs, middle at position 4).

Initial: $0001000$.

Step 1: Must split position 4. $0_3\,1_4\,0_5 \to 1_3\,0_4\,1_5$. State: $0010100$. On at 3, 5.

Now we can split position 3 (left) or position 5 (right). By symmetry, let's split left.

Step 2: $0_2\,1_3\,0_4 \to 1_2\,0_3\,1_4$. State: $0100110$... wait, let me be careful. State before: $0_1\,0_2\,1_3\,0_4\,1_5\,0_6\,0_7$. After splitting positions 2,3,4: $0_1\,1_2\,0_3\,1_4\,1_5\,0_6\,0_7$. On at 2, 4, 5. Block of size 2 at 4,5.

Step 3: Options:
- Split position 2: $0_1\,1_2\,0_3 \to 1_1\,0_2\,1_3$. State: $1\,0\,1\,1\,1\,0\,0$. On at 1,3,4,5. Block of size 3 at 3,4,5.
- Split block [4,5]: $0_3\,1_4\,1_5\,0_6 \to 1_3\,0_4\,0_5\,1_6$. State: $0\,1\,1\,0\,0\,1\,0$. On at 2,3,6. Block of size 2 at 2,3.

Let me follow the first option (split position 2): State: $1\,0\,1\,1\,1\,0\,0$. On at 1,3,4,5. Block of size 3 at 3,4,5.

Step 4: Options:
- Split block [3,5] (size 3): $0_2\,1_3\,1_4\,1_5\,0_6 \to 1_2\,0_3\,0_4\,0_5\,1_6$. State: $1\,1\,0\,0\,0\,1\,0$. On at 1,2,6. Block of size 2 at 1,2.
- Split block [3,4] (size 2): $0_2\,1_3\,1_4\,0_5$... wait, position 5 is on, not off. We need off at both endpoints. Position 5 is on. So we can't split [3,4] because the right endpoint (position 5) is on, not off.

Hmm wait, the block of size 3 is at positions 3,4,5. To split a sub-block, we need off bulbs at the endpoints. The off bulbs adjacent to this block are at positions 2 and 6. So the only way to split this block is to use the entire block: $0_2\,1_3\,1_4\,1_5\,0_6 \to 1_2\,0_3\,0_4\,0_5\,1_6$.

Wait, but what about using position 1? Position 1 is on, position 2 is off. So $1_1\,0_2\,1_3$... that's not a valid pattern (we need $0\,1^k\,0$, but position 1 is on). 

What about the block at position 1? It's a single on-bulb at position 1. Its left neighbor is... position 0, which doesn't exist (we're at the boundary). So position 1 can't be split (no off-bulb to its left). 

So the only option is to split the block of size 3: $0_2\,1_3\,1_4\,1_5\,0_6 \to 1_2\,0_3\,0_4\,0_5\,1_6$. State: $1\,1\,0\,0\,0\,1\,0$. On at 1,2,6. Block of size 2 at 1,2.

Step 5: Options:
- Split block [1,2] (size 2): need off at 0 (doesn't exist) and 3 (off). Can't, because position 0 doesn't exist. Actually, we need two off bulbs that are non-adjacent with all on between. For block [1,2], we need off at position 0 and position 3. Position 0 doesn't exist. So we can't split this block from the left.

Hmm, but what about from the right? We need off at both ends. The block is at positions 1,2. Left end is position 0 (doesn't exist), right end is position 3 (off). We can't split because we need off bulbs on both sides.

- Split position 6: $0_5\,1_6\,0_7 \to 1_5\,0_6\,1_7$. State: $1\,1\,0\,0\,1\,0\,1$. On at 1,2,5,7. Block of size 2 at 1,2.

Step 6: Options:
- Split position 5: $0_4\,1_5\,0_6 \to 1_4\,0_5\,1_6$. State: $1\,1\,0\,1\,0\,1\,1$. On at 1,2,4,6,7. Blocks: [1,2], [6,7].
- Split position 7: $0_6\,1_7\,0_8$... position 8 doesn't exist. Can't.
- Split block [1,2]: still can't (no left off-bulb).

Step 7: Split position 4: $0_3\,1_4\,0_5 \to 1_3\,0_4\,1_5$. State: $1\,1\,1\,0\,1\,1\,1$. On at 1,2,3,5,6,7. Blocks: [1,2,3], [5,6,7].

Step 8: Split block [1,3] (size 3): $0_0\,1_1\,1_2\,1_3\,0_4$... position 0 doesn't exist. Can't.
Split block [5,7] (size 3): $0_4\,1_5\,1_6\,1_7\,0_8$... position 8 doesn't exist. Can't.

Hmm, so we're stuck at step 8 with 8 steps? Wait, let me recount.

Steps: 1, 2, 3, 4, 5, 6, 7. That's 7 steps. And then we're stuck. But wait, at step 7, the state is $1\,1\,1\,0\,1\,1\,1$. Can we do anything?

The blocks are [1,2,3] and [5,6,7], with off at 4. To split [1,2,3], we need off at 0 and 4. Position 0 doesn't exist. To split [5,6,7], we need off at 4 and 8. Position 8 doesn't exist. So we're stuck.

But wait, can we split a sub-block? Within [1,2,3], we need $0\,1^k\,0$. The off bulbs are at 4 (right of the block) and... nothing to the left. So we can't.

What about the gap at position 4? We have $1_3\,0_4\,1_5$. This is $1\,0\,1$, not $0\,1^k\,0$. So no.

So this path gives 7 steps for $n=4$. But maybe there's a better path.

Let me try a different approach. Let me go back to step 3 and try the other option.

Step 3 (alternative): Split block [4,5] (size 2): $0_3\,1_4\,1_5\,0_6 \to 1_3\,0_4\,0_5\,1_6$. State: $0\,1\,1\,0\,0\,1\,0$. On at 2,3,6. Block of size 2 at 2,3.

Step 4: Options:
- Split block [2,3] (size 2): $0_1\,1_2\,1_3\,0_4 \to 1_1\,0_2\,0_3\,1_4$. State: $1\,0\,0\,1\,0\,1\,0$. On at 1,4,6.
- Split position 6: $0_5\,1_6\,0_7 \to 1_5\,0_6\,1_7$. State: $0\,1\,1\,0\,1\,0\,1$. On at 2,3,5,7. Block of size 2 at 2,3.

Let me follow the first: State: $1\,0\,0\,1\,0\,1\,0$. On at 1,4,6.

Step 5: Options:
- Split position 4: $0_3\,1_4\,0_5 \to 1_3\,0_4\,1_5$. State: $1\,0\,1\,0\,1\,1\,0$. On at 1,3,5,6. Block of size 2 at 5,6.
- Split position 6: $0_5\,1_6\,0_7 \to 1_5\,0_6\,1_7$. State: $1\,0\,0\,1\,1\,0\,1$. On at 1,4,5,7. Block of size 2 at 4,5.
- Split position 1: $0_0\,1_1\,0_2$... position 0 doesn't exist. Can't.

Follow first: State: $1\,0\,1\,0\,1\,1\,0$. On at 1,3,5,6.

Step 6: Options:
- Split position 3: $0_2\,1_3\,0_4 \to 1_2\,0_3\,1_4$. State: $1\,1\,0\,1\,1\,1\,0$. On at 1,2,4,5,6. Blocks: [1,2], [4,5,6].
- Split block [5,6] (size 2): $0_4\,1_5\,1_6\,0_7 \to 1_4\,0_5\,0_6\,1_7$. State: $1\,0\,1\,1\,0\,0\,1$. On at 1,3,4,7. Block of size 2 at 3,4.

Follow first: State: $1\,1\,0\,1\,1\,1\,0$. On at 1,2,4,5,6. Blocks: [1,2], [4,5,6].

Step 7: Options:
- Split block [4,6] (size 3): $0_3\,1_4\,1_5\,1_6\,0_7 \to 1_3\,0_4\,0_5\,0_6\,1_7$. State: $1\,1\,1\,0\,0\,0\,1$. On at 1,2,3,7. Block of size 3 at 1,2,3.
- Split block [1,2] (size 2): $0_0\,1_1\,1_2\,0_3$... position 0 doesn't exist. Can't.
- Split block [4,5] (size 2): $0_3\,1_4\,1_5\,0_6$... position 6 is on, not off. Can't.

Follow first: State: $1\,1\,1\,0\,0\,0\,1$. On at 1,2,3,7. Block of size 3 at 1,2,3.

Step 8: Options:
- Split block [1,3] (size 3): $0_0\,1_1\,1_2\,1_3\,0_4$... position 0 doesn't exist. Can't.
- Split position 7: $0_6\,1_7\,0_8$... position 8 doesn't exist. Can't.

Stuck at 8 steps.

Let me try the other branch at step 6: State: $1\,0\,1\,1\,0\,0\,1$. On at 1,3,4,7. Block of size 2 at 3,4.

Step 7: Options:
- Split block [3,4] (size 2): $0_2\,1_3\,1_4\,0_5 \to 1_2\,0_3\,0_4\,1_5$. State: $1\,1\,0\,0\,1\,0\,1$. On at 1,2,5,7. Block of size 2 at 1,2.
- Split position 7: $0_6\,1_7\,0_8$... can't.
- Split position 1: can't (boundary).

Follow first: State: $1\,1\,0\,0\,1\,0\,1$. On at 1,2,5,7. Block of size 2 at 1,2.

Step 8: Options:
- Split position 5: $0_4\,1_5\,0_6 \to 1_4\,0_5\,1_6$. State: $1\,1\,0\,1\,0\,1\,1$. On at 1,2,4,6,7. Blocks: [1,2], [6,7].
- Split position 7: can't.
- Split block [1,2]: can't (boundary).

Follow first: State: $1\,1\,0\,1\,0\,1\,1$. On at 1,2,4,6,7. Blocks: [1,2], [6,7].

Step 9: Options:
- Split position 4: $0_3\,1_4\,0_5 \to 1_3\,0_4\,1_5$. State: $1\,1\,1\,0\,1\,1\,1$. On at 1,2,3,5,6,7. Blocks: [1,2,3], [5,6,7].
- Split block [1,2]: can't.
- Split block [6,7]: can't.

Follow first: State: $1\,1\,1\,0\,1\,1\,1$. On at 1,2,3,5,6,7. Blocks: [1,2,3], [5,6,7].

Step 10: Can't split [1,2,3] (boundary), can't split [5,6,7] (boundary). Stuck.

So this path gives 9 steps! That's better than 7.

Let me see if I can do even better. Let me try to be more systematic.

Actually, let me try the other branch at step 5. State: $1\,0\,0\,1\,0\,1\,0$. On at 1,4,6.

Step 5 (alt): Split position 6: $0_5\,1_6\,0_7 \to 1_5\,0_6\,1_7$. State: $1\,0\,0\,1\,1\,0\,1$. On at 1,4,5,7. Block of size 2 at 4,5.

Step 6: Options:
- Split block [4,5] (size 2): $0_3\,1_4\,1_5\,0_6 \to 1_3\,0_4\,0_5\,1_6$. State: $1\,0\,1\,0\,0\,1\,1$. On at 1,3,6,7. Block of size 2 at 6,7.
- Split position 7: $0_6\,1_7\,0_8$... can't.
- Split position 1: can't.

Follow first: State: $1\,0\,1\,0\,0\,1\,1$. On at 1,3,6,7. Block of size 2 at 6,7.

Step 7: Options:
- Split position 3: $0_2\,1_3\,0_4 \to 1_2\,0_3\,1_4$. State: $1\,1\,0\,1\,0\,1\,1$. On at 1,2,4,6,7. Blocks: [1,2], [6,7].
- Split block [6,7] (size 2): $0_5\,1_6\,1_7\,0_8$... can't.

Follow first: State: $1\,1\,0\,1\,0\,1\,1$. On at 1,2,4,6,7. Blocks: [1,2], [6,7].

This is the same state as in the previous path at step 8. From here:
Step 8: Split position 4: $0_3\,1_4\,0_5 \to 1_3\,0_4\,1_5$. State: $1\,1\,1\,0\,1\,1\,1$.
Step 9: Stuck.

So this path gives 8 steps. Worse than 9.

Let me go back and try more branches. Let me restart from step 2 and try splitting right first.

Step 2 (alt): Split position 5: $0_4\,1_5\,0_6 \to 1_4\,0_5\,1_6$. State: $0\,0\,1\,1\,0\,1\,0$. On at 3,4,6. Block of size 2 at 3,4.

By symmetry (mirror), this should give the same as splitting left first. So max is still 9.

Wait, but I should also try different orders of operations. Let me go back to the path that gave 9 steps and see if I can do better by making different choices.

The 9-step path was:
1. $0001000$ → $0010100$ (split middle)
2. $0010100$ → $0100110$... wait, let me retrace.

Actually, let me retrace the 9-step path:
1. $0001000$ → $0010100$ (split pos 4: $0_3 1_4 0_5 → 1_3 0_4 1_5$). On at 3,5.
2. $0010100$ → $0100110$... hmm, I split left (pos 3): $0_2 1_3 0_4 → 1_2 0_3 1_4$. State: $0100110$... wait, $0_1 0_2 1_3 0_4 1_5 0_6 0_7$ → $0_1 1_2 0_3 1_4 1_5 0_6 0_7$ = $0100110$. On at 2,4,5. Block [4,5].
3. Split block [4,5]: $0_3 1_4 1_5 0_6 → 1_3 0_4 0_5 1_6$. State: $0110010$. On at 2,3,6. Block [2,3].
4. Split block [2,3]: $0_1 1_2 1_3 0_4 → 1_1 0_2 0_3 1_4$. State: $1001010$. On at 1,4,6.
5. Split pos 4: $0_3 1_4 0_5 → 1_3 0_4 1_5$. State: $1010110$. On at 1,3,5,6. Block [5,6].
6. Split block [5,6]: $0_4 1_5 1_6 0_7 → 1_4 0_5 0_6 1_7$. State: $1011001$. On at 1,3,4,7. Block [3,4].
7. Split block [3,4]: $0_2 1_3 1_4 0_5 → 1_2 0_3 0_4 1_5$. State: $1100101$. On at 1,2,5,7. Block [1,2].
8. Split pos 5: $0_4 1_5 0_6 → 1_4 0_5 1_6$. State: $1101011$. On at 1,2,4,6,7. Blocks [1,2], [6,7].
9. Split pos 4: $0_3 1_4 0_5 → 1_3 0_4 1_5$. State: $1110111$. On at 1,2,3,5,6,7. Blocks [1,2,3], [5,6,7].
Stuck.

So 9 steps. Can we do better?

Let me try a different strategy. Instead of always splitting blocks of size 2, let me try to create larger blocks and split them.

Actually, let me think about this more carefully. The key is to maximize the total number of operations. Each operation either:
- Splits a block of size 1 (creates 2 on-bulbs, net +1)
- Splits a block of size 2 (creates 2 on-bulbs, net 0)
- Splits a block of size k ≥ 3 (creates 2 on-bulbs, net 2-k < 0)

To maximize steps, we want to use size-1 splits as much as possible (they increase the number of on-bulbs, giving more material for future splits). Size-2 splits are neutral. Size ≥3 splits are wasteful.

But we're constrained by the geometry. Let me think about what the optimal strategy looks like.

Actually, I wonder if the answer for $n=10$ is $n(n-1) = 90$ or something like that. Let me check: $f(1)=0, f(2)=1, f(3)=4, f(4)=9$. These are $(n-1)^2$! $0, 1, 4, 9$. So $f(n) = (n-1)^2$?

For $n=10$: $f(10) = 81$.

But wait, I need to verify $f(4) = 9$ more carefully. I found a path with 9 steps, but maybe there's a longer one. And I need to verify that 9 is optimal.

Let me think about whether 9 is optimal for $n=4$.

Hmm, let me think about an upper bound. 

Consider the potential function $\Phi = \sum_{i \text{ on}} (i - n)^2$ where positions are $1, \ldots, 2n-1$ and $n$ is the middle.

For the operation on $[a, b]$ with $k = b-a-1$:
$\Delta \Phi = (a-n)^2 + (b-n)^2 - \sum_{j=a+1}^{b-1} (j-n)^2$.

Let me substitute $x = a - n, y = b - n$, so $k = y - x - 1$.

$\Delta \Phi = x^2 + y^2 - \sum_{j=x+1}^{y-1} j^2 = x^2 + y^2 - \left(\sum_{j=1}^{y-1} j^2 - \sum_{j=1}^{x} j^2\right)$.

$= x^2 + y^2 - \frac{(y-1)y(2y-1)}{6} + \frac{x(x+1)(2x+1)}{6}$.

This is messy. Let me try specific values.

For $k=1$ ($y = x+2$): $\Delta \Phi = x^2 + (x+2)^2 - (x+1)^2 = x^2 + x^2+4x+4 - x^2-2x-1 = x^2 + 2x + 3$.

For $x = 0$ (middle): $\Delta \Phi = 3$.
For $x = 1$: $\Delta \Phi = 6$.
For $x = -1$: $\Delta \Phi = 1 - 2 + 3 = 2$.
For $x = 2$: $\Delta \Phi = 4 + 4 + 3 = 11$.
For $x = -2$: $\Delta \Phi = 4 - 4 + 3 = 3$.

So $\Delta \Phi$ varies. Not a constant decrease.

Let me try $\Phi = \sum_{i \text{ on}} |i - n|$.

For $k=1$ ($y = x+2$): $\Delta \Phi = |x| + |x+2| - |x+1|$.

For $x = 0$: $0 + 2 - 1 = 1$.
For $x = 1$: $1 + 3 - 2 = 2$.
For $x = -1$: $1 + 1 - 0 = 2$.
For $x = 2$: $2 + 4 - 3 = 3$.
For $x = -2$: $2 + 0 - 1 = 1$.

Not constant either.

Let me try a different potential. What about the number of "inversions" or some combinatorial quantity?

Actually, let me think about this problem differently. Let me consider the "dual" process: instead of tracking on-bulbs, track off-bulbs.

The operation takes two off-bulbs (non-adjacent, with all on between) and flips everything. In terms of off-bulbs: two off-bulbs become on (so they're removed from the off-set), and the on-bulbs between them become off (added to the off-set).

So the off-set changes: remove $a$ and $b$, add $a+1, \ldots, b-1$. Net change in off-count: $(b-a-1) - 2 = k - 2$.

For $k=1$: off-count decreases by 1.
For $k=2$: off-count stays same.
For $k \geq 3$: off-count increases.

Initially, off-count = $2n-2$ (all except middle). The process ends when there's no valid operation, which means... the off-bulbs don't have any pair with all on between them.

Hmm, this is the same thing just dualized.

Let me try yet another approach. Let me think about the problem as a game on a binary tree and try to find the exact recurrence.

I'll think about it as follows. Consider the interval $[1, 2n-1]$ with the middle bulb on. The process builds a binary tree of splits. Each split of a block of size $k$ at position $p$ (center of the block) creates two children at $p - d$ and $p + d$ where $d = (k+1)/2$... no, the children are at the boundaries of the block.

Hmm, let me think about it more carefully.

Actually, let me think about the problem in terms of the following recursive structure.

Consider a "segment" of length $L$ (i.e., $L$ consecutive positions) with a single on-bulb in the center. What's the maximum number of operations?

For odd $L = 2m+1$: the center is at position $m+1$, and we have $m$ off-bulbs on each side. This is exactly our problem with $n = m+1$.

For even $L = 2m$: there's no single center. But we can consider a segment with a single on-bulb at some position.

Actually, let me think about a more general setup. Consider a segment of length $L$ with a single on-bulb at position $p$ (1-indexed within the segment). The off-bulbs extend $p-1$ to the left and $L-p$ to the right.

Let $g(a, b)$ = max operations where $a$ is the number of off-bulbs to the left of the on-bulb and $b$ is the number to the right.

Our problem: $g(n-1, n-1)$ for $n = 10$, i.e., $g(9, 9)$.

Base case: $g(0, 0) = 0$ (no off-bulbs, can't operate).
$g(1, 0) = 0$ (only one off-bulb, need two non-adjacent off-bulbs).
$g(1, 1) = 1$ (one off-bulb on each side, operate on the whole thing).
$g(0, 1) = 0$.

First operation in $g(a, b)$ with $a, b \geq 1$: we split the on-bulb, using the adjacent off-bulbs on both sides. $0\,1\,0 \to 1\,0\,1$. Now we have two on-bulbs, with $a-1$ off-bulbs to the left of the left on-bulb, 1 off-bulb between the two on-bulbs, and $b-1$ off-bulbs to the right of the right on-bulb.

But wait, the first operation doesn't have to use the adjacent off-bulbs. We could use off-bulbs that are further away, as long as all bulbs between them are on. But initially, only the center is on, so the only on-bulb is the center. The only $0\,1^k\,0$ pattern is $0\,1\,0$ using the immediate neighbors. So the first operation is forced.

After the first operation: two on-bulbs at distance 2, with 1 off-bulb between them. Left on-bulb has $a-1$ off-bulbs to its left, right on-bulb has $b-1$ off-bulbs to its right.

Now, we can operate on the left on-bulb (using its left neighbor and the off-bulb between the two on-bulbs), or on the right on-bulb (using the off-bulb between and its right neighbor), or on both on-bulbs as a block (if we use off-bulbs further away with both on-bulbs and the off-bulb between them... but the off-bulb between them is off, so we can't have "all on between" for a larger block).

Wait, the two on-bulbs are at positions $p-1$ and $p+1$ (where $p$ was the original center). Between them is position $p$, which is off. So the two on-bulbs are NOT contiguous; they're separated by an off-bulb. So we can't treat them as a single block.

We can operate on the left on-bulb: $0\,1\,0$ using positions $p-2, p-1, p$. This turns on $p-2$ and $p$, turning off $p-1$. Now $p$ is on, and $p+1$ is on, forming a block of size 2 at $p, p+1$.

Or operate on the right on-bulb: $0\,1\,0$ using positions $p, p+1, p+2$. This turns on $p$ and $p+2$, turning off $p+1$. Now $p-1$ and $p$ are on, forming a block of size 2 at $p-1, p$.

So after the first operation and one more, we get a block of size 2 and a single on-bulb. The block of size 2 can be split, or the single can be split further.

This is getting complex. Let me try to set up a recurrence.

Let me define $g(a, b)$ as above. After the first operation (forced), we have two singles separated by 1 off-bulb, with $a-1$ off to the left and $b-1$ off to the right.

Now, the two singles can be operated on independently, but they interact through the shared off-bulb between them.

Let me think about this differently. Let me consider the "left" and "right" subproblems.

After the first split, the left single has $a-1$ off-bulbs to its left and 1 off-bulb to its right (the shared one). The right single has 1 off-bulb to its left (shared) and $b-1$ off-bulbs to its right.

If we operate on the left single first: $0\,1\,0$ using the left neighbor and the shared off-bulb. This turns on the shared off-bulb, creating a block of size 2 with the right single. Now the right single is part of a block of size 2, and the left side has $a-2$ off-bulbs with a new single at the left.

Hmm, this is really a complex interaction. Let me try to think about it as a tree.

Actually, let me try a different approach. Let me think about the problem as follows.

Each operation $0\,1^k\,0 \to 1\,0^k\,1$ can be associated with an interval $[a, b]$ (the positions affected). The operation "claims" this interval. After the operation, the two endpoints are on and the interior is off.

The key constraint is that the interval must have off endpoints and on interior at the time of the operation.

I think the process can be modeled as a binary tree where:
- Each node corresponds to an interval $[a, b]$ that is "claimed" by an operation.
- The root is the first operation.
- The children of a node are the operations that "claim" sub-intervals.

But the structure is more complex because operations can span across multiple previous operations' intervals.

Let me try to think about the problem from the perspective of the final state.

In the final state, every block of on-bulbs touches a boundary (position 1 or $2n-1$). The maximum number of operations is achieved when we delay reaching this state as long as possible.

Hmm, let me try to think about the problem in terms of a specific strategy and count the operations.

Strategy: Always split the smallest available block (size 1 if possible, then size 2, etc.).

For $n=3$ (5 bulbs):
1. $00100$ → $01010$ (split size 1)
2. $01010$ → $10010$ (split left size 1)
3. $10010$ → $10101$ (split right size 1)
4. $10101$ → $11011$ (split size 1 at position 3)
Total: 4. ✓

For $n=4$ (7 bulbs), the 9-step path I found:
1. $0001000$ → $0010100$ (split size 1)
2. $0010100$ → $0100110$ (split left size 1, creating block of size 2)
3. $0100110$ → $0110010$ (split block of size 2)
4. $0110010$ → $1001010$ (split block of size 2)
5. $1001010$ → $1010110$ (split size 1, creating block of size 2)
6. $1010110$ → $1011001$ (split block of size 2)
7. $1011001$ → $1100101$ (split block of size 2)
8. $1100101$ → $1101011$ (split size 1, creating block of size 2)
9. $1101011$ → $1110111$ (split size 1, creating two blocks of size 3)
Total: 9. ✓ = $(4-1)^2 = 9$.

So the pattern $f(n) = (n-1)^2$ holds for $n = 1, 2, 3, 4$.

Let me verify this makes sense. For $n=5$, $f(5) = 16$.

Let me think about why $f(n) = (n-1)^2$.

Consider the potential function $\Phi = \sum_{i \text{ on}} (i - n)^2$ where the positions are $1, \ldots, 2n-1$.

Initially: $\Phi = 0$ (only the middle bulb is on, at position $n$).

For the operation on $[a, b]$ with $k = b - a - 1$, let $x = a - n, y = b - n$ (so $y = x + k + 1$):
$\Delta \Phi = x^2 + y^2 - \sum_{j=x+1}^{y-1} j^2$.

For $k = 1$ ($y = x + 2$): $\Delta \Phi = x^2 + (x+2)^2 - (x+1)^2 = x^2 + 2x + 3$.

Hmm, this varies with $x$. Not a clean potential.

Let me try $\Phi = \sum_{i \text{ on}} \binom{|i-n|+1}{2} = \sum_{i \text{ on}} \frac{|i-n|(|i-n|+1)}{2}$.

For $k=1$ ($y = x+2$, assuming $x \geq 0$ for simplicity):
$\Delta \Phi = \frac{x(x+1)}{2} + \frac{(x+2)(x+3)}{2} - \frac{(x+1)(x+2)}{2}$
$= \frac{x^2+x + x^2+5x+6 - x^2-3x-2}{2} = \frac{x^2 + 3x + 4}{2}$.

Still varies. Not helpful.

Let me try a completely different potential. What about counting the number of "gaps" (off-bulbs between the leftmost and rightmost on-bulbs)?

Initially: 0 gaps (span is 1, no off-bulbs in between).
Each operation: the span might grow, and the interior might change.

Hmm, this is also complex.

Let me try to think about the problem combinatorially. 

I notice that in the optimal paths I found, the operations seem to follow a specific pattern. Let me look at the $n=4$ case more carefully.

The 9-step path:
1. Split center (pos 4): creates on at 3,5
2. Split left (pos 3): creates on at 2,4; block [4,5]
3. Split block [4,5]: creates on at 3,6; block [2,3]
4. Split block [2,3]: creates on at 1,4; on at 1,4,6
5. Split pos 4: creates on at 3,5; block [5,6]
6. Split block [5,6]: creates on at 4,7; block [3,4]
7. Split block [3,4]: creates on at 2,5; block [1,2]
8. Split pos 5: creates on at 4,6; blocks [1,2], [6,7]
9. Split pos 4: creates on at 3,5; blocks [1,2,3], [5,6,7]

I see a pattern: the operations "sweep" from left to right and then right to left, creating and splitting blocks of size 2.

Actually, let me think about this differently. Let me count the operations by type:
- Size 1 splits: steps 1, 2, 5, 8, 9 (5 operations, each increases on-count by 1)
- Size 2 splits: steps 3, 4, 6, 7 (4 operations, each keeps on-count same)

Total: 5 + 4 = 9.

For $n=3$:
- Size 1 splits: steps 1, 2, 3, 4 (4 operations)
- Size 2 splits: 0

Total: 4.

For $n=2$:
- Size 1 splits: step 1 (1 operation)
Total: 1.

So the number of size 1 splits is $2n-1-1 = 2(n-1)$... no, for $n=2$: 1, $n=3$: 4, $n=4$: 5. That doesn't match $2(n-1)$.

Wait, let me recount. For $n=4$: size 1 splits are steps 1, 2, 5, 8, 9 = 5. Size 2 splits are 3, 4, 6, 7 = 4. Total 9.

For $n=3$: size 1 splits are 1, 2, 3, 4 = 4. Size 2 = 0. Total 4.

For $n=2$: size 1 = 1. Total 1.

Size 1 splits: 1, 4, 5 for $n = 2, 3, 4$.
Size 2 splits: 0, 0, 4 for $n = 2, 3, 4$.

Hmm, $n=3$ has 0 size-2 splits but $n=4$ has 4. Let me check if $n=3$ could have size-2 splits.

For $n=3$, the 4-step path: $00100 → 01010 → 10010 → 10101 → 11011$. All operations are on blocks of size 1. No size-2 blocks are ever created (or if they are, they're not split).

Actually, in step 2: $01010 → 10010$. The on-bulbs are at 1, 4. No block of size 2. Step 3: $10010 → 10101$. On at 1, 3, 5. No block of size 2. Step 4: $10101 → 11011$. On at 1, 2, 4, 5. Blocks [1,2] and [4,5], both size 2. But we can't split them (they're at the boundaries).

So for $n=3$, we end with two blocks of size 2 at the boundaries, and we can't split them. Total 4 = $(3-1)^2$.

For $n=4$, we end with two blocks of size 3 at the boundaries. Total 9 = $(4-1)^2$.

Interesting. The final state has two blocks of size $n-1$ at the boundaries, with a single off-bulb in the middle.

For general $n$: the final state is $1^{n-1}\,0\,1^{n-1}$ (on-bulbs at positions $1, \ldots, n-1$ and $n+1, \ldots, 2n-1$, off at position $n$).

The number of on-bulbs in the final state is $2(n-1)$. The initial number is 1. Each size-1 split adds 1, each size-2 split adds 0, each size-$k$ split ($k \geq 3$) subtracts $k-2$.

If we only use size-1 and size-2 splits: $1 + s_1 = 2(n-1)$, so $s_1 = 2n-3$. And $s_1 + s_2 = (n-1)^2$, so $s_2 = (n-1)^2 - (2n-3) = n^2 - 2n + 1 - 2n + 3 = n^2 - 4n + 4 = (n-2)^2$.

Check: $n=2$: $s_1 = 1, s_2 = 0$. ✓
$n=3$: $s_1 = 3, s_2 = 1$. But I counted $s_1 = 4, s_2 = 0$ for $n=3$. ✗

Hmm, that doesn't match. Let me recount for $n=3$.

$n=3$: final state $11011$. On-bulbs: 4. Initial: 1. $s_1 = 4 - 1 = 3$? But I counted 4 size-1 splits. 

Wait, size-1 split: $0\,1\,0 \to 1\,0\,1$. This takes 1 on-bulb and produces 2, so net +1. But it also requires 2 off-bulbs (the endpoints). After the split, those 2 off-bulbs become on, and the 1 on-bulb becomes off. So on-count goes from 1 to 2, net +1. ✓

4 size-1 splits: on-count goes from 1 to 1+4 = 5. But the final state has 4 on-bulbs. Contradiction!

Let me recheck. $n=3$, 5 bulbs.

Step 1: $00100 → 01010$. On: 1→2. ✓ (+1)
Step 2: $01010 → 10010$. On at 2,4 → on at 1,4. On: 2→2. That's net 0! So this is a size-2 split?

Wait, $01010$: on at 2, 4. The operation is on positions 1,2,3: $0_1\,1_2\,0_3 → 1_1\,0_2\,1_3$. But position 3 is off and position 4 is on. So $0_1\,1_2\,0_3$ is the pattern $0\,1\,0$ with $k
