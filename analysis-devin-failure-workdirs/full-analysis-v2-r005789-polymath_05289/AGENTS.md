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
  <problem_id>polymath_05289</problem_id>
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

Let \( a, b, c, \) and \( d \) be elements of the set \(\{1, 2, 3, \ldots, 2014, 2015\}\) such that \( a < b < c < d \), \( a + b \) is a divisor of \( c + d \), and \( a + c \) is a divisor of \( b + d \). Find the greatest value that the number \( a \) can have.

## Standard Solution

To find the greatest value of \( a \) such that \( a, b, c, d \) are elements of the set \(\{1, 2, \ldots, 2015\}\) with \( a < b < c < d \), and the conditions \( a + b \mid c + d \) and \( a + c \mid b + d \) are satisfied, we proceed as follows:

1. **Express \( c \) and \( d \) in terms of \( a \) and \( b \)**:
   Given the conditions:
   \[
   c + d = k(a + b) \quad \text{and} \quad b + d = m(a + c)
   \]
   for some integers \( k \) and \( m \).

2. **Assume specific values for \( k \) and \( m \)**:
   We try \( k = 3 \) and \( m = 2 \) to see if they satisfy the conditions:
   \[
   c + d = 3(a + b) \quad \text{and} \quad b + d = 2(a + c)
   \]

3. **Solve for \( c \) and \( d \)**:
   From \( c + d = 3(a + b) \), we have:
   \[
   d = 3(a + b) - c
   \]
   Substitute \( d \) into the second equation:
   \[
   b + (3(a + b) - c) = 2(a + c)
   \]
   Simplifying, we get:
   \[
   b + 3a + 3b - c = 2a + 2c \implies 4b + 3a - c = 2a + 2c \implies 4b + a = 3c \implies c = \frac{4b + a}{3}
   \]
   Since \( c \) must be an integer, \( 4b + a \) must be divisible by 3.

4. **Express \( d \) in terms of \( a \) and \( b \)**:
   Substitute \( c = \frac{4b + a}{3} \) back into the expression for \( d \):
   \[
   d = 3(a + b) - \frac{4b + a}{3} = \frac{9a + 9b - 4b - a}{3} = \frac{8a + 5b}{3}
   \]
   Since \( d \) must also be an integer, \( 8a + 5b \) must be divisible by 3.

5. **Determine the maximum \( a \)**:
   We need to find the largest \( a \) such that \( a < b < c < d \) and all values are within the set \(\{1, 2, \ldots, 2015\}\).

   - From \( c = \frac{4b + a}{3} \) and \( d = \frac{8a + 5b}{3} \), we need:
     \[
     a < b < \frac{4b + a}{3} < \frac{8a + 5b}{3}
     \]
   - Also, \( d \leq 2015 \):
     \[
     \frac{8a + 5b}{3} \leq 2015 \implies 8a + 5b \leq 6045
     \]

6. **Maximize \( a \) with \( b \)**:
   - Let \( b = 466 \):
     \[
     c = \frac{4 \cdot 466 + a}{3} = \frac{1864 + a}{3}
     \]
     \[
     d = \frac{8a + 5 \cdot 466}{3} = \frac{8a + 2330}{3}
     \]
   - Solve for \( a \):
     \[
     1864 + a \equiv 0 \pmod{3} \implies a \equiv -1864 \equiv 2 \pmod{3}
     \]
     \[
     8a + 2330 \equiv 0 \pmod{3} \implies 8a \equiv -2330 \equiv 2 \pmod{3} \implies a \equiv 2 \pmod{3}
     \]
   - Let \( a = 464 \):
     \[
     c = \frac{1864 + 464}{3} = 776
     \]
     \[
     d = \frac{8 \cdot 464 + 2330}{3} = 2014
     \]
   - Verify:
     \[
     464 < 466 < 776 < 2014
     \]
     \[
     464 + 466 = 930 \mid 776 + 2014 = 2790
     \]
     \[
     464 + 776 = 1240 \mid 466 + 2014 = 2480
     \]

Thus, the greatest value of \( a \) is \(\boxed{464}\).

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We need to find the greatest value of $a$ where $a,b,c,d \in \{1,2,...,2015\}$, $a < b < c < d$, $a+b \mid c+d$, and $a+c \mid b+d$.

Let me think about this problem carefully.

We have $a < b < c < d$ with all in $\{1, ..., 2015\}$.

Conditions:
1. $(a+b) \mid (c+d)$
2. $(a+c) \mid (b+d)$

Let me set up variables. Let $s = a+b$, $t = a+c$. Note $s < t$ since $b < c$.

We need $s \mid (c+d)$ and $t \mid (b+d)$.

Let $c + d = ms$ and $b + d = nt$ for positive integers $m, n$.

From $c + d = ms$ and $b + d = nt$:
- $c - b = ms - nt$, so $c = b + ms - nt$.
- $d = ms - c = ms - b - ms + nt = nt - b$.

So $d = nt - b$ and $c = b + ms - nt$.

Constraints:
- $a < b < c < d$, all in $\{1, ..., 2015\}$.
- $c = b + ms - nt > b$, so $ms > nt$, i.e., $ms - nt \geq 1$.
- $d = nt - b > c = b + ms - nt$, so $nt - b > b + ms - nt$, i.e., $2nt - 2b > ms$, i.e., $b < nt - ms/2$.
- $d = nt - b \leq 2015$.
- $a = s - b \geq 1$, so $b \leq s - 1$.
- $a = s - b$, and $a < b$ means $s - b < b$, i.e., $b > s/2$.
- $b < c$ already handled.
- $c < d$ already handled.
- $c \leq 2015$: $b + ms - nt \leq 2015$.

We want to maximize $a = s - b$.

To maximize $a$, we want $s$ large and $b$ small (but $b > s/2$ and $b \geq a+1 = s - b + 1$, so $b \geq (s+1)/2$).

Actually $a = s - b$, and $b > s/2$ means $a < s/2$, so $a \leq \lfloor (s-1)/2 \rfloor$.

Also $b \geq a + 1 = s - b + 1$, so $2b \geq s + 1$, $b \geq \lceil(s+1)/2\rceil$.

Let me think about what values are feasible. We need $d = nt - b \leq 2015$ and $c = b + ms - nt \leq 2015$ and $c \geq 1$ (actually $c > b > a \geq 1$).

Let me try to maximize $a$. Let's think about the constraints on $m$ and $n$.

Since $c + d = ms$ and $c > b > a$, $d > c > b > a$, we have $c + d > a + b = s$... well $c + d \geq (b+1) + (b+2) \geq 2b + 3$. And $ms = c + d$. Also $b + d = nt$.

Since $d > c > b$, $b + d > b + c > 2b$, and $nt = b + d$. Also $t = a + c > a + b = s$.

Let me think about bounds. $c + d \leq 2015 + 2014 = 4029$ (since $c < d \leq 2015$). Actually $c < d \leq 2015$ so $c \leq 2014$, $d \leq 2015$, $c + d \leq 4029$. And $s = a + b \geq 1 + 2 = 3$. So $m = (c+d)/s \leq 4029/3 = 1343$.

Similarly $b + d \leq 2014 + 2015 = 4029$ (since $b < c < d$, $b \leq 2013$). And $t = a + c \geq 1 + 3 = 4$. So $n \leq 4029/4 \approx 1007$.

This is a big search space. Let me think more cleverly.

We want to maximize $a$. Let's think about what structure gives large $a$.

Let me try $a$ close to 2015. If $a$ is large, say $a = 2015 - k$ for small $k$, then $b, c, d$ are even larger, but they must be $\leq 2015$. So $b \leq 2015$, $c \leq 2015$, $d \leq 2015$, and $a < b < c < d$. If $a = 2015$, impossible since $b > a = 2015$ but $b \leq 2015$. So $a \leq 2012$ (need $a, a+1, a+2, a+3 \leq 2015$, so $a \leq 2012$).

Let me think about small cases to find a pattern.

Let me try to find the maximum $a$ by thinking about the structure.

Let $c + d = m(a+b)$ and $b + d = n(a+c)$.

Subtracting: $(c+d) - (b+d) = c - b = m(a+b) - n(a+c)$.

So $c - b = ma + mb - na - nc = a(m-n) + mb - nc$.

Also $d = n(a+c) - b$ and $d = m(a+b) - c$.

From $d = n(a+c) - b$: $d = na + nc - b$.
From $d = m(a+b) - c$: $d = ma + mb - c$.

So $na + nc - b = ma + mb - c$, giving $a(n-m) + c(n+1) = b(m+1)$, i.e., $b = \frac{a(n-m) + c(n+1)}{m+1}$.

Hmm, this is getting complicated. Let me try a different parametrization.

Let me set $a+b = s$, $a+c = t$, with $s < t$ (since $b < c$). Then $b = s - a$, $c = t - a$.

$c + d = ms \Rightarrow d = ms - c = ms - t + a$.
$b + d = nt \Rightarrow d = nt - b = nt - s + a$.

So $ms - t + a = nt - s + a$, giving $ms - t = nt - s$, i.e., $s(m+1) = t(n+1)$.

So $s(m+1) = t(n+1)$. Since $s < t$, we need $m+1 > n+1$, i.e., $m > n$. Let $m > n \geq 1$.

Let $s(m+1) = t(n+1) = L$ for some common value $L$. So $s = L/(m+1)$ and $t = L/(n+1)$.

Since $s < t$, $m+1 > n+1$, consistent.

Now $d = ms - t + a = m \cdot \frac{L}{m+1} - \frac{L}{n+1} + a$.

And $b = s - a = \frac{L}{m+1} - a$, $c = t - a = \frac{L}{n+1} - a$.

