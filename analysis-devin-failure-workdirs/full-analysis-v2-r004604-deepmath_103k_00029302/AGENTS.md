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
  <problem_id>deepmath_103k_00029302</problem_id>
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

Let \( f \in L^p(\mathbb{R}) \) be a continuous function for some \( 1 \leq p < \infty \). Does it follow that \( \lim_{|x| \to \infty} f(x) = 0 \)? Justify your answer.

## Standard Solution

Okay, so the problem is asking whether if a function f is in L^p(R) and is continuous, does it necessarily follow that the limit of f(x) as |x| approaches infinity is zero. Hmm, I remember that for functions in L^p spaces, especially when p is between 1 and infinity, there's some decay at infinity, but I need to recall if continuity is enough to enforce that the actual limit is zero. 

First, let me recall what L^p(R) means. A function f is in L^p(R) if the integral of |f(x)|^p over all of R is finite. That definitely requires that |f(x)|^p tends to zero in some averaged sense as |x| goes to infinity. But does that mean pointwise convergence to zero? I know there are examples of functions in L^p that don't go to zero pointwise, but those are usually not continuous. For instance, functions with tall spikes that get narrower as |x| increases can be in L^p even if the spikes don't diminish in height, because the area under the spike (the integral) becomes small due to the narrowing width. But such functions aren't continuous because of the sudden spikes.

Since f is continuous here, maybe that changes things. If f didn't go to zero, then there would exist some epsilon > 0 and a sequence of points x_n with |x_n| approaching infinity such that |f(x_n)| >= epsilon. But f is continuous, so around each x_n, there would be a small interval where |f(x)| is, say, at least epsilon/2. If those intervals don't overlap too much, the integral of |f|^p over those intervals would add up to something finite, but wait, if |x_n| goes to infinity, the intervals around x_n can be spaced out so that they don't overlap. Each such interval contributes at least (epsilon/2)^p times the length of the interval. If the lengths are bounded below, then summing over infinitely many such intervals would make the integral infinite, which contradicts f being in L^p. 

Therefore, maybe for continuous functions in L^p, the decay at infinity must actually be zero. Let me try to formalize that argument.

Suppose, for contradiction, that lim_{|x|->infty} f(x) is not zero. Then there exists an epsilon > 0 and a sequence {x_n} with |x_n| -> infinity such that |f(x_n)| >= epsilon for all n. Since f is continuous, for each x_n, there exists a delta_n > 0 such that for |x - x_n| < delta_n, |f(x) - f(x_n)| < epsilon/2. Therefore, on each interval (x_n - delta_n, x_n + delta_n), we have |f(x)| >= |f(x_n)| - |f(x) - f(x_n)| >= epsilon - epsilon/2 = epsilon/2.

Now, the integral of |f|^p over R would include the integrals over each of these intervals. Let's compute the integral over each interval: it's at least (epsilon/2)^p * 2 delta_n. If we can choose the delta_n such that the intervals (x_n - delta_n, x_n + delta_n) are disjoint (which we can do by choosing delta_n small enough and since |x_n| tends to infinity, the points x_n are eventually far apart), then the total integral would be at least sum_{n=1}^\infty (epsilon/2)^p * 2 delta_n. If we can have delta_n bounded below by some positive number, say delta, then the sum becomes infinite, contradicting f being in L^p. 

But wait, the problem is whether we can choose delta_n to be bounded below. Since the function is continuous, the delta_n depends on the modulus of continuity at each x_n. However, even if the function is continuous, the modulus of continuity could get worse as |x_n| increases, meaning delta_n might have to be chosen smaller and smaller. For example, if near each x_n, the function has a spike that is very narrow, but still maintains |f(x)| >= epsilon/2 in that narrow interval, even if the intervals are getting narrower. But if the function is continuous, the width of the interval around x_n where |f(x)| >= epsilon/2 could potentially be made to have lengths delta_n such that sum delta_n converges, thus making the total integral finite. 

Wait, but if the delta_n are chosen such that (epsilon/2)^p * 2 delta_n is summable, then even with infinitely many intervals, the integral could still be finite. For example, if delta_n = 1/n^2, then sum delta_n converges. So in that case, even if we have infinitely many such intervals, as long as their widths go to zero fast enough, the integral could still be finite. But does the continuity of f allow such a construction?

Let me try to construct a counterexample. Suppose we have a continuous function f that is in L^p but does not go to zero at infinity. For instance, consider a function that has bumps at each integer n >= 1, where the bump at n has height 1 but width 1/n^2. So around each integer n, the function rises to 1, stays there for a width of 1/n^2, and then goes back down to zero. The integral of |f|^p over each bump is approximately 1^p * 1/n^2 = 1/n^2. Since the sum of 1/n^2 converges, the total integral would be finite (pi^2/6 or something), so f is in L^p. However, as n approaches infinity, the function has points (at each integer n) where f(n) = 1, so the limit as |x| approaches infinity does not exist; in fact, it has points going out to infinity where f is 1. But wait, in this case, the function isn't continuous because between the bumps, it goes down to zero. If the function is made continuous by connecting the bumps with smooth downs and ups, then actually between the bumps, the function would have to decrease to zero. Wait, but if the bumps are at each integer n, and the width is 1/n^2, then the distance between consecutive bumps is 1 (from n to n+1), but the width of each bump is 1/n^2, which gets smaller as n increases. So the bumps are getting narrower but their separation remains constant. However, as n increases, the next bump is at n+1, which is 1 unit away, but the width of the bump at n is 1/n^2. So for large n, the bump at n is very narrow and the next bump is 1 unit away. Therefore, it's possible to have a continuous function that goes up to 1 at each n, with the bump of width 1/n^2, and connects back to zero in between. 

But wait, to make the function continuous, between the bumps, the function must decrease from 1 to 0 and then back to 1. However, if the bumps are placed at each integer n with width 1/n^2, then between n and n+1, the function would have to go down from 1 to 0 and then up to 1 again. However, the distance between n and n+1 is 1, and the width of each bump is 1/n^2, so the "valley" between the bumps has length 1 - 1/n^2 - 1/(n+1)^2. Wait, but as n increases, the valleys between the bumps become almost 1 unit in length. So the function would have to go down from 1 to 0 over a distance of (1 - 1/n^2)/2 and then up again. If the descent and ascent are linear, then the slope would be on the order of n^2, which becomes steeper as n increases. But since the function is required to be continuous, but not necessarily differentiable, steep slopes are allowed. However, if the slope becomes unbounded, the function might not be continuous? Wait, no, continuity doesn't require the function to have bounded slope; it just requires the function to have no jumps. Even if the slope becomes infinite at some points, as long as the function is defined everywhere and has no jumps, it's continuous. For example, the function f(x) = sqrt|x| is continuous everywhere, even though the derivative at x=0 is infinite.

But in our case, if the slope between the bumps becomes steeper as n increases, but still remains finite everywhere, then the function is continuous. However, if the slopes become unbounded, then perhaps the function is still continuous, just not differentiable at those points. So maybe such a function is possible. If so, then this function is in L^p because the integral is sum_{n=1}^\infty 1/n^2 which converges, and the function is continuous, yet f(n) = 1 for all n, so the limit as |x| approaches infinity does not exist; in fact, it has points going to infinity where f is 1. Therefore, this would be a counterexample, showing that even continuous functions in L^p don't necessarily decay to zero at infinity.

But wait, in this construction, the function is 1 at each integer n, but between the integers, it dips down to zero. However, as n increases, the dips become steeper. The important thing is that the function is continuous. Let me try to write down such a function explicitly.

Define f(x) as follows: For each integer n ≥ 1, let f(n) = 1. Then, around each n, define f(x) to linearly decrease to 0 over the interval [n - 1/(2n^2), n] and linearly increase back to 1 over the interval [n, n + 1/(2n^2)]. Outside of these intervals around each n, set f(x) = 0. Wait, but then between n + 1/(2n^2) and (n+1) - 1/(2(n+1)^2), the function is zero. The length of the interval where f(x) is non-zero around each n is 1/n^2. The total integral is sum_{n=1}^\infty (1/n^2) * (1^p) = sum_{n=1}^\infty 1/n^2, which converges. The function is continuous because at the points n ± 1/(2n^2), the function transitions linearly to zero, so there are no jumps. However, between these intervals, the function is zero. But wait, for each n, the support of the bump around n is [n - 1/(2n^2), n + 1/(2n^2)], which has length 1/n^2. The distance between consecutive bumps is (n+1) - 1/(2(n+1)^2) - (n + 1/(2n^2)) ) = 1 - 1/(2(n+1)^2) - 1/(2n^2). For large n, this distance is approximately 1 - 0 - 0 = 1. Therefore, as n increases, the bumps get narrower and are spaced approximately 1 unit apart. Therefore, the supports of the bumps do not overlap because the distance between them is about 1 unit, and their widths are 1/n^2, which for n ≥ 1 is at most 1, so starting from some n onward, the bumps won't overlap. Wait, actually, for n=1, the width is 1/1^2 = 1, so the first bump around n=1 is from 1 - 1/2 to 1 + 1/2, which is [0.5, 1.5]. The next bump around n=2 is [2 - 1/8, 2 + 1/8] = [1.875, 2.125]. The distance between the end of the first bump (1.5) and the start of the second bump (1.875) is 0.375, which is positive. Similarly, for n=3, the bump is [3 - 1/18, 3 + 1/18] ≈ [2.944, 3.056], which is separated from the n=2 bump. So actually, none of the bumps overlap. Therefore, the function f(x) as constructed is continuous, in L^p (since the integral is sum 1/n^2 < infty), yet f(n) = 1 for all n, so the limit as |x| approaches infinity does not exist; in particular, lim sup_{|x|->infty} |f(x)| = 1 and lim inf is 0. Therefore, the limit does not equal zero. 

Therefore, the answer to the original question is no; it does not follow that the limit is zero. The constructed function serves as a counterexample.

But wait, let me verify continuity again. For each bump around n, the function increases linearly from 0 to 1 over an interval of length 1/(2n^2) on the left side of n, and decreases linearly from 1 to 0 over an interval of length 1/(2n^2) on the right side. So, at the points n ± 1/(2n^2), the function is 0, and between these points, it's a linear slope. Since the function is 0 outside these intervals, and at the endpoints of the intervals it's 0, which matches the surrounding regions, there are no jumps. Hence, f is continuous everywhere. 

Moreover, f is in L^p because ||f||_p^p = sum_{n=1}^\infty (area of each bump). Each bump is a triangle with base 1/n^2 and height 1, but wait, actually in my construction, each bump is a tent function: it goes from 0 to 1 and back to 0 over an interval of total width 1/n^2. So the integral over each bump is the area of the triangle: (base * height)/2 = (1/n^2 * 1)/2 = 1/(2n^2). Therefore, the total integral is sum_{n=1}^\infty 1/(2n^2) = (1/2)(pi^2/6) < infty. So yes, f is in L^p for any p ≥ 1. 

Therefore, this function is a continuous function in L^p(R) which does not satisfy lim_{|x|->infty} f(x) = 0. Hence, the answer is no, it does not follow.

Alternatively, another classic example is a function that has taller and taller spikes spaced further apart, but since the function is continuous, the spikes have to be connected smoothly to the base. However, as long as the area under each spike is summable, the function can be in L^p even if the spikes don't diminish in height. This is similar to the example above.

But wait, in the example above, the function is 1 at each integer n, but between the integers, it's zero except near the integers where it has the tent functions. However, in this case, the maximum value of f is 1, achieved at each integer n. So even though the function is continuous and in L^p, the limit at infinity does not exist because f(n) = 1 for all n, hence there is a sequence x_n = n approaching infinity where f(x_n) = 1, but elsewhere, the function is zero or small. Therefore, lim inf is 0 and lim sup is 1, so the limit does not exist.

Therefore, the conclusion is that continuity combined with L^p does not necessarily enforce the function to decay to zero at infinity. Hence, the answer is no.

**Final Answer**
\boxed{No}
</think>

Given a continuous function \( f \in L^p(\mathbb{R}) \) for some \( 1 \leq p < \infty \), we need to determine if it necessarily follows that \( \lim_{|x| \to \infty} f(x) = 0 \).

To address this, consider constructing a function that is continuous and in \( L^p(\mathbb{R}) \) but does not decay to zero at infinity. One such example is a function with bumps at each integer \( n \geq 1 \), where each bump has height 1 and width \( \frac{1}{n^2} \). 

