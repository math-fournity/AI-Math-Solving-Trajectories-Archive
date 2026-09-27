# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
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

- **CONNECTION_ERROR**: The AI didn't really attempt the problem — the thinking is extremely short (< 500 chars), contains API connection errors, garbled text, or has NO mathematical content at all (e.g., only error messages or empty output). This is a technical failure, not a mathematical one. **Important**: If the AI solved a DIFFERENT problem than the one given (wrong problem, misread problem), that is DIRECTION_ERROR, not CONNECTION_ERROR. CONNECTION_ERROR is only for technical failures where no real thinking happened.

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
  <problem_id>polymath_01530</problem_id>
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
- If the AI's thinking is too short to analyze (< 500 chars AND no mathematical content), output CONNECTION_ERROR. But if the AI solved a different problem or went in the wrong direction, use DIRECTION_ERROR even if the thinking is short.
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

Let \( n \geq 4 \) and \( n \) points be given in the plane. After connecting all pairs of points with line segments, what is the maximum possible number of line segments that do not intersect any other segment except at their endpoints?

## Standard Solution

**Solution:**  
Let us call a line segment that does not intersect any other segment except at its endpoints a special segment. For \( n \geq 4 \), we will prove by induction that the maximum number of special segments is \( 2n-2 \).

If the given \( n \) points are the vertices of a convex \( n \)-gon, the number of special segments is exactly \( n \) (the sides of the \( n \)-gon), and in this case \( n < 2n-2 \). Otherwise, one of the \( n \) points, say \( A \), will not be on the boundary of the convex hull of these \( n \) points. Connect some pairs of the remaining \( n-1 \) points so that all closed regions are triangles (triangulation). The point \( A \) must be inside one of these triangles, say \( P_1P_2P_3 \). Clearly, there are no other points inside triangle \( P_1P_2P_3 \) except \( A \). If \( A \) is removed, by the induction hypothesis there can be at most \( 2(n-1)-2 = 2n-4 \) special segments. When \( A \) is placed back, only \( [AP_1], [AP_2], [AP_3] \) can be added as special segments (other segments from \( A \) will intersect one of the sides of triangle \( P_1P_2P_3 \)).

If at least one of \( [P_1P_2], [P_1P_3], [P_2P_3] \) is not special after removing \( A \), then some segment \( \ell \) must cross triangle \( P_1P_2P_3 \) (possibly with one endpoint at \( P_1, P_2 \), or \( P_3 \)). Then \( \ell \) will intersect at least one of \( [AP_1], [AP_2], [AP_3] \). Thus, when \( A \) is placed back, at most two of \( [AP_1], [AP_2], [AP_3] \) can be special, so the total is at most \( 2n-4+2=2n-2 \).

If all of \( [P_1P_2], [P_1P_3], [P_2P_3] \) are special after removing \( A \), then for \( n>4 \) there is a point \( Q \) outside triangle \( P_1P_2P_3 \), and the segment \( [AQ] \) will intersect at least one of \( [P_1P_2], [P_1P_3], [P_2P_3] \). Thus, at least one of these loses its special property. Again, the total is at most \( 2n-4+2=2n-2 \).

Finally, let's show that \( 2n-2 \) special segments are possible. Take a circle and a point \( A \) outside the circle. Let the tangents from \( A \) to the circle touch at \( X \) and \( Y \). Take any \( A_1, A_2, \ldots, A_{n-1} \) on the minor arc \( XY \). Then each of the segments \( [A_1A_2], [A_2A_3], \ldots, [A_{n-1}A_1], [AA_1], [AA_2], \ldots, [AA_{n-1}] \) will be special.

