# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Does there exist a holomorphic function that is not identically zero and has an uncountable number of zeroes?       — 题目文本
#   Okay, so the question is asking if there's a holomorphic function that isn't zero everywhere but still has an uncountable number of zeros. Hmm, interesting. Let me start by recalling some complex analysis basics.

First, holomorphic functions are complex differentiable at every point in their domain. I remember that one key property of holomorphic functions is their behavior regarding zeros. If a holomorphic function has a sequence of zeros that accumulate (i.e., get arbitrarily close) to a point within its domain, then the function must be identically zero on the connected component containing that accumulation point. This is known as the identity theorem, I think.

So, if a function has an uncountable number of zeros, that might mean the zeros aren't just a countable set. But in complex analysis, zeros of a non-zero holomorphic function are isolated. Wait, that's a theorem, right? The identity theorem says that if the zeros have an accumulation point in the domain, the function is zero everywhere. So, if a function isn't identically zero, its zeros must be isolated, meaning each zero has a neighborhood with no other zeros. 

But isolated points would form a countable set, right? Because in a connected open subset of the complex plane, every uncountable set has an accumulation point. So if you have uncountably many zeros, they must accumulate somewhere in the domain, which by the identity theorem would force the function to be zero everywhere. Therefore, such a function cannot exist. 

Wait, let me verify this step by step. Suppose there is a holomorphic function f defined on a domain D (which is open and connected) such that f is not identically zero, but the set Z = {z ∈ D | f(z) = 0} is uncountable. Since D is a subset of the complex plane, which is a separable space (it has a countable dense subset, like the complex numbers with rational real and imaginary parts), any uncountable subset of D must have a limit point in D. This is due to the fact that in a metric space with a countable base, every uncountable subset has a limit point in the space. 

So, if Z is uncountable, then by the identity theorem, since the zeros accumulate at some point in D, f must be identically zero on D. But that contradicts the assumption that f is not identically zero. Therefore, such a function cannot exist. 

But wait, maybe the domain isn't connected? The problem didn't specify, but usually, in complex analysis, unless stated otherwise, domains are connected. If the domain is disconnected, maybe you could have uncountably many zeros spread across different components? But even then, each connected component is an open set. If the function is holomorphic on the entire domain, each connected component is a domain on its own. If the function has uncountably many zeros, then in at least one of those components, the zeros would still have to be uncountable, but again, in each connected component (which is a domain in C), uncountable zeros would lead to an accumulation point, hence the function is zero on that component. So even if the domain is disconnected, unless you have uncountably many components, which isn't possible in C, since C is second countable. 

Wait, the domain could be a collection of uncountably many disjoint open sets? But in C, open sets are made up of countably many disjoint connected components. So, actually, a domain in C can't have uncountably many connected components. Therefore, even if the domain is disconnected, the number of connected components is countable. Therefore, if the function has uncountably many zeros, one of the connected components must contain uncountably many zeros, which again leads to the function being identically zero on that component. But the problem states the function is not identically zero, so maybe it's zero on some components and non-zero on others? But in that case, the zeros are on a union of countably many components, each of which could be a single point if the component is a single point? Wait, no, connected components in a domain in C are open, so they can't be single points. So each connected component is a region where the function is either identically zero or has isolated zeros. 

Therefore, even if the domain is disconnected, the zeros must be on countably many connected components (each of which the function is identically zero) or have isolated zeros. So in total, the zeros would be a countable union of countable sets or uncountable, but if there are uncountably many zeros, they would have to lie in uncountably many connected components, which is impossible. Therefore, the zeros must be countable. 

Therefore, regardless of the domain's connectedness, a holomorphic function not identically zero cannot have uncountably many zeros. So the answer is no, such a function does not exist. 

Let me check if I missed something. Maybe if the function is defined on a non-open set? But holomorphic functions are defined on open sets. If the function is defined on a non-open set with accumulation points outside the domain, but the problem says "has an uncountable number of zeros". For example, suppose the domain is the unit disk, and the function has zeros at uncountably many points inside the disk. But as the unit disk is a separable metric space, any uncountable subset has a limit point in the closure. If the closure is within the domain, then the function is zero. If the limit point is on the boundary, which is not in the domain, then the zeros inside the domain don't accumulate to a point in the domain. But in that case, can you have uncountably many zeros without an accumulation point in the domain?

Wait, in topology, a space is Lindelöf if every open cover has a countable subcover. Every separable metric space is Lindelöf. The complex plane is separable, so any open subset is Lindelöf. So, in an open domain D in C, suppose we have an uncountable set of zeros. Then, since D is Lindelöf, every uncountable subset must have a limit point in D. Wait, is that true? Let me recall: in a Lindelöf space, every uncountable subset has a condensation point (a point where every neighborhood contains uncountably many points of the set), which in a metric space is a limit point. So yes, in a Lindelöf space (which open sets in C are), every uncountable subset has a condensation point, which is a limit point. Therefore, even if you try to have an uncountable set of zeros in D, they must have a limit point in D, so by identity theorem, the function is zero everywhere. Therefore, there's no non-zero holomorphic function with uncountably many zeros in any open domain in C. 

Therefore, the answer is no, such a function does not exist. 

**Final Answer**
\boxed{No}
</think>

To determine if there exists a holomorphic function that is not identically zero but has an uncountable number of zeros, we need to recall key properties of holomorphic functions and their zeros.

1. **Identity Theorem**: If a holomorphic function has zeros that accumulate at a point within its domain, the function must be identically zero on the connected component containing that accumulation point.
2. **Isolated Zeros**: For a non-zero holomorphic function, zeros must be isolated. This means each zero has a neighborhood with no other zeros.
3. **Uncountable Sets in Separable Spaces**: The complex plane is a separable space, meaning every uncountable subset has a limit point within the space. In a domain (open and connected subset) of the complex plane, any uncountable set of zeros would have a limit point in the domain.
4. **Lindelöf Property**: Open sets in the complex plane are Lindelöf, implying every uncountable subset has a condensation point (which is a limit point in a metric space).

Given these properties, if a holomorphic function had an uncountable number of zeros, those zeros would necessarily accumulate at some point within the domain. By the identity theorem, this would force the function to be identically zero throughout the domain, contradicting the requirement that the function is not identically zero. 

Thus, no such holomorphic function can exist.

\[
\boxed{No}
\]  — 标准解答
#   Let me think about this problem carefully.

The question: Does there exist a smooth function $u$ on $S^1$ such that the generalized Fourier series $u = \sum_{n \in \mathbb{N}} \langle u, u_n \rangle u_n$ does not converge uniformly, where $\{u_n\}$ is an orthonormal basis of smooth functions on $S^1$?

So we get to choose the orthonormal basis $\{u_n\}$ of smooth functions on $S^1$ (with respect to $L^2$ inner product presumably), and we need to find a smooth function $u$ such that its generalized Fourier series (expansion in this basis) does not converge uniformly.

First, let me think about the standard case. The standard Fourier basis $e^{inx}/\sqrt{2\pi}$ gives uniform convergence for smooth functions (in fact, the Fourier series of a smooth function converges absolutely and uniformly, with rapid decay of coefficients).

But here we're allowed to choose ANY orthonormal basis of smooth functions. The question is whether there exists some "bad" orthonormal basis and some smooth function whose expansion doesn't converge uniformly.

This is a classic type of result. Let me think about it.

Key insight: The uniform norm and $L^2$ norm are different. We can construct an orthonormal basis where the partial sums have large uniform norm.

Actually, let me think about this more carefully. The question is whether there EXISTS such a basis and such a function.

One approach: Take the standard Fourier basis and apply a unitary transformation that mixes modes in a way that destroys uniform convergence.

Actually, a cleaner approach. Consider the following. We want an orthonormal basis $\{u_n\}$ of smooth functions and a smooth $u$ such that $\sum \langle u, u_n\rangle u_n$ doesn't converge uniformly.

Let me think about what's known. There's a classical result that for any orthonormal basis, the Fourier series converges in $L^2$. But uniform convergence is not guaranteed for arbitrary orthonormal bases.

Actually, there's a result by... let me think. The Menshov-Rademacher theorem and related results are about orthogonal systems.

Let me think about a concrete construction.

Consider smooth functions on $S^1$. The space $C^\infty(S^1)$ is dense in $L^2(S^1)$. We can build an orthonormal basis of smooth functions by Gram-Schmidt on some countable dense set of smooth functions.

The idea: We want to construct an orthonormal basis where the partial sums of some smooth function blow up in sup norm.

Here's a strategy. Let's think about it in terms of the following. Consider a smooth function $u$ with $\|u\|_\infty = 1$ but $\|u\|_{L^2}$ very small. If we can make $u$ itself one of the basis elements, say $u = u_N$, then the partial sum $S_N = \sum_{n=1}^N \langle u, u_n\rangle u_n$ includes the term $\langle u, u_N\rangle u_N = \|u\|_{L^2}^2 \cdot u / \|u\|_{L^2}$... wait, if $u_N = u/\|u\|_{L^2}$, then $\langle u, u_N\rangle = \|u\|_{L^2}$, and the contribution is $\|u\|_{L^2} \cdot u_N = \|u\|_{L^2} \cdot u/\|u\|_{L^2} = u$. So the partial sum up to $N$ would include $u$ itself (plus other terms). That doesn't immediately help.

Let me think differently.

Alternative approach: We want the partial sums to not converge uniformly. One way is to make the partial sums oscillate or diverge in sup norm.

Classic construction idea: Take a sequence of smooth functions $\phi_k$ that are orthonormal in $L^2$ but have large sup norm. Then for a suitable smooth $u$, the partial sums can have large sup norm.

Actually, here's a cleaner idea. Consider the following construction:

Take the standard trigonometric basis. Now, construct a new orthonormal basis by taking "blocks" of the standard basis and applying unitary transformations within each block.

Specifically, partition $\mathbb{Z}$ into blocks $B_1, B_2, \ldots$ and within each block, apply a unitary transformation to the exponentials. The new basis elements are still smooth (finite linear combinations of exponentials), and they're still orthonormal.

Now, the Fourier coefficients of $u$ in the new basis are related to the standard Fourier coefficients by the unitary transformations within blocks.

The partial sums in the new basis group terms by blocks. If we order the new basis so that all elements of block $B_k$ come together, then the partial sum at the end of block $B_k$ equals the partial sum of the standard Fourier series up to the max frequency in blocks $B_1, \ldots, B_k$ (since unitary transformations within blocks preserve the partial sum within each block — the projection onto the span of a block is invariant under unitary transformations of that block).

Wait, that's a key point. If we apply a unitary transformation within a block, the projection onto the span of that block is unchanged. So the partial sum at block boundaries is the same as the standard Fourier partial sum at the corresponding frequency. This means block-diagonal unitary transformations don't change the partial sums at block boundaries.

But the partial sums WITHIN a block can be different! And if the blocks are large, the intermediate partial sums within a block can be very different from the standard Fourier partial sums.

So the strategy is: make large blocks, and within each block, apply a unitary transformation such that some intermediate partial sum within the block has huge sup norm.

Let me formalize this.

Let the standard basis be $e_n(x) = e^{inx}/\sqrt{2\pi}$ for $n \in \mathbb{Z}$. Consider blocks $B_k = \{N_k, N_k+1, \ldots, N_k + m_k - 1\}$ (in terms of frequencies). Within block $B_k$, we have $m_k$ basis elements. We apply an orthogonal (unitary) transformation $O_k \in O(m_k)$ to get new basis elements $u_{k,j} = \sum_{i} (O_k)_{ji} e_{N_k + i}$.

These are still smooth (trigonometric polynomials), orthonormal, and form a complete basis.

Now, take $u$ to be a smooth function. Its standard Fourier coefficients are $\hat{u}(n) = \langle u, e_n\rangle$. The new coefficients are $\langle u, u_{k,j}\rangle = \sum_i (O_k)_{ji} \hat{u}(N_k + i)$.

The partial sum of the new series up to some point within block $B_k$ is:
$$S = \sum_{\text{completed blocks}} \text{projection onto span of block} + \text{partial projection within block } B_k$$

The projection onto completed blocks equals the standard Fourier partial sum up to the max frequency of those blocks. Within block $B_k$, the partial sum depends on which basis elements we've included so far.

So the partial sum at some intermediate point in block $B_k$ is:
$$S = \text{(standard partial sum up to } N_k - 1) + \sum_{j=1}^{J} \langle u, u_{k,j}\rangle u_{k,j}$$

where $J < m_k$.

The term $\sum_{j=1}^{J} \langle u, u_{k,j}\rangle u_{k,j}$ is a partial sum of the expansion of $u$'s projection onto block $B_k$ in the rotated basis. This can be made large in sup norm by choosing the rotation appropriately.

Let me think about how to make this concrete.

Consider a single block with frequencies $\{0, 1, \ldots, m-1\}$ (for simplicity, say the constant term and first harmonics). The projection of $u$ onto this block is $P u = \sum_{n=0}^{m-1} \hat{u}(n) e_n$. In the standard basis, the partial sums of $Pu$ converge nicely. But if we rotate the basis, the partial sums of $Pu$ in the rotated basis can be made large.

Specifically, $Pu$ is a trigonometric polynomial of degree $m-1$. Its $L^2$ norm is $\|Pu\|_{L^2} = (\sum_{n=0}^{m-1} |\hat{u}(n)|^2)^{1/2}$. We can write $Pu = \sum_{j=1}^{m} c_j v_j$ where $v_j$ is the rotated basis and $c_j = \langle u, v_j\rangle$.

The partial sum $\sum_{j=1}^{J} c_j v_j$ is the projection of $Pu$ onto the span of $\{v_1, \ldots, v_J\}$. By choosing the rotation, we can make this projection have large sup norm.

In fact, we can choose $v_1 = Pu / \|Pu\|_{L^2}$. Then $c_1 = \|Pu\|_{L^2}$, and the first partial sum is $c_1 v_1 = Pu$. So the partial sum after one term of the block equals $Pu$ plus the standard partial sum up to the previous block. That's not larger than the full thing.

Hmm, let me think about this differently. We want the partial sum to be much LARGER than $u$ in sup norm.

Consider this: take $v_1$ to be a function in the span of the block with $\|v_1\|_{L^2} = 1$ but $\|v_1\|_\infty$ very large. Then $c_1 = \langle u, v_1\rangle$ and the partial sum includes $c_1 v_1$ which has sup norm $|c_1| \|v_1\|_\infty$.

But $|c_1| = |\langle u, v_1\rangle| \leq \|u\|_{L^2} \|v_1\|_{L^2} = \|u\|_{L^2}$ (since $\|v_1\|_{L^2} = 1$). And $\|v_1\|_\infty$ can be as large as $\sqrt{m}$ (for a trigonometric polynomial of degree $m$ with $L^2$ norm 1, the sup norm can be up to $\sqrt{m}$, achieved by a Dirichlet-like kernel).

Actually, the sup norm of a trigonometric polynomial of degree $N$ with $L^2$ norm 1 can be as large as $\sqrt{2N+1}$ (the Dirichlet kernel $D_N$ has $L^2$ norm $\sqrt{2\pi(2N+1)}$ and sup norm $2\pi(2N+1)$, so normalized, sup norm / $L^2$ norm $= \sqrt{2N+1}$... let me be more careful).

Let me use the normalized basis $e_n = e^{inx}/\sqrt{2\pi}$. Then $\|e_n\|_{L^2} = 1$ and $\|e_n\|_\infty = 1/\sqrt{2\pi}$.

The Dirichlet kernel $D_N(x) = \sum_{n=-N}^{N} e^{inx} = \frac{\sin((N+1/2)x)}{\sin(x/2)}$. In terms of the normalized basis, $\sum_{n=-N}^{N} e_n = D_N(x)/\sqrt{2\pi}$. The $L^2$ norm of $\sum_{n=-N}^N e_n$ is $\sqrt{2N+1}$ (since the $e_n$ are orthonormal). The sup norm is $\|D_N\|_\infty / \sqrt{2\pi} = (2N+1)/\sqrt{2\pi}$.

So the ratio $\|\sum_{n=-N}^N e_n\|_\infty / \|\sum_{n=-N}^N e_n\|_{L^2} = (2N+1)/\sqrt{2\pi} / \sqrt{2N+1} = \sqrt{2N+1}/\sqrt{2\pi} \sim \sqrt{N}$.

OK so for a block of size $m$ (frequencies in a range), we can find a unit vector in the span with sup norm $\sim \sqrt{m}$.

Now, let's set up the construction. We want to choose $u$ smooth and blocks such that the partial sums blow up.

Let me try a specific construction. Let $u$ be a smooth function, say $u(x) = \sum_{n} a_n e_n(x)$ with rapid decay (since $u$ is smooth). 

Consider blocks $B_k$ of size $m_k$ at frequencies around $N_k$. The standard Fourier coefficients of $u$ at these frequencies are $a_{N_k}, a_{N_k+1}, \ldots$ which decay rapidly.

Within block $B_k$, the projection of $u$ is $P_k u = \sum_{n \in B_k} a_n e_n$ with $L^2$ norm $\rho_k = (\sum_{n \in B_k} |a_n|^2)^{1/2}$.

Now, in the rotated basis for block $B_k$, let the first basis vector be $v_{k,1} = P_k u / \rho_k$ (if $\rho_k > 0$). Then $\langle u, v_{k,1}\rangle = \rho_k$ and the first partial sum within the block is $\rho_k \cdot v_{k,1} = P_k u$. This just gives us $P_k u$, which is bounded.