Constraints:
- $a < b$: $a < \frac{L}{m+1} - a \Rightarrow 2a < \frac{L}{m+1} \Rightarrow a < \frac{L}{2(m+1)}$.
- $b < c$: $\frac{L}{m+1} < \frac{L}{n+1}$, which is $m+1 > n+1$, i.e., $m > n$. ✓ (already required)
- $c < d$: $\frac{L}{n+1} - a < m \cdot \frac{L}{m+1} - \frac{L}{n+1} + a \Rightarrow \frac{2L}{n+1} - \frac{mL}{m+1} < 2a$.
- $d \leq 2015$: $m \cdot \frac{L}{m+1} - \frac{L}{n+1} + a \leq 2015$.
- $a \geq 1$, $b \geq 1$ (i.e., $\frac{L}{m+1} > a$), $c \geq 1$, $d \geq 1$.
- All integers.

Also $s = a + b$ and $t = a + c$ must be positive integers, and $L = s(m+1) = t(n+1)$.

Let me denote $s = a + b$ and $t = a + c$. We have $s(m+1) = t(n+1)$.

Let $g = \gcd(m+1, n+1)$, $m+1 = gp$, $n+1 = gq$ with $\gcd(p,q) = 1$ and $p > q$ (since $m > n$). Then $s \cdot gp = t \cdot gq$, so $sp = tq$, and since $\gcd(p,q)=1$, $q \mid s$ and $p \mid t$. Let $s = qk$, $t = pk$ for some positive integer $k$.

Then:
- $a + b = qk$, $a + c = pk$.
- $b = qk - a$, $c = pk - a$.
- $d = ms - t + a = (gp-1)qk - pk + a = gpqk - qk - pk + a$.
- Also $d = nt - s + a = (gq-1)pk - qk + a = gpqk - pk - qk + a$. Same thing. Good.

So $d = gpqk - (p+q)k + a = k(gp q - p - q) + a$.

Let me define $D = gpq - p - q = pq \cdot g - p - q$. Then $d = Dk + a$.

Constraints:
- $a < b = qk - a \Rightarrow 2a < qk \Rightarrow a \leq \lfloor(qk-1)/2\rfloor$.
- $b < c$: $qk < pk$ since $p > q$. ✓
- $c < d$: $pk - a < Dk + a \Rightarrow pk - Dk < 2a \Rightarrow k(p - D) < 2a$.
  - $p - D = p - gpq + p + q = 2p + q - gpq = p(2 - gq) + q$. Hmm, let me recompute. $D = gpq - p - q$, so $p - D = p - gpq + p + q = 2p + q - gpq$.
  - For $c < d$, we need $2a > k(p - D) = k(2p + q - gpq)$.
  - Note $gpq \geq p + q$ would make $D \geq 0$. Actually $gpq - p - q = D$. If $g \geq 2$ (and $p, q \geq 1$), then $gpq \geq 2pq \geq 2p \geq p + q$ (when $p \geq q$, which is true). Actually $2pq \geq p + q$ when $p, q \geq 1$ and at least one $\geq 1$... $2 \cdot 1 \cdot 1 = 2 \geq 2 = 1 + 1$. Yes. So $D \geq 0$ when $g \geq 2$.
  - If $g = 1$: $D = pq - p - q = (p-1)(q-1) - 1$. This can be negative. E.g., $p=2, q=1$: $D = 2 - 2 - 1 = -1$. $p=3, q=1$: $D = 3 - 3 - 1 = -1$. $p=3, q=2$: $D = 6 - 3 - 2 = 1$.
- $d \leq 2015$: $Dk + a \leq 2015$.
- $a \geq 1$, $b = qk - a \geq 1$ (so $qk \geq a + 1$), $c = pk - a \geq 1$ (so $pk \geq a + 1$), $d \geq 1$.
- All values in $\{1, ..., 2015\}$, and $a < b < c < d$.

We want to maximize $a$.

From $a < qk/2$ and $d = Dk + a \leq 2015$:

$a \leq \min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$.

To maximize $a$, we want $qk$ large (so $a$ can be up to $\sim qk/2$) and $Dk$ small (so $2015 - Dk$ is large).

If $D = 0$: $d = a$, but we need $d > c > b > a$, so $d > a$, contradiction. So $D \geq 1$ is needed (actually $d = Dk + a > a$ requires $Dk \geq 1$, and $d > c = pk - a$ requires $Dk + a > pk - a$, i.e., $Dk > pk - 2a$, i.e., $2a > k(p - D)$).

Let me think about what gives the largest $a$.

We need $a \leq \lfloor(qk-1)/2\rfloor$ and $a \leq 2015 - Dk$ and $2a > k(2p + q - gpq)$ (from $c < d$).

To maximize $a$, ideally we want $Dk$ small and $qk$ large, and $a$ close to $qk/2$.

If $a \approx qk/2$, then $d = Dk + qk/2 \leq 2015$, so $k(D + q/2) \leq 2015$.

And $c < d$: $2a > k(2p + q - gpq)$. With $a \approx qk/2$: $qk > k(2p + q - gpq)$, i.e., $q > 2p + q - gpq$, i.e., $gpq > 2p$, i.e., $gq > 2$.

So if $gq > 2$ (i.e., $gq \geq 3$), the constraint $c < d$ is satisfiable with $a$ near $qk/2$.

Let me consider specific cases.

**Case $g = 1, q = 1$:** Then $gq = 1 < 3$, so we need $2a > k(2p + 1 - p) = k(p + 1)$. And $a < k/2$ (since $qk = k$). So $2a < k$ but $2a > k(p+1) \geq 2k$ (since $p \geq 2$). Contradiction ($k > 2k$ impossible). So $g=1, q=1$ doesn't work for $p \geq 2$.

Wait, $p > q = 1$ so $p \geq 2$. Then $k(p+1) \geq 3k > k > 2a$. So $c < d$ requires $2a > 3k$ but $a < k/2$ gives $2a < k$. Contradiction. So $g=1, q=1$ is impossible.

**Case $g = 2, q = 1$:** $gq = 2 < 3$. $D = 2p - p - 1 = p - 1$. $c < d$: $2a > k(2p + 1 - 2p) = k$. And $a < k/2$ gives $2a < k$. Contradiction again. So $g=2, q=1$ impossible.

**Case $g = 3, q = 1$:** $gq = 3$. $D = 3p - p - 1 = 2p - 1$. $c < d$: $2a > k(2p + 1 - 3p) = k(1 - p)$. Since $p \geq 2$, $1 - p \leq -1$, so $2a > k(1-p)$ is automatically satisfied (RHS negative). Good.

So with $g=3, q=1, p \geq 2$: $D = 2p - 1$, $a < k/2$, $d = (2p-1)k + a \leq 2015$.

To maximize $a$: $a \leq \lfloor(k-1)/2\rfloor$ and $a \leq 2015 - (2p-1)k$.

We want to maximize $\min(\lfloor(k-1)/2\rfloor, 2015 - (2p-1)k)$.

With $p = 2$: $D = 3$. $a \leq \min(\lfloor(k-1)/2\rfloor, 2015 - 3k)$.
- $\lfloor(k-1)/2\rfloor = 2015 - 3k$ roughly when $k/2 \approx 2015 - 3k$, i.e., $3.5k \approx 2015$, $k \approx 575.7$.
- $k = 575$: $\lfloor 574/2 \rfloor = 287$, $2015 - 1725 = 290$. Min = 287.
- $k = 576$: $\lfloor 575/2 \rfloor = 287$, $2015 - 1728 = 287$. Min = 287.
- $k = 577$: $\lfloor 576/2 \rfloor = 288$, $2015 - 1731 = 284$. Min = 284.
- So max is 287 at $k = 575$ or $576$.

Check $k=576, p=2, g=3, q=1$: $a = 287$, $b = 576 - 287 = 289$, $c = 2 \cdot 576 - 287 = 865$, $d = 3 \cdot 576 + 287 = 2015$.
- $a < b < c < d$: $287 < 289 < 865 < 2015$. ✓
- $a + b = 576$, $c + d = 865 + 2015 = 2880 = 5 \cdot 576$. ✓ ($m = gp - 1 = 5$)
- $a + c = 1152$, $b + d = 289 + 2015 = 2304 = 2 \cdot 1152$. ✓ ($n = gq - 1 = 2$)
- All in $\{1, ..., 2015\}$. ✓

So $a = 287$ works. But can we do better with other parameters?

Let me try larger $q$.

**Case $g = 1, q = 2, p = 3$:** $gq = 2 < 3$. $D = 6 - 3 - 2 = 1$. $c < d$: $2a > k(6 + 2 - 6) = 2k$. And $a < qk/2 = k$. So $2a > 2k$ but $a < k$ gives $2a < 2k$. Contradiction. Impossible.

**Case $g = 2, q = 2, p = 3$:** $gq = 4 > 3$. $D = 12 - 3 - 2 = 7$. $c < d$: $2a > k(6 + 2 - 12) = -4k$. Auto satisfied.
$a < qk/2 = k$, $d = 7k + a \leq 2015$.
$a \leq \min(k-1, 2015 - 7k)$. Max when $k = 2015 - 7k$, $8k = 2015$, $k \approx 251.9$.
- $k = 251$: $\min(250, 2015 - 1757) = \min(250, 258) = 250$.
- $k = 252$: $\min(251, 2015 - 1764) = \min(251, 251) = 251$.
- $k = 253$: $\min(252, 2015 - 1771) = \min(252, 244) = 244$.
So max $a = 251$ at $k = 252$. Less than 287.

**Case $g = 1, q = 3, p = 4$:** $gq = 3$. $D = 12 - 4 - 3 = 5$. $c < d$: $2a > k(8 + 3 - 12) = -k$. Auto satisfied.
$a < 3k/2$, $d = 5k + a \leq 2015$.
$a \leq \min(\lfloor(3k-1)/2\rfloor, 2015 - 5k)$.
$3k/2 \approx 2015 - 5k \Rightarrow 6.5k \approx 2015 \Rightarrow k \approx 310$.
- $k = 310$: $\lfloor 929/2 \rfloor = 464$, $2015 - 1550 = 465$. Min = 464.
- $k = 309$: $\lfloor 926/2 \rfloor = 463$, $2015 - 1545 = 470$. Min = 463.
- $k = 311$: $\lfloor 932/2 \rfloor = 466$, $2015 - 1555 = 460$. Min = 460.
So max $a = 464$ at $k = 310$. Better than 287!

