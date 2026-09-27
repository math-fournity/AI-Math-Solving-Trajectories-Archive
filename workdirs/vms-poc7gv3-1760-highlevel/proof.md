# Proof: $\angle BEA_1 = 90°$ and $\angle AEB_1 = 90°$

## Problem Statement

In triangle $ABC$, let $J$ be the centre of the excircle tangent to side $BC$ at $A_1$ and to the extensions of sides $AC$ and $AB$ at $B_1$ and $C_1$, respectively. Suppose that the lines $A_1B_1$ and $AB$ are perpendicular and intersect at $D$. Let $E$ be the foot of the perpendicular from $C_1$ to line $DJ$. Determine the angles $\angle BEA_1$ and $\angle AEB_1$.

**Answer:** $\angle BEA_1 = 90°$ and $\angle AEB_1 = 90°$.

---

## Step 1: The perpendicularity condition forces the triangle to be isosceles

Let $a = BC$, $b = CA$, $c = AB$, and $s = \frac{a+b+c}{2}$. Place $B$ at the origin and $A$ at $(c, 0)$, so $AB$ lies along the $x$-axis. Then $C = (a\cos B,\; a\sin B)$ where $\cos B = \frac{a^2 + c^2 - b^2}{2ac}$.

**Tangent lengths for the $A$-excircle.** The excircle opposite $A$ is tangent to $BC$ at $A_1$, to the extension of $AB$ beyond $B$ at $C_1$, and to the extension of $AC$ beyond $C$ at $B_1$. The tangent lengths are:

$$BA_1 = BC_1 = s - c, \qquad CA_1 = CB_1 = s - b, \qquad AC_1 = AB_1 = s.$$

**Computing the $x$-coordinates.**

- $A_1 = \frac{s-c}{a}\,C$, so $x_{A_1} = (s-c)\cos B$.
- $B_1 = C + \frac{s-b}{b}(C - A)$, so $x_{B_1} = a\cos B + \frac{s-b}{b}(a\cos B - c) = \frac{sa\cos B - (s-b)c}{b}$.

The condition $A_1B_1 \perp AB$ means $A_1B_1$ is vertical (since $AB$ is horizontal), i.e., $x_{A_1} = x_{B_1}$:

$$(s - c)\cos B = \frac{sa\cos B - (s-b)c}{b}.$$

Rearranging:

$$b(s-c)\cos B = sa\cos B - (s-b)c \implies \cos B\bigl[b(s-c) - sa\bigr] = -(s-b)c.$$

Substituting $s = \frac{a+b+c}{2}$ and $\cos B = \frac{a^2+c^2-b^2}{2ac}$, and simplifying (expanding and factoring), the condition reduces to:

$$(a - b)(a - b + c)(a + b - c)(a + b + c) = 0.$$

For a non-degenerate triangle, the triangle inequality gives $a + b - c > 0$, $a - b + c > 0$, and $a + b + c > 0$. Therefore:

$$\boxed{a = b, \quad \text{i.e., } BC = CA.}$$

The triangle is isosceles with $CA = CB = a$ and $AB = c$, and $\cos B = \frac{c}{2a}$.

---

## Step 2: Coordinate setup for the isosceles triangle

Set $B = (0,\, 0)$, $A = (c,\, 0)$, and $C = \bigl(\frac{c}{2},\; h\bigr)$ where $h = \frac{\sqrt{4a^2 - c^2}}{2} = a\sin B$.

The semi-perimeter and tangent lengths become:

$$s = a + \frac{c}{2}, \quad s - c = \frac{2a - c}{2}, \quad s - a = \frac{c}{2}.$$

**Key points:**

| Point | Coordinates |
|-------|------------|
| $A_1$ | $\displaystyle\left(\frac{c(2a-c)}{4a},\;\frac{(2a-c)h}{2a}\right)$ |
| $C_1$ | $\displaystyle\left(-\frac{2a-c}{2},\;0\right)$ |
| $B_1$ | $\displaystyle\left(\frac{c(2a-c)}{4a},\;\frac{(2a+c)h}{2a}\right)$ |
| $D$ | $\displaystyle\left(\frac{c(2a-c)}{4a},\;0\right)$ |
| $J$ | $\displaystyle\left(\frac{c}{2} - a,\;h\right) = \left(-\frac{2a-c}{2},\;h\right)$ |

**Verification of key properties:**