That's not helpful. Let me instead make the first basis vector in the block be something with large sup norm, say $w_k = $ (normalized Dirichlet-like kernel in the block's frequency range). Then $\langle u, w_k\rangle$ could be small (since $u$'s coefficients decay), but the partial sum $\langle u, w_k\rangle w_k$ has sup norm $|\langle u, w_k\rangle| \|w_k\|_\infty$.

We have $|\langle u, w_k\rangle| \leq \|P_k u\|_{L^2} \|w_k\|_{L^2} = \rho_k \cdot 1 = \rho_k$. And $\|w_k\|_\infty \sim \sqrt{m_k}$. So the sup norm of the partial sum contribution is at most $\rho_k \sqrt{m_k}$.

But actually, we can be more precise. $\langle u, w_k\rangle = \sum_{n \in B_k} a_n \langle e_n, w_k\rangle = \sum_{n \in B_k} a_n \overline{\hat{w}_k(n)}$. If $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (the normalized flat sum), then $\langle e_n, w_k\rangle = 1/\sqrt{m_k}$, so $\langle u, w_k\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n$.

The partial sum after including $w_k$ as the first element of block $B_k$ is:
$$S = \text{(standard partial sum up to before block } B_k) + \langle u, w_k\rangle w_k$$

The sup norm of $\langle u, w_k\rangle w_k$ is $|\langle u, w_k\rangle| \|w_k\|_\infty = \left|\frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n\right| \cdot \frac{m_k}{\sqrt{2\pi}\sqrt{m_k}} \cdot \sqrt{2\pi}$...

Hmm, let me be more careful with normalizations. Let me use $e_n(x) = e^{inx}/\sqrt{2\pi}$, so $\|e_n\|_{L^2} = 1$, $\|e_n\|_\infty = 1/\sqrt{2\pi}$.

For a block $B_k = \{N_k, \ldots, N_k + m_k - 1\}$, define $w_k = \frac{1}{\sqrt{m_k}} \sum_{n=N_k}^{N_k+m_k-1} e_n$. Then $\|w_k\|_{L^2} = 1$ and $\|w_k\|_\infty = \frac{1}{\sqrt{m_k}} \cdot \frac{1}{\sqrt{2\pi}} \cdot \left\|\sum_{n=N_k}^{N_k+m_k-1} e^{inx}\right\|_\infty$.

Now $\sum_{n=N_k}^{N_k+m_k-1} e^{inx} = e^{iN_k x} \sum_{j=0}^{m_k-1} e^{ijx} = e^{iN_k x} \frac{1 - e^{im_k x}}{1 - e^{ix}}$. The sup norm of this is $m_k$ (at $x = 0$). So $\|w_k\|_\infty = \frac{m_k}{\sqrt{m_k} \sqrt{2\pi}} = \frac{\sqrt{m_k}}{\sqrt{2\pi}}$.

And $\langle u, w_k\rangle = \frac{1}{\sqrt{m_k}} \sum_{n=N_k}^{N_k+m_k-1} a_n$ where $a_n = \langle u, e_n\rangle = \sqrt{2\pi} \hat{u}(n)$ (with the standard Fourier convention $\hat{u}(n) = \frac{1}{2\pi}\int u(x) e^{-inx} dx$... actually let me not worry about the exact normalization and just work with $a_n = \langle u, e_n\rangle$).

So the partial sum contribution from $w_k$ is $\langle u, w_k\rangle w_k$, with sup norm:
$$|\langle u, w_k\rangle| \|w_k\|_\infty = \left|\frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n\right| \cdot \frac{\sqrt{m_k}}{\sqrt{2\pi}} = \frac{1}{\sqrt{2\pi}} \left|\sum_{n \in B_k} a_n\right|$$

Now, for a smooth function $u$, the coefficients $a_n$ decay rapidly. If the block is at high frequencies $N_k$ with size $m_k$, then $|a_n| \lesssim N_k^{-p}$ for any $p$ (since $u$ is smooth). So $|\sum_{n \in B_k} a_n| \lesssim m_k \cdot N_k^{-p}$.

To make this large, we'd need $m_k \cdot N_k^{-p}$ to be large, but for smooth $u$, we can take $p$ as large as we want, so this seems hard to make diverge.

Hmm, but wait. We get to CHOOSE $u$. So let's choose $u$ strategically.

Actually, the key issue is: we need $u$ to be smooth (so coefficients decay faster than any polynomial), but we want $\sum_{n \in B_k} a_n$ to not go to zero (or to grow).

If $u$ is smooth, $|a_n| \leq C_p (1+|n|)^{-p}$ for all $p$. So $|\sum_{n \in B_k} a_n| \leq C_p m_k N_k^{-p}$. For this to be bounded below, we need $m_k \geq c N_k^p$ for some $p$. But since $p$ can be arbitrarily large (smooth function), we'd need $m_k$ to grow faster than any polynomial in $N_k$. 

But wait, we also need the blocks to cover all frequencies and be disjoint. If $m_k$ grows super-polynomially relative to $N_k$, and $N_{k+1} = N_k + m_k$, then $N_k$ grows very fast. The coefficients $a_n$ for $n \in B_k$ are roughly $a_{N_k}$ (if $m_k$ is not too large relative to the decay scale), and $a_{N_k} \sim N_k^{-p}$ for all $p$.

Actually, for a smooth function, $a_n$ decays faster than any polynomial, but we can choose $u$ such that $a_n$ doesn't decay TOO fast. For instance, $a_n \sim e^{-\sqrt{|n|}}$ or $a_n \sim e^{-|n|^\alpha}$ for some $\alpha < 1$. Such a function is still smooth (since $e^{-|n|^\alpha}$ decays faster than any polynomial for any $\alpha > 0$).

Wait, is that right? $e^{-|n|^\alpha}$ for $\alpha > 0$: does $\sum n^p e^{-n^\alpha}$ converge for all $p$? Yes, because $e^{-n^\alpha}$ decays faster than any polynomial. So $u(x) = \sum a_n e^{inx}$ with $a_n = e^{-|n|^\alpha}$ is smooth for any $\alpha > 0$.

But it's not analytic (for $\alpha < 1$). That's fine, we only need smooth.

Now, with $a_n = e^{-n^\alpha}$ (for $n > 0$), consider a block $B_k = \{N_k, \ldots, N_k + m_k - 1\}$. Then $\sum_{n \in B_k} a_n \approx m_k \cdot e^{-N_k^\alpha}$ (if $m_k \ll N_k$ so that $a_n$ doesn't vary much over the block). 

The sup norm of the partial sum contribution is $\sim \frac{m_k e^{-N_k^\alpha}}{\sqrt{2\pi}}$.

For this to diverge, we need $m_k e^{-N_k^\alpha} \to \infty$, i.e., $m_k \gg e^{N_k^\alpha}$.

But we also need $m_k \ll N_k$ for the approximation to hold (so that $a_n$ doesn't vary much). This gives $e^{N_k^\alpha} \ll N_k$, which is impossible for large $N_k$.

So this doesn't work with this choice. Let me reconsider.

Actually, I don't need $a_n$ to be approximately constant over the block. Let me reconsider.

The sup norm of the partial sum contribution from $w_k$ is $\frac{1}{\sqrt{2\pi}} |\sum_{n \in B_k} a_n|$. I need this to not go to zero.

If $a_n = e^{-n^\alpha}$ and the block is $\{N_k, \ldots, N_k + m_k - 1\}$, then $\sum_{n \in B_k} a_n \leq m_k e^{-N_k^\alpha}$. For this to be $\geq c > 0$, we need $m_k \geq c e^{N_k^\alpha}$.

But then $N_{k+1} = N_k + m_k \geq N_k + c e^{N_k^\alpha}$, which grows very fast. The point is that the blocks would be huge, but that's OK — we just need the construction to work.

But wait, we also need $u$ to be in $L^2$, i.e., $\sum |a_n|^2 < \infty$. With $a_n = e^{-n^\alpha}$, this is fine for any $\alpha > 0$.

And we need $u$ to be smooth, which requires $\sum n^{2p} |a_n|^2 < \infty$ for all $p$, i.e., $\sum n^{2p} e^{-2n^\alpha} < \infty$, which is true for any $\alpha > 0$.

So let's try: $a_n = e^{-n^\alpha}$ for $n \geq 1$ (and $a_{-n} = a_n$ or just work with one-sided, or set $a_{-n} = 0$).

Actually, let me work on $S^1 = \mathbb{R}/2\pi\mathbb{Z}$ and use the basis $e_n = e^{inx}/\sqrt{2\pi}$ for $n \in \mathbb{Z}$.

Let me set $a_n = e^{-|n|^\alpha}$ for some $0 < \alpha < 1$, and $a_0 = 0$ (or whatever). Then $u(x) = \sum_{n \in \mathbb{Z}} a_n e_n(x)$ is smooth.

Now, I need to construct the orthonormal basis. Here's the plan:

1. Partition $\mathbb{Z}_{>0}$ (positive frequencies) into blocks $B_1, B_2, \ldots$ where $B_k = \{N_k, N_k + 1, \ldots, N_k + m_k - 1\}$ with $N_1 = 1$ and $N_{k+1} = N_k + m_k$.

2. For the negative frequencies, keep the standard basis (or also partition them, doesn't matter).

3. Within each block $B_k$, define the first new basis element as $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$, and the remaining $m_k - 1$ basis elements as any orthonormal completion (e.g., via Gram-Schmidt).

4. Order the new basis so that $w_1, (\text{rest of block 1}), w_2, (\text{rest of block 2}), \ldots$ — actually, we want $w_k$ to come first in each block, and the ordering of blocks is sequential.

Wait, but we need the partial sums to diverge. The partial sum up to $w_k$ (i.e., including all of blocks $1, \ldots, k-1$ and just $w_k$ from block $k$) is:

$$S_k = \sum_{j=1}^{k-1} P_j u + \langle u, w_k\rangle w_k$$

where $P_j u$ is the projection of $u$ onto block $B_j$ (which equals $\sum_{n \in B_j} a_n e_n$).

Now, $S_k = \sum_{n=1}^{N_k - 1} a_n e_n + \langle u, w_k\rangle w_k$ (the standard partial sum up to $N_k - 1$, plus the $w_k$ contribution).

Wait, that's not quite right. The partial sum up to $w_k$ includes all completed blocks (which give the standard partial sum up to $N_k - 1$) plus $w_k$ from the current block. But the standard partial sum up to $N_k - 1$ also includes the negative frequencies if we kept those standard. Let me simplify by only working with positive frequencies and setting negative frequency coefficients to zero.

Let me redefine: $u(x) = \sum_{n=1}^{\infty} a_n e_n(x) + \overline{a_n} \overline{e_n(x)}$... actually, let me just work with complex-valued functions for simplicity, or just use the one-sided basis.

Hmm, let me simplify. Let me use the orthonormal basis $\{e_n : n \in \mathbb{Z}\}$ of $L^2(S^1)$ where $e_n(x) = e^{inx}/\sqrt{2\pi}$. I'll construct a new orthonormal basis by modifying only the positive frequency part.

Let $u(x) = \sum_{n=1}^{\infty} a_n e_n(x)$ with $a_n = e^{-n^\alpha}$, $0 < \alpha < 1$. This is a smooth function (the negative frequency part is zero, which is fine).

Now, partition $\{1, 2, 3, \ldots\}$ into blocks $B_k = \{N_k, \ldots, N_k + m_k - 1\}$ with $N_1 = 1$, $N_{k+1} = N_k + m_k$.

For negative frequencies $\{..., -2, -1, 0\}$, keep the standard basis $e_n$.

For each block $B_k$ (positive frequencies), define:
- $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (first element of the rotated block)
- $v_{k,2}, \ldots, v_{k,m_k}$: orthonormal completion of $w_k$ in $\text{span}\{e_n : n \in B_k\}$.

The new orthonormal basis is: $\{e_n : n \leq 0\} \cup \{w_1, v_{1,2}, \ldots, v_{1,m_1}, w_2, v_{2,2}, \ldots\}$.

Order them as: $e_0, e_{-1}, e_{-2}, \ldots$ (but this is infinite; let me interleave). Actually, the ordering matters for the partial sums. Let me order the basis as:

$e_0, w_1, v_{1,2}, \ldots, v_{1,m_1}, w_2, v_{2,2}, \ldots, v_{2,m_2}, w_3, \ldots$

and put the negative frequency basis elements somewhere (they don't matter since $u$ has no negative frequency components, so $\langle u, e_{-n}\rangle = 0$).

Actually, to be careful, let me just include all negative frequency basis elements at the beginning. Since $\langle u, e_n\rangle = 0$ for $n \leq 0$, these contribute nothing to the partial sums of $u$'s expansion. So effectively, the partial sums of $u$ are determined by the positive frequency blocks.

The partial sum of $u$ up to and including $w_k$ (but not the rest of block $k$) is:

$$S_k = \sum_{j=1}^{k-1} \sum_{n \in B_j} a_n e_n + \langle u, w_k\rangle w_k$$

The first part is $\sum_{n=1}^{N_k - 1} a_n e_n = $ (standard Fourier partial sum of $u$ up to frequency $N_k - 1$).

The second part: $\langle u, w_k\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n = \frac{1}{\sqrt{m_k}} \sum_{n=N_k}^{N_k+m_k-1} e^{-n^\alpha}$.

And $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$.

So $\langle u, w_k\rangle w_k = \frac{1}{m_k} \left(\sum_{n \in B_k} a_n\right) \sum_{n \in B_k} e_n$.

The sup norm of this is $\frac{1}{m_k} \left|\sum_{n \in B_k} a_n\right| \cdot \left\|\sum_{n \in B_k} e_n\right\|_\infty$.

Now, $\left\|\sum_{n \in B_k} e_n\right\|_\infty = \frac{1}{\sqrt{2\pi}} \left\|\sum_{n=N_k}^{N_k+m_k-1} e^{inx}\right\|_\infty = \frac{m_k}{\sqrt{2\pi}}$ (the sup is achieved at $x = 0$).

So $\|\langle u, w_k\rangle w_k\|_\infty = \frac{1}{m_k} \left|\sum_{n \in B_k} a_n\right| \cdot \frac{m_k}{\sqrt{2\pi}} = \frac{1}{\sqrt{2\pi}} \left|\sum_{n \in B_k} a_n\right|$.

Now, $\sum_{n \in B_k} a_n = \sum_{n=N_k}^{N_k+m_k-1} e^{-n^\alpha}$. 

Since $e^{-n^\alpha}$ is decreasing, $\sum_{n=N_k}^{N_k+m_k-1} e^{-n^\alpha} \geq m_k \cdot e^{-(N_k+m_k-1)^\alpha}$.

Hmm, but also $\leq m_k \cdot e^{-N_k^\alpha}$.

So $\|\langle u, w_k\rangle w_k\|_\infty \geq \frac{m_k e^{-(N_k+m_k)^\alpha}}{\sqrt{2\pi}}$.

For this to go to infinity, we need $m_k e^{-(N_k+m_k)^\alpha} \to \infty$, i.e., $\log m_k > (N_k + m_k)^\alpha + O(1)$.

But we also need the standard partial sum $\sum_{n=1}^{N_k-1} a_n e_n$ to be bounded (which it is, since it converges to $u$ uniformly — wait, does it? The standard Fourier series of a smooth function converges uniformly. Yes, for smooth $u$, the standard Fourier series converges absolutely and uniformly.)

Actually, the standard Fourier series of $u$ converges uniformly to $u$. So $\sum_{n=1}^{N} a_n e_n \to u$ uniformly. In particular, $\left\|\sum_{n=1}^{N_k-1} a_n e_n\right\|_\infty \leq \|u\|_\infty + \epsilon_k$ where $\epsilon_k \to 0$.

So $\|S_k\|_\infty \geq \|\langle u, w_k\rangle w_k\|_\infty - \left\|\sum_{n=1}^{N_k-1} a_n e_n\right\|_\infty \geq \frac{m_k e^{-(N_k+m_k)^\alpha}}{\sqrt{2\pi}} - (\|u\|_\infty + 1)$.

If we can make $m_k e^{-(N_k+m_k)^\alpha} \to \infty$, then $\|S_k\|_\infty \to \infty$, and the series doesn't converge uniformly (in fact, the partial sums are unbounded).

So the question reduces to: can we choose blocks (i.e., $N_k$ and $m_k$) such that $m_k e^{-(N_k + m_k)^\alpha} \to \infty$?

This requires $\log m_k > (N_k + m_k)^\alpha$, i.e., $m_k > e^{(N_k + m_k)^\alpha}$.

But if $m_k > e^{(N_k + m_k)^\alpha}$, then $m_k > e^{m_k^\alpha}$ (since $N_k + m_k > m_k$). For large $m_k$, $e^{m_k^\alpha} \gg m_k$ when $\alpha > 0$. So $m_k > e^{m_k^\alpha}$ is impossible for large $m_k$.

Hmm, so this approach doesn't directly work because the block size $m_k$ appears in the exponent too.

Let me reconsider. The issue is that $\sum_{n \in B_k} a_n \leq m_k a_{N_k} = m_k e^{-N_k^\alpha}$, but also $\sum_{n \in B_k} a_n \geq m_k a_{N_k + m_k} = m_k e^{-(N_k+m_k)^\alpha}$.

The sup norm of the contribution is $\frac{1}{\sqrt{2\pi}} |\sum_{n \in B_k} a_n|$, which is at most $\frac{m_k e^{-N_k^\alpha}}{\sqrt{2\pi}}$.

For this to diverge, we need $m_k e^{-N_k^\alpha} \to \infty$, i.e., $m_k \gg e^{N_k^\alpha}$.

And we need $N_{k+1} = N_k + m_k$, so $N_{k+1} \approx m_k$ (if $m_k \gg N_k$).

So let's try: $m_k = \lceil e^{N_k^\alpha} \cdot k \rceil$ (growing faster than $e^{N_k^\alpha}$). Then $N_{k+1} = N_k + m_k \approx e^{N_k^\alpha} \cdot k$.

The sup norm of the $w_k$ contribution is $\sim \frac{m_k e^{-N_k^\alpha}}{\sqrt{2\pi}} \sim \frac{k}{\sqrt{2\pi}} \to \infty$. 

But wait, I need to check that $\sum_{n \in B_k} a_n \approx m_k e^{-N_k^\alpha}$, which requires that $a_n$ doesn't vary too much over the block. Since $a_n = e^{-n^\alpha}$ and the block goes from $N_k$ to $N_k + m_k - 1$, the ratio $a_{N_k + m_k}/a_{N_k} = e^{-(N_k+m_k)^\alpha + N_k^\alpha}$. 

$(N_k + m_k)^\alpha - N_k^\alpha = N_k^\alpha [(1 + m_k/N_k)^\alpha - 1] \approx N_k^\alpha \cdot \alpha \cdot m_k/N_k = \alpha m_k N_k^{\alpha - 1}$ for $m_k \ll N_k$.

But in our case, $m_k \gg N_k$ (since $m_k \sim e^{N_k^\alpha} \cdot k$ and $N_k$ grows), so $(N_k + m_k)^\alpha \approx m_k^\alpha$.

So $a_{N_k + m_k}/a_{N_k} = e^{-m_k^\alpha + N_k^\alpha}$. Since $m_k \sim e^{N_k^\alpha} k$, we have $m_k^\alpha \sim e^{\alpha N_k^\alpha} k^\alpha$, which is much larger than $N_k^\alpha$. So $a_{N_k + m_k}/a_{N_k} \approx e^{-m_k^\alpha} \to 0$ very fast.

This means most of the sum $\sum_{n \in B_k} a_n$ comes from the first few terms (near $N_k$), and the sum is approximately $\sum_{n=N_k}^{\infty} e^{-n^\alpha} \approx \int_{N_k}^{\infty} e^{-x^\alpha} dx$.

For large $N_k$, $\int_{N_k}^{\infty} e^{-x^\alpha} dx \sim \frac{1}{\alpha} N_k^{1-\alpha} e^{-N_k^\alpha}$ (by Laplace's method / integration by parts).

So $\sum_{n \in B_k} a_n \approx \sum_{n=N_k}^{\infty} e^{-n^\alpha} \approx C N_k^{1-\alpha} e^{-N_k^\alpha}$ (since the block is so large that it captures essentially all the remaining mass).

Wait, but that means $\sum_{n \in B_k} a_n \approx C N_k^{1-\alpha} e^{-N_k^\alpha}$, which goes to 0 as $N_k \to \infty$ (since $e^{-N_k^\alpha}$ dominates). So the sup norm of the $w_k$ contribution goes to 0, not infinity!

The problem is that when the block is too large, the sum $\sum_{n \in B_k} a_n$ is essentially the tail sum, which goes to 0.

So there's a tension: we need $m_k$ large enough that $m_k e^{-N_k^\alpha}$ is large, but if $m_k$ is too large, the sum saturates at the tail sum which is $\sim N_k^{1-\alpha} e^{-N_k^\alpha}$, which goes to 0.

The optimal $m_k$ is where $a_{N_k + m_k} \approx a_{N_k} / 2$, i.e., $(N_k + m_k)^\alpha - N_k^\alpha \approx \log 2$. For large $N_k$, this gives $m_k \approx \frac{N_k^{1-\alpha}}{\alpha} \log 2$. With this $m_k$, $\sum_{n \in B_k} a_n \approx m_k e^{-N_k^\alpha} \approx C N_k^{1-\alpha} e^{-N_k^\alpha}$, which still goes to 0.

So with $a_n = e^{-n^\alpha}$, the sup norm of the $w_k$ contribution is $\sim N_k^{1-\alpha} e^{-N_k^\alpha} \to 0$. This doesn't diverge.

The fundamental issue is that for a smooth function, the coefficients decay faster than any polynomial, so the "mass" in any block at high frequencies is small, and we can't make the partial sums diverge this way.

Let me reconsider the problem. Maybe I need a different approach.

Actually, wait. Let me reconsider. The issue is that I was trying to make the partial sums diverge to infinity. But for uniform convergence to fail, I just need the partial sums to not converge uniformly, which could mean they oscillate or fail to be Cauchy in sup norm.

But actually, if the partial sums are unbounded, that's the strongest way to fail uniform convergence.

Let me think about this differently. Maybe I should not use the "flat" vector $w_k = \frac{1}{\sqrt{m_k}} \sum e_n$ but instead use a different vector in the block.

The key quantity is: for a unit vector $v$ in the span of $\{e_n : n \in B_k\}$, what is $|\langle u, v\rangle| \|v\|_\infty$?

We have $|\langle u, v\rangle| \leq \|P_k u\|_{L^2} = \rho_k$ (the $L^2$ norm of the projection of $u$ onto the block). And $\|v\|_\infty$ can be as large as $\sqrt{m_k}/\sqrt{2\pi}$ (for the flat vector).

But actually, we can do better. We can choose $v$ to maximize $|\langle u, v\rangle| \|v\|_\infty$ subject to $\|v\|_{L^2} = 1$ and $v \in \text{span}\{e_n : n \in B_k\}$.

Hmm, but $|\langle u, v\rangle| \leq \rho_k$ and $\|v\|_\infty \leq \sqrt{m_k}/\sqrt{2\pi}$, so the product is at most $\rho_k \sqrt{m_k}/\sqrt{2\pi}$.

Now, $\rho_k^2 = \sum_{n \in B_k} |a_n|^2$. For $a_n = e^{-n^\alpha}$ and a block at $N_k$ with size $m_k$, $\rho_k^2 \approx m_k e^{-2N_k^\alpha}$ (if $m_k$ is not too large). So $\rho_k \approx \sqrt{m_k} e^{-N_k^\alpha}$.

The product is $\rho_k \sqrt{m_k}/\sqrt{2\pi} \approx m_k e^{-N_k^\alpha}/\sqrt{2\pi}$.

But we need $v$ to simultaneously have $\langle u, v\rangle \approx \rho_k$ and $\|v\|_\infty \approx \sqrt{m_k}/\sqrt{2\pi}$. The vector that maximizes $\langle u, v\rangle$ is $v = P_k u / \rho_k$, which has $\|v\|_\infty = \|P_k u\|_\infty / \rho_k$. And the vector that maximizes $\|v\|_\infty$ is the flat vector, which has $\langle u, v\rangle = \frac{1}{\sqrt{m_k}} \sum a_n$.

These are generally different vectors, so we can't simultaneously achieve both maxima. But we can try to find a vector that does well on both.

Actually, let me think about this more carefully. The maximum of $|\langle u, v\rangle| \|v\|_\infty$ over unit vectors $v$ in the block is a well-defined optimization problem. Let me think about what happens.

Write $v = \sum_{n \in B_k} c_n e_n$ with $\sum |c_n|^2 = 1$. Then $\langle u, v\rangle = \sum_{n \in B_k} a_n \overline{c_n}$ and $\|v\|_\infty = \sup_x |\sum_{n \in B_k} c_n e_n(x)|/\sqrt{2\pi}$... wait, $\|v\|_\infty = \sup_x |\sum c_n e^{inx}/\sqrt{2\pi}| = \frac{1}{\sqrt{2\pi}} \sup_x |\sum c_n e^{inx}|$.

Hmm, this is getting complicated. Let me try a completely different approach.

Alternative approach: Instead of trying to make the partial sums diverge, let me think about whether the answer to the question is yes or no.

I recall that there's a classical result that for any orthonormal basis of $L^2$, the Fourier series of an $L^2$ function converges in $L^2$. But uniform convergence is not guaranteed.

In fact, I believe the answer is YES — such a smooth function and orthonormal basis exist. This is related to the fact that there's no orthonormal basis that's an "unconditional basis" for $C(S^1)$ (or for the space of smooth functions with uniform norm).

Actually, let me think about this more carefully. The question is asking about a specific $u$ and a specific basis, not about all $u$ for a given basis.

Let me think about the problem from the perspective of functional analysis.

The partial sum operator $S_N: L^2 \to L^2$ is the orthogonal projection onto $\text{span}\{u_1, \ldots, u_N\}$. For uniform convergence of the series for a specific $u$, we need $S_N u \to u$ in $L^\infty$.

The operator norm $\|S_N\|_{L^\infty \to L^\infty}$ can be large. If we can find a basis where $\|S_N\|_{L^\infty \to L^\infty}$ is unbounded, then by the uniform boundedness principle, there exists $u \in C(S^1)$ (even smooth, since smooth functions are dense) such that $S_N u$ doesn't converge in $L^\infty$.

Wait, but the uniform boundedness principle gives us $u \in C(S^1)$, not necessarily smooth. However, since smooth functions are dense in $C(S^1)$, and the operators $S_N$ are continuous on $C(S^1)$ (are they? $S_N$ is a finite-rank operator, so it's continuous on any normed space), we can potentially find a smooth $u$.

Actually, let me think about this more carefully. The uniform boundedness principle says: if $\sup_N \|S_N\|_{X \to X} = \infty$ for a Banach space $X$, then there exists $u \in X$ such that $\sup_N \|S_N u\|_X = \infty$.

If $X = C(S^1)$ (continuous functions with sup norm), and $\sup_N \|S_N\|_{C \to C} = \infty$, then there exists $u \in C(S^1)$ with $\sup_N \|S_N u\|_\infty = \infty$, so the series doesn't converge uniformly.

But we need $u$ to be smooth. The issue is that the UBP gives us $u \in C(S^1)$, not smooth.

However, we can use a stronger argument. If the operators $S_N$ are unbounded on $C(S^1)$, we can find a smooth $u$ as follows:

Consider the restriction of $S_N$ to $C^\infty(S^1)$. The space $C^\infty(S^1)$ with the sup norm is not complete (its completion is $C(S^1)$), but we can still apply a version of the UBP argument.

Actually, a cleaner approach: $C^\infty(S^1)$ is a Fréchet space (with the topology of uniform convergence of all derivatives). The operators $S_N$ are continuous on this Fréchet space. If $\sup_N \|S_N u\|_\infty < \infty$ for all smooth $u$, then by the uniform boundedness principle for Fréchet spaces, $\sup_N \|S_N\|_{C^\infty \to L^\infty} < \infty$ (where the operator norm is with respect to some continuous seminorm on $C^\infty$). 

Hmm, this is getting into functional analysis territory. Let me think about whether there's a more direct construction.

Actually, let me reconsider the direct construction approach, but with a better choice of $u$ and basis.

The key issue before was that for a smooth function, the coefficients decay too fast. But what if I choose the blocks to be at LOW frequencies, not high frequencies?

Wait, but there are only finitely many low frequencies. The blocks need to cover all positive integers, so most blocks are at high frequencies.

Let me reconsider. Maybe I should use a different type of basis element, not just rotations within frequency blocks.

Actually, here's another idea. What if the orthonormal basis is not related to the Fourier basis at all? We can take any complete orthonormal system of smooth functions.

Let me think about the following construction. Take a sequence of smooth functions $\phi_1, \phi_2, \ldots$ that are orthonormal in $L^2$ and have $\|\phi_n\|_\infty \to \infty$. Then for $u = \phi_1$ (say), the Fourier series is $u = \sum \langle u, \phi_n\rangle \phi_n = \|\phi_1\|_{L^2}^2 \phi_1 / \|\phi_1\|_{L^2}^2$... wait, if $\phi_1$ is already normalized, then $\langle u, \phi_1\rangle = 1$ and $\langle u, \phi_n\rangle = 0$ for $n > 1$. So the series is just $\phi_1$, which converges trivially.

That doesn't work because $u$ being a basis element means the series terminates.

Let me think about this differently. I want $u$ to have nonzero inner products with many basis elements, and the partial sums to be large.

Here's an idea based on the "gliding hump" or "sliding hump" technique:

Construct the orthonormal basis $\{u_n\}$ and the function $u$ simultaneously, inductively. At each step, ensure that a partial sum is large.

Let me think about this more carefully.

Actually, let me go back to the block rotation approach but think about it differently.

The issue was that for a smooth function with coefficients $a_n = e^{-n^\alpha}$, the "mass" $\rho_k$ in a block at frequency $N_k$ is too small. But what if I choose $u$ to have coefficients that don't decay as a function of $n$, but instead have the mass concentrated in specific blocks?

Wait, but $u$ needs to be smooth, so $a_n$ must decay faster than any polynomial. However, I can choose which frequencies have large coefficients and which have small ones, as long as the overall decay is faster than polynomial.

Here's the key idea: Choose $u$ such that its coefficients are large at the frequencies $N_k$ (the start of each block) and small elsewhere. Specifically, let $a_{N_k} = 1/k^2$ (or some slowly decaying sequence) and $a_n = 0$ for $n \neq N_k$ (or very small). But wait, $a_n$ needs to decay faster than any polynomial in $n$ for $u$ to be smooth. If $a_{N_k} = 1/k^2$ and $N_k$ grows very fast, then $a_{N_k} = 1/k^2$ needs to be $o(N_k^{-p})$ for all $p$, i.e., $k^2 \gg N_k^p$ for all $p$, i.e., $N_k \ll k^{2/p}$ for all $p$, which means $N_k$ must be bounded. Contradiction.

So I can't have $a_{N_k}$ decaying only polynomially in $k$ if $N_k \to \infty$.

OK so the constraint is: $a_n$ must decay faster than any polynomial in $n$. If I want $a_{N_k}$ to be "large", I need $N_k$ to be not too large relative to $a_{N_k}$.

Let me try $a_{N_k} = e^{-\sqrt{N_k}}$ (which is faster than any polynomial decay). Then $u$ is smooth (since $e^{-\sqrt{n}}$ decays faster than any polynomial). And I want the partial sums to diverge.

With the block approach, the sup norm of the $w_k$ contribution is $\sim \frac{1}{\sqrt{2\pi}} |\sum_{n \in B_k} a_n|$. If $a_n$ is concentrated at $N_k$ (i.e., $a_n \approx 0$ for $n \in B_k \setminus \{N_k\}$), then $\sum_{n \in B_k} a_n \approx a_{N_k} = e^{-\sqrt{N_k}}$, which goes to 0.

So the sup norm goes to 0, and the partial sums converge. Not helpful.

Hmm. It seems like for any smooth function, the coefficients decay too fast for the block approach to work.

Let me reconsider. Maybe the answer is NO — for any orthonormal basis of smooth functions and any smooth $u$, the generalized Fourier series converges uniformly?

That doesn't sound right either. Let me think about what's known.

Actually, I think the answer is YES, such a function and basis exist. Let me think about why.

The key insight might be that we should not restrict to bases that are "frequency-organized." We can use an arbitrary orthonormal basis of smooth functions.

Here's a different approach. Consider the following:

Let $\{e_n\}$ be the standard Fourier basis. Define a new orthonormal basis by applying a unitary operator $U$ on $L^2(S^1)$ that maps smooth functions to smooth functions but doesn't preserve uniform convergence of Fourier series.

If $U$ is a unitary operator that preserves $C^\infty(S^1)$ (i.e., $U$ and $U^{-1}$ map smooth functions to smooth functions), then $\{Ue_n\}$ is an orthonormal basis of smooth functions. The generalized Fourier series of $u$ in this basis is $\sum \langle u, Ue_n\rangle Ue_n = U \sum \langle U^{-1}u, e_n\rangle e_n = U(S_N^{std}(U^{-1}u))$ where $S_N^{std}$ is the standard Fourier partial sum.

So the partial sums in the new basis are $U(S_N^{std}(U^{-1}u))$. For this to converge uniformly to $u = U(U^{-1}u)$, we need $S_N^{std}(U^{-1}u) \to U^{-1}u$ uniformly AND $U$ to be continuous in sup norm.

If $U$ is not continuous in sup norm (i.e., $\|U\|_{L^\infty \to L^\infty} = \infty$), then even though $S_N^{std}(U^{-1}u) \to U^{-1}u$ uniformly (since $U^{-1}u$ is smooth), the images $U(S_N^{std}(U^{-1}u))$ might not converge uniformly.

But wait, $S_N^{std}(U^{-1}u) \to U^{-1}u$ uniformly means $\|S_N^{std}(U^{-1}u) - U^{-1}u\|_\infty \to 0$. Then $U(S_N^{std}(U^{-1}u)) - U(U^{-1}u) = U(S_N^{std}(U^{-1}u) - U^{-1}u)$. If $U$ is unbounded on $L^\infty$, the norm $\|U(S_N^{std}(U^{-1}u) - U^{-1}u)\|_\infty$ might not go to 0 even though $\|S_N^{std}(U^{-1}u) - U^{-1}u\|_\infty \to 0$.

But this requires that $U^{-1}u - S_N^{std}(U^{-1}u)$ is not in the kernel of $U$'s "blow-up" and that $U$ amplifies these specific errors.

This is getting abstract. Let me think of a concrete unitary operator.

Hmm, actually, a unitary operator on $L^2$ that preserves smooth functions but is unbounded on $L^\infty$... 

One example: a "permutation" of the Fourier basis that doesn't respect frequency. But a permutation of basis elements is unitary and preserves smoothness (since each basis element is smooth, and the permuted basis is still a basis of smooth functions). But a permutation doesn't change the partial sums in a useful way — it just reorders them.

Wait, actually, a permutation of the Fourier basis DOES change the partial sums! The standard Fourier partial sum $S_N$ projects onto the first $N$ frequencies, but a permuted basis projects onto an arbitrary set of $N$ frequencies.

But for a smooth function, the standard Fourier series converges absolutely ($\sum |a_n| < \infty$), so any rearrangement also converges absolutely and uniformly. So permutations don't help.

OK so the issue is that for smooth functions, the standard Fourier series converges absolutely, which makes it robust under rearrangements. We need something more drastic than permutation.

Let me go back to the block rotation idea, but think about it more carefully.

The block rotation changes the partial sums WITHIN a block. The partial sum at the end of a block is the same as the standard Fourier partial sum (projection onto the block's span is invariant). But intermediate partial sums within a block can be different.

For a smooth function, the standard Fourier series converges absolutely and uniformly. The partial sums at block boundaries converge uniformly to $u$. The question is whether the intermediate partial sums (within blocks) can diverge.

The intermediate partial sum within block $B_k$ after including $J$ of the $m_k$ rotated basis elements is:

$$S = \text{(standard partial sum up to } N_k - 1) + \sum_{j=1}^{J} \langle u, v_{k,j}\rangle v_{k,j}$$

where $v_{k,1}, \ldots, v_{k,m_k}$ is the rotated basis for block $B_k$.

The "error" from the standard partial sum at the end of the block is:

$$\sum_{j=1}^{J} \langle u, v_{k,j}\rangle v_{k,j} - P_k u = -\sum_{j=J+1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}$$

So the intermediate partial sum equals the standard partial sum at the end of the block minus the "remaining" terms. The sup norm of the remaining terms is $\|\sum_{j=J+1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}\|_\infty$.

This is the projection of $P_k u$ onto the span of $\{v_{k,J+1}, \ldots, v_{k,m_k}\}$, which is a subspace of dimension $m_k - J$ within the block.

The maximum sup norm of such a projection (over all choices of subspace and $J$) is bounded by $\|P_k u\|_\infty \cdot$ (some factor related to the basis).

Hmm, actually, the projection of $P_k u$ onto any subspace of the block has $L^2$ norm at most $\|P_k u\|_{L^2} = \rho_k$. And the sup norm is at most $\sqrt{m_k} \rho_k / \sqrt{2\pi}$ (by Cauchy-Schwarz, since any unit vector in the block has sup norm at most $\sqrt{m_k}/\sqrt{2\pi}$).

Wait, more precisely: the projection $Q$ of $P_k u$ onto a $d$-dimensional subspace is $Q = \sum_{j \in J} \langle u, v_j\rangle v_j$ where $|J| = d$. We have $\|Q\|_{L^2} \leq \rho_k$ and $Q$ is a trigonometric polynomial of degree $\leq N_k + m_k$. So $\|Q\|_\infty \leq \sqrt{m_k} \|Q\|_{L^2} / \sqrt{2\pi} \leq \sqrt{m_k} \rho_k / \sqrt{2\pi}$... 

Hmm wait, that's not right. $Q$ is in the span of $m_k$ basis elements (the block), so $\|Q\|_\infty \leq \sqrt{m_k} \|Q\|_{L^2}$... no, that's not right either. The correct bound is: if $Q = \sum_{n \in B_k} c_n e_n$, then $\|Q\|_\infty \leq \sum |c_n| \|e_n\|_\infty = \frac{1}{\sqrt{2\pi}} \sum |c_n| \leq \frac{\sqrt{m_k}}{\sqrt{2\pi}} (\sum |c_n|^2)^{1/2} = \frac{\sqrt{m_k}}{\sqrt{2\pi}} \|Q\|_{L^2}$.

So $\|Q\|_\infty \leq \frac{\sqrt{m_k}}{\sqrt{2\pi}} \rho_k$.

Now, $\rho_k = (\sum_{n \in B_k} |a_n|^2)^{1/2}$. For a smooth function, $|a_n| \leq C_p n^{-p}$ for all $p$. If the block is at frequency $N_k$ with size $m_k$, then $\rho_k \leq C_p m_k^{1/2} N_k^{-p}$.

So $\|Q\|_\infty \leq \frac{m_k}{\sqrt{2\pi}} C_p N_k^{-p}$.

For this to diverge, we need $m_k N_k^{-p} \to \infty$ for some fixed $p$. But since $u$ is smooth, this must hold for ALL $p$, so we need $m_k N_k^{-p} \to \infty$ for all $p$, i.e., $m_k \gg N_k^p$ for all $p$, i.e., $m_k$ grows faster than any polynomial in $N_k$.

But $N_{k+1} = N_k + m_k$, so if $m_k \gg N_k^p$ for all $p$, then $N_{k+1} \approx m_k \gg N_k^p$ for all $p$, meaning $N_k$ grows faster than any iterated exponential. This is fine in principle — there's no constraint on how fast $N_k$ grows.

But we also need $u$ to be in $L^2$, i.e., $\sum |a_n|^2 < \infty$. And $u$ smooth, i.e., $\sum n^{2p} |a_n|^2 < \infty$ for all $p$.

If $a_n \leq C_p n^{-p}$ for all $p$, and the blocks are at $N_k$ with $N_k$ growing super fast, then the contribution of block $B_k$ to $\sum n^{2p} |a_n|^2$ is $\sum_{n \in B_k} n^{2p} |a_n|^2 \leq m_k (N_k + m_k)^{2p} C_p^2 (N_k)^{-2q}$ for any $q$ (using $|a_n| \leq C_q n^{-q}$).

Hmm, this is getting complicated. Let me try to be very concrete.

Let me choose $u$ with $a_n = e^{-\sqrt{n}}$ (for $n \geq 1$). This is smooth (decays faster than any polynomial). And $\sum |a_n|^2 = \sum e^{-2\sqrt{n}} < \infty$ (converges since $e^{-2\sqrt{n}}$ decays faster than $1/n^2$).

Now, $\rho_k = (\sum_{n \in B_k} e^{-2\sqrt{n}})^{1/2}$. For a block at $N_k$ with size $m_k$ (where $m_k \ll N_k$ so that $\sqrt{n} \approx \sqrt{N_k}$ for $n \in B_k$), $\rho_k \approx \sqrt{m_k} e^{-\sqrt{N_k}}$.

The sup norm of the "remaining" projection is at most $\frac{\sqrt{m_k}}{\sqrt{2\pi}} \rho_k \approx \frac{m_k e^{-\sqrt{N_k}}}{\sqrt{2\pi}}$.

For this to diverge, we need $m_k e^{-\sqrt{N_k}} \to \infty$, i.e., $\log m_k > \sqrt{N_k}$, i.e., $m_k > e^{\sqrt{N_k}}$.

But we also need $m_k \ll N_k$ for the approximation $\sqrt{n} \approx \sqrt{N_k}$. This requires $e^{\sqrt{N_k}} \ll N_k$, which is false for large $N_k$.

If $m_k \sim e^{\sqrt{N_k}}$, then for $n$ near $N_k + m_k$, $\sqrt{n} \approx \sqrt{m_k} = e^{\sqrt{N_k}/2}$, so $a_n \approx e^{-e^{\sqrt{N_k}/2}}$, which is tiny. The sum $\sum_{n \in B_k} e^{-2\sqrt{n}}$ is dominated by the terms near $N_k$:

$\sum_{n=N_k}^{N_k+m_k-1} e^{-2\sqrt{n}} \approx \sum_{n=N_k}^{\infty} e^{-2\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-2\sqrt{x}} dx = \int_{\sqrt{N_k}}^{\infty} 2t e^{-2t} dt \approx \sqrt{N_k} e^{-2\sqrt{N_k}}$ (by integration by parts).

So $\rho_k \approx N_k^{1/4} e^{-\sqrt{N_k}}$.

And the sup norm bound is $\frac{\sqrt{m_k}}{\sqrt{2\pi}} \rho_k \approx \frac{e^{\sqrt{N_k}/2}}{\sqrt{2\pi}} N_k^{1/4} e^{-\sqrt{N_k}} = \frac{N_k^{1/4} e^{-\sqrt{N_k}/2}}{\sqrt{2\pi}} \to 0$.

So even with $m_k \sim e^{\sqrt{N_k}}$, the sup norm goes to 0. The problem is that the $L^2$ mass $\rho_k$ decays as $e^{-\sqrt{N_k}}$, and even though we can amplify by $\sqrt{m_k} \sim e^{\sqrt{N_k}/2}$, the product still decays.

The fundamental issue: $\rho_k \sim e^{-\sqrt{N_k}}$ and the amplification factor is $\sqrt{m_k}$, but $m_k$ can't be larger than $\sim e^{2\sqrt{N_k}}$ (because beyond that, the block captures all remaining mass and $\rho_k$ saturates). At $m_k \sim e^{2\sqrt{N_k}}$, $\rho_k \sim N_k^{1/4} e^{-\sqrt{N_k}}$ and amplification $\sim e^{\sqrt{N_k}}$, giving product $\sim N_k^{1/4}$, which diverges!

Wait, let me recheck. If $m_k \sim e^{2\sqrt{N_k}}$, then the block goes from $N_k$ to $N_k + e^{2\sqrt{N_k}}$. For $n$ near the end of the block, $\sqrt{n} \approx \sqrt{e^{2\sqrt{N_k}}} = e^{\sqrt{N_k}}$, so $a_n \approx e^{-e^{\sqrt{N_k}}}$, which is super tiny. So the sum $\sum_{n \in B_k} e^{-2\sqrt{n}}$ is still dominated by terms near $N_k$:

$\sum_{n=N_k}^{N_k + m_k} e^{-2\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-2\sqrt{x}} dx \approx \sqrt{N_k} e^{-2\sqrt{N_k}}$.

So $\rho_k \approx N_k^{1/4} e^{-\sqrt{N_k}}$.

And $\sqrt{m_k} \approx e^{\sqrt{N_k}}$.

Product: $\sqrt{m_k} \rho_k \approx e^{\sqrt{N_k}} \cdot N_k^{1/4} e^{-\sqrt{N_k}} = N_k^{1/4} \to \infty$.

So the sup norm of the "remaining" projection can be as large as $\sim N_k^{1/4} / \sqrt{2\pi} \to \infty$!

But wait, this is an upper bound. Can we actually achieve this? The bound $\|Q\|_\infty \leq \frac{\sqrt{m_k}}{\sqrt{2\pi}} \|Q\|_{L^2}$ is achieved when $Q$ is proportional to the flat vector $\sum_{n \in B_k} e_n$. But $Q$ is a projection of $P_k u$, so $Q$ is determined by the choice of subspace.

Let me think about this. We want to choose a subspace $V \subset \text{span}\{e_n : n \in B_k\}$ such that the projection of $P_k u$ onto $V$ has large sup norm.

$P_k u = \sum_{n \in B_k} a_n e_n$ where $a_n = e^{-\sqrt{n}}$. The mass is concentrated near $n = N_k$ (since $a_n$ decays). So $P_k u \approx a_{N_k} \sum_{j=0}^{J} e^{-(\sqrt{N_k+j} - \sqrt{N_k})} e_{N_k+j}$ where $J$ is such that $\sqrt{N_k + J} - \sqrt{N_k} \sim 1$, i.e., $J \sim \sqrt{N_k}$.

So $P_k u$ is essentially supported on $\sim \sqrt{N_k}$ basis elements near $N_k$, with $L^2$ norm $\rho_k \sim N_k^{1/4} e^{-\sqrt{N_k}}$.

Now, the flat vector $w = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ has $\|w\|_\infty = \frac{\sqrt{m_k}}{\sqrt{2\pi}} \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2\pi}}$. The projection of $P_k u$ onto $w$ is $\langle P_k u, w\rangle w = \frac{1}{\sqrt{m_k}} (\sum_{n \in B_k} a_n) w$.

$\sum_{n \in B_k} a_n \approx \sum_{n=N_k}^{\infty} e^{-\sqrt{n}} \approx \sqrt{N_k} e^{-\sqrt{N_k}}$ (similar calculation).

So $\langle P_k u, w\rangle = \frac{\sqrt{N_k} e^{-\sqrt{N_k}}}{\sqrt{m_k}} \approx \frac{\sqrt{N_k} e^{-\sqrt{N_k}}}{e^{\sqrt{N_k}}} = \sqrt{N_k} e^{-2\sqrt{N_k}}$.

And $\|\langle P_k u, w\rangle w\|_\infty = |\langle P_k u, w\rangle| \|w\|_\infty \approx \sqrt{N_k} e^{-2\sqrt{N_k}} \cdot e^{\sqrt{N_k}} / \sqrt{2\pi} = \sqrt{N_k} e^{-\sqrt{N_k}} / \sqrt{2\pi} \to 0$.

So projecting onto the flat vector doesn't work because $\langle P_k u, w\rangle$ is too small (the flat vector has components at all frequencies in the block, but $P_k u$ is concentrated near $N_k$).

Instead, I should project onto a subspace that aligns with $P_k u$ but has large sup norm. 

The optimal strategy: choose $v$ to be a unit vector in the block that maximizes $|\langle P_k u, v\rangle| \|v\|_\infty$.

$P_k u$ is concentrated on $\sim \sqrt{N_k}$ basis elements near $N_k$. Let's say $P_k u \approx \rho_k \cdot \psi$ where $\psi$ is a unit vector supported on $\sim \sqrt{N_k}$ basis elements. Then $\|P_k u\|_\infty \approx \rho_k \|\psi\|_\infty \approx N_k^{1/4} e^{-\sqrt{N_k}} \cdot \frac{\sqrt{\sqrt{N_k}}}{\sqrt{2\pi}} = \frac{N_k^{1/2} e^{-\sqrt{N_k}}}{\sqrt{2\pi}}$ (since $\psi$ is supported on $\sqrt{N_k}$ basis elements, its sup norm is $\sim N_k^{1/4}/\sqrt{2\pi}$).

Now, I want to find a unit vector $v$ in the full block (of size $m_k \sim e^{2\sqrt{N_k}}$) such that $|\langle P_k u, v\rangle| \|v\|_\infty$ is large.

$|\langle P_k u, v\rangle| = \rho_k |\langle \psi, v\rangle| \leq \rho_k$ (since $\|v\| = 1$). Equality when $v = \psi$, but then $\|v\|_\infty = \|\psi\|_\infty \sim N_k^{1/4}/\sqrt{2\pi}$, giving product $\sim \rho_k N_k^{1/4} = N_k^{1/2} e^{-\sqrt{N_k}} \to 0$.

Alternatively, $v$ could be the flat vector, giving $|\langle \psi, v\rangle| \sim \sqrt{\sqrt{N_k}/m_k} = N_k^{1/4}/e^{\sqrt{N_k}}$ and $\|v\|_\infty \sim e^{\sqrt{N_k}}/\sqrt{2\pi}$, product $\sim \rho_k \cdot N_k^{1/4}/e^{\sqrt{N_k}} \cdot e^{\sqrt{N_k}} = \rho_k N_k^{1/4} = N_k^{1/2} e^{-\sqrt{N_k}} \to 0$.

Hmm, in both cases the product goes to 0. The issue is that $\rho_k \sim N_k^{1/4} e^{-\sqrt{N_k}}$ decays too fast.

Let me try to optimize. We want to maximize $|\langle P_k u, v\rangle| \|v\|_\infty$ over unit vectors $v$ in the block. 

Write $v = \alpha \psi + \beta \phi$ where $\psi = P_k u / \rho_k$ (the "signal" direction) and $\phi$ is a unit vector orthogonal to $\psi$ in the block. Then $|\langle P_k u, v\rangle| = \rho_k |\alpha|$ and $\|v\|_\infty \leq |\alpha| \|\psi\|_\infty + |\beta| \|\phi\|_\infty$ (by triangle inequality).

With $|\alpha|^2 + |\beta|^2 = 1$, and $\|\phi\|_\infty \leq \sqrt{m_k}/\sqrt{2\pi}$ (max sup norm in the block), we get:

$|\langle P_k u, v\rangle| \|v\|_\infty \leq \rho_k |\alpha| (|\alpha| \|\psi\|_\infty + |\beta| \sqrt{m_k}/\sqrt{2\pi})$.

This is maximized (roughly) when $|\alpha| \sim \rho_k \|\psi\|_\infty / (\rho_k \|\psi\|_\infty + \rho_k \sqrt{m_k}/\sqrt{2\pi})$... hmm, let me just optimize.

Let $A = \|\psi\|_\infty \sim N_k^{1/4}/\sqrt{2\pi}$ and $B = \sqrt{m_k}/\sqrt{2\pi} \sim e^{\sqrt{N_k}}/\sqrt{2\pi}$.

We want to maximize $f(\alpha, \beta) = \rho_k |\alpha| (|\alpha| A + |\beta| B)$ subject to $\alpha^2 + \beta^2 = 1$.

Let $\alpha = \cos\theta$, $\beta = \sin\theta$. Then $f = \rho_k \cos\theta (\cos\theta \cdot A + \sin\theta \cdot B)$.

$\frac{df}{d\theta} = \rho_k [-\sin\theta(\cos\theta \cdot A + \sin\theta \cdot B) + \cos\theta(-\sin\theta \cdot A + \cos\theta \cdot B)]$
$= \rho_k [-\sin\theta\cos\theta A - \sin^2\theta B - \sin\theta\cos\theta A + \cos^2\theta B]$
$= \rho_k [-2\sin\theta\cos\theta A + (\cos^2\theta - \sin^2\theta) B]$
$= \rho_k [-\sin 2\theta \cdot A + \cos 2\theta \cdot B]$

Setting to 0: $\tan 2\theta = B/A$, so $2\theta \approx \pi/2$ (since $B \gg A$), $\theta \approx \pi/4$, $\alpha \approx \beta \approx 1/\sqrt{2}$.

Then $f \approx \rho_k \cdot \frac{1}{\sqrt{2}} \cdot (\frac{A}{\sqrt{2}} + \frac{B}{\sqrt{2}}) \approx \rho_k \cdot \frac{B}{2} \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}} \cdot e^{\sqrt{N_k}}}{2\sqrt{2\pi}} = \frac{N_k^{1/4}}{2\sqrt{2\pi}}$.

This diverges! So the maximum of $|\langle P_k u, v\rangle| \|v\|_\infty$ is $\sim N_k^{1/4} \to \infty$.

But wait, this is an upper bound using the triangle inequality. The actual sup norm of $v = \alpha\psi + \beta\phi$ might be less than $|\alpha| \|\psi\|_\infty + |\beta| \|\phi\|_\infty$ due to cancellation. Let me think about whether we can actually achieve this.

We need $\phi$ to be a unit vector orthogonal to $\psi$ with $\|\phi\|_\infty \sim \sqrt{m_k}/\sqrt{2\pi}$ and such that $\psi$ and $\phi$ achieve their sup norms at the same point (or nearly so).

$\psi$ is supported on $\sim \sqrt{N_k}$ basis elements near $N_k$ and has sup norm at $x = 0$ (say). $\phi$ should be the flat vector over the full block, which also has sup norm at $x = 0$. But $\phi$ needs to be orthogonal to $\psi$.

Let $\phi_0 = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (the flat vector). Then $\langle \psi, \phi_0\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} \langle \psi, e_n\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} \hat{\psi}(n)$. Since $\psi$ is supported on $\sim \sqrt{N_k}$ elements, $|\langle \psi, \phi_0\rangle| \leq \sqrt{\sqrt{N_k}/m_k} = N_k^{1/4}/\sqrt{m_k} \sim N_k^{1/4}/e^{\sqrt{N_k}} \to 0$.

So $\phi_0$ is nearly orthogonal to $\psi$. Let $\phi = \frac{\phi_0 - \langle \phi_0, \psi\rangle \psi}{\|\phi_0 - \langle \phi_0, \psi\rangle \psi\|}$. Then $\phi$ is a unit vector orthogonal to $\psi$, and $\phi \approx \phi_0$ (since $\langle \phi_0, \psi\rangle \to 0$). So $\|\phi\|_\infty \approx \|\phi_0\|_\infty \sim e^{\sqrt{N_k}}/\sqrt{2\pi}$.

Now, $v = \alpha \psi + \beta \phi$ with $\alpha = \beta = 1/\sqrt{2}$. At $x = 0$:
$v(0) = \alpha \psi(0) + \beta \phi(0) \approx \frac{1}{\sqrt{2}} (A\sqrt{2\pi} + B\sqrt{2\pi}) / \sqrt{2\pi}$... 

wait, let me be more careful. $\psi(0) = \|\psi\|_\infty$ (assuming the sup is at 0) and $\phi(0) \approx \phi_0(0) = \|\phi_0\|_\infty = \sqrt{m_k}/\sqrt{2\pi}$.

$v(0) = \frac{1}{\sqrt{2}} \psi(0) + \frac{1}{\sqrt{2}} \phi(0) \approx \frac{1}{\sqrt{2}} (N_k^{1/4}/\sqrt{2\pi} + e^{\sqrt{N_k}}/\sqrt{2\pi}) \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}}$.

