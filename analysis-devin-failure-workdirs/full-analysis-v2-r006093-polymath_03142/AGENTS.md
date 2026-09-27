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
  <problem_id>polymath_03142</problem_id>
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

Given an integer \( n \ge 2 \), find the maximal constant \( \lambda(n) \) such that for any sequence of real numbers \( a_0, a_1, a_2, \ldots, a_n \) satisfying \( 0 = a_0 \le a_1 \le a_2 \le \cdots \le a_n \) and \( a_i \ge \frac{1}{2}(a_{i+1} + a_{i-1}) \) for \( i = 1, 2, \ldots, n-1 \), the inequality \( \left( \sum_{i=1}^n i a_i \right)^2 \ge \lambda(n) \sum_{i=1}^n a_i^2 \) holds.

## Standard Solution

To find the maximal constant \(\lambda(n)\) such that for any sequence of real numbers \(a_0, a_1, a_2, \ldots, a_n\) satisfying \(0 = a_0 \le a_1 \le a_2 \le \cdots \le a_n\) and \(a_i \ge \frac{1}{2}(a_{i+1} + a_{i-1})\) for \(i = 1, 2, \ldots, n-1\), the inequality \(\left( \sum_{i=1}^n i a_i \right)^2 \ge \lambda(n) \sum_{i=1}^n a_i^2\) holds, we proceed as follows:

### Step 1: Understanding the Constraints
The sequence \(a_0, a_1, \ldots, a_n\) is non-decreasing, and the concavity condition \(a_i \ge \frac{1}{2}(a_{i+1} + a_{i-1})\) implies that the differences \(d_i = a_i - a_{i-1}\) are non-negative and non-increasing.

### Step 2: Expressing the Problem in Terms of Differences
Let \(d_i = a_i - a_{i-1}\) for \(i = 1, 2, \ldots, n\). These differences must satisfy:
- \(d_i \ge 0\)
- \(d_i \ge d_{i+1}\)

The sequence \(a_i\) can be written as:
\[ a_i = \sum_{k=1}^i d_k \]

### Step 3: Formulating the Ratio
We need to minimize the ratio:
\[ \frac{\left( \sum_{i=1}^n i a_i \right)^2}{\sum_{i=1}^n a_i^2} \]

### Step 4: Analyzing the Minimal Ratio
We observe that the minimal ratio occurs when the sequence \(a_i\) is constant from \(a_1\) onwards, i.e., \(a_i = d\) for \(i \ge 1\). This means:
\[ d_1 = d, \quad d_2 = 0, \quad d_3 = 0, \quad \ldots, \quad d_n = 0 \]

### Step 5: Calculating the Ratio for the Constant Sequence
For this specific sequence:
\[ a_i = d \quad \text{for} \quad i = 1, 2, \ldots, n \]

The numerator becomes:
\[ \sum_{i=1}^n i a_i = d \sum_{i=1}^n i = d \cdot \frac{n(n+1)}{2} \]

The denominator becomes:
\[ \sum_{i=1}^n a_i^2 = \sum_{i=1}^n d^2 = n d^2 \]

Thus, the ratio is:
\[ \frac{\left( d \cdot \frac{n(n+1)}{2} \right)^2}{n d^2} = \frac{d^2 \cdot \left( \frac{n(n+1)}{2} \right)^2}{n d^2} = \frac{\left( \frac{n(n+1)}{2} \right)^2}{n} = \frac{n^2(n+1)^2}{4n} = \frac{n(n+1)^2}{4} \]

### Step 6: Verifying the Minimal Ratio
We need to verify that no other configuration of \(d_i\) can yield a lower ratio. By testing other configurations (e.g., non-zero differences), we confirm that the minimal ratio is indeed achieved when the sequence is constant from \(a_1\) onwards.

### Conclusion
The maximal constant \(\lambda(n)\) is:
\[ \boxed{\frac{n(n+1)^2}{4}} \]

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have a sequence $a_0, a_1, \ldots, a_n$ with $0 = a_0 \le a_1 \le \cdots \le a_n$ and the concavity condition $a_i \ge \frac{1}{2}(a_{i+1} + a_{i-1})$ for $i = 1, \ldots, n-1$. We need to find the maximal $\lambda(n)$ such that $(\sum_{i=1}^n i a_i)^2 \ge \lambda(n) \sum_{i=1}^n a_i^2$.

The concavity condition $a_i \ge \frac{1}{2}(a_{i+1} + a_{i-1})$ means $2a_i \ge a_{i+1} + a_{i-1}$, i.e., $a_{i+1} - a_i \le a_i - a_{i-1}$. So the differences $d_i = a_i - a_{i-1}$ are non-increasing: $d_1 \ge d_2 \ge \cdots \ge d_n \ge 0$ (since $a$ is non-decreasing, $d_i \ge 0$).

So $a_i = \sum_{j=1}^i d_j$ where $d_1 \ge d_2 \ge \cdots \ge d_n \ge 0$.

We want to minimize $\frac{(\sum_{i=1}^n i a_i)^2}{\sum_{i=1}^n a_i^2}$ over all such sequences (not all zero).

This is a ratio, so we want to minimize $\frac{(\sum i a_i)^2}{\sum a_i^2}$, which is the square of the cosine-like ratio. Actually we want the infimum of $\frac{(\sum i a_i)^2}{\sum a_i^2}$, and $\lambda(n)$ is that infimum.

Let me think about this as an optimization problem. We want to minimize $R = \frac{(\sum_{i=1}^n i a_i)^2}{\sum_{i=1}^n a_i^2}$.

Since the constraint is a cone (positive combinations of valid sequences are valid), and $R$ is homogeneous of degree 0, we can normalize $\sum a_i^2 = 1$ and minimize $(\sum i a_i)^2$, or equivalently minimize $\sum i a_i$ (since $a_i \ge 0$ and $i > 0$, the sum is non-negative, and we want it as small as possible).

Actually, to minimize $\sum i a_i$ subject to $\sum a_i^2 = 1$ and the cone constraints.

The extreme rays of the cone $\{d: d_1 \ge d_2 \ge \cdots \ge d_n \ge 0\}$ are the vectors $e^{(k)} = (1, 1, \ldots, 1, 0, \ldots, 0)$ (first $k$ entries are 1) for $k = 1, \ldots, n$. So $d = \sum_{k=1}^n c_k e^{(k)}$ with $c_k \ge 0$.

Then $a_i = \sum_{j=1}^i d_j = \sum_{j=1}^i \sum_{k=1}^n c_k e^{(k)}_j = \sum_{k=1}^n c_k \min(i, k)$.

So $a_i = \sum_{k=1}^n c_k \min(i, k)$.

Let $v^{(k)}$ be the vector with $v^{(k)}_i = \min(i, k)$ for $i = 1, \ldots, n$. Then $a = \sum_{k=1}^n c_k v^{(k)}$ with $c_k \ge 0$.

We want to minimize $\frac{(\sum i a_i)^2}{\sum a_i^2} = \frac{(\sum_k c_k \sum_i i v^{(k)}_i)^2}{\sum_{k,l} c_k c_l \sum_i v^{(k)}_i v^{(l)}_i}$.

Let $S_k = \sum_{i=1}^n i \min(i, k)$ and $G_{kl} = \sum_{i=1}^n \min(i,k) \min(i,l)$.

We want to minimize $\frac{(\sum_k c_k S_k)^2}{\sum_{kl} c_k c_l G_{kl}}$ over $c_k \ge 0$ (not all zero).

This is like minimizing the ratio of a linear form squared to a quadratic form, over the positive orthant.

The minimum of $\frac{(c^T S)^2}{c^T G c}$ over $c \ge 0$.

If we could use any $c$ (no sign constraint), the minimum would be 0 (just pick $c$ orthogonal to $S$). But with $c \ge 0$ and $S_k > 0$, $c^T S > 0$, so we're minimizing a positive quantity.

Let $f(c) = \frac{(c^T S)^2}{c^T G c}$. To minimize, take derivative. At the optimum (interior), $\nabla f = 0$ gives $2(c^T S) S (c^T G c) - (c^T S)^2 \cdot 2 G c = 0$, so $S (c^T G c) = (c^T S) G c$, i.e., $Gc = \frac{c^T G c}{c^T S} S$, so $Gc \propto S$.

But the optimum might be on the boundary (some $c_k = 0$).

Actually, let me think about this differently. The minimum of $\frac{(c^T S)^2}{c^T G c}$ over $c \ge 0$ equals $\left(\min_{c \ge 0, c^T G c = 1} c^T S\right)^2$.

Hmm, this is getting complex. Let me try small cases.

**Case $n = 2$:** $d_1 \ge d_2 \ge 0$. $a_1 = d_1$, $a_2 = d_1 + d_2$. Extreme rays: $c_1$ gives $a = (1, 1)$, $c_2$ gives $a = (1, 2)$.

For $a = (1,1)$: $(\sum i a_i)^2 = (1+2)^2 = 9$, $\sum a_i^2 = 2$, ratio = $9/2$.
For $a = (1,2)$: $(1+4)^2 = 25$, $\sum a_i^2 = 5$, ratio = $5$.
For general $a = c_1(1,1) + c_2(1,2) = (c_1+c_2, c_1+2c_2)$: $\sum i a_i = (c_1+c_2) + 2(c_1+2c_2) = 3c_1 + 5c_2$. $\sum a_i^2 = (c_1+c_2)^2 + (c_1+2c_2)^2 = 2c_1^2 + 6c_1 c_2 + 5c_2^2$.

Ratio = $(3c_1+5c_2)^2 / (2c_1^2 + 6c_1 c_2 + 5c_2^2)$.

Let $t = c_2/c_1 \ge 0$ (and $c_1 > 0$; also consider $c_1 = 0$). Ratio = $(3+5t)^2/(2+6t+5t^2)$.

At $t=0$: $9/2 = 4.5$. At $t \to \infty$: $25/5 = 5$. Derivative: $\frac{d}{dt} \frac{(3+5t)^2}{2+6t+5t^2}$. Numerator derivative: $2(3+5t) \cdot 5 \cdot (2+6t+5t^2) - (3+5t)^2(6+10t)$. Set to 0: $10(2+6t+5t^2) = (3+5t)(6+10t) = 18 + 50t + 50t^2$. So $20 + 60t + 50t^2 = 18 + 50t + 50t^2$, giving $2 + 10t = 0$, $t = -1/5 < 0$. So no critical point in $t \ge 0$, and the ratio is increasing. Minimum at $t = 0$: $\lambda(2) = 9/2$.

So $\lambda(2) = 9/2$, achieved by $a = (1, 1)$, i.e., $d = (1, 0)$, i.e., $a_1 = a_2 = 1$.

**Case $n = 3$:** Extreme rays $v^{(1)} = (1,1,1)$, $v^{(2)} = (1,2,2)$, $v^{(3)} = (1,2,3)$.

$S_1 = 1+2+3 = 6$, $S_2 = 1+4+6 = 11$, $S_3 = 1+4+9 = 14$.

