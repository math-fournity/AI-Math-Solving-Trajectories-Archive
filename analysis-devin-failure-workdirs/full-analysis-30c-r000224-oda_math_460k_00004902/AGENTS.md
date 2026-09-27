# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Jake can wash his car with 1 bottle of car wash soap 4 times.  If each bottle costs $4.00, and he washes his car once a week for 20 weeks, how much does he spend on car soap?       — 题目文本
#   <think>Okay, let's see. The problem is about Jake washing his car and figuring out how much he spends on soap over 20 weeks. Let's break it down step by step.

First, the problem says that 1 bottle of car wash soap can be used 4 times. So each bottle lasts for 4 washes. Then, each bottle costs $4.00. Jake washes his car once a week for 20 weeks. We need to find out the total cost.

First, let's figure out how many times he needs to wash his car. Since he washes once a week for 20 weeks, that's 20 washes total. 

Next, we need to find out how many bottles of soap he needs. Each bottle does 4 washes. So, if he has 20 washes, we divide the total number of washes by the number of washes per bottle. That's 20 divided by 4. Let me calculate that: 20 ÷ 4 = 5. So he needs 5 bottles.

Now, each bottle is $4.00. So 5 bottles times $4.00 per bottle. That's 5 × 4 = 20. So the total cost is $20.00.

Wait, let me double-check. 4 washes per bottle, 20 washes total. 20 divided by 4 is 5 bottles. 5 times $4 is $20. Yep, that makes sense. I think that's right.
</think>

Jake washes his car once a week for 20 weeks, so he needs 20 washes. Each bottle of soap can be used 4 times, so the number of bottles needed is \( \frac{20}{4} = 5 \) bottles. Each bottle costs $4.00, so the total cost is \( 5 \times 4 = 20 \) dollars.

\(\boxed{20}\)  — 标准解答
#   Let me analyze this geometry problem carefully.

We have an acute triangle $ABC$. $T$ is the reflection of $A$ in the perpendicular bisector of $BC$. $A'$ is the $A$-antipode on the circumcircle $(ABC)$ (the point diametrically opposite to $A$). $P$ is the second intersection of $AA'$ with the parabola through $ABCT$. $D$ is the point on $(ABC)$ such that $AD \perp BC$. $Q = PD \cap BC$. $R$ is the intersection of $AD$ with the tangent to $(ADC)$ at $A'$. $M$ is the midpoint of $BC$. Calculate $QR/AM$.

Wait, let me re-read. $R$ is the intersection of $AD$ with the tangent to $(ADC)$ at $A'$. But $A'$ is the antipode of $A$ on $(ABC)$. Is $A'$ on $(ADC)$? $D$ is on $(ABC)$, so $(ADC) = (ABC)$ since $A$, $D$, $C$ are all on the circumcircle. So $(ADC)$ is the same as $(ABC)$. So $R$ is the intersection of $AD$ with the tangent to $(ABC)$ at $A'$.

Let me set up coordinates. Let me place the circumcircle as the unit circle, or use a convenient coordinate system.

Actually, let me think about this more carefully. Let me use coordinates with $BC$ horizontal.

Let me place $M$ at the origin, $BC$ along the x-axis. Let $B = (-a, 0)$, $C = (a, 0)$, so $M = (0, 0)$ and $BC = 2a$. Let $A = (d, h)$ with $h > 0$ (acute triangle).

The perpendicular bisector of $BC$ is the y-axis (since $M$ is the midpoint and $BC$ is along x-axis). The reflection of $A = (d, h)$ in the y-axis is $T = (-d, h)$.

Now, $A'$ is the antipode of $A$ on the circumcircle. Let me find the circumcircle first.

The circumcircle passes through $B = (-a, 0)$, $C = (a, 0)$, $A = (d, h)$. The center is on the y-axis (by symmetry of $B$ and $C$), say $O = (0, k)$. Then:
- $OB^2 = a^2 + k^2$
- $OA^2 = d^2 + (h - k)^2$

So $a^2 + k^2 = d^2 + h^2 - 2hk + k^2$, giving $a^2 = d^2 + h^2 - 2hk$, so $k = \frac{d^2 + h^2 - a^2}{2h}$.

The circumradius $R_c = \sqrt{a^2 + k^2}$.

$A'$ is the antipode of $A$, so $A' = 2O - A = (-d, 2k - h)$.

Now, $D$ is the point on $(ABC)$ such that $AD \perp BC$. Since $BC$ is along the x-axis, $AD$ is vertical, so $D$ has the same x-coordinate as $A$, which is $d$. $D$ is on the circumcircle: $d^2 + (y_D - k)^2 = a^2 + k^2$, so $(y_D - k)^2 = a^2 + k^2 - d^2$. We have $A = (d, h)$ is one solution, so $y_D - k = -(h - k)$, giving $y_D = 2k - h$. So $D = (d, 2k - h)$.

Interesting, so $D = (d, 2k - h)$ and $A' = (-d, 2k - h)$. So $D$ and $A'$ have the same y-coordinate! They are reflections of each other in the y-axis. That makes sense because $D$ is the reflection of $A'$ in the perpendicular bisector of $BC$... wait, no. $A' = (-d, 2k-h)$ and $D = (d, 2k-h)$. Yes, $D$ is the reflection of $A'$ in the y-axis (perpendicular bisector of $BC$). And $T = (-d, h)$ is the reflection of $A$ in the y-axis.

Now, the line $AA'$: $A = (d, h)$, $A' = (-d, 2k - h)$. Direction: $(-2d, 2k - 2h) = (-2d, 2(k-h))$, or simplified $(-d, k-h)$.

Parametrize: $(x, y) = (d, h) + t(-d, k-h) = (d(1-t), h + t(k-h))$.

At $t = 0$: $A$. At $t = 1$: $A'$. At $t = 2$: $(d(1-2), h + 2(k-h)) = (-d, 2k - h) = A'$. Wait, that's wrong. At $t = 1$: $(d - d, h + k - h) = (0, k) = O$, the center. At $t = 2$: $(-d, h + 2(k-h)) = (-d, 2k - h) = A'$. So $A'$ corresponds to $t = 2$.

Hmm, let me recheck. $A' = (-d, 2k - h)$. With $t = 2$: $x = d(1-2) = -d$ ✓, $y = h + 2(k-h) = 2k - h$ ✓. Good.

Now I need the parabola through $A$, $B$, $C$, $T$.

$A = (d, h)$, $B = (-a, 0)$, $C = (a, 0)$, $T = (-d, h)$.

A general parabola has equation $\alpha x^2 + \beta xy + \gamma y^2 + \delta x + \epsilon y + \zeta = 0$ with the conic being a parabola (discriminant $\beta^2 - 4\alpha\gamma = 0$).

By symmetry, since $A$ and $T$ are symmetric about the y-axis, and $B$ and $C$ are symmetric about the y-axis, the parabola should be symmetric about the y-axis. So the equation has no odd powers of $x$: $\alpha x^2 + \gamma y^2 + \epsilon y + \zeta = 0$ (with $\beta = 0$, $\delta = 0$).

For a parabola, $\beta^2 - 4\alpha\gamma = 0 \Rightarrow -4\alpha\gamma = 0$, so either $\alpha = 0$ or $\gamma = 0$.

If $\alpha = 0$: $\gamma y^2 + \epsilon y + \zeta = 0$, which is just a pair of horizontal lines (or a single line), not a parabola through 4 points in general position. So $\gamma = 0$.

Then $\alpha x^2 + \epsilon y + \zeta = 0$, i.e., $x^2 = -\frac{\epsilon}{\alpha} y - \frac{\zeta}{\alpha}$, a parabola with vertical axis.

Using $B = (-a, 0)$: $\alpha a^2 + \zeta = 0 \Rightarrow \zeta = -\alpha a^2$.
Using $A = (d, h)$: $\alpha d^2 + \epsilon h + \zeta = 0 \Rightarrow \alpha d^2 + \epsilon h - \alpha a^2 = 0 \Rightarrow \epsilon h = \alpha(a^2 - d^2) \Rightarrow \epsilon = \frac{\alpha(a^2 - d^2)}{h}$.

So the parabola is: $\alpha x^2 + \frac{\alpha(a^2 - d^2)}{h} y - \alpha a^2 = 0$, or $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0$.

So $x^2 = a^2 - \frac{a^2 - d^2}{h} y$.

Let me verify with $T = (-d, h)$: $d^2 = a^2 - \frac{a^2 - d^2}{h} \cdot h = a^2 - (a^2 - d^2) = d^2$ ✓.

Now, $P$ is the second intersection of $AA'$ with this parabola. The line $AA'$ is parametrized as $(d(1-t), h + t(k-h))$.

Substitute into $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0$:

$d^2(1-t)^2 + \frac{a^2 - d^2}{h}(h + t(k-h)) - a^2 = 0$

$d^2(1 - 2t + t^2) + (a^2 - d^2) + \frac{(a^2 - d^2)(k-h)}{h} t - a^2 = 0$

$d^2 - 2d^2 t + d^2 t^2 + a^2 - d^2 + \frac{(a^2 - d^2)(k-h)}{h} t - a^2 = 0$

$d^2 t^2 - 2d^2 t + \frac{(a^2 - d^2)(k-h)}{h} t = 0$

$t \left[ d^2 t - 2d^2 + \frac{(a^2 - d^2)(k-h)}{h} \right] = 0$

So $t = 0$ (which gives $A$) or $t = \frac{2d^2 - \frac{(a^2 - d^2)(k-h)}{h}}{d^2} = 2 - \frac{(a^2 - d^2)(k-h)}{d^2 h}$.

Recall $k = \frac{d^2 + h^2 - a^2}{2h}$, so $k - h = \frac{d^2 + h^2 - a^2 - 2h^2}{2h} = \frac{d^2 - h^2 - a^2}{2h}$.

So $\frac{(a^2 - d^2)(k-h)}{h} = \frac{(a^2 - d^2)(d^2 - h^2 - a^2)}{2h^2}$.

Let me denote $t_P = 2 - \frac{(a^2 - d^2)(d^2 - h^2 - a^2)}{2d^2 h^2}$.

Note that $d^2 - h^2 - a^2 = -(a^2 + h^2 - d^2)$ and $a^2 - d^2 = -(d^2 - a^2)$.

So $(a^2 - d^2)(d^2 - h^2 - a^2) = (-(d^2 - a^2))(-(a^2 + h^2 - d^2)) = (d^2 - a^2)(a^2 + h^2 - d^2)$.

Hmm, let me just compute numerically to get intuition. Let me pick a specific triangle.

Let me try $B = (-3, 0)$, $C = (3, 0)$, $A = (1, 4)$. So $a = 3$, $d = 1$, $h = 4$.

Check acute: $AB = \sqrt{16 + 16} = \sqrt{32}$, $AC = \sqrt{4 + 16} = \sqrt{20}$, $BC = 6$. Check $AB^2 + AC^2 = 52 > 36 = BC^2$ ✓, $AB^2 + BC^2 = 68 > 20$ ✓, $AC^2 + BC^2 = 56 > 32$ ✓. Acute.

$k = \frac{1 + 16 - 9}{8} = \frac{8}{8} = 1$. So $O = (0, 1)$, $R_c = \sqrt{9 + 1} = \sqrt{10}$.

$A' = (-1, 2 \cdot 1 - 4) = (-1, -2)$. Check: $(-1)^2 + (-2-1)^2 = 1 + 9 = 10$ ✓.
$D = (1, -2)$. Check: $1 + 9 = 10$ ✓.

Parabola: $x^2 + \frac{9 - 1}{4} y - 9 = 0 \Rightarrow x^2 + 2y - 9 = 0 \Rightarrow y = \frac{9 - x^2}{2}$.

Line $AA'$: from $(1, 4)$ to $(-1, -2)$. Direction $(-2, -6)$, or $(-1, -3)$. Parametrize: $(1 - t, 4 - 3t)$.

Substitute into parabola: $(1-t)^2 + 2(4 - 3t) - 9 = 0 \Rightarrow 1 - 2t + t^2 + 8 - 6t - 9 = 0 \Rightarrow t^2 - 8t = 0 \Rightarrow t(t - 8) = 0$.

So $t = 0$ (point $A$) or $t = 8$ (point $P$). $P = (1 - 8, 4 - 24) = (-7, -20)$.

Now $D = (1, -2)$. Line $PD$: from $(-7, -20)$ to $(1, -2)$. Direction $(8, 18)$, or $(4, 9)$. Parametrize: $(-7 + 4s, -20 + 9s)$.

$Q = PD \cap BC$. $BC$ is the x-axis ($y = 0$). So $-20 + 9s = 0 \Rightarrow s = 20/9$. $Q = (-7 + 80/9, 0) = (-63/9 + 80/9, 0) = (17/9, 0)$.

Now $R$: intersection of $AD$ with the tangent to $(ABC)$ at $A'$.

$AD$ is the vertical line $x = 1$ (since $A = (1, 4)$ and $D = (1, -2)$).

The circumcircle is $x^2 + (y-1)^2 = 10$. The tangent at $A' = (-1, -2)$: the radius to $A'$ is from $O = (0, 1)$ to $(-1, -2)$, direction $(-1, -3)$. The tangent is perpendicular to this, so direction $(3, -1)$. Tangent line: $(-1, -2) + u(3, -1)$, i.e., $x = -1 + 3u$, $y = -2 - u$.

Intersection with $x = 1$: $-1 + 3u = 1 \Rightarrow u = 2/3$. $y = -2 - 2/3 = -8/3$. So $R = (1, -8/3)$.

Now $Q = (17/9, 0)$, $R = (1, -8/3) = (9/9, -8/3)$.

$QR = \sqrt{(17/9 - 1)^2 + (0 + 8/3)^2} = \sqrt{(8/9)^2 + (8/3)^2} = \sqrt{64/81 + 64/9} = \sqrt{64/81 + 576/81} = \sqrt{640/81} = \frac{8\sqrt{10}}{9}$.

$AM = \sqrt{(1-0)^2 + (4-0)^2} = \sqrt{17}$.

$QR/AM = \frac{8\sqrt{10}}{9\sqrt{17}}$.

Hmm, that doesn't look like a clean ratio. Let me double-check.

Wait, maybe I should re-examine. The problem says "the tangent to $(ADC)$ at $A'$". Since $A$, $D$, $C$ are on the circumcircle, $(ADC) = (ABC)$. So the tangent is to the circumcircle at $A'$. That's what I computed.

Let me recheck $QR$. $Q = (17/9, 0)$, $R = (1, -8/3)$.

$QR^2 = (17/9 - 9/9)^2 + (0 - (-8/3))^2 = (8/9)^2 + (8/3)^2 = 64/81 + 64/9 = 64/81 + 576/81 = 640/81$.

$QR = \sqrt{640}/9 = 8\sqrt{10}/9$.

$AM = \sqrt{1 + 16} = \sqrt{17}$.

$QR/AM = \frac{8\sqrt{10}}{9\sqrt{17}} = \frac{8\sqrt{170}}{9 \cdot 17} = \frac{8\sqrt{170}}{153}$.

That's not clean. Let me try another triangle to see if the ratio is constant.

Let me try $B = (-2, 0)$, $C = (2, 0)$, $A = (0, 3)$. So $a = 2$, $d = 0$, $h = 3$.

But $d = 0$ means $A$ is on the y-axis, so $T = A$, and the parabola degenerates. Let me avoid that.

Let me try $B = (-4, 0)$, $C = (4, 0)$, $A = (2, 5)$. $a = 4$, $d = 2$, $h = 5$.

Check acute: $AB^2 = 4 + 25 = 29$, $AC^2 = 4 + 25 = 29$, $BC^2 = 16$. All angles acute? $AB^2 + AC^2 = 58 > 16$ ✓, $AB^2 + BC^2 = 45 > 29$ ✓. Yes acute (isosceles).

$k = \frac{4 + 25 - 16}{10} = \frac{13}{10}$. $O = (0, 13/10)$, $R_c = \sqrt{16 + 169/100} = \sqrt{1769/100} = \sqrt{1769}/10$.

$A' = (-2, 2 \cdot 13/10 - 5) = (-2, -12/10) = (-2, -6/5)$.
$D = (2, -6/5)$.

Parabola: $x^2 + \frac{16 - 4}{5} y - 16 = 0 \Rightarrow x^2 + \frac{12}{5} y - 16 = 0$.

Line $AA'$: from $(2, 5)$ to $(-2, -6/5)$. Direction $(-4, -6/5 - 5) = (-4, -31/5)$. Parametrize: $(2 - 4t, 5 - \frac{31}{5}t)$.

Substitute: $(2-4t)^2 + \frac{12}{5}(5 - \frac{31}{5}t) - 16 = 0$

$4 - 16t + 16t^2 + 12 - \frac{372}{25}t - 16 = 0$

$16t^2 - 16t - \frac{372}{25}t + 0 = 0$

$16t^2 - (16 + \frac{372}{25})t = 0$

$16t^2 - \frac{400 + 372}{25}t = 0$

$16t^2 - \frac{772}{25}t = 0$

$t(16t - \frac{772}{25}) = 0$

$t = 0$ or $t = \frac{772}{400} = \frac{193}{100}$.

$P = (2 - 4 \cdot \frac{193}{100}, 5 - \frac{31}{5} \cdot \frac{193}{100}) = (2 - \frac{772}{100}, 5 - \frac{5983}{500}) = (\frac{200 - 772}{100}, \frac{2500 - 5983}{500}) = (-\frac{572}{100}, -\frac{3483}{500}) = (-\frac{143}{25}, -\frac{3483}{500})$.

Let me simplify: $P_x = -143/25$, $P_y = -3483/500$.

$D = (2, -6/5) = (2, -600/500)$.

Line $PD$: from $P = (-143/25, -3483/500)$ to $D = (2, -6/5)$.

Direction: $(2 + 143/25, -6/5 + 3483/500) = (50/25 + 143/25, -600/500 + 3483/500) = (193/25, 2883/500)$.

$Q = PD \cap BC$ (y = 0). Parametrize: $P + s \cdot \text{direction}$.

$y_Q = -3483/500 + s \cdot 2883/500 = 0 \Rightarrow s = 3483/2883 = 1161/961 = 1161/961$.

Let me simplify: $\gcd(3483, 2883)$. $3483 = 1 \cdot 2883 + 600$. $2883 = 4 \cdot 600 + 483$. $600 = 1 \cdot 483 + 117$. $483 = 4 \cdot 117 + 15$. $117 = 7 \cdot 15 + 12$. $15 = 1 \cdot 12 + 3$. $12 = 4 \cdot 3$. So $\gcd = 3$. $s = 1161/961$.

$x_Q = -143/25 + \frac{1161}{961} \cdot \frac{193}{25} = \frac{1}{25}(-143 + \frac{1161 \cdot 193}{961})$.

$1161 \cdot 193 = 1161 \cdot 200 - 1161 \cdot 7 = 232200 - 8127 = 224073$.

$224073 / 961$: $961 \cdot 233 = 224113$. Hmm, that's not exact. $961 \cdot 233 = 961 \cdot 200 + 961 \cdot 33 = 192200 + 31713 = 223913$. $224073 - 223913 = 160$. So $224073/961 = 233 + 160/961$. Not clean.

This is getting messy. Let me try a different approach—maybe use the first example and see if the answer simplifies, or try to find the general formula.

Actually, let me reconsider. Maybe the ratio is not constant and depends on the triangle, but the problem says "calculate the ratio", implying it's a constant. Let me recheck my first computation.

First example: $a = 3$, $d = 1$, $h = 4$.
$QR/AM = \frac{8\sqrt{10}}{9\sqrt{17}}$.

$\frac{8\sqrt{10}}{9\sqrt{17}} = \frac{8}{9}\sqrt{\frac{10}{17}}$. Not a clean number.

Hmm, let me reconsider the problem. Maybe I'm misunderstanding something.

"Let $R$ be the intersection of $AD$ with the tangent to $(ADC)$ at $A'$."

Wait—maybe $(ADC)$ doesn't mean the circumcircle of triangle $ADC$. Maybe it means something else? In some notations, $(ADC)$ could refer to a specific circle. But conventionally, $(ADC)$ is the circumcircle of triangle $ADC$, which since $A$, $D$, $C$ are on the circumcircle of $ABC$, is the same as $(ABC)$.

Unless $D$ is not on the circumcircle? Let me re-read: "Let $D$ be the point on $(ABC)$ such that $AD \perp BC$." Yes, $D$ is on $(ABC)$.

So $(ADC) = (ABC)$, and the tangent at $A'$ is the tangent to the circumcircle at $A'$.

Let me recheck my computation for the first example.

$O = (0, 1)$, $A' = (-1, -2)$. The tangent at $A'$ to $x^2 + (y-1)^2 = 10$:

The gradient of $x^2 + (y-1)^2$ at $(-1, -2)$ is $(-2, -6)$. Tangent line: $-2(x+1) - 6(y+2) = 0 \Rightarrow -2x - 2 - 6y - 12 = 0 \Rightarrow 2x + 6y + 14 = 0 \Rightarrow x + 3y + 7 = 0$.

$AD$ is $x = 1$. So $1 + 3y + 7 = 0 \Rightarrow y = -8/3$. $R = (1, -8/3)$. ✓