And $\langle P_k u, v\rangle = \rho_k \alpha = \rho_k / \sqrt{2} \approx N_k^{1/4} e^{-\sqrt{N_k}} / \sqrt{2}$.

So $|\langle P_k u, v\rangle| |v(0)| \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}}}{\sqrt{2}} \cdot \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}} = \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$.

But this is $|\langle P_k u, v\rangle| |v(0)|$, not $\|v\|_\infty$. We need $\|v\|_\infty \geq |v(0)|$, which is true. And the partial sum contribution is $\langle u, v\rangle v = \langle P_k u, v\rangle v$ (since $u$'s projection onto the block is $P_k u$). The sup norm of this is $|\langle P_k u, v\rangle| \|v\|_\infty \geq |\langle P_k u, v\rangle| |v(0)| \sim N_k^{1/4} \to \infty$.

Wait, but I need to be more careful. The partial sum includes $\langle u, v\rangle v$ where $v$ is one of the new basis elements. But $v$ is a specific basis element, and the partial sum at that point includes all previous basis elements plus $v$.

Let me set up the construction more carefully.

Construction:
- $u(x) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} e_n(x)$ (smooth function on $S^1$, using only positive frequencies for simplicity; we can make it real-valued by also including negative frequencies, but let's keep it simple).
- Partition $\{1, 2, 3, \ldots\}$ into blocks $B_k = \{N_k, \ldots, N_k + m_k - 1\}$ with $m_k = \lceil e^{2\sqrt{N_k}} \rceil$ and $N_{k+1} = N_k + m_k$.
- Within each block, the first basis element is $v_k = \frac{1}{\sqrt{2}} \psi_k + \frac{1}{\sqrt{2}} \phi_k$ where $\psi_k = P_k u / \rho_k$ and $\phi_k$ is the (nearly) flat vector orthogonalized against $\psi_k$.
- The remaining $m_k - 1$ basis elements complete the orthonormal basis for the block.
- The new basis is ordered as: (negative frequency standard basis elements, $e_0$), $v_1$, (rest of block 1), $v_2$, (rest of block 2), ...

The partial sum of $u$ up to and including $v_k$ is:
$$S_k = \sum_{j=1}^{k-1} P_j u + \langle u, v_k\rangle v_k$$

$= \text{(standard Fourier partial sum up to } N_k - 1) + \langle P_k u, v_k\rangle v_k$

The standard Fourier partial sum converges uniformly to $u$ (since $u$ is smooth), so $\|\text{standard partial sum up to } N_k - 1\|_\infty \leq \|u\|_\infty + 1$ for large $k$.

And $\|\langle P_k u, v_k\rangle v_k\|_\infty \geq |\langle P_k u, v_k\rangle| |v_k(0)| \sim \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$.

But wait, I need to check that the partial sum $S_k$ actually has large sup norm, not just that the $v_k$ contribution does. The issue is that the standard partial sum and the $v_k$ contribution might cancel at $x = 0$.

At $x = 0$: $S_k(0) = \text{(standard partial sum at 0)} + \langle P_k u, v_k\rangle v_k(0)$.

The standard partial sum at 0 converges to $u(0)$, which is finite. And $\langle P_k u, v_k\rangle v_k(0) \sim \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$ (positive, since we can choose the sign of $v_k$ appropriately).

Actually, $\langle P_k u, v_k\rangle = \rho_k / \sqrt{2} > 0$ (real and positive). And $v_k(0) = \frac{1}{\sqrt{2}} \psi_k(0) + \frac{1}{\sqrt{2}} \phi_k(0)$. Both $\psi_k(0)$ and $\phi_k(0)$ are positive (they're sums of $e_n(0) = 1/\sqrt{2\pi}$ with positive coefficients). So $v_k(0) > 0$ and $\langle P_k u, v_k\rangle v_k(0) > 0$ and $\to \infty$.

Therefore $S_k(0) \to \infty$, so $\|S_k\|_\infty \to \infty$, and the series doesn't converge uniformly (in fact, the partial sums are unbounded).

Wait, I need to double-check that $\psi_k(0)$ and $\phi_k(0)$ are both positive and large.

$\psi_k = P_k u / \rho_k$. $P_k u = \sum_{n \in B_k} e^{-\sqrt{n}} e_n$. At $x = 0$, $P_k u(0) = \sum_{n \in B_k} e^{-\sqrt{n}} \cdot \frac{1}{\sqrt{2\pi}} > 0$. So $\psi_k(0) = P_k u(0) / \rho_k > 0$.

$\phi_k \approx \phi_{k,0} = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$. At $x = 0$, $\phi_{k,0}(0) = \frac{m_k}{\sqrt{m_k} \sqrt{2\pi}} = \frac{\sqrt{m_k}}{\sqrt{2\pi}} > 0$. And $\phi_k$ is a small perturbation of $\phi_{k,0}$, so $\phi_k(0) \approx \phi_{k,0}(0) > 0$.

So indeed $v_k(0) > 0$ and large, and $\langle P_k u, v_k\rangle v_k(0) \to \infty$.

Now, the standard partial sum at 0: $\sum_{n=1}^{N_k-1} e^{-\sqrt{n}} e_n(0) = \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{N_k-1} e^{-\sqrt{n}} \to \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{\infty} e^{-\sqrt{n}} = u(0)$, which is finite. So the standard partial sum at 0 is bounded.

Therefore $S_k(0) = \text{(bounded)} + \text{(something} \to +\infty) \to +\infty$.

This means the partial sums $S_k$ are unbounded, so the series doesn't converge uniformly. 

Now let me make sure all the details are right.

1. $u$ is smooth: $a_n = e^{-\sqrt{n}}$ decays faster than any polynomial, so $u \in C^\infty(S^1)$. ✓

2. The basis elements are smooth: each $v_k$ is a finite linear combination of $e_n$ (trigonometric polynomials), hence smooth. The other basis elements in each block are also finite linear combinations, hence smooth. The negative frequency basis elements $e_n$ for $n \leq 0$ are smooth. ✓

3. The basis is orthonormal: within each block, we apply an orthogonal transformation to the standard basis, preserving orthonormality. Across blocks, the basis elements are in orthogonal subspaces. ✓

4. The basis is complete: it spans the same space as the standard Fourier basis (we just rotated within blocks). ✓

5. The partial sums $S_k$ are unbounded: as shown above, $S_k(0) \to \infty$. ✓

Let me also verify the key estimate more carefully.

$\rho_k = \|P_k u\|_{L^2} = (\sum_{n=N_k}^{N_k+m_k-1} e^{-2\sqrt{n}})^{1/2}$.

With $m_k = \lceil e^{2\sqrt{N_k}} \rceil$, the block goes from $N_k$ to $N_k + e^{2\sqrt{N_k}}$. For $n$ in this range, $\sqrt{n}$ ranges from $\sqrt{N_k}$ to $\sqrt{N_k + e^{2\sqrt{N_k}}} \approx e^{\sqrt{N_k}}$ (for large $N_k$). So $e^{-2\sqrt{n}}$ ranges from $e^{-2\sqrt{N_k}}$ to $e^{-2e^{\sqrt{N_k}}}$, which is essentially 0 for the upper end.

The sum $\sum_{n=N_k}^{N_k+m_k-1} e^{-2\sqrt{n}} \approx \sum_{n=N_k}^{\infty} e^{-2\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-2\sqrt{x}} dx$.

$\int_{N_k}^{\infty} e^{-2\sqrt{x}} dx = \int_{\sqrt{N_k}}^{\infty} 2t e^{-2t} dt = [2t \cdot \frac{-e^{-2t}}{2}]_{\sqrt{N_k}}^{\infty} + \int_{\sqrt{N_k}}^{\infty} e^{-2t} dt = \sqrt{N_k} e^{-2\sqrt{N_k}} + \frac{e^{-2\sqrt{N_k}}}{2}$.

So $\sum_{n \in B_k} e^{-2\sqrt{n}} \approx \sqrt{N_k} e^{-2\sqrt{N_k}}$ and $\rho_k \approx N_k^{1/4} e^{-\sqrt{N_k}}$.

$\langle P_k u, v_k\rangle = \rho_k / \sqrt{2} \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}}}{\sqrt{2}}$.

