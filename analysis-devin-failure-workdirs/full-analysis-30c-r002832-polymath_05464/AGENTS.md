# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   An acute triangle $ABC$ is given, $AC \not= BC$. The altitudes drawn from $A$ and $B$ meet at $H$ and intersect the external bisector of the angle $C$ at $Y$ and $X$ respectively. The external bisector of the angle $AHB$ meets the segments $AX$ and $BY$ at $P$ and $Q$ respectively. It is known that $PX = QY$. Let $k$ be the largest real number such that the inequality $AP + BQ \ge k \cdot CH$ always holds. Find the value of $k$.       — 题目文本
#   In the original problem, it is proven that for an acute triangle $ABC$ with $AC \neq BC$ and $PX = QY$, the relationship $AP + BQ \ge 2CH$ holds. The proof uses the fact that $XDEY$ (where $P, Q$ are $D, E$) is a parallelogram, leading to $AD \cdot BE = XD^2$ (or $AP \cdot BQ = PX^2$). It is also shown that $CH = PX$ by demonstrating that $CHPX$ is an isosceles trapezoid. Applying the AM-GM inequality, $AP + BQ \ge 2\sqrt{AP \cdot BQ} = 2PX = 2CH$. The equality occurs in the limit as the triangle approaches an isosceles configuration, meaning $k=2$ is the sharpest constant.  — 标准解答
#   Let me work through this problem carefully.

We have an acute triangle ABC with AC ≠ BC. Altitudes from A and B meet at H (orthocenter). The external bisector of angle C intersects the altitude from A at Y and the altitude from B at X. The external bisector of angle AHB meets segments AX and BY at P and Q respectively. Given PX = QY. Find the largest k such that AP + BQ ≥ k·CH always holds.

Let me set up coordinates. Let me think about this geometrically first.

The altitudes from A and B: altitude from A is perpendicular to BC, altitude from B is perpendicular to AC. They meet at H, the orthocenter.

The external bisector of angle C: this is the line through C that bisects the external angle at C.

The external bisector of angle AHB: angle AHB = π - C (since in a triangle, the orthocenter creates angle AHB = π - C). The external bisector of angle AHB bisects the external angle at H.

Let me use coordinates. Place C at the origin. Let the external bisector of angle C be a convenient axis.

Actually, let me think about the external bisector of angle C. The internal bisector of angle C bisects angle ACB. The external bisector is perpendicular to the internal bisector.

Let me set up coordinates with C at origin, and the external bisector of angle C along the x-axis. Then the internal bisector of angle C is along the y-axis.

Let angle C = 2γ. Then CA makes angle (π/2 - γ) with the x-axis... wait, let me think more carefully.

If the external bisector of C is the x-axis, then the two sides CA and CB are symmetric with respect to... no. The external bisector bisects the external angle. The internal bisector bisects the internal angle. They are perpendicular.

Let me place C at origin. Let the internal bisector of angle C point in the direction of angle 0 (positive x-axis), and the external bisector point in the direction π/2 (positive y-axis). Wait, let me just pick the external bisector as the x-axis for convenience since the problem involves the external bisector of C heavily.

Let the external bisector of angle C be the x-axis, with C at origin. Then the internal bisector of angle C is the y-axis.

Let angle C = 2γ (where 0 < γ < π/2 since triangle is acute, so C < π/2... wait, acute means all angles < π/2, so C < π/2, thus γ < π/4).

The sides CA and CB make angles with the internal bisector. CA makes angle γ with the internal bisector (y-axis), and CB makes angle -γ with the internal bisector. So relative to the x-axis (external bisector):
- CA direction: angle (π/2 - γ) from x-axis... 

Hmm, let me reconsider. If internal bisector is along positive y-axis, then CA is at angle (π/2 + γ) from positive x-axis and CB is at angle (π/2 - γ) from positive x-axis. Wait, that's not right either. Let me be more careful.

The internal bisector of angle C bisects the angle between CA and CB. If the internal bisector is the positive y-axis, then CA and CB are symmetric about the y-axis. CA is at angle (π/2 + γ) and CB is at angle (π/2 - γ) from the positive x-axis. So angle ACB = 2γ. Good.

The external bisector of angle C is perpendicular to the internal bisector, so it's the x-axis. Good.

Now, let's say CA = b and CB = a (standard notation: a = BC, b = CA, c = AB).

A is at distance b from C along direction (π/2 + γ):
A = (b cos(π/2 + γ), b sin(π/2 + γ)) = (-b sin γ, b cos γ)

B is at distance a from C along direction (π/2 - γ):
B = (a cos(π/2 - γ), a sin(π/2 - γ)) = (a sin γ, a cos γ)

C = (0, 0).

Now, the altitude from A is perpendicular to BC. Direction of BC: from B to C is (-a sin γ, -a cos γ), so BC direction is (sin γ, cos γ) (from C to B). The altitude from A is perpendicular to BC, so its direction is perpendicular to (sin γ, cos γ), which is (cos γ, -sin γ) or (-cos γ, sin γ).

The altitude from A passes through A = (-b sin γ, b cos γ) with direction (cos γ, -sin γ):
Parametrically: (-b sin γ + t cos γ, b cos γ - t sin γ)

Similarly, altitude from B is perpendicular to AC. Direction of AC: from C to A is (-b sin γ, b cos γ), so direction is (-sin γ, cos γ). Perpendicular direction: (cos γ, sin γ) or (-cos γ, -sin γ).

Altitude from B passes through B = (a sin γ, a cos γ) with direction (cos γ, sin γ):
Parametrically: (a sin γ + s cos γ, a cos γ + s sin γ)

Orthocenter H: intersection of the two altitudes.
From altitude A: (-b sin γ + t cos γ, b cos γ - t sin γ)
From altitude B: (a sin γ + s cos γ, a cos γ + s sin γ)

Setting equal:
-b sin γ + t cos γ = a sin γ + s cos γ ... (1)
b cos γ - t sin γ = a cos γ + s sin γ ... (2)

From (1): t cos γ - s cos γ = (a + b) sin γ → (t - s) cos γ = (a + b) sin γ → t - s = (a + b) tan γ

From (2): -t sin γ - s sin γ = (a - b) cos γ → -(t + s) sin γ = (a - b) cos γ → t + s = -(a - b) cos γ / sin γ = (b - a) / tan γ

So:
t = [(a+b) tan γ + (b-a)/tan γ] / 2
s = [(b-a)/tan γ - (a+b) tan γ] / 2

Let me compute H coordinates using altitude from A:
H_x = -b sin γ + t cos γ
H_y = b cos γ - t sin γ

t cos γ = [(a+b) tan γ + (b-a)/tan γ] cos γ / 2 = [(a+b) sin γ + (b-a) cos²γ/sin γ] / 2

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me use the known formula for the orthocenter. In a triangle with C at origin:
H = A + B - (projection stuff)... actually, let me just use the formula.

For a triangle with vertices A, B, C, the orthocenter H satisfies:
H = A + B + C - 2O where O is the circumcenter. That's not quite right.

Actually, let me just compute H directly. We know that in the coordinate system with C at origin:
The altitude from A is perpendicular to BC. BC has direction (a sin γ, a cos γ) - (0,0) = (sin γ, cos γ) (unit direction since a cancels). So altitude from A: point A + t(cos γ, -sin γ).

The altitude from B is perpendicular to AC. AC has direction (-b sin γ, b cos γ), unit direction (-sin γ, cos γ). So altitude from B: point B + s(cos γ, sin γ).

Let me find H by solving:
A + t(cos γ, -sin γ) = B + s(cos γ, sin γ)

(-b sin γ + t cos γ, b cos γ - t sin γ) = (a sin γ + s cos γ, a cos γ + s sin γ)

From x: t cos γ - s cos γ = (a + b) sin γ → t - s = (a+b) sin γ / cos γ = (a+b) tan γ
From y: -t sin γ - s sin γ = (a - b) cos γ → t + s = (b-a) cos γ / sin γ = (b-a)/tan γ

So t = [(a+b) tan γ + (b-a)/tan γ]/2, s = [(b-a)/tan γ - (a+b) tan γ]/2

H_x = -b sin γ + t cos γ = -b sin γ + [(a+b) sin γ + (b-a) cos²γ/sin γ]/2
= -b sin γ + (a+b) sin γ/2 + (b-a) cos²γ/(2 sin γ)
= sin γ[-b + (a+b)/2] + (b-a) cos²γ/(2 sin γ)
= sin γ[(a-b)/2] + (b-a) cos²γ/(2 sin γ)
= (a-b)/2 [sin γ - cos²γ/sin γ]
= (a-b)/2 [(sin²γ - cos²γ)/sin γ]
= (a-b)/2 [-cos(2γ)/sin γ]
= -(a-b) cos(2γ)/(2 sin γ)
= (b-a) cos(2γ)/(2 sin γ)

H_y = b cos γ - t sin γ = b cos γ - [(a+b) sin²γ/cos γ + (b-a) cos γ]/2... 

wait let me redo:
t sin γ = [(a+b) tan γ + (b-a)/tan γ] sin γ / 2 = [(a+b) sin²γ/cos γ + (b-a) cos γ] / 2

H_y = b cos γ - [(a+b) sin²γ/cos γ + (b-a) cos γ]/2
= b cos γ - (a+b) sin²γ/(2 cos γ) - (b-a) cos γ/2
= cos γ [b - (b-a)/2] - (a+b) sin²γ/(2 cos γ)
= cos γ [(2b - b + a)/2] - (a+b) sin²γ/(2 cos γ)
= cos γ (a+b)/2 - (a+b) sin²γ/(2 cos γ)
= (a+b)/2 [cos γ - sin²γ/cos γ]
= (a+b)/2 [(cos²γ - sin²γ)/cos γ]
= (a+b)/2 [cos(2γ)/cos γ]
= (a+b) cos(2γ)/(2 cos γ)

So H = ((b-a) cos(2γ)/(2 sin γ), (a+b) cos(2γ)/(2 cos γ))

Since the triangle is acute, the orthocenter is inside the triangle, so H_y > 0, which means cos(2γ) > 0, i.e., γ < π/4, i.e., C = 2γ < π/2. Good, consistent with acute triangle.

Now, CH = distance from C=(0,0) to H:
CH² = [(b-a) cos(2γ)/(2 sin γ)]² + [(a+b) cos(2γ)/(2 cos γ)]²
= cos²(2γ)/4 [(b-a)²/sin²γ + (a+b)²/cos²γ]
= cos²(2γ)/4 [(b-a)² cos²γ + (a+b)² sin²γ]/(sin²γ cos²γ)

Let me compute (b-a)² cos²γ + (a+b)² sin²γ:
= (b²-2ab+a²)cos²γ + (a²+2ab+b²)sin²γ
= a²(cos²γ+sin²γ) + b²(cos²γ+sin²γ) + 2ab(sin²γ - cos²γ)
= a² + b² - 2ab cos(2γ)

So CH² = cos²(2γ)(a² + b² - 2ab cos(2γ))/(4 sin²γ cos²γ)

Note that by the law of cosines, c² = a² + b² - 2ab cos(C) = a² + b² - 2ab cos(2γ). So:

CH² = cos²(2γ) c² / (4 sin²γ cos²γ) = c² cos²(2γ) / sin²(2γ) = c² / tan²(2γ) = c² cot²(C)

So CH = c cot(C) = c · cos(C)/sin(C). This is a known formula: CH = c cot C. Actually, let me verify: the distance from C to the orthocenter is indeed c·cot(C)... hmm, actually I recall the formula is CH = 2R cos C where R is the circumradius. And c = 2R sin C. So CH = 2R cos C = c cos C / sin C = c cot C. Yes, consistent!

Good. So CH = c cot C where C = 2γ.

Now let's find X and Y. The external bisector of angle C is the x-axis (y = 0).

X is the intersection of the altitude from B with the x-axis (external bisector of C).
Altitude from B: (a sin γ + s cos γ, a cos γ + s sin γ)
Set y = 0: a cos γ + s sin γ = 0 → s = -a cos γ / sin γ = -a / tan γ
X_x = a sin γ + s cos γ = a sin γ - a cos²γ / sin γ = a(sin²γ - cos²γ)/sin γ = -a cos(2γ)/sin γ
X = (-a cos(2γ)/sin γ, 0)

Y is the intersection of the altitude from A with the x-axis.
Altitude from A: (-b sin γ + t cos γ, b cos γ - t sin γ)
Set y = 0: b cos γ - t sin γ = 0 → t = b cos γ / sin γ = b / tan γ
Y_x = -b sin γ + t cos γ = -b sin γ + b cos²γ / sin γ = b(cos²γ - sin²γ)/sin γ = b cos(2γ)/sin γ
Y = (b cos(2γ)/sin γ, 0)

So X and Y are on the x-axis (external bisector of C), with:
X = (-a cos(2γ)/sin γ, 0)
Y = (b cos(2γ)/sin γ, 0)

XY = (a + b) cos(2γ)/sin γ (distance, since cos(2γ) > 0 for acute triangle).

Now, the external bisector of angle AHB. Angle AHB = π - C = π - 2γ. The external bisector of angle AHB bisects the external angle at H.

The external angle at H is 2γ (since internal angle is π - 2γ, external is 2γ). The external bisector bisects this into two angles of γ each.

Hmm, I need to find the direction of the external bisector of angle AHB. Let me think about this.

The angle AHB is the angle at H in triangle AHB. The sides HA and HB go from H to A and H to B respectively.

Direction from H to A: A - H = (-b sin γ, b cos γ) - ((b-a) cos(2γ)/(2 sin γ), (a+b) cos(2γ)/(2 cos γ))

This is getting complicated. Let me think of another approach.

Actually, the external bisector of angle AHB. Note that angle AHB = π - C. The internal bisector of angle AHB and the external bisector are perpendicular.

There's a nice property: the internal bisector of angle AHB passes through... hmm. Actually, in the orthocenter configuration, the bisectors of angle AHB have nice properties. The internal bisector of angle AHB is related to the bisector of angle C.

Let me think about this differently. The angle AHB = π - C. The internal bisector of angle AHB bisects the angle π - C, creating angles of (π-C)/2 = π/2 - C/2 = π/2 - γ. The external bisector is perpendicular to the internal bisector.

Actually, I recall that the internal bisector of angle AHB is parallel to the internal bisector of angle C (or the external bisector of angle C). Let me verify.

The altitude from A is perpendicular to BC, and the altitude from B is perpendicular to AC. The angle between the altitudes (which is angle AHB) equals π - C (since the angle between two lines perpendicular to two sides equals the supplement of the angle between those sides).

The internal bisector of angle AHB: since the altitudes are perpendicular to BC and AC respectively, the bisector of the angle between the altitudes is perpendicular to the bisector of the angle between BC and AC (which is angle C). Wait, not exactly.

If two lines L1, L2 meet at angle θ, and two other lines M1 ⊥ L1, M2 ⊥ L2 meet at angle π - θ, then the bisector of the angle between M1, M2 is perpendicular to the bisector of the angle between L1, L2. 

The altitudes from A and B are perpendicular to BC and AC respectively. The angle between BC and AC is C. The angle between the altitudes is π - C. The bisector of angle C (internal bisector of C) and the bisector of the angle between the altitudes (internal bisector of angle AHB) are perpendicular.

So: internal bisector of angle AHB ⊥ internal bisector of angle C.

Since the internal bisector of angle C is the y-axis (in our coordinates), the internal bisector of angle AHB is horizontal, i.e., parallel to the x-axis, which is the external bisector of angle C.

And the external bisector of angle AHB is perpendicular to the internal bisector of angle AHB, so it's vertical, i.e., parallel to the y-axis, which is the internal bisector of angle C.

So the external bisector of angle AHB is a vertical line (parallel to y-axis) passing through H.

The external bisector of angle AHB is the vertical line x = H_x = (b-a) cos(2γ)/(2 sin γ).

Now, P is the intersection of this vertical line with segment AX, and Q is the intersection with segment BY.

Let me find P on segment AX.
A = (-b sin γ, b cos γ)
X = (-a cos(2γ)/sin γ, 0)

Parametrize AX: A + u(X - A) for u ∈ [0, 1].
X - A = (-a cos(2γ)/sin γ + b sin γ, -b cos γ)

x-coordinate: -b sin γ + u(-a cos(2γ)/sin γ + b sin γ)
Set this equal to H_x = (b-a) cos(2γ)/(2 sin γ):

-b sin γ + u(-a cos(2γ)/sin γ + b sin γ) = (b-a) cos(2γ)/(2 sin γ)

Let me compute -a cos(2γ)/sin γ + b sin γ:
= [-a cos(2γ) + b sin²γ] / sin γ
= [-a(cos²γ - sin²γ) + b sin²γ] / sin γ
= [-a cos²γ + a sin²γ + b sin²γ] / sin γ
= [-a cos²γ + (a+b) sin²γ] / sin γ

So:
u · [-a cos²γ + (a+b) sin²γ] / sin γ = (b-a) cos(2γ)/(2 sin γ) + b sin γ
= [(b-a) cos(2γ) + 2b sin²γ] / (2 sin γ)
= [(b-a)(cos²γ - sin²γ) + 2b sin²γ] / (2 sin γ)
= [(b-a) cos²γ - (b-a) sin²γ + 2b sin²γ] / (2 sin γ)
= [(b-a) cos²γ + (a+b) sin²γ] / (2 sin γ)

So:
u = [(b-a) cos²γ + (a+b) sin²γ] / (2 [-a cos²γ + (a+b) sin²γ])

Hmm, this is getting messy. Let me denote for convenience:
Let p = cos²γ, q = sin²γ. Note p + q = 1, p - q = cos(2γ).

Then:
Numerator of u: (b-a)p + (a+b)q = bp - ap + aq + bq = b(p+q) + a(q-p) = b - a cos(2γ)
Denominator of u: 2[-ap + (a+b)q] = 2[-ap + aq + bq] = 2[a(q-p) + bq] = 2[-a cos(2γ) + bq]

So u = [b - a cos(2γ)] / [2(bq - a cos(2γ))] = [b - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]

