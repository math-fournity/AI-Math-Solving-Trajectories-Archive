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
  <problem_id>polymath_00277</problem_id>
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

1. Let positive integers $a_{1}, a_{2}, \cdots, a_{31}, b_{1}, b_{2}, \cdots, b_{31}$ satisfy
$$
\begin{array}{l}
\text { (1) } a_{1}<a_{2}<\cdots<a_{31} \leqslant 2015, \\
b_{1}<b_{2}<\cdots<b_{31} \leqslant 2015 ; \\
\text { (2) } a_{1}+a_{2}+\cdots+a_{31}=b_{1}+b_{2}+\cdots+b_{31} \text {. } \\
\text { Find } S=\left|a_{1}-b_{1}\right|+\left|a_{2}-b_{2}\right|+\cdots+\left|a_{31}-b_{31}\right|
\end{array}
$$
the maximum value.
(Supplied by He Yijie)

## Standard Solution

1. Define the sets
$$
\begin{array}{l}
A=\left\{m \mid a_{m}>b_{m}, 1 \leqslant m \leqslant 31\right\}, \\
B=\left\{n \mid a_{n}<b_{n}, 1 \leqslant n \leqslant 31\right\} . \\
\text { Let } S_{1}=\sum_{m \in A}\left(a_{m}-b_{m}\right), S_{2}=\sum_{m \in B}\left(b_{n}-a_{n}\right) .
\end{array}
$$

Then $S=S_{1}+S_{2}$.
From condition (2), we know
$$
\begin{array}{l}
S_{1}-S_{2}=\sum_{m \in A \cup B}\left(a_{m}-b_{m}\right)=0 \\
\Rightarrow S_{1}=S_{2}=\frac{S}{2} . \\
\text { When } A=\varnothing, S=2 S_{1}=0 .
\end{array}
$$

Assume $A \neq \varnothing$, then $B \neq \varnothing$. In this case, $|A|, |B|$ are positive integers, and $|A|+|B| \leqslant 31$.
$$
\begin{array}{l}
\text { Let } u=a_{k}-b_{k}=\max _{m \in A}\left\{a_{m}-b_{m}\right\}, \\
v=b_{l}-a_{l}=\max _{n \in B}\left\{b_{n}-a_{n}\right\} .
\end{array}
$$

We will prove: $u+v \leqslant 1984$.
Without loss of generality, assume $1 \leqslant k<l \leqslant 31$.
Then $u+v=a_{k}-b_{k}+b_{l}-a_{l}$
$$
=b_{31}-\left(b_{31}-b_{l}\right)-b_{k}-\left(a_{l}-a_{k}\right) \text {. }
$$

From condition (1), we have
$$
\begin{array}{l}
b_{31} \leqslant 2015, b_{31}-b_{l} \geqslant 31-l, \\
b_{k} \geqslant k, a_{l}-a_{k} \geqslant l-k .
\end{array}
$$

Thus, $u+v \leqslant 2015-(31-l)-k-(l-k)$ $=1984$.
Clearly, $S_{1} \leqslant u|A|, S_{2} \leqslant v|B|$, hence,
$$
\begin{array}{l}
1984 \geqslant u+v \geqslant \frac{S_{1}}{|A|}+\frac{S_{2}}{|B|} \geqslant \frac{S_{1}}{|A|}+\frac{S_{2}}{31-|A|} \\
=\frac{S}{2} \cdot \frac{31}{|A|(31-|A|)} \geqslant \frac{31 S}{2 \times 15 \times 16} \\
\Rightarrow S \leqslant \frac{2 \times 15 \times 16}{31} \times 1984=30720 .
\end{array}
$$

On the other hand, if we take
$$
\begin{array}{l}
\left(a_{1}, a_{2}, \cdots, a_{16}, a_{17}, a_{18}, \cdots, a_{31}\right) \\
=(1,2, \cdots, 16,2001,2002, \cdots, 2015), \\
\left(b_{1}, b_{2}, \cdots, b_{31}\right)=(961,962, \cdots, 991),
\end{array}
$$

then conditions (1) and (2) are satisfied. In this case,
$$
S=2 S_{1}=2 \times 16 \times 960=30720 \text {. }
$$

In conclusion, the maximum value of $S$ is 30720.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have positive integers $a_1 < a_2 < \cdots < a_{31} \leq 2015$ and $b_1 < b_2 < \cdots < b_{31} \leq 2015$, with $\sum a_i = \sum b_i$. We want to maximize $S = \sum_{i=1}^{31} |a_i - b_i|$.

Let me think about this. First, let me check for answer leaks - the problem text doesn't contain any solution or answer, so we're good.

Let me think about the structure. We have two increasing sequences of 31 positive integers, each at most 2015, with equal sums. We want to maximize the sum of absolute differences of corresponding elements.

Key insight: To maximize $\sum |a_i - b_i|$, we want the sequences to be as "different" as possible at each position while maintaining equal total sums.

Let me think about what the maximum could be. 