$v_k(0) = \frac{1}{\sqrt{2}} \psi_k(0) + \frac{1}{\sqrt{2}} \phi_k(0)$.

$\psi_k(0) = \frac{P_k u(0)}{\rho_k} = \frac{\sum_{n \in B_k} e^{-\sqrt{n}} / \sqrt{2\pi}}{\rho_k}$.

$\sum_{n \in B_k} e^{-\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-\sqrt{x}} dx = \int_{\sqrt{N_k}}^{\infty} 2t e^{-t} dt = 2\sqrt{N_k} e^{-\sqrt{N_k}} + 2e^{-\sqrt{N_k}} \approx 2\sqrt{N_k} e^{-\sqrt{N_k}}$.

So $\psi_k(0) \approx \frac{2\sqrt{N_k} e^{-\sqrt{N_k}} / \sqrt{2\pi}}{N_k^{1/4} e^{-\sqrt{N_k}}} = \frac{2 N_k^{1/4}}{\sqrt{2\pi}}$.

$\phi_k(0) \approx \phi_{k,0}(0) = \frac{\sqrt{m_k}}{\sqrt{2\pi}} \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2\pi}}$.

$v_k(0) \approx \frac{1}{\sqrt{2}} \cdot \frac{2N_k^{1/4}}{\sqrt{2\pi}} + \frac{1}{\sqrt{2}} \cdot \frac{e^{\sqrt{N_k}}}{\sqrt{2\pi}} \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}}$ (dominated by the second term).

$\langle P_k u, v_k\rangle v_k(0) \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}}}{\sqrt{2}} \cdot \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}} = \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$. ✓

Great, so the construction works. Let me also verify that $N_k \to \infty$ (so that $N_k^{1/4} \to \infty$).

$N_1 = 1$, $m_1 = \lceil e^{2} \rceil = 8$ (approximately), $N_2 = 9$, $m_2 = \lceil e^{2\sqrt{9}} \rceil = \lceil e^6 \rceil \approx 403$, $N_3 \approx 412$, $m_3 = \lceil e^{2\sqrt{412}} \rceil \approx e^{40.6} \approx 2.3 \times 10^{17}$, ...

So $N_k$ grows very rapidly and $N_k \to \infty$. ✓

Now let me also make sure the construction of the orthonormal basis is valid. Within each block $B_k$ of size $m_k$, we need $m_k$ orthonormal vectors. We define $v_k$ as above, and then complete to an orthonormal basis of the block using Gram-Schmidt. All vectors are finite linear combinations of $e_n$ (trigonometric polynomials), hence smooth.

The full orthonormal basis of $L^2(S^1)$ is:
- $e_n$ for $n \leq 0$ (negative frequencies and constant)
- For each block $B_k$: $v_k, v_{k,2}, \ldots, v_{k,m_k}$ (orthonormal basis of the block)

This is a complete orthonormal basis of smooth functions. ✓

The generalized Fourier series of $u$ is $u = \sum_{n \leq 0} \langle u, e_n\rangle e_n + \sum_{k=1}^{\infty} \sum_{j=1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}$.

Since $u$ has only positive frequency components, $\langle u, e_n\rangle = 0$ for $n \leq 0$. So the series is $\sum_{k=1}^{\infty} \sum_{j=1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}$.

The partial sum up to $v_k$ (including all of blocks $1, \ldots, k-1$ and just $v_k$ from block $k$) is:
$S_k = \sum_{j=1}^{k-1} P_j u + \langle u, v_k\rangle v_k = \sum_{n=1}^{N_k-1} a_n e_n + \langle P_k u, v_k\rangle v_k$.

And $S_k(0) \to \infty$ as shown. ✓

So the answer is YES, such a smooth function and orthonormal basis exist.

Let me now write up the proof cleanly.

Actually, wait. Let me reconsider one thing. I need to make sure that $v_k$ is the FIRST element of block $k$ in the ordering. The ordering of the basis is: (all $e_n$ for $n \leq 0$), then $v_1, v_{1,2}, \ldots, v_{1,m_1}$, then $v_2, v_{2,2}, \ldots, v_{2,m_2}$, etc.

But there are infinitely many $e_n$ for $n \leq 0$. We can't put all of them before $v_1$. We need to interleave.

Actually, since $\langle u, e_n\rangle = 0$ for $n \leq 0$, the ordering of the $e_n$ for $n \leq 0$ doesn't affect the partial sums of $u$'s series. We can interleave them anywhere. For instance:

$e_0, v_1, v_{1,2}, \ldots, v_{1,m_1}, e_{-1}, v_2, v_{2,2}, \ldots, v_{2,m_2}, e_{-2}, v_3, \ldots$

Or we can just put one $e_{-k}$ between blocks. Since $\langle u, e_{-k}\rangle = 0$, these don't contribute to the partial sums.

Actually, to be fully rigorous, let me just define the ordering as: enumerate all basis elements in any order such that $v_k$ comes after all elements of blocks $1, \ldots, k-1$ and before all other elements of block $k$. The negative frequency elements can be placed anywhere (they don't contribute to $u$'s partial sums). For instance, place $e_{-k}$ right before $v_{k+1}$.

The key point is that the partial sum $S_k$ (up to and including $v_k$, but not the rest of block $k$) is well-defined and equals $\sum_{n=1}^{N_k-1} a_n e_n + \langle P_k u, v_k\rangle v_k$.

OK, I think the proof is solid. Let me also consider whether we need $u$ to be real-valued. The problem says "smooth function on $S^1$", which could be complex-valued. If we need real-valued, we can take $u(x) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} (e_n(x) + e_{-n}(x)) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} \cdot \frac{2\cos(nx)}{\sqrt{2\pi}}$, which is real-valued and smooth. The construction would need to be adapted slightly (using cosine/sine basis or working with paired frequencies), but the essential idea is the same.

