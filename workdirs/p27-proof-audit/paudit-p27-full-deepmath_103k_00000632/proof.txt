# Proof: Local Injectivity under a.e. Orientation-Preserving Isometric Differential

## Answer

$$\boxed{\text{No}}$$

There need not exist any ball $B_\epsilon(p)\subseteq M$ on which $f$ is injective. We construct a counterexample valid for every dimension $d\geq 1$.

---

## Step 1 — Two disjoint dense singular measures of disjoint support

Partition $\mathbb{Q}\cap[0,1]$ into two disjoint dense sets $Q^+=\{q_1,q_2,\dots\}$ and $Q^-=\{r_1,r_2,\dots\}$.

Inductively choose pairwise disjoint Cantor sets $C_n^+\subseteq(q_n-2^{-n-3},\,q_n+2^{-n-3})$ and $C_n^-\subseteq(r_n-2^{-n-3},\,r_n+2^{-n-3})$, each of Lebesgue measure $0$, with all $\{C_n^+,C_n^-\}_{n\geq 1}$ pairwise disjoint. (At step $n$ the union of previously chosen sets is closed and nowhere dense, so a Cantor set of measure $0$ fits inside the prescribed interval avoiding it.)

Let $\mu_n^\pm$ be the Cantor probability measure supported on $C_n^\pm$ (continuous, no atoms), and set
$$
\mu^+ = \sum_{n=1}^{\infty} 2^{-n}\,\mu_n^+,\qquad
\mu^- = \sum_{n=1}^{\infty} 2^{-n}\,\mu_n^-.
$$

**Properties of $\mu^\pm$.**

- Each $\mu^\pm$ is a probability measure on $[0,1]$, continuous (no atoms), since each $\mu_n^\pm$ is.
- $\operatorname{supp}\mu^+ = D^+ := \bigcup_n C_n^+$ and $\operatorname{supp}\mu^- = D^- := \bigcup_n C_n^-$.
- $D^+\cap D^-=\varnothing$ (pairwise disjoint construction).
- $D^+$ and $D^-$ are both **dense** in $[0,1]$: every $q_n$ is within $2^{-n-3}$ of $C_n^+$, and $\{q_n\}$ is dense, so $D^+$ is dense; likewise $D^-$.
- $\mu^\pm$ are **singular** w.r.t. Lebesgue measure, since $D^\pm$ has measure $0$.

---

## Step 2 — The function $f$

Define the signed distribution function
$$
g(x) = \mu^+([0,x]) - \mu^-([0,x]),\qquad x\in[0,1],
$$
extended to all of $\mathbb{R}$ by $g(x)=g(0)$ for $x<0$ and $g(x)=g(1)$ for $x>1$. Set
$$
f(x) = x + g(x).
$$

**Continuity.** $\mu^\pm$ have no atoms, so $g$ is continuous, hence $f$ is continuous.

**A.e. differentiability and $f'=1$ a.e.** Since $\mu^\pm$ are singular w.r.t. Lebesgue measure, the Radon–Nikodym derivative $d\mu^\pm/dx = 0$ a.e. By the Lebesgue decomposition theorem, $g'(x)=0$ for Lebesgue-a.e. $x$, hence
$$
f'(x) = 1 + g'(x) = 1\quad\text{a.e.}
$$
In dimension $d=1$, $f'=1$ is an orientation-preserving isometry a.e.

---

## Step 3 — $f$ is not injective on any interval

We use the classical fact (see Rudin, *Real and Complex Analysis*; or Folland, *Real Analysis*):

> **Fact (symmetric derivative of a singular measure).** If $\mu$ is a finite Borel measure singular w.r.t. Lebesgue measure, then for $\mu$-a.e. $x$,
> $$
> \lim_{r\to 0^+}\frac{\mu([x-r,x+r])}{2r}=+\infty.
> $$

In particular, for $\mu^-$-a.e. $x\in D^-$ this limit is $+\infty$, and likewise for $\mu^+$-a.e. $x\in D^+$.

Let $I\subseteq\mathbb{R}$ be any nonempty open interval.

### (a) $f$ is not strictly increasing on $I$

Since $D^-$ is dense, $D^-\cap I\neq\varnothing$. Pick $x\in D^-\cap I$ at which the symmetric derivative of $\mu^-$ is $+\infty$. For all sufficiently small $r>0$ with $[x-r,x+r]\subseteq I$:
- $\mu^-([x-r,x+r]) > 4r$ (by the symmetric-derivative fact),
- $\mu^+([x-r,x+r]) < r$ (since $\mu^+$ is a continuous measure, $\mu^+([x-r,x+r])\to 0$ as $r\to 0$).

