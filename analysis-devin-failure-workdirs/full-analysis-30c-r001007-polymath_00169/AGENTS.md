# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   For an invertible $n\times n$ matrix $M$ with integer entries we define a sequence $\mathcal{S}_M=\{M_i\}_{i=0}^{\infty}$ by the recurrence $M_0=M$ ,$M_{i+1}=(M_i^T)^{-1}M_i$ for $i\geq 0$.

Find the smallest integer $n\geq 2 $  for wich there exists a normal $n\times n$ matrix with integer entries such that its sequence $\mathcal{S}_M$ is not constant and has period $P=7$ i.e $M_{i+7}=M_i$.
($M^T$ means the transpose of a matrix $M$ . A square matrix is called normal if $M^T M=M M^T$ holds).

[i]Proposed by Martin Niepel (Comenius University, Bratislava)..[/i]       — 题目文本
#   1. **Define the sequence and initial conditions:**
   Given an invertible \( n \times n \) matrix \( M \) with integer entries, we define the sequence \( \mathcal{S}_M = \{M_i\}_{i=0}^{\infty} \) by the recurrence relation:
   \[
   M_0 = M, \quad M_{i+1} = (M_i^T)^{-1} M_i \quad \text{for} \ i \geq 0.
   \]

2. **Calculate the first few terms of the sequence:**
   \[
   M_1 = (M_0^T)^{-1} M_0 = (M^T)^{-1} M.
   \]
   \[
   M_2 = (M_1^T)^{-1} M_1 = ([(M^T)^{-1} M]^T)^{-1} (M^T)^{-1} M = (M^T)^{-1} (M^T)^{-1} M = (M^T)^{-2} M^2.
   \]

3. **Inductive step:**
   Assume \( M_i = (M^T)^{-2^{i-1}} M^{2^{i-1}} \) holds for some \( i \geq 1 \). Then,
   \[
   M_{i+1} = (M_i^T)^{-1} M_i = ([(M^T)^{-2^{i-1}} M^{2^{i-1}}]^T)^{-1} (M^T)^{-2^{i-1}} M^{2^{i-1}}.
   \]
   Since \( (AB)^T = B^T A^T \),
   \[
   M_i^T = (M^{2^{i-1}})^T ((M^T)^{-2^{i-1}})^T = (M^T)^{2^{i-1}} (M^{-2^{i-1}}).
   \]
   Therefore,
   \[
   (M_i^T)^{-1} = (M^{-2^{i-1}})^{-1} ((M^T)^{2^{i-1}})^{-1} = M^{2^{i-1}} (M^T)^{-2^{i-1}}.
   \]
   Thus,
   \[
   M_{i+1} = M^{2^{i-1}} (M^T)^{-2^{i-1}} (M^T)^{-2^{i-1}} M^{2^{i-1}} = (M^T)^{-2^i} M^{2^i}.
   \]
   By induction, \( M_i = (M^T)^{-2^{i-1}} M^{2^{i-1}} \) holds for all \( i \geq 1 \).

4. **Periodicity condition:**
   We need \( M_7 = M \), which implies:
   \[
   (M^T)^{-64} M^{64} = M.
   \]
   This simplifies to:
   \[
   M^{63} = (M^T)^{64}.
   \]
   Taking the transpose of both sides, we get:
   \[
   (M^{63})^T = ((M^T)^{64})^T \implies (M^T)^{63} = M^{64}.
   \]
   Combining both equations, we have:
   \[
   M^{63} = (M^T)^{64} \quad \text{and} \quad M^{64} = (M^T)^{63}.
   \]
   These imply that \( M = (M^T)^{-1} \), meaning \( M \) is an orthogonal matrix.

5. **Orthogonal matrix with integer entries:**
   Since \( M \) is orthogonal and has integer entries, it must be a permutation matrix. For \( M_7 = M \), we need:
   \[
   M^{128} = M \implies M^{127} = I.
   \]
   Since \( 127 \) is a prime number, the permutation described by \( M \) must have a cycle of length \( 127 \). This is only possible if \( n \geq 127 \).

6. **Conclusion:**
   The smallest integer \( n \geq 2 \) for which there exists a normal \( n \times n \) matrix with integer entries such that its sequence \( \mathcal{S}_M \) is not constant and has period \( P = 7 \) is \( n = 127 \).

The final answer is \( \boxed{127} \).  — 标准解答
#   Let me analyze this problem carefully.

We have a sequence defined by $M_0 = M$, $M_{i+1} = (M_i^T)^{-1} M_i$ for an invertible $n \times n$ integer matrix $M$.

We need to find the smallest $n \geq 2$ for which there exists a **normal** $n \times n$ integer matrix whose sequence $\mathcal{S}_M$ is not constant and has period $P = 7$.

First, let me understand the recurrence. Let $M_{i+1} = (M_i^T)^{-1} M_i$.

Let me think about what happens for a normal matrix. A matrix $M$ is normal if $M^T M = M M^T$.

Let me think about the structure. Let me write $M_i$ in some factored form.

Let me think about this differently. Consider the polar-like decomposition. Actually, let me think about what the recurrence does.

$M_{i+1} = (M_i^T)^{-1} M_i$

Let me try to understand this in terms of some transformation. Let's think about $M_i = U_i R_i$ or something.

Actually, let me think about it as follows. Consider the "left polar decomposition" type thing. If $M_i$ is invertible, we can write $M_i = (M_i^T)^{-1} \cdot (M_i^T M_i)$. So $M_i = (M_i^T)^{-1} \cdot (M_i^T M_i)$, meaning $M_{i+1} = (M_i^T M_i)$... no wait.

$M_{i+1} = (M_i^T)^{-1} M_i$. 

Hmm, let me think about the relationship between consecutive terms.

Let me compute $M_{i+1}^T$:
$M_{i+1}^T = M_i^T ((M_i^T)^{-1})^T = M_i^T (M_i^{-1})^T$... wait.

$M_{i+1} = (M_i^T)^{-1} M_i$, so $M_{i+1}^T = M_i^T ((M_i^T)^{-1})^T = M_i^T (M_i^{-1})^T$... 

Hmm, $((M_i^T)^{-1})^T = ((M_i^T)^T)^{-1} = M_i^{-1}$.

So $M_{i+1}^T = M_i^T \cdot M_i^{-1}$.

And $M_{i+1}^{-1} = M_i^{-1} \cdot M_i^T$.

So $(M_{i+1}^T)^{-1} = (M_i^T M_i^{-1})^{-1} = M_i (M_i^T)^{-1}$.

Then $M_{i+2} = (M_{i+1}^T)^{-1} M_{i+1} = M_i (M_i^T)^{-1} \cdot (M_i^T)^{-1} M_i$.

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the substitution $M_i = (M_0^T)^{-i} \cdot$ something... Actually let me try to find a pattern.

Let me define $A_i = M_i^T M_i$ (the "Gram matrix"). 

$A_{i+1} = M_{i+1}^T M_{i+1} = M_i^T M_i^{-1} (M_i^T)^{-1} M_i$... 

Hmm wait, $M_{i+1}^T = M_i^T M_i^{-1}$, so 
$A_{i+1} = M_i^T M_i^{-1} (M_i^T)^{-1} M_i$.

This doesn't simplify nicely in general.

Let me try another substitution. Let $B_i = (M_i^T)^{-1} M_i = M_{i+1}$. So the map is $M \mapsto (M^T)^{-1} M$.

Let me think about what this map does to certain structured matrices.

**Key idea**: Let's think about matrices of the form $M = \lambda Q$ where $Q$ is orthogonal ($Q^T Q = I$). Then $M^T = \lambda Q^T$, $(M^T)^{-1} = \lambda^{-1} Q$, and $M_{i+1} = \lambda^{-1} Q \cdot \lambda Q = Q^2$... no wait, $M_{i+1} = (M^T)^{-1} M = \lambda^{-1} Q \cdot \lambda Q = Q^2$? No: $(M^T)^{-1} = (\lambda Q^T)^{-1} = \lambda^{-1} (Q^T)^{-1} = \lambda^{-1} Q$. So $M_{i+1} = \lambda^{-1} Q \cdot \lambda Q = Q \cdot Q = Q^2$.

Hmm, but then $M_1 = Q^2$ which is orthogonal, and $M_2 = (Q^2)^T)^{-1} Q^2 = (Q^T)^2)^{-1} Q^2 = Q^{-2} Q^2 = I$. So the sequence becomes constant at $I$ after 2 steps. Not useful for period 7.

Let me think more carefully. The map $f(M) = (M^T)^{-1} M$.

Let me try $M = $ upper triangular or something.

Actually, let me think about this problem from the perspective of the structure that's preserved.

Let me consider the substitution $M_i = P_i S_i$ where... hmm.

Let me try yet another approach. Consider the QR-like decomposition. Actually, let me think about what happens with the substitution $N_i = M_i^{-T} M_i$ (which is $M_{i+1}$). 

Let me think about the eigenvalue structure. Actually, let me try to think about this in terms of a simpler recurrence.

Let me try: suppose $M$ is such that $M^T = D M D^{-1}$ for some diagonal $D$ (i.e., $M$ is " centrosymmetric" or has some symmetry). Then $(M^T)^{-1} = D M^{-1} D^{-1}$, and $M_{i+1} = D M_i^{-1} D^{-1} M_i$.

Hmm, let me try a very specific structure. Let me consider block matrices or companion matrices.

Actually, let me think about this more carefully using the normality condition.

If $M$ is normal ($M^T M = M M^T$), what can we say?

For a normal matrix, $M$ and $M^T$ commute. So $M^T M = M M^T$.

Then $M_1 = (M^T)^{-1} M = (M^T)^{-1} M$. Since $M$ and $M^T$ commute, $(M^T)^{-1}$ and $M$ commute, so $M_1 = M (M^T)^{-1}$ as well.

Is $M_1$ normal? $M_1^T M_1 = (M^T M^{-1})((M^T)^{-1} M) = M^T M^{-1} (M^T)^{-1} M$. Since $M$ and $M^T$ commute, $M^{-1}$ and $(M^T)^{-1}$ commute, and $M^T$ commutes with $M^{-1}$... Let me be careful.

$M^T M = M M^T$ implies $M^{-1} (M^T)^{-1} = (M^T)^{-1} M^{-1}$ (taking inverse of both sides: $(MM^T)^{-1} = (M^T M)^{-1}$, so $(M^T)^{-1} M^{-1} = M^{-1} (M^T)^{-1}$). Also $M^T M^{-1} = M^{-1} M^T$ (from $M^T M = M M^T$, multiply by $M^{-1}$ on right: $M^T = M M^T M^{-1}$, and on left: $M^{-1} M^T M = M^T$, so $M^{-1} M^T = M^T M^{-1}$).

So $M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M = M^T (M^T)^{-1} M^{-1} M = I$.

Wait, that means $M_1^T M_1 = I$?! So $M_1$ is orthogonal?!

Let me double-check. $M_1^T = M^T M^{-1}$ (computed earlier). $M_1 = (M^T)^{-1} M$.

$M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M$.

Using $M^{-1} (M^T)^{-1} = (M^T)^{-1} M^{-1}$:
$= M^T (M^T)^{-1} M^{-1} M = I \cdot I = I$.

Yes! So if $M$ is normal, then $M_1$ is orthogonal: $M_1^T M_1 = I$.

And $M_1 M_1^T = (M^T)^{-1} M \cdot M^T M^{-1} = (M^T)^{-1} M M^T M^{-1} = (M^T)^{-1} M^T M M^{-1} = I$.

So $M_1$ is orthogonal (and hence also normal).

Now if $M_1$ is orthogonal, $M_1^T = M_1^{-1}$, so $(M_1^T)^{-1} = M_1$, and $M_2 = M_1 \cdot M_1 = M_1^2$.

More generally, if $M_i$ is orthogonal, $M_{i+1} = M_i^2$.

So from $M_1$ onward, $M_{i+1} = M_i^2$, meaning $M_i = M_1^{2^{i-1}}$ for $i \geq 1$.

So the sequence from $M_1$ is: $M_1, M_1^2, M_1^4, M_1^8, \ldots, M_1^{2^{i-1}}, \ldots$

For this to have period 7 (starting from $M_1$), we need $M_1^{2^7} = M_1^{2^0} = M_1$, i.e., $M_1^{128} = M_1$, i.e., $M_1^{127} = I$.

And we need the period to be exactly 7, meaning $M_1^{2^k} \neq M_1$ for $k = 1, 2, 3, 4, 5, 6$, i.e., $M_1^{2^k - 1} \neq I$ for $k = 1, \ldots, 6$, i.e., $M_1^1, M_1^3, M_1^7, M_1^{15}, M_1^{31}, M_1^{63} \neq I$.

Since 127 is prime, the order of $M_1$ must divide 127. The order is 127 (since $M_1 \neq I$ as the sequence is not constant, and 127 is prime so the only divisors are 1 and 127).

Wait, but we need to be careful. The period of the sequence $M_1, M_1^2, M_1^4, \ldots$ is the smallest $p$ such that $M_1^{2^p} = M_1$, i.e., $M_1^{2^p - 1} = I$. The order of $M_1$ divides $2^p - 1$. For the period to be exactly 7, we need the order of $M_1$ to divide $2^7 - 1 = 127$ but not divide $2^k - 1$ for any $k < 7$.

Since 127 is prime, the order of $M_1$ is either 1 or 127. If it's 127, then $127 | 2^k - 1$ iff $2^k \equiv 1 \pmod{127}$, and the order of 2 mod 127 is... 127 is prime, so the order of 2 divides 126 = 2 × 63 = 2 × 7 × 9 = 2 × 7 × 9. Let me compute: $126 = 2 \cdot 3^2 \cdot 7$.

The order of 2 mod 127: We need $2^k \equiv 1 \pmod{127}$. The order divides 126. Let me check: is the order 7? $2^7 = 128 \equiv 1 \pmod{127}$. Yes! So the order of 2 mod 127 is 7.

So if $M_1$ has order 127, then $M_1^{2^k} = M_1$ iff $2^k \equiv 1 \pmod{127}$ iff $7 | k$. So the period is exactly 7. 

So we need:
1. $M$ is a normal integer matrix, invertible.
2. $M_1 = (M^T)^{-1} M$ is an orthogonal integer matrix of order 127.
3. The sequence is not constant, which is ensured since $M_1$ has order 127 ≠ 1.

Wait, but $M_1$ needs to be an orthogonal **integer** matrix. An orthogonal integer matrix has $M_1^T M_1 = I$ with integer entries, so $M_1 \in O_n(\mathbb{Z})$, which means $M_1$ is a signed permutation matrix.

A signed permutation matrix of order 127... but signed permutation matrices have order that divides... well, a permutation matrix has order = lcm of cycle lengths. A signed permutation matrix can have order that's a bit more complex but still, the order of a signed permutation in $O_n(\mathbb{Z})$ is limited.

Actually, the order of a signed permutation matrix: each signed permutation is a permutation $\sigma$ combined with signs. The order divides... For a single cycle of length $k$ with signs, the order can be $k$ or $2k$ depending on the product of signs around the cycle.

For order 127 (which is prime), we need a cycle of length 127 (with appropriate signs). A signed permutation matrix that is a single 127-cycle with all positive signs has order 127. This requires $n \geq 127$.

But wait, can we do better? Can we have $M_1$ be orthogonal with order 127 but not a signed permutation? No—orthogonal integer matrices are exactly signed permutation matrices.

Hmm, so this approach gives $n \geq 127$. But maybe we can do better by not requiring $M_1$ to be an integer matrix?

Wait, let me reconsider. $M$ is an integer matrix, and $M_1 = (M^T)^{-1} M$. Is $M_1$ necessarily an integer matrix? Not necessarily! $M_1$ is a rational matrix in general.

But $M_1$ is orthogonal (we showed $M_1^T M_1 = I$). And $M_1$ is rational. An orthogonal rational matrix is not necessarily a signed permutation matrix!

For example, $\frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$ is orthogonal and rational but not a signed permutation.

So $M_1$ is an orthogonal **rational** matrix. The question is: what's the minimal $n$ for which there exists an orthogonal rational $n \times n$ matrix of order 127?

Hmm, but actually we need more: we need $M_1 = (M^T)^{-1} M$ for some normal integer matrix $M$. Let me think about what constraints this places.

Actually, let me reconsider. We need:
- $M$ is an $n \times n$ integer matrix, invertible, normal.
- $M_1 = (M^T)^{-1} M$ is orthogonal (automatically from normality).
- $M_1$ has order 127 (so the period is 7).
- $M_1$ is rational (since $M$ is integer).

Actually, $M_1 = (M^T)^{-1} M$. Since $M$ is integer and invertible, $(M^T)^{-1} = (M^{-1})^T$ is rational, so $M_1$ is rational. Good.

Now, conversely, given an orthogonal rational matrix $Q$ of order 127, can we find a normal integer matrix $M$ such that $(M^T)^{-1} M = Q$?

From $(M^T)^{-1} M = Q$, we get $M = M^T Q$, i.e., $M = M^T Q$. Taking transpose: $M^T = Q^T M$. So $M = Q^T M Q$... no. $M = M^T Q$ and $M^T = Q^T M$, so $M = Q^T M Q$... let me redo: $M^T = (M^T Q)^T = Q^T M$. And $M = M^T Q = Q^T M Q$. So $M = Q^T M Q$, i.e., $Q M = M Q$ (multiply by $Q$ on left: $QM = Q Q^T M Q = M Q$). So $M$ commutes with $Q$.

Also, $M = M^T Q$ means $M^T = M Q^{-1} = M Q^T$ (since $Q$ is orthogonal, $Q^{-1} = Q^T$).

So the conditions on $M$ are:
1. $M$ commutes with $Q$.
2. $M^T = M Q^T$ (equivalently $M = M^T Q$).
3. $M$ is normal (but if $M^T = M Q^T$ and $M$ commutes with $Q$, then $M^T M = M Q^T M = M M Q^T = M M^T$... let me check: $M^T M = M Q^T M$. Since $M$ commutes with $Q$, $M$ commutes with $Q^T$, so $M Q^T M = Q^T M^2$. And $M M^T = M \cdot M Q^T = M^2 Q^T = Q^T M^2$. So yes, $M^T M = M M^T$, normal is automatic.)
4. $M$ is an integer matrix.

So we need: an integer matrix $M$ that commutes with $Q$ and satisfies $M^T = M Q^T$.

From $M^T = M Q^T$: $M = (M^T)^T = (M Q^T)^T = Q M^T = Q \cdot M Q^T = Q M Q^T$. Since $M$ commutes with $Q$, $Q M Q^T = M Q Q^T = M$. Consistent.

So the key constraint is: $M^T = M Q^T$ and $M$ commutes with $Q$, with $M$ integer.

From $M^T = M Q^T$, we get $M = M^T Q$, so $M^T = M Q^T = M^T Q Q^T = M^T$. Consistent again.

Let me think about this differently. We have $M^T = M Q^T$. This means $M^T Q = M$, i.e., $M$ is determined by... hmm.

Let me think about it as: $M = M^T Q$, so if we know $M$ on one "side", the other is determined. 

Actually, let me think about the structure more carefully. Since $Q$ has order 127 (prime), the minimal polynomial of $Q$ divides $x^{127} - 1$. Over $\mathbb{Q}$, $x^{127} - 1 = (x-1)\Phi_{127}(x)$ where $\Phi_{127}(x) = x^{126} + x^{125} + \cdots + x + 1$ is the 127th cyclotomic polynomial, which is irreducible over $\mathbb{Q}$ (since 127 is prime).

So the rational canonical form of $Q$ consists of blocks corresponding to $x - 1$ (eigenvalue 1) and $\Phi_{127}(x)$ (the primitive 127th roots of unity).

For $Q$ to have order exactly 127, it must have at least one block corresponding to $\Phi_{127}(x)$. The block for $\Phi_{127}(x)$ is the companion matrix of $\Phi_{127}(x)$, which is $126 \times 126$.

