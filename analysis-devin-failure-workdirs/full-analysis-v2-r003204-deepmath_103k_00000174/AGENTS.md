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
  <problem_id>deepmath_103k_00000174</problem_id>
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

Find the radius of convergence for the series \( \sum_{n\geq 1}\left(\frac{x}{\sin n}\right)^{n} \).

## Standard Solution

Alright, so I need to find the radius of convergence for the power series \(\sum_{n\geq 1}\left(\frac{x}{\sin n}\right)^{n}\). Hmm, okay. Let me recall how to do that. The radius of convergence for a series \(\sum a_n x^n\) is usually found using the root test or the ratio test. But here, the series isn't exactly in the form \(\sum a_n x^n\); instead, it's \(\sum \left(\frac{x}{\sin n}\right)^n\), which can be rewritten as \(\sum \left(\frac{1}{\sin n}\right)^n x^n\). So in this case, the coefficient \(a_n\) is \(\left(\frac{1}{\sin n}\right)^n\). 

Therefore, the radius of convergence \(R\) should be given by the reciprocal of the limit superior of \(|a_n|^{1/n}\) as \(n\) approaches infinity. The formula is \(1/\limsup_{n\to\infty} |a_n|^{1/n}\). Let me write that down:

\[
R = \frac{1}{\limsup_{n\to\infty} |a_n|^{1/n}} = \frac{1}{\limsup_{n\to\infty} \left|\frac{1}{\sin n}\right|}
\]

Wait, hold on. Because \(a_n = \left(\frac{1}{\sin n}\right)^n\), so \(|a_n|^{1/n} = \left|\frac{1}{\sin n}\right|\). So the radius of convergence is \(1/\limsup_{n\to\infty} |1/\sin n|\). But now, I need to figure out what \(\limsup_{n\to\infty} |1/\sin n|\) is. 

Hmm, this depends on the behavior of \(|\sin n|\) as \(n\) approaches infinity. Since \(n\) here is in radians, right? Because in calculus, unless specified otherwise, trigonometric functions are usually in radians. So \(n\) is an integer in radians. So we need to consider the values of \(\sin n\) for integer values of \(n\). 

But how does \(\sin n\) behave as \(n\) grows? Since \(n\) is an integer multiple of radians, and \(\pi\) is irrational, the sequence \(n \mod \pi\) is dense in \([0, \pi]\). Wait, is that the case? Actually, more accurately, because we're dealing with integers and \(\pi\) is irrational, the fractional parts of \(n/(2\pi)\) are dense in [0,1), due to equidistribution theorem. Therefore, the sequence \(n \mod 2\pi\) is dense in \([0, 2\pi)\). Therefore, the values of \(\sin n\) should be dense in \([-1, 1]\). But since \(n\) is an integer, and \(\sin n\) is evaluated at integer radians. 

Wait, but \(\sin n\) is periodic with period \(2\pi\), but since \(n\) is an integer and \(2\pi\) is irrational, the values \(\sin n\) do not repeat periodically. Instead, they are dense in \([-1,1]\). So this means that for any \(y \in [-1,1]\), there exists a subsequence \(n_k\) such that \(\sin n_k\) approaches \(y\). Therefore, the lim sup of \(|\sin n|\) as \(n\) approaches infinity is 1, because there are infinitely many \(n\) for which \(\sin n\) is close to 1 or -1. Similarly, the lim inf of \(|\sin n|\) is 0, because we can get \(\sin n\) arbitrarily close to 0. 

But in our case, we need the lim sup of \(|1/\sin n|\). Since \(|\sin n|\) can get arbitrarily close to 0, \(|1/\sin n|\) can get arbitrarily large. Therefore, the lim sup of \(|1/\sin n|\) as \(n\) approaches infinity is infinity. Therefore, \(R = 1/\infty = 0\). 

Wait, does that mean the radius of convergence is 0? That seems too hasty. Let me check again. The radius of convergence is determined by the lim sup of \(|a_n|^{1/n}\), which in this case is \(|1/\sin n|\). So the lim sup of \(|1/\sin n|\) as \(n \to \infty\) is infinity. Therefore, the reciprocal is zero. So the radius of convergence is zero. 

But does that make sense? If the radius of convergence is zero, the series only converges when \(x = 0\). Let me test this intuition. Suppose we fix an \(x \neq 0\). Then the term \(\left(\frac{x}{\sin n}\right)^n\) for some \(n\) where \(|\sin n|\) is very small would be enormous, right? For example, if there exists a subsequence \(n_k\) where \(|\sin n_k| < \epsilon\), then \(|\frac{x}{\sin n_k}|^{n_k} > \left(\frac{|x|}{\epsilon}\right)^{n_k}\). If \(\epsilon\) is very small, say \(\epsilon = 1/n_k\), then this term would be \(|x| n_k|^{n_k}\), which tends to infinity as \(n_k\) increases (unless \(x = 0\)). Therefore, the terms of the series do not approach zero for any \(x \neq 0\), hence the series diverges everywhere except at \(x = 0\). 

Therefore, the radius of convergence is indeed 0. But let me think again. Maybe there's a mistake here. 

Wait, but perhaps I need to be careful with the root test. The root test says that the radius of convergence is \(1/\limsup_{n \to \infty} |a_n|^{1/n}\). Here, \(a_n = \left(\frac{1}{\sin n}\right)^n\), so \(|a_n|^{1/n} = \left|\frac{1}{\sin n}\right|\). So the lim sup of this is infinity. Therefore, \(1/\infty = 0\). So yes, the radius of convergence is 0. 

Alternatively, using the root test for the series \(\sum \left( \frac{x}{\sin n} \right)^n\), the nth root of the absolute value is \(\left| \frac{x}{\sin n} \right|\). For convergence, we need this to be less than 1 for sufficiently large n. But since \(|\sin n|\) can be arbitrarily small, \(|\frac{x}{\sin n}|\) can be arbitrarily large for any fixed \(x \neq 0\). Therefore, there are infinitely many n for which the nth root exceeds 1, hence the series diverges for any \(x \neq 0\). Therefore, radius of convergence is 0. 

Hmm. But maybe there's a different approach? Let me check with the definition. The radius of convergence is the supremum of all real numbers \(r \geq 0\) such that the series converges absolutely for all x with |x| < r. If the radius were greater than 0, say R > 0, then for |x| < R, the series converges. But take x = R/2. Then we have terms \(\left( \frac{R/2}{\sin n} \right)^n\). Since |\sin n| can be as small as we like, we can find n where |\sin n| < R/(2*2), so that |R/(2 sin n)| > 2, so the term would be greater than 2^n, which goes to infinity. Therefore, even for x = R/2, the series would have unbounded terms, hence cannot converge. Therefore, R must be 0. 

Therefore, regardless of the method, the radius of convergence is 0. 

But let me check some references or similar problems. Wait, actually, in some textbooks, there's an example where the coefficients involve terms like 1/sin(n), but raised to the nth power. Hmm, for example, if you have \(\sum (\frac{x}{a_n})^n\), then the radius of convergence is determined by the lim sup of |1/a_n|. So if a_n approaches 0 infinitely often, then the lim sup is infinity, and the radius is 0. 

Alternatively, maybe using the root test more formally: 

For the series \(\sum_{n \geq 1} \left( \frac{x}{\sin n} \right)^n\), apply the root test. The nth root of the absolute value of the nth term is |x / sin n|. The root test says that if lim sup |x / sin n| < 1, the series converges absolutely; if lim sup |x / sin n| > 1, it diverges. 

But for any fixed x ≠ 0, since lim sup |1 / sin n| = ∞, then lim sup |x / sin n| = ∞. Therefore, for any x ≠ 0, lim sup |x / sin n| = ∞ > 1, so the series diverges. Therefore, the radius of convergence is 0. 

Yes, that makes sense. Therefore, the answer should be 0. 

Wait, but wait another moment. The problem says "the series \( \sum_{n\geq 1}\left(\frac{x}{\sin n}\right)^{n} \)". Is there a possibility that sin n is bounded away from zero? But as we discussed before, since n is an integer in radians, and pi is irrational, the sequence {n mod pi} is dense in [0, pi], so sin n can get arbitrarily close to zero. Therefore, |1/sin n| is unbounded. Hence, the lim sup is infinity. 

Therefore, radius of convergence is 0. 

Therefore, the answer is 0.

**Final Answer**
The radius of convergence is \(\boxed{0}\).
</think>

To find the radius of convergence for the series \( \sum_{n\geq 1}\left(\frac{x}{\sin n}\right)^{n} \), we use the root test. The series can be rewritten as \( \sum_{n\geq 1} \left( \frac{1}{\sin n} \right)^n x^n \), where the coefficient \( a_n = \left( \frac{1}{\sin n} \right)^n \).

The radius of convergence \( R \) is given by the reciprocal of the limit superior of \( |a_n|^{1/n} \):

\[
R = \frac{1}{\limsup_{n\to\infty} |a_n|^{1/n}}
\]

Here, \( |a_n|^{1/n} = \left| \frac{1}{\sin n} \right| \). We need to determine \( \limsup_{n\to\infty} \left| \frac{1}{\sin n} \right| \).

Since \( n \) is an integer and \( \pi \) is irrational, the sequence \( n \mod \pi \) is dense in \( [0, \pi) \). This implies that \( \sin n \) can get arbitrarily close to 0 for infinitely many \( n \). Therefore, \( |1/\sin n| \) can become arbitrarily large, leading to:

\[
\limsup_{n\to\infty} \left| \frac{1}{\sin n} \right| = \infty
\]

Thus, the radius of convergence is:

\[
R = \frac{1}{\infty} = 0
\]

Hence, the radius of convergence for the series is \(\boxed{0}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

The problem asks: Determine the degree of extension of the algebraic closure over the field $\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p)$, where $p$ is a prime number.

Let me first understand the construction.

$\mathbb{Z}((X))$ is the ring of formal Laurent series in $X$ with integer coefficients. The "conti" subscript likely refers to the subring of "continuous" Laurent series, or more precisely, the $X$-adic completion or something related.

Actually, let me think about this more carefully. $\mathbb{Z}((X))$ is the ring of formal Laurent series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$.

The notation $\mathbb{Z}((X))_{conti}$ — this likely refers to the ring of formal series $\sum_{n \geq n_0} a_n X^n$ where the coefficients $a_n$ are "continuous" in some sense. 

Actually, I think this is related to the construction of $\mathbb{Q}_p$ via the "field of norms" or via a specific quotient construction.

Let me reconsider. The quotient $\mathbb{Z}((X))/(X-p)$: if we mod out by $(X-p)$, we're setting $X = p$. So a formal Laurent series $\sum a_n X^n$ becomes $\sum a_n p^n$, which converges $p$-adically. But we need to be careful about which series give well-defined $p$-adic numbers.

Actually, $\mathbb{Z}((X))$ consists of series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$ and $n_0 \in \mathbb{Z}$ (possibly negative). When we substitute $X = p$, we get $\sum_{n \geq n_0} a_n p^n$. For this to converge $p$-adically, we need... well, if $n_0$ can be any integer (possibly very negative), then $\sum_{n \geq n_0} a_n p^n$ might not converge. For example, if $n_0 = -100$, then $a_{n_0} p^{-100}$ is a rational number with denominator $p^{100}$, and the series $\sum_{n \geq n_0} a_n p^n$ would be a $p$-adic number only if it converges in $\mathbb{Q}_p$.

Actually, any series $\sum_{n \geq n_0} a_n p^n$ with $a_n \in \mathbb{Z}$ converges in $\mathbb{Q}_p$ because $|a_n p^n|_p \leq p^{-n} \to 0$ as $n \to \infty$. So the series converges $p$-adically for any starting index $n_0$.

But the issue is whether the map $\mathbb{Z}((X)) \to \mathbb{Q}_p$ sending $X \mapsto p$ is surjective. Every $p$-adic number can be written as $\sum_{n \geq n_0} a_n p^n$ with $a_n \in \{0, 1, \ldots, p-1\}$ (the $p$-adic expansion), so yes, the map is surjective onto $\mathbb{Q}_p$.

