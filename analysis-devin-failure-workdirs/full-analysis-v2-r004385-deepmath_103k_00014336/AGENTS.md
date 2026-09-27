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
  <problem_id>deepmath_103k_00014336</problem_id>
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

Determine the multiple eigenvalue of the matrix \( A = \begin{bmatrix} 2 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 \\ 3 & 5 & -2 & -2 \\ -2 & 3 & 3 & 5 \\ \end{bmatrix} \).

## Standard Solution

Okay, so I need to find the multiple eigenvalue of this matrix A. Let me recall that multiple eigenvalues are eigenvalues that have algebraic multiplicity greater than one. So, first, I should probably find all the eigenvalues of A and then check which ones are repeated. 

The matrix A is a 4x4 matrix. Finding eigenvalues of a 4x4 matrix can be a bit tedious, but maybe there's a pattern or a block structure that can simplify the process. Let me look at the matrix again:

A = 
[ 2   0    0     0 ]
[ 1  -1    0     0 ]
[ 3   5   -2    -2 ]
[-2  3    3     5 ]

Hmm, let me see if the matrix is block triangular. If it can be divided into blocks such that the blocks below the diagonal are zero, then the eigenvalues of the entire matrix are the eigenvalues of the diagonal blocks. 

Looking at the matrix, the first two rows and columns seem to form a 2x2 block, and the last two rows and columns form another 2x2 block. Let me check:

First block (top-left 2x2):
[2  0]
[1 -1]

Second block (bottom-right 2x2):
[-2  -2]
[ 3   5]

The entries in positions (3,1), (3,2), (4,1), and (4,2) are non-zero, so actually, the matrix isn't block triangular. Wait, no. Block triangular would have blocks below the diagonal, but here, the lower-left blocks (rows 3-4, columns 1-2) are non-zero, but the upper-right blocks (rows 1-2, columns 3-4) are zero. So actually, the matrix is block lower triangular. 

Yes, that's right! A block lower triangular matrix has eigenvalues that are the eigenvalues of the diagonal blocks. So even though there are non-zero elements below the diagonal blocks, as long as the upper right blocks are zero, it's block lower triangular. So in this case, since the matrix is divided into two 2x2 blocks on the diagonal, and the block above the diagonal is zero, the eigenvalues of A are the eigenvalues of the top-left 2x2 block combined with the eigenvalues of the bottom-right 2x2 block. 

That simplifies things! So I can compute the eigenvalues of each 2x2 block separately and then combine them. Let's start with the first block:

First block:
[2  0]
[1 -1]

The eigenvalues of a 2x2 matrix can be found by solving the characteristic equation det(λI - B) = 0, where B is the block. 

So for the first block, let's call it B:

det(λI - B) = det([λ - 2, 0], [-1, λ + 1]) = (λ - 2)(λ + 1) - (0)(-1) = (λ - 2)(λ + 1)

Setting this equal to zero gives eigenvalues λ = 2 and λ = -1. 

So the first two eigenvalues are 2 and -1.

Now, the second block is the bottom-right 2x2 matrix:

C = 
[-2  -2]
[3    5]

Again, compute its eigenvalues. Let's compute the characteristic polynomial:

det(λI - C) = det([λ + 2, 2], [-3, λ - 5])

Calculating the determinant: (λ + 2)(λ - 5) - (2)(-3) = λ² -5λ + 2λ -10 + 6 = λ² -3λ -4

Wait, let's compute it step by step:

First, expand (λ + 2)(λ - 5):

= λ*(λ -5) + 2*(λ -5) = λ² -5λ + 2λ -10 = λ² -3λ -10

Then subtract (2)*(-3) which is -6, but since it's det(λI - C), it's (λ + 2)(λ -5) - (2)(-3) = (λ² -3λ -10) +6 = λ² -3λ -4.

So the characteristic polynomial is λ² -3λ -4. Let's factor this:

Looking for two numbers that multiply to -4 and add to -3. Those numbers are -4 and +1.

Therefore, λ² -3λ -4 = (λ -4)(λ +1). Wait, but (λ -4)(λ +1) = λ² -3λ -4. Yes, that's correct. So the eigenvalues are λ =4 and λ = -1.

Wait, hold on. The eigenvalues for the second block are 4 and -1? Let me verify:

det(λI - C) = (λ + 2)(λ -5) +6 = λ² -5λ +2λ -10 +6 = λ² -3λ -4. 

Yes, roots are (3 ± sqrt(9 +16))/2 = (3 ±5)/2 => 8/2=4 and -2/2=-1. Yes, so 4 and -1.

So eigenvalues for the second block are 4 and -1. 

Therefore, combining the eigenvalues from both blocks, the eigenvalues of the entire matrix A are 2, -1, 4, -1. 

Wait, so -1 appears twice? Because the first block had eigenvalues 2 and -1, and the second block had eigenvalues 4 and -1. So combining them, the eigenvalues are 2, -1, 4, -1. Therefore, the multiple eigenvalue is -1 with algebraic multiplicity 2. The others (2 and 4) are simple eigenvalues with multiplicity 1.

Therefore, the multiple eigenvalue of matrix A is -1.

But let me make sure that the matrix is indeed block lower triangular. Let me check the structure again. The original matrix A:

Row 1: [2, 0, 0, 0]

Row 2: [1, -1, 0, 0]

Row 3: [3, 5, -2, -2]

Row 4: [-2, 3, 3, 5]

So, if we partition this into four 2x2 blocks, the top-left block is rows 1-2, columns 1-2; the top-right block is rows 1-2, columns 3-4 (which are all zeros); the bottom-left block is rows 3-4, columns 1-2 (non-zero); and the bottom-right block is rows 3-4, columns 3-4. 

Yes, so the matrix is block lower triangular because the top-right block is zero. Therefore, its eigenvalues are the union of the eigenvalues of the diagonal blocks. Therefore, my previous conclusion holds. 

But wait, just to be thorough, is there any chance that the matrix could have more multiple eigenvalues? For instance, even if the blocks are considered, maybe due to some symmetry or other reasons, but looking at the eigenvalues we found: 2, -1, 4, -1. So only -1 is repeated. 

But maybe there's a mistake here? Let's compute the eigenvalues of the entire matrix to confirm. 

Alternatively, perhaps the process is correct, but to be 100% sure, maybe I should compute the characteristic polynomial of the entire matrix and see if it factors as (λ -2)(λ +1)^2(λ -4). If that's the case, then indeed the eigenvalues are 2, -1 (twice), and 4. 

But computing the characteristic polynomial for a 4x4 matrix is time-consuming, but maybe manageable here. Let's try. 

The characteristic polynomial is det(λI - A). Let's write down λI - A:

λI - A = 

[λ -2, 0,    0,    0   ]
[ -1, λ +1,  0,    0   ]
[ -3, -5, λ +2,   2    ]
[ 2,  -3,  -3, λ -5   ]

Now, computing the determinant of this 4x4 matrix. Since there are zeros in the first two columns of the top-right part, maybe expanding along the first row or column would be efficient. 

Looking at the first row: [λ -2, 0, 0, 0]. The determinant can be expanded along the first row. 

det(λI - A) = (λ -2)*det(minor) - 0 + 0 - 0 = (λ -2)*det(minor matrix).

The minor matrix here is the 3x3 matrix obtained by removing the first row and column:

Minor matrix:
[λ +1,  0,    0   ]
[ -5, λ +2,   2    ]
[ -3,  -3, λ -5   ]

Wait, actually, no. When we remove the first row and first column, we get:

Row 2, column 2 becomes the first entry:

Original matrix without first row and column:

[λ +1, 0,    0    ]
[ -5, λ +2,  2    ]
[ -3, -3, λ -5    ]

Wait, let me check again. The original λI - A matrix is:

Row 1: [λ-2, 0, 0, 0]

Row 2: [-1, λ+1, 0, 0]

Row 3: [-3, -5, λ+2, 2]

Row 4: [2, -3, -3, λ-5]

So removing first row and first column gives:

Row 2: [λ+1, 0, 0]

Row 3: [-5, λ+2, 2]

Row 4: [-3, -3, λ-5]

Therefore, the minor matrix is:

[λ +1, 0,    0    ]
[ -5, λ +2,  2    ]
[ -3, -3, λ -5    ]

Now, compute the determinant of this 3x3 matrix. Let's do that. Again, this matrix has some zeros, so maybe expanding along the first row.

det(minor) = (λ +1)*det([λ +2, 2], [-3, λ -5]) - 0 + 0.

So compute that 2x2 determinant:

(λ +2)(λ -5) - (2)(-3) = λ² -5λ +2λ -10 +6 = λ² -3λ -4.

So det(minor) = (λ +1)(λ² -3λ -4).

Therefore, the determinant of λI - A is (λ -2)*(λ +1)*(λ² -3λ -4). 

But λ² -3λ -4 factors into (λ -4)(λ +1). So:

det(λI - A) = (λ -2)*(λ +1)*(λ -4)*(λ +1) = (λ -2)(λ -4)(λ +1)^2.

Therefore, the characteristic polynomial is (λ -2)(λ -4)(λ +1)^2. So the eigenvalues are 2, 4, and -1 with multiplicity 2. 

Hence, the multiple eigenvalue is -1 with algebraic multiplicity 2. 

Therefore, the answer is -1.

**Final Answer**
The multiple eigenvalue of the matrix \( A \) is \boxed{-1}.
</think>

To determine the multiple eigenvalue of the matrix \( A = \begin{bmatrix} 2 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 \\ 3 & 5 & -2 & -2 \\ -2 & 3 & 3 & 5 \\ \end{bmatrix} \), we first recognize that the matrix is block lower triangular. This means the eigenvalues of \( A \) are the eigenvalues of the diagonal blocks.

1. **Top-left 2x2 block:**
   \[
   \begin{bmatrix} 2 & 0 \\ 1 & -1 \end{bmatrix}
   \]
   The characteristic polynomial is:
   \[
   \det(\lambda I - B) = (\lambda - 2)(\lambda + 1)
   \]
   Eigenvalues: \( \lambda = 2 \) and \( \lambda = -1 \).

2. **Bottom-right 2x2 block:**
   \[
   \begin{bmatrix} -2 & -2 \\ 3 & 5 \end{bmatrix}
   \]
   The characteristic polynomial is:
   \[
   \det(\lambda I - C) = (\lambda + 2)(\lambda - 5) + 6 = \lambda^2 - 3\lambda - 4
   \]
   Factoring gives:
   \[
   (\lambda - 4)(\lambda + 1)
   \]
   Eigenvalues: \( \lambda = 4 \) and \( \lambda = -1 \).

Combining the eigenvalues from both blocks, we get the eigenvalues of \( A \) as \( 2, -1, 4, -1 \). The eigenvalue \( -1 \) is repeated twice, indicating it has algebraic multiplicity 2.

To confirm, we compute the characteristic polynomial of the entire matrix \( A \):
\[
\det(\lambda I - A) = (\lambda - 2)(\lambda + 1)^2(\lambda - 4)
\]
This confirms the eigenvalues are \( 2, 4, \) and \( -1 \) (with multiplicity 2).

Thus, the multiple eigenvalue of the matrix \( A \) is \(\boxed{-1}\).

## AI's Thinking (Attempted Solution Process)

The problem asks about the maximum modulus principle for a connected analytic subset $X$ of a domain $U \subset \mathbb{C}^n$, even when $X$ has singularities. The question: if $f: U \to \mathbb{C}$ is holomorphic and $|f|$ attains its maximum on $X$, must $f$ be constant on $X$?

Let me think about this carefully.

First, answer leak check: The problem statement doesn't contain any leaked answer or solution sketch. It's a clean question. Good.

Now let me think about the mathematics.

The classical maximum modulus principle says: if $f$ is holomorphic on a domain $U \subset \mathbb{C}^n$ and $|f|$ attains its maximum at an interior point of $U$, then $f$ is constant on $U$.

The question is about restricting to an analytic subset $X \subset U$. The question: if $|f|$ attains its maximum on $X$ (meaning at some point of $X$, $|f|$ achieves the sup over $X$), must $f$ be constant on $X$?

Wait, let me re-read. "if $f : U \to \mathbb{C}$ is a holomorphic function whose modulus attains its maximum on $X$, must $f$ be constant on $X$?"