So the minimal dimension for $Q$ to have order 127 is 126 (just the companion matrix of $\Phi_{127}$), or 127 if we include the eigenvalue 1 block (but we don't need it).

Wait, but we also need $Q$ to be orthogonal. The companion matrix of $\Phi_{127}$ is not orthogonal in general. We need $Q$ to be both orthogonal and rational, with order 127.

Hmm, so the question becomes: what is the minimal $n$ such that there exists an orthogonal rational $n \times n$ matrix of order 127?

An orthogonal rational matrix $Q$ of order 127: $Q^{127} = I$, $Q^T Q = I$, $Q$ rational.

Since $Q$ is orthogonal and rational, $Q^T = Q^{-1}$. And $Q^{127} = I$.

The eigenvalues of $Q$ are 127th roots of unity. Since $Q$ is real (rational), eigenvalues come in conjugate pairs. The primitive 127th roots of unity come in 63 conjugate pairs. So to have all primitive 127th roots, we'd need dimension at least 126.

But we don't need all of them. We just need $Q$ to have order 127, which means at least one primitive 127th root of unity as an eigenvalue. But since $Q$ is real, if $\zeta$ is an eigenvalue, so is $\bar{\zeta} = \zeta^{-1}$. And since $Q$ is rational, the characteristic polynomial has rational coefficients, so if $\zeta$ is a root, all conjugates (all primitive 127th roots) are roots. So the characteristic polynomial must be divisible by $\Phi_{127}(x)$, which has degree 126.

Therefore, $n \geq 126$.

Now, can we achieve $n = 126$? We need a $126 \times 126$ orthogonal rational matrix whose characteristic polynomial is $\Phi_{127}(x)$.

The companion matrix $C$ of $\Phi_{127}(x)$ has order 127 and characteristic polynomial $\Phi_{127}(x)$, but it's not orthogonal. However, we might be able to find an orthogonal rational matrix with the same characteristic polynomial.

Actually, let me think about this. The rational canonical form is unique. If $Q$ is a $126 \times 126$ rational matrix with characteristic polynomial $\Phi_{127}(x)$ (which is irreducible), then the rational canonical form of $Q$ is the companion matrix of $\Phi_{127}(x)$. So $Q = P C P^{-1}$ for some rational $P$.

For $Q$ to be orthogonal, we need $Q^T Q = I$, i.e., $P^{-T} C^T P^T P C P^{-1} = I$, i.e., $C^T (P^T P) C = P^T P$. So we need a positive definite rational matrix $S = P^T P$ such that $C^T S C = S$.

This is equivalent to finding a rational positive definite matrix $S$ that is "fixed" by the action $S \mapsto C^T S C$. 

Hmm, this is getting complicated. Let me think about whether such an $S$ exists.

Actually, there's a classical result: every finite-order rational matrix is conjugate (over $\mathbb{Q}$) to an orthogonal rational matrix. Is this true? I'm not sure.

Let me think differently. Consider the $\mathbb{Q}$-vector space $V = \mathbb{Q}^{126}$ with $Q$ acting on it. Since $\Phi_{127}$ is irreducible, $V$ is an irreducible $\mathbb{Q}[Q]$-module, isomorphic to $\mathbb{Q}(\zeta)$ where $\zeta$ is a primitive 127th root of unity.

An invariant positive definite bilinear form on $V$ corresponds to an element of $\mathbb{Q}(\zeta)$ that is fixed by the appropriate involution and is totally positive. 

The involution on $\mathbb{Q}(\zeta)$ induced by $Q \mapsto Q^T$ (which corresponds to $\zeta \mapsto \zeta^{-1} = \bar{\zeta}$) is complex conjugation. An invariant form corresponds to $\alpha \in \mathbb{Q}(\zeta)$ with $\bar{\alpha} = \alpha$ (i.e., $\alpha$ is in the maximal real subfield $\mathbb{Q}(\zeta + \bar{\zeta})$) and $\alpha$ is totally positive (positive under all embeddings).

Such elements exist (e.g., $\alpha = 1$ works if the form $S = I$ is invariant, but it's not in general). We need to find $\alpha$ in the real subfield that is totally positive.

Actually, the trace form $\text{tr}(x \bar{x})$ gives a positive definite invariant form. The trace form on $\mathbb{Q}(\zeta)/\mathbb{Q}$ is $\text{Tr}_{\mathbb{Q}(\zeta)/\mathbb{Q}}(x \bar{x})$, which is positive definite (since $\mathbb{Q}(\zeta)$ is a CM field). This gives a rational positive definite invariant bilinear form.

So yes, there exists a rational positive definite matrix $S$ with $C^T S C = S$, and then $Q = S^{1/2} C S^{-1/2}$... but $S^{1/2}$ might not be rational. 

Hmm, but we need $Q$ to be rational. Let me think again.

We have $C^T S C = S$ with $S$ rational positive definite. We want $Q = P C P^{-1}$ orthogonal with $P$ rational. This requires $P^T P = S$, i.e., $P$ is a rational "square root" of $S$ in the sense $P^T P = S$. But not every rational positive definite $S$ has a rational $P$ with $P^T P = S$ (this is the issue of representing $S$ as a sum of squares, essentially).

Hmm, this is getting complicated. Let me think about whether the answer might just be 126, or whether there are additional constraints from the requirement that $M$ is an integer matrix.

Actually, wait. Let me reconsider the problem. We need $M$ to be an integer matrix, and $M_1 = (M^T)^{-1} M$ to be orthogonal rational of order 127. But we also need $M$ to be normal.

We showed that if $M$ is normal, then $M_1$ is automatically orthogonal. And the conditions on $M$ given $Q = M_1$ are: $M$ commutes with $Q$, $M^T = M Q^T$, and $M$ is integer.

So the question is really: given an orthogonal rational matrix $Q$ of order 127, can we find an integer matrix $M$ commuting with $Q$ with $M^T = M Q^T$?

Let me think about the structure of matrices commuting with $Q$. If $Q$ has characteristic polynomial $\Phi_{127}(x)$ (irreducible), then the centralizer of $Q$ in $M_n(\mathbb{Q})$ is $\mathbb{Q}[Q] \cong \mathbb{Q}(\zeta)$. So $M = f(Q)$ for some $f \in \mathbb{Q}(\zeta)$.

The condition $M^T = M Q^T$ becomes: $f(Q)^T = f(Q) Q^T$. Since $Q$ is orthogonal, $Q^T = Q^{-1} = Q^{126}$. And $f(Q)^T = \bar{f}(Q)$ where $\bar{f}$ is the image under $\zeta \mapsto \zeta^{-1}$ (complex conjugation on $\mathbb{Q}(\zeta)$).

So the condition is $\bar{f}(Q) = f(Q) \cdot Q^{-1}$, i.e., $\bar{f}(\zeta) = f(\zeta) \cdot \zeta^{-1}$, i.e., $\bar{f}(\zeta) = f(\zeta) / \zeta$.

Let $f(\zeta) = \alpha \in \mathbb{Q}(\zeta)$. The condition is $\bar{\alpha} = \alpha / \zeta$, i.e., $\alpha = \bar{\alpha} \cdot \zeta$.

So $\alpha / \bar{\alpha} = \zeta$. This means $\alpha$ is an element of $\mathbb{Q}(\zeta)$ with $\alpha / \bar{\alpha} = \zeta$.

Such an $\alpha$ exists if and only if $\zeta$ is in the image of the norm map $N: \mathbb{Q}(\zeta)^* \to \mathbb{Q}(\zeta)^+$... actually, $\alpha / \bar{\alpha} = \zeta$ means $\alpha \bar{\alpha}^{-1} = \zeta$, so $N(\alpha) = \alpha \bar{\alpha}$ and $\alpha / \bar{\alpha} = \zeta$.

This is related to Hilbert's Theorem 90. In the extension $\mathbb{Q}(\zeta) / \mathbb{Q}(\zeta+\bar{\zeta})$ (which is a degree 2 extension with Galois group generated by complex conjugation), Hilbert's Theorem 90 says that $\zeta = \alpha / \bar{\alpha}$ for some $\alpha$ iff $N_{\mathbb{Q}(\zeta)/\mathbb{Q}(\zeta+\bar{\zeta})}(\zeta) = \zeta \bar{\zeta} = 1$. And indeed $\zeta \bar{\zeta} = |\zeta|^2 = 1$. So by Hilbert's Theorem 90, such an $\alpha$ exists in $\mathbb{Q}(\zeta)$.

So there exists $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$. Then $M = \alpha(Q)$ (i.e., $M = f(Q)$ where $f(\zeta) = \alpha$) satisfies $M^T = M Q^T$ and $M$ commutes with $Q$.

But we need $M$ to be an **integer** matrix. $M = f(Q)$ is a rational matrix (since $f$ has rational coefficients and $Q$ is rational). For $M$ to be integer, we need $f(Q)$ to have integer entries.

Since $Q$ is a rational matrix with characteristic polynomial $\Phi_{127}$, the entries of $f(Q)$ are rational. We can scale: if $\alpha$ works, then $c \alpha$ also works for any $c \in \mathbb{Q}^*$ (since $(c\alpha)/\overline{(c\alpha)} = \alpha/\bar{\alpha} = \zeta$). So we can scale $M$ by a rational constant to clear denominators, making $M$ integer.

But wait, scaling $M$ by $c$ changes $M_1 = (M^T)^{-1} M$. If $M \to cM$, then $M^T \to c M^T$, $(M^T)^{-1} \to c^{-1} (M^T)^{-1}$, and $M_1 \to c^{-1} (M^T)^{-1} \cdot c M = M_1$. So $M_1$ is unchanged! Great.

So the strategy is:
1. Find an orthogonal rational $Q$ of order 127, of size $n \times n$.
2. Find $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$ (exists by Hilbert 90).
3. Set $M = f(Q)$ where $f(\zeta) = \alpha$, then scale to make $M$ integer.

The minimal $n$ is determined by the minimal size of an orthogonal rational matrix of order 127.

As argued, $n \geq 126$ (since the characteristic polynomial must be divisible by $\Phi_{127}$ of degree 126, and eigenvalues come in conjugate pairs for real matrices, but actually the degree of $\Phi_{127}$ is already even: $\phi(127) = 126$, so a real matrix can have characteristic polynomial $\Phi_{127}$).

Wait, I need to be more careful. $\Phi_{127}(x) = x^{126} + x^{125} + \cdots + 1$ has degree 126. A real matrix can have this as its characteristic polynomial (the roots are the primitive 127th roots of unity, which come in 63 conjugate pairs, all non-real). So $n = 126$ is possible in terms of the characteristic polynomial.

Now, can we find an **orthogonal rational** $126 \times 126$ matrix with characteristic polynomial $\Phi_{127}$?

As I discussed, this requires finding a rational positive definite $S$ with $C^T S C = S$ (where $C$ is the companion matrix of $\Phi_{127}$), and then a rational $P$ with $P^T P = S$.

The existence of $S$ is guaranteed (trace form). The existence of rational $P$ with $P^T P = S$ is the question of whether $S$ is a sum of squares of rational matrices, which is always true for positive definite rational matrices (by the theory of quadratic forms over $\mathbb{Q}$—every positive definite rational quadratic form can be diagonalized, and each positive rational number is a sum of four squares, so we can write $S = P^T P$ with $P$ rational).

Wait, actually that's not quite right. $P^T P = S$ with $P$ rational and $S$ positive definite rational—this is asking whether the quadratic form represented by $S$ is equivalent over $\mathbb{Q}$ to the standard form. This is not always true! Two positive definite forms over $\mathbb{Q}$ are equivalent iff they have the same dimension, determinant (up to squares), Hasse invariant, and signature.

Hmm, but actually we don't need $P^T P = S$ exactly. We need $Q = P C P^{-1}$ to be orthogonal, which means $(PCP^{-1})^T (PCP^{-1}) = I$, i.e., $P^{-T} C^T P^T P C P^{-1} = I$, i.e., $C^T (P^T P) C = P^T P$. So $S = P^T P$ must satisfy $C^T S C = S$.

But we get to choose $S$ (any rational positive definite $S$ with $C^T S C = S$), and then we need $S = P^T P$ for some rational $P$.

The space of $S$ satisfying $C^T S C = S$ is a $\mathbb{Q}$-vector space. By the theory of the trace form, this space is 1-dimensional over the centralizer of $C$, which is $\mathbb{Q}[C] \cong \mathbb{Q}(\zeta)$. Actually, the space of invariant bilinear forms is isomorphic to the space of $\alpha \in \mathbb{Q}(\zeta)$ with $\bar{\alpha} = \alpha$ (symmetric forms) or $\bar{\alpha} = -\alpha$ (skew forms). The symmetric ones form the real subfield $\mathbb{Q}(\zeta + \bar{\zeta})$, which has dimension 63 over $\mathbb{Q}$.

So the space of symmetric invariant forms is 63-dimensional over $\mathbb{Q}$. We need to find one that is positive definite and is a sum of squares (i.e., $S = P^T P$ for rational $P$).

A positive definite form that is a sum of squares is the same as a form equivalent to the identity. By the Hasse-Minkowski theorem, a positive definite form over $\mathbb{Q}$ is equivalent to the identity iff it has the same invariants (dimension, discriminant, Hasse invariant) as the identity.

The identity form has discriminant 1 and Hasse invariant 1. So we need a symmetric invariant form with discriminant a perfect square and Hasse invariant 1.

Since the space of symmetric invariant forms is 63-dimensional, we have a lot of freedom. It seems very likely that such a form exists, but proving it rigorously requires more work.

Hmm, let me think about this differently. Maybe there's a more direct construction.

Actually, let me reconsider. Maybe I'm overcomplicating this. Let me think about whether we actually need $Q$ to be orthogonal, or whether the problem allows $M_1$ to be orthogonal over $\mathbb{R}$ but rational.

We showed that if $M$ is normal (integer), then $M_1 = (M^T)^{-1} M$ is orthogonal ($M_1^T M_1 = I$) and rational. So $M_1$ is an orthogonal rational matrix. The sequence from $M_1$ is $M_1, M_1^2, M_1^4, \ldots$ and we need period 7, so $M_1$ has order 127.

Conversely, given an orthogonal rational $Q$ of order 127, we can construct $M$ (integer, normal) with $M_1 = Q$, by Hilbert 90 and scaling.

So the minimal $n$ is the minimal dimension of an orthogonal rational matrix of order 127.

Now, I claimed $n \geq 126$. Let me also check: can we have $n = 126$?

For $n = 126$: we need a $126 \times 126$ orthogonal rational matrix $Q$ with $Q^{127} = I$ and $Q \neq I$. The characteristic polynomial must be $\Phi_{127}(x)$ (the only option for a 126-dimensional matrix with order dividing 127 and not equal to 1).

Let me think about a concrete construction. Consider the field $\mathbb{Q}(\zeta)$ where $\zeta = e^{2\pi i/127}$. This is a degree 126 extension of $\mathbb{Q}$. As a $\mathbb{Q}$-vector space, $\mathbb{Q}(\zeta) \cong \mathbb{Q}^{126}$.

Multiplication by $\zeta$ is a $\mathbb{Q}$-linear map on $\mathbb{Q}(\zeta)$, and its matrix (in some basis) is a $126 \times 126$ rational matrix of order 127. But it's not orthogonal in general.

To make it orthogonal, we need to choose the right basis. The trace form $\langle x, y \rangle = \text{Tr}(x \bar{y})$ is a positive definite $\mathbb{Q}$-bilinear form on $\mathbb{Q}(\zeta)$ that is invariant under multiplication by $\zeta$ (since $\text{Tr}(\zeta x \cdot \overline{\zeta y}) = \text{Tr}(\zeta x \cdot \bar{\zeta} \bar{y}) = \text{Tr}(|\zeta|^2 x \bar{y}) = \text{Tr}(x \bar{y})$).

So if we choose an orthonormal basis (over $\mathbb{Q}$) for the trace form, the matrix of multiplication by $\zeta$ would be orthogonal. But an orthonormal basis over $\mathbb{Q}$ for the trace form means we need the trace form to be equivalent to the standard form over $\mathbb{Q}$.

The trace form $\text{Tr}(x \bar{y})$ on $\mathbb{Q}(\zeta)/\mathbb{Q}$: its discriminant is the discriminant of $\mathbb{Q}(\zeta)$. For $\zeta$ a primitive $p$-th root of unity ($p$ prime), the discriminant of $\mathbb{Q}(\zeta)$ is $(-1)^{(p-1)/2} p^{p-2}$. For $p = 127$: disc $= (-1)^{63} \cdot 127^{125} = -127^{125}$.

The discriminant of the trace form is $-127^{125}$. For the form to be equivalent to the identity (which has discriminant 1), we'd need $-127^{125}$ to be a perfect square, which it's not (since 127 is odd and the sign is negative). So the trace form is NOT equivalent to the identity form over $\mathbb{Q}$.

Hmm. So we can't just orthonormalize the trace form.

But we don't have to use the trace form. We can use any invariant positive definite form. The space of invariant symmetric bilinear forms is $\mathbb{Q}(\zeta + \bar{\zeta})$ (the maximal real subfield), which is 63-dimensional. We need to find an element $\beta$ in this space such that the corresponding form is positive definite and equivalent to the identity over $\mathbb{Q}$.

An invariant symmetric form is $\langle x, y \rangle_\beta = \text{Tr}(\beta x \bar{y})$ for $\beta \in \mathbb{Q}(\zeta+\bar{\zeta})$, $\beta$ totally positive. The discriminant of this form is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N_{\mathbb{Q}(\zeta+\bar{\zeta})/\mathbb{Q}}(\beta)^2$... actually, let me think more carefully.

The discriminant of the form $\text{Tr}(\beta x \bar{y})$ is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N(\beta)^2$ where $N$ is the norm from $\mathbb{Q}(\zeta+\bar{\zeta})$ to $\mathbb{Q}$... actually I'm not sure about the exact formula. Let me think differently.

Actually, the form $\text{Tr}(\beta x \bar{y})$ on the 126-dimensional space has discriminant $= \text{disc}(\mathbb{Q}(\zeta)) \cdot N_{\mathbb{Q}(\zeta+\bar{\zeta})/\mathbb{Q}}(\beta)^2$. Wait, I think the discriminant is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N(\beta)^{126/63}$... I'm getting confused with the formulas.

Let me think about it more carefully. The trace form $\text{Tr}_{\mathbb{Q}(\zeta)/\mathbb{Q}}(x \bar{x})$ has a certain discriminant $D$. If we modify it to $\text{Tr}(\beta x \bar{x})$ where $\beta$ is in the real subfield $K^+ = \mathbb{Q}(\zeta + \bar{\zeta})$ (degree 63), then the discriminant changes by $N_{K^+/\mathbb{Q}}(\beta)^2$ (since $\beta$ acts on the 126-dim space, and the norm of $\beta$ as an element of $K^+$ raised to the appropriate power...).

Actually, I think the discriminant of $\text{Tr}(\beta x \bar{y})$ is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N_{K^+/\mathbb{Q}}(\beta)^2$. Since $\text{disc}(\mathbb{Q}(\zeta)) = -127^{125}$, the discriminant of the modified form is $-127^{125} \cdot N(\beta)^2$.

For this to be a perfect square (necessary for equivalence to identity), we need $-127^{125} \cdot N(\beta)^2$ to be a perfect square. But $-127^{125}$ is negative, so $-127^{125} \cdot N(\beta)^2$ is negative, and a negative number can't be a perfect square. 

Wait, but the discriminant of a positive definite form is positive! Let me recheck.

The discriminant of $\mathbb{Q}(\zeta)$ for $p = 127$: $\text{disc}(\mathbb{Q}(\zeta_p)) = (-1)^{(p-1)/2} p^{p-2}$. For $p = 127$, $(p-1)/2 = 63$, so $(-1)^{63} = -1$, giving $-127^{125}$.

But the trace form $\text{Tr}(x \bar{x})$ is positive definite (since $\mathbb{Q}(\zeta)$ is a CM field, $\text{Tr}(x\bar{x}) = \sum_\sigma \sigma(x)\overline{\sigma(x)} = \sum |\sigma(x)|^2 > 0$ for $x \neq 0$). A positive definite form has positive discriminant. So the discriminant of the trace form should be positive.

I think the issue is that the discriminant of the trace form $\text{Tr}(x\bar{y})$ is not the same as the discriminant of the number field. The discriminant of the number field $\mathbb{Q}(\zeta)$ is the discriminant of the trace form $\text{Tr}(xy)$ (without conjugation), which can be negative. The trace form $\text{Tr}(x\bar{y})$ is a different form.

Let me recalculate. The discriminant of $\text{Tr}(x\bar{y})$ with respect to the basis $1, \zeta, \zeta^2, \ldots, \zeta^{125}$: the $(i,j)$ entry is $\text{Tr}(\zeta^i \bar{\zeta}^j) = \text{Tr}(\zeta^{i-j})$. 

$\text{Tr}(\zeta^k) = \sum_{t=0}^{126} \zeta^{kt}$. For $k \equiv 0 \pmod{127}$, this is 126. For $k \not\equiv 0 \pmod{127}$, this is $\sum_{t=0}^{126} \zeta^{kt} = 0$ (sum of all 127th roots of unity, which is 0) minus... wait, $\sum_{t=0}^{126} (\zeta^k)^t = 0$ if $\zeta^k \neq 1$, i.e., if $k \not\equiv 0 \pmod{127}$. And $= 127$ if $k \equiv 0 \pmod{127}$.

But $\text{Tr}_{\mathbb{Q}(\zeta)/\mathbb{Q}}(\zeta^k) = \sum_{\sigma} \sigma(\zeta^k)$ where $\sigma$ ranges over all 126 embeddings. The embeddings are $\sigma_a: \zeta \mapsto \zeta^a$ for $a = 1, 2, \ldots, 126$. So $\text{Tr}(\zeta^k) = \sum_{a=1}^{126} \zeta^{ak}$.

For $k \equiv 0 \pmod{127}$: $\text{Tr}(\zeta^0) = \text{Tr}(1) = 126$.
For $k \not\equiv 0 \pmod{127}$: $\text{Tr}(\zeta^k) = \sum_{a=1}^{126} \zeta^{ak} = \sum_{a=0}^{126} \zeta^{ak} - 1 = 0 - 1 = -1$.

So the matrix of the trace form $\text{Tr}(\zeta^i \bar{\zeta}^j) = \text{Tr}(\zeta^{i-j})$ is a circulant-like matrix where the $(i,j)$ entry is $126$ if $i \equiv j \pmod{127}$ and $-1$ otherwise. This is $127 I - J$ where $J$ is the all-ones matrix (in the basis $\zeta^0, \ldots, \zeta^{125}$, but note we're using indices $0$ to $125$, which is 126 elements).

Wait, actually, the entries are $\text{Tr}(\zeta^{i-j})$ for $i, j \in \{0, 1, \ldots, 125\}$. When $i = j$, $\text{Tr}(1) = 126$. When $i \neq j$, $i - j \not\equiv 0 \pmod{127}$ (since $|i-j| \leq 125 < 127$), so $\text{Tr}(\zeta^{i-j}) = -1$.

So the matrix is $127 I_{126} - J_{126}$ where $J_{126}$ is the $126 \times 126$ all-ones matrix. The eigenvalues of $J_{126}$ are $126$ (once) and $0$ (125 times). So the eigenvalues of $127 I - J$ are $127 - 126 = 1$ (once) and $127$ (125 times). All positive, confirming positive definiteness.

The determinant is $1 \cdot 127^{125} = 127^{125}$.

So the discriminant of the trace form $\text{Tr}(x\bar{y})$ is $127^{125}$, which is positive (as expected for a positive definite form). Good.

Now, for the form $\text{Tr}(\beta x \bar{y})$ with $\beta \in K^+ = \mathbb{Q}(\zeta + \bar{\zeta})$ totally positive, the discriminant is $127^{125} \cdot N_{K^+/\mathbb{Q}}(\beta)^2$.

For this form to be equivalent to the identity over $\mathbb{Q}$, we need (among other things) the discriminant to be a perfect square. So we need $127^{125} \cdot N(\beta)^2 = \square$. Since $127^{125} = 127 \cdot (127^{62})^2$, we need $127 \cdot N(\beta)^2 = \square$, i.e., $127$ must be a perfect square times $N(\beta)^{-2}$... wait, $127^{125} \cdot N(\beta)^2 = 127 \cdot 127^{124} \cdot N(\beta)^2 = 127 \cdot (127^{62} \cdot N(\beta))^2$. For this to be a perfect square, we need $127$ to be a perfect square, which it's not.

So the discriminant is $127 \cdot (\text{something})^2$, which is never a perfect square. This means NO invariant positive definite form on $\mathbb{Q}(\zeta)$ is equivalent to the identity over $\mathbb{Q}$!

This means we CANNOT find a $126 \times 126$ orthogonal rational matrix with characteristic polynomial $\Phi_{127}$.

Wait, let me double-check this. The discriminant of the form $\text{Tr}(\beta x \bar{y})$ is $127^{125} \cdot N(\beta)^2$. For equivalence to the identity, we need this to be a perfect square. $127^{125} \cdot N(\beta)^2 = 127 \cdot (127^{62})^2 \cdot N(\beta)^2 = 127 \cdot (127^{62} N(\beta))^2$. This is a perfect square iff $127$ is a perfect square, which it's not. So indeed, no invariant form is equivalent to the identity.

Therefore, $n = 126$ is impossible!

So we need $n > 126$. What about $n = 127$? With $n = 127$, we can have the characteristic polynomial be $(x-1) \Phi_{127}(x) = x^{127} - 1$. The eigenvalue 1 corresponds to a 1-dimensional invariant subspace.

With the extra dimension (eigenvalue 1), we have more freedom. The invariant forms on the 1-dimensional eigenspace (for eigenvalue 1) can be any positive rational number. So the discriminant of the full form is $127^{125} \cdot N(\beta)^2 \cdot c$ where $c > 0$ is the form on the eigenvalue-1 space. We need $127^{125} \cdot N(\beta)^2 \cdot c = \square$, i.e., $127 \cdot (127^{62} N(\beta))^2 \cdot c = \square$, i.e., $127 c = \square$. So we need $c = 127 \cdot d^2$ for some rational $d$. Then the discriminant is $(127^{62} N(\beta) \cdot 127 d)^2 = (127^{63} N(\beta) d)^2$, a perfect square. 

But we also need the Hasse invariant to match. This requires more careful analysis.

Hmm, this is getting quite involved. Let me think about whether the answer is 127 or something else.

Actually, wait. I need to also check the Hasse-Minkowski invariants more carefully. Let me think about this from a higher level.

The question is: what is the minimal $n$ such that there exists an orthogonal rational $n \times n$ matrix of order 127?

The characteristic polynomial of such a matrix must be $(x-1)^a \Phi_{127}(x)^b$ where $a + 126b = n$ and $b \geq 1$. The minimal $n$ with $b = 1$ is $n = 126$ (with $a = 0$) or $n = 127$ (with $a = 1$).

We showed $n = 126$ doesn't work (discriminant obstruction). Let me check $n = 127$.

For $n = 127$, the matrix $Q$ has eigenvalues: one eigenvalue 1, and the 126 primitive 127th roots of unity. The rational canonical form is $\text{diag}(1, C)$ where $C$ is the companion matrix of $\Phi_{127}$.

An invariant positive definite form on the 127-dimensional space is $\text{Tr}(\beta x \bar{y})$ on the $\Phi_{127}$-part (126-dimensional) plus $c$ on the eigenvalue-1 part (1-dimensional). The discriminant is $127^{125} \cdot N(\beta)^2 \cdot c$.

For equivalence to identity: discriminant must be a perfect square. $127^{125} \cdot N(\beta)^2 \cdot c = 127 \cdot (127^{62} N(\beta))^2 \cdot c$. Need $127 c = \square$, so $c = 127 d^2$ for some $d \in \mathbb{Q}^*$.

Now we also need the Hasse invariant to be 1 (same as identity). The Hasse invariant of a direct sum is the product of Hasse invariants times some cross terms. This is getting complicated.

Let me try a different approach. Instead of trying to prove existence via quadratic form theory, let me try to construct an explicit orthogonal rational matrix of order 127.

Actually, let me think about this problem from a completely different angle. Maybe the answer is not 126 or 127 but something else entirely, and I'm missing something.

Let me reconsider. The problem asks for the smallest $n \geq 2$ such that there exists a normal $n \times n$ integer matrix $M$ whose sequence has period 7 and is not constant.

I've established:
1. If $M$ is normal, $M_1 = (M^T)^{-1} M$ is orthogonal (rational).
2. The sequence from $M_1$ is $M_1, M_1^2, M_1^4, \ldots, M_1^{2^{i-1}}, \ldots$
3. Period 7 means $M_1^{2^7} = M_1$ and $M_1^{2^k} \neq M_1$ for $k < 7$, i.e., $M_1^{127} = I$ and $M_1^{2^k - 1} \neq I$ for $k = 1, \ldots, 6$.
4. Since 127 is prime and $\text{ord}_{127}(2) = 7$, $M_1$ having order 127 gives period exactly 7.
5. The minimal $n$ is the minimal dimension of an orthogonal rational matrix of order 127.

And I've shown $n \geq 126$ (characteristic polynomial must include $\Phi_{127}$) and $n = 126$ is impossible (discriminant obstruction).

For $n = 127$, I need to verify that an orthogonal rational $127 \times 127$ matrix of order 127 exists.

Let me think about this more carefully. Consider the regular representation of the cyclic group $C_{127}$ acting on $\mathbb{Q}^{127}$. The group ring $\mathbb{Q}[C_{127}] \cong \mathbb{Q}[x]/(x^{127}-1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$ (by CRT, since $x^{127} - 1 = (x-1)\Phi_{127}(x)$ and $\Phi_{127}$ is irreducible).

The regular representation gives a $127 \times 127$ rational matrix (the permutation matrix of the cyclic shift) of order 127. But this permutation matrix is already orthogonal! It's a permutation matrix, hence signed permutation with all positive signs, hence orthogonal.

Wait, the cyclic shift permutation matrix $P$ of size 127 has order 127 and is orthogonal (it's a permutation matrix). Its characteristic polynomial is $x^{127} - 1 = (x-1)\Phi_{127}(x)$.

So $Q = P$ (the 127-cycle permutation matrix) is an orthogonal rational (even integer) matrix of order 127! And it's $127 \times 127$.

So $n = 127$ works for the orthogonal rational matrix part. Now I need to check that we can find a normal integer matrix $M$ with $M_1 = P$.

Using the Hilbert 90 approach: we need $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$, and then $M = f(P)$ where $f$ is the polynomial representing $\alpha$ in $\mathbb{Q}(\zeta)$, scaled to be integer.

But wait, $P$ is the companion matrix of $x^{127} - 1$, not of $\Phi_{127}$. The centralizer of $P$ is $\mathbb{Q}[P] \cong \mathbb{Q}[x]/(x^{127}-1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$. So $M = f(P)$ for $f \in \mathbb{Q}[x]/(x^{127}-1)$.

The condition $M^T = M P^T = M P^{-1} = M P^{126}$ (since $P$ is orthogonal, $P^T = P^{-1} = P^{126}$).

In terms of $\mathbb{Q}[x]/(x^{127}-1)$: $M = f(x)$, $M^T$ corresponds to $f(x^{-1}) = f(x^{126})$ (since $P^T = P^{126}$). The condition $M^T = M P^{126}$ becomes $f(x^{126}) = f(x) \cdot x^{126}$ in $\mathbb{Q}[x]/(x^{127}-1)$.

Under the CRT isomorphism $\mathbb{Q}[x]/(x^{127}-1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$, $x \mapsto (1, \zeta)$. So $f$ maps to $(f(1), f(\zeta)) = (a, \alpha)$ where $a = f(1) \in \mathbb{Q}$ and $\alpha = f(\zeta) \in \mathbb{Q}(\zeta)$.

The condition $f(x^{126}) = f(x) \cdot x^{126}$:
- At $x = 1$: $f(1) = f(1) \cdot 1$, so $a = a$. Always true.
- At $x = \zeta$: $f(\zeta^{126}) = f(\zeta) \cdot \zeta^{126}$, i.e., $f(\bar{\zeta}) = \alpha \cdot \bar{\zeta}$, i.e., $\bar{\alpha} = \alpha \bar{\zeta}$, i.e., $\alpha / \bar{\alpha} = \zeta$.

So we need $\alpha / \bar{\alpha} = \zeta$ (same as before) and $a$ can be anything. By Hilbert 90, such $\alpha$ exists. Then $M = f(P)$ is rational, and we scale to make it integer.

But we also need $M$ to be normal. We showed normality is automatic given $M^T = M Q^T$ and $M$ commutes with $Q$. Let me double check: $M = f(P)$ commutes with $P$ (since it's a polynomial in $P$). And $M^T = M P^T$ is our condition. So $M$ is normal. ✓

And we need $M$ to be invertible. $M = f(P)$ is invertible iff $f(1) \neq 0$ and $f(\zeta) \neq 0$, i.e., $a \neq 0$ and $\alpha \neq 0$. We can choose $a = 1$ and $\alpha \neq 0$ (from Hilbert 90, $\alpha \neq 0$). ✓

So $n = 127$ works! But wait, I need to check that $n = 126$ really doesn't work, and also check if there's some clever way to get a smaller $n$.

Actually, wait. I think I need to reconsider. The issue with $n = 126$ was that no invariant positive definite form on the 126-dimensional irreducible representation is equivalent to the identity. But maybe I can use a non-irreducible representation?

For $n < 126$, the characteristic polynomial of $Q$ must be $(x-1)^a \Phi_{127}(x)^b$ with $a + 126b = n$ and $b \geq 1$. Since $b \geq 1$ and $126b \leq n < 126$, we need $b = 1$ and $a < 0$, which is impossible. So for $n < 126$, it's impossible to have order 127 (the characteristic polynomial can't include $\Phi_{127}$).

Wait, that's not right. The characteristic polynomial doesn't have to be a product of cyclotomic polynomials in that way. Let me reconsider.

$Q$ is a rational matrix with $Q^{127} = I$. The minimal polynomial of $Q$ divides $x^{127} - 1 = (x-1)\Phi_{127}(x)$. The characteristic polynomial is a product of powers of the irreducible factors of the minimal polynomial. Since $\Phi_{127}$ is irreducible over $\mathbb{Q}$, the characteristic polynomial is $(x-1)^a \Phi_{127}(x)^b$ where $a + 126b = n$.

For $Q$ to have order 127, we need $b \geq 1$ (otherwise $Q = I$). So $n = a + 126b \geq 126$.

For $n = 126$: $a = 0, b = 1$. Characteristic polynomial is $\Phi_{127}(x)$.
For $n = 127$: $a = 1, b = 1$. Characteristic polynomial is $(x-1)\Phi_{127}(x) = x^{127} - 1$.

I showed $n = 126$ fails (discriminant obstruction). And $n = 127$ works (permutation matrix).

But wait, I should double-check the $n = 126$ case more carefully. The issue is whether there exists a $126 \times 126$ orthogonal rational matrix with characteristic polynomial $\Phi_{127}$.

Such a matrix $Q$ would satisfy $Q^T Q = I$ and have char poly $\Phi_{127}$. The existence is equivalent to: the companion matrix $C$ of $\Phi_{127}$ is conjugate to an orthogonal matrix over $\mathbb{Q}$, i.e., there exists $S$ positive definite rational with $C^T S C = S$ and $S$ equivalent to $I$ over $\mathbb{Q}$.

I showed that any such $S$ has discriminant $127 \cdot (\text{square})$, which is not a perfect square, so $S$ is not equivalent to $I$.

But actually, I should be more careful. The space of symmetric forms $S$ with $C^T S C = S$ is not just the trace form. Let me reconsider.

The centralizer of $C$ (companion matrix of $\Phi_{127}$, irreducible) is $\mathbb{Q}[C] \cong \mathbb{Q}(\zeta)$. A symmetric bilinear form $S$ with $C^T S C = S$ corresponds to an element $\beta \in \mathbb{Q}(\zeta)$ with $\bar{\beta} = \beta$ (i.e., $\beta \in K^+ = \mathbb{Q}(\zeta + \bar{\zeta})$, the real subfield of degree 63).

The form is $S_\beta(x, y) = \text{Tr}(\beta x \bar{y})$ (up to identification). The discriminant of $S_\beta$ is $\text{disc}(\text{Tr}(\beta x \bar{y}))$.

Let me compute this. The matrix of $S_\beta$ in the basis $1, \zeta, \ldots, \zeta^{125}$ has $(i,j)$ entry $\text{Tr}(\beta \zeta^i \bar{\zeta}^j) = \text{Tr}(\beta \zeta^{i-j})$.

This is a "twisted" trace form. The discriminant of $\text{Tr}(\beta x \bar{y})$ is $N_{\mathbb{Q}(\zeta)/\mathbb{Q}}(\beta) \cdot \text{disc}(\text{Tr}(x\bar{y}))$... actually, I think the discriminant of $\text{Tr}(\beta x \bar{y})$ is $N_{K^+/\mathbb{Q}}(\beta)^2 \cdot \text{disc}(\text{Tr}(x\bar{y}))$.

Wait, let me think about this more carefully. $\beta \in K^+$, and $\text{Tr}(\beta x \bar{y})$ where the trace is from $\mathbb{Q}(\zeta)$ (degree 126) to $\mathbb{Q}$.

The discriminant of $\text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y})$ where $L = \mathbb{Q}(\zeta)$: this is a standard computation. If $\beta \in K^+ = L^+$ (the maximal real subfield), then $\text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y}) = \text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y})$.

Actually, since $L/K^+$ is a CM extension (degree 2), and $\beta \in K^+$, we have $\text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y}) = \text{Tr}_{K^+/\mathbb{Q}}(\beta \text{Tr}_{L/K^+}(x\bar{y}))$.

