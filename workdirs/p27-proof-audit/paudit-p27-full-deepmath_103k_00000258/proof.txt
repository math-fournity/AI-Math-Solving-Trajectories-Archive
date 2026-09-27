# Proof

**Question.** Is it consistent with ZF set theory that there is no uncountable set of algebraically independent real numbers?

**Answer.** No. In fact, ZF proves that there exists an uncountable (indeed perfect) set of algebraically independent reals. Hence (assuming ZF is consistent) the theory ZF + "there is no uncountable algebraically independent set of reals" is inconsistent.

---

## Setup and notation

A set $A \subseteq \mathbb{R}$ is *algebraically independent* (over $\mathbb{Q}$) if for every finite distinct $a_1, \dots, a_n \in A$ and every nonzero polynomial $p \in \mathbb{Q}[X_1, \dots, X_n]$, we have $p(a_1, \dots, a_n) \neq 0$.

For each $n \geq 1$, let
$$
A_n = \{(x_1, \dots, x_n) \in \mathbb{R}^n : x_1, \dots, x_n \text{ are distinct and algebraically independent}\}.
$$

---

## Step 1: $A_n$ is comeager in $\mathbb{R}^n$ (in ZF)

The complement $\mathbb{R}^n \setminus A_n$ is the union of:

- $D_n = \bigcup_{1 \leq i < j \leq n} \{x \in \mathbb{R}^n : x_i = x_j\}$: the set of tuples with a repeated entry. This is a finite union of hyperplanes, each closed and nowhere dense (in ZF).

- $E_n = \bigcup_{p \in \mathbb{Q}[X_1,\dots,X_n] \setminus \{0\}} Z(p)$, where $Z(p) = \{x \in \mathbb{R}^n : p(x) = 0\}$. Each $Z(p)$ is closed (it is the zero set of a continuous function). Each $Z(p)$ is nowhere dense: a nonzero polynomial in $n$ variables cannot vanish on any nonempty open box, since on any line parallel to a coordinate axis along which the polynomial is not identically zero, it has only finitely many roots. The ring $\mathbb{Q}[X_1, \dots, X_n]$ is countable (provably in ZF: it is a countable union of finite-dimensional spaces over $\mathbb{Q}$, each with a canonical basis of monomials). So $E_n$ is a countable union of closed nowhere dense sets, i.e., meager.

Therefore $\mathbb{R}^n \setminus A_n = D_n \cup E_n$ is meager, and $A_n$ is comeager. $\square$

---

## Step 2: Mycielski's theorem for $\mathbb{R}$ is provable in ZF

**Theorem (Mycielski).** *Let $R_n \subseteq \mathbb{R}^n$ ($n \geq 1$) be comeager relations. Then there exists a perfect set $P \subseteq \mathbb{R}$ such that for every $n$ and every distinct $x_1, \dots, x_n \in P$, $(x_1, \dots, x_n) \in R_n$.*

We prove this in ZF for $X = \mathbb{R}$.

### Why no choice is needed

The key point is that $\mathbb{R}$ has a *countable base* (the set of open intervals with rational endpoints), which can be well-ordered canonically. This allows deterministic "least element" selections at every step of the construction, replacing any appeal to the axiom of choice.

### Proof of the theorem (ZF)

For each $n$, since $R_n$ is comeager, write $\mathbb{R}^n \setminus R_n = \bigcup_{k=0}^{\infty} F_{n,k}$ where each $F_{n,k} \subseteq \mathbb{R}^n$ is closed nowhere dense. (This decomposition is available in ZF: comeager = complement of a countable union of closed nowhere dense sets, and the Baire category theorem for $\mathbb{R}^n$ — a complete separable metric space — is provable in ZF using the countable base for deterministic choices.)

We construct a binary tree of closed intervals $(I_s)_{s \in 2^{<\omega}}$ with rational endpoints, satisfying:

1. **Nesting:** $I_s \subseteq I_t$ and $I_s \cap I_t = \emptyset$ whenever $s \supsetneq t$ and $s, t$ are at the same level (siblings and cousins are disjoint).
2. **Shrinking:** $|I_s| \leq 2^{-|s|}$ (length at most $2^{-n}$ at level $n$).
3. **Avoidance:** For every level $n$, every $m$-element subset $\{i_1 < \cdots < i_m\} \subseteq \{0, \dots, n\}$ (indexing $m$ of the $2^{n+1}$ branches at level $n+1$), and every $k \leq n$, the "box"
$$
I_{s_{i_1}} \times \cdots \times I_{s_{i_m}} \subseteq \mathbb{R}^m
$$
is disjoint from $F_{m,k}$.

**Construction at level $n \to n+1$ (simultaneous selection of all $2^{n+1}$ children):**

Suppose $(I_s)_{|s|=n}$ have been chosen. We must choose, for each of the $2^n$ parent nodes $s$ at level $n$, two disjoint subintervals $I_{s\frown 0}, I_{s\frown 1} \subseteq I_s$ (with rational endpoints, small enough), such that condition (3) holds for all relevant $m$-subsets and all $k \leq n$.

The conditions to satisfy are all of the form: *a certain product of chosen intervals must avoid a certain closed nowhere dense set $F_{m,k}$.* We argue these are *open dense* conditions on the tuple of all $2^{n+1}$ subintervals simultaneously.

- **Openness:** Avoiding a closed set is an open condition (if a product of open intervals is disjoint from a closed set, so is a small perturbation).
- **Denseness:** Given any initial choice of subintervals (within the parents), we can shrink them to avoid any fixed closed nowhere dense set $F_{m,k}$, because $F_{m,k}$ is nowhere dense — its complement is open and dense, so within any open box we can find a smaller open box avoiding it.