$G_{11} = 3$, $G_{22} = 1+4+4 = 9$, $G_{33} = 1+4+9 = 14$.
$G_{12} = 1+2+2 = 5$, $G_{13} = 1+2+3 = 6$, $G_{23} = 1+4+6 = 11$.

Ratio = $(6c_1 + 11c_2 + 14c_3)^2 / (3c_1^2 + 9c_2^2 + 14c_3^2 + 10c_1 c_2 + 12c_1 c_3 + 22c_2 c_3)$.

Let me try $c_2 = c_3 = 0$: ratio = $36/3 = 12$.
Try $c_1 = 0, c_3 = 0$: ratio = $121/9 \approx 13.44$.
Try $c_1 = 0, c_2 = 0$: ratio = $196/14 = 14$.

So the minimum among extreme rays is 12 (from $v^{(1)}$). But combinations might do better.

Let me try $c_1 = 1, c_2 = t, c_3 = 0$. Ratio = $(6+11t)^2/(3+10t+9t^2)$.
Derivative: $22(3+10t+9t^2) - (6+11t)(10+18t) = 0$. $66 + 220t + 198t^2 = 60 + 108t + 110t + 198t^2 = 60 + 218t + 198t^2$. So $66 + 220t = 60 + 218t$, $6 + 2t = 0$, $t = -3$. Negative, so ratio increasing for $t \ge 0$. Min at $t=0$: 12.

Try $c_1 = 1, c_2 = 0, c_3 = t$. Ratio = $(6+14t)^2/(3+12t+14t^2)$.
Derivative: $28(3+12t+14t^2) - (6+14t)(12+28t) = 0$. $84 + 336t + 392t^2 = 72 + 168t + 168t + 392t^2 = 72 + 336t + 392t^2$. So $84 = 72$, impossible. So $12 > 0$, ratio increasing. Min at $t=0$: 12.

Try $c_1 = 0, c_2 = 1, c_3 = t$. Ratio = $(11+14t)^2/(9+22t+14t^2)$.
Derivative: $28(9+22t+14t^2) - (11+14t)(22+28t) = 0$. $252 + 616t + 392t^2 = 242 + 308t + 392t + 392t^2 = 242 + 700t + 392t^2$. So $252 + 616t = 242 + 700t$, $10 = 84t$, $t = 10/84 = 5/42 \approx 0.119$.

At $t = 5/42$: ratio = $(11 + 14 \cdot 5/42)^2 / (9 + 22 \cdot 5/42 + 14 \cdot 25/1764)$.
$14 \cdot 5/42 = 70/42 = 5/3$. So numerator: $(11 + 5/3)^2 = (38/3)^2 = 1444/9$.
$22 \cdot 5/42 = 110/42 = 55/21$. $14 \cdot 25/1764 = 350/1764 = 25/126$.
Denominator: $9 + 55/21 + 25/126 = 1134/126 + 330/126 + 25/126 = 1489/126$.
Ratio = $(1444/9) / (1489/126) = (1444/9) \cdot (126/1489) = 1444 \cdot 14 / 1489 = 20216/1489 \approx 13.577$.

That's bigger than 12, so not better.

Now try all three: $c_1, c_2, c_3$ all positive. The minimum of the ratio over the positive orthant. Let me think about whether the minimum is always at a single extreme ray.

Actually, for $n=2$ and $n=3$, the minimum seems to be at $v^{(1)}$ (the constant sequence $a_i = 1$). For constant $a_i = 1$: $(\sum i)^2 / n = (n(n+1)/2)^2 / n = n(n+1)^2/4$.

For $n=2$: $2 \cdot 9/4 = 9/2$. ✓
For $n=3$: $3 \cdot 16/4 = 12$. ✓

Is the minimum always achieved by the constant sequence? Let me check $n=4$.

$v^{(1)} = (1,1,1,1)$: $S = 1+2+3+4 = 10$, $G = 4$. Ratio = $100/4 = 25$. And $n(n+1)^2/4 = 4 \cdot 25/4 = 25$. ✓

Let me check if any other ray or combination gives less than 25.

$v^{(2)} = (1,2,2,2)$: $S = 1+4+6+8 = 19$, $G = 1+4+4+4 = 13$. Ratio = $361/13 \approx 27.77$.
$v^{(3)} = (1,2,3,3)$: $S = 1+4+9+12 = 26$, $G = 1+4+9+9 = 23$. Ratio = $676/23 \approx 29.39$.
$v^{(4)} = (1,2,3,4)$: $S = 1+4+9+16 = 30$, $G = 1+4+9+16 = 30$. Ratio = $900/30 = 30$.

So among extreme rays, $v^{(1)}$ gives the minimum. But could a combination give less?

Let me try $c_1 = 1, c_2 = t, c_3 = 0, c_4 = 0$ for $n=4$.
$S = 10 + 19t$, $G = 4 + 2 \cdot G_{12} t + 13 t^2$.
$G_{12} = \sum \min(i,1)\min(i,2) = 1 \cdot 1 + 1 \cdot 2 + 1 \cdot 2 + 1 \cdot 2 = 1+2+2+2 = 7$.
Ratio = $(10+19t)^2/(4+14t+13t^2)$.
Derivative: $38(4+14t+13t^2) - (10+19t)(14+26t) = 0$.
$152 + 532t + 494t^2 = 140 + 260t + 266t + 494t^2 = 140 + 526t + 494t^2$.
$152 + 532t = 140 + 526t$, $12 + 6t = 0$, $t = -2$. Negative. So increasing, min at $t=0$.

It seems like the minimum is always at $v^{(1)}$, giving $\lambda(n) = n(n+1)^2/4$.

But wait, I should check more carefully. Maybe for larger $n$, a combination of extreme rays could give a smaller ratio.

Let me think about this more carefully. We want to minimize $\frac{(c^T S)^2}{c^T G c}$ over $c \ge 0$.

The minimum of $\frac{(c^T S)^2}{c^T G c}$ over all $c$ (no constraint) is 0 (since we can choose $c$ orthogonal to $S$). Over $c \ge 0$, since all $S_k > 0$, $c^T S > 0$ for $c \ge 0, c \ne 0$.

The minimum over $c \ge 0$ is achieved at some point. By the KKT conditions, at the optimum, either we're at an interior point where $Gc \propto S$, or on the boundary.

Actually, let me think about it as: minimize $c^T S$ subject to $c^T G c = 1$ and $c \ge 0$. The Lagrangian is $c^T S - \mu(c^T G c - 1) - \lambda^T c$ where $\lambda \ge 0$. KKT: $S - 2\mu G c - \lambda = 0$, so $S = 2\mu G c + \lambda$ with $\lambda \ge 0$, $\lambda_k c_k = 0$.

For interior solution ($\lambda = 0$): $S = 2\mu G c$, so $c = \frac{1}{2\mu} G^{-1} S$. If $G^{-1} S$ has all positive components, this is the solution. Otherwise, some components are 0.

Let me compute $G^{-1} S$ for $n = 3$.

$G = \begin{pmatrix} 3 & 5 & 6 \\ 5 & 9 & 11 \\ 6 & 11 & 14 \end{pmatrix}$, $S = (6, 11, 14)^T$.

$G^{-1} S$: Let me solve $Gx = S$.
$3x_1 + 5x_2 + 6x_3 = 6$
$5x_1 + 9x_2 + 11x_3 = 11$
$6x_1 + 11x_2 + 14x_3 = 14$

From eq1: $x_1 = (6 - 5x_2 - 6x_3)/3 = 2 - 5x_2/3 - 2x_3$.
Sub into eq2: $5(2 - 5x_2/3 - 2x_3) + 9x_2 + 11x_3 = 11$. $10 - 25x_2/3 - 10x_3 + 9x_2 + 11x_3 = 11$. $10 + (9 - 25/3)x_2 + x_3 = 11$. $10 + (2/3)x_2 + x_3 = 11$. $(2/3)x_2 + x_3 = 1$. So $x_3 = 1 - 2x_2/3$.

Sub into eq3: $6(2 - 5x_2/3 - 2x_3) + 11x_2 + 14x_3 = 14$. $12 - 10x_2 - 12x_3 + 11x_2 + 14x_3 = 14$. $12 + x_2 + 2x_3 = 14$. $x_2 + 2x_3 = 2$.

From $x_3 = 1 - 2x_2/3$: $x_2 + 2(1 - 2x_2/3) = 2$. $x_2 + 2 - 4x_2/3 = 2$. $x_2 - 4x_2/3 = 0$. $-x_2/3 = 0$. $x_2 = 0$.

Then $x_3 = 1$, $x_1 = 2 - 0 - 2 = 0$.

So $G^{-1} S = (0, 0, 1)^T$. This has non-negative components! So the interior solution is $c \propto (0, 0, 1)$, which is the extreme ray $v^{(3)}$.

But that gives ratio 14, which is the maximum, not the minimum! 

Wait, I think I mixed up. The KKT condition for minimizing $c^T S$ subject to $c^T G c = 1$ gives $c \propto G^{-1} S$, which minimizes $c^T S$... no wait.

If we minimize $c^T S$ s.t. $c^T G c = 1$, the solution is $c = \frac{G^{-1}S}{\sqrt{S^T G^{-1} S}}$ and the minimum value is $\sqrt{S^T G^{-1} S}$. But this is the unconstrained minimum. With $c \ge 0$, if $G^{-1}S \ge 0$, then this is also the constrained minimum.

$S^T G^{-1} S = S^T (0,0,1)^T = 14$. So minimum of $c^T S$ is $\sqrt{14}$, and ratio is $14$.

But that's the maximum ratio, not the minimum! I think I have the direction wrong.

We want to minimize $\frac{(c^T S)^2}{c^T G c}$. Since $c^T S > 0$ for $c \ge 0$, this is $(c^T S)^2 / (c^T G c)$. To minimize this, we want $c^T S$ small and $c^T G c$ large.

Hmm, but minimizing $(c^T S)^2/(c^T G c)$ is not the same as minimizing $c^T S$ s.t. $c^T G c = 1$. Let me redo.

$\min_{c \ge 0} \frac{(c^T S)^2}{c^T G c}$. Let $f(c) = \frac{(c^T S)^2}{c^T G c}$. $\nabla f = \frac{2(c^T S) S \cdot (c^T G c) - (c^T S)^2 \cdot 2Gc}{(c^T G c)^2} = \frac{2(c^T S)[S(c^T G c) - (c^T S) Gc]}(c^T G c)^2}$.

Setting to 0: $S = \frac{c^T S}{c^T G c} Gc$, i.e., $Gc = \frac{c^T G c}{c^T S} S$, so $Gc \propto S$, same as before. But this gives a critical point which is a maximum (ratio 14), not a minimum.

So the minimum must be on the boundary of the positive orthant. The boundary consists of faces where some $c_k = 0$. The minimum is achieved at a vertex (single extreme ray) or on an edge/face.

For $n = 3$, the ratios at vertices are 12, 121/9 ≈ 13.44, 14. The minimum is 12 at $v^{(1)}$.

