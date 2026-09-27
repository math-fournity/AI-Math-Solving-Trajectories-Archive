# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In acute \(\triangle ABC\), \(AB = 11\) and \(CB = 10\). Points \(E\) and \(D\) are constructed such that \(\angle CBE\) and \(\angle ABD\) are right angles, and \(ACEBD\) is a non-degenerate pentagon. Additionally, \(\angle AEB \cong \angle DCB\), \(AE = CD\), and \(ED = 20\). Given that \(EA\) and \(CD\) intersect at \(P\) and \(AP = 4\), find \(CP^2\).       — 题目文本
#   First, note that because \(\angle AEB \cong \angle DCB\), \(AE = DC\), and \(m \angle CBD = 90^\circ + m \angle ABC = m \angle EBA\), we have \(\triangle AEB \cong \triangle DCB\). Thus, \(DB = AB = 11\) and \(EB = CB = 10\). Notice that \(\angle EBA\) and \(\angle CBA\) are supplementary. 

Applying the law of cosines on \(\triangle EBD\):

\[
20^2 = 10^2 + 11^2 - 2 \cdot 11 \cdot 10 \cdot \cos(\angle EBD)
\]

Applying the law of cosines on \(\triangle ABC\):

\[
\begin{gathered}
AC^2 = 10^2 + 11^2 - 2 \cdot 11 \cdot 10 \cdot \cos(180^\circ - \angle EBD) \\
AC^2 = 10^2 + 11^2 + 2 \cdot 11 \cdot 10 \cdot \cos(\angle EBD)
\end{gathered}
\]

Then we have:

\[
\begin{gathered}
AC^2 + 20^2 = 2(10^2 + 11^2) \\
AC^2 = 42
\end{gathered}
\]

Also, notice that \(\triangle AEB\) is a \(90^\circ\) rotation of \(\triangle DCB\), so \(\overline{DC}\) and \(\overline{AE}\) must be perpendicular. Thus, \(\triangle APC\) is a right triangle, so we have:

\[
\begin{gathered}
42 = 4^2 + CP^2 \\
CP^2 = 26
\end{gathered}
\]

\(\boxed{26}\)  — 标准解答
#   Let me analyze this problem carefully.

We have acute triangle ABC with AB = 11, CB = 10. Points E and D are constructed such that ∠CBE and ∠ABD are right angles, and ACEBD is a non-degenerate pentagon. Also ∠AEB ≅ ∠DCB, AE = CD, and ED = 20. EA and CD intersect at P with AP = 4. Find CP².

Let me set up coordinates. Let me place B at the origin.

Since ∠CBE is a right angle, E is on a line through B perpendicular to BC.
Since ∠ABD is a right angle, D is on a line through B perpendicular to BA.

Let me place B at origin. Let me put the triangle in a coordinate system.

Let me think about the configuration. ACEBD is a pentagon, so the order of vertices is A, C, E, B, D. This means going around the pentagon: A → C → E → B → D → A.

So the pentagon has vertices A, C, E, B, D in that order. The sides are AC, CE, EB, BD, DA.