Consider the set $A = \{a_1, \ldots, a_{31}\}$ and $B = \{b_1, \ldots, b_{31}\}$ as sets (they're sets since strictly increasing). The sum condition means $\sum A = \sum B$.

Now $S = \sum_{i=1}^{31} |a_i - b_i|$ where both are sorted in increasing order.

To maximize this, we want $a_i$ and $b_i$ to be far apart for each $i$. But they must have the same sum.

Strategy: Make $A$ consist of small numbers and $B$ consist of large numbers, but then the sums wouldn't be equal. So we need a balance.

Let me think differently. Consider the symmetric difference. Let $C = A \cap B$ (common elements), $A' = A \setminus B$, $B' = B \setminus A$. Then $|A'| = |B'| = k$ for some $k$, and $\sum A' = \sum B'$ (since $\sum A = \sum B$ and the common elements cancel).

The elements in $C$ contribute 0 to $S$ (when matched at the same position). The elements in $A'$ and $B'$ contribute to $S$.

Actually, let me think about this more carefully. When we sort and pair, the common elements might not pair with each other if the non-common elements shift positions.

Hmm, let me think about this differently.

Let me consider the simplest approach: try to make $A$ and $B$ share as few elements as possible, and make the non-shared elements as far apart as possible.

Let's say $A$ and $B$ share $m$ elements (the intersection). Then $|A \setminus B| = |B \setminus A| = 31 - m$. Let $k = 31 - m$.

The $k$ elements in $A \setminus B$ and $k$ elements in $B \setminus A$ must have equal sums (since the shared elements contribute equally to both sums).

Now, when we sort the combined sequences and pair them, the contribution to $S$ comes from the non-shared elements. But the pairing after sorting is complex.

Let me think about a specific construction. 

Idea: Let $A = \{1, 2, \ldots, 31\}$ (the smallest 31 positive integers). Sum = $31 \cdot 32/2 = 496$.

Now I need $B$ to be 31 distinct positive integers $\leq 2015$ with sum 496, but as different from $A$ as possible. But if $B$ must have sum 496 and 31 distinct positive integers, the minimum sum is also 496 (achieved by $\{1, 2, \ldots, 31\}$). So $B = A$ is forced. That gives $S = 0$. Not useful.

So we need larger sums to have room to maneuver.

Let me think about the other extreme. Let $A = \{1985, 1986, \ldots, 2015\}$ (the largest 31 numbers $\leq 2015$). Sum = $31 \cdot 2000 = 62000$. Similarly $B$ must have sum 62000 with 31 distinct integers $\leq 2015$, max sum is also 62000. So $B = A$, $S = 0$.

So extremes don't work. We need something in the middle.

Let me think about what maximizes $S$. 

Consider the following approach: Let $A$ have some very small and some very large elements, and $B$ have elements in the middle, or vice versa. Actually, let me think about it as: we want $a_i$ small and $b_i$ large (or vice versa) for each $i$, but the sums must be equal.

If for all $i$, $a_i < b_i$, then $\sum a_i < \sum b_i$, contradiction. So some $a_i > b_i$ and some $a_i < b_i$.

Let's say for indices $1 \leq i \leq p$, $a_i < b_i$, and for $p+1 \leq i \leq 31$, $a_i > b_i$ (or some mix). Actually, since both are sorted, there's a crossover point.

Let me think about the structure. Since $a_1 < a_2 < \cdots < a_{31}$ and $b_1 < b_2 < \cdots < b_{31}$, and they have the same sum, there must be some crossing.

Let me consider the differences $d_i = a_i - b_i$. We have $\sum d_i = 0$. We want to maximize $\sum |d_i|$.

The $d_i$ sequence: since $a_i$ and $b_i$ are both increasing, $d_i$ doesn't have a simple monotonicity. But there's a constraint from the ordering.

Let me think about an upper bound. 

Upper bound approach: 

$S = \sum |a_i - b_i|$. 

Consider the multiset $A \cup B$ (with multiplicity). The sum of all elements is $2 \sum a_i$. 

Actually, let me think about it as follows. $S = \sum_{i: a_i > b_i} (a_i - b_i) + \sum_{i: a_i < b_i} (b_i - a_i)$. Since $\sum d_i = 0$, both sums are equal. So $S = 2 \sum_{i: a_i > b_i} (a_i - b_i)$.

Let $P = \{i : a_i > b_i\}$ and $N = \{i : a_i < b_i\}$. Then $S = 2 \sum_{i \in P} (a_i - b_i) = 2 \sum_{i \in N} (b_i - a_i)$.

To maximize $S$, we want to maximize $\sum_{i \in P} (a_i - b_i)$.

Now, the elements $\{a_i : i \in P\}$ are some subset of $A$, and $\{b_i : i \in P\}$ are the corresponding subset of $B$ (at the same positions). Similarly for $N$.

Hmm, this is getting complex. Let me think about specific constructions.

Construction idea: 
- $A$ consists of the 31 smallest elements from some range, and $B$ consists of 31 elements that are "spread out" to have the same sum.

Actually, let me think about it more cleverly.

Let me try: $A = \{1, 2, \ldots, k\} \cup \{\text{some large numbers}\}$ and $B = \{k+1, k+2, \ldots\} \cup \{\text{some numbers}\}$.

Let me try a specific construction. Suppose $A$ has its first $p$ elements very small and last $31-p$ elements very large, while $B$ has all elements in the middle range.

Let me try $p = 15$ or so.

Actually, let me think about this more carefully with a cleaner approach.

Let me consider the problem as: we have two sets $A, B$ of size 31, subsets of $\{1, 2, \ldots, 2015\}$, with $\sum A = \sum B$. Maximize $\sum_{i=1}^{31} |a_i - b_i|$ where elements are sorted.

Let me think about the maximum possible value of $\sum_{i \in P} a_i$ where $P$ is the set of indices where $a_i > b_i$. 

The elements $a_i$ for $i \in P$ are at most 2015 each, and there are at most 31 of them. But they also need to be balanced by $b_i$ for $i \in N$ being large.

Let me try a concrete construction.

Let me try: 
- $A = \{1, 2, \ldots, 15, 2001, 2002, \ldots, 2015\}$ (15 small + 16 large)
  - Wait, that's 31 elements. Sum = $\sum_{i=1}^{15} i + \sum_{i=2001}^{2015} i = 120 + 16 \cdot 2008 = 120 + 32128 = 32248$.
  
- $B$ should have 31 elements with sum 32248, as different from $A$ as possible.

Hmm, this is getting complicated. Let me think about what $B$ should look like to maximize $S$.

If $A = \{1, \ldots, 15, 2001, \ldots, 2015\}$, then to maximize $S$, we'd want $B$ to be as far from $A$ as possible at each position. The sorted $A$ is $1, 2, \ldots, 15, 2001, \ldots, 2015$. 

For positions 1-15, $a_i = i$ (small), so we want $b_i$ large. For positions 16-31, $a_i = 2000+i$ (large), so we want $b_i$ small.

But $B$ must be sorted! So $b_1 < b_2 < \cdots < b_{31}$. If $b_1, \ldots, b_{15}$ are large and $b_{16}, \ldots, b_{31}$ are small, that contradicts sorting.

So the sortedness constraint is key. Since both are sorted, $b_1$ is the smallest element of $B$ and $b_{31}$ is the largest.

So if $a_1$ is small, to make $|a_1 - b_1|$ large, we need $b_1$ large, but $b_1$ is the minimum of $B$, so all of $B$ would be large, making $\sum B$ large.

This tension is the crux of the problem.

Let me reconsider. Given the sorting constraint, the natural structure is:
- For small $i$, both $a_i$ and $b_i$ are relatively small.
- For large $i$, both are relatively large.

The crossover happens somewhere in the middle.

Let me think about it as: there's some index $p$ where for $i \leq p$, $a_i < b_i$ (so $A$'s small elements are smaller than $B$'s small elements), and for $i > p$, $a_i > b_i$ (so $A$'s large elements are larger than $B$'s large elements). This way, $A$ is more "spread out" than $B$.

Wait, but that would make $\sum A > \sum B$ if $A$ has both smaller smalls and larger larges... no wait. If $a_i < b_i$ for small $i$ and $a_i > b_i$ for large $i$, then $A$ is more spread out. The sum could go either way.

Actually, for the sums to be equal, we need $\sum_{i \leq p} (b_i - a_i) = \sum_{i > p} (a_i - b_i)$. And $S = 2 \sum_{i > p} (a_i - b_i) = 2 \sum_{i \leq p} (b_i - a_i)$.

So to maximize $S$, we want to maximize $\sum_{i \leq p} (b_i - a_i)$, which equals $\sum_{i > p} (a_i - b_i)$.

To maximize this, we want:
- $a_i$ for $i \leq p$ to be as small as possible (close to 1, 2, ..., p)
- $b_i$ for $i \leq p$ to be as large as possible (but still less than $b_{p+1}$, and $b_i < b_{i+1}$)
- $a_i$ for $i > p$ to be as large as possible (close to 2015, 2014, ...)
- $b_i$ for $i > p$ to be as small as possible (but still greater than $b_p$)

And the balance condition: $\sum_{i \leq p} (b_i - a_i) = \sum_{i > p} (a_i - b_i)$.

Let me try $p = 15$ (so 15 elements on each side, plus one in the middle... actually 31 is odd, so let me think about $p = 15$ or $p = 16$).

Let me try $p = 15$: indices 1-15 have $a_i < b_i$, indices 16-31 have $a_i > b_i$. (16 elements on the right side.)

Actually, let me think about whether we need a clean split. In general, the sign of $a_i - b_i$ could change multiple times. But for maximizing $S$, I think a single crossover is optimal.

Let me consider: $A$ has very small and very large elements, $B$ has elements clustered in the middle.

Construction:
- $A = \{1, 2, \ldots, k\} \cup \{2016-k, 2017-k, \ldots, 2015\}$ where $k + (31-k) = 31$, so $A$ has $k$ small elements and $31-k$ large elements.

Wait, but $A$ needs 31 elements total. So $k$ small + $(31-k)$ large = 31. The small ones are $1, \ldots, k$ and the large ones are $2016-(31-k), \ldots, 2015$, i.e., $1985+k, \ldots, 2015$.

Sum of $A$ = $\frac{k(k+1)}{2} + \sum_{j=1985+k}^{2015} j = \frac{k(k+1)}{2} + \frac{(31-k)(1985+k+2015)}{2} = \frac{k(k+1)}{2} + \frac{(31-k)(4000+k)}{2}$.

Now $B$ should be 31 consecutive integers in the middle, say $\{m, m+1, \ldots, m+30\}$, with the same sum. Sum of $B$ = $31m + \frac{30 \cdot 31}{2} = 31m + 465$.

Setting equal: $\frac{k(k+1)}{2} + \frac{(31-k)(4000+k)}{2} = 31m + 465$.

$k(k+1) + (31-k)(4000+k) = 62m + 930$.

$k^2 + k + 31 \cdot 4000 + 31k - 4000k - k^2 = 62m + 930$.

$k + 124000 + 31k - 4000k = 62m + 930$.

$124000 - 3968k = 62m + 930$.

$62m = 124000 - 930 - 3968k = 123070 - 3968k$.

$m = \frac{123070 - 3968k}{62} = \frac{123070}{62} - \frac{3968k}{62} = 1985 - 64k$.

So $m = 1985 - 64k$.

For $B = \{m, \ldots, m+30\}$ to be valid, we need $m \geq 1$ and $m + 30 \leq 2015$, i.e., $m \leq 1985$.

$m = 1985 - 64k \geq 1 \Rightarrow k \leq 31.0...$, so $k \leq 31$. And $m \leq 1985$ is satisfied for $k \geq 0$.

Also, we need $B$ to not overlap with $A$ in a way that... actually, overlap is fine, but for maximizing $S$, we want minimal overlap.

Also, we need $A$ and $B$ to be disjoint for maximum $S$ (if they share an element, that element contributes 0 to $S$ at its position, roughly).

Wait, actually that's not quite right because of the sorting/pairing. Let me think again.

If $A = \{1, \ldots, k\} \cup \{1985+k, \ldots, 2015\}$ and $B = \{1985-64k, \ldots, 2014-64k\}$, then for them to be disjoint, we need $k < 1985 - 64k$ (the largest small element of $A$ is less than the smallest element of $B$) and $2014 - 64k < 1985 + k$ (the largest element of $B$ is less than the smallest large element of $A$).

First condition: $k < 1985 - 64k \Rightarrow 65k < 1985 \Rightarrow k < 30.5$, so $k \leq 30$.

Second condition: $2014 - 64k < 1985 + k \Rightarrow 29 < 65k \Rightarrow k > 0.44$, so $k \geq 1$.

So for $1 \leq k \leq 30$, $A$ and $B$ are disjoint.

Now let's compute $S$ for this construction.

$A$ sorted: $1, 2, \ldots, k, 1985+k, \ldots, 2015$.
$B$ sorted: $1985-64k, 1986-64k, \ldots, 2014-64k$.

For $i = 1, \ldots, k$: $a_i = i$, $b_i = 1985 - 64k + (i-1) = 1984 - 64k + i$.
$|a_i - b_i| = b_i - a_i = 1984 - 64k + i - i = 1984 - 64k$.

For $i = k+1, \ldots, 31$: $a_i = 1985 + k + (i - k - 1) = 1984 + i$, $b_i = 1984 - 64k + i$.
$|a_i - b_i| = a_i - b_i = (1984 + i) - (1984 - 64k + i) = 64k$.

So $S = k \cdot (1984 - 64k) + (31 - k) \cdot 64k = k(1984 - 64k) + 64k(31 - k) = k \cdot 1984 - 64k^2 + 1984k - 64k^2 = 1984k - 64k^2 + 1984k - 64k^2$.

Wait, let me redo: $k(1984 - 64k) + (31-k)(64k) = 1984k - 64k^2 + 1984k - 64k^2 = 2 \cdot 1984k - 2 \cdot 64k^2 = 3968k - 128k^2$.

Hmm wait: $(31-k) \cdot 64k = 64k \cdot 31 - 64k^2 = 1984k - 64k^2$.

So $S = (1984k - 64k^2) + (1984k - 64k^2) = 3968k - 128k^2$.

To maximize: $dS/dk = 3968 - 256k = 0 \Rightarrow k = 3968/256 = 15.5$.

Since $k$ must be an integer, try $k = 15$ or $k = 16$.

$k = 15$: $S = 3968 \cdot 15 - 128 \cdot 225 = 59520 - 28800 = 30720$.
$k = 16$: $S = 3968 \cdot 16 - 128 \cdot 256 = 63488 - 32768 = 30720$.

Both give $S = 30720$!

Let me verify with $k = 15$:
- $A = \{1, \ldots, 15\} \cup \{2000, \ldots, 2015\}$. That's 15 + 16 = 31 elements.
- $m = 1985 - 64 \cdot 15 = 1985 - 960 = 1025$.
- $B = \{1025, 1026, \ldots, 1055\}$. 31 elements.
- Sum of $A$: $120 + \sum_{j=2000}^{2015} j = 120 + 16 \cdot 2007.5 = 120 + 32120 = 32240$.
  Wait, $\sum_{j=2000}^{2015} j = \frac{16 \cdot (2000+2015)}{2} = 8 \cdot 4015 = 32120$. So sum = $120 + 32120 = 32240$.
- Sum of $B$: $31 \cdot 1025 + 465 = 31775 + 465 = 32240$. ✓

$S$: For $i = 1, \ldots, 15$: $|a_i - b_i| = |i - (1024 + i)| = 1024$. So $15 \cdot 1024 = 15360$.
For $i = 16, \ldots, 31$: $a_i = 2000 + (i-16) = 1984 + i$, $b_i = 1025 + (i-1) = 1024 + i$. $|a_i - b_i| = 960$. So $16 \cdot 960 = 15360$.
$S = 15360 + 15360 = 30720$. ✓

Now let me verify with $k = 16$:
- $A = \{1, \ldots, 16\} \cup \{2001, \ldots, 2015\}$. 16 + 15 = 31 elements.
- $m = 1985 - 64 \cdot 16 = 1985 - 1024 = 961$.
- $B = \{961, \ldots, 991\}$. 31 elements.
- Sum of $A$: $136 + \sum_{j=2001}^{2015} j = 136 + 15 \cdot 2008 = 136 + 30120 = 30256$.
- Sum of $B$: $31 \cdot 961 + 465 = 29791 + 465 = 30256$. ✓

$S$: For $i = 1, \ldots, 16$: $|i - (960 + i)| = 960$. $16 \cdot 960 = 15360$.
For $i = 17, \ldots, 31$: $a_i = 2001 + (i-17) = 1984 + i$, $b_i = 961 + (i-1) = 960 + i$. $|a_i - b_i| = 1024$. $15 \cdot 1024 = 15360$.
$S = 30720$. ✓

So we get $S = 30720$ with this construction. Now I need to prove this is optimal.

Let me think about the upper bound.

We have $S = 2 \sum_{i \in P} (a_i - b_i)$ where $P = \{i : a_i > b_i\}$.

Let $p = |P|$ and $q = 31 - p - r$ where $r$ is the number of indices with $a_i = b_i$. For simplicity, assume $r = 0$ (no common elements at the same position), which is optimal.

So $p + q = 31$ with $p$ indices where $a_i > b_i$ and $q$ where $a_i < b_i$.

$S = 2 \sum_{i \in P} (a_i - b_i)$.

Now, the key constraint is the ordering. Let me think about what constraints the ordering imposes.

Since $a_1 < \cdots < a_{31}$ and $b_1 < \cdots < b_{31}$:

For $i \in P$ (where $a_i > b_i$): these tend to be larger indices.
For $i \in N$ (where $a_i < b_i$): these tend to be smaller indices.

In our optimal construction, $P = \{16, \ldots, 31\}$ (or $\{17, \ldots, 31\}$) and $N = \{1, \ldots, 15\}$ (or $\{1, \ldots, 16\}$). So there's a single crossover point.

Let me think about the upper bound more carefully.

Claim: The crossover structure (single crossover) is optimal. That is, there exists $p$ such that $a_i \leq b_i$ for $i \leq p$ and $a_i \geq b_i$ for $i > p$.

This seems intuitive but let me think about whether it's necessarily true. Actually, it doesn't have to be true in general, but for the purpose of an upper bound, we can argue that the maximum is achieved with a single crossover.

Hmm, actually, let me think about an upper bound directly.

Upper bound approach:

$S = \sum |a_i - b_i|$. 

Consider the "transport" interpretation. We have two sets $A$ and $B$ of size 31 in $\{1, \ldots, 2015\}$ with equal sums. The quantity $S$ is the $L^1$ distance between the sorted sequences.

Let me think about it differently. Consider the indicator functions. Let $f_A(x) = 1$ if $x \in A$, $0$ otherwise, and similarly $f_B$. Then... hmm, this might not directly help.

Let me think about the problem in terms of the "gap" structure.

Alternative approach: Think of $A$ and $B$ as subsets. Let $A \Delta B = (A \setminus B) \cup (B \setminus A)$ be the symmetric difference. Let $|A \setminus B| = |B \setminus A| = k$ (they must be equal since $|A| = |B| = 31$). The elements in $A \cap B$ (there are $31 - k$ of them) ideally contribute 0 to $S$.

Actually, the elements in $A \cap B$ don't necessarily pair up in the sorted order. Let me think about this more carefully.

If $A \cap B = C$ with $|C| = 31 - k$, and $A \setminus B = \{a'_1 < \cdots < a'_k\}$, $B \setminus A = \{b'_1 < \cdots < b'_k\}$, then when we sort $A$ and $B$ and pair them, the common elements might not align.

However, there's a nice way to think about this. Consider the sorted list of all elements in $A \cup B$ (as a multiset). The elements of $A \cap B$ appear twice. 

Actually, let me think about a cleaner upper bound argument.

Let me consider the following. We have $S = 2T$ where $T = \sum_{i \in P} (a_i - b_i) = \sum_{i \in N} (b_i - a_i)$.

$T = \sum_{i \in P} a_i - \sum_{i \in P} b_i$.

Now, $\sum_{i \in P} a_i \leq$ sum of the $|P|$ largest elements of $A$. And $\sum_{i \in P} b_i \geq$ sum of the $|P|$ smallest elements of $B$... but this isn't quite right because $P$ is a specific set of indices.

Hmm, let me think about this differently.

Let me use the structure that in the optimal solution, there's a single crossover at position $p$. So for $i \leq p$, $a_i < b_i$, and for $i > p$, $a_i > b_i$.

Then $T = \sum_{i=p+1}^{31} a_i - \sum_{i=p+1}^{31} b_i = \sum_{i=1}^{p} b_i - \sum_{i=1}^{p} a_i$.

To maximize $T$:
- $\sum_{i=1}^{p} a_i$ should be minimized: the smallest possible is $\sum_{i=1}^{p} i = \frac{p(p+1)}{2}$.
- $\sum_{i=p+1}^{31} a_i$ should be maximized: the largest possible is $\sum_{j=2015-(31-p)+1}^{2015} j = \sum_{j=1985+p}^{2015} j$.
- $\sum_{i=1}^{p} b_i$ should be maximized and $\sum_{i=p+1}^{31} b_i$ should be minimized, subject to $b_1 < \cdots < b_{31}$ and $\sum b_i = \sum a_i$.

But we also need the constraint that $a_i < b_i$ for $i \leq p$ and $a_i > b_i$ for $i > p$, and that $b_p < b_{p+1}$.

Let me set up the optimization. Let $p$ be the crossover point. We want to maximize:

$T = \sum_{i=1}^{p} (b_i - a_i)$

subject to:
1. $a_1 < \cdots < a_{31}$, all in $\{1, \ldots, 2015\}$
2. $b_1 < \cdots < b_{31}$, all in $\{1, \ldots, 2015\}$
3. $\sum a_i = \sum b_i$
4. $a_i \leq b_i$ for $i \leq p$, $a_i \geq b_i$ for $i > p$ (the crossover structure)

To maximize $T = \sum_{i=1}^p (b_i - a_i) = \sum_{i=p+1}^{31} (a_i - b_i)$:

We want $a_i$ for $i \leq p$ to be as small as possible and $a_i$ for $i > p$ to be as large as possible. The extreme is:
- $a_i = i$ for $i = 1, \ldots, p$ (smallest $p$ positive integers)
- $a_i = 1985 + p + (i - p - 1) = 1984 + i$ for $i = p+1, \ldots, 31$ (largest $31-p$ integers $\leq 2015$)

This gives $\sum a_i = \frac{p(p+1)}{2} + \sum_{j=1985+p}^{2015} j = \frac{p(p+1)}{2} + \frac{(31-p)(4000+p)}{2}$.

Now for $B$: we want $\sum_{i=1}^p b_i$ to be as large as possible and $\sum_{i=p+1}^{31} b_i$ to be as small as possible, with $\sum b_i = \sum a_i$ and $b_1 < \cdots < b_{31}$, and $b_i \geq a_i + 1$ for $i \leq p$, $b_i \leq a_i - 1$ for $i > p$.

Actually wait, we don't strictly need $b_i \geq a_i + 1$; we need $b_i > a_i$ for $i \leq p$ and $b_i < a_i$ for $i > p$. But we also need $b_p < b_{p+1}$.

To maximize $T = \sum_{i=1}^p b_i - \sum_{i=1}^p a_i$, given $\sum b_i = \sum a_i$, we have $T = \sum_{i=p+1}^{31} a_i - \sum_{i=p+1}^{31} b_i$. So we want to maximize $\sum_{i=p+1}^{31} a_i$ (done, set to max) and minimize $\sum_{i=p+1}^{31} b_i$.

To minimize $\sum_{i=p+1}^{31} b_i$ while keeping $b_1 < \cdots < b_{31}$ and $\sum b_i = \sum a_i$: we want $b_{p+1}, \ldots, b_{31}$ to be as small as possible, which means $b_1, \ldots, b_p$ should be as large as possible.

The constraint is $b_p < b_{p+1}$ and all are distinct positive integers $\leq 2015$. Also $b_i > a_i$ for $i \leq p$ and $b_i < a_i$ for $i > p$.

To make $b_{p+1}, \ldots, b_{31}$ as small as possible, we want them to be $31 - p$ consecutive integers starting from some value $m+1$ (where $m = b_p$). And $b_1, \ldots, b_p$ should be $m - p + 1, \ldots, m$ (consecutive, ending at $m$).

So $B = \{m - p + 1, \ldots, m, m+1, \ldots, m + 30 - p\} = \{m - p + 1, \ldots, m + 30 - p\}$, which is 31 consecutive integers from $m - p + 1$ to $m + 30 - p$.

Sum of $B$ = $31 \cdot (m - p + 1 + m + 30 - p)/2 = 31(2m + 31 - 2p)/2$.

Setting equal to sum of $A$:
$31(2m + 31 - 2p)/2 = \frac{p(p+1)}{2} + \frac{(31-p)(4000+p)}{2}$.

$31(2m + 31 - 2p) = p(p+1) + (31-p)(4000+p)$.

$62m + 31 \cdot 31 - 62p = p^2 + p + 31 \cdot 4000 + 31p - 4000p - p^2$.

$62m + 961 - 62p = p + 124000 + 31p - 4000p$.

$62m + 961 - 62p = 124000 - 3968p$.

$62m = 124000 - 3968p - 961 + 62p = 123039 - 3906p$.

$m = \frac{123039 - 3906p}{62}$.

Let me check: $123039 / 62 = 1984.5$. Hmm, that's not an integer. $62 \times 1984 = 123008$. $123039 - 123008 = 31$. So $123039 / 62 = 1984 + 31/62 = 1984.5$.

$3906 / 62 = 63$. So $m = 1984.5 - 63p$.

For $m$ to be an integer, we need $1984.5 - 63p$ to be an integer, which requires $p$ to be a half-integer... that's a problem.

Hmm, this means with $B$ being exactly 31 consecutive integers, we can't always match. Let me reconsider.

Actually, in our earlier construction, $B$ was 31 consecutive integers and it worked. Let me recheck.

Earlier: $A = \{1, \ldots, k\} \cup \{1985+k, \ldots, 2015\}$, $B = \{1985-64k, \ldots, 2014-64k\}$.

The crossover is at position $k$: for $i \leq k$, $a_i = i < b_i = 1984 - 64k + i$ (since $1984 - 64k > 0$ for $k \leq 30$). For $i > k$, $a_i = 1984 + i > b_i = 1984 - 64k + i$ (since $64k > 0$).

So $p = k$ in my notation above. Let me recheck the formula.

With $p = k$: $m = 1984.5 - 63k$. For $k = 15$: $m = 1984.5 - 945 = 1039.5$. But we had $m = 1025$ earlier...

Wait, I think I made an error. Let me recompute. In the earlier construction, $B = \{1985 - 64k, \ldots, 2014 - 64k\}$, so the smallest element is $1985 - 64k$ and the largest is $2014 - 64k$. The "midpoint" $m$ in my new notation was $b_p = b_k$. 

$b_k = 1985 - 64k + (k-1) = 1984 - 63k$.

And $b_{k+1} = 1985 - 64k + k = 1985 - 63k$.

So $B = \{1985 - 64k, \ldots, 2014 - 64k\}$, which is $\{m - k + 1, \ldots, m + 30 - k\}$ where $m = b_k = 1984 - 63k$.

Let me recheck: $m - k + 1 = 1984 - 63k - k + 1 = 1985 - 64k$. ✓
$m + 30 - k = 1984 - 63k + 30 - k = 2014 - 64k$. ✓

So $m = 1984 - 63k$, and from my formula $m = 1984.5 - 63p$ with $p = k$. There's a discrepancy of 0.5.

Let me recheck the sum computation. 

$A = \{1, \ldots, k\} \cup \{1985+k, \ldots, 2015\}$.

Wait, I need to be more careful. The large elements of $A$ are $1985 + k, 1986 + k, \ldots, 2015$. That's $2015 - (1985+k) + 1 = 31 - k$ elements. ✓

Sum of large part: $\sum_{j=1985+k}^{2015} j = \frac{(31-k)(1985+k+2015)}{2} = \frac{(31-k)(4000+k)}{2}$.

Sum of small part: $\frac{k(k+1)}{2}$.

Total: $\frac{k(k+1) + (31-k)(4000+k)}{2} = \frac{k^2 + k + 124000 + 31k - 4000k - k^2}{2} = \frac{124000 - 3968k}{2} = 62000 - 1984k$.

Sum of $B = \{1985-64k, \ldots, 2014-64k\}$: This is 31 consecutive integers with average $(1985-64k + 2014-64k)/2 = (3999 - 128k)/2 = 1999.5 - 64k$.

Sum = $31(1999.5 - 64k) = 61984.5 - 1984k$... wait that doesn't match.

Hmm, $31 \times 1999.5 = 61984.5$. But sum should be an integer. Let me recompute.

$1985 - 64k + 2014 - 64k = 3999 - 128k$. Average = $(3999 - 128k)/2$. For $k = 15$: $(3999 - 1920)/2 = 2079/2 = 1039.5$. Sum = $31 \times 1039.5 = 32224.5$.

But earlier I computed sum of $B$ for $k=15$ as 32240. Let me recheck.

$B = \{1025, 1026, \ldots, 1055\}$. Sum = $\frac{31 \times (1025 + 1055)}{2} = \frac{31 \times 2080}{2} = 31 \times 1040 = 32240$. ✓

But $1985 - 64 \times 15 = 1985 - 960 = 1025$. ✓
$2014 - 64 \times 15 = 2014 - 960 = 1054$. 

Wait! $2014 - 960 = 1054$, not 1055! So $B = \{1025, \ldots, 1054\}$, which is only 30 elements!

I made an error earlier. Let me recompute.

$B = \{1985 - 64k, \ldots, 2014 - 64k\}$. Number of elements: $(2014 - 64k) - (1985 - 64k) + 1 = 30$. That's only 30 elements, not 31!

I made an error in my original calculation. Let me redo this.

We need $B$ to have 31 elements. If $B$ is 31 consecutive integers $\{m, m+1, \ldots, m+30\}$, then sum = $31m + 465$.

Setting equal to sum of $A = 62000 - 1984k$:
$31m + 465 = 62000 - 1984k$
$31m = 61535 - 1984k$
$m = \frac{61535 - 1984k}{31} = 1985 - 64k - \frac{1984k \mod 31}{31}$...

Wait, $61535 / 31 = 1985$. $1984 / 31 = 64$. So $m = 1985 - 64k$.

So $B = \{1985 - 64k, 1986 - 64k, \ldots, 2015 - 64k\}$, which is 31 elements from $1985 - 64k$ to $2015 - 64k$.

For $k = 15$: $B = \{1025, 1026, \ldots, 1055\}$. ✓ 31 elements. Sum = $31 \times 1040 = 32240$. ✓

OK so I had the wrong upper bound earlier. It should be $2015 - 64k$, not $2014 - 64k$. Let me redo the $S$ computation.

$A$ sorted: $1, 2, \ldots, k, 1985+k, \ldots, 2015$.
$B$ sorted: $1985-64k, 1986-64k, \ldots, 2015-64k$.

For $i = 1, \ldots, k$: $a_i = i$, $b_i = 1985 - 64k + (i-1) = 1984 - 64k + i$.
$|a_i - b_i| = 1984 - 64k$.

For $i = k+1, \ldots, 31$: $a_i = 1985 + k + (i - k - 1) = 1984 + i$, $b_i = 1985 - 64k + (i-1) = 1984 - 64k + i$.
$|a_i - b_i| = (1984 + i) - (1984 - 64k + i) = 64k$.

So $S = k(1984 - 64k) + (31-k)(64k) = 1984k - 64k^2 + 1984k - 64k^2 = 3968k - 128k^2$.

Same as before. Good, so $S = 3968k - 128k^2$, maximized at $k = 15.5$, giving $S = 30720$ for $k = 15$ or $k = 16$.

Now I need to verify the disjointness and validity conditions.

For $k = 15$:
- $A = \{1, \ldots, 15\} \cup \{2000, \ldots, 2015\}$
- $B = \{1025, \ldots, 1055\}$
- Disjoint? $15 < 1025$ ✓ and $1055 < 2000$ ✓. Yes, disjoint.
- All elements in $\{1, \ldots, 2015\}$? ✓
- Crossover: for $i \leq 15$, $a_i = i < 1024 + i = b_i$ ✓ (since $1024 > 0$). For $i \geq 16$, $a_i = 1984 + i > 1984 - 960 + i = 1024 + i = b_i$ ✓ (since $960 > 0$).

For $k = 16$:
- $A = \{1, \ldots, 16\} \cup \{2001, \ldots, 2015\}$
- $B = \{1985 - 1024, \ldots, 2015 - 1024\} = \{961, \ldots, 991\}$
- Disjoint? $16 < 961$ ✓ and $991 < 2001$ ✓.
- Valid. ✓

Now, is this construction optimal? I need to prove that $S \leq 30720$.

Let me think about the upper bound proof.

Approach: Show that for any valid $A, B$, $S \leq 30720$.

Let me think about this using the crossover structure. First, I'll argue that we can assume a single crossover (WLOG or that it's optimal), then optimize.