So the maximum of $|f|$ restricted to $X$ is attained at some point of $X$. Does this force $f$ to be constant on $X$?

This is the maximum modulus principle on analytic sets. The answer is yes, it holds, even with singularities.

Let me think about why.

The key idea: An analytic subset $X$ of a domain in $\mathbb{C}^n$ has a regular part (smooth part) $X_{\text{reg}}$ which is a complex manifold, and a singular part $X_{\text{sing}}$ which is a proper analytic subset. The regular part $X_{\text{reg}}$ is open and dense in $X$ (in the induced topology), and it's a complex manifold.

If $f$ is holomorphic on $U$, then $f|_X$ is holomorphic on $X$ (in the sense of being a holomorphic function on the analytic set).

Case 1: The maximum is attained at a regular point $p \in X_{\text{reg}}$.

At a regular point, $X$ is locally a complex submanifold of $\mathbb{C}^n$. So locally near $p$, $X$ looks like $\mathbb{C}^k$ for some $k = \dim_p X$. The restriction $f|_X$ is holomorphic on this submanifold. By the classical maximum modulus principle on complex manifolds, if $|f|$ attains its maximum at $p$ relative to a neighborhood in $X$, then $f$ is constant on the connected component of $X_{\text{reg}}$ containing $p$.

But we need to be careful: the maximum is attained over all of $X$, not just locally. So $|f(p)| = \sup_{x \in X} |f(x)|$. In particular, $|f|$ attains a local maximum at $p$ in $X$. By the maximum modulus principle on the complex manifold $X_{\text{reg}}$, $f$ is constant on the connected component of $X_{\text{reg}}$ containing $p$.

Case 2: The maximum is attained only at a singular point.

Hmm, this is trickier. Let me think.

Actually, let me think more carefully. The question is whether $f$ must be constant on $X$ (the whole connected analytic set).

Approach: Use the regular part. $X_{\text{reg}}$ is a complex manifold, and $X_{\text{sing}}$ is a proper analytic subset of $X$ (lower dimension). 

If $|f|$ attains its maximum on $X$ at some point $p$:
- If $p \in X_{\text{reg}}$: By the maximum modulus principle on the complex manifold $X_{\text{reg}}$, $f$ is constant on the connected component of $X_{\text{reg}}$ containing $p$. Since $X$ is connected and $X_{\text{reg}}$ is dense in $X$, and $X_{\text{sing}}$ has lower dimension, the connected component of $X_{\text{reg}}$ containing $p$... hmm, is $X_{\text{reg}}$ connected if $X$ is connected?

Actually, $X_{\text{reg}}$ might not be connected even if $X$ is connected. For example, consider $X = \{z \in \mathbb{C}^2 : z_1 z_2 = 0\}$, which is the union of two axes. This is connected (they meet at the origin), but $X_{\text{reg}} = \{z_1 = 0, z_2 \neq 0\} \cup \{z_2 = 0, z_1 \neq 0\}$, which has two connected components.

But wait, in this case, if $f$ is constant on one component of $X_{\text{reg}}$, say $f = c$ on $\{z_1 = 0, z_2 \neq 0\}$, then by continuity $f = c$ on $\{z_1 = 0\}$ (the closure includes the origin). Similarly, if $f$ is constant on the other component... but we only know $f$ is constant on the component containing $p$.

Hmm, let me reconsider. Let me think about whether the answer is actually yes.

Actually, let me reconsider the problem. The question is whether the maximum modulus principle holds. Let me think about a potential counterexample.

Consider $X = \{z_1 z_2 = 0\} \subset \mathbb{C}^2$. This is connected (the two axes meet at origin). Let $f(z_1, z_2) = z_1$. Then $f|_X$: on the $z_1$-axis ($z_2 = 0$), $f = z_1$; on the $z_2$-axis ($z_1 = 0$), $f = 0$.

The maximum of $|f|$ on $X$... well, $X$ is unbounded, so $|f|$ doesn't attain a maximum. We need $X$ to be in a bounded domain, or we need the maximum to be attained.

Let me take $U$ to be a bounded domain, say the unit ball $B \subset \mathbb{C}^2$, and $X = \{z_1 z_2 = 0\} \cap B$. Then $X$ is connected (the two axes meet at origin, which is in $B$). $f(z_1, z_2) = z_1$.

On $X$: $|f|$ on the $z_1$-axis is $|z_1|$ which ranges over $[0, 1)$ (in the open ball). On the $z_2$-axis, $f = 0$. So $\sup_X |f| = 1$ but it's not attained (since the ball is open). 

So we need a closed analytic subset or the max to be attained. Let me think about this differently.

Actually, the problem says "whose modulus attains its maximum on $X$". So we're given that the maximum is attained. The question is whether $f$ must be constant on $X$.

Let me think about whether there's a counterexample.

Consider $X = \{z_1 z_2 = 0\} \cap \overline{B}$... no, we need $X$ to be an analytic subset of a domain $U$. Analytic subsets are defined by vanishing of holomorphic functions, and they're closed in $U$ but $U$ is open.

Hmm, let me think about this more carefully. If $U$ is a bounded domain and $X$ is an analytic subset of $U$, then $X$ is closed in $U$ but not necessarily compact. The maximum of $|f|$ on $X$ might not be attained in general. The problem assumes it is attained.

Let me try a different approach. Let me think about whether the answer is yes.

Claim: Yes, the maximum modulus principle holds on connected analytic sets, even with singularities.

Proof sketch:
1. $X_{\text{reg}}$ is a complex manifold, dense in $X$.
2. If $|f|$ attains its max on $X$ at $p \in X_{\text{reg}}$, then by MMP on manifolds, $f$ is constant on the connected component of $X_{\text{reg}}$ containing $p$.
3. By continuity, $f$ is constant on the closure of that component in $X$.
4. Need to show this closure is all of $X$ (using connectedness of $X$).

For step 4: The issue is that $X_{\text{reg}}$ might have multiple connected components. But if $f$ is constant on one component and we know $|f|$ attains its max there, we need to propagate.

Actually, let me think about this differently. Let me use the fact that $f$ is holomorphic on all of $U$, not just on $X$.

Alternative approach: Since $f$ is holomorphic on $U \subset \mathbb{C}^n$, and $|f|$ attains its maximum on $X$ at a point $p \in X$, we have $|f(p)| \geq |f(x)|$ for all $x \in X$.

If $p \in X_{\text{reg}}$, then locally $X$ is a complex submanifold, and $|f|$ has a local max on this submanifold at $p$. By MMP on the submanifold, $f$ is locally constant on $X$ near $p$. 

Now, the set $S = \{x \in X_{\text{reg}} : f(x) = f(p)\}$ is both open and closed in $X_{\text{reg}}$ (open by MMP, closed by continuity). So $f$ is constant on each connected component of $X_{\text{reg}}$ that intersects $S$.

But we need more: we need $f$ constant on all of $X$.

Key insight: $f$ is constant on a connected component $C$ of $X_{\text{reg}}$ with value $f(p) = c$, and $|c| = \max_X |f|$. Now consider any other connected component $C'$ of $X_{\text{reg}}$. We have $|f| \leq |c|$ on $C'$. If $C'$ shares a limit point with $C$ (in $X$), then by continuity $f = c$ at that limit point, and then by MMP on $C'$, $f = c$ on $C'$.

But do all components of $X_{\text{reg}}$ share limit points? In a connected analytic set, the components of $X_{\text{reg}}$ are connected through $X_{\text{sing}}$. 

Hmm, but this isn't quite enough. Let me think about the example $X = \{z_1 z_2 = 0\}$ again. $X_{\text{reg}}$ has two components: $C_1 = \{z_2 = 0, z_1 \neq 0\}$ and $C_2 = \{z_1 = 0, z_2 \neq 0\}$. They share the limit point $(0,0) \in X_{\text{sing}}$.

If $f = c$ on $C_1$ with $|c| = \max$, then by continuity $f(0,0) = c$. Now on $C_2$, $|f| \leq |c|$ and $f$ approaches $c$ at the limit point $(0,0)$. But $(0,0) \notin C_2$, so we can't directly apply MMP on $C_2$.

However, $f$ is holomorphic on $U$, and on $C_2 = \{z_1 = 0, z_2 \neq 0\}$, $f(0, z_2)$ is a holomorphic function of $z_2$ (on the punctured disk, say). We have $|f(0, z_2)| \leq |c|$ and $\lim_{z_2 \to 0} f(0, z_2) = c$. By the removable singularity theorem (or just by continuity of $f$ on $U$), $f(0, z_2)$ extends holomorphically to $z_2 = 0$ with value $c$. Now $|f(0, z_2)| \leq |c|$ and $f(0, 0) = c$, so by MMP on the disk, $f(0, z_2) = c$ for all $z_2$.

So in this example, it works. The key is that $f$ is holomorphic on all of $U$, not just on $X$, so we can use the extension to the singular points.

Let me try to make this general.

General proof:

Let $X$ be a connected analytic subset of a domain $U \subset \mathbb{C}^n$, and $f: U \to \mathbb{C}$ holomorphic with $|f|$ attaining its maximum on $X$ at a point $p \in X$. Let $M = |f(p)| = \max_{x \in X} |f(x)|$.

Let $S = \{x \in X : |f(x)| = M\}$. This is a closed subset of $X$ (by continuity of $f$). We want to show $S = X$, i.e., $f$ is constant on $X$ (with $|f| = M$; actually $f$ could take values on the circle $|w| = M$, but by connectedness and continuity, $f$ must be a single constant).

Wait, actually $S = \{x \in X : |f(x)| = M\}$ is closed. If we can show $S$ is also open in $X$, then by connectedness $S = X$, and $f$ maps $X$ into the circle $\{|w| = M\}$. Since $X$ is connected and $f$ is continuous, $f(X)$ is connected in $\{|w| = M\}$, which means $f$ is constant on $X$.

So the key is to show $S$ is open in $X$.

Take $q \in S$. We need to show that near $q$ in $X$, all points are in $S$.

Case 1: $q \in X_{\text{reg}}$. Then locally $X$ is a complex submanifold of dimension $k \geq 1$ (if $k = 0$, $X$ is discrete, but $X$ is connected so $X$ is a point, trivial). $f|_X$ is holomorphic on this submanifold, and $|f|$ attains its max at $q$. By MMP on the submanifold, $f$ is constant (= $f(q)$) in a neighborhood of $q$ in $X$. So $S$ is open near $q$.

Case 2: $q \in X_{\text{sing}}$. This is the tricky case. We need to show that $f$ is constant near $q$ in $X$.

At a singular point, we can use the local structure of analytic sets. Near $q$, $X$ is defined by the vanishing of some holomorphic functions. The key tool is the local parametrization or the fact that $X_{\text{reg}}$ is dense in $X$.

Since $X_{\text{reg}}$ is dense in $X$, there exist points of $X_{\text{reg}}$ arbitrarily close to $q$. At such points $q' \in X_{\text{reg}} \cap S$... wait, we don't know that $q' \in S$. We know $q \in S$ (i.e., $|f(q)| = M$), but nearby regular points might have $|f| < M$.

Hmm, so the issue is: at a singular point $q$ where $|f(q)| = M$, we need to show $f$ is constant near $q$ in $X$.

Let me think about this. Near $q$, $X$ is an analytic set. The regular part $X_{\text{reg}} \cap B$ (for a small ball $B$ around $q$) is a complex manifold (possibly with several connected components, each of some dimension).

On each connected component $C$ of $X_{\text{reg}} \cap B$, $f|_C$ is holomorphic and $|f| \leq M$ on $C$ (since $M$ is the global max on $X$). If $q$ is in the closure of $C$, then $\lim_{x \to q, x \in C} f(x) = f(q)$ (by continuity), and $|f(q)| = M$. 

Now, $f|_C$ is holomorphic on $C$ with $|f| \leq M$, and $f$ approaches $f(q)$ with $|f(q)| = M$ at the boundary point $q$. 

If $C$ is a complex manifold of dimension $\geq 1$, and $q$ is a boundary point of $C$ (in $X$), can we conclude $f$ is constant on $C$?

This is like a boundary maximum principle. Let me think...

