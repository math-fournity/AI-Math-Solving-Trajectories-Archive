# Proof: $1_B \hat{\otimes}_\varepsilon f$ is a continuous linear injective map

## Answer

**Yes**, the map $1_B \hat{\otimes}_\varepsilon f : B \hat{\otimes}_\varepsilon E \to B \hat{\otimes}_\varepsilon F$ is a continuous linear injective map.

## Proof

### Step 1: Setup and key identification

Let $B$ be a Banach space and $E$ a complete locally convex space (LCS). The **injective tensor product** $B \otimes_\varepsilon E$ is defined as the algebraic tensor product $B \otimes E$ equipped with the topology of uniform convergence on equicontinuous subsets of $B'$, realized via the canonical embedding

$$
J_E : B \otimes E \hookrightarrow \mathcal{L}(B'_\beta, E), \qquad b \otimes e \mapsto \big[\phi \mapsto \phi(b)\, e\big],
$$

where $B'_\beta$ denotes the strong dual of $B$ (i.e., $B'$ with the topology of uniform convergence on bounded sets). The injective tensor topology on $B \otimes E$ is precisely the subspace topology induced by $\mathcal{L}(B'_\beta, E)$ equipped with the topology of uniform convergence on bounded (equivalently, equicontinuous) subsets of $B'$.

**The embedding $J_E$ is injective.** Indeed, if $u = \sum_{i=1}^n b_i \otimes e_i$ with $\{e_i\}_{i=1}^n$ linearly independent and $J_E(u) = 0$, then $\sum_{i=1}^n \phi(b_i)\, e_i = 0$ for all $\phi \in B'$. By linear independence of the $e_i$, this gives $\phi(b_i) = 0$ for all $\phi \in B'$ and all $i$. By the Hahn–Banach theorem, $b_i = 0$ for all $i$, hence $u = 0$.

### Step 2: Completion as a subspace of operators

Since $B$ is a normed space, the equicontinuous subsets of $B'$ are exactly the norm-bounded subsets (by the Banach–Alaoglu theorem). The space $\mathcal{L}(B'_\beta, E)$, equipped with the topology of uniform convergence on bounded sets, is **complete** whenever $E$ is complete (this is a standard result: the limit of a uniformly convergent net of continuous linear maps on bounded sets is itself continuous and linear).

Therefore, the completion

$$
B \hat{\otimes}_\varepsilon E = \overline{B \otimes E}^{\,\mathcal{L}(B'_\beta, E)}
$$

is a **closed subspace** of $\mathcal{L}(B'_\beta, E)$. In particular, the embedding extends to an injection:

$$
J_E : B \hat{\otimes}_\varepsilon E \hookrightarrow \mathcal{L}(B'_\beta, E).
$$

### Step 3: The map $1_B \hat{\otimes}_\varepsilon f$ as post-composition

The algebraic map $1_B \otimes f : B \otimes E \to B \otimes F$ sends $\sum b_i \otimes e_i$ to $\sum b_i \otimes f(e_i)$. Under the embeddings $J_E$ and $J_F$, this corresponds to **post-composition by $f$**:

$$
J_F \circ (1_B \otimes f) \circ J_E^{-1} : T \mapsto f \circ T, \qquad T \in B \otimes E \subset \mathcal{L}(B'_\beta, E).
$$

Since $f : E \to F$ is continuous, the post-composition map

$$
C_f : \mathcal{L}(B'_\beta, E) \to \mathcal{L}(B'_\beta, F), \qquad T \mapsto f \circ T
$$

is continuous (with respect to the topologies of uniform convergence on bounded sets). By density of $B \otimes E$ in $B \hat{\otimes}_\varepsilon E$ and continuity of $C_f$, the unique continuous extension of $1_B \otimes f$ to the completions satisfies:

$$
J_F \circ (1_B \hat{\otimes}_\varepsilon f) = C_f \circ J_E.
$$

That is, $1_B \hat{\otimes}_\varepsilon f$ is exactly post-composition by $f$, viewed as a map from $B \hat{\otimes}_\varepsilon E \subset \mathcal{L}(B'_\beta, E)$ to $B \hat{\otimes}_\varepsilon F \subset \mathcal{L}(B'_\beta, F)$.

### Step 4: Injectivity of post-composition

We now show $1_B \hat{\otimes}_\varepsilon f$ is injective. Suppose $T \in B \hat{\otimes}_\varepsilon E$ and $(1_B \hat{\otimes}_\varepsilon f)(T) = 0$ in $B \hat{\otimes}_\varepsilon F$. Since $J_F$ is injective:

$$
0 = J_F\big((1_B \hat{\otimes}_\varepsilon f)(T)\big) = C_f(J_E(T)) = f \circ J_E(T).
$$

This means $f\big(J_E(T)(\phi)\big) = 0$ for every $\phi \in B'$. Since $f$ is **injective**, we conclude $J_E(T)(\phi) = 0$ for every $\phi \in B'$, i.e., $J_E(T) = 0$ as an element of $\mathcal{L}(B'_\beta, E)$. Since $J_E$ is injective, $T = 0$.

Therefore, $\ker(1_B \hat{\otimes}_\varepsilon f) = \{0\}$, and the map is injective.

### Step 5: Continuity

Continuity of $1_B \hat{\otimes}_\varepsilon f$ follows from the universal property of the completion: the algebraic map $1_B \otimes f : B \otimes_\varepsilon E \to B \otimes_\varepsilon F$ is continuous (since $f$ is continuous and the injective tensor product is functorial in the category of LCS with continuous linear maps), and it extends uniquely to a continuous map between the completions.

### Role of the hypotheses

- **$E$ nuclear (and complete):** Ensures $E$ is a complete LCS, so that $\mathcal{L}(B'_\beta, E)$ is complete and $B \hat{\otimes}_\varepsilon E$ embeds as a closed subspace. Nuclearity also guarantees $B \hat{\otimes}_\varepsilon E = B \hat{\otimes}_\pi E$ (injective and projective tensor products coincide), though this equality is not needed for the injectivity argument — the key structure is the injective tensor product on the **codomain** $B \hat{\otimes}_\varepsilon F$.

- **$B$ Banach:** Ensures equicontinuous = norm-bounded in $B'$, giving the clean embedding into $\mathcal{L}(B'_\beta, E)$.

- **$f$ injective:** This is the essential hypothesis. The entire argument reduces to the elementary fact that post-composition by an injective map is injective on any space of linear maps.

- **Separability and infinite-dimensionality:** Not needed for the injectivity conclusion; these conditions contextualize the problem setting.

### Conclusion

The map $1_B \hat{\otimes}_\varepsilon f : B \hat{\otimes}_\varepsilon E \to B \hat{\otimes}_\varepsilon F$ is a **continuous linear injective** map. The essential reason is that the injective tensor product realizes $B \hat{\otimes}_\varepsilon E$ as a space of operators from $B'$ to $E$, and post-composition by the injective map $f$ preserves injectivity on any operator space.

$$\boxed{\text{Yes}}$$