For edges: we checked $c_1, c_2$ (increasing from 12), $c_1, c_3$ (increasing from 12), $c_2, c_3$ (has a min at $t = 5/42$ giving ≈ 13.58). So the global min is 12.

So for $n = 3$, $\lambda(3) = 12 = 3 \cdot 16/4 = n(n+1)^2/4$.

Let me conjecture $\lambda(n) = \frac{n(n+1)^2}{4}$ and try to prove it.

We need to show $(\sum_{i=1}^n i a_i)^2 \ge \frac{n(n+1)^2}{4} \sum_{i=1}^n a_i^2$ for all valid sequences, with equality at $a_i = 1$ for all $i$.

At $a_i = 1$: LHS = $(n(n+1)/2)^2 = n^2(n+1)^2/4$, RHS = $n(n+1)^2/4 \cdot n = n^2(n+1)^2/4$. ✓

So we need to prove: $\sum_{i=1}^n i a_i \ge \frac{(n+1)\sqrt{n}}{2} \sqrt{\sum a_i^2}$, or equivalently, $\left(\sum i a_i\right)^2 \ge \frac{n(n+1)^2}{4} \sum a_i^2$.

Hmm, let me think about this differently. By Cauchy-Schwarz, $(\sum i a_i)^2 \le (\sum i^2)(\sum a_i^2) = \frac{n(n+1)(2n+1)}{6} \sum a_i^2$. That's an upper bound, not useful.

We need a lower bound. The constraint is that $a$ is concave and non-negative with $a_0 = 0$.

Let me think about what sequences minimize the ratio. The constant sequence $a_i = c$ gives ratio $n(n+1)^2/4$. Can we do worse?

Consider $a_i = i$ (linear). Then $\sum i a_i = \sum i^2 = n(n+1)(2n+1)/6$, $\sum a_i^2 = \sum i^2 = n(n+1)(2n+1)/6$. Ratio = $n(n+1)(2n+1)/6$. For $n = 3$: $3 \cdot 4 \cdot 7/6 = 14 > 12$. For $n = 4$: $4 \cdot 5 \cdot 9/6 = 30 > 25$.

Consider $a_i = \min(i, k)$ for some $k$. We computed these give higher ratios.

What about $a_i$ that's "flat" — like $a_1 = a_2 = \cdots = a_n = 1$? That's the constant, giving $n(n+1)^2/4$.

What if $a_1$ is very small? Like $a_1 = \epsilon$, $a_2 = \cdots = a_n = 1$. But we need $a_1 \ge (a_0 + a_2)/2 = 1/2$, so $a_1 \ge 1/2$. And $a_1 \le a_2 = 1$. Let $a_1 = t \in [1/2, 1]$, $a_2 = \cdots = a_n = 1$.

Check concavity: $a_1 \ge (a_0 + a_2)/2 = 1/2$ ✓. $a_2 \ge (a_1 + a_3)/2 = (t+1)/2$ ✓ since $t \le 1$. For $i \ge 3$: $a_i = 1 \ge (1+1)/2 = 1$ ✓.

$\sum i a_i = t + \sum_{i=2}^n i = t + (n(n+1)/2 - 1) = t + n(n+1)/2 - 1$.
$\sum a_i^2 = t^2 + (n-1)$.

Ratio = $(t + n(n+1)/2 - 1)^2 / (t^2 + n - 1)$.

At $t = 1$: $(n(n+1)/2)^2 / n = n(n+1)^2/4$. ✓

Derivative w.r.t. $t$: $\frac{2(t + C)(t^2 + n - 1) - (t+C)^2 \cdot 2t}{(t^2+n-1)^2}$ where $C = n(n+1)/2 - 1$.

$= \frac{2(t+C)[(t^2+n-1) - t(t+C)]}{(t^2+n-1)^2} = \frac{2(t+C)(n-1-Ct)}{(t^2+n-1)^2}$.

Since $t + C > 0$, the sign depends on $n - 1 - Ct$. $C = n(n+1)/2 - 1 = (n^2+n-2)/2 = (n+2)(n-1)/2$.

$n - 1 - Ct = n - 1 - \frac{(n+2)(n-1)}{2} t = (n-1)(1 - \frac{(n+2)t}{2})$.

This is zero when $t = 2/(n+2)$. For $n \ge 2$, $2/(n+2) \le 1/2$, and $t \ge 1/2$. So for $t \ge 1/2 \ge 2/(n+2)$, the derivative is $\le 0$ (since $n-1 > 0$ and $1 - (n+2)t/2 \le 0$). So the ratio is decreasing in $t$ for $t \in [1/2, 1]$, meaning the minimum is at $t = 1$, giving $n(n+1)^2/4$.

So perturbing the constant sequence by lowering $a_1$ increases the ratio. Good.

What about other perturbations? Let me try $a_1 = \cdots = a_{n-1} = 1$, $a_n = t \ge 1$ (since non-decreasing). Concavity: $a_{n-1} \ge (a_{n-2} + a_n)/2 = (1+t)/2$, so $t \le 1$. So $t = 1$ only. Not useful.

What about $a_1 = \cdots = a_k = 1$, $a_{k+1} = \cdots = a_n = t$ with $t \ge 1$? Concavity at $k$: $1 \ge (1 + t)/2$, so $t \le 1$, meaning $t = 1$. So no room.

What about making the sequence increase? Like $a_i = 1 + \epsilon \cdot i$ for small $\epsilon$? This is linear, so concavity holds with equality. $\sum i a_i = \sum i(1 + \epsilon i) = \sum i + \epsilon \sum i^2 = n(n+1)/2 + \epsilon n(n+1)(2n+1)/6$. $\sum a_i^2 = \sum (1+\epsilon i)^2 = n + 2\epsilon \sum i + \epsilon^2 \sum i^2 = n + \epsilon n(n+1) + \epsilon^2 n(n+1)(2n+1)/6$.

Ratio = $\frac{(n(n+1)/2 + \epsilon n(n+1)(2n+1)/6)^2}{n + \epsilon n(n+1) + \epsilon^2 n(n+1)(2n+1)/6}$.

At $\epsilon = 0$: $n(n+1)^2/4$. Let me compute the derivative at $\epsilon = 0$.

Let $A = n(n+1)/2$, $B = n(n+1)(2n+1)/6$, $D = n(n+1)$, $E = n(n+1)(2n+1)/6 = B$.

Ratio = $(A + \epsilon B)^2 / (n + \epsilon D + \epsilon^2 B)$.

$\frac{d}{d\epsilon}\bigg|_0 = \frac{2AB \cdot n - A^2 \cdot D}{n^2} = \frac{A(2Bn - AD)}{n^2}$.

$2Bn = 2 \cdot \frac{n(n+1)(2n+1)}{6} \cdot n = \frac{n^2(n+1)(2n+1)}{3}$.
$AD = \frac{n(n+1)}{2} \cdot n(n+1) = \frac{n^2(n+1)^2}{2}$.

$2Bn - AD = n^2(n+1)\left(\frac{2n+1}{3} - \frac{n+1}{2}\right) = n^2(n+1) \cdot \frac{2(2n+1) - 3(n+1)}{6} = n^2(n+1) \cdot \frac{4n+2-3n-3}{6} = n^2(n+1) \cdot \frac{n-1}{6}$.

For $n \ge 2$, this is positive. So the derivative is positive, meaning increasing $\epsilon$ from 0 increases the ratio. Good, the constant sequence is a local minimum.

Now I need to prove this is the global minimum. Let me think about a proof strategy.

We want to show: for any concave non-decreasing sequence with $a_0 = 0$,
$$\left(\sum_{i=1}^n i a_i\right)^2 \ge \frac{n(n+1)^2}{4} \sum_{i=1}^n a_i^2.$$

Equivalently, $\sum i a_i \ge \frac{(n+1)\sqrt{n}}{2} \|a\|_2$.

Hmm, let me think about this using the representation $a_i = \sum_{k=1}^n c_k \min(i, k)$ with $c_k \ge 0$.

$\sum i a_i = \sum_k c_k S_k$ where $S_k = \sum_{i=1}^n i \min(i, k)$.
$\sum a_i^2 = \sum_{k,l} c_k c_l G_{kl}$ where $G_{kl} = \sum_i \min(i,k)\min(i,l)$.

We need $(\sum c_k S_k)^2 \ge \frac{n(n+1)^2}{4} \sum_{kl} c_k c_l G_{kl}$ for all $c_k \ge 0$.

This is equivalent to: the matrix $M = S S^T - \frac{n(n+1)^2}{4} G$ is copositive (i.e., $c^T M c \ge 0$ for all $c \ge 0$).

Hmm, this is a copositivity condition, which is generally hard to verify. Let me think of another approach.

Alternative approach: Direct inequality. We want to show
$$\sum_{i=1}^n i a_i \ge \frac{(n+1)}{2} \sum_{i=1}^n a_i \cdot \frac{\sqrt{n}}{\sqrt{\sum a_i^2}} \cdot \frac{\sum a_i^2}{\sum a_i}$$

No, that's circular. Let me think differently.

Actually, let me try to prove $\sum i a_i \ge \frac{n+1}{2} \sum a_i$ first (which is a known inequality for concave sequences), and then use Cauchy-Schwarz.

**Claim 1:** For a concave non-decreasing sequence with $a_0 = 0$, $\sum_{i=1}^n i a_i \ge \frac{n+1}{2} \sum_{i=1}^n a_i$.

Proof: By Abel summation / summation by parts. $\sum i a_i = \sum_{i=1}^n i a_i$. Let $A_k = \sum_{i=1}^k a_i$. Then $\sum i a_i = n A_n - \sum_{k=1}^{n-1} A_k$ (by Abel). Also $\sum a_i = A_n$.

So we need $n A_n - \sum_{k=1}^{n-1} A_k \ge \frac{n+1}{2} A_n$, i.e., $\frac{n-1}{2} A_n \ge \sum_{k=1}^{n-1} A_k$.

Since $a$ is concave with $a_0 = 0$, $a_i \ge a_1 \cdot i / 1$... no, concave means $a_i \ge$ linear interpolation. Actually, concave with $a_0 = 0$ means $a_i / i$ is non-increasing (since $a_i = \sum_{j=1}^i d_j$ with $d_j$ non-increasing, $a_i/i$ is the average of non-increasing sequence, which is non-increasing). So $a_i / i \ge a_n / n$ for $i \le n$, i.e., $a_i \ge i a_n / n$.

Hmm, but I need a bound on $A_k$ in terms of $A_n$. Since $a_i/i$ is non-increasing, $a_i \ge (i/k) a_k$ for $i \le k$... no, $a_i/i \ge a_k/k$ for $i \le k$, so $a_i \ge (i/k) a_k$. Then $A_k = \sum_{i=1}^k a_i \ge \sum_{i=1}^k (i/k) a_k = a_k (k+1)/2$. Hmm, this gives a lower bound on $A_k$, but I need an upper bound.