$Q = (17/9, 0)$. $QR^2 = (17/9 - 1)^2 + (8/3)^2 = (8/9)^2 + (8/3)^2 = 64/81 + 64/9 = 64(1/81 + 1/9) = 64(1/81 + 9/81) = 64 \cdot 10/81 = 640/81$.

$QR = 8\sqrt{10}/9$. $AM = \sqrt{17}$. Ratio $= 8\sqrt{10}/(9\sqrt{17})$.

Let me try yet another triangle to check if this is constant.

$B = (-1, 0)$, $C = (1, 0)$, $A = (0.5, 2)$. $a = 1$, $d = 0.5$, $h = 2$.

Check acute: $AB^2 = 0.25 + 4 = 4.25$, $AC^2 = 0.25 + 4 = 4.25$, $BC^2 = 4$. $AB^2 + BC^2 = 8.25 > 4.25$ ✓. Acute.

$k = \frac{0.25 + 4 - 1}{4} = \frac{3.25}{4} = \frac{13}{16}$. $O = (0, 13/16)$.

$A' = (-0.5, 2 \cdot 13/16 - 2) = (-0.5, 13/8 - 2) = (-0.5, -3/8)$.
$D = (0.5, -3/8)$.

Parabola: $x^2 + \frac{1 - 0.25}{2} y - 1 = 0 \Rightarrow x^2 + \frac{3}{8} y - 1 = 0$.

Line $AA'$: from $(0.5, 2)$ to $(-0.5, -3/8)$. Direction $(-1, -19/8)$. Parametrize: $(0.5 - t, 2 - \frac{19}{8}t)$.

Substitute: $(0.5 - t)^2 + \frac{3}{8}(2 - \frac{19}{8}t) - 1 = 0$

$0.25 - t + t^2 + \frac{3}{4} - \frac{57}{64}t - 1 = 0$

$t^2 - t - \frac{57}{64}t + 0.25 + 0.75 - 1 = 0$

$t^2 - \frac{64 + 57}{64}t = 0$

$t^2 - \frac{121}{64}t = 0$

$t(t - \frac{121}{64}) = 0$

$t = 0$ or $t = 121/64$.

$P = (0.5 - 121/64, 2 - \frac{19}{8} \cdot \frac{121}{64}) = (32/64 - 121/64, 2 - \frac{2299}{512}) = (-89/64, 1024/512 - 2299/512) = (-89/64, -1275/512)$.

$D = (0.5, -3/8) = (32/64, -192/512)$.

Line $PD$: direction $(32/64 + 89/64, -192/512 + 1275/512) = (121/64, 1083/512)$.

$Q$: $y = 0$. $-1275/512 + s \cdot 1083/512 = 0 \Rightarrow s = 1275/1083 = 425/361$.

$x_Q = -89/64 + \frac{425}{361} \cdot \frac{121}{64} = \frac{1}{64}(-89 + \frac{425 \cdot 121}{361})$.

$425 \cdot 121 = 51425$. $51425/361 = 51425/361$. $361 \cdot 142 = 51262$. $51425 - 51262 = 163$. So $51425/361 = 142 + 163/361$. Not clean.

Hmm, $361 = 19^2$. $163$ is prime. So $x_Q = \frac{1}{64} \cdot \frac{-89 \cdot 361 + 51425}{361} = \frac{-32129 + 51425}{64 \cdot 361} = \frac{19296}{23104}$.

$19296 / 23104$: $\gcd$? $19296 = 2^5 \cdot 3 \cdot 201 = ...$. Let me just compute: $19296 / 64 = 301.5$. Hmm. $23104 / 64 = 361$. So $x_Q = 19296/23104$. $19296 = 64 \cdot 301.5$? No. $64 \cdot 301 = 19264$. $19296 - 19264 = 32$. So $19296 = 64 \cdot 301 + 32$. Not divisible by 64.

Let me just compute numerically. $x_Q = 19296/23104 \approx 0.8352$.

$R$: tangent to circumcircle at $A'$. Circumcircle: $x^2 + (y - 13/16)^2 = 1 + (13/16)^2 = 1 + 169/256 = 425/256$.

At $A' = (-1/2, -3/8)$: gradient $(-1, 2(-3/8 - 13/16)) = (-1, 2(-6/16 - 13/16)) = (-1, 2(-19/16)) = (-1, -19/8)$.

Tangent: $-1(x + 1/2) - \frac{19}{8}(y + 3/8) = 0 \Rightarrow -(x + 1/2) - \frac{19}{8}(y + 3/8) = 0$.

$AD$ is $x = 1/2$. So $-(1/2 + 1/2) - \frac{19}{8}(y + 3/8) = 0 \Rightarrow -1 - \frac{19}{8}(y + 3/8) = 0 \Rightarrow \frac{19}{8}(y + 3/8) = -1 \Rightarrow y + 3/8 = -8/19 \Rightarrow y = -8/19 - 3/8 = (-64 - 57)/152 = -121/152$.

$R = (1/2, -121/152)$.

$Q = (19296/23104, 0)$. Let me simplify $19296/23104$. $\gcd(19296, 23104)$: $23104 - 19296 = 3808$. $19296 / 3808 = 5.07$. $19296 = 5 \cdot 3808 + 256$. $3808 / 256 = 14.875$. $3808 = 14 \cdot 256 + 224$. $256 / 224 = 1$ r $32$. $224 / 32 = 7$. So $\gcd = 32$. $19296/32 = 603$. $23104/32 = 722$. So $x_Q = 603/722$. $722 = 2 \cdot 361 = 2 \cdot 19^2$. $603 = 3 \cdot 201 = 3 \cdot 3 \cdot 67 = 9 \cdot 67$. $\gcd(603, 722) = 1$. So $x_Q = 603/722$.

$R = (1/2, -121/152)$. $152 = 8 \cdot 19$. $121 = 11^2$.

$QR^2 = (603/722 - 1/2)^2 + (121/152)^2 = (603/722 - 361/722)^2 + (121/152)^2 = (242/722)^2 + (121/152)^2$.

$242/722 = 121/361$. So $QR^2 = (121/361)^2 + (121/152)^2 = 121^2 (1/361^2 + 1/152^2)$.

$361 = 19^2$, $152 = 8 \cdot 19$. $361^2 = 19^4$, $152^2 = 64 \cdot 19^2$.

$1/361^2 + 1/152^2 = 1/19^4 + 1/(64 \cdot 19^2) = (64 + 19^2)/(64 \cdot 19^4) = (64 + 361)/(64 \cdot 19^4) = 425/(64 \cdot 19^4)$.

$QR^2 = 121^2 \cdot 425 / (64 \cdot 19^4) = 14641 \cdot 425 / (64 \cdot 130321)$.

$14641 = 121^2 = 11^4$. $130321 = 19^4$.

$QR = 121 \sqrt{425} / (8 \cdot 19^2) = 121 \sqrt{425} / (8 \cdot 361) = 121 \sqrt{425} / 2888$.

$\sqrt{425} = 5\sqrt{17}$. $QR = 121 \cdot 5\sqrt{17} / 2888 = 605\sqrt{17}/2888$.

$2888 = 8 \cdot 361 = 8 \cdot 19^2$. $605 = 5 \cdot 121 = 5 \cdot 11^2$.

$AM = \sqrt{0.25 + 4} = \sqrt{4.25} = \sqrt{17/4} = \sqrt{17}/2$.

$QR/AM = \frac{605\sqrt{17}/2888}{\sqrt{17}/2} = \frac{605 \cdot 2}{2888} = \frac{1210}{2888}$.

$1210/2888$: $\gcd$? $2888 = 2 \cdot 1210 + 468$. $1210 = 2 \cdot 468 + 274$. $468 = 1 \cdot 274 + 194$. $274 = 1 \cdot 194 + 80$. $194 = 2 \cdot 80 + 34$. $80 = 2 \cdot 34 + 12$. $34 = 2 \cdot 12 + 10$. $12 = 1 \cdot 10 + 2$. $10 = 5 \cdot 2$. $\gcd = 2$.

$1210/2 = 605$. $2888/2 = 1444$. $605/1444$. $1444 = 4 \cdot 361 = 4 \cdot 19^2 = (2 \cdot 19)^2 = 38^2$. $605 = 5 \cdot 121 = 5 \cdot 11^2$.

$QR/AM = 605/1444 = 5 \cdot 11^2 / (2 \cdot 19)^2 = 5 \cdot 121 / 1444$.

For the first example: $QR/AM = 8\sqrt{10}/(9\sqrt{17})$. Let me compute this numerically: $8\sqrt{10} \approx 8 \cdot 3.162 = 25.30$. $9\sqrt{17} \approx 9 \cdot 4.123 = 37.11$. Ratio $\approx 0.682$.

For the second example: $605/1444 \approx 0.419$.

These are different! So the ratio is NOT constant. That means either I'm making an error, or the problem has a specific answer that I'm not getting because of a misunderstanding.

Let me re-read the problem very carefully.

"Let $ABC$ be an acute triangle and let $T$ be the reflection of $A$ in the perpendicular bisector of $BC$."

OK so $T$ is the reflection of $A$ across the perpendicular bisector of $BC$. ✓

"Let $A'$ be the $A$-antipode on the circumcircle $(ABC)$"

$A'$ is the point diametrically opposite $A$ on the circumcircle. ✓

"and let $P$ be the second intersection of $AA'$ with the parabola through $ABCT$."

The parabola passing through $A$, $B$, $C$, $T$. $P$ is the second intersection of line $AA'$ with this parabola (the first being $A$). ✓

"Let $D$ be the point on $(ABC)$ such that $AD \perp BC$"

$D$ is on the circumcircle with $AD \perp BC$. ✓

"and let $Q = PD \cap BC$."

$Q$ is the intersection of line $PD$ with line $BC$. ✓

"Let $R$ be the intersection of $AD$ with the tangent to $(ADC)$ at $A'$."

$R$ is the intersection of line $AD$ with the tangent to circle $(ADC)$ at $A'$. Since $(ADC) = (ABC)$, this is the tangent to the circumcircle at $A'$. ✓

"If $M$ is the midpoint of $BC$, calculate the ratio $\frac{QR}{AM}$."

Hmm, but my two examples give different ratios. Let me double-check the second example more carefully.

Actually, wait. Let me recheck the second example. $a = 1$, $d = 0.5$, $h = 2$.

$k = \frac{d^2 + h^2 - a^2}{2h} = \frac{0.25 + 4 - 1}{4} = \frac{3.25}{4} = 0.8125 = 13/16$. ✓

$A' = (-d, 2k - h) = (-0.5, 13/8 - 2) = (-0.5, -3/8)$. ✓

$D = (d, 2k - h) = (0.5, -3/8)$. ✓

Parabola: $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0 \Rightarrow x^2 + \frac{1 - 0.25}{2} y - 1 = 0 \Rightarrow x^2 + \frac{3}{8} y - 1 = 0$. ✓

Line $AA'$: $A = (0.5, 2)$, $A' = (-0.5, -3/8)$. Direction: $(-1, -3/8 - 2) = (-1, -19/8)$. Parametrize: $(0.5 - t, 2 - 19t/8)$. ✓

Substitute into parabola:
$(0.5 - t)^2 + \frac{3}{8}(2 - 19t/8) - 1 = 0$
$0.25 - t + t^2 + 3/4 - 57t/64 - 1 = 0$
$t^2 - t - 57t/64 + 0 = 0$
$t^2 - (64 + 57)t/64 = 0$
$t^2 - 121t/64 = 0$
$t(t - 121/64) = 0$ ✓

$P = (0.5 - 121/64, 2 - 19/8 \cdot 121/64) = (32/64 - 121/64, 2 - 2299/512)$
$= (-89/64, 1024/512 - 2299/512) = (-89/64, -1275/512)$ ✓

$D = (1/2, -3/8) = (32/64, -192/512)$.

Direction $PD$: $(32/64 - (-89/64), -192/512 - (-1275/512)) = (121/64, 1083/512)$.

$Q$: $y = 0$. $-1275/512 + s \cdot 1083/512 = 0 \Rightarrow s = 1275/1083$.

$\gcd(1275, 1083)$: $1275 = 1 \cdot 1083 + 192$. $1083 = 5 \cdot 192 + 123$. $192 = 1 \cdot 123 + 69$. $123 = 1 \cdot 69 + 54$. $69 = 1 \cdot 54 + 15$. $54 = 3 \cdot 15 + 9$. $15 = 1 \cdot 9 + 6$. $9 = 1 \cdot 6 + 3$. $6 = 2 \cdot 3$. $\gcd = 3$.

$s = 425/361$. ✓

$x_Q = -89/64 + (425/361)(121/64) = (-89 \cdot 361 + 425 \cdot 121)/(64 \cdot 361)$.

$-89 \cdot 361 = -32129$. $425 \cdot 121 = 51425$. $-32129 + 51425 = 19296$.

$x_Q = 19296/(64 \cdot 361) = 19296/23104 = 603/722$. ✓

$R$: tangent at $A' = (-1/2, -3/8)$ to circumcircle $x^2 + (y - 13/16)^2 = 425/256$.

At $A'$: $\nabla = (2x, 2(y - 13/16)) = (-1, 2(-3/8 - 13/16)) = (-1, 2(-6/16 - 13/16)) = (-1, -38/16) = (-1, -19/8)$.

Tangent: $-1(x + 1/2) + (-19/8)(y + 3/8) = 0$, i.e., $(x + 1/2) + (19/8)(y + 3/8) = 0$.

$AD$: $x = 1/2$. $(1/2 + 1/2) + (19/8)(y + 3/8) = 0 \Rightarrow 1 + (19/8)(y + 3/8) = 0 \Rightarrow y + 3/8 = -8/19 \Rightarrow y = -8/19 - 3/8 = (-64 - 57)/152 = -121/152$. ✓

$R = (1/2, -121/152)$.

$QR^2 = (603/722 - 1/2)^2 + (0 - (-121/152))^2 = (603/722 - 361/722)^2 + (121/152)^2 = (242/722)^2 + (121/152)^2$.

$242/722 = 121/361$. $121/152 = 121/152$.

$QR^2 = 121^2/361^2 + 121^2/152^2 = 121^2(1/361^2 + 1/152^2)$.

$361 = 19^2$, $152 = 8 \cdot 19$. $361^2 = 19^4 = 130321$. $152^2 = 64 \cdot 361 = 23104$.

$1/130321 + 1/23104 = (23104 + 130321)/(130321 \cdot 23104) = 153425/(130321 \cdot 23104)$.

Hmm, $153425 = 5^2 \cdot 61 \cdot 101$? Let me check: $153425 / 25 = 6137$. $6137 / 7 = 876.7$. $6137 / 11 = 557.9$. $6137 / 13 = 472.1$. $6137 / 17 = 361$. So $6137 = 17 \cdot 361 = 17 \cdot 19^2$. So $153425 = 25 \cdot 17 \cdot 19^2 = 5^2 \cdot 17 \cdot 19^2$.

$130321 \cdot 23104 = 19^4 \cdot 64 \cdot 19^2 = 64 \cdot 19^6$.

$QR^2 = 121^2 \cdot 5^2 \cdot 17 \cdot 19^2 / (64 \cdot 19^6) = 121^2 \cdot 25 \cdot 17 / (64 \cdot 19^4)$.

$QR = 121 \cdot 5 \sqrt{17} / (8 \cdot 19^2) = 605\sqrt{17}/(8 \cdot 361) = 605\sqrt{17}/2888$. ✓

$AM = \sqrt{(1/2)^2 + 2^2} = \sqrt{1/4 + 4} = \sqrt{17/4} = \sqrt{17}/2$.

$QR/AM = (605\sqrt{17}/2888) / (\sqrt{17}/2) = 605 \cdot 2 / 2888 = 1210/2888 = 605/1444$.

$605/1444 = 5 \cdot 121 / (4 \cdot 361) = 5 \cdot 11^2 / (4 \cdot 19^2) = 5(11/38)^2$.

For the first example: $QR/AM = 8\sqrt{10}/(9\sqrt{17})$.

Let me compute $8\sqrt{10}/(9\sqrt{17})$ more carefully. $= \frac{8}{9}\sqrt{\frac{10}{17}}$. Numerically: $\sqrt{10/17} = \sqrt{0.588} = 0.767$. $8/9 \cdot 0.767 = 0.682$.

Second example: $605/1444 = 0.419$.

These are definitely different. So either the ratio is not constant (and the problem is asking for something else), or I have a misunderstanding.

Wait, let me reconsider. Maybe the problem is asking for a ratio that is always 2, or some constant, and I'm making a computational error. Let me very carefully redo the first example.

First example: $B = (-3, 0)$, $C = (3, 0)$, $A = (1, 4)$.

$a = 3$, $d = 1$, $h = 4$.

$k = (1 + 16 - 9)/8 = 8/8 = 1$. $O = (0, 1)$. $R_c = \sqrt{10}$.

$A' = (-1, 2 - 4) = (-1, -2)$. $D = (1, -2)$.

Parabola: $x^2 + (9-1)/4 \cdot y - 9 = 0 \Rightarrow x^2 + 2y - 9 = 0$.

Line $AA'$: $(1, 4) + t(-2, -6) = (1-2t, 4-6t)$. Or equivalently $(1-t', 4-3t')$ with $t' = 2t$... let me use the parametrization $(1-2t, 4-6t)$ where $t=0$ gives $A$ and $t=1$ gives $A'$.

Substitute: $(1-2t)^2 + 2(4-6t) - 9 = 0$
$1 - 4t + 4t^2 + 8 - 12t - 9 = 0$
$4t^2 - 16t = 0$
$4t(t - 4) = 0$
$t = 0$ or $t = 4$.

$P = (1 - 8, 4 - 24) = (-7, -20)$. ✓

$D = (1, -2)$. Line $PD$: from $(-7, -20)$ to $(1, -2)$. Direction $(8, 18)$. Parametrize: $(-7 + 8s, -20 + 18s)$.

$Q$: $y = 0 \Rightarrow -20 + 18s = 0 \Rightarrow s = 20/18 = 10/9$.
$x_Q = -7 + 80/9 = -63/9 + 80/9 = 17/9$. ✓

$R$: tangent at $A' = (-1, -2)$ to $x^2 + (y-1)^2 = 10$.

Gradient at $A'$: $(2(-1), 2(-2-1)) = (-2, -6)$. Tangent: $-2(x+1) - 6(y+2) = 0 \Rightarrow x + 1 + 3(y+2) = 0 \Rightarrow x + 3y + 7 = 0$.

$AD$: $x = 1$. $1 + 3y + 7 = 0 \Rightarrow y = -8/3$. $R = (1, -8/3)$. ✓

$QR^2 = (17/9 - 1)^2 + (0 + 8/3)^2 = (8/9)^2 + (8/3)^2 = 64/81 + 64/9 = 64/81 + 576/81 = 640/81$.

$QR = 8\sqrt{10}/9$.

$AM = \sqrt{1 + 16} = \sqrt{17}$.

$QR/AM = 8\sqrt{10}/(9\sqrt{17})$.

Numerically: $8 \cdot 3.1623 / (9 \cdot 4.1231) = 25.298 / 37.108 = 0.6817$.

Second example: $605/1444 = 0.4190$.

These are different. So the ratio depends on the triangle. That's strange for a problem that says "calculate the ratio."

Hmm, let me reconsider the problem statement. Maybe I'm wrong about the parabola. Let me re-read: "the parabola through $ABCT$." Four points determine a conic, and there's a unique parabola through four points (in general position). But wait—do four points always determine a unique parabola? A general conic has 5 degrees of freedom. A parabola has 4 (the parabola constraint removes one). So 4 points determine a unique parabola (generically). ✓

But wait, I assumed the parabola is symmetric about the y-axis because $A, T$ and $B, C$ are symmetric pairs. Is that necessarily the case? The four points $A, B, C, T$ are symmetric about the y-axis as a set, but the unique parabola through them must also be symmetric. Actually, if we reflect the parabola through the y-axis, we get another parabola through the same four points (since the set is symmetric). By uniqueness, it must be the same parabola. So yes, the parabola is symmetric about the y-axis. ✓

So my computation should be correct. But the ratio isn't constant...

Let me reconsider. Maybe I'm misunderstanding "$A$-antipode." In some contexts, the $A$-antipode might not mean the diametrically opposite point, but rather the point where the $A$-altitude meets the circumcircle again, or the reflection of the orthocenter... Let me think.

Actually, "antipode" typically means the diametrically opposite point. The "$A$-antipode" is the point on the circumcircle diametrically opposite to $A$. That's what I used.

Hmm, but wait. Let me reconsider whether $(ADC)$ might not be the circumcircle. If $D$ is defined differently...

"Let $D$ be the point on $(ABC)$ such that $AD \perp BC$."

$D$ is on the circumcircle, $AD \perp BC$. Since $BC$ is the x-axis, $AD$ is vertical, so $D$ has the same x-coordinate as $A$. There are two intersections of the vertical line through $A$ with the circumcircle: $A$ itself and $D$. So $D$ is the other intersection. ✓

And $(ADC)$ is the circumcircle of $A$, $D$, $C$, which is the same as $(ABC)$. ✓

So the tangent at $A'$ is to the circumcircle. ✓

Let me try a third example to see if there's a pattern.

$B = (-5, 0)$, $C = (5, 0)$, $A = (3, 6)$. $a = 5$, $d = 3$, $h = 6$.

