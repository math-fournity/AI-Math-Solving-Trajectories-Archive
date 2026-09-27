# IMO 1966 Problem 5 — Solution

## Problem

Solve the system (for $x_1, x_2, x_3, x_4$):

$$|a_1-a_2|\,x_2 + |a_1-a_3|\,x_3 + |a_1-a_4|\,x_4 = 1$$
$$|a_2-a_1|\,x_1 + |a_2-a_3|\,x_3 + |a_2-a_4|\,x_4 = 1$$
$$|a_3-a_1|\,x_1 + |a_3-a_2|\,x_2 + |a_3-a_4|\,x_4 = 1$$
$$|a_4-a_1|\,x_1 + |a_4-a_2|\,x_2 + |a_4-a_3|\,x_3 = 1$$

where $a_1, a_2, a_3, a_4$ are four distinct real numbers.

## Answer

Let $m = \min(a_1, a_2, a_3, a_4)$ and $M = \max(a_1, a_2, a_3, a_4)$. The unique solution is

$$\boxed{x_i = \begin{cases} \dfrac{1}{M - m} & \text{if } a_i = m \text{ or } a_i = M, \\[6pt] 0 & \text{otherwise.} \end{cases}}$$

Equivalently: only the two variables corresponding to the **extreme** values of the $a_i$ are nonzero (and equal), all others are zero.

## Proof

**Step 1 — Reduction to the ordered case.** The system is invariant under any simultaneous permutation of the indices $\{1,2,3,4\}$ (permuting both the $a_i$ and the $x_i$ together). Hence, without loss of generality, assume

$$a_1 < a_2 < a_3 < a_4.$$

Set $b_1 = a_2 - a_1 > 0$, $\;b_2 = a_3 - a_2 > 0$, $\;b_3 = a_4 - a_3 > 0$, so that

$$a_2 - a_1 = b_1,\quad a_3 - a_1 = b_1 + b_2,\quad a_4 - a_1 = b_1 + b_2 + b_3,$$
$$a_3 - a_2 = b_2,\quad a_4 - a_2 = b_2 + b_3,\quad a_4 - a_3 = b_3.$$

All absolute values resolve with a definite sign, and the system becomes

$$(\text{I})\quad b_1\, x_2 + (b_1{+}b_2)\, x_3 + (b_1{+}b_2{+}b_3)\, x_4 = 1$$
$$(\text{II})\quad b_1\, x_1 + b_2\, x_3 + (b_2{+}b_3)\, x_4 = 1$$
$$(\text{III})\quad (b_1{+}b_2)\, x_1 + b_2\, x_2 + b_3\, x_4 = 1$$
$$(\text{IV})\quad (b_1{+}b_2{+}b_3)\, x_1 + (b_2{+}b_3)\, x_2 + b_3\, x_3 = 1$$

**Step 2 — Subtract consecutive equations.** Since all four right-hand sides equal $1$, subtracting two equations eliminates the constant:

**(I) $-$ (II):**
$$b_1(x_2 - x_1) + (b_1{+}b_2)x_3 - b_2 x_3 + (b_1{+}b_2{+}b_3)x_4 - (b_2{+}b_3)x_4 = 0$$
$$\Longrightarrow\; b_1\,(x_2 - x_1 + x_3 + x_4) = 0.$$

Since $b_1 > 0$:

$$\text{(A)}\quad x_1 = x_2 + x_3 + x_4.$$

**(II) $-$ (III):**
$$b_1 x_1 - (b_1{+}b_2)x_1 + b_2 x_3 - b_2 x_2 + (b_2{+}b_3)x_4 - b_3 x_4 = 0$$
$$\Longrightarrow\; b_2\,(-x_1 - x_2 + x_3 + x_4) = 0.$$

Since $b_2 > 0$:

$$\text{(B)}\quad x_1 + x_2 = x_3 + x_4.$$

**(III) $-$ (IV):**
$$(b_1{+}b_2)x_1 - (b_1{+}b_2{+}b_3)x_1 + b_2 x_2 - (b_2{+}b_3)x_2 + b_3 x_4 - b_3 x_3 = 0$$
$$\Longrightarrow\; b_3\,(-x_1 - x_2 - x_3 + x_4) = 0.$$

Since $b_3 > 0$:

$$\text{(C)}\quad x_4 = x_1 + x_2 + x_3.$$