But is the kernel exactly $(X-p)$? This is where the "conti" condition comes in. The issue is that $\mathbb{Z}((X))$ is not a PID or a nice ring, and $(X-p)$ might not be a maximal ideal, or the quotient might not be what we expect.

Wait, let me reconsider the "conti" notation. I think $\mathbb{Z}((X))_{conti}$ refers to the ring of formal series $\sum_{n \geq n_0} a_n X^n$ where the map $n \mapsto a_n$ is "continuous" in some topology, or more likely, it refers to the subring where the coefficients satisfy some boundedness or continuity condition.

Actually, I think this might be related to the concept from the theory of "perfectoid" or "field of norms" or perhaps the construction by Kedlaya or others.

Let me think about this differently. The notation $\mathbb{Z}((X))_{conti}$ might refer to the ring of formal series $\sum_{n \geq n_0} a_n X^n$ such that the sequence $(a_n)$ is eventually periodic modulo any power of $p$, or something like that. 

Hmm, actually I recall that in some contexts, particularly related to the work of Kedlaya on "slopes of $p$-adic differential equations" and the theory of "twisted Laurent series", there's a notion of $\mathbb{Z}((X))_{conti}$ being the ring of formal Laurent series $\sum a_n X^n$ where the coefficients $a_n \in \mathbb{Z}$ form a "continuous" sequence, meaning that for each $k$, the sequence $a_n \mod p^k$ is eventually periodic.

Actually, I think I'm overcomplicating this. Let me reconsider.

The construction $\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p)$ suggests that this is some kind of "extension" of $\mathbb{Q}_p$, and the question asks about the degree of the algebraic closure over this field.

Let me think about what $\mathbb{Z}((X))_{conti}$ could be. 

One possibility: $\mathbb{Z}((X))_{conti}$ is the ring of formal Laurent series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$, equipped with the $(p, X)$-adic topology, and "conti" means we take the completion or some subring.

Another possibility: This is related to the construction in the theory of "large fields" or "ample fields".

Actually, let me think about this from the perspective of the answer. The question asks for "the degree of extension of the algebraic closure over $\mathbb{Q}_p^{ext}$". 

For $\mathbb{Q}_p$ itself, the algebraic closure $\overline{\mathbb{Q}_p}$ has infinite degree over $\mathbb{Q}_p$ (in fact, countably infinite degree). The algebraic closure of $\mathbb{Q}_p$ is not complete; its completion is $\mathbb{C}_p$.

Now, if $\mathbb{Q}_p^{ext}$ is some extension of $\mathbb{Q}_p$, the degree of the algebraic closure over it would depend on how much of the algebraic closure is already contained in $\mathbb{Q}_p^{ext}$.

Let me reconsider the construction. If $\mathbb{Z}((X))_{conti}$ is the ring of formal Laurent series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$ where the sequence $(a_n)$ is "continuous" (in the sense that for each $k$, $a_n \mod p^k$ is eventually periodic), then modding out by $(X-p)$ gives a field that contains $\mathbb{Q}_p$ but is potentially much larger.

Wait, actually, I think I need to reconsider. The key insight might be:

$\mathbb{Z}((X))$ is the ring of formal Laurent series with integer coefficients. The ideal $(X-p)$ in this ring... but $\mathbb{Z}((X))$ is not a field, it's a ring. The quotient $\mathbb{Z}((X))/(X-p)$ — is this even a field?

Actually, $\mathbb{Z}((X))$ is not a field (it's a domain but not a field, since $\mathbb{Z}$ is not a field). The field of fractions of $\mathbb{Z}((X))$ would be... hmm.

Let me reconsider. Maybe $\mathbb{Z}((X))_{conti}$ is defined to make the quotient a field.

Actually, I think the correct interpretation might be:

$\mathbb{Z}((X))_{conti}$ is the ring of formal series $\sum_{n \geq n_0} a_n X^n$ where $a_n \in \mathbb{Z}$ and the sequence is "continuous" in the profinite topology on $\mathbb{Z}$, meaning that for every $k$, the reduction mod $p^k$ gives an eventually periodic sequence. This is related to the concept of "$p$-quasi-automata" or the work of Kedlaya.

When we quotient by $(X-p)$, we get a field that is strictly larger than $\mathbb{Q}_p$.

Hmm, but I'm not sure about the exact definition. Let me try a different approach.

Actually, I think the key reference here might be the work of Kedlaya on "The algebraic closure of the field of formal Laurent series in positive characteristic" or related work on $p$-adic differential equations.

Let me think about this more carefully. In the theory of formal Laurent series:

- $\mathbb{F}_p((X))$ is the field of formal Laurent series over $\mathbb{F}_p$. Its algebraic closure has infinite degree, and the completion of the algebraic closure is the field of Puiseux series (in characteristic 0) or more complex (in characteristic $p$).

- For $\mathbb{Q}_p$, the algebraic closure $\overline{\mathbb{Q}_p}$ has countably infinite degree over $\mathbb{Q}_p$.

Now, the construction $\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p)$ seems to be building a field that is an extension of $\mathbb{Q}_p$ by somehow incorporating formal Laurent series.

Let me try yet another interpretation. Perhaps $\mathbb{Z}((X))_{conti}$ is the $X$-adic completion of $\mathbb{Z}[X, X^{-1}]$, which is $\mathbb{Z}((X))$, and "conti" refers to taking the subring of elements that are "continuous" as functions from $\mathbb{Z}_p$ to $\mathbb{Q}_p$ (i.e., the series that converge and give continuous functions on $\mathbb{Z}_p$ when $X$ is replaced by a $p$-adic variable).

Actually, I think I should consider the possibility that this is related to the concept of a "maximal immediate extension" or "spherically complete extension" of $\mathbb{Q}_p$.

Let me try to think about what happens when we substitute $X = p$ in a formal Laurent series.

A formal Laurent series $f(X) = \sum_{n \geq n_0} a_n X^n \in \mathbb{Z}((X))$ gives, upon substituting $X = p$, the series $\sum_{n \geq n_0} a_n p^n$. This always converges in $\mathbb{Q}_p$ (since $|a_n p^n|_p \leq p^{-n} \to 0$). So we get a map $\mathbb{Z}((X)) \to \mathbb{Q}_p$.

This map is surjective (every $p$-adic number has a $p$-adic expansion with digits in $\{0, \ldots, p-1\} \subset \mathbb{Z}$).

The kernel of this map consists of all formal Laurent series $\sum a_n X^n$ such that $\sum a_n p^n = 0$ in $\mathbb{Q}_p$.

Now, $(X-p)$ is contained in the kernel, but is the kernel exactly $(X-p)$? 

Consider the series $f(X) = \sum_{n=0}^{\infty} p^n X^n = \frac{1}{1-pX}$ (formally, this is in $\mathbb{Z}((X))$... wait, no, the coefficients are $p^n$ which are in $\mathbb{Z}$, so yes, $f(X) = \sum_{n=0}^{\infty} p^n X^n \in \mathbb{Z}[[X]] \subset \mathbb{Z}((X))$).

When we substitute $X = p$: $\sum_{n=0}^{\infty} p^n \cdot p^n = \sum_{n=0}^{\infty} p^{2n}$. This converges in $\mathbb{Q}_p$ to $\frac{1}{1-p^2}$.

Is $f(X) = \sum p^n X^n$ in the ideal $(X-p)$ of $\mathbb{Z}((X))$? We'd need $f(X) = (X-p) \cdot g(X)$ for some $g(X) \in \mathbb{Z}((X))$. 

$(X-p) \cdot g(X) = X \cdot g(X) - p \cdot g(X)$. If $g(X) = \sum b_n X^n$, then $(X-p)g(X) = \sum b_n X^{n+1} - \sum p b_n X^n = \sum (b_{n-1} - p b_n) X^n$ (with appropriate boundary conditions).

We need $b_{n-1} - p b_n = p^n$ for all $n \geq 0$ (and $b_{-1} = 0$ for the constant term).

From $n=0$: $b_{-1} - p b_0 = 1$, so $-p b_0 = 1$, so $b_0 = -1/p$. But $b_0$ must be in $\mathbb{Z}$, and $-1/p \notin \mathbb{Z}$. So $f(X) \notin (X-p)$ in $\mathbb{Z}((X))$.

But $f(p) = \sum p^{2n} = \frac{1}{1-p^2} \neq 0$ in $\mathbb{Q}_p$, so $f$ is not in the kernel either. So this doesn't give us a counterexample to the kernel being $(X-p)$.

Let me find something in the kernel but not in $(X-p)$. 

Consider $g(X) = \sum_{n=0}^{\infty} c_n X^n$ where we want $\sum c_n p^n = 0$ but $g \notin (X-p)$.

For example, take $c_0 = p, c_1 = -1$, and $c_n = 0$ for $n \geq 2$. Then $g(X) = p - X = -(X-p) \in (X-p)$. That's trivially in the ideal.

Let me try something more complex. Consider $h(X) = \sum_{n=0}^{\infty} a_n X^n$ where $a_0 = p^2, a_1 = 0, a_2 = -1$, rest zero. Then $h(p) = p^2 - p^2 = 0$. And $h(X) = p^2 - X^2 = (p-X)(p+X) = -(X-p)(p+X) \in (X-p)$. Still in the ideal.

OK so for polynomials, the kernel is exactly $(X-p) \cap \mathbb{Z}[X] = (X-p) \cdot \mathbb{Z}[X]$... wait, is that true? If $f \in \mathbb{Z}[X]$ and $f(p) = 0$, then $X - p$ divides $f$ in $\mathbb{Q}[X]$, so $f(X) = (X-p) q(X)$ with $q(X) \in \mathbb{Q}[X]$. But $q(X)$ might not be in $\mathbb{Z}[X]$. For example, $f(X) = X - p$ itself: $q(X) = 1 \in \mathbb{Z}[X]$, fine. But $f(X) = 2X - 2p = 2(X-p)$: $q(X) = 2 \in \mathbb{Z}[X]$, fine. 

What about $f(X) = pX - p^2 = p(X-p)$? That's in $(X-p)$ in $\mathbb{Z}[X]$ since $p \in \mathbb{Z}$. Fine.

Actually, $(X-p)$ in $\mathbb{Z}[X]$: the ideal generated by $X-p$ in $\mathbb{Z}[X]$ consists of all $(X-p) \cdot q(X)$ where $q(X) \in \mathbb{Z}[X]$. If $f(p) = 0$ and $f \in \mathbb{Z}[X]$, then $f(X) = (X-p)q(X)$ in $\mathbb{Q}[X]$. By Gauss's lemma or direct computation, since $X - p$ is monic, polynomial division of $f$ by $X - p$ in $\mathbb{Z}[X]$ gives $q(X) \in \mathbb{Z}[X]$ (because the leading coefficient of $X-p$ is 1, so the division algorithm works over $\mathbb{Z}$). So yes, for polynomials, the kernel of evaluation at $p$ is exactly $(X-p) \cdot \mathbb{Z}[X]$.

Now for formal power series: if $f(X) = \sum_{n=0}^{\infty} a_n X^n \in \mathbb{Z}[[X]]$ and $\sum a_n p^n = 0$ in $\mathbb{Q}_p$, is $f \in (X-p) \cdot \mathbb{Z}[[X]]$?

We need $f(X) = (X-p) g(X)$ with $g(X) = \sum b_n X^n \in \mathbb{Z}[[X]]$. This gives $a_n = b_{n-1} - p b_n$ (with $b_{-1} = 0$).

So $a_0 = -p b_0$, hence $b_0 = -a_0/p$. For $b_0 \in \mathbb{Z}$, we need $p | a_0$.

But we only know $\sum a_n p^n = 0$ in $\mathbb{Q}_p$, which means $v_p(\sum a_n p^n) = \infty$. This means $a_0 \equiv 0 \pmod{p}$ (since the sum is 0, its $p$-adic valuation is infinite, so $a_0 \equiv 0 \pmod p$). Actually, let me be more careful. $\sum_{n=0}^{\infty} a_n p^n = 0$ means that for every $k$, $\sum_{n=0}^{k-1} a_n p^n \equiv 0 \pmod{p^k}$.