Check acute: $AB^2 = 4 + 36 = 40$, $AC^2 = 4 + 36 = 40$, $BC^2 = 100$. $AB^2 + AC^2 = 80 < 100$. Not acute! The angle at $A$ is obtuse.

Let me try $A = (3, 8)$. $AB^2 = 4 + 64 = 68$, $AC^2 = 4 + 64 = 68$, $BC^2 = 100$. $68 + 68 = 136 > 100$ ✓. $68 + 100 > 68$ ✓. Acute (isosceles).

$a = 5$, $d = 3$, $h = 8$.

$k = (9 + 64 - 25)/16 = 48/16 = 3$. $O = (0, 3)$. $R_c = \sqrt{25 + 9} = \sqrt{34}$.

$A' = (-3, 6 - 8) = (-3, -2)$. $D = (3, -2)$.

Parabola: $x^2 + (25-9)/8 \cdot y - 25 = 0 \Rightarrow x^2 + 2y - 25 = 0$.

Line $AA'$: $(3, 8) + t(-6, -10) = (3-6t, 8-10t)$. $t=0$: $A$, $t=1$: $A'$.

Substitute: $(3-6t)^2 + 2(8-10t) - 25 = 0$
$9 - 36t + 36t^2 + 16 - 20t - 25 = 0$
$36t^2 - 56t = 0$
$4t(9t - 14) = 0$
$t = 0$ or $t = 14/9$.

$P = (3 - 6 \cdot 14/9, 8 - 10 \cdot 14/9) = (3 - 84/9, 8 - 140/9) = (27/9 - 84/9, 72/9 - 140/9) = (-57/9, -68/9) = (-19/3, -68/9)$.

$D = (3, -2)$. Line $PD$: from $(-19/3, -68/9)$ to $(3, -2) = (27/9, -18/9)$.

Direction: $(27/9 + 57/9, -18/9 + 68/9) = (84/9, 50/9) = (84, 50)/9$. Simplify: $(42, 25)/4.5$... let me use $(84, 50)$, i.e., $(42, 25)$.

$Q$: $y = 0$. $-68/9 + s \cdot 50/9 = 0 \Rightarrow s = 68/50 = 34/25$.

$x_Q = -19/3 + (34/25) \cdot (84/9) = -19/3 + 34 \cdot 84/(25 \cdot 9) = -19/3 + 2856/225 = -19/3 + 952/75$.

$-19/3 = -475/75$. $x_Q = -475/75 + 952/75 = 477/75 = 159/25$.

$R$: tangent at $A' = (-3, -2)$ to $x^2 + (y-3)^2 = 34$.

Gradient: $(2(-3), 2(-2-3)) = (-6, -10)$. Tangent: $-6(x+3) - 10(y+2) = 0 \Rightarrow 6(x+3) + 10(y+2) = 0 \Rightarrow 6x + 18 + 10y + 20 = 0 \Rightarrow 6x + 10y + 38 = 0 \Rightarrow 3x + 5y + 19 = 0$.

$AD$: $x = 3$. $9 + 5y + 19 = 0 \Rightarrow y = -28/5$. $R = (3, -28/5)$.

$QR^2 = (159/25 - 3)^2 + (28/5)^2 = (159/25 - 75/25)^2 + (28/5)^2 = (84/25)^2 + (28/5)^2$.

$= 7056/625 + 784/25 = 7056/625 + 19600/625 = 26656/625$.

$QR = \sqrt{26656}/25$. $26656 = 16 \cdot 1666 = 16 \cdot 2 \cdot 833 = 32 \cdot 833$. $833 = 7 \cdot 119 = 7 \cdot 7 \cdot 17 = 49 \cdot 17$. So $26656 = 32 \cdot 49 \cdot 17 = 16 \cdot 2 \cdot 49 \cdot 17$. $\sqrt{26656} = 4 \cdot 7 \sqrt{2 \cdot 17} = 28\sqrt{34}$.

$QR = 28\sqrt{34}/25$.

$AM = \sqrt{9 + 64} = \sqrt{73}$.

$QR/AM = 28\sqrt{34}/(25\sqrt{73})$.

Numerically: $28 \cdot 5.831 / (25 \cdot 8.544) = 163.27 / 213.6 = 0.7644$.

So the three ratios are:
- Example 1: $0.6817$
- Example 2: $0.4190$
- Example 3: $0.7644$

These are all different. The ratio is definitely not constant. So I must be misunderstanding the problem.

Let me re-read the problem once more...

"Let $R$ be the intersection of $AD$ with the tangent to $(ADC)$ at $A'$."

Hmm, what if $(ADC)$ is not the circumcircle of triangle $ADC$? What if it's a different circle? In some competition notations, $(XYZ)$ always means the circumcircle of triangle $XYZ$. But since $A$, $D$, $C$ are on the circumcircle of $ABC$, $(ADC) = (ABC)$.

Unless... $D$ is not on the circumcircle? Let me re-read: "Let $D$ be the point on $(ABC)$ such that $AD \perp BC$." No, $D$ is on $(ABC)$.

Wait, maybe the problem means something different by "$A$-antipode." Let me consider the possibility that $A'$ is the reflection of $A$ over $BC$, or the foot of the altitude, or the midpoint of arc $BC$...

Actually, in many geometry problems, the "$A$-antipode" refers to the point on the circumcircle diametrically opposite to $A$. That's the standard meaning. Let me stick with that.

Hmm, but what if the problem means the tangent to $(ADC)$ at $A'$ where $(ADC)$ is NOT the circumcircle but some other circle? That doesn't make sense with standard notation.

Wait, I just realized something. What if $A'$ is NOT on the circumcircle $(ADC) = (ABC)$? Let me check: $A'$ is the antipode of $A$ on $(ABC)$, so $A'$ is on $(ABC) = (ADC)$. So the tangent at $A'$ to $(ADC)$ is well-defined. ✓

Let me reconsider the problem. Maybe the issue is with the parabola. Let me re-examine.

Actually, wait. I just realized: maybe the problem is using "parabola" in a more general sense, or maybe there's a specific parabola associated with $ABCT$ that I'm not considering. But a parabola through 4 points is unique (generically), so that should be fine.

Let me reconsider: is the answer perhaps supposed to be 2, and I'm making a systematic error? Let me check if maybe $R$ is defined differently.

Actually, let me reconsider the problem. Maybe "the tangent to $(ADC)$ at $A'$" means the tangent to the circle $(ADC)$ at the point $A'$, but $A'$ might not be on $(ADC)$. If $A'$ is not on $(ADC)$, then the tangent from $A'$ to $(ADC)$ would be a different thing (tangent lines from an external point). But $A'$ IS on $(ABC) = (ADC)$, so this doesn't apply.

Hmm, let me try a completely different interpretation. What if $(ADC)$ is not the circumcircle of $ADC$ but rather some other circle? For instance, what if the problem means the circle with diameter $AD$ passing through $C$? No, that's non-standard.

Or what if the problem has a typo and it should be "the tangent to $(ABC)$ at $D$" or "at $A$"? Let me try "tangent to $(ABC)$ at $D$".

For example 1: $D = (1, -2)$. Tangent at $D$ to $x^2 + (y-1)^2 = 10$: gradient at $D$ is $(2, -6)$. Tangent: $2(x-1) - 6(y+2) = 0 \Rightarrow x - 1 - 3(y+2) = 0 \Rightarrow x - 3y - 7 = 0$.

$AD$: $x = 1$. $1 - 3y - 7 = 0 \Rightarrow y = -2$. So $R = (1, -2) = D$. That gives $QR = QD$, which is just the distance from $Q$ to $D$. $QD = \sqrt{(17/9 - 1)^2 + 4} = \sqrt{64/81 + 4} = \sqrt{64/81 + 324/81} = \sqrt{388/81} = 2\sqrt{97}/9$. $QR/AM = 2\sqrt{97}/(9\sqrt{17})$. Not clean either.

Let me try "tangent to $(ABC)$ at $A$."

Tangent at $A = (1, 4)$: gradient $(2, 6)$. Tangent: $2(x-1) + 6(y-4) = 0 \Rightarrow x - 1 + 3(y-4) = 0 \Rightarrow x + 3y - 13 = 0$.

$AD$: $x = 1$. $1 + 3y - 13 = 0 \Rightarrow y = 4$. So $R = (1, 4) = A$. $QR = QA$. Not useful.

OK so those alternatives don't work either. Let me go back to the original interpretation.

Actually, let me reconsider. Maybe I should look at this more carefully. Perhaps the answer IS supposed to be 2 and I'm making an error somewhere. Let me try to derive the general formula.

Let me use the general setup: $B = (-a, 0)$, $C = (a, 0)$, $A = (d, h)$, $M = (0, 0)$.

$k = \frac{d^2 + h^2 - a^2}{2h}$, $O = (0, k)$.

$A' = (-d, 2k - h)$, $D = (d, 2k - h)$.

Let me denote $e = 2k - h = \frac{d^2 + h^2 - a^2}{h} - h = \frac{d^2 - a^2}{h}$.

So $A' = (-d, e)$, $D = (d, e)$ where $e = \frac{d^2 - a^2}{h}$.

Note: $e = (d^2 - a^2)/h$. Since the triangle is acute and $|d| < a$ (for the foot of altitude to be on $BC$), we have $d^2 < a^2$, so $e < 0$. This makes sense—$D$ is below $BC$.

Parabola: $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0$. Note $\frac{a^2 - d^2}{h} = -e$. So the parabola is $x^2 - ey - a^2 = 0$, or $x^2 = a^2 + ey$.

Line $AA'$: from $(d, h)$ to $(-d, e)$. Direction $(-2d, e - h)$. Parametrize: $(d - 2dt, h + (e-h)t) = (d(1-2t), h + (e-h)t)$.

$t = 0$: $A$. $t = 1$: $(-d, e) = A'$. ✓

Substitute into parabola $x^2 - ey - a^2 = 0$:
$d^2(1-2t)^2 - e(h + (e-h)t) - a^2 = 0$
$d^2(1 - 4t + 4t^2) - eh - e(e-h)t - a^2 = 0$
$d^2 - 4d^2 t + 4d^2 t^2 - eh - e(e-h)t - a^2 = 0$

Now, $d^2 - eh - a^2 = d^2 - a^2 - eh$. And $e = (d^2 - a^2)/h$, so $eh = d^2 - a^2$. Thus $d^2 - eh - a^2 = d^2 - (d^2 - a^2) - a^2 = 0$. ✓ (This confirms $A$ is on the parabola.)

So: $4d^2 t^2 - 4d^2 t - e(e-h)t = 0$
$t(4d^2 t - 4d^2 - e(e-h)) = 0$
$t = 0$ or $t = \frac{4d^2 + e(e-h)}{4d^2}$.

$e(e-h) = e \cdot e - eh = e^2 - (d^2 - a^2) = \frac{(d^2 - a^2)^2}{h^2} - (d^2 - a^2) = (d^2 - a^2)\left(\frac{d^2 - a^2}{h^2} - 1\right) = (d^2 - a^2) \cdot \frac{d^2 - a^2 - h^2}{h^2}$.

So $t_P = \frac{4d^2 + (d^2 - a^2)(d^2 - a^2 - h^2)/h^2}{4d^2} = 1 + \frac{(d^2 - a^2)(d^2 - a^2 - h^2)}{4d^2 h^2}$.

Let me denote $\Delta = d^2 - a^2$ (which is negative for acute triangles with the foot on $BC$). Then $e = \Delta/h$.

$t_P = 1 + \frac{\Delta(\Delta - h^2)}{4d^2 h^2}$.

$P = (d(1 - 2t_P), h + (e - h)t_P)$.

$1 - 2t_P = 1 - 2 - \frac{2\Delta(\Delta - h^2)}{4d^2 h^2} = -1 - \frac{\Delta(\Delta - h^2)}{2d^2 h^2}$.

$P_x = d\left(-1 - \frac{\Delta(\Delta - h^2)}{2d^2 h^2}\right) = -d - \frac{\Delta(\Delta - h^2)}{2dh^2}$.

$e - h = \Delta/h - h = (\Delta - h^2)/h$.

$P_y = h + \frac{\Delta - h^2}{h} \cdot t_P = h + \frac{(\Delta - h^2)}{h}\left(1 + \frac{\Delta(\Delta - h^2)}{4d^2 h^2}\right)$

$= h + \frac{\Delta - h^2}{h} + \frac{\Delta(\Delta - h^2)^2}{4d^2 h^3}$

$= \frac{h^2 + \Delta - h^2}{h} + \frac{\Delta(\Delta - h^2)^2}{4d^2 h^3}$

$= \frac{\Delta}{h} + \frac{\Delta(\Delta - h^2)^2}{4d^2 h^3}$

$= \frac{\Delta}{h}\left(1 + \frac{(\Delta - h^2)^2}{4d^2 h^2}\right)$

$= e\left(1 + \frac{(\Delta - h^2)^2}{4d^2 h^2}\right)$

This is getting complicated. Let me try a different approach. Let me use the formula for $Q$ and $R$ in terms of the general parameters and see if $QR/AM$ simplifies.

Actually, let me try to compute symbolically using the substitution $u = d/a$, $v = h/a$ (normalize $a = 1$). Then the ratio should be a function of $u$ and $v$ if it's not constant.

From my examples:
- Example 1: $a=3, d=1, h=4 \Rightarrow u=1/3, v=4/3$. Ratio $= 8\sqrt{10}/(9\sqrt{17})$.
- Example 2: $a=1, d=0.5, h=2 \Rightarrow u=0.5, v=2$. Ratio $= 605/1444$.
- Example 3: $a=5, d=3, h=8 \Rightarrow u=0.6, v=1.6$. Ratio $= 28\sqrt{34}/(25\sqrt{73})$.

These are all different, confirming the ratio is not constant.

Hmm, but the problem says "calculate the ratio $\frac{QR}{AM}$". This strongly suggests the answer is a constant. Let me reconsider whether I'm misunderstanding the problem.

Oh wait—maybe I need to reconsider what "the tangent to $(ADC)$ at $A'$" means. What if $A'$ is NOT on the circle $(ADC)$? Let me think again...

$A'$ is the antipode of $A$ on $(ABC)$. $D$ is on $(ABC)$ with $AD \perp BC$. $C$ is on $(ABC)$. So $A$, $D$, $C$ are all on $(ABC)$, and $(ADC) = (ABC)$. $A'$ is also on $(ABC)$. So $A'$ is on $(ADC)$, and the tangent at $A'$ is well-defined.

Unless the problem means something different by "$A$-antipode." Let me consider: in some sources, the "$A$-antipode" might refer to the antipode of $A$ with respect to the nine-point circle, or the reflection of $H$ (orthocenter) over $BC$, or the point where the $A$-symmedian meets the circumcircle...

Actually, in many competition geometry contexts, the "$A$-antipode" is simply the point diametrically opposite $A$ on the circumcircle. I'll stick with this.

Let me try yet another interpretation: maybe "the tangent to $(ADC)$ at $A'$" means the tangent from $A'$ to the circle $(ADC)$, but since $A'$ is on the circle, this is just the tangent at $A'$. Same thing.

Hmm, let me try a completely different approach. What if the problem is correct and the answer is indeed a constant, but I'm making an error in the parabola? Let me reconsider.

Wait, actually, I want to double-check that four points determine a unique parabola. A conic is $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ with 5 degrees of freedom (up to scaling). A parabola requires $B^2 - 4AC = 0$, which is one constraint, leaving 4 degrees of freedom. Four points give 4 equations, so generically a unique parabola. ✓

But what if the four points $A, B, C, T$ are in a special position where there's no parabola or infinitely many? In my examples, I found a unique parabola, so that's fine.

Let me try to see if maybe the problem intends $P$ to be the second intersection of $AA'$ with the parabola, where "second" means the one other than $A'$ (not other than $A$). But $A'$ is generally not on the parabola. Let me check: is $A'$ on the parabola?

Parabola: $x^2 - ey - a^2 = 0$ where $e = (d^2 - a^2)/h$.

$A' = (-d, e)$. $d^2 - e \cdot e - a^2 = d^2 - e^2 - a^2 = d^2 - a^2 - (d^2 - a^2)^2/h^2 = (d^2 - a^2)(1 - (d^2 - a^2)/h^2) = (d^2 - a^2)(h^2 - d^2 + a^2)/h^2$.

This is zero only if $d^2 = a^2$ (degenerate) or $h^2 = d^2 - a^2$ (which would make $k = 0$, meaning $O$ is on $BC$). So in general, $A'$ is NOT on the parabola, and "second intersection" means the one other than $A$. ✓

OK, I'm stuck on why the ratio isn't constant. Let me try to approach this differently—maybe compute the general formula and see if it simplifies to a constant.

Let me use the general parametrization. $B = (-a, 0)$, $C = (a, 0)$, $A = (d, h)$, $M = (0, 0)$.

$e = (d^2 - a^2)/h$, $D = (d, e)$, $A' = (-d, e)$.

Parabola: $x^2 = a^2 + ey$, i.e., $x^2 - ey - a^2 = 0$.

Line $AA'$: $(d(1-2t), h + (e-h)t)$, $t = 0$ at $A$, $t = 1$ at $A'$.

$t_P = 1 + \frac{\Delta(\Delta - h^2)}{4d^2 h^2}$ where $\Delta = d^2 - a^2$.

Let me simplify. $\Delta - h^2 = d^2 - a^2 - h^2$. And $\Delta = d^2 - a^2$.

$t_P = 1 + \frac{(d^2 - a^2)(d^2 - a^2 - h^2)}{4d^2 h^2}$.

Let me denote $p = d^2 - a^2 - h^2$ and $\Delta = d^2 - a^2$. Then $t_P = 1 + \frac{\Delta \cdot p}{4d^2 h^2}$.

$P_x = d(1 - 2t_P) = d\left(-1 - \frac{\Delta p}{2d^2 h^2}\right) = -d - \frac{\Delta p}{2dh^2}$.

$P_y = h + (e-h)t_P = h + \frac{p}{h}\left(1 + \frac{\Delta p}{4d^2 h^2}\right) = h + \frac{p}{h} + \frac{\Delta p^2}{4d^2 h^3}$.

$= \frac{h^2 + p}{h} + \frac{\Delta p^2}{4d^2 h^3} = \frac{h^2 + d^2 - a^2 - h^2}{h} + \frac{\Delta p^2}{4d^2 h^3} = \frac{\Delta}{h} + \frac{\Delta p^2}{4d^2 h^3} = \frac{\Delta}{h}\left(1 + \frac{p^2}{4d^2 h^2}\right)$.

So $P = \left(-d - \frac{\Delta p}{2dh^2}, \frac{\Delta}{h}\left(1 + \frac{p^2}{4d^2 h^2}\right)\right)$.

$D = (d, e) = (d, \Delta/h)$.

Now, line $PD$. Direction from $P$ to $D$:

$\Delta x = d - P_x = d + d + \frac{\Delta p}{2dh^2} = 2d + \frac{\Delta p}{2dh^2} = \frac{4d^2 h^2 + \Delta p}{2dh^2}$.

$\Delta y = e - P_y = \frac{\Delta}{h} - \frac{\Delta}{h}\left(1 + \frac{p^2}{4d^2 h^2}\right) = -\frac{\Delta p^2}{4d^2 h^3}$.

So direction is $\left(\frac{4d^2 h^2 + \Delta p}{2dh^2}, -\frac{\Delta p^2}{4d^2 h^3}\right)$.

$Q$ is where $y = 0$ on line $PD$. Parametrize: $P + s \cdot \text{direction}$.

$y_Q = P_y + s \cdot \Delta y = 0 \Rightarrow s = -P_y / \Delta y = \frac{\Delta(1 + p^2/(4d^2 h^2))/h}{\Delta p^2/(4d^2 h^3)} = \frac{(1 + p^2/(4d^2 h^2)) \cdot 4d^2 h^3}{p^2 \cdot h} = \frac{4d^2 h^2(1 + p^2/(4d^2 h^2))}{p^2} = \frac{4d^2 h^2 + p^2}{p^2}$.

$x_Q = P_x + s \cdot \Delta x = -d - \frac{\Delta p}{2dh^2} + \frac{4d^2 h^2 + p^2}{p^2} \cdot \frac{4d^2 h^2 + \Delta p}{2dh^2}$.

This is getting very messy. Let me try a substitution to simplify. Let me set $a = 1$ (normalize) and use $d$ and $h$ as parameters.

Actually, let me try a slightly different approach. Let me use the specific coordinate system where the circumcircle is the unit circle, and use trigonometric parametrization.

Let the circumcircle be the unit circle. Let $A = e^{i\alpha}$, $B = e^{i\beta}$, $C = e^{i\gamma}$.

The antipode of $A$ is $A' = -e^{i\alpha} = e^{i(\alpha + \pi)}$.

$T$ is the reflection of $A$ in the perpendicular bisector of $BC$. The perpendicular bisector of $BC$ passes through the center $O$ and the midpoint of arc $BC$. In terms of angles, the perpendicular bisector of $BC$ is the line through $O$ in the direction of $e^{i(\beta+\gamma)/2}$ (the midpoint of the arc). Reflecting $A = e^{i\alpha}$ in this line gives $T = e^{i(\beta + \gamma - \alpha)}$.

$D$ is the point on the circumcircle with $AD \perp BC$. The direction of $BC$ is $e^{i\gamma} - e^{i\beta}$. $AD \perp BC$ means $D - A$ is perpendicular to $C - B$.

