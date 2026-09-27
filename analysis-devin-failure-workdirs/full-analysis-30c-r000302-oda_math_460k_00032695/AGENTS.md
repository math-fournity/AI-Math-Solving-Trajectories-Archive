# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Suppose $f(x) = 3x-2$ and $g(x) = 4x+5$. Calculate $g(f(x))$.       — 题目文本
#   <think>Okay, let's see. The problem is to calculate g(f(x)) where f(x) is 3x - 2 and g(x) is 4x + 5. Hmm, so first, I need to remember what function composition is. Function composition means that we substitute the entire function f(x) into the function g. So g(f(x)) is like taking g of whatever f(x) is. 

Let me start by writing down what f(x) is. f(x) = 3x - 2. Then, g(x) is 4x + 5. So when we do g(f(x)), we need to replace every x in the g function with f(x). That is, wherever there's an x in g(x), we put (3x - 2) instead. 

Let me write that out. g(f(x)) = g(3x - 2). Now, since g(x) is 4x + 5, replacing x with (3x - 2) gives us 4*(3x - 2) + 5. Let me compute that step by step. First, distribute the 4 into the parentheses: 4*3x is 12x, and 4*(-2) is -8. So that part becomes 12x - 8. Then we add the 5. So 12x - 8 + 5. Combining like terms, -8 + 5 is -3. So the entire expression simplifies to 12x - 3. 

Let me check that again to make sure I didn't make a mistake. Starting with g(f(x)): substitute f(x) into g. So g takes an input, multiplies by 4, then adds 5. The input here is f(x) which is 3x - 2. So 4*(3x - 2) + 5. Multiply 4 by 3x: 12x. 4 times -2 is -8. Then +5. So 12x -8 +5. Combine constants: -8 +5 is -3. So 12x -3. That seems right. I think that's the answer.
</think>

To calculate \( g(f(x)) \), we need to substitute \( f(x) \) into the function \( g(x) \). 

Given:
- \( f(x) = 3x - 2 \)
- \( g(x) = 4x + 5 \)

First, substitute \( f(x) \) into \( g(x) \):
\[
g(f(x)) = g(3x - 2)
\]

Next, replace \( x \) in \( g(x) \) with \( 3x - 2 \):
\[
g(3x - 2) = 4(3x - 2) + 5
\]

Simplify the expression:
\[
4(3x - 2) + 5 = 12x - 8 + 5 = 12x - 3
\]

Thus, the final answer is \(\boxed{12x - 3}\).  — 标准解答
#   The problem asks about a point P on the Neuberg cubic of triangle ABC such that the cevian triangle of P is equilateral. Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC. If R is the isogonal conjugate of P, find the ratio QR/PQ.

Let me think about this carefully.

First, let me recall the relevant facts:

1. **Neuberg cubic**: The Neuberg cubic is the locus of points P such that the reflections of P over the sides of triangle ABC are collinear. Wait, actually let me reconsider. The Neuberg cubic is the isogonal pivotal cubic with pivot at the point... Actually, the Neuberg cubic is the locus of points P such that the cevian triangle of P is in perspective with triangle ABC... no.

Let me recall more carefully. The Neuberg cubic is a famous cubic curve. One characterization: P is on the Neuberg cubic if and only if the reflections of P over the sides of BC, CA, AB are collinear with the isogonal conjugate of P... no.

Actually, the Neuberg cubic has several characterizations:
- It's the locus of P such that the reflections of P in the sides of ABC are collinear. Wait, that's not quite right either.

