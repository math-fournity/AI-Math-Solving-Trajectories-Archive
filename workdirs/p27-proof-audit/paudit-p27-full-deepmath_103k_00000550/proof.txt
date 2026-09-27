# Proof: Any bending of the cylinder $M$ leaves the bases planar

**Answer: YES.** Every bending of $M$ leaves both boundary circles planar.

---

## Setup

Let
$$
M=\{(\cos\theta,\sin\theta,z):\theta\in[0,2\pi],\,z\in[0,1]\}
$$
be the unit cylinder of height $1$, with the induced metric. Parametrizing by $(\theta,z)$, the first fundamental form is
$$
\mathrm{I}=d\theta^{2}+dz^{2},
$$
a **flat metric**. The two boundary components are the circles $C_0=\{z=0\}$ and $C_1=\{z=1\}$.

A bending $\Gamma:M\times[0,1]\to\mathbb{R}^3$ produces, for each $t$, an isometric embedding $M\to M_t=\Gamma(M,t)\subset\mathbb{R}^3$ with $M_0=M$. We must show each $M_t$ has both boundary curves planar.

Fix $t$ and write $M_t$ throughout. We prove every such $M_t$ has planar boundary curves.

---

## Step 1. $M_t$ is a developable surface

The Gauss curvature $K$ of $M$ is identically $0$ (flat metric). By the **Theorema Egregium**, $K$ is preserved under isometry, so $K\equiv 0$ on $M_t$. Hence $M_t$ is a **developable surface**: locally ruled by straight-line segments (rulings) along which the tangent plane is constant.

## Step 2. $M_t$ is not a plane; it carries a global ruling structure

An isometry is a diffeomorphism, so $M_t$ is homeomorphic to $M\cong S^1\times[0,1]$ (an annulus). A plane is simply connected; an annulus is not. Therefore $M_t$ is **not a plane**.

A non-planar developable surface in $\mathbb{R}^3$ is locally one of: a generalized cylinder (parallel rulings), a cone, or a tangent developable. Cones have an apex singularity and tangent developables have a cusp singularity along the edge curve; neither is a smooth submanifold at the singular point. Since $M_t$ is a smooth submanifold with boundary (condition 1), the only admissible type is a **generalized cylinder**: ruled by a family of parallel straight lines.

(More invariantly: the rulings of a smooth developable surface are the null directions of the second fundamental form. On a smooth annulus without singular points, these form a smooth line field whose integral curves are straight line segments in $\mathbb{R}^3$; the ruling direction varies smoothly. We will not need the full classification — only that rulings are straight lines, which holds for *any* developable surface.)

## Step 3. Rulings are geodesics; pulled back to $(\theta,z)$ they are straight lines

Each ruling is a straight line in $\mathbb{R}^3$, hence has zero curvature, hence zero geodesic curvature: **rulings are geodesics of $M_t$**. Under the isometry, geodesics correspond to geodesics. Geodesics of the flat metric $d\theta^2+dz^2$ on $S^1\times[0,1]$ are straight lines in the $(\theta,z)$-plane (lifted to the universal cover $\mathbb{R}\times[0,1]$). Therefore **each ruling pulls back to a straight line segment in the $(\theta,z)$-plane**.

## Step 4. Each ruling connects the two boundary components

A ruling pulled back to $(\theta,z)$ is a straight segment. Its endpoints lie on $\partial M=\{z=0\}\cup\{z=1\}$. If some ruling had both endpoints on the *same* boundary component, then by smoothness of the ruling direction field, nearby rulings would do the same, forming a "strip" hugging one boundary. The transition from such a strip to rulings crossing from $z=0$ to $z=1$ would force a ruling to become tangent to a boundary component, where the parametrization degenerates (Jacobian vanishes) — contradicting the smooth-submanifold condition. Hence **every ruling connects $C_0$ to $C_1$**.

## Step 5. Parametrization of $M_t$ by rulings