Actually, let me think about whether a single crossover is necessarily optimal. 

Consider the general case. Let $d_i = a_i - b_i$. We have $\sum d_i = 0$ and want to maximize $\sum |d_i|$. The constraint is that $a_i$ and $b_i$ are both strictly increasing sequences in $\{1, \ldots, 2015\}$.

The key constraint from monotonicity: if $i < j$, then $a_i < a_j$ and $b_i < b_j$, so $d_i - d_j = (a_i - a_j) - (b_i - b_j)$, which doesn't have a definite sign.

But there's a useful observation: the sequence $d_i$ can change sign, but the "total positive part" equals the "total negative part" (since $\sum d_i = 0$).

Let me think about an upper bound using a different approach.

Consider the set $A \cup B$ (with multiplicity). The sum of all elements (counting multiplicity) is $2\sigma$ where $\sigma = \sum a_i = \sum b_i$.

Now, $S = \sum |a_i - b_i|$. 

Let me think about the problem as a matching/transport problem. We have two sorted sequences and we're computing the $L^1$ distance.

Alternative approach: Think of $A$ and $B$ as multisets. The quantity $\sum |a_i - b_i|$ (with both sorted) is the Earth Mover's Distance (EMD) / Wasserstein-1 distance between the two uniform distributions on $A$ and $B$.