Let me think again. The Neuberg cubic K001 (in Bernard Gibert's catalog) is the isogonal cubic with pivot at the de Longchamps point. 

Key property: P is on the Neuberg cubic if and only if the reflections of P over the sidelines of ABC are collinear. The line through these three reflections is called the "orthic axis" or related to it.

Actually, I think the correct statement is: P lies on the Neuberg cubic if and only if the reflections of P in the three sides of triangle ABC are collinear. And the line containing them passes through the isogonal conjugate of P.

Wait, let me be more precise. The Neuberg cubic is the locus of points P such that the reflections of P in the sides of BC, CA, AB are collinear. The line on which these reflections lie passes through the isogonal conjugate P* of P.

Hmm, actually I recall that the key property is: if P is on the Neuberg cubic, then the reflections of P over the sides of the triangle are collinear, and this line passes through the isogonal conjugate of P.

So if R is the isogonal conjugate of P, then R lies on the line containing the three reflections of P.

Now, Q is defined as "the point of concurrency of the reflections of P about the sides of triangle ABC." 

Wait, this is confusing. If the reflections are collinear (on the Neuberg cubic), they don't have a "point of concurrency." Unless "reflections of P about the sides" means something different—like reflecting the cevians, or reflecting lines.

Let me re-read: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

Hmm, maybe "reflections of P about the sides" refers to the lines obtained by reflecting the cevians AP, BP, CP about the sides? Or maybe it refers to reflecting the lines PA, PB, PC?

Actually, I think there might be a different interpretation. Let me reconsider.

Actually, wait. Let me reconsider the problem. Perhaps the "reflections of P about the sides" are three points (the reflections of P over each side), and "point of concurrency" doesn't make sense for three points unless they're collinear (and then there's no concurrency point).

Let me think about this differently. Maybe Q is defined differently. Perhaps "the reflections of P about the sides" means the reflection lines—i.e., for each side, we reflect P over that side to get a point, and then... no.

Actually, I wonder if the problem means: reflect the cevians of P over the sides. The cevian from A through P hits BC at some point D. Reflect the line AD (or the cevian) over the perpendicular bisector... no, reflect over the side BC.

Actually, let me reconsider. In the context of the Neuberg cubic, there's a well-known construction. Let me think about what "reflections of P about the sides" could mean in terms of cevians.

Hmm, actually maybe the problem is using "reflections of P about the sides" to mean the reflections of the point P over each side, giving three points P_a, P_b, P_c. On the Neuberg cubic, these are collinear. But the problem says "point of concurrency," which suggests lines, not points.

Let me reconsider: maybe "reflections of P about the sides" means: for each vertex, reflect the cevian line. Specifically:
- The cevian from A to P meets BC at D. Reflect line AD over line BC (or over the angle bisector at A?)...

Actually, I think the most natural reading might be different. Let me consider: "the reflections of P about the sides of triangle ABC" could mean the lines obtained by reflecting AP over side BC, BP over side CA, CP over side AB. But that's a bit unusual.

Alternatively, maybe it's: reflect the lines PA, PB, PC about the sides BC, CA, AB respectively. These three reflected lines might be concurrent, and that concurrency point is Q.

Actually, wait. I think I recall now. There's a classical result related to the Neuberg cubic:

The Neuberg cubic is the locus of P such that if you reflect the cevians AP, BP, CP over the sides BC, CA, AB respectively, the three reflected lines are concurrent. And this concurrency point is related to the isogonal conjugate.

Hmm, but that doesn't sound right either, because reflecting a cevian over the opposite side is a specific operation.

Let me think about this more carefully.

Actually, I think the correct characterization of the Neuberg cubic involves the following: P is on the Neuberg cubic if and only if the reflections of the lines AP, BP, CP in the sides BC, CA, AB respectively are concurrent.

Wait, I think I'm overcomplicating this. Let me look at this from a different angle.

The Neuberg cubic has the property that it's the locus of P such that the cevian triangle of P is in perspective with the reflection triangle... or something like that.

Actually, let me think about what's known:

The Neuberg cubic K001 is characterized by: P is on K001 iff the reflections of P over the sides of ABC are collinear. The line through these reflections is called the "orthic axis" of P (or the "anti-pedal line"). This line passes through the isogonal conjugate P* of P.

So if R = P* (isogonal conjugate), then R lies on the line through the three reflections of P.

Now, the problem says Q is "the point of concurrency of the reflections of P about the sides." If the reflections are three points that are collinear, there's no "point of concurrency." So maybe the problem means something else by "reflections."

Let me re-read the problem once more: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

Hmm, maybe "reflections of P about the sides" means the three lines, each being the perpendicular from P to a side, reflected... no.

Actually, I think there might be a different interpretation. In some formulations, "the reflection of P about side BC" could refer to the line that is the reflection of line AP about line BC. But that's unusual.

Wait, actually, I think the problem might be referring to the following: reflect the cevian lines. The cevian from A through P is line AP. Reflect this line about side BC. Similarly reflect BP about CA and CP about AB. These three reflected lines are concurrent when P is on the Neuberg cubic, and the point of concurrency is Q.

Actually no, I don't think that's the standard characterization.

Let me try yet another interpretation. Perhaps "reflections of P about the sides" means: take the reflection of P over each side, getting three points. Then "point of concurrency" refers to the cevians from the vertices to these reflected points. Specifically:
- Reflect P over BC to get P_a
- Reflect P over CA to get P_b  
- Reflect P over AB to get P_c
- Lines AP_a, BP_b, CP_c are concurrent at Q.

This would make more sense with "point of concurrency." And on the Neuberg cubic, these lines would indeed be concurrent.

Hmm, but I'm not sure this is a known property.

Actually, let me think about this differently. Let me consider the possibility that the problem is well-posed and that the answer is a clean ratio.

Let me consider the special case where the cevian triangle of P is equilateral. This is a very specific condition.

The cevian triangle of P is the triangle formed by the feet of the cevians from P to the sides. If P has barycentric coordinates (x:y:z), the cevian triangle has vertices at (0:y:z), (x:0:z), (x:y:0) on the sides BC, CA, AB respectively.

For the cevian triangle to be equilateral is a strong condition.

Now, let me think about what's special about the Neuberg cubic and equilateral cevian triangles.

Actually, I recall that there's a connection between the Neuberg cubic and equilateral triangles. The Neuberg cubic passes through the vertices of the two equilateral triangles erected on the sides of ABC (the Napoleon triangles related points).

Let me think about specific points on the Neuberg cubic where the cevian triangle is equilateral.

Hmm, this is getting complicated. Let me try to think about this more carefully using coordinates.

Let me set up coordinates. Let me use a specific triangle to compute, since the ratio might be universal (independent of the triangle).

Actually, wait. The problem says "find the ratio QR/PQ," implying it's a fixed number. So it should be independent of the triangle and the specific point P (as long as the conditions are met).

Let me try to use a specific triangle and specific point P.

Let me consider the equilateral triangle ABC first. If ABC is equilateral, then by symmetry, the Neuberg cubic has special properties. But for an equilateral triangle, many things degenerate.

Let me try a different approach. Let me use a right triangle or a specific triangle where I can compute.

Actually, let me think about this more carefully from the theory.

The Neuberg cubic is the isogonal cubic with pivot at the de Longchamps point L. This means:
- If P is on the cubic, then its isogonal conjugate R is also on the cubic.
- The line PR passes through the pivot L (de Longchamps point).

Wait, that's the definition of an isogonal cubic with pivot: P is on the cubic iff P, its isogonal conjugate P*, and the pivot are collinear.

So for the Neuberg cubic: P, R (= isogonal conjugate of P), and L (de Longchamps point) are collinear.

Now, the de Longchamps point L is the reflection of the orthocenter H over the circumcenter O. So L = 2O - H.

Now, the problem also involves Q, the point of concurrency of the reflections of P about the sides.

Let me reconsider what "reflections of P about the sides" means. I think the most standard interpretation in the context of the Neuberg cubic is:

The reflections of P over the three sides are three points, and on the Neuberg cubic, these three points are collinear. The line through them passes through R (the isogonal conjugate).

But the problem says "point of concurrency," not "line of collinearity." So maybe the problem is using a different definition.

Let me consider another possibility: maybe "reflections of P about the sides" means reflecting the cevians. Specifically:
- Cevian AP meets BC at D. Reflect the cevian line AD about side BC to get a line through D.
- Similarly for the other two cevians.
- These three reflected lines are concurrent at Q.

This interpretation would give a "point of concurrency."

Actually, I think I recall now. There's a theorem that says: P is on the Neuberg cubic if and only if the reflections of the cevians AP, BP, CP in the sides BC, CA, AB are concurrent. And the point of concurrency Q, the isogonal conjugate R, and P have a specific relationship.

Let me think about this. If we reflect line AP about side BC, we get a line through D (where D is the foot of the cevian on BC). The reflection of line AP about line BC...

Hmm, actually, reflecting a line about another line: if line AP makes angle α with BC, the reflected line makes angle -α with BC, passing through D.

Let me try to work this out with coordinates.

Let me use a specific triangle. Let me take A = (0, 3), B = (-2, 0), C = (2, 0). This is an isoceles triangle.

Actually, let me try a more systematic approach. Let me use barycentric coordinates.

In barycentric coordinates, P = (u : v : w). The cevian triangle of P has vertices:
- D = (0 : v : w) on BC
- E = (u : 0 : w) on CA  
- F = (u : v : 0) on AB

For the Neuberg cubic in barycentric coordinates, the equation is:
∑ u(v² - w²)(something) = 0

Actually, the Neuberg cubic equation in barycentrics is:
∑ x(y² - z²)(x²(y² + z²) - y²z² - ... ) 

This is getting complicated. Let me try a computational approach with a specific triangle.

Let me use the triangle with A = (0, 4), B = (-3, 0), C = (3, 0).

Hmm, let me think about this differently. Let me consider the possibility that the answer is 2.

Actually, let me think about what's known about the relationship between P, Q, and R on the Neuberg cubic.

If the Neuberg cubic is the locus where the reflections of P over the sides are collinear, and this line passes through R, then maybe Q is defined differently.

Let me re-read the problem: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

OK here's another interpretation: "the reflections of P about the sides" could be three lines (not points). For each side, we can consider the line connecting P to its reflection over that side. This line is perpendicular to the side and passes through the midpoint of P and its reflection (which is on the side). So these three lines are the perpendiculars from P to the three sides. These are generally not concurrent (they all pass through P, actually—wait, no).

Hmm, the line connecting P to its reflection over side BC is perpendicular to BC and passes through P. So all three such lines pass through P. That's trivially concurrent at P, which doesn't give useful information.

Let me try yet another interpretation. Maybe "reflections of P about the sides" means: for each side, consider the line that is the reflection of the opposite cevian about that side. 

- Reflect cevian AP (or line AP) about side BC → get line ℓ_a
- Reflect cevian BP about side CA → get line ℓ_b  
- Reflect cevian CP about side AB → get line ℓ_c
- Q = concurrency point of ℓ_a, ℓ_b, ℓ_c

This makes sense with "point of concurrency" and is related to the Neuberg cubic.

Actually, I now recall more clearly. The Neuberg cubic can be characterized as follows:

P is on the Neuberg cubic if and only if the reflections of the lines AP, BP, CP in the sides BC, CA, AB respectively are concurrent.

The point of concurrency is sometimes denoted Q, and there's a relationship between P, Q, and the isogonal conjugate R of P.

Let me try to verify this and find the ratio.

Let me work with a specific example. Let me use the triangle A = (0, 3), B = (-2, 0), C = (2, 0), and find a point P on the Neuberg cubic with equilateral cevian triangle.

Actually, this is getting very complicated computationally. Let me think about whether there's a more theoretical approach.

Let me consider the key relationships:

1. P is on the Neuberg cubic → reflections of cevians AP, BP, CP over sides BC, CA, AB are concurrent at Q.
2. R = isogonal conjugate of P.
3. The cevian triangle of P is equilateral.

For the Neuberg cubic, there's a known result: the point of concurrency Q of the reflected cevians, the point P, and the isogonal conjugate R are collinear, and there's a specific ratio.

Actually, I think the key result might be: Q, P, R are collinear and Q is the reflection of R over P, or something like that, giving QR/PQ = 2.

Or maybe the relationship is that P is the midpoint of QR, giving QR/PQ = 2... no, if P is the midpoint of QR, then PQ = PR and QR = 2PQ, so QR/PQ = 2.

Alternatively, maybe R is the midpoint of PQ, giving QR/PQ = 1.

Or maybe Q = R, giving QR/PQ = 0, but that seems too trivial.

Let me think about this more carefully.

Actually, I recall that for the Neuberg cubic, there's a result involving the "anti-complementary triangle" or the "cevian conic." 

Let me try a different approach. Let me think about the specific case where the cevian triangle is equilateral and see what constraints this imposes.

The cevian triangle of P = (u:v:w) has vertices D = (0:v:w), E = (u:0:w), F = (u:v:0).

For this to be equilateral, we need DE = EF = FD.

In barycentric coordinates, the distance between two points involves the side lengths of the triangle. This is complex.

Let me try a very specific approach. Let me use an equilateral triangle ABC and see what happens.

If ABC is equilateral with side length s, then by symmetry, the Neuberg cubic has nice properties. For an equilateral triangle, the isogonal conjugate of P = (u:v:w) is R = (a²/u : b²/v : c²/w) = (1/u : 1/v : 1/w) since a = b = c.

For an equilateral triangle, the Neuberg cubic... actually, for an equilateral triangle, many cubics degenerate because of the high symmetry. The de Longchamps point coincides with the circumcenter and orthocenter (they're all the same point for an equilateral triangle). So the Neuberg cubic, being the isogonal cubic with pivot at the de Longchamps point (= circumcenter = orthocenter = centroid), might degenerate.

Actually, for an equilateral triangle, O = H = G = L, so the isogonal cubic with pivot at L would be the set of P such that P, P*, and L are collinear. Since L is the centroid (1:1:1), this is the condition that (u:v:w), (1/u:1/v:1/w), and (1:1:1) are collinear.

The collinearity condition is:
| u   v   w  |
| 1/u 1/v 1/w| = 0
| 1   1   1  |

Expanding: u(1/v - 1/w) - v(1/u - 1/w) + w(1/u - 1/v) = 0
= u(w-v)/(vw) - v(w-u)/(uw) + w(v-u)/(uv) = 0
= [u²(w-v) - v²(w-u) + w²(v-u)] / (uvw) = 0

Numerator: u²w - u²v - v²w + v²u + w²v - w²u
= u²(w-v) + v²(u-w) + w²(v-u)
= u²(w-v) - v²(w-u) + w²(v-u)

Let me factor: = (u-v)(v-w)(w-u) ... let me check.

Actually, u²(w-v) + v²(u-w) + w²(v-u) is a well-known expression that equals -(u-v)(v-w)(w-u).

Let me verify: (u-v)(v-w)(w-u) = (u-v)(vw - vu - w² + wu) = (u-v)(vw - vu - w² + wu)
= uvw - vu² - uw² + u²w - v²w + v²u + vw² - vuw
= -vu² - uw² + u²w - v²w + v²u + vw²
= u²w - u²v + v²u - v²w + vw² - uw²
= u²(w-v) + v²(u-w) + w²(v-u) ✓

So the Neuberg cubic for an equilateral triangle is (u-v)(v-w)(w-u) = 0, which is the union of the three medians. This is degenerate, so the equilateral triangle case won't work well.

Let me try a different triangle. Let me use a right triangle.

Let me use A = (0, 0), B = (4, 0), C = (0, 3). This is a 3-4-5 right triangle with the right angle at A.

Side lengths: a = BC = 5, b = CA = 3, c = AB = 4.

For this triangle:
- O (circumcenter) = midpoint of BC = (2, 3/2)
- H (orthocenter) = A = (0, 0) (since it's a right triangle at A)
- L (de Longchamps point) = 2O - H = (4, 3)

The Neuberg cubic is the locus of P such that P, R (isogonal conjugate of P), and L are collinear.

In barycentric coordinates, the isogonal conjugate of P = (u:v:w) is R = (a²/u : b²/v : c²/w) = (25/u : 9/v : 16/w).

L (de Longchamps point) in barycentric coordinates: L = 2O - H. 

O in barycentrics = (sin 2A : sin 2B : sin 2C). For our triangle:
- A = 90°, B = arctan(3/4), C = arctan(4/3)
- sin 2A = sin 180° = 0
- sin 2B = 2 sin B cos B = 2 · (3/5) · (4/5) = 24/25
- sin 2C = 2 sin C cos C = 2 · (4/5) · (3/5) = 24/25

So O = (0 : 24/25 : 24/25) = (0 : 1 : 1). This makes sense—O is the midpoint of BC.

H = A = (1 : 0 : 0) in barycentrics.

L = 2O - H. In barycentric coordinates, we can't simply do 2O - H because barycentric coordinates are homogeneous. We need to convert to Cartesian, compute, then convert back.

O = (2, 3/2) in Cartesian, H = (0, 0), L = (4, 3).

Converting L = (4, 3) to barycentrics: 
L = αA + βB + γC where α + β + γ = 1
4 = 0·α + 4·β + 0·γ → β = 1
3 = 0·α + 0·β + 3·γ → γ = 1
α = 1 - β - γ = 1 - 1 - 1 = -1

So L = (-1 : 1 : 1) in barycentrics.

The Neuberg cubic condition: P = (u:v:w), R = (25/u : 9/v : 16/w), L = (-1:1:1) are collinear.

Collinearity:
| u    v    w   |
| 25/u 9/v 16/w| = 0
| -1   1    1   |

Expanding:
u(9/v · 1 - 16/w · 1) - v(25/u · 1 - 16/w · (-1)) + w(25/u · 1 - 9/v · (-1)) = 0

= u(9/v - 16/w) - v(25/u + 16/w) + w(25/u + 9/v) = 0

= 9u/v - 16u/w - 25v/u - 16v/w + 25w/u + 9w/v = 0

Multiply by uvw:
9u²w - 16u²v - 25v²w - 16v²u + 25w²u + 9w²v = 0

Rearranging:
9u²w - 16u²v - 16v²u - 25v²w + 25w²u + 9w²v = 0

This is the equation of the Neuberg cubic for our triangle.

Now, I also need the condition that the cevian triangle of P is equilateral. The cevian triangle has vertices:
- D = (0 : v : w) on BC
- E = (u : 0 : w) on CA
- F = (u : v : 0) on AB

I need to compute the side lengths of triangle DEF and set them equal.

This is getting quite involved. Let me try to use Cartesian coordinates.

A = (0,0), B = (4,0), C = (0,3).

P = (u:v:w) in barycentrics → Cartesian: P = (u·A + v·B + w·C)/(u+v+w) = (4v/(u+v+w), 3w/(u+v+w)).

Let me set s = u+v+w and use normalized barycentrics. P = (4v/s, 3w/s).

D = (0:v:w) → Cartesian: (4v/(v+w), 3w/(v+w))
E = (u:0:w) → Cartesian: (0, 3w/(u+w))... wait, E = (u:0:w) means E = (u·A + 0·B + w·C)/(u+w) = (0, 3w/(u+w)). Hmm, that's on CA (the y-axis from (0,0) to (0,3)).

F = (u:v:0) → Cartesian: (4v/(u+v), 0). This is on AB (the x-axis from (0,0) to (4,0)).

So:
D = (4v/(v+w), 3w/(v+w))
E = (0, 3w/(u+w))
F = (4v/(u+v), 0)

Now I need DE = EF = FD.

DE² = (4v/(v+w))² + (3w/(v+w) - 3w/(u+w))²
= 16v²/(v+w)² + 9w²(1/(v+w) - 1/(u+w))²
= 16v²/(v+w)² + 9w²((u+w-v-w)/((v+w)(u+w)))²
= 16v²/(v+w)² + 9w²(u-v)²/((v+w)²(u+w)²)
= [16v²(u+w)² + 9w²(u-v)²] / ((v+w)²(u+w)²)

EF² = (4v/(u+v))² + (3w/(u+w))²
= 16v²/(u+v)² + 9w²/(u+w)²

FD² = (4v/(v+w) - 4v/(u+v))² + (3w/(v+w))²
= 16v²(1/(v+w) - 1/(u+v))² + 9w²/(v+w)²
= 16v²((u+v-v-w)/((v+w)(u+v)))² + 9w²/(v+w)²
= 16v²(u-w)²/((v+w)²(u+v)²) + 9w²/(v+w)²
= [16v²(u-w)² + 9w²(u+v)²] / ((v+w)²(u+v)²)

Setting DE² = EF²:
[16v²(u+w)² + 9w²(u-v)²] / ((v+w)²(u+w)²) = [16v²(u+w)² + 9w²(u+v)²] / ((u+v)²(u+w)²)

Wait, let me redo EF²:
EF² = (4v/(u+v) - 0)² + (0 - 3w/(u+w))² = 16v²/(u+v)² + 9w²/(u+w)²

So EF² = [16v²(u+w)² + 9w²(u+v)²] / ((u+v)²(u+w)²)

Setting DE² = EF²:
[16v²(u+w)² + 9w²(u-v)²] / ((v+w)²(u+w)²) = [16v²(u+w)² + 9w²(u+v)²] / ((u+v)²(u+w)²)

Cancel (u+w)²:
[16v²(u+w)² + 9w²(u-v)²] / (v+w)² = [16v²(u+w)² + 9w²(u+v)²] / (u+v)²

This is getting very messy. Let me try a different approach—maybe use numerical computation.

Actually, let me try to think about this problem more cleverly.

The condition that the cevian triangle is equilateral is very restrictive. For a given triangle ABC, there are only finitely many points P on the Neuberg cubic with equilateral cevian triangle.

Let me think about what special points on the Neuberg cubic might have equilateral cevian triangles.

Actually, I recall that the two isodynamic points are on the Neuberg cubic. The isodynamic points are related to equilateral triangles. Let me check if the cevian triangle of an isodynamic point is equilateral.

The isodynamic points are the points from which the triangle subtends equal angles (120° each for the first isodynamic point). They are the isogonal conjugates of the Fermat points.

The first Fermat point (isogonal conjugate of the first isodynamic point) is the point from which all sides subtend 120° angles (for triangles with all angles < 120°).

Hmm, but the cevian triangle of the Fermat point being equilateral... I'm not sure about that.

Let me think about this differently. Let me consider the possibility that P is one of the isodynamic points.

The isodynamic points have the property that their pedal triangles are equilateral. But the problem asks about the cevian triangle, not the pedal triangle.

The pedal triangle is formed by the feet of perpendiculars from P to the sides. The cevian triangle is formed by the intersections of cevians AP, BP, CP with the opposite sides.

These are different in general. The pedal triangle of P has vertices at the feet of perpendiculars, while the cevian triangle has vertices at the cevian feet.

For the pedal triangle to be equilateral, P is an isodynamic point. For the cevian triangle to be equilateral, P is... some other special point.

Let me think about what points have equilateral cevian triangles.

Actually, I think I should just try to compute this numerically. Let me pick a specific triangle and find P numerically.

Let me use the triangle A = (0,0), B = (4,0), C = (0,3) (the 3-4-5 right triangle).

I need to find P = (u:v:w) such that:
1. P is on the Neuberg cubic: 9u²w - 16u²v - 16v²u - 25v²w + 25w²u + 9w²v = 0
2. The cevian triangle is equilateral: DE = EF = FD

Let me parametrize. Since barycentric coordinates are homogeneous, I can set w = 1 and use u, v as parameters. Then I have two equations (from the equilateral condition: DE = EF and EF = FD) and one equation (Neuberg cubic). That's three equations in two unknowns, which is overdetermined. So there might be only finitely many solutions (or none for this particular triangle).

Wait, actually, the equilateral condition gives two equations (DE = EF and EF = FD), and the Neuberg cubic gives one equation. With w = 1, we have two unknowns u, v and three equations. This is overdetermined, so generically there are no solutions. But the problem states that such a P exists, so maybe the problem is asking for a general result that holds when such a P exists.

Hmm, but the problem says "Consider a point P on the Neuberg cubic such that the cevian triangle of P is equilateral." This implies such points exist. Maybe they exist for specific triangles, or maybe the problem is about a general property.

Actually, wait. Let me reconsider. The problem might be implying that for any triangle, there exist points on the Neuberg cubic with equilateral cevian triangle, and the ratio QR/PQ is always the same. Or it might be that the problem is about a specific configuration.

Let me reconsider the problem. Maybe I'm overcomplicating the interpretation of Q.

Let me re-read: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

I think "the reflections of P about the sides" are three points (reflections of P over each side). "Point of concurrency" might be a mistranslation or unusual phrasing for "the point" associated with these reflections. On the Neuberg cubic, the three reflections are collinear, and the line passes through R (isogonal conjugate). 

But "point of concurrency" of three collinear points doesn't make sense. Unless Q is defined as some specific point on this line.

Wait, maybe "reflections of P about the sides" refers to the three lines obtained by reflecting line AP about the perpendicular bisector of BC... no, that's weird.

OK let me try another interpretation. Maybe "reflections of P about the sides" means: for each side, reflect the cevian from the opposite vertex through P about that side. So:
- Reflect line AP about side BC → line ℓ_a
- Reflect line BP about side CA → line ℓ_b
- Reflect line CP about side AB → line ℓ_c

And Q is the concurrency point of ℓ_a, ℓ_b, ℓ_c.

This is actually a known characterization of the Neuberg cubic! P is on the Neuberg cubic iff these three reflected lines are concurrent.

Let me try to verify this and compute the ratio.

Let me work with the 3-4-5 right triangle: A = (0,0), B = (4,0), C = (0,3).

Let P = (px, py) in Cartesian coordinates.

Cevian AP: line from A = (0,0) through P = (px, py). This line has direction (px, py) and equation py·x - px·y = 0.

This cevian meets BC at D. BC goes from B = (4,0) to C = (0,3). Parametrically: (4-4t, 3t) for t ∈ [0,1]. The cevian AP has equation y = (py/px)x (assuming px ≠ 0). So 3t = (py/px)(4-4t), giving t = 4py/(3px + 4py). D = (4·3px/(3px+4py), 3·4py/(3px+4py)) = (12px/(3px+4py), 12py/(3px+4py)).

Now, reflect line AP about line BC.

Line BC: from (4,0) to (0,3). Direction: (-4, 3). Equation: 3x + 4y = 12.

To reflect a line about another line, I can reflect two points on the line and find the reflected line.

Line AP passes through A = (0,0) and P = (px, py). It meets BC at D.

Reflecting line AP about line BC: The reflected line passes through D (since D is on BC, it's fixed by the reflection). We need to reflect one more point.

Let me reflect A = (0,0) about line BC (3x + 4y = 12).

The reflection of point (x0, y0) about line ax + by = c is:
(x0 - 2a(ax0 + by0 - c)/(a² + b²), y0 - 2b(ax0 + by0 - c)/(a² + b²))

For A = (0,0), line 3x + 4y = 12:
ax0 + by0 - c = 0 + 0 - 12 = -12
a² + b² = 9 + 16 = 25

Reflected A: (0 - 2·3·(-12)/25, 0 - 2·4·(-12)/25) = (72/25, 96/25) = (2.88, 3.84)

So the reflected line ℓ_a passes through D and A' = (72/25, 96/25).

Similarly, I need to reflect line BP about line CA, and line CP about line AB.

Line BP: from B = (4,0) through P = (px, py). Meets CA at E.
Line CA: from C = (0,3) to A = (0,0), which is the y-axis, x = 0.

E is where line BP meets x = 0. Line BP: parametrically (4 + t(px-4), t·py). At x = 0: 4 + t(px-4) = 0, t = 4/(4-px). So E = (0, 4py/(4-px)).

Reflect line BP about line CA (x = 0). The reflection of a line about the y-axis maps (x,y) to (-x,y). So the reflected line ℓ_b passes through E = (0, 4py/(4-px)) (which is on CA, so fixed) and the reflection of B = (4,0) about x = 0, which is B' = (-4, 0).

So ℓ_b passes through E = (0, 4py/(4-px)) and B' = (-4, 0).

Line CP: from C = (0,3) through P = (px, py). Meets AB at F.
Line AB: from A = (0,0) to B = (4,0), which is the x-axis, y = 0.

F is where line CP meets y = 0. Line CP: parametrically (t·px, 3 + t(py-3)). At y = 0: 3 + t(py-3) = 0, t = 3/(3-py). So F = (3px/(3-py), 0).

Reflect line CP about line AB (y = 0). The reflection maps (x,y) to (x,-y). So the reflected line ℓ_c passes through F = (3px/(3-py), 0) (on AB, fixed) and the reflection of C = (0,3) about y = 0, which is C' = (0, -3).

So ℓ_c passes through F = (3px/(3-py), 0) and C' = (0, -3).

Now, Q is the concurrency point of ℓ_a, ℓ_b, ℓ_c.

Let me find the equations of these three lines.

ℓ_a: through D = (12px/(3px+4py), 12py/(3px+4py)) and A' = (72/25, 96/25).

ℓ_b: through E = (0, 4py/(4-px)) and B' = (-4, 0).

ℓ_c: through F = (3px/(3-py), 0) and C' = (0, -3).

Let me find Q as the intersection of ℓ_b and ℓ_c, and then check that it lies on ℓ_a (which is the Neuberg cubic condition).

ℓ_b: through (0, 4py/(4-px)) and (-4, 0).
Direction: (-4, -4py/(4-px)).
Parametrically: (0 - 4t, 4py/(4-px) - 4py·t/(4-px)) = (-4t, 4py(1-t)/(4-px)).
Or in equation form: 
Slope = (0 - 4py/(4-px))/(-4 - 0) = py/(4-px)
Equation: y - 4py/(4-px) = py/(4-px) · (x - 0)
y = py/(4-px) · x + 4py/(4-px)
y = py(x + 4)/(4 - px)

ℓ_c: through (3px/(3-py), 0) and (0, -3).
Slope = (-3 - 0)/(0 - 3px/(3-py)) = -3 · (3-py)/(-3px) = (3-py)/px
Equation: y - 0 = (3-py)/px · (x - 3px/(3-py))
y = (3-py)/px · x - (3-py)/px · 3px/(3-py) = (3-py)/px · x - 3
y = (3-py)x/px - 3

Setting ℓ_b and ℓ_c equal:
py(x + 4)/(4 - px) = (3-py)x/px - 3

py·px·(x + 4) = (4-px)·((3-py)x - 3px)

py·px·x + 4·py·px = (4-px)(3-py)x - 3px(4-px)

py·px·x + 4pypx = (4-px)(3-py)x - 3px(4-px)

x[py·px - (4-px)(3-py)] = -3px(4-px) - 4pypx

Let me expand (4-px)(3-py) = 12 - 4py - 3px + px·py

py·px - (12 - 4py - 3px + px·py) = py·px - 12 + 4py + 3px - px·py = 4py + 3px - 12

So: x(4py + 3px - 12) = -3px(4-px) - 4pypx = -12px + 3px² - 4pypx = 3px² - 4pypx - 12px = px(3px - 4py - 12)

x = px(3px - 4py - 12) / (4py + 3px - 12)

Let me denote the denominator as Δ = 3px + 4py - 12. Note that 3px + 4py = 12 is the equation of line BC, so Δ = 0 means P is on BC.

x_Q = px(3px - 4py - 12) / (3px + 4py - 12)

Hmm, let me also compute y_Q from ℓ_b:
y_Q = py(x_Q + 4)/(4 - px)

x_Q + 4 = px(3px - 4py - 12)/(3px + 4py - 12) + 4
= [px(3px - 4py - 12) + 4(3px + 4py - 12)] / (3px + 4py - 12)
= [3px² - 4pxpy - 12px + 12px + 16py - 48] / (3px + 4py - 12)
= [3px² - 4pxpy + 16py - 48] / (3px + 4py - 12)
= [3px² - 4py(px - 4) - 48] / (3px + 4py - 12)

Hmm, let me try to factor. 3px² - 48 = 3(px² - 16) = 3(px-4)(px+4). And -4pxpy + 16py = -4py(px - 4).

So: 3(px-4)(px+4) - 4py(px-4) = (px-4)(3(px+4) - 4py) = (px-4)(3px + 12 - 4py)

x_Q + 4 = (px-4)(3px + 12 - 4py) / (3px + 4py - 12)

y_Q = py · (px-4)(3px + 12 - 4py) / ((4 - px)(3px + 4py - 12))
= py · (-(4-px))(3px + 12 - 4py) / ((4-px)(3px + 4py - 12))
= -py(3px + 12 - 4py) / (3px + 4py - 12)
= py(4py - 3px - 12) / (3px + 4py - 12)

So Q = (px(3px - 4py - 12)/(3px + 4py - 12), py(4py - 3px - 12)/(3px + 4py - 12))

Now, the isogonal conjugate R of P. For a triangle with vertices A, B, C and side lengths a, b, c, the isogonal conjugate in Cartesian coordinates is complex. Let me compute it using barycentric coordinates.

P in barycentrics: P = (u:v:w) where u + v + w = s, and P_cartesian = (4v/s, 3w/s). So v = s·px/4, w = s·py/3, u = s - v - w = s(1 - px/4 - py/3).

We can take u = 1 - px/4 - py/3, v = px/4, w = py/3 (setting s = 1).

Actually, let me use unnormalized: u = 12 - 3px - 4py, v = 3px, w = 4py (multiplying by 12).

R (isogonal conjugate) in barycentrics: (a²/u : b²/v : c²/w) = (25/u : 9/v : 16/w) = (25/(12-3px-4py) : 9/(3px) : 16/(4py)) = (25/(12-3px-4py) : 3/px : 4/py)

Converting to Cartesian:
R_x = 4 · v_R / (u_R + v_R + w_R) = 4 · (3/px) / (25/(12-3px-4py) + 3/px + 4/py)

Let me compute the denominator:
25/(12-3px-4py) + 3/px + 4/py

Let me denote d = 12 - 3px - 4py (note: this is related to Δ = 3px + 4py - 12 = -d).

= 25/d + 3/px + 4/py = (25pxpy + 3dpy + 4dpx) / (dpxpy)

25pxpy + 3dpy + 4dpx = 25pxpy + 3(12-3px-4py)py + 4(12-3px-4py)px
= 25pxpy + 36py - 9pxpy - 12py² + 48px - 12px² - 16pxpy
= (25 - 9 - 16)pxpy + 36py - 12py² + 48px - 12px²
= 0·pxpy + 36py - 12py² + 48px - 12px²
= -12px² + 48px - 12py² + 36py
= -12(px² - 4px + py² - 3py)
= -12(px² - 4px + 4 + py² - 3py + 9/4 - 4 - 9/4)
= -12((px-2)² + (py-3/2)² - 4 - 9/4)
= -12((px-2)² + (py-3/2)² - 25/4)

Interesting! (px-2)² + (py-3/2)² is the squared distance from P to the circumcenter O = (2, 3/2). And 25/4 = (5/2)² = R² (circumradius squared, since the circumradius is 5/2 for a 3-4-5 triangle).

So the denominator = -12(|PO|² - R²) / (dpxpy) = 12(R² - |PO|²) / (dpxpy)

R_x = 4 · (3/px) · dpxpy / (12(R² - |PO|²)) = 12dpy / (12(R² - |PO|²)) = dpy / (R² - |PO|²)

where d = 12 - 3px - 4py = -Δ.

R_x = (12 - 3px - 4py)py / (R² - |PO|²)

Similarly, R_y = 3 · w_R / (u_R + v_R + w_R) = 3 · (4/py) · dpxpy / (12(R² - |PO|²)) = 12dpx / (12(R² - |PO|²)) = dpx / (R² - |PO|²)

R_y = (12 - 3px - 4py)px / (R² - |PO|²)

So R = ((12-3px-4py)py / (R²-|PO|²), (12-3px-4py)px / (R²-|PO|²))

where R² = 25/4 and |PO|² = (px-2)² + (py-3/2)².

Let me denote D = R² - |PO|² = 25/4 - (px-2)² - (py-3/2)² and d = 12 - 3px - 4py.

R = (d·py/D, d·px/D)

Now, Q = (px(3px - 4py - 12)/(3px + 4py - 12), py(4py - 3px - 12)/(3px + 4py - 12))

Note that 3px + 4py - 12 = -d, so:

Q = (px(3px - 4py - 12)/(-d), py(4py - 3px - 12)/(-d))
= (-px(3px - 4py - 12)/d, -py(4py - 3px - 12)/d)
= (px(12 - 3px + 4py)/d, py(12 - 3px + 4py)/d)... 

wait let me redo this.

3px - 4py - 12 = -(12 - 3px + 4py). And 4py - 3px - 12 = -(12 + 3px - 4py).

Hmm, let me be more careful.

Q_x = px(3px - 4py - 12) / (3px + 4py - 12) = px(3px - 4py - 12) / (-d) = -px(3px - 4py - 12)/d = px(12 + 4py - 3px)/d

Q_y = py(4py - 3px - 12) / (3px + 4py - 12) = py(4py - 3px - 12)/(-d) = -py(4py - 3px - 12)/d = py(12 + 3px - 4py)/d

So Q = (px(12 + 4py - 3px)/d, py(12 + 3px - 4py)/d)

And R = (d·py/D, d·px/D)

And P = (px, py).

Now I need to compute QR/PQ. But first, I need to find the specific P that is on the Neuberg cubic AND has equilateral cevian triangle.

The Neuberg cubic condition is that ℓ_a also passes through Q. Let me compute that condition.

ℓ_a passes through D = (12px/(3px+4py), 12py/(3px+4py)) and A' = (72/25, 96/25).

Actually, this is getting very messy. Let me try a numerical approach. Let me pick a specific P and see if I can find one on the Neuberg cubic with equilateral cevian triangle.

Actually, let me try a completely different approach. Let me think about the problem theoretically.

Key insight: The problem asks for QR/PQ, which should be a constant. Let me see if there's a known relationship.

For the Neuberg cubic, the key property is that P, R (isogonal conjugate), and L (de Longchamps point) are collinear. Also, the reflections of the cevians are concurrent at Q.

I wonder if Q, P, R are collinear and if there's a fixed ratio.

Let me check with our formulas. Are P, Q, R collinear?

P = (px, py)
Q = (px(12 + 4py - 3px)/d, py(12 + 3px - 4py)/d) where d = 12 - 3px - 4py
R = (d·py/D, d·px/D) where D = 25/4 - (px-2)² - (py-3/2)²

For P, Q, R to be collinear, we need:
(Q_x - px)(R_y - py) = (Q_y - py)(R_x - px)

Q_x - px = px(12 + 4py - 3px)/d - px = px[(12 + 4py - 3px) - d]/d = px[(12 + 4py - 3px) - (12 - 3px - 4py)]/d = px[8py]/d = 8pxpy/d

Q_y - py = py(12 + 3px - 4py)/d - py = py[(12 + 3px - 4py) - d]/d = py[(12 + 3px - 4py) - (12 - 3px - 4py)]/d = py[6px]/d = 6pxpy/d

R_x - px = dpy/D - px = (dpy - pxD)/D
R_y - py = dpx/D - py = (dpx - pyD)/D

Collinearity: (8pxpy/d)(dpx - pyD)/D = (6pxpy/d)(dpy - pxD)/D

Simplifying (assuming pxpy ≠ 0):
8(dpx - pyD) = 6(dpy - pxD)
8dpx - 8pyD = 6dpy - 6pxD
8dpx + 6pxD = 6dpy + 8pyD
px(8d + 6D) = py(6d + 8D)
px · 2(4d + 3D) = py · 2(3d + 4D)
px(4d + 3D) = py(3d + 4D)

This is not automatically true, so P, Q, R are not always collinear. They're collinear only when px(4d + 3D) = py(3d + 4D), which is an additional condition.

Hmm, so maybe P, Q, R are not collinear in general, and the ratio QR/PQ is still a constant due to the equilateral cevian triangle condition.

This is getting very complex. Let me try a numerical approach.

Let me try to find a point P on the Neuberg cubic with equilateral cevian triangle for the 3-4-5 triangle.

Actually, let me try a simpler triangle. Let me use an isoceles triangle to reduce the number of parameters.

Let me use A = (0, h), B = (-1, 0), C = (1, 0) for some height h. By symmetry, if P is on the axis of symmetry (x = 0), then the cevian triangle might have some symmetry.

If P = (0, py) (on the axis of symmetry), then by symmetry, the cevian triangle has D on BC at (0, 0) (the midpoint), and E, F are symmetric about the y-axis. For the cevian triangle to be equilateral, we need DE = DF (automatic by symmetry) and DE = EF.

D = (0, 0) (foot of cevian from A to BC, which is the midpoint since P is on the axis).

Wait, the cevian from A through P = (0, py) hits BC (the x-axis) at (0, 0). So D = (0, 0).

E = foot of cevian from B through P on CA. 
Line BP: from B = (-1, 0) through P = (0, py). Parametrically: (-1 + t, t·py). 
Line CA: from C = (1, 0) to A = (0, h). Parametrically: (1-s, s·h).
Intersection: -1 + t = 1 - s and t·py = s·h.
From first: s = 2 - t. Substituting: t·py = (2-t)·h → t = 2h/(py + h).
E = (-1 + 2h/(py+h), 2hpy/(py+h)) = ((h-py)/(py+h), 2hpy/(py+h))

F = foot of cevian from C through P on AB.
By symmetry (since the triangle is isoceles and P is on the axis):
F = ((py-h)/(py+h), 2hpy/(py+h))... wait, let me compute.

Line CP: from C = (1, 0) through P = (0, py). Parametrically: (1-t, t·py).
Line AB: from A = (0, h) to B = (-1, 0). Parametrically: (-s, h(1-s)).
Intersection: 1-t = -s and t·py = h(1-s).
From first: s = t-1. Substituting: t·py = h(1-(t-1)) = h(2-t) → t = 2h/(py+h).
F = (1 - 2h/(py+h), 2hpy/(py+h)) = ((py-h)/(py+h), 2hpy/(py+h))

So E = ((h-py)/(h+py), 2hpy/(h+py)) and F = ((py-h)/(h+py), 2hpy/(h+py)) = (-(h-py)/(h+py), 2hpy/(h+py)).

So E and F are symmetric about the y-axis, as expected. E = (-a, b) and F = (a, b) where a = (h-py)/(h+py) and b = 2hpy/(h+py).

D = (0, 0).

DE² = a² + b² = ((h-py)/(h+py))² + (2hpy/(h+py))² = [(h-py)² + 4h²py²]/(h+py)²

EF = 2a = 2(h-py)/(h+py) (distance between E and F, which are at (-a,b) and (a,b)).

EF² = 4(h-py)²/(h+py)²

For equilateral: DE² = EF²:
(h-py)² + 4h²py² = 4(h-py)²
4h²py² = 3(h-py)²
2hpy = ±√3(h-py)

Case 1: 2hpy = √3(h-py) → 2hpy = √3h - √3py → py(2h + √3) = √3h → py = √3h/(2h + √3)

Case 2: 2hpy = -√3(h-py) → 2hpy = -√3h + √3py → py(2h - √3) = -√3h → py = -√3h/(2h - √3) = √3h/(√3 - 2h)

For Case 1 (assuming h > 0 and py > 0, and py < h for P inside the triangle):
py = √3h/(2h + √3)

For this to be inside the triangle, we need 0 < py < h:
√3h/(2h + √3) < h → √3 < 2h + √3 → 0 < 2h, which is true.
And py > 0 requires h > 0. ✓

Now, I also need P to be on the Neuberg cubic. Let me compute the Neuberg cubic for this isoceles triangle.

For the isoceles triangle A = (0, h), B = (-1, 0), C = (1, 0):
Side lengths: a = BC = 2, b = CA = √(1+h²), c = AB = √(1+h²).

Since b = c, the triangle is isoceles with b = c.

Circumcenter O: by symmetry, O is on the y-axis. O = (0, y_O).
OA = OB: h - y_O = √(1 + y_O²) → (h - y_O)² = 1 + y_O² → h² - 2hy_O + y_O² = 1 + y_O² → h² - 2hy_O = 1 → y_O = (h² - 1)/(2h)

Orthocenter H: by symmetry, H is on the y-axis. H = (0, y_H).
For a triangle with vertices (0,h), (-1,0), (1,0), the orthocenter is at (0, 1/h).
(Actually, let me verify: the altitude from A is the y-axis (x=0). The altitude from B is perpendicular to AC. AC has direction (1-0, 0-h) = (1, -h), so the altitude from B has direction (h, 1). Line through B = (-1, 0) with direction (h, 1): parametrically (-1+ht, t). At x = 0: t = 1/h, y = 1/h. So H = (0, 1/h). ✓)

De Longchamps point L = 2O - H = (0, 2(h²-1)/(2h) - 1/h) = (0, (h²-1)/h - 1/h) = (0, (h²-2)/h)

Now, P = (0, py) is on the Neuberg cubic iff P, R (isogonal conjugate of P), and L are collinear.

Since P and L are both on the y-axis, R must also be on the y-axis for collinearity. By symmetry (since the triangle is isoceles and P is on the axis), R is indeed on the y-axis. So the collinearity is automatic!

Wait, that means every point on the y-axis is on the Neuberg cubic? That can't be right...

Actually, for an isoceles triangle, the axis of symmetry is a component of many triangle cubics. Let me check: the Neuberg cubic for an isoceles triangle might contain the axis of symmetry as a component.

Hmm, actually, the Neuberg cubic is an irreducible cubic (for a general triangle). For an isoceles triangle, it might factor. Let me check.

In barycentric coordinates for our isoceles triangle (b = c):
The Neuberg cubic equation involves terms with (b² - c²) and (b² + c²). When b = c, some terms vanish.

Actually, the general Neuberg cubic equation in barycentrics is:
Σ x(y² - z²)(...) = 0

When b = c (y and z play symmetric roles), the equation might factor as (y - z) · (quadratic) = 0, where y = z is the axis of symmetry.

So for an isoceles triangle, the Neuberg cubic factors into the axis of symmetry (y = z, i.e., the median from A) and a conic. Points on the axis of symmetry are trivially on the Neuberg cubic.

This means my approach of using an isoceles triangle with P on the axis won't give a non-trivial constraint from the Neuberg cubic. The equilateral cevian triangle condition gives py = √3h/(2h + √3), but the Neuberg cubic condition is automatically satisfied.

So for any h, P = (0, √3h/(2h + √3)) is on the Neuberg cubic (trivially, being on the axis) and has an equilateral cevian triangle. 

Now I need to compute Q and R for this P and find QR/PQ. If the ratio is constant (independent of h), that's our answer.

Let me compute Q. I need to reflect the cevians about the sides and find the concurrency point.

For the isoceles triangle A = (0, h), B = (-1, 0), C = (1, 0), P = (0, py):

Cevian AP: from A = (0, h) through P = (0, py). This is the y-axis (x = 0). It meets BC (y = 0) at D = (0, 0).

Reflect line AP (x = 0) about line BC (y = 0): The reflection of the y-axis about the x-axis is still the y-axis (x = 0). So ℓ_a is the y-axis.

Cevian BP: from B = (-1, 0) through P = (0, py). Direction: (1, py). Equation: y = py(x + 1).
Meets CA at E = ((h-py)/(h+py), 2hpy/(h+py)) (computed earlier).

Reflect line BP about line CA. Line CA goes from C = (1, 0) to A = (0, h). Direction: (-1, h). Equation: hx + y = h (since at C: h·1 + 0 = h ✓, at A: h·0 + h = h ✓).

To reflect line BP about line CA, I reflect two points on BP about CA.

Point B = (-1, 0): reflect about hx + y = h.
Using the reflection formula: for line ax + by = c, reflection of (x0, y0) is (x0 - 2a(ax0+by0-c)/(a²+b²), y0 - 2b(ax0+by0-c)/(a²+b²)).
a = h, b = 1, c = h. a² + b² = h² + 1.
ax0 + by0 - c = h·(-1) + 1·0 - h = -2h.
B' = (-1 - 2h·(-2h)/(h²+1), 0 - 2·1·(-2h)/(h²+1)) = (-1 + 4h²/(h²+1), 4h/(h²+1)) = ((-h²-1+4h²)/(h²+1), 4h/(h²+1)) = ((3h²-1)/(h²+1), 4h/(h²+1))

Point E is on CA, so it's fixed by the reflection. E = ((h-py)/(h+py), 2hpy/(h+py)).

So ℓ_b passes through E and B'.

By symmetry, ℓ_c is the reflection of ℓ_b about the y-axis. So ℓ_c passes through F = (-E_x, E_y) and C' = (-B'_x, B'_y).

Q is the intersection of ℓ_a (the y-axis, x = 0), ℓ_b, and ℓ_c. By symmetry, Q is on the y-axis. So Q = (0, qy) for some qy.

To find qy, I use ℓ_b: the line through E and B', and find where it crosses x = 0.

E = ((h-py)/(h+py), 2hpy/(h+py))
B' = ((3h²-1)/(h²+1), 4h/(h²+1))

The line through E and B':
Parametrically: E + t(B' - E).
x-coordinate: E_x + t(B'_x - E_x) = 0 → t = -E_x/(B'_x - E_x) = E_x/(E_x - B'_x)

y = E_y + t(B'_y - E_y) = E_y + E_x/(E_x - B'_x) · (B'_y - E_y)
= (E_y(E_x - B'_x) + E_x(B'_y - E_y)) / (E_x - B'_x)
= (E_y·E_x - E_y·B'_x + E_x·B'_y - E_x·E_y) / (E_x - B'_x)
= (E_x·B'_y - E_y·B'_x) / (E_x - B'_x)

Let me compute this. Let me denote:
E_x = (h-py)/(h+py), E_y = 2hpy/(h+py)
B'_x = (3h²-1)/(h²+1), B'_y = 4h/(h²+1)

E_x - B'_x = (h-py)/(h+py) - (3h²-1)/(h²+1)
= [(h-py)(h²+1) - (3h²-1)(h+py)] / [(h+py)(h²+1)]

Numerator of E_x - B'_x:
(h-py)(h²+1) - (3h²-1)(h+py)
= h³ + h - pyh² - py - 3h³ - 3h²py + h + py
= h³ + h - pyh² - py - 3h³ - 3h²py + h + py
= -2h³ + 2h - 4h²py
= 2h(-h² + 1 - 2hpy)
= 2h(1 - h² - 2hpy)

E_x·B'_y - E_y·B'_x = [(h-py)/(h+py)]·[4h/(h²+1)] - [2hpy/(h+py)]·[(3h²-1)/(h²+1)]
= [4h(h-py) - 2hpy(3h²-1)] / [(h+py)(h²+1)]
= h[4(h-py) - 2py(3h²-1)] / [(h+py)(h²+1)]
= h[4h - 4py - 6h²py + 2py] / [(h+py)(h²+1)]
= h[4h - 2py - 6h²py] / [(h+py)(h²+1)]
= h[4h - 2py(1 + 3h²)] / [(h+py)(h²+1)]
= 2h[2h - py(1 + 3h²)] / [(h+py)(h²+1)]

So qy = (E_x·B'_y - E_y·B'_x) / (E_x - B'_x)
= {2h[2h - py(1 + 3h²)] / [(h+py)(h²+1)]} / {2h(1 - h² - 2hpy) / [(h+py)(h²+1)]}
= [2h - py(1 + 3h²)] / (1 - h² - 2hpy)

Now, substituting py = √3h/(2h + √3):

Let me denote s = √3 for brevity. py = sh/(2h + s).

1 + 3h² = 1 + 3h²

2h - py(1 + 3h²) = 2h - sh(1 + 3h²)/(2h + s) = h[2(2h + s) - s(1 + 3h²)]/(2h + s) = h[4h + 2s - s - 3sh²]/(2h + s) = h[4h + s - 3sh²]/(2h + s) = h[4h + s(1 - 3h²)]/(2h + s)

1 - h² - 2hpy = 1 - h² - 2h·sh/(2h + s) = [(1 - h²)(2h + s) - 2sh²]/(2h + s) = [2h + s - 2h³ - sh² - 2sh²]/(2h + s) = [2h + s - 2h³ - 3sh²]/(2h + s) = [2h(1 - h²) + s(1 - 3h²)]/(2h + s)

So qy = h[4h + s(1 - 3h²)] / [2h(1 - h²) + s(1 - 3h²)]

Hmm, let me factor. Note that 1 - 3h² = (1 - s·h)(1 + s·h) and 4h + s(1 - 3h²) = 4h + s - 3sh².

Let me try specific values of h to see if the ratio QR/PQ is constant.

Let me try h = 1 (equilateral triangle with side 2). But wait, for h = 1, the triangle A = (0,1), B = (-1,0), C = (1,0) has side lengths a = 2, b = c = √2. This is not equilateral.

Actually, for an equilateral triangle with B = (-1, 0), C = (1, 0), we need A = (0, √3). So h = √3.

But as I noted earlier, the equilateral triangle case is degenerate for the Neuberg cubic. Let me try h = 2.

h = 2, s = √3:
py = √3·2/(4 + √3) = 2√3/(4 + √3) = 2√3(4 - √3)/(16 - 3) = 2√3(4 - √3)/13 = (8√3 - 6)/13

Let me compute numerically:
√3 ≈ 1.7321
py = 2·1.7321/(4 + 1.7321) = 3.4641/5.7321 ≈ 0.6043

qy = h[4h + s(1 - 3h²)] / [2h(1 - h²) + s(1 - 3h²)]
= 2[8 + √3(1 - 12)] / [4(1 - 4) + √3(1 - 12)]
= 2[8 - 11√3] / [4(-3) + √3(-11)]
= 2[8 - 11√3] / [-12 - 11√3]
= 2(8 - 11√3) / (-(12 + 11√3))
= -2(8 - 11√3) / (12 + 11√3)
= 2(11√3 - 8) / (12 + 11√3)

Numerically: 11√3 ≈ 19.053, so 11√3 - 8 ≈ 11.053, 12 + 11√3 ≈ 31.053.
qy ≈ 2·11.053/31.053 ≈ 22.106/31.053 ≈ 0.7119

So Q = (0, 0.7119), P = (0, 0.6043).

Now I need R (isogonal conjugate of P).

For the isoceles triangle with b = c, the isogonal conjugate of P = (0, py) is on the y-axis. Let me compute it.

P in barycentrics: P = (u:v:w) where u + v + w = 1 (normalized).
P = u·A + v·B + w·C = (0, u·h) + (-v, 0) + (w, 0) = (w - v, u·h).
Since P = (0, py): w = v and u·h = py, so u = py/h, v = w = (1 - py/h)/2.

R (isogonal conjugate) = (a²/u : b²/v : c²/w) = (4/u : (1+h²)/v : (1+h²)/w).
Since v = w, R = (4/u : (1+h²)/v : (1+h²)/v), which is on the axis of symmetry. ✓

R in Cartesian: R = (0, r_y) where r_y = u_R · h / (u_R + v_R + w_R).
u_R = 4/u = 4h/py, v_R = w_R = (1+h²)/v = (1+h²)·2/(1 - py/h) = 2(1+h²)h/(h - py).

r_y = (4h/py)·h / (4h/py + 2·2(1+h²)h/(h-py))
= 4h²/py / (4h/py + 4(1+h²)h/(h-py))
= 4h²/py / [4h(1/py + (1+h²)/(h-py))]
= h/py / [1/py + (1+h²)/(h-py)]
= h/py · py(h-py) / [(h-py) + py(1+h²)]
= h(h-py) / [h - py + py + h²py]
= h(h-py) / [h + h²py]
= h(h-py) / [h(1 + hpy)]
= (h - py) / (1 + hpy)

So R = (0, (h - py)/(1 + hpy)).

For h = 2, py ≈ 0.6043:
r_y = (2 - 0.6043)/(1 + 2·0.6043) = 1.3957/(1 + 1.2086) = 1.3957/2.2086 ≈ 0.6320

So R = (0, 0.6320).

Now:
P = (0, 0.6043)
Q = (0, 0.7119)
R = (0, 0.6320)

PQ = |0.7119 - 0.6043| = 0.1076
QR = |0.7119 - 0.6320| = 0.0799

QR/PQ = 0.0799/0.1076 ≈ 0.7425

Hmm, that doesn't look like a clean ratio. Let me try another h to see if it's constant.

Let me try h = 3.
py = √3·3/(6 + √3) = 3√3/(6 + √3) = 3√3(6 - √3)/(36 - 3) = 3√3(6 - √3)/33 = √3(6 - √3)/11 = (6√3 - 3)/11

Numerically: py = (6·1.7321 - 3)/11 = (10.3926 - 3)/11 = 7.3926/11 ≈ 0.6720

qy = h[4h + s(1 - 3h²)] / [2h(1 - h²) + s(1 - 3h²)]
= 3[12 + √3(1 - 27)] / [6(1 - 9) + √3(1 - 27)]
= 3[12 - 26√3] / [6(-8) + √3(-26)]
= 3[12 - 26√3] / [-48 - 26√3]
= -3[12 - 26√3] / [48 + 26√3]
= 3[26√3 - 12] / [48 + 26√3]

Numerically: 26√3 ≈ 45.035, 26√3 - 12 ≈ 33.035, 48 + 26√3 ≈ 93.035.
qy ≈ 3·33.035/93.035 ≈ 99.105/93.035 ≈ 1.0652

R: r_y = (h - py)/(1 + hpy) = (3 - 0.6720)/(1 + 3·0.6720) = 2.328/(1 + 2.016) = 2.328/3.016 ≈ 0.7719

P = (0, 0.6720)
Q = (0, 1.0652)
R = (0, 0.7719)

PQ = 1.0652 - 0.6720 = 0.3932
QR = 1.0652 - 0.7719 = 0.2933

QR/PQ = 0.2933/0.3932 ≈ 0.7460

Hmm, 0.7425 and 0.7460 are close but not exactly equal. Let me check my calculations more carefully.

Actually, let me redo the calculations with exact values.

For h = 2, s = √3:
py = 2s/(4 + s)

qy = 2(11s - 8)/(12 + 11s)

Let me rationalize:
qy = 2(11s - 8)/(12 + 11s) · (12 - 11s)/(12 - 11s) = 2(11s - 8)(12 - 11s)/(144 - 363) = 2(11s - 8)(12 - 11s)/(-219)

(11s - 8)(12 - 11s) = 132s - 121s² - 96 + 88s = 220s - 121·3 - 96 = 220s - 363 - 96 = 220s - 459

qy = 2(220s - 459)/(-219) = -2(220s - 459)/219 = 2(459 - 220s)/219

Numerically: 220s ≈ 381.066, 459 - 381.066 = 77.934, qy = 2·77.934/219 ≈ 155.868/219 ≈ 0.7118. ✓

r_y = (h - py)/(1 + hpy) = (2 - 2s/(4+s))/(1 + 2·2s/(4+s)) = ((2(4+s) - 2s)/(4+s))/((4+s+4s)/(4+s)) = (8+2s-2s)/(4+5s) = 8/(4+5s)

Numerically: 5s ≈ 8.660, r_y = 8/(4+8.660) = 8/12.660 ≈ 0.6319. ✓

PQ = qy - py = 2(459 - 220s)/219 - 2s/(4+s)

Let me compute 2s/(4+s) = 2s(4-s)/(16-3) = 2s(4-s)/13 = (8s - 2·3)/13 = (8s - 6)/13

PQ = 2(459 - 220s)/219 - (8s - 6)/13

To combine, find common denominator. 219 = 3·73, 13 is prime. LCM = 219·13 = 2847.

PQ = [2(459 - 220s)·13 - (8s - 6)·219] / 2847
= [26(459 - 220s) - 219(8s - 6)] / 2847
= [11934 - 5720s - 1752s + 1314] / 2847
= [13248 - 7472s] / 2847

QR = qy - r_y = 2(459 - 220s)/219 - 8/(4+5s)

8/(4+5s) = 8(4-5s)/(16-75) = 8(4-5s)/(-59) = -8(4-5s)/59 = 8(5s-4)/59

QR = 2(459-220s)/219 - 8(5s-4)/59

LCM of 219 and 59: 219 = 3·73, 59 is prime. LCM = 219·59 = 12921.

QR = [2(459-220s)·59 - 8(5s-4)·219] / 12921
= [118(459-220s) - 1752(5s-4)] / 12921
= [54162 - 25960s - 8760s + 7008] / 12921
= [61170 - 34720s] / 12921

QR/PQ = [61170 - 34720s]/12921 / [13248 - 7472s]/2847
= [61170 - 34720s] · 2847 / (12921 · [13248 - 7472s])
= [61170 - 34720s] · 2847 / (12921 · [13248 - 7472s])

Note 12921 = 219·59 and 2847 = 219·13. So 2847/12921 = 13/59.

QR/PQ = 13[61170 - 34720s] / (59[13248 - 7472s])

Let me compute numerically:
61170 - 34720·1.7321 = 61170 - 60138.5 = 1031.5
13248 - 7472·1.7321 = 13248 - 12940.7 = 307.3

QR/PQ = 13·1031.5 / (59·307.3) = 13409.5 / 18130.7 ≈ 0.7397

Hmm, that's different from my earlier calculation. Let me recheck.

Wait, I think I made an arithmetic error. Let me recompute more carefully.

For h = 2, s = √3:
py = 2s/(4+s)

Let me compute py exactly:
py = 2√3/(4+√3) = 2√3(4-√3)/((4+√3)(4-√3)) = 2√3(4-√3)/(16-3) = 2√3(4-√3)/13 = (8√3 - 2·3)/13 = (8√3 - 6)/13

OK so py = (8√3 - 6)/13.

qy: I had qy = 2(11√3 - 8)/(12 + 11√3).

Let me rationalize:
qy = 2(11√3 - 8)/(12 + 11√3) · (12 - 11√3)/(12 - 11√3)
= 2(11√3 - 8)(12 - 11√3) / (144 - 121·3)
= 2(11√3 - 8)(12 - 11√3) / (144 - 363)
= 2(11√3 - 8)(12 - 11√3) / (-219)

(11√3 - 8)(12 - 11√3) = 132√3 - 121·3 - 96 + 88√3 = 220√3 - 363 - 96 = 220√3 - 459

qy = 2(220√3 - 459) / (-219) = -2(220√3 - 459)/219 = 2(459 - 220√3)/219

r_y = 8/(4 + 5√3) = 8(4 - 5√3)/(16 - 75) = 8(4 - 5√3)/(-59) = 8(5√3 - 4)/59

Now:
PQ = qy - py = 2(459 - 220√3)/219 - (8√3 - 6)/13

Common denominator: 219 = 3·73, 13. LCM = 3·73·13 = 2847.

PQ = [2(459 - 220√3)·13 - (8√3 - 6)·219] / 2847

2·13 = 26, so:
= [26(459 - 220√3) - 219(8√3 - 6)] / 2847
= [11934 - 5720√3 - 1752√3 + 1314] / 2847
= [13248 - 7472√3] / 2847

QR = qy - r_y = 2(459 - 220√3)/219 - 8(5√3 - 4)/59

Common denominator: 219 and 59. LCM = 219·59 = 12921.

= [2(459 - 220√3)·59 - 8(5√3 - 4)·219] / 12921

2·59 = 118:
= [118(459 - 220√3) - 1752(5√3 - 4)] / 12921
= [54162 - 25960√3 - 8760√3 + 7008] / 12921
= [61170 - 34720√3] / 12921

QR/PQ = [61170 - 34720√3] / 12921 · 2847 / [13248 - 7472√3]
= [61170 - 34720√3] · 2847 / (12921 · [13248 - 7472√3])

2847/12921 = 2847/12921. Let me simplify: 2847 = 13·219, 12921 = 59·219. So 2847/12921 = 13/59.

QR/PQ = 13[61170 - 34720√3] / (59[13248 - 7472√3])

Let me factor. 
61170 = 13·4705.3... no. Let me try: 61170/13 = 4705.38... not integer.
Let me try: 61170/2 = 30585, 34720/2 = 17360. 
61170/10 = 6117, 34720/10 = 3472.
GCD(61170, 34720): 61170 = 1·34720 + 26450, 34720 = 1·26450 + 8270, 26450 = 3·8270 + 1640, 8270 = 5·1640 + 70, 1640 = 23·70 + 30, 70 = 2·30 + 10, 30 = 3·10. GCD = 10.

61170 - 34720√3 = 10(6117 - 3472√3)

13248 - 7472√3: GCD(13248, 7472) = 13248 = 1·7472 + 5776, 7472 = 1·5776 + 1696, 5776 = 3·1696 + 688, 1696 = 2·688 + 320, 688 = 2·320 + 48, 320 = 6·48 + 32, 48 = 1·32 + 16, 32 = 2·16. GCD = 16.

13248 - 7472√3 = 16(828 - 467√3)

QR/PQ = 13·10(6117 - 3472√3) / (59·16(828 - 467√3))
= 130(6117 - 3472√3) / (944(828 - 467√3))
= 65(6117 - 3472√3) / (472(828 - 467√3))

Let me compute numerically:
6117 - 3472·1.7320508 = 6117 - 6013.6 = 103.4
828 - 467·1.7320508 = 828 - 808.87 = 19.13

QR/PQ = 65·103.4 / (472·19.13) = 6721 / 9029.4 ≈ 0.7442

Hmm, let me try to see if this simplifies to something. Let me compute more precisely.

√3 = 1.7320508075688772...

3472√3 = 3472 × 1.7320508075688772 = 6013.64440191...
6117 - 6013.64440191 = 103.35559809

467√3 = 467 × 1.7320508075688772 = 808.86772714...
828 - 808.86772714 = 19.13227286

QR/PQ = 65 × 103.35559809 / (472 × 19.13227286) = 6718.113876 / 9038.43363 = 0.74309...

Let me try h = 3 to compare.

For h = 3, s = √3:
py = 3s/(6+s) = 3s(6-s)/(36-3) = 3s(6-s)/33 = s(6-s)/11 = (6s-3)/11

qy = 3(26s - 12)/(48 + 26s)

r_y = (3 - py)/(1 + 3py) = (3 - (6s-3)/11)/(1 + 3(6s-3)/11) = ((33 - 6s + 3)/11)/((11 + 18s - 9)/11) = (36 - 6s)/(2 + 18s) = 6(6-s)/(2(1+9s)) = 3(6-s)/(1+9s)

Let me compute:
py = (6√3 - 3)/11 ≈ (10.392 - 3)/11 = 7.392/11 ≈ 0.6720

qy = 3(26√3 - 12)/(48 + 26√3) ≈ 3(45.033 - 12)/(48 + 45.033) = 3·33.033/93.033 = 99.1/93.033 ≈ 1.0652

r_y = 3(6 - √3)/(1 + 9√3) ≈ 3·4.268/(1 + 15.588) = 12.804/16.588 ≈ 0.7719

PQ = qy - py ≈ 1.0652 - 0.6720 = 0.3932
QR = qy - r_y ≈ 1.0652 - 0.7719 = 0.2933

QR/PQ ≈ 0.2933/0.3932 ≈ 0.7460

So for h=2: QR/PQ ≈ 0.7431
For h=3: QR/PQ ≈ 0.7460

These are close but not equal. This suggests either:
1. My interpretation of Q is wrong, or
2. The ratio is not constant (which contradicts the problem asking to "find the ratio"), or
3. I'm making computational errors.

Let me double-check my formula for Q.

Actually, wait. Let me reconsider the problem. Maybe "reflections of P about the sides" means the reflections of the point P (not the cevians) over the sides, and "point of concurrency" means the point where the lines from the vertices to these reflected points concur.

So:
- P_a = reflection of P over BC
- P_b = reflection of P over CA
- P_c = reflection of P over AB
- Q = concurrence of lines AP_a, BP_b, CP_c

Let me try this interpretation.

For the isoceles triangle A = (0, h), B = (-1, 0), C = (1, 0), P = (0, py):

P_a = reflection of P = (0, py) over BC (y = 0) = (0, -py)
P_b = reflection of P over CA (hx + y = h)
P_c = reflection of P over AB (hx - y = h)... wait, let me get the equations right.

CA: from C = (1, 0) to A = (0, h). Equation: hx + y = h (verified earlier).
AB: from A = (0, h) to B = (-1, 0). Direction: (-1, -h). Equation: hx - y = ... at A: h·0 - h = -h. At B: h·(-1) - 0 = -h. So equation: hx - y = -h, or y = hx + h.

P_b = reflection of (0, py) over hx + y = h:
a = h, b = 1, c = h. a² + b² = h² + 1.
ax0 + by0 - c = 0 + py - h = py - h.
P_b = (0 - 2h(py-h)/(h²+1), py - 2(py-h)/(h²+1)) = (-2h(py-h)/(h²+1), py - 2(py-h)/(h²+1))
= (2h(h-py)/(h²+1), (py(h²+1) - 2(py-h))/(h²+1))
= (2h(h-py)/(h²+1), (pyh² + py - 2py + 2h)/(h²+1))
= (2h(h-py)/(h²+1), (pyh² - py + 2h)/(h²+1))
= (2h(h-py)/(h²+1), (py(h²-1) + 2h)/(h²+1))

P_c = reflection of (0, py) over y = hx + h, i.e., hx - y = -h, or -hx + y = h.
a = -h, b = 1, c = h. a² + b² = h² + 1.
ax0 + by0 - c = 0 + py - h = py - h.
P_c = (0 - 2(-h)(py-h)/(h²+1), py - 2(py-h)/(h²+1)) = (2h(py-h)/(h²+1), (py(h²-1)+2h)/(h²+1))
= (-2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1))

By symmetry, P_c = (-P_b_x, P_b_y). ✓

Now, lines AP_a, BP_b, CP_c:

AP_a: from A = (0, h) to P_a = (0, -py). This is the y-axis (x = 0).

BP_b: from B = (-1, 0) to P_b = (2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1)).

CP_c: from C = (1, 0) to P_c = (-2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1)).

By symmetry, Q is on the y-axis. Q = (0, qy).

From line BP_b: 
B = (-1, 0), P_b = (2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1))

Direction: (2h(h-py)/(h²+1) + 1, (py(h²-1)+2h)/(h²+1))
= ((2h(h-py) + h²+1)/(h²+1), (py(h²-1)+2h)/(h²+1))

Parametrically: (-1 + t(2h(h-py)+h²+1)/(h²+1), t(py(h²-1)+2h)/(h²+1))

At x = 0: -1 + t(2h(h-py)+h²+1)/(h²+1) = 0
t = (h²+1)/(2h(h-py)+h²+1)

qy = t(py(h²-1)+2h)/(h²+1) = (py(h²-1)+2h)/(2h(h-py)+h²+1)

So Q = (0, (py(h²-1)+2h)/(2h(h-py)+h²+1))

Let me compute for h = 2, py = (8√3-6)/13:

py(h²-1)+2h = py·3 + 4 = 3(8√3-6)/13 + 4 = (24√3-18+52)/13 = (24√3+34)/13

2h(h-py)+h²+1 = 4(2-py)+5 = 4(2-(8√3-6)/13)+5 = 4(26-8√3+6)/13+5 = 4(32-8√3)/13+5 = (128-32√3)/13+5 = (128-32√3+65)/13 = (193-32√3)/13

qy = (24√3+34)/(193-32√3)

Numerically: 24√3 ≈ 41.569, 24√3+34 ≈ 75.569, 32√3 ≈ 55.426, 193-32√3 ≈ 137.574.
qy ≈ 75.569/137.574 ≈ 0.5493

So Q = (0, 0.5493), P = (0, 0.6043), R = (0, 0.6319).

PQ = |0.5493 - 0.6043| = 0.0550
QR = |0.5493 - 0.6319| = 0.0826

QR/PQ = 0.0826/0.0550 = 1.502

Hmm, that's approximately 3/2! Let me check with h = 3.

For h = 3, py = (6√3-3)/11:

py(h²-1)+2h = py·8 + 6 = 8(6√3-3)/11 + 6 = (48√3-24+66)/11 = (48√3+42)/11

2h(h-py)+h²+1 = 6(3-py)+10 = 6(3-(6√3-3)/11)+10 = 6(33-6√3+3)/11+10 = 6(36-6√3)/11+10 = (216-36√3)/11+10 = (216-36√3+110)/11 = (326-36√3)/11

qy = (48√3+42)/(326-36√3)

Numerically: 48√3 ≈ 83.138, 48√3+42 ≈ 125.138, 36√3 ≈ 62.354, 326-36√3 ≈ 263.646.
qy ≈ 125.138/263.646 ≈ 0.4747

P = (0, 0.6720), Q = (0, 0.4747), R = (0, 0.7719).

PQ = |0.4747 - 0.6720| = 0.1973
QR = |0.4747 - 0.7719| = 0.2972

QR/PQ = 0.2972/0.1973 ≈ 1.506

So for h=2: QR/PQ ≈ 1.502, for h=3: QR/PQ ≈ 1.506. These are close to 3/2 but not exactly equal. The small discrepancy might be due to rounding. Let me check more precisely.

For h = 2:
qy = (24√3+34)/(193-32√3)
py = (8√3-6)/13
r_y = 8(5√3-4)/59

PQ = py - qy (since py > qy)
= (8√3-6)/13 - (24√3+34)/(193-32√3)

Common denominator: 13(193-32√3)

= [(8√3-6)(193-32√3) - 13(24√3+34)] / [13(193-32√3)]

(8√3-6)(193-32√3) = 8·193√3 - 8·32·3 - 6·193 + 6·32√3 = 1544√3 - 768 - 1158 + 192√3 = 1736√3 - 1926

13(24√3+34) = 312√3 + 442

Numerator: 1736√3 - 1926 - 312√3 - 442 = 1424√3 - 2368

PQ = (1424√3 - 2368) / [13(193-32√3)]

QR = r_y - qy (since r_y > qy)
= 8(5√3-4)/59 - (24√3+34)/(193-32√3)

Common denominator: 59(193-32√3)

= [8(5√3-4)(193-32√3) - 59(24√3+34)] / [59(193-32√3)]

(5√3-4)(193-32√3) = 5·193√3 - 5·32·3 - 4·193 + 4·32√3 = 965√3 - 480 - 772 + 128√3 = 1093√3 - 1252

8(1093√3 - 1252) = 8744√3 - 10016

59(24√3+34) = 1416√3 + 2006

Numerator: 8744√3 - 10016 - 1416√3 - 2006 = 7328√3 - 12022

QR = (7328√3 - 12022) / [59(193-32√3)]

QR/PQ = (7328√3 - 12022) / [59(193-32√3)] · [13(193-32√3)] / (1424√3 - 2368)
= 13(7328√3 - 12022) / [59(1424√3 - 2368)]

Let me factor:
7328 = 16·458 = 16·2·229 = 32·229
12022 = 2·6011
1424 = 16·89
2368 = 32·74 = 32·2·37

7328√3 - 12022 = 2(3664√3 - 6011)
1424√3 - 2368 = 16(89√3 - 148)

QR/PQ = 13·2(3664√3 - 6011) / [59·16(89√3 - 148)]
= 26(3664√3 - 6011) / [944(89√3 - 148)]
= 13(3664√3 - 6011) / [472(89√3 - 148)]

Let me check if 3664√3 - 6011 = k(89√3 - 148        — AI历史解题过程（thinking）
#   oda_math_460k_00032695         — 题目ID

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
  <problem_id>oda_math_460k_00032695</problem_id>
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

Suppose $f(x) = 3x-2$ and $g(x) = 4x+5$. Calculate $g(f(x))$.

## Standard Solution

<think>Okay, let's see. The problem is to calculate g(f(x)) where f(x) is 3x - 2 and g(x) is 4x + 5. Hmm, so first, I need to remember what function composition is. Function composition means that we substitute the entire function f(x) into the function g. So g(f(x)) is like taking g of whatever f(x) is. 

Let me start by writing down what f(x) is. f(x) = 3x - 2. Then, g(x) is 4x + 5. So when we do g(f(x)), we need to replace every x in the g function with f(x). That is, wherever there's an x in g(x), we put (3x - 2) instead. 

Let me write that out. g(f(x)) = g(3x - 2). Now, since g(x) is 4x + 5, replacing x with (3x - 2) gives us 4*(3x - 2) + 5. Let me compute that step by step. First, distribute the 4 into the parentheses: 4*3x is 12x, and 4*(-2) is -8. So that part becomes 12x - 8. Then we add the 5. So 12x - 8 + 5. Combining like terms, -8 + 5 is -3. So the entire expression simplifies to 12x - 3. 

Let me check that again to make sure I didn't make a mistake. Starting with g(f(x)): substitute f(x) into g. So g takes an input, multiplies by 4, then adds 5. The input here is f(x) which is 3x - 2. So 4*(3x - 2) + 5. Multiply 4 by 3x: 12x. 4 times -2 is -8. Then +5. So 12x -8 +5. Combine constants: -8 +5 is -3. So 12x -3. That seems right. I think that's the answer.
</think>

To calculate \( g(f(x)) \), we need to substitute \( f(x) \) into the function \( g(x) \). 

Given:
- \( f(x) = 3x - 2 \)
- \( g(x) = 4x + 5 \)

First, substitute \( f(x) \) into \( g(x) \):
\[
g(f(x)) = g(3x - 2)
\]

Next, replace \( x \) in \( g(x) \) with \( 3x - 2 \):
\[
g(3x - 2) = 4(3x - 2) + 5
\]

Simplify the expression:
\[
4(3x - 2) + 5 = 12x - 8 + 5 = 12x - 3
\]

Thus, the final answer is \(\boxed{12x - 3}\).

## AI's Thinking (Attempted Solution Process)

The problem asks about a point P on the Neuberg cubic of triangle ABC such that the cevian triangle of P is equilateral. Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC. If R is the isogonal conjugate of P, find the ratio QR/PQ.

Let me think about this carefully.

First, let me recall the relevant facts:

1. **Neuberg cubic**: The Neuberg cubic is the locus of points P such that the reflections of P over the sides of triangle ABC are collinear. Wait, actually let me reconsider. The Neuberg cubic is the isogonal pivotal cubic with pivot at the point... Actually, the Neuberg cubic is the locus of points P such that the cevian triangle of P is in perspective with triangle ABC... no.

Let me recall more carefully. The Neuberg cubic is a famous cubic curve. One characterization: P is on the Neuberg cubic if and only if the reflections of P over the sides of BC, CA, AB are collinear with the isogonal conjugate of P... no.

Actually, the Neuberg cubic has several characterizations:
- It's the locus of P such that the reflections of P in the sides of ABC are collinear. Wait, that's not quite right either.

Let me think again. The Neuberg cubic K001 (in Bernard Gibert's catalog) is the isogonal cubic with pivot at the de Longchamps point. 

Key property: P is on the Neuberg cubic if and only if the reflections of P over the sidelines of ABC are collinear. The line through these three reflections is called the "orthic axis" or related to it.

Actually, I think the correct statement is: P lies on the Neuberg cubic if and only if the reflections of P in the three sides of triangle ABC are collinear. And the line containing them passes through the isogonal conjugate of P.

Wait, let me be more precise. The Neuberg cubic is the locus of points P such that the reflections of P in the sides of BC, CA, AB are collinear. The line on which these reflections lie passes through the isogonal conjugate P* of P.

Hmm, actually I recall that the key property is: if P is on the Neuberg cubic, then the reflections of P over the sides of the triangle are collinear, and this line passes through the isogonal conjugate of P.

So if R is the isogonal conjugate of P, then R lies on the line containing the three reflections of P.

Now, Q is defined as "the point of concurrency of the reflections of P about the sides of triangle ABC." 

Wait, this is confusing. If the reflections are collinear (on the Neuberg cubic), they don't have a "point of concurrency." Unless "reflections of P about the sides" means something different—like reflecting the cevians, or reflecting lines.

Let me re-read: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

Hmm, maybe "reflections of P about the sides" refers to the lines obtained by reflecting the cevians AP, BP, CP about the sides? Or maybe it refers to reflecting the lines PA, PB, PC?

Actually, I think there might be a different interpretation. Let me reconsider.

Actually, wait. Let me reconsider the problem. Perhaps the "reflections of P about the sides" are three points (the reflections of P over each side), and "point of concurrency" doesn't make sense for three points unless they're collinear (and then there's no concurrency point).

Let me think about this differently. Maybe Q is defined differently. Perhaps "the reflections of P about the sides" means the reflection lines—i.e., for each side, we reflect P over that side to get a point, and then... no.

Actually, I wonder if the problem means: reflect the cevians of P over the sides. The cevian from A through P hits BC at some point D. Reflect the line AD (or the cevian) over the perpendicular bisector... no, reflect over the side BC.

Actually, let me reconsider. In the context of the Neuberg cubic, there's a well-known construction. Let me think about what "reflections of P about the sides" could mean in terms of cevians.

Hmm, actually maybe the problem is using "reflections of P about the sides" to mean the reflections of the point P over each side, giving three points P_a, P_b, P_c. On the Neuberg cubic, these are collinear. But the problem says "point of concurrency," which suggests lines, not points.

Let me reconsider: maybe "reflections of P about the sides" means: for each vertex, reflect the cevian line. Specifically:
- The cevian from A to P meets BC at D. Reflect line AD over line BC (or over the angle bisector at A?)...

Actually, I think the most natural reading might be different. Let me consider: "the reflections of P about the sides of triangle ABC" could mean the lines obtained by reflecting AP over side BC, BP over side CA, CP over side AB. But that's a bit unusual.

Alternatively, maybe it's: reflect the lines PA, PB, PC about the sides BC, CA, AB respectively. These three reflected lines might be concurrent, and that concurrency point is Q.

Actually, wait. I think I recall now. There's a classical result related to the Neuberg cubic:

The Neuberg cubic is the locus of P such that if you reflect the cevians AP, BP, CP over the sides BC, CA, AB respectively, the three reflected lines are concurrent. And this concurrency point is related to the isogonal conjugate.

Hmm, but that doesn't sound right either, because reflecting a cevian over the opposite side is a specific operation.

Let me think about this more carefully.

Actually, I think the correct characterization of the Neuberg cubic involves the following: P is on the Neuberg cubic if and only if the reflections of the lines AP, BP, CP in the sides BC, CA, AB respectively are concurrent.

Wait, I think I'm overcomplicating this. Let me look at this from a different angle.

The Neuberg cubic has the property that it's the locus of P such that the cevian triangle of P is in perspective with the reflection triangle... or something like that.

Actually, let me think about what's known:

The Neuberg cubic K001 is characterized by: P is on K001 iff the reflections of P over the sides of ABC are collinear. The line through these reflections is called the "orthic axis" of P (or the "anti-pedal line"). This line passes through the isogonal conjugate P* of P.

So if R = P* (isogonal conjugate), then R lies on the line through the three reflections of P.

Now, the problem says Q is "the point of concurrency of the reflections of P about the sides." If the reflections are three points that are collinear, there's no "point of concurrency." So maybe the problem means something else by "reflections."

Let me re-read the problem once more: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

Hmm, maybe "reflections of P about the sides" means the three lines, each being the perpendicular from P to a side, reflected... no.

Actually, I think there might be a different interpretation. In some formulations, "the reflection of P about side BC" could refer to the line that is the reflection of line AP about line BC. But that's unusual.

Wait, actually, I think the problem might be referring to the following: reflect the cevian lines. The cevian from A through P is line AP. Reflect this line about side BC. Similarly reflect BP about CA and CP about AB. These three reflected lines are concurrent when P is on the Neuberg cubic, and the point of concurrency is Q.

Actually no, I don't think that's the standard characterization.

Let me try yet another interpretation. Perhaps "reflections of P about the sides" means: take the reflection of P over each side, getting three points. Then "point of concurrency" refers to the cevians from the vertices to these reflected points. Specifically:
- Reflect P over BC to get P_a
- Reflect P over CA to get P_b  
- Reflect P over AB to get P_c
- Lines AP_a, BP_b, CP_c are concurrent at Q.

This would make more sense with "point of concurrency." And on the Neuberg cubic, these lines would indeed be concurrent.

Hmm, but I'm not sure this is a known property.

Actually, let me think about this differently. Let me consider the possibility that the problem is well-posed and that the answer is a clean ratio.

Let me consider the special case where the cevian triangle of P is equilateral. This is a very specific condition.

The cevian triangle of P is the triangle formed by the feet of the cevians from P to the sides. If P has barycentric coordinates (x:y:z), the cevian triangle has vertices at (0:y:z), (x:0:z), (x:y:0) on the sides BC, CA, AB respectively.

For the cevian triangle to be equilateral is a strong condition.

Now, let me think about what's special about the Neuberg cubic and equilateral cevian triangles.

Actually, I recall that there's a connection between the Neuberg cubic and equilateral triangles. The Neuberg cubic passes through the vertices of the two equilateral triangles erected on the sides of ABC (the Napoleon triangles related points).

Let me think about specific points on the Neuberg cubic where the cevian triangle is equilateral.

Hmm, this is getting complicated. Let me try to think about this more carefully using coordinates.

Let me set up coordinates. Let me use a specific triangle to compute, since the ratio might be universal (independent of the triangle).

Actually, wait. The problem says "find the ratio QR/PQ," implying it's a fixed number. So it should be independent of the triangle and the specific point P (as long as the conditions are met).

Let me try to use a specific triangle and specific point P.

Let me consider the equilateral triangle ABC first. If ABC is equilateral, then by symmetry, the Neuberg cubic has special properties. But for an equilateral triangle, many things degenerate.

Let me try a different approach. Let me use a right triangle or a specific triangle where I can compute.

Actually, let me think about this more carefully from the theory.

The Neuberg cubic is the isogonal cubic with pivot at the de Longchamps point L. This means:
- If P is on the cubic, then its isogonal conjugate R is also on the cubic.
- The line PR passes through the pivot L (de Longchamps point).

Wait, that's the definition of an isogonal cubic with pivot: P is on the cubic iff P, its isogonal conjugate P*, and the pivot are collinear.

So for the Neuberg cubic: P, R (= isogonal conjugate of P), and L (de Longchamps point) are collinear.

Now, the de Longchamps point L is the reflection of the orthocenter H over the circumcenter O. So L = 2O - H.

Now, the problem also involves Q, the point of concurrency of the reflections of P about the sides.

Let me reconsider what "reflections of P about the sides" means. I think the most standard interpretation in the context of the Neuberg cubic is:

The reflections of P over the three sides are three points, and on the Neuberg cubic, these three points are collinear. The line through them passes through R (the isogonal conjugate).

But the problem says "point of concurrency," not "line of collinearity." So maybe the problem is using a different definition.

Let me consider another possibility: maybe "reflections of P about the sides" means reflecting the cevians. Specifically:
- Cevian AP meets BC at D. Reflect the cevian line AD about side BC to get a line through D.
- Similarly for the other two cevians.
- These three reflected lines are concurrent at Q.

This interpretation would give a "point of concurrency."

Actually, I think I recall now. There's a theorem that says: P is on the Neuberg cubic if and only if the reflections of the cevians AP, BP, CP in the sides BC, CA, AB are concurrent. And the point of concurrency Q, the isogonal conjugate R, and P have a specific relationship.

Let me think about this. If we reflect line AP about side BC, we get a line through D (where D is the foot of the cevian on BC). The reflection of line AP about line BC...

Hmm, actually, reflecting a line about another line: if line AP makes angle α with BC, the reflected line makes angle -α with BC, passing through D.

Let me try to work this out with coordinates.

Let me use a specific triangle. Let me take A = (0, 3), B = (-2, 0), C = (2, 0). This is an isoceles triangle.

Actually, let me try a more systematic approach. Let me use barycentric coordinates.

In barycentric coordinates, P = (u : v : w). The cevian triangle of P has vertices:
- D = (0 : v : w) on BC
- E = (u : 0 : w) on CA  
- F = (u : v : 0) on AB

For the Neuberg cubic in barycentric coordinates, the equation is:
∑ u(v² - w²)(something) = 0

Actually, the Neuberg cubic equation in barycentrics is:
∑ x(y² - z²)(x²(y² + z²) - y²z² - ... ) 

This is getting complicated. Let me try a computational approach with a specific triangle.

Let me use the triangle with A = (0, 4), B = (-3, 0), C = (3, 0).

Hmm, let me think about this differently. Let me consider the possibility that the answer is 2.

Actually, let me think about what's known about the relationship between P, Q, and R on the Neuberg cubic.

If the Neuberg cubic is the locus where the reflections of P over the sides are collinear, and this line passes through R, then maybe Q is defined differently.

Let me re-read the problem: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

OK here's another interpretation: "the reflections of P about the sides" could be three lines (not points). For each side, we can consider the line connecting P to its reflection over that side. This line is perpendicular to the side and passes through the midpoint of P and its reflection (which is on the side). So these three lines are the perpendiculars from P to the three sides. These are generally not concurrent (they all pass through P, actually—wait, no).

Hmm, the line connecting P to its reflection over side BC is perpendicular to BC and passes through P. So all three such lines pass through P. That's trivially concurrent at P, which doesn't give useful information.

Let me try yet another interpretation. Maybe "reflections of P about the sides" means: for each side, consider the line that is the reflection of the opposite cevian about that side. 

- Reflect cevian AP (or line AP) about side BC → get line ℓ_a
- Reflect cevian BP about side CA → get line ℓ_b  
- Reflect cevian CP about side AB → get line ℓ_c
- Q = concurrency point of ℓ_a, ℓ_b, ℓ_c

This makes sense with "point of concurrency" and is related to the Neuberg cubic.

Actually, I now recall more clearly. The Neuberg cubic can be characterized as follows:

P is on the Neuberg cubic if and only if the reflections of the lines AP, BP, CP in the sides BC, CA, AB respectively are concurrent.

The point of concurrency is sometimes denoted Q, and there's a relationship between P, Q, and the isogonal conjugate R of P.

Let me try to verify this and find the ratio.

Let me work with a specific example. Let me use the triangle A = (0, 3), B = (-2, 0), C = (2, 0), and find a point P on the Neuberg cubic with equilateral cevian triangle.

Actually, this is getting very complicated computationally. Let me think about whether there's a more theoretical approach.

Let me consider the key relationships:

1. P is on the Neuberg cubic → reflections of cevians AP, BP, CP over sides BC, CA, AB are concurrent at Q.
2. R = isogonal conjugate of P.
3. The cevian triangle of P is equilateral.

For the Neuberg cubic, there's a known result: the point of concurrency Q of the reflected cevians, the point P, and the isogonal conjugate R are collinear, and there's a specific ratio.

Actually, I think the key result might be: Q, P, R are collinear and Q is the reflection of R over P, or something like that, giving QR/PQ = 2.

Or maybe the relationship is that P is the midpoint of QR, giving QR/PQ = 2... no, if P is the midpoint of QR, then PQ = PR and QR = 2PQ, so QR/PQ = 2.

Alternatively, maybe R is the midpoint of PQ, giving QR/PQ = 1.

Or maybe Q = R, giving QR/PQ = 0, but that seems too trivial.

Let me think about this more carefully.

Actually, I recall that for the Neuberg cubic, there's a result involving the "anti-complementary triangle" or the "cevian conic." 

Let me try a different approach. Let me think about the specific case where the cevian triangle is equilateral and see what constraints this imposes.

The cevian triangle of P = (u:v:w) has vertices D = (0:v:w), E = (u:0:w), F = (u:v:0).

For this to be equilateral, we need DE = EF = FD.

In barycentric coordinates, the distance between two points involves the side lengths of the triangle. This is complex.

Let me try a very specific approach. Let me use an equilateral triangle ABC and see what happens.

If ABC is equilateral with side length s, then by symmetry, the Neuberg cubic has nice properties. For an equilateral triangle, the isogonal conjugate of P = (u:v:w) is R = (a²/u : b²/v : c²/w) = (1/u : 1/v : 1/w) since a = b = c.

For an equilateral triangle, the Neuberg cubic... actually, for an equilateral triangle, many cubics degenerate because of the high symmetry. The de Longchamps point coincides with the circumcenter and orthocenter (they're all the same point for an equilateral triangle). So the Neuberg cubic, being the isogonal cubic with pivot at the de Longchamps point (= circumcenter = orthocenter = centroid), might degenerate.

Actually, for an equilateral triangle, O = H = G = L, so the isogonal cubic with pivot at L would be the set of P such that P, P*, and L are collinear. Since L is the centroid (1:1:1), this is the condition that (u:v:w), (1/u:1/v:1/w), and (1:1:1) are collinear.

The collinearity condition is:
| u   v   w  |
| 1/u 1/v 1/w| = 0
| 1   1   1  |

Expanding: u(1/v - 1/w) - v(1/u - 1/w) + w(1/u - 1/v) = 0
= u(w-v)/(vw) - v(w-u)/(uw) + w(v-u)/(uv) = 0
= [u²(w-v) - v²(w-u) + w²(v-u)] / (uvw) = 0

Numerator: u²w - u²v - v²w + v²u + w²v - w²u
= u²(w-v) + v²(u-w) + w²(v-u)
= u²(w-v) - v²(w-u) + w²(v-u)

Let me factor: = (u-v)(v-w)(w-u) ... let me check.

Actually, u²(w-v) + v²(u-w) + w²(v-u) is a well-known expression that equals -(u-v)(v-w)(w-u).

Let me verify: (u-v)(v-w)(w-u) = (u-v)(vw - vu - w² + wu) = (u-v)(vw - vu - w² + wu)
= uvw - vu² - uw² + u²w - v²w + v²u + vw² - vuw
= -vu² - uw² + u²w - v²w + v²u + vw²
= u²w - u²v + v²u - v²w + vw² - uw²
= u²(w-v) + v²(u-w) + w²(v-u) ✓

So the Neuberg cubic for an equilateral triangle is (u-v)(v-w)(w-u) = 0, which is the union of the three medians. This is degenerate, so the equilateral triangle case won't work well.

Let me try a different triangle. Let me use a right triangle.

Let me use A = (0, 0), B = (4, 0), C = (0, 3). This is a 3-4-5 right triangle with the right angle at A.

Side lengths: a = BC = 5, b = CA = 3, c = AB = 4.

For this triangle:
- O (circumcenter) = midpoint of BC = (2, 3/2)
- H (orthocenter) = A = (0, 0) (since it's a right triangle at A)
- L (de Longchamps point) = 2O - H = (4, 3)

The Neuberg cubic is the locus of P such that P, R (isogonal conjugate of P), and L are collinear.

In barycentric coordinates, the isogonal conjugate of P = (u:v:w) is R = (a²/u : b²/v : c²/w) = (25/u : 9/v : 16/w).

L (de Longchamps point) in barycentric coordinates: L = 2O - H. 

O in barycentrics = (sin 2A : sin 2B : sin 2C). For our triangle:
- A = 90°, B = arctan(3/4), C = arctan(4/3)
- sin 2A = sin 180° = 0
- sin 2B = 2 sin B cos B = 2 · (3/5) · (4/5) = 24/25
- sin 2C = 2 sin C cos C = 2 · (4/5) · (3/5) = 24/25

So O = (0 : 24/25 : 24/25) = (0 : 1 : 1). This makes sense—O is the midpoint of BC.

H = A = (1 : 0 : 0) in barycentrics.

L = 2O - H. In barycentric coordinates, we can't simply do 2O - H because barycentric coordinates are homogeneous. We need to convert to Cartesian, compute, then convert back.

O = (2, 3/2) in Cartesian, H = (0, 0), L = (4, 3).

Converting L = (4, 3) to barycentrics: 
L = αA + βB + γC where α + β + γ = 1
4 = 0·α + 4·β + 0·γ → β = 1
3 = 0·α + 0·β + 3·γ → γ = 1
α = 1 - β - γ = 1 - 1 - 1 = -1

So L = (-1 : 1 : 1) in barycentrics.

The Neuberg cubic condition: P = (u:v:w), R = (25/u : 9/v : 16/w), L = (-1:1:1) are collinear.

Collinearity:
| u    v    w   |
| 25/u 9/v 16/w| = 0
| -1   1    1   |

Expanding:
u(9/v · 1 - 16/w · 1) - v(25/u · 1 - 16/w · (-1)) + w(25/u · 1 - 9/v · (-1)) = 0

= u(9/v - 16/w) - v(25/u + 16/w) + w(25/u + 9/v) = 0

= 9u/v - 16u/w - 25v/u - 16v/w + 25w/u + 9w/v = 0

Multiply by uvw:
9u²w - 16u²v - 25v²w - 16v²u + 25w²u + 9w²v = 0

Rearranging:
9u²w - 16u²v - 16v²u - 25v²w + 25w²u + 9w²v = 0

This is the equation of the Neuberg cubic for our triangle.

Now, I also need the condition that the cevian triangle of P is equilateral. The cevian triangle has vertices:
- D = (0 : v : w) on BC
- E = (u : 0 : w) on CA
- F = (u : v : 0) on AB

I need to compute the side lengths of triangle DEF and set them equal.

This is getting quite involved. Let me try to use Cartesian coordinates.

A = (0,0), B = (4,0), C = (0,3).

P = (u:v:w) in barycentrics → Cartesian: P = (u·A + v·B + w·C)/(u+v+w) = (4v/(u+v+w), 3w/(u+v+w)).

Let me set s = u+v+w and use normalized barycentrics. P = (4v/s, 3w/s).

D = (0:v:w) → Cartesian: (4v/(v+w), 3w/(v+w))
E = (u:0:w) → Cartesian: (0, 3w/(u+w))... wait, E = (u:0:w) means E = (u·A + 0·B + w·C)/(u+w) = (0, 3w/(u+w)). Hmm, that's on CA (the y-axis from (0,0) to (0,3)).

F = (u:v:0) → Cartesian: (4v/(u+v), 0). This is on AB (the x-axis from (0,0) to (4,0)).

So:
D = (4v/(v+w), 3w/(v+w))
E = (0, 3w/(u+w))
F = (4v/(u+v), 0)

Now I need DE = EF = FD.

DE² = (4v/(v+w))² + (3w/(v+w) - 3w/(u+w))²
= 16v²/(v+w)² + 9w²(1/(v+w) - 1/(u+w))²
= 16v²/(v+w)² + 9w²((u+w-v-w)/((v+w)(u+w)))²
= 16v²/(v+w)² + 9w²(u-v)²/((v+w)²(u+w)²)
= [16v²(u+w)² + 9w²(u-v)²] / ((v+w)²(u+w)²)

EF² = (4v/(u+v))² + (3w/(u+w))²
= 16v²/(u+v)² + 9w²/(u+w)²

FD² = (4v/(v+w) - 4v/(u+v))² + (3w/(v+w))²
= 16v²(1/(v+w) - 1/(u+v))² + 9w²/(v+w)²
= 16v²((u+v-v-w)/((v+w)(u+v)))² + 9w²/(v+w)²
= 16v²(u-w)²/((v+w)²(u+v)²) + 9w²/(v+w)²
= [16v²(u-w)² + 9w²(u+v)²] / ((v+w)²(u+v)²)

Setting DE² = EF²:
[16v²(u+w)² + 9w²(u-v)²] / ((v+w)²(u+w)²) = [16v²(u+w)² + 9w²(u+v)²] / ((u+v)²(u+w)²)

Wait, let me redo EF²:
EF² = (4v/(u+v) - 0)² + (0 - 3w/(u+w))² = 16v²/(u+v)² + 9w²/(u+w)²

So EF² = [16v²(u+w)² + 9w²(u+v)²] / ((u+v)²(u+w)²)

Setting DE² = EF²:
[16v²(u+w)² + 9w²(u-v)²] / ((v+w)²(u+w)²) = [16v²(u+w)² + 9w²(u+v)²] / ((u+v)²(u+w)²)

Cancel (u+w)²:
[16v²(u+w)² + 9w²(u-v)²] / (v+w)² = [16v²(u+w)² + 9w²(u+v)²] / (u+v)²

This is getting very messy. Let me try a different approach—maybe use numerical computation.

Actually, let me try to think about this problem more cleverly.

The condition that the cevian triangle is equilateral is very restrictive. For a given triangle ABC, there are only finitely many points P on the Neuberg cubic with equilateral cevian triangle.

Let me think about what special points on the Neuberg cubic might have equilateral cevian triangles.

Actually, I recall that the two isodynamic points are on the Neuberg cubic. The isodynamic points are related to equilateral triangles. Let me check if the cevian triangle of an isodynamic point is equilateral.

The isodynamic points are the points from which the triangle subtends equal angles (120° each for the first isodynamic point). They are the isogonal conjugates of the Fermat points.

The first Fermat point (isogonal conjugate of the first isodynamic point) is the point from which all sides subtend 120° angles (for triangles with all angles < 120°).

Hmm, but the cevian triangle of the Fermat point being equilateral... I'm not sure about that.

Let me think about this differently. Let me consider the possibility that P is one of the isodynamic points.

The isodynamic points have the property that their pedal triangles are equilateral. But the problem asks about the cevian triangle, not the pedal triangle.

The pedal triangle is formed by the feet of perpendiculars from P to the sides. The cevian triangle is formed by the intersections of cevians AP, BP, CP with the opposite sides.

These are different in general. The pedal triangle of P has vertices at the feet of perpendiculars, while the cevian triangle has vertices at the cevian feet.

For the pedal triangle to be equilateral, P is an isodynamic point. For the cevian triangle to be equilateral, P is... some other special point.

Let me think about what points have equilateral cevian triangles.

Actually, I think I should just try to compute this numerically. Let me pick a specific triangle and find P numerically.

Let me use the triangle A = (0,0), B = (4,0), C = (0,3) (the 3-4-5 right triangle).

I need to find P = (u:v:w) such that:
1. P is on the Neuberg cubic: 9u²w - 16u²v - 16v²u - 25v²w + 25w²u + 9w²v = 0
2. The cevian triangle is equilateral: DE = EF = FD

Let me parametrize. Since barycentric coordinates are homogeneous, I can set w = 1 and use u, v as parameters. Then I have two equations (from the equilateral condition: DE = EF and EF = FD) and one equation (Neuberg cubic). That's three equations in two unknowns, which is overdetermined. So there might be only finitely many solutions (or none for this particular triangle).

Wait, actually, the equilateral condition gives two equations (DE = EF and EF = FD), and the Neuberg cubic gives one equation. With w = 1, we have two unknowns u, v and three equations. This is overdetermined, so generically there are no solutions. But the problem states that such a P exists, so maybe the problem is asking for a general result that holds when such a P exists.

Hmm, but the problem says "Consider a point P on the Neuberg cubic such that the cevian triangle of P is equilateral." This implies such points exist. Maybe they exist for specific triangles, or maybe the problem is about a general property.

Actually, wait. Let me reconsider. The problem might be implying that for any triangle, there exist points on the Neuberg cubic with equilateral cevian triangle, and the ratio QR/PQ is always the same. Or it might be that the problem is about a specific configuration.

Let me reconsider the problem. Maybe I'm overcomplicating the interpretation of Q.

Let me re-read: "Let Q be the point of concurrency of the reflections of P about the sides of triangle ABC."

I think "the reflections of P about the sides" are three points (reflections of P over each side). "Point of concurrency" might be a mistranslation or unusual phrasing for "the point" associated with these reflections. On the Neuberg cubic, the three reflections are collinear, and the line passes through R (isogonal conjugate). 

But "point of concurrency" of three collinear points doesn't make sense. Unless Q is defined as some specific point on this line.

Wait, maybe "reflections of P about the sides" refers to the three lines obtained by reflecting line AP about the perpendicular bisector of BC... no, that's weird.

OK let me try another interpretation. Maybe "reflections of P about the sides" means: for each side, reflect the cevian from the opposite vertex through P about that side. So:
- Reflect line AP about side BC → line ℓ_a
- Reflect line BP about side CA → line ℓ_b
- Reflect line CP about side AB → line ℓ_c

And Q is the concurrency point of ℓ_a, ℓ_b, ℓ_c.

This is actually a known characterization of the Neuberg cubic! P is on the Neuberg cubic iff these three reflected lines are concurrent.

Let me try to verify this and compute the ratio.

Let me work with the 3-4-5 right triangle: A = (0,0), B = (4,0), C = (0,3).

Let P = (px, py) in Cartesian coordinates.

Cevian AP: line from A = (0,0) through P = (px, py). This line has direction (px, py) and equation py·x - px·y = 0.

This cevian meets BC at D. BC goes from B = (4,0) to C = (0,3). Parametrically: (4-4t, 3t) for t ∈ [0,1]. The cevian AP has equation y = (py/px)x (assuming px ≠ 0). So 3t = (py/px)(4-4t), giving t = 4py/(3px + 4py). D = (4·3px/(3px+4py), 3·4py/(3px+4py)) = (12px/(3px+4py), 12py/(3px+4py)).

Now, reflect line AP about line BC.

Line BC: from (4,0) to (0,3). Direction: (-4, 3). Equation: 3x + 4y = 12.

To reflect a line about another line, I can reflect two points on the line and find the reflected line.

Line AP passes through A = (0,0) and P = (px, py). It meets BC at D.

Reflecting line AP about line BC: The reflected line passes through D (since D is on BC, it's fixed by the reflection). We need to reflect one more point.

Let me reflect A = (0,0) about line BC (3x + 4y = 12).

The reflection of point (x0, y0) about line ax + by = c is:
(x0 - 2a(ax0 + by0 - c)/(a² + b²), y0 - 2b(ax0 + by0 - c)/(a² + b²))

For A = (0,0), line 3x + 4y = 12:
ax0 + by0 - c = 0 + 0 - 12 = -12
a² + b² = 9 + 16 = 25

Reflected A: (0 - 2·3·(-12)/25, 0 - 2·4·(-12)/25) = (72/25, 96/25) = (2.88, 3.84)

So the reflected line ℓ_a passes through D and A' = (72/25, 96/25).

Similarly, I need to reflect line BP about line CA, and line CP about line AB.

Line BP: from B = (4,0) through P = (px, py). Meets CA at E.
Line CA: from C = (0,3) to A = (0,0), which is the y-axis, x = 0.

E is where line BP meets x = 0. Line BP: parametrically (4 + t(px-4), t·py). At x = 0: 4 + t(px-4) = 0, t = 4/(4-px). So E = (0, 4py/(4-px)).

Reflect line BP about line CA (x = 0). The reflection of a line about the y-axis maps (x,y) to (-x,y). So the reflected line ℓ_b passes through E = (0, 4py/(4-px)) (which is on CA, so fixed) and the reflection of B = (4,0) about x = 0, which is B' = (-4, 0).

So ℓ_b passes through E = (0, 4py/(4-px)) and B' = (-4, 0).

Line CP: from C = (0,3) through P = (px, py). Meets AB at F.
Line AB: from A = (0,0) to B = (4,0), which is the x-axis, y = 0.

F is where line CP meets y = 0. Line CP: parametrically (t·px, 3 + t(py-3)). At y = 0: 3 + t(py-3) = 0, t = 3/(3-py). So F = (3px/(3-py), 0).

Reflect line CP about line AB (y = 0). The reflection maps (x,y) to (x,-y). So the reflected line ℓ_c passes through F = (3px/(3-py), 0) (on AB, fixed) and the reflection of C = (0,3) about y = 0, which is C' = (0, -3).

So ℓ_c passes through F = (3px/(3-py), 0) and C' = (0, -3).

Now, Q is the concurrency point of ℓ_a, ℓ_b, ℓ_c.

Let me find the equations of these three lines.

ℓ_a: through D = (12px/(3px+4py), 12py/(3px+4py)) and A' = (72/25, 96/25).

ℓ_b: through E = (0, 4py/(4-px)) and B' = (-4, 0).

ℓ_c: through F = (3px/(3-py), 0) and C' = (0, -3).

Let me find Q as the intersection of ℓ_b and ℓ_c, and then check that it lies on ℓ_a (which is the Neuberg cubic condition).

ℓ_b: through (0, 4py/(4-px)) and (-4, 0).
Direction: (-4, -4py/(4-px)).
Parametrically: (0 - 4t, 4py/(4-px) - 4py·t/(4-px)) = (-4t, 4py(1-t)/(4-px)).
Or in equation form: 
Slope = (0 - 4py/(4-px))/(-4 - 0) = py/(4-px)
Equation: y - 4py/(4-px) = py/(4-px) · (x - 0)
y = py/(4-px) · x + 4py/(4-px)
y = py(x + 4)/(4 - px)

ℓ_c: through (3px/(3-py), 0) and (0, -3).
Slope = (-3 - 0)/(0 - 3px/(3-py)) = -3 · (3-py)/(-3px) = (3-py)/px
Equation: y - 0 = (3-py)/px · (x - 3px/(3-py))
y = (3-py)/px · x - (3-py)/px · 3px/(3-py) = (3-py)/px · x - 3
y = (3-py)x/px - 3

Setting ℓ_b and ℓ_c equal:
py(x + 4)/(4 - px) = (3-py)x/px - 3

py·px·(x + 4) = (4-px)·((3-py)x - 3px)

py·px·x + 4·py·px = (4-px)(3-py)x - 3px(4-px)

py·px·x + 4pypx = (4-px)(3-py)x - 3px(4-px)

x[py·px - (4-px)(3-py)] = -3px(4-px) - 4pypx

Let me expand (4-px)(3-py) = 12 - 4py - 3px + px·py

py·px - (12 - 4py - 3px + px·py) = py·px - 12 + 4py + 3px - px·py = 4py + 3px - 12

So: x(4py + 3px - 12) = -3px(4-px) - 4pypx = -12px + 3px² - 4pypx = 3px² - 4pypx - 12px = px(3px - 4py - 12)

x = px(3px - 4py - 12) / (4py + 3px - 12)

Let me denote the denominator as Δ = 3px + 4py - 12. Note that 3px + 4py = 12 is the equation of line BC, so Δ = 0 means P is on BC.

x_Q = px(3px - 4py - 12) / (3px + 4py - 12)

Hmm, let me also compute y_Q from ℓ_b:
y_Q = py(x_Q + 4)/(4 - px)

x_Q + 4 = px(3px - 4py - 12)/(3px + 4py - 12) + 4
= [px(3px - 4py - 12) + 4(3px + 4py - 12)] / (3px + 4py - 12)
= [3px² - 4pxpy - 12px + 12px + 16py - 48] / (3px + 4py - 12)
= [3px² - 4pxpy + 16py - 48] / (3px + 4py - 12)
= [3px² - 4py(px - 4) - 48] / (3px + 4py - 12)

Hmm, let me try to factor. 3px² - 48 = 3(px² - 16) = 3(px-4)(px+4). And -4pxpy + 16py = -4py(px - 4).

So: 3(px-4)(px+4) - 4py(px-4) = (px-4)(3(px+4) - 4py) = (px-4)(3px + 12 - 4py)

x_Q + 4 = (px-4)(3px + 12 - 4py) / (3px + 4py - 12)

y_Q = py · (px-4)(3px + 12 - 4py) / ((4 - px)(3px + 4py - 12))
= py · (-(4-px))(3px + 12 - 4py) / ((4-px)(3px + 4py - 12))
= -py(3px + 12 - 4py) / (3px + 4py - 12)
= py(4py - 3px - 12) / (3px + 4py - 12)

So Q = (px(3px - 4py - 12)/(3px + 4py - 12), py(4py - 3px - 12)/(3px + 4py - 12))

Now, the isogonal conjugate R of P. For a triangle with vertices A, B, C and side lengths a, b, c, the isogonal conjugate in Cartesian coordinates is complex. Let me compute it using barycentric coordinates.

P in barycentrics: P = (u:v:w) where u + v + w = s, and P_cartesian = (4v/s, 3w/s). So v = s·px/4, w = s·py/3, u = s - v - w = s(1 - px/4 - py/3).

We can take u = 1 - px/4 - py/3, v = px/4, w = py/3 (setting s = 1).

Actually, let me use unnormalized: u = 12 - 3px - 4py, v = 3px, w = 4py (multiplying by 12).

R (isogonal conjugate) in barycentrics: (a²/u : b²/v : c²/w) = (25/u : 9/v : 16/w) = (25/(12-3px-4py) : 9/(3px) : 16/(4py)) = (25/(12-3px-4py) : 3/px : 4/py)

Converting to Cartesian:
R_x = 4 · v_R / (u_R + v_R + w_R) = 4 · (3/px) / (25/(12-3px-4py) + 3/px + 4/py)

Let me compute the denominator:
25/(12-3px-4py) + 3/px + 4/py

Let me denote d = 12 - 3px - 4py (note: this is related to Δ = 3px + 4py - 12 = -d).

= 25/d + 3/px + 4/py = (25pxpy + 3dpy + 4dpx) / (dpxpy)

25pxpy + 3dpy + 4dpx = 25pxpy + 3(12-3px-4py)py + 4(12-3px-4py)px
= 25pxpy + 36py - 9pxpy - 12py² + 48px - 12px² - 16pxpy
= (25 - 9 - 16)pxpy + 36py - 12py² + 48px - 12px²
= 0·pxpy + 36py - 12py² + 48px - 12px²
= -12px² + 48px - 12py² + 36py
= -12(px² - 4px + py² - 3py)
= -12(px² - 4px + 4 + py² - 3py + 9/4 - 4 - 9/4)
= -12((px-2)² + (py-3/2)² - 4 - 9/4)
= -12((px-2)² + (py-3/2)² - 25/4)

Interesting! (px-2)² + (py-3/2)² is the squared distance from P to the circumcenter O = (2, 3/2). And 25/4 = (5/2)² = R² (circumradius squared, since the circumradius is 5/2 for a 3-4-5 triangle).

So the denominator = -12(|PO|² - R²) / (dpxpy) = 12(R² - |PO|²) / (dpxpy)

R_x = 4 · (3/px) · dpxpy / (12(R² - |PO|²)) = 12dpy / (12(R² - |PO|²)) = dpy / (R² - |PO|²)

where d = 12 - 3px - 4py = -Δ.

R_x = (12 - 3px - 4py)py / (R² - |PO|²)

Similarly, R_y = 3 · w_R / (u_R + v_R + w_R) = 3 · (4/py) · dpxpy / (12(R² - |PO|²)) = 12dpx / (12(R² - |PO|²)) = dpx / (R² - |PO|²)

R_y = (12 - 3px - 4py)px / (R² - |PO|²)

So R = ((12-3px-4py)py / (R²-|PO|²), (12-3px-4py)px / (R²-|PO|²))

where R² = 25/4 and |PO|² = (px-2)² + (py-3/2)².

Let me denote D = R² - |PO|² = 25/4 - (px-2)² - (py-3/2)² and d = 12 - 3px - 4py.

R = (d·py/D, d·px/D)

Now, Q = (px(3px - 4py - 12)/(3px + 4py - 12), py(4py - 3px - 12)/(3px + 4py - 12))

Note that 3px + 4py - 12 = -d, so:

Q = (px(3px - 4py - 12)/(-d), py(4py - 3px - 12)/(-d))
= (-px(3px - 4py - 12)/d, -py(4py - 3px - 12)/d)
= (px(12 - 3px + 4py)/d, py(12 - 3px + 4py)/d)... 

wait let me redo this.

3px - 4py - 12 = -(12 - 3px + 4py). And 4py - 3px - 12 = -(12 + 3px - 4py).

Hmm, let me be more careful.

Q_x = px(3px - 4py - 12) / (3px + 4py - 12) = px(3px - 4py - 12) / (-d) = -px(3px - 4py - 12)/d = px(12 + 4py - 3px)/d

Q_y = py(4py - 3px - 12) / (3px + 4py - 12) = py(4py - 3px - 12)/(-d) = -py(4py - 3px - 12)/d = py(12 + 3px - 4py)/d

So Q = (px(12 + 4py - 3px)/d, py(12 + 3px - 4py)/d)

And R = (d·py/D, d·px/D)

And P = (px, py).

Now I need to compute QR/PQ. But first, I need to find the specific P that is on the Neuberg cubic AND has equilateral cevian triangle.

The Neuberg cubic condition is that ℓ_a also passes through Q. Let me compute that condition.

ℓ_a passes through D = (12px/(3px+4py), 12py/(3px+4py)) and A' = (72/25, 96/25).

Actually, this is getting very messy. Let me try a numerical approach. Let me pick a specific P and see if I can find one on the Neuberg cubic with equilateral cevian triangle.

Actually, let me try a completely different approach. Let me think about the problem theoretically.

Key insight: The problem asks for QR/PQ, which should be a constant. Let me see if there's a known relationship.

For the Neuberg cubic, the key property is that P, R (isogonal conjugate), and L (de Longchamps point) are collinear. Also, the reflections of the cevians are concurrent at Q.

I wonder if Q, P, R are collinear and if there's a fixed ratio.

Let me check with our formulas. Are P, Q, R collinear?

P = (px, py)
Q = (px(12 + 4py - 3px)/d, py(12 + 3px - 4py)/d) where d = 12 - 3px - 4py
R = (d·py/D, d·px/D) where D = 25/4 - (px-2)² - (py-3/2)²

For P, Q, R to be collinear, we need:
(Q_x - px)(R_y - py) = (Q_y - py)(R_x - px)

Q_x - px = px(12 + 4py - 3px)/d - px = px[(12 + 4py - 3px) - d]/d = px[(12 + 4py - 3px) - (12 - 3px - 4py)]/d = px[8py]/d = 8pxpy/d

Q_y - py = py(12 + 3px - 4py)/d - py = py[(12 + 3px - 4py) - d]/d = py[(12 + 3px - 4py) - (12 - 3px - 4py)]/d = py[6px]/d = 6pxpy/d

R_x - px = dpy/D - px = (dpy - pxD)/D
R_y - py = dpx/D - py = (dpx - pyD)/D

Collinearity: (8pxpy/d)(dpx - pyD)/D = (6pxpy/d)(dpy - pxD)/D

Simplifying (assuming pxpy ≠ 0):
8(dpx - pyD) = 6(dpy - pxD)
8dpx - 8pyD = 6dpy - 6pxD
8dpx + 6pxD = 6dpy + 8pyD
px(8d + 6D) = py(6d + 8D)
px · 2(4d + 3D) = py · 2(3d + 4D)
px(4d + 3D) = py(3d + 4D)

This is not automatically true, so P, Q, R are not always collinear. They're collinear only when px(4d + 3D) = py(3d + 4D), which is an additional condition.

Hmm, so maybe P, Q, R are not collinear in general, and the ratio QR/PQ is still a constant due to the equilateral cevian triangle condition.

This is getting very complex. Let me try a numerical approach.

Let me try to find a point P on the Neuberg cubic with equilateral cevian triangle for the 3-4-5 triangle.

Actually, let me try a simpler triangle. Let me use an isoceles triangle to reduce the number of parameters.

Let me use A = (0, h), B = (-1, 0), C = (1, 0) for some height h. By symmetry, if P is on the axis of symmetry (x = 0), then the cevian triangle might have some symmetry.

If P = (0, py) (on the axis of symmetry), then by symmetry, the cevian triangle has D on BC at (0, 0) (the midpoint), and E, F are symmetric about the y-axis. For the cevian triangle to be equilateral, we need DE = DF (automatic by symmetry) and DE = EF.

D = (0, 0) (foot of cevian from A to BC, which is the midpoint since P is on the axis).

Wait, the cevian from A through P = (0, py) hits BC (the x-axis) at (0, 0). So D = (0, 0).

E = foot of cevian from B through P on CA. 
Line BP: from B = (-1, 0) through P = (0, py). Parametrically: (-1 + t, t·py). 
Line CA: from C = (1, 0) to A = (0, h). Parametrically: (1-s, s·h).
Intersection: -1 + t = 1 - s and t·py = s·h.
From first: s = 2 - t. Substituting: t·py = (2-t)·h → t = 2h/(py + h).
E = (-1 + 2h/(py+h), 2hpy/(py+h)) = ((h-py)/(py+h), 2hpy/(py+h))

F = foot of cevian from C through P on AB.
By symmetry (since the triangle is isoceles and P is on the axis):
F = ((py-h)/(py+h), 2hpy/(py+h))... wait, let me compute.

Line CP: from C = (1, 0) through P = (0, py). Parametrically: (1-t, t·py).
Line AB: from A = (0, h) to B = (-1, 0). Parametrically: (-s, h(1-s)).
Intersection: 1-t = -s and t·py = h(1-s).
From first: s = t-1. Substituting: t·py = h(1-(t-1)) = h(2-t) → t = 2h/(py+h).
F = (1 - 2h/(py+h), 2hpy/(py+h)) = ((py-h)/(py+h), 2hpy/(py+h))

So E = ((h-py)/(h+py), 2hpy/(h+py)) and F = ((py-h)/(h+py), 2hpy/(h+py)) = (-(h-py)/(h+py), 2hpy/(h+py)).

So E and F are symmetric about the y-axis, as expected. E = (-a, b) and F = (a, b) where a = (h-py)/(h+py) and b = 2hpy/(h+py).

D = (0, 0).

DE² = a² + b² = ((h-py)/(h+py))² + (2hpy/(h+py))² = [(h-py)² + 4h²py²]/(h+py)²

EF = 2a = 2(h-py)/(h+py) (distance between E and F, which are at (-a,b) and (a,b)).

EF² = 4(h-py)²/(h+py)²

For equilateral: DE² = EF²:
(h-py)² + 4h²py² = 4(h-py)²
4h²py² = 3(h-py)²
2hpy = ±√3(h-py)

Case 1: 2hpy = √3(h-py) → 2hpy = √3h - √3py → py(2h + √3) = √3h → py = √3h/(2h + √3)

Case 2: 2hpy = -√3(h-py) → 2hpy = -√3h + √3py → py(2h - √3) = -√3h → py = -√3h/(2h - √3) = √3h/(√3 - 2h)

For Case 1 (assuming h > 0 and py > 0, and py < h for P inside the triangle):
py = √3h/(2h + √3)

For this to be inside the triangle, we need 0 < py < h:
√3h/(2h + √3) < h → √3 < 2h + √3 → 0 < 2h, which is true.
And py > 0 requires h > 0. ✓

Now, I also need P to be on the Neuberg cubic. Let me compute the Neuberg cubic for this isoceles triangle.

For the isoceles triangle A = (0, h), B = (-1, 0), C = (1, 0):
Side lengths: a = BC = 2, b = CA = √(1+h²), c = AB = √(1+h²).

Since b = c, the triangle is isoceles with b = c.

Circumcenter O: by symmetry, O is on the y-axis. O = (0, y_O).
OA = OB: h - y_O = √(1 + y_O²) → (h - y_O)² = 1 + y_O² → h² - 2hy_O + y_O² = 1 + y_O² → h² - 2hy_O = 1 → y_O = (h² - 1)/(2h)

Orthocenter H: by symmetry, H is on the y-axis. H = (0, y_H).
For a triangle with vertices (0,h), (-1,0), (1,0), the orthocenter is at (0, 1/h).
(Actually, let me verify: the altitude from A is the y-axis (x=0). The altitude from B is perpendicular to AC. AC has direction (1-0, 0-h) = (1, -h), so the altitude from B has direction (h, 1). Line through B = (-1, 0) with direction (h, 1): parametrically (-1+ht, t). At x = 0: t = 1/h, y = 1/h. So H = (0, 1/h). ✓)

De Longchamps point L = 2O - H = (0, 2(h²-1)/(2h) - 1/h) = (0, (h²-1)/h - 1/h) = (0, (h²-2)/h)

Now, P = (0, py) is on the Neuberg cubic iff P, R (isogonal conjugate of P), and L are collinear.

Since P and L are both on the y-axis, R must also be on the y-axis for collinearity. By symmetry (since the triangle is isoceles and P is on the axis), R is indeed on the y-axis. So the collinearity is automatic!

Wait, that means every point on the y-axis is on the Neuberg cubic? That can't be right...

Actually, for an isoceles triangle, the axis of symmetry is a component of many triangle cubics. Let me check: the Neuberg cubic for an isoceles triangle might contain the axis of symmetry as a component.

Hmm, actually, the Neuberg cubic is an irreducible cubic (for a general triangle). For an isoceles triangle, it might factor. Let me check.

In barycentric coordinates for our isoceles triangle (b = c):
The Neuberg cubic equation involves terms with (b² - c²) and (b² + c²). When b = c, some terms vanish.

Actually, the general Neuberg cubic equation in barycentrics is:
Σ x(y² - z²)(...) = 0

When b = c (y and z play symmetric roles), the equation might factor as (y - z) · (quadratic) = 0, where y = z is the axis of symmetry.

So for an isoceles triangle, the Neuberg cubic factors into the axis of symmetry (y = z, i.e., the median from A) and a conic. Points on the axis of symmetry are trivially on the Neuberg cubic.

This means my approach of using an isoceles triangle with P on the axis won't give a non-trivial constraint from the Neuberg cubic. The equilateral cevian triangle condition gives py = √3h/(2h + √3), but the Neuberg cubic condition is automatically satisfied.

So for any h, P = (0, √3h/(2h + √3)) is on the Neuberg cubic (trivially, being on the axis) and has an equilateral cevian triangle. 

Now I need to compute Q and R for this P and find QR/PQ. If the ratio is constant (independent of h), that's our answer.

Let me compute Q. I need to reflect the cevians about the sides and find the concurrency point.

For the isoceles triangle A = (0, h), B = (-1, 0), C = (1, 0), P = (0, py):

Cevian AP: from A = (0, h) through P = (0, py). This is the y-axis (x = 0). It meets BC (y = 0) at D = (0, 0).

Reflect line AP (x = 0) about line BC (y = 0): The reflection of the y-axis about the x-axis is still the y-axis (x = 0). So ℓ_a is the y-axis.

Cevian BP: from B = (-1, 0) through P = (0, py). Direction: (1, py). Equation: y = py(x + 1).
Meets CA at E = ((h-py)/(h+py), 2hpy/(h+py)) (computed earlier).

Reflect line BP about line CA. Line CA goes from C = (1, 0) to A = (0, h). Direction: (-1, h). Equation: hx + y = h (since at C: h·1 + 0 = h ✓, at A: h·0 + h = h ✓).

To reflect line BP about line CA, I reflect two points on BP about CA.

Point B = (-1, 0): reflect about hx + y = h.
Using the reflection formula: for line ax + by = c, reflection of (x0, y0) is (x0 - 2a(ax0+by0-c)/(a²+b²), y0 - 2b(ax0+by0-c)/(a²+b²)).
a = h, b = 1, c = h. a² + b² = h² + 1.
ax0 + by0 - c = h·(-1) + 1·0 - h = -2h.
B' = (-1 - 2h·(-2h)/(h²+1), 0 - 2·1·(-2h)/(h²+1)) = (-1 + 4h²/(h²+1), 4h/(h²+1)) = ((-h²-1+4h²)/(h²+1), 4h/(h²+1)) = ((3h²-1)/(h²+1), 4h/(h²+1))

Point E is on CA, so it's fixed by the reflection. E = ((h-py)/(h+py), 2hpy/(h+py)).

So ℓ_b passes through E and B'.

By symmetry, ℓ_c is the reflection of ℓ_b about the y-axis. So ℓ_c passes through F = (-E_x, E_y) and C' = (-B'_x, B'_y).

Q is the intersection of ℓ_a (the y-axis, x = 0), ℓ_b, and ℓ_c. By symmetry, Q is on the y-axis. So Q = (0, qy) for some qy.

To find qy, I use ℓ_b: the line through E and B', and find where it crosses x = 0.

E = ((h-py)/(h+py), 2hpy/(h+py))
B' = ((3h²-1)/(h²+1), 4h/(h²+1))

The line through E and B':
Parametrically: E + t(B' - E).
x-coordinate: E_x + t(B'_x - E_x) = 0 → t = -E_x/(B'_x - E_x) = E_x/(E_x - B'_x)

y = E_y + t(B'_y - E_y) = E_y + E_x/(E_x - B'_x) · (B'_y - E_y)
= (E_y(E_x - B'_x) + E_x(B'_y - E_y)) / (E_x - B'_x)
= (E_y·E_x - E_y·B'_x + E_x·B'_y - E_x·E_y) / (E_x - B'_x)
= (E_x·B'_y - E_y·B'_x) / (E_x - B'_x)

Let me compute this. Let me denote:
E_x = (h-py)/(h+py), E_y = 2hpy/(h+py)
B'_x = (3h²-1)/(h²+1), B'_y = 4h/(h²+1)

E_x - B'_x = (h-py)/(h+py) - (3h²-1)/(h²+1)
= [(h-py)(h²+1) - (3h²-1)(h+py)] / [(h+py)(h²+1)]

Numerator of E_x - B'_x:
(h-py)(h²+1) - (3h²-1)(h+py)
= h³ + h - pyh² - py - 3h³ - 3h²py + h + py
= h³ + h - pyh² - py - 3h³ - 3h²py + h + py
= -2h³ + 2h - 4h²py
= 2h(-h² + 1 - 2hpy)
= 2h(1 - h² - 2hpy)

E_x·B'_y - E_y·B'_x = [(h-py)/(h+py)]·[4h/(h²+1)] - [2hpy/(h+py)]·[(3h²-1)/(h²+1)]
= [4h(h-py) - 2hpy(3h²-1)] / [(h+py)(h²+1)]
= h[4(h-py) - 2py(3h²-1)] / [(h+py)(h²+1)]
= h[4h - 4py - 6h²py + 2py] / [(h+py)(h²+1)]
= h[4h - 2py - 6h²py] / [(h+py)(h²+1)]
= h[4h - 2py(1 + 3h²)] / [(h+py)(h²+1)]
= 2h[2h - py(1 + 3h²)] / [(h+py)(h²+1)]

So qy = (E_x·B'_y - E_y·B'_x) / (E_x - B'_x)
= {2h[2h - py(1 + 3h²)] / [(h+py)(h²+1)]} / {2h(1 - h² - 2hpy) / [(h+py)(h²+1)]}
= [2h - py(1 + 3h²)] / (1 - h² - 2hpy)

Now, substituting py = √3h/(2h + √3):

Let me denote s = √3 for brevity. py = sh/(2h + s).

1 + 3h² = 1 + 3h²

2h - py(1 + 3h²) = 2h - sh(1 + 3h²)/(2h + s) = h[2(2h + s) - s(1 + 3h²)]/(2h + s) = h[4h + 2s - s - 3sh²]/(2h + s) = h[4h + s - 3sh²]/(2h + s) = h[4h + s(1 - 3h²)]/(2h + s)

1 - h² - 2hpy = 1 - h² - 2h·sh/(2h + s) = [(1 - h²)(2h + s) - 2sh²]/(2h + s) = [2h + s - 2h³ - sh² - 2sh²]/(2h + s) = [2h + s - 2h³ - 3sh²]/(2h + s) = [2h(1 - h²) + s(1 - 3h²)]/(2h + s)

So qy = h[4h + s(1 - 3h²)] / [2h(1 - h²) + s(1 - 3h²)]

Hmm, let me factor. Note that 1 - 3h² = (1 - s·h)(1 + s·h) and 4h + s(1 - 3h²) = 4h + s - 3sh².

Let me try specific values of h to see if the ratio QR/PQ is constant.

Let me try h = 1 (equilateral triangle with side 2). But wait, for h = 1, the triangle A = (0,1), B = (-1,0), C = (1,0) has side lengths a = 2, b = c = √2. This is not equilateral.

Actually, for an equilateral triangle with B = (-1, 0), C = (1, 0), we need A = (0, √3). So h = √3.

But as I noted earlier, the equilateral triangle case is degenerate for the Neuberg cubic. Let me try h = 2.

h = 2, s = √3:
py = √3·2/(4 + √3) = 2√3/(4 + √3) = 2√3(4 - √3)/(16 - 3) = 2√3(4 - √3)/13 = (8√3 - 6)/13

Let me compute numerically:
√3 ≈ 1.7321
py = 2·1.7321/(4 + 1.7321) = 3.4641/5.7321 ≈ 0.6043

qy = h[4h + s(1 - 3h²)] / [2h(1 - h²) + s(1 - 3h²)]
= 2[8 + √3(1 - 12)] / [4(1 - 4) + √3(1 - 12)]
= 2[8 - 11√3] / [4(-3) + √3(-11)]
= 2[8 - 11√3] / [-12 - 11√3]
= 2(8 - 11√3) / (-(12 + 11√3))
= -2(8 - 11√3) / (12 + 11√3)
= 2(11√3 - 8) / (12 + 11√3)

Numerically: 11√3 ≈ 19.053, so 11√3 - 8 ≈ 11.053, 12 + 11√3 ≈ 31.053.
qy ≈ 2·11.053/31.053 ≈ 22.106/31.053 ≈ 0.7119

So Q = (0, 0.7119), P = (0, 0.6043).

Now I need R (isogonal conjugate of P).

For the isoceles triangle with b = c, the isogonal conjugate of P = (0, py) is on the y-axis. Let me compute it.

P in barycentrics: P = (u:v:w) where u + v + w = 1 (normalized).
P = u·A + v·B + w·C = (0, u·h) + (-v, 0) + (w, 0) = (w - v, u·h).
Since P = (0, py): w = v and u·h = py, so u = py/h, v = w = (1 - py/h)/2.

R (isogonal conjugate) = (a²/u : b²/v : c²/w) = (4/u : (1+h²)/v : (1+h²)/w).
Since v = w, R = (4/u : (1+h²)/v : (1+h²)/v), which is on the axis of symmetry. ✓

R in Cartesian: R = (0, r_y) where r_y = u_R · h / (u_R + v_R + w_R).
u_R = 4/u = 4h/py, v_R = w_R = (1+h²)/v = (1+h²)·2/(1 - py/h) = 2(1+h²)h/(h - py).

r_y = (4h/py)·h / (4h/py + 2·2(1+h²)h/(h-py))
= 4h²/py / (4h/py + 4(1+h²)h/(h-py))
= 4h²/py / [4h(1/py + (1+h²)/(h-py))]
= h/py / [1/py + (1+h²)/(h-py)]
= h/py · py(h-py) / [(h-py) + py(1+h²)]
= h(h-py) / [h - py + py + h²py]
= h(h-py) / [h + h²py]
= h(h-py) / [h(1 + hpy)]
= (h - py) / (1 + hpy)

So R = (0, (h - py)/(1 + hpy)).

For h = 2, py ≈ 0.6043:
r_y = (2 - 0.6043)/(1 + 2·0.6043) = 1.3957/(1 + 1.2086) = 1.3957/2.2086 ≈ 0.6320

So R = (0, 0.6320).

Now:
P = (0, 0.6043)
Q = (0, 0.7119)
R = (0, 0.6320)

PQ = |0.7119 - 0.6043| = 0.1076
QR = |0.7119 - 0.6320| = 0.0799

QR/PQ = 0.0799/0.1076 ≈ 0.7425

Hmm, that doesn't look like a clean ratio. Let me try another h to see if it's constant.

Let me try h = 3.
py = √3·3/(6 + √3) = 3√3/(6 + √3) = 3√3(6 - √3)/(36 - 3) = 3√3(6 - √3)/33 = √3(6 - √3)/11 = (6√3 - 3)/11

Numerically: py = (6·1.7321 - 3)/11 = (10.3926 - 3)/11 = 7.3926/11 ≈ 0.6720

qy = h[4h + s(1 - 3h²)] / [2h(1 - h²) + s(1 - 3h²)]
= 3[12 + √3(1 - 27)] / [6(1 - 9) + √3(1 - 27)]
= 3[12 - 26√3] / [6(-8) + √3(-26)]
= 3[12 - 26√3] / [-48 - 26√3]
= -3[12 - 26√3] / [48 + 26√3]
= 3[26√3 - 12] / [48 + 26√3]

Numerically: 26√3 ≈ 45.035, 26√3 - 12 ≈ 33.035, 48 + 26√3 ≈ 93.035.
qy ≈ 3·33.035/93.035 ≈ 99.105/93.035 ≈ 1.0652

R: r_y = (h - py)/(1 + hpy) = (3 - 0.6720)/(1 + 3·0.6720) = 2.328/(1 + 2.016) = 2.328/3.016 ≈ 0.7719

P = (0, 0.6720)
Q = (0, 1.0652)
R = (0, 0.7719)

PQ = 1.0652 - 0.6720 = 0.3932
QR = 1.0652 - 0.7719 = 0.2933

QR/PQ = 0.2933/0.3932 ≈ 0.7460

Hmm, 0.7425 and 0.7460 are close but not exactly equal. Let me check my calculations more carefully.

Actually, let me redo the calculations with exact values.

For h = 2, s = √3:
py = 2s/(4 + s)

qy = 2(11s - 8)/(12 + 11s)

Let me rationalize:
qy = 2(11s - 8)/(12 + 11s) · (12 - 11s)/(12 - 11s) = 2(11s - 8)(12 - 11s)/(144 - 363) = 2(11s - 8)(12 - 11s)/(-219)

(11s - 8)(12 - 11s) = 132s - 121s² - 96 + 88s = 220s - 121·3 - 96 = 220s - 363 - 96 = 220s - 459

qy = 2(220s - 459)/(-219) = -2(220s - 459)/219 = 2(459 - 220s)/219

Numerically: 220s ≈ 381.066, 459 - 381.066 = 77.934, qy = 2·77.934/219 ≈ 155.868/219 ≈ 0.7118. ✓

r_y = (h - py)/(1 + hpy) = (2 - 2s/(4+s))/(1 + 2·2s/(4+s)) = ((2(4+s) - 2s)/(4+s))/((4+s+4s)/(4+s)) = (8+2s-2s)/(4+5s) = 8/(4+5s)

Numerically: 5s ≈ 8.660, r_y = 8/(4+8.660) = 8/12.660 ≈ 0.6319. ✓

PQ = qy - py = 2(459 - 220s)/219 - 2s/(4+s)

Let me compute 2s/(4+s) = 2s(4-s)/(16-3) = 2s(4-s)/13 = (8s - 2·3)/13 = (8s - 6)/13

PQ = 2(459 - 220s)/219 - (8s - 6)/13

To combine, find common denominator. 219 = 3·73, 13 is prime. LCM = 219·13 = 2847.

PQ = [2(459 - 220s)·13 - (8s - 6)·219] / 2847
= [26(459 - 220s) - 219(8s - 6)] / 2847
= [11934 - 5720s - 1752s + 1314] / 2847
= [13248 - 7472s] / 2847

QR = qy - r_y = 2(459 - 220s)/219 - 8/(4+5s)

8/(4+5s) = 8(4-5s)/(16-75) = 8(4-5s)/(-59) = -8(4-5s)/59 = 8(5s-4)/59

QR = 2(459-220s)/219 - 8(5s-4)/59

LCM of 219 and 59: 219 = 3·73, 59 is prime. LCM = 219·59 = 12921.

QR = [2(459-220s)·59 - 8(5s-4)·219] / 12921
= [118(459-220s) - 1752(5s-4)] / 12921
= [54162 - 25960s - 8760s + 7008] / 12921
= [61170 - 34720s] / 12921

QR/PQ = [61170 - 34720s]/12921 / [13248 - 7472s]/2847
= [61170 - 34720s] · 2847 / (12921 · [13248 - 7472s])
= [61170 - 34720s] · 2847 / (12921 · [13248 - 7472s])

Note 12921 = 219·59 and 2847 = 219·13. So 2847/12921 = 13/59.

QR/PQ = 13[61170 - 34720s] / (59[13248 - 7472s])

Let me compute numerically:
61170 - 34720·1.7321 = 61170 - 60138.5 = 1031.5
13248 - 7472·1.7321 = 13248 - 12940.7 = 307.3

QR/PQ = 13·1031.5 / (59·307.3) = 13409.5 / 18130.7 ≈ 0.7397

Hmm, that's different from my earlier calculation. Let me recheck.

Wait, I think I made an arithmetic error. Let me recompute more carefully.

For h = 2, s = √3:
py = 2s/(4+s)

Let me compute py exactly:
py = 2√3/(4+√3) = 2√3(4-√3)/((4+√3)(4-√3)) = 2√3(4-√3)/(16-3) = 2√3(4-√3)/13 = (8√3 - 2·3)/13 = (8√3 - 6)/13

OK so py = (8√3 - 6)/13.

qy: I had qy = 2(11√3 - 8)/(12 + 11√3).

Let me rationalize:
qy = 2(11√3 - 8)/(12 + 11√3) · (12 - 11√3)/(12 - 11√3)
= 2(11√3 - 8)(12 - 11√3) / (144 - 121·3)
= 2(11√3 - 8)(12 - 11√3) / (144 - 363)
= 2(11√3 - 8)(12 - 11√3) / (-219)

(11√3 - 8)(12 - 11√3) = 132√3 - 121·3 - 96 + 88√3 = 220√3 - 363 - 96 = 220√3 - 459

qy = 2(220√3 - 459) / (-219) = -2(220√3 - 459)/219 = 2(459 - 220√3)/219

r_y = 8/(4 + 5√3) = 8(4 - 5√3)/(16 - 75) = 8(4 - 5√3)/(-59) = 8(5√3 - 4)/59

Now:
PQ = qy - py = 2(459 - 220√3)/219 - (8√3 - 6)/13

Common denominator: 219 = 3·73, 13. LCM = 3·73·13 = 2847.

PQ = [2(459 - 220√3)·13 - (8√3 - 6)·219] / 2847

2·13 = 26, so:
= [26(459 - 220√3) - 219(8√3 - 6)] / 2847
= [11934 - 5720√3 - 1752√3 + 1314] / 2847
= [13248 - 7472√3] / 2847

QR = qy - r_y = 2(459 - 220√3)/219 - 8(5√3 - 4)/59

Common denominator: 219 and 59. LCM = 219·59 = 12921.

= [2(459 - 220√3)·59 - 8(5√3 - 4)·219] / 12921

2·59 = 118:
= [118(459 - 220√3) - 1752(5√3 - 4)] / 12921
= [54162 - 25960√3 - 8760√3 + 7008] / 12921
= [61170 - 34720√3] / 12921

QR/PQ = [61170 - 34720√3] / 12921 · 2847 / [13248 - 7472√3]
= [61170 - 34720√3] · 2847 / (12921 · [13248 - 7472√3])

2847/12921 = 2847/12921. Let me simplify: 2847 = 13·219, 12921 = 59·219. So 2847/12921 = 13/59.

QR/PQ = 13[61170 - 34720√3] / (59[13248 - 7472√3])

Let me factor. 
61170 = 13·4705.3... no. Let me try: 61170/13 = 4705.38... not integer.
Let me try: 61170/2 = 30585, 34720/2 = 17360. 
61170/10 = 6117, 34720/10 = 3472.
GCD(61170, 34720): 61170 = 1·34720 + 26450, 34720 = 1·26450 + 8270, 26450 = 3·8270 + 1640, 8270 = 5·1640 + 70, 1640 = 23·70 + 30, 70 = 2·30 + 10, 30 = 3·10. GCD = 10.

61170 - 34720√3 = 10(6117 - 3472√3)

13248 - 7472√3: GCD(13248, 7472) = 13248 = 1·7472 + 5776, 7472 = 1·5776 + 1696, 5776 = 3·1696 + 688, 1696 = 2·688 + 320, 688 = 2·320 + 48, 320 = 6·48 + 32, 48 = 1·32 + 16, 32 = 2·16. GCD = 16.

13248 - 7472√3 = 16(828 - 467√3)

QR/PQ = 13·10(6117 - 3472√3) / (59·16(828 - 467√3))
= 130(6117 - 3472√3) / (944(828 - 467√3))
= 65(6117 - 3472√3) / (472(828 - 467√3))

Let me compute numerically:
6117 - 3472·1.7320508 = 6117 - 6013.6 = 103.4
828 - 467·1.7320508 = 828 - 808.87 = 19.13

QR/PQ = 65·103.4 / (472·19.13) = 6721 / 9029.4 ≈ 0.7442

Hmm, let me try to see if this simplifies to something. Let me compute more precisely.

√3 = 1.7320508075688772...

3472√3 = 3472 × 1.7320508075688772 = 6013.64440191...
6117 - 6013.64440191 = 103.35559809

467√3 = 467 × 1.7320508075688772 = 808.86772714...
828 - 808.86772714 = 19.13227286

QR/PQ = 65 × 103.35559809 / (472 × 19.13227286) = 6718.113876 / 9038.43363 = 0.74309...

Let me try h = 3 to compare.

For h = 3, s = √3:
py = 3s/(6+s) = 3s(6-s)/(36-3) = 3s(6-s)/33 = s(6-s)/11 = (6s-3)/11

qy = 3(26s - 12)/(48 + 26s)

r_y = (3 - py)/(1 + 3py) = (3 - (6s-3)/11)/(1 + 3(6s-3)/11) = ((33 - 6s + 3)/11)/((11 + 18s - 9)/11) = (36 - 6s)/(2 + 18s) = 6(6-s)/(2(1+9s)) = 3(6-s)/(1+9s)

Let me compute:
py = (6√3 - 3)/11 ≈ (10.392 - 3)/11 = 7.392/11 ≈ 0.6720

qy = 3(26√3 - 12)/(48 + 26√3) ≈ 3(45.033 - 12)/(48 + 45.033) = 3·33.033/93.033 = 99.1/93.033 ≈ 1.0652

r_y = 3(6 - √3)/(1 + 9√3) ≈ 3·4.268/(1 + 15.588) = 12.804/16.588 ≈ 0.7719

PQ = qy - py ≈ 1.0652 - 0.6720 = 0.3932
QR = qy - r_y ≈ 1.0652 - 0.7719 = 0.2933

QR/PQ ≈ 0.2933/0.3932 ≈ 0.7460

So for h=2: QR/PQ ≈ 0.7431
For h=3: QR/PQ ≈ 0.7460

These are close but not equal. This suggests either:
1. My interpretation of Q is wrong, or
2. The ratio is not constant (which contradicts the problem asking to "find the ratio"), or
3. I'm making computational errors.

Let me double-check my formula for Q.

Actually, wait. Let me reconsider the problem. Maybe "reflections of P about the sides" means the reflections of the point P (not the cevians) over the sides, and "point of concurrency" means the point where the lines from the vertices to these reflected points concur.

So:
- P_a = reflection of P over BC
- P_b = reflection of P over CA
- P_c = reflection of P over AB
- Q = concurrence of lines AP_a, BP_b, CP_c

Let me try this interpretation.

For the isoceles triangle A = (0, h), B = (-1, 0), C = (1, 0), P = (0, py):

P_a = reflection of P = (0, py) over BC (y = 0) = (0, -py)
P_b = reflection of P over CA (hx + y = h)
P_c = reflection of P over AB (hx - y = h)... wait, let me get the equations right.

CA: from C = (1, 0) to A = (0, h). Equation: hx + y = h (verified earlier).
AB: from A = (0, h) to B = (-1, 0). Direction: (-1, -h). Equation: hx - y = ... at A: h·0 - h = -h. At B: h·(-1) - 0 = -h. So equation: hx - y = -h, or y = hx + h.

P_b = reflection of (0, py) over hx + y = h:
a = h, b = 1, c = h. a² + b² = h² + 1.
ax0 + by0 - c = 0 + py - h = py - h.
P_b = (0 - 2h(py-h)/(h²+1), py - 2(py-h)/(h²+1)) = (-2h(py-h)/(h²+1), py - 2(py-h)/(h²+1))
= (2h(h-py)/(h²+1), (py(h²+1) - 2(py-h))/(h²+1))
= (2h(h-py)/(h²+1), (pyh² + py - 2py + 2h)/(h²+1))
= (2h(h-py)/(h²+1), (pyh² - py + 2h)/(h²+1))
= (2h(h-py)/(h²+1), (py(h²-1) + 2h)/(h²+1))

P_c = reflection of (0, py) over y = hx + h, i.e., hx - y = -h, or -hx + y = h.
a = -h, b = 1, c = h. a² + b² = h² + 1.
ax0 + by0 - c = 0 + py - h = py - h.
P_c = (0 - 2(-h)(py-h)/(h²+1), py - 2(py-h)/(h²+1)) = (2h(py-h)/(h²+1), (py(h²-1)+2h)/(h²+1))
= (-2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1))

By symmetry, P_c = (-P_b_x, P_b_y). ✓

Now, lines AP_a, BP_b, CP_c:

AP_a: from A = (0, h) to P_a = (0, -py). This is the y-axis (x = 0).

BP_b: from B = (-1, 0) to P_b = (2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1)).

CP_c: from C = (1, 0) to P_c = (-2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1)).

By symmetry, Q is on the y-axis. Q = (0, qy).

From line BP_b: 
B = (-1, 0), P_b = (2h(h-py)/(h²+1), (py(h²-1)+2h)/(h²+1))

Direction: (2h(h-py)/(h²+1) + 1, (py(h²-1)+2h)/(h²+1))
= ((2h(h-py) + h²+1)/(h²+1), (py(h²-1)+2h)/(h²+1))

Parametrically: (-1 + t(2h(h-py)+h²+1)/(h²+1), t(py(h²-1)+2h)/(h²+1))

At x = 0: -1 + t(2h(h-py)+h²+1)/(h²+1) = 0
t = (h²+1)/(2h(h-py)+h²+1)

qy = t(py(h²-1)+2h)/(h²+1) = (py(h²-1)+2h)/(2h(h-py)+h²+1)

So Q = (0, (py(h²-1)+2h)/(2h(h-py)+h²+1))

Let me compute for h = 2, py = (8√3-6)/13:

py(h²-1)+2h = py·3 + 4 = 3(8√3-6)/13 + 4 = (24√3-18+52)/13 = (24√3+34)/13

2h(h-py)+h²+1 = 4(2-py)+5 = 4(2-(8√3-6)/13)+5 = 4(26-8√3+6)/13+5 = 4(32-8√3)/13+5 = (128-32√3)/13+5 = (128-32√3+65)/13 = (193-32√3)/13

qy = (24√3+34)/(193-32√3)

Numerically: 24√3 ≈ 41.569, 24√3+34 ≈ 75.569, 32√3 ≈ 55.426, 193-32√3 ≈ 137.574.
qy ≈ 75.569/137.574 ≈ 0.5493

So Q = (0, 0.5493), P = (0, 0.6043), R = (0, 0.6319).

PQ = |0.5493 - 0.6043| = 0.0550
QR = |0.5493 - 0.6319| = 0.0826

QR/PQ = 0.0826/0.0550 = 1.502

Hmm, that's approximately 3/2! Let me check with h = 3.

For h = 3, py = (6√3-3)/11:

py(h²-1)+2h = py·8 + 6 = 8(6√3-3)/11 + 6 = (48√3-24+66)/11 = (48√3+42)/11

2h(h-py)+h²+1 = 6(3-py)+10 = 6(3-(6√3-3)/11)+10 = 6(33-6√3+3)/11+10 = 6(36-6√3)/11+10 = (216-36√3)/11+10 = (216-36√3+110)/11 = (326-36√3)/11

qy = (48√3+42)/(326-36√3)

Numerically: 48√3 ≈ 83.138, 48√3+42 ≈ 125.138, 36√3 ≈ 62.354, 326-36√3 ≈ 263.646.
qy ≈ 125.138/263.646 ≈ 0.4747

P = (0, 0.6720), Q = (0, 0.4747), R = (0, 0.7719).

PQ = |0.4747 - 0.6720| = 0.1973
QR = |0.4747 - 0.7719| = 0.2972

QR/PQ = 0.2972/0.1973 ≈ 1.506

So for h=2: QR/PQ ≈ 1.502, for h=3: QR/PQ ≈ 1.506. These are close to 3/2 but not exactly equal. The small discrepancy might be due to rounding. Let me check more precisely.

For h = 2:
qy = (24√3+34)/(193-32√3)
py = (8√3-6)/13
r_y = 8(5√3-4)/59

PQ = py - qy (since py > qy)
= (8√3-6)/13 - (24√3+34)/(193-32√3)

Common denominator: 13(193-32√3)

= [(8√3-6)(193-32√3) - 13(24√3+34)] / [13(193-32√3)]

(8√3-6)(193-32√3) = 8·193√3 - 8·32·3 - 6·193 + 6·32√3 = 1544√3 - 768 - 1158 + 192√3 = 1736√3 - 1926

13(24√3+34) = 312√3 + 442

Numerator: 1736√3 - 1926 - 312√3 - 442 = 1424√3 - 2368

PQ = (1424√3 - 2368) / [13(193-32√3)]

QR = r_y - qy (since r_y > qy)
= 8(5√3-4)/59 - (24√3+34)/(193-32√3)

Common denominator: 59(193-32√3)

= [8(5√3-4)(193-32√3) - 59(24√3+34)] / [59(193-32√3)]

(5√3-4)(193-32√3) = 5·193√3 - 5·32·3 - 4·193 + 4·32√3 = 965√3 - 480 - 772 + 128√3 = 1093√3 - 1252

8(1093√3 - 1252) = 8744√3 - 10016

59(24√3+34) = 1416√3 + 2006

Numerator: 8744√3 - 10016 - 1416√3 - 2006 = 7328√3 - 12022

QR = (7328√3 - 12022) / [59(193-32√3)]

QR/PQ = (7328√3 - 12022) / [59(193-32√3)] · [13(193-32√3)] / (1424√3 - 2368)
= 13(7328√3 - 12022) / [59(1424√3 - 2368)]

Let me factor:
7328 = 16·458 = 16·2·229 = 32·229
12022 = 2·6011
1424 = 16·89
2368 = 32·74 = 32·2·37

7328√3 - 12022 = 2(3664√3 - 6011)
1424√3 - 2368 = 16(89√3 - 148)

QR/PQ = 13·2(3664√3 - 6011) / [59·16(89√3 - 148)]
= 26(3664√3 - 6011) / [944(89√3 - 148)]
= 13(3664√3 - 6011) / [472(89√3 - 148)]

Let me check if 3664√3 - 6011 = k(89√3 - 148
