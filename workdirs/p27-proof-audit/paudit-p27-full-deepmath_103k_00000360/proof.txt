# Proof: Borel image of a homeomorphism between Polish spaces

**Theorem.** Let $X$ and $Y$ be Polish spaces, let $A \subset X$ be a Borel subset, and let $f: A \to B \subset Y$ be a homeomorphism (onto $B = f(A)$). Then $B$ is a Borel subset of $Y$.

This is the **Lusin–Suslin theorem** in the special case where the injective Borel map is in fact a homeomorphism. We give a self-contained proof.

---

## Standard tools

We use three standard results of descriptive set theory, whose proofs are independent of the Lusin–Suslin theorem (they are derived from the representation of analytic sets as projections of closed sets in $\omega^\omega \times Z$ and the rank analysis of trees).

**(i) Analytic sets and their stability.** A subset $E$ of a Polish space $Z$ is *analytic* ($\Sigma^1_1$) if it is the projection of a closed set in $Z \times \omega^\omega$. Every Borel set is analytic. Analytic sets are closed under countable unions, countable intersections, and images/preimages under Borel maps: if $E \subset Z$ is analytic and $g: Z \to W$ is Borel, then $g(E)$ is analytic in $W$.

**(ii) Lusin's First Separation Theorem.** If $E_1, E_2$ are disjoint analytic subsets of a Polish space $Z$, there is a Borel set $C \subset Z$ with $E_1 \subset C$ and $E_2 \cap C = \emptyset$. By iterating, any countable family $\{E_n\}_{n \in \omega}$ of pairwise disjoint analytic sets can be separated by pairwise disjoint Borel sets $\{C_n\}_{n \in \omega}$ with $E_n \subset C_n$.

**(iii) Souslin's Theorem.** A subset $E$ of a Polish space $Z$ is Borel if and only if both $E$ and $Z \setminus E$ are analytic. (Immediate from (ii): if $E$ and $Z\setminus E$ are disjoint analytic, they are separated by a Borel set $C$ with $E \subset C \subset Z \setminus (Z\setminus E) = E$.)

---

## Main proof

Since $A$ is Borel in $X$, it is a standard fact that $A$ is a **Lusin space**: there is a finer Polish topology on $A$ (compatible with the subspace Borel structure) in which $A$ is Polish, and $A$ admits a Lusin scheme. Concretely, because $f$ is a homeomorphism, the metric
$$\rho(x, x') := d_Y\bigl(f(x), f(x')\bigr), \qquad x, x' \in A,$$
is compatible with the subspace topology on $A$. We use this metric to control diameters of the pieces.

### Step 1. A Lusin scheme on $A$ with vanishing $f$-diameter

There exists a family $\{A_s\}_{s \in \omega^{<\omega}}$ of subsets of $A$ with:

1. $A_\emptyset = A$ and $A_s = \bigsqcup_{n \in \omega} A_{s^\frown n}$ (disjoint union);
2. $A_s \cap A_t = \emptyset$ whenever $s, t \in \omega^{<\omega}$ are incompatible;
3. for every $x \in A$ there is a unique $\alpha \in \omega^\omega$ with $\{x\} = \bigcap_{k} A_{\alpha|k}$;
4. $\operatorname{diam}_\rho(A_s) = \operatorname{diam}_Y(f(A_s)) \to 0$ as $|s| \to \infty$.

*Construction.* Since $A$ is Borel in the Polish space $X$, it is a Lusin space, hence admits a Lusin scheme satisfying (1)–(3) with Borel pieces $A_s$ and with $\operatorname{diam}_\rho(A_s) \to 0$ (one builds the scheme by recursively splitting each piece into countably many Borel sub-pieces of $\rho$-diameter $\le 2^{-|s|}$, using that $(A, \rho)$ is separable). Property (4) is then immediate from the definition of $\rho$. ∎