Actually, since $a_i/i$ is non-increasing, for $i \le k$, $a_i \le (i/1) a_1 = i a_1$... no, $a_i/i \le a_1/1 = a_1$, so $a_i \le i a_1$. That gives $A_k \le a_1 k(k+1)/2$, not directly useful.

Let me think again. We need $\sum_{k=1}^{n-1} A_k \le \frac{n-1}{2} A_n$.

Since $a_i$ is concave and $a_0 = 0$, $a_i \ge \frac{i}{n} a_n$ (because $a_i/i$ is non-increasing, so $a_i/i \ge a_n/n$). So $A_k \ge \frac{a_n}{n} \frac{k(k+1)}{2}$.

Also, $a_i \le a_n$ for all $i$ (non-decreasing), so $A_k \le k a_n$.

And $A_n \ge \frac{a_n}{n} \frac{n(n+1)}{2} = \frac{(n+1) a_n}{2}$.

So $\frac{n-1}{2} A_n \ge \frac{(n-1)(n+1) a_n}{4}$ and $\sum_{k=1}^{n-1} A_k \le a_n \sum_{k=1}^{n-1} k = a_n \frac{(n-1)n}{2}$.

We need $\frac{(n-1)(n+1)}{4} \ge \frac{(n-1)n}{2}$, i.e., $\frac{n+1}{4} \ge \frac{n}{2}$, i.e., $n+1 \ge 2n$, i.e., $n \le 1$. That fails for $n \ge 2$.

So this crude approach doesn't work. Let me think more carefully.

Actually, let me reconsider. The inequality $\sum i a_i \ge \frac{n+1}{2} \sum a_i$ — is it even true?

For $a_i = 1$ (constant): $\sum i = n(n+1)/2$, $\frac{n+1}{2} \cdot n = n(n+1)/2$. Equality. ✓

For $a_i = i$ (linear): $\sum i^2 = n(n+1)(2n+1)/6$, $\frac{n+1}{2} \sum i = \frac{n+1}{2} \cdot n(n+1)/2 = n(n+1)^2/4$. Need $n(n+1)(2n+1)/6 \ge n(n+1)^2/4$, i.e., $(2n+1)/6 \ge (n+1)/4$, i.e., $2(2n+1) \ge 3(n+1)$, i.e., $4n+2 \ge 3n+3$, i.e., $n \ge 1$. ✓

For $a = (1/2, 1, 1, \ldots, 1)$ (n terms, $a_1 = 1/2$): $\sum i a_i = 1/2 + \sum_{i=2}^n i = 1/2 + n(n+1)/2 - 1 = n(n+1)/2 - 1/2$. $\sum a_i = 1/2 + (n-1) = n - 1/2$. $\frac{n+1}{2}(n - 1/2) = \frac{(n+1)(2n-1)}{4}$. Need $n(n+1)/2 - 1/2 \ge (n+1)(2n-1)/4$, i.e., $\frac{2n(n+1) - 2}{4} \ge \frac{(n+1)(2n-1)}{4}$, i.e., $2n^2 + 2n - 2 \ge 2n^2 + n - 1$, i.e., $n \ge 1$. ✓

OK so the inequality $\sum i a_i \ge \frac{n+1}{2} \sum a_i$ seems to hold. Let me prove it properly.

$\sum i a_i - \frac{n+1}{2} \sum a_i = \sum_{i=1}^n \left(i - \frac{n+1}{2}\right) a_i = \sum_{i=1}^n \frac{2i - n - 1}{2} a_i$.

Let $b_i = 2i - n - 1$. Then $b_i = i - (n+1-i)$, so $b_i$ is antisymmetric around $(n+1)/2$: $b_i = -b_{n+1-i}$.

$\sum b_i a_i = \sum_{i=1}^n b_i a_i$. Pair up: $\sum_{i=1}^{\lfloor n/2 \rfloor} b_i (a_i - a_{n+1-i})$ (for odd $n$, the middle term has $b_i = 0$).

For $i \le \lfloor n/2 \rfloor$, $b_i = 2i - n - 1 < 0$ and $a_i \le a_{n+1-i}$ (non-decreasing). So $b_i(a_i - a_{n+1-i}) = (\text{negative})(\text{non-positive}) \ge 0$.

So $\sum b_i a_i \ge 0$, proving $\sum i a_i \ge \frac{n+1}{2} \sum a_i$. ✓

Now, combining with Cauchy-Schwarz: $\sum a_i \le \sqrt{n} \sqrt{\sum a_i^2}$, so $\sum i a_i \ge \frac{n+1}{2} \sum a_i$... but this goes the wrong way for our purpose. We need $\sum i a_i \ge \frac{(n+1)\sqrt{n}}{2} \sqrt{\sum a_i^2}$, but we have $\sum i a_i \ge \frac{n+1}{2} \sum a_i$ and $\sum a_i \le \sqrt{n} \sqrt{\sum a_i^2}$, which gives $\sum i a_i \ge \frac{n+1}{2} \sum a_i$ but we can't chain these.

Actually, we need $\sum i a_i \ge \frac{(n+1)\sqrt{n}}{2} \|a\|_2$. We have $\sum i a_i \ge \frac{n+1}{2} \sum a_i \ge \frac{n+1}{2} \|a\|_2$ (since $\sum a_i \ge \|a\|_2$ when... no, $\sum a_i \ge \sqrt{\sum a_i^2}$ only if... $\sum a_i \ge \sqrt{\sum a_i^2}$ iff $(\sum a_i)^2 \ge \sum a_i^2$ iff $2\sum_{i<j} a_i a_j \ge 0$, which is true since $a_i \ge 0$). But $\frac{n+1}{2} \|a\|_2 \le \frac{(n+1)\sqrt{n}}{2} \|a\|_2$, so this is too weak.

We need a tighter approach. The Cauchy-Schwarz gives $\sum a_i \le \sqrt{n} \|a\|_2$, so $\frac{n+1}{2}\sum a_i \le \frac{(n+1)\sqrt{n}}{2}\|a\|_2$. We need the reverse direction somehow.

Let me think about this problem differently. We want to show:
$$\sum_{i=1}^n i a_i \ge \frac{(n+1)\sqrt{n}}{2} \sqrt{\sum a_i^2}$$

with equality when all $a_i$ are equal.

This is saying that the "weighted average" $\frac{\sum i a_i}{\sum a_i}$ is at least $\frac{n+1}{2}$ (which we proved), AND that $\sum a_i \ge \sqrt{n} \sqrt{\sum a_i^2}$... no, that's $\sum a_i \le \sqrt{n}\|a\|_2$ by Cauchy-Schwarz.

Hmm wait. We need $\frac{\sum i a_i}{\|a\|_2} \ge \frac{(n+1)\sqrt{n}}{2}$. We know $\frac{\sum i a_i}{\sum a_i} \ge \frac{n+1}{2}$. And $\frac{\sum a_i}{\|a\|_2} \le \sqrt{n}$. So $\frac{\sum i a_i}{\|a\|_2} = \frac{\sum i a_i}{\sum a_i} \cdot \frac{\sum a_i}{\|a\|_2} \ge \frac{n+1}{2} \cdot \frac{\sum a_i}{\|a\|_2}$.

But $\frac{\sum a_i}{\|a\|_2}$ can be as small as 1 (when one $a_i$ dominates). So this gives $\ge \frac{n+1}{2}$, not $\frac{(n+1)\sqrt{n}}{2}$.

So the two inequalities don't compose. We need a more refined approach that uses the concavity more strongly.

Let me think about this as a variational problem. We want to minimize $\sum i a_i$ subject to $\sum a_i^2 = 1$ and the concavity/non-decreasing/$a_0 = 0$ constraints.

Using Lagrange multipliers on the cone of valid sequences. The cone is generated by $v^{(k)}$, so $a = \sum c_k v^{(k)}$, $c_k \ge 0$.

We want to minimize $\frac{(\sum c_k S_k)^2}{\sum c_k c_l G_{kl}}$ over $c \ge 0$.

As computed, the unconstrained critical point gives $Gc \propto S$, which is a maximum. The minimum is on the boundary.

I showed for $n = 2, 3, 4$ that the minimum is at $c = (1, 0, \ldots, 0)$, i.e., $a = v^{(1)} = (1, 1, \ldots, 1)$.

Let me try to prove that the minimum is always at $v^{(1)}$.

We need: for all $c \ge 0$, $\frac{(\sum c_k S_k)^2}{\sum c_k c_l G_{kl}} \ge \frac{S_1^2}{G_{11}} = \frac{(\sum i)^2}{n} = \frac{n(n+1)^2}{4}$.

$S_1 = \sum_{i=1}^n i = n(n+1)/2$, $G_{11} = n$.

So we need: $(\sum c_k S_k)^2 \ge \frac{n(n+1)^2}{4} \sum_{kl} c_k c_l G_{kl}$ for all $c_k \ge 0$.

Equivalently, $\sum_{kl} c_k c_l \left(S_k S_l - \frac{n(n+1)^2}{4} G_{kl}\right) \ge 0$ for all $c \ge 0$.

Let $M_{kl} = S_k S_l - \frac{n(n+1)^2}{4} G_{kl}$. We need $c^T M c \ge 0$ for all $c \ge 0$ (copositivity).

$M_{11} = S_1^2 - \frac{n(n+1)^2}{4} G_{11} = \frac{n^2(n+1)^2}{4} - \frac{n(n+1)^2}{4} \cdot n = 0$. Good, equality at $c = e_1$.

For copositivity, we need $M$ to be copositive. A sufficient condition is that $M$ is positive semidefinite, but it's not (since $M_{11} = 0$ and we'd need the first row/column to be 0 for PSD, which they're not necessarily).

Actually, since $M_{11} = 0$, for copositivity we need $M_{1k} \ge 0$ for all $k$ (otherwise $c = e_1 + t e_k$ for small $t > 0$ would give negative). Let me check.

$M_{1k} = S_1 S_k - \frac{n(n+1)^2}{4} G_{1k}$.

$G_{1k} = \sum_{i=1}^n \min(i, 1) \min(i, k) = \sum_{i=1}^n \min(i, k) = S_k$... wait, $\min(i, 1) = 1$ for all $i \ge 1$. So $G_{1k} = \sum_{i=1}^n 1 \cdot \min(i, k) = \sum_{i=1}^n \min(i, k)$.

And $S_k = \sum_{i=1}^n i \min(i, k)$.

So $M_{1k} = S_1 S_k - \frac{n(n+1)^2}{4} \sum_{i=1}^n \min(i, k)$.

Let $T_k = \sum_{i=1}^n \min(i, k) = \sum_{i=1}^k i + \sum_{i=k+1}^n k = \frac{k(k+1)}{2} + k(n-k) = \frac{k(k+1) + 2k(n-k)}{2} = \frac{k(2n - k + 1)}{2}$.

$S_k = \sum_{i=1}^k i^2 + \sum_{i=k+1}^n ik = \frac{k(k+1)(2k+1)}{6} + k \cdot \frac{(k+1+n)(n-k)}{2}$.