For $k=1$: $a_0 \equiv 0 \pmod{p}$. So $b_0 = -a_0/p \in \mathbb{Z}$. ✓

For $k=2$: $a_0 + a_1 p \equiv 0 \pmod{p^2}$. Since $a_0 = -p b_0$, we have $-p b_0 + a_1 p \equiv 0 \pmod{p^2}$, so $p(-b_0 + a_1) \equiv 0 \pmod{p^2}$, so $-b_0 + a_1 \equiv 0 \pmod{p}$, so $a_1 \equiv b_0 \pmod{p}$. Now $a_1 = b_0 - p b_1$, so $b_1 = (b_0 - a_1)/p$. For $b_1 \in \mathbb{Z}$, we need $p | (b_0 - a_1)$, which is exactly $a_1 \equiv b_0 \pmod{p}$. ✓

By induction, the condition $\sum_{n=0}^{k-1} a_n p^n \equiv 0 \pmod{p^k}$ for all $k$ ensures that all $b_n \in \mathbb{Z}$. So for formal power series (non-negative exponents), the kernel is exactly $(X-p) \cdot \mathbb{Z}[[X]]$.

Now what about formal Laurent series (with possibly negative exponents)? If $f(X) = \sum_{n \geq n_0} a_n X^n$ with $n_0 < 0$, then $f(p) = \sum_{n \geq n_0} a_n p^n$. For this to be 0 in $\mathbb{Q}_p$... 

Let's say $n_0 = -1$. Then $f(X) = a_{-1} X^{-1} + a_0 + a_1 X + \ldots$. We need $f(X) = (X-p) g(X)$ where $g(X) = \sum_{n \geq m} b_n X^n$ for some $m$. 

$(X-p) g(X) = \sum b_n X^{n+1} - \sum p b_n X^n$. The lowest power of $X$ in $(X-p)g(X)$ is $X^{m+1}$ (from the first sum) or $X^m$ (from the second sum, with coefficient $-p b_m$). So the lowest power is $X^m$ with coefficient $-p b_m$ (assuming $m < m+1$, which is always true). 

Wait, actually the lowest power of $X$ in $X \cdot g(X)$ is $X^{m+1}$ and in $p \cdot g(X)$ is $X^m$. So the lowest power in $(X-p)g(X)$ is $X^m$ with coefficient $-p b_m$.

For $f(X)$ with lowest power $X^{n_0}$, we need $m = n_0$ and $-p b_{n_0} = a_{n_0}$. So $b_{n_0} = -a_{n_0}/p$, which requires $p | a_{n_0}$.

But from $f(p) = 0$, we get $a_{n_0} p^{n_0} + a_{n_0+1} p^{n_0+1} + \ldots = 0$, so $p^{n_0}(a_{n_0} + a_{n_0+1} p + \ldots) = 0$, so $a_{n_0} + a_{n_0+1} p + \ldots = 0$ in $\mathbb{Q}_p$. This means $a_{n_0} \equiv 0 \pmod{p}$ (by the same argument as before). So $b_{n_0} \in \mathbb{Z}$. ✓

And by the same inductive argument, all $b_n \in \mathbb{Z}$. So the kernel of the evaluation map $\mathbb{Z}((X)) \to \mathbb{Q}_p$ is exactly $(X-p) \cdot \mathbb{Z}((X))$.

Wait, but this would mean $\mathbb{Z}((X))/(X-p) \cong \mathbb{Q}_p$, and then $\mathbb{Q}_p^{ext} = \mathbb{Q}_p$, which doesn't seem like an "extension".

Hmm, but the problem says $\mathbb{Z}((X))_{conti}$, not $\mathbb{Z}((X))$. The "conti" must be doing something important.

Let me reconsider what "conti" means. I think "conti" might refer to the subring of $\mathbb{Z}((X))$ consisting of series where the coefficient sequence is "continuous" in some profinite sense. 

Actually, I think this might be related to the concept from the theory of "automatic sequences" or "$p$-automatic sequences". A sequence $(a_n)_{n \geq 0}$ with values in a finite set is $p$-automatic if and only if it is $p$-definable, and there's a connection to formal power series over finite fields.

But here the coefficients are in $\mathbb{Z}$, not a finite field. 

Let me think about this differently. Perhaps "conti" refers to the ring of formal Laurent series $\sum a_n X^n$ where the function $n \mapsto a_n$ is continuous with respect to some topology on $\mathbb{Z}$ (the index set) and $\mathbb{Z}$ (the coefficient set).

If we put the $p$-adic topology on the coefficient $\mathbb{Z}$, and some topology on the index set $\mathbb{Z}$, then "continuous" would mean that nearby indices have nearby (mod $p^k$) coefficients.

Actually, I think I recall now. This might be related to the concept of "quasi-morphisms" or the work of Kedlaya on "semistable reduction for $p$-adic curves" or his book "p-adic Differential Equations".

In Kedlaya's work, there's a notion of a "twisted polynomial" and "Robba ring", and the concept of $\mathbb{Z}((X))_{conti}$ might be related to the ring of formal series that converge on some annulus.

Actually, let me try another interpretation. Perhaps $\mathbb{Z}((X))_{conti}$ is the ring of formal series $\sum_{n \geq n_0} a_n X^n \in \mathbb{Z}((X))$ such that the sequence $(a_n)$ is bounded, or such that the series converges for $|X|_p < 1$ (i.e., in the open unit disc in $\mathbb{Q}_p$), or something like that.

If $\mathbb{Z}((X))_{conti}$ is the subring of $\mathbb{Z}((X))$ consisting of series that converge as $p$-adic functions on some domain, then the quotient by $(X-p)$ might give a larger field than $\mathbb{Q}_p$.

Hmm, but $X = p$ has $|p|_p = p^{-1} < 1$, so if the series converges for $|X|_p < 1$, it would converge at $X = p$.

Let me try yet another approach. Maybe the "conti" refers to the $p$-adic continuity of the coefficient sequence, viewed as a function $\mathbb{Z} \to \mathbb{Z}_p$ (with $\mathbb{Z}$ given the profinite topology or the $p$-adic topology).

A sequence $(a_n)_{n \in \mathbb{Z}}$ is $p$-adically continuous if for every $k$, there exists $N$ such that $n \equiv m \pmod{p^N}$ implies $a_n \equiv a_m \pmod{p^k}$.

This is equivalent to saying that the sequence extends to a continuous function $\mathbb{Z}_p \to \mathbb{Z}_p$.

With this interpretation, $\mathbb{Z}((X))_{conti}$ would be the ring of formal Laurent series $\sum_{n \geq n_0} a_n X^n$ where $(a_n)$ is a $p$-adically continuous sequence.

This is a very interesting ring. When we quotient by $(X-p)$, we're essentially evaluating these series at $X = p$, but the "continuous" condition on the coefficients means that the resulting field might be larger than $\mathbb{Q}_p$.

Actually, I think this is related to the concept of the "field of norms" (corps des normes) in the theory of $p$-adic fields, or to the construction of the "tilt" in perfectoid theory.

Let me think about what elements of $\mathbb{Z}((X))_{conti}/(X-p)$ look like. An element is represented by a series $\sum_{n \geq n_0} a_n X^n$ where $(a_n)$ is $p$-adically continuous, and we evaluate at $X = p$.

The $p$-adic continuity of $(a_n)$ means that $a_n$ depends "continuously" on $n$ in the $p$-adic sense. So for $n$ close to $n_0$ $p$-adically, $a_n$ is close to $a_{n_0}$.

Now, the key question is: does this give a field extension of $\mathbb{Q}_p$, and if so, what is the degree of its algebraic closure over it?

Actually, I think I need to reconsider the problem from scratch. Let me think about what $\mathbb{Q}_p^{ext}$ means — the "ext" suggests it's an extension of $\mathbb{Q}_p$.

If $\mathbb{Z}((X))_{conti}$ is larger than $\mathbb{Z}((X))$... no, it's a subring. So the quotient $\mathbb{Z}((X))_{conti}/(X-p)$ would be a quotient of a subring, which maps to $\mathbb{Q}_p$ (since $\mathbb{Z}((X))_{conti} \subset \mathbb{Z}((X))$ and $\mathbb{Z}((X))/(X-p) \cong \mathbb{Q}_p$). So $\mathbb{Q}_p^{ext}$ would be a subfield of $\mathbb{Q}_p$? That doesn't make sense with the name "ext".

Wait, maybe I have the inclusion backwards. Maybe $\mathbb{Z}((X))_{conti}$ is LARGER than $\mathbb{Z}((X))$, not smaller. Perhaps it allows more general coefficient sequences.

Actually, $\mathbb{Z}((X))$ already allows arbitrary sequences of integers as coefficients. So $\mathbb{Z}((X))_{conti}$ as a subring would be smaller. But then the quotient would be smaller than $\mathbb{Q}_p$.

Unless... the quotient $\mathbb{Z}((X))_{conti}/(X-p)$ is not the image in $\mathbb{Q}_p$ but rather a different construction. Maybe the ideal $(X-p)$ in $\mathbb{Z}((X))_{conti}$ is different from the intersection $(X-p)\mathbb{Z}((X)) \cap \mathbb{Z}((X))_{conti}$.

Hmm, this is getting complicated. Let me try to think about this from a different angle.

Actually, maybe the "conti" subscript means something completely different. Perhaps $\mathbb{Z}((X))_{conti}$ is the ring of "continuous" formal Laurent series, meaning series $\sum a_n X^n$ where $a_n \in \mathbb{Z}$ and the series represents a continuous function on some $p$-adic space.

Or perhaps this is the ring of formal series $\sum a_n X^n$ where $a_n \in \mathbb{Z}_p$ (the $p$-adic integers) rather than $\mathbb{Z}$, and "conti" refers to the $p$-adic continuity. But then it would be $\mathbb{Z}_p((X))$, not $\mathbb{Z}((X))_{conti}$.

Let me try to search my memory for this specific construction. I think this might be related to the work of Fesenko or others on "explicit local class field theory" or the theory of "higher local fields".

A higher local field is a field like $\mathbb{Q}_p((X))$ or $\mathbb{F}_p((X))((Y))$, which has multiple topologies. But $\mathbb{Z}((X))_{conti}/(X-p)$ doesn't quite fit this pattern.

Actually, wait. Let me reconsider. Maybe the problem is using notation from a specific textbook or paper, and $\mathbb{Z}((X))_{conti}$ has a precise meaning in that context.

Let me consider the possibility that this is the ring of formal series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$, where the series is "continuous" in the sense that it converges in the $X$-adic topology AND the $p$-adic topology simultaneously, i.e., it's an element of the completion of $\mathbb{Z}[X, X^{-1}]$ with respect to the ideal $(p, X)$.

The $(p,X)$-adic completion of $\mathbb{Z}[X, X^{-1}]$ would be... hmm, this is getting complicated.

Let me try yet another interpretation. In the theory of $p$-adic fields, there's a construction where you take $\mathbb{Z}((X))$ and complete it with respect to a topology that combines the $X$-adic and $p$-adic topologies. The result might be a ring where the quotient by $(X-p)$ gives a field larger than $\mathbb{Q}_p$.

Actually, I think I might be overthinking this. Let me consider the possibility that the answer is simply that the degree is infinite, or more specifically, that the algebraic closure has countably infinite degree, or that the degree is $p^n$ for some $n$, or something like that.

Let me think about what properties $\mathbb{Q}_p^{ext}$ would have.

If $\mathbb{Q}_p^{ext}$ is a field extension of $\mathbb{Q}_p$ that is "large enough" to contain all algebraic elements over $\mathbb{Q}_p$, then the algebraic closure over $\mathbb{Q}_p^{ext}$ would have degree 1. But that seems too simple.

