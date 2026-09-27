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
  <problem_id>polymath_01258</problem_id>
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

Frank and Joe are playing ping pong. For each game, there is a \(30\%\) chance that Frank wins and a \(70\%\) chance Joe wins. During a match, they play games until someone wins a total of \(21\) games. What is the expected value of the number of games played per match?

## Standard Solution

The expected value of the ratio of Frank's to Joe's score is \(3:7\), so Frank is expected to win \(9\) games for each of Joe's \(21\). Thus, the expected number of games in a match is \(30\).

\(\boxed{30}\)

## AI's Thinking (Attempted Solution Process)

The problem asks for the expected number of games played in a match where Frank and Joe play until someone wins 21 games. Frank wins each game with probability 0.3, Joe with 0.7.

Let me solve this. The match ends when someone reaches 21 wins. The number of games played is at least 21 and at most 41.

Let me think about this carefully. The match ends when either Frank reaches 21 wins or Joe reaches 21 wins.

Let N = number of games played. The match ends at game N where N is the first time either player reaches 21.

The minimum is 21 (someone wins 21 in a row, or more generally wins all first 21 games). The maximum is 41 (someone wins 21-20).

Let me compute E[N].

Approach: The match ends when someone reaches 21. Let's think of it as: we play games, and the match ends when either Frank has 21 wins or Joe has 21 wins.

E[N] = sum over n from 21 to 41 of n * P(N = n).

Alternatively, E[N] = sum over n from 20 to 40 of P(N > n).

N > n means after n games, neither has reached 21. So after n games, Frank has at most 20 wins and Joe has at most 20 wins. Since n = Frank wins + Joe wins, if n ≤ 20, both have at most 20, so N > n always for n ≤ 20. For n from 21 to 40, N > n means Frank has between n-20 and 20 wins (so that Joe has at most 20 and Frank has at most 20).

Actually, let me use the formula E[N] = sum_{n=0}^{40} P(N > n).

For n ≤ 20: P(N > n) = 1 (since you need at least 21 games for someone to reach 21).

For n from 21 to 40: P(N > n) = P(after n games, Frank wins ≤ 20 and Joe wins ≤ 20) = P(Frank wins between max(0, n-20) and 20 in n games).

Since Joe wins = n - Frank wins, Joe ≤ 20 means Frank ≥ n-20. Frank ≤ 20. So Frank wins in [max(0,n-20), 20].

For n from 21 to 40, max(0, n-20) = n-20 (since n ≥ 21 > 20).

So P(N > n) = sum_{k=n-20}^{20} C(n,k) * 0.3^k * 0.7^{n-k}.

E[N] = 21 + sum_{n=21}^{40} sum_{k=n-20}^{20} C(n,k) * 0.3^k * 0.7^{n-k}.

Wait, E[N] = sum_{n=0}^{40} P(N > n) = sum_{n=0}^{20} 1 + sum_{n=21}^{40} P(N > n) = 21 + sum_{n=21}^{40} P(N > n).

This is a computational problem. Let me compute this numerically.

Actually, let me think about whether there's a cleaner approach. 

Alternative: E[N] = 21 + E[number of games beyond 21]. 

Hmm, let me think differently. The match ends when someone reaches 21. Let's think of it as a race to 21.

Actually, let me just compute numerically. Let me be careful.

E[N] = 21 + sum_{n=21}^{40} P(N > n)

where P(N > n) = sum_{k=n-20}^{20} C(n,k) (0.3)^k (0.7)^{n-k}.

Let me compute this. Actually, let me think about it more cleverly.

P(N > n) for n ≥ 21 is the probability that in n games, both players have between n-20 and 20 wins. Equivalently, it's 1 - P(Frank ≥ 21 in n games) - P(Joe ≥ 21 in n games).

P(Frank ≥ 21 in n games) = sum_{k=21}^{n} C(n,k) 0.3^k 0.7^{n-k}.
P(Joe ≥ 21 in n games) = sum_{k=21}^{n} C(n,k) 0.7^k 0.3^{n-k} = sum_{j=0}^{n-21} C(n,j) 0.3^j 0.7^{n-j} (where j = n-k, k ≥ 21 means j ≤ n-21).

