# Problem

Let $ABC$ be an acute triangle, and let $M$ be the midpoint of $AC$. A circle $\omega$ passing through $B$ and $M$ meets the sides $AB$ and $BC$ again at $P$ and $Q$, respectively. Let $T$ be the point such that the quadrilateral $BPTQ$ is a parallelogram. Suppose that $T$ lies on the circumcircle of the triangle $ABC$. Determine all possible values of $BT/BM$.

# Answer

$$\boxed{\dfrac{BT}{BM} = \sqrt{2}}$$

# Proof

## Setup

Place $B$ at the origin. Let $\vec{BA} = \mathbf{a}$ and $\vec{BC} = \mathbf{c}$. Then:

- $M$ is the midpoint of $AC$, so $\vec{BM} = \frac{\mathbf{a} + \mathbf{c}}{2}$.
- $P$ lies on line $AB$, so $\vec{BP} = t\,\mathbf{a}$ for some real number $t$.
- $Q$ lies on line $BC$, so $\vec{BQ} = s\,\mathbf{c}$ for some real number $s$.

Since $BPTQ$ is a parallelogram with vertices in order $B, P, T, Q$, the diagonal property gives:

$$\vec{BT} = \vec{BP} + \vec{BQ} = t\,\mathbf{a} + s\,\mathbf{c}.$$

## Key equation (1): Concyclicity of $B, P, M, Q$

A circle through the origin $B$ has equation

$$|\mathbf{x}|^2 + \mathbf{d} \cdot \mathbf{x} = 0$$

for some vector $\mathbf{d}$ (this is the general equation of a circle passing through the origin: $x^2 + y^2 + Dx + Ey = 0$ in coordinates).

**Through $P = t\,\mathbf{a}$:**

$$t^2|\mathbf{a}|^2 + t\,(\mathbf{d} \cdot \mathbf{a}) = 0 \implies \mathbf{d} \cdot \mathbf{a} = -t\,|\mathbf{a}|^2. \tag{$*$}$$

**Through $Q = s\,\mathbf{c}$:**

$$s^2|\mathbf{c}|^2 + s\,(\mathbf{d} \cdot \mathbf{c}) = 0 \implies \mathbf{d} \cdot \mathbf{c} = -s\,|\mathbf{c}|^2. \tag{$**$}$$

**Through $M = \frac{\mathbf{a}+\mathbf{c}}{2}$:**

$$\frac{|\mathbf{a}+\mathbf{c}|^2}{4} + \frac{\mathbf{d} \cdot (\mathbf{a}+\mathbf{c})}{2} = 0.$$

Substituting $(*)$ and $(**)$:

$$\frac{|\mathbf{a}+\mathbf{c}|^2}{4} + \frac{-t\,|\mathbf{a}|^2 - s\,|\mathbf{c}|^2}{2} = 0,$$

which rearranges to:

$$|\mathbf{a}+\mathbf{c}|^2 = 2\!\left(t\,|\mathbf{a}|^2 + s\,|\mathbf{c}|^2\right). \tag{1}$$

## Key equation (2): $T$ on the circumcircle of $ABC$

The circumcircle of $ABC$ passes through $B = \mathbf{0}$, $A = \mathbf{a}$, $C = \mathbf{c}$, so it has equation

$$|\mathbf{x}|^2 + \mathbf{e} \cdot \mathbf{x} = 0$$

where $\mathbf{e} \cdot \mathbf{a} = -|\mathbf{a}|^2$ and $\mathbf{e} \cdot \mathbf{c} = -|\mathbf{c}|^2$.

**$T = t\,\mathbf{a} + s\,\mathbf{c}$ on this circle:**

$$|t\,\mathbf{a} + s\,\mathbf{c}|^2 + \mathbf{e} \cdot (t\,\mathbf{a} + s\,\mathbf{c}) = 0.$$

Expanding:

$$\underbrace{|t\,\mathbf{a} + s\,\mathbf{c}|^2}_{BT^2} + t\,(\mathbf{e} \cdot \mathbf{a}) + s\,(\mathbf{e} \cdot \mathbf{c}) = 0,$$

$$BT^2 - t\,|\mathbf{a}|^2 - s\,|\mathbf{c}|^2 = 0,$$

giving:

$$BT^2 = t\,|\mathbf{a}|^2 + s\,|\mathbf{c}|^2. \tag{2}$$

## Combining (1) and (2)

From equation (2): $\;BT^2 = t\,|\mathbf{a}|^2 + s\,|\mathbf{c}|^2$.

From equation (1): $\;t\,|\mathbf{a}|^2 + s\,|\mathbf{c}|^2 = \dfrac{|\mathbf{a}+\mathbf{c}|^2}{2}$.

Therefore:

$$BT^2 = \frac{|\mathbf{a}+\mathbf{c}|^2}{2}.$$

On the other hand:

$$BM^2 = \left|\frac{\mathbf{a}+\mathbf{c}}{2}\right|^2 = \frac{|\mathbf{a}+\mathbf{c}|^2}{4}.$$

Taking the ratio:

$$\frac{BT^2}{BM^2} = \frac{|\mathbf{a}+\mathbf{c}|^2/2}{|\mathbf{a}+\mathbf{c}|^2/4} = 2.$$

Since $BT$ and $BM$ are positive lengths:

$$\frac{BT}{BM} = \sqrt{2}.$$

## Existence

The value $\sqrt{2}$ is achievable. For example, take $B = (0,0)$, $A = (6,0)$, $C = (2,4)$. This is an acute triangle ($AB^2 = 36$, $BC^2 = 20$, $AC^2 = 32$; all sums of two exceed the third). The midpoint is $M = (4,2)$.

The circle $\omega: x^2 + y^2 - 5x = 0$ passes through $B = (0,0)$, $P = (5,0) \in AB$, $Q = (1,2) \in BC$, and $M = (4,2)$ (since $16 + 4 - 20 = 0$). The parallelogram point is $T = P + Q = (6,2)$, which lies on the circumcircle $x^2 + y^2 - 6x - 2y = 0$ (since $36 + 4 - 36 - 4 = 0$). One checks $BT = \sqrt{40}$, $BM = \sqrt{20}$, and $BT/BM = \sqrt{2}$.

## Conclusion

The only possible value is

$$\dfrac{BT}{BM} = \sqrt{2}. \qquad \blacksquare$$