Hmm, this is getting complicated. Let me just use the fact that the discriminant of $\text{Tr}(\beta x \bar{y})$ is $N_{K^+/\mathbb{Q}}(\beta)^2 \cdot D_0$ where $D_0 = 127^{125}$ is the discriminant of the untwisted trace form $\text{Tr}(x\bar{y})$.

Actually, I realize I should verify this. The map $\beta \mapsto S_\beta$ is a linear map from $K^+$ (63-dimensional) to symmetric $126 \times 126$ matrices. The determinant of $S_\beta$ as a function of $\beta$ is a homogeneous polynomial of degree 126 in the coordinates of $\beta$ (since $S_\beta$ is 126-dimensional). But $\beta$ has 63 coordinates, so $\det(S_\beta)$ is a degree 126 form in 63 variables... this doesn't factor as $N(\beta)^2$ in an obvious way.

Actually, I think the correct statement is: $\det(S_\beta) = N_{L/\mathbb{Q}}(\beta) \cdot D_0$ where $N_{L/\mathbb{Q}}$ is the norm from $L = \mathbb{Q}(\zeta)$ to $\mathbb{Q}$. Since $\beta \in K^+$, $N_{L/\mathbb{Q}}(\beta) = N_{K^+/\mathbb{Q}}(\beta)^2$ (because $L/K^+$ has degree 2 and $\beta \in K^+$, so $N_{L/\mathbb{Q}}(\beta) = N_{K^+/\mathbb{Q}}(N_{L/K^+}(\beta)) = N_{K^+/\mathbb{Q}}(\beta^2) = N_{K^+/\mathbb{Q}}(\beta)^2$).

So $\det(S_\beta) = N_{K^+/\mathbb{Q}}(\beta)^2 \cdot 127^{125}$.

For $S_\beta$ to be equivalent to $I_{126}$ over $\mathbb{Q}$, we need $\det(S_\beta) = \square$. So $N_{K^+/\mathbb{Q}}(\beta)^2 \cdot 127^{125} = \square$, i.e., $127^{125} = \square / N(\beta)^2 = \square$. But $127^{125} = 127 \cdot 127^{124} = 127 \cdot (127^{62})^2$, which is not a perfect square. Contradiction.

So indeed, $n = 126$ is impossible.

Now, for $n = 127$: the permutation matrix $P$ of the 127-cycle is a $127 \times 127$ orthogonal integer matrix of order 127. We need to find a normal integer matrix $M$ with $M_1 = (M^T)^{-1} M = P$.

As I argued, this requires $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$ (Hilbert 90 gives existence), and then $M = f(P)$ where $f(1) = a \neq 0$ and $f(\zeta) = \alpha$, scaled to be integer.

Let me construct this more explicitly. By Hilbert 90, $\alpha = \zeta - 1$ works? Let me check: $\alpha / \bar{\alpha} = (\zeta - 1)/(\bar{\zeta} - 1) = (\zeta - 1)/(\zeta^{-1} - 1) = (\zeta - 1) \cdot \zeta / (1 - \zeta) = -\zeta$. So $\alpha / \bar{\alpha} = -\zeta$, not $\zeta$. Close but not quite.

Let me try $\alpha = \zeta + 1$: $\bar{\alpha} = \zeta^{-1} + 1 = (1 + \zeta)/\zeta$. $\alpha / \bar{\alpha} = (\zeta + 1) / ((1+\zeta)/\zeta) = \zeta$. Yes! So $\alpha = 1 + \zeta$ works.

So $f(\zeta) = 1 + \zeta$ and $f(1) = 1 + 1 = 2$. So $f(x) = 1 + x$ and $M = I + P$.

Let me verify: $M = I + P$ where $P$ is the 127-cycle permutation matrix.

$M^T = I + P^T = I + P^{-1} = I + P^{126}$.

$M P^T = (I + P)(I + P^{-1}) = (I + P)(P^{-1} + I) \cdot P^{-1} \cdot P$... let me just compute directly.

$M^T = I + P^{126}$. $M P^{126} = (I + P) P^{126} = P^{126} + P^{127} = P^{126} + I = I + P^{126} = M^T$. ✓

So $M^T = M P^{126} = M P^T$. ✓

Is $M$ normal? $M^T M = (I + P^{126})(I + P) = I + P + P^{126} + I = 2I + P + P^{126}$. $M M^T = (I + P)(I + P^{126}) = I + P^{126} + P + I = 2I + P + P^{126}$. So $M^T M = M M^T$. ✓ Normal.

Is $M$ invertible? $M = I + P$. The eigenvalues of $P$ are the 127th roots of unity. The eigenvalues of $M = I + P$ are $1 + \omega$ for each 127th root of unity $\omega$. For $\omega = -1$... but $-1$ is not a 127th root of unity (127 is odd). So all eigenvalues $1 + \omega \neq 0$, and $M$ is invertible. ✓

Is $M$ an integer matrix? $M = I + P$ where $P$ is a permutation matrix. Yes, $M$ is an integer matrix. ✓

Now let's verify $M_1 = (M^T)^{-1} M = P$.

$(M^T)^{-1} = (I + P^{126})^{-1}$. $M = I + P$.

$(M^T)^{-1} M = (I + P^{126})^{-1}(I + P)$.

Note that $I + P = P(P^{-1} + I) = P(I + P^{126})$ (since $P^{-1} = P^{126}$). So $(I + P^{126})^{-1}(I + P) = (I + P^{126})^{-1} P (I + P^{126}) = P$ (since $P$ commutes with $I + P^{126}$). 

Wait: $(I + P^{126})^{-1} \cdot P \cdot (I + P^{126})$. Since $P$ commutes with $P^{126}$ (both are powers of $P$), $P$ commutes with $I + P^{126}$, so $(I + P^{126})^{-1} P (I + P^{126}) = P (I+P^{126})^{-1}(I+P^{126}) = P$. ✓

So $M_1 = P$, which has order 127. The sequence is $M, P, P^2, P^4, P^8, P^{16}, P^{32}, P^{64}, P^{128} = P, \ldots$ with period 7 (since $P^{128} = P^{127} \cdot P = P$).

Wait, let me recheck the period. $M_1 = P$, $M_2 = P^2$, $M_3 = P^4$, $M_4 = P^8$, $M_5 = P^{16}$, $M_6 = P^{32}$, $M_7 = P^{64}$, $M_8 = P^{128} = P = M_1$. So $M_{i+7} = M_i$ for $i \geq 1$. ✓

Is the period exactly 7? We need $M_{1+k} \neq M_1$ for $k = 1, 2, 3, 4, 5, 6$, i.e., $P^{2^k} \neq P$ for $k = 1, \ldots, 6$, i.e., $P^{2^k - 1} \neq I$ for $k = 1, \ldots, 6$, i.e., $127 \nmid 2^k - 1$ for $k = 1, \ldots, 6$.

$2^1 - 1 = 1$, $2^2 - 1 = 3$, $2^3 - 1 = 7$, $2^4 - 1 = 15$, $2^5 - 1 = 31$, $2^6 - 1 = 63$. None of these are divisible by 127. ✓ (And $2^7 - 1 = 127$, which is divisible by 127.) ✓