Let me also compute the y-coordinate of P:
P_y = b cos γ + u(0 - b cos γ) = b cos γ (1 - u) = b cos γ · [1 - (b - a cos(2γ))/(2(b sin²γ - a cos(2γ)))]
= b cos γ · [2(b sin²γ - a cos(2γ)) - (b - a cos(2γ))] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [2b sin²γ - 2a cos(2γ) - b + a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [2b sin²γ - b - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [b(2 sin²γ - 1) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [-b cos(2γ) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [-(a+b) cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= -b(a+b) cos(2γ) cos γ / [2(b sin²γ - a cos(2γ))]

And P_x = H_x = (b-a) cos(2γ)/(2 sin γ).

Similarly, let me find Q on segment BY.
B = (a sin γ, a cos γ)
Y = (b cos(2γ)/sin γ, 0)

Parametrize BY: B + v(Y - B) for v ∈ [0, 1].
Y - B = (b cos(2γ)/sin γ - a sin γ, -a cos γ)

x-coordinate: a sin γ + v(b cos(2γ)/sin γ - a sin γ)
Set equal to H_x = (b-a) cos(2γ)/(2 sin γ):

a sin γ + v(b cos(2γ)/sin γ - a sin γ) = (b-a) cos(2γ)/(2 sin γ)

b cos(2γ)/sin γ - a sin γ = [b cos(2γ) - a sin²γ] / sin γ = [b(p-q) - aq] / sin γ = [bp - bq - aq] / sin γ = [bp - (a+b)q] / sin γ

So:
v · [bp - (a+b)q] / sin γ = (b-a)(p-q)/(2 sin γ) - a sin γ
= [(b-a)(p-q) - 2aq] / (2 sin γ)
= [(b-a)(p-q) - 2aq] / (2 sin γ)
= [bp - bq - ap + aq - 2aq] / (2 sin γ)
= [bp - bq - ap - aq] / (2 sin γ)
= [b(p-q) - a(p+q)] / (2 sin γ)
= [b cos(2γ) - a] / (2 sin γ)

So:
v = [b cos(2γ) - a] / [2(bp - (a+b)q)]
= [b cos(2γ) - a] / [2(b cos²γ - (a+b) sin²γ)]

Q_y = a cos γ + v(0 - a cos γ) = a cos γ (1 - v)
= a cos γ · [2(b cos²γ - (a+b) sin²γ) - (b cos(2γ) - a)] / [2(b cos²γ - (a+b) sin²γ)]
= a cos γ · [2b cos²γ - 2(a+b) sin²γ - b cos(2γ) + a] / [2(b cos²γ - (a+b) sin²γ)]

Let me simplify the numerator:
2b cos²γ - 2(a+b) sin²γ - b(cos²γ - sin²γ) + a
= 2bp - 2(a+b)q - b(p-q) + a
= 2bp - 2aq - 2bq - bp + bq + a
= bp - bq - 2aq + a
= b(p-q) + a(1 - 2q)
= b cos(2γ) + a(p - q)  [since 1 - 2q = 1 - 2sin²γ = cos(2γ) = p - q]
= b cos(2γ) + a cos(2γ)
= (a+b) cos(2γ)

So Q_y = a cos γ · (a+b) cos(2γ) / [2(b cos²γ - (a+b) sin²γ)]
= a(a+b) cos(2γ) cos γ / [2(b cos²γ - (a+b) sin²γ)]

Now, P is on segment AX and Q is on segment BY. The problem says the external bisector of angle AHB meets segments AX and BY at P and Q. For P and Q to be on the segments (not extensions), we need u, v ∈ [0, 1].

Now, AP = distance from A to P = u · |AX| (since P = A + u(X-A)).
BQ = distance from B to Q = v · |BY|.

PX = (1-u) · |AX|, QY = (1-v) · |BY|.

The condition PX = QY means (1-u)|AX| = (1-v)|BY|.

Let me compute |AX| and |BY|.

|AX|² = (X_x - A_x)² + (0 - A_y)²
= (-a cos(2γ)/sin γ + b sin γ)² + b² cos²γ

Let me compute -a cos(2γ)/sin γ + b sin γ = [-a cos(2γ) + b sin²γ]/sin γ = [-a(p-q) + bq]/sin γ = [-ap + aq + bq]/sin γ = [-ap + (a+b)q]/sin γ

So |AX|² = [-ap + (a+b)q]²/sin²γ + b² cos²γ
= [-ap + (a+b)q]²/sin²γ + b²p

Let me denote D_A = -ap + (a+b)q = -a cos²γ + (a+b) sin²γ. Then:
|AX|² = D_A²/sin²γ + b² cos²γ = [D_A² + b² cos²γ sin²γ]/sin²γ = [D_A² + b²pq]/sin²γ

D_A² + b²pq = a²p² - 2a(a+b)pq + (a+b)²q² + b²pq
= a²p² + (a+b)²q² + pq[b² - 2a(a+b)]
= a²p² + (a+b)²q² + pq[b² - 2a² - 2ab]
= a²p² + (a² + 2ab + b²)q² + pq[b² - 2a² - 2ab]
= a²p² + a²q² + 2abq² + b²q² + b²pq - 2a²pq - 2abpq
= a²(p² + q² - 2pq) + 2ab(q² - pq) + b²(q² + pq)
= a²(p-q)² + 2abq(q-p) + b²q(p+q)
= a² cos²(2γ) - 2abq cos(2γ) + b²q
= a² cos²(2γ) - 2ab sin²γ cos(2γ) + b² sin²γ

Hmm, let me try to factor this. Let me see if it's a perfect square or something nice.

= a² cos²(2γ) + b² sin²γ - 2ab sin²γ cos(2γ)

Let me check if this equals (a cos(2γ) - b sin²γ... no. Let me try (a cos(2γ) - b sin γ)²... no, that would give a² cos²(2γ) - 2ab sin γ cos(2γ) + b² sin²γ, which has sin γ not sin²γ.

Hmm. Let me try a slightly different approach. Let me use the substitution a = BC, b = CA, and use the angle C = 2γ.

Actually, this algebra is getting very heavy. Let me try a computational/numerical approach to get intuition for the answer, then verify.

Let me pick specific values. Let me try γ = π/6 (so C = π/3 = 60°), and try different a, b.

With C = 60°, cos(2γ) = cos(60°) = 1/2, sin γ = sin(30°) = 1/2, cos γ = cos(30°) = √3/2, sin²γ = 1/4, cos²γ = 3/4.

Let me try a = 3, b = 2 (so AC = 2, BC = 3, AC ≠ BC ✓).

H_x = (b-a) cos(2γ)/(2 sin γ) = (2-3)(1/2)/(2·1/2) = (-1)(1/2)/1 = -1/2
H_y = (a+b) cos(2γ)/(2 cos γ) = 5(1/2)/(2·√3/2) = (5/2)/√3 = 5/(2√3)

CH = √(1/4 + 25/12) = √(3/12 + 25/12) = √(28/12) = √(7/3) = √7/√3

Check: c² = a² + b² - 2ab cos(C) = 9 + 4 - 2·3·2·(1/2) = 13 - 6 = 7, so c = √7.
CH = c cot C = √7 · cot(60°) = √7 · (1/√3) = √7/√3. ✓

X = (-a cos(2γ)/sin γ, 0) = (-3·(1/2)/(1/2), 0) = (-3, 0)
Y = (b cos(2γ)/sin γ, 0) = (2·(1/2)/(1/2), 0) = (2, 0)

A = (-b sin γ, b cos γ) = (-2·(1/2), 2·√3/2) = (-1, √3)
B = (a sin γ, a cos γ) = (3·(1/2), 3·√3/2) = (3/2, 3√3/2)

External bisector of angle AHB: vertical line x = H_x = -1/2.

P on AX: A = (-1, √3), X = (-3, 0).
Direction X - A = (-2, -√3).
P = A + u(X - A) = (-1 - 2u, √3 - √3 u) = (-1 - 2u, √3(1-u))
Set x = -1/2: -1 - 2u = -1/2 → u = -1/4.

Hmm, u = -1/4 < 0, which means P is not on segment AX but on the extension beyond A. That's a problem since the problem says P is on segment AX.

Let me reconsider. Maybe I have the wrong bisector. The problem says "the external bisector of the angle AHB". Let me reconsider which bisector this is.

Angle AHB = π - C. The external bisector of angle AHB bisects the external angle at H. The external angle at H is the supplement, which is C = 2γ. Wait, no. The external angle is π - (π - C) = C. So the external bisector bisects angle C at H.

But I said the external bisector of angle AHB is perpendicular to the internal bisector of angle AHB, and the internal bisector of angle AHB is parallel to the external bisector of angle C (x-axis). So the external bisector of angle AHB is vertical (parallel to y-axis / internal bisector of C). That seems right.

But with a = 3, b = 2, γ = π/6, we get u = -1/4, meaning P is not on segment AX. Let me check if the problem requires specific relationship between a and b for P, Q to be on the segments.

Actually, the problem says "meets the segments AX and BY at P and Q respectively". This implies P is on segment AX and Q is on segment BY. So maybe the condition PX = QY constrains the triangle further, and for those triangles, P and Q are indeed on the segments.

Wait, but the problem says "It is known that PX = QY" — this is a given condition. So we need to find triangles satisfying PX = QY, and for those, find the minimum of (AP + BQ)/CH.

Let me compute PX and QY for the general case and set them equal.

PX = (1 - u)|AX|, QY = (1 - v)|BY|.

Let me compute 1 - u and 1 - v.

1 - u = 1 - [b - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= [2(b sin²γ - a cos(2γ)) - (b - a cos(2γ))] / [2(b sin²γ - a cos(2γ))]
= [2b sin²γ - 2a cos(2γ) - b + a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= [b(2 sin²γ - 1) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= [-b cos(2γ) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= -(a+b) cos(2γ) / [2(b sin²γ - a cos(2γ))]

1 - v = 1 - [b cos(2γ) - a] / [2(b cos²γ - (a+b) sin²γ)]
= [2(b cos²γ - (a+b) sin²γ) - (b cos(2γ) - a)] / [2(b cos²γ - (a+b) sin²γ)]

Numerator: 2b cos²γ - 2(a+b) sin²γ - b cos(2γ) + a
= 2bp - 2(a+b)q - b(p-q) + a
= 2bp - 2aq - 2bq - bp + bq + a
= bp - bq - 2aq + a
= b(p-q) + a(1 - 2q)
= b cos(2γ) + a cos(2γ)
= (a+b) cos(2γ)

So 1 - v = (a+b) cos(2γ) / [2(b cos²γ - (a+b) sin²γ)]

Now, the condition PX = QY:
(1-u)|AX| = (1-v)|BY|

-(a+b) cos(2γ) |AX| / [2(b sin²γ - a cos(2γ))] = (a+b) cos(2γ) |BY| / [2(b cos²γ - (a+b) sin²γ)]

Since (a+b) cos(2γ) > 0 (acute triangle), we can cancel:

-|AX| / (b sin²γ - a cos(2γ)) = |BY| / (b cos²γ - (a+b) sin²γ)

Note that b sin²γ - a cos(2γ) = bq - a(p-q) = bq - ap + aq = (a+b)q - ap = D_A (which we defined earlier).
And b cos²γ - (a+b) sin²γ = bp - (a+b)q = D_B (let's call it).

So: -|AX| / D_A = |BY| / D_B

Since |AX|, |BY| > 0, this means D_A and D_B have opposite signs (or we need to be careful about signs).

Actually, for P to be on segment AX, we need u ∈ [0,1], which requires 1-u ∈ [0,1]. We computed 1-u = -(a+b)cos(2γ)/(2 D_A). Since (a+b)cos(2γ) > 0, we need D_A < 0 for 1-u > 0, i.e., u < 1. And for u > 0, we need... let me check: u = [b - a cos(2γ)]/(2 D_A). For u > 0, we need [b - a cos(2γ)] and D_A to have the same sign.

Similarly for Q: 1-v = (a+b)cos(2γ)/(2 D_B) > 0 requires D_B > 0.

So for P on segment AX: D_A < 0 (for 1-u > 0) and u > 0 (which needs b - a cos(2γ) and D_A same sign, so b - a cos(2γ) < 0, i.e., b < a cos(2γ)).

For Q on segment BY: D_B > 0 (for 1-v > 0) and v > 0 (which needs b cos(2γ) - a and D_B same sign, so b cos(2γ) - a > 0, i.e., b cos(2γ) > a, OR both negative).

Hmm wait, let me reconsider. For P on segment AX, we need 0 ≤ u ≤ 1.
u = [b - a cos(2γ)] / [2 D_A] where D_A = (a+b) sin²γ - a cos²γ = (a+b)q - ap.

And 1 - u = -(a+b) cos(2γ) / [2 D_A].

For 0 ≤ u ≤ 1: need 0 ≤ 1-u ≤ 1, so 0 ≤ -(a+b)cos(2γ)/(2D_A) ≤ 1.
Since (a+b)cos(2γ) > 0, we need D_A < 0 for 1-u ≥ 0.
And 1-u ≤ 1 means -(a+b)cos(2γ)/(2D_A) ≤ 1, i.e., -(a+b)cos(2γ) ≥ 2D_A (since D_A < 0, dividing flips), i.e., (a+b)cos(2γ) ≤ -2D_A = 2(ap - (a+b)q) = 2a cos(2γ) + 2b cos²γ - 2b sin²γ... 

hmm wait: -2D_A = -2[(a+b)q - ap] = 2ap - 2(a+b)q = 2a(p-q) - 2bq = 2a cos(2γ) - 2b sin²γ.

So (a+b)cos(2γ) ≤ 2a cos(2γ) - 2b sin²γ
→ b cos(2γ) ≤ a cos(2γ) - 2b sin²γ
→ b cos(2γ) + 2b sin²γ ≤ a cos(2γ)
→ b[cos(2γ) + 2 sin²γ] ≤ a cos(2γ)
→ b[cos²γ - sin²γ + 2 sin²γ] ≤ a cos(2γ)
→ b[cos²γ + sin²γ] ≤ a cos(2γ)
→ b ≤ a cos(2γ)

So for P on segment AX, we need D_A < 0 and b ≤ a cos(2γ).

D_A < 0: (a+b) sin²γ < a cos²γ, i.e., (a+b) sin²γ < a cos²γ, i.e., b sin²γ < a(cos²γ - sin²γ) = a cos(2γ), i.e., b < a cos(2γ)/sin²γ.

Since cos(2γ)/sin²γ = (cos²γ - sin²γ)/sin²γ = cos²γ/sin²γ - 1 = cot²γ - 1, and for γ < π/4, this is positive. Also b ≤ a cos(2γ) is a stronger condition than b < a cos(2γ)/sin²γ (since cos(2γ) < cos(2γ)/sin²γ when sin²γ < 1, which is always true). So the binding condition is b ≤ a cos(2γ), i.e., b/a ≤ cos(2γ) = cos C.

Similarly for Q on segment BY: need D_B > 0 and v ≥ 0.
D_B = b cos²γ - (a+b) sin²γ = bp - (a+b)q.
D_B > 0: b cos²γ > (a+b) sin²γ, i.e., b cos²γ - b sin²γ > a sin²γ, i.e., b cos(2γ) > a sin²γ, i.e., a < b cos(2γ)/sin²γ.

1 - v = (a+b)cos(2γ)/(2D_B) ≤ 1 requires (a+b)cos(2γ) ≤ 2D_B = 2bp - 2(a+b)q = 2b(p-q) - 2aq = 2b cos(2γ) - 2a sin²γ.
→ a cos(2γ) ≤ b cos(2γ) - 2a sin²γ
→ a cos(2γ) + 2a sin²γ ≤ b cos(2γ)
→ a[cos(2γ) + 2 sin²γ] ≤ b cos(2γ)
→ a ≤ b cos(2γ)

So for Q on segment BY: a ≤ b cos(2γ), i.e., a/b ≤ cos C.

Combining: b ≤ a cos C and a ≤ b cos C. So b/a ≤ cos C and a/b ≤ cos C, meaning:
b/a ≤ cos C and a/b ≤ cos C
→ (b/a)(a/b) ≤ cos²C → 1 ≤ cos²C → cos²C ≥ 1 → cos C = 1 → C = 0.

That can't be right for a non-degenerate triangle. So both conditions can't be simultaneously satisfied unless... wait, that means P and Q can't both be on the segments AX and BY simultaneously?

Let me re-examine. Maybe I have the wrong bisector. Let me reconsider.

The problem says "the external bisector of the angle AHB meets the segments AX and BY at P and Q respectively." Maybe "segments AX and BY" refers to the segments from A to X and from B to Y, where X is on the altitude from B (extended if necessary) and Y is on the altitude from A (extended if necessary). But the problem says X is where the altitude from B meets the external bisector of C, and Y is where the altitude from A meets the external bisector of C. These are specific points.

Hmm, but if P can't be on segment AX and Q on segment BY simultaneously (for a non-degenerate acute triangle with AC ≠ BC), then maybe I have the wrong bisector.

Let me reconsider. Maybe the "external bisector of angle AHB" is the other external bisector. An angle has two bisectors: internal and external. The external bisector bisects the reflex angle (or equivalently, is perpendicular to the internal bisector). But there's only one external bisector line.

Wait, but I need to be more careful. The "external bisector of angle AHB" — angle AHB is the angle at H in the configuration. There are two rays from H: HA and HB. The internal bisector bisects the angle between them (the angle < π), and the external bisector bisects the supplementary angle.

I claimed the internal bisector of angle AHB is parallel to the external bisector of C (x-axis), and the external bisector of angle AHB is parallel to the internal bisector of C (y-axis). Let me double-check this.

The altitude from A is perpendicular to BC. The altitude from B is perpendicular to AC. The angle between the altitudes (at H) is π - C.

The internal bisector of the angle between the altitudes: if we rotate both altitudes by 90°, they become parallel to BC and AC respectively. The bisector of the angle between BC and AC is the bisector of angle C. Rotating back by 90°, the bisector of the angle between the altitudes is perpendicular to the bisector of angle C.

So internal bisector of angle AHB ⊥ bisector of angle C.

The internal bisector of angle C is the y-axis. So the internal bisector of angle AHB is horizontal (parallel to x-axis = external bisector of C). The external bisector of angle AHB is vertical (parallel to y-axis = internal bisector of C). This seems correct.

But then P and Q can't both be on the segments. Let me recheck with the numerical example.

With a=3, b=2, γ=π/6: 
- For P on AX: need b ≤ a cos C, i.e., 2 ≤ 3·(1/2) = 1.5. FALSE.
- For Q on BY: need a ≤ b cos C, i.e., 3 ≤ 2·(1/2) = 1. FALSE.

So indeed neither P nor Q is on the respective segment. Let me try a=2, b=3:
- For P on AX: need b ≤ a cos C, i.e., 3 ≤ 2·(1/2) = 1. FALSE.
- For Q on BY: need a ≤ b cos C, i.e., 2 ≤ 3·(1/2) = 1.5. FALSE.

Still false. Let me try a=1, b=1 (but AC ≠ BC is required, so a ≠ b). Let me try a=1.1, b=1:
- P on AX: 1 ≤ 1.1·0.5 = 0.55. FALSE.

It seems like for C = 60°, the conditions are very restrictive. Let me try a smaller angle C.

Let me try C = 30° (γ = 15°). cos C = cos 30° ≈ 0.866.
- a = 1, b = 0.8: P on AX needs 0.8 ≤ 1·0.866 = 0.866. TRUE. Q on BY needs 1 ≤ 0.8·0.866 = 0.693. FALSE.

Hmm, still can't get both. The issue is that b ≤ a cos C and a ≤ b cos C together imply 1 ≤ cos²C, which is impossible for C > 0.

So I must be making an error. Let me reconsider the problem.

Wait, maybe I need to reconsider which external bisector of angle C is being used. The external bisector of angle C — there are actually two external angles at C, and thus two external bisectors. But they're the same line (the external bisector is unique as a line, just with two opposite rays).

Actually, I think the issue might be with my identification of the external bisector of angle AHB. Let me reconsider.

Actually, wait. Let me reconsider the problem statement. "The external bisector of the angle AHB meets the segments AX and BY at P and Q respectively."

Maybe AX and BY don't mean the segments from A to X and B to Y. Maybe they mean the lines AX and BY. In many geometry problems, "segment AX" could refer to the line segment, but if P is not between A and X, then maybe the problem means the line.

Actually, re-reading: "meets the segments AX and BY at P and Q respectively" — this does say segments. But if it's impossible for both P and Q to be on the segments simultaneously, then maybe I have an error somewhere.

Let me recheck my computation of X and Y.

X is where the altitude from B meets the external bisector of C. The altitude from B is perpendicular to AC and passes through B. The external bisector of C is the x-axis.

Altitude from B: passes through B = (a sin γ, a cos γ) with direction (cos γ, sin γ) (perpendicular to AC direction (-sin γ, cos γ)).

Wait, is (cos γ, sin γ) the right direction? AC direction is (-sin γ, cos γ) (from C to A). Perpendicular to this: (cos γ, sin γ) or (-cos γ, -sin γ). Let me verify: (-sin γ)(cos γ) + (cos γ)(sin γ) = 0. Yes, perpendicular.

So altitude from B: (a sin γ + s cos γ, a cos γ + s sin γ). Setting y = 0: a cos γ + s sin γ = 0, s = -a cos γ/sin γ. x = a sin γ - a cos²γ/sin γ = a(sin²γ - cos²γ)/sin γ = -a cos(2γ)/sin γ.

Since cos(2γ) > 0 (acute triangle, C < π/2 so 2γ < π/2... wait, C < π/2 means 2γ < π/2, so γ < π/4, so cos(2γ) > 0). So X_x = -a cos(2γ)/sin γ < 0. X is on the negative x-axis.

Similarly Y_x = b cos(2γ)/sin γ > 0. Y is on the positive x-axis.

A = (-b sin γ, b cos γ): A_x < 0, A_y > 0.
B = (a sin γ, a cos γ): B_x > 0, B_y > 0.

So A is in the second quadrant, B is in the first quadrant, X is on the negative x-axis, Y is on the positive x-axis.

Segment AX: from A (second quadrant) to X (negative x-axis). This segment is entirely in the region x < 0 (roughly). Actually, A_x = -b sin γ < 0 and X_x = -a cos(2γ)/sin γ < 0, so the segment AX has x < 0 throughout.

Segment BY: from B (first quadrant) to Y (positive x-axis). B_x = a sin γ > 0 and Y_x = b cos(2γ)/sin γ > 0, so segment BY has x > 0 throughout.

The external bisector of angle AHB is the vertical line x = H_x = (b-a) cos(2γ)/(2 sin γ).

For P on segment AX (x < 0): need H_x < 0, i.e., b < a.
For Q on segment BY (x > 0): need H_x > 0, i.e., b > a.

These are contradictory! So P and Q can't both be on the respective segments unless... hmm.

Wait, unless the vertical line x = H_x passes through both segments, which requires H_x to be in the x-range of both AX and BY. But AX has x < 0 and BY has x > 0, so H_x would need to be both < 0 and > 0, impossible.

So there's definitely something wrong with my approach. Let me reconsider.

Maybe the external bisector of angle AHB is not vertical. Let me recheck.

I claimed: internal bisector of angle AHB is parallel to external bisector of C (x-axis), and external bisector of angle AHB is parallel to internal bisector of C (y-axis).

But wait, is this correct? Let me think again more carefully.

The angle AHB at H is formed by rays HA and HB. The internal bisector bisects this angle. I need to find the actual direction of this bisector, not just say it's "parallel to" something.

Let me compute the directions of HA and HB.

H = ((b-a) cos(2γ)/(2 sin γ), (a+b) cos(2γ)/(2 cos γ))

HA = A - H = (-b sin γ - (b-a) cos(2γ)/(2 sin γ), b cos γ - (a+b) cos(2γ)/(2 cos γ))

Let me compute HA_x:
= [-2b sin²γ - (b-a) cos(2γ)] / (2 sin γ)
= [-2b sin²γ - (b-a)(cos²γ - sin²γ)] / (2 sin γ)
= [-2b sin²γ - b cos²γ + b sin²γ + a cos²γ - a sin²γ] / (2 sin γ)
= [-b sin²γ - b cos²γ + a cos²γ - a sin²γ] / (2 sin γ)
= [-b(sin²γ + cos²γ) + a(cos²γ - sin²γ)] / (2 sin γ)
= [-b + a cos(2γ)] / (2 sin γ)

HA_y:
= [2b cos²γ - (a+b) cos(2γ)] / (2 cos γ)
= [2b cos²γ - (a+b)(cos²γ - sin²γ)] / (2 cos γ)
= [2b cos²γ - a cos²γ + a sin²γ - b cos²γ + b sin²γ] / (2 cos γ)
= [b cos²γ + b sin²γ - a cos²γ + a sin²γ] / (2 cos γ)
= [b - a cos(2γ)] / (2 cos γ)

So HA = ([a cos(2γ) - b] / (2 sin γ), [b - a cos(2γ)] / (2 cos γ))
= (a cos(2γ) - b) / 2 · (1/sin γ, -1/cos γ)

So HA direction is (1/sin γ, -1/cos γ) (up to sign), or equivalently (cos γ, -sin γ) (multiplying by sin γ cos γ). This makes sense: the altitude from A has direction (cos γ, -sin γ), and HA is along this altitude.

Similarly, HB = B - H:
HB_x = a sin γ - (b-a) cos(2γ)/(2 sin γ)
= [2a sin²γ - (b-a) cos(2γ)] / (2 sin γ)
= [2a sin²γ - b cos(2γ) + a cos(2γ)] / (2 sin γ)
= [2a sin²γ + a(cos²γ - sin²γ) - b(cos²γ - sin²γ)] / (2 sin γ)
= [a sin²γ + a cos²γ - b cos²γ + b sin²γ] / (2 sin γ)
= [a - b cos(2γ)] / (2 sin γ)

Hmm wait, let me redo:
= [2a sin²γ - (b-a)(cos²γ - sin²γ)] / (2 sin γ)
= [2a sin²γ - b cos²γ + b sin²γ + a cos²γ - a sin²γ] / (2 sin γ)
= [a sin²γ + a cos²γ + b sin²γ - b cos²γ] / (2 sin γ)
= [a + b(sin²γ - cos²γ)] / (2 sin γ)
= [a - b cos(2γ)] / (2 sin γ)

HB_y = a cos γ - (a+b) cos(2γ)/(2 cos γ)
= [2a cos²γ - (a+b) cos(2γ)] / (2 cos γ)
= [2a cos²γ - (a+b)(cos²γ - sin²γ)] / (2 cos γ)
= [2a cos²γ - a cos²γ + a sin²γ - b cos²γ + b sin²γ] / (2 cos γ)
= [a cos²γ + a sin²γ - b cos²γ + b sin²γ] / (2 cos γ)
= [a - b cos(2γ)] / (2 cos γ)

Wait, that gives:
= [a(cos²γ + sin²γ) + b(sin²γ - cos²γ)] / (2 cos γ)
= [a - b cos(2γ)] / (2 cos γ)

So HB = ([a - b cos(2γ)] / (2 sin γ), [a - b cos(2γ)] / (2 cos γ))
= [a - b cos(2γ)] / 2 · (1/sin γ, 1/cos γ)

So HB direction is (1/sin γ, 1/cos γ), or equivalently (cos γ, sin γ). This is the direction of the altitude from B, which makes sense.

Now, the internal bisector of angle AHB bisects the angle between HA and HB.

HA direction: (cos γ, -sin γ) (pointing from H toward A, but the sign depends on a cos(2γ) - b)
HB direction: (cos γ, sin γ) (pointing from H toward B, but the sign depends on a - b cos(2γ))

The unit vectors:
HA unit: (cos γ, -sin γ) (this is already a unit vector since cos²γ + sin²γ = 1)
HB unit: (cos γ, sin γ) (also a unit vector)

The internal bisector direction is the sum of unit vectors: (cos γ, -sin γ) + (cos γ, sin γ) = (2 cos γ, 0), which is horizontal (along x-axis). ✓

The external bisector direction is the difference: (cos γ, -sin γ) - (cos γ, sin γ) = (0, -2 sin γ), which is vertical (along y-axis). ✓

So my earlier analysis was correct: the external bisector of angle AHB is vertical, passing through H.

But then P on segment AX (x < 0) and Q on segment BY (x > 0) can't both be on the vertical line x = H_x unless H_x = 0, which means a = b, contradicting AC ≠ BC.

So something is fundamentally wrong. Let me re-read the problem.

"The altitudes drawn from A and B meet at H and intersect the external bisector of the angle C at Y and X respectively."

So: altitude from A intersects external bisector of C at Y. Altitude from B intersects external bisector of C at X. This is what I had.

"The external bisector of the angle AHB meets the segments AX and BY at P and Q respectively."

So the external bisector of angle AHB meets segment AX at P and segment BY at Q.

Segment AX: from A to X. A is in the second quadrant (x < 0), X is on the negative x-axis (x < 0). So segment AX has x < 0.

Segment BY: from B to Y. B is in the first quadrant (x > 0), Y is on the positive x-axis (x > 0). So segment BY has x > 0.

The external bisector of angle AHB is vertical (x = H_x). For it to meet segment AX (x < 0), we need H_x < 0, i.e., b < a. For it to meet segment BY (x > 0), we need H_x > 0, i.e., b > a. Contradiction.

Unless... the external bisector of angle AHB is not the vertical line but the horizontal line! Let me reconsider.

Wait, I think I may have confused internal and external. Let me reconsider.

The angle AHB = π - C. The internal bisector bisects this angle. The external bisector is perpendicular to the internal bisector.

I found the internal bisector direction is (2 cos γ, 0) = horizontal. The external bisector direction is (0, -2 sin γ) = vertical.

But wait, which bisector is "internal" and which is "external" depends on which angle we're bisecting. The angle AHB is the angle at H looking from HA to HB. There are two angles: the one < π (which is π - C) and the one > π (which is π + C). The internal bisector bisects the angle < π, and the external bisector bisects the angle > π (or equivalently, is perpendicular to the internal bisector).

But actually, the internal and external bisectors are just two perpendicular lines through H. One is horizontal, one is vertical. The "external bisector of angle AHB" is the one that bisects the external (reflex) angle.

Hmm, but regardless of which is internal and which is external, one is horizontal and one is vertical. The vertical one can't meet both segments. The horizontal one (y = H_y) could potentially meet both segments.

Let me check: the horizontal line y = H_y = (a+b) cos(2γ)/(2 cos γ).

Segment AX: from A = (-b sin γ, b cos γ) to X = (-a cos(2γ)/sin γ, 0).
The y-coordinates along AX go from b cos γ (at A) to 0 (at X). H_y = (a+b) cos(2γ)/(2 cos γ).

Is H_y between 0 and b cos γ? 
H_y = (a+b) cos(2γ)/(2 cos γ) vs b cos γ.
H_y / (b cos γ) = (a+b) cos(2γ) / (2b cos²γ) = (a+b)(cos²γ - sin²γ) / (2b cos²γ) = (a+b)/(2b) · (1 - tan²γ).

For this to be between 0 and 1: need (a+b)/(2b) · (1 - tan²γ) ≤ 1, i.e., (a+b)(1 - tan²γ) ≤ 2b, i.e., (a+b) - (a+b)tan²γ ≤ 2b, i.e., a - b ≤ (a+b)tan²γ. Since a, b > 0 and tan²γ > 0, this is a - b ≤ (a+b)tan²γ. If a ≤ b, this is automatically satisfied. If a > b, need (a-b)/(a+b) ≤ tan²γ.

Similarly for segment BY: from B = (a sin γ, a cos γ) to Y = (b cos(2γ)/sin γ, 0).
Y-coordinates go from a cos γ (at B) to 0 (at Y). H_y = (a+b) cos(2γ)/(2 cos γ).
H_y / (a cos γ) = (a+b) cos(2γ) / (2a cos²γ) = (a+b)/(2a) · (1 - tan²γ).
For this to be between 0 and 1: (a+b)(1-tan²γ) ≤ 2a, i.e., b - a ≤ (a+b)tan²γ. If b ≤ a, auto. If b > a, need (b-a)/(a+b) ≤ tan²γ.

So the horizontal line y = H_y can meet both segments AX and BY if:
|a - b|/(a+b) ≤ tan²γ, i.e., |a-b| ≤ (a+b) tan²γ.

This is possible! So maybe the "external bisector of angle AHB" is the horizontal line, not the vertical line.

Let me reconsider which bisector is internal and which is external.

The angle AHB = π - C. Looking at the directions:
- HA direction (from H): (cos γ, -sin γ) [when a cos(2γ) > b, pointing toward A] or (-cos γ, sin γ) [when a cos(2γ) < b]
- HB direction (from H): (cos γ, sin γ) [when a > b cos(2γ)] or (-cos γ, -sin γ) [when a < b cos(2γ)]

The angle between (cos γ, -sin γ) and (cos γ, sin γ): 
cos(angle) = cos²γ - sin²γ = cos(2γ) = cos C.
So the angle is C... wait, that's the angle between the two direction vectors. But angle AHB = π - C, not C.

Hmm, the issue is the direction of HA and HB. The vectors (cos γ, -sin γ) and (cos γ, sin γ) have angle C between them (since cos of angle = cos(2γ) = cos C). But the actual angle AHB is π - C. This means the rays HA and HB point in directions that make angle π - C, not C.

This happens when one of the direction vectors is flipped. For instance, if HA points in direction (-cos γ, sin γ) (opposite to (cos γ, -sin γ)) and HB points in direction (cos γ, sin γ), then the angle between them is:
cos(angle) = -cos²γ + sin²γ = -cos(2γ) = -cos C, so angle = π - C. ✓

So the actual rays from H are:
- HA: direction (-cos γ, sin γ) = pointing up-left (toward A in second quadrant)
- HB: direction (cos γ, sin γ) = pointing up-right (toward B in first quadrant)

The angle between these is π - C (opening upward). The internal bisector (bisecting the angle π - C that opens upward) is the direction (0, 1) = vertical (upward). The external bisector is horizontal.

Wait, let me recalculate. The sum of unit vectors:
(-cos γ, sin γ) + (cos γ, sin γ) = (0, 2 sin γ), direction (0, 1) = vertical.

The difference:
(-cos γ, sin γ) - (cos γ, sin γ) = (-2 cos γ, 0), direction (-1, 0) = horizontal.

So the internal bisector of angle AHB (bisecting the angle π - C that opens upward) is vertical (upward), and the external bisector is horizontal.

I had it backwards! The internal bisector is vertical, and the external bisector is horizontal.

So the external bisector of angle AHB is the horizontal line y = H_y = (a+b) cos(2γ)/(2 cos γ).

This makes much more sense! The horizontal line can intersect both segments AX and BY.

Let me redo the computation with the correct bisector.

The external bisector of angle AHB is the horizontal line y = H_y = (a+b) cos(2γ)/(2 cos γ).

P is on segment AX with y = H_y.
A = (-b sin γ, b cos γ), X = (-a cos(2γ)/sin γ, 0).

Parametrize: P = A + u(X - A), u ∈ [0, 1].
P_y = b cos γ + u(0 - b cos γ) = b cos γ(1 - u) = H_y = (a+b) cos(2γ)/(2 cos γ)

So 1 - u = (a+b) cos(2γ) / (2b cos²γ) = (a+b)(cos²γ - sin²γ) / (2b cos²γ) = (a+b)/(2b) · (1 - tan²γ)

u = 1 - (a+b)(1 - tan²γ)/(2b) = [2b - (a+b)(1 - tan²γ)] / (2b) = [2b - a - b + (a+b)tan²γ] / (2b) = [b - a + (a+b)tan²γ] / (2b)

For u ∈ [0, 1]: need 0 ≤ b - a + (a+b)tan²γ and b - a + (a+b)tan²γ ≤ 2b.
The first: (a+b)tan²γ ≥ a - b, i.e., if a > b: tan²γ ≥ (a-b)/(a+b).
The second: (a+b)tan²γ ≤ b + a, i.e., tan²γ ≤ 1, i.e., γ ≤ π/4, which is true for acute triangle.

Similarly, Q is on segment BY with y = H_y.
B = (a sin γ, a cos γ), Y = (b cos(2γ)/sin γ, 0).

Q = B + v(Y - B), v ∈ [0, 1].
Q_y = a cos γ(1 - v) = H_y = (a+b) cos(2γ)/(2 cos γ)

1 - v = (a+b) cos(2γ) / (2a cos²γ) = (a+b)/(2a) · (1 - tan²γ)

v = 1 - (a+b)(1 - tan²γ)/(2a) = [2a - (a+b)(1 - tan²γ)] / (2a) = [2a - a - b + (a+b)tan²γ] / (2a) = [a - b + (a+b)tan²γ] / (2a)

For v ∈ [0, 1]: need 0 ≤ a - b + (a+b)tan²γ and a - b + (a+b)tan²γ ≤ 2a.
First: if b > a: tan²γ ≥ (b-a)/(a+b).
Second: tan²γ ≤ 1, true.

So for both P and Q to be on the segments: |a - b|/(a+b) ≤ tan²γ.

Now, AP = u · |AX|, PX = (1-u) · |AX|.
BQ = v · |BY|, QY = (1-v) · |BY|.

PX = (1-u)|AX| = [(a+b)(1 - tan²γ)/(2b)] · |AX|
QY = (1-v)|BY| = [(a+b)(1 - tan²γ)/(2a)] · |BY|

Condition PX = QY:
[(a+b)(1 - tan²γ)/(2b)] · |AX| = [(a+b)(1 - tan²γ)/(2a)] · |BY|

Since (a+b)(1-tan²γ) > 0 (acute triangle, γ < π/4 so tan²γ < 1), we can cancel:
|AX|/b = |BY|/a
a · |AX| = b · |BY|

So the condition PX = QY reduces to a · |AX| = b · |BY|.

Let me compute |AX| and |BY|.

|AX|² = (X_x - A_x)² + (0 - A_y)²
X_x - A_x = -a cos(2γ)/sin γ - (-b sin γ) = -a cos(2γ)/sin γ + b sin γ = [-a cos(2γ) + b sin²γ]/sin γ

Let me use the notation: let t = tan γ, so sin γ = t/√(1+t²), cos γ = 1/√(1+t²), sin²γ = t²/(1+t²), cos²γ = 1/(1+t²), cos(2γ) = (1-t²)/(1+t²).

Actually, let me try a different approach. Let me use the formula for the distance from a point to a line, or just compute directly.

|AX|² = [(-a cos(2γ) + b sin²γ)/sin γ]² + b² cos²γ

Let me expand:
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin⁴γ] / sin²γ + b² cos²γ
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin⁴γ + b² cos²γ sin²γ] / sin²γ
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ(sin²γ + cos²γ)] / sin²γ
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ

Similarly:
|BY|² = (Y_x - B_x)² + (0 - B_y)²
Y_x - B_x = b cos(2γ)/sin γ - a sin γ = [b cos(2γ) - a sin²γ]/sin γ

|BY|² = [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin⁴γ] / sin²γ + a² cos²γ
= [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin⁴γ + a² cos²γ sin²γ] / sin²γ
= [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ] / sin²γ

So:
|AX|² = [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ
|BY|² = [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ] / sin²γ

The condition a|AX| = b|BY| means a²|AX|² = b²|BY|²:
a²[a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] = b²[b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ]

a⁴ cos²(2γ) - 2a³b cos(2γ) sin²γ + a²b² sin²γ = b⁴ cos²(2γ) - 2ab³ cos(2γ) sin²γ + a²b² sin²γ

a⁴ cos²(2γ) - 2a³b cos(2γ) sin²γ = b⁴ cos²(2γ) - 2ab³ cos(2γ) sin²γ

(a⁴ - b⁴) cos²(2γ) = 2ab cos(2γ) sin²γ (a² - b²)

(a² - b²)(a² + b²) cos²(2γ) = 2ab(a² - b²) cos(2γ) sin²γ

Since a ≠ b (AC ≠ BC), we can divide by (a² - b²):

(a² + b²) cos²(2γ) = 2ab cos(2γ) sin²γ

Since cos(2γ) > 0 (acute triangle), divide by cos(2γ):

(a² + b²) cos(2γ) = 2ab sin²γ

(a² + b²)(cos²γ - sin²γ) = 2ab sin²γ

(a² + b²) cos²γ = (a² + b²) sin²γ + 2ab sin²γ = (a² + 2ab + b²) sin²γ = (a+b)² sin²γ

So: (a² + b²) cos²γ = (a+b)² sin²γ

→ tan²γ = (a² + b²) / (a+b)²

→ tan γ = √(a² + b²) / (a+b)

This is the condition from PX = QY.

Now, let me compute AP + BQ and CH under this condition.

AP = u · |AX|, BQ = v · |BY|.

u = [b - a + (a+b)tan²γ] / (2b)
v = [a - b + (a+b)tan²γ] / (2a)

Under the condition tan²γ = (a² + b²)/(a+b)²:

(a+b)tan²γ = (a² + b²)/(a+b)

u = [b - a + (a² + b²)/(a+b)] / (2b) = [(b-a)(a+b) + a² + b²] / [(a+b) · 2b]
= [b² - a² + a² + b²] / [2b(a+b)]
= 2b² / [2b(a+b)]
= b / (a+b)

v = [a - b + (a² + b²)/(a+b)] / (2a) = [(a-b)(a+b) + a² + b²] / [(a+b) · 2a]
= [a² - b² + a² + b²] / [2a(a+b)]
= 2a² / [2a(a+b)]
= a / (a+b)

So u = b/(a+b) and v = a/(a+b). Nice!

AP = u · |AX| = [b/(a+b)] · |AX|
BQ = v · |BY| = [a/(a+b)] · |BY|

AP + BQ = [b|AX| + a|BY|] / (a+b)

Under the condition a|AX| = b|BY|, let's say |AX| = bt and |BY| = at for some t > 0. Then:
AP + BQ = [b · bt + a · at] / (a+b) = [b²t + a²t] / (a+b) = (a² + b²)t / (a+b)

Now I need to find t. We have |AX| = bt, so |AX|² = b²t².

From our formula:
|AX|² = [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ

Under the condition (a² + b²) cos(2γ) = 2ab sin²γ, i.e., cos(2γ) = 2ab sin²γ / (a² + b²):

Let me substitute. Let S = a² + b², P = ab.
cos(2γ) = 2P sin²γ / S

Also, cos(2γ) = cos²γ - sin²γ = 1 - 2sin²γ, so:
1 - 2sin²γ = 2P sin²γ / S
1 = sin²γ(2 + 2P/S) = sin²γ · 2(S + P)/S
sin²γ = S / [2(S + P)] = (a² + b²) / [2(a² + b² + ab)]

And cos²γ = 1 - sin²γ = [2(a² + b² + ab) - (a² + b²)] / [2(a² + b² + ab)] = (a² + b² + 2ab) / [2(a² + b² + ab)] = (a+b)² / [2(a² + b² + ab)]

Let me verify: tan²γ = sin²γ/cos²γ = (a² + b²) / (a+b)². ✓

Now, cos(2γ) = 1 - 2sin²γ = 1 - (a² + b²)/(a² + b² + ab) = ab / (a² + b² + ab)

Let me verify with the other formula: 2ab sin²γ / (a² + b²) = 2ab · (a² + b²)/[2(a² + b² + ab)] / (a² + b²) = ab / (a² + b² + ab). ✓

Now let me compute |AX|²:
|AX|² = [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ

Let me substitute cos(2γ) = ab/(a² + b² + ab) and sin²γ = (a² + b²)/[2(a² + b² + ab)].

Let D = a² + b² + ab for convenience.

cos(2γ) = ab/D
sin²γ = (a² + b²)/(2D) = S/(2D) where S = a² + b²

Numerator of |AX|²:
a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ
= a² (ab/D)² - 2ab · (ab/D) · S/(2D) + b² · S/(2D)
= a² · a²b²/D² - a²b² · S/D² + b²S/(2D)
= a⁴b²/D² - a²b²S/D² + b²S/(2D)
= b²/D² [a⁴ - a²S + SD/2]
= b²/D² [a⁴ - a²(a² + b²) + (a² + b²)(a² + b² + ab)/2]
= b²/D² [a⁴ - a⁴ - a²b² + (a² + b²)²/2 + ab(a² + b²)/2]
= b²/D² [-a²b² + (a⁴ + 2a²b² + b⁴)/2 + (a³b + ab³)/2]
= b²/D² [-a²b² + a⁴/2 + a²b² + b⁴/2 + a³b/2 + ab³/2]
= b²/D² [a⁴/2 + b⁴/2 + a³b/2 + ab³/2]
= b²/(2D²) [a⁴ + b⁴ + a³b + ab³]
= b²/(2D²) [a³(a + b) + b³(a + b)]
= b²/(2D²) (a + b)(a³ + b³)
= b²/(2D²) (a + b)(a + b)(a² - ab + b²)
= b²(a + b)²(a² - ab + b²) / (2D²)

And |AX|² = [numerator] / sin²γ = [b²(a+b)²(a² - ab + b²) / (2D²)] / [S/(2D)]
= b²(a+b)²(a² - ab + b²) / (2D²) · 2D/S
= b²(a+b)²(a² - ab + b²) / (DS)

where D = a² + ab + b² and S = a² + b².

Note that a² - ab + b² = D - 2ab. Also, D = S + ab.

So |AX|² = b²(a+b)²(D - 2ab) / (D · S)

|AX| = b(a+b) √[(D - 2ab)/(DS)] = b(a+b) √(D - 2ab) / √(DS)

Similarly, |BY|² = [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ] / sin²γ

By symmetry (swapping a and b):
|BY|² = a²(a+b)²(D - 2ab) / (DS)

|BY| = a(a+b) √(D - 2ab) / √(DS)

Let me verify the condition a|AX| = b|BY|:
a · b(a+b)√(D-2ab)/√(DS) = b · a(a+b)√(D-2ab)/√(DS). ✓ (Both sides equal.)

Now, t such that |AX| = bt:
bt = b(a+b)√(D-2ab)/√(DS)
t = (a+b)√(D-2ab)/√(DS)

AP + BQ = (a² + b²)t / (a+b) = S · (a+b)√(D-2ab) / [(a+b)√(DS)] = S√(D-2ab) / √(DS)

= S √(D - 2ab) / √(D · S) = √S · √(D - 2ab) / √D = √[S(D - 2ab)/D]

where S = a² + b², D = a² + ab + b², D - 2ab = a² - ab + b².

AP + BQ = √[(a² + b²)(a² - ab + b²) / (a² + ab + b²)]

Now, CH = c cot C. We have c² = a² + b² - 2ab cos C = a² + b² - 2ab cos(2γ).

cos(2γ) = ab/D, so c² = S - 2ab · ab/D = S - 2a²b²/D = (SD - 2a²b²)/D.

SD = (a² + b²)(a² + ab + b²) = a⁴ + a³b + a²b² + a²b² + ab³ + b⁴ = a⁴ + a³b + 2a²b² + ab³ + b⁴

SD - 2a²b² = a⁴ + a³b + ab³ + b⁴ = a³(a + b) + b³(a + b) = (a + b)(a³ + b³) = (a + b)²(a² - ab + b²)

So c² = (a+b)²(a² - ab + b²) / D = (a+b)²(D - 2ab) / D

c = (a+b)√(D - 2ab) / √D

CH = c cot C = c · cos(2γ)/sin(2γ) = c · cos(2γ) / (2 sin γ cos γ)

sin(2γ) = 2 sin γ cos γ. sin²γ = S/(2D), cos²γ = (a+b)²/(2D).
sin γ cos γ = √[S(a+b)²/(4D²)] = (a+b)√S / (2D)
sin(2γ) = 2 · (a+b)√S / (2D) = (a+b)√S / D

cos(2γ) = ab/D

cot C = cot(2γ) = cos(2γ)/sin(2γ) = (ab/D) / ((a+b)√S/D) = ab / ((a+b)√S)

CH = c · cot C = [(a+b)√(D-2ab)/√D] · [ab/((a+b)√S)] = ab√(D-2ab) / (√D · √S) = ab√(D-2ab) / √(DS)

Now, the ratio:
(AP + BQ) / CH = √[S(D-2ab)/D] / [ab√(D-2ab)/√(DS)]
= √[S(D-2ab)/D] · √(DS) / [ab√(D-2ab)]
= √[S(D-2ab) · DS / D] / [ab√(D-2ab)]
= √[S²(D-2ab)] / [ab√(D-2ab)]
= S√(D-2ab) / [ab√(D-2ab)]
= S / (ab)
= (a² + b²) / (ab)

So (AP + BQ) / CH = (a² + b²) / (ab) = a/b + b/a.

By AM-GM, a/b + b/a ≥ 2, with equality when a = b. But a ≠ b (given AC ≠ BC), so the ratio is strictly > 2.

But we need the infimum. As a/b → 1 (but a ≠ b), the ratio approaches 2. So the infimum is 2, but it's not achieved.

Wait, but the problem asks for the largest k such that AP + BQ ≥ k · CH always holds. If the ratio (AP+BQ)/CH = a/b + b/a > 2 always (with equality only in the limit a → b), then k = 2.

But wait, we need to check that the infimum is indeed 2 and is approached. As a → b, the ratio → 2. But we also need to check that the triangle remains valid (acute, with the condition PX = QY satisfied, and P, Q on the segments).

Let me verify: when a → b, the condition tan²γ = (a² + b²)/(a+b)² → 2a²/(4a²) = 1/2, so γ → arctan(1/√2), C = 2γ → 2 arctan(1/√2). 

arctan(1/√2) ≈ 35.26°, so C ≈ 70.53°. This is less than 90°, so the triangle can be acute.

Also, we need |a - b|/(a+b) ≤ tan²γ. When a ≈ b, |a-b|/(a+b) → 0 ≤ 1/2 = tan²γ. ✓

And we need the triangle to be acute: all angles < 90°. C ≈ 70.53° < 90°. We also need A < 90° and B < 90°. By the law of sines, a/sin A = b/sin B = c/sin C. When a ≈ b, A ≈ B ≈ (180° - 70.53°)/2 ≈ 54.74° < 90°. ✓

So as a → b (with a ≠ b), the ratio (AP + BQ)/CH → 2, and all conditions are satisfied. The infimum is 2, approached but never achieved.

Therefore k = 2.

Wait, but I should double-check. The problem says "the largest real number k such that AP + BQ ≥ k · CH always holds." If the ratio is always > 2 but approaches 2, then for k = 2, the inequality AP + BQ ≥ 2 · CH always holds (strictly), and for any k > 2, there exists a triangle where AP + BQ < k · CH. So k = 2.

Let me verify with a specific numerical example. Let me take a = 2, b = 1 (so a ≠ b).

Condition: tan²γ = (4 + 1)/(3)² = 5/9, tan γ = √5/3.
γ = arctan(√5/3) ≈ arctan(0.745) ≈ 36.7°
C = 2γ ≈ 73.4°

Check acute: C ≈ 73.4° < 90°. 
c² = (a+b)²(D - 2ab)/D where D = 4 + 2 + 1 = 7, D - 2ab = 7 - 4 = 3.
c² = 9 · 3 / 7 = 27/7, c = √(27/7) ≈ 1.964.

sin A = a sin C / c. sin C = sin(73.4°) ≈ 0.958. sin A ≈ 2 · 0.958 / 1.964 ≈ 0.976. A ≈ 77.4° < 90°. ✓
sin B = b sin C / c ≈ 1 · 0.958 / 1.964 ≈ 0.488. B ≈ 29.2° < 90°. ✓

Ratio = (a² + b²)/(ab) = 5/2 = 2.5.

Let me try a = 1.1, b = 1:
Ratio = (1.21 + 1)/(1.1) = 2.21/1.1 = 2.009...

Approaching 2. ✓

So k = 2.

Let me also verify the whole computation with the numerical example a = 2, b = 1.

tan²γ = 5/9, sin²γ = 5/14, cos²γ = 9/14, cos(2γ) = cos²γ - sin²γ = 4/14 = 2/7.

D = a² + ab + b² = 4 + 2 + 1 = 7.
S = a² + b² = 5.
D - 2ab = 7 - 4 = 3.

c² = (a+b)²(D-2ab)/D = 9 · 3/7 = 27/7.
CH = ab√(D-2ab)/√(DS) = 2·1·√3/√(7·5) = 2√3/√35 = 2√(3/35) = 2√(3/35).

AP + BQ = √[S(D-2ab)/D] = √[5·3/7] = √(15/7).

Ratio = √(15/7) / (2√(3/35)) = √(15/7) / (2√3/√35) = √(15/7) · √35 / (2√3) = √(15·35/(7·3)) / 2 = √(525/21) / 2 = √25 / 2 = 5/2 = 2.5. ✓

Great, this confirms the ratio is (a² + b²)/(ab) = 5/2.

So the answer is k = 2.

Let me write up the proof.

Actually, let me make sure I haven't made an error in identifying the external bisector. Let me re-examine.

The angle AHB = π - C. The rays from H to A and H to B point in directions (-cos γ, sin γ) and (cos γ, sin γ) respectively (both pointing upward, one left and one right). The angle between them (opening upward) is π - C.

The internal bisector of this angle is the upward vertical direction (0, 1), which bisects the angle π - C.

The external bisector is perpendicular to the internal bisector, so it's horizontal. The external bisector of angle AHB is the horizontal line through H.

This is correct. The external bisector bisects the external (reflex) angle, which opens downward. Its bisector is horizontal.

Now let me also verify that P is indeed between A and X (on the segment) for our numerical example.

a = 2, b = 1, γ = arctan(√5/3).
A = (-b sin γ, b cos γ) = (-sin γ, cos γ)
X = (-a cos(2γ)/sin γ, 0) = (-2 · (2/7) / sin γ, 0) = (-4/(7 sin γ), 0)

sin γ = √(5/14), so X = (-4/(7·√(5/14)), 0) = (-4√(14/5)/7, 0) = (-4√14/(7√5), 0) = (-4√70/35, 0)

A = (-√(5/14), √(9/14)) = (-√5/√14, 3/√14)

u = b/(a+b) = 1/3.
P = A + (1/3)(X - A).
P_y = A_y + (1/3)(0 - A_y) = (2/3)A_y = (2/3)(3/√14) = 2/√14.

H_y = (a+b)cos(2γ)/(2cos γ) = 3·(2/7)/(2·3/√14) = (6/7)/(6/√14) = √14/7 = √14/7.
2/√14 = 2√14/14 = √14/7. ✓ P_y = H_y.

P_x = A_x + (1/3)(X_x - A_x) = -√5/√14 + (1/3)(-4√70/35 + √5/√14)

Let me compute X_x - A_x = -4√70/35 + √5/√14 = -4√70/35 + √5·√14/14 = -4√70/35 + √70/14

= √70(-4/35 + 1/14) = √70(-8/70 + 5/70) = √70(-3/70) = -3√70/70 = -3√70/70

P_x = -√5/√14 + (1/3)(-3√70/70) = -√5/√14 - √70/70 = -√5√14/14 - √70/70 = -√70/14 - √70/70 = -√70(1/14 + 1/70) = -√70(5/70 + 1/70) = -6√70/70 = -3√70/35

Is this between A_x = -√5/√14 = -√70/14 = -5√70/70 and X_x = -4√70/35 = -8√70/70?

P_x = -3√70/35 = -6√70/70. A_x = -5√70/70, X_x = -8√70/70.

-8√70/70 ≤ -6√70/70 ≤ -5√70/70? -8 ≤ -6 ≤ -5? Yes! ✓ P is between A and X.

Great. Now let me also verify Q.

v = a/(a+b) = 2/3.
B = (a sin γ, a cos γ) = (2√(5/14), 2·3/√14) = (2√5/√14, 6/√14)
Y = (b cos(2γ)/sin γ, 0) = ((2/7)/√(5/14), 0) = (2√(14/5)/7, 0) = (2√70/35, 0)

Q = B + (2/3)(Y - B).
Q_y = B_y + (2/3)(0 - B_y) = (1/3)B_y = (1/3)(6/√14) = 2/√14 = √14/7 = H_y. ✓

Q_x = B_x + (2/3)(Y_x - B_x) = 2√5/√14 + (2/3)(2√70/35 - 2√5/√14)

Y_x - B_x = 2√70/35 - 2√70/14 = 2√70(1/35 - 1/14) = 2√70(2/70 - 5/70) = 2√70(-3/70) = -6√70/70 = -3√70/35

Q_x = 2√70/14 + (2/3)(-3√70/35) = √70/7 - 2√70/35 = √70(5/35 - 2/35) = 3√70/35

Is this between B_x = 2√70/14 = 5√70/35 and Y_x = 2√70/35?
2√70/35 ≤ 3√70/35 ≤ 5√70/35? 2 ≤ 3 ≤ 5? Yes! ✓ Q is between B and Y.

Everything checks out. The answer is k = 2.

Now let me write a clean proof.

**Proof:**

Set up coordinates with C at the origin, the internal bisector of angle C along the positive y-axis, and the external bisector of angle C along the x-axis. Let angle C = 2γ (so 0 < γ < π/4 for an acute triangle). Let BC = a, CA = b with a ≠ b.

Then:
- A = (-b sin γ, b cos γ)
- B = (a sin γ, a cos γ)

The altitude from A (perpendicular to BC, direction (cos γ, -sin γ)) meets the x-axis at:
Y = (b cos 2γ / sin γ, 0)

The altitude from B (perpendicular to AC, direction (cos γ, sin γ)) meets the x-axis at:
X = (-a cos 2γ / sin γ, 0)

The orthocenter is:
H = ((b-a) cos 2γ / (2 sin γ), (a+b) cos 2γ / (2 cos γ))

The rays HA and HB point in directions (-cos γ, sin γ) and (cos γ, sin γ) respectively, so the internal bisector of angle AHB is vertical and the **external bisector** is the horizontal line y = H_y = (a+b) cos 2γ / (2 cos γ).

**Finding P and Q:** P is on segment AX with P_y = H_y, giving parameter u = b/(a+b) (after applying the condition below). Q is on segment BY with Q_y = H_y, giving v = a/(a+b).

**Condition PX = QY:** Computing (1-u)|AX| = (1-v)|BY| and simplifying yields:
(a² + b²) cos 2γ = 2ab sin²γ
equivalently: tan²γ = (a² + b²)/(a+b)².

**Computing the ratio:** Under this condition, with D = a² + ab + b², S = a² + b²:
- |AX|² = b²(a+b)²(D - 2ab)/(DS), |BY|² = a²(a+b)²(D - 2ab)/(DS)
- AP + BQ = √[S(D - 2ab)/D]
- CH = ab√(D - 2ab)/√(DS)

Therefore:
(AP + BQ)/CH = S/(ab) = (a² + b²)/(ab) = a/b + b/a

By AM-GM, a/b + b/a ≥ 2 with equality iff a = b. Since a ≠ b, the ratio is strictly > 2, but approaches 2 as a → b. The limiting case a → b gives a valid acute triangle (C → 2 arctan(1/√2) ≈ 70.5°), so the infimum is 2.

Therefore k = 2.

### PROOF COMPLETE

Wait, I need to be more careful about the proof. Let me make sure the derivation of u = b/(a+b) under the condition is clear, and that I properly show the condition PX = QY leads to tan²γ = (a²+b²)/(a+b)².

Let me also double-check: the problem says "the largest real number k such that AP + BQ ≥ k·CH always holds." This means k = inf{(AP+BQ)/CH} over all valid configurations. We showed (AP+BQ)/CH = a/b + b/a > 2, with inf = 2. So k = 2.

Let me write the proof more carefully.

Actually, I realize I should double-check the formula for AP + BQ more carefully. Let me recompute.

Under the condition, u = b/(a+b) and v = a/(a+b).

AP = u · |AX| = (b/(a+b)) · |AX|
BQ = v · |BY| = (a/(a+b)) · |BY|

From the condition a|AX| = b|BY|, we get |BY| = a|AX|/b.

AP + BQ = (b/(a+b))|AX| + (a/(a+b)) · (a|AX|/b) = |AX|/(a+b) · (b + a²/b) = |AX|/(a+b) · (b² + a²)/b = |AX| · S / (b(a+b))

And |AX| = b(a+b)√(D-2ab)/√(DS), so:
AP + BQ = b(a+b)√(D-2ab)/√(DS) · S/(b(a+b)) = S√(D-2ab)/√(DS) = √(S²(D-2ab)/(DS)) = √(S(D-2ab)/D). ✓

CH = c · cot C. c² = (a+b)²(D-2ab)/D, so c = (a+b)√(D-2ab)/√D.
cot C = cot(2γ) = cos(2γ)/sin(2γ).
cos(2γ) = ab/D.
sin(2γ) = 2sinγ cosγ. sin²γ = S/(2D), cos²γ = (a+b)²/(2D).
sin(2γ) = 2√(S(a+b)²/(4D²)) = (a+b)√S/D.
cot C = (ab/D)/((a+b)√S/D) = ab/((a+b)√S).

CH = (a+b)√(D-2ab)/√D · ab/((a+b)√S) = ab√(D-2ab)/(√D·√S) = ab√(D-2ab)/√(DS). ✓

Ratio = √(S(D-2ab)/D) / (ab√(D-2ab)/√(DS)) = √(S(D-2ab)/D) · √(DS)/(ab√(D-2ab)) = √(S(D-2ab)·DS/D)/(ab√(D-2ab)) = √(S²(D-2ab))/(ab√(D-2ab)) = S√(D-2ab)/(ab√(D-2ab)) = S/(ab) = (a²+b²)/(ab). ✓

The proof is correct. k = 2.        — AI历史解题过程（thinking）
#   polymath_05464         — 题目ID

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
  <problem_id>polymath_05464</problem_id>
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

An acute triangle $ABC$ is given, $AC \not= BC$. The altitudes drawn from $A$ and $B$ meet at $H$ and intersect the external bisector of the angle $C$ at $Y$ and $X$ respectively. The external bisector of the angle $AHB$ meets the segments $AX$ and $BY$ at $P$ and $Q$ respectively. It is known that $PX = QY$. Let $k$ be the largest real number such that the inequality $AP + BQ \ge k \cdot CH$ always holds. Find the value of $k$.

## Standard Solution

In the original problem, it is proven that for an acute triangle $ABC$ with $AC \neq BC$ and $PX = QY$, the relationship $AP + BQ \ge 2CH$ holds. The proof uses the fact that $XDEY$ (where $P, Q$ are $D, E$) is a parallelogram, leading to $AD \cdot BE = XD^2$ (or $AP \cdot BQ = PX^2$). It is also shown that $CH = PX$ by demonstrating that $CHPX$ is an isosceles trapezoid. Applying the AM-GM inequality, $AP + BQ \ge 2\sqrt{AP \cdot BQ} = 2PX = 2CH$. The equality occurs in the limit as the triangle approaches an isosceles configuration, meaning $k=2$ is the sharpest constant.

## AI's Thinking (Attempted Solution Process)

Let me work through this problem carefully.

We have an acute triangle ABC with AC ≠ BC. Altitudes from A and B meet at H (orthocenter). The external bisector of angle C intersects the altitude from A at Y and the altitude from B at X. The external bisector of angle AHB meets segments AX and BY at P and Q respectively. Given PX = QY. Find the largest k such that AP + BQ ≥ k·CH always holds.

Let me set up coordinates. Let me think about this geometrically first.

The altitudes from A and B: altitude from A is perpendicular to BC, altitude from B is perpendicular to AC. They meet at H, the orthocenter.

The external bisector of angle C: this is the line through C that bisects the external angle at C.

The external bisector of angle AHB: angle AHB = π - C (since in a triangle, the orthocenter creates angle AHB = π - C). The external bisector of angle AHB bisects the external angle at H.

Let me use coordinates. Place C at the origin. Let the external bisector of angle C be a convenient axis.

Actually, let me think about the external bisector of angle C. The internal bisector of angle C bisects angle ACB. The external bisector is perpendicular to the internal bisector.

Let me set up coordinates with C at origin, and the external bisector of angle C along the x-axis. Then the internal bisector of angle C is along the y-axis.

Let angle C = 2γ. Then CA makes angle (π/2 - γ) with the x-axis... wait, let me think more carefully.

If the external bisector of C is the x-axis, then the two sides CA and CB are symmetric with respect to... no. The external bisector bisects the external angle. The internal bisector bisects the internal angle. They are perpendicular.

Let me place C at origin. Let the internal bisector of angle C point in the direction of angle 0 (positive x-axis), and the external bisector point in the direction π/2 (positive y-axis). Wait, let me just pick the external bisector as the x-axis for convenience since the problem involves the external bisector of C heavily.

Let the external bisector of angle C be the x-axis, with C at origin. Then the internal bisector of angle C is the y-axis.

Let angle C = 2γ (where 0 < γ < π/2 since triangle is acute, so C < π/2... wait, acute means all angles < π/2, so C < π/2, thus γ < π/4).

The sides CA and CB make angles with the internal bisector. CA makes angle γ with the internal bisector (y-axis), and CB makes angle -γ with the internal bisector. So relative to the x-axis (external bisector):
- CA direction: angle (π/2 - γ) from x-axis... 

Hmm, let me reconsider. If internal bisector is along positive y-axis, then CA is at angle (π/2 + γ) from positive x-axis and CB is at angle (π/2 - γ) from positive x-axis. Wait, that's not right either. Let me be more careful.

The internal bisector of angle C bisects the angle between CA and CB. If the internal bisector is the positive y-axis, then CA and CB are symmetric about the y-axis. CA is at angle (π/2 + γ) and CB is at angle (π/2 - γ) from the positive x-axis. So angle ACB = 2γ. Good.

The external bisector of angle C is perpendicular to the internal bisector, so it's the x-axis. Good.

Now, let's say CA = b and CB = a (standard notation: a = BC, b = CA, c = AB).

A is at distance b from C along direction (π/2 + γ):
A = (b cos(π/2 + γ), b sin(π/2 + γ)) = (-b sin γ, b cos γ)

B is at distance a from C along direction (π/2 - γ):
B = (a cos(π/2 - γ), a sin(π/2 - γ)) = (a sin γ, a cos γ)

C = (0, 0).

Now, the altitude from A is perpendicular to BC. Direction of BC: from B to C is (-a sin γ, -a cos γ), so BC direction is (sin γ, cos γ) (from C to B). The altitude from A is perpendicular to BC, so its direction is perpendicular to (sin γ, cos γ), which is (cos γ, -sin γ) or (-cos γ, sin γ).

The altitude from A passes through A = (-b sin γ, b cos γ) with direction (cos γ, -sin γ):
Parametrically: (-b sin γ + t cos γ, b cos γ - t sin γ)

Similarly, altitude from B is perpendicular to AC. Direction of AC: from C to A is (-b sin γ, b cos γ), so direction is (-sin γ, cos γ). Perpendicular direction: (cos γ, sin γ) or (-cos γ, -sin γ).

Altitude from B passes through B = (a sin γ, a cos γ) with direction (cos γ, sin γ):
Parametrically: (a sin γ + s cos γ, a cos γ + s sin γ)

Orthocenter H: intersection of the two altitudes.
From altitude A: (-b sin γ + t cos γ, b cos γ - t sin γ)
From altitude B: (a sin γ + s cos γ, a cos γ + s sin γ)

Setting equal:
-b sin γ + t cos γ = a sin γ + s cos γ ... (1)
b cos γ - t sin γ = a cos γ + s sin γ ... (2)

From (1): t cos γ - s cos γ = (a + b) sin γ → (t - s) cos γ = (a + b) sin γ → t - s = (a + b) tan γ

From (2): -t sin γ - s sin γ = (a - b) cos γ → -(t + s) sin γ = (a - b) cos γ → t + s = -(a - b) cos γ / sin γ = (b - a) / tan γ

So:
t = [(a+b) tan γ + (b-a)/tan γ] / 2
s = [(b-a)/tan γ - (a+b) tan γ] / 2

Let me compute H coordinates using altitude from A:
H_x = -b sin γ + t cos γ
H_y = b cos γ - t sin γ

t cos γ = [(a+b) tan γ + (b-a)/tan γ] cos γ / 2 = [(a+b) sin γ + (b-a) cos²γ/sin γ] / 2

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me use the known formula for the orthocenter. In a triangle with C at origin:
H = A + B - (projection stuff)... actually, let me just use the formula.

For a triangle with vertices A, B, C, the orthocenter H satisfies:
H = A + B + C - 2O where O is the circumcenter. That's not quite right.

Actually, let me just compute H directly. We know that in the coordinate system with C at origin:
The altitude from A is perpendicular to BC. BC has direction (a sin γ, a cos γ) - (0,0) = (sin γ, cos γ) (unit direction since a cancels). So altitude from A: point A + t(cos γ, -sin γ).

The altitude from B is perpendicular to AC. AC has direction (-b sin γ, b cos γ), unit direction (-sin γ, cos γ). So altitude from B: point B + s(cos γ, sin γ).

Let me find H by solving:
A + t(cos γ, -sin γ) = B + s(cos γ, sin γ)

(-b sin γ + t cos γ, b cos γ - t sin γ) = (a sin γ + s cos γ, a cos γ + s sin γ)

From x: t cos γ - s cos γ = (a + b) sin γ → t - s = (a+b) sin γ / cos γ = (a+b) tan γ
From y: -t sin γ - s sin γ = (a - b) cos γ → t + s = (b-a) cos γ / sin γ = (b-a)/tan γ

So t = [(a+b) tan γ + (b-a)/tan γ]/2, s = [(b-a)/tan γ - (a+b) tan γ]/2

H_x = -b sin γ + t cos γ = -b sin γ + [(a+b) sin γ + (b-a) cos²γ/sin γ]/2
= -b sin γ + (a+b) sin γ/2 + (b-a) cos²γ/(2 sin γ)
= sin γ[-b + (a+b)/2] + (b-a) cos²γ/(2 sin γ)
= sin γ[(a-b)/2] + (b-a) cos²γ/(2 sin γ)
= (a-b)/2 [sin γ - cos²γ/sin γ]
= (a-b)/2 [(sin²γ - cos²γ)/sin γ]
= (a-b)/2 [-cos(2γ)/sin γ]
= -(a-b) cos(2γ)/(2 sin γ)
= (b-a) cos(2γ)/(2 sin γ)

H_y = b cos γ - t sin γ = b cos γ - [(a+b) sin²γ/cos γ + (b-a) cos γ]/2... 

wait let me redo:
t sin γ = [(a+b) tan γ + (b-a)/tan γ] sin γ / 2 = [(a+b) sin²γ/cos γ + (b-a) cos γ] / 2

H_y = b cos γ - [(a+b) sin²γ/cos γ + (b-a) cos γ]/2
= b cos γ - (a+b) sin²γ/(2 cos γ) - (b-a) cos γ/2
= cos γ [b - (b-a)/2] - (a+b) sin²γ/(2 cos γ)
= cos γ [(2b - b + a)/2] - (a+b) sin²γ/(2 cos γ)
= cos γ (a+b)/2 - (a+b) sin²γ/(2 cos γ)
= (a+b)/2 [cos γ - sin²γ/cos γ]
= (a+b)/2 [(cos²γ - sin²γ)/cos γ]
= (a+b)/2 [cos(2γ)/cos γ]
= (a+b) cos(2γ)/(2 cos γ)

So H = ((b-a) cos(2γ)/(2 sin γ), (a+b) cos(2γ)/(2 cos γ))

Since the triangle is acute, the orthocenter is inside the triangle, so H_y > 0, which means cos(2γ) > 0, i.e., γ < π/4, i.e., C = 2γ < π/2. Good, consistent with acute triangle.

Now, CH = distance from C=(0,0) to H:
CH² = [(b-a) cos(2γ)/(2 sin γ)]² + [(a+b) cos(2γ)/(2 cos γ)]²
= cos²(2γ)/4 [(b-a)²/sin²γ + (a+b)²/cos²γ]
= cos²(2γ)/4 [(b-a)² cos²γ + (a+b)² sin²γ]/(sin²γ cos²γ)

Let me compute (b-a)² cos²γ + (a+b)² sin²γ:
= (b²-2ab+a²)cos²γ + (a²+2ab+b²)sin²γ
= a²(cos²γ+sin²γ) + b²(cos²γ+sin²γ) + 2ab(sin²γ - cos²γ)
= a² + b² - 2ab cos(2γ)

So CH² = cos²(2γ)(a² + b² - 2ab cos(2γ))/(4 sin²γ cos²γ)

Note that by the law of cosines, c² = a² + b² - 2ab cos(C) = a² + b² - 2ab cos(2γ). So:

CH² = cos²(2γ) c² / (4 sin²γ cos²γ) = c² cos²(2γ) / sin²(2γ) = c² / tan²(2γ) = c² cot²(C)

So CH = c cot(C) = c · cos(C)/sin(C). This is a known formula: CH = c cot C. Actually, let me verify: the distance from C to the orthocenter is indeed c·cot(C)... hmm, actually I recall the formula is CH = 2R cos C where R is the circumradius. And c = 2R sin C. So CH = 2R cos C = c cos C / sin C = c cot C. Yes, consistent!

Good. So CH = c cot C where C = 2γ.

Now let's find X and Y. The external bisector of angle C is the x-axis (y = 0).

X is the intersection of the altitude from B with the x-axis (external bisector of C).
Altitude from B: (a sin γ + s cos γ, a cos γ + s sin γ)
Set y = 0: a cos γ + s sin γ = 0 → s = -a cos γ / sin γ = -a / tan γ
X_x = a sin γ + s cos γ = a sin γ - a cos²γ / sin γ = a(sin²γ - cos²γ)/sin γ = -a cos(2γ)/sin γ
X = (-a cos(2γ)/sin γ, 0)

Y is the intersection of the altitude from A with the x-axis.
Altitude from A: (-b sin γ + t cos γ, b cos γ - t sin γ)
Set y = 0: b cos γ - t sin γ = 0 → t = b cos γ / sin γ = b / tan γ
Y_x = -b sin γ + t cos γ = -b sin γ + b cos²γ / sin γ = b(cos²γ - sin²γ)/sin γ = b cos(2γ)/sin γ
Y = (b cos(2γ)/sin γ, 0)

So X and Y are on the x-axis (external bisector of C), with:
X = (-a cos(2γ)/sin γ, 0)
Y = (b cos(2γ)/sin γ, 0)

XY = (a + b) cos(2γ)/sin γ (distance, since cos(2γ) > 0 for acute triangle).

Now, the external bisector of angle AHB. Angle AHB = π - C = π - 2γ. The external bisector of angle AHB bisects the external angle at H.

The external angle at H is 2γ (since internal angle is π - 2γ, external is 2γ). The external bisector bisects this into two angles of γ each.

Hmm, I need to find the direction of the external bisector of angle AHB. Let me think about this.

The angle AHB is the angle at H in triangle AHB. The sides HA and HB go from H to A and H to B respectively.

Direction from H to A: A - H = (-b sin γ, b cos γ) - ((b-a) cos(2γ)/(2 sin γ), (a+b) cos(2γ)/(2 cos γ))

This is getting complicated. Let me think of another approach.

Actually, the external bisector of angle AHB. Note that angle AHB = π - C. The internal bisector of angle AHB and the external bisector are perpendicular.

There's a nice property: the internal bisector of angle AHB passes through... hmm. Actually, in the orthocenter configuration, the bisectors of angle AHB have nice properties. The internal bisector of angle AHB is related to the bisector of angle C.

Let me think about this differently. The angle AHB = π - C. The internal bisector of angle AHB bisects the angle π - C, creating angles of (π-C)/2 = π/2 - C/2 = π/2 - γ. The external bisector is perpendicular to the internal bisector.

Actually, I recall that the internal bisector of angle AHB is parallel to the internal bisector of angle C (or the external bisector of angle C). Let me verify.

The altitude from A is perpendicular to BC, and the altitude from B is perpendicular to AC. The angle between the altitudes (which is angle AHB) equals π - C (since the angle between two lines perpendicular to two sides equals the supplement of the angle between those sides).

The internal bisector of angle AHB: since the altitudes are perpendicular to BC and AC respectively, the bisector of the angle between the altitudes is perpendicular to the bisector of the angle between BC and AC (which is angle C). Wait, not exactly.

If two lines L1, L2 meet at angle θ, and two other lines M1 ⊥ L1, M2 ⊥ L2 meet at angle π - θ, then the bisector of the angle between M1, M2 is perpendicular to the bisector of the angle between L1, L2. 

The altitudes from A and B are perpendicular to BC and AC respectively. The angle between BC and AC is C. The angle between the altitudes is π - C. The bisector of angle C (internal bisector of C) and the bisector of the angle between the altitudes (internal bisector of angle AHB) are perpendicular.

So: internal bisector of angle AHB ⊥ internal bisector of angle C.

Since the internal bisector of angle C is the y-axis (in our coordinates), the internal bisector of angle AHB is horizontal, i.e., parallel to the x-axis, which is the external bisector of angle C.

And the external bisector of angle AHB is perpendicular to the internal bisector of angle AHB, so it's vertical, i.e., parallel to the y-axis, which is the internal bisector of angle C.

So the external bisector of angle AHB is a vertical line (parallel to y-axis) passing through H.

The external bisector of angle AHB is the vertical line x = H_x = (b-a) cos(2γ)/(2 sin γ).

Now, P is the intersection of this vertical line with segment AX, and Q is the intersection with segment BY.

Let me find P on segment AX.
A = (-b sin γ, b cos γ)
X = (-a cos(2γ)/sin γ, 0)

Parametrize AX: A + u(X - A) for u ∈ [0, 1].
X - A = (-a cos(2γ)/sin γ + b sin γ, -b cos γ)

x-coordinate: -b sin γ + u(-a cos(2γ)/sin γ + b sin γ)
Set this equal to H_x = (b-a) cos(2γ)/(2 sin γ):

-b sin γ + u(-a cos(2γ)/sin γ + b sin γ) = (b-a) cos(2γ)/(2 sin γ)

Let me compute -a cos(2γ)/sin γ + b sin γ:
= [-a cos(2γ) + b sin²γ] / sin γ
= [-a(cos²γ - sin²γ) + b sin²γ] / sin γ
= [-a cos²γ + a sin²γ + b sin²γ] / sin γ
= [-a cos²γ + (a+b) sin²γ] / sin γ

So:
u · [-a cos²γ + (a+b) sin²γ] / sin γ = (b-a) cos(2γ)/(2 sin γ) + b sin γ
= [(b-a) cos(2γ) + 2b sin²γ] / (2 sin γ)
= [(b-a)(cos²γ - sin²γ) + 2b sin²γ] / (2 sin γ)
= [(b-a) cos²γ - (b-a) sin²γ + 2b sin²γ] / (2 sin γ)
= [(b-a) cos²γ + (a+b) sin²γ] / (2 sin γ)

So:
u = [(b-a) cos²γ + (a+b) sin²γ] / (2 [-a cos²γ + (a+b) sin²γ])

Hmm, this is getting messy. Let me denote for convenience:
Let p = cos²γ, q = sin²γ. Note p + q = 1, p - q = cos(2γ).

Then:
Numerator of u: (b-a)p + (a+b)q = bp - ap + aq + bq = b(p+q) + a(q-p) = b - a cos(2γ)
Denominator of u: 2[-ap + (a+b)q] = 2[-ap + aq + bq] = 2[a(q-p) + bq] = 2[-a cos(2γ) + bq]

So u = [b - a cos(2γ)] / [2(bq - a cos(2γ))] = [b - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]

Let me also compute the y-coordinate of P:
P_y = b cos γ + u(0 - b cos γ) = b cos γ (1 - u) = b cos γ · [1 - (b - a cos(2γ))/(2(b sin²γ - a cos(2γ)))]
= b cos γ · [2(b sin²γ - a cos(2γ)) - (b - a cos(2γ))] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [2b sin²γ - 2a cos(2γ) - b + a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [2b sin²γ - b - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [b(2 sin²γ - 1) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [-b cos(2γ) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= b cos γ · [-(a+b) cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= -b(a+b) cos(2γ) cos γ / [2(b sin²γ - a cos(2γ))]

And P_x = H_x = (b-a) cos(2γ)/(2 sin γ).

Similarly, let me find Q on segment BY.
B = (a sin γ, a cos γ)
Y = (b cos(2γ)/sin γ, 0)

Parametrize BY: B + v(Y - B) for v ∈ [0, 1].
Y - B = (b cos(2γ)/sin γ - a sin γ, -a cos γ)

x-coordinate: a sin γ + v(b cos(2γ)/sin γ - a sin γ)
Set equal to H_x = (b-a) cos(2γ)/(2 sin γ):

a sin γ + v(b cos(2γ)/sin γ - a sin γ) = (b-a) cos(2γ)/(2 sin γ)

b cos(2γ)/sin γ - a sin γ = [b cos(2γ) - a sin²γ] / sin γ = [b(p-q) - aq] / sin γ = [bp - bq - aq] / sin γ = [bp - (a+b)q] / sin γ

So:
v · [bp - (a+b)q] / sin γ = (b-a)(p-q)/(2 sin γ) - a sin γ
= [(b-a)(p-q) - 2aq] / (2 sin γ)
= [(b-a)(p-q) - 2aq] / (2 sin γ)
= [bp - bq - ap + aq - 2aq] / (2 sin γ)
= [bp - bq - ap - aq] / (2 sin γ)
= [b(p-q) - a(p+q)] / (2 sin γ)
= [b cos(2γ) - a] / (2 sin γ)

So:
v = [b cos(2γ) - a] / [2(bp - (a+b)q)]
= [b cos(2γ) - a] / [2(b cos²γ - (a+b) sin²γ)]

Q_y = a cos γ + v(0 - a cos γ) = a cos γ (1 - v)
= a cos γ · [2(b cos²γ - (a+b) sin²γ) - (b cos(2γ) - a)] / [2(b cos²γ - (a+b) sin²γ)]
= a cos γ · [2b cos²γ - 2(a+b) sin²γ - b cos(2γ) + a] / [2(b cos²γ - (a+b) sin²γ)]

Let me simplify the numerator:
2b cos²γ - 2(a+b) sin²γ - b(cos²γ - sin²γ) + a
= 2bp - 2(a+b)q - b(p-q) + a
= 2bp - 2aq - 2bq - bp + bq + a
= bp - bq - 2aq + a
= b(p-q) + a(1 - 2q)
= b cos(2γ) + a(p - q)  [since 1 - 2q = 1 - 2sin²γ = cos(2γ) = p - q]
= b cos(2γ) + a cos(2γ)
= (a+b) cos(2γ)

So Q_y = a cos γ · (a+b) cos(2γ) / [2(b cos²γ - (a+b) sin²γ)]
= a(a+b) cos(2γ) cos γ / [2(b cos²γ - (a+b) sin²γ)]

Now, P is on segment AX and Q is on segment BY. The problem says the external bisector of angle AHB meets segments AX and BY at P and Q. For P and Q to be on the segments (not extensions), we need u, v ∈ [0, 1].

Now, AP = distance from A to P = u · |AX| (since P = A + u(X-A)).
BQ = distance from B to Q = v · |BY|.

PX = (1-u) · |AX|, QY = (1-v) · |BY|.

The condition PX = QY means (1-u)|AX| = (1-v)|BY|.

Let me compute |AX| and |BY|.

|AX|² = (X_x - A_x)² + (0 - A_y)²
= (-a cos(2γ)/sin γ + b sin γ)² + b² cos²γ

Let me compute -a cos(2γ)/sin γ + b sin γ = [-a cos(2γ) + b sin²γ]/sin γ = [-a(p-q) + bq]/sin γ = [-ap + aq + bq]/sin γ = [-ap + (a+b)q]/sin γ

So |AX|² = [-ap + (a+b)q]²/sin²γ + b² cos²γ
= [-ap + (a+b)q]²/sin²γ + b²p

Let me denote D_A = -ap + (a+b)q = -a cos²γ + (a+b) sin²γ. Then:
|AX|² = D_A²/sin²γ + b² cos²γ = [D_A² + b² cos²γ sin²γ]/sin²γ = [D_A² + b²pq]/sin²γ

D_A² + b²pq = a²p² - 2a(a+b)pq + (a+b)²q² + b²pq
= a²p² + (a+b)²q² + pq[b² - 2a(a+b)]
= a²p² + (a+b)²q² + pq[b² - 2a² - 2ab]
= a²p² + (a² + 2ab + b²)q² + pq[b² - 2a² - 2ab]
= a²p² + a²q² + 2abq² + b²q² + b²pq - 2a²pq - 2abpq
= a²(p² + q² - 2pq) + 2ab(q² - pq) + b²(q² + pq)
= a²(p-q)² + 2abq(q-p) + b²q(p+q)
= a² cos²(2γ) - 2abq cos(2γ) + b²q
= a² cos²(2γ) - 2ab sin²γ cos(2γ) + b² sin²γ

Hmm, let me try to factor this. Let me see if it's a perfect square or something nice.

= a² cos²(2γ) + b² sin²γ - 2ab sin²γ cos(2γ)

Let me check if this equals (a cos(2γ) - b sin²γ... no. Let me try (a cos(2γ) - b sin γ)²... no, that would give a² cos²(2γ) - 2ab sin γ cos(2γ) + b² sin²γ, which has sin γ not sin²γ.

Hmm. Let me try a slightly different approach. Let me use the substitution a = BC, b = CA, and use the angle C = 2γ.

Actually, this algebra is getting very heavy. Let me try a computational/numerical approach to get intuition for the answer, then verify.

Let me pick specific values. Let me try γ = π/6 (so C = π/3 = 60°), and try different a, b.

With C = 60°, cos(2γ) = cos(60°) = 1/2, sin γ = sin(30°) = 1/2, cos γ = cos(30°) = √3/2, sin²γ = 1/4, cos²γ = 3/4.

Let me try a = 3, b = 2 (so AC = 2, BC = 3, AC ≠ BC ✓).

H_x = (b-a) cos(2γ)/(2 sin γ) = (2-3)(1/2)/(2·1/2) = (-1)(1/2)/1 = -1/2
H_y = (a+b) cos(2γ)/(2 cos γ) = 5(1/2)/(2·√3/2) = (5/2)/√3 = 5/(2√3)

CH = √(1/4 + 25/12) = √(3/12 + 25/12) = √(28/12) = √(7/3) = √7/√3

Check: c² = a² + b² - 2ab cos(C) = 9 + 4 - 2·3·2·(1/2) = 13 - 6 = 7, so c = √7.
CH = c cot C = √7 · cot(60°) = √7 · (1/√3) = √7/√3. ✓

X = (-a cos(2γ)/sin γ, 0) = (-3·(1/2)/(1/2), 0) = (-3, 0)
Y = (b cos(2γ)/sin γ, 0) = (2·(1/2)/(1/2), 0) = (2, 0)

A = (-b sin γ, b cos γ) = (-2·(1/2), 2·√3/2) = (-1, √3)
B = (a sin γ, a cos γ) = (3·(1/2), 3·√3/2) = (3/2, 3√3/2)

External bisector of angle AHB: vertical line x = H_x = -1/2.

P on AX: A = (-1, √3), X = (-3, 0).
Direction X - A = (-2, -√3).
P = A + u(X - A) = (-1 - 2u, √3 - √3 u) = (-1 - 2u, √3(1-u))
Set x = -1/2: -1 - 2u = -1/2 → u = -1/4.

Hmm, u = -1/4 < 0, which means P is not on segment AX but on the extension beyond A. That's a problem since the problem says P is on segment AX.

Let me reconsider. Maybe I have the wrong bisector. The problem says "the external bisector of the angle AHB". Let me reconsider which bisector this is.

Angle AHB = π - C. The external bisector of angle AHB bisects the external angle at H. The external angle at H is the supplement, which is C = 2γ. Wait, no. The external angle is π - (π - C) = C. So the external bisector bisects angle C at H.

But I said the external bisector of angle AHB is perpendicular to the internal bisector of angle AHB, and the internal bisector of angle AHB is parallel to the external bisector of angle C (x-axis). So the external bisector of angle AHB is vertical (parallel to y-axis / internal bisector of C). That seems right.

But with a = 3, b = 2, γ = π/6, we get u = -1/4, meaning P is not on segment AX. Let me check if the problem requires specific relationship between a and b for P, Q to be on the segments.

Actually, the problem says "meets the segments AX and BY at P and Q respectively". This implies P is on segment AX and Q is on segment BY. So maybe the condition PX = QY constrains the triangle further, and for those triangles, P and Q are indeed on the segments.

Wait, but the problem says "It is known that PX = QY" — this is a given condition. So we need to find triangles satisfying PX = QY, and for those, find the minimum of (AP + BQ)/CH.

Let me compute PX and QY for the general case and set them equal.

PX = (1 - u)|AX|, QY = (1 - v)|BY|.

Let me compute 1 - u and 1 - v.

1 - u = 1 - [b - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= [2(b sin²γ - a cos(2γ)) - (b - a cos(2γ))] / [2(b sin²γ - a cos(2γ))]
= [2b sin²γ - 2a cos(2γ) - b + a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= [b(2 sin²γ - 1) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= [-b cos(2γ) - a cos(2γ)] / [2(b sin²γ - a cos(2γ))]
= -(a+b) cos(2γ) / [2(b sin²γ - a cos(2γ))]

1 - v = 1 - [b cos(2γ) - a] / [2(b cos²γ - (a+b) sin²γ)]
= [2(b cos²γ - (a+b) sin²γ) - (b cos(2γ) - a)] / [2(b cos²γ - (a+b) sin²γ)]

Numerator: 2b cos²γ - 2(a+b) sin²γ - b cos(2γ) + a
= 2bp - 2(a+b)q - b(p-q) + a
= 2bp - 2aq - 2bq - bp + bq + a
= bp - bq - 2aq + a
= b(p-q) + a(1 - 2q)
= b cos(2γ) + a cos(2γ)
= (a+b) cos(2γ)

So 1 - v = (a+b) cos(2γ) / [2(b cos²γ - (a+b) sin²γ)]

Now, the condition PX = QY:
(1-u)|AX| = (1-v)|BY|

-(a+b) cos(2γ) |AX| / [2(b sin²γ - a cos(2γ))] = (a+b) cos(2γ) |BY| / [2(b cos²γ - (a+b) sin²γ)]

Since (a+b) cos(2γ) > 0 (acute triangle), we can cancel:

-|AX| / (b sin²γ - a cos(2γ)) = |BY| / (b cos²γ - (a+b) sin²γ)

Note that b sin²γ - a cos(2γ) = bq - a(p-q) = bq - ap + aq = (a+b)q - ap = D_A (which we defined earlier).
And b cos²γ - (a+b) sin²γ = bp - (a+b)q = D_B (let's call it).

So: -|AX| / D_A = |BY| / D_B

Since |AX|, |BY| > 0, this means D_A and D_B have opposite signs (or we need to be careful about signs).

Actually, for P to be on segment AX, we need u ∈ [0,1], which requires 1-u ∈ [0,1]. We computed 1-u = -(a+b)cos(2γ)/(2 D_A). Since (a+b)cos(2γ) > 0, we need D_A < 0 for 1-u > 0, i.e., u < 1. And for u > 0, we need... let me check: u = [b - a cos(2γ)]/(2 D_A). For u > 0, we need [b - a cos(2γ)] and D_A to have the same sign.

Similarly for Q: 1-v = (a+b)cos(2γ)/(2 D_B) > 0 requires D_B > 0.

So for P on segment AX: D_A < 0 (for 1-u > 0) and u > 0 (which needs b - a cos(2γ) and D_A same sign, so b - a cos(2γ) < 0, i.e., b < a cos(2γ)).

For Q on segment BY: D_B > 0 (for 1-v > 0) and v > 0 (which needs b cos(2γ) - a and D_B same sign, so b cos(2γ) - a > 0, i.e., b cos(2γ) > a, OR both negative).

Hmm wait, let me reconsider. For P on segment AX, we need 0 ≤ u ≤ 1.
u = [b - a cos(2γ)] / [2 D_A] where D_A = (a+b) sin²γ - a cos²γ = (a+b)q - ap.

And 1 - u = -(a+b) cos(2γ) / [2 D_A].

For 0 ≤ u ≤ 1: need 0 ≤ 1-u ≤ 1, so 0 ≤ -(a+b)cos(2γ)/(2D_A) ≤ 1.
Since (a+b)cos(2γ) > 0, we need D_A < 0 for 1-u ≥ 0.
And 1-u ≤ 1 means -(a+b)cos(2γ)/(2D_A) ≤ 1, i.e., -(a+b)cos(2γ) ≥ 2D_A (since D_A < 0, dividing flips), i.e., (a+b)cos(2γ) ≤ -2D_A = 2(ap - (a+b)q) = 2a cos(2γ) + 2b cos²γ - 2b sin²γ... 

hmm wait: -2D_A = -2[(a+b)q - ap] = 2ap - 2(a+b)q = 2a(p-q) - 2bq = 2a cos(2γ) - 2b sin²γ.

So (a+b)cos(2γ) ≤ 2a cos(2γ) - 2b sin²γ
→ b cos(2γ) ≤ a cos(2γ) - 2b sin²γ
→ b cos(2γ) + 2b sin²γ ≤ a cos(2γ)
→ b[cos(2γ) + 2 sin²γ] ≤ a cos(2γ)
→ b[cos²γ - sin²γ + 2 sin²γ] ≤ a cos(2γ)
→ b[cos²γ + sin²γ] ≤ a cos(2γ)
→ b ≤ a cos(2γ)

So for P on segment AX, we need D_A < 0 and b ≤ a cos(2γ).

D_A < 0: (a+b) sin²γ < a cos²γ, i.e., (a+b) sin²γ < a cos²γ, i.e., b sin²γ < a(cos²γ - sin²γ) = a cos(2γ), i.e., b < a cos(2γ)/sin²γ.

Since cos(2γ)/sin²γ = (cos²γ - sin²γ)/sin²γ = cos²γ/sin²γ - 1 = cot²γ - 1, and for γ < π/4, this is positive. Also b ≤ a cos(2γ) is a stronger condition than b < a cos(2γ)/sin²γ (since cos(2γ) < cos(2γ)/sin²γ when sin²γ < 1, which is always true). So the binding condition is b ≤ a cos(2γ), i.e., b/a ≤ cos(2γ) = cos C.

Similarly for Q on segment BY: need D_B > 0 and v ≥ 0.
D_B = b cos²γ - (a+b) sin²γ = bp - (a+b)q.
D_B > 0: b cos²γ > (a+b) sin²γ, i.e., b cos²γ - b sin²γ > a sin²γ, i.e., b cos(2γ) > a sin²γ, i.e., a < b cos(2γ)/sin²γ.

1 - v = (a+b)cos(2γ)/(2D_B) ≤ 1 requires (a+b)cos(2γ) ≤ 2D_B = 2bp - 2(a+b)q = 2b(p-q) - 2aq = 2b cos(2γ) - 2a sin²γ.
→ a cos(2γ) ≤ b cos(2γ) - 2a sin²γ
→ a cos(2γ) + 2a sin²γ ≤ b cos(2γ)
→ a[cos(2γ) + 2 sin²γ] ≤ b cos(2γ)
→ a ≤ b cos(2γ)

So for Q on segment BY: a ≤ b cos(2γ), i.e., a/b ≤ cos C.

Combining: b ≤ a cos C and a ≤ b cos C. So b/a ≤ cos C and a/b ≤ cos C, meaning:
b/a ≤ cos C and a/b ≤ cos C
→ (b/a)(a/b) ≤ cos²C → 1 ≤ cos²C → cos²C ≥ 1 → cos C = 1 → C = 0.

That can't be right for a non-degenerate triangle. So both conditions can't be simultaneously satisfied unless... wait, that means P and Q can't both be on the segments AX and BY simultaneously?

Let me re-examine. Maybe I have the wrong bisector. Let me reconsider.

The problem says "the external bisector of the angle AHB meets the segments AX and BY at P and Q respectively." Maybe "segments AX and BY" refers to the segments from A to X and from B to Y, where X is on the altitude from B (extended if necessary) and Y is on the altitude from A (extended if necessary). But the problem says X is where the altitude from B meets the external bisector of C, and Y is where the altitude from A meets the external bisector of C. These are specific points.

Hmm, but if P can't be on segment AX and Q on segment BY simultaneously (for a non-degenerate acute triangle with AC ≠ BC), then maybe I have the wrong bisector.

Let me reconsider. Maybe the "external bisector of angle AHB" is the other external bisector. An angle has two bisectors: internal and external. The external bisector bisects the reflex angle (or equivalently, is perpendicular to the internal bisector). But there's only one external bisector line.

Wait, but I need to be more careful. The "external bisector of angle AHB" — angle AHB is the angle at H in the configuration. There are two rays from H: HA and HB. The internal bisector bisects the angle between them (the angle < π), and the external bisector bisects the supplementary angle.

I claimed the internal bisector of angle AHB is parallel to the external bisector of C (x-axis), and the external bisector of angle AHB is parallel to the internal bisector of C (y-axis). Let me double-check this.

The altitude from A is perpendicular to BC. The altitude from B is perpendicular to AC. The angle between the altitudes (at H) is π - C.

The internal bisector of the angle between the altitudes: if we rotate both altitudes by 90°, they become parallel to BC and AC respectively. The bisector of the angle between BC and AC is the bisector of angle C. Rotating back by 90°, the bisector of the angle between the altitudes is perpendicular to the bisector of angle C.

So internal bisector of angle AHB ⊥ bisector of angle C.

The internal bisector of angle C is the y-axis. So the internal bisector of angle AHB is horizontal (parallel to x-axis = external bisector of C). The external bisector of angle AHB is vertical (parallel to y-axis = internal bisector of C). This seems correct.

But then P and Q can't both be on the segments. Let me recheck with the numerical example.

With a=3, b=2, γ=π/6: 
- For P on AX: need b ≤ a cos C, i.e., 2 ≤ 3·(1/2) = 1.5. FALSE.
- For Q on BY: need a ≤ b cos C, i.e., 3 ≤ 2·(1/2) = 1. FALSE.

So indeed neither P nor Q is on the respective segment. Let me try a=2, b=3:
- For P on AX: need b ≤ a cos C, i.e., 3 ≤ 2·(1/2) = 1. FALSE.
- For Q on BY: need a ≤ b cos C, i.e., 2 ≤ 3·(1/2) = 1.5. FALSE.

Still false. Let me try a=1, b=1 (but AC ≠ BC is required, so a ≠ b). Let me try a=1.1, b=1:
- P on AX: 1 ≤ 1.1·0.5 = 0.55. FALSE.

It seems like for C = 60°, the conditions are very restrictive. Let me try a smaller angle C.

Let me try C = 30° (γ = 15°). cos C = cos 30° ≈ 0.866.
- a = 1, b = 0.8: P on AX needs 0.8 ≤ 1·0.866 = 0.866. TRUE. Q on BY needs 1 ≤ 0.8·0.866 = 0.693. FALSE.

Hmm, still can't get both. The issue is that b ≤ a cos C and a ≤ b cos C together imply 1 ≤ cos²C, which is impossible for C > 0.

So I must be making an error. Let me reconsider the problem.

Wait, maybe I need to reconsider which external bisector of angle C is being used. The external bisector of angle C — there are actually two external angles at C, and thus two external bisectors. But they're the same line (the external bisector is unique as a line, just with two opposite rays).

Actually, I think the issue might be with my identification of the external bisector of angle AHB. Let me reconsider.

Actually, wait. Let me reconsider the problem statement. "The external bisector of the angle AHB meets the segments AX and BY at P and Q respectively."

Maybe AX and BY don't mean the segments from A to X and B to Y. Maybe they mean the lines AX and BY. In many geometry problems, "segment AX" could refer to the line segment, but if P is not between A and X, then maybe the problem means the line.

Actually, re-reading: "meets the segments AX and BY at P and Q respectively" — this does say segments. But if it's impossible for both P and Q to be on the segments simultaneously, then maybe I have an error somewhere.

Let me recheck my computation of X and Y.

X is where the altitude from B meets the external bisector of C. The altitude from B is perpendicular to AC and passes through B. The external bisector of C is the x-axis.

Altitude from B: passes through B = (a sin γ, a cos γ) with direction (cos γ, sin γ) (perpendicular to AC direction (-sin γ, cos γ)).

Wait, is (cos γ, sin γ) the right direction? AC direction is (-sin γ, cos γ) (from C to A). Perpendicular to this: (cos γ, sin γ) or (-cos γ, -sin γ). Let me verify: (-sin γ)(cos γ) + (cos γ)(sin γ) = 0. Yes, perpendicular.

So altitude from B: (a sin γ + s cos γ, a cos γ + s sin γ). Setting y = 0: a cos γ + s sin γ = 0, s = -a cos γ/sin γ. x = a sin γ - a cos²γ/sin γ = a(sin²γ - cos²γ)/sin γ = -a cos(2γ)/sin γ.

Since cos(2γ) > 0 (acute triangle, C < π/2 so 2γ < π/2... wait, C < π/2 means 2γ < π/2, so γ < π/4, so cos(2γ) > 0). So X_x = -a cos(2γ)/sin γ < 0. X is on the negative x-axis.

Similarly Y_x = b cos(2γ)/sin γ > 0. Y is on the positive x-axis.

A = (-b sin γ, b cos γ): A_x < 0, A_y > 0.
B = (a sin γ, a cos γ): B_x > 0, B_y > 0.

So A is in the second quadrant, B is in the first quadrant, X is on the negative x-axis, Y is on the positive x-axis.

Segment AX: from A (second quadrant) to X (negative x-axis). This segment is entirely in the region x < 0 (roughly). Actually, A_x = -b sin γ < 0 and X_x = -a cos(2γ)/sin γ < 0, so the segment AX has x < 0 throughout.

Segment BY: from B (first quadrant) to Y (positive x-axis). B_x = a sin γ > 0 and Y_x = b cos(2γ)/sin γ > 0, so segment BY has x > 0 throughout.

The external bisector of angle AHB is the vertical line x = H_x = (b-a) cos(2γ)/(2 sin γ).

For P on segment AX (x < 0): need H_x < 0, i.e., b < a.
For Q on segment BY (x > 0): need H_x > 0, i.e., b > a.

These are contradictory! So P and Q can't both be on the respective segments unless... hmm.

Wait, unless the vertical line x = H_x passes through both segments, which requires H_x to be in the x-range of both AX and BY. But AX has x < 0 and BY has x > 0, so H_x would need to be both < 0 and > 0, impossible.

So there's definitely something wrong with my approach. Let me reconsider.

Maybe the external bisector of angle AHB is not vertical. Let me recheck.

I claimed: internal bisector of angle AHB is parallel to external bisector of C (x-axis), and external bisector of angle AHB is parallel to internal bisector of C (y-axis).

But wait, is this correct? Let me think again more carefully.

The angle AHB at H is formed by rays HA and HB. The internal bisector bisects this angle. I need to find the actual direction of this bisector, not just say it's "parallel to" something.

Let me compute the directions of HA and HB.

H = ((b-a) cos(2γ)/(2 sin γ), (a+b) cos(2γ)/(2 cos γ))

HA = A - H = (-b sin γ - (b-a) cos(2γ)/(2 sin γ), b cos γ - (a+b) cos(2γ)/(2 cos γ))

Let me compute HA_x:
= [-2b sin²γ - (b-a) cos(2γ)] / (2 sin γ)
= [-2b sin²γ - (b-a)(cos²γ - sin²γ)] / (2 sin γ)
= [-2b sin²γ - b cos²γ + b sin²γ + a cos²γ - a sin²γ] / (2 sin γ)
= [-b sin²γ - b cos²γ + a cos²γ - a sin²γ] / (2 sin γ)
= [-b(sin²γ + cos²γ) + a(cos²γ - sin²γ)] / (2 sin γ)
= [-b + a cos(2γ)] / (2 sin γ)

HA_y:
= [2b cos²γ - (a+b) cos(2γ)] / (2 cos γ)
= [2b cos²γ - (a+b)(cos²γ - sin²γ)] / (2 cos γ)
= [2b cos²γ - a cos²γ + a sin²γ - b cos²γ + b sin²γ] / (2 cos γ)
= [b cos²γ + b sin²γ - a cos²γ + a sin²γ] / (2 cos γ)
= [b - a cos(2γ)] / (2 cos γ)

So HA = ([a cos(2γ) - b] / (2 sin γ), [b - a cos(2γ)] / (2 cos γ))
= (a cos(2γ) - b) / 2 · (1/sin γ, -1/cos γ)

So HA direction is (1/sin γ, -1/cos γ) (up to sign), or equivalently (cos γ, -sin γ) (multiplying by sin γ cos γ). This makes sense: the altitude from A has direction (cos γ, -sin γ), and HA is along this altitude.

Similarly, HB = B - H:
HB_x = a sin γ - (b-a) cos(2γ)/(2 sin γ)
= [2a sin²γ - (b-a) cos(2γ)] / (2 sin γ)
= [2a sin²γ - b cos(2γ) + a cos(2γ)] / (2 sin γ)
= [2a sin²γ + a(cos²γ - sin²γ) - b(cos²γ - sin²γ)] / (2 sin γ)
= [a sin²γ + a cos²γ - b cos²γ + b sin²γ] / (2 sin γ)
= [a - b cos(2γ)] / (2 sin γ)

Hmm wait, let me redo:
= [2a sin²γ - (b-a)(cos²γ - sin²γ)] / (2 sin γ)
= [2a sin²γ - b cos²γ + b sin²γ + a cos²γ - a sin²γ] / (2 sin γ)
= [a sin²γ + a cos²γ + b sin²γ - b cos²γ] / (2 sin γ)
= [a + b(sin²γ - cos²γ)] / (2 sin γ)
= [a - b cos(2γ)] / (2 sin γ)

HB_y = a cos γ - (a+b) cos(2γ)/(2 cos γ)
= [2a cos²γ - (a+b) cos(2γ)] / (2 cos γ)
= [2a cos²γ - (a+b)(cos²γ - sin²γ)] / (2 cos γ)
= [2a cos²γ - a cos²γ + a sin²γ - b cos²γ + b sin²γ] / (2 cos γ)
= [a cos²γ + a sin²γ - b cos²γ + b sin²γ] / (2 cos γ)
= [a - b cos(2γ)] / (2 cos γ)

Wait, that gives:
= [a(cos²γ + sin²γ) + b(sin²γ - cos²γ)] / (2 cos γ)
= [a - b cos(2γ)] / (2 cos γ)

So HB = ([a - b cos(2γ)] / (2 sin γ), [a - b cos(2γ)] / (2 cos γ))
= [a - b cos(2γ)] / 2 · (1/sin γ, 1/cos γ)

So HB direction is (1/sin γ, 1/cos γ), or equivalently (cos γ, sin γ). This is the direction of the altitude from B, which makes sense.

Now, the internal bisector of angle AHB bisects the angle between HA and HB.

HA direction: (cos γ, -sin γ) (pointing from H toward A, but the sign depends on a cos(2γ) - b)
HB direction: (cos γ, sin γ) (pointing from H toward B, but the sign depends on a - b cos(2γ))

The unit vectors:
HA unit: (cos γ, -sin γ) (this is already a unit vector since cos²γ + sin²γ = 1)
HB unit: (cos γ, sin γ) (also a unit vector)

The internal bisector direction is the sum of unit vectors: (cos γ, -sin γ) + (cos γ, sin γ) = (2 cos γ, 0), which is horizontal (along x-axis). ✓

The external bisector direction is the difference: (cos γ, -sin γ) - (cos γ, sin γ) = (0, -2 sin γ), which is vertical (along y-axis). ✓

So my earlier analysis was correct: the external bisector of angle AHB is vertical, passing through H.

But then P on segment AX (x < 0) and Q on segment BY (x > 0) can't both be on the vertical line x = H_x unless H_x = 0, which means a = b, contradicting AC ≠ BC.

So something is fundamentally wrong. Let me re-read the problem.

"The altitudes drawn from A and B meet at H and intersect the external bisector of the angle C at Y and X respectively."

So: altitude from A intersects external bisector of C at Y. Altitude from B intersects external bisector of C at X. This is what I had.

"The external bisector of the angle AHB meets the segments AX and BY at P and Q respectively."

So the external bisector of angle AHB meets segment AX at P and segment BY at Q.

Segment AX: from A to X. A is in the second quadrant (x < 0), X is on the negative x-axis (x < 0). So segment AX has x < 0.

Segment BY: from B to Y. B is in the first quadrant (x > 0), Y is on the positive x-axis (x > 0). So segment BY has x > 0.

The external bisector of angle AHB is vertical (x = H_x). For it to meet segment AX (x < 0), we need H_x < 0, i.e., b < a. For it to meet segment BY (x > 0), we need H_x > 0, i.e., b > a. Contradiction.

Unless... the external bisector of angle AHB is not the vertical line but the horizontal line! Let me reconsider.

Wait, I think I may have confused internal and external. Let me reconsider.

The angle AHB = π - C. The internal bisector bisects this angle. The external bisector is perpendicular to the internal bisector.

I found the internal bisector direction is (2 cos γ, 0) = horizontal. The external bisector direction is (0, -2 sin γ) = vertical.

But wait, which bisector is "internal" and which is "external" depends on which angle we're bisecting. The angle AHB is the angle at H looking from HA to HB. There are two angles: the one < π (which is π - C) and the one > π (which is π + C). The internal bisector bisects the angle < π, and the external bisector bisects the angle > π (or equivalently, is perpendicular to the internal bisector).

But actually, the internal and external bisectors are just two perpendicular lines through H. One is horizontal, one is vertical. The "external bisector of angle AHB" is the one that bisects the external (reflex) angle.

Hmm, but regardless of which is internal and which is external, one is horizontal and one is vertical. The vertical one can't meet both segments. The horizontal one (y = H_y) could potentially meet both segments.

Let me check: the horizontal line y = H_y = (a+b) cos(2γ)/(2 cos γ).

Segment AX: from A = (-b sin γ, b cos γ) to X = (-a cos(2γ)/sin γ, 0).
The y-coordinates along AX go from b cos γ (at A) to 0 (at X). H_y = (a+b) cos(2γ)/(2 cos γ).

Is H_y between 0 and b cos γ? 
H_y = (a+b) cos(2γ)/(2 cos γ) vs b cos γ.
H_y / (b cos γ) = (a+b) cos(2γ) / (2b cos²γ) = (a+b)(cos²γ - sin²γ) / (2b cos²γ) = (a+b)/(2b) · (1 - tan²γ).

For this to be between 0 and 1: need (a+b)/(2b) · (1 - tan²γ) ≤ 1, i.e., (a+b)(1 - tan²γ) ≤ 2b, i.e., (a+b) - (a+b)tan²γ ≤ 2b, i.e., a - b ≤ (a+b)tan²γ. Since a, b > 0 and tan²γ > 0, this is a - b ≤ (a+b)tan²γ. If a ≤ b, this is automatically satisfied. If a > b, need (a-b)/(a+b) ≤ tan²γ.

Similarly for segment BY: from B = (a sin γ, a cos γ) to Y = (b cos(2γ)/sin γ, 0).
Y-coordinates go from a cos γ (at B) to 0 (at Y). H_y = (a+b) cos(2γ)/(2 cos γ).
H_y / (a cos γ) = (a+b) cos(2γ) / (2a cos²γ) = (a+b)/(2a) · (1 - tan²γ).
For this to be between 0 and 1: (a+b)(1-tan²γ) ≤ 2a, i.e., b - a ≤ (a+b)tan²γ. If b ≤ a, auto. If b > a, need (b-a)/(a+b) ≤ tan²γ.

So the horizontal line y = H_y can meet both segments AX and BY if:
|a - b|/(a+b) ≤ tan²γ, i.e., |a-b| ≤ (a+b) tan²γ.

This is possible! So maybe the "external bisector of angle AHB" is the horizontal line, not the vertical line.

Let me reconsider which bisector is internal and which is external.

The angle AHB = π - C. Looking at the directions:
- HA direction (from H): (cos γ, -sin γ) [when a cos(2γ) > b, pointing toward A] or (-cos γ, sin γ) [when a cos(2γ) < b]
- HB direction (from H): (cos γ, sin γ) [when a > b cos(2γ)] or (-cos γ, -sin γ) [when a < b cos(2γ)]

The angle between (cos γ, -sin γ) and (cos γ, sin γ): 
cos(angle) = cos²γ - sin²γ = cos(2γ) = cos C.
So the angle is C... wait, that's the angle between the two direction vectors. But angle AHB = π - C, not C.

Hmm, the issue is the direction of HA and HB. The vectors (cos γ, -sin γ) and (cos γ, sin γ) have angle C between them (since cos of angle = cos(2γ) = cos C). But the actual angle AHB is π - C. This means the rays HA and HB point in directions that make angle π - C, not C.

This happens when one of the direction vectors is flipped. For instance, if HA points in direction (-cos γ, sin γ) (opposite to (cos γ, -sin γ)) and HB points in direction (cos γ, sin γ), then the angle between them is:
cos(angle) = -cos²γ + sin²γ = -cos(2γ) = -cos C, so angle = π - C. ✓

So the actual rays from H are:
- HA: direction (-cos γ, sin γ) = pointing up-left (toward A in second quadrant)
- HB: direction (cos γ, sin γ) = pointing up-right (toward B in first quadrant)

The angle between these is π - C (opening upward). The internal bisector (bisecting the angle π - C that opens upward) is the direction (0, 1) = vertical (upward). The external bisector is horizontal.

Wait, let me recalculate. The sum of unit vectors:
(-cos γ, sin γ) + (cos γ, sin γ) = (0, 2 sin γ), direction (0, 1) = vertical.

The difference:
(-cos γ, sin γ) - (cos γ, sin γ) = (-2 cos γ, 0), direction (-1, 0) = horizontal.

So the internal bisector of angle AHB (bisecting the angle π - C that opens upward) is vertical (upward), and the external bisector is horizontal.

I had it backwards! The internal bisector is vertical, and the external bisector is horizontal.

So the external bisector of angle AHB is the horizontal line y = H_y = (a+b) cos(2γ)/(2 cos γ).

This makes much more sense! The horizontal line can intersect both segments AX and BY.

Let me redo the computation with the correct bisector.

The external bisector of angle AHB is the horizontal line y = H_y = (a+b) cos(2γ)/(2 cos γ).

P is on segment AX with y = H_y.
A = (-b sin γ, b cos γ), X = (-a cos(2γ)/sin γ, 0).

Parametrize: P = A + u(X - A), u ∈ [0, 1].
P_y = b cos γ + u(0 - b cos γ) = b cos γ(1 - u) = H_y = (a+b) cos(2γ)/(2 cos γ)

So 1 - u = (a+b) cos(2γ) / (2b cos²γ) = (a+b)(cos²γ - sin²γ) / (2b cos²γ) = (a+b)/(2b) · (1 - tan²γ)

u = 1 - (a+b)(1 - tan²γ)/(2b) = [2b - (a+b)(1 - tan²γ)] / (2b) = [2b - a - b + (a+b)tan²γ] / (2b) = [b - a + (a+b)tan²γ] / (2b)

For u ∈ [0, 1]: need 0 ≤ b - a + (a+b)tan²γ and b - a + (a+b)tan²γ ≤ 2b.
The first: (a+b)tan²γ ≥ a - b, i.e., if a > b: tan²γ ≥ (a-b)/(a+b).
The second: (a+b)tan²γ ≤ b + a, i.e., tan²γ ≤ 1, i.e., γ ≤ π/4, which is true for acute triangle.

Similarly, Q is on segment BY with y = H_y.
B = (a sin γ, a cos γ), Y = (b cos(2γ)/sin γ, 0).

Q = B + v(Y - B), v ∈ [0, 1].
Q_y = a cos γ(1 - v) = H_y = (a+b) cos(2γ)/(2 cos γ)

1 - v = (a+b) cos(2γ) / (2a cos²γ) = (a+b)/(2a) · (1 - tan²γ)

v = 1 - (a+b)(1 - tan²γ)/(2a) = [2a - (a+b)(1 - tan²γ)] / (2a) = [2a - a - b + (a+b)tan²γ] / (2a) = [a - b + (a+b)tan²γ] / (2a)

For v ∈ [0, 1]: need 0 ≤ a - b + (a+b)tan²γ and a - b + (a+b)tan²γ ≤ 2a.
First: if b > a: tan²γ ≥ (b-a)/(a+b).
Second: tan²γ ≤ 1, true.

So for both P and Q to be on the segments: |a - b|/(a+b) ≤ tan²γ.

Now, AP = u · |AX|, PX = (1-u) · |AX|.
BQ = v · |BY|, QY = (1-v) · |BY|.

PX = (1-u)|AX| = [(a+b)(1 - tan²γ)/(2b)] · |AX|
QY = (1-v)|BY| = [(a+b)(1 - tan²γ)/(2a)] · |BY|

Condition PX = QY:
[(a+b)(1 - tan²γ)/(2b)] · |AX| = [(a+b)(1 - tan²γ)/(2a)] · |BY|

Since (a+b)(1-tan²γ) > 0 (acute triangle, γ < π/4 so tan²γ < 1), we can cancel:
|AX|/b = |BY|/a
a · |AX| = b · |BY|

So the condition PX = QY reduces to a · |AX| = b · |BY|.

Let me compute |AX| and |BY|.

|AX|² = (X_x - A_x)² + (0 - A_y)²
X_x - A_x = -a cos(2γ)/sin γ - (-b sin γ) = -a cos(2γ)/sin γ + b sin γ = [-a cos(2γ) + b sin²γ]/sin γ

Let me use the notation: let t = tan γ, so sin γ = t/√(1+t²), cos γ = 1/√(1+t²), sin²γ = t²/(1+t²), cos²γ = 1/(1+t²), cos(2γ) = (1-t²)/(1+t²).

Actually, let me try a different approach. Let me use the formula for the distance from a point to a line, or just compute directly.

|AX|² = [(-a cos(2γ) + b sin²γ)/sin γ]² + b² cos²γ

Let me expand:
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin⁴γ] / sin²γ + b² cos²γ
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin⁴γ + b² cos²γ sin²γ] / sin²γ
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ(sin²γ + cos²γ)] / sin²γ
= [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ

Similarly:
|BY|² = (Y_x - B_x)² + (0 - B_y)²
Y_x - B_x = b cos(2γ)/sin γ - a sin γ = [b cos(2γ) - a sin²γ]/sin γ

|BY|² = [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin⁴γ] / sin²γ + a² cos²γ
= [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin⁴γ + a² cos²γ sin²γ] / sin²γ
= [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ] / sin²γ

So:
|AX|² = [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ
|BY|² = [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ] / sin²γ

The condition a|AX| = b|BY| means a²|AX|² = b²|BY|²:
a²[a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] = b²[b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ]

a⁴ cos²(2γ) - 2a³b cos(2γ) sin²γ + a²b² sin²γ = b⁴ cos²(2γ) - 2ab³ cos(2γ) sin²γ + a²b² sin²γ

a⁴ cos²(2γ) - 2a³b cos(2γ) sin²γ = b⁴ cos²(2γ) - 2ab³ cos(2γ) sin²γ

(a⁴ - b⁴) cos²(2γ) = 2ab cos(2γ) sin²γ (a² - b²)

(a² - b²)(a² + b²) cos²(2γ) = 2ab(a² - b²) cos(2γ) sin²γ

Since a ≠ b (AC ≠ BC), we can divide by (a² - b²):

(a² + b²) cos²(2γ) = 2ab cos(2γ) sin²γ

Since cos(2γ) > 0 (acute triangle), divide by cos(2γ):

(a² + b²) cos(2γ) = 2ab sin²γ

(a² + b²)(cos²γ - sin²γ) = 2ab sin²γ

(a² + b²) cos²γ = (a² + b²) sin²γ + 2ab sin²γ = (a² + 2ab + b²) sin²γ = (a+b)² sin²γ

So: (a² + b²) cos²γ = (a+b)² sin²γ

→ tan²γ = (a² + b²) / (a+b)²

→ tan γ = √(a² + b²) / (a+b)

This is the condition from PX = QY.

Now, let me compute AP + BQ and CH under this condition.

AP = u · |AX|, BQ = v · |BY|.

u = [b - a + (a+b)tan²γ] / (2b)
v = [a - b + (a+b)tan²γ] / (2a)

Under the condition tan²γ = (a² + b²)/(a+b)²:

(a+b)tan²γ = (a² + b²)/(a+b)

u = [b - a + (a² + b²)/(a+b)] / (2b) = [(b-a)(a+b) + a² + b²] / [(a+b) · 2b]
= [b² - a² + a² + b²] / [2b(a+b)]
= 2b² / [2b(a+b)]
= b / (a+b)

v = [a - b + (a² + b²)/(a+b)] / (2a) = [(a-b)(a+b) + a² + b²] / [(a+b) · 2a]
= [a² - b² + a² + b²] / [2a(a+b)]
= 2a² / [2a(a+b)]
= a / (a+b)

So u = b/(a+b) and v = a/(a+b). Nice!

AP = u · |AX| = [b/(a+b)] · |AX|
BQ = v · |BY| = [a/(a+b)] · |BY|

AP + BQ = [b|AX| + a|BY|] / (a+b)

Under the condition a|AX| = b|BY|, let's say |AX| = bt and |BY| = at for some t > 0. Then:
AP + BQ = [b · bt + a · at] / (a+b) = [b²t + a²t] / (a+b) = (a² + b²)t / (a+b)

Now I need to find t. We have |AX| = bt, so |AX|² = b²t².

From our formula:
|AX|² = [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ

Under the condition (a² + b²) cos(2γ) = 2ab sin²γ, i.e., cos(2γ) = 2ab sin²γ / (a² + b²):

Let me substitute. Let S = a² + b², P = ab.
cos(2γ) = 2P sin²γ / S

Also, cos(2γ) = cos²γ - sin²γ = 1 - 2sin²γ, so:
1 - 2sin²γ = 2P sin²γ / S
1 = sin²γ(2 + 2P/S) = sin²γ · 2(S + P)/S
sin²γ = S / [2(S + P)] = (a² + b²) / [2(a² + b² + ab)]

And cos²γ = 1 - sin²γ = [2(a² + b² + ab) - (a² + b²)] / [2(a² + b² + ab)] = (a² + b² + 2ab) / [2(a² + b² + ab)] = (a+b)² / [2(a² + b² + ab)]

Let me verify: tan²γ = sin²γ/cos²γ = (a² + b²) / (a+b)². ✓

Now, cos(2γ) = 1 - 2sin²γ = 1 - (a² + b²)/(a² + b² + ab) = ab / (a² + b² + ab)

Let me verify with the other formula: 2ab sin²γ / (a² + b²) = 2ab · (a² + b²)/[2(a² + b² + ab)] / (a² + b²) = ab / (a² + b² + ab). ✓

Now let me compute |AX|²:
|AX|² = [a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ] / sin²γ

Let me substitute cos(2γ) = ab/(a² + b² + ab) and sin²γ = (a² + b²)/[2(a² + b² + ab)].

Let D = a² + b² + ab for convenience.

cos(2γ) = ab/D
sin²γ = (a² + b²)/(2D) = S/(2D) where S = a² + b²

Numerator of |AX|²:
a² cos²(2γ) - 2ab cos(2γ) sin²γ + b² sin²γ
= a² (ab/D)² - 2ab · (ab/D) · S/(2D) + b² · S/(2D)
= a² · a²b²/D² - a²b² · S/D² + b²S/(2D)
= a⁴b²/D² - a²b²S/D² + b²S/(2D)
= b²/D² [a⁴ - a²S + SD/2]
= b²/D² [a⁴ - a²(a² + b²) + (a² + b²)(a² + b² + ab)/2]
= b²/D² [a⁴ - a⁴ - a²b² + (a² + b²)²/2 + ab(a² + b²)/2]
= b²/D² [-a²b² + (a⁴ + 2a²b² + b⁴)/2 + (a³b + ab³)/2]
= b²/D² [-a²b² + a⁴/2 + a²b² + b⁴/2 + a³b/2 + ab³/2]
= b²/D² [a⁴/2 + b⁴/2 + a³b/2 + ab³/2]
= b²/(2D²) [a⁴ + b⁴ + a³b + ab³]
= b²/(2D²) [a³(a + b) + b³(a + b)]
= b²/(2D²) (a + b)(a³ + b³)
= b²/(2D²) (a + b)(a + b)(a² - ab + b²)
= b²(a + b)²(a² - ab + b²) / (2D²)

And |AX|² = [numerator] / sin²γ = [b²(a+b)²(a² - ab + b²) / (2D²)] / [S/(2D)]
= b²(a+b)²(a² - ab + b²) / (2D²) · 2D/S
= b²(a+b)²(a² - ab + b²) / (DS)

where D = a² + ab + b² and S = a² + b².

Note that a² - ab + b² = D - 2ab. Also, D = S + ab.

So |AX|² = b²(a+b)²(D - 2ab) / (D · S)

|AX| = b(a+b) √[(D - 2ab)/(DS)] = b(a+b) √(D - 2ab) / √(DS)

Similarly, |BY|² = [b² cos²(2γ) - 2ab cos(2γ) sin²γ + a² sin²γ] / sin²γ

By symmetry (swapping a and b):
|BY|² = a²(a+b)²(D - 2ab) / (DS)

|BY| = a(a+b) √(D - 2ab) / √(DS)

Let me verify the condition a|AX| = b|BY|:
a · b(a+b)√(D-2ab)/√(DS) = b · a(a+b)√(D-2ab)/√(DS). ✓ (Both sides equal.)

Now, t such that |AX| = bt:
bt = b(a+b)√(D-2ab)/√(DS)
t = (a+b)√(D-2ab)/√(DS)

AP + BQ = (a² + b²)t / (a+b) = S · (a+b)√(D-2ab) / [(a+b)√(DS)] = S√(D-2ab) / √(DS)

= S √(D - 2ab) / √(D · S) = √S · √(D - 2ab) / √D = √[S(D - 2ab)/D]

where S = a² + b², D = a² + ab + b², D - 2ab = a² - ab + b².

AP + BQ = √[(a² + b²)(a² - ab + b²) / (a² + ab + b²)]

Now, CH = c cot C. We have c² = a² + b² - 2ab cos C = a² + b² - 2ab cos(2γ).

cos(2γ) = ab/D, so c² = S - 2ab · ab/D = S - 2a²b²/D = (SD - 2a²b²)/D.

SD = (a² + b²)(a² + ab + b²) = a⁴ + a³b + a²b² + a²b² + ab³ + b⁴ = a⁴ + a³b + 2a²b² + ab³ + b⁴

SD - 2a²b² = a⁴ + a³b + ab³ + b⁴ = a³(a + b) + b³(a + b) = (a + b)(a³ + b³) = (a + b)²(a² - ab + b²)

So c² = (a+b)²(a² - ab + b²) / D = (a+b)²(D - 2ab) / D

c = (a+b)√(D - 2ab) / √D

CH = c cot C = c · cos(2γ)/sin(2γ) = c · cos(2γ) / (2 sin γ cos γ)

sin(2γ) = 2 sin γ cos γ. sin²γ = S/(2D), cos²γ = (a+b)²/(2D).
sin γ cos γ = √[S(a+b)²/(4D²)] = (a+b)√S / (2D)
sin(2γ) = 2 · (a+b)√S / (2D) = (a+b)√S / D

cos(2γ) = ab/D

cot C = cot(2γ) = cos(2γ)/sin(2γ) = (ab/D) / ((a+b)√S/D) = ab / ((a+b)√S)

CH = c · cot C = [(a+b)√(D-2ab)/√D] · [ab/((a+b)√S)] = ab√(D-2ab) / (√D · √S) = ab√(D-2ab) / √(DS)

Now, the ratio:
(AP + BQ) / CH = √[S(D-2ab)/D] / [ab√(D-2ab)/√(DS)]
= √[S(D-2ab)/D] · √(DS) / [ab√(D-2ab)]
= √[S(D-2ab) · DS / D] / [ab√(D-2ab)]
= √[S²(D-2ab)] / [ab√(D-2ab)]
= S√(D-2ab) / [ab√(D-2ab)]
= S / (ab)
= (a² + b²) / (ab)

So (AP + BQ) / CH = (a² + b²) / (ab) = a/b + b/a.

By AM-GM, a/b + b/a ≥ 2, with equality when a = b. But a ≠ b (given AC ≠ BC), so the ratio is strictly > 2.

But we need the infimum. As a/b → 1 (but a ≠ b), the ratio approaches 2. So the infimum is 2, but it's not achieved.

Wait, but the problem asks for the largest k such that AP + BQ ≥ k · CH always holds. If the ratio (AP+BQ)/CH = a/b + b/a > 2 always (with equality only in the limit a → b), then k = 2.

But wait, we need to check that the infimum is indeed 2 and is approached. As a → b, the ratio → 2. But we also need to check that the triangle remains valid (acute, with the condition PX = QY satisfied, and P, Q on the segments).

Let me verify: when a → b, the condition tan²γ = (a² + b²)/(a+b)² → 2a²/(4a²) = 1/2, so γ → arctan(1/√2), C = 2γ → 2 arctan(1/√2). 

arctan(1/√2) ≈ 35.26°, so C ≈ 70.53°. This is less than 90°, so the triangle can be acute.

Also, we need |a - b|/(a+b) ≤ tan²γ. When a ≈ b, |a-b|/(a+b) → 0 ≤ 1/2 = tan²γ. ✓

And we need the triangle to be acute: all angles < 90°. C ≈ 70.53° < 90°. We also need A < 90° and B < 90°. By the law of sines, a/sin A = b/sin B = c/sin C. When a ≈ b, A ≈ B ≈ (180° - 70.53°)/2 ≈ 54.74° < 90°. ✓

So as a → b (with a ≠ b), the ratio (AP + BQ)/CH → 2, and all conditions are satisfied. The infimum is 2, approached but never achieved.

Therefore k = 2.

Wait, but I should double-check. The problem says "the largest real number k such that AP + BQ ≥ k · CH always holds." If the ratio is always > 2 but approaches 2, then for k = 2, the inequality AP + BQ ≥ 2 · CH always holds (strictly), and for any k > 2, there exists a triangle where AP + BQ < k · CH. So k = 2.

Let me verify with a specific numerical example. Let me take a = 2, b = 1 (so a ≠ b).

Condition: tan²γ = (4 + 1)/(3)² = 5/9, tan γ = √5/3.
γ = arctan(√5/3) ≈ arctan(0.745) ≈ 36.7°
C = 2γ ≈ 73.4°

Check acute: C ≈ 73.4° < 90°. 
c² = (a+b)²(D - 2ab)/D where D = 4 + 2 + 1 = 7, D - 2ab = 7 - 4 = 3.
c² = 9 · 3 / 7 = 27/7, c = √(27/7) ≈ 1.964.

sin A = a sin C / c. sin C = sin(73.4°) ≈ 0.958. sin A ≈ 2 · 0.958 / 1.964 ≈ 0.976. A ≈ 77.4° < 90°. ✓
sin B = b sin C / c ≈ 1 · 0.958 / 1.964 ≈ 0.488. B ≈ 29.2° < 90°. ✓

Ratio = (a² + b²)/(ab) = 5/2 = 2.5.

Let me try a = 1.1, b = 1:
Ratio = (1.21 + 1)/(1.1) = 2.21/1.1 = 2.009...

Approaching 2. ✓

So k = 2.

Let me also verify the whole computation with the numerical example a = 2, b = 1.

tan²γ = 5/9, sin²γ = 5/14, cos²γ = 9/14, cos(2γ) = cos²γ - sin²γ = 4/14 = 2/7.

D = a² + ab + b² = 4 + 2 + 1 = 7.
S = a² + b² = 5.
D - 2ab = 7 - 4 = 3.

c² = (a+b)²(D-2ab)/D = 9 · 3/7 = 27/7.
CH = ab√(D-2ab)/√(DS) = 2·1·√3/√(7·5) = 2√3/√35 = 2√(3/35) = 2√(3/35).

AP + BQ = √[S(D-2ab)/D] = √[5·3/7] = √(15/7).

Ratio = √(15/7) / (2√(3/35)) = √(15/7) / (2√3/√35) = √(15/7) · √35 / (2√3) = √(15·35/(7·3)) / 2 = √(525/21) / 2 = √25 / 2 = 5/2 = 2.5. ✓

Great, this confirms the ratio is (a² + b²)/(ab) = 5/2.

So the answer is k = 2.

Let me write up the proof.

Actually, let me make sure I haven't made an error in identifying the external bisector. Let me re-examine.

The angle AHB = π - C. The rays from H to A and H to B point in directions (-cos γ, sin γ) and (cos γ, sin γ) respectively (both pointing upward, one left and one right). The angle between them (opening upward) is π - C.

The internal bisector of this angle is the upward vertical direction (0, 1), which bisects the angle π - C.

The external bisector is perpendicular to the internal bisector, so it's horizontal. The external bisector of angle AHB is the horizontal line through H.

This is correct. The external bisector bisects the external (reflex) angle, which opens downward. Its bisector is horizontal.

Now let me also verify that P is indeed between A and X (on the segment) for our numerical example.

a = 2, b = 1, γ = arctan(√5/3).
A = (-b sin γ, b cos γ) = (-sin γ, cos γ)
X = (-a cos(2γ)/sin γ, 0) = (-2 · (2/7) / sin γ, 0) = (-4/(7 sin γ), 0)

sin γ = √(5/14), so X = (-4/(7·√(5/14)), 0) = (-4√(14/5)/7, 0) = (-4√14/(7√5), 0) = (-4√70/35, 0)

A = (-√(5/14), √(9/14)) = (-√5/√14, 3/√14)

u = b/(a+b) = 1/3.
P = A + (1/3)(X - A).
P_y = A_y + (1/3)(0 - A_y) = (2/3)A_y = (2/3)(3/√14) = 2/√14.

H_y = (a+b)cos(2γ)/(2cos γ) = 3·(2/7)/(2·3/√14) = (6/7)/(6/√14) = √14/7 = √14/7.
2/√14 = 2√14/14 = √14/7. ✓ P_y = H_y.

P_x = A_x + (1/3)(X_x - A_x) = -√5/√14 + (1/3)(-4√70/35 + √5/√14)

Let me compute X_x - A_x = -4√70/35 + √5/√14 = -4√70/35 + √5·√14/14 = -4√70/35 + √70/14

= √70(-4/35 + 1/14) = √70(-8/70 + 5/70) = √70(-3/70) = -3√70/70 = -3√70/70

P_x = -√5/√14 + (1/3)(-3√70/70) = -√5/√14 - √70/70 = -√5√14/14 - √70/70 = -√70/14 - √70/70 = -√70(1/14 + 1/70) = -√70(5/70 + 1/70) = -6√70/70 = -3√70/35

Is this between A_x = -√5/√14 = -√70/14 = -5√70/70 and X_x = -4√70/35 = -8√70/70?

P_x = -3√70/35 = -6√70/70. A_x = -5√70/70, X_x = -8√70/70.

-8√70/70 ≤ -6√70/70 ≤ -5√70/70? -8 ≤ -6 ≤ -5? Yes! ✓ P is between A and X.

Great. Now let me also verify Q.

v = a/(a+b) = 2/3.
B = (a sin γ, a cos γ) = (2√(5/14), 2·3/√14) = (2√5/√14, 6/√14)
Y = (b cos(2γ)/sin γ, 0) = ((2/7)/√(5/14), 0) = (2√(14/5)/7, 0) = (2√70/35, 0)

Q = B + (2/3)(Y - B).
Q_y = B_y + (2/3)(0 - B_y) = (1/3)B_y = (1/3)(6/√14) = 2/√14 = √14/7 = H_y. ✓

Q_x = B_x + (2/3)(Y_x - B_x) = 2√5/√14 + (2/3)(2√70/35 - 2√5/√14)

Y_x - B_x = 2√70/35 - 2√70/14 = 2√70(1/35 - 1/14) = 2√70(2/70 - 5/70) = 2√70(-3/70) = -6√70/70 = -3√70/35

Q_x = 2√70/14 + (2/3)(-3√70/35) = √70/7 - 2√70/35 = √70(5/35 - 2/35) = 3√70/35

Is this between B_x = 2√70/14 = 5√70/35 and Y_x = 2√70/35?
2√70/35 ≤ 3√70/35 ≤ 5√70/35? 2 ≤ 3 ≤ 5? Yes! ✓ Q is between B and Y.

Everything checks out. The answer is k = 2.

Now let me write a clean proof.

**Proof:**

Set up coordinates with C at the origin, the internal bisector of angle C along the positive y-axis, and the external bisector of angle C along the x-axis. Let angle C = 2γ (so 0 < γ < π/4 for an acute triangle). Let BC = a, CA = b with a ≠ b.

Then:
- A = (-b sin γ, b cos γ)
- B = (a sin γ, a cos γ)

The altitude from A (perpendicular to BC, direction (cos γ, -sin γ)) meets the x-axis at:
Y = (b cos 2γ / sin γ, 0)

The altitude from B (perpendicular to AC, direction (cos γ, sin γ)) meets the x-axis at:
X = (-a cos 2γ / sin γ, 0)

The orthocenter is:
H = ((b-a) cos 2γ / (2 sin γ), (a+b) cos 2γ / (2 cos γ))

The rays HA and HB point in directions (-cos γ, sin γ) and (cos γ, sin γ) respectively, so the internal bisector of angle AHB is vertical and the **external bisector** is the horizontal line y = H_y = (a+b) cos 2γ / (2 cos γ).

**Finding P and Q:** P is on segment AX with P_y = H_y, giving parameter u = b/(a+b) (after applying the condition below). Q is on segment BY with Q_y = H_y, giving v = a/(a+b).

**Condition PX = QY:** Computing (1-u)|AX| = (1-v)|BY| and simplifying yields:
(a² + b²) cos 2γ = 2ab sin²γ
equivalently: tan²γ = (a² + b²)/(a+b)².

**Computing the ratio:** Under this condition, with D = a² + ab + b², S = a² + b²:
- |AX|² = b²(a+b)²(D - 2ab)/(DS), |BY|² = a²(a+b)²(D - 2ab)/(DS)
- AP + BQ = √[S(D - 2ab)/D]
- CH = ab√(D - 2ab)/√(DS)

Therefore:
(AP + BQ)/CH = S/(ab) = (a² + b²)/(ab) = a/b + b/a

By AM-GM, a/b + b/a ≥ 2 with equality iff a = b. Since a ≠ b, the ratio is strictly > 2, but approaches 2 as a → b. The limiting case a → b gives a valid acute triangle (C → 2 arctan(1/√2) ≈ 70.5°), so the infimum is 2.

Therefore k = 2.

### PROOF COMPLETE

Wait, I need to be more careful about the proof. Let me make sure the derivation of u = b/(a+b) under the condition is clear, and that I properly show the condition PX = QY leads to tan²γ = (a²+b²)/(a+b)².

Let me also double-check: the problem says "the largest real number k such that AP + BQ ≥ k·CH always holds." This means k = inf{(AP+BQ)/CH} over all valid configurations. We showed (AP+BQ)/CH = a/b + b/a > 2, with inf = 2. So k = 2.

Let me write the proof more carefully.

Actually, I realize I should double-check the formula for AP + BQ more carefully. Let me recompute.

Under the condition, u = b/(a+b) and v = a/(a+b).

AP = u · |AX| = (b/(a+b)) · |AX|
BQ = v · |BY| = (a/(a+b)) · |BY|

From the condition a|AX| = b|BY|, we get |BY| = a|AX|/b.

AP + BQ = (b/(a+b))|AX| + (a/(a+b)) · (a|AX|/b) = |AX|/(a+b) · (b + a²/b) = |AX|/(a+b) · (b² + a²)/b = |AX| · S / (b(a+b))

And |AX| = b(a+b)√(D-2ab)/√(DS), so:
AP + BQ = b(a+b)√(D-2ab)/√(DS) · S/(b(a+b)) = S√(D-2ab)/√(DS) = √(S²(D-2ab)/(DS)) = √(S(D-2ab)/D). ✓

CH = c · cot C. c² = (a+b)²(D-2ab)/D, so c = (a+b)√(D-2ab)/√D.
cot C = cot(2γ) = cos(2γ)/sin(2γ).
cos(2γ) = ab/D.
sin(2γ) = 2sinγ cosγ. sin²γ = S/(2D), cos²γ = (a+b)²/(2D).
sin(2γ) = 2√(S(a+b)²/(4D²)) = (a+b)√S/D.
cot C = (ab/D)/((a+b)√S/D) = ab/((a+b)√S).

CH = (a+b)√(D-2ab)/√D · ab/((a+b)√S) = ab√(D-2ab)/(√D·√S) = ab√(D-2ab)/√(DS). ✓

Ratio = √(S(D-2ab)/D) / (ab√(D-2ab)/√(DS)) = √(S(D-2ab)/D) · √(DS)/(ab√(D-2ab)) = √(S(D-2ab)·DS/D)/(ab√(D-2ab)) = √(S²(D-2ab))/(ab√(D-2ab)) = S√(D-2ab)/(ab√(D-2ab)) = S/(ab) = (a²+b²)/(ab). ✓

The proof is correct. k = 2.
