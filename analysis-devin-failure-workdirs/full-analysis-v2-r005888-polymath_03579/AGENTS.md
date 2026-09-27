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
  <problem_id>polymath_03579</problem_id>
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

Find the maximum number of telephone numbers that satisfy the following three conditions:
a) all are five-digit numbers, starting with 0 is allowed;
b) each number contains at most two different digits;
c) deleting any digit in two arbitrary numbers (possibly in different positions) does not lead to two identical sequences of length 4.

## Standard Solution

Let \( C \) be the set of telephone numbers that satisfy conditions a)-c) and has maximum cardinality. Let \( A \) be the set of telephone numbers from \( C \) in which there exists a digit that appears 4 or 5 times, and let \( B \) be the set of those numbers from \( C \) in which there exists a digit that appears exactly 3 times. Clearly, \( C = A \cup B \). Since \( C \) contains at most one number in which a fixed digit appears 4 or 5 times, we have \(|A| \leq 10\).

Let \( B_{i, j}, 0 \leq i, j \leq 9 \), be the set of numbers in which digit \( i \) appears 3 times, and digit \( j \) appears 2 times. We will prove that the maximum number of telephone numbers in \( B_{i, j} \cup B_{j, i} \) is 4. Without loss of generality, we can consider the case \( i=0, j=1 \). Let \( a_{i} \) be the number of telephone numbers from \( B_{0,1} \cup B_{1,0} \) with exactly \( i \) blocks. (The sequence of symbols \( a_{i}, \ldots, a_{j} \) is called a block if \( a_{i-1} \neq a_{i}=\cdots=a_{j} \neq a_{j+1} \).) If we assume that \(\left|B_{0,1} \cup B_{1,0}\right|=5\), then

\[
\begin{aligned}
a_{2}+a_{3}+a_{4}+a_{5} & =5 \\
2 a_{2}+3 a_{3}+4 a_{4}+5 a_{5} & \leq 14
\end{aligned}
\]

The last inequality follows from the fact that no two numbers have a common subsequence of length 4. It is immediately checked that \( a_{2} \leq 2 \) and \( a_{3} \leq 2 \). Therefore, the only possibility is \( a_{2}=a_{3}=2, a_{4}=1 \). Such a set of numbers must contain \( 01110 \) and \( 10001 \). It is now clear that no telephone number composed of two blocks can be added to these two numbers.

On the other hand, it is possible to find four words in \( B_{0,1} \cup B_{1,0} \) that satisfy condition c), for example

\[
B_{0,1} \cup B_{1,0}=\{10001,01010,11100,00111\}
\]

The set \( C \) can be represented as

\[
C=A \cup B=A \cup\left(\cup_{0 \leq i<j \leq 9} B_{i, j} \cup B_{j, i}\right).
\]

It is clear that the choice of numbers in \( B_{i, j} \cup B_{j, i} \) does not affect the choice of numbers in \( B_{k, l} \cup B_{l, k} \) for \((i, j) \neq(k, l)\). It is also clear that in \( A \) we can choose 10 numbers that do not affect the choice of the remaining numbers from \( C \), for example

\[
A=\{00000,11111, \ldots, 99999\}
\]

Therefore, the sought maximum number is

\[
\begin{aligned}
|C| & =|A|+\sum_{0 \leq i<j \leq 9}\left|B_{i, j} \cup B_{j, i}\right| \\
& =10+\binom{10}{2} \cdot 4 \\
& =10+45 \cdot 4=190
\end{aligned}
\]

Thus, the maximum number of telephone numbers is \(\boxed{190}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the maximum number of telephone numbers (5-digit sequences, leading 0 allowed) such that:
a) All are five-digit numbers (00000 to 99999, leading zeros allowed)
b) Each number contains at most two different digits
c) Deleting any digit in two arbitrary numbers (possibly in different positions) does not lead to two identical sequences of length 4.

So condition (c) says: for any two numbers in our set (possibly the same? "two arbitrary numbers" - I think this means any two distinct numbers, but let me think about whether it could mean the same number too), deleting one digit from each (any position) should not produce the same 4-digit sequence.

Wait, let me re-read: "deleting any digit in two arbitrary numbers (possibly in different positions) does not lead to two identical sequences of length 4."

So we pick two numbers from our set (they could be the same number or different numbers - "two arbitrary numbers"), delete one digit from each (the positions can be different), and the resulting two 4-digit sequences must not be identical.

If the two numbers are the same number, then deleting a digit at position i and deleting a digit at position j (i≠j) from the same number should give different 4-sequences. Actually if i=j, we'd get the same sequence trivially, so I think "possibly in different positions" means the deletion positions can be different, and we need to consider all pairs of deletions.

Hmm, but if we pick the same number twice and delete at the same position, we get identical sequences. So "two arbitrary numbers" must mean two distinct numbers. Let me reconsider.

Actually, I think "two arbitrary numbers" means two (possibly different) numbers from the set. If they're the same number, deleting at the same position gives the same 4-sequence, which would violate the condition. So the condition must apply to distinct numbers, OR the condition applies to all pairs including same number but different deletion positions.

Let me re-read more carefully: "deleting any digit in two arbitrary numbers (possibly in different positions) does not lead to two identical sequences of length 4."

I think this means: take any two numbers from the set (distinct), delete any one digit from the first (at any position) and any one digit from the second (at any position, possibly different from the first's deletion position). The two resulting 4-sequences must be different.

So the condition is: for any two distinct numbers A, B in the set, the set of 4-sequences obtained by deleting one digit from A and the set of 4-sequences obtained by deleting one digit from B are disjoint.

Wait, but it says "does not lead to two identical sequences" - so for any choice of deletion position in A and any choice of deletion position in B, the results are different. That means the two sets of 4-sequences (from A and from B) are disjoint.

Actually, let me reconsider whether it includes the same number. If A = B, then deleting at position i from both gives the same 4-sequence, which violates the condition. So if the condition applies to the same number, no number can be in the set. That doesn't make sense. So the condition must apply to distinct numbers only.

Hmm, but actually "two arbitrary numbers" typically means two numbers that could be any two, possibly the same. But as I noted, if they're the same, deleting at the same position gives identical sequences. So the condition must be about distinct numbers.

Let me formalize: Let S be our set of 5-digit numbers. For each number x in S, let D(x) = {4-sequences obtained by deleting one digit from x}. The condition is: for any distinct x, y in S, D(x) ∩ D(y) = ∅.

We want to maximize |S| subject to:
- Each x in S uses at most 2 distinct digits
- For distinct x, y in S: D(x) ∩ D(y) = ∅

First, let me count the total number of 5-digit sequences using at most 2 distinct digits.

Digits are 0-9 (10 digits). A 5-digit sequence using at most 2 distinct digits:
- Using exactly 1 digit: 10 choices (00000, 11111, ..., 99999)
- Using exactly 2 digits: C(10,2) * (2^5 - 2) = 45 * 30 = 1350

Total = 10 + 1350 = 1360.

Now, each such number generates a set D(x) of at most 5 four-sequences (deleting each of the 5 positions; some may coincide).

The total number of 4-digit sequences is 10^4 = 10000. Each number x uses at most 5 of these (from D(x)), and the D(x) sets must be pairwise disjoint. So |S| ≤ 10000 / min|D(x)|.

But we also need each x to use at most 2 distinct digits, and the 4-sequences in D(x) don't need to use at most 2 digits (they're just 4-sequences).

Wait, but the constraint is that the 4-sequences from different numbers must be disjoint. The total pool of 4-sequences is 10000. If each number uses exactly 5 distinct 4-sequences, then |S| ≤ 10000/5 = 2000. But we only have 1360 candidate numbers, so the bound is at most 1360.

But can we achieve 1360? That would require all D(x) sets to be pairwise disjoint. Let's check: total 4-sequences used = sum of |D(x)| over all x. If all are disjoint, this sum ≤ 10000. With 1360 numbers, if each uses 5, that's 6800 ≤ 10000, so it's possible in principle. But some numbers use fewer than 5 (when deleting different positions gives the same 4-sequence).