- $x_{A_1} = x_{B_1} = \frac{c(2a-c)}{4a}$, confirming $A_1B_1 \perp AB$. ✓
- $x_J = x_{C_1} = -\frac{2a-c}{2}$, so $J$ lies directly above $C_1$ (the radius $JC_1$ is perpendicular to $AB$). ✓
- The excircle radius is $r_a = \frac{\text{Area}}{s - a} = \frac{ch/2}{c/2} = h$, and indeed $J$ is at distance $h$ from each tangent line. ✓

---

## Step 3: Computing the foot $E$

The line $DJ$ passes through $D = \bigl(\frac{c(2a-c)}{4a},\, 0\bigr)$ with direction

$$J - D = \left(-\frac{2a-c}{2} - \frac{c(2a-c)}{4a},\; h\right) = \left(\frac{-(2a-c)(2a+c)}{4a},\; h\right) = \left(\frac{-(4a^2-c^2)}{4a},\; h\right) = \left(\frac{-4h^2}{4a},\; h\right) = \left(\frac{-h^2}{a},\; h\right).$$

Since $4a^2 - c^2 = 4h^2$, the direction simplifies to $h\!\left(-\frac{h}{a},\; 1\right)$, so we take the direction vector as $(-h,\; a)$.

**Parametrization of line $DJ$:** $\;P(t) = D + t\,(-h,\; a) = \left(\frac{c(2a-c)}{4a} - ht,\; at\right)$.

**Foot of perpendicular from $C_1$:** The vector $C_1 - P(t)$ must be perpendicular to $(-h, a)$:

$$\left(C_1 - P(t)\right) \cdot (-h,\, a) = 0.$$

Computing $C_1 - P(t) = \left(-\frac{2a-c}{2} - \frac{c(2a-c)}{4a} + ht,\; -at\right) = \left(\frac{-(2a-c)(2a+c)}{4a} + ht,\; -at\right) = \left(\frac{-4h^2}{4a} + ht,\; -at\right) = \left(\frac{-h^2}{a} + ht,\; -at\right)$.

The dot product with $(-h, a)$:

$$-h\!\left(\frac{-h^2}{a} + ht\right) + a(-at) = \frac{h^3}{a} - h^2 t - a^2 t = 0,$$

$$t = \frac{h^3}{a(h^2 + a^2)}.$$

Therefore:

$$E = \left(\frac{c(2a-c)}{4a} - \frac{h^4}{a(h^2+a^2)},\;\frac{h^3}{h^2+a^2}\right).$$

---

## Step 4: Proving $\angle BEA_1 = 90°$

We show $\vec{EB} \cdot \vec{EA_1} = 0$.

