# Degree of the Algebraic Closure over $\mathbb{Q}_p^{ext}$

## Problem

Determine the degree of extension of the algebraic closure over the field
$$\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p),$$
where $p$ is a prime number.

## Answer

$$\boxed{\aleph_0}$$

## Proof

The proof proceeds in two steps: (1) we show that $\mathbb{Q}_p^{ext} \cong \mathbb{Q}_p$, and (2) we show that $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = \aleph_0$.

---

### Step 1: $\mathbb{Q}_p^{ext} \cong \mathbb{Q}_p$

**The ring $\mathbb{Z}((X))_{conti}$.** The notation $\mathbb{Z}((X))_{conti}$ denotes the $p$-adic completion of the formal Laurent series ring $\mathbb{Z}((X))$. Concretely, completing the coefficient ring $\mathbb{Z}$ with respect to the $p$-adic topology yields $\mathbb{Z}_p$, and thus

$$\mathbb{Z}((X))_{conti} = \mathbb{Z}_p((X)) = \mathbb{Z}_p[[X]][X^{-1}],$$

the ring of formal Laurent series with coefficients in $\mathbb{Z}_p$.

**The evaluation map.** Define the ring homomorphism
$$\phi: \mathbb{Z}_p((X)) \longrightarrow \mathbb{Q}_p, \qquad X \longmapsto p.$$
This is well-defined because for any $f = \sum_{n \geq n_0} a_n X^n \in \mathbb{Z}_p((X))$ with $a_n \in \mathbb{Z}_p$, the series $\sum_{n \geq n_0} a_n p^n$ converges in $\mathbb{Q}_p$: the tail satisfies $v_p(a_n p^n) \geq n \to +\infty$ as $n \to +\infty$ (since $v_p(a_n) \geq 0$), and the finitely many terms with $n < 0$ contribute elements of $p^{n_0}\mathbb{Z}_p \subset \mathbb{Q}_p$.

**Surjectivity of $\phi$.** Every element of $\mathbb{Z}_p$ is the image of a power series in $\mathbb{Z}_p[[X]] \subset \mathbb{Z}_p((X))$: given $z = \sum_{n=0}^{\infty} b_n p^n$ with $b_n \in \{0,1,\ldots,p-1\} \subset \mathbb{Z}_p$, the series $\sum b_n X^n$ maps to $z$. Moreover, $\phi(X^{-1}) = p^{-1}$, so $p$ is invertible in the image. Since $\mathbb{Q}_p = \mathbb{Z}_p[1/p]$, the image of $\phi$ is all of $\mathbb{Q}_p$.

**The kernel is $(X-p)$.** We first show $\ker(\phi|_{\mathbb{Z}_p[[X]]}) = (X-p) \cdot \mathbb{Z}_p[[X]]$.

*$\supseteq$*: Clear, since $\phi(X - p) = p - p = 0$.

*$\subseteq$*: Let $f = \sum_{n \geq 0} a_n X^n \in \mathbb{Z}_p[[X]]$ with $\phi(f) = \sum a_n p^n = 0$. We perform a Taylor expansion of $f$ around $X = p$. Writing $X = (X-p) + p$ and expanding:

$$f = \sum_{n \geq 0} a_n \bigl((X-p)+p\bigr)^n = \sum_{k \geq 0} (X-p)^k \underbrace{\left(\sum_{n \geq k} a_n \binom{n}{k} p^{n-k}\right)}_{=:\, c_k}.$$

Each coefficient $c_k = \sum_{n \geq k} a_n \binom{n}{k} p^{n-k}$ is a well-defined element of $\mathbb{Z}_p$, since each summand lies in $\mathbb{Z}_p$ and $v_p\!\left(a_n \binom{n}{k} p^{n-k}\right) \geq n - k \to +\infty$ as $n \to \infty$, ensuring $p$-adic convergence.

The constant term is $c_0 = \sum_{n \geq 0} a_n p^n = \phi(f) = 0$. Therefore

$$f = (X-p) \sum_{k \geq 1} c_k (X-p)^{k-1} = (X-p) \cdot g,$$

where $g = \sum_{j \geq 0} c_{j+1}(X-p)^j$. We verify $g \in \mathbb{Z}_p[[X]]$: expanding each $(X-p)^j$ back in powers of $X$, the coefficient of $X^i$ in $g$ is $\sum_{j \geq i} c_{j+1}\binom{j}{i}(-p)^{j-i}$, which converges in $\mathbb{Z}_p$ (each summand has $p$-adic valuation $\geq j - i \to +\infty$). Hence $g \in \mathbb{Z}_p[[X]]$ and $f \in (X-p)\cdot\mathbb{Z}_p[[X]]$.