\(2n-2\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. The problem asks: given n≥4 points in the plane, connect all pairs with line segments. What is the maximum possible number of line segments that do not intersect any other segment except at their endpoints?

This is a classic problem. The answer is that the maximum number of non-crossing edges in a triangulation of n points... wait, let me think carefully.

Actually, the question is about the maximum number of edges that are "non-crossing" — i.e., edges that don't cross any other edge. But we connect ALL pairs, so we have a complete geometric graph. We want to maximize the number of edges that don't cross any other edge.

Wait, let me re-read. "After connecting all pairs of points with line segments, what is the maximum possible number of line segments that do not intersect any other segment except at their endpoints?"

So we draw all $\binom{n}{2}$ segments. Among these, some segments cross other segments. We want to count the segments that do NOT cross any other segment (intersections at endpoints don't count). We want to maximize this count over all configurations of n points.

A segment that doesn't cross any other segment is an edge of the "non-crossing" subgraph — it's an edge in some triangulation-like structure. Actually, a segment that doesn't cross any other segment in the complete geometric graph is exactly an edge of the convex hull triangulation... no.

Let me think again. In the complete geometric graph on n points, an edge is "uncrossed" if no other edge crosses it. The set of uncrossed edges forms a planar graph (since no two uncrossed edges cross each other — if two uncrossed edges crossed each other, each would cross the other, contradiction). So the uncrossed edges form a planar straight-line graph.

We want to maximize the number of uncrossed edges. The uncrossed edges form a planar graph, so by Euler's formula, a planar graph on n vertices has at most 3n - 6 edges (for n ≥ 3).

Can we achieve 3n - 6? We need a triangulation. In a triangulation of n points in general position (no three collinear), every face is a triangle, and the number of edges is 3n - 3 - h where h is the number of hull vertices. Wait, let me recall: for a triangulation of n points with h points on the convex hull, the number of edges is 3n - 3 - h, and the number of triangles is 2n - 2 - h.

To maximize edges, we minimize h. The minimum h is 3 (all points in convex position would give h = n, but we want h small). If h = 3, edges = 3n - 6.

But wait — are all edges of a triangulation "uncrossed" in the complete geometric graph? Yes! In a triangulation, no two edges cross. And every edge of the triangulation, does it cross any edge of the complete graph? An edge e of the triangulation: could some other edge of the complete graph cross e? If edge e = (a,b) is in the triangulation, and some edge (c,d) crosses it, then (c,d) is also in the complete graph. But the question is whether e is "uncrossed" — meaning no edge of the complete graph crosses e.

Hmm, so the question is: in the complete geometric graph, which edges are uncrossed? An edge (a,b) is uncrossed if no other edge (c,d) crosses it.

The uncrossed edges are exactly the edges of the "crossing-free" subgraph, which is the set of edges that appear in every... no. The uncrossed edges are exactly the edges of the convex hull plus the edges that are in the "relative interior" of the triangulation... 

Actually, let me think about this differently. The set of uncrossed edges forms a planar graph (as argued). But is every planar subgraph achievable? No — the uncrossed edges have a specific structure.

Claim: The uncrossed edges are exactly the edges of the convex hull of the point set, plus... no, that's not right either.

Let me think about small cases. For n = 4 points in convex position (a convex quadrilateral): the 4 hull edges are uncrossed, and the 2 diagonals cross each other. So uncrossed edges = 4. For n = 4 with one point inside a triangle: the 3 hull edges are uncrossed, and the 3 edges from the interior point to the hull vertices are uncrossed (they don't cross anything). The 3 edges among hull vertices that are not hull edges... wait, in a triangle with one interior point, the complete graph has $\binom{4}{2} = 6$ edges. The 3 hull edges don't cross anything. The 3 edges from interior to hull vertices: do any of them cross? No, they all share the interior point as endpoint. Do they cross any hull edge? An edge from interior point to a hull vertex — could it cross a hull edge? The hull edges form a triangle, and the interior point is inside. The edge from interior to a vertex stays inside the triangle, so it doesn't cross any hull edge. So all 6 edges are uncrossed? Wait, that gives 6 = 3(4) - 6 = 6. Yes!

For n = 4 convex: uncrossed = 4 < 6. For n = 4 with interior point: uncrossed = 6 = 3n - 6.

So the maximum for n = 4 is 6, achieved with 3 hull vertices and 1 interior point.

Now, can we always achieve 3n - 6? We need h = 3 (triangular hull) and a triangulation. With h = 3, a triangulation has 3n - 6 edges. And all triangulation edges are uncrossed (since triangulation edges don't cross each other, and... wait, but we need to check that triangulation edges don't cross ANY edge of the complete graph, not just other triangulation edges).

Hmm, this is the key point. A triangulation edge (a,b) — could some non-triangulation edge (c,d) of the complete graph cross it?

Consider a triangulation of n points with triangular hull. Take a triangulation edge e = (a,b). This edge is either a hull edge or an interior edge. 

If e is a hull edge: no edge of the complete graph can cross it, because all points are on one side of the hull edge (inside the hull), so any segment between two points stays on that side or on the edge. Actually, a hull edge can't be crossed by any segment between two points of the set, since all points are in the closed half-plane on one side.

If e is an interior edge: e is shared by two triangles, say triangle (a,b,c) on one side and triangle (a,b,d) on the other side. The edge e divides the plane into two half-planes. Point c is on one side, point d is on the other. Now, could some edge (p,q) of the complete graph cross e? For (p,q) to cross e, p and q must be on opposite sides of the line through e. 

The points on c's side of line ab: includes c and possibly others. The points on d's side: includes d and possibly others. 

In a triangulation, the edge e = (a,b) is "flippable" if there exist points on both sides. But the key question is: does any edge (p,q) with p on c's side and q on d's side cross the segment ab?

Not necessarily! The edge (p,q) crosses the LINE through ab, but might not cross the SEGMENT ab. It crosses the segment ab only if the crossing point is between a and b.

Hmm, so actually a triangulation edge CAN be crossed by a non-triangulation edge. Let me reconsider.

Example: n = 5. Triangle hull with vertices A, B, C. Two interior points P, Q. Triangulation: say triangles ABP, BCP, CAP... wait, with 2 interior points, we need to be more careful.

Let me take a specific example. Hull: A=(0,0), B=(10,0), C=(0,10). Interior points: P=(1,1), Q=(2,2). 

Hmm, P and Q are collinear with A. Let me use P=(1,1), Q=(3,1).

Triangulation edges: hull edges AB, BC, CA. Interior edges: AP, BP, CP, AQ, BQ, CQ, PQ. That's 3 + 7 = 10 = 3(5) - 6 + ... wait 3n-6 = 9 for n=5. Let me recount. With h=3, edges = 3n - 3 - h = 15 - 3 - 3 = 9. So 9 edges.

A triangulation: AB, BC, CA (hull), and then we need 6 more interior edges. Triangles: 2n - 2 - h = 10 - 2 - 3 = 5 triangles.

One possible triangulation: 
- Triangle ABP, BCP, CAP (triangulating with just P) — that's 3 triangles using P, with edges AP, BP, CP added.
- Now add Q. Q is inside one of these triangles, say inside triangle ABP. Then we split ABP into ABQ, BQP, AQP, adding edges AQ, BQ, PQ.
- Total: 3 hull + AP, BP, CP + AQ, BQ, PQ = 9 edges. Triangles: BCP, CAP, ABQ, BQP, AQP = 5. ✓

Now, is edge CP crossed by any complete-graph edge? CP goes from C=(0,10) to P=(1,1). Does edge BQ = (10,0)-(3,1) cross CP? Let me check. CP: from (0,10) to (1,1). BQ: from (10,0) to (3,1). These are far apart, probably don't cross.

Does edge AQ = (0,0)-(3,1) cross CP = (0,10)-(1,1)? AQ goes from origin to (3,1), CP goes from (0,10) to (1,1). Let me check if they cross. Parametrize AQ: (3t, t) for t∈[0,1]. CP: (s, 10-9s) for s∈[0,1]. Setting equal: 3t = s and t = 10 - 9s = 10 - 27t. So t + 27t = 10, 28t = 10, t = 10/28 = 5/14. s = 15/14 > 1. So s > 1, meaning the intersection is outside segment CP. So they don't cross.

This is getting complicated. Let me think about it more abstractly.

The key theorem: In a triangulation of a point set, every edge of the triangulation is uncrossed by any edge of the complete geometric graph.

Wait, is this true? Actually, I think this IS true, and here's why:

Consider a triangulation edge e = (a,b). If e is a hull edge, it can't be crossed (as argued). If e is an interior edge, it's shared by two triangles T1 = (a,b,c) and T2 = (a,b,d). The triangle T1 is empty (contains no points of the set in its interior), and T2 is empty. Now, any edge (p,q) of the complete graph that crosses segment ab must have p on one side of line ab and q on the other. Say p is on the c-side and q is on the d-side. 

For (p,q) to cross the segment ab (not just the line), the crossing point must be between a and b. The segment ab, together with the two triangles, forms a "diamond" shape a-c-b-d (or a-d-b-c). The edge (p,q) crosses ab means p and q are on opposite sides. 

But here's the thing: p is in the half-plane on c's side of line ab, and q is on d's side. The segment pq must cross line ab somewhere. Does it cross the segment ab specifically?

The segment ab is bounded. The line through ab extends infinitely. The crossing of pq with line ab could be outside the segment ab.

Hmm, so it's NOT automatically true that every triangulation edge is uncrossed. Let me think of a counterexample.

Consider 4 points: A=(0,0), B=(10,0), C=(5,5), D=(5,-5). Wait, D is outside the triangle ABC. Let me reconsider.

Actually, for a triangulation to exist with h=3, all points must be inside the triangle. Let me try: A=(0,0), B=(10,0), C=(5,10). Interior: P=(4,1), Q=(6,1).

Triangulation: Let's say triangles ABP, BCP, CAP, and Q is inside triangle BCP. Wait, is Q=(6,1) inside triangle BCP where B=(10,0), C=(5,10), P=(4,1)? Let me check. Actually this is getting complicated. Let me think more carefully.

Actually, I recall now that this is a well-known result. The maximum number of non-crossing edges is $3n - 6$ for $n \geq 3$, achieved when the points are in "general position" with exactly 3 points on the convex hull (i.e., all other points inside a triangle), and the non-crossing edges form a triangulation.

But the subtlety is whether all triangulation edges are truly uncrossed. Let me think about this more carefully.

Claim: In a triangulation of a point set S, every edge of the triangulation is not crossed by any edge of the complete geometric graph on S.

Proof: Let e = (a,b) be a triangulation edge. 
- If e is a hull edge: All points of S lie in the closed half-plane determined by e. Any segment between two points of S lies in this half-plane, so cannot cross e (which is on the boundary). ✓
- If e is an interior edge: e is shared by two triangles T1 = (a,b,c) and T2 = (a,b,d), with c and d on opposite sides of line ab. Both triangles are empty (no points of S in their interiors).

Now suppose some edge (p,q) of the complete graph crosses segment ab. Then p and q are on opposite sides of line ab. WLOG p is on the c-side and q is on the d-side.

The segment pq crosses line ab at some point x. For pq to cross segment ab, x must lie on the segment ab (between a and b).

Now, x is on segment ab, which is an edge of both triangles T1 and T2. The point x is on the boundary of T1 (on edge ab) and on the boundary of T2 (on edge ab).

The segment from p to x: p is on the c-side of line ab. The triangle T1 = (a,b,c) is on the c-side. Is p inside T1? Not necessarily — p could be outside T1 but still on the c-side of line ab.

Hmm, so p might not be inside T1. In that case, the segment px might exit T1 through edge ac or bc, not through ab. But x is on ab...

Let me think about this differently. The segment pq crosses ab at point x (between a and b). Consider the triangle T1 = (a,b,c) on the c-side. The point p is on the c-side. The segment from p to x (where x is on edge ab of T1) must enter T1 at some point, because x is on the boundary of T1 and p is on the same side as c.

Actually, p might be outside T1. For example, p could be beyond vertex c, outside the triangle. But the segment from p to x must cross the boundary of T1. Since x is on edge ab of T1, and p is on the c-side, the segment px must cross either edge ac or edge bc of T1 (or p is inside T1).

Case 1: p is inside T1. But T1 is empty (no points of S in its interior). Contradiction since p ∈ S.

Case 2: p is outside T1, on the c-side. The segment from p to x (x on edge ab) must cross the boundary of T1. Since x is on edge ab, the segment enters T1 through edge ab at x (if p is "beyond" edge ab, but p is on the c-side, same as c, so p is on the interior side of edge ab relative to T1). Wait, I need to be more careful.

The triangle T1 has edges ab, bc, ca. The edge ab has c on one side (the interior of T1). Point p is on the c-side of line ab, so p is on the same side as the interior of T1 relative to edge ab. 

If p is inside T1: contradiction (T1 is empty).
If p is outside T1: p is on the c-side of line ab but outside the triangle. Then p must be on the far side of edge ac or edge bc (the side away from b or away from a respectively). The segment from p to x (x on ab) must cross edge ac or edge bc to enter T1.

So the segment pq (going from p through x to q) crosses edge ac or edge bc of the triangulation. But that's a different edge — we're trying to show that ab is uncrossed, and we've shown that if (p,q) crosses ab, then (p,q) also crosses ac or bc. That doesn't directly give a contradiction.

Hmm, so my approach isn't working directly. Let me reconsider.

Actually wait. The question is whether edge (p,q) crosses edge ab. I was trying to prove it can't. But maybe it can? Let me try to construct a concrete counterexample.

Let me try n=5. Hull: A=(0,0), B=(10,0), C=(5,10). Interior: P=(1,1), Q=(9,1).

A triangulation: 
- Triangles with P: ABP (A=(0,0), B=(10,0), P=(1,1)), BCP, CAP.
  - BCP: B=(10,0), C=(5,10), P=(1,1). Is this a valid triangle? Yes.
  - CAP: C=(5,10), A=(0,0), P=(1,1). Yes.
- Now Q=(9,1). Is Q inside BCP? BCP has vertices (10,0), (5,10), (1,1). Let me check if (9,1) is inside. The triangle BCP: going B→C→P. Edge BC from (10,0) to (5,10): the line is x + y/2 = 10... let me use barycentric or just check. Actually, (9,1) is close to B=(10,0). Edge BP from (10,0) to (1,1): parametrically (10-9t, t). At y=1, t=1, x=1. So the edge BP at y=1 is at x=1. Point (9,1) has x=9 > 1, so it's on the B-side of edge BP. Edge BC from (10,0) to (5,10): at y=1, t=0.1, x=10-0.5=9.5. So at y=1, edge BC is at x=9.5. Point (9,1) has x=9 < 9.5, so it's on the P-side of edge BC. Edge CP from (5,10) to (1,1): at y=1, x=1. Point (9,1) has x=9 > 1, so it's on the B-side of CP. So Q=(9,1) is inside triangle BCP? It's on the B-side of BP, P-side of BC, and B-side of CP. For it to be inside BCP, it needs to be on the correct side of all three edges. The interior of BCP is on the P-side of BC (since P is opposite to BC... wait, P is a vertex of BCP). Let me redo this.

Triangle BCP with vertices B=(10,0), C=(5,10), P=(1,1). The interior is bounded by edges BC, CP, PB.
- Edge BC: from B to C. The third vertex P=(1,1) is on one side. Q=(9,1): is it on the same side as P? Line BC: from (10,0) to (5,10), direction (-5,10), normal (10,5) or (2,1). Line: 2(x-10) + 1(y-0) = 0 → 2x + y = 20. P: 2(1)+1 = 3 < 20. Q: 2(9)+1 = 19 < 20. Same side. ✓
- Edge CP: from C=(5,10) to P=(1,1), direction (-4,-9), normal (-9,4) or (9,-4). Line: 9(x-5) - 4(y-10) = 0 → 9x - 4y = 5. B: 9(10)-4(0) = 90 > 5. Q: 9(9)-4(1) = 77 > 5. Same side as B. ✓
- Edge PB: from P=(1,1) to B=(10,0), direction (9,-1), normal (-1,-9) or (1,9). Line: 1(x-1) + 9(y-1) = 0 → x + 9y = 10. C: 5 + 90 = 95 > 10. Q: 9 + 9 = 18 > 10. Same side as C. ✓

So Q is inside triangle BCP. Good. So we split BCP into BCQ, CQP, PBQ. Adding edges BQ, CQ, PQ.

Total triangulation edges: AB, BC, CA (hull) + AP, BP, CP (from P) + BQ, CQ, PQ (from Q) = 9 = 3(5)-6. ✓

Now, is edge CP crossed by any complete-graph edge? CP goes from C=(5,10) to P=(1,1). 

Consider edge AQ from A=(0,0) to Q=(9,1). Does AQ cross CP?

AQ: parametrically (9t, t) for t∈[0,1].
CP: parametrically (5-4s, 10-9s) for s∈[0,1].

Set equal: 9t = 5-4s and t = 10-9s.
From second: t = 10-9s. Substitute: 9(10-9s) = 5-4s → 90-81s = 5-4s → 85 = 77s → s = 85/77 ≈ 1.104. Since s > 1, the intersection is outside segment CP. So AQ doesn't cross CP. ✓

What about edge BQ from B=(10,0) to Q=(9,1)? This is a triangulation edge, so it doesn't cross CP (both in triangulation).

What about edge AP from A=(0,0) to P=(1,1)? Triangulation edge, doesn't cross CP.

Hmm, what about edge AQ? We showed it doesn't cross CP. 

Let me try a different configuration where a triangulation edge IS crossed.

Actually, let me think about this more carefully. I think the key insight is:

Theorem: In a triangulation of a point set, every edge is uncrossed by the complete geometric graph.

Proof for interior edge e = (a,b) shared by triangles (a,b,c) and (a,b,d):

The two triangles form a quadrilateral a-c-b-d (or a-d-b-c) that is "empty" — no points of S inside either triangle, hence no points inside the quadrilateral (the quadrilateral is the union of the two triangles, and any point inside would be in one of the triangles).

Now suppose edge (p,q) crosses segment ab. Then p and q are on opposite sides of line ab. WLOG p is on the c-side, q is on the d-side.

The crossing point x is on segment ab. Now, x is inside the quadrilateral a-c-b-d (on the diagonal ab). The segment from p to x: p is on the c-side. The segment must enter the triangle (a,b,c) to reach x (which is on edge ab of this triangle). If p is outside triangle (a,b,c), the segment px must cross edge ac or edge bc. But then (p,q) would cross ac or bc, not just ab. That's fine — (p,q) can cross multiple edges. The question is just whether (p,q) crosses ab.

Wait, I think I was overcomplicating this. The question is: does (p,q) cross ab? And I need to show it doesn't.

Hmm, but actually, it CAN cross ab. Let me try harder to find a counterexample.

Let me try: A=(0,0), B=(10,0), C=(5,10). P=(2,1), Q=(8,1). 

Triangulation: P inside ABC, split into ABP, BCP, CAP. Q inside BCP (similar to before). Split BCP into BCQ, CQP, PBQ.

Edges: AB, BC, CA, AP, BP, CP, BQ, CQ, PQ.

Now consider edge CP from C=(5,10) to P=(2,1). And edge AQ from A=(0,0) to Q=(8,1).

AQ: (8t, t), CP: (5-3s, 10-9s).
8t = 5-3s, t = 10-9s.
8(10-9s) = 5-3s → 80-72s = 5-3s → 75 = 69s → s = 75/69 ≈ 1.087. Still > 1.

Let me try to make AQ cross CP. I need the intersection to have s ∈ (0,1) and t ∈ (0,1).

AQ: (8t, t), CP: (5-3s, 10-9s).
t = 10-9s, 8t = 5-3s.
8(10-9s) = 5-3s → 80 - 72s = 5 - 3s → 75 = 69s → s = 75/69 > 1.

The issue is that AQ is nearly horizontal (from (0,0) to (8,1)) while CP goes from (5,10) to (2,1), which is mostly vertical. They might not cross within the segments.

Let me try a different approach. Let me put points such that a non-triangulation edge clearly crosses a triangulation edge.

A=(0,0), B=(10,0), C=(5,10). P=(3,3), Q=(7,3).

Triangulation: P inside ABC. Triangles ABP, BCP, CAP. Q inside BCP? Let me check. BCP: B=(10,0), C=(5,10), P=(3,3). Is Q=(7,3) inside?

Edge BC: 2x+y=20. Q: 14+3=17<20, P: 6+3=9<20. Same side. ✓
Edge CP: from (5,10) to (3,3), direction (-2,-7), normal (7,-2). Line: 7(x-5)-2(y-10)=0 → 7x-2y=15. B: 70>15, Q: 49-6=43>15. Same side. ✓
Edge PB: from (3,3) to (10,0), direction (7,-3), normal (3,7). Line: 3(x-3)+7(y-3)=0 → 3x+7y=30. C: 15+70=85>30, Q: 21+21=42>30. Same side. ✓

So Q is inside BCP. Split into BCQ, CQP, PBQ. Edges: BQ, CQ, PQ added.

Now, edge CP from C=(5,10) to P=(3,3). Edge AQ from A=(0,0) to Q=(7,3).

AQ: (7t, 3t), CP: (5-2s, 10-7s).
7t = 5-2s, 3t = 10-7s.
From second: t = (10-7s)/3. Substitute: 7(10-7s)/3 = 5-2s → (70-49s)/3 = 5-2s → 70-49s = 15-6s → 55 = 43s → s = 55/43 ≈ 1.28. Still > 1.

Hmm, it seems hard to make AQ cross CP. Let me think about why.

The triangulation edge CP has the property that triangle CAP is on one side (containing A) and triangle BCP (now split) is on the other side (containing B and Q). The edge AQ goes from A (on the C-side... wait, A is a vertex of triangle CAP which is on one side of CP).

Actually, A is on one side of line CP, and Q is on the other side (Q is inside BCP, which is on the other side of CP from A). So AQ does cross the LINE through CP. But does it cross the SEGMENT CP?

The segment CP goes from C=(5,10) to P=(3,3). A=(0,0) is on one side, Q=(7,3) is on the other. The line through CP: let me compute. Direction: (-2,-7), normal: (7,-2). Line: 7x - 2y = 7(5) - 2(10) = 35-20 = 15. A: 0-0=0 < 15. Q: 49-6=43 > 15. So A and Q are on opposite sides. ✓

The intersection of AQ with line CP: we computed s = 55/43 > 1, meaning the intersection is beyond P on the line CP (past P away from C). So AQ crosses the line CP beyond P, not within the segment CP.

Why does this happen? Because P is "between" A and Q in some sense along the direction perpendicular to CP. The segment AQ passes "below" P (closer to A's side) and exits the line CP beyond P.

Can I make it cross within the segment? I'd need the intersection parameter s to be in (0,1). Let me try to engineer this.

Let me use A=(0,0), B=(10,0), C=(5,10). P=(4,5), Q=(6,1).

Check P inside ABC: Edge AB: y=0, P has y=5>0. ✓ Edge BC: 2x+y=20, P: 8+5=13<20. ✓ Edge CA: from C=(5,10) to A=(0,0), direction (-5,-10), normal (10,-5) or (2,-1). Line: 2x-y=0. B: 20>0, P: 8-5=3>0. Same side. ✓ So P is inside ABC.

Triangles: ABP, BCP, CAP.
Check Q inside BCP: B=(10,0), C=(5,10), P=(4,5).
Edge BC: 2x+y=20. Q: 12+1=13<20, P: 8+5=13<20. Same side. ✓
Edge CP: from (5,10) to (4,5), direction (-1,-5), normal (5,-1). Line: 5(x-5)-(y-10)=0 → 5x-y=15. B: 50>15, Q: 30-1=29>15. Same side. ✓
Edge PB: from (4,5) to (10,0), direction (6,-5), normal (5,6). Line: 5(x-4)+6(y-5)=0 → 5x+6y=50. C: 25+60=85>50, Q: 30+6=36<50. OPPOSITE sides! ✗

So Q is NOT inside BCP. Q is on the other side of edge PB from C. So Q is inside triangle ABP instead.

Let me check: ABP with A=(0,0), B=(10,0), P=(4,5).
Edge AB: y=0. Q: y=1>0. P: y=5>0. Same side. ✓
Edge BP: from (10,0) to (4,5), direction (-6,5), normal (5,6). Line: 5(x-10)+6(y-0)=0 → 5x+6y=50. A: 0<50, Q: 30+6=36<50. Same side. ✓
Edge PA: from (4,5) to (0,0), direction (-4,-5), normal (5,-4). Line: 5(x-4)-4(y-5)=0 → 5x-4y=0. B: 50>0, Q: 30-4=26>0. Same side. ✓

So Q is inside ABP. Split ABP into ABQ, BQP, QAP. Add edges AQ, BQ, PQ.

Triangulation edges: AB, BC, CA, AP, BP, CP, AQ, BQ, PQ = 9. ✓

Now, does any non-triangulation edge cross a triangulation edge?

The non-triangulation edges are: AC (wait, CA is a hull edge, it's in the triangulation). Let me list all $\binom{5}{2}=10$ edges: AB, AC, AD... wait, the points are A, B, C, P, Q.

All edges: AB, AC, AP, AQ, BC, BP, BQ, CP, CQ, PQ.
Triangulation edges: AB, BC, CA (=AC), AP, BP, CP, AQ, BQ, PQ.
Non-triangulation edge: CQ.

So the only non-triangulation edge is CQ. Does CQ cross any triangulation edge?

CQ from C=(5,10) to Q=(6,1). Let me check against each triangulation edge:
- AB: from (0,0) to (10,0), y=0. CQ goes from y=10 to y=1, doesn't reach y=0. No crossing.
- BC: shared endpoint C. No crossing (except at C).
- CA: shared endpoint C. No crossing.
- AP: from (0,0) to (4,5). CQ from (5,10) to (6,1). Do they cross? AP: (4t, 5t). CQ: (5+s, 10-9s) where s∈[0,1] (from C to Q: (5+1·s, 10-9·s)). 4t = 5+s, 5t = 10-9s. From first: s = 4t-5. From second: 5t = 10-9(4t-5) = 10-36t+45 = 55-36t. So 41t = 55, t = 55/41 ≈ 1.34 > 1. No crossing.
- BP: from (10,0) to (4,5). CQ from (5,10) to (6,1). BP: (10-6t, 5t). CQ: (5+s, 10-9s). 10-6t = 5+s, 5t = 10-9s. s = 5-6t. 5t = 10-9(5-6t) = 10-45+54t = -35+54t. 49t = 35, t = 5/7 ≈ 0.714. s = 5-6(5/7) = 5-30/7 = 5/7 ≈ 0.714. Both in (0,1). So BP and CQ cross!

So edge CQ crosses edge BP. But BP is a triangulation edge. So BP IS crossed by CQ!

This means BP is NOT an uncrossed edge. So the triangulation does NOT consist entirely of uncrossed edges!

Wait, this changes everything. Let me re-examine.

So in this configuration, the uncrossed edges are all edges except those that are crossed by some other edge. BP is crossed by CQ. Is CQ crossed by BP? Yes (crossing is symmetric). So both BP and CQ are crossed edges.

Are there other crossed edges? Let me check if CQ crosses any other triangulation edge.
- AQ: from (0,0) to (6,1). CQ from (5,10) to (6,1). Shared endpoint Q. No crossing.
- BQ: from (10,0) to (6,1). CQ from (5,10) to (6,1). Shared endpoint Q. No crossing.
- PQ: from (4,5) to (6,1). CQ from (5,10) to (6,1). Shared endpoint Q. No crossing.
- CP: from (5,10) to (4,5). CQ from (5,10) to (6,1). Shared endpoint C. No crossing.

So CQ only crosses BP. And BP only crosses CQ. So the uncrossed edges are: AB, BC, CA, AP, CP, AQ, BQ, PQ, CQ — wait, CQ is crossed by BP, so CQ is not uncrossed. And BP is crossed by CQ, so BP is not uncrossed.

Uncrossed edges: AB, BC, CA, AP, CP, AQ, BQ, PQ = 8. Plus... let me recount. Total edges: AB, AC, AP, AQ, BC, BP, BQ, CP, CQ, PQ = 10. Crossed: BP (crossed by CQ), CQ (crossed by BP). Uncrossed: AB, AC, AP, AQ, BC, BQ, CP, PQ = 8.

So we get 8 uncrossed edges, not 9. The triangulation had 9 edges but one of them (BP) is crossed.

So the maximum is NOT simply 3n-6. We need to think more carefully.

Hmm wait, but maybe with a different configuration we can achieve 3n-6? Or maybe the answer is different.

Let me reconsider. The set of uncrossed edges forms a planar graph (no two uncrossed edges cross each other). So the maximum is at most 3n-6. But can we always achieve 3n-6?

For n=4 with one interior point (h=3): all 6 edges are uncrossed, and 6 = 3(4)-6. ✓

For n=5: can we achieve 9? We need a configuration where all 9 triangulation edges are uncrossed, meaning no non-triangulation edge crosses any triangulation edge. But with n=5 and h=3, there are $\binom{5}{2} - 9 = 1$ non-triangulation edge. We need that one edge to not cross any triangulation edge.

In my example, the non-triangulation edge CQ crossed BP. Can we choose the configuration so that the single non-triangulation edge doesn't cross any triangulation edge?

The non-triangulation edge connects two non-adjacent vertices in the triangulation. In a triangulation with h=3 and n=5, there are 2 interior points. The non-triangulation edge could be between the two interior points (if they're not connected in the triangulation — but in a triangulation, if both are interior, they might or might not be connected).

Wait, in my triangulation, P and Q ARE connected (PQ is an edge). The non-triangulation edge was CQ. Let me think about which pairs are not in the triangulation.

In my example, the triangulation edges were: AB, BC, CA, AP, BP, CP, AQ, BQ, PQ. The missing edge is CQ. C is a hull vertex and Q is an interior point. They're not connected in the triangulation because Q is inside triangle ABP (not adjacent to C in the triangulation).

For CQ to not cross any triangulation edge, we need C and Q to "see" each other (the segment CQ doesn't cross any triangulation edge). This happens if CQ is itself a triangulation edge, or if it can be added as an edge without crossing.

Actually, the uncrossed edges are exactly those edges that can be added to the "crossing-free graph" — they're the edges of the complete graph that don't cross any other edge of the complete graph.

Let me reconsider the problem. The uncrossed edges of the complete geometric graph are exactly the edges that appear in EVERY triangulation? No, that's not right either.

Actually, an edge of the complete geometric graph is uncrossed if and only if it doesn't cross any other edge. The set of uncrossed edges is a planar graph. Moreover, it's a subgraph of every triangulation? No...

Let me think about it differently. An edge e = (a,b) is uncrossed if and only if the segment ab doesn't contain any point of S in its interior AND doesn't cross any other segment cd where c,d ∈ S.

Wait, actually, an edge (a,b) is uncrossed if no other edge (c,d) crosses it. Two segments cross if they share a point in their interiors. So (a,b) is uncrossed if for every other pair (c,d), the segments ab and cd don't cross (they may share endpoints).

This is equivalent to: the segment ab is an edge of the convex hull of S, OR ab is a segment that doesn't cross any other segment between points of S.

The set of uncrossed edges is known as the "empty edges" or rather, it's the set of edges in the "crossing-free" graph. Actually, I think the uncrossed edges are exactly the edges that are in some triangulation... no, that's not right.

Let me think about it from the perspective of the Delaunay triangulation or just any triangulation. An edge (a,b) is uncrossed iff it's in every triangulation? No. An edge is in every triangulation iff it's a hull edge or it's a "necessary" edge (an edge that separates two points that can only be connected through it). 

Actually, I think the correct characterization is: an edge (a,b) is uncrossed if and only if it is an edge of the convex hull, or the segment ab has the property that no other segment between points of S crosses it. This is equivalent to saying that (a,b) is an edge of some triangulation of S... no, that's not right either, because in my example, BP was a triangulation edge but was crossed by CQ.

Wait, I think I made an error. Let me recheck whether BP and CQ actually cross.

B=(10,0), P=(4,5), C=(5,10), Q=(6,1).

BP: from (10,0) to (4,5). CQ: from (5,10) to (6,1).

BP parametrically: (10-6t, 5t) for t∈[0,1].
CQ parametrically: (5+s, 10-9s) for s∈[0,1].

10-6t = 5+s → s = 5-6t
5t = 10-9s = 10-9(5-6t) = 10-45+54t = -35+54t
5t = -35+54t → 35 = 49t → t = 5/7
s = 5-6(5/7) = 5-30/7 = (35-30)/7 = 5/7

Both t=5/7 and s=5/7 are in (0,1). So yes, BP and CQ cross. My calculation was correct.

So the triangulation edge BP is crossed by the non-triangulation edge CQ. This means not all triangulation edges are uncrossed.

So the answer is NOT simply 3n-6. Let me reconsider the problem.

Hmm, but wait. Maybe with a better choice of point configuration, we can avoid this. The question asks for the MAXIMUM over all configurations. So maybe for some special configuration, all edges are uncrossed?

For n=4 with h=3 (triangle + 1 interior point), all 6 edges are uncrossed. 6 = 3(4)-6.

For n=5, can we find a configuration where all 10 edges are uncrossed? That would require the complete graph K5 to be planar, which is impossible. So the maximum is at most 3(5)-6 = 9.

Can we achieve 9 for n=5? We need 9 uncrossed edges. The uncrossed edges form a planar graph, so 9 is the max for a triangulation. We need a configuration where the uncrossed edges form a triangulation (9 edges with h=3).

For this, we need a configuration where exactly 1 edge is crossed (the 10th edge), and that crossed edge crosses exactly one other edge (which would also be crossed). Wait, if edge X crosses edge Y, then both X and Y are crossed. So at least 2 edges are crossed, giving at most 8 uncrossed edges.

Hmm wait, that's a key observation! If two edges cross, BOTH are "crossed" (each crosses the other). So the number of crossed edges is always even (at least 2). So for n=5, we can have at most 10 - 2 = 8 uncrossed edges.

But wait, can we have a configuration where NO edges cross? That requires all $\binom{n}{2}$ edges to be uncrossed, which means the complete geometric graph is planar. For n ≥ 5, K_n is not planar, so this is impossible. For n=4, K4 is planar, and with h=3 (one interior point), all 6 edges are uncrossed. For n=5, K5 is not planar, so at least one pair of edges must cross, meaning at least 2 edges are crossed, giving at most 8 uncrossed.

But can we achieve 8 for n=5? In my example, I got exactly 8. Let me verify: uncrossed edges were AB, AC, AP, AQ, BC, BQ, CP, PQ = 8. Yes!

But wait, can we do better with a different configuration? What if we have h=5 (all points in convex position)? Then the uncrossed edges are the 5 hull edges (the diagonals all cross each other). So 5 uncrossed edges. Worse.

What about h=4? Four hull vertices and one interior point. The hull edges (4) are uncrossed. The edges from interior to hull (4) are uncrossed (they don't cross each other since they share the interior point, and they don't cross hull edges since the interior point is inside). The diagonals of the quadrilateral (2) cross each other, so both are crossed. The edges from interior point to hull vertices: 4 edges, all uncrossed. Total uncrossed: 4 (hull) + 4 (interior to hull) = 8. Same as h=3 case.

Actually wait, with h=4 and 1 interior point, total edges = $\binom{5}{2} = 10$. Hull edges: 4. Diagonals: 2 (these cross each other). Edges from interior to hull: 4. Do any of the interior-to-hull edges cross any hull edge? No, because the interior point is inside the convex hull, so segments from it to hull vertices stay inside. Do any interior-to-hull edges cross each other? No, they all share the interior point. Do any interior-to-hull edges cross the diagonals? Possibly! 

If the interior point is at the center of the quadrilateral, the diagonals pass through the center. The edges from the interior point to the hull vertices would overlap with parts of the diagonals but not cross them (they share the interior point). Actually, if the interior point is exactly at the intersection of the diagonals, then the edges from the interior point to opposite vertices are sub-segments of the diagonals, so they don't "cross" the diagonals (they're collinear and share a point). But if the interior point is not at the center, the edges from it to the vertices might cross the diagonals.

Let me be more careful. Take a convex quadrilateral ABCD and an interior point P. The diagonals AC and BD cross each other. Now, does edge AP cross diagonal BD? If P is close to A, probably not. If P is near the center, AP might cross BD.

Actually, AP goes from A to P (both inside or on the hull). BD goes from B to D. AP crosses BD if and only if A and P are on opposite sides of line BD. Since P is inside the quadrilateral, P is on the same side of BD as... well, it depends. In a convex quadrilateral ABCD (in order), the diagonal BD separates A and C. So A is on one side of BD and C is on the other. P is inside the quadrilateral, so P could be on either side of BD.

If P is on the same side as A (i.e., in triangle ABD), then AP doesn't cross BD. If P is on the same side as C (in triangle BCD), then AP crosses BD.

So to maximize uncrossed edges with h=4, we should place P in a position where the edges from P to the hull vertices don't cross the diagonals. If P is in triangle ABD (say), then:
- AP: doesn't cross BD (A and P on same side). Does AP cross AC? A is shared, so no. Does AP cross BC? No (AP is inside triangle ABD, BC is outside). Does AP cross CD? No. So AP is uncrossed.
- BP: doesn't cross AC (B and P... B is on line BD, hmm). Actually B is a vertex of the quadrilateral. BP goes from B to P. Does BP cross AC? B and P: B is on one side of AC (in a convex quad ABCD, diagonal AC separates B and D). P is in triangle ABD, so P is on the same side as B (and D). So BP doesn't cross AC. Does BP cross BD? B is shared. So BP is uncrossed.
- DP: similarly uncrossed.
- CP: C and P are on opposite sides of BD (C is on the C-side, P is on the A-side). So CP crosses BD! So CP is crossed, and BD is crossed (by both AC and CP).

So with P in triangle ABD: uncrossed edges are AB, BC, CD, DA (hull), AP, BP, DP (interior to hull, not crossing anything) = 7. Crossed: AC (crosses BD), BD (crosses AC and CP), CP (crosses BD). That's 3 crossed edges, 7 uncrossed.

Hmm, that's worse than the h=3 case (8 uncrossed). Let me recheck the h=3 case.

With h=3 (triangle ABC, interior points P, Q), I found 8 uncrossed edges. Let me see if we can do better.

Actually, let me reconsider. Maybe we can choose the positions of P and Q more carefully to avoid the crossing.

In my example, the issue was that CQ crossed BP. Can we choose P and Q so that no non-triangulation edge crosses any triangulation edge?

With n=5, h=3, the triangulation has 9 edges and there's 1 non-triangulation edge. If that 1 non-triangulation edge doesn't cross any triangulation edge, then all 10 edges are uncrossed, but that's impossible (K5 is not planar). So the non-triangulation edge MUST cross at least one triangulation edge, meaning at least 2 edges are crossed, giving at most 8.

Wait, but the non-triangulation edge might cross a triangulation edge, making both crossed. So at least 2 edges are crossed, giving at most 8. And I showed 8 is achievable. So for n=5, the answer is 8.

Hmm, but 8 = 3(5) - 7. Let me check n=4: 6 = 3(4) - 6. n=5: 8 = 3(5) - 7.

Let me think about n=6. With h=3, triangulation has 3(6)-6 = 12 edges. Total edges = $\binom{6}{2} = 15$. Non-triangulation edges: 3. Each non-triangulation edge, if it crosses a triangulation edge, makes 2 edges crossed. But multiple non-triangulation edges might cross the same triangulation edge, and non-triangulation edges might cross each other.

This is getting complicated. Let me think about the problem differently.

The uncrossed edges form a planar graph. The question is: what is the maximum number of edges in this planar graph, over all configurations of n points?

The uncrossed edges are exactly the edges (a,b) such that segment ab doesn't cross any other segment cd (c,d ∈ S, {c,d} ≠ {a,b}).

Key insight: The uncrossed edges are exactly the edges of the convex hull layers' triangulation... no.

Actually, I think the uncrossed edges are exactly the edges that are in EVERY triangulation of the point set. Wait, no. An edge in every triangulation is called a "mandatory" edge. Hull edges are mandatory. But there can be other mandatory edges.

Hmm, actually, I don't think uncrossed edges = mandatory edges. Let me think again.

An edge (a,b) is uncrossed if no other edge crosses it. An edge (a,b) is in every triangulation if it's a hull edge or if it's forced (e.g., it separates two subsets that can't be triangulated without it).

Actually, I think these are the same! An edge (a,b) is uncrossed if and only if it's in every triangulation.

Proof: 
(⟸) If (a,b) is in every triangulation, then (a,b) is uncrossed. Because if some edge (c,d) crosses (a,b), then in any triangulation, (a,b) is present, and (c,d) cannot be present (since triangulation edges don't cross). But we can always find a triangulation containing (c,d) (any edge can be extended to a triangulation). This triangulation doesn't contain (a,b) (since (c,d) crosses (a,b)), contradicting that (a,b) is in every triangulation.

(⟹) If (a,b) is uncrossed, then (a,b) is in every triangulation. Suppose not: there's a triangulation T not containing (a,b). Since (a,b) is uncrossed, it doesn't cross any edge. So we can add (a,b) to T without creating any crossing. But T is a triangulation (maximal planar straight-line graph), so adding any edge creates a crossing. Contradiction.

Wait, is a triangulation a maximal planar straight-line graph? Yes! A triangulation of a point set is a maximal set of non-crossing edges. So if (a,b) is uncrossed (doesn't cross any edge of T), we can add it to T, contradicting maximality.

So uncrossed edges = edges in every triangulation = mandatory edges.

Now, the question becomes: what is the maximum number of mandatory edges over all configurations of n points?

The mandatory edges include all hull edges. For h hull vertices, that's h edges. Additionally, there can be interior mandatory edges.

When does an interior edge become mandatory? An edge (a,b) is mandatory if every triangulation must include it. This happens when (a,b) is the only way to "connect" two parts of the point set, i.e., when removing (a,b) from the triangulation would leave a non-triangular face that can't be triangulated without (a,b).

Actually, an edge (a,b) is mandatory if and only if there's no other edge that can "replace" it, i.e., the edge (a,b) is the only edge connecting the two sides. More precisely, (a,b) is mandatory iff the segment ab has points of S on both sides, and there's no other pair (c,d) with c on one side and d on the other such that cd doesn't cross ab. But since (a,b) is uncrossed, no edge crosses it, so... hmm, this is circular.

Let me think about it differently. An edge (a,b) is mandatory (uncrossed) if and only if:
1. It's a hull edge, OR
2. It's an interior edge such that the segment ab is not crossed by any other segment between points of S.

For condition 2, the segment ab is crossed by some segment cd iff c and d are on opposite sides of line ab AND the segments actually intersect (not just the lines). 

An interior edge (a,b) is uncrossed iff no segment cd (with c,d ∈ S \ {a,b}) crosses segment ab. This means: for every pair (c,d) with c on one side of line ab and d on the other, the segment cd does not intersect segment ab.

This is a strong condition. It means that the segment ab acts as a "separator" — all points on one side can only reach the other side through a or b.

Now, to maximize the number of uncrossed (mandatory) edges, we want to maximize the number of mandatory edges. 

Let me think about what configuration maximizes mandatory edges.

For n=4, h=3: 6 mandatory edges (all edges). 
For n=4, h=4: 4 mandatory edges (hull edges only, diagonals cross).
For n=5, h=3: we showed 8 mandatory edges.
For n=5, h=4: let me think... 4 hull + some interior. With 1 interior point in a quadrilateral, the interior point connects to 4 hull vertices. But as I showed, one of those connections might cross a diagonal. If the interior point is in a position where all 4 connections are uncrossed, we'd have 4 + 4 = 8. But can all 4 be uncrossed? The interior point P, edge CP crosses BD (as I showed). So at most 3 of the 4 interior-to-hull edges are uncrossed, giving 4 + 3 = 7. Plus, are there any other uncrossed edges? The diagonals are crossed. So 7.

Hmm, but what if P is at a special position? If P is at the intersection of the diagonals, then AP, BP, CP, DP are all sub-segments of the diagonals. They don't "cross" the diagonals (they're collinear). But are they uncrossed? AP is part of diagonal AC. Does AP cross BD? AP is from A to P (the center), and BD goes from B to D through P. They share point P. If P is in the interior of both segments, then AP and BD share an interior point, which counts as crossing! So AP is crossed by BD.

So with P at the center, all 4 interior-to-hull edges are crossed (each crosses one of the diagonals). Plus the 2 diagonals cross each other. So crossed edges: AC, BD, AP, BP, CP, DP = 6. Uncrossed: 4 hull edges. That's terrible.

OK so h=4 is worse than h=3 for n=5. Let me focus on h=3.

For n=5, h=3, I got 8. Is 8 optimal? We showed at least 2 edges must be crossed (since K5 is not planar, at least one crossing exists, and each crossing makes 2 edges crossed). So max uncrossed = 10 - 2 = 8. And 8 is achievable. So for n=5, the answer is 8.

Now let me think about the general pattern.

For n=4: 6 = 3(4) - 6
For n=5: 8 = 3(5) - 7

Let me think about n=6. With h=3, triangulation has 12 edges, total edges = 15, non-triangulation = 3. Each crossing makes 2 edges crossed. But crossings can share edges.

The minimum number of crossings in a complete geometric graph on n points is related to the rectilinear crossing number. But we're not asking about crossings — we're asking about the number of edges that participate in at least one crossing.

An edge is "crossed" if it participates in at least one crossing. We want to minimize the number of crossed edges, or equivalently maximize the number of uncrossed edges.

The uncrossed edges form a planar graph (maximal planar subgraph that's in every triangulation). Actually, the uncrossed edges are the mandatory edges, which form a subgraph of every triangulation.

Hmm, let me think about this differently. The uncrossed edges form a planar graph G. G is a subgraph of every triangulation. The number of edges in G is what we want to maximize.

Since G is planar, |E(G)| ≤ 3n - 6. But G must also be a subgraph of every triangulation, which is a strong constraint.

Actually, G doesn't have to be a triangulation. G is just the set of mandatory edges. The question is: what's the maximum number of mandatory edges?

Let me think about when an edge is mandatory. An edge (a,b) is mandatory iff it's in every triangulation. For a point set with h hull vertices, all h hull edges are mandatory. Interior edges are mandatory only in special configurations.

When is an interior edge mandatory? An interior edge (a,b) is mandatory iff every triangulation includes it. This happens iff there's no triangulation that excludes it, which happens iff (a,b) cannot be "replaced" by a flipping edge. In a triangulation, an interior edge (a,b) shared by triangles (a,b,c) and (a,b,d) can be flipped to (c,d) if (c,d) doesn't cross any other edge. If the flip is always possible (i.e., (c,d) is a valid edge), then (a,b) is not mandatory.

An edge (a,b) is mandatory iff for every pair of triangles (a,b,c) and (a,b,d) sharing it, the flip edge (c,d) would cross some existing edge, OR the quadrilateral acbd is not convex (so the flip is not valid).

Actually, more precisely: (a,b) is mandatory iff it's in every triangulation. An edge can be removed from a triangulation only by flipping. But an edge might be in all triangulations even if individual flips are possible, because flipping might lead to a configuration where the edge must be added back.

This is getting complicated. Let me think about the problem from a different angle.

Let me consider the "onion" structure. The convex hull layers (onion peeling). The outermost layer is the convex hull. Remove it, and the next layer is the convex hull of the remaining points, etc.

For points in convex position (all on one layer), the mandatory edges are just the hull edges: n edges. But we can do better with interior points.

Let me think about the problem for small n and try to find a pattern.

n=4, h=3: 6 uncrossed edges (all edges). The interior point is connected to all 3 hull vertices, and all 3 hull edges. Total 6.
n=4, h=4: 4 uncrossed edges (hull only).
So max for n=4 is 6.

n=5, h=3: 8 uncrossed edges.
n=5, h=4: 7 uncrossed edges.
n=5, h=5: 5 uncrossed edges.
So max for n=5 is 8.

n=6, h=3: Let me think. 3 hull vertices, 3 interior points. Triangulation has 12 edges. Total edges = 15. How many can be uncrossed?

With 3 interior points, we need to arrange them so that as many edges as possible are mandatory.

Let me think about a specific configuration. Hull: equilateral triangle A, B, C. Interior: 3 points P, Q, R arranged in a small triangle near the center.

If P, Q, R are very close to the center and form a small triangle, the triangulation would connect them to each other and to the hull vertices. The triangulation would look like: hull edges (3) + edges from each interior point to nearby hull vertices + edges among interior points.

The non-triangulation edges would be edges from interior points to "far" hull vertices. These might cross edges from other interior points to "near" hull vertices.

This is getting complicated. Let me try to think about the problem more abstractly.

Key observation: The uncrossed edges form a planar graph that is a subgraph of every triangulation. This planar graph is the "common refinement" of all triangulations, sometimes called the "core" of the point set.

The number of edges in the core depends on the point configuration. We want to maximize it.

For h=3 (triangular hull), the core includes the 3 hull edges. Interior edges are in the core iff they're mandatory.

Let me think about when an interior edge is mandatory with h=3. An interior edge (a,b) is mandatory iff it's in every triangulation. 

Consider the simplest case: n points with h=3, and the interior points are in "convex position" (forming a convex polygon inside the triangle). Then the triangulation of the interior points can vary, and many edges are not mandatory.

But if the interior points are in a "nested" configuration (each inside the triangle formed by the previous), then more edges become mandatory.

Actually, let me think about a "nested" configuration: hull triangle A, B, C. Point P1 inside ABC. Point P2 inside ABP1 (or some triangle involving P1). Point P3 inside a triangle involving P1, P2. Etc.

In a nested configuration, each new point is inside a triangle of the previous triangulation, so it connects to the 3 vertices of that triangle. These 3 edges are mandatory (they're the only way to connect the new point to the rest).

Wait, are they mandatory? If P2 is inside triangle ABP1, then edges AP2, BP2, P1P2 are added. Are these mandatory? 

Edge AP2: is it in every triangulation? P2 is inside triangle ABP1. In any triangulation, P2 must be connected to some vertices. The triangle ABP1 must be subdivided to include P2. The possible subdivisions: connect P2 to all 3 vertices of ABP1 (giving AP2, BP2, P1P2), or... actually, there's only one way to triangulate a triangle with one interior point: connect it to all 3 vertices. So AP2, BP2, P1P2 are all mandatory. ✓

So in a nested configuration, each new point adds 3 mandatory edges. Starting with the hull triangle (3 edges) and the first interior point (3 edges), each subsequent point adds 3 edges.

For n points with h=3: 3 (hull) + 3(n-3) (interior) = 3n - 6.

Wait, that gives 3n - 6! But we showed that for n=5, the maximum is 8 = 3(5) - 7, not 9 = 3(5) - 6.

Let me recheck. For n=5, h=3, nested configuration: hull ABC, P1 inside ABC, P2 inside triangle ABP1 (say).

Mandatory edges: AB, BC, CA (hull) + AP1, BP1, CP1 (P1 inside ABC) + AP2, BP2, P1P2 (P2 inside ABP1) = 9 edges.

But we showed that at least 2 edges must be crossed (K5 is not planar). So at most 8 edges can be uncrossed. Contradiction!

So some of these 9 "mandatory" edges must actually be crossed. Let me check.

The 9 edges are: AB, BC, CA, AP1, BP1, CP1, AP2, BP2, P1P2.
The 1 non-triangulation edge: CP2 (assuming the triangulation doesn't include it).

Wait, total edges = $\binom{5}{2} = 10$. The triangulation has 9 edges. The missing edge is CP2 (C is not adjacent to P2 in this triangulation, since P2 is inside triangle ABP1, not involving C).

Does CP2 cross any triangulation edge? CP2 goes from C to P2. P2 is inside triangle ABP1. The segment CP2 must cross the boundary of triangle ABP1 to reach P2. The boundary consists of edges AB, AP1, BP1. 

CP2 crosses AB? C is outside triangle ABP1 (on the far side of AB from P1). P2 is inside. So CP2 crosses AB? Wait, C is a hull vertex. Is C on the opposite side of line AB from P1? P1 is inside triangle ABC, so P1 is on the same side of AB as C. So C and P1 are on the same side of AB. P2 is inside triangle ABP1, so P2 is also on the same side of AB as C. So CP2 doesn't cross AB.

CP2 crosses AP1? C and P2: are they on opposite sides of line AP1? A=(0,0), P1=(3,3) (let's say). Line AP1: y = x. C=(5,10) (say). C is above the line (y > x: 10 > 5). P2 is inside triangle ABP1 where A=(0,0), B=(10,0), P1=(3,3). P2 is below line AP1 (y < x) if it's on the B-side. Let's say P2=(5,1). y=1 < x=5, so P2 is below. C is above. So CP2 crosses line AP1. Does it cross segment AP1?

CP2: from C=(5,10) to P2=(5,1). This is a vertical segment x=5, y from 1 to 10.
AP1: from A=(0,0) to P1=(3,3). Parametrically (3t, 3t). At x=5: 3t=5, t=5/3 > 1. So AP1 doesn't reach x=5. So CP2 doesn't cross AP1.

Hmm, let me use specific coordinates. A=(0,0), B=(10,0), C=(5,10). P1=(3,3). P2 inside triangle ABP1, say P2=(4,1).

CP2: from C=(5,10) to P2=(4,1). 
AP1: from A=(0,0) to P1=(3,3). Parametrically (3t, 3t).
CP2: parametrically (5-t, 10-9t) for t∈[0,1] (from C to P2, direction (-1,-9)).
3s = 5-t, 3s = 10-9t. So 5-t = 10-9t → 8t = 5 → t = 5/8. s = (5-5/8)/3 = (35/8)/3 = 35/24 > 1. So s > 1, CP2 doesn't cross AP1.

CP2 crosses BP1? B=(10,0), P1=(3,3). BP1: parametrically (10-7s, 3s).
CP2: (5-t, 10-9t).
10-7s = 5-t, 3s = 10-9t.
t = 5-7s+5 = 10-7s... wait: 10-7s = 5-t → t = 5-10+7s = -5+7s.
3s = 10-9(-5+7s) = 10+45-63s = 55-63s.
66s = 55, s = 55/66 = 5/6. t = -5+7(5/6) = -5+35/6 = (-30+35)/6 = 5/6.
Both in (0,1). So CP2 crosses BP1!

So CP2 crosses BP1. This means BP1 is crossed (not uncrossed), and CP2 is crossed. So the mandatory edges are not all 9; BP1 is crossed.

But wait, I claimed BP1 is mandatory because P1 is inside triangle ABC and must be connected to all 3 vertices. But that's the only triangulation of ABC with P1 inside. However, when we add P2 inside triangle ABP1, the overall triangulation changes. The edge BP1 is still in the triangulation (it's needed to separate triangle BCP1 from triangle ABP1, which is now split). But the edge BP1 is crossed by CP2, which is not in the triangulation.

So BP1 is in this particular triangulation but is crossed by a non-triangulation edge. This means BP1 is NOT mandatory (not in every triangulation), because there exists a triangulation that includes CP2 instead of BP1 (by flipping).

Wait, can we flip BP1? BP1 is shared by triangles BCP1 and BP1P2 (or ABP2, depending on the triangulation). Let me think about the full triangulation.

Triangulation: ABC split by P1 into ABP1, BCP1, CAP1. Then ABP1 split by P2 into ABP2, BP1P2, AP1P2.

So the triangles are: BCP1, CAP1, ABP2, BP1P2, AP1P2.
Edges: AB, BC, CA, AP1, BP1, CP1, AP2, BP2, P1P2.

Edge BP1 is shared by triangles BCP1 and BP1P2. The flip edge would be CP2. If CP2 doesn't cross any other edge, the flip is valid, and BP1 is not mandatory.

We showed CP2 crosses BP1. But for the flip, we need CP2 to not cross any OTHER edge (besides BP1, which is being removed). Let me check: does CP2 cross any edge other than BP1?

CP2 from C=(5,10) to P2=(4,1). Check against:
- AB: y=0, CP2 goes from y=10 to y=1, doesn't reach y=0. No.
- BC: shared endpoint C. No.
- CA: shared endpoint C. No.
- AP1: we showed no crossing.
- CP1: shared endpoint C. No.
- AP2: from A=(0,0) to P2=(4,1). CP2 from C=(5,10) to P2=(4,1). Shared endpoint P2. No.
- BP2: from B=(10,0) to P2=(4,1). CP2 from C=(5,10) to P2=(4,1). Shared endpoint P2. No.
- P1P2: from P1=(3,3) to P2=(4,1). CP2 from C=(5,10) to P2=(4,1). Shared endpoint P2. No.

So CP2 only crosses BP1. The flip is valid! So we can flip BP1 to CP2, getting a different triangulation. This means BP1 is NOT mandatory.

So in this nested configuration, BP1 is not mandatory. The mandatory edges are: AB, BC, CA, AP1, CP1, AP2, BP2, P1P2 = 8. (BP1 is not mandatory because it can be flipped to CP2.)

Hmm, so we get 8 again. Same as before.

Can we do better? What if we choose the positions more carefully so that BP1 cannot be flipped?

BP1 can be flipped iff CP2 doesn't cross any other edge (besides BP1). If we place P2 such that CP2 crosses some other edge, then the flip is invalid and BP1 is mandatory.

But if CP2 crosses some other edge, then that other edge is also crossed, so it's not uncrossed either. So we'd be trading one crossed edge for another.

Let me think about this more carefully. We want to maximize uncrossed edges. Each crossing makes 2 edges crossed. We want to minimize the number of edges that participate in crossings.

The minimum number of edges that participate in crossings is related to the minimum number of crossings in the complete geometric graph, but it's not the same — one edge can participate in multiple crossings, and we want to minimize the number of DISTINCT edges that participate in at least one crossing.

For n=4, h=3: 0 crossings, 0 crossed edges, 6 uncrossed.
For n=5: at least 1 crossing (K5 not planar), so at least 2 crossed edges, at most 8 uncrossed. Achievable: 8.

For n=6: K6 is not planar. The minimum number of crossings in a rectilinear drawing of K6 is... the rectilinear crossing number of K6 is 3 (I think). But we want the minimum number of EDGES that participate in crossings.

Hmm, actually, I realize this might be a well-known competition problem. Let me think about what the answer should be.

The answer to this problem is $3n - 6$ for $n \geq 4$... no, we showed it's not achievable for n=5.

Wait, let me reconsider. For n=4, the answer is 6 = 3(4) - 6. For n=5, the answer is 8. Let me check: is 8 = 3(5) - 7? Yes. 

Hmm, let me reconsider whether the answer might be $\binom{n}{2} - \binom{n-3}{2}$ or something like that.

$\binom{4}{2} - \binom{1}{2} = 6 - 0 = 6$. ✓
$\binom{5}{2} - \binom{2}{2} = 10 - 1 = 9$. ✗ (should be 8)

How about $3n - 6 - (n - 4) = 2n - 2$?
n=4: 6. ✓
n=5: 8. ✓
n=6: 10. 

Or $3n - 6 - \binom{n-3}{2} + \binom{n-4}{2}$... this is getting complicated.

Let me think about it differently. With h=3 (triangular hull), the n-3 interior points form a set inside the triangle. The uncrossed edges include the 3 hull edges plus the mandatory interior edges.

Each interior point must be connected to at least 3 other points in any triangulation (since it's an interior vertex of a triangulation, it has degree ≥ 3). But the edges connecting it might not all be mandatory.

In the nested configuration, each new point adds 3 edges, but one of them might be flippable. So each new point after the first adds 2 mandatory edges (3 added, 1 flippable). First interior point: 3 mandatory (no flip possible since it's the only interior point). Hull: 3 mandatory.

Total: 3 + 3 + 2(n-4) = 2n - 2 for n ≥ 4.

n=4: 2(4)-2 = 6. ✓
n=5: 2(5)-2 = 8. ✓
n=6: 2(6)-2 = 10.

But is this actually achievable? And is it the maximum? Let me think about whether we can do better than the nested configuration.

Actually, let me reconsider. In the nested configuration, is it always exactly 1 flippable edge per new point? Or could it be 0 or 2?

When we add P_k inside a triangle T = (a, b, c) of the current triangulation, we add edges P_ka, P_kb, P_kc. Each of these edges is shared by two triangles. For each, the flip might or might not be valid.

Edge P_ka is shared by triangles P_kab and P_kac (or some other pairing). The flip edge would be bc, but bc is already in the triangulation (it's an edge of T). Wait, no. Let me think again.

If P_k is inside triangle (a,b,c), the three new triangles are (a,b,P_k), (b,c,P_k), (c,a,P_k). Edge aP_k is shared by triangles (a,b,P_k) and (c,a,P_k). The flip edge is bc. But bc is already an edge of the triangulation (it's an edge of the original triangle T). So the flip would create a duplicate edge, which is invalid. So edge aP_k is NOT flippable!

Wait, that means all 3 edges added for each new point are mandatory? But we showed that for n=5, BP1 is flippable (to CP2). Let me reconcile.

When P2 is added inside triangle ABP1, the three new triangles are (A,B,P2), (B,P1,P2), (P1,A,P2). Edge BP2 is shared by triangles (A,B,P2) and (B,P1,P2). The flip edge is AP1. But AP1 is already in the triangulation! So BP2 is not flippable.

Edge AP2 is shared by triangles (A,B,P2) and (P1,A,P2). The flip edge is BP1. BP1 is already in the triangulation. So AP2 is not flippable.

Edge P1P2 is shared by triangles (B,P1,P2) and (P1,A,P2). The flip edge is AB. AB is already in the triangulation. So P1P2 is not flippable.

So none of the 3 new edges are flippable by a simple flip! But we showed that BP1 CAN be flipped to CP2. BP1 is not one of the new edges — it's an old edge that became shared by different triangles after the insertion.

So the issue is: when we add P2 inside triangle ABP1, the edge BP1 (which was previously shared by triangles ABP1 and BCP1) is now shared by triangles BP1P2 and BCP1. The flip edge is CP2. If CP2 doesn't cross any other edge, the flip is valid.

So the new edges (AP2, BP2, P1P2) are all mandatory (not flippable), but an old edge (BP1) becomes flippable.

So for each new point added inside a triangle, 3 new mandatory edges are added, but 1 old edge might become flippable (losing 1 mandatory edge). Net gain: 2 mandatory edges per new point.

But does the old edge always become flippable? It depends on whether the flip edge crosses any other edge. If we can arrange the points so that the flip edge always crosses some other edge, the old edge remains mandatory, and we gain 3 per new point.

But if the flip edge crosses another edge, that other edge is also crossed, so it's not uncrossed. We'd be trading one non-uncrossed edge for another.

Hmm, this is a zero-sum game. Let me think about it more carefully.

When we flip BP1 to CP2:
- If the flip is valid (CP2 doesn't cross any other edge): BP1 is not mandatory. But CP2 is now in the new triangulation. Is CP2 mandatory? In the new triangulation, CP2 is shared by triangles CP2B and CP2P1 (or similar). Its flip edge is BP1. If BP1 doesn't cross any other edge in the new triangulation, then CP2 is also not mandatory. So both BP1 and CP2 are non-mandatory, and both are uncrossed (since neither crosses any edge in their respective triangulations... wait, no).

Actually, let me reconsider. BP1 is uncrossed iff it doesn't cross any edge of the complete graph. We showed BP1 is crossed by CP2. So BP1 is NOT uncrossed. And CP2 is crossed by BP1, so CP2 is NOT uncrossed either. Both are crossed.

So regardless of the flip, both BP1 and CP2 are crossed edges (they cross each other). The question is whether we can avoid this crossing altogether by choosing a different configuration.

The crossing between BP1 and CP2 exists because of the geometry: C and P2 are on opposite sides of line BP1 (or more precisely, the segments cross). Can we choose P2 so that CP2 doesn't cross BP1?

CP2 crosses BP1 iff C and P2 are on opposite sides of line BP1 AND B and P1 are on opposite sides of line CP2 (both conditions needed for segment crossing).

P2 is inside triangle ABP1. C is outside triangle ABP1 (on the other side of BP1 from A... or from the interior of ABP1). 

Actually, C is a hull vertex, and triangle ABP1 is inside the hull triangle ABC. C is on the opposite side of line BP1 from A (since A and C are on opposite sides of line BP1 in the triangle ABC... not necessarily).

Hmm, let me think about this. In triangle ABC with P1 inside, the line BP1 divides the triangle into two parts. A is on one side and C is on the other (since BP1 goes from B to P1, and P1 is inside ABC, the line BP1 separates A and C).

So C is on the opposite side of line BP1 from A. P2 is inside triangle ABP1, so P2 is on the same side as A. Therefore C and P2 are on opposite sides of line BP1. So the segment CP2 crosses the line BP1.

For the SEGMENTS to cross (not just the lines), we also need B and P1 to be on opposite sides of line CP2, AND the crossing point to be within both segments.

Can we avoid the segment crossing? The crossing point of CP2 with line BP1 might be outside segment BP1. This happens if the crossing point is beyond P1 or beyond B.

If P2 is very close to A, then CP2 ≈ CA, which doesn't cross BP1 (since CA and BP1 share no interior point in a triangle... actually, in triangle ABC, CA and BP1 do cross if P1 is inside! No wait, CA is a side of the triangle and BP1 goes from B to an interior point. CA and BP1: B is on one side of CA, P1 is on the same side (inside the triangle). So BP1 doesn't cross CA. And CP2 ≈ CA, so CP2 doesn't cross BP1.

So if P2 is very close to A, CP2 doesn't cross BP1! Let me verify.

A=(0,0), B=(10,0), C=(5,10), P1=(3,3), P2=(0.1, 0.05) (very close to A, inside triangle ABP1).

Is P2 inside triangle ABP1? A=(0,0), B=(10,0), P1=(3,3). P2=(0.1, 0.05).
Edge AB: y=0. P2: y=0.05 > 0. P1: y=3 > 0. Same side. ✓
Edge BP1: from (10,0) to (3,3). Line: 3(x-10)+7(y-0)=0... direction (-7,3), normal (3,7). Line: 3(x-10)+7y=0 → 3x+7y=30. A: 0 < 30. P2: 0.3+0.35=0.65 < 30. Same side. ✓
Edge P1A: from (3,3) to (0,0). Direction (-3,-3), normal (1,-1). Line: x-y=0. B: 10 > 0. P2: 0.1-0.05=0.05 > 0. Same side. ✓
So P2 is inside ABP1. ✓

CP2: from C=(5,10) to P2=(0.1, 0.05). 
BP1: from B=(10,0) to P1=(3,3).

CP2: parametrically (5-4.9t, 10-9.95t) for t∈[0,1].
BP1: parametrically (10-7s, 3s) for s∈[0,1].

5-4.9t = 10-7s → 7s = 5+4.9t → s = (5+4.9t)/7
10-9.95t = 3s = 3(5+4.9t)/7 = (15+14.7t)/7
7(10-9.95t) = 15+14.7t
70-69.65t = 15+14.7t
55 = 84.35t
t = 55/84.35 ≈ 0.652
s = (5+4.9(0.652))/7 = (5+3.195)/7 = 8.195/7 ≈ 1.171

s > 1! So the crossing point is outside segment BP1 (beyond P1). So CP2 doesn't cross BP1. ✓

So with P2 close to A, CP2 doesn't cross BP1. Does CP2 cross any other triangulation edge?

Triangulation edges: AB, BC, CA, AP1, BP1, CP1, AP2, BP2, P1P2.

CP2 from C=(5,10) to P2=(0.1,0.05). Check against:
- AB: y=0. CP2 goes from y=10 to y=0.05, doesn't reach y=0. No crossing (barely).
- BC: shared C. No.
- CA: shared C. No.
- AP1: from (0,0) to (3,3). CP2 from (5,10) to (0.1,0.05). AP1: (3s, 3s). CP2: (5-4.9t, 10-9.95t). 3s = 5-4.9t, 3s = 10-9.95t. So 5-4.9t = 10-9.95t → 5.05t = 5 → t = 5/5.05 ≈ 0.990. s = (5-4.9(0.990))/3 = (5-4.851)/3 = 0.149/3 ≈ 0.0497. Both in (0,1). So CP2 crosses AP1!

Hmm, so CP2 crosses AP1 instead. So AP1 is crossed, and CP2 is crossed. We still have 2 crossed edges.

Can we avoid this too? If P2 is close to A, CP2 ≈ CA, which doesn't cross AP1 (they share A). But CP2 is not exactly CA; it goes from C to P2 which is near A but not exactly A.

Let me try P2 even closer to A: P2=(0.001, 0.0005).

CP2: from (5,10) to (0.001, 0.0005). AP1: from (0,0) to (3,3).
CP2: (5-4.999t, 10-9.9995t). AP1: (3s, 3s).
3s = 5-4.999t, 3s = 10-9.9995t.
5-4.999t = 10-9.9995t → 5.0005t = 5 → t ≈ 0.99990.
s = (5-4.999(0.99990))/3 ≈ (5-4.9985)/3 ≈ 0.0015/3 ≈ 0.0005.
Both in (0,1). Still crosses!

The issue is that CP2, going from C to a point near A, passes very close to A and crosses AP1 (which emanates from A). As P2 → A, the crossing point approaches A, but it's still a crossing (in the interior of both segments) as long as P2 ≠ A.

Hmm, but if P2 = A, it's not a valid configuration (P2 must be a distinct point). So for any P2 near A inside triangle ABP1, CP2 crosses AP1.

What if P2 is close to B instead? Then CP2 ≈ CB, which doesn't cross AP1 or BP1. Let me check.

P2=(9.9, 0.05) (close to B, inside triangle ABP1).
Is P2 inside ABP1? A=(0,0), B=(10,0), P1=(3,3).
Edge AB: y=0, P2: y=0.05>0. ✓
Edge BP1: 3x+7y=30. P2: 29.7+0.35=30.05 > 30. A: 0 < 30. P2 is on the OPPOSITE side from A. ✗

So P2 is NOT inside ABP1 if it's close to B (it's on the wrong side of BP1). 

What about P2 close to P1? P2=(2.9, 2.9).
Inside ABP1? 
Edge AB: y=0, P2: y=2.9>0. ✓
Edge BP1: 3x+7y=30. P2: 8.7+20.3=29 < 30. Same as A. ✓
Edge P1A: x-y=0. P2: 2.9-2.9=0. On the line! Not strictly inside. Let me use P2=(3.1, 2.8).
Edge P1A: x-y=0. P2: 3.1-2.8=0.3>0. B: 10>0. Same side. ✓
Edge BP1: 3(3.1)+7(2.8)=9.3+19.6=28.9<30. ✓
Inside. ✓

CP2 from C=(5,10) to P2=(3.1,2.8). 
BP1 from B=(10,0) to P1=(3,3).
CP2: (5-1.9t, 10-7.2t). BP1: (10-7s, 3s).
5-1.9t = 10-7s → 7s = 5+1.9t → s = (5+1.9t)/7
10-7.2t = 3s = 3(5+1.9t)/7 = (15+5.7t)/7
7(10-7.2t) = 15+5.7t
70-50.4t = 15+5.7t
55 = 56.1t
t = 55/56.1 ≈ 0.980
s = (5+1.9(0.980))/7 = (5+1.862)/7 = 6.862/7 ≈ 0.980
Both in (0,1). CP2 crosses BP1.

And AP1: from (0,0) to (3,3). CP2: (5-1.9t, 10-7.2t). AP1: (3s,3s).
3s = 5-1.9t, 3s = 10-7.2t. 5-1.9t = 10-7.2t → 5.3t = 5 → t ≈ 0.943. s = (5-1.9(0.943))/3 = (5-1.792)/3 = 3.208/3 ≈ 1.069. s > 1. No crossing with AP1.

So with P2 near P1, CP2 crosses BP1 but not AP1. Still 2 crossed edges.

It seems like no matter where we place P2 inside triangle ABP1, CP2 will cross either BP1 or AP1 (or both). This is because C is outside triangle ABP1, and the segment from C to any interior point of ABP1 must cross the boundary of ABP1. The boundary consists of edges AB, AP1, BP1. We showed it doesn't cross AB (C and P2 on same side). So it must cross AP1 or BP1.

Actually, that's the key insight! C is outside triangle ABP1. P2 is inside. The segment CP2 must cross the boundary of triangle ABP1. The boundary edges are AB, AP1, BP1. Since C and P2 are on the same side of AB (both inside the hull triangle ABC, on the same side as C), CP2 doesn't cross AB. So CP2 must cross AP1 or BP1. Either way, one triangulation edge is crossed.

So for n=5, h=3, we always have at least 2 crossed edges (CP2 and either AP1 or BP1), giving at most 8 uncrossed edges. And 8 is achievable. ✓

Now, for general n with h=3, let me think about the pattern.

With h=3 and k = n-3 interior points, the triangulation has 3n-6 edges. The non-triangulation edges are $\binom{n}{2} - (3n-6) = \binom{n}{2} - 3n + 6$.

For n=4: $\binom{4}{2} - 6 = 0$ non-triangulation edges. 0 crossed, 6 uncrossed.
For n=5: $\binom{5}{2} - 9 = 1$ non-triangulation edge. This edge crosses 1 triangulation edge. 2 crossed, 8 uncrossed.
For n=6: $\binom{6}{2} - 12 = 3$ non-triangulation edges. How many triangulation edges do they cross?

Let me think about n=6, h=3. 3 interior points P1, P2, P3 in a nested configuration.

Hull: ABC. P1 inside ABC. P2 inside triangle ABP1. P3 inside triangle ABP2 (or some other triangle).

Triangulation edges: 3 (hull) + 3 (P1) + 3 (P2) + 3 (P3) = 12. But some old edges might be "consumed" — no, in a triangulation, inserting a point into a triangle replaces 1 triangle with 3, adding 3 edges. Total edges: 3 + 3 + 3 + 3 = 12 = 3(6)-6. ✓

Non-triangulation edges: $\binom{6}{2} - 12 = 15 - 12 = 3$.

Which edges are not in the triangulation? The triangulation edges are: AB, BC, CA, AP1, BP1, CP1, AP2, BP2, P1P2, AP3, BP3, P2P3 (if P3 is inside ABP2).

Non-triangulation edges: CP2, CP3, P1P3. (The edges from C to P2, P3, and from P1 to P3, which are not in the triangulation.)

Wait, let me be more careful. All edges: AB, AC, AP1, AP2, AP3, BC, BP1, BP2, BP3, CA, CP1, CP2, CP3, P1P2, P1P3, P2P3. That's 15.

Triangulation: AB, BC, CA, AP1, BP1, CP1, AP2, BP2, P1P2, AP3, BP3, P2P3 = 12.
Non-triangulation: CP2, CP3, P1P3 = 3.

Now, CP2: from C to P2 (inside triangle ABP1). As before, this crosses either AP1 or BP1.
CP3: from C to P3 (inside triangle ABP2, which is inside ABP1). This must cross the boundary of ABP2, which consists of AB, AP2, BP2. Since C is on the same side of AB as P3, it doesn't cross AB. So it crosses AP2 or BP2.
P1P3: from P1 to P3 (inside triangle ABP2). P1 is outside triangle ABP2 (P1 is a vertex of ABP1, and ABP2 is inside ABP1). The segment P1P3 must cross the boundary of ABP2. The boundary is AB, AP2, BP2. P1 is on the same side of AB as P3 (both inside the hull). So P1P3 crosses AP2 or BP2.

So the crossed edges:
- CP2 crosses AP1 or BP1: 1 triangulation edge + CP2 = 2 crossed.
- CP3 crosses AP2 or BP2: 1 triangulation edge + CP3 = 2 crossed.
- P1P3 crosses AP2 or BP2: 1 triangulation edge + P1P3 = 2 crossed.

But some triangulation edges might be crossed by multiple non-triangulation edges. If CP3 and P1P3 both cross the same edge (say BP2), then BP2 is crossed once, and the crossed edges are: {CP2, AP1 or BP1, CP3, P1P3, BP2} = 5 crossed edges. Uncrossed: 15 - 5 = 10.

If they cross different edges (CP3 crosses AP2, P1P3 crosses BP2), then crossed edges: {CP2, AP1 or BP1, CP3, AP2, P1P3, BP2} = 6 crossed. Uncrossed: 15 - 6 = 9.

So to maximize uncrossed edges, we want the non-triangulation edges to cross the same triangulation edges as much as possible (to minimize the total number of distinct crossed edges).

In the best case: CP2 crosses BP1, CP3 crosses BP2, P1P3 crosses BP2. Crossed: {CP2, BP1, CP3, P1P3, BP2} = 5. Uncrossed: 10.

Or: CP2 crosses BP1, CP3 crosses BP2, P1P3 crosses BP2. Same as above.

Can we get 4 crossed? We'd need all 3 non-triangulation edges to cross the same triangulation edge. But CP2 crosses an edge of triangle ABP1 (AP1 or BP1), while CP3 and P1P3 cross edges of triangle ABP2 (AP2 or BP2). These are different edges. So at least 2 distinct triangulation edges are crossed. Plus the 3 non-triangulation edges. Total: at least 5 crossed. Uncrossed: at most 10.

Can we achieve 10? We need CP2 to cross exactly one of {AP1, BP1}, CP3 and P1P3 to both cross the same one of {AP2, BP2}. Let me try to construct this.

Actually, let me reconsider. Maybe a non-nested configuration does better. Or maybe h > 3 does better for larger n.

Let me step back and think about the problem from a higher level.

The uncrossed edges form a planar graph. We want to maximize the number of edges. The graph is a subgraph of every triangulation (it's the "core" or "common edges" of all triangulations).

For a point set in general position with h hull vertices, the number of triangulations can be huge, and the core can be small. But for special configurations (like nested points), the core can be larger.

I think the answer to this problem is $3n - 6 - \binom{n-3}{2} + \binom{n-3}{2}$... no, let me think about the pattern differently.

n=4: 6 = 6
n=5: 8 = 6 + 2
n=6: 10 = 6 + 4 (if achievable)

Pattern: 6 + 2(n-4) = 2n - 2.

n=4: 2(4)-2 = 6 ✓
n=5: 2(5)-2 = 8 ✓
n=6: 2(6)-2 = 10

Let me check if 2n-2 makes sense. With h=3 and nested configuration:
- 3 hull edges (always uncrossed)
- 3 edges for first interior point (always uncrossed, since no other edges to cross)
- For each subsequent interior point (n-4 of them), 3 new edges added, but 1 old edge becomes crossed. Net: +2 uncrossed edges per new point.

Total: 3 + 3 + 2(n-4) = 2n - 2.

But wait, does each new point cause exactly 1 old edge to become crossed? Or could it cause more?

When we add P_k inside triangle T = (a, b, c) of the current triangulation, the non-triangulation edges from P_k to vertices not in T must cross the boundary of T. Each such non-triangulation edge crosses exactly one edge of T (since it enters T from outside). 

The number of non-triangulation edges from P_k is: P_k is connected to 3 vertices of T in the triangulation. The remaining n - 1 - 3 = n - 4 vertices are not adjacent to P_k in the triangulation. But some of these might be outside the hull (none, since h=3) or inside other triangles.

Hmm, this is getting complicated. Let me think about it differently.

Actually, I think the answer might be $2n - 2$ for $n \geq 4$. Let me try to prove this.

Upper bound: The uncrossed edges form a planar graph. But we need a tighter bound than 3n-6.

Key insight: In the complete geometric graph, the uncrossed edges form a planar graph. Moreover, this planar graph has a specific structure: it's a subgraph of every triangulation. 

Actually, let me think about the problem differently. Let me consider the "crossing graph" — the graph whose vertices are the edges of the complete geometric graph, and two vertices are connected if the corresponding edges cross. The uncrossed edges are the isolated vertices of this crossing graph.

We want to maximize the number of isolated vertices, i.e., minimize the number of non-isolated vertices.

Hmm, this is a complex combinatorial optimization. Let me try a different approach.

Let me think about what the answer should be and try to prove it.

Claim: The maximum number of uncrossed edges is $2n - 2$ for $n \geq 4$.

Wait, actually, I want to double-check with n=6 more carefully. Let me think about whether 10 is achievable and whether we can do better.

With n=6, h=3, nested configuration, I estimated 10 uncrossed edges. Let me verify more carefully.

Hull: A, B, C. P1 inside ABC. P2 inside ABP1. P3 inside ABP2.

Triangulation: AB, BC, CA, AP1, BP1, CP1, AP2, BP2, P1P2, AP3, BP3, P2P3.

Non-triangulation: CP2, CP3, P1P3.

CP2 crosses one of {AP1, BP1} (say BP1).
CP3 crosses one of {AP2, BP2} (say BP2).
P1P3 crosses one of {AP2, BP2} (say BP2).

Crossed edges: CP2, BP1, CP3, BP2, P1P3 = 5.
Uncrossed: 15 - 5 = 10.

But we need to verify that no other crossings exist. Specifically:
- Does CP2 cross any edge other than BP1? We need to check.
- Does CP3 cross any edge other than BP2?
- Does P1P3 cross any edge other than BP2?
- Do the non-triangulation edges cross each other?

This requires careful geometric analysis. Let me use specific coordinates.

A=(0,0), B=(10,0), C=(5,10). P1=(3,3). P2=(4,1). P3=(4.5, 0.5).

Check P2 inside ABP1: Already checked earlier, P2=(4,1) is inside ABP1. ✓
Check P3 inside ABP2: A=(0,0), B=(10,0), P2=(4,1).
Edge AB: y=0, P3: y=0.5>0. ✓
Edge BP2: from (10,0) to (4,1). Direction (-6,1), normal (1,6). Line: (x-10)+6(y-0)=0 → x+6y=10. A: 0<10. P3: 4.5+3=7.5<10. Same side. ✓
Edge P2A: from (4,1) to (0,0). Direction (-4,-1), normal (1,-4). Line: (x-4)-4(y-1)=0 → x-4y=0. B: 10>0. P3: 4.5-2=2.5>0. Same side. ✓
P3 inside ABP2. ✓

Now let me check the crossings.

CP2: from C=(5,10) to P2=(4,1).
BP1: from B=(10,0) to P1=(3,3).
CP2: (5-t, 10-9t). BP1: (10-7s, 3s).
5-t = 10-7s → t = 7s-5.
10-9t = 3s → 10-9(7s-5) = 3s → 10-63s+45 = 3s → 55 = 66s → s = 5/6.
t = 7(5/6)-5 = 35/6-5 = 5/6.
Both in (0,1). CP2 crosses BP1. ✓

CP3: from C=(5,10) to P3=(4.5,0.5).
BP2: from B=(10,0) to P2=(4,1).
CP3: (5-0.5t, 10-9.5t). BP2: (10-6s, s).
5-0.5t = 10-6s → 6s = 5+0.5t → s = (5+0.5t)/6.
10-9.5t = s = (5+0.5t)/6.
6(10-9.5t) = 5+0.5t
60-57t = 5+0.5t
55 = 57.5t
t = 55/57.5 = 110/115 = 22/23 ≈ 0.957.
s = (5+0.5(22/23))/6 = (5+11/23)/6 = (115/23+11/23)/6 = (126/23)/6