If $\mathbb{Q}_p^{ext}$ is strictly between $\mathbb{Q}_p$ and $\overline{\mathbb{Q}_p}$, then the degree of $\overline{\mathbb{Q}_p}$ over $\mathbb{Q}_p^{ext}$ would be infinite (since $\overline{\mathbb{Q}_p}$ has infinite degree over $\mathbb{Q}_p$, and removing finitely many algebraic extensions wouldn't make it finite).

Actually, for any intermediate field $\mathbb{Q}_p \subset K \subset \overline{\mathbb{Q}_p}$ with $K \neq \overline{\mathbb{Q}_p}$, the degree $[\overline{\mathbb{Q}_p} : K]$ is infinite. This is because $\overline{\mathbb{Q}_p}$ has infinite degree over $\mathbb{Q}_p$, and if $[K:\mathbb{Q}_p]$ is finite, then $[\overline{\mathbb{Q}_p}:K] = [\overline{\mathbb{Q}_p}:\mathbb{Q}_p]/[K:\mathbb{Q}_p]$ is still infinite. If $[K:\mathbb{Q}_p]$ is infinite, then $[\overline{\mathbb{Q}_p}:K]$ could be finite or infinite.

Hmm, but actually, for algebraically closed fields, if $K$ is an intermediate field between $\mathbb{Q}_p$ and $\overline{\mathbb{Q}_p}$, then $[\overline{\mathbb{Q}_p}:K]$ is either 1 (if $K = \overline{\mathbb{Q}_p}$) or infinite. This is because if $[\overline{\mathbb{Q}_p}:K] = n < \infty$, then $\overline{\mathbb{Q}_p}$ is a finite extension of $K$, but $\overline{\mathbb{Q}_p}$ is algebraically closed, so $K$ must also be algebraically closed (a finite extension of a non-algebraically-closed field cannot be algebraically closed... actually, that's not quite right).

Wait, actually, if $L/K$ is a finite extension and $L$ is algebraically closed, then $K$ is real closed (by the Artin-Schreier theorem). So if $\overline{\mathbb{Q}_p}$ is algebraically closed (which it is, being the algebraic closure of $\mathbb{Q}_p$) and $[\overline{\mathbb{Q}_p}:K] < \infty$, then $K$ is real closed. But $\mathbb{Q}_p$ is not formally real (since $-1$ is a sum of squares in $\mathbb{Q}_p$ for $p > 2$... actually, $\mathbb{Q}_p$ contains $\sqrt{-1}$ for $p \equiv 1 \pmod 4$). More importantly, a real closed field must be formally real, but $\mathbb{Q}_p$ is not formally real (it contains a square root of $-1$ for $p \equiv 1 \pmod 4$, and for $p \equiv 3 \pmod 4$, $-1$ is not a square but $\mathbb{Q}_p$ is still not formally real because... hmm, actually $\mathbb{Q}_p$ might be formally real for some $p$).

Wait, $\mathbb{Q}_p$ is formally real if and only if $-1$ is not a sum of squares. In $\mathbb{Q}_p$, $-1$ is a sum of squares if and only if... by the theory of quadratic forms over $\mathbb{Q}_p$, every element of $\mathbb{Q}_p$ is a sum of at most 4 squares (for $p$ odd). Actually, $-1$ is a sum of squares in $\mathbb{Q}_p$ for all primes $p$. For $p = 2$: $-1 = 1 + 1 + 1 + (-4) = ...$, hmm, let me think. In $\mathbb{Q}_2$, $-1$ is not a square but is it a sum of squares? $-1 \equiv 7 \pmod 8$, and by the theory, $-1$ is a sum of 4 squares in $\mathbb{Q}_2$. For odd $p$: $-1$ is a sum of 2 squares in $\mathbb{Q}_p$ iff $-1$ is a square mod $p$ (for $p \equiv 1 \pmod 4$) or... actually, by Chevalley-Warning, every element of $\mathbb{Q}_p$ is a sum of 2 squares for $p \equiv 1 \pmod 4$, and for $p \equiv 3 \pmod 4$, $-1$ is a sum of 2 squares iff... hmm, I'm getting confused.

The point is: $\mathbb{Q}_p$ is NOT formally real (for any $p$, $-1$ is a sum of squares in $\mathbb{Q}_p$). This is because $\mathbb{Q}_p$ has finite extensions of every degree, and in particular, it's not real closed. A formally real field can be ordered, but $\mathbb{Q}_p$ cannot be ordered (since it has torsion in its multiplicative group structure, or more directly, since $p$-adic fields have the property that $-1$ is a sum of squares).

Actually, the simplest argument: $\mathbb{Q}_p$ has a finite extension of degree 2 (e.g., $\mathbb{Q}_p(\sqrt{p})$ for $p$ odd, or $\mathbb{Q}_2(\sqrt{2})$). If $\mathbb{Q}_p$ were formally real, its algebraic closure would be $\mathbb{Q}_p(i)$, a degree 2 extension. But $\overline{\mathbb{Q}_p}$ has infinite degree over $\mathbb{Q}_p$, so $\mathbb{Q}_p$ is not formally real.

OK so by Artin-Schreier, if $[\overline{\mathbb{Q}_p} : K] < \infty$ and $\overline{\mathbb{Q}_p}$ is algebraically closed, then $K$ is real closed, hence formally real. But $K$ contains $\mathbb{Q}_p$ which is not formally real, so $K$ is not formally real. Contradiction. Therefore $[\overline{\mathbb{Q}_p} : K] = \infty$ for any $K$ with $\mathbb{Q}_p \subseteq K \subsetneq \overline{\mathbb{Q}_p}$.

But wait, what if $\mathbb{Q}_p^{ext}$ is NOT contained in $\overline{\mathbb{Q}_p}$? If $\mathbb{Q}_p^{ext}$ is a transcendental extension of $\mathbb{Q}_p$, then the algebraic closure of $\mathbb{Q}_p^{ext}$ would be a different thing.

Hmm, the problem asks for "the degree of extension of the algebraic closure over $\mathbb{Q}_p^{ext}$". If $\mathbb{Q}_p^{ext}$ is a transcendental extension of $\mathbb{Q}_p$, then its algebraic closure $\overline{\mathbb{Q}_p^{ext}}$ would have infinite degree over $\mathbb{Q}_p^{ext}$ (since even $\overline{\mathbb{Q}(t)}$ has infinite degree over $\mathbb{Q}(t)$).

But actually, for any field $K$ that is not algebraically closed, $[\overline{K}:K]$ is either infinite or 2 (by Artin-Schreier: if $[\overline{K}:K] < \infty$, then $K$ is real closed and $[\overline{K}:K] = 2$).

So the answer is either 1 (if $\mathbb{Q}_p^{ext}$ is algebraically closed), 2 (if $\mathbb{Q}_p^{ext}$ is real closed), or infinite.

Now, $\mathbb{Q}_p^{ext}$ contains $\mathbb{Q}_p$, which is not formally real. So $\mathbb{Q}_p^{ext}$ is not formally real (since it contains a non-formally-real field). Therefore $\mathbb{Q}_p^{ext}$ is not real closed. So the degree is either 1 or infinite.

The question is: is $\mathbb{Q}_p^{ext}$ algebraically closed?

If $\mathbb{Q}_p^{ext}$ is algebraically closed, the degree is 1. If not, the degree is infinite.

Now, the name "$\mathbb{Q}_p^{ext}$" and the construction suggest that it might be an extension of $\mathbb{Q}_p$ that is "large" in some sense. If it's large enough to be algebraically closed, the answer would be 1. If it's a proper subfield of $\overline{\mathbb{Q}_p}$ or a transcendental extension, the answer would be infinite.

Let me think about this more carefully. The construction $\mathbb{Z}((X))_{conti}/(X-p)$ — if "conti" means that the coefficient sequences are $p$-adically continuous, then this is a very rich ring, and the quotient might indeed be algebraically closed or close to it.

Actually, let me think about this from the perspective of the "field of norms" theory. In the theory of $p$-adic fields, the field of norms (corps des normes) of the cyclotomic $\mathbb{Z}_p$-extension of $\mathbb{Q}_p$ is $\mathbb{F}_p((X))$. This is related to the "tilt" construction in perfectoid theory.

But here we have $\mathbb{Z}((X))$ instead of $\mathbb{F}_p((X))$, and we're quotienting by $(X-p)$ instead of working in characteristic $p$.

Hmm, let me think about this differently. Perhaps the "conti" condition is what makes the quotient a field that is "maximal" or "spherically complete" in some sense.

Actually, I think I should consider the possibility that this construction gives a field that is isomorphic to $\mathbb{C}_p$ (the completion of $\overline{\mathbb{Q}_p}$). If $\mathbb{Q}_p^{ext} \cong \mathbb{C}_p$, then since $\mathbb{C}_p$ is algebraically closed, the degree of the algebraic closure over it would be 1.

But $\mathbb{C}_p$ is the completion of $\overline{\mathbb{Q}_p}$, and it's algebraically closed (by Krasner's lemma, the completion of an algebraically closed non-archimedean field is algebraically closed). So if $\mathbb{Q}_p^{ext} = \mathbb{C}_p$, the answer is 1.

Alternatively, maybe $\mathbb{Q}_p^{ext}$ is some other algebraically closed field containing $\mathbb{Q}_p$.

Let me think about what the "conti" condition gives us. If $\mathbb{Z}((X))_{conti}$ is the ring of formal Laurent series with $p$-adically continuous coefficient sequences, then when we evaluate at $X = p$, we get elements of $\mathbb{Q}_p$ that are "more general" than just $p$-adic expansions with digits in $\{0, \ldots, p-1\}$.

Wait, but I showed earlier that $\mathbb{Z}((X))/(X-p) \cong \mathbb{Q}_p$, and $\mathbb{Z}((X))_{conti} \subset \mathbb{Z}((X))$, so the image of $\mathbb{Z}((X))_{conti}$ in $\mathbb{Q}_p$ is a subring of $\mathbb{Q}_p$. This would make $\mathbb{Q}_p^{ext}$ a subfield of $\mathbb{Q}_p$, not an extension.

Unless the "conti" condition allows coefficients that are not just integers but $p$-adic integers, or something more general.

OK, I think I need to reconsider the problem. Let me consider the possibility that $\mathbb{Z}((X))_{conti}$ is NOT a subring of $\mathbb{Z}((X))$ but rather a LARGER ring.

Perhaps $\mathbb{Z}((X))_{conti}$ is the ring of formal series $\sum_{n \geq n_0} a_n X^n$ where $a_n \in \mathbb{Z}_p$ (not just $\mathbb{Z}$) and the sequence $(a_n)$ is continuous in some sense. Or perhaps it's the ring of series with $a_n \in \mathbb{Z}$ but with a different notion of "formal series" that allows more general index sets.

Actually, I just realized something. Maybe "conti" refers to the ring of "continuous functions" from $\mathbb{Z}_p$ to $\mathbb{Z}_p$ (or $\mathbb{Q}_p$), represented as formal series. A continuous function $f: \mathbb{Z}_p \to \mathbb{Z}_p$ can be written as $f(X) = \sum_{n=0}^{\infty} a_n \binom{X}{n}$ (Mahler expansion) where $a_n \to 0$ in $\mathbb{Z}_p$. But this is different from a formal Laurent series.

Alternatively, maybe $\mathbb{Z}((X))_{conti}$ is the ring of formal series $\sum a_n X^n$ that converge $p$-adically for $X$ in some domain, and the "conti" refers to the continuity of the resulting function.

I think I'm going in circles. Let me try to approach this problem from the answer side.

The problem asks to "determine the degree of extension of the algebraic closure over $\mathbb{Q}_p^{ext}$". The possible answers are:
1. Degree 1 (if $\mathbb{Q}_p^{ext}$ is algebraically closed)
2. Degree 2 (if $\mathbb{Q}_p^{ext}$ is real closed — but this is impossible since it contains $\mathbb{Q}_p$)
3. Infinite degree

Given the construction and the name "ext" (extension), I think the most likely intended answer is that $\mathbb{Q}_p^{ext}$ is algebraically closed, so the degree is 1.

But let me think about why this might be the case.

Actually, let me reconsider the construction. Perhaps $\mathbb{Z}((X))_{conti}$ is not a subring of $\mathbb{Z}((X))$ but rather a completion or enlargement.

One possibility: $\mathbb{Z}((X))_{conti}$ is the $(p,X)$-adic completion of $\mathbb{Z}[X, X^{-1}]$. This would be the ring of formal series $\sum_{n \geq n_0} a_n X^n$ where $a_n \in \mathbb{Z}$ and $a_n \to 0$ as $n \to \infty$ in the $p$-adic topology (i.e., $v_p(a_n) \to \infty$). Wait, that doesn't make sense either because in $\mathbb{Z}((X))$, the coefficients are already in $\mathbb{Z}$ and don't need to tend to 0.

Hmm, let me think about the $(p,X)$-adic topology. In the $(p,X)$-adic topology on $\mathbb{Z}[[X]]$, a sequence converges if it converges both $p$-adically and $X$-adically. The completion of $\mathbb{Z}[[X]]$ with respect to the $(p,X)$-adic topology is $\mathbb{Z}[[X]]$ itself (since $\mathbb{Z}[[X]]$ is already complete with respect to the $X$-adic topology, and adding the $p$-adic condition...).

Actually, the $(p,X)$-adic completion of $\mathbb{Z}[X]$ is $\mathbb{Z}_p[[X]]$ (the ring of formal power series with $p$-adic integer coefficients). This is because completing with respect to $(p,X)$ means we allow both $p$-adic limits and $X$-adic limits.

Similarly, the $(p,X)$-adic completion of $\mathbb{Z}[X, X^{-1}]$ or $\mathbb{Z}((X))$ might be $\mathbb{Z}_p((X))$ (formal Laurent series with $p$-adic integer coefficients) or something like that.

If $\mathbb{Z}((X))_{conti} = \mathbb{Z}_p((X))$, then $\mathbb{Z}_p((X))/(X-p)$... 

In $\mathbb{Z}_p((X))$, $X - p$ generates an ideal. The quotient $\mathbb{Z}_p((X))/(X-p)$: setting $X = p$ in a formal Laurent series with $\mathbb{Z}_p$-coefficients gives a $\mathbb{Q}_p$-valued series. Since $\mathbb{Z}_p \supset \mathbb{Z}$, this gives a potentially larger field than $\mathbb{Q}_p$.

Actually, $\mathbb{Z}_p((X))/(X-p)$: an element is $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}_p$, evaluated at $X = p$, giving $\sum_{n \geq n_0} a_n p^n \in \mathbb{Q}_p$. But every element of $\mathbb{Q}_p$ can be written this way (using $p$-adic expansion with digits in $\{0, \ldots, p-1\} \subset \mathbb{Z}_p$). So $\mathbb{Z}_p((X))/(X-p) \cong \mathbb{Q}_p$ as well.

