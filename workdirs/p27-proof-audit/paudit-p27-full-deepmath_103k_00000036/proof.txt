# Proof: $K$ and $H(K)$ have the same conductor

**Theorem.** Let $K$ be an abelian number field and $H(K)$ the Hilbert class field of $K$. If $H(K)$ is abelian over $\mathbb{Q}$, then $\mathfrak{f}(K) = \mathfrak{f}(H(K))$.

## Answer

$$\boxed{\text{Yes, } K \text{ and } H(K) \text{ have the same conductor.}}$$

## Proof

### Setup and the easy divisibility

Since $K \subseteq H(K)$ and both are abelian over $\mathbb{Q}$, the conductor of the subextension divides the conductor of the full extension:

$$\mathfrak{f}(K) \mid \mathfrak{f}(H(K)).$$

It remains to prove the reverse divisibility $\mathfrak{f}(H(K)) \mid \mathfrak{f}(K)$.

### Key observation: the hypothesis makes the Artin map available

The conductor $\mathfrak{f}(H(K))$ in the class field theory sense is defined via the Artin reciprocity map, which requires $H(K)/\mathbb{Q}$ to be abelian. This is precisely the hypothesis. The Artin map

$$\psi_{H(K)/\mathbb{Q}} : \{\text{ideals of } \mathbb{Z} \text{ coprime to } \mathfrak{d}(H(K))\} \longrightarrow \mathrm{Gal}(H(K)/\mathbb{Q})$$

is a surjective homomorphism, and $\mathfrak{f}(H(K))$ is the minimal modulus $\mathfrak{m}$ (finite part $\mathfrak{m}_0$, possibly with an infinite sign condition) such that $\psi_{H(K)/\mathbb{Q}}$ factors through the ray class group $\mathrm{Cl}_{\mathfrak{m}}(\mathbb{Q})$.

### Ramified primes coincide

If a prime $p$ is unramified in $K/\mathbb{Q}$, then every prime of $K$ above $p$ is unramified over $p$. Since $H(K)/K$ is unramified at all primes (finite and infinite), every prime of $H(K)$ above $p$ is unramified over $p$. Hence $p$ is unramified in $H(K)/\mathbb{Q}$.

Conversely, since $K \subseteq H(K)$, any prime ramified in $K/\mathbb{Q}$ is ramified in $H(K)/\mathbb{Q}$.

Therefore $K/\mathbb{Q}$ and $H(K)/\mathbb{Q}$ have the **same ramified primes**, and consequently the same primes appear in $\mathfrak{f}(K)$ and $\mathfrak{f}(H(K))$.

### The main argument: $\psi_{H(K)/\mathbb{Q}}$ factors through $\mathfrak{f}(K)$

To show $\mathfrak{f}(H(K)) \mid \mathfrak{f}(K)$, we must show that $\psi_{H(K)/\mathbb{Q}}$ factors through the ray class group modulo $\mathfrak{f}(K)$. Equivalently, we show:

> **Claim.** For every positive $a \in \mathbb{Q}^*$ with $a \equiv 1 \pmod{\mathfrak{f}(K)}$ and $\gcd(a, \mathfrak{f}(H(K))) = 1$, we have $\psi_{H(K)/\mathbb{Q}}((a)) = 1$.

**Well-definedness of the Artin map at $(a)$:** The condition $a \equiv 1 \pmod{\mathfrak{f}(K)}$ implies $\gcd(a, \mathfrak{f}(K)) = 1$. Since the ramified primes of $H(K)/\mathbb{Q}$ and $K/\mathbb{Q}$ coincide (established above), $\gcd(a, \mathfrak{f}(K)) = 1$ implies $\gcd(a, \mathfrak{f}(H(K))) = 1$, so the Artin map is defined at $(a)$.

**Proof of the Claim.** Let $a \in \mathbb{Q}^*$, $a > 0$, $a \equiv 1 \pmod{\mathfrak{f}(K)}$, $\gcd(a, \mathfrak{f}(H(K))) = 1$.

**Step 1 — Restriction to $K$ is trivial.** Since $a \equiv 1 \pmod{\mathfrak{f}(K)}$, by definition of the conductor of $K/\mathbb{Q}$:

$$\psi_{K/\mathbb{Q}}((a)) = 1 \in \mathrm{Gal}(K/\mathbb{Q}).$$

By the compatibility of Artin maps in the tower $H(K) \supseteq K \supseteq \mathbb{Q}$ (restriction to subextensions):

$$\psi_{H(K)/\mathbb{Q}}((a))\Big|_K = \psi_{K/\mathbb{Q}}((a)) = 1.$$

Therefore $\psi_{H(K)/\mathbb{Q}}((a)) \in \mathrm{Gal}(H(K)/K)$.