For the EMD between two sets of points on a line, there's a nice formula:
$$\sum_{i=1}^{31} |a_i - b_i| = \sum_{i=1}^{31} |F_A^{-1}(i/32) - F_B^{-1}(i/32)|$$
where $F_A^{-1}$ is the quantile function. But this is just restating the problem.

Let me try a different approach to the upper bound.

Key idea: Consider the "prefix sums" of the indicator functions.

Define $A(x) = |A \cap \{1, \ldots, x\}|$ and $B(x) = |B \cap \{1, \ldots, x\}|$ for $x = 0, 1, \ldots, 2015$.

Then there's a formula:
$$\sum_{i=1}^{31} |a_i - b_i| = \sum_{x=1}^{2015} |A(x) - B(x)|$$

This is a well-known identity relating the EMD on a line to the $L^1$ distance of cumulative distribution functions.

Let me verify: $\sum_{x=1}^{2015} |A(x) - B(x)|$. 

$A(x) - B(x)$ counts how many more elements of $A$ than $B$ are $\leq x$. 

The identity $\sum |a_i - b_i| = \sum_x |A(x) - B(x)|$ holds when both are sorted. Yes, this is a standard result.

So $S = \sum_{x=1}^{2015} |A(x) - B(x)|$.

Now, $A(x)$ and $B(x)$ are both non-decreasing functions from $\{0, \ldots, 2015\}$ to $\{0, \ldots, 31\}$, with $A(0) = B(0) = 0$ and $A(2015) = B(2015) = 31$.

Also, $\sum_{x=1}^{2015} A(x) = \sum_{i=1}^{31} (2015 - a_i + 1) = 31 \cdot 2016 - \sum a_i$... wait, let me think.

$\sum_{x=0}^{2015} A(x) = \sum_{x=0}^{2015} |A \cap \{1, \ldots, x\}| = \sum_{a \in A} (2015 - a + 1) = \sum_{a \in A} (2016 - a) = 31 \cdot 2016 - \sigma$.

Similarly $\sum_{x=0}^{2015} B(x) = 31 \cdot 2016 - \sigma$.

So $\sum_{x=0}^{2015} (A(x) - B(x)) = 0$, which is consistent with $\sum d_i = 0$.

Now, $S = \sum_{x=1}^{2015} |A(x) - B(x)|$ and $\sum_{x=0}^{2015} (A(x) - B(x)) = 0$ (note $A(0) = B(0) = 0$ so the $x=0$ term is 0).

