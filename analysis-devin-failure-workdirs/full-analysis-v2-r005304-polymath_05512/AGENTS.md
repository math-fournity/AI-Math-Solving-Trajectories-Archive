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
  <problem_id>polymath_05512</problem_id>
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

Prime $p>2$ and a polynomial $Q$ with integer coefficients are such that there are no integers $1 \le i < j \le p-1$ for which $(Q(j)-Q(i))(jQ(j)-iQ(i))$ is divisible by $p$. What is the smallest possible degree of $Q$?

[i](Proposed by Anton Trygub)[/i]

## Standard Solution

1. **Understanding the problem**: We need to find the smallest possible degree of a polynomial \( Q \) with integer coefficients such that for any integers \( 1 \le i < j \le p-1 \), the product \((Q(j)-Q(i))(jQ(j)-iQ(i))\) is not divisible by the prime \( p \).

2. **Initial assumptions**: Assume \( Q \) is the polynomial with the smallest degree that satisfies the given condition. We need to explore the possible degrees of \( Q \).

3. **Degree analysis**:
    - **Case 1**: \( \deg(Q) > p-1 \). Using Fermat's Little Theorem, \( x^p \equiv x \pmod{p} \), we get a contradiction because the degree of \( Q \) would not be minimal.
    - **Case 2**: \( \deg(Q) = p-1 \). Using the identity \( x^{p-1} \equiv 1 \pmod{p} \) for \( x \) in the range \( 1 \le x \le p-1 \), we can reduce the polynomial modulo \( p \). This would imply that \( Q \) can be reduced to a polynomial of degree less than \( p-1 \), contradicting the minimality assumption.
    - **Case 3**: \( \deg(Q) < p-2 \). We need to show that this leads to a contradiction.

4. **Detailed analysis for \( \deg(Q) < p-2 \)**:
    - **Subcase 1**: \( (Q(i), p) = 1 \) for all \( i \) in \( \{1, 2, \ldots, p-1\} \). This implies that \( \{Q(1), Q(2), \ldots, Q(p-1)\} \) and \( \{1 \cdot Q(1), 2 \cdot Q(2), \ldots, (p-1) \cdot Q(p-1)\} \) are two complete residue systems modulo \( p \). By Wilson's Theorem, we have:
        \[
        Q(1) \cdot Q(2) \cdot \ldots \cdot Q(p-1) \equiv -1 \pmod{p}
        \]
        and
        \[
        (1 \cdot Q(1)) \cdot (2 \cdot Q(2)) \cdot \ldots \cdot ((p-1) \cdot Q(p-1)) \equiv -1 \pmod{p}
        \]
        However, this product can also be written as:
        \[
        (1 \cdot 2 \cdot \ldots \cdot (p-1)) \cdot (Q(1) \cdot Q(2) \cdot \ldots \cdot Q(p-1)) \equiv (-1) \cdot (-1) \equiv 1 \pmod{p}
        \]
        This is a contradiction.
    - **Subcase 2**: There exists \( i \) such that \( Q(i) \equiv 0 \pmod{p} \). Since \( \deg(Q) < p-2 \), the degree of \( xQ(x) \) is at most \( p-2 \). We have the identity:
        \[
        \sum_{i=0}^{p-1} iQ(i) \equiv 0 \pmod{p} \implies \sum_{i=1}^{p-1} iQ(i) \equiv 0 \pmod{p}
        \]
        Given that there exists \( i \) such that \( Q(i) \equiv 0 \pmod{p} \), the set \( \{1 \cdot Q(1), 2 \cdot Q(2), \ldots, (i-1) \cdot Q(i-1), (i+1) \cdot Q(i+1), \ldots, (p-1) \cdot Q(p-1)\} \) is similar to \( \{1, 2, \ldots, i-1, i+1, \ldots, p-1\} \). From the identity, we get:
        \[
        1 + 2 + \ldots + (p-1) - x \equiv 0 \pmod{p} \implies x \equiv 0 \pmod{p}
        \]
        This is a contradiction since \( x \) is in the range \( 1 \le x \le p-1 \).

5. **Conclusion**: The smallest possible degree of \( Q \) that avoids the contradictions in all cases is \( p-2 \).

The final answer is \( \boxed{ p-2 } \)

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a prime $p > 2$ and a polynomial $Q$ with integer coefficients such that there are no integers $1 \le i < j \le p-1$ for which $(Q(j) - Q(i))(jQ(j) - iQ(i))$ is divisible by $p$.

We need to find the smallest possible degree of $Q$.

Let me think about this. We work modulo $p$. The condition is that for all $1 \le i < j \le p-1$ (so $i, j \in \{1, 2, \ldots, p-1\}$, which are the nonzero elements of $\mathbb{F}_p$), we need:
$$p \nmid (Q(j) - Q(i))(jQ(j) - iQ(i))$$

This means both:
1. $Q(j) \not\equiv Q(i) \pmod{p}$ (so $Q$ is injective on $\{1, \ldots, p-1\}$ mod $p$)
2. $jQ(j) \not\equiv iQ(i) \pmod{p}$ (so the function $x \mapsto xQ(x)$ is also injective on $\{1, \ldots, p-1\}$ mod $p$)

Since $\{1, \ldots, p-1\}$ has $p-1$ elements and we're mapping into $\mathbb{F}_p$, injectivity means $Q$ permutes $\{1, \ldots, p-1\}$ into some subset of size $p-1$ of $\mathbb{F}_p$, and similarly $xQ(x)$ permutes $\{1, \ldots, p-1\}$ into some subset of size $p-1$.

Wait, actually injective from a set of size $p-1$ to $\mathbb{F}_p$ (size $p$) means the image has size $p-1$, so exactly one element of $\mathbb{F}_p$ is missed.

Let me think about what $Q$ restricted to $\mathbb{F}_p^*$ looks like. Since we only care about $Q$ on $\{1, \ldots, p-1\} = \mathbb{F}_p^*$, we can think of $Q$ as a function from $\mathbb{F}_p^*$ to $\mathbb{F}_p$.

Condition 1: $Q: \mathbb{F}_p^* \to \mathbb{F}_p$ is injective.
Condition 2: $x \cdot Q(x): \mathbb{F}_p^* \to \mathbb{F}_p$ is injective.