So the period is exactly 7. And the sequence is not constant (since $M_1 = P \neq I = M_2^{\infty}$... well, $M_1 = P \neq P^2 = M_2$, so it's not constant). ✓

So $n = 127$ works. And $n = 126$ doesn't work. And $n < 126$ is impossible. So the answer is $\boxed{127}$.

Wait, but I should double-check that $n < 126$ is truly impossible. For $n < 126$, the characteristic polynomial of $Q$ (orthogonal rational of order 127) must be $(x-1)^a \Phi_{127}(x)^b$ with $a + 126b = n$, $b \geq 1$. Since $126b \geq 126 > n$ for $b \geq 1$ and $n < 126$, this is impossible. So indeed $n \geq 126$. ✓

And $n = 126$ is impossible because no invariant positive definite form on the irreducible 126-dimensional representation is equivalent to the identity (discriminant obstruction). ✓

And $n = 127$ works (explicit construction with $M = I + P$). ✓

Hmm wait, but I need to be more careful about the $n = 126$ case. I showed that the discriminant of any invariant form is $127^{125} \cdot N(\beta)^2 = 127 \cdot (\text{square})$, which is not a perfect square. But for a form to be equivalent to the identity, we need not just the discriminant to be a perfect square, but also the Hasse invariant to be 1. Since the discriminant is already not a perfect square, the form is not equivalent to the identity. This is sufficient.

But actually, I need to make sure I haven't made an error. Let me re-examine.

The claim is: there is no $126 \times 126$ orthogonal rational matrix $Q$ with $Q^{127} = I$ and $Q \neq I$.

Proof: Such $Q$ would have characteristic polynomial $\Phi_{127}(x)$ (since $n = 126 = \deg \Phi_{127}$ and $b = 1, a = 0$). The rational canonical form of $Q$ is the companion matrix $C$ of $\Phi_{127}$. So $Q = S C S^{-1}$ for some rational $S$.

$Q$ orthogonal means $Q^T Q = I$, i.e., $S^{-T} C^T S^T S C S^{-1} = I$, i.e., $C^T (S^T S) C = S^T S$. Let $T = S^T S$, which is positive definite rational. So $C^T T C = T$.

The space of symmetric $T$ with $C^T T C = T$ is parametrized by $\beta \in K^+$ (the real subfield), with $\det(T) = 127^{125} \cdot N_{K^+/\mathbb{Q}}(\beta)^2$.

For $T = S^T S$ with $S$ rational, $T$ must be equivalent to the identity over $\mathbb{Q}$ (since $S^T S$ and $I$ are equivalent: $S^T I S = S^T S = T$, so $T$ is equivalent to $I$). A necessary condition is $\det(T) = \square$ (perfect square in $\mathbb{Q}$). But $\det(T) = 127 \cdot (127^{62} N(\beta))^2$, which is $127$ times a square, not a square. Contradiction.

So $n = 126$ is impossible. ✓

Actually, I want to make sure about the formula $\det(T_\beta) = 127^{125} \cdot N_{K^+/\mathbb{Q}}(\beta)^2$. Let me verify this for $\beta = 1$ (the untwisted trace form).

For $\beta = 1$: $T_1$ has $(i,j)$ entry $\text{Tr}(\zeta^{i-j})$ for $i, j = 0, \ldots, 125$. As computed, this is $127 I - J$ (where $J$ is all-ones). $\det(127I - J) = 127^{125} \cdot (127 - 126) = 127^{125} \cdot 1 = 127^{125}$. And $N_{K^+/\mathbb{Q}}(1) = 1$. So $\det(T_1) = 127^{125} \cdot 1 = 127^{125}$. ✓

For general $\beta$: The determinant of $T_\beta$ as a function of $\beta$ is a polynomial. Since $T_\beta$ is the matrix of the form $\text{Tr}(\beta x \bar{y})$, and this form is the "twist" of the trace form by $\beta$, the determinant transforms as $\det(T_\beta) = N_{L/\mathbb{Q}}(\beta) \cdot \det(T_1)$ where $N_{L/\mathbb{Q}}$ is the norm from $L = \mathbb{Q}(\zeta)$ to $\mathbb{Q}$.

Since $\beta \in K^+ \subset L$, $N_{L/\mathbb{Q}}(\beta) = N_{K^+/\mathbb{Q}}(\beta)^{[L:K^+]} = N_{K^+/\mathbb{Q}}(\beta)^2$.

So $\det(T_\beta) = N_{K^+/\mathbb{Q}}(\beta)^2 \cdot 127^{125}$. ✓

Great, so the formula is confirmed. And $127^{125} = 127 \cdot (127^{62})^2$, so $\det(T_\beta) = 127 \cdot (127^{62} N(\beta))^2$, which is never a perfect square (since 127 is not a perfect square).

Therefore, $n = 126$ is impossible, and the answer is $n = 127$.

Let me also verify that the sequence is "not constant." The sequence is $M_0 = M = I + P$, $M_1 = P$, $M_2 = P^2$, etc. Since $M_0 \neq M_1$ (as $I + P \neq P$), the sequence is not constant. Also, $M_1 = P \neq P^2 = M_2$, etc. ✓

So the answer is $\boxed{127}$.

Let me also sanity-check by making sure I haven't made an error in the key step that normality of $M$ implies $M_1$ is orthogonal.

$M$ normal: $M^T M = M M^T$.
$M_1 = (M^T)^{-1} M$.
$M_1^T = M^T (M^{-1})^T = M^T (M^T)^{-1}$... wait. $M_1 = (M^T)^{-1} M$. $M_1^T = M^T ((M^T)^{-1})^T = M^T (M^T^T)^{-1} = M^T M^{-1}$.

$M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M$.

Since $M$ is normal, $M^T M = M M^T$, which gives $M^{-1} (M^T)^{-1} = (M^T)^{-1} M^{-1}$ (inverse of $M M^T = M^T M$ gives $(M^T)^{-1} M^{-1} = M^{-1} (M^T)^{-1}$). Also, $M^T M^{-1} = M^{-1} M^T$ (from $M^T M = M M^T$, left-multiply by $M^{-1}$: $M^{-1} M^T M = M^T$, right-multiply by $M^{-1}$: $M^{-1} M^T = M^T M^{-1}$).

So $M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M = M^T (M^T)^{-1} M^{-1} M = I \cdot I = I$. ✓

And from $M_1$ orthogonal, $M_{i+1} = (M_i^T)^{-1} M_i = M_i^{-1} M_i = M_i$... wait, no. If $M_i$ is orthogonal, $M_i^T = M_i^{-1}$, so $(M_i^T)^{-1} = M_i$, and $M_{i+1} = M_i \cdot M_i = M_i^2$. ✓

So from $M_1$ onward, $M_{i+1} = M_i^2$, giving $M_i = M_1^{2^{i-1}}$. ✓

Everything checks out. The answer is $n = 127$.

Let me also think about whether I need to worry about the case where $M$ is normal but $M_1$ might not have order exactly 127. In our construction, $M_1 = P$ (the 127-cycle permutation), which has order 127. The period of the sequence $P, P^2, P^4, \ldots$ is the multiplicative order of 2 modulo 127, which is 7 (since $2^7 = 128 \equiv 1 \pmod{127}$ and 7 is prime, so the order is 7). ✓

Actually, I should verify that 7 is the exact order of 2 mod 127, not just that $2^7 \equiv 1$. Since 127 is prime, the order of 2 divides $126 = 2 \times 3^2 \times 7$. The divisors of 126 are: 1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126. We need to check that $2^d \not\equiv 1 \pmod{127}$ for $d | 126$, $d < 7$, i.e., $d \in \{1, 2, 3\}$ (since we need $d < 7$ and $d | 126$; but actually the order could be any divisor of 126, not just less than 7).

Wait, the period is the order of 2 mod 127. Let me compute this properly.

$2^1 = 2 \not\equiv 1$
$2^2 = 4 \not\equiv 1$
$2^3 = 8 \not\equiv 1$
$2^6 = 64 \not\equiv 1$
$2^7 = 128 \equiv 1 \pmod{127}$

So the order of 2 mod 127 divides 7. Since 7 is prime and $2^1 \neq 1$, the order is 7. ✓

(The order must divide 126 by Fermat's little theorem, and also divide 7 since $2^7 \equiv 1$. So the order divides $\gcd(126, 7) = 7$. Since $2^1 \not\equiv 1$, the order is 7.)

Great, so the period is exactly 7.

Now let me write up the complete proof.

Actually, let me reconsider one thing. I want to make sure the construction $M = I + P$ gives a valid $M_0$ that is part of the period-7 sequence. The sequence is:
- $M_0 = M = I + P$
- $M_1 = P$
- $M_2 = P^2$
- $M_3 = P^4$
- $M_4 = P^8$
- $M_5 = P^{16}$
- $M_6 = P^{32}$
- $M_7 = P^{64}$
- $M_8 = P^{128} = P = M_1$

So $M_{i+7} = M_i$ for $i \geq 1$. But what about $M_0$? We need $M_7 = M_0$, i.e., $P^{64} = I + P$. But $P^{64} \neq I + P$ in general (they're different matrices). 

Hmm, so the period starting from $M_0$ might not be 7. Let me reconsider.

The problem says "the sequence $\mathcal{S}_M$ has period $P = 7$, i.e., $M_{i+7} = M_i$." This should hold for all $i \geq 0$, including $i = 0$.

So we need $M_7 = M_0$, i.e., $M_1^{2^6} = M_0$, i.e., $P^{64} = I + P$. But this is not true!

So my construction doesn't quite work as stated. The issue is that $M_0 = M$ is not part of the periodic cycle; only $M_1, M_2, \ldots$ are periodic.

Let me reconsider. We need $M_{i+7} = M_i$ for ALL $i \geq 0$. In particular, $M_7 = M_0$.

$M_7 = M_1^{2^6} = P^{64}$. $M_0 = I + P$. So we need $P^{64} = I + P$, which is false.

So I need to choose $M$ more carefully. The condition is:
- $M_1 = (M^T)^{-1} M = Q$ (orthogonal, order 127)
- $M_0 = M$ must equal $M_7 = Q^{2^6} = Q^{64}$.

So $M = Q^{64}$. But also $M_1 = (M^T)^{-1} M = Q$. So $(Q^{64})^T)^{-1} Q^{64} = Q$.

$(Q^{64})^T = (Q^T)^{64} = Q^{-64} = Q^{127-64} = Q^{63}$ (since $Q^{127} = I$).

$(Q^{64})^T)^{-1} = (Q^{63})^{-1} = Q^{-63} = Q^{64}$.

So $M_1 = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

So if we set $M = Q^{64}$, then $M_1 = Q$, and $M_7 = Q^{2^6} = Q^{64} = M$. ✓

But we also need $M = Q^{64}$ to be a normal integer matrix.

$Q = P$ (the 127-cycle permutation matrix). $M = P^{64}$. This is a permutation matrix (hence integer and orthogonal). Is it normal? Permutation matrices are orthogonal, hence normal. ✓

But wait, if $M = P^{64}$ is orthogonal, then $M_1 = (M^T)^{-1} M = M^{-1} M = I$. That gives $M_1 = I$, and the sequence is constant from $M_1$ onward. That's not what we want!

The issue is: if $M$ is orthogonal, then $M_1 = (M^T)^{-1} M = M^{-1} M = I$, and the sequence becomes constant. So $M$ cannot be orthogonal.

So $M = Q^{64}$ being orthogonal is a problem. We need $M$ to be normal but NOT orthogonal.

Let me reconsider. We need:
1. $M$ is normal, integer, invertible.
2. $M_1 = (M^T)^{-1} M = Q$ (orthogonal, order 127).
3. $M_7 = M_0$, i.e., $Q^{64} = M$.

From (2) and (3): $M = Q^{64}$ and $(M^T)^{-1} M = Q$.

$(Q^{64})^T)^{-1} Q^{64} = Q$.

If $Q$ is orthogonal, $(Q^{64})^T = Q^{-64}$, so $((Q^{64})^T)^{-1} = Q^{64}$, and $M_1 = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

But $M = Q^{64}$ is orthogonal (since $Q$ is), so $M$ is orthogonal, and then $M_1 = I$... 

Wait, no. If $M$ is orthogonal, $M^T = M^{-1}$, so $(M^T)^{-1} = M$, and $M_1 = M \cdot M = M^2$. But we also said $M_1 = Q$. So $M^2 = Q$, i.e., $(Q^{64})^2 = Q^{128} = Q$. ✓ Consistent.

But then $M_2 = M_1^2 = Q^2$, $M_3 = Q^4$, ..., $M_7 = Q^{64} = M$. ✓

And the sequence is $M, Q, Q^2, Q^4, Q^8, Q^{16}, Q^{32}, Q^{64} = M, Q, \ldots$ with period 7. ✓

But wait, is the sequence constant? $M = Q^{64} \neq Q = M_1$ (since $Q$ has order 127 and $64 \not\equiv 1 \pmod{127}$). So the sequence is not constant. ✓

But the problem is: $M = Q^{64} = P^{64}$ is a permutation matrix, hence orthogonal. And if $M$ is orthogonal, $M_1 = M^2 = P^{128} = P$. So $M_1 = P = Q$. ✓

But then $M_2 = (M_1^T)^{-1} M_1$. $M_1 = P$ is orthogonal, so $M_2 = P^2$. ✓

So actually, the issue I was worried about doesn't arise. Let me re-examine.

If $M = P^{64}$ (orthogonal), then:
- $M_0 = P^{64}$
- $M_1 = (M_0^T)^{-1} M_0 = (P^{64})^{-1} \cdot P^{64}$... wait, $M_0^T = (P^{64})^T = (P^T)^{64} = P^{-64} = P^{63}$. $(M_0^T)^{-1} = (P^{63})^{-1} = P^{-63} = P^{64}$. $M_1 = P^{64} \cdot P^{64} = P^{128} = P$. ✓

- $M_2 = (M_1^T)^{-1} M_1 = (P^T)^{-1} P = P \cdot P = P^2$. ✓ (Since $P$ is orthogonal, $(P^T)^{-1} = P$.)

- $M_i = P^{2^{i-1}}$ for $i \geq 1$. ✓

- $M_7 = P^{64} = M_0$. ✓

- $M_8 = P^{128} = P = M_1$. ✓

So the sequence is $P^{64}, P, P^2, P^4, P^8, P^{16}, P^{32}, P^{64}, P, \ldots$ with period 7. ✓

And it's not constant since $P^{64} \neq P$. ✓

But wait, $M = P^{64}$ is orthogonal, and the problem requires $M$ to be normal. Orthogonal matrices are normal. ✓

But hold on—is the sequence really not constant? $M_0 = P^{64}$, $M_1 = P$. These are different (since $P$ has order 127 and $64 \not\equiv 1 \pmod{127}$). But also, is $M_0 = M_1$? No, $P^{64} \neq P$ since $P^{63} \neq I$. ✓ Not constant.

But actually, I realize there might be a subtlety. When $M$ is orthogonal, $M_1 = M^2$, and the sequence becomes $M, M^2, M^4, M^8, \ldots$ from the start. So $M_i = M^{2^i}$ for all $i \geq 0$. The period is the smallest $p$ with $M^{2^p} = M$, i.e., $M^{2^p - 1} = I$. With $M = P^{64}$, $M^{2^p - 1} = P^{64(2^p - 1)}$. We need $127 | 64(2^p - 1)$, i.e., $127 | 2^p - 1$ (since $\gcd(64, 127) = 1$). The smallest such $p$ is 7. ✓

So the period is 7. ✓

But wait, I need to double-check: is the sequence $M, M^2, M^4, \ldots$ when $M$ is orthogonal? 

$M_0 = M$. $M_1 = (M^T)^{-1} M = M^{-1} M = I$... 

NO! If $M$ is orthogonal, $M^T = M^{-1}$, so $(M^T)^{-1} = (M^{-1})^{-1} = M$. So $M_1 = M \cdot M = M^2$. ✓ (Not $I$.)

OK so I had it right. $M_1 = M^2$ when $M$ is orthogonal. Good.

So with $M = P^{64}$:
- $M_0 = P^{64}$
- $M_1 = (P^{64})^2 = P^{128} = P$
- $M_2 = P^2$
- $M_3 = P^4$
- ...
- $M_7 = P^{64} = M_0$ ✓

Period 7, not constant. $M = P^{64}$ is a $127 \times 127$ orthogonal (hence normal) integer matrix. ✓

So $n = 127$ works. But now I realize I need to re-examine whether we could potentially do better. The key constraint is that $M_1 = (M^T)^{-1} M$ must be orthogonal of order 127, and $M_7 = M_0$.

Actually, the condition $M_7 = M_0$ is automatically satisfied if $M_1$ has the right order. Let me re-derive.

If $M$ is normal, $M_1$ is orthogonal. Then $M_i = M_1^{2^{i-1}}$ for $i \geq 1$. The period of the sequence from $M_1$ is the order of 2 modulo $\text{ord}(M_1)$. 

For the full sequence (including $M_0$) to have period 7, we need $M_{i+7} = M_i$ for all $i \geq 0$. For $i \geq 1$, this is $M_1^{2^{i+6}} = M_1^{2^{i-1}}$, i.e., $M_1^{2^{i-1}(2^7 - 1)} = I$, which is satisfied if $M_1^{127} = I$ (since $2^7 - 1 = 127$). For $i = 0$: $M_7 = M_0$, i.e., $M_1^{64} = M_0$.

So we need $M_0 = M_1^{64}$. But $M_0 = M$ and $M_1 = (M^T)^{-1} M$. So $M = ((M^T)^{-1} M)^{64}$.

This is an additional constraint on $M$! It's not just that $M_1$ has order 127; we need $M = M_1^{64}$.

In our construction with $M = P^{64}$: $M_1 = P$ and $M_1^{64} = P^{64} = M$. ✓

But in the more general approach (where $M$ is not orthogonal), we need to ensure $M = M_1^{64}$.

Given $Q = M_1$ (orthogonal of order 127), we need $M = Q^{64}$ and $(M^T)^{-1} M = Q$.

$M = Q^{64}$. $M^T = (Q^{64})^T = (Q^T)^{64} = Q^{-64}$ (since $Q$ orthogonal). $(M^T)^{-1} = Q^{64}$. $M_1 = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

So $M = Q^{64}$ always works (for any orthogonal $Q$ of order 127), and $M$ is automatically orthogonal (hence normal). And $M$ is integer iff $Q$ is integer.

So the question reduces to: what is the minimal $n$ such that there exists an orthogonal **integer** matrix $Q$ of order 127?

Orthogonal integer matrices are signed permutation matrices. A signed permutation matrix of order 127: the underlying permutation must have a cycle whose length (or twice the length) is divisible by 127. Since 127 is prime, we need a cycle of length 127 (with product of signs = 1, giving order 127) or a cycle of length 127 with product of signs = -1 (giving order 254, not 127).

Wait, let me think about this. A signed permutation on a cycle of length $k$: if the product of signs around the cycle is $+1$, the order is $k$. If $-1$, the order is $2k$.

For order 127 (prime), we need a cycle of length 127 with product of signs $+1$. This requires $n \geq 127$.

Could we have a shorter cycle? A cycle of length $k$ with product of signs $+1$ has order $k$. For $k | 127$, $k = 1$ or $k = 127$. $k = 1$ gives order 1 (not 127). So we need $k = 127$.

What about combining multiple cycles? The order of a signed permutation is the lcm of the orders of its cycles. For the lcm to be 127, each cycle's order must divide 127, and at least one must be 127. So we need at least one cycle of length 127 (with product of signs $+1$). This requires $n \geq 127$.

So the minimal $n$ for an orthogonal integer matrix of order 127 is $n = 127$.

But wait—do we need $Q$ to be an integer matrix? Let me re-examine.

$M = Q^{64}$ must be an integer matrix. $Q = M_1 = (M^T)^{-1} M$ is rational (since $M$ is integer). $Q$ is orthogonal and rational. $M = Q^{64}$ must be integer.

So $Q$ doesn't have to be integer; it just needs to be rational orthogonal, and $Q^{64}$ must be integer.

This changes things! $Q$ can be a rational orthogonal matrix (not necessarily signed permutation), and we just need $Q^{64}$ to be an integer matrix.

So the question becomes: what is the minimal $n$ such that there exists a rational orthogonal $n \times n$ matrix $Q$ of order 127 with $Q^{64}$ being an integer matrix?

Hmm, but $Q^{64}$ being an integer matrix and $Q$ being rational orthogonal... Let me think about what $Q^{64}$ looks like.

If $Q$ has order 127, then $Q^{64} = Q^{-63} = (Q^{-1})^{63}$. Also, $Q^{64} = Q^{64}$.

Actually, since $Q^{127} = I$, $Q^{64} = Q^{64 \mod 127} = Q^{64}$. And $Q^{64}$ is also rational (since $Q$ is rational). For $Q^{64}$ to be integer, we need the entries of $Q^{64}$ to be integers.

Now, $M = Q^{64}$ is an integer matrix. Is $M$ normal? $M = Q^{64}$ where $Q$ is orthogonal. $M^T = (Q^T)^{64} = Q^{-64}$. $M^T M = Q^{-64} Q^{64} = I$. So $M$ is orthogonal, hence normal. ✓

And $M_1 = (M^T)^{-1} M = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

So the question is: minimal $n$ such that there exists a rational orthogonal $Q$ of order 127 with $Q^{64}$ integer.

Now, $Q^{64}$ is a rational matrix (power of rational matrix). For it to be integer, we need its entries to be integers.

The eigenvalues of $Q$ are 127th roots of unity. The eigenvalues of $Q^{64}$ are $\omega^{64}$ for each eigenvalue $\omega$ of $Q$. Since $\gcd(64, 127) = 1$, the map $\omega \mapsto \omega^{64}$ is a bijection on the 127th roots of unity. So $Q^{64}$ has the same order as $Q$ (order 127), and the same characteristic polynomial (up to relabeling of roots).

Actually, the characteristic polynomial of $Q^{64}$: if $Q$ has eigenvalues $\omega_1, \ldots, \omega_n$ (127th roots of unity), then $Q^{64}$ has eigenvalues $\omega_1^{64}, \ldots, \omega_n^{64}$. Since $\gcd(64, 127) = 1$, $\omega \mapsto \omega^{64}$ permutes the primitive 127th roots of unity. So the characteristic polynomial of $Q^{64}$ is the same as that of $Q$ (since the Galois group acts transitively on primitive roots, and the char poly has rational coefficients).

Wait, that's not quite right. The characteristic polynomial of $Q$ is $(x-1)^a \Phi_{127}(x)^b$. The eigenvalues of $Q^{64}$ are $1^{64} = 1$ (with multiplicity $a$) and $\omega^{64}$ for primitive 127th roots $\omega$ (with multiplicity $b$ each). Since $\omega \mapsto \omega^{64}$ permutes the primitive 127th roots, the characteristic polynomial of $Q^{64}$ is also $(x-1)^a \Phi_{127}(x)^b$. So $Q^{64}$ has the same characteristic polynomial as $Q$.

Now, $Q^{64}$ is a rational matrix (power of rational $Q$) with the same characteristic polynomial as $Q$. And $Q^{64}$ must be an integer matrix.

The question is: can $Q^{64}$ be an integer matrix even if $Q$ is not?

Let me think about this for $n = 126$. We need a rational orthogonal $126 \times 126$ matrix $Q$ of order 127 such that $Q^{64}$ is an integer matrix.

$Q$ has characteristic polynomial $\Phi_{127}(x)$. $Q^{64}$ also has characteristic polynomial $\Phi_{127}(x)$. $Q^{64}$ is a rational matrix with this characteristic polynomial, so its rational canonical form is the companion matrix $C$ of $\Phi_{127}$. For $Q^{64}$ to be an integer matrix, we need... well, $Q^{64}$ is similar to $C$ over $\mathbb{Q}$, and $Q^{64}$ is an integer matrix with characteristic polynomial $\Phi_{127}$.

The companion matrix $C$ of $\Phi_{127}$ is an integer matrix with characteristic polynomial $\Phi_{127}$. So integer matrices with this characteristic polynomial exist. The question is whether $Q^{64}$ can be one of them.