Parametrize the bottom boundary $C_0$ (pulled back, then mapped to $\mathbb{R}^3$) by arc length $s\in[0,2\pi)$:
$$
\gamma_0(s)=X(s,0),\qquad |\gamma_0'(s)|=1.
$$
The ruling starting at $\gamma_0(s)$ ends at a point $\gamma_1(g(s))$ on the top boundary, where $\gamma_1(u)=X(u,1)$ is the top boundary and $g:[0,2\pi)\to[0,2\pi)$ is a smooth map (a circle map, hence $g(s+2\pi)=g(s)+2\pi$ up to the $S^1$ identification). The pulled-back ruling is the straight segment from $(s,0)$ to $(g(s),1)$, i.e.
$$
(\theta,z)=\bigl((1-z)\,s+z\,g(s),\,z\bigr).
$$
Thus the surface is
$$
X(s,z)=(1-z)\,\gamma_0(s)+z\,\gamma_1(g(s)),\qquad z\in[0,1].
$$
Set
$$
D(s,z)=(1-z)+z\,g'(s),\qquad \alpha(s)=g(s)-s.
$$
Differentiating:
$$
X_s=(1-z)\,\gamma_0'(s)+z\,g'(s)\,\gamma_1'(g(s)),\qquad X_z=-\gamma_0(s)+\gamma_1(g(s)).
$$

## Step 6. The isometry conditions force parallel rulings

The metric on $M$ is $d\theta^2+dz^2$, so the isometry condition $X^*\mathrm{I}_{\mathrm{Eucl}}=d\theta^2+dz^2$ in $(s,z)$-coordinates reads (after the change of variables $\theta=(1-z)s+z\,g(s)$, whose Jacobian is $D$):
$$
E:=|X_s|^2=D^2,\qquad F:=X_s\cdot X_z=D\,\alpha,\qquad G:=|X_z|^2=\alpha^2+1.
$$

**From $G$:**
$$
|X_z|^2=|\gamma_1(g(s))-\gamma_0(s)|^2=\alpha(s)^2+1. \tag{G}
$$