Let me compute $S_k$ more carefully.
$S_k = \sum_{i=1}^k i \cdot i + \sum_{i=k+1}^n i \cdot k = \sum_{i=1}^k i^2 + k \sum_{i=k+1}^n i = \frac{k(k+1)(2k+1)}{6} + k \cdot \frac{(n-k)(n+k+1)}{2}$.

$= \frac{k(k+1)(2k+1)}{6} + \frac{k(n-k)(n+k+1)}{2}$.

$= \frac{k}{6}\left[(k+1)(2k+1) + 3(n-k)(n+k+1)\right]$.

$(k+1)(2k+1) = 2k^2 + 3k + 1$.
$3(n-k)(n+k+1) = 3(n^2 + n - k^2 - k) = 3n^2 + 3n - 3k^2 - 3k$.

Sum: $2k^2 + 3k + 1 + 3n^2 + 3n - 3k^2 - 3k = -k^2 + 3n^2 + 3n + 1$.

So $S_k = \frac{k(3n^2 + 3n + 1 - k^2)}{6}$.

Check: $S_1 = \frac{3n^2 + 3n + 1 - 1}{6} = \frac{3n(n+1)}{6} = \frac{n(n+1)}{2}$. ✓
$S_n = \frac{n(3n^2 + 3n + 1 - n^2)}{6} = \frac{n(2n^2 + 3n + 1)}{6} = \frac{n(n+1)(2n+1)}{6}$. ✓ (sum of $i^2$)

$T_k = \frac{k(2n - k + 1)}{2}$.

$M_{1k} = \frac{n(n+1)}{2} \cdot \frac{k(3n^2+3n+1-k^2)}{6} - \frac{n(n+1)^2}{4} \cdot \frac{k(2n-k+1)}{2}$.

$= \frac{nk}{12}\left[(n+1)(3n^2+3n+1-k^2) - \frac{3(n+1)^2(2n-k+1)}{2} \cdot 2\right]$

Wait, let me redo this more carefully.

$M_{1k} = S_1 S_k - \frac{n(n+1)^2}{4} T_k$

$= \frac{n(n+1)}{2} \cdot \frac{k(3n^2+3n+1-k^2)}{6} - \frac{n(n+1)^2}{4} \cdot \frac{k(2n-k+1)}{2}$

$= \frac{nk(n+1)}{12}(3n^2+3n+1-k^2) - \frac{nk(n+1)^2(2n-k+1)}{8}$

$= \frac{nk(n+1)}{24}\left[2(3n^2+3n+1-k^2) - 3(n+1)(2n-k+1)\right]$

$= \frac{nk(n+1)}{24}\left[6n^2+6n+2-2k^2 - 3(2n^2+3n+1-nk-k)\right]$

$= \frac{nk(n+1)}{24}\left[6n^2+6n+2-2k^2 - 6n^2-9n-3+3nk+3k\right]$

$= \frac{nk(n+1)}{24}\left[-3n-1-2k^2+3nk+3k\right]$

$= \frac{nk(n+1)}{24}\left[3k(n+1) - 2k^2 - 3n - 1\right]$

$= \frac{nk(n+1)}{24}\left[3k(n+1) - 2k^2 - (3n+1)\right]$

Let me factor $3k(n+1) - 2k^2 - (3n+1) = -2k^2 + 3k(n+1) - (3n+1)$.

At $k = 1$: $-2 + 3(n+1) - 3n - 1 = -2 + 3n + 3 - 3n - 1 = 0$. ✓ (since $M_{11} = 0$)

Factor: $-2k^2 + 3k(n+1) - (3n+1) = -(2k^2 - 3k(n+1) + 3n + 1) = -(2k - 1)(k - (3n+1))$... let me check: $(2k-1)(k - (3n+1)) = 2k^2 - 2k(3n+1) - k + 3n+1 = 2k^2 - (6n+3)k + 3n+1$. And $2k^2 - 3k(n+1) + 3n+1 = 2k^2 - (3n+3)k + 3n+1$. These don't match.

Let me just factor $-2k^2 + 3(n+1)k - (3n+1)$. Roots: $k = \frac{-3(n+1) \pm \sqrt{9(n+1)^2 - 8(3n+1)}}{-4} = \frac{3(n+1) \mp \sqrt{9n^2+18n+9-24n-8}}{4} = \frac{3(n+1) \mp \sqrt{9n^2-6n+1}}{4} = \frac{3(n+1) \mp (3n-1)}{4}$.

$9n^2 - 6n + 1 = (3n-1)^2$. ✓

So roots: $k = \frac{3(n+1) - (3n-1)}{4} = \frac{4}{4} = 1$ and $k = \frac{3(n+1) + (3n-1)}{4} = \frac{6n+2}{4} = \frac{3n+1}{2}$.

So $-2k^2 + 3(n+1)k - (3n+1) = -2(k-1)(k - \frac{3n+1}{2}) = 2(k-1)(\frac{3n+1}{2} - k)$.

For $1 \le k \le n$: $\frac{3n+1}{2} \ge \frac{3 \cdot 2 + 1}{2} = 3.5 > n$ when $n \le 3$... wait, $\frac{3n+1}{2} > n$ iff $3n+1 > 2n$ iff $n > -1$, always true. So $\frac{3n+1}{2} > n \ge k$ for all $k \le n$.

So for $k \ge 1$: $(k - 1) \ge 0$ and $(\frac{3n+1}{2} - k) > 0$, so $M_{1k} \ge 0$ for all $k \ge 1$, with equality only at $k = 1$.

Good, so $M_{1k} \ge 0$ for all $k$. This is necessary for copositivity (since $M_{11} = 0$).

But copositivity requires more than just $M_{1k} \ge 0$. We need $c^T M c \ge 0$ for all $c \ge 0$.

Let me think about this differently. Since $M_{11} = 0$ and $M_{1k} \ge 0$, we can write:

$c^T M c = \sum_{k,l \ge 2} c_k c_l M_{kl} + 2c_1 \sum_{k \ge 2} c_k M_{1k}$.

The second term is $\ge 0$. So we need $\sum_{k,l \ge 2} c_k c_l M_{kl} \ge 0$ for all $c_k \ge 0$ ($k \ge 2$), i.e., the submatrix $M^{(2)} = (M_{kl})_{k,l \ge 2}$ is copositive.

This is a recursive structure. We need to show $M^{(2)}$ is copositive, which requires $M^{(2)}_{22} \ge 0$ and $M^{(2)}_{2k} \ge 0$ for $k \ge 2$ (if $M^{(2)}_{22} = 0$), and then recurse.

Actually, $M_{22} = S_2^2 - \frac{n(n+1)^2}{4} G_{22}$. Let me compute.

$S_2 = \frac{2(3n^2+3n+1-4)}{6} = \frac{2(3n^2+3n-3)}{6} = \frac{3n^2+3n-3}{3} = n^2+n-1$.

$G_{22} = \sum_{i=1}^n \min(i,2)^2 = \sum_{i=1}^2 i^2 + \sum_{i=3}^n 4 = 5 + 4(n-2) = 4n - 3$.

$M_{22} = (n^2+n-1)^2 - \frac{n(n+1)^2}{4}(4n-3)$.

$(n^2+n-1)^2 = n^4 + 2n^3 - n^2 - 2n + 1$.

$\frac{n(n+1)^2(4n-3)}{4} = \frac{n(n^2+2n+1)(4n-3)}{4} = \frac{n(4n^3+8n^2+4n-3n^2-6n-3)}{4} = \frac{n(4n^3+5n^2-2n-3)}{4} = \frac{4n^4+5n^3-2n^2-3n}{4}$.

$M_{22} = n^4 + 2n^3 - n^2 - 2n + 1 - \frac{4n^4+5n^3-2n^2-3n}{4} = \frac{4n^4+8n^3-4n^2-8n+4 - 4n^4-5n^3+2n^2+3n}{4} = \frac{3n^3-2n^2-5n+4}{4}$.

At $n = 2$: $(24 - 8 - 10 + 4)/4 = 10/4 = 5/2 > 0$.
At $n = 3$: $(81 - 18 - 15 + 4)/4 = 52/4 = 13 > 0$.

So $M_{22} > 0$ for $n \ge 2$. Good. But we still need the full submatrix to be copositive, which is not guaranteed just by diagonal entries being positive.

This approach is getting complicated. Let me try a completely different strategy.

**Alternative approach: Direct proof using the structure of concave sequences.**

We want to prove $\left(\sum i a_i\right)^2 \ge \frac{n(n+1)^2}{4} \sum a_i^2$.

Let $\mu = \frac{n+1}{2}$. We've shown $\sum i a_i \ge \mu \sum a_i$, i.e., $\sum (i - \mu) a_i \ge 0$.

Now, $\sum i a_i = \mu \sum a_i + \sum (i - \mu) a_i$.

$(\sum i a_i)^2 = \mu^2 (\sum a_i)^2 + 2\mu (\sum a_i)(\sum (i-\mu)a_i) + (\sum (i-\mu)a_i)^2$.

We need this $\ge \frac{n(n+1)^2}{4} \sum a_i^2 = n\mu^2 \sum a_i^2$.

So we need: $\mu^2(\sum a_i)^2 + 2\mu(\sum a_i)(\sum(i-\mu)a_i) + (\sum(i-\mu)a_i)^2 \ge n\mu^2 \sum a_i^2$.

$\mu^2[(\sum a_i)^2 - n\sum a_i^2] + 2\mu(\sum a_i)(\sum(i-\mu)a_i) + (\sum(i-\mu)a_i)^2 \ge 0$.

Now, $(\sum a_i)^2 - n\sum a_i^2 = -\sum_{i<j}(a_i - a_j)^2 \le 0$ (by the identity). Actually, $(\sum a_i)^2 = \sum a_i^2 + 2\sum_{i<j} a_i a_j$, so $(\sum a_i)^2 - n\sum a_i^2 = 2\sum_{i<j} a_i a_j - (n-1)\sum a_i^2 = -\sum_{i<j}(a_i - a_j)^2 \le 0$.

Wait: $n\sum a_i^2 - (\sum a_i)^2 = \sum_{i<j}(a_i - a_j)^2$. So $(\sum a_i)^2 - n\sum a_i^2 = -\sum_{i<j}(a_i - a_j)^2 \le 0$.

Let $P = \sum a_i$, $Q = \sum a_i^2$, $R = \sum(i-\mu)a_i \ge 0$, $D = nQ - P^2 = \sum_{i<j}(a_i-a_j)^2 \ge 0$.

We need: $-\mu^2 D + 2\mu P R + R^2 \ge 0$, i.e., $R^2 + 2\mu P R \ge \mu^2 D$.

Since $R \ge 0$ and $P \ge 0$, the LHS is $\ge 0$. We need it to be $\ge \mu^2 D$.

This is equivalent to $R \ge \mu(\sqrt{D + P^2} - P) = \mu \cdot \frac{D}{\sqrt{D+P^2}+P}$... hmm, this doesn't simplify nicely.