These two events are mutually exclusive when n ≤ 40 (both can't have ≥ 21 wins if n ≤ 40, since that requires n ≥ 42). For n = 41, both having ≥ 21 is impossible too (21+21=42 > 41). So they're always mutually exclusive for n ≤ 41.

So P(N > n) = 1 - P(Frank ≥ 21) - P(Joe ≥ 21) for n from 21 to 40.

E[N] = 21 + sum_{n=21}^{40} [1 - P(Frank ≥ 21 in n) - P(Joe ≥ 21 in n)].

= 21 + 20 - sum_{n=21}^{40} P(Frank ≥ 21 in n) - sum_{n=21}^{40} P(Joe ≥ 21 in n).

= 41 - sum_{n=21}^{40} P(Frank ≥ 21 in n) - sum_{n=21}^{40} P(Joe ≥ 21 in n).

Hmm, this is still computational. Let me just compute numerically.

Let me compute S_F = sum_{n=21}^{40} P(Frank ≥ 21 in n games) and S_J = sum_{n=21}^{40} P(Joe ≥ 21 in n games).

P(Frank ≥ 21 in n games) = sum_{k=21}^{n} C(n,k) 0.3^k 0.7^{n-k}.

For n = 21: P = 0.3^21 (very small).
For n = 22: P = sum_{k=21}^{22} C(22,k) 0.3^k 0.7^{22-k} = C(22,21) 0.3^21 0.7 + 0.3^22.
...

This is getting complex. Let me think about whether I should just compute this numerically with careful arithmetic.

Actually, let me reconsider. There might be a cleaner way using the negative binomial or something.

Let me think about it as: the match is a sequence of games. Let X = number of games until Frank gets 21 wins (negative binomial), Y = number of games until Joe gets 21 wins. N = min(X, Y).

E[N] = sum_{n=0}^{inf} P(N > n) = sum_{n=0}^{40} P(X > n and Y > n).

P(X > n) = P(Frank has ≤ 20 wins in n games) = sum_{k=0}^{min(20,n)} C(n,k) 0.3^k 0.7^{n-k}.
P(Y > n) = P(Joe has ≤ 20 wins in n games) = sum_{k=0}^{min(20,n)} C(n,k) 0.7^k 0.3^{n-k}.

P(X > n and Y > n) = P(both ≤ 20 wins in n games). For n ≤ 20, this is 1. For n ≥ 21, it's P(Frank wins in [n-20, 20]).

This is the same as before. Let me just compute numerically.

Let me compute this step by step. I'll compute P(N > n) for n = 21, 22, ..., 40.

P(N > n) = sum_{k=n-20}^{20} C(n,k) 0.3^k 0.7^{n-k}.

Let me compute each term. This is tedious but let me try.

Actually, let me use the complementary form:
P(N > n) = 1 - P(Frank ≥ 21) - P(Joe ≥ 21)

where P(Frank ≥ 21) = sum_{k=21}^{n} C(n,k) 0.3^k 0.7^{n-k} and P(Joe ≥ 21) = sum_{k=0}^{n-21} C(n,k) 0.3^k 0.7^{n-k}.

Note P(Joe ≥ 21 in n games) = P(Frank ≤ n-21 in n games) = sum_{k=0}^{n-21} C(n,k) 0.3^k 0.7^{n-k}.

So P(N > n) = 1 - [upper tail] - [lower tail] = P(n-20 ≤ Frank wins ≤ 20), which is the middle part.

Let me just compute E[N] numerically. Let me try to be systematic.

E[N] = 21 + sum_{n=21}^{40} P(N > n).

Let me compute P(N > n) for each n from 21 to 40.

For n = 21: P(N > 21) = P(Frank wins exactly... well, Frank wins in [1, 20]). 
P(N > 21) = 1 - P(Frank = 21) - P(Joe = 21) = 1 - 0.3^21 - 0.7^21.
0.3^21 ≈ very small, 0.7^21 ≈ 0.7^21. 
0.7^10 ≈ 0.028248, 0.7^20 ≈ 0.000798, 0.7^21 ≈ 0.000558.
0.3^21 ≈ negligible (0.3^10 ≈ 5.9e-6, 0.3^20 ≈ 3.5e-11, 0.3^21 ≈ 1e-11).
So P(N > 21) ≈ 1 - 0.000558 = 0.999442.

This is going to be very tedious for all 20 terms. Let me think if there's a smarter approach.

Actually, let me reconsider. Let me think about E[N] differently.

E[N] = E[min(X, Y)] where X ~ NegBin(r=21, p=0.3) and Y ~ NegBin(r=21, p=0.7), but X and Y are dependent (they're based on the same sequence of games).

Actually, X and Y are not independent. They're both determined by the same sequence of Bernoulli trials.

Let me think about it yet another way. 

E[N] = sum_{n=0}^{40} P(N > n).

Let me split: E[N] = sum_{n=0}^{20} 1 + sum_{n=21}^{40} P(N > n) = 21 + sum_{n=21}^{40} P(N > n).

Now, sum_{n=21}^{40} P(N > n) = sum_{n=21}^{40} P(n-20 ≤ K_n ≤ 20) where K_n ~ Bin(n, 0.3).

Let me substitute m = n - 20, so m goes from 1 to 20, n = m + 20:
sum_{m=1}^{20} P(m ≤ K_{m+20} ≤ 20).

Hmm, not obviously simpler.

Let me try yet another approach. 

E[N] = E[21 + (games played beyond the 21st)].

After 21 games, if someone has 21 wins, the match is over. Otherwise, we continue.

Actually, let me think about it as: E[N] = 21 + E[extra games].

The extra games beyond 21: after each game from 21 onward, the match continues if neither has reached 21.

Hmm, let me just try to compute this numerically with reasonable precision. Let me organize the computation.

Let me define for n from 21 to 40:
P(N > n) = sum_{k=n-20}^{20} C(n,k) (0.3)^k (0.7)^{n-k}

I need to compute this sum for each n and add them up.

Let me try to compute this using a different parametrization. Let j = k - (n-20), so j goes from 0 to 40-n, and k = n-20+j.

P(N > n) = sum_{j=0}^{40-n} C(n, n-20+j) (0.3)^{n-20+j} (0.7)^{20-j}.

Hmm, still complex.

Let me try to just compute numerically. I'll compute P(N > n) for each n.

Actually, let me think about this problem differently. Let me use the fact that:

E[N] = 21 + sum_{n=21}^{40} P(N > n)

and try to compute the sum numerically.

Let me compute P(N > n) = P(Bin(n, 0.3) ∈ [n-20, 20]).

For n = 21: P(Bin(21, 0.3) ∈ [1, 20]) = 1 - P(Bin(21,0.3)=0) - P(Bin(21,0.3)=21) = 1 - 0.7^21 - 0.3^21.
0.7^21 = 0.7^21. Let me compute: 0.7^1=0.7, 0.7^2=0.49, 0.7^3=0.343, 0.7^4=0.2401, 0.7^5=0.16807, 0.7^6=0.117649, 0.7^7=0.0823543, 0.7^8=0.05764801, 0.7^9=0.040353607, 0.7^10=0.028247525, 0.7^11=0.019773267, 0.7^12=0.013841287, 0.7^13=0.009688901, 0.7^14=0.006782231, 0.7^15=0.004747562, 0.7^16=0.003323293, 0.7^17=0.002326305, 0.7^18=0.001628414, 0.7^19=0.001139889, 0.7^20=0.000797923, 0.7^21=0.000558546.

0.3^21: 0.3^1=0.3, 0.3^2=0.09, 0.3^3=0.027, 0.3^4=0.0081, 0.3^5=0.00243, 0.3^6=0.000729, 0.3^7=0.0002187, 0.3^8=0.00006561, 0.3^9=0.000019683, 0.3^10=0.0000059049, 0.3^11=0.00000177147, 0.3^12=0.000000531441, 0.3^13≈1.594e-7, 0.3^14≈4.783e-8, 0.3^15≈1.435e-8, ... 0.3^21 ≈ 2.55e-12. Negligible.

So P(N > 21) ≈ 1 - 0.0005585 = 0.9994415.

For n = 22: P(Bin(22, 0.3) ∈ [2, 20]) = 1 - P(≤1) - P(=21) - P(=22).
P(=22) = 0.3^22 ≈ 7.66e-12. Negligible.
P(=21) = C(22,21) 0.3^21 0.7 = 22 * 2.55e-12 * 0.7 ≈ 3.93e-11. Negligible.
P(≤1) = 0.7^22 + 22*0.3*0.7^21 = 0.7^22 + 22*0.3*0.7^21.
0.7^22 = 0.7 * 0.7^21 = 0.7 * 0.000558546 = 0.000390982.
22*0.3*0.7^21 = 6.6 * 0.000558546 = 0.003686404.
P(≤1) = 0.000390982 + 0.003686404 = 0.004077386.
P(N > 22) ≈ 1 - 0.004077386 = 0.995922614.

For n = 23: P(Bin(23, 0.3) ∈ [3, 20]) = 1 - P(≤2) - P(≥21).
P(≥21) = P(=21) + P(=22) + P(=23).
P(=23) = 0.3^23 ≈ negligible.
P(=22) = C(23,22) 0.3^22 0.7 = 23 * 7.66e-12 * 0.7 ≈ negligible.
P(=21) = C(23,21) 0.3^21 0.7^2 = C(23,2) * 2.55e-12 * 0.49 = 253 * 2.55e-12 * 0.49 ≈ 3.16e-10. Negligible.
P(≤2) = 0.7^23 + 23*0.3*0.7^22 + C(23,2)*0.3^2*0.7^21.
0.7^23 = 0.7 * 0.000390982 = 0.000273687.
23*0.3*0.7^22 = 6.9 * 0.000390982 = 0.002697775.
C(23,2) = 253. 253 * 0.09 * 0.000558546 = 253 * 0.000050269 = 0.012718118.
P(≤2) = 0.000273687 + 0.002697775 + 0.012718118 = 0.015689580.
P(N > 23) ≈ 1 - 0.015689580 = 0.984310420.

For n = 24: P(Bin(24, 0.3) ∈ [4, 20]) = 1 - P(≤3) - P(≥21).
P(≥21): P(=21) = C(24,21) 0.3^21 0.7^3 = C(24,3) * 2.55e-12 * 0.343 = 2024 * 2.55e-12 * 0.343 ≈ 1.77e-9. Negligible.
P(≤3) = P(=0) + P(=1) + P(=2) + P(=3).
P(=0) = 0.7^24 = 0.7 * 0.000273687 = 0.000191581.
P(=1) = 24 * 0.3 * 0.7^23 = 7.2 * 0.000273687 = 0.001970544.
P(=2) = C(24,2) * 0.09 * 0.7^22 = 276 * 0.09 * 0.000390982 = 276 * 0.000035188 = 0.009711953.
P(=3) = C(24,3) * 0.027 * 0.7^21 = 2024 * 0.027 * 0.000558546 = 2024 * 0.000015081 = 0.030523344.
P(≤3) = 0.000191581 + 0.001970544 + 0.009711953 + 0.030523344 = 0.042397422.
P(N > 24) ≈ 1 - 0.042397422 = 0.957602578.

For n = 25: P(Bin(25, 0.3) ∈ [5, 20]) = 1 - P(≤4) - P(≥21).
P(≥21): P(=21) = C(25,21) 0.3^21 0.7^4 = C(25,4) * 2.55e-12 * 0.2401 = 12650 * 2.55e-12 * 0.2401 ≈ 7.75e-9. Negligible.
P(≤4):
P(=0) = 0.7^25 = 0.7 * 0.000191581 = 0.000134107.
P(=1) = 25 * 0.3 * 0.7^24 = 7.5 * 0.000191581 = 0.001436854.
P(=2) = C(25,2) * 0.09 * 0.7^23 = 300 * 0.09 * 0.000273687 = 300 * 0.000024632 = 0.007389549.
P(=3) = C(25,3) * 0.027 * 0.7^22 = 2300 * 0.027 * 0.000390982 = 2300 * 0.000010557 = 0.024280191.
P(=4) = C(25,4) * 0.0081 * 0.7^21 = 12650 * 0.0081 * 0.000558546 = 12650 * 0.000004524 = 0.057228846.
P(≤4) = 0.000134107 + 0.001436854 + 0.007389549 + 0.024280191 + 0.057228846 = 0.090469547.
P(N > 25) ≈ 1 - 0.090469547 = 0.909530453.

For n = 26: P(Bin(26, 0.3) ∈ [6, 20]) = 1 - P(≤5) - P(≥21).
P(≥21): P(=21) = C(26,21) 0.3^21 0.7^5 = C(26,5) * 2.55e-12 * 0.16807 = 65780 * 2.55e-12 * 0.16807 ≈ 2.82e-8. Negligible.
P(≤5):
P(=0) = 0.7^26 = 0.7 * 0.000134107 = 0.000093875.
P(=1) = 26 * 0.3 * 0.7^25 = 7.8 * 0.000134107 = 0.001046037.
P(=2) = C(26,2) * 0.09 * 0.7^24 = 325 * 0.09 * 0.000191581 = 325 * 0.000017242 = 0.005603722.
P(=3) = C(26,3) * 0.027 * 0.7^23 = 2600 * 0.027 * 0.000273687 = 2600 * 0.000007390 = 0.019213287.
P(=4) = C(26,4) * 0.0081 * 0.7^22 = 14950 * 0.0081 * 0.000390982 = 14950 * 0.000003167 = 0.047344842.
P(=5) = C(26,5) * 0.00243 * 0.7^21 = 65780 * 0.00243 * 0.000558546 = 65780 * 0.000001357 = 0.089279446.
P(≤5) = 0.000093875 + 0.001046037 + 0.005603722 + 0.019213287 + 0.047344842 + 0.089279446 = 0.162581209.
P(N > 26) ≈ 1 - 0.162581209 = 0.837418791.

For n = 27: P(Bin(27, 0.3) ∈ [7, 20]) = 1 - P(≤6) - P(≥21).
P(≥21): P(=21) = C(27,21) 0.3^21 0.7^6 = C(27,6) * 2.55e-12 * 0.117649 = 296010 * 2.55e-12 * 0.117649 ≈ 8.88e-8. Negligible.
P(≤6):
P(=0) = 0.7^27 = 0.7 * 0.000093875 = 0.000065713.
P(=1) = 27 * 0.3 * 0.7^26 = 8.1 * 0.000093875 = 0.000760384.
P(=2) = C(27,2) * 0.09 * 0.7^25 = 351 * 0.09 * 0.000134107 = 351 * 0.000012070 = 0.004236452.
P(=3) = C(27,3) * 0.027 * 0.7^24 = 2925 * 0.027 * 0.000191581 = 2925 * 0.000005173 = 0.015130057.
P(=4) = C(27,4) * 0.0081 * 0.7^23 = 17550 * 0.0081 * 0.000273687 = 17550 * 0.000002217 = 0.038908018.
P(=5) = C(27,5) * 0.00243 * 0.7^22 = 80730 * 0.00243 * 0.000390982 = 80730 * 0.000000950 = 0.076708500.
P(=6) = C(27,6) * 0.000729 * 0.7^21 = 296010 * 0.000729 * 0.000558546 = 296010 * 0.000000407 = 0.120486607.
P(≤6) = 0.000065713 + 0.000760384 + 0.004236452 + 0.015130057 + 0.038908018 + 0.076708500 + 0.120486607 = 0.256295731.
P(N > 27) ≈ 1 - 0.256295731 = 0.743704269.

For n = 28: P(Bin(28, 0.3) ∈ [8, 20]) = 1 - P(≤7) - P(≥21).
P(≥21): P(=21) = C(28,21) 0.3^21 0.7^7 = C(28,7) * 2.55e-12 * 0.0823543 = 1184040 * 2.55e-12 * 0.0823543 ≈ 2.49e-7. Negligible.
P(≤7):
P(=0) = 0.7^28 = 0.7 * 0.000065713 = 0.000045999.
P(=1) = 28 * 0.3 * 0.7^27 = 8.4 * 0.000065713 = 0.000551987.
P(=2) = C(28,2) * 0.09 * 0.7^26 = 378 * 0.09 * 0.000093875 = 378 * 0.000008449 = 0.003193610.
P(=3) = C(28,3) * 0.027 * 0.7^25 = 3276 * 0.027 * 0.000134107 = 3276 * 0.000003621 = 0.011863690.
P(=4) = C(28,4) * 0.0081 * 0.7^24 = 20475 * 0.0081 * 0.000191581 = 20475 * 0.000001552 = 0.031777000.
P(=5) = C(28,5) * 0.00243 * 0.7^23 = 98280 * 0.00243 * 0.000273687 = 98280 * 0.000000665 = 0.065367220.
P(=6) = C(28,6) * 0.000729 * 0.7^22 = 376740 * 0.000729 * 0.000390982 = 376740 * 0.000000285 = 0.107381190.
P(=7) = C(28,7) * 0.0002187 * 0.7^21 = 1184040 * 0.0002187 * 0.000558546 = 1184040 * 0.000000122 = 0.144565080.
P(≤7) = 0.000045999 + 0.000551987 + 0.003193610 + 0.011863690 + 0.031777000 + 0.065367220 + 0.107381190 + 0.144565080 = 0.364745776.
P(N > 28) ≈ 1 - 0.364745776 = 0.635254224.

For n = 29: P(Bin(29, 0.3) ∈ [9, 20]) = 1 - P(≤8) - P(≥21).
P(≥21): P(=21) = C(29,21) 0.3^21 0.7^8 = C(29,8) * 2.55e-12 * 0.05764801 = 4292145 * 2.55e-12 * 0.05764801 ≈ 6.31e-7. Still negligible.
P(≤8):
P(=0) = 0.7^29 = 0.7 * 0.000045999 = 0.000032199.
P(=1) = 29 * 0.3 * 0.7^28 = 8.7 * 0.000045999 = 0.000400191.
P(=2) = C(29,2) * 0.09 * 0.7^27 = 406 * 0.09 * 0.000065713 = 406 * 0.000005914 = 0.002401084.
P(=3) = C(29,3) * 0.027 * 0.7^26 = 3654 * 0.027 * 0.000093875 = 3654 * 0.000002535 = 0.009262890.
P(=4) = C(29,4) * 0.0081 * 0.7^25 = 23751 * 0.0081 * 0.000134107 = 23751 * 0.000001086 = 0.025807627.
P(=5) = C(29,5) * 0.00243 * 0.7^24 = 118755 * 0.00243 * 0.000191581 = 118755 * 0.000000466 = 0.055331083.
P(=6) = C(29,6) * 0.000729 * 0.7^23 = 475020 * 0.000729 * 0.000273687 = 475020 * 0.000000199 = 0.094740980.
P(=7) = C(29,7) * 0.0002187 * 0.7^22 = 1560780 * 0.0002187 * 0.000390982 = 1560780 * 0.0000000855 = 0.133486719.
P(=8) = C(29,8) * 0.00006561 * 0.7^21 = 4292145 * 0.00006561 * 0.000558546 = 4292145 * 0.0000000366 = 0.157252447.
P(≤8) = 0.000032199 + 0.000400191 + 0.002401084 + 0.009262890 + 0.025807627 + 0.055331083 + 0.094740980 + 0.133486719 + 0.157252447 = 0.478715220.
P(N > 29) ≈ 1 - 0.478715220 = 0.521284780.

For n = 30: P(Bin(30, 0.3) ∈ [10, 20]) = 1 - P(≤9) - P(≥21).
Now P(≥21) starts to be non-negligible. Let me compute both tails.
P(≤9):
P(=0) = 0.7^30 = 0.7 * 0.000032199 = 0.000022540.
P(=1) = 30 * 0.3 * 0.7^29 = 9 * 0.000032199 = 0.000289791.
P(=2) = C(30,2) * 0.09 * 0.7^28 = 435 * 0.09 * 0.000045999 = 435 * 0.000004140 = 0.001800904.
P(=3) = C(30,3) * 0.027 * 0.7^27 = 4060 * 0.027 * 0.000065713 = 4060 * 0.000001774 = 0.007203014.
P(=4) = C(30,4) * 0.0081 * 0.7^26 = 27405 * 0.0081 * 0.000093875 = 27405 * 0.000000760 = 0.020844048.
P(=5) = C(30,5) * 0.00243 * 0.7^25 = 142506 * 0.00243 * 0.000134107 = 142506 * 0.000000326 = 0.046455656.
P(=6) = C(30,6) * 0.000729 * 0.7^24 = 593775 * 0.000729 * 0.000191581 = 593775 * 0.000000140 = 0.082908473.
P(=7) = C(30,7) * 0.0002187 * 0.7^23 = 2035800 * 0.0002187 * 0.000273687 = 2035800 * 0.0000000599 = 0.121924420.
P(=8) = C(30,8) * 0.00006561 * 0.7^22 = 5852925 * 0.00006561 * 0.000390982 = 5852925 * 0.0000000256 = 0.150090880.
P(=9) = C(30,9) * 0.000019683 * 0.7^21 = 14307150 * 0.000019683 * 0.000558546 = 14307150 * 0.00000001099 = 0.157297626.
P(≤9) = 0.000022540 + 0.000289791 + 0.001800904 + 0.007203014 + 0.020844048 + 0.046455656 + 0.082908473 + 0.121924420 + 0.150090880 + 0.157297626 = 0.588737352.

P(≥21):
P(=21) = C(30,21) 0.3^21 0.7^9 = C(30,9) * 2.55e-12 * 0.040353607 = 14307150 * 2.55e-12 * 0.040353607 = 14307150 * 1.029e-13 = 1.472e-6. Very small.
P(=22) = C(30,22) 0.3^22 0.7^8 = C(30,8) * 7.66e-12 * 0.05764801 = 5852925 * 4.416e-13 = 2.584e-6. Very small.
P(=23) = C(30,23) 0.3^23 0.7^7 = C(30,7) * 2.298e-12 * 0.0823543 = 2035800 * 1.892e-13 = 3.852e-7. Very small.
Higher terms even smaller.
P(≥21) ≈ 1.472e-6 + 2.584e-6 + 3.852e-7 + ... ≈ 4.5e-6. Negligible.

P(N > 30) ≈ 1 - 0.588737352 - 0.0000045 = 0.411258148.

Hmm, this is getting really tedious and error-prone. Let me think about whether there's a cleaner analytical approach.

Actually, let me reconsider the problem. The answer is likely a "nice" number or at least a computable expression. Let me think about whether there's a closed form.

E[N] = 21 + sum_{n=21}^{40} P(N > n).

Hmm, I wonder if there's a way to express this more cleanly.

Actually, let me think about it differently. Let me use the identity:

E[N] = sum_{n=0}^{inf} P(N > n) = sum_{n=0}^{40} P(N > n).

For a race to r wins, there's a known result. Let me think...

The expected number of games in a race to r wins where player A wins each game with probability p:

E[N] = r + sum_{n=r}^{2r-2} P(N > n)

where P(N > n) = P(neither player has r wins after n games).

Actually, I recall that for a race to r, E[N] = r * [some expression]. But I don't think there's a simple closed form in general.

Let me try a different approach. Let me think about E[N] using the linearity of expectation in a clever way.

Consider the match as a sequence of games. The match ends at game N. 

E[N] = E[21 + (N - 21)] = 21 + E[N - 21].

N - 21 is the number of "extra" games beyond 21. 

Hmm, that doesn't simplify things directly.

Let me try another approach. Think of it as: we play games until someone reaches 21. 

E[N] = sum_{k=0}^{20} E[N | Frank ends with 21-k, Joe ends with k] * P(Frank wins match with Joe having k wins) + similar for Joe winning.

If Frank wins the match with Joe having exactly k wins (k = 0, 1, ..., 20), then the match lasted 21 + k games, and the last game was won by Frank. The probability is C(20+k, k) * 0.3^21 * 0.7^k (Frank wins 21, Joe wins k, last game is Frank's).

Similarly, if Joe wins with Frank having exactly k wins (k = 0, 1, ..., 20), the match lasted 21 + k games, last game won by Joe. Probability is C(20+k, k) * 0.7^21 * 0.3^k.

So E[N] = sum_{k=0}^{20} (21+k) * [C(20+k, k) * 0.3^21 * 0.7^k + C(20+k, k) * 0.7^21 * 0.3^k].

= sum_{k=0}^{20} (21+k) * C(20+k, k) * [0.3^21 * 0.7^k + 0.7^21 * 0.3^k].

This is a finite sum that can be computed. Let me see if there's a simplification.

Let S = sum_{k=0}^{20} (21+k) * C(20+k, k) * [0.3^21 * 0.7^k + 0.7^21 * 0.3^k].

Note that (21+k) * C(20+k, k) = (21+k) * C(20+k, 20). 

Also, (21+k) * C(20+k, k) = (21+k) * (20+k)! / (k! * 20!) = (21+k)! / (k! * 20!) * 1/(20+k+1-20) ... hmm, let me think.

(21+k) * C(20+k, k) = (21+k) * (20+k)!/(k! * 20!) 

Let me use the identity: (r+k) * C(r-1+k, k) = r * C(r+k, k) / ... hmm.

Actually, (21+k) * C(20+k, k) = 21 * C(21+k, k). Let me verify:
C(21+k, k) = (21+k)!/(k! * 21!) 
21 * C(21+k, k) = 21 * (21+k)!/(k! * 21!) = (21+k)!/(k! * 20!)
(21+k) * C(20+k, k) = (21+k) * (20+k)!/(k! * 20!) = (21+k)!/(k! * 20!)
Yes! So (21+k) * C(20+k, k) = 21 * C(21+k, k).

So E[N] = 21 * sum_{k=0}^{20} C(21+k, k) * [0.3^21 * 0.7^k + 0.7^21 * 0.3^k].

Now, sum_{k=0}^{20} C(21+k, k) * 0.3^21 * 0.7^k = 0.3^21 * sum_{k=0}^{20} C(21+k, k) * 0.7^k.

And sum_{k=0}^{20} C(21+k, k) * 0.7^21 * 0.3^k = 0.7^21 * sum_{k=0}^{20} C(21+k, k) * 0.3^k.

Now, recall that sum_{k=0}^{inf} C(r-1+k, k) x^k = 1/(1-x)^r for |x| < 1. Here r = 22 (since C(21+k, k) = C(21+k, 21) = C(22-1+k, k)), so:

sum_{k=0}^{inf} C(21+k, k) x^k = 1/(1-x)^22.

So sum_{k=0}^{20} C(21+k, k) x^k = 1/(1-x)^22 - sum_{k=21}^{inf} C(21+k, k) x^k.

The tail sum_{k=21}^{inf} C(21+k, k) x^k is the probability that a NegBin(22, 1-x) variable is ≥ 21, or equivalently... hmm, this is getting complicated.

Actually, let me think about this differently. 

sum_{k=0}^{20} C(21+k, k) * 0.7^k = sum_{k=0}^{20} C(21+k, 21) * 0.7^k.

This is a partial sum of the negative binomial series. The full sum is 1/(1-0.7)^22 = 1/0.3^22.

So sum_{k=0}^{20} C(21+k, k) * 0.7^k = 1/0.3^22 - sum_{k=21}^{inf} C(21+k, k) * 0.7^k.

Therefore:
0.3^21 * sum_{k=0}^{20} C(21+k, k) * 0.7^k = 0.3^21/0.3^22 - 0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k
= 1/0.3 - 0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k.

Similarly:
0.7^21 * sum_{k=0}^{20} C(21+k, k) * 0.3^k = 0.7^21/0.7^22 - 0.7^21 * sum_{k=21}^{inf} C(21+k, k) * 0.3^k
= 1/0.7 - 0.7^21 * sum_{k=21}^{inf} C(21+k, k) * 0.3^k.

So E[N] = 21 * [1/0.3 + 1/0.7 - 0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k - 0.7^21 * sum_{k=21}^{inf} C(21+k, k) * 0.3^k].

Now, 1/0.3 + 1/0.7 = 10/3 + 10/7 = (70 + 30)/21 = 100/21.

So E[N] = 21 * [100/21 - 0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k - 0.7^21 * sum_{k=21}^{inf} C(21+k, k) * 0.3^k].

= 100 - 21 * [0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k + 0.7^21 * sum_{k=21}^{inf} C(21+k, k) * 0.3^k].

Now I need to evaluate the tail sums. Let me think about what they represent.

sum_{k=21}^{inf} C(21+k, k) * 0.7^k * 0.3^21 = sum_{k=21}^{inf} C(21+k, 21) * 0.3^21 * 0.7^k.

This is the probability that in a sequence of Bernoulli(0.3) trials, the 22nd success occurs after at least 21+21 = 42 trials... no wait.

Actually, C(21+k, 21) * 0.3^21 * 0.7^k is the probability that the 22nd success (with prob 0.3) occurs at trial 22+k. Wait no, the negative binomial: P(22nd success at trial 22+k) = C(21+k, 21) * 0.3^22 * 0.7^k. So C(21+k, 21) * 0.3^21 * 0.7^k = P(22nd success at trial 22+k) / 0.3.

So sum_{k=21}^{inf} C(21+k, 21) * 0.3^21 * 0.7^k = (1/0.3) * P(22nd success occurs at trial ≥ 43) = (1/0.3) * P(Bin(42, 0.3) ≤ 21).

Because the 22nd success occurs at trial ≥ 43 iff in the first 42 trials, there are at most 21 successes.

Similarly, sum_{k=21}^{inf} C(21+k, 21) * 0.7^21 * 0.3^k = (1/0.7) * P(Bin(42, 0.7) ≤ 21) = (1/0.7) * P(Bin(42, 0.3) ≥ 21).

So:
0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k = (1/0.3) * P(Bin(42, 0.3) ≤ 21).
0.7^21 * sum_{k=21}^{inf} C(21+k, k) * 0.3^k = (1/0.7) * P(Bin(42, 0.3) ≥ 21).

Therefore:
E[N] = 100 - 21 * [(1/0.3) * P(Bin(42, 0.3) ≤ 21) + (1/0.7) * P(Bin(42, 0.3) ≥ 21)].

Now, P(Bin(42, 0.3) ≤ 21) + P(Bin(42, 0.3) ≥ 21) = 1 + P(Bin(42, 0.3) = 21) (since they overlap at k=21).

Let me denote p = P(Bin(42, 0.3) = 21) and let A = P(Bin(42, 0.3) ≤ 21), B = P(Bin(42, 0.3) ≥ 21). Then A + B = 1 + p.

E[N] = 100 - 21 * [A/0.3 + B/0.7] = 100 - 21 * [A/0.3 + B/0.7].

= 100 - 21 * [(7A + 3B)/2.1] = 100 - 21/2.1 * (7A + 3B) = 100 - 10 * (7A + 3B).

Now, 7A + 3B = 7A + 3(1 + p - A) = 7A + 3 + 3p - 3A = 4A + 3 + 3p.

So E[N] = 100 - 10 * (4A + 3 + 3p) = 100 - 40A - 30 - 30p = 70 - 40A - 30p.

Where A = P(Bin(42, 0.3) ≤ 21) and p = P(Bin(42, 0.3) = 21).

Hmm, this is still a computational expression. Let me see if I can simplify further or if the answer is supposed to be a specific number.

Actually, wait. Let me reconsider. The problem says "What is the expected value of the number of games played per match?" This might expect a numerical answer.

Let me compute A = P(Bin(42, 0.3) ≤ 21) and p = P(Bin(42, 0.3) = 21).

The mean of Bin(42, 0.3) is 12.6, and the standard deviation is sqrt(42 * 0.3 * 0.7) = sqrt(8.82) ≈ 2.97.

21 is about (21 - 12.6)/2.97 ≈ 2.83 standard deviations above the mean. So P(Bin(42, 0.3) ≤ 21) is quite close to 1, maybe around 0.997 or so.

Let me be more precise. Actually, let me compute this more carefully.

P(Bin(42, 0.3) ≥ 21) = P(Bin(42, 0.7) ≤ 21). The mean of Bin(42, 0.7) is 29.4, std dev is still 2.97. 21 is (21-29.4)/2.97 ≈ -2.83 std devs. So P(Bin(42, 0.7) ≤ 21) is small, maybe around 0.002-0.003.

So B = P(Bin(42, 0.3) ≥ 21) ≈ 0.002-0.003, and A = 1 + p - B ≈ 1 - B + p.

Let me compute more precisely. Actually, let me try to compute B = P(Bin(42, 0.3) ≥ 21) = sum_{k=21}^{42} C(42,k) 0.3^k 0.7^{42-k}.

This is P(Bin(42, 0.3) ≥ 21). Let me compute this using the relationship to Bin(42, 0.7):
B = P(Bin(42, 0.3) ≥ 21) = P(Bin(42, 0.7) ≤ 21).

Let me compute P(Bin(42, 0.7) ≤ 21) = sum_{k=0}^{21} C(42,k) 0.7^k 0.3^{42-k}.

The terms near k=21 will dominate (since mean is 29.4, we're in the left tail). Let me compute the terms around k=20, 21.

Actually, this is still quite tedious. Let me try to use a normal approximation to get a rough answer, and then see if the problem expects an exact or approximate answer.

Normal approximation: Bin(42, 0.3) ≈ N(12.6, 8.82).
P(Bin(42, 0.3) ≤ 21) ≈ Φ((21.5 - 12.6)/2.97) = Φ(8.9/2.97) = Φ(2.996) ≈ 0.9987.
P(Bin(42, 0.3) = 21) ≈ φ(2.83)/2.97 ≈ (1/sqrt(2π)) * exp(-2.83^2/2) / 2.97.
exp(-4.00) ≈ 0.0183. 1/sqrt(2π) ≈ 0.3989. So φ(2.83) ≈ 0.3989 * 0.0183 ≈ 0.00730. p ≈ 0.00730/2.97 ≈ 0.00246.

E[N] ≈ 70 - 40 * 0.9987 - 30 * 0.00246 ≈ 70 - 39.948 - 0.0738 ≈ 29.978.

Hmm, so E[N] ≈ 30. That's interesting. Let me check if the answer is exactly 30 or just approximately 30.

Wait, let me reconsider. Is there a reason the answer might be exactly 30?

If Frank wins with probability p = 0.3 and Joe with q = 0.7, and they play to 21, is E[N] = 21/p' for some p'? No, that doesn't make sense.

Actually, let me reconsider. For a race to 1 (first to win a game), E[N] = 1 (always exactly 1 game). For a race to r where p = q = 0.5, by symmetry E[N] = r + sum of P(both < r after n games)... 

Hmm, let me think about whether E[N] = 30 exactly.

If E[N] = 30, then from E[N] = 70 - 40A - 30p, we'd need 40A + 30p = 40, i.e., A = 1 - 3p/4. Since A = 1 - B + p, this means 1 - B + p = 1 - 3p/4, so -B + p = -3p/4, so B = p + 3p/4 = 7p/4. 

Is B = 7p/4? B = P(Bin(42,0.3) ≥ 21) and p = P(Bin(42,0.3) = 21). B = p + P(Bin(42,0.3) ≥ 22). So we'd need P(Bin(42,0.3) ≥ 22) = 3p/4. This seems unlikely to be exactly true.

Let me try to be more precise with the computation. Let me compute B and p more carefully.

Actually, let me try a completely different approach. Let me use the recursion approach.

Let E(a, b) = expected number of additional games when Frank has a wins and Joe has b wins.

E(21, b) = 0 for all b, E(a, 21) = 0 for all a.
E(a, b) = 1 + 0.3 * E(a+1, b) + 0.7 * E(a, b+1) for a < 21, b < 21.

We want E(0, 0).

This is a 21x21 grid (a from 0 to 20, b from 0 to 20). We can solve this by working backwards from the boundary.

E(20, 20) = 1 + 0.3 * E(21, 20) + 0.7 * E(20, 21) = 1 + 0 + 0 = 1.

E(20, 19) = 1 + 0.3 * E(21, 19) + 0.7 * E(20, 20) = 1 + 0 + 0.7 * 1 = 1.7.
E(19, 20) = 1 + 0.3 * E(20, 20) + 0.7 * E(19, 21) = 1 + 0.3 * 1 + 0 = 1.3.

E(20, 18) = 1 + 0.3 * 0 + 0.7 * E(20, 19) = 1 + 0.7 * 1.7 = 1 + 1.19 = 2.19.
E(19, 19) = 1 + 0.3 * E(20, 19) + 0.7 * E(19, 20) = 1 + 0.3 * 1.7 + 0.7 * 1.3 = 1 + 0.51 + 0.91 = 2.42.
E(18, 20) = 1 + 0.3 * E(19, 20) + 0.7 * 0 = 1 + 0.3 * 1.3 = 1.39.

This is doable but tedious for a 21x21 grid. Let me see if there's a pattern.

Actually, let me think about this problem more carefully. The answer is likely not a "nice" closed form, and the problem probably expects a numerical answer. Let me try to compute it more carefully.

Let me go back to the formula:
E[N] = 100 - 21 * [(1/0.3) * A + (1/0.7) * B]

where A = P(Bin(42, 0.3) ≤ 21), B = P(Bin(42, 0.3) ≥ 21), and A + B = 1 + p where p = P(Bin(42, 0.3) = 21).

E[N] = 100 - 21 * [A/0.3 + B/0.7]
= 100 - 21 * [(7A + 3B) / 2.1]
= 100 - 10 * (7A + 3B)
= 100 - 10 * (7A + 3(1 + p - A))
= 100 - 10 * (4A + 3 + 3p)
= 100 - 40A - 30 - 30p
= 70 - 40A - 30p.

Now I need A and p. Let me compute B = P(Bin(42, 0.3) ≥ 21) = sum_{k=21}^{42} C(42,k) 0.3^k 0.7^{42-k}.

Let me compute this sum. The dominant terms will be around k = 21 (since the mean is 12.6, 21 is far in the right tail).

Let me compute the ratio of consecutive terms: r(k) = P(k+1)/P(k) = [(42-k)/(k+1)] * (0.3/0.7) = [(42-k)/(k+1)] * (3/7).

At k = 21: r(21) = (21/22) * (3/7) = 63/154 ≈ 0.409.
At k = 22: r(22) = (20/23) * (3/7) = 60/161 ≈ 0.373.
At k = 23: r(23) = (19/24) * (3/7) = 57/168 ≈ 0.339.

So the terms decrease rapidly. B ≈ p * (1 + 0.409 + 0.409*0.373 + ...) ≈ p * (1 + 0.409 + 0.153 + 0.052 + ...) ≈ p * 1.62 or so.

Let me compute p = C(42, 21) * 0.3^21 * 0.7^21.

C(42, 21) = 42! / (21! * 21!). This is a large number. Let me compute it.

C(42, 21) = 538257874440.

Let me verify: C(42, 21) is known to be 538257874440. Actually, let me compute it step by step.

C(42, 21) = product_{i=1}^{21} (42-21+i)/i = product_{i=1}^{21} (21+i)/i.

= (22/1)(23/2)(24/3)(25/4)(26/5)(27/6)(28/7)(29/8)(30/9)(31/10)(32/11)(33/12)(34/13)(35/14)(36/15)(37/16)(38/17)(39/18)(40/19)(41/20)(42/21)

= 22 * 11.5 * 8 * 6.25 * 5.2 * 4.5 * 4 * 3.625 * 3.333... * 3.1 * 2.909... * 2.75 * 2.615... * 2.5 * 2.4 * 2.3125 * 2.235... * 2.1667 * 2.105... * 2.05 * 2

This is getting messy. Let me just use the known value. C(42, 21) = 538,257,874,440. (I'm fairly confident about this.)

Actually, let me compute it differently. C(2n, n) for n=21:
C(2,1) = 2
C(4,2) = 6
C(6,3) = 20
C(8,4) = 70
C(10,5) = 252
C(12,6) = 924
C(14,7) = 3432
C(16,8) = 12870
C(18,9) = 48620
C(20,10) = 184756
C(22,11) = 705432
C(24,12) = 2704156
C(26,13) = 10400600
C(28,14) = 40116600
C(30,15) = 155117520
C(32,16) = 601080390
C(34,17) = 2333606220
C(36,18) = 9075135300
C(38,19) = 35345263800
C(40,20) = 137846528820
C(42,21) = 538257874440

Yes, C(42, 21) = 538,257,874,440.

Now, 0.3^21 * 0.7^21 = (0.21)^21.

0.21^21. Let me compute this.
0.21^1 = 0.21
0.21^2 = 0.0441
0.21^3 = 0.009261
0.21^4 = 0.00194481
0.21^5 = 0.0004084101
0.21^6 = 0.000085766121
0.21^7 = 0.00001801088541
0.21^8 = 0.0000037822859361
0.21^9 = 0.000000794280046581
0.21^10 = 0.00000016679880978201
0.21^11 = 0.000000035027750054221
0.21^12 = 0.0000000073558275113864
0.21^13 = 0.00000000154472377739114
0.21^14 = 0.00000000032439199325214
0.21^15 = 0.00000000006812231858295
0.21^16 = 0.00000000001430568690242
0.21^17 = 0.00000000000300419424951
0.21^18 = 0.00000000000063088079240
0.21^19 = 0.00000000000013248496640
0.21^20 = 0.00000000000002782184294
0.21^21 = 0.00000000000000584258702

So (0.21)^21 ≈ 5.8426 × 10^{-15}.

p = C(42, 21) * (0.21)^21 = 538257874440 * 5.8426e-15 ≈ 538257874440 * 5.8426e-15.

538257874440 * 5.8426e-15 = 5.38258e11 * 5.8426e-15 = 5.38258 * 5.8426 * 10^{-4} = 31.449 * 10^{-4} = 0.0031449.

Let me be more precise: 538257874440 * 5.84258702e-15.

538257874440 * 5.84258702 = ?
538257874440 * 5 = 2691289372200
538257874440 * 0.8 = 430606299552
538257874440 * 0.04 = 21530314977.6
538257874440 * 0.002 = 1076515748.88
538257874440 * 0.0005 = 269128937.22
538257874440 * 0.00008 = 43060629.9552
538257874440 * 0.000007 = 3767805.12108
538257874440 * 0.00000002 = 10765.157488

Adding: 2691289372200 + 430606299552 + 21530314977.6 + 1076515748.88 + 269128937.22 + 43060629.9552 + 3767805.12108 + 10765.157488 ≈ 

2691289372200
+ 430606299552 = 3121895671752
+ 21530314977.6 = 3143425986729.6
+ 1076515748.88 = 3144502502478.48
+ 269128937.22 = 3144771631415.7
+ 43060629.9552 = 3144814692045.655
+ 3767805.12108 = 3144818459850.776
+ 10765.157488 = 3144818470615.933

So 538257874440 * 5.84258702 ≈ 3.144818e12.

Then * 10^{-15} = 3.144818e-3 = 0.00314482.

So p ≈ 0.0031448.

Now I need B = P(Bin(42, 0.3) ≥ 21) = p + P(=22) + P(=23) + ...

P(=22) = P(=21) * r(21) = p * (21/22) * (3/7) = p * 63/154 = p * 0.40909...

P(=22) = 0.0031448 * 0.40909 = 0.0012865.

P(=23) = P(=22) * r(22) = 0.0012865 * (20/23) * (3/7) = 0.0012865 * 60/161 = 0.0012865 * 0.37267 = 0.0004795.

P(=24) = P(=23) * r(23) = 0.0004795 * (19/24) * (3/7) = 0.0004795 * 57/168 = 0.0004795 * 0.33929 = 0.0001627.

P(=25) = 0.0001627 * (18/25) * (3/7) = 0.0001627 * 54/175 = 0.0001627 * 0.30857 = 0.0000502.

P(=26) = 0.0000502 * (17/26) * (3/7) = 0.0000502 * 51/182 = 0.0000502 * 0.28022 = 0.00001407.

P(=27) = 0.00001407 * (16/27) * (3/7) = 0.00001407 * 48/189 = 0.00001407 * 0.25397 = 0.000003574.

P(=28) = 0.000003574 * (15/28) * (3/7) = 0.000003574 * 45/196 = 0.000003574 * 0.22959 = 0.0000008206.

P(=29) = 0.0000008206 * (14/29) * (3/7) = 0.0000008206 * 42/203 = 0.0000008206 * 0.20690 = 0.0000001698.

P(=30) = 0.0000001698 * (13/30) * (3/7) = 0.0000001698 * 39/210 = 0.0000001698 * 0.18571 = 0.00000003154.

Remaining terms are negligible.

B ≈ 0.0031448 + 0.0012865 + 0.0004795 + 0.0001627 + 0.0000502 + 0.00001407 + 0.000003574 + 0.0000008206 + 0.0000001698 + 0.00000003154 + ...

= 0.0031448 + 0.0012865 = 0.0044313
+ 0.0004795 = 0.0049108
+ 0.0001627 = 0.0050735
+ 0.0000502 = 0.0051237
+ 0.00001407 = 0.0051378
+ 0.000003574 = 0.0051413
+ 0.0000008206 = 0.0051422
+ 0.0000001698 = 0.0051423
+ 0.00000003154 = 0.0051424

So B ≈ 0.0051424.

A = 1 + p - B = 1 + 0.0031448 - 0.0051424 = 0.9980024.

E[N] = 70 - 40 * A - 30 * p = 70 - 40 * 0.9980024 - 30 * 0.0031448
= 70 - 39.920096 - 0.094344
= 70 - 40.01444
= 29.98556.

Hmm, so E[N] ≈ 29.986. That's very close to 30 but not exactly 30.

Wait, let me double-check my formula. Let me re-derive.

E[N] = 21 * sum_{k=0}^{20} C(21+k, k) * [0.3^21 * 0.7^k + 0.7^21 * 0.3^k].

Let me verify with a simple case. Suppose r = 1 (race to 1). Then:
E[N] = 1 * sum_{k=0}^{0} C(1+k, k) * [p^1 * q^k + q^1 * p^k] = 1 * C(1,0) * [p + q] = p + q = 1. ✓

Suppose r = 2 (race to 2), p = 0.3, q = 0.7.
E[N] = 2 * sum_{k=0}^{1} C(2+k, k) * [0.3^2 * 0.7^k + 0.7^2 * 0.3^k].
k=0: C(2,0) * [0.09 + 0.49] = 1 * 0.58 = 0.58.
k=1: C(3,1) * [0.09 * 0.7 + 0.49 * 0.3] = 3 * [0.063 + 0.147] = 3 * 0.21 = 0.63.
E[N] = 2 * (0.58 + 0.63) = 2 * 1.21 = 2.42.

Let me verify by direct computation. Race to 2:
- AA: 2 games, prob 0.09
- BB: 2 games, prob 0.49
- ABA: 3 games, prob 0.3*0.7*0.3 = 0.063
- ABB: 3 games, prob 0.3*0.7*0.7 = 0.147
- BAA: 3 games, prob 0.7*0.3*0.3 = 0.063
- BAB: 3 games, prob 0.7*0.3*0.7 = 0.147

Wait, let me be more careful. Race to 2: the match ends when someone gets 2 wins.
- 2 games: AA (0.09) or BB (0.49). Total prob 0.58.
- 3 games: the first 2 games are split (AB or BA), then the 3rd game decides.
  - AB then A: 0.3*0.7*0.3 = 0.063
  - AB then B: 0.3*0.7*0.7 = 0.147
  - BA then A: 0.7*0.3*0.3 = 0.063
  - BA then B: 0.7*0.3*0.7 = 0.147
  Total prob for 3 games: 0.063+0.147+0.063+0.147 = 0.42.

E[N] = 2*0.58 + 3*0.42 = 1.16 + 1.26 = 2.42. ✓

Great, the formula works.

Now let me verify the alternative formula for r=2:
E[N] = 100... no wait, that was specific to r=21. Let me re-derive for general r.

E[N] = r * sum_{k=0}^{r-1} C(r+k, k) * [p^r * q^k + q^r * p^k].

Using the identity sum_{k=0}^{inf} C(r+k, k) x^k = 1/(1-x)^{r+1}:

sum_{k=0}^{r-1} C(r+k, k) p^r q^k = p^r * [1/(1-q)^{r+1} - sum_{k=r}^{inf} C(r+k, k) q^k]
= p^r / p^{r+1} - p^r * sum_{k=r}^{inf} C(r+k, k) q^k
= 1/p - p^r * sum_{k=r}^{inf} C(r+k, k) q^k.

Similarly, sum_{k=0}^{r-1} C(r+k, k) q^r p^k = 1/q - q^r * sum_{k=r}^{inf} C(r+k, k) p^k.

E[N] = r * [1/p + 1/q - p^r * sum_{k=r}^{inf} C(r+k, k) q^k - q^r * sum_{k=r}^{inf} C(r+k, k) p^k].

For r = 21, p = 0.3, q = 0.7:
1/p + 1/q = 10/3 + 10/7 = 100/21.
E[N] = 21 * [100/21 - 0.3^21 * T_q - 0.7^21 * T_p]
= 100 - 21 * [0.3^21 * T_q + 0.7^21 * T_p]

where T_q = sum_{k=21}^{inf} C(21+k, k) * 0.7^k and T_p = sum_{k=21}^{inf} C(21+k, k) * 0.3^k.

Now, 0.3^21 * T_q = 0.3^21 * sum_{k=21}^{inf} C(21+k, k) * 0.7^k = sum_{k=21}^{inf} C(21+k, 21) * 0.3^21 * 0.7^k.

This is (1/0.3) * sum_{k=21}^{inf} C(21+k, 21) * 0.3^22 * 0.7^k = (1/0.3) * P(22nd success at trial ≥ 22+21=43) = (1/0.3) * P(Bin(42, 0.3) ≤ 21).

Wait, let me recheck. The 22nd success occurs at trial 22+k with probability C(21+k, 21) * 0.3^22 * 0.7^k. The 22nd success occurs at trial ≥ 43 iff in the first 42 trials, there are at most 21 successes, i.e., P(Bin(42, 0.3) ≤ 21).

So sum_{k=21}^{inf} C(21+k, 21) * 0.3^22 * 0.7^k = P(Bin(42, 0.3) ≤ 21) = A.

Therefore 0.3^21 * T_q = A / 0.3.

Similarly, 0.7^21 * T_p = B / 0.7 where B = P(Bin(42, 0.7) ≤ 21) = P(Bin(42, 0.3) ≥ 21).

So E[N] = 100 - 21 * [A/0.3 + B/0.7] = 100 - 21 * [(7A + 3B)/2.1] = 100 - 10(7A + 3B).

With A + B = 1 + p (where p = P(Bin(42, 0.3) = 21)):
7A + 3B = 7A + 3(1 + p - A) = 4A + 3 + 3p.
E[N] = 100 - 10(4A + 3 + 3p) = 100 - 40A - 30 - 30p = 70 - 40A - 30p.

Now, A = P(Bin(42, 0.3) ≤ 21) = 1 - P(Bin(42, 0.3) ≥ 22) = 1 - (B - p) = 1 - B + p.

So E[N] = 70 - 40(1 - B + p) - 30p = 70 - 40 + 40B - 40p - 30p = 30 + 40B - 70p.

Let me verify: E[N] = 30 + 40B - 70p where B = P(Bin(42, 0.3) ≥ 21) and p = P(Bin(42, 0.3) = 21).

With B ≈ 0.0051424 and p ≈ 0.0031448:
E[N] = 30 + 40 * 0.0051424 - 70 * 0.0031448
= 30 + 0.205696 - 0.220136
= 30 - 0.01444
= 29.98556.

So E[N] ≈ 29.986.

Hmm, this is very close to 30 but not exactly 30. Let me double-check my computation of p and B more carefully.

Let me recompute p = C(42, 21) * 0.3^21 * 0.7^21 = C(42, 21) * (0.21)^21.

C(42, 21) = 538257874440.

(0.21)^21: Let me compute more carefully.
0.21^2 = 0.0441
0.21^4 = 0.0441^2 = 0.00194481
0.21^8 = 0.00194481^2 = 0.0000037822859361
0.21^16 = 0.0000037822859361^2 = 1.43056869e-11

0.21^21 = 0.21^16 * 0.21^4 * 0.21^1 = 1.43056869e-11 * 0.00194481 * 0.21
= 1.43056869e-11 * 0.00194481 = 2.78218e-14
* 0.21 = 5.84259e-15

So (0.21)^21 = 5.84259 × 10^{-15}.

p = 538257874440 * 5.84259e-15 = 538257874440 * 5.84259 * 10^{-15}.

538257874440 * 5.84259:
538257874440 * 5 = 2691289372200
538257874440 * 0.8 = 430606299552
538257874440 * 0.04 = 21530314977.6
538257874440 * 0.002 = 1076515748.88
538257874440 * 0.0005 = 269128937.22
538257874440 * 0.00009 = 48443208.7
538257874440 * 0.000009 = 4844320.87

Sum: 2691289372200 + 430606299552 + 21530314977.6 + 1076515748.88 + 269128937.22 + 48443208.7 + 4844320.87

= 2691289372200
+ 430606299552 = 3121895671752
+ 21530314977.6 = 3143425986729.6
+ 1076515748.88 = 3144502502478.5
+ 269128937.22 = 3144771631415.7
+ 48443208.7 = 3144820074624.4
+ 4844320.87 = 3144824918945.3

So 538257874440 * 5.84259 ≈ 3.14482 × 10^{12}.

p = 3.14482 × 10^{12} × 10^{-15} = 3.14482 × 10^{-3} = 0.00314482.

OK so p ≈ 0.00314482. This matches my earlier calculation.

Now for B, let me recompute more carefully.

B = P(Bin(42, 0.3) ≥ 21) = sum_{k=21}^{42} C(42,k) 0.3^k 0.7^{42-k}.

Let me compute the terms using the ratio method, starting from k=21.

P(21) = p = 0.00314482.

P(22)/P(21) = (42-21)/(21+1) * 0.3/0.7 = 21/22 * 3/7 = 63/154.
63/154 = 0.409090909...
P(22) = 0.00314482 * 0.40909091 = 0.00128651.

P(23)/P(22) = (42-22)/(22+1) * 3/7 = 20/23 * 3/7 = 60/161 = 0.372670807...
P(23) = 0.00128651 * 0.37267081 = 0.00047945.

P(24)/P(23) = 19/24 * 3/7 = 57/168 = 0.339285714...
P(24) = 0.00047945 * 0.33928571 = 0.00016270.

P(25)/P(24) = 18/25 * 3/7 = 54/175 = 0.308571429...
P(25) = 0.00016270 * 0.30857143 = 0.000050205.

P(26)/P(25) = 17/26 * 3/7 = 51/182 = 0.280219780...
P(26) = 0.000050205 * 0.28021978 = 0.000014069.

P(27)/P(26) = 16/27 * 3/7 = 48/189 = 16/63 = 0.253968254...
P(27) = 0.000014069 * 0.25396825 = 0.000003573.

P(28)/P(27) = 15/28 * 3/7 = 45/196 = 0.229591837...
P(28) = 0.000003573 * 0.22959184 = 0.0000008203.

P(29)/P(28) = 14/29 * 3/7 = 42/203 = 0.206896552...
P(29) = 0.0000008203 * 0.20689655 = 0.0000001697.

P(30)/P(29) = 13/30 * 3/7 = 39/210 = 0.185714286...
P(30) = 0.0000001697 * 0.18571429 = 0.00000003152.

P(31)/P(30) = 12/31 * 3/7 = 36/217 = 0.165898618...
P(31) = 0.00000003152 * 0.16589862 = 0.00000000523.

P(32)/P(31) = 11/32 * 3/7 = 33/224 = 0.147321429...
P(32) = 0.00000000523 * 0.14732143 = 0.00000000077.

Remaining terms negligible.

B = 0.00314482 + 0.00128651 + 0.00047945 + 0.00016270 + 0.000050205 + 0.000014069 + 0.000003573 + 0.0000008203 + 0.0000001697 + 0.00000003152 + 0.00000000523 + 0.00000000077

Let me add these up:
0.00314482
+ 0.00128651 = 0.00443133
+ 0.00047945 = 0.00491078
+ 0.00016270 = 0.00507348
+ 0.000050205 = 0.00512369
+ 0.000014069 = 0.00513775
+ 0.000003573 = 0.00514133
+ 0.0000008203 = 0.00514215
+ 0.0000001697 = 0.00514232
+ 0.00000003152 = 0.00514235
+ 0.00000000523 = 0.00514235
+ 0.00000000077 = 0.00514235

B ≈ 0.00514235.

E[N] = 30 + 40 * 0.00514235 - 70 * 0.00314482
= 30 + 0.205694 - 0.220137
= 30 - 0.014443
= 29.985557.

So E[N] ≈ 29.986.

Hmm, but this doesn't seem like a "clean" answer. Let me reconsider whether the problem is asking for an exact closed-form or a numerical answer.

The problem says "What is the expected value of the number of games played per match?" This is a standard probability problem. Given the parameters (30%, 70%, 21 games), the answer is likely a specific numerical value.

Let me reconsider. Maybe I should express the answer as a formula or compute it more precisely.

Actually, wait. Let me reconsider the problem. Maybe the answer is supposed to be expressed as a sum or formula, not a decimal. Or maybe there's a cleaner form.

Let me reconsider: E[N] = 30 + 40B - 70p where B = P(Bin(42, 0.3) ≥ 21) and p = P(Bin(42, 0.3) = 21).

Alternatively, E[N] = 30 + 40 * P(Bin(42, 0.3) ≥ 21) - 70 * P(Bin(42, 0.3) = 21).

= 30 + 40 * [P(Bin(42, 0.3) ≥ 21)] - 70 * [P(Bin(42, 0.3) = 21)]

= 30 + 40 * P(Bin(42, 0.3) ≥ 22) + 40 * P(Bin(42, 0.3) = 21) - 70 * P(Bin(42, 0.3) = 21)

= 30 + 40 * P(Bin(42, 0.3) ≥ 22) - 30 * P(Bin(42, 0.3) = 21).

Hmm, not obviously cleaner.

Let me try yet another form. E[N] = 30 + 40B - 70p.

Note that B = P(Bin(42, 0.3) ≥ 21) and p = P(Bin(42, 0.3) = 21).

40B - 70p = 40 * P(≥ 21) - 70 * P(= 21) = 40 * P(≥ 22) + 40 * P(= 21) - 70 * P(= 21) = 40 * P(≥ 22) - 30 * P(= 21).

So E[N] = 30 + 40 * P(Bin(42, 0.3) ≥ 22) - 30 * P(Bin(42, 0.3) = 21).

P(Bin(42, 0.3) ≥ 22) = B - p = 0.00514235 - 0.00314482 = 0.00199753.

E[N] = 30 + 40 * 0.00199753 - 30 * 0.00314482 = 30 + 0.079901 - 0.094345 = 29.985556.

So E[N] ≈ 29.986.

Actually, I wonder if the problem expects an exact answer. Let me reconsider.

The problem is from a math competition or textbook. Given the specific numbers (30%, 70%, 21), the answer might be expected as a decimal or as a formula.

Let me try to see if the answer simplifies to something nice. We have:

E[N] = 100 - 10(7A + 3B) where A = P(Bin(42, 0.3) ≤ 21), B = P(Bin(42, 0.3) ≥ 21).

Or equivalently, E[N] = 30 + 40B - 70p.

I don't think this simplifies to a nice closed form. The answer is approximately 29.986.

But wait, let me reconsider. Maybe I should double-check my formula by computing E[N] for a small case and comparing.

For r = 2, p = 0.3, q = 0.7:
E[N] = 2 * [1/0.3 + 1/0.7 - 0.3^2 * T_q - 0.7^2 * T_p]

where T_q = sum_{k=2}^{inf} C(2+k, k) * 0.7^k and T_p = sum_{k=2}^{inf} C(2+k, k) * 0.3^k.

1/0.3 + 1/0.7 = 10/3 + 10/7 = 100/21.

0.3^2 * T_q = (1/0.3) * P(Bin(4, 0.3) ≤ 1) [since 2r-2 = 2, so we need P(Bin(2*2-2, 0.3) ≤ r-1) = P(Bin(2, 0.3) ≤ 1)].

Wait, I need to recheck the general formula. For general r:
0.p^r * T_q = (1/p) * P(Bin(2r, p) ≤ r-1) ... let me re-derive.

Actually, for general r, the tail sum is:
p^r * sum_{k=r}^{inf} C(r+k, k) q^k = (1/p) * P(Bin(2r, p) ≤ r-1).

Wait, let me re-derive. sum_{k=r}^{inf} C(r+k, r) p^{r+1} q^k = P((r+1)th success at trial ≥ r+1+r+1 = 2r+2) ... no.

Hmm, let me be more careful. C(r+k, r) p^{r+1} q^k is the probability that the (r+1)th success occurs at trial (r+1+k). The (r+1)th success occurs at trial ≥ (r+1+r) = 2r+1 iff in the first 2r trials, there are at most r successes.

Wait, (r+1)th success at trial (r+1+k) means k failures among the first r+k trials, with the last trial being a success. For this to be at trial ≥ 2r+1, we need r+1+k ≥ 2r+1, i.e., k ≥ r.

P((r+1)th success at trial ≥ 2r+1) = P(Bin(2r, p) ≤ r) [at most r successes in first 2r trials].

So sum_{k=r}^{inf} C(r+k, r) p^{r+1} q^k = P(Bin(2r, p) ≤ r).

Therefore p^r * sum_{k=r}^{inf} C(r+k, r) q^k = (1/p) * P(Bin(2r, p) ≤ r).

For r = 21: p^r * T_q = (1/0.3) * P(Bin(42, 0.3) ≤ 21) = A/0.3. ✓ (This matches what I had before, since r = 21 and we need P(Bin(42, 0.3) ≤ 21).)

For r = 2: p^r * T_q = (1/0.3) * P(Bin(4, 0.3) ≤ 2).

P(Bin(4, 0.3) ≤ 2) = 1 - P(Bin(4, 0.3) ≥ 3) = 1 - [C(4,3)*0.3^3*0.7 + 0.3^4] = 1 - [4*0.027*0.7 + 0.0081] = 1 - [0.0756 + 0.0081] = 1 - 0.0837 = 0.9163.

0.3^2 * T_q = 0.9163/0.3 = 3.054333...

Similarly, q^r * T_p = (1/0.7) * P(Bin(4, 0.7) ≤ 2) = (1/0.7) * P(Bin(4, 0.3) ≥ 2).

P(Bin(4, 0.3) ≥ 2) = 1 - P(Bin(4, 0.3) ≤ 1) = 1 - [0.7^4 + 4*0.3*0.7^3] = 1 - [0.2401 + 4*0.3*0.343] = 1 - [0.2401 + 0.4116] = 1 - 0.6517 = 0.3483.

0.7^2 * T_p = 0.3483/0.7 = 0.497571...

E[N] = 2 * [100/21 - 3.054333 - 0.497571] = 2 * [4.761905 - 3.054333 - 0.497571] = 2 * 1.210001 = 2.420002.

And we computed E[N] = 2.42 directly. ✓ 

So the formula is correct. Now for r = 21:

E[N] = 21 * [100/21 - A/0.3 - B/0.7] = 100 - 21 * [A/0.3 + B/0.7] = 100 - 10(7A + 3B).

With A = P(Bin(42, 0.3) ≤ 21) ≈ 0.998002 and B = P(Bin(42, 0.3) ≥ 21) ≈ 0.005142:

7A + 3B = 7 * 0.998002 + 3 * 0.005142 = 6.986014 + 0.015426 = 7.001440.

E[N] = 100 - 10 * 7.001440 = 100 - 70.01440 = 29.98560.

So E[N] ≈ 29.986.

Hmm, let me reconsider whether this problem has a clean answer. The fact that it's so close to 30 is suspicious. Let me check: is there a reason it should be exactly 30?

For the symmetric case p = q = 0.5, race to r:
E[N] = r * [1/0.5 + 1/0.5 - 2 * (1/0.5) * P(Bin(2r, 0.5) ≤ r-1)]
Wait, by symmetry A = B = P(Bin(2r, 0.5) ≥ r) and p = P(Bin(2r, 0.5) = r).

Actually for p = q = 0.5:
A = P(Bin(2r, 0.5) ≤ r) and B = P(Bin(2r, 0.5) ≥ r). By symmetry A = B = 1/2 + p/2 where p = P(Bin(2r, 0.5) = r).

E[N] = 100... no, for general r with p = q = 0.5:
E[N] = r * [2/0.5 - 2 * (1/0.5) * P(Bin(2r, 0.5) ≤ r)] = r * [4 - 4 * P(Bin(2r, 0.5) ≤ r)].

Hmm, this doesn't simplify to a nice number either.

For the asymmetric case, the answer 29.986 doesn't seem to be a clean number. Let me reconsider whether the problem might have a different interpretation or whether I should express the answer differently.

Actually, looking at the problem again: "What is the expected value of the number of games played per match?" This is a straightforward expected value question. Given the specific parameters, the answer is a specific number. Let me compute it more precisely.

Let me try to compute E[N] to more decimal places.

E[N] = 30 + 40B - 70p.

I need more precise values of B and p.

p = C(42, 21) * (0.21)^21.

Let me compute (0.21)^21 more precisely.

0.21 = 21/100.

(21/100)^21 = 21^21 / 100^21.

21^21 = 21^20 * 21.
21^1 = 21
21^2 = 441
21^3 = 9261
21^4 = 194481
21^5 = 4084101
21^6 = 85766121
21^7 = 1801088541
21^8 = 37822859361
21^9 = 794280946281
21^10 = 16679880977841
21^11 = 350277500534661
21^12 = 7355827511227881
21^13 = 154472377715785481
21^14 = 3243919932531494881 (hmm, let me double check)

Actually, this is getting very large. Let me use a different approach.

Let me compute p = C(42,21) * 0.3^21 * 0.7^21 using logarithms.

ln(p) = ln(C(42,21)) + 21*ln(0.3) + 21*ln(0.7).

ln(0.3) = ln(3) - ln(10) = 1.098612 - 2.302585 = -1.203973.
ln(0.7) = ln(7) - ln(10) = 1.945910 - 2.302585 = -0.356675.

21 * ln(0.3) = -25.28343.
21 * ln(0.7) = -7.49017.

Sum = -32.77360.

ln(C(42,21)): C(42,21) = 538257874440.
ln(538257874440) = ln(5.38258 × 10^{11}) = ln(5.38258) + 11*ln(10) = 1.68312 + 25.32844 = 27.01156.

ln(p) = 27.01156 - 32.77360 = -5.762