Check: $g=1, q=3, p=4, k=310, a=464$.
- $b = 3 \cdot 310 - 464 = 930 - 464 = 466$.
- $c = 4 \cdot 310 - 464 = 1240 - 464 = 776$.
- $d = 5 \cdot 310 + 464 = 1550 + 464 = 2014$.
- $a < b < c < d$: $464 < 466 < 776 < 2014$. ✓
- $a + b = 930$, $c + d = 776 + 2014 = 2790 = 3 \cdot 930$. ✓ ($m = gp - 1 = 3$)
- $a + c = 1240$, $b + d = 466 + 2014 = 2480 = 2 \cdot 1240$. ✓ ($n = gq - 1 = 2$)
- All $\leq 2015$. ✓

So $a = 464$. Can we do better?

Let me try to optimize more systematically. We want to maximize $\min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$ where $D = gpq - p - q$, subject to $c < d$ constraint.

The $c < d$ constraint: $2a > k(2p + q - gpq)$. If $gpq \geq 2p + q$ (i.e., $g \geq 2 + q/(pq) = 2 + 1/p$... hmm let me think). $gpq \geq 2p + q \iff g \geq 2/p + 1/q \cdot ... $ wait: $gpq \geq 2p + q \iff g \geq (2p+q)/(pq) = 2/q + 1/p$. Since $p \geq 2, q \geq 1$, $2/q + 1/p \leq 2/1 + 1/2 = 2.5$. So $g \geq 3$ always works, and $g = 2$ works when $2/q + 1/p \leq 2$, i.e., $2/q \leq 2 - 1/p < 2$, i.e., $q \geq 2$ (roughly). And $g = 1$ works when $2/q + 1/p \leq 1$, i.e., $2p + q \leq pq$, i.e., $pq - 2p - q \geq 0$, i.e., $(p-1)(q-2) \geq 2$... let me check: $pq - 2p - q = p(q-2) - q$. For $q = 3, p = 4$: $4 - 3 = 1 > 0$... wait $p(q-2) - q = 4 \cdot 1 - 3 = 1 > 0$. Yes works. For $q = 3, p = 3$: $3 \cdot 1 - 3 = 0$, so $gpq = 2p + q$, $c < d$ requires $2a > 0$, always true. For $q = 2, p = 3$: $3 \cdot 0 - 2 = -2 < 0$, doesn't work (as we saw). For $q = 4, p = 2$: $2 \cdot 2 - 4 = 0$, works. For $q = 2, p = 2$: not valid since $p > q$.

OK so when the $c < d$ constraint is auto-satisfied (RHS $\leq 0$), we just need $a \leq \min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$.

The optimal is when $\lfloor(qk-1)/2\rfloor \approx 2015 - Dk$, i.e., $qk/2 \approx 2015 - Dk$, i.e., $k(q/2 + D) \approx 2015$, i.e., $k \approx 2015 / (D + q/2) = 2015 / (gpq - p - q + q/2) = 2015 / (gpq - p - q/2)$.

And the max $a \approx qk/2 \approx \frac{2015 q}{2(gpq - p - q/2)} = \frac{2015 q}{2gpq - 2p - q} = \frac{2015 q}{2p(gq - 1) - q}$.

To maximize this, we want to minimize $\frac{2p(gq-1) - q}{q} = \frac{2p(gq-1)}{q} - 1 = 2p(g - 1/q) - 1$.

So we want to minimize $2p(g - 1/q) - 1 = 2pg - 2p/q - 1$.

Since $p \geq q+1$ (as $p > q$ and both positive integers with $\gcd(p,q) = 1$), and $g \geq 1$:

For $g = 1$: minimize $2p - 2p/q - 1 = 2p(1 - 1/q) - 1 = 2p(q-1)/q - 1$.
- $q = 2, p = 3$: $2 \cdot 3 \cdot 1/2 - 1 = 2$. But we showed $g=1, q=2$ doesn't work (c<d constraint). 
- $q = 3, p = 4$: $2 \cdot 4 \cdot 2/3 - 1 = 16/3 - 1 = 13/3 \approx 4.33$. $a \approx 2015 \cdot 3 / (2 \cdot 13/3 \cdot 3) = ... $ let me just use the formula $a \approx \frac{2015 q}{2p(gq-1) - q}$.
  - $g=1, q=3, p=4$: $a \approx \frac{2015 \cdot 3}{2 \cdot 4 \cdot 2 - 3} = \frac{6045}{13} \approx 465$. Matches our 464!
- $q = 4, p = 5$: $a \approx \frac{2015 \cdot 4}{2 \cdot 5 \cdot 3 - 4} = \frac{8060}{26} \approx 310$. Worse.
- $q = 3, p = 5$ (but $\gcd(3,5)=1$, ok): $D = 15 - 5 - 3 = 7$. $a \approx \frac{2015 \cdot 3}{2 \cdot 5 \cdot 2 - 3} = \frac{6045}{17} \approx 355$. Worse than 465.
- $q = 5, p = 6$: $a \approx \frac{2015 \cdot 5}{2 \cdot 6 \cdot 4 - 5} = \frac{10075}{43} \approx 234$. Worse.

So for $g = 1$, the best seems to be $q = 3, p = 4$ giving $a \approx 465$.

Let me check $q = 4, p = 5$ more carefully. $g=1, q=4, p=5$: $D = 20 - 5 - 4 = 11$. $a \approx 2015 \cdot 4 / (2 \cdot 5 \cdot 3 - 4) = 8060/26 = 310$. Worse.

What about $q = 3, p = 4$ with $g = 1$ is the best for $g = 1$.

For $g = 2$: minimize $2p(2 - 1/q) - 1 = 2p(2q-1)/q - 1$.
- $q = 1, p = 2$: $D = 4 - 2 - 1 = 1$. But $gq = 2 < 3$, c<d constraint: $2a > k(4 + 1 - 4) = k$, and $a < k/2$ gives $2a < k$. Contradiction. Doesn't work.
- $q = 1, p = 3$: $gq = 2$, same issue. $2a > k(6+1-6) = k$, $2a < k$. Contradiction.
- $q = 2, p = 3$: $D = 12 - 3 - 2 = 7$. $a \approx 2015 \cdot 2 / (2 \cdot 3 \cdot 3 - 2) = 4030/16 = 251.9$. We got 251. Worse.
- $q = 3, p = 4$: $D = 24 - 4 - 3 = 17$. $a \approx 2015 \cdot 3 / (2 \cdot 4 \cdot 5 - 3) = 6045/37 \approx 163$. Worse.

For $g = 3$: 
- $q = 1, p = 2$: $D = 6 - 2 - 1 = 3$. $a \approx 2015 \cdot 1 / (2 \cdot 2 \cdot 2 - 1) = 2015/7 \approx 287.9$. We got 287. Worse than 464.
- $q = 1, p = 3$: $D = 9 - 3 - 1 = 5$. $a \approx 2015 / (2 \cdot 3 \cdot 2 - 1) = 2015/11 \approx 183$. Worse.

So the best so far is $g = 1, q = 3, p = 4$ with $a = 464$.

But wait, I should also check whether we can push $a$ higher by not having $a$ exactly at the midpoint. Let me also consider other parametrizations more carefully.

Actually, let me reconsider. The formula $a \approx \frac{2015 q}{2p(gq-1) - q}$ suggests we want $2p(gq-1) - q$ to be small relative to $q$. The ratio is $\frac{2p(gq-1)}{q} - 1$.

For $g = 1$: $\frac{2p(q-1)}{q} - 1$. To minimize, we want $p$ small and $q$ large, but $p > q$ and $\gcd(p,q) = 1$. The smallest $p$ for given $q$ is $p = q + 1$ (if $\gcd(q+1, q) = 1$, which is always true).

So with $p = q + 1, g = 1$: ratio $= \frac{2(q+1)(q-1)}{q} - 1 = \frac{2(q^2-1)}{q} - 1 = 2q - 2/q - 1$.

$a \approx \frac{2015 q}{2(q+1)(q-1) - q} = \frac{2015 q}{2q^2 - 2 - q} = \frac{2015 q}{2q^2 - q - 2}$.

For $q = 3$: $\frac{6045}{18 - 3 - 2} = \frac{6045}{13} \approx 465$.
For $q = 4$: $\frac{8060}{32 - 4 - 2} = \frac{8060}{26} \approx 310$.
For $q = 5$: $\frac{10075}{50 - 5 - 2} = \frac{10075}{43} \approx 234$.
For $q = 2$: $\frac{4030}{8 - 2 - 2} = \frac{4030}{4} = 1007.5$. But wait, $q = 2, p = 3, g = 1$ doesn't work because of the $c < d$ constraint!

Let me recheck: $g = 1, q = 2, p = 3$: $gpq = 6$, $2p + q = 8$. $gpq < 2p + q$, so the c<d constraint requires $2a > k(8 - 6) = 2k$, but $a < qk/2 = k$, so $2a < 2k$. Contradiction. So indeed doesn't work.

So the c<d constraint eliminates $q = 2, p = 3, g = 1$.

What about $q = 2, p = 5, g = 1$? $\gcd(5, 2) = 1$. $D = 10 - 5 - 2 = 3$. $gpq = 10$, $2p + q = 12$. $gpq < 2p + q$, so c<d requires $2a > k(12 - 10) = 2k$, but $a < k$, $2a < 2k$. Contradiction. Doesn't work.

Actually for $g = 1, q = 2$: $gpq = 2p$, $2p + q = 2p + 2$. $gpq = 2p < 2p + 2 = 2p + q$ always. So c<d always requires $2a > 2k$, impossible. So $g = 1, q = 2$ never works.

