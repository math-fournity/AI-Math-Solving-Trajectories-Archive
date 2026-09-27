# Dimension of the Image

## Problem

Determine the dimension of the image of the map
$$
\Phi: H^{1}(G_{S}, Ad(\bar{\rho})) = H^{1}(G_{S}, \mathbb{F}_{p}) \oplus H^{1}(G_{S}, Ad^{0}(\bar{\rho})) \rightarrow H^{1}(I_{p}, Ad^{0}(\bar{\rho})) \rightarrow H^{1}(I_{p}, \mathbb{F}_{p}(\omega^{k-1}))
$$
where $Ad^{0}(\bar{\rho}) \cong \mathbb{F}_{p} \oplus \mathbb{F}_{p}(\omega^{k-1}) \oplus \mathbb{F}_{p}(\omega^{1-k})$ as an $I_p$-module.

## Answer

$$\boxed{1}$$

## Proof

We work under the hypotheses implicit in the problem statement:
- $\bar{\rho}: G_{\mathbb{Q}} \to \mathrm{GL}_2(\mathbb{F}_p)$ is absolutely irreducible.
- $\bar{\rho}|_{I_p}$ is semisimple (split), with $\bar{\rho}|_{I_p} \sim \mathrm{diag}(\omega^{k-1}, 1)$, so that $Ad^0(\bar{\rho})|_{I_p} \cong \mathbb{F}_p \oplus \mathbb{F}_p(\omega^{k-1}) \oplus \mathbb{F}_p(\omega^{1-k})$ as stated.
- $\omega^{k-1}$ and $\omega^{1-k}$ are non-trivial characters of $I_p/P_p \cong \mathbb{F}_p^{\times}$, i.e., $k \not\equiv 1 \pmod{p-1}$ and $k \not\equiv 1 \pmod{p-1}$ (equivalently $1-k \not\equiv 0$).

### Step 1: The scalar part maps to zero

We have $Ad(\bar{\rho}) = \mathbb{F}_p \oplus Ad^0(\bar{\rho})$ where $\mathbb{F}_p$ is the scalar (trace) part. The map $H^1(G_S, Ad(\bar{\rho})) \to H^1(I_p, Ad^0(\bar{\rho}))$ is "restrict to $I_p$, then project $Ad(\bar{\rho}) \to Ad^0(\bar{\rho})$." The projection $Ad(\bar{\rho}) \to Ad^0(\bar{\rho})$ kills the scalar summand $\mathbb{F}_p$. Therefore any class in $H^1(G_S, \mathbb{F}_p)$ (scalar cocycles) maps to zero. The composite $\Phi$ reduces to
$$
\Phi: H^1(G_S, Ad^0(\bar{\rho})) \xrightarrow{\mathrm{res}_{I_p}} H^1(I_p, Ad^0(\bar{\rho})) \xrightarrow{\mathrm{proj}} H^1(I_p, \mathbb{F}_p(\omega^{k-1})).
$$

### Step 2: The target is 1-dimensional

We compute $\dim_{\mathbb{F}_p} H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$.