For simplicity, let me present the proof with complex-valued functions (the problem doesn't specify real-valued).

Actually, let me reconsider whether I should present a cleaner version. The core idea is:

1. Choose $u$ smooth with coefficients $a_n = e^{-\sqrt{n}}$ (for $n \geq 1$).
2. Partition positive integers into blocks $B_k$ with $|B_k| = m_k \approx e^{2\sqrt{N_k}}$ where $N_k$ is the start of block $k$.
3. Within each block, choose the first basis element $v_k$ to be a combination of the "signal" direction $\psi_k = P_k u / \|P_k u\|$ and the "flat" direction $\phi_k$ (normalized sum of all $e_n$ in the block, orthogonalized against $\psi_k$).
4. The partial sum up to $v_k$ has $S_k(0) \to \infty$.

The key estimate is that $\|P_k u\|_{L^2} \cdot \|\phi_k\|_\infty \sim N_k^{1/4} \to \infty$, which happens because:
- $\|P_k u\|_{L^2} \sim N_k^{1/4} e^{-\sqrt{N_k}}$ (the $L^2$ mass in the block)
- $\|\phi_k\|_\infty \sim e^{\sqrt{N_k}}$ (the sup norm of the flat vector in a block of size $e^{2\sqrt{N_k}}$)
- Product $\sim N_k^{1/4} \to \infty$

And by choosing $v_k$ to have components along both $\psi_k$ and $\phi_k$, we get $|\langle P_k u, v_k\rangle| |v_k(0)| \sim N_k^{1/4} \to \infty$.

Let me write this up now.

Hmm, actually, I realize I should double-check one more thing. The partial sum $S_k$ is the sum up to the $N_k$-th basis element (in the ordering), where $v_k$ is the last included element. But the index in the series $\sum_{n \in \mathbb{N}}$ is just a natural number indexing the basis. So the "partial sum" $S_N = \sum_{n=1}^{N} \langle u, u_n\rangle u_n$ for the $N$-th partial sum. We need to show that for some sequence $N \to \infty$, $\|S_N\|_\infty \not\to \|u\|_\infty$ (or more precisely, $S_N$ doesn't converge uniformly).

In our construction, the partial sums at the specific indices corresponding to "just after $v_k$" diverge. Since these indices go to infinity (as $k \to \infty$), the series doesn't converge uniformly.

OK, I'm confident the proof is correct. Let me write it up.

One more thing: I should verify that $u$ is indeed smooth. $u(x) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} e^{inx}/\sqrt{2\pi}$. For $u$ to be $C^\infty$, we need $\sum n^{2p} e^{-2\sqrt{n}} < \infty$ for all $p \geq 0$. Since $e^{-2\sqrt{n}}$ decays faster than any polynomial (i.e., $n^{2p} e^{-2\sqrt{n}} \to 0$ faster than any power), and in fact $\sum n^{2p} e^{-2\sqrt{n}} < \infty$ (by comparison with, say, $\sum n^{2p} e^{-n}$ for large $n$, since $e^{-2\sqrt{n}} \leq e^{-n}$ for $n \geq 4$), this holds. ✓

Also, $u \in L^2$: $\sum e^{-2\sqrt{n}} < \infty$ since $e^{-2\sqrt{n}} \leq n^{-2}$ for large $n$. ✓

Let me write the proof now.

Actually, I realize I should be a bit more careful about the construction of $\phi_k$. Let me define things precisely.

Block $B_k = \{N_k, N_k+1, \ldots, N_k + m_k - 1\}$ where $m_k = \lceil e^{2\sqrt{N_k}} \rceil$ and $N_{k+1} = N_k + m_k$, $N_1 = 1$.

$P_k u = \sum_{n \in B_k} a_n e_n$ where $a_n = e^{-\sqrt{n}}$.

$\rho_k = \|P_k u\|_{L^2} = (\sum_{n \in B_k} |a_n|^2)^{1/2}$.

$\psi_k = P_k u / \rho_k$ (unit vector in the direction of $P_k u$).

$F_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (flat unit vector).

$\phi_k = \frac{F_k - \langle F_k, \psi_k\rangle \psi_k}{\|F_k - \langle F_k, \psi_k\rangle \psi_k\|}$ (flat vector orthogonalized against $\psi_k$).

$v_k = \frac{1}{\sqrt{2}} (\psi_k + \phi_k)$.

Then $\|v_k\|_{L^2} = 1$ (since $\psi_k \perp \phi_k$ and both are unit vectors), and $v_k$ is a smooth function (trigonometric polynomial).

$\langle u, v_k\rangle = \langle P_k u, v_k\rangle = \rho_k \langle \psi_k, v_k\rangle = \rho_k / \sqrt{2}$.

The partial sum up to $v_k$:
$S_k = \sum_{n=1}^{N_k - 1} a_n e_n + \frac{\rho_k}{\sqrt{2}} v_k$

At $x = 0$:
$S_k(0) = \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{N_k-1} e^{-\sqrt{n}} + \frac{\rho_k}{\sqrt{2}} v_k(0)$

The first term converges to $u(0) = \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{\infty} e^{-\sqrt{n}} < \infty$.

For the second term:
$v_k(0) = \frac{1}{\sqrt{2}} (\psi_k(0) + \phi_k(0))$

$\psi_k(0) = \frac{1}{\rho_k \sqrt{2\pi}} \sum_{n \in B_k} e^{-\sqrt{n}}$

$\phi_k(0) \geq F_k(0) - |\langle F_k, \psi_k\rangle| |\psi_k(0)|$ (by triangle inequality, since $\phi_k = (F_k - \langle F_k, \psi_k\rangle\psi_k)/\|\cdot\|$ and $\|\cdot\| \leq 1$)

Actually, let me be more careful. $\phi_k = \frac{F_k - c_k \psi_k}{\sqrt{1 - |c_k|^2}}$ where $c_k = \langle F_k, \psi_k\rangle$.

$\phi_k(0) = \frac{F_k(0) - c_k \psi_k(0)}{\sqrt{1 - |c_k|^2}}$.

$|c_k| = |\langle F_k, \psi_k\rangle| = \frac{|\langle F_k, P_k u\rangle|}{\rho_k} =        — AI历史解题过程（thinking）
#   deepmath_103k_00000320         — 题目ID

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
  <problem_id>deepmath_103k_00000320</problem_id>
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

Does there exist a holomorphic function that is not identically zero and has an uncountable number of zeroes?

## Standard Solution

Okay, so the question is asking if there's a holomorphic function that isn't zero everywhere but still has an uncountable number of zeros. Hmm, interesting. Let me start by recalling some complex analysis basics.

First, holomorphic functions are complex differentiable at every point in their domain. I remember that one key property of holomorphic functions is their behavior regarding zeros. If a holomorphic function has a sequence of zeros that accumulate (i.e., get arbitrarily close) to a point within its domain, then the function must be identically zero on the connected component containing that accumulation point. This is known as the identity theorem, I think.

So, if a function has an uncountable number of zeros, that might mean the zeros aren't just a countable set. But in complex analysis, zeros of a non-zero holomorphic function are isolated. Wait, that's a theorem, right? The identity theorem says that if the zeros have an accumulation point in the domain, the function is zero everywhere. So, if a function isn't identically zero, its zeros must be isolated, meaning each zero has a neighborhood with no other zeros. 

But isolated points would form a countable set, right? Because in a connected open subset of the complex plane, every uncountable set has an accumulation point. So if you have uncountably many zeros, they must accumulate somewhere in the domain, which by the identity theorem would force the function to be zero everywhere. Therefore, such a function cannot exist. 

Wait, let me verify this step by step. Suppose there is a holomorphic function f defined on a domain D (which is open and connected) such that f is not identically zero, but the set Z = {z ∈ D | f(z) = 0} is uncountable. Since D is a subset of the complex plane, which is a separable space (it has a countable dense subset, like the complex numbers with rational real and imaginary parts), any uncountable subset of D must have a limit point in D. This is due to the fact that in a metric space with a countable base, every uncountable subset has a limit point in the space. 

So, if Z is uncountable, then by the identity theorem, since the zeros accumulate at some point in D, f must be identically zero on D. But that contradicts the assumption that f is not identically zero. Therefore, such a function cannot exist. 

But wait, maybe the domain isn't connected? The problem didn't specify, but usually, in complex analysis, unless stated otherwise, domains are connected. If the domain is disconnected, maybe you could have uncountably many zeros spread across different components? But even then, each connected component is an open set. If the function is holomorphic on the entire domain, each connected component is a domain on its own. If the function has uncountably many zeros, then in at least one of those components, the zeros would still have to be uncountable, but again, in each connected component (which is a domain in C), uncountable zeros would lead to an accumulation point, hence the function is zero on that component. So even if the domain is disconnected, unless you have uncountably many components, which isn't possible in C, since C is second countable. 

Wait, the domain could be a collection of uncountably many disjoint open sets? But in C, open sets are made up of countably many disjoint connected components. So, actually, a domain in C can't have uncountably many connected components. Therefore, even if the domain is disconnected, the number of connected components is countable. Therefore, if the function has uncountably many zeros, one of the connected components must contain uncountably many zeros, which again leads to the function being identically zero on that component. But the problem states the function is not identically zero, so maybe it's zero on some components and non-zero on others? But in that case, the zeros are on a union of countably many components, each of which could be a single point if the component is a single point? Wait, no, connected components in a domain in C are open, so they can't be single points. So each connected component is a region where the function is either identically zero or has isolated zeros. 

Therefore, even if the domain is disconnected, the zeros must be on countably many connected components (each of which the function is identically zero) or have isolated zeros. So in total, the zeros would be a countable union of countable sets or uncountable, but if there are uncountably many zeros, they would have to lie in uncountably many connected components, which is impossible. Therefore, the zeros must be countable. 

Therefore, regardless of the domain's connectedness, a holomorphic function not identically zero cannot have uncountably many zeros. So the answer is no, such a function does not exist. 

Let me check if I missed something. Maybe if the function is defined on a non-open set? But holomorphic functions are defined on open sets. If the function is defined on a non-open set with accumulation points outside the domain, but the problem says "has an uncountable number of zeros". For example, suppose the domain is the unit disk, and the function has zeros at uncountably many points inside the disk. But as the unit disk is a separable metric space, any uncountable subset has a limit point in the closure. If the closure is within the domain, then the function is zero. If the limit point is on the boundary, which is not in the domain, then the zeros inside the domain don't accumulate to a point in the domain. But in that case, can you have uncountably many zeros without an accumulation point in the domain?

Wait, in topology, a space is Lindelöf if every open cover has a countable subcover. Every separable metric space is Lindelöf. The complex plane is separable, so any open subset is Lindelöf. So, in an open domain D in C, suppose we have an uncountable set of zeros. Then, since D is Lindelöf, every uncountable subset must have a limit point in D. Wait, is that true? Let me recall: in a Lindelöf space, every uncountable subset has a condensation point (a point where every neighborhood contains uncountably many points of the set), which in a metric space is a limit point. So yes, in a Lindelöf space (which open sets in C are), every uncountable subset has a condensation point, which is a limit point. Therefore, even if you try to have an uncountable set of zeros in D, they must have a limit point in D, so by identity theorem, the function is zero everywhere. Therefore, there's no non-zero holomorphic function with uncountably many zeros in any open domain in C. 

Therefore, the answer is no, such a function does not exist. 

**Final Answer**
\boxed{No}
</think>

To determine if there exists a holomorphic function that is not identically zero but has an uncountable number of zeros, we need to recall key properties of holomorphic functions and their zeros.

1. **Identity Theorem**: If a holomorphic function has zeros that accumulate at a point within its domain, the function must be identically zero on the connected component containing that accumulation point.
2. **Isolated Zeros**: For a non-zero holomorphic function, zeros must be isolated. This means each zero has a neighborhood with no other zeros.
3. **Uncountable Sets in Separable Spaces**: The complex plane is a separable space, meaning every uncountable subset has a limit point within the space. In a domain (open and connected subset) of the complex plane, any uncountable set of zeros would have a limit point in the domain.
4. **Lindelöf Property**: Open sets in the complex plane are Lindelöf, implying every uncountable subset has a condensation point (which is a limit point in a metric space).

Given these properties, if a holomorphic function had an uncountable number of zeros, those zeros would necessarily accumulate at some point within the domain. By the identity theorem, this would force the function to be identically zero throughout the domain, contradicting the requirement that the function is not identically zero. 

Thus, no such holomorphic function can exist.

\[
\boxed{No}
\]

## AI's Thinking (Attempted Solution Process)

Let me think about this problem carefully.

The question: Does there exist a smooth function $u$ on $S^1$ such that the generalized Fourier series $u = \sum_{n \in \mathbb{N}} \langle u, u_n \rangle u_n$ does not converge uniformly, where $\{u_n\}$ is an orthonormal basis of smooth functions on $S^1$?

So we get to choose the orthonormal basis $\{u_n\}$ of smooth functions on $S^1$ (with respect to $L^2$ inner product presumably), and we need to find a smooth function $u$ such that its generalized Fourier series (expansion in this basis) does not converge uniformly.

First, let me think about the standard case. The standard Fourier basis $e^{inx}/\sqrt{2\pi}$ gives uniform convergence for smooth functions (in fact, the Fourier series of a smooth function converges absolutely and uniformly, with rapid decay of coefficients).

But here we're allowed to choose ANY orthonormal basis of smooth functions. The question is whether there exists some "bad" orthonormal basis and some smooth function whose expansion doesn't converge uniformly.

This is a classic type of result. Let me think about it.

Key insight: The uniform norm and $L^2$ norm are different. We can construct an orthonormal basis where the partial sums have large uniform norm.

Actually, let me think about this more carefully. The question is whether there EXISTS such a basis and such a function.

One approach: Take the standard Fourier basis and apply a unitary transformation that mixes modes in a way that destroys uniform convergence.

Actually, a cleaner approach. Consider the following. We want an orthonormal basis $\{u_n\}$ of smooth functions and a smooth $u$ such that $\sum \langle u, u_n\rangle u_n$ doesn't converge uniformly.

Let me think about what's known. There's a classical result that for any orthonormal basis, the Fourier series converges in $L^2$. But uniform convergence is not guaranteed for arbitrary orthonormal bases.

Actually, there's a result by... let me think. The Menshov-Rademacher theorem and related results are about orthogonal systems.

Let me think about a concrete construction.

Consider smooth functions on $S^1$. The space $C^\infty(S^1)$ is dense in $L^2(S^1)$. We can build an orthonormal basis of smooth functions by Gram-Schmidt on some countable dense set of smooth functions.

The idea: We want to construct an orthonormal basis where the partial sums of some smooth function blow up in sup norm.

Here's a strategy. Let's think about it in terms of the following. Consider a smooth function $u$ with $\|u\|_\infty = 1$ but $\|u\|_{L^2}$ very small. If we can make $u$ itself one of the basis elements, say $u = u_N$, then the partial sum $S_N = \sum_{n=1}^N \langle u, u_n\rangle u_n$ includes the term $\langle u, u_N\rangle u_N = \|u\|_{L^2}^2 \cdot u / \|u\|_{L^2}$... wait, if $u_N = u/\|u\|_{L^2}$, then $\langle u, u_N\rangle = \|u\|_{L^2}$, and the contribution is $\|u\|_{L^2} \cdot u_N = \|u\|_{L^2} \cdot u/\|u\|_{L^2} = u$. So the partial sum up to $N$ would include $u$ itself (plus other terms). That doesn't immediately help.

Let me think differently.

Alternative approach: We want the partial sums to not converge uniformly. One way is to make the partial sums oscillate or diverge in sup norm.

Classic construction idea: Take a sequence of smooth functions $\phi_k$ that are orthonormal in $L^2$ but have large sup norm. Then for a suitable smooth $u$, the partial sums can have large sup norm.

Actually, here's a cleaner idea. Consider the following construction:

Take the standard trigonometric basis. Now, construct a new orthonormal basis by taking "blocks" of the standard basis and applying unitary transformations within each block.

Specifically, partition $\mathbb{Z}$ into blocks $B_1, B_2, \ldots$ and within each block, apply a unitary transformation to the exponentials. The new basis elements are still smooth (finite linear combinations of exponentials), and they're still orthonormal.

Now, the Fourier coefficients of $u$ in the new basis are related to the standard Fourier coefficients by the unitary transformations within blocks.

The partial sums in the new basis group terms by blocks. If we order the new basis so that all elements of block $B_k$ come together, then the partial sum at the end of block $B_k$ equals the partial sum of the standard Fourier series up to the max frequency in blocks $B_1, \ldots, B_k$ (since unitary transformations within blocks preserve the partial sum within each block — the projection onto the span of a block is invariant under unitary transformations of that block).

Wait, that's a key point. If we apply a unitary transformation within a block, the projection onto the span of that block is unchanged. So the partial sum at block boundaries is the same as the standard Fourier partial sum at the corresponding frequency. This means block-diagonal unitary transformations don't change the partial sums at block boundaries.

But the partial sums WITHIN a block can be different! And if the blocks are large, the intermediate partial sums within a block can be very different from the standard Fourier partial sums.

So the strategy is: make large blocks, and within each block, apply a unitary transformation such that some intermediate partial sum within the block has huge sup norm.

Let me formalize this.

Let the standard basis be $e_n(x) = e^{inx}/\sqrt{2\pi}$ for $n \in \mathbb{Z}$. Consider blocks $B_k = \{N_k, N_k+1, \ldots, N_k + m_k - 1\}$ (in terms of frequencies). Within block $B_k$, we have $m_k$ basis elements. We apply an orthogonal (unitary) transformation $O_k \in O(m_k)$ to get new basis elements $u_{k,j} = \sum_{i} (O_k)_{ji} e_{N_k + i}$.

These are still smooth (trigonometric polynomials), orthonormal, and form a complete basis.

Now, take $u$ to be a smooth function. Its standard Fourier coefficients are $\hat{u}(n) = \langle u, e_n\rangle$. The new coefficients are $\langle u, u_{k,j}\rangle = \sum_i (O_k)_{ji} \hat{u}(N_k + i)$.

The partial sum of the new series up to some point within block $B_k$ is:
$$S = \sum_{\text{completed blocks}} \text{projection onto span of block} + \text{partial projection within block } B_k$$

The projection onto completed blocks equals the standard Fourier partial sum up to the max frequency of those blocks. Within block $B_k$, the partial sum depends on which basis elements we've included so far.

So the partial sum at some intermediate point in block $B_k$ is:
$$S = \text{(standard partial sum up to } N_k - 1) + \sum_{j=1}^{J} \langle u, u_{k,j}\rangle u_{k,j}$$

where $J < m_k$.

The term $\sum_{j=1}^{J} \langle u, u_{k,j}\rangle u_{k,j}$ is a partial sum of the expansion of $u$'s projection onto block $B_k$ in the rotated basis. This can be made large in sup norm by choosing the rotation appropriately.

Let me think about how to make this concrete.

Consider a single block with frequencies $\{0, 1, \ldots, m-1\}$ (for simplicity, say the constant term and first harmonics). The projection of $u$ onto this block is $P u = \sum_{n=0}^{m-1} \hat{u}(n) e_n$. In the standard basis, the partial sums of $Pu$ converge nicely. But if we rotate the basis, the partial sums of $Pu$ in the rotated basis can be made large.

Specifically, $Pu$ is a trigonometric polynomial of degree $m-1$. Its $L^2$ norm is $\|Pu\|_{L^2} = (\sum_{n=0}^{m-1} |\hat{u}(n)|^2)^{1/2}$. We can write $Pu = \sum_{j=1}^{m} c_j v_j$ where $v_j$ is the rotated basis and $c_j = \langle u, v_j\rangle$.

The partial sum $\sum_{j=1}^{J} c_j v_j$ is the projection of $Pu$ onto the span of $\{v_1, \ldots, v_J\}$. By choosing the rotation, we can make this projection have large sup norm.

In fact, we can choose $v_1 = Pu / \|Pu\|_{L^2}$. Then $c_1 = \|Pu\|_{L^2}$, and the first partial sum is $c_1 v_1 = Pu$. So the partial sum after one term of the block equals $Pu$ plus the standard partial sum up to the previous block. That's not larger than the full thing.

Hmm, let me think about this differently. We want the partial sum to be much LARGER than $u$ in sup norm.

Consider this: take $v_1$ to be a function in the span of the block with $\|v_1\|_{L^2} = 1$ but $\|v_1\|_\infty$ very large. Then $c_1 = \langle u, v_1\rangle$ and the partial sum includes $c_1 v_1$ which has sup norm $|c_1| \|v_1\|_\infty$.

But $|c_1| = |\langle u, v_1\rangle| \leq \|u\|_{L^2} \|v_1\|_{L^2} = \|u\|_{L^2}$ (since $\|v_1\|_{L^2} = 1$). And $\|v_1\|_\infty$ can be as large as $\sqrt{m}$ (for a trigonometric polynomial of degree $m$ with $L^2$ norm 1, the sup norm can be up to $\sqrt{m}$, achieved by a Dirichlet-like kernel).

Actually, the sup norm of a trigonometric polynomial of degree $N$ with $L^2$ norm 1 can be as large as $\sqrt{2N+1}$ (the Dirichlet kernel $D_N$ has $L^2$ norm $\sqrt{2\pi(2N+1)}$ and sup norm $2\pi(2N+1)$, so normalized, sup norm / $L^2$ norm $= \sqrt{2N+1}$... let me be more careful).

Let me use the normalized basis $e_n = e^{inx}/\sqrt{2\pi}$. Then $\|e_n\|_{L^2} = 1$ and $\|e_n\|_\infty = 1/\sqrt{2\pi}$.

The Dirichlet kernel $D_N(x) = \sum_{n=-N}^{N} e^{inx} = \frac{\sin((N+1/2)x)}{\sin(x/2)}$. In terms of the normalized basis, $\sum_{n=-N}^{N} e_n = D_N(x)/\sqrt{2\pi}$. The $L^2$ norm of $\sum_{n=-N}^N e_n$ is $\sqrt{2N+1}$ (since the $e_n$ are orthonormal). The sup norm is $\|D_N\|_\infty / \sqrt{2\pi} = (2N+1)/\sqrt{2\pi}$.

So the ratio $\|\sum_{n=-N}^N e_n\|_\infty / \|\sum_{n=-N}^N e_n\|_{L^2} = (2N+1)/\sqrt{2\pi} / \sqrt{2N+1} = \sqrt{2N+1}/\sqrt{2\pi} \sim \sqrt{N}$.

OK so for a block of size $m$ (frequencies in a range), we can find a unit vector in the span with sup norm $\sim \sqrt{m}$.

Now, let's set up the construction. We want to choose $u$ smooth and blocks such that the partial sums blow up.

Let me try a specific construction. Let $u$ be a smooth function, say $u(x) = \sum_{n} a_n e_n(x)$ with rapid decay (since $u$ is smooth). 

Consider blocks $B_k$ of size $m_k$ at frequencies around $N_k$. The standard Fourier coefficients of $u$ at these frequencies are $a_{N_k}, a_{N_k+1}, \ldots$ which decay rapidly.

Within block $B_k$, the projection of $u$ is $P_k u = \sum_{n \in B_k} a_n e_n$ with $L^2$ norm $\rho_k = (\sum_{n \in B_k} |a_n|^2)^{1/2}$.

Now, in the rotated basis for block $B_k$, let the first basis vector be $v_{k,1} = P_k u / \rho_k$ (if $\rho_k > 0$). Then $\langle u, v_{k,1}\rangle = \rho_k$ and the first partial sum within the block is $\rho_k \cdot v_{k,1} = P_k u$. This just gives us $P_k u$, which is bounded.

That's not helpful. Let me instead make the first basis vector in the block be something with large sup norm, say $w_k = $ (normalized Dirichlet-like kernel in the block's frequency range). Then $\langle u, w_k\rangle$ could be small (since $u$'s coefficients decay), but the partial sum $\langle u, w_k\rangle w_k$ has sup norm $|\langle u, w_k\rangle| \|w_k\|_\infty$.

We have $|\langle u, w_k\rangle| \leq \|P_k u\|_{L^2} \|w_k\|_{L^2} = \rho_k \cdot 1 = \rho_k$. And $\|w_k\|_\infty \sim \sqrt{m_k}$. So the sup norm of the partial sum contribution is at most $\rho_k \sqrt{m_k}$.

But actually, we can be more precise. $\langle u, w_k\rangle = \sum_{n \in B_k} a_n \langle e_n, w_k\rangle = \sum_{n \in B_k} a_n \overline{\hat{w}_k(n)}$. If $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (the normalized flat sum), then $\langle e_n, w_k\rangle = 1/\sqrt{m_k}$, so $\langle u, w_k\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n$.

The partial sum after including $w_k$ as the first element of block $B_k$ is:
$$S = \text{(standard partial sum up to before block } B_k) + \langle u, w_k\rangle w_k$$

The sup norm of $\langle u, w_k\rangle w_k$ is $|\langle u, w_k\rangle| \|w_k\|_\infty = \left|\frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n\right| \cdot \frac{m_k}{\sqrt{2\pi}\sqrt{m_k}} \cdot \sqrt{2\pi}$...

Hmm, let me be more careful with normalizations. Let me use $e_n(x) = e^{inx}/\sqrt{2\pi}$, so $\|e_n\|_{L^2} = 1$, $\|e_n\|_\infty = 1/\sqrt{2\pi}$.

For a block $B_k = \{N_k, \ldots, N_k + m_k - 1\}$, define $w_k = \frac{1}{\sqrt{m_k}} \sum_{n=N_k}^{N_k+m_k-1} e_n$. Then $\|w_k\|_{L^2} = 1$ and $\|w_k\|_\infty = \frac{1}{\sqrt{m_k}} \cdot \frac{1}{\sqrt{2\pi}} \cdot \left\|\sum_{n=N_k}^{N_k+m_k-1} e^{inx}\right\|_\infty$.

Now $\sum_{n=N_k}^{N_k+m_k-1} e^{inx} = e^{iN_k x} \sum_{j=0}^{m_k-1} e^{ijx} = e^{iN_k x} \frac{1 - e^{im_k x}}{1 - e^{ix}}$. The sup norm of this is $m_k$ (at $x = 0$). So $\|w_k\|_\infty = \frac{m_k}{\sqrt{m_k} \sqrt{2\pi}} = \frac{\sqrt{m_k}}{\sqrt{2\pi}}$.

And $\langle u, w_k\rangle = \frac{1}{\sqrt{m_k}} \sum_{n=N_k}^{N_k+m_k-1} a_n$ where $a_n = \langle u, e_n\rangle = \sqrt{2\pi} \hat{u}(n)$ (with the standard Fourier convention $\hat{u}(n) = \frac{1}{2\pi}\int u(x) e^{-inx} dx$... actually let me not worry about the exact normalization and just work with $a_n = \langle u, e_n\rangle$).

So the partial sum contribution from $w_k$ is $\langle u, w_k\rangle w_k$, with sup norm:
$$|\langle u, w_k\rangle| \|w_k\|_\infty = \left|\frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n\right| \cdot \frac{\sqrt{m_k}}{\sqrt{2\pi}} = \frac{1}{\sqrt{2\pi}} \left|\sum_{n \in B_k} a_n\right|$$

Now, for a smooth function $u$, the coefficients $a_n$ decay rapidly. If the block is at high frequencies $N_k$ with size $m_k$, then $|a_n| \lesssim N_k^{-p}$ for any $p$ (since $u$ is smooth). So $|\sum_{n \in B_k} a_n| \lesssim m_k \cdot N_k^{-p}$.

To make this large, we'd need $m_k \cdot N_k^{-p}$ to be large, but for smooth $u$, we can take $p$ as large as we want, so this seems hard to make diverge.

Hmm, but wait. We get to CHOOSE $u$. So let's choose $u$ strategically.

Actually, the key issue is: we need $u$ to be smooth (so coefficients decay faster than any polynomial), but we want $\sum_{n \in B_k} a_n$ to not go to zero (or to grow).

If $u$ is smooth, $|a_n| \leq C_p (1+|n|)^{-p}$ for all $p$. So $|\sum_{n \in B_k} a_n| \leq C_p m_k N_k^{-p}$. For this to be bounded below, we need $m_k \geq c N_k^p$ for some $p$. But since $p$ can be arbitrarily large (smooth function), we'd need $m_k$ to grow faster than any polynomial in $N_k$. 

But wait, we also need the blocks to cover all frequencies and be disjoint. If $m_k$ grows super-polynomially relative to $N_k$, and $N_{k+1} = N_k + m_k$, then $N_k$ grows very fast. The coefficients $a_n$ for $n \in B_k$ are roughly $a_{N_k}$ (if $m_k$ is not too large relative to the decay scale), and $a_{N_k} \sim N_k^{-p}$ for all $p$.

Actually, for a smooth function, $a_n$ decays faster than any polynomial, but we can choose $u$ such that $a_n$ doesn't decay TOO fast. For instance, $a_n \sim e^{-\sqrt{|n|}}$ or $a_n \sim e^{-|n|^\alpha}$ for some $\alpha < 1$. Such a function is still smooth (since $e^{-|n|^\alpha}$ decays faster than any polynomial for any $\alpha > 0$).

Wait, is that right? $e^{-|n|^\alpha}$ for $\alpha > 0$: does $\sum n^p e^{-n^\alpha}$ converge for all $p$? Yes, because $e^{-n^\alpha}$ decays faster than any polynomial. So $u(x) = \sum a_n e^{inx}$ with $a_n = e^{-|n|^\alpha}$ is smooth for any $\alpha > 0$.

But it's not analytic (for $\alpha < 1$). That's fine, we only need smooth.

Now, with $a_n = e^{-n^\alpha}$ (for $n > 0$), consider a block $B_k = \{N_k, \ldots, N_k + m_k - 1\}$. Then $\sum_{n \in B_k} a_n \approx m_k \cdot e^{-N_k^\alpha}$ (if $m_k \ll N_k$ so that $a_n$ doesn't vary much over the block). 

The sup norm of the partial sum contribution is $\sim \frac{m_k e^{-N_k^\alpha}}{\sqrt{2\pi}}$.

For this to diverge, we need $m_k e^{-N_k^\alpha} \to \infty$, i.e., $m_k \gg e^{N_k^\alpha}$.

But we also need $m_k \ll N_k$ for the approximation to hold (so that $a_n$ doesn't vary much). This gives $e^{N_k^\alpha} \ll N_k$, which is impossible for large $N_k$.

So this doesn't work with this choice. Let me reconsider.

Actually, I don't need $a_n$ to be approximately constant over the block. Let me reconsider.

The sup norm of the partial sum contribution from $w_k$ is $\frac{1}{\sqrt{2\pi}} |\sum_{n \in B_k} a_n|$. I need this to not go to zero.

If $a_n = e^{-n^\alpha}$ and the block is $\{N_k, \ldots, N_k + m_k - 1\}$, then $\sum_{n \in B_k} a_n \leq m_k e^{-N_k^\alpha}$. For this to be $\geq c > 0$, we need $m_k \geq c e^{N_k^\alpha}$.

But then $N_{k+1} = N_k + m_k \geq N_k + c e^{N_k^\alpha}$, which grows very fast. The point is that the blocks would be huge, but that's OK — we just need the construction to work.

But wait, we also need $u$ to be in $L^2$, i.e., $\sum |a_n|^2 < \infty$. With $a_n = e^{-n^\alpha}$, this is fine for any $\alpha > 0$.

And we need $u$ to be smooth, which requires $\sum n^{2p} |a_n|^2 < \infty$ for all $p$, i.e., $\sum n^{2p} e^{-2n^\alpha} < \infty$, which is true for any $\alpha > 0$.

So let's try: $a_n = e^{-n^\alpha}$ for $n \geq 1$ (and $a_{-n} = a_n$ or just work with one-sided, or set $a_{-n} = 0$).

Actually, let me work on $S^1 = \mathbb{R}/2\pi\mathbb{Z}$ and use the basis $e_n = e^{inx}/\sqrt{2\pi}$ for $n \in \mathbb{Z}$.

Let me set $a_n = e^{-|n|^\alpha}$ for some $0 < \alpha < 1$, and $a_0 = 0$ (or whatever). Then $u(x) = \sum_{n \in \mathbb{Z}} a_n e_n(x)$ is smooth.

Now, I need to construct the orthonormal basis. Here's the plan:

1. Partition $\mathbb{Z}_{>0}$ (positive frequencies) into blocks $B_1, B_2, \ldots$ where $B_k = \{N_k, N_k + 1, \ldots, N_k + m_k - 1\}$ with $N_1 = 1$ and $N_{k+1} = N_k + m_k$.

2. For the negative frequencies, keep the standard basis (or also partition them, doesn't matter).

3. Within each block $B_k$, define the first new basis element as $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$, and the remaining $m_k - 1$ basis elements as any orthonormal completion (e.g., via Gram-Schmidt).

4. Order the new basis so that $w_1, (\text{rest of block 1}), w_2, (\text{rest of block 2}), \ldots$ — actually, we want $w_k$ to come first in each block, and the ordering of blocks is sequential.

Wait, but we need the partial sums to diverge. The partial sum up to $w_k$ (i.e., including all of blocks $1, \ldots, k-1$ and just $w_k$ from block $k$) is:

$$S_k = \sum_{j=1}^{k-1} P_j u + \langle u, w_k\rangle w_k$$

where $P_j u$ is the projection of $u$ onto block $B_j$ (which equals $\sum_{n \in B_j} a_n e_n$).

Now, $S_k = \sum_{n=1}^{N_k - 1} a_n e_n + \langle u, w_k\rangle w_k$ (the standard partial sum up to $N_k - 1$, plus the $w_k$ contribution).

Wait, that's not quite right. The partial sum up to $w_k$ includes all completed blocks (which give the standard partial sum up to $N_k - 1$) plus $w_k$ from the current block. But the standard partial sum up to $N_k - 1$ also includes the negative frequencies if we kept those standard. Let me simplify by only working with positive frequencies and setting negative frequency coefficients to zero.

Let me redefine: $u(x) = \sum_{n=1}^{\infty} a_n e_n(x) + \overline{a_n} \overline{e_n(x)}$... actually, let me just work with complex-valued functions for simplicity, or just use the one-sided basis.

Hmm, let me simplify. Let me use the orthonormal basis $\{e_n : n \in \mathbb{Z}\}$ of $L^2(S^1)$ where $e_n(x) = e^{inx}/\sqrt{2\pi}$. I'll construct a new orthonormal basis by modifying only the positive frequency part.

Let $u(x) = \sum_{n=1}^{\infty} a_n e_n(x)$ with $a_n = e^{-n^\alpha}$, $0 < \alpha < 1$. This is a smooth function (the negative frequency part is zero, which is fine).

Now, partition $\{1, 2, 3, \ldots\}$ into blocks $B_k = \{N_k, \ldots, N_k + m_k - 1\}$ with $N_1 = 1$, $N_{k+1} = N_k + m_k$.

For negative frequencies $\{..., -2, -1, 0\}$, keep the standard basis $e_n$.

For each block $B_k$ (positive frequencies), define:
- $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (first element of the rotated block)
- $v_{k,2}, \ldots, v_{k,m_k}$: orthonormal completion of $w_k$ in $\text{span}\{e_n : n \in B_k\}$.

The new orthonormal basis is: $\{e_n : n \leq 0\} \cup \{w_1, v_{1,2}, \ldots, v_{1,m_1}, w_2, v_{2,2}, \ldots\}$.

Order them as: $e_0, e_{-1}, e_{-2}, \ldots$ (but this is infinite; let me interleave). Actually, the ordering matters for the partial sums. Let me order the basis as:

$e_0, w_1, v_{1,2}, \ldots, v_{1,m_1}, w_2, v_{2,2}, \ldots, v_{2,m_2}, w_3, \ldots$

and put the negative frequency basis elements somewhere (they don't matter since $u$ has no negative frequency components, so $\langle u, e_{-n}\rangle = 0$).

Actually, to be careful, let me just include all negative frequency basis elements at the beginning. Since $\langle u, e_n\rangle = 0$ for $n \leq 0$, these contribute nothing to the partial sums of $u$'s expansion. So effectively, the partial sums of $u$ are determined by the positive frequency blocks.

The partial sum of $u$ up to and including $w_k$ (but not the rest of block $k$) is:

$$S_k = \sum_{j=1}^{k-1} \sum_{n \in B_j} a_n e_n + \langle u, w_k\rangle w_k$$

The first part is $\sum_{n=1}^{N_k - 1} a_n e_n = $ (standard Fourier partial sum of $u$ up to frequency $N_k - 1$).

The second part: $\langle u, w_k\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} a_n = \frac{1}{\sqrt{m_k}} \sum_{n=N_k}^{N_k+m_k-1} e^{-n^\alpha}$.

And $w_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$.

So $\langle u, w_k\rangle w_k = \frac{1}{m_k} \left(\sum_{n \in B_k} a_n\right) \sum_{n \in B_k} e_n$.

The sup norm of this is $\frac{1}{m_k} \left|\sum_{n \in B_k} a_n\right| \cdot \left\|\sum_{n \in B_k} e_n\right\|_\infty$.

Now, $\left\|\sum_{n \in B_k} e_n\right\|_\infty = \frac{1}{\sqrt{2\pi}} \left\|\sum_{n=N_k}^{N_k+m_k-1} e^{inx}\right\|_\infty = \frac{m_k}{\sqrt{2\pi}}$ (the sup is achieved at $x = 0$).

So $\|\langle u, w_k\rangle w_k\|_\infty = \frac{1}{m_k} \left|\sum_{n \in B_k} a_n\right| \cdot \frac{m_k}{\sqrt{2\pi}} = \frac{1}{\sqrt{2\pi}} \left|\sum_{n \in B_k} a_n\right|$.

Now, $\sum_{n \in B_k} a_n = \sum_{n=N_k}^{N_k+m_k-1} e^{-n^\alpha}$. 

Since $e^{-n^\alpha}$ is decreasing, $\sum_{n=N_k}^{N_k+m_k-1} e^{-n^\alpha} \geq m_k \cdot e^{-(N_k+m_k-1)^\alpha}$.

Hmm, but also $\leq m_k \cdot e^{-N_k^\alpha}$.

So $\|\langle u, w_k\rangle w_k\|_\infty \geq \frac{m_k e^{-(N_k+m_k)^\alpha}}{\sqrt{2\pi}}$.

For this to go to infinity, we need $m_k e^{-(N_k+m_k)^\alpha} \to \infty$, i.e., $\log m_k > (N_k + m_k)^\alpha + O(1)$.

But we also need the standard partial sum $\sum_{n=1}^{N_k-1} a_n e_n$ to be bounded (which it is, since it converges to $u$ uniformly — wait, does it? The standard Fourier series of a smooth function converges uniformly. Yes, for smooth $u$, the standard Fourier series converges absolutely and uniformly.)

Actually, the standard Fourier series of $u$ converges uniformly to $u$. So $\sum_{n=1}^{N} a_n e_n \to u$ uniformly. In particular, $\left\|\sum_{n=1}^{N_k-1} a_n e_n\right\|_\infty \leq \|u\|_\infty + \epsilon_k$ where $\epsilon_k \to 0$.

So $\|S_k\|_\infty \geq \|\langle u, w_k\rangle w_k\|_\infty - \left\|\sum_{n=1}^{N_k-1} a_n e_n\right\|_\infty \geq \frac{m_k e^{-(N_k+m_k)^\alpha}}{\sqrt{2\pi}} - (\|u\|_\infty + 1)$.

If we can make $m_k e^{-(N_k+m_k)^\alpha} \to \infty$, then $\|S_k\|_\infty \to \infty$, and the series doesn't converge uniformly (in fact, the partial sums are unbounded).

So the question reduces to: can we choose blocks (i.e., $N_k$ and $m_k$) such that $m_k e^{-(N_k + m_k)^\alpha} \to \infty$?

This requires $\log m_k > (N_k + m_k)^\alpha$, i.e., $m_k > e^{(N_k + m_k)^\alpha}$.

But if $m_k > e^{(N_k + m_k)^\alpha}$, then $m_k > e^{m_k^\alpha}$ (since $N_k + m_k > m_k$). For large $m_k$, $e^{m_k^\alpha} \gg m_k$ when $\alpha > 0$. So $m_k > e^{m_k^\alpha}$ is impossible for large $m_k$.

Hmm, so this approach doesn't directly work because the block size $m_k$ appears in the exponent too.

Let me reconsider. The issue is that $\sum_{n \in B_k} a_n \leq m_k a_{N_k} = m_k e^{-N_k^\alpha}$, but also $\sum_{n \in B_k} a_n \geq m_k a_{N_k + m_k} = m_k e^{-(N_k+m_k)^\alpha}$.

The sup norm of the contribution is $\frac{1}{\sqrt{2\pi}} |\sum_{n \in B_k} a_n|$, which is at most $\frac{m_k e^{-N_k^\alpha}}{\sqrt{2\pi}}$.

For this to diverge, we need $m_k e^{-N_k^\alpha} \to \infty$, i.e., $m_k \gg e^{N_k^\alpha}$.

And we need $N_{k+1} = N_k + m_k$, so $N_{k+1} \approx m_k$ (if $m_k \gg N_k$).

So let's try: $m_k = \lceil e^{N_k^\alpha} \cdot k \rceil$ (growing faster than $e^{N_k^\alpha}$). Then $N_{k+1} = N_k + m_k \approx e^{N_k^\alpha} \cdot k$.

The sup norm of the $w_k$ contribution is $\sim \frac{m_k e^{-N_k^\alpha}}{\sqrt{2\pi}} \sim \frac{k}{\sqrt{2\pi}} \to \infty$. 

But wait, I need to check that $\sum_{n \in B_k} a_n \approx m_k e^{-N_k^\alpha}$, which requires that $a_n$ doesn't vary too much over the block. Since $a_n = e^{-n^\alpha}$ and the block goes from $N_k$ to $N_k + m_k - 1$, the ratio $a_{N_k + m_k}/a_{N_k} = e^{-(N_k+m_k)^\alpha + N_k^\alpha}$. 

$(N_k + m_k)^\alpha - N_k^\alpha = N_k^\alpha [(1 + m_k/N_k)^\alpha - 1] \approx N_k^\alpha \cdot \alpha \cdot m_k/N_k = \alpha m_k N_k^{\alpha - 1}$ for $m_k \ll N_k$.

But in our case, $m_k \gg N_k$ (since $m_k \sim e^{N_k^\alpha} \cdot k$ and $N_k$ grows), so $(N_k + m_k)^\alpha \approx m_k^\alpha$.

So $a_{N_k + m_k}/a_{N_k} = e^{-m_k^\alpha + N_k^\alpha}$. Since $m_k \sim e^{N_k^\alpha} k$, we have $m_k^\alpha \sim e^{\alpha N_k^\alpha} k^\alpha$, which is much larger than $N_k^\alpha$. So $a_{N_k + m_k}/a_{N_k} \approx e^{-m_k^\alpha} \to 0$ very fast.

This means most of the sum $\sum_{n \in B_k} a_n$ comes from the first few terms (near $N_k$), and the sum is approximately $\sum_{n=N_k}^{\infty} e^{-n^\alpha} \approx \int_{N_k}^{\infty} e^{-x^\alpha} dx$.

For large $N_k$, $\int_{N_k}^{\infty} e^{-x^\alpha} dx \sim \frac{1}{\alpha} N_k^{1-\alpha} e^{-N_k^\alpha}$ (by Laplace's method / integration by parts).

So $\sum_{n \in B_k} a_n \approx \sum_{n=N_k}^{\infty} e^{-n^\alpha} \approx C N_k^{1-\alpha} e^{-N_k^\alpha}$ (since the block is so large that it captures essentially all the remaining mass).

Wait, but that means $\sum_{n \in B_k} a_n \approx C N_k^{1-\alpha} e^{-N_k^\alpha}$, which goes to 0 as $N_k \to \infty$ (since $e^{-N_k^\alpha}$ dominates). So the sup norm of the $w_k$ contribution goes to 0, not infinity!

The problem is that when the block is too large, the sum $\sum_{n \in B_k} a_n$ is essentially the tail sum, which goes to 0.

So there's a tension: we need $m_k$ large enough that $m_k e^{-N_k^\alpha}$ is large, but if $m_k$ is too large, the sum saturates at the tail sum which is $\sim N_k^{1-\alpha} e^{-N_k^\alpha}$, which goes to 0.

The optimal $m_k$ is where $a_{N_k + m_k} \approx a_{N_k} / 2$, i.e., $(N_k + m_k)^\alpha - N_k^\alpha \approx \log 2$. For large $N_k$, this gives $m_k \approx \frac{N_k^{1-\alpha}}{\alpha} \log 2$. With this $m_k$, $\sum_{n \in B_k} a_n \approx m_k e^{-N_k^\alpha} \approx C N_k^{1-\alpha} e^{-N_k^\alpha}$, which still goes to 0.

So with $a_n = e^{-n^\alpha}$, the sup norm of the $w_k$ contribution is $\sim N_k^{1-\alpha} e^{-N_k^\alpha} \to 0$. This doesn't diverge.

The fundamental issue is that for a smooth function, the coefficients decay faster than any polynomial, so the "mass" in any block at high frequencies is small, and we can't make the partial sums diverge this way.

Let me reconsider the problem. Maybe I need a different approach.

Actually, wait. Let me reconsider. The issue is that I was trying to make the partial sums diverge to infinity. But for uniform convergence to fail, I just need the partial sums to not converge uniformly, which could mean they oscillate or fail to be Cauchy in sup norm.

But actually, if the partial sums are unbounded, that's the strongest way to fail uniform convergence.

Let me think about this differently. Maybe I should not use the "flat" vector $w_k = \frac{1}{\sqrt{m_k}} \sum e_n$ but instead use a different vector in the block.

The key quantity is: for a unit vector $v$ in the span of $\{e_n : n \in B_k\}$, what is $|\langle u, v\rangle| \|v\|_\infty$?

We have $|\langle u, v\rangle| \leq \|P_k u\|_{L^2} = \rho_k$ (the $L^2$ norm of the projection of $u$ onto the block). And $\|v\|_\infty$ can be as large as $\sqrt{m_k}/\sqrt{2\pi}$ (for the flat vector).

But actually, we can do better. We can choose $v$ to maximize $|\langle u, v\rangle| \|v\|_\infty$ subject to $\|v\|_{L^2} = 1$ and $v \in \text{span}\{e_n : n \in B_k\}$.

Hmm, but $|\langle u, v\rangle| \leq \rho_k$ and $\|v\|_\infty \leq \sqrt{m_k}/\sqrt{2\pi}$, so the product is at most $\rho_k \sqrt{m_k}/\sqrt{2\pi}$.

Now, $\rho_k^2 = \sum_{n \in B_k} |a_n|^2$. For $a_n = e^{-n^\alpha}$ and a block at $N_k$ with size $m_k$, $\rho_k^2 \approx m_k e^{-2N_k^\alpha}$ (if $m_k$ is not too large). So $\rho_k \approx \sqrt{m_k} e^{-N_k^\alpha}$.

The product is $\rho_k \sqrt{m_k}/\sqrt{2\pi} \approx m_k e^{-N_k^\alpha}/\sqrt{2\pi}$.

But we need $v$ to simultaneously have $\langle u, v\rangle \approx \rho_k$ and $\|v\|_\infty \approx \sqrt{m_k}/\sqrt{2\pi}$. The vector that maximizes $\langle u, v\rangle$ is $v = P_k u / \rho_k$, which has $\|v\|_\infty = \|P_k u\|_\infty / \rho_k$. And the vector that maximizes $\|v\|_\infty$ is the flat vector, which has $\langle u, v\rangle = \frac{1}{\sqrt{m_k}} \sum a_n$.

These are generally different vectors, so we can't simultaneously achieve both maxima. But we can try to find a vector that does well on both.

Actually, let me think about this more carefully. The maximum of $|\langle u, v\rangle| \|v\|_\infty$ over unit vectors $v$ in the block is a well-defined optimization problem. Let me think about what happens.

Write $v = \sum_{n \in B_k} c_n e_n$ with $\sum |c_n|^2 = 1$. Then $\langle u, v\rangle = \sum_{n \in B_k} a_n \overline{c_n}$ and $\|v\|_\infty = \sup_x |\sum_{n \in B_k} c_n e_n(x)|/\sqrt{2\pi}$... wait, $\|v\|_\infty = \sup_x |\sum c_n e^{inx}/\sqrt{2\pi}| = \frac{1}{\sqrt{2\pi}} \sup_x |\sum c_n e^{inx}|$.

Hmm, this is getting complicated. Let me try a completely different approach.

Alternative approach: Instead of trying to make the partial sums diverge, let me think about whether the answer to the question is yes or no.

I recall that there's a classical result that for any orthonormal basis of $L^2$, the Fourier series of an $L^2$ function converges in $L^2$. But uniform convergence is not guaranteed.

In fact, I believe the answer is YES — such a smooth function and orthonormal basis exist. This is related to the fact that there's no orthonormal basis that's an "unconditional basis" for $C(S^1)$ (or for the space of smooth functions with uniform norm).

Actually, let me think about this more carefully. The question is asking about a specific $u$ and a specific basis, not about all $u$ for a given basis.

Let me think about the problem from the perspective of functional analysis.

The partial sum operator $S_N: L^2 \to L^2$ is the orthogonal projection onto $\text{span}\{u_1, \ldots, u_N\}$. For uniform convergence of the series for a specific $u$, we need $S_N u \to u$ in $L^\infty$.

The operator norm $\|S_N\|_{L^\infty \to L^\infty}$ can be large. If we can find a basis where $\|S_N\|_{L^\infty \to L^\infty}$ is unbounded, then by the uniform boundedness principle, there exists $u \in C(S^1)$ (even smooth, since smooth functions are dense) such that $S_N u$ doesn't converge in $L^\infty$.

Wait, but the uniform boundedness principle gives us $u \in C(S^1)$, not necessarily smooth. However, since smooth functions are dense in $C(S^1)$, and the operators $S_N$ are continuous on $C(S^1)$ (are they? $S_N$ is a finite-rank operator, so it's continuous on any normed space), we can potentially find a smooth $u$.

Actually, let me think about this more carefully. The uniform boundedness principle says: if $\sup_N \|S_N\|_{X \to X} = \infty$ for a Banach space $X$, then there exists $u \in X$ such that $\sup_N \|S_N u\|_X = \infty$.

If $X = C(S^1)$ (continuous functions with sup norm), and $\sup_N \|S_N\|_{C \to C} = \infty$, then there exists $u \in C(S^1)$ with $\sup_N \|S_N u\|_\infty = \infty$, so the series doesn't converge uniformly.

But we need $u$ to be smooth. The issue is that the UBP gives us $u \in C(S^1)$, not smooth.

However, we can use a stronger argument. If the operators $S_N$ are unbounded on $C(S^1)$, we can find a smooth $u$ as follows:

Consider the restriction of $S_N$ to $C^\infty(S^1)$. The space $C^\infty(S^1)$ with the sup norm is not complete (its completion is $C(S^1)$), but we can still apply a version of the UBP argument.

Actually, a cleaner approach: $C^\infty(S^1)$ is a Fréchet space (with the topology of uniform convergence of all derivatives). The operators $S_N$ are continuous on this Fréchet space. If $\sup_N \|S_N u\|_\infty < \infty$ for all smooth $u$, then by the uniform boundedness principle for Fréchet spaces, $\sup_N \|S_N\|_{C^\infty \to L^\infty} < \infty$ (where the operator norm is with respect to some continuous seminorm on $C^\infty$). 

Hmm, this is getting into functional analysis territory. Let me think about whether there's a more direct construction.

Actually, let me reconsider the direct construction approach, but with a better choice of $u$ and basis.

The key issue before was that for a smooth function, the coefficients decay too fast. But what if I choose the blocks to be at LOW frequencies, not high frequencies?

Wait, but there are only finitely many low frequencies. The blocks need to cover all positive integers, so most blocks are at high frequencies.

Let me reconsider. Maybe I should use a different type of basis element, not just rotations within frequency blocks.

Actually, here's another idea. What if the orthonormal basis is not related to the Fourier basis at all? We can take any complete orthonormal system of smooth functions.

Let me think about the following construction. Take a sequence of smooth functions $\phi_1, \phi_2, \ldots$ that are orthonormal in $L^2$ and have $\|\phi_n\|_\infty \to \infty$. Then for $u = \phi_1$ (say), the Fourier series is $u = \sum \langle u, \phi_n\rangle \phi_n = \|\phi_1\|_{L^2}^2 \phi_1 / \|\phi_1\|_{L^2}^2$... wait, if $\phi_1$ is already normalized, then $\langle u, \phi_1\rangle = 1$ and $\langle u, \phi_n\rangle = 0$ for $n > 1$. So the series is just $\phi_1$, which converges trivially.

That doesn't work because $u$ being a basis element means the series terminates.

Let me think about this differently. I want $u$ to have nonzero inner products with many basis elements, and the partial sums to be large.

Here's an idea based on the "gliding hump" or "sliding hump" technique:

Construct the orthonormal basis $\{u_n\}$ and the function $u$ simultaneously, inductively. At each step, ensure that a partial sum is large.

Let me think about this more carefully.

Actually, let me go back to the block rotation approach but think about it differently.

The issue was that for a smooth function with coefficients $a_n = e^{-n^\alpha}$, the "mass" $\rho_k$ in a block at frequency $N_k$ is too small. But what if I choose $u$ to have coefficients that don't decay as a function of $n$, but instead have the mass concentrated in specific blocks?

Wait, but $u$ needs to be smooth, so $a_n$ must decay faster than any polynomial. However, I can choose which frequencies have large coefficients and which have small ones, as long as the overall decay is faster than polynomial.

Here's the key idea: Choose $u$ such that its coefficients are large at the frequencies $N_k$ (the start of each block) and small elsewhere. Specifically, let $a_{N_k} = 1/k^2$ (or some slowly decaying sequence) and $a_n = 0$ for $n \neq N_k$ (or very small). But wait, $a_n$ needs to decay faster than any polynomial in $n$ for $u$ to be smooth. If $a_{N_k} = 1/k^2$ and $N_k$ grows very fast, then $a_{N_k} = 1/k^2$ needs to be $o(N_k^{-p})$ for all $p$, i.e., $k^2 \gg N_k^p$ for all $p$, i.e., $N_k \ll k^{2/p}$ for all $p$, which means $N_k$ must be bounded. Contradiction.

So I can't have $a_{N_k}$ decaying only polynomially in $k$ if $N_k \to \infty$.

OK so the constraint is: $a_n$ must decay faster than any polynomial in $n$. If I want $a_{N_k}$ to be "large", I need $N_k$ to be not too large relative to $a_{N_k}$.

Let me try $a_{N_k} = e^{-\sqrt{N_k}}$ (which is faster than any polynomial decay). Then $u$ is smooth (since $e^{-\sqrt{n}}$ decays faster than any polynomial). And I want the partial sums to diverge.

With the block approach, the sup norm of the $w_k$ contribution is $\sim \frac{1}{\sqrt{2\pi}} |\sum_{n \in B_k} a_n|$. If $a_n$ is concentrated at $N_k$ (i.e., $a_n \approx 0$ for $n \in B_k \setminus \{N_k\}$), then $\sum_{n \in B_k} a_n \approx a_{N_k} = e^{-\sqrt{N_k}}$, which goes to 0.

So the sup norm goes to 0, and the partial sums converge. Not helpful.

Hmm. It seems like for any smooth function, the coefficients decay too fast for the block approach to work.

Let me reconsider. Maybe the answer is NO — for any orthonormal basis of smooth functions and any smooth $u$, the generalized Fourier series converges uniformly?

That doesn't sound right either. Let me think about what's known.

Actually, I think the answer is YES, such a function and basis exist. Let me think about why.

The key insight might be that we should not restrict to bases that are "frequency-organized." We can use an arbitrary orthonormal basis of smooth functions.

Here's a different approach. Consider the following:

Let $\{e_n\}$ be the standard Fourier basis. Define a new orthonormal basis by applying a unitary operator $U$ on $L^2(S^1)$ that maps smooth functions to smooth functions but doesn't preserve uniform convergence of Fourier series.

If $U$ is a unitary operator that preserves $C^\infty(S^1)$ (i.e., $U$ and $U^{-1}$ map smooth functions to smooth functions), then $\{Ue_n\}$ is an orthonormal basis of smooth functions. The generalized Fourier series of $u$ in this basis is $\sum \langle u, Ue_n\rangle Ue_n = U \sum \langle U^{-1}u, e_n\rangle e_n = U(S_N^{std}(U^{-1}u))$ where $S_N^{std}$ is the standard Fourier partial sum.

So the partial sums in the new basis are $U(S_N^{std}(U^{-1}u))$. For this to converge uniformly to $u = U(U^{-1}u)$, we need $S_N^{std}(U^{-1}u) \to U^{-1}u$ uniformly AND $U$ to be continuous in sup norm.

If $U$ is not continuous in sup norm (i.e., $\|U\|_{L^\infty \to L^\infty} = \infty$), then even though $S_N^{std}(U^{-1}u) \to U^{-1}u$ uniformly (since $U^{-1}u$ is smooth), the images $U(S_N^{std}(U^{-1}u))$ might not converge uniformly.

But wait, $S_N^{std}(U^{-1}u) \to U^{-1}u$ uniformly means $\|S_N^{std}(U^{-1}u) - U^{-1}u\|_\infty \to 0$. Then $U(S_N^{std}(U^{-1}u)) - U(U^{-1}u) = U(S_N^{std}(U^{-1}u) - U^{-1}u)$. If $U$ is unbounded on $L^\infty$, the norm $\|U(S_N^{std}(U^{-1}u) - U^{-1}u)\|_\infty$ might not go to 0 even though $\|S_N^{std}(U^{-1}u) - U^{-1}u\|_\infty \to 0$.

But this requires that $U^{-1}u - S_N^{std}(U^{-1}u)$ is not in the kernel of $U$'s "blow-up" and that $U$ amplifies these specific errors.

This is getting abstract. Let me think of a concrete unitary operator.

Hmm, actually, a unitary operator on $L^2$ that preserves smooth functions but is unbounded on $L^\infty$... 

One example: a "permutation" of the Fourier basis that doesn't respect frequency. But a permutation of basis elements is unitary and preserves smoothness (since each basis element is smooth, and the permuted basis is still a basis of smooth functions). But a permutation doesn't change the partial sums in a useful way — it just reorders them.

Wait, actually, a permutation of the Fourier basis DOES change the partial sums! The standard Fourier partial sum $S_N$ projects onto the first $N$ frequencies, but a permuted basis projects onto an arbitrary set of $N$ frequencies.

But for a smooth function, the standard Fourier series converges absolutely ($\sum |a_n| < \infty$), so any rearrangement also converges absolutely and uniformly. So permutations don't help.

OK so the issue is that for smooth functions, the standard Fourier series converges absolutely, which makes it robust under rearrangements. We need something more drastic than permutation.

Let me go back to the block rotation idea, but think about it more carefully.

The block rotation changes the partial sums WITHIN a block. The partial sum at the end of a block is the same as the standard Fourier partial sum (projection onto the block's span is invariant). But intermediate partial sums within a block can be different.

For a smooth function, the standard Fourier series converges absolutely and uniformly. The partial sums at block boundaries converge uniformly to $u$. The question is whether the intermediate partial sums (within blocks) can diverge.

The intermediate partial sum within block $B_k$ after including $J$ of the $m_k$ rotated basis elements is:

$$S = \text{(standard partial sum up to } N_k - 1) + \sum_{j=1}^{J} \langle u, v_{k,j}\rangle v_{k,j}$$

where $v_{k,1}, \ldots, v_{k,m_k}$ is the rotated basis for block $B_k$.

The "error" from the standard partial sum at the end of the block is:

$$\sum_{j=1}^{J} \langle u, v_{k,j}\rangle v_{k,j} - P_k u = -\sum_{j=J+1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}$$

So the intermediate partial sum equals the standard partial sum at the end of the block minus the "remaining" terms. The sup norm of the remaining terms is $\|\sum_{j=J+1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}\|_\infty$.

This is the projection of $P_k u$ onto the span of $\{v_{k,J+1}, \ldots, v_{k,m_k}\}$, which is a subspace of dimension $m_k - J$ within the block.

The maximum sup norm of such a projection (over all choices of subspace and $J$) is bounded by $\|P_k u\|_\infty \cdot$ (some factor related to the basis).

Hmm, actually, the projection of $P_k u$ onto any subspace of the block has $L^2$ norm at most $\|P_k u\|_{L^2} = \rho_k$. And the sup norm is at most $\sqrt{m_k} \rho_k / \sqrt{2\pi}$ (by Cauchy-Schwarz, since any unit vector in the block has sup norm at most $\sqrt{m_k}/\sqrt{2\pi}$).

Wait, more precisely: the projection $Q$ of $P_k u$ onto a $d$-dimensional subspace is $Q = \sum_{j \in J} \langle u, v_j\rangle v_j$ where $|J| = d$. We have $\|Q\|_{L^2} \leq \rho_k$ and $Q$ is a trigonometric polynomial of degree $\leq N_k + m_k$. So $\|Q\|_\infty \leq \sqrt{m_k} \|Q\|_{L^2} / \sqrt{2\pi} \leq \sqrt{m_k} \rho_k / \sqrt{2\pi}$... 

Hmm wait, that's not right. $Q$ is in the span of $m_k$ basis elements (the block), so $\|Q\|_\infty \leq \sqrt{m_k} \|Q\|_{L^2}$... no, that's not right either. The correct bound is: if $Q = \sum_{n \in B_k} c_n e_n$, then $\|Q\|_\infty \leq \sum |c_n| \|e_n\|_\infty = \frac{1}{\sqrt{2\pi}} \sum |c_n| \leq \frac{\sqrt{m_k}}{\sqrt{2\pi}} (\sum |c_n|^2)^{1/2} = \frac{\sqrt{m_k}}{\sqrt{2\pi}} \|Q\|_{L^2}$.

So $\|Q\|_\infty \leq \frac{\sqrt{m_k}}{\sqrt{2\pi}} \rho_k$.

Now, $\rho_k = (\sum_{n \in B_k} |a_n|^2)^{1/2}$. For a smooth function, $|a_n| \leq C_p n^{-p}$ for all $p$. If the block is at frequency $N_k$ with size $m_k$, then $\rho_k \leq C_p m_k^{1/2} N_k^{-p}$.

So $\|Q\|_\infty \leq \frac{m_k}{\sqrt{2\pi}} C_p N_k^{-p}$.

For this to diverge, we need $m_k N_k^{-p} \to \infty$ for some fixed $p$. But since $u$ is smooth, this must hold for ALL $p$, so we need $m_k N_k^{-p} \to \infty$ for all $p$, i.e., $m_k \gg N_k^p$ for all $p$, i.e., $m_k$ grows faster than any polynomial in $N_k$.

But $N_{k+1} = N_k + m_k$, so if $m_k \gg N_k^p$ for all $p$, then $N_{k+1} \approx m_k \gg N_k^p$ for all $p$, meaning $N_k$ grows faster than any iterated exponential. This is fine in principle — there's no constraint on how fast $N_k$ grows.

But we also need $u$ to be in $L^2$, i.e., $\sum |a_n|^2 < \infty$. And $u$ smooth, i.e., $\sum n^{2p} |a_n|^2 < \infty$ for all $p$.

If $a_n \leq C_p n^{-p}$ for all $p$, and the blocks are at $N_k$ with $N_k$ growing super fast, then the contribution of block $B_k$ to $\sum n^{2p} |a_n|^2$ is $\sum_{n \in B_k} n^{2p} |a_n|^2 \leq m_k (N_k + m_k)^{2p} C_p^2 (N_k)^{-2q}$ for any $q$ (using $|a_n| \leq C_q n^{-q}$).

Hmm, this is getting complicated. Let me try to be very concrete.

Let me choose $u$ with $a_n = e^{-\sqrt{n}}$ (for $n \geq 1$). This is smooth (decays faster than any polynomial). And $\sum |a_n|^2 = \sum e^{-2\sqrt{n}} < \infty$ (converges since $e^{-2\sqrt{n}}$ decays faster than $1/n^2$).

Now, $\rho_k = (\sum_{n \in B_k} e^{-2\sqrt{n}})^{1/2}$. For a block at $N_k$ with size $m_k$ (where $m_k \ll N_k$ so that $\sqrt{n} \approx \sqrt{N_k}$ for $n \in B_k$), $\rho_k \approx \sqrt{m_k} e^{-\sqrt{N_k}}$.

The sup norm of the "remaining" projection is at most $\frac{\sqrt{m_k}}{\sqrt{2\pi}} \rho_k \approx \frac{m_k e^{-\sqrt{N_k}}}{\sqrt{2\pi}}$.

For this to diverge, we need $m_k e^{-\sqrt{N_k}} \to \infty$, i.e., $\log m_k > \sqrt{N_k}$, i.e., $m_k > e^{\sqrt{N_k}}$.

But we also need $m_k \ll N_k$ for the approximation $\sqrt{n} \approx \sqrt{N_k}$. This requires $e^{\sqrt{N_k}} \ll N_k$, which is false for large $N_k$.

If $m_k \sim e^{\sqrt{N_k}}$, then for $n$ near $N_k + m_k$, $\sqrt{n} \approx \sqrt{m_k} = e^{\sqrt{N_k}/2}$, so $a_n \approx e^{-e^{\sqrt{N_k}/2}}$, which is tiny. The sum $\sum_{n \in B_k} e^{-2\sqrt{n}}$ is dominated by the terms near $N_k$:

$\sum_{n=N_k}^{N_k+m_k-1} e^{-2\sqrt{n}} \approx \sum_{n=N_k}^{\infty} e^{-2\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-2\sqrt{x}} dx = \int_{\sqrt{N_k}}^{\infty} 2t e^{-2t} dt \approx \sqrt{N_k} e^{-2\sqrt{N_k}}$ (by integration by parts).

So $\rho_k \approx N_k^{1/4} e^{-\sqrt{N_k}}$.

And the sup norm bound is $\frac{\sqrt{m_k}}{\sqrt{2\pi}} \rho_k \approx \frac{e^{\sqrt{N_k}/2}}{\sqrt{2\pi}} N_k^{1/4} e^{-\sqrt{N_k}} = \frac{N_k^{1/4} e^{-\sqrt{N_k}/2}}{\sqrt{2\pi}} \to 0$.

So even with $m_k \sim e^{\sqrt{N_k}}$, the sup norm goes to 0. The problem is that the $L^2$ mass $\rho_k$ decays as $e^{-\sqrt{N_k}}$, and even though we can amplify by $\sqrt{m_k} \sim e^{\sqrt{N_k}/2}$, the product still decays.

The fundamental issue: $\rho_k \sim e^{-\sqrt{N_k}}$ and the amplification factor is $\sqrt{m_k}$, but $m_k$ can't be larger than $\sim e^{2\sqrt{N_k}}$ (because beyond that, the block captures all remaining mass and $\rho_k$ saturates). At $m_k \sim e^{2\sqrt{N_k}}$, $\rho_k \sim N_k^{1/4} e^{-\sqrt{N_k}}$ and amplification $\sim e^{\sqrt{N_k}}$, giving product $\sim N_k^{1/4}$, which diverges!

Wait, let me recheck. If $m_k \sim e^{2\sqrt{N_k}}$, then the block goes from $N_k$ to $N_k + e^{2\sqrt{N_k}}$. For $n$ near the end of the block, $\sqrt{n} \approx \sqrt{e^{2\sqrt{N_k}}} = e^{\sqrt{N_k}}$, so $a_n \approx e^{-e^{\sqrt{N_k}}}$, which is super tiny. So the sum $\sum_{n \in B_k} e^{-2\sqrt{n}}$ is still dominated by terms near $N_k$:

$\sum_{n=N_k}^{N_k + m_k} e^{-2\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-2\sqrt{x}} dx \approx \sqrt{N_k} e^{-2\sqrt{N_k}}$.

So $\rho_k \approx N_k^{1/4} e^{-\sqrt{N_k}}$.

And $\sqrt{m_k} \approx e^{\sqrt{N_k}}$.

Product: $\sqrt{m_k} \rho_k \approx e^{\sqrt{N_k}} \cdot N_k^{1/4} e^{-\sqrt{N_k}} = N_k^{1/4} \to \infty$.

So the sup norm of the "remaining" projection can be as large as $\sim N_k^{1/4} / \sqrt{2\pi} \to \infty$!

But wait, this is an upper bound. Can we actually achieve this? The bound $\|Q\|_\infty \leq \frac{\sqrt{m_k}}{\sqrt{2\pi}} \|Q\|_{L^2}$ is achieved when $Q$ is proportional to the flat vector $\sum_{n \in B_k} e_n$. But $Q$ is a projection of $P_k u$, so $Q$ is determined by the choice of subspace.

Let me think about this. We want to choose a subspace $V \subset \text{span}\{e_n : n \in B_k\}$ such that the projection of $P_k u$ onto $V$ has large sup norm.

$P_k u = \sum_{n \in B_k} a_n e_n$ where $a_n = e^{-\sqrt{n}}$. The mass is concentrated near $n = N_k$ (since $a_n$ decays). So $P_k u \approx a_{N_k} \sum_{j=0}^{J} e^{-(\sqrt{N_k+j} - \sqrt{N_k})} e_{N_k+j}$ where $J$ is such that $\sqrt{N_k + J} - \sqrt{N_k} \sim 1$, i.e., $J \sim \sqrt{N_k}$.

So $P_k u$ is essentially supported on $\sim \sqrt{N_k}$ basis elements near $N_k$, with $L^2$ norm $\rho_k \sim N_k^{1/4} e^{-\sqrt{N_k}}$.

Now, the flat vector $w = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ has $\|w\|_\infty = \frac{\sqrt{m_k}}{\sqrt{2\pi}} \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2\pi}}$. The projection of $P_k u$ onto $w$ is $\langle P_k u, w\rangle w = \frac{1}{\sqrt{m_k}} (\sum_{n \in B_k} a_n) w$.

$\sum_{n \in B_k} a_n \approx \sum_{n=N_k}^{\infty} e^{-\sqrt{n}} \approx \sqrt{N_k} e^{-\sqrt{N_k}}$ (similar calculation).

So $\langle P_k u, w\rangle = \frac{\sqrt{N_k} e^{-\sqrt{N_k}}}{\sqrt{m_k}} \approx \frac{\sqrt{N_k} e^{-\sqrt{N_k}}}{e^{\sqrt{N_k}}} = \sqrt{N_k} e^{-2\sqrt{N_k}}$.

And $\|\langle P_k u, w\rangle w\|_\infty = |\langle P_k u, w\rangle| \|w\|_\infty \approx \sqrt{N_k} e^{-2\sqrt{N_k}} \cdot e^{\sqrt{N_k}} / \sqrt{2\pi} = \sqrt{N_k} e^{-\sqrt{N_k}} / \sqrt{2\pi} \to 0$.

So projecting onto the flat vector doesn't work because $\langle P_k u, w\rangle$ is too small (the flat vector has components at all frequencies in the block, but $P_k u$ is concentrated near $N_k$).

Instead, I should project onto a subspace that aligns with $P_k u$ but has large sup norm. 

The optimal strategy: choose $v$ to be a unit vector in the block that maximizes $|\langle P_k u, v\rangle| \|v\|_\infty$.

$P_k u$ is concentrated on $\sim \sqrt{N_k}$ basis elements near $N_k$. Let's say $P_k u \approx \rho_k \cdot \psi$ where $\psi$ is a unit vector supported on $\sim \sqrt{N_k}$ basis elements. Then $\|P_k u\|_\infty \approx \rho_k \|\psi\|_\infty \approx N_k^{1/4} e^{-\sqrt{N_k}} \cdot \frac{\sqrt{\sqrt{N_k}}}{\sqrt{2\pi}} = \frac{N_k^{1/2} e^{-\sqrt{N_k}}}{\sqrt{2\pi}}$ (since $\psi$ is supported on $\sqrt{N_k}$ basis elements, its sup norm is $\sim N_k^{1/4}/\sqrt{2\pi}$).

Now, I want to find a unit vector $v$ in the full block (of size $m_k \sim e^{2\sqrt{N_k}}$) such that $|\langle P_k u, v\rangle| \|v\|_\infty$ is large.

$|\langle P_k u, v\rangle| = \rho_k |\langle \psi, v\rangle| \leq \rho_k$ (since $\|v\| = 1$). Equality when $v = \psi$, but then $\|v\|_\infty = \|\psi\|_\infty \sim N_k^{1/4}/\sqrt{2\pi}$, giving product $\sim \rho_k N_k^{1/4} = N_k^{1/2} e^{-\sqrt{N_k}} \to 0$.

Alternatively, $v$ could be the flat vector, giving $|\langle \psi, v\rangle| \sim \sqrt{\sqrt{N_k}/m_k} = N_k^{1/4}/e^{\sqrt{N_k}}$ and $\|v\|_\infty \sim e^{\sqrt{N_k}}/\sqrt{2\pi}$, product $\sim \rho_k \cdot N_k^{1/4}/e^{\sqrt{N_k}} \cdot e^{\sqrt{N_k}} = \rho_k N_k^{1/4} = N_k^{1/2} e^{-\sqrt{N_k}} \to 0$.

Hmm, in both cases the product goes to 0. The issue is that $\rho_k \sim N_k^{1/4} e^{-\sqrt{N_k}}$ decays too fast.

Let me try to optimize. We want to maximize $|\langle P_k u, v\rangle| \|v\|_\infty$ over unit vectors $v$ in the block. 

Write $v = \alpha \psi + \beta \phi$ where $\psi = P_k u / \rho_k$ (the "signal" direction) and $\phi$ is a unit vector orthogonal to $\psi$ in the block. Then $|\langle P_k u, v\rangle| = \rho_k |\alpha|$ and $\|v\|_\infty \leq |\alpha| \|\psi\|_\infty + |\beta| \|\phi\|_\infty$ (by triangle inequality).

With $|\alpha|^2 + |\beta|^2 = 1$, and $\|\phi\|_\infty \leq \sqrt{m_k}/\sqrt{2\pi}$ (max sup norm in the block), we get:

$|\langle P_k u, v\rangle| \|v\|_\infty \leq \rho_k |\alpha| (|\alpha| \|\psi\|_\infty + |\beta| \sqrt{m_k}/\sqrt{2\pi})$.

This is maximized (roughly) when $|\alpha| \sim \rho_k \|\psi\|_\infty / (\rho_k \|\psi\|_\infty + \rho_k \sqrt{m_k}/\sqrt{2\pi})$... hmm, let me just optimize.

Let $A = \|\psi\|_\infty \sim N_k^{1/4}/\sqrt{2\pi}$ and $B = \sqrt{m_k}/\sqrt{2\pi} \sim e^{\sqrt{N_k}}/\sqrt{2\pi}$.

We want to maximize $f(\alpha, \beta) = \rho_k |\alpha| (|\alpha| A + |\beta| B)$ subject to $\alpha^2 + \beta^2 = 1$.

Let $\alpha = \cos\theta$, $\beta = \sin\theta$. Then $f = \rho_k \cos\theta (\cos\theta \cdot A + \sin\theta \cdot B)$.

$\frac{df}{d\theta} = \rho_k [-\sin\theta(\cos\theta \cdot A + \sin\theta \cdot B) + \cos\theta(-\sin\theta \cdot A + \cos\theta \cdot B)]$
$= \rho_k [-\sin\theta\cos\theta A - \sin^2\theta B - \sin\theta\cos\theta A + \cos^2\theta B]$
$= \rho_k [-2\sin\theta\cos\theta A + (\cos^2\theta - \sin^2\theta) B]$
$= \rho_k [-\sin 2\theta \cdot A + \cos 2\theta \cdot B]$

Setting to 0: $\tan 2\theta = B/A$, so $2\theta \approx \pi/2$ (since $B \gg A$), $\theta \approx \pi/4$, $\alpha \approx \beta \approx 1/\sqrt{2}$.

Then $f \approx \rho_k \cdot \frac{1}{\sqrt{2}} \cdot (\frac{A}{\sqrt{2}} + \frac{B}{\sqrt{2}}) \approx \rho_k \cdot \frac{B}{2} \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}} \cdot e^{\sqrt{N_k}}}{2\sqrt{2\pi}} = \frac{N_k^{1/4}}{2\sqrt{2\pi}}$.

This diverges! So the maximum of $|\langle P_k u, v\rangle| \|v\|_\infty$ is $\sim N_k^{1/4} \to \infty$.

But wait, this is an upper bound using the triangle inequality. The actual sup norm of $v = \alpha\psi + \beta\phi$ might be less than $|\alpha| \|\psi\|_\infty + |\beta| \|\phi\|_\infty$ due to cancellation. Let me think about whether we can actually achieve this.

We need $\phi$ to be a unit vector orthogonal to $\psi$ with $\|\phi\|_\infty \sim \sqrt{m_k}/\sqrt{2\pi}$ and such that $\psi$ and $\phi$ achieve their sup norms at the same point (or nearly so).

$\psi$ is supported on $\sim \sqrt{N_k}$ basis elements near $N_k$ and has sup norm at $x = 0$ (say). $\phi$ should be the flat vector over the full block, which also has sup norm at $x = 0$. But $\phi$ needs to be orthogonal to $\psi$.

Let $\phi_0 = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (the flat vector). Then $\langle \psi, \phi_0\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} \langle \psi, e_n\rangle = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} \hat{\psi}(n)$. Since $\psi$ is supported on $\sim \sqrt{N_k}$ elements, $|\langle \psi, \phi_0\rangle| \leq \sqrt{\sqrt{N_k}/m_k} = N_k^{1/4}/\sqrt{m_k} \sim N_k^{1/4}/e^{\sqrt{N_k}} \to 0$.