Actually, let's use a different approach. Since $f$ is holomorphic on all of $U$ (an open set in $\mathbb{C}^n$), not just on $X$, we can use the full power of several complex variables.

Approach using the maximum modulus principle in $\mathbb{C}^n$:

If $|f|$ attains its maximum on $X$ at $q$, and if $X$ contains a complex line through $q$ (or more generally, if $X$ has positive dimension at $q$), then... hmm, but $|f|$ might not attain its maximum on all of $U$ at $q$, just on $X$.

Let me think about this differently. 

Alternative approach: Use the fact that $f$ is holomorphic on $U$ and $X$ is an analytic subset. 

Consider the restriction $f|_X$. This is a holomorphic function on the analytic set $X$ (in the sense of functions that are locally restrictions of holomorphic functions on the ambient space). 

For the maximum modulus principle on analytic sets, the standard result is:

**Theorem**: Let $X$ be a connected analytic subset of a domain $U \subset \mathbb{C}^n$, and let $f$ be a holomorphic function on $U$. If $|f|$ attains its maximum on $X$, then $f$ is constant on $X$.

The proof typically goes through the regular part and uses the density of $X_{\text{reg}}$ in $X$.

Let me try to write a clean proof.

Proof:

Let $M = \max_{x \in X} |f(x)|$ and let $p \in X$ be a point where $|f(p)| = M$. Define $A = \{x \in X : f(x) = f(p)\}$. We claim $A = X$.

First, note that $A$ is closed in $X$ (by continuity of $f$).

We show $A$ is open in $X$. Let $q \in A$, so $f(q) = f(p)$ and $|f(q)| = M$.

We need to find a neighborhood $V$ of $q$ in $X$ such that $V \subset A$.

Since $f$ is holomorphic on $U$, we can consider the function $g = f - f(q) = f - f(p)$, which is holomorphic on $U$ with $g(q) = 0$ and $|g(x)| \leq |f(x)| + |f(p)| \leq 2M$... that's not directly useful.

Better: Consider $h = f - f(p)$. Then $h$ is holomorphic on $U$, $h(q) = 0$, and for $x \in X$, $|f(x)| \leq M = |f(p)|$, so $|h(x)| = |f(x) - f(p)| \geq |f(p)| - |f(x)| \geq 0$... that gives a lower bound, not useful.

Let me think again. We want to show $f$ is constant near $q$ in $X$.

Approach: Use the local structure of analytic sets and induction on dimension.

Actually, let me use a cleaner approach. The key fact is:

**Fact**: If $X$ is an analytic set and $f$ is holomorphic in a neighborhood of $X$, and $|f|$ attains a local maximum at $q \in X$ (relative to $X$), then $f$ is constant in a neighborhood of $q$ in $X$.

Proof of fact: By induction on $\dim_q X$.

Base case: $\dim_q X = 0$. Then $X$ is discrete near $q$, so $q$ is an isolated point of $X$, and trivially $f$ is "constant" near $q$ in $X$.

Inductive step: Assume the result for dimensions $< k$, prove for $\dim_q X = k$.

If $q \in X_{\text{reg}}$: $X$ is locally a complex submanifold of dimension $k$ at $q$. By the classical MMP on complex manifolds, $f$ is constant near $q$ in $X$.

If $q \in X_{\text{sing}}$: The singular locus $X_{\text{sing}}$ is an analytic subset of $X$ with $\dim_q X_{\text{sing}} < k$ (since $q$ is a singular point, but the singular locus has strictly smaller dimension). 

Now, $X_{\text{reg}}$ is dense in $X$ near $q$. Consider a small neighborhood $B$ of $q$. The regular part $X_{\text{reg}} \cap B$ consists of finitely many connected components, each a complex manifold of dimension $k$ (the dimension of $X$ at $q$).

On each such component $C_i$, $f|_{C_i}$ is holomorphic with $|f| \leq M$ on $C_i$, and $q$ is in the closure of $C_i$ (assuming $C_i$ is a component whose closure contains $q$; some components might not have $q$ in their closure).

For a component $C_i$ with $q \in \overline{C_i}$: We have $f$ holomorphic on $C_i$ (a complex manifold), $|f| \leq M$ on $C_i$, and $\lim_{x \to q, x \in C_i} f(x) = f(q)$ with $|f(q)| = M$.

Now I need to conclude that $f$ is constant on $C_i$. 

Here's the key: $C_i$ is a complex manifold of dimension $k$, and $f$ is holomorphic on $C_i$ with $|f| \leq M$. The point $q$ is a boundary point of $C_i$ (in $X$) where $|f|$ approaches $M$. 

But this alone doesn't force $f$ to be constant on $C_i$! For example, consider the punctured disk $\{0 < |z| < 1\}$ and $f(z) = z$. Then $|f| < 1$ on the punctured disk, and $|f| \to 0$ as $z \to 0$. The sup is 1 but not attained. But if the sup were attained at the boundary point $z = 0$... well, $f(0) = 0 \neq 1$.

Hmm, let me think of a better example. Consider $f(z) = z$ on $\{0 < |z| < 1\} \cup \{0\}$, with $f(0) = 0$. Then $|f|$ on this set has sup $= 1$ (not attained). Not helpful.

What if we had $f(z) = 1$ at $z = 0$ and $f(z) = z$ for $z \neq 0$? That's not holomorphic.

OK so the point is: $f$ is holomorphic on all of $U$, so $f$ is continuous at $q$ and holomorphic in a neighborhood of $q$ in $\mathbb{C}^n$. The restriction to $C_i$ is the restriction of a function holomorphic in the ambient space.

Let me use this. Since $f$ is holomorphic in a neighborhood of $q$ in $\mathbb{C}^n$, and $C_i$ is a complex submanifold whose closure contains $q$, we can use the following:

Choose local coordinates near $q$ in $\mathbb{C}^n$ such that $C_i$ near $q$ is given by $\{z_{k+1} = \cdots = z_n = 0\}$ (after a possible reparametrization—but $C_i$ might not extend smoothly to $q$ since $q$ is a singular point of $X$).

Hmm, this is getting complicated because $C_i$ might not have a nice extension to $q$.

Let me try yet another approach. 

**Using the maximum modulus principle in $\mathbb{C}^n$ directly:**

Since $f$ is holomorphic on $U \subset \mathbb{C}^n$, and $|f|$ attains its maximum on $X$ at $p$, we have $|f(p)| \geq |f(x)|$ for all $x \in X$.

Consider the set $Y = \{z \in U : |f(z)| \leq |f(p)|\}$. This is a closed subset of $U$ containing $X$. 

Hmm, this doesn't directly help.

**Another approach: Using the local maximum modulus principle for holomorphic functions on analytic sets.**

The standard result in several complex variables is that the maximum modulus principle holds for holomorphic functions on analytic sets. The proof uses the following:

1. The regular part $X_{\text{reg}}$ is a complex manifold, and MMP holds there.
2. The singular part $X_{\text{sing}}$ has strictly lower dimension, and we use induction.
3. The key linking step uses the fact that $f$ is the restriction of a holomorphic function on the ambient space, so it extends holomorphically across singular points.

Let me try to make this precise with the induction on dimension.

**Theorem**: Let $X$ be a connected analytic subset of a domain $U \subset \mathbb{C}^n$, and $f: U \to \mathbb{C}$ holomorphic. If $|f|$ attains its maximum on $X$, then $f$ is constant on $X$.

**Proof by induction on $d = \dim X$.**

Base case $d = 0$: $X$ is a discrete set of points. Since $X$ is connected, $X$ is a single point, and $f$ is trivially constant on $X$.

Inductive step: Assume the result for all connected analytic sets of dimension $< d$, and let $\dim X = d$.

Let $M = \max_X |f|$ and $p \in X$ with $|f(p)| = M$.

Let $S = \{x \in X : |f(x)| = M\}$. $S$ is closed in $X$. We show $S$ is open in $X$.

**Case 1: $p \in X_{\text{reg}}$.** Near $p$, $X$ is a complex submanifold of dimension $d$. By the classical MMP on complex manifolds, $f$ is constant in a neighborhood of $p$ in $X$. So $S$ contains a neighborhood of $p$ in $X$.

**Case 2: $p \in X_{\text{sing}}$.** 

The singular locus $X_{\text{sing}}$ is an analytic subset of $X$ with $\dim X_{\text{sing}} < d$ (this is a standard fact: the singular locus of an analytic set has strictly smaller dimension).

Now, $X_{\text{sing}}$ might not be connected, but let $X_{\text{sing}}^0$ be the connected component of $X_{\text{sing}}$ containing $p$ (in the analytic set sense, or we can take the irreducible component). Actually, let me think about this differently.

Consider $X_{\text{sing}}$ as an analytic subset. It has dimension $< d$. The restriction $f|_{X_{\text{sing}}}$ is holomorphic (as the restriction of a holomorphic function on $U$), and $|f|$ attains its maximum on $X_{\text{sing}}$ at $p$ (since $|f(p)| = M = \max_X |f| \geq \max_{X_{\text{sing}}} |f|$, and $p \in X_{\text{sing}}$).

But wait, $X_{\text{sing}}$ might not be connected. Let $Z$ be the connected component of $X_{\text{sing}}$ containing $p$. Then $Z$ is a connected analytic set of dimension $< d$, and $|f|$ attains its maximum on $Z$ at $p$. By the inductive hypothesis, $f$ is constant on $Z$.

So $f = f(p)$ on $Z$, meaning $Z \subset S$.

But we need more: we need $S$ to contain a neighborhood of $p$ in $X$, not just in $X_{\text{sing}}$.

Now, near $p$, $X_{\text{reg}}$ is dense in $X$. The regular part near $p$ consists of finitely many connected components $C_1, \ldots, C_m$, each a complex manifold of dimension $d$ (the components of $X_{\text{reg}}$ whose closures contain $p$).

For each $C_i$: $f|_{C_i}$ is holomorphic, $|f| \leq M$ on $C_i$, and $p$ is in the closure of $C_i$ with $f(p) = f(p)$ (and $|f(p)| = M$).

I need to show $f$ is constant on each $C_i$ (with value $f(p)$).

Here's the key argument: Since $f$ is holomorphic on $U$ (open in $\mathbb{C}^n$), and $C_i$ is a $d$-dimensional complex submanifold of $U$ whose closure contains $p$, we can use the following lemma:

**Lemma**: Let $f$ be holomorphic on a domain $U \subset \mathbb{C}^n$, let $C$ be a connected complex submanifold of $U$ of dimension $d \geq 1$, and let $p \in U$ be a point in the closure of $C$ (in $\mathbb{C}^n$) with $p \in U$. If $|f| \leq M$ on $C$ and $|f(p)| = M$, then $f$ is constant on $C$ with value $f(p)$.

Proof of Lemma: Since $f$ is continuous on $U$ and $p \in \overline{C}$, we have $f(p) = \lim_{x \to p, x \in C} f(x)$. 

Consider the function $g = f - f(p)$, holomorphic on $U$, with $g(p) = 0$ and $|g(x)| = |f(x) - f(p)| \leq |f(x)| + |f(p)| \leq 2M$ on $C$. That's not tight enough.

Better: $|f(x)| \leq M$ on $C$ and $|f(p)| = M$. Write $f(p) = Me^{i\theta}$. Consider $h(z) = e^{-i\theta} f(z)$, so $h(p) = M$ (real, positive) and $|h(x)| \leq M$ on $C$, i.e., $\text{Re}(h(x)) \leq |h(x)| \leq M$ on $C$, and $\text{Re}(h(p)) = M$.

So $\text{Re}(h)$ is a harmonic function (on $U$, since $h$ is holomorphic) that attains its maximum on $C \cup \{p\}$ at $p$. 

Hmm, but $\text{Re}(h)$ is pluriharmonic (hence harmonic) on $U$, and $C \cup \{p\}$ is not open in $\mathbb{C}^n$, so the maximum principle for harmonic functions doesn't directly apply to $C \cup \{p\}$.

Let me think differently. 

Actually, here's a cleaner approach. Since $f$ is holomorphic on $U \subset \mathbb{C}^n$, and $C$ is a complex submanifold, $f|_C$ is holomorphic on $C$. The point $p$ is in the closure of $C$ but not in $C$ (since $p \in X_{\text{sing}}$ and $C \subset X_{\text{reg}}$). 