$Q^{64}$ is determined by $Q$: $Q^{64} = Q^{64}$. If $Q$ is rational orthogonal with char poly $\Phi_{127}$, then $Q^{64}$ is rational with char poly $\Phi_{127}$, and $Q^{64        — AI历史解题过程（thinking）
#   polymath_00169         — 题目ID

# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search.
- All information you need is in this AGENTS.md file.
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
  <problem_id>polymath_00169</problem_id>
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

For an invertible $n\times n$ matrix $M$ with integer entries we define a sequence $\mathcal{S}_M=\{M_i\}_{i=0}^{\infty}$ by the recurrence $M_0=M$ ,$M_{i+1}=(M_i^T)^{-1}M_i$ for $i\geq 0$.

Find the smallest integer $n\geq 2 $  for wich there exists a normal $n\times n$ matrix with integer entries such that its sequence $\mathcal{S}_M$ is not constant and has period $P=7$ i.e $M_{i+7}=M_i$.
($M^T$ means the transpose of a matrix $M$ . A square matrix is called normal if $M^T M=M M^T$ holds).

[i]Proposed by Martin Niepel (Comenius University, Bratislava)..[/i]

## Standard Solution

1. **Define the sequence and initial conditions:**
   Given an invertible \( n \times n \) matrix \( M \) with integer entries, we define the sequence \( \mathcal{S}_M = \{M_i\}_{i=0}^{\infty} \) by the recurrence relation:
   \[
   M_0 = M, \quad M_{i+1} = (M_i^T)^{-1} M_i \quad \text{for} \ i \geq 0.
   \]

2. **Calculate the first few terms of the sequence:**
   \[
   M_1 = (M_0^T)^{-1} M_0 = (M^T)^{-1} M.
   \]
   \[
   M_2 = (M_1^T)^{-1} M_1 = ([(M^T)^{-1} M]^T)^{-1} (M^T)^{-1} M = (M^T)^{-1} (M^T)^{-1} M = (M^T)^{-2} M^2.
   \]

3. **Inductive step:**
   Assume \( M_i = (M^T)^{-2^{i-1}} M^{2^{i-1}} \) holds for some \( i \geq 1 \). Then,
   \[
   M_{i+1} = (M_i^T)^{-1} M_i = ([(M^T)^{-2^{i-1}} M^{2^{i-1}}]^T)^{-1} (M^T)^{-2^{i-1}} M^{2^{i-1}}.
   \]
   Since \( (AB)^T = B^T A^T \),
   \[
   M_i^T = (M^{2^{i-1}})^T ((M^T)^{-2^{i-1}})^T = (M^T)^{2^{i-1}} (M^{-2^{i-1}}).
   \]
   Therefore,
   \[
   (M_i^T)^{-1} = (M^{-2^{i-1}})^{-1} ((M^T)^{2^{i-1}})^{-1} = M^{2^{i-1}} (M^T)^{-2^{i-1}}.
   \]
   Thus,
   \[
   M_{i+1} = M^{2^{i-1}} (M^T)^{-2^{i-1}} (M^T)^{-2^{i-1}} M^{2^{i-1}} = (M^T)^{-2^i} M^{2^i}.
   \]
   By induction, \( M_i = (M^T)^{-2^{i-1}} M^{2^{i-1}} \) holds for all \( i \geq 1 \).

4. **Periodicity condition:**
   We need \( M_7 = M \), which implies:
   \[
   (M^T)^{-64} M^{64} = M.
   \]
   This simplifies to:
   \[
   M^{63} = (M^T)^{64}.
   \]
   Taking the transpose of both sides, we get:
   \[
   (M^{63})^T = ((M^T)^{64})^T \implies (M^T)^{63} = M^{64}.
   \]
   Combining both equations, we have:
   \[
   M^{63} = (M^T)^{64} \quad \text{and} \quad M^{64} = (M^T)^{63}.
   \]
   These imply that \( M = (M^T)^{-1} \), meaning \( M \) is an orthogonal matrix.

5. **Orthogonal matrix with integer entries:**
   Since \( M \) is orthogonal and has integer entries, it must be a permutation matrix. For \( M_7 = M \), we need:
   \[
   M^{128} = M \implies M^{127} = I.
   \]
   Since \( 127 \) is a prime number, the permutation described by \( M \) must have a cycle of length \( 127 \). This is only possible if \( n \geq 127 \).

6. **Conclusion:**
   The smallest integer \( n \geq 2 \) for which there exists a normal \( n \times n \) matrix with integer entries such that its sequence \( \mathcal{S}_M \) is not constant and has period \( P = 7 \) is \( n = 127 \).

The final answer is \( \boxed{127} \).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a sequence defined by $M_0 = M$, $M_{i+1} = (M_i^T)^{-1} M_i$ for an invertible $n \times n$ integer matrix $M$.

We need to find the smallest $n \geq 2$ for which there exists a **normal** $n \times n$ integer matrix whose sequence $\mathcal{S}_M$ is not constant and has period $P = 7$.

First, let me understand the recurrence. Let $M_{i+1} = (M_i^T)^{-1} M_i$.

Let me think about what happens for a normal matrix. A matrix $M$ is normal if $M^T M = M M^T$.

Let me think about the structure. Let me write $M_i$ in some factored form.

Let me think about this differently. Consider the polar-like decomposition. Actually, let me think about what the recurrence does.

$M_{i+1} = (M_i^T)^{-1} M_i$

Let me try to understand this in terms of some transformation. Let's think about $M_i = U_i R_i$ or something.

Actually, let me think about it as follows. Consider the "left polar decomposition" type thing. If $M_i$ is invertible, we can write $M_i = (M_i^T)^{-1} \cdot (M_i^T M_i)$. So $M_i = (M_i^T)^{-1} \cdot (M_i^T M_i)$, meaning $M_{i+1} = (M_i^T M_i)$... no wait.

$M_{i+1} = (M_i^T)^{-1} M_i$. 

Hmm, let me think about the relationship between consecutive terms.

Let me compute $M_{i+1}^T$:
$M_{i+1}^T = M_i^T ((M_i^T)^{-1})^T = M_i^T (M_i^{-1})^T$... wait.

$M_{i+1} = (M_i^T)^{-1} M_i$, so $M_{i+1}^T = M_i^T ((M_i^T)^{-1})^T = M_i^T (M_i^{-1})^T$... 

Hmm, $((M_i^T)^{-1})^T = ((M_i^T)^T)^{-1} = M_i^{-1}$.

So $M_{i+1}^T = M_i^T \cdot M_i^{-1}$.

And $M_{i+1}^{-1} = M_i^{-1} \cdot M_i^T$.

So $(M_{i+1}^T)^{-1} = (M_i^T M_i^{-1})^{-1} = M_i (M_i^T)^{-1}$.

Then $M_{i+2} = (M_{i+1}^T)^{-1} M_{i+1} = M_i (M_i^T)^{-1} \cdot (M_i^T)^{-1} M_i$.

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the substitution $M_i = (M_0^T)^{-i} \cdot$ something... Actually let me try to find a pattern.

Let me define $A_i = M_i^T M_i$ (the "Gram matrix"). 

$A_{i+1} = M_{i+1}^T M_{i+1} = M_i^T M_i^{-1} (M_i^T)^{-1} M_i$... 

Hmm wait, $M_{i+1}^T = M_i^T M_i^{-1}$, so 
$A_{i+1} = M_i^T M_i^{-1} (M_i^T)^{-1} M_i$.

This doesn't simplify nicely in general.

Let me try another substitution. Let $B_i = (M_i^T)^{-1} M_i = M_{i+1}$. So the map is $M \mapsto (M^T)^{-1} M$.

Let me think about what this map does to certain structured matrices.

**Key idea**: Let's think about matrices of the form $M = \lambda Q$ where $Q$ is orthogonal ($Q^T Q = I$). Then $M^T = \lambda Q^T$, $(M^T)^{-1} = \lambda^{-1} Q$, and $M_{i+1} = \lambda^{-1} Q \cdot \lambda Q = Q^2$... no wait, $M_{i+1} = (M^T)^{-1} M = \lambda^{-1} Q \cdot \lambda Q = Q^2$? No: $(M^T)^{-1} = (\lambda Q^T)^{-1} = \lambda^{-1} (Q^T)^{-1} = \lambda^{-1} Q$. So $M_{i+1} = \lambda^{-1} Q \cdot \lambda Q = Q \cdot Q = Q^2$.

Hmm, but then $M_1 = Q^2$ which is orthogonal, and $M_2 = (Q^2)^T)^{-1} Q^2 = (Q^T)^2)^{-1} Q^2 = Q^{-2} Q^2 = I$. So the sequence becomes constant at $I$ after 2 steps. Not useful for period 7.

Let me think more carefully. The map $f(M) = (M^T)^{-1} M$.

Let me try $M = $ upper triangular or something.

Actually, let me think about this problem from the perspective of the structure that's preserved.

Let me consider the substitution $M_i = P_i S_i$ where... hmm.

Let me try yet another approach. Consider the QR-like decomposition. Actually, let me think about what happens with the substitution $N_i = M_i^{-T} M_i$ (which is $M_{i+1}$). 

Let me think about the eigenvalue structure. Actually, let me try to think about this in terms of a simpler recurrence.

Let me try: suppose $M$ is such that $M^T = D M D^{-1}$ for some diagonal $D$ (i.e., $M$ is " centrosymmetric" or has some symmetry). Then $(M^T)^{-1} = D M^{-1} D^{-1}$, and $M_{i+1} = D M_i^{-1} D^{-1} M_i$.

Hmm, let me try a very specific structure. Let me consider block matrices or companion matrices.

Actually, let me think about this more carefully using the normality condition.

If $M$ is normal ($M^T M = M M^T$), what can we say?

For a normal matrix, $M$ and $M^T$ commute. So $M^T M = M M^T$.

Then $M_1 = (M^T)^{-1} M = (M^T)^{-1} M$. Since $M$ and $M^T$ commute, $(M^T)^{-1}$ and $M$ commute, so $M_1 = M (M^T)^{-1}$ as well.

Is $M_1$ normal? $M_1^T M_1 = (M^T M^{-1})((M^T)^{-1} M) = M^T M^{-1} (M^T)^{-1} M$. Since $M$ and $M^T$ commute, $M^{-1}$ and $(M^T)^{-1}$ commute, and $M^T$ commutes with $M^{-1}$... Let me be careful.

$M^T M = M M^T$ implies $M^{-1} (M^T)^{-1} = (M^T)^{-1} M^{-1}$ (taking inverse of both sides: $(MM^T)^{-1} = (M^T M)^{-1}$, so $(M^T)^{-1} M^{-1} = M^{-1} (M^T)^{-1}$). Also $M^T M^{-1} = M^{-1} M^T$ (from $M^T M = M M^T$, multiply by $M^{-1}$ on right: $M^T = M M^T M^{-1}$, and on left: $M^{-1} M^T M = M^T$, so $M^{-1} M^T = M^T M^{-1}$).

So $M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M = M^T (M^T)^{-1} M^{-1} M = I$.

Wait, that means $M_1^T M_1 = I$?! So $M_1$ is orthogonal?!

Let me double-check. $M_1^T = M^T M^{-1}$ (computed earlier). $M_1 = (M^T)^{-1} M$.

$M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M$.

Using $M^{-1} (M^T)^{-1} = (M^T)^{-1} M^{-1}$:
$= M^T (M^T)^{-1} M^{-1} M = I \cdot I = I$.

Yes! So if $M$ is normal, then $M_1$ is orthogonal: $M_1^T M_1 = I$.

And $M_1 M_1^T = (M^T)^{-1} M \cdot M^T M^{-1} = (M^T)^{-1} M M^T M^{-1} = (M^T)^{-1} M^T M M^{-1} = I$.

So $M_1$ is orthogonal (and hence also normal).

Now if $M_1$ is orthogonal, $M_1^T = M_1^{-1}$, so $(M_1^T)^{-1} = M_1$, and $M_2 = M_1 \cdot M_1 = M_1^2$.

More generally, if $M_i$ is orthogonal, $M_{i+1} = M_i^2$.

So from $M_1$ onward, $M_{i+1} = M_i^2$, meaning $M_i = M_1^{2^{i-1}}$ for $i \geq 1$.

So the sequence from $M_1$ is: $M_1, M_1^2, M_1^4, M_1^8, \ldots, M_1^{2^{i-1}}, \ldots$

For this to have period 7 (starting from $M_1$), we need $M_1^{2^7} = M_1^{2^0} = M_1$, i.e., $M_1^{128} = M_1$, i.e., $M_1^{127} = I$.

And we need the period to be exactly 7, meaning $M_1^{2^k} \neq M_1$ for $k = 1, 2, 3, 4, 5, 6$, i.e., $M_1^{2^k - 1} \neq I$ for $k = 1, \ldots, 6$, i.e., $M_1^1, M_1^3, M_1^7, M_1^{15}, M_1^{31}, M_1^{63} \neq I$.

Since 127 is prime, the order of $M_1$ must divide 127. The order is 127 (since $M_1 \neq I$ as the sequence is not constant, and 127 is prime so the only divisors are 1 and 127).

Wait, but we need to be careful. The period of the sequence $M_1, M_1^2, M_1^4, \ldots$ is the smallest $p$ such that $M_1^{2^p} = M_1$, i.e., $M_1^{2^p - 1} = I$. The order of $M_1$ divides $2^p - 1$. For the period to be exactly 7, we need the order of $M_1$ to divide $2^7 - 1 = 127$ but not divide $2^k - 1$ for any $k < 7$.

Since 127 is prime, the order of $M_1$ is either 1 or 127. If it's 127, then $127 | 2^k - 1$ iff $2^k \equiv 1 \pmod{127}$, and the order of 2 mod 127 is... 127 is prime, so the order of 2 divides 126 = 2 × 63 = 2 × 7 × 9 = 2 × 7 × 9. Let me compute: $126 = 2 \cdot 3^2 \cdot 7$.

The order of 2 mod 127: We need $2^k \equiv 1 \pmod{127}$. The order divides 126. Let me check: is the order 7? $2^7 = 128 \equiv 1 \pmod{127}$. Yes! So the order of 2 mod 127 is 7.

So if $M_1$ has order 127, then $M_1^{2^k} = M_1$ iff $2^k \equiv 1 \pmod{127}$ iff $7 | k$. So the period is exactly 7. 

So we need:
1. $M$ is a normal integer matrix, invertible.
2. $M_1 = (M^T)^{-1} M$ is an orthogonal integer matrix of order 127.
3. The sequence is not constant, which is ensured since $M_1$ has order 127 ≠ 1.

Wait, but $M_1$ needs to be an orthogonal **integer** matrix. An orthogonal integer matrix has $M_1^T M_1 = I$ with integer entries, so $M_1 \in O_n(\mathbb{Z})$, which means $M_1$ is a signed permutation matrix.

A signed permutation matrix of order 127... but signed permutation matrices have order that divides... well, a permutation matrix has order = lcm of cycle lengths. A signed permutation matrix can have order that's a bit more complex but still, the order of a signed permutation in $O_n(\mathbb{Z})$ is limited.

Actually, the order of a signed permutation matrix: each signed permutation is a permutation $\sigma$ combined with signs. The order divides... For a single cycle of length $k$ with signs, the order can be $k$ or $2k$ depending on the product of signs around the cycle.

For order 127 (which is prime), we need a cycle of length 127 (with appropriate signs). A signed permutation matrix that is a single 127-cycle with all positive signs has order 127. This requires $n \geq 127$.

But wait, can we do better? Can we have $M_1$ be orthogonal with order 127 but not a signed permutation? No—orthogonal integer matrices are exactly signed permutation matrices.

Hmm, so this approach gives $n \geq 127$. But maybe we can do better by not requiring $M_1$ to be an integer matrix?

Wait, let me reconsider. $M$ is an integer matrix, and $M_1 = (M^T)^{-1} M$. Is $M_1$ necessarily an integer matrix? Not necessarily! $M_1$ is a rational matrix in general.

But $M_1$ is orthogonal (we showed $M_1^T M_1 = I$). And $M_1$ is rational. An orthogonal rational matrix is not necessarily a signed permutation matrix!

For example, $\frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$ is orthogonal and rational but not a signed permutation.

So $M_1$ is an orthogonal **rational** matrix. The question is: what's the minimal $n$ for which there exists an orthogonal rational $n \times n$ matrix of order 127?

Hmm, but actually we need more: we need $M_1 = (M^T)^{-1} M$ for some normal integer matrix $M$. Let me think about what constraints this places.

Actually, let me reconsider. We need:
- $M$ is an $n \times n$ integer matrix, invertible, normal.
- $M_1 = (M^T)^{-1} M$ is orthogonal (automatically from normality).
- $M_1$ has order 127 (so the period is 7).
- $M_1$ is rational (since $M$ is integer).

Actually, $M_1 = (M^T)^{-1} M$. Since $M$ is integer and invertible, $(M^T)^{-1} = (M^{-1})^T$ is rational, so $M_1$ is rational. Good.

Now, conversely, given an orthogonal rational matrix $Q$ of order 127, can we find a normal integer matrix $M$ such that $(M^T)^{-1} M = Q$?

From $(M^T)^{-1} M = Q$, we get $M = M^T Q$, i.e., $M = M^T Q$. Taking transpose: $M^T = Q^T M$. So $M = Q^T M Q$... no. $M = M^T Q$ and $M^T = Q^T M$, so $M = Q^T M Q$... let me redo: $M^T = (M^T Q)^T = Q^T M$. And $M = M^T Q = Q^T M Q$. So $M = Q^T M Q$, i.e., $Q M = M Q$ (multiply by $Q$ on left: $QM = Q Q^T M Q = M Q$). So $M$ commutes with $Q$.

Also, $M = M^T Q$ means $M^T = M Q^{-1} = M Q^T$ (since $Q$ is orthogonal, $Q^{-1} = Q^T$).

So the conditions on $M$ are:
1. $M$ commutes with $Q$.
2. $M^T = M Q^T$ (equivalently $M = M^T Q$).
3. $M$ is normal (but if $M^T = M Q^T$ and $M$ commutes with $Q$, then $M^T M = M Q^T M = M M Q^T = M M^T$... let me check: $M^T M = M Q^T M$. Since $M$ commutes with $Q$, $M$ commutes with $Q^T$, so $M Q^T M = Q^T M^2$. And $M M^T = M \cdot M Q^T = M^2 Q^T = Q^T M^2$. So yes, $M^T M = M M^T$, normal is automatic.)
4. $M$ is an integer matrix.

So we need: an integer matrix $M$ that commutes with $Q$ and satisfies $M^T = M Q^T$.

From $M^T = M Q^T$: $M = (M^T)^T = (M Q^T)^T = Q M^T = Q \cdot M Q^T = Q M Q^T$. Since $M$ commutes with $Q$, $Q M Q^T = M Q Q^T = M$. Consistent.

So the key constraint is: $M^T = M Q^T$ and $M$ commutes with $Q$, with $M$ integer.

From $M^T = M Q^T$, we get $M = M^T Q$, so $M^T = M Q^T = M^T Q Q^T = M^T$. Consistent again.

Let me think about this differently. We have $M^T = M Q^T$. This means $M^T Q = M$, i.e., $M$ is determined by... hmm.

Let me think about it as: $M = M^T Q$, so if we know $M$ on one "side", the other is determined. 

Actually, let me think about the structure more carefully. Since $Q$ has order 127 (prime), the minimal polynomial of $Q$ divides $x^{127} - 1$. Over $\mathbb{Q}$, $x^{127} - 1 = (x-1)\Phi_{127}(x)$ where $\Phi_{127}(x) = x^{126} + x^{125} + \cdots + x + 1$ is the 127th cyclotomic polynomial, which is irreducible over $\mathbb{Q}$ (since 127 is prime).

So the rational canonical form of $Q$ consists of blocks corresponding to $x - 1$ (eigenvalue 1) and $\Phi_{127}(x)$ (the primitive 127th roots of unity).

For $Q$ to have order exactly 127, it must have at least one block corresponding to $\Phi_{127}(x)$. The block for $\Phi_{127}(x)$ is the companion matrix of $\Phi_{127}(x)$, which is $126 \times 126$.