Hmm, so even with $\mathbb{Z}_p$ coefficients, we get $\mathbb{Q}_p$. The "conti" must mean something else.

Let me try another interpretation. Maybe $\mathbb{Z}((X))_{conti}$ is the ring of formal series $\sum_{n \in \mathbb{Z}} a_n X^n$ (bi-infinite series, not just bounded below) where the sequence $(a_n)$ is "continuous" in some sense. Bi-infinite formal Laurent series don't usually make sense, but with a continuity condition, they might.

If we allow bi-infinite series $\sum_{n \in \mathbb{Z}} a_n X^n$ with $a_n \in \mathbb{Z}$, subject to some continuity/boundedness condition, then evaluating at $X = p$ gives $\sum_{n \in \mathbb{Z}} a_n p^n$, which might not converge in $\mathbb{Q}_p$ (since the terms with $n \to -\infty$ have $|a_n p^n|_p = |a_n|_p \cdot p^{-n} \to \infty$).

But if we impose that $a_n \to 0$ $p$-adically as $n \to -\infty$ fast enough, the series might converge. Specifically, if $v_p(a_n) \geq -n + C$ for some constant $C$ and all $n \ll 0$, then $|a_n p^n|_p \leq p^{-C}$ and the series might converge.

Actually, for the series $\sum_{n \in \mathbb{Z}} a_n p^n$ to converge in $\mathbb{Q}_p$, we need $|a_n p^n|_p \to 0$ as $n \to +\infty$ (which is automatic since $|p^n|_p \to 0$) and the partial sums to converge as $n \to -\infty$ as well. For the negative direction, we need the "tail" $\sum_{n \leq N} a_n p^n$ to converge as $N \to -\infty$, which requires $|a_n p^n|_p \to 0$ as $n \to -\infty$, i.e., $|a_n|_p \cdot p^{-n} \to 0$, i.e., $v_p(a_n) + n \to +\infty$ as $n \to -\infty$, i.e., $v_p(a_n) \to +\infty$ as $n \to -\infty$ (since $n \to -\infty$, we need $v_p(a_n)$ to grow faster than $|n|$).

This is a very strong condition. With this condition, the bi-infinite series would give elements of $\mathbb{Q}_p$, but potentially "more" elements than just $\mathbb{Q}_p$... no, they'd still be in $\mathbb{Q}_p$ since the series converges in $\mathbb{Q}_p$.

I'm stuck on the interpretation. Let me try to think about this from a higher level.

The problem is asking about a specific construction that gives a field $\mathbb{Q}_p^{ext}$, and asks for the degree of its algebraic closure over it. The answer should be a specific number or "infinite".

Given the constraints of the problem (it seems to be a well-posed problem with a definite answer), and given that:
- The degree can't be 2 (since $\mathbb{Q}_p^{ext}$ contains $\mathbb{Q}_p$ which is not formally real)
- The degree is either 1 or infinite

I think the answer is likely **infinite**, meaning $\mathbb{Q}_p^{ext}$ is not algebraically closed.

But wait, maybe I should reconsider. Perhaps the construction is designed to give an algebraically closed field, and the answer is 1.

Actually, let me reconsider the problem statement. It says "the degree of extension of the algebraic closure over the field $\mathbb{Q}_p^{ext}$". This could mean $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$.

If $\mathbb{Q}_p^{ext}$ is algebraically closed, this is 1.
If $\mathbb{Q}_p^{ext}$ is not algebraically closed (and not real closed), this is infinite.

Hmm, let me think about this more carefully. The construction $\mathbb{Z}((X))_{conti}/(X-p)$ with the "conti" condition is reminiscent of constructions in the theory of "perfectoid spaces" or "tilting", where one constructs characteristic 0 fields from characteristic $p$ fields or vice versa.

In perfectoid theory, the tilt of $\mathbb{Q}_p(\mu_{p^\infty})$ is $\mathbb{F}_p((t^{1/p^\infty}))$. But this is in characteristic $p$, not characteristic 0.

Let me try a completely different approach. Maybe the "conti" refers to the ring of formal series that are "continuous" as functions on the $p$-adic integers, i.e., the ring of series $\sum a_n X^n$ that converge and define continuous functions $\mathbb{Z}_p \to \mathbb{Q}_p$.

A formal power series $\sum_{n=0}^{\infty} a_n X^n$ with $a_n \in \mathbb{Z}$ converges on $\mathbb{Z}_p$ if and only if $|a_n|_p \cdot |X^n|_p \to 0$ for all $X \in \mathbb{Z}_p$, which is equivalent to $|a_n|_p \to 0$ (since $|X|_p \leq 1$ on $\mathbb{Z}_p$). Since $a_n \in \mathbb{Z}$, $|a_n|_p \leq 1$, and $|a_n|_p \to 0$ means $v_p(a_n) \to \infty$, i.e., $p^k | a_n$ for large $n$.

So $\mathbb{Z}[[X]]_{conti}$ would be the ring of series $\sum a_n X^n$ with $a_n \in \mathbb{Z}$ and $v_p(a_n) \to \infty$. This is the same as the $(p,X)$-adic completion of $\mathbb{Z}[X]$, which is $\mathbb{Z}_p[[X]]$... no, it's the subring of $\mathbb{Z}[[X]]$ where $v_p(a_n) \to \infty$.

Actually, this ring is the same as the completion of $\mathbb{Z}[X]$ with respect to the ideal $(p, X)$, which is the ring of formal power series $\sum a_n X^n$ with $a_n \in \mathbb{Z}$ and $a_n \to 0$ $p$-adically. This is indeed a subring of $\mathbb{Z}[[X]]$.

For formal Laurent series, $\mathbb{Z}((X))_{conti}$ would be the ring of series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$ and $v_p(a_n) \to \infty$ as $n \to \infty$.

Now, the quotient $\mathbb{Z}((X))_{conti}/(X-p)$: we evaluate at $X = p$, getting $\sum_{n \geq n_0} a_n p^n$ where $v_p(a_n) \to \infty$. Since $v_p(a_n p^n) = v_p(a_n) + n \to \infty$, the series converges in $\mathbb{Q}_p$. But the image is still in $\mathbb{Q}_p$, so the quotient is a subring of $\mathbb{Q}_p$.

Hmm, but is the quotient a field? And is it all of $\mathbb{Q}_p$ or a proper subring?

Every $p$-adic integer $z \in \mathbb{Z}_p$ has a $p$-adic expansion $z = \sum_{n=0}^{\infty} c_n p^n$ with $c_n \in \{0, \ldots, p-1\}$. The corresponding formal series $\sum c_n X^n$ has $v_p(c_n) = 0$ for infinitely many $n$ (unless $z = 0$), so $v_p(c_n) \not\to \infty$. So this series is NOT in $\mathbb{Z}[[X]]_{conti}$ (unless $z = 0$).

This means that most $p$-adic integers are NOT in the image of $\mathbb{Z}((X))_{conti}$ under evaluation at $X = p$. So the quotient $\mathbb{Z}((X))_{conti}/(X-p)$ is a proper subring of $\mathbb{Q}_p$.

But the problem says $\mathbb{Q}_p^{ext}$, suggesting it's an extension of $\mathbb{Q}_p$, not a subfield. So maybe my interpretation of "conti" is wrong.

Let me try the opposite: maybe "conti" means the series are continuous in the $X$-adic sense, which is the standard formal Laurent series, and the "ext" refers to the fact that the quotient gives an extension of $\mathbb{Q}_p$ because we're using a different ring.

Actually, wait. Maybe I had the inclusion backwards. Let me reconsider.

If $\mathbb{Z}((X))_{conti}$ is the ring of series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}_p$ (not $\mathbb{Z}$) and some continuity condition, then this is LARGER than $\mathbb{Z}((X))$ (since $\mathbb{Z} \subset \mathbb{Z}_p$), and the quotient by $(X-p)$ could give a field larger than $\mathbb{Q}_p$.

But as I computed earlier, $\mathbb{Z}_p((X))/(X-p) \cong \mathbb{Q}_p$ as well, since every $p$-adic number has a $p$-adic expansion with coefficients in $\{0, \ldots, p-1\} \subset \mathbb{Z}_p$.

Hmm, unless the "continuity" condition allows for even more general coefficients, like elements of $\overline{\mathbb{Q}_p}$ or $\mathbb{C}_p$.

OK, I think I need to take a step back and consider the possibility that this problem is from a specific context that I'm not fully recalling. Let me consider the most natural interpretation and try to give the best answer I can.

Given the construction $\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p)$, and the fact that:

1. The name suggests it's an extension of $\mathbb{Q}_p$
2. The "conti" condition on the coefficient sequence suggests some kind of $p$-adic continuity
3. The question asks for the degree of the algebraic closure over this field

I think the most likely answer is that the degree is **infinite**. Here's my reasoning:

If $\mathbb{Q}_p^{ext}$ is a field extension of $\mathbb{Q}_p$ (possibly transcendental), then:
- If it's algebraic over $\mathbb{Q}_p$ and not algebraically closed, then $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = [\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}]$ is infinite (by the Artin-Schreier argument, since $\mathbb{Q}_p^{ext}$ is not formally real).
- If it's transcendental over $\mathbb{Q}_p$, then $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$ is also infinite (since the algebraic closure of a transcendental extension has infinite degree).

In either case, the answer is infinite, UNLESS $\mathbb{Q}_p^{ext}$ is algebraically closed.

Now, is $\mathbb{Q}_p^{ext}$ algebraically closed? For the construction to yield an algebraically closed field, the "conti" condition would need to be very special. I don't see an obvious reason why this construction would give an algebraically closed field.

Actually, wait. Let me reconsider. Maybe the construction is designed to give $\mathbb{C}_p$ (the completion of $\overline{\mathbb{Q}_p}$), which is algebraically closed.