Let $g(x) = A(x) - B(x)$. Then $g(0) = 0$, $g(2015) = 0$, $\sum_{x=0}^{2015} g(x) = 0$, and $S = \sum_{x=1}^{2015} |g(x)|$.

The constraints on $g$: $A(x)$ increases by 0 or 1 at each step (since $A$ is a set), similarly $B(x)$. So $g(x) - g(x-1) \in \{-1, 0, 1\}$ for each $x$. Also $|g(x)| \leq 31$.

We want to maximize $\sum |g(x)|$ subject to:
- $g(0) = 0$, $g(2015) = 0$
- $g(x) - g(x-1) \in \{-1, 0, 1\}$
- $\sum g(x) = 0$
- $g$ takes integer values

This is now a cleaner optimization problem!

To maximize $\sum |g(x)|$ with $\sum g(x) = 0$ and the step constraint, we want $g$ to be as large in absolute value as possible.

The optimal strategy: make $g$ increase to some maximum value $M$, stay there, then decrease to some minimum value $-M'$, stay there, then return to 0. But we need $\sum g(x) = 0$.

Actually, to maximize $\sum |g(x)|$ with $\sum g(x) = 0$, we want $g$ to spend as much time as possible at large positive and large negative values, with the positive and negative parts balancing.

The constraint $g(x) - g(x-1) \in \{-1, 0, 1\}$ means $g$ can change by at most 1 per step. So to go from 0 to $M$ takes at least $M$ steps, and from $M$ to $-M'$ takes at least $M + M'$ steps, and from $-M'$ to 0 takes at least $M'$ steps. Total transition steps: at least $2M + 2M'$.

We have 2015 steps (from $x=0$ to $x=2015$, that's 2015 steps). Wait, $g$ is defined at $x = 0, 1, \ldots, 2015$, so there are 2015 transitions and 2016 values.

Actually, $S = \sum_{x=1}^{2015} |g(x)|$, so we're summing over 2015 values (excluding $x=0$).

Let me think about the optimal shape of $g$. 

The optimal $g$ should:
1. Rise from 0 to $M$ as quickly as possible (in $M$ steps)
2. Stay at $M$ for as long as possible
3. Drop from $M$ to $-M'$ as quickly as possible (in $M + M'$ steps)
4. Stay at $-M'$ for as long as possible
5. Rise from $-M'$ to 0 as quickly as possible (in $M'$ steps)

The total "transition" steps are $M + (M + M') + M' = 2M + 2M'$. The remaining $2015 - 2M - 2M'$ steps are spent at $M$ or $-M'$.

Let $t_1$ = time at $M$, $t_2$ = time at $-M'$. Then $t_1 + t_2 = 2015 - 2M - 2M'$ (this is the number of $x$ values where $g$ is flat at $M$ or $-M'$, but we also need to count the transition values).

Hmm, let me be more careful. Let me think of $g$ as a function on $\{0, 1, \ldots, 2015\}$.

The "ramp up" from 0 to $M$: $g$ goes $0, 1, 2, \ldots, M$. This takes $M$ steps, and the values at these steps (excluding the starting 0) are $1, 2, \ldots, M$. The sum of $|g|$ over these steps is $1 + 2 + \cdots + M = M(M+1)/2$.

The "plateau at $M$": $g$ stays at $M$ for $t_1$ steps. Sum of $|g|$ = $M \cdot t_1$.

The "ramp down" from $M$ to $-M'$: $g$ goes $M, M-1, \ldots, 0, -1, \ldots, -M'$. This takes $M + M'$ steps. The values (excluding the starting $M$) are $M-1, \ldots, 0, -1, \ldots, -M'$. Sum of $|g|$ = $(M-1) + \cdots + 1 + 0 + 1 + \cdots + M' = M(M-1)/2 + M'(M'+1)/2$.

The "plateau at $-M'$": $g$ stays at $-M'$ for $t_2$ steps. Sum of $|g|$ = $M' \cdot t_2$.

The "ramp up" from $-M'$ to 0: $g$ goes $-M', -M'+1, \ldots, -1, 0$. This takes $M'$ steps. Values (excluding starting $-M'$): $-M'+1, \ldots, -1, 0$. Sum of $|g|$ = $1 + 2 + \cdots + (M'-1) = (M'-1)M'/2$.

Total steps (transitions): $M + t_1 + (M+M') + t_2 + M' = 2M + 2M' + t_1 + t_2 = 2015$.

So $t_1 + t_2 = 2015 - 2M - 2M'$.

Sum constraint: $\sum_{x=1}^{2015} g(x) = 0$.

Sum of $g$ over ramp up (0 to M): $1 + 2 + \cdots + M = M(M+1)/2$.
Sum of $g$ over plateau at M: $M \cdot t_1$.
Sum of $g$ over ramp down (M to -M'): $(M-1) + (M-2) + \cdots + 0 + (-1) + \cdots + (-M') = M(M-1)/2 - M'(M'+1)/2$.
Sum of $g$ over plateau at -M': $-M' \cdot t_2$.
Sum of $g$ over ramp up (-M' to 0): $(-M'+1) + \cdots + (-1) + 0 = -(M'-1)M'/2$.

Total sum: $M(M+1)/2 + Mt_1 + M(M-1)/2 - M'(M'+1)/2 - M't_2 - (M'-1)M'/2$.

$= M(M+1)/2 + M(M-1)/2 + Mt_1 - M'(M'+1)/2 - (M'-1)M'/2 - M't_2$.

$= M^2 + Mt_1 - M'^2 - M't_2$.

Setting this to 0: $M^2 + Mt_1 = M'^2 + M't_2$, i.e., $M(M + t_1) = M'(M' + t_2)$.

And $S = M(M+1)/2 + Mt_1 + M(M-1)/2 + M'(M'+1)/2 + M't_2 + (M'-1)M'/2$.

$= M^2 + Mt_1 + M'^2 + M't_2$.

Using the sum constraint $M(M+t_1) = M'(M'+t_2)$, let this common value be $V$. Then $S = V + V = 2V$.

So $S = 2M(M + t_1) = 2M'(M' + t_2)$.

We want to maximize $V = M(M + t_1)$ subject to:
- $t_1 + t_2 = 2015 - 2M - 2M'$
- $M(M + t_1) = M'(M' + t_2)$
- $M, M' \geq 1$ (positive integers, assuming $g$ actually goes positive and negative)
- $t_1, t_2 \geq 0$
- $M, M' \leq 31$ (since $|g(x)| \leq 31$)

Wait, actually $|g(x)| \leq 31$ is a constraint! Because $A(x)$ and $B(x)$ are between 0 and 31, so $|g(x)| \leq 31$.

So $M \leq 31$ and $M' \leq 31$.

From $M(M+t_1) = M'(M'+t_2)$ and $t_1 + t_2 = 2015 - 2M - 2M'$:

Let me set $M = M'$ for symmetry (this seems optimal). Then $M + t_1 = M + t_2$, so $t_1 = t_2$. And $2t_1 = 2015 - 4M$, so $t_1 = (2015 - 4M)/2$.

For $t_1 \geq 0$: $M \leq 503.75$, so $M \leq 503$. But $M \leq 31$, so this is fine.

$V = M(M + t_1) = M(M + (2015 - 4M)/2) = M(2M + 2015 - 4M)/2 = M(2015 - 2M)/2$.

$S = 2V = M(2015 - 2M)$.

To maximize: $dS/dM = 2015 - 4M = 0 \Rightarrow M = 503.75$. But $M \leq 31$, so the maximum is at $M = 31$.

$S = 31 \cdot (2015 - 62) = 31 \cdot 1953 = 60543$.

Hmm, that's much larger than 30720! Let me check if this is achievable.

With $M = M' = 31$, $t_1 = t_2 = (2015 - 124)/2 = 1891/2 = 945.5$. Not an integer!

So we need $t_1$ to be an integer. $2015 - 4M$ must be even, so $4M$ must be odd, which is impossible since $4M$ is always even. So $M = M'$ with integer $t_1 = t_2$ requires $2015 - 4M$ to be even, but $2015$ is odd and $4M$ is even, so $2015 - 4M$ is always odd. So $t_1 = t_2$ is never an integer!

So we need $M \neq M'$ or $t_1 \neq t_2$.

Let me try $M = 31, M' = 31$ but $t_1 \neq t_2$. Then $t_1 + t_2 = 2015 - 124 = 1891$ and $31(31 + t_1) = 31(31 + t_2)$, so $t_1 = t_2 = 945.5$. Not integer.

Try $M = 31, M' = 30$: $t_1 + t_2 = 2015 - 62 - 60 = 1893$. And $31(31 + t_1) = 30(30 + t_2)$. So $961 + 31t_1 = 900 + 30t_2$, i.e., $31t_1 - 30t_2 = -61$. With $t_1 + t_2 = 1893$: $t_2 = 1893 - t_1$. $31t_1 - 30(1893 - t_1) = -61$. $61t_1 - 56790 = -61$. $61t_1 = 56729$. $t_1 = 56729/61 = 930.31...$. Not integer.

Try $M = 31, M' = 29$: $t_1 + t_2 = 2015 - 62 - 58 = 1895$. $31(31+t_1) = 29(29+t_2)$. $961 + 31t_1 = 841 + 29t_2$. $31t_1 - 29t_2 = -120$. $t_2 = 1895 - t_1$. $31t_1 - 29(1895 - t_1) = -120$. $60t_1 - 54955 = -120$. $60t_1 = 54835$. $t_1 = 913.916...$. Not integer.

Hmm, let me try $M = 30, M' = 31$: $t_1 + t_2 = 2015 - 60 - 62 = 1893$. $30(30+t_1) = 31(31+t_2)$. $900 + 30t_1 = 961 + 31t_2$. $30t_1 - 31t_2 = 61$. $t_2 = 1893 - t_1$. $30t_1 - 31(1893 - t_1) = 61$. $61t_1 - 58683 = 61$. $61t_1 = 58744$. $t_1 = 963.016...$. Not integer.

This is getting messy. Let me think about whether $M = 31$ is actually achievable.

Actually, wait. I need to also check that the function $g$ corresponds to actual sets $A$ and $B$. The constraint is not just that $g(x) - g(x-1) \in \{-1, 0, 1\}$, but also that $A(x)$ and $B(x)$ are each non-decreasing with steps of 0 or 1. So $g(x) - g(x-1) = (A(x) - A(x-1)) - (B(x) - B(x-1))$ where each term is 0 or 1. So $g(x) - g(x-1) \in \{-1, 0, 1\}$, which I already have. But additionally, the positions where $A$ increases and $B$ increases must be distinct enough.