So the minimal dimension for $Q$ to have order 127 is 126 (just the companion matrix of $\Phi_{127}$), or 127 if we include the eigenvalue 1 block (but we don't need it).

Wait, but we also need $Q$ to be orthogonal. The companion matrix of $\Phi_{127}$ is not orthogonal in general. We need $Q$ to be both orthogonal and rational, with order 127.

Hmm, so the question becomes: what is the minimal $n$ such that there exists an orthogonal rational $n \times n$ matrix of order 127?

An orthogonal rational matrix $Q$ of order 127: $Q^{127} = I$, $Q^T Q = I$, $Q$ rational.

Since $Q$ is orthogonal and rational, $Q^T = Q^{-1}$. And $Q^{127} = I$.

The eigenvalues of $Q$ are 127th roots of unity. Since $Q$ is real (rational), eigenvalues come in conjugate pairs. The primitive 127th roots of unity come in 63 conjugate pairs. So to have all primitive 127th roots, we'd need dimension at least 126.

But we don't need all of them. We just need $Q$ to have order 127, which means at least one primitive 127th root of unity as an eigenvalue. But since $Q$ is real, if $\zeta$ is an eigenvalue, so is $\bar{\zeta} = \zeta^{-1}$. And since $Q$ is rational, the characteristic polynomial has rational coefficients, so if $\zeta$ is a root, all conjugates (all primitive 127th roots) are roots. So the characteristic polynomial must be divisible by $\Phi_{127}(x)$, which has degree 126.

Therefore, $n \geq 126$.

Now, can we achieve $n = 126$? We need a $126 \times 126$ orthogonal rational matrix whose characteristic polynomial is $\Phi_{127}(x)$.

The companion matrix $C$ of $\Phi_{127}(x)$ has order 127 and characteristic polynomial $\Phi_{127}(x)$, but it's not orthogonal. However, we might be able to find an orthogonal rational matrix with the same characteristic polynomial.

Actually, let me think about this. The rational canonical form is unique. If $Q$ is a $126 \times 126$ rational matrix with characteristic polynomial $\Phi_{127}(x)$ (which is irreducible), then the rational canonical form of $Q$ is the companion matrix of $\Phi_{127}(x)$. So $Q = P C P^{-1}$ for some rational $P$.

For $Q$ to be orthogonal, we need $Q^T Q = I$, i.e., $P^{-T} C^T P^T P C P^{-1} = I$, i.e., $C^T (P^T P) C = P^T P$. So we need a positive definite rational matrix $S = P^T P$ such that $C^T S C = S$.

This is equivalent to finding a rational positive definite matrix $S$ that is "fixed" by the action $S \mapsto C^T S C$. 

Hmm, this is getting complicated. Let me think about whether such an $S$ exists.

Actually, there's a classical result: every finite-order rational matrix is conjugate (over $\mathbb{Q}$) to an orthogonal rational matrix. Is this true? I'm not sure.

Let me think differently. Consider the $\mathbb{Q}$-vector space $V = \mathbb{Q}^{126}$ with $Q$ acting on it. Since $\Phi_{127}$ is irreducible, $V$ is an irreducible $\mathbb{Q}[Q]$-module, isomorphic to $\mathbb{Q}(\zeta)$ where $\zeta$ is a primitive 127th root of unity.

An invariant positive definite bilinear form on $V$ corresponds to an element of $\mathbb{Q}(\zeta)$ that is fixed by the appropriate involution and is totally positive. 

The involution on $\mathbb{Q}(\zeta)$ induced by $Q \mapsto Q^T$ (which corresponds to $\zeta \mapsto \zeta^{-1} = \bar{\zeta}$) is complex conjugation. An invariant form corresponds to $\alpha \in \mathbb{Q}(\zeta)$ with $\bar{\alpha} = \alpha$ (i.e., $\alpha$ is in the maximal real subfield $\mathbb{Q}(\zeta + \bar{\zeta})$) and $\alpha$ is totally positive (positive under all embeddings).

Such elements exist (e.g., $\alpha = 1$ works if the form $S = I$ is invariant, but it's not in general). We need to find $\alpha$ in the real subfield that is totally positive.

Actually, the trace form $\text{tr}(x \bar{x})$ gives a positive definite invariant form. The trace form on $\mathbb{Q}(\zeta)/\mathbb{Q}$ is $\text{Tr}_{\mathbb{Q}(\zeta)/\mathbb{Q}}(x \bar{x})$, which is positive definite (since $\mathbb{Q}(\zeta)$ is a CM field). This gives a rational positive definite invariant bilinear form.

So yes, there exists a rational positive definite matrix $S$ with $C^T S C = S$, and then $Q = S^{1/2} C S^{-1/2}$... but $S^{1/2}$ might not be rational. 

Hmm, but we need $Q$ to be rational. Let me think again.

We have $C^T S C = S$ with $S$ rational positive definite. We want $Q = P C P^{-1}$ orthogonal with $P$ rational. This requires $P^T P = S$, i.e., $P$ is a rational "square root" of $S$ in the sense $P^T P = S$. But not every rational positive definite $S$ has a rational $P$ with $P^T P = S$ (this is the issue of representing $S$ as a sum of squares, essentially).

Hmm, this is getting complicated. Let me think about whether the answer might just be 126, or whether there are additional constraints from the requirement that $M$ is an integer matrix.

Actually, wait. Let me reconsider the problem. We need $M$ to be an integer matrix, and $M_1 = (M^T)^{-1} M$ to be orthogonal rational of order 127. But we also need $M$ to be normal.

We showed that if $M$ is normal, then $M_1$ is automatically orthogonal. And the conditions on $M$ given $Q = M_1$ are: $M$ commutes with $Q$, $M^T = M Q^T$, and $M$ is integer.

So the question is really: given an orthogonal rational matrix $Q$ of order 127, can we find an integer matrix $M$ commuting with $Q$ with $M^T = M Q^T$?

Let me think about the structure of matrices commuting with $Q$. If $Q$ has characteristic polynomial $\Phi_{127}(x)$ (irreducible), then the centralizer of $Q$ in $M_n(\mathbb{Q})$ is $\mathbb{Q}[Q] \cong \mathbb{Q}(\zeta)$. So $M = f(Q)$ for some $f \in \mathbb{Q}(\zeta)$.

The condition $M^T = M Q^T$ becomes: $f(Q)^T = f(Q) Q^T$. Since $Q$ is orthogonal, $Q^T = Q^{-1} = Q^{126}$. And $f(Q)^T = \bar{f}(Q)$ where $\bar{f}$ is the image under $\zeta \mapsto \zeta^{-1}$ (complex conjugation on $\mathbb{Q}(\zeta)$).

So the condition is $\bar{f}(Q) = f(Q) \cdot Q^{-1}$, i.e., $\bar{f}(\zeta) = f(\zeta) \cdot \zeta^{-1}$, i.e., $\bar{f}(\zeta) = f(\zeta) / \zeta$.

Let $f(\zeta) = \alpha \in \mathbb{Q}(\zeta)$. The condition is $\bar{\alpha} = \alpha / \zeta$, i.e., $\alpha = \bar{\alpha} \cdot \zeta$.

So $\alpha / \bar{\alpha} = \zeta$. This means $\alpha$ is an element of $\mathbb{Q}(\zeta)$ with $\alpha / \bar{\alpha} = \zeta$.

Such an $\alpha$ exists if and only if $\zeta$ is in the image of the norm map $N: \mathbb{Q}(\zeta)^* \to \mathbb{Q}(\zeta)^+$... actually, $\alpha / \bar{\alpha} = \zeta$ means $\alpha \bar{\alpha}^{-1} = \zeta$, so $N(\alpha) = \alpha \bar{\alpha}$ and $\alpha / \bar{\alpha} = \zeta$.

This is related to Hilbert's Theorem 90. In the extension $\mathbb{Q}(\zeta) / \mathbb{Q}(\zeta+\bar{\zeta})$ (which is a degree 2 extension with Galois group generated by complex conjugation), Hilbert's Theorem 90 says that $\zeta = \alpha / \bar{\alpha}$ for some $\alpha$ iff $N_{\mathbb{Q}(\zeta)/\mathbb{Q}(\zeta+\bar{\zeta})}(\zeta) = \zeta \bar{\zeta} = 1$. And indeed $\zeta \bar{\zeta} = |\zeta|^2 = 1$. So by Hilbert's Theorem 90, such an $\alpha$ exists in $\mathbb{Q}(\zeta)$.

So there exists $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$. Then $M = \alpha(Q)$ (i.e., $M = f(Q)$ where $f(\zeta) = \alpha$) satisfies $M^T = M Q^T$ and $M$ commutes with $Q$.

But we need $M$ to be an **integer** matrix. $M = f(Q)$ is a rational matrix (since $f$ has rational coefficients and $Q$ is rational). For $M$ to be integer, we need $f(Q)$ to have integer entries.

Since $Q$ is a rational matrix with characteristic polynomial $\Phi_{127}$, the entries of $f(Q)$ are rational. We can scale: if $\alpha$ works, then $c \alpha$ also works for any $c \in \mathbb{Q}^*$ (since $(c\alpha)/\overline{(c\alpha)} = \alpha/\bar{\alpha} = \zeta$). So we can scale $M$ by a rational constant to clear denominators, making $M$ integer.

But wait, scaling $M$ by $c$ changes $M_1 = (M^T)^{-1} M$. If $M \to cM$, then $M^T \to c M^T$, $(M^T)^{-1} \to c^{-1} (M^T)^{-1}$, and $M_1 \to c^{-1} (M^T)^{-1} \cdot c M = M_1$. So $M_1$ is unchanged! Great.

So the strategy is:
1. Find an orthogonal rational $Q$ of order 127, of size $n \times n$.
2. Find $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$ (exists by Hilbert 90).
3. Set $M = f(Q)$ where $f(\zeta) = \alpha$, then scale to make $M$ integer.

The minimal $n$ is determined by the minimal size of an orthogonal rational matrix of order 127.

As argued, $n \geq 126$ (since the characteristic polynomial must be divisible by $\Phi_{127}$ of degree 126, and eigenvalues come in conjugate pairs for real matrices, but actually the degree of $\Phi_{127}$ is already even: $\phi(127) = 126$, so a real matrix can have characteristic polynomial $\Phi_{127}$).

Wait, I need to be more careful. $\Phi_{127}(x) = x^{126} + x^{125} + \cdots + 1$ has degree 126. A real matrix can have this as its characteristic polynomial (the roots are the primitive 127th roots of unity, which come in 63 conjugate pairs, all non-real). So $n = 126$ is possible in terms of the characteristic polynomial.

Now, can we find an **orthogonal rational** $126 \times 126$ matrix with characteristic polynomial $\Phi_{127}$?

As I discussed, this requires finding a rational positive definite $S$ with $C^T S C = S$ (where $C$ is the companion matrix of $\Phi_{127}$), and then a rational $P$ with $P^T P = S$.

The existence of $S$ is guaranteed (trace form). The existence of rational $P$ with $P^T P = S$ is the question of whether $S$ is a sum of squares of rational matrices, which is always true for positive definite rational matrices (by the theory of quadratic forms over $\mathbb{Q}$—every positive definite rational quadratic form can be diagonalized, and each positive rational number is a sum of four squares, so we can write $S = P^T P$ with $P$ rational).

Wait, actually that's not quite right. $P^T P = S$ with $P$ rational and $S$ positive definite rational—this is asking whether the quadratic form represented by $S$ is equivalent over $\mathbb{Q}$ to the standard form. This is not always true! Two positive definite forms over $\mathbb{Q}$ are equivalent iff they have the same dimension, determinant (up to squares), Hasse invariant, and signature.

Hmm, but actually we don't need $P^T P = S$ exactly. We need $Q = P C P^{-1}$ to be orthogonal, which means $(PCP^{-1})^T (PCP^{-1}) = I$, i.e., $P^{-T} C^T P^T P C P^{-1} = I$, i.e., $C^T (P^T P) C = P^T P$. So $S = P^T P$ must satisfy $C^T S C = S$.

But we get to choose $S$ (any rational positive definite $S$ with $C^T S C = S$), and then we need $S = P^T P$ for some rational $P$.

The space of $S$ satisfying $C^T S C = S$ is a $\mathbb{Q}$-vector space. By the theory of the trace form, this space is 1-dimensional over the centralizer of $C$, which is $\mathbb{Q}[C] \cong \mathbb{Q}(\zeta)$. Actually, the space of invariant bilinear forms is isomorphic to the space of $\alpha \in \mathbb{Q}(\zeta)$ with $\bar{\alpha} = \alpha$ (symmetric forms) or $\bar{\alpha} = -\alpha$ (skew forms). The symmetric ones form the real subfield $\mathbb{Q}(\zeta + \bar{\zeta})$, which has dimension 63 over $\mathbb{Q}$.

So the space of symmetric invariant forms is 63-dimensional over $\mathbb{Q}$. We need to find one that is positive definite and is a sum of squares (i.e., $S = P^T P$ for rational $P$).

A positive definite form that is a sum of squares is the same as a form equivalent to the identity. By the Hasse-Minkowski theorem, a positive definite form over $\mathbb{Q}$ is equivalent to the identity iff it has the same invariants (dimension, discriminant, Hasse invariant) as the identity.

The identity form has discriminant 1 and Hasse invariant 1. So we need a symmetric invariant form with discriminant a perfect square and Hasse invariant 1.

Since the space of symmetric invariant forms is 63-dimensional, we have a lot of freedom. It seems very likely that such a form exists, but proving it rigorously requires more work.

Hmm, let me think about this differently. Maybe there's a more direct construction.

Actually, let me reconsider. Maybe I'm overcomplicating this. Let me think about whether we actually need $Q$ to be orthogonal, or whether the problem allows $M_1$ to be orthogonal over $\mathbb{R}$ but rational.

We showed that if $M$ is normal (integer), then $M_1 = (M^T)^{-1} M$ is orthogonal ($M_1^T M_1 = I$) and rational. So $M_1$ is an orthogonal rational matrix. The sequence from $M_1$ is $M_1, M_1^2, M_1^4, \ldots$ and we need period 7, so $M_1$ has order 127.

Conversely, given an orthogonal rational $Q$ of order 127, we can construct $M$ (integer, normal) with $M_1 = Q$, by Hilbert 90 and scaling.

So the minimal $n$ is the minimal dimension of an orthogonal rational matrix of order 127.

Now, I claimed $n \geq 126$. Let me also check: can we have $n = 126$?

For $n = 126$: we need a $126 \times 126$ orthogonal rational matrix $Q$ with $Q^{127} = I$ and $Q \neq I$. The characteristic polynomial must be $\Phi_{127}(x)$ (the only option for a 126-dimensional matrix with order dividing 127 and not equal to 1).

Let me think about a concrete construction. Consider the field $\mathbb{Q}(\zeta)$ where $\zeta = e^{2\pi i/127}$. This is a degree 126 extension of $\mathbb{Q}$. As a $\mathbb{Q}$-vector space, $\mathbb{Q}(\zeta) \cong \mathbb{Q}^{126}$.

Multiplication by $\zeta$ is a $\mathbb{Q}$-linear map on $\mathbb{Q}(\zeta)$, and its matrix (in some basis) is a $126 \times 126$ rational matrix of order 127. But it's not orthogonal in general.

To make it orthogonal, we need to choose the right basis. The trace form $\langle x, y \rangle = \text{Tr}(x \bar{y})$ is a positive definite $\mathbb{Q}$-bilinear form on $\mathbb{Q}(\zeta)$ that is invariant under multiplication by $\zeta$ (since $\text{Tr}(\zeta x \cdot \overline{\zeta y}) = \text{Tr}(\zeta x \cdot \bar{\zeta} \bar{y}) = \text{Tr}(|\zeta|^2 x \bar{y}) = \text{Tr}(x \bar{y})$).

So if we choose an orthonormal basis (over $\mathbb{Q}$) for the trace form, the matrix of multiplication by $\zeta$ would be orthogonal. But an orthonormal basis over $\mathbb{Q}$ for the trace form means we need the trace form to be equivalent to the standard form over $\mathbb{Q}$.

The trace form $\text{Tr}(x \bar{y})$ on $\mathbb{Q}(\zeta)/\mathbb{Q}$: its discriminant is the discriminant of $\mathbb{Q}(\zeta)$. For $\zeta$ a primitive $p$-th root of unity ($p$ prime), the discriminant of $\mathbb{Q}(\zeta)$ is $(-1)^{(p-1)/2} p^{p-2}$. For $p = 127$: disc $= (-1)^{63} \cdot 127^{125} = -127^{125}$.

The discriminant of the trace form is $-127^{125}$. For the form to be equivalent to the identity (which has discriminant 1), we'd need $-127^{125}$ to be a perfect square, which it's not (since 127 is odd and the sign is negative). So the trace form is NOT equivalent to the identity form over $\mathbb{Q}$.

Hmm. So we can't just orthonormalize the trace form.

But we don't have to use the trace form. We can use any invariant positive definite form. The space of invariant symmetric bilinear forms is $\mathbb{Q}(\zeta + \bar{\zeta})$ (the maximal real subfield), which is 63-dimensional. We need to find an element $\beta$ in this space such that the corresponding form is positive definite and equivalent to the identity over $\mathbb{Q}$.

An invariant symmetric form is $\langle x, y \rangle_\beta = \text{Tr}(\beta x \bar{y})$ for $\beta \in \mathbb{Q}(\zeta+\bar{\zeta})$, $\beta$ totally positive. The discriminant of this form is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N_{\mathbb{Q}(\zeta+\bar{\zeta})/\mathbb{Q}}(\beta)^2$... actually, let me think more carefully.

The discriminant of the form $\text{Tr}(\beta x \bar{y})$ is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N(\beta)^2$ where $N$ is the norm from $\mathbb{Q}(\zeta+\bar{\zeta})$ to $\mathbb{Q}$... actually I'm not sure about the exact formula. Let me think differently.

Actually, the form $\text{Tr}(\beta x \bar{y})$ on the 126-dimensional space has discriminant $= \text{disc}(\mathbb{Q}(\zeta)) \cdot N_{\mathbb{Q}(\zeta+\bar{\zeta})/\mathbb{Q}}(\beta)^2$. Wait, I think the discriminant is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N(\beta)^{126/63}$... I'm getting confused with the formulas.

Let me think about it more carefully. The trace form $\text{Tr}_{\mathbb{Q}(\zeta)/\mathbb{Q}}(x \bar{x})$ has a certain discriminant $D$. If we modify it to $\text{Tr}(\beta x \bar{x})$ where $\beta$ is in the real subfield $K^+ = \mathbb{Q}(\zeta + \bar{\zeta})$ (degree 63), then the discriminant changes by $N_{K^+/\mathbb{Q}}(\beta)^2$ (since $\beta$ acts on the 126-dim space, and the norm of $\beta$ as an element of $K^+$ raised to the appropriate power...).

Actually, I think the discriminant of $\text{Tr}(\beta x \bar{y})$ is $\text{disc}(\mathbb{Q}(\zeta)) \cdot N_{K^+/\mathbb{Q}}(\beta)^2$. Since $\text{disc}(\mathbb{Q}(\zeta)) = -127^{125}$, the discriminant of the modified form is $-127^{125} \cdot N(\beta)^2$.

For this to be a perfect square (necessary for equivalence to identity), we need $-127^{125} \cdot N(\beta)^2$ to be a perfect square. But $-127^{125}$ is negative, so $-127^{125} \cdot N(\beta)^2$ is negative, and a negative number can't be a perfect square. 

Wait, but the discriminant of a positive definite form is positive! Let me recheck.

The discriminant of $\mathbb{Q}(\zeta)$ for $p = 127$: $\text{disc}(\mathbb{Q}(\zeta_p)) = (-1)^{(p-1)/2} p^{p-2}$. For $p = 127$, $(p-1)/2 = 63$, so $(-1)^{63} = -1$, giving $-127^{125}$.

But the trace form $\text{Tr}(x \bar{x})$ is positive definite (since $\mathbb{Q}(\zeta)$ is a CM field, $\text{Tr}(x\bar{x}) = \sum_\sigma \sigma(x)\overline{\sigma(x)} = \sum |\sigma(x)|^2 > 0$ for $x \neq 0$). A positive definite form has positive discriminant. So the discriminant of the trace form should be positive.

I think the issue is that the discriminant of the trace form $\text{Tr}(x\bar{y})$ is not the same as the discriminant of the number field. The discriminant of the number field $\mathbb{Q}(\zeta)$ is the discriminant of the trace form $\text{Tr}(xy)$ (without conjugation), which can be negative. The trace form $\text{Tr}(x\bar{y})$ is a different form.

Let me recalculate. The discriminant of $\text{Tr}(x\bar{y})$ with respect to the basis $1, \zeta, \zeta^2, \ldots, \zeta^{125}$: the $(i,j)$ entry is $\text{Tr}(\zeta^i \bar{\zeta}^j) = \text{Tr}(\zeta^{i-j})$. 

$\text{Tr}(\zeta^k) = \sum_{t=0}^{126} \zeta^{kt}$. For $k \equiv 0 \pmod{127}$, this is 126. For $k \not\equiv 0 \pmod{127}$, this is $\sum_{t=0}^{126} \zeta^{kt} = 0$ (sum of all 127th roots of unity, which is 0) minus... wait, $\sum_{t=0}^{126} (\zeta^k)^t = 0$ if $\zeta^k \neq 1$, i.e., if $k \not\equiv 0 \pmod{127}$. And $= 127$ if $k \equiv 0 \pmod{127}$.

But $\text{Tr}_{\mathbb{Q}(\zeta)/\mathbb{Q}}(\zeta^k) = \sum_{\sigma} \sigma(\zeta^k)$ where $\sigma$ ranges over all 126 embeddings. The embeddings are $\sigma_a: \zeta \mapsto \zeta^a$ for $a = 1, 2, \ldots, 126$. So $\text{Tr}(\zeta^k) = \sum_{a=1}^{126} \zeta^{ak}$.

For $k \equiv 0 \pmod{127}$: $\text{Tr}(\zeta^0) = \text{Tr}(1) = 126$.
For $k \not\equiv 0 \pmod{127}$: $\text{Tr}(\zeta^k) = \sum_{a=1}^{126} \zeta^{ak} = \sum_{a=0}^{126} \zeta^{ak} - 1 = 0 - 1 = -1$.

So the matrix of the trace form $\text{Tr}(\zeta^i \bar{\zeta}^j) = \text{Tr}(\zeta^{i-j})$ is a circulant-like matrix where the $(i,j)$ entry is $126$ if $i \equiv j \pmod{127}$ and $-1$ otherwise. This is $127 I - J$ where $J$ is the all-ones matrix (in the basis $\zeta^0, \ldots, \zeta^{125}$, but note we're using indices $0$ to $125$, which is 126 elements).

Wait, actually, the entries are $\text{Tr}(\zeta^{i-j})$ for $i, j \in \{0, 1, \ldots, 125\}$. When $i = j$, $\text{Tr}(1) = 126$. When $i \neq j$, $i - j \not\equiv 0 \pmod{127}$ (since $|i-j| \leq 125 < 127$), so $\text{Tr}(\zeta^{i-j}) = -1$.

So the matrix is $127 I_{126} - J_{126}$ where $J_{126}$ is the $126 \times 126$ all-ones matrix. The eigenvalues of $J_{126}$ are $126$ (once) and $0$ (125 times). So the eigenvalues of $127 I - J$ are $127 - 126 = 1$ (once) and $127$ (125 times). All positive, confirming positive definiteness.

The determinant is $1 \cdot 127^{125} = 127^{125}$.

So the discriminant of the trace form $\text{Tr}(x\bar{y})$ is $127^{125}$, which is positive (as expected for a positive definite form). Good.

Now, for the form $\text{Tr}(\beta x \bar{y})$ with $\beta \in K^+ = \mathbb{Q}(\zeta + \bar{\zeta})$ totally positive, the discriminant is $127^{125} \cdot N_{K^+/\mathbb{Q}}(\beta)^2$.

For this form to be equivalent to the identity over $\mathbb{Q}$, we need (among other things) the discriminant to be a perfect square. So we need $127^{125} \cdot N(\beta)^2 = \square$. Since $127^{125} = 127 \cdot (127^{62})^2$, we need $127 \cdot N(\beta)^2 = \square$, i.e., $127$ must be a perfect square times $N(\beta)^{-2}$... wait, $127^{125} \cdot N(\beta)^2 = 127 \cdot 127^{124} \cdot N(\beta)^2 = 127 \cdot (127^{62} \cdot N(\beta))^2$. For this to be a perfect square, we need $127$ to be a perfect square, which it's not.

So the discriminant is $127 \cdot (\text{something})^2$, which is never a perfect square. This means NO invariant positive definite form on $\mathbb{Q}(\zeta)$ is equivalent to the identity over $\mathbb{Q}$!

This means we CANNOT find a $126 \times 126$ orthogonal rational matrix with characteristic polynomial $\Phi_{127}$.

Wait, let me double-check this. The discriminant of the form $\text{Tr}(\beta x \bar{y})$ is $127^{125} \cdot N(\beta)^2$. For equivalence to the identity, we need this to be a perfect square. $127^{125} \cdot N(\beta)^2 = 127 \cdot (127^{62})^2 \cdot N(\beta)^2 = 127 \cdot (127^{62} N(\beta))^2$. This is a perfect square iff $127$ is a perfect square, which it's not. So indeed, no invariant form is equivalent to the identity.

Therefore, $n = 126$ is impossible!

So we need $n > 126$. What about $n = 127$? With $n = 127$, we can have the characteristic polynomial be $(x-1) \Phi_{127}(x) = x^{127} - 1$. The eigenvalue 1 corresponds to a 1-dimensional invariant subspace.

With the extra dimension (eigenvalue 1), we have more freedom. The invariant forms on the 1-dimensional eigenspace (for eigenvalue 1) can be any positive rational number. So the discriminant of the full form is $127^{125} \cdot N(\beta)^2 \cdot c$ where $c > 0$ is the form on the eigenvalue-1 space. We need $127^{125} \cdot N(\beta)^2 \cdot c = \square$, i.e., $127 \cdot (127^{62} N(\beta))^2 \cdot c = \square$, i.e., $127 c = \square$. So we need $c = 127 \cdot d^2$ for some rational $d$. Then the discriminant is $(127^{62} N(\beta) \cdot 127 d)^2 = (127^{63} N(\beta) d)^2$, a perfect square. 

But we also need the Hasse invariant to match. This requires more careful analysis.

Hmm, this is getting quite involved. Let me think about whether the answer is 127 or something else.

Actually, wait. I need to also check the Hasse-Minkowski invariants more carefully. Let me think about this from a higher level.

The question is: what is the minimal $n$ such that there exists an orthogonal rational $n \times n$ matrix of order 127?

The characteristic polynomial of such a matrix must be $(x-1)^a \Phi_{127}(x)^b$ where $a + 126b = n$ and $b \geq 1$. The minimal $n$ with $b = 1$ is $n = 126$ (with $a = 0$) or $n = 127$ (with $a = 1$).

We showed $n = 126$ doesn't work (discriminant obstruction). Let me check $n = 127$.

For $n = 127$, the matrix $Q$ has eigenvalues: one eigenvalue 1, and the 126 primitive 127th roots of unity. The rational canonical form is $\text{diag}(1, C)$ where $C$ is the companion matrix of $\Phi_{127}$.

An invariant positive definite form on the 127-dimensional space is $\text{Tr}(\beta x \bar{y})$ on the $\Phi_{127}$-part (126-dimensional) plus $c$ on the eigenvalue-1 part (1-dimensional). The discriminant is $127^{125} \cdot N(\beta)^2 \cdot c$.

For equivalence to identity: discriminant must be a perfect square. $127^{125} \cdot N(\beta)^2 \cdot c = 127 \cdot (127^{62} N(\beta))^2 \cdot c$. Need $127 c = \square$, so $c = 127 d^2$ for some $d \in \mathbb{Q}^*$.

Now we also need the Hasse invariant to be 1 (same as identity). The Hasse invariant of a direct sum is the product of Hasse invariants times some cross terms. This is getting complicated.

Let me try a different approach. Instead of trying to prove existence via quadratic form theory, let me try to construct an explicit orthogonal rational matrix of order 127.

Actually, let me think about this problem from a completely different angle. Maybe the answer is not 126 or 127 but something else entirely, and I'm missing something.

Let me reconsider. The problem asks for the smallest $n \geq 2$ such that there exists a normal $n \times n$ integer matrix $M$ whose sequence has period 7 and is not constant.

I've established:
1. If $M$ is normal, $M_1 = (M^T)^{-1} M$ is orthogonal (rational).
2. The sequence from $M_1$ is $M_1, M_1^2, M_1^4, \ldots, M_1^{2^{i-1}}, \ldots$
3. Period 7 means $M_1^{2^7} = M_1$ and $M_1^{2^k} \neq M_1$ for $k < 7$, i.e., $M_1^{127} = I$ and $M_1^{2^k - 1} \neq I$ for $k = 1, \ldots, 6$.
4. Since 127 is prime and $\text{ord}_{127}(2) = 7$, $M_1$ having order 127 gives period exactly 7.
5. The minimal $n$ is the minimal dimension of an orthogonal rational matrix of order 127.

And I've shown $n \geq 126$ (characteristic polynomial must include $\Phi_{127}$) and $n = 126$ is impossible (discriminant obstruction).

For $n = 127$, I need to verify that an orthogonal rational $127 \times 127$ matrix of order 127 exists.

Let me think about this more carefully. Consider the regular representation of the cyclic group $C_{127}$ acting on $\mathbb{Q}^{127}$. The group ring $\mathbb{Q}[C_{127}] \cong \mathbb{Q}[x]/(x^{127}-1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$ (by CRT, since $x^{127} - 1 = (x-1)\Phi_{127}(x)$ and $\Phi_{127}$ is irreducible).

The regular representation gives a $127 \times 127$ rational matrix (the permutation matrix of the cyclic shift) of order 127. But this permutation matrix is already orthogonal! It's a permutation matrix, hence signed permutation with all positive signs, hence orthogonal.

Wait, the cyclic shift permutation matrix $P$ of size 127 has order 127 and is orthogonal (it's a permutation matrix). Its characteristic polynomial is $x^{127} - 1 = (x-1)\Phi_{127}(x)$.

So $Q = P$ (the 127-cycle permutation matrix) is an orthogonal rational (even integer) matrix of order 127! And it's $127 \times 127$.

So $n = 127$ works for the orthogonal rational matrix part. Now I need to check that we can find a normal integer matrix $M$ with $M_1 = P$.

Using the Hilbert 90 approach: we need $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$, and then $M = f(P)$ where $f$ is the polynomial representing $\alpha$ in $\mathbb{Q}(\zeta)$, scaled to be integer.

But wait, $P$ is the companion matrix of $x^{127} - 1$, not of $\Phi_{127}$. The centralizer of $P$ is $\mathbb{Q}[P] \cong \mathbb{Q}[x]/(x^{127}-1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$. So $M = f(P)$ for $f \in \mathbb{Q}[x]/(x^{127}-1)$.

The condition $M^T = M P^T = M P^{-1} = M P^{126}$ (since $P$ is orthogonal, $P^T = P^{-1} = P^{126}$).

In terms of $\mathbb{Q}[x]/(x^{127}-1)$: $M = f(x)$, $M^T$ corresponds to $f(x^{-1}) = f(x^{126})$ (since $P^T = P^{126}$). The condition $M^T = M P^{126}$ becomes $f(x^{126}) = f(x) \cdot x^{126}$ in $\mathbb{Q}[x]/(x^{127}-1)$.

Under the CRT isomorphism $\mathbb{Q}[x]/(x^{127}-1) \cong \mathbb{Q} \times \mathbb{Q}(\zeta)$, $x \mapsto (1, \zeta)$. So $f$ maps to $(f(1), f(\zeta)) = (a, \alpha)$ where $a = f(1) \in \mathbb{Q}$ and $\alpha = f(\zeta) \in \mathbb{Q}(\zeta)$.

The condition $f(x^{126}) = f(x) \cdot x^{126}$:
- At $x = 1$: $f(1) = f(1) \cdot 1$, so $a = a$. Always true.
- At $x = \zeta$: $f(\zeta^{126}) = f(\zeta) \cdot \zeta^{126}$, i.e., $f(\bar{\zeta}) = \alpha \cdot \bar{\zeta}$, i.e., $\bar{\alpha} = \alpha \bar{\zeta}$, i.e., $\alpha / \bar{\alpha} = \zeta$.

So we need $\alpha / \bar{\alpha} = \zeta$ (same as before) and $a$ can be anything. By Hilbert 90, such $\alpha$ exists. Then $M = f(P)$ is rational, and we scale to make it integer.

But we also need $M$ to be normal. We showed normality is automatic given $M^T = M Q^T$ and $M$ commutes with $Q$. Let me double check: $M = f(P)$ commutes with $P$ (since it's a polynomial in $P$). And $M^T = M P^T$ is our condition. So $M$ is normal. ✓

And we need $M$ to be invertible. $M = f(P)$ is invertible iff $f(1) \neq 0$ and $f(\zeta) \neq 0$, i.e., $a \neq 0$ and $\alpha \neq 0$. We can choose $a = 1$ and $\alpha \neq 0$ (from Hilbert 90, $\alpha \neq 0$). ✓

So $n = 127$ works! But wait, I need to check that $n = 126$ really doesn't work, and also check if there's some clever way to get a smaller $n$.

Actually, wait. I think I need to reconsider. The issue with $n = 126$ was that no invariant positive definite form on the 126-dimensional irreducible representation is equivalent to the identity. But maybe I can use a non-irreducible representation?

For $n < 126$, the characteristic polynomial of $Q$ must be $(x-1)^a \Phi_{127}(x)^b$ with $a + 126b = n$ and $b \geq 1$. Since $b \geq 1$ and $126b \leq n < 126$, we need $b = 1$ and $a < 0$, which is impossible. So for $n < 126$, it's impossible to have order 127 (the characteristic polynomial can't include $\Phi_{127}$).

Wait, that's not right. The characteristic polynomial doesn't have to be a product of cyclotomic polynomials in that way. Let me reconsider.

$Q$ is a rational matrix with $Q^{127} = I$. The minimal polynomial of $Q$ divides $x^{127} - 1 = (x-1)\Phi_{127}(x)$. The characteristic polynomial is a product of powers of the irreducible factors of the minimal polynomial. Since $\Phi_{127}$ is irreducible over $\mathbb{Q}$, the characteristic polynomial is $(x-1)^a \Phi_{127}(x)^b$ where $a + 126b = n$.

For $Q$ to have order 127, we need $b \geq 1$ (otherwise $Q = I$). So $n = a + 126b \geq 126$.

For $n = 126$: $a = 0, b = 1$. Characteristic polynomial is $\Phi_{127}(x)$.
For $n = 127$: $a = 1, b = 1$. Characteristic polynomial is $(x-1)\Phi_{127}(x) = x^{127} - 1$.

I showed $n = 126$ fails (discriminant obstruction). And $n = 127$ works (permutation matrix).

But wait, I should double-check the $n = 126$ case more carefully. The issue is whether there exists a $126 \times 126$ orthogonal rational matrix with characteristic polynomial $\Phi_{127}$.

Such a matrix $Q$ would satisfy $Q^T Q = I$ and have char poly $\Phi_{127}$. The existence is equivalent to: the companion matrix $C$ of $\Phi_{127}$ is conjugate to an orthogonal matrix over $\mathbb{Q}$, i.e., there exists $S$ positive definite rational with $C^T S C = S$ and $S$ equivalent to $I$ over $\mathbb{Q}$.

I showed that any such $S$ has discriminant $127 \cdot (\text{square})$, which is not a perfect square, so $S$ is not equivalent to $I$.

But actually, I should be more careful. The space of symmetric forms $S$ with $C^T S C = S$ is not just the trace form. Let me reconsider.

The centralizer of $C$ (companion matrix of $\Phi_{127}$, irreducible) is $\mathbb{Q}[C] \cong \mathbb{Q}(\zeta)$. A symmetric bilinear form $S$ with $C^T S C = S$ corresponds to an element $\beta \in \mathbb{Q}(\zeta)$ with $\bar{\beta} = \beta$ (i.e., $\beta \in K^+ = \mathbb{Q}(\zeta + \bar{\zeta})$, the real subfield of degree 63).

The form is $S_\beta(x, y) = \text{Tr}(\beta x \bar{y})$ (up to identification). The discriminant of $S_\beta$ is $\text{disc}(\text{Tr}(\beta x \bar{y}))$.

Let me compute this. The matrix of $S_\beta$ in the basis $1, \zeta, \ldots, \zeta^{125}$ has $(i,j)$ entry $\text{Tr}(\beta \zeta^i \bar{\zeta}^j) = \text{Tr}(\beta \zeta^{i-j})$.

This is a "twisted" trace form. The discriminant of $\text{Tr}(\beta x \bar{y})$ is $N_{\mathbb{Q}(\zeta)/\mathbb{Q}}(\beta) \cdot \text{disc}(\text{Tr}(x\bar{y}))$... actually, I think the discriminant of $\text{Tr}(\beta x \bar{y})$ is $N_{K^+/\mathbb{Q}}(\beta)^2 \cdot \text{disc}(\text{Tr}(x\bar{y}))$.

Wait, let me think about this more carefully. $\beta \in K^+$, and $\text{Tr}(\beta x \bar{y})$ where the trace is from $\mathbb{Q}(\zeta)$ (degree 126) to $\mathbb{Q}$.

The discriminant of $\text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y})$ where $L = \mathbb{Q}(\zeta)$: this is a standard computation. If $\beta \in K^+ = L^+$ (the maximal real subfield), then $\text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y}) = \text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y})$.