For $g = 1, q = 3$: $gpq = 3p$, $2p + q = 2p + 3$. $3p \geq 2p + 3 \iff p \geq 3$. So $p \geq 3$ works (with $p > q = 3$ meaning $p \geq 4$, or $p = 3$ gives equality, $3p = 2p+3$ when $p=3$, so $2a > 0$, always true).

Wait, $p = 3, q = 3$? But $\gcd(3, 3) = 3 \neq 1$. So $p = 3, q = 3$ is not valid. Need $\gcd(p, q) = 1$, so $p = 4$ (since $p > q = 3$).

For $g = 1, q = 3, p = 4$: works, $a \approx 465$.

For $g = 1, q = 4$: $gpq = 4p$, $2p + q = 2p + 4$. $4p \geq 2p + 4 \iff p \geq 2$. So $p \geq 5$ (since $p > q = 4$ and $\gcd(p, 4) = 1$, so $p = 5$). $p = 5$: $a \approx 310$. Worse.

So the best for $g = 1$ is $q = 3, p = 4$, $a \approx 465$.

Now let me check if there's a way to get higher $a$ with non-coprime considerations or other approaches.

Actually, I realize I should also check: can we get $a$ higher by having $d$ not exactly at 2015? Let me re-examine.

With $g = 1, q = 3, p = 4, k = 310, a = 464$: $d = 5 \cdot 310 + 464 = 2014$. We have room ($d = 2014 < 2015$). Can we increase $a$?

$a \leq \lfloor(3 \cdot 310 - 1)/2\rfloor = \lfloor 929/2 \rfloor = 464$. And $a \leq 2015 - 5 \cdot 310 = 465$. So $a = 464$ is the max for $k = 310$.

What about $k = 309$? $a \leq \lfloor 926/2 \rfloor = 463$ and $a \leq 2015 - 1545 = 470$. Min = 463. Worse.

What about $k = 311$? $a \leq \lfloor 932/2 \rfloor = 466$ and $a \leq 2015 - 1555 = 460$. Min = 460. Worse.

So $k = 310, a = 464$ is optimal for this parametrization.

Hmm, but what if we try $g = 1, q = 3, p = 4$ but allow $d = 2015$ exactly? $d = 5k + a = 2015$. And $a \leq \lfloor(3k-1)/2\rfloor$. So $a = 2015 - 5k$ and $2015 - 5k \leq (3k-1)/2$, i.e., $4030 - 10k \leq 3k - 1$, $4031 \leq 13k$, $k \geq 310.08$, so $k \geq 311$. At $k = 311$: $a = 2015 - 1555 = 460$. And $\lfloor 932/2 \rfloor = 466 \geq 460$. So $a = 460$. Worse than 464.

At $k = 310$: $a = 2015 - 1550 = 465$. $\lfloor 929/2 \rfloor = 464 < 465$. So $a = 464$. That's what we got.

So the binding constraint is $a < qk/2$ (i.e., $a < b$), not $d \leq 2015$.

To get higher $a$, we need $qk/2$ to be larger, which means $qk$ larger, but then $Dk$ also grows, pushing $d > 2015$.

The fundamental tradeoff: $a \approx qk/2$ and $d \approx Dk + qk/2 = (D + q/2)k \leq 2015$, so $a \approx qk/2 \approx \frac{2015 q}{2(D + q/2)} = \frac{2015 q}{2D + q}$.

With $D = gpq - p - q$: $a \approx \frac{2015 q}{2gpq - 2p - 2q + q} = \frac{2015 q}{2gpq - 2p - q} = \frac{2015 q}{2p(gq - 1) - q}$.

To maximize, minimize $\frac{2p(gq-1) - q}{q} = \frac{2p(gq-1)}{q} - 1$.

For $g = 1$: $\frac{2p(q-1)}{q} - 1$. With $p = q+1$: $\frac{2(q+1)(q-1)}{q} - 1 = 2q - 2/q - 1$.
- $q = 3$: $6 - 2/3 - 1 = 13/3 \approx 4.33$. $a \approx 2015/4.33 \approx 465$.
- $q = 4$: $8 - 1/2 - 1 = 6.5$. $a \approx 2015 \cdot 4 / (2 \cdot 6.5 \cdot ... ) $ hmm let me just compute directly. $a \approx 2015 \cdot 4 / (2 \cdot 5 \cdot 3 - 4) = 8060/26 = 310$.

For $g = 2, q = 1$: $\frac{2p \cdot 1}{1} - 1 = 2p - 1$. With $p = 2$: $3$. $a \approx 2015/3 \approx 671$? But we showed $g = 2, q = 1$ doesn't work!

The issue is the c<d constraint. For $g = 2, q = 1$: $gpq = 2p$, $2p + q = 2p + 1$. $gpq = 2p < 2p + 1$, so c<d requires $2a > k$, but $a < k/2$ gives $2a < k$. Contradiction.

So $g = 2, q = 1$ never works. The c<d constraint kills it.

For $g = 2, q = 2, p = 3$: $\frac{2 \cdot 3 \cdot 3}{2} - 1 = 8$. $a \approx 2015 \cdot 2 / 16 = 251.9$. We got 251.

For $g = 2, q = 3, p = 4$: $\frac{2 \cdot 4 \cdot 5}{3} - 1 = 40/3 - 1 = 37/3 \approx 12.33$. $a \approx 2015 \cdot 3 / 37 \approx 163$. Worse.

Hmm, so $g = 1, q = 3, p = 4$ giving $a = 464$ seems to be the best. But let me think if there are other parametrizations I'm missing.

Wait, I assumed $m > n$ (i.e., $m + 1 > n + 1$). What if $m = n$? Then $s(m+1) = t(m+1)$ gives $s = t$, but $s = a + b < a + c = t$ since $b < c$. Contradiction. So $m > n$ is necessary.

What about $n = 0$? Then $b + d = 0$, impossible since $b, d \geq 1$. So $n \geq 1$.

And $m \geq 2$ (since $m > n \geq 1$).

Let me also check: could there be solutions where $m$ and $n$ are not of the form I described? No, my parametrization is general: $s(m+1) = t(n+1)$ with $m > n \geq 1$ covers all cases.

Let me also verify: I need $m \geq 2$ (since $m > n \geq 1$). With $g = 1, q = 3, p = 4$: $m = gp - 1 = 3$, $n = gq - 1 = 2$. $m = 3 > n = 2 \geq 1$. ✓

Now let me think about whether we can do better with a different approach. Let me consider $g = 1$ and vary $q$ more.

For $g = 1$, the c<d constraint requires $gpq \geq 2p + q$, i.e., $pq \geq 2p + q$, i.e., $p(q-2) \geq q$, i.e., $p \geq q/(q-2)$ (for $q > 2$).
- $q = 3$: $p \geq 3$. But $p > q = 3$ and $\gcd(p, 3) = 1$, so $p \geq 4$.
- $q = 4$: $p \geq 2$. $p > 4$ and $\gcd(p, 4) = 1$, so $p \geq 5$.
- $q = 5$: $p \geq 5/3 \approx 1.67$. $p > 5$ and $\gcd(p, 5) = 1$, so $p \geq 6$.

The approximate $a$ values:
- $q = 3, p = 4$: $a \approx 465$.
- $q = 4, p = 5$: $a \approx 310$.
- $q = 5, p = 6$: $a \approx 234$.
- $q = 6, p = 7$: $a \approx \frac{2015 \cdot 6}{2 \cdot 7 \cdot 5 - 6} = \frac{12090}{64} \approx 189$.

Decreasing. So $q = 3$ is the sweet spot for $g = 1$.

What about $g = 1, q = 3, p = 5$? $\gcd(5, 3) = 1$. $D = 15 - 5 - 3 = 7$. $a \approx \frac{2015 \cdot 3}{2 \cdot 5 \cdot 2 - 3} = \frac{6045}{17} \approx 355$. Worse.

$g = 1, q = 3, p = 7$? $\gcd(7, 3) = 1$. $D = 21 - 7 - 3 = 11$. $a \approx \frac{6045}{2 \cdot 7 \cdot 2 - 3} = \frac{6045}{25} \approx 241$. Worse.

So $p = 4$ is optimal for $q = 3, g = 1$.

Now let me think about $g = 2$ more carefully.

For $g = 2$, c<d requires $2pq \geq 2p + q$, i.e., $2p(q-1) \geq q$, i.e., $p \geq q/(2(q-1))$. For $q \geq 2$, $q/(2(q-1)) \leq 1$, so always satisfied (since $p \geq 2$).

- $q = 2, p = 3$: $a \approx 252$.
- $q = 1, p = 2$: doesn't work (c<d constraint).

Wait, for $g = 2, q = 1$: $2pq = 2p$, $2p + q = 2p + 1$. $2p < 2p + 1$. Doesn't work.

For $g = 2, q = 2, p = 3$: works, $a \approx 252$.
For $g = 2, q = 3, p = 4$: $a \approx 163$.

So $g = 2$ best is 252, worse than 464.

For $g = 3$:
- $q = 1, p = 2$: $a \approx 288$.
- $q = 1, p = 3$: $a \approx 183$.
- $q = 2, p = 3$: $D = 18 - 3 - 2 = 13$. $a \approx \frac{2015 \cdot 2}{2 \cdot 3 \cdot 5 - 2} = \frac{4030}{28} \approx 144$.

So $g = 3$ best is 288, worse than 464.

It seems like $g = 1, q = 3, p = 4$ with $a = 464$ is the answer. But let me double-check by trying to see if there's any other combination I might have missed.

Actually, wait. I should also consider the case where the c<d constraint is NOT auto-satisfied but still achievable. In those cases, $a$ might be pushed higher than $qk/2$... no wait, $a < qk/2$ is always required (from $a < b$). The c<d constraint gives a lower bound on $a$, not an upper bound. So if c<d is not auto-satisfied, it restricts $a$ from below, which doesn't help us maximize $a$.