**Extension to $\mathbb{Z}_p((X))$.** Since $\mathbb{Z}_p((X)) = \mathbb{Z}_p[[X]][X^{-1}]$ and $\phi(X) = p$ is a unit in $\mathbb{Q}_p$, the kernel of $\phi$ on $\mathbb{Z}_p((X))$ is the localization of $(X-p)\cdot\mathbb{Z}_p[[X]]$, which is $(X-p)\cdot\mathbb{Z}_p((X))$.

**Conclusion.** By the first isomorphism theorem,

$$\mathbb{Q}_p^{ext} = \mathbb{Z}((X))_{conti}/(X-p) = \mathbb{Z}_p((X))/(X-p) \cong \mathbb{Q}_p.$$

---

### Step 2: $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = \aleph_0$

By Step 1, $\mathbb{Q}_p^{ext} \cong \mathbb{Q}_p$, so we must compute $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p]$.

**Lower bound: $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] \geq \aleph_0$.**

Consider the cyclotomic tower. For $p$ odd, let $\zeta_{p^n}$ denote a primitive $p^n$-th root of unity. The extension $\mathbb{Q}_p(\zeta_{p^n})/\mathbb{Q}_p$ is totally ramified of degree

$$[\mathbb{Q}_p(\zeta_{p^n}) : \mathbb{Q}_p] = \varphi(p^n) = (p-1)p^{n-1}.$$

(For $p = 2$, one may use $\mathbb{Q}_2(\zeta_{2^n})$ for $n \geq 2$, which has degree $2^{n-2}$, or alternatively use unramified extensions $\mathbb{Q}_p(\mu_{q})$ of degree $f$ for arbitrary $f$.)

These extensions form a tower:
$$\mathbb{Q}_p \subset \mathbb{Q}_p(\zeta_p) \subset \mathbb{Q}_p(\zeta_{p^2}) \subset \mathbb{Q}_p(\zeta_{p^3}) \subset \cdots$$

since $\zeta_{p^n} = \zeta_{p^{n+1}}^p$. The degrees $(p-1)p^{n-1} \to \infty$ as $n \to \infty$, so

$$[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] \geq \sup_{n} [\mathbb{Q}_p(\zeta_{p^n}) : \mathbb{Q}_p] = \aleph_0.$$

**Upper bound: $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] \leq \aleph_0$.**

By **Krasner's theorem**, for each positive integer $d$, there are only finitely many extensions of $\mathbb{Q}_p$ of degree $d$ (up to $\mathbb{Q}_p$-isomorphism). This is a fundamental finiteness result for local fields: the number of degree-$d$ extensions of $\mathbb{Q}_p$ is bounded by a function of $d$ and $p$.

Since there are finitely many extensions of each degree $d \in \mathbb{N}$, the total number of finite extensions of $\mathbb{Q}_p$ (up to isomorphism) is countable:

$$\{\text{finite extensions of } \mathbb{Q}_p\} = \bigcup_{d=1}^{\infty} \{\text{extensions of degree } d\},$$

a countable union of finite sets.

The algebraic closure is the directed union:
$$\overline{\mathbb{Q}_p} = \bigcup_{K/\mathbb{Q}_p \text{ finite}} K.$$

From the countable family of finite extensions, we can extract a countable $\mathbb{Q}_p$-basis for $\overline{\mathbb{Q}_p}$: enumerate the finite extensions as $K_1, K_2, K_3, \ldots$, and for each $K_i$, choose a finite $\mathbb{Q}_p$-basis $B_i$. The union $B = \bigcup_i B_i$ is a countable set that spans $\overline{\mathbb{Q}_p}$ over $\mathbb{Q}_p$ (since every element of $\overline{\mathbb{Q}_p}$ lies in some $K_i$ and is thus a $\mathbb{Q}_p$-linear combination of $B_i \subseteq B$). Extracting a maximal linearly independent subset of $B$ yields a $\mathbb{Q}_p$-basis of $\overline{\mathbb{Q}_p}$ of cardinality at most $|B| = \aleph_0$.

Therefore $[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] \leq \aleph_0$.

**Combining both bounds:**

$$[\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = \aleph_0.$$

---

### Final Result

Since $\mathbb{Q}_p^{ext} \cong \mathbb{Q}_p$, the degree of the algebraic closure over $\mathbb{Q}_p^{ext}$ equals the degree of the algebraic closure over $\mathbb{Q}_p$:

$$[\overline{\mathbb{Q}_p^{ext}} : \mathbb{Q}_p^{ext}] = [\overline{\mathbb{Q}_p} : \mathbb{Q}_p] = \boxed{\aleph_0}.$$