So $\phi_0$ is nearly orthogonal to $\psi$. Let $\phi = \frac{\phi_0 - \langle \phi_0, \psi\rangle \psi}{\|\phi_0 - \langle \phi_0, \psi\rangle \psi\|}$. Then $\phi$ is a unit vector orthogonal to $\psi$, and $\phi \approx \phi_0$ (since $\langle \phi_0, \psi\rangle \to 0$). So $\|\phi\|_\infty \approx \|\phi_0\|_\infty \sim e^{\sqrt{N_k}}/\sqrt{2\pi}$.

Now, $v = \alpha \psi + \beta \phi$ with $\alpha = \beta = 1/\sqrt{2}$. At $x = 0$:
$v(0) = \alpha \psi(0) + \beta \phi(0) \approx \frac{1}{\sqrt{2}} (A\sqrt{2\pi} + B\sqrt{2\pi}) / \sqrt{2\pi}$... 

wait, let me be more careful. $\psi(0) = \|\psi\|_\infty$ (assuming the sup is at 0) and $\phi(0) \approx \phi_0(0) = \|\phi_0\|_\infty = \sqrt{m_k}/\sqrt{2\pi}$.

$v(0) = \frac{1}{\sqrt{2}} \psi(0) + \frac{1}{\sqrt{2}} \phi(0) \approx \frac{1}{\sqrt{2}} (N_k^{1/4}/\sqrt{2\pi} + e^{\sqrt{N_k}}/\sqrt{2\pi}) \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}}$.