Now, any function from $\mathbb{F}_p^*$ to $\mathbb{F}_p$ can be represented by a polynomial of degree at most $p-2$ (since $\mathbb{F}_p^*$ has $p-1$ elements, a polynomial of degree $\leq p-2$ is determined by its values on $p-1$ points... wait, actually a polynomial of degree $\leq p-2$ has $p-1$ coefficients, so it's determined by $p-1$ values). Actually, the space of polynomials of degree $\leq d$ has dimension $d+1$. To interpolate $p-1$ points, we need degree $p-2$.

But actually, we can also use the fact that on $\mathbb{F}_p^*$, $x^{p-1} = 1$, so $x^{p-1}$ acts like the constant 1. So any polynomial, when restricted to $\mathbb{F}_p^*$, is equivalent to one of degree $\leq p-2$.

So the question is: what is the minimum degree $d$ such that there exists a polynomial $Q$ of degree $d$ (with integer coefficients, but we work mod $p$) satisfying both injectivity conditions on $\mathbb{F}_p^*$?

Let me think about small cases and try to find a pattern.

For $Q$ to be injective on $\mathbb{F}_p^*$, and $xQ(x)$ to be injective on $\mathbb{F}_p^*$.

Let me think of $Q$ as a permutation-like function. Actually, $Q$ maps $\mathbb{F}_p^*$ (size $p-1$) injectively into $\mathbb{F}_p$ (size $p$), so it misses exactly one value.

Let me consider $Q(x) = x^k$ for some $k$. Then:
- Condition 1: $x^k$ is injective on $\mathbb{F}_p^*$ iff $\gcd(k, p-1) = 1$.
- Condition 2: $x \cdot x^k = x^{k+1}$ is injective on $\mathbb{F}_p^*$ iff $\gcd(k+1, p-1) = 1$.

So we need $\gcd(k, p-1) = 1$ and $\gcd(k+1, p-1) = 1$.

Since $p-1$ is even (as $p > 2$), $k$ and $k+1$ are consecutive, so one is even and one is odd. For $\gcd(k, p-1) = 1$ and $\gcd(k+1, p-1) = 1$, we need both $k$ and $k+1$ to be coprime to $p-1$.

Since $p-1$ is even, one of $k, k+1$ is even, so it shares a factor of 2 with $p-1$. This means we can't have both coprime to $p-1$ if $p-1$ is even. Wait, that's not right. $\gcd(\text{even number}, p-1)$ where $p-1$ is even - the even number shares factor 2 with $p-1$, so $\gcd \geq 2 > 1$.

So $Q(x) = x^k$ doesn't work for any $k$ when $p > 2$! Because $p-1$ is even, and one of $k, k+1$ is even, so one of $\gcd(k, p-1), \gcd(k+1, p-1)$ is $\geq 2$.

Hmm, so monomials don't work. We need a more general polynomial.

Let me think about this differently. Let's consider the problem more carefully.

We need $Q: \mathbb{F}_p^* \to \mathbb{F}_p$ injective, and $xQ(x): \mathbb{F}_p^* \to \mathbb{F}_p$ injective.

Let $f = Q|_{\mathbb{F}_p^*}$ and $g = (x \mapsto xQ(x))|_{\mathbb{F}_p^*}$. Both are injective maps from $\mathbb{F}_p^*$ to $\mathbb{F}_p$.

The image of $f$ misses one element of $\mathbb{F}_p$, say $a$. The image of $g$ misses one element, say $b$.

Now, $g(x) = x \cdot f(x)$. So the image of $g$ is $\{x \cdot f(x) : x \in \mathbb{F}_p^*\}$.

Let me think about what constraints this places.

Actually, let me think about the degree more carefully. The degree of $Q$ as a polynomial with integer coefficients. Since we only care about values mod $p$, and on $\mathbb{F}_p^*$ we can reduce degree mod $p-1$ (since $x^{p-1} \equiv 1$), the effective degree on $\mathbb{F}_p^*$ is at most $p-2$.

But the question asks for the smallest possible degree of $Q$ as a polynomial with integer coefficients. So we want to minimize the actual degree.

Let me try small primes.

$p = 3$: $\mathbb{F}_3^* = \{1, 2\}$. We need $Q(1) \neq Q(2) \pmod{3}$ and $1 \cdot Q(1) \neq 2 \cdot Q(2) \pmod{3}$.

So $Q(1) \neq Q(2)$ and $Q(1) \neq 2Q(2) \pmod{3}$.

Try $Q(x) = x$: $Q(1) = 1, Q(2) = 2$. Check: $1 \neq 2$ ✓, $1 \neq 2 \cdot 2 = 4 \equiv 1 \pmod{3}$. So $Q(1) = 1 = 2Q(2) = 1$. Fails!

Try $Q(x) = 2x$: $Q(1) = 2, Q(2) = 4 \equiv 1$. Check: $2 \neq 1$ ✓, $2 \neq 2 \cdot 1 = 2$. Fails! $Q(1) = 2 = 2Q(2) = 2$.

Try $Q(x) = x + 1$: $Q(1) = 2, Q(2) = 3 \equiv 0$. Check: $2 \neq 0$ ✓, $2 \neq 2 \cdot 0 = 0$ ✓. Works! Degree 1.

So for $p = 3$, degree 1 works. Let me check: $Q(x) = x + 1$.
- $i=1, j=2$: $Q(2) - Q(1) = 3 - 2 = 1$, not divisible by 3. $2Q(2) - 1Q(1) = 6 - 2 = 4$, not divisible by 3. Product = 4, not divisible by 3. ✓

So degree 1 works for $p = 3$.

$p = 5$: $\mathbb{F}_5^* = \{1, 2, 3, 4\}$. We need $Q$ injective on this set and $xQ(x)$ injective.

Try $Q(x) = x + c$ for some constant $c$. Then $Q$ is injective (since $x$ is injective). And $xQ(x) = x(x+c) = x^2 + cx$. We need $x^2 + cx$ injective on $\{1,2,3,4\}$ mod 5.

$x^2 + cx = (x + c/2)^2 - c^2/4$. So this is a shifted square function. On $\mathbb{F}_5^*$, the squares are $\{1, 4, 4, 1\}$ for $x = 1,2,3,4$. So $x^2$ takes values $1, 4, 4, 1$ - not injective (1 and 4 each appear twice).

Adding $cx$ doesn't help because $x^2 + cx$ is still a quadratic. Let me compute for each $c$:
- $c=0$: $x^2$: values $1, 4, 4, 1$. Not injective.
- $c=1$: $x^2 + x$: $1+1=2, 4+2=6\equiv1, 4+3=7\equiv2, 1+4=5\equiv0$. Values: $2, 1, 2, 0$. Not injective (2 appears twice).
- $c=2$: $x^2 + 2x$: $1+2=3, 4+4=8\equiv3, 4+6=10\equiv0, 1+8=9\equiv4$. Values: $3, 3, 0, 4$. Not injective.
- $c=3$: $x^2 + 3x$: $1+3=4, 4+6=10\equiv0, 4+9=13\equiv3, 1+12=13\equiv3$. Values: $4, 0, 3, 3$. Not injective.
- $c=4$: $x^2 + 4x$: $1+4=5\equiv0, 4+8=12\equiv2, 4+12=16\equiv1, 1+16=17\equiv2$. Values: $0, 2, 1, 2$. Not injective.

So no linear polynomial works for $p = 5$.

Try degree 2. $Q(x) = ax^2 + bx + c$. We need $Q$ injective on $\{1,2,3,4\}$ mod 5 and $xQ(x)$ injective.

Let me try $Q(x) = x^2 + x + 1$.
Values on $\{1,2,3,4\}$: $1+1+1=3, 4+2+1=7\equiv2, 9+3+1=13\equiv3, 16+4+1=21\equiv1$. Values: $3, 2, 3, 1$. Not injective (3 twice).

Let me try $Q(x) = x^2 + 1$.
Values: $1+1=2, 4+1=5\equiv0, 9+1=10\equiv0, 16+1=17\equiv2$. Values: $2, 0, 0, 2$. Not injective.

Hmm, quadratics on $\mathbb{F}_5^*$... Since $|\mathbb{F}_5^*| = 4$ and a quadratic has at most... well, a quadratic can be injective on a set of 4 elements.

Let me try $Q(x) = x^2 + 2x$.
Values: $1+2=3, 4+4=8\equiv3, 9+6=15\equiv0, 16+8=24\equiv4$. Values: $3, 3, 0, 4$. Not injective.

$Q(x) = 2x^2 + x$:
Values: $2+1=3, 8+2=10\equiv0, 18+3=21\equiv1, 32+4=36\equiv1$. Values: $3, 0, 1, 1$. Not injective.

$Q(x) = x^2 + 3x + 1$:
Values: $1+3+1=5\equiv0, 4+6+1=11\equiv1, 9+9+1=19\equiv4, 16+12+1=29\equiv4$. Values: $0, 1, 4, 4$. Not injective.

$Q(x) = 2x^2 + 3x + 1$:
Values: $2+3+1=6\equiv1, 8+6+1=15\equiv0, 18+9+1=28\equiv3, 32+12+1=45\equiv0$. Values: $1, 0, 3, 0$. Not injective.

$Q(x) = x^2 + x + 2$:
Values: $1+1+2=4, 4+2+2=8\equiv3, 9+3+2=14\equiv4, 16+4+2=22\equiv2$. Values: $4, 3, 4, 2$. Not injective.

$Q(x) = 2x^2 + x + 1$:
Values: $2+1+1=4, 8+2+1=11\equiv1, 18+3+1=22\equiv2, 32+4+1=37\equiv2$. Values: $4, 1, 2, 2$. Not injective.

$Q(x) = 2x^2 + 2x + 1$:
Values: $2+2+1=5\equiv0, 8+4+1=13\equiv3, 18+6+1=25\equiv0, 32+8+1=41\equiv1$. Values: $0, 3, 0, 1$. Not injective.

$Q(x) = 3x^2 + x + 1$:
Values: $3+1+1=5\equiv0, 12+2+1=15\equiv0, 27+3+1=31\equiv1, 48+4+1=53\equiv3$. Values: $0, 0, 1, 3$. Not injective.

$Q(x) = x^2 + 4x + 2$:
Values: $1+4+2=7\equiv2, 4+8+2=14\equiv4, 9+12+2=23\equiv3, 16+16+2=34\equiv4$. Values: $2, 4, 3, 4$. Not injective.

$Q(x) = 2x^2 + 4x + 1$:
Values: $2+4+1=7\equiv2, 8+8+1=17\equiv2, 18+12+1=31\equiv1, 32+16+1=49\equiv4$. Values: $2, 2, 1, 4$. Not injective.

$Q(x) = 3x^2 + 2x + 1$:
Values: $3+2+1=6\equiv1, 12+4+1=17\equiv2, 27+6+1=34\equiv4, 48+8+1=57\equiv2$. Values: $1, 2, 4, 2$. Not injective.

$Q(x) = 3x^2 + 3x + 1$:
Values: $3+3+1=7\equiv2, 12+6+1=19\equiv4, 27+9+1=37\equiv2, 48+12+1=61\equiv1$. Values: $2, 4, 2, 1$. Not injective.

$Q(x) = 3x^2 + 4x + 1$:
Values: $3+4+1=8\equiv3, 12+8+1=21\equiv1, 27+12+1=40\equiv0, 48+16+1=65\equiv0$. Values: $3, 1, 0, 0$. Not injective.

$Q(x) = 4x^2 + x + 1$:
Values: $4+1+1=6\equiv1, 16+2+1=19\equiv4, 36+3+1=40\equiv0, 64+4+1=69\equiv4$. Values: $1, 4, 0, 4$. Not injective.

$Q(x) = 4x^2 + 2x + 1$:
Values: $4+2+1=7\equiv2, 16+4+1=21\equiv1, 36+6+1=43\equiv3, 64+8+1=73\equiv3$. Values: $2, 1, 3, 3$. Not injective.

$Q(x) = 4x^2 + 3x + 1$:
Values: $4+3+1=8\equiv3, 16+6+1=23\equiv3, 36+9+1=46\equiv1, 64+12+1=77\equiv2$. Values: $3, 3, 1, 2$. Not injective.

$Q(x) = 4x^2 + 4x + 1 = (2x+1)^2$:
Values: $9\equiv4, 25\equiv0, 49\equiv4, 81\equiv1$. Values: $4, 0, 4, 1$. Not injective.

Hmm, it seems like no quadratic works for $p=5$ either. Let me think about why.

Actually, wait. On $\mathbb{F}_5^* = \{1,2,3,4\}$, note that $x$ and $-x$ are both in the set (since $p > 2$, $-1 \neq 1$). Specifically, $1$ and $4 = -1$, $2$ and $3 = -2$.

For a quadratic $Q(x) = ax^2 + bx + c$, $Q(x) - Q(-x) = 2bx$. So $Q(x) = Q(-x)$ iff $2bx = 0$ iff $b = 0$ (since $x \neq 0$ and $p > 2$ so $2 \neq 0$). So if $b \neq 0$, then $Q(x) \neq Q(-x)$ for all $x \in \mathbb{F}_5^*$.

But we also need $xQ(x) \neq (-x)Q(-x)$, i.e., $xQ(x) + xQ(-x) \neq 0$, i.e., $x(Q(x) + Q(-x)) \neq 0$. Since $x \neq 0$, we need $Q(x) + Q(-x) \neq 0$, i.e., $2(ax^2 + c) \neq 0$, i.e., $ax^2 + c \neq 0$ for all $x \in \mathbb{F}_5^*$.

So for a quadratic to work on $p = 5$, we need:
1. $b \neq 0$ (so $Q(x) \neq Q(-x)$)
2. $ax^2 + c \neq 0$ for all $x \in \mathbb{F}_5^*$ (so $xQ(x) \neq (-x)Q(-x)$)
3. $Q$ is injective on $\{1, 2, 3, 4\}$ (not just that $Q(x) \neq Q(-x)$, but all pairs)
4. $xQ(x)$ is injective on $\{1, 2, 3, 4\}$

The pairs $(x, -x)$ in $\mathbb{F}_5^*$ are $(1,4)$ and $(2,3)$. Conditions 1 and 2 handle these pairs. But we also need to check cross-pairs: $Q(1) \neq Q(2)$, $Q(1) \neq Q(3)$, $Q(2) \neq Q(4)$, $Q(3) \neq Q(4)$, and similarly for $xQ(x)$.

This is getting complicated. Let me try to be more systematic for $p = 5$.

Actually, let me think about this more cleverly. For $p = 5$, $\mathbb{F}_5^* = \{1, 2, 3, 4\}$. We need $Q$ to be injective on this set (4 values, all distinct mod 5) and $xQ(x)$ to be injective (4 values, all distinct mod 5).

Since there are 5 elements in $\mathbb{F}_5$, an injective map from a 4-element set misses exactly one element.

Let me enumerate. $Q$ takes 4 distinct values in $\mathbb{F}_5$, missing one. Similarly $xQ(x)$ takes 4 distinct values, missing one.

Let me try to find a quadratic that works by being more systematic. Actually, let me just try all quadratics mod 5 systematically. A quadratic is $ax^2 + bx + c$ with $a \neq 0$. There are $4 \times 5 \times 5 = 100$ quadratics mod 5. That's a lot to check by hand.

Let me think about it differently. Let me try specific forms.

$Q(x) = x^2 + 2x + 3$:
Values: $1+2+3=6\equiv1, 4+4+3=11\equiv1, 9+6+3=18\equiv3, 16+8+3=27\equiv2$. Values: $1, 1, 3, 2$. Not injective.

$Q(x) = x^2 + 2$:
Values: $1+2=3, 4+2=6\equiv1, 9+2=11\equiv1, 16+2=18\equiv3$. Values: $3, 1, 1, 3$. Not injective.

Hmm, the issue with quadratics on $\mathbb{F}_5^*$ is that $x^2$ takes only 2 values on $\mathbb{F}_5^*$ (the quadratic residues), so $ax^2$ also takes only 2 values. Adding $bx + c$ can help, but...

Actually, let me reconsider. On $\mathbb{F}_5^*$, $x^2$ takes values $\{1, 4\}$ (for $x = 1, 4$ and $x = 2, 3$). So $ax^2 + bx + c$ takes values:
- For $x = 1$: $a + b + c$
- For $x = 2$: $4a + 2b + c$
- For $x = 3$: $4a + 3b + c$  (since $3^2 = 9 \equiv 4$)
- For $x = 4$: $a + 4b + c$  (since $4^2 = 16 \equiv 1$)

For injectivity: $a+b+c, 4a+2b+c, 4a+3b+c, a+4b+c$ all distinct mod 5.

Differences:
- $Q(2) - Q(1) = 3a + b$
- $Q(3) - Q(1) = 3a + 2b$
- $Q(4) - Q(1) = 3b$
- $Q(3) - Q(2) = b$
- $Q(4) - Q(2) = -3a + 2b = 2a + 2b$
- $Q(4) - Q(3) = -3a + b = 2a + b$

For all these to be nonzero mod 5:
- $3a + b \neq 0$
- $3a + 2b \neq 0$
- $3b \neq 0$, i.e., $b \neq 0$
- $b \neq 0$ (same)
- $2a + 2b \neq 0$, i.e., $a + b \neq 0$
- $2a + b \neq 0$

So conditions for $Q$ injective: $b \neq 0$, $3a + b \neq 0$, $3a + 2b \neq 0$, $a + b \neq 0$, $2a + b \neq 0$.

Now for $xQ(x)$ injective. $xQ(x) = x(ax^2 + bx + c) = ax^3 + bx^2 + cx$.

Values on $\{1, 2, 3, 4\}$:
- $x=1$: $a + b + c$
- $x=2$: $8a + 4b + 2c = 3a + 4b + 2c$
- $x=3$: $27a + 9b + 3c = 2a + 4b + 3c$
- $x=4$: $64a + 16b + 4c = 4a + b + 4c$

Differences:
- $g(2) - g(1) = 2a + 3b + c$
- $g(3) - g(1) = a + 3b + 2c$
- $g(4) - g(1) = 3a + 3c$
- $g(3) - g(2) = -a + c = 4a + c$
- $g(4) - g(2) = a - 3b + 2c = a + 2b + 2c$
- $g(4) - g(3) = 2a - 3b + c = 2a + 2b + c$

For all nonzero mod 5:
- $2a + 3b + c \neq 0$
- $a + 3b + 2c \neq 0$
- $3a + 3c \neq 0$, i.e., $a + c \neq 0$
- $4a + c \neq 0$
- $a + 2b + 2c \neq 0$
- $2a + 2b + c \neq 0$

So we need to find $a, b, c \in \mathbb{F}_5$ with $a \neq 0$ satisfying all these conditions.

Let me try $a = 1, b = 1$:
- $Q$ conditions: $b = 1 \neq 0$ ✓, $3 + 1 = 4 \neq 0$ ✓, $3 + 2 = 5 \equiv 0$ ✗. Fails.

$a = 1, b = 2$:
- $Q$: $b = 2 \neq 0$ ✓, $3 + 2 = 5 \equiv 0$ ✗. Fails.

$a = 1, b = 3$:
- $Q$: $b = 3 \neq 0$ ✓, $3 + 3 = 6 \equiv 1 \neq 0$ ✓, $3 + 6 = 9 \equiv 4 \neq 0$ ✓, $1 + 3 = 4 \neq 0$ ✓, $2 + 3 = 5 \equiv 0$ ✗. Fails.

$a = 1, b = 4$:
- $Q$: $b = 4 \neq 0$ ✓, $3 + 4 = 7 \equiv 2 \neq 0$ ✓, $3 + 8 = 11 \equiv 1 \neq 0$ ✓, $1 + 4 = 5 \equiv 0$ ✗. Fails.

$a = 2, b = 1$:
- $Q$: $b = 1 \neq 0$ ✓, $6 + 1 = 7 \equiv 2 \neq 0$ ✓, $6 + 2 = 8 \equiv 3 \neq 0$ ✓, $2 + 1 = 3 \neq 0$ ✓, $4 + 1 = 5 \equiv 0$ ✗. Fails.

$a = 2, b = 2$:
- $Q$: $b = 2 \neq 0$ ✓, $6 + 2 = 8 \equiv 3 \neq 0$ ✓, $6 + 4 = 10 \equiv 0$ ✗. Fails.

$a = 2, b = 3$:
- $Q$: $b = 3 \neq 0$ ✓, $6 + 3 = 9 \equiv 4 \neq 0$ ✓, $6 + 6 = 12 \equiv 2 \neq 0$ ✓, $2 + 3 = 5 \equiv 0$ ✗. Fails.

$a = 2, b = 4$:
- $Q$: $b = 4 \neq 0$ ✓, $6 + 4 = 10 \equiv 0$ ✗. Fails.

$a = 3, b = 1$:
- $Q$: $b = 1 \neq 0$ ✓, $9 + 1 = 10 \equiv 0$ ✗. Fails.

$a = 3, b = 2$:
- $Q$: $b = 2 \neq 0$ ✓, $9 + 2 = 11 \equiv 1 \neq 0$ ✓, $9 + 4 = 13 \equiv 3 \neq 0$ ✓, $3 + 2 = 5 \equiv 0$ ✗. Fails.

$a = 3, b = 3$:
- $Q$: $b = 3 \neq 0$ ✓, $9 + 3 = 12 \equiv 2 \neq 0$ ✓, $9 + 6 = 15 \equiv 0$ ✗. Fails.

$a = 3, b = 4$:
- $Q$: $b = 4 \neq 0$ ✓, $9 + 4 = 13 \equiv 3 \neq 0$ ✓, $9 + 8 = 17 \equiv 2 \neq 0$ ✓, $3 + 4 = 7 \equiv 2 \neq 0$ ✓, $6 + 4 = 10 \equiv 0$ ✗. Fails.

$a = 4, b = 1$:
- $Q$: $b = 1 \neq 0$ ✓, $12 + 1 = 13 \equiv 3 \neq 0$ ✓, $12 + 2 = 14 \equiv 4 \neq 0$ ✓, $4 + 1 = 5 \equiv 0$ ✗. Fails.

$a = 4, b = 2$:
- $Q$: $b = 2 \neq 0$ ✓, $12 + 2 = 14 \equiv 4 \neq 0$ ✓, $12 + 4 = 16 \equiv 1 \neq 0$ ✓, $4 + 2 = 6 \equiv 1 \neq 0$ ✓, $8 + 2 = 10 \equiv 0$ ✗. Fails.

$a = 4, b = 3$:
- $Q$: $b = 3 \neq 0$ ✓, $12 + 3 = 15 \equiv 0$ ✗. Fails.

$a = 4, b = 4$:
- $Q$: $b = 4 \neq 0$ ✓, $12 + 4 = 16 \equiv 1 \neq 0$ ✓, $12 + 8 = 20 \equiv 0$ ✗. Fails.

So NO quadratic works for $p = 5$! Every quadratic fails the injectivity of $Q$ itself on $\mathbb{F}_5^*$.

Wait, that's surprising. Let me double-check. The conditions for $Q$ injective were:
- $b \neq 0$
- $3a + b \neq 0$
- $3a + 2b \neq 0$
- $a + b \neq 0$
- $2a + b \neq 0$

With $a \neq 0$, we need $b \notin \{0, -3a, -3a/2 \cdot 2, -a, -2a\} = \{0, -3a, -3a \cdot 3, -a, -2a\}$.

Wait, let me redo. $3a + 2b \neq 0$ means $b \neq -3a/2 = -3a \cdot 3 = -9a = a$ (since $-9 \equiv 1 \pmod{5}$). So $b \neq a$.

So the forbidden values of $b$ (given $a$) are: $0, -3a, a, -a, -2a$.

With $a = 1$: forbidden $b$ values are $0, 2, 1, 4, 3$. That's all of $\{0, 1, 2, 3, 4\}$! So no $b$ works.

With $a = 2$: forbidden $b$ values are $0, -6 \equiv 4, 2, -2 \equiv 3, -4 \equiv 1$. That's $\{0, 1, 2, 3, 4\}$. All forbidden.

So indeed, for $p = 5$, no quadratic polynomial is injective on $\mathbb{F}_5^*$. This makes sense because $\mathbb{F}_5^*$ has 4 elements, and a quadratic $ax^2 + bx + c$ is determined by 3 parameters, so it's a 3-dimensional family, but the injectivity condition is quite restrictive.

Actually, let me think about why. The issue is that $x^2$ on $\mathbb{F}_5^*$ takes only 2 values (1 and 4), so $ax^2$ takes only 2 values. Then $ax^2 + bx + c$ is like adding a linear function to a 2-valued function. The linear part $bx + c$ takes 4 distinct values (if $b \neq 0$), but the quadratic part "collides" some of them.

Specifically, $Q(1) - Q(4) = (a + b + c) - (a + 4b + c) = -3b = 2b$, and $Q(2) - Q(3) = (4a + 2b + c) - (4a + 3b + c) = -b = 4b$. These are both nonzero if $b \neq 0$, so the "paired" elements (1,4) and (2,3) are fine. But the cross-pairs cause issues.

$Q(1) - Q(2) = -3a - b = 2a + 4b$, $Q(1) - Q(3) = -3a - 2b = 2a + 3b$, $Q(2) - Q(4) = 3a - 2b = 3a + 3b$, $Q(3) - Q(4) = 3a - b = 3a + 4b$.

For all nonzero: $2a + 4b \neq 0$, $2a + 3b \neq 0$, $3a + 3b \neq 0$, $3a + 4b \neq 0$.

Combined with $b \neq 0$ and $2b \neq 0$ (same) and $4b \neq 0$ (same):
- $b \neq 0$
- $2a + 4b \neq 0 \Rightarrow a + 2b \neq 0$
- $2a + 3b \neq 0$
- $3a + 3b \neq 0 \Rightarrow a + b \neq 0$
- $3a + 4b \neq 0$

So forbidden $b$ values (given $a \neq 0$): $0, -a/2 = -a \cdot 3 = 2a, -2a/3 = -2a \cdot 2 = a, -a, -3a/4 = -3a \cdot 4 = -12a = 3a$.

So forbidden: $\{0, 2a, a, -a = 4a, 3a\} = \{0, a, 2a, 3a, 4a\}$. All 5 values are forbidden! So indeed no quadratic is injective on $\mathbb{F}_5^*$.

This is because $\mathbb{F}_5^*$ has 4 elements, and a quadratic has 3 parameters. The "collision" structure is too rich.

OK so for $p = 5$, we need degree $\geq 3$. Let me check if degree 3 works.

$Q(x) = x^3$. On $\mathbb{F}_5^*$: $1, 8 \equiv 3, 27 \equiv 2, 64 \equiv 4$. Values: $1, 3, 2, 4$. All distinct! ✓

$xQ(x) = x^4$. On $\mathbb{F}_5^*$: $1, 16 \equiv 1, 81 \equiv 1, 256 \equiv 1$. All equal to 1. Not injective. ✗

$Q(x) = x^3 + x$:
Values: $1+1=2, 8+2=10\equiv0, 27+3=30\equiv0, 64+4=68\equiv3$. Values: $2, 0, 0, 3$. Not injective.

$Q(x) = x^3 + 1$:
Values: $1+1=2, 8+1=9\equiv4, 27+1=28\equiv3, 64+1=65\equiv0$. Values: $2, 4, 3, 0$. All distinct! ✓

$xQ(x) = x^4 + x$:
Values: $1+1=2, 16+2=18\equiv3, 81+3=84\equiv4, 256+4=260\equiv0$. Values: $2, 3, 4, 0$. All distinct! ✓

So $Q(x) = x^3 + 1$ works for $p = 5$! Degree 3.

Let me verify: $i, j \in \{1, 2, 3, 4\}$, $i < j$.
- $Q$ values: $Q(1)=2, Q(2)=4, Q(3)=3, Q(4)=0$. All distinct mod 5. ✓
- $xQ(x)$ values: $1 \cdot 2 = 2, 2 \cdot 4 = 8 \equiv 3, 3 \cdot 3 = 9 \equiv 4, 4 \cdot 0 = 0$. All distinct mod 5. ✓

So for $p = 5$, the answer is 3.

Now let me check $p = 3$ again. We found degree 1 works. Let me also check: is the answer supposed to be in terms of $p$? The problem says "What is the smallest possible degree of $Q$?" - it should be a function of $p$ or a universal answer.

Wait, re-reading the problem: "Prime $p > 2$ and a polynomial $Q$... What is the smallest possible degree of $Q$?"

I think the answer should be in terms of $p$. Let me gather more data.

$p = 3$: degree 1 works (e.g., $Q(x) = x + 1$).
$p = 5$: degree 3 works (e.g., $Q(x) = x^3 + 1$). Degree 2 doesn't work.

Let me check $p = 7$.

For $p = 7$, $\mathbb{F}_7^* = \{1, 2, 3, 4, 5, 6\}$, which has 6 elements.

First, can degree 1 work? $Q(x) = ax + b$ with $a \neq 0$. Then $Q$ is injective (obviously). $xQ(x) = ax^2 + bx$. We need $ax^2 + bx$ injective on $\{1, ..., 6\}$ mod 7.

$ax^2 + bx = a(x^2 + (b/a)x) = a(x + b/(2a))^2 - b^2/(4a)$. So $xQ(x) = a(x + b/(2a))^2 + \text{const}$. The square function on $\mathbb{F}_7^*$ takes values $\{1, 4, 2, 2, 4, 1\}$ for $x = 1, ..., 6$ (i.e., $x^2$ for $x = 1, 2, 3, 4, 5, 6$ mod 7: $1, 4, 2, 2, 4, 1$). So $(x + c)^2$ also takes only 3 values (the quadratic residues), each twice. So $ax^2 + bx$ takes at most 3 distinct values on $\mathbb{F}_7^*$, which is less than 6. Not injective.

So degree 1 doesn't work for $p = 7$.

Can degree 2 work? $Q(x) = ax^2 + bx + c$. We need $Q$ injective on $\{1, ..., 6\}$ and $xQ(x)$ injective.

$Q$ injective: $Q$ has 3 parameters, needs to separate 6 points. The differences $Q(i) - Q(j) = (i-j)(a(i+j) + b)$. For $Q(i) \neq Q(j)$, we need $a(i+j) + b \neq 0$ for all $i \neq j$ in $\mathbb{F}_7^*$.

The values of $i + j$ for $i \neq j$ in $\mathbb{F}_7^*$: We need $i + j$ to range over... well, $i, j \in \{1, 2, 3, 4, 5, 6\}$, $i \neq j$. The possible sums $i + j$ mod 7: since $i$ and $j$ are distinct nonzero elements, $i + j$ can be any element of $\mathbb{F}_7$ except... let me think. $i + j = 0$ is possible (e.g., $i = 1, j = 6$). $i + j$ can be any value in $\mathbb{F}_7$ actually. For instance:
- $i + j = 0$: $(1, 6), (2, 5), (3, 4)$
- $i + j = 1$: impossible since $i, j \geq 1$ and $i \neq j$... wait, mod 7. $i = 3, j = 5$: $3 + 5 = 8 \equiv 1$. Yes.
- Actually, $i + j$ can be anything in $\mathbb{F}_7$.

So we need $a \cdot s + b \neq 0$ for all $s$ that appears as $i + j$ with $i \neq j \in \mathbb{F}_7^*$. Since $s$ can be any element of $\mathbb{F}_7$ (let me verify: $s = 0$: yes; $s = 1$: $3 + 5$; $s = 2$: $1 + 1$... no, $i \neq j$. $s = 2$: $3 + 6 = 9 \equiv 2$; $s = 3$: $1 + 2$; $s = 4$: $1 + 3$; $s = 5$: $2 + 3$; $s = 6$: $1 + 5$). So $s$ ranges over all of $\mathbb{F}_7$.

Therefore $a \cdot s + b \neq 0$ for all $s \in \mathbb{F}_7$ is impossible (since $s = -b/a$ makes it 0). So no quadratic is injective on $\mathbb{F}_7^*$!

Wait, that's a strong result. For $p = 7$, $Q(i) - Q(j) = (i - j)(a(i+j) + b)$. Since $i \neq j$, $i - j \neq 0$. So $Q(i) = Q(j)$ iff $a(i+j) + b = 0$, i.e., $i + j = -b/a$. Since $i + j$ can be any element of $\mathbb{F}_7$ (as shown above), there always exist $i \neq j$ with $i + j = -b/a$, so $Q$ is never injective on $\mathbb{F}_7^*$ for a quadratic.

Hmm wait, but I need to be more careful. We need $i + j = -b/a$ with $i, j \in \mathbb{F}_7^*$ and $i \neq j$. Given any target sum $s \in \mathbb{F}_7$, can we find $i \neq j \in \mathbb{F}_7^*$ with $i + j = s$?

- $s = 0$: $i = 1, j = 6$. ✓
- $s = 1$: $i = 3, j = 5$ (since $3 + 5 = 8 \equiv 1$). ✓
- $s = 2$: $i = 3, j = 6$ (since $3 + 6 = 9 \equiv 2$). ✓
- $s = 3$: $i = 1, j = 2$. ✓
- $s = 4$: $i = 1, j = 3$. ✓
- $s = 5$: $i = 2, j = 3$. ✓
- $s = 6$: $i = 1, j = 5$. ✓

Yes, for every $s \in \mathbb{F}_7$, there exist $i \neq j \in \mathbb{F}_7^*$ with $i + j = s$. So no quadratic is injective on $\mathbb{F}_7^*$.

More generally, for $p \geq 7$, the same argument shows that no quadratic is injective on $\mathbb{F}_p^*$, because for any $s \in \mathbb{F}_p$, we can find $i \neq j \in \mathbb{F}_p^*$ with $i + j = s$ (as long as $p - 1 \geq 4$, i.e., $p \geq 5$, there are enough elements).

Wait, for $p = 5$, we also showed no quadratic works. And the argument here would be: for any $s \in \mathbb{F}_5$, can we find $i \neq j \in \mathbb{F}_5^*$ with $i + j = s$?
- $s = 0$: $1 + 4$. ✓
- $s = 1$: $2 + 4 = 6 \equiv 1$. ✓
- $s = 2$: $1 + 1$... no, $i \neq j$. $3 + 4 = 7 \equiv 2$. ✓
- $s = 3$: $1 + 2$. ✓
- $s = 4$: $1 + 3$. ✓

Yes, so for $p = 5$ too, no quadratic is injective on $\mathbb{F}_5^*$.

For $p = 3$: $\mathbb{F}_3^* = \{1, 2\}$. For a quadratic $Q(x) = ax^2 + bx + c$, $Q(1) - Q(2) = a(1-2)(1+2) + b(1-2) = -a \cdot 3 + b \cdot (-1) = -3a - b \equiv -b \pmod{3}$. So $Q(1) = Q(2)$ iff $b = 0$. So a quadratic with $b \neq 0$ is injective on $\mathbb{F}_3^*$. But we showed degree 1 already works for $p = 3$.

OK so let me think about the general pattern. For degree $d$ polynomial $Q$, $Q(i) - Q(j) = (i - j) \cdot R(i, j)$ where $R$ is a polynomial in $i, j$. For $Q$ to be injective on $\mathbb{F}_p^*$, we need $R(i, j) \neq 0$ for all $i \neq j \in \mathbb{F}_p^*$.

More precisely, if $Q(x) = \sum_{k=0}^{d} a_k x^k$, then $Q(i) - Q(j) = \sum_{k=1}^{d} a_k (i^k - j^k) = (i - j) \sum_{k=1}^{d} a_k \sum_{l=0}^{k-1} i^l j^{k-1-l}$.

So $Q(i) - Q(j) = (i-j) \cdot S(i,j)$ where $S(i,j) = \sum_{k=1}^{d} a_k \frac{i^k - j^k}{i - j}$.

For injectivity, we need $S(i, j) \neq 0$ for all $i \neq j \in \mathbb{F}_p^*$.

Similarly, $xQ(x) = \sum_{k=0}^{d} a_k x^{k+1}$, and $(iQ(i) - jQ(j)) = (i-j) \cdot T(i,j)$ where $T(i,j) = \sum_{k=0}^{d} a_k \frac{i^{k+1} - j^{k+1}}{i - j}$.

For the second injectivity, $T(i,j) \neq 0$ for all $i \neq j \in \mathbb{F}_p^*$.

Now, $S(i,j)$ is a symmetric polynomial in $i, j$ of degree $d - 1$ in each variable. $T(i,j)$ is a symmetric polynomial of degree $d$ in each variable.

Let me think about this in terms of the "sum" $s = i + j$ and "product" $p_{ij} = ij$. Since $S$ and $T$ are symmetric, they can be expressed as polynomials in $s$ and $p_{ij}$.

Actually, let me think about it differently. Let $u = i + j$ and $v = ij$. Then $i$ and $j$ are roots of $t^2 - ut + v = 0$. The condition $i, j \in \mathbb{F}_p^*$ and $i \neq j$ means $u^2 - 4v \neq 0$ (discriminant nonzero), $v \neq 0$ (both nonzero), and $i, j \in \mathbb{F}_p$ (which is automatic if the discriminant is a square... well, in $\mathbb{F}_p$, $i$ and $j$ exist iff $u^2 - 4v$ is a square, but we're working over $\mathbb{F}_p$ so it's fine as long as the quadratic splits).

Hmm, this is getting complicated. Let me think about the problem from a higher level.

The key insight might be related to the following: we need both $Q$ and $x \mapsto xQ(x)$ to be injective (hence "almost permutations") on $\mathbb{F}_p^*$.

Let me think about what happens with $Q(x) = x^d + c$ for appropriate $d$.

$Q$ injective on $\mathbb{F}_p^*$: $x^d$ injective on $\mathbb{F}_p^*$ iff $\gcd(d, p-1) = 1$.
$xQ(x) = x^{d+1} + cx$ injective on $\mathbb{F}_p^*$: need $x^{d+1} + cx$ injective.

For $Q(x) = x^d + c$, $Q$ is injective iff $\gcd(d, p-1) = 1$ (the constant doesn't affect injectivity).

For $xQ(x) = x^{d+1} + cx$, this is injective on $\mathbb{F}_p^*$ iff... this is harder to analyze in general.

For $p = 5$, $d = 3$: $\gcd(3, 4) = 1$ ✓. $xQ(x) = x^4 + cx$. $x^4 = 1$ on $\mathbb{F}_5^*$, so $x^4 + cx = 1 + cx$, which is injective iff $c \neq 0$. With $c = 1$, it works. ✓

For $p = 7$, let me try $d = 3$: $\gcd(3, 6) = 3 \neq 1$. So $x^3$ is not injective on $\mathbb{F}_7^*$. 

$d = 5$: $\gcd(5, 6) = 1$ ✓. $Q(x) = x^5 + c$. $xQ(x) = x^6 + cx = 1 + cx$ on $\mathbb{F}_7^*$ (since $x^6 = 1$). This is injective iff $c \neq 0$. So $Q(x) = x^5 + 1$ should work for $p = 7$.

Let me verify: $Q(x) = x^5 + 1$ on $\mathbb{F}_7^* = \{1, 2, 3, 4, 5, 6\}$:
- $Q(1) = 2, Q(2) = 32 + 1 = 33 \equiv 5, Q(3) = 243 + 1 = 244 \equiv 244 - 34 \cdot 7 = 244 - 238 = 6, Q(4) = 1024 + 1 = 1025 \equiv 1025 - 146 \cdot 7 = 1025 - 1022 = 3, Q(5) = 3125 + 1 = 3126 \equiv 3126 - 446 \cdot 7 = 3126 - 3122 = 4, Q(6) = 7776 + 1 = 7777 \equiv 7777 - 1111 \cdot 7 = 7777 - 7777 = 0$.

Values: $2, 5, 6, 3, 4, 0$. All distinct! ✓

$xQ(x) = x^6 + x = 1 + x$ on $\mathbb{F}_7^*$: values $2, 3, 4, 5, 6, 0$. All distinct! ✓

So $Q(x) = x^5 + 1$ works for $p = 7$, degree 5.

But can we do better? Can degree 3 or 4 work for $p = 7$?

Let me think about degree 3 for $p = 7$. We need $Q(x) = ax^3 + bx^2 + cx + d$ injective on $\mathbb{F}_7^*$ and $xQ(x) = ax^4 + bx^3 + cx^2 + dx$ injective on $\mathbb{F}_7^*$.

This is a 4-parameter family (with $a \neq 0$), and we need to separate 6 points in two different ways. Let me think about whether this is possible.

Actually, let me think about the problem more generally. Let me consider the approach of using $Q(x) = x^{p-2} + c$.

$x^{p-2} = x^{-1}$ on $\mathbb{F}_p^*$ (by Fermat's little theorem). So $Q(x) = x^{-1} + c$, which is injective on $\mathbb{F}_p^*$ (since $x^{-1}$ is a bijection on $\mathbb{F}_p^*$). And $xQ(x) = 1 + cx$, which is injective iff $c \neq 0$.

So $Q(x) = x^{p-2} + 1$ always works, with degree $p - 2$.

But we found better:
- $p = 3$: degree 1 (which is $p - 2 = 1$). ✓
- $p = 5$: degree 3 (which is $p - 2 = 3$). ✓
- $p = 7$: degree 5 (which is $p - 2 = 5$). ✓

Hmm, so far the answer seems to be $p - 2$. But wait, for $p = 5$, I showed degree 2 doesn't work, and degree 3 does. For $p = 7$, I showed degree 1 and 2 don't work. Let me check if degree 3 or 4 works for $p = 7$.

Actually, let me think about this more carefully. The pattern $Q(x) = x^{p-2} + 1 = x^{-1} + 1$ gives degree $p - 2$. But maybe we can do better with a different polynomial.

Let me think about $p = 7$ and degree 3.

$Q(x) = ax^3 + bx^2 + cx + d$, $a \neq 0$.

$Q(i) - Q(j) = (i-j)[a(i^2 + ij + j^2) + b(i+j) + c]$.

For injectivity, need $a(i^2 + ij + j^2) + b(i+j) + c \neq 0$ for all $i \neq j \in \mathbb{F}_7^*$.

Let $s = i + j, p_{ij} = ij$. Then $i^2 + ij + j^2 = (i+j)^2 - ij = s^2 - p_{ij}$.

So the condition is $a(s^2 - p_{ij}) + bs + c \neq 0$, i.e., $as^2 + bs + c \neq ap_{ij}$, for all valid $(s, p_{ij})$ pairs.

Now, for $i, j \in \mathbb{F}_7^*$, $i \neq j$, what are the possible $(s, p_{ij})$ pairs? $s = i + j$ and $p_{ij} = ij$. Given $s$ and $p_{ij}$, $i$ and $j$ are roots of $t^2 - st + p_{ij} = 0$, which has roots in $\mathbb{F}_7$ iff $s^2 - 4p_{ij}$ is a square (or zero) in $\mathbb{F}_7$. We need $i \neq j$ so $s^2 - 4p_{ij} \neq 0$, and $i, j \neq 0$ so $p_{ij} \neq 0$.

This is getting complicated. Let me just try to find a degree 3 polynomial that works for $p = 7$ by trial.

Let me try $Q(x) = x^3 + x + 1$:
Values on $\{1, 2, 3, 4, 5, 6\}$ mod 7:
- $1 + 1 + 1 = 3$
- $8 + 2 + 1 = 11 \equiv 4$
- $27 + 3 + 1 = 31 \equiv 3$
- $64 + 4 + 1 = 69 \equiv 69 - 9 \cdot 7 = 69 - 63 = 6$
- $125 + 5 + 1 = 131 \equiv 131 - 18 \cdot 7 = 131 - 126 = 5$
- $216 + 6 + 1 = 223 \equiv 223 - 31 \cdot 7 = 223 - 217 = 6$

Values: $3, 4, 3, 6, 5, 6$. Not injective (3 and 6 repeated).

$Q(x) = x^3 + 2x + 1$:
- $1 + 2 + 1 = 4$
- $8 + 4 + 1 = 13 \equiv 6$
- $27 + 6 + 1 = 34 \equiv 34 - 4 \cdot 7 = 6$
- $64 + 8 + 1 = 73 \equiv 73 - 10 \cdot 7 = 3$
- $125 + 10 + 1 = 136 \equiv 136 - 19 \cdot 7 = 136 - 133 = 3$
- $216 + 12 + 1 = 229 \equiv 229 - 32 \cdot 7 = 229 - 224 = 5$

Values: $4, 6, 6, 3, 3, 5$. Not injective.

$Q(x) = x^3 + 3x + 1$:
- $1 + 3 + 1 = 5$
- $8 + 6 + 1 = 15 \equiv 1$
- $27 + 9 + 1 = 37 \equiv 37 - 5 \cdot 7 = 2$
- $64 + 12 + 1 = 77 \equiv 0$
- $125 + 15 + 1 = 141 \equiv 141 - 20 \cdot 7 = 1$
- $216 + 18 + 1 = 235 \equiv 235 - 33 \cdot 7 = 235 - 231 = 4$

Values: $5, 1, 2, 0, 1, 4$. Not injective (1 repeated).

$Q(x) = x^3 + x^2 + 1$:
- $1 + 1 + 1 = 3$
- $8 + 4 + 1 = 13 \equiv 6$
- $27 + 9 + 1 = 37 \equiv 2$
- $64 + 16 + 1 = 81 \equiv 81 - 11 \cdot 7 = 4$
- $125 + 25 + 1 = 151 \equiv 151 - 21 \cdot 7 = 4$
- $216 + 36 + 1 = 253 \equiv 253 - 36 \cdot 7 = 1$

Values: $3, 6, 2, 4, 4, 1$. Not injective (4 repeated).

$Q(x) = x^3 + x^2 + x + 1 = (x+1)(x^2+1)$:
- $1 + 1 + 1 + 1 = 4$
- $8 + 4 + 2 + 1 = 15 \equiv 1$
- $27 + 9 + 3 + 1 = 40 \equiv 5$
- $64 + 16 + 4 + 1 = 85 \equiv 85 - 12 \cdot 7 = 1$
- $125 + 25 + 5 + 1 = 156 \equiv 156 - 22 \cdot 7 = 2$
- $216 + 36 + 6 + 1 = 259 \equiv 259 - 37 \cdot 7 = 0$

Values: $4, 1, 5, 1, 2, 0$. Not injective.

$Q(x) = 2x^3 + x + 1$:
- $2 + 1 + 1 = 4$
- $16 + 2 + 1 = 19 \equiv 5$
- $54 + 3 + 1 = 58 \equiv 58 - 8 \cdot 7 = 2$
- $128 + 4 + 1 = 133 \equiv 0$
- $250 + 5 + 1 = 256 \equiv 256 - 36 \cdot 7 = 4$
- $432 + 6 + 1 = 439 \equiv 439 - 62 \cdot 7 = 439 - 434 = 5$

Values: $4, 5, 2, 0, 4, 5$. Not injective.

$Q(x) = 2x^3 + x^2 + 1$:
- $2 + 1 + 1 = 4$
- $16 + 4 + 1 = 21 \equiv 0$
- $54 + 9 + 1 = 64 \equiv 1$
- $128 + 16 + 1 = 145 \equiv 145 - 20 \cdot 7 = 5$
- $250 + 25 + 1 = 276 \equiv 276 - 39 \cdot 7 = 3$
- $432 + 36 + 1 = 469 \equiv 469 - 67 \cdot 7 = 0$

Values: $4, 0, 1, 5, 3, 0$. Not injective.

$Q(x) = 2x^3 + 2x^2 + x + 1$:
- $2 + 2 + 1 + 1 = 6$
- $16 + 8 + 2 + 1 = 27 \equiv 6$
Not injective already.

$Q(x) = 3x^3 + x + 1$:
- $3 + 1 + 1 = 5$
- $24 + 2 + 1 = 27 \equiv 6$
- $81 + 3 + 1 = 85 \equiv 1$
- $192 + 4 + 1 = 197 \equiv 197 - 28 \cdot 7 = 1$
Not injective.

$Q(x) = 3x^3 + 2x + 1$:
- $3 + 2 + 1 = 6$
- $24 + 4 + 1 = 29 \equiv 1$
- $81 + 6 + 1 = 88 \equiv 88 - 12 \cdot 7 = 4$
- $192 + 8 + 1 = 201 \equiv 201 - 28 \cdot 7 = 5$
- $375 + 10 + 1 = 386 \equiv 386 - 55 \cdot 7 = 1$
Not injective.

$Q(x) = 3x^3 + x^2 + x + 1$:
- $3 + 1 + 1 + 1 = 6$
- $24 + 4 + 2 + 1 = 31 \equiv 3$
- $81 + 9 + 3 + 1 = 94 \equiv 94 - 13 \cdot 7 = 3$
Not injective.

$Q(x) = x^3 + 2x^2 + 3x + 1$:
- $1 + 2 + 3 + 1 = 7 \equiv 0$
- $8 + 8 + 6 + 1 = 23 \equiv 2$
- $27 + 18 + 9 + 1 = 55 \equiv 55 - 7 \cdot 7 = 6$
- $64 + 32 + 12 + 1 = 109 \equiv 109 - 15 \cdot 7 = 4$
- $125 + 50 + 15 + 1 = 191 \equiv 191 - 27 \cdot 7 = 2$
Not injective.

$Q(x) = x^3 + 3x^2 + 2x + 1$:
- $1 + 3 + 2 + 1 = 7 \equiv 0$
- $8 + 12 + 4 + 1 = 25 \equiv 4$
- $27 + 27 + 6 + 1 = 61 \equiv 61 - 8 \cdot 7 = 5$
- $64 + 48 + 8 + 1 = 121 \equiv 121 - 17 \cdot 7 = 2$
- $125 + 75 + 10 + 1 = 211 \equiv 211 - 30 \cdot 7 = 1$
- $216 + 108 + 12 + 1 = 337 \equiv 337 - 48 \cdot 7 = 1$
Not injective.

$Q(x) = 2x^3 + 3x^2 + x + 1$:
- $2 + 3 + 1 + 1 = 7 \equiv 0$
- $16 + 12 + 2 + 1 = 31 \equiv 3$
- $54 + 27 + 3 + 1 = 85 \equiv 1$
- $128 + 48 + 4 + 1 = 181 \equiv 181 - 25 \cdot 7 = 6$
- $250 + 75 + 5 + 1 = 331 \equiv 331 - 47 \cdot 7 = 2$
- $432 + 108 + 6 + 1 = 547 \equiv 547 - 78 \cdot 7 = 1$
Not injective.

$Q(x) = 2x^3 + x^2 + 2x + 1$:
- $2 + 1 + 2 + 1 = 6$
- $16 + 4 + 4 + 1 = 25 \equiv 4$
- $54 + 9 + 6 + 1 = 70 \equiv 0$
- $128 + 16 + 8 + 1 = 153 \equiv 153 - 21 \cdot 7 = 6$
Not injective.

Hmm, I'm having trouble finding a degree 3 polynomial that's even injective on $\mathbb{F}_7^*$, let alone satisfying both conditions. Let me think about why.

For a cubic $Q(x) = ax^3 + bx^2 + cx + d$, $Q(i) - Q(j) = (i-j)[a(i^2+ij+j^2) + b(i+j) + c]$.

Let $s = i+j, q = ij$ (using $q$ for product to avoid confusion with prime $p$). Then $i^2 + ij + j^2 = s^2 - q$. So the condition is $a(s^2 - q) + bs + c \neq 0$ for all valid $(s, q)$.

Now, for $i, j \in \mathbb{F}_7^*$, $i \neq j$, what values can $(s, q)$ take?

$s = i + j$ can be any element of $\mathbb{F}_7$ (as we showed). For a given $s$, $q = ij$ ranges over... well, $i$ and $j$ are roots of $t^2 - st + q = 0$, so $q = i(s - i)$ for $i \in \mathbb{F}_7^*$, $i \neq s/2$ (to ensure $i \neq j$), and $s - i \neq 0$ (to ensure $j \neq 0$), i.e., $i \neq s$.

So for a given $s$, $q$ ranges over $\{i(s-i) : i \in \mathbb{F}_7^*, i \neq s, i \neq s/2\}$ (when $s \neq 0$) or $\{i(-i) : i \in \mathbb{F}_7^*, i \neq 0\} = \{-i^2 : i \in \mathbb{F}_7^*\}$ (when $s = 0$).

For $s = 0$: $q = -i^2$ for $i \in \{1, 2, 3, 4, 5, 6\}$. $i^2$ mod 7: $1, 4, 2, 2, 4, 1$. So $q = -i^2$ mod 7: $6, 3, 5, 5, 3, 6$. So $q \in \{3, 5, 6\}$, each appearing twice (corresponding to $i$ and $-i$).

For $s = 1$: $q = i(1-i)$ for $i \in \{1, 2, 3, 4, 5, 6\} \setminus \{1, 4\}$ (excluding $i = s = 1$ and $i = s/2$... wait, $s/2 = 4$ in $\mathbb{F}_7$ since $2 \cdot 4 = 8 \equiv 1$). So $i \in \{2, 3, 5, 6\}$.
- $i = 2$: $q = 2 \cdot (-1) = -2 \equiv 5$
- $i = 3$: $q = 3 \cdot (-2) = -6 \equiv 1$
- $i = 5$: $q = 5 \cdot (-4) = -20 \equiv 1$
- $i = 6$: $q = 6 \cdot (-5) = -30 \equiv 5$

So for $s = 1$: $q \in \{1, 5\}$, each appearing twice (as expected, since $(i, j)$ and $(j, i)$ give the same $q$).

For $s = 2$: $s/2 = 1$, exclude $i = 2$ and $i = 1$. $i \in \{3, 4, 5, 6\}$.
- $i = 3$: $q = 3 \cdot (-1) = -3 \equiv 4$
- $i = 4$: $q = 4 \cdot (-2) = -8 \equiv 6$
- $i = 5$: $q = 5 \cdot (-3) = -15 \equiv 6$
- $i = 6$: $q = 6 \cdot (-4) = -24 \equiv 4$

$q \in \{4, 6\}$.

For $s = 3$: $s/2 = 5$ (since $2 \cdot 5 = 10 \equiv 3$), exclude $i = 3$ and $i = 5$. $i \in \{1, 2, 4, 6\}$.
- $i = 1$: $q = 1 \cdot (-2) = -2 \equiv 5$
- $i = 2$: $q = 2 \cdot (-1) = -2 \equiv 5$... wait, $j = s - i = 3 - 2 = 1$. $q = 2 \cdot 1 = 2$. Let me recompute.

Oh wait, I think I made an error. $q = i(s - i)$, not $i \cdot (-i)$. Let me redo.

For $s = 3$: $q = i(3 - i)$ for $i \in \{1, 2, 4, 6\}$ (excluding $i = 3$ and $i = 5 = s/2$).
- $i = 1$: $q = 1 \cdot 2 = 2$
- $i = 2$: $q = 2 \cdot 1 = 2$
- $i = 4$: $q = 4 \cdot (-1) = -4 \equiv 3$
- $i = 6$: $q = 6 \cdot (-3) = -18 \equiv 3$

$q \in \{2, 3\}$.

For $s = 4$: $s/2 = 2$, exclude $i = 4$ and $i = 2$. $i \in \{1, 3, 5, 6\}$.
- $i = 1$: $q = 1 \cdot 3 = 3$
- $i = 3$: $q = 3 \cdot 1 = 3$
- $i = 5$: $q = 5 \cdot (-1) = -5 \equiv 2$
- $i = 6$: $q = 6 \cdot (-2) = -12 \equiv 2$

$q \in \{2, 3\}$.

For $s = 5$: $s/2 = 6$ (since $2 \cdot 6 = 12 \equiv 5$), exclude $i = 5$ and $i = 6$. $i \in \{1, 2, 3, 4\}$.
- $i = 1$: $q = 1 \cdot 4 = 4$
- $i = 2$: $q = 2 \cdot 3 = 6$
- $i = 3$: $q = 3 \cdot 2 = 6$
- $i = 4$: $q = 4 \cdot 1 = 4$

$q \in \{4, 6\}$.

For $s = 6$: $s/2 = 3$, exclude $i = 6$ and $i = 3$. $i \in \{1, 2, 4, 5\}$.
- $i = 1$: $q = 1 \cdot 5 = 5$
- $i = 2$: $q = 2 \cdot 4 = 1$
- $i = 4$: $q = 4 \cdot 2 = 1$
- $i = 5$: $q = 5 \cdot 1 = 5$

$q \in \{1, 5\}$.

So the valid $(s, q)$ pairs are:
- $s = 0$: $q \in \{3, 5, 6\}$
- $s = 1$: $q \in \{1, 5\}$
- $s = 2$: $q \in \{4, 6\}$
- $s = 3$: $q \in \{2, 3\}$
- $s = 4$: $q \in \{2, 3\}$
- $s = 5$: $q \in \{4, 6\}$
- $s = 6$: $q \in \{1, 5\}$

The condition for $Q$ injective is: $a(s^2 - q) + bs + c \neq 0$ for all these $(s, q)$ pairs.

That is, $q \neq s^2 + (bs + c)/a$ for all valid $(s, q)$.

Let $f(s) = s^2 + (bs + c)/a = s^2 + (b/a)s + (c/a)$. We need: for each $s$, $f(s) \notin Q_s$ where $Q_s$ is the set of valid $q$ values for that $s$.

- $s = 0$: $f(0) = c/a \notin \{3, 5, 6\}$
- $s = 1$: $f(1) = 1 + b/a + c/a \notin \{1, 5\}$
- $s = 2$: $f(2) = 4 + 2b/a + c/a \notin \{4, 6\}$
- $s = 3$: $f(3) = 2 + 3b/a + c/a \notin \{2, 3\}$ (since $9 \equiv 2$ mod 7)
- $s = 4$: $f(4) = 2 + 4b/a + c/a \notin \{2, 3\}$ (since $16 \equiv 2$)
- $s = 5$: $f(5) = 4 + 5b/a + c/a \notin \{4, 6\}$ (since $25 \equiv 4$)
- $s = 6$: $f(6) = 1 + 6b/a + c/a \notin \{1, 5\}$ (since $36 \equiv 1$)

Let $\alpha = b/a, \beta = c/a$. Then:
- $s = 0$: $\beta \notin \{3, 5, 6\}$, so $\beta \in \{0, 1, 2, 4\}$
- $s = 1$: $1 + \alpha + \beta \notin \{1, 5\}$, so $1 + \alpha + \beta \in \{0, 2, 3, 4, 6\}$
- $s = 2$: $4 + 2\alpha + \beta \notin \{4, 6\}$, so $4 + 2\alpha + \beta \in \{0, 1, 2, 3, 5\}$
- $s = 3$: $2 + 3\alpha + \beta \notin \{2, 3\}$, so $2 + 3\alpha + \beta \in \{0, 1, 4, 5, 6\}$
- $s = 4$: $2 + 4\alpha + \beta \notin \{2, 3\}$, so $2 + 4\alpha + \beta \in \{0, 1, 4, 5, 6\}$
- $s = 5$: $4 + 5\alpha + \beta \notin \{4, 6\}$, so $4 + 5\alpha + \beta \in \{0, 1, 2, 3, 5\}$
- $s = 6$: $1 + 6\alpha + \beta \notin \{1, 5\}$, so $1 + 6\alpha + \beta \in \{0, 2, 3, 4, 6\}$

Note the symmetry: $s$ and $-s$ (i.e., $s$ and $7 - s$) have the same $Q_s$ sets (since if $(i, j)$ gives sum $s$, then $(-i, -j)$ gives sum $-s$ and product $q$). Indeed:
- $s = 1$ and $s = 6$: both have $Q_s = \{1, 5\}$
- $s = 2$ and $s = 5$: both have $Q_s = \{4, 6\}$
- $s = 3$ and $s = 4$: both have $Q_s = \{2, 3\}$

And $f(-s) = s^2 - \alpha s + \beta$ while $f(s) = s^2 + \alpha s + \beta$.

Let me denote $f(s) = s^2 + \alpha s + \beta$. The conditions are:
- $f(0) = \beta \in \{0, 1, 2, 4\}$
- $f(1) \in \{0, 2, 3, 4, 6\}$ and $f(6) \in \{0, 2, 3, 4, 6\}$
- $f(2) \in \{0, 1, 2, 3, 5\}$ and $f(5) \in \{0, 1, 2, 3, 5\}$
- $f(3) \in \{0, 1, 4, 5, 6\}$ and $f(4) \in \{0, 1, 4, 5, 6\}$

Note $f(s) + f(-s) = 2s^2 + 2\beta$ and $f(s) - f(-s) = 2\alpha s$.

For $s = 1, 6$: $f(1) = 1 + \alpha + \beta$, $f(6) = 1 - \alpha + \beta$. Both in $\{0, 2, 3, 4, 6\}$ (not in $\{1, 5\}$).
For $s = 2, 5$: $f(2) = 4 + 2\alpha + \beta$, $f(5) = 4 - 2\alpha + \beta$. Both in $\{0, 1, 2, 3, 5\}$ (not in $\{4, 6\}$).
For $s = 3, 4$: $f(3) = 2 + 3\alpha + \beta$, $f(4) = 2 - 3\alpha + \beta$. Both in $\{0, 1, 4, 5, 6\}$ (not in $\{2, 3\}$).

Let me try $\beta = 0$:
- $f(0) = 0 \in \{0, 1, 2, 4\}$ ✓
- $f(1) = 1 + \alpha$, $f(6) = 1 - \alpha$. Both $\notin \{1, 5\}$.
  - $1 + \alpha \neq 1 \Rightarrow \alpha \neq 0$; $1 + \alpha \neq 5 \Rightarrow \alpha \neq 4$
  - $1 - \alpha \neq 1 \Rightarrow \alpha \neq 0$; $1 - \alpha \neq 5 \Rightarrow \alpha \neq -4 = 3$
  - So $\alpha \notin \{0, 3, 4\}$, i.e., $\alpha \in \{1, 2, 5, 6\}$
- $f(2) = 4 + 2\alpha$, $f(5) = 4 - 2\alpha$. Both $\notin \{4, 6\}$.
  - $4 + 2\alpha \neq 4 \Rightarrow \alpha \neq 0$; $4 + 2\alpha \neq 6 \Rightarrow 2\alpha \neq 2 \Rightarrow \alpha \neq 1$
  - $4 - 2\alpha \neq 4 \Rightarrow \alpha \neq 0$; $4 - 2\alpha \neq 6 \Rightarrow -2\alpha \neq 2 \Rightarrow \alpha \neq -1 = 6$
  - So $\alpha \notin \{0, 1, 6\}$, combined with above: $\alpha \in \{2, 5\}$
- $f(3) = 2 + 3\alpha$, $f(4) = 2 - 3\alpha$. Both $\notin \{2, 3\}$.
  - $2 + 3\alpha \neq 2 \Rightarrow \alpha \neq 0$; $2 + 3\alpha \neq 3 \Rightarrow 3\alpha \neq 1 \Rightarrow \alpha \neq 5$ (since $3 \cdot 5 = 15 \equiv 1$)
  - $2 - 3\alpha \neq 2 \Rightarrow \alpha \neq 0$; $2 - 3\alpha \neq 3 \Rightarrow -3\alpha \neq 1 \Rightarrow \alpha \neq -5 = 2$ (since $3 \cdot 2 = 6 \equiv -1$, so $-3 \cdot 2 = 1$)
  - So $\alpha \notin \{0, 2, 5\}$. But we needed $\alpha \in \{2, 5\}$. Contradiction!

So $\beta = 0$ doesn't work.

Let me try $\beta = 1$:
- $f(0) = 1 \in \{0, 1, 2, 4\}$ ✓
- $f(1) = 2 + \alpha$, $f(6) = 2 - \alpha$. Both $\notin \{1, 5\}$.
  - $2 + \alpha \neq 1 \Rightarrow \alpha \neq 6$; $2 + \alpha \neq 5 \Rightarrow \alpha \neq 3$
  - $2 - \alpha \neq 1 \Rightarrow \alpha \neq 1$; $2 - \alpha \neq 5 \Rightarrow \alpha \neq -3 = 4$
  - $\alpha \notin \{1, 3, 4, 6\}$, so $\alpha \in \{0, 2, 5\}$
- $f(2) = 5 + 2\alpha$, $f(5) = 5 - 2\alpha$. Both $\notin \{4, 6\}$.
  - $5 + 2\alpha \neq 4 \Rightarrow 2\alpha \neq 6 \Rightarrow \alpha \neq 3$; $5 + 2\alpha \neq 6 \Rightarrow 2\alpha \neq 1 \Rightarrow \alpha \neq 4$
  - $5 - 2\alpha \neq 4 \Rightarrow 2\alpha \neq 1 \Rightarrow \alpha \neq 4$; $5 - 2\alpha \neq 6 \Rightarrow -2\alpha \neq 1 \Rightarrow \alpha \neq 3$
  - $\alpha \notin \{3, 4\}$, combined: $\alpha \in \{0, 2, 5\}$
- $f(3) = 3 + 3\alpha$, $f(4) = 3 - 3\alpha$. Both $\notin \{2, 3\}$.
  - $3 + 3\alpha \neq 2 \Rightarrow 3\alpha \neq 6 \Rightarrow \alpha \neq 2$; $3 + 3\alpha \neq 3 \Rightarrow \alpha \neq 0$
  - $3 - 3\alpha \neq 2 \Rightarrow 3\alpha \neq 1 \Rightarrow \alpha \neq 5$; $3 - 3\alpha \neq 3 \Rightarrow \alpha \neq 0$
  - $\alpha \notin \{0, 2, 5\}$. But we needed $\alpha \in \{0, 2, 5\}$. Contradiction!

$\beta = 2$:
- $f(0) = 2 \in \{0, 1, 2, 4\}$ ✓
- $f(1) = 3 + \alpha$, $f(6) = 3 - \alpha$. Both $\notin \{1, 5\}$.
  - $3 + \alpha \neq 1 \Rightarrow \alpha \neq 5$; $3 + \alpha \neq 5 \Rightarrow \alpha \neq 2$
  - $3 - \alpha \neq 1 \Rightarrow \alpha \neq 2$; $3 - \alpha \neq 5 \Rightarrow \alpha \neq 5$
  - $\alpha \notin \{2, 5\}$, so $\alpha \in \{0, 1, 3, 4, 6\}$
- $f(2) = 6 + 2\alpha$, $f(5) = 6 - 2\alpha$. Both $\notin \{4, 6\}$.
  - $6 + 2\alpha \neq 4 \Rightarrow 2\alpha \neq 5 \Rightarrow \alpha \neq 6$; $6 + 2\alpha \neq 6 \Rightarrow \alpha \neq 0$
  - $6 - 2\alpha \neq 4 \Rightarrow 2\alpha \neq 2 \Rightarrow \alpha \neq 1$; $6 - 2\alpha \neq 6 \Rightarrow \alpha \neq 0$
  - $\alpha \notin \{0, 1, 6\}$, combined: $\alpha \in \{3, 4\}$
- $f(3) = 4 + 3\alpha$, $f(4) = 4 - 3\alpha$. Both $\notin \{2, 3\}$.
  - $4 + 3\alpha \neq 2 \Rightarrow 3\alpha \neq 5 \Rightarrow \alpha \neq 4$; $4 + 3\alpha \neq 3 \Rightarrow 3\alpha \neq 6 \Rightarrow \alpha \neq 2$
  - $4 - 3\alpha \neq 2 \Rightarrow 3\alpha \neq 2 \Rightarrow \alpha \neq 3$; $4 - 3\alpha \neq 3 \Rightarrow 3\alpha \neq 1 \Rightarrow \alpha \neq 5$
  - $\alpha \notin \{2, 3, 4, 5\}$. But we needed $\alpha \in \{3, 4\}$. Contradiction!

$\beta = 4$:
- $f(0) = 4 \in \{0, 1, 2, 4\}$ ✓
- $f(1) = 5 + \alpha$, $f(6) = 5 - \alpha$. Both $\notin \{1, 5\}$.
  - $5 + \alpha \neq 1 \Rightarrow \alpha \neq 3$; $5 + \alpha \neq 5 \Rightarrow \alpha \neq 0$
  - $5 - \alpha \neq 1 \Rightarrow \alpha \neq 4$; $5 - \alpha \neq 5 \Rightarrow \alpha \neq 0$
  - $\alpha \notin \{0, 3, 4\}$, so $\alpha \in \{1, 2, 5, 6\}$
- $f(2) = 1 + 2\alpha$, $f(5) = 1 - 2\alpha$. Both $\notin \{4, 6\}$.
  - $1 + 2\alpha \neq 4 \Rightarrow 2\alpha \neq 3 \Rightarrow \alpha \neq 5$; $1 + 2\alpha \neq 6 \Rightarrow 2\alpha \neq 5 \Rightarrow \alpha \neq 6$
  - $1 - 2\alpha \neq 4 \Rightarrow 2\alpha \neq 4 \Rightarrow \alpha \neq 2$; $1 - 2\alpha \neq 6 \Rightarrow 2\alpha \neq 2 \Rightarrow \alpha \neq 1$
  - $\alpha \notin \{1, 2, 5, 6\}$. But we needed $\alpha \in \{1, 2, 5, 6\}$. Contradiction!

So no cubic is injective on $\mathbb{F}_7^*$! This means degree 3 doesn't work for $p = 7$.

Let me check degree 4 for $p = 7$.

$Q(x) = ax^4 + bx^3 + cx^2 + dx + e$, $a \neq 0$.

$Q(i) - Q(j) = (i-j)[a(i^3 + i^2j + ij^2 + j^3) + b(i^2 + ij + j^2) + c(i+j) + d]$.

Using $s = i+j, q = ij$:
- $i^2 + ij + j^2 = s^2 - q$
- $i^3 + i^2j + ij^2 + j^3 = (i+j)(i^2 + j^2) + ij(i+j) = s(s^2 - 2q) + qs = s^3 - qs$

Wait, let me recompute. $i^3 + i^2j + ij^2 + j^3 = (i^3 + j^3) + ij(i + j) = (i+j)(i^2 - ij + j^2) + ij(i+j) = (i+j)(i^2 - ij + j^2 + ij) = (i+j)(i^2 + j^2) = s(s^2 - 2q)$.

So $Q(i) - Q(j) = (i-j)[a \cdot s(s^2 - 2q) + b(s^2 - q) + cs + d]$.

For injectivity: $a \cdot s(s^2 - 2q) + b(s^2 - q) + cs + d \neq 0$ for all valid $(s, q)$.

This is $as^3 - 2asq + bs^2 - bq + cs + d = as^3 + bs^2 + cs + d - q(2as + b)$.

So the condition is $q \neq \frac{as^3 + bs^2 + cs + d}{2as + b}$ (when $2as + b \neq 0$) for all valid $(s, q)$.

When $2as + b = 0$, the condition becomes $as^3 + bs^2 + cs + d \neq 0$.

This is more flexible. Let me define $g(s) = \frac{as^3 + bs^2 + cs + d}{2as + b}$ (when $2as + b \neq 0$). We need $g(s) \notin Q_s$ for each $s$.

This is a degree 3 over degree 1 rational function, which simplifies to a degree 2 polynomial (plus a remainder). Specifically, $g(s) = \frac{as^3 + bs^2 + cs + d}{2as + b}$.

Let me do polynomial division. $\frac{as^3 + bs^2 + cs + d}{2as + b}$.

Dividing $as^3$ by $2as$ gives $\frac{s^2}{2}$. Multiply: $\frac{s^2}{2}(2as + b) = as^3 + \frac{bs^2}{2}$. Subtract: $(b - \frac{b}{2})s^2 + cs + d = \frac{b}{2}s^2 + cs + d$.

Dividing $\frac{b}{2}s^2$ by $2as$ gives $\frac{b}{4a}s$. Multiply: $\frac{b}{4a}s(2as + b) = \frac{b}{2}s^2 + \frac{b^2}{4a}s$. Subtract: $(c - \frac{b^2}{4a})s + d$.

Dividing $(c - \frac{b^2}{4a})s$ by $2as$ gives $\frac{c - \frac{b^2}{4a}}{2a} = \frac{4ac - b^2}{8a^2}$. Multiply: $\frac{4ac - b^2}{8a^2}(2as + b) = \frac{4ac - b^2}{4a}s + \frac{b(4ac - b^2)}{8a^2}$. Subtract: $d - \frac{b(4ac - b^2)}{8a^2}$.

So $g(s) = \frac{s^2}{2} + \frac{b}{4a}s + \frac{4ac - b^2}{8a^2} + \frac{d - \frac{b(4ac - b^2)}{8a^2}}{2as + b}$.

This is a quadratic in $s$ plus a rational remainder term. The quadratic part is $\frac{s^2}{2} + \frac{b}{4a}s + \frac{4ac - b^2}{8a^2} = \frac{1}{2}(s + \frac{b}{2a})^2 - \frac{b^2}{8a^2} + \frac{4ac - b^2}{8a^2} = \frac{1}{2}(s + \frac{b}{2a})^2 + \frac{4ac - 2b^2}{8a^2} = \frac{1}{2}(s + \frac{b}{2a})^2 + \frac{2ac - b^2}{4a^2}$.

So $g(s) = \frac{1}{2}(s + \frac{b}{2a})^2 + \frac{2ac - b^2}{4a^2} + \frac{R}{2as + b}$ where $R = d - \frac{b(4ac - b^2)}{8a^2}$.

The key point is that $g(s)$ is essentially a shifted square plus a correction term. The square part means $g(s) = g(-s - \frac{b}{a})$... no, that's not quite right because of the remainder term.

Actually, this is getting very complicated. Let me try a different approach.

Let me try to find a degree 4 polynomial for $p = 7$ by trial.

$Q(x) = x^4 + 1$:
Values on $\{1, ..., 6\}$ mod 7:
- $1 + 1 = 2$
- $16 + 1 = 17 \equiv 3$
- $81 + 1 = 82 \equiv 82 - 11 \cdot 7 = 5$
- $256 + 1 = 257 \equiv 257 - 36 \cdot 7 = 5$
Not injective (5 repeated).

$Q(x) = x^4 + x + 1$:
- $1 + 1 + 1 = 3$
- $16 + 2 + 1 = 19 \equiv 5$
- $81 + 3 + 1 = 85 \equiv 1$
- $256 + 4 + 1 = 261 \equiv 261 - 37 \cdot 7 = 2$
- $625 + 5 + 1 = 631 \equiv 631 - 90 \cdot 7 = 1$
Not injective.

$Q(x) = x^4 + x^2 + 1$:
- $1 + 1 + 1 = 3$
- $16 + 4 + 1 = 21 \equiv 0$
- $81 + 9 + 1 = 91 \equiv 0$
Not injective.

$Q(x) = x^4 + x^3 + 1$:
- $1 + 1 + 1 = 3$
- $16 + 8 + 1 = 25 \equiv 4$
- $81 + 27 + 1 = 109 \equiv 109 - 15 \cdot 7 = 4$
Not injective.

$Q(x) = x^4 + 2x + 1$:
- $1 + 2 + 1 = 4$
- $16 + 4 + 1 = 21 \equiv 0$
- $81 + 6 + 1 = 88 \equiv 88 - 12 \cdot 7 = 4$
Not injective.

$Q(x) = 2x^4 + x + 1$:
- $2 + 1 + 1 = 4$
- $32 + 2 + 1 = 35 \equiv 0$
- $162 + 3 + 1 = 166 \equiv 166 - 23 \cdot 7 = 5$
- $512 + 4 + 1 = 517 \equiv 517 - 73 \cdot 7 = 6$
- $1250 + 5 + 1 = 1256 \equiv 1256 - 179 \cdot 7 = 3$
- $2592 + 6 + 1 = 2599 \equiv 2599 - 371 \cdot 7 = 2$

Values: $4, 0, 5, 6, 3, 2$. All distinct! ✓

Now check $xQ(x) = 2x^5 + x^2 + x$:
- $x=1$: $2 + 1 + 1 = 4$
- $x=2$: $64 + 4 + 2 = 70 \equiv 0$
- $x=3$: $486 + 9 + 3 = 498 \equiv 498 - 71 \cdot 7 = 1$
- $x=4$: $2048 + 16 + 4 = 2068 \equiv 2068 - 295 \cdot 7 = 3$
- $x=5$: $6250 + 25 + 5 = 6280 \equiv 6280 - 897 \cdot 7 = 1$
Not injective (1 repeated).

Hmm. Let me try other degree 4 polynomials.

$Q(x) = 2x^4 + x^2 + x + 1$:
- $2 + 1 + 1 + 1 = 5$
- $32 + 4 + 2 + 1 = 39 \equiv 4$
- $162 + 9 + 3 + 1 = 175 \equiv 0$
- $512 + 16 + 4 + 1 = 533 \equiv 533 - 76 \cdot 7 = 1$
- $1250 + 25 + 5 + 1 = 1281 \equiv 1281 - 183 \cdot 7 = 0$
Not injective.

$Q(x) = 2x^4 + 2x + 1$:
- $2 + 2 + 1 = 5$
- $32 + 4 + 1 = 37 \equiv 2$
- $162 + 6 + 1 = 169 \equiv 169 - 24 \cdot 7 = 1$
- $512 + 8 + 1 = 521 \equiv 521 - 74 \cdot 7 = 3$
- $1250 + 10 + 1 = 1261 \equiv 1261 - 180 \cdot 7 = 1$
Not injective.

$Q(x) = 2x^4 + x^3 + x + 1$:
- $2 + 1 + 1 + 1 = 5$
- $32 + 8 + 2 + 1 = 43 \equiv 1$
- $162 + 27 + 3 + 1 = 193 \equiv 193 - 27 \cdot 7 = 4$
- $512 + 64 + 4 + 1 = 581 \equiv 581 - 83 \cdot 7 = 0$
- $1250 + 125 + 5 + 1 = 1381 \equiv 1381 - 197 \cdot 7 = 2$
- $2592 + 216 + 6 + 1 = 
