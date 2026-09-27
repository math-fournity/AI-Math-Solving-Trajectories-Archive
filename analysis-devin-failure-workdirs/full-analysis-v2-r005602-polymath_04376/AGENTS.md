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
  <problem_id>polymath_04376</problem_id>
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

The numbers $0, 1, \dots, n$ ($n \ge 2$) are written on a blackboard. In each step we erase an integer which is the arithmetic mean of two different numbers which are still left on the blackboard. We make such steps until no further integer can be erased. Let $g(n)$ be the smallest possible number of integers left on the blackboard at the end.
Calculate the sum $\sum_{n=2}^{100} g(n)$.

## Standard Solution

From the original solution, $g(n) = 2$ if $n$ is a power of 2, and $g(n) = 3$ if $n$ is not a power of 2.
For $n$ in the range $[2, 100]$, the powers of 2 are $2^1, 2^2, 2^3, 2^4, 2^5, 2^6$, which are $2, 4, 8, 16, 32, 64$.
There are 6 such values of $n$.
The total number of values for $n$ is $100 - 2 + 1 = 99$.
The number of values for which $g(n) = 3$ is $99 - 6 = 93$.
The sum is $6 \times 2 + 93 \times 3 = 12 + 279 = 291$.

## AI's Thinking (Attempted Solution Process)

Let me work through this problem carefully.

We have numbers $0, 1, \ldots, n$ on a blackboard. In each step, we erase an integer that is the arithmetic mean of two different numbers still on the blackboard. We continue until no further integer can be erased. $g(n)$ is the smallest possible number of integers left.

First, let me understand the operation. We have a set $S$ of integers. We can erase $x \in S$ if there exist $a, b \in S$ with $a \neq b$ and $x = (a+b)/2$, i.e., $a + b = 2x$. So $x$ is the midpoint of $a$ and $b$.

We want to find the minimum number of elements left when no more erasures are possible. A set where no element can be erased is called "irreducible" or "stable" — no element is the average of two distinct other elements.

Wait, actually we want to minimize the number left. So we want to erase as many as possible. But the order of erasures matters — we want to choose the order to maximize erasures.

A terminal set (no more erasures possible) is a set $T$ where no element is the average of two distinct other elements of $T$. Such sets are called "sum-free" in a sense... actually, no. The condition is: for all $x \in T$, there do not exist $a, b \in T$, $a \neq b$, with $a + b = 2x$. Equivalently, $T$ contains no 3-term arithmetic progression (3-AP) where the middle term is the one being averaged... wait, no. A 3-term AP is $a, x, b$ with $a + b = 2x$. So the condition is that $T$ has no 3-term arithmetic progression.

Wait, but $a$ and $b$ must be distinct, and $x$ must be different from... actually $x$ could equal $a$ or $b$? No. $x = (a+b)/2$ and $a \neq b$. If $x = a$, then $a = (a+b)/2$ so $2a = a+b$ so $a = b$, contradiction. So $x \neq a$ and $x \neq b$. So indeed, $a, x, b$ form a 3-term AP with $a \neq b$ (and all three distinct).

So a terminal set is a subset of $\{0, 1, \ldots, n\}$ with no 3-term arithmetic progression.

We want to find the minimum size of a 3-AP-free subset that can be reached by the erasure process. But actually, we need to be more careful: not every 3-AP-free subset is reachable. The erasure process must be able to reach it.

Actually, let me reconsider. We want to minimize the number of integers left. We can choose the order of erasures. The question is: what is the minimum possible size of a terminal set reachable from $\{0, 1, \ldots, n\}$?

A terminal set must be 3-AP-free. But can we reach every 3-AP-free subset? Not necessarily. However, we want the minimum, so we want to reach the smallest possible 3-AP-free subset that is reachable.

Actually, let me think about this differently. The question is about the minimum over all valid erasure sequences. 

Let me think about small cases.