Since $f$ is holomorphic on $U$ and continuous at $p$, and $C$ is a complex manifold whose closure contains $p$, we can consider the behavior of $f|_C$ as we approach $p$.

The key insight: $f|_C$ is a bounded holomorphic function on $C$ (bounded by $M$), and it extends continuously to $p$ (with value $f(p)$, $|f(p)| = M$). 

If $C$ were a bounded symmetric domain or had some nice compactification, we could use boundary behavior of bounded holomorphic functions. But in general, $C$ is just a complex submanifold.

Let me try a more direct approach. 

Take a small ball $B$ around $p$ in $\mathbb{C}^n$. In $B$, $X$ is an analytic set. The regular part $X_{\text{reg}} \cap B$ has components $C_1, \ldots, C_m$ (those whose closures contain $p$).

For each $C_i$, since $f$ is holomorphic on $B$ and $C_i$ is a complex submanifold of $B$, $f|_{C_i}$ is holomorphic. We have $|f| \leq M$ on $C_i$ and $f \to f(p)$ as we approach $p$ in $C_i$, with $|f(p)| = M$.

Now, I claim $f$ is constant on $C_i \cap B'$ for some smaller ball $B'$.

To see this, consider the Taylor expansion of $f$ at $p$ in $\mathbb{C}^n$:
$$f(z) = f(p) + \sum_{|\alpha| \geq 1} \frac{D^\alpha f(p)}{\alpha!} (z-p)^\alpha.$$

Since $|f(p)| = M$ is the maximum of $|f|$ on $X$, and $C_i \subset X$, we have $|f(z)| \leq M$ for $z \in C_i$.

Now, $f(z) - f(p) = \sum_{|\alpha| \geq 1} c_\alpha (z-p)^\alpha$ where $c_\alpha = \frac{D^\alpha f(p)}{\alpha!}$.

For $z \in C_i$ approaching $p$, $f(z) - f(p) = O(|z-p|)$ (the linear terms dominate). But we also know $|f(z)| \leq M = |f(p)|$, so:
$$|f(z)|^2 \leq |f(p)|^2.$$
$$|f(p) + (f(z) - f(p))|^2 \leq |f(p)|^2.$$
$$|f(p)|^2 + 2\text{Re}(\overline{f(p)}(f(z)-f(p))) + |f(z)-f(p)|^2 \leq |f(p)|^2.$$
$$2\text{Re}(\overline{f(p)}(f(z)-f(p))) + |f(z)-f(p)|^2 \leq 0.$$

For $z \in C_i$ close to $p$, $f(z) - f(p) = L(z-p) + O(|z-p|^2)$ where $L = df(p)$ is the linear part. So:
$$2\text{Re}(\overline{f(p)} \cdot L(z-p)) + O(|z-p|^2) \leq 0.$$

This means $\text{Re}(\overline{f(p)} \cdot L(z-p)) \leq O(|z-p|^2)$ for $z \in C_i$ near $p$.

Now, $C_i$ is a complex submanifold, so near $p$ (in the closure), $C_i$ can be parametrized. Actually, $C_i$ doesn't include $p$, but $p$ is in its closure. The tangent cone of $C_i$ at $p$ is a complex cone in $T_p \mathbb{C}^n = \mathbb{C}^n$.

The tangent cone $T_p C_i$ is a complex analytic cone (a cone that is also an analytic set). For $v \in T_p C_i$, there exists a curve $\gamma: (0, \epsilon) \to C_i$ with $\gamma(t) \to p$ and $\frac{\gamma(t) - p}{|\gamma(t) - p|} \to \frac{v}{|v|}$ (or $\gamma(t) - p = t v + o(t)$).

For such $v$ and the curve $\gamma(t) = p + tv + o(t)$:
$$\text{Re}(\overline{f(p)} \cdot L(tv)) + O(t^2) \leq 0.$$
$$t \cdot \text{Re}(\overline{f(p)} \cdot L(v)) + O(t^2) \leq 0.$$

Dividing by $t$ and letting $t \to 0^+$:
$$\text{Re}(\overline{f(p)} \cdot L(v)) \leq 0.$$

Since $T_p C_i$ is a complex cone (closed under multiplication by complex scalars), if $v \in T_p C_i$, then $iv \in T_p C_i$ as well. So:
$$\text{Re}(\overline{f(p)} \cdot L(iv)) \leq 0.$$
$$\text{Re}(i \cdot \overline{f(p)} \cdot L(v)) \leq 0.$$
$$-\text{Im}(\overline{f(p)} \cdot L(v)) \leq 0.$$