**Step 2 — Tower compatibility with $H(K)/K$.** The Artin maps in the tower $H(K) \supseteq K \supseteq \mathbb{Q}$ satisfy the standard compatibility (see e.g. Neukirch, *Class Field Theory*, or Milne, *Class Field Theory*, Ch. V):

$$\psi_{H(K)/K}(x) = \psi_{H(K)/\mathbb{Q}}(x)\Big|_{\mathrm{Gal}(H(K)/K)}$$

for any idele $x \in \mathbb{A}_{\mathbb{Q}}^*$, viewed as an idele of $K$ via the natural inclusion $\mathbb{A}_{\mathbb{Q}}^* \hookrightarrow \mathbb{A}_K^*$.

Applying this to the principal idele $x = (a) \in \mathbb{Q}^* \hookrightarrow K^*$:

$$\psi_{H(K)/K}((a)) = \psi_{H(K)/\mathbb{Q}}((a))\Big|_{\mathrm{Gal}(H(K)/K)}.$$

**Step 3 — The unramified Artin map kills principal ideals.** Since $H(K)/K$ is unramified at every prime (finite and infinite), the Artin map $\psi_{H(K)/K}$ factors through the ideal class group:

$$\psi_{H(K)/K} : \mathrm{Cl}(K) \xrightarrow{\;\sim\;} \mathrm{Gal}(H(K)/K), \qquad [\mathfrak{A}] \longmapsto \left(\frac{H(K)/K}{\mathfrak{A}}\right).$$

For the principal idele $a \in K^*$, the associated ideal is $a\mathcal{O}_K$, which is principal. Hence its class is trivial:

$$\psi_{H(K)/K}((a)) = [a\mathcal{O}_K] = 1 \in \mathrm{Cl}(K) \cong \mathrm{Gal}(H(K)/K).$$

**Step 4 — Conclusion.** From Step 1, $\psi_{H(K)/\mathbb{Q}}((a)) \in \mathrm{Gal}(H(K)/K)$. From Steps 2 and 3, this element equals $\psi_{H(K)/K}((a)) = 1$. Therefore:

$$\psi_{H(K)/\mathbb{Q}}((a)) = 1 \in \mathrm{Gal}(H(K)/\mathbb{Q}).$$

This proves the Claim. $\square$

Since $\psi_{H(K)/\mathbb{Q}}$ is trivial on all principal ideals $(a)$ with $a \equiv 1 \pmod{\mathfrak{f}(K)}$, $a > 0$, the Artin map factors through the ray class group modulo $\mathfrak{f}(K)$. By minimality of the conductor:

$$\mathfrak{f}(H(K)) \mid \mathfrak{f}(K).$$

### The infinite part

The conductor includes an infinite (sign) component: $\mathfrak{f}_\infty(L) = \infty$ if and only if $L$ is not totally real (equivalently, the sign character appears in the Dirichlet character group of $L/\mathbb{Q}$).

Since $H(K)/K$ is unramified at every infinite place, every real embedding of $K$ extends to a real embedding of $H(K)$. Therefore:

$$H(K) \text{ is totally real} \iff K \text{ is totally real},$$

which gives $\mathfrak{f}_\infty(H(K)) = \mathfrak{f}_\infty(K)$.

### Final conclusion

Combining the finite and infinite parts:

$$\mathfrak{f}(K) \mid \mathfrak{f}(H(K)) \quad \text{and} \quad \mathfrak{f}(H(K)) \mid \mathfrak{f}(K),$$

therefore

$$\mathfrak{f}(K) = \mathfrak{f}(H(K)). \qquad \blacksquare$$

### Remark on the role of the hypothesis

The hypothesis that $H(K)/\mathbb{Q}$ is abelian is essential in two ways:

1. **It makes the conductor well-defined.** The class field theory conductor (minimal modulus for the Artin reciprocity map) is defined for abelian extensions. Without this hypothesis, $\mathfrak{f}(H(K))$ in this sense would not be defined.

2. **It is not automatic.** For example, $K = \mathbb{Q}(\sqrt{-23})$ has class number $h(K) = 3$, and $\mathrm{Gal}(H(K)/\mathbb{Q}) \cong S_3$ is non-abelian. The hypothesis fails, and the question does not apply.

### Verification: $K = \mathbb{Q}(\sqrt{-5})$

- $h(K) = 2$, $\mathrm{Cl}(K) \cong \mathbb{Z}/2\mathbb{Z}$.
- $H(K) = \mathbb{Q}(\sqrt{-5}, i)$, and $\mathrm{Gal}(H(K)/\mathbb{Q}) \cong (\mathbb{Z}/2)^2$ is abelian. ✓
- $\mathfrak{f}(K) = 20$ and $\mathfrak{f}(H(K)) = 20$. ✓

### PROOF COMPLETE