There are only *finitely many* conditions at each level (finitely many $m$-subsets of $\{0,\dots,n\}$, finitely many $k \leq n$). A finite intersection of open dense conditions is open dense. Since the parameter space (tuples of rational-endpoint intervals inside the parents) has a countable dense subset (rational-endpoint intervals), we can **search the canonical enumeration** and pick the *first* tuple of subintervals satisfying all conditions. This is a deterministic, choice-free selection.

**Remark on the "simultaneous" selection.** We select all $2^{n+1}$ children at once, rather than one at a time. This is essential: if we selected children one by one, the condition "the product of the $i$-th child with the (already chosen) $j$-th child avoids $F_{2,k}$" involves a *projection* of $F_{2,k}$, and the projection of a closed nowhere dense set need not be closed or nowhere dense. By selecting all children simultaneously, we work directly with the original closed nowhere dense sets $F_{m,k} \subseteq \mathbb{R}^m$, avoiding projections entirely.

### Defining $P$ and verifying its properties

Let
$$
P = \bigcap_{n=0}^{\infty} \bigcup_{|s|=n} I_s.
$$

By the nesting and shrinking conditions, $P$ is a nonempty perfect set (homeomorphic to $2^\omega$): every branch through the tree gives a unique point, and every point is a limit of other branches.

**Algebraic independence.** Let $x_1, \dots, x_m \in P$ be distinct. Choose $n$ large enough that $x_1, \dots, x_m$ correspond to $m$ *distinct* nodes at level $n$ (possible since they are distinct points, hence eventually in different intervals). Then by condition (3), the box $I_{s_1} \times \cdots \times I_{s_m}$ is disjoint from $F_{m,k}$ for every $k \leq n$. Since $\mathbb{R}^m \setminus A_m = \bigcup_{k=0}^{\infty} F_{m,k}$ and $(x_1, \dots, x_m)$ lies in this box, we have $(x_1, \dots, x_m) \notin F_{m,k}$ for $k \leq n$.

We need $(x_1, \dots, x_m) \notin F_{m,k}$ for *all* $k$, not just $k \leq n$. But condition (3) is enforced at *every* level $\geq n$: at level $n' \geq n$, the intervals containing $x_1, \dots, x_m$ still form a box avoiding $F_{m,k}$ for all $k \leq n'$. Since $n'$ can be taken arbitrarily large, $(x_1, \dots, x_m)$ avoids $F_{m,k}$ for every $k$. Hence $(x_1, \dots, x_m) \in A_m$, i.e., $x_1, \dots, x_m$ are algebraically independent.

Since $m$ was arbitrary, every finite subset of $P$ is algebraically independent, so $P$ is an algebraically independent set. $\square$

---

## Step 3: $P$ is uncountable (in ZF)

A perfect subset of $\mathbb{R}$ is uncountable, and this is provable in ZF.

*Proof.* Suppose $P$ is perfect and $\{y_0, y_1, y_2, \dots\} \subseteq P$ is any countable sequence (given by a function $f: \omega \to P$). We construct a point $x \in P \setminus \{y_n : n \in \omega\}$ by a diagonal argument using the countable base.

Since $P$ is perfect, $y_0$ is not isolated in $P$. Pick (deterministically, using the canonical enumeration of rational-endpoint intervals) a closed interval $J_0 \subseteq I_{\emptyset}$ (the root interval) with $J_0 \cap P \neq \emptyset$ and $y_0 \notin J_0$. Since $P \cap J_0$ is still perfect (as a subset of $P$), pick a subinterval $J_1 \subseteq J_0$ with $P \cap J_1 \neq \emptyset$ and $y_1 \notin J_1$, with $|J_1| \leq 1/2$. Continue: at stage $n$, pick $J_{n+1} \subseteq J_n$ with $P \cap J_{n+1} \neq \emptyset$, $y_{n+1} \notin J_{n+1}$, and $|J_{n+1}| \leq 2^{-(n+1)}$.

All selections use the canonical enumeration of rational-endpoint intervals (pick the first one satisfying the conditions), so no choice axiom is needed. By compactness, $\bigcap_n J_n \neq \emptyset$; let $x \in \bigcap_n J_n$. Then $x \in P$ (since $P \cap J_n \neq \emptyset$ for all $n$ and $P$ is closed) and $x \neq y_n$ for every $n$ (since $y_n \notin J_n \ni x$).

Therefore no countable sequence enumerates $P$, so $P$ is uncountable. $\square$

(In fact, $P$ has cardinality $2^{\aleph_0}$, since the map $2^\omega \to P$ sending each branch to its limit point is a bijection, but uncountability suffices for our purpose.)

---

## Step 4: Conclusion

Combining Steps 1–3:

- (Step 1) Each $A_n$ is comeager in $\mathbb{R}^n$, provably in ZF.
- (Step 2, Mycielski's theorem) There exists a perfect set $P \subseteq \mathbb{R}$ such that every finite subset of $P$ is algebraically independent, provably in ZF.
- (Step 3) $P$ is uncountable, provably in ZF.

Therefore:
$$
\text{ZF} \vdash \text{``there exists an uncountable algebraically independent set of reals.''}
$$

Consequently, if ZF is consistent, then ZF + "there is no uncountable algebraically independent set of reals" is **inconsistent**. The answer to the question is:

$$
\boxed{\text{No}}
$$

### PROOF COMPLETE
