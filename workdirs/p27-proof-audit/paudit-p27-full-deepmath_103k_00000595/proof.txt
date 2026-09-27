# Proof: Nowhere-Vanishing Sections of $T\mathbb{P}^n \otimes \mathcal{O}(d-1)$

**Problem.** For what integer values of $d$ does $E = T\mathbb{P}^n \otimes \mathcal{O}_X(d-1)$ admit a globally nonvanishing (nowhere-zero) section, where $X = \mathbb{P}^n$ over an algebraically closed field?

**Answer.** In characteristic $0$:

$$\boxed{d = -1 \text{ if } n = 1; \quad \text{no integer } d \text{ if } n \geq 2.}$$

(The $n = 1$ case holds in **all** characteristics; for $n \geq 2$ the cases $d \leq 1$ are ruled out in all characteristics, and $d \geq 2$ is ruled out by the Chern class argument in characteristic $0$.)

---

## Setup: The Euler Sequence and Sections of $E$

The Euler exact sequence on $\mathbb{P}^n$ is:
$$0 \to \mathcal{O}_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus(n+1)} \to T\mathbb{P}^n \to 0.$$

Tensoring by $\mathcal{O}(d-1)$ (which is locally free, hence exact):
$$0 \to \mathcal{O}(d-1) \to \mathcal{O}(d)^{\oplus(n+1)} \to E \to 0. \tag{$\star$}$$

**Key equivalence.** A nowhere-zero section $s \in H^0(E)$ is equivalent to an injection of vector bundles $\mathcal{O} \hookrightarrow E$, which (tensoring by $\mathcal{O}(1-d)$) is equivalent to an injection $\mathcal{O}(1-d) \hookrightarrow T\mathbb{P}^n$ as a sub-line-bundle. The equivalence between "sheaf injection" and "nowhere-zero" holds because a morphism of line bundles $\mathcal{O} \to E$ that is injective as a sheaf map is fiberwise injective: if it vanished at some point $x$, the kernel would be nonzero at $x$, contradicting injectivity.

---

## Case $n = 1$: $d = -1$

For $n = 1$, $T\mathbb{P}^1 \cong \mathcal{O}(2)$, so:
$$E = \mathcal{O}(2) \otimes \mathcal{O}(d-1) = \mathcal{O}(d+1).$$

A nowhere-zero section of $\mathcal{O}(d+1)$ on $\mathbb{P}^1$ is a homogeneous polynomial of degree $d+1$ in two variables with no zero on $\mathbb{P}^1$.

- **$d + 1 > 0$** (i.e., $d \geq 0$): A nonzero homogeneous polynomial of positive degree in two variables over an algebraically closed field factors completely into linear factors, hence has a zero on $\mathbb{P}^1$. No nowhere-zero section exists.

- **$d + 1 = 0$** (i.e., $d = -1$): $E = \mathcal{O}(0) = \mathcal{O}$. The constant section $1$ is nowhere zero. ✓

- **$d + 1 < 0$** (i.e., $d \leq -2$): $H^0(\mathcal{O}(d+1)) = 0$, so no sections exist at all.

**Conclusion for $n = 1$:** The unique solution is $d = -1$, valid in all characteristics.

---

## Case $n \geq 2$: No Solution (Characteristic $0$)

We show that no integer $d$ yields a nowhere-zero section, by treating four ranges of $d$.

### Step 1: $d \leq -1$ — No Sections Exist

From $(\star)$, taking global sections (and using $H^1(\mathcal{O}(d-1)) = 0$ for $n \geq 2$ since $0 < 1 < n$):
$$H^0(E) \hookrightarrow H^0(\mathcal{O}(d))^{\oplus(n+1)} \quad \text{(surjection from the middle term)}.$$

For $d \leq -1$: $H^0(\mathcal{O}(d)) = 0$ and $H^0(\mathcal{O}(d-1)) = 0$, so from the long exact cohomology sequence of $(\star)$:
$$0 \to H^0(\mathcal{O}(d-1)) \to H^0(\mathcal{O}(d))^{\oplus(n+1)} \to H^0(E) \to H^1(\mathcal{O}(d-1)) \to \cdots$$

Since $H^0(\mathcal{O}(d-1)) = 0$, $H^0(\mathcal{O}(d)) = 0$, and $H^1(\mathcal{O}(d-1)) = 0$ (for $n \geq 2$), we get $H^0(E) = 0$.

**No section exists, hence no nowhere-zero section.** (Valid in all characteristics.)

### Step 2: $d = 0$ — Every Nonzero Section Vanishes at a Point

Here $E = T\mathbb{P}^n \otimes \mathcal{O}(-1)$. From $(\star)$ with $d = 0$:
$$0 \to \mathcal{O}(-1) \to \mathcal{O}(0)^{\oplus(n+1)} \to E \to 0.$$

Since $H^0(\mathcal{O}(-1)) = 0$ and $H^1(\mathcal{O}(-1)) = 0$ (for $n \geq 2$):
$$H^0(E) \cong H^0(\mathcal{O})^{\oplus(n+1)} \cong k^{n+1}.$$

