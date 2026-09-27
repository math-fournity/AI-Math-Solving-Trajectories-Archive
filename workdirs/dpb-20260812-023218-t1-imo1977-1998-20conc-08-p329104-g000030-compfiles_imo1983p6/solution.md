# IMO 1983 Problem 6 — Solution

## Problem

Suppose $a, b, c$ are the side lengths of a triangle. Prove that
$$a^2 b(a-b) + b^2 c(b-c) + c^2 a(c-a) \geq 0,$$
and determine when equality occurs.

## Proof

**Ravi substitution.** Since $a, b, c$ are the sides of a (non-degenerate) triangle, there exist $x, y, z > 0$ such that
$$a = y + z, \quad b = z + x, \quad c = x + y.$$
(This is the standard Ravi substitution, valid because each side is strictly less than the sum of the other two.)

**Rewrite the expression.** Let
$$S = a^2 b(a-b) + b^2 c(b-c) + c^2 a(c-a).$$
Substituting and expanding (verified by direct computation):
$$S = 2\bigl[x^3 z + x y^3 + y z^3 - xyz(x + y + z)\bigr].$$

**Key reduction.** Since $x, y, z > 0$, divide the bracket by $xyz > 0$:
$$\frac{x^3 z + x y^3 + y z^3 - xyz(x+y+z)}{xyz}
= \frac{x^2}{y} + \frac{y^2}{z} + \frac{z^2}{x} - (x + y + z).$$

So it suffices to prove
$$\frac{x^2}{y} + \frac{y^2}{z} + \frac{z^2}{x} \geq x + y + z \qquad (x, y, z > 0).$$

**Apply Cauchy–Schwarz (Engel / Titu form).** By the Cauchy–Schwarz inequality in Engel form,
$$\frac{x^2}{y} + \frac{y^2}{z} + \frac{z^2}{x} \geq \frac{(x + y + z)^2}{x + y + z} = x + y + z.$$

Therefore $S \geq 0$. $\blacksquare$

## Equality condition

Equality in Titu's lemma holds if and only if
$$\frac{x}{y} = \frac{y}{z} = \frac{z}{x}.$$
Let this common ratio be $k > 0$. Then $x = ky$, $y = kz$, $z = kx$, so $x = k^3 x$, giving $k^3 = 1$, hence $k = 1$. Thus $x = y = z$, which gives
$$a = y + z = 2x, \quad b = z + x = 2x, \quad c = x + y = 2x,$$
i.e. $a = b = c$.

**Equality holds if and only if the triangle is equilateral.** $\blacksquare$

## Summary

| Step | Tool / Fact |
|------|-------------|
| Triangle $\Rightarrow$ $a=y+z,\ b=z+x,\ c=x+y$ with $x,y,z>0$ | Ravi substitution |
| $S = 2\bigl[x^3z + xy^3 + yz^3 - xyz(x+y+z)\bigr]$ | Direct expansion |
| Reduce to $\frac{x^2}{y}+\frac{y^2}{z}+\frac{z^2}{x} \geq x+y+z$ | Divide by $xyz>0$ |
| Final inequality | Cauchy–Schwarz (Engel form) |
| Equality $\Leftrightarrow$ $x=y=z$ $\Leftrightarrow$ $a=b=c$ | Equality condition of C-S |