And $\langle P_k u, v\rangle = \rho_k \alpha = \rho_k / \sqrt{2} \approx N_k^{1/4} e^{-\sqrt{N_k}} / \sqrt{2}$.

So $|\langle P_k u, v\rangle| |v(0)| \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}}}{\sqrt{2}} \cdot \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}} = \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$.

But this is $|\langle P_k u, v\rangle| |v(0)|$, not $\|v\|_\infty$. We need $\|v\|_\infty \geq |v(0)|$, which is true. And the partial sum contribution is $\langle u, v\rangle v = \langle P_k u, v\rangle v$ (since $u$'s projection onto the block is $P_k u$). The sup norm of this is $|\langle P_k u, v\rangle| \|v\|_\infty \geq |\langle P_k u, v\rangle| |v(0)| \sim N_k^{1/4} \to \infty$.

Wait, but I need to be more careful. The partial sum includes $\langle u, v\rangle v$ where $v$ is one of the new basis elements. But $v$ is a specific basis element, and the partial sum at that point includes all previous basis elements plus $v$.

Let me set up the construction more carefully.

Construction:
- $u(x) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} e_n(x)$ (smooth function on $S^1$, using only positive frequencies for simplicity; we can make it real-valued by also including negative frequencies, but let's keep it simple).
- Partition $\{1, 2, 3, \ldots\}$ into blocks $B_k = \{N_k, \ldots, N_k + m_k - 1\}$ with $m_k = \lceil e^{2\sqrt{N_k}} \rceil$ and $N_{k+1} = N_k + m_k$.
- Within each block, the first basis element is $v_k = \frac{1}{\sqrt{2}} \psi_k + \frac{1}{\sqrt{2}} \phi_k$ where $\psi_k = P_k u / \rho_k$ and $\phi_k$ is the (nearly) flat vector orthogonalized against $\psi_k$.
- The remaining $m_k - 1$ basis elements complete the orthonormal basis for the block.
- The new basis is ordered as: (negative frequency standard basis elements, $e_0$), $v_1$, (rest of block 1), $v_2$, (rest of block 2), ...

The partial sum of $u$ up to and including $v_k$ is:
$$S_k = \sum_{j=1}^{k-1} P_j u + \langle u, v_k\rangle v_k$$

$= \text{(standard Fourier partial sum up to } N_k - 1) + \langle P_k u, v_k\rangle v_k$

The standard Fourier partial sum converges uniformly to $u$ (since $u$ is smooth), so $\|\text{standard partial sum up to } N_k - 1\|_\infty \leq \|u\|_\infty + 1$ for large $k$.

And $\|\langle P_k u, v_k\rangle v_k\|_\infty \geq |\langle P_k u, v_k\rangle| |v_k(0)| \sim \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$.

But wait, I need to check that the partial sum $S_k$ actually has large sup norm, not just that the $v_k$ contribution does. The issue is that the standard partial sum and the $v_k$ contribution might cancel at $x = 0$.

At $x = 0$: $S_k(0) = \text{(standard partial sum at 0)} + \langle P_k u, v_k\rangle v_k(0)$.

The standard partial sum at 0 converges to $u(0)$, which is finite. And $\langle P_k u, v_k\rangle v_k(0) \sim \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$ (positive, since we can choose the sign of $v_k$ appropriately).

Actually, $\langle P_k u, v_k\rangle = \rho_k / \sqrt{2} > 0$ (real and positive). And $v_k(0) = \frac{1}{\sqrt{2}} \psi_k(0) + \frac{1}{\sqrt{2}} \phi_k(0)$. Both $\psi_k(0)$ and $\phi_k(0)$ are positive (they're sums of $e_n(0) = 1/\sqrt{2\pi}$ with positive coefficients). So $v_k(0) > 0$ and $\langle P_k u, v_k\rangle v_k(0) > 0$ and $\to \infty$.

Therefore $S_k(0) \to \infty$, so $\|S_k\|_\infty \to \infty$, and the series doesn't converge uniformly (in fact, the partial sums are unbounded).

Wait, I need to double-check that $\psi_k(0)$ and $\phi_k(0)$ are both positive and large.

$\psi_k = P_k u / \rho_k$. $P_k u = \sum_{n \in B_k} e^{-\sqrt{n}} e_n$. At $x = 0$, $P_k u(0) = \sum_{n \in B_k} e^{-\sqrt{n}} \cdot \frac{1}{\sqrt{2\pi}} > 0$. So $\psi_k(0) = P_k u(0) / \rho_k > 0$.

$\phi_k \approx \phi_{k,0} = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$. At $x = 0$, $\phi_{k,0}(0) = \frac{m_k}{\sqrt{m_k} \sqrt{2\pi}} = \frac{\sqrt{m_k}}{\sqrt{2\pi}} > 0$. And $\phi_k$ is a small perturbation of $\phi_{k,0}$, so $\phi_k(0) \approx \phi_{k,0}(0) > 0$.

So indeed $v_k(0) > 0$ and large, and $\langle P_k u, v_k\rangle v_k(0) \to \infty$.

Now, the standard partial sum at 0: $\sum_{n=1}^{N_k-1} e^{-\sqrt{n}} e_n(0) = \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{N_k-1} e^{-\sqrt{n}} \to \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{\infty} e^{-\sqrt{n}} = u(0)$, which is finite. So the standard partial sum at 0 is bounded.

Therefore $S_k(0) = \text{(bounded)} + \text{(something} \to +\infty) \to +\infty$.

This means the partial sums $S_k$ are unbounded, so the series doesn't converge uniformly. 

Now let me make sure all the details are right.

1. $u$ is smooth: $a_n = e^{-\sqrt{n}}$ decays faster than any polynomial, so $u \in C^\infty(S^1)$. ✓

2. The basis elements are smooth: each $v_k$ is a finite linear combination of $e_n$ (trigonometric polynomials), hence smooth. The other basis elements in each block are also finite linear combinations, hence smooth. The negative frequency basis elements $e_n$ for $n \leq 0$ are smooth. ✓

3. The basis is orthonormal: within each block, we apply an orthogonal transformation to the standard basis, preserving orthonormality. Across blocks, the basis elements are in orthogonal subspaces. ✓

4. The basis is complete: it spans the same space as the standard Fourier basis (we just rotated within blocks). ✓

5. The partial sums $S_k$ are unbounded: as shown above, $S_k(0) \to \infty$. ✓

Let me also verify the key estimate more carefully.

$\rho_k = \|P_k u\|_{L^2} = (\sum_{n=N_k}^{N_k+m_k-1} e^{-2\sqrt{n}})^{1/2}$.

With $m_k = \lceil e^{2\sqrt{N_k}} \rceil$, the block goes from $N_k$ to $N_k + e^{2\sqrt{N_k}}$. For $n$ in this range, $\sqrt{n}$ ranges from $\sqrt{N_k}$ to $\sqrt{N_k + e^{2\sqrt{N_k}}} \approx e^{\sqrt{N_k}}$ (for large $N_k$). So $e^{-2\sqrt{n}}$ ranges from $e^{-2\sqrt{N_k}}$ to $e^{-2e^{\sqrt{N_k}}}$, which is essentially 0 for the upper end.

The sum $\sum_{n=N_k}^{N_k+m_k-1} e^{-2\sqrt{n}} \approx \sum_{n=N_k}^{\infty} e^{-2\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-2\sqrt{x}} dx$.

$\int_{N_k}^{\infty} e^{-2\sqrt{x}} dx = \int_{\sqrt{N_k}}^{\infty} 2t e^{-2t} dt = [2t \cdot \frac{-e^{-2t}}{2}]_{\sqrt{N_k}}^{\infty} + \int_{\sqrt{N_k}}^{\infty} e^{-2t} dt = \sqrt{N_k} e^{-2\sqrt{N_k}} + \frac{e^{-2\sqrt{N_k}}}{2}$.

So $\sum_{n \in B_k} e^{-2\sqrt{n}} \approx \sqrt{N_k} e^{-2\sqrt{N_k}}$ and $\rho_k \approx N_k^{1/4} e^{-\sqrt{N_k}}$.

$\langle P_k u, v_k\rangle = \rho_k / \sqrt{2} \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}}}{\sqrt{2}}$.

