# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Suppose Harvard Yard is a \(17 \times 17\) square. There are \(14\) dorms located on the perimeter of the Yard. If \(s\) is the minimum distance between two dorms, the maximum possible value of \(s\) can be expressed as \(a-\sqrt{b}\) where \(a, b\) are positive integers. Compute \(100a+b\).       — 题目文本
#   If two neighboring dorms are separated by a distance of more than \(s\), we can move them slightly closer together and adjust the other dorms, increasing \(s\). Therefore, in an optimal arrangement, the dorms form an equilateral \(14\)-gon with side length \(s\).

By scaling, the problem is now equivalent to finding the smallest \(a\) such that there exist \(14\) vertices on the boundary of an \(a \times a\) square that form an equilateral \(14\)-gon with side length \(1\). Such a \(14\)-gon must be centrally symmetric.

We know that \(x_{1}^{2}+y_{1}^{2}=x_{2}^{2}+y_{2}^{2}=1\) and \(x_{1}+x_{2}+3=y_{1}+y_{2}+2=a\). Moreover, if these equations are satisfied, then such a \(14\)-gon exists. We now consider the vectors \(\vec{v}_{1}=\left(x_{1}, y_{1}\right)\) and \(\vec{v}_{2}=\left(x_{2}, y_{2}\right)\). These unit vectors are in the first quadrant and add to \((a-3, a-2)\), which lies on the line \(y=x+1\).

Since \(\vec{v}_{1}\) and \(\vec{v}_{2}\) must lie in the first quadrant, from the above diagram we deduce that the minimum value of \(a\) occurs when one of \(\vec{v}_{1}, \vec{v}_{2}\) is \((0,1)\), meaning that \((a-3, a-2)=\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}+1\right)\). This means that \(a=\frac{\sqrt{2}}{2}+3\), so the maximum possible value of \(s\) is

\[
\frac{17}{\frac{\sqrt{2}}{2}+3}=17 \cdot \frac{3-\frac{\sqrt{2}}{2}}{17 / 2}=6-\sqrt{2}
\]

Thus, \(a = 6\) and \(b = 2\). Therefore, \(100a + b = 100 \times 6 + 2 = 602\).

\(\boxed{602}\)  — 标准解答
#   Let me solve this problem. Harvard Yard is a 17×17 square. 14 dorms on the perimeter. We want to maximize the minimum distance between any two dorms.

The perimeter of a 17×17 square. Let me think of the square as [0,17]×[0,17]. The perimeter has total length 4×17 = 68.

We need to place 14 points on the perimeter to maximize the minimum pairwise distance.

This is a packing problem on the perimeter of a square. The perimeter is a closed curve of length 68. If we place 14 points evenly spaced along the perimeter (by arc length), each would be 68/14 ≈ 4.857 apart. But the minimum distance is Euclidean, not arc length. Points on the same side that are arc-length 4.857 apart have Euclidean distance 4.857, but points near a corner might be closer in Euclidean distance than arc length.

Actually, the key issue: points near a corner on adjacent sides. If two points are on adjacent sides near a corner, their Euclidean distance could be less than their arc-length distance.

Let me think about this more carefully. The perimeter is a closed loop of length 68. We place 14 points. To maximize minimum Euclidean distance.