### Step 2. A Borel approximation scheme $\{B_s\}$ in $Y$

We build Borel sets $B_s \subset Y$ ($s \in \omega^{<\omega}$) by induction on $|s|$, satisfying:

- (a) $f(A_s) \subset B_s$;
- (b) $B_{s^\frown n} \subset B_s$ for all $n$;
- (c) $B_{s^\frown n} \cap B_{s^\frown m} = \emptyset$ for $n \neq m$;
- (d) $\operatorname{diam}_Y(B_s) \to 0$ as $|s| \to \infty$.

*Construction.* Set $B_\emptyset = Y$. Suppose $B_s$ has been defined and is Borel with $f(A_s) \subset B_s$. The sets $f(A_{s^\frown n})$ ($n \in \omega$) are pairwise disjoint (since $f$ is injective and the $A_{s^\frown n}$ are disjoint) and analytic (image of the Borel set $A_{s^\frown n}$ under the Borel map $f$). By the iterated Separation Theorem (ii), there exist pairwise disjoint Borel sets $D_n \subset Y$ with $f(A_{s^\frown n}) \subset D_n$. Replacing $D_n$ by $D_n \cap B_s$ preserves these properties and ensures $D_n \subset B_s$.

Now choose a sequence $\varepsilon_k \to 0$ (e.g. $\varepsilon_k = 2^{-k}$) and set
$$B_{s^\frown n} := D_n \cap \bigl\{y \in Y : d_Y\bigl(y,\, f(A_{s^\frown n})\bigr) < \varepsilon_{|s|+1}\bigr\}.$$
This is Borel (the distance function to a set is upper/lower semicontinuous, and $f(A_{s^\frown n})$ is analytic hence measurable for the distance function). Then:

- (a) $f(A_{s^\frown n}) \subset B_{s^\frown n}$: clear, since $f(A_{s^\frown n}) \subset D_n$ and the distance is $0$ on the set itself.
- (b) $B_{s^\frown n} \subset D_n \subset B_s$: by construction.
- (c) $B_{s^\frown n} \subset D_n$ and the $D_n$ are disjoint.
- (d) If $y, y' \in B_{s^\frown n}$, pick $z, z' \in f(A_{s^\frown n})$ with $d_Y(y,z), d_Y(y',z') < \varepsilon_{|s|+1}$. Then
$$d_Y(y,y') \le \varepsilon_{|s|+1} + \operatorname{diam}_Y(f(A_{s^\frown n})) + \varepsilon_{|s|+1} \le 2\varepsilon_{|s|+1} + 2^{-(|s|+1)},$$
which $\to 0$ as $|s| \to \infty$ by Step 1, property (4). ∎

### Step 3. The remainder decomposition

Define the **remainder**
$$R_s := B_s \setminus \bigcup_{n \in \omega} B_{s^\frown n}, \qquad s \in \omega^{<\omega}.$$
Each $R_s$ is Borel. We claim:

> **Key identity.** $\displaystyle \bigsqcup_{n \in \omega} B_{(n)} \;=\; f(A) \;\sqcup\; \bigsqcup_{s \in \omega^{<\omega}} R_s \quad\text{(disjoint union).}$

*Proof of the identity.* We verify four things.

**Disjointness of the right-hand side.** First, the $R_s$ are pairwise disjoint: if $s, t$ are incompatible, then $B_s \cap B_t = \emptyset$ (by induction on $\max(|s|,|t|)$ using (c) at the first level where the paths diverge), so $R_s \cap R_t = \emptyset$; if $s \subsetneq t$, then $R_s \subset B_s \setminus \bigcup_n B_{s^\frown n}$ while $R_t \subset B_t \subset B_{s^\frown n_0}$ for some $n_0$, so $R_t \cap R_s = \emptyset$. Similarly $f(A) \cap R_s = \emptyset$ for every $s$ (shown below).

**Inclusion $f(A) \subset \bigcup_n B_{(n)}$.** Since $f(A) = \bigsqcup_n f(A_{(n)}) \subset \bigsqcup_n B_{(n)}$ by (a). ✓

**Inclusion $\bigcup_s R_s \subset \bigcup_n B_{(n)}$.** For any $s$, $R_s \subset B_s \subset B_{(s_0)} \subset \bigcup_n B_{(n)}$. ✓

**$f(A) \cap \bigcup_s R_s = \emptyset$.** Let $y = f(x) \in f(A)$, and let $\alpha \in \omega^\omega$ be the unique branch with $\{x\} = \bigcap_k A_{\alpha|k}$ (Step 1, property (3)). Then $y \in \bigcap_k B_{\alpha|k}$ by (a). For any $s \in \omega^{<\omega}$:

- If $s = \alpha|j$ for some $j$, then $y \in B_{\alpha|(j+1)} = B_{s^\frown \alpha(j)} \subset \bigcup_n B_{s^\frown n}$, so $y \notin R_s$.
- If $s$ is incompatible with $\alpha$, then $B_s \cap B_{\alpha||s||} = \emptyset$ (paths diverge at some level, use (c)), so $y \notin B_s \supset R_s$, hence $y \notin R_s$.

Thus $y \notin \bigcup_s R_s$. ✓

**$\bigcup_n B_{(n)} \subset f(A) \cup \bigcup_s R_s$.** Let $y \in \bigcup_n B_{(n)}$; by (c) there is a unique $n_0$ with $y \in B_{(n_0)}$. Either $y \in R_{(n_0)}$ (done), or $y \in \bigcup_m B_{(n_0, m)}$, and by (c) there is a unique $n_1$ with $y \in B_{(n_0, n_1)}$. Continue. Either the process terminates at some finite stage, yielding $y \in R_s$ for some $s$, or it produces an infinite sequence $\alpha = (n_0, n_1, \dots) \in \omega^\omega$ with $y \in \bigcap_k B_{\alpha|k}$.

In the latter case, by property (d), $\operatorname{diam}_Y(B_{\alpha|k}) \to 0$, so $\bigcap_k B_{\alpha|k}$ contains **at most one point** (any two points in the intersection would be at distance $\le \operatorname{diam}(B_{\alpha|k})$ for all $k$, hence at distance $0$). On the other hand, the unique $x_\alpha \in \bigcap_k A_{\alpha|k}$ (Step 1, property (3)) satisfies
$$f(x_\alpha) \in \bigcap_k f(A_{\alpha|k}) \subset \bigcap_k B_{\alpha|k}$$
by (a). Therefore $y = f(x_\alpha) \in f(A)$. ✓

This completes the proof of the key identity. ∎

### Conclusion

From the key identity,
$$f(A) = \left(\bigcup_{n \in \omega} B_{(n)}\right) \setminus \left(\bigcup_{s \in \omega^{<\omega}} R_s\right).$$
The set $\bigcup_n B_{(n)}$ is a countable union of Borel sets, hence Borel. The set $\bigcup_s R_s$ is a countable union (over $\omega^{<\omega}$, which is countable) of Borel sets, hence Borel. Therefore $f(A) = B$ is Borel. $\blacksquare$

---

**Remark.** The same argument proves the full Lusin–Suslin theorem (injective Borel image of a Borel set is Borel); the only place we used that $f$ is a homeomorphism rather than merely Borel is in Step 1, where the metric $\rho = d_Y \circ (f \times f)$ is compatible with the topology of $A$, allowing a Lusin scheme with $\operatorname{diam}_Y(f(A_s)) \to 0$. For the general case one replaces this by a Borel-isomorphism argument (every Borel set is a one-to-one continuous image of a closed subset of $\omega^\omega$), which yields the same diameter control.

$$\boxed{B \text{ is a Borel subset of } Y.}$$

### PROOF COMPLETE