In complex numbers on the unit circle, the condition $AD \perp BC$ is $\frac{D - A}{\bar{D} - \bar{A}} = -\frac{C - B}{\bar{C} - \bar{B}}$. Since on the unit circle $\bar{z} = 1/z$, this becomes $\frac{D - A}{1/D - 1/A} = -\frac{C - B}{1/C - 1/B}$.

$\frac{D - A}{(A - D)/(AD)} = -\frac{C - B}{(B - C)/(BC)}$

$\frac{AD(D - A)}{A - D} = -\frac{BC(C - B)}{B - C}$

$-AD = BC$ (since $(D-A)/(A-D) = -1$ and $(C-B)/(B-C) = -1$)

$-AD = BC \Rightarrow AD = -BC$.

So $D = -BC/A$. On the unit circle, $D = -e^{i(\beta + \gamma - \alpha)} = -T$... wait, $T = e^{i(\beta + \gamma - \alpha)}$, so $D = -T = e^{i(\beta + \gamma - \alpha + \pi)}$.

Hmm interesting. So $D = -T$ (as complex numbers on the unit circle).

And $A' = -A$.

Now, the parabola through $A$, $B$, $C$, $T$. This is more complex to handle in this coordinate system.

Let me go back to the coordinate approach but try to be more systematic.

Let me use the coordinate system with $M$ at the origin, $BC$ along x-axis, and normalize $a = 1$ (so $B = (-1, 0)$, $C = (1, 0)$). Then $A = (d, h)$ with $|d| < 1$ and $h > 0$.

$e = d^2 - 1$ (divided by $h$... wait, $e = (d^2 - a^2)/h = (d^2 - 1)/h$).

Let me use $\delta = d^2 - 1$ (negative). Then $e = \delta/h$.

$D = (d, \delta/h)$, $A' = (-d, \delta/h)$.

Parabola: $x^2 - \frac{\delta}{h} y - 1 = 0$, i.e., $h x^2 - \delta y - h = 0$.

Line $AA'$: from $(d, h)$ to $(-d, \delta/h)$. Direction $(-2d, \delta/h - h) = (-2d, (\delta - h^2)/h)$.

Let $\phi = \delta - h^2 = d^2 - 1 - h^2$.

Parametrize: $(d(1-2t), h + \phi t/h)$.

Substitute into parabola: $h \cdot d^2(1-2t)^2 - \delta(h + \phi t/h) - h = 0$

$hd^2(1 - 4t + 4t^2) - \delta h - \delta \phi t/h - h = 0$

$hd^2 - 4hd^2 t + 4hd^2 t^2 - \delta h - \delta \phi t/h - h = 0$

Constant term: $hd^2 - \delta h - h = h(d^2 - \delta - 1) = h(d^2 - (d^2 - 1) - 1) = 0$. ✓

$4hd^2 t^2 - (4hd^2 + \delta\phi/h) t = 0$

$t(4hd^2 t - 4hd^2 - \delta\phi/h) = 0$

$t_P = \frac{4hd^2 + \delta\phi/h}{4hd^2} = 1 + \frac{\delta\phi}{4h^2 d^2}$.

$P_x = d(1 - 2t_P) = d\left(-1 - \frac{\delta\phi}{2h^2 d^2}\right) = -d - \frac{\delta\phi}{2h^2 d}$.

$P_y = h + \frac{\phi}{h} t_P = h + \frac{\phi}{h}\left(1 + \frac{\delta\phi}{4h^2 d^2}\right) = h + \frac{\phi}{h} + \frac{\delta\phi^2}{4h^3 d^2} = \frac{h^2 + \phi}{h} + \frac{\delta\phi^2}{4h^3 d^2}$.

$h^2 + \phi = h^2 + d^2 - 1 - h^2 = d^2 - 1 = \delta$.

$P_y = \frac{\delta}{h} + \frac{\delta\phi^2}{4h^3 d^2} = \frac{\delta}{h}\left(1 + \frac{\phi^2}{4h^2 d^2}\right) = \frac{\delta(4h^2 d^2 + \phi^2)}{4h^3 d^2}$.

$D = (d, \delta/h) = (d, \delta/h)$.

Direction $PD$:
$\Delta x = d - P_x = 2d + \frac{\delta\phi}{2h^2 d} = \frac{4h^2 d^2 + \delta\phi}{2h^2 d}$.

$\Delta y = \delta/h - P_y = \frac{\delta}{h} - \frac{\delta(4h^2 d^2 + \phi^2)}{4h^3 d^2} = \frac{\delta}{h}\left(1 - \frac{4h^2 d^2 + \phi^2}{4h^2 d^2}\right) = \frac{\delta}{h} \cdot \frac{-\phi^2}{4h^2 d^2} = \frac{-\delta\phi^2}{4h^3 d^2}$.

$Q$: $y = 0$. $s = -P_y / \Delta y = \frac{\delta(4h^2 d^2 + \phi^2)/(4h^3 d^2)}{\delta\phi^2/(4h^3 d^2)} = \frac{4h^2 d^2 + \phi^2}{\phi^2}$.

$x_Q = P_x + s \cdot \Delta x = -d - \frac{\delta\phi}{2h^2 d} + \frac{4h^2 d^2 + \phi^2}{\phi^2} \cdot \frac{4h^2 d^2 + \delta\phi}{2h^2 d}$.

Let me denote $\Sigma = 4h^2 d^2 + \phi^2$ and $\Gamma = 4h^2 d^2 + \delta\phi$.

$x_Q = -d - \frac{\delta\phi}{2h^2 d} + \frac{\Sigma \Gamma}{2h^2 d \phi^2}$.

$= \frac{-2h^2 d^2 - \delta\phi + \Sigma\Gamma/\phi^2}{2h^2 d}$... hmm, let me be more careful.

$= \frac{1}{2h^2 d}\left(-2h^2 d^2 - \delta\phi + \frac{\Sigma \Gamma}{\phi^2}\right)$

$= \frac{1}{2h^2 d \phi^2}\left(-2h^2 d^2 \phi^2 - \delta\phi^3 + \Sigma\Gamma\right)$

$\Sigma\Gamma = (4h^2 d^2 + \phi^2)(4h^2 d^2 + \delta\phi) = 16h^4 d^4 + 4h^2 d^2 \delta\phi + 4h^2 d^2 \phi^2 + \delta\phi^3$.

$-2h^2 d^2 \phi^2 - \delta\phi^3 + 16h^4 d^4 + 4h^2 d^2 \delta\phi + 4h^2 d^2 \phi^2 + \delta\phi^3$

$= 16h^4 d^4 + 4h^2 d^2 \delta\phi + 2h^2 d^2 \phi^2$

$= 2h^2 d^2(8h^2 d^2 + 2\delta\phi + \phi^2)$.

Now, $\phi = \delta - h^2 = d^2 - 1 - h^2$. $\delta = d^2 - 1$.

$2\delta\phi + \phi^2 = \phi(2\delta + \phi) = \phi(2\delta + \delta - h^2) = \phi(3\delta - h^2)$.

$8h^2 d^2 + 2\delta\phi + \phi^2 = 8h^2 d^2 + \phi(3\delta - h^2)$.

$\phi(3\delta - h^2) = (\delta - h^2)(3\delta - h^2) = 3\delta^2 - \delta h^2 - 3\delta h^2 + h^4 = 3\delta^2 - 4\delta h^2 + h^4$.

$8h^2 d^2 + 3\delta^2 - 4\delta h^2 + h^4$.

$\delta = d^2 - 1$, $\delta^2 = (d^2-1)^2 = d^4 - 2d^2 + 1$.

$= 8h^2 d^2 + 3d^4 - 6d^2 + 3 - 4(d^2-1)h^2 + h^4$

$= 8h^2 d^2 + 3d^4 - 6d^2 + 3 - 4d^2 h^2 + 4h^2 + h^4$

$= 4h^2 d^2 + 3d^4 - 6d^2 + 3 + 4h^2 + h^4$

$= 3d^4 + 4h^2 d^2 - 6d^2 + h^4 + 4h^2 + 3$

$= 3(d^4 - 2d^2 + 1) + 4h^2 d^2 + h^4 + 4h^2$

$= 3(d^2 - 1)^2 + 4h^2 d^2 + h^4 + 4h^2$

$= 3\delta^2 + 4h^2 d^2 + h^4 + 4h^2$

$= 3\delta^2 + h^2(4d^2 + h^2 + 4)$

$= 3\delta^2 + h^2(4(d^2 + 1) + h^2)$

Hmm, this doesn't simplify nicely. Let me try a different approach.

Actually, let me reconsider the problem. Maybe I should try to verify with a specific simple case where computations are easy.

Let me try an isosceles triangle where $d = 0$. But then $T = A$ and the parabola degenerates. So $d \neq 0$.

Let me try $B = (-1, 0)$, $C = (1, 0)$, $A = (d, h)$ with specific nice values.

Let me try $d = 1/2$, $h = \sqrt{3}/2$. Then $A = (1/2, \sqrt{3}/2)$, which is on the unit circle! So $a = 1$, and $A$ is on the circle of radius 1 centered at origin. But the circumcircle of $ABC$ is not the unit circle unless $B$ and $C$ are also on it. $B = (-1, 0)$ and $C = (1, 0)$ are on the unit circle. And $A = (1/2, \sqrt{3}/2)$ is on the unit circle. So the circumcircle is the unit circle, $O = (0, 0)$, $k = 0$.

Then $e = (d^2 - a^2)/h = (1/4 - 1)/(\sqrt{3}/2) = (-3/4)/(\sqrt{3}/2) = -3/(2\sqrt{3}) = -\sqrt{3}/2$.

$A' = (-1/2, -\sqrt{3}/2)$, $D = (1/2, -\sqrt{3}/2)$.

This is an equilateral triangle! $A = (1/2, \sqrt{3}/2)$, $B = (-1, 0)$, $C = (1, 0)$. $AB = AC = BC$... let me check. $AB = \sqrt{9/4 + 3/4} = \sqrt{3}$. $BC = 2$. Not equilateral. Actually $A$ is at angle $60°$ on the unit circle, $B$ at $180°$, $C$ at $0°$. So arc $BC$ (not containing $A$) is $180°$, arc $CA$ is $60°$, arc $AB$ is $120°$. The triangle has angles $A = 90°$, $B = 30°$, $C = 60°$. But the problem requires acute, and $A = 90°$ is not acute. Let me adjust.

Let me try $A$ at angle $80°$: $A = (\cos 80°, \sin 80°)$. Then $B = (-1, 0)$ (angle $180°$), $C = (1, 0)$ (angle $0°$). The triangle has angles: $A = (180° - 80°)/2 = 50°$... no, let me compute properly.

Arc $BC$ not containing $A$: from $C$ (0°) to $B$ (180°) going the other way (through 360°), which is 180°. So angle $A = 90°$. Hmm, that's because $B$ and $C$ are diametrically opposite. So any triangle with $B$ and $C$ diametrically opposite on the circumcircle has a right angle at $A$. Not acute.

So I can't have $B$ and $C$ diametrically opposite. Let me use a different setup.

Let me try the circumcircle as the unit circle with $B$ and $C$ not diametrically opposite.

Let $B = e^{i \cdot 200°}$, $C = e^{i \cdot 340°}$ (i.e., $-20°$), $A = e^{i \cdot 80°}$.

Actually, this is getting complicated. Let me go back to my coordinate system and just try to find the general formula for $QR/AM$ and see if it simplifies.

Let me use the normalized coordinates: $B = (-1, 0)$, $C = (1, 0)$, $A = (d, h)$, $M = (0, 0)$.

$\delta = d^2 - 1$, $\phi = d^2 - 1 - h^2 = \delta - h^2$.

$e = \delta/h$, $D = (d, \delta/h)$, $A' = (-d, \delta/h)$.

$R$: tangent to circumcircle at $A'$, intersected with $AD$ (which is $x = d$).

Circumcircle: $x^2 + (y - k)^2 = R_c^2$ where $k = \delta/(2h) + h/2 = (\delta + h^2)/(2h) = (d^2 - 1 + h^2)/(2h)$.

Wait, $k = (d^2 + h^2 - 1)/(2h)$. And $R_c^2 = 1 + k^2$.

Tangent at $A' = (-d, \delta/h)$: gradient $(2(-d), 2(\delta/h - k))$.

$\delta/h - k = \delta/h - (d^2 + h^2 - 1)/(2h) = (2\delta - d^2 - h^2 + 1)/(2h) = (2(d^2 - 1) - d^2 - h^2 + 1)/(2h) = (d^2 - 1 - h^2)/(2h) = \phi/(2h)$.

So gradient at $A'$ is $(-2d, \phi/h)$.

Tangent line: $-2d(x + d) + (\phi/h)(y - \delta/h) = 0$.

At $x = d$ (line $AD$): $-2d(2d) + (\phi/h)(y - \delta/h) = 0 \Rightarrow -4d^2 + (\phi/h)(y - \delta/h) = 0 \Rightarrow y - \delta/h = 4d^2 h/\phi \Rightarrow y = \delta/h + 4d^2 h/\phi$.

$R = (d, \delta/h + 4d^2 h/\phi)$.

Let me simplify: $y_R = \delta/h + 4d^2 h/\phi = \frac{\delta \phi + 4d^2 h^2}{h\phi}$.

Now, $\delta\phi + 4d^2 h^2 = \delta(\delta - h^2) + 4d^2 h^2 = \delta^2 - \delta h^2 + 4d^2 h^2 = (d^2-1)^2 - (d^2-1)h^2 + 4d^2 h^2$

$= d^4 - 2d^2 + 1 - d^2 h^2 + h^2 + 4d^2 h^2 = d^4 - 2d^2 + 1 + 3d^2 h^2 + h^2$

$= (d^2 - 1)^2 + h^2(3d^2 + 1) = \delta^2 + h^2(3d^2 + 1)$.

Hmm, also $= d^4 + 3d^2 h^2 + h^2 - 2d^2 + 1$. Not obviously simplifiable.

Let me denote $\Gamma = \delta\phi + 4d^2 h^2 = 4d^2 h^2 + \delta\phi$ (same as before).

$y_R = \Gamma/(h\phi)$.

Now I need $Q$. From the computation above:

$x_Q = \frac{2h^2 d^2(8h^2 d^2 + 2\delta\phi + \phi^2)}{2h^2 d \phi^2} = \frac{d(8h^2 d^2 + 2\delta\phi + \phi^2)}{\phi^2}$.

Wait, let me recompute. We had:

$x_Q = \frac{1}{2h^2 d \phi^2}\left(2h^2 d^2(8h^2 d^2 + 2\delta\phi + \phi^2)\right) = \frac{d(8h^2 d^2 + 2\delta\phi + \phi^2)}{\phi^2}$.

Let me denote $\Omega = 8h^2 d^2 + 2\delta\phi + \phi^2$.

$x_Q = d\Omega/\phi^2$.

$Q = (d\Omega/\phi^2, 0)$, $R = (d, \Gamma/(h\phi))$.

$QR^2 = (d\Omega/\phi^2 - d)^2 + (\Gamma/(h\phi))^2 = d^2(\Omega/\phi^2 - 1)^2 + \Gamma^2/(h^2\phi^2)$.

$= d^2((\Omega - \phi^2)/\phi^2)^2 + \Gamma^2/(h^2\phi^2)$

$= \frac{d^2(\Omega - \phi^2)^2}{\phi^4} + \frac{\Gamma^2}{h^2\phi^2}$

$= \frac{d^2 h^2 (\Omega - \phi^2)^2 + \Gamma^2 \phi^2}{h^2 \phi^4}$.

$\Omega - \phi^2 = 8h^2 d^2 + 2\delta\phi + \phi^2 - \phi^2 = 8h^2 d^2 + 2\delta\phi = 2(4h^2 d^2 + \delta\phi) = 2\Gamma$.

So $(\Omega - \phi^2)^2 = 4\Gamma^2$.

$QR^2 = \frac{d^2 h^2 \cdot 4\Gamma^2 + \Gamma^2 \phi^2}{h^2 \phi^4} = \frac{\Gamma^2(4d^2 h^2 + \phi^2)}{h^2 \phi^4}$.

$QR = \frac{|\Gamma| \sqrt{4d^2 h^2 + \phi^2}}{h \phi^2}$ (taking absolute values since distances are positive, and $\phi < 0$ for acute triangles, $\phi^2 > 0$).

$AM = \sqrt{d^2 + h^2}$.

$\frac{QR}{AM} = \frac{|\Gamma| \sqrt{4d^2 h^2 + \phi^2}}{h \phi^2 \sqrt{d^2 + h^2}}$.

Now, $\Gamma = 4d^2 h^2 + \delta\phi = 4d^2 h^2 + (d^2 - 1)(d^2 - 1 - h^2)$.

$4d^2 h^2 + \phi^2 = 4d^2 h^2 + (d^2 - 1 - h^2)^2$.

Note that $4d^2 h^2 + (d^2 - 1 - h^2)^2 = (2dh)^2 + (d^2 - 1 - h^2)^2$. This is of the form $a^2 + b^2$ where $a = 2dh$ and $b = d^2 - 1 - h^2$. And $a^2 + b^2 = (d^2 + h^2 - 1)^2 + 4h^2$... let me check:

$(d^2 + h^2 - 1)^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 - 2h^2$.

$4d^2 h^2 + (d^2 - 1 - h^2)^2 = 4d^2 h^2 + d^4 + 1 + h^4 - 2d^2 + 2h^2 - 2d^2 h^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 + 2h^2$.

$(d^2 + h^2 - 1)^2 + 4h^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 - 2h^2 + 4h^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 + 2h^2$.

Yes! So $4d^2 h^2 + \phi^2 = (d^2 + h^2 - 1)^2 + 4h^2$.

Hmm, that's a nice identity but doesn't immediately simplify the ratio.

Let me also compute $\Gamma$:

$\Gamma = 4d^2 h^2 + (d^2 - 1)(d^2 - 1 - h^2) = 4d^2 h^2 + (d^2-1)^2 - (d^2-1)h^2$

$= (d^2 - 1)^2 + h^2(4d^2 - d^2 + 1) = (d^2-1)^2 + h^2(3d^2 + 1)$.

$= d^4 - 2d^2 + 1 + 3d^2 h^2 + h^2$.

Hmm. Let me also note that $\phi = d^2 - 1 - h^2$, so $\phi^2 = (d^2 - 1 - h^2)^2$.

The ratio is:

$\frac{QR}{AM} = \frac{|\Gamma| \sqrt{(d^2 + h^2 - 1)^2 + 4h^2}}{h (d^2 - 1 - h^2)^2 \sqrt{d^2 + h^2}}$.

This is clearly not a constant—it depends on $d$ and $h$. So either the problem has a different interpretation, or I'm making an error.

Let me verify with example 1: $a = 3$, so I need to rescale. With $a = 1$: $d = 1/3$, $h = 4/3$.

$\delta = 1/9 - 1 = -8/9$. $\phi = -8/9 - 16/9 = -24/9 = -8/3$.

$\Gamma = 4 \cdot (1/9) \cdot (16/9) + (-8/9)(-8/3) = 64/81 + 64/27 = 64/81 + 192/81 = 256/81$.

$4d^2 h^2 + \phi^2 = 64/81 + 64/9 = 64/81 + 576/81 = 640/81$.

$QR = \        — AI历史解题过程（thinking）
#   oda_math_460k_00004902         — 题目ID

# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search.
- All information you need is in this AGENTS.md file.
- Output your analysis directly in your response (in this TUI).
- End your analysis with a line containing exactly: `### ANALYSIS COMPLETE`

## Analysis Task

You are given three inputs:
1. **Problem** — a math competition problem
2. **Standard Solution** — the correct solution from the problem bank
3. **AI's Thinking** — an AI's attempted solution process (its reasoning when it tried to solve the problem, but failed)

Your task: analyze WHY the AI failed, by comparing its thinking with the standard solution.

### Dimension 1: Failure Type

Compare the standard solution's key approach with the AI's thinking:

- **DIRECTION_ERROR**: The AI's thinking went in a fundamentally wrong direction. The standard solution uses a specific mathematical approach that the AI never considered. The AI was exploring a completely different strategy. The failure is about *which direction to explore*, not about running out of time.

- **TOKEN_LIMIT**: The AI's thinking was going in the RIGHT direction — it was using the same key approach as the standard solution (or a valid alternative) — but ran out of tokens before completing the proof. The failure is about *not enough time*, not about *wrong direction*.

- **CONNECTION_ERROR**: The AI didn't really attempt the problem. The thinking is very short, contains connection errors, or has no meaningful mathematical content. This is a technical failure, not a mathematical one.

- **PARTIAL_PROGRESS**: The AI's thinking was partially in the right direction — it identified some key ideas from the standard solution — but missed the crucial turning point. The AI was on the right track but took a wrong turn at a critical juncture.

### Dimension 2: Key Turning Point Type

If the verdict is DIRECTION_ERROR or PARTIAL_PROGRESS, identify what type of key turning point the standard solution uses:

1. **mod_p_grouping**: The standard solution uses modular arithmetic (mod p, where p is small/obvious like 4, 8) to group/categorize objects and find a contradiction or hidden structure.

2. **mod_p_non_obvious**: The standard solution uses modular arithmetic where the prime p is NOT obvious from the problem statement (e.g., mod 11, mod p where p needs to be discovered through analysis).