A section $s$ corresponds to a vector $(a_0, \ldots, a_n) \in k^{n+1}$. Under the map $\mathcal{O}^{\oplus(n+1)} \to E = T\mathbb{P}^n \otimes \mathcal{O}(-1)$, the section $s$ at the point $x = [x_0 : \cdots : x_n]$ is the projection of $(a_0, \ldots, a_n)$ modulo the line $\text{span}(x_0, \ldots, x_n)$ (which is the image of $\mathcal{O}(-1) \to \mathcal{O}^{\oplus(n+1)}$ fiberwise).

Thus $s(x) = 0$ if and only if $(a_0, \ldots, a_n) \in \text{span}(x_0, \ldots, x_n)$, i.e., $[x_0 : \cdots : x_n] = [a_0 : \cdots : a_n]$.

For any nonzero $(a_0, \ldots, a_n)$, the section vanishes at the point $[a_0 : \cdots : a_n] \in \mathbb{P}^n$.

**No nowhere-zero section exists.** (Valid in all characteristics.)

### Step 3: $d = 1$ — Every Vector Field Vanishes Somewhere

Here $E = T\mathbb{P}^n$ and $H^0(T\mathbb{P}^n) \cong \mathfrak{pgl}_{n+1}(k)$, the Lie algebra of $(n+1)\times(n+1)$ matrices modulo scalars.

A vector field corresponds to a matrix $A \in M_{(n+1)\times(n+1)}(k)$ (defined up to adding a scalar matrix). The vector field vanishes at $x = [x_0 : \cdots : x_n]$ if and only if $Ax$ is proportional to $x$, i.e., $x$ is an eigenvector of $A$.

**Key fact:** Over an algebraically closed field, every $(n+1)\times(n+1)$ matrix has an eigenvalue (the characteristic polynomial splits completely), hence has an eigenvector. This holds in **any characteristic**.

Therefore every vector field on $\mathbb{P}^n$ vanishes at some point (the eigenvector of the corresponding matrix).

**No nowhere-zero section exists.** (Valid in all characteristics.)

### Step 4: $d \geq 2$ — Chern Class Obstruction (Characteristic $0$)

This is the only step requiring characteristic $0$.

**Necessary condition.** If $E$ has a nowhere-zero section, then $E \cong \mathcal{O} \oplus F$ where $F$ is a vector bundle of rank $n - 1$. Since $F$ has rank $n-1 < n$, its top Chern class satisfies $c_n(F) = 0$, and therefore:
$$c_n(E) = c_n(\mathcal{O} \oplus F) = c_n(\mathcal{O}) \cdot c_n(F) = 1 \cdot 0 = 0.$$

So **$c_n(E) = 0$ is a necessary condition** for a nowhere-zero section to exist.

**Computing $c_n(E)$.** From the Euler sequence, $c(T\mathbb{P}^n) = (1+H)^{n+1}$, so $c_k(T\mathbb{P}^n) = \binom{n+1}{k} H^k$ where $H = c_1(\mathcal{O}(1))$ is the hyperplane class.

The Chern roots of $T\mathbb{P}^n$ are formal elements $\alpha_1, \ldots, \alpha_n$ with $\prod_{i=1}^n(1+\alpha_i) = (1+H)^{n+1}$. Tensoring by $\mathcal{O}(d-1)$ shifts each Chern root to $\alpha_i + (d-1)H$, so:

$$c_n(E) = \prod_{i=1}^{n}\bigl(\alpha_i + (d-1)H\bigr) = \sum_{k=0}^{n} \binom{n+1}{k}(d-1)^{n-k}\, H^n.$$

Setting $u = d - 1$, this sum equals:
$$\sum_{k=0}^{n}\binom{n+1}{k}u^{n-k} = \frac{(1+u)^{n+1} - 1}{u} = \frac{d^{n+1} - 1}{d - 1} = 1 + d + d^2 + \cdots + d^n$$

(for $d \neq 1$; for $d = 1$ the value is $n+1$, consistent with the limit). Thus:

$$\boxed{c_n(E) = (1 + d + d^2 + \cdots + d^n)\, H^n.}$$

**Characteristic $0$ analysis.** For $d \geq 2$ in characteristic $0$:
$$1 + d + d^2 + \cdots + d^n = \frac{d^{n+1} - 1}{d - 1} > 0,$$
since $d \geq 2$ implies $d^{n+1} > 1$ and $d - 1 > 0$. Therefore $c_n(E) \neq 0$, contradicting the necessary condition.

**No nowhere-zero section exists for $d \geq 2$ in characteristic $0$.**

---

## Summary

| Range of $d$ | $n = 1$ | $n \geq 2$ (char $0$) | Reason |
|---|---|---|---|
| $d \leq -2$ | $H^0 = 0$ | $H^0 = 0$ | No sections |
| $d = -1$ | ✓ $\mathcal{O}$ has constant section | $H^0 = 0$ | $n=1$: $\mathcal{O}(0)$; $n\geq2$: no sections |
| $d = 0$ | Polynomial has zero | Every section vanishes at $[a]$ | Direct analysis |
| $d = 1$ | Polynomial has zero | Every vector field vanishes (eigenvector) | Matrix eigenvalue argument |
| $d \geq 2$ | Polynomial has zero | $c_n(E) \neq 0$ | Chern class obstruction (char $0$) |

**Final answer (characteristic $0$):**

$$\boxed{d = -1 \text{ if } n = 1; \quad \text{no integer } d \text{ works if } n \geq 2.}$$

### PROOF COMPLETE