$\mathbb{C}_p$ is the completion of $\overline{\mathbb{Q}_p}$ with respect to the $p$-adic absolute value. It is algebraically closed (by Krasner's lemma). If $\mathbb{Q}_p^{ext} = \mathbb{C}_p$, then the degree of the algebraic closure over it is 1.

But how would the construction $\mathbb{Z}((X))_{conti}/(X-p)$ give $\mathbb{C}_p$? 

If "conti" means that the coefficients $a_n$ are in $\overline{\mathbb{Q}_p}$ (or $\mathbb{C}_p$) and the sequence is "continuous" in some sense, then evaluating at $X = p$ could give elements of $\mathbb{C}_p$.

Actually, I think there might be a connection to the concept of "perfectoid" fields. In perfectoid theory, one considers the tilt $\mathbb{Q}_p^{cyc,\flat}$ which is a perfectoid field of characteristic $p$. The untilt gives back a characteristic 0 field. But I'm not sure this directly relates to the given construction.

Let me try yet another approach. Let me consider the possibility that the answer is simply $\infty$ (infinite degree), and try to justify it.

Claim: $\mathbb{Q}_p^{ext}$ is not algebraically closed, and therefore $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$.

Justification: 
- $\mathbb{Q}_p^{ext}$ is a field containing $\mathbb{Q}_p$.
- $\mathbb{Q}_p^{ext}$ is not formally real (since it contains $\mathbb{Q}_p$ which is not formally real).
- By the Artin-Schreier theorem, if $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] < \infty$, then $\mathbb{Q}_p^{ext}$ is real closed, hence formally real. Contradiction.
- Therefore $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$ (assuming $\mathbb{Q}_p^{ext}$ is not algebraically closed).

But I still need to argue that $\mathbb{Q}_p^{ext}$ is not algebraically closed. 

Hmm, actually, if $\mathbb{Q}_p^{ext}$ IS algebraically closed, then $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = 1$, and the Artin-Schreier argument doesn't apply (since the degree is finite but equals 1, which is the trivial case).

So the key question remains: is $\mathbb{Q}_p^{ext}$ algebraically closed?

Let me think about this from the construction. $\mathbb{Z}((X))_{conti}/(X-p)$ is a quotient of a ring of formal series by a principal ideal. For this to be algebraically closed, the ring would need to be very special.

Actually, I just thought of something. In the theory of formal Laurent series, the field $\mathbb{C}((X))$ (where $\mathbb{C}$ is algebraically closed of characteristic 0) has the property that its algebraic closure is the field of Puiseux series $\bigcup_{n \geq 1} \mathbb{C}((X^{1/n}))$, which has infinite degree over $\mathbb{C}((X))$. But $\mathbb{C}((X))$ is not algebraically closed.

Similarly, $\mathbb{Q}_p((X))$ is not algebraically closed, and its algebraic closure has infinite degree.

But $\mathbb{Q}_p^{ext}$ is not $\mathbb{Q}_p((X))$; it's a quotient of a subring (or super-ring) of $\mathbb{Z}((X))$ by $(X-p)$.

OK let me try to think about what specific property the "conti" condition gives.

I think the key insight might be this: the "conti" condition on the coefficient sequence $(a_n)$ means that the sequence is determined by a continuous function $\mathbb{Z}_p \to \mathbb{Z}_p$ (or $\mathbb{Z}_p \to \mathbb{Z}$). When we evaluate at $X = p$, we're essentially composing this continuous function with the $p$-adic expansion, giving us a "rich" field.

But I'm not sure this leads to algebraic closure.

Let me try a completely different approach. Maybe the problem is asking about a well-known result, and the answer is that the degree is countably infinite, or $2^{\aleph_0}$, or something like that.

Actually, for $\mathbb{Q}_p$, the algebraic closure $\overline{\mathbb{Q}_p}$ has countable dimension over $\mathbb{Q}_p$ (since $\mathbb{Q}_p$ is a complete discretely valued field with finite residue field, and by Krasner's lemma, there are only finitely many extensions of each degree, so the algebraic closure is a countable union of finite extensions). So $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = \aleph_0$.

If $\mathbb{Q}_p^{ext}$ is an intermediate field between $\mathbb{Q}_p$ and $\overline{\mathbb{Q}_p}$, then $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}]$ divides... no, it doesn't necessarily divide, but $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = [\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}] \cdot [\mathbb{Q}_p^{ext} : \mathbb{Q}_p]$ (as cardinals). If $[\mathbb{Q}_p^{ext} : \mathbb{Q}_p]$ is finite, then $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}] = \aleph_0$. If $[\mathbb{Q}_p^{ext} : \mathbb{Q}_p] = \aleph_0$, then $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}]$ could be finite or $\aleph_0$.

But by the Artin-Schreier argument, $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}]$ can't be a finite number greater than 1 (since $\mathbb{Q}_p^{ext}$ is not formally real). So it's either 1 or $\aleph_0$ (or uncountable, if $\mathbb{Q}_p^{ext}$ is not contained in $\overline{\mathbb{Q}_p}$).

If $\mathbb{Q}_p^{ext}$ is a transcendental extension of $\mathbb{Q}_p$, then $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$ is uncountable (since the transcendence degree adds uncountably many algebraically independent elements, and the algebraic closure has uncountable degree).

Hmm, I think I need to just go with my best guess. Let me consider the most likely scenarios:

1. If $\mathbb{Q}_p^{ext}$ is algebraically closed: degree = 1
2. If $\mathbb{Q}_p^{ext}$ is not algebraically closed: degree = infinite

Given the construction and the name "ext", I think the problem might be designed so that $\mathbb{Q}_p^{ext}$ is NOT algebraically closed, and the answer is **infinite**.

But actually, let me reconsider. The construction $\mathbb{Z}((X))_{conti}/(X-p)$ might be designed to produce a field that is "maximal" in some sense, perhaps even algebraically closed or spherically complete.

Actually, I just thought of something. The field $\mathbb{C}_p$ (completion of $\overline{\mathbb{Q}_p}$) is both complete and algebraically closed. If the "conti" condition is strong enough to force completeness, then $\mathbb{Q}_p^{ext}$ might be $\mathbb{C}_p$ or something similar, and the answer would be 1.

But I don't think the quotient of a ring of formal series by a principal ideal would typically give a complete field.

Let me try to think about this more concretely. Consider the polynomial $T^2 - a$ where $a \in \mathbb{Q}_p^{ext}$ is not a square. Does this polynomial have a root in $\mathbb{Q}_p^{ext}$?

If $\mathbb{Q}_p^{ext}$ is constructed from formal Laurent series with continuous coefficients, then solving $T^2 = a$ in $\mathbb{Q}_p^{ext}$ amounts to finding a formal Laurent series $T(X) = \sum b_n X^n$ with continuous coefficients such that $T(X)^2 \equiv a(X) \pmod{X-p}$, i.e., $T(p)^2 = a(p)$ in $\mathbb{Q}_p$ (or whatever the target field is).

If $a(p)$ has a square root in the target field, then we can find $T(p)$, but we also need $T(X)$ to have continuous coefficients, which is an additional constraint.

This is getting very complicated without knowing the exact definition of "conti". 

Let me just go with the answer that the degree is **infinite**, based on the following reasoning:

1. $\mathbb{Q}_p^{ext}$ is a field of characteristic 0 containing $\mathbb{Q}_p$.
2. $\mathbb{Q}_p^{ext}$ is not formally real (since it contains $\mathbb{Q}_p$).
3. By Artin-Schreier, if $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$ is finite, it must be 1 (algebraically closed) or 2 (real closed). Since $\mathbb{Q}_p^{ext}$ is not formally real, it can't be real closed, so the only finite possibility is 1.
4. I claim $\mathbb{Q}_p^{ext}$ is not algebraically closed. (This needs justification.)
5. Therefore $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$.

For step 4, I would argue that the construction $\mathbb{Z}((X))_{conti}/(X-p)$ does not produce an algebraically closed field, because the "conti" condition, while restrictive, does not guarantee that all algebraic equations are solvable within the field.

Actually, hmm, I realize I should think about this more carefully. Let me consider whether the problem might have a specific finite answer.

Wait, the problem says "determine the degree of extension of the algebraic closure over the field $\mathbb{Q}_p^{ext}$". If the answer is infinite, the problem would typically say "show that the degree is infinite" rather than "determine the degree". The phrasing "determine the degree" suggests a specific numerical answer.

But the only possible finite answers are 1 and 2, and 2 is ruled out. So if the answer is finite, it must be 1.

Hmm, but "determine the degree" could also have the answer "infinite" or "countably infinite" or "uncountably infinite".

Let me reconsider. Maybe the answer is 1, meaning $\mathbb{Q}_p^{ext}$ is algebraically closed.

Why might $\mathbb{Q}_p^{ext}$ be algebraically closed? If the "conti" condition is strong enough, the field might contain all algebraic extensions of $\mathbb{Q}_p$.

Actually, I think I recall something now. There's a construction in $p$-adic Hodge theory where one considers the ring $\mathbb{A}_{inf}$ and its fraction field, which is related to $\mathbb{Z}((X))$ type constructions. The field of fractions of $\mathbb{A}_{inf}/(X-p)$ might be related to $\mathbb{C}_p$ or a variant.

In the Fontaine-Wintenberger theory, the field of norms of the cyclotomic extension $\mathbb{Q}_p(\mu_{p^\infty})$ is $\mathbb{F}_p((X))$. The "untilting" of $\mathbb{F}_p((X))$ at $X = p$ gives back $\mathbb{Q}_p(\mu_{p^\infty})$ (or something related). But this is in the context of perfectoid fields, where the tilt is in characteristic $p$.

For a perfectoid field $K$ of characteristic 0, the tilt $K^\flat$ is a perfectoid field of characteristic $p$, and $K^\flat \cong \varprojlim K / p$ where the transition map is $x \mapsto x^p$. The untilt is recovered via $\mathbb{A}_{inf}$ and quotienting by a suitable ideal.

But I don't think this directly applies to the given construction.

Let me try to think about the problem from the perspective of the answer being 1 (algebraically closed).

If $\mathbb{Q}_p^{ext}$ is algebraically closed, then the construction $\mathbb{Z}((X))_{conti}/(X-p)$ must produce an algebraically closed field. This would be a remarkable result, and it would mean that the "conti" condition is exactly what's needed to make the field algebraically closed.

One way this could work: if $\mathbb{Z}((X))_{conti}$ is a "large enough" ring that the quotient by $(X-p)$ captures all algebraic extensions of $\mathbb{Q}_p$. 

Actually, I think I might have been overthinking this. Let me consider the possibility that the "conti" condition makes $\mathbb{Z}((X))_{conti}$ a Henselian local ring (or something similar), and the quotient by $(X-p)$ gives a Henselian field, which might be algebraically closed if it's "large enough".

Hmm, but Henselian doesn't mean algebraically closed.

OK, I think I need to just commit to an answer. Let me go with **infinite** based on the following argument:

The field $\mathbb{Q}_p^{ext}$ contains $\mathbb{Q}_p$ and is not formally real. By the Artin-Schreier theorem, if the algebraic closure $\overline{\mathbb{Q}_p^{ext}}$ has finite degree over $\mathbb{Q}_p^{ext}$, then either $\mathbb{Q}_p^{ext}$ is algebraically closed (degree 1) or real closed (degree 2). Since $\mathbb{Q}_p^{ext}$ is not formally real, it cannot be real closed. 

Now, $\mathbb{Q}_p^{ext}$ is constructed as a quotient of a ring of formal Laurent series with "continuous" coefficients. This construction, while producing a field extension of $\mathbb{Q}_p$, does not produce an algebraically closed field, because:
- The "conti" condition restricts the coefficient sequences to be $p$-adically continuous, which is a topological/combinatorial condition that does not guarantee the existence of roots for all polynomials.
- In particular, one can construct algebraic extensions of $\mathbb{Q}_p^{ext}$ that are not captured by the "conti" condition.

Therefore, $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$.

Hmm, but I'm not fully confident in this answer. Let me reconsider one more time.

Actually, I just realized something important. The problem might be related to a specific result in the theory of $p$-adic fields. Let me think about the field $\mathbb{Q}_p^{ext}$ more carefully.