Actually, let me think about when D(x) has fewer than 5 elements. If x = aaaaa (all same digit), then deleting any position gives aaaa, so |D(x)| = 1. If x = aaaab (four a's and one b), then deleting the b gives aaaa, and deleting any a gives aaab (with b in different positions: positions 1,2,3,4 → but wait, the 4-sequence depends on where b ends up).

Let me think more carefully. x = d1 d2 d3 d4 d5. Deleting position i gives the 4-sequence d1...d_{i-1} d_{i+1}...d5.

For x = aaaab (a,a,a,a,b): 
- Delete pos 1: aaab
- Delete pos 2: aaab
- Delete pos 3: aaab
- Delete pos 4: aaab
- Delete pos 5: aaaa

So D(x) = {aaab, aaaa}, |D(x)| = 2.

For x = aaabb (a,a,a,b,b):
- Delete pos 1: aabb
- Delete pos 2: aabb
- Delete pos 3: aabb
- Delete pos 4: aaab
- Delete pos 5: aaab

D(x) = {aabb, aaab}, |D(x)| = 2.

Hmm, so numbers with repeated digits can have small D(x).

For x = ababa (a,b,a,b,a):
- Delete pos 1: baba
- Delete pos 2: aaba
- Delete pos 3: abba
- Delete pos 4: abaa
- Delete pos 5: abab

D(x) = {baba, aaba, abba, abaa, abab}, |D(x)| = 5.

For x = ababc... wait, only 2 digits allowed.

For x = ababa, all 5 deletions give different results, so |D(x)| = 5.

The key question is: what's the maximum size of a set S where each element uses at most 2 digits and the D(x) sets are pairwise disjoint?

Let me think about this differently. The total number of 4-sequences is 10000. We need to partition (or pack) these into groups of size |D(x)|, where each group corresponds to a valid 5-digit number with at most 2 distinct digits.

Actually, we don't need to partition all 10000; we just need to select a subset of 4-sequences and group them.

Let me think about which 4-sequences can be in D(x) for some valid x. A 4-sequence s is in D(x) for some x using at most 2 digits if and only if s uses at most 2 digits (since deleting a digit from a 2-digit number gives a sequence using at most 2 digits). Wait, that's not quite right. If x uses digits {a, b}, then any 4-sequence in D(x) uses only digits from {a, b}, so it uses at most 2 digits.

Conversely, if a 4-sequence s uses at most 2 digits, say {a, b}, then we can insert a or b at any position to get a 5-digit number using at most 2 digits, and s would be in D(x) for that x.

So the 4-sequences that can appear in any D(x) are exactly the 4-sequences using at most 2 distinct digits.

Number of 4-sequences using at most 2 digits:
- 1 digit: 10
- 2 digits: C(10,2) * (2^4 - 2) = 45 * 14 = 630
- Total: 640

So the total pool of usable 4-sequences is 640. Each number x uses |D(x)| of these, and the sets must be disjoint. So |S| ≤ 640 / min|D(x)|.

But min|D(x)| = 1 (for aaaaa). So this bound is weak.

Actually, we need to be more careful. We want to maximize |S|, so we want to use numbers with small |D(x)| to pack more numbers. But we also need the D(x) sets to be disjoint.

Let me think about this as a packing problem. We have 640 available 4-sequences. We want to select a maximum number of 5-digit numbers (each using ≤2 digits) such that their D(x) sets are disjoint subsets of the 640 available 4-sequences.

For a number x using digits {a,b}, D(x) ⊆ {4-sequences using digits from {a,b}}. The set of 4-sequences using digits from {a,b} has size 2^4 = 16 (including those using only a or only b). But we said the usable pool is 640 = 10 + 630, which counts 4-sequences using at most 2 digits. A 4-sequence using only digit a is counted once (in the "1 digit" category), not 9 times (once for each pair {a, b}). So the 4-sequences using digits from {a,b} (allowing 1 or 2 digits) number 16, but the single-digit ones (aaaa, bbbb) are shared across multiple pairs.

This makes the problem more complex because the 4-sequences using a single digit are shared resources.

Let me reconsider. The 4-sequences using at most 2 digits:
- Single digit: aaaa for each a (10 total)
- Two digits {a,b}: all 4-sequences using both a and b, which is 2^4 - 2 = 14 for each pair, total 45 * 14 = 630.

Total: 640.

Now, for a 5-digit number x using digits {a, b} (both used), D(x) consists of 4-sequences using digits from {a, b}. These 4-sequences could use only a, only b, or both. The ones using only a or only b are the "shared" single-digit 4-sequences.

For a 5-digit number x using only digit a, D(x) = {aaaa}, using 1 of the 10 single-digit 4-sequences.

Let me categorize the 5-digit numbers by their digit pattern:
1. All same digit (aaaaa): D(x) = {aaaa}, |D(x)| = 1. There are 10 such numbers.
2. Four of one digit, one of another (e.g., aaaab): D(x) = {aaaa, aaab} (where aaab has b in some position). |D(x)| = 2. Actually let me recheck.

x = aaaab: D(x) = {aaab (delete any of first 4), aaaa (delete last)}. So |D(x)| = 2. The 4-sequences are aaaa (single digit) and aaab (two digits).

But x = aabaa: 
- Delete pos 1: abaa
- Delete pos 2: abaa
- Delete pos 3: aaaa
- Delete pos 4: aaba
- Delete pos 5: aaba

D(x) = {abaa, aaaa, aaba}, |D(x)| = 3.

Hmm, so the size of D(x) depends on the specific pattern, not just the count of each digit.

Let me be more systematic. For a 5-digit number with digits from {a, b}, the 4-sequences in D(x) are obtained by deleting each position. Two deletions give the same 4-sequence iff the deleted digits are the same AND the resulting sequences are the same.

Actually, deleting position i and position j (i < j) give the same 4-sequence iff d_i = d_j and the sequence d_1...d_{i-1} d_{i+1}...d_{j-1} d_{j+1}...d_5 is the same as d_1...d_{i-1} d_{i+1}...d_{j-1} d_{j+1}...d_5, which is always true if d_i = d_j (since we're just removing one occurrence of the same digit from two different positions, and the remaining sequence is the same).

Wait, that's not right. Let me think again. If we delete position i, we get d_1...d_{i-1} d_{i+1}...d_5. If we delete position j (j > i), we get d_1...d_{j-1} d_{j+1}...d_5. These are the same iff d_{i+1}...d_5 (with position i removed) equals d_1...d_{j-1} d_{j+1}...d_5 (with position j removed).

Hmm, let me think of it differently. Deleting position i gives a 4-sequence. Deleting positions i and j give the same 4-sequence iff d_i = d_j and for all k between i and j, d_k = d_{k+1}... no, that's not right either.

Let me just think concretely. The 4-sequence from deleting position i is:
s_i = d_1 d_2 ... d_{i-1} d_{i+1} ... d_5

s_i = s_j (for i < j) iff:
d_1...d_{i-1} d_{i+1}...d_j ... d_5 = d_1...d_i ... d_{j-1} d_{j+1}...d_5

The first i-1 positions are the same. Then position i of s_i is d_{i+1} and position i of s_j is d_i. So we need d_{i+1} = d_i. Then position i+1 of s_i is d_{i+2} and position i+1 of s_j is d_{i+1} = d_i = d_{i+1}. So we need d_{i+2} = d_{i+1}. Continuing, we need d_{i+1} = d_{i+2} = ... = d_j. And also d_i = d_{i+1} (from the first condition). So d_i = d_{i+1} = ... = d_j, i.e., all digits from position i to j are the same.

So s_i = s_j (for i < j) iff d_i = d_{i+1} = ... = d_j (all digits in positions i through j are the same).

This means: the number of distinct 4-sequences in D(x) equals the number of "runs" in x. A run is a maximal block of consecutive identical digits.

For example:
- aaaaa: 1 run → |D(x)| = 1
- aaaab: 2 runs → |D(x)| = 2
- aabaa: 3 runs (aa, b, aa) → |D(x)| = 3
- ababa: 5 runs → |D(x)| = 5
- aabba: 3 runs (aa, bb, a) → |D(x)| = 3
- abbaa: 3 runs (a, bb, aa) → |D(x)| = 3

So |D(x)| = number of runs in x.

Now, the problem is to select a maximum set S of 5-digit numbers (each using ≤ 2 distinct digits) such that the D(x) sets are pairwise disjoint.

The total pool of 4-sequences using ≤ 2 digits is 640. Each number x uses (number of runs) 4-sequences. We want to maximize the count of numbers while keeping the D(x) sets disjoint.

To maximize |S|, we want to use numbers with as few runs as possible (to use fewer 4-sequences per number). But we also need the D(x) sets to be disjoint.

Numbers with 1 run: aaaaa (10 numbers), each using 1 four-sequence (aaaa). These 10 four-sequences are all distinct, so we can include all 10. That uses 10 four-sequences.

Numbers with 2 runs: e.g., aaaab, baaaa, aabbb, bbbaa, etc. Each uses 2 four-sequences. The 4-sequences used are: one single-digit (aaaa or bbbb) and one two-digit.

Wait, let me check. x = aaaab: D(x) = {aaaa, aaab}. So it uses aaaa (single digit a) and aaab (two digits {a,b}).

x = baaaa: D(x) = {aaaa, baaa}. Uses aaaa and baaa.

x = aabbb: D(x) = {abbb, aabb}. Let me verify:
- Delete pos 1: abbb
- Delete pos 2: abbb
- Delete pos 3: abbb... wait no.

x = aabbb = a,a,b,b,b:
- Delete pos 1: abbb
- Delete pos 2: abbb
- Delete pos 3: aabb
- Delete pos 4: aabb
- Delete pos 5: aabb

D(x) = {abbb, aabb}, |D(x)| = 2. Both are two-digit 4-sequences.

x = bbbaa = b,b,b,a,a:
- Delete pos 1: bbaa
- Delete pos 2: bbaa
- Delete pos 3: bbaa
- Delete pos 4: bbba
- Delete pos 5: bbba

D(x) = {bbaa, bbba}, |D(x)| = 2.

So for 2-run numbers, the D(x) set depends on the structure. If the run lengths are (k, 5-k) for digit a then digit b (or vice versa), the 4-sequences are:
- If we delete from the first run (length k): we get a sequence with (k-1) a's and (5-k) b's
- If we delete from the second run (length 5-k): we get a sequence with k a's and (5-k-1) b's

So D(x) = {4-sequence with (k-1) a's followed by (5-k) b's, 4-sequence with k a's followed by (5-k-1) b's}.

For x = aaaab (k=4 a's, 1 b): D(x) = {aaa b, aaaa} = {aaab, aaaa}. The first has 3 a's and 1 b, the second has 4 a's.

For x = aabbb (k=2 a's, 3 b's): D(x) = {abbb, aabb}. First has 1 a and 3 b's, second has 2 a's and 2 b's.

For x = abbbb (k=1 a, 4 b's): D(x) = {bbbb, abbb}. First has 4 b's, second has 1 a and 3 b's.

So for 2-run numbers with digits {a,b} and run lengths (k, 5-k):
- If k=1: D(x) = {bbbb, abbb} (or {aaaa, baaa} if b is first)
- If k=2: D(x) = {abbb, aabb} (or {baaa, bbaa} if b is first)
- If k=3: D(x) = {aabb, aaab} (or {bbaa, bbba} if b is first)
- If k=4: D(x) = {aaab, aaaa} (or {bbba, bbbb} if b is first)

Now, the single-digit 4-sequences (aaaa, bbbb, etc.) are scarce resources (only 10 of them). Each is used by:
- The 1-run number aaaaa (uses aaaa)
- The 2-run numbers aaaab and aaaac (for any c ≠ a) — wait, aaaab uses aaaa, and so does aabaa? No, aabaa has 3 runs.

Let me reconsider. Which numbers use the 4-sequence aaaa in their D(x)?
- aaaaa (1 run): D = {aaaa}
- aaaab (2 runs, k=4): D = {aaab, aaaa}
- baaaa (2 runs, k=1 for b, so 4 a's): D = {aaaa, baaa}

So aaaa is used by aaaaa, aaaab, baaaa, and also by any number where deleting a digit gives aaaa. That means the original number has 4 a's and 1 other digit, and the other digit is deleted. So the numbers are: aaaab (delete b), aabaa... no wait, aabaa deleting position 3 gives aaaa. Let me check: aabaa, delete pos 3: aaaa. Yes! So aabaa also uses aaaa.

Hmm wait, aabaa has 3 runs (aa, b, aa), so |D(aabaa)| = 3, and one of its 4-sequences is aaaa.

So aaaa is used by many numbers: any 5-digit number with exactly 4 a's and 1 non-a digit. There are 9 * 5 = 45 such numbers (9 choices for the other digit, 5 positions for it). Plus aaaaa itself.

So aaaa is a very contested resource. Since D(x) sets must be disjoint, at most one number can use aaaa in its D(x).

This means: among all numbers that have aaaa in their D(x), we can pick at most one.

Similarly for each single-digit 4-sequence.

Let me think about the structure more carefully. The 4-sequences using at most 2 digits are:
- 10 single-digit ones: aaaa for a = 0..9
- 630 two-digit ones: for each pair {a,b}, 14 sequences using both a and b

For a pair {a, b}, the 14 two-digit 4-sequences are all sequences of length 4 using both a and b. These can be categorized by the number of a's: 1 a + 3 b's (4 sequences), 2 a's + 2 b's (6 sequences), 3 a's + 1 b (4 sequences). Total: 4 + 6 + 4 = 14.

Now, for each pair {a, b}, the 4-sequences involving only a and b are: aaaa, bbbb, and the 14 two-digit ones. Total 16.

But aaaa and bbbb are shared with other pairs.

Let me think about this problem pair by pair. For a fixed pair {a, b}, the 4-sequences that can appear in D(x) for numbers using only digits a and b are the 16 sequences: aaaa, bbbb, and 14 two-digit ones.

But aaaa is also usable by numbers involving {a, c} for any c, and bbbb by numbers involving {b, c}.

The constraint is that the D(x) sets are globally disjoint. So if a number using {a, b} claims aaaa, no other number (using any digit pair) can claim aaaa.

This is a complex optimization problem. Let me think about it differently.

Key insight: The single-digit 4-sequences (aaaa for each a) are the bottleneck. There are 10 of them, and each can be used by at most one number. Numbers that use a single-digit 4-sequence in their D(x) are:
- 1-run numbers: aaaaa uses aaaa
- 2-run numbers with run lengths (4,1) or (1,4): these use one single-digit and one two-digit 4-sequence
- 3-run numbers where one run has length 1 and the other two runs are of the same digit: e.g., aabaa uses aaaa

Actually, let me reconsider. A number uses aaaa in its D(x) iff deleting some digit gives aaaa, which means the number has 4 a's and 1 other digit. So the number uses digits {a, b} for some b, and has the pattern with 4 a's and 1 b.

The patterns with 4 a's and 1 b are: baaaa, abaaa, aabaa, aaaba, aaaab. These have 2, 3, 3, 3, 2 runs respectively.

Wait: baaaa = b,a,a,a,a → runs: (b)(aaaa) = 2 runs. D = {aaaa, baaa}.
abaaa = a,b,a,a,a → runs: (a)(b)(aaa) = 3 runs. D = {baaa, aaaa, abaa}... let me compute.

abaaa:
- Delete pos 1: baaa
- Delete pos 2: aaaa
- Delete pos 3: abaa
- Delete pos 4: abaa
- Delete pos 5: abaa

D = {baaa, aaaa, abaa}, |D| = 3.

aabaa:
- Delete pos 1: abaa
- Delete pos 2: abaa
- Delete pos 3: aaaa
- Delete pos 4: aaba
- Delete pos 5: aaba

D = {abaa, aaaa, aaba}, |D| = 3.

aaaba:
- Delete pos 1: aaba
- Delete pos 2: aaba
- Delete pos 3: aaba
- Delete pos 4: aaaa
- Delete pos 5: aaab

D = {aaba, aaaa, aaab}, |D| = 3.

aaaab:
- Delete pos 1: aaab
- Delete pos 2: aaab
- Delete pos 3: aaab
- Delete pos 4: aaab
- Delete pos 5: aaaa

D = {aaab, aaaa}, |D| = 2.

So for numbers with 4 a's and 1 b:
- baaaa (2 runs): D = {aaaa, baaa}
- abaaa (3 runs): D = {baaa, aaaa, abaa}
- aabaa (3 runs): D = {abaa, aaaa, aaba}
- aaaba (3 runs): D = {aaba, aaaa, aaab}
- aaaab (2 runs): D = {aaab, aaaa}

Each of these uses aaaa. So at most one of these (plus aaaaa) can be in our set, for each digit a.

Now, let me think about the overall strategy. We have 640 four-sequences. We want to pack as many 5-digit numbers as possible, each using some of these 4-sequences, with disjoint D(x) sets.

To maximize the count, we want numbers with small |D(x)|, i.e., few runs. The minimum is 1 run (|D|=1), but there are only 10 such numbers (aaaaa for each a), and they use the 10 single-digit 4-sequences.

Next best is 2 runs (|D|=2). How many 2-run numbers are there? For each pair {a, b} and each split (k, 5-k) with 1 ≤ k ≤ 4, there are 2 numbers (a^k b^{5-k} and b^k a^{5-k}). So for each pair, 8 numbers. Total: 45 * 8 = 360.

But 2-run numbers use single-digit 4-sequences when k=1 or k=4. Specifically:
- k=1: a bbbb → D = {bbbb, abbb} (uses bbbb)
- k=4: aaaa b → D = {aaab, aaaa} (uses aaaa)
- k=2: aa bbb → D = {abbb, aabb} (uses only two-digit 4-sequences)
- k=3: aaa bb → D = {aabb, aaab} (uses only two-digit 4-sequences)

So 2-run numbers with k=2 or k=3 don't use any single-digit 4-sequences. Their D(x) sets consist entirely of two-digit 4-sequences.

For each pair {a, b}, the 2-run numbers with k=2 and k=3 are:
- aabbb: D = {abbb, aabb}
- bbbaa: D = {bbaa, bbba}
- aaabb: D = {aabb, aaab}
- bbbaa... wait, let me redo this.

For pair {a, b}, the 2-run numbers are:
- a bbbb (k=1): D = {bbbb, abbb}
- aa bbb (k=2): D = {abbb, aabb}
- aaa bb (k=3): D = {aabb, aaab}
- aaaa b (k=4): D = {aaab, aaaa}
- b aaaa (k=1): D = {aaaa, baaa}
- bb aaa (k=2): D = {baaa, bbaa}
- bbb aa (k=3): D = {bbaa, bbba}
- bbbb a (k=4): D = {bbba, bbbb}

The 4-sequences used (two-digit only) for this pair are:
abbb, aabb, aaab (from a-side runs)
baaa, bbaa, bbba (from b-side runs)

And the single-digit ones: aaaa, bbbb.

Now, for k=2 and k=3 (no single-digit 4-sequences):
- aabbb: D = {abbb, aabb}
- aaabb: D = {aabb, aaab}
- bbaaa: D = {baaa, bbaa}
- bbbaa: D = {bbaa, bbba}

These 4 numbers use the 4-sequences: abbb, aabb, aaab, baaa, bbaa, bbba. That's 6 four-sequences, and the 4 numbers use 2 each = 8, but there are only 6 distinct ones. So they can't all be disjoint!

Let me check: aabbb uses {abbb, aabb}, aaabb uses {aabb, aaab}. These share aabb! So we can't have both aabbb and aaabb.

Similarly, bbaaa uses {baaa, bbaa}, bbbaa uses {bbaa, bbba}. These share bbaa.

So for each pair {a, b}, among the 4 "pure two-digit" 2-run numbers, we can pick at most 2 (one from each side): e.g., aabbb and bbaaa, or aabbb and bbbaa, or aaabb and bbaaa, or aaabb and bbbaa.

Wait, let me check: aabbb uses {abbb, aabb}, bbaaa uses {baaa, bbaa}. These are disjoint! So we can pick both.

aaabb uses {aabb, aaab}, bbbaa uses {bbaa, bbba}. Also disjoint.

aabbb and bbbaa: {abbb, aabb} and {bbaa, bbba}. Disjoint.

aaabb and bbaaa: {aabb, aaab} and {baaa, bbaa}. Disjoint.

So we can pick 2 out of 4 for each pair, using 4 four-sequences per pair. But can we pick more by also using the k=1 and k=4 numbers (which use single-digit 4-sequences)?

The k=1 and k=4 numbers use single-digit 4-sequences (aaaa or bbbb), which are shared across pairs. So using them consumes a scarce resource.

Let me think about the global optimization. We have:
- 10 single-digit 4-sequences (aaaa for each a)
- For each pair {a,b}, 14 two-digit 4-sequences

For each pair {a,b}, the two-digit 4-sequences are:
- 1a3b: abbb, babb, bbab, bbba (4 sequences)
- 2a2b: aabb, abab, abba, baab, baba, bbaa (6 sequences)
- 3a1b: aaab, aaba, abaa, baaa (4 sequences)

The 2-run numbers for pair {a,b} use:
- k=1 (a bbbb): {bbbb, abbb}
- k=2 (aa bbb): {abbb, aabb}
- k=3 (aaa bb): {aabb, aaab}
- k=4 (aaaa b): {aaab, aaaa}
- k=1 (b aaaa): {aaaa, baaa}
- k=2 (bb aaa): {baaa, bbaa}
- k=3 (bbb aa): {bbaa, bbba}
- k=4 (bbbb a): {bbba, bbbb}

The two-digit 4-sequences used by 2-run numbers are: abbb, aabb, aaab, baaa, bbaa, bbba. These are 6 out of 14. The other 8 two-digit 4-sequences (babb, bbab, abab, abba, baab, baba, aaba, abaa) are not used by any 2-run number. They would be used by 3-run, 4-run, or 5-run numbers.

Now, for 3-run numbers, |D(x)| = 3, so they use 3 four-sequences each. For 4-run numbers, |D(x)| = 4. For 5-run numbers, |D(x)| = 5.

To maximize the count, we want to use numbers with fewer runs. But we also need to efficiently use the 4-sequence pool.

Let me think about this as follows. For each pair {a, b}, we have 16 four-sequences (aaaa, bbbb, and 14 two-digit). We want to pack 5-digit numbers (using only a and b) into these 16 four-sequences, with each number using (number of runs) four-sequences.

But the single-digit four-sequences are shared across pairs. So let me separate the problem.

Let me first handle the single-digit four-sequences. There are 10 of them. Each can be used by at most one number. The numbers that use a single-digit four-sequence are:
- 1-run: aaaaa uses aaaa (1 four-sequence)
- 2-run with k=1 or k=4: uses 1 single-digit + 1 two-digit
- 3-run with a run of length 1 in the middle: e.g., aabaa uses aaaa + 2 two-digit
- etc.

If we use aaaaa, we get 1 number for 1 four-sequence (aaaa). If we use aaaab (2-run, k=4), we get 1 number for 2 four-sequences (aaaa + aaab). If we use aabaa (3-run), we get 1 number for 3 four-sequences (aaaa + abaa + aaba).

Using aaaaa is the most efficient for the single-digit four-sequences (1 number per 1 four-sequence). But it doesn't use any two-digit four-sequences, so it doesn't help with the bulk of the pool.

Let me think about the two-digit four-sequences. For each pair {a, b}, there are 14 two-digit four-sequences. The 2-run numbers (k=2, k=3) use 2 two-digit four-sequences each, and we can fit 2 per pair (as shown above), using 4 two-digit four-sequences per pair. But we have 14 per pair, so there are 10 unused two-digit four-sequences per pair.

Can we use 3-run numbers to fill in? A 3-run number uses 3 four-sequences. Some of these might be two-digit, some might be single-digit.

Let me enumerate 3-run numbers for pair {a, b}. A 3-run number has pattern: a^i b^j a^k or b^i a^j b^k, where i+j+k = 5, i,j,k ≥ 1.

For a^i b^j a^k:
- i=1, j=1, k=3: abaaa → D = {baaa, aaaa, abaa}. Uses aaaa (single) + baaa, abaa (two-digit).
- i=1, j=2, k=2: abbaa → D = {bbaa, abaa, abba}. Let me verify.

abbaa = a,b,b,a,a:
- Delete pos 1: bbaa
- Delete pos 2: abaa
- Delete pos 3: abaa... wait:
  - Delete pos 1: b,b,a,a = bbaa
  - Delete pos 2: a,b,a,a = abaa
  - Delete pos 3: a,b,a,a = abaa
  - Delete pos 4: a,b,b,a = abba
  - Delete pos 5: a,b,b,a = abba

D = {bbaa, abaa, abba}, |D| = 3. All two-digit!

- i=1, j=3, k=1: abbba → 
  - Delete pos 1: bbba
  - Delete pos 2: abba
  - Delete pos 3: abba
  - Delete pos 4: abba
  - Delete pos 5: abbb

D = {bbba, abba, abbb}, |D| = 3. All two-digit!

- i=2, j=1, k=2: aabaa → D = {abaa, aaaa, aaba}. Uses aaaa (single) + abaa, aaba (two-digit).

- i=2, j=2, k=1: aabba →
  - Delete pos 1: abba
  - Delete pos 2: abba
  - Delete pos 3: aaba
  - Delete pos 4: aaba
  - Delete pos 5: aabb

D = {abba, aaba, aabb}, |D| = 3. All two-digit!

- i=3, j=1, k=1: aaaba → D = {aaba, aaaa, aaab}. Uses aaaa + aaba, aaab.

By symmetry, for b^i a^j b^k, we get similar patterns with a and b swapped.

So the 3-run numbers that don't use single-digit four-sequences are:
- abbaa: D = {bbaa, abaa, abba}
- abbba: D = {bbba, abba, abbb}
- aabba: D = {abba, aaba, aabb}
- baabb: D = {aabb, baa b... let me compute}

baabb = b,a,a,b,b:
- Delete pos 1: aabb
- Delete pos 2: babb
- Delete pos 3: babb
- Delete pos 4: baab
- Delete pos 5: baab

D = {aabb, babb, baab}, |D| = 3. All two-digit!

bbaab = b,b,a,a,b:
- Delete pos 1: baab
- Delete pos 2: baab
- Delete pos 3: bbab
- Delete pos 4: bbab
- Delete pos 5: bbaa

D = {baab, bbab, bbaa}, |D| = 3. All two-digit!

bbabb = b,b,a,b,b:
- Delete pos 1: babb
- Delete pos 2: babb
- Delete pos 3: bbab... wait:
  - Delete pos 1: b,a,b,b = babb
  - Delete pos 2: b,a,b,b = babb
  - Delete pos 3: b,b,b,b = bbbb. 

Oh wait, bbabb = b,b,a,b,b. Delete pos 3 (the a): b,b,b,b = bbbb. That's a single-digit four-sequence!

Let me recompute:
- Delete pos 1: b,a,b,b = babb
- Delete pos 2: b,a,b,b = babb
- Delete pos 3: b,b,b,b = bbbb
- Delete pos 4: b,b,a,b = bbab
- Delete pos 5: b,b,a,b = bbab

D = {babb, bbbb, bbab}, |D| = 3. Uses bbbb (single-digit).

So bbabb uses bbbb. This is because the middle run has length 1, and deleting it gives all b's.

So 3-run numbers with the middle run of length 1 use a single-digit four-sequence. 3-run numbers with the middle run of length ≥ 2 don't.

Let me list all 3-run numbers for pair {a, b} with middle run ≥ 2 (no single-digit four-sequences):

Pattern a^i b^j a^k with j ≥ 2:
- i=1, j=2, k=2: abbaa → D = {bbaa, abaa, abba}
- i=1, j=3, k=1: abbba → D = {bbba, abba, abbb}
- i=2, j=2, k=1: aabba → D = {abba, aaba, aabb}

Pattern b^i a^j b^k with j ≥ 2:
- i=1, j=2, k=2: baabb → D = {aabb, babb, baab}
- i=1, j=3, k=1: baaab → D = {aaab, baab, baaa}
- i=2, j=2, k=1: bbaab → D = {baab, bbab, bbaa}

So 6 three-run numbers per pair that don't use single-digit four-sequences, each using 3 two-digit four-sequences.

The two-digit four-sequences used by these 6 numbers:
- abbaa: {bbaa, abaa, abba}
- abbba: {bbba, abba, abbb}
- aabba: {abba, aaba, aabb}
- baabb: {aabb, babb, baab}
- baaab: {aaab, baab, baaa}
- bbaab: {baab, bbab, bbaa}

Let me list all 14 two-digit four-sequences for pair {a, b}:
1a3b: abbb, babb, bbab, bbba
2a2b: aabb, abab, abba, baab, baba, bbaa
3a1b: aaab, aaba, abaa, baaa

Now, the 2-run numbers (k=2, k=3) use:
- aabbb: {abbb, aabb}
- aaabb: {aabb, aaab}
- bbaaa: {baaa, bbaa}
- bbbaa: {bbaa, bbba}

The 3-run numbers (middle ≥ 2) use:
- abbaa: {bbaa, abaa, abba}
- abbba: {bbba, abba, abbb}
- aabba: {abba, aaba, aabb}
- baabb: {aabb, babb, baab}
- baaab: {aaab, baab, baaa}
- bbaab: {baab, bbab, bbaa}

The two-digit four-sequences not used by any 2-run or 3-run (middle ≥ 2) number:
From 1a3b: abbb (used by aabbb, abbba), babb (used by baabb), bbab (used by bbaab), bbba (used by bbbaa, abbba). All used.
From 2a2b: aabb (used by many), abab (not used!), abba (used by many), baab (used by many), baba (not used!), bbaa (used by many). So abab and baba are not used.
From 3a1b: aaab (used by aaabb, baaab), aaba (used by aabba), abaa (used by abbaa), baaa (used by bbaaa, baaab). All used.

So abab and baba are only used by 4-run and 5-run numbers.

Let me check 4-run numbers. A 4-run number for pair {a, b} has pattern like abab a, ababa, etc.

ababa = a,b,a,b,a (5 runs, not 4). Let me think about 4-run patterns.

4-run patterns with 2 digits and length 5: the runs alternate, so with 4 runs, the pattern is a^i b^j a^k b^l or b^i a^j b^k a^l with i+j+k+l = 5, all ≥ 1.

Possible (i,j,k,l) with sum 5, all ≥ 1:
(1,1,1,2), (1,1,2,1), (1,2,1,1), (2,1,1,1)

For a^1 b^1 a^1 b^2 = ababb:
- Delete pos 1: babb
- Delete pos 2: aabb
- Delete pos 3: abbb... wait:
  ababb = a,b,a,b,b
  - Delete pos 1: b,a,b,b = babb
  - Delete pos 2: a,a,b,b = aabb
  - Delete pos 3: a,b,b,b = abbb... no: a,b,b,b. Wait, delete pos 3 from a,b,a,b,b: a,b,b,b = abbb.
  - Delete pos 4: a,b,a,b = abab
  - Delete pos 5: a,b,a,b = abab

D = {babb, aabb, abbb, abab}, |D| = 4. Uses abab!

For a^1 b^1 a^2 b^1 = ab aab = abaab:
  abaab = a,b,a,a,b
  - Delete pos 1: b,a,a,b = baab
  - Delete pos 2: a,a,a,b = aaab
  - Delete pos 3: a,b,a,b = abab
  - Delete pos 4: a,b,a,b = abab
  - Delete pos 5: a,b,a,a = abaa

D = {baab, aaab, abab, abaa}, |D| = 4. Uses abab!

For a^1 b^2 a^1 b^1 = abba b = abbab:
  abbab = a,b,b,a,b
  - Delete pos 1: b,b,a,b = bbab
  - Delete pos 2: a,b,a,b = abab
  - Delete pos 3: a,b,a,b = abab
  - Delete pos 4: a,b,b,b = abbb
  - Delete pos 5: a,b,b,a = abba

D = {bbab, abab, abbb, abba}, |D| = 4. Uses abab!

For a^2 b^1 a^1 b^1 = aabab:
  aabab = a,a,b,a,b
  - Delete pos 1: a,b,a,b = abab
  - Delete pos 2: a,b,a,b = abab
  - Delete pos 3: a,a,a,b = aaab
  - Delete pos 4: a,a,b,b = aabb
  - Delete pos 5: a,a,b,a = aaba

D = {abab, aaab, aabb, aaba}, |D| = 4. Uses abab!

By symmetry, the b^i a^j b^k a^l patterns will use baba.

So 4-run numbers use 4 four-sequences each, including abab or baba.

5-run numbers: ababa or babab. 
ababa = a,b,a,b,a:
- Delete pos 1: b,a,b,a = baba
- Delete pos 2: a,a,b,a = aaba
- Delete pos 3: a,b,b,a = abba
- Delete pos 4: a,b,a,a = abaa
- Delete pos 5: a,b,a,b = abab

D = {baba, aaba, abba, abaa, abab}, |D| = 5. Uses both abab and baba!

babab = b,a,b,a,b:
- Delete pos 1: a,b,a,b = abab
- Delete pos 2: b,b,a,b = bbab
- Delete pos 3: b,a,a,b = baab
- Delete pos 4: b,a,b,b = babb
- Delete pos 5: b,a,b,a = baba

D = {abab, bbab, baab, babb, baba}, |D| = 5.

OK so now I have a complete picture. Let me think about the optimization.

For each pair {a, b}, the 14 two-digit four-sequences are:
1a3b: abbb, babb, bbab, bbba
2a2b: aabb, abab, abba, baab, baba, bbaa
3a1b: aaab, aaba, abaa, baaa

The numbers and their D(x) sets (only two-digit four-sequences):

2-run (k=2,3): 4 numbers, each using 2 four-sequences:
- aabbb: {abbb, aabb}
- aaabb: {aabb, aaab}
- bbaaa: {baaa, bbaa}
- bbbaa: {bbaa, bbba}

3-run (middle ≥ 2): 6 numbers, each using 3 four-sequences:
- abbaa: {bbaa, abaa, abba}
- abbba: {bbba, abba, abbb}
- aabba: {abba, aaba, aabb}
- baabb: {aabb, babb, baab}
- baaab: {aaab, baab, baaa}
- bbaab: {baab, bbab, bbaa}

4-run: 8 numbers, each using 4 four-sequences:
- ababb: {babb, aabb, abbb, abab}
- abaab: {baab, aaab, abab, abaa}
- abbab: {bbab, abab, abbb, abba}
- aabab: {abab, aaab, aabb, aaba}
- babaa: {abaa, bbaa, baba, baaa} (by symmetry with abaab, swapping a,b)
- baaba: {aaba, bbba, abab... wait let me compute}

Actually, let me be more careful. The 4-run numbers with pattern a^i b^j a^k b^l:

(1,1,1,2): ababb → D = {babb, aabb, abbb, abab}
(1,1,2,1): abaab → D = {baab, aaab, abab, abaa}
(1,2,1,1): abbab → D = {bbab, abab, abbb, abba}
(2,1,1,1): aabab → D = {abab, aaab, aabb, aaba}

And with pattern b^i a^j b^k a^l:
(1,1,1,2): babba → D = {abba, bbaa, baaa, baba}... let me compute.
babba = b,a,b,b,a:
- Delete pos 1: a,b,b,a = abba
- Delete pos 2: b,b,b,a = bbba... wait: b,b,b,a. Hmm, that's bbba. But bbba is a 1a3b sequence (3 b's and 1 a). Let me recheck.

babba = b,a,b,b,a
- Delete pos 1: a,b,b,a = abba
- Delete pos 2: b,b,b,a = bbba
- Delete pos 3: b,a,b,a = baba
- Delete pos 4: b,a,b,a = baba
- Delete pos 5: b,a,b,b = babb

D = {abba, bbba, baba, babb}, |D| = 4.

(1,1,2,1): baaba = b,a,a,b,a:
- Delete pos 1: a,a,b,a = aaba
- Delete pos 2: b,a,b,a = baba
- Delete pos 3: b,a,b,a = baba
- Delete pos 4: b,a,a,a = baaa
- Delete pos 5: b,a,a,b = baab

D = {aaba, baba, baaa, baab}, |D| = 4.

(1,2,1,1): bbaab... wait, that's 3 runs (bb, aa, b). No: b,b,a,a,b = bbaab has runs (bb)(aa)(b) = 3 runs. That's not 4 runs.

Hmm, I need to be more careful. b^i a^j b^k a^l with i+j+k+l=5, all ≥ 1:
(1,1,1,2): b a b aa = babaa
(1,1,2,1): b a bb a = babba
(1,2,1,1): b aa b a = baaba
(2,1,1,1): bb a b a = bbaba

babaa = b,a,b,a,a:
- Delete pos 1: a,b,a,a = abaa
- Delete pos 2: b,b,a,a = bbaa
- Delete pos 3: b,a,a,a = baaa
- Delete pos 4: b,a,b,a = baba
- Delete pos 5: b,a,b,a = baba

D = {abaa, bbaa, baaa, baba}, |D| = 4.

babba = b,a,b,b,a: computed above, D = {abba, bbba, baba, babb}, |D| = 4.

baaba = b,a,a,b,a: computed above, D = {aaba, baba, baaa, baab}, |D| = 4.

bbaba = b,b,a,b,a:
- Delete pos 1: b,a,b,a = baba
- Delete pos 2: b,a,b,a = baba
- Delete pos 3: b,b,b,a = bbba
- Delete pos 4: b,b,a,a = bbaa
- Delete pos 5: b,b,a,b = bbab

D = {baba, bbba, bbaa, bbab}, |D| = 4.

So the 8 four-run numbers and their D sets:
a-side first:
- ababb: {babb, aabb, abbb, abab}
- abaab: {baab, aaab, abab, abaa}
- abbab: {bbab, abab, abbb, abba}
- aabab: {abab, aaab, aabb, aaba}

b-side first:
- babaa: {abaa, bbaa, baaa, baba}
- babba: {abba, bbba, baba, babb}
- baaba: {aaba, baba, baaa, baab}
- bbaba: {baba, bbba, bbaa, bbab}

5-run numbers:
- ababa: {baba, aaba, abba, abaa, abab}
- babab: {abab, bbab, baab, babb, baba}

Now, the key observation: abab appears in D sets of: ababb, abaab, abbab, aabab, ababa. That's 5 numbers (all a-first 4-run and the a-first 5-run). Similarly, baba appears in: babaa, babba, baaba, bbaba, babab. That's 5 numbers.

Since D sets must be disjoint, at most one number can use abab, and at most one can use baba.

Also, abab and baba each appear in exactly 5 numbers per pair. So for each pair, we can use at most 1 number containing abab and at most 1 containing baba.

Now let me think about the overall optimization for a single pair {a, b}, ignoring single-digit four-sequences for now.

We have 14 two-digit four-sequences. We want to select a maximum number of 5-digit numbers (using only a, b, and no single-digit four-sequences in their D sets) with disjoint D sets.

The available numbers (no single-digit four-sequences):
- 2-run (k=2,3): 4 numbers, |D|=2
- 3-run (middle ≥ 2): 6 numbers, |D|=3
- 4-run: 8 numbers, |D|=4
- 5-run: 2 numbers, |D|=5

Total: 20 numbers.

But their D sets overlap, and the total four-sequences available is 14.

If we could perfectly partition 14 four-sequences into D sets, we'd want to maximize the count. With |D|=2 numbers, we could fit at most 7. But can we find 7 disjoint D sets of size 2?

The 2-run D sets are:
- aabbb: {abbb, aabb}
- aaabb: {aabb, aaab}
- bbaaa: {baaa, bbaa}
- bbbaa: {bbaa, bbba}

These overlap: aabbb and aaabb share aabb; bbaaa and bbbaa share bbaa. So at most 2 of these 4 can be chosen (one from each pair): e.g., aabbb and bbaaa, using {abbb, aabb, baaa, bbaa}.

Can we add more 2-run-like sets? There are only 4 two-run numbers, so at most 2.

After choosing 2 two-run numbers (using 4 four-sequences), we have 10 four-sequences left. Can we add 3-run numbers (|D|=3)?

Let me try to find a maximum packing for a single pair.

Let me label the 14 four-sequences:
1: abbb, 2: babb, 3: bbab, 4: bbba (1a3b)
5: aabb, 6: abab, 7: abba, 8: baab, 9: baba, 10: bbaa (2a2b)
11: aaab, 12: aaba, 13: abaa, 14: baaa (3a1b)

2-run D sets:
- aabbb: {1, 5}
- aaabb: {5, 11}
- bbaaa: {14, 10}
- bbbaa: {10, 4}

3-run D sets:
- abbaa: {10, 13, 7}
- abbba: {4, 7, 1}
- aabba: {7, 12, 5}
- baabb: {5, 2, 8}
- baaab: {11, 8, 14}
- bbaab: {8, 3, 10}

4-run D sets:
- ababb: {2, 5, 1, 6}
- abaab: {8, 11, 6, 13}
- abbab: {3, 6, 1, 7}
- aabab: {6, 11, 5, 12}
- babaa: {13, 10, 14, 9}
- babba: {7, 4, 9, 2}
- baaba: {12, 9, 14, 8}
- bbaba: {9, 4, 10, 3}

5-run D sets:
- ababa: {9, 12, 7, 13, 6}
- babab: {6, 3, 8, 2, 9}

Now I want to find the maximum number of disjoint D sets from this collection.

This is a set packing problem. Let me try to find a good solution.

First, note that 6 (abab) appears in: ababb, abaab, abbab, aabab, ababa. And 9 (baba) appears in: babaa, babba, baaba, bbaba, babab. These are 5 numbers each, and we can pick at most 1 from each group.

Let me try to maximize the count. With 14 four-sequences, if all D sets have size 2, we could get 7. But we only have 4 size-2 sets, and at most 2 are disjoint. So the max with size-2 is 2, using 4 four-sequences.

Then we have 10 four-sequences left. Can we pack size-3 sets? We have 6 size-3 sets. Let's see which are disjoint from {1, 5, 14, 10} (the choice aabbb + bbaaa).

Available size-3 sets (disjoint from {1, 5, 14, 10}):
- abbaa: {10, 13, 7} — contains 10, not disjoint. ✗
- abbba: {4, 7, 1} — contains 1, not disjoint. ✗
- aabba: {7, 12, 5} — contains 5, not disjoint. ✗
- baabb: {5, 2, 8} — contains 5, not disjoint. ✗
- baaab: {11, 8, 14} — contains 14, not disjoint. ✗
- bbaab: {8, 3, 10} — contains 10, not disjoint. ✗

None of the size-3 sets are disjoint from {1, 5, 14, 10}! That's because the 2-run sets use four-sequences that appear in many 3-run sets.

Let me try a different choice of 2-run sets. Choose aaabb and bbbaa: {5, 11, 10, 4}.

Size-3 sets disjoint from {5, 11, 10, 4}:
- abbaa: {10, 13, 7} — 10, ✗
- abbba: {4, 7, 1} — 4, ✗
- aabba: {7, 12, 5} — 5, ✗
- baabb: {5, 2, 8} — 5, ✗
- baaab: {11, 8, 14} — 11, ✗
- bbaab: {8, 3, 10} — 10, ✗

Same problem. Every 3-run set contains at least one of {5, 11, 10, 4}.

Let me check: the 3-run sets use {1, 4, 5, 7, 8, 10, 11, 12, 13, 14}. The 2-run sets use {1, 4, 5, 10, 11, 14}. So every 3-run set contains at least one element from {1, 4, 5, 10, 11, 14}, which are exactly the elements used by 2-run sets.

Actually, let me check: abbaa = {10, 13, 7}. 10 is in 2-run sets. abbba = {4, 7, 1}. 4 and 1 are in 2-run sets. aabba = {7, 12, 5}. 5 is in 2-run sets. baabb = {5, 2, 8}. 5 is in 2-run sets. baaab = {11, 8, 14}. 11 and 14 are in 2-run sets. bbaab = {8, 3, 10}. 10 is in 2-run sets.

So indeed, every 3-run set intersects every maximal 2-run packing. This means if we use any 2-run numbers, we can't use any 3-run numbers (from the same pair).

What if we don't use any 2-run numbers? Then we can try to pack 3-run numbers.

3-run sets: {10,13,7}, {4,7,1}, {7,12,5}, {5,2,8}, {11,8,14}, {8,3,10}

Can we find disjoint ones? 
- {10,13,7} and {5,2,8} and {11,8,14}: {5,2,8} and {11,8,14} share 8. ✗
- {10,13,7} and {5,2,8}: disjoint! Uses {10,13,7,5,2,8} = 6 four-sequences.
  Can we add more? {4,7,1} shares 7. {7,12,5} shares 7 and 5. {11,8,14} shares 8. {8,3,10} shares 10 and 8. None work.
  So 2 three-run numbers, using 6 four-sequences.

- {4,7,1} and {11,8,14}: disjoint! Uses {4,7,1,11,8,14} = 6.
  Can we add? {10,13,7} shares 7. {7,12,5} shares 7. {5,2,8} shares 8. {8,3,10} shares 8. None.
  So 2 three-run numbers.

- {7,12,5} and {11,8,14} and {8,3,10}: {11,8,14} and {8,3,10} share 8. ✗
- {7,12,5} and {8,3,10}: disjoint! Uses {7,12,5,8,3,10} = 6.
  Can we add? {4,7,1} shares 7. {10,13,7} shares 10 and 7. {5,2,8} shares 5 and 8. {11,8,14} shares 8. None.
  So 2 three-run numbers.

- {4,7,1} and {5,2,8} and {11,8,14}: {5,2,8} and {11,8,14} share 8. ✗
- {4,7,1} and {8,3,10}: disjoint! Uses {4,7,1,8,3,10} = 6.
  Can we add? {5,2,8} shares 8. {11,8,14} shares 8. {7,12,5} shares 7. {10,13,7} shares 10 and 7. None.
  So 2.

Hmm, it seems like we can only get 2 three-run numbers per pair. Let me check if we can get 3.

For 3 disjoint size-3 sets from 14 elements, we need 9 elements. Let me try:
- {10,13,7}, {5,2,8}, {4,...}: {4,7,1} shares 7, {11,8,14} shares 8, {8,3,10} shares 10 and 8. None work.
- {4,7,1}, {5,2,8}, {11,...}: {11,8,14} shares 8, {8,3,10} shares 8. None.
- {4,7,1}, {11,8,14}, {5,...}: {5,2,8} shares 8, {7,12,5} shares 7. None.
- {7,12,5}, {11,8,14}, {4,...}: {4,7,1} shares 7, {10,13,7} shares 7. None.
- {7,12,5}, {8,3,10}, {4,...}: {4,7,1} shares 7, {11,8,14} shares 8. None.

It seems impossible to get 3 disjoint 3-run sets. Let me verify by checking the structure.

The 3-run sets form a graph where edges represent intersection. Let me see:
- abbaa {10,13,7} intersects: abbba(7), aabba(7), bbaab(10)
- abbba {4,7,1} intersects: abbaa(7), aabba(7)
- aabba {7,12,5} intersects: abbaa(7), abbba(7), baabb(5)
- baabb {5,2,8} intersects: aabba(5), baaab(8), bbaab(8)
- baaab {11,8,14} intersects: baabb(8), bbaab(8)
- bbaab {8,3,10} intersects: abbaa(10), baabb(8), baaab(8)

So the intersection graph has the following structure:
abbaa — abbba — aabba — baabb — baaab — bbaab — abbaa (cycle)

It's a cycle of length 6! In a cycle of length 6, the maximum independent set has size 3. But we need disjoint sets, which is stronger than independent (independent means no shared elements, which is exactly what we need).

Wait, in the intersection graph, an independent set means no two sets share an element. So the maximum independent set in a 6-cycle is 3. But I showed above that we can't find 3 disjoint sets. Let me recheck.

A 6-cycle: 1-2-3-4-5-6-1. Maximum independent set: {1,3,5} or {2,4,6}, size 3.

So {abbaa, aabba, baaab} should be independent. Let me check:
- abbaa {10,13,7} and aabba {7,12,5}: share 7! Not independent!

Hmm, so my graph is wrong. Let me redo the intersections.

abbaa {10,13,7}: 
- vs abbba {4,7,1}: share 7 ✓
- vs aabba {7,12,5}: share 7 ✓
- vs baabb {5,2,8}: no share ✗
- vs baaab {11,8,14}: no share ✗
- vs bbaab {8,3,10}: share 10 ✓

abbba {4,7,1}:
- vs aabba {7,12,5}: share 7 ✓
- vs baabb {5,2,8}: no share ✗
- vs baaab {11,8,14}: no share ✗
- vs bbaab {8,3,10}: no share ✗

aabba {7,12,5}:
- vs baabb {5,2,8}: share 5 ✓
- vs baaab {11,8,14}: no share ✗
- vs bbaab {8,3,10}: no share ✗

baabb {5,2,8}:
- vs baaab {11,8,14}: share 8 ✓
- vs bbaab {8,3,10}: share 8 ✓

baaab {11,8,14}:
- vs bbaab {8,3,10}: share 8 ✓

So the intersection graph:
abbaa connects to: abbba, aabba, bbaab
abbba connects to: abbaa, aabba
aabba connects to: abbaa, abbba, baabb
baabb connects to: aabba, baaab, bbaab
baaab connects to: baabb, bbaab
bbaab connects to: abbaa, baabb, baaab

This is not a simple cycle. Let me find the maximum independent set.

Try {abbaa, baabb}: no intersection (abbaa={10,13,7}, baabb={5,2,8}). ✓
Can we add a third? 
- abbba: shares 7 with abbaa ✗
- aabba: shares 7 with abbaa, 5 with baabb ✗
- baaab: shares 8 with baabb ✗
- bbaab: shares 10 with abbaa, 8 with baabb ✗
None. So {abbaa, baabb} is maximal with size 2.

Try {abbba, baabb}: abbba={4,7,1}, baabb={5,2,8}. No intersection. ✓
Add third?
- abbaa: shares 7 with abbba ✗
- aabba: shares 7 with abbba, 5 with baabb ✗
- baaab: shares 8 with baabb ✗
- bbaab: shares 8 with baabb ✗
None. Size 2.

Try {abbba, baaab}: {4,7,1} and {11,8,14}. No intersection. ✓
Add third?
- abbaa: shares 7 with abbba ✗
- aabba: shares 7 with abbba ✗
- baabb: shares 8 with baaab ✗
- bbaab: shares 8 with baaab ✗
None. Size 2.

Try {abbba, bbaab}: {4,7,1} and {8,3,10}. No intersection. ✓
Add third?
- abbaa: shares 7 with abbba, 10 with bbaab ✗
- aabba: shares 7 with abbba ✗
- baabb: shares 8 with bbaab ✗
- baaab: shares 8 with bbaab ✗
None. Size 2.

Try {aabba, baaab}: {7,12,5} and {11,8,14}. No intersection. ✓
Add third?
- abbaa: shares 7 with aabba ✗
- abbba: shares 7 with aabba ✗
- baabb: shares 5 with aabba, 8 with baaab ✗
- bbaab: shares 8 with baaab ✗
None. Size 2.

Try {aabba, bbaab}: {7,12,5} and {8,3,10}. No intersection. ✓
Add third?
- abbaa: shares 7 with aabba, 10 with bbaab ✗
- abbba: shares 7 with aabba ✗
- baabb: shares 5 with aabba, 8 with bbaab ✗
- baaab: shares 8 with bbaab ✗
None. Size 2.

So the maximum independent set in the 3-run intersection graph is 2. We can pick at most 2 three-run numbers per pair.

Now, what about mixing 2-run and 3-run? We showed that every 3-run set intersects every maximal 2-run packing. But what about non-maximal 2-run packings (just 1 two-run number)?

If we pick 1 two-run number, say aabbb {1, 5}, can we add 3-run numbers?
3-run sets disjoint from {1, 5}:
- abbaa {10,13,7}: ✓
- abbba {4,7,1}: shares 1 ✗
- aabba {7,12,5}: shares 5 ✗
- baabb {5,2,8}: shares 5 ✗
- baaab {11,8,14}: ✓
- bbaab {8,3,10}: ✓

So we can pick from {abbaa, baaab, bbaab}. But these three:
- abbaa {10,13,7} and baaab {11,8,14}: disjoint ✓
- abbaa and bbaab {8,3,10}: share 10 ✗
- baaab and bbaab: share 8 ✗

So we can pick abbaa and baaab (both disjoint from aabbb and from each other). That gives us 1 + 2 = 3 numbers using 2 + 3 + 3 = 8 four-sequences.

Can we do better with a different 2-run choice?

Pick aaabb {5, 11}. 3-run sets disjoint from {5, 11}:
- abbaa {10,13,7}: ✓
- abbba {4,7,1}: ✓
- aabba {7,12,5}: shares 5 ✗
- baabb {5,2,8}: shares 5 ✗
- baaab {11,8,14}: shares 11 ✗
- bbaab {8,3,10}: ✓

From {abbaa, abbba, bbaab}:
- abbaa {10,13,7} and abbba {4,7,1}: share 7 ✗
- abbaa and bbaab {8,3,10}: share 10 ✗
- abbba and bbaab: disjoint ✓

So abbba and bbaab, plus aaabb. 3 numbers, 2+3+3 = 8 four-sequences.

Pick bbaaa {14, 10}. 3-run sets disjoint from {14, 10}:
- abbaa {10,13,7}: shares 10 ✗
- abbba {4,7,1}: ✓
- aabba {7,12,5}: ✓
- baabb {5,2,8}: ✓
- baaab {11,8,14}: shares 14 ✗
- bbaab {8,3,10}: shares 10 ✗

From {abbba, aabba, baabb}:
- abbba {4,7,1} and aabba {7,12,5}: share 7 ✗
- abbba and baabb {5,2,8}: disjoint ✓
- aabba and baabb: share 5 ✗

So abbba and baabb, plus bbaaa. 3 numbers, 8 four-sequences.

Pick bbbaa {10, 4}. 3-run sets disjoint from {10, 4}:
- abbaa {10,13,7}: shares 10 ✗
- abbba {4,7,1}: shares 4 ✗
- aabba {7,12,5}: ✓
- baabb {5,2,8}: ✓
- baaab {11,8,14}: ✓
- bbaab {8,3,10}: shares 10 ✗

From {aabba, baabb, baaab}:
- aabba {7,12,5} and baabb {5,2,8}: share 5 ✗
- aabba and baaab {11,8,14}: disjoint ✓
- baabb and baaab: share 8 ✗

So aabba and baaab, plus bbbaa. 3 numbers, 8 four-sequences.

So with 1 two-run + 2 three-run, we get 3 numbers using 8 four-sequences. With 2 two-run + 0 three-run, we get 2 numbers using 4 four-sequences. With 0 two-run + 2 three-run, we get 2 numbers using 6 four-sequences.

Can we do better by including 4-run or 5-run numbers?

Let me try: 1 two-run + 2 three-run + some 4-run. We've used 8 four-sequences, leaving 6. Can we fit a 4-run number (size 4) in the remaining 6?

Example: aabbb {1,5} + abbaa {10,13,7} + baaab {11,8,14}. Used: {1,5,7,8,10,11,13,14}. Remaining: {2,3,4,6,9,12}.

4-run sets using only {2,3,4,6,9,12}:
- ababb {2,5,1,6}: 5 and 1 not available ✗
- abaab {8,11,6,13}: 8,11,13 not available ✗
- abbab {3,6,1,7}: 1,7 not available ✗
- aabab {6,11,5,12}: 11,5 not available ✗
- babaa {13,10,14,9}: 13,10,14 not available ✗
- babba {7,4,9,2}: 7 not available ✗
- baaba {12,9,14,8}: 14,8 not available ✗
- bbaba {9,4,10,3}: 10 not available ✗

None work. What about 5-run?
- ababa {9,12,7,13,6}: 7,13 not available ✗
- babab {6,3,8,2,9}: 8 not available ✗

None.

Let me try a different combination. How about 0 two-run + 2 three-run + 4-run?

abbba {4,7,1} + bbaab {8,3,10}. Used: {1,3,4,7,8,10}. Remaining: {2,5,6,9,11,12,13,14}.

4-run sets using only remaining:
- ababb {2,5,1,6}: 1 not available ✗
- abaab {8,11,6,13}: 8 not available ✗
- abbab {3,6,1,7}: 3,1,7 not available ✗
- aabab {6,11,5,12}: all in remaining ✓! {6,11,5,12} ⊆ {2,5,6,9,11,12,13,14} ✓

So aabab {6,11,5,12} works! Used now: {1,3,4,6,7,8,10,11,12}. Wait, I need to add 5 to the used set. Used: {1,3,4,5,6,7,8,10,11,12}. Remaining: {2,9,13,14}.

Can we add more? 
- 4-run: babaa {13,10,14,9}: 10 not available ✗. baaba {12,9,14,8}: 12,8 not available ✗. bbaba {9,4,10,3}: 4,10,3 not available ✗. babba {7,4,9,2}: 7,4 not available ✗. ababb: 1 not avail ✗. abaab: 8 not avail ✗. abbab: 3,1,7 not avail ✗.
- 5-run: ababa {9,12,7,13,6}: 12,7,6 not avail ✗. babab {6,3,8,2,9}: 6,3,8 not avail ✗.
- 3-run: all already checked or not disjoint.
- 2-run: aabbb {1,5}: 1,5 not avail ✗. aaabb {5,11}: 5,11 not avail ✗. bbaaa {14,10}: 10 not avail ✗. bbbaa {10,4}: 10,4 not avail ✗.

So we have 3 numbers (2 three-run + 1 four-run) using 10 four-sequences. That's worse than 1 two-run + 2 three-run = 3 numbers using 8.

Let me try other combinations.

How about 1 two-run + 1 three-run + 1 four-run?

aabbb {1,5} + abbaa {10,13,7}. Used: {1,5,7,10,13}. Remaining: {2,3,4,6,8,9,11,12,14}.

4-run from remaining:
- ababb {2,5,1,6}: 5,1 not avail ✗
- abaab {8,11,6,13}: 13 not avail ✗
- abbab {3,6,1,7}: 1,7 not avail ✗
- aabab {6,11,5,12}: 5 not avail ✗
- babaa {13,10,14,9}: 13,10 not avail ✗
- babba {7,4,9,2}: 7 not avail ✗
- baaba {12,9,14,8}: all in remaining ✓!
- bbaba {9,4,10,3}: 10 not avail ✗

baaba {12,9,14,8} works! Used: {1,5,7,8,9,10,12,13,14}. Remaining: {2,3,4,6,11}.

Can we add more? 
- 3-run: baaab {11,8,14}: 8,14 not avail ✗. bbaab {8,3,10}: 8,10 not avail ✗. baabb {5,2,8}: 5,8 not avail ✗. aabba {7,12,5}: 7,12,5 not avail ✗. abbba {4,7,1}: 7,1 not avail ✗.
- 2-run: all have 1,5,10,14,4 not avail.
- 4-run: ababb {2,5,1,6}: 5,1 ✗. abaab {8,11,6,13}: 8,13 ✗. abbab {3,6,1,7}: 1,7 ✗. aabab {6,11,5,12}: 5,12 ✗. babaa {13,10,14,9}: all ✗. babba {7,4,9,2}: 7,9 ✗. bbaba {9,4,10,3}: 9,10 ✗.
- 5-run: ababa {9,12,7,13,6}: 9,12,7,13 ✗. babab {6,3,8,2,9}: 8,9 ✗.

So 3 numbers using 9 four-sequences. Still 3 numbers.

Let me try to get 4 numbers. We need 4 disjoint D sets from the 14 four-sequences. The minimum total size is 2+2+2+2=8 (but we can only get 2 disjoint 2-run sets) or 2+2+3+3=10 or 2+3+3+4=12, etc.

With 2 two-run + 2 three-run: we showed 2-run and 3-run can't coexist (for maximal 2-run). But what about 1 two-run + 3 three-run? We showed max 2 three-run with 1 two-run. What about 0 two-run + 3 three-run? We showed max 2 three-run.

What about 2 two-run + 1 four-run? 2 two-run uses 4, 4-run uses 4, total 8. Let's check.

aabbb {1,5} + bbaaa {14,10}. Used: {1,5,10,14}. Remaining: {2,3,4,6,7,8,9,11,12,13}.

4-run from remaining:
- ababb {2,5,1,6}: 5,1 ✗
- abaab {8,11,6,13}: all in remaining ✓!
- abbab {3,6,1,7}: 1 ✗
- aabab {6,11,5,12}: 5 ✗
- babaa {13,10,14,9}: 10,14 ✗
- babba {7,4,9,2}: all in remaining ✓!
- baaba {12,9,14,8}: 14 ✗
- bbaba {9,4,10,3}: 10 ✗

So abaab {8,11,6,13} or babba {7,4,9,2}. Can we add both?
abaab uses {8,11,6,13}, babba uses {7,4,9,2}. Together with {1,5,10,14}: total {1,2,4,5,6,7,8,9,10,11,13,14}. That's 12 four-sequences. Remaining: {3,12}.

Can we add more from {3,12}? No D set has size ≤ 2 using only {3,12} (no 2-run set is {3,12}). So 4 numbers using 12 four-sequences.

Actually wait, can we also fit a 2-run or 3-run in the remaining {3,12}? 
2-run: aabbb{1,5}, aaabb{5,11}, bbaaa{14,10}, bbbaa{10,4}. None use only {3,12}.
3-run: none use only {3,12}.

So 4 numbers: 2 two-run + 2 four-run, using 12 four-sequences. That's 4 numbers per pair!

Can we do 5? We'd need 5 disjoint D sets. Minimum total: 2+2+3+3+4 = 14 (exactly all 14 four-sequences). Or 2+2+2+3+4 = 13, but we can only get 2 disjoint 2-run. Or 2+3+3+3+3 = 14, but we can only get 2 disjoint 3-run. Or 2+2+4+4+4 = 16 > 14, impossible.

So the only possibility for 5 is 2+2+3+3+4 = 14 or 2+3+3+4+4 = 16 (too much) or 2+2+2+4+4 = 14 (but max 2 disjoint 2-run) or 3+3+4+4 = 14 (only 4 numbers) etc.

For 5 numbers with total 14: 2+2+3+3+4 = 14. We need 2 disjoint 2-run, 2 disjoint 3-run (both disjoint from the 2-run), and 1 four-run (disjoint from all).

But we showed that 2-run and 3-run can't coexist! Every 3-run set intersects every maximal 2-run packing. But what about non-maximal? We need 2 two-run sets, which is a maximal 2-run packing. And every 3-run set intersects every maximal 2-run packing. So we can't have 2 two-run + any 3-run.

What about 2+3+3+3+3 = 14? We need 1 two-run + 4 three-run. But max 3-run with 1 two-run is 2. So impossible.

What about 2+2+2+4+4 = 14? We need 3 disjoint 2-run, but max is 2. Impossible.

What about 3+3+4+4 = 14? That's only 4 numbers.

What about 2+4+4+4 = 14? 1 two-run + 3 four-run. Let me check.

aabbb {1,5}. Remaining: {2,3,4,6,7,8,9,10,11,12,13,14}.

4-run sets disjoint from {1,5}:
- abaab {8,11,6,13}: ✓
- babaa {13,10,14,9}: ✓
- babba {7,4,9,2}: ✓
- baaba {12,9,14,8}: ✓
- bbaba {9,4,10,3}: ✓
- ababb {2,5,1,6}: 5,1 ✗
- abbab {3,6,1,7}: 1 ✗
- aabab {6,11,5,12}: 5 ✗

From {abaab, babaa, babba, baaba, bbaba}, can we find 3 disjoint?
- abaab {8,11,6,13} and babba {7,4,9,2}: disjoint ✓. Used: {1,5,8,11,6,13,7,4,9,2}. Remaining: {3,10,12,14}.
  Can we add from {babaa {13,10,14,9}: 13,9 ✗, baaba {12,9,14,8}: 9,8 ✗, bbaba {9,4,10,3}: 9,4 ✗}? None work.

- abaab {8,11,6,13} and baaba {12,9,14,8}: share 8 ✗
- abaab and bbaba {9,4,10,3}: disjoint ✓. Used: {1,5,8,11,6,13,9,4,10,3}. Remaining: {2,7,12,14}.
  Add babaa {13,10,14,9}: 13,10,9 ✗. babba {7,4,9,2}: 4,9 ✗. baaba {12,9,14,8}: 9,8 ✗. None.

- babaa {13,10,14,9} and babba {7,4,9,2}: share 9 ✗
- babaa and baaba {12,9,14,8}: share 14,9 ✗
- babaa and bbaba {9,4,10,3}: share 10,9 ✗
- babba {7,4,9,2} and baaba {12,9,14,8}: share 9 ✗
- babba and bbaba {9,4,10,3}: share 9,4 ✗
- baaba {12,9,14,8} and bbaba {9,4,10,3}: share 9 ✗

So we can get at most 2 disjoint 4-run sets (plus 1 two-run = 3 total). Not 4.

What about 4+4+4+... = need 3 four-run for 12, or 4+4+4+2 = 14 for 4 numbers. We already found 2 two-run + 2 four-run = 4 numbers.

Can we get 3 four-run? From the analysis above, max 2 disjoint 4-run sets (when also using a 2-run). Without 2-run:

4-run sets: ababb {2,5,1,6}, abaab {8,11,6,13}, abbab {3,6,1,7}, aabab {6,11,5,12}, babaa {13,10,14,9}, babba {7,4,9,2}, baaba {12,9,14,8}, bbaba {9,4,10,3}.

Note: 6 (abab) appears in ababb, abaab, abbab, aabab. 9 (baba) appears in babaa, babba, baaba, bbaba. So we can pick at most 1 from the first group and 1 from the second group, giving max 2 disjoint 4-run sets.

Wait, can we pick 1 from each group and they're disjoint?
- abaab {8,11,6,13} and babba {7,4,9,2}: disjoint ✓ (as found above)
- abaab and bbaba {9,4,10,3}: disjoint ✓
- ababb {2,5,1,6} and babaa {13,10,14,9}: disjoint ✓
- ababb and baaba {12,9,14,8}: disjoint ✓
- etc.

So max 2 disjoint 4-run sets. Combined with 2 two-run, we get 4 numbers.

What about 2 two-run + 2 four-run + something? We used 12 four-sequences, leaving 2. No D set has size ≤ 2 using just those 2.

What about 2 two-run + 1 four-run + 1 five-run? 4+4+5 = 13. Let me check.

aabbb {1,5} + bbaaa {14,10} + abaab {8,11,6,13}. Used: {1,5,8,10,11,13,14,6}. Remaining: {2,3,4,7,9,12}.

5-run: ababa {9,12,7,13,6}: 13,6 ✗. babab {6,3,8,2,9}: 6,8 ✗. None.

aabbb {1,5} + bbaaa {14,10} + babba {7,4,9,2}. Used: {1,2,4,5,7,9,10,14}. Remaining: {3,6,8,11,12,13}.

5-run: ababa {9,12,7,13,6}: 9,7 ✗. babab {6,3,8,2,9}: 2,9 ✗. None.

So 5 numbers seems impossible for a single pair (without single-digit four-sequences).

Let me also check: can we get 4 numbers in other ways?

0 two-run + 2 three-run + 1 four-run: 6+4 = 10 four-sequences. We found this above (3 numbers). Can we add another?

abbba {4,7,1} + bbaab {8,3,10} + aabab {6,11,5,12}. Used: {1,3,4,5,6,7,8,10,11,12}. Remaining: {2,9,13,14}.

Can we add? 2-run: none from {2,9,13,14}. 3-run: none. 4-run: babaa {13,10,14,9}: 10 ✗. 5-run: ababa {9,12,7,13,6}: 12,7,6 ✗. babab {6,3,8,2,9}: 6,3,8 ✗. None.

So 3 numbers max with this approach.

What about 1 three-run + 2 four-run? 3+4+4 = 11. 
abbaa {10,13,7}. 4-run disjoint: abaab {8,11,6,13}: 13 ✗. babaa {13,10,14,9}: 13,10 ✗. babba {7,4,9,2}: 7 ✗. baaba {12,9,14,8}: ✓. bbaba {9,4,10,3}: 10 ✗. ababb {2,5,1,6}: ✓. abbab {3,6,1,7}: 7 ✗. aabab {6,11,5,12}: ✓.

From {baaba, ababb, aabab}: 
- baaba {12,9,14,8} and ababb {2,5,1,6}: disjoint ✓. Used: {10,13,7,12,9,14,8,2,5,1,6} = 11. Remaining: {3,4,11}.
  Can we add? No D set fits in {3,4,11}.
- baaba and aabab {6,11,5,12}: share 12 ✗
- ababb and aabab: share 5,6 ✗

So 3 numbers (1 three-run + 2 four-run) using 11 four-sequences.

What about 1 three-run + 2 four-run + 1 two-run? That would be 3+4+4+2 = 13.

abbaa {10,13,7} + baaba {12,9,14,8} + ababb {2,5,1,6}. Used: {1,2,5,6,7,8,9,10,12,13,14}. Remaining: {3,4,11}.

2-run from {3,4,11}: none. So can't add a 2-run.

Let me try different: abbba {4,7,1} + baaba {12,9,14,8} + ababb... ababb {2,5,1,6}: 1 ✗. abaab {8,11,6,13}: 8 ✗. aabab {6,11,5,12}: 12 ✗. bbaba {9,4,10,3}: 9,4 ✗. babaa {13,10,14,9}: 9,14 ✗. babba {7,4,9,2}: 7,4,9 ✗. abbab {3,6,1,7}: 1,7 ✗.

None! So abbba + baaba can't be extended with a 4-run.

Let me try: baaab {11,8,14} + ababb {2,5,1,6} + babba {7,4,9,2}: share 2 ✗.
baaab + ababb + bbaba {9,4,10,3}: disjoint? {11,8,14} and {2,5,1,6} and {9,4,10,3}: all disjoint ✓! Used: {1,2,3,4,5,6,8,9,10,11,14}. Remaining: {7,12,13}.

2-run from {7,12,13}: none. 3-run: abbaa {10,13,7}: 10 ✗. aabba {7,12,5}: 5 ✗. None.

So 3 numbers using 11 four-sequences.

I'm starting to think the maximum is 4 numbers per pair (2 two-run + 2 four-run), using 12 four-sequences, with 2 four-sequences wasted.

But wait, can we use those 2 wasted four-sequences for numbers from other pairs? No, because four-sequences using digits {a,b} can only be in D(x) for numbers using digits from {a,b}. So the 14 two-digit four-sequences for pair {a,b} are exclusive to that pair.

Actually wait, that's not quite right. A 4-sequence like abab uses digits a and b. It can only be in D(x) if x uses digits from {a,b}. And x must use at most 2 digits. So if x uses digits {a,b}, then D(x) contains only 4-sequences using digits from {a,b}. The 4-sequence abab can only be in D(x) for numbers using digits {a,b} (or {a} or {b} alone, but those give aaaa or bbbb). So yes, the 14 two-digit four-sequences for {a,b} are exclusive to numbers using exactly digits {a,b}.

So for each pair {a,b}, we can independently optimize, except for the shared single-digit four-sequences.

Now, the single-digit four-sequences (aaaa for each a) can be used by:
1. aaaaa (1-run): uses only aaaa, |D|=1
2. 2-run numbers with k=1 or k=4 involving digit a: e.g., aaaab uses {aaab, aaaa}, baaaa uses {aaaa, baaa}
3. 3-run numbers with middle run of length 1: e.g., aabaa uses {abaa, aaaa, aaba}

For each digit a, aaaa can be used by at most one number. The candidates are:
- aaaaa (uses 1 four-sequence: aaaa)
- For each b ≠ a: aaaab (uses aaaa + aaab), baaaa (uses aaaa + baaa), abaaa (uses aaaa + baaa + abaa), aabaa (uses aaaa + abaa + aaba), aaaba (uses aaaa + aaba + aaab)

Using aaaaa gives 1 number for 1 four-sequence (aaaa). Using aaaab gives 1 number for 2 four-sequences (aaaa + aaab), but aaab is a two-digit four-sequence for pair {a,b}, so it competes with the per-pair optimization.

If we use aaaaa, we get 1 number and don't consume any two-digit four-sequences. If we use a 2-run or 3-run number involving aaaa, we get 1 number but consume a two-digit four-sequence from some pair.

Given that the per-pair optimization gives 4 numbers using 12 out of 14 two-digit four-sequences (leaving 2 unused), maybe we can use those 2 unused four-sequences together with aaaa to get an extra number.

Let me think about this. For pair {a,b}, the 4-number solution uses 12 of 14 two-digit four-sequences, leaving 2 unused. Which 2 are unused depends on the specific choice.

Example: aabbb {1,5} + bbaaa {14,10} + abaab {8,11,6,13} + babba {7,4,9,2}.
Used: {1,2,4,5,6,7,8,9,10,11,13,14}. Unused: {3,12} = {bbab, aaba}.

Can we use aaaa with one of the unused? We need a number whose D set includes aaaa and one of {bbab, aaba} (and possibly others, all from the unused set).

A number using aaaa in its D set has 4 a's and 1 b (or is aaaaa). The 4-a-1-b numbers and their D sets:
- baaaa: {aaaa, baaa} — baaa = 14, not in unused ✗
- abaaa: {baaa, aaaa, abaa} — baaa=14, abaa=13, not in unused ✗
- aabaa: {abaa, aaaa, aaba} — abaa=13, aaba=12. 13 not in unused ✗
- aaaba: {aaba, aaaa, aaab} — aaba=12, aaab=11. 11 not in unused ✗
- aaaab: {aaab, aaaa} — aaab=11, not in unused ✗

None work with unused = {3, 12} = {bbab, aaba}.

What about the b-side? bbbb with one of the unused?
4-b-1-a numbers:
- abbbb: {bbbb, abbb} — abbb=1, not in unused ✗
- babbb: {abbb, bbbb, babb} — abbb=1, babb=2, not in unused ✗
- bbabb: {babb, bbbb, bbab} — babb=2, bbab=3. 2 not in unused ✗
- bbbab: {bbab, bbbb, bbba} — bbab=3, bbba=4. 4 not in unused ✗
- bbbba: {bbba, bbbb} — bbba=4, not in unused ✗

None work with unused = {3, 12}.

Let me try a different 4-number solution for pair {a,b} and see what's unused.

aabbb {1,5} + bbaaa {14,10} + abaab {8,11,6,13} + bbaba {9,4,10,3}: share 10 with bbaaa ✗.

aabbb {1,5} + bbaaa {14,10} + babba {7,4,9,2} + abaab {8,11,6,13}: same as before, unused {3,12}.

aabbb {1,5} + bbbaa {10,4}: share? {1,5} and {10,4} disjoint ✓. 
4-run disjoint from {1,5,10,4}: 
- abaab {8,11,6,13}: ✓
- babaa {13,10,14,9}: 10 ✗
- babba {7,4,9,2}: 4 ✗
- baaba {12,9,14,8}: ✓
- bbaba {9,4,10,3}: 4,10 ✗
- ababb {2,5,1,6}: 5,1 ✗
- abbab {3,6,1,7}: 1 ✗
- aabab {6,11,5,12}: 5 ✗

From {abaab, baaba}: share 8 ✗. So only 1 four-run. Total: 3 numbers.

aaabb {5,11} + bbaaa {14,10}: disjoint ✓. Used: {5,10,11,14}.
4-run disjoint: 
- ababb {2,5,1,6}: 5 ✗
- abaab {8,11,6,13}: 11 ✗
- abbab {3,6,1,7}: ✓
- aabab {6,11,5,12}: 11,5 ✗
- babaa {13,10,14,9}: 10,14 ✗
- babba {7,4,9,2}: ✓
- baaba {12,9,14,8}: 14 ✗
- bbaba {9,4,10,3}: 10 ✗

From {abbab, babba}: {3,6,1,7} and {7,4,9,2}: share 7 ✗. So only 1. Total: 3.

aaabb {5,11} + bbbaa {10,4}: disjoint ✓. Used: {4,5,10,11}.
4-run disjoint:
- ababb {2,5,