Actually, $R^2 + 2\mu PR - \mu^2 D \ge 0$ iff $R \ge \frac{-2\mu P + \sqrt{4\mu^2 P^2 + 4\mu^2 D}}{2} = -\mu P + \mu\sqrt{P^2 + D} = \mu(\sqrt{P^2 + D} - P)$.

Since $P^2 + D = P^2 + nQ - P^2 = nQ$, this is $\mu(\sqrt{nQ} - P)$.

So we need $R \ge \mu(\sqrt{nQ} - P)$, i.e., $\sum(i-\mu)a_i \ge \mu(\sqrt{n\sum a_i^2} - \sum a_i)$.

Equivalently, $\sum i a_i - \mu \sum a_i \ge \mu\sqrt{nQ} - \mu P$, i.e., $\sum i a_i \ge \mu\sqrt{nQ}$, which is exactly what we want to prove. So this is circular!

Let me try yet another approach.

**Approach: Use the concavity to relate $\sum a_i^2$ to $(\sum a_i)^2$ more tightly.**

For a concave sequence, the $a_i$ are "more equal" than arbitrary non-negative numbers, so $\sum a_i^2$ should be closer to $(\sum a_i)^2/n$.

Specifically, if $a$ is concave and non-decreasing with $a_0 = 0$, can we bound $\sum a_i^2$ in terms of $(\sum a_i)^2$ and $\sum i a_i$?

Hmm, let me try a different decomposition. Write $a_i = \bar{a} + \delta_i$ where $\bar{a} = \frac{1}{n}\sum a_i$ and $\sum \delta_i = 0$.

$\sum i a_i = \sum i \bar{a} + \sum i \delta_i = \bar{a} \frac{n(n+1)}{2} + \sum i \delta_i = \mu n \bar{a} + \sum (i - \mu) \delta_i + \mu \sum \delta_i = \mu P + \sum (i-\mu)\delta_i$.

Wait, $\sum i \delta_i = \sum (i - \mu) \delta_i + \mu \sum \delta_i = \sum (i-\mu)\delta_i$ since $\sum \delta_i = 0$.

So $R = \sum(i-\mu)a_i = \sum(i-\mu)\delta_i$ (since $\sum(i-\mu)\bar{a} = \bar{a}\sum(i-\mu) = 0$).

And $Q = \sum a_i^2 = n\bar{a}^2 + \sum \delta_i^2$.

We need $(\mu P + R)^2 \ge n\mu^2 Q = n\mu^2(n\bar{a}^2 + \sum \delta_i^2) = n^2\mu^2\bar{a}^2 + n\mu^2\sum\delta_i^2$.

$(\mu P + R)^2 = \mu^2 P^2 + 2\mu PR + R^2 = \mu^2 n^2 \bar{a}^2 + 2\mu PR + R^2$.

So we need $2\mu PR + R^2 \ge n\mu^2 \sum \delta_i^2$, i.e., $R(2\mu P + R) \ge n\mu^2 \sum \delta_i^2$.

Since $R \ge 0$ and $P \ge 0$, and $R = \sum(i-\mu)\delta_i$, we need to bound $R$ from below in terms of $\sum \delta_i^2$.