Actually, the constraint $g(x) - g(x-1) \in \{-1, 0, 1\}$ with $g(0) = g(2015) = 0$ and $|g(x)| \leq 31$ is necessary but might not be sufficient. We need $A(x)$ and $B(x)$ to each be non-decreasing with increments in $\{0, 1\}$, starting at 0 and ending at 31. 

Given $g = A - B$, we need to decompose $g$ into $A$ and $B$ such that both are valid "counting functions" of 31-element subsets of $\{1, \ldots, 2015\}$.

$A(x) = (g(x) + g(x) + 2B(x))/2$... this doesn't directly work. Let me think differently.

Given $g$, we need $A(x) - A(x-1) \in \{0,1\}$ and $B(x) - B(x-1) \in \{0,1\}$ and $A(x) - B(x) = g(x)$.

At each step, $g(x) - g(x-1) = \Delta A - \Delta B$ where $\Delta A, \Delta B \in \{0, 1\}$.
- If $g(x) - g(x-1) = 1$: $\Delta A = 1, \Delta B = 0$.
- If $g(x) - g(x-1) = -1$: $\Delta A = 0, \Delta B = 1$.
- If $g(x) - g(x-1) = 0$: either $\Delta A = \Delta B = 0$ or $\Delta A = \Delta B = 1$.

So when $g$ is flat (change = 0), we have a choice: both increase or both stay. The total number of increases of $A$ must be 31 (since $A(2015) = 31$), and similarly for $B$.

The number of steps where $\Delta A = 1$: this equals the number of $+1$ steps of $g$ plus the number of flat steps where we choose $\Delta A = 1$. This must equal 31.

Similarly for $B$.

Let $n_+$ = number of $+1$ steps, $n_-$ = number of $-1$ steps, $n_0$ = number of flat steps. Then $n_+ + n_- + n_0 = 2015$.

For $A$: $n_+ + k_A = 31$ where $k_A$ is the number of flat steps with $\Delta A = 1$.
For $B$: $n_- + k_B = 31$ where $k_B$ is the number of flat steps with $\Delta B = 1$.
And $k_A + k_B = n_0$ (each flat step has either both 0 or both 1).

So $n_+ + k_A = 31$, $n_- + k_B = 31$, $k_A + k_B = n_0$.
Adding: $n_+ + n_- + n_0 = 62$. But $n_+ + n_- + n_0 = 2015$. So $2015 = 62$?? That's a contradiction!

Wait, that can't be right. Let me recheck.

Oh, I see the issue. $A(2015) = 31$ means $\sum_{x=1}^{2015} \Delta A(x) = 31$. The total number of steps is 2015. So $n_+ + k_A = 31$ and $n_- + k_B = 31$ and $k_A + k_B = n_0$. So $n_+ + n_- + n_0 = n_+ + n_- + k_A + k_B = (n_+ + k_A) + (n_- + k_B) = 31 + 31 = 62$.

But the total number of steps is 2015, not 62! So we need $n_+ + n_- + n_0 = 2015$ AND $n_+ + k_A + n_- + k_B = 62$. Since $k_A + k_B = n_0$, we get $n_+ + n_- + n_0 = 62$... but also $= 2015$. Contradiction!

This means not every function $g$ with the step constraint is realizable. The constraint is much stronger: $n_+ + n_- + n_0 = 2015$ but $n_+ + n_- + k_A + k_B = 62$ where $k_A + k_B \leq n_0$. So $n_+ + n_- + n_0 = 2015$ and $n_+ + n_- \leq 62$. Thus $n_0 \geq 2015 - 62 = 1953$.

So the number of non-flat steps is at most 62! This makes sense: $A$ has 31 elements and $B$ has 31 elements, so there are at most 62 positions where either $A$ or $B$ "jumps". At all other positions, both are flat.

So $g$ is mostly flat, with at most 62 non-flat steps. And $n_+ \leq 31$ (since $A$ has 31 elements) and $n_- \leq 31$ (since $B$ has 31 elements).

This changes the optimization significantly! The function $g$ can only change at most 62 times out of 2015 steps.

Let me reconsider. $g$ starts at 0, changes by $+1$ at most 31 times (when an element of $A$ is encountered), changes by $-1$ at most 31 times (when an element of $B$ is encountered), and is flat elsewhere. But at positions where both $A$ and $B$ have an element, $g$ is also flat (both increase by 1).

So the non-flat steps of $g$ are exactly the positions in $A \Delta B$ (symmetric difference). The number of such positions is $|A \Delta B| = 2k$ where $k = |A \setminus B| = |B \setminus A|$.

So $n_+ = k$ (elements in $A \setminus B$) and $n_- = k$ (elements in $B \setminus A$), and $n_0 = 2015 - 2k$ (including positions where both or neither have an element).

Now, $g$ goes from 0, has $k$ upward steps and $k$ downward steps, and we want to maximize $\sum |g(x)|$.

The maximum of $g$ is at most $k$ (if all upward steps come before all downward steps), and the minimum is at least $-k$ (if all downward steps come before all upward steps). But we want both positive and negative parts.

For $\sum g(x) = 0$ and $S = \sum |g(x)|$ to be maximized, we want $g$ to go up to some $M$, stay there, go down to some $-M'$, stay there, and return to 0.

With $k$ up-steps and $k$ down-steps:
- To go from 0 to $M$: need $M$ up-steps.
- To go from $M$ to $-M'$: need $M$ down-steps and $M'$ up-steps... wait, no. To go from $M$ to $-M'$, we need $M + M'$ down-steps. But we only have $k$ down-steps total.

Let me re-think. We have $k$ up-steps and $k$ down-steps. The function $g$ goes from 0 to some max, down to some min, and back to 0.

To maximize $\sum |g|$, the optimal shape is:
1. $g$ rises from 0 to $M$ using $M$ up-steps.
2. $g$ stays at $M$ for $t_1$ flat steps.
3. $g$ drops from $M$ to $-M'$ using $M + M'$ down-steps.
4. $g$ stays at $-M'$ for $t_2$ flat steps.
5. $g$ rises from $-M'$ to 0 using $M'$ up-steps.

Total up-steps: $M + M' = k$.
Total down-steps: $M + M' = k$.
Good, both equal $k$.

Total steps: $(M + t_1) + (M + M') + (M' + t_2) = 2M + 2M' + t_1 + t_2 = 2k + t_1 + t_2 = 2015$.

Wait, the total number of steps is $n_+ + n_- + n_0 = 2k + n_0 = 2015$, so $n_0 = 2015 - 2k$ and $t_1 + t_2 = n_0 = 2015 - 2k$.

But wait, I also need to account for the flat steps during transitions. When $g$ rises from 0 to $M$, it uses $M$ up-steps, but between consecutive up-steps there might be flat steps. Similarly for other transitions.

Actually, I was overcomplicating. Let me re-think.

$g$ is defined on $\{0, 1, \ldots, 2015\}$. There are 2015 transitions. Among these, $k$ are $+1$, $k$ are $-1$, and $2015 - 2k$ are $0$.

The values $g(0), g(1), \ldots, g(2015)$ with $g(0) = g(2015) = 0$.

$S = \sum_{x=1}^{2015} |g(x)|$.

To maximize $S$, we want to arrange the $+1$ and $-1$ steps to maximize the area under $|g|$.

The optimal arrangement: all $+1$ steps first (in the first $k$ non-flat positions), making $g$ rise to $k$, then all $-1$ steps (in the next $k$ non-flat positions), making $g$ fall back to 0. But this gives $g \geq 0$ everywhere, so $\sum g(x) > 0$, which violates the constraint.

Wait, $\sum g(x) = 0$ is automatically satisfied because $g(0) = g(2015) = 0$ and... no, $\sum g(x) = 0$ is an additional constraint (it's equivalent to $\sum A = \sum B$).

Hmm, actually, $\sum_{x=0}^{2015} g(x) = \sum_{x=0}^{2015} A(x) - \sum_{x=0}^{2015} B(x) = (31 \cdot 2016 - \sigma) - (31 \cdot 2016 - \sigma) = 0$. So $\sum g(x) = 0$ is automatically satisfied! Great.

So the only constraints are:
- $g(0) = g(2015) = 0$
- $g$ has exactly $k$ steps of $+1$ and $k$ steps of $-1$ (and $2015 - 2k$ steps of $0$)
- $|g(x)| \leq 31$ (since $A(x), B(x) \in [0, 31]$)
- $g$ corresponds to valid $A, B$ (but I think the step constraint + the count constraint is sufficient)

Wait, is $|g(x)| \leq 31$ tight? $A(x) \in [0, 31]$ and $B(x) \in [0, 31]$, so $g(x) \in [-31, 31]$. But also, $A(x) + B(x) \leq 62$ and... actually, the constraint $|g(x)| \leq 31$ is correct but might not be the binding constraint. The binding constraint is that $M \leq k$ (can't go higher than the number of up-steps) and $M' \leq k$ (can't go lower than the number of down-steps).

Also, we need $k \leq 31$ (since $A$ and $B$ each have 31 elements, the symmetric difference has at most $2 \cdot 31 = 62$ elements, so $k \leq 31$).

Now, with the optimal shape (rise to $M$, plateau, fall to $-M'$, plateau, rise to 0):

Up-steps used: $M$ (rising) + $M'$ (rising from $-M'$) = $M + M' = k$.
Down-steps used: $M + M'$ (falling from $M$ to $-M'$) = $k$.

So $M + M' = k \leq 31$.

The flat steps: $t_1 + t_2 = 2015 - 2k$ (total flat steps). But we also need flat steps during transitions if the transitions aren't consecutive. Actually, in the optimal arrangement, we want to minimize flat steps during transitions (we want the transitions to be as "compressed" as possible, and the flat steps to be at the plateaus).

So the arrangement is:
- Rise from 0 to $M$: $M$ consecutive $+1$ steps. $g$ values: $1, 2, \ldots, M$.
- Plateau at $M$: $t_1$ flat steps. $g$ values: $M, M, \ldots, M$.
- Fall from $M$ to $-M'$: $M + M'$ consecutive $-1$ steps. $g$ values: $M-1, \ldots, 0, -1, \ldots, -M'$.
- Plateau at $-M'$: $t_2$ flat steps. $g$ values: $-M', \ldots, -M'$.
- Rise from $-M'$ to 0: $M'$ consecutive $+1$ steps. $g$ values: $-M'+1, \ldots, -1, 0$.

Total non-flat steps: $M + (M+M') + M' = 2k$. ✓
Total flat steps: $t_1 + t_2 = 2015 - 2k$. ✓

Now, $S = \sum_{x=1}^{2015} |g(x)|$.

Rise 0→M: $|g|$ values are $1, 2, \ldots, M$. Sum = $M(M+1)/2$.
Plateau at M: $M \cdot t_1$.
Fall M→-M': $|g|$ values are $M-1, M-2, \ldots, 1, 0, 1, \ldots, M'$. Sum = $M(M-1)/2 + M'(M'+1)/2$.
Plateau at -M': $M' \cdot t_2$.
Rise -M'→0: $|g|$ values are $M'-1, \ldots, 1, 0$. Sum = $(M'-1)M'/2$.

$S = M(M+1)/2 + Mt_1 + M(M-1)/2 + M'(M'+1)/2 + M't_2 + (M'-1)M'/2$.

$= M^2 + Mt_1 + M'^2 + M't_2$.

And the sum constraint $\sum g(x) = 0$:
Rise: $1 + 2 + \cdots + M = M(M+1)/2$.
Plateau M: $Mt_1$.
Fall: $(M-1) + \cdots + 1 + 0 + (-1) + \cdots + (-M') = M(M-1)/2 - M'(M'+1)/2$.
Plateau -M': $-M't_2$.
Rise: $(-M'+1) + \cdots + (-1) + 0 = -(M'-1)M'/2$.

Total: $M(M+1)/2 + Mt_1 + M(M-1)/2 - M'(M'+1)/2 - M't_2 - (M'-1)M'/2$.

$= M^2 + Mt_1 - M'^2 - M't_2 = 0$.

So $M^2 + Mt_1 = M'^2 + M't_2$, i.e., $M(M + t_1) = M'(M' + t_2)$.