**Simplification using $p = \cos B = \frac{c}{2a}$ and $q = \sin B = \frac{h}{a}$** (so $p^2 + q^2 = 1$, $c = 2ap$, $h = aq$). Dividing all coordinates by $a$ (which doesn't affect angles), we work with:

| Point | Coordinates (scaled by $1/a$) |
|-------|------|
| $B$ | $(0,\, 0)$ |
| $A$ | $(2p,\, 0)$ |
| $C$ | $(p,\, q)$ |
| $A_1$ | $\bigl(p(1-p),\; q(1-p)\bigr)$ |
| $C_1$ | $(p - 1,\, 0)$ |
| $B_1$ | $\bigl(p(1-p),\; q(1+p)\bigr)$ |
| $D$ | $\bigl(p(1-p),\, 0\bigr)$ |
| $J$ | $(p - 1,\, q)$ |

Direction of $DJ$: $(p-1-p(1-p),\; q) = (p-1-p+p^2,\; q) = (p^2-1,\; q) = (-q^2,\; q) = q(-q,\, 1)$, so direction $(-q,\, 1)$.

Parameter: $t = \frac{q^3}{1 + q^2}$ (using $h \to q$, $a \to 1$ in the formula above).

$$E = \left(p(1-p) - \frac{q^4}{1+q^2},\;\frac{q^3}{1+q^2}\right).$$

Since $1 + q^2 = 2 - p^2$ and $q^2 = 1 - p^2$:

$$E_x = \frac{(1-p)(p^2+p-1)}{2-p^2}, \qquad E_y = \frac{q^3}{2-p^2}.$$

**Vectors:**

$$\vec{EB} = (-E_x,\,-E_y) = \left(\frac{-(1-p)(p^2+p-1)}{2-p^2},\;\frac{-q^3}{2-p^2}\right).$$

$$\vec{EA_1} = \bigl(p(1-p)-E_x,\; q(1-p)-E_y\bigr).$$

Computing the components:

$$p(1-p) - E_x = (1-p)\!\left(p - \frac{p^2+p-1}{2-p^2}\right) = (1-p)\cdot\frac{p(2-p^2)-(p^2+p-1)}{2-p^2} = (1-p)\cdot\frac{(1+p)^2(1-p)}{2-p^2} = \frac{(1-p^2)^2}{2-p^2} = \frac{q^4}{2-p^2}.$$

$$q(1-p) - E_y = q\!\left((1-p) - \frac{q^2}{2-p^2}\right) = q\cdot\frac{(1-p)(2-p^2)-(1-p^2)}{2-p^2} = q\cdot\frac{-(1-p)(p^2+p-1)}{2-p^2} = \frac{-q(1-p)(p^2+p-1)}{2-p^2}.$$

**Dot product:**

$$\vec{EB}\cdot\vec{EA_1} = \frac{-(1-p)(p^2+p-1)}{2-p^2}\cdot\frac{q^4}{2-p^2} + \frac{-q^3}{2-p^2}\cdot\frac{-q(1-p)(p^2+p-1)}{2-p^2} = \frac{-(1-p)(p^2+p-1)\,q^4 + (1-p)(p^2+p-1)\,q^4}{(2-p^2)^2} = 0.$$

Therefore $\angle BEA_1 = 90°$. $\quad\blacksquare$

---

## Step 5: Proving $\angle AEB_1 = 90°$

We show $\vec{EA} \cdot \vec{EB_1} = 0$.

**Vectors:**

$$\vec{EA} = (2p - E_x,\; -E_y).$$

$$2p - E_x = \frac{2p(2-p^2) - (1-p)(p^2+p-1)}{2-p^2} = \frac{4p - 2p^3 + p^3 - 2p + 1}{2-p^2} = \frac{1 + 2p - p^3}{2-p^2} = \frac{-(p+1)(p^2-p-1)}{2-p^2} = \frac{(p+1)(1+p-p^2)}{2-p^2}.$$

$$\vec{EB_1} = \bigl(p(1-p)-E_x,\; q(1+p)-E_y\bigr).$$

We already have $p(1-p) - E_x = \frac{q^4}{2-p^2}$.

$$q(1+p) - E_y = q\!\left((1+p) - \frac{q^2}{2-p^2}\right) = q\cdot\frac{(1+p)(2-p^2)-(1-p^2)}{2-p^2} = q\cdot\frac{1+2p-p^3}{2-p^2} = \frac{q(p+1)(1+p-p^2)}{2-p^2}.$$

**Dot product:**

$$\vec{EA}\cdot\vec{EB_1} = \frac{(p+1)(1+p-p^2)}{2-p^2}\cdot\frac{q^4}{2-p^2} + \frac{-q^3}{2-p^2}\cdot\frac{q(p+1)(1+p-p^2)}{2-p^2} = \frac{(p+1)(1+p-p^2)\,q^4 - (p+1)(1+p-p^2)\,q^4}{(2-p^2)^2} = 0.$$

Therefore $\angle AEB_1 = 90°$. $\quad\blacksquare$

---

## Conclusion

$$\boxed{\angle BEA_1 = 90° \qquad \text{and} \qquad \angle AEB_1 = 90°.}$$

**Proof summary:**

1. **Isosceles reduction:** The condition $A_1B_1 \perp AB$ forces $BC = CA$ (the triangle is isosceles with apex $C$). This follows from factoring the perpendicularity condition into $(a-b)(a-b+c)(a+b-c)(a+b+c) = 0$, where the triangle inequality eliminates all factors except $a - b$.

2. **Coordinate computation:** In the isosceles triangle, the excircle center $J$ lies directly above the tangent point $C_1$ (since $JC_1 \perp AB$). The line $DJ$ has a clean direction, and the foot $E$ of the perpendicular from $C_1$ to $DJ$ can be computed explicitly.

3. **Orthogonality:** A direct dot-product calculation shows $\vec{EB} \cdot \vec{EA_1} = 0$ and $\vec{EA} \cdot \vec{EB_1} = 0$, establishing both angles as right angles. The key algebraic identity making both dot products vanish is the cancellation between the $x$-component and $y$-component contributions, which arises from the symmetric structure of the isosceles triangle and the excircle tangent lengths.

**QED.**