If $\mathbb{Z}((X))_{conti}$ is the ring of formal Laurent series $\sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$ and the sequence $(a_n)$ is $p$-adically continuous (i.e., extends to a continuous function $\mathbb{Z}_p \to \mathbb{Z}_p$), then:

- The evaluation map at $X = p$ sends this to $\sum a_n p^n \in \mathbb{Q}_p$.
- But the $p$-adic continuity of $(a_n)$ is a strong condition that restricts which $p$-adic numbers we get.

Wait, but as I noted earlier, this would give a SUBFIELD of $\mathbb{Q}_p$, not an extension. The name "$\mathbb{Q}_p^{ext}$" suggests an extension.

Unless... the "conti" condition is on a LARGER ring than $\mathbb{Z}((X))$. Maybe $\mathbb{Z}((X))_{conti}$ is the ring of formal series with coefficients in $\mathbb{Z}_p$ (not $\mathbb{Z}$) that are continuous, and this is larger than $\mathbb{Z}((X))$.

But even $\mathbb{Z}_p((X))/(X-p) \cong \mathbb{Q}_p$ as I argued.

OK, let me try the interpretation that $\mathbb{Z}((X))_{conti}$ is the ring of formal series $\sum_{n \geq n_0} a_n X^n$ where $a_n \in \overline{\mathbb{Z}_p}$ (the integral closure of $\mathbb{Z}_p$ in $\overline{\mathbb{Q}_p}$, i.e., the ring of elements of $\overline{\mathbb{Q}_p}$ with non-negative valuation) and the sequence is "continuous" in some sense.

With this interpretation, the quotient by $(X-p)$ would give a field containing $\overline{\mathbb{Q}_p}$, and if the "conti" condition is strong enough, it might even be $\mathbb{C}_p$ (which is algebraically closed).

But this is speculative. Let me just go with the answer.

Actually, you know what, let me reconsider the problem from scratch. I think the key might be in understanding what $\mathbb{Z}((X))_{conti}$ means in the context of this problem.

I think the most likely interpretation is:

$\mathbb{Z}((X))_{conti}$ is the ring of formal Laurent series $f(X) = \sum_{n \geq n_0} a_n X^n$ with $a_n \in \mathbb{Z}$, such that the sequence $(a_n)_{n \geq n_0}$ is $p$-adically continuous, meaning that for every $k \geq 1$, the sequence $(a_n \mod p^k)_{n \geq n_0}$ is eventually periodic.

This is the definition of a "$p$-automatic" or "$p$-definable" sequence (in the sense of Cobham/Christol), and it's related to the theory of algebraic power series over finite fields.

With this definition, the evaluation at $X = p$ gives a $p$-adic number $\sum a_n p^n$ where the digit sequence is eventually periodic mod $p^k$ for every $k$. These are exactly the $p$-adic numbers that are "algebraic" in some sense (related to Christol's theorem, which says that a formal power series over $\mathbb{F}_p$ is algebraic over $\mathbb{F}_p(X)$ if and only if its coefficient sequence is $p$-automatic).

But Christol's theorem is about power series over $\mathbb{F}_p$, not $\mathbb{Z}$. The analog for $\mathbb{Z}$ might be different.

Hmm, actually, there's a result that says: a $p$-adic number $\alpha = \sum a_n p^n$ (with $a_n \in \{0, \ldots, p-1\}$) is algebraic over $\mathbb{Q}$ if and only if the sequence $(a_n)$ is $p$-automatic. This is a theorem of Cobham (for the "only if" direction, assuming $\alpha$ is algebraic over $\mathbb{Q}$) and... actually, I think the exact statement is more subtle.

If the "conti" condition (eventual periodicity mod $p^k$ for all $k$) characterizes algebraic elements, then $\mathbb{Q}_p^{ext}$ might be the field of algebraic $p$-adic numbers, i.e., $\overline{\mathbb{Q}} \cap \mathbb{Q}_p$ (the algebraic closure of $\mathbb{Q}$ in $\mathbb{Q}_p$).

But $\overline{\mathbb{Q}} \cap \mathbb{Q}_p$ is NOT algebraically closed (it's the field of $p$-adic algebraic numbers, which is a subfield of $\overline{\mathbb{Q}_p}$ but not algebraically closed). Its algebraic closure is $\overline{\mathbb{Q}_p}$, which has infinite degree over it.

Wait, actually, $\overline{\mathbb{Q}} \cap \mathbb{Q}_p = \overline{\mathbb{Q}} \cdot \mathbb{Q}_p \cap \mathbb{Q}_p$... no, that's not right either. $\overline{\mathbb{Q}} \cap \mathbb{Q}_p$ is just the set of elements of $\mathbb{Q}_p$ that are algebraic over $\mathbb{Q}$, which is $\mathbb{Q}_p \cap \overline{\mathbb{Q}}$. This is a countable field, and it's not algebraically closed (e.g., $\sqrt{p}$ is in $\overline{\mathbb{Q}_p}$ but $\sqrt{p} \notin \mathbb{Q}_p$, so $\sqrt{p}$ is not in $\mathbb{Q}_p \cap \overline{\mathbb{Q}}$... wait, $\sqrt{p}$ is algebraic over $\mathbb{Q}$, so $\sqrt{p} \in \overline{\mathbb{Q}}$, but $\sqrt{p} \notin \mathbb{Q}_p$ for $p$ odd, so $\sqrt{p} \notin \overline{\mathbb{Q}} \cap \mathbb{Q}_p$).

Hmm, but $\overline{\mathbb{Q}} \cap \mathbb{Q}_p$ is not the same as $\mathbb{Q}_p^{ext}$ in general. The "conti" condition might give a different field.

OK, I think I've spent too long on this. Let me just go with my best answer.

Based on my analysis:

1. $\mathbb{Q}_p^{ext}$ is a field of characteristic 0 containing $\mathbb{Q}_p$ (or a subfield of $\mathbb{Q}_p$ — the exact nature depends on the interpretation of "conti").

2. $\mathbb{Q}_p^{ext}$ is not formally real (since it contains or is contained in $\mathbb{Q}_p$, which is not formally real).

3. By the Artin-Schreier theorem, the degree $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$ is either 1 (if $\mathbb{Q}_p^{ext}$ is algebraically closed) or infinite (since $\mathbb{Q}_p^{ext}$ is not formally real, it can't be real closed, so the degree can't be 2).

4. The construction $\mathbb{Z}((X))_{conti}/(X-p)$ does not produce an algebraically closed field (the "conti" condition is a regularity condition on coefficients, not a condition that guarantees algebraic closedness).

5. Therefore, $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$.

Wait, actually, I want to reconsider point 4. Maybe the "conti" condition IS strong enough to make the field algebraically closed.

Let me think about a specific example. Consider the polynomial $T^2 - (1+p)$ over $\mathbb{Q}_p$. This has a root $\sqrt{1+p} \in \overline{\mathbb{Q}_p}$ (by Hensel's lemma, since $1+p \equiv 1 \pmod{p}$ and $1$ is a square). So $\sqrt{1+p} \in \mathbb{Q}_p$ (for $p$ odd). So this doesn't give a non-trivial extension.

Consider $T^2 - p$ over $\mathbb{Q}_p$. This is an Eisenstein polynomial, so it gives a ramified extension of degree 2. $\sqrt{p} \notin \mathbb{Q}_p$. Is $\sqrt{p} \in \mathbb{Q}_p^{ext}$?

If $\mathbb{Q}_p^{ext}$ is a subfield of $\mathbb{Q}_p$, then $\sqrt{p} \notin \mathbb{Q}_p^{ext}$ (since $\sqrt{p} \notin \mathbb{Q}_p$). But if $\mathbb{Q}_p^{ext}$ is an extension of $\mathbb{Q}_p$, then $\sqrt{p}$ might or might not be in $\mathbb{Q}_p^{ext}$.

I think the answer depends crucially on the interpretation of "conti", which I'm not sure about. Given the ambiguity, let me go with the answer that seems most mathematically interesting and likely intended:

The degree is **infinite**.

Here's my final reasoning:

$\mathbb{Q}_p^{ext}$ is a field of characteristic 0 that is not formally real (it contains $\mathbb{Q}_p$ or is contained in $\mathbb{Q}_p$, either way it's not formally real). By the Artin-Schreier theorem, the algebraic closure $\overline{\mathbb{Q}_p^{ext}}$ has either degree 1 over $\mathbb{Q}_p^{ext}$ (if $\mathbb{Q}_p^{ext}$ is algebraically closed) or infinite degree. The construction via formal Laurent series with continuous coefficients does not yield an algebraically closed field (one can exhibit algebraic elements not in the field, such as roots of Eisenstein polynomials that cannot be represented by series with the required continuity property). Therefore, the degree of the algebraic closure over $\mathbb{Q}_p^{ext}$ is infinite.

Hmm wait, actually I want to reconsider once more. Let me think about whether the problem might have a more specific answer.

The problem says "determine the degree of extension of the algebraic closure over the field $\mathbb{Q}_p^{ext}$". If the answer is just "infinite", that's not very specific. Maybe the answer is a specific infinite cardinal, like $\aleph_0$ or $2^{\aleph_0}$.

For $\mathbb{Q}_p$, $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = \aleph_0$ (countably infinite). If $\mathbb{Q}_p^{ext}$ is between $\mathbb{Q}_p$ and $\overline{\mathbb{Q}_p}$, then $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p^{ext}]$ is at most $\aleph_0$.

If $\mathbb{Q}_p^{ext}$ is a transcendental extension of $\mathbb{Q}_p$, then $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$ could be uncountable.

Given the construction from formal Laurent series, $\mathbb{Q}_p^{ext}$ has cardinality at most $|\mathbb{Z}((X))_{conti}|$, which depends on the "conti" condition. If "conti" means $p$-adically continuous sequences, then the cardinality is $|\mathbb{Z}_p|^{|\mathbb{Z}|} = 2^{\aleph_0}$ (uncountable). If "conti" means eventually periodic mod $p^k$ for all $k$, then the cardinality is $\aleph_0$ (countable).

If $\mathbb{Q}_p^{ext}$ is countable, then $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] \leq \aleph_0$ (since the algebraic closure of a countable field is countable). If $\mathbb{Q}_p^{ext}$ is uncountable, the degree could be larger.

I think the most likely answer, given the problem's phrasing, is that the degree is **infinite** (or more specifically, countably infinite, $\aleph_0$).

But actually, let me reconsider the possibility that the answer is 1 (algebraically closed). 

Hmm, I just thought of something. The notation $\mathbb{Q}_p^{ext}$ might stand for "the extremal extension" or "the maximal extension" of $\mathbb{Q}_p$, which could be algebraically closed. In some contexts, "ext" refers to an extremal or maximal object.

If $\mathbb{Q}_p^{ext}$ is the "maximal" extension of $\mathbb{Q}_p$ obtained from this construction, it might indeed be algebraically closed, giving degree 1.

But I'm not confident enough in this interpretation. Let me go with **infinite** as my answer.

Actually, wait. Let me reconsider the problem one more time.

The construction $\mathbb{Z}((X))_{conti}/(X-p)$: if "conti" means that the coefficients form a continuous sequence (in the $p$-adic topology), then this is a very natural construction. The key insight might be:

- $\mathbb{Z}((X))$ with the $(X)$-adic topology is a complete topological ring.
- The "conti" subring consists of elements where the coefficients vary continuously in the $p$-adic sense.
- Quotienting by $(X-p)$ gives a field that inherits both the $X$-adic and $p$-adic structures.

If the resulting field is complete with respect to a non-trivial non-archimedean valuation, and if it's "large enough" (e.g., spherically complete), then by Krasner's lemma, it might be algebraically closed.

A spherically complete field is not necessarily algebraically closed, but a maximally complete (or spherically complete) immediate extension of a discretely valued field is unique up to isomorphism.

Hmm, I don't think spherical completeness implies algebraic closedness.

OK, I'll go with my answer: the degree is **infinite**.

Let me write up a clean proof.

Actually, let me reconsider one final time. I want to make sure I'm not missing something.

The problem is: "Determine the degree of extension of the algebraic closure over the field $\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p)$."

I think the key observation is:

1. $\mathbb{Q}_p^{ext}$ is a field of characteristic 0.
2. $\mathbb{Q}_p^{ext}$ contains $\mathbb{Q}_p$ (or is related to $\mathbb{Q}_p$ in a way that makes it not formally real).
3. By Artin-Schreier, $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] \in \{1, 2, \infty\}$.
4. Since $\mathbb{Q}_p^{ext}$ is not formally real, $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] \neq 2$.
5. So the degree is either 1 or $\infty$.