Actually, since $L/K^+$ is a CM extension (degree 2), and $\beta \in K^+$, we have $\text{Tr}_{L/\mathbb{Q}}(\beta x \bar{y}) = \text{Tr}_{K^+/\mathbb{Q}}(\beta \text{Tr}_{L/K^+}(x\bar{y}))$.

Hmm, this is getting complicated. Let me just use the fact that the discriminant of $\text{Tr}(\beta x \bar{y})$ is $N_{K^+/\mathbb{Q}}(\beta)^2 \cdot D_0$ where $D_0 = 127^{125}$ is the discriminant of the untwisted trace form $\text{Tr}(x\bar{y})$.

Actually, I realize I should verify this. The map $\beta \mapsto S_\beta$ is a linear map from $K^+$ (63-dimensional) to symmetric $126 \times 126$ matrices. The determinant of $S_\beta$ as a function of $\beta$ is a homogeneous polynomial of degree 126 in the coordinates of $\beta$ (since $S_\beta$ is 126-dimensional). But $\beta$ has 63 coordinates, so $\det(S_\beta)$ is a degree 126 form in 63 variables... this doesn't factor as $N(\beta)^2$ in an obvious way.

Actually, I think the correct statement is: $\det(S_\beta) = N_{L/\mathbb{Q}}(\beta) \cdot D_0$ where $N_{L/\mathbb{Q}}$ is the norm from $L = \mathbb{Q}(\zeta)$ to $\mathbb{Q}$. Since $\beta \in K^+$, $N_{L/\mathbb{Q}}(\beta) = N_{K^+/\mathbb{Q}}(\beta)^2$ (because $L/K^+$ has degree 2 and $\beta \in K^+$, so $N_{L/\mathbb{Q}}(\beta) = N_{K^+/\mathbb{Q}}(N_{L/K^+}(\beta)) = N_{K^+/\mathbb{Q}}(\beta^2) = N_{K^+/\mathbb{Q}}(\beta)^2$).

So $\det(S_\beta) = N_{K^+/\mathbb{Q}}(\beta)^2 \cdot 127^{125}$.

For $S_\beta$ to be equivalent to $I_{126}$ over $\mathbb{Q}$, we need $\det(S_\beta) = \square$. So $N_{K^+/\mathbb{Q}}(\beta)^2 \cdot 127^{125} = \square$, i.e., $127^{125} = \square / N(\beta)^2 = \square$. But $127^{125} = 127 \cdot 127^{124} = 127 \cdot (127^{62})^2$, which is not a perfect square. Contradiction.

So indeed, $n = 126$ is impossible.

Now, for $n = 127$: the permutation matrix $P$ of the 127-cycle is a $127 \times 127$ orthogonal integer matrix of order 127. We need to find a normal integer matrix $M$ with $M_1 = (M^T)^{-1} M = P$.

As I argued, this requires $\alpha \in \mathbb{Q}(\zeta)^*$ with $\alpha / \bar{\alpha} = \zeta$ (Hilbert 90 gives existence), and then $M = f(P)$ where $f(1) = a \neq 0$ and $f(\zeta) = \alpha$, scaled to be integer.

Let me construct this more explicitly. By Hilbert 90, $\alpha = \zeta - 1$ works? Let me check: $\alpha / \bar{\alpha} = (\zeta - 1)/(\bar{\zeta} - 1) = (\zeta - 1)/(\zeta^{-1} - 1) = (\zeta - 1) \cdot \zeta / (1 - \zeta) = -\zeta$. So $\alpha / \bar{\alpha} = -\zeta$, not $\zeta$. Close but not quite.

Let me try $\alpha = \zeta + 1$: $\bar{\alpha} = \zeta^{-1} + 1 = (1 + \zeta)/\zeta$. $\alpha / \bar{\alpha} = (\zeta + 1) / ((1+\zeta)/\zeta) = \zeta$. Yes! So $\alpha = 1 + \zeta$ works.

So $f(\zeta) = 1 + \zeta$ and $f(1) = 1 + 1 = 2$. So $f(x) = 1 + x$ and $M = I + P$.

Let me verify: $M = I + P$ where $P$ is the 127-cycle permutation matrix.

$M^T = I + P^T = I + P^{-1} = I + P^{126}$.

$M P^T = (I + P)(I + P^{-1}) = (I + P)(P^{-1} + I) \cdot P^{-1} \cdot P$... let me just compute directly.

$M^T = I + P^{126}$. $M P^{126} = (I + P) P^{126} = P^{126} + P^{127} = P^{126} + I = I + P^{126} = M^T$. ✓

So $M^T = M P^{126} = M P^T$. ✓

Is $M$ normal? $M^T M = (I + P^{126})(I + P) = I + P + P^{126} + I = 2I + P + P^{126}$. $M M^T = (I + P)(I + P^{126}) = I + P^{126} + P + I = 2I + P + P^{126}$. So $M^T M = M M^T$. ✓ Normal.

Is $M$ invertible? $M = I + P$. The eigenvalues of $P$ are the 127th roots of unity. The eigenvalues of $M = I + P$ are $1 + \omega$ for each 127th root of unity $\omega$. For $\omega = -1$... but $-1$ is not a 127th root of unity (127 is odd). So all eigenvalues $1 + \omega \neq 0$, and $M$ is invertible. ✓

Is $M$ an integer matrix? $M = I + P$ where $P$ is a permutation matrix. Yes, $M$ is an integer matrix. ✓

Now let's verify $M_1 = (M^T)^{-1} M = P$.

$(M^T)^{-1} = (I + P^{126})^{-1}$. $M = I + P$.

$(M^T)^{-1} M = (I + P^{126})^{-1}(I + P)$.

Note that $I + P = P(P^{-1} + I) = P(I + P^{126})$ (since $P^{-1} = P^{126}$). So $(I + P^{126})^{-1}(I + P) = (I + P^{126})^{-1} P (I + P^{126}) = P$ (since $P$ commutes with $I + P^{126}$). 

Wait: $(I + P^{126})^{-1} \cdot P \cdot (I + P^{126})$. Since $P$ commutes with $P^{126}$ (both are powers of $P$), $P$ commutes with $I + P^{126}$, so $(I + P^{126})^{-1} P (I + P^{126}) = P (I+P^{126})^{-1}(I+P^{126}) = P$. ✓

So $M_1 = P$, which has order 127. The sequence is $M, P, P^2, P^4, P^8, P^{16}, P^{32}, P^{64}, P^{128} = P, \ldots$ with period 7 (since $P^{128} = P^{127} \cdot P = P$).

Wait, let me recheck the period. $M_1 = P$, $M_2 = P^2$, $M_3 = P^4$, $M_4 = P^8$, $M_5 = P^{16}$, $M_6 = P^{32}$, $M_7 = P^{64}$, $M_8 = P^{128} = P = M_1$. So $M_{i+7} = M_i$ for $i \geq 1$. ✓

Is the period exactly 7? We need $M_{1+k} \neq M_1$ for $k = 1, 2, 3, 4, 5, 6$, i.e., $P^{2^k} \neq P$ for $k = 1, \ldots, 6$, i.e., $P^{2^k - 1} \neq I$ for $k = 1, \ldots, 6$, i.e., $127 \nmid 2^k - 1$ for $k = 1, \ldots, 6$.

$2^1 - 1 = 1$, $2^2 - 1 = 3$, $2^3 - 1 = 7$, $2^4 - 1 = 15$, $2^5 - 1 = 31$, $2^6 - 1 = 63$. None of these are divisible by 127. ✓ (And $2^7 - 1 = 127$, which is divisible by 127.) ✓