Let $V = M(M + t_1) = M'(M' + t_2)$. Then $S = 2V$.

We want to maximize $V$ subject to:
- $M + M' = k \leq 31$
- $t_1 + t_2 = 2015 - 2k$
- $M(M + t_1) = M'(M' + t_2)$
- $t_1, t_2 \geq 0$
- $M, M' \geq 0$ (integers)

From $M + t_1 + M' + t_2 = k + (2015 - 2k) = 2015 - k$:
$M + t_1 + M' + t_2 = 2015 - k$.

Let $u = M + t_1$ and $v = M' + t_2$. Then $u + v = 2015 - k$ and $Mu = M'v$ and $M + M' = k$.

From $Mu = M'v$ and $u + v = 2015 - k$:
$v = Mu/M'$ and $u + Mu/M' = 2015 - k$, so $u(1 + M/M') = 2015 - k$, $u(M' + M)/M' = 2015 - k$, $u \cdot k / M' = 2015 - k$, so $u = M'(2015 - k)/k$ and $v = M(2015 - k)/k$.

Then $V = Mu = M \cdot M'(2015-k)/k = MM'(2015-k)/k$.

We want to maximize $V = \frac{MM'(2015-k)}{k}$ subject to $M + M' = k$, $M, M' \geq 0$.

By AM-GM, $MM' \leq (M+M')^2/4 = k^2/4$, with equality when $M = M' = k/2$.

So $V \leq \frac{k^2/4 \cdot (2015-k)}{k} = \frac{k(2015-k)}{4}$.

$S = 2V \leq \frac{k(2015-k)}{2}$.

Now maximize over $k \leq 31$: $f(k) = k(2015-k)/2$. This is a downward parabola with maximum at $k = 2015/2 = 1007.5$. Since $k \leq 31$, the maximum is at $k = 31$.

$S \leq 31 \cdot (2015 - 31)/2 = 31 \cdot 1984 / 2 = 31 \cdot 992 = 30752$.

But we need $M = M' = k/2 = 15.5$, which is not an integer! So the AM-GM bound isn't achieved exactly.

With $k = 31$, $M + M' = 31$. To maximize $MM'$, use $M = 15, M' = 16$ (or vice versa). $MM' = 240$.

$V = 240 \cdot (2015 - 31)/31 = 240 \cdot 1984/31$.

$1984/31 = 64$. So $V = 240 \cdot 64 = 15360$. $S = 2 \cdot 15360 = 30720$.

So $S \leq 30720$ when $k = 31, M = 15, M' = 16$ (or $M = 16, M' = 15$).

But wait, I need to check that $t_1, t_2 \geq 0$.

$u = M'(2015-k)/k = 16 \cdot 1984/31 = 16 \cdot 64 = 1024$. $t_1 = u - M = 1024 - 15 = 1009 \geq 0$. ✓
$v = M(2015-k)/k = 15 \cdot 64 = 960$. $t_2 = v - M' = 960 - 16 = 944 \geq 0$. ✓

Great!

Now let me also check: is $k = 31$ actually the best? We need to check if for $k < 31$, we could get a larger $S$.

For general $k$ with $M = M' = k/2$ (when $k$ is even):
$S = k(2015-k)/2$.

For $k = 30$: $S = 30 \cdot 1985/2 = 29775$. Less than 30720.
For $k = 31$ with $M = 15, M' = 16$: $S = 30720$.
For $k = 32$: Not possible since $k \leq 31$.

Actually wait, can $k = 31$? $k = |A \setminus B| = |B \setminus A|$. Since $|A| = |B| = 31$, $k$ can be at most 31 (when $A$ and $B$ are disjoint). So $k \leq 31$. ✓

But I should also check: for $k = 31$, we need $A$ and $B$ to be disjoint. And $M = 15, M' = 16$ means $g$ reaches a max of 15 and min of -16 (or max 16, min -15). This requires $|g(x)| \leq 31$, which is satisfied.

But there's also the constraint that $g(x) \geq -B(x) \geq -31$ and $g(x) \leq A(x) \leq 31$. More precisely, $A(x) = (g(x) + A(x) + B(x))/... $ hmm, let me think about whether the decomposition is valid.

Given $g$ with the right step structure, can we always find valid $A$ and $B$? 

We need $A(x) \geq 0$, $B(x) \geq 0$, $A(x) \leq 31$, $B(x) \leq 31$, and $A(x) - B(x) = g(x)$.

At each step:
- $+1$ step: $A$ increases, $B$ stays. So $A(x) = A(x-1) + 1$, $B(x) = B(x-1)$.
- $-1$ step: $A$ stays, $B$ increases. So $A(x) = A(x-1)$, $B(x) = B(x-1) + 1$.
- $0$ step: both stay or both increase.

We need $A(x) \leq 31$ and $B(x) \leq 31$ at all times, and $A(2015) = B(2015) = 31$.

For the $+1$ steps: $A$ increases. After all $k = 31$ up-steps in the first phase, $A = 31$. But then $A$ can't increase anymore. In the fall phase, $A$ doesn't increase (only $B$ does). In the rise phase from $-M'$ to 0, $A$ increases by $M'$ steps. So total $A$ increases = $M + M' = k = 31$. ✓