$v_k(0) = \frac{1}{\sqrt{2}} \psi_k(0) + \frac{1}{\sqrt{2}} \phi_k(0)$.

$\psi_k(0) = \frac{P_k u(0)}{\rho_k} = \frac{\sum_{n \in B_k} e^{-\sqrt{n}} / \sqrt{2\pi}}{\rho_k}$.

$\sum_{n \in B_k} e^{-\sqrt{n}} \approx \int_{N_k}^{\infty} e^{-\sqrt{x}} dx = \int_{\sqrt{N_k}}^{\infty} 2t e^{-t} dt = 2\sqrt{N_k} e^{-\sqrt{N_k}} + 2e^{-\sqrt{N_k}} \approx 2\sqrt{N_k} e^{-\sqrt{N_k}}$.

So $\psi_k(0) \approx \frac{2\sqrt{N_k} e^{-\sqrt{N_k}} / \sqrt{2\pi}}{N_k^{1/4} e^{-\sqrt{N_k}}} = \frac{2 N_k^{1/4}}{\sqrt{2\pi}}$.

$\phi_k(0) \approx \phi_{k,0}(0) = \frac{\sqrt{m_k}}{\sqrt{2\pi}} \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2\pi}}$.

$v_k(0) \approx \frac{1}{\sqrt{2}} \cdot \frac{2N_k^{1/4}}{\sqrt{2\pi}} + \frac{1}{\sqrt{2}} \cdot \frac{e^{\sqrt{N_k}}}{\sqrt{2\pi}} \approx \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}}$ (dominated by the second term).

$\langle P_k u, v_k\rangle v_k(0) \approx \frac{N_k^{1/4} e^{-\sqrt{N_k}}}{\sqrt{2}} \cdot \frac{e^{\sqrt{N_k}}}{\sqrt{2}\sqrt{2\pi}} = \frac{N_k^{1/4}}{2\sqrt{2\pi}} \to \infty$. ✓

Great, so the construction works. Let me also verify that $N_k \to \infty$ (so that $N_k^{1/4} \to \infty$).

$N_1 = 1$, $m_1 = \lceil e^{2} \rceil = 8$ (approximately), $N_2 = 9$, $m_2 = \lceil e^{2\sqrt{9}} \rceil = \lceil e^6 \rceil \approx 403$, $N_3 \approx 412$, $m_3 = \lceil e^{2\sqrt{412}} \rceil \approx e^{40.6} \approx 2.3 \times 10^{17}$, ...

So $N_k$ grows very rapidly and $N_k \to \infty$. ✓

Now let me also make sure the construction of the orthonormal basis is valid. Within each block $B_k$ of size $m_k$, we need $m_k$ orthonormal vectors. We define $v_k$ as above, and then complete to an orthonormal basis of the block using Gram-Schmidt. All vectors are finite linear combinations of $e_n$ (trigonometric polynomials), hence smooth.

The full orthonormal basis of $L^2(S^1)$ is:
- $e_n$ for $n \leq 0$ (negative frequencies and constant)
- For each block $B_k$: $v_k, v_{k,2}, \ldots, v_{k,m_k}$ (orthonormal basis of the block)

This is a complete orthonormal basis of smooth functions. ✓

The generalized Fourier series of $u$ is $u = \sum_{n \leq 0} \langle u, e_n\rangle e_n + \sum_{k=1}^{\infty} \sum_{j=1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}$.

Since $u$ has only positive frequency components, $\langle u, e_n\rangle = 0$ for $n \leq 0$. So the series is $\sum_{k=1}^{\infty} \sum_{j=1}^{m_k} \langle u, v_{k,j}\rangle v_{k,j}$.

The partial sum up to $v_k$ (including all of blocks $1, \ldots, k-1$ and just $v_k$ from block $k$) is:
$S_k = \sum_{j=1}^{k-1} P_j u + \langle u, v_k\rangle v_k = \sum_{n=1}^{N_k-1} a_n e_n + \langle P_k u, v_k\rangle v_k$.

And $S_k(0) \to \infty$ as shown. ✓

So the answer is YES, such a smooth function and orthonormal basis exist.

Let me now write up the proof cleanly.

Actually, wait. Let me reconsider one thing. I need to make sure that $v_k$ is the FIRST element of block $k$ in the ordering. The ordering of the basis is: (all $e_n$ for $n \leq 0$), then $v_1, v_{1,2}, \ldots, v_{1,m_1}$, then $v_2, v_{2,2}, \ldots, v_{2,m_2}$, etc.

But there are infinitely many $e_n$ for $n \leq 0$. We can't put all of them before $v_1$. We need to interleave.

Actually, since $\langle u, e_n\rangle = 0$ for $n \leq 0$, the ordering of the $e_n$ for $n \leq 0$ doesn't affect the partial sums of $u$'s series. We can interleave them anywhere. For instance:

$e_0, v_1, v_{1,2}, \ldots, v_{1,m_1}, e_{-1}, v_2, v_{2,2}, \ldots, v_{2,m_2}, e_{-2}, v_3, \ldots$

Or we can just put one $e_{-k}$ between blocks. Since $\langle u, e_{-k}\rangle = 0$, these don't contribute to the partial sums.

Actually, to be fully rigorous, let me just define the ordering as: enumerate all basis elements in any order such that $v_k$ comes after all elements of blocks $1, \ldots, k-1$ and before all other elements of block $k$. The negative frequency elements can be placed anywhere (they don't contribute to $u$'s partial sums). For instance, place $e_{-k}$ right before $v_{k+1}$.

The key point is that the partial sum $S_k$ (up to and including $v_k$, but not the rest of block $k$) is well-defined and equals $\sum_{n=1}^{N_k-1} a_n e_n + \langle P_k u, v_k\rangle v_k$.

OK, I think the proof is solid. Let me also consider whether we need $u$ to be real-valued. The problem says "smooth function on $S^1$", which could be complex-valued. If we need real-valued, we can take $u(x) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} (e_n(x) + e_{-n}(x)) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} \cdot \frac{2\cos(nx)}{\sqrt{2\pi}}$, which is real-valued and smooth. The construction would need to be adapted slightly (using cosine/sine basis or working with paired frequencies), but the essential idea is the same.

For simplicity, let me present the proof with complex-valued functions (the problem doesn't specify real-valued).

Actually, let me reconsider whether I should present a cleaner version. The core idea is:

1. Choose $u$ smooth with coefficients $a_n = e^{-\sqrt{n}}$ (for $n \geq 1$).
2. Partition positive integers into blocks $B_k$ with $|B_k| = m_k \approx e^{2\sqrt{N_k}}$ where $N_k$ is the start of block $k$.
3. Within each block, choose the first basis element $v_k$ to be a combination of the "signal" direction $\psi_k = P_k u / \|P_k u\|$ and the "flat" direction $\phi_k$ (normalized sum of all $e_n$ in the block, orthogonalized against $\psi_k$).
4. The partial sum up to $v_k$ has $S_k(0) \to \infty$.

The key estimate is that $\|P_k u\|_{L^2} \cdot \|\phi_k\|_\infty \sim N_k^{1/4} \to \infty$, which happens because:
- $\|P_k u\|_{L^2} \sim N_k^{1/4} e^{-\sqrt{N_k}}$ (the $L^2$ mass in the block)
- $\|\phi_k\|_\infty \sim e^{\sqrt{N_k}}$ (the sup norm of the flat vector in a block of size $e^{2\sqrt{N_k}}$)
- Product $\sim N_k^{1/4} \to \infty$

And by choosing $v_k$ to have components along both $\psi_k$ and $\phi_k$, we get $|\langle P_k u, v_k\rangle| |v_k(0)| \sim N_k^{1/4} \to \infty$.

Let me write this up now.

Hmm, actually, I realize I should double-check one more thing. The partial sum $S_k$ is the sum up to the $N_k$-th basis element (in the ordering), where $v_k$ is the last included element. But the index in the series $\sum_{n \in \mathbb{N}}$ is just a natural number indexing the basis. So the "partial sum" $S_N = \sum_{n=1}^{N} \langle u, u_n\rangle u_n$ for the $N$-th partial sum. We need to show that for some sequence $N \to \infty$, $\|S_N\|_\infty \not\to \|u\|_\infty$ (or more precisely, $S_N$ doesn't converge uniformly).

In our construction, the partial sums at the specific indices corresponding to "just after $v_k$" diverge. Since these indices go to infinity (as $k \to \infty$), the series doesn't converge uniformly.

OK, I'm confident the proof is correct. Let me write it up.

One more thing: I should verify that $u$ is indeed smooth. $u(x) = \sum_{n=1}^{\infty} e^{-\sqrt{n}} e^{inx}/\sqrt{2\pi}$. For $u$ to be $C^\infty$, we need $\sum n^{2p} e^{-2\sqrt{n}} < \infty$ for all $p \geq 0$. Since $e^{-2\sqrt{n}}$ decays faster than any polynomial (i.e., $n^{2p} e^{-2\sqrt{n}} \to 0$ faster than any power), and in fact $\sum n^{2p} e^{-2\sqrt{n}} < \infty$ (by comparison with, say, $\sum n^{2p} e^{-n}$ for large $n$, since $e^{-2\sqrt{n}} \leq e^{-n}$ for $n \geq 4$), this holds. ✓

Also, $u \in L^2$: $\sum e^{-2\sqrt{n}} < \infty$ since $e^{-2\sqrt{n}} \leq n^{-2}$ for large $n$. ✓

Let me write the proof now.

Actually, I realize I should be a bit more careful about the construction of $\phi_k$. Let me define things precisely.

Block $B_k = \{N_k, N_k+1, \ldots, N_k + m_k - 1\}$ where $m_k = \lceil e^{2\sqrt{N_k}} \rceil$ and $N_{k+1} = N_k + m_k$, $N_1 = 1$.

$P_k u = \sum_{n \in B_k} a_n e_n$ where $a_n = e^{-\sqrt{n}}$.

$\rho_k = \|P_k u\|_{L^2} = (\sum_{n \in B_k} |a_n|^2)^{1/2}$.

$\psi_k = P_k u / \rho_k$ (unit vector in the direction of $P_k u$).

$F_k = \frac{1}{\sqrt{m_k}} \sum_{n \in B_k} e_n$ (flat unit vector).

$\phi_k = \frac{F_k - \langle F_k, \psi_k\rangle \psi_k}{\|F_k - \langle F_k, \psi_k\rangle \psi_k\|}$ (flat vector orthogonalized against $\psi_k$).

$v_k = \frac{1}{\sqrt{2}} (\psi_k + \phi_k)$.

Then $\|v_k\|_{L^2} = 1$ (since $\psi_k \perp \phi_k$ and both are unit vectors), and $v_k$ is a smooth function (trigonometric polynomial).

$\langle u, v_k\rangle = \langle P_k u, v_k\rangle = \rho_k \langle \psi_k, v_k\rangle = \rho_k / \sqrt{2}$.

The partial sum up to $v_k$:
$S_k = \sum_{n=1}^{N_k - 1} a_n e_n + \frac{\rho_k}{\sqrt{2}} v_k$

At $x = 0$:
$S_k(0) = \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{N_k-1} e^{-\sqrt{n}} + \frac{\rho_k}{\sqrt{2}} v_k(0)$

The first term converges to $u(0) = \frac{1}{\sqrt{2\pi}} \sum_{n=1}^{\infty} e^{-\sqrt{n}} < \infty$.

For the second term:
$v_k(0) = \frac{1}{\sqrt{2}} (\psi_k(0) + \phi_k(0))$

$\psi_k(0) = \frac{1}{\rho_k \sqrt{2\pi}} \sum_{n \in B_k} e^{-\sqrt{n}}$

$\phi_k(0) \geq F_k(0) - |\langle F_k, \psi_k\rangle| |\psi_k(0)|$ (by triangle inequality, since $\phi_k = (F_k - \langle F_k, \psi_k\rangle\psi_k)/\|\cdot\|$ and $\|\cdot\| \leq 1$)

Actually, let me be more careful. $\phi_k = \frac{F_k - c_k \psi_k}{\sqrt{1 - |c_k|^2}}$ where $c_k = \langle F_k, \psi_k\rangle$.

$\phi_k(0) = \frac{F_k(0) - c_k \psi_k(0)}{\sqrt{1 - |c_k|^2}}$.

$|c_k| = |\langle F_k, \psi_k\rangle| = \frac{|\langle F_k, P_k u\rangle|}{\rho_k} =