Then
$$
g(x+r)-g-r) = \mu^+([x-r,x+r]) - \mu^-([x-r,x+r]) < r - 4r = -3r,
$$
so
$$
f(x+r)-f(x-r) = 2r + \bigl(g(x+r)-g(x-r)\bigr) < 2r - 3r = -r < 0.
$$
Since $x+r > x-r$ yet $f(x+r) < f(x-r)$, the function $f$ is **not strictly increasing** on $I$.

### (b) $f$ is not strictly decreasing on $I$

Symmetrically, $D^+\cap I\neq\varnothing$. Pick $y\in D^+\cap I$ at which the symmetric derivative of $\mu^+$ is $+\infty$. For small $r>0$:
- $\mu^+([y-r,y+r]) > 4r$,
- $\mu^-([y-r,y+r]) < r$.

Then
$$
g(y+r)-g(y-r) = \mu^+([y-r,y+r]) - \mu^-([y-r,y+r]) > 4r - r = 3r,
$$
so
$$
f(y+r)-f(y-r) = 2r + 3r = 5r > 0.
$$
Since $y+r > y-r$ and $f(y+r) > f(y-r)$, the function $f$ is **not strictly decreasing** on $I$.

### (c) Conclusion for $d=1$

A continuous function on an interval is injective if and only if it is strictly monotone. Since $f$ is continuous on $I$ and is neither strictly increasing nor strictly decreasing, $f$ is **not injective on $I$**.

As every open ball in $\mathbb{R}$ contains an open interval, $f$ is not injective on any ball.

---

## Step 4 — Higher dimensions $d\geq 2$

Take $M=N=\mathbb{R}^d$ with the Euclidean metric. Define
$$
F(x_1,x_2,\dots,x_d) = \bigl(f(x_1),\,x_2,\,\dots,\,x_d\bigr),
$$
where $f$ is the 1D function from Step 2.

**Continuity.** $F$ is continuous since $f$ is.

**A.e. differentiability.** By Fubini's theorem, $f$ is differentiable for a.e. $x_1$, so $F$ is differentiable for a.e. $(x_1,\dots,x_d)\in\mathbb{R}^d$.

**Differential is an orientation-preserving isometry a.e.** At every point of differentiability,
$$
dF = \begin{pmatrix} f'(x_1) & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} = I_d\quad\text{a.e.},
$$
since $f'=1$ a.e. The identity $I_d\in SO(d)$ is an orientation-preserving isometry.

**Non-injectivity on every ball.** Let $B_\epsilon(p)\subseteq\mathbb{R}^d$ be any ball. The line segment
$$
\ell = \bigl\{(t,\,p_2,\,\dots,\,p_d) : t\in(p_1-\epsilon,\,p_1+\epsilon)\bigr\}\subseteq B_\epsilon(p)
$$
is mapped by $F$ to $\{(f(t),\,p_2,\,\dots,\,p_d):t\in(p_1-\epsilon,p_1+\epsilon)\}$. By Step 3, $f$ is not injective on $(p_1-\epsilon,p_1+\epsilon)$, so there exist $t_1\neq t_2$ with $f(t_1)=f(t_2)$. Then
$$
F(t_1,p_2,\dots,p_d) = F(t_2,p_2,\dots,p_d),
$$
yet $(t_1,p_2,\dots,p_d)\neq(t_2,p_2,\dots,p_d)$. Hence $F$ is not injective on $B_\epsilon(p)$.

---

## Step 5 — Riemannian manifold setting

The above gives a counterexample on $M=N=\mathbb{R}^d$ (a $d$-dimensional Riemannian manifold). For general $d$-dimensional Riemannian manifolds, take any coordinate chart and transport the construction inward; the conclusion is the same. Thus the answer is negative in general.

---

## Why Positive Results Fail Here

One might hope for a positive answer via Reshetnyak's theory of quasiregular mappings: $dF=I$ a.e. implies the distortion $K=1$, which would force $F$ to be open and discrete (hence locally injective off a discrete branch set). However, Reshetnyak's theorem requires $F\in W^{1,d}_{\mathrm{loc}}$, in particular the ACL (absolute continuity on lines) property. The hypothesis of mere a.e. differentiability does **not** imply ACL — our function $f(x)=x+g(x)$ with $g$ a singular-measure distribution function is the canonical counterexample: it is differentiable a.e. with $f'=1$ but is not absolutely continuous. Hence the Sobolev/quasiregular machinery does not apply, and no local injectivity can be guaranteed.

---

### PROOF COMPLETE

$$\boxed{\text{No}}$$