∠CBE is a right angle - this is the angle at B in the pentagon (between sides EB and BC... wait, but BC isn't a side of the pentagon). Actually ∠CBE is the angle at vertex B formed by rays BC and BE. In the pentagon ACEBD, at vertex B the sides are EB and BD. So ∠CBE is between BC (a diagonal) and BE (a side). Hmm, let me reconsider.

Actually, let me reconsider. ∠CBE = 90° means the angle at B between BC and BE is 90°. ∠ABD = 90° means the angle at B between BA and BD is 90°.

So E is on the line through B perpendicular to BC, and D is on the line through B perpendicular to BA.

Let me set up coordinates. Place B at origin. Let BC be along some direction and BA along another.

Let me say the angle at B in triangle ABC is β. So ∠ABC = β.

Place B at origin, C at (10, 0) (since BC = 10). Then A is at distance 11 from B, making angle β with BC. So A = (11cos β, 11sin β).

Since triangle is acute, β is between 0 and π.

E is on the line through B perpendicular to BC. BC is along the x-axis, so E is on the y-axis: E = (0, e) for some e (could be positive or negative).

D is on the line through B perpendicular to BA. BA direction is (cos β, sin β), so perpendicular direction is (-sin β, cos β). So D = d·(-sin β, cos β) for some d.

Now, ACEBD is a non-degenerate pentagon with vertices in order A, C, E, B, D. For this to be a valid (non-self-intersecting) pentagon, we need to think about the positions.

Let me think about the order. Going A → C → E → B → D → A. 

A = (11cos β, 11sin β), C = (10, 0), E = (0, e), B = (0,0), D = d(-sin β, cos β).

For the pentagon to be non-degenerate and the vertices to be in this order (say counterclockwise), let me think about where E and D should be.

If β is acute (triangle is acute, so β < 90°), then A is in the first quadrant (positive x, positive y).

For the pentagon A, C, E, B, D to go counterclockwise:
- A is at angle β from x-axis (in first quadrant)
- C is at (10, 0) on positive x-axis
- E is on y-axis
- B is at origin
- D is at angle (β + 90°) from x-axis

Hmm, for the pentagon to make sense, E should be above B (positive y) so that going from C to E to B makes sense. And D should be positioned so that going from B to D to A makes sense.

Let me think counterclockwise. If we go counterclockwise:
- Start at A (upper left-ish, angle β)
- Go to C (on positive x-axis, angle 0) - this is clockwise from A, so maybe the pentagon is clockwise?

Let me think again. The order A, C, E, B, D. 

A is at angle β (first quadrant), C is at angle 0 (positive x-axis), E is at angle 90° (if e > 0, positive y-axis), B is at origin, D is at angle β + 90°.

Going A → C: from angle β to angle 0, that's clockwise.
Going C → E: from angle 0 to angle 90°, that's counterclockwise.

This doesn't form a simple polygon easily. Let me reconsider.

Maybe E is below the x-axis (e < 0), so E is at angle -90° or 270°.

Going A (angle β) → C (angle 0) → E (angle 270° or -90°) → B (origin) → D (angle β+90°) → A.

Hmm, this is getting complicated. Let me just set up the equations and not worry too much about the geometric configuration for now.

Conditions:
1. ∠AEB ≅ ∠DCB
2. AE = CD
3. ED = 20
4. AP = 4 where P is intersection of EA and CD.

Let me compute.

A = (11cos β, 11sin β)
C = (10, 0)
E = (0, e)
D = (-d sin β, d cos β)

AE = CD:
AE² = (11cos β - 0)² + (11sin β - e)² = 121cos²β + (11sin β - e)² = 121 - 22e sin β + e²
CD² = (10 + d sin β)² + (0 - d cos β)² = 100 + 20d sin β + d² sin²β + d² cos²β = 100 + 20d sin β + d²

So AE = CD gives: 121 - 22e sin β + e² = 100 + 20d sin β + d²
→ 21 - 22e sin β + e² - 20d sin β - d² = 0 ... (i)

∠AEB ≅ ∠DCB:

∠AEB is the angle at E in triangle AEB. 
∠DCB is the angle at C in triangle DCB.

Let me compute these angles using vectors or the cosine.

At E: vectors EA = A - E = (11cos β, 11sin β - e) and EB = B - E = (0, -e).
cos(∠AEB) = (EA · EB) / (|EA| |EB|) = (11cos β · 0 + (11sin β - e)(-e)) / (AE · |e|)
= (-11e sin β + e²) / (AE · |e|)
= (e² - 11e sin β) / (AE · |e|)
= e(e - 11 sin β) / (AE · |e|)

If e > 0, |e| = e, so cos(∠AEB) = (e - 11 sin β) / AE
If e < 0, |e| = -e, so cos(∠AEB) = (e - 11 sin β) / (AE · (-1)) = (11 sin β - e) / AE

Let me keep it general: cos(∠AEB) = (e² - 11e sin β) / (AE · |e|)

At C: vectors CD = D - C = (-d sin β - 10, d cos β) and CB = B - C = (-10, 0).
cos(∠DCB) = (CD · CB) / (|CD| |CB|) = ((-d sin β - 10)(-10) + d cos β · 0) / (CD · 10)
= (10d sin β + 100) / (10 · CD)
= (d sin β + 10) / CD

So ∠AEB ≅ ∠DCB means:
(e² - 11e sin β) / (AE · |e|) = (d sin β + 10) / CD

Since AE = CD, this simplifies to:
(e² - 11e sin β) / |e| = d sin β + 10

If e > 0: (e - 11 sin β) = d sin β + 10 → e - d sin β = 10 + 11 sin β ... (ii)
If e < 0: (11 sin β - e) = d sin β + 10 → -e - d sin β = 10 - 11 sin β → e + d sin β = 11 sin β - 10 ... (ii')

ED = 20:
ED² = (0 - (-d sin β))² + (e - d cos β)² = d² sin²β + e² - 2ed cos β + d² cos²β = d² + e² - 2ed cos β = 400 ... (iii)

Now, P is the intersection of lines EA and CD, with AP = 4.

Line EA: from E(0, e) to A(11cos β, 11sin β). Parametrize: P = E + t(A - E) = (11t cos β, e + t(11sin β - e)) for parameter t. When t=0, P=E; when t=1, P=A.

AP = 4 means |P - A| = 4. P - A = (1-t)(A - E) = (1-t)(11cos β, 11sin β - e). So |P - A| = |1-t| · AE = 4.
So |1 - t| = 4/AE, meaning t = 1 - 4/AE or t = 1 + 4/AE.

Line CD: from C(10, 0) to D(-d sin β, d cos β). Parametrize: P = C + s(D - C) = (10 + s(-d sin β - 10), s · d cos β) for parameter s. When s=0, P=C; when s=1, P=D.

CP = |P - C| = |s| · CD. So CP² = s² · CD² = s² · AE² (since AE = CD).

We need to find CP² = s² · AE².

At intersection, the two parametrizations are equal:
11t cos β = 10 + s(-d sin β - 10) = 10 - s(10 + d sin β) ... (iv)
e + t(11sin β - e) = s · d cos β ... (v)

This is getting complex. Let me try to think about this differently.

Actually, let me reconsider the problem. The conditions ∠AEB ≅ ∠DCB and AE = CD suggest some kind of congruence or similarity between triangles AEB and DCB.

In triangle AEB: sides AE, EB, AB = 11.
In triangle DCB: sides DC, CB = 10, DB.

We have AE = CD and ∠AEB = ∠DCB. 

If triangles AEB and DCB were similar with AE corresponding to DC and ∠AEB corresponding to ∠DCB, then the similarity would be:
A ↔ D, E ↔ C, B ↔ B (or some other correspondence).

Let me check: if the correspondence is A↔D, E↔C, B↔B:
- AE ↔ DC ✓ (given AE = CD)
- ∠AEB ↔ ∠DCB ✓ (given)
- EB ↔ CB = 10
- AB = 11 ↔ DB

So if triangles AEB ~ DCB with this correspondence, then:
AE/DC = EB/CB = AB/DB
Since AE = CD, AE/DC = 1, so EB = CB = 10 and AB = DB = 11.

So EB = 10 and DB = 11. That means e = ±10 (since E = (0, e) and EB = |e| = 10) and d = 11 (since DB = d = 11).

Wait, but this would make the triangles congruent, not just similar. Let me check: AE = CD (given), EB = CB = 10, AB = DB = 11. By SSS, triangles AEB ≅ DCB. And ∠AEB = ∠DCB is consistent.

But wait, is this necessarily the case? The conditions only give us AE = CD and ∠AEB = ∠DCB. This is SSA (side-side-angle), which doesn't uniquely determine congruence. There could be two configurations.

But let me explore the congruent case first: EB = 10, DB = 11, i.e., e = ±10, d = 11.

Case 1: e = 10, d = 11.

From (ii): e - d sin β = 10 + 11 sin β
10 - 11 sin β = 10 + 11 sin β
-11 sin β = 11 sin β
sin β = 0. 

That's degenerate. So e = 10 doesn't work with this.

Case 2: e = -10, d = 11.

From (ii'): e + d sin β = 11 sin β - 10
-10 + 11 sin β = 11 sin β - 10
-10 = -10 ✓

So e = -10, d = 11 works for any β! Let me check with (i):
21 - 22e sin β + e² - 20d sin β - d² = 0
21 - 22(-10) sin β + 100 - 20(11) sin β - 121 = 0
21 + 220 sin β + 100 - 220 sin β - 121 = 0
21 + 100 - 121 = 0
0 = 0 ✓

Great, so e = -10, d = 11 satisfies (i) and (ii') for any β.

Now check (iii): ED² = d² + e² - 2ed cos β = 121 + 100 - 2(11)(-10) cos β = 221 + 220 cos β = 400
220 cos β = 179
cos β = 179/220

Let me verify: sin²β + cos²β = 1. sin²β = 1 - (179/220)² = 1 - 32041/48400 = (48400 - 32041)/48400 = 16359/48400.

Hmm, let me check if 16359 is a perfect square. √16359 ≈ 127.9. 128² = 16384. So 16359 is not a perfect square. Let me double-check: 127² = 16129, 128² = 16384. 16359 is between them, not a perfect square.

Hmm, but the problem should have a nice answer. Let me reconsider.

Wait, maybe the triangles aren't congruent. Let me reconsider the SSA case.

Actually, let me reconsider. The conditions are AE = CD and ∠AEB = ∠DCB. In triangle AEB, we know AB = 11. In triangle DCB, we know CB = 10. 

With AE = CD and ∠AEB = ∠DCB, this is like SSA. Let me use the law of sines.

In triangle AEB: AE/sin(∠ABE) = AB/sin(∠AEB) = EB/sin(∠EAB)
In triangle DCB: DC/sin(∠DBC) = CB/sin(∠DCB) = DB/sin(∠DCB... wait, ∠DCB is at C.

Let me be more careful.

In triangle AEB:
- ∠AEB at E (given equal to ∠DCB)
- ∠ABE at B
- ∠EAB at A
- AB = 11, AE, EB

In triangle DCB:
- ∠DCB at C (given equal to ∠AEB)
- ∠DBC at B
- ∠BDC at D
- CB = 10, CD, DB

By law of sines in triangle AEB: AE/sin(∠ABE) = 11/sin(∠AEB)
By law of sines in triangle DCB: CD/sin(∠DBC) = 10/sin(∠DCB)

Since AE = CD and ∠AEB = ∠DCB:
sin(∠ABE) = (AE/11) sin(∠AEB) ... from first
sin(∠DBC) = (CD/10) sin(∠DCB) = (AE/10) sin(∠AEB) ... from second

So sin(∠ABE)/sin(∠DBC) = (AE/11)/(AE/10) = 10/11.

Now, ∠ABE + ∠DBC = ∠ABD - ∠EBD... wait, no. Let me think about the angles at B.

∠ABD = 90° (given). ∠CBE = 90° (given).

The angles at B: ∠ABE, ∠EBC (or ∠CBE), ∠CBD (or ∠DBC), ∠DBA (or ∠ABD).

We know ∠CBE = 90° and ∠ABD = 90°.

The full angle around B is 360°. The angles are ∠ABE, ∠EBC = 90°, ∠CBD, ∠DBA = 90°.
So ∠ABE + 90° + ∠CBD + 90° = 360° (if these four angles partition the full angle).
→ ∠ABE + ∠CBD = 180°.

Wait, that's only if the four rays BA, BE, BC, BD are arranged so that the four angles partition 360°. Let me think about this more carefully.

Actually, the four rays from B are BA, BC, BE, BD. We know ∠CBE = 90° (angle between BC and BE) and ∠ABD = 90° (angle between BA and BD).

The angle ∠ABC = β (angle of the triangle at B).

Let me think about the arrangement. In the pentagon ACEBD, the order is A, C, E, B, D. So going around B, the neighbors in the pentagon are E and D (since ...E, B, D... in the sequence). 

Let me think about the angular arrangement of the four rays from B. 

If we go counterclockwise around B, we might have: BA, BE, BC, BD or some other order.

∠CBE = 90°: the angle from BC to BE is 90°.
∠ABD = 90°: the angle from BA to BD is 90°.
∠ABC = β: the angle from BA to BC is β.

Let me consider the counterclockwise order. If the order is BA, BE, BC, BD (counterclockwise):
- ∠ABE (from BA to BE counterclockwise) = some angle α
- ∠EBC (from BE to BC counterclockwise) = 90° (since ∠CBE = 90°, and this is the same angle)
- ∠CBD (from BC to BD counterclockwise) = some angle γ
- ∠DBA (from BD to BA counterclockwise) = 90° (since ∠ABD = 90°)

Total: α + 90° + γ + 90° = 360° → α + γ = 180°.

Also, ∠ABC = β. From BA counterclockwise to BC: α + 90° = β. So α = β - 90°.

Since the triangle is acute, β < 90°, so α = β - 90° < 0. That's impossible.

Let me try the order BA, BD, BC, BE (counterclockwise):
- ∠ABD = 90° (from BA to BD) ✓
- ∠DBC (from BD to BC) = some angle γ
- ∠CBE = 90° (from BC to BE) ✓
- ∠EBA (from BE to BA) = some angle α

Total: 90° + γ + 90° + α = 360° → α + γ = 180°.

∠ABC = β: from BA to BC counterclockwise = 90° + γ = β. So γ = β - 90°. Again negative since β < 90°.

Hmm. Let me try clockwise orders or different arrangements.

Maybe the order counterclockwise is BA, BC, BE, BD:
- ∠ABC = β (from BA to BC) ✓
- ∠CBE = 90° (from BC to BE) ✓
- ∠EBD (from BE to BD) = some angle
- ∠DBA = 90° (from BD to BA) ✓ (since ∠ABD = 90°)

Total: β + 90° + ∠EBD + 90° = 360° → ∠EBD = 180° - β.

In this case:
∠ABE = ∠ABC + ∠CBE = β + 90° (the angle from BA to BE going counterclockwise through C)
∠DBC = ∠DBA - ... wait, ∠DBC is the angle from BD to BC. Going from BD counterclockwise to BC would be through BA: ∠DBA + ∠ABC = 90° + β. But that's the reflex angle. The direct angle from BD to BC (going clockwise, i.e., the smaller angle) would be 360° - (90° + β) = 270° - β. Hmm, that's more than 180°.

Actually, I need to be more careful. ∠DBC is the angle at B in triangle DBC, which is the angle between rays BD and BC. The angle between two rays is always taken to be ≤ 180°.

With the counterclockwise order BA, BC, BE, BD:
- Angle from BA to BC (counterclockwise) = β
- Angle from BC to BE (counterclockwise) = 90°
- Angle from BE to BD (counterclockwise) = 180° - β
- Angle from BD to BA (counterclockwise) = 90°

The angle between BD and BC: going counterclockwise from BC to BD is 90° + (180° - β) = 270° - β. Going clockwise from BC to BD is β + 90°. The smaller angle is min(270° - β, 90° + β). Since β is acute (0 < β < 90°), 90° + β < 180° and 270° - β > 180°. So the angle between BD and BC is 90° + β.

So ∠DBC = 90° + β. But this is more than 90°, and in triangle DBC, we'd have an obtuse angle at B. That's fine.

And ∠ABE: angle between BA and BE. Going counterclockwise from BA to BE is β + 90°. Going clockwise is 360° - (β + 90°) = 270° - β. The smaller is β + 90° (since β < 90°, β + 90° < 180°). So ∠ABE = β + 90°.

But wait, in triangle ABE, ∠ABE = 90° + β. That's an obtuse angle. And ∠AEB is given. Then ∠EAB = 180° - (90° + β) - ∠AEB = 90° - β - ∠AEB. For this to be positive, ∠AEB < 90° - β.

In triangle DCB, ∠DBC = 90° + β (obtuse), ∠DCB = ∠AEB, ∠BDC = 180° - (90° + β) - ∠AEB = 90° - β - ∠AEB.

So triangles AEB and DCB have:
- ∠AEB = ∠DCB (given)
- ∠ABE = 90° + β = ∠DBC
- ∠EAB = 90° - β - ∠AEB = ∠BDC

So the triangles are similar! AEB ~ DCB with correspondence A↔D, E↔C, B↔B.

And the ratio: AB/DB = AE/DC = EB/CB.
Since AE = CD (given), AE/DC = 1, so the triangles are congruent!
AB = DB = 11, EB = CB = 10.

So indeed EB = 10, DB = 11, and the triangles are congruent.

Now, with the counterclockwise order BA, BC, BE, BD, and E on the positive y side... let me reconsider coordinates.

Wait, I had e = -10 earlier. Let me reconcile.

With B at origin, C at (10, 0), A at (11cos β, 11sin β) with β acute (so A in first quadrant).

The counterclockwise order of rays from B is: BA (at angle β), BC (at angle 0), BE (at angle 90° from BC, so at angle 90°), BD (at angle 90° from BA, so at angle β + 90°).

Wait, I need to check: counterclockwise order BA, BC, BE, BD means:
- BA at angle β
- BC at angle 0

But going counterclockwise from BA (angle β) to BC (angle 0)... that's going clockwise (decreasing angle). So the counterclockwise order would be BC (angle 0), BA (angle β), ... 

Hmm, let me reconsider. Counterclockwise means increasing angle. So:
- BC at angle 0
- BA at angle β (since 0 < β < 90°)
- BD at angle β + 90° (90° counterclockwise from BA)
- BE at angle 90° (90° counterclockwise from BC)

So counterclockwise order: BC (0°), BA (β), BE (90°), BD (β+90°).

Wait, is β < 90°? Yes. And β + 90° vs 90°: β + 90° > 90°. So the order is: BC (0°), BA (β), BE (90°), BD (β + 90°).

Hmm, but the pentagon order is A, C, E, B, D. Let me check if this is consistent with a simple polygon.

The vertices in order:
A = (11cos β, 11sin β) - first quadrant
C = (10, 0) - on positive x-axis
E = (0, 10) - on positive y-axis (since e = 10 now, as EB = 10 and E is at angle 90°)
B = (0, 0) - origin
D = 11(-sin β, cos β) - at angle β + 90°, in second quadrant

Going A → C → E → B → D → A:
A (first quadrant) → C (positive x-axis) → E (positive y-axis) → B (origin) → D (second quadrant) → A (first quadrant)

This could form a simple polygon. Let me check: A is in the first quadrant, C is on the positive x-axis, E is on the positive y-axis, B is at origin, D is in the second quadrant. Going A → C → E → B → D → A, this seems like it could be a simple (non-self-intersecting) pentagon.

But wait, I had earlier derived that e = -10 works but e = 10 doesn't (with the equation from ∠AEB = ∠DCB). Let me recheck with this configuration.

With e = 10 (E at (0, 10)):
cos(∠AEB) = (e² - 11e sin β) / (AE · |e|) = (100 - 110 sin β) / (AE · 10) = (10 - 11 sin β) / AE

cos(∠DCB) = (d sin β + 10) / CD = (11 sin β + 10) / CD = (11 sin β + 10) / AE (since CD = AE)

Setting equal: (10 - 11 sin β) / AE = (11 sin β + 10) / AE
10 - 11 sin β = 11 sin β + 10
-11 sin β = 11 sin β
sin β = 0. Degenerate.

So e = 10 doesn't work. But e = -10 does. So E = (0, -10), which is on the negative y-axis, at angle 270° (or -90°).

Let me reconsider the angular arrangement with E at angle -90° (or 270°).

Rays from B:
- BC at angle 0
- BA at angle β (0 < β < 90°)
- BD at angle β + 90° (90° counterclockwise from BA)
- BE at angle -90° (or 270°)

Counterclockwise order: BC (0°), BA (β), BD (β + 90°), BE (270°).

The angle ∠CBE: from BC (0°) to BE (270°). Going counterclockwise: 270°. Going clockwise: 90°. The angle is 90°. ✓

The angle ∠ABD: from BA (β) to BD (β + 90°). Counterclockwise: 90°. ✓

Now the pentagon order A, C, E, B, D:
A (first quadrant) → C (positive x-axis) → E (negative y-axis) → B (origin) → D (second quadrant) → A

Let me check if this is a simple polygon. 
A is at (11cos β, 11sin β) with sin β > 0, cos β > 0.
C is at (10, 0).
E is at (0, -10).
B is at (0, 0).
D is at (-11 sin β, 11 cos β) with sin β > 0, cos β > 0, so D is in the second quadrant.

A → C: from first quadrant to positive x-axis. OK.
C → E: from (10, 0) to (0, -10). This goes down-left. OK.
E → B: from (0, -10) to (0, 0). This goes straight up. OK.
B → D: from (0, 0) to second quadrant. OK.
D → A: from second quadrant to first quadrant. This could cross other edges. Let me check.

D = (-11 sin β, 11 cos β), A = (11 cos β, 11 sin β).
The segment DA goes from second quadrant to first quadrant. It could cross the segment CE (from (10, 0) to (0, -10)) or other segments.

Actually, for the pentagon to be non-degenerate, it just needs to be a valid pentagon (not necessarily convex). Let me not worry about this and proceed with the computation.

So we have:
e = -10, d = 11
cos β = 179/220 (from ED = 20)

Wait, let me recompute. ED² = d² + e² - 2ed cos β = 121 + 100 - 2(11)(-10) cos β = 221 + 220 cos β = 400.
cos β = (400 - 221) / 220 = 179/220.

sin²β = 1 - (179/220)² = 1 - 32041/48400 = 16359/48400.

Let me factor 16359. 16359 / 3 = 5453. 5453 / 7 = 779. 779 / 19 = 41. So 16359 = 3 × 7 × 19 × 41. Not a perfect square.

Hmm, so sin β = √(16359/48400) = √16359 / 220. This is not clean.

But the problem asks for CP², which might still be a nice number even if intermediate values aren't.

Let me proceed with the computation.

We have:
A = (11cos β, 11sin β)
C = (10, 0)
E = (0, -10)
D = (-11 sin β, 11 cos β)

cos β = 179/220, sin β = √16359 / 220.

Let me denote s = sin β, c = cos β = 179/220.

A = (11c, 11s) = (11·179/220, 11s) = (179/20, 11s)
C = (10, 0)
E = (0, -10)
D = (-11s, 11c) = (-11s, 179/20)

Now, P is the intersection of lines EA and CD.

Line EA: from E(0, -10) to A(179/20, 11s).
Direction: (179/20, 11s + 10).
Parametrize: P = E + t(A - E) = (179t/20, -10 + t(11s + 10)).

Line CD: from C(10, 0) to D(-11s, 179/20).
Direction: (-11s - 10, 179/20).
Parametrize: P = C + u(D - C) = (10 + u(-11s - 10), u · 179/20) = (10 - u(11s + 10), 179u/20).

Setting equal:
179t/20 = 10 - u(11s + 10) ... (1)
-10 + t(11s + 10) = 179u/20 ... (2)

From (1): 179t/20 + u(11s + 10) = 10
From (2): t(11s + 10) - 179u/20 = 10

Let me denote a = 11s + 10 and b = 179/20.

From (1): bt + au = 10
From (2): at - bu = 10

Solving:
From (1): u = (10 - bt)/a
Sub into (2): at - b(10 - bt)/a = 10
a²t - b(10 - bt) = 10a
a²t - 10b + b²t = 10a
t(a² + b²) = 10a + 10b = 10(a + b)
t = 10(a + b) / (a² + b²)

Similarly, from (2): t = (10 + bu)/a, sub into (1):
b(10 + bu)/a + au = 10
b(10 + bu) + a²u = 10a
10b + b²u + a²u = 10a
u(a² + b²) = 10a - 10b = 10(a - b)
u = 10(a - b) / (a² + b²)

Now, AP = |P - A| = |1 - t| · |A - E| = |1 - t| · AE.

We need AE. AE² = (179/20)² + (11s + 10)² = b² + a².

So AE = √(a² + b²).

AP = |1 - t| · √(a² + b²) = |1 - 10(a+b)/(a²+b²)| · √(a²+b²)
= |(a²+b² - 10(a+b))/(a²+b²)| · √(a²+b²)
= |a²+b² - 10a - 10b| / √(a²+b²)

Let me compute a² + b² - 10a - 10b.

a = 11s + 10, b = 179/20.

a² = (11s + 10)² = 121s² + 220s + 100
b² = (179/20)² = 32041/400

a² + b² = 121s² + 220s + 100 + 32041/400

Now s² = 1 - c² = 1 - 32041/48400 = 16359/48400.
121s² = 121 × 16359/48400 = 16359/400 (since 48400 = 400 × 121).

So a² + b² = 16359/400 + 220s + 100 + 32041/400 = (16359 + 32041)/400 + 220s + 100 = 48400/400 + 220s + 100 = 121 + 220s + 100 = 221 + 220s.

10a + 10b = 10(11s + 10) + 10(179/20) = 110s + 100 + 179/2 = 110s + 100 + 89.5 = 110s + 189.5 = 110s + 379/2.

a² + b² - 10a - 10b = 221 + 220s - 110s - 379/2 = 221 + 110s - 379/2 = (442 - 379)/2 + 110s = 63/2 + 110s.

So AP = |63/2 + 110s| / √(221 + 220s).

Since s = sin β > 0 (β is acute), 63/2 + 110s > 0, so:

AP = (63/2 + 110s) / √(221 + 220s)

We're given AP = 4:

(63/2 + 110s) / √(221 + 220s) = 4

63/2 + 110s = 4√(221 + 220s)

Let me square both sides:
(63/2 + 110s)² = 16(221 + 220s)

(63/2)² + 2(63/2)(110s) + (110s)² = 3536 + 3520s

3969/4 + 6930s + 12100s² = 3536 + 3520s

12100s² + 6930s + 3969/4 = 3536 + 3520s

12100s² + (6930 - 3520)s + 3969/4 - 3536 = 0

12100s² + 3410s + (3969/4 - 14144/4) = 0

12100s² + 3410s - 10175/4 = 0

Multiply by 4:
48400s² + 13640s - 10175 = 0

Let me use the quadratic formula:
s = (-13640 ± √(13640² + 4 × 48400 × 10175)) / (2 × 48400)
= (-13640 ± √(186049600 + 19739200000)) / 96800

Wait, let me compute more carefully.

13640² = 13640 × 13640. 
13640 × 13640: 13640 × 13000 = 177,320,000; 13640 × 640 = 8,729,600. Total = 186,049,600.

4 × 48400 × 10175 = 4 × 48400 × 10175.
48400 × 10175 = 48400 × 10000 + 48400 × 175 = 484,000,000 + 8,470,000 = 492,470,000.
4 × 492,470,000 = 1,969,880,000.

Discriminant = 186,049,600 + 1,969,880,000 = 2,155,929,600.

√2,155,929,600 = ? Let me check. 46432² = ? 46000² = 2,116,000,000. 46400² = 2,152,960,000. 46432² = 46432 × 46432. 

46432² = (46400 + 32)² = 46400² + 2×46400×32 + 32² = 2,152,960,000 + 2,969,600 + 1,024 = 2,155,930,624.

That's close but not exactly 2,155,929,600. The difference is 2,155,930,624 - 2,155,929,600 = 1,024. So √2,155,929,600 ≠ 46432.

Let me try 46431² = 46432² - 2×46432 + 1 = 2,155,930,624 - 92,864 + 1 = 2,155,837,761. That's too small.

Hmm, so the discriminant is not a perfect square. Let me recheck my computation.

Actually, wait. Let me recheck. We also have the constraint that s² = 16359/48400, i.e., 48400s² = 16359. Let me use this.

From 48400s² + 13640s - 10175 = 0 and 48400s² = 16359:

16359 + 13640s - 10175 = 0
13640s = 10175 - 16359 = -6184
s = -6184/13640 = -6184/13640

Let me simplify: gcd(6184, 13640). 
6184 = 2 × 3092 = 4 × 1546 = 8 × 773
13640 = 8 × 1705 = 8 × 5 × 341 = 8 × 5 × 11 × 31
773 = ? 773/7 = 110.4, 773/11 = 70.3, 773/13 = 59.5, 773/17 = 45.5, 773/19 = 40.7, 773/23 = 33.6, 773 is prime? 773/773 = 1. √773 ≈ 27.8. Primes up to 27: 2,3,5,7,11,13,17,19,23. 773/3 = 257.7, 773/7 = 110.4, 773/11 = 70.3, 773/13 = 59.5, 773/17 = 45.5, 773/19 = 40.7, 773/23 = 33.6. So 773 is prime.

So s = -773/1705. But s = sin β > 0 (β is acute). This gives s < 0, which is a contradiction!

Hmm, so there's an inconsistency. Let me recheck.

Oh wait, I think the issue is that the AP = 4 condition, combined with the other constraints, might not be compatible with the congruent triangle case. Or maybe I made an error somewhere.

Let me recheck. Actually, wait. The issue might be that the triangles AEB and DCB are NOT congruent. The SSA condition can give two different triangles. Let me reconsider.

We have AE = CD and ∠AEB = ∠DCB. The SSA condition means there could be two cases. In one case the triangles are congruent (which I explored), and in another they're not.

Actually, let me reconsider. The SSA (side-side-angle) ambiguity: given two sides and a non-included angle, there can be 0, 1, or 2 triangles. But here we have two separate triangles, each with their own constraints.

In triangle AEB: we know AB = 11, AE (unknown), ∠AEB (unknown but equals ∠DCB).
In triangle DCB: we know CB = 10, CD = AE (unknown), ∠DCB = ∠AEB (unknown).

The constraint is AE = CD and ∠AEB = ∠DCB. These don't force congruence because the known sides (AB = 11, CB = 10) are different.

Let me redo this without assuming congruence.

Let me use the law of sines approach.

In triangle AEB: AB/sin(∠AEB) = AE/sin(∠ABE) = EB/sin(∠EAB)
In triangle DCB: CB/sin(∠DCB) = CD/sin(∠DBC) = DB/sin(∠BDC)

Since ∠AEB = ∠DCB = θ (say), and AE = CD:
From triangle AEB: 11/sin θ = AE/sin(∠ABE) → AE = 11 sin(∠ABE)/sin θ
From triangle DCB: 10/sin θ = CD/sin(∠DBC) → CD = 10 sin(∠DBC)/sin θ

Since AE = CD: 11 sin(∠ABE) = 10 sin(∠DBC) ... (*)

Now, what are ∠ABE and ∠DBC?

From the angular arrangement (counterclockwise: BC at 0°, BA at β, BE at -90° (or 270°), BD at β+90°):

∠ABE = angle between BA and BE. BA at angle β, BE at angle 270° (or -90°). 
The angle between them: |β - 270°| = 270° - β (going one way) or 360° - (270° - β) = 90° + β (going the other way). The smaller angle is 90° + β (since β < 90°, 90° + β < 180° < 270° - β).

So ∠ABE = 90° + β. (This is the angle in triangle ABE at vertex B.)

∠DBC = angle between BD and BC. BD at angle β + 90°, BC at angle 0°.
The angle: β + 90° (going counterclockwise from BC to BD) or 360° - (β + 90°) = 270° - β (going clockwise). The smaller is β + 90° (since β < 90°, β + 90° < 180°).

So ∠DBC = 90° + β.

So ∠ABE = ∠DBC = 90° + β!

Then from (*): 11 sin(90° + β) = 10 sin(90° + β).
Since sin(90° + β) = cos β ≠ 0 (β is acute), this gives 11 = 10, contradiction!

So this configuration is impossible. That means my angular arrangement is wrong, or the triangles aren't arranged as I thought.

Let me reconsider the angular arrangement. Maybe E is on the other side.

Let me reconsider. We have ∠CBE = 90° and ∠ABD = 90°. There are two possible positions for E (on either side of line BC) and two for D (on either side of line BA).

Let me consider different cases.

Case A: E is on the same side as A (above the x-axis, e > 0), D is on the same side as C.

With B at origin, C at (10, 0), A at (11cos β, 11sin β) (first quadrant, β acute).

E on the line through B perpendicular to BC (y-axis), on the same side as A: E = (0, e) with e > 0.
D on the line through B perpendicular to BA, on the same side as C: The perpendicular to BA is direction (-sin β, cos β) or (sin β, -cos β). "Same side as C" - C is at (10, 0). 

The line BA has direction (cos β, sin β). The perpendicular directions are (-sin β, cos β) and (sin β, -cos β). 

Which side is C on? The line BA passes through origin with direction (cos β, sin β). The normal to this line is (-sin β, cos β). C = (10, 0). The signed distance of C from line BA is C · (-sin β, cos β) = -10 sin β < 0. So C is on the side of (-sin β, cos β) being negative, i.e., on the side of (sin β, -cos β).

So D on the same side as C: D = d(sin β, -cos β) with d > 0.

Let me check: D = (d sin β, -d cos β). This is in the fourth quadrant (positive x, negative y) for d > 0.

∠ABD: angle between BA = (cos β, sin β) and BD = (sin β, -cos β).
cos(∠ABD) = cos β · sin β + sin β · (-cos β) = 0. So ∠ABD = 90°. ✓

Now:
E = (0, e), e > 0
D = (d sin β, -d cos β), d > 0

AE² = (11cos β)² + (11sin β - e)² = 121 - 22e sin β + e²
CD² = (10 - d sin β)² + (d cos β)² = 100 - 20d sin β + d² sin²β + d² cos²β = 100 - 20d sin β + d²

AE = CD: 121 - 22e sin β + e² = 100 - 20d sin β + d²
→ 21 - 22e sin β + e² + 20d sin β - d² = 0 ... (I)

∠AEB = ∠DCB:

cos(∠AEB) = (EA · EB) / (|EA| |EB|)
EA = A - E = (11cos β, 11sin β - e), EB = B - E = (0, -e)
EA · EB = -e(11sin β - e) = e² - 11e sin β
|EB| = e (since e > 0)
cos(∠AEB) = (e² - 11e sin β) / (AE · e) = (e - 11 sin β) / AE

cos(∠DCB) = (CD · CB) / (|CD| |CB|)
CD = D - C = (d sin β - 10, -d cos β), CB = B - C = (-10, 0)
CD · CB = -10(d sin β - 10) = 100 - 10d sin β
|CB| = 10
cos(∠DCB) = (100 - 10d sin β) / (CD · 10) = (10 - d sin β) / CD = (10 - d sin β) / AE

Setting equal: (e - 11 sin β) / AE = (10 - d sin β) / AE
e - 11 sin β = 10 - d sin β
e + d sin β = 10 + 11 sin β ... (II)

ED = 20:
ED² = (0 - d sin β)² + (e - (-d cos β))² = d² sin²β + (e + d cos β)² = d² sin²β + e² + 2ed cos β + d² cos²β = d² + e² + 2ed cos β = 400 ... (III)

Now, let me also think about the angles at B.

With E at (0, e) (angle 90° from B) and D at (d sin β, -d cos β) (angle -β from B, or 360° - β):

Wait, D = (d sin β, -d cos β). The angle of D from B is arctan(-d cos β / (d sin β)) = arctan(-cos β / sin β) = arctan(-cot β) = -(90° - β) = β - 90°. Since β < 90°, this is negative, so D is at angle β - 90° (or 270° + β).

Rays from B:
- BC at angle 0
- BA at angle β
- BE at angle 90°
- BD at angle β - 90° (or 270° + β)

Counterclockwise order: BD (β - 90°, or equivalently 270° + β), BC (0°), BA (β), BE (90°).

Hmm, β - 90° is negative, so in [0, 360°) it's 270° + β. So counterclockwise: BC (0°), BA (β), BE (90°), BD (270° + β).

∠ABE = angle between BA (β) and BE (90°) = 90° - β.
∠DBC = angle between BD (270° + β) and BC (0°). Going counterclockwise from BD to BC: 360° - (270° + β) = 90° - β. Going clockwise: 270° + β. The smaller is 90° - β.

So ∠ABE = ∠DBC = 90° - β.

From the law of sines relation (*): 11 sin(∠ABE) = 10 sin(∠DBC)
11 sin(90° - β) = 10 sin(90° - β)
11 cos β = 10 cos β
11 = 10. Contradiction again!

Hmm. So this case also doesn't work. Let me try other configurations.

Case B: E above (e > 0), D on the opposite side from C.

D = d(-sin β, cos β) with d > 0 (this is the direction (-sin β, cos β), which is on the opposite side from C).

D = (-d sin β, d cos β), in the second quadrant.

∠ABD: angle between BA = (cos β, sin β) and BD = (-sin β, cos β).
cos(∠ABD) = -cos β sin β + sin β cos β = 0. ✓

CD² = (10 + d sin β)² + (d cos β)² = 100 + 20d sin β + d²

AE = CD: 121 - 22e sin β + e² = 100 + 20d sin β + d²
→ 21 - 22e sin β + e² - 20d sin β - d² = 0 ... (I')

cos(∠DCB) = (CD · CB) / (|CD| |CB|)
CD = D - C = (-d sin β - 10, d cos β), CB = (-10, 0)
CD · CB = 10(d sin β + 10) = 10d sin β + 100
cos(∠DCB) = (10d sin β + 100) / (10 · CD) = (d sin β + 10) / CD = (d sin β + 10) / AE

cos(∠AEB) = (e - 11 sin β) / AE (same as before, e > 0)

Setting equal: e - 11 sin β = d sin β + 10
e - d sin β = 10 + 11 sin β ... (II')

ED² = (0 + d sin β)² + (e - d cos β)² = d² sin²β + e² - 2ed cos β + d² cos²β = d² + e² - 2ed cos β = 400 ... (III')

Now the angles at B:
D = (-d sin β, d cos β) at angle 90° + β from B.
E = (0, e) at angle 90° from B.

Rays: BC (0°), BA (β), BE (90°), BD (90° + β).

Counterclockwise: BC (0°), BA (β), BE (90°), BD (90° + β).

∠ABE = 90° - β (angle between BA at β and BE at 90°).
∠DBC = angle between BD (90° + β) and BC (0°). Counterclockwise from BC to BD: 90° + β. Clockwise: 270° - β. Smaller is 90° + β.

So ∠ABE = 90° - β, ∠DBC = 90° + β.

From (*): 11 sin(90° - β) = 10 sin(90° + β)
11 cos β = 10 cos β
11 = 10. Contradiction again!

Hmm, all cases with e > 0 seem to give contradictions. Let me try e < 0.

Case C: E below (e < 0, so E = (0, e) with e < 0, |e| = -e), D on the opposite side from C: D = (-d sin β, d cos β), d > 0.

This is the case I originally considered. Let me redo the angles.

E = (0, e) with e < 0, so E is at angle 270° (or -90°) from B.
D = (-d sin β, d cos β) at angle 90° + β from B.

Rays: BC (0°), BA (β), BD (90° + β), BE (270°).

∠ABE = angle between BA (β) and BE (270°). Counterclockwise from BA to BE: 270° - β. Clockwise: 90° + β. Smaller is 90° + β (since β < 90°, 90° + β < 180° < 270° - β).

∠DBC = angle between BD (90° + β) and BC (0°). Counterclockwise from BC to BD: 90° + β. Clockwise: 270° - β. Smaller is 90° + β.

So ∠ABE = ∠DBC = 90° + β.

From (*): 11 sin(90° + β) = 10 sin(90° + β) → 11 = 10. Contradiction!

Case D: E below (e < 0), D on the same side as C: D = (d sin β, -d cos β), d > 0.

E at angle 270°, D at angle β - 90° (or 270° + β).

∠ABE = 90° + β (same as case C).
∠DBC = angle between BD (270° + β) and BC (0°). Counterclockwise from BC to BD: 270° + β. Clockwise: 90° - β. Smaller is 90° - β.

So ∠ABE = 90° + β, ∠DBC = 90° - β.

From (*): 11 sin(90° + β) = 10 sin(90° - β)
11 cos β = 10 cos β
11 = 10. Still contradiction!

Hmm, every case gives 11 = 10. That's because in every case, ∠ABE and ∠DBC are either both 90° + β or both 90° - β, or one is 90° + β and the other is 90° - β, but sin(90° + β) = cos β = sin(90° - β). So we always get 11 cos β = 10 cos β, hence 11 = 10.

This means the triangles AEB and DCB CANNOT be similar with the correspondence I assumed. Let me reconsider.

Wait, I think the issue is that the correspondence might not be A↔D, E↔C, B↔B. Let me reconsider which angles correspond.

We have ∠AEB = ∠DCB. In triangle AEB, this is the angle at E. In triangle DCB, this is the angle at C. So E ↔ C.

Now, the other angles: in triangle AEB, the angles are at A, E, B. In triangle DCB, the angles are at D, C, B. With E ↔ C, the remaining correspondences could be:
- A ↔ D, B ↔ B (which I've been trying, leading to contradiction)
- A ↔ B, B ↔ D

Let me try A ↔ B and B ↔ D, i.e., triangle AEB ~ BCD with A↔B, E↔C, B↔D.

Then: AE/BC = EB/CD = AB/BD
AE/10 = EB/CD = 11/BD

Since AE = CD: AE/10 = EB/AE, so AE² = 10·EB.
And AE/10 = 11/BD, so BD = 110/AE.

Also, ∠ABE (at B in triangle AEB) corresponds to ∠BDC (at D in triangle BCD).
∠EAB (at A in triangle AEB) corresponds to ∠DBC (at B in triangle BCD).

Let me set up the equations for this case.

Using the law of sines:
In triangle AEB: 11/sin(∠AEB) = AE/sin(∠ABE) = EB/sin(∠EAB)
In triangle DCB: 10/sin(∠DCB) = CD/sin(∠DBC) = DB/sin(∠BDC)

With ∠AEB = ∠DCB = θ, AE = CD:
11/sin θ = AE/sin(∠ABE) → AE = 11 sin(∠ABE)/sin θ
10/sin θ = AE/sin(∠DBC) → AE = 10 sin(∠DBC)/sin θ

So 11 sin(∠ABE) = 10 sin(∠DBC). Same as before (*). But now the correspondence is different: ∠ABE corresponds to ∠BDC, and ∠EAB corresponds to ∠DBC.

So the similarity gives ∠EAB = ∠DBC and ∠ABE = ∠BDC.

From the law of sines: 11 sin(∠ABE) = 10 sin(∠DBC), i.e., 11 sin(∠BDC) = 10 sin(∠EAB).

But from the similarity, ∠ABE = ∠BDC and ∠EAB = ∠DBC. So 11 sin(∠ABE) = 10 sin(∠ABE) (since ∠DBC = ∠EAB and ∠ABE = ∠BDC, we get 11 sin(∠BDC) = 10 sin(∠DBC), but ∠BDC = ∠ABE and ∠DBC = ∠EAB, and ∠ABE + ∠EAB = 180° - θ).

Hmm, this is getting circular. Let me think differently.

If the triangles are similar with A↔B, E↔C, B↔D, then:
AE/BC = EB/CD = AB/BD
AE/10 = EB/AE = 11/BD

From AE/10 = EB/AE: AE² = 10·EB.
From AE/10 = 11/BD: BD = 110/AE.

And the angles: ∠EAB = ∠DBC, ∠ABE = ∠BDC.

Now, ∠ABE + ∠DBC: these are angles at B in the two triangles. In the full configuration, ∠ABE and ∠DBC are related to the angles at B.

Let me reconsider the angular arrangement. Let me go back to Case C (e < 0, D = (-d sin β, d cos β)):

∠ABE = 90° + β, ∠DBC = 90° + β.

If ∠EAB = ∠DBC = 90° + β, then in triangle AEB: ∠EAB + ∠ABE + ∠AEB = 180°, so (90° + β) + (90° + β) + θ = 180°, giving θ = -2β < 0. Impossible.

Let me try Case D (e < 0, D = (d sin β, -d cos β)):
∠ABE = 90° + β, ∠DBC = 90° - β.

If ∠EAB = ∠DBC = 90° - β, then in triangle AEB: (90° - β) + (90° + β) + θ = 180°, so θ = 180° - 180° = 0. Degenerate.

If ∠ABE = ∠BDC and ∠EAB = ∠DBC:
∠ABE = 90° + β = ∠BDC, ∠EAB = 90° - β = ∠DBC.
In triangle AEB: (90° - β) + (90° + β) + θ = 180° → θ = 0. Degenerate.

Hmm. Let me try Case B (e > 0, D = (-d sin β, d cos β)):
∠ABE = 90° - β, ∠DBC = 90° + β.

If ∠EAB = ∠DBC = 90° + β, then in triangle AEB: (90° + β) + (90° - β) + θ = 180° → θ = 0. Degenerate.

If ∠ABE = ∠BDC = 90° - β, ∠EAB = ∠DBC = 90° + β:
In triangle AEB: (90° + β) + (90° - β) + θ = 180° → θ = 0. Degenerate.

Case A (e > 0, D = (d sin β, -d cos β)):
∠ABE = 90° - β, ∠DBC = 90° - β.

If ∠EAB = ∠DBC = 90° - β, then: (90° - β) + (90° - β) + θ = 180° → θ = 2β. This is positive! 

So in Case A, with the correspondence A↔B, E↔C, B↔D, we get θ = 2β.

Let me also check ∠ABE = ∠BDC: ∠ABE = 90° - β, ∠BDC = 180° - ∠DCB - ∠DBC = 180° - 2β - (90° - β) = 90° - β. ✓

So in Case A, the triangles are similar with A↔B, E↔C, B↔D, and ∠AEB = ∠DCB = 2β.

Now let me set up the equations for Case A.

E = (0, e), e > 0
D = (d sin β, -d cos β), d > 0

From the similarity: AE/BC = EB/CD = AB/BD
AE/10 = EB/AE = 11/BD (since AE = CD)

So AE² = 10·EB = 10e (since EB = e, as E = (0, e) and B = (0, 0)).
And BD = 110/AE, so d = 110/AE (since BD = d).

Also, AE² = 121 - 22e sin β + e² (computed earlier).
And AE² = 10e.
So 121 - 22e sin β + e² = 10e → e² - (10 + 22 sin β)e + 121 = 0 ... (A1)

d = 110/AE = 110/√(10e).

Now, ∠AEB = 2β. Let me verify using the cosine formula.
cos(∠AEB) = (e - 11 sin β)/AE (from earlier, with e > 0).
cos(2β) = 1 - 2sin²β = 2cos²β - 1.

So (e - 11 sin β)/AE = cos(2β) = 1 - 2sin²β.

Also, AE² = 10e, so AE = √(10e).
(e - 11 sin β)/√(10e) = 1 - 2sin²β ... (A2)

ED = 20:
ED² = d² + e² + 2ed cos β = 400 (from (III) in Case A).

Wait, let me recompute. In Case A:
E = (0, e), D = (d sin β, -d cos β).
ED² = (d sin β)² + (e + d cos β)² = d² sin²β + e² + 2ed cos β + d² cos²β = d² + e² + 2ed cos β = 400 ... (A3)

Now I have unknowns e, d, β with equations (A1), (A2), (A3), plus d = 110/√(10e).

Let me also use the angle condition more carefully. Actually, let me use the law of sines instead.

In triangle AEB: AB/sin(∠AEB) = 11/sin(2β) = AE/sin(∠ABE) = AE/sin(90° - β) = AE/cos β.
So AE = 11 cos β / sin(2β) = 11 cos β / (2 sin β cos β) = 11/(2 sin β).

Also AE² = 10e, so e = AE²/10 = 121/(40 sin²β).

And EB = e = 121/(40 sin²β). But also from law of sines: EB/sin(∠EAB) = 11/sin(2β).
∠EAB = 90° - β (from the similarity).
EB = 11 sin(90° - β)/sin(2β) = 11 cos β/(2 sin β cos β) = 11/(2 sin β).

So e = 11/(2 sin β). But also e = 121/(40 sin²β). So:
11/(2 sin β) = 121/(40 sin²β)
11 × 40 sin²β = 121 × 2 sin β
440 sin²β = 242 sin β
Since sin β ≠ 0: 440 sin β = 242 → sin β = 242/440 = 121/220.

So sin β = 121/220.

Then cos β = √(1 - (121/220)²) = √(1 - 14641/48400) = √(33759/48400) = √33759/220.

Let me factor 33759. 33759/3 = 11253. 11253/3 = 3751. 3751/11 = 341. 341 = 11 × 31. So 33759 = 3² × 11² × 31 = 9 × 121 × 31 = 33759. √33759 = 3 × 11 × √31 = 33√31.

So cos β = 33√31/220.

Now, AE = 11/(2 sin β) = 11/(2 × 121/220) = 11 × 220/(2 × 121) = 11 × 220/242 = 2420/242 = 10.

So AE = 10, and CD = AE = 10.

e = 11/(2 sin β) = 11 × 220/(2 × 121) = 2420/242 = 10. So e = 10.

d = 110/AE = 110/10 = 11. So d = 11.

Let me verify (A1): e² - (10 + 22 sin β)e + 121 = 100 - (10 + 22 × 121/220) × 10 + 121 = 100 - (10 + 242/220) × 10 + 121 = 100 - (10 + 11/10) × 10 + 121 = 100 - 110 - 11 + 121 = 100. 

Hmm, that gives 100, not 0. Let me recheck.

Wait, (A1) was: e² - (10 + 22 sin β)e + 121 = 0.
100 - (10 + 22 × 121/220) × 10 + 121
= 100 - (10 + 1342/220) × 10 + 121

22 × 121/220 = 2662/220 = 1331/110 = 121/10 = 12.1

So: 100 - (10 + 12.1) × 10 + 121 = 100 - 22.1 × 10 + 121 = 100 - 221 + 121 = 0. ✓

Great! I made an arithmetic error before. Let me recheck: 22 × 121/220 = 22 × 121 / 220 = 2662/220 = 12.1 = 121/10. So 10 + 121/10 = 221/10. (221/10) × 10 = 221. 100 - 221 + 121 = 0. ✓

Now check (A3): ED² = d² + e² + 2ed cos β = 121 + 100 + 2 × 11 × 10 × 33√31/220 = 221 + 220 × 33√31/220 = 221 + 33√31.

But ED = 20, so ED² = 400. So 221 + 33√31 = 400 → 33√31 = 179.

√31 ≈ 5.568. 33 × 5.568 ≈ 183.7. That's not 179. So this doesn't work!

Hmm. So the ED = 20 condition is not satisfied. Let me recheck.

Actually wait, I think I need to recheck whether the similarity actually holds, or if I need to consider the non-similar case.

Let me reconsider. The conditions are:
1. ∠AEB = ∠DCB
2. AE = CD
3. ED = 20
4. AP = 4

These don't necessarily imply the triangles are similar. The similarity was one possibility I derived from the angle arrangement, but maybe the triangles aren't similar and I need to solve the system directly.

Let me go back to the direct approach for Case A.

Case A: E = (0, e), e > 0; D = (d sin β, -d cos β), d > 0.

Equations:
(I): 21 - 22e sin β + e² + 20d sin β - d² = 0
(II): e + d sin β = 10 + 11 sin β
(III): d² + e² + 2ed cos β = 400

And AP = 4 where P is intersection of EA and CD.

Let me solve (I) and (II) first.

From (II): e = 10 + 11 sin β - d sin β = 10 + (11 - d) sin β.

Substitute into (I):
21 - 22(10 + (11-d) sin β) sin β + (10 + (11-d) sin β)² + 20d sin β - d² = 0

Let me expand:
21 - 220 sin β - 22(11-d) sin²β + 100 + 20(11-d) sin β + (11-d)² sin²β + 20d sin β - d² = 0

21 + 100 - 220 sin β + 20(11-d) sin β + 20d sin β - 22(11-d) sin²β + (11-d)² sin²β - d² = 0

121 + (-220 + 220 - 20d + 20d) sin β + (-22(11-d) + (11-d)²) sin²β - d² = 0

121 + 0 + (11-d)(-22 + 11 - d) sin²β - d² = 0

121 + (11-d)(-11 - d) sin²β - d² = 0

121 - (11-d)(11+d) sin²β - d² = 0

121 - (121 - d²) sin²β - d² = 0

121 - 121 sin²β + d² sin²β - d² = 0

121(1 - sin²β) + d²(sin²β - 1) = 0

121 cos²β - d² cos²β = 0

(121 - d²) cos²β = 0

Since β is acute, cos β ≠ 0, so d² = 121, d = 11 (since d > 0).

So d = 11! Then from (II): e = 10 + (11 - 11) sin β = 10.

So e = 10, d = 11, regardless of β!

Now from (III): 121 + 100 + 2 × 11 × 10 × cos β = 400
221 + 220 cos β = 400
cos β = 179/220

And sin β = √(1 - (179/220)²) = √(48400 - 32041)/220 = √16359/220.

Hmm, so we're back to the same values. And √16359 is not a nice number. But let me check if the AP = 4 condition gives us something.

Wait, but I showed earlier that with e = 10, d = 11, the angle condition ∠AEB = ∠DCB gives sin β = 0 (degenerate). Let me recheck.

With e = 10, d = 11:
cos(∠AEB) = (e - 11 sin β)/AE = (10 - 11 sin β)/AE
cos(∠DCB) = (10 - d sin β)/AE = (10 - 11 sin β)/AE

These are automatically equal! So ∠AEB = ∠DCB is automatically satisfied for any β. 

But wait, I need to check that the angles are actually equal, not just that their cosines are equal. Since both angles are in (0, π), equal cosines imply equal angles. So yes, the condition is satisfied.

But earlier when I tried e = 10 with the first case (Case C, where E was at (0, -10)), I got sin β = 0. That was a different case. In Case A, e = 10 works fine.

OK so now I need to check: is the pentagon ACEBD non-degenerate with this configuration?

A = (11 cos β, 11 sin β) = (11 × 179/220, 11 sin β) = (179/20, 11 sin β)
C = (10, 0)
E = (0, 10)
B = (0, 0)
D = (11 sin β, -11 cos β) = (11 sin β, -179/20)

Pentagon A, C, E, B, D:
A = (179/20, 11 sin β) ≈ (8.95, positive)
C = (10, 0)
E = (0, 10)
B = (0, 0)
D = (11 sin β, -179/20) ≈ (positive, -8.95)

Going A → C → E → B → D → A. Let me check if this is a simple polygon.

A is in the first quadrant, C is on the positive x-axis, E is on the positive y-axis, B is at origin, D is in the fourth quadrant.

A → C: from first quadrant to (10, 0). 
C → E: from (10, 0) to (0, 10). This is a line going up-left.
E → B: from (0, 10) to (0, 0). Going straight down.
B → D: from (0, 0) to fourth quadrant.
D → A: from fourth quadrant to first quadrant.

Does D → A cross any other edge? D is at (11 sin β, -179/20) and A is at (179/20, 11 sin β). The segment DA goes from fourth quadrant to first quadrant, passing through... let me check if it crosses CE.

CE goes from (10, 0) to (0, 10), which is the line x + y = 10.
DA goes from (11 sin β, -179/20) to (179/20, 11 sin β).

Let me parametrize DA: (1-t)(11 sin β, -179/20) + t(179/20, 11 sin β) for t ∈ [0,1].
x = (1-t)(11 sin β) + t(179/20)
y = (1-t)(-179/20) + t(11 sin β)

On the line x + y = 10:
(1-t)(11 sin β) + t(179/20) + (1-t)(-179/20) + t(11 sin β) = 10
(1-t)(11 sin β - 179/20) + t(179/20 + 11 sin β) = 10
Let u = 11 sin β, v = 179/20.
(1-t)(u - v) + t(u + v) = 10
u - v + t(u + v - u + v) = 10
u - v + 2tv = 10
t = (10 - u + v)/(2v) = (10 - 11 sin β + 179/20)/(2 × 179/20) = (10 + 179/20 - 11 sin β)/(179/10)

10 + 179/20 = 200/20 + 179/20 = 379/20.
t = (379/20 - 11 sin β)/(179/10) = (379/20 - 11 sin β) × 10/179 = (379 - 220 sin β)/(20 × 179/10) 

Hmm, let me just compute numerically. sin β = √16359/220. √16359 ≈ 127.9. So sin β ≈ 127.9/220 ≈ 0.5814.

11 sin β ≈ 6.395.
t = (379/20 - 6.395)/(179/10) = (18.95 - 6.395)/17.9 = 12.555/17.9 ≈ 0.701.

This is between 0 and 1, so the line DA does cross the line CE. But does it cross the segment CE?

On CE, the parametric form is (10 - s, s) for s ∈ [0, 10] (from C(10,0) to E(0,10)). At the crossing point:
x = (1-0.701)(6.395) + 0.701(8.95) = 0.299 × 6.395 + 0.701 × 8.95 ≈ 1.912 + 6.274 = 8.186
y = 0.299 × (-8.95) + 0.701 × 6.395 ≈ -2.676 + 4.483 = 1.807

On CE: x + y = 8.186 + 1.807 = 9.993 ≈ 10. ✓ (rounding errors)
And x = 8.186, y = 1.807, both positive and x ∈ [0, 10], y ∈ [0, 10]. So yes, the segment DA crosses the segment CE.

This means the pentagon ACEBD is self-intersecting, which might make it degenerate. But the problem says "non-degenerate pentagon." Hmm.

Actually, "non-degenerate" might just mean that no three consecutive vertices are collinear and no two consecutive vertices coincide, not that the polygon is simple. Or it might mean the polygon is simple. Let me not worry about this for now and proceed with the computation.

Actually, wait. Let me reconsider. Maybe the pentagon being non-degenerate just means it's a valid pentagon (5 distinct vertices, no three consecutive collinear). A self-intersecting pentagon is still a pentagon (a star pentagon, for instance). Let me proceed.

So we have:
A = (179/20, 11s) where s = sin β = √16359/220
C = (10, 0)
E = (0, 10)
B = (0, 0)
D = (11s, -179/20)

Now, P is the intersection of lines EA and CD, with AP = 4.

Line EA: from E(0, 10) to A(179/20, 11s).
Direction: (179/20, 11s - 10).
Parametrize: P = E + t(A - E) = (179t/20, 10 + t(11s - 10)).
When t = 0, P = E; when t = 1, P = A.

AP = |1 - t| × AE.
AE² = (179/20)² + (11s - 10)² = 32041/400 + 121s² - 220s + 100.

121s² = 121 × 16359/48400 = 16359/400.

AE² = 32041/400 + 16359/400 + 100 - 220s = 48400/400 + 100 - 220s = 121 + 100 - 220s = 221 - 220s.

So AE = √(221 - 220s).

AP = |1 - t| × √(221 - 220s) = 4.

Line CD: from C(10, 0) to D(11s, -179/20).
Direction: (11s - 10, -179/20).
Parametrize: P = C + u(D - C) = (10 + u(11s - 10), -179u/20).
When u = 0, P = C; when u = 1, P = D.

CP = |u| × CD = |u| × AE (since CD = AE).
CP² = u² × AE² = u² × (221 - 220s).

Setting the parametrizations equal:
179t/20 = 10 + u(11s - 10) ... (1)
10 + t(11s - 10) = -179u/20 ... (2)

Let me denote a = 11s - 10 and b = 179/20.

(1): bt = 10 + ua → bt - ua = 10
(2): 10 + ta = -ub → ta + ub = -10

From (1): bt - ua = 10
From (2): at + bu = -10

This is a linear system in t and u:
b·t - a·u = 10
a·t + b·u = -10

Determinant: b² + a² = AE² = 221 - 220s.

t = (10b + 10a) / (a² + b²) = 10(a + b) / (a² + b²) = 10(a + b) / (221 - 220s)

Wait, let me use Cramer's rule properly.

System:
bt - au = 10
at + bu = -10

In matrix form:
[b  -a] [t] = [10]
[a   b] [u]   [-10]

det = b² + a²

t = |10  -a; -10  b| / det = (10b - (-a)(-10)) / det = (10b - 10a) / det = 10(b - a) / (a² + b²)

u = |b  10; a  -10| / det = (b(-10) - 10a) / det = (-10b - 10a) / det = -10(a + b) / (a² + b²)

So:
t = 10(b - a) / (a² + b²) = 10(b - a) / (221 - 220s)
u = -10(a + b) / (a² + b²) = -10(a + b) / (221 - 220s)

Now, a = 11s - 10, b = 179/20.

a + b = 11s - 10 + 179/20 = 11s + (179/20 - 200/20) = 11s - 21/20.
b - a = 179/20 - 11s + 10 = 179/20 + 200/20 - 11s = 379/20 - 11s.

t = 10(379/20 - 11s) / (221 - 220s) = (379/2 - 110s) / (221 - 220s)

u = -10(11s - 21/20) / (221 - 220s) = (-110s + 21/2) / (221 - 220s) = (21/2 - 110s) / (221 - 220s)

AP = |1 - t| × AE = 4.

1 - t = 1 - (379/2 - 110s)/(221 - 220s) = (221 - 220s - 379/2 + 110s) / (221 - 220s) = (221 - 379/2 - 110s) / (221 - 220s) = (442/2 - 379/2 - 110s) / (221 - 220s) = (63/2 - 110s) / (221 - 220s)

AP = |63/2 - 110s| / √(221 - 220s) = 4

Since s = √16359/220 ≈ 0.5814, 110s ≈ 63.95. So 63/2 - 110s ≈ 31.5 - 63.95 = -32.45. So |63/2 - 110s| = 110s - 63/2.

(110s - 63/2) / √(221 - 220s) = 4

110s - 63/2 = 4√(221 - 220s)

Let me square both sides:
(110s - 63/2)² = 16(221 - 220s)

12100s² - 2 × 110s × 63/2 + (63/2)² = 3536 - 3520s

12100s² - 6930s + 3969/4 = 3536 - 3520s

12100s² - 6930s + 3969/4 - 3536 + 3520s = 0

12100s² - 3410s + 3969/4 - 14144/4 = 0

12100s² - 3410s - 10175/4 = 0

Multiply by 4:
48400s² - 13640s - 10175 = 0

Now, we also know 48400s² = 16359 (from cos β = 179/220):

16359 - 13640s - 10175 = 0
13640s = 16359 - 10175 = 6184
s = 6184/13640

Let me simplify: gcd(6184, 13640).
6184 = 2³ × 773
13640 = 2³ × 1705
gcd = 8

s = 773/1705

Let me check: 773/1705. Can this be simplified further? 773 is prime (checked earlier). 1705 = 5 × 341 = 5 × 11 × 31. 773 is not divisible by 5, 11, or 31 (773/11 = 70.27, 773/31 = 24.94). So s = 773/1705.

But we also need s² = 16359/48400. Let me check: (773/1705)² = 597529/2907025. And 16359/48400.

597529/2907025 vs 16359/48400. Cross multiply: 597529 × 48400 vs 16359 × 2907025.

597529 × 48400 = 597529 × 48400. Let me compute: 597529 × 48000 = 28,721,392,000; 597529 × 400 = 239,011,600. Total = 28,960,403,600.

16359 × 2907025 = 16359 × 2907025. 16359 × 2900000 = 47,441,100,000; 16359 × 7025 = 16359 × 7000 + 16359 × 25 = 114,513,000 + 408,975 = 114,921,975. Total = 47,556,021,975.

28,960,403,600 ≠ 47,556,021,975. So s = 773/1705 is NOT consistent with s² = 16359/48400!

This means the system is over-determined and inconsistent. Let me recheck.

Oh, I see the issue. The ED = 20 condition gives cos β = 179/220, which determines s² = 16359/48400. The AP = 4 condition gives 48400s² - 13640s - 10175 = 0, which determines s = 773/1705 (taking the positive root). These two are inconsistent, meaning there's no solution with this configuration!

Wait, but the problem says such a configuration exists. Let me recheck my work.

Hmm, let me recheck the AP = 4 equation. Let me recompute 1 - t.

t = 10(b - a) / (a² + b²) where a = 11s - 10, b = 179/20.

b - a = 179/20 - 11s + 10 = 179/20 + 10 - 11s = (179 + 200)/20 - 11s = 379/20 - 11s.

t = 10(379/20 - 11s) / (221 - 220s) = (379/2 - 110s) / (221 - 220s).

1 - t = (221 - 220s - 379/2 + 110s) / (221 - 220s) = (221 - 379/2 - 110s) / (221 - 220s).

221 - 379/2 = 442/2 - 379/2 = 63/2.

1 - t = (63/2 - 110s) / (221 - 220s).

AP = |1-t| × AE = |63/2 - 110s| / √(221 - 220s) = 4.

With s ≈ 0.5814: 63/2 - 110(0.5814) = 31.5 - 63.95 = -32.45.
221 - 220(0.5814) = 221 - 127.9 = 93.1.
AP = 32.45 / √93.1 = 32.45 / 9.65 ≈ 3.36.

But we need AP = 4. So with cos β = 179/220, AP ≈ 3.36, not 4. So indeed the ED = 20 and AP = 4 conditions are not simultaneously satisfiable in this configuration.

This means I have the wrong configuration. Let me reconsider.

Maybe I need to reconsider which case we're in. Let me go back and consider the case where the triangles are NOT similar, or a different geometric arrangement.

Actually, let me reconsider the problem. Maybe I've been too hasty in determining the angular arrangement. Let me think about what "ACEBD is a non-degenerate pentagon" means more carefully.

The pentagon ACEBD has vertices A, C, E, B, D in order. The sides are AC, CE, EB, BD, DA. The diagonals are AE, CB, BD... wait, no. Let me list the sides: AC, CE, EB, BD, DA. The diagonals are AE, CB, CD, AB, ED... hmm, actually the diagonals of pentagon ACEBD are: AE, CB, and CD (connecting non-adjacent vertices).

Wait, in pentagon ACEBD:
- Vertices: A(1), C(2), E(3), B(4), D(5)
- Sides: AC, CE, EB, BD, DA
- Diagonals: AE (1-3), CB (2-4), CD (2-5)... no. Diagonals connect non-adjacent vertices. 
  - A(1) is adjacent to C(2) and D(5). Non-adjacent to E(3) and B(4). Diagonals: AE, AB.
  - C(2) is adjacent to A(1) and E(3). Non-adjacent to B(4) and D(5). Diagonals: CB, CD.
  - E(3) is adjacent to C(2) and B(4). Non-adjacent to A(1) and D(5). Diagonals: EA, ED.
  - B(4) is adjacent to E(3) and D(5). Non-adjacent to A(1) and C(2). Diagonals: BA, BC.
  - D(5) is adjacent to B(4) and A(1). Non-adjacent to C(2) and E(3). Diagonals: DC, DE.

So the diagonals are: AE, AB, CB, CD, ED, ED (some repeated). The 5 diagonals are: AE, AB, CB, CD, DE. Wait, that's only 5 for a pentagon (which has 5 diagonals). Let me recount: AE, AB, CB, CD, DE. Yes, 5 diagonals.

Now, ∠CBE = 90°: this is the angle at B between BC (a diagonal) and BE (a side). 
∠ABD = 90°: this is the angle at B between BA (a diagonal) and BD (a side).

EA and CD are both diagonals, and they intersect at P.

So the problem is about a pentagon where two specific diagonals from B (BA and BC) are perpendicular to the two sides at B (BD and BE respectively).

Let me reconsider the geometry. In the pentagon ACEBD, at vertex B, the two sides are EB and BD. The angle ∠EBD is the interior angle at B. The diagonals from B are BA and BC.

∠CBE = 90°: diagonal BC ⊥ side BE.
∠ABD = 90°: diagonal BA ⊥ side BD.

So at vertex B, we have four rays: BE (side), BD (side), BC (diagonal), BA (diagonal). BC ⊥ BE and BA ⊥ BD.

The interior angle at B is ∠EBD. The angle ∠ABC = β is the angle between the two diagonals from B.

Now, the four rays BE, BC, BA, BD emanate from B. We know BC ⊥ BE and BA ⊥ BD. The angle between BC and BA is β (the angle of the original triangle at B).

The arrangement: if we go around B, the order of rays could be BE, BC, BA, BD or BE, BA, BC, BD, etc.

If the order is BE, BC, BA, BD (say counterclockwise):
- ∠EBC = 90° (given)
- ∠CBA = β
- ∠ABD = 90° (given)
- ∠DBE = 360° - 90° - β - 90° = 180° - β (the interior angle at B)

This seems reasonable. The interior angle at B is 180° - β, which is > 90° since β < 90° (acute triangle).

Alternatively, if the order is BE, BA, BC, BD:
- ∠EBA = some angle
- ∠ABC = β
- ∠CBD = some angle
- ∠DBE = some angle
With ∠EBC = ∠EBA + ∠ABC = 90° and ∠ABD = ∠ABC + ∠CBD = 90°.
So ∠EBA = 90° - β and ∠CBD = 90° - β.
∠DBE = 360° - (90° - β) - β - (90° - β) = 360° - 90° + β - β - 90° + β = 180° + β.
Interior angle at B would be 180° + β > 180°, which makes the pentagon non-convex at B. This is possible for a non-degenerate pentagon.

Hmm, there are multiple possible arrangements. Let me think about which one is consistent with the pentagon being non-degenerate and the other conditions.

Let me try the first arrangement: counterclockwise order BE, BC, BA, BD.

Place B at origin. Let BC be along the positive x-axis: C = (10, 0).
BE is 90° counterclockwise from BC, so BE is along the positive y-axis: E = (0, e) with e > 0.
BA is at angle β counterclockwise from BC: A = (11 cos β, 11 sin β) with β acute.
BD is 90° counterclockwise from BA: D = d(-sin β, cos β) with d > 0.

This is exactly Case B from before! And in Case B, I found that the angle condition and AE = CD lead to d = 11, e = 10 (from the algebraic manipulation), and then ED = 20 gives cos β = 179/220, but AP = 4 is inconsistent.

Wait, actually, let me redo Case B more carefully. In Case B:

E = (0, e), e > 0
D = (-d sin β, d cos β), d > 0

AE² = 121 - 22e sin β + e²
CD² = 100 + 20d sin β + d²

AE = CD: 121 - 22e sin β + e² = 100 + 20d sin β + d² → 21 - 22e sin β + e² - 20d sin β - d² = 0 ... (I')

cos(∠AEB) = (e - 11 sin β)/AE (e > 0)
cos(∠DCB) = (d sin β + 10)/AE

∠AEB = ∠DCB: e - 11 sin β = d sin β + 10 → e - d sin β = 10 + 11 sin β ... (II')

ED² = d² + e² - 2ed cos β = 400 ... (III')

From (II'): e = 10 + 11 sin β + d sin β = 10 + (11 + d) sin β.

Sub into (I'):
21 - 22(10 + (11+d) sin β) sin β + (10 + (11+d) sin β)² - 20d sin β - d² = 0

Let me expand:
21 - 220 sin β - 22(11+d) sin²β + 100 + 20(11+d) sin β + (11+d)² sin²β - 20d sin β - d² = 0

121 + (-220 + 220 + 20d - 20d) sin β + (-22(11+d) + (11+d)²) sin²β - d² = 0

121 + (11+d)(-22 + 11 + d) sin²β - d² = 0

121 + (11+d)(d - 11) sin²β - d² = 0

121 + (d² - 121) sin²β - d² = 0

121 - 121 sin²β + d² sin²β - d² = 0

121 cos²β - d² cos²β = 0

(121 - d²) cos²β = 0

d = 11 (since cos β ≠ 0).

Then e = 10 + (11 + 11) sin β = 10 + 22 sin β.

ED² = 121 + (10 + 22 sin β)² - 2 × 11 × (10 + 22 sin β) cos β = 400.

Let me expand:
121 + 100 + 440 sin β + 484 sin²β - 22(10 + 22 sin β) cos β = 400

221 + 440 sin β + 484 sin²β - 220 cos β - 484 sin β cos β = 400

440 sin β + 484 sin²β - 220 cos β - 484 sin β cos β = 179

Hmm, this is more complex because e depends on β. Let me use sin²β + cos²β = 1.

484 sin²β = 484(1 - cos²β) = 484 - 484 cos²β.

440 sin β + 484 - 484 cos²β - 220 cos β - 484 sin β cos β = 179

440 sin β - 484 cos²β - 220 cos β - 484 sin β cos β = 179 - 484 = -305

440 sin β - 220 cos β - 484 cos β(sin β + cos β) = -305

This is getting messy. Let me try a substitution. Let me set s = sin β, c = cos β.

440s + 484s² - 220c - 484sc = 179

With s² + c² = 1:
440s + 484(1 - c²) - 220c - 484sc = 179
440s + 484 - 484c² - 220c - 484sc = 179
440s - 484c² - 220c - 484sc = -305
440s - 220c - 484c(s + c) = -305

Let me try s + c = t, then sc = (t² - 1)/2 and s² + c² = 1.
Also s - c = u, t² + u² = 2.

440s - 220c = 220(2s - c). Hmm, 2s - c isn't simply expressible in terms of t.

Let me try a different approach. Let me just compute AP and set it to 4, and see what we get.

With d = 11, e = 10 + 22s:

A = (11c, 11s)
E = (0, 10 + 22s)
C = (10, 0)
D = (-11s, 11c)

AE² = 221 - 220s + 484s² - 440s = 221 + 484s² - 660s... 

Wait, let me recompute AE².
AE² = (11c)² + (11s - (10 + 22s))² = 121c² + (-10 - 11s)² = 121c² + (10 + 11s)² = 121c² + 100 + 220s + 121s² = 121(c² + s²) + 100 + 220s = 121 + 100 + 220s = 221 + 220s.

Oh interesting, AE² = 221 + 220s. (Different from Case A where it was 221 - 220s.)

CD² = (10 + 11s)² + (11c)² = 100 + 220s + 121s² + 121c² = 100 + 220s + 121 = 221 + 220s. ✓ (AE = CD)

Now, line EA: from E(0, 10 + 22s) to A(11c, 11s).
Direction: (11c, 11s - 10 - 22s) = (11c, -10 - 11s).
Parametrize: P = E + t(A - E) = (11ct, 10 + 22s + t(-10 - 11s)) = (11ct, 10 + 22s - t(10 + 11s)).

Line CD: from C(10, 0) to D(-11s, 11c).
Direction: (-11s - 10, 11c).
Parametrize: P = C + u(D - C) = (10 + u(-11s - 10), 11cu) = (10 - u(10 + 11s), 11cu).

Setting equal:
11ct = 10 - u(10 + 11s) ... (1)
10 + 22s - t(10 + 11s) = 11cu ... (2)

Let me denote p = 11c, q = 10 + 11s.

(1): pt = 10 - qu → pt + qu = 10
(2): 10 + 22s - qt = pu → -qt - pu = -(10 + 22s) → qt + pu = 10 + 22s

System:
pt + qu = 10
qt + pu = 10 + 22s... 

wait, let me redo (2): 10 + 22s - qt = pu → -qt - pu = -(10 + 22s) → qt + pu = 10 + 22s. Hmm, that doesn't look right.

(2): 10 + 22s - t(10 + 11s) = 11cu
10 + 22s - qt = pu
-qt - pu = -(10 + 22s)
qt + pu = 10 + 22s

Wait, that's wrong. Let me redo:
10 + 22s - qt = pu
→ -qt - pu = -(10 + 22s)
→ qt + pu = 10 + 22s

Hmm, but the sign: 10 + 22s - qt = pu means pu + qt = 10 + 22s. Yes.

System:
pt + qu = 10 ... (1)
pu + qt = 10 + 22s ... (2)

Wait, (2) should be: pu + qt = 10 + 22s. But let me double check: from (2), 10 + 22s - qt = pu, so pu = 10 + 22s - qt, so pu + qt = 10 + 22s. Yes.

        — AI历史解题过程（thinking）
#   polymath_05233         — 题目ID

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
  <problem_id>polymath_05233</problem_id>
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

In acute \(\triangle ABC\), \(AB = 11\) and \(CB = 10\). Points \(E\) and \(D\) are constructed such that \(\angle CBE\) and \(\angle ABD\) are right angles, and \(ACEBD\) is a non-degenerate pentagon. Additionally, \(\angle AEB \cong \angle DCB\), \(AE = CD\), and \(ED = 20\). Given that \(EA\) and \(CD\) intersect at \(P\) and \(AP = 4\), find \(CP^2\).

## Standard Solution

First, note that because \(\angle AEB \cong \angle DCB\), \(AE = DC\), and \(m \angle CBD = 90^\circ + m \angle ABC = m \angle EBA\), we have \(\triangle AEB \cong \triangle DCB\). Thus, \(DB = AB = 11\) and \(EB = CB = 10\). Notice that \(\angle EBA\) and \(\angle CBA\) are supplementary. 

Applying the law of cosines on \(\triangle EBD\):

\[
20^2 = 10^2 + 11^2 - 2 \cdot 11 \cdot 10 \cdot \cos(\angle EBD)
\]

Applying the law of cosines on \(\triangle ABC\):

\[
\begin{gathered}
AC^2 = 10^2 + 11^2 - 2 \cdot 11 \cdot 10 \cdot \cos(180^\circ - \angle EBD) \\
AC^2 = 10^2 + 11^2 + 2 \cdot 11 \cdot 10 \cdot \cos(\angle EBD)
\end{gathered}
\]

Then we have:

\[
\begin{gathered}
AC^2 + 20^2 = 2(10^2 + 11^2) \\
AC^2 = 42
\end{gathered}
\]

Also, notice that \(\triangle AEB\) is a \(90^\circ\) rotation of \(\triangle DCB\), so \(\overline{DC}\) and \(\overline{AE}\) must be perpendicular. Thus, \(\triangle APC\) is a right triangle, so we have:

\[
\begin{gathered}
42 = 4^2 + CP^2 \\
CP^2 = 26
\end{gathered}
\]

\(\boxed{26}\)

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have acute triangle ABC with AB = 11, CB = 10. Points E and D are constructed such that ∠CBE and ∠ABD are right angles, and ACEBD is a non-degenerate pentagon. Also ∠AEB ≅ ∠DCB, AE = CD, and ED = 20. EA and CD intersect at P with AP = 4. Find CP².

Let me set up coordinates. Let me place B at the origin.

Since ∠CBE is a right angle, E is on a line through B perpendicular to BC.
Since ∠ABD is a right angle, D is on a line through B perpendicular to BA.

Let me place B at origin. Let me put the triangle in a coordinate system.

Let me think about the configuration. ACEBD is a pentagon, so the order of vertices is A, C, E, B, D. This means going around the pentagon: A → C → E → B → D → A.

So the pentagon has vertices A, C, E, B, D in that order. The sides are AC, CE, EB, BD, DA.

∠CBE is a right angle - this is the angle at B in the pentagon (between sides EB and BC... wait, but BC isn't a side of the pentagon). Actually ∠CBE is the angle at vertex B formed by rays BC and BE. In the pentagon ACEBD, at vertex B the sides are EB and BD. So ∠CBE is between BC (a diagonal) and BE (a side). Hmm, let me reconsider.

Actually, let me reconsider. ∠CBE = 90° means the angle at B between BC and BE is 90°. ∠ABD = 90° means the angle at B between BA and BD is 90°.

So E is on the line through B perpendicular to BC, and D is on the line through B perpendicular to BA.

Let me set up coordinates. Place B at origin. Let BC be along some direction and BA along another.

Let me say the angle at B in triangle ABC is β. So ∠ABC = β.

Place B at origin, C at (10, 0) (since BC = 10). Then A is at distance 11 from B, making angle β with BC. So A = (11cos β, 11sin β).

Since triangle is acute, β is between 0 and π.

E is on the line through B perpendicular to BC. BC is along the x-axis, so E is on the y-axis: E = (0, e) for some e (could be positive or negative).

D is on the line through B perpendicular to BA. BA direction is (cos β, sin β), so perpendicular direction is (-sin β, cos β). So D = d·(-sin β, cos β) for some d.

Now, ACEBD is a non-degenerate pentagon with vertices in order A, C, E, B, D. For this to be a valid (non-self-intersecting) pentagon, we need to think about the positions.

Let me think about the order. Going A → C → E → B → D → A. 

A = (11cos β, 11sin β), C = (10, 0), E = (0, e), B = (0,0), D = d(-sin β, cos β).

For the pentagon to be non-degenerate and the vertices to be in this order (say counterclockwise), let me think about where E and D should be.

If β is acute (triangle is acute, so β < 90°), then A is in the first quadrant (positive x, positive y).

For the pentagon A, C, E, B, D to go counterclockwise:
- A is at angle β from x-axis (in first quadrant)
- C is at (10, 0) on positive x-axis
- E is on y-axis
- B is at origin
- D is at angle (β + 90°) from x-axis

Hmm, for the pentagon to make sense, E should be above B (positive y) so that going from C to E to B makes sense. And D should be positioned so that going from B to D to A makes sense.

Let me think counterclockwise. If we go counterclockwise:
- Start at A (upper left-ish, angle β)
- Go to C (on positive x-axis, angle 0) - this is clockwise from A, so maybe the pentagon is clockwise?

Let me think again. The order A, C, E, B, D. 

A is at angle β (first quadrant), C is at angle 0 (positive x-axis), E is at angle 90° (if e > 0, positive y-axis), B is at origin, D is at angle β + 90°.

Going A → C: from angle β to angle 0, that's clockwise.
Going C → E: from angle 0 to angle 90°, that's counterclockwise.

This doesn't form a simple polygon easily. Let me reconsider.

Maybe E is below the x-axis (e < 0), so E is at angle -90° or 270°.

Going A (angle β) → C (angle 0) → E (angle 270° or -90°) → B (origin) → D (angle β+90°) → A.

Hmm, this is getting complicated. Let me just set up the equations and not worry too much about the geometric configuration for now.

Conditions:
1. ∠AEB ≅ ∠DCB
2. AE = CD
3. ED = 20
4. AP = 4 where P is intersection of EA and CD.

Let me compute.

A = (11cos β, 11sin β)
C = (10, 0)
E = (0, e)
D = (-d sin β, d cos β)

AE = CD:
AE² = (11cos β - 0)² + (11sin β - e)² = 121cos²β + (11sin β - e)² = 121 - 22e sin β + e²
CD² = (10 + d sin β)² + (0 - d cos β)² = 100 + 20d sin β + d² sin²β + d² cos²β = 100 + 20d sin β + d²

So AE = CD gives: 121 - 22e sin β + e² = 100 + 20d sin β + d²
→ 21 - 22e sin β + e² - 20d sin β - d² = 0 ... (i)

∠AEB ≅ ∠DCB:

∠AEB is the angle at E in triangle AEB. 
∠DCB is the angle at C in triangle DCB.

Let me compute these angles using vectors or the cosine.

At E: vectors EA = A - E = (11cos β, 11sin β - e) and EB = B - E = (0, -e).
cos(∠AEB) = (EA · EB) / (|EA| |EB|) = (11cos β · 0 + (11sin β - e)(-e)) / (AE · |e|)
= (-11e sin β + e²) / (AE · |e|)
= (e² - 11e sin β) / (AE · |e|)
= e(e - 11 sin β) / (AE · |e|)

If e > 0, |e| = e, so cos(∠AEB) = (e - 11 sin β) / AE
If e < 0, |e| = -e, so cos(∠AEB) = (e - 11 sin β) / (AE · (-1)) = (11 sin β - e) / AE

Let me keep it general: cos(∠AEB) = (e² - 11e sin β) / (AE · |e|)

At C: vectors CD = D - C = (-d sin β - 10, d cos β) and CB = B - C = (-10, 0).
cos(∠DCB) = (CD · CB) / (|CD| |CB|) = ((-d sin β - 10)(-10) + d cos β · 0) / (CD · 10)
= (10d sin β + 100) / (10 · CD)
= (d sin β + 10) / CD

So ∠AEB ≅ ∠DCB means:
(e² - 11e sin β) / (AE · |e|) = (d sin β + 10) / CD

Since AE = CD, this simplifies to:
(e² - 11e sin β) / |e| = d sin β + 10

If e > 0: (e - 11 sin β) = d sin β + 10 → e - d sin β = 10 + 11 sin β ... (ii)
If e < 0: (11 sin β - e) = d sin β + 10 → -e - d sin β = 10 - 11 sin β → e + d sin β = 11 sin β - 10 ... (ii')

ED = 20:
ED² = (0 - (-d sin β))² + (e - d cos β)² = d² sin²β + e² - 2ed cos β + d² cos²β = d² + e² - 2ed cos β = 400 ... (iii)

Now, P is the intersection of lines EA and CD, with AP = 4.

Line EA: from E(0, e) to A(11cos β, 11sin β). Parametrize: P = E + t(A - E) = (11t cos β, e + t(11sin β - e)) for parameter t. When t=0, P=E; when t=1, P=A.

AP = 4 means |P - A| = 4. P - A = (1-t)(A - E) = (1-t)(11cos β, 11sin β - e). So |P - A| = |1-t| · AE = 4.
So |1 - t| = 4/AE, meaning t = 1 - 4/AE or t = 1 + 4/AE.

Line CD: from C(10, 0) to D(-d sin β, d cos β). Parametrize: P = C + s(D - C) = (10 + s(-d sin β - 10), s · d cos β) for parameter s. When s=0, P=C; when s=1, P=D.

CP = |P - C| = |s| · CD. So CP² = s² · CD² = s² · AE² (since AE = CD).

We need to find CP² = s² · AE².

At intersection, the two parametrizations are equal:
11t cos β = 10 + s(-d sin β - 10) = 10 - s(10 + d sin β) ... (iv)
e + t(11sin β - e) = s · d cos β ... (v)

This is getting complex. Let me try to think about this differently.

Actually, let me reconsider the problem. The conditions ∠AEB ≅ ∠DCB and AE = CD suggest some kind of congruence or similarity between triangles AEB and DCB.

In triangle AEB: sides AE, EB, AB = 11.
In triangle DCB: sides DC, CB = 10, DB.

We have AE = CD and ∠AEB = ∠DCB. 

If triangles AEB and DCB were similar with AE corresponding to DC and ∠AEB corresponding to ∠DCB, then the similarity would be:
A ↔ D, E ↔ C, B ↔ B (or some other correspondence).

Let me check: if the correspondence is A↔D, E↔C, B↔B:
- AE ↔ DC ✓ (given AE = CD)
- ∠AEB ↔ ∠DCB ✓ (given)
- EB ↔ CB = 10
- AB = 11 ↔ DB

So if triangles AEB ~ DCB with this correspondence, then:
AE/DC = EB/CB = AB/DB
Since AE = CD, AE/DC = 1, so EB = CB = 10 and AB = DB = 11.

So EB = 10 and DB = 11. That means e = ±10 (since E = (0, e) and EB = |e| = 10) and d = 11 (since DB = d = 11).

Wait, but this would make the triangles congruent, not just similar. Let me check: AE = CD (given), EB = CB = 10, AB = DB = 11. By SSS, triangles AEB ≅ DCB. And ∠AEB = ∠DCB is consistent.

But wait, is this necessarily the case? The conditions only give us AE = CD and ∠AEB = ∠DCB. This is SSA (side-side-angle), which doesn't uniquely determine congruence. There could be two configurations.

But let me explore the congruent case first: EB = 10, DB = 11, i.e., e = ±10, d = 11.

Case 1: e = 10, d = 11.

From (ii): e - d sin β = 10 + 11 sin β
10 - 11 sin β = 10 + 11 sin β
-11 sin β = 11 sin β
sin β = 0. 

That's degenerate. So e = 10 doesn't work with this.

Case 2: e = -10, d = 11.

From (ii'): e + d sin β = 11 sin β - 10
-10 + 11 sin β = 11 sin β - 10
-10 = -10 ✓

So e = -10, d = 11 works for any β! Let me check with (i):
21 - 22e sin β + e² - 20d sin β - d² = 0
21 - 22(-10) sin β + 100 - 20(11) sin β - 121 = 0
21 + 220 sin β + 100 - 220 sin β - 121 = 0
21 + 100 - 121 = 0
0 = 0 ✓

Great, so e = -10, d = 11 satisfies (i) and (ii') for any β.

Now check (iii): ED² = d² + e² - 2ed cos β = 121 + 100 - 2(11)(-10) cos β = 221 + 220 cos β = 400
220 cos β = 179
cos β = 179/220

Let me verify: sin²β + cos²β = 1. sin²β = 1 - (179/220)² = 1 - 32041/48400 = (48400 - 32041)/48400 = 16359/48400.

Hmm, let me check if 16359 is a perfect square. √16359 ≈ 127.9. 128² = 16384. So 16359 is not a perfect square. Let me double-check: 127² = 16129, 128² = 16384. 16359 is between them, not a perfect square.

Hmm, but the problem should have a nice answer. Let me reconsider.

Wait, maybe the triangles aren't congruent. Let me reconsider the SSA case.

Actually, let me reconsider. The conditions are AE = CD and ∠AEB = ∠DCB. In triangle AEB, we know AB = 11. In triangle DCB, we know CB = 10. 

With AE = CD and ∠AEB = ∠DCB, this is like SSA. Let me use the law of sines.

In triangle AEB: AE/sin(∠ABE) = AB/sin(∠AEB) = EB/sin(∠EAB)
In triangle DCB: DC/sin(∠DBC) = CB/sin(∠DCB) = DB/sin(∠DCB... wait, ∠DCB is at C.

Let me be more careful.

In triangle AEB:
- ∠AEB at E (given equal to ∠DCB)
- ∠ABE at B
- ∠EAB at A
- AB = 11, AE, EB

In triangle DCB:
- ∠DCB at C (given equal to ∠AEB)
- ∠DBC at B
- ∠BDC at D
- CB = 10, CD, DB

By law of sines in triangle AEB: AE/sin(∠ABE) = 11/sin(∠AEB)
By law of sines in triangle DCB: CD/sin(∠DBC) = 10/sin(∠DCB)

Since AE = CD and ∠AEB = ∠DCB:
sin(∠ABE) = (AE/11) sin(∠AEB) ... from first
sin(∠DBC) = (CD/10) sin(∠DCB) = (AE/10) sin(∠AEB) ... from second

So sin(∠ABE)/sin(∠DBC) = (AE/11)/(AE/10) = 10/11.

Now, ∠ABE + ∠DBC = ∠ABD - ∠EBD... wait, no. Let me think about the angles at B.

∠ABD = 90° (given). ∠CBE = 90° (given).

The angles at B: ∠ABE, ∠EBC (or ∠CBE), ∠CBD (or ∠DBC), ∠DBA (or ∠ABD).

We know ∠CBE = 90° and ∠ABD = 90°.

The full angle around B is 360°. The angles are ∠ABE, ∠EBC = 90°, ∠CBD, ∠DBA = 90°.
So ∠ABE + 90° + ∠CBD + 90° = 360° (if these four angles partition the full angle).
→ ∠ABE + ∠CBD = 180°.

Wait, that's only if the four rays BA, BE, BC, BD are arranged so that the four angles partition 360°. Let me think about this more carefully.

Actually, the four rays from B are BA, BC, BE, BD. We know ∠CBE = 90° (angle between BC and BE) and ∠ABD = 90° (angle between BA and BD).

The angle ∠ABC = β (angle of the triangle at B).

Let me think about the arrangement. In the pentagon ACEBD, the order is A, C, E, B, D. So going around B, the neighbors in the pentagon are E and D (since ...E, B, D... in the sequence). 

Let me think about the angular arrangement of the four rays from B. 

If we go counterclockwise around B, we might have: BA, BE, BC, BD or some other order.

∠CBE = 90°: the angle from BC to BE is 90°.
∠ABD = 90°: the angle from BA to BD is 90°.
∠ABC = β: the angle from BA to BC is β.

Let me consider the counterclockwise order. If the order is BA, BE, BC, BD (counterclockwise):
- ∠ABE (from BA to BE counterclockwise) = some angle α
- ∠EBC (from BE to BC counterclockwise) = 90° (since ∠CBE = 90°, and this is the same angle)
- ∠CBD (from BC to BD counterclockwise) = some angle γ
- ∠DBA (from BD to BA counterclockwise) = 90° (since ∠ABD = 90°)

Total: α + 90° + γ + 90° = 360° → α + γ = 180°.

Also, ∠ABC = β. From BA counterclockwise to BC: α + 90° = β. So α = β - 90°.

Since the triangle is acute, β < 90°, so α = β - 90° < 0. That's impossible.

Let me try the order BA, BD, BC, BE (counterclockwise):
- ∠ABD = 90° (from BA to BD) ✓
- ∠DBC (from BD to BC) = some angle γ
- ∠CBE = 90° (from BC to BE) ✓
- ∠EBA (from BE to BA) = some angle α

Total: 90° + γ + 90° + α = 360° → α + γ = 180°.

∠ABC = β: from BA to BC counterclockwise = 90° + γ = β. So γ = β - 90°. Again negative since β < 90°.

Hmm. Let me try clockwise orders or different arrangements.

Maybe the order counterclockwise is BA, BC, BE, BD:
- ∠ABC = β (from BA to BC) ✓
- ∠CBE = 90° (from BC to BE) ✓
- ∠EBD (from BE to BD) = some angle
- ∠DBA = 90° (from BD to BA) ✓ (since ∠ABD = 90°)

Total: β + 90° + ∠EBD + 90° = 360° → ∠EBD = 180° - β.

In this case:
∠ABE = ∠ABC + ∠CBE = β + 90° (the angle from BA to BE going counterclockwise through C)
∠DBC = ∠DBA - ... wait, ∠DBC is the angle from BD to BC. Going from BD counterclockwise to BC would be through BA: ∠DBA + ∠ABC = 90° + β. But that's the reflex angle. The direct angle from BD to BC (going clockwise, i.e., the smaller angle) would be 360° - (90° + β) = 270° - β. Hmm, that's more than 180°.

Actually, I need to be more careful. ∠DBC is the angle at B in triangle DBC, which is the angle between rays BD and BC. The angle between two rays is always taken to be ≤ 180°.

With the counterclockwise order BA, BC, BE, BD:
- Angle from BA to BC (counterclockwise) = β
- Angle from BC to BE (counterclockwise) = 90°
- Angle from BE to BD (counterclockwise) = 180° - β
- Angle from BD to BA (counterclockwise) = 90°

The angle between BD and BC: going counterclockwise from BC to BD is 90° + (180° - β) = 270° - β. Going clockwise from BC to BD is β + 90°. The smaller angle is min(270° - β, 90° + β). Since β is acute (0 < β < 90°), 90° + β < 180° and 270° - β > 180°. So the angle between BD and BC is 90° + β.

So ∠DBC = 90° + β. But this is more than 90°, and in triangle DBC, we'd have an obtuse angle at B. That's fine.

And ∠ABE: angle between BA and BE. Going counterclockwise from BA to BE is β + 90°. Going clockwise is 360° - (β + 90°) = 270° - β. The smaller is β + 90° (since β < 90°, β + 90° < 180°). So ∠ABE = β + 90°.

But wait, in triangle ABE, ∠ABE = 90° + β. That's an obtuse angle. And ∠AEB is given. Then ∠EAB = 180° - (90° + β) - ∠AEB = 90° - β - ∠AEB. For this to be positive, ∠AEB < 90° - β.

In triangle DCB, ∠DBC = 90° + β (obtuse), ∠DCB = ∠AEB, ∠BDC = 180° - (90° + β) - ∠AEB = 90° - β - ∠AEB.

So triangles AEB and DCB have:
- ∠AEB = ∠DCB (given)
- ∠ABE = 90° + β = ∠DBC
- ∠EAB = 90° - β - ∠AEB = ∠BDC

So the triangles are similar! AEB ~ DCB with correspondence A↔D, E↔C, B↔B.

And the ratio: AB/DB = AE/DC = EB/CB.
Since AE = CD (given), AE/DC = 1, so the triangles are congruent!
AB = DB = 11, EB = CB = 10.

So indeed EB = 10, DB = 11, and the triangles are congruent.

Now, with the counterclockwise order BA, BC, BE, BD, and E on the positive y side... let me reconsider coordinates.

Wait, I had e = -10 earlier. Let me reconcile.

With B at origin, C at (10, 0), A at (11cos β, 11sin β) with β acute (so A in first quadrant).

The counterclockwise order of rays from B is: BA (at angle β), BC (at angle 0), BE (at angle 90° from BC, so at angle 90°), BD (at angle 90° from BA, so at angle β + 90°).

Wait, I need to check: counterclockwise order BA, BC, BE, BD means:
- BA at angle β
- BC at angle 0

But going counterclockwise from BA (angle β) to BC (angle 0)... that's going clockwise (decreasing angle). So the counterclockwise order would be BC (angle 0), BA (angle β), ... 

Hmm, let me reconsider. Counterclockwise means increasing angle. So:
- BC at angle 0
- BA at angle β (since 0 < β < 90°)
- BD at angle β + 90° (90° counterclockwise from BA)
- BE at angle 90° (90° counterclockwise from BC)

So counterclockwise order: BC (0°), BA (β), BE (90°), BD (β+90°).

Wait, is β < 90°? Yes. And β + 90° vs 90°: β + 90° > 90°. So the order is: BC (0°), BA (β), BE (90°), BD (β + 90°).

Hmm, but the pentagon order is A, C, E, B, D. Let me check if this is consistent with a simple polygon.

The vertices in order:
A = (11cos β, 11sin β) - first quadrant
C = (10, 0) - on positive x-axis
E = (0, 10) - on positive y-axis (since e = 10 now, as EB = 10 and E is at angle 90°)
B = (0, 0) - origin
D = 11(-sin β, cos β) - at angle β + 90°, in second quadrant

Going A → C → E → B → D → A:
A (first quadrant) → C (positive x-axis) → E (positive y-axis) → B (origin) → D (second quadrant) → A (first quadrant)

This could form a simple polygon. Let me check: A is in the first quadrant, C is on the positive x-axis, E is on the positive y-axis, B is at origin, D is in the second quadrant. Going A → C → E → B → D → A, this seems like it could be a simple (non-self-intersecting) pentagon.

But wait, I had earlier derived that e = -10 works but e = 10 doesn't (with the equation from ∠AEB = ∠DCB). Let me recheck with this configuration.

With e = 10 (E at (0, 10)):
cos(∠AEB) = (e² - 11e sin β) / (AE · |e|) = (100 - 110 sin β) / (AE · 10) = (10 - 11 sin β) / AE

cos(∠DCB) = (d sin β + 10) / CD = (11 sin β + 10) / CD = (11 sin β + 10) / AE (since CD = AE)

Setting equal: (10 - 11 sin β) / AE = (11 sin β + 10) / AE
10 - 11 sin β = 11 sin β + 10
-11 sin β = 11 sin β
sin β = 0. Degenerate.

So e = 10 doesn't work. But e = -10 does. So E = (0, -10), which is on the negative y-axis, at angle 270° (or -90°).

Let me reconsider the angular arrangement with E at angle -90° (or 270°).

Rays from B:
- BC at angle 0
- BA at angle β (0 < β < 90°)
- BD at angle β + 90° (90° counterclockwise from BA)
- BE at angle -90° (or 270°)

Counterclockwise order: BC (0°), BA (β), BD (β + 90°), BE (270°).

The angle ∠CBE: from BC (0°) to BE (270°). Going counterclockwise: 270°. Going clockwise: 90°. The angle is 90°. ✓

The angle ∠ABD: from BA (β) to BD (β + 90°). Counterclockwise: 90°. ✓

Now the pentagon order A, C, E, B, D:
A (first quadrant) → C (positive x-axis) → E (negative y-axis) → B (origin) → D (second quadrant) → A

Let me check if this is a simple polygon. 
A is at (11cos β, 11sin β) with sin β > 0, cos β > 0.
C is at (10, 0).
E is at (0, -10).
B is at (0, 0).
D is at (-11 sin β, 11 cos β) with sin β > 0, cos β > 0, so D is in the second quadrant.

A → C: from first quadrant to positive x-axis. OK.
C → E: from (10, 0) to (0, -10). This goes down-left. OK.
E → B: from (0, -10) to (0, 0). This goes straight up. OK.
B → D: from (0, 0) to second quadrant. OK.
D → A: from second quadrant to first quadrant. This could cross other edges. Let me check.

D = (-11 sin β, 11 cos β), A = (11 cos β, 11 sin β).
The segment DA goes from second quadrant to first quadrant. It could cross the segment CE (from (10, 0) to (0, -10)) or other segments.

Actually, for the pentagon to be non-degenerate, it just needs to be a valid pentagon (not necessarily convex). Let me not worry about this and proceed with the computation.

So we have:
e = -10, d = 11
cos β = 179/220 (from ED = 20)

Wait, let me recompute. ED² = d² + e² - 2ed cos β = 121 + 100 - 2(11)(-10) cos β = 221 + 220 cos β = 400.
cos β = (400 - 221) / 220 = 179/220.

sin²β = 1 - (179/220)² = 1 - 32041/48400 = 16359/48400.

Let me factor 16359. 16359 / 3 = 5453. 5453 / 7 = 779. 779 / 19 = 41. So 16359 = 3 × 7 × 19 × 41. Not a perfect square.

Hmm, so sin β = √(16359/48400) = √16359 / 220. This is not clean.

But the problem asks for CP², which might still be a nice number even if intermediate values aren't.

Let me proceed with the computation.

We have:
A = (11cos β, 11sin β)
C = (10, 0)
E = (0, -10)
D = (-11 sin β, 11 cos β)

cos β = 179/220, sin β = √16359 / 220.

Let me denote s = sin β, c = cos β = 179/220.

A = (11c, 11s) = (11·179/220, 11s) = (179/20, 11s)
C = (10, 0)
E = (0, -10)
D = (-11s, 11c) = (-11s, 179/20)

Now, P is the intersection of lines EA and CD.

Line EA: from E(0, -10) to A(179/20, 11s).
Direction: (179/20, 11s + 10).
Parametrize: P = E + t(A - E) = (179t/20, -10 + t(11s + 10)).

Line CD: from C(10, 0) to D(-11s, 179/20).
Direction: (-11s - 10, 179/20).
Parametrize: P = C + u(D - C) = (10 + u(-11s - 10), u · 179/20) = (10 - u(11s + 10), 179u/20).

Setting equal:
179t/20 = 10 - u(11s + 10) ... (1)
-10 + t(11s + 10) = 179u/20 ... (2)

From (1): 179t/20 + u(11s + 10) = 10
From (2): t(11s + 10) - 179u/20 = 10

Let me denote a = 11s + 10 and b = 179/20.

From (1): bt + au = 10
From (2): at - bu = 10

Solving:
From (1): u = (10 - bt)/a
Sub into (2): at - b(10 - bt)/a = 10
a²t - b(10 - bt) = 10a
a²t - 10b + b²t = 10a
t(a² + b²) = 10a + 10b = 10(a + b)
t = 10(a + b) / (a² + b²)

Similarly, from (2): t = (10 + bu)/a, sub into (1):
b(10 + bu)/a + au = 10
b(10 + bu) + a²u = 10a
10b + b²u + a²u = 10a
u(a² + b²) = 10a - 10b = 10(a - b)
u = 10(a - b) / (a² + b²)

Now, AP = |P - A| = |1 - t| · |A - E| = |1 - t| · AE.

We need AE. AE² = (179/20)² + (11s + 10)² = b² + a².

So AE = √(a² + b²).

AP = |1 - t| · √(a² + b²) = |1 - 10(a+b)/(a²+b²)| · √(a²+b²)
= |(a²+b² - 10(a+b))/(a²+b²)| · √(a²+b²)
= |a²+b² - 10a - 10b| / √(a²+b²)

Let me compute a² + b² - 10a - 10b.

a = 11s + 10, b = 179/20.

a² = (11s + 10)² = 121s² + 220s + 100
b² = (179/20)² = 32041/400

a² + b² = 121s² + 220s + 100 + 32041/400

Now s² = 1 - c² = 1 - 32041/48400 = 16359/48400.
121s² = 121 × 16359/48400 = 16359/400 (since 48400 = 400 × 121).

So a² + b² = 16359/400 + 220s + 100 + 32041/400 = (16359 + 32041)/400 + 220s + 100 = 48400/400 + 220s + 100 = 121 + 220s + 100 = 221 + 220s.

10a + 10b = 10(11s + 10) + 10(179/20) = 110s + 100 + 179/2 = 110s + 100 + 89.5 = 110s + 189.5 = 110s + 379/2.

a² + b² - 10a - 10b = 221 + 220s - 110s - 379/2 = 221 + 110s - 379/2 = (442 - 379)/2 + 110s = 63/2 + 110s.

So AP = |63/2 + 110s| / √(221 + 220s).

Since s = sin β > 0 (β is acute), 63/2 + 110s > 0, so:

AP = (63/2 + 110s) / √(221 + 220s)

We're given AP = 4:

(63/2 + 110s) / √(221 + 220s) = 4

63/2 + 110s = 4√(221 + 220s)

Let me square both sides:
(63/2 + 110s)² = 16(221 + 220s)

(63/2)² + 2(63/2)(110s) + (110s)² = 3536 + 3520s

3969/4 + 6930s + 12100s² = 3536 + 3520s

12100s² + 6930s + 3969/4 = 3536 + 3520s

12100s² + (6930 - 3520)s + 3969/4 - 3536 = 0

12100s² + 3410s + (3969/4 - 14144/4) = 0

12100s² + 3410s - 10175/4 = 0

Multiply by 4:
48400s² + 13640s - 10175 = 0

Let me use the quadratic formula:
s = (-13640 ± √(13640² + 4 × 48400 × 10175)) / (2 × 48400)
= (-13640 ± √(186049600 + 19739200000)) / 96800

Wait, let me compute more carefully.

13640² = 13640 × 13640. 
13640 × 13640: 13640 × 13000 = 177,320,000; 13640 × 640 = 8,729,600. Total = 186,049,600.

4 × 48400 × 10175 = 4 × 48400 × 10175.
48400 × 10175 = 48400 × 10000 + 48400 × 175 = 484,000,000 + 8,470,000 = 492,470,000.
4 × 492,470,000 = 1,969,880,000.

Discriminant = 186,049,600 + 1,969,880,000 = 2,155,929,600.

√2,155,929,600 = ? Let me check. 46432² = ? 46000² = 2,116,000,000. 46400² = 2,152,960,000. 46432² = 46432 × 46432. 

46432² = (46400 + 32)² = 46400² + 2×46400×32 + 32² = 2,152,960,000 + 2,969,600 + 1,024 = 2,155,930,624.

That's close but not exactly 2,155,929,600. The difference is 2,155,930,624 - 2,155,929,600 = 1,024. So √2,155,929,600 ≠ 46432.

Let me try 46431² = 46432² - 2×46432 + 1 = 2,155,930,624 - 92,864 + 1 = 2,155,837,761. That's too small.

Hmm, so the discriminant is not a perfect square. Let me recheck my computation.

Actually, wait. Let me recheck. We also have the constraint that s² = 16359/48400, i.e., 48400s² = 16359. Let me use this.

From 48400s² + 13640s - 10175 = 0 and 48400s² = 16359:

16359 + 13640s - 10175 = 0
13640s = 10175 - 16359 = -6184
s = -6184/13640 = -6184/13640

Let me simplify: gcd(6184, 13640). 
6184 = 2 × 3092 = 4 × 1546 = 8 × 773
13640 = 8 × 1705 = 8 × 5 × 341 = 8 × 5 × 11 × 31
773 = ? 773/7 = 110.4, 773/11 = 70.3, 773/13 = 59.5, 773/17 = 45.5, 773/19 = 40.7, 773/23 = 33.6, 773 is prime? 773/773 = 1. √773 ≈ 27.8. Primes up to 27: 2,3,5,7,11,13,17,19,23. 773/3 = 257.7, 773/7 = 110.4, 773/11 = 70.3, 773/13 = 59.5, 773/17 = 45.5, 773/19 = 40.7, 773/23 = 33.6. So 773 is prime.

So s = -773/1705. But s = sin β > 0 (β is acute). This gives s < 0, which is a contradiction!

Hmm, so there's an inconsistency. Let me recheck.

Oh wait, I think the issue is that the AP = 4 condition, combined with the other constraints, might not be compatible with the congruent triangle case. Or maybe I made an error somewhere.

Let me recheck. Actually, wait. The issue might be that the triangles AEB and DCB are NOT congruent. The SSA condition can give two different triangles. Let me reconsider.

We have AE = CD and ∠AEB = ∠DCB. The SSA condition means there could be two cases. In one case the triangles are congruent (which I explored), and in another they're not.

Actually, let me reconsider. The SSA (side-side-angle) ambiguity: given two sides and a non-included angle, there can be 0, 1, or 2 triangles. But here we have two separate triangles, each with their own constraints.

In triangle AEB: we know AB = 11, AE (unknown), ∠AEB (unknown but equals ∠DCB).
In triangle DCB: we know CB = 10, CD = AE (unknown), ∠DCB = ∠AEB (unknown).

The constraint is AE = CD and ∠AEB = ∠DCB. These don't force congruence because the known sides (AB = 11, CB = 10) are different.

Let me redo this without assuming congruence.

Let me use the law of sines approach.

In triangle AEB: AB/sin(∠AEB) = AE/sin(∠ABE) = EB/sin(∠EAB)
In triangle DCB: CB/sin(∠DCB) = CD/sin(∠DBC) = DB/sin(∠BDC)

Since ∠AEB = ∠DCB = θ (say), and AE = CD:
From triangle AEB: 11/sin θ = AE/sin(∠ABE) → AE = 11 sin(∠ABE)/sin θ
From triangle DCB: 10/sin θ = CD/sin(∠DBC) → CD = 10 sin(∠DBC)/sin θ

Since AE = CD: 11 sin(∠ABE) = 10 sin(∠DBC) ... (*)

Now, what are ∠ABE and ∠DBC?

From the angular arrangement (counterclockwise: BC at 0°, BA at β, BE at -90° (or 270°), BD at β+90°):

∠ABE = angle between BA and BE. BA at angle β, BE at angle 270° (or -90°). 
The angle between them: |β - 270°| = 270° - β (going one way) or 360° - (270° - β) = 90° + β (going the other way). The smaller angle is 90° + β (since β < 90°, 90° + β < 180° < 270° - β).

So ∠ABE = 90° + β. (This is the angle in triangle ABE at vertex B.)

∠DBC = angle between BD and BC. BD at angle β + 90°, BC at angle 0°.
The angle: β + 90° (going counterclockwise from BC to BD) or 360° - (β + 90°) = 270° - β (going clockwise). The smaller is β + 90° (since β < 90°, β + 90° < 180°).

So ∠DBC = 90° + β.

So ∠ABE = ∠DBC = 90° + β!

Then from (*): 11 sin(90° + β) = 10 sin(90° + β).
Since sin(90° + β) = cos β ≠ 0 (β is acute), this gives 11 = 10, contradiction!

So this configuration is impossible. That means my angular arrangement is wrong, or the triangles aren't arranged as I thought.

Let me reconsider the angular arrangement. Maybe E is on the other side.

Let me reconsider. We have ∠CBE = 90° and ∠ABD = 90°. There are two possible positions for E (on either side of line BC) and two for D (on either side of line BA).

Let me consider different cases.

Case A: E is on the same side as A (above the x-axis, e > 0), D is on the same side as C.

With B at origin, C at (10, 0), A at (11cos β, 11sin β) (first quadrant, β acute).

E on the line through B perpendicular to BC (y-axis), on the same side as A: E = (0, e) with e > 0.
D on the line through B perpendicular to BA, on the same side as C: The perpendicular to BA is direction (-sin β, cos β) or (sin β, -cos β). "Same side as C" - C is at (10, 0). 

The line BA has direction (cos β, sin β). The perpendicular directions are (-sin β, cos β) and (sin β, -cos β). 

Which side is C on? The line BA passes through origin with direction (cos β, sin β). The normal to this line is (-sin β, cos β). C = (10, 0). The signed distance of C from line BA is C · (-sin β, cos β) = -10 sin β < 0. So C is on the side of (-sin β, cos β) being negative, i.e., on the side of (sin β, -cos β).

So D on the same side as C: D = d(sin β, -cos β) with d > 0.

Let me check: D = (d sin β, -d cos β). This is in the fourth quadrant (positive x, negative y) for d > 0.

∠ABD: angle between BA = (cos β, sin β) and BD = (sin β, -cos β).
cos(∠ABD) = cos β · sin β + sin β · (-cos β) = 0. So ∠ABD = 90°. ✓

Now:
E = (0, e), e > 0
D = (d sin β, -d cos β), d > 0

AE² = (11cos β)² + (11sin β - e)² = 121 - 22e sin β + e²
CD² = (10 - d sin β)² + (d cos β)² = 100 - 20d sin β + d² sin²β + d² cos²β = 100 - 20d sin β + d²

AE = CD: 121 - 22e sin β + e² = 100 - 20d sin β + d²
→ 21 - 22e sin β + e² + 20d sin β - d² = 0 ... (I)

∠AEB = ∠DCB:

cos(∠AEB) = (EA · EB) / (|EA| |EB|)
EA = A - E = (11cos β, 11sin β - e), EB = B - E = (0, -e)
EA · EB = -e(11sin β - e) = e² - 11e sin β
|EB| = e (since e > 0)
cos(∠AEB) = (e² - 11e sin β) / (AE · e) = (e - 11 sin β) / AE

cos(∠DCB) = (CD · CB) / (|CD| |CB|)
CD = D - C = (d sin β - 10, -d cos β), CB = B - C = (-10, 0)
CD · CB = -10(d sin β - 10) = 100 - 10d sin β
|CB| = 10
cos(∠DCB) = (100 - 10d sin β) / (CD · 10) = (10 - d sin β) / CD = (10 - d sin β) / AE

Setting equal: (e - 11 sin β) / AE = (10 - d sin β) / AE
e - 11 sin β = 10 - d sin β
e + d sin β = 10 + 11 sin β ... (II)

ED = 20:
ED² = (0 - d sin β)² + (e - (-d cos β))² = d² sin²β + (e + d cos β)² = d² sin²β + e² + 2ed cos β + d² cos²β = d² + e² + 2ed cos β = 400 ... (III)

Now, let me also think about the angles at B.

With E at (0, e) (angle 90° from B) and D at (d sin β, -d cos β) (angle -β from B, or 360° - β):

Wait, D = (d sin β, -d cos β). The angle of D from B is arctan(-d cos β / (d sin β)) = arctan(-cos β / sin β) = arctan(-cot β) = -(90° - β) = β - 90°. Since β < 90°, this is negative, so D is at angle β - 90° (or 270° + β).

Rays from B:
- BC at angle 0
- BA at angle β
- BE at angle 90°
- BD at angle β - 90° (or 270° + β)

Counterclockwise order: BD (β - 90°, or equivalently 270° + β), BC (0°), BA (β), BE (90°).

Hmm, β - 90° is negative, so in [0, 360°) it's 270° + β. So counterclockwise: BC (0°), BA (β), BE (90°), BD (270° + β).

∠ABE = angle between BA (β) and BE (90°) = 90° - β.
∠DBC = angle between BD (270° + β) and BC (0°). Going counterclockwise from BD to BC: 360° - (270° + β) = 90° - β. Going clockwise: 270° + β. The smaller is 90° - β.

So ∠ABE = ∠DBC = 90° - β.

From the law of sines relation (*): 11 sin(∠ABE) = 10 sin(∠DBC)
11 sin(90° - β) = 10 sin(90° - β)
11 cos β = 10 cos β
11 = 10. Contradiction again!

Hmm. So this case also doesn't work. Let me try other configurations.

Case B: E above (e > 0), D on the opposite side from C.

D = d(-sin β, cos β) with d > 0 (this is the direction (-sin β, cos β), which is on the opposite side from C).

D = (-d sin β, d cos β), in the second quadrant.

∠ABD: angle between BA = (cos β, sin β) and BD = (-sin β, cos β).
cos(∠ABD) = -cos β sin β + sin β cos β = 0. ✓

CD² = (10 + d sin β)² + (d cos β)² = 100 + 20d sin β + d²

AE = CD: 121 - 22e sin β + e² = 100 + 20d sin β + d²
→ 21 - 22e sin β + e² - 20d sin β - d² = 0 ... (I')

cos(∠DCB) = (CD · CB) / (|CD| |CB|)
CD = D - C = (-d sin β - 10, d cos β), CB = (-10, 0)
CD · CB = 10(d sin β + 10) = 10d sin β + 100
cos(∠DCB) = (10d sin β + 100) / (10 · CD) = (d sin β + 10) / CD = (d sin β + 10) / AE

cos(∠AEB) = (e - 11 sin β) / AE (same as before, e > 0)

Setting equal: e - 11 sin β = d sin β + 10
e - d sin β = 10 + 11 sin β ... (II')

ED² = (0 + d sin β)² + (e - d cos β)² = d² sin²β + e² - 2ed cos β + d² cos²β = d² + e² - 2ed cos β = 400 ... (III')

Now the angles at B:
D = (-d sin β, d cos β) at angle 90° + β from B.
E = (0, e) at angle 90° from B.

Rays: BC (0°), BA (β), BE (90°), BD (90° + β).

Counterclockwise: BC (0°), BA (β), BE (90°), BD (90° + β).

∠ABE = 90° - β (angle between BA at β and BE at 90°).
∠DBC = angle between BD (90° + β) and BC (0°). Counterclockwise from BC to BD: 90° + β. Clockwise: 270° - β. Smaller is 90° + β.

So ∠ABE = 90° - β, ∠DBC = 90° + β.

From (*): 11 sin(90° - β) = 10 sin(90° + β)
11 cos β = 10 cos β
11 = 10. Contradiction again!

Hmm, all cases with e > 0 seem to give contradictions. Let me try e < 0.

Case C: E below (e < 0, so E = (0, e) with e < 0, |e| = -e), D on the opposite side from C: D = (-d sin β, d cos β), d > 0.

This is the case I originally considered. Let me redo the angles.

E = (0, e) with e < 0, so E is at angle 270° (or -90°) from B.
D = (-d sin β, d cos β) at angle 90° + β from B.

Rays: BC (0°), BA (β), BD (90° + β), BE (270°).

∠ABE = angle between BA (β) and BE (270°). Counterclockwise from BA to BE: 270° - β. Clockwise: 90° + β. Smaller is 90° + β (since β < 90°, 90° + β < 180° < 270° - β).

∠DBC = angle between BD (90° + β) and BC (0°). Counterclockwise from BC to BD: 90° + β. Clockwise: 270° - β. Smaller is 90° + β.

So ∠ABE = ∠DBC = 90° + β.

From (*): 11 sin(90° + β) = 10 sin(90° + β) → 11 = 10. Contradiction!

Case D: E below (e < 0), D on the same side as C: D = (d sin β, -d cos β), d > 0.

E at angle 270°, D at angle β - 90° (or 270° + β).

∠ABE = 90° + β (same as case C).
∠DBC = angle between BD (270° + β) and BC (0°). Counterclockwise from BC to BD: 270° + β. Clockwise: 90° - β. Smaller is 90° - β.

So ∠ABE = 90° + β, ∠DBC = 90° - β.

From (*): 11 sin(90° + β) = 10 sin(90° - β)
11 cos β = 10 cos β
11 = 10. Still contradiction!

Hmm, every case gives 11 = 10. That's because in every case, ∠ABE and ∠DBC are either both 90° + β or both 90° - β, or one is 90° + β and the other is 90° - β, but sin(90° + β) = cos β = sin(90° - β). So we always get 11 cos β = 10 cos β, hence 11 = 10.

This means the triangles AEB and DCB CANNOT be similar with the correspondence I assumed. Let me reconsider.

Wait, I think the issue is that the correspondence might not be A↔D, E↔C, B↔B. Let me reconsider which angles correspond.

We have ∠AEB = ∠DCB. In triangle AEB, this is the angle at E. In triangle DCB, this is the angle at C. So E ↔ C.

Now, the other angles: in triangle AEB, the angles are at A, E, B. In triangle DCB, the angles are at D, C, B. With E ↔ C, the remaining correspondences could be:
- A ↔ D, B ↔ B (which I've been trying, leading to contradiction)
- A ↔ B, B ↔ D

Let me try A ↔ B and B ↔ D, i.e., triangle AEB ~ BCD with A↔B, E↔C, B↔D.

Then: AE/BC = EB/CD = AB/BD
AE/10 = EB/CD = 11/BD

Since AE = CD: AE/10 = EB/AE, so AE² = 10·EB.
And AE/10 = 11/BD, so BD = 110/AE.

Also, ∠ABE (at B in triangle AEB) corresponds to ∠BDC (at D in triangle BCD).
∠EAB (at A in triangle AEB) corresponds to ∠DBC (at B in triangle BCD).

Let me set up the equations for this case.

Using the law of sines:
In triangle AEB: 11/sin(∠AEB) = AE/sin(∠ABE) = EB/sin(∠EAB)
In triangle DCB: 10/sin(∠DCB) = CD/sin(∠DBC) = DB/sin(∠BDC)

With ∠AEB = ∠DCB = θ, AE = CD:
11/sin θ = AE/sin(∠ABE) → AE = 11 sin(∠ABE)/sin θ
10/sin θ = AE/sin(∠DBC) → AE = 10 sin(∠DBC)/sin θ

So 11 sin(∠ABE) = 10 sin(∠DBC). Same as before (*). But now the correspondence is different: ∠ABE corresponds to ∠BDC, and ∠EAB corresponds to ∠DBC.

So the similarity gives ∠EAB = ∠DBC and ∠ABE = ∠BDC.

From the law of sines: 11 sin(∠ABE) = 10 sin(∠DBC), i.e., 11 sin(∠BDC) = 10 sin(∠EAB).

But from the similarity, ∠ABE = ∠BDC and ∠EAB = ∠DBC. So 11 sin(∠ABE) = 10 sin(∠ABE) (since ∠DBC = ∠EAB and ∠ABE = ∠BDC, we get 11 sin(∠BDC) = 10 sin(∠DBC), but ∠BDC = ∠ABE and ∠DBC = ∠EAB, and ∠ABE + ∠EAB = 180° - θ).

Hmm, this is getting circular. Let me think differently.

If the triangles are similar with A↔B, E↔C, B↔D, then:
AE/BC = EB/CD = AB/BD
AE/10 = EB/AE = 11/BD

From AE/10 = EB/AE: AE² = 10·EB.
From AE/10 = 11/BD: BD = 110/AE.

And the angles: ∠EAB = ∠DBC, ∠ABE = ∠BDC.

Now, ∠ABE + ∠DBC: these are angles at B in the two triangles. In the full configuration, ∠ABE and ∠DBC are related to the angles at B.

Let me reconsider the angular arrangement. Let me go back to Case C (e < 0, D = (-d sin β, d cos β)):

∠ABE = 90° + β, ∠DBC = 90° + β.

If ∠EAB = ∠DBC = 90° + β, then in triangle AEB: ∠EAB + ∠ABE + ∠AEB = 180°, so (90° + β) + (90° + β) + θ = 180°, giving θ = -2β < 0. Impossible.

Let me try Case D (e < 0, D = (d sin β, -d cos β)):
∠ABE = 90° + β, ∠DBC = 90° - β.

If ∠EAB = ∠DBC = 90° - β, then in triangle AEB: (90° - β) + (90° + β) + θ = 180°, so θ = 180° - 180° = 0. Degenerate.

If ∠ABE = ∠BDC and ∠EAB = ∠DBC:
∠ABE = 90° + β = ∠BDC, ∠EAB = 90° - β = ∠DBC.
In triangle AEB: (90° - β) + (90° + β) + θ = 180° → θ = 0. Degenerate.

Hmm. Let me try Case B (e > 0, D = (-d sin β, d cos β)):
∠ABE = 90° - β, ∠DBC = 90° + β.

If ∠EAB = ∠DBC = 90° + β, then in triangle AEB: (90° + β) + (90° - β) + θ = 180° → θ = 0. Degenerate.

If ∠ABE = ∠BDC = 90° - β, ∠EAB = ∠DBC = 90° + β:
In triangle AEB: (90° + β) + (90° - β) + θ = 180° → θ = 0. Degenerate.

Case A (e > 0, D = (d sin β, -d cos β)):
∠ABE = 90° - β, ∠DBC = 90° - β.

If ∠EAB = ∠DBC = 90° - β, then: (90° - β) + (90° - β) + θ = 180° → θ = 2β. This is positive! 

So in Case A, with the correspondence A↔B, E↔C, B↔D, we get θ = 2β.

Let me also check ∠ABE = ∠BDC: ∠ABE = 90° - β, ∠BDC = 180° - ∠DCB - ∠DBC = 180° - 2β - (90° - β) = 90° - β. ✓

So in Case A, the triangles are similar with A↔B, E↔C, B↔D, and ∠AEB = ∠DCB = 2β.

Now let me set up the equations for Case A.

E = (0, e), e > 0
D = (d sin β, -d cos β), d > 0

From the similarity: AE/BC = EB/CD = AB/BD
AE/10 = EB/AE = 11/BD (since AE = CD)

So AE² = 10·EB = 10e (since EB = e, as E = (0, e) and B = (0, 0)).
And BD = 110/AE, so d = 110/AE (since BD = d).

Also, AE² = 121 - 22e sin β + e² (computed earlier).
And AE² = 10e.
So 121 - 22e sin β + e² = 10e → e² - (10 + 22 sin β)e + 121 = 0 ... (A1)

d = 110/AE = 110/√(10e).

Now, ∠AEB = 2β. Let me verify using the cosine formula.
cos(∠AEB) = (e - 11 sin β)/AE (from earlier, with e > 0).
cos(2β) = 1 - 2sin²β = 2cos²β - 1.

So (e - 11 sin β)/AE = cos(2β) = 1 - 2sin²β.

Also, AE² = 10e, so AE = √(10e).
(e - 11 sin β)/√(10e) = 1 - 2sin²β ... (A2)

ED = 20:
ED² = d² + e² + 2ed cos β = 400 (from (III) in Case A).

Wait, let me recompute. In Case A:
E = (0, e), D = (d sin β, -d cos β).
ED² = (d sin β)² + (e + d cos β)² = d² sin²β + e² + 2ed cos β + d² cos²β = d² + e² + 2ed cos β = 400 ... (A3)

Now I have unknowns e, d, β with equations (A1), (A2), (A3), plus d = 110/√(10e).

Let me also use the angle condition more carefully. Actually, let me use the law of sines instead.

In triangle AEB: AB/sin(∠AEB) = 11/sin(2β) = AE/sin(∠ABE) = AE/sin(90° - β) = AE/cos β.
So AE = 11 cos β / sin(2β) = 11 cos β / (2 sin β cos β) = 11/(2 sin β).

Also AE² = 10e, so e = AE²/10 = 121/(40 sin²β).

And EB = e = 121/(40 sin²β). But also from law of sines: EB/sin(∠EAB) = 11/sin(2β).
∠EAB = 90° - β (from the similarity).
EB = 11 sin(90° - β)/sin(2β) = 11 cos β/(2 sin β cos β) = 11/(2 sin β).

So e = 11/(2 sin β). But also e = 121/(40 sin²β). So:
11/(2 sin β) = 121/(40 sin²β)
11 × 40 sin²β = 121 × 2 sin β
440 sin²β = 242 sin β
Since sin β ≠ 0: 440 sin β = 242 → sin β = 242/440 = 121/220.

So sin β = 121/220.

Then cos β = √(1 - (121/220)²) = √(1 - 14641/48400) = √(33759/48400) = √33759/220.

Let me factor 33759. 33759/3 = 11253. 11253/3 = 3751. 3751/11 = 341. 341 = 11 × 31. So 33759 = 3² × 11² × 31 = 9 × 121 × 31 = 33759. √33759 = 3 × 11 × √31 = 33√31.

So cos β = 33√31/220.

Now, AE = 11/(2 sin β) = 11/(2 × 121/220) = 11 × 220/(2 × 121) = 11 × 220/242 = 2420/242 = 10.

So AE = 10, and CD = AE = 10.

e = 11/(2 sin β) = 11 × 220/(2 × 121) = 2420/242 = 10. So e = 10.

d = 110/AE = 110/10 = 11. So d = 11.

Let me verify (A1): e² - (10 + 22 sin β)e + 121 = 100 - (10 + 22 × 121/220) × 10 + 121 = 100 - (10 + 242/220) × 10 + 121 = 100 - (10 + 11/10) × 10 + 121 = 100 - 110 - 11 + 121 = 100. 

Hmm, that gives 100, not 0. Let me recheck.

Wait, (A1) was: e² - (10 + 22 sin β)e + 121 = 0.
100 - (10 + 22 × 121/220) × 10 + 121
= 100 - (10 + 1342/220) × 10 + 121

22 × 121/220 = 2662/220 = 1331/110 = 121/10 = 12.1

So: 100 - (10 + 12.1) × 10 + 121 = 100 - 22.1 × 10 + 121 = 100 - 221 + 121 = 0. ✓

Great! I made an arithmetic error before. Let me recheck: 22 × 121/220 = 22 × 121 / 220 = 2662/220 = 12.1 = 121/10. So 10 + 121/10 = 221/10. (221/10) × 10 = 221. 100 - 221 + 121 = 0. ✓

Now check (A3): ED² = d² + e² + 2ed cos β = 121 + 100 + 2 × 11 × 10 × 33√31/220 = 221 + 220 × 33√31/220 = 221 + 33√31.

But ED = 20, so ED² = 400. So 221 + 33√31 = 400 → 33√31 = 179.

√31 ≈ 5.568. 33 × 5.568 ≈ 183.7. That's not 179. So this doesn't work!

Hmm. So the ED = 20 condition is not satisfied. Let me recheck.

Actually wait, I think I need to recheck whether the similarity actually holds, or if I need to consider the non-similar case.

Let me reconsider. The conditions are:
1. ∠AEB = ∠DCB
2. AE = CD
3. ED = 20
4. AP = 4

These don't necessarily imply the triangles are similar. The similarity was one possibility I derived from the angle arrangement, but maybe the triangles aren't similar and I need to solve the system directly.

Let me go back to the direct approach for Case A.

Case A: E = (0, e), e > 0; D = (d sin β, -d cos β), d > 0.

Equations:
(I): 21 - 22e sin β + e² + 20d sin β - d² = 0
(II): e + d sin β = 10 + 11 sin β
(III): d² + e² + 2ed cos β = 400

And AP = 4 where P is intersection of EA and CD.

Let me solve (I) and (II) first.

From (II): e = 10 + 11 sin β - d sin β = 10 + (11 - d) sin β.

Substitute into (I):
21 - 22(10 + (11-d) sin β) sin β + (10 + (11-d) sin β)² + 20d sin β - d² = 0

Let me expand:
21 - 220 sin β - 22(11-d) sin²β + 100 + 20(11-d) sin β + (11-d)² sin²β + 20d sin β - d² = 0

21 + 100 - 220 sin β + 20(11-d) sin β + 20d sin β - 22(11-d) sin²β + (11-d)² sin²β - d² = 0

121 + (-220 + 220 - 20d + 20d) sin β + (-22(11-d) + (11-d)²) sin²β - d² = 0

121 + 0 + (11-d)(-22 + 11 - d) sin²β - d² = 0

121 + (11-d)(-11 - d) sin²β - d² = 0

121 - (11-d)(11+d) sin²β - d² = 0

121 - (121 - d²) sin²β - d² = 0

121 - 121 sin²β + d² sin²β - d² = 0

121(1 - sin²β) + d²(sin²β - 1) = 0

121 cos²β - d² cos²β = 0

(121 - d²) cos²β = 0

Since β is acute, cos β ≠ 0, so d² = 121, d = 11 (since d > 0).

So d = 11! Then from (II): e = 10 + (11 - 11) sin β = 10.

So e = 10, d = 11, regardless of β!

Now from (III): 121 + 100 + 2 × 11 × 10 × cos β = 400
221 + 220 cos β = 400
cos β = 179/220

And sin β = √(1 - (179/220)²) = √(48400 - 32041)/220 = √16359/220.

Hmm, so we're back to the same values. And √16359 is not a nice number. But let me check if the AP = 4 condition gives us something.

Wait, but I showed earlier that with e = 10, d = 11, the angle condition ∠AEB = ∠DCB gives sin β = 0 (degenerate). Let me recheck.

With e = 10, d = 11:
cos(∠AEB) = (e - 11 sin β)/AE = (10 - 11 sin β)/AE
cos(∠DCB) = (10 - d sin β)/AE = (10 - 11 sin β)/AE

These are automatically equal! So ∠AEB = ∠DCB is automatically satisfied for any β. 

But wait, I need to check that the angles are actually equal, not just that their cosines are equal. Since both angles are in (0, π), equal cosines imply equal angles. So yes, the condition is satisfied.

But earlier when I tried e = 10 with the first case (Case C, where E was at (0, -10)), I got sin β = 0. That was a different case. In Case A, e = 10 works fine.

OK so now I need to check: is the pentagon ACEBD non-degenerate with this configuration?

A = (11 cos β, 11 sin β) = (11 × 179/220, 11 sin β) = (179/20, 11 sin β)
C = (10, 0)
E = (0, 10)
B = (0, 0)
D = (11 sin β, -11 cos β) = (11 sin β, -179/20)

Pentagon A, C, E, B, D:
A = (179/20, 11 sin β) ≈ (8.95, positive)
C = (10, 0)
E = (0, 10)
B = (0, 0)
D = (11 sin β, -179/20) ≈ (positive, -8.95)

Going A → C → E → B → D → A. Let me check if this is a simple polygon.

A is in the first quadrant, C is on the positive x-axis, E is on the positive y-axis, B is at origin, D is in the fourth quadrant.

A → C: from first quadrant to (10, 0). 
C → E: from (10, 0) to (0, 10). This is a line going up-left.
E → B: from (0, 10) to (0, 0). Going straight down.
B → D: from (0, 0) to fourth quadrant.
D → A: from fourth quadrant to first quadrant.

Does D → A cross any other edge? D is at (11 sin β, -179/20) and A is at (179/20, 11 sin β). The segment DA goes from fourth quadrant to first quadrant, passing through... let me check if it crosses CE.

CE goes from (10, 0) to (0, 10), which is the line x + y = 10.
DA goes from (11 sin β, -179/20) to (179/20, 11 sin β).

Let me parametrize DA: (1-t)(11 sin β, -179/20) + t(179/20, 11 sin β) for t ∈ [0,1].
x = (1-t)(11 sin β) + t(179/20)
y = (1-t)(-179/20) + t(11 sin β)

On the line x + y = 10:
(1-t)(11 sin β) + t(179/20) + (1-t)(-179/20) + t(11 sin β) = 10
(1-t)(11 sin β - 179/20) + t(179/20 + 11 sin β) = 10
Let u = 11 sin β, v = 179/20.
(1-t)(u - v) + t(u + v) = 10
u - v + t(u + v - u + v) = 10
u - v + 2tv = 10
t = (10 - u + v)/(2v) = (10 - 11 sin β + 179/20)/(2 × 179/20) = (10 + 179/20 - 11 sin β)/(179/10)

10 + 179/20 = 200/20 + 179/20 = 379/20.
t = (379/20 - 11 sin β)/(179/10) = (379/20 - 11 sin β) × 10/179 = (379 - 220 sin β)/(20 × 179/10) 

Hmm, let me just compute numerically. sin β = √16359/220. √16359 ≈ 127.9. So sin β ≈ 127.9/220 ≈ 0.5814.

11 sin β ≈ 6.395.
t = (379/20 - 6.395)/(179/10) = (18.95 - 6.395)/17.9 = 12.555/17.9 ≈ 0.701.

This is between 0 and 1, so the line DA does cross the line CE. But does it cross the segment CE?

On CE, the parametric form is (10 - s, s) for s ∈ [0, 10] (from C(10,0) to E(0,10)). At the crossing point:
x = (1-0.701)(6.395) + 0.701(8.95) = 0.299 × 6.395 + 0.701 × 8.95 ≈ 1.912 + 6.274 = 8.186
y = 0.299 × (-8.95) + 0.701 × 6.395 ≈ -2.676 + 4.483 = 1.807

On CE: x + y = 8.186 + 1.807 = 9.993 ≈ 10. ✓ (rounding errors)
And x = 8.186, y = 1.807, both positive and x ∈ [0, 10], y ∈ [0, 10]. So yes, the segment DA crosses the segment CE.

This means the pentagon ACEBD is self-intersecting, which might make it degenerate. But the problem says "non-degenerate pentagon." Hmm.

Actually, "non-degenerate" might just mean that no three consecutive vertices are collinear and no two consecutive vertices coincide, not that the polygon is simple. Or it might mean the polygon is simple. Let me not worry about this for now and proceed with the computation.

Actually, wait. Let me reconsider. Maybe the pentagon being non-degenerate just means it's a valid pentagon (5 distinct vertices, no three consecutive collinear). A self-intersecting pentagon is still a pentagon (a star pentagon, for instance). Let me proceed.

So we have:
A = (179/20, 11s) where s = sin β = √16359/220
C = (10, 0)
E = (0, 10)
B = (0, 0)
D = (11s, -179/20)

Now, P is the intersection of lines EA and CD, with AP = 4.

Line EA: from E(0, 10) to A(179/20, 11s).
Direction: (179/20, 11s - 10).
Parametrize: P = E + t(A - E) = (179t/20, 10 + t(11s - 10)).
When t = 0, P = E; when t = 1, P = A.

AP = |1 - t| × AE.
AE² = (179/20)² + (11s - 10)² = 32041/400 + 121s² - 220s + 100.

121s² = 121 × 16359/48400 = 16359/400.

AE² = 32041/400 + 16359/400 + 100 - 220s = 48400/400 + 100 - 220s = 121 + 100 - 220s = 221 - 220s.

So AE = √(221 - 220s).

AP = |1 - t| × √(221 - 220s) = 4.

Line CD: from C(10, 0) to D(11s, -179/20).
Direction: (11s - 10, -179/20).
Parametrize: P = C + u(D - C) = (10 + u(11s - 10), -179u/20).
When u = 0, P = C; when u = 1, P = D.

CP = |u| × CD = |u| × AE (since CD = AE).
CP² = u² × AE² = u² × (221 - 220s).

Setting the parametrizations equal:
179t/20 = 10 + u(11s - 10) ... (1)
10 + t(11s - 10) = -179u/20 ... (2)

Let me denote a = 11s - 10 and b = 179/20.

(1): bt = 10 + ua → bt - ua = 10
(2): 10 + ta = -ub → ta + ub = -10

From (1): bt - ua = 10
From (2): at + bu = -10

This is a linear system in t and u:
b·t - a·u = 10
a·t + b·u = -10

Determinant: b² + a² = AE² = 221 - 220s.

t = (10b + 10a) / (a² + b²) = 10(a + b) / (a² + b²) = 10(a + b) / (221 - 220s)

Wait, let me use Cramer's rule properly.

System:
bt - au = 10
at + bu = -10

In matrix form:
[b  -a] [t] = [10]
[a   b] [u]   [-10]

det = b² + a²

t = |10  -a; -10  b| / det = (10b - (-a)(-10)) / det = (10b - 10a) / det = 10(b - a) / (a² + b²)

u = |b  10; a  -10| / det = (b(-10) - 10a) / det = (-10b - 10a) / det = -10(a + b) / (a² + b²)

So:
t = 10(b - a) / (a² + b²) = 10(b - a) / (221 - 220s)
u = -10(a + b) / (a² + b²) = -10(a + b) / (221 - 220s)

Now, a = 11s - 10, b = 179/20.

a + b = 11s - 10 + 179/20 = 11s + (179/20 - 200/20) = 11s - 21/20.
b - a = 179/20 - 11s + 10 = 179/20 + 200/20 - 11s = 379/20 - 11s.

t = 10(379/20 - 11s) / (221 - 220s) = (379/2 - 110s) / (221 - 220s)

u = -10(11s - 21/20) / (221 - 220s) = (-110s + 21/2) / (221 - 220s) = (21/2 - 110s) / (221 - 220s)

AP = |1 - t| × AE = 4.

1 - t = 1 - (379/2 - 110s)/(221 - 220s) = (221 - 220s - 379/2 + 110s) / (221 - 220s) = (221 - 379/2 - 110s) / (221 - 220s) = (442/2 - 379/2 - 110s) / (221 - 220s) = (63/2 - 110s) / (221 - 220s)

AP = |63/2 - 110s| / √(221 - 220s) = 4

Since s = √16359/220 ≈ 0.5814, 110s ≈ 63.95. So 63/2 - 110s ≈ 31.5 - 63.95 = -32.45. So |63/2 - 110s| = 110s - 63/2.

(110s - 63/2) / √(221 - 220s) = 4

110s - 63/2 = 4√(221 - 220s)

Let me square both sides:
(110s - 63/2)² = 16(221 - 220s)

12100s² - 2 × 110s × 63/2 + (63/2)² = 3536 - 3520s

12100s² - 6930s + 3969/4 = 3536 - 3520s

12100s² - 6930s + 3969/4 - 3536 + 3520s = 0

12100s² - 3410s + 3969/4 - 14144/4 = 0

12100s² - 3410s - 10175/4 = 0

Multiply by 4:
48400s² - 13640s - 10175 = 0

Now, we also know 48400s² = 16359 (from cos β = 179/220):

16359 - 13640s - 10175 = 0
13640s = 16359 - 10175 = 6184
s = 6184/13640

Let me simplify: gcd(6184, 13640).
6184 = 2³ × 773
13640 = 2³ × 1705
gcd = 8

s = 773/1705

Let me check: 773/1705. Can this be simplified further? 773 is prime (checked earlier). 1705 = 5 × 341 = 5 × 11 × 31. 773 is not divisible by 5, 11, or 31 (773/11 = 70.27, 773/31 = 24.94). So s = 773/1705.

But we also need s² = 16359/48400. Let me check: (773/1705)² = 597529/2907025. And 16359/48400.

597529/2907025 vs 16359/48400. Cross multiply: 597529 × 48400 vs 16359 × 2907025.

597529 × 48400 = 597529 × 48400. Let me compute: 597529 × 48000 = 28,721,392,000; 597529 × 400 = 239,011,600. Total = 28,960,403,600.

16359 × 2907025 = 16359 × 2907025. 16359 × 2900000 = 47,441,100,000; 16359 × 7025 = 16359 × 7000 + 16359 × 25 = 114,513,000 + 408,975 = 114,921,975. Total = 47,556,021,975.

28,960,403,600 ≠ 47,556,021,975. So s = 773/1705 is NOT consistent with s² = 16359/48400!

This means the system is over-determined and inconsistent. Let me recheck.

Oh, I see the issue. The ED = 20 condition gives cos β = 179/220, which determines s² = 16359/48400. The AP = 4 condition gives 48400s² - 13640s - 10175 = 0, which determines s = 773/1705 (taking the positive root). These two are inconsistent, meaning there's no solution with this configuration!

Wait, but the problem says such a configuration exists. Let me recheck my work.

Hmm, let me recheck the AP = 4 equation. Let me recompute 1 - t.

t = 10(b - a) / (a² + b²) where a = 11s - 10, b = 179/20.

b - a = 179/20 - 11s + 10 = 179/20 + 10 - 11s = (179 + 200)/20 - 11s = 379/20 - 11s.

t = 10(379/20 - 11s) / (221 - 220s) = (379/2 - 110s) / (221 - 220s).

1 - t = (221 - 220s - 379/2 + 110s) / (221 - 220s) = (221 - 379/2 - 110s) / (221 - 220s).

221 - 379/2 = 442/2 - 379/2 = 63/2.

1 - t = (63/2 - 110s) / (221 - 220s).

AP = |1-t| × AE = |63/2 - 110s| / √(221 - 220s) = 4.

With s ≈ 0.5814: 63/2 - 110(0.5814) = 31.5 - 63.95 = -32.45.
221 - 220(0.5814) = 221 - 127.9 = 93.1.
AP = 32.45 / √93.1 = 32.45 / 9.65 ≈ 3.36.

But we need AP = 4. So with cos β = 179/220, AP ≈ 3.36, not 4. So indeed the ED = 20 and AP = 4 conditions are not simultaneously satisfiable in this configuration.

This means I have the wrong configuration. Let me reconsider.

Maybe I need to reconsider which case we're in. Let me go back and consider the case where the triangles are NOT similar, or a different geometric arrangement.

Actually, let me reconsider the problem. Maybe I've been too hasty in determining the angular arrangement. Let me think about what "ACEBD is a non-degenerate pentagon" means more carefully.

The pentagon ACEBD has vertices A, C, E, B, D in order. The sides are AC, CE, EB, BD, DA. The diagonals are AE, CB, BD... wait, no. Let me list the sides: AC, CE, EB, BD, DA. The diagonals are AE, CB, CD, AB, ED... hmm, actually the diagonals of pentagon ACEBD are: AE, CB, and CD (connecting non-adjacent vertices).

Wait, in pentagon ACEBD:
- Vertices: A(1), C(2), E(3), B(4), D(5)
- Sides: AC, CE, EB, BD, DA
- Diagonals: AE (1-3), CB (2-4), CD (2-5)... no. Diagonals connect non-adjacent vertices. 
  - A(1) is adjacent to C(2) and D(5). Non-adjacent to E(3) and B(4). Diagonals: AE, AB.
  - C(2) is adjacent to A(1) and E(3). Non-adjacent to B(4) and D(5). Diagonals: CB, CD.
  - E(3) is adjacent to C(2) and B(4). Non-adjacent to A(1) and D(5). Diagonals: EA, ED.
  - B(4) is adjacent to E(3) and D(5). Non-adjacent to A(1) and C(2). Diagonals: BA, BC.
  - D(5) is adjacent to B(4) and A(1). Non-adjacent to C(2) and E(3). Diagonals: DC, DE.

So the diagonals are: AE, AB, CB, CD, ED, ED (some repeated). The 5 diagonals are: AE, AB, CB, CD, DE. Wait, that's only 5 for a pentagon (which has 5 diagonals). Let me recount: AE, AB, CB, CD, DE. Yes, 5 diagonals.

Now, ∠CBE = 90°: this is the angle at B between BC (a diagonal) and BE (a side). 
∠ABD = 90°: this is the angle at B between BA (a diagonal) and BD (a side).

EA and CD are both diagonals, and they intersect at P.

So the problem is about a pentagon where two specific diagonals from B (BA and BC) are perpendicular to the two sides at B (BD and BE respectively).

Let me reconsider the geometry. In the pentagon ACEBD, at vertex B, the two sides are EB and BD. The angle ∠EBD is the interior angle at B. The diagonals from B are BA and BC.

∠CBE = 90°: diagonal BC ⊥ side BE.
∠ABD = 90°: diagonal BA ⊥ side BD.

So at vertex B, we have four rays: BE (side), BD (side), BC (diagonal), BA (diagonal). BC ⊥ BE and BA ⊥ BD.

The interior angle at B is ∠EBD. The angle ∠ABC = β is the angle between the two diagonals from B.

Now, the four rays BE, BC, BA, BD emanate from B. We know BC ⊥ BE and BA ⊥ BD. The angle between BC and BA is β (the angle of the original triangle at B).

The arrangement: if we go around B, the order of rays could be BE, BC, BA, BD or BE, BA, BC, BD, etc.

If the order is BE, BC, BA, BD (say counterclockwise):
- ∠EBC = 90° (given)
- ∠CBA = β
- ∠ABD = 90° (given)
- ∠DBE = 360° - 90° - β - 90° = 180° - β (the interior angle at B)

This seems reasonable. The interior angle at B is 180° - β, which is > 90° since β < 90° (acute triangle).

Alternatively, if the order is BE, BA, BC, BD:
- ∠EBA = some angle
- ∠ABC = β
- ∠CBD = some angle
- ∠DBE = some angle
With ∠EBC = ∠EBA + ∠ABC = 90° and ∠ABD = ∠ABC + ∠CBD = 90°.
So ∠EBA = 90° - β and ∠CBD = 90° - β.
∠DBE = 360° - (90° - β) - β - (90° - β) = 360° - 90° + β - β - 90° + β = 180° + β.
Interior angle at B would be 180° + β > 180°, which makes the pentagon non-convex at B. This is possible for a non-degenerate pentagon.

Hmm, there are multiple possible arrangements. Let me think about which one is consistent with the pentagon being non-degenerate and the other conditions.

Let me try the first arrangement: counterclockwise order BE, BC, BA, BD.

Place B at origin. Let BC be along the positive x-axis: C = (10, 0).
BE is 90° counterclockwise from BC, so BE is along the positive y-axis: E = (0, e) with e > 0.
BA is at angle β counterclockwise from BC: A = (11 cos β, 11 sin β) with β acute.
BD is 90° counterclockwise from BA: D = d(-sin β, cos β) with d > 0.

This is exactly Case B from before! And in Case B, I found that the angle condition and AE = CD lead to d = 11, e = 10 (from the algebraic manipulation), and then ED = 20 gives cos β = 179/220, but AP = 4 is inconsistent.

Wait, actually, let me redo Case B more carefully. In Case B:

E = (0, e), e > 0
D = (-d sin β, d cos β), d > 0

AE² = 121 - 22e sin β + e²
CD² = 100 + 20d sin β + d²

AE = CD: 121 - 22e sin β + e² = 100 + 20d sin β + d² → 21 - 22e sin β + e² - 20d sin β - d² = 0 ... (I')

cos(∠AEB) = (e - 11 sin β)/AE (e > 0)
cos(∠DCB) = (d sin β + 10)/AE

∠AEB = ∠DCB: e - 11 sin β = d sin β + 10 → e - d sin β = 10 + 11 sin β ... (II')

ED² = d² + e² - 2ed cos β = 400 ... (III')

From (II'): e = 10 + 11 sin β + d sin β = 10 + (11 + d) sin β.

Sub into (I'):
21 - 22(10 + (11+d) sin β) sin β + (10 + (11+d) sin β)² - 20d sin β - d² = 0

Let me expand:
21 - 220 sin β - 22(11+d) sin²β + 100 + 20(11+d) sin β + (11+d)² sin²β - 20d sin β - d² = 0

121 + (-220 + 220 + 20d - 20d) sin β + (-22(11+d) + (11+d)²) sin²β - d² = 0

121 + (11+d)(-22 + 11 + d) sin²β - d² = 0

121 + (11+d)(d - 11) sin²β - d² = 0

121 + (d² - 121) sin²β - d² = 0

121 - 121 sin²β + d² sin²β - d² = 0

121 cos²β - d² cos²β = 0

(121 - d²) cos²β = 0

d = 11 (since cos β ≠ 0).

Then e = 10 + (11 + 11) sin β = 10 + 22 sin β.

ED² = 121 + (10 + 22 sin β)² - 2 × 11 × (10 + 22 sin β) cos β = 400.

Let me expand:
121 + 100 + 440 sin β + 484 sin²β - 22(10 + 22 sin β) cos β = 400

221 + 440 sin β + 484 sin²β - 220 cos β - 484 sin β cos β = 400

440 sin β + 484 sin²β - 220 cos β - 484 sin β cos β = 179

Hmm, this is more complex because e depends on β. Let me use sin²β + cos²β = 1.

484 sin²β = 484(1 - cos²β) = 484 - 484 cos²β.

440 sin β + 484 - 484 cos²β - 220 cos β - 484 sin β cos β = 179

440 sin β - 484 cos²β - 220 cos β - 484 sin β cos β = 179 - 484 = -305

440 sin β - 220 cos β - 484 cos β(sin β + cos β) = -305

This is getting messy. Let me try a substitution. Let me set s = sin β, c = cos β.

440s + 484s² - 220c - 484sc = 179

With s² + c² = 1:
440s + 484(1 - c²) - 220c - 484sc = 179
440s + 484 - 484c² - 220c - 484sc = 179
440s - 484c² - 220c - 484sc = -305
440s - 220c - 484c(s + c) = -305

Let me try s + c = t, then sc = (t² - 1)/2 and s² + c² = 1.
Also s - c = u, t² + u² = 2.

440s - 220c = 220(2s - c). Hmm, 2s - c isn't simply expressible in terms of t.

Let me try a different approach. Let me just compute AP and set it to 4, and see what we get.

With d = 11, e = 10 + 22s:

A = (11c, 11s)
E = (0, 10 + 22s)
C = (10, 0)
D = (-11s, 11c)

AE² = 221 - 220s + 484s² - 440s = 221 + 484s² - 660s... 

Wait, let me recompute AE².
AE² = (11c)² + (11s - (10 + 22s))² = 121c² + (-10 - 11s)² = 121c² + (10 + 11s)² = 121c² + 100 + 220s + 121s² = 121(c² + s²) + 100 + 220s = 121 + 100 + 220s = 221 + 220s.

Oh interesting, AE² = 221 + 220s. (Different from Case A where it was 221 - 220s.)

CD² = (10 + 11s)² + (11c)² = 100 + 220s + 121s² + 121c² = 100 + 220s + 121 = 221 + 220s. ✓ (AE = CD)

Now, line EA: from E(0, 10 + 22s) to A(11c, 11s).
Direction: (11c, 11s - 10 - 22s) = (11c, -10 - 11s).
Parametrize: P = E + t(A - E) = (11ct, 10 + 22s + t(-10 - 11s)) = (11ct, 10 + 22s - t(10 + 11s)).

Line CD: from C(10, 0) to D(-11s, 11c).
Direction: (-11s - 10, 11c).
Parametrize: P = C + u(D - C) = (10 + u(-11s - 10), 11cu) = (10 - u(10 + 11s), 11cu).

Setting equal:
11ct = 10 - u(10 + 11s) ... (1)
10 + 22s - t(10 + 11s) = 11cu ... (2)

Let me denote p = 11c, q = 10 + 11s.

(1): pt = 10 - qu → pt + qu = 10
(2): 10 + 22s - qt = pu → -qt - pu = -(10 + 22s) → qt + pu = 10 + 22s

System:
pt + qu = 10
qt + pu = 10 + 22s... 

wait, let me redo (2): 10 + 22s - qt = pu → -qt - pu = -(10 + 22s) → qt + pu = 10 + 22s. Hmm, that doesn't look right.

(2): 10 + 22s - t(10 + 11s) = 11cu
10 + 22s - qt = pu
-qt - pu = -(10 + 22s)
qt + pu = 10 + 22s

Wait, that's wrong. Let me redo:
10 + 22s - qt = pu
→ -qt - pu = -(10 + 22s)
→ qt + pu = 10 + 22s

Hmm, but the sign: 10 + 22s - qt = pu means pu + qt = 10 + 22s. Yes.

System:
pt + qu = 10 ... (1)
pu + qt = 10 + 22s ... (2)

Wait, (2) should be: pu + qt = 10 + 22s. But let me double check: from (2), 10 + 22s - qt = pu, so pu = 10 + 22s - qt, so pu + qt = 10 + 22s. Yes.


