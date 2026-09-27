# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $\triangle ABC$ be a triangle with side lengths $a, b, c$, semiperimeter $s$, and inradius $r$. Semicircles with diameters $BC, CA, AB$ are drawn outside of the triangle. A circle with radius $t$ is tangent to all three semicircles. If $a=13, b=14$, and $c=15$, calculate the value of $t - \frac{s}{2}$.       — 题目文本
#   From the original solution, the radius $t$ of the circle tangent to the three semicircles is given by $t = g + \frac{s}{2}$, where $g$ satisfies the relation $\frac{1}{2g} = \frac{1}{s-a} + \frac{1}{s-b} + \frac{1}{s-c} + \frac{2}{r}$. For a triangle with sides $13, 14, 15$, the semiperimeter is $s = \frac{13+14+15}{2} = 21$. The area is $A = \sqrt{21(21-13)(21-14)(21-15)} = \sqrt{21 \cdot 8 \cdot 7 \cdot 6} = \sqrt{7056} = 84$. The inradius is $r = A/s = 84/21 = 4$. Substituting these values: $s-a = 8, s-b = 7, s-c = 6$. Then $\frac{1}{2g} = \frac{1}{8} + \frac{1}{7} + \frac{1}{6} + \frac{2}{4} = \frac{21+24+28+84}{168} = \frac{157}{168}$. Thus $2g = \frac{168}{157}$, so $g = \frac{84}{157}$. Since $t - \frac{s}{2} = g$, the answer is $\frac{84}{157}$.  — 标准解答
#   Let me solve this problem. First, answer leak check - the problem text doesn't contain any leaked answers or solution sketches. Good.

Let me solve the problem.

We have triangle ABC with sides a=13, b=14, c=15. Semicircles drawn outside the triangle on diameters BC, CA, AB. A circle of radius t tangent to all three semicircles. Find t - s/2.

First, s = (13+14+15)/2 = 21. So s/2 = 10.5.

Area of triangle 13-14-15: Using Heron's formula, area = sqrt(21·8·7·6) = sqrt(21·336) = sqrt(7056) = 84. So r = area/s = 84/21 = 4.

Now the semicircles. Semicircle on BC (diameter a=13) has radius 13/2. On CA (diameter b=14) has radius 7. On AB (diameter c=15) has radius 15/2.

These are drawn outside the triangle. We need a circle tangent to all three semicircles.

Let me think about this. The semicircles are on the sides as diameters, drawn outside the triangle. A circle tangent to all three.

Let me set up coordinates. Place the triangle. Let me think about the geometry.

Actually, there's a known result related to this. The three semicircles on the sides of a triangle, drawn externally, form a shape. A circle tangent to all three...

Let me think about the centers. The center of the semicircle on BC is the midpoint of BC. The semicircle is drawn outside the triangle, so it's the arc on the side opposite to A.

Let me set up coordinates. Let B = (0,0), C = (13, 0). Then a = BC = 13.

Find A: AB = c = 15, AC = b = 14.
A = (x, y) where x² + y² = 225, (x-13)² + y² = 196.
x² - (x-13)² = 225 - 196 = 29
x² - x² + 26x - 169 = 29
26x = 198
x = 198/26 = 99/13
y² = 225 - (99/13)² = 225 - 9801/169 = (225·169 - 9801)/169 = (38025 - 9801)/169 = 28224/169
y = 168/13 (since area = (1/2)(13)(y) = 84, so y = 168/13). Yes.

So A = (99/13, 168/13).

Midpoints:
- M_a (midpoint of BC) = (13/2, 0), radius of semicircle = 13/2
- M_b (midpoint of CA) = ((13 + 99/13)/2, (0 + 168/13)/2) = ((169/13 + 99/13)/2, 84/13) = (268/26, 84/13) = (134/13, 84/13), radius = 7
- M_c (midpoint of AB) = ((0 + 99/13)/2, (0 + 168/13)/2) = (99/26, 84/13), radius = 15/2

The semicircles are drawn outside the triangle. The center of the tangent circle should be on the same side as the triangle interior? No - the semicircles bulge outward, so the tangent circle is likely in the region where the semicircles are, which is outside the triangle.

Actually, let me think about this differently. The semicircle on BC outside the triangle means the arc is on the opposite side of BC from A. Since A is above BC (y > 0), the semicircle on BC is below BC (y < 0).

Similarly, semicircle on CA is on the opposite side of CA from B, and semicircle on AB is on the opposite side of AB from C.

So the three semicircle arcs are all outside the triangle, bulging outward. A circle tangent to all three would be... in the interior of the triangle? Or somewhere else?

Hmm, if the semicircles bulge outward, a circle tangent to all three from the inside (i.e., in the triangle region) would be tangent to the arcs. But the arcs are on the far side. Actually, the semicircle includes the diameter as part of its boundary (the flat part), and the arc. The "semicircle" as a region is the half-disk.

Wait, I think the problem means the arcs only. A circle tangent to all three semicircular arcs.

Let me reconsider. The tangent circle is likely inside the triangle, tangent to each semicircular arc. Since the arcs bulge outward, a circle inside the triangle could be tangent to each arc at the point where the arc crosses... no.

Actually, let me think again. The semicircle on BC as diameter, drawn outside the triangle. The arc is below BC. For a circle inside the triangle (above BC) to be tangent to this arc, it would need to reach across BC. That doesn't work for tangency to the arc.

Alternatively, the tangent circle is also outside, in the region "below" all three arcs? That seems complicated.

Let me reconsider the problem. Maybe the tangent circle is tangent to the semicircles (as in tangent to the circular arcs), and it's located in the region enclosed by the three arcs. 

Actually, I recall this type of problem. The three semicircles on the sides of a triangle, drawn externally, and a circle tangent to all three. This is related to the "arbelos" generalization.

Let me think about it using the centers and radii. The tangent circle is tangent to each semicircle. For the tangency, the distance from the tangent circle's center to each semicircle's center equals the sum or difference of radii.

If the tangent circle is externally tangent to each semicircle (i.e., the tangent circle is outside each semicircle disk), then:
distance to M_a = t + 13/2
distance to M_b = t + 7
distance to M_c = t + 15/2

If internally tangent (tangent circle inside the semicircle disk), then distance = |R - t|.

Let me think about where the tangent circle is. The three semicircles bulge outward from the triangle. The region "inside" all three semicircular arcs... 

Actually, I think the answer might be that t = s/2, making t - s/2 = 0. Let me check.

There's a known result: For a triangle with semicircles on its sides (drawn externally), the circle tangent to all three semicircles has radius equal to s/2 (half the semiperimeter). This would make t - s/2 = 0.

Let me verify this. If t = s/2 = 10.5, let me check if there's a circle of radius 10.5 tangent to all three semicircles.

The center of such a circle would be at distance t + R_i from each midpoint (if externally tangent), or at distance |t - R_i| (if internally tangent).

With t = 10.5:
- Distance to M_a = 10.5 + 6.5 = 17, or |10.5 - 6.5| = 4
- Distance to M_b = 10.5 + 7 = 17.5, or |10.5 - 7| = 3.5
- Distance to M_c = 10.5 + 7.5 = 18, or |10.5 - 7.5| = 3

Hmm, let me think about which case. The inradius r = 4. The distances from the incenter to the midpoints of the sides...

Incenter I: weighted average by side lengths.
I = (a·A + b·B + c·C) / (a+b+c) where a is opposite A, etc.

Wait, incenter = (a·A + b·B + c·C)/(a+b+c) where a = BC, b = CA, c = AB.

I = (13·A + 14·B + 15·C) / 42

A = (99/13, 168/13), B = (0,0), C = (13, 0)

I_x = (13·(99/13) + 14·0 + 15·13) / 42 = (99 + 0 + 195) / 42 = 294/42 = 7
I_y = (13·(168/13) + 0 + 0) / 42 = 168/42 = 4

So incenter I = (7, 4). Makes sense, r = 4.

Distance from I to M_a = (13/2, 0): sqrt((7 - 6.5)² + 16) = sqrt(0.25 + 16) = sqrt(16.25) = sqrt(65)/2 ≈ 4.03

That's not 4. So the incenter is not the center of the tangent circle with internal tangency.

Let me reconsider. Maybe the tangent circle is externally tangent to all three semicircles, and its center is somewhere specific.

Actually, let me reconsider the problem. Maybe I should think about it as follows: the three semicircles drawn outside create a region, and there's a circle inscribed in the curvilinear triangle formed by the three arcs.

Let me think about Descartes' circle theorem or a direct approach.

Actually, let me reconsider. The problem says "a circle with radius t is tangent to all three semicircles." The semicircles are drawn outside the triangle. 

Let me think about the geometry more carefully. The three semicircular arcs, drawn outside, form a curvilinear triangle (like a rounded triangle pointing outward). A circle tangent to all three arcs from the outside (i.e., in the central region near the triangle) would be tangent to each arc.

But wait - the arcs are on the outside of the triangle. The central region (where the triangle is) is on the opposite side of each arc from where the arc bulges. So a circle in the triangle region would be tangent to the "back" of each semicircle... but the semicircle arc is only on one side.

Hmm, let me reconsider. The semicircle on BC with diameter BC, drawn outside the triangle (below BC). The arc goes from B to C below BC. A circle in the upper half (where the triangle is) can't be tangent to this arc unless it crosses BC.

So maybe the tangent circle is below BC, in the region of the semicircle. But then it needs to be tangent to all three semicircles which are on different sides.

Actually, I think the key insight is: the three semicircles, drawn externally, create three "lune" shapes. The circle tangent to all three is in the region that's inside all three semicircular disks but outside the triangle. Wait, no - the semicircles are on different sides.

Let me reconsider. Maybe the tangent circle is tangent to the semicircles from outside (externally tangent), meaning it doesn't overlap with any semicircle disk. The center would be at distance t + R_i from each midpoint.

Let me try to find such a point. We need a point P = (x, y) such that:
|P - M_a| = t + 13/2
|P - M_b| = t + 7
|P - M_c| = t + 15/2

This is the problem of finding a circle externally tangent to three circles (the full circles, not just semicircles). The solution is the outer Soddy circle or one of the Apollonius circles.

Actually, for three circles with radii R_a = 13/2, R_b = 7, R_c = 15/2, and centers at the midpoints of the sides, a circle externally tangent to all three...

Let me use the formula. If a circle of radius t is externally tangent to three circles of radii R_1, R_2, R_3 with centers at distances d_ij apart, we can use the system of equations.

Actually, let me think about this differently. There's a beautiful result here.

The midpoints of the sides of a triangle form the medial triangle. The sides of the medial triangle are a/2, b/2, c/2. The circumradius of the medial triangle is R/2 where R is the circumradius of the original triangle.

For the 13-14-15 triangle: R = abc/(4·Area) = 13·14·15/(4·84) = 2730/336 = 65/8.

The medial triangle has circumradius R/2 = 65/16.

Now, the three circles centered at the midpoints with radii a/2, b/2, c/2. A circle externally tangent to all three has radius t where:

The distance from the tangent circle's center to M_a is t + a/2, etc.

This is equivalent to finding a circle tangent to three circles. By the Soddy/Descartes approach or direct computation.

Let me try a different approach. Consider inverting or using the formula for the inscribed circle of the "arbelos-like" figure.

Actually, let me just try to compute directly. Let me use the Apollonius problem.

We have three circles:
- C_a: center (13/2, 0), radius 13/2
- C_b: center (134/13, 84/13), radius 7
- C_c: center (99/26, 84/13), radius 15/2

We want a circle externally tangent to all three, with center (x, y) and radius t.

(x - 13/2)² + y² = (t + 13/2)²
(x - 134/13)² + (y - 84/13)² = (t + 7)²
(x - 99/26)² + (y - 84/13)² = (t + 15/2)²

Let me expand the first equation:
x² - 13x + 169/4 + y² = t² + 13t + 169/4
x² + y² - 13x = t² + 13t

Second equation:
x² - 2·(134/13)x + (134/13)² + y² - 2·(84/13)y + (84/13)² = t² + 14t + 49
x² + y² - (268/13)x - (168/13)y + (134² + 84²)/169 = t² + 14t + 49

134² = 17956, 84² = 7056, sum = 25012. 25012/169 = 25012/169. Let me compute: 169 × 148 = 25012. Yes! So 25012/169 = 148.

So: x² + y² - (268/13)x - (168/13)y + 148 = t² + 14t + 49
x² + y² - (268/13)x - (168/13)y + 99 = t² + 14t

Third equation:
x² - 2·(99/26)x + (99/26)² + y² - (168/13)y + (84/13)² = t² + 15t + 225/4

(99/26)² = 9801/676. (84/13)² = 7056/169 = 28224/676.
Sum = (9801 + 28224)/676 = 38025/676. 

38025/676: 676 × 56 = 37856, 38025 - 37856 = 169, so 56 + 169/676 = 56 + 1/4 = 225/4. 

So: x² + y² - (99/13)x - (168/13)y + 225/4 = t² + 15t + 225/4
x² + y² - (99/13)x - (168/13)y = t² + 15t

Now from equation 1: x² + y² = t² + 13t + 13x

Substitute into equation 2:
t² + 13t + 13x - (268/13)x - (168/13)y + 99 = t² + 14t
13x - (268/13)x - (168/13)y + 99 = 14t - 13t
(169/13 - 268/13)x - (168/13)y + 99 = t
(-99/13)x - (168/13)y + 99 = t
t = 99 - (99/13)x - (168/13)y
t = 99 - (99x + 168y)/13

Substitute x² + y² = t² + 13t + 13x into equation 3:
t² + 13t + 13x - (99/13)x - (168/13)y = t² + 15t
13x - (99/13)x - (168/13)y = 15t - 13t
(169/13 - 99/13)x - (168/13)y = 2t
(70/13)x - (168/13)y = 2t
t = (70x - 168y)/(26) = (35x - 84y)/13

So we have two expressions for t:
t = 99 - (99x + 168y)/13 ... (I)
t = (35x - 84y)/13 ... (II)

Setting equal:
99 - (99x + 168y)/13 = (35x - 84y)/13
99·13 - 99x - 168y = 35x - 84y
1287 - 99x - 168y = 35x - 84y
1287 = 134x + 84y
134x + 84y = 1287

Divide by 2: 67x + 42y = 1287/2

Hmm, let me keep it as 134x + 84y = 1287.

From (II): t = (35x - 84y)/13

From 134x + 84y = 1287, we get 84y = 1287 - 134x, so y = (1287 - 134x)/84.

t = (35x - (1287 - 134x))/13 = (35x - 1287 + 134x)/13 = (169x - 1287)/13 = 13x - 99

So t = 13x - 99, which means x = (t + 99)/13.

And from 134x + 84y = 1287:
134·(t+99)/13 + 84y = 1287
(134/13)(t + 99) + 84y = 1287

134/13 = 134/13. 134 = 13·10 + 4, so 134/13 is not integer. Let me keep it.

84y = 1287 - (134/13)(t + 99) = 1287 - (134t + 134·99)/13 = (1287·13 - 134t - 13266)/13 = (16731 - 134t - 13266)/13 = (3465 - 134t)/13

y = (3465 - 134t)/(13·84) = (3465 - 134t)/1092

Now substitute into equation 1: x² + y² = t² + 13t + 13x

x = (t + 99)/13, so 13x = t + 99.

x² + y² = t² + 13t + t + 99 = t² + 14t + 99

x² = (t + 99)²/169

y² = (3465 - 134t)²/1092² = (3465 - 134t)²/1192464

Note 1092 = 84·13. 1092² = 1192464. And 169 = 13². 

Let me write everything over a common denominator. 1192464 = 84² · 169 = 7056 · 169. So 1192464/169 = 7056.

x² + y² = (t+99)²/169 + (3465-134t)²/1192464
= [7056(t+99)² + (3465-134t)²] / 1192464

And t² + 14t + 99 = [1192464(t² + 14t + 99)] / 1192464

So:
7056(t+99)² + (3465-134t)² = 1192464(t² + 14t + 99)

Let me expand. Let u = t for simplicity.

7056(u + 99)² = 7056(u² + 198u + 9801) = 7056u² + 1397088u + 69157056

(3465 - 134u)² = 134²u² - 2·3465·134u + 3465² = 17956u² - 928620u + 12006225

Sum = (7056 + 17956)u² + (1397088 - 928620)u + (69157056 + 12006225)
= 25012u² + 468468u + 81163281

RHS: 1192464(u² + 14u + 99) = 1192464u² + 16694496u + 118053936

So:
25012u² + 468468u + 81163281 = 1192464u² + 16694496u + 118053936

0 = (1192464 - 25012)u² + (16694496 - 468468)u + (118053936 - 81163281)
0 = 1167452u² + 16226028u + 36890655

Let me simplify. Divide by common factor. 

1167452, 16226028, 36890655.

Let me check GCD. 1167452 = 4·291863. 16226028 = 4·4056507. 36890655 = ? 36890655/3 = 12296885. 12296885/5 = 2459377. So 36890655 = 15·2459377. 

Is 291863 divisible by 3? 2+9+1+8+6+3 = 29, no. So GCD of 1167452 and 36890655... 1167452 = 2²·291863. 36890655 = 3·5·2459377. 291863 and 2459377 - let me check if 2459377/291863 ≈ 8.43, not integer. So GCD is likely 1 or small.

Let me just use the quadratic formula.

u = [-16226028 ± sqrt(16226028² - 4·1167452·36890655)] / (2·1167452)

Discriminant: 16226028² - 4·1167452·36890655

16226028² = let me compute. 16226028² = (1.6226028×10⁷)² ≈ 2.6328×10¹⁴. Let me be more precise.

Actually, this is getting very computational. Let me try a different approach.

Let me reconsider. Maybe the answer is indeed t = s/2 and I should verify it differently, or maybe there's a cleaner approach.

Actually, wait. Let me reconsider the problem. The problem asks for t - s/2. If the answer is 0, that's a clean answer. Let me check if t = 10.5 works.

If t = 10.5, then from t = 13x - 99: 10.5 = 13x - 99, so 13x = 109.5, x = 109.5/13 = 8.423...

From 134x + 84y = 1287: 134(109.5/13) + 84y = 1287. 134·109.5/13 = 14673/13 = 1128.69... 1287 - 1128.69 = 158.31, y = 158.31/84 = 1.885...

Let me check equation 1: x² + y² = t² + 13t + 13x
x² + y² = (109.5/13)² + (158.31/84)² 

This is getting messy. Let me try a cleaner approach.

Actually, let me reconsider whether the tangency is external or internal. Maybe the circle is internally tangent to the semicircles (i.e., the tangent circle is inside the semicircular disks). But the semicircles are on different sides of the triangle, so a single circle can't be inside all three half-disks simultaneously (they don't overlap).