1. **Construction of the Function**:
   - For each integer \( n \geq 1 \), define a bump centered at \( n \).
   - Each bump rises linearly from 0 to 1 over the interval \( [n - \frac{1}{2n^2}, n] \) and then decreases linearly back to 0 over the interval \( [n, n + \frac{1}{2n^2}] \).
   - Outside these intervals, the function is 0.

2. **Continuity**:
   - The function is continuous because it is constructed using linear segments with no jumps. At the boundaries of each interval, the function value matches the surrounding zero regions.

3. **Integrability**:
   - The integral of \( |f(x)|^p \) over each bump is the area of a triangular region with base \( \frac{1}{n^2} \) and height 1. The area of each triangle is \( \frac{1}{2n^2} \).
   - The total integral over all bumps is \( \sum_{n=1}^{\infty} \frac{1}{2n^2} \), which converges (as it is a constant multiple of the convergent series \( \sum_{n=1}^{\infty} \frac{1}{n^2} \)).

4. **Non-Decay at Infinity**:
   - The function attains the value 1 at each integer \( n \), which are points going to infinity. Hence, \( \lim_{|x| \to \infty} f(x) \) does not exist because \( \limsup_{|x| \to \infty} f(x) = 1 \) and \( \liminf_{|x| \to \infty} f(x) = 0 \).

This construction demonstrates that a continuous function in \( L^p(\mathbb{R}) \) does not necessarily decay to zero at infinity. Therefore, the answer is:

\[
\boxed{No}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks: Determine whether the integral closure of a Noetherian integral domain is always Noetherian when the dimension of the domain is 2.

This is a classic question in commutative algebra. The answer is NO — the integral closure of a Noetherian integral domain of dimension 2 is NOT always Noetherian. This is the famous counterexample by Akizuki (1935) / Nagata.

Let me recall the details. The question is about whether the integral closure (in its field of fractions) of a Noetherian domain of dimension 2 is Noetherian.

Key facts:
- Dimension 1: Krull-Akizuki theorem says YES — the integral closure of a Noetherian domain of dimension 1 is a Dedekind domain (or more precisely, a Noetherian integrally closed domain), so it's Noetherian.
- Dimension 2: The answer is NO. Akizuki gave a counterexample in 1935 of a 2-dimensional Noetherian local domain whose integral closure is not Noetherian (in fact, not even finitely generated as a module).
- Dimension ≥ 3: Also NO, by Nagata's examples.

Actually, let me be careful. Nagata's famous counterexample shows that the integral closure of a Noetherian domain need not be Noetherian (and need not be finitely generated). The Akizuki example is 1-dimensional... wait, no.

Let me reconsider. The Krull-Akizuki theorem states: if A is a 1-dimensional Noetherian domain with fraction field K, and L is a finite extension of K, then the integral closure of A in L is a Dedekind domain (hence Noetherian). So for dimension 1, the answer is YES.

For dimension 2, the answer is NO. This was shown by Akizuki in 1935. Akizuki constructed a 2-dimensional Noetherian local domain whose integral closure is not Noetherian.

Actually, I need to be more careful about the history. Let me think about what's known:

- Nagata's counterexample (from his book "Local Rings", 1962): He gave an example of a Noetherian domain whose integral closure is not Noetherian. This is a 2-dimensional (or 3-dimensional?) example.

Actually, the most famous example is Nagata's. Let me recall: Nagata constructed a 2-dimensional Noetherian local domain whose integral closure is not a finite module and not Noetherian.

The answer to the question is: NO, the integral closure of a Noetherian integral domain of dimension 2 is NOT always Noetherian.

Now I need to provide a proof/counterexample. Let me construct the Nagata-type example.

The standard construction:

Let $k$ be a field of characteristic 0, and consider the formal power series ring $k[[x, y]]$. Let $K = k((x, y))$ be its fraction field.

Actually, let me recall the construction more carefully. The idea is to create a Noetherian domain $A$ of dimension 2 whose integral closure $A'$ in its fraction field is not Noetherian.

One approach (Nagata's): Take a field $k$ and consider $k[[x, y]]$. Choose elements in the fraction field that are integral over a subring but form an infinite ascending chain of ideals in the integral closure.

Let me think about the specific construction. 

A well-known approach: Let $k$ be a field, and let $s_1, s_2, \ldots$ be infinitely many elements. Consider the ring $R = k[[x, y]]$ and construct a subring $A$ of $R$ (or of its fraction field) that is Noetherian, 2-dimensional, but whose integral closure is $R$ itself (or something larger) which is not finitely generated.

Actually, let me recall the precise construction. The key idea in Nagata's example:

Let $k$ be a field. Let $x, y$ be indeterminates. Consider the formal power series ring $V = k[[x]]$. For each $i \geq 1$, define $y_i = x^{i} / (1 + x)^{...}$... hmm, I don't remember the exact construction.

Let me think about this differently. The standard counterexample:

**Nagata's Example**: Let $k$ be a field of characteristic 0. Let $R = k[[X, Y]]$ be the formal power series ring in two variables. Consider the fraction field $K = k((X, Y))$. 

Choose a sequence of elements $\alpha_n \in K$ such that:
- Each $\alpha_n$ is integral over some Noetherian subring $A$ of $K$
- The $\alpha_n$ generate an infinite ascending chain of ideals in the integral closure $A'$

Actually, let me recall the more specific construction. I think the construction involves:

Let $k$ be a field, $t$ an indeterminate. Consider the DVR $V = k[[t]]$ with fraction field $k((t))$. 

Choose a sequence of rational numbers $r_n$ that is strictly increasing, e.g., $r_n = 1 - 1/(n+1)$ for $n \geq 1$, so $r_1 = 1/2, r_2 = 2/3, r_3 = 3/4, \ldots$, converging to 1.

For each $n$, consider the valuation $v_n$ on $k((t))$ defined by... no, that's not quite right either.

Let me try a different, cleaner approach. I recall that the construction uses the idea of "pseudo-valuation rings" or composite of valuations.

Actually, here's a cleaner version of the construction that I can recall:

**Construction**: Let $k$ be a field. Let $x, y$ be algebraically independent over $k$. Consider the field $K = k(x, y)$. 

Define a discrete valuation $v$ on $K$ as follows: first define $v(x) = 1$, and extend $v$ to $k(x)$ by $v(f/g) = \deg g - \deg f$ (the valuation at infinity on $k(x)$... no, that gives $v(x) = -1$). 

Hmm, let me think more carefully.

Actually, let me use a well-known explicit construction. Here's one based on Nagata:

Let $k$ be a field, and let $t$ be an indeterminate. Consider $k[[t]]$, the formal power series ring, which is a DVR with uniformizer $t$. Its fraction field is $k((t))$.

Now, consider the element $y = \sum_{i=1}^{\infty} a_i t^{r_i}$ where $r_i$ is a sequence of positive rational numbers with bounded denominators but... no, $k[[t]]$ only has integer exponents.

Let me try yet another approach. I think the cleanest version uses the following:

Let $k$ be a field. Let $x, y$ be indeterminates over $k$. Consider the polynomial ring $k[x, y]$ and its fraction field $k(x, y)$.

Define a rank-1 discrete valuation $v$ on $k(x, y)$ by: $v(x) = 1$, $v(y) = \alpha$ where $\alpha$ is a positive irrational number. This extends to a valuation on $k(x, y)$ by $v(\sum c_{ij} x^i y^j) = \min\{i + j\alpha\}$ and then to the fraction field.

The valuation ring $V = \{f \in k(x,y) : v(f) \geq 0\}$ is a DVR (since $v$ is a discrete rank-1 valuation — well, it's rank 1 but the value group is $\mathbb{Z} + \mathbb{Z}\alpha \cong \mathbb{Z}^2$ lex... no, the value group is $\{m + n\alpha : m, n \in \mathbb{Z}\}$ which is isomorphic to $\mathbb{Z}^2$ with lex ordering? No, it's ordered as a subgroup of $\mathbb{R}$, so it's a rank-1 valuation (archimedean), and the value group is $\mathbb{Z} + \mathbb{Z}\alpha$ which is not discrete (it's dense in $\mathbb{R}$ since $\alpha$ is irrational).

So $V$ is a valuation ring but NOT a DVR (not Noetherian) because the value group is not discrete.

Now, the key construction: We want to find a Noetherian subring $A$ of $V$ (or of $k(x,y)$) such that $V$ is the integral closure of $A$, and $A$ has dimension 2.

Hmm, but if $V$ is the integral closure and $V$ is not Noetherian, that would give us the counterexample. But we need $A$ to be Noetherian and 2-dimensional.

Actually, the standard construction is more subtle. Let me recall it properly.

**Nagata's construction** (from "Local Rings", Interscience, 1962, Appendix, Example 5):

Let $k$ be a field, $x, y$ indeterminates. Let $\alpha$ be a positive irrational number. Define the valuation $v$ on $k(x, y)$ by $v(x) = 1$, $v(y) = \alpha$, extended to $k(x,y)$ by $v(\sum c_{ij} x^i y^j) = \min(i + j\alpha)$ and to fractions by $v(f/g) = v(f) - v(g)$.

The value group is $\Gamma = \mathbb{Z} + \mathbb{Z}\alpha \subset \mathbb{R}$, which is not discrete (it's dense in $\mathbb{R}$).

The valuation ring $V = \{f \in k(x,y) : v(f) \geq 0\}$ has maximal ideal $\mathfrak{m} = \{f : v(f) > 0\}$.

Now, $V$ is not Noetherian because $\Gamma$ is not discrete (the maximal ideal is not finitely generated).

Now we need to construct a Noetherian subring $A$ of $k(x,y)$ of dimension 2 such that $V$ is integral over $A$ (or at least $V \subseteq A'$, the integral closure of $A$).

The idea: Choose a sequence of elements $z_n \in V$ such that $v(z_n) = r_n$ where $r_n$ is a strictly decreasing sequence of positive elements of $\Gamma$ converging to 0. Then the ideals $(z_1) \subset (z_1, z_2) \subset (z_1, z_2, z_3) \subset \cdots$ form a strictly ascending chain in $V$, showing $V$ is not Noetherian. But we need these $z_n$ to be integral over $A$.

Actually, I think the cleaner approach is:

Let $R = k[x, y]_{(x,y)}$, the localization of $k[x,y]$ at the maximal ideal $(x,y)$. This is a 2-dimensional Noetherian local domain. Its integral closure in $k(x,y)$ is... well, $k[x,y]$ is already integrally closed (it's a UFD), so $R$ is integrally closed. That doesn't help.

We need a non-integrally-closed Noetherian domain. 

Let me think about this differently. The construction should produce a Noetherian domain $A$ that is NOT integrally closed, and whose integral closure $A'$ is not Noetherian.

Here's the idea: Take a subring of $V$ (the valuation ring above) that is Noetherian but whose integral closure contains $V$ (or equals $V$).

Since $V$ is a valuation ring, it's integrally closed. So if we can find a Noetherian subring $A \subseteq V$ such that $A' = V$ (or $V \subseteq A'$), and $\dim(A) = 2$, we're done.

But wait, if $A \subseteq V$ and $V$ is integral over $A$, then $\dim(A) = \dim(V) = 1$ (since $V$ is a valuation ring of rank 1, hence dimension 1). That gives dimension 1, not 2.

So we need a different approach for dimension 2.

For dimension 2, the construction needs to be more elaborate. Let me recall...

I think the key is to use a 2-dimensional ring and a valuation that is centered on it but whose valuation ring is not Noetherian, and then construct a subring whose integral closure is the valuation ring (or contains it in a way that makes the integral closure non-Noetherian).

Actually, I recall now. The standard example for dimension 2 is due to Akizuki (1935). Let me try to recall it.

Akizuki's example: Let $k$ be a field, $x$ an indeterminate. Consider $k[[x]]$ and its fraction field $k((x))$. Choose an element $y \in k((x))$ that is transcendental over $k(x)$... no, $k((x))$ might have larger transcendence degree.

Hmm, actually, let me think about this more carefully using a known construction.

**A cleaner approach using Nagata's example:**

Let $k$ be a field. Let $K = k(x, y)$ where $x, y$ are algebraically independent. 

Consider a valuation $v$ on $K$ defined as follows. Let $\alpha$ be a positive irrational number. Set $v(x) = 1$, $v(y) = \alpha$. This gives a rank-1 valuation on $K$ with value group $\mathbb{Z} + \mathbb{Z}\alpha \subset \mathbb{R}$ (dense, hence not discrete).

The valuation ring $V$ of $v$ is a 1-dimensional integrally closed domain that is NOT Noetherian.

Now, the residue field of $V$: The maximal ideal is $\mathfrak{m}_V = \{f : v(f) > 0\}$. The residue field $V/\mathfrak{m}_V$... elements with $v(f) = 0$ are units. The elements $c \in k^*$ have $v(c) = 0$, so $k \subseteq V$ and $k \to V/\mathfrak{m}_V$ is the residue map. Actually, $x$ has $v(x) = 1 > 0$, so $x \in \mathfrak{m}_V$. And $y$ has $v(y) = \alpha > 0$, so $y \in \mathfrak{m}_V$. So the residue field is just $k$ (assuming $k$ is algebraically closed in $K$... well, $V/\mathfrak{m}_V = k$ since any element of $k(x,y)$ with $v = 0$ that's a unit... hmm, this needs more care).

OK, this is getting complicated. Let me try to use a more concrete and well-documented construction.

**Nagata's 2-dimensional example (from Local Rings, Example in Appendix):**

I recall that the construction goes roughly as follows:

1. Start with a field $k$ and a 2-dimensional regular local ring, like $R = k[[x, y]]$.
2. Construct a subring $A$ of $R$ (or of its fraction field) that is Noetherian, 2-dimensional, but whose integral closure is not Noetherian.

The specific construction uses the idea of "gluing" or creating a ring where the integral closure picks up an infinite ascending chain.

Let me try a specific construction that I'm more confident about:

**Construction using a 1-dimensional non-Noetherian valuation and a 2-dimensional base:**

Let $k$ be a field. Let $t$ be an indeterminate. Consider $K_0 = k(t)$ and the $t$-adic valuation $v_0$ on $K_0$ (so $v_0(t) = 1$), with valuation ring $V_0 = k[t]_{(t)}$ (or $k[[t]]$).

Now let $y$ be another indeterminate, and consider $K = k(t, y) = K_0(y)$. Extend $v_0$ to a valuation $v$ on $K$ by defining $v(y) = \alpha$ for some positive irrational $\alpha$. 

Wait, but we need to be more careful. We can define $v$ on $k(t)[y]$ by $v(\sum a_i y^i) = \min_i (v_0(a_i) + i\alpha)$ and extend to $K = k(t, y)$. The value group is $\mathbb{Z} + \mathbb{Z}\alpha$, which is dense in $\mathbb{R}$.

The valuation ring $V$ of $v$ on $K$ is 1-dimensional and not Noetherian.

Now, to get a 2-dimensional example, we can use the following trick:

Consider the ring $A = k + \mathfrak{m}_V$, i.e., the set of elements of $V$ whose residue is in $k$... but that's still 1-dimensional.

Hmm. Let me think about this differently.

Actually, I think the right approach for a 2-dimensional counterexample is:

Take $A$ to be a 2-dimensional Noetherian local domain, and show its integral closure $A'$ is not Noetherian. The 2-dimensionality comes from the fact that $A$ has two "directions" — one from the base field and one from the valuation.

Here's a construction I'm fairly confident about:

Let $k$ be a field, $x, y$ indeterminates. Let $\alpha$ be a positive irrational number. Define $v$ on $k(x, y)$ by $v(x) = 1, v(y) = \alpha$ (as before). Let $V$ be the valuation ring.

Now consider the subring $A = k[x, y]_{(x,y)} \cap V$... no, $k[x,y]_{(x,y)}$ is already contained in $V$ since $v(x) = 1 > 0$ and $v(y) = \alpha > 0$ means $x, y \in \mathfrak{m}_V$, so all polynomials with zero constant term are in $\mathfrak{m}_V$, and units of $k[x,y]_{(x,y)}$ (polynomials with nonzero constant term) have $v = 0$ so are in $V$. So $k[x,y]_{(x,y)} \subseteq V$.

But $k[x,y]_{(x,y)}$ is integrally closed (it's a regular local ring, hence normal). So its integral closure is itself. That doesn't help.

We need a non-normal subring. Let me think...

OK here's the key idea. We need to construct a Noetherian domain $A$ of dimension 2 that is contained in $V$ (or whose integral closure relates to $V$) such that $A$ is NOT integrally closed and its integral closure is not Noetherian.

One way: Take $A$ to be a subring of $V$ generated by elements that are "close to" being a Noetherian ring but whose integral closure is $V$ (or contains $V$).

Since $V$ is 1-dimensional and we want $A$ to be 2-dimensional, we can't have $V$ as the integral closure of $A$ (integral extensions preserve dimension). So the integral closure $A'$ of $A$ must be 2-dimensional and not Noetherian.

So we need $A'$ to be a 2-dimensional integrally closed domain that is not Noetherian, and $A$ to be a Noetherian subring of $A'$ with $A'$ integral over $A$.

Hmm, this is the crux. How do we get a 2-dimensional non-Noetherian integrally closed domain as the integral closure of a Noetherian domain?

I think the construction goes like this:

1. Take a 1-dimensional non-Noetherian valuation ring $V$ (as above, with dense value group).
2. Take a 1-dimensional Noetherian domain $B$ (like $k[[z]]$ for some $z$).
3. Form a "composite" or "fiber product" type construction to get a 2-dimensional ring.

Actually, here's a cleaner idea. Let me use the following construction:

Let $k$ be a field. Let $V$ be a 1-dimensional valuation ring with fraction field $L$, not Noetherian (e.g., $V$ has dense value group). Let $z$ be an indeterminate over $L$. 

Consider $A = V + zL[z]_{(z)}$... no, this is getting complicated.

Let me try the approach from Matsumura's "Commutative Algebra" or other standard references.

Actually, I recall now that the standard example is as follows:

**Nagata's example (2-dimensional):**

Let $k$ be a field, and let $x, y$ be indeterminates. Let $\alpha_1, \alpha_2, \ldots$ be a sequence of positive rational numbers converging to an irrational number $\alpha$ (or just a strictly increasing sequence bounded above).

Hmm, I think I should look at this from a higher level and present the argument more carefully.

Let me recall the precise construction from Nagata's book. I believe it's in the appendix of "Local Rings."

The construction (as I recall it):

Let $k$ be a field of characteristic 0. Let $K = k(x, y)$ where $x, y$ are algebraically independent over $k$. 

Choose an irrational number $\alpha > 0$. Define a valuation $v$ on $K$ by $v(x) = 1, v(y) = \alpha$. The valuation ring $V$ has value group $\mathbb{Z} + \mathbb{Z}\alpha$, which is not discrete.

Now, choose a sequence of positive rational numbers $r_1 > r_2 > r_3 > \cdots$ converging to 0, with each $r_n \in \mathbb{Z} + \mathbb{Z}\alpha$. (This is possible since the value group is dense.)

For each $n$, choose $z_n \in K$ with $v(z_n) = r_n$. For instance, $z_n = x^{a_n} y^{b_n}$ where $a_n + b_n \alpha = r_n$.

Now, the elements $z_n$ are in $V$ and $v(z_n) \to 0$. The ideals $I_n = (z_1, \ldots, z_n) \cdot V$ form a strictly ascending chain (since $v(z_{n+1}) < v(z_n)$ and the value group is dense, so $z_{n+1} \notin I_n$). This shows $V$ is not Noetherian.

Now, we need to construct a Noetherian subring $A$ of $V$ (or of $K$) of dimension 2 whose integral closure is not Noetherian.

The idea: Let $A$ be a subring of $V$ such that:
- $A$ is Noetherian and 2-dimensional
- The $z_n$ are integral over $A$
- The integral closure $A'$ of $A$ contains $V$ (or at least contains all $z_n$ in a way that creates an infinite ascending chain)

For the $z_n$ to be integral over $A$, each $z_n$ should satisfy a monic polynomial with coefficients in $A$.

Here's the specific construction:

Let $A = k + \mathfrak{m}$ where $\mathfrak{m}$ is the maximal ideal of $V$... no, this gives a 1-dimensional ring.

OK, I think I need to use a different approach. Let me think about the 2-dimensional case more carefully.

**The 2-dimensional construction:**

I think the right construction is:

Let $k$ be a field, $x, y$ indeterminates over $k$. Let $v$ be the valuation on $k(x, y)$ with $v(x) = 1, v(y) = \alpha$ (irrational $\alpha > 0$), and $V$ the valuation ring.

The residue field of $V$ is $k$ (elements with $v = 0$ that are units; the only such elements in $k(x,y)$ with $v = 0$ are... well, constants in $k$ and ratios like $x^a y^b / x^c y^d$ with $a + b\alpha = c + d\alpha$, which since $\alpha$ is irrational means $a = c, b = d$, so just elements of $k$). So $\kappa(V) = k$.

Now, the dimension of $V$ is 1 (it's a rank-1 valuation ring).

To get a 2-dimensional example, we can use the following trick: Let $z$ be a new indeterminate, and work in $K(z) = k(x, y, z)$. Extend $v$ to $K(z)$ by setting $v(z) = 0$ and $v(\sum a_i z^i) = \min_i v(a_i)$ (i.e., $z$ is a unit and the Gauss extension). Then the valuation ring $W$ of this extended valuation has residue field $k(z)$ (the residue of $z$ is transcendental over $k$). So $W$ is 1-dimensional with residue field $k(z)$, which has transcendence degree 1 over $k$.

Now, consider the subring $A = k[x, y, z]_{(x, y, z)} \cap W$... but $k[x,y,z]_{(x,y,z)} \subseteq W$ since $v(x) = 1 > 0, v(y) = \alpha > 0, v(z) = 0$ (so $z$ is a unit in $W$, and $z$ is not in the maximal ideal of $k[x,y,z]_{(x,y,z)}$... wait, $z$ IS in the maximal ideal $(x,y,z)$ of $k[x,y,z]_{(x,y,z)}$).

Hmm, this is getting complicated. Let me try yet another approach.

Actually, I think the cleanest way to present this is to use the following well-known result and construction:

**Theorem (Akizuki, 1935; Nagata):** There exists a 2-dimensional Noetherian local domain whose integral closure is not Noetherian.

**Construction:** 

Let me use the construction from Nagata's "Local Rings" (1962), which I'll try to reconstruct.

Let $k$ be a field. Let $K = k((t))$ be the field of formal Laurent series. The $t$-adic valuation $v$ on $K$ has valuation ring $k[[t]]$, a DVR.

Now, $K$ has infinite transcendence degree over $k(t)$ (assuming $k$ is not too large). Choose elements $x_1, x_2, \ldots \in K$ that are algebraically independent over $k(t)$.

Actually, I think the standard construction is more specific. Let me try to recall it from Matsumura or Eisenbud.

Hmm, let me try a different, more concrete approach. I'll use the following construction which I'm fairly confident is correct:

**Step 1:** Let $k$ be a field, $t$ an indeterminate. Let $V = k[[t]]$, a DVR with fraction field $K_0 = k((t))$ and uniformizer $t$.

**Step 2:** Let $y$ be an element of $K_0$ that is transcendental over $k(t)$. For example, $y = \sum_{n=0}^{\infty} t^{n!}$ (which is transcendental over $k(t)$ by a standard result).

**Step 3:** Let $L = k(t, y) \subset K_0$. The restriction of the $t$-adic valuation to $L$ gives a discrete valuation $w$ on $L$ with valuation ring $V_L = L \cap V$.

**Step 4:** Now, $V_L$ is a DVR (since $w$ is a discrete valuation on $L$), with residue field containing $k$ and fraction field $L$.

**Step 5:** Consider the ring $A = k[t, y]_{(t, y)}$... but wait, $y \in k[[t]]$, so $y$ is a power series in $t$. The ring $k[t, y]$ is a subring of $k[[t]]$. Since $y$ is transcendental over $k(t)$, $k[t, y]$ is a polynomial ring in two variables (well, $k[t, y] \cong k[T, Y]$ as a ring since $t$ and $y$ are algebraically independent over $k$... wait, $t$ and $y$ are algebraically independent over $k$ means $k[t, y] \cong k[T, Y]$).

So $A = k[t, y]_{(t, y)}$ is a 2-dimensional regular local ring, hence integrally closed. Its integral closure is itself. That doesn't give us a counterexample.

We need $A$ to NOT be integrally closed. So we need to take a subring of $k[t, y]$ (or some other ring) that is Noetherian, 2-dimensional, but not integrally closed, with non-Noetherian integral closure.

OK, let me try the actual Nagata construction. I'll look at this from the perspective of what I know about the structure.

The key insight is: we need a Noetherian domain $A$ of dimension 2 whose integral closure $A'$ is not a finitely generated $A$-module (and in fact not Noetherian).

By the Krull-Akizuki theorem, this can't happen in dimension 1. In dimension 2, it can.

The construction uses the following idea: Create a 2-dimensional Noetherian local domain $(A, \mathfrak{m})$ such that the integral closure $A'$ has an infinite ascending chain of prime ideals (or ideals), making it non-Noetherian.

Here's a construction I'm now fairly confident about, based on Nagata:

**Setup:** Let $k$ be a field. Let $x, y$ be indeterminates over $k$. Consider $R = k[x, y]_{(x, y)}$, a 2-dimensional regular local ring with fraction field $K = k(x, y)$.

**Valuation:** Let $\alpha$ be a positive irrational number. Define a valuation $v$ on $K$ by $v(x) = 1, v(y) = \alpha$. The valuation ring $V$ of $v$ has value group $\Gamma = \mathbb{Z} + \mathbb{Z}\alpha \subset \mathbb{R}$, which is dense (not discrete), so $V$ is not Noetherian.

**Key observation:** $R \subseteq V$ (since $v(x) > 0, v(y) > 0$, so $x, y \in \mathfrak{m}_V$, and elements of $R$ are fractions $f/g$ with $f, g \in k[x,y]$ and $g(0,0) \neq 0$, so $v(g) = 0$ and $v(f/g) = v(f) \geq 0$).

**Constructing $A$:** We want a Noetherian subring $A$ of $K$ with $A \subseteq V$, $\dim A = 2$, and $A' \supseteq V$ (so $A'$ is not Noetherian).

But as I noted, if $A \subseteq V$ and $V$ is integral over $A$, then $\dim A = \dim V = 1$, not 2. So we can't have $V$ integral over $A$ with $\dim A = 2$.

So the integral closure $A'$ of $A$ is not $V$ itself, but rather some 2-dimensional ring that contains $V$ (or parts of $V$) and is not Noetherian.

Hmm, let me reconsider. Maybe the construction is different from what I'm thinking.

Let me try to think about this from the perspective of the actual known counterexample.

I recall that in Nagata's example, the construction involves:

1. A field $k$ and a formal power series ring $k[[x_1, \ldots, x_n]]$.
2. A subring constructed by "analytically gluing" or using composite valuations.

Actually, let me try a completely different and more concrete approach. Here's a construction I've seen:

**Nagata's counterexample (concrete version):**

Let $k$ be a field of characteristic 0. Let $t$ be an indeterminate. Consider the DVR $V_0 = k[[t]]$ with fraction field $K_0 = k((t))$.

Choose a sequence of elements $a_n \in k[[t]]$ (for $n = 1, 2, 3, \ldots$) such that $a_n$ has order $r_n$ (i.e., $a_n = c_n t^{r_n} + \text{higher order terms}$) where $r_n$ is a strictly increasing sequence of positive integers.

Hmm, but with integer orders, $k[[t]]$ is Noetherian, so this doesn't directly help.

I think the issue is that I need to use a non-discrete valuation, not the $t$-adic one.

Let me try the following approach, which I believe is closer to the actual construction:

**Construction:**

Let $k$ be a field. Let $x, y$ be indeterminates. Let $K = k(x, y)$.

Let $\alpha$ be a positive irrational number. Define $v$ on $K$ by $v(x) = 1, v(y) = \alpha$. Let $V$ be the valuation ring (not Noetherian, as the value group $\mathbb{Z} + \mathbb{Z}\alpha$ is dense).

Now, the residue field of $V$ is $k$ (as argued before).

Consider the ring $A = k + \mathfrak{m}_V$ where $\mathfrak{m}_V$ is the maximal ideal of $V$. Then:
- $A$ consists of elements of $V$ whose residue is in $k$ (which is all of $V$ since the residue field IS $k$). So $A = V$. That doesn't help.

OK so the residue field being $k$ means $k + \mathfrak{m}_V = V$.

Let me try a different valuation. Let $v$ be a valuation on $K = k(x, y)$ with $v(x) = 1, v(y) = 0$ and $v|_k = 0$, but where the residue field of $v$ is $k(y)$ (not just $k$). This is the valuation that sends $x \to 0$ and keeps $y$ as a transcendental residue.

Specifically, $v$ is the $(x)$-adic valuation on $k(y)[x]$ extended to $k(x, y) = k(y)(x)$. This gives $v(x) = 1, v(y) = 0$, and the valuation ring $V$ has residue field $k(y)$. The value group is $\mathbb{Z}$, so $V$ is a DVR. This is Noetherian, so not useful.

To get a non-Noetherian valuation with residue field of transcendence degree 1, we need a non-discrete valuation whose residue field is $k(y)$ (or similar).

Here's the idea: Use a composite valuation. First apply the $x$-adic valuation (residue field $k(y)$), then apply a non-discrete valuation on the residue field $k(y)$.

Let me make this precise. Let $K = k(x, y)$. Consider the $x$-adic valuation $v_1$ on $K$ (with $v_1(x) = 1, v_1(y) = 0$), giving valuation ring $V_1$ with residue field $k(y)$ and value group $\mathbb{Z}$.

Now, on the residue field $k(y)$, choose a non-discrete valuation $v_2$ with value group $\mathbb{Z} + \mathbb{Z}\alpha$ (dense) for some irrational $\alpha > 0$. For instance, $v_2$ is defined by $v_2(y - c) = $ something... actually, let $v_2$ be the valuation on $k(y)$ defined by $v_2(y) = \alpha$ (extending the trivial valuation on $k$). This gives value group $\mathbb{Z} + \mathbb{Z}\alpha$.

The composite valuation $v = v_1 \circ v_2$ (first $v_1$, then $v_2$ on the residue) is a rank-2 valuation on $K$. Its valuation ring $V$ has dimension 2 (rank 2 valuation ring).

The value group of $v$ is $\mathbb{Z} \times (\mathbb{Z} + \mathbb{Z}\alpha)$ with lex ordering. This is a rank-2 group.

$V$ is a 2-dimensional valuation ring, and it's not Noetherian (since the value group is not finitely generated, or more precisely, the second component is not discrete).

Now, $V$ is integrally closed (all valuation rings are). If we can find a Noetherian subring $A$ of $V$ with $\dim A = 2$ and $A' = V$ (or $A' \supseteq V$), then $A'$ is not Noetherian, giving our counterexample.

But can we find such an $A$? The issue is that $V$ is a rank-2 valuation ring, and we need a Noetherian subring over which $V$ is integral.

Actually, for a rank-2 valuation ring $V$ with fraction field $K$, we can often find a Noetherian subring $A$ of $V$ with $\dim A = 2$ such that $V$ lies over $A$ (i.e., $V$ dominates $A$), but $V$ being integral over $A$ is a stronger condition.

Hmm, I think the actual construction is more subtle. Let me try to recall the precise statement and construction.

Actually, I think the key theorem is:

**Theorem (Nagata):** Let $k$ be a field. There exists a 2-dimensional Noetherian local domain $(A, \mathfrak{m})$ containing $k$ whose integral closure $A'$ is not a finitely generated $A$-module (and in fact is not Noetherian).

The construction uses the following:

Let $k$ be a field. Let $K = k(x, y)$ with $x, y$ algebraically independent. Let $v$ be a valuation on $K$ defined as follows:

Choose a positive irrational $\alpha$. Define $v$ on $k[x, y]$ by $v(\sum c_{ij} x^i y^j) = \min\{i + j\alpha : c_{ij} \neq 0\}$, and extend to $K$.

The valuation ring $V$ has value group $\mathbb{Z} + \mathbb{Z}\alpha$ (dense, rank 1), so $V$ is 1-dimensional and not Noetherian.

Now, the center of $v$ on $R = k[x, y]_{(x, y)}$ is $\mathfrak{m} = (x, y)R$ (since $v(x) > 0, v(y) > 0$). So $V$ dominates $R$.

But $R$ is integrally closed (regular local ring), so $R' = R$, and $V \supsetneq R$ but $V$ is not integral over $R$ (since $R$ is already integrally closed and $V \neq R$).

So this doesn't directly give us the counterexample. We need a non-integrally-closed Noetherian subring.

I think the actual construction modifies $R$ to make it non-integrally-closed while keeping it Noetherian, and such that its integral closure is "large" (contains $V$ or something like $V$).

Here's the idea: Take a subring $A$ of $R = k[x, y]_{(x,y)}$ (or of $K$) that is Noetherian, 2-dimensional, not integrally closed, and whose integral closure $A'$ is not Noetherian.

One way to do this: Choose elements $z_1, z_2, \ldots \in V \setminus R$ that are integral over some Noetherian subring $A$ of $R$, and such that the $z_n$ generate an infinite ascending chain of ideals in $A'$.

For $z_n$ to be integral over $A$, we need $z_n$ to satisfy a monic polynomial with coefficients in $A$.

Here's a specific construction:

Let $\alpha > 0$ be irrational. Let $r_n$ be a strictly decreasing sequence of positive elements of $\mathbb{Z} + \mathbb{Z}\alpha$ converging to 0. For instance, since $\alpha$ is irrational, by the theory of continued fractions, there exist integers $p_n, q_n$ with $|p_n - q_n \alpha| \to 0$. So we can take $r_n = |p_n - q_n \alpha|$ (or $p_n - q_n\alpha$ if positive).

For each $n$, let $z_n = x^{p_n} / y^{q_n}$ (assuming $p_n - q_n \alpha > 0$, so $v(z_n) = p_n - q_n\alpha = r_n > 0$, meaning $z_n \in V$). Or $z_n = y^{q_n} / x^{p_n}$ if $q_n \alpha - p_n > 0$.

Now, $z_n \in K = k(x, y)$ and $v(z_n) = r_n \to 0$. The $z_n$ are in $V$ but not in $R$ (since they involve negative powers of $x$ or $y$).

For $z_n$ to be integral over a subring $A$, we need $z_n$ to satisfy a monic polynomial over $A$. 

If $z_n = x^{p_n} / y^{q_n}$, then $z_n$ is a root of $T^{q_n} y^{q_n \cdot q_n} - x^{p_n \cdot q_n}$... no, that's not right. $z_n = x^{p_n} y^{-q_n}$, so $z_n^{q_n} = x^{p_n q_n} y^{-q_n^2}$, and $z_n$ satisfies $y^{q_n} T - x^{p_n} = 0$, which is not monic.

To make it monic: $z_n$ satisfies $T^{q_n} - x^{p_n q_n} / y^{q_n^2}$... this has coefficient $x^{p_n q_n} / y^{q_n^2}$ which needs to be in $A$.

This is getting complicated. Let me try a different, cleaner construction.

**Cleaner construction using quadratic extensions:**

Let me use the following approach. Let $k$ be a field with $\text{char}(k) \neq 2$. Let $R = k[[x, y]]$ (2-dimensional regular local ring). 

Choose a sequence of elements $f_n \in R$ such that $f_n$ is square-free (or $n$-th-power-free) and the $f_n$ generate an infinite ascending chain in the integral closure.

Actually, here's a cleaner idea. Consider the ring $A = k[[x^2, x^3, y]]$. This is a 2-dimensional Noetherian local domain (it's a subring of $k[[x, y]]$). Its integral closure is $k[[x, y]]$ (since $x = x^3 / x^2$ is in the fraction field, and $x$ satisfies $T^2 - x^2 = 0$ over $A$, so $x$ is integral over $A$; then $k[[x, y]]$ is integral over $A$). And $k[[x, y]]$ is Noetherian. So this gives a Noetherian integral closure. Not a counterexample.

The point is: for "nice" subrings of $k[[x, y]]$, the integral closure is still Noetherian (it's a finitely generated module over the subring, by the excellence of $k[[x, y]]$ or by the theorem of excellence).

The counterexample must use a ring that is NOT excellent, or a more exotic construction.

**Key theorem:** A Noetherian local domain $A$ is **excellent** (or at least **Nagata**, also called **pseudo-excellent**) if and only if the integral closure of $A$ in any finite extension of its fraction field is a finitely generated $A$-module. In particular, for a Nagata domain, the integral closure is Noetherian.

So the counterexample must be a non-Nagata (non-excellent) Noetherian domain.

Nagata constructed the first example of a non-Nagata (non-excellent) Noetherian domain, and this is exactly the example we need.

**Nagata's non-excellent domain:**

The construction (as I recall it now):

Let $k$ be a field of characteristic $p > 0$ (this is important for the construction). Actually, Nagata's original example might work in any characteristic. Let me think...

Actually, I think the construction works as follows:

Let $k$ be a field. Let $K = k(x, y)$ with $x, y$ algebraically independent. 

Let $\alpha$ be a positive irrational number. Define the valuation $v$ on $K$ by $v(x) = 1, v(y) = \alpha$, with valuation ring $V$ (not Noetherian, as value group $\mathbb{Z} + \mathbb{Z}\alpha$ is dense).

The residue field of $V$ is $k$.

Now, $V$ is a 1-dimensional valuation ring. The key idea is to construct a 2-dimensional Noetherian subring $A$ of $K$ such that $V$ is a localization of the integral closure of $A$ (or the integral closure of $A$ contains a copy of $V$ in some sense).

Here's the actual construction (I'm now recalling it more clearly):

**Step 1:** Let $k$ be a field, $x, y$ indeterminates, $K = k(x, y)$. Let $v$ be the valuation with $v(x) = 1, v(y) = \alpha$ (irrational $\alpha > 0$), valuation ring $V$, maximal ideal $\mathfrak{m}_V$.

**Step 2:** Choose a sequence of elements $c_n \in \mathbb{Z} + \mathbb{Z}\alpha$ with $0 < c_1 < c_2 < \cdots$ and $c_n \to \infty$... no, we want $c_n \to 0$ for the ascending chain of ideals.

Actually, for the non-Noetherianity of $V$, we use: since the value group is dense, there exist $r_1 > r_2 > r_3 > \cdots > 0$ with $r_n \in \mathbb{Z} + \mathbb{Z}\alpha$ and $r_n \to 0$. Let $z_n = x^{a_n} y^{b_n}$ with $a_n + b_n \alpha = r_n$. Then $(z_1) \subsetneq (z_1, z_2) \subsetneq (z_1, z_2, z_3) \subsetneq \cdots$ is a strictly ascending chain of ideals in $V$ (since $v(z_{n+1}) < v(z_i)$ for $i \leq n$, so $z_{n+1} \notin (z_1, \ldots, z_n)$).

**Step 3:** Now, we want to construct a Noetherian subring $A$ of $K$ (or of $V$) with $\dim A = 2$ such that the $z_n$ are integral over $A$.

For $z_n = x^{a_n} y^{b_n}$ (where $a_n$ or $b_n$ might be negative), $z_n$ is in $K = k(x, y)$. If $b_n < 0$, then $z_n = x^{a_n} / y^{|b_n|}$, and $z_n$ satisfies the polynomial $y^{|b_n|} T - x^{a_n} = 0$ over $k[x, y]$, but this is not monic.

To make it monic: $z_n$ satisfies $T^{|b_n|} - x^{a_n |b_n|} / y^{|b_n|^2} = 0$... the coefficient is $x^{a_n |b_n|} / y^{|b_n|^2}$, which is in $K$ but not necessarily in $A$.

Alternatively, if $z_n = x^{a_n} / y^{b_n}$ (with $a_n, b_n > 0$ and $a_n - b_n \alpha = r_n > 0$), then $z_n^{b_n} = x^{a_n b_n} / y^{b_n^2}$, and $z_n$ satisfies $y^{b_n^2} T^{b_n} - x^{a_n b_n} = 0$ over $k[x, y]$. This is monic in $T$ if we divide by $y^{b_n^2}$: $T^{b_n} - x^{a_n b_n} / y^{b_n^2} = 0$. But the coefficient $x^{a_n b_n} / y^{b_n^2}$ is not in $k[x, y]$.

So $z_n$ is NOT integral over $k[x, y]$ (since $k[x, y]$ is integrally closed and $z_n \notin k[x, y]$).

We need to choose $A$ to be a non-integrally-closed subring of $k[x, y]$ (or $K$) such that the $z_n$ become integral over $A$.

**The trick:** Make $A$ contain elements like $x^{a_n} / y^{b_n - 1}$ or similar, so that $z_n = x^{a_n} / y^{b_n}$ satisfies a monic polynomial over $A$.

Actually, here's the key idea. If $A$ contains $y$ and $x^{a_n} / y^{b_n - 1}$ (call this $w_n$), then $z_n = w_n / y$ satisfies $y T - w_n = 0$, which is monic if $y$ is a unit... but $y$ is not a unit in the local ring.

Hmm, let me think about this differently.

If $A$ contains $w_n = x^{a_n} / y^{b_n - 1}$ and $y$, then $z_n = w_n / y$ satisfies $T - w_n/y = 0$, i.e., $yT - w_n = 0$. This is not monic. But $z_n$ satisfies $T^{b_n} - (x^{a_n}/y^{b_n})^{b_n-1} \cdot z_n = ...$, no, this is circular.

Let me try: if $z_n = x^{a_n}/y^{b_n}$ and $A$ contains $x^{a_n}$ and $y^{b_n}$, then $z_n$ satisfies $y^{b_n} T - x^{a_n} = 0$, which is monic iff $y^{b_n}$ is a unit in $A$, which it's not (in a local ring where $y$ is in the maximal ideal).

OK, I think the actual construction is more subtle and involves choosing the $z_n$ to be integral over $A$ by making $A$ contain specific elements.

Let me try to recall the actual Nagata construction more carefully. I believe it goes like this:

**Nagata's construction:**

Let $k$ be a field. Let $t$ be an indeterminate. Consider the formal power series ring $k[[t]]$ and its fraction field $k((t))$.

Choose a sequence of elements $u_1, u_2, \ldots \in k[[t]]$ that are algebraically independent over $k$ (this is possible since $k[[t]]$ has uncountable dimension over $k$ when $k$ is countable, or we can always find such elements).

Actually, I think the construction uses specific power series. Let me try:

Let $k$ be a field. Let $x_1, x_2, \ldots$ be countably many indeterminates. Consider the field $K = k(x_1, x_2, \ldots)$ (infinite transcendence degree). 

Actually, this is getting too complicated without being able to look up the reference. Let me try to present the argument at a higher level, citing the known result, and then give the key ideas of the construction.

Actually, wait. Let me reconsider the problem. The question is: "Determine whether the integral closure of a Noetherian integral domain is always Noetherian when the dimension of the domain is 2."

The answer is **NO**. The proof is by counterexample. The most famous counterexample is due to Akizuki (1935) for dimension 2 (and Nagata generalized this).

Let me present the construction more carefully. I'll use the approach from Nagata's book, which I'll try to reconstruct as faithfully as I can.

**Nagata's Example (2-dimensional):**

Let $k$ be a field. Let $K = k(x, y)$ where $x, y$ are algebraically independent over $k$.

Let $\alpha$ be a positive irrational number. Define the valuation $v$ on $K$ by:
$$v\left(\sum c_{ij} x^i y^j\right) = \min\{i + j\alpha : c_{ij} \neq 0\}$$
and extend to $K$ by $v(f/g) = v(f) - v(g)$.

The value group is $\Gamma = \mathbb{Z} + \mathbb{Z}\alpha \subset \mathbb{R}$, which is dense (since $\alpha$ is irrational). The valuation ring $V = \{f \in K : v(f) \geq 0\}$ is a rank-1 valuation ring, hence 1-dimensional, and is NOT Noetherian (since $\Gamma$ is not discrete).

The maximal ideal of $V$ is $\mathfrak{m} = \{f : v(f) > 0\}$, and the residue field is $V/\mathfrak{m} \cong k$.

Now, the key construction: We want to build a 2-dimensional Noetherian subring $A$ of $K$ whose integral closure $A'$ is not Noetherian.

The idea is to use the fact that $V$ is not Noetherian and "embed" this non-Noetherianity into the integral closure of a 2-dimensional Noetherian ring.

**Constructing $A$:**

Let $z$ be a new indeterminate. Consider $K' = K(z) = k(x, y, z)$. Extend $v$ to $K'$ by setting $v(z) = 0$ and using the Gauss extension: $v(\sum a_i z^i) = \min_i v(a_i)$. The valuation ring $W$ of this extended valuation has residue field $k(z)$ (transcendence degree 1 over $k$) and is 1-dimensional (rank 1), not Noetherian.

Now, $\dim W = 1$ and the residue field has transcendence degree 1 over $k$, so by Abhyankar's inequality, the "dimension" of $W$ in terms of $K'/k$ is $\text{tr.deg}(K'/k) - \text{tr.deg}(\kappa(W)/k) = 3 - 1 = 2$... wait, that's the "transcendence degree defect" not the Krull dimension.

Actually, for a valuation ring $W$ of $K' = k(x, y, z)$, the Krull dimension of $W$ equals the rank of the value group, which is 1 (since we used a rank-1 extension). So $\dim W = 1$.

But the residue field $\kappa(W) = k(z)$ has transcendence degree 1 over $k$. And $\text{tr.deg}(K'/k) = 3$. So by Abhyankar's inequality: $\text{rank}(\Gamma) + \text{tr.deg}(\kappa/k) \leq \text{tr.deg}(K'/k)$, i.e., $1 + 1 \leq 3$. OK.

This doesn't directly give us a 2-dimensional ring. Let me reconsider.

Actually, I think the right approach is:

1. Take a 1-dimensional non-Noetherian valuation ring $V$ with fraction field $L$ and residue field $\kappa$.
2. Let $z$ be an indeterminate over $L$.
3. Consider the ring $A = \{f \in L[z]_{(z)} : f(0) \in V\}$, i.e., the set of rational functions in $z$ over $L$ that are defined at $z = 0$ and whose value at $z = 0$ is in $V$. This is $V + zL[z]_{(z)}$.

This ring $A = V + zL[z]_{(z)}$ has dimension $\dim V + 1 = 1 + 1 = 2$ (by the dimension formula for such "composite" rings).

But $A$ is not Noetherian (since $V$ is not Noetherian, and $A$ contains $V$ as a retract).

So this doesn't give a Noetherian $A$. We need a different approach.

**The actual approach:** We need to find a Noetherian subring $A$ of $A' = V + zL[z]_{(z)}$ (or some other 2-dimensional non-Noetherian integrally closed ring) such that $A$ is Noetherian and $A'$ is the integral closure of $A$.

The idea is to "approximate" $V$ by a Noetherian subring.

Let me try the following:

Let $k$ be a field. Let $L = k(y)$ and $V$ be a non-Noetherian valuation ring of $L$ (e.g., the valuation with $v(y) = \alpha$ irrational, value group $\mathbb{Z} + \mathbb{Z}\alpha$).

Let $x$ be an indeterminate over $L$. Consider $K = L(x) = k(x, y)$.

Let $W = V + xL[[x]]$ (the composite of $V$ and the $x$-adic DVR $L[[x]]$). Then $W$ is a 2-dimensional integrally closed local domain (it's the intersection of $V[[x]]$... no, $W = \{f \in L[[x]] : f(0) \in V\}$).

$W$ is not Noetherian (since $V$ is not Noetherian).

Now, consider the subring $A = k[x, y]_{(x, y)}$ of $K = k(x, y)$. We have $A \subseteq W$ (since $k[x, y]_{(x,y)} \subseteq L[x]_{(x)} \subseteq L[[x]]$ and the constant term of any element of $k[x,y]_{(x,y)}$ is in $k \subseteq V$). But $A$ is integrally closed (regular local ring), so $A' = A \neq W$.

We need a non-integrally-closed Noetherian subring of $W$ whose integral closure is $W$ (or contains $W$).

**The key construction:** Let me modify $A$ to make it non-integrally-closed while keeping it Noetherian, and such that its integral closure is $W$ (or at least not Noetherian).

Consider $A = k + (x, y)W = k + \mathfrak{m}_W$ where $\mathfrak{m}_W$ is the maximal ideal of $W$. But the residue field of $W$ is $\kappa(W) = V/\mathfrak{m}_V$... hmm, what is the residue field of $W$?

$W = V + xL[[x]]$. The maximal ideal of $W$ is $\mathfrak{m}_W = \mathfrak{m}_V + xL[[x]]$. The residue field is $W/\mathfrak{m}_W = V/\mathfrak{m}_V = \kappa(V)$.

For our $V$ (valuation with $v(y) = \alpha$ on $L = k(y)$), the residue field $\kappa(V) = k$ (since $v(y) > 0$ means $y \in \mathfrak{m}_V$, and the only elements of $k(y)$ with $v = 0$ are... well, $v(c) = 0$ for $c \in k^*$, and $v(y) = \alpha > 0$, so $v(f/g) = 0$ means $\deg_y$-weighted... actually, $v$ on $k(y)$ is defined by $v(y) = \alpha$ and $v|_k = 0$. So $v(\sum a_i y^i) = \min\{i\alpha : a_i \neq 0\}$. For $v(f/g) = 0$, we need $v(f) = v(g)$. The residue field consists of elements with $v = 0$ modulo elements with $v > 0$. An element $c \in k^*$ has $v(c) = 0$ and its residue is $c$. An element $y$ has $v(y) = \alpha > 0$. So the residue field is $k$.)

So $\kappa(W) = k$, and $k + \mathfrak{m}_W = W$ (since the residue field is $k$, every element of $W$ has residue in $k$). So this doesn't help.

Let me try a different residue field. Use a valuation on $L = k(y)$ whose residue field is larger than $k$.

For instance, let $v$ be the $y$-adic valuation on $k(y)$: $v(y) = 1, v|_k = 0$. Then $V = k[y]_{(y)}$ (or $k[[y]]$ in the completion), which is a DVR (Noetherian). The residue field is $k$. This is Noetherian, not useful.

To get a non-Noetherian valuation with residue field larger than $k$, I need a non-discrete valuation on $k(y)$ whose residue field is not $k$.

Hmm, a rank-1 valuation on $k(y) = k(y)$ (transcendence degree 1) with residue field $\neq k$ would need the residue field to have transcendence degree 0 over $k$ (by Abhyankar: rank + tr.deg(residue) ≤ tr.deg = 1, so if rank = 1, tr.deg(residue) ≤ 0, meaning the residue field is algebraic over $k$). So the residue field is algebraic over $k$, and if $k$ is algebraically closed, the residue field is $k$.

So for $k(y)$ (transcendence degree 1), any rank-1 valuation has residue field algebraic over $k$. To get a residue field of transcendence degree 1, we need a valuation on a field of transcendence degree ≥ 2.

OK so let me use $K = k(x, y)$ (transcendence degree 2). Use a rank-1 non-discrete valuation $v$ on $K$ with residue field of transcendence degree 1 over $k$.

For instance: $v(x) = 1, v(y) = 0$, and $v|_{k(y)} = 0$ (trivial on $k(y)$). Then $v$ is the $x$-adic valuation on $k(y)(x) = K$, which is a DVR (discrete, Noetherian). The residue field is $k(y)$ (transcendence degree 1). But this is Noetherian.

To make it non-discrete: use $v(x) = \alpha$ (irrational) and $v(y) = 0$. Then the value group is $\mathbb{Z}\alpha \cong \mathbb{Z}$ (still discrete!). That's because $v$ only takes values in $\mathbb{Z}\alpha$ on $k(y)[x]$ (since $v(x^i) = i\alpha$ and $v|_{k(y)} = 0$), and $v(f/g) = (v(f) - v(g)) \in \mathbb{Z}\alpha$. So the value group is $\mathbb{Z}\alpha \cong \mathbb{Z}$, which is discrete. So $V$ is a DVR. Not useful.

To get a non-discrete valuation on $K = k(x, y)$ with residue field of tr.deg 1: we need a valuation that is non-trivial on both $x$ and $y$ in a way that makes the value group non-discrete, while keeping the residue field large.

For instance: $v(x) = 1, v(y) = \alpha$ (irrational). Value group = $\mathbb{Z} + \mathbb{Z}\alpha$ (dense, non-discrete). Residue field: elements with $v = 0$ are those $f/g$ with $v(f) = v(g)$. Since $v(x) = 1$ and $v(y) = \alpha$ are both $> 0$, both $x$ and $y$ are in $\mathfrak{m}_V$. The residue field is $k$ (as argued before). So tr.deg(residue) = 0.

By Abhyankar: rank(Γ) + tr.deg(κ/k) ≤ tr.deg(K/k) = 2. Here rank = 1, tr.deg(κ) = 0, so $1 + 0 = 1 \leq 2$. OK, there's "room" for a higher-dimensional residue field, but this particular valuation gives residue field $k$.

To get a non-discrete valuation with residue field of tr.deg 1, I need a rank-1 valuation on $K = k(x,y)$ where one of $x, y$ has value 0 and is part of the residue field, while the other generates a non-discrete value group.

But as I showed, if $v(y) = 0$ and $v|_{k(y)} = 0$, then $v$ on $k(y)(x)$ with $v(x) = \alpha$ gives value group $\mathbb{Z}\alpha \cong \mathbb{Z}$ (discrete). To make it non-discrete, I'd need $v$ to be non-trivial on $k(y)$ as well, but then $y$ wouldn't be in the residue field.

Alternatively, use a higher-rank valuation. A rank-2 valuation on $K = k(x, y)$ can have residue field of tr.deg 1 and be non-discrete.

For instance: the composite valuation. First, the $x$-adic valuation $v_1$ on $K$ (with $v_1(x) = 1, v_1(y) = 0$, residue field $k(y)$). Then, a non-discrete valuation $v_2$ on the residue field $k(y)$ (e.g., $v_2(y) = \alpha$ irrational). The composite $v = v_1 \circ v_2$ is a rank-2 valuation on $K$ with value group $\mathbb{Z} \times (\mathbb{Z} + \mathbb{Z}\alpha)$ (lex order).

The valuation ring $V$ of this composite valuation is 2-dimensional (rank 2). It's not Noetherian (since the value group is not finitely generated / the second component is non-discrete).

The residue field of $V$ (the rank-2 valuation ring) is the residue field of $v_2$ on $k(y)$, which is $k$ (since $v_2(y) = \alpha > 0$).

The prime ideals of $V$: $V$ has a chain $\mathfrak{m}_V \supsetneq \mathfrak{p} \supsetneq (0)$ where $\mathfrak{p}$ is the prime corresponding to the first component of the valuation. The residue field at $\mathfrak{p}$ is the residue field of $v_1$, which is $k(y)$ (tr.deg 1 over $k$). The residue field at $\mathfrak{m}_V$ is $k$.

So $V$ is a 2-dimensional non-Noetherian valuation ring. 

Now, $V$ is integrally closed (it's a valuation ring). If we can find a Noetherian subring $A$ of $V$ with $\dim A = 2$ and $V$ integral over $A$ (or $A' \supseteq V$), then $A'$ is not Noetherian.

But $V$ being integral over $A$ with $\dim A = 2$ and $\dim V = 2$ is consistent (integral extensions preserve dimension).

The question is: can we find such an $A$?

**Constructing $A$:**

$V$ is a 2-dimensional valuation ring of $K = k(x, y)$. The center of $V$ on $R = k[x, y]_{(x, y)}$ is $\mathfrak{m} = (x, y)$ (since $v_1(x) = 1 > 0$ and $v_1(y) = 0$ but $v_2(y) = \alpha > 0$, so both $x$ and $y$ are in $\mathfrak{m}_V$).

So $R \subseteq V$ and $V$ dominates $R$. But $R$ is integrally closed, so $R' = R \neq V$.

We need a non-integrally-closed Noetherian subring of $V$ (or of $K$) whose integral closure contains $V$.

Here's the idea: Take $A = k[x^2, x^3, y]_{(x^2, x^3, y)}$. This is a 2-dimensional Noetherian local domain (a subring of $k[x, y]_{(x, y)}$). Its integral closure is $k[x, y]_{(x, y)}$ (since $x = x^3/x^2$ is in the fraction field and $x^2 - (x)^2 = 0$ shows $x$ is integral over $A$). But $k[x,y]_{(x,y)}$ is Noetherian. So this doesn't give a non-Noetherian integral closure.

The issue is that $k[x, y]_{(x, y)}$ is excellent (or Nagata), so its integral closure in any finite extension is finitely generated. We need a non-excellent ring.

**Non-excellent rings:** The key is to construct a Noetherian domain that is NOT a Nagata domain (not universally Japanese). Nagata's example of a non-Nagata domain is exactly what we need.

Let me try to recall Nagata's actual construction of a non-excellent (non-Nagata) ring.

I believe the construction is:

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$ with $x, y$ algebraically independent. Let $v$ be a valuation on $K$ with $v(x) = 1, v(y) = \alpha$ (irrational), valuation ring $V$ (non-Noetherian, 1-dimensional).

Now, in characteristic $p$, the Frobenius is useful. Consider the subring $A = k[x^p, y^p, x, y]_{(x, y)}$... no, that's just $k[x, y]_{(x, y)}$.

Hmm, let me think about this differently. In characteristic $p$, if $a$ is an element of the fraction field such that $a^p \in A$, then $a$ is integral over $A$ (since $T^p - a^p = 0$). So we can use the Frobenius to create integral elements.

**Nagata's construction (characteristic $p$):**

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$. Let $v$ be the valuation with $v(x) = 1, v(y) = \alpha$ (irrational), valuation ring $V$.

Choose a sequence $r_n \in \mathbb{Z} + \mathbb{Z}\alpha$ with $r_n \to 0^+$, $r_n > 0$. Let $z_n = x^{a_n} y^{b_n}$ with $a_n + b_n \alpha = r_n$ (so $v(z_n) = r_n$). Some of the $a_n, b_n$ might be negative.

Now, $z_n^p = x^{p a_n} y^{p b_n}$, and $v(z_n^p) = p r_n$. If $a_n, b_n \geq 0$, then $z_n^p \in k[x, y]$, so $z_n$ is integral over $k[x, y]$ (satisfying $T^p - z_n^p = 0$). But if $a_n$ or $b_n$ is negative, $z_n^p \notin k[x, y]$.

Hmm, this only works when $a_n, b_n \geq 0$, which means $z_n \in k[x, y]$, which means $z_n$ is already in $k[x, y]$ and integral over it (trivially). Not useful.

Let me try: $z_n = x^{a_n} / y^{b_n}$ with $a_n, b_n > 0$ and $a_n - b_n \alpha = r_n > 0$. Then $z_n^p = x^{p a_n} / y^{p b_n}$, which is not in $k[x, y]$ (since $b_n > 0$). So $z_n$ is not integral over $k[x, y]$ via the Frobenius.

But if we take $A = k[x, y, z_1^p, z_2^p, \ldots]_{(x, y, z_1^p, \ldots)}$... this is not Noetherian (infinitely many generators).

I think the actual construction is more clever. Let me try to recall it from a different angle.

**The actual Nagata construction (I think this is right):**

Let $k$ be a field of characteristic $p > 0$. Let $t$ be an indeterminate. Consider the formal power series ring $k[[t]]$ and its fraction field $k((t))$.

Choose an element $s \in k[[t]]$ that is transcendental over $k(t)$. (For example, $s = \sum_{n=0}^{\infty} t^{n!}$ is transcendental over $k(t)$ by a standard argument.)

Now, consider the subring $A = k[[t^p, s^p, t, s]]$... no, that's $k[[t, s]]$ which is a 2-dimensional regular local ring (Noetherian, integrally closed).

Hmm. Let me try:

$A = k[[t^p, s]]$. This is a subring of $k[[t, s]]$. Is it Noetherian? $k[[t^p, s]]$ is a formal power series ring in two variables (since $t^p$ and $s$ are algebraically independent over $k$... are they? $t^p \in k[[t]]$ and $s \in k[[t]]$, so both are power series in $t$. They're algebraically independent over $k$ iff there's no polynomial relation $f(t^p, s) = 0$ for $f \in k[X, Y]$. Since $s$ is transcendental over $k(t)$, and $t^p \in k(t)$, $s$ is transcendental over $k(t^p) \supseteq k(t)$... wait, $s$ is transcendental over $k(t)$, and $k(t^p) \subseteq k(t)$, so $s$ is transcendental over $k(t^p)$. So $t^p$ and $s$ are algebraically independent over $k$, and $k[[t^p, s]] \cong k[[X, Y]]$, a 2-dimensional regular local ring. This is Noetherian and integrally closed. Not useful.

Let me try: $A = k + (t^p, s) k[[t^p, s]]$... this is the "glued" ring. But since the residue field of $k[[t^p, s]]$ is $k$, this is just $k[[t^p, s]]$ itself.

OK, I think I need to use a different approach. Let me try to use the approach where we have a non-Noetherian valuation ring and construct a Noetherian subring whose integral closure is the valuation ring.

Actually, I recall now that the key construction uses the following:

**Nagata's example:**

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$ with $x, y$ algebraically independent. Let $v$ be the valuation on $K$ with $v(x) = 1, v(y) = \alpha$ (irrational $\alpha > 0$), valuation ring $V$.

Consider the subring $A = k[x^p, y, x^p y^{-1}, x^{2p} y^{-2}, \ldots]$... no, this has infinitely many generators and is not Noetherian.

Hmm, I think the actual construction is:

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$. Consider the element $z = y/x^{\alpha}$... but $\alpha$ is irrational, so this doesn't make sense algebraically.

OK, I think I'm overcomplicating this. Let me step back and think about what construction would actually work.

**The fundamental idea:**

We want a 2-dimensional Noetherian domain $A$ whose integral closure $A'$ is not Noetherian. The non-Noetherianity of $A'$ comes from an infinite ascending chain of ideals, which in turn comes from a non-discrete valuation that $A'$ "sees."

The construction should:
1. Start with a 2-dimensional Noetherian domain (e.g., a subring of $k[[x, y]]$ or $k[x, y]$).
2. Make it non-integrally-closed by removing some elements.
3. The integral closure should "recover" those elements plus infinitely many more, creating a non-Noetherian ring.

**A concrete construction (I'll try this one):**

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$ with $x, y$ algebraically independent.

Let $\alpha$ be a positive irrational number. Define $v$ on $K$ by $v(x) = 1, v(y) = \alpha$.

Choose a sequence of pairs $(a_n, b_n) \in \mathbb{Z}^2$ with $a_n + b_n \alpha > 0$ and $a_n + b_n \alpha \to 0$ as $n \to \infty$. (This is possible since $\mathbb{Z} + \mathbb{Z}\alpha$ is dense in $\mathbb{R}$.)

Let $z_n = x^{a_n} y^{b_n}$ (where if $a_n < 0$ or $b_n < 0$, we interpret this as $x^{a_n} y^{b_n} \in K$). So $v(z_n) = a_n + b_n \alpha = r_n > 0$, meaning $z_n \in V$ (the valuation ring).

Now, the key: in characteristic $p$, $z_n^p = x^{p a_n} y^{p b_n}$, and $v(z_n^p) = p r_n$. If we can arrange that $z_n^p \in A$ for some Noetherian ring $A$, then $z_n$ is integral over $A$ (root of $T^p - z_n^p$).

For $z_n^p = x^{p a_n} y^{p b_n}$ to be in $A$, we need $A$ to contain $x^{p a_n} y^{p b_n}$ for all $n$. If $a_n, b_n \geq 0$, then $x^{p a_n} y^{p b_n} \in k[x^p, y^p] \subseteq k[x, y]$. But we also need $z_n \notin A$ (otherwise $z_n$ is trivially in $A$ and doesn't create new elements in the integral closure).

If $a_n > 0, b_n < 0$: $z_n = x^{a_n} / y^{|b_n|}$, and $z_n^p = x^{p a_n} / y^{p |b_n|}$. For $z_n^p \in A$, we need $A$ to contain $x^{p a_n} / y^{p |b_n|}$.

If $A = k[x^p, y^p]_{(x^p, y^p)}$, then $x^{p a_n} / y^{p |b_n|} \notin A$ (since $y^{p |b_n|}$ is not a unit). So this doesn't work.

What if $A$ contains $1/y^p$? Then $A$ would contain $K = k(x, y)$ (since $y = y^p \cdot (1/y^{p-1})$... no, $1/y^{p-1}$ is not necessarily in $A$). Actually, if $A$ contains $y^p$ and $1/y^p$, then $y^p$ is a unit, and $A$ contains $k[x^p, y^p, 1/y^p] = k[x^p, y^p, y^{-p}]$. But this is not a local ring, and it might not be Noetherian in the way we want.

I think the actual construction is more subtle. Let me try to recall it from the literature.

**Actually, I think the correct construction is as follows (Nagata, "Local Rings", Example 5 in Appendix):**

Let $k$ be a field. Let $K = k(x, y)$ with $x, y$ algebraically independent over $k$. 

Let $v$ be a discrete valuation on $K$ (the $x$-adic valuation: $v(x) = 1, v(y) = 0$, residue field $k(y)$). Let $V_1$ be the valuation ring of $v$ (a DVR with residue field $k(y)$).

On the residue field $k(y)$, let $w$ be a non-discrete valuation with $w(y) = \alpha$ (irrational), valuation ring $V_2$ (non-Noetherian, residue field $k$).

The composite valuation $v \circ w$ gives a rank-2 valuation ring $V$ on $K$, which is 2-dimensional and not Noetherian.

Now, $V$ has a prime ideal $\mathfrak{p}$ (the height-1 prime) such that $V_\mathfrak{p} = V_1$ (a DVR) and $V/\mathfrak{p} \cong V_2$ (non-Noetherian).

The non-Noetherianity of $V$ comes from $V/\mathfrak{p} \cong V_2$ being non-Noetherian (the ideals of $V_2$ lift to ideals of $V$ containing $\mathfrak{p}$).

Now, we want a Noetherian subring $A$ of $V$ with $\dim A = 2$ and $A' \supseteq V$.

Since $V$ is a valuation ring of $K = k(x, y)$, and $R = k[x, y]_{(x, y)} \subseteq V$ (as $v(x) = 1 > 0$ and $w(y \mod v) = \alpha > 0$ so $y \in \mathfrak{m}_V$), $V$ dominates $R$.

$R$ is integrally closed, so $R' = R$. We need a non-integrally-closed subring.

**The construction of $A$:**

Let $k$ be a field of characteristic $p > 0$. Consider $R = k[x, y]_{(x, y)}$ and its subring $A = k[x^p, y]_{(x^p, y)}$... wait, is this Noetherian?

$A = k[x^p, y]_{(x^p, y)}$. Since $x^p$ and $y$ are algebraically independent over $k$ (because $x$ and $y$ are, and $x^p$ is just $x$ raised to the $p$-th power), $k[x^p, y] \cong k[X, Y]$, so $A \cong k[X, Y]_{(X, Y)}$, a 2-dimensional regular local ring. This is Noetherian and integrally closed. Not useful.

What about $A = k[x^p, y^p, xy]_{(x^p, y^p, xy)}$? In characteristic $p$, $(xy)^p = x^p y^p$, so $xy$ satisfies $T^p - x^p y^p = 0$ over $k[x^p, y^p]$. So $xy$ is integral over $k[x^p, y^p]$. The ring $A = k[x^p, y^p, xy]$ is a finitely generated $k[x^p, y^p]$-algebra (generated by $xy$), so it's Noetherian. Its dimension is 2 (same as $k[x^p, y^p]$). The integral closure of $A$ is $k[x, y]$ (since $x = (xy) \cdot y^{p-1} / y^p$... hmm, $x = (xy) / y$, and $y$ satisfies $T^p - y^p = 0$ over $A$, so $y$ is integral over $A$, and then $x = xy/y$ is in the fraction field and integral over $A$ (since $x^p \in A$)). So $A' = k[x, y]_{(x, y)}$ (or $k[x, y]$), which is Noetherian. Still not a counterexample.

I think the issue is that all these "algebraic" constructions give Noetherian integral closures because they're dealing with finite extensions. The counterexample requires an infinite extension or a non-finitely-generated integral closure.

Let me try the following approach, which I think is closer to the actual construction:

**Nagata's construction (final attempt):**

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$ with $x, y$ algebraically independent.

Let $\alpha$ be a positive irrational number. Define $v$ on $K$ by $v(x) = 1, v(y) = \alpha$. Let $V$ be the valuation ring (non-Noetherian, 1-dimensional, residue field $k$).

Since $\mathbb{Z} + \mathbb{Z}\alpha$ is dense in $\mathbb{R}$, we can find a sequence $(a_n, b_n) \in \mathbb{Z}_{\geq 0}^2$ with $r_n = a_n + b_n \alpha$ strictly decreasing to 0, with $r_n > 0$. (We need $a_n, b_n \geq 0$ so that $z_n = x^{a_n} y^{b_n} \in k[x, y]$.)

Wait, but if $a_n, b_n \geq 0$ and $r_n = a_n + b_n\alpha \to 0$ with $r_n > 0$, then since $a_n, b_n \geq 0$ and $\alpha > 0$, we need $a_n \to 0$ and $b_n \to 0$, but $a_n, b_n$ are non-negative integers, so eventually $a_n = b_n = 0$, giving $r_n = 0$. Contradiction. So we can't have $a_n, b_n \geq 0$ with $r_n \to 0^+$.

So we need $a_n$ or $b_n$ to be negative. Say $b_n < 0$: $z_n = x^{a_n} / y^{|b_n|}$ with $a_n - |b_n| \alpha = r_n > 0$, $r_n \to 0$. This is possible: by the theory of continued fractions, there exist $a_n, b_n > 0$ with $|a_n - b_n \alpha| \to 0$, and we can arrange $a_n - b_n \alpha > 0$ (i.e., $a_n/b_n > \alpha$, the convergents from above). So $z_n = x^{a_n} / y^{b_n}$ with $v(z_n) = a_n - b_n \alpha = r_n > 0 \to 0$.

Now, $z_n \in V$ (since $v(z_n) > 0$) but $z_n \notin k[x, y]$ (since $b_n > 0$ means $y^{b_n}$ is in the denominator).

In characteristic $p$: $z_n^p = x^{p a_n} / y^{p b_n}$. This is also not in $k[x, y]$.

But $z_n^{p b_n} = x^{p a_n b_n} / y^{p b_n^2}$. Still not in $k[x, y]$.

Hmm, the Frobenius doesn't help here because the negative powers of $y$ persist.

**Alternative approach using a different ring:**

What if instead of $k[x, y]$, we use a ring that already contains $1/y$? For instance, $k[x, y, 1/y] = k[x, y, y^{-1}]$. But this is not a local ring, and its localizations might not give us what we want.

Or: use $k[[x]][y, 1/y]$... this is getting complicated.

Let me try yet another approach. I think the actual Nagata construction uses formal power series and goes like this:

**Nagata's construction (using formal power series):**

Let $k$ be a field of characteristic $p > 0$. Let $t$ be an indeterminate. Consider $k[[t]]$, a DVR with fraction field $k((t))$.

Let $s = \sum_{i=1}^{\infty} c_i t^{r_i}$ be a formal power series in $k[[t]]$ where $r_i$ is a strictly increasing sequence of positive integers, chosen so that $s$ is transcendental over $k(t)$.

Now, consider the subring $A = k[[t^p, s^p, t \cdot s]]$ of $k[[t, s]]$... hmm, I need to think about what this looks like.

Actually, I think the construction is:

Let $k$ be a field of characteristic $p > 0$. Let $R = k[[x, y]]$ (2-dimensional regular local ring). Consider the subring $A = k[[x^p, y]]$... this is $k[[X, Y]]$ (since $x^p, y$ are algebraically independent), a 2-dimensional regular local ring, integrally closed. Not useful.

What about $A = k[[x^p, y^p, x + y]]$? In characteristic $p$, $(x+y)^p = x^p + y^p$, so $x + y$ satisfies $T^p - x^p - y^p = 0$ over $k[[x^p, y^p]]$. So $A = k[[x^p, y^p, x+y]]$ is a finite module over $k[[x^p, y^p]]$ (generated by $1, x+y, (x+y)^2, \ldots, (x+y)^{p-1}$), hence Noetherian, dimension 2. Its integral closure is $k[[x, y]]$ (since $x = ((x+y) - y)$ and $y$ satisfies $T^p - y^p = 0$, so $y$ is integral over $A$, and then $x = (x+y) - y$ is integral over $A$). And $k[[x, y]]$ is Noetherian. Still not a counterexample.

The problem is that all these constructions give finite integral extensions, hence Noetherian integral closures.

**The key insight:** To get a non-Noetherian integral closure, we need the integral closure to NOT be a finite module over $A$. This requires $A$ to be non-excellent (non-Nagata).

Nagata's example of a non-excellent ring uses a field $k$ that is NOT excellent, or a construction that exploits the non-excellence of certain fields.

Actually, I recall now. The construction uses a field $k$ of characteristic $p$ with $[k : k^p] = \infty$ (i.e., $k$ is not perfect, or more precisely, $k$ has infinite $p$-degree). Wait, no, even perfect fields can give non-excellent rings in characteristic $p$.

Hmm, actually, I think the construction uses a field $k$ of characteristic 0, and the non-excellence comes from the analytic structure.

Let me try to recall the construction from a different source. I believe the standard reference is Nagata's book "Local Rings," and the example is in the appendix.

Actually, you know what, let me just look at this from the perspective of what I can prove rigorously. The question is asking whether the integral closure of a 2-dimensional Noetherian domain is always Noetherian. The answer is NO, and I should present the counterexample.

Let me use the following construction, which I'm fairly confident is correct based on my understanding of the theory:

**Construction (Nagata, 1962):**

Let $k$ be a field. Let $K = k(x, y)$ where $x, y$ are algebraically independent over $k$. Let $\alpha$ be a positive irrational number.

Define the valuation $v$ on $K$ by $v(x) = 1, v(y) = \alpha$, with valuation ring $V = \{f \in K : v(f) \geq 0\}$.

The value group $\Gamma = \mathbb{Z} + \mathbb{Z}\alpha$ is dense in $\mathbb{R}$, so $V$ is not Noetherian.

The residue field of $V$ is $k$, and $\dim V = 1$.

Now, let $z$ be an indeterminate over $K$, and let $L = K(z) = k(x, y, z)$. Extend $v$ to $L$ by the Gauss extension: $v(\sum a_i z^i) = \min_i v(a_i)$ and $v(z) = 0$. The valuation ring $W$ of this extended valuation has:
- Value group $\Gamma$ (same as before, dense, non-discrete)
- Residue field $\kappa(W) = k(z)$ (since the residue of $z$ is transcendental over $k$)
- $\dim W = 1$ (rank 1 valuation)

$W$ is not Noetherian (since $\Gamma$ is not discrete).

Now, consider the ring $R = k[x, y, z]_{(x, y, z)}$, a 3-dimensional regular local ring. We have $R \subseteq W$ (since $v(x) = 1 > 0, v(y) = \alpha > 0, v(z) = 0$, so $x, y \in \mathfrak{m}_W$ and $z$ is a unit in $W$; but $z \in (x, y, z)$, the maximal ideal of $R$... hmm, $z$ is in the maximal ideal of $R$ but is a unit in $W$. So $R \not\subseteq W$? No, $R \subseteq W$ because every element of $R$ is a fraction $f/g$ with $f, g \in k[x,y,z]$ and $g(0,0,0) \neq 0$, and $v(g) = 0$ (since the constant term of $g$ is nonzero, $v(g) = 0$) and $v(f) \geq 0$ (since $v(x), v(y) \geq 0$ and $v(z) = 0$). So $v(f/g) = v(f) - v(g) = v(f) \geq 0$, hence $f/g \in W$. Yes, $R \subseteq W$.)

But $R$ is 3-dimensional and integrally closed. We want a 2-dimensional Noetherian subring.

Let me use $R' = k[x, y, z]_{(x, y)}$ (localize at $(x, y)$, not $(x, y, z)$). This is a 2-dimensional... no, $k[x, y, z]_{(x, y)}$ has dimension 3 (the prime $(x, y)$ has height 2, and the ring has dimension 3).

Hmm. Let me use $R_0 = k[x, y]_{(x, y)}$, which is 2-dimensional. But $R_0 \subseteq V \subseteq W$ (where $V$ is the valuation ring on $K = k(x, y)$), and $R_0$ is integrally closed. Not useful.

OK, I think the issue is that I need to construct a 2-dimensional Noetherian domain whose integral closure is a 2-dimensional non-Noetherian ring, and the non-Noetherianity comes from a valuation.

Let me try the following approach:

**Use a 2-dimensional valuation ring:**

Let $K = k(x, y)$. Use the rank-2 composite valuation $v = v_1 \circ v_2$ where:
- $v_1$ is the $x$-adic valuation on $K$ ($v_1(x) = 1, v_1(y) = 0$, residue field $k(y)$)
- $v_2$ is the non-discrete valuation on $k(y)$ ($v_2(y) = \alpha$ irrational, residue field $k$)

The valuation ring $V$ is 2-dimensional and not Noetherian.

$V$ has a height-1 prime $\mathfrak{p}$ with $V/\mathfrak{p} \cong V_2$ (the non-Noetherian valuation ring of $v_2$ on $k(y)$) and $V_\mathfrak{p} = V_1$ (the DVR of $v_1$).

Now, $R = k[x, y]_{(x, y)} \subseteq V$ (since $v_1(x) = 1 > 0$ and $v_2(y \mod v_1) = \alpha > 0$, so both $x, y \in \mathfrak{m}_V$). $R$ is 2-dimensional and integrally closed.

We need a Noetherian subring $A$ of $V$ (or $K$) with $\dim A = 2$, not integrally closed, and $A' \supseteq V$.

**The construction of $A$ (using characteristic $p$):**

Let $k$ be a field of characteristic $p > 0$. Let $K = k(x, y)$.

Consider the subring $A = k[x^p, y]_{(x^p, y)}$ of $K$. This is isomorphic to $k[X, Y]_{(X, Y)}$ (since $x^p$ and $y$ are algebraically independent), so it's a 2-dimensional regular local ring, Noetherian and integrally closed. Not useful.

What about $A = k[x^p, y^p, x]_{(x^p, y^p, x)}$? In characteristic $p$, $x^p \in A$ and $x \in A$, so $A = k[x, y^p]_{(x, y^p)}$ (since $x^p = (x)^p$ is in $k[x]$). This is $k[X, Y]_{(X, Y)}$ (with $X = x, Y = y^p$), a 2-dimensional regular local ring, integrally closed. Not useful.

What about $A = k[x^p, y, xy]_{(x^p, y, xy)}$? We have $x^p, y, xy \in k[x, y]$. The relation: $(xy)^p = x^p y^p$, and $y^p = (y)^p \in k[y]$. So $A = k[x^p, y, xy]$. Is this Noetherian? It's a finitely generated $k$-algebra ($k[x^p, y, xy]$), so yes, it's Noetherian. Its dimension: the fraction field of $A$ is $k(x, y)$ (since $x = (xy)/y$ and $y \in A$). So $\dim A = 2$ (it's a 2-dimensional domain). The integral closure: $x = (xy)/y$ is in the fraction field, and $x^p \in A$, so $x$ satisfies $T^p - x^p = 0$ over $A$, hence $x$ is integral over $A$. So $A' \supseteq k[x, y]$. Since $k[x, y]$ is integrally closed, $A' = k[x, y]$ (localized at the appropriate prime). This is Noetherian. Not a counterexample.

The problem persists: finite extensions give Noetherian integral closures.

**The real construction:** I think the key is that Nagata's example uses a ring that is NOT a finitely generated algebra over a field, but rather a subring of a formal power series ring or a more exotic construction.

Let me try the following, which I believe is closer to the actual construction:

**Nagata's example (using formal power series):**

Let $k$ be a field of characteristic $p > 0$. Let $t$ be an indeterminate. Consider $k[[t]]$, a DVR with fraction field $k((t))$.

Choose a formal power series $s \in k[[t]]$ that is transcendental over $k(t)$. (For instance, $s = \sum_{n=1}^{\infty} t^{n!}$.)

Now, $k[[t]]$ is a DVR with uniformizer $t$. The element $s$ has some $t$-adic order, say $\text{ord}_t(s) = m$ (the smallest $n$ with $c_n \neq 0$ in $s = \sum c_n t^n$). WLOG, assume $\text{ord}_t(s) = 1$ (by replacing $s$ with $s/t^{m-1}$ if needed, or just choosing $s$ appropriately).

Consider the subring $A = k[[t^p, s^p, t]]$ of $k[[t]]$... but $k[[t]]$ is 1-dimensional, so $A$ would be at most 1-dimensional. Not useful for a 2-dimensional example.

Let me use two variables. Consider $k[[x, y]]$ (2-dimensional regular local ring). Choose $s \in k[[x]]$ transcendental over $k(x)$. Consider $A = k[[x^p, y, s]]$... but $s \in k[[x]]$, so $A \subseteq k[[x, y]]$ and $A$ is generated by $x^p, y, s$ which are power series in $x$ and $y$. Since $s \in k[[x]]$, $A = k[[x^p, s, y]]$. If $x^p$ and $s$ are algebraically independent over $k$ (which they are if $s$ is transcendental over $k(x^p)$, which follows from $s$ being transcendental over $k(x)$), then $A \cong k[[X, Y, Z]]$, a 3-dimensional regular local ring. Not 2-dimensional.

Hmm. I need to be more careful.

OK, I think I need to approach this differently. Let me use the known result and present the proof at a high level, giving the key ideas of the construction without getting bogged down in the details that I can't recall precisely.

Actually, let me try to recall the precise construction from Nagata. I believe it's the following:

**Nagata's Example (from "Local Rings", Appendix, Example 5):**

Let $k$ be a field, and let $K = k(x, y)$ where $x, y$ are algebraically independent over $k$.

Let $v$ be a valuation of $K$ defined as follows. Choose a positive irrational number $\alpha$. Set $v(x) = 1$ and $v(y) = \alpha$. The value group is $\mathbb{Z} + \mathbb{Z}\alpha$, which is a dense subgroup of $\mathbb{R}$.

Let $V$ be the valuation ring of $v$. Then $V$ is a 1-dimensional valuation ring, and it is not Noetherian (since the value group is not discrete).

The residue field of $V$ is $k$.

Now, let $z$ be an indeterminate over $K$, and set $L = K(z) = k(x, y, z)$. Extend $v$ to $L$ by defining $v(z) = 0$ and $v(\sum a_i z^i) = \min_i v(a_i)$ (Gauss extension). Let $W$ be the valuation ring of $v$ on $L$. Then $W$ is a 1-dimensional valuation ring with residue field $k(z)$, and $W$ is not Noetherian.

Now, consider the ring $R = k[x, y, z]_{(x, y, z)}$, a 3-dimensional regular local ring. We have $R \subseteq W$.

The integral closure of $R$ is $R$ itself (since $R$ is regular, hence normal). So this doesn't directly help.

Instead, consider the following subring of $L$:

$A = k + \mathfrak{m}_W$

where $\mathfrak{m}_W$ is the maximal ideal of $W$. Since the residue field of $W$ is $k(z)$, $A = \{f \in W : \bar{f} \in k\}$ where $\bar{f}$ is the residue of $f$ in $k(z)$. In other words, $A$ consists of elements of $W$ whose residue is a constant (in $k$, not a general element of $k(z)$).

Then $A$ is a local ring with maximal ideal $\mathfrak{m}_W$ (same as $W$), and $A/\mathfrak{m}_W = k$.

What is $\dim A$? Since $A \subseteq W$ and $W$ is a valuation ring of $L$, and $A$ and $W$ have the same maximal ideal, the prime ideals of $A$ correspond to the prime ideals of $W$ (which are just $(0)$ and $\mathfrak{m}_W$ since $W$ is rank 1). So $\dim A = 1$. Not 2-dimensional.

Hmm. The residue field of $W$ is $k(z)$, which has transcendence degree 1 over $k$. By the dimension formula, $\dim A + \text{tr.deg}(\kappa(A)/k) \leq \text{tr.deg}(L/k) = 3$. Here $\dim A = 1$ and $\text{tr.deg}(\kappa(A)/k) = \text{tr.deg}(k/k) = 0$ (since $\kappa(A) = k$). So $1 + 0 = 1 \leq 3$. There's "room" for higher dimension.

But $A$ as constructed is 1-dimensional. To get a 2-dimensional ring, I need a different construction.

**Idea:** Use a rank-2 valuation on $L = k(x, y, z)$ (or $K = k(x, y)$) to get a 2-dimensional valuation ring, and then construct a Noetherian subring.

Let me use $K = k(x, y)$ with the rank-2 composite valuation $v = v_1 \circ v_2$:
- $v_1$: $x$-adic on $K$ ($v_1(x) = 1, v_1(y) = 0$, residue field $k(y)$)
- $v_2$: non-discrete on $k(y)$ ($v_2(y) = \alpha$ irrational, residue field $k$)

The valuation ring $V$ is 2-dimensional, not Noetherian. The residue field is $k$.

$V$ has a height-1 prime $\mathfrak{p}$ with $V/\mathfrak{p} \cong$ (valuation ring of $v_2$ on $k(y)$) and $V_\mathfrak{p} = $ (DVR of $v_1$).

Now, $R = k[x, y]_{(x, y)} \subseteq V$ and $R$ is 2-dimensional, integrally closed.

Consider $A = k + \mathfrak{p}$ (the set of elements of $V$ whose image in $V/\mathfrak{p}$ is in $k$). Then $A$ is a local ring with $\kappa(A) = k$, and $\dim A = ?$.

The primes of $A$: $(0) \subset \mathfrak{p} \cap A = \mathfrak{p} \subset \mathfrak{m}_V \cap A = \mathfrak{m}_V$. So $\dim A = 2$.

Is $A$ Noetherian? $A = k + \mathfrak{p}$ where $\mathfrak{p}$ is
