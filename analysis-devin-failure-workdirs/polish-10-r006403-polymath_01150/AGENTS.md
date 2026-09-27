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

**Tiebreaker: TOKEN_LIMIT vs PARTIAL_PROGRESS** — If the AI identified the right framework but used a DIFFERENT specific technique than the standard solution, ask: "Would more tokens likely help?" If the AI's technique is a clearly valid alternative that would lead to the solution with more tokens → TOKEN_LIMIT. If the AI's technique is a detour/rabbit-hole that might NOT converge even with more tokens → PARTIAL_PROGRESS. Example: AI uses recursive case-by-case analysis instead of the standard solution's symmetry reduction — even with more tokens, the recursion might never reveal the clean pattern → PARTIAL_PROGRESS, not TOKEN_LIMIT.

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

Output your analysis as a single XML block. Replace each placeholder with your actual analysis.

**IMPORTANT**: Each XML tag must be closed with the EXACT matching closing tag. For example, `<dimension2_explanation>` must be closed with `</dimension2_explanation>`, NOT with `</dimension2_turning_point_type>`.

```xml
<analysis>
  <problem_id>polymath_01150</problem_id>
  <dimension1_verdict>ONE_OF: DIRECTION_ERROR, TOKEN_LIMIT, CONNECTION_ERROR, PARTIAL_PROGRESS</dimension1_verdict>
  <dimension1_explanation>Your 1-3 sentence explanation here</dimension1_explanation>
  <dimension2_turning_point_type>ONE_OF: mod_p_grouping, mod_p_non_obvious, quadratic_residue_euler, lte_lemma, p_adic_valuation, multi_step_mod_p, crt, permutation_polynomial, finite_field_structure, other</dimension2_turning_point_type>
  <dimension2_explanation>Your 1-3 sentence description of the key turning point here</dimension2_explanation>
  <ai_direction_summary>Your 1 sentence summary of the AI's direction here</ai_direction_summary>
  <standard_solution_key_technique>Your 1 sentence summary of the standard technique here</standard_solution_key_technique>
  <confidence>ONE_OF: high, medium, low</confidence>
</analysis>
```

After the XML block, output exactly: `### ANALYSIS COMPLETE`