$n = 2$: $\{0, 1, 2\}$. Can we erase 1? 1 = (0+2)/2, yes. After erasing 1: $\{0, 2\}$. Can we erase anything? 0 = (a+b)/2 needs $a+b = 0$, impossible with positive. 2 = (a+b)/2 needs $a+b = 4$, only 0+2 = 2 ≠ 4... wait, we need two different numbers. $\{0, 2\}$: to erase 0, need $a + b = 0$ with $a, b \in \{0, 2\}$, $a \neq b$. Only option is 0 and 2, sum = 2 ≠ 0. To erase 2, need $a + b = 4$, only 0+2 = 2 ≠ 4. So $\{0, 2\}$ is terminal. Size 2. Can we do better? We can only erase 1 (the only number that's an average). So $g(2) = 2$.

$n = 3$: $\{0, 1, 2, 3\}$. Numbers that are averages: 1 = (0+2)/2, 2 = (1+3)/2, 1 = (0+2)/2, 2 = (0+4)/... no 4 isn't there. Let me list: 
- 0: need $a+b=0$, impossible.
- 1: (0+2)/2 = 1. Yes.
- 2: (1+3)/2 = 2. Yes. Also (0+4)/... no. 
- 3: need $a+b=6$, impossible.

So we can erase 1 or 2. 

If we erase 1 first: $\{0, 2, 3\}$. Now: 2 = (0+... no. (0+4)/2 no. Actually 2 = (1+3)/2 but 1 is gone. Is 2 the average of any two? 0+3=3, /2 = 1.5 no. 0+2 = 2, /2 = 1 no. 2+3 = 5, /2 = 2.5 no. So 2 can't be erased. 0: no. 3: no. So terminal, size 3.

If we erase 2 first: $\{0, 1, 3\}$. 1 = (0+2)/2 but 2 gone. 1 = (-1+3)/2 no. Is 1 average of any two in {0,1,3}? 0+1=1, /2=0.5 no. 0+3=3, /2=1.5 no. 1+3=4, /2=2 no. So 1 can't be erased. Terminal, size 3.

So $g(3) = 3$? Hmm, that seems large. Wait, can we erase more? From $\{0, 1, 2, 3\}$, after erasing 1, we get $\{0, 2, 3\}$ which is terminal. After erasing 2, we get $\{0, 1, 3\}$ which is terminal. Both size 3. So $g(3) = 3$.

Hmm wait, but $\{0, 1, 3\}$ — is this 3-AP-free? 0, 1, 3: APs would be (0,1,2) no 2; (0, 3/2, 3) no; (1, 2, 3) no 2. Actually 3-APs in {0,1,3}: we need $a, b, c$ with $b - a = c - b$, i.e., $a + c = 2b$. Check: 0+1=1, 2*0=0 no, 2*1=2 no, 2*3=6 no. 0+3=3, 2*1=2 no. 1+3=4, 2*0=0 no, 2*1=2 no, 2*3=6 no. So yes, 3-AP-free. Size 3.

But the maximum 3-AP-free subset of {0,1,2,3} has size... {0,1,3} or {0,2,3} both size 3. Actually can we have size 2? {0,3} is 3-AP-free, size 2. But can we reach it? From {0,1,2,3}, we'd need to erase both 1 and 2. But after erasing one of them, the other becomes unerasesable. So we can't reach {0,3}.

So $g(3) = 3$.

$n = 4$: $\{0,1,2,3,4\}$. Let me think about what's reachable.

Averages: 1=(0+2)/2, 2=(0+4)/2=(1+3)/2, 3=(2+4)/2.

Strategy: erase 2 first. $\{0,1,3,4\}$. Now: 1=(0+2)/2 no 2. 1=(−1+3)/2 no. Is 1 average? 0+1=1,/2=0.5; 0+3=3,/2=1.5; 0+4=4,/2=2; 1+3=4,/2=2; 1+4=5,/2=2.5; 3+4=7,/2=3.5. So 1 not erasable. 3=(2+4)/2 no 2. 3=(1+5)/2 no. 0+3=3,/2=1.5; 0+4=4,/2=2; 1+4=5,/2=2.5; 1+3=4,/2=2; 0+1=1,/2=0.5. So 3 not erasable. So $\{0,1,3,4\}$ is terminal? Check 4: 0+4=4,/2=2; 1+4=5,/2=2.5; 3+4=7,/2=3.5; 0+3=3,/2=1.5; 0+1=1,/2=0.5; 1+3=4,/2=2. So 4 not erasable. 0: not erasable. So terminal, size 4.

Hmm, that's bad. Let me try erasing 1 first. $\{0,2,3,4\}$. Now: 2=(0+4)/2 yes! 3=(2+4)/2 yes. Erase 3: $\{0,2,4\}$. 2=(0+4)/2 yes! Erase 2: $\{0,4\}$. Terminal, size 2!

So $g(4) \leq 2$. Can we get 1? A single element is always 3-AP-free, but can we reach it? From $\{0,4\}$, neither can be erased. So $g(4) = 2$.

Wait, let me re-examine. From $\{0,2,3,4\}$, I said erase 3. Let me verify: 3 = (2+4)/2 = 3. Yes. After erasing 3: $\{0,2,4\}$. 2 = (0+4)/2 = 2. Yes. Erase 2: $\{0,4\}$. Terminal. Size 2.

Alternatively from $\{0,2,3,4\}$, erase 2: $\{0,3,4\}$. 3=(2+4)/2 no 2. 3=(0+6)/2 no. 0+3=3,/2=1.5; 0+4=4,/2=2; 3+4=7,/2=3.5. So 3 not erasable. Terminal, size 3.

So the order matters. Best is: erase 1, then 3, then 2. Result: $\{0,4\}$, size 2.

So $g(4) = 2$.

$n = 5$: $\{0,1,2,3,4,5\}$. Let me try to get to size 2.

Try: erase 1 (=(0+2)/2). $\{0,2,3,4,5\}$. Erase 3 (=(2+4)/2 or (1+5)/2, 1 gone, so (2+4)/2). $\{0,2,4,5\}$. Erase 2 (=(0+4)/2). $\{0,4,5\}$. Now: 4=(3+5)/2 no 3. 4=(0+8)/2 no. 0+4=4,/2=2; 0+5=5,/2=2.5; 4+5=9,/2=4.5. So 4 not erasable. 5: 0+5=5,/2=2.5; 4+5=9,/2=4.5; 0+4=4,/2=2. So 5 not erasable. 0 not erasable. Terminal, size 3.

Hmm. Let me try different order. From $\{0,2,3,4,5\}$: erase 2 (=(0+4)/2). $\{0,3,4,5\}$. 4=(3+5)/2 yes! Erase 4. $\{0,3,5\}$. 3=(1+5)/2 no 1. 3=(0+6)/2 no. 0+3=3,/2=1.5; 0+5=5,/2=2.5; 3+5=8,/2=4. So 3 not erasable. Terminal, size 3.

Try from $\{0,1,2,3,4,5\}$: erase 2 (=(0+4)/2 or (1+3)/2). $\{0,1,3,4,5\}$. Erase 1 (=(0+2)/2 no 2. (−1+3)/2 no. Hmm, is 1 erasable? 0+1=1,/2=0.5; 0+3=3,/2=1.5; 0+4=4,/2=2; 0+5=5,/2=2.5; 1+3=4,/2=2; 1+4=5,/2=2.5; 1+5=6,/2=3; 3+4=7,/2=3.5; 3+5=8,/2=4; 4+5=9,/2=4.5. So 1 not erasable. 

Erase 4 (=(3+5)/2). $\{0,1,3,5\}$. 1=(0+2)/2 no. 3=(1+5)/2 yes! Erase 3. $\{0,1,5\}$. 1 not erasable (0+2 no). 5 not erasable. Terminal, size 3.

Try: erase 3 (=(1+5)/2 or (2+4)/2). $\{0,1,2,4,5\}$. Erase 1 (=(0+2)/2). $\{0,2,4,5\}$. Erase 2 (=(0+4)/2). $\{0,4,5\}$. Terminal, size 3.

Erase 4 (=(3+5)/2 no 3. (2+6)/2 no. Hmm from {0,1,2,4,5}: 4=(3+5)/2 no 3. 4=(2+6)/2 no. 4=(1+7)/2 no. 4=(0+8)/2 no. 0+4=4,/2=2; 1+4=5,/2=2.5; 2+4=6,/2=3; 5+4=9,/2=4.5; 0+5=5,/2=2.5; 1+5=6,/2=3; 2+5=7,/2=3.5; 0+2=2,/2=1; 0+1=1,/2=0.5; 1+2=3,/2=1.5. So 4 not erasable.

Erase 2 (=(0+4)/2). $\{0,1,4,5\}$. 1 not erasable. 4=(3+5)/2 no 3. 0+4=4,/2=2; 1+4=5,/2=2.5; 4+5=9,/2=4.5; 0+5=5,/2=2.5; 1+5=6,/2=3; 0+1=1,/2=0.5. So 4 not erasable. 5 not erasable. Terminal, size 4.

Hmm. Let me try another approach for $n=5$.

From $\{0,1,2,3,4,5\}$: erase 2 (=(1+3)/2). $\{0,1,3,4,5\}$. erase 4 (=(3+5)/2). $\{0,1,3,5\}$. erase 3 (=(1+5)/2). $\{0,1,5\}$. Terminal, size 3.

From $\{0,1,2,3,4,5\}$: erase 3 (=(2+4)/2). $\{0,1,2,4,5\}$. erase 2 (=(0+4)/2). $\{0,1,4,5\}$. erase 1? 1=(0+2)/2 no 2. Not erasable. erase 4? 4=(3+5)/2 no 3. Not erasable. Terminal, size 4.

From $\{0,1,2,3,4,5\}$: erase 3 (=(1+5)/2). $\{0,1,2,4,5\}$. Same as above.

Hmm, it seems like $g(5) = 3$. Let me try to be more systematic.

Actually, let me think about this more carefully. The key insight might be related to 2-adic valuations or something.

Let me think about what sets are reachable. Actually, let me think about the problem from the perspective of what's the minimum 3-AP-free set reachable.

Let me think about it differently. Consider the numbers in terms of their 2-adic valuation. 

Actually, I recall a similar problem. The idea is that the minimum terminal set size is related to the number of odd numbers, or something about the structure.

Let me think about parity. If all remaining numbers have the same parity, then no number can be the average of two others (since the average of two numbers of the same parity has the same parity, but actually the average of two even numbers is even, and the average of two odd numbers is even — wait no. Average of two odd numbers: (odd+odd)/2 = even/2 which could be odd or even. Hmm.

Wait, let me reconsider. If we have only even numbers, say $\{0, 2, 4\}$, then 2 = (0+4)/2, so 2 can be erased. So having all even doesn't make it terminal.

Let me think about the structure differently. 

Key observation: if $S$ is a terminal set (3-AP-free subset of $\{0, \ldots, n\}$), then it contains no 3-term AP. The question is about the minimum size of a reachable terminal set.

Actually, I think the answer might be related to the following: the minimum is achieved by keeping numbers that form a "Sidon-like" set or specifically numbers with certain 2-adic properties.

Let me compute more values.

$n = 2$: $g(2) = 2$ (computed above)
$n = 3$: $g(3) = 3$ (computed above)
$n = 4$: $g(4) = 2$ (computed above)
$n = 5$: $g(5) = 3$ (seems to be)

Let me verify $g(5) = 3$ more carefully. Can we reach a set of size 2?

A 3-AP-free set of size 2 from $\{0,...,5\}$: any 2-element set is 3-AP-free. So we need to check if any 2-element subset is reachable.

To reach $\{a, b\}$, we need to erase all other elements in some order. Let's think about which pairs could work.

Actually, let me think about it more carefully. The elements $0$ and $n$ can never be erased (they're the extremes, can't be averages). Wait, is that true? 0 can be the average of two numbers only if both are 0 (impossible since they must be different) or one is negative. So 0 can never be erased. Similarly, $n$ can never be erased (would need a number > $n$). So 0 and $n$ are always in the terminal set!

Wait, that's a key insight. 0 and $n$ can never be erased. So the terminal set always contains 0 and $n$. So $g(n) \geq 2$ for all $n$.

For $n = 2$: $\{0, 2\}$, and 1 can be erased. $g(2) = 2$. ✓
For $n = 3$: $\{0, 3\}$ plus we need to check if 1 and 2 can both be erased. From $\{0,1,2,3\}$, erase 1: $\{0,2,3\}$. Now 2 = (0+... 2=(1+3)/2 no 1. 2=(0+4)/2 no 4. Not erasable. Erase 2 first: $\{0,1,3\}$. 1=(0+2)/2 no 2. Not erasable. So we can only erase one of {1,2}. $g(3) = 3$. ✓
For $n = 4$: We showed $g(4) = 2$ (reach $\{0,4\}$). ✓
For $n = 5$: 0 and 5 must remain. Can we reach $\{0,5\}$? We need to erase 1,2,3,4. 

From $\{0,1,2,3,4,5\}$:
- 4 = (3+5)/2. Erase 4. $\{0,1,2,3,5\}$.
- 2 = (1+3)/2 or (0+4)/2 no 4. So 2 = (1+3)/2. Erase 2. $\{0,1,3,5\}$.
- 3 = (1+5)/2. Erase 3. $\{0,1,5\}$.
- 1 = (0+2)/2 no 2. 1 = (-1+3)/2 no 3. 1 = (0+... 0+1=1,/2=0.5; 0+5=5,/2=2.5; 1+5=6,/2=3. So 1 not erasable. Stuck at size 3.

Try different order:
- 1 = (0+2)/2. Erase 1. $\{0,2,3,4,5\}$.
- 3 = (2+4)/2. Erase 3. $\{0,2,4,5\}$.
- 2 = (0+4)/2. Erase 2. $\{0,4,5\}$.
- 4 = (3+5)/2 no 3. 4 = (0+8)/2 no. Not erasable. Stuck at size 3.

- 2 = (0+4)/2 or (1+3)/2. Erase 2. $\{0,1,3,4,5\}$.
- 4 = (3+5)/2. Erase 4. $\{0,1,3,5\}$.
- 3 = (1+5)/2. Erase 3. $\{0,1,5\}$.
- 1 not erasable. Stuck at size 3.

- 3 = (1+5)/2 or (2+4)/2. Erase 3. $\{0,1,2,4,5\}$.
- 2 = (0+4)/2. Erase 2. $\{0,1,4,5\}$.
- 4 = (3+5)/2 no 3. Not erasable. 1 not erasable. Stuck at size 4.

- 3 = (2+4)/2. Erase 3. $\{0,1,2,4,5\}$. Same as above.

So it seems $g(5) = 3$. We always get stuck with at least 3 elements.

Let me think about why. After erasing, we're left with 0, 5, and at least one more. The issue is that to erase the last middle element, we need two elements that average to it, but those two might have been erased already.

Let me think about this more structurally. 

Key insight: 0 and $n$ are always in the terminal set. Now, consider the 2-adic valuation. 

Actually, let me think about it in terms of the following. Define $v_2(k)$ as the 2-adic valuation of $k$ (the largest power of 2 dividing $k$), with $v_2(0) = \infty$.

Claim: In a terminal set, for each $d = v_2(n)$, ... hmm, this is getting complicated. Let me think differently.

Let me consider the problem modulo powers of 2.

Actually, I think the key structural insight is:

**Lemma**: If $a$ and $b$ are in the set with $a \neq b$ and $a \equiv b \pmod{2}$, then $(a+b)/2$ is an integer and could potentially be erased (if it's in the set). So in a terminal set, for any two elements of the same parity, their average is not in the set.

But more importantly, think about it this way: the terminal set must be 3-AP-free. The minimum size of a 3-AP-free subset of $\{0, \ldots, n\}$ that contains 0 and $n$ and is reachable.

Hmm, but reachability is the tricky part.

Let me think about this problem from a different angle. 

**Observation**: The erasure process is "monotone" in the sense that we only remove elements. The question is about the minimum size of a maximal (can't extend) erasure sequence's result.

Let me think about what makes an element "erasable" vs "not erasable". An element $x$ is erasable if there exist $a, b$ in the current set with $a + b = 2x$ and $a \neq b$.

**Key insight**: Consider the elements grouped by their residue modulo $2^k$ for increasing $k$.

Actually, let me think about the problem in terms of the following greedy strategy:

Consider the binary representations. The numbers $0$ and $n$ are fixed. Now, think about which numbers can be "forced" to remain.

Let me try a different approach. Let me compute $g(n)$ for small $n$ by brute force (in my head) and look for a pattern.

$g(2) = 2$
$g(3) = 3$
$g(4) = 2$
$g(5) = 3$

$n = 6$: $\{0,1,2,3,4,5,6\}$. 0 and 6 must remain. Can we reach $\{0, 6\}$?

- Erase 3 = (0+6)/2. $\{0,1,2,4,5,6\}$.
- Erase 2 = (0+4)/2. $\{0,1,4,5,6\}$.
- Erase 4 = (2+6)/2 no 2. 4 = (3+5)/2 no 3. 4 = (0+8)/2 no. Hmm. 0+4=4,/2=2; 0+6=6,/2=3; 0+1=1,/2=0.5; 0+5=5,/2=2.5; 1+4=5,/2=2.5; 1+5=6,/2=3; 1+6=7,/2=3.5; 4+5=9,/2=4.5; 4+6=10,/2=5; 5+6=11,/2=5.5. So 4 is not erasable. 5 = (4+6)/2 = 5. Yes! Erase 5. $\{0,1,4,6\}$.
- 4 = (2+6)/2 no 2. 4 = (0+8)/2 no. 0+4=4,/2=2; 0+6=6,/2=3; 0+1=1,/2=0.5; 1+4=5,/2=2.5; 1+6=7,/2=3.5; 4+6=10,/2=5. So 4 not erasable. 1 = (0+2)/2 no 2. 0+1=1,/2=0.5; 0+4=4,/2=2; 0+6=6,/2=3; 1+4=5,/2=2.5; 1+6=7,/2=3.5; 4+6=10,/2=5. So 1 not erasable. Stuck at size 4.

Let me try a different approach for $n=6$:
- Erase 1 = (0+2)/2. $\{0,2,3,4,5,6\}$.
- Erase 3 = (2+4)/2 or (0+6)/2. $\{0,2,4,5,6\}$.
- Erase 5 = (4+6)/2. $\{0,2,4,6\}$.
- Erase 2 = (0+4)/2. $\{0,4,6\}$.
- Erase 4 = (2+6)/2 no 2. 4 = (0+8)/2 no. 0+4=4,/2=2; 0+6=6,/2=3; 4+6=10,/2=5. Not erasable. Stuck at size 3.

- From $\{0,2,4,6\}$: erase 4 = (2+6)/2. $\{0,2,6\}$. 2 = (0+4)/2 no 4. 2 = (-2+6)/2 no. 0+2=2,/2=1; 0+6=6,/2=3; 2+6=8,/2=4. Not erasable. Stuck at size 3.

- From $\{0,2,4,5,6\}$: erase 2 = (0+4)/2. $\{0,4,5,6\}$. 5 = (4+6)/2. Erase 5. $\{0,4,6\}$. 4 = (2+6)/2 no 2. Stuck at size 3.

- From $\{0,2,4,5,6\}$: erase 4 = (2+6)/2. $\{0,2,5,6\}$. 2 = (0+4)/2 no 4. 5 = (4+6)/2 no 4. 0+2=2,/2=1; 0+5=5,/2=2.5; 0+6=6,/2=3; 2+5=7,/2=3.5; 2+6=8,/2=4; 5+6=11,/2=5.5. Not erasable. Stuck at size 4.

Hmm, let me try:
- Erase 2 = (0+4)/2 or (1+3)/2. $\{0,1,3,4,5,6\}$.
- Erase 4 = (3+5)/2. $\{0,1,3,5,6\}$.
- Erase 3 = (1+5)/2. $\{0,1,5,6\}$.
- Erase 5 = (4+6)/2 no 4. 5 = (0+10)/2 no. 0+1=1,/2=0.5; 0+5=5,/2=2.5; 0+6=6,/2=3; 1+5=6,/2=3; 1+6=7,/2=3.5; 5+6=11,/2=5.5. Not erasable. 1 not erasable. Stuck at size 4.

- From $\{0,1,3,5,6\}$: erase 5 = (4+6)/2 no 4. 5 = (0+10)/2 no. 5 = (1+9)/2 no. 5 = (3+7)/2 no. 0+5=5,/2=2.5; 1+5=6,/2=3; 3+5=8,/2=4; 5+6=11,/2=5.5; 0+6=6,/2=3; 1+6=7,/2=3.5; 3+6=9,/2=4.5; 0+3=3,/2=1.5; 0+1=1,/2=0.5; 1+3=4,/2=2. So 5 not erasable. 

Let me try yet another approach:
- Erase 3 = (0+6)/2. $\{0,1,2,4,5,6\}$.
- Erase 1 = (0+2)/2. $\{0,2,4,5,6\}$.
- Erase 5 = (4+6)/2. $\{0,2,4,6\}$.
- Erase 2 = (0+4)/2. $\{0,4,6\}$. Stuck at 3.
- Or erase 4 = (2+6)/2. $\{0,2,6\}$. Stuck at 3.

It seems like $g(6) = 3$. Let me see if there's any way to get to 2.

To get to $\{0, 6\}$, we need to erase 1,2,3,4,5 in some order. The last element to be erased (say $x$) must be the average of two elements still present, which would be 0, 6, and possibly $x$ itself (but $x$ can't be one of the two). So the last erased element $x$ must satisfy $x = (0+6)/2 = 3$, or $x = (a+b)/2$ where $a, b \in \{0, 6\} \cup \{x\}$... wait, at the step before the last erasure, the set is $\{0, 6, x\}$ (plus maybe others, but if we're erasing down to $\{0,6\}$, the second-to-last set is $\{0, 6, x\}$). Then $x = (a+b)/2$ where $a, b \in \{0, 6, x\}$, $a \neq b$. Options: $(0+6)/2 = 3$, $(0+x)/2$, $(6+x)/2$. So $x = 3$ (from $(0+6)/2$), or $x = (0+x)/2 \Rightarrow x = 0$ (impossible, 0 can't be erased), or $x = (6+x)/2 \Rightarrow x = 6$ (impossible). So $x = 3$.

So the last element to erase must be 3, and at that point the set is $\{0, 3, 6\}$. So we need to reach $\{0, 3, 6\}$ from $\{0,1,2,3,4,5,6\}$ by erasing 1, 2, 4, 5 in some order.

From $\{0,1,2,3,4,5,6\}$, erase 1, 2, 4, 5 to get $\{0, 3, 6\}$:
- Erase 1 = (0+2)/2. Need 2 present. $\{0,2,3,4,5,6\}$.
- Erase 2: 2 = (0+4)/2. Need 4 present. $\{0,3,4,5,6\}$.
- Erase 4: 4 = (3+5)/2. Need 3, 5 present. $\{0,3,5,6\}$.
- Erase 5: 5 = (4+6)/2. Need 4 present. But 4 is gone! 5 = (0+10)/2 no. 5 = (3+7)/2 no. Not erasable!

Try different order:
- Erase 4 = (3+5)/2. $\{0,1,2,3,5,6\}$.
- Erase 2 = (1+3)/2 or (0+4)/2 no 4. So 2 = (1+3)/2. $\{0,1,3,5,6\}$.
- Erase 1 = (0+2)/2 no 2. 1 = (-1+3)/2 no. Not erasable! 

- Erase 5 = (4+6)/2. $\{0,1,2,3,4,6\}$.
- Erase 4 = (2+6)/2. $\{0,1,2,3,6\}$.
- Erase 2 = (1+3)/2 or (0+4)/2 no 4. 2 = (1+3)/2. $\{0,1,3,6\}$.
- Erase 1 = (0+2)/2 no 2. Not erasable!

- Erase 1 = (0+2)/2. $\{0,2,3,4,5,6\}$.
- Erase 5 = (4+6)/2. $\{0,2,3,4,6\}$.
- Erase 4 = (2+6)/2. $\{0,2,3,6\}$.
- Erase 2 = (0+4)/2 no 4. 2 = (1+3)/2 no 1. 2 = (-2+6)/2 no. 0+2=2,/2=1; 0+3=3,/2=1.5; 0+6=6,/2=3; 2+3=5,/2=2.5; 2+6=8,/2=4; 3+6=9,/2=4.5. Not erasable!

- Erase 2 = (0+4)/2 or (1+3)/2. $\{0,1,3,4,5,6\}$.
- Erase 4 = (3+5)/2. $\{0,1,3,5,6\}$.
- Erase 1 = (0+2)/2 no 2. Not erasable!

- Erase 2 = (0+4)/2. $\{0,1,3,4,5,6\}$. Same as above.

- Erase 5 = (4+6)/2. $\{0,1,2,3,4,6\}$.
- Erase 1 = (0+2)/2. $\{0,2,3,4,6\}$.
- Erase 4 = (2+6)/2. $\{0,2,3,6\}$.
- Erase 2: not erasable (as shown above).

- Erase 4 = (2+6)/2. $\{0,1,2,3,5,6\}$.
- Erase 5 = (4+6)/2 no 4. 5 = (0+10)/2 no. Not erasable!

- Erase 4 = (3+5)/2. $\{0,1,2,3,5,6\}$.
- Erase 5 = (4+6)/2 no 4. Not erasable!

- Erase 1 = (0+2)/2. $\{0,2,3,4,5,6\}$.
- Erase 4 = (3+5)/2. $\{0,2,3,5,6\}$.
- Erase 5 = (4+6)/2 no 4. 5 = (0+10)/2 no. 5 = (3+7)/2 no. 0+5=5,/2=2.5; 2+5=7,/2=3.5; 3+5=8,/2=4; 5+6=11,/2=5.5; 0+6=6,/2=3; 2+6=8,/2=4; 3+6=9,/2=4.5; 0+3=3,/2=1.5; 0+2=2,/2=1; 2+3=5,/2=2.5. Not erasable!

- Erase 2 = (0+4)/2. $\{0,1,3,4,5,6\}$.
- Erase 5 = (4+6)/2. $\{0,1,3,4,6\}$.
- Erase 4 = (2+6)/2 no 2. 4 = (3+5)/2 no 5. 4 = (0+8)/2 no. 0+4=4,/2=2; 1+4=5,/2=2.5; 3+4=7,/2=3.5; 4+6=10,/2=5; 0+6=6,/2=3; 1+6=7,/2=3.5; 3+6=9,/2=4.5; 0+3=3,/2=1.5; 0+1=1,/2=0.5; 1+3=4,/2=2. Not erasable!

Hmm. It seems impossible to reach $\{0, 3, 6\}$ from $\{0,...,6\}$. So $g(6) = 3$.

Wait, but I haven't tried all orders. Let me be more systematic. To reach $\{0,3,6\}$, I need to erase $\{1,2,4,5\}$ in some order. There are $4! = 24$ orders. But many are equivalent. Let me think about constraints.

For 1 to be erasable: need $a + b = 2$ with $a, b$ in set, $a \neq b$. Options: $\{0, 2\}$. So 1 can only be erased if 0 and 2 are both present. Since 0 is always present, 1 can be erased iff 2 is present.

For 2 to be erasable: need $a + b = 4$. Options from $\{0,...,6\}$: $\{0,4\}$, $\{1,3\}$. So 2 can be erased if either (0 and 4 present) or (1 and 3 present).

For 4 to be erasable: need $a + b = 8$. Options: $\{2,6\}$, $\{3,5\}$. So 4 can be erased if (2 and 6 present) or (3 and 5 present).

For 5 to be erasable: need $a + b = 10$. Options: $\{4,6\}$. So 5 can be erased iff 4 and 6 are both present (6 always present, so iff 4 present).

So:
- 1 erasable iff 2 present.
- 5 erasable iff 4 present.
- 2 erasable iff (4 present) or (1 and 3 present).
- 4 erasable iff (2 present) or (3 and 5 present).

We need to erase all of 1, 2, 4, 5. 

Case 1: Erase 1 first (requires 2 present ✓). Then 2 must be erased later, requiring (4 present) or (1 and 3 present). But 1 is gone, so need 4 present. Then 4 must be erased, requiring (2 present) or (3 and 5 present). If 2 is still present, 4 can be erased. Then 5 must be erased, requiring 4 present. But 4 is gone!

So: erase 1, then need to erase 2 (requires 4), then erase 4 (requires 2 or 3+5), then erase 5 (requires 4). But after erasing 4, can't erase 5. So we need to erase 5 before 4.

Order: 1, 2, 5, 4. 
- Erase 1 (2 present ✓). Set: {0,2,3,4,5,6}.
- Erase 2 (4 present ✓). Set: {0,3,4,5,6}.
- Erase 5 (4 present ✓). Set: {0,3,4,6}.
- Erase 4 (2 present? No. 3 and 5 present? 5 is gone. So 4 not erasable!). Fail.

Order: 1, 5, 2, 4.
- Erase 1 (2 present ✓). {0,2,3,4,5,6}.
- Erase 5 (4 present ✓). {0,2,3,4,6}.
- Erase 2 (4 present ✓). {0,3,4,6}.
- Erase 4 (2 present? No. 3 and 5 present? 5 gone. Not erasable!). Fail.

Order: 5, 1, 2, 4.
- Erase 5 (4 present ✓). {0,1,2,3,4,6}.
- Erase 1 (2 present ✓). {0,2,3,4,6}.
- Erase 2 (4 present ✓). {0,3,4,6}.
- Erase 4 (2 no, 3+5 no). Fail.

Order: 5, 2, 1, 4.
- Erase 5 (4 ✓). {0,1,2,3,4,6}.
- Erase 2 (4 ✓ or 1+3 ✓). {0,1,3,4,6}.
- Erase 1 (2 present? No!). Fail.

Order: 2, 1, 5, 4.
- Erase 2 (4 ✓ or 1+3 ✓). {0,1,3,4,5,6}.
- Erase 1 (2 present? No!). Fail.

Order: 2, 5, 1, 4.
- Erase 2. {0,1,3,4,5,6}.
- Erase 5 (4 ✓). {0,1,3,4,6}.
- Erase 1 (2? No). Fail.

Order: 2, 5, 4, 1.
- Erase 2. {0,1,3,4,5,6}.
- Erase 5 (4 ✓). {0,1,3,4,6}.
- Erase 4 (2? No. 3+5? 5 gone. Not erasable). Fail.

Order: 4, 1, 2, 5.
- Erase 4 (2 ✓ or 3+5 ✓). {0,1,2,3,5,6}.
- Erase 1 (2 ✓). {0,2,3,5,6}.
- Erase 2 (4? No. 1+3? 1 gone. Not erasable). Fail.

Order: 4, 2, 1, 5.
- Erase 4 (2 ✓). {0,1,2,3,5,6}.
- Erase 2 (4? No. 1+3 ✓). {0,1,3,5,6}.
- Erase 1 (2? No). Fail.

Order: 4, 2, 5, 1.
- Erase 4 (2 ✓). {0,1,2,3,5,6}.
- Erase 2 (1+3 ✓). {0,1,3,5,6}.
- Erase 5 (4? No). Fail.

Order: 4, 5, 2, 1.
- Erase 4 (2 ✓ or 3+5 ✓). {0,1,2,3,5,6}.
- Erase 5 (4? No). Fail.

Order: 5, 4, 2, 1.
- Erase 5 (4 ✓). {0,1,2,3,4,6}.
- Erase 4 (2 ✓). {0,1,2,3,6}.
- Erase 2 (4? No. 1+3 ✓). {0,1,3,6}.
- Erase 1 (2? No). Fail.

Order: 5, 4, 1, 2.
- Erase 5 (4 ✓). {0,1,2,3,4,6}.
- Erase 4 (2 ✓). {0,1,2,3,6}.
- Erase 1 (2 ✓). {0,2,3,6}.
- Erase 2 (4? No. 1+3? 1 gone. Not erasable). Fail.

Order: 4, 1, 5, 2.
- Erase 4 (2 ✓). {0,1,2,3,5,6}.
- Erase 1 (2 ✓). {0,2,3,5,6}.
- Erase 5 (4? No). Fail.

Order: 1, 4, 5, 2.
- Erase 1 (2 ✓). {0,2,3,4,5,6}.
- Erase 4 (2 ✓ or 3+5 ✓). {0,2,3,5,6}.
- Erase 5 (4? No). Fail.

Order: 1, 4, 2, 5.
- Erase 1 (2 ✓). {0,2,3,4,5,6}.
- Erase 4 (2 ✓). {0,2,3,5,6}.
- Erase 2 (4? No. 1+3? 1 gone. Not erasable). Fail.

Order: 1, 2, 4, 5.
- Erase 1 (2 ✓). {0,2,3,4,5,6}.
- Erase 2 (4 ✓). {0,3,4,5,6}.
- Erase 4 (2? No. 3+5 ✓). {0,3,5,6}.
- Erase 5 (4? No). Fail.

Order: 2, 4, 1, 5.
- Erase 2 (4 ✓ or 1+3 ✓). {0,1,3,4,5,6}.
- Erase 4 (2? No. 3+5 ✓). {0,1,3,5,6}.
- Erase 1 (2? No). Fail.

Order: 2, 4, 5, 1.
- Erase 2. {0,1,3,4,5,6}.
- Erase 4 (3+5 ✓). {0,1,3,5,6}.
- Erase 5 (4? No). Fail.

Order: 2, 1, 4, 5.
- Erase 2. {0,1,3,4,5,6}.
- Erase 1 (2? No). Fail.

I think I've checked enough. It's impossible to reach $\{0, 3, 6\}$. So $g(6) = 3$.

Wait, but I should also check if we can reach some other 3-element terminal set, or if maybe we're forced to have more than 3. From the attempts above, we reached $\{0, 4, 6\}$ and $\{0, 2, 6\}$ and $\{0, 1, 5\}$ etc., all size 3. And we showed we can reach size 3 (e.g., $\{0, 4, 6\}$). So $g(6) = 3$.

Hmm wait, I need to double-check. We showed that from $\{0,...,6\}$, we can reach $\{0,4,6\}$ (size 3). And we can't reach $\{0,6\}$ (size 2). So $g(6) = 3$.

Let me also check: can we reach $\{0,3,6\}$? We showed above that we can't erase all of 1,2,4,5 to get there. But maybe there's a path I missed? Actually, I enumerated all 24 orderings of erasing {1,2,4,5} and none worked. So indeed $g(6) = 3$.

Now let me tabulate:
$g(2) = 2$
$g(3) = 3$
$g(4) = 2$
$g(5) = 3$
$g(6) = 3$

$n = 7$: $\{0,...,7\}$. 0 and 7 must remain. Can we reach $\{0, 7\}$?

The last element erased must be $x = (0+7)/2 = 3.5$, not an integer. So we can't erase the last middle element using 0 and 7. We need at least one more element. So $g(7) \geq 3$.

Can we reach a 3-element set? We need $\{0, a, 7\}$ where $a$ is such that we can erase everything else, and then $\{0, a, 7\}$ is terminal (3-AP-free, which any 3-element set without a 3-AP is).

For $\{0, a, 7\}$ to be 3-AP-free: no 3-AP among 0, a, 7. The 3-APs would be: (0, a, 2a) needs $2a = 7$, so $a = 3.5$, no. (0, 7, 14) no. (a, 0, -a) no. (a, 7, 14-a) needs... actually the condition is: is any of 0, a, 7 the average of the other two? 
- 0 = (a+7)/2 → a = -7, no.
- a = (0+7)/2 = 3.5, no (not integer).
- 7 = (0+a)/2 → a = 14, no.
So any $\{0, a, 7\}$ with $1 \leq a \leq 6$ is 3-AP-free. Good.

Now, to reach $\{0, a, 7\}$, the last erased element $x$ must be the average of two elements in $\{0, a, 7\} \setminus \{x\}$... wait, the last erased element is from the set $\{0, a, 7, x\}$, and $x = (b+c)/2$ where $b, c \in \{0, a, 7\}$, $b \neq c$. So $x \in \{(0+a)/2, (0+7)/2, (a+7)/2\} = \{a/2, 3.5, (a+7)/2\}$. For $x$ to be an integer, we need $a$ even (for $a/2$) or $a$ odd (for $(a+7)/2$). Since 7 is odd, $(a+7)/2$ is integer iff $a$ is odd. And $a/2$ is integer iff $a$ is even. So for any $a$, one of these is an integer.

But we also need $x$ to be in $\{1, ..., 6\} \setminus \{a\}$, and we need to be able to reach $\{0, a, 7, x\}$ from $\{0,...,7\}$.

This is getting complex. Let me try specific values.

Try $a = 3$: $\{0, 3, 7\}$. Last erased $x$: $(0+3)/2 = 1.5$ no, $(0+7)/2 = 3.5$ no, $(3+7)/2 = 5$. So $x = 5$. We need to reach $\{0, 3, 5, 7\}$ and then erase 5.

From $\{0,...,7\}$, erase $\{1, 2, 4, 6\}$ to get $\{0, 3, 5, 7\}$:
- Erase 1 = (0+2)/2. Need 2. ✓
- Erase 2 = (0+4)/2 or (1+3)/2. 
- Erase 4 = (1+7)/2 or (2+6)/2 or (3+5)/2.
- Erase 6 = (5+7)/2 or (4+8)/2 no 8 or (1+11)/2 no. So 6 = (5+7)/2. Need 5.

Try order: 1, 2, 6, 4.
- Erase 1 (2 ✓). {0,2,3,4,5,6,7}.
- Erase 2 (4 ✓ or 1+3, 1 gone, so 4 ✓). {0,3,4,5,6,7}.
- Erase 6 (5 ✓). {0,3,4,5,7}.
- Erase 4 (2+6 no, 3+5 ✓). {0,3,5,7}. ✓

Now erase 5 = (3+7)/2 = 5. ✓. {0, 3, 7}. Size 3!

So $g(7) \leq 3$. And $g(7) \geq 3$ (since 7 is odd, $(0+7)/2$ is not integer). So $g(7) = 3$.

$n = 8$: $\{0,...,8\}$. 0 and 8 must remain. $(0+8)/2 = 4$, integer. So potentially $g(8) = 2$.

To reach $\{0, 8\}$: last erased is 4 = (0+8)/2. Need to reach $\{0, 4, 8\}$ first.

From $\{0,...,8\}$, erase $\{1,2,3,5,6,7\}$ to get $\{0, 4, 8\}$:
- 1 = (0+2)/2. Need 2.
- 2 = (0+4)/2 or (1+3)/2.
- 3 = (0+6)/2 or (1+5)/2 or (2+4)/2.
- 5 = (4+6)/2 or (2+8)/2 or (3+7)/2 or (1+9)/2 no.
- 6 = (4+8)/2 or (5+7)/2 or (0+12)/2 no.
- 7 = (6+8)/2 or (5+9)/2 no.

Try: erase 1, 2, 3, 5, 6, 7 in some order.

Order: 1, 3, 5, 7, 6, 2.
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8}.
- Erase 3 (0+6 ✓ or 2+4 ✓ or 1+5, 1 gone). {0,2,4,5,6,7,8}.
- Erase 5 (4+6 ✓ or 2+8 ✓). {0,2,4,6,7,8}.
- Erase 7 (6+8 ✓). {0,2,4,6,8}.
- Erase 6 (4+8 ✓). {0,2,4,8}.
- Erase 2 (0+4 ✓). {0,4,8}. ✓

Now erase 4 = (0+8)/2. ✓. {0, 8}. Size 2!

So $g(8) = 2$.

Let me also try $n = 9$: $(0+9)/2 = 4.5$, not integer. So $g(9) \geq 3$.

Can we reach size 3? Try $\{0, a, 9\}$. Last erased $x = (a+9)/2$ (if $a$ odd) or $a/2$ (if $a$ even) or $(0+9)/2 = 4.5$ (no). 

Try $a = 1$: $x = (1+9)/2 = 5$. Need to reach $\{0, 1, 5, 9\}$ then erase 5. But 1 can only be erased if 2 is present, and we need 1 to stay. So we need to erase 2,3,4,6,7,8 while keeping 0,1,5,9.

- 2 = (0+4)/2 or (1+3)/2. Need 4 or (1 and 3).
- 3 = (0+6)/2 or (1+5)/2 or (2+4)/2.
- 4 = (0+8)/2 or (1+7)/2 or (2+6)/2 or (3+5)/2.
- 6 = (0+12)/2 no or (3+9)/2 or (5+7)/2 or (4+8)/2.
- 7 = (5+9)/2 or (6+8)/2 or (4+10)/2 no.
- 8 = (7+9)/2 or (6+10)/2 no or (0+16)/2 no.

Try order: 2, 3, 4, 6, 7, 8.
- Erase 2 (1+3 ✓). {0,1,3,4,5,6,7,8,9}.
- Erase 3 (1+5 ✓ or 0+6 ✓). {0,1,4,5,6,7,8,9}.
- Erase 4 (1+7 ✓ or 0+8 ✓). {0,1,5,6,7,8,9}.
- Erase 6 (3+9 no 3, 5+7 ✓, 4+8 no 4). {0,1,5,7,8,9}.
- Erase 7 (5+9 ✓). {0,1,5,8,9}.
- Erase 8 (7+9 no 7, 0+16 no, 5+11 no, 1+15 no). 8 = (7+9)/2 no 7. 8 = (6+10)/2 no. Hmm. 0+8=8,/2=4; 1+8=9,/2=4.5; 5+8=13,/2=6.5; 8+9=17,/2=8.5; 0+9=9,/2=4.5; 0+5=5,/2=2.5; 0+1=1,/2=0.5; 1+5=6,/2=3; 1+9=10,/2=5; 5+9=14,/2=7. So 8 not erasable! Fail.

Try: 8, 7, 6, 4, 3, 2.
- Erase 8 (7+9 ✓). {0,1,2,3,4,5,6,7,9}.
- Erase 7 (5+9 ✓). {0,1,2,3,4,5,6,9}.
- Erase 6 (3+9 ✓). {0,1,2,3,4,5,9}.
- Erase 4 (0+8 no 8, 1+7 no 7, 2+6 no 6, 3+5 ✓). {0,1,2,3,5,9}.
- Erase 3 (1+5 ✓ or 0+6 no 6). {0,1,2,5,9}.
- Erase 2 (0+4 no 4, 1+3 no 3). 2 not erasable! Fail.

Try: 8, 7, 6, 4, 2, 3.
- Erase 8 (7+9 ✓). {0,1,2,3,4,5,6,7,9}.
- Erase 7 (5+9 ✓). {0,1,2,3,4,5,6,9}.
- Erase 6 (3+9 ✓). {0,1,2,3,4,5,9}.
- Erase 4 (3+5 ✓). {0,1,2,3,5,9}.
- Erase 2 (1+3 ✓). {0,1,3,5,9}.
- Erase 3 (1+5 ✓). {0,1,5,9}. ✓

Now erase 5 = (1+9)/2 = 5. ✓. {0, 1, 9}. Size 3!

So $g(9) = 3$.

Let me now tabulate what I have:
$g(2) = 2$
$g(3) = 3$
$g(4) = 2$
$g(5) = 3$
$g(6) = 3$
$g(7) = 3$
$g(8) = 2$
$g(9) = 3$

I see a pattern: $g(n) = 2$ when $n$ is a power of 2, and $g(n) = 3$ otherwise? Let me check: $n=2$ (power of 2) → 2. $n=4$ (power of 2) → 2. $n=8$ (power of 2) → 2. $n=3,5,6,7,9$ → 3. 

But wait, what about $n = 6$? 6 is not a power of 2, and $g(6) = 3$. What about larger $n$? Let me check $n = 10$.

$n = 10$: $(0+10)/2 = 5$, integer. So potentially $g(10) = 2$.

To reach $\{0, 10\}$: last erased is 5 = (0+10)/2. Need to reach $\{0, 5, 10\}$ first.

From $\{0,...,10\}$, erase $\{1,2,3,4,6,7,8,9\}$ to get $\{0, 5, 10\}$.

This is more complex. Let me think about whether this is possible.

Actually, let me think about the structure more carefully. 

I notice that when $n$ is a power of 2, we can reduce to $\{0, n\}$. The strategy is to work with the binary structure.

Let me think about $n = 10$. $10 = 2 \cdot 5$. 

Hmm, let me think about this differently. Let me consider the 2-adic valuation of $n$.

$v_2(2) = 1$, $g(2) = 2$
$v_2(3) = 0$, $g(3) = 3$
$v_2(4) = 2$, $g(4) = 2$
$v_2(5) = 0$, $g(5) = 3$
$v_2(6) = 1$, $g(6) = 3$
$v_2(7) = 0$, $g(7) = 3$
$v_2(8) = 3$, $g(8) = 2$
$v_2(9) = 0$, $g(9) = 3$

So $g(n) = 2$ when $n$ is a power of 2, and $g(n) = 3$ otherwise (for $n \leq 9$). But I need to check more values.

Actually wait, $v_2(6) = 1$ and $g(6) = 3$, while $v_2(2) = 1$ and $g(2) = 2$. So it's not just about $v_2$.

Let me think about $n = 10$ more carefully.

$n = 10$: Can we reach $\{0, 10\}$? We need to reach $\{0, 5, 10\}$ first (since 5 = (0+10)/2 is the last to erase).

To reach $\{0, 5, 10\}$ from $\{0,...,10\}$, we need to erase 1,2,3,4,6,7,8,9.

Let me think about which elements are "hard" to erase. 

1 can be erased iff 2 is present (since 1 = (0+2)/2 is the only way).
9 can be erased iff 8 or 10 is present (9 = (8+10)/2). 10 always present, so 9 erasable iff 8 present.

Similarly:
2 = (0+4)/2 or (1+3)/2.
3 = (0+6)/2 or (1+5)/2 or (2+4)/2.
4 = (0+8)/2 or (1+7)/2 or (2+6)/2 or (3+5)/2.
6 = (2+10)/2 or (3+9)/2 or (4+8)/2 or (5+7)/2.
7 = (4+10)/2 or (5+9)/2 or (6+8)/2.
8 = (6+10)/2 or (7+9)/2.

We need to keep 0, 5, 10 and erase everything else.

Let me try:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,3,4,5,6,7,8,10}.
- Erase 3 (0+6 ✓ or 2+4 ✓). {0,2,4,5,6,7,8,10}.
- Erase 7 (4+10 ✓ or 6+8 ✓). {0,2,4,5,6,8,10}.
- Erase 2 (0+4 ✓). {0,4,5,6,8,10}.
- Erase 6 (4+8 ✓ or 2+10 no 2). {0,4,5,8,10}.
- Erase 8 (6+10 no 6, 7+9 no). 8 = (6+10)/2 no 6. 8 = (7+9)/2 no. 8 = (5+11)/2 no. 8 = (0+16)/2 no. 8 = (4+12)/2 no. 0+8=8,/2=4; 4+8=12,/2=6; 5+8=13,/2=6.5; 8+10=18,/2=9; 0+10=10,/2=5; 0+5=5,/2=2.5; 0+4=4,/2=2; 4+5=9,/2=4.5; 4+10=14,/2=7; 5+10=15,/2=7.5. So 8 not erasable! Fail.

Try: erase 8 before 6.
- ... {0,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,4,5,6,10}.
- Erase 6 (2+10 no 2, 4+8 no 8, 5+7 no 7, 3+9 no). 6 = (4+8)/2 no 8. 6 = (5+7)/2 no 7. 6 = (2+10)/2 no 2. 6 = (3+9)/2 no. 0+6=6,/2=3; 4+6=10,/2=5; 5+6=11,/2=5.5; 6+10=16,/2=8; 0+10=10,/2=5; 0+5=5,/2=2.5; 0+4=4,/2=2; 4+5=9,/2=4.5; 4+10=14,/2=7; 5+10=15,/2=7.5. So 6 not erasable! Fail.

Hmm. The problem is that 6 and 8 are "entangled" — 6 needs 8 (or other elements) to be erased, and 8 needs 6 (or other elements) to be erased.

Let me try keeping more elements around longer:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 3 (2+4 ✓). {0,2,4,5,6,7,8,9,10}.
- Erase 7 (4+10 ✓ or 6+8 ✓ or 5+9 ✓). {0,2,4,5,6,8,9,10}.
- Erase 9 (8+10 ✓). {0,2,4,5,6,8,10}.
- Erase 2 (0+4 ✓). {0,4,5,6,8,10}.
- Now stuck as before.

Try:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,3,4,5,6,7,8,10}.
- Erase 7 (6+8 ✓ or 4+10 ✓). {0,2,3,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,2,3,4,5,6,10}.
- Erase 6 (2+10 ✓). {0,2,3,4,5,10}.
- Erase 2 (0+4 ✓). {0,3,4,5,10}.
- Erase 4 (3+5 ✓). {0,3,5,10}.
- Erase 3 (1+5 no 1, 0+6 no 6, 2+4 no). 3 = (0+6)/2 no 6. 3 = (1+5)/2 no 1. 3 = (2+4)/2 no. 0+3=3,/2=1.5; 3+5=8,/2=4; 3+10=13,/2=6.5; 0+5=5,/2=2.5; 0+10=10,/2=5; 5+10=15,/2=7.5. So 3 not erasable! Fail.

Try:
- Erase 3 (0+6 ✓). {0,1,2,4,5,6,7,8,9,10}.
- Erase 1 (0+2 ✓). {0,2,4,5,6,7,8,9,10}.
- Erase 9 (8+10 ✓). {0,2,4,5,6,7,8,10}.
- Erase 7 (6+8 ✓ or 4+10 ✓). {0,2,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,2,4,5,6,10}.
- Erase 6 (2+10 ✓). {0,2,4,5,10}.
- Erase 2 (0+4 ✓). {0,4,5,10}.
- Erase 4 (3+5 no 3, 0+8 no 8, 2+6 no, 1+7 no). 4 = (3+5)/2 no 3. 4 = (0+8)/2 no 8. 4 = (2+6)/2 no. 0+4=4,/2=2; 4+5=9,/2=4.5; 4+10=14,/2=7; 0+5=5,/2=2.5; 0+10=10,/2=5; 5+10=15,/2=7.5. So 4 not erasable! Fail.

Try:
- Erase 3 (1+5 ✓). {0,1,2,4,5,6,7,8,9,10}.
- Erase 1 (0+2 ✓). {0,2,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,4,5,6,7,8,10}.
- Erase 7 (4+10 ✓). {0,2,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,2,4,5,6,10}.
- Erase 6 (2+10 ✓). {0,2,4,5,10}.
- Erase 4 (3+5 no 3, 0+8 no 8). Not erasable. Fail.

Hmm, the issue is that after erasing 3, we can't erase 4 later because 4 needs (3,5) or (0,8) or (2,6) or (1,7), and all of those pairs have at least one element erased.

Let me try keeping 3 around longer:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,3,4,5,6,7,8,10}.
- Erase 7 (6+8 ✓). {0,2,3,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,2,3,4,5,6,10}.
- Erase 6 (2+10 ✓). {0,2,3,4,5,10}.
- Erase 4 (3+5 ✓). {0,2,3,5,10}.
- Erase 2 (0+4 no 4, 1+3 no 1). 2 = (0+4)/2 no 4. 2 = (1+3)/2 no 1. 0+2=2,/2=1; 2+3=5,/2=2.5; 2+5=7,/2=3.5; 2+10=12,/2=6; 0+3=3,/2=1.5; 0+5=5,/2=2.5; 0+10=10,/2=5; 3+5=8,/2=4; 3+10=13,/2=6.5; 5+10=15,/2=7.5. So 2 not erasable! Fail.

Try:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,3,4,5,6,7,8,10}.
- Erase 7 (4+10 ✓). {0,2,3,4,5,6,8,10}.
- Erase 6 (4+8 ✓). {0,2,3,4,5,8,10}.
- Erase 8 (6+10 no 6, 7+9 no). 8 = (6+10)/2 no 6. 8 = (7+9)/2 no. Not erasable! Fail.

Try:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,3,4,5,6,7,8,10}.
- Erase 7 (4+10 ✓). {0,2,3,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,2,3,4,5,6,10}.
- Erase 4 (3+5 ✓). {0,2,3,5,6,10}.
- Erase 6 (2+10 ✓). {0,2,3,5,10}.
- Erase 2 (0+4 no 4, 1+3 no 1). Not erasable. Fail.

Try:
- Erase 1 (2 ✓). {0,2,3,4,5,6,7,8,9,10}.
- Erase 9 (8 ✓). {0,2,3,4,5,6,7,8,10}.
- Erase 7 (5+9 no 9, 6+8 ✓, 4+10 ✓). {0,2,3,4,5,6,8,10}.
- Erase 4 (3+5 ✓). {0,2,3,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,2,3,5,6,10}.
- Erase 6 (2+10 ✓). {0,2,3,5,10}.
- Erase 2 (1+3 no 1, 0+4 no 4). Not erasable. Fail.

The problem is always 2 (or 3) at the end. Let me try keeping 1 around:
- Erase 9 (8 ✓). {0,1,2,3,4,5,6,7,8,10}.
- Erase 7 (4+10 ✓ or 6+8 ✓). {0,1,2,3,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,1,2,3,4,5,6,10}.
- Erase 6 (2+10 ✓). {0,1,2,3,4,5,10}.
- Erase 4 (3+5 ✓). {0,1,2,3,5,10}.
- Erase 2 (1+3 ✓). {0,1,3,5,10}.
- Erase 3 (1+5 ✓). {0,1,5,10}.
- Erase 1 (0+2 no 2). 1 = (0+2)/2 no 2. Not erasable! Fail.

- From {0,1,3,5,10}: erase 1 (0+2 no 2). Not erasable. 
- Erase 5 (1+9 no 9, 3+7 no 7, 0+10 ✓). 5 = (0+10)/2 = 5. Yes! {0,1,3,10}.
- Erase 3 (1+5 no 5, 0+6 no 6). Not erasable. Fail.

Hmm. Let me try:
- Erase 9 (8 ✓). {0,1,2,3,4,5,6,7,8,10}.
- Erase 7 (6+8 ✓). {0,1,2,3,4,5,6,8,10}.
- Erase 8 (6+10 ✓). {0,1,2,3,4,5,6,10}.
- Erase 6 (2+10 ✓). {0,1,2,3,4,5,10}.
- Erase 2 (0+4 ✓ or 1+3 ✓). {0,1,3,4,5,10}.
- Erase 4 (3+5 ✓). {0,1,3,5,10}.
- Erase 3 (1+5 ✓). {0,1,5,10}.
- Erase 1 (0+2 no 2). Not erasable. Fail.

- From {0,1,3,4,5,10}: erase 3 (1+5 ✓). {0,1,4,5,10}.
- Erase 4 (3+5 no 3, 0+8 no 8). Not erasable. Fail.

- From {0,1,3,4,5,10}: erase 1 (0+2 no 2). Not erasable.

- From {0,1,2,3,4,5,10}: erase 3 (1+5 ✓). {0,1,2,4,5,10}.
- Erase 1 (0+2 ✓). {0,2,4,5,10}.
- Erase 2 (0+4 ✓). {0,4,5,10}.
- Erase 4 (3+5 no 3). Not erasable. Fail.

- From {0,1,2,4,5,10}: erase 4 (3+5 no 3, 0+8 no 8, 2+6 no 6, 1+7 no 7). Not erasable. Fail.

- From {0,1,2,3,4,5,10}: erase 4 (3+5 ✓). {0,1,2,3,5,10}.
- Erase 2 (1+3 ✓). {0,1,3,5,10}.
- Erase 3 (1+5 ✓). {0,1,5,10}.
- Erase 1 (0+2 no). Fail.

- From {0,1,2,3,5,10}: erase 1 (0+2 ✓). {0,2,3,5,10}.
- Erase 3 (1+5 no 1, 0+6 no 6, 2+4 no 4). Not erasable. Fail.

It seems very hard to reach $\{0, 5, 10\}$ for $n = 10$. Let me think about whether it's possible at all.

Actually, let me think about this more carefully. The issue is that 1 and 9 are "leaf" elements that can only be erased using 2 and 8 respectively. And 2 and 8 are also constrained.

Let me think about the problem in terms of a graph or dependency structure.

Actually, let me think about the 2-adic valuation more carefully.

For $n = 10 = 2 \cdot 5$. The numbers $0, 10$ have $v_2(0) = \infty$, $v_2(10) = 1$. The midpoint is 5, with $v_2(5) = 0$.

For $n = 8 = 2^3$. The numbers $0, 8$ have $v_2(0) = \infty$, $v_2(8) = 3$. The midpoint is 4, with $v_2(4) = 2$. Then midpoint of 0, 4 is 2 ($v_2 = 1$), midpoint of 4, 8 is 6 ($v_2 = 1$). Then midpoints of 0,2 is 1, of 2,4 is 3, of 4,6 is 5, of 6,8 is 7. So we can erase in order of decreasing $v_2$: first erase 4, then 2 and 6, then 1, 3, 5, 7. This works because at each step, the elements being erased are averages of elements with higher $v_2$ that are still present.

For $n = 10$, the issue is that 10 is not a power of 2, so the binary structure doesn't work as cleanly.

Let me think about what the general pattern is.

**Conjecture**: $g(n) = 2$ if $n$ is a power of 2, and $g(n) \geq 3$ otherwise.

But I need to verify this for more cases and also figure out the exact value for non-powers-of-2.

Actually, let me think about $n = 6$ more carefully. $6 = 2 \cdot 3$. We showed $g(6) = 3$. And $n = 10 = 2 \cdot 5$, and it seems $g(10) = 3$ as well (can't reach 2).

Let me think about $n = 12 = 4 \cdot 3$. Can we reach $\{0, 12\}$? Midpoint is 6 = (0+12)/2. Then we need to reach $\{0, 6, 12\}$. Midpoint of 0, 6 is 3, midpoint of 6, 12 is 9. So we need to reach $\{0, 3, 6, 9, 12\}$. Then midpoint of 0, 3 is 1.5 (not integer), midpoint of 3, 6 is 4.5 (not integer), etc. So from $\{0, 3, 6, 9, 12\}$, can we erase anything? 

3 = (0+6)/2 ✓. 9 = (6+12)/2 ✓. 6 = (0+12)/2 ✓. So we can erase 3, 6, or 9. But we need to erase all of them to get to $\{0, 12\}$.

If we erase 6 first: $\{0, 3, 9, 12\}$. 3 = (0+6)/2 no 6. 9 = (6+12)/2 no 6. 3 = (−3+9)/2 no. 0+3=3,/2=1.5; 0+9=9,/2=4.5; 0+12=12,/2=6; 3+9=12,/2=6; 3+12=15,/2=7.5; 9+12=21,/2=10.5. So nothing erasable. Stuck at 4.

If we erase 3 first: $\{0, 6, 9, 12\}$. 9 = (6+12)/2 ✓. Erase 9. $\{0, 6, 12\}$. 6 = (0+12)/2 ✓. Erase 6. $\{0, 12\}$. ✓!

So from $\{0, 3, 6, 9, 12\}$, we can reach $\{0, 12\}$ by erasing 3, then 9, then 6.

But can we reach $\{0, 3, 6, 9, 12\}$ from $\{0, ..., 12\}$?

We need to erase 1, 2, 4, 5, 7, 8, 10, 11.

Let me try:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓ or 1+3 no 1). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 4 (3+5 ✓ or 0+8 ✓). {0,3,5,6,7,8,9,12}.
- Erase 8 (6+10 no 10, 4+12 no 4, 7+9 ✓). {0,3,5,6,7,9,12}.
- Erase 7 (5+9 ✓ or 6+8 no 8). {0,3,5,6,9,12}.
- Erase 5 (3+7 no 7, 4+6 no 4, 1+9 no 1). 5 = (3+7)/2 no 7. 5 = (4+6)/2 no 4. 5 = (1+9)/2 no 1. 5 = (0+10)/2 no 10. 5 = (2+8)/2 no. 0+5=5,/2=2.5; 3+5=8,/2=4; 5+6=11,/2=5.5; 5+9=14,/2=7; 5+12=17,/2=8.5; 0+6=6,/2=3; 0+9=9,/2=4.5; 0+12=12,/2=6; 3+6=9,/2=4.5; 3+9=12,/2=6; 3+12=15,/2=7.5; 6+9=15,/2=7.5; 6+12=18,/2=9; 9+12=21,/2=10.5. So 5 not erasable! Fail.

Try different order:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 5 (3+7 ✓ or 1+9 no 1). {0,3,4,6,7,8,9,12}.
- Erase 7 (5+9 no 5, 6+8 ✓, 4+10 no 10). {0,3,4,6,8,9,12}.
- Erase 8 (6+10 no 10, 7+9 no 7, 4+12 ✓). {0,3,4,6,9,12}.
- Erase 4 (3+5 no 5, 0+8 no 8, 2+6 no 2). 4 = (3+5)/2 no 5. 4 = (0+8)/2 no 8. 4 = (2+6)/2 no 2. 4 = (1+7)/2 no. 0+4=4,/2=2; 3+4=7,/2=3.5; 4+6=10,/2=5; 4+9=13,/2=6.5; 4+12=16,/2=8; 0+6=6,/2=3; 0+9=9,/2=4.5; 0+12=12,/2=6; 3+6=9,/2=4.5; 3+9=12,/2=6; 3+12=15,/2=7.5; 6+9=15,/2=7.5; 6+12=18,/2=9; 9+12=21,/2=10.5. So 4 not erasable! Fail.

Try:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 4 (0+8 ✓). {0,3,5,6,7,8,9,12}.
- Erase 8 (6+10 no 10, 7+9 ✓, 4+12 no 4). {0,3,5,6,7,9,12}.
- Erase 7 (5+9 ✓). {0,3,5,6,9,12}.
- Erase 5: not erasable (as before). Fail.

Try:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 4 (3+5 ✓). {0,3,5,6,7,8,9,12}.
- Erase 5 (3+7 ✓). {0,3,6,7,8,9,12}.
- Erase 7 (6+8 ✓). {0,3,6,8,9,12}.
- Erase 8 (6+10 no 10, 7+9 no 7, 4+12 no 4). 8 = (6+10)/2 no 10. 8 = (7+9)/2 no 7. 8 = (4+12)/2 no 4. 8 = (0+16)/2 no. 0+8=8,/2=4; 3+8=11,/2=5.5; 6+8=14,/2=7; 8+9=17,/2=8.5; 8+12=20,/2=10; 0+12=12,/2=6; 0+9=9,/2=4.5; 0+6=6,/2=3; 0+3=3,/2=1.5; 3+6=9,/2=4.5; 3+9=12,/2=6; 3+12=15,/2=7.5; 6+9=15,/2=7.5; 6+12=18,/2=9; 9+12=21,/2=10.5. So 8 not erasable! Fail.

Try:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 7 (5+9 ✓ or 6+8 ✓). {0,3,4,5,6,8,9,12}.
- Erase 5 (3+7 no 7, 1+9 no 1, 4+6 ✓). {0,3,4,6,8,9,12}.
- Erase 4 (3+5 no 5, 0+8 ✓). {0,3,6,8,9,12}.
- Erase 8 (6+10 no 10, 7+9 no 7, 4+12 no 4). Not erasable. Fail.

Try:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 7 (6+8 ✓). {0,3,4,5,6,8,9,12}.
- Erase 8 (6+10 no 10, 7+9 no 7, 4+12 ✓). {0,3,4,5,6,9,12}.
- Erase 4 (3+5 ✓). {0,3,5,6,9,12}.
- Erase 5 (3+7 no 7, 4+6 no 4, 1+9 no 1). Not erasable. Fail.

Try:
- Erase 1 (0+2 ✓). {0,2,3,4,5,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,6,7,8,9,12}.
- Erase 7 (6+8 ✓). {0,3,4,5,6,8,9,12}.
- Erase 8 (4+12 ✓). {0,3,4,5,6,9,12}.
- Erase 5 (4+6 ✓). {0,3,4,6,9,12}.
- Erase 4 (3+5 no 5, 0+8 no 8, 2+6 no 2). Not erasable. Fail.

Hmm, the problem is always 4 or 5 at the end. Let me try a completely different approach.

- Erase 5 (3+7 ✓ or 4+6 ✓ or 1+9 ✓ or 0+10 ✓). {0,1,2,3,4,6,7,8,9,10,11,12}.
- Erase 1 (0+2 ✓). {0,2,3,4,6,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,6,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,6,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,6,7,8,9,12}.
- Erase 7 (6+8 ✓). {0,3,4,6,8,9,12}.
- Erase 8 (4+12 ✓). {0,3,4,6,9,12}.
- Erase 4 (3+5 no 5, 0+8 no 8, 2+6 no 2). Not erasable. Fail.

- From {0,3,4,6,8,9,12}: erase 4 (0+8 ✓). {0,3,6,8,9,12}.
- Erase 8 (6+10 no 10, 7+9 no 7, 4+12 no 4). Not erasable. Fail.

- From {0,3,4,6,8,9,12}: erase 9 (6+12 ✓). {0,3,4,6,8,12}.
- Erase 8 (6+10 no 10, 4+12 ✓). {0,3,4,6,12}.
- Erase 4 (3+5 no 5, 0+8 no 8, 2+6 no 2). Not erasable. Fail.

- From {0,3,4,6,12}: erase 6 (0+12 ✓). {0,3,4,12}.
- Erase 4 (3+5 no 5, 0+8 no 8). Not erasable. Fail.

- From {0,3,4,6,8,12}: erase 6 (0+12 ✓). {0,3,4,8,12}.
- Erase 4 (0+8 ✓). {0,3,8,12}.
- Erase 8 (4+12 no 4, 6+10 no). 8 = (4+12)/2 no 4. 8 = (6+10)/2 no. 8 = (3+13)/2 no. 8 = (0+16)/2 no. 0+8=8,/2=4; 3+8=11,/2=5.5; 8+12=20,/2=10; 0+12=12,/2=6; 0+3=3,/2=1.5; 3+12=15,/2=7.5. Not erasable. Fail.

Hmm. Let me try yet another approach.

- Erase 6 (0+12 ✓). {0,1,2,3,4,5,7,8,9,10,11,12}.
- Erase 1 (0+2 ✓). {0,2,3,4,5,7,8,9,10,11,12}.
- Erase 11 (10+12 ✓). {0,2,3,4,5,7,8,9,10,12}.
- Erase 2 (0+4 ✓). {0,3,4,5,7,8,9,10,12}.
- Erase 10 (8+12 ✓). {0,3,4,5,7,8,9,12}.
- Erase 5 (3+7 ✓). {0,3,4,7,8,9,12}.
- Erase 7 (5+9 no 5, 6+8 no 6, 4+10 no 10). 7 = (5+9)/2 no 5. 7 = (6+8)/2 no 6. 7 = (4+10)/2 no 10. 7 = (3+11)/2 no 11. 7 = (0+14)/2 no. 0+7=7,/2=3.5; 3+7=10,/2=5; 4+7=11,/2=5.5; 7+8=15,/2=7.5; 7+9=16,/2=8; 7+12=19,/2=9.5; 0+12=12,/2=6; 0+9=9,/2=4.5; 0+8=8,/2=4; 0+4=4,/2=2; 0+3=3,/2=1.5; 3+4=7,/2=3.5; 3+8=11,/2=5.5; 3+9=12,/2=6; 3+12=15,/2=7.5; 4+8=12,/2=6; 4+9=13,/2=6.5; 4+12=16,/2=8; 8+9=17,/2=8.5; 8+12=20,/2=10; 9+12=21,/2=10.5. So 7 not erasable! Fail.

- From {0,3,4,5,7,8,9,12}: erase 7 (6+8 no 6, 5+9 ✓). {0,3,4,5,8,9,12}.
- Erase 5 (3+7 no 7, 4+6 no 6, 1+9 no 1). Not erasable. Fail.

- From {0,3,4,5,7,8,9,12}: erase 9 (6+12 no 6, 7+11 no 11, 8+10 no 10). 9 = (6+12)/2 no 6. 9 = (7+11)/2 no 11. 9 = (8+10)/2 no 10. 9 = (5+13)/2 no. 9 = (0+18)/2 no. 0+9=9,/2=4.5; 3+9=12,/2=6; 4+9=13,/2=6.5; 5+9=14,/2=7; 7+9=16,/2=8; 8+9=17,/2=8.5; 9+12=21,/2=10.5; 0+12=12,/2=6; 0+8=8,/2=4; 0+7=7,/2=3.5; 0+5=5,/2=2.5; 