Actually, the c<d constraint is $2a > k(2p + q - gpq)$. If $2p + q - gpq > 0$, this gives a lower bound on $a$. Combined with the upper bound $a < qk/2$, we need $k(2p + q - gpq) < qk$, i.e., $2p + q - gpq < q$, i.e., $2p < gpq$, i.e., $gq > 2$. So as long as $gq > 2$, there's a feasible range for $a$.

When $gq > 2$ but $2p + q - gpq > 0$ (i.e., $gpq < 2p + q$), the lower bound on $a$ is $a > k(2p + q - gpq)/2$, and the upper bound is $a < qk/2$. The max $a$ is still $\lfloor(qk-1)/2\rfloor$ (same as before), but we also need $d = Dk + a \leq 2015$.

So the analysis is the same: $a \leq \min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$, and additionally $a > k(2p + q - gpq)/2$ (if that's positive).

The lower bound doesn't affect the maximum. So my analysis is correct.

But wait, I should also check: when $gq > 2$ but $gpq < 2p + q$, does the lower bound ever conflict with the upper bound in the optimal region?

For $g = 1, q = 3, p = 4$: $gpq = 12$, $2p + q = 11$. $gpq > 2p + q$, so lower bound is $2a > k(11 - 12) = -k$, auto-satisfied. Good.

Let me also consider: what if $q = 1$ with higher $g$?

$g = 1, q = 1$: $gpq = p$, $2p + 1$. $p < 2p + 1$ always. And $gq = 1 < 3$. c<d: $2a > k(2p + 1 - p) = k(p+1)$. $a < k/2$, so $2a < k < k(p+1)$. Impossible. So $g = 1, q = 1$ never works.

$g = 2, q = 1$: $gq = 2 < 3$. $2a > k(2p + 1 - 2p) = k$. $2a < k$. Impossible.

$g = 3, q = 1$: $gq = 3$. $gpq = 3p$, $2p + 1$. $3p > 2p + 1$ for $p \geq 2$. Auto-satisfied. $a \approx 2015/(2p \cdot 2 - 1) = 2015/(4p - 1)$.
- $p = 2$: $2015/7 \approx 288$.
- $p = 3$: $2015/11 \approx 183$.

So $g = 3, q = 1, p = 2$ gives $a \approx 288$, worse than 464.

$g = 4, q = 1$: $D = 4p - p - 1 = 3p - 1$. $a \approx 2015/(2p \cdot 3 - 1) = 2015/(6p - 1)$.
- $p = 2$: $2015/11 \approx 183$. Worse.

OK so I'm fairly convinced the answer is $a = 464$.

But wait, let me reconsider. I've been assuming $p$ and $q$ are coprime. But what if they're not? Let me re-examine.

I had $s(m+1) = t(n+1)$, $g = \gcd(m+1, n+1)$, $m+1 = gp$, $n+1 = gq$, $\gcd(p, q) = 1$, $p > q$. Then $s = qk$, $t = pk$.

This is correct and covers all cases. The coprimality is built into the parametrization.

But actually, I realize I should also check: are there solutions where $s(m+1) = t(n+1)$ but with different structure? No, this is the complete characterization.

Let me also verify there's no issue with the constraint that all values must be in $\{1, ..., 2015\}$ and distinct with $a < b < c < d$.

For $g = 1, q = 3, p = 4, k = 310, a = 464$:
- $a = 464$
- $b = 930 - 464 = 466$
- $c = 1240 - 464 = 776$
- $d = 1550 + 464 = 2014$

All in $\{1, ..., 2015\}$, $464 < 466 < 776 < 2014$. ✓

$a + b = 930$, $c + d = 2790 = 3 \times 930$. ✓
$a + c = 1240$, $b + d = 2480 = 2 \times 1240$. ✓

Now, can we possibly get $a = 465$? We'd need $k$ such that $\lfloor(3k-1)/2\rfloor \geq 465$ and $2015 - 5k \geq 465$ (i.e., $k \leq 310$) and $3k \geq 931$ (i.e., $k \geq 311$). But $k \leq 310$ and $k \geq 311$ is impossible. So $a = 465$ is not achievable with this parametrization.

But could $a = 465$ be achievable with a different parametrization? Let me check all parametrizations that could give $a \geq 465$.

From the formula $a \approx \frac{2015q}{2p(gq-1) - q}$, the only parametrization giving $a \geq 465$ is $g = 1, q = 3, p = 4$ (giving $\approx 465$). All others give significantly less.

But let me be more careful. Let me check if any other $(g, p, q)$ can give $a \geq 465$.

We need $\frac{2015q}{2p(gq-1) - q} \geq 465$, i.e., $2015q \geq 465(2p(gq-1) - q) = 465 \cdot 2p(gq-1) - 465q$, i.e., $2480q \geq 930p(gq-1)$, i.e., $\frac{q}{p(gq-1)} \geq \frac{930}{2480} = \frac{93}{248}$.

So we need $\frac{q}{p(gq-1)} \geq \frac{93}{248} \approx 0.375$.

For $g = 1$: $\frac{q}{p(q-1)} \geq 0.375$. With $p = q+1$: $\frac{q}{(q+1)(q-1)} = \frac{q}{q^2-1} \geq 0.375$.
- $q = 3$: $3/8 = 0.375$. Exactly! So $a \approx 2015 \cdot 0.375 / (2 \cdot 0.375 - ... )$... hmm let me just compute. $\frac{3}{4 \cdot 2} = 3/8 = 0.375$. $a \approx 2015 \cdot 3 / (2 \cdot 4 \cdot 2 - 3) = 6045/13 = 465$. So $a \approx 465$ but we can only achieve 464.
- $q = 2$: $\frac{2}{3 \cdot 1} = 2/3 \approx 0.667 \geq 0.375$. But $g = 1, q = 2$ doesn't work (c<d constraint). 

Hmm wait, $q = 2, g = 1$ gives a higher ratio but doesn't work. What about $q = 2$ with $g = 2$?

$g = 2, q = 2, p = 3$: $\frac{2}{3 \cdot 3} = 2/9 \approx 0.222 < 0.375$. Doesn't reach 465.

What about non-coprime $p, q$? No, we defined $\gcd(p, q) = 1$.

What about $g = 1, q = 3, p = 3$? $\gcd(3, 3) = 3 \neq 1$. Not valid. But what if we absorb the gcd into $g$? If $p = q = 3$, then $m + 1 = 3g, n + 1 = 3g$, so $m = n$, which contradicts $m > n$. So this doesn't arise.

What about $g = 1, q = 3, p = 2$? $p < q$, not valid since $p > q$.

I think $a = 464$ is the answer. But let me also try to see if there's a completely different approach that might give a higher value.

Actually, let me reconsider the problem. Maybe I should try small examples to see if there's a pattern, or try to think about it differently.

Let me reconsider. We have:
- $a + b \mid c + d$, say $c + d = m(a+b)$
- $a + c \mid b + d$, say $b + d = n(a+c)$

With $m > n \geq 1$ (as shown).

From these: $c - b = m(a+b) - n(a+c)$, and $d = m(a+b) - c = n(a+c) - b$.

Let me try $n = 1$: $b + d = a + c$, so $d = a + c - b$. Then $c + d = c + a + c - b = a + 2c - b = m(a+b)$. So $a + 2c - b = m(a+b)$, giving $2c = m(a+b) - a + b = (m-1)a + (m+1)b$, so $c = \frac{(m-1)a + (m+1)b}{2}$.

For $c$ to be an integer, $(m-1)a + (m+1)b$ must be even.

$d = a + c - b = a + \frac{(m-1)a + (m+1)b}{2} - b = \frac{2a + (m-1)a + (m+1)b - 2b}{2} = \frac{(m+1)a + (m-1)b}{2}$.

Constraints:
- $c > b$: $\frac{(m-1)a + (m+1)b}{2} > b \Rightarrow (m-1)a + (m+1)b > 2b \Rightarrow (m-1)a > (1-m)b \Rightarrow (m-1)(a + b) > 0$. True for $m \geq 2$.
- $d > c$: $\frac{(m+1)a + (m-1)b}{2} > \frac{(m-1)a + (m+1)b}{2} \Rightarrow (m+1)a + (m-1)b > (m-1)a + (m+1)b \Rightarrow 2a > 2b$. But $a < b$! Contradiction!

So $n = 1$ is impossible (since $d > c$ requires $a > b$, contradiction).

So $n \geq 2$, meaning $m \geq 3$.

With $n = 2$: $b + d = 2(a + c)$, so $d = 2a + 2c - b$. And $c + d = m(a+b)$, so $c + 2a + 2c - b = m(a+b)$, giving $3c + 2a - b = m(a+b)$, so $3c = m(a+b) - 2a + b = (m-2)a + (m+1)b$, $c = \frac{(m-2)a + (m+1)b}{3}$.

$d = 2a + 2c - b = 2a + \frac{2(m-2)a + 2(m+1)b}{3} - b = \frac{6a + 2(m-2)a + 2(m+1)b - 3b}{3} = \frac{(2m+2)a + (2m-1)b}{3}$.

Constraints:
- $c$ integer: $3 \mid (m-2)a + (m+1)b$.
- $d$ integer: $3 \mid (2m+2)a + (2m-1)b$. (This follows from the first since $d = 2(a+c) - b$ and $c$ integer, $a, b$ integer.)
- $a < b < c < d$, all in $\{1, ..., 2015\}$.
- $d \leq 2015$.

$c > b$: $(m-2)a + (m+1)b > 3b \Rightarrow (m-2)a > (2-m)b \Rightarrow (m-2)(a+b) > 0$. True for $m \geq 3$.

$d > c$: $(2m+2)a + (2m-1)b > (m-2)a + (m+1)b \Rightarrow (m+4)a > (2-m)b \Rightarrow (m+4)a + (m-2)b > 0$. True for $m \geq 3$.

$d \leq 2015$: $\frac{(2m+2)a + (2m-1)b}{3} \leq 2015$.

To maximize $a$, we want $b$ close to $a$ (just $b = a + 1$ ideally, to minimize the contribution of $b$ to $d$) and $m$ small.

With $m = 3, n = 2$: This is exactly the case $g = 1, q = 3, p = 4$ (since $m + 1 = 4, n + 1 = 3$, $g = 1, p = 4, q = 3$).

$c = \frac{a + 4b}{3}$, $d = \frac{8a + 5b}{3}$.

For $c, d$ integers: $3 \mid a + 4b = a + b + 3b$, so $3 \mid a + b$. Let $a + b = 3k$.

Then $c = \frac{a + 4b}{3} = \frac{a + b + 3b}{3} = k + b$. And $d = \frac{8a + 5b}{3} = \frac{8a + 8b - 3b}{3} = \frac{8(a+b) - 3b}{3} = \frac{24k - 3b}{3} = 8k - b$.

So $c = k + b$, $d = 8k - b$, $a + b = 3k$, $a = 3k - b$.

Constraints:
- $a < b$: $3k - b < b \Rightarrow b > 3k/2$.
- $b < c = k + b$: always true. ✓
- $c < d$: $k + b < 8k - b \Rightarrow 2b < 7k \Rightarrow b < 7k/2$.
- $d \leq 2015$: $8k - b \leq 2015$.
- $a \geq 1$: $b \leq 3k - 1$.
- $b \geq 1$, $c \geq 1$, $d \geq 1$.
- All in $\{1, ..., 2015\}$.

$a = 3k - b$. To maximize $a$, minimize $b$. $b > 3k/2$, so $b \geq \lfloor 3k/2 \rfloor + 1$.

Also $d = 8k - b \leq 2015$, so $b \geq 8k - 2015$.

And $b < 7k/2$ (from c < d), so $b \leq \lfloor(7k-1)/2\rfloor$.

And $a = 3k - b \leq 2015$ (obviously, since $a < b \leq 2015$).

Also $c = k + b \leq 2015$, so $b \leq 2015 - k$.

So $b \geq \max(\lfloor 3k/2 \rfloor + 1, 8k - 2015, 1)$ and $b \leq \min(\lfloor(7k-1)/2\rfloor, 3k - 1, 2015 - k)$.

To maximize $a = 3k - b$, minimize $b$:
$b_{\min} = \max(\lfloor 3k/2 \rfloor + 1, 8k - 2015)$.

(We need $8k - 2015 \geq 1$ only if $k$ is large; for the optimal $k$, both constraints matter.)

$a = 3k - b_{\min}$.

If $b_{\min} = \lfloor 3k/2 \rfloor + 1$ (i.e., $a < b$ is binding): $a = 3k - \lfloor 3k/2 \rfloor - 1 = \lceil 3k/2 \rceil - 1$.

If $b_{\min} = 8k - 2015$ (i.e., $d \leq 2015$ is binding): $a = 3k - 8k + 2015 = 2015 - 5k$.

The crossover: $\lceil 3k/2 \rceil - 1 = 2015 - 5k$, roughly $3k/2 = 2016 - 5k$, $13k/2 = 2016$, $k = 2016 \cdot 2/13 = 4032/13 \approx 310.15$.

At $k = 310$: $b_{\min} = \max(\lfloor 465 \rfloor + 1, 2480 - 2015) = \max(466, 465) = 466$. $a = 930 - 466 = 464$.
At $k = 311$: $b_{\min} = \max(\lfloor 466.5 \rfloor + 1, 2488 - 2015) = \max(467, 473) = 473$. $a = 933 - 473 = 460$.

So $k = 310$ gives $a = 464$, which is the best for $m = 3, n = 2$.

Now let me check $m = 4, n = 2$: $m+1 = 5, n+1 = 3$, $g = \gcd(5,3) = 1$, $p = 5, q = 3$.

$c = \frac{(m-2)a + (m+1)b}{3} = \frac{2a + 5b}{3}$. $d = \frac{(2m+2)a + (2m-1)b}{3} = \frac{10a + 7b}{3}$.

$3 \mid 2a + 5b$. Let $2a + 5b = 3j$. Then $c = j$, $d = \frac{10a + 7b}{3}$.

Actually, let me use the parametrization. $s = a + b = 3k$, $t = a + c = 5k$. $a = 3k - b$, $c = 5k - a = 5k - 3k + b = 2k + b$. $d = Dk + a = (gpq - p - q)k + a = (15 - 5 - 3)k + a = 7k + a = 7k + 3k - b = 10k - b$.

Constraints:
- $a < b$: $b > 3k/2$.
- $c < d$: $2k + b < 10k - b \Rightarrow 2b < 8k \Rightarrow b < 4k$.
- $d \leq 2015$: $10k - b \leq 2015 \Rightarrow b \geq 10k - 2015$.
- $c \leq 2015$: $2k + b \leq 2015$.

$a = 3k - b$, minimize $b$: $b_{\min} = \max(\lfloor 3k/2 \rfloor + 1, 10k - 2015)$.

Crossover: $3k/2 \approx 10k - 2015$, $2015 \approx 17k/2$, $k \approx 4030/17 \approx 237$.

At $k = 237$: $b_{\min} = \max(\lfloor 355.5 \rfloor + 1, 2370 - 2015) = \max(356, 355) = 356$. $a = 711 - 356 = 355$.

So $a = 355$, worse than 464.

$m = 3, n = 2$ is the best with $n = 2$.

Now let me try $n = 3, m = 4$: $m + 1 = 5, n + 1 = 4$, $g = 1, p = 5, q = 4$.

$s = 4k, t = 5k$. $a = 4k - b$, $c = 5k - a = k + b$, $d = (20 - 5 - 4)k + a = 11k + a = 11k + 4k - b = 15k - b$.

$b > 2k$ (from $a < b$), $d \leq 2015$: $b \geq 15k - 2015$.

Crossover: $2k \approx 15k - 2015$, $13k \approx 2015$, $k \approx 155$.

At $k = 155$: $b_{\min} = \max(311, 2325 - 2015) = \max(311, 310) = 311$. $a = 620 - 311 = 309$.

Worse.

$n = 2, m = 3$ is the winner so far. Let me also try $n = 3, m = 5$: $m+1 = 6, n+1 = 4$, $g = 2, p = 3, q = 2$.

$s = 2k, t = 3k$. $a = 2k - b$, $c = 3k - a = k + b$, $d = (12 - 3 - 2)k + a = 7k + a = 7k + 2k - b = 9k - b$.

$b > k$ (from $a < b$), $d \leq 2015$: $b \geq 9k - 2015$.

Crossover: $k \approx 9k - 2015$, $8k \approx 2015$, $k \approx 252$.

At $k = 252$: $b_{\min} = \max(253, 2268 - 2015) = \max(253, 253) = 253$. $a = 504 - 253 = 251$.

Worse.

Let me try $n = 2, m = 5$: $m+1 = 6, n+1 = 3$, $g = 3, p = 2, q = 1$.

$s = k, t = 2k$. $a = k - b$, $c = 2k - a = k + b$, $d = (6 - 2 - 1)k + a = 3k + a = 3k + k - b = 4k - b$.

$b > k/2$ (from $a < b$), $d \leq 2015$: $b \geq 4k - 2015$.

Crossover: $k/2 \approx 4k - 2015$, $7k/2 \approx 2015$, $k \approx 576$.

At $k = 576$: $b_{\min} = \max(289, 2304 - 2015) = \max(289, 289) = 289$. $a = 576 - 289 = 287$.

This is the $g = 3, q = 1, p = 2$ case. $a = 287$. Worse than 464.

So the best is $a = 464$ with $m = 3, n = 2$.

Let me also try $n = 4, m = 5$: $m+1 = 6, n+1 = 5$, $g = 1, p = 6, q = 5$.

$s = 5k, t = 6k$. $a = 5k - b$, $c = 6k - a = k + b$, $d = (30 - 6 - 5)k + a = 19k + a = 19k + 5k - b = 24k - b$.

$b > 5k/2$, $d \leq 2015$: $b \geq 24k - 2015$.

Crossover: $5k/2 \approx 24k - 2015$, $43k/2 \approx 2015$, $k \approx 93.7$.

At $k = 94$: $b_{\min} = \max(236, 2256 - 2015) = \max(236, 241) = 241$. $a = 470 - 241 = 229$. Worse.

What about $n = 2, m = 4$? Already checked: $a = 355$.

$n = 2, m = 6$? $m+1 = 7, n+1 = 3$, $g = 1, p = 7, q = 3$.

$s = 3k, t = 7k$. $a = 3k - b$, $c = 7k - a = 4k + b$, $d = (21 - 7 - 3)k + a = 11k + a = 11k + 3k - b = 14k - b$.

$b > 3k/2$, $d \leq 2015$: $b \geq 14k - 2015$.

Crossover: $3k/2 \approx 14k - 2015$, $25k/2 \approx 2015$, $k \approx 161.2$.

At $k = 161$: $b_{\min} = \max(242, 2254 - 2015) = \max(242, 239) = 242$. $a = 483 - 242 = 241$. Worse.

So indeed $m = 3, n = 2$ (i.e., $g = 1, q = 3, p = 4$) gives the best result of $a = 464$.

Let me also try some other combinations just to be thorough:

$n = 3, m = 4$: already checked, $a = 309$.
$n = 4, m = 7$: $m+1 = 8, n+1 = 5$, $g = 1, p = 8, q = 5$. $D = 40 - 8 - 5 = 27$. $a \approx 2015 \cdot 5 / (2 \cdot 8 \cdot 4 - 5) = 10075/59 \approx 170$. Worse.

$n = 5, m = 6$: $m+1 = 7, n+1 = 6$, $g = 1, p = 7, q = 6$. $D = 42 - 7 - 6 = 29$. $a \approx 2015 \cdot 6 / (2 \cdot 7 \cdot 5 - 6) = 12090/64 \approx 189$. Worse.

I'm now confident the answer is $\boxed{464}$.

Wait, but let me reconsider. I want to make sure I haven't missed any case. Let me think about whether there could be solutions with very different structure.

The key equation is $s(m+1) = t(n+1)$ where $s = a+b, t = a+c, m > n \geq 2$ (we showed $n \geq 2$).

With $g = \gcd(m+1, n+1)$, $p = (m+1)/g$, $q = (n+1)/g$, $\gcd(p,q) = 1$, $p > q$.

$s = qk, t = pk$, $D = gpq - p - q$, $d = Dk + a$, $a = qk - b$.

$a \leq \lfloor(qk-1)/2\rfloor$ and $d = Dk + a \leq 2015$.

Max $a \approx \frac{2015q}{2D + q} = \frac{2015q}{2gpq - 2p - q}$.

We need $n \geq 2$, so $gq \geq 3$ (since $n = gq - 1 \geq 2$ means $gq \geq 3$).

And $m \geq 3$, so $gp \geq 4$.

To maximize $\frac{q}{2gpq - 2p - q} = \frac{q}{2p(gq - 1) - q}$:

Let $f = 2p(gq - 1) - q$. We want to minimize $f/q = 2p(gq-1)/q - 1 = 2p(g - 1/q) - 1$.

Since $p \geq q + 1$ (coprime, $p > q$) and $g \geq 1$, $gq \geq 3$:

For $g = 1$: $f/q = 2p(1 - 1/q) - 1 = 2p(q-1)/q - 1$. With $p = q+1$: $2(q+1)(q-1)/q - 1 = 2(q^2-1)/q - 1 = 2q - 2/q - 1$.
- $q = 3$: $6 - 2/3 - 1 = 13/3$. $a \approx 2015/(13/3) = 6045/13 \approx 465$.
- $q = 4$: $8 - 1/2 - 1 = 6.5$. $a \approx 2015 \cdot 4 / (2 \cdot 6.5 \cdot 4) $... wait, $a \approx 2015q/f = 2015 \cdot 4 / (2 \cdot 5 \cdot 3 - 4) = 8060/26 = 310$.
- $q = 5$: $10 - 2/5 - 1 = 8.6$. $a \approx 2015 \cdot 5 / (2 \cdot 6 \cdot 4 - 5) = 10075/43 \approx 234$.

For $g = 2$: $f/q = 2p(2 - 1/q) - 1$. With $p = q + 1$ (if coprime):
- $q = 2, p = 3$: $f = 2 \cdot 3 \cdot 3 - 2 = 16$. $a \approx 2015 \cdot 2/16 = 251.9$.
- $q = 3, p = 4$: $f = 2 \cdot 4 \cdot 5 - 3 = 37$. $a \approx 6045/37 \approx 163$.

For $g = 3$: $f/q = 2p(3 - 1/q) - 1$.
- $q = 1, p = 2$: $f = 2 \cdot 2 \cdot 2 - 1 = 7$. $a \approx 2015/7 \approx 287.9$.
- $q = 1, p = 4$ (coprime with 1): $f = 2 \cdot 4 \cdot 2 - 1 = 15$. $a \approx 2015/15 \approx 134$.

For $g = 4$:
- $q = 1, p = 2$: $f = 2 \cdot 2 \cdot 3 - 1 = 11$. $a \approx 2015/11 \approx 183$.

So the global maximum of the approximate $a$ is at $g = 1, q = 3, p = 4$, giving $a \approx 465$, and the exact maximum is $a = 464$.

Let me verify once more that $a = 464$ works and $a = 465$ doesn't.

$a = 464, b = 466, c = 776, d = 2014$:
- $a + b = 930$, $c + d = 2790 = 3 \times 930$. ✓
- $a + c = 1240$, $b + d = 2480 = 2 \times 1240$. ✓
- $464 < 466 < 776 < 2014$. ✓
- All in $\{1, ..., 2015\}$. ✓

For $a = 465$: We need $m = 3, n = 2$ (the only parametrization that could work). $a + b = 3k$, $b > 3k/2$, so $a = 3k - b < 3k/2$. $a = 465$ requires $3k/2 > 465$, $k > 310$, so $k \geq 311$. Then $d = 8k - b \geq 8 \cdot 311 - b$. With $b > 3 \cdot 311 / 2 = 466.5$, $b \geq 467$. $d = 8 \cdot 311 - 467 = 2488 - 467 = 2021 > 2015$. ✗

Alternatively, $b$ larger to reduce $d$: $d = 8k - b \leq 2015$ requires $b \geq 8k - 2015 = 8 \cdot 311 - 2015 = 2488 - 2015 = 473$. Then $a = 933 - 473 = 460 < 465$. ✗

So $a = 465$ is impossible. The answer is $a = 464$.

Actually, hold on. I want to make sure I haven't missed any parametrization. Let me think about whether there could be other $(m, n)$ pairs that I haven't considered.

The formula $a \approx \frac{2015q}{2p(gq-1) - q}$ where $g = \gcd(m+1, n+1)$, $p = (m+1)/g$, $q = (n+1)/g$.

I need $n \geq 2$ (so $gq \geq 3$) and $m \geq 3$ (so $gp \geq 4$).

I've checked:
- $(m, n) = (3, 2)$: $g=1, p=4, q=3$. $a = 464$. ✓ Best.
- $(m, n) = (4, 2)$: $g=1, p=5, q=3$. $a = 355$.
- $(m, n) = (5, 2)$: $g=3, p=2, q=1$. $a = 287$.
- $(m, n) = (6, 2)$: $g=1, p=7, q=3$. $a = 241$.
- $(m, n) = (4, 3)$: $g=1, p=5, q=4$. $a = 309$.
- $(m, n) = (5, 3)$: $g=2, p=3, q=2$. $a = 251$.
- $(m, n) = (5, 4)$: $g=1, p=6, q=5$. $a = 229$.
- $(m, n) = (7, 2)$: $g=1, p=8, q=3$. $D = 24 - 8 - 3 = 13$. $a \approx 6045/(2 \cdot 8 \cdot 2 - 3) = 6045/29 \approx 208$.
- $(m, n) = (3, 2)$ variants with different $g$: already covered.

I think I've been thorough enough. The answer is $a = 464$.

Hmm, but actually let me reconsider one more time. I want to check: is the formula $a \approx \frac{2015q}{2D+q}$ always achievable? The exact maximum is $\min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$ optimized over $k$. Let me verify for a few more cases that the exact value doesn't exceed 464.

For $(m, n) = (7, 3)$: $g = \gcd(8, 4) = 4$, $p = 2, q = 1$. $D = 8 - 2 - 1 = 5$. $a \leq \min(\lfloor(k-1)/2\rfloor, 2015 - 5k)$. Crossover: $k/2 \approx 2015 - 5k$, $11k/2 \approx 2015$, $k \approx 366.4$. At $k = 366$: $\min(182, 2015 - 1830) = \min(182, 185) = 182$. At $k = 367$: $\min(183, 2015 - 1835) = \min(183, 180) = 180$. So max $a = 182$. Worse.

For $(m, n) = (8, 3)$: $g = \gcd(9, 4) = 1$, $p = 9, q = 4$. $D = 36 - 9 - 4 = 23$. $a \approx 2015 \cdot 4 / (2 \cdot 9 \cdot 3 - 4) = 8060/50 = 161.2$. Worse.

For $(m, n) = (3, 2)$ is clearly the best. Let me also check $(m, n) = (3, 2)$ but with $g > 1$... wait, $g = \gcd(4, 3) = 1$, so there's only one option.

I'm confident. The answer is $\boxed{464}$.

Let me now also think about whether I need to prove that no other parametrization can beat 464, more rigorously.

We showed that $a \leq \frac{2015q}{2D + q}$ approximately, where $D = gpq - p - q \geq 1$ (need $D \geq 1$ for $d > a$). Actually $D$ could be 0 only if $gpq = p + q$, which for $g = 1$ means $pq = p + q$, i.e., $(p-1)(q-1) = 1$, so $p = q = 2$, but $p > q$ so impossible. For $g \geq 2$, $gpq \geq 2pq \geq 2 \cdot 2 \cdot 1 = 4 > p + q$ when $p + q \leq 3$... actually for $g = 2, p = 2, q = 1$: $gpq = 4, p + q = 3$, $D = 1$. For $g = 2, p = 3, q = 1$: $gpq = 6, p+q = 4, D = 2$. So $D \geq 1$ always (given $gq \geq 3, gp \geq 4, p > q \geq 1$).

The exact bound: $a \leq \min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$ for some positive integer $k$.

The maximum over $k$ of $\min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$ is at most $\frac{2015q}{2D + q}$ (achieved when the two expressions are equal).

So $a \leq \frac{2015q}{2D + q} = \frac{2015q}{2gpq - 2p - q}$.

We need to show that for all valid $(g, p, q)$ with $gq \geq 3$, $gp \geq 4$, $p > q \geq 1$, $\gcd(p, q) = 1$, we have $\frac{2015q}{2gpq - 2p - q} \leq 465$ (approximately), with equality only at $(g, p, q) = (1, 4, 3)$.

$\frac{q}{2gpq - 2p - q} \leq \frac{465}{2015} = \frac{93}{403}$.

So we need $403q \leq 93(2gpq - 2p - q) = 186gpq - 186p - 93q$, i.e., $496q \leq 186gpq - 186p$, i.e., $186p(gq - 1) \geq 496q$, i.e., $p(gq - 1) \geq \frac{496q}{186} = \frac{248q}{93}$.

For $(g, p, q) = (1, 4, 3)$: $p(gq-1) = 4 \cdot 2 = 8$. $\frac{248 \cdot 3}{93} = \frac{744}{93} = 8$. Equality! So $a \leq 465$ approximately, and the exact value is 464.

For any other $(g, p, q)$, we need $p(gq - 1) > \frac{248q}{93}$, i.e., $p(gq-1) \geq 8 + \epsilon$ for some $\epsilon > 0$ (since $p(gq-1)$ is an integer and equals 8 only at $(1, 4, 3)$... let me check).

$p(gq - 1) = 8$: 
- $g = 1$: $p(q-1) = 8$. $(p, q)$ coprime, $p > q \geq 3$ (since $gq \geq 3$). $q = 3, p = 4$: $4 \cdot 2 = 8$. ✓ $q = 4, p = 8/3$ not integer. $q = 5, p = 2$ but $p < q$. $q = 9, p = 1$ but $p < q$. So only $(p, q) = (4, 3)$.
- $g = 2$: $p(2q - 1) = 8$. $q = 1, p = 8$ but $gq = 2 < 3$. $q = 2, p = 8/3$ not integer. No valid.
- $g = 3$: $p(3q - 1) = 8$. $q = 1, p = 2$: $2 \cdot 2 = 4 \neq 8$. $q = 1, p = 4$: $4 \cdot 2 = 8$. ✓ But $gq = 3 \geq 3$, $gp = 12 \geq 4$. Valid! $(g, p, q) = (3, 4, 1)$.

Wait! $(g, p, q) = (3, 4, 1)$: $D = 12 - 4 - 1 = 7$. $a \approx 2015 \cdot 1 / (2 \cdot 7 + 1) = 2015/15 \approx 134.3$. 

Hmm, but $p(gq-1) = 4 \cdot 2 = 8 = 248 \cdot 1 / 93 = 248/93 \approx 2.67$. Wait, that doesn't match. Let me recompute.

$p(gq - 1) \geq \frac{248q}{93}$. For $(g, p, q) = (3, 4, 1)$: $p(gq - 1) = 4 \cdot 2 = 8$. $\frac{248 \cdot 1}{93} = 248/93 \approx 2.67$. So $8 \geq 2.67$. ✓ But the approximate $a$ is $2015 \cdot 1 / (2 \cdot 7 + 1) = 2015/15 \approx 134$, which is much less than 465.

I think I made an error. Let me redo. $a \approx \frac{2015q}{2D + q}$. For $(3, 4, 1)$: $D = 7$, $a \approx 2015/(14 + 1) = 2015/15 \approx 134$. For $(1, 4, 3)$: $D = 5$, $a \approx 2015 \cdot 3 / (10 + 3) = 6045/13 \approx 465$.

The condition $p(gq-1) = 8$ doesn't mean $a$ is the same; it means $\frac{q}{2D+q}$ is the same ratio... let me recheck.

$\frac{q}{2D + q} = \frac{q}{2(gpq - p - q) + q} = \frac{q}{2gpq - 2p - q}$. 

For $(1, 4, 3)$: $\frac{3}{24 - 8 - 3} = 3/13$.
For $(3, 4, 1)$: $\frac{1}{24 - 8 - 1} = 1/15$.

These are different! So my algebraic manipulation was wrong. Let me redo.

$\frac{q}{2gpq - 2p - q} \leq \frac{93}{403}$?

$403q \leq 93(2gpq - 2p - q) = 186gpq - 186p - 93q$
$496q \leq 186gpq - 186p = 186p(gq - 1)$
$\frac{496q}{186} \leq p(gq - 1)$
$\frac{248q}{93} \leq p(gq - 1)$

For $(1, 4, 3)$: $p(gq-1) = 4 \cdot 2 = 8$. $\frac{248 \cdot 3}{93} = 8$. Equality. ✓
For $(3, 4, 1)$: $p(gq-1) = 4 \cdot 2 = 8$. $\frac{248 \cdot 1}{93} = 248/93 \approx 2.67$. $8 \geq 2.67$. ✓ (satisfies the inequality, meaning $a \leq 465$)

So the condition $p(gq-1) \geq \frac{248q}{93}$ is satisfied by $(3, 4, 1)$, but that just means $a \leq 465$ for that case too. The actual $a$ for $(3, 4, 1)$ is much smaller (134).

The point is: equality $p(gq-1) = \frac{248q}{93}$ holds only when $\frac{q}{2D+q} = \frac{93}{403}$, which gives $a \approx 465$. For $(3, 4, 1)$, $p(gq-1) = 8 > 248/93$, so $\frac{q}{2D+q} < 93/403$, meaning $a < 465$.

So I need to find all $(g, p, q)$ where $p(gq - 1) = \frac{248q}{93}$, i.e., $93 \cdot p(gq-1) = 248q$.

$93p(gq - 1) = 248q$. Since $\gcd(93, 248) = \gcd(93, 248)$. $93 = 3 \cdot 31$, $248 = 8 \cdot 31$. $\gcd = 31$. So $3p(gq-1) = 8q$.

So $3p(gq - 1) = 8q$. This means $3 \mid 8q$, i.e., $3 \mid q$ (since $\gcd(3, 8) = 1$). Let $q = 3r$. Then $3p(3gr - 1) = 24r$, i.e., $p(3gr - 1) = 8r$.

For $r = 1, q = 3$: $p(3g - 1) = 8$.
- $g = 1$: $p \cdot 2 = 8$, $p = 4$. $\gcd(4, 3) = 1$. ✓ $(g, p, q) = (1, 4, 3)$.
- $g = 2$: $p \cdot 5 = 8$, $p = 8/5$. Not integer.
- $g = 3$: $p \cdot 8 = 8$, $p = 1$. But $p > q = 3$. ✗

For $r = 2, q = 6$: $p(6g - 1) = 16$.
- $g = 1$: $p \cdot 5 = 16$. Not integer.
- $g = 2$: $p \cdot 11 = 16$. Not integer.
- $g = 3$: $p \cdot 17 = 16$. $p < 1$. ✗

For $r = 3, q = 9$: $p(9g - 1) = 24$.
- $g = 1$: $p \cdot 8 = 24$, $p = 3$. But $p > q = 9$? No, $3 < 9$. ✗

For larger $r$, $p$ gets smaller relative to $q$, so $p > q$ fails.

So the only solution to $3p(gq-1) = 8q$ with $p > q \geq 1$, $\gcd(p,q) = 1$, $gq \geq 3$, $gp \geq 4$ is $(g, p, q) = (1, 4, 3)$.

This means $(1, 4, 3)$ is the unique parametrization achieving $a \approx 465$, and all others give strictly less. The exact maximum for $(1, 4, 3)$ is $a = 464$ (since the approximate value 465 is not achievable due to integrality).

Therefore, the greatest value of $a$ is $\boxed{464}$.

Now let me write up the proof properly.

Actually, let me reconsider the proof structure. I need to:
1. Set up the parametrization
2. Show that $a \leq 464$ for all valid configurations
3. Exhibit a configuration with $a = 464$

For step 2, I need to show that for all $(g, p, q)$ other than $(1, 4, 3)$, the approximate upper bound is $< 465$, and for $(1, 4, 3)$, the exact maximum is 464.

Let me think about a cleaner way to present this.

The key steps:
1. From $a+b \mid c+d$ and $a+c \mid b+d$, derive $s(m+1) = t(n+1)$ where $s = a+b, t = a+c, m > n \geq 2$.
2. Parametrize: $g = \gcd(m+1, n+1)$, $p = (m+1)/g, q = (n+1)/g$, $\gcd(p,q) = 1$, $p > q$, $gq \geq 3$.
3. $s = qk, t = pk$, $a = qk - b$, $d = (gpq - p - q)k + a$.
4. $a < b$ gives $a \leq \lfloor(qk-1)/2\rfloor$.
5. $d \leq 2015$ gives $a \leq 2015 - (gpq - p - q)k$.
6. So $a \leq \min(\lfloor(qk-1)/2\rfloor, 2015 - Dk)$ where $D = gpq - p - q$.
7. The maximum of this over $k$ is at most $\frac{2015q}{2D + q}$ (by AM-like argument).
8. Show $\frac{2015q}{2D+q} \leq 465$ for all valid $(g, p, q)$, with equality only at $(1, 4, 3)$.
9. For $(1, 4, 3)$: exact computation gives $a = 464$.
10. Exhibit the solution.

For step 7-8: $\frac{2015q}{2D+q} \leq 465 \iff 2015q \leq 465(2D + q) = 930D + 465q \iff 1550q \leq 930D \iff D \geq \frac{1550q}{930} = \frac{155q}{93} = \frac{5q}{3}$.

So we need $D = gpq - p - q \geq \frac{5q}{3}$, i.e., $gpq - p - q \geq \frac{5q}{3}$, i.e., $gpq - p \geq q + \frac{5q}{3} = \frac{8q}{3}$, i.e., $p(gq - 1) \geq \frac{8q}{3}$, i.e., $3p(gq - 1) \geq 8q$.

We need to show $3p(gq - 1) \geq 8q$ for all valid $(g, p, q)$ with $gq \geq 3$, $p > q \geq 1$, $\gcd(p, q) = 1$, and $p \geq 2$ (since $gp \geq 4$ and $g \geq 1$ means $p \geq 2$... actually $gp \geq 4$ and $g \geq 1$ means $p \geq 4$ if $g = 1$, or $p \geq 2$ if $g \geq 2$).

Hmm, this is getting complicated. Let me just enumerate cases.

Case 1: $g = 1$. Then $q \geq 3$ (since $gq \geq 3$), $p \geq q + 1 \geq 4$.
$3p(q - 1) \geq 8q$. Since $p \geq q + 1$: $3(q+1)(q-1) = 3(q^2 - 1) \geq 8q$, i.e., $3q^2 - 8q - 3 \geq 0$. Discriminant: $64 + 36 = 100$, roots: $(8 \pm 10)/6$. Positive root: $18/6 = 3$. So $q \geq 3$ satisfies this. Equality at $q = 3$.

For $q = 3, p = 4$: $3 \cdot 4 \cdot 2 = 24 = 8 \cdot 3$. Equality. So $a \leq 465$ (approximately), and exact is 464.

For $q = 3, p \geq 5$: $3p \cdot 2 = 6p \geq 30 > 
