# Proof: The ring $\frac{\mathbb{Z}_p[[X]] \otimes_\mathbb{Z} \mathbb{Q}_p}{(X-p)^r}$ is not principal for any $r \geq 1$

## Answer

$$\boxed{\text{No}}$$

The ring $\frac{\mathbb{Z}_p[[X]] \otimes_\mathbb{Z} \mathbb{Q}_p}{(X-p)^r}$ is **not** principal for any integer $r \geq 1$.

---

## Proof

### Step 1: Compute $\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q}_p$

**Claim:** $\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q}_p \cong \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p$ (as $\mathbb{Q}$-algebras), and this is **not** isomorphic to $\mathbb{Q}_p$.

**Proof of claim.** Since $\mathbb{Q}_p$ is a $\mathbb{Q}$-vector space, we have $\mathbb{Q}_p \cong \mathbb{Q} \otimes_\mathbb{Q} \mathbb{Q}_p$ as $\mathbb{Z}$-modules (the $\mathbb{Z}$-module structure factors through $\mathbb{Q}$). By associativity of the tensor product:

$$\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q}_p \cong \mathbb{Z}_p \otimes_\mathbb{Z} (\mathbb{Q} \otimes_\mathbb{Q} \mathbb{Q}_p) \cong (\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q}) \otimes_\mathbb{Q} \mathbb{Q}_p.$$

Now, $\mathbb{Z}_p$ is torsion-free over $\mathbb{Z}$ (hence flat, since $\mathbb{Z}$ is a PID), so $\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q} \cong S^{-1}\mathbb{Z}_p$ where $S = \mathbb{Z} \setminus \{0\}$. In $\mathbb{Z}_p$, every prime $\ell \neq p$ is already a unit, so inverting all nonzero integers amounts to inverting $p$, giving $\mathbb{Z}_p[1/p] = \mathbb{Q}_p$. Therefore:

$$\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q}_p \cong \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p.$$

As a $\mathbb{Q}_p$-vector space (via the first factor), $\mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p$ has dimension $\dim_\mathbb{Q} \mathbb{Q}_p = 2^{\aleph_0}$ (uncountable), whereas $\mathbb{Q}_p$ has dimension $1$ over itself. Hence $\mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p \not\cong \mathbb{Q}_p$. $\square$

Set $A := \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p$.

### Step 2: Compute $R_r := \frac{\mathbb{Z}_p[[X]] \otimes_\mathbb{Z} \mathbb{Q}_p}{(X-p)^r}$

**Claim:** $R_r \cong A[X]/(X^r)$ for all $r \geq 1$.

**Proof of claim.** Since $\mathbb{Q}_p$ is flat over $\mathbb{Z}$ (torsion-free over a PID), tensoring the exact sequence

$$0 \to (X-p)^r \to \mathbb{Z}_p[[X]] \to \mathbb{Z}_p[[X]]/(X-p)^r \to 0$$

with $\mathbb{Q}_p$ remains exact, giving:

$$R_r \cong \left(\mathbb{Z}_p[[X]]/(X-p)^r\right) \otimes_\mathbb{Z} \mathbb{Q}_p.$$

The substitution $X \mapsto X + p$ is an automorphism of $\mathbb{Z}_p[[X]]$ (since $p \in \mathbb{Z}_p$ and the power series $f(X+p) = \sum a_n(X+p)^n$ has well-defined coefficients $\binom{n}{k}p^{n-k} \in \mathbb{Z}_p$). This automorphism sends the ideal $(X-p)$ to $(X)$, so:

$$\mathbb{Z}_p[[X]]/(X-p)^r \cong \mathbb{Z}_p[[X]]/(X^r) \cong \mathbb{Z}_p[X]/(X^r).$$

(The last isomorphism holds because quotienting $\mathbb{Z}_p[[X]]$ by $X^r$ truncates power series to degree $< r$, yielding $\mathbb{Z}_p[X]/(X^r)$.)

Now, $\mathbb{Z}_p[X]/(X^r)$ is a $\mathbb{Z}_p$-algebra (free of rank $r$ as a $\mathbb{Z}_p$-module), so:

$$\left(\mathbb{Z}_p[X]/(X^r)\right) \otimes_\mathbb{Z} \mathbb{Q}_p \cong \left(\mathbb{Z}_p[X]/(X^r)\right) \otimes_{\mathbb{Z}_p} \left(\mathbb{Z}_p \otimes_\mathbb{Z} \mathbb{Q}_p\right) \cong \left(\mathbb{Z}_p[X]/(X^r)\right) \otimes_{\mathbb{Z}_p} A.$$

By the standard base-change isomorphism for polynomial rings, $(\mathbb{Z}_p[X]/(X^r)) \otimes_{\mathbb{Z}_p} A \cong A[X]/(X^r)$.

Combining: $R_r \cong A[X]/(X^r)$. $\square$

In particular, $R_1 \cong A[X]/(X) \cong A = \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p$.

### Step 3: $A = \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p$ is not Noetherian

**Claim:** $A$ is not a Noetherian ring.