And replacing $v$ by $-v$ (which is also in the cone since it's a cone):
$$\text{Re}(\overline{f(p)} \cdot L(-v)) \leq 0 \implies -\text{Re}(\overline{f(p)} \cdot L(v)) \leq 0 \implies \text{Re}(\overline{f(p)} \cdot L(v)) \geq 0.$$

Combined with $\text{Re}(\overline{f(p)} \cdot L(v)) \leq 0$, we get $\text{Re}(\overline{f(p)} \cdot L(v)) = 0$.

Similarly, $-iv \in T_p C_i$ gives $\text{Im}(\overline{f(p)} \cdot L(v)) \geq 0$, and combined with $\text{Im}(\overline{f(p)} \cdot L(v)) \leq 0$, we get $\text{Im}(\overline{f(p)} \cdot L(v)) = 0$.

So $\overline{f(p)} \cdot L(v) = 0$ for all $v \in T_p C_i$, i.e., $df(p)|_{T_p C_i} = 0$ (up to the scalar $\overline{f(p)}$, but since $|f(p)| = M > 0$—if $M = 0$ then $f = 0$ on $X$ and we're done—we can divide).

Wait, if $M > 0$, then $\overline{f(p)} \neq 0$, so $L(v) = df(p)(v) = 0$ for all $v \in T_p C_i$.

This means the first-order term vanishes on $C_i$. But we need to show all terms vanish, i.e., $f$ is constant on $C_i$.

We can continue: if $df(p)|_{T_p C_i} = 0$, then $f(z) - f(p) = O(|z-p|^2)$ for $z \in C_i$. Repeating the argument with the second-order terms:

$|f(z)|^2 \leq |f(p)|^2$ gives $2\text{Re}(\overline{f(p)}(f(z)-f(p))) + |f(z)-f(p)|^2 \leq 0$.

With $f(z) - f(p) = Q(z-p) + O(|z-p|^3)$ where $Q$ is the quadratic part:
$2\text{Re}(\overline{f(p)} \cdot Q(z-p)) + O(|z-p|^3) \leq 0$ (the $|f(z)-f(p)|^2$ term is $O(|z-p|^4)$).

Wait, $|f(z) - f(p)|^2 = O(|z-p|^4)$, so:
$2\text{Re}(\overline{f(p)} \cdot Q(z-p)) + O(|z-p|^3) \leq 0$.

For $\gamma(t) = p + tv + o(t)$ with $v \in T_p C_i$:
$2t^2 \text{Re}(\overline{f(p)} \cdot Q(v)) + O(t^3) \leq 0$.

Dividing by $t^2$: $2\text{Re}(\overline{f(p)} \cdot Q(v)) + O(t) \leq 0$, letting $t \to 0$: $\text{Re}(\overline{f(p)} \cdot Q(v)) \leq 0$.

Using the complex cone property again (replace $v$ by $iv$, $-v$, $-iv$): $\overline{f(p)} \cdot Q(v) = 0$ for all $v \in T_p C_i$.

But wait, $Q$ is a quadratic form, and $Q(iv) = i^2 Q(v) = -Q(v)$ (since $Q$ is the degree-2 part of a holomorphic function, which is a sum of terms $(z-p)^\alpha$ with $|\alpha| = 2$, so $Q(iv) = (iv)^\alpha$ summed... actually $Q$ is a homogeneous polynomial of degree 2 in $z-p$, so $Q(iv) = i^2 Q(v) = -Q(v)$).

So $\overline{f(p)} \cdot Q(iv) = -\overline{f(p)} \cdot Q(v)$. From $\text{Re}(\overline{f(p)} \cdot Q(iv)) \leq 0$: $\text{Re}(-\overline{f(p)} \cdot Q(v)) \leq 0$, i.e., $\text{Re}(\overline{f(p)} \cdot Q(v)) \geq 0$. Combined with $\leq 0$: $\text{Re}(\overline{f(p)} \cdot Q(v)) = 0$.

For the imaginary part: $Q(-iv) = (-i)^2 Q(v) = -Q(v)$. So $\text{Re}(\overline{f(p)} \cdot Q(-iv)) = -\text{Re}(\overline{f(p)} \cdot Q(v)) = 0$. Hmm, that gives the same. Let me use $-v$: $Q(-v) = (-1)^2 Q(v) = Q(v)$. So $\text{Re}(\overline{f(p)} \cdot Q(-v)) \leq 0$ gives the same as $\text{Re}(\overline{f(p)} \cdot Q(v)) \leq 0$.

Hmm, for the imaginary part, I need to use $iv$ and $-iv$:
- $\text{Re}(\overline{f(p)} \cdot Q(iv)) \leq 0 \implies \text{Re}(-\overline{f(p)} \cdot Q(v)) \leq 0 \implies \text{Re}(\overline{f(p)} \cdot Q(v)) \geq 0$.
- Combined with $\text{Re}(\overline{f(p)} \cdot Q(v)) \leq 0$: $\text{Re}(\overline{f(p)} \cdot Q(v)) = 0$.

But I also need $\text{Im}(\overline{f(p)} \cdot Q(v)) = 0$. Let me check: $Q(e^{i\theta} v) = e^{2i\theta} Q(v)$. So $\overline{f(p)} \cdot Q(e^{i\theta} v) = e^{2i\theta} \overline{f(p)} \cdot Q(v)$. The real part: $\text{Re}(e^{2i\theta} \overline{f(p)} \cdot Q(v)) \leq 0$ for all $\theta$ (since $e^{i\theta} v \in T_p C_i$ for all $\theta$, as $T_p C_i$ is a complex cone). This means $\text{Re}(e^{2i\theta} w) \leq 0$ for all $\theta$, where $w = \overline{f(p)} \cdot Q(v)$. But $\text{Re}(e^{2i\theta} w) \leq 0$ for all $\theta$ is impossible unless $w = 0$ (since as $\theta$ varies, $e^{2i\theta} w$ traces a circle, and the real part takes both positive and negative values unless $w = 0$).

So $\overline{f(p)} \cdot Q(v) = 0$ for all $v \in T_p C_i$.

By induction, all homogeneous terms in the Taylor expansion of $f$ at $p$, when restricted to directions in $T_p C_i$, vanish (after multiplying by $\overline{f(p)}$, and since $f(p) \neq 0$, the terms themselves vanish on $T_p C_i$).

But does this mean $f$ is constant on $C_i$? Not immediately, because $C_i$ is not exactly a cone at $p$; it's a submanifold whose tangent cone at $p$ is $T_p C_i$.

Hmm, actually, the tangent cone $T_p C_i$ captures the first-order directions. The higher-order behavior of $C_i$ near $p$ is captured by higher-order tangent data. 

Actually, let me think about this more carefully. The argument above shows that the Taylor series of $f$ at $p$ vanishes on the tangent cone $T_p C_i$ to all orders. But $C_i$ is a submanifold that approaches $p$ along directions in $T_p C_i$, and the Taylor series of $f$ at $p$ restricted to $C_i$... 

Actually, since $f$ is holomorphic (hence analytic), $f(z) = \sum_\alpha c_\alpha (z-p)^\alpha$ converges in a neighborhood of $p$. For $z \in C_i$ near $p$, $z - p$ is approximately in $T_p C_i$. The argument shows that all terms in the Taylor series vanish when evaluated on tangent directions. But the actual points $z \in C_i$ are not exactly in the tangent cone; they're in the submanifold which is tangent to the cone.

Let me think about whether this is sufficient. 

Actually, I think the cleaner approach is to use the following:

Since $f$ is holomorphic on $U$ and $|f(p)| = M$ is the maximum on $X$, and $C_i \subset X$, we have $|f| \leq M$ on $C_i$. The function $f|_{C_i}$ is a bounded holomorphic function on the complex manifold $C_i$, bounded by $M$, and it extends continuously to the boundary point $p$ with $|f(p)| = M$.

Now, here's the key: we can use the **Schwarz lemma** or **Phragmén–Lindelöf** type argument, but more directly, we use the following:

Consider the function $f|_{C_i}$ on $C_i$. Take any point $q \in C_i$ and any complex line $\ell$ in $C_i$ through $q$ (i.e., a one-dimensional complex submanifold of $C_i$ passing through $q$). Then $f|_\ell$ is a holomorphic function of one variable, bounded by $M$, and... but we don't know that $|f|$ attains $M$ on $\ell$.

Hmm, this doesn't directly work.

Let me try yet another approach. Let me use the **maximum modulus principle via subharmonic functions**.

$|f|^2$ is plurisubharmonic on $U$ (since $f$ is holomorphic). The restriction of a plurisubharmonic function to an analytic set is plurisubharmonic (this is a standard result). So $|f|^2|_X$ is plurisubharmonic on $X$.

For plurisubharmonic functions on analytic sets, the maximum principle holds: if a plurisubharmonic function on a connected analytic set attains its maximum, it is constant.

This is actually the cleanest approach. Let me elaborate.

**Key facts**:
1. If $\phi$ is plurisubharmonic on $U \subset \mathbb{C}^n$ and $X$ is an analytic subset of $U$, then $\phi|_X$ is plurisubharmonic on $X$ (in the sense of plurisubharmonic functions on analytic sets).
2. The maximum principle for plurisubharmonic functions on connected analytic sets: if $\phi$ is plurisubharmonic on a connected analytic set $X$ and $\phi$ attains its maximum on $X$, then $\phi$ is constant on $X$.

Fact 1 is standard: the restriction of a psh function to an analytic set is psh. This can be found in, e.g., Klimek's book "Pluripotential Theory" or Demailly's book.

Fact 2 follows from the fact that psh functions on analytic sets satisfy the maximum principle, which can be proved using the regular part and induction on dimension (similar to what I was doing above, but the psh framework makes it cleaner).

Actually, let me just use $|f|$ directly. $|f|$ is plurisubharmonic on $U$ (since $f$ is holomorphic, $\log|f|$ is psh, and $|f| = e^{\log|f|}$ is psh since $e^\phi$ is psh when $\phi$ is psh... actually, $|f|$ is psh because $|f| = \sup_\theta \text{Re}(e^{i\theta} f)$, and the supremum of psh functions is psh).

So $|f|$ is psh on $U$, hence $|f||_X$ is psh on $X$. By the maximum principle for psh functions on connected analytic sets, if $|f|$ attains its maximum on $X$, then $|f|$ is constant on $X$.

If $|f|$ is constant on $X$ (say $|f| = M$ on $X$), then $f(X) \subset \{|w| = M\}$. Since $X$ is connected and $f$ is continuous, $f(X)$ is a connected subset of the circle $\{|w| = M\}$, hence a single point. So $f$ is constant on $X$.

This is the cleanest proof. But I should justify the two key facts.

Let me write up the proof properly.

**Proof**:

We use the theory of plurisubharmonic functions on analytic sets.

**Step 1: $|f|$ is plurisubharmonic on $U$.**

Since $f$ is holomorphic on $U$, $\log|f|$ is plurisubharmonic on $U$ (where $\log|f| = -\infty$ at zeros of $f$). The function $t \mapsto e^t$ is convex and increasing, so $|f| = e^{\log|f|}$ is plurisubharmonic. Alternatively, $|f| = \sup_{\theta \in [0,2\pi)} \text{Re}(e^{i\theta} f)$, and each $\text{Re}(e^{i\theta} f)$ is pluriharmonic (hence psh), so $|f|$ is psh as the supremum of psh functions.

**Step 2: $|f||_X$ is plurisubharmonic on $X$.**

This is a standard result: the restriction of a plurisubharmonic function to an analytic subset is plurisubharmonic. 

*Justification*: A function $\phi$ on an analytic set $X$ is plurisubharmonic if it is upper semicontinuous and its restriction to every analytic curve in $X$ is subharmonic. Since $|f|$ is psh on $U$, its restriction to any analytic curve $\gamma \subset X \subset U$ is subharmonic (restriction of psh to a complex curve is subharmonic). Hence $|f||_X$ is psh on $X$.

**Step 3: Maximum principle for psh functions on connected analytic sets.**

If $\phi$ is a plurisubharmonic function on a connected analytic set $X$ and $\phi$ attains its global maximum on $X$, then $\phi$ is constant on $X$.

*Proof of Step 3*: Let $M = \sup_X \phi$ and suppose $\phi(p) = M$ for some $p \in X$. Let $S = \{x \in X : \phi(x) = M\}$, which is closed (by upper semicontinuity). We show $S$ is open in $X$.

- If $p \in X_{\text{reg}}$: Near $p$, $X$ is a complex manifold. On a complex manifold, the maximum principle for psh functions gives $\phi = M$ in a neighborhood of $p$ in $X$.

- If $p \in X_{\text{sing}}$: $X_{\text{sing}}$ is an analytic subset of $X$ with $\dim X_{\text{sing}} < \dim X$. The restriction $\phi|_{X_{\text{sing}}}$ is psh on $X_{\text{sing}}$ and attains its maximum at $p$. By induction on dimension (base case: dimension 0, trivial), $\phi = M$ on the connected component of $X_{\text{sing}}$ containing $p$.

  Now, $X_{\text{reg}}$ is dense in $X$, and near $p$, the components of $X_{\text{reg}}$ have $p$ in their closure. On each such component $C_i$, $\phi \leq M$ and $\phi \to M$ as we approach $p$ (by continuity, since $\phi(p) = M$ and $\phi$ is usc... actually we need $\phi$ to be continuous, which it is since $|f|$ is continuous).

  Since $\phi = |f|$ is continuous and $\phi = M$ on $X_{\text{sing}}$ near $p$, and $\phi \leq M$ on $C_i$ with $\phi \to M$ near $p$... 

  Actually, for the psh case on $C_i$ (a complex manifold), we can use the following: $\phi$ is psh on $C_i$, $\phi \leq M$, and $\phi$ approaches $M$ at the boundary point $p$. But this alone doesn't force $\phi = M$ on $C_i$ (consider $\phi(z) = |z|^2$ on the punctured disk, which approaches 0 at the origin but is not constant).

  Hmm wait, but we have more: $\phi = M$ on $X_{\text{sing}}$ near $p$, and $X_{\text{sing}}$ intersects the closure of $C_i$. So $\phi = M$ at points of $X_{\text{sing}}$ that are limit points of $C_i$.

  Actually, I realize the issue. The maximum principle for psh functions on analytic sets with singularities requires a more careful argument. Let me think about this.

  The cleanest way: use the fact that for psh functions on analytic sets, the maximum principle can be proved by reducing to the regular part and using the fact that psh functions satisfy the maximum principle on complex manifolds, combined with the density of the regular part.

  Here's a cleaner argument for Step 3:

  Let $\phi$ be psh on $X$, attaining max $M$ at $p$. Let $S = \{x \in X : \phi(x) = M\}$.

  **$S$ is open in $X$**: Take $q \in S$. 
  - If $q \in X_{\text{reg}}$: MMP on the manifold $X_{\text{reg}}$ gives $\phi = M$ near $q$ in $X$.
  - If $q \in X_{\text{sing}}$: Consider the irreducible components of $X$ passing through $q$. Each irreducible component $X_j$ has $\dim X_j \geq 1$ (if $\dim X \geq 1$) and $X_{j,\text{reg}}$ is a connected complex manifold dense in $X_j$. Since $\phi = M$ at $q$ and $\phi \leq M$ on $X_j$, and $\phi$ is continuous (in our case, $\phi = |f|$ is continuous)...

  Hmm, I keep running into the same issue. Let me think about whether the maximum principle for psh functions on singular analytic sets is actually true, or whether I need the additional structure that $\phi = |f|$ for a holomorphic $f$ on the ambient space.

  Actually, the maximum principle for psh functions on connected analytic sets IS true. Here's why:

  The key fact is: **if $\phi$ is psh on $X$ and $\phi$ is not identically $-\infty$ on any irreducible component, then $\phi$ cannot attain a local maximum unless it is locally constant.**

  For a psh function on an analytic set, the local maximum principle works as follows. Near any point $q \in X$, we can find a neighborhood $V$ and a local parametrization $\pi: D \to X \cap V$ where $D$ is a domain in some $\mathbb{C}^k$ and $\pi$ is a holomorphic map (this is the local parametrization theorem for analytic sets). Then $\phi \circ \pi$ is psh on $D$, and if $\phi$ attains a local max at $q$, then $\phi \circ \pi$ attains a local max, hence is constant, hence $\phi$ is constant on $X \cap V$.

  Wait, but $\pi$ might not be one-to-one, and $\phi \circ \pi$ being constant doesn't immediately imply $\phi$ is constant (it does if $\pi$ is surjective, which it is by the parametrization theorem).

  Actually, the local parametrization theorem says: near a point $q$ of an analytic set $X$ of dimension $d$, there exists a linear projection $\pi: \mathbb{C}^n \to \mathbb{C}^d$ such that $\pi|_X$ is a finite branched covering near $q$. More precisely, there's a neighborhood $V$ of $q$ and a domain $D \subset \mathbb{C}^d$ such that $\pi: X \cap V \to D$ is proper and finite-to-one, and $\pi(q) = 0$.

  But this doesn't directly give us a parametrization from $D$ to $X$; it gives a map from $X$ to $D$.

  Let me use a different approach. The local parametrization theorem (or Remmert's proper mapping theorem) gives: there exists a proper holomorphic map $\pi: X \cap V \to D \subset \mathbb{C}^d$ that is finite-to-one.

  If $\phi$ is psh on $X$ and attains a local max at $q$, consider $\psi = \phi \circ s$ where $s$ is a local section of $\pi$... but local sections might not exist at branch points.

  OK, let me just use the direct approach with the Taylor expansion, which I was developing earlier. That approach works specifically because $\phi = |f|$ where $f$ is holomorphic on the ambient space.

Actually, let me reconsider. The cleanest approach might be to use the following well-known result:

**Theorem (Maximum Modulus Principle on Analytic Sets)**: Let $X$ be a connected analytic subset of a domain $U \subset \mathbb{C}^n$, and let $f$ be holomorphic on $U$. If $|f|$ attains its maximum on $X$, then $f$ is constant on $X$.

This is indeed a standard result in several complex variables. The proof uses the structure theory of analytic sets. Let me write a clean proof.

**Proof**:

We proceed by induction on $d = \dim X$.

**Base case** ($d = 0$): $X$ is a discrete set. Since $X$ is connected, $X$ is a single point, and $f$ is trivially constant on $X$.

**Inductive step**: Assume the result for all connected analytic subsets of dimension $< d$. Let $\dim X = d \geq 1$.

Let $M = \max_X |f|$ and let $p \in X$ with $|f(p)| = M$. If $M = 0$, then $f = 0$ on $X$ and we are done. So assume $M > 0$.

Define $S = \{x \in X : f(x) = f(p)\}$. Since $f$ is continuous, $S$ is closed in $X$. We show $S$ is open in $X$; by connectedness of $X$, this gives $S = X$.

**Claim**: $S$ is open in $X$.

Let $q \in S$, so $f(q) = f(p)$ and $|f(q)| = M$.

**Subcase 2a: $q \in X_{\text{reg}}$.** Near $q$, $X$ is a complex submanifold of dimension $d$. The function $f|_X$ is holomorphic on this submanifold, and $|f|$ attains its maximum at $q$ (since $|f(q)| = M = \max_X |f| \geq \max_{X \cap V} |f|$ for any neighborhood $V$ of $q$). By the classical maximum modulus principle on complex manifolds, $f$ is constant in a neighborhood of $q$ in $X$. Hence $S$ contains a neighborhood of $q$ in $X$.

**Subcase 2b: $q \in X_{\text{sing}}$.** The singular locus $X_{\text{sing}}$ is a proper analytic subset of $X$, with $\dim X_{\text{sing}} < d$ (standard fact from analytic set theory). 

The restriction $f|_{X_{\text{sing}}}$ is holomorphic (as the restriction of a holomorphic function on $U$), and $|f|$ attains its maximum on $X_{\text{sing}}$ at $q$ (since $|f(q)| = M \geq |f(x)|$ for all $x \in X \supset X_{\text{sing}}$). 

Let $Z$ be the connected component of $X_{\text{sing}}$ containing $q$ (as an analytic set, $X_{\text{sing}}$ decomposes into connected components, each an analytic set). Then $Z$ is a connected analytic set with $\dim Z < d$, and $|f|$ attains its maximum on $Z$ at $q$. By the inductive hypothesis, $f$ is constant on $Z$ with value $f(q) = f(p)$. So $Z \subset S$.

Now we need to show that $S$ contains a neighborhood of $q$ in $X$ (not just in $X_{\text{sing}}$). Since $X_{\text{reg}}$ is dense in $X$, it suffices to show that $f = f(p)$ on each component of $X_{\text{reg}}$ near $q$.

Near $q$, the regular part $X_{\text{reg}}$ has finitely many connected components $C_1, \ldots, C_m$ (in a small neighborhood of $q$) whose closures contain $q$. Each $C_i$ is a complex manifold of dimension $d$.

For each $C_i$: $f|_{C_i}$ is holomorphic, $|f| \leq M$ on $C_i$, and $\lim_{x \to q, x \in C_i} f(x) = f(q) = f(p)$ (by continuity of $f$ on $U$), with $|f(p)| = M$.

We now show $f \equiv f(p)$ on $C_i$ (in a neighborhood of $q$).

Since $f$ is holomorphic on $U \subset \mathbb{C}^n$, it has a Taylor expansion at $q$:
$$f(z) = f(q) + \sum_{|\alpha| \geq 1} c_\alpha (z - q)^\alpha, \quad c_\alpha = \frac{D^\alpha f(q)}{\alpha!},$$
converging in a neighborhood of $q$ in $\mathbb{C}^n$.

For $z \in C_i$ near $q$, we have $|f(z)| \leq M = |f(q)|$. Writing $f(z) = f(q) + g(z)$ where $g(z) = f(z) - f(q) = \sum_{|\alpha| \geq 1} c_\alpha (z-q)^\alpha$:

$$|f(q) + g(z)|^2 \leq |f(q)|^2.$$
$$|f(q)|^2 + 2\operatorname{Re}(\overline{f(q)} \, g(z)) + |g(z)|^2 \leq |f(q)|^2.$$
$$2\operatorname{Re}(\overline{f(q)} \, g(z)) + |g(z)|^2 \leq 0. \quad (\star)$$

Let $T_q C_i$ denote the **tangent cone** of $C_i$ at $q$: the set of all $v \in \mathbb{C}^n$ such that there exists a sequence $z_k \in C_i$ with $z_k \to q$ and $\frac{z_k - q}{|z_k - q|} \to \frac{v}{|v|}$ (for $v \neq 0$), together with $v = 0$. The tangent cone $T_q C_i$ is a complex analytic cone (closed under multiplication by complex scalars) of dimension $d$.

For any $v \in T_q C_i$ with $v \neq 0$, there exists a curve $\gamma: (0, \epsilon) \to C_i$ with $\gamma(t) \to q$ and $\gamma(t) - q = t v + o(t)$ as $t \to 0^+$. Substituting into $(\star)$:

$$2\operatorname{Re}\!\left(\overline{f(q)} \sum_{|\alpha| \geq 1} c_\alpha (tv + o(t))^\alpha\right) + \left|\sum_{|\alpha| \geq 1} c_\alpha (tv + o(t))^\alpha\right|^2 \leq 0.$$

The leading term is $2t \operatorname{Re}(\overline{f(q)} \sum_{|\alpha|=1} c_\alpha v^\alpha) = 2t \operatorname{Re}(\overline{f(q)} \, df(q)(v))$. Dividing by $t$ and letting $t \to 0^+$:

$$\operatorname{Re}(\overline{f(q)} \, df(q)(v)) \leq 0.$$

Since $T_q C_i$ is a **complex** cone, $e^{i\theta} v \in T_q C_i$ for all $\theta$. Replacing $v$ by $e^{i\theta} v$:

$$\operatorname{Re}(\overline{f(q)} \, df(q)(e^{i\theta} v)) \leq 0 \quad \text{for all } \theta \in [0, 2\pi).$$

That is, $\operatorname{Re}(e^{i\theta} \overline{f(q)} \, df(q)(v)) \leq 0$ for all $\theta$. As $\theta$ varies, $e^{i\theta} \overline{f(q)} \, df(q)(v)$ traces a circle in $\mathbb{C}$, and its real part is $\leq 0$ for all $\theta$. This is only possible if $\overline{f(q)} \, df(q)(v) = 0$. Since $|f(q)| = M > 0$, we conclude:

$$df(q)(v) = 0 \quad \text{for all } v \in T_q C_i.$$

This means the linear term vanishes on $T_q C_i$, so $g(z) = O(|z-q|^2)$ for $z \in C_i$ near $q$.

Now repeat the argument with the quadratic term. Write $g(z) = Q_2(z-q) + O(|z-q|^3)$ where $Q_2 = \sum_{|\alpha|=2} c_\alpha (z-q)^\alpha$ is the degree-2 homogeneous part. Since $g(z) = O(|z-q|^2)$, the inequality $(\star)$ gives:

$$2\operatorname{Re}(\overline{f(q)} \, Q_2(z-q)) + O(|z-q|^3) \leq 0$$

(the $|g(z)|^2$ term is $O(|z-q|^4)$, absorbed into $O(|z-q|^3)$). For the curve $\gamma(t) = q + tv + o(t)$:

$$2t^2 \operatorname{Re}(\overline{f(q)} \, Q_2(v)) + O(t^3) \leq 0.$$

Dividing by $t^2$ and letting $t \to 0^+$: $\operatorname{Re}(\overline{f(q)} \, Q_2(v)) \leq 0$.

Again using that $T_q C_i$ is a complex cone: for $e^{i\theta} v \in T_q C_i$, $Q_2(e^{i\theta} v) = e^{2i\theta} Q_2(v)$ (since $Q_2$ is homogeneous of degree 2). So:

$$\operatorname{Re}(e^{2i\theta} \overline{f(q)} \, Q_2(v)) \leq 0 \quad \text{for all } \theta.$$

As $\theta$ varies, $e^{2i\theta}$ traces the full circle, so $\overline{f(q)} \, Q_2(v) = 0$, hence $Q_2(v) = 0$ for all $v \in T_q C_i$ (since $f(q) \neq 0$).

By induction on the degree of the homogeneous terms, we show that for every $k \geq 1$, the degree-$k$ homogeneous part $Q_k(v) = \sum_{|\alpha|=k} c_\alpha v^\alpha$ vanishes on $T_q C_i$:

- Having shown $Q_1, \ldots, Q_{k-1}$ vanish on $T_q C_i$, we have $g(z) = Q_k(z-q) + O(|z-q|^{k+1})$ on $C_i$.
- Inequality $(\star)$ gives $2\operatorname{Re}(\overline{f(q)} \, Q_k(z-q)) + O(|z-q|^{k+1}) \leq 0$ (the $|g|^2$ term is $O(|z-q|^{2k})$, absorbed).
- For $\gamma(t) = q + tv + o(t)$: $2t^k \operatorname{Re}(\overline{f(q)} \, Q_k(v)) + O(t^{k+1}) \leq 0$.
- Dividing by $t^k$ and letting $t \to 0^+$: $\operatorname{Re}(\overline{f(q)} \, Q_k(v)) \leq 0$.
- Using $Q_k(e^{i\theta} v) = e^{ik\theta} Q_k(v)$ and the complex cone property: $\operatorname{Re}(e^{ik\theta} \overline{f(q)} \, Q_k(v)) \leq 0$ for all $\theta$, hence $\overline{f(q)} \, Q_k(v) = 0$, hence $Q_k(v) = 0$.

Since the Taylor series of $f$ at $q$ converges in a neighborhood of $q$ in $\mathbb{C}^n$, and all homogeneous terms vanish on $T_q C_i$, we need to conclude that $f$ is constant on $C_i$ near $q$.

**However**, this requires care: the vanishing of $Q_k$ on $T_q C_i$ for all $k$ means that the Taylor series of $f - f(q)$ at $q$ vanishes to all orders on the tangent cone $T_q C_i$. But $C_i$ is not contained in $T_q C_i$; rather, $C_i$ is tangent to $T_q C_i$ at $q$.

To bridge this gap, we use the **local parametrization** of $C_i$ near $q$. Since $C_i$ is a complex submanifold of dimension $d$ (in $X_{\text{reg}}$) whose closure contains $q$, and $T_q C_i$ is a $d$-dimensional complex cone, we can choose local coordinates in $\mathbb{C}^n$ near $q$ such that:

- $q = 0$,
- $T_q C_i \subset \{z_{d+1} = \cdots = z_n = 0\}$ (after a linear change of coordinates, since $T_q C_i$ spans a $d$-dimensional subspace).

Wait, $T_q C_i$ is a cone, not necessarily a subspace. But it's a complex cone of dimension $d$, so it spans a $d$-dimensional linear subspace. After a linear change of coordinates, this subspace is $\mathbb{C}^d \times \{0\}$.

In these coordinates, $C_i$ near $q = 0$ can be written as a graph: $z_j = h_j(z_1, \ldots, z_d)$ for $j = d+1, \ldots, n$, where $h_j$ are holomorphic functions defined on a punctured neighborhood of $0$ in $\mathbb{C}^d$ (since $C_i$ doesn't include $q$, but $q$ is in its closure). Actually, since $C_i$ is a submanifold not including $q$, but approaching $q$...

Hmm, this is getting complicated. Let me think about whether $C_i$ can be parametrized near $q$.

Actually, $C_i$ is a connected component of $X_{\text{reg}} \cap B$ (for a small ball $B$ around $q$). It's a complex manifold of dimension $d$, but $q \notin C_i$ (since $q \in X_{\text{sing}}$). However, $q \in \overline{C_i}$.

The issue is that $C_i$ might not have a nice parametrization extending to $q$. For example, $C_i$ could be something like $\{(z, w) \in \mathbb{C}^2 : w = z^{3/2}, z \neq 0\}$... no, that's not a complex manifold in the usual sense.

Actually, since $C_i$ is a complex submanifold of $\mathbb{C}^n \setminus \{q\}$ (or rather, of $B \setminus X_{\text{sing}}$), and $q$ is in its closure, we can use the **Remmert-Stein theorem** or the fact that $C_i$ extends across $q$ as part of the analytic set $X$.

Actually, here's a better approach. Instead of trying to parametrize $C_i$, let me use the fact that $f$ is holomorphic on all of $U$ (including at $q$), and the Taylor series argument shows that $f - f(q)$ vanishes to all orders on $T_q C_i$.

Since $f$ is holomorphic at $q$, $f(z) = f(q) + \sum_{k=1}^\infty Q_k(z-q)$ where $Q_k$ are homogeneous polynomials of degree $k$. We've shown $Q_k|_{T_q C_i} = 0$ for all $k$.

Now, $T_q C_i$ is a $d$-dimensional complex cone in $\mathbb{C}^n$. Let $L = \operatorname{span}(T_q C_i)$, a $d$-dimensional linear subspace. We've shown $Q_k|_L = 0$ for all $k$ (since $Q_k$ is a polynomial and vanishes on the cone $T_q C_i$ which is not contained in any hyperplane of $L$, so $Q_k$ vanishes on all of $L$ by homogeneity).

Wait, does $Q_k$ vanishing on $T_q C_i$ imply $Q_k$ vanishes on $L = \operatorname{span}(T_q C_i)$? $T_q C_i$ is a cone in $L$ of dimension $d = \dim L$. A homogeneous polynomial of degree $k$ that vanishes on a $d$-dimensional cone in $L \cong \mathbb{C}^d$... does it vanish on all of $L$?

Not necessarily! For example, $Q(z) = z_1^2$ vanishes on the cone $\{z_1 = 0\}$ which is $(d-1)$-dimensional, but not on all of $\mathbb{C}^d$. But if the cone is $d$-dimensional (full dimension in $L$), then... a $d$-dimensional cone in $\mathbb{C}^d$ must contain an open set, so $Q_k$ vanishes on an open set in $L$, hence on all of $L$.

Is $T_q C_i$ $d$-dimensional? The tangent cone of a $d$-dimensional component at a point in its closure should be $d$-dimensional. Yes, this is a standard fact: the tangent cone of an irreducible analytic set of dimension $d$ at any point has dimension $d$.

So $T_q C_i$ is a $d$-dimensional complex cone in $L \cong \mathbb{C}^d$, hence it has nonempty interior in $L$. Since $Q_k$ is a polynomial vanishing on a set with nonempty interior in $L$, $Q_k|_L = 0$.

So $f(z) - f(q) = 0$ for all $z$ in a neighborhood of $q$ in $L$ (since the Taylor series vanishes on $L$). That is, $f$ is constant (= $f(q)$) on $L \cap B'$ for some small ball $B'$ around $q$.

Now, $C_i$ is a $d$-dimensional complex submanifold whose tangent cone at $q$ is $T_q C_i \subset L$, with $\dim L = d$. So $C_i$ is tangent to $L$ at $q$. 

For $z \in C_i$ near $q$, $z$ is close to $L$ (since the tangent direction is in $L$). More precisely, after choosing coordinates so that $L = \{z_{d+1} = \cdots = z_n = 0\}$, points of $C_i$ near $q$ have $z_{d+1}, \ldots, z_n = o(|(z_1, \ldots, z_d)|)$.

Since $f$ is constant on $L \cap B'$ and $f$ is holomorphic, we can write $f(z) - f(q) = \sum_{j=d+1}^n z_j \cdot h_j(z)$ for some holomorphic functions $h_j$ (because $f - f(q)$ vanishes on $L$, so it's divisible by the ideal of $L$, which is generated by $z_{d+1}, \ldots, z_n$).

For $z \in C_i$ near $q$: $z_j = o(|z'|$ for $j > d$ where $z' = (z_1, \ldots, z_d)$. And $h_j(z) = O(1)$. So $f(z) - f(q) = O(\max_{j>d} |z_j|) = o(|z'|)$.

But we also know $|f(z)| \leq M = |f(q)|$, so from $(\star)$: $2\operatorname{Re}(\overline{f(q)}(f(z)-f(q))) \leq -|f(z)-f(q)|^2 \leq 0$, giving $\operatorname{Re}(\overline{f(q)}(f(z)-f(q))) \leq 0$.

Hmm, this gives $f(z) - f(q) = o(|z'|)$ but we need to show $f(z) = f(q)$ on $C_i$.

Let me use a different approach. Since $f - f(q)$ vanishes on $L$ to all orders (in fact, $f = f(q)$ on $L \cap B'$), and $C_i$ approaches $q$ tangent to $L$, we can use the following:

$f(z) - f(q) = \sum_{j=d+1}^{n} z_j h_j(z)$ where $h_j$ are holomorphic near $q$. On $C_i$, $z_j$ for $j > d$ are determined by $z' = (z_1, \ldots, z_d)$ via the implicit function theorem (since $C_i$ is a submanifold tangent to $L$).

Wait, but $C_i$ doesn't include $q$, so we can't directly apply the implicit function theorem at $q$. However, $C_i$ is a submanifold of $B \setminus \{q\}$, and for points of $C_i$ close to $q$, we can parametrize $C_i$ by $z'$ (since the projection onto $L$ is a local diffeomorphism on $C_i$ for points near $q$, because $C_i$ is tangent to $L$).

More precisely: for $z \in C_i$ sufficiently close to $q$, the projection $\pi: z \mapsto z' = (z_1, \ldots, z_d)$ is a local biholomorphism (since $T_z C_i$ is close to $L$ for $z$ near $q$, as $C_i$ is tangent to $L$ at $q$). So $C_i$ can be locally written as $z_j = \psi_j(z')$ for $j = d+1, \ldots, n$, where $\psi_j$ are holomorphic on some punctured neighborhood of $0$ in $\mathbb{C}^d$.

Now, $f(z) - f(q) = \sum_{j=d+1}^n \psi_j(z') h_j(z', \psi(z'))$ on $C_i$. And $|\psi_j(z')| = o(|z'|)$ (since $C_i$ is tangent to $L$ at $q$). Also $h_j$ are bounded near $q$. So $f(z) - f(q) = o(|z'|)$ on $C_i$.

From $(\star)$: $2\operatorname{Re}(\overline{f(q)}(f(z)-f(q))) + |f(z)-f(q)|^2 \leq 0$, and $f(z) - f(q) = o(|z'|)$, so $2\operatorname{Re}(\overline{f(q)}(f(z)-f(q))) \leq 0$.

Now, $f(z) - f(q) = \sum_{j=d+1}^n \psi_j(z') h_j(z', \psi(z'))$. The functions $\psi_j$ are holomorphic on a punctured neighborhood of $0$ in $\mathbb{C}^d$, and $|\psi_j(z')| = o(|z'|)$, which means $\psi_j(z') = O(|z'|^{1+\epsilon})$ for some $\epsilon > 0$ (actually, by a result of Łojasiewicz or just by the fact that $\psi_j$ is holomorphic on a punctured domain and $|\psi_j(z')|/|z'| \to 0$, we can conclude more).

Hmm, actually, $\psi_j$ is holomorphic on a punctured neighborhood of $0$ in $\mathbb{C}^d$ with $|\psi_j(z')| = o(|z'|)$. If $d \geq 2$, by Hartogs' theorem, $\psi_j$ extends holomorphically across $0$, and then $\psi_j(z') = o(|z'|)$ means $\psi_j(0) = 0$ and $d\psi_j(0) = 0$, so $\psi_j(z') = O(|z'|^2)$.

If $d = 1$, $\psi_j$ is holomorphic on a punctured disk with $|\psi_j(z')| = o(|z'|)$. Since $f$ is bounded on $C_i$ (by $M$), and $f(z) - f(q) = \sum \psi_j h_j$, we need more information. Actually, $\psi_j$ might have a pole at $0$, but $|\psi_j(z')| = o(|z'|)$ prevents poles. In fact, $|\psi_j(z')| = o(|z'|)$ means $\psi_j$ has a zero of order $\geq 2$ at $0$ (if it extends) or is $O(|z'|^{1+\epsilon})$.

Actually, for $d = 1$: $\psi_j$ is holomorphic on $0 < |z'| < r$ with $|\psi_j(z')| = o(|z'|)$. This means $\psi_j(z')/z' \to 0$ as $z' \to 0$. If $\psi_j$ has a pole of order $m$ at $0$, then $|\psi_j(z')| \sim |z'|^{-m}$, contradicting $|\psi_j| = o(|z'|)$. So $\psi_j$ has a removable singularity at $0$ (since it's bounded: $|\psi_j(z')| \leq C|z'|$ for small $z'$). After extension, $\psi_j(0) = 0$ and $\psi_j'(0) = 0$ (from $|\psi_j(z')| = o(|z'|)$). So $\psi_j(z') = O(|z'|^2)$.

For $d \geq 2$: By Hartogs, $\psi_j$ extends holomorphically to $0$, and $\psi_j(0) = 0$, $d\psi_j(0) = 0$, so $\psi_j(z') = O(|z'|^2)$.

In either case, $\psi_j(z') = O(|z'|^2)$, so $f(z) - f(q) = O(|z'|^2)$ on $C_i$.

Now we can iterate: $f(z) - f(q) = \sum_{j>d} \psi_j(z') h_j(z) = O(|z'|^2)$, and from $(\star)$, $\operatorname{Re}(\overline{f(q)}(f(z)-f(q))) \leq 0$, with $f(z) - f(q) = O(|z'|^2)$.

The function $F(z') := f(z', \psi(z')) - f(q)$ is holomorphic on a punctured neighborhood of $0$ in $\mathbb{C}^d$ (or on a neighborhood after extension), with $|F(z')| \leq 2M$ (bounded) and $F(z') = O(|z'|^2)$.

Since $F$ is bounded and holomorphic on a punctured neighborhood, it extends holomorphically to $0$ (for $d = 1$, removable singularity; for $d \geq 2$, Hartogs). After extension, $F(0) = 0$ and $dF(0) = 0$ (from $F = O(|z'|^2)$).

Now, $|f(z)| \leq M$ on $C_i$ translates to $|F(z') + f(q)| \leq M = |f(q)|$, i.e., $|F(z') + f(q)| \leq |f(q)|$. This means:

$$|F(z') + f(q)|^2 \leq |f(q)|^2$$
$$|F(z')|^2 + 2\operatorname{Re}(\overline{f(q)} F(z')) \leq 0.$$

Since $F$ is holomorphic near $0$ with $F(0) = 0$, $dF(0) = 0$, we have $F(z') = Q_2(z') + O(|z'|^3)$ where $Q_2$ is a homogeneous polynomial of degree 2. The inequality gives:

$$2\operatorname{Re}(\overline{f(q)} Q_2(z')) + O(|z'|^3) \leq 0.$$

For $z' = tv$ with $v \in \mathbb{C}^d$: $2t^2 \operatorname{Re}(\overline{f(q)} Q_2(v)) + O(t^3) \leq 0$, so $\operatorname{Re}(\overline{f(q)} Q_2(v)) \leq 0$ for all $v$. Replacing $v$ by $e^{i\theta} v$ (and $Q_2(e^{i\theta}v) = e^{2i\theta} Q_2(v)$): $\operatorname{Re}(e^{2i\theta} \overline{f(q)} Q_2(v)) \leq 0$ for all $\theta$, hence $Q_2(v) = 0$ for all $v$.

By induction (same argument as before, now on $\mathbb{C}^d$ where we have full freedom of directions), all homogeneous terms of $F$ vanish, so $F \equiv 0$, i.e., $f = f(q)$ on $C_i$ near $q$.

Wait, but I need to be more careful. The argument for $Q_k$ vanishing uses the fact that we can approach $0$ from any direction $v \in \mathbb{C}^d$. Since $F$ is now defined on a full neighborhood of $0$ in $\mathbb{C}^d$ (after extension), and $|F(z') + f(q)| \leq |f(q)|$ for $z'$ in a punctured neighborhood (corresponding to $C_i$), the inequality holds for all small $z'$, and the argument goes through.

Actually, the inequality $|F(z') + f(q)| \leq |f(q)|$ holds for $z'$ in the domain of $F$ that corresponds to $C_i$. After extension, $F$ is holomorphic near $0$, and the inequality holds on a punctured neighborhood (which is dense), so by continuity it holds at $0$ too. And for $z'$ near $0$ (including $0$), we have $|F(z') + f(q)| \leq |f(q)|$.

Now, $F$ is holomorphic near $0$ in $\mathbb{C}^d$ with $|F(z') + f(q)| \leq |f(q)|$ and $F(0) = 0$, $|f(q)| = M > 0$. The function $G(z') = F(z') + f(q)$ is holomorphic with $|G(z')| \leq M = |G(0)|$. By the **classical maximum modulus principle** on $\mathbb{C}^d$, $G$ is constant near $0$, i.e., $F \equiv 0$ near $0$.

So $f = f(q) = f(p)$ on $C_i$ near $q$. This shows $S$ contains a neighborhood of $q$ in $C_i$, and since this holds for all components $C_i$ near $q$, and also $Z \subset S$ (the singular part), $S$ contains a neighborhood of $q$ in $X$.

**Conclusion**: $S$ is both open and closed in $X$. Since $X$ is connected and $S \neq \emptyset$ (it contains $p$), we have $S = X$. Therefore $f \equiv f(p)$ on $X$, i.e., $f$ is constant on $X$. $\blacksquare$

Wait, I want to double-check the key step where I reduce to the classical MMP. After extending $F$ holomorphically to a neighborhood of $0$ in $\mathbb{C}^d$, I have $G = F + f(q)$ holomorphic near $0$ with $|G(z')| \leq |G(0)| = M$ for $z'$ in a neighborhood of $0$. By the classical maximum modulus principle in several variables (which says: if $|G|$ attains its maximum at an interior point, $G$ is constant), $G$ is constant. So $F = 0$, $f = f(q)$ on $C_i$ near $q$. 

This is correct. The classical MMP in $\mathbb{C}^d$ says: if $G$ is holomorphic on a domain $\Omega \subset \mathbb{C}^d$ and $|G|$ attains its maximum at an interior point, then $G$ is constant. Here, $|G(0)| = M$ and $|G(z')| \leq M$ for $z'$ near $0$, so $|G|$ attains its maximum at $0$, an interior point. Hence $G$ is constant.

Great, so the proof works. Let me also verify the base case and the structure of the induction.

The induction is on $d = \dim X$. The base case $d = 0$ is trivial. For the inductive step, we use the result on $X_{\text{sing}}$ (which has dimension $< d$) to handle the singular part, and the Taylor series / classical MMP argument to handle the regular part near singular points.

Actually, wait. In Subcase 2b, I used the inductive hypothesis on $Z$ (a connected component of $X_{\text{sing}}$) to conclude $f$ is constant on $Z$. But I also need $Z$ to be a connected analytic subset of $U$. Is $X_{\text{sing}}$ an analytic subset of $U$? Yes, the singular locus of an analytic set is itself an analytic set (this is a standard result). And its connected components are analytic sets.

Also, I should check: is $Z$ connected as an analytic set? Connected components of an analytic set are analytic sets, and they're connected in the topological sense. So yes, $Z$ is a connected analytic set of dimension $< d$, and the inductive hypothesis applies.

One more thing: in the argument, I need $f|_Z$ to be holomorphic on $Z$ in the sense that it's the restriction of a holomorphic function on $U$. This is true since $f$ is holomorphic on $U$ and $Z \subset X \subset U$.

I think the proof is complete. Let me also note that the key ideas are:
1. Induction on dimension, using $X_{\text{sing}}$ for the inductive step.
2. At regular points, classical MMP on the submanifold.
3. At singular points, use the inductive hypothesis on the singular locus, then handle the regular components approaching the singular point using the Taylor expansion and the complex cone property of the tangent cone, reducing to the classical MMP after extending the parametrization.

The answer to the question is **yes**: the maximum modulus principle holds for connected analytic subsets, even with singularities.

Let me now write the clean proof.

Actually, I realize I should double-check one thing: the claim that the tangent cone $T_q C_i$ is $d$-dimensional. 

$C_i$ is a connected component of $X_{\text{reg}} \cap B$ whose closure contains $q$. The dimension of $C_i$ is $d$ (the dimension of $X$ at $q$, which is the maximum dimension of $X$ near $q$). The tangent cone of $C_i$ at $q$ is the set of tangent directions of $C_i$ at $q$, and for a $d$-dimensional complex manifold approaching $q$, the tangent cone is a $d$-dimensional complex cone. This is a standard result in the theory of analytic sets (the tangent cone of an irreducible analytic set of dimension $d$ at any point has dimension $d$).

Actually, $C_i$ is not an analytic set (it's a manifold that doesn't include $q$), but its closure $\overline{C_i} \cap B$ is an irreducible analytic set (an irreducible component of $X \cap B$) of dimension $d$. The tangent cone of this irreducible component at $q$ is $d$-dimensional, and it equals $T_q C_i$ (the tangent cone of $C_i$ at $q$, defined as the set of limit directions).

OK, I'm confident the proof is correct. Let me write it up cleanly.

Let me also reconsider: do I actually need the full Taylor series argument, or can I simplify?

After extending $F$ to a holomorphic function near $0$ in $\mathbb{C}^d$, I have $G = F + f(q)$ holomorphic near $0$ with $|G(0)| = M$ and $|G(z')| \leq M$ for $z'$ in a punctured neighborhood. By continuity, $|G(z')| \leq M$ in a full neighborhood. Then by classical MMP, $G$ is constant. So $F = 0$ and $f = f(q)$ on $C_i$ near $q$.

The key steps that enable this are:
1. $C_i$ can be parametrized as a graph over its tangent space $L$ near $q$ (for points close to $q$).
2. The parametrizing functions $\psi_j$ extend holomorphically to $q$ (using removable singularity / Hartogs).
3. After extension, $F = f \circ \psi - f(q)$ is holomorphic near $0$ in $\mathbb{C}^d$ and bounded, with $|F + f(q)| \leq |f(q)|$.
4. Classical MMP gives $F = 0$.

This is cleaner than the full Taylor series argument. The Taylor series argument was needed to show that $F$ extends and is $O(|z'|^2)$, but actually, I can just use the boundedness of $f$ on $C_i$ to show $F$ is bounded, hence extends (removable singularity / Hartogs), and then classical MMP.

Wait, let me re-examine. $F(z') = f(z', \psi(z')) - f(q)$ where $\psi = (\psi_{d+1}, \ldots, \psi_n)$. The $\psi_j$ are holomorphic on a punctured neighborhood of $0$ in $\mathbb{C}^d$. We need:
(a) $\psi_j$ extend holomorphically to $0$.
(b) $F$ is bounded (so it extends if needed).

For (a): We know $|\psi_j(z')| = o(|z'|)$ (tangent to $L$). This means $\psi_j$ is bounded near $0$ (since $|\psi_j(z')| \leq |z'|$ for small $z'$). For $d \geq 2$, Hartogs gives extension. For $d = 1$, bounded holomorphic on punctured disk gives removable singularity.

After extension, $\psi_j(0) = 0$ (from $|\psi_j(z')| = o(|z'|)$, so $\psi_j(0) = \lim \psi_j(z') = 0$... wait, $|\psi_j(z')| = o(|z'|)$ means $\psi_j(z')/z' \to 0$, which gives $\psi_j(0) = 0$ and $\psi_j'(0) = 0$ for $d=1$, or $d\psi_j(0) = 0$ for general $d$).

For (b): $|F(z')| = |f(z', \psi(z')) - f(q)| \leq |f(z', \psi(z'))| + |f(q)| \leq M + M = 2M$. So $F$ is bounded. After $\psi$ extends, $F$ is holomorphic near $0$ (composition of holomorphic functions), so no extension needed for $F$.

Then $G(z') = f(z', \psi(z'))$ is holomorphic near $0$ with $G(0) = f(q)$ (since $\psi(0) = 0$, i.e., $(0, \psi(0)) = (0, 0) = q$ in our coordinates). And $|G(z')| \leq M = |G(0)|$ for $z'$ in a punctured neighborhood (where the parametrization corresponds to $C_i$). By continuity, $|G(z')| \leq M$ in a full neighborhood. By classical MMP, $G$ is constant, so $f = f(q)$ on $C_i$ near $q$.

This is much cleaner. The key insight is:
1. Parametrize $C_i$ as a graph over its tangent space.
2. The graphing functions extend holomorphically to $q$ (by boundedness + Hartogs/removable singularity).
3. The composition $f \circ \psi$ is holomorphic near $q$ in $\mathbb{C}^d$ and satisfies the classical MMP.

Let me write the final clean proof now.

Hmm, actually, I want to make sure about one thing: the parametrization of $C_i$ as a graph. $C_i$ is a $d$-dimensional complex submanifold of $\mathbb{C}^n$ (in a neighborhood of $q$, but not including $q$). The tangent cone $T_q C_i$ is a $d$-dimensional complex cone, spanning a $d$-dimensional subspace $L$. For points $z \in C_i$ close to $q$, the tangent space $T_z C_i$ is close to $L$ (is this true?).

Actually, this needs justification. The tangent cone at $q$ being $L$ (or spanning $L$) means that the directions from $q$ to points of $C_i$ approach $L$. But does the tangent space $T_z C_i$ approach $L$ as $z \to q$?

For a smooth submanifold, yes: if the tangent cone at a boundary point is $L$, then the tangent spaces approach $L$. This follows from the fact that $C_i$ is a complex submanifold and its closure is an analytic set.

More precisely: $\overline{C_i} \cap B$ is an irreducible analytic set of dimension $d$ (an irreducible component of $X \cap B$). At the point $q$, the tangent cone of this irreducible component is $T_q C_i$, which spans $L$. For $z \in C_i$ near $q$, $T_z C_i = T_z(\overline{C_i})$ (the tangent space of the analytic set at a regular point), and these tangent spaces converge to $L$ as $z \to q$ (this is a property of the tangent cone: it is the limit of tangent spaces at regular points approaching the point).

This is indeed a standard result: the tangent cone of an analytic set at a point is the limit (in the appropriate sense) of the tangent spaces at regular points approaching that point. See, e.g., Whitney's "Complex Analytic Varieties" or Chirka's "Complex Analytic Sets".

So for $z \in C_i$ sufficiently close to $q$, $T_z C_i$ is close to $L$, and the projection $\pi_L: \mathbb{C}^n \to L$ is a local biholomorphism on $C_i$ near $z$. This gives the graph parametrization.

OK, I'm now confident in the proof. Let me write it up.

Actually, I realize there might be an even simpler approach that avoids the local parametrization entirely. Let me think...

**Alternative simpler approach**: 

Use the fact that $|f|^2$ is plurisubharmonic on $U$, and its restriction to $X$ is plurisubharmonic on $X$. Then use the maximum principle for psh functions on analytic sets.

The maximum principle for psh functions on analytic sets can be proved as follows:

A psh function $\phi$ on an analytic set $X$ is psh if and only if for every holomorphic map $\gamma: \mathbb{D} \to X$ (from the unit disk), $\phi \circ \gamma$ is subharmonic on $\mathbb{D}$.

If $\phi$ attains its maximum at $p \in X$, take any holomorphic curve $\gamma: \mathbb{D} \to X$ with $\gamma(0) = p$. Then $\phi \circ \gamma$ is subharmonic on $\mathbb{D}$ and attains its maximum at $0$, so $\phi \circ \gamma$ is constant. This means $\phi$ is constant along every holomorphic curve through $p$.

But does this imply $\phi$ is constant on $X$? We need: for any $x \in X$, there exists a holomorphic curve $\gamma: \mathbb{D} \to X$ with $\gamma(0) = p$ and $\gamma(t_0) = x$ for some $t_0$. This is not obvious for a general analytic set.

However, for a connected analytic set, we can chain holomorphic curves: if $\phi$ is constant along every holomorphic curve through $p$, then $\phi = \phi(p)$ on the set of points reachable by holomorphic curves from $p$. This set is both open and closed in $X$ (open because locally, through any regular point, there are holomorphic curves in all directions; closed by continuity). By connectedness, it's all of $X$.

But wait, at singular points, are there "enough" holomorphic curves? At a singular point $q$, we need holomorphic curves through $q$ that reach into each branch of $X$. 

By the local parametrization theorem, near any point $q \in X$, there are holomorphic curves passing through $q$ in every tangent direction of $X$ at $q$. So the set of points reachable from $p$ by holomorphic curves is indeed open.

Hmm, but I need to be more careful. Let me think about whether this approach works.

Define $S = \{x \in X : \phi(x) = \phi(p)\}$ where $\phi = |f|$ (or $|f|^2$). $S$ is closed. I want to show $S$ is open.

For $q \in S$ and $q \in X_{\text{reg}}$: Through $q$, there are holomorphic curves in $X$ going in all directions of $T_q X$. Along each such curve, $\phi$ is subharmonic and attains its max at the point corresponding to $q$, so $\phi$ is constant along the curve. This gives $\phi = \phi(p)$ in a neighborhood of $q$ in $X$ (since the curves fill out a neighborhood).

For $q \in S$ and $q \in X_{\text{sing}}$: We need holomorphic curves through $q$ that reach into $X_{\text{reg}}$. By the local structure of analytic sets, such curves exist (e.g., curves transverse to $X_{\text{sing}}$ within $X$). Along each such curve $\gamma$ with $\gamma(0) = q$, $\phi \circ \gamma$ is subharmonic and attains its max at $0$, so $\phi \circ \gamma$ is constant. This gives $\phi = \phi(p)$ along each such curve, hence in a neighborhood of $q$ in $X$.

But I need to verify that the holomorphic curves through a singular point $q$ fill out a neighborhood of $q$ in $X$. This is true: by the local parametrization theorem, $X$ near $q$ is the image of a holomorphic map from a domain in $\mathbb{C}^d$ (a finite-to-one proper map), and holomorphic curves in $\mathbb{C}^d$ map to holomorphic curves in $X$.

Actually, this approach using holomorphic curves and the subharmonic maximum principle is quite clean. Let me formalize it.

**Proof using holomorphic curves**:

$\phi = |f|$ is psh