3. **quadratic_residue_euler**: The standard solution uses quadratic residues, Legendre symbols, or Euler's criterion.

4. **lte_lemma**: The standard solution uses the Lifting The Exponent (LTE) lemma.

5. **p_adic_valuation**: The standard solution uses p-adic valuation (v_p) analysis.

6. **multi_step_mod_p**: The standard solution uses multiple steps of modular arithmetic analysis (not just one mod operation).

7. **crt**: The standard solution uses the Chinese Remainder Theorem (combining information from multiple moduli).

8. **permutation_polynomial**: The standard solution uses properties of permutation polynomials over finite fields.

9. **finite_field_structure**: The standard solution exploits the structure of finite fields (Z/pZ, F_p, F_p^k).

10. **other**: None of the above categories fit. Describe the technique in dimension2_explanation.

### Output Format

Output your analysis in this EXACT XML format. The XML must be well-formed and parseable.

```xml
<analysis>
  <problem_id>oda_math_460k_00004902</problem_id>
  <dimension1_verdict>DIRECTION_ERROR|TOKEN_LIMIT|CONNECTION_ERROR|PARTIAL_PROGRESS</dimension1_verdict>
  <dimension1_explanation>1-3 sentences explaining the verdict</dimension1_explanation>
  <dimension2_turning_point_type>mod_p_grouping|mod_p_non_obvious|quadratic_residue_euler|lte_lemma|p_adic_valuation|multi_step_mod_p|crt|permutation_polynomial|finite_field_structure|other</dimension2_turning_point_type>
  <dimension2_explanation>1-3 sentences describing the key turning point in the standard solution</dimension2_explanation>
  <ai_direction_summary>1 sentence describing what direction the AI's thinking went</ai_direction_summary>
  <standard_solution_key_technique>1 sentence describing the key technique in the standard solution</standard_solution_key_technique>
  <confidence>high|medium|low</confidence>
</analysis>
```

After the XML block, output exactly: `### ANALYSIS COMPLETE`