First, an upper bound: by arc length, the minimum arc-length distance between consecutive points (in arc-length order) is at most 68/14 = 34/7 ≈ 4.857. The Euclidean distance between two points is at most their arc-length distance (with equality only if they're on the same side). So the minimum Euclidean distance ≤ 34/7 ≈ 4.857.

But can we achieve something close? The issue is corners. If a point is placed near a corner on one side and another point near the same corner on the adjacent side, they could be close in Euclidean distance.

Actually, let me think about whether we can avoid corners entirely or place points strategically.

The answer is supposed to be a - √b. Let me think about what configuration gives this.

Let me consider placing points symmetrically. The square has 4-fold symmetry. 14 = 4×3 + 2, so we can't distribute perfectly evenly across 4 sides. Or maybe 14 points with some on corners.

Actually, let me think about this differently. A common approach: place points so that the minimum distance is determined by a specific pair.

Let me consider the structure. With 14 points on the perimeter of a 17×17 square, and the answer being a - √b.

Let me think about placing points at the corners and along edges. 

If we use the 4 corners, that's 4 points, leaving 10 for the edges. 10/4 = 2.5, so some edges get 2 and some get 3 interior points.

Actually, let me think about whether corners should be used. If a corner is used, the two adjacent points (one on each side) need to be at least distance s from the corner.

Let me try a symmetric approach. Place 2 points at opposite corners, or use all 4 corners.

Let me try: use all 4 corners (4 points), and place 10 points on the edges. Distribute as evenly as possible: each edge gets either 2 or 3 interior points. To be symmetric, we could have 2 edges with 3 and 2 edges with 2, but that breaks symmetry. 

Alternatively, don't use corners. Place points only on the interiors of edges.

Hmm, let me think about this more carefully with the answer format a - √b.

Let me consider a configuration where the minimum distance is achieved by a pair of points on adjacent sides near a corner.

Suppose on one side, points are at distance x from the corner, and on the adjacent side, a point is at distance y from the corner. The Euclidean distance between them is √(x² + y²). If x = y, this is x√2.

If we want to maximize the minimum distance, we need to balance the constraint from same-side distances and cross-corner distances.

Let me set up coordinates. Square [0,17]². 

Consider a symmetric placement. Let's say on each side we place some number of equally spaced points. 

With 14 points and 4-fold symmetry, we could have:
- 4 corners + 10 edge points (but 10 isn't divisible by 4)
- 0 corners + 14 edge points (14 isn't divisible by 4)
- 2 corners (opposite) + 12 edge points (12/4 = 3 per side, but the sides with corners have different structure)

Actually 2-fold symmetry might work better. Let me think about 14 = 2×7.

With 2-fold symmetry (180° rotation), we could have 7 points in each half.

Let me try a different approach. Let me think about what a - √b could be.

Common answers: 17 - √(something), or 34/2 - √(something)...

Let me think about the configuration where the binding constraint is between a point on one side and a point on the adjacent side, both at distance d from a corner. Then their distance is d√2. And on each side, the spacing between consecutive points is some value.

Let me try: no points at corners. On each side, place points symmetrically. 

With 14 points, let's try 2-fold symmetry. Place points so that on two opposite sides we have 4 points each and on the other two sides we have 3 points each. 4+4+3+3 = 14. With 2-fold symmetry (180° rotation), opposite sides have the same number.

For sides with 4 points: if the side has length 17 and 4 points, equally spaced, the spacing is 17/5 = 3.4 (if including endpoints) or 17/3 ≈ 5.67 (if not including endpoints, 4 points divide into 3 gaps... no, 4 points on a segment of length 17, if evenly spaced with equal gaps including to the corners: 17/5 = 3.4).

Hmm, this is getting complicated. Let me think about it more carefully.

Actually, let me reconsider. The problem says the answer is a - √b where a, b are positive integers. So the answer is of the form (integer) - √(integer).

Let me think about what configurations give such answers.

Consider placing points at the 4 corners and distributing the remaining 10 on the edges. If we place 2 or 3 on each edge...

Actually, let me try a specific configuration. Suppose we place points at all 4 corners, and on each side, we place 2 or 3 additional points. To maintain symmetry, let's say on each side we place either 2 or 3 points, with opposite sides having the same count. So 2 sides with 3 and 2 sides with 2: total = 4 + 2×3 + 2×2 = 4 + 6 + 4 = 14. ✓

For the sides with 3 interior points (plus 2 corners = 5 points on that side): the 4 gaps are equal, each 17/4 = 4.25.

For the sides with 2 interior points (plus 2 corners = 4 points on that side): the 3 gaps are equal, each 17/3 ≈ 5.667.

Now the minimum distance: on the 3-interior-point sides, consecutive points are 4.25 apart. On the 2-interior-point sides, consecutive points are 17/3 apart. 

But we also need to check cross-corner distances. At a corner where a 3-point side meets a 2-point side: the nearest point on the 3-point side is at distance 4.25 from the corner, and the nearest point on the 2-point side is at distance 17/3 from the corner. The distance between these two points is √(4.25² + (17/3)²) = √(18.0625 + 32.111) = √50.17 ≈ 7.08. That's large, not binding.

At a corner where two 3-point sides meet: nearest points are both 4.25 from the corner, distance = 4.25√2 ≈ 6.01. Still larger than 4.25.

At a corner where two 2-point sides meet: nearest points are both 17/3 from corner, distance = (17/3)√2 ≈ 8.02. Not binding.

So the minimum distance is 4.25 = 17/4. But 17/4 is not of the form a - √b. So this configuration doesn't give the right answer format.

Hmm. So the answer a - √b suggests that the binding constraint involves a cross-corner distance, which introduces a √2 factor, leading to irrational numbers.

Let me reconsider. Maybe we shouldn't place points at corners, and the binding constraint is between points on adjacent sides near a corner.

Let me try: no points at corners. Place all 14 points on the interiors of the 4 sides. With 2-fold symmetry: 4+4+3+3 = 14 (opposite sides have same count).

For a side with 4 points: let's say they're at positions x₁ < x₂ < x₃ < x₄ from one end. The minimum distance on this side is min(x₁, x₂-x₁, x₃-x₂, x₄-x₃, 17-x₄).

For a side with 3 points: similarly.

The cross-corner constraint: at a corner where a 4-point side meets a 3-point side, the nearest points to the corner are at distances x₁ (on the 4-point side) and y₁ (on the 3-point side) from the corner. Their Euclidean distance is √(x₁² + y₁²).

To maximize the minimum distance s, we want to balance all these constraints.

Let me set up the problem. Let's say the 4-point sides are the top and bottom, and the 3-point sides are the left and right.

On a 4-point side (length 17): points at positions a, a+d, a+2d, a+3d from the left end, where the spacing is d and the end gaps are a and 17-(a+3d) = 17-a-3d. For symmetry of the side (not necessarily required), a = 17-a-3d, so 2a+3d = 17. The minimum distance on this side is min(a, d).

On a 3-point side (length 17): points at positions b, b+e, b+2e from the bottom. End gaps: b and 17-b-2e. For side symmetry: 2b+2e = 17, i.e., b+e = 17/2. Minimum distance: min(b, e).

Cross-corner: at each corner, we have a point at distance a (or 17-a-3d) from the corner on the horizontal side, and a point at distance b (or 17-b-2e) from the corner on the vertical side. The Euclidean distance is √(a² + b²) or similar.

This is getting complex. Let me try to think about what gives a - √b.

The form a - √b typically arises when we have something like: the side length minus a diagonal. For instance, if on a side of length 17, we place points such that the gap from the corner is (17 - s)/2 or something, and the cross-corner distance gives √(x² + x²) = x√2, and we set x√2 = s, so x = s/√2, and then the side spacing gives another equation.

Let me try a cleaner approach. Suppose the binding constraints are:
1. Same-side spacing = s
2. Cross-corner distance = s, where two points are at distances p and q from the corner on adjacent sides, and √(p² + q²) = s.

If p = q (symmetric near corner), then p√2 = s, so p = s/√2.

Now, on a side of length 17 with k interior points, if the end gaps are p = s/√2 and the interior spacing is s, then:
2p + (k-1)s = 17
2(s/√2) + (k-1)s = 17
s(√2 + k - 1) = 17
s = 17/(√2 + k - 1)

For different k:
- k=3: s = 17/(√2 + 2) = 17(2-√2)/((2+√2)(2-√2)) = 17(2-√2)/(4-2) = 17(2-√2)/2 = 17 - 17√2/2. Not of the form a - √b with integer a, b.

Hmm, that doesn't work directly. Let me reconsider.

Actually, maybe the end gaps aren't both s/√2. Maybe one side has a different number of points.

Let me try: suppose on two opposite sides we have k points and on the other two we have m points, with k ≠ m. Then the end gaps might differ.

Let me try k=4, m=3 (so 4+4+3+3 = 14). 

On a 4-point side: end gaps p₁, interior spacing s, so 2p₁ + 3s = 17.
On a 3-point side: end gaps p₂, interior spacing s, so 2p₂ + 2s = 17.

Cross-corner at a corner where 4-point side meets 3-point side: √(p₁² + p₂²) = s.

From the equations:
p₁ = (17 - 3s)/2
p₂ = (17 - 2s)/2

Cross-corner: p₁² + p₂² = s²
((17-3s)/2)² + ((17-2s)/2)² = s²
(17-3s)² + (17-2s)² = 4s²
(289 - 102s + 9s²) + (289 - 68s + 4s²) = 4s²
578 - 170s + 13s² = 4s²
9s² - 170s + 578 = 0

s = (170 ± √(170² - 4·9·578))/(2·9) = (170 ± √(28900 - 20808))/18 = (170 ± √8092)/18

√8092 = √(4·2023) = 2√2023. Hmm, 2023 = 7·17² = 7·289. So √2023 = 17√7. So √8092 = 34√7.

s = (170 ± 34√7)/18 = (85 ± 17√7)/9

s = (85 - 17√7)/9 or s = (85 + 17√7)/9

(85 - 17√7)/9 ≈ (85 - 17·2.6458)/9 ≈ (85 - 44.98)/9 ≈ 40.02/9 ≈ 4.447

(85 + 17√7)/9 ≈ (85 + 44.98)/9 ≈ 129.98/9 ≈ 14.44 (too large, not feasible)

So s = (85 - 17√7)/9. This is not of the form a - √b with integer a, b (it's a fraction).

Hmm. So this symmetric configuration with equal spacing s on all sides doesn't give the right form.

Let me reconsider. Maybe the spacing isn't equal on all sides, or the configuration isn't symmetric in this way.

Wait, actually, maybe I should not assume the interior spacing equals s on all sides. The minimum distance is s, and we want to maximize it. The binding constraints could be different.

Let me reconsider the problem. Maybe the optimal configuration doesn't have the same-side spacing as the binding constraint. Maybe the binding constraint is only the cross-corner distance, and the same-side spacing is larger.

Let me try: on a 4-point side, the points are placed to maximize the minimum of (end gaps, interior spacings, cross-corner distances). If the cross-corner distance is the binding constraint, then the same-side spacings could be larger than s.

Actually, let me think about this differently. Let me consider that the minimum distance s is determined by cross-corner pairs, and we want to maximize s subject to fitting 14 points.

Let me try a configuration with 2-fold symmetry (180° rotation), with 4 points on two opposite sides and 3 on the other two, but where the points on each side are placed to maximize the minimum distance considering both same-side and cross-corner constraints.

Actually, let me try a completely different approach. Let me consider placing points only on 2 adjacent sides, or some other non-symmetric arrangement.

Hmm, but 14 points on the perimeter of a 17×17 square. Let me think about upper bounds more carefully.

The perimeter has length 68. 14 points, so average arc-length spacing is 68/14 ≈ 4.857. The minimum Euclidean distance is at most 68/14 = 34/7 ≈ 4.857 (since Euclidean distance ≤ arc-length distance for points on the same side, but for points on different sides, the Euclidean distance could be less than the arc-length distance).

Wait, actually, for any two points on the perimeter, the Euclidean distance is at most the arc-length distance (the shorter way around). This is because the perimeter is a convex curve, and for a convex curve, the chord length is at most the arc length. So the minimum Euclidean distance ≤ minimum arc-length distance between consecutive points ≤ 68/14 = 34/7.

But can we achieve 34/7? Only if all consecutive points (in arc-length order) are on the same straight side, which is impossible since we have 4 sides of length 17 and 14 points.

Actually, the issue is that some consecutive pairs will straddle a corner, and for those, the Euclidean distance is less than the arc-length distance.

Let me think about it more carefully. If we place 14 points with arc-length spacing 34/7, some points will be near corners. The points near a corner on adjacent sides will have Euclidean distance less than 34/7.

So the optimal configuration likely has some points at corners (to avoid the cross-corner penalty) or adjusts spacing near corners.

Let me reconsider the configuration with points at corners.

Configuration: 4 corners + 10 edge points. With 2-fold symmetry: 4 corners + 5+5 on opposite pairs. So 2 opposite sides have 3 edge points each, and the other 2 have 2 edge points each. Wait, 3+3+2+2 = 10. ✓

On a side with 3 edge points + 2 corners = 5 points: 4 gaps of 17/4 = 4.25 each.
On a side with 2 edge points + 2 corners = 4 points: 3 gaps of 17/3 each.

Cross-corner: at a corner, the nearest edge point on one side is at 4.25 (if 3-edge side) or 17/3 (if 2-edge side). But the corner itself is a point! So the cross-corner distance is from the corner to the nearest point on each adjacent side, which is 4.25 or 17/3. The distance from the corner to a point at distance d along one side is just d. So the minimum distance involving a corner is min(4.25, 17/3) = 4.25.

And the minimum same-side distance is 4.25 (on the 3-edge sides).

So the minimum distance is 4.25 = 17/4. Not of the form a - √b.

Hmm. So using corners gives 17/4, which is rational. The answer a - √b is irrational, so the optimal configuration must not use corners, and the binding constraint must be a cross-corner distance.

Let me go back to the no-corners configuration. The issue with my earlier attempt was that I assumed equal spacing s on all sides. Let me not assume that.

Let me try: no corners, 2-fold symmetry, 4+4+3+3 points on the 4 sides.

Let me label the sides: top and bottom have 4 points each, left and right have 3 points each.

On a 4-point side (say bottom, from (0,0) to (17,0)): points at positions x₁, x₂, x₃, x₄ from the left. End gaps: x₁ and 17-x₄. Interior gaps: x₂-x₁, x₃-x₂, x₄-x₃.

On a 3-point side (say left, from (0,0) to (0,17)): points at positions y₁, y₂, y₃ from the bottom. End gaps: y₁ and 17-y₃. Interior gap: y₃-y₂-y₁... wait, y₂-y₁ and y₃-y₂.

With 2-fold symmetry (180° rotation about center (8.5, 8.5)):
- Bottom side points at x₁, x₂, x₃, x₄ → top side points at 17-x₄, 17-x₃, 17-x₂, 17-x₁ (from left).
- Left side points at y₁, y₂, y₃ → right side points at 17-y₃, 17-y₂, 17-y₁ (from bottom).

For the bottom side to also have 2-fold symmetry (reflection about x=8.5): x₁ = 17-x₄, x₂ = 17-x₃. So points at x₁, x₂, 17-x₂, 17-x₁. End gap: x₁. Interior gaps: x₂-x₁, 17-2x₂, x₂-x₁. So gaps: x₁, x₂-x₁, 17-2x₂, x₂-x₁, x₁... wait, there are 4 points and 5 gaps (including end gaps to corners). No wait, the end gaps are to the corners, but corners aren't points. The gaps between consecutive points on the side are: x₁ (from corner to first point), x₂-x₁, (17-x₂)-x₂ = 17-2x₂... 

Hmm wait, the 4 points are at x₁, x₂, 17-x₂, 17-x₁. The gaps between consecutive points: x₂-x₁, (17-x₂)-x₂ = 17-2x₂, x₂-x₁. And the end gaps (to corners): x₁ and x₁ (by symmetry). So the gaps on this side are: x₁, x₂-x₁, 17-2x₂, x₂-x₁, x₁. But the end gaps are to the corners, not to other points. The minimum same-side distance is min(x₂-x₁, 17-2x₂).

For the left side with 3 points at y₁, y₂, y₃ with 2-fold symmetry: y₁ = 17-y₃, so y₃ = 17-y₁. And y₂ = 17-y₂, so y₂ = 8.5. Points at y₁, 8.5, 17-y₁. Gaps: y₁, 8.5-y₁, 8.5-y₁, y₁. Minimum same-side distance: min(y₁, 8.5-y₁).

Now, cross-corner distances. At corner (0,0):
- Nearest point on bottom: (x₁, 0), distance x₁ from corner.
- Nearest point on left: (0, y₁), distance y₁ from corner.
- Distance between these two: √(x₁² + y₁²).

At corner (17,0):
- Nearest point on bottom: (17-x₁, 0), distance x₁ from corner.
- Nearest point on right: (17, 17-y₃) = (17, y₁) [since y₃ = 17-y₁, 17-y₃ = y₁], distance y₁ from corner.
- Distance: √(x₁² + y₁²). Same by symmetry.

At corner (0,17):
- Nearest point on left: (0, 17-y₁), distance y₁ from corner.
- Nearest point on top: (x₁, 17) [since top is reflection of bottom, nearest point to (0,17) is at x₁ from left], distance x₁ from corner.
- Distance: √(x₁² + y₁²). Same.

So all cross-corner distances are √(x₁² + y₁²).

Now, we also need to check distances between points on adjacent sides that aren't the nearest to the corner. For example, the second nearest point on the bottom from corner (0,0) is at x₂, and the nearest on left is at y₁. Distance = √(x₂² + y₁²). Since x₂ > x₁, this is larger. Similarly, other cross-side distances are larger. But we should also check the distance between the nearest point on the bottom to corner (0,0) and the second nearest on the left, etc. These are all larger than √(x₁² + y₁²) since they involve larger distances from the corner.

Wait, but there's also the distance between a point on the bottom near corner (0,0) and a point on the left near corner (0,0). The closest such pair is (x₁, 0) and (0, y₁) with distance √(x₁² + y₁²). The next closest would be (x₂, 0) and (0, y₁) with distance √(x₂² + y₁²), or (x₁, 0) and (0, 8.5) with distance √(x₁² + 8.5²). Both are larger.

But wait, I also need to check distances between points on the bottom and points on the top (opposite sides), and points on the left and right. These are all at least 17 apart (since the sides are 17 apart), so they're not binding.

Also, I need to check distances between points on the bottom and points on the right side (not just near the shared corner). The closest would be near corner (17,0): (17-x₁, 0) and (17, y₁), distance √(x₁² + y₁²). Already accounted for.

What about a point on the bottom near (0,0) and a point on the right side? The right side is at x=17, so the distance is at least 17-x₁ ≈ 13+, not binding.

So the constraints are:
1. Same-side on 4-point sides: min(x₂-x₁, 17-2x₂) ≥ s
2. Same-side on 3-point sides: min(y₁, 8.5-y₁) ≥ s
3. Cross-corner: √(x₁² + y₁²) ≥ s

We want to maximize s. At the optimum, several of these will be tight.

Let me consider the case where constraints 1, 2, and 3 are all tight.

From constraint 2: min(y₁, 8.5-y₁) = s. If y₁ ≤ 8.5-y₁, i.e., y₁ ≤ 4.25, then y₁ = s. If y₁ > 4.25, then 8.5-y₁ = s, so y₁ = 8.5-s.

From constraint 1: min(x₂-x₁, 17-2x₂) = s. 

From constraint 3: x₁² + y₁² = s².

Case A: y₁ = s (so s ≤ 4.25).
Then from constraint 3: x₁² + s² = s², so x₁ = 0. But x₁ = 0 means a point at the corner, which contradicts our no-corners assumption. So this case doesn't work (unless we allow corner points, but then the answer is rational as we computed).

Case B: y₁ = 8.5 - s (so s < 4.25, since y₁ > 4.25 requires s < 4.25... wait, y₁ = 8.5-s and y₁ > 4.25 means s < 4.25).

From constraint 3: x₁² + (8.5-s)² = s²
x₁² = s² - (8.5-s)² = s² - 72.25 + 17s - s² = 17s - 72.25
x₁ = √(17s - 72.25)

For x₁ to be real: 17s > 72.25, s > 4.25. But we need s < 4.25 for this case. Contradiction!

So neither case works with all three constraints tight. This means my assumption about which constraints are tight is wrong.

Let me reconsider. Maybe constraint 2 is not tight, or constraint 1 is not tight.

Let me think about what's binding. The cross-corner distance √(x₁² + y₁²) is likely the binding constraint, along with one of the same-side constraints.

Let me consider: the binding constraints are the cross-corner distance and the same-side distance on the 4-point sides.

So: √(x₁² + y₁²) = s and min(x₂-x₁, 17-2x₂) = s, while min(y₁, 8.5-y₁) ≥ s.

For the 4-point side, let's say x₂-x₁ = s and 17-2x₂ ≥ s (or vice versa). Let's first try x₂-x₁ = s and 17-2x₂ ≥ s.

Then x₂ = x₁ + s, and 17-2(x₁+s) ≥ s, so 17-2x₁-2s ≥ s, 17-2x₁ ≥ 3s, x₁ ≤ (17-3s)/2.

Also, the end gap x₁ should be ≥ s? No, the end gap is to the corner, not to another point. The end gap doesn't directly constrain s (unless there's a point at the corner, which there isn't). Wait, but the end gap x₁ is the distance from the corner to the first point. There's no other point at the corner, so x₁ doesn't need to be ≥ s. However, x₁ appears in the cross-corner constraint.

Actually, wait. The same-side minimum distance on the 4-point side is min(x₂-x₁, 17-2x₂). The end gaps x₁ don't matter for same-side distance (since there's no point at the corner). So the same-side constraint is just min(x₂-x₁, 17-2x₂) ≥ s.

Similarly, on the 3-point side, the same-side minimum distance is min(8.5-y₁, y₁) [the gaps between consecutive points are 8.5-y₁, 8.5-y₁, and the end gaps are y₁ and y₁]. Wait, the 3 points are at y₁, 8.5, 17-y₁. The gaps between consecutive points: 8.5-y₁ and 8.5-y₁. The end gaps: y₁ and y₁. The same-side minimum distance is min(8.5-y₁, y₁). But the end gaps don't involve other points, so the same-side minimum distance between points is 8.5-y₁ (the gap between consecutive points). Wait, no: the minimum distance between any two points on the same side. The points are at y₁, 8.5, 17-y₁. Distances: 8.5-y₁ (between y₁ and 8.5), 8.5-y₁ (between 8.5 and 17-y₁), 17-2y₁ (between y₁ and 17-y₁). So the minimum same-side distance is 8.5-y₁ (assuming y₁ > 0, which it is).

So the same-side constraint on the 3-point side is 8.5-y₁ ≥ s, i.e., y₁ ≤ 8.5-s.

And the cross-corner constraint: √(x₁² + y₁²) = s (tight).

We want to maximize s. We have freedom to choose x₁, x₂, y₁.

The constraints:
- Cross-corner: x₁² + y₁² = s² (tight)
- 4-point side: x₂-x₁ ≥ s and 17-2x₂ ≥ s (at least one tight)
- 3-point side: 8.5-y₁ ≥ s
- x₁ ≥ 0, y₁ ≥ 0
- Also, x₁ < x₂ < 17-x₂ < 17-x₁ (ordering on the 4-point side)

To maximize s, we want to make the constraints as tight as possible. The 3-point side constraint y₁ ≤ 8.5-s and the cross-corner x₁² + y₁² = s².

We want to maximize s, so we want y₁ as large as possible (to allow x₁ to be small, which gives more room on the 4-point side). But y₁ ≤ 8.5-s.

If y₁ = 8.5-s (tight 3-point side), then x₁² = s² - (8.5-s)² = 17s - 72.25. Need s > 4.25.

But if s > 4.25, then y₁ = 8.5-s < 4.25, and the same-side distance on the 3-point side is 8.5-y₁ = s. OK.

Now, on the 4-point side: x₁ = √(17s-72.25). We need x₂-x₁ ≥ s and 17-2x₂ ≥ s.

From 17-2x₂ ≥ s: x₂ ≤ (17-s)/2.
From x₂-x₁ ≥ s: x₂ ≥ x₁+s.

So we need x₁+s ≤ (17-s)/2, i.e., x₁ ≤ (17-3s)/2.

√(17s-72.25) ≤ (17-3s)/2

Square both sides (need 17-3s > 0, i.e., s < 17/3 ≈ 5.67):
17s - 72.25 ≤ (17-3s)²/4
4(17s-72.25) ≤ (17-3s)²
68s - 289 ≤ 289 - 102s + 9s²
0 ≤ 9s² - 170s + 578

9s² - 170s + 578 ≥ 0

Discriminant: 170² - 4·9·578 = 28900 - 20808 = 8092 = 4·2023 = 4·7·289 = 4·7·17² = (34)²·7

s = (170 ± 34√7)/18 = (85 ± 17√7)/9

The quadratic 9s²-170s+578 ≥ 0 when s ≤ (85-17√7)/9 or s ≥ (85+17√7)/9.

(85-17√7)/9 ≈ (85-44.98)/9 ≈ 40.02/9 ≈ 4.447
(85+17√7)/9 ≈ 14.44 (too large)

So s ≤ (85-17√7)/9 ≈ 4.447.

But wait, we need s > 4.25 for x₁ to be real. And (85-17√7)/9 ≈ 4.447 > 4.25. ✓

So the maximum s in this configuration is s = (85-17√7)/9.

But this is (85-17√7)/9, which is not of the form a - √b with integer a, b. It's a fraction.

Hmm. So either my configuration is wrong, or the answer format allows for this to be rewritten.

(85-17√7)/9 = 85/9 - 17√7/9. Not a - √b with integer a, b.

Let me reconsider. Maybe I have the wrong configuration. Let me try different numbers of points per side.

What if we use 4+3+4+3 = 14 but with a different symmetry? Or 5+2+5+2 = 14? Or some other distribution?

Actually, wait. Let me reconsider whether the 2-fold symmetry with reflection (4-fold symmetry) is optimal. Maybe a configuration with only 2-fold symmetry (180° rotation, no reflection) is better.

Or maybe the optimal configuration doesn't have the same spacing on all sides.

Let me try a different distribution: 5+2+5+2 = 14 (opposite sides have 5 and 2).

On a 5-point side: 4 interior gaps + 2 end gaps = 17. If symmetric: 2a + 4d = 17 where a is end gap and d is interior spacing.
On a 2-point side: 1 interior gap + 2 end gaps = 17. If symmetric: 2b + e = 17 where b is end gap and e is interior spacing.

Same-side min on 5-point side: d (if d ≤ a) or a (if a ≤ d, but a is end gap to corner, not between points). Wait, the 5 points on a side of length 17, with end gaps a and interior spacing d: points at a, a+d, a+2d, a+3d, a+4d. End gap on right: 17-(a+4d) = a (by symmetry). So 2a+4d = 17. Same-side min distance: d (between consecutive points). The end gaps a are to the corner, not between points.

Same-side min on 2-point side: e (the single gap between the 2 points). With 2b+e = 17.

Cross-corner: √(a² + b²) = s.

Constraints:
- d ≥ s (5-point side)
- e ≥ s (2-point side)
- √(a² + b²) = s (cross-corner, tight)
- 2a + 4d = 17 → d = (17-2a)/4
- 2b + e = 17 → e = 17-2b

From d ≥ s: (17-2a)/4 ≥ s → a ≤ (17-4s)/2
From e ≥ s: 17-2b ≥ s → b ≤ (17-s)/2

Cross-corner: a² + b² = s².

To maximize s, set d = s and e = s (make same-side constraints tight):
a = (17-4s)/2, b = (17-s)/2.

a² + b² = s²:
((17-4s)/2)² + ((17-s)/2)² = s²
(17-4s)² + (17-s)² = 4s²
(289-136s+16s²) + (289-34s+s²) = 4s²
578 - 170s + 17s² = 4s²
13s² - 170s + 578 = 0

s = (170 ± √(28900-4·13·578))/(2·13) = (170 ± √(28900-30056))/26

28900-30056 = -1156 < 0. No real solution!

So we can't have both d = s and e = s simultaneously with the cross-corner constraint. This means the 5+2+5+2 configuration can't have all constraints tight simultaneously. The cross-corner distance is too large relative to the same-side distances, or vice versa.

Let me try not making both same-side constraints tight. Maybe only one is tight.

If d = s (5-point side tight) and e > s (2-point side not tight):
a = (17-4s)/2, b is free with b ≤ (17-s)/2 and a² + b² = s².

b = √(s² - a²) = √(s² - ((17-4s)/2)²).

We need b ≤ (17-s)/2 and e = 17-2b ≥ s, i.e., b ≤ (17-s)/2.

Also b ≥ 0, so s² ≥ ((17-4s)/2)², i.e., 4s² ≥ (17-4s)², 2s ≥ 17-4s (need 17-4s > 0), 6s ≥ 17, s ≥ 17/6 ≈ 2.83.

To maximize s, we want b as large as possible (to maximize the cross-corner distance? no, the cross-corner is fixed at s). Actually, we want to maximize s, and the constraint is b ≤ (17-s)/2. So:

√(s² - ((17-4s)/2)²) ≤ (17-s)/2

s² - ((17-4s)/2)² ≤ ((17-s)/2)²

4s² - (17-4s)² ≤ (17-s)²

4s² - (289-136s+16s²) ≤ 289-34s+s²

4s² - 289 + 136s - 16s² ≤ 289 - 34s + s²

-12s² + 136s - 289 ≤ 289 - 34s + s²

-13s² + 170s - 578 ≤ 0

13s² - 170s + 578 ≥ 0

Discriminant: 170² - 4·13·578 = 28900-30056 = -1156 < 0.

Since the discriminant is negative and the leading coefficient is positive, 13s²-170s+578 > 0 for all s. So the constraint is always satisfied! This means b ≤ (17-s)/2 is never binding when d = s.

So with d = s, we can increase s until some other constraint binds. What other constraint? We need b ≥ 0, which gives s ≥ 17/6. And we need the 2-point side to have e ≥ s, which is b ≤ (17-s)/2, always satisfied. And we need the 3-point side... wait, there's no 3-point side in this configuration.

Hmm, but we also need to check that the 2-point side's same-side distance e is actually ≥ s. We have e = 17-2b, and b = √(s²-a²). As s increases, a = (17-4s)/2 decreases (and eventually becomes 0 when s = 17/4 = 4.25), and b = √(s²-a²) increases. e = 17-2b decreases. At some point e = s.

Let me find when e = s: 17-2b = s, b = (17-s)/2. And b² = s²-a², a = (17-4s)/2.

((17-s)/2)² = s² - ((17-4s)/2)²

This is the same equation as before: 13s²-170s+578 = 0, which has no real solutions. So e > s always when d = s.

So what limits s? We need a ≥ 0: (17-4s)/2 ≥ 0, s ≤ 17/4 = 4.25. And b ≤ (17-s)/2, always satisfied. And we need the points to be in order, etc.

Wait, but if s can go up to 4.25 with d = s, what happens at s = 4.25? Then a = 0, meaning a point at the corner. And b = √(s²-0) = s = 4.25. e = 17-2(4.25) = 8.5. So the 2-point side has points at 4.25 and 12.75, with gap 8.5. And the 5-point side has points at 0, 4.25, 8.5, 12.75, 17 (i.e., at the corners and equally spaced). The minimum distance is 4.25.

But 4.25 = 17/4, same as before. And this is rational, not a - √b.

So the 5+2+5+2 configuration gives at most 17/4, same as the corner configuration. Not better.

Let me go back to the 4+4+3+3 configuration which gave s = (85-17√7)/9 ≈ 4.447. This is better than 17/4 = 4.25! So the 4+4+3+3 configuration is better.

But the answer (85-17√7)/9 is not of the form a - √b. Let me double-check my algebra.

Actually, wait. Let me reconsider. Maybe I need to not assume the 4-point side has reflection symmetry. With only 180° rotation symmetry, the 4-point side doesn't need to be symmetric about its midpoint.

Let me redo the 4+4+3+3 configuration with only 180° rotation symmetry (no reflection).

Bottom side: 4 points at x₁ < x₂ < x₃ < x₄.
Top side (180° rotation): points at 17-x₄, 17-x₃, 17-x₂, 17-x₁.
Left side: 3 points at y₁ < y₂ < y₃.
Right side (180° rotation): points at 17-y₃, 17-y₂, 17-y₁.

Now, the cross-corner distances:
At (0,0): nearest bottom point at x₁, nearest left point at y₁. Distance √(x₁²+y₁²).
At (17,0): nearest bottom point at 17-x₄, nearest right point at 17-y₃. Distance √((17-x₄)²+(17-y₃)²).
At (0,17): nearest top point at 17-x₄ (from left, so at position 17-x₄ from left = x₄ from right, distance from corner (0,17) is 17-x₄... wait, the top side goes from (0,17) to (17,17). A point at position 17-x₄ from the left is at (17-x₄, 17). Distance from corner (0,17) is 17-x₄. Nearest left point at 17-y₁ (from bottom, so at (0, 17-y₁)). Distance from corner (0,17) is y₁. Cross-corner distance: √((17-x₄)²+y₁²).
At (17,17): nearest top point at x₁ (from left, at (x₁, 17), distance from (17,17) is 17-x₁). Nearest right point at y₁ (from bottom, at (17, y₁), distance from (17,17) is 17-y₁). Cross-corner: √((17-x₁)²+(17-y₁)²).

By 180° rotation, corner (0,0) maps to (17,17), and (17,0) maps to (0,17). So:
√(x₁²+y₁²) = √((17-x₁)²+(17-y₁)²) → x₁²+y₁² = (17-x₁)²+(17-y₁)² → x₁²+y₁² = 289-34x₁+x₁²+289-34y₁+y₁² → 0 = 578-34(x₁+y₁) → x₁+y₁ = 17.

Similarly, √((17-x₄)²+(17-y₃)²) = √((17-x₄)²+y₁²) → (17-y₃)² = y₁² → 17-y₃ = y₁ (taking positive root) → y₃ = 17-y₁. But this is already implied by the 180° rotation: right side has point at 17-y₃ from bottom, and left side has point at y₁ from bottom. For the cross-corner at (17,0) and (0,17) to be equal, we need... actually, let me be more careful.

By 180° rotation, the configuration at corner (17,0) is the rotation of the configuration at corner (0,17). So their cross-corner distances are automatically equal. And the configuration at (0,0) is the rotation of (17,17). So we have two potentially different cross-corner distances:

d₁ = √(x₁²+y₁²) (at corners (0,0) and (17,17))
d₂ = √((17-x₄)²+(17-y₃)²) (at corners (17,0) and (0,17))

But wait, from 180° rotation, x₁+y₁ = 17 doesn't necessarily hold. Let me recheck.

180° rotation maps (x,y) to (17-x, 17-y). So a point at (x₁, 0) on the bottom maps to (17-x₁, 17) on the top. For this to be a point on the top side, we need 17-x₁ to be one of the top side positions. The top side positions are 17-x₄, 17-x₃, 17-x₂, 17-x₁. So 17-x₁ is indeed a top side position. ✓

A point at (0, y₁) on the left maps to (17, 17-y₁) on the right. Right side positions are 17-y₃, 17-y₂, 17-y₁. So 17-y₁ is a right side position. ✓

Now, corner (0,0) maps to (17,17) under 180° rotation. The nearest bottom point to (0,0) is at x₁, and the nearest left point to (0,0) is at y₁. Under rotation, the nearest top point to (17,17) is at 17-x₁ (from left, so at distance 17-(17-x₁) = x₁ from (17,17)), and the nearest right point to (17,17) is at 17-y₁ (from bottom, so at distance 17-(17-y₁) = y₁ from (17,17)). So the cross-corner distance at (17,17) is also √(x₁²+y₁²). ✓

Corner (17,0) maps to (0,17). The nearest bottom point to (17,0) is at 17-x₄ (distance x₄ from (17,0)... wait, the bottom point closest to (17,0) is the one with the largest x-coordinate, which is x₄. Its distance from (17,0) is 17-x₄. The nearest right point to (17,0) is at 17-y₃ (from bottom, so at (17, 17-y₃), distance from (17,0) is 17-y₃). Cross-corner distance: √((17-x₄)²+(17-y₃)²).

Under rotation, corner (0,17): nearest top point is at 17-x₄ (from left, at (17-x₄, 17), distance from (0,17) is 17-x₄). Nearest left point is at 17-y₁ (at (0, 17-y₁), distance from (0,17) is y₁). Wait, that doesn't match.

Hmm, let me recompute. At corner (0,17): the top side goes from (0,17) to (17,17). The nearest top point to (0,17) is the one with the smallest x-coordinate, which is 17-x₄ (since the top points are at 17-x₄, 17-x₃, 17-x₂, 17-x₁ and x₁ < x₂ < x₃ < x₄, so 17-x₄ < 17-x₃ < 17-x₂ < 17-x₁). So the nearest top point is at 17-x₄, distance 17-x₄ from (0,17).

The left side goes from (0,0) to (0,17). The nearest left point to (0,17) is the one with the largest y-coordinate, which is y₃. Distance from (0,17) is 17-y₃.

Cross-corner at (0,17): √((17-x₄)²+(17-y₃)²). Same as at (17,0). ✓

So we have two cross-corner distances:
d₁ = √(x₁²+y₁²) (at (0,0) and (17,17))
d₂ = √((17-x₄)²+(17-y₃)²) (at (17,0) and (0,17))

Now, we also need to check other cross-side distances. For example, the distance between the bottom point at x₁ and the left point at y₂ (the second point on the left side). This is √(x₁²+y₂²). Since y₂ > y₁, this is larger than d₁. Similarly for other non-nearest pairs.

But we also need to check distances between bottom points and right points, and top points and left points, etc. The closest such distance would be between a bottom point near (17,0) and a right point near (17,0), which is d₂. Other cross-side distances (bottom-left, top-right, etc.) are all larger.

Wait, I also need to check distances between points on the bottom and points on the left that aren't both nearest to the same corner. For example, bottom point at x₄ (near (17,0)) and left point at y₁ (near (0,0)). Distance = √(x₄²+y₁²). This is large since x₄ is close to 17. Not binding.

What about bottom point at x₂ and left point at y₁? Distance = √(x₂²+y₁²). Since x₂ > x₁, this is > d₁. Not binding (if d₁ is the minimum).

OK so the binding constraints are:
1. Same-side on bottom: min(x₂-x₁, x₃-x₂, x₄-x₃) ≥ s
2. Same-side on left: min(y₂-y₁, y₃-y₂) ≥ s
3. Cross-corner d₁ = √(x₁²+y₁²) ≥ s
4. Cross-corner d₂ = √((17-x₄)²+(17-y₃)²) ≥ s
5. End gaps don't directly constrain s (no points at corners)

We want to maximize s. At optimum, several constraints are tight.

Now, with 180° rotation but no reflection, we have more freedom. Let me consider the case where d₁ = d₂ = s (both cross-corner constraints tight) and the same-side constraints are also tight.

If d₁ = d₂ = s:
x₁² + y₁² = s²
(17-x₄)² + (17-y₃)² = s²

And same-side on bottom: let's say x₂-x₁ = x₃-x₂ = x₄-x₃ = s (equal spacing). Then x₂ = x₁+s, x₃ = x₁+2s, x₄ = x₁+3s.

Same-side on left: y₂-y₁ = y₃-y₂ = s (equal spacing). Then y₂ = y₁+s, y₃ = y₁+2s.

Now d₂: (17-x₁-3s)² + (17-y₁-2s)² = s².

And d₁: x₁² + y₁² = s².

Two equations, two unknowns (x₁, y₁), parameterized by s.

From d₁: x₁² + y₁² = s².
From d₂: (17-x₁-3s)² + (17-y₁-2s)² = s².

Let u = 17-x₁-3s, v = 17-y₁-2s. Then u²+v² = s² and x₁²+y₁² = s².

Also, x₁ = 17-3s-u, y₁ = 17-2s-v.

(17-3s-u)² + (17-2s-v)² = s²

And u²+v² = s².

Let me expand:
(17-3s)² - 2(17-3s)u + u² + (17-2s)² - 2(17-2s)v + v² = s²

(17-3s)² + (17-2s)² - 2(17-3s)u - 2(2s)v + (u²+v²) = s²

(17-3s)² + (17-2s)² - 2(17-3s)u - 2(17-2s)v + s² = s²

(17-3s)² + (17-2s)² = 2(17-3s)u + 2(17-2s)v

Let A = 17-3s, B = 17-2s. Then:
A² + B² = 2Au + 2Bv

And u²+v² = s², x₁ = A-u, y₁ = B-v, x₁²+y₁² = s²:
(A-u)² + (B-v)² = s²
A²-2Au+u² + B²-2Bv+v² = s²
A²+B² - 2(Au+Bv) + (u²+v²) = s²
A²+B² - (A²+B²) + s² = s² [using 2(Au+Bv) = A²+B² and u²+v²=s²]
0 = 0 ✓

So the two equations are consistent but don't uniquely determine u, v. We have:
u²+v² = s² (circle of radius s)
2Au + 2Bv = A²+B² (line)

The line intersects the circle. The distance from origin to the line is (A²+B²)/(2√(A²+B²)) = √(A²+B²)/2.

For intersection: √(A²+B²)/2 ≤ s, i.e., A²+B² ≤ 4s².

A²+B² = (17-3s)²+(17-2s)² = 289-102s+9s²+289-68s+4s² = 578-170s+13s².

4s² ≥ 578-170s+13s² → 0 ≥ 578-170s+9s² → 9s²-170s+578 ≤ 0.

This is the same quadratic as before! 9s²-170s+578 ≤ 0 when (85-17√7)/9 ≤ s ≤ (85+17√7)/9.

So the maximum s is (85+17√7)/9 ≈ 14.44, but that's way too large (s can't exceed 17). The minimum s for which the system has a solution is (85-17√7)/9 ≈ 4.447.

Wait, I think I'm confusing myself. The constraint is 9s²-170s+578 ≤ 0, which holds for s ∈ [(85-17√7)/9, (85+17√7)/9]. So s can be at most (85+17√7)/9 ≈ 14.44. But we also need all the points to fit on the sides, which requires x₁ ≥ 0, x₄ ≤ 17, y₁ ≥ 0, y₃ ≤ 17.

x₄ = x₁+3s ≤ 17 → x₁ ≤ 17-3s. For s ≈ 14.44, 17-3s < 0, so x₁ < 0, impossible.

So the real constraint is that all points fit. Let me add: x₁ ≥ 0, y₁ ≥ 0, x₄ = x₁+3s ≤ 17, y₃ = y₁+2s ≤ 17.

From x₁ ≥ 0 and x₁²+y₁² = s²: y₁ ≤ s.
From y₁ ≥ 0 and x₁²+y₁² = s²: x₁ ≤ s.
From x₄ ≤ 17: x₁ ≤ 17-3s, so s ≤ 17/3 ≈ 5.67 (if x₁ = 0).
From y₃ ≤ 17: y₁ ≤ 17-2s, so s ≤ 17/2 = 8.5 (if y₁ = 0).

The binding constraint is s ≤ 17/3 from the bottom side (4 points with spacing s need total length 3s ≤ 17, plus end gaps).

But we also need the cross-corner constraints. Let me think about what happens as s increases.

For the system to have a solution, we need 9s²-170s+578 ≤ 0, i.e., s ≥ (85-17√7)/9 ≈ 4.447. And we need x₁ ≥ 0, y₁ ≥ 0, x₁+3s ≤ 17, y₁+2s ≤ 17.

At s = (85-17√7)/9, the line is tangent to the circle, giving a unique solution. Let me check if the points fit.

Actually, I realize the issue. For s > (85-17√7)/9, the system has solutions (the line cuts the circle in two points). We want to maximize s, so we want the largest s for which all constraints are satisfied.

The constraints are:
- 9s²-170s+578 ≤ 0 (cross-corner system solvable)
- x₁ ≥ 0, y₁ ≥ 0 (points not beyond corners)
- x₁+3s ≤ 17, y₁+2s ≤ 17 (points fit on sides)

The cross-corner constraint gives s ≤ (85+17√7)/9 ≈ 14.44, which is not binding.
The fitting constraints give s ≤ 17/3 ≈ 5.67 (from x₁+3s ≤ 17 with x₁ ≥ 0).

But we also need x₁²+y₁² = s² with x₁ ≥ 0, y₁ ≥ 0, x₁ ≤ 17-3s, y₁ ≤ 17-2s.

The maximum of x₁²+y₁² subject to 0 ≤ x₁ ≤ 17-3s, 0 ≤ y₁ ≤ 17-2s is (17-3s)²+(17-2s)² (at the corner of the feasible region). We need this ≥ s²:

(17-3s)²+(17-2s)² ≥ s²
578-170s+13s² ≥ s²
12s²-170s+578 ≥ 0

Discriminant: 170²-4·12·578 = 28900-27744 = 1156 = 34².
s = (170±34)/24 = 204/24 = 8.5 or 136/24 = 17/3 ≈ 5.667.

So 12s²-170s+578 ≥ 0 when s ≤ 17/3 or s ≥ 8.5.

For s ≤ 17/3, this is satisfied. So the fitting constraint and the cross-corner constraint together give:

s ≤ 17/3 (fitting) and s ≥ (85-17√7)/9 (cross-corner solvable) and 9s²-170s+578 ≤ 0 (cross-corner solvable, i.e., s ≤ (85+17√7)/9).

Wait, I think I need to be more careful. The cross-corner constraint says that there exist x₁, y₁ with x₁²+y₁² = s² and (17-x₁-3s)²+(17-y₁-2s)² = s² and 0 ≤ x₁ ≤ 17-3s and 0 ≤ y₁ ≤ 17-2s.

The system x₁²+y₁² = s² and (17-3s-x₁)²+(17-2s-y₁)² = s² has solutions when 9s²-170s+578 ≤ 0 (i.e., the line intersects the circle). But we also need the solution to satisfy 0 ≤ x₁ ≤ 17-3s and 0 ≤ y₁ ≤ 17-2s.

Hmm, this is getting complicated. Let me think about it differently.

We want to maximize s. The constraints from the 4+4+3+3 configuration with equal spacing s on all sides and both cross-corner distances equal to s are:

1. x₁² + y₁² = s²
2. (17-3s-x₁)² + (17-2s-y₁)² = s²
3. 0 ≤ x₁ ≤ 17-3s
4. 0 ≤ y₁ ≤ 17-2s

From 1 and 2, the system is solvable when 9s²-170s+578 ≤ 0, i.e., s ∈ [(85-17√7)/9, (85+17√7)/9].

For s in this range, the solutions (x₁, y₁) lie on the intersection of the circle x₁²+y₁²=s² and the line 2(17-3s)x₁ + 2(17-2s)y₁ = (17-3s)²+(17-2s)².

We need to check if any solution satisfies constraints 3 and 4.

As s increases from (85-17√7)/9, the solutions move along the circle. At some point, the constraints 3, 4 may be violated.

Let me check at s = 17/3 (the fitting limit for the bottom side). Then 17-3s = 0, so x₁ = 0 (from constraint 3). Then y₁ = s = 17/3 from constraint 1. Check constraint 4: y₁ = 17/3 ≤ 17-2s = 17-34/3 = 17/3. ✓ (tight). Check constraint 2: (0)²+(17/3)² = (17/3)² = s². ✓.

So at s = 17/3, x₁ = 0, y₁ = 17/3. This means a point at the corner (0,0) on the bottom side! And the left side has its first point at y₁ = 17/3.

But x₁ = 0 means a point at corner (0,0). Is this allowed? The problem says dorms are on the perimeter, and corners are on the perimeter, so yes.

But if there's a point at (0,0), then the distance from this point to the nearest left-side point at (0, 17/3) is 17/3 ≈ 5.667. And the distance to the nearest bottom-side point at (s, 0) = (17/3, 0) is also 17/3. So the minimum distance is 17/3.

But 17/3 ≈ 5.667 > (85-17√7)/9 ≈ 4.447. So s = 17/3 is better!

Wait, but I need to check all constraints. At s = 17/3:
- Bottom side: points at 0, 17/3, 34/3, 17. So points at corners (0,0) and (17,0) and at 17/3 and 34/3. Spacing: 17/3 each.
- Top side (180° rotation): points at 0, 17/3, 34/3, 17 (same as bottom, since 17-x₄ = 17-17 = 0, 17-x₃ = 17-34/3 = 17/3, etc.). So top also has points at corners.
- Left side: points at 17/3, 17/3+17/3 = 34/3, 34/3+17/3 = 17. So points at (0, 17/3), (0, 34/3), (0, 17). The last is a corner!
- Right side: points at 0, 17/3, 34/3 (by 180° rotation: 17-y₃ = 0, 17-y₂ = 17-34/3 = 17/3, 17-y₁ = 17-17/3 = 34/3). So points at (17, 0), (17, 17/3), (17, 34/3). The first is a corner!

So the corners (0,0), (17,0), (0,17), (17,17) all have points. That's 4 corner points. Plus 2+2+2+2 = 8 edge points. Total: 12, not 14. Wait, let me recount.

Bottom: 4 points (0, 17/3, 34/3, 17) — 2 corners + 2 edge.
Top: 4 points (0, 17/3, 34/3, 17) — 2 corners + 2 edge.
Left: 3 points (17/3, 34/3, 17) — 1 corner + 2 edge.
Right: 3 points (0, 17/3, 34/3) — 1 corner + 2 edge.

Corners: (0,0) on bottom, (17,0) on bottom and right, (0,17) on top and left, (17,17) on top and left... wait, (17,17) is on top (at x=17) and right (at y=17). But right side points are at y = 0, 17/3, 34/3. y=17 is not among them. And (0,17) is on top (at x=0) and left (at y=17). Left side points are at y = 17/3, 34/3, 17. y=17 is among them. So (0,17) is a left side point and a top side point.

Let me list all distinct points:
Bottom: (0,0), (17/3, 0), (34/3, 0), (17, 0)
Top: (0, 17), (17/3, 17), (34/3, 17), (17, 17)
Left: (0, 17/3), (0, 34/3), (0, 17)
Right: (17, 0), (17, 17/3), (17, 34/3)

Distinct points: (0,0), (17/3,0), (34/3,0), (17,0), (0,17), (17/3,17), (34/3,17), (17,17), (0,17/3), (0,34/3), (17,17/3), (17,34/3).

That's 12 distinct points. But we need 14! The issue is that (17,0) appears on both bottom and right, and (0,17) appears on both top and left. So we have 12 distinct points, not 14.

So the configuration with s = 17/3 only gives 12 distinct points, not 14. We need 14 distinct points.

The problem is that at s = 17/3, the 4-point sides use corners, which coincide with points on the 3-point sides. So we lose 2 points to coincidence.

So we need s < 17/3 to have 14 distinct points (no coincidences at corners). As s decreases from 17/3, the points move away from corners and we get 14 distinct points.

But we want to maximize s. So the optimal s is just below 17/3? No, because as s decreases, we need to check the cross-corner constraint.

Actually, wait. At s = 17/3, we have 12 points. We need 14. So we need to either add 2 more points (which would decrease the minimum distance) or use a different configuration.

Hmm, I think the issue is that my 4+4+3+3 distribution with equal spacing doesn't work at s = 17/3 because of corner coincidences. Let me reconsider.

Maybe the optimal configuration is different. Let me think about this problem from scratch.

We have 14 points on the perimeter of a 17×17 square. We want to maximize the minimum pairwise distance.

Let me think about it as placing 14 points on a closed curve of length 68. The curve has 4 "corners" where the direction changes by 90°.

Key insight: for points on the same side, the Euclidean distance equals the arc-length distance. For points on adjacent sides near a corner, the Euclidean distance is less than the arc-length distance (it's the hypotenuse of a right triangle).

To maximize the minimum Euclidean distance, we want to avoid having points close to corners on adjacent sides (which would give small Euclidean distances). One way is to place points at corners (so the "cross-corner" issue becomes a same-side issue). Another way is to keep points away from corners.

Let me think about the trade-off. If we place points at corners, we "use up" corner positions but avoid cross-corner penalties. If we don't place points at corners, we need to keep points away from corners, which wastes perimeter length.

Let me consider the configuration with all 4 corners occupied. Then we have 10 points on the edges. The minimum distance is determined by the spacing on the edges and the distance from corner points to nearby edge points.

With 4 corners + 10 edge points, and 2-fold symmetry: 5+5 edge points on opposite pairs. Say 3 on two opposite sides and 2 on the other two.

3-edge side: 5 points total (2 corners + 3 edge), 4 gaps of 17/4 = 4.25.
2-edge side: 4 points total (2 corners + 2 edge), 3 gaps of 17/3 ≈ 5.667.

Minimum distance: 4.25 (on the 3-edge sides). Cross-corner: at a corner, the nearest edge point is at 4.25 (on the 3-edge side) or 17/3 (on the 2-edge side). The distance from the corner to the nearest edge point is 4.25 or 17/3, so the minimum is 4.25.

But we should also check the distance between the nearest edge point on one side and the nearest edge point on the adjacent side, both near the same corner. At a corner where a 3-edge side meets a 2-edge side: the edge points are at 4.25 and 17/3 from the corner. Distance = √(4.25² + (17/3)²) = √(18.0625 + 32.111) = √50.17 ≈ 7.08. Not binding.

At a corner where two 3-edge sides meet: edge points at 4.25 and 4.25 from corner. Distance = 4.25√2 ≈ 6.01. Not binding (since 4.25 < 6.01).

At a corner where two 2-edge sides meet: edge points at 17/3 and 17/3. Distance = (17/3)√2 ≈ 8.02. Not binding.

So minimum distance = 4.25 = 17/4. This is the corner configuration.

Now, the no-corner configuration with 4+4+3+3 gave s ≈ 4.447, which is better than 4.25. But it's not of the form a - √b.

Hmm, let me reconsider. Maybe I need to not require equal spacing on all sides. Let me go back to the 4+4+3+3 configuration with 180° rotation symmetry but without requiring equal spacing or both cross-corner distances to be equal.

Let me parameterize differently. On the bottom side, 4 points at x₁ < x₂ < x₃ < x₄ with spacings d₁ = x₂-x₁, d₂ = x₃-x₂, d₃ = x₄-x₃. End gaps: x₁ and 17-x₄.

On the left side, 3 points at y₁ < y₂ < y₃ with spacings e₁ = y₂-y₁, e₂ = y₃-y₂. End gaps: y₁ and 17-y₃.

180° rotation: top has points at 17-x₄, 17-x₃, 17-x₂, 17-x₁. Right has points at 17-y₃, 17-y₂, 17-y₁.

Constraints (minimum distance s):
- Same-side bottom: min(d₁, d₂, d₃) ≥ s
- Same-side left: min(e₁, e₂) ≥ s
- Cross-corner at (0,0): √(x₁² + y₁²) ≥ s
- Cross-corner at (17,0): √((17-x₄)² + (17-y₃)²) ≥ s
- Cross-corner at (0,17): √((17-x₄)² + (17-y₃)²) ≥ s [same as (17,0) by symmetry]

Wait, I computed earlier that (0,17) and (17,0) have the same cross-corner distance. And (0,0) and (17,17) have the same. So two cross-corner constraints.

- Other cross-side distances (non-nearest to same corner): all larger, not binding.

To maximize s, we want to make the binding constraints tight. The question is which constraints are binding.

Let me consider the case where:
- Same-side bottom: d₁ = d₂ = d₃ = s (equal spacing, all tight)
- Same-side left: e₁ = e₂ = s (equal spacing, all tight)
- Cross-corner at (0,0): √(x₁² + y₁²) = s (tight)
- Cross-corner at (17,0): √((17-x₄)² + (17-y₃)²) = s (tight)

This is the case I analyzed before, giving s = (85-17√7)/9 or s = (85+17√7)/9 (too large).

But maybe not all same-side constraints need to be tight. Maybe only the cross-corner constraints and some same-side constraints are tight.

Let me try: cross-corner at (0,0) is tight, cross-corner at (17,0) is NOT tight (i.e., the points near (17,0) are farther apart), and same-side constraints are tight.

If only cross-corner at (0,0) is tight: √(x₁² + y₁²) = s.

Same-side bottom: d₁ = d₂ = d₃ = s. So x₂ = x₁+s, x₃ = x₁+2s, x₄ = x₁+3s.
Same-side left: e₁ = e₂ = s. So y₂ = y₁+s, y₃ = y₁+2s.

Cross-corner at (17,0): (17-x₁-3s)² + (17-y₁-2s)² ≥ s². (Not tight.)

We want to maximize s. The constraints are:
1. x₁² + y₁² = s² (tight cross-corner at (0,0))
2. x₁ ≥ 0, y₁ ≥ 0 (points not beyond corners)
3. x₁ + 3s ≤ 17 (bottom points fit) → x₁ ≤ 17-3s
4. y₁ + 2s ≤ 17 (left points fit) → y₁ ≤ 17-2s
5. (17-x₁-3s)² + (17-y₁-2s)² ≥ s² (cross-corner at (17,0) not tight)

From 1: x₁ = s·cos(θ), y₁ = s·sin(θ) for some θ ∈ [0, π/2].

From 3: s·cos(θ) ≤ 17-3s → cos(θ) ≤ (17-3s)/s = 17/s - 3.
From 4: s·sin(θ) ≤ 17-2s → sin(θ) ≤ 17/s - 2.

For these to have a solution, we need (17/s-3)² + (17/s-2)² ≥ 1 (since cos²θ + sin²θ = 1 and both cos θ and sin θ are at most those bounds). Actually, we need cos θ ≤ 17/s-3 and sin θ ≤ 17/s-2, and cos²θ + sin²θ = 1. This requires (17/s-3)² + (17/s-2)² ≥ 1 (so that the rectangle [0, 17/s-3] × [0, 17/s-2] intersects the unit circle).

Also, 17/s-3 ≥ 0 → s ≤ 17/3, and 17/s-2 ≥ 0 → s ≤ 17/2.

Let t = 17/s. Then (t-3)² + (t-2)² ≥ 1 → 2t²-10t+13 ≥ 1 → 2t²-10t+12 ≥ 0 → t²-5t+6 ≥ 0 → (t-2)(t-3) ≥ 0 → t ≤ 2 or t ≥ 3.

Since t = 17/s and s ≤ 17/3, t ≥ 3. So t ≥ 3, i.e., s ≤ 17/3. And the constraint (t-3)²+(t-2)² ≥ 1 is satisfied for t ≥ 3 (equality at t = 3, i.e., s = 17/3).

So the fitting constraints allow s up to 17/3. Now check constraint 5:

(17-x₁-3s)² + (17-y₁-2s)² ≥ s²

Let u = 17-x₁-3s = 17-s·cos(θ)-3s = 17-s(3+cos θ) and v = 17-y₁-2s = 17-s(2+sin θ).

u² + v² ≥ s²
(17-s(3+cos θ))² + (17-s(2+sin θ))² ≥ s²

At s = 17/3, t = 3, and from the fitting constraint (t-3)²+(t-2)² = 1, so cos θ = 0, sin θ = 1 (i.e., θ = π/2, x₁ = 0, y₁ = s = 17/3).

Then u = 17-0-17 = 0, v = 17-17/3-34/3 = 17-17 = 0. So u²+v² = 0 < s². Constraint 5 is violated!

So at s = 17/3, the cross-corner at (17,0) is too small. We need to reduce s.

Let me find the maximum s where constraint 5 is satisfied. We need:

(17-s(3+cos θ))² + (17-s(2+sin θ))² ≥ s²

with cos²θ + sin²θ = 1, 0 ≤ cos θ ≤ 17/s-3, 0 ≤ sin θ ≤ 17/s-2.

To maximize s, we want to choose θ to maximize the LHS. The LHS is maximized when u and v are as large as possible, i.e., when cos θ and sin θ are as small as possible. But cos θ and sin θ are constrained by cos²θ+sin²θ=1.

Actually, to maximize u²+v² = (17-s(3+cosθ))²+(17-s(2+sinθ))², we want to minimize s(3+cosθ) and s(2+sinθ), i.e., minimize cosθ and sinθ. But cos²θ+sin²θ=1, so we can't minimize both. 

The LHS is a function of θ. Let me compute it:

f(θ) = (17-s(3+cosθ))² + (17-s(2+sinθ))²

= (17-3s)² - 2(17-3s)s·cosθ + s²cos²θ + (17-2s)² - 2(17-2s)s·sinθ + s²sin²θ

= (17-3s)² + (17-2s)² + s² - 2s[(17-3s)cosθ + (17-2s)sinθ]

= 578-170s+13s² - 2s[(17-3s)cosθ + (17-2s)sinθ]

To maximize f(θ), we minimize (17-3s)cosθ + (17-2s)sinθ. This is of the form A·cosθ + B·sinθ where A = 17-3s, B = 17-2s. The minimum over θ is -√(A²+B²) (achieved when (cosθ, sinθ) is in the direction of (-A, -B), i.e., θ in the third quadrant). But we need cosθ ≥ 0 and sinθ ≥ 0 (first quadrant).

In the first quadrant, the minimum of A·cosθ + B·sinθ (with A, B > 0 for s < 17/3) is achieved at the endpoints: either cosθ = 0, sinθ = 1 (giving B) or cosθ = 1, sinθ = 0 (giving A), whichever is smaller. Since A = 17-3s < B = 17-2s for s > 0, the minimum is A = 17-3s, achieved at θ = 0 (cosθ = 1, sinθ = 0, i.e., x₁ = s, y₁ = 0).

But y₁ = 0 means a point at the corner (0,0) on the left side. Hmm, that's a corner point.

Wait, but we also need sinθ ≤ 17/s-2 and cosθ ≤ 17/s-3. At θ = 0: cosθ = 1 ≤ 17/s-3 requires s ≤ 17/4 = 4.25. And sinθ = 0 ≤ 17/s-2 always. So for s ≤ 4.25, we can use θ = 0.

For s > 4.25, cosθ = 1 > 17/s-3, so θ = 0 is not feasible. The minimum of A·cosθ+B·sinθ in the feasible region is achieved at the boundary cosθ = 17/s-3 (i.e., x₁ = 17-3s, the maximum allowed). Then sinθ = √(1-(17/s-3)²) and y₁ = s·sinθ.

This is getting complicated. Let me try a different approach.

Let me consider the possibility that the optimal configuration has a different structure. Maybe not 4+4+3+3.

Actually, let me reconsider the problem. The answer is a - √b. Let me think about what values of a and b make sense.

If the answer involves √2 (from cross-corner distances with equal distances from the corner), then a - √b could be something like 17 - √(something) or a multiple.

Let me try the configuration where the binding constraint is between two points on adjacent sides at equal distance d from a corner, giving distance d√2 = s, so d = s/√2. And the same-side spacing is also s.

On a side with k interior points (no corners), with end gaps d = s/√2 and interior spacing s:
2d + (k-1)s = 17
2(s/√2) + (k-1)s = 17
s√2 + (k-1)s = 17
s(√2 + k - 1) = 17
s = 17/(k-1+√2)

For this to give a - √b, we need 17/(k-1+√2) = 17(k-1-√2)/((k-1)²-2) = a - √b.

For k = 3: s = 17/(2+√2) = 17(2-√2)/(4-2) = 17(2-√2)/2 = 17 - 17√2/2. Not integer a, b.

For k = 4: s = 17/(3+√2) = 17(3-√2)/(9-2) = 17(3-√2)/7 = 51/7 - 17√2/7. Not integer a, b.

Hmm, these don't give integer a, b. The issue is the denominator.

What if the end gaps are not s/√2 but something else? Let me think about configurations where the end gaps on different sides are different.

Let me try: on two opposite sides, k points with end gaps p and interior spacing s. On the other two sides, m points with end gaps q and interior spacing s. Cross-corner: √(p²+q²) = s.

2p + (k-1)s = 17 → p = (17-(k-1)s)/2
2q + (m-1)s = 17 → q = (17-(m-1)s)/2

p² + q² = s²:
((17-(k-1)s)/2)² + ((17-(m-1)s)/2)² = s²
(17-(k-1)s)² + (17-(m-1)s)² = 4s²

Let a = k-1, b = m-1.
(17-as)² + (17-bs)² = 4s²
289-34as+a²s² + 289-34bs+b²s² = 4s²
(a²+b²-4)s² - 34(a+b)s + 578 = 0

For 4+4+3+3: k=4, m=3, a=3, b=2.
(9+4-4)s² - 34·5·s + 578 = 0
9s² - 170s + 578 = 0
s = (170 ± √(28900-20808))/18 = (170 ± √8092)/18 = (170 ± 34√7)/18 = (85 ± 17√7)/9

As before. s = (85-17√7)/9. Not a - √b.

For 5+5+2+2: k=5, m=2, a=4, b=1.
(16+1-4)s² - 34·5·s + 578 = 0
13s² - 170s + 578 = 0
Discriminant: 28900-30056 = -1156 < 0. No real solution.

For 4+4+4+2: k=4, m=2, a=3, b=1. But this is 4+4+4+2 = 14 with 2-fold symmetry? Opposite sides have same count: 4+2+4+2 = 14. So k=4, m=2.
(9+1-4)s² - 34·4·s + 578 = 0
6s² - 136s + 578 = 0
3s² - 68s + 289 = 0
s = (68 ± √(4624-3468))/6 = (68 ± √1156)/6 = (68 ± 34)/6
s = 102/6 = 17 or s = 34/6 = 17/3.

s = 17 is too large (can't have minimum distance 17 on a 17×17 square with 14 points). s = 17/3 ≈ 5.667.

But as we saw, s = 17/3 leads to corner coincidences (12 points, not 14). So this doesn't work for 14 distinct points.

For 3+3+4+4: same as 4+4+3+3.

For 5+3+5+3: k=5, m=3, a=4, b=2.
(16+4-4)s² - 34·6·s + 578 = 0
16s² - 204s + 578 = 0
8s² - 102s + 289 = 0
s = (102 ± √(10404-9248))/16 = (102 ± √1156)/16 = (102 ± 34)/16
s = 136/16 = 8.5 or s = 68/16 = 4.25.

s = 4.25 = 17/4 (rational, same as corner config). s = 8.5 too large.

For 6+1+6+1: k=6, m=1, a=5, b=0.
(25+0-4)s² - 34·5·s + 578 = 0
21s² - 170s + 578 = 0
Discriminant: 28900-4·21·578 = 28900-48552 < 0. No real solution.

For 3+4+3+4: same as 4+4+3+3.

For 5+2+5+2: already done, no real solution.

For 4+3+4+3: same as 4+4+3+3.

Hmm, so the only configurations with 2-fold symmetry (opposite sides same count) that give real solutions are:
- 4+4+3+3: s = (85-17√7)/9 ≈ 4.447
- 4+4+4+2: s = 17/3 ≈ 5.667 (but only 12 distinct points)
- 5+5+3+3: s = 17/4 = 4.25 or s = 8.5 (too large)

Wait, 5+5+3+3 = 16, not 14. Let me recheck. 5+5+2+2 = 14, 4+4+3+3 = 14, 4+4+4+2 = 14, 3+3+4+4 = 14, 5+3+5+3 = 16. 

Hmm, 5+3+5+3 = 16, not 14. Let me recalculate. For 14 points with 2-fold symmetry (opposite sides equal): possible distributions are (a, b, a, b) with 2a+2b = 14, so a+b = 7. Options: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).

So: 1+6+1+6, 2+5+2+5, 3+4+3+4, 4+3+4+3, 5+2+5+2, 6+1+6+1.

I already computed:
- 3+4+3+4 (= 4+4+3+3): s = (85-17√7)/9 ≈ 4.447
- 4+2+4+2 (= 4+4+2+2): s = 17/3 (12 points) or 17 (too large)
- 5+2+5+2: no real solution
- 2+5+2+5: same as 5+2+5+2
- 1+6+1+6: k=1, m=6, a=0, b=5. (0+25-4)s²-34·5·s+578 = 0 → 21s²-170s+578 = 0, discriminant < 0.
- 6+1+6+1: same as 1+6+1+6.

So the best real solution is 3+4+3+4 with s = (85-17√7)/9 ≈ 4.447.

But this isn't of the form a - √b! Let me re-examine.

(85-17√7)/9. Let me see if this can be written as a - √b.

a - √b = (85-17√7)/9. If a = 85/9, that's not an integer. So this doesn't work.

Hmm. Maybe my approach is wrong. Let me reconsider the problem.

Wait, maybe the configuration doesn't have 2-fold symmetry. Or maybe the optimal configuration uses corners in a different way.

Let me reconsider. Maybe the optimal configuration has some points at corners and some not, with a non-symmetric arrangement.

Actually, let me reconsider the 4+4+2+2 configuration (s = 17/3) more carefully. The issue was that at s = 17/3, we get 12 distinct points because of corner coincidences. But what if we don't require equal spacing? Maybe we can have 14 distinct points with minimum distance close to 17/3.

Actually, the 4+4+2+2 configuration has 4+4+2+2 = 12 points on the sides (not counting corners separately). Wait, no. In the 4+4+2+2 configuration, the 4-point sides have 4 points each and the 2-point sides have 2 points each, totaling 12. But we need 14. So 4+4+2+2 only gives 12 points. That's wrong.

Oh wait, I think I miscounted. Let me recheck. 4+4+2+2 = 12, not 14. So this distribution doesn't have 14 points. I made an error earlier.

Let me redo. For 14 points with 2-fold symmetry (opposite sides equal): 2a+2b = 14, a+b = 7. The distributions are (a,b) = (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). These give 2+12, 4+10, 6+8, 8+6, 10+4, 12+2 total points. All sum to 14. ✓

So 3+4 means 3 on one pair of opposite sides and 4 on the other, giving 6+8 = 14. ✓
4+2 means 4 on one pair and 2 on the other, giving 8+4 = 12. ✗ Wait, 2·4 + 2·2 = 8+4 = 12 ≠ 14.

Hmm, 2a+2b = 14 → a+b = 7. If a=4, b=3: 2·4+2·3 = 8+6 = 14. ✓
If a=4, b=2: 2·4+2·2 = 8+4 = 12 ≠ 14. So (4,2) is not valid since 4+2 = 6 ≠ 7.

I made an error. Let me redo. a+b = 7, so the valid pairs are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).

For (3,4): k=4, m=3 (or k=3, m=4). I computed s = (85-17√7)/9.
For (2,5): k=5, m=2. I computed discriminant < 0.
For (1,6): k=6, m=1. Discriminant < 0.

So the only valid 2-fold symmetric configuration with a real solution is (3,4), giving s = (85-17√7)/9.

But this isn't a - √b. So either:
1. The optimal configuration doesn't have 2-fold symmetry.
2. The optimal configuration has a different structure (e.g., using corners).
3. I'm making an error somewhere.

Let me reconsider. Maybe the optimal configuration uses some corners but not all, or has a different symmetry.

Actually, let me reconsider the problem. Maybe the answer involves a different kind of configuration. Let me think about what a - √b could be.

If a and b are positive integers, and the answer is around 4.447, then a - √b ≈ 4.447. So a ≈ 4.447 + √b. For b = 1: a ≈ 5.447, not integer. b = 4: a ≈ 6.447, not integer. b = 9: a ≈ 7.447, not integer. b = 16: a ≈ 8.447, not integer. b = 25: a ≈ 9.447, not integer.

Hmm, none of these work for s ≈ 4.447. So maybe the answer isn't (85-17√7)/9.

Let me reconsider. Maybe the optimal configuration is different from what I've been trying.

Let me think about configurations without any symmetry. Or configurations with a different kind of symmetry.

Actually, let me reconsider the problem. Maybe I should think about it as placing 14 points on the perimeter, where the perimeter is a 1D curve, and the distance is Euclidean.

Let me think about the problem differently. The perimeter has 4 sides of length 17. Let me "unfold" the perimeter into a line segment of length 68, with the understanding that the Euclidean distance between two points depends on their positions on the perimeter.

Actually, let me think about a specific configuration that might give a - √b.

Consider placing points at the 4 corners and 10 other points. But we saw this gives 17/4.

What if we place points at only 2 corners (opposite corners) and 12 other points?

With 2 corners (say (0,0) and (17,17)) and 12 edge points. By 2-fold symmetry (180° rotation about (8.5, 8.5)), the 12 edge points are paired. So 6 on each "half".

The sides: bottom (0,0) to (17,0), right (17,0) to (17,17), top (17,17) to (0,17), left (0,17) to (0,0).

(0,0) is a corner point. (17,17) is a corner point. The bottom side has (0,0) at one end. The left side has (0,0) at one end. The top side has (17,17) at one end. The right side has (17,17) at one end.

With 180° rotation symmetry, if we place p points on the bottom (excluding (0,0)), then we place p points on the top (excluding (17,17)). If we place q points on the right (excluding (17,17)), then q on the left (excluding (0,0)). Total: 2 + 2p + 2q = 14, so p + q = 6.

Options: (p,q) = (0,6), (1,5), (2,4), (3,3), (4,2), (5,1), (6,0).

Let me try (p,q) = (3,3): 3 points on each side (excluding the corner point).

Bottom: (0,0) + 3 points at x₁ < x₂ < x₃. By 180° rotation, top has (17,17) + 3 points at 17-x₃, 17-x₂, 17-x₁.
Right: (17,17) + 3 points at y₁ < y₂ < y₃ (from (17,0) upward). By rotation, left has (0,0) + 3 points at 17-y₃, 17-y₂, 17-y₁ (from (0,0) upward).

Wait, I need to be more careful. The right side goes from (17,0) to (17,17). (17,17) is a corner point. So the 3 right-side points are at distances y₁, y₂, y₃ from (17,0), with y₃ < 17. By 180° rotation, the left side has points at (0, 17-y₃), (0, 17-y₂), (0, 17-y₁) (from (0,0), these are at distances 17-y₃, 17-y₂, 17-y₁ from (0,0)). And (0,0) is a corner point on the left.

So on the bottom: points at 0, x₁, x₂, x₃ (from (0,0)). Spacings: x₁, x₂-x₁, x₃-x₂, 17-x₃ (end gap to (17,0)).
On the left: points at 0, 17-y₃, 17-y₂, 17-y₁ (from (0,0)). Spacings: 17-y₃, y₃-y₂, y₂-y₁, y₁ (end gap to (0,17)).

Cross-corner at (0,0): the corner point (0,0) is shared by bottom and left. The nearest bottom point is at x₁, distance x₁. The nearest left point is at 17-y₃, distance 17-y₃. These are same-side distances from the corner point, so the minimum distance involving (0,0) is min(x₁, 17-y₃).

Cross-corner at (17,0): no corner point here. Nearest bottom point: x₃, distance 17-x₃. Nearest right point: y₁, distance y₁. Cross-corner distance: √((17-x₃)² + y₁²).

Cross-corner at (0,17): no corner point here. Nearest left point: 17-y₁, distance y₁ (from (0,17)). Nearest top point: 17-x₃ (from (0,17) along the top, the nearest is at 17-x₃ from the left, so distance 17-x₃ from (0,17)). Wait, the top goes from (0,17) to (17,17). The top points are at 17-x₃, 17-x₂, 17-x₁, 17 (from left). Nearest to (0,17) is at 17-x₃, distance 17-x₃. Cross-corner: √((17-x₃)² + y₁²). Same as (17,0) by symmetry. ✓

Cross-corner at (17,17): corner point. Nearest top point: 17-x₁, distance x₁ (from (17,17)). Nearest right point: 17-y₁, distance 17-y₁... wait, the right side points are at y₁, y₂, y₃ from (17,0). (17,17) is at distance 17 from (17,0). Nearest right point to (17,17) is at y₃, distance 17-y₃. So the minimum distance involving (17,17) is min(x₁, 17-y₃) (same as (0,0) by symmetry). ✓

So the constraints are:
1. Same-side bottom: min(x₁, x₂-x₁, x₃-x₂) ≥ s (the end gap 17-x₃ is to a non-point corner, so it doesn't count for same-side, but it appears in cross-corner)
2. Same-side left: min(17-y₃, y₃-y₂, y₂-y₁) ≥ s
3. Same-side right: min(y₁, y₂-y₁, y₃-y₂) ≥ s (end gap 17-y₃ to corner (17,17))
4. Same-side top: min(17-x₃, x₃-x₂, x₂-x₁) ≥ s (end gap x₁ to corner (17,17))... wait, top points are at 17-x₃, 17-x₂, 17-x₁, 17 from left. Spacings: 17-x₃, x₃-x₂, x₂-x₁, x₁. Same-side min: min(17-x₃, x₃-x₂, x₂-x₁). (End gap x₁ is to corner (17,17).)
5. Corner (0,0): min(x₁, 17-y₃) ≥ s
6. Corner (17,17): min(x₁, 17-y₃) ≥ s (same as 5 by symmetry)
7. Cross-corner (17,0) and (0,17): √((17-x₃)² + y₁²) ≥ s

By symmetry (180° rotation), constraints 1 and 4 are the same, 2 and 3 are the same. So:
- min(x₁, x₂-x₁, x₃-x₂, 17-x₃) ≥ s (bottom/top same-side + end gaps that are to non-point corners)

Wait, I need to be more careful. The end gap 17-x₃ on the bottom is the distance from the last bottom point to the corner (17,0), which is not a point. So this end gap doesn't directly constrain s (there's no point at (17,0)). But it appears in the cross-corner constraint 7.

Similarly, the end gap x₁ on the bottom is the distance from (0,0) (which IS a point) to the first bottom point. So x₁ ≥ s is a constraint (constraint 5).

And 17-y₃ on the left is the distance from (0,0) to the first left point. So 17-y₃ ≥ s (constraint 5).

And y₁ on the right is the distance from (17,0) (not a point) to the first right point. Not a direct constraint, but appears in cross-corner.

And 17-y₁ on the right is the distance from (17,17) (a point) to the last right point. So 17-y₁ ≥ s. But by symmetry, this is the same as 17-y₃ on the left... hmm, no. Let me recheck.

Right side: points at y₁, y₂, y₃ from (17,0). (17,17) is at distance 17 from (17,0). Distance from (17,17) to nearest right point (y₃): 17-y₃. So 17-y₃ ≥ s.

Left side: points at 17-y₃, 17-y₂, 17-y₁ from (0,0). (0,0) is a point. Distance from (0,0) to nearest left point (17-y₃): 17-y₃. So 17-y₃ ≥ s. Same constraint. ✓

And on the bottom: (0,0) is a point. Distance to nearest bottom point (x₁): x₁. So x₁ ≥ s.
On the top: (17,17) is a point. Distance to nearest top point: the top points are at 17-x₃, 17-x₂, 17-x₁, 17 from left. (17,17) is at position 17 from left. Nearest is at 17, distance 0... wait, (17,17) is at position 17 on the top. The top points include 17 (from the rotation: 17-x₁ where x₁ maps to 17-x₁, and the corner (17,17) is at 17). Actually, the top side has the corner point (17,17) at position 17, and the        — AI历史解题过程（thinking）
#   polymath_02816         — 题目ID

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
  <problem_id>polymath_02816</problem_id>
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

Suppose Harvard Yard is a \(17 \times 17\) square. There are \(14\) dorms located on the perimeter of the Yard. If \(s\) is the minimum distance between two dorms, the maximum possible value of \(s\) can be expressed as \(a-\sqrt{b}\) where \(a, b\) are positive integers. Compute \(100a+b\).

## Standard Solution

If two neighboring dorms are separated by a distance of more than \(s\), we can move them slightly closer together and adjust the other dorms, increasing \(s\). Therefore, in an optimal arrangement, the dorms form an equilateral \(14\)-gon with side length \(s\).

By scaling, the problem is now equivalent to finding the smallest \(a\) such that there exist \(14\) vertices on the boundary of an \(a \times a\) square that form an equilateral \(14\)-gon with side length \(1\). Such a \(14\)-gon must be centrally symmetric.

We know that \(x_{1}^{2}+y_{1}^{2}=x_{2}^{2}+y_{2}^{2}=1\) and \(x_{1}+x_{2}+3=y_{1}+y_{2}+2=a\). Moreover, if these equations are satisfied, then such a \(14\)-gon exists. We now consider the vectors \(\vec{v}_{1}=\left(x_{1}, y_{1}\right)\) and \(\vec{v}_{2}=\left(x_{2}, y_{2}\right)\). These unit vectors are in the first quadrant and add to \((a-3, a-2)\), which lies on the line \(y=x+1\).

Since \(\vec{v}_{1}\) and \(\vec{v}_{2}\) must lie in the first quadrant, from the above diagram we deduce that the minimum value of \(a\) occurs when one of \(\vec{v}_{1}, \vec{v}_{2}\) is \((0,1)\), meaning that \((a-3, a-2)=\left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}+1\right)\). This means that \(a=\frac{\sqrt{2}}{2}+3\), so the maximum possible value of \(s\) is

\[
\frac{17}{\frac{\sqrt{2}}{2}+3}=17 \cdot \frac{3-\frac{\sqrt{2}}{2}}{17 / 2}=6-\sqrt{2}
\]

Thus, \(a = 6\) and \(b = 2\). Therefore, \(100a + b = 100 \times 6 + 2 = 602\).

\(\boxed{602}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. Harvard Yard is a 17×17 square. 14 dorms on the perimeter. We want to maximize the minimum distance between any two dorms.

The perimeter of a 17×17 square. Let me think of the square as [0,17]×[0,17]. The perimeter has total length 4×17 = 68.

We need to place 14 points on the perimeter to maximize the minimum pairwise distance.

This is a packing problem on the perimeter of a square. The perimeter is a closed curve of length 68. If we place 14 points evenly spaced along the perimeter (by arc length), each would be 68/14 ≈ 4.857 apart. But the minimum distance is Euclidean, not arc length. Points on the same side that are arc-length 4.857 apart have Euclidean distance 4.857, but points near a corner might be closer in Euclidean distance than arc length.

Actually, the key issue: points near a corner on adjacent sides. If two points are on adjacent sides near a corner, their Euclidean distance could be less than their arc-length distance.

Let me think about this more carefully. The perimeter is a closed loop of length 68. We place 14 points. To maximize minimum Euclidean distance.

First, an upper bound: by arc length, the minimum arc-length distance between consecutive points (in arc-length order) is at most 68/14 = 34/7 ≈ 4.857. The Euclidean distance between two points is at most their arc-length distance (with equality only if they're on the same side). So the minimum Euclidean distance ≤ 34/7 ≈ 4.857.

But can we achieve something close? The issue is corners. If a point is placed near a corner on one side and another point near the same corner on the adjacent side, they could be close in Euclidean distance.

Actually, let me think about whether we can avoid corners entirely or place points strategically.

The answer is supposed to be a - √b. Let me think about what configuration gives this.

Let me consider placing points symmetrically. The square has 4-fold symmetry. 14 = 4×3 + 2, so we can't distribute perfectly evenly across 4 sides. Or maybe 14 points with some on corners.

Actually, let me think about this differently. A common approach: place points so that the minimum distance is determined by a specific pair.

Let me consider the structure. With 14 points on the perimeter of a 17×17 square, and the answer being a - √b.

Let me think about placing points at the corners and along edges. 

If we use the 4 corners, that's 4 points, leaving 10 for the edges. 10/4 = 2.5, so some edges get 2 and some get 3 interior points.

Actually, let me think about whether corners should be used. If a corner is used, the two adjacent points (one on each side) need to be at least distance s from the corner.

Let me try a symmetric approach. Place 2 points at opposite corners, or use all 4 corners.

Let me try: use all 4 corners (4 points), and place 10 points on the edges. Distribute as evenly as possible: each edge gets either 2 or 3 interior points. To be symmetric, we could have 2 edges with 3 and 2 edges with 2, but that breaks symmetry. 

Alternatively, don't use corners. Place points only on the interiors of edges.

Hmm, let me think about this more carefully with the answer format a - √b.

Let me consider a configuration where the minimum distance is achieved by a pair of points on adjacent sides near a corner.

Suppose on one side, points are at distance x from the corner, and on the adjacent side, a point is at distance y from the corner. The Euclidean distance between them is √(x² + y²). If x = y, this is x√2.

If we want to maximize the minimum distance, we need to balance the constraint from same-side distances and cross-corner distances.

Let me set up coordinates. Square [0,17]². 

Consider a symmetric placement. Let's say on each side we place some number of equally spaced points. 

With 14 points and 4-fold symmetry, we could have:
- 4 corners + 10 edge points (but 10 isn't divisible by 4)
- 0 corners + 14 edge points (14 isn't divisible by 4)
- 2 corners (opposite) + 12 edge points (12/4 = 3 per side, but the sides with corners have different structure)

Actually 2-fold symmetry might work better. Let me think about 14 = 2×7.

With 2-fold symmetry (180° rotation), we could have 7 points in each half.

Let me try a different approach. Let me think about what a - √b could be.

Common answers: 17 - √(something), or 34/2 - √(something)...

Let me think about the configuration where the binding constraint is between a point on one side and a point on the adjacent side, both at distance d from a corner. Then their distance is d√2. And on each side, the spacing between consecutive points is some value.

Let me try: no points at corners. On each side, place points symmetrically. 

With 14 points, let's try 2-fold symmetry. Place points so that on two opposite sides we have 4 points each and on the other two sides we have 3 points each. 4+4+3+3 = 14. With 2-fold symmetry (180° rotation), opposite sides have the same number.

For sides with 4 points: if the side has length 17 and 4 points, equally spaced, the spacing is 17/5 = 3.4 (if including endpoints) or 17/3 ≈ 5.67 (if not including endpoints, 4 points divide into 3 gaps... no, 4 points on a segment of length 17, if evenly spaced with equal gaps including to the corners: 17/5 = 3.4).

Hmm, this is getting complicated. Let me think about it more carefully.

Actually, let me reconsider. The problem says the answer is a - √b where a, b are positive integers. So the answer is of the form (integer) - √(integer).

Let me think about what configurations give such answers.

Consider placing points at the 4 corners and distributing the remaining 10 on the edges. If we place 2 or 3 on each edge...

Actually, let me try a specific configuration. Suppose we place points at all 4 corners, and on each side, we place 2 or 3 additional points. To maintain symmetry, let's say on each side we place either 2 or 3 points, with opposite sides having the same count. So 2 sides with 3 and 2 sides with 2: total = 4 + 2×3 + 2×2 = 4 + 6 + 4 = 14. ✓

For the sides with 3 interior points (plus 2 corners = 5 points on that side): the 4 gaps are equal, each 17/4 = 4.25.

For the sides with 2 interior points (plus 2 corners = 4 points on that side): the 3 gaps are equal, each 17/3 ≈ 5.667.

Now the minimum distance: on the 3-interior-point sides, consecutive points are 4.25 apart. On the 2-interior-point sides, consecutive points are 17/3 apart. 

But we also need to check cross-corner distances. At a corner where a 3-point side meets a 2-point side: the nearest point on the 3-point side is at distance 4.25 from the corner, and the nearest point on the 2-point side is at distance 17/3 from the corner. The distance between these two points is √(4.25² + (17/3)²) = √(18.0625 + 32.111) = √50.17 ≈ 7.08. That's large, not binding.

At a corner where two 3-point sides meet: nearest points are both 4.25 from the corner, distance = 4.25√2 ≈ 6.01. Still larger than 4.25.

At a corner where two 2-point sides meet: nearest points are both 17/3 from corner, distance = (17/3)√2 ≈ 8.02. Not binding.

So the minimum distance is 4.25 = 17/4. But 17/4 is not of the form a - √b. So this configuration doesn't give the right answer format.

Hmm. So the answer a - √b suggests that the binding constraint involves a cross-corner distance, which introduces a √2 factor, leading to irrational numbers.

Let me reconsider. Maybe we shouldn't place points at corners, and the binding constraint is between points on adjacent sides near a corner.

Let me try: no points at corners. Place all 14 points on the interiors of the 4 sides. With 2-fold symmetry: 4+4+3+3 = 14 (opposite sides have same count).

For a side with 4 points: let's say they're at positions x₁ < x₂ < x₃ < x₄ from one end. The minimum distance on this side is min(x₁, x₂-x₁, x₃-x₂, x₄-x₃, 17-x₄).

For a side with 3 points: similarly.

The cross-corner constraint: at a corner where a 4-point side meets a 3-point side, the nearest points to the corner are at distances x₁ (on the 4-point side) and y₁ (on the 3-point side) from the corner. Their Euclidean distance is √(x₁² + y₁²).

To maximize the minimum distance s, we want to balance all these constraints.

Let me set up the problem. Let's say the 4-point sides are the top and bottom, and the 3-point sides are the left and right.

On a 4-point side (length 17): points at positions a, a+d, a+2d, a+3d from the left end, where the spacing is d and the end gaps are a and 17-(a+3d) = 17-a-3d. For symmetry of the side (not necessarily required), a = 17-a-3d, so 2a+3d = 17. The minimum distance on this side is min(a, d).

On a 3-point side (length 17): points at positions b, b+e, b+2e from the bottom. End gaps: b and 17-b-2e. For side symmetry: 2b+2e = 17, i.e., b+e = 17/2. Minimum distance: min(b, e).

Cross-corner: at each corner, we have a point at distance a (or 17-a-3d) from the corner on the horizontal side, and a point at distance b (or 17-b-2e) from the corner on the vertical side. The Euclidean distance is √(a² + b²) or similar.

This is getting complex. Let me try to think about what gives a - √b.

The form a - √b typically arises when we have something like: the side length minus a diagonal. For instance, if on a side of length 17, we place points such that the gap from the corner is (17 - s)/2 or something, and the cross-corner distance gives √(x² + x²) = x√2, and we set x√2 = s, so x = s/√2, and then the side spacing gives another equation.

Let me try a cleaner approach. Suppose the binding constraints are:
1. Same-side spacing = s
2. Cross-corner distance = s, where two points are at distances p and q from the corner on adjacent sides, and √(p² + q²) = s.

If p = q (symmetric near corner), then p√2 = s, so p = s/√2.

Now, on a side of length 17 with k interior points, if the end gaps are p = s/√2 and the interior spacing is s, then:
2p + (k-1)s = 17
2(s/√2) + (k-1)s = 17
s(√2 + k - 1) = 17
s = 17/(√2 + k - 1)

For different k:
- k=3: s = 17/(√2 + 2) = 17(2-√2)/((2+√2)(2-√2)) = 17(2-√2)/(4-2) = 17(2-√2)/2 = 17 - 17√2/2. Not of the form a - √b with integer a, b.

Hmm, that doesn't work directly. Let me reconsider.

Actually, maybe the end gaps aren't both s/√2. Maybe one side has a different number of points.

Let me try: suppose on two opposite sides we have k points and on the other two we have m points, with k ≠ m. Then the end gaps might differ.

Let me try k=4, m=3 (so 4+4+3+3 = 14). 

On a 4-point side: end gaps p₁, interior spacing s, so 2p₁ + 3s = 17.
On a 3-point side: end gaps p₂, interior spacing s, so 2p₂ + 2s = 17.

Cross-corner at a corner where 4-point side meets 3-point side: √(p₁² + p₂²) = s.

From the equations:
p₁ = (17 - 3s)/2
p₂ = (17 - 2s)/2

Cross-corner: p₁² + p₂² = s²
((17-3s)/2)² + ((17-2s)/2)² = s²
(17-3s)² + (17-2s)² = 4s²
(289 - 102s + 9s²) + (289 - 68s + 4s²) = 4s²
578 - 170s + 13s² = 4s²
9s² - 170s + 578 = 0

s = (170 ± √(170² - 4·9·578))/(2·9) = (170 ± √(28900 - 20808))/18 = (170 ± √8092)/18

√8092 = √(4·2023) = 2√2023. Hmm, 2023 = 7·17² = 7·289. So √2023 = 17√7. So √8092 = 34√7.

s = (170 ± 34√7)/18 = (85 ± 17√7)/9

s = (85 - 17√7)/9 or s = (85 + 17√7)/9

(85 - 17√7)/9 ≈ (85 - 17·2.6458)/9 ≈ (85 - 44.98)/9 ≈ 40.02/9 ≈ 4.447

(85 + 17√7)/9 ≈ (85 + 44.98)/9 ≈ 129.98/9 ≈ 14.44 (too large, not feasible)

So s = (85 - 17√7)/9. This is not of the form a - √b with integer a, b (it's a fraction).

Hmm. So this symmetric configuration with equal spacing s on all sides doesn't give the right form.

Let me reconsider. Maybe the spacing isn't equal on all sides, or the configuration isn't symmetric in this way.

Wait, actually, maybe I should not assume the interior spacing equals s on all sides. The minimum distance is s, and we want to maximize it. The binding constraints could be different.

Let me reconsider the problem. Maybe the optimal configuration doesn't have the same-side spacing as the binding constraint. Maybe the binding constraint is only the cross-corner distance, and the same-side spacing is larger.

Let me try: on a 4-point side, the points are placed to maximize the minimum of (end gaps, interior spacings, cross-corner distances). If the cross-corner distance is the binding constraint, then the same-side spacings could be larger than s.

Actually, let me think about this differently. Let me consider that the minimum distance s is determined by cross-corner pairs, and we want to maximize s subject to fitting 14 points.

Let me try a configuration with 2-fold symmetry (180° rotation), with 4 points on two opposite sides and 3 on the other two, but where the points on each side are placed to maximize the minimum distance considering both same-side and cross-corner constraints.

Actually, let me try a completely different approach. Let me consider placing points only on 2 adjacent sides, or some other non-symmetric arrangement.

Hmm, but 14 points on the perimeter of a 17×17 square. Let me think about upper bounds more carefully.

The perimeter has length 68. 14 points, so average arc-length spacing is 68/14 ≈ 4.857. The minimum Euclidean distance is at most 68/14 = 34/7 ≈ 4.857 (since Euclidean distance ≤ arc-length distance for points on the same side, but for points on different sides, the Euclidean distance could be less than the arc-length distance).

Wait, actually, for any two points on the perimeter, the Euclidean distance is at most the arc-length distance (the shorter way around). This is because the perimeter is a convex curve, and for a convex curve, the chord length is at most the arc length. So the minimum Euclidean distance ≤ minimum arc-length distance between consecutive points ≤ 68/14 = 34/7.

But can we achieve 34/7? Only if all consecutive points (in arc-length order) are on the same straight side, which is impossible since we have 4 sides of length 17 and 14 points.

Actually, the issue is that some consecutive pairs will straddle a corner, and for those, the Euclidean distance is less than the arc-length distance.

Let me think about it more carefully. If we place 14 points with arc-length spacing 34/7, some points will be near corners. The points near a corner on adjacent sides will have Euclidean distance less than 34/7.

So the optimal configuration likely has some points at corners (to avoid the cross-corner penalty) or adjusts spacing near corners.

Let me reconsider the configuration with points at corners.

Configuration: 4 corners + 10 edge points. With 2-fold symmetry: 4 corners + 5+5 on opposite pairs. So 2 opposite sides have 3 edge points each, and the other 2 have 2 edge points each. Wait, 3+3+2+2 = 10. ✓

On a side with 3 edge points + 2 corners = 5 points: 4 gaps of 17/4 = 4.25 each.
On a side with 2 edge points + 2 corners = 4 points: 3 gaps of 17/3 each.

Cross-corner: at a corner, the nearest edge point on one side is at 4.25 (if 3-edge side) or 17/3 (if 2-edge side). But the corner itself is a point! So the cross-corner distance is from the corner to the nearest point on each adjacent side, which is 4.25 or 17/3. The distance from the corner to a point at distance d along one side is just d. So the minimum distance involving a corner is min(4.25, 17/3) = 4.25.

And the minimum same-side distance is 4.25 (on the 3-edge sides).

So the minimum distance is 4.25 = 17/4. Not of the form a - √b.

Hmm. So using corners gives 17/4, which is rational. The answer a - √b is irrational, so the optimal configuration must not use corners, and the binding constraint must be a cross-corner distance.

Let me go back to the no-corners configuration. The issue with my earlier attempt was that I assumed equal spacing s on all sides. Let me not assume that.

Let me try: no corners, 2-fold symmetry, 4+4+3+3 points on the 4 sides.

Let me label the sides: top and bottom have 4 points each, left and right have 3 points each.

On a 4-point side (say bottom, from (0,0) to (17,0)): points at positions x₁, x₂, x₃, x₄ from the left. End gaps: x₁ and 17-x₄. Interior gaps: x₂-x₁, x₃-x₂, x₄-x₃.

On a 3-point side (say left, from (0,0) to (0,17)): points at positions y₁, y₂, y₃ from the bottom. End gaps: y₁ and 17-y₃. Interior gap: y₃-y₂-y₁... wait, y₂-y₁ and y₃-y₂.

With 2-fold symmetry (180° rotation about center (8.5, 8.5)):
- Bottom side points at x₁, x₂, x₃, x₄ → top side points at 17-x₄, 17-x₃, 17-x₂, 17-x₁ (from left).
- Left side points at y₁, y₂, y₃ → right side points at 17-y₃, 17-y₂, 17-y₁ (from bottom).

For the bottom side to also have 2-fold symmetry (reflection about x=8.5): x₁ = 17-x₄, x₂ = 17-x₃. So points at x₁, x₂, 17-x₂, 17-x₁. End gap: x₁. Interior gaps: x₂-x₁, 17-2x₂, x₂-x₁. So gaps: x₁, x₂-x₁, 17-2x₂, x₂-x₁, x₁... wait, there are 4 points and 5 gaps (including end gaps to corners). No wait, the end gaps are to the corners, but corners aren't points. The gaps between consecutive points on the side are: x₁ (from corner to first point), x₂-x₁, (17-x₂)-x₂ = 17-2x₂... 

Hmm wait, the 4 points are at x₁, x₂, 17-x₂, 17-x₁. The gaps between consecutive points: x₂-x₁, (17-x₂)-x₂ = 17-2x₂, x₂-x₁. And the end gaps (to corners): x₁ and x₁ (by symmetry). So the gaps on this side are: x₁, x₂-x₁, 17-2x₂, x₂-x₁, x₁. But the end gaps are to the corners, not to other points. The minimum same-side distance is min(x₂-x₁, 17-2x₂).

For the left side with 3 points at y₁, y₂, y₃ with 2-fold symmetry: y₁ = 17-y₃, so y₃ = 17-y₁. And y₂ = 17-y₂, so y₂ = 8.5. Points at y₁, 8.5, 17-y₁. Gaps: y₁, 8.5-y₁, 8.5-y₁, y₁. Minimum same-side distance: min(y₁, 8.5-y₁).

Now, cross-corner distances. At corner (0,0):
- Nearest point on bottom: (x₁, 0), distance x₁ from corner.
- Nearest point on left: (0, y₁), distance y₁ from corner.
- Distance between these two: √(x₁² + y₁²).

At corner (17,0):
- Nearest point on bottom: (17-x₁, 0), distance x₁ from corner.
- Nearest point on right: (17, 17-y₃) = (17, y₁) [since y₃ = 17-y₁, 17-y₃ = y₁], distance y₁ from corner.
- Distance: √(x₁² + y₁²). Same by symmetry.

At corner (0,17):
- Nearest point on left: (0, 17-y₁), distance y₁ from corner.
- Nearest point on top: (x₁, 17) [since top is reflection of bottom, nearest point to (0,17) is at x₁ from left], distance x₁ from corner.
- Distance: √(x₁² + y₁²). Same.

So all cross-corner distances are √(x₁² + y₁²).

Now, we also need to check distances between points on adjacent sides that aren't the nearest to the corner. For example, the second nearest point on the bottom from corner (0,0) is at x₂, and the nearest on left is at y₁. Distance = √(x₂² + y₁²). Since x₂ > x₁, this is larger. Similarly, other cross-side distances are larger. But we should also check the distance between the nearest point on the bottom to corner (0,0) and the second nearest on the left, etc. These are all larger than √(x₁² + y₁²) since they involve larger distances from the corner.

Wait, but there's also the distance between a point on the bottom near corner (0,0) and a point on the left near corner (0,0). The closest such pair is (x₁, 0) and (0, y₁) with distance √(x₁² + y₁²). The next closest would be (x₂, 0) and (0, y₁) with distance √(x₂² + y₁²), or (x₁, 0) and (0, 8.5) with distance √(x₁² + 8.5²). Both are larger.

But wait, I also need to check distances between points on the bottom and points on the top (opposite sides), and points on the left and right. These are all at least 17 apart (since the sides are 17 apart), so they're not binding.

Also, I need to check distances between points on the bottom and points on the right side (not just near the shared corner). The closest would be near corner (17,0): (17-x₁, 0) and (17, y₁), distance √(x₁² + y₁²). Already accounted for.

What about a point on the bottom near (0,0) and a point on the right side? The right side is at x=17, so the distance is at least 17-x₁ ≈ 13+, not binding.

So the constraints are:
1. Same-side on 4-point sides: min(x₂-x₁, 17-2x₂) ≥ s
2. Same-side on 3-point sides: min(y₁, 8.5-y₁) ≥ s
3. Cross-corner: √(x₁² + y₁²) ≥ s

We want to maximize s. At the optimum, several of these will be tight.

Let me consider the case where constraints 1, 2, and 3 are all tight.

From constraint 2: min(y₁, 8.5-y₁) = s. If y₁ ≤ 8.5-y₁, i.e., y₁ ≤ 4.25, then y₁ = s. If y₁ > 4.25, then 8.5-y₁ = s, so y₁ = 8.5-s.

From constraint 1: min(x₂-x₁, 17-2x₂) = s. 

From constraint 3: x₁² + y₁² = s².

Case A: y₁ = s (so s ≤ 4.25).
Then from constraint 3: x₁² + s² = s², so x₁ = 0. But x₁ = 0 means a point at the corner, which contradicts our no-corners assumption. So this case doesn't work (unless we allow corner points, but then the answer is rational as we computed).

Case B: y₁ = 8.5 - s (so s < 4.25, since y₁ > 4.25 requires s < 4.25... wait, y₁ = 8.5-s and y₁ > 4.25 means s < 4.25).

From constraint 3: x₁² + (8.5-s)² = s²
x₁² = s² - (8.5-s)² = s² - 72.25 + 17s - s² = 17s - 72.25
x₁ = √(17s - 72.25)

For x₁ to be real: 17s > 72.25, s > 4.25. But we need s < 4.25 for this case. Contradiction!

So neither case works with all three constraints tight. This means my assumption about which constraints are tight is wrong.

Let me reconsider. Maybe constraint 2 is not tight, or constraint 1 is not tight.

Let me think about what's binding. The cross-corner distance √(x₁² + y₁²) is likely the binding constraint, along with one of the same-side constraints.

Let me consider: the binding constraints are the cross-corner distance and the same-side distance on the 4-point sides.

So: √(x₁² + y₁²) = s and min(x₂-x₁, 17-2x₂) = s, while min(y₁, 8.5-y₁) ≥ s.

For the 4-point side, let's say x₂-x₁ = s and 17-2x₂ ≥ s (or vice versa). Let's first try x₂-x₁ = s and 17-2x₂ ≥ s.

Then x₂ = x₁ + s, and 17-2(x₁+s) ≥ s, so 17-2x₁-2s ≥ s, 17-2x₁ ≥ 3s, x₁ ≤ (17-3s)/2.

Also, the end gap x₁ should be ≥ s? No, the end gap is to the corner, not to another point. The end gap doesn't directly constrain s (unless there's a point at the corner, which there isn't). Wait, but the end gap x₁ is the distance from the corner to the first point. There's no other point at the corner, so x₁ doesn't need to be ≥ s. However, x₁ appears in the cross-corner constraint.

Actually, wait. The same-side minimum distance on the 4-point side is min(x₂-x₁, 17-2x₂). The end gaps x₁ don't matter for same-side distance (since there's no point at the corner). So the same-side constraint is just min(x₂-x₁, 17-2x₂) ≥ s.

Similarly, on the 3-point side, the same-side minimum distance is min(8.5-y₁, y₁) [the gaps between consecutive points are 8.5-y₁, 8.5-y₁, and the end gaps are y₁ and y₁]. Wait, the 3 points are at y₁, 8.5, 17-y₁. The gaps between consecutive points: 8.5-y₁ and 8.5-y₁. The end gaps: y₁ and y₁. The same-side minimum distance is min(8.5-y₁, y₁). But the end gaps don't involve other points, so the same-side minimum distance between points is 8.5-y₁ (the gap between consecutive points). Wait, no: the minimum distance between any two points on the same side. The points are at y₁, 8.5, 17-y₁. Distances: 8.5-y₁ (between y₁ and 8.5), 8.5-y₁ (between 8.5 and 17-y₁), 17-2y₁ (between y₁ and 17-y₁). So the minimum same-side distance is 8.5-y₁ (assuming y₁ > 0, which it is).

So the same-side constraint on the 3-point side is 8.5-y₁ ≥ s, i.e., y₁ ≤ 8.5-s.

And the cross-corner constraint: √(x₁² + y₁²) = s (tight).

We want to maximize s. We have freedom to choose x₁, x₂, y₁.

The constraints:
- Cross-corner: x₁² + y₁² = s² (tight)
- 4-point side: x₂-x₁ ≥ s and 17-2x₂ ≥ s (at least one tight)
- 3-point side: 8.5-y₁ ≥ s
- x₁ ≥ 0, y₁ ≥ 0
- Also, x₁ < x₂ < 17-x₂ < 17-x₁ (ordering on the 4-point side)

To maximize s, we want to make the constraints as tight as possible. The 3-point side constraint y₁ ≤ 8.5-s and the cross-corner x₁² + y₁² = s².

We want to maximize s, so we want y₁ as large as possible (to allow x₁ to be small, which gives more room on the 4-point side). But y₁ ≤ 8.5-s.

If y₁ = 8.5-s (tight 3-point side), then x₁² = s² - (8.5-s)² = 17s - 72.25. Need s > 4.25.

But if s > 4.25, then y₁ = 8.5-s < 4.25, and the same-side distance on the 3-point side is 8.5-y₁ = s. OK.

Now, on the 4-point side: x₁ = √(17s-72.25). We need x₂-x₁ ≥ s and 17-2x₂ ≥ s.

From 17-2x₂ ≥ s: x₂ ≤ (17-s)/2.
From x₂-x₁ ≥ s: x₂ ≥ x₁+s.

So we need x₁+s ≤ (17-s)/2, i.e., x₁ ≤ (17-3s)/2.

√(17s-72.25) ≤ (17-3s)/2

Square both sides (need 17-3s > 0, i.e., s < 17/3 ≈ 5.67):
17s - 72.25 ≤ (17-3s)²/4
4(17s-72.25) ≤ (17-3s)²
68s - 289 ≤ 289 - 102s + 9s²
0 ≤ 9s² - 170s + 578

9s² - 170s + 578 ≥ 0

Discriminant: 170² - 4·9·578 = 28900 - 20808 = 8092 = 4·2023 = 4·7·289 = 4·7·17² = (34)²·7

s = (170 ± 34√7)/18 = (85 ± 17√7)/9

The quadratic 9s²-170s+578 ≥ 0 when s ≤ (85-17√7)/9 or s ≥ (85+17√7)/9.

(85-17√7)/9 ≈ (85-44.98)/9 ≈ 40.02/9 ≈ 4.447
(85+17√7)/9 ≈ 14.44 (too large)

So s ≤ (85-17√7)/9 ≈ 4.447.

But wait, we need s > 4.25 for x₁ to be real. And (85-17√7)/9 ≈ 4.447 > 4.25. ✓

So the maximum s in this configuration is s = (85-17√7)/9.

But this is (85-17√7)/9, which is not of the form a - √b with integer a, b. It's a fraction.

Hmm. So either my configuration is wrong, or the answer format allows for this to be rewritten.

(85-17√7)/9 = 85/9 - 17√7/9. Not a - √b with integer a, b.

Let me reconsider. Maybe I have the wrong configuration. Let me try different numbers of points per side.

What if we use 4+3+4+3 = 14 but with a different symmetry? Or 5+2+5+2 = 14? Or some other distribution?

Actually, wait. Let me reconsider whether the 2-fold symmetry with reflection (4-fold symmetry) is optimal. Maybe a configuration with only 2-fold symmetry (180° rotation, no reflection) is better.

Or maybe the optimal configuration doesn't have the same spacing on all sides.

Let me try a different distribution: 5+2+5+2 = 14 (opposite sides have 5 and 2).

On a 5-point side: 4 interior gaps + 2 end gaps = 17. If symmetric: 2a + 4d = 17 where a is end gap and d is interior spacing.
On a 2-point side: 1 interior gap + 2 end gaps = 17. If symmetric: 2b + e = 17 where b is end gap and e is interior spacing.

Same-side min on 5-point side: d (if d ≤ a) or a (if a ≤ d, but a is end gap to corner, not between points). Wait, the 5 points on a side of length 17, with end gaps a and interior spacing d: points at a, a+d, a+2d, a+3d, a+4d. End gap on right: 17-(a+4d) = a (by symmetry). So 2a+4d = 17. Same-side min distance: d (between consecutive points). The end gaps a are to the corner, not between points.

Same-side min on 2-point side: e (the single gap between the 2 points). With 2b+e = 17.

Cross-corner: √(a² + b²) = s.

Constraints:
- d ≥ s (5-point side)
- e ≥ s (2-point side)
- √(a² + b²) = s (cross-corner, tight)
- 2a + 4d = 17 → d = (17-2a)/4
- 2b + e = 17 → e = 17-2b

From d ≥ s: (17-2a)/4 ≥ s → a ≤ (17-4s)/2
From e ≥ s: 17-2b ≥ s → b ≤ (17-s)/2

Cross-corner: a² + b² = s².

To maximize s, set d = s and e = s (make same-side constraints tight):
a = (17-4s)/2, b = (17-s)/2.

a² + b² = s²:
((17-4s)/2)² + ((17-s)/2)² = s²
(17-4s)² + (17-s)² = 4s²
(289-136s+16s²) + (289-34s+s²) = 4s²
578 - 170s + 17s² = 4s²
13s² - 170s + 578 = 0

s = (170 ± √(28900-4·13·578))/(2·13) = (170 ± √(28900-30056))/26

28900-30056 = -1156 < 0. No real solution!

So we can't have both d = s and e = s simultaneously with the cross-corner constraint. This means the 5+2+5+2 configuration can't have all constraints tight simultaneously. The cross-corner distance is too large relative to the same-side distances, or vice versa.

Let me try not making both same-side constraints tight. Maybe only one is tight.

If d = s (5-point side tight) and e > s (2-point side not tight):
a = (17-4s)/2, b is free with b ≤ (17-s)/2 and a² + b² = s².

b = √(s² - a²) = √(s² - ((17-4s)/2)²).

We need b ≤ (17-s)/2 and e = 17-2b ≥ s, i.e., b ≤ (17-s)/2.

Also b ≥ 0, so s² ≥ ((17-4s)/2)², i.e., 4s² ≥ (17-4s)², 2s ≥ 17-4s (need 17-4s > 0), 6s ≥ 17, s ≥ 17/6 ≈ 2.83.

To maximize s, we want b as large as possible (to maximize the cross-corner distance? no, the cross-corner is fixed at s). Actually, we want to maximize s, and the constraint is b ≤ (17-s)/2. So:

√(s² - ((17-4s)/2)²) ≤ (17-s)/2

s² - ((17-4s)/2)² ≤ ((17-s)/2)²

4s² - (17-4s)² ≤ (17-s)²

4s² - (289-136s+16s²) ≤ 289-34s+s²

4s² - 289 + 136s - 16s² ≤ 289 - 34s + s²

-12s² + 136s - 289 ≤ 289 - 34s + s²

-13s² + 170s - 578 ≤ 0

13s² - 170s + 578 ≥ 0

Discriminant: 170² - 4·13·578 = 28900-30056 = -1156 < 0.

Since the discriminant is negative and the leading coefficient is positive, 13s²-170s+578 > 0 for all s. So the constraint is always satisfied! This means b ≤ (17-s)/2 is never binding when d = s.

So with d = s, we can increase s until some other constraint binds. What other constraint? We need b ≥ 0, which gives s ≥ 17/6. And we need the 2-point side to have e ≥ s, which is b ≤ (17-s)/2, always satisfied. And we need the 3-point side... wait, there's no 3-point side in this configuration.

Hmm, but we also need to check that the 2-point side's same-side distance e is actually ≥ s. We have e = 17-2b, and b = √(s²-a²). As s increases, a = (17-4s)/2 decreases (and eventually becomes 0 when s = 17/4 = 4.25), and b = √(s²-a²) increases. e = 17-2b decreases. At some point e = s.

Let me find when e = s: 17-2b = s, b = (17-s)/2. And b² = s²-a², a = (17-4s)/2.

((17-s)/2)² = s² - ((17-4s)/2)²

This is the same equation as before: 13s²-170s+578 = 0, which has no real solutions. So e > s always when d = s.

So what limits s? We need a ≥ 0: (17-4s)/2 ≥ 0, s ≤ 17/4 = 4.25. And b ≤ (17-s)/2, always satisfied. And we need the points to be in order, etc.

Wait, but if s can go up to 4.25 with d = s, what happens at s = 4.25? Then a = 0, meaning a point at the corner. And b = √(s²-0) = s = 4.25. e = 17-2(4.25) = 8.5. So the 2-point side has points at 4.25 and 12.75, with gap 8.5. And the 5-point side has points at 0, 4.25, 8.5, 12.75, 17 (i.e., at the corners and equally spaced). The minimum distance is 4.25.

But 4.25 = 17/4, same as before. And this is rational, not a - √b.

So the 5+2+5+2 configuration gives at most 17/4, same as the corner configuration. Not better.

Let me go back to the 4+4+3+3 configuration which gave s = (85-17√7)/9 ≈ 4.447. This is better than 17/4 = 4.25! So the 4+4+3+3 configuration is better.

But the answer (85-17√7)/9 is not of the form a - √b. Let me double-check my algebra.

Actually, wait. Let me reconsider. Maybe I need to not assume the 4-point side has reflection symmetry. With only 180° rotation symmetry, the 4-point side doesn't need to be symmetric about its midpoint.

Let me redo the 4+4+3+3 configuration with only 180° rotation symmetry (no reflection).

Bottom side: 4 points at x₁ < x₂ < x₃ < x₄.
Top side (180° rotation): points at 17-x₄, 17-x₃, 17-x₂, 17-x₁.
Left side: 3 points at y₁ < y₂ < y₃.
Right side (180° rotation): points at 17-y₃, 17-y₂, 17-y₁.

Now, the cross-corner distances:
At (0,0): nearest bottom point at x₁, nearest left point at y₁. Distance √(x₁²+y₁²).
At (17,0): nearest bottom point at 17-x₄, nearest right point at 17-y₃. Distance √((17-x₄)²+(17-y₃)²).
At (0,17): nearest top point at 17-x₄ (from left, so at position 17-x₄ from left = x₄ from right, distance from corner (0,17) is 17-x₄... wait, the top side goes from (0,17) to (17,17). A point at position 17-x₄ from the left is at (17-x₄, 17). Distance from corner (0,17) is 17-x₄. Nearest left point at 17-y₁ (from bottom, so at (0, 17-y₁)). Distance from corner (0,17) is y₁. Cross-corner distance: √((17-x₄)²+y₁²).
At (17,17): nearest top point at x₁ (from left, at (x₁, 17), distance from (17,17) is 17-x₁). Nearest right point at y₁ (from bottom, at (17, y₁), distance from (17,17) is 17-y₁). Cross-corner: √((17-x₁)²+(17-y₁)²).

By 180° rotation, corner (0,0) maps to (17,17), and (17,0) maps to (0,17). So:
√(x₁²+y₁²) = √((17-x₁)²+(17-y₁)²) → x₁²+y₁² = (17-x₁)²+(17-y₁)² → x₁²+y₁² = 289-34x₁+x₁²+289-34y₁+y₁² → 0 = 578-34(x₁+y₁) → x₁+y₁ = 17.

Similarly, √((17-x₄)²+(17-y₃)²) = √((17-x₄)²+y₁²) → (17-y₃)² = y₁² → 17-y₃ = y₁ (taking positive root) → y₃ = 17-y₁. But this is already implied by the 180° rotation: right side has point at 17-y₃ from bottom, and left side has point at y₁ from bottom. For the cross-corner at (17,0) and (0,17) to be equal, we need... actually, let me be more careful.

By 180° rotation, the configuration at corner (17,0) is the rotation of the configuration at corner (0,17). So their cross-corner distances are automatically equal. And the configuration at (0,0) is the rotation of (17,17). So we have two potentially different cross-corner distances:

d₁ = √(x₁²+y₁²) (at corners (0,0) and (17,17))
d₂ = √((17-x₄)²+(17-y₃)²) (at corners (17,0) and (0,17))

But wait, from 180° rotation, x₁+y₁ = 17 doesn't necessarily hold. Let me recheck.

180° rotation maps (x,y) to (17-x, 17-y). So a point at (x₁, 0) on the bottom maps to (17-x₁, 17) on the top. For this to be a point on the top side, we need 17-x₁ to be one of the top side positions. The top side positions are 17-x₄, 17-x₃, 17-x₂, 17-x₁. So 17-x₁ is indeed a top side position. ✓

A point at (0, y₁) on the left maps to (17, 17-y₁) on the right. Right side positions are 17-y₃, 17-y₂, 17-y₁. So 17-y₁ is a right side position. ✓

Now, corner (0,0) maps to (17,17) under 180° rotation. The nearest bottom point to (0,0) is at x₁, and the nearest left point to (0,0) is at y₁. Under rotation, the nearest top point to (17,17) is at 17-x₁ (from left, so at distance 17-(17-x₁) = x₁ from (17,17)), and the nearest right point to (17,17) is at 17-y₁ (from bottom, so at distance 17-(17-y₁) = y₁ from (17,17)). So the cross-corner distance at (17,17) is also √(x₁²+y₁²). ✓

Corner (17,0) maps to (0,17). The nearest bottom point to (17,0) is at 17-x₄ (distance x₄ from (17,0)... wait, the bottom point closest to (17,0) is the one with the largest x-coordinate, which is x₄. Its distance from (17,0) is 17-x₄. The nearest right point to (17,0) is at 17-y₃ (from bottom, so at (17, 17-y₃), distance from (17,0) is 17-y₃). Cross-corner distance: √((17-x₄)²+(17-y₃)²).

Under rotation, corner (0,17): nearest top point is at 17-x₄ (from left, at (17-x₄, 17), distance from (0,17) is 17-x₄). Nearest left point is at 17-y₁ (at (0, 17-y₁), distance from (0,17) is y₁). Wait, that doesn't match.

Hmm, let me recompute. At corner (0,17): the top side goes from (0,17) to (17,17). The nearest top point to (0,17) is the one with the smallest x-coordinate, which is 17-x₄ (since the top points are at 17-x₄, 17-x₃, 17-x₂, 17-x₁ and x₁ < x₂ < x₃ < x₄, so 17-x₄ < 17-x₃ < 17-x₂ < 17-x₁). So the nearest top point is at 17-x₄, distance 17-x₄ from (0,17).

The left side goes from (0,0) to (0,17). The nearest left point to (0,17) is the one with the largest y-coordinate, which is y₃. Distance from (0,17) is 17-y₃.

Cross-corner at (0,17): √((17-x₄)²+(17-y₃)²). Same as at (17,0). ✓

So we have two cross-corner distances:
d₁ = √(x₁²+y₁²) (at (0,0) and (17,17))
d₂ = √((17-x₄)²+(17-y₃)²) (at (17,0) and (0,17))

Now, we also need to check other cross-side distances. For example, the distance between the bottom point at x₁ and the left point at y₂ (the second point on the left side). This is √(x₁²+y₂²). Since y₂ > y₁, this is larger than d₁. Similarly for other non-nearest pairs.

But we also need to check distances between bottom points and right points, and top points and left points, etc. The closest such distance would be between a bottom point near (17,0) and a right point near (17,0), which is d₂. Other cross-side distances (bottom-left, top-right, etc.) are all larger.

Wait, I also need to check distances between points on the bottom and points on the left that aren't both nearest to the same corner. For example, bottom point at x₄ (near (17,0)) and left point at y₁ (near (0,0)). Distance = √(x₄²+y₁²). This is large since x₄ is close to 17. Not binding.

What about bottom point at x₂ and left point at y₁? Distance = √(x₂²+y₁²). Since x₂ > x₁, this is > d₁. Not binding (if d₁ is the minimum).

OK so the binding constraints are:
1. Same-side on bottom: min(x₂-x₁, x₃-x₂, x₄-x₃) ≥ s
2. Same-side on left: min(y₂-y₁, y₃-y₂) ≥ s
3. Cross-corner d₁ = √(x₁²+y₁²) ≥ s
4. Cross-corner d₂ = √((17-x₄)²+(17-y₃)²) ≥ s
5. End gaps don't directly constrain s (no points at corners)

We want to maximize s. At optimum, several constraints are tight.

Now, with 180° rotation but no reflection, we have more freedom. Let me consider the case where d₁ = d₂ = s (both cross-corner constraints tight) and the same-side constraints are also tight.

If d₁ = d₂ = s:
x₁² + y₁² = s²
(17-x₄)² + (17-y₃)² = s²

And same-side on bottom: let's say x₂-x₁ = x₃-x₂ = x₄-x₃ = s (equal spacing). Then x₂ = x₁+s, x₃ = x₁+2s, x₄ = x₁+3s.

Same-side on left: y₂-y₁ = y₃-y₂ = s (equal spacing). Then y₂ = y₁+s, y₃ = y₁+2s.

Now d₂: (17-x₁-3s)² + (17-y₁-2s)² = s².

And d₁: x₁² + y₁² = s².

Two equations, two unknowns (x₁, y₁), parameterized by s.

From d₁: x₁² + y₁² = s².
From d₂: (17-x₁-3s)² + (17-y₁-2s)² = s².

Let u = 17-x₁-3s, v = 17-y₁-2s. Then u²+v² = s² and x₁²+y₁² = s².

Also, x₁ = 17-3s-u, y₁ = 17-2s-v.

(17-3s-u)² + (17-2s-v)² = s²

And u²+v² = s².

Let me expand:
(17-3s)² - 2(17-3s)u + u² + (17-2s)² - 2(17-2s)v + v² = s²

(17-3s)² + (17-2s)² - 2(17-3s)u - 2(2s)v + (u²+v²) = s²

(17-3s)² + (17-2s)² - 2(17-3s)u - 2(17-2s)v + s² = s²

(17-3s)² + (17-2s)² = 2(17-3s)u + 2(17-2s)v

Let A = 17-3s, B = 17-2s. Then:
A² + B² = 2Au + 2Bv

And u²+v² = s², x₁ = A-u, y₁ = B-v, x₁²+y₁² = s²:
(A-u)² + (B-v)² = s²
A²-2Au+u² + B²-2Bv+v² = s²
A²+B² - 2(Au+Bv) + (u²+v²) = s²
A²+B² - (A²+B²) + s² = s² [using 2(Au+Bv) = A²+B² and u²+v²=s²]
0 = 0 ✓

So the two equations are consistent but don't uniquely determine u, v. We have:
u²+v² = s² (circle of radius s)
2Au + 2Bv = A²+B² (line)

The line intersects the circle. The distance from origin to the line is (A²+B²)/(2√(A²+B²)) = √(A²+B²)/2.

For intersection: √(A²+B²)/2 ≤ s, i.e., A²+B² ≤ 4s².

A²+B² = (17-3s)²+(17-2s)² = 289-102s+9s²+289-68s+4s² = 578-170s+13s².

4s² ≥ 578-170s+13s² → 0 ≥ 578-170s+9s² → 9s²-170s+578 ≤ 0.

This is the same quadratic as before! 9s²-170s+578 ≤ 0 when (85-17√7)/9 ≤ s ≤ (85+17√7)/9.

So the maximum s is (85+17√7)/9 ≈ 14.44, but that's way too large (s can't exceed 17). The minimum s for which the system has a solution is (85-17√7)/9 ≈ 4.447.

Wait, I think I'm confusing myself. The constraint is 9s²-170s+578 ≤ 0, which holds for s ∈ [(85-17√7)/9, (85+17√7)/9]. So s can be at most (85+17√7)/9 ≈ 14.44. But we also need all the points to fit on the sides, which requires x₁ ≥ 0, x₄ ≤ 17, y₁ ≥ 0, y₃ ≤ 17.

x₄ = x₁+3s ≤ 17 → x₁ ≤ 17-3s. For s ≈ 14.44, 17-3s < 0, so x₁ < 0, impossible.

So the real constraint is that all points fit. Let me add: x₁ ≥ 0, y₁ ≥ 0, x₄ = x₁+3s ≤ 17, y₃ = y₁+2s ≤ 17.

From x₁ ≥ 0 and x₁²+y₁² = s²: y₁ ≤ s.
From y₁ ≥ 0 and x₁²+y₁² = s²: x₁ ≤ s.
From x₄ ≤ 17: x₁ ≤ 17-3s, so s ≤ 17/3 ≈ 5.67 (if x₁ = 0).
From y₃ ≤ 17: y₁ ≤ 17-2s, so s ≤ 17/2 = 8.5 (if y₁ = 0).

The binding constraint is s ≤ 17/3 from the bottom side (4 points with spacing s need total length 3s ≤ 17, plus end gaps).

But we also need the cross-corner constraints. Let me think about what happens as s increases.

For the system to have a solution, we need 9s²-170s+578 ≤ 0, i.e., s ≥ (85-17√7)/9 ≈ 4.447. And we need x₁ ≥ 0, y₁ ≥ 0, x₁+3s ≤ 17, y₁+2s ≤ 17.

At s = (85-17√7)/9, the line is tangent to the circle, giving a unique solution. Let me check if the points fit.

Actually, I realize the issue. For s > (85-17√7)/9, the system has solutions (the line cuts the circle in two points). We want to maximize s, so we want the largest s for which all constraints are satisfied.

The constraints are:
- 9s²-170s+578 ≤ 0 (cross-corner system solvable)
- x₁ ≥ 0, y₁ ≥ 0 (points not beyond corners)
- x₁+3s ≤ 17, y₁+2s ≤ 17 (points fit on sides)

The cross-corner constraint gives s ≤ (85+17√7)/9 ≈ 14.44, which is not binding.
The fitting constraints give s ≤ 17/3 ≈ 5.67 (from x₁+3s ≤ 17 with x₁ ≥ 0).

But we also need x₁²+y₁² = s² with x₁ ≥ 0, y₁ ≥ 0, x₁ ≤ 17-3s, y₁ ≤ 17-2s.

The maximum of x₁²+y₁² subject to 0 ≤ x₁ ≤ 17-3s, 0 ≤ y₁ ≤ 17-2s is (17-3s)²+(17-2s)² (at the corner of the feasible region). We need this ≥ s²:

(17-3s)²+(17-2s)² ≥ s²
578-170s+13s² ≥ s²
12s²-170s+578 ≥ 0

Discriminant: 170²-4·12·578 = 28900-27744 = 1156 = 34².
s = (170±34)/24 = 204/24 = 8.5 or 136/24 = 17/3 ≈ 5.667.

So 12s²-170s+578 ≥ 0 when s ≤ 17/3 or s ≥ 8.5.

For s ≤ 17/3, this is satisfied. So the fitting constraint and the cross-corner constraint together give:

s ≤ 17/3 (fitting) and s ≥ (85-17√7)/9 (cross-corner solvable) and 9s²-170s+578 ≤ 0 (cross-corner solvable, i.e., s ≤ (85+17√7)/9).

Wait, I think I need to be more careful. The cross-corner constraint says that there exist x₁, y₁ with x₁²+y₁² = s² and (17-x₁-3s)²+(17-y₁-2s)² = s² and 0 ≤ x₁ ≤ 17-3s and 0 ≤ y₁ ≤ 17-2s.

The system x₁²+y₁² = s² and (17-3s-x₁)²+(17-2s-y₁)² = s² has solutions when 9s²-170s+578 ≤ 0 (i.e., the line intersects the circle). But we also need the solution to satisfy 0 ≤ x₁ ≤ 17-3s and 0 ≤ y₁ ≤ 17-2s.

Hmm, this is getting complicated. Let me think about it differently.

We want to maximize s. The constraints from the 4+4+3+3 configuration with equal spacing s on all sides and both cross-corner distances equal to s are:

1. x₁² + y₁² = s²
2. (17-3s-x₁)² + (17-2s-y₁)² = s²
3. 0 ≤ x₁ ≤ 17-3s
4. 0 ≤ y₁ ≤ 17-2s

From 1 and 2, the system is solvable when 9s²-170s+578 ≤ 0, i.e., s ∈ [(85-17√7)/9, (85+17√7)/9].

For s in this range, the solutions (x₁, y₁) lie on the intersection of the circle x₁²+y₁²=s² and the line 2(17-3s)x₁ + 2(17-2s)y₁ = (17-3s)²+(17-2s)².

We need to check if any solution satisfies constraints 3 and 4.

As s increases from (85-17√7)/9, the solutions move along the circle. At some point, the constraints 3, 4 may be violated.

Let me check at s = 17/3 (the fitting limit for the bottom side). Then 17-3s = 0, so x₁ = 0 (from constraint 3). Then y₁ = s = 17/3 from constraint 1. Check constraint 4: y₁ = 17/3 ≤ 17-2s = 17-34/3 = 17/3. ✓ (tight). Check constraint 2: (0)²+(17/3)² = (17/3)² = s². ✓.

So at s = 17/3, x₁ = 0, y₁ = 17/3. This means a point at the corner (0,0) on the bottom side! And the left side has its first point at y₁ = 17/3.

But x₁ = 0 means a point at corner (0,0). Is this allowed? The problem says dorms are on the perimeter, and corners are on the perimeter, so yes.

But if there's a point at (0,0), then the distance from this point to the nearest left-side point at (0, 17/3) is 17/3 ≈ 5.667. And the distance to the nearest bottom-side point at (s, 0) = (17/3, 0) is also 17/3. So the minimum distance is 17/3.

But 17/3 ≈ 5.667 > (85-17√7)/9 ≈ 4.447. So s = 17/3 is better!

Wait, but I need to check all constraints. At s = 17/3:
- Bottom side: points at 0, 17/3, 34/3, 17. So points at corners (0,0) and (17,0) and at 17/3 and 34/3. Spacing: 17/3 each.
- Top side (180° rotation): points at 0, 17/3, 34/3, 17 (same as bottom, since 17-x₄ = 17-17 = 0, 17-x₃ = 17-34/3 = 17/3, etc.). So top also has points at corners.
- Left side: points at 17/3, 17/3+17/3 = 34/3, 34/3+17/3 = 17. So points at (0, 17/3), (0, 34/3), (0, 17). The last is a corner!
- Right side: points at 0, 17/3, 34/3 (by 180° rotation: 17-y₃ = 0, 17-y₂ = 17-34/3 = 17/3, 17-y₁ = 17-17/3 = 34/3). So points at (17, 0), (17, 17/3), (17, 34/3). The first is a corner!

So the corners (0,0), (17,0), (0,17), (17,17) all have points. That's 4 corner points. Plus 2+2+2+2 = 8 edge points. Total: 12, not 14. Wait, let me recount.

Bottom: 4 points (0, 17/3, 34/3, 17) — 2 corners + 2 edge.
Top: 4 points (0, 17/3, 34/3, 17) — 2 corners + 2 edge.
Left: 3 points (17/3, 34/3, 17) — 1 corner + 2 edge.
Right: 3 points (0, 17/3, 34/3) — 1 corner + 2 edge.

Corners: (0,0) on bottom, (17,0) on bottom and right, (0,17) on top and left, (17,17) on top and left... wait, (17,17) is on top (at x=17) and right (at y=17). But right side points are at y = 0, 17/3, 34/3. y=17 is not among them. And (0,17) is on top (at x=0) and left (at y=17). Left side points are at y = 17/3, 34/3, 17. y=17 is among them. So (0,17) is a left side point and a top side point.

Let me list all distinct points:
Bottom: (0,0), (17/3, 0), (34/3, 0), (17, 0)
Top: (0, 17), (17/3, 17), (34/3, 17), (17, 17)
Left: (0, 17/3), (0, 34/3), (0, 17)
Right: (17, 0), (17, 17/3), (17, 34/3)

Distinct points: (0,0), (17/3,0), (34/3,0), (17,0), (0,17), (17/3,17), (34/3,17), (17,17), (0,17/3), (0,34/3), (17,17/3), (17,34/3).

That's 12 distinct points. But we need 14! The issue is that (17,0) appears on both bottom and right, and (0,17) appears on both top and left. So we have 12 distinct points, not 14.

So the configuration with s = 17/3 only gives 12 distinct points, not 14. We need 14 distinct points.

The problem is that at s = 17/3, the 4-point sides use corners, which coincide with points on the 3-point sides. So we lose 2 points to coincidence.

So we need s < 17/3 to have 14 distinct points (no coincidences at corners). As s decreases from 17/3, the points move away from corners and we get 14 distinct points.

But we want to maximize s. So the optimal s is just below 17/3? No, because as s decreases, we need to check the cross-corner constraint.

Actually, wait. At s = 17/3, we have 12 points. We need 14. So we need to either add 2 more points (which would decrease the minimum distance) or use a different configuration.

Hmm, I think the issue is that my 4+4+3+3 distribution with equal spacing doesn't work at s = 17/3 because of corner coincidences. Let me reconsider.

Maybe the optimal configuration is different. Let me think about this problem from scratch.

We have 14 points on the perimeter of a 17×17 square. We want to maximize the minimum pairwise distance.

Let me think about it as placing 14 points on a closed curve of length 68. The curve has 4 "corners" where the direction changes by 90°.

Key insight: for points on the same side, the Euclidean distance equals the arc-length distance. For points on adjacent sides near a corner, the Euclidean distance is less than the arc-length distance (it's the hypotenuse of a right triangle).

To maximize the minimum Euclidean distance, we want to avoid having points close to corners on adjacent sides (which would give small Euclidean distances). One way is to place points at corners (so the "cross-corner" issue becomes a same-side issue). Another way is to keep points away from corners.

Let me think about the trade-off. If we place points at corners, we "use up" corner positions but avoid cross-corner penalties. If we don't place points at corners, we need to keep points away from corners, which wastes perimeter length.

Let me consider the configuration with all 4 corners occupied. Then we have 10 points on the edges. The minimum distance is determined by the spacing on the edges and the distance from corner points to nearby edge points.

With 4 corners + 10 edge points, and 2-fold symmetry: 5+5 edge points on opposite pairs. Say 3 on two opposite sides and 2 on the other two.

3-edge side: 5 points total (2 corners + 3 edge), 4 gaps of 17/4 = 4.25.
2-edge side: 4 points total (2 corners + 2 edge), 3 gaps of 17/3 ≈ 5.667.

Minimum distance: 4.25 (on the 3-edge sides). Cross-corner: at a corner, the nearest edge point is at 4.25 (on the 3-edge side) or 17/3 (on the 2-edge side). The distance from the corner to the nearest edge point is 4.25 or 17/3, so the minimum is 4.25.

But we should also check the distance between the nearest edge point on one side and the nearest edge point on the adjacent side, both near the same corner. At a corner where a 3-edge side meets a 2-edge side: the edge points are at 4.25 and 17/3 from the corner. Distance = √(4.25² + (17/3)²) = √(18.0625 + 32.111) = √50.17 ≈ 7.08. Not binding.

At a corner where two 3-edge sides meet: edge points at 4.25 and 4.25 from corner. Distance = 4.25√2 ≈ 6.01. Not binding (since 4.25 < 6.01).

At a corner where two 2-edge sides meet: edge points at 17/3 and 17/3. Distance = (17/3)√2 ≈ 8.02. Not binding.

So minimum distance = 4.25 = 17/4. This is the corner configuration.

Now, the no-corner configuration with 4+4+3+3 gave s ≈ 4.447, which is better than 4.25. But it's not of the form a - √b.

Hmm, let me reconsider. Maybe I need to not require equal spacing on all sides. Let me go back to the 4+4+3+3 configuration with 180° rotation symmetry but without requiring equal spacing or both cross-corner distances to be equal.

Let me parameterize differently. On the bottom side, 4 points at x₁ < x₂ < x₃ < x₄ with spacings d₁ = x₂-x₁, d₂ = x₃-x₂, d₃ = x₄-x₃. End gaps: x₁ and 17-x₄.

On the left side, 3 points at y₁ < y₂ < y₃ with spacings e₁ = y₂-y₁, e₂ = y₃-y₂. End gaps: y₁ and 17-y₃.

180° rotation: top has points at 17-x₄, 17-x₃, 17-x₂, 17-x₁. Right has points at 17-y₃, 17-y₂, 17-y₁.

Constraints (minimum distance s):
- Same-side bottom: min(d₁, d₂, d₃) ≥ s
- Same-side left: min(e₁, e₂) ≥ s
- Cross-corner at (0,0): √(x₁² + y₁²) ≥ s
- Cross-corner at (17,0): √((17-x₄)² + (17-y₃)²) ≥ s
- Cross-corner at (0,17): √((17-x₄)² + (17-y₃)²) ≥ s [same as (17,0) by symmetry]

Wait, I computed earlier that (0,17) and (17,0) have the same cross-corner distance. And (0,0) and (17,17) have the same. So two cross-corner constraints.

- Other cross-side distances (non-nearest to same corner): all larger, not binding.

To maximize s, we want to make the binding constraints tight. The question is which constraints are binding.

Let me consider the case where:
- Same-side bottom: d₁ = d₂ = d₃ = s (equal spacing, all tight)
- Same-side left: e₁ = e₂ = s (equal spacing, all tight)
- Cross-corner at (0,0): √(x₁² + y₁²) = s (tight)
- Cross-corner at (17,0): √((17-x₄)² + (17-y₃)²) = s (tight)

This is the case I analyzed before, giving s = (85-17√7)/9 or s = (85+17√7)/9 (too large).

But maybe not all same-side constraints need to be tight. Maybe only the cross-corner constraints and some same-side constraints are tight.

Let me try: cross-corner at (0,0) is tight, cross-corner at (17,0) is NOT tight (i.e., the points near (17,0) are farther apart), and same-side constraints are tight.

If only cross-corner at (0,0) is tight: √(x₁² + y₁²) = s.

Same-side bottom: d₁ = d₂ = d₃ = s. So x₂ = x₁+s, x₃ = x₁+2s, x₄ = x₁+3s.
Same-side left: e₁ = e₂ = s. So y₂ = y₁+s, y₃ = y₁+2s.

Cross-corner at (17,0): (17-x₁-3s)² + (17-y₁-2s)² ≥ s². (Not tight.)

We want to maximize s. The constraints are:
1. x₁² + y₁² = s² (tight cross-corner at (0,0))
2. x₁ ≥ 0, y₁ ≥ 0 (points not beyond corners)
3. x₁ + 3s ≤ 17 (bottom points fit) → x₁ ≤ 17-3s
4. y₁ + 2s ≤ 17 (left points fit) → y₁ ≤ 17-2s
5. (17-x₁-3s)² + (17-y₁-2s)² ≥ s² (cross-corner at (17,0) not tight)

From 1: x₁ = s·cos(θ), y₁ = s·sin(θ) for some θ ∈ [0, π/2].

From 3: s·cos(θ) ≤ 17-3s → cos(θ) ≤ (17-3s)/s = 17/s - 3.
From 4: s·sin(θ) ≤ 17-2s → sin(θ) ≤ 17/s - 2.

For these to have a solution, we need (17/s-3)² + (17/s-2)² ≥ 1 (since cos²θ + sin²θ = 1 and both cos θ and sin θ are at most those bounds). Actually, we need cos θ ≤ 17/s-3 and sin θ ≤ 17/s-2, and cos²θ + sin²θ = 1. This requires (17/s-3)² + (17/s-2)² ≥ 1 (so that the rectangle [0, 17/s-3] × [0, 17/s-2] intersects the unit circle).

Also, 17/s-3 ≥ 0 → s ≤ 17/3, and 17/s-2 ≥ 0 → s ≤ 17/2.

Let t = 17/s. Then (t-3)² + (t-2)² ≥ 1 → 2t²-10t+13 ≥ 1 → 2t²-10t+12 ≥ 0 → t²-5t+6 ≥ 0 → (t-2)(t-3) ≥ 0 → t ≤ 2 or t ≥ 3.

Since t = 17/s and s ≤ 17/3, t ≥ 3. So t ≥ 3, i.e., s ≤ 17/3. And the constraint (t-3)²+(t-2)² ≥ 1 is satisfied for t ≥ 3 (equality at t = 3, i.e., s = 17/3).

So the fitting constraints allow s up to 17/3. Now check constraint 5:

(17-x₁-3s)² + (17-y₁-2s)² ≥ s²

Let u = 17-x₁-3s = 17-s·cos(θ)-3s = 17-s(3+cos θ) and v = 17-y₁-2s = 17-s(2+sin θ).

u² + v² ≥ s²
(17-s(3+cos θ))² + (17-s(2+sin θ))² ≥ s²

At s = 17/3, t = 3, and from the fitting constraint (t-3)²+(t-2)² = 1, so cos θ = 0, sin θ = 1 (i.e., θ = π/2, x₁ = 0, y₁ = s = 17/3).

Then u = 17-0-17 = 0, v = 17-17/3-34/3 = 17-17 = 0. So u²+v² = 0 < s². Constraint 5 is violated!

So at s = 17/3, the cross-corner at (17,0) is too small. We need to reduce s.

Let me find the maximum s where constraint 5 is satisfied. We need:

(17-s(3+cos θ))² + (17-s(2+sin θ))² ≥ s²

with cos²θ + sin²θ = 1, 0 ≤ cos θ ≤ 17/s-3, 0 ≤ sin θ ≤ 17/s-2.

To maximize s, we want to choose θ to maximize the LHS. The LHS is maximized when u and v are as large as possible, i.e., when cos θ and sin θ are as small as possible. But cos θ and sin θ are constrained by cos²θ+sin²θ=1.

Actually, to maximize u²+v² = (17-s(3+cosθ))²+(17-s(2+sinθ))², we want to minimize s(3+cosθ) and s(2+sinθ), i.e., minimize cosθ and sinθ. But cos²θ+sin²θ=1, so we can't minimize both. 

The LHS is a function of θ. Let me compute it:

f(θ) = (17-s(3+cosθ))² + (17-s(2+sinθ))²

= (17-3s)² - 2(17-3s)s·cosθ + s²cos²θ + (17-2s)² - 2(17-2s)s·sinθ + s²sin²θ

= (17-3s)² + (17-2s)² + s² - 2s[(17-3s)cosθ + (17-2s)sinθ]

= 578-170s+13s² - 2s[(17-3s)cosθ + (17-2s)sinθ]

To maximize f(θ), we minimize (17-3s)cosθ + (17-2s)sinθ. This is of the form A·cosθ + B·sinθ where A = 17-3s, B = 17-2s. The minimum over θ is -√(A²+B²) (achieved when (cosθ, sinθ) is in the direction of (-A, -B), i.e., θ in the third quadrant). But we need cosθ ≥ 0 and sinθ ≥ 0 (first quadrant).

In the first quadrant, the minimum of A·cosθ + B·sinθ (with A, B > 0 for s < 17/3) is achieved at the endpoints: either cosθ = 0, sinθ = 1 (giving B) or cosθ = 1, sinθ = 0 (giving A), whichever is smaller. Since A = 17-3s < B = 17-2s for s > 0, the minimum is A = 17-3s, achieved at θ = 0 (cosθ = 1, sinθ = 0, i.e., x₁ = s, y₁ = 0).

But y₁ = 0 means a point at the corner (0,0) on the left side. Hmm, that's a corner point.

Wait, but we also need sinθ ≤ 17/s-2 and cosθ ≤ 17/s-3. At θ = 0: cosθ = 1 ≤ 17/s-3 requires s ≤ 17/4 = 4.25. And sinθ = 0 ≤ 17/s-2 always. So for s ≤ 4.25, we can use θ = 0.

For s > 4.25, cosθ = 1 > 17/s-3, so θ = 0 is not feasible. The minimum of A·cosθ+B·sinθ in the feasible region is achieved at the boundary cosθ = 17/s-3 (i.e., x₁ = 17-3s, the maximum allowed). Then sinθ = √(1-(17/s-3)²) and y₁ = s·sinθ.

This is getting complicated. Let me try a different approach.

Let me consider the possibility that the optimal configuration has a different structure. Maybe not 4+4+3+3.

Actually, let me reconsider the problem. The answer is a - √b. Let me think about what values of a and b make sense.

If the answer involves √2 (from cross-corner distances with equal distances from the corner), then a - √b could be something like 17 - √(something) or a multiple.

Let me try the configuration where the binding constraint is between two points on adjacent sides at equal distance d from a corner, giving distance d√2 = s, so d = s/√2. And the same-side spacing is also s.

On a side with k interior points (no corners), with end gaps d = s/√2 and interior spacing s:
2d + (k-1)s = 17
2(s/√2) + (k-1)s = 17
s√2 + (k-1)s = 17
s(√2 + k - 1) = 17
s = 17/(k-1+√2)

For this to give a - √b, we need 17/(k-1+√2) = 17(k-1-√2)/((k-1)²-2) = a - √b.

For k = 3: s = 17/(2+√2) = 17(2-√2)/(4-2) = 17(2-√2)/2 = 17 - 17√2/2. Not integer a, b.

For k = 4: s = 17/(3+√2) = 17(3-√2)/(9-2) = 17(3-√2)/7 = 51/7 - 17√2/7. Not integer a, b.

Hmm, these don't give integer a, b. The issue is the denominator.

What if the end gaps are not s/√2 but something else? Let me think about configurations where the end gaps on different sides are different.

Let me try: on two opposite sides, k points with end gaps p and interior spacing s. On the other two sides, m points with end gaps q and interior spacing s. Cross-corner: √(p²+q²) = s.

2p + (k-1)s = 17 → p = (17-(k-1)s)/2
2q + (m-1)s = 17 → q = (17-(m-1)s)/2

p² + q² = s²:
((17-(k-1)s)/2)² + ((17-(m-1)s)/2)² = s²
(17-(k-1)s)² + (17-(m-1)s)² = 4s²

Let a = k-1, b = m-1.
(17-as)² + (17-bs)² = 4s²
289-34as+a²s² + 289-34bs+b²s² = 4s²
(a²+b²-4)s² - 34(a+b)s + 578 = 0

For 4+4+3+3: k=4, m=3, a=3, b=2.
(9+4-4)s² - 34·5·s + 578 = 0
9s² - 170s + 578 = 0
s = (170 ± √(28900-20808))/18 = (170 ± √8092)/18 = (170 ± 34√7)/18 = (85 ± 17√7)/9

As before. s = (85-17√7)/9. Not a - √b.

For 5+5+2+2: k=5, m=2, a=4, b=1.
(16+1-4)s² - 34·5·s + 578 = 0
13s² - 170s + 578 = 0
Discriminant: 28900-30056 = -1156 < 0. No real solution.

For 4+4+4+2: k=4, m=2, a=3, b=1. But this is 4+4+4+2 = 14 with 2-fold symmetry? Opposite sides have same count: 4+2+4+2 = 14. So k=4, m=2.
(9+1-4)s² - 34·4·s + 578 = 0
6s² - 136s + 578 = 0
3s² - 68s + 289 = 0
s = (68 ± √(4624-3468))/6 = (68 ± √1156)/6 = (68 ± 34)/6
s = 102/6 = 17 or s = 34/6 = 17/3.

s = 17 is too large (can't have minimum distance 17 on a 17×17 square with 14 points). s = 17/3 ≈ 5.667.

But as we saw, s = 17/3 leads to corner coincidences (12 points, not 14). So this doesn't work for 14 distinct points.

For 3+3+4+4: same as 4+4+3+3.

For 5+3+5+3: k=5, m=3, a=4, b=2.
(16+4-4)s² - 34·6·s + 578 = 0
16s² - 204s + 578 = 0
8s² - 102s + 289 = 0
s = (102 ± √(10404-9248))/16 = (102 ± √1156)/16 = (102 ± 34)/16
s = 136/16 = 8.5 or s = 68/16 = 4.25.

s = 4.25 = 17/4 (rational, same as corner config). s = 8.5 too large.

For 6+1+6+1: k=6, m=1, a=5, b=0.
(25+0-4)s² - 34·5·s + 578 = 0
21s² - 170s + 578 = 0
Discriminant: 28900-4·21·578 = 28900-48552 < 0. No real solution.

For 3+4+3+4: same as 4+4+3+3.

For 5+2+5+2: already done, no real solution.

For 4+3+4+3: same as 4+4+3+3.

Hmm, so the only configurations with 2-fold symmetry (opposite sides same count) that give real solutions are:
- 4+4+3+3: s = (85-17√7)/9 ≈ 4.447
- 4+4+4+2: s = 17/3 ≈ 5.667 (but only 12 distinct points)
- 5+5+3+3: s = 17/4 = 4.25 or s = 8.5 (too large)

Wait, 5+5+3+3 = 16, not 14. Let me recheck. 5+5+2+2 = 14, 4+4+3+3 = 14, 4+4+4+2 = 14, 3+3+4+4 = 14, 5+3+5+3 = 16. 

Hmm, 5+3+5+3 = 16, not 14. Let me recalculate. For 14 points with 2-fold symmetry (opposite sides equal): possible distributions are (a, b, a, b) with 2a+2b = 14, so a+b = 7. Options: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).

So: 1+6+1+6, 2+5+2+5, 3+4+3+4, 4+3+4+3, 5+2+5+2, 6+1+6+1.

I already computed:
- 3+4+3+4 (= 4+4+3+3): s = (85-17√7)/9 ≈ 4.447
- 4+2+4+2 (= 4+4+2+2): s = 17/3 (12 points) or 17 (too large)
- 5+2+5+2: no real solution
- 2+5+2+5: same as 5+2+5+2
- 1+6+1+6: k=1, m=6, a=0, b=5. (0+25-4)s²-34·5·s+578 = 0 → 21s²-170s+578 = 0, discriminant < 0.
- 6+1+6+1: same as 1+6+1+6.

So the best real solution is 3+4+3+4 with s = (85-17√7)/9 ≈ 4.447.

But this isn't of the form a - √b! Let me re-examine.

(85-17√7)/9. Let me see if this can be written as a - √b.

a - √b = (85-17√7)/9. If a = 85/9, that's not an integer. So this doesn't work.

Hmm. Maybe my approach is wrong. Let me reconsider the problem.

Wait, maybe the configuration doesn't have 2-fold symmetry. Or maybe the optimal configuration uses corners in a different way.

Let me reconsider. Maybe the optimal configuration has some points at corners and some not, with a non-symmetric arrangement.

Actually, let me reconsider the 4+4+2+2 configuration (s = 17/3) more carefully. The issue was that at s = 17/3, we get 12 distinct points because of corner coincidences. But what if we don't require equal spacing? Maybe we can have 14 distinct points with minimum distance close to 17/3.

Actually, the 4+4+2+2 configuration has 4+4+2+2 = 12 points on the sides (not counting corners separately). Wait, no. In the 4+4+2+2 configuration, the 4-point sides have 4 points each and the 2-point sides have 2 points each, totaling 12. But we need 14. So 4+4+2+2 only gives 12 points. That's wrong.

Oh wait, I think I miscounted. Let me recheck. 4+4+2+2 = 12, not 14. So this distribution doesn't have 14 points. I made an error earlier.

Let me redo. For 14 points with 2-fold symmetry (opposite sides equal): 2a+2b = 14, a+b = 7. The distributions are (a,b) = (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). These give 2+12, 4+10, 6+8, 8+6, 10+4, 12+2 total points. All sum to 14. ✓

So 3+4 means 3 on one pair of opposite sides and 4 on the other, giving 6+8 = 14. ✓
4+2 means 4 on one pair and 2 on the other, giving 8+4 = 12. ✗ Wait, 2·4 + 2·2 = 8+4 = 12 ≠ 14.

Hmm, 2a+2b = 14 → a+b = 7. If a=4, b=3: 2·4+2·3 = 8+6 = 14. ✓
If a=4, b=2: 2·4+2·2 = 8+4 = 12 ≠ 14. So (4,2) is not valid since 4+2 = 6 ≠ 7.

I made an error. Let me redo. a+b = 7, so the valid pairs are (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).

For (3,4): k=4, m=3 (or k=3, m=4). I computed s = (85-17√7)/9.
For (2,5): k=5, m=2. I computed discriminant < 0.
For (1,6): k=6, m=1. Discriminant < 0.

So the only valid 2-fold symmetric configuration with a real solution is (3,4), giving s = (85-17√7)/9.

But this isn't a - √b. So either:
1. The optimal configuration doesn't have 2-fold symmetry.
2. The optimal configuration has a different structure (e.g., using corners).
3. I'm making an error somewhere.

Let me reconsider. Maybe the optimal configuration uses some corners but not all, or has a different symmetry.

Actually, let me reconsider the problem. Maybe the answer involves a different kind of configuration. Let me think about what a - √b could be.

If a and b are positive integers, and the answer is around 4.447, then a - √b ≈ 4.447. So a ≈ 4.447 + √b. For b = 1: a ≈ 5.447, not integer. b = 4: a ≈ 6.447, not integer. b = 9: a ≈ 7.447, not integer. b = 16: a ≈ 8.447, not integer. b = 25: a ≈ 9.447, not integer.

Hmm, none of these work for s ≈ 4.447. So maybe the answer isn't (85-17√7)/9.

Let me reconsider. Maybe the optimal configuration is different from what I've been trying.

Let me think about configurations without any symmetry. Or configurations with a different kind of symmetry.

Actually, let me reconsider the problem. Maybe I should think about it as placing 14 points on the perimeter, where the perimeter is a 1D curve, and the distance is Euclidean.

Let me think about the problem differently. The perimeter has 4 sides of length 17. Let me "unfold" the perimeter into a line segment of length 68, with the understanding that the Euclidean distance between two points depends on their positions on the perimeter.

Actually, let me think about a specific configuration that might give a - √b.

Consider placing points at the 4 corners and 10 other points. But we saw this gives 17/4.

What if we place points at only 2 corners (opposite corners) and 12 other points?

With 2 corners (say (0,0) and (17,17)) and 12 edge points. By 2-fold symmetry (180° rotation about (8.5, 8.5)), the 12 edge points are paired. So 6 on each "half".

The sides: bottom (0,0) to (17,0), right (17,0) to (17,17), top (17,17) to (0,17), left (0,17) to (0,0).

(0,0) is a corner point. (17,17) is a corner point. The bottom side has (0,0) at one end. The left side has (0,0) at one end. The top side has (17,17) at one end. The right side has (17,17) at one end.

With 180° rotation symmetry, if we place p points on the bottom (excluding (0,0)), then we place p points on the top (excluding (17,17)). If we place q points on the right (excluding (17,17)), then q on the left (excluding (0,0)). Total: 2 + 2p + 2q = 14, so p + q = 6.

Options: (p,q) = (0,6), (1,5), (2,4), (3,3), (4,2), (5,1), (6,0).

Let me try (p,q) = (3,3): 3 points on each side (excluding the corner point).

Bottom: (0,0) + 3 points at x₁ < x₂ < x₃. By 180° rotation, top has (17,17) + 3 points at 17-x₃, 17-x₂, 17-x₁.
Right: (17,17) + 3 points at y₁ < y₂ < y₃ (from (17,0) upward). By rotation, left has (0,0) + 3 points at 17-y₃, 17-y₂, 17-y₁ (from (0,0) upward).

Wait, I need to be more careful. The right side goes from (17,0) to (17,17). (17,17) is a corner point. So the 3 right-side points are at distances y₁, y₂, y₃ from (17,0), with y₃ < 17. By 180° rotation, the left side has points at (0, 17-y₃), (0, 17-y₂), (0, 17-y₁) (from (0,0), these are at distances 17-y₃, 17-y₂, 17-y₁ from (0,0)). And (0,0) is a corner point on the left.

So on the bottom: points at 0, x₁, x₂, x₃ (from (0,0)). Spacings: x₁, x₂-x₁, x₃-x₂, 17-x₃ (end gap to (17,0)).
On the left: points at 0, 17-y₃, 17-y₂, 17-y₁ (from (0,0)). Spacings: 17-y₃, y₃-y₂, y₂-y₁, y₁ (end gap to (0,17)).

Cross-corner at (0,0): the corner point (0,0) is shared by bottom and left. The nearest bottom point is at x₁, distance x₁. The nearest left point is at 17-y₃, distance 17-y₃. These are same-side distances from the corner point, so the minimum distance involving (0,0) is min(x₁, 17-y₃).

Cross-corner at (17,0): no corner point here. Nearest bottom point: x₃, distance 17-x₃. Nearest right point: y₁, distance y₁. Cross-corner distance: √((17-x₃)² + y₁²).

Cross-corner at (0,17): no corner point here. Nearest left point: 17-y₁, distance y₁ (from (0,17)). Nearest top point: 17-x₃ (from (0,17) along the top, the nearest is at 17-x₃ from the left, so distance 17-x₃ from (0,17)). Wait, the top goes from (0,17) to (17,17). The top points are at 17-x₃, 17-x₂, 17-x₁, 17 (from left). Nearest to (0,17) is at 17-x₃, distance 17-x₃. Cross-corner: √((17-x₃)² + y₁²). Same as (17,0) by symmetry. ✓

Cross-corner at (17,17): corner point. Nearest top point: 17-x₁, distance x₁ (from (17,17)). Nearest right point: 17-y₁, distance 17-y₁... wait, the right side points are at y₁, y₂, y₃ from (17,0). (17,17) is at distance 17 from (17,0). Nearest right point to (17,17) is at y₃, distance 17-y₃. So the minimum distance involving (17,17) is min(x₁, 17-y₃) (same as (0,0) by symmetry). ✓

So the constraints are:
1. Same-side bottom: min(x₁, x₂-x₁, x₃-x₂) ≥ s (the end gap 17-x₃ is to a non-point corner, so it doesn't count for same-side, but it appears in cross-corner)
2. Same-side left: min(17-y₃, y₃-y₂, y₂-y₁) ≥ s
3. Same-side right: min(y₁, y₂-y₁, y₃-y₂) ≥ s (end gap 17-y₃ to corner (17,17))
4. Same-side top: min(17-x₃, x₃-x₂, x₂-x₁) ≥ s (end gap x₁ to corner (17,17))... wait, top points are at 17-x₃, 17-x₂, 17-x₁, 17 from left. Spacings: 17-x₃, x₃-x₂, x₂-x₁, x₁. Same-side min: min(17-x₃, x₃-x₂, x₂-x₁). (End gap x₁ is to corner (17,17).)
5. Corner (0,0): min(x₁, 17-y₃) ≥ s
6. Corner (17,17): min(x₁, 17-y₃) ≥ s (same as 5 by symmetry)
7. Cross-corner (17,0) and (0,17): √((17-x₃)² + y₁²) ≥ s

By symmetry (180° rotation), constraints 1 and 4 are the same, 2 and 3 are the same. So:
- min(x₁, x₂-x₁, x₃-x₂, 17-x₃) ≥ s (bottom/top same-side + end gaps that are to non-point corners)

Wait, I need to be more careful. The end gap 17-x₃ on the bottom is the distance from the last bottom point to the corner (17,0), which is not a point. So this end gap doesn't directly constrain s (there's no point at (17,0)). But it appears in the cross-corner constraint 7.

Similarly, the end gap x₁ on the bottom is the distance from (0,0) (which IS a point) to the first bottom point. So x₁ ≥ s is a constraint (constraint 5).

And 17-y₃ on the left is the distance from (0,0) to the first left point. So 17-y₃ ≥ s (constraint 5).

And y₁ on the right is the distance from (17,0) (not a point) to the first right point. Not a direct constraint, but appears in cross-corner.

And 17-y₁ on the right is the distance from (17,17) (a point) to the last right point. So 17-y₁ ≥ s. But by symmetry, this is the same as 17-y₃ on the left... hmm, no. Let me recheck.

Right side: points at y₁, y₂, y₃ from (17,0). (17,17) is at distance 17 from (17,0). Distance from (17,17) to nearest right point (y₃): 17-y₃. So 17-y₃ ≥ s.

Left side: points at 17-y₃, 17-y₂, 17-y₁ from (0,0). (0,0) is a point. Distance from (0,0) to nearest left point (17-y₃): 17-y₃. So 17-y₃ ≥ s. Same constraint. ✓

And on the bottom: (0,0) is a point. Distance to nearest bottom point (x₁): x₁. So x₁ ≥ s.
On the top: (17,17) is a point. Distance to nearest top point: the top points are at 17-x₃, 17-x₂, 17-x₁, 17 from left. (17,17) is at position 17 from left. Nearest is at 17, distance 0... wait, (17,17) is at position 17 on the top. The top points include 17 (from the rotation: 17-x₁ where x₁ maps to 17-x₁, and the corner (17,17) is at 17). Actually, the top side has the corner point (17,17) at position 17, and the