Use the exact sequence $1 \to P_p \to I_p \to I_p/P_p \to 1$ where $P_p$ is the wild inertia (pro-$p$) and $I_p/P_p \cong \hat{\mathbb{Z}}^{(p')}$ is the tame inertia (pro-prime-to-$p$).

The mod-$p$ cyclotomic character $\omega$ factors through $I_p/P_p \cong \mathbb{F}_p^{\times}$ (the tame quotient), so $\omega$ is trivial on $P_p$. Hence $\mathbb{F}_p(\omega^{k-1})^{P_p} = \mathbb{F}_p(\omega^{k-1})$.

**Tame cohomology vanishes.** Since $I_p/P_p \cong \hat{\mathbb{Z}}^{(p')}$ is pro-prime-to-$p$ and $\mathbb{F}_p(\omega^{k-1})$ is $p$-torsion, we have
$$
H^1(I_p/P_p, \mathbb{F}_p(\omega^{k-1})) = \mathrm{Hom}_{\mathrm{cont}}(\hat{\mathbb{Z}}^{(p')}, \mathbb{F}_p(\omega^{k-1})) = 0,
$$
because any continuous homomorphism from a pro-prime-to-$p$ group to a $p$-torsion group is trivial. Similarly $H^2(I_p/P_p, \mathbb{F}_p(\omega^{k-1})) = 0$ when $\omega^{k-1}$ is non-trivial (the norm map $N = \sum_{g \in \mathbb{F}_p^{\times}} \omega^{k-1}(g)$ is an automorphism of $\mathbb{F}_p$ since $\omega^{k-1} \neq 1$).

**Wild inertia cohomology.** By inflation-restriction (with both $H^1$ and $H^2$ of the quotient vanishing):
$$
H^1(I_p, \mathbb{F}_p(\omega^{k-1})) \cong H^1(P_p, \mathbb{F}_p(\omega^{k-1}))^{I_p/P_p} = \mathrm{Hom}(P_p, \mathbb{F}_p)^{I_p/P_p, \omega^{k-1}\text{-twist}}.
$$

**Structure of wild inertia (Serre, *Local Fields*).** As a module over $I_p/P_p \cong \mathbb{F}_p^{\times}$,
$$
P_p^{\mathrm{ab}} \otimes \mathbb{F}_p \cong \bigoplus_{i \in \mathbb{Z}/(p-1)\mathbb{Z}} \mathbb{F}_p(\omega^i).
$$
Therefore
$$
\mathrm{Hom}(P_p, \mathbb{F}_p) \cong (P_p^{\mathrm{ab}})^{\vee} \otimes \mathbb{F}_p \cong \bigoplus_{i=0}^{p-2} \mathbb{F}_p(\omega^{-i}).
$$
Twisting by $\omega^{k-1}$ (i.e., taking $\mathrm{Hom}(P_p, \mathbb{F}_p(\omega^{k-1}))$) and then $I_p/P_p$-invariants selects the component with $\omega^{-i} \cdot \omega^{k-1} = 1$, i.e., $i \equiv k-1 \pmod{p-1}$. This gives exactly one copy of $\mathbb{F}_p$.

Therefore
$$
\dim_{\mathbb{F}_p} H^1(I_p, \mathbb{F}_p(\omega^{k-1})) = 1.
$$

### Step 3: The local map is surjective

Consider the local map
$$
\ell: H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) \to H^1(I_p, \mathbb{F}_p(\omega^{k-1})).
$$

**Local Euler characteristic formula.** For a finite $\mathbb{F}_p[G_{\mathbb{Q}_p}]$-module $M$:
$$
\dim H^1(G_{\mathbb{Q}_p}, M) = \dim H^0(G_{\mathbb{Q}_p}, M) + \dim H^0(G_{\mathbb{Q}_p}, M^*(1)) + \dim M - \dim M^{I_p}.
$$
(Here $M^*(1) = \mathrm{Hom}(M, \mu_{p})$ is the Tate dual.)

For $M = Ad^0(\bar{\rho})$ (3-dimensional):
- $H^0(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) = \mathbb{F}_p$ (the diagonal trace-zero matrix $\mathrm{diag}(1, -1)$ is fixed when $\bar{\rho}$ is semisimple at $p$; dimension 1).
- $Ad^0(\bar{\rho})$ is self-dual up to twist: $Ad^0(\bar{\rho})^*(1) \cong Ad^0(\bar{\rho})$ (the trace pairing on $Ad^0$ is perfect and $G_{\mathbb{Q}_p}$-equivariant). So $H^0(G_{\mathbb{Q}_p}, M^*(1)) = 1$.
- $M^{I_p} = \mathbb{F}_p$ (the diagonal part; the off-diagonal pieces $\mathbb{F}_p(\omega^{k-1})$ and $\mathbb{F}_p(\omega^{1-k})$ have no $I_p$-invariants since $\omega^{k-1}, \omega^{1-k}$ are non-trivial).

Therefore $\dim H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) = 1 + 1 + 3 - 1 = 4$.

**Inflation-restriction for $G_{\mathbb{Q}_p}$.** Use $1 \to I_p \to G_{\mathbb{Q}_p} \to G_{\mathbb{F}_p} \cong \hat{\mathbb{Z}} \to 1$:
$$
0 \to H^1(\hat{\mathbb{Z}}, M^{I_p}) \to H^1(G_{\mathbb{Q}_p}, M) \to H^1(I_p, M)^{\hat{\mathbb{Z}}} \to H^2(\hat{\mathbb{Z}}, M^{I_p}) \to H^2(G_{\mathbb{Q}_p}, M).
$$
With $M^{I_p} = \mathbb{F}_p$ (trivial $\hat{\mathbb{Z}}$-action, since Frobenius acts trivially on the diagonal in the semisimple case):
- $H^1(\hat{\mathbb{Z}}, \mathbb{F}_p) = \mathbb{F}_p$ (1-dim, since $\hat{\mathbb{Z}}$ surjects onto $\mathbb{Z}/p\mathbb{Z}$).
- $H^2(\hat{\mathbb{Z}}, \mathbb{F}_p) = \mathbb{F}_p / N\mathbb{F}_p = \mathbb{F}_p$ (1-dim, since norm $N = p \cdot \mathrm{id} = 0$ on $\mathbb{F}_p$).

By local Tate duality, $H^2(G_{\mathbb{Q}_p}, M) \cong H^0(G_{\mathbb{Q}_p}, M^*(1))^* = \mathbb{F}_p$ (1-dim), and the connecting map $H^2(\hat{\mathbb{Z}}, \mathbb{F}_p) \to H^2(G_{\mathbb{Q}_p}, M)$ is an isomorphism (both 1-dimensional, and the map is non-zero). So the sequence gives:
$$
0 \to \mathbb{F}_p \to H^1(G_{\mathbb{Q}_p}, M) \to H^1(I_p, M)^{\hat{\mathbb{Z}}} \to 0,
$$
hence $\dim H^1(I_p, M)^{\hat{\mathbb{Z}}} = 4 - 1 = 3$.

**Frobenius action on $H^1(I_p, Ad^0(\bar{\rho}))$.** We have
$$
H^1(I_p, Ad^0(\bar{\rho})) \cong H^1(I_p, \mathbb{F}_p) \oplus H^1(I_p, \mathbb{F}_p(\omega^{k-1})) \oplus H^1(I_p, \mathbb{F}_p(\omega^{1-k})),
$$
each summand 1-dimensional (by the same computation as Step 2, with the trivial character giving the $\omega^0$-component).

**Key fact: $\omega(\mathrm{Frob}_p) = 1$.** The mod-$p$ cyclotomic character $\omega: G_{\mathbb{Q}} \to \mathbb{F}_p^{\times}$ is defined by $\sigma(\zeta) = \zeta^{\omega(\sigma)}$ for $\zeta \in \mu_p$. The extension $\mathbb{Q}_p(\mu_p)/\mathbb{Q}_p$ is **totally ramified** of degree $p-1$ (since $\mathbb{Q}_p$ already contains $\mu_{p-1}$ but not $\mu_p$). Therefore $\omega|_{G_{\mathbb{Q}_p}}$ factors through $\mathrm{Gal}(\mathbb{Q}_p(\mu_p)/\mathbb{Q}_p)$, which is totally ramified, meaning $\omega$ is **trivial on the unramified quotient** $G_{\mathbb{F}_p} = \hat{\mathbb{Z}}$. Hence $\omega(\mathrm{Frob}_p) = 1$, and consequently $\omega^j(\mathrm{Frob}_p) = 1$ for all $j$.

**Frobenius acts trivially on each summand.** The Frobenius action on $H^1(I_p, \mathbb{F}_p(\omega^j))$ is by $\omega^j(\mathrm{Frob}_p) = 1$ (the coefficient twist) composed with the conjugation action on $P_p$. On the $\omega^{-j}$-isotypic component of $\mathrm{Hom}(P_p, \mathbb{F}_p)$, the conjugation by $\mathrm{Frob}_p$ (acting as $\sigma \mapsto \sigma^p$ on tame inertia) scales by $p$, while the dual $\mathrm{Hom}$ action scales by $p^{-1}$; these cancel, leaving the net action as $\omega^j(\mathrm{Frob}_p) = 1$. (Equivalently: the Frobenius action on $H^1(I_p, \mathbb{F}_p(\omega^j))$ is via the character $\omega^j$ evaluated at $\mathrm{Frob}_p$, which is 1.)

Therefore
$$
H^1(I_p, Ad^0(\bar{\rho}))^{\hat{\mathbb{Z}}} = H^1(I_p, Ad^0(\bar{\rho})) \cong \mathbb{F}_p^3,
$$
consistent with $\dim = 3$ from the inflation-restriction computation.

**The local map is surjective.** The local map $\ell: H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) \to H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$ factors as
$$
H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho})) \twoheadrightarrow H^1(I_p, Ad^0(\bar{\rho}))^{\hat{\mathbb{Z}}} \xrightarrow{\mathrm{proj}} H^1(I_p, \mathbb{F}_p(\omega^{k-1})),
$$
where the first map is surjective (from the inflation-restriction sequence, with kernel $H^1(\hat{\mathbb{Z}}, \mathbb{F}_p) = \mathbb{F}_p$) and the second is the projection onto the $\omega^{k-1}$-summand, which is a direct summand of the 3-dimensional Frobenius-invariant space. The projection is surjective. Therefore **$\ell$ is surjective**, i.e., the local map hits the full 1-dimensional target.

### Step 4: Global-to-local surjectivity

It remains to show that the global restriction map
$$
\mathrm{res}_p: H^1(G_S, Ad^0(\bar{\rho})) \to H^1(G_{\mathbb{Q}_p}, Ad^0(\bar{\rho}))
$$
has image that maps surjectively onto $H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$ under $\ell$.

Since $\bar{\rho}$ is absolutely irreducible, $H^0(G_S, Ad^0(\bar{\rho})) = 0$ (Schur's lemma: the only endomorphisms commuting with an absolutely irreducible representation are scalars, and trace-zero scalars are zero). Similarly $H^0(G_S, Ad^0(\bar{\rho})^*(1)) = 0$ (since $Ad^0(\bar{\rho})^*(1) \cong Ad^0(\bar{\rho})$ is also absolutely irreducible as a $G_S$-module, being a twist of an absolutely irreducible representation).

By the **Poitou–Tate exact sequence** (for the module $M = Ad^0(\bar{\rho})$ over $G_S$):
$$
H^1(G_S, M) \xrightarrow{\bigoplus_{v \in S} \mathrm{res}_v} \bigoplus_{v \in S} H^1(G_{\mathbb{Q}_v}, M) \xrightarrow{\Sigma \, \mathrm{inv}_v} H^0(G_S, M^*(1))^* \to H^2(G_S, M) \to \cdots
$$
Since $H^0(G_S, M^*(1)) = 0$, the sum of local invariants maps $\Sigma \, \mathrm{inv}_v$ has target $0$, so the localization map $\bigoplus_{v \in S} \mathrm{res}_v$ is **surjective**. This means: for any tuple $(c_v)_{v \in S} \in \bigoplus_{v \in S} H^1(G_{\mathbb{Q}_v}, M)$, there exists a global class $c \in H^1(G_S, M)$ with $\mathrm{res}_v(c) = c_v$ for all $v \in S$. In particular, taking $c_p$ to be any class in $H^1(G_{\mathbb{Q}_p}, M)$ and $c_v = 0$ for $v \neq p$, we obtain a global class mapping to $c_p$. Therefore **$\mathrm{res}_p$ is surjective**.

Since $\mathrm{res}_p$ is surjective and $\ell$ is surjective (Step 3), the composite $\Phi = \ell \circ \mathrm{res}_p$ is surjective onto $H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$.

### Conclusion

The image of $\Phi$ is all of $H^1(I_p, \mathbb{F}_p(\omega^{k-1}))$, which is 1-dimensional. Therefore
$$
\dim \mathrm{Im}(\Phi) = \boxed{1}.
$$
