# Is $S(A)$ weak${}^*$ compact if $A$ is a non-zero, non-unital $C^*$-algebra?

## Answer

$$\boxed{\text{No.}$$

There exists a non-zero, non-unital $C^*$-algebra $A$ such that $S(A)$ is not weak${}^*$ compact. In particular, $A = C_0(\mathbb{R})$ is a counterexample.

---

## Preliminaries

Let $A$ be a $C^*$-algebra. A **state** on $A$ is a positive linear functional $\omega \in A^*$ with $\|\omega\| = 1$. The set of all states is
$$
S(A) = \{\omega \in A^* : \omega \geq 0,\; \|\omega\| = 1\}.
$$

Every state has norm $1$, so $S(A) \subseteq \overline{B}_{A^*}$, the closed unit ball of $A^*$. By the **Banach–Alaoglu theorem**, $\overline{B}_{A^*}$ is weak${}^*$ compact. Therefore
$$
S(A) \text{ is weak}^* \text{ compact} \iff S(A) \text{ is weak}^* \text{ closed in } A^*.
$$

**Unital case (for contrast).** If $A$ has a unit $\mathbf{1}$, then for every positive functional $\omega$ one has $\|\omega\| = \omega(\mathbf{1})$, so
$$
S(A) = \{\omega \in A^* : \omega \geq 0,\; \omega(\mathbf{1}) = 1\}.
$$
The positivity condition $\omega \geq 0$ is weak${}^*$ closed (it is the intersection of the weak${}^*$ closed half-spaces $\{\omega : \omega(a) \geq 0\}$ over $a \in A_+$), and the map $\omega \mapsto \omega(\mathbf{1})$ is weak${}^*$ continuous, so $\{\omega : \omega(\mathbf{1})=1\}$ is weak${}^*$ closed. Hence $S(A)$ is weak${}^*$ closed, and therefore weak${}^*$ compact.

The key point: in the unital case the norm condition $\|\omega\|=1$ can be rewritten as the weak${}^*$ continuous condition $\omega(\mathbf{1})=1$. In the **non-unital** case there is no unit element to play this role, and the norm condition $\|\omega\|=1$ is **not** weak${}^*$ closed (the norm is weak${}^*$ lower semi-continuous, so $\{\|\omega\|\leq 1\}$ is weak${}^*$ closed, but $\{\|\omega\|\geq 1\}$ is not). This suggests that $S(A)$ may fail to be weak${}^*$ closed, and we now exhibit a concrete counterexample.

---

## Counterexample: $A = C_0(\mathbb{R})$

Let
$$
A = C_0(\mathbb{R}) = \{f : \mathbb{R} \to \mathbb{C} \text{ continuous} : f(x) \to 0 \text{ as } |x|\to\infty\},
$$
with the supremum norm. This is a commutative $C^*$-algebra.

- **Non-zero:** The function $f(x) = e^{-x^2}$ lies in $A$ and is non-zero. ✓
- **Non-unital:** The constant function $\mathbf{1}$ does not vanish at infinity, so $\mathbf{1} \notin A$. ✓

By the **Riesz representation theorem**, the positive linear functionals on $C_0(\mathbb{R})$ are exactly the integration functionals against positive regular Borel measures, and the states are exactly the probability measures. In particular, for each $n \in \mathbb{N}$, the **point evaluation (Dirac measure)**
$$
\delta_n(f) := f(n), \qquad f \in C_0(\mathbb{R}),
$$
is a state:

- **Positivity:** If $f \geq 0$ pointwise, then $f(n) \geq 0$, so $\delta_n(f) \geq 0$. ✓
- **Norm one:** Clearly $|\delta_n(f)| = |f(n)| \leq \|f\|_\infty$, so $\|\delta_n\| \leq 1$. For the reverse inequality, take any $f \in C_0(\mathbb{R})$ with $f(n) = 1$ and $\|f\|_\infty = 1$ (such $f$ exists, e.g. a bump function peaked at $n$). Then $|\delta_n(f)| = 1 = \|f\|_\infty$, giving $\|\delta_n\| = 1$. ✓

Hence $\{\delta_n : n \in \mathbb{N}\} \subseteq S(A)$.

---

## The sequence $\delta_n$ converges weak${}^*$ to $0$

The weak${}^*$ topology on $A^*$ is the topology of pointwise convergence on elements of $A$. For any $f \in C_0(\mathbb{R})$, by definition $f(x) \to 0$ as $|x| \to \infty$, so in particular
$$
\delta_n(f) = f(n) \xrightarrow{n\to\infty} 0.
$$
Therefore $\delta_n \to 0$ in the weak${}^*$ topology, where $0 \in A^*$ denotes the zero functional.

---

## $0 \notin S(A)$

The zero functional has norm $\|0\| = 0 \neq 1$, so it is not a state. Thus $0 \notin S(A)$.

---

## Conclusion

We have exhibited a sequence $\{\delta_n\} \subseteq S(A)$ with $\delta_n \to 0$ in the weak${}^*$ topology, but $0 \notin S(A)$. Therefore $S(A)$ is **not** weak${}^*$ closed. Since $S(A) \subseteq \overline{B}_{A^*}$ (which is weak${}^*$ compact by Banach–Alaoglu), a subset of a compact space is compact if and only if it is closed. Hence $S(A)$ is **not** weak${}^*$ compact.

This shows that for the non-zero, non-unital $C^*$-algebra $A = C_0(\mathbb{R})$, the state space $S(A)$ is not weak${}^*$ compact. $\blacksquare$

---

### Remark

In fact one can show the sharper result: $S(A)$ is weak${}^*$ compact **if and only if** $A$ is unital. The reverse direction is the unital argument above; the forward direction follows because if $A$ is non-unital, one can always construct a net of states converging weak${}^*$ to $0$ (using the structure theory of non-unital $C^*$-algebras — approximate units, hereditary subalgebras, or the one-point unitization). The counterexample $A = C_0(\mathbb{R})$ above is the concrete, most transparent instance of this general phenomenon.