**Proof of claim.** Let $\{e_\alpha\}_{\alpha \in \mathcal{A}}$ be a $\mathbb{Q}$-basis of $\mathbb{Q}_p$ with $e_0 = 1$. Since $\dim_\mathbb{Q} \mathbb{Q}_p = 2^{\aleph_0}$, the set $\mathcal{A} \setminus \{0\}$ is uncountable.

We construct a countably infinite sequence $\alpha_1, \alpha_2, \alpha_3, \ldots \in \mathcal{A} \setminus \{0\}$ inductively: having chosen $\alpha_1, \ldots, \alpha_n$, set $K_n := \mathbb{Q}(e_{\alpha_1}, \ldots, e_{\alpha_n})$, a finitely generated field extension of $\mathbb{Q}$. Since $K_n$ has countable dimension over $\mathbb{Q}$ while $\mathbb{Q}_p$ has uncountable dimension, $K_n \subsetneq \mathbb{Q}_p$, so there exists a basis element $e_{\alpha_{n+1}} \notin K_n$. Choose such an $\alpha_{n+1}$.

For each $n \geq 1$, define the ideal:

$$J_n := \left(e_{\alpha_i} \otimes 1 - 1 \otimes e_{\alpha_i} \;:\; 1 \leq i \leq n\right) \subset A.$$

We show $J_1 \subsetneq J_2 \subsetneq J_3 \subsetneq \cdots$ is a strictly ascending chain.

It suffices to prove $e_{\alpha_{n+1}} \otimes 1 - 1 \otimes e_{\alpha_{n+1}} \notin J_n$ for each $n$.

Consider the natural surjection of $\mathbb{Q}$-algebras:

$$\Phi_n : A = \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p \longrightarrow \mathbb{Q}_p \otimes_{K_n} \mathbb{Q}_p, \qquad a \otimes_\mathbb{Q} b \longmapsto a \otimes_{K_n} b.$$

This map quotients out by the additional relations $k \otimes 1 = 1 \otimes k$ for all $k \in K_n$. Since $e_{\alpha_i} \in K_n$ for $1 \leq i \leq n$, we have $\Phi_n(e_{\alpha_i} \otimes 1 - 1 \otimes e_{\alpha_i}) = 0$, so $J_n \subseteq \ker(\Phi_n)$.

On the other hand:

$$\Phi_n\!\left(e_{\alpha_{n+1}} \otimes 1 - 1 \otimes e_{\alpha_{n+1}}\right) = e_{\alpha_{n+1}} \otimes_{K_n} 1 - 1 \otimes_{K_n} e_{\alpha_{n+1}}.$$

Since $e_{\alpha_{n+1}} \notin K_n$ and $\mathbb{Q}_p$ is a $K_n$-vector space, we may extend $\{1\}$ to a $K_n$-basis $\{f_j\}_{j \in \mathcal{J}}$ of $\mathbb{Q}_p$ with $f_0 = 1$. Write $e_{\alpha_{n+1}} = \sum_j c_j f_j$ with $c_j \in K_n$ and some $c_j \neq 0$ for $j \neq 0$ (since $e_{\alpha_{n+1}} \notin K_n = K_n \cdot f_0$). Then:

$$e_{\alpha_{n+1}} \otimes_{K_n} 1 - 1 \otimes_{K_n} e_{\alpha_{n+1}} = \sum_{j \neq 0} c_j \left(f_j \otimes_{K_n} f_0 - f_0 \otimes_{K_n} f_j\right).$$

Since $\{f_i \otimes_{K_n} f_j\}_{i,j \in \mathcal{J}}$ is a $K_n$-basis of $\mathbb{Q}_p \otimes_{K_n} \mathbb{Q}_p$, the elements $f_j \otimes_{K_n} f_0$ and $f_0 \otimes_{K_n} f_j$ are distinct basis elements for $j \neq 0$. Hence the above expression is a nontrivial linear combination of basis elements, so it is nonzero.

Therefore $e_{\alpha_{n+1}} \otimes 1 - 1 \otimes e_{\alpha_{n+1}} \notin \ker(\Phi_n) \supseteq J_n$, which gives $J_n \subsetneq J_{n+1}$.

The strictly ascending chain $J_1 \subsetneq J_2 \subsetneq J_3 \subsetneq \cdots$ witnesses that $A$ is not Noetherian. $\square$

### Step 4: Conclusion

Since $A = \mathbb{Q}_p \otimes_\mathbb{Q} \mathbb{Q}_p$ is not Noetherian, it is not a principal ideal ring (every principal ideal ring is Noetherian, since every ideal is generated by a single element).

For any $r \geq 1$, we have $R_r \cong A[X]/(X^r)$ (Step 2). There is a surjective ring homomorphism:

$$R_r \cong A[X]/(X^r) \longrightarrow A[X]/(X) \cong A,$$

given by evaluation at $X = 0$. If $R_r$ were a principal ideal ring, then its quotient $A$ would also be a principal ideal ring (a quotient of a PIR is a PIR). But $A$ is not Noetherian, hence not a PIR. Contradiction.

Therefore $R_r$ is **not** principal for any $r \geq 1$. $\square$

### PROOF COMPLETE