**Rules:**
- The XML must be inside a ```xml code block
- Do NOT add any text before or after the XML block (except ### ANALYSIS COMPLETE)
- If the AI's thinking is too short to analyze (< 500 chars of mathematical content), output CONNECTION_ERROR
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

Jake can wash his car with 1 bottle of car wash soap 4 times.  If each bottle costs $4.00, and he washes his car once a week for 20 weeks, how much does he spend on car soap?

## Standard Solution

<think>Okay, let's see. The problem is about Jake washing his car and figuring out how much he spends on soap over 20 weeks. Let's break it down step by step.

First, the problem says that 1 bottle of car wash soap can be used 4 times. So each bottle lasts for 4 washes. Then, each bottle costs $4.00. Jake washes his car once a week for 20 weeks. We need to find out the total cost.

First, let's figure out how many times he needs to wash his car. Since he washes once a week for 20 weeks, that's 20 washes total. 

Next, we need to find out how many bottles of soap he needs. Each bottle does 4 washes. So, if he has 20 washes, we divide the total number of washes by the number of washes per bottle. That's 20 divided by 4. Let me calculate that: 20 ÷ 4 = 5. So he needs 5 bottles.

Now, each bottle is $4.00. So 5 bottles times $4.00 per bottle. That's 5 × 4 = 20. So the total cost is $20.00.

Wait, let me double-check. 4 washes per bottle, 20 washes total. 20 divided by 4 is 5 bottles. 5 times $4 is $20. Yep, that makes sense. I think that's right.
</think>

Jake washes his car once a week for 20 weeks, so he needs 20 washes. Each bottle of soap can be used 4 times, so the number of bottles needed is \( \frac{20}{4} = 5 \) bottles. Each bottle costs $4.00, so the total cost is \( 5 \times 4 = 20 \) dollars.

\(\boxed{20}\)

## AI's Thinking (Attempted Solution Process)

Let me analyze this geometry problem carefully.

We have an acute triangle $ABC$. $T$ is the reflection of $A$ in the perpendicular bisector of $BC$. $A'$ is the $A$-antipode on the circumcircle $(ABC)$ (the point diametrically opposite to $A$). $P$ is the second intersection of $AA'$ with the parabola through $ABCT$. $D$ is the point on $(ABC)$ such that $AD \perp BC$. $Q = PD \cap BC$. $R$ is the intersection of $AD$ with the tangent to $(ADC)$ at $A'$. $M$ is the midpoint of $BC$. Calculate $QR/AM$.

Wait, let me re-read. $R$ is the intersection of $AD$ with the tangent to $(ADC)$ at $A'$. But $A'$ is the antipode of $A$ on $(ABC)$. Is $A'$ on $(ADC)$? $D$ is on $(ABC)$, so $(ADC) = (ABC)$ since $A$, $D$, $C$ are all on the circumcircle. So $(ADC)$ is the same as $(ABC)$. So $R$ is the intersection of $AD$ with the tangent to $(ABC)$ at $A'$.

Let me set up coordinates. Let me place the circumcircle as the unit circle, or use a convenient coordinate system.

Actually, let me think about this more carefully. Let me use coordinates with $BC$ horizontal.

Let me place $M$ at the origin, $BC$ along the x-axis. Let $B = (-a, 0)$, $C = (a, 0)$, so $M = (0, 0)$ and $BC = 2a$. Let $A = (d, h)$ with $h > 0$ (acute triangle).

The perpendicular bisector of $BC$ is the y-axis (since $M$ is the midpoint and $BC$ is along x-axis). The reflection of $A = (d, h)$ in the y-axis is $T = (-d, h)$.

Now, $A'$ is the antipode of $A$ on the circumcircle. Let me find the circumcircle first.

The circumcircle passes through $B = (-a, 0)$, $C = (a, 0)$, $A = (d, h)$. The center is on the y-axis (by symmetry of $B$ and $C$), say $O = (0, k)$. Then:
- $OB^2 = a^2 + k^2$
- $OA^2 = d^2 + (h - k)^2$

So $a^2 + k^2 = d^2 + h^2 - 2hk + k^2$, giving $a^2 = d^2 + h^2 - 2hk$, so $k = \frac{d^2 + h^2 - a^2}{2h}$.

The circumradius $R_c = \sqrt{a^2 + k^2}$.

$A'$ is the antipode of $A$, so $A' = 2O - A = (-d, 2k - h)$.

Now, $D$ is the point on $(ABC)$ such that $AD \perp BC$. Since $BC$ is along the x-axis, $AD$ is vertical, so $D$ has the same x-coordinate as $A$, which is $d$. $D$ is on the circumcircle: $d^2 + (y_D - k)^2 = a^2 + k^2$, so $(y_D - k)^2 = a^2 + k^2 - d^2$. We have $A = (d, h)$ is one solution, so $y_D - k = -(h - k)$, giving $y_D = 2k - h$. So $D = (d, 2k - h)$.

Interesting, so $D = (d, 2k - h)$ and $A' = (-d, 2k - h)$. So $D$ and $A'$ have the same y-coordinate! They are reflections of each other in the y-axis. That makes sense because $D$ is the reflection of $A'$ in the perpendicular bisector of $BC$... wait, no. $A' = (-d, 2k-h)$ and $D = (d, 2k-h)$. Yes, $D$ is the reflection of $A'$ in the y-axis (perpendicular bisector of $BC$). And $T = (-d, h)$ is the reflection of $A$ in the y-axis.

Now, the line $AA'$: $A = (d, h)$, $A' = (-d, 2k - h)$. Direction: $(-2d, 2k - 2h) = (-2d, 2(k-h))$, or simplified $(-d, k-h)$.

Parametrize: $(x, y) = (d, h) + t(-d, k-h) = (d(1-t), h + t(k-h))$.

At $t = 0$: $A$. At $t = 1$: $A'$. At $t = 2$: $(d(1-2), h + 2(k-h)) = (-d, 2k - h) = A'$. Wait, that's wrong. At $t = 1$: $(d - d, h + k - h) = (0, k) = O$, the center. At $t = 2$: $(-d, h + 2(k-h)) = (-d, 2k - h) = A'$. So $A'$ corresponds to $t = 2$.

Hmm, let me recheck. $A' = (-d, 2k - h)$. With $t = 2$: $x = d(1-2) = -d$ ✓, $y = h + 2(k-h) = 2k - h$ ✓. Good.

Now I need the parabola through $A$, $B$, $C$, $T$.

$A = (d, h)$, $B = (-a, 0)$, $C = (a, 0)$, $T = (-d, h)$.

A general parabola has equation $\alpha x^2 + \beta xy + \gamma y^2 + \delta x + \epsilon y + \zeta = 0$ with the conic being a parabola (discriminant $\beta^2 - 4\alpha\gamma = 0$).

By symmetry, since $A$ and $T$ are symmetric about the y-axis, and $B$ and $C$ are symmetric about the y-axis, the parabola should be symmetric about the y-axis. So the equation has no odd powers of $x$: $\alpha x^2 + \gamma y^2 + \epsilon y + \zeta = 0$ (with $\beta = 0$, $\delta = 0$).

For a parabola, $\beta^2 - 4\alpha\gamma = 0 \Rightarrow -4\alpha\gamma = 0$, so either $\alpha = 0$ or $\gamma = 0$.

If $\alpha = 0$: $\gamma y^2 + \epsilon y + \zeta = 0$, which is just a pair of horizontal lines (or a single line), not a parabola through 4 points in general position. So $\gamma = 0$.

Then $\alpha x^2 + \epsilon y + \zeta = 0$, i.e., $x^2 = -\frac{\epsilon}{\alpha} y - \frac{\zeta}{\alpha}$, a parabola with vertical axis.

Using $B = (-a, 0)$: $\alpha a^2 + \zeta = 0 \Rightarrow \zeta = -\alpha a^2$.
Using $A = (d, h)$: $\alpha d^2 + \epsilon h + \zeta = 0 \Rightarrow \alpha d^2 + \epsilon h - \alpha a^2 = 0 \Rightarrow \epsilon h = \alpha(a^2 - d^2) \Rightarrow \epsilon = \frac{\alpha(a^2 - d^2)}{h}$.

So the parabola is: $\alpha x^2 + \frac{\alpha(a^2 - d^2)}{h} y - \alpha a^2 = 0$, or $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0$.

So $x^2 = a^2 - \frac{a^2 - d^2}{h} y$.

Let me verify with $T = (-d, h)$: $d^2 = a^2 - \frac{a^2 - d^2}{h} \cdot h = a^2 - (a^2 - d^2) = d^2$ ✓.

Now, $P$ is the second intersection of $AA'$ with this parabola. The line $AA'$ is parametrized as $(d(1-t), h + t(k-h))$.

Substitute into $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0$:

$d^2(1-t)^2 + \frac{a^2 - d^2}{h}(h + t(k-h)) - a^2 = 0$

$d^2(1 - 2t + t^2) + (a^2 - d^2) + \frac{(a^2 - d^2)(k-h)}{h} t - a^2 = 0$

$d^2 - 2d^2 t + d^2 t^2 + a^2 - d^2 + \frac{(a^2 - d^2)(k-h)}{h} t - a^2 = 0$

$d^2 t^2 - 2d^2 t + \frac{(a^2 - d^2)(k-h)}{h} t = 0$

$t \left[ d^2 t - 2d^2 + \frac{(a^2 - d^2)(k-h)}{h} \right] = 0$

So $t = 0$ (which gives $A$) or $t = \frac{2d^2 - \frac{(a^2 - d^2)(k-h)}{h}}{d^2} = 2 - \frac{(a^2 - d^2)(k-h)}{d^2 h}$.

Recall $k = \frac{d^2 + h^2 - a^2}{2h}$, so $k - h = \frac{d^2 + h^2 - a^2 - 2h^2}{2h} = \frac{d^2 - h^2 - a^2}{2h}$.

So $\frac{(a^2 - d^2)(k-h)}{h} = \frac{(a^2 - d^2)(d^2 - h^2 - a^2)}{2h^2}$.

Let me denote $t_P = 2 - \frac{(a^2 - d^2)(d^2 - h^2 - a^2)}{2d^2 h^2}$.

Note that $d^2 - h^2 - a^2 = -(a^2 + h^2 - d^2)$ and $a^2 - d^2 = -(d^2 - a^2)$.

So $(a^2 - d^2)(d^2 - h^2 - a^2) = (-(d^2 - a^2))(-(a^2 + h^2 - d^2)) = (d^2 - a^2)(a^2 + h^2 - d^2)$.

Hmm, let me just compute numerically to get intuition. Let me pick a specific triangle.

Let me try $B = (-3, 0)$, $C = (3, 0)$, $A = (1, 4)$. So $a = 3$, $d = 1$, $h = 4$.

Check acute: $AB = \sqrt{16 + 16} = \sqrt{32}$, $AC = \sqrt{4 + 16} = \sqrt{20}$, $BC = 6$. Check $AB^2 + AC^2 = 52 > 36 = BC^2$ ✓, $AB^2 + BC^2 = 68 > 20$ ✓, $AC^2 + BC^2 = 56 > 32$ ✓. Acute.

$k = \frac{1 + 16 - 9}{8} = \frac{8}{8} = 1$. So $O = (0, 1)$, $R_c = \sqrt{9 + 1} = \sqrt{10}$.

$A' = (-1, 2 \cdot 1 - 4) = (-1, -2)$. Check: $(-1)^2 + (-2-1)^2 = 1 + 9 = 10$ ✓.
$D = (1, -2)$. Check: $1 + 9 = 10$ ✓.

Parabola: $x^2 + \frac{9 - 1}{4} y - 9 = 0 \Rightarrow x^2 + 2y - 9 = 0 \Rightarrow y = \frac{9 - x^2}{2}$.

Line $AA'$: from $(1, 4)$ to $(-1, -2)$. Direction $(-2, -6)$, or $(-1, -3)$. Parametrize: $(1 - t, 4 - 3t)$.

Substitute into parabola: $(1-t)^2 + 2(4 - 3t) - 9 = 0 \Rightarrow 1 - 2t + t^2 + 8 - 6t - 9 = 0 \Rightarrow t^2 - 8t = 0 \Rightarrow t(t - 8) = 0$.

So $t = 0$ (point $A$) or $t = 8$ (point $P$). $P = (1 - 8, 4 - 24) = (-7, -20)$.

Now $D = (1, -2)$. Line $PD$: from $(-7, -20)$ to $(1, -2)$. Direction $(8, 18)$, or $(4, 9)$. Parametrize: $(-7 + 4s, -20 + 9s)$.

$Q = PD \cap BC$. $BC$ is the x-axis ($y = 0$). So $-20 + 9s = 0 \Rightarrow s = 20/9$. $Q = (-7 + 80/9, 0) = (-63/9 + 80/9, 0) = (17/9, 0)$.

Now $R$: intersection of $AD$ with the tangent to $(ABC)$ at $A'$.

$AD$ is the vertical line $x = 1$ (since $A = (1, 4)$ and $D = (1, -2)$).

The circumcircle is $x^2 + (y-1)^2 = 10$. The tangent at $A' = (-1, -2)$: the radius to $A'$ is from $O = (0, 1)$ to $(-1, -2)$, direction $(-1, -3)$. The tangent is perpendicular to this, so direction $(3, -1)$. Tangent line: $(-1, -2) + u(3, -1)$, i.e., $x = -1 + 3u$, $y = -2 - u$.

Intersection with $x = 1$: $-1 + 3u = 1 \Rightarrow u = 2/3$. $y = -2 - 2/3 = -8/3$. So $R = (1, -8/3)$.

Now $Q = (17/9, 0)$, $R = (1, -8/3) = (9/9, -8/3)$.

$QR = \sqrt{(17/9 - 1)^2 + (0 + 8/3)^2} = \sqrt{(8/9)^2 + (8/3)^2} = \sqrt{64/81 + 64/9} = \sqrt{64/81 + 576/81} = \sqrt{640/81} = \frac{8\sqrt{10}}{9}$.

$AM = \sqrt{(1-0)^2 + (4-0)^2} = \sqrt{17}$.

$QR/AM = \frac{8\sqrt{10}}{9\sqrt{17}}$.

Hmm, that doesn't look like a clean ratio. Let me double-check.

Wait, maybe I should re-examine. The problem says "the tangent to $(ADC)$ at $A'$". Since $A$, $D$, $C$ are on the circumcircle, $(ADC) = (ABC)$. So the tangent is to the circumcircle at $A'$. That's what I computed.

Let me recheck $QR$. $Q = (17/9, 0)$, $R = (1, -8/3)$.

$QR^2 = (17/9 - 9/9)^2 + (0 - (-8/3))^2 = (8/9)^2 + (8/3)^2 = 64/81 + 64/9 = 64/81 + 576/81 = 640/81$.

$QR = \sqrt{640}/9 = 8\sqrt{10}/9$.

$AM = \sqrt{1 + 16} = \sqrt{17}$.

$QR/AM = \frac{8\sqrt{10}}{9\sqrt{17}} = \frac{8\sqrt{170}}{9 \cdot 17} = \frac{8\sqrt{170}}{153}$.

That's not clean. Let me try another triangle to see if the ratio is constant.

Let me try $B = (-2, 0)$, $C = (2, 0)$, $A = (0, 3)$. So $a = 2$, $d = 0$, $h = 3$.

But $d = 0$ means $A$ is on the y-axis, so $T = A$, and the parabola degenerates. Let me avoid that.

Let me try $B = (-4, 0)$, $C = (4, 0)$, $A = (2, 5)$. $a = 4$, $d = 2$, $h = 5$.

Check acute: $AB^2 = 4 + 25 = 29$, $AC^2 = 4 + 25 = 29$, $BC^2 = 16$. All angles acute? $AB^2 + AC^2 = 58 > 16$ ✓, $AB^2 + BC^2 = 45 > 29$ ✓. Yes acute (isosceles).

$k = \frac{4 + 25 - 16}{10} = \frac{13}{10}$. $O = (0, 13/10)$, $R_c = \sqrt{16 + 169/100} = \sqrt{1769/100} = \sqrt{1769}/10$.

$A' = (-2, 2 \cdot 13/10 - 5) = (-2, -12/10) = (-2, -6/5)$.
$D = (2, -6/5)$.

Parabola: $x^2 + \frac{16 - 4}{5} y - 16 = 0 \Rightarrow x^2 + \frac{12}{5} y - 16 = 0$.

Line $AA'$: from $(2, 5)$ to $(-2, -6/5)$. Direction $(-4, -6/5 - 5) = (-4, -31/5)$. Parametrize: $(2 - 4t, 5 - \frac{31}{5}t)$.

Substitute: $(2-4t)^2 + \frac{12}{5}(5 - \frac{31}{5}t) - 16 = 0$

$4 - 16t + 16t^2 + 12 - \frac{372}{25}t - 16 = 0$

$16t^2 - 16t - \frac{372}{25}t + 0 = 0$

$16t^2 - (16 + \frac{372}{25})t = 0$

$16t^2 - \frac{400 + 372}{25}t = 0$

$16t^2 - \frac{772}{25}t = 0$

$t(16t - \frac{772}{25}) = 0$

$t = 0$ or $t = \frac{772}{400} = \frac{193}{100}$.

$P = (2 - 4 \cdot \frac{193}{100}, 5 - \frac{31}{5} \cdot \frac{193}{100}) = (2 - \frac{772}{100}, 5 - \frac{5983}{500}) = (\frac{200 - 772}{100}, \frac{2500 - 5983}{500}) = (-\frac{572}{100}, -\frac{3483}{500}) = (-\frac{143}{25}, -\frac{3483}{500})$.

Let me simplify: $P_x = -143/25$, $P_y = -3483/500$.

$D = (2, -6/5) = (2, -600/500)$.

Line $PD$: from $P = (-143/25, -3483/500)$ to $D = (2, -6/5)$.

Direction: $(2 + 143/25, -6/5 + 3483/500) = (50/25 + 143/25, -600/500 + 3483/500) = (193/25, 2883/500)$.

$Q = PD \cap BC$ (y = 0). Parametrize: $P + s \cdot \text{direction}$.

$y_Q = -3483/500 + s \cdot 2883/500 = 0 \Rightarrow s = 3483/2883 = 1161/961 = 1161/961$.

Let me simplify: $\gcd(3483, 2883)$. $3483 = 1 \cdot 2883 + 600$. $2883 = 4 \cdot 600 + 483$. $600 = 1 \cdot 483 + 117$. $483 = 4 \cdot 117 + 15$. $117 = 7 \cdot 15 + 12$. $15 = 1 \cdot 12 + 3$. $12 = 4 \cdot 3$. So $\gcd = 3$. $s = 1161/961$.

$x_Q = -143/25 + \frac{1161}{961} \cdot \frac{193}{25} = \frac{1}{25}(-143 + \frac{1161 \cdot 193}{961})$.

$1161 \cdot 193 = 1161 \cdot 200 - 1161 \cdot 7 = 232200 - 8127 = 224073$.

$224073 / 961$: $961 \cdot 233 = 224113$. Hmm, that's not exact. $961 \cdot 233 = 961 \cdot 200 + 961 \cdot 33 = 192200 + 31713 = 223913$. $224073 - 223913 = 160$. So $224073/961 = 233 + 160/961$. Not clean.

This is getting messy. Let me try a different approach—maybe use the first example and see if the answer simplifies, or try to find the general formula.

Actually, let me reconsider. Maybe the ratio is not constant and depends on the triangle, but the problem says "calculate the ratio", implying it's a constant. Let me recheck my first computation.

First example: $a = 3$, $d = 1$, $h = 4$.
$QR/AM = \frac{8\sqrt{10}}{9\sqrt{17}}$.

$\frac{8\sqrt{10}}{9\sqrt{17}} = \frac{8}{9}\sqrt{\frac{10}{17}}$. Not a clean number.

Hmm, let me reconsider the problem. Maybe I'm misunderstanding something.

"Let $R$ be the intersection of $AD$ with the tangent to $(ADC)$ at $A'$."

Wait—maybe $(ADC)$ doesn't mean the circumcircle of triangle $ADC$. Maybe it means something else? In some notations, $(ADC)$ could refer to a specific circle. But conventionally, $(ADC)$ is the circumcircle of triangle $ADC$, which since $A$, $D$, $C$ are on the circumcircle of $ABC$, is the same as $(ABC)$.

Unless $D$ is not on the circumcircle? Let me re-read: "Let $D$ be the point on $(ABC)$ such that $AD \perp BC$." Yes, $D$ is on $(ABC)$.

So $(ADC) = (ABC)$, and the tangent at $A'$ is the tangent to the circumcircle at $A'$.

Let me recheck my computation for the first example.

$O = (0, 1)$, $A' = (-1, -2)$. The tangent at $A'$ to $x^2 + (y-1)^2 = 10$:

The gradient of $x^2 + (y-1)^2$ at $(-1, -2)$ is $(-2, -6)$. Tangent line: $-2(x+1) - 6(y+2) = 0 \Rightarrow -2x - 2 - 6y - 12 = 0 \Rightarrow 2x + 6y + 14 = 0 \Rightarrow x + 3y + 7 = 0$.

$AD$ is $x = 1$. So $1 + 3y + 7 = 0 \Rightarrow y = -8/3$. $R = (1, -8/3)$. ✓

$Q = (17/9, 0)$. $QR^2 = (17/9 - 1)^2 + (8/3)^2 = (8/9)^2 + (8/3)^2 = 64/81 + 64/9 = 64(1/81 + 1/9) = 64(1/81 + 9/81) = 64 \cdot 10/81 = 640/81$.

$QR = 8\sqrt{10}/9$. $AM = \sqrt{17}$. Ratio $= 8\sqrt{10}/(9\sqrt{17})$.

Let me try yet another triangle to check if this is constant.

$B = (-1, 0)$, $C = (1, 0)$, $A = (0.5, 2)$. $a = 1$, $d = 0.5$, $h = 2$.

Check acute: $AB^2 = 0.25 + 4 = 4.25$, $AC^2 = 0.25 + 4 = 4.25$, $BC^2 = 4$. $AB^2 + BC^2 = 8.25 > 4.25$ ✓. Acute.

$k = \frac{0.25 + 4 - 1}{4} = \frac{3.25}{4} = \frac{13}{16}$. $O = (0, 13/16)$.

$A' = (-0.5, 2 \cdot 13/16 - 2) = (-0.5, 13/8 - 2) = (-0.5, -3/8)$.
$D = (0.5, -3/8)$.

Parabola: $x^2 + \frac{1 - 0.25}{2} y - 1 = 0 \Rightarrow x^2 + \frac{3}{8} y - 1 = 0$.

Line $AA'$: from $(0.5, 2)$ to $(-0.5, -3/8)$. Direction $(-1, -19/8)$. Parametrize: $(0.5 - t, 2 - \frac{19}{8}t)$.

Substitute: $(0.5 - t)^2 + \frac{3}{8}(2 - \frac{19}{8}t) - 1 = 0$

$0.25 - t + t^2 + \frac{3}{4} - \frac{57}{64}t - 1 = 0$

$t^2 - t - \frac{57}{64}t + 0.25 + 0.75 - 1 = 0$

$t^2 - \frac{64 + 57}{64}t = 0$

$t^2 - \frac{121}{64}t = 0$

$t(t - \frac{121}{64}) = 0$

$t = 0$ or $t = 121/64$.

$P = (0.5 - 121/64, 2 - \frac{19}{8} \cdot \frac{121}{64}) = (32/64 - 121/64, 2 - \frac{2299}{512}) = (-89/64, 1024/512 - 2299/512) = (-89/64, -1275/512)$.

$D = (0.5, -3/8) = (32/64, -192/512)$.

Line $PD$: direction $(32/64 + 89/64, -192/512 + 1275/512) = (121/64, 1083/512)$.

$Q$: $y = 0$. $-1275/512 + s \cdot 1083/512 = 0 \Rightarrow s = 1275/1083 = 425/361$.

$x_Q = -89/64 + \frac{425}{361} \cdot \frac{121}{64} = \frac{1}{64}(-89 + \frac{425 \cdot 121}{361})$.

$425 \cdot 121 = 51425$. $51425/361 = 51425/361$. $361 \cdot 142 = 51262$. $51425 - 51262 = 163$. So $51425/361 = 142 + 163/361$. Not clean.

Hmm, $361 = 19^2$. $163$ is prime. So $x_Q = \frac{1}{64} \cdot \frac{-89 \cdot 361 + 51425}{361} = \frac{-32129 + 51425}{64 \cdot 361} = \frac{19296}{23104}$.

$19296 / 23104$: $\gcd$? $19296 = 2^5 \cdot 3 \cdot 201 = ...$. Let me just compute: $19296 / 64 = 301.5$. Hmm. $23104 / 64 = 361$. So $x_Q = 19296/23104$. $19296 = 64 \cdot 301.5$? No. $64 \cdot 301 = 19264$. $19296 - 19264 = 32$. So $19296 = 64 \cdot 301 + 32$. Not divisible by 64.

Let me just compute numerically. $x_Q = 19296/23104 \approx 0.8352$.

$R$: tangent to circumcircle at $A'$. Circumcircle: $x^2 + (y - 13/16)^2 = 1 + (13/16)^2 = 1 + 169/256 = 425/256$.

At $A' = (-1/2, -3/8)$: gradient $(-1, 2(-3/8 - 13/16)) = (-1, 2(-6/16 - 13/16)) = (-1, 2(-19/16)) = (-1, -19/8)$.

Tangent: $-1(x + 1/2) - \frac{19}{8}(y + 3/8) = 0 \Rightarrow -(x + 1/2) - \frac{19}{8}(y + 3/8) = 0$.

$AD$ is $x = 1/2$. So $-(1/2 + 1/2) - \frac{19}{8}(y + 3/8) = 0 \Rightarrow -1 - \frac{19}{8}(y + 3/8) = 0 \Rightarrow \frac{19}{8}(y + 3/8) = -1 \Rightarrow y + 3/8 = -8/19 \Rightarrow y = -8/19 - 3/8 = (-64 - 57)/152 = -121/152$.

$R = (1/2, -121/152)$.

$Q = (19296/23104, 0)$. Let me simplify $19296/23104$. $\gcd(19296, 23104)$: $23104 - 19296 = 3808$. $19296 / 3808 = 5.07$. $19296 = 5 \cdot 3808 + 256$. $3808 / 256 = 14.875$. $3808 = 14 \cdot 256 + 224$. $256 / 224 = 1$ r $32$. $224 / 32 = 7$. So $\gcd = 32$. $19296/32 = 603$. $23104/32 = 722$. So $x_Q = 603/722$. $722 = 2 \cdot 361 = 2 \cdot 19^2$. $603 = 3 \cdot 201 = 3 \cdot 3 \cdot 67 = 9 \cdot 67$. $\gcd(603, 722) = 1$. So $x_Q = 603/722$.

$R = (1/2, -121/152)$. $152 = 8 \cdot 19$. $121 = 11^2$.

$QR^2 = (603/722 - 1/2)^2 + (121/152)^2 = (603/722 - 361/722)^2 + (121/152)^2 = (242/722)^2 + (121/152)^2$.

$242/722 = 121/361$. So $QR^2 = (121/361)^2 + (121/152)^2 = 121^2 (1/361^2 + 1/152^2)$.

$361 = 19^2$, $152 = 8 \cdot 19$. $361^2 = 19^4$, $152^2 = 64 \cdot 19^2$.

$1/361^2 + 1/152^2 = 1/19^4 + 1/(64 \cdot 19^2) = (64 + 19^2)/(64 \cdot 19^4) = (64 + 361)/(64 \cdot 19^4) = 425/(64 \cdot 19^4)$.

$QR^2 = 121^2 \cdot 425 / (64 \cdot 19^4) = 14641 \cdot 425 / (64 \cdot 130321)$.

$14641 = 121^2 = 11^4$. $130321 = 19^4$.

$QR = 121 \sqrt{425} / (8 \cdot 19^2) = 121 \sqrt{425} / (8 \cdot 361) = 121 \sqrt{425} / 2888$.

$\sqrt{425} = 5\sqrt{17}$. $QR = 121 \cdot 5\sqrt{17} / 2888 = 605\sqrt{17}/2888$.

$2888 = 8 \cdot 361 = 8 \cdot 19^2$. $605 = 5 \cdot 121 = 5 \cdot 11^2$.

$AM = \sqrt{0.25 + 4} = \sqrt{4.25} = \sqrt{17/4} = \sqrt{17}/2$.

$QR/AM = \frac{605\sqrt{17}/2888}{\sqrt{17}/2} = \frac{605 \cdot 2}{2888} = \frac{1210}{2888}$.

$1210/2888$: $\gcd$? $2888 = 2 \cdot 1210 + 468$. $1210 = 2 \cdot 468 + 274$. $468 = 1 \cdot 274 + 194$. $274 = 1 \cdot 194 + 80$. $194 = 2 \cdot 80 + 34$. $80 = 2 \cdot 34 + 12$. $34 = 2 \cdot 12 + 10$. $12 = 1 \cdot 10 + 2$. $10 = 5 \cdot 2$. $\gcd = 2$.

$1210/2 = 605$. $2888/2 = 1444$. $605/1444$. $1444 = 4 \cdot 361 = 4 \cdot 19^2 = (2 \cdot 19)^2 = 38^2$. $605 = 5 \cdot 121 = 5 \cdot 11^2$.

$QR/AM = 605/1444 = 5 \cdot 11^2 / (2 \cdot 19)^2 = 5 \cdot 121 / 1444$.

For the first example: $QR/AM = 8\sqrt{10}/(9\sqrt{17})$. Let me compute this numerically: $8\sqrt{10} \approx 8 \cdot 3.162 = 25.30$. $9\sqrt{17} \approx 9 \cdot 4.123 = 37.11$. Ratio $\approx 0.682$.

For the second example: $605/1444 \approx 0.419$.

These are different! So the ratio is NOT constant. That means either I'm making an error, or the problem has a specific answer that I'm not getting because of a misunderstanding.

Let me re-read the problem very carefully.

"Let $ABC$ be an acute triangle and let $T$ be the reflection of $A$ in the perpendicular bisector of $BC$."

OK so $T$ is the reflection of $A$ across the perpendicular bisector of $BC$. ✓

"Let $A'$ be the $A$-antipode on the circumcircle $(ABC)$"

$A'$ is the point diametrically opposite $A$ on the circumcircle. ✓

"and let $P$ be the second intersection of $AA'$ with the parabola through $ABCT$."

The parabola passing through $A$, $B$, $C$, $T$. $P$ is the second intersection of line $AA'$ with this parabola (the first being $A$). ✓

"Let $D$ be the point on $(ABC)$ such that $AD \perp BC$"

$D$ is on the circumcircle with $AD \perp BC$. ✓

"and let $Q = PD \cap BC$."

$Q$ is the intersection of line $PD$ with line $BC$. ✓

"Let $R$ be the intersection of $AD$ with the tangent to $(ADC)$ at $A'$."

$R$ is the intersection of line $AD$ with the tangent to circle $(ADC)$ at $A'$. Since $(ADC) = (ABC)$, this is the tangent to the circumcircle at $A'$. ✓

"If $M$ is the midpoint of $BC$, calculate the ratio $\frac{QR}{AM}$."

Hmm, but my two examples give different ratios. Let me double-check the second example more carefully.

Actually, wait. Let me recheck the second example. $a = 1$, $d = 0.5$, $h = 2$.

$k = \frac{d^2 + h^2 - a^2}{2h} = \frac{0.25 + 4 - 1}{4} = \frac{3.25}{4} = 0.8125 = 13/16$. ✓

$A' = (-d, 2k - h) = (-0.5, 13/8 - 2) = (-0.5, -3/8)$. ✓

$D = (d, 2k - h) = (0.5, -3/8)$. ✓

Parabola: $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0 \Rightarrow x^2 + \frac{1 - 0.25}{2} y - 1 = 0 \Rightarrow x^2 + \frac{3}{8} y - 1 = 0$. ✓

Line $AA'$: $A = (0.5, 2)$, $A' = (-0.5, -3/8)$. Direction: $(-1, -3/8 - 2) = (-1, -19/8)$. Parametrize: $(0.5 - t, 2 - 19t/8)$. ✓

Substitute into parabola:
$(0.5 - t)^2 + \frac{3}{8}(2 - 19t/8) - 1 = 0$
$0.25 - t + t^2 + 3/4 - 57t/64 - 1 = 0$
$t^2 - t - 57t/64 + 0 = 0$
$t^2 - (64 + 57)t/64 = 0$
$t^2 - 121t/64 = 0$
$t(t - 121/64) = 0$ ✓

$P = (0.5 - 121/64, 2 - 19/8 \cdot 121/64) = (32/64 - 121/64, 2 - 2299/512)$
$= (-89/64, 1024/512 - 2299/512) = (-89/64, -1275/512)$ ✓

$D = (1/2, -3/8) = (32/64, -192/512)$.

Direction $PD$: $(32/64 - (-89/64), -192/512 - (-1275/512)) = (121/64, 1083/512)$.

$Q$: $y = 0$. $-1275/512 + s \cdot 1083/512 = 0 \Rightarrow s = 1275/1083$.

$\gcd(1275, 1083)$: $1275 = 1 \cdot 1083 + 192$. $1083 = 5 \cdot 192 + 123$. $192 = 1 \cdot 123 + 69$. $123 = 1 \cdot 69 + 54$. $69 = 1 \cdot 54 + 15$. $54 = 3 \cdot 15 + 9$. $15 = 1 \cdot 9 + 6$. $9 = 1 \cdot 6 + 3$. $6 = 2 \cdot 3$. $\gcd = 3$.

$s = 425/361$. ✓

$x_Q = -89/64 + (425/361)(121/64) = (-89 \cdot 361 + 425 \cdot 121)/(64 \cdot 361)$.

$-89 \cdot 361 = -32129$. $425 \cdot 121 = 51425$. $-32129 + 51425 = 19296$.

$x_Q = 19296/(64 \cdot 361) = 19296/23104 = 603/722$. ✓

$R$: tangent at $A' = (-1/2, -3/8)$ to circumcircle $x^2 + (y - 13/16)^2 = 425/256$.

At $A'$: $\nabla = (2x, 2(y - 13/16)) = (-1, 2(-3/8 - 13/16)) = (-1, 2(-6/16 - 13/16)) = (-1, -38/16) = (-1, -19/8)$.

Tangent: $-1(x + 1/2) + (-19/8)(y + 3/8) = 0$, i.e., $(x + 1/2) + (19/8)(y + 3/8) = 0$.

$AD$: $x = 1/2$. $(1/2 + 1/2) + (19/8)(y + 3/8) = 0 \Rightarrow 1 + (19/8)(y + 3/8) = 0 \Rightarrow y + 3/8 = -8/19 \Rightarrow y = -8/19 - 3/8 = (-64 - 57)/152 = -121/152$. ✓

$R = (1/2, -121/152)$.

$QR^2 = (603/722 - 1/2)^2 + (0 - (-121/152))^2 = (603/722 - 361/722)^2 + (121/152)^2 = (242/722)^2 + (121/152)^2$.

$242/722 = 121/361$. $121/152 = 121/152$.

$QR^2 = 121^2/361^2 + 121^2/152^2 = 121^2(1/361^2 + 1/152^2)$.

$361 = 19^2$, $152 = 8 \cdot 19$. $361^2 = 19^4 = 130321$. $152^2 = 64 \cdot 361 = 23104$.

$1/130321 + 1/23104 = (23104 + 130321)/(130321 \cdot 23104) = 153425/(130321 \cdot 23104)$.

Hmm, $153425 = 5^2 \cdot 61 \cdot 101$? Let me check: $153425 / 25 = 6137$. $6137 / 7 = 876.7$. $6137 / 11 = 557.9$. $6137 / 13 = 472.1$. $6137 / 17 = 361$. So $6137 = 17 \cdot 361 = 17 \cdot 19^2$. So $153425 = 25 \cdot 17 \cdot 19^2 = 5^2 \cdot 17 \cdot 19^2$.

$130321 \cdot 23104 = 19^4 \cdot 64 \cdot 19^2 = 64 \cdot 19^6$.

$QR^2 = 121^2 \cdot 5^2 \cdot 17 \cdot 19^2 / (64 \cdot 19^6) = 121^2 \cdot 25 \cdot 17 / (64 \cdot 19^4)$.

$QR = 121 \cdot 5 \sqrt{17} / (8 \cdot 19^2) = 605\sqrt{17}/(8 \cdot 361) = 605\sqrt{17}/2888$. ✓

$AM = \sqrt{(1/2)^2 + 2^2} = \sqrt{1/4 + 4} = \sqrt{17/4} = \sqrt{17}/2$.

$QR/AM = (605\sqrt{17}/2888) / (\sqrt{17}/2) = 605 \cdot 2 / 2888 = 1210/2888 = 605/1444$.

$605/1444 = 5 \cdot 121 / (4 \cdot 361) = 5 \cdot 11^2 / (4 \cdot 19^2) = 5(11/38)^2$.

For the first example: $QR/AM = 8\sqrt{10}/(9\sqrt{17})$.

Let me compute $8\sqrt{10}/(9\sqrt{17})$ more carefully. $= \frac{8}{9}\sqrt{\frac{10}{17}}$. Numerically: $\sqrt{10/17} = \sqrt{0.588} = 0.767$. $8/9 \cdot 0.767 = 0.682$.

Second example: $605/1444 = 0.419$.

These are definitely different. So either the ratio is not constant (and the problem is asking for something else), or I have a misunderstanding.

Wait, let me reconsider. Maybe the problem is asking for a ratio that is always 2, or some constant, and I'm making a computational error. Let me very carefully redo the first example.

First example: $B = (-3, 0)$, $C = (3, 0)$, $A = (1, 4)$.

$a = 3$, $d = 1$, $h = 4$.

$k = (1 + 16 - 9)/8 = 8/8 = 1$. $O = (0, 1)$. $R_c = \sqrt{10}$.

$A' = (-1, 2 - 4) = (-1, -2)$. $D = (1, -2)$.

Parabola: $x^2 + (9-1)/4 \cdot y - 9 = 0 \Rightarrow x^2 + 2y - 9 = 0$.

Line $AA'$: $(1, 4) + t(-2, -6) = (1-2t, 4-6t)$. Or equivalently $(1-t', 4-3t')$ with $t' = 2t$... let me use the parametrization $(1-2t, 4-6t)$ where $t=0$ gives $A$ and $t=1$ gives $A'$.

Substitute: $(1-2t)^2 + 2(4-6t) - 9 = 0$
$1 - 4t + 4t^2 + 8 - 12t - 9 = 0$
$4t^2 - 16t = 0$
$4t(t - 4) = 0$
$t = 0$ or $t = 4$.

$P = (1 - 8, 4 - 24) = (-7, -20)$. ✓

$D = (1, -2)$. Line $PD$: from $(-7, -20)$ to $(1, -2)$. Direction $(8, 18)$. Parametrize: $(-7 + 8s, -20 + 18s)$.

$Q$: $y = 0 \Rightarrow -20 + 18s = 0 \Rightarrow s = 20/18 = 10/9$.
$x_Q = -7 + 80/9 = -63/9 + 80/9 = 17/9$. ✓

$R$: tangent at $A' = (-1, -2)$ to $x^2 + (y-1)^2 = 10$.

Gradient at $A'$: $(2(-1), 2(-2-1)) = (-2, -6)$. Tangent: $-2(x+1) - 6(y+2) = 0 \Rightarrow x + 1 + 3(y+2) = 0 \Rightarrow x + 3y + 7 = 0$.

$AD$: $x = 1$. $1 + 3y + 7 = 0 \Rightarrow y = -8/3$. $R = (1, -8/3)$. ✓

$QR^2 = (17/9 - 1)^2 + (0 + 8/3)^2 = (8/9)^2 + (8/3)^2 = 64/81 + 64/9 = 64/81 + 576/81 = 640/81$.

$QR = 8\sqrt{10}/9$.

$AM = \sqrt{1 + 16} = \sqrt{17}$.

$QR/AM = 8\sqrt{10}/(9\sqrt{17})$.

Numerically: $8 \cdot 3.1623 / (9 \cdot 4.1231) = 25.298 / 37.108 = 0.6817$.

Second example: $605/1444 = 0.4190$.

These are different. So the ratio depends on the triangle. That's strange for a problem that says "calculate the ratio."

Hmm, let me reconsider the problem statement. Maybe I'm wrong about the parabola. Let me re-read: "the parabola through $ABCT$." Four points determine a conic, and there's a unique parabola through four points (in general position). But wait—do four points always determine a unique parabola? A general conic has 5 degrees of freedom. A parabola has 4 (the parabola constraint removes one). So 4 points determine a unique parabola (generically). ✓

But wait, I assumed the parabola is symmetric about the y-axis because $A, T$ and $B, C$ are symmetric pairs. Is that necessarily the case? The four points $A, B, C, T$ are symmetric about the y-axis as a set, but the unique parabola through them must also be symmetric. Actually, if we reflect the parabola through the y-axis, we get another parabola through the same four points (since the set is symmetric). By uniqueness, it must be the same parabola. So yes, the parabola is symmetric about the y-axis. ✓

So my computation should be correct. But the ratio isn't constant...

Let me reconsider. Maybe I'm misunderstanding "$A$-antipode." In some contexts, the $A$-antipode might not mean the diametrically opposite point, but rather the point where the $A$-altitude meets the circumcircle again, or the reflection of the orthocenter... Let me think.

Actually, "antipode" typically means the diametrically opposite point. The "$A$-antipode" is the point on the circumcircle diametrically opposite to $A$. That's what I used.

Hmm, but wait. Let me reconsider whether $(ADC)$ might not be the circumcircle. If $D$ is defined differently...

"Let $D$ be the point on $(ABC)$ such that $AD \perp BC$."

$D$ is on the circumcircle, $AD \perp BC$. Since $BC$ is the x-axis, $AD$ is vertical, so $D$ has the same x-coordinate as $A$. There are two intersections of the vertical line through $A$ with the circumcircle: $A$ itself and $D$. So $D$ is the other intersection. ✓

And $(ADC)$ is the circumcircle of $A$, $D$, $C$, which is the same as $(ABC)$. ✓

So the tangent at $A'$ is to the circumcircle. ✓

Let me try a third example to see if there's a pattern.

$B = (-5, 0)$, $C = (5, 0)$, $A = (3, 6)$. $a = 5$, $d = 3$, $h = 6$.

Check acute: $AB^2 = 4 + 36 = 40$, $AC^2 = 4 + 36 = 40$, $BC^2 = 100$. $AB^2 + AC^2 = 80 < 100$. Not acute! The angle at $A$ is obtuse.

Let me try $A = (3, 8)$. $AB^2 = 4 + 64 = 68$, $AC^2 = 4 + 64 = 68$, $BC^2 = 100$. $68 + 68 = 136 > 100$ ✓. $68 + 100 > 68$ ✓. Acute (isosceles).

$a = 5$, $d = 3$, $h = 8$.

$k = (9 + 64 - 25)/16 = 48/16 = 3$. $O = (0, 3)$. $R_c = \sqrt{25 + 9} = \sqrt{34}$.

$A' = (-3, 6 - 8) = (-3, -2)$. $D = (3, -2)$.

Parabola: $x^2 + (25-9)/8 \cdot y - 25 = 0 \Rightarrow x^2 + 2y - 25 = 0$.

Line $AA'$: $(3, 8) + t(-6, -10) = (3-6t, 8-10t)$. $t=0$: $A$, $t=1$: $A'$.

Substitute: $(3-6t)^2 + 2(8-10t) - 25 = 0$
$9 - 36t + 36t^2 + 16 - 20t - 25 = 0$
$36t^2 - 56t = 0$
$4t(9t - 14) = 0$
$t = 0$ or $t = 14/9$.

$P = (3 - 6 \cdot 14/9, 8 - 10 \cdot 14/9) = (3 - 84/9, 8 - 140/9) = (27/9 - 84/9, 72/9 - 140/9) = (-57/9, -68/9) = (-19/3, -68/9)$.

$D = (3, -2)$. Line $PD$: from $(-19/3, -68/9)$ to $(3, -2) = (27/9, -18/9)$.

Direction: $(27/9 + 57/9, -18/9 + 68/9) = (84/9, 50/9) = (84, 50)/9$. Simplify: $(42, 25)/4.5$... let me use $(84, 50)$, i.e., $(42, 25)$.

$Q$: $y = 0$. $-68/9 + s \cdot 50/9 = 0 \Rightarrow s = 68/50 = 34/25$.

$x_Q = -19/3 + (34/25) \cdot (84/9) = -19/3 + 34 \cdot 84/(25 \cdot 9) = -19/3 + 2856/225 = -19/3 + 952/75$.

$-19/3 = -475/75$. $x_Q = -475/75 + 952/75 = 477/75 = 159/25$.

$R$: tangent at $A' = (-3, -2)$ to $x^2 + (y-3)^2 = 34$.

Gradient: $(2(-3), 2(-2-3)) = (-6, -10)$. Tangent: $-6(x+3) - 10(y+2) = 0 \Rightarrow 6(x+3) + 10(y+2) = 0 \Rightarrow 6x + 18 + 10y + 20 = 0 \Rightarrow 6x + 10y + 38 = 0 \Rightarrow 3x + 5y + 19 = 0$.

$AD$: $x = 3$. $9 + 5y + 19 = 0 \Rightarrow y = -28/5$. $R = (3, -28/5)$.

$QR^2 = (159/25 - 3)^2 + (28/5)^2 = (159/25 - 75/25)^2 + (28/5)^2 = (84/25)^2 + (28/5)^2$.

$= 7056/625 + 784/25 = 7056/625 + 19600/625 = 26656/625$.

$QR = \sqrt{26656}/25$. $26656 = 16 \cdot 1666 = 16 \cdot 2 \cdot 833 = 32 \cdot 833$. $833 = 7 \cdot 119 = 7 \cdot 7 \cdot 17 = 49 \cdot 17$. So $26656 = 32 \cdot 49 \cdot 17 = 16 \cdot 2 \cdot 49 \cdot 17$. $\sqrt{26656} = 4 \cdot 7 \sqrt{2 \cdot 17} = 28\sqrt{34}$.

$QR = 28\sqrt{34}/25$.

$AM = \sqrt{9 + 64} = \sqrt{73}$.

$QR/AM = 28\sqrt{34}/(25\sqrt{73})$.

Numerically: $28 \cdot 5.831 / (25 \cdot 8.544) = 163.27 / 213.6 = 0.7644$.

So the three ratios are:
- Example 1: $0.6817$
- Example 2: $0.4190$
- Example 3: $0.7644$

These are all different. The ratio is definitely not constant. So I must be misunderstanding the problem.

Let me re-read the problem once more...

"Let $R$ be the intersection of $AD$ with the tangent to $(ADC)$ at $A'$."

Hmm, what if $(ADC)$ is not the circumcircle of triangle $ADC$? What if it's a different circle? In some competition notations, $(XYZ)$ always means the circumcircle of triangle $XYZ$. But since $A$, $D$, $C$ are on the circumcircle of $ABC$, $(ADC) = (ABC)$.

Unless... $D$ is not on the circumcircle? Let me re-read: "Let $D$ be the point on $(ABC)$ such that $AD \perp BC$." No, $D$ is on $(ABC)$.

Wait, maybe the problem means something different by "$A$-antipode." Let me consider the possibility that $A'$ is the reflection of $A$ over $BC$, or the foot of the altitude, or the midpoint of arc $BC$...

Actually, in many geometry problems, the "$A$-antipode" refers to the point on the circumcircle diametrically opposite to $A$. That's the standard meaning. Let me stick with that.

Hmm, but what if the problem means the tangent to $(ADC)$ at $A'$ where $(ADC)$ is NOT the circumcircle but some other circle? That doesn't make sense with standard notation.

Wait, I just realized something. What if $A'$ is NOT on the circumcircle $(ADC) = (ABC)$? Let me check: $A'$ is the antipode of $A$ on $(ABC)$, so $A'$ is on $(ABC) = (ADC)$. So the tangent at $A'$ to $(ADC)$ is well-defined. ✓

Let me reconsider the problem. Maybe the issue is with the parabola. Let me re-examine.

Actually, wait. I just realized: maybe the problem is using "parabola" in a more general sense, or maybe there's a specific parabola associated with $ABCT$ that I'm not considering. But a parabola through 4 points is unique (generically), so that should be fine.

Let me reconsider: is the answer perhaps supposed to be 2, and I'm making a systematic error? Let me check if maybe $R$ is defined differently.

Actually, let me reconsider the problem. Maybe "the tangent to $(ADC)$ at $A'$" means the tangent to the circle $(ADC)$ at the point $A'$, but $A'$ might not be on $(ADC)$. If $A'$ is not on $(ADC)$, then the tangent from $A'$ to $(ADC)$ would be a different thing (tangent lines from an external point). But $A'$ IS on $(ABC) = (ADC)$, so this doesn't apply.

Hmm, let me try a completely different interpretation. What if $(ADC)$ is not the circumcircle of $ADC$ but rather some other circle? For instance, what if the problem means the circle with diameter $AD$ passing through $C$? No, that's non-standard.

Or what if the problem has a typo and it should be "the tangent to $(ABC)$ at $D$" or "at $A$"? Let me try "tangent to $(ABC)$ at $D$".

For example 1: $D = (1, -2)$. Tangent at $D$ to $x^2 + (y-1)^2 = 10$: gradient at $D$ is $(2, -6)$. Tangent: $2(x-1) - 6(y+2) = 0 \Rightarrow x - 1 - 3(y+2) = 0 \Rightarrow x - 3y - 7 = 0$.

$AD$: $x = 1$. $1 - 3y - 7 = 0 \Rightarrow y = -2$. So $R = (1, -2) = D$. That gives $QR = QD$, which is just the distance from $Q$ to $D$. $QD = \sqrt{(17/9 - 1)^2 + 4} = \sqrt{64/81 + 4} = \sqrt{64/81 + 324/81} = \sqrt{388/81} = 2\sqrt{97}/9$. $QR/AM = 2\sqrt{97}/(9\sqrt{17})$. Not clean either.

Let me try "tangent to $(ABC)$ at $A$."

Tangent at $A = (1, 4)$: gradient $(2, 6)$. Tangent: $2(x-1) + 6(y-4) = 0 \Rightarrow x - 1 + 3(y-4) = 0 \Rightarrow x + 3y - 13 = 0$.

$AD$: $x = 1$. $1 + 3y - 13 = 0 \Rightarrow y = 4$. So $R = (1, 4) = A$. $QR = QA$. Not useful.

OK so those alternatives don't work either. Let me go back to the original interpretation.

Actually, let me reconsider. Maybe I should look at this more carefully. Perhaps the answer IS supposed to be 2 and I'm making an error somewhere. Let me try to derive the general formula.

Let me use the general setup: $B = (-a, 0)$, $C = (a, 0)$, $A = (d, h)$, $M = (0, 0)$.

$k = \frac{d^2 + h^2 - a^2}{2h}$, $O = (0, k)$.

$A' = (-d, 2k - h)$, $D = (d, 2k - h)$.

Let me denote $e = 2k - h = \frac{d^2 + h^2 - a^2}{h} - h = \frac{d^2 - a^2}{h}$.

So $A' = (-d, e)$, $D = (d, e)$ where $e = \frac{d^2 - a^2}{h}$.

Note: $e = (d^2 - a^2)/h$. Since the triangle is acute and $|d| < a$ (for the foot of altitude to be on $BC$), we have $d^2 < a^2$, so $e < 0$. This makes sense—$D$ is below $BC$.

Parabola: $x^2 + \frac{a^2 - d^2}{h} y - a^2 = 0$. Note $\frac{a^2 - d^2}{h} = -e$. So the parabola is $x^2 - ey - a^2 = 0$, or $x^2 = a^2 + ey$.

Line $AA'$: from $(d, h)$ to $(-d, e)$. Direction $(-2d, e - h)$. Parametrize: $(d - 2dt, h + (e-h)t) = (d(1-2t), h + (e-h)t)$.

$t = 0$: $A$. $t = 1$: $(-d, e) = A'$. ✓

Substitute into parabola $x^2 - ey - a^2 = 0$:
$d^2(1-2t)^2 - e(h + (e-h)t) - a^2 = 0$
$d^2(1 - 4t + 4t^2) - eh - e(e-h)t - a^2 = 0$
$d^2 - 4d^2 t + 4d^2 t^2 - eh - e(e-h)t - a^2 = 0$

Now, $d^2 - eh - a^2 = d^2 - a^2 - eh$. And $e = (d^2 - a^2)/h$, so $eh = d^2 - a^2$. Thus $d^2 - eh - a^2 = d^2 - (d^2 - a^2) - a^2 = 0$. ✓ (This confirms $A$ is on the parabola.)

So: $4d^2 t^2 - 4d^2 t - e(e-h)t = 0$
$t(4d^2 t - 4d^2 - e(e-h)) = 0$
$t = 0$ or $t = \frac{4d^2 + e(e-h)}{4d^2}$.

$e(e-h) = e \cdot e - eh = e^2 - (d^2 - a^2) = \frac{(d^2 - a^2)^2}{h^2} - (d^2 - a^2) = (d^2 - a^2)\left(\frac{d^2 - a^2}{h^2} - 1\right) = (d^2 - a^2) \cdot \frac{d^2 - a^2 - h^2}{h^2}$.

So $t_P = \frac{4d^2 + (d^2 - a^2)(d^2 - a^2 - h^2)/h^2}{4d^2} = 1 + \frac{(d^2 - a^2)(d^2 - a^2 - h^2)}{4d^2 h^2}$.

Let me denote $\Delta = d^2 - a^2$ (which is negative for acute triangles with the foot on $BC$). Then $e = \Delta/h$.

$t_P = 1 + \frac{\Delta(\Delta - h^2)}{4d^2 h^2}$.

$P = (d(1 - 2t_P), h + (e - h)t_P)$.

$1 - 2t_P = 1 - 2 - \frac{2\Delta(\Delta - h^2)}{4d^2 h^2} = -1 - \frac{\Delta(\Delta - h^2)}{2d^2 h^2}$.

$P_x = d\left(-1 - \frac{\Delta(\Delta - h^2)}{2d^2 h^2}\right) = -d - \frac{\Delta(\Delta - h^2)}{2dh^2}$.

$e - h = \Delta/h - h = (\Delta - h^2)/h$.

$P_y = h + \frac{\Delta - h^2}{h} \cdot t_P = h + \frac{(\Delta - h^2)}{h}\left(1 + \frac{\Delta(\Delta - h^2)}{4d^2 h^2}\right)$

$= h + \frac{\Delta - h^2}{h} + \frac{\Delta(\Delta - h^2)^2}{4d^2 h^3}$

$= \frac{h^2 + \Delta - h^2}{h} + \frac{\Delta(\Delta - h^2)^2}{4d^2 h^3}$

$= \frac{\Delta}{h} + \frac{\Delta(\Delta - h^2)^2}{4d^2 h^3}$

$= \frac{\Delta}{h}\left(1 + \frac{(\Delta - h^2)^2}{4d^2 h^2}\right)$

$= e\left(1 + \frac{(\Delta - h^2)^2}{4d^2 h^2}\right)$

This is getting complicated. Let me try a different approach. Let me use the formula for $Q$ and $R$ in terms of the general parameters and see if $QR/AM$ simplifies.

Actually, let me try to compute symbolically using the substitution $u = d/a$, $v = h/a$ (normalize $a = 1$). Then the ratio should be a function of $u$ and $v$ if it's not constant.

From my examples:
- Example 1: $a=3, d=1, h=4 \Rightarrow u=1/3, v=4/3$. Ratio $= 8\sqrt{10}/(9\sqrt{17})$.
- Example 2: $a=1, d=0.5, h=2 \Rightarrow u=0.5, v=2$. Ratio $= 605/1444$.
- Example 3: $a=5, d=3, h=8 \Rightarrow u=0.6, v=1.6$. Ratio $= 28\sqrt{34}/(25\sqrt{73})$.

These are all different, confirming the ratio is not constant.

Hmm, but the problem says "calculate the ratio $\frac{QR}{AM}$". This strongly suggests the answer is a constant. Let me reconsider whether I'm misunderstanding the problem.

Oh wait—maybe I need to reconsider what "the tangent to $(ADC)$ at $A'$" means. What if $A'$ is NOT on the circle $(ADC)$? Let me think again...

$A'$ is the antipode of $A$ on $(ABC)$. $D$ is on $(ABC)$ with $AD \perp BC$. $C$ is on $(ABC)$. So $A$, $D$, $C$ are all on $(ABC)$, and $(ADC) = (ABC)$. $A'$ is also on $(ABC)$. So $A'$ is on $(ADC)$, and the tangent at $A'$ is well-defined.

Unless the problem means something different by "$A$-antipode." Let me consider: in some sources, the "$A$-antipode" might refer to the antipode of $A$ with respect to the nine-point circle, or the reflection of $H$ (orthocenter) over $BC$, or the point where the $A$-symmedian meets the circumcircle...

Actually, in many competition geometry contexts, the "$A$-antipode" is simply the point diametrically opposite $A$ on the circumcircle. I'll stick with this.

Let me try yet another interpretation: maybe "the tangent to $(ADC)$ at $A'$" means the tangent from $A'$ to the circle $(ADC)$, but since $A'$ is on the circle, this is just the tangent at $A'$. Same thing.

Hmm, let me try a completely different approach. What if the problem is correct and the answer is indeed a constant, but I'm making an error in the parabola? Let me reconsider.

Wait, actually, I want to double-check that four points determine a unique parabola. A conic is $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ with 5 degrees of freedom (up to scaling). A parabola requires $B^2 - 4AC = 0$, which is one constraint, leaving 4 degrees of freedom. Four points give 4 equations, so generically a unique parabola. ✓

But what if the four points $A, B, C, T$ are in a special position where there's no parabola or infinitely many? In my examples, I found a unique parabola, so that's fine.

Let me try to see if maybe the problem intends $P$ to be the second intersection of $AA'$ with the parabola, where "second" means the one other than $A'$ (not other than $A$). But $A'$ is generally not on the parabola. Let me check: is $A'$ on the parabola?

Parabola: $x^2 - ey - a^2 = 0$ where $e = (d^2 - a^2)/h$.

$A' = (-d, e)$. $d^2 - e \cdot e - a^2 = d^2 - e^2 - a^2 = d^2 - a^2 - (d^2 - a^2)^2/h^2 = (d^2 - a^2)(1 - (d^2 - a^2)/h^2) = (d^2 - a^2)(h^2 - d^2 + a^2)/h^2$.

This is zero only if $d^2 = a^2$ (degenerate) or $h^2 = d^2 - a^2$ (which would make $k = 0$, meaning $O$ is on $BC$). So in general, $A'$ is NOT on the parabola, and "second intersection" means the one other than $A$. ✓

OK, I'm stuck on why the ratio isn't constant. Let me try to approach this differently—maybe compute the general formula and see if it simplifies to a constant.

Let me use the general parametrization. $B = (-a, 0)$, $C = (a, 0)$, $A = (d, h)$, $M = (0, 0)$.

$e = (d^2 - a^2)/h$, $D = (d, e)$, $A' = (-d, e)$.

Parabola: $x^2 = a^2 + ey$, i.e., $x^2 - ey - a^2 = 0$.

Line $AA'$: $(d(1-2t), h + (e-h)t)$, $t = 0$ at $A$, $t = 1$ at $A'$.

$t_P = 1 + \frac{\Delta(\Delta - h^2)}{4d^2 h^2}$ where $\Delta = d^2 - a^2$.

Let me simplify. $\Delta - h^2 = d^2 - a^2 - h^2$. And $\Delta = d^2 - a^2$.

$t_P = 1 + \frac{(d^2 - a^2)(d^2 - a^2 - h^2)}{4d^2 h^2}$.

Let me denote $p = d^2 - a^2 - h^2$ and $\Delta = d^2 - a^2$. Then $t_P = 1 + \frac{\Delta \cdot p}{4d^2 h^2}$.

$P_x = d(1 - 2t_P) = d\left(-1 - \frac{\Delta p}{2d^2 h^2}\right) = -d - \frac{\Delta p}{2dh^2}$.

$P_y = h + (e-h)t_P = h + \frac{p}{h}\left(1 + \frac{\Delta p}{4d^2 h^2}\right) = h + \frac{p}{h} + \frac{\Delta p^2}{4d^2 h^3}$.

$= \frac{h^2 + p}{h} + \frac{\Delta p^2}{4d^2 h^3} = \frac{h^2 + d^2 - a^2 - h^2}{h} + \frac{\Delta p^2}{4d^2 h^3} = \frac{\Delta}{h} + \frac{\Delta p^2}{4d^2 h^3} = \frac{\Delta}{h}\left(1 + \frac{p^2}{4d^2 h^2}\right)$.

So $P = \left(-d - \frac{\Delta p}{2dh^2}, \frac{\Delta}{h}\left(1 + \frac{p^2}{4d^2 h^2}\right)\right)$.

$D = (d, e) = (d, \Delta/h)$.

Now, line $PD$. Direction from $P$ to $D$:

$\Delta x = d - P_x = d + d + \frac{\Delta p}{2dh^2} = 2d + \frac{\Delta p}{2dh^2} = \frac{4d^2 h^2 + \Delta p}{2dh^2}$.

$\Delta y = e - P_y = \frac{\Delta}{h} - \frac{\Delta}{h}\left(1 + \frac{p^2}{4d^2 h^2}\right) = -\frac{\Delta p^2}{4d^2 h^3}$.

So direction is $\left(\frac{4d^2 h^2 + \Delta p}{2dh^2}, -\frac{\Delta p^2}{4d^2 h^3}\right)$.

$Q$ is where $y = 0$ on line $PD$. Parametrize: $P + s \cdot \text{direction}$.

$y_Q = P_y + s \cdot \Delta y = 0 \Rightarrow s = -P_y / \Delta y = \frac{\Delta(1 + p^2/(4d^2 h^2))/h}{\Delta p^2/(4d^2 h^3)} = \frac{(1 + p^2/(4d^2 h^2)) \cdot 4d^2 h^3}{p^2 \cdot h} = \frac{4d^2 h^2(1 + p^2/(4d^2 h^2))}{p^2} = \frac{4d^2 h^2 + p^2}{p^2}$.

$x_Q = P_x + s \cdot \Delta x = -d - \frac{\Delta p}{2dh^2} + \frac{4d^2 h^2 + p^2}{p^2} \cdot \frac{4d^2 h^2 + \Delta p}{2dh^2}$.

This is getting very messy. Let me try a substitution to simplify. Let me set $a = 1$ (normalize) and use $d$ and $h$ as parameters.

Actually, let me try a slightly different approach. Let me use the specific coordinate system where the circumcircle is the unit circle, and use trigonometric parametrization.

Let the circumcircle be the unit circle. Let $A = e^{i\alpha}$, $B = e^{i\beta}$, $C = e^{i\gamma}$.

The antipode of $A$ is $A' = -e^{i\alpha} = e^{i(\alpha + \pi)}$.

$T$ is the reflection of $A$ in the perpendicular bisector of $BC$. The perpendicular bisector of $BC$ passes through the center $O$ and the midpoint of arc $BC$. In terms of angles, the perpendicular bisector of $BC$ is the line through $O$ in the direction of $e^{i(\beta+\gamma)/2}$ (the midpoint of the arc). Reflecting $A = e^{i\alpha}$ in this line gives $T = e^{i(\beta + \gamma - \alpha)}$.

$D$ is the point on the circumcircle with $AD \perp BC$. The direction of $BC$ is $e^{i\gamma} - e^{i\beta}$. $AD \perp BC$ means $D - A$ is perpendicular to $C - B$.

In complex numbers on the unit circle, the condition $AD \perp BC$ is $\frac{D - A}{\bar{D} - \bar{A}} = -\frac{C - B}{\bar{C} - \bar{B}}$. Since on the unit circle $\bar{z} = 1/z$, this becomes $\frac{D - A}{1/D - 1/A} = -\frac{C - B}{1/C - 1/B}$.

$\frac{D - A}{(A - D)/(AD)} = -\frac{C - B}{(B - C)/(BC)}$

$\frac{AD(D - A)}{A - D} = -\frac{BC(C - B)}{B - C}$

$-AD = BC$ (since $(D-A)/(A-D) = -1$ and $(C-B)/(B-C) = -1$)

$-AD = BC \Rightarrow AD = -BC$.

So $D = -BC/A$. On the unit circle, $D = -e^{i(\beta + \gamma - \alpha)} = -T$... wait, $T = e^{i(\beta + \gamma - \alpha)}$, so $D = -T = e^{i(\beta + \gamma - \alpha + \pi)}$.

Hmm interesting. So $D = -T$ (as complex numbers on the unit circle).

And $A' = -A$.

Now, the parabola through $A$, $B$, $C$, $T$. This is more complex to handle in this coordinate system.

Let me go back to the coordinate approach but try to be more systematic.

Let me use the coordinate system with $M$ at the origin, $BC$ along x-axis, and normalize $a = 1$ (so $B = (-1, 0)$, $C = (1, 0)$). Then $A = (d, h)$ with $|d| < 1$ and $h > 0$.

$e = d^2 - 1$ (divided by $h$... wait, $e = (d^2 - a^2)/h = (d^2 - 1)/h$).

Let me use $\delta = d^2 - 1$ (negative). Then $e = \delta/h$.

$D = (d, \delta/h)$, $A' = (-d, \delta/h)$.

Parabola: $x^2 - \frac{\delta}{h} y - 1 = 0$, i.e., $h x^2 - \delta y - h = 0$.

Line $AA'$: from $(d, h)$ to $(-d, \delta/h)$. Direction $(-2d, \delta/h - h) = (-2d, (\delta - h^2)/h)$.

Let $\phi = \delta - h^2 = d^2 - 1 - h^2$.

Parametrize: $(d(1-2t), h + \phi t/h)$.

Substitute into parabola: $h \cdot d^2(1-2t)^2 - \delta(h + \phi t/h) - h = 0$

$hd^2(1 - 4t + 4t^2) - \delta h - \delta \phi t/h - h = 0$

$hd^2 - 4hd^2 t + 4hd^2 t^2 - \delta h - \delta \phi t/h - h = 0$

Constant term: $hd^2 - \delta h - h = h(d^2 - \delta - 1) = h(d^2 - (d^2 - 1) - 1) = 0$. ✓

$4hd^2 t^2 - (4hd^2 + \delta\phi/h) t = 0$

$t(4hd^2 t - 4hd^2 - \delta\phi/h) = 0$

$t_P = \frac{4hd^2 + \delta\phi/h}{4hd^2} = 1 + \frac{\delta\phi}{4h^2 d^2}$.

$P_x = d(1 - 2t_P) = d\left(-1 - \frac{\delta\phi}{2h^2 d^2}\right) = -d - \frac{\delta\phi}{2h^2 d}$.

$P_y = h + \frac{\phi}{h} t_P = h + \frac{\phi}{h}\left(1 + \frac{\delta\phi}{4h^2 d^2}\right) = h + \frac{\phi}{h} + \frac{\delta\phi^2}{4h^3 d^2} = \frac{h^2 + \phi}{h} + \frac{\delta\phi^2}{4h^3 d^2}$.

$h^2 + \phi = h^2 + d^2 - 1 - h^2 = d^2 - 1 = \delta$.

$P_y = \frac{\delta}{h} + \frac{\delta\phi^2}{4h^3 d^2} = \frac{\delta}{h}\left(1 + \frac{\phi^2}{4h^2 d^2}\right) = \frac{\delta(4h^2 d^2 + \phi^2)}{4h^3 d^2}$.

$D = (d, \delta/h) = (d, \delta/h)$.

Direction $PD$:
$\Delta x = d - P_x = 2d + \frac{\delta\phi}{2h^2 d} = \frac{4h^2 d^2 + \delta\phi}{2h^2 d}$.

$\Delta y = \delta/h - P_y = \frac{\delta}{h} - \frac{\delta(4h^2 d^2 + \phi^2)}{4h^3 d^2} = \frac{\delta}{h}\left(1 - \frac{4h^2 d^2 + \phi^2}{4h^2 d^2}\right) = \frac{\delta}{h} \cdot \frac{-\phi^2}{4h^2 d^2} = \frac{-\delta\phi^2}{4h^3 d^2}$.

$Q$: $y = 0$. $s = -P_y / \Delta y = \frac{\delta(4h^2 d^2 + \phi^2)/(4h^3 d^2)}{\delta\phi^2/(4h^3 d^2)} = \frac{4h^2 d^2 + \phi^2}{\phi^2}$.

$x_Q = P_x + s \cdot \Delta x = -d - \frac{\delta\phi}{2h^2 d} + \frac{4h^2 d^2 + \phi^2}{\phi^2} \cdot \frac{4h^2 d^2 + \delta\phi}{2h^2 d}$.

Let me denote $\Sigma = 4h^2 d^2 + \phi^2$ and $\Gamma = 4h^2 d^2 + \delta\phi$.

$x_Q = -d - \frac{\delta\phi}{2h^2 d} + \frac{\Sigma \Gamma}{2h^2 d \phi^2}$.

$= \frac{-2h^2 d^2 - \delta\phi + \Sigma\Gamma/\phi^2}{2h^2 d}$... hmm, let me be more careful.

$= \frac{1}{2h^2 d}\left(-2h^2 d^2 - \delta\phi + \frac{\Sigma \Gamma}{\phi^2}\right)$

$= \frac{1}{2h^2 d \phi^2}\left(-2h^2 d^2 \phi^2 - \delta\phi^3 + \Sigma\Gamma\right)$

$\Sigma\Gamma = (4h^2 d^2 + \phi^2)(4h^2 d^2 + \delta\phi) = 16h^4 d^4 + 4h^2 d^2 \delta\phi + 4h^2 d^2 \phi^2 + \delta\phi^3$.

$-2h^2 d^2 \phi^2 - \delta\phi^3 + 16h^4 d^4 + 4h^2 d^2 \delta\phi + 4h^2 d^2 \phi^2 + \delta\phi^3$

$= 16h^4 d^4 + 4h^2 d^2 \delta\phi + 2h^2 d^2 \phi^2$

$= 2h^2 d^2(8h^2 d^2 + 2\delta\phi + \phi^2)$.

Now, $\phi = \delta - h^2 = d^2 - 1 - h^2$. $\delta = d^2 - 1$.

$2\delta\phi + \phi^2 = \phi(2\delta + \phi) = \phi(2\delta + \delta - h^2) = \phi(3\delta - h^2)$.

$8h^2 d^2 + 2\delta\phi + \phi^2 = 8h^2 d^2 + \phi(3\delta - h^2)$.

$\phi(3\delta - h^2) = (\delta - h^2)(3\delta - h^2) = 3\delta^2 - \delta h^2 - 3\delta h^2 + h^4 = 3\delta^2 - 4\delta h^2 + h^4$.

$8h^2 d^2 + 3\delta^2 - 4\delta h^2 + h^4$.

$\delta = d^2 - 1$, $\delta^2 = (d^2-1)^2 = d^4 - 2d^2 + 1$.

$= 8h^2 d^2 + 3d^4 - 6d^2 + 3 - 4(d^2-1)h^2 + h^4$

$= 8h^2 d^2 + 3d^4 - 6d^2 + 3 - 4d^2 h^2 + 4h^2 + h^4$

$= 4h^2 d^2 + 3d^4 - 6d^2 + 3 + 4h^2 + h^4$

$= 3d^4 + 4h^2 d^2 - 6d^2 + h^4 + 4h^2 + 3$

$= 3(d^4 - 2d^2 + 1) + 4h^2 d^2 + h^4 + 4h^2$

$= 3(d^2 - 1)^2 + 4h^2 d^2 + h^4 + 4h^2$

$= 3\delta^2 + 4h^2 d^2 + h^4 + 4h^2$

$= 3\delta^2 + h^2(4d^2 + h^2 + 4)$

$= 3\delta^2 + h^2(4(d^2 + 1) + h^2)$

Hmm, this doesn't simplify nicely. Let me try a different approach.

Actually, let me reconsider the problem. Maybe I should try to verify with a specific simple case where computations are easy.

Let me try an isosceles triangle where $d = 0$. But then $T = A$ and the parabola degenerates. So $d \neq 0$.

Let me try $B = (-1, 0)$, $C = (1, 0)$, $A = (d, h)$ with specific nice values.

Let me try $d = 1/2$, $h = \sqrt{3}/2$. Then $A = (1/2, \sqrt{3}/2)$, which is on the unit circle! So $a = 1$, and $A$ is on the circle of radius 1 centered at origin. But the circumcircle of $ABC$ is not the unit circle unless $B$ and $C$ are also on it. $B = (-1, 0)$ and $C = (1, 0)$ are on the unit circle. And $A = (1/2, \sqrt{3}/2)$ is on the unit circle. So the circumcircle is the unit circle, $O = (0, 0)$, $k = 0$.

Then $e = (d^2 - a^2)/h = (1/4 - 1)/(\sqrt{3}/2) = (-3/4)/(\sqrt{3}/2) = -3/(2\sqrt{3}) = -\sqrt{3}/2$.

$A' = (-1/2, -\sqrt{3}/2)$, $D = (1/2, -\sqrt{3}/2)$.

This is an equilateral triangle! $A = (1/2, \sqrt{3}/2)$, $B = (-1, 0)$, $C = (1, 0)$. $AB = AC = BC$... let me check. $AB = \sqrt{9/4 + 3/4} = \sqrt{3}$. $BC = 2$. Not equilateral. Actually $A$ is at angle $60°$ on the unit circle, $B$ at $180°$, $C$ at $0°$. So arc $BC$ (not containing $A$) is $180°$, arc $CA$ is $60°$, arc $AB$ is $120°$. The triangle has angles $A = 90°$, $B = 30°$, $C = 60°$. But the problem requires acute, and $A = 90°$ is not acute. Let me adjust.

Let me try $A$ at angle $80°$: $A = (\cos 80°, \sin 80°)$. Then $B = (-1, 0)$ (angle $180°$), $C = (1, 0)$ (angle $0°$). The triangle has angles: $A = (180° - 80°)/2 = 50°$... no, let me compute properly.

Arc $BC$ not containing $A$: from $C$ (0°) to $B$ (180°) going the other way (through 360°), which is 180°. So angle $A = 90°$. Hmm, that's because $B$ and $C$ are diametrically opposite. So any triangle with $B$ and $C$ diametrically opposite on the circumcircle has a right angle at $A$. Not acute.

So I can't have $B$ and $C$ diametrically opposite. Let me use a different setup.

Let me try the circumcircle as the unit circle with $B$ and $C$ not diametrically opposite.

Let $B = e^{i \cdot 200°}$, $C = e^{i \cdot 340°}$ (i.e., $-20°$), $A = e^{i \cdot 80°}$.

Actually, this is getting complicated. Let me go back to my coordinate system and just try to find the general formula for $QR/AM$ and see if it simplifies.

Let me use the normalized coordinates: $B = (-1, 0)$, $C = (1, 0)$, $A = (d, h)$, $M = (0, 0)$.

$\delta = d^2 - 1$, $\phi = d^2 - 1 - h^2 = \delta - h^2$.

$e = \delta/h$, $D = (d, \delta/h)$, $A' = (-d, \delta/h)$.

$R$: tangent to circumcircle at $A'$, intersected with $AD$ (which is $x = d$).

Circumcircle: $x^2 + (y - k)^2 = R_c^2$ where $k = \delta/(2h) + h/2 = (\delta + h^2)/(2h) = (d^2 - 1 + h^2)/(2h)$.

Wait, $k = (d^2 + h^2 - 1)/(2h)$. And $R_c^2 = 1 + k^2$.

Tangent at $A' = (-d, \delta/h)$: gradient $(2(-d), 2(\delta/h - k))$.

$\delta/h - k = \delta/h - (d^2 + h^2 - 1)/(2h) = (2\delta - d^2 - h^2 + 1)/(2h) = (2(d^2 - 1) - d^2 - h^2 + 1)/(2h) = (d^2 - 1 - h^2)/(2h) = \phi/(2h)$.

So gradient at $A'$ is $(-2d, \phi/h)$.

Tangent line: $-2d(x + d) + (\phi/h)(y - \delta/h) = 0$.

At $x = d$ (line $AD$): $-2d(2d) + (\phi/h)(y - \delta/h) = 0 \Rightarrow -4d^2 + (\phi/h)(y - \delta/h) = 0 \Rightarrow y - \delta/h = 4d^2 h/\phi \Rightarrow y = \delta/h + 4d^2 h/\phi$.

$R = (d, \delta/h + 4d^2 h/\phi)$.

Let me simplify: $y_R = \delta/h + 4d^2 h/\phi = \frac{\delta \phi + 4d^2 h^2}{h\phi}$.

Now, $\delta\phi + 4d^2 h^2 = \delta(\delta - h^2) + 4d^2 h^2 = \delta^2 - \delta h^2 + 4d^2 h^2 = (d^2-1)^2 - (d^2-1)h^2 + 4d^2 h^2$

$= d^4 - 2d^2 + 1 - d^2 h^2 + h^2 + 4d^2 h^2 = d^4 - 2d^2 + 1 + 3d^2 h^2 + h^2$

$= (d^2 - 1)^2 + h^2(3d^2 + 1) = \delta^2 + h^2(3d^2 + 1)$.

Hmm, also $= d^4 + 3d^2 h^2 + h^2 - 2d^2 + 1$. Not obviously simplifiable.

Let me denote $\Gamma = \delta\phi + 4d^2 h^2 = 4d^2 h^2 + \delta\phi$ (same as before).

$y_R = \Gamma/(h\phi)$.

Now I need $Q$. From the computation above:

$x_Q = \frac{2h^2 d^2(8h^2 d^2 + 2\delta\phi + \phi^2)}{2h^2 d \phi^2} = \frac{d(8h^2 d^2 + 2\delta\phi + \phi^2)}{\phi^2}$.

Wait, let me recompute. We had:

$x_Q = \frac{1}{2h^2 d \phi^2}\left(2h^2 d^2(8h^2 d^2 + 2\delta\phi + \phi^2)\right) = \frac{d(8h^2 d^2 + 2\delta\phi + \phi^2)}{\phi^2}$.

Let me denote $\Omega = 8h^2 d^2 + 2\delta\phi + \phi^2$.

$x_Q = d\Omega/\phi^2$.

$Q = (d\Omega/\phi^2, 0)$, $R = (d, \Gamma/(h\phi))$.

$QR^2 = (d\Omega/\phi^2 - d)^2 + (\Gamma/(h\phi))^2 = d^2(\Omega/\phi^2 - 1)^2 + \Gamma^2/(h^2\phi^2)$.

$= d^2((\Omega - \phi^2)/\phi^2)^2 + \Gamma^2/(h^2\phi^2)$

$= \frac{d^2(\Omega - \phi^2)^2}{\phi^4} + \frac{\Gamma^2}{h^2\phi^2}$

$= \frac{d^2 h^2 (\Omega - \phi^2)^2 + \Gamma^2 \phi^2}{h^2 \phi^4}$.

$\Omega - \phi^2 = 8h^2 d^2 + 2\delta\phi + \phi^2 - \phi^2 = 8h^2 d^2 + 2\delta\phi = 2(4h^2 d^2 + \delta\phi) = 2\Gamma$.

So $(\Omega - \phi^2)^2 = 4\Gamma^2$.

$QR^2 = \frac{d^2 h^2 \cdot 4\Gamma^2 + \Gamma^2 \phi^2}{h^2 \phi^4} = \frac{\Gamma^2(4d^2 h^2 + \phi^2)}{h^2 \phi^4}$.

$QR = \frac{|\Gamma| \sqrt{4d^2 h^2 + \phi^2}}{h \phi^2}$ (taking absolute values since distances are positive, and $\phi < 0$ for acute triangles, $\phi^2 > 0$).

$AM = \sqrt{d^2 + h^2}$.

$\frac{QR}{AM} = \frac{|\Gamma| \sqrt{4d^2 h^2 + \phi^2}}{h \phi^2 \sqrt{d^2 + h^2}}$.

Now, $\Gamma = 4d^2 h^2 + \delta\phi = 4d^2 h^2 + (d^2 - 1)(d^2 - 1 - h^2)$.

$4d^2 h^2 + \phi^2 = 4d^2 h^2 + (d^2 - 1 - h^2)^2$.

Note that $4d^2 h^2 + (d^2 - 1 - h^2)^2 = (2dh)^2 + (d^2 - 1 - h^2)^2$. This is of the form $a^2 + b^2$ where $a = 2dh$ and $b = d^2 - 1 - h^2$. And $a^2 + b^2 = (d^2 + h^2 - 1)^2 + 4h^2$... let me check:

$(d^2 + h^2 - 1)^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 - 2h^2$.

$4d^2 h^2 + (d^2 - 1 - h^2)^2 = 4d^2 h^2 + d^4 + 1 + h^4 - 2d^2 + 2h^2 - 2d^2 h^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 + 2h^2$.

$(d^2 + h^2 - 1)^2 + 4h^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 - 2h^2 + 4h^2 = d^4 + h^4 + 1 + 2d^2 h^2 - 2d^2 + 2h^2$.

Yes! So $4d^2 h^2 + \phi^2 = (d^2 + h^2 - 1)^2 + 4h^2$.

Hmm, that's a nice identity but doesn't immediately simplify the ratio.

Let me also compute $\Gamma$:

$\Gamma = 4d^2 h^2 + (d^2 - 1)(d^2 - 1 - h^2) = 4d^2 h^2 + (d^2-1)^2 - (d^2-1)h^2$

$= (d^2 - 1)^2 + h^2(4d^2 - d^2 + 1) = (d^2-1)^2 + h^2(3d^2 + 1)$.

$= d^4 - 2d^2 + 1 + 3d^2 h^2 + h^2$.

Hmm. Let me also note that $\phi = d^2 - 1 - h^2$, so $\phi^2 = (d^2 - 1 - h^2)^2$.

The ratio is:

$\frac{QR}{AM} = \frac{|\Gamma| \sqrt{(d^2 + h^2 - 1)^2 + 4h^2}}{h (d^2 - 1 - h^2)^2 \sqrt{d^2 + h^2}}$.

This is clearly not a constant—it depends on $d$ and $h$. So either the problem has a different interpretation, or I'm making an error.

Let me verify with example 1: $a = 3$, so I need to rescale. With $a = 1$: $d = 1/3$, $h = 4/3$.

$\delta = 1/9 - 1 = -8/9$. $\phi = -8/9 - 16/9 = -24/9 = -8/3$.

$\Gamma = 4 \cdot (1/9) \cdot (16/9) + (-8/9)(-8/3) = 64/81 + 64/27 = 64/81 + 192/81 = 256/81$.

$4d^2 h^2 + \phi^2 = 64/81 + 64/9 = 64/81 + 576/81 = 640/81$.

$QR = \