**Step 3 — Solve the linear system (A), (B), (C).**

From **(A)** and **(C)**: $x_1 = x_2 + x_3 + x_4$ and $x_4 = x_1 + x_2 + x_3$. Subtracting,

$$x_1 - x_4 = (x_2 + x_3) - (x_2 + x_3) \cdot(-1)\;\;[\text{rearranging}]$$

More directly: (A) gives $x_1 - x_4 = x_2 + x_3$; (C) gives $x_4 - x_1 = x_2 + x_3$. Adding these two:

$$0 = 2(x_2 + x_3) \;\Longrightarrow\; x_3 = -x_2.$$

Substituting $x_3 = -x_2$ into (A): $x_1 = x_2 - x_2 + x_4 = x_4$, so

$$x_1 = x_4.$$

Substituting $x_1 = x_4$ and $x_3 = -x_2$ into (B): $x_1 + x_2 = -x_2 + x_1$, giving $2x_2 = 0$, hence

$$x_2 = 0, \qquad x_3 = 0, \qquad x_1 = x_4.$$

The three relations (A), (B), (C) are linearly independent (they have rank $3$), so the solution space of the homogeneous part is one-dimensional: $\{(t,\, 0,\, 0,\, t) : t \in \mathbb{R}\}$.

**Step 4 — Determine $t$ from one original equation.** Substitute $x_1 = x_4 = t$, $x_2 = x_3 = 0$ into equation (I):

$$(b_1 + b_2 + b_3)\, t = 1 \;\Longrightarrow\; t = \frac{1}{b_1 + b_2 + b_3} = \frac{1}{a_4 - a_1}.$$

One verifies the remaining equations (II), (III), (IV) are automatically satisfied:

- (II): $b_1 t + (b_2 + b_3) t = (b_1 + b_2 + b_3) t = 1$. ✓
- (III): $(b_1 + b_2) t + b_3 t = (b_1 + b_2 + b_3) t = 1$. ✓
- (IV): $(b_1 + b_2 + b_3) t = 1$. ✓

**Step 5 — Uniqueness.** The three independent difference equations (A), (B), (C) reduce the 4-dimensional space to a 1-dimensional line; the single scalar equation (I) then pins down the unique value $t = 1/(a_4 - a_1)$, which is well-defined since $a_4 \neq a_1$ (the $a_i$ are distinct). Hence the solution is **unique**.

**Step 6 — General form (undo the ordering).** In the ordered case $a_1 < a_2 < a_3 < a_4$ we obtained

$$x_1 = x_4 = \frac{1}{a_4 - a_1}, \qquad x_2 = x_3 = 0.$$

Here $a_1 = m$ (the minimum) and $a_4 = M$ (the maximum), so $a_4 - a_1 = M - m$. The variables that are nonzero are exactly those whose $a_i$ is an extreme value. Since the system is permutation-invariant, the same holds for any ordering of the $a_i$:

$$x_i = \begin{cases} \dfrac{1}{M - m} & \text{if } a_i = m \text{ or } a_i = M, \\[6pt] 0 & \text{otherwise,} \end{cases}$$

where $m = \min(a_1,a_2,a_3,a_4)$ and $M = \max(a_1,a_2,a_3,a_4)$.

$\blacksquare$ (QED)

## Verification (numerical)

Tested with multiple orderings, e.g. $a = (3, 1, 4, 2)$: $m = 1 = a_2$, $M = 4 = a_3$, predicted $x_2 = x_3 = 1/3$, $x_1 = x_4 = 0$.

- Eq 1: $|3{-}1|{\cdot}\tfrac13 + |3{-}4|{\cdot}\tfrac13 + |3{-}2|{\cdot}0 = \tfrac23 + \tfrac13 = 1$ ✓
- Eq 2: $|1{-}3|{\cdot}0 + |1{-}4|{\cdot}\tfrac13 + |1{-}2|{\cdot}0 = 1$ ✓
- Eq 3: $|4{-}3|{\cdot}0 + |4{-}1|{\cdot}\tfrac13 + |4{-}2|{\cdot}0 = 1$ ✓
- Eq 4: $|2{-}3|{\cdot}0 + |2{-}1|{\cdot}\tfrac13 + |2{-}4|{\cdot}\tfrac13 = \tfrac13 + \tfrac23 = 1$ ✓