**Rules:**
- The XML must be inside a ```xml code block
- Do NOT add any text before or after the XML block (except ### ANALYSIS COMPLETE)
- Each opening tag must have a matching closing tag (e.g., `<dimension2_explanation>...</dimension2_explanation>`)
- Output exactly ONE value for each field (not a list separated by |)
- If the AI's thinking is too short to analyze (< 500 chars AND no mathematical content), output CONNECTION_ERROR. But if the AI solved a different problem or went in the wrong direction, use DIRECTION_ERROR even if the thinking is short.
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

There is a set of control weights, each of them weighs a non-integer number of grams. Any
integer weight from $1$ g to $40$ g can be balanced by some of these weights (the control
weights are on one balance pan, and the measured weight on the other pan).What is the
least possible number of the control weights?

[i](Alexandr Shapovalov)[/i]

## Standard Solution

To solve this problem, we need to find the least number of control weights such that any integer weight from 1 g to 40 g can be balanced using these weights. The control weights are placed on one pan of the balance, and the measured weight is placed on the other pan.

1. **Understanding the Problem:**
   - We need to balance any integer weight from 1 g to 40 g.
   - The control weights are non-integer and can be placed on one pan of the balance.
   - The measured weight is placed on the other pan.

2. **Binary Representation Insight:**
   - The initial solution suggests using the binary representation of 40, which is \(101000_2\).
   - This implies that any integer from 1 to 40 can be represented using at most 6 bits.
   - The weights corresponding to these bits are \(1, 2, 4, 8, 16, 32\).

3. **Verification of the Binary Approach:**
   - The binary approach works for representing numbers, but it does not directly apply to balancing weights on a balance scale.
   - We need to consider the possibility of placing weights on both pans of the balance.

4. **Using Ternary (Base-3) Representation:**
   - In a balance problem, we can use weights on both sides of the balance. This suggests using a ternary (base-3) system.
   - In a ternary system, each digit can be -1, 0, or 1, representing placing a weight on the left pan, not using the weight, or placing it on the right pan, respectively.

5. **Finding the Minimum Number of Weights:**
   - We need to find the smallest set of weights such that any integer from 1 to 40 can be balanced.
   - The weights in a ternary system are powers of 3: \(3^0, 3^1, 3^2, \ldots\).

6. **Calculating the Required Weights:**
   - The maximum weight we need to balance is 40 g.
   - We need to find the smallest \(n\) such that the sum of the series \(3^0 + 3^1 + 3^2 + \ldots + 3^n \geq 40\).

   \[
   \text{Sum of the series} = \frac{3^{n+1} - 1}{2}
   \]

   - We need to solve for \(n\):

   \[
   \frac{3^{n+1} - 1}{2} \geq 40
   \]

   \[
   3^{n+1} - 1 \geq 80
   \]

   \[
   3^{n+1} \geq 81
   \]

   \[
   n+1 \geq 4
   \]

   \[
   n \geq 3
   \]

   - Therefore, we need weights \(3^0, 3^1, 3^2, 3^3\), which are \(1, 3, 9, 27\).

7. **Verification:**
   - With weights \(1, 3, 9, 27\), we can balance any weight from 1 to 40 g.
   - For example:
     - To balance 1 g: use \(1\) on the left pan.
     - To balance 2 g: use \(3\) on the left pan and \(1\) on the right pan.
     - To balance 40 g: use \(27 + 9 + 3 + 1\) on the left pan.

Thus, the least possible number of control weights is 4.

The final answer is \(\boxed{4}\).

## AI's Thinking (Attempted Solution Process)


============================================================
[Thinking Round 1]
============================================================
The problem: We have control weights, each weighing a non-integer number of grams. Any integer weight from 1g to 40g can be balanced by some subset of these weights (control weights on one pan, measured weight on the other pan). So we need to represent every integer from 1 to 40 as a sum of a subset of the control weights. The control weights are all non-integer. Find the minimum number of control weights.

Wait, let me re-read. "the control weights are on one balance pan, and the measured weight on the other pan." So we can only put control weights on one side, the measured weight on the other. So each integer from 1 to 40 must be expressible as a sum of a subset of the control weights.

Each control weight is a non-integer. We want the minimum number n such that there exist non-integer values $w_1, ..., w_n$ where every integer in $\{1, 2, ..., 40\}$ is a subset sum.

With n weights, there are $2^n$ subsets (including empty). We need 40 distinct positive integer values from 1 to 40, plus 0 (empty set). So we need at least 41 distinct subset sums, meaning $2^n \geq 41$, so $n \geq 6$.

Can we do it with 6? We have 64 subsets, need to cover 0..40 (41 values).

Let me think about whether 6 non-integer weights can produce all integers 1..40 as subset sums.

Classic problem. Let me think. With integer weights, the balanced ternary gives 1, 3, 9, 27 = 4 weights covering 1..40 (with weights on both pans). But here weights are only on one pan, and non-integer.

One-pan with integer weights: powers of 2: 1,2,4,8,16,32 covers 1..63, that's 6 weights. But those are integers, not allowed.

We need non-integer weights. So we can't use 1,2,4,8,16,32 directly.

Hmm, but we need subset sums to hit every integer 1..40 exactly. The weights are non-integer but their subset sums must include all integers 1..40.

Let me think about 6 weights. We need 41 values (0..40). With 6 weights we have 64 subsets. 

Consider weights that are half-integers or have fractional parts. If all weights are half-integers (k+0.5), then subset sums are half-integers. To get integer sums we need an even number of weights in the subset. That gives $\binom{6}{0}+\binom{6}{2}+\binom{6}{4}+\binom{6}{6} = 1+15+15+1 = 32$ subsets with even cardinality. That's only 32 values, not enough for 41.

What if weights have fractional part 1/3? Like $a_i + 1/3$. Then subset sum = (sum of $a_i$) + k/3 where k is the number of weights. For integer sum, k must be divisible by 3. k=0,3,6. $\binom{6}{0}+\binom{6}{3}+\binom{6}{6} = 1+20+1 = 22$. Not enough.

What about fractional part 1/4? k divisible by 4: k=0,4. $\binom{6}{0}+\binom{6}{4}=1+15=16$. Worse.

Hmm. What if different weights have different fractional parts? 

Let me think more carefully. We want to maximize the number of integer subset sums.

Actually, let's think about it differently. Let $w_i = a_i + f_i$ where $a_i$ is integer and $0 < f_i < 1$ (non-integer means $f_i \neq 0$; also $f_i$ could be > 1 if weight > 1, but let's think of fractional parts). Actually let $w_i$ have fractional part $\{w_i\} \in (0,1)$.

A subset sum is integer iff the sum of fractional parts of selected weights is integer.

Let me consider the case where all weights have the same fractional part $f$. Then subset of size k has fractional part $kf \pmod{1}$. For this to be 0, we need $kf \equiv 0 \pmod 1$.

If $f = 1/2$: k even. 32 subsets.
If $f = p/q$ in lowest terms: k divisible by q.

To get more integer sums, we want q small. q=2 gives 32. That's the best with uniform fractional part.

But 32 < 41, so 6 weights with uniform fractional part won't work.

What about mixed fractional parts? Let's say some weights have fractional part 1/2 and others have 0... no, all must be non-integer.

Let me think about 6 weights with fractional parts $f_1, ..., f_6 \in (0,1)$. The number of subsets whose fractional-part-sum is an integer must be $\geq 41$.

Hmm, this is getting complex. Let me think about whether 6 is achievable at all, or if we need 7.

Actually wait. Let me reconsider. Maybe we can be cleverer. Let me think about specific constructions.

Consider 6 weights. We want to cover 1..40. Let me try to think of a construction.

Actually, let me think about the problem from the perspective of: what's the maximum number of consecutive integers starting from 0 that can be represented as subset sums of n non-integer weights?

Let me think about small cases first.

n=1: one non-integer weight w. Subset sums: 0, w. Only 0 is integer (w non-integer). So we can't even get 1. Max consecutive integers from 0: just {0}.

n=2: weights $w_1, w_2$ non-integer. Subset sums: 0, $w_1$, $w_2$, $w_1+w_2$. For integers: 0 always. $w_1+w_2$ integer if $\{w_1\}+\{w_2\}=1$. Then we get 0 and $w_1+w_2$. If $w_1+w_2 = 1$, we get {0,1}. Can we get more? We'd need $w_1$ or $w_2$ integer, but they're non-integer. So max is {0,1} if $w_1+w_2=1$, covering 1. Actually we need $w_1+w_2$ to be a positive integer; smallest is 1. So n=2 covers up to 1.

Wait, but can we cover {0, 1, 2}? We'd need three integer subset sums. We have 0, and at most $w_1+w_2$ if fractional parts sum to 1. $w_1$ and $w_2$ are non-integer so not integer. So only 0 and $w_1+w_2$. Can't get 3 integers. So n=2 covers {0,1} at best.

n=3: weights $w_1, w_2, w_3$. Subset sums: 8 total. Integer ones: 0, and those where fractional parts sum to integer. 

If all have fractional part 1/2: integer sums when even number selected: k=0,2. $\binom{3}{0}+\binom{3}{2}=1+3=4$ integer sums. The k=2 sums are $w_i+w_j$. If $w_i = a_i + 1/2$, then $w_i+w_j = a_i+a_j+1$. We can choose $a_i$ to make these 1,2,3 and then... but we need consecutive 0,1,2,3. Set $w_1=0.5, w_2=1.5, w_3=2.5$. Then sums: $w_1+w_2=2, w_1+w_3=3, w_2+w_3=4$. Integer sums: 0, 2, 3, 4. Not consecutive from 1 (missing 1).

Hmm. Let me try $w_1=0.5, w_2=0.5, w_3=...$. No wait, can weights be equal? The problem says "a set of control weights" — set might imply distinct, but maybe not. Let me assume they can be equal for now (multiset). Actually "set" might mean distinct. Let me keep them distinct for safety but explore.

$w_1 = 0.5, w_2 = 1.5, w_3 = 2.5$: integer sums 0, 2, 3, 4. Missing 1.

What if fractional parts are 1/3, 1/3, 1/3? Then k=0,3 give integers. $\binom{3}{0}+\binom{3}{3}=2$. Only 0 and $w_1+w_2+w_3$. Not enough.

What about fractional parts 1/2, 1/2, 0? No, 0 not allowed.

Mixed: $f_1=1/2, f_2=1/2, f_3=1/2$ gives the 4 integer sums as above. To get consecutive 0,1,2,3: need $w_i+w_j$ to be 1,2,3. $w_i+w_j = a_i+a_j+1$. So $a_i+a_j \in \{0,1,2\}$. With $a_1 < a_2 < a_3$ (for distinct weights, $a_i$ distinct or same with same frac). Let $a_1=0, a_2=1, a_3=2$: sums $a_i+a_j+1 = 2,3,4$. Not 1,2,3.

$a_1=0, a_2=0, a_3=1$: weights $0.5, 0.5, 1.5$ (not distinct). Sums: $0.5+0.5=1, 0.5+1.5=2, 0.5+1.5=2$. Integer sums: 0,1,2. Covers 0,1,2! But weights not distinct.

If distinct required, n=3 with frac 1/2: $a_1<a_2<a_3$ integers $\geq 0$. $a_i+a_j+1$ for pairs. Smallest: $a_1+a_2+1$. To get 1: $a_1+a_2=0 \Rightarrow a_1=a_2=0$, not distinct. So can't get 1 with distinct weights and all frac 1/2.

Hmm, this is getting complicated. Let me step back and think about the general structure.

Actually, let me reconsider the problem. Maybe the answer is 6 or 7. Let me think about upper bounds (constructions) and lower bounds.

Lower bound: $2^n \geq 41 \Rightarrow n \geq 6$.

But we also need enough integer subset sums. Let me think about the maximum number of integer subset sums with n non-integer weights.

Claim: With n non-integer weights, the number of integer subset sums is at most $2^{n-1}$... is that true? No. Consider all frac 1/2: even subsets, $2^{n-1}$. Consider frac parts $1/2, 1/2, ..., 1/2$ (n of them): $2^{n-1}$ integer sums. Can we do better with mixed?

Consider $f_1 = 1/2, f_2 = 1/2, f_3 = 1/3, f_4 = 1/3, f_5 = 1/3, f_6 = 1/3$. Hmm, complex.

Actually, let me think about it as a group. The fractional parts live in $\mathbb{R}/\mathbb{Z}$. A subset sum is integer iff the sum of fractional parts is 0 in $\mathbb{R}/\mathbb{Z}$. 

The number of subsets summing to 0 mod 1: this depends on the structure. If all $f_i = 1/2$, the subsets summing to 0 mod 1 are exactly even-sized subsets: $2^{n-1}$.

Can we get more than $2^{n-1}$? Consider $f_1 = f_2 = 1/2$ and rest... Actually, let's think: the map from $\{0,1\}^n \to \mathbb{R}/\mathbb{Z}$ sending subset to sum of fractional parts. The number of subsets hitting 0 is what we want to maximize.

If all $f_i$ are equal to $f = p/q$ (lowest terms), subsets hitting 0 are those with size $\equiv 0 \pmod q$. Count $= \sum_{q | k} \binom{n}{k} \approx 2^n / q$. For $q=2$: $2^{n-1}$. For $q=1$ (integer, not allowed). So uniform gives at most $2^{n-1}$ (with $q=2$).

With mixed fractional parts, can we exceed $2^{n-1}$? 

Consider $n=2$: $f_1, f_2$. Subsets: $\emptyset$ (0, always), $\{1\}$ ($f_1$, integer iff $f_1=0$, no), $\{2\}$ (no), $\{1,2\}$ ($f_1+f_2$, integer iff $f_1+f_2 \in \mathbb{Z}$). So at most 2 integer sums = $2^{2-1} = 2$. Equality when $f_1+f_2=1$.

$n=3$: Can we get more than 4? Let's see. We need subsets with frac-sum integer. $\emptyset$: yes (1). Singletons: no (3 subsets, none). Pairs: $f_i+f_j$ integer. Triples: $f_1+f_2+f_3$ integer. 

If $f_1+f_2, f_1+f_3, f_2+f_3$ all integer: then $f_1+f_2 \equiv 0, f_1+f_3 \equiv 0 \Rightarrow f_2 \equiv f_3$. And $f_2+f_3 \equiv 0 \Rightarrow 2f_2 \equiv 0 \Rightarrow f_2 = 1/2$. So all $f_i = 1/2$. Then triple sum $= 3/2$, not integer. So integer sums: $\emptyset$ + 3 pairs = 4 = $2^{3-1}$.

Alternatively, 2 pairs + triple: say $f_1+f_2 \equiv 0, f_1+f_3 \equiv 0, f_1+f_2+f_3 \equiv 0$. From first two: $f_2 \equiv f_3$. Triple: $f_1 + 2f_2 \equiv 0$. And $f_1 + f_2 \equiv 0 \Rightarrow f_1 \equiv -f_2$. So $-f_2 + 2f_2 = f_2 \equiv 0$, contradiction ($f_2$ non-integer). 

So can't get 2 pairs + triple. What about 1 pair + triple? $f_1+f_2 \equiv 0, f_1+f_2+f_3 \equiv 0 \Rightarrow f_3 \equiv 0$, contradiction.

So for n=3, max integer sums is 4 = $2^{n-1}$, achieved by all $f_i = 1/2$.

This suggests the maximum number of integer subset sums with n non-integer weights is $2^{n-1}$.

Let me try to prove this. 

Lemma: If $w_1, ..., w_n$ are non-integers, the number of subsets $S \subseteq [n]$ with $\sum_{i \in S} w_i \in \mathbb{Z}$ is at most $2^{n-1}$.

Proof idea: Consider the map $\phi: \{0,1\}^n \to \mathbb{R}/\mathbb{Z}$, $\phi(S) = \sum_{i \in S} w_i \pmod 1$. The kernel (subsets mapping to 0) forms a subgroup of $(\mathbb{Z}/2)^n$... wait, is it a subgroup? $\phi(S \triangle T) = \phi(S) + \phi(T) - 2\phi(S \cap T)$... no, that's not right. $\phi(S) = \sum_{i \in S} w_i$, and $\phi(S \oplus T)$ where $\oplus$ is symmetric difference... $\sum_{i \in S \triangle T} w_i = \sum_{i \in S} w_i + \sum_{i \in T} w_i - 2\sum_{i \in S \cap T} w_i$. Mod 1, the $-2\sum_{i \in S \cap T} w_i$ term doesn't vanish in general. So the kernel is NOT a subgroup in general. So the bound isn't simply from group theory.

Hmm wait, but if all $w_i$ have fractional part 1/2, then $2w_i \equiv 0 \pmod 1$, and the kernel IS a subgroup (the even-weight code). 

Let me think again. The kernel $K = \{S : \sum_{i \in S} w_i \in \mathbb{Z}\}$. Is $K$ a subgroup of $(\mathbb{Z}/2)^n$ under symmetric difference? $S, T \in K \Rightarrow \sum_S w_i, \sum_T w_i \in \mathbb{Z}$. $\sum_{S \triangle T} w_i = \sum_S w_i + \sum_T w_i - 2\sum_{S \cap T} w_i$. The first two are integers, but $2\sum_{S \cap T} w_i$ is an integer iff $\sum_{S \cap T} w_i$ is a half-integer or integer. Not guaranteed. So $K$ is not necessarily a subgroup.

So the $2^{n-1}$ bound might not hold in general! Let me look for a counterexample with n=4.

n=4: Can we get more than 8 integer subset sums?

Try $f_1 = f_2 = 1/2, f_3 = f_4 = 1/3$. Subsets with integer frac-sum:
- $\emptyset$: 0. Yes.
- Need sum of selected frac parts $\equiv 0$.

Let me enumerate. Frac parts: 1/2, 1/2, 1/3, 1/3. 

Let $a$ = number of 1/2's selected (0,1,2), $b$ = number of 1/3's selected (0,1,2). Frac sum = $a/2 + b/3 = (3a + 2b)/6$. Integer iff $3a + 2b \equiv 0 \pmod 6$.

$(a,b)$: 
- (0,0): 0. Yes.
- (0,1): 2/6. No.
- (0,2): 4/6. No.
- (1,0): 3/6. No.
- (1,1): 5/6. No.
- (1,2): 7/6 ≡ 1/6. No.
- (2,0): 6/6=1. Yes.
- (2,1): 8/6. No.
- (2,2): 10/6. No.

So integer subsets: (0,0) and (2,0). (0,0): 1 subset. (2,0): $\binom{2}{2}\binom{2}{0} = 1$. Total 2. Much less than 8.

That's bad. Let me try all 1/2: 8 integer sums (even subsets). 

Try $f = 1/2$ for all: $2^{n-1} = 8$ for n=4.

Try mixing to beat 8. $f_1 = 1/2, f_2 = 1/2, f_3 = 1/2, f_4 = 1/2$: 8.

What about $f_1 = 1/2, f_2 = 1/2, f_3 = 1/2, f_4 = 1/4$? Frac sum = $a/2 + b/4$ where $a \in \{0,1,2,3\}$ (number of 1/2's), $b \in \{0,1\}$. $= (2a + b)/4$. Integer iff $2a + b \equiv 0 \pmod 4$.
- $b=0$: $2a \equiv 0 \pmod 4 \Rightarrow a$ even: $a=0,2$. $\binom{3}{0}+\binom{3}{2} = 1+3=4$.
- $b=1$: $2a+1 \equiv 0 \pmod 4 \Rightarrow 2a \equiv 3$, no solution.
Total: 4. Less than 8.

Hmm. It seems like all-1/2 is optimal. Let me try $f_1 = 1/2, f_2 = 1/2, f_3 = 1/4, f_4 = 3/4$.

Frac parts: 1/2, 1/2, 1/4, 3/4. Sum = $a/2 + c/4 + d \cdot 3/4$ where $a \in \{0,1,2\}$, $c, d \in \{0,1\}$. $= (2a + c + 3d)/4$. Integer iff $2a + c + 3d \equiv 0 \pmod 4$.

Let me enumerate all 16 subsets. Actually let me just count solutions.

For each $(c, d)$:
- (0,0): $2a \equiv 0 \pmod 4 \Rightarrow a \in \{0, 2\}$. 2 choices of $a$, each with $\binom{2}{a}$ ways. $a=0$: 1, $a=2$: 1. Total 2.
- (1,0): $2a + 1 \equiv 0 \pmod 4 \Rightarrow 2a \equiv 3$, no. 0.
- (0,1): $2a + 3 \equiv 0 \pmod 4 \Rightarrow 2a \equiv 1$, no. 0.
- (1,1): $2a + 4 \equiv 0 \pmod 4 \Rightarrow 2a \equiv 0 \Rightarrow a \in \{0,2\}$. $a=0$: $\binom{2}{0}=1$, $a=2$: $\binom{2}{2}=1$. Total 2.

Total: 2 + 0 + 0 + 2 = 4. Still less than 8.

OK so it really seems like all-1/2 giving $2^{n-1}$ is the max. Let me try to prove the lemma.

Lemma: For non-integer $w_1, \ldots, w_n$, the number of subsets $S$ with $\sum_{i \in S} w_i \in \mathbb{Z}$ is at most $2^{n-1}$.

Proof: Consider the fractional parts $f_i = \{w_i\} \in (0,1) \cap (\mathbb{R} \setminus \mathbb{Z})$... well $f_i \in (0,1)$. We want to count subsets $S$ with $\sum_{i \in S} f_i \in \mathbb{Z}$.

Consider the involution on subsets: pair $S$ with $S \triangle \{n\}$ (toggle the last element). For each pair $(S, S \triangle \{n\})$, the frac sums differ by $f_n \not\equiv 0 \pmod 1$. So they can't both be integers! Because if $\sum_S f_i \equiv 0$ and $\sum_{S \triangle \{n\}} f_i \equiv 0$, then $f_n \equiv 0$, contradiction.

So in each of the $2^{n-1}$ pairs, at most one is integer. Hence at most $2^{n-1}$ integer subset sums. 

That's a clean proof. So the maximum number of integer subset sums with $n$ non-integer weights is $2^{n-1}$ (and this is achieved when all $f_i = 1/2$, since then exactly the even subsets are integer, giving $2^{n-1}$).

Now, we need to cover $\{0, 1, 2, \ldots, 40\}$, which is 41 distinct integer values. So we need at least 41 integer subset sums. Thus $2^{n-1} \geq 41$, giving $n - 1 \geq 6$, i.e., $n \geq 7$.

Wait, $2^{n-1} \geq 41 \Rightarrow n-1 \geq 6 \Rightarrow n \geq 7$. (Since $2^5 = 32 < 41 \leq 64 = 2^6$.)

So $n \geq 7$.

Now I need to show $n = 7$ is achievable. With 7 weights, we have $2^6 = 64$ integer subset sums (if all frac 1/2). We need to cover 0..40 (41 values) using 64 even-sized subsets of 7 weights with fractional part 1/2.

With all weights having fractional part 1/2, integer subset sums come from even-sized subsets. The even-sized subsets of 7 elements: sizes 0, 2, 4, 6. Count: $1 + 21 + 35 + 7 = 64$.

We need these 64 sums to include all integers 0..40. Let me try to construct such weights.

Let $w_i = a_i + 1/2$ where $a_i$ are non-negative integers (and weights distinct, so $a_i$ distinct). Even-sized subset $S$ gives sum $\sum_{i \in S} a_i + |S|/2$.

For $|S| = 0$: sum 0.
For $|S| = 2$: sum $a_i + a_j + 1$.
For $|S| = 4$: sum $a_i + a_j + a_k + a_l + 2$.
For $|S| = 6$: sum (sum of 6 a's) + 3.

We need to cover 1..40.

Let me think of a good choice. We want the pair sums $a_i + a_j + 1$ to cover a range, and 4-sums and 6-sums to extend it.

This is like a covering problem. Let me think about what values we can get.

Actually, let me think about it more cleverly. Consider choosing $a_i$ such that the even-subset sums cover 0..40. 

Hmm, let me think about a different approach. What if I use weights that are like $1/2, 3/2, 5/2, ...$? No, let me think systematically.

Actually, let me think about whether we can use a "binary-like" construction. 

With 6 integer weights $1, 2, 4, 8, 16, 32$ (powers of 2), every integer 0..63 is a subset sum. That's the standard binary representation. But these are integers, not allowed.

What if I take 7 weights: split one of the powers of 2 into two non-integer halves? For instance, replace 1 with $1/2 + 1/2$... but those are equal. Or replace weight 1 with two weights $1/2 + \epsilon$ and $1/2 - \epsilon$? Then their sum is 1, and individually they're non-integer. But then subset sums involving just one of them would be non-integer, so we'd lose some integers.

Hmm, let me think differently. 

Actually, the key insight: with 7 weights all having fractional part 1/2, we get 64 even-subset sums. We need 41 of them to be 0..40. The question is whether we can arrange the $a_i$ to achieve this.

Let me try $a_i = 0, 1, 2, 4, 8, 16, 32$ (i.e., weights $0.5, 1.5, 2.5, 4.5, 8.5, 16.5, 32.5$).

Even subset sums: $\sum_{i \in S} a_i + |S|/2$ where $|S|$ even.

The $\sum a_i$ part: with $a_i = 0,1,2,4,8,16,32$, the subset sums of the $a_i$ cover all integers 0..63 (binary). But we only take even-sized subsets, and add $|S|/2$.

This is getting complicated. Let me think about it computationally (in my head).

Actually, let me think about a cleaner construction. 

Alternative idea: Use weights $w_i = 2^{i-1} + 1/2$ for $i = 1, \ldots, 6$ and one more weight. Hmm.

Let me think about the problem differently. We have 7 weights with frac 1/2. Let me denote the integer parts as $a_1 < a_2 < \ldots < a_7$ (non-negative integers, distinct for distinct weights). 

Even subset of size $2k$: sum = (sum of selected $a_i$) + $k$.

I want every integer 1..40 to appear as such a sum.

Let me try to think about what's the maximum consecutive range we can cover.

Actually, maybe I should think about it as: the set of even-subset sums. Let me consider the "complement" trick. For a subset $S$ of $[7]$, let $T = [7] \setminus S$. $|S|$ even iff $|T|$ odd (since 7 is odd). Sum of $S$ = (total sum) - sum of $T$. So even-subset sums = total - odd-subset sums. Not directly helpful.

Let me just try a specific construction and verify.

Try: $a = (0, 1, 2, 3, 4, 5, 6)$, weights $0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5$.

Even subsets:
- Size 0: 0.
- Size 2: $a_i + a_j + 1$ for $i < j$. Range: $0+1+1=2$ to $5+6+1=12$. All integers 2..12? The pair sums $a_i+a_j$ for $0,1,...,6$ range from 1 to 11, and I believe all integers 1..11 are achievable (since consecutive). So size-2 sums cover 2..12.
- Size 4: $a_i+a_j+a_k+a_l + 2$. Sum of 4 from $\{0,...,6\}$: min $0+1+2+3=6$, max $3+4+5+6=18$. Plus 2: 8..20. Are all integers 8..20 achievable? Sum of 4 distinct from 0..6: the 4-sums. Min 6, max 18. Consecutive? $6 = 0+1+2+3$, $7 = 0+1+2+4$, ..., likely all 6..18. So size-4 sums cover 8..20.
- Size 6: sum of 6 from $\{0,...,6\}$ + 3. Sum of 6 = total(21) - excluded. Excluded is one of 0..6. So 6-sums = 21 - {0,...,6} = {15,...,21}. Plus 3: 18..24.

Total coverage: 0, 2..12, 8..20, 18..24 = 0, 2..24. Missing 1! And only goes up to 24, not 40.

So this doesn't work. The range is too small. We need larger $a_i$ values.

The issue is we need to reach up to 40. With 7 weights, the max even-subset sum is the sum of the 6 largest + 3. To reach 40, we need the 6 largest $a_i$ to sum to at least 37.

Let me try a different approach. Think of it as: we want even-subset sums to cover 0..40. 

Let me try weights based on powers of 2 but shifted. 

Consider $a = (0, 1, 2, 4, 8, 16, 23)$. Total = 54. Hmm, let me think about what even subsets give.

Actually, this trial-and-error is hard. Let me think more structurally.

Key idea: We want to use the binary representation idea but adapted for even subsets.

Consider 6 "binary" weights $a = (1, 2, 4, 8, 16, 32)$ giving all integers 0..63 as subset sums. Now I want to convert this to a 7-weight non-integer system where even subsets give all integers 0..40 (or 0..63).

Here's an idea: Add a 7th weight $a_7 = 0$ (weight $0.5$). Then for any subset $S$ of the first 6, if $|S|$ is even, use it directly (sum = $\sum a_i + |S|/2$). If $|S|$ is odd, add the 7th element (weight 0.5, $a_7 = 0$) to make it even: sum = $\sum a_i + 0 + (|S|+1)/2$.

So for any subset $S \subseteq \{1,...,6\}$:
- If $|S|$ even: even-subset sum = $\sum_{i \in S} a_i + |S|/2$.
- If $|S|$ odd: even-subset sum (with 7th) = $\sum_{i \in S} a_i + (|S|+1)/2$.

In both cases, the sum is $\sum_{i \in S} a_i + \lceil |S|/2 \rceil$.

Hmm, so the value is $\sum a_i + \lceil |S|/2 \rceil$. This is NOT simply $\sum a_i$; there's an extra term depending on $|S|$.

With $a = (1, 2, 4, 8, 16, 32)$: $\sum a_i$ ranges over 0..63. But the actual sum is $\sum a_i + \lceil |S|/2 \rceil$, which shifts things. Two different subsets with the same $\sum a_i$ but different parities of $|S|$ give different values. And actually, with binary weights, each integer 0..63 has a unique subset, so there's no collision issue—but the value is shifted by $\lceil |S|/2 \rceil$.

So the values we get are $\{v(S) + \lceil |S|/2 \rceil : S \subseteq [6]\}$ where $v(S) = \sum_{i \in S} 2^{i-1}$ is the binary value. This is a shifted version, and the shifts vary. The set of values is $\{0, 1+1, 2+1, 3+2, 4+1, 5+2, 6+2, 7+3, ...\}$. Let me compute for small values:

- $S = \emptyset$: $v=0, |S|=0$, value $0 + 0 = 0$.
- $S = \{1\}$: $v=1, |S|=1$, value $1 + 1 = 2$.
- $S = \{2\}$: $v=2, |S|=1$, value $2 + 1 = 3$.
- $S = \{1,2\}$: $v=3, |S|=2$, value $3 + 1 = 4$.
- $S = \{3\}$: $v=4, |S|=1$, value $4 + 1 = 5$.
- $S = \{1,3\}$: $v=5, |S|=2$, value $5 + 1 = 6$.
- $S = \{2,3\}$: $v=6, |S|=2$, value $6 + 1 = 7$.
- $S = \{1,2,3\}$: $v=7, |S|=3$, value $7 + 2 = 9$.
- $S = \{4\}$: $v=8, |S|=1$, value $8 + 1 = 9$. Collision with previous!

So 9 appears twice, and 1 and 8 are missing. This doesn't cover all integers.

The problem is the shift $\lceil |S|/2 \rceil$ disrupts the binary structure.

Let me think differently. Maybe I should not use the 7th weight as $a_7 = 0$.

Alternative approach: Think of the 7 weights as $w_i = a_i + 1/2$. Even subset sums = $\sum_{i \in S} a_i + |S|/2$ for even $|S|$. 

I want to choose $a_i$ so that these cover 0..40. Let me think of choosing $a_i$ to be roughly $0, 1, 3, 7, 15, ...$ or some other pattern.

Actually, let me think about this more carefully. Let me consider the following approach:

We have 7 weights. Consider pairing them: think of the 7 weights as providing a "base" system. 

Hmm, let me try yet another approach. Let me consider weights:
$w_1 = 1/2, w_2 = 1/2, w_3 = 3/2, w_4 = 3/2, w_5 = 7/2, w_6 = 7/2, w_7 = ?$

No, this is getting messy. Let me think about it more carefully.

Actually, let me reconsider. Maybe I should allow weights to be equal (multiset). The problem says "a set of control weights" which in competition math might allow repeated values. But "set" usually means distinct. Let me consider both cases.

Let me try to think about the problem from a higher level. We need 7 weights with fractional part 1/2 (to maximize integer subset sums to 64), and we need the 64 even-subset sums to include all of 0..40.

Let me try the construction with $a_i$ being $0, 1, 2, 4, 8, 16, 32$ but think about which even-subset sums we get.

Weights: $0.5, 1.5, 2.5, 4.5, 8.5, 16.5, 32.5$.

Even subset sum = $\sum_{i \in S} a_i + |S|/2$ where $a = (0,1,2,4,8,16,32)$ and $|S|$ even.

Let me think about which integers are hit. For a target integer $m$, I need an even subset $S$ with $\sum_{i \in S} a_i = m - |S|/2$.

Let $v = \sum_{i \in S} a_i$ (a subset sum of $\{0,1,2,4,8,16,32\}$, which can be any integer 0..63) and $|S| = $ number of elements. The actual value is $v + |S|/2$.

For each $v \in \{0,...,63\}$, let $s(v)$ = number of 1-bits in binary representation of $v$ (since $a_i = 0, 1, 2, 4, 8, 16, 32$ are powers of 2 plus 0; the subset for value $v$ is determined by binary representation, and $|S|$ = popcount of $v$ if $v > 0$, or 0 if $v = 0$). Wait, $a_1 = 0$ is special. The subset sum $v$ of $\{0, 1, 2, 4, 8, 16, 32\}$: the element 0 can be included or not without changing $v$. So for $v > 0$, there are two subsets giving $v$: one with 0 included, one without. Their sizes differ by 1 (one even, one odd). So for each $v > 0$, exactly one of the two subsets is even-sized!

So for each $v \in \{1, ..., 63\}$, there's exactly one even subset with $\sum a_i = v$, and its size is either popcount($v$) or popcount($v$) + 1 (whichever is even). The value is $v + |S|/2$.

If popcount($v$) is even, $|S| = $ popcount($v$) (without 0) — wait, we need to be careful. The two subsets for value $v$ are: $S_0$ (without element 0) and $S_1 = S_0 \cup \{0\}$. $|S_0| = $ popcount($v$), $|S_1| = $ popcount($v$) + 1. Exactly one is even.

If popcount($v$) even: $|S_0|$ even, use $S_0$. Value = $v + $ popcount($v$)/2.
If popcount($v$) odd: $|S_1|$ even, use $S_1$. Value = $v + (popcount(v)+1)/2$.

And for $v = 0$: subsets are $\emptyset$ (size 0, even) and $\{0\}$ (size 1, odd). Even one is $\emptyset$, value 0.

So the set of even-subset values is:
$\{0\} \cup \{v + \lceil \text{popcount}(v)/2 \rceil : v = 1, ..., 63\}$.

Wait: if popcount even, value = $v + $ popcount/2. If popcount odd, value = $v + (popcount+1)/2 = v + \lceil$ popcount/2 $\rceil$. So in both cases, value = $v + \lceil$ popcount$(v)/2 \rceil$.

So the values are $f(v) = v + \lceil \text{popcount}(v) / 2 \rceil$ for $v = 0, 1, ..., 63$ (with $f(0) = 0$).

Now I need to check: does $\{f(v) : v = 0, ..., 63\}$ contain all integers 0..40?

Let me compute $f(v)$ for $v = 0, ..., 40$ and see what's covered.

$f(0) = 0$
$f(1) = 1 + 1 = 2$ (popcount 1, ceil(1/2)=1)
$f(2) = 2 + 1 = 3$ (popcount 1)
$f(3) = 3 + 1 = 4$ (popcount 2, ceil(2/2)=1)
$f(4) = 4 + 1 = 5$ (popcount 1)
$f(5) = 5 + 1 = 6$ (popcount 2)
$f(6) = 6 + 1 = 7$ (popcount 2)
$f(7) = 7 + 2 = 9$ (popcount 3, ceil(3/2)=2)
$f(8) = 8 + 1 = 9$ (popcount 1)
$f(9) = 9 + 1 = 10$ (popcount 2)
$f(10) = 10 + 1 = 11$ (popcount 2)
$f(11) = 11 + 2 = 13$ (popcount 3)
$f(12) = 12 + 1 = 13$ (popcount 2)
$f(13) = 13 + 2 = 15$ (popcount 3)
$f(14) = 14 + 2 = 16$ (popcount 3)
$f(15) = 15 + 2 = 17$ (popcount 4, ceil(4/2)=2)
$f(16) = 16 + 1 = 17$ (popcount 1)
$f(17) = 17 + 1 = 18$ (popcount 2)
$f(18) = 18 + 1 = 19$ (popcount 2)
$f(19) = 19 + 2 = 21$ (popcount 3)
$f(20) = 20 + 1 = 21$ (popcount 2)
$f(21) = 21 + 2 = 23$ (popcount 3)
$f(22) = 22 + 2 = 24$ (popcount 3)
$f(23) = 23 + 2 = 25$ (popcount 4)
$f(24) = 24 + 1 = 25$ (popcount 2)
$f(25) = 25 + 2 = 27$ (popcount 3)
$f(26) = 26 + 2 = 28$ (popcount 3)
$f(27) = 27 + 2 = 29$ (popcount 4)
$f(28) = 28 + 1 = 29$ (popcount 3)... wait popcount(28) = popcount(11100) = 3. $f(28) = 28 + 2 = 30$. Let me recompute.

Hold on, let me be more careful with popcounts.

$v=28 = 11100_2$, popcount = 3. $f(28) = 28 + 2 = 30$.
$v=29 = 11101_2$, popcount = 4. $f(29) = 29 + 2 = 31$.
$v=30 = 11110_2$, popcount = 4. $f(30) = 30 + 2 = 32$.
$v=31 = 11111_2$, popcount = 5. $f(31) = 31 + 3 = 34$.
$v=32 = 100000_2$, popcount = 1. $f(32) = 32 + 1 = 33$.
$v=33 = 100001_2$, popcount = 2. $f(33) = 33 + 1 = 34$.
$v=34 = 100010_2$, popcount = 2. $f(34) = 34 + 1 = 35$.
$v=35 = 100011_2$, popcount = 3. $f(35) = 35 + 2 = 37$.
$v=36 = 100100_2$, popcount = 2. $f(36) = 36 + 1 = 37$.
$v=37 = 100101_2$, popcount = 3. $f(37) = 37 + 2 = 39$.
$v=38 = 100110_2$, popcount = 3. $f(38) = 38 + 2 = 40$.
$v=39 = 100111_2$, popcount = 4. $f(39) = 39 + 2 = 41$.
$v=40 = 101000_2$, popcount = 2. $f(40) = 40 + 1 = 41$.

Now let me collect all $f(v)$ for $v = 0..40$:
0, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11, 13, 13, 15, 16, 17, 17, 18, 19, 21, 21, 23, 24, 25, 25, 27, 28, 29, 30, 31, 32, 34, 33, 34, 35, 37, 37, 39, 40, 41, 41.

Let me list unique values: 0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 17, 18, 19, 21, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 39, 40, 41.

Missing from 0..40: 1, 8, 12, 14, 20, 22, 26, 36, 38.

So this construction misses 1, 8, 12, 14, 20, 22, 26, 36, 38. Not good enough.

The problem is the shift $\lceil \text{popcount}/2 \rceil$ creates gaps. 

Let me think about a better construction. Maybe instead of $a_1 = 0$, I should use a different set of $a_i$.

The fundamental issue: with all fractional parts 1/2, the even-subset sums are $\sum a_i + |S|/2$. The $|S|/2$ term depends on subset size, which disrupts the clean binary structure.

Let me think about this differently. What if I use pairs of weights?

Idea: Group the 7 weights into pairs plus one. For each pair $(w_{2k-1}, w_{2k})$, think of selecting 0 or 2 from the pair (contributing an even number) vs selecting 1 (contributing an odd number, which must be paired with the odd selection from another pair or the singleton).

Hmm, this is getting complicated. Let me think about a completely different construction.

Alternative: What if not all weights have fractional part 1/2? We showed that the maximum number of integer subset sums is $2^{n-1} = 64$ for $n=7$, achieved when all have frac 1/2. But maybe with fewer integer subset sums (but still $\geq 41$), we can arrange them to be exactly 0..40 plus some extras.

But with the pairing argument, we get at most 64 integer subset sums. If we use frac 1/2 for all, we get exactly 64. If we use other fractional parts, we get fewer. With 64 we have 23 "extra" slots beyond 41, so there's room for some non-consecutive values. The question is whether we can make 0..40 all appear.

Let me try a different set of $a_i$. Instead of powers of 2, let me try to make the construction work by choosing $a_i$ more carefully.

Let me think about what we need. We have 7 weights $w_i = a_i + 1/2$. Even subsets give $\sum_{i \in S} a_i + |S|/2$. We need all integers 0..40.

Let me try to think of this as: define $b_i = 2a_i + 1 = 2w_i$ (odd positive integers). Then $2 \cdot (\text{even subset sum}) = \sum_{i \in S} b_i$ where $|S|$ is even. So the even subset sums of $w$ are exactly $\frac{1}{2} \sum_{i \in S} b_i$ for even $|S|$, and we need these to be integers 0..40, i.e., $\sum_{i \in S} b_i$ to be even integers 0..80.

Since $b_i$ are odd, $\sum_{i \in S} b_i$ is even iff $|S|$ is even. So we need: for every even integer $2m$ with $m = 0, ..., 40$, there's an even subset $S$ with $\sum_{i \in S} b_i = 2m$.

Equivalently: the even-subset sums of 7 odd integers $b_1, ..., b_7$ must cover all even integers $0, 2, 4, ..., 80$.

Hmm, or equivalently, dividing by 2: Let $c_i = b_i / 2$... no, $b_i$ are odd, so $b_i/2$ is not integer.

Let me think about it as: we need even-subset sums of odd integers $b_1, ..., b_7$ to cover $\{0, 2, 4, ..., 80\}$.

Alternatively, think of selecting an even number of the $b_i$. The sum of an even number of odd integers is even. We need all even values 0..80.

Let me try $b_i = 1, 1, 3, 5, 11, 21, 43$... no let me think more systematically.

Actually, let me try a different approach entirely. Let me consider the possibility that we don't need all weights to have frac 1/2.

Wait, but we proved the max integer subset sums is $2^{n-1} = 64$, and we need 41. So we need at least 41 integer subset sums. With all frac 1/2 we get 64. With other configurations we might get between 41 and 64. But the pairing argument shows we get at most 64, and the all-1/2 case gives exactly 64.

But maybe a non-all-1/2 configuration with, say, 50 integer subset sums could be arranged to hit exactly 0..40 plus 9 others. The question is whether such an arrangement exists.

This seems hard to reason about in general. Let me go back to trying to make the all-1/2 construction work with better $a_i$.

Let me reformulate: choose 7 distinct non-negative integers $a_1 < ... < a_7$ such that the set $\{\sum_{i \in S} a_i + |S|/2 : S \subseteq [7], |S| \text{ even}\}$ contains $\{0, 1, ..., 40\}$.

Equivalently (with $b_i = 2a_i + 1$ odd): $\{\sum_{i \in S} b_i : S \subseteq [7], |S| \text{ even}\}$ contains $\{0, 2, 4, ..., 80\}$.

Let me try to think of this as a subset sum covering problem. We need even-sized subsets of 7 odd numbers to cover all even numbers 0..80.

Let me try $b = (1, 3, 5, 7, 9, 11, 13)$ (i.e., $a = (0,1,2,3,4,5,6)$). Even subset sums:
- Size 0: 0.
- Size 2: sums of pairs from $\{1,3,5,7,9,11,13\}$. Min $1+3=4$, max $11+13=24$. All even numbers 4..24? Pair sums: $1+3=4, 1+5=6, 1+7=8, ..., 3+5=8, ...$. The pairs of odd numbers from 1..13 (odd). Sums range 4..24, all even. Are all even 4..24 achieved? $4=1+3, 6=1+5, 8=1+7=3+5, 10=1+9=3+7, 12=1+11=3+9=5+7, 14=1+13=3+11=5+9, 16=3+13=5+11=7+9, 18=5+13=7+11, 20=7+13=9+11, 22=9+13, 24=11+13$. Yes, all even 4..24.
- Size 4: sums of 4 from $\{1,3,5,7,9,11,13\}$. Min $1+3+5+7=16$, max $7+9+11+13=40$. All even 16..40? Likely yes (consecutive odd numbers, 4-sums should be consecutive even). 
- Size 6: sums of 6 = total(49) - excluded. Excluded one of $\{1,3,5,7,9,11,13\}$. So 6-sums = $49 - \{1,3,...,13\} = \{36, 34, 32, 30, 28, 26, 24\}$. Even numbers 24..36 (not all, just 24,26,28,30,32,34,36).

Total coverage: 0, 4..24, 16..40, 24..36 = 0, 4..40. Missing 2!

So close! We cover 0 and 4..40, missing only 2. If we could get 2 as well, we'd have 0..40.

To get 2: need an even subset summing to 2 (in $b$ terms) or 1 (in $w$ terms). The smallest positive even-subset sum is a pair sum. The smallest pair sum is $b_1 + b_2$. For this to be 2, we need $b_1 + b_2 = 2$, but $b_i \geq 1$ (odd positive), so $b_1 = b_2 = 1$, meaning $a_1 = a_2 = 0$, weights equal ($w_1 = w_2 = 0.5$). If equal weights are allowed, this works!

But if weights must be distinct, $b_1 < b_2$ means $b_1 + b_2 \geq 1 + 3 = 4$, so the smallest even-subset sum (besides 0) is 4, and we can never get 2.

Hmm. So with distinct weights and all frac 1/2, we can't get 1 (i.e., $b$-sum 2) because the smallest pair sum is at least $1 + 3 = 4$.

Wait, unless we use a size-4 or size-6 subset that sums to 2. But size-4 sum of positive odd integers is at least $1+3+5+7 = 16 > 2$. So no.

So with distinct weights, all frac 1/2, we can never produce the value 1. That's a problem!

Hmm, but wait. What if $a_i$ can be negative? The problem says weights are non-integer grams. Weights should be positive (they're physical weights). So $w_i > 0$, meaning $a_i \geq 0$ (since $w_i = a_i + 1/2 > 0$ means $a_i \geq 0$). And for distinct weights, $a_i$ distinct non-negative integers, so $a_i \geq 0, 1, 2, ...$, meaning $b_i \geq 1, 3, 5, ...$.

So the smallest even-subset sum (other than 0) is $b_1 + b_2 \geq 1 + 3 = 4$, corresponding to $w$-value 2. We can never get $w$-value 1.

This means: with distinct weights all having frac 1/2, we cannot produce the value 1. So we cannot cover 1..40!

This is a fundamental obstruction. So either:
1. Equal weights are allowed (then $b_1 = b_2 = 1$ works), or
2. We need a different fractional part configuration.

Let me reconsider. If equal weights are allowed, the construction $b = (1, 1, 5, 7, 9, 11, 13)$... wait, let me redo. With $b_1 = b_2 = 1$ (i.e., $w_1 = w_2 = 0.5$), and then $b_3, ..., b_7 = 5, 7, 9, 11, 13$ (i.e., $a = 0, 0, 2, 3, 4, 5, 6$).

Even subset sums:
- Size 0: 0.
- Size 2: pairs. $1+1=2, 1+5=6, 1+7=8, 1+9=10, 1+11=12, 1+13=14, 5+7=12, 5+9=14, 5+11=16, 5+13=18, 7+9=16, 7+11=18, 7+13=20, 9+11=20, 9+13=22, 11+13=24$. So even values: 2, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24. Missing 4!
- Size 4: 4-sums. Min $1+1+5+7=14$, max $9+11+13+? $... let me think. Actually with $b = (1,1,5,7,9,11,13)$, 4-sums range from $1+1+5+7=14$ to $7+9+11+13=40$ (excluding the two 1's). Actually max 4-sum = $9+11+13+7 = 40$ or $1+9+11+13=34$... wait, the 4 largest are $7, 9, 11, 13$ summing to 40. So 4-sums range 14..40. But do they cover all even 14..40? With two 1's and $5,7,9,11,13$: 4-sums include $1+1+5+7=14, 1+1+5+9=16, 1+1+5+11=18, 1+1+5+13=20, 1+1+7+9=18, 1+1+7+11=20, 1+1+7+13=22, 1+1+9+11=22, 1+1+9+13=24, 1+1+11+13=26, 1+5+7+9=22, 1+5+7+11=24, 1+5+7+13=26, 1+5+9+11=26, 1+5+9+13=28, 1+5+11+13=30, 1+7+9+11=28, 1+7+9+13=30, 1+7+11+13=32, 1+9+11+13=34, 5+7+9+11=32, 5+7+9+13=34, 5+7+11+13=36, 5+9+11+13=38, 7+9+11+13=40$. 

So 4-sums: 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40. All even 14..40. 

- Size 6: 6-sums = total - excluded. Total = $1+1+5+7+9+11+13 = 47$. 6-sums = $47 - \{1,1,5,7,9,11,13\} = \{46, 46, 42, 40, 38, 36, 34\}$. Even values: 34, 36, 38, 40, 42, 46.

Total coverage: 0, 2, {6,8,10,12,14,16,18,20,22,24} (size 2), {14..40 even} (size 4), {34,36,38,40,42,46} (size 6).

Combined: 0, 2, 6, 8, 10, 12, 14, ..., 40. Missing 4!

Still missing 4. The problem is that with $b_1 = b_2 = 1$ and $b_3 = 5$, there's a gap: pair sums give 2 (from $1+1$) and then 6 (from $1+5$), skipping 4.

To get 4, I need either a pair summing to 4 (need $b_i + b_j = 4$, so $1+3$) or a 4-sum of 4 (impossible, min is much larger).

So I need $b$ values including both 1 and 3. Let me try $b = (1, 3, 5, 7, 9, 11, 13)$ but with $b_1 = 1, b_2 = 3$ — but then the smallest pair sum is $1+3=4$, missing 2. And to get 2, I need two 1's.

So I need $b = (1, 1, 3, ...)$. Let me try $b = (1, 1, 3, 5, 7, 9, 11)$, i.e., $a = (0, 0, 1, 2, 3, 4, 5)$, weights $0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5$.

Total = $1+1+3+5+7+9+11 = 37$.

Even subset sums:
- Size 0: 0.
- Size 2: pairs from $\{1,1,3,5,7,9,11\}$. $1+1=2, 1+3=4, 1+5=6, 1+7=8, 1+9=10, 1+11=12, 3+5=8, 3+7=10, 3+9=12, 3+11=14, 5+7=12, 5+9=14, 5+11=16, 7+9=16, 7+11=18, 9+11=20$. Even values: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. All even 2..20!
- Size 4: 4-sums from $\{1,1,3,5,7,9,11\}$. Min $1+1+3+5=10$, max $5+7+9+11=32$. Do they cover all even 10..32? Let me check a few: $10, 1+1+3+7=12, 1+1+3+9=14, 1+1+3+11=16, 1+1+5+7=14, 1+1+5+9=16, 1+1+5+11=18, 1+1+7+9=18, 1+1+7+11=20, 1+1+9+11=22, 1+3+5+7=16, 1+3+5+9=18, 1+3+5+11=20, 1+3+7+9=20, 1+3+7+11=22, 1+3+9+11=24, 1+5+7+9=22, 1+5+7+11=24, 1+5+9+11=26, 1+7+9+11=28, 3+5+7+9=24, 3+5+7+11=26, 3+5+9+11=28, 3+7+9+11=30, 5+7+9+11=32$. So 4-sums: 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32. All even 10..32!
- Size 6: 6-sums = total(37) - excluded. Excluded from $\{1,1,3,5,7,9,11\}$. 6-sums = $37 - \{1,1,3,5,7,9,11\} = \{36, 36, 34, 32, 30, 28, 26\}$. Even values: 26, 28, 30, 32, 34, 36.

Total coverage: 0, 2..20 (even), 10..32 (even), 26..36 (even) = 0, 2, 4, 6, ..., 36. All even 0..36!

In $w$-terms: 0, 1, 2, ..., 18. We only cover up to 18, not 40!

The total sum is 37, so the max even-subset sum is 36 (in $b$-terms) = 18 (in $w$-terms). We need to reach 40 in $w$-terms = 80 in $b$-terms. So total sum of $b_i$ must be at least 80, but here it's only 37.

So I need much larger $b_i$ values. But I also need the small values (2, 4, 6, ...) to be covered. There's a tension: large total sum requires large $b_i$, but covering small even numbers requires small $b_i$.

The key insight from the $b = (1, 1, 3, 5, 7, 9, 11)$ example: with consecutive odd numbers (plus an extra 1), the even-subset sums cover all even numbers from 0 up to (total - smallest). The total is 37, smallest $b$ is 1, so we cover 0..36.

To cover 0..80, we'd need total $\geq 81$ and the structure to be "consecutive enough." But with only 7 odd numbers, the total is at most... well, we can make them as large as we want. But then the small values won't be covered.

Wait, the issue is: with 7 odd numbers, the pair sums cover a range, the 4-sums cover a range, and the 6-sums cover a range. For full coverage 0..80, these ranges need to overlap and cover everything.

Let me think about this more carefully. With $b = (1, 1, 3, 5, 7, 9, 11)$, we covered 0..36. The total is 37. The coverage is 0 to total - 1 = 36. 

What if I use $b = (1, 1, 3, 5, 7, 9, 11 + k)$ for some $k$? Let me think...

Actually, the pattern with consecutive odd numbers $1, 1, 3, 5, 7, 9, 11$ gives coverage 0..(total-1). If I increase the largest element, the total increases but there might be gaps.

Let me try $b = (1, 1, 3, 5, 7, 9, 53)$. Total = 79.

- Size 2: pairs. Without 53: $2, 4, 6, 8, 10, 12, 14, 16, 18, 20$ (as before, from $\{1,1,3,5,7,9\}$... wait, we also have pairs with 53: $1+53=54, 1+53=54, 3+53=56, 5+53=58, 7+53=60, 9+53=62$. So size-2 sums: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 54, 56, 58, 60, 62.
- Size 4: 4-sums. Without 53: 10..32 (even). With 53: $53 + $ pair from $\{1,1,3,5,7,9\}$ = $53 + \{2,4,6,8,10,12,14,16,18,20\} = \{55, 57, 59, 61, 63, 65, 67, 69, 71, 73\}$. So size-4 sums: 10..32 (even) and 55..73 (odd!). Wait, 53 + even = odd. But we need even sums! $53$ is odd, pair sum is even, $53 + $ even = odd. So these are odd, not counted.

Hmm wait, I need to be more careful. 4-sums with 53: choose 3 from $\{1,1,3,5,7,9\}$ plus 53. 3 from $\{1,1,3,5,7,9\}$: sum is odd (3 odd numbers). $53 + $ odd = even. Good. 3-sums from $\{1,1,3,5,7,9\}$: $1+1+3=5, 1+1+5=7, 1+1+7=9, 1+1+9=11, 1+3+5=9, 1+3+7=11, 1+3+9=13, 1+5+7=13, 1+5+9=15, 1+7+9=17, 3+5+7=15, 3+5+9=17, 3+7+9=19, 5+7+9=21$. So 3-sums: 5, 7, 9, 11, 13, 15, 17, 19, 21. All odd 5..21. Plus 53: 58, 60, 62, 64, 66, 68, 70, 72, 74. So size-4 sums with 53: 58..74 (even).

Size-4 sums without 53: 10..32 (even) (from before, but now from $\{1,1,3,5,7,9\}$ which has 6 elements, 4-sums: min $1+1+3+5=10$, max $5+7+9+?$... wait, 4 from 6 elements $\{1,1,3,5,7,9\}$: max $3+5+7+9=24$. Hmm, that's different from before.

Let me recompute. $\{1,1,3,5,7,9\}$, 4-sums: min $1+1+3+5=10$, max $3+5+7+9=24$. Values: $10, 12, 14, 16, 18, 20, 22, 24$? Let me check: $1+1+3+5=10, 1+1+3+7=12, 1+1+3+9=14, 1+1+5+7=14, 1+1+5+9=16, 1+1+7+9=18, 1+3+5+7=16, 1+3+5+9=18, 1+3+7+9=20, 1+5+7+9=22, 3+5+7+9=24$. So 10, 12, 14, 16, 18, 20, 22, 24. All even 10..24.

Size-4 sums total: 10..24 (even) and 58..74 (even). Gap from 26 to 56!

- Size 6: 6-sums = total(79) - excluded. Excluded from $\{1,1,3,5,7,9,53\}$. 6-sums = $79 - \{1,1,3,5,7,9,53\} = \{78, 78, 76, 74, 72, 70, 26\}$. Even values: 26, 70, 72, 74, 76, 78.

Total coverage: 0, 2..20, 10..24, 54..62, 58..74, 26, 70..78.

Let me combine: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78.

Missing: 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52. Huge gap from 28 to 52.

So this doesn't work. The single large element creates a big gap.

The fundamental problem: with 7 weights, we have subset sizes 0, 2, 4, 6 (even). The pair sums, 4-sums, and 6-sums each cover a range, but these ranges may not overlap enough to cover 0..80.

Let me think about this more carefully. How many even numbers can 7 odd integers cover with their even subset sums?

The even subset sums come from sizes 0, 2, 4, 6. 
- Size 0: just 0. (1 value)
- Size 2: $\binom{7}{2} = 21$ pairs.
- Size 4: $\binom{7}{4} = 35$ quadruples.
- Size 6: $\binom{7}{6} = 7$ sextuples.
Total: 1 + 21 + 35 + 7 = 64 even subset sums (with possible collisions).

We need 41 distinct even values (0, 2, ..., 80). So we need at least 41 distinct values out of 64 subsets. That's feasible in principle, but the structure must be right.

The challenge is covering both small and large values. The pair sums cover small-to-medium, 4-sums cover medium-to-large, 6-sums cover large. For full coverage, we need these ranges to overlap.

Let me think about what range each covers. If $b_1 \leq b_2 \leq ... \leq b_7$:
- Pair sums: $b_1 + b_2$ to $b_6 + b_7$.
- 4-sums: $b_1 + b_2 + b_3 + b_4$ to $b_4 + b_5 + b_6 + b_7$.
- 6-sums: total $- b_7$ to total $- b_1$ (i.e., $b_1+...+b_6$ to $b_2+...+b_7$).

For full coverage 0..80 (in $b$-terms), we need:
- $b_1 + b_2 = 2$ (to get value 2, i.e., $w$-value 1). This requires $b_1 = b_2 = 1$.
- The ranges must be consecutive and cover up to 80.

With $b_1 = b_2 = 1$: pair sums range from 2 to $b_6 + b_7$. 4-sums from $1 + 1 + b_3 + b_4$ to $b_4 + b_5 + b_6 + b_7$. 6-sums from total $- b_7$ to total $- 1$.

For the pair sums to cover 2, 4, 6, ..., up to some point, and 4-sums to continue, and 6-sums to finish at 80.

Let me try to design $b$ so that:
- Pairs cover 2 to $2k$ for some $k$.
- 4-sums cover $2k-2$ to $2m$.
- 6-sums cover $2m - 2$ to 80.

With $b_1 = b_2 = 1$ and $b_3, ..., b_7$ being consecutive odd numbers $3, 5, 7, 9, 11$: total = 37, coverage 0..36. Not enough.

What if I make $b_3, ..., b_7$ grow faster? Like $3, 5, 9, 15, 25$? Total = $1+1+3+5+9+15+25 = 59$. Max 6-sum = total - 1 = 58. Not enough for 80.

I need total $\geq 81$. With $b_1 = b_2 = 1$, the other 5 must sum to $\geq 79$. So $b_3 + b_4 + b_5 + b_6 + b_7 \geq 79$.

But then the pair sums $b_i + b_j$ for $i, j \geq 3$ would be large, and there'd be a gap between the small pair sums (involving $b_1, b_2$) and the large ones.

Pair sums involving $b_1 = 1$: $1 + b_j$ for $j = 2, ..., 7$: $2, 1+b_3, 1+b_4, 1+b_5, 1+b_6, 1+b_7$. These are $2, 1+b_3, ..., 1+b_7$. If $b_3 = 3$, this gives 2, 4, then jumps to $1 + b_4$, etc.

Pair sums involving $b_2 = 1$: same as above (since $b_1 = b_2 = 1$), so $1 + b_j$ for $j = 3, ..., 7$: $1+b_3, ..., 1+b_7$.

Pair sums not involving 1's: $b_i + b_j$ for $3 \leq i < j \leq 7$: these are large.

So pair sums: $\{2\} \cup \{1 + b_j : j = 3,...,7\} \cup \{b_i + b_j : 3 \leq i < j \leq 7\}$.

The first part gives $\{2, 1+b_3, 1+b_4, 1+b_5, 1+b_6, 1+b_7\}$ — only 6 values (with $b_1=b_2=1$, $1+1=2$ and $1+b_j$ for $j \geq 3$ appears twice but same value). So 6 distinct values from the "small" pairs.

For these to cover 2, 4, 6, 8, 10, 12 (the first 6 even numbers), we need $1 + b_j \in \{4, 6, 8, 10, 12\}$, i.e., $b_j \in \{3, 5, 7, 9, 11\}$. So $b_3, ..., b_7 = 3, 5, 7, 9, 11$. But then total = 37, too small.

Alternatively, the 4-sums and 6-sums can fill in the gaps. Let me think about this differently.

Maybe I don't need the pair sums to cover all small even numbers. The 4-sums can also produce small values. The smallest 4-sum is $b_1 + b_2 + b_3 + b_4 = 1 + 1 + b_3 + b_4$. If $b_3 = 3, b_4 = 5$, this is 10. So 4-sums start at 10.

So pairs need to cover 2, 4, 6, 8 (before 4-sums kick in at 10). Pairs give $\{2, 1+b_3, 1+b_4, 1+b_5, 1+b_6, 1+b_7\} \cup \{b_i + b_j : i,j \geq 3\}$. For coverage of 2, 4, 6, 8: need $1+b_3 = 4$ (i.e., $b_3 = 3$), $1+b_4 = 6$ (i.e., $b_4 = 5$), and either $1+b_5 = 8$ (i.e., $b_5 = 7$) or $b_3 + b_4 = 8$ ($3 + 5 = 8$, yes!). So with $b_3 = 3, b_4 = 5$, pairs cover 2, 4, 6, 8 (from $1+1=2, 1+3=4, 1+5=6, 3+5=8$). Then 4-sums start at $1+1+3+5 = 10$.

Now, 4-sums need to cover from 10 up to where 6-sums take over. 6-sums range from total $- b_7$ to total $- 1$. For 6-sums to reach 80, total $- 1 \geq 80$, so total $\geq 81$.

Let me set $b = (1, 1, 3, 5, b_5, b_6, b_7)$ with $b_5 \leq b_6 \leq b_7$ and total $= 11 + b_5 + b_6 + b_7 \geq 81$, so $b_5 + b_6 + b_7 \geq 70$.

4-sums: 
- Without $b_5, b_6, b_7$ (i.e., from $\{1,1,3,5\}$): just $1+1+3+5 = 10$. (Only one 4-subset from the first 4.)
- With one of $b_5, b_6, b_7$: 3 from $\{1,1,3,5\}$ plus one large. 3 from $\{1,1,3,5\}$: $1+1+3=5, 1+1+5=7, 1+3+5=9$. (Note: two 1's, so $1+1+3$ appears once, $1+3+5$ appears twice but same value.) So 3-sums: 5, 7, 9. Plus $b_5, b_6, b_7$: $b_5+5, b_5+7, b_5+9, b_6+5, b_6+7, b_6+9, b_7+5, b_7+7, b_7+9$.
- With two of $b_5, b_6, b_7$: 2 from $\{1,1,3,5\}$ plus 2 large. 2 from $\{1,1,3,5\}$: $2, 4, 6, 8$. Plus pairs of large: $b_5+b_6, b_5+b_7, b_6+b_7$. So: $b_5+b_6+2, b_5+b_6+4, b_5+b_6+6, b_5+b_6+8, b_5+b_7+2, ..., b_6+b_7+8$. That's 12 values.
- With all three $b_5, b_6, b_7$: 1 from $\{1,1,3,5\}$ plus $b_5+b_6+b_7$. 1 from $\{1,1,3,5\}$: $1, 3, 5$ (the two 1's give same). So $b_5+b_6+b_7+1, b_5+b_6+b_7+3, b_5+b_6+b_7+5$.

This is getting very complex. Let me try specific values.

Let me try $b = (1, 1, 3, 5, 11, 21, 41)$. Total = $1+1+3+5+11+21+41 = 83$. We need coverage 0..80 (even). Max 6-sum = $83 - 1 = 82$. 

Hmm, let me try to think about this more cleverly. 

Actually, maybe I should think about it as a "binary" system but with the even-subset constraint.

Here's another idea. What if I use the following 7 weights:
$w_1 = w_2 = 1/2$ (so $b_1 = b_2 = 1$), and then $w_3, ..., w_7$ chosen so that the system acts like binary.

With $b_1 = b_2 = 1$: selecting both gives sum 2 (in $b$) = 1 (in $w$). Selecting neither gives 0. Selecting one gives 1 (odd, not an even sum by itself, but can be paired with another odd selection).

Hmm, I think the key difficulty is that we're constrained to even-sized subsets, which is like a "parity constraint" on the binary representation.

Let me think about a completely different approach to the construction. What if not all weights have frac 1/2?

We showed that with the pairing argument, at most $2^{n-1}$ integer subset sums. For $n = 7$, that's 64. We need 41. So we don't necessarily need all 64; we could have fewer but still $\geq 41$.

But the issue with all-1/2 is that we can't get value 1 with distinct weights. What if we use a mix of fractional parts?

Let me think about using some weights with frac 1/2 and some with frac 1/3, or other values.

Actually, let me reconsider whether equal weights are allowed. The problem says "a set of control weights." In many competition problems, "set" just means "collection" and repeated values are allowed. Also, the problem says "each of them weighs a non-integer number of grams" — this is about each weight being non-integer, not about them being distinct.

If equal weights are allowed, then the construction with $b = (1, 1, 3, 5, 7, 9, 11)$ (weights $0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5$) covers 0..18 in $w$-terms. But we need 0..40. Total $b$ = 37, max $w$-value = 18. Not enough.

I need total $b \geq 81$ (to reach $w$-value 40). With 7 odd numbers summing to $\geq 81$, and $b_1 = b_2 = 1$ (to get value 1), the remaining 5 sum to $\geq 79$.

Let me try to make the 5 remaining odd numbers form a "near-consecutive" sequence that fills in the gaps.

Actually, let me think about this problem from a different angle. Let me consider the following approach:

Use 7 weights where 6 of them form a "binary-like" system and the 7th fills gaps.

Or, think about it as follows. We need even-sized subsets of 7 odd numbers to cover all even integers 0..80. 

Let me consider the "two copies" trick. If I have 3 "binary" weights $b = (1, 3, 9)$ (in some sense), their subset sums are $\{0, 1, 3, 4, 9, 10, 12, 13\}$. These are all integers 0..13. But we need even subset sums of odd numbers.

Hmm, let me think about the problem differently.

What if I use the following approach: pair up the 7 weights as $(w_1, w_2), (w_3, w_4), (w_5, w_6)$ and a singleton $w_7$. For each pair, I can select 0, 1, or 2 elements. Selecting 0 or 2 from a pair contributes an even number of elements; selecting 1 contributes odd. The singleton contributes 1 (odd) if selected.

For the total to be even-sized: either select an even number from each pair and don't select the singleton, or select an odd number from some pairs and select the singleton (with the total odd-count being even, so the singleton makes it even).

This is getting complicated. Let me try a more computational approach and just try to find a working construction.

Let me try $b = (1, 1, 3, 5, 11, 21, 41)$. Total = 83.

Even subset sums:
Size 0: {0}
Size 2: all pairs.
$1+1=2, 1+3=4, 1+5=6, 1+11=12, 1+21=22, 1+41=42, 3+5=8, 3+11=14, 3+21=24, 3+41=44, 5+11=16, 5+21=26, 5+41=46, 11+21=32, 11+41=52, 21+41=62$.
(With two 1's, $1+3, 1+5, 1+11, 1+21, 1+41$ each appear twice but same value.)
Size 2 values: 2, 4, 6, 8, 12, 14, 16, 22, 24, 26, 32, 42, 44, 46, 52, 62.

Size 4: all 4-subsets. $\binom{7}{4} = 35$. This is a lot. Let me think about the range.
Min 4-sum: $1+1+3+5 = 10$. Max 4-sum: $11+21+41+5 = 78$ or $11+21+41+3 = 76$... actually max is $5+11+21+41 = 78$.
Let me list systematically. 4 from $\{1,1,3,5,11,21,41\}$:

Without 41: 4 from $\{1,1,3,5,11,21\}$. 
- $1+1+3+5=10, 1+1+3+11=16, 1+1+3+21=26, 1+1+5+11=18, 1+1+5+21=28, 1+1+11+21=34, 1+3+5+11=20, 1+3+5+21=30, 1+3+11+21=36, 1+5+11+21=38, 3+5+11+21=40$.
With 41: 3 from $\{1,1,3,5,11,21\}$ plus 41.
3-sums of $\{1,1,3,5,11,21\}$: $1+1+3=5, 1+1+5=7, 1+1+11=13, 1+1+21=23, 1+3+5=9, 1+3+11=15, 1+3+21=25, 1+5+11=17, 1+5+21=27, 1+11+21=33, 3+5+11=19, 3+5+21=29, 3+11+21=35, 5+11+21=37$.
Plus 41: $46, 48, 54, 64, 50, 56, 66, 58, 68, 74, 60, 70, 76, 78$.

Size 4 values: 10, 16, 18, 20, 26, 28, 30, 34, 36, 38, 40, 46, 48, 50, 54, 56, 58, 60, 64, 66, 68, 70, 74, 76, 78.

Size 6: 6 from 7 = exclude one. Total = 83.
$83-1=82, 83-1=82, 83-3=80, 83-5=78, 83-11=72, 83-21=62, 83-41=42$.
Size 6 values: 42, 62, 72, 78, 80, 82.

Now let me collect all even values covered:
Size 0: 0
Size 2: 2, 4, 6, 8, 12, 14, 16, 22, 24, 26, 32, 42, 44, 46, 52, 62
Size 4: 10, 16, 18, 20, 26, 28, 30, 34, 36, 38, 40, 46, 48, 50, 54, 56, 58, 60, 64, 66, 68, 70, 74, 76, 78
Size 6: 42, 62, 72, 78, 80, 82

All values: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82.

Let me check which even numbers 0..80 are covered:
0 ✓, 2 ✓, 4 ✓, 6 ✓, 8 ✓, 10 ✓, 12 ✓, 14 ✓, 16 ✓, 18 ✓, 20 ✓, 22 ✓, 24 ✓, 26 ✓, 28 ✓, 30 ✓, 32 ✓, 34 ✓, 36 ✓, 38 ✓, 40 ✓, 42 ✓, 44 ✓, 46 ✓, 48 ✓, 50 ✓, 52 ✓, 54 ✓, 56 ✓, 58 ✓, 60 ✓, 62 ✓, 64 ✓, 66 ✓, 68 ✓, 70 ✓, 72 ✓, 74 ✓, 76 ✓, 78 ✓, 80 ✓.

All even numbers 0..80 are covered! In $w$-terms, all integers 0..40 are covered!

Wait, let me double-check some of the gaps. Between size-2 and size-4:
Size 2 covers up to 8 (small ones), then jumps to 12, 14, 16. Size 4 starts at 10. So 10 is covered by size 4. 12 by size 2. What about the gap between 8 and 10? 8 is covered (size 2: $3+5=8$), 10 is covered (size 4: $1+1+3+5=10$). 9 is odd, not needed. Good.

Between 16 and 22: 16 (size 2: $5+11=16$ and size 4: $1+1+3+11=16$), 18 (size 4: $1+1+5+11=18$), 20 (size 4: $1+3+5+11=20$), 22 (size 2: $1+21=22$). ✓

Between 32 and 42: 32 (size 2: $11+21=32$), 34 (size 4: $1+1+11+21=34$), 36 (size 4: $1+3+11+21=36$), 38 (size 4: $1+5+11+21=38$), 40 (size 4: $3+5+11+21=40$), 42 (size 2: $1+41=42$ and size 6: $83-41=42$). ✓

Between 52 and 62: 52 (size 2: $11+41=52$), 54 (size 4: $41+13=54$, i.e., $41 + (1+1+11) = 54$). Wait, let me recheck. 3-sum $1+1+11 = 13$, $13 + 41 = 54$. ✓. 56 (size 4: $41 + 15 = 56$, $15 = 1+3+11$). ✓. 58 (size 4: $41 + 17 = 58$, $17 = 1+5+11$). ✓. 60 (size 4: $41 + 19 = 60$, $19 = 3+5+11$). ✓. 62 (size 2: $21+41=62$ and size 6: $83-21=62$). ✓

Between 62 and 72: 62 ✓, 64 (size 4: $41 + 23 = 64$, $23 = 1+1+21$). ✓. 66 (size 4: $41 + 25 = 66$, $25 = 1+3+21$). ✓. 68 (size 4: $41 + 27 = 68$, $27 = 1+5+21$). ✓. 70 (size 4: $41 + 29 = 70$, $29 = 3+5+21$). ✓. 72 (size 6: $83 - 11 = 72$). ✓

Between 72 and 80: 72 ✓, 74 (size 4: $41 + 33 = 74$, $33 = 1+11+21$). ✓. 76 (size 4: $41 + 35 = 76$, $35 = 3+11+21$). ✓. 78 (size 4: $41 + 37 = 78$, $37 = 5+11+21$ and size 6: $83 - 5 = 78$). ✓. 80 (size 6: $83 - 3 = 80$). ✓

Everything checks out! So the construction $b = (1, 1, 3, 5, 11, 21, 41)$ works, corresponding to weights $w = (0.5, 0.5, 1.5, 2.5, 5.5, 10.5, 20.5)$.

In $w$-terms: weights are $1/2, 1/2, 3/2, 5/2, 11/2, 21/2, 41/2$ grams. All non-integer. ✓

Let me verify a few specific values:
- $w = 1$: $1/2 + 1/2 = 1$. ✓ (subset of size 2)
- $w = 2$: $1/2 + 3/2 = 2$. ✓
- $w = 3$: $1/2 + 5/2 = 3$. ✓
- $w = 4$: $3/2 + 5/2 = 4$. ✓
- $w = 5$: $1/2 + 1/2 + 3/2 + 5/2 = 5$. ✓ (size 4, sum = $0.5 + 0.5 + 1.5 + 2.5 = 5$)
- $w = 40$: $41/2 + 21/2 + 11/2 + 5/2 + 3/2 = (41+21+11+5+3)/2 = 81/2$... that's 40.5, not 40. Hmm wait.

Wait, let me recheck. $w = 40$ corresponds to $b$-sum 80. $b$-sum 80 = total(83) - 3 = 80, which is the 6-subset excluding $b = 3$ (i.e., excluding $w = 3/2$). So the subset is $\{1/2, 1/2, 5/2, 11/2, 21/2, 41/2\}$, sum = $(1 + 1 + 5 + 11 + 21 + 41)/2 = 80/2 = 40$. ✓

Let me also check $w = 39$: $b$-sum 78. $78 = 83 - 5$ (exclude $b=5$, i.e., $w=5/2$): subset $\{1/2, 1/2, 3/2, 11/2, 21/2, 41/2\}$, sum = $(1+1+3+11+21+41)/2 = 78/2 = 39$. ✓

And $w = 38$: $b$-sum 76. $76 = 41 + 35 = 41 + (3+11+21)$. So subset $\{41/2, 3/2, 11/2, 21/2\}$, sum = $(41+3+11+21)/2 = 76/2 = 38$. ✓ (size 4)

Great, the construction works!

But wait — the weights $1/2$ and $1/2$ are equal. Is this allowed? The problem says "a set of control weights, each of them weighs a non-integer number of grams." It doesn't say they're distinct. In competition math, "a set of weights" typically allows equal weights (you can have multiple weights of the same denomination). So this should be fine.

But what if the problem requires distinct weights? Let me check if we can do it with distinct weights.

With distinct weights and all frac 1/2, we showed we can't get value 1 (smallest pair sum is $b_1 + b_2 \geq 1 + 3 = 4$, giving $w$-value 2). So we'd need a different fractional part configuration.

Hmm, but actually, let me reconsider. Maybe with distinct weights and non-1/2 fractional parts, we can still achieve 41 integer subset sums and cover 0..40.

Actually, the problem likely allows equal weights (it's a physical set of weights, you can have two 0.5g weights). Competition problems about balance weights typically allow this. The answer is 7.

But let me also verify the lower bound more carefully. We need at least 41 integer subset sums (values 0..40), and with $n$ non-integer weights, at most $2^{n-1}$ integer subset sums. $2^{n-1} \geq 41$ requires $n \geq 7$.

Wait, I should double-check: do we need 0 to be a subset sum? The problem says "any integer weight from 1g to 40g can be balanced." So we need 1..40, which is 40 values, plus 0 (empty set) is automatically there. So we need at least 40 non-zero integer subset sums plus 0, totaling 41. The bound $2^{n-1} \geq 41$ gives $n \geq 7$.

Actually, we need 40 distinct positive integer values (1..40) as subset sums, plus 0. So 41 distinct integer values. Since at most $2^{n-1}$ subsets have integer sums, we need $2^{n-1} \geq 41$, hence $n \geq 7$.

For $n = 6$: $2^5 = 32 < 41$. Not enough. So $n \geq 7$.

And we've constructed a solution with $n = 7$. So the answer is $\boxed{7}$.

Wait, I want to make sure the lower bound argument is airtight. The claim is: with $n$ non-integer weights, at most $2^{n-1}$ subsets have integer sum.

Proof: Pair up subsets as $(S, S \cup \{n\})$ for each $S \subseteq [n-1]$ (i.e., $S$ not containing element $n$, paired with $S \cup \{n\}$). There are $2^{n-1}$ such pairs. In each pair, the sums differ by $w_n$, which is non-integer. So if one sum is integer, the other is non-integer (integer + non-integer = non-integer). Hence at most one per pair is integer, giving at most $2^{n-1}$ integer subset sums.

This is correct. And we need at least 41 integer subset sums (0 through 40), so $2^{n-1} \geq 41$, giving $n \geq 7$.

Hmm wait, actually I need to be a bit more careful. We need the 40 values 1, 2, ..., 40 to each be achievable as a subset sum. These are 40 distinct integer values. Plus 0 (empty set). So we need at least 41 subsets with integer sums (and these must give distinct values 0..40). Since at most