So the period is exactly 7. And the sequence is not constant (since $M_1 = P \neq I = M_2^{\infty}$... well, $M_1 = P \neq P^2 = M_2$, so it's not constant). ✓

So $n = 127$ works. And $n = 126$ doesn't work. And $n < 126$ is impossible. So the answer is $\boxed{127}$.

Wait, but I should double-check that $n < 126$ is truly impossible. For $n < 126$, the characteristic polynomial of $Q$ (orthogonal rational of order 127) must be $(x-1)^a \Phi_{127}(x)^b$ with $a + 126b = n$, $b \geq 1$. Since $126b \geq 126 > n$ for $b \geq 1$ and $n < 126$, this is impossible. So indeed $n \geq 126$. ✓

And $n = 126$ is impossible because no invariant positive definite form on the irreducible 126-dimensional representation is equivalent to the identity (discriminant obstruction). ✓

And $n = 127$ works (explicit construction with $M = I + P$). ✓

Hmm wait, but I need to be more careful about the $n = 126$ case. I showed that the discriminant of any invariant form is $127^{125} \cdot N(\beta)^2 = 127 \cdot (\text{square})$, which is not a perfect square. But for a form to be equivalent to the identity, we need not just the discriminant to be a perfect square, but also the Hasse invariant to be 1. Since the discriminant is already not a perfect square, the form is not equivalent to the identity. This is sufficient.

But actually, I need to make sure I haven't made an error. Let me re-examine.

The claim is: there is no $126 \times 126$ orthogonal rational matrix $Q$ with $Q^{127} = I$ and $Q \neq I$.

Proof: Such $Q$ would have characteristic polynomial $\Phi_{127}(x)$ (since $n = 126 = \deg \Phi_{127}$ and $b = 1, a = 0$). The rational canonical form of $Q$ is the companion matrix $C$ of $\Phi_{127}$. So $Q = S C S^{-1}$ for some rational $S$.

$Q$ orthogonal means $Q^T Q = I$, i.e., $S^{-T} C^T S^T S C S^{-1} = I$, i.e., $C^T (S^T S) C = S^T S$. Let $T = S^T S$, which is positive definite rational. So $C^T T C = T$.

The space of symmetric $T$ with $C^T T C = T$ is parametrized by $\beta \in K^+$ (the real subfield), with $\det(T) = 127^{125} \cdot N_{K^+/\mathbb{Q}}(\beta)^2$.

For $T = S^T S$ with $S$ rational, $T$ must be equivalent to the identity over $\mathbb{Q}$ (since $S^T S$ and $I$ are equivalent: $S^T I S = S^T S = T$, so $T$ is equivalent to $I$). A necessary condition is $\det(T) = \square$ (perfect square in $\mathbb{Q}$). But $\det(T) = 127 \cdot (127^{62} N(\beta))^2$, which is $127$ times a square, not a square. Contradiction.

So $n = 126$ is impossible. ✓

Actually, I want to make sure about the formula $\det(T_\beta) = 127^{125} \cdot N_{K^+/\mathbb{Q}}(\beta)^2$. Let me verify this for $\beta = 1$ (the untwisted trace form).

For $\beta = 1$: $T_1$ has $(i,j)$ entry $\text{Tr}(\zeta^{i-j})$ for $i, j = 0, \ldots, 125$. As computed, this is $127 I - J$ (where $J$ is all-ones). $\det(127I - J) = 127^{125} \cdot (127 - 126) = 127^{125} \cdot 1 = 127^{125}$. And $N_{K^+/\mathbb{Q}}(1) = 1$. So $\det(T_1) = 127^{125} \cdot 1 = 127^{125}$. ✓

For general $\beta$: The determinant of $T_\beta$ as a function of $\beta$ is a polynomial. Since $T_\beta$ is the matrix of the form $\text{Tr}(\beta x \bar{y})$, and this form is the "twist" of the trace form by $\beta$, the determinant transforms as $\det(T_\beta) = N_{L/\mathbb{Q}}(\beta) \cdot \det(T_1)$ where $N_{L/\mathbb{Q}}$ is the norm from $L = \mathbb{Q}(\zeta)$ to $\mathbb{Q}$.

Since $\beta \in K^+ \subset L$, $N_{L/\mathbb{Q}}(\beta) = N_{K^+/\mathbb{Q}}(\beta)^{[L:K^+]} = N_{K^+/\mathbb{Q}}(\beta)^2$.

So $\det(T_\beta) = N_{K^+/\mathbb{Q}}(\beta)^2 \cdot 127^{125}$. ✓

Great, so the formula is confirmed. And $127^{125} = 127 \cdot (127^{62})^2$, so $\det(T_\beta) = 127 \cdot (127^{62} N(\beta))^2$, which is never a perfect square (since 127 is not a perfect square).

Therefore, $n = 126$ is impossible, and the answer is $n = 127$.

Let me also verify that the sequence is "not constant." The sequence is $M_0 = M = I + P$, $M_1 = P$, $M_2 = P^2$, etc. Since $M_0 \neq M_1$ (as $I + P \neq P$), the sequence is not constant. Also, $M_1 = P \neq P^2 = M_2$, etc. ✓

So the answer is $\boxed{127}$.

Let me also sanity-check by making sure I haven't made an error in the key step that normality of $M$ implies $M_1$ is orthogonal.

$M$ normal: $M^T M = M M^T$.
$M_1 = (M^T)^{-1} M$.
$M_1^T = M^T (M^{-1})^T = M^T (M^T)^{-1}$... wait. $M_1 = (M^T)^{-1} M$. $M_1^T = M^T ((M^T)^{-1})^T = M^T (M^T^T)^{-1} = M^T M^{-1}$.

$M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M$.

Since $M$ is normal, $M^T M = M M^T$, which gives $M^{-1} (M^T)^{-1} = (M^T)^{-1} M^{-1}$ (inverse of $M M^T = M^T M$ gives $(M^T)^{-1} M^{-1} = M^{-1} (M^T)^{-1}$). Also, $M^T M^{-1} = M^{-1} M^T$ (from $M^T M = M M^T$, left-multiply by $M^{-1}$: $M^{-1} M^T M = M^T$, right-multiply by $M^{-1}$: $M^{-1} M^T = M^T M^{-1}$).

So $M_1^T M_1 = M^T M^{-1} (M^T)^{-1} M = M^T (M^T)^{-1} M^{-1} M = I \cdot I = I$. ✓

And from $M_1$ orthogonal, $M_{i+1} = (M_i^T)^{-1} M_i = M_i^{-1} M_i = M_i$... wait, no. If $M_i$ is orthogonal, $M_i^T = M_i^{-1}$, so $(M_i^T)^{-1} = M_i$, and $M_{i+1} = M_i \cdot M_i = M_i^2$. ✓

So from $M_1$ onward, $M_{i+1} = M_i^2$, giving $M_i = M_1^{2^{i-1}}$. ✓

Everything checks out. The answer is $n = 127$.

Let me also think about whether I need to worry about the case where $M$ is normal but $M_1$ might not have order exactly 127. In our construction, $M_1 = P$ (the 127-cycle permutation), which has order 127. The period of the sequence $P, P^2, P^4, \ldots$ is the multiplicative order of 2 modulo 127, which is 7 (since $2^7 = 128 \equiv 1 \pmod{127}$ and 7 is prime, so the order is 7). ✓

Actually, I should verify that 7 is the exact order of 2 mod 127, not just that $2^7 \equiv 1$. Since 127 is prime, the order of 2 divides $126 = 2 \times 3^2 \times 7$. The divisors of 126 are: 1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126. We need to check that $2^d \not\equiv 1 \pmod{127}$ for $d | 126$, $d < 7$, i.e., $d \in \{1, 2, 3\}$ (since we need $d < 7$ and $d | 126$; but actually the order could be any divisor of 126, not just less than 7).

Wait, the period is the order of 2 mod 127. Let me compute this properly.

$2^1 = 2 \not\equiv 1$
$2^2 = 4 \not\equiv 1$
$2^3 = 8 \not\equiv 1$
$2^6 = 64 \not\equiv 1$
$2^7 = 128 \equiv 1 \pmod{127}$

So the order of 2 mod 127 divides 7. Since 7 is prime and $2^1 \neq 1$, the order is 7. ✓

(The order must divide 126 by Fermat's little theorem, and also divide 7 since $2^7 \equiv 1$. So the order divides $\gcd(126, 7) = 7$. Since $2^1 \not\equiv 1$, the order is 7.)

Great, so the period is exactly 7.

Now let me write up the complete proof.

Actually, let me reconsider one thing. I want to make sure the construction $M = I + P$ gives a valid $M_0$ that is part of the period-7 sequence. The sequence is:
- $M_0 = M = I + P$
- $M_1 = P$
- $M_2 = P^2$
- $M_3 = P^4$
- $M_4 = P^8$
- $M_5 = P^{16}$
- $M_6 = P^{32}$
- $M_7 = P^{64}$
- $M_8 = P^{128} = P = M_1$

So $M_{i+7} = M_i$ for $i \geq 1$. But what about $M_0$? We need $M_7 = M_0$, i.e., $P^{64} = I + P$. But $P^{64} \neq I + P$ in general (they're different matrices). 

Hmm, so the period starting from $M_0$ might not be 7. Let me reconsider.

The problem says "the sequence $\mathcal{S}_M$ has period $P = 7$, i.e., $M_{i+7} = M_i$." This should hold for all $i \geq 0$, including $i = 0$.

So we need $M_7 = M_0$, i.e., $M_1^{2^6} = M_0$, i.e., $P^{64} = I + P$. But this is not true!

So my construction doesn't quite work as stated. The issue is that $M_0 = M$ is not part of the periodic cycle; only $M_1, M_2, \ldots$ are periodic.

Let me reconsider. We need $M_{i+7} = M_i$ for ALL $i \geq 0$. In particular, $M_7 = M_0$.

$M_7 = M_1^{2^6} = P^{64}$. $M_0 = I + P$. So we need $P^{64} = I + P$, which is false.

So I need to choose $M$ more carefully. The condition is:
- $M_1 = (M^T)^{-1} M = Q$ (orthogonal, order 127)
- $M_0 = M$ must equal $M_7 = Q^{2^6} = Q^{64}$.

So $M = Q^{64}$. But also $M_1 = (M^T)^{-1} M = Q$. So $(Q^{64})^T)^{-1} Q^{64} = Q$.

$(Q^{64})^T = (Q^T)^{64} = Q^{-64} = Q^{127-64} = Q^{63}$ (since $Q^{127} = I$).

$(Q^{64})^T)^{-1} = (Q^{63})^{-1} = Q^{-63} = Q^{64}$.

So $M_1 = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

So if we set $M = Q^{64}$, then $M_1 = Q$, and $M_7 = Q^{2^6} = Q^{64} = M$. ✓

But we also need $M = Q^{64}$ to be a normal integer matrix.

$Q = P$ (the 127-cycle permutation matrix). $M = P^{64}$. This is a permutation matrix (hence integer and orthogonal). Is it normal? Permutation matrices are orthogonal, hence normal. ✓

But wait, if $M = P^{64}$ is orthogonal, then $M_1 = (M^T)^{-1} M = M^{-1} M = I$. That gives $M_1 = I$, and the sequence is constant from $M_1$ onward. That's not what we want!

The issue is: if $M$ is orthogonal, then $M_1 = (M^T)^{-1} M = M^{-1} M = I$, and the sequence becomes constant. So $M$ cannot be orthogonal.

So $M = Q^{64}$ being orthogonal is a problem. We need $M$ to be normal but NOT orthogonal.

Let me reconsider. We need:
1. $M$ is normal, integer, invertible.
2. $M_1 = (M^T)^{-1} M = Q$ (orthogonal, order 127).
3. $M_7 = M_0$, i.e., $Q^{64} = M$.

From (2) and (3): $M = Q^{64}$ and $(M^T)^{-1} M = Q$.

$(Q^{64})^T)^{-1} Q^{64} = Q$.

If $Q$ is orthogonal, $(Q^{64})^T = Q^{-64}$, so $((Q^{64})^T)^{-1} = Q^{64}$, and $M_1 = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

But $M = Q^{64}$ is orthogonal (since $Q$ is), so $M$ is orthogonal, and then $M_1 = I$... 

Wait, no. If $M$ is orthogonal, $M^T = M^{-1}$, so $(M^T)^{-1} = M$, and $M_1 = M \cdot M = M^2$. But we also said $M_1 = Q$. So $M^2 = Q$, i.e., $(Q^{64})^2 = Q^{128} = Q$. ✓ Consistent.

But then $M_2 = M_1^2 = Q^2$, $M_3 = Q^4$, ..., $M_7 = Q^{64} = M$. ✓

And the sequence is $M, Q, Q^2, Q^4, Q^8, Q^{16}, Q^{32}, Q^{64} = M, Q, \ldots$ with period 7. ✓

But wait, is the sequence constant? $M = Q^{64} \neq Q = M_1$ (since $Q$ has order 127 and $64 \not\equiv 1 \pmod{127}$). So the sequence is not constant. ✓

But the problem is: $M = Q^{64} = P^{64}$ is a permutation matrix, hence orthogonal. And if $M$ is orthogonal, $M_1 = M^2 = P^{128} = P$. So $M_1 = P = Q$. ✓

But then $M_2 = (M_1^T)^{-1} M_1$. $M_1 = P$ is orthogonal, so $M_2 = P^2$. ✓

So actually, the issue I was worried about doesn't arise. Let me re-examine.

If $M = P^{64}$ (orthogonal), then:
- $M_0 = P^{64}$
- $M_1 = (M_0^T)^{-1} M_0 = (P^{64})^{-1} \cdot P^{64}$... wait, $M_0^T = (P^{64})^T = (P^T)^{64} = P^{-64} = P^{63}$. $(M_0^T)^{-1} = (P^{63})^{-1} = P^{-63} = P^{64}$. $M_1 = P^{64} \cdot P^{64} = P^{128} = P$. ✓

- $M_2 = (M_1^T)^{-1} M_1 = (P^T)^{-1} P = P \cdot P = P^2$. ✓ (Since $P$ is orthogonal, $(P^T)^{-1} = P$.)

- $M_i = P^{2^{i-1}}$ for $i \geq 1$. ✓

- $M_7 = P^{64} = M_0$. ✓

- $M_8 = P^{128} = P = M_1$. ✓

So the sequence is $P^{64}, P, P^2, P^4, P^8, P^{16}, P^{32}, P^{64}, P, \ldots$ with period 7. ✓

And it's not constant since $P^{64} \neq P$. ✓

But wait, $M = P^{64}$ is orthogonal, and the problem requires $M$ to be normal. Orthogonal matrices are normal. ✓

But hold on—is the sequence really not constant? $M_0 = P^{64}$, $M_1 = P$. These are different (since $P$ has order 127 and $64 \not\equiv 1 \pmod{127}$). But also, is $M_0 = M_1$? No, $P^{64} \neq P$ since $P^{63} \neq I$. ✓ Not constant.

But actually, I realize there might be a subtlety. When $M$ is orthogonal, $M_1 = M^2$, and the sequence becomes $M, M^2, M^4, M^8, \ldots$ from the start. So $M_i = M^{2^i}$ for all $i \geq 0$. The period is the smallest $p$ with $M^{2^p} = M$, i.e., $M^{2^p - 1} = I$. With $M = P^{64}$, $M^{2^p - 1} = P^{64(2^p - 1)}$. We need $127 | 64(2^p - 1)$, i.e., $127 | 2^p - 1$ (since $\gcd(64, 127) = 1$). The smallest such $p$ is 7. ✓

So the period is 7. ✓

But wait, I need to double-check: is the sequence $M, M^2, M^4, \ldots$ when $M$ is orthogonal? 

$M_0 = M$. $M_1 = (M^T)^{-1} M = M^{-1} M = I$... 

NO! If $M$ is orthogonal, $M^T = M^{-1}$, so $(M^T)^{-1} = (M^{-1})^{-1} = M$. So $M_1 = M \cdot M = M^2$. ✓ (Not $I$.)

OK so I had it right. $M_1 = M^2$ when $M$ is orthogonal. Good.

So with $M = P^{64}$:
- $M_0 = P^{64}$
- $M_1 = (P^{64})^2 = P^{128} = P$
- $M_2 = P^2$
- $M_3 = P^4$
- ...
- $M_7 = P^{64} = M_0$ ✓

Period 7, not constant. $M = P^{64}$ is a $127 \times 127$ orthogonal (hence normal) integer matrix. ✓

So $n = 127$ works. But now I realize I need to re-examine whether we could potentially do better. The key constraint is that $M_1 = (M^T)^{-1} M$ must be orthogonal of order 127, and $M_7 = M_0$.

Actually, the condition $M_7 = M_0$ is automatically satisfied if $M_1$ has the right order. Let me re-derive.

If $M$ is normal, $M_1$ is orthogonal. Then $M_i = M_1^{2^{i-1}}$ for $i \geq 1$. The period of the sequence from $M_1$ is the order of 2 modulo $\text{ord}(M_1)$. 

For the full sequence (including $M_0$) to have period 7, we need $M_{i+7} = M_i$ for all $i \geq 0$. For $i \geq 1$, this is $M_1^{2^{i+6}} = M_1^{2^{i-1}}$, i.e., $M_1^{2^{i-1}(2^7 - 1)} = I$, which is satisfied if $M_1^{127} = I$ (since $2^7 - 1 = 127$). For $i = 0$: $M_7 = M_0$, i.e., $M_1^{64} = M_0$.

So we need $M_0 = M_1^{64}$. But $M_0 = M$ and $M_1 = (M^T)^{-1} M$. So $M = ((M^T)^{-1} M)^{64}$.

This is an additional constraint on $M$! It's not just that $M_1$ has order 127; we need $M = M_1^{64}$.

In our construction with $M = P^{64}$: $M_1 = P$ and $M_1^{64} = P^{64} = M$. ✓

But in the more general approach (where $M$ is not orthogonal), we need to ensure $M = M_1^{64}$.

Given $Q = M_1$ (orthogonal of order 127), we need $M = Q^{64}$ and $(M^T)^{-1} M = Q$.

$M = Q^{64}$. $M^T = (Q^{64})^T = (Q^T)^{64} = Q^{-64}$ (since $Q$ orthogonal). $(M^T)^{-1} = Q^{64}$. $M_1 = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

So $M = Q^{64}$ always works (for any orthogonal $Q$ of order 127), and $M$ is automatically orthogonal (hence normal). And $M$ is integer iff $Q$ is integer.

So the question reduces to: what is the minimal $n$ such that there exists an orthogonal **integer** matrix $Q$ of order 127?

Orthogonal integer matrices are signed permutation matrices. A signed permutation matrix of order 127: the underlying permutation must have a cycle whose length (or twice the length) is divisible by 127. Since 127 is prime, we need a cycle of length 127 (with product of signs = 1, giving order 127) or a cycle of length 127 with product of signs = -1 (giving order 254, not 127).

Wait, let me think about this. A signed permutation on a cycle of length $k$: if the product of signs around the cycle is $+1$, the order is $k$. If $-1$, the order is $2k$.

For order 127 (prime), we need a cycle of length 127 with product of signs $+1$. This requires $n \geq 127$.

Could we have a shorter cycle? A cycle of length $k$ with product of signs $+1$ has order $k$. For $k | 127$, $k = 1$ or $k = 127$. $k = 1$ gives order 1 (not 127). So we need $k = 127$.

What about combining multiple cycles? The order of a signed permutation is the lcm of the orders of its cycles. For the lcm to be 127, each cycle's order must divide 127, and at least one must be 127. So we need at least one cycle of length 127 (with product of signs $+1$). This requires $n \geq 127$.

So the minimal $n$ for an orthogonal integer matrix of order 127 is $n = 127$.

But wait—do we need $Q$ to be an integer matrix? Let me re-examine.

$M = Q^{64}$ must be an integer matrix. $Q = M_1 = (M^T)^{-1} M$ is rational (since $M$ is integer). $Q$ is orthogonal and rational. $M = Q^{64}$ must be integer.

So $Q$ doesn't have to be integer; it just needs to be rational orthogonal, and $Q^{64}$ must be integer.

This changes things! $Q$ can be a rational orthogonal matrix (not necessarily signed permutation), and we just need $Q^{64}$ to be an integer matrix.

So the question becomes: what is the minimal $n$ such that there exists a rational orthogonal $n \times n$ matrix $Q$ of order 127 with $Q^{64}$ being an integer matrix?

Hmm, but $Q^{64}$ being an integer matrix and $Q$ being rational orthogonal... Let me think about what $Q^{64}$ looks like.

If $Q$ has order 127, then $Q^{64} = Q^{-63} = (Q^{-1})^{63}$. Also, $Q^{64} = Q^{64}$.

Actually, since $Q^{127} = I$, $Q^{64} = Q^{64 \mod 127} = Q^{64}$. And $Q^{64}$ is also rational (since $Q$ is rational). For $Q^{64}$ to be integer, we need the entries of $Q^{64}$ to be integers.

Now, $M = Q^{64}$ is an integer matrix. Is $M$ normal? $M = Q^{64}$ where $Q$ is orthogonal. $M^T = (Q^T)^{64} = Q^{-64}$. $M^T M = Q^{-64} Q^{64} = I$. So $M$ is orthogonal, hence normal. ✓

And $M_1 = (M^T)^{-1} M = Q^{64} \cdot Q^{64} = Q^{128} = Q$. ✓

So the question is: minimal $n$ such that there exists a rational orthogonal $Q$ of order 127 with $Q^{64}$ integer.

Now, $Q^{64}$ is a rational matrix (power of rational matrix). For it to be integer, we need its entries to be integers.

The eigenvalues of $Q$ are 127th roots of unity. The eigenvalues of $Q^{64}$ are $\omega^{64}$ for each eigenvalue $\omega$ of $Q$. Since $\gcd(64, 127) = 1$, the map $\omega \mapsto \omega^{64}$ is a bijection on the 127th roots of unity. So $Q^{64}$ has the same order as $Q$ (order 127), and the same characteristic polynomial (up to relabeling of roots).

Actually, the characteristic polynomial of $Q^{64}$: if $Q$ has eigenvalues $\omega_1, \ldots, \omega_n$ (127th roots of unity), then $Q^{64}$ has eigenvalues $\omega_1^{64}, \ldots, \omega_n^{64}$. Since $\gcd(64, 127) = 1$, $\omega \mapsto \omega^{64}$ permutes the primitive 127th roots of unity. So the characteristic polynomial of $Q^{64}$ is the same as that of $Q$ (since the Galois group acts transitively on primitive roots, and the char poly has rational coefficients).

Wait, that's not quite right. The characteristic polynomial of $Q$ is $(x-1)^a \Phi_{127}(x)^b$. The eigenvalues of $Q^{64}$ are $1^{64} = 1$ (with multiplicity $a$) and $\omega^{64}$ for primitive 127th roots $\omega$ (with multiplicity $b$ each). Since $\omega \mapsto \omega^{64}$ permutes the primitive 127th roots, the characteristic polynomial of $Q^{64}$ is also $(x-1)^a \Phi_{127}(x)^b$. So $Q^{64}$ has the same characteristic polynomial as $Q$.

Now, $Q^{64}$ is a rational matrix (power of rational $Q$) with the same characteristic polynomial as $Q$. And $Q^{64}$ must be an integer matrix.

The question is: can $Q^{64}$ be an integer matrix even if $Q$ is not?

Let me think about this for $n = 126$. We need a rational orthogonal $126 \times 126$ matrix $Q$ of order 127 such that $Q^{64}$ is an integer matrix.

$Q$ has characteristic polynomial $\Phi_{127}(x)$. $Q^{64}$ also has characteristic polynomial $\Phi_{127}(x)$. $Q^{64}$ is a rational matrix with this characteristic polynomial, so its rational canonical form is the companion matrix $C$ of $\Phi_{127}$. For $Q^{64}$ to be an integer matrix, we need... well, $Q^{64}$ is similar to $C$ over $\mathbb{Q}$, and $Q^{64}$ is an integer matrix with characteristic polynomial $\Phi_{127}$.

The companion matrix $C$ of $\Phi_{127}$ is an integer matrix with characteristic polynomial $\Phi_{127}$. So integer matrices with this characteristic polynomial exist. The question is whether $Q^{64}$ can be one of them.

$Q^{64}$ is determined by $Q$: $Q^{64} = Q^{64}$. If $Q$ is rational orthogonal with char poly $\Phi_{127}$, then $Q^{64}$ is rational with char poly $\Phi_{127}$, and $Q^{64