**From $E=D^2$, expanded in powers of $z$.** Write $X_s=(1-z)A+z\,B$ with $A=\gamma_0'(s)$, $B=g'(s)\,\gamma_1'(g(s))$. Then
$$
|X_s|^2=(1-z)^2|A|^2+2z(1-z)\,A\cdot B+z^2|B|^2.
$$
Also $D^2=\bigl((1-z)+z\,g'\bigr)^2=(1-z)^2+2z(1-z)\,g'+z^2(g')^2$. Equating coefficients of $z^0,z^1,z^2$:
$$
|A|^2=1,\qquad A\cdot B=g',\qquad |B|^2=(g')^2.
$$
That is,
$$
|\gamma_0'(s)|=1,\qquad \gamma_0'(s)\cdot\gamma_1'(g(s))=1,\qquad |\gamma_1'(g(s))|=1. \tag{$\ast$}
$$
(The third equation uses $g'\neq 0$, which follows from $D\neq 0$ — needed for the change of variables to be regular — together with $|B|^2=(g')^2$ forcing $|\gamma_1'|=1$ when $g'\neq 0$; and $g'=0$ would make $D=1-z$ vanish at $z=1$, violating smoothness of $M_t$ at the top boundary.)

The middle equation of $(\ast)$ says two **unit** vectors have dot product $1$, so they are equal:
$$
\boxed{\;\gamma_0'(s)=\gamma_1'(g(s))\quad\text{for all }s.\;}
$$
Integrating from a fixed $s_0$:
$$
\gamma_1(g(s))-\gamma_0(s)=\gamma_1(g(s_0))-\gamma_0(s_0)=:c\quad\text{(constant vector)}.
$$
So **all rulings are parallel**, with common direction $c$. From (G):
$$
|c|^2=\alpha(s)^2+1\;\Longrightarrow\;\alpha(s)=\text{const}=:\alpha.
$$
Hence $g(s)=s+\alpha$ (constant shear), and $|c|^2=\alpha^2+1$.

## Step 7. Periodicity forces $\alpha=0$

From $\gamma_1(g(s))=\gamma_0(s)+c$ and $\gamma_0'(s)=\gamma_1'(g(s))$, differentiating $\gamma_1(s+\alpha)=\gamma_0(s)+c$ gives $\gamma_1'(s+\alpha)=\gamma_0'(s)$, consistent. Taking the dot product of $\gamma_0'(s)=\gamma_1'(g(s))$ with $c$ and using $\gamma_1(g(s))=\gamma_0(s)+c$:
$$
\gamma_0'(s)\cdot c = \alpha\quad\text{(constant, for all }s\text{)}.
$$
Decompose $\gamma_0'$ along $\hat c=c/|c|$ and its orthogonal complement:
$$
\gamma_0'(s)=\frac{\alpha}{|c|}\,\hat c\;+\;\gamma_0'^{\perp}(s),\qquad \gamma_0'^{\perp}\perp c,\quad |\gamma_0'^{\perp}|=\sqrt{1-\alpha^2/|c|^2}=\frac{1}{\sqrt{1+\alpha^2}}.
$$
Integrate over one period $[s,s+2\pi]$. Since $\gamma_0$ is a closed curve ($\gamma_0(s+2\pi)=\gamma_0(s)$):
$$
0=\gamma_0(s+2\pi)-\gamma_0(s)=\frac{2\pi\alpha}{|c|}\,\hat c+\int_s^{s+2\pi}\gamma_0'^{\perp}(u)\,du.
$$
The first term is **parallel** to $\hat c$; the integral is **perpendicular** to $c$ (hence to $\hat c$). Two orthogonal vectors summing to zero must each be zero. In particular
$$
\frac{2\pi\alpha}{|c|}=0\;\Longrightarrow\;\boxed{\;\alpha=0.\;}
$$

## Step 8. With $\alpha=0$, both boundary curves are planar

$\alpha=0$ gives:
- $g(s)=s$: rulings are vertical in $(\theta,z)$, i.e. each ruling connects $(s,0)$ to $(s,1)$.
- $|c|^2=0+1=1$, so $|c|=1$.
- $\gamma_0'(s)\cdot c=\alpha=0$ for all $s$: **$c$ is perpendicular to every tangent vector of $\gamma_0$**.

A curve all of whose tangents are perpendicular to a fixed vector $c$ lies in a plane perpendicular to $c$: indeed $\frac{d}{ds}(\gamma_0(s)\cdot c)=\gamma_0'(s)\cdot c=0$, so $\gamma_0(s)\cdot c=\text{const}$. Therefore **$\gamma_0$ is planar**, lying in the plane $\{x\cdot c=\text{const}\}$.

Since $\gamma_1(s)=\gamma_0(s)+c$, the top boundary $\gamma_1$ lies in the parallel plane $\{x\cdot c=\text{const}+|c|^2\}$.

## Step 9. Conclusion

For every $t$, both boundary curves of $M_t=\Gamma(M,t)$ lie in (parallel) planes. Therefore **any bending of $M$ leaves the bases planar**.

$$
\boxed{\text{Yes. Every bending of }M\text{ leaves both boundary circles planar.}}
$$

---

## Remark (non-trivial bendings exist)

The conclusion does *not* force the bending to be a rigid motion. The bottom curve $\gamma_0$ may be any closed plane curve of length $2\pi$ (arc-length parametrized, with $\int_0^{2\pi}\kappa\,ds=2\pi$), not necessarily a circle; the surface $\gamma_0(s)+z\,c$ ($c$ a unit normal to the plane of $\gamma_0$) is then an isometric embedding of $M$ with planar but non-circular bases. What the proof rules out is only *non-planarity* of the bases, not non-circularity.