Similarly for $B$: $B$ increases during the fall ($M + M' = k = 31$ steps) and during flat steps where both increase. But we need $B(2015) = 31$, and $B$ increases by $k = 31$ from the $-1$ steps. So all of $B$'s increases come from the $-1$ steps, and the flat steps must have $\Delta A = \Delta B = 0$.

Wait, but then $A(2015) = M + M' = 31$ from $+1$ steps, and $B(2015) = M + M' = 31$ from $-1$ steps. The flat steps have $\Delta A = \Delta B = 0$. So total $A$ increases = 31 ✓ and total $B$ increases = 31 ✓.

Now, during the process, $A(x) = $ (number of $+1$ steps up to position $x$) and $B(x) = $ (number of $-1$ steps up to position $x$).

In the rise phase (0 to $M$): $A$ goes from 0 to $M$, $B$ stays at 0. So $A(x) \leq M \leq 31$ ✓, $B(x) = 0$ ✓.

In the plateau at $M$: $A = M$, $B = 0$. $g = M$. ✓

In the fall phase ($M$ to $-M'$): $A$ stays at $M$, $B$ goes from 0 to $M + M' = k = 31$. So $B(x) \leq 31$ ✓. $A(x) = M \leq 31$ ✓.

In the plateau at $-M'$: $A = M$, $B = 31$. $g = M - 31 = M - k = M - (M+M') = -M'$. ✓

In the rise phase ($-M'$ to 0): $A$ goes from $M$ to $M + M' = 31$, $B$ stays at 31. $A(x) \leq 31$ ✓, $B(x) = 31$ ✓.

So the decomposition is valid! The constraint $A(x) \leq 31$ and $B(x) \leq 31$ is automatically satisfied.

So the upper bound $S \leq 30720$ is tight, achieved by our construction.

But wait, I need to also verify that this is indeed the global maximum. I showed that for the "single crossover" shape, the maximum is 30720. But could a different shape (multiple crossovers) do better?

Let me think about this. The key formula is $S = 2V$ where $V = MM'(2015-k)/k$ with $M + M' = k$. This was derived assuming a specific shape (rise, plateau, fall, plateau, rise). 

Could a different shape give a larger $S$? For instance, what if $g$ goes up, down, up, down (multiple oscillations)?

The formula $S = \sum |g(x)|$ with $\sum g(x) = 0$ means $S = 2 \sum_{g(x)>0} g(x) = 2 \sum_{g(x)<0} |g(x)|$.

For a general $g$ with $k$ up-steps and $k$ down-steps, the maximum of $g$ is at most $k$ and the minimum is at least $-k$. But with the area constraint, the optimal is to concentrate the positive and negative parts.

I think the single-crossover shape is optimal because:
1. To maximize $\sum_{g>0} g(x)$, we want $g$ to be as positive as possible for as long as possible.
2. To maximize $\sum_{g<0} |g(x)|$, we want $g$ to be as negative as possible for as long as possible.
3. With a fixed number of up/down steps, the single crossover concentrates the positive and negative regions.

Let me prove this more rigorously. 

Consider any $g$ with $k$ up-steps and $k$ down-steps, $g(0) = g(2015) = 0$, $\sum g(x) = 0$.

Let $P = \{x : g(x) > 0\}$ and $N = \{x : g(x) < 0\}$. $S = 2\sum_{x \in P} g(x)$.

$\sum_{x \in P} g(x) = \sum_{x \in P} (A(x) - B(x))$.

Hmm, this is getting complicated. Let me try a different approach.

Actually, I realize the formula $S = 2V$ with $V = MM'(2015-k)/k$ was derived for a specific shape. Let me verify that this is indeed optimal among all shapes.

Alternative approach: Direct upper bound.

$S = \sum_{x=1}^{2015} |g(x)|$ where $g(x) = A(x) - B(x)$.

$g$ has $k$ up-steps and $k$ down-steps, $g(0) = g(2015) = 0$, $\sum g(x) = 0$.

Let $M = \max_x g(x)$ and $m = \min_x g(x) = -M'$ (with $M' > 0$).

$S = \sum_{g>0} g + \sum_{g<0} |g| = 2\sum_{g>0} g$ (since $\sum g = 0$).

Now, $\sum_{g>0} g \leq M \cdot |P|$ where $|P|$ is the number of positions where $g > 0$. But this isn't tight enough.

Let me think about it differently. 

$\sum_{x=1}^{2015} |g(x)| \leq \sum_{x=1}^{2015} |g(x)|$... that's circular.

Let me use the constraint more carefully. We have $k$ up-steps and $k$ down-steps. The function $g$ can be decomposed into "excursions" above 0 and below 0.

Claim: The single-crossover shape is optimal.

Proof sketch: Consider any shape. We can "rearrange" the steps to form a single crossover without decreasing $S$. 

Specifically, move all up-steps that occur when $g > 0$ to be as early as possible (to increase the positive area), and all down-steps that occur when $g < 0$ to be as late as possible (to increase the negative area). The extreme case is the single crossover.

Actually, let me think about this more carefully with a cleaner argument.

Let me use the following approach. We have $g$ with $k$ up-steps and $k$ down-steps. Define the "positive area" $P = \sum_{g(x)>0} g(x)$ and "negative area" $N = \sum_{g(x)<0} |g(x)|$. We have $P = N$ and $S = 2P$.

Now, $P = \sum_{g(x)>0} g(x)$. The positive part of $g$ consists of some number of "hills" (excursions above 0). Each hill starts at 0, goes up, and returns to 0. 

For a single hill reaching height $h$ with $u$ up-steps and $d$ down-steps ($u = d$ for the hill to return to 0, but actually $u - d = 0$ only if the hill starts and ends at 0), the area is maximized when the hill is as "flat-topped" as possible.

Hmm, this is getting complicated. Let me try a more direct approach.

Direct proof of upper bound:

We have $S = \sum_{i=1}^{31} |a_i - b_i|$.

Let $P = \{i : a_i > b_i\}$ and $N = \{i : a_i < b_i\}$ (assuming no ties, which is optimal). Let $p = |P|$ and $q = |N|$, so $p + q = 31$.

$S = 2\sum_{i \in P} (a_i - b_i) = 2\sum_{i \in N} (b_i - a_i)$.

Now, $\sum_{i \in P} a_i + \sum_{i \in N} a_i = \sum_{i \in P} b_i + \sum_{i \in N} b_i$ (equal sums).

So $\sum_{i \in P} a_i - \sum_{i \in P} b_i = \sum_{i \in N} b_i - \sum_{i \in N} a_i$. This is just the balance condition.

Now, $T = \sum_{i \in P} (a_i - b_i)$. We want to maximize $T$ (then $S = 2T$).

The elements $\{a_i : i \in P\}$ are some $p$ elements of $A$, and $\{b_i : i \in P\}$ are the corresponding $p$ elements of $B$ (at the same indices). 

Key constraint: Since both sequences are sorted, if $i \in P$ (i.e., $a_i > b_i$), these tend to be larger indices. Similarly, $i \in N$ tend to be smaller indices.

In fact, there's a useful structural result: if we define $d_i = a_i - b_i$, then there exists a crossover point $c$ such that $d_i \leq 0$ for $i \leq c$ and $d_i \geq 0$ for $i > c$. This is because... actually, this isn't necessarily true in general. 

Hmm, but for the purpose of an upper bound, I can use the CDF approach which I already set up.

Let me go back to the CDF approach and prove the upper bound rigorously.

We have $S = \sum_{x=1}^{2015} |g(x)|$ where $g(x) = A(x) - B(x)$, $g(0) = g(2015) = 0$, $\sum g(x) = 0$, and $g$ has $k$ up-steps and $k$ down-steps with $k \leq 31$.

I want to show $S \leq 30720$.

Let me use a different bounding approach. 

$S = 2 \sum_{x: g(x) > 0} g(x)$.

Let $M = \max g(x)$. The positive values of $g$ form some region(s). 

$\sum_{x: g(x)>0} g(x) \leq M \cdot |\{x : g(x) > 0\}|$.

But also, the number of positive positions is at most $2015 - 2k + k = 2015 - k$ (since we need at least $k$ down-steps to bring $g$ back below 0 and eventually to 0). Hmm, this isn't quite right either.

Let me try yet another approach. 

Consider the "single crossover" bound. I'll show that for any $g$ with $k$ up-steps and $k$ down-steps:

$S \leq \frac{k(2015 - k)}{2} \cdot \frac{4M_0 M_0'}{(M_0 + M_0')^2}$

where $M_0 = $ max of $g$ and $M_0' = |\min g|$, and $M_0 + M_0' \leq k$.

Actually, this is getting too complicated. Let me just prove the bound directly.

Lemma: For any $g$ with $k$ up-steps, $k$ down-steps, $g(0) = g(2015) = 0$, $\sum g(x) = 0$:

$S = \sum |g(x)| \leq \frac{k(2015 - k)}{2}$.

Proof: $S = 2 \sum_{g > 0} g(x)$. Let $M = \max g$ and $M' = -\min g$ (so $M, M' \geq 0$ and $M + M' \leq k$).

The positive part of $g$ has area $P = \sum_{g>0} g(x)$. This area is bounded by $M$ times the number of positions where $g > 0$... but I need a better bound.

Actually, let me think about it as follows. The positive area $P$ and negative area $N = P$ satisfy:

$P \leq M \cdot L_+$ where $L_+$ is the "width" of the positive region.
$P \leq M' \cdot L_-$ where $L_-$ is the "width" of the negative region.

And $L_+ + L_- \leq 2015 - 2k$ (the total flat + transition width, minus the transition steps).

Hmm, actually $L_+ + L_-$ should account for the transition steps too. Let me think about it as: the total number of positions is 2015, and the transitions (non-flat steps) take up $2k$ positions. The remaining $2015 - 2k$ positions are flat. But the "width" of the positive region includes both flat and transition positions.

Let me define things more carefully. The positive region is $\{x : g(x) > 0\}$. Let $L_+ = |\{x \in \{1, \ldots, 2015\} : g(x) > 0\}|$ and $L_- = |\{x : g(x) < 0\}|$ and $L_0 = |\{x : g(x) = 0\}|$. Then $L_+ + L_- + L_0 = 2015$.

$P = \sum_{g>0} g(x) \leq M \cdot L_+$.
$P = \sum_{g<0} |g(x)| \leq M' \cdot L_-$.

So $P \leq \min(M \cdot L_+, M' \cdot L_-)$.

Also, $P \geq$ (something related to the transitions). 

And $L_+ + L_- \leq 2015$ (with equality when $L_0 = 0$, but $L_0 \geq 2k - 2$ or something... actually $g = 0$ at $x = 0$ and $x = 2015$ and at transition points where $g$ passes through 0).

Hmm, let me try a cleaner approach.

$P = \sum_{g > 0} g(x)$. 

I'll bound $P$ using the constraint on the number of steps.

The positive excursion of $g$ requires at least $M$ up-steps to reach height $M$ and at least $M$ down-steps to return to 0 (if it returns through 0). Similarly, the negative excursion requires at least $M'$ down-steps and $M'$ up-steps.

Total up-steps needed: at least $M$ (for positive excursion) + $M'$ (to return from negative to 0) = $M + M' \leq k$.
Total down-steps needed: at least $M$ (to return from positive) + $M'$ (for negative excursion) = $M + M' \leq k$.

So $M + M' \leq k$. ✓

Now, the positive region: $g$ is positive on some set of positions. The area $P = \sum_{g>0} g(x)$. 

The maximum area for a given $M$ and a given number of positions $L_+$ is $M \cdot L_+$ (achieved when $g = M$ on all positive positions). But to have $g = M$ on $L_+$ positions, we need $M$ up-steps before and $M$ down-steps after, using $2M$ transition steps. The $L_+$ flat positions at height $M$ plus the $M$ transition steps going up and $M$ going down (but the transition steps also contribute to the area).

Actually, the area of the positive excursion, including transition steps, is:
- Going up from 0 to $M$: $M$ steps, contributing $1 + 2 + \cdots + M = M(M+1)/2$.
- Flat at $M$: $t_1$ steps, contributing $M \cdot t_1$.
- Going down from $M$ to 0: $M$ steps, contributing $M + (M-1) + \cdots + 1 = M(M+1)/2$.

Wait, but the "going down" might go below 0 (to $-M'$). Let me separate the positive and negative parts.

If $g$ has a single crossover (goes up to $M$, then down to $-M'$, then up to 0), the positive area is:
- Up from 0 to $M$: $1 + 2 + \cdots + M = M(M+1)/2$.
- Flat at $M$: $M \cdot t_1$.
- Down from $M$ to 0: $M + (M-1) + \cdots + 1 = M(M+1)/2$. (Only the part above 0.)
Total positive area: $M(M+1)/2 + Mt_1 + M(M+1)/2 = M(M+1) + Mt_1 = M(M + 1 + t_1)$.

Hmm wait, going down from $M$ to 0 takes $M$ steps, and the values are $M-1, M-2, \ldots, 0$ (if we're going down from $M$). But the value at the step is $g(x)$, and $|g(x)|$ for the positive part. Let me be more careful.

When $g$ goes from $M$ down to 0 (and then continues to $-M'$), the values at each step are:
$g$ at the first down-step: $M - 1$ (positive, contributes $M-1$ to positive area).
...
$g$ at the $M$-th down-step: $0$ (doesn't contribute).
$g$ at the $(M+1)$-th down-step: $-1$ (contributes to negative area).
...

So the positive area during the descent from $M$ to 0 is: $(M-1) + (M-2) + \cdots + 1 + 0 = M(M-1)/2$.

And the positive area during the ascent from 0 to $M$ is: $1 + 2 + \cdots + M = M(M+1)/2$.

Total positive area (for single crossover): $M(M+1)/2 + Mt_1 + M(M-1)/2 = M^2 + Mt_1 = M(M + t_1)$.

Similarly, negative area: $M'(M' + t_2)$.

And $P = M(M + t_1) = M'(M' + t_2) = V$.

$S = 2V$.

Now, $M + t_1 + M' + t_2 = $ (total positions in the "positive plateau + negative plateau + transitions"). The transitions take $2k$ steps (as computed), and the plateaus take $t_1 + t_2 = 201