But $\delta_i$ can be positive or negative, and $R$ depends on the correlation between $\delta_i$ and $(i - \mu)$. For concave sequences, $\delta_i$ tends to be negative for large $i$ (since concave means the sequence flattens out, so $a_i$ is below the linear interpolation for large $i$... actually, concave with $a_0 = 0$ means $a_i$ grows fast initially and slows down, so $\delta_i$ is positive for small $i$ and negative for large $i$, which means $R = \sum(i-\mu)\delta_i$ has $(i-\mu) < 0$ for small $i$ where $\delta_i > 0$, and $(i-\mu) > 0$ for large $i$ where $\delta_i < 0$. So $R = \sum (i-\mu)\delta_i$ has both terms negative... wait, $(i-\mu) < 0$ and $\delta_i > 0$ gives negative, and $(i-\mu) > 0$ and $\delta_i < 0$ gives negative. So $R < 0$?

But we proved $R \ge 0$! Let me recheck.

$R = \sum(i - \mu) a_i = \sum i a_i - \mu \sum a_i$. We proved $\sum i a_i \ge \mu \sum a_i$, so $R \ge 0$.

But with the decomposition, $R = \sum(i-\mu)\delta_i$. For a concave sequence, $\delta_i$ is positive for small $i$ and negative for large $i$ (relative to the mean). Then $(i-\mu) < 0$ for small $i$ and $\delta_i > 0$, so the product is negative. And $(i-\mu) > 0$ for large $i$ and $\delta_i < 0$, product is negative. So $R < 0$? Contradiction!

Let me re-examine. For a concave sequence with $a_0 = 0$, non-decreasing: e.g., $a = (1, 1, 1)$ for $n = 3$. $\bar{a} = 1$, $\delta_i = 0$, $R = 0$. OK.

$a = (1, 2, 2)$: $\bar{a} = 5/3$, $\delta = (-2/3, 1/3, 1/3)$. $R = (1-2)(-2/3) + (2-2)(1/3) + (3-2)(1/3) = 2/3 + 0 + 1/3 = 1 > 0$. ✓

So $\delta_i$ is negative for small $i$ and positive for large $i$ (for this example). That makes sense: concave with $a_0 = 0$ means $a_i$ starts small and grows, so $a_i$ is below the mean for small $i$ and above for large $i$. Wait, but concave means it grows fast initially... 

For $a = (1, 2, 2)$: $a_1 = 1 < 5/3$, $a_2 = 2 > 5/3$, $a_3 = 2 > 5/3$. So $\delta_1 < 0$, $\delta_2, \delta_3 > 0$. And $R = (1-2)(-2/3) + (2-2)(1/3) + (3-2)(1/3) = 2/3 + 1/3 = 1 > 0$. ✓

So for concave sequences, $\delta_i$ is negative for small $i$ and positive for large $i$, which makes $R = \sum(i-\mu)\delta_i > 0$ (positive correlation between $i$ and $\delta_i$). Good.

Now, the question is: can we bound $R$ from below in terms of $\sum \delta_i^2$?

We need $R(2\mu P + R) \ge n\mu^2 \sum \delta_i^2$.

Since $R \ge 0$ and $P \ge 0$, $2\mu P + R \ge R$, so $R(2\mu P + R) \ge R^2$. So it suffices to show $R^2 \ge n\mu^2 \sum \delta_i^2$, i.e., $R \ge \mu\sqrt{n}\|\delta\|_2$.

But $R = \sum(i-\mu)\delta_i \le \|\delta\|_2 \cdot \|(i-\mu)\|_2 = \|\delta\|_2 \cdot \sqrt{\sum(i-\mu)^2} = \|\delta\|_2 \cdot \sqrt{n(n^2-1)/12}$.

And $\mu\sqrt{n} = \frac{(n+1)\sqrt{n}}{2}$. We need $\sqrt{n(n^2-1)/12} \ge \frac{(n+1)\sqrt{n}}{2}$, i.e., $\frac{n^2-1}{12} \ge \frac{(n+1)^2}{4}$, i.e., $\frac{(n-1)(n+1)}{12} \ge \frac{(n+1)^2}{4}$, i.e., $\frac{n-1}{12} \ge \frac{n+1}{4}$, i.e., $n-1 \ge 3(n+1) = 3n+3$, i.e., $-2n \ge 4$, impossible. So Cauchy-Schwarz goes the wrong way.

So $R \le \|\delta\|_2 \sqrt{n(n^2-1)/12}$, which is less than $\mu\sqrt{n}\|\delta\|_2$ for $n \ge 2$. So we can't bound $R$ from below by $\mu\sqrt{n}\|\delta\|_2$ in general. But we don't need that—we need $R(2\mu P + R) \ge n\mu^2 \sum\delta_i^2$, and the $2\mu P$ term helps.

So we need $R \cdot 2\mu P \ge n\mu^2 \sum \delta_i^2 - R^2$, i.e., $2\mu P R \ge n\mu^2 \sum\delta_i^2 - R^2$.

If $R^2 \ge n\mu^2 \sum\delta_i^2$, we're done. Otherwise, we need $2\mu PR \ge n\mu^2\sum\delta_i^2 - R^2 > 0$.

This is getting complicated. Let me try a more computational approach.

**Approach: Verify the inequality by reducing to extreme rays and checking copositivity computationally for general $n$.**

Actually, let me try to prove the inequality directly. We need:

$$\left(\sum_{i=1}^n i a_i\right)^2 \ge \frac{n(n+1)^2}{4} \sum_{i=1}^n a_i^2$$

for all concave non-decreasing sequences with $a_0 = 0$.

Equivalently, $\sum i a_i \ge \frac{(n+1)\sqrt{n}}{2}\|a\|_2$.

Let me try to use the representation $a_i = \sum_{j=1}^i d_j$ with $d_1 \ge d_2 \ge \cdots \ge d_n \ge 0$.

$\sum i a_i = \sum_{i=1}^n i \sum_{j=1}^i d_j = \sum_{j=1}^n d_j \sum_{i=j}^n i = \sum_{j=1}^n d_j \frac{(n+j)(n-j+1)}{2} = \sum_{j=1}^n d_j \frac{n(n+1) - j(j-1)}{2}$.

$\sum a_i^2 = \sum_{i=1}^n \left(\sum_{j=1}^i d_j\right)^2$.

This is still complex. Let me try the extreme ray approach more carefully.

We need to show that for $c \ge 0$, $c^T M c \ge 0$ where $M_{kl} = S_k S_l - \frac{n(n+1)^2}{4} G_{kl}$.

We showed $M_{11} = 0$ and $M_{1k} \ge 0$ for all $k$. So $c^T Mc = 2c_1 \sum_{k \ge 2} c_k M_{1k} + \sum_{k,l \ge 2} c_k c_l M_{kl}$.

The first term is $\ge 0$. So it suffices to show $\sum_{k,l \ge 2} c_k c_l M_{kl} \ge 0$ for $c_k \ge 0$, i.e., the submatrix $M^{(2:n)}$ is copositive.

But this submatrix doesn't have the same structure. Let me check if $M_{22} = 0$ for some $n$... we computed $M_{22} = \frac{3n^3 - 2n^2 - 5n + 4}{4}$. At $n = 2$: $5/2 > 0$. So $M_{22} > 0$.

If $M_{22} > 0$, then for copositivity of $M^{(2:n)}$, we need... it's not just about diagonal entries.

Actually, for a $2 \times 2$ matrix $\begin{pmatrix} a & b \\ b & d \end{pmatrix}$ with $a, d \ge 0$, copositivity is equivalent to $a \ge 0, d \ge 0$, and $b + \sqrt{ad} \ge 0$ (i.e., $b \ge -\sqrt{ad}$). For larger matrices, it's more complex.

Let me try a different approach entirely.

**Approach: Prove the inequality by induction on $n$.**

Base case $n = 2$: $\lambda(2) = 9/2$, verified above.

Inductive step: Assume the result for $n-1$, prove for $n$.

Hmm, the constraint structure changes with $n$, so induction isn't straightforward.

**Approach: Use Schur-convexity or majorization.**

The concavity condition means the sequence $a$ is "majorized" by the constant sequence in some sense. Actually, for a concave sequence with $a_0 = 0$, the sequence is "more spread out" than constant... no, concave means it's "less spread out" in some sense.

Hmm, let me think about this more carefully using a variational argument.

**Key insight:** The minimum of $\frac{(\sum i a_i)^2}{\sum a_i^2}$ over the cone of valid sequences is achieved at an extreme ray. We've verified this for $n = 2, 3, 4$ (the minimum is at $v^{(1)}$). Let me try to prove this in general.

We need to show that for any $c \ge 0$ (not all zero), $\frac{(\sum c_k S_k)^2}{\sum c_k c_l G_{kl}} \ge \frac{S_1^2}{G_{11}}$.

This is equivalent to: $G_{11}(\sum c_k S_k)^2 \ge S_1^2 \sum c_k c_l G_{kl}$.

$G_{11} = n$, $S_1 = n(n+1)/2$.

$n(\sum c_k S_k)^2 \ge \frac{n^2(n+1)^2}{4} \sum c_k c_l G_{kl}$.

$(\sum c_k S_k)^2 \ge \frac{n(n+1)^2}{4} \sum c_k c_l G_{kl}$.

Which is what we had. Let me try to prove this by showing that $S_k / \sqrt{G_{kk}} \ge S_1/\sqrt{G_{11}}$ for all $k$, and that the "cross terms" don't hurt.

$S_k / \sqrt{G_{kk}}$ for extreme ray $k$: this is the ratio for $a = v^{(k)}$.

$v^{(k)}_i = \min(i, k)$. $\sum i v^{(k)}_i = S_k$, $\sum (v^{(k)}_i)^2 = G_{kk}$.

Ratio $= S_k^2 / G_{kk}$.

We need $S_k^2 / G_{kk} \ge S_1^2 / G_{11} = n(n+1)^2/4$ for all $k$.

$S_k = \frac{k(3n^2+3n+1-k^2)}{6}$, $G_{kk} = \sum_{i=1}^n \min(i,k)^2 = \sum_{i=1}^k i^2 + k^2(n-k) = \frac{k(k+1)(2k+1)}{6} + k^2(n-k)$.

$= \frac{k(k+1)(2k+1) + 6k^2(n-k)}{6} = \frac{k[(k+1)(2k+1) + 6k(n-k)]}{6} = \frac{k[2k^2+3k+1+6kn-6k^2]}{6} = \frac{k[-4k^2+6kn+3k+1]}{6} = \frac{k[6kn-4k^2+3k+1]}{6}$.

Hmm, let me just check: $G_{kk} = \frac{k(6kn - 4k^2 + 3k + 1)}{6}$.

Check $k=1$: $\frac{6n - 4 + 3 + 1}{6} = \frac{6n}{6} = n$. ✓
Check $k=n$: $\frac{n(6n^2 - 4n^2 + 3n + 1)}{6} = \frac{n(2n^2+3n+1)}{6} = \frac{n(n+1)(2n+1)}{6}$. ✓

$\frac{S_k^2}{G_{kk}} = \frac{k^2(3n^2+3n+1-k^2)^2/36}{k(6kn-4k^2+3k+1)/6} = \frac{k(3n^2+3n+1-k^2)^2}{6(6kn-4k^2+3k+1)}$.

We need this $\ge \frac{n(n+1)^2}{4}$ for all $1 \le k \le n$.

At $k = 1$: $\frac{(3n^2+3n)^2}{6 \cdot 6n} = \frac{9n^2(n+1)^2}{36n} = \frac{n(n+1)^2}{4}$. ✓ (equality)

Let me check $k = 2$, $n = 4$: $S_2 = \frac{2(48+12+1-4)}{6} = \frac{2 \cdot 57}{6} = 19$. $G_{22} = \frac{2(48-16+6+1)}{6} = \frac{2 \cdot 39}{6} = 13$. Ratio $= 361/13 \approx 27.77$. And $n(n+1)^2/4 = 4 \cdot 25/4 = 25$. $27.77 > 25$. ✓

So the ratio at each extreme ray is $\ge n(n+1)^2/4$, with equality at $k = 1$. But we also need to check combinations.

For combinations, the ratio of a positive combination can be less than the minimum of individual ratios (this is the key difficulty). This happens when the "cross terms" $G_{kl}$ are large relative to $G_{kk}, G_{ll}$.

Specifically, for $c = \alpha e_k + \beta e_l$ with $\alpha, \beta > 0$:
Ratio $= \frac{(\alpha S_k + \beta S_l)^2}{\alpha^2 G_{kk} + 2\alpha\beta G_{kl} + \beta^2 G_{ll}}$.

This can be less than $\min(S_k^2/G_{kk}, S_l^2/G_{ll})$ if $G_{kl}$ is large enough.

The ratio is minimized (over $\alpha/\beta$) at some point, and the minimum of the 2-variable ratio is:

$\frac{S_k^2 G_{ll} - 2 S_k S_l G_{kl} + S_l^2 G_{kk}}{G_{kk} G_{ll} - G_{kl}^2}$... no, that's not right.

Actually, $\min_{\alpha,\beta > 0} \frac{(\alpha S_k + \beta S_l)^2}{\alpha^2 G_{kk} + 2\alpha\beta G_{kl} + \beta^2 G_{ll}}$.

Let $t = \alpha/\beta$. Ratio $= \frac{(tS_k + S_l)^2}{t^2 G_{kk} + 2t G_{kl} + G_{ll}}$.

This is a ratio of quadratics. The minimum over $t > 0$ can be found by taking derivative. But the unconstrained minimum (over all $t$) is:

$\min_t \frac{(tS_k + S_l)^2}{t^2 G_{kk} + 2tG_{kl} + G_{ll}}$.

If $G_{kl}^2 < G_{kk} G_{ll}$ (positive definite), the minimum is 0 (achieved at $t = -S_l/S_k$). But with $t > 0$, the minimum is at $t = 0$ or $t \to \infty$ or at a critical point.

Derivative: $\frac{2(tS_k+S_l)S_k(t^2G_{kk}+2tG_{kl}+G_{ll}) - (tS_k+S_l)^2(2tG_{kk}+2G_{kl})}{(\ldots)^2} = 0$.

$(tS_k+S_l)[S_k(t^2G_{kk}+2tG_{kl}+G_{ll}) - (tS_k+S_l)(tG_{kk}+G_{kl})] = 0$.

Since $tS_k + S_l > 0$:
$S_k(t^2G_{kk}+2tG_{kl}+G_{ll}) = (tS_k+S_l)(tG_{kk}+G_{kl})$
$t^2 S_k G_{kk} + 2t S_k G_{kl} + S_k G_{ll} = t^2 S_k G_{kk} + t S_k G_{kl} + t S_l G_{kk} + S_l G_{kl}$
$t S_k G_{kl} + S_k G_{ll} = t S_l G_{kk} + S_l G_{kl}$
$t(S_k G_{kl} - S_l G_{kk}) = S_l G_{kl} - S_k G_{ll}$
$t = \frac{S_l G_{kl} - S_k G_{ll}}{S_k G_{kl} - S_l G_{kk}} = \frac{S_k G_{ll} - S_l G_{kl}}{S_l G_{kk} - S_k G_{kl}}$.

For this to give a minimum (not maximum), and for $t > 0$, we need specific sign conditions.

This is getting very involved. Let me try a completely different approach.

**Approach: Use the Cauchy-Schwarz inequality in a clever way, exploiting concavity.**

We want $\sum i a_i \ge \frac{(n+1)\sqrt{n}}{2} \|a\|_2$.

Consider the vector $w = (1, 2, \ldots, n)$ and $a = (a_1, \ldots, a_n)$. We want $w \cdot a \ge \frac{(n+1)\sqrt{n}}{2} \|a\|_2$.

By Cauchy-Schwarz, $w \cdot a \le \|w\|_2 \|a\|_2 = \sqrt{n(n+1)(2n+1)/6} \|a\|_2$. This is an upper bound.

We need a lower bound, which must use the constraint on $a$.

**Approach: Reformulate as a constrained optimization and use KKT conditions.**

We minimize $\sum i a_i$ subject to $\sum a_i^2 = 1$, $a_0 = 0$, $a$ non-decreasing, and $2a_i \ge a_{i+1} + a_{i-1}$.

The Lagrangian: $L = \sum i a_i - \lambda(\sum a_i^2 - 1) - \sum_{i=1}^{n-1} \mu_i (2a_i - a_{i+1} - a_{i-1}) - \sum_{i=1}^n \nu_i(a_i - a_{i-1})$ where $\mu_i \ge 0$, $\nu_i \ge 0$.

$\frac{\partial L}{\partial a_i} = i - 2\lambda a_i - 2\mu_i + \mu_{i-1} + \mu_{i+1} - \nu_i + \nu_{i+1} = 0$ (with $\mu_0 = \mu_n = 0$, $\nu_{n+1} = 0$... need to be careful with boundary).

Wait, actually $a_0 = 0$ is fixed, so we don't optimize over $a_0$. The constraints are:
- $a_i \ge a_{i-1}$ for $i = 1, \ldots, n$ (with $a_0 = 0$)
- $2a_i \ge a_{i+1} + a_{i-1}$ for $i = 1, \ldots, n-1$
- $\sum a_i^2 = 1$

At the optimum (which we believe is $a_i = 1/\sqrt{n}$), all $a_i$ are equal, so $a_i - a_{i-1} = 0$ for $i \ge 2$ and $a_1 - a_0 = 1/\sqrt{n} > 0$. The concavity constraint $2a_i = a_{i+1} + a_{i-1}$ holds with equality for $i = 2, \ldots, n-1$ (since all equal), and for $i = 1$: $2a_1 = 2/\sqrt{n} \ge a_2 + a_0 = 1/\sqrt{n}$, so $2/\sqrt{n} \ge 1/\sqrt{n}$, strict inequality.

So at the optimum, the active constraints are: concavity for $i = 2, \ldots, n-1$ (equality), and $\sum a_i^2 = 1$. The non-decreasing constraints are active for $i = 2, \ldots, n$ (equality $a_i = a_{i-1}$) but not for $i = 1$.

Hmm, this is a degenerate case. The KKT conditions would be complex. Let me try a different approach.

**Approach: Prove the inequality using a clever algebraic manipulation.**

We want to show $(\sum i a_i)^2 \ge \frac{n(n+1)^2}{4} \sum a_i^2$.

Let me try to write $\sum i a_i - \frac{n+1}{2}\|a\|_2 \sqrt{n}$... no, this doesn't factor nicely.

Let me try to use the identity/approach from the proof of $\sum i a_i \ge \frac{n+1}{2} \sum a_i$ and strengthen it.

We showed $\sum i a_i = \frac{n+1}{2} \sum a_i + \sum_{i=1}^{\lfloor n/2\rfloor} (n+1-2i)(a_{n+1-i} - a_i) \cdot \frac{1}{2}$... let me redo this.

$\sum i a_i - \frac{n+1}{2}\sum a_i = \sum (i - \frac{n+1}{2}) a_i = \sum_{i=1}^n \frac{2i-n-1}{2} a_i$.

Pair $i$ and $n+1-i$: $\frac{2i-n-1}{2} a_i + \frac{2(n+1-i)-n-1}{2} a_{n+1-i} = \frac{2i-n-1}{2}(a_i - a_{n+1-i})$.

For $i < (n+1)/2$: $2i - n - 1 < 0$ and $a_i \le a_{n+1-i}$, so the product is $\ge 0$.

$R = \sum_{i=1}^{\lfloor n/2 \rfloor} \frac{2i-n-1}{2}(a_i - a_{n+1-i}) = \sum_{i=1}^{\lfloor n/2 \rfloor} \frac{n+1-2i}{2}(a_{n+1-i} - a_i)$.

So $R = \sum_{i=1}^{\lfloor n/2 \rfloor} \frac{n+1-2i}{2}(a_{n+1-i} - a_i) \ge 0$.

Now, $\sum i a_i = \mu P + R$ where $\mu = (n+1)/2$, $P = \sum a_i$, $R \ge 0$.

$(\sum i a_i)^2 = (\mu P + R)^2 = \mu^2 P^2 + 2\mu PR + R^2$.

We need $\mu^2 P^2 + 2\mu PR + R^2 \ge n\mu^2 Q$ where $Q = \sum a_i^2$.

$\mu^2(P^2 - nQ) + 2\mu PR + R^2 \ge 0$.

$P^2 - nQ = -\sum_{i<j}(a_i - a_j)^2 = -D$ where $D \ge 0$.

So $-\mu^2 D + 2\mu PR + R^2 \ge 0$, i.e., $R^2 + 2\mu PR \ge \mu^2 D$.

Now, $D = \sum_{i<j}(a_i - a_j)^2$. Let me express $D$ in terms of the paired differences.

$D = \sum_{i<j}(a_j - a_i)^2$. Pair $i$ and $n+1-i$: for $i < (n+1)/2$, the pair $(i, n+1-i)$ contributes $(a_{n+1-i} - a_i)^2$ plus all other pairs.

Actually, $D = \sum_{i<j}(a_j - a_i)^2$ includes all pairs, not just symmetric ones. So this decomposition doesn't simplify $D$ nicely.

Let me try to bound $D$ in terms of $R$ and $P$.

$D = nQ - P^2$. We need $R^2 + 2\mu PR \ge \mu^2(nQ - P^2) = \mu^2 n Q - \mu^2 P^2$.

$R^2 + 2\mu PR + \mu^2 P^2 \ge \mu^2 n Q$, i.e., $(R + \mu P)^2 \ge \mu^2 n Q$, i.e., $R + \mu P \ge \mu\sqrt{nQ}$ (since both sides positive).

$R + \mu P = \sum i a_i$. So this is $\sum i a_i \ge \mu\sqrt{nQ} = \frac{(n+1)\sqrt{n}}{2}\sqrt{\sum a_i^2}$, which is exactly what we want to prove. So this is circular again!

OK so the algebraic manipulation approach just reduces to the original inequality. I need a genuinely different idea.

**Approach: Use the concavity to bound $\sum a_i^2$ in terms of $\sum a_i$ and $\sum i a_i$.**

For a concave sequence, the $a_i$ are "smooth", so $\sum a_i^2$ is bounded above by something involving $\sum a_i$ and $\sum i a_i$.

Specifically, we want: $\sum a_i^2 \le \frac{4}{n(n+1)^2}(\sum i a_i)^2$.

For the constant sequence, this is equality: $n \le \frac{4}{n(n+1)^2} \cdot \frac{n^2(n+1)^2}{4} = n$. ✓

Can we prove $\sum a_i^2 \le \frac{4}{n(n+1)^2}(\sum i a_i)^2$ for all concave non-decreasing sequences with $a_0 = 0$?

This is equivalent to the original inequality. Let me think about what makes concave sequences special.

For a concave sequence with $a_0 = 0$, we have $a_i \ge \frac{i}{n} a_n$ (since $a_i/i$ is non-increasing). Also, $a_i \le \min(a_n, i \cdot a_1)$ (since $a_i/i \le a_1$ and $a_i \le a_n$).

Hmm, let me try to use the second moment method or some interpolation inequality.

**Approach: Discrete Wirtinger / Hardy-type inequality.**

Actually, this reminds me of Hardy's inequality or weighted inequalities for monotone sequences. Let me think...

We have a concave sequence (second differences $\le 0$). We want a lower bound on $\sum i a_i$ relative to $\|a\|_2$.

**Approach: Use duality / Cauchy-Schwarz with a cleverly chosen weight.**

We want $\sum i a_i \ge C \|a\|_2$ where $C = \frac{(n+1)\sqrt{n}}{2}$.

By Cauchy-Schwarz, $\sum i a_i = \sum (i \sqrt{w_i})(a_i / \sqrt{w_i}) \le \sqrt{\sum i^2 w_i} \sqrt{\sum a_i^2 / w_i}$ for any $w_i > 0$. But this gives an upper bound, not lower.

For a lower bound, we need to use the constraint. Let me think of it as: the minimum of $\sum i a_i$ over $\{a: \|a\|_2 = 1, a \text{ valid}\}$ is $C$.

The constraint set is a cone intersected with the unit sphere. The minimum of a linear function over this set is at an extreme point of the cone (intersected with the sphere), which is a unit vector along an extreme ray.

Wait, is that true? The minimum of a linear function over $\{x \in K: \|x\| = 1\}$ where $K$ is a cone—is it achieved at an extreme ray?

Not necessarily. The set $\{x \in K: \|x\| = 1\}$ is not convex (it's the intersection of a cone with a sphere). The minimum of a linear function over this set could be at a non-extreme point.

However, we can write: $\min_{a \in K, \|a\|=1} c^T a$ where $c = (1, 2, \ldots, n)$. Since $K$ is a cone, $\min_{a \in K, \|a\|=1} c^T a = \min_{a \in K, a \ne 0} \frac{c^T a}{\|a\|}$.

This is the minimum of $c^T a / \|a\|$ over the cone. The minimum is achieved at some point $a^*$. If $a^*$ is in the interior of $K$, then the gradient condition gives $c/\|a\| - (c^T a) a/\|a\|^3 = 0$ (from the cone being open), but the cone has non-empty interior, so... actually, the minimum of $c^T a / \|a\|$ over a cone is not necessarily at an extreme ray.

Example: in $\mathbb{R}^2$, cone $K = \{x \ge 0, y \ge 0\}$, $c = (1, 1)$. $\min c^T x / \|x\| = \min \frac{x+y}{\sqrt{x^2+y^2}}$ over $x, y \ge 0$. At $(1, 0)$: $1$. At $(0, 1)$: $1$. At $(1, 1)$: $\sqrt{2}$. So the minimum is at the extreme rays. But if $c = (1, -1)$, then at $(1, 0)$: $1$, at $(0, 1)$: $-1$, at $(1, 1)$: $0$. Minimum at $(0, 1)$, an extreme ray.

Actually, for a polyhedral cone, the minimum of $c^T x / \|x\|$ is always achieved at an extreme ray. Here's why: any point in the cone is a positive combination of extreme rays: $x = \sum \alpha_i v_i$. Then $c^T x = \sum \alpha_i c^T v_i$ and $\|x\| \le \sum \alpha_i \|v_i\|$ (triangle inequality). So $\frac{c^T x}{\|x\|} \ge \frac{\sum \alpha_i c^T v_i}{\sum \alpha_i \|v_i\|} \ge \min_i \frac{c^T v_i}{\|v_i\|}$.

Wait, that's not right because $\|x\| \le \sum \alpha_i \|v_i\|$ gives $\frac{c^T x}{\|x\|} \ge \frac{\sum \alpha_i c^T v_i}{\sum \alpha_i \|v_i\|}$, and the latter is a weighted average of $\frac{c^T v_i}{\|v_i\|}$, so it's $\ge \min_i \frac{c^T v_i}{\|v_i\|}$.

Yes! So $\frac{c^T x}{\|x\|} \ge \min_i \frac{c^T v_i}{\|v_i\|}$ for any $x$ in the cone. And the minimum is achieved at the extreme ray $v_i$ that minimizes $c^T v_i / \|v_i\|$.

So the minimum of $\frac{\sum i a_i}{\|a\|_2}$ over the cone is $\min_k \frac{S_k}{\sqrt{G_{kk}}}$, and $\lambda(n) = \left(\min_k \frac{S_k}{\sqrt{G_{kk}}}\right)^2 = \min_k \frac{S_k^2}{G_{kk}}$.

Wait, but this uses the triangle inequality $\|x\| \le \sum \alpha_i \|v_i\|$, which is for the $\ell_2$ norm. Let me double-check.

$x = \sum \alpha_i v_i$ with $\alpha_i \ge 0$. $\|x\|_2 = \|\sum \alpha_i v_i\|_2 \le \sum \alpha_i \|v_i\|_2$ by triangle inequality. ✓

$c^T x = \sum \alpha_i c^T v_i$. So $\frac{c^T x}{\|x\|_2} \ge \frac{\sum \alpha_i c^T v_i}{\sum \alpha_i \|v_i\|_2}$. And $\frac{\sum \alpha_i c^T v_i}{\sum \alpha_i \|v_i\|_2} = \frac{\sum \alpha_i \|v_i\|_2 \cdot \frac{c^T v_i}{\|v_i\|_2}}{\sum \alpha_i \|v_i\|_2}$, which is a weighted average of $\frac{c^T v_i}{\|v_i\|_2}$ with weights $\alpha_i \|v_i\|_2 \ge 0$. So it's $\ge \min_i \frac{c^T v_i}{\|v_i\|_2}$.

Therefore, $\frac{c^T x}{\|x\|_2} \ge \min_i \frac{c^T v_i}{\|v_i\|_2}$, and the minimum over the cone is $\min_i \frac{c^T v_i}{\|v_i\|_2}$, achieved at the extreme ray.

So $\lambda(n) = \min_{k=1}^n \frac{S_k^2}{G_{kk}}$.

Now I need to find $\min_{k=1}^n \frac{S_k^2}{G_{kk}}$ and show it equals $\frac{n(n+1)^2}{4}$ (achieved at $k = 1$).

We have:
$S_k = \frac{k(3n^2+3n+1-k^2)}{6}$
$G_{kk} = \frac{k(6kn-4k^2+3k+1)}{6}$

$\frac{S_k^2}{G_{kk}} = \frac{k^2(3n^2+3n+1-k^2)^2/36}{k(6kn-4k^2+3k+1)/6} = \frac{k(3n^2+3n+1-k^2)^2}{6(6kn-4k^2+3k+1)}$.

We need to show $\frac{k(3n^2+3n+1-k^2)^2}{6(6kn-4