Now, the question is whether $\mathbb{Q}_p^{ext}$ is algebraically closed. 

I think the answer is that $\mathbb{Q}_p^{ext}$ is NOT algebraically closed, and the degree is **infinite**. 

Here's a concrete argument: Consider the polynomial $f(T) = T^p - T - 1/p$ (an Artin-Schreier polynomial). Over $\mathbb{Q}_p$, this polynomial is irreducible (by Artin-Schreier theory in characteristic 0, or by direct computation). If $\mathbb{Q}_p^{ext}$ is an extension of $\mathbb{Q}_p$ that is "close" to $\mathbb{Q}_p$ (in the sense that it's obtained by a quotient of formal series), then this polynomial might still be irreducible over $\mathbb{Q}_p^{ext}$, showing that $\mathbb{Q}_p^{ext}$ is not algebraically closed.

But this argument is not rigorous without knowing the exact nature of $\mathbb{Q}_p^{ext}$.

Let me try another approach. The field $\mathbb{Q}_p^{ext}$ is constructed as a quotient of a ring of formal Laurent series. The cardinality of this field is at most the cardinality of $\mathbb{Z}((X))_{conti}$. If "conti" means $p$-adically continuous, then the cardinality is at most $|\mathbb{Z}_p^{\mathbb{Z}}| = (2^{\aleph_0})^{\aleph_0} = 2^{\aleph_0}$. The algebraic closure of a field of cardinality $\kappa$ has cardinality at most $\kappa^{\aleph_0}$. So the algebraic closure of $\mathbb{Q}_p^{ext}$ has cardinality at most $(2^{\aleph_0})^{\aleph_0} = 2^{\aleph_0}$, which is the same as the cardinality of $\mathbb{Q}_p^{ext}$. So the degree $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$ is at most $2^{\aleph_0}$ (as a cardinal).

But this doesn't help determine the exact degree.

OK, I'll commit to my answer: the degree is **infinite**. Let me write the proof.

Hmm, actually, I realize I should think about this more carefully. Let me consider the possibility that the answer is 1.

If $\mathbb{Z}((X))_{conti}$ is the ring of formal Laurent series with $p$-adically continuous coefficient sequences, and if this ring is "large enough" that the quotient by $(X-p)$ gives an algebraically closed field, then the answer is 1.

One argument for this: the $p$-adic continuity condition on the coefficients means that the coefficients are determined by a continuous function $\mathbb{Z}_p \to \mathbb{Z}_p$. The space of such functions is very rich (it's a $\mathbb{Z}_p$-module of uncountable rank). When we evaluate at $X = p$, the resulting field might be "large enough" to be algebraically closed.

But I don't have a rigorous argument for this. And I don't have a rigorous argument against it either.

Let me just go with the answer that I think is most likely correct, given the mathematical context.

I think the answer is **infinite**, and here's my best argument:

$\mathbb{Q}_p^{ext}$ is a field of characteristic 0 that is not formally real. By the Artin-Schreier theorem, the degree of its algebraic closure over it is either 1 (if algebraically closed) or infinite. The construction $\mathbb{Z}((X))_{conti}/(X-p)$ produces a field that is not algebraically closed, because the "conti" condition (whatever its exact meaning) is a regularity condition on the coefficient sequences that does not guarantee the solvability of all polynomial equations. In particular, one can find irreducible polynomials over $\mathbb{Q}_p^{ext}$ (such as Artin-Schreier polynomials or Eisenstein polynomials) that have no roots in $\mathbb{Q}_p^{ext}$. Therefore, the degree of the algebraic closure over $\mathbb{Q}_p^{ext}$ is infinite.

Actually, I just want to double-check the Artin-Schreier theorem statement.

Artin-Schreier theorem: Let $K$ be a field with $\overline{K} \neq K$ (i.e., $K$ is not algebraically closed) and $[\overline{K}:K] < \infty$. Then:
1. $[\overline{K}:K] = 2$
2. $K$ is real closed (hence formally real)
3. $\overline{K} = K(i)$ where $i^2 = -1$

So if $K$ is not formally real and not algebraically closed, then $[\overline{K}:K] = \infty$.

And $\mathbb{Q}_p$ is not formally real (for any prime $p$). This is because $\mathbb{Q}_p$ has $-1$ as a sum of squares. Specifically:
- For $p \equiv 1 \pmod{4}$: $-1$ is a square in $\mathbb{Q}_p$, so $-1 = x^2$ for some $x$, hence $-1$ is a sum of 1 square.
- For $p \equiv 3 \pmod{4}$: $-1$ is not a square, but by the theory of quadratic forms, $-1$ is a sum of 2 squares in $\mathbb{Q}_p$ (since the $u$-invariant of $\mathbb{Q}_p$ is 4, meaning every element is a sum of at most 4 squares, and $-1$ is a sum of 2 squares).
- For $p = 2$: $-1$ is a sum of 4 squares in $\mathbb{Q}_2$ (e.g., $-1 = 1 + 1 + 1 + (-4)$, but $-4$ is a square times $-1$... hmm, let me think. Actually, $-1 \equiv 7 \pmod{8}$, and by Hensel's lemma, $-1$ is a sum of 4 squares in $\mathbb{Q}_2$.)

In any case, $\mathbb{Q}_p$ is not formally real, so any field containing $\mathbb{Q}_p$ is also not formally real.

So the argument is:
1. $\mathbb{Q}_p^{ext}$ contains $\mathbb{Q}_p$ (assuming the construction gives an extension).
2. $\mathbb{Q}_p$ is not formally real, so $\mathbb{Q}_p^{ext}$ is not formally real.
3. If $\mathbb{Q}_p^{ext}$ is not algebraically closed, then by Artin-Schreier, $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$.
4. $\mathbb{Q}_p^{ext}$ is not algebraically closed (argument needed).
5. Therefore, $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = \infty$.

For step 4, I need to argue that $\mathbb{Q}_p^{ext}$ is not algebraically closed. 

One approach: show that $\mathbb{Q}_p^{ext}$ has a non-trivial valuation (inherited from the $p$-adic valuation or the $X$-adic valuation), and the residue field or value group is not "algebraically closed" in the appropriate sense. For a complete non-archimedean field $K$, $K$ is algebraically closed if and only if its value group is divisible and its residue field is algebraically closed. If $\mathbb{Q}_p^{ext}$ has value group $\mathbb{Z}$ (not divisible) or residue field $\mathbb{F}_p$ (not algebraically closed), then it's not algebraically closed.

But I'm not sure about the valuation structure of $\mathbb{Q}_p^{ext}$.

Another approach: exhibit a specific polynomial that has no root in $\mathbb{Q}_p^{ext}$.

Let me try: the polynomial $T^p - T - X^{-1}$ (as an element of $\mathbb{Q}_p^{ext}[T]$, where $X$ is the image of $X$ in the quotient... wait, $X = p$ in the quotient, so this would be $T^p - T - 1/p$).

The polynomial $T^p - T - 1/p$ over $\mathbb{Q}_p$: by Artin-Schreier theory, this is related to the Artin-Schreier extension in characteristic $p$. In characteristic 0, $T^p - T - 1/p$ is a polynomial of degree $p$. Is it irreducible over $\mathbb{Q}_p$?

The discriminant of $T^p - T - a$ is $(-1)^{p(p-1)/2} \cdot (p^p \cdot a^{p-1} - (-1)^{p-1} \cdot p^{p-1})$... this is getting complicated. Let me just check if $T^p - T - 1/p$ has a root in $\mathbb{Q}_p$.

If $\alpha \in \mathbb{Q}_p$ satisfies $\alpha^p - \alpha = 1/p$, then $v_p(\alpha^p - \alpha) = v_p(1/p) = -1$. Now, $v_p(\alpha^p - \alpha) = v_p(\alpha(\alpha^{p-1} - 1))$. If $v_p(\alpha) \geq 0$, then $v_p(\alpha^{p-1} - 1) \geq 0$ (since $\alpha^{p-1} \equiv 0$ or $1 \pmod{p}$... hmm, this depends on $\alpha$). 

If $v_p(\alpha) > 0$, then $v_p(\alpha^p) = p \cdot v_p(\alpha) > v_p(\alpha)$, so $v_p(\alpha^p - \alpha) = v_p(\alpha) \geq 1 > -1$. Contradiction.

If $v_p(\alpha) = 0$, then $\alpha$ is a unit, and $\alpha^{p-1} \equiv 1 \pmod{p}$ (by Fermat's little theorem), so $v_p(\alpha^{p-1} - 1) \geq 1$, and $v_p(\alpha^p - \alpha) = v_p(\alpha) + v_p(\alpha^{p-1} - 1) \geq 1 > -1$. Contradiction.

If $v_p(\alpha) < 0$, then $v_p(\alpha^p) = p \cdot v_p(\alpha) < v_p(\alpha)$, so $v_p(\alpha^p - \alpha) = p \cdot v_p(\alpha)$. We need $p \cdot v_p(\alpha) = -1$, which is impossible since $v_p(\alpha) \in \mathbb{Z}$ and $p \geq 2$.

So $T^p - T - 1/p$ has no root in $\mathbb{Q}_p$. But does it have a root in $\mathbb{Q}_p^{ext}$?

If $\mathbb{Q}_p^{ext}$ is an extension of $\mathbb{Q}_p$, then $\alpha \in \mathbb{Q}_p^{ext}$ with $\alpha^p - \alpha = 1/p$ might exist. The question is whether the "conti" condition allows such an $\alpha$.

Without knowing the exact definition of "conti", I can't determine this. But I'll assume that $\mathbb{Q}_p^{ext}$ is not algebraically closed and go with the answer **infinite**.

Let me now write up the proof. I'll focus on the Artin-Schreier argument, which is the key mathematical content.

Wait, actually, I want to reconsider one more time. Let me think about whether the problem might be asking about something different.

"Determine the degree of extension of the algebraic closure over the field $\mathbb{Q}_p^{ext}$"

This is asking for $[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}]$.

Given the Artin-Schreier constraint, this is either 1 or infinite (since $\mathbb{Q}_p^{ext}$ is not formally real).

I think the problem is designed to test whether the student knows the Artin-Schreier theorem and can apply it. The answer is:

- If $\mathbb{Q}_p^{ext}$ is algebraically closed: degree = 1
- If $\mathbb{Q}_p^{ext}$ is not algebraically closed: degree = infinite

The construction $\mathbb{Z}((X))_{conti}/(X-p)$ is meant to produce a field that is NOT algebraically closed (it's some kind of "extension" of $\mathbb{Q}_p$ but not the full algebraic closure), so the answer is **infinite**.

Alternatively, the construction might be designed to produce $\mathbb{C}_p$ (which is algebraically closed), in which case the answer is 1.

I'll go with **infinite** as my final answer.

Let me write the proof now.

Hmm, actually, I want to think about this one more time. The problem says $\mathbb{Q}_p^{ext}$, and the "ext" might stand for "extension" (just meaning it's an extension of $\mathbb{Q}_p$) or "extreme" or "external" or something else.

Given that the problem is asking to "determine the degree", and the possible answers are 1 or infinite, I think the problem is testing the Artin-Schreier theorem. The answer is likely **infinite**, because:

1. $\mathbb{Q}_p^{ext}$ is a field of characteristic 0 containing $\mathbb{Q}_p$.
2. $\mathbb{Q}_p$ is not formally real (it's a $p$-adic field).
3. Therefore $\mathbb{Q}_p^{ext}$ is not formally real.
4. $\mathbb{Q}_p^{ext}$ is not algebraically closed (it's a proper subfield of its algebraic closure, as the construction doesn't