Wait, actually the three semicircles drawn outside the triangle - do their half-disks overlap? The half-disk on BC (below BC), the half-disk on CA (on the side opposite B), the half-disk on AB (on the side opposite C). These three half-disks might overlap in some region, or they might not.

Actually, for an acute triangle, the three external semicircles' half-disks don't overlap with each other (they're on different sides). For the 13-14-15 triangle, let me check if it's acute. The largest side is 15. 15² = 225, 13² + 14² = 169 + 196 = 365 > 225. So the triangle is acute.

For an acute triangle, the external semicircles don't overlap. So the tangent circle must be externally tangent to all three (not inside any of them).

OK so let me continue with the computation. Let me try to be more careful.

Actually, let me try a completely different approach. Let me use the concept of the "inner Soddy circle" of three mutually tangent circles, but our three circles (the full circles on the sides as diameters) are not mutually tangent.

The three circles have centers at the midpoints of the sides and radii a/2, b/2, c/2. The distance between midpoints of sides:
- M_a and M_b: midpoint of BC and midpoint of CA. This distance = c/2 (half of AB, since the segment connecting midpoints of two sides equals half the third side).
- M_b and M_c: distance = a/2
- M_c and M_a: distance = b/2

So the three circles have:
- Radii: a/2, b/2, c/2
- Distances between centers: c/2, a/2, b/2

Check: Circle at M_a (radius a/2) and circle at M_b (radius b/2), distance between them = c/2.
For external tangency: a/2 + b/2 = c/2, i.e., a + b = c. Not generally true.
For the circles to be tangent: |a/2 - b/2| = c/2 or a/2 + b/2 = c/2. Neither holds in general.

So the three circles are not mutually tangent. The distance between M_a and M_b is c/2, and the radii are a/2 and b/2. Since a + b > c (triangle inequality), a/2 + b/2 > c/2, so the circles overlap! The two circles at M_a and M_b overlap.

Wait, that means the full circles overlap. But we're only considering semicircles (half-disks) drawn outside the triangle. The half-disks might not overlap even though the full circles do.

OK, this is getting complicated. Let me just solve the quadratic.

0 = 1167452u² + 16226028u + 36890655

Let me try to factor out common factors more carefully.

1167452 = 4 × 291863
16226028 = 4 × 4056507
36890655: is this divisible by 4? 36890655/4 = 9222663.75, no. So GCD includes at most 1 from the factor of 4.

Let me check if 291863 is prime. 291863 / 7 = 41694.7... no. /11 = 26533, let me check: 11 × 26533 = 291863. Yes! So 291863 = 11 × 26533.

26533 / 11 = 2412.09... no. /13 = 2041, let me check: 13 × 2041 = 26533. Yes! So 26533 = 13 × 2041.

2041 / 13 = 157. 13 × 157 = 2041. Yes! So 2041 = 13 × 157.

157 is prime.

So 291863 = 11 × 13 × 13 × 157 = 11 × 169 × 157.
1167452 = 4 × 11 × 169 × 157 = 44 × 169 × 157.

4056507: /3 = 1352169. /3 = 450723. /3 = 150241. Is 150241 divisible by 11? 1-5+0-2+4-1 = -3, no. By 13? 150241/13 = 11557. 13 × 11557 = 150241. Yes! 11557/13 = 889. 13 × 889 = 11557. Yes! 889 = 7 × 127. 127 is prime.

So 4056507 = 27 × 169 × 7 × 127 = 3³ × 7 × 13² × 127.
16226028 = 4 × 3³ × 7 × 13² × 127 = 2² × 3³ × 7 × 13² × 127.

36890655: /3 = 12296885. /5 = 2459377. 2459377 / 7 = 351339.57... no. /11 = 223579.7... no. /13 = 189183.6... let me check: 13 × 189183 = 2459379, not quite. /157 = 15666.8... no. 

Hmm, let me try differently. 2459377 / 127 = 19365.17... no. 

Let me try: 2459377 / 169 = 14558.7... no.

This is getting really messy. Let me just compute numerically.

u = [-16226028 ± sqrt(16226028² - 4 × 1167452 × 36890655)] / (2 × 1167452)

16226028² = 263,284,005,847,984 (approximately). Let me compute more carefully.

Actually, let me just compute the discriminant numerically.

16226028² ≈ 2.6328 × 10^14
4 × 1167452 × 36890655 ≈ 4 × 1.167452 × 10^6 × 3.6890655 × 10^7 ≈ 4 × 4.307 × 10^13 ≈ 1.723 × 10^14

Discriminant ≈ 2.6328 × 10^14 - 1.723 × 10^14 ≈ 0.91 × 10^14

sqrt ≈ 9.54 × 10^6

u = (-16226028 + 9540000) / 2334904 ≈ -6686028 / 2334904 ≈ -2.86 (negative, not valid)
or u = (-16226028 - 9540000) / 2334904 ≈ -25766028 / 2334904 ≈ -11.04 (negative, not valid)

Both roots are negative! That means there's no circle externally tangent to all three with positive radius. That makes sense because the three full circles overlap - you can't have a circle externally tangent to all three from outside.

So the tangency must be internal for some of the semicircles. Let me reconsider.

Since the semicircles are half-disks (not full circles), and they're drawn outside the triangle, the tangent circle is in the region of the triangle (or near it), tangent to the arcs.

Wait, I think I need to reconsider the geometry. The semicircle on BC drawn outside the triangle: the arc is below BC. A circle above BC (in the triangle) can be tangent to this arc only if it's tangent at a point on BC (the diameter), but the arc doesn't include the diameter as part of the arc (the arc is the curved part). 

Hmm, actually, maybe the problem means the semicircles include the diameter as part of the boundary, and the tangent circle is tangent to the straight part (the diameter) of each semicircle? No, that would just be the incircle.

Let me reconsider. Maybe the tangent circle is tangent to the curved arcs, and it's located in the region outside the triangle but "between" the three arcs. 

Actually, I think I've been overcomplicating this. Let me reconsider the setup.

The three semicircles are drawn outside the triangle. They bulge outward. The region "inside" all three arcs (i.e., the region that is inside all three half-disks) would be... the half-disk on BC is below BC, the half-disk on CA is on the far side from B, the half-disk on AB is on the far side from C. For an acute triangle, these three half-disks don't have a common intersection.

But the arcs themselves form a curvilinear boundary. The circle tangent to all three arcs from the "inside" (the triangle side) would be a circle that touches each arc from the triangle's side.

For the semicircle on BC (arc below BC), a circle above BC tangent to this arc: the tangency point would be on BC itself (the midpoint of the arc is directly below the midpoint of BC). Actually, the closest point of the arc to a point above BC is on the diameter BC. But the arc is the curved part, which is below BC.

I think I'm confusing myself. Let me reconsider: maybe the tangent circle is below all the arcs, in the exterior region, and it's internally tangent to each semicircle (i.e., the tangent circle is inside each half-disk).

But for an acute triangle, the three half-disks don't share a common region, so a circle can't be inside all three.

Let me try yet another interpretation: the tangent circle is externally tangent to the semicircular arcs, meaning it touches each arc from outside the half-disk. The center is at distance t + R_i from each midpoint (external tangency to the full circle), but we also need the tangency point to be on the arc (the correct half).

But we showed that external tangency to all three full circles gives negative t. So that doesn't work.

What if the tangent circle is internally tangent to some and externally tangent to others?

Let me think about this more carefully with the geometry. 

Actually, I wonder if the problem is about the circle inscribed in the curvilinear triangle formed by the three semicircular arcs. This is a well-known configuration.

Let me reconsider. The three semicircles on the sides of a triangle, drawn externally, form a shape. The "arbelos" of Archimedes is the case of three semicircles on a line. For a triangle, the three external semicircles create a figure, and there's a circle inscribed in the curvilinear triangle formed by the three arcs.

The curvilinear triangle is the region bounded by the three arcs. This region is the original triangle plus three "lune" regions... no.

Actually, the three arcs, drawn externally, bound a region that contains the triangle. The region inside all three arcs (on the triangle side of each arc) is the triangle itself plus the regions between the triangle sides and the arcs. Wait, no - the arcs are on the outside of the triangle, so the region on the triangle side of each arc includes the triangle and more.

Hmm, let me think about it differently. Each semicircular arc divides the plane into two regions: the half-disk (inside the semicircle) and the rest (outside). The three arcs, drawn externally, create a region that is the intersection of the three "outside" regions (outside all three half-disks). This region contains the triangle and extends to infinity. A circle tangent to all three arcs from outside would be in this region.

Alternatively, the region inside all three half-disks (intersection of the three half-disks) - for an acute triangle, this is empty (as I noted).

So the tangent circle is in the region outside all three half-disks, and it's externally tangent to each. But we showed that gives negative t for the full circles. 

Wait, but the semicircles are half-circles, not full circles. The external tangency to the full circle might not apply because the tangency point needs to be on the arc (the correct half).

Hmm, but if the tangent circle is outside all three half-disks and tangent to the arcs, the tangency point is on the arc, and the distance from the center to the midpoint is t + R_i (external tangency). The constraint that the tangency point is on the correct half is automatically satisfied if the center is on the correct side.

But we showed no positive t exists for external tangency to all three full circles. So maybe the tangent circle is on the same side as some arcs and the opposite side of others.

Let me reconsider the problem from scratch. Maybe I should consider that the tangent circle could be internally tangent to the semicircles (inside the half-disk) for some and externally tangent for others.

Actually, you know what, let me reconsider. Maybe the problem is simpler than I think. Let me re-read it.

"Semicircles with diameters BC, CA, AB are drawn outside of the triangle. A circle with radius t is tangent to all three semicircles."

I think the standard interpretation is: the three semicircles form a figure (like a rounded triangle), and there's a circle inscribed in the curvilinear triangular gap in the middle. But the "middle" is where the triangle is.

Actually, I think the correct interpretation is: the circle is tangent to all three semicircular arcs, and it's located in the region of the triangle. The circle is internally tangent to each semicircle (i.e., the tangent circle is on the opposite side of the diameter from the arc, so the distance from the center to the midpoint is |t - R_i|, and specifically t - R_i if t > R_i or R_i - t if R_i > t).

Wait, no. If the tangent circle is on the opposite side of the diameter from the arc, it's not inside the half-disk. The tangency would be with the full circle, on the opposite side from the arc. But the arc is only on one side, so the tangency point wouldn't be on the arc.

I think I need to reconsider. Let me think about what "tangent to a semicircle" means. A semicircle is a half-disk, which is a region bounded by a diameter and a semicircular arc. A circle tangent to a semicircle could be tangent to the arc (the curved part) or to the diameter (the straight part).

If tangent to the arc: the tangent circle touches the curved boundary. The center of the tangent circle is at distance t + R (external) or |t - R| (internal) from the midpoint of the diameter, and the tangency point is on the arc (the correct half of the full circle).

If the tangent circle is in the triangle region (opposite side from the arc), then for it to be tangent to the arc, it would need to reach across the diameter. The tangency point on the full circle would be on the opposite half from the arc. So it's tangent to the full circle but not to the arc. This doesn't work.

Unless... the tangent circle is large enough to encompass the semicircle. If t > R and the tangent circle contains the semicircle, then the tangency is internal, and the tangency point could be on the arc side.

Hmm, this is getting complicated. Let me try a different approach entirely.

Let me consider the possibility that the circle is tangent to the semicircles from the inside, meaning the tangent circle is in the half-disk region. But for an acute triangle, the three half-disks don't overlap, so this is impossible.

Wait, maybe I should check: do the three external semicircles of the 13-14-15 triangle overlap?

The half-disk on BC is below BC. The half-disk on CA is on the side of CA opposite to B. The half-disk on AB is on the side of AB opposite to C.

For the half-disk on BC (below BC) and the half-disk on AB (opposite side from C): 

The side AB goes from A(99/13, 168/13) to B(0,0). The side opposite from C(13,0). C is to the right. The half-disk on AB is to the left of AB (away from C).

The half-disk on BC is below BC (y < 0). The half-disk on AB is to the left of line AB. Do these overlap? Near vertex B, the half-disk on BC extends below B, and the half-disk on AB extends to the left of B. They might overlap near B.

Actually, at vertex B, both semicircles pass through B (since B is an endpoint of both diameters BC and AB). The half-disk on BC near B goes below BC, and the half-disk on AB near B goes to the left of AB. The angle at B: 

cos B = (a² + c² - b²)/(2ac) = (169 + 225 - 196)/(2·13·15) = 198/390 = 33/65.

The angle B is acute. The two half-disks near B are on the exterior sides, so they're on opposite sides of the angle at B. They don't overlap near B (they're separated by the exterior angle).

Actually, the half-disk on BC is on the side of BC opposite to A, and the half-disk on AB is on the side of AB opposite to C. At vertex B, the exterior region (outside the triangle) is divided by the extension of the sides. The two half-disks are in different parts of the exterior, so they don't overlap.

OK so for an acute triangle, the three external half-disks don't overlap. So the tangent circle can't be inside all three.

Let me reconsider the problem. Maybe the tangent circle is tangent to the semicircles from the outside (externally tangent to the full circles), and the issue is that I need to also consider the constraint that the tangency points are on the arcs.

But we showed that external tangency to all three full circles gives negative t. So maybe the configuration is different.

Wait, let me re-examine my computation. I assumed the tangent circle is externally tangent to all three (distance = t + R_i). Let me re-examine.

Actually, I realize I might have made an error. Let me reconsider: maybe the tangent circle is internally tangent to the semicircles, meaning the tangent circle contains each semicircle (t > R_i) or is contained in each (t < R_i). 

If the tangent circle contains each semicircle (t > R_i for all), then distance from center to midpoint = t - R_i. This would mean the tangent circle is large and encompasses all three semicircles.

Let me try this case:
(x - 13/2)² + y² = (t - 13/2)²
(x - 134/13)² + (y - 84/13)² = (t - 7)²
(x - 99/26)² + (y - 84/13)² = (t - 15/2)²

Expanding equation 1:
x² - 13x + 169/4 + y² = t² - 13t + 169/4
x² + y² - 13x = t² - 13t

Equation 2:
x² + y² - (268/13)x - (168/13)y + 148 = t² - 14t + 49
x² + y² - (268/13)x - (168/13)y + 99 = t² - 14t

Equation 3:
x² + y² - (99/13)x - (168/13)y = t² - 15t

From eq 1: x² + y² = t² - 13t + 13x

Sub into eq 2:
t² - 13t + 13x - (268/13)x - (168/13)y + 99 = t² - 14t
-13t + 13x - (268/13)x - (168/13)y + 99 = -14t
t + (169/13 - 268/13)x - (168/13)y + 99 = 0
t - (99/13)x - (168/13)y + 99 = 0
t = (99/13)x + (168/13)y - 99

Sub into eq 3:
t² - 13t + 13x - (99/13)x - (168/13)y = t² - 15t
-13t + (169/13 - 99/13)x - (168/13)y = -15t
2t + (70/13)x - (168/13)y = 0
t = -(70/13)x + (168/13)y = (168y - 70x)/13 = (84y - 35x)/13·... wait

t = (168y - 70x)/13

Wait, let me redo: 2t + (70/13)x - (168/13)y = 0
2t = (168/13)y - (70/13)x = (168y - 70x)/13
t = (168y - 70x)/26 = (84y - 35x)/13

Setting the two expressions for t equal:
(99x + 168y)/13 - 99 = (84y - 35x)/13
99x + 168y - 1287 = 84y - 35x
134x + 84y = 1287

Same equation as before! 134x + 84y = 1287.

And t = (84y - 35x)/13. From 134x + 84y = 1287: 84y = 1287 - 134x.
t = (1287 - 134x - 35x)/13 = (1287 - 169x)/13 = 99 - 13x

So t = 99 - 13x, x = (99 - t)/13.

From 134x + 84y = 1287:
134(99-t)/13 + 84y = 1287
(134·99 - 134t)/13 + 84y = 1287
(13266 - 134t)/13 + 84y = 1287
84y = 1287 - (13266 - 134t)/13 = (16731 - 13266 + 134t)/13 = (3465 + 134t)/13
y = (3465 + 134t)/(13·84) = (3465 + 134t)/1092

Now substitute into equation 1: x² + y² = t² - 13t + 13x

13x = 99 - t, so:
x² + y² = t² - 13t + 99 - t = t² - 14t + 99

x = (99-t)/13, x² = (99-t)²/169
y = (3465 + 134t)/1092, y² = (3465 + 134t)²/1192464

[(99-t)²·7056 + (3465+134t)²] / 1192464 = t² - 14t + 99

7056(99-t)² + (3465+134t)² = 1192464(t² - 14t + 99)

7056(99-t)² = 7056(t² - 198t + 9801) = 7056t² - 1397088t + 69157056

(3465+134t)² = 17956t² + 928620t + 12006225

Sum = 25012t² - 468468t + 81163281

RHS = 1192464t² - 16694496t + 118053936

0 = (1192464 - 25012)t² + (-16694496 + 468468)t + (118053936 - 81163281)
0 = 1167452t² - 16226028t + 36890655

Now the discriminant is the same: 16226028² - 4·1167452·36890655 (same as before since signs work out).

u = [16226028 ± sqrt(discriminant)] / (2·1167452)

The discriminant is the same as before. Let me compute it.

D = 16226028² - 4 × 1167452 × 36890655

Let me compute 16226028²:
16226028 = 16226028
16226028² = (16226000 + 28)² = 16226000² + 2·16226000·28 + 28²
= 263283076000000 + 908656000 + 784
= 263283984656784

Now 4 × 1167452 × 36890655:
1167452 × 36890655:
Let me compute step by step.
1167452 × 36890655

= 1167452 × (36000000 + 890655)
= 1167452 × 36000000 + 1167452 × 890655

1167452 × 36000000 = 1167452 × 36 × 10^6 = 42028272 × 10^6 = 42028272000000

1167452 × 890655:
= 1167452 × (900000 - 9345)
= 1167452 × 900000 - 1167452 × 9345

1167452 × 900000 = 1050706800000

1167452 × 9345:
= 1167452 × (9000 + 345)
= 1167452 × 9000 + 1167452 × 345

1167452 × 9000 = 10507068000

1167452 × 345:
= 1167452 × (300 + 45)
= 1167452 × 300 + 1167452 × 45

1167452 × 300 = 350235600
1167452 × 45 = 1167452 × (50 - 5) = 58372600 - 5837260 = 52535340

1167452 × 345 = 350235600 + 52535340 = 402770940

1167452 × 9345 = 10507068000 + 402770940 = 10909838940

1167452 × 890655 = 1050706800000 - 10909838940 = 1039796961060

1167452 × 36890655 = 42028272000000 + 1039796961060 = 43068068961060

4 × 43068068961060 = 172272275844240

D = 263283984656784 - 172272275844240 = 91011708812544

sqrt(D) = sqrt(91011708812544)

Let me compute: 9540000² = 91011600000000. Close!
9540000² = 91011600000000
D - 91011600000000 = 91011708812544 - 91011600000000 = 108812544

9540000² + 108812544. Let me try 9540057:
9540057² = 9540000² + 2·9540000·57 + 57² = 91011600000000 + 1087560000 + 3249 = 9101267563249. Too big.

Hmm, let me try 9540005:
9540005² = 9540000² + 2·9540000·5 + 25 = 91011600000000 + 95400000 + 25 = 91011695400025. 

D = 91011708812544. 91011708812544 - 91011695400025 = 13412519. 

9540005² + 13412519. Next: 9540005 + d, (9540005+d)² ≈ 9540005² + 2·9540005·d. 
2·9540005·d = 13412519, d ≈ 13412519/19080010 ≈ 0.703. Not integer.

So sqrt(D) is not an integer. Let me check if D is a perfect square.

D = 91011708812544

Let me factor: 91011708812544 = 16 × 5688231800784 (dividing by 16)
5688231800784 = 16 × 355514487549 (not integer, since 5688231800784/16 = 355514487549)

Actually 5688231800784 / 4 = 1422057950196
1422057950196 / 4 = 355514487549

So D = 64 × 355514487549? Let me check: 64 × 355514487549 = 22752927203136. No, that's not right.

Let me redo. D = 91011708812544.
D / 4 = 22752927203136
D / 16 = 5688231800784
D / 64 = 1422057950196
D / 256 = 355514487549

355514487549: is this divisible by small primes? 
Sum of digits: 3+5+5+5+1+4+4+8+7+5+4+9 = 60, divisible by 3. 355514487549 / 3 = 118504829183.

118504829183: sum = 1+1+8+5+0+4+8+2+9+1+8+3 = 50, not divisible by 3.
/7: 118504829183/7 = 16929261311.86... let me check: 7 × 16929261312 = 118504829184. Close but not exact.
/11: alternating sum: 3-8+1-9+2-8+4-0+5-8+1-1 = -18, not divisible by 11.
/13: 118504829183/13 = 9115756091.0. 13 × 9115756091 = 118504829183. Yes!

9115756091 / 13 = 701212006.23... no.
/7: 9115756091/7 = 1302250870.14... no.
/157: 9115756091/157 = 58049402.49... no.

This is getting very messy. Let me try a completely different approach to the problem.

Let me reconsider. Maybe I should think about this problem using inversion or some known formula.

Actually, let me reconsider the problem setup. Maybe the tangent circle is not tangent to the full circles but specifically to the semicircular arcs, and the tangency is such that the tangent circle is on the same side as the arc (i.e., in the half-disk region) for some and on the opposite side for others.

Actually, let me reconsider the problem. Perhaps the three semicircles, drawn outside, create a region that looks like a "curvilinear triangle" and the inscribed circle of this curvilinear triangle is what we seek.

The curvilinear triangle is the region bounded by the three arcs. This region is the original triangle plus the three "lune" regions between each side and its arc. Wait, no. The arcs are outside the triangle, so the region bounded by the three arcs includes the triangle and the lune regions.

Actually, the three arcs connect at the vertices of the triangle (since each semicircle has its diameter as a side of the triangle, and the arc goes from one vertex to another). So the three arcs form a closed curve: arc from B to C (below BC), arc from C to A (outside CA), arc from A to B (outside AB). This closed curve encloses a region that contains the triangle.

The circle inscribed in this curvilinear triangle (tangent to all three arcs from inside) would be in this enclosed region. The center would be somewhere near the triangle, and the tangency to each arc would be from the "inside" of the curvilinear triangle.

For the arc on BC (below BC), the inside of the curvilinear triangle is above the arc (toward the triangle). So the tangent circle is above the arc, meaning it's on the opposite side of the arc from the half-disk center. The distance from the tangent circle's center to M_a is t + R_a (external tangency to the full circle), and the tangency point is on the arc (below BC), which is the correct half.

Wait, but external tangency to the full circle means the tangent circle is outside the full circle. If the tangent circle is above BC and the arc is below BC, the tangent circle is outside the full circle (since the full circle extends both above and below BC, and the tangent circle is above BC but outside the circle). The tangency point would be on the upper half of the full circle (above BC), not on the arc (which is below BC). So this doesn't work.

Hmm. Let me think again.

If the tangent circle is inside the curvilinear triangle (which contains the original triangle), and it's tangent to the arc below BC, then the tangent circle must reach below BC to touch the arc. The tangent circle's center could be above BC, and the circle extends below BC to touch the arc.

In this case, the tangent circle overlaps with the full circle on BC. The tangency is internal: the tangent circle is internally tangent to the full circle (the tangent circle contains the full circle, or vice versa).

If the tangent circle contains the full circle on BC: distance from center to M_a = t - R_a (with t > R_a). The tangency point is on the arc side (below BC) if the center is above BC. This could work!

So the tangent circle is a large circle that contains all three full circles, and is internally tangent to each. The distance from its center to each midpoint is t - R_i.

This is the case I already computed! Let me continue with that.

0 = 1167452t² - 16226028t + 36890655

t = [16226028 ± sqrt(91011708812544)] / (2 × 1167452)

Let me compute sqrt(91011708812544) more carefully.

91011708812544. Let me try to see if this is a perfect square.

sqrt(91011708812544) ≈ 9540057.something

Let me try 9540057:
9540057² = ?
9540057 = 9540000 + 57
9540057² = 9540000² + 2×9540000×57 + 57²
= 91011600000000 + 1087560000 + 3249
= 9101267563249

That's way less than 91011708812544. Wait, I think I miscounted digits.

91011708812544 has 14 digits. 9540057² should have about 14 digits.
9540057² = 9101267563249 which has 13 digits. That's wrong.

Let me recompute. 9540057 ≈ 9.54 × 10^6. (9.54 × 10^6)² = 91.0 × 10^12 = 9.1 × 10^13. That's 14 digits. 

9540057² = 9540057 × 9540057.

Let me be more careful:
9540000² = 91011600000000 (this is 9.10016 × 10^13, 14 digits) ✓

2 × 9540000 × 57 = 1087560000

57² = 3249

9540057² = 91011600000000 + 1087560000 + 3249 = 91012687563249

Hmm wait: 91011600000000 + 1087560000 = 91012687560000, + 3249 = 91012687563249.

D = 91011708812544

91012687563249 - 91011708812544 = 978750705. So 9540057² is about 978750705 more than D.

So sqrt(D) ≈ 9540057 - 978750705/(2×9540057) ≈ 9540057 - 978750705/19080114 ≈ 9540057 - 51.3 ≈ 9540005.7

Let me try 9540005:
9540005² = 9540000² + 2×9540000×5 + 25 = 91011600000000 + 95400000 + 25 = 91011695400025

D - 91011695400025 = 91011708812544 - 91011695400025 = 13412519

9540006² = 9540005² + 2×9540005 + 1 = 91011695400025 + 19080011 = 91011714480036

91011714480036 > 91011708812544. So sqrt(D) is between 9540005 and 9540006.

So D is not a perfect square, and t is not a "nice" number. This suggests I might have the wrong tangency model.

Let me reconsider. Maybe the tangency is mixed: the tangent circle is externally tangent to some semicircles and internally tangent to others.

Actually, wait. Let me reconsider the geometry. The curvilinear triangle formed by the three arcs contains the original triangle. The inscribed circle of this curvilinear triangle is tangent to each arc from inside. 

For the arc on BC (below BC): the tangent circle is above the arc (inside the curvilinear triangle). The tangent circle and the full circle on BC: the tangent circle is outside the full circle (above BC, the full circle extends from -R_a to +R_a vertically, and the tangent circle is above). Actually, the full circle on BC has center at (13/2, 0) and radius 13/2, so it extends from y = -13/2 to y = 13/2. The tangent circle, if its center is above the triangle, might be outside this full circle.

If the tangent circle is externally tangent to the full circle on BC: distance = t + 13/2, and the tangency point is on the lower half of the full circle (the arc below BC). This works if the tangent circle's center is above the full circle.

But we showed that external tangency to all three gives negative t. So maybe it's external for some and internal for others.

Hmm, let me think about this differently. Let me consider the specific geometry.

The tangent circle is inside the curvilinear triangle. The curvilinear triangle is "fatter" than the original triangle (the arcs bulge outward). So the inscribed circle of the curvilinear triangle is larger than the incircle of the triangle.

For the arc on BC (below BC), the tangent circle (above BC, inside the curvilinear triangle) touches the arc from above. The tangent circle is outside the full circle on BC (since the full circle on BC is centered at (13/2, 0) with radius 13/2, and the tangent circle is above this). The tangency is external: distance = t + 13/2.

For the arc on CA (outside CA, away from B), the tangent circle (on the B side of CA, inside the curvilinear triangle) touches the arc from the B side. The tangent circle is outside the full circle on CA. External tangency: distance = t + 7.

Similarly for AB: external tangency, distance = t + 15/2.

So it should be external tangency to all three. But we showed that gives negative t. 

Wait, maybe I made a computational error. Let me recheck.

Actually, let me reconsider. The full circle on BC has center (13/2, 0) and radius 13/2. It extends from x = 0 to x = 13 and y = -13/2 to y = 13/2. The tangent circle, if centered above the triangle (say at (7, y) with y > 0), might be inside this full circle if y < 13/2 and the distance from (7, y) to (13/2, 0) is less than 13/2.

Distance from (7, 4) [incenter] to (13/2, 0) = sqrt(0.25 + 16) = sqrt(16.25) ≈ 4.03 < 6.5. So the incenter is inside the full circle on BC! 

So the tangent circle, if near the incenter, is inside the full circles. The tangency would be internal: the tangent circle is inside the full circle, and tangent to it from inside. Distance = R_i - t (if t < R_i).

But the tangent circle is tangent to the arc (lower half of the circle), not the upper half. If the tangent circle is inside the full circle and tangent to it, the tangency point is on the upper half (near the tangent circle), not on the arc (lower half). So this doesn't work either.

Unless the tangent circle is below the center of the full circle, in which case the tangency point is on the lower half (the arc). But the tangent circle is supposed to be inside the curvilinear triangle, which is above BC.

I'm going in circles (no pun intended). Let me try a completely different approach.

Let me reconsider: maybe the tangent circle is NOT inside the curvilinear triangle. Maybe it's in one of the lune regions, or maybe it's a different circle entirely.

Actually, re-reading the problem: "A circle with radius t is tangent to all three semicircles." It just says tangent to all three semicircles. It doesn't specify where. There might be multiple such circles (Apollonius problem has up to 8 solutions). The problem says "a circle," implying there's a unique one (or the relevant one).

Let me think about what circle is tangent to all three semicircles (arcs). The three arcs form a closed curve. There could be:
1. A circle inside the curvilinear triangle, tangent to all three arcs from inside.
2. Three circles, each in a lune region, tangent to two arcs and one side.
3. Other Apollonius circles.

For case 1, we need to figure out the correct tangency type.

Let me reconsider. The curvilinear triangle is the region enclosed by the three arcs. This region contains the original triangle. The "inscribed circle" of this curvilinear triangle is tangent to each arc from inside the curvilinear triangle.

For the arc on BC (below BC): inside the curvilinear triangle means above the arc. The tangent circle is above the arc. The full circle on BC has the arc as its lower half. The tangent circle, being above the arc, is on the opposite side from the half-disk. 

If the tangent circle is outside the full circle (above it), the tangency is external: distance = t + R_a, tangency point on the lower half (the arc). ✓
If the tangent circle is inside the full circle, the tangency is internal: distance = R_a - t, tangency point on the upper half (not the arc). ✗

So for the tangency point to be on the arc, the tangent circle must be outside the full circle, and the tangency is external.

But we showed external tangency to all three gives negative t. So there's no such circle?

Wait, maybe I made an error. Let me recheck the external tangency case.

External tangency: distance = t + R_i.
Equations:
(x - 13/2)² + y² = (t + 13/2)²
(x - 134/13)² + (y - 84/13)² = (t + 7)²
(x - 99/26)² + (y - 84/13)² = (t + 15/2)²

From eq 1: x² + y² - 13x = t² + 13t
From eq 2: x² + y² - (268/13)x - (168/13)y + 99 = t² + 14t
From eq 3: x² + y² - (99/13)x - (168/13)y = t² + 15t

From eq 1 and eq 2:
-13x + (268/13)x + (168/13)y - 99 = 13t - 14t = -t
(-169/13 + 268/13)x + (168/13)y - 99 = -t
(99/13)x + (168/13)y - 99 = -t
t = 99 - (99x + 168y)/13

From eq 1 and eq 3:
-13x + (99/13)x + (168/13)y = 13t - 15t = -2t
(-169/13 + 99/13)x + (168/13)y = -2t
(-70/13)x + (168/13)y = -2t
t = (70x - 168y)/26 = (35x - 84y)/13

Setting equal:
99 - (99x + 168y)/13 = (35x - 84y)/13
1287 - 99x - 168y = 35x - 84y
1287 = 134x + 84y

t = (35x - 84y)/13

From 134x + 84y = 1287: 84y = 1287 - 134x
t = (35x - 1287 + 134x)/13 = (169x - 1287)/13 = 13x - 99

So x = (t + 99)/13.

84y = 1287 - 134(t+99)/13 = (1287·13 - 134t - 134·99)/13 = (16731 - 134t - 13266)/13 = (3465 - 134t)/13
y = (3465 - 134t)/(13·84) = (3465 - 134t)/1092

Substitute into eq 1: x² + y² = t² + 13t + 13x = t² + 13t + t + 99 = t² + 14t + 99

((t+99)/13)² + ((3465-134t)/1092)² = t² + 14t + 99

(t+99)²/169 + (3465-134t)²/1192464 = t² + 14t + 99

Multiply by 1192464:
7056(t+99)² + (3465-134t)² = 1192464(t² + 14t + 99)

7056(t²+198t+9801) + (134²t² - 2·3465·134t + 3465²) = 1192464t² + 16694496t + 118053936

7056t² + 1397088t + 69157056 + 17956t² - 928620t + 12006225 = 1192464t² + 16694496t + 118053936

(7056+17956)t² + (1397088-928620)t + (69157056+12006225) = 1192464t² + 16694496t + 118053936

25012t² + 468468t + 81163281 = 1192464t² + 16694496t + 118053936

0 = 1167452t² + 16226028t + 36890655

Discriminant = 16226028² - 4·1167452·36890655 = 263283984656784 - 172272275844240 = 91011708812544

Since the coefficient of t² and the constant are both positive, and the coefficient of t is positive, both roots are negative (by Vieta's, sum of roots = -16226028/1167452 < 0, product = 36890655/1167452 > 0, so both roots negative). 

So indeed, no positive solution for external tangency to all three.

Now for internal tangency to all three (tangent circle contains all three full circles):
0 = 1167452t² - 16226028t + 36890655

t = [16226028 ± sqrt(91011708812544)] / 2334904

Both roots positive (sum = 16226028/1167452 > 0, product = 36890655/1167452 > 0).

sqrt(91011708812544) ≈ 9540005.7 (from earlier computation)

t₁ = (16226028 + 9540006) / 2334904 ≈ 25766034 / 2334904 ≈ 11.04
t₂ = (16226028 - 9540006) / 2334904 ≈ 6686022 / 2334904 ≈ 2.86

For the tangent circle to contain all three full circles, we need t > max(R_i) = 15/2 = 7.5. So t₁ ≈ 11.04 works, t₂ ≈ 2.86 doesn't.

But wait, does this configuration make geometric sense? The tangent circle contains all three full circles and is internally tangent to each. The tangency point for each would be on the far side of each full circle from the tangent circle's center. 

For the arc on BC (below BC), the tangency point needs to be on the arc (below BC). If the tangent circle's center is above BC, the tangency point with the full circle on BC is on the lower side (below BC), which is the arc. ✓

Similarly for the other arcs, if the tangent circle's center is inside the triangle, the tangency points would be on the arcs (the exterior sides). ✓

So this is the correct configuration! The tangent circle is a large circle centered inside the triangle, containing all three full circles, internally tangent to each, with tangency points on the arcs.

So t ≈ 11.04. And s/2 = 10.5. So t - s/2 ≈ 0.54. That doesn't seem like a clean answer.

Let me compute more precisely.

t = (16226028 - sqrt(91011708812544)) / 2334904 (taking the smaller root, which is the one where the tangent circle is "just barely" containing the circles, i.e., the inscribed circle of the curvilinear triangle)

Wait, actually, which root corresponds to the inscribed circle? The larger root (t₁ ≈ 11.04) would be a bigger circle, and the smaller root (t₂ ≈ 2.86) would be smaller. But t₂ < 7.5, so it can't contain the full circles. So t₁ is the answer.

Hmm, but 11.04 - 10.5 = 0.54, not a clean number. Let me check if the discriminant is actually a perfect square and I made an arithmetic error.

Let me recompute D = 16226028² - 4 × 1167452 × 36890655.

Actually, let me recheck my expansion. Let me recompute 7056 × 9801:
7056 × 9801 = 7056 × (10000 - 199) = 70560000 - 1404144 = 69155856

Wait, I had 69157056 before. Let me recheck.
7056 × 9801:
7056 × 9000 = 63504000
7056 × 800 = 5644800
7056 × 1 = 7056
Total = 63504000 + 5644800 + 7056 = 69155856

I had 69157056 before, which is wrong! Let me redo.

7056 × 9801 = 69155856. The difference is 69157056 - 69155856 = 1200.

Let me also recheck 3465²:
3465² = (3500 - 35)² = 12250000 - 245000 + 1225 = 12006225. ✓

And 2 × 3465 × 134 = 6930 × 134 = 928620. ✓

And 7056 × 198 = 7056 × 200 - 7056 × 2 = 1411200 - 14112 = 1397088. ✓

So the constant term: 69155856 + 12006225 = 81162081 (not 81163281 as I had before).

Let me redo the equation:
25012t² + 468468t + 81162081 = 1192464t² + 16694496t + 118053936

0 = 1167452t² + 16226028t + 36891855

Wait, 118053936 - 81162081 = 36891855 (not 36890655).

The difference: 36891855 - 36890655 = 1200. Same as the error in the constant term.

So the correct equation for external tangency is:
0 = 1167452t² + 16226028t + 36891855

And for internal tangency:
0 = 1167452t² - 16226028t + 36891855

Discriminant = 16226028² - 4 × 1167452 × 36891855

Let me recompute 4 × 1167452 × 36891855.

1167452 × 36891855:
= 1167452 × (36000000 + 891855)
= 1167452 × 36000000 + 1167452 × 891855

1167452 × 36000000 = 42028272000000

1167452 × 891855:
= 1167452 × (900000 - 8145)
= 1167452 × 900000 - 1167452 × 8145

1167452 × 900000 = 1050706800000

1167452 × 8145:
= 1167452 × (8000 + 145)
= 1167452 × 8000 + 1167452 × 145

1167452 × 8000 = 9339616000

1167452 × 145:
= 1167452 × (100 + 45)
= 116745200 + 52535340
= 169280540

1167452 × 8145 = 9339616000 + 169280540 = 9508896540

1167452 × 891855 = 1050706800000 - 9508896540 = 1041197903460

1167452 × 36891855 = 42028272000000 + 1041197903460 = 43069469903460

4 × 43069469903460 = 172277879613840

D = 263283984656784 - 172277879613840 = 91006105042944

Hmm, let me double-check 16226028²:
16226028² = (16226000 + 28)² = 16226000² + 2 × 16226000 × 28 + 784

16226000² = (16226)² × 10^6 = 263282276 × 10^6 = 263282276000000

Wait, 16226² = ?
16226² = (16000 + 226)² = 256000000 + 7232000 + 51076 = 263283076

So 16226000² = 263283076000000

2 × 16226000 × 28 = 909656000

16226028² = 263283076000000 + 909656000 + 784 = 263283985656784

Hmm, I had 263283984656784 before. The difference is 263283985656784 - 263283984656784 = 1000000. Let me recheck.

16226² = 16226 × 16226.
16226 × 16000 = 259616000
16226 × 226 = 16226 × 200 + 16226 × 26 = 3245200 + 421876 = 3667076
Total = 259616000 + 3667076 = 263283076. ✓

16226000² = 263283076 × 10^6 = 263283076000000. ✓

2 × 16226000 × 28 = 16226000 × 56 = 909656000. ✓

28² = 784. ✓

16226028² = 263283076000000 + 909656000 + 784 = 263283985656784

So I had an error before (263283984656784 vs 263283985656784, difference of 1000000).

D = 263283985656784 - 172277879613840 = 91006106042944

Let me check if this is a perfect square.

sqrt(91006106042944) ≈ ?

9539700² = ?
95397² = ?
95397 × 95397:
95397 × 95000 = 9062715000
95397 × 397 = 95397 × 400 - 95397 × 3 = 38158800 - 286191 = 37872609
Total = 9062715000 + 37872609 = 9100587609

9539700² = 9100587609 × 10^4 = 91005876090000

D - 91005876090000 = 91006106042944 - 91005876090000 = 229952944

9539700² + 229952944. 
(9539700 + d)² ≈ 9539700² + 2 × 9539700 × d
2 × 9539700 × d = 229952944
d = 229952944 / 19079400 ≈ 12.05

9539712² = 9539700² + 2 × 9539700 × 12 + 144 = 91005876090000 + 229492800 + 144 = 91006105582944

D - 91006105582944 = 91006106042944 - 91006105582944 = 460000

9539712² + 460000. 
(9539712 + d)² ≈ 9539712² + 2 × 9539712 × d
2 × 9539712 × d = 460000
d = 460000 / 19079424 ≈ 0.0241

Not an integer. So D is not a perfect square.

Hmm, this is problematic. The answer t - s/2 should be a clean number for a competition problem. Let me reconsider my approach.

Maybe I have the wrong model. Let me reconsider the problem.

Actually, wait. Let me reconsider whether the tangent circle is internally tangent to the full circles (containing them) or whether there's a different configuration.

Actually, I just realized something. The problem says "semicircles," not "circles." A semicircle is a half-disk. When we say a circle is "tangent to a semicircle," it could mean tangent to the boundary of the half-disk, which includes both the arc and the diameter.

If the tangent circle is tangent to the diameter (the straight side) of each semicircle, then it's tangent to the three sides of the triangle, which is the incircle! The incircle has radius r = 4. But the incircle is tangent to the sides (diameters) from inside the triangle, and the semicircles are drawn outside. The incircle is on the opposite side of each diameter from the semicircle. Is the incircle "tangent to the semicircle"? 

If "tangent to the semicircle" means tangent to the boundary of the half-disk, then the incircle is tangent to the diameter part of the boundary. But the incircle is on the opposite side from the half-disk, so it's tangent to the diameter from outside the half-disk. This could count as tangent to the semicircle.

But then t = r = 4, and t - s/2 = 4 - 10.5 = -6.5. That's a possible answer but seems unlikely for a competition.

Actually, no. The incircle is tangent to the sides of the triangle, which are the diameters of the semicircles. But the incircle is on the interior side, while the semicircles are on the exterior side. The incircle touches the diameter at the same point regardless of which side the semicircle is on. So the incircle is tangent to the straight edge of each semicircle. But is this what the problem means?

I think the problem means tangent to the curved part (the arc). Let me reconsider.

Actually, let me try a completely different approach. Let me think about what happens if we invert or use some transformation.

Hmm, let me try yet another approach. Let me consider the possibility that the tangent circle is tangent to the semicircles from the same side as the arcs (i.e., the tangent circle is in the half-disk region for each semicircle). But we showed the half-disks don't overlap for an acute triangle.

Wait, actually, I should double-check this. The half-disks are on the exterior of the triangle. Do they overlap?

Half-disk on BC: below BC (y < 0, roughly).
Half-disk on CA: on the side of CA opposite to B.
Half-disk on AB: on the side of AB opposite to C.

Let me check if the half-disk on BC and the half-disk on AB overlap.

The half-disk on BC is the set of points inside the circle centered at (13/2, 0) with radius 13/2, and below BC (y < 0).
The half-disk on AB is the set of points inside the circle centered at (99/26, 84/13) with radius 15/2, and on the side of AB opposite to C.

The line AB goes from (0,0) to (99/13, 168/13). The direction is (99, 168)/13. The normal pointing away from C: C = (13, 0). 

The line AB: 168x - 99y = 0 (since it passes through origin with direction (99, 168)). At C = (13, 0): 168 × 13 - 99 × 0 = 2184 > 0. So the side of AB containing C is where 168x - 99y > 0. The half-disk on AB is where 168x - 99y < 0.

The half-disk on BC is where y < 0 (below BC, which is the x-axis).

Do these overlap? We need a point where y < 0 and 168x - 99y < 0, i.e., 168x < 99y. Since y < 0, 99y < 0, so 168x < 99y < 0, meaning x < 0. 

Also, the point must be inside both circles. The circle on BC: (x - 13/2)² + y² < (13/2)², which means x² - 13x + y² < 0, i.e., x² + y² < 13x. Since x < 0, 13x < 0, but x² + y² ≥ 0, so x² + y² < 13x < 0 is impossible. So the half-disks on BC and AB don't overlap. ✓

OK so the half-disks don't overlap. The tangent circle must be in the region outside all three half-disks (the curvilinear triangle region containing the original triangle).

Let me reconsider. In this region, the tangent circle is on the opposite side of each diameter from the arc. For the tangency to be with the arc (not the diameter), the tangent circle must reach across the diameter to touch the arc. This means the tangent circle overlaps with the full circle, and the tangency is internal (the tangent circle contains the full circle, or is contained in it).

If the tangent circle contains the full circle (t > R_i), the distance from center to midpoint is t - R_i, and the tangency point is on the far side of the full circle from the tangent circle's center. If the center is inside the triangle (above BC), the tangency point with the circle on BC is below BC (on the arc). ✓

This is the internal tangency case I computed. t ≈ 11.04.

But the answer isn't clean. Let me re-examine my computation more carefully.

Actually, let me try to simplify the equation. 

0 = 1167452t² - 16226028t + 36891855

Let me try to factor out common factors.

1167452 = 4 × 291863 = 4 × 11 × 26533 = 4 × 11 × 13 × 2041 = 4 × 11 × 13 × 13 × 157 = 4 × 11 × 13² × 157

16226028 = 4 × 4056507 = 4 × 3³ × 7 × 13² × 127

36891855: Let me factor this.
36891855 / 3 = 12297285
12297285 / 3 = 4099095
4099095 / 3 = 1366365
1366365 / 3 = 455455
455455 / 5 = 91091
91091 / 7 = 13013
13013 / 7 = 1859
1859 / 13 = 143
143 / 11 = 13
13 / 13 = 1

So 36891855 = 3⁴ × 5 × 7² × 13² × 11 = 3⁴ × 5 × 7² × 11 × 13²

Let me verify: 3⁴ = 81, 81 × 5 = 405, 405 × 49 = 19845, 19845 × 11 = 218295, 218295 × 169 = 36891855. 
218295 × 169 = 218295 × 170 - 218295 = 37110150 - 218295 = 36891855. ✓

So:
1167452 = 2² × 11 × 13² × 157
16226028 = 2² × 3³ × 7 × 13² × 127
36891855 = 3⁴ × 5 × 7² × 11 × 13²

GCD = 13² = 169.

1167452 / 169 = 6914
16226028 / 169 = 96012
36891855 / 169 = 218295

Let me verify: 169 × 6914 = 169 × 7000 - 169 × 86 = 1183000 - 14534 = 1168466. That's not 1167452.

Hmm, let me recompute. 1167452 / 169:
169 × 6000 = 1014000
1167452 - 1014000 = 153452
169 × 900 = 152100
153452 - 152100 = 1352
169 × 8 = 1352
So 1167452 / 169 = 6908.

Let me verify: 169 × 6908 = 169 × 7000 - 169 × 92 = 1183000 - 15548 = 1167452. ✓

16226028 / 169:
169 × 96000 = 16224000
16226028 - 16224000 = 2028
169 × 12 = 2028
So 16226028 / 169 = 96012. ✓

36891855 / 169 = 218295. ✓ (verified above)

So the equation becomes:
6908t² - 96012t + 218295 = 0

Let me check GCD of 6908, 96012, 218295.
6908 = 4 × 1727 = 4 × 11 × 157
96012 = 4 × 24003 = 4 × 3 × 8001 = 4 × 3 × 3 × 2667 = 4 × 9 × 2667 = 4 × 9 × 3 × 889 = 4 × 27 × 889 = 4 × 27 × 7 × 127
218295 = 3⁴ × 5 × 7² × 11 = 81 × 5 × 49 × 11

GCD: 6908 has factors 2² × 11 × 157. 96012 has 2² × 3³ × 7 × 127. 218295 has 3⁴ × 5 × 7² × 11.
Common factors: 6908 and 96012 share 2² = 4. 218295 is odd, so no factor of 2. So GCD = 1.

So the simplified equation is 6908t² - 96012t + 218295 = 0.

Discriminant = 96012² - 4 × 6908 × 218295

96012² = ?
96012² = (96000 + 12)² = 9216000000 + 2304000 + 144 = 9218304144

4 × 6908 × 218295:
6908 × 218295 = ?
6908 × 200000 = 1381600000
6908 × 18000 = 124344000
6908 × 295 = 6908 × 300 - 6908 × 5 = 2072400 - 34540 = 2037860
Total = 1381600000 + 124344000 + 2037860 = 1509981860

4 × 1509981860 = 6039927440

D = 9218304144 - 6039927440 = 3178376704

sqrt(3178376704) = ?
56376² = ?
56000² = 3136000000
56376² = (56000 + 376)² = 3136000000 + 42112000 + 141376 = 3180353376

Too big. 3180353376 - 3178376704 = 1976672.

56350² = (56000 + 350)² = 3136000000 + 39200000 + 122500 = 3175322500

3178376704 - 3175322500 = 3054204

56358² = 56350² + 2 × 56350 × 8 + 64 = 3175322500 + 901600 + 64 = 3176224164
56360² = 56358² + 2 × 56358 × 2 + 4 = 3176224164 + 225432 + 4 = 3176449600
56370² = 56360² + 2 × 56360 × 10 + 100 = 3176449600 + 1127200 + 100 = 3177576900
56380² = 56370² + 2 × 56370 × 10 + 100 = 3177576900 + 1127400 + 100 = 3178704400

3178704400 > 3178376704. So between 56370 and 56380.

56377² = 56370² + 2 × 56370 × 7 + 49 = 3177576900 + 789180 + 49 = 3178366129
56378² = 56377² + 2 × 56377 + 1 = 3178366129 + 112755 = 3178478884

3178478884 > 3178376704. So between 56377 and 56378.

3178376704 - 3178366129 = 10575. Not a perfect square.

So the discriminant is not a perfect square, and t is irrational. This means t - s/2 is also irrational, which is unusual for a competition problem asking to "calculate the value."

Let me reconsider the problem. Maybe I have the wrong tangency model.

Let me reconsider: maybe the problem is about the circle inscribed in the curvilinear triangle formed by the three semicircular arcs, but the tangency is with the arcs from inside, and the distance relationship is different from what I assumed.

Actually, wait. I think the issue might be that the tangent circle is externally tangent to the semicircles (the half-disks), not the full circles. Being externally tangent to a half-disk means the tangent circle is outside the half-disk and tangent to its boundary. The boundary includes the arc and the diameter. If the tangent circle is tangent to the arc (not the diameter), and it's outside the half-disk, then it's on the opposite side of the diameter from the arc. The distance from the center to the midpoint is t + R (external to the full circle), and the tangency point is on the arc side.

But wait, if the tangent circle is on the opposite side of the diameter from the arc, and externally tangent to the full circle, the tangency point is on the near side (the tangent circle's side), which is the opposite side from the arc. So the tangency point is NOT on the arc. Contradiction.

Unless the tangent circle is on the same side as the arc (inside the half-disk region), and externally tangent to the full circle. Then the tangency point is on the arc side. But then the tangent circle is in the half-disk region, and we showed the half-disks don't overlap.

I'm stuck. Let me try a completely different approach.

Let me reconsider the problem. Maybe "semicircles with diameters BC, CA, AB drawn outside the triangle" and "a circle tangent to all three semicircles" refers to a different geometric configuration than what I've been considering.

Perhaps the tangent circle is in the "gap" between the three semicircles, outside the triangle but between the arcs. But for an acute triangle, the arcs are on the far side of each side, and the gaps between them are at the vertices.

Actually, you know what, let me try the problem with a different tangency model. What if the tangent circle is internally tangent to some semicircles and externally tangent to others?

Let me try: the tangent circle is inside the curvilinear triangle (containing the original triangle), and it's tangent to each arc. For each arc, the tangent circle is on the opposite side of the diameter from the arc. The tangent circle overlaps with the full circle (since it reaches across the diameter to touch the arc). The tangency is internal: the full circle is inside the tangent circle (t > R_i), and the distance is t - R_i.

This is what I computed, giving t ≈ 11.04. But the answer isn't clean.

Alternatively, the tangent circle is smaller than the full circles (t < R_i), and it's inside the full circle, tangent to it from inside. The distance is R_i - t. The tangency point is on the tangent circle's side of the full circle's center. If the tangent circle is above BC (inside the triangle) and the full circle on BC has center on BC, the tangency point is above BC (the upper half of the full circle, not the arc). So the tangency point is not on the arc. This doesn't work.

Hmm, unless the tangent circle is below BC (in the half-disk region). But then it can't be in the triangle region for all three simultaneously.

I think the internal tangency (tangent circle contains the full circles) is the right model, and the answer is just not a "nice" number. But the problem says "calculate the value of t - s/2," implying a specific numerical answer.

Let me try to compute t more precisely and see if t - s/2 simplifies.

t = (96012 + sqrt(3178376704)) / (2 × 6908) = (96012 + sqrt(3178376704)) / 13816

sqrt(3178376704) ≈ 56377.094

t ≈ (96012 + 56377.094) / 13816 ≈ 152389.094 / 13816 ≈ 11.0358

t - s/2 ≈ 11.0358 - 10.5 = 0.5358

That's not clean. Let me try the other root:
t = (96012 - 56377.094) / 13816 ≈ 39634.906 / 13816 ≈ 2.869

This is less than 7.5, so it can't contain the full circles. Not valid for this model.

Hmm, let me reconsider the problem entirely. Maybe I'm wrong about the tangency model.

Let me re-read the problem: "Semicircles with diameters BC, CA, AB are drawn outside of the triangle. A circle with radius t is tangent to all three semicircles."

Maybe "tangent to all three semicircles" means tangent to the three semicircular arcs, and the circle is in the region between the arcs (the curvilinear triangle). The tangency is such that the circle touches each arc from inside the curvilinear triangle.

For the curvilinear triangle (region containing the original triangle, bounded by the three arcs), the inscribed circle touches each arc from inside. The inscribed circle is in the original triangle region, and it reaches out to touch each arc.

For the arc on BC (below BC): the inscribed circle is above BC, and it touches the arc below BC. The inscribed circle must extend below BC to reach the arc. This means the inscribed circle is large enough to cross BC.

The distance from the inscribed circle's center to the midpoint of BC: if the inscribed circle contains the full circle on BC (t > 13/2), then distance = t - 13/2, and the tangency point is on the far side (below BC, on the arc). ✓

This is the model I've been using. Let me try to see if maybe I made an error in the coordinate setup.

Let me recheck the coordinates.

B = (0, 0), C = (13, 0), A = (99/13, 168/13).

Check: AB = sqrt((99/13)² + (168/13)²) = sqrt((9801 + 28224)/169) = sqrt(38025/169) = 195/13 = 15. ✓
AC = sqrt((99/13 - 13)² + (168/13)²) = sqrt((99/13 - 169/13)² + (168/13)²) = sqrt((-70/13)² + (168/13)²) = sqrt((4900 + 28224)/169) = sqrt(33124/169) = 182/13 = 14. ✓

Midpoints:
M_a = midpoint of BC = (13/2, 0) ✓
M_b = midpoint of CA = ((13 + 99/13)/2, (0 + 168/13)/2) = ((169/13 + 99/13)/2, 84/13) = (268/26, 84/13) = (134/13, 84/13) ✓
M_c = midpoint of AB = (99/26, 84/13) ✓

Radii: a/2 = 13/2, b/2 = 7, c/2 = 15/2 ✓

These all look correct. Let me recheck the equations.

For internal tangency (tangent circle contains the full circles):
|P - M_a| = t - 13/2
|P - M_b| = t - 7
|P - M_c| = t - 15/2

Squaring:
(x - 13/2)² + y² = (t - 13/2)² = t² - 13t + 169/4
x² - 13x + 169/4 + y² = t² - 13t + 169/4
x² + y² - 13x = t² - 13t ... (1)

(x - 134/13)² + (y - 84/13)² = (t - 7)² = t² - 14t + 49
x² - (268/13)x + (134/13)² + y² - (168/13)y + (84/13)² = t² - 14t + 49

(134/13)² + (84/13)² = (17956 + 7056)/169 = 25012/169 = 148

x² + y² - (268/13)x - (168/13)y + 148 = t² - 14t + 49
x² + y² - (268/13)x - (168/13)y + 99 = t² - 14t ... (2)

(x - 99/26)² + (y - 84/13)² = (t - 15/2)² = t² - 15t + 225/4

(99/26)² + (84/13)² = 9801/676 + 7056/169 = 9801/        — AI历史解题过程（thinking）
#   polymath_05423         — 题目ID

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
  <problem_id>polymath_05423</problem_id>
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

Let $\triangle ABC$ be a triangle with side lengths $a, b, c$, semiperimeter $s$, and inradius $r$. Semicircles with diameters $BC, CA, AB$ are drawn outside of the triangle. A circle with radius $t$ is tangent to all three semicircles. If $a=13, b=14$, and $c=15$, calculate the value of $t - \frac{s}{2}$.

## Standard Solution

From the original solution, the radius $t$ of the circle tangent to the three semicircles is given by $t = g + \frac{s}{2}$, where $g$ satisfies the relation $\frac{1}{2g} = \frac{1}{s-a} + \frac{1}{s-b} + \frac{1}{s-c} + \frac{2}{r}$. For a triangle with sides $13, 14, 15$, the semiperimeter is $s = \frac{13+14+15}{2} = 21$. The area is $A = \sqrt{21(21-13)(21-14)(21-15)} = \sqrt{21 \cdot 8 \cdot 7 \cdot 6} = \sqrt{7056} = 84$. The inradius is $r = A/s = 84/21 = 4$. Substituting these values: $s-a = 8, s-b = 7, s-c = 6$. Then $\frac{1}{2g} = \frac{1}{8} + \frac{1}{7} + \frac{1}{6} + \frac{2}{4} = \frac{21+24+28+84}{168} = \frac{157}{168}$. Thus $2g = \frac{168}{157}$, so $g = \frac{84}{157}$. Since $t - \frac{s}{2} = g$, the answer is $\frac{84}{157}$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. First, answer leak check - the problem text doesn't contain any leaked answers or solution sketches. Good.

Let me solve the problem.

We have triangle ABC with sides a=13, b=14, c=15. Semicircles drawn outside the triangle on diameters BC, CA, AB. A circle of radius t tangent to all three semicircles. Find t - s/2.

First, s = (13+14+15)/2 = 21. So s/2 = 10.5.

Area of triangle 13-14-15: Using Heron's formula, area = sqrt(21·8·7·6) = sqrt(21·336) = sqrt(7056) = 84. So r = area/s = 84/21 = 4.

Now the semicircles. Semicircle on BC (diameter a=13) has radius 13/2. On CA (diameter b=14) has radius 7. On AB (diameter c=15) has radius 15/2.

These are drawn outside the triangle. We need a circle tangent to all three semicircles.

Let me think about this. The semicircles are on the sides as diameters, drawn outside the triangle. A circle tangent to all three.

Let me set up coordinates. Place the triangle. Let me think about the geometry.

Actually, there's a known result related to this. The three semicircles on the sides of a triangle, drawn externally, form a shape. A circle tangent to all three...

Let me think about the centers. The center of the semicircle on BC is the midpoint of BC. The semicircle is drawn outside the triangle, so it's the arc on the side opposite to A.

Let me set up coordinates. Let B = (0,0), C = (13, 0). Then a = BC = 13.

Find A: AB = c = 15, AC = b = 14.
A = (x, y) where x² + y² = 225, (x-13)² + y² = 196.
x² - (x-13)² = 225 - 196 = 29
x² - x² + 26x - 169 = 29
26x = 198
x = 198/26 = 99/13
y² = 225 - (99/13)² = 225 - 9801/169 = (225·169 - 9801)/169 = (38025 - 9801)/169 = 28224/169
y = 168/13 (since area = (1/2)(13)(y) = 84, so y = 168/13). Yes.

So A = (99/13, 168/13).

Midpoints:
- M_a (midpoint of BC) = (13/2, 0), radius of semicircle = 13/2
- M_b (midpoint of CA) = ((13 + 99/13)/2, (0 + 168/13)/2) = ((169/13 + 99/13)/2, 84/13) = (268/26, 84/13) = (134/13, 84/13), radius = 7
- M_c (midpoint of AB) = ((0 + 99/13)/2, (0 + 168/13)/2) = (99/26, 84/13), radius = 15/2

The semicircles are drawn outside the triangle. The center of the tangent circle should be on the same side as the triangle interior? No - the semicircles bulge outward, so the tangent circle is likely in the region where the semicircles are, which is outside the triangle.

Actually, let me think about this differently. The semicircle on BC outside the triangle means the arc is on the opposite side of BC from A. Since A is above BC (y > 0), the semicircle on BC is below BC (y < 0).

Similarly, semicircle on CA is on the opposite side of CA from B, and semicircle on AB is on the opposite side of AB from C.

So the three semicircle arcs are all outside the triangle, bulging outward. A circle tangent to all three would be... in the interior of the triangle? Or somewhere else?

Hmm, if the semicircles bulge outward, a circle tangent to all three from the inside (i.e., in the triangle region) would be tangent to the arcs. But the arcs are on the far side. Actually, the semicircle includes the diameter as part of its boundary (the flat part), and the arc. The "semicircle" as a region is the half-disk.

Wait, I think the problem means the arcs only. A circle tangent to all three semicircular arcs.

Let me reconsider. The tangent circle is likely inside the triangle, tangent to each semicircular arc. Since the arcs bulge outward, a circle inside the triangle could be tangent to each arc at the point where the arc crosses... no.

Actually, let me think again. The semicircle on BC as diameter, drawn outside the triangle. The arc is below BC. For a circle inside the triangle (above BC) to be tangent to this arc, it would need to reach across BC. That doesn't work for tangency to the arc.

Alternatively, the tangent circle is also outside, in the region "below" all three arcs? That seems complicated.

Let me reconsider the problem. Maybe the tangent circle is tangent to the semicircles (as in tangent to the circular arcs), and it's located in the region enclosed by the three arcs. 

Actually, I recall this type of problem. The three semicircles on the sides of a triangle, drawn externally, and a circle tangent to all three. This is related to the "arbelos" generalization.

Let me think about it using the centers and radii. The tangent circle is tangent to each semicircle. For the tangency, the distance from the tangent circle's center to each semicircle's center equals the sum or difference of radii.

If the tangent circle is externally tangent to each semicircle (i.e., the tangent circle is outside each semicircle disk), then:
distance to M_a = t + 13/2
distance to M_b = t + 7
distance to M_c = t + 15/2

If internally tangent (tangent circle inside the semicircle disk), then distance = |R - t|.

Let me think about where the tangent circle is. The three semicircles bulge outward from the triangle. The region "inside" all three semicircular arcs... 

Actually, I think the answer might be that t = s/2, making t - s/2 = 0. Let me check.

There's a known result: For a triangle with semicircles on its sides (drawn externally), the circle tangent to all three semicircles has radius equal to s/2 (half the semiperimeter). This would make t - s/2 = 0.

Let me verify this. If t = s/2 = 10.5, let me check if there's a circle of radius 10.5 tangent to all three semicircles.

The center of such a circle would be at distance t + R_i from each midpoint (if externally tangent), or at distance |t - R_i| (if internally tangent).

With t = 10.5:
- Distance to M_a = 10.5 + 6.5 = 17, or |10.5 - 6.5| = 4
- Distance to M_b = 10.5 + 7 = 17.5, or |10.5 - 7| = 3.5
- Distance to M_c = 10.5 + 7.5 = 18, or |10.5 - 7.5| = 3

Hmm, let me think about which case. The inradius r = 4. The distances from the incenter to the midpoints of the sides...

Incenter I: weighted average by side lengths.
I = (a·A + b·B + c·C) / (a+b+c) where a is opposite A, etc.

Wait, incenter = (a·A + b·B + c·C)/(a+b+c) where a = BC, b = CA, c = AB.

I = (13·A + 14·B + 15·C) / 42

A = (99/13, 168/13), B = (0,0), C = (13, 0)

I_x = (13·(99/13) + 14·0 + 15·13) / 42 = (99 + 0 + 195) / 42 = 294/42 = 7
I_y = (13·(168/13) + 0 + 0) / 42 = 168/42 = 4

So incenter I = (7, 4). Makes sense, r = 4.

Distance from I to M_a = (13/2, 0): sqrt((7 - 6.5)² + 16) = sqrt(0.25 + 16) = sqrt(16.25) = sqrt(65)/2 ≈ 4.03

That's not 4. So the incenter is not the center of the tangent circle with internal tangency.

Let me reconsider. Maybe the tangent circle is externally tangent to all three semicircles, and its center is somewhere specific.

Actually, let me reconsider the problem. Maybe I should think about it as follows: the three semicircles drawn outside create a region, and there's a circle inscribed in the curvilinear triangle formed by the three arcs.

Let me think about Descartes' circle theorem or a direct approach.

Actually, let me reconsider. The problem says "a circle with radius t is tangent to all three semicircles." The semicircles are drawn outside the triangle. 

Let me think about the geometry more carefully. The three semicircular arcs, drawn outside, form a curvilinear triangle (like a rounded triangle pointing outward). A circle tangent to all three arcs from the outside (i.e., in the central region near the triangle) would be tangent to each arc.

But wait - the arcs are on the outside of the triangle. The central region (where the triangle is) is on the opposite side of each arc from where the arc bulges. So a circle in the triangle region would be tangent to the "back" of each semicircle... but the semicircle arc is only on one side.

Hmm, let me reconsider. The semicircle on BC with diameter BC, drawn outside the triangle (below BC). The arc goes from B to C below BC. A circle in the upper half (where the triangle is) can't be tangent to this arc unless it crosses BC.

So maybe the tangent circle is below BC, in the region of the semicircle. But then it needs to be tangent to all three semicircles which are on different sides.

Actually, I think the key insight is: the three semicircles, drawn externally, create three "lune" shapes. The circle tangent to all three is in the region that's inside all three semicircular disks but outside the triangle. Wait, no - the semicircles are on different sides.

Let me reconsider. Maybe the tangent circle is tangent to the semicircles from outside (externally tangent), meaning it doesn't overlap with any semicircle disk. The center would be at distance t + R_i from each midpoint.

Let me try to find such a point. We need a point P = (x, y) such that:
|P - M_a| = t + 13/2
|P - M_b| = t + 7
|P - M_c| = t + 15/2

This is the problem of finding a circle externally tangent to three circles (the full circles, not just semicircles). The solution is the outer Soddy circle or one of the Apollonius circles.

Actually, for three circles with radii R_a = 13/2, R_b = 7, R_c = 15/2, and centers at the midpoints of the sides, a circle externally tangent to all three...

Let me use the formula. If a circle of radius t is externally tangent to three circles of radii R_1, R_2, R_3 with centers at distances d_ij apart, we can use the system of equations.

Actually, let me think about this differently. There's a beautiful result here.

The midpoints of the sides of a triangle form the medial triangle. The sides of the medial triangle are a/2, b/2, c/2. The circumradius of the medial triangle is R/2 where R is the circumradius of the original triangle.

For the 13-14-15 triangle: R = abc/(4·Area) = 13·14·15/(4·84) = 2730/336 = 65/8.

The medial triangle has circumradius R/2 = 65/16.

Now, the three circles centered at the midpoints with radii a/2, b/2, c/2. A circle externally tangent to all three has radius t where:

The distance from the tangent circle's center to M_a is t + a/2, etc.

This is equivalent to finding a circle tangent to three circles. By the Soddy/Descartes approach or direct computation.

Let me try a different approach. Consider inverting or using the formula for the inscribed circle of the "arbelos-like" figure.

Actually, let me just try to compute directly. Let me use the Apollonius problem.

We have three circles:
- C_a: center (13/2, 0), radius 13/2
- C_b: center (134/13, 84/13), radius 7
- C_c: center (99/26, 84/13), radius 15/2

We want a circle externally tangent to all three, with center (x, y) and radius t.

(x - 13/2)² + y² = (t + 13/2)²
(x - 134/13)² + (y - 84/13)² = (t + 7)²
(x - 99/26)² + (y - 84/13)² = (t + 15/2)²

Let me expand the first equation:
x² - 13x + 169/4 + y² = t² + 13t + 169/4
x² + y² - 13x = t² + 13t

Second equation:
x² - 2·(134/13)x + (134/13)² + y² - 2·(84/13)y + (84/13)² = t² + 14t + 49
x² + y² - (268/13)x - (168/13)y + (134² + 84²)/169 = t² + 14t + 49

134² = 17956, 84² = 7056, sum = 25012. 25012/169 = 25012/169. Let me compute: 169 × 148 = 25012. Yes! So 25012/169 = 148.

So: x² + y² - (268/13)x - (168/13)y + 148 = t² + 14t + 49
x² + y² - (268/13)x - (168/13)y + 99 = t² + 14t

Third equation:
x² - 2·(99/26)x + (99/26)² + y² - (168/13)y + (84/13)² = t² + 15t + 225/4

(99/26)² = 9801/676. (84/13)² = 7056/169 = 28224/676.
Sum = (9801 + 28224)/676 = 38025/676. 

38025/676: 676 × 56 = 37856, 38025 - 37856 = 169, so 56 + 169/676 = 56 + 1/4 = 225/4. 

So: x² + y² - (99/13)x - (168/13)y + 225/4 = t² + 15t + 225/4
x² + y² - (99/13)x - (168/13)y = t² + 15t

Now from equation 1: x² + y² = t² + 13t + 13x

Substitute into equation 2:
t² + 13t + 13x - (268/13)x - (168/13)y + 99 = t² + 14t
13x - (268/13)x - (168/13)y + 99 = 14t - 13t
(169/13 - 268/13)x - (168/13)y + 99 = t
(-99/13)x - (168/13)y + 99 = t
t = 99 - (99/13)x - (168/13)y
t = 99 - (99x + 168y)/13

Substitute x² + y² = t² + 13t + 13x into equation 3:
t² + 13t + 13x - (99/13)x - (168/13)y = t² + 15t
13x - (99/13)x - (168/13)y = 15t - 13t
(169/13 - 99/13)x - (168/13)y = 2t
(70/13)x - (168/13)y = 2t
t = (70x - 168y)/(26) = (35x - 84y)/13

So we have two expressions for t:
t = 99 - (99x + 168y)/13 ... (I)
t = (35x - 84y)/13 ... (II)

Setting equal:
99 - (99x + 168y)/13 = (35x - 84y)/13
99·13 - 99x - 168y = 35x - 84y
1287 - 99x - 168y = 35x - 84y
1287 = 134x + 84y
134x + 84y = 1287

Divide by 2: 67x + 42y = 1287/2

Hmm, let me keep it as 134x + 84y = 1287.

From (II): t = (35x - 84y)/13

From 134x + 84y = 1287, we get 84y = 1287 - 134x, so y = (1287 - 134x)/84.

t = (35x - (1287 - 134x))/13 = (35x - 1287 + 134x)/13 = (169x - 1287)/13 = 13x - 99

So t = 13x - 99, which means x = (t + 99)/13.

And from 134x + 84y = 1287:
134·(t+99)/13 + 84y = 1287
(134/13)(t + 99) + 84y = 1287

134/13 = 134/13. 134 = 13·10 + 4, so 134/13 is not integer. Let me keep it.

84y = 1287 - (134/13)(t + 99) = 1287 - (134t + 134·99)/13 = (1287·13 - 134t - 13266)/13 = (16731 - 134t - 13266)/13 = (3465 - 134t)/13

y = (3465 - 134t)/(13·84) = (3465 - 134t)/1092

Now substitute into equation 1: x² + y² = t² + 13t + 13x

x = (t + 99)/13, so 13x = t + 99.

x² + y² = t² + 13t + t + 99 = t² + 14t + 99

x² = (t + 99)²/169

y² = (3465 - 134t)²/1092² = (3465 - 134t)²/1192464

Note 1092 = 84·13. 1092² = 1192464. And 169 = 13². 

Let me write everything over a common denominator. 1192464 = 84² · 169 = 7056 · 169. So 1192464/169 = 7056.

x² + y² = (t+99)²/169 + (3465-134t)²/1192464
= [7056(t+99)² + (3465-134t)²] / 1192464

And t² + 14t + 99 = [1192464(t² + 14t + 99)] / 1192464

So:
7056(t+99)² + (3465-134t)² = 1192464(t² + 14t + 99)

Let me expand. Let u = t for simplicity.

7056(u + 99)² = 7056(u² + 198u + 9801) = 7056u² + 1397088u + 69157056

(3465 - 134u)² = 134²u² - 2·3465·134u + 3465² = 17956u² - 928620u + 12006225

Sum = (7056 + 17956)u² + (1397088 - 928620)u + (69157056 + 12006225)
= 25012u² + 468468u + 81163281

RHS: 1192464(u² + 14u + 99) = 1192464u² + 16694496u + 118053936

So:
25012u² + 468468u + 81163281 = 1192464u² + 16694496u + 118053936

0 = (1192464 - 25012)u² + (16694496 - 468468)u + (118053936 - 81163281)
0 = 1167452u² + 16226028u + 36890655

Let me simplify. Divide by common factor. 

1167452, 16226028, 36890655.

Let me check GCD. 1167452 = 4·291863. 16226028 = 4·4056507. 36890655 = ? 36890655/3 = 12296885. 12296885/5 = 2459377. So 36890655 = 15·2459377. 

Is 291863 divisible by 3? 2+9+1+8+6+3 = 29, no. So GCD of 1167452 and 36890655... 1167452 = 2²·291863. 36890655 = 3·5·2459377. 291863 and 2459377 - let me check if 2459377/291863 ≈ 8.43, not integer. So GCD is likely 1 or small.

Let me just use the quadratic formula.

u = [-16226028 ± sqrt(16226028² - 4·1167452·36890655)] / (2·1167452)

Discriminant: 16226028² - 4·1167452·36890655

16226028² = let me compute. 16226028² = (1.6226028×10⁷)² ≈ 2.6328×10¹⁴. Let me be more precise.

Actually, this is getting very computational. Let me try a different approach.

Let me reconsider. Maybe the answer is indeed t = s/2 and I should verify it differently, or maybe there's a cleaner approach.

Actually, wait. Let me reconsider the problem. The problem asks for t - s/2. If the answer is 0, that's a clean answer. Let me check if t = 10.5 works.

If t = 10.5, then from t = 13x - 99: 10.5 = 13x - 99, so 13x = 109.5, x = 109.5/13 = 8.423...

From 134x + 84y = 1287: 134(109.5/13) + 84y = 1287. 134·109.5/13 = 14673/13 = 1128.69... 1287 - 1128.69 = 158.31, y = 158.31/84 = 1.885...

Let me check equation 1: x² + y² = t² + 13t + 13x
x² + y² = (109.5/13)² + (158.31/84)² 

This is getting messy. Let me try a cleaner approach.

Actually, let me reconsider whether the tangency is external or internal. Maybe the circle is internally tangent to the semicircles (i.e., the tangent circle is inside the semicircular disks). But the semicircles are on different sides of the triangle, so a single circle can't be inside all three half-disks simultaneously (they don't overlap).

Wait, actually the three semicircles drawn outside the triangle - do their half-disks overlap? The half-disk on BC (below BC), the half-disk on CA (on the side opposite B), the half-disk on AB (on the side opposite C). These three half-disks might overlap in some region, or they might not.

Actually, for an acute triangle, the three external semicircles' half-disks don't overlap with each other (they're on different sides). For the 13-14-15 triangle, let me check if it's acute. The largest side is 15. 15² = 225, 13² + 14² = 169 + 196 = 365 > 225. So the triangle is acute.

For an acute triangle, the external semicircles don't overlap. So the tangent circle must be externally tangent to all three (not inside any of them).

OK so let me continue with the computation. Let me try to be more careful.

Actually, let me try a completely different approach. Let me use the concept of the "inner Soddy circle" of three mutually tangent circles, but our three circles (the full circles on the sides as diameters) are not mutually tangent.

The three circles have centers at the midpoints of the sides and radii a/2, b/2, c/2. The distance between midpoints of sides:
- M_a and M_b: midpoint of BC and midpoint of CA. This distance = c/2 (half of AB, since the segment connecting midpoints of two sides equals half the third side).
- M_b and M_c: distance = a/2
- M_c and M_a: distance = b/2

So the three circles have:
- Radii: a/2, b/2, c/2
- Distances between centers: c/2, a/2, b/2

Check: Circle at M_a (radius a/2) and circle at M_b (radius b/2), distance between them = c/2.
For external tangency: a/2 + b/2 = c/2, i.e., a + b = c. Not generally true.
For the circles to be tangent: |a/2 - b/2| = c/2 or a/2 + b/2 = c/2. Neither holds in general.

So the three circles are not mutually tangent. The distance between M_a and M_b is c/2, and the radii are a/2 and b/2. Since a + b > c (triangle inequality), a/2 + b/2 > c/2, so the circles overlap! The two circles at M_a and M_b overlap.

Wait, that means the full circles overlap. But we're only considering semicircles (half-disks) drawn outside the triangle. The half-disks might not overlap even though the full circles do.

OK, this is getting complicated. Let me just solve the quadratic.

0 = 1167452u² + 16226028u + 36890655

Let me try to factor out common factors more carefully.

1167452 = 4 × 291863
16226028 = 4 × 4056507
36890655: is this divisible by 4? 36890655/4 = 9222663.75, no. So GCD includes at most 1 from the factor of 4.

Let me check if 291863 is prime. 291863 / 7 = 41694.7... no. /11 = 26533, let me check: 11 × 26533 = 291863. Yes! So 291863 = 11 × 26533.

26533 / 11 = 2412.09... no. /13 = 2041, let me check: 13 × 2041 = 26533. Yes! So 26533 = 13 × 2041.

2041 / 13 = 157. 13 × 157 = 2041. Yes! So 2041 = 13 × 157.

157 is prime.

So 291863 = 11 × 13 × 13 × 157 = 11 × 169 × 157.
1167452 = 4 × 11 × 169 × 157 = 44 × 169 × 157.

4056507: /3 = 1352169. /3 = 450723. /3 = 150241. Is 150241 divisible by 11? 1-5+0-2+4-1 = -3, no. By 13? 150241/13 = 11557. 13 × 11557 = 150241. Yes! 11557/13 = 889. 13 × 889 = 11557. Yes! 889 = 7 × 127. 127 is prime.

So 4056507 = 27 × 169 × 7 × 127 = 3³ × 7 × 13² × 127.
16226028 = 4 × 3³ × 7 × 13² × 127 = 2² × 3³ × 7 × 13² × 127.

36890655: /3 = 12296885. /5 = 2459377. 2459377 / 7 = 351339.57... no. /11 = 223579.7... no. /13 = 189183.6... let me check: 13 × 189183 = 2459379, not quite. /157 = 15666.8... no. 

Hmm, let me try differently. 2459377 / 127 = 19365.17... no. 

Let me try: 2459377 / 169 = 14558.7... no.

This is getting really messy. Let me just compute numerically.

u = [-16226028 ± sqrt(16226028² - 4 × 1167452 × 36890655)] / (2 × 1167452)

16226028² = 263,284,005,847,984 (approximately). Let me compute more carefully.

Actually, let me just compute the discriminant numerically.

16226028² ≈ 2.6328 × 10^14
4 × 1167452 × 36890655 ≈ 4 × 1.167452 × 10^6 × 3.6890655 × 10^7 ≈ 4 × 4.307 × 10^13 ≈ 1.723 × 10^14

Discriminant ≈ 2.6328 × 10^14 - 1.723 × 10^14 ≈ 0.91 × 10^14

sqrt ≈ 9.54 × 10^6

u = (-16226028 + 9540000) / 2334904 ≈ -6686028 / 2334904 ≈ -2.86 (negative, not valid)
or u = (-16226028 - 9540000) / 2334904 ≈ -25766028 / 2334904 ≈ -11.04 (negative, not valid)

Both roots are negative! That means there's no circle externally tangent to all three with positive radius. That makes sense because the three full circles overlap - you can't have a circle externally tangent to all three from outside.

So the tangency must be internal for some of the semicircles. Let me reconsider.

Since the semicircles are half-disks (not full circles), and they're drawn outside the triangle, the tangent circle is in the region of the triangle (or near it), tangent to the arcs.

Wait, I think I need to reconsider the geometry. The semicircle on BC drawn outside the triangle: the arc is below BC. A circle above BC (in the triangle) can be tangent to this arc only if it's tangent at a point on BC (the diameter), but the arc doesn't include the diameter as part of the arc (the arc is the curved part). 

Hmm, actually, maybe the problem means the semicircles include the diameter as part of the boundary, and the tangent circle is tangent to the straight part (the diameter) of each semicircle? No, that would just be the incircle.

Let me reconsider. Maybe the tangent circle is tangent to the curved arcs, and it's located in the region outside the triangle but "between" the three arcs. 

Actually, I think I've been overcomplicating this. Let me reconsider the setup.

The three semicircles are drawn outside the triangle. They bulge outward. The region "inside" all three arcs (i.e., the region that is inside all three half-disks) would be... the half-disk on BC is below BC, the half-disk on CA is on the far side from B, the half-disk on AB is on the far side from C. For an acute triangle, these three half-disks don't have a common intersection.

But the arcs themselves form a curvilinear boundary. The circle tangent to all three arcs from the "inside" (the triangle side) would be a circle that touches each arc from the triangle's side.

For the semicircle on BC (arc below BC), a circle above BC tangent to this arc: the tangency point would be on BC itself (the midpoint of the arc is directly below the midpoint of BC). Actually, the closest point of the arc to a point above BC is on the diameter BC. But the arc is the curved part, which is below BC.

I think I'm confusing myself. Let me reconsider: maybe the tangent circle is below all the arcs, in the exterior region, and it's internally tangent to each semicircle (i.e., the tangent circle is inside each half-disk).

But for an acute triangle, the three half-disks don't share a common region, so a circle can't be inside all three.

Let me try yet another interpretation: the tangent circle is externally tangent to the semicircular arcs, meaning it touches each arc from outside the half-disk. The center is at distance t + R_i from each midpoint (external tangency to the full circle), but we also need the tangency point to be on the arc (the correct half).

But we showed that external tangency to all three full circles gives negative t. So that doesn't work.

What if the tangent circle is internally tangent to some and externally tangent to others?

Let me think about this more carefully with the geometry. 

Actually, I wonder if the problem is about the circle inscribed in the curvilinear triangle formed by the three semicircular arcs. This is a well-known configuration.

Let me reconsider. The three semicircles on the sides of a triangle, drawn externally, form a shape. The "arbelos" of Archimedes is the case of three semicircles on a line. For a triangle, the three external semicircles create a figure, and there's a circle inscribed in the curvilinear triangle formed by the three arcs.

The curvilinear triangle is the region bounded by the three arcs. This region is the original triangle plus three "lune" regions... no.

Actually, the three arcs, drawn externally, bound a region that contains the triangle. The region inside all three arcs (on the triangle side of each arc) is the triangle itself plus the regions between the triangle sides and the arcs. Wait, no - the arcs are on the outside of the triangle, so the region on the triangle side of each arc includes the triangle and more.

Hmm, let me think about it differently. Each semicircular arc divides the plane into two regions: the half-disk (inside the semicircle) and the rest (outside). The three arcs, drawn externally, create a region that is the intersection of the three "outside" regions (outside all three half-disks). This region contains the triangle and extends to infinity. A circle tangent to all three arcs from outside would be in this region.

Alternatively, the region inside all three half-disks (intersection of the three half-disks) - for an acute triangle, this is empty (as I noted).

So the tangent circle is in the region outside all three half-disks, and it's externally tangent to each. But we showed that gives negative t for the full circles. 

Wait, but the semicircles are half-circles, not full circles. The external tangency to the full circle might not apply because the tangency point needs to be on the arc (the correct half).

Hmm, but if the tangent circle is outside all three half-disks and tangent to the arcs, the tangency point is on the arc, and the distance from the center to the midpoint is t + R_i (external tangency). The constraint that the tangency point is on the correct half is automatically satisfied if the center is on the correct side.

But we showed no positive t exists for external tangency to all three full circles. So maybe the tangent circle is on the same side as some arcs and the opposite side of others.

Let me reconsider the problem from scratch. Maybe I should consider that the tangent circle could be internally tangent to the semicircles (inside the half-disk) for some and externally tangent for others.

Actually, you know what, let me reconsider. Maybe the problem is simpler than I think. Let me re-read it.

"Semicircles with diameters BC, CA, AB are drawn outside of the triangle. A circle with radius t is tangent to all three semicircles."

I think the standard interpretation is: the three semicircles form a figure (like a rounded triangle), and there's a circle inscribed in the curvilinear triangular gap in the middle. But the "middle" is where the triangle is.

Actually, I think the correct interpretation is: the circle is tangent to all three semicircular arcs, and it's located in the region of the triangle. The circle is internally tangent to each semicircle (i.e., the tangent circle is on the opposite side of the diameter from the arc, so the distance from the center to the midpoint is |t - R_i|, and specifically t - R_i if t > R_i or R_i - t if R_i > t).

Wait, no. If the tangent circle is on the opposite side of the diameter from the arc, it's not inside the half-disk. The tangency would be with the full circle, on the opposite side from the arc. But the arc is only on one side, so the tangency point wouldn't be on the arc.

I think I need to reconsider. Let me think about what "tangent to a semicircle" means. A semicircle is a half-disk, which is a region bounded by a diameter and a semicircular arc. A circle tangent to a semicircle could be tangent to the arc (the curved part) or to the diameter (the straight part).

If tangent to the arc: the tangent circle touches the curved boundary. The center of the tangent circle is at distance t + R (external) or |t - R| (internal) from the midpoint of the diameter, and the tangency point is on the arc (the correct half of the full circle).

If the tangent circle is in the triangle region (opposite side from the arc), then for it to be tangent to the arc, it would need to reach across the diameter. The tangency point on the full circle would be on the opposite half from the arc. So it's tangent to the full circle but not to the arc. This doesn't work.

Unless... the tangent circle is large enough to encompass the semicircle. If t > R and the tangent circle contains the semicircle, then the tangency is internal, and the tangency point could be on the arc side.

Hmm, this is getting complicated. Let me try a different approach entirely.

Let me consider the possibility that the circle is tangent to the semicircles from the inside, meaning the tangent circle is in the half-disk region. But for an acute triangle, the three half-disks don't overlap, so this is impossible.

Wait, maybe I should check: do the three external semicircles of the 13-14-15 triangle overlap?

The half-disk on BC is below BC. The half-disk on CA is on the side of CA opposite to B. The half-disk on AB is on the side of AB opposite to C.

For the half-disk on BC (below BC) and the half-disk on AB (opposite side from C): 

The side AB goes from A(99/13, 168/13) to B(0,0). The side opposite from C(13,0). C is to the right. The half-disk on AB is to the left of AB (away from C).

The half-disk on BC is below BC (y < 0). The half-disk on AB is to the left of line AB. Do these overlap? Near vertex B, the half-disk on BC extends below B, and the half-disk on AB extends to the left of B. They might overlap near B.

Actually, at vertex B, both semicircles pass through B (since B is an endpoint of both diameters BC and AB). The half-disk on BC near B goes below BC, and the half-disk on AB near B goes to the left of AB. The angle at B: 

cos B = (a² + c² - b²)/(2ac) = (169 + 225 - 196)/(2·13·15) = 198/390 = 33/65.

The angle B is acute. The two half-disks near B are on the exterior sides, so they're on opposite sides of the angle at B. They don't overlap near B (they're separated by the exterior angle).

Actually, the half-disk on BC is on the side of BC opposite to A, and the half-disk on AB is on the side of AB opposite to C. At vertex B, the exterior region (outside the triangle) is divided by the extension of the sides. The two half-disks are in different parts of the exterior, so they don't overlap.

OK so for an acute triangle, the three external half-disks don't overlap. So the tangent circle can't be inside all three.

Let me reconsider the problem. Maybe the tangent circle is tangent to the semicircles from the outside (externally tangent to the full circles), and the issue is that I need to also consider the constraint that the tangency points are on the arcs.

But we showed that external tangency to all three full circles gives negative t. So maybe the configuration is different.

Wait, let me re-examine my computation. I assumed the tangent circle is externally tangent to all three (distance = t + R_i). Let me re-examine.

Actually, I realize I might have made an error. Let me reconsider: maybe the tangent circle is internally tangent to the semicircles, meaning the tangent circle contains each semicircle (t > R_i) or is contained in each (t < R_i). 

If the tangent circle contains each semicircle (t > R_i for all), then distance from center to midpoint = t - R_i. This would mean the tangent circle is large and encompasses all three semicircles.

Let me try this case:
(x - 13/2)² + y² = (t - 13/2)²
(x - 134/13)² + (y - 84/13)² = (t - 7)²
(x - 99/26)² + (y - 84/13)² = (t - 15/2)²

Expanding equation 1:
x² - 13x + 169/4 + y² = t² - 13t + 169/4
x² + y² - 13x = t² - 13t

Equation 2:
x² + y² - (268/13)x - (168/13)y + 148 = t² - 14t + 49
x² + y² - (268/13)x - (168/13)y + 99 = t² - 14t

Equation 3:
x² + y² - (99/13)x - (168/13)y = t² - 15t

From eq 1: x² + y² = t² - 13t + 13x

Sub into eq 2:
t² - 13t + 13x - (268/13)x - (168/13)y + 99 = t² - 14t
-13t + 13x - (268/13)x - (168/13)y + 99 = -14t
t + (169/13 - 268/13)x - (168/13)y + 99 = 0
t - (99/13)x - (168/13)y + 99 = 0
t = (99/13)x + (168/13)y - 99

Sub into eq 3:
t² - 13t + 13x - (99/13)x - (168/13)y = t² - 15t
-13t + (169/13 - 99/13)x - (168/13)y = -15t
2t + (70/13)x - (168/13)y = 0
t = -(70/13)x + (168/13)y = (168y - 70x)/13 = (84y - 35x)/13·... wait

t = (168y - 70x)/13

Wait, let me redo: 2t + (70/13)x - (168/13)y = 0
2t = (168/13)y - (70/13)x = (168y - 70x)/13
t = (168y - 70x)/26 = (84y - 35x)/13

Setting the two expressions for t equal:
(99x + 168y)/13 - 99 = (84y - 35x)/13
99x + 168y - 1287 = 84y - 35x
134x + 84y = 1287

Same equation as before! 134x + 84y = 1287.

And t = (84y - 35x)/13. From 134x + 84y = 1287: 84y = 1287 - 134x.
t = (1287 - 134x - 35x)/13 = (1287 - 169x)/13 = 99 - 13x

So t = 99 - 13x, x = (99 - t)/13.

From 134x + 84y = 1287:
134(99-t)/13 + 84y = 1287
(134·99 - 134t)/13 + 84y = 1287
(13266 - 134t)/13 + 84y = 1287
84y = 1287 - (13266 - 134t)/13 = (16731 - 13266 + 134t)/13 = (3465 + 134t)/13
y = (3465 + 134t)/(13·84) = (3465 + 134t)/1092

Now substitute into equation 1: x² + y² = t² - 13t + 13x

13x = 99 - t, so:
x² + y² = t² - 13t + 99 - t = t² - 14t + 99

x = (99-t)/13, x² = (99-t)²/169
y = (3465 + 134t)/1092, y² = (3465 + 134t)²/1192464

[(99-t)²·7056 + (3465+134t)²] / 1192464 = t² - 14t + 99

7056(99-t)² + (3465+134t)² = 1192464(t² - 14t + 99)

7056(99-t)² = 7056(t² - 198t + 9801) = 7056t² - 1397088t + 69157056

(3465+134t)² = 17956t² + 928620t + 12006225

Sum = 25012t² - 468468t + 81163281

RHS = 1192464t² - 16694496t + 118053936

0 = (1192464 - 25012)t² + (-16694496 + 468468)t + (118053936 - 81163281)
0 = 1167452t² - 16226028t + 36890655

Now the discriminant is the same: 16226028² - 4·1167452·36890655 (same as before since signs work out).

u = [16226028 ± sqrt(discriminant)] / (2·1167452)

The discriminant is the same as before. Let me compute it.

D = 16226028² - 4 × 1167452 × 36890655

Let me compute 16226028²:
16226028 = 16226028
16226028² = (16226000 + 28)² = 16226000² + 2·16226000·28 + 28²
= 263283076000000 + 908656000 + 784
= 263283984656784

Now 4 × 1167452 × 36890655:
1167452 × 36890655:
Let me compute step by step.
1167452 × 36890655

= 1167452 × (36000000 + 890655)
= 1167452 × 36000000 + 1167452 × 890655

1167452 × 36000000 = 1167452 × 36 × 10^6 = 42028272 × 10^6 = 42028272000000

1167452 × 890655:
= 1167452 × (900000 - 9345)
= 1167452 × 900000 - 1167452 × 9345

1167452 × 900000 = 1050706800000

1167452 × 9345:
= 1167452 × (9000 + 345)
= 1167452 × 9000 + 1167452 × 345

1167452 × 9000 = 10507068000

1167452 × 345:
= 1167452 × (300 + 45)
= 1167452 × 300 + 1167452 × 45

1167452 × 300 = 350235600
1167452 × 45 = 1167452 × (50 - 5) = 58372600 - 5837260 = 52535340

1167452 × 345 = 350235600 + 52535340 = 402770940

1167452 × 9345 = 10507068000 + 402770940 = 10909838940

1167452 × 890655 = 1050706800000 - 10909838940 = 1039796961060

1167452 × 36890655 = 42028272000000 + 1039796961060 = 43068068961060

4 × 43068068961060 = 172272275844240

D = 263283984656784 - 172272275844240 = 91011708812544

sqrt(D) = sqrt(91011708812544)

Let me compute: 9540000² = 91011600000000. Close!
9540000² = 91011600000000
D - 91011600000000 = 91011708812544 - 91011600000000 = 108812544

9540000² + 108812544. Let me try 9540057:
9540057² = 9540000² + 2·9540000·57 + 57² = 91011600000000 + 1087560000 + 3249 = 9101267563249. Too big.

Hmm, let me try 9540005:
9540005² = 9540000² + 2·9540000·5 + 25 = 91011600000000 + 95400000 + 25 = 91011695400025. 

D = 91011708812544. 91011708812544 - 91011695400025 = 13412519. 

9540005² + 13412519. Next: 9540005 + d, (9540005+d)² ≈ 9540005² + 2·9540005·d. 
2·9540005·d = 13412519, d ≈ 13412519/19080010 ≈ 0.703. Not integer.

So sqrt(D) is not an integer. Let me check if D is a perfect square.

D = 91011708812544

Let me factor: 91011708812544 = 16 × 5688231800784 (dividing by 16)
5688231800784 = 16 × 355514487549 (not integer, since 5688231800784/16 = 355514487549)

Actually 5688231800784 / 4 = 1422057950196
1422057950196 / 4 = 355514487549

So D = 64 × 355514487549? Let me check: 64 × 355514487549 = 22752927203136. No, that's not right.

Let me redo. D = 91011708812544.
D / 4 = 22752927203136
D / 16 = 5688231800784
D / 64 = 1422057950196
D / 256 = 355514487549

355514487549: is this divisible by small primes? 
Sum of digits: 3+5+5+5+1+4+4+8+7+5+4+9 = 60, divisible by 3. 355514487549 / 3 = 118504829183.

118504829183: sum = 1+1+8+5+0+4+8+2+9+1+8+3 = 50, not divisible by 3.
/7: 118504829183/7 = 16929261311.86... let me check: 7 × 16929261312 = 118504829184. Close but not exact.
/11: alternating sum: 3-8+1-9+2-8+4-0+5-8+1-1 = -18, not divisible by 11.
/13: 118504829183/13 = 9115756091.0. 13 × 9115756091 = 118504829183. Yes!

9115756091 / 13 = 701212006.23... no.
/7: 9115756091/7 = 1302250870.14... no.
/157: 9115756091/157 = 58049402.49... no.

This is getting very messy. Let me try a completely different approach to the problem.

Let me reconsider. Maybe I should think about this problem using inversion or some known formula.

Actually, let me reconsider the problem setup. Maybe the tangent circle is not tangent to the full circles but specifically to the semicircular arcs, and the tangency is such that the tangent circle is on the same side as the arc (i.e., in the half-disk region) for some and on the opposite side for others.

Actually, let me reconsider the problem. Perhaps the three semicircles, drawn outside, create a region that looks like a "curvilinear triangle" and the inscribed circle of this curvilinear triangle is what we seek.

The curvilinear triangle is the region bounded by the three arcs. This region is the original triangle plus the three "lune" regions between each side and its arc. Wait, no. The arcs are outside the triangle, so the region bounded by the three arcs includes the triangle and the lune regions.

Actually, the three arcs connect at the vertices of the triangle (since each semicircle has its diameter as a side of the triangle, and the arc goes from one vertex to another). So the three arcs form a closed curve: arc from B to C (below BC), arc from C to A (outside CA), arc from A to B (outside AB). This closed curve encloses a region that contains the triangle.

The circle inscribed in this curvilinear triangle (tangent to all three arcs from inside) would be in this enclosed region. The center would be somewhere near the triangle, and the tangency to each arc would be from the "inside" of the curvilinear triangle.

For the arc on BC (below BC), the inside of the curvilinear triangle is above the arc (toward the triangle). So the tangent circle is above the arc, meaning it's on the opposite side of the arc from the half-disk center. The distance from the tangent circle's center to M_a is t + R_a (external tangency to the full circle), and the tangency point is on the arc (below BC), which is the correct half.

Wait, but external tangency to the full circle means the tangent circle is outside the full circle. If the tangent circle is above BC and the arc is below BC, the tangent circle is outside the full circle (since the full circle extends both above and below BC, and the tangent circle is above BC but outside the circle). The tangency point would be on the upper half of the full circle (above BC), not on the arc (which is below BC). So this doesn't work.

Hmm. Let me think again.

If the tangent circle is inside the curvilinear triangle (which contains the original triangle), and it's tangent to the arc below BC, then the tangent circle must reach below BC to touch the arc. The tangent circle's center could be above BC, and the circle extends below BC to touch the arc.

In this case, the tangent circle overlaps with the full circle on BC. The tangency is internal: the tangent circle is internally tangent to the full circle (the tangent circle contains the full circle, or vice versa).

If the tangent circle contains the full circle on BC: distance from center to M_a = t - R_a (with t > R_a). The tangency point is on the arc side (below BC) if the center is above BC. This could work!

So the tangent circle is a large circle that contains all three full circles, and is internally tangent to each. The distance from its center to each midpoint is t - R_i.

This is the case I already computed! Let me continue with that.

0 = 1167452t² - 16226028t + 36890655

t = [16226028 ± sqrt(91011708812544)] / (2 × 1167452)

Let me compute sqrt(91011708812544) more carefully.

91011708812544. Let me try to see if this is a perfect square.

sqrt(91011708812544) ≈ 9540057.something

Let me try 9540057:
9540057² = ?
9540057 = 9540000 + 57
9540057² = 9540000² + 2×9540000×57 + 57²
= 91011600000000 + 1087560000 + 3249
= 9101267563249

That's way less than 91011708812544. Wait, I think I miscounted digits.

91011708812544 has 14 digits. 9540057² should have about 14 digits.
9540057² = 9101267563249 which has 13 digits. That's wrong.

Let me recompute. 9540057 ≈ 9.54 × 10^6. (9.54 × 10^6)² = 91.0 × 10^12 = 9.1 × 10^13. That's 14 digits. 

9540057² = 9540057 × 9540057.

Let me be more careful:
9540000² = 91011600000000 (this is 9.10016 × 10^13, 14 digits) ✓

2 × 9540000 × 57 = 1087560000

57² = 3249

9540057² = 91011600000000 + 1087560000 + 3249 = 91012687563249

Hmm wait: 91011600000000 + 1087560000 = 91012687560000, + 3249 = 91012687563249.

D = 91011708812544

91012687563249 - 91011708812544 = 978750705. So 9540057² is about 978750705 more than D.

So sqrt(D) ≈ 9540057 - 978750705/(2×9540057) ≈ 9540057 - 978750705/19080114 ≈ 9540057 - 51.3 ≈ 9540005.7

Let me try 9540005:
9540005² = 9540000² + 2×9540000×5 + 25 = 91011600000000 + 95400000 + 25 = 91011695400025

D - 91011695400025 = 91011708812544 - 91011695400025 = 13412519

9540006² = 9540005² + 2×9540005 + 1 = 91011695400025 + 19080011 = 91011714480036

91011714480036 > 91011708812544. So sqrt(D) is between 9540005 and 9540006.

So D is not a perfect square, and t is not a "nice" number. This suggests I might have the wrong tangency model.

Let me reconsider. Maybe the tangency is mixed: the tangent circle is externally tangent to some semicircles and internally tangent to others.

Actually, wait. Let me reconsider the geometry. The curvilinear triangle formed by the three arcs contains the original triangle. The inscribed circle of this curvilinear triangle is tangent to each arc from inside. 

For the arc on BC (below BC): the tangent circle is above the arc (inside the curvilinear triangle). The tangent circle and the full circle on BC: the tangent circle is outside the full circle (above BC, the full circle extends from -R_a to +R_a vertically, and the tangent circle is above). Actually, the full circle on BC has center at (13/2, 0) and radius 13/2, so it extends from y = -13/2 to y = 13/2. The tangent circle, if its center is above the triangle, might be outside this full circle.

If the tangent circle is externally tangent to the full circle on BC: distance = t + 13/2, and the tangency point is on the lower half of the full circle (the arc below BC). This works if the tangent circle's center is above the full circle.

But we showed that external tangency to all three gives negative t. So maybe it's external for some and internal for others.

Hmm, let me think about this differently. Let me consider the specific geometry.

The tangent circle is inside the curvilinear triangle. The curvilinear triangle is "fatter" than the original triangle (the arcs bulge outward). So the inscribed circle of the curvilinear triangle is larger than the incircle of the triangle.

For the arc on BC (below BC), the tangent circle (above BC, inside the curvilinear triangle) touches the arc from above. The tangent circle is outside the full circle on BC (since the full circle on BC is centered at (13/2, 0) with radius 13/2, and the tangent circle is above this). The tangency is external: distance = t + 13/2.

For the arc on CA (outside CA, away from B), the tangent circle (on the B side of CA, inside the curvilinear triangle) touches the arc from the B side. The tangent circle is outside the full circle on CA. External tangency: distance = t + 7.

Similarly for AB: external tangency, distance = t + 15/2.

So it should be external tangency to all three. But we showed that gives negative t. 

Wait, maybe I made a computational error. Let me recheck.

Actually, let me reconsider. The full circle on BC has center (13/2, 0) and radius 13/2. It extends from x = 0 to x = 13 and y = -13/2 to y = 13/2. The tangent circle, if centered above the triangle (say at (7, y) with y > 0), might be inside this full circle if y < 13/2 and the distance from (7, y) to (13/2, 0) is less than 13/2.

Distance from (7, 4) [incenter] to (13/2, 0) = sqrt(0.25 + 16) = sqrt(16.25) ≈ 4.03 < 6.5. So the incenter is inside the full circle on BC! 

So the tangent circle, if near the incenter, is inside the full circles. The tangency would be internal: the tangent circle is inside the full circle, and tangent to it from inside. Distance = R_i - t (if t < R_i).

But the tangent circle is tangent to the arc (lower half of the circle), not the upper half. If the tangent circle is inside the full circle and tangent to it, the tangency point is on the upper half (near the tangent circle), not on the arc (lower half). So this doesn't work either.

Unless the tangent circle is below the center of the full circle, in which case the tangency point is on the lower half (the arc). But the tangent circle is supposed to be inside the curvilinear triangle, which is above BC.

I'm going in circles (no pun intended). Let me try a completely different approach.

Let me reconsider: maybe the tangent circle is NOT inside the curvilinear triangle. Maybe it's in one of the lune regions, or maybe it's a different circle entirely.

Actually, re-reading the problem: "A circle with radius t is tangent to all three semicircles." It just says tangent to all three semicircles. It doesn't specify where. There might be multiple such circles (Apollonius problem has up to 8 solutions). The problem says "a circle," implying there's a unique one (or the relevant one).

Let me think about what circle is tangent to all three semicircles (arcs). The three arcs form a closed curve. There could be:
1. A circle inside the curvilinear triangle, tangent to all three arcs from inside.
2. Three circles, each in a lune region, tangent to two arcs and one side.
3. Other Apollonius circles.

For case 1, we need to figure out the correct tangency type.

Let me reconsider. The curvilinear triangle is the region enclosed by the three arcs. This region contains the original triangle. The "inscribed circle" of this curvilinear triangle is tangent to each arc from inside the curvilinear triangle.

For the arc on BC (below BC): inside the curvilinear triangle means above the arc. The tangent circle is above the arc. The full circle on BC has the arc as its lower half. The tangent circle, being above the arc, is on the opposite side from the half-disk. 

If the tangent circle is outside the full circle (above it), the tangency is external: distance = t + R_a, tangency point on the lower half (the arc). ✓
If the tangent circle is inside the full circle, the tangency is internal: distance = R_a - t, tangency point on the upper half (not the arc). ✗

So for the tangency point to be on the arc, the tangent circle must be outside the full circle, and the tangency is external.

But we showed external tangency to all three gives negative t. So there's no such circle?

Wait, maybe I made an error. Let me recheck the external tangency case.

External tangency: distance = t + R_i.
Equations:
(x - 13/2)² + y² = (t + 13/2)²
(x - 134/13)² + (y - 84/13)² = (t + 7)²
(x - 99/26)² + (y - 84/13)² = (t + 15/2)²

From eq 1: x² + y² - 13x = t² + 13t
From eq 2: x² + y² - (268/13)x - (168/13)y + 99 = t² + 14t
From eq 3: x² + y² - (99/13)x - (168/13)y = t² + 15t

From eq 1 and eq 2:
-13x + (268/13)x + (168/13)y - 99 = 13t - 14t = -t
(-169/13 + 268/13)x + (168/13)y - 99 = -t
(99/13)x + (168/13)y - 99 = -t
t = 99 - (99x + 168y)/13

From eq 1 and eq 3:
-13x + (99/13)x + (168/13)y = 13t - 15t = -2t
(-169/13 + 99/13)x + (168/13)y = -2t
(-70/13)x + (168/13)y = -2t
t = (70x - 168y)/26 = (35x - 84y)/13

Setting equal:
99 - (99x + 168y)/13 = (35x - 84y)/13
1287 - 99x - 168y = 35x - 84y
1287 = 134x + 84y

t = (35x - 84y)/13

From 134x + 84y = 1287: 84y = 1287 - 134x
t = (35x - 1287 + 134x)/13 = (169x - 1287)/13 = 13x - 99

So x = (t + 99)/13.

84y = 1287 - 134(t+99)/13 = (1287·13 - 134t - 134·99)/13 = (16731 - 134t - 13266)/13 = (3465 - 134t)/13
y = (3465 - 134t)/(13·84) = (3465 - 134t)/1092

Substitute into eq 1: x² + y² = t² + 13t + 13x = t² + 13t + t + 99 = t² + 14t + 99

((t+99)/13)² + ((3465-134t)/1092)² = t² + 14t + 99

(t+99)²/169 + (3465-134t)²/1192464 = t² + 14t + 99

Multiply by 1192464:
7056(t+99)² + (3465-134t)² = 1192464(t² + 14t + 99)

7056(t²+198t+9801) + (134²t² - 2·3465·134t + 3465²) = 1192464t² + 16694496t + 118053936

7056t² + 1397088t + 69157056 + 17956t² - 928620t + 12006225 = 1192464t² + 16694496t + 118053936

(7056+17956)t² + (1397088-928620)t + (69157056+12006225) = 1192464t² + 16694496t + 118053936

25012t² + 468468t + 81163281 = 1192464t² + 16694496t + 118053936

0 = 1167452t² + 16226028t + 36890655

Discriminant = 16226028² - 4·1167452·36890655 = 263283984656784 - 172272275844240 = 91011708812544

Since the coefficient of t² and the constant are both positive, and the coefficient of t is positive, both roots are negative (by Vieta's, sum of roots = -16226028/1167452 < 0, product = 36890655/1167452 > 0, so both roots negative). 

So indeed, no positive solution for external tangency to all three.

Now for internal tangency to all three (tangent circle contains all three full circles):
0 = 1167452t² - 16226028t + 36890655

t = [16226028 ± sqrt(91011708812544)] / 2334904

Both roots positive (sum = 16226028/1167452 > 0, product = 36890655/1167452 > 0).

sqrt(91011708812544) ≈ 9540005.7 (from earlier computation)

t₁ = (16226028 + 9540006) / 2334904 ≈ 25766034 / 2334904 ≈ 11.04
t₂ = (16226028 - 9540006) / 2334904 ≈ 6686022 / 2334904 ≈ 2.86

For the tangent circle to contain all three full circles, we need t > max(R_i) = 15/2 = 7.5. So t₁ ≈ 11.04 works, t₂ ≈ 2.86 doesn't.

But wait, does this configuration make geometric sense? The tangent circle contains all three full circles and is internally tangent to each. The tangency point for each would be on the far side of each full circle from the tangent circle's center. 

For the arc on BC (below BC), the tangency point needs to be on the arc (below BC). If the tangent circle's center is above BC, the tangency point with the full circle on BC is on the lower side (below BC), which is the arc. ✓

Similarly for the other arcs, if the tangent circle's center is inside the triangle, the tangency points would be on the arcs (the exterior sides). ✓

So this is the correct configuration! The tangent circle is a large circle centered inside the triangle, containing all three full circles, internally tangent to each, with tangency points on the arcs.

So t ≈ 11.04. And s/2 = 10.5. So t - s/2 ≈ 0.54. That doesn't seem like a clean answer.

Let me compute more precisely.

t = (16226028 - sqrt(91011708812544)) / 2334904 (taking the smaller root, which is the one where the tangent circle is "just barely" containing the circles, i.e., the inscribed circle of the curvilinear triangle)

Wait, actually, which root corresponds to the inscribed circle? The larger root (t₁ ≈ 11.04) would be a bigger circle, and the smaller root (t₂ ≈ 2.86) would be smaller. But t₂ < 7.5, so it can't contain the full circles. So t₁ is the answer.

Hmm, but 11.04 - 10.5 = 0.54, not a clean number. Let me check if the discriminant is actually a perfect square and I made an arithmetic error.

Let me recompute D = 16226028² - 4 × 1167452 × 36890655.

Actually, let me recheck my expansion. Let me recompute 7056 × 9801:
7056 × 9801 = 7056 × (10000 - 199) = 70560000 - 1404144 = 69155856

Wait, I had 69157056 before. Let me recheck.
7056 × 9801:
7056 × 9000 = 63504000
7056 × 800 = 5644800
7056 × 1 = 7056
Total = 63504000 + 5644800 + 7056 = 69155856

I had 69157056 before, which is wrong! Let me redo.

7056 × 9801 = 69155856. The difference is 69157056 - 69155856 = 1200.

Let me also recheck 3465²:
3465² = (3500 - 35)² = 12250000 - 245000 + 1225 = 12006225. ✓

And 2 × 3465 × 134 = 6930 × 134 = 928620. ✓

And 7056 × 198 = 7056 × 200 - 7056 × 2 = 1411200 - 14112 = 1397088. ✓

So the constant term: 69155856 + 12006225 = 81162081 (not 81163281 as I had before).

Let me redo the equation:
25012t² + 468468t + 81162081 = 1192464t² + 16694496t + 118053936

0 = 1167452t² + 16226028t + 36891855

Wait, 118053936 - 81162081 = 36891855 (not 36890655).

The difference: 36891855 - 36890655 = 1200. Same as the error in the constant term.

So the correct equation for external tangency is:
0 = 1167452t² + 16226028t + 36891855

And for internal tangency:
0 = 1167452t² - 16226028t + 36891855

Discriminant = 16226028² - 4 × 1167452 × 36891855

Let me recompute 4 × 1167452 × 36891855.

1167452 × 36891855:
= 1167452 × (36000000 + 891855)
= 1167452 × 36000000 + 1167452 × 891855

1167452 × 36000000 = 42028272000000

1167452 × 891855:
= 1167452 × (900000 - 8145)
= 1167452 × 900000 - 1167452 × 8145

1167452 × 900000 = 1050706800000

1167452 × 8145:
= 1167452 × (8000 + 145)
= 1167452 × 8000 + 1167452 × 145

1167452 × 8000 = 9339616000

1167452 × 145:
= 1167452 × (100 + 45)
= 116745200 + 52535340
= 169280540

1167452 × 8145 = 9339616000 + 169280540 = 9508896540

1167452 × 891855 = 1050706800000 - 9508896540 = 1041197903460

1167452 × 36891855 = 42028272000000 + 1041197903460 = 43069469903460

4 × 43069469903460 = 172277879613840

D = 263283984656784 - 172277879613840 = 91006105042944

Hmm, let me double-check 16226028²:
16226028² = (16226000 + 28)² = 16226000² + 2 × 16226000 × 28 + 784

16226000² = (16226)² × 10^6 = 263282276 × 10^6 = 263282276000000

Wait, 16226² = ?
16226² = (16000 + 226)² = 256000000 + 7232000 + 51076 = 263283076

So 16226000² = 263283076000000

2 × 16226000 × 28 = 909656000

16226028² = 263283076000000 + 909656000 + 784 = 263283985656784

Hmm, I had 263283984656784 before. The difference is 263283985656784 - 263283984656784 = 1000000. Let me recheck.

16226² = 16226 × 16226.
16226 × 16000 = 259616000
16226 × 226 = 16226 × 200 + 16226 × 26 = 3245200 + 421876 = 3667076
Total = 259616000 + 3667076 = 263283076. ✓

16226000² = 263283076 × 10^6 = 263283076000000. ✓

2 × 16226000 × 28 = 16226000 × 56 = 909656000. ✓

28² = 784. ✓

16226028² = 263283076000000 + 909656000 + 784 = 263283985656784

So I had an error before (263283984656784 vs 263283985656784, difference of 1000000).

D = 263283985656784 - 172277879613840 = 91006106042944

Let me check if this is a perfect square.

sqrt(91006106042944) ≈ ?

9539700² = ?
95397² = ?
95397 × 95397:
95397 × 95000 = 9062715000
95397 × 397 = 95397 × 400 - 95397 × 3 = 38158800 - 286191 = 37872609
Total = 9062715000 + 37872609 = 9100587609

9539700² = 9100587609 × 10^4 = 91005876090000

D - 91005876090000 = 91006106042944 - 91005876090000 = 229952944

9539700² + 229952944. 
(9539700 + d)² ≈ 9539700² + 2 × 9539700 × d
2 × 9539700 × d = 229952944
d = 229952944 / 19079400 ≈ 12.05

9539712² = 9539700² + 2 × 9539700 × 12 + 144 = 91005876090000 + 229492800 + 144 = 91006105582944

D - 91006105582944 = 91006106042944 - 91006105582944 = 460000

9539712² + 460000. 
(9539712 + d)² ≈ 9539712² + 2 × 9539712 × d
2 × 9539712 × d = 460000
d = 460000 / 19079424 ≈ 0.0241

Not an integer. So D is not a perfect square.

Hmm, this is problematic. The answer t - s/2 should be a clean number for a competition problem. Let me reconsider my approach.

Maybe I have the wrong model. Let me reconsider the problem.

Actually, wait. Let me reconsider whether the tangent circle is internally tangent to the full circles (containing them) or whether there's a different configuration.

Actually, I just realized something. The problem says "semicircles," not "circles." A semicircle is a half-disk. When we say a circle is "tangent to a semicircle," it could mean tangent to the boundary of the half-disk, which includes both the arc and the diameter.

If the tangent circle is tangent to the diameter (the straight side) of each semicircle, then it's tangent to the three sides of the triangle, which is the incircle! The incircle has radius r = 4. But the incircle is tangent to the sides (diameters) from inside the triangle, and the semicircles are drawn outside. The incircle is on the opposite side of each diameter from the semicircle. Is the incircle "tangent to the semicircle"? 

If "tangent to the semicircle" means tangent to the boundary of the half-disk, then the incircle is tangent to the diameter part of the boundary. But the incircle is on the opposite side from the half-disk, so it's tangent to the diameter from outside the half-disk. This could count as tangent to the semicircle.

But then t = r = 4, and t - s/2 = 4 - 10.5 = -6.5. That's a possible answer but seems unlikely for a competition.

Actually, no. The incircle is tangent to the sides of the triangle, which are the diameters of the semicircles. But the incircle is on the interior side, while the semicircles are on the exterior side. The incircle touches the diameter at the same point regardless of which side the semicircle is on. So the incircle is tangent to the straight edge of each semicircle. But is this what the problem means?

I think the problem means tangent to the curved part (the arc). Let me reconsider.

Actually, let me try a completely different approach. Let me think about what happens if we invert or use some transformation.

Hmm, let me try yet another approach. Let me consider the possibility that the tangent circle is tangent to the semicircles from the same side as the arcs (i.e., the tangent circle is in the half-disk region for each semicircle). But we showed the half-disks don't overlap for an acute triangle.

Wait, actually, I should double-check this. The half-disks are on the exterior of the triangle. Do they overlap?

Half-disk on BC: below BC (y < 0, roughly).
Half-disk on CA: on the side of CA opposite to B.
Half-disk on AB: on the side of AB opposite to C.

Let me check if the half-disk on BC and the half-disk on AB overlap.

The half-disk on BC is the set of points inside the circle centered at (13/2, 0) with radius 13/2, and below BC (y < 0).
The half-disk on AB is the set of points inside the circle centered at (99/26, 84/13) with radius 15/2, and on the side of AB opposite to C.

The line AB goes from (0,0) to (99/13, 168/13). The direction is (99, 168)/13. The normal pointing away from C: C = (13, 0). 

The line AB: 168x - 99y = 0 (since it passes through origin with direction (99, 168)). At C = (13, 0): 168 × 13 - 99 × 0 = 2184 > 0. So the side of AB containing C is where 168x - 99y > 0. The half-disk on AB is where 168x - 99y < 0.

The half-disk on BC is where y < 0 (below BC, which is the x-axis).

Do these overlap? We need a point where y < 0 and 168x - 99y < 0, i.e., 168x < 99y. Since y < 0, 99y < 0, so 168x < 99y < 0, meaning x < 0. 

Also, the point must be inside both circles. The circle on BC: (x - 13/2)² + y² < (13/2)², which means x² - 13x + y² < 0, i.e., x² + y² < 13x. Since x < 0, 13x < 0, but x² + y² ≥ 0, so x² + y² < 13x < 0 is impossible. So the half-disks on BC and AB don't overlap. ✓

OK so the half-disks don't overlap. The tangent circle must be in the region outside all three half-disks (the curvilinear triangle region containing the original triangle).

Let me reconsider. In this region, the tangent circle is on the opposite side of each diameter from the arc. For the tangency to be with the arc (not the diameter), the tangent circle must reach across the diameter to touch the arc. This means the tangent circle overlaps with the full circle, and the tangency is internal (the tangent circle contains the full circle, or is contained in it).

If the tangent circle contains the full circle (t > R_i), the distance from center to midpoint is t - R_i, and the tangency point is on the far side of the full circle from the tangent circle's center. If the center is inside the triangle (above BC), the tangency point with the circle on BC is below BC (on the arc). ✓

This is the internal tangency case I computed. t ≈ 11.04.

But the answer isn't clean. Let me re-examine my computation more carefully.

Actually, let me try to simplify the equation. 

0 = 1167452t² - 16226028t + 36891855

Let me try to factor out common factors.

1167452 = 4 × 291863 = 4 × 11 × 26533 = 4 × 11 × 13 × 2041 = 4 × 11 × 13 × 13 × 157 = 4 × 11 × 13² × 157

16226028 = 4 × 4056507 = 4 × 3³ × 7 × 13² × 127

36891855: Let me factor this.
36891855 / 3 = 12297285
12297285 / 3 = 4099095
4099095 / 3 = 1366365
1366365 / 3 = 455455
455455 / 5 = 91091
91091 / 7 = 13013
13013 / 7 = 1859
1859 / 13 = 143
143 / 11 = 13
13 / 13 = 1

So 36891855 = 3⁴ × 5 × 7² × 13² × 11 = 3⁴ × 5 × 7² × 11 × 13²

Let me verify: 3⁴ = 81, 81 × 5 = 405, 405 × 49 = 19845, 19845 × 11 = 218295, 218295 × 169 = 36891855. 
218295 × 169 = 218295 × 170 - 218295 = 37110150 - 218295 = 36891855. ✓

So:
1167452 = 2² × 11 × 13² × 157
16226028 = 2² × 3³ × 7 × 13² × 127
36891855 = 3⁴ × 5 × 7² × 11 × 13²

GCD = 13² = 169.

1167452 / 169 = 6914
16226028 / 169 = 96012
36891855 / 169 = 218295

Let me verify: 169 × 6914 = 169 × 7000 - 169 × 86 = 1183000 - 14534 = 1168466. That's not 1167452.

Hmm, let me recompute. 1167452 / 169:
169 × 6000 = 1014000
1167452 - 1014000 = 153452
169 × 900 = 152100
153452 - 152100 = 1352
169 × 8 = 1352
So 1167452 / 169 = 6908.

Let me verify: 169 × 6908 = 169 × 7000 - 169 × 92 = 1183000 - 15548 = 1167452. ✓

16226028 / 169:
169 × 96000 = 16224000
16226028 - 16224000 = 2028
169 × 12 = 2028
So 16226028 / 169 = 96012. ✓

36891855 / 169 = 218295. ✓ (verified above)

So the equation becomes:
6908t² - 96012t + 218295 = 0

Let me check GCD of 6908, 96012, 218295.
6908 = 4 × 1727 = 4 × 11 × 157
96012 = 4 × 24003 = 4 × 3 × 8001 = 4 × 3 × 3 × 2667 = 4 × 9 × 2667 = 4 × 9 × 3 × 889 = 4 × 27 × 889 = 4 × 27 × 7 × 127
218295 = 3⁴ × 5 × 7² × 11 = 81 × 5 × 49 × 11

GCD: 6908 has factors 2² × 11 × 157. 96012 has 2² × 3³ × 7 × 127. 218295 has 3⁴ × 5 × 7² × 11.
Common factors: 6908 and 96012 share 2² = 4. 218295 is odd, so no factor of 2. So GCD = 1.

So the simplified equation is 6908t² - 96012t + 218295 = 0.

Discriminant = 96012² - 4 × 6908 × 218295

96012² = ?
96012² = (96000 + 12)² = 9216000000 + 2304000 + 144 = 9218304144

4 × 6908 × 218295:
6908 × 218295 = ?
6908 × 200000 = 1381600000
6908 × 18000 = 124344000
6908 × 295 = 6908 × 300 - 6908 × 5 = 2072400 - 34540 = 2037860
Total = 1381600000 + 124344000 + 2037860 = 1509981860

4 × 1509981860 = 6039927440

D = 9218304144 - 6039927440 = 3178376704

sqrt(3178376704) = ?
56376² = ?
56000² = 3136000000
56376² = (56000 + 376)² = 3136000000 + 42112000 + 141376 = 3180353376

Too big. 3180353376 - 3178376704 = 1976672.

56350² = (56000 + 350)² = 3136000000 + 39200000 + 122500 = 3175322500

3178376704 - 3175322500 = 3054204

56358² = 56350² + 2 × 56350 × 8 + 64 = 3175322500 + 901600 + 64 = 3176224164
56360² = 56358² + 2 × 56358 × 2 + 4 = 3176224164 + 225432 + 4 = 3176449600
56370² = 56360² + 2 × 56360 × 10 + 100 = 3176449600 + 1127200 + 100 = 3177576900
56380² = 56370² + 2 × 56370 × 10 + 100 = 3177576900 + 1127400 + 100 = 3178704400

3178704400 > 3178376704. So between 56370 and 56380.

56377² = 56370² + 2 × 56370 × 7 + 49 = 3177576900 + 789180 + 49 = 3178366129
56378² = 56377² + 2 × 56377 + 1 = 3178366129 + 112755 = 3178478884

3178478884 > 3178376704. So between 56377 and 56378.

3178376704 - 3178366129 = 10575. Not a perfect square.

So the discriminant is not a perfect square, and t is irrational. This means t - s/2 is also irrational, which is unusual for a competition problem asking to "calculate the value."

Let me reconsider the problem. Maybe I have the wrong tangency model.

Let me reconsider: maybe the problem is about the circle inscribed in the curvilinear triangle formed by the three semicircular arcs, but the tangency is with the arcs from inside, and the distance relationship is different from what I assumed.

Actually, wait. I think the issue might be that the tangent circle is externally tangent to the semicircles (the half-disks), not the full circles. Being externally tangent to a half-disk means the tangent circle is outside the half-disk and tangent to its boundary. The boundary includes the arc and the diameter. If the tangent circle is tangent to the arc (not the diameter), and it's outside the half-disk, then it's on the opposite side of the diameter from the arc. The distance from the center to the midpoint is t + R (external to the full circle), and the tangency point is on the arc side.

But wait, if the tangent circle is on the opposite side of the diameter from the arc, and externally tangent to the full circle, the tangency point is on the near side (the tangent circle's side), which is the opposite side from the arc. So the tangency point is NOT on the arc. Contradiction.

Unless the tangent circle is on the same side as the arc (inside the half-disk region), and externally tangent to the full circle. Then the tangency point is on the arc side. But then the tangent circle is in the half-disk region, and we showed the half-disks don't overlap.

I'm stuck. Let me try a completely different approach.

Let me reconsider the problem. Maybe "semicircles with diameters BC, CA, AB drawn outside the triangle" and "a circle tangent to all three semicircles" refers to a different geometric configuration than what I've been considering.

Perhaps the tangent circle is in the "gap" between the three semicircles, outside the triangle but between the arcs. But for an acute triangle, the arcs are on the far side of each side, and the gaps between them are at the vertices.

Actually, you know what, let me try the problem with a different tangency model. What if the tangent circle is internally tangent to some semicircles and externally tangent to others?

Let me try: the tangent circle is inside the curvilinear triangle (containing the original triangle), and it's tangent to each arc. For each arc, the tangent circle is on the opposite side of the diameter from the arc. The tangent circle overlaps with the full circle (since it reaches across the diameter to touch the arc). The tangency is internal: the full circle is inside the tangent circle (t > R_i), and the distance is t - R_i.

This is what I computed, giving t ≈ 11.04. But the answer isn't clean.

Alternatively, the tangent circle is smaller than the full circles (t < R_i), and it's inside the full circle, tangent to it from inside. The distance is R_i - t. The tangency point is on the tangent circle's side of the full circle's center. If the tangent circle is above BC (inside the triangle) and the full circle on BC has center on BC, the tangency point is above BC (the upper half of the full circle, not the arc). So the tangency point is not on the arc. This doesn't work.

Hmm, unless the tangent circle is below BC (in the half-disk region). But then it can't be in the triangle region for all three simultaneously.

I think the internal tangency (tangent circle contains the full circles) is the right model, and the answer is just not a "nice" number. But the problem says "calculate the value of t - s/2," implying a specific numerical answer.

Let me try to compute t more precisely and see if t - s/2 simplifies.

t = (96012 + sqrt(3178376704)) / (2 × 6908) = (96012 + sqrt(3178376704)) / 13816

sqrt(3178376704) ≈ 56377.094

t ≈ (96012 + 56377.094) / 13816 ≈ 152389.094 / 13816 ≈ 11.0358

t - s/2 ≈ 11.0358 - 10.5 = 0.5358

That's not clean. Let me try the other root:
t = (96012 - 56377.094) / 13816 ≈ 39634.906 / 13816 ≈ 2.869

This is less than 7.5, so it can't contain the full circles. Not valid for this model.

Hmm, let me reconsider the problem entirely. Maybe I'm wrong about the tangency model.

Let me re-read the problem: "Semicircles with diameters BC, CA, AB are drawn outside of the triangle. A circle with radius t is tangent to all three semicircles."

Maybe "tangent to all three semicircles" means tangent to the three semicircular arcs, and the circle is in the region between the arcs (the curvilinear triangle). The tangency is such that the circle touches each arc from inside the curvilinear triangle.

For the curvilinear triangle (region containing the original triangle, bounded by the three arcs), the inscribed circle touches each arc from inside. The inscribed circle is in the original triangle region, and it reaches out to touch each arc.

For the arc on BC (below BC): the inscribed circle is above BC, and it touches the arc below BC. The inscribed circle must extend below BC to reach the arc. This means the inscribed circle is large enough to cross BC.

The distance from the inscribed circle's center to the midpoint of BC: if the inscribed circle contains the full circle on BC (t > 13/2), then distance = t - 13/2, and the tangency point is on the far side (below BC, on the arc). ✓

This is the model I've been using. Let me try to see if maybe I made an error in the coordinate setup.

Let me recheck the coordinates.

B = (0, 0), C = (13, 0), A = (99/13, 168/13).

Check: AB = sqrt((99/13)² + (168/13)²) = sqrt((9801 + 28224)/169) = sqrt(38025/169) = 195/13 = 15. ✓
AC = sqrt((99/13 - 13)² + (168/13)²) = sqrt((99/13 - 169/13)² + (168/13)²) = sqrt((-70/13)² + (168/13)²) = sqrt((4900 + 28224)/169) = sqrt(33124/169) = 182/13 = 14. ✓

Midpoints:
M_a = midpoint of BC = (13/2, 0) ✓
M_b = midpoint of CA = ((13 + 99/13)/2, (0 + 168/13)/2) = ((169/13 + 99/13)/2, 84/13) = (268/26, 84/13) = (134/13, 84/13) ✓
M_c = midpoint of AB = (99/26, 84/13) ✓

Radii: a/2 = 13/2, b/2 = 7, c/2 = 15/2 ✓

These all look correct. Let me recheck the equations.

For internal tangency (tangent circle contains the full circles):
|P - M_a| = t - 13/2
|P - M_b| = t - 7
|P - M_c| = t - 15/2

Squaring:
(x - 13/2)² + y² = (t - 13/2)² = t² - 13t + 169/4
x² - 13x + 169/4 + y² = t² - 13t + 169/4
x² + y² - 13x = t² - 13t ... (1)

(x - 134/13)² + (y - 84/13)² = (t - 7)² = t² - 14t + 49
x² - (268/13)x + (134/13)² + y² - (168/13)y + (84/13)² = t² - 14t + 49

(134/13)² + (84/13)² = (17956 + 7056)/169 = 25012/169 = 148

x² + y² - (268/13)x - (168/13)y + 148 = t² - 14t + 49
x² + y² - (268/13)x - (168/13)y + 99 = t² - 14t ... (2)

(x - 99/26)² + (y - 84/13)² = (t - 15/2)² = t² - 15t + 225/4

(99/26)² + (84/13)² = 9801/676 + 7056/169 = 9801/
