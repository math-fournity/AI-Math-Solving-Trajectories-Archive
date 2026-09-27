# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let there be 320 points arranged on a circle, labeled \(1, 2, 3, \ldots, 8, 1, 2, 3, \ldots, 8, \ldots\) in order. Line segments may only be drawn to connect points labeled with the same number. What is the largest number of non-intersecting line segments one can draw? (Two segments sharing the same endpoint are considered to be intersecting).       — 题目文本
#   Let us label the points \(p_{1}, \ldots, p_{320}\). Consider the shortest line segment \(p_{a} p_{b}\). There are no lines from points on the smaller sector of the circle defined by this line, \(p \in \{p_{a+1}, p_{a+2}, \ldots, p_{b-1}\}\). Assuming the contrary, if there is a line from \(p\), any line \(pq\) must be in the same sector, as otherwise \(pq\) will intersect \(p_{a} p_{b}\), which is contradictory.

Since there are no points between \(p_{a}\) and \(p_{b}\), we can effectively remove this section, leaving the points \(p_{1}, \ldots, p_{a}, p_{b+1}, \ldots, p_{320}\). Since \(a \equiv b \pmod{8}\), some \(8k\) points are removed, for \(k \in \mathbb{N}\). We now consider the shortest line in the remaining set of points. After recursive removal of at least 8 points for each line removed, we can remove at most 39 such lines, leaving 8 points \(1, 2, \ldots, 8\) on which no further removal is possible.

We see that 39 is possible, with line segments between \(p_{4k}\) and \(p_{320-4k}\) for \(k = \{1, \ldots, 39\}\).

\(\boxed{39}\)  — 标准解答
#   Let me solve this problem. We have 320 points on a circle, labeled 1,2,3,...,8,1,2,3,...,8,... in order. So 320/8 = 40 points with each label. So there are 40 points labeled 1, 40 labeled 2, ..., 40 labeled 8.

Line segments may only be drawn to connect points with the same label. So we can only draw chords connecting two points with the same number. We want the maximum number of non-intersecting line segments (chords), where two segments sharing an endpoint are also considered intersecting.

So essentially, for each label i (1 to 8), we have 40 points on the circle, and we can draw non-intersecting chords among these 40 points. But chords from different labels can also intersect each other! So we need to consider the global constraint.

Wait, let me think about this more carefully. The points are arranged on a circle with labels 1,2,3,...,8 repeating. So the positions are:
Position 1: label 1
Position 2: label 2
...
Position 8: label 8
Position 9: label 1
Position 10: label 2
...
Position 320: label 8

So there are 40 points of each label, evenly spaced (every 8th position).

A chord connects two points with the same label. Two chords intersect if they cross each other inside the circle, or if they share an endpoint.

Since each point can be used at most once (sharing endpoint = intersecting), each point is in at most one chord.

So we're selecting a set of chords (each connecting two same-labeled points) such that no two chords cross and no two share an endpoint. Maximize the number of chords.

Total points = 320, so at most 160 chords (if we could pair everything). But the constraint is that chords can only connect same-label points, and chords can't cross.

Let me think about this as a non-crossing matching problem.

For a single label with 40 points on a circle, the maximum non-crossing matching pairs up to 20 chords (pairing all 40 points in a non-crossing way, e.g., adjacent pairs). But here the 40 points of a given label are interspersed with points of other labels.

The key constraint: chords from different labels can cross each other. So we need to find a global non-crossing set of chords where each chord connects same-label points.

Let me think of this differently. We have 320 points on a circle. We want to select a set of non-crossing chords where each chord connects two points of the same label. Each point used at most once.

This is like a non-crossing matching problem with color constraints.

Let me think about upper bounds. 

One approach: Consider the structure. The points are arranged in 40 blocks of 8 consecutive points (labels 1-8). 

Let me think about what non-crossing chords look like. A set of non-crossing chords on a circle forms a planar structure. 

Key insight: If we have a non-crossing set of chords, we can think of them as dividing the circle into regions. 

Let me think about small cases first. 

Consider a simpler version: 2n points on a circle, labeled 1,2,...,k repeating. What's the max non-crossing same-label matching?

Actually, let me think about this problem more carefully.

Let me consider the problem as follows. We have 320 points on a circle. A chord between positions i and j (same label) divides the remaining points into two arcs. For non-crossing, any other chord must have both endpoints on the same arc (or be nested).

This is essentially a maximum non-crossing matching with the constraint that matched pairs must have the same label.

This can be solved with dynamic programming, but 320 points is large. Let me think about the structure.

Let me think about it differently. Consider the 40 points of label 1. They are at positions 1, 9, 17, 25, ..., 313. These are equally spaced (every 8 positions). Similarly for each label.

Now, a chord connecting two points of the same label, say label 1 at positions 1 and 9, is a short chord. A chord connecting positions 1 and 313 is a long chord.

For non-crossing matchings, short chords are generally better because they "use up" less of the circle.

Let me think about the maximum. 

Upper bound: Each label has 40 points, so at most 20 chords per label, giving at most 160 total. But chords from different labels cross, so we can't achieve this.

Let me think about which chords can coexist.

Consider two labels, say label 1 and label 2. The points of label 1 are at positions 1, 9, 17, ... and label 2 at positions 2, 10, 18, .... A chord of label 1 connecting positions a and b, and a chord of label 2 connecting positions c and d, cross if and only if the positions interleave (a < c < b < d or c < a < d < b, considering circular order).

Let me think about a specific strategy. What if we only use "short" chords connecting adjacent same-label points?

For label 1: positions 1, 9, 17, 25, ..., 313. Adjacent pairs: (1,9), (17,25), (33,41), ..., (305,313). That's 20 chords. But do these cross chords from other labels?

A chord (1,9) of label 1 spans positions 2,3,4,5,6,7,8 (the interior). A chord of label 2, say (2,10), spans positions 3,4,5,6,7,8,9. Do (1,9) and (2,10) cross? Position order: 1, 2, 9, 10. So 1 < 2 < 9 < 10, which means they interleave: 1 < 2 < 9 < 10. Yes, they cross!

So we can't use both (1,9) for label 1 and (2,10) for label 2.

Hmm, this is more constrained than I thought.

Let me reconsider. The points are at positions 1 through 320 on a circle. Label at position i is ((i-1) mod 8) + 1.

A chord from position i to position j (same label) and a chord from position k to position l (same label, possibly different) cross iff the four positions are distinct and interleave around the circle.

Since same-label points are 8 apart, the shortest chord for any label spans 8 positions (connecting position i and i+8, going through 7 intermediate positions).

Let me think about the problem differently. 

Consider the 320 points. Let's think about which pairs of same-label points can be connected without crossing.

Actually, let me think about this problem as a maximum independent set in a circle graph, but that's NP-hard in general. However, the special structure here might help.

Let me reconsider. The problem is to find a maximum non-crossing matching where each matched pair has the same label. This is actually solvable in polynomial time using DP on intervals.

For n points on a circle, the DP is: dp[i][j] = max non-crossing matching using points in the arc from i to j. The recurrence is:
dp[i][j] = max(dp[i+1][j], max over k in (i,j] where label(i)==label(k) of 1 + dp[i+1][k-1] + dp[k+1][j])

But with 320 points, this is O(320^3) which is about 32 million, feasible computationally. But I need to solve this by hand...

Let me think about the structure more.

The labels repeat with period 8. So position i has label ((i-1) mod 8) + 1. Two positions have the same label iff they differ by a multiple of 8.

So a chord connects positions i and j where j - i ≡ 0 (mod 8), i.e., j = i + 8m for some positive integer m.

The chord (i, i+8m) divides the circle into two arcs: one of length 8m-1 (positions i+1 to i+8m-1) and one of length 320-8m-1 (positions i+8m+1 to i-1, wrapping around).

For two chords to not cross, they must be "nested" or in separate arcs.

Let me think about the problem structure. 

Consider the 40 "blocks" of 8 consecutive points. Block b (for b = 0, 1, ..., 39) contains positions 8b+1, 8b+2, ..., 8b+8, with labels 1, 2, ..., 8 respectively.

A chord connects two positions with the same label, which are in blocks that differ by some amount. Specifically, position 8b + L (label L) can connect to position 8b' + L (same label L) for any b ≠ b'.

The chord from block b to block b' (with label L) spans all blocks between b and b' (in one direction).

Now, for non-crossing chords, if we have a chord from block b to block b' (spanning blocks b+1, ..., b'-1 in between), then any other chord must either be entirely within blocks b+1 to b'-1, or entirely outside (in the complementary arc).

This is like a non-crossing matching on 40 blocks, but within each block, we can use at most one chord endpoint (since each position is used at most once, and each block has one position per label).

Wait, actually each block has 8 positions (one per label), and each position can be used at most once. So from each block, we can use up to 8 positions (one per label), but each position is used in at most one chord.

Hmm, let me reconsider. Each block has 8 points, one of each label. A chord uses 2 points (of the same label) from 2 different blocks. Each point is used at most once.

So the question is: select a set of non-crossing chords, each connecting same-label points from different blocks, maximizing the total number of chords.

Let me think about this as follows. Consider the 40 blocks arranged in a circle. A chord connects block b to block b' using label L (both blocks have a point with label L). Two chords cross if their block-pairs interleave on the circle of blocks.

But wait, it's more subtle because within a block, the 8 points are at different positions, so the crossing condition depends on the exact positions, not just the blocks.

Actually, let me reconsider. Two chords (i, j) and (k, l) with i < j and k < l cross iff i < k < j < l or k < i < l < j (in linear order, assuming no wrapping). On a circle, we need to be more careful, but the idea is the same.

Since the points within a block are at consecutive positions, the crossing condition does depend on the exact positions.

Let me think about this more carefully with a specific example.

Chord A: connects position 8b+L to position 8b'+L (label L, blocks b and b').
Chord B: connects position 8c+M to position 8c'+M (label M, blocks c and c').

Assume b < b' and c < c' (in terms of block order, and the chords go "forward"). The positions are:
A: 8b+L to 8b'+L
B: 8c+M to 8c'+M

For them to cross (in the linear sense, assuming no wrapping around the circle), we need one endpoint of B between the endpoints of A and the other outside.

This is getting complicated. Let me try a different approach.

Let me think about the problem as a DP on the circle of 320 points.

Actually, let me try to think about it more cleverly.

Key observation: The labels repeat with period 8. So the configuration has a rotational symmetry of order 8 (shifting by 8 positions maps label 1 to label 1, etc., but shifts the blocks).

Wait, no. Shifting by 8 positions maps position i to position i+8, which has the same label. So the configuration is invariant under rotation by 8 positions (i.e., by 1 block). This means the problem has a 40-fold rotational symmetry (by blocks).

Hmm, but that doesn't directly help with the optimization.

Let me try to think about upper and lower bounds.

Lower bound: Can we achieve some number of chords?

Strategy 1: Use only chords within consecutive blocks. For example, connect position 8b+L to position 8(b+1)+L for each b and L. But these chords would cross each other (as we saw, (1,9) and (2,10) cross).

Actually wait. Let me reconsider. Position 1 (label 1, block 0) to position 9 (label 1, block 1). Position 2 (label 2, block 0) to position 10 (label 2, block 1). These chords: (1,9) and (2,10). In the circle, positions 1, 2, 9, 10 appear in order 1, 2, 9, 10. So 1 < 2 < 9 < 10, meaning chord (1,9) separates 2 from 10, so they cross. Yes, they cross.

So we can't use all 8 labels between the same pair of consecutive blocks.

Strategy 2: What if we pair up blocks and use only one label per pair?

If we pair block 0 with block 1 using label 1 (chord from pos 1 to pos 9), and pair block 2 with block 3 using label 1 (chord from pos 17 to pos 25), etc., then these chords don't cross (they're in disjoint arcs). We get 20 chords (from 40 blocks paired into 20 pairs, each pair using 1 chord).

But we can do better. Within each pair of consecutive blocks, we could potentially use more than one label if the chords don't cross.

Wait, chords (1,9) [label 1] and (3,11) [label 3]: positions 1, 3, 9, 11 in order 1, 3, 9, 11. Chord (1,9) separates 3 from 11, so they cross. So any two chords between the same pair of consecutive blocks will cross (since the positions interleave).

So between any pair of consecutive blocks, we can use at most 1 chord.

What about non-consecutive blocks? Chord from block 0 to block 2 (skipping block 1). E.g., position 1 (label 1, block 0) to position 17 (label 1, block 2). This spans blocks 0, 1, 2. Inside, we could have chords entirely within block 1 (but a chord needs two points of the same label, and block 1 has only one point per label, so no chord within a single block). Or chords within the arc from position 2 to position 16.

Hmm, this is getting complex. Let me think about it differently.

Let me reformulate: We have 320 points on a circle. We want a maximum non-crossing matching where each matched pair has the same label (same residue mod 8).

I think the answer might be 40. Let me think about why.

Actually, let me think about a cleaner approach. Consider the 320 points. Any non-crossing matching on a circle with n points has at most n/2 edges. Here n = 320, so at most 160. But the label constraint reduces this.

Let me think about the problem as follows. Consider the dual perspective: instead of thinking about which chords to draw, think about which points are unmatched.

In a non-crossing matching on a circle, the unmatched points and the chords form a non-crossing structure. 

Let me try to think about small cases and find a pattern.

Small case: 2 blocks (16 points), labels 1-8, 1-8. What's the max non-crossing same-label matching?

Points: 1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8 (positions 1-16).

Possible chords: (1,9), (2,10), (3,11), (4,12), (5,13), (6,14), (7,15), (8,16) — each connecting same label across the two blocks.

Any two of these cross (as argued above, positions interleave). So max is 1 chord.

With 2 blocks, max = 1.

Small case: 3 blocks (24 points). Labels: 1-8, 1-8, 1-8.

Possible chords: within blocks 0-1, blocks 1-2, blocks 0-2, or blocks 0-2 wrapping around.

Chords between blocks 0 and 1: (1,9), (2,10), ..., (8,16). At most 1 (they all cross each other).
Chords between blocks 1 and 2: (9,17), (10,18), ..., (16,24). At most 1.
Chords between blocks 0 and 2: (1,17), (2,18), ..., (8,24). At most 1 (they all cross each other).

Can we have 2 non-crossing chords? E.g., (1,9) [blocks 0-1, label 1] and (10,18) [blocks 1-2, label 2]. Positions: 1, 9, 10, 18. Chord (1,9) and (10,18): 1 < 9 < 10 < 18, so they don't interleave — they don't cross! But wait, position 9 and 10 are in the same block (block 1). Chord (1,9) uses position 9, and chord (10,18) uses position 10. These are different positions, so no shared endpoint. And they don't cross. So we can have 2 chords.

Can we have 3? We'd need 3 non-crossing chords. Let's try (1,9), (10,18), and something in the remaining arc. After drawing (1,9) and (10,18), the remaining points are: 2,3,4,5,6,7,8 (between 1 and 9, exclusive), 11,12,13,14,15,16 (between 10 and 18, exclusive), and 19,20,21,22,23,24 (between 18 and 1, wrapping around). 

In the arc 2-8 (block 0 minus position 1), we have labels 2,3,4,5,6,7,8 — all different, no same-label pair. Similarly for other arcs. So no more chords can be added. Max = 2 for 3 blocks.

Hmm wait, but we could also try chords that span multiple blocks. Let me try (1,17) [blocks 0-2, label 1] and (9,10)... no, 9 and 10 have different labels. 

What about (2,10) [label 2, blocks 0-1] and (17, 25)? No, we only have 3 blocks (24 points), so position 25 doesn't exist.

Let me try (1,17) [label 1, blocks 0-2] — this spans the entire circle almost. Then inside the arc from 2 to 16, we have blocks 0 (positions 2-8), 1 (positions 9-16). Same labels: position 2 (label 2) and position 10 (label 2), etc. We can draw one chord in this arc, say (2,10). Then inside the arc from 3 to 9, we have labels 3,4,5,6,7,8,1 — all different. And inside the arc from 11 to 16, labels 3,4,5,6,7,8 — all different. So max 2 chords.

In the complementary arc (positions 18-24, i.e., block 2 minus position 17), labels 2,3,4,5,6,7,8 — all different, no chord.

So with 3 blocks, max = 2.

Pattern so far: 2 blocks → 1, 3 blocks → 2. Let me check 4 blocks.

4 blocks (32 points). Labels: 1-8 repeated 4 times.

Can we get 4? Let's try: (1,9) [label 1, blocks 0-1], (10,18) [label 2, blocks 1-2], (19,27) [label 3, blocks 2-3]. These are non-crossing (each is in a disjoint arc region). Wait, let me check: (1,9) and (10,18): 1 < 9 < 10 < 18, no cross. (10,18) and (19,27): 10 < 18 < 19 < 27, no cross. (1,9) and (19,27): 1 < 9 < 19 < 27, no cross. 

Can we add a 4th? Remaining positions: 2-8, 11-17, 20-26, 28-32. In each of these arcs, all labels are distinct (each arc is a subset of a single block minus one position). So no more chords. Max = 3? 

Wait, but what about the arc from 28 to 1 (wrapping around)? Positions 28-32: labels 4,5,6,7,8. All distinct. And position 1 is used. So no chord there.

Hmm, but what if we use a different strategy? What about (1,25) [label 1, blocks 0-3, spanning 3 blocks], and then chords inside?

(1,25): spans positions 2-24. Inside, we have blocks 0 (pos 2-8), 1 (pos 9-16), 2 (pos 17-24). This is like the 3-block problem, which gives 2 chords. Plus the complementary arc (positions 26-32): labels 2,3,4,5,6,7,8 — no chord. So total 3.

What about (1,17) [label 1, blocks 0-2] and (25, 9)? No, that wraps around. Let me think on the circle.

On the circle, (1,17) divides into arcs: 2-16 and 18-320... wait, we only have 32 points. Arcs: 2-16 and 18-32,1 (wrapping). In arc 2-16 (blocks 0 minus pos 1, and block 1): this is like 2 blocks minus 1 point. Labels: 2,3,4,5,6,7,8,1,2,3,4,5,6,7,8. Same labels: (2,10), (3,11), ..., (8,16). But these all cross each other, so at most 1. In arc 18-32 (block 2 minus pos 17, and block 3): labels 2,3,4,5,6,7,8,1,2,3,4,5,6,7,8. Same: at most 1 chord. So total 3.

Hmm, seems like 4 blocks give 3. Pattern: n blocks → n-1?

Let me verify with 2 blocks: 2-1 = 1. ✓. 3 blocks: 3-1 = 2. ✓. 4 blocks: 4-1 = 3. ✓.

If this pattern holds, 40 blocks → 39.

But wait, let me check if we can do better with 4 blocks. 

What about using chords that don't span exactly 1 block? 

Let me try: (1,9) [label 1, blocks 0-1], (17,25) [label 1, blocks 2-3]. These don't cross (1 < 9 < 17 < 25). Can we add more? In arc 2-8: no same-label pairs. In arc 10-16: labels 2,3,4,5,6,7,8,1 — all distinct. In arc 18-24: labels 2,3,4,5,6,7,8,1 — all distinct. In arc 26-32: labels 2,3,4,5,6,7,8 — all distinct. So total 2. Worse.

What about (2,10) [label 2, blocks 0-1], (3,11) [label 3, blocks 0-1]? These cross (2 < 3 < 10 < 11). So no.

What about (1,9) [label 1, blocks 0-1], (18,26) [label 2, blocks 2-3], and something in between? Arc 10-17: labels 2,3,4,5,6,7,8,1 — all distinct. Arc 19-25: labels 3,4,5,6,7,8,1 — all distinct. Arc 27-32,1: labels 3,4,5,6,7,8 — distinct. Arc 2-8: distinct. So total 2.

What about (1,17) [label 1, blocks 0-2], (18, 26) [label 2, blocks 2-3]? Positions: 1, 17, 18, 26. 1 < 17 < 18 < 26, no cross. Arc 2-16: 2 blocks minus 1 point, at most 1 chord. Arc 19-25: distinct. Arc 27-32: distinct. Total: 1 + 1 + 1 = 3.

What about (1,9) [label 1], (10,18) [label 2], (19,27) [label 3], (28, 4)? Position 28 is label 4, position 4 is label 4. But 28 > 4, so on the circle, this chord wraps around. (28, 4) and (1, 9): on the circle, 28, 1, 4, 9 — does (28,4) separate 1 from 9? The arc from 28 to 4 (going forward) includes 29,30,31,32,1,2,3,4. So 1 is inside this arc but 9 is outside. So (28,4) and (1,9) cross. So this doesn't work.

What if instead of (28,4), we use (4, 28)? Same chord, same crossing issue.

Hmm. What about (1,9), (10,18), (19,27), and (28, 36)? But we only have 32 points (4 blocks), so position 36 doesn't exist.

So for 4 blocks, max seems to be 3.

Let me try 5 blocks (40 points). Can we get 5?

(1,9) [label 1, blocks 0-1], (10,18) [label 2, blocks 1-2], (19,27) [label 3, blocks 2-3], (28,36) [label 4, blocks 3-4]. These are all non-crossing. Can we add a 5th? Remaining arcs: 2-8 (distinct), 11-17 (distinct), 20-26 (distinct), 29-35 (distinct), 37-40 (labels 5,6,7,8 — distinct). So total 4. 

Can we do better with 5 blocks? Let me try a different strategy.

(1,17) [label 1, blocks 0-2], (18,34) [label 2, blocks 2-4]. Positions: 1, 17, 18, 34. No cross. Arc 2-16: 2 blocks minus 1 point → 1 chord. Arc 19-33: 2 blocks minus 1 point → 1 chord. Arc 35-40,1: labels 3,4,5,6,7,8 — distinct. Total: 1 + 1 + 1 + 1 = 4.

What about (1,33) [label 1, blocks 0-4, spanning 4 blocks]? Arc 2-32: 4 blocks minus 1 point. This is like 4 blocks with one point removed. Hmm, this is getting complicated.

Let me try to think about it more carefully. With 5 blocks, can we get 5?

Let me try: (1,9) [label 1], (10,18) [label 2], (19,27) [label 3], (28,36) [label 4], (37, 5) [label 5, wrapping]. (37,5) wraps around: arc from 37 to 5 includes 38,39,40,1,2,3,4,5. Does (37,5) cross (1,9)? 1 is in the arc 37-5, and 9 is outside. So yes, they cross. Doesn't work.

What about (37, 45)? Only 40 points, so no.

What if we use (40, 8) [label 8, blocks 4-0, wrapping]? Arc from 40 to 8 includes 1,2,...,8. Does this cross (1,9)? 1 is in the arc, 9 is outside. Cross. Doesn't work.

So with the "chain" strategy, we get 4 for 5 blocks. Can we do better?

Let me try: (1,25) [label 1, blocks 0-3], (26,34) [label 2, blocks 3-4]. No cross (1 < 25 < 26 < 34). Arc 2-24: 3 blocks minus 1 point. Arc 27-33: 1 block minus 1 point, distinct. Arc 35-40: distinct. Arc 2-24: this is blocks 0 (pos 2-8), 1 (pos 9-16), 2 (pos 17-24), which is like 3 blocks → 2 chords. Total: 1 + 2 + 1 = 4.

What about (1,17) [label 1, blocks 0-2], (18,26) [label 2, blocks 2-3], (27,35) [label 3, blocks 3-4]? No crosses. Arc 2-16: 2 blocks minus 1 point → 1. Arc 19-25: 1 block minus 1 point → 0. Arc 28-34: 1 block minus 1 point → 0. Arc 36-40: distinct. Total: 1 + 1 + 1 + 0 = 3. Worse.

What about (1,17) [label 1, blocks 0-2], (18,34) [label 2, blocks 2-4]? Arc 2-16: 2 blocks minus 1 → 1. Arc 19-33: 2 blocks minus 1 → 1. Arc 35-40: distinct. Total: 1 + 1 + 1 = 3. Wait, I think I miscounted. (1,17) is 1 chord, plus 1 in arc 2-16, plus 1 in arc 19-33, plus 0 in arc 35-40 = 3. But earlier I said 4. Let me recheck.

Oh wait, I think I need to be more careful. (1,17) and (18,34): positions 1, 17, 18, 34. 1 < 17 < 18 < 34. No cross. Arc 2-16: positions 2-16, which is block 0 (pos 2-8) and block 1 (pos 9-16). This is 2 full blocks minus nothing (wait, position 1 is used by the first chord, position 17 is used by the first chord). So arc 2-16 has 15 points: labels 2,3,4,5,6,7,8,1,2,3,4,5,6,7,8. Same-label pairs: (2,10), (3,11), ..., (8,16), and also (1 is at position 9, but there's no other 1 in this arc... wait, position 9 has label 1, and there's no other label 1 in positions 2-16 except position 9. So the same-label pairs are (2,10), (3,11), (4,12), (5,13), (6,14), (7,15), (8,16). These all cross each other, so at most 1.

Arc 19-33: positions 19-33, which is block 2 (pos 19-24, labels 3,4,5,6,7,8) and block 3 (pos 25-32, labels 1,2,3,4,5,6,7,8) and position 33 (label 1, block 4). Wait, I have 5 blocks (40 points). Block 3 is positions 25-32, block 4 is positions 33-40.

Arc 19-33: positions 19-33. Labels: 3,4,5,6,7,8 (block 2, pos 19-24), 1,2,3,4,5,6,7,8 (block 3, pos 25-32), 1 (block 4, pos 33). Same-label pairs: (3, 27), (4, 28), (5, 29), (6, 30), (7, 31), (8, 32), (1, 33). Wait, position 25 has label 1, position 33 has label 1. So (25, 33) is a pair. And (3, 27): position 19 has label 3, position 27 has label 3. Yes. Etc.

But all these chords span from block 2 to block 3 (or block 3 to block 4 for (25,33)). They would all cross each other (same issue as before). So at most 1.

Actually wait, (25, 33) goes from block 3 to block 4, while (19, 27) goes from block 2 to block 3. Do they cross? Positions 19, 25, 27, 33: 19 < 25 < 27 < 33. Chord (19,27) separates 25 from 33, so yes they cross.

What about (19, 27) and (26, 34)? But 34 is outside the arc 19-33. So (26,34) is not in this arc.

OK so arc 19-33 gives at most 1 chord.

Arc 35-40: positions 35-40, labels 3,4,5,6,7,8. All distinct. 0 chords.

Total: 1 (chord (1,17)) + 1 (arc 2-16) + 1 (arc 19-33) + 0 = 3. 

Hmm, but earlier with (1,25) and (26,34), I got 4. Let me recheck that.

(1,25) [label 1, blocks 0-3], (26,34) [label 2, blocks 3-4]. 
Arc 2-24: positions 2-24, blocks 0 (pos 2-8), 1 (pos 9-16), 2 (pos 17-24). 3 full blocks. This is the 3-block problem → 2 chords.
Arc 27-33: positions 27-33, labels 3,4,5,6,7,8 (block 3, pos 27-32) and 1 (block 4, pos 33). All distinct. 0 chords.
Arc 35-40: labels 3,4,5,6,7,8. Distinct. 0.
Total: 1 + 1 + 2 + 0 + 0 = 4. Yes, 4.

Can we do 5 with 5 blocks? Let me think harder.

What about (1,9) [label 1, blocks 0-1], (10,26) [label 2, blocks 1-3], (27,35) [label 3, blocks 3-4]?
Positions: 1, 9, 10, 26, 27, 35. No crosses (1 < 9 < 10 < 26 < 27 < 35).
Arc 2-8: distinct. 0.
Arc 11-25: positions 11-25, block 1 (pos 11-16, labels 3,4,5,6,7,8) and block 2 (pos 17-24, labels 1,2,3,4,5,6,7,8) and position 25 (label 1, block 3). Same-label pairs: (3,19), (4,20), (5,21), (6,22), (7,23), (8,24), (1, 25), (2, 18). Wait, position 18 has label 2, and is there another 2? Position 10 has label 2 but it's used. So in arc 11-25: labels are 3,4,5,6,7,8,1,2,3,4,5,6,7,8,1. Same pairs: (3,19), (4,20), (5,21), (6,22), (7,23), (8,24), (17,25) [both label 1]. These all cross each other, so at most 1.
Arc 28-34: positions 28-34, labels 4,5,6,7,8 (block 3) and 1,2 (block 4). Distinct. 0.
Arc 36-40: distinct. 0.
Total: 1 + 1 + 1 + 0 + 0 + 0 = 3. Worse.

What about (1,17) [label 1, blocks 0-2], (2,10) [label 2, blocks 0-1]? These cross: 1 < 2 < 17, and 10 is between 2 and 17. So 1 < 2 < 10 < 17, chord (1,17) separates 2 from 10. Cross. Doesn't work.

What about (1,17) [label 1, blocks 0-2], (18, 2) [label 2, wrapping]? (18,2) wraps around: arc from 18 to 2 includes 19,...,40,1,2. Does (1,17) cross (18,2)? 1 is in arc 18-2, 17 is outside. Cross. Doesn't work.

Hmm, it seems hard to get more than 4 with 5 blocks. Let me try another approach.

(1,9) [label 1], (17,25) [label 1, blocks 2-3], (26,34) [label 2, blocks 3-4]. No crosses. Arc 2-8: 0. Arc 10-16: 0. Arc 18-24: 0. Arc 27-33: 0. Arc 35-40: 0. Total: 3. Worse.

(1,9) [label 1], (10,18) [label 2], (19,27) [label 3], (28,36) [label 4]. 4 chords. Can we squeeze in a 5th? All remaining arcs have distinct labels. So 4.

What if we don't use the chain strategy? Let me try:

(1,25) [label 1, blocks 0-3], (2,10) [label 2, blocks 0-1]. Cross? 1 < 2 < 10 < 25. Chord (1,25) separates 2 from 10. Cross. No.

(1,25) [label 1], (26,34) [label 2], (35, 3) [label 3, wrapping]. (35,3) wraps: arc 35-3 includes 36,...,40,1,2,3. Does it cross (1,25)? 1 is in arc 35-3, 25 is outside. Cross. No.

(1,25) [label 1], (26,34) [label 2]. Arc 2-24: 3 blocks → 2 chords. Arc 27-33: 0. Arc 35-40: 0. Total: 4.

What about (1,33) [label 1, blocks 0-4]? This spans almost the entire circle. Arc 2-32: 4 blocks minus 1 point. This is like 4 blocks with position 1 removed from block 0. So blocks 0' (pos 2-8), 1 (pos 9-16), 2 (pos 17-24), 3 (pos 25-32). 4 full blocks → 3 chords. Arc 34-40: labels 2,3,4,5,6,7,8. 0. Total: 1 + 3 = 4.

Hmm, so 5 blocks consistently gives 4. The pattern n blocks → n-1 seems to hold.

Wait, but let me double-check with a different approach for 5 blocks. What about using longer chords creatively?

(1,17) [label 1, blocks 0-2], (25,33) [label 1, blocks 3-4]. No cross (1 < 17 < 25 < 33). Arc 2-16: 2 blocks minus 1 → 1. Arc 18-24: block 2 minus pos 17, labels 2,3,4,5,6,7,8. 0. Arc 26-32: block 3 minus pos 25, labels 2,3,4,5,6,7,8. 0. Arc 34-40: labels 2,3,4,5,6,7,8. 0. Total: 1 + 1 + 0 + 0 + 0 = 2. Worse.

OK so it really seems like n blocks → n-1 chords. For 40 blocks, that would be 39.

But wait, I should check this more carefully. Let me think about why n-1 is the answer and whether we can do better.

Actually, let me reconsider. With the chain strategy, we get n-1 by using chords (1,9), (10,18), (19,27), ..., (8(n-2)+1, 8(n-1)+1). Wait, let me be more precise.

For n blocks, the chain strategy: 
- Chord 1: (1, 9) [label 1, blocks 0-1]
- Chord 2: (10, 18) [label 2, blocks 1-2]
- Chord 3: (19, 27) [label 3, blocks 2-3]
- ...
- Chord k: (8(k-1)+k', 8k+k') where k' = ((k-1) mod 8) + 1

Wait, let me be more careful. Chord i connects block i-1 to block i, using label i (for i = 1, 2, ..., n-1). But labels go from 1 to 8, so for i > 8, we'd use label ((i-1) mod 8) + 1.

Chord i: position 8(i-1) + L_i to position 8i + L_i, where L_i = ((i-1) mod 8) + 1.

For i = 1: L_1 = 1, positions 1 and 9. ✓
For i = 2: L_2 = 2, positions 10 and 18. ✓
For i = 3: L_3 = 3, positions 19 and 27. ✓
...
For i = 8: L_8 = 8, positions 57 and 65. ✓
For i = 9: L_9 = 1, positions 65 and 73. But position 65 is used by chord 8! Conflict!

So the chain strategy breaks at i = 9 because position 65 (label 8, block 8) is used by chord 8, and chord 9 also wants to use position 65 (label 1, block 8)... wait, no. Position 65 = 8*8 + 1, which has label 1, not label 8. Let me recalculate.

Block 8 is positions 65-72. Position 65 has label 1, position 66 has label 2, ..., position 72 has label 8.

Chord 8: L_8 = 8, positions 8*7 + 8 = 64 and 8*8 + 8 = 72. So positions 64 and 72.
Chord 9: L_9 = 1, positions 8*8 + 1 = 65 and 8*9 + 1 = 73. So positions 65 and 73.

Position 64 (block 7, label 8) and position 72 (block 8, label 8) for chord 8.
Position 65 (block 8, label 1) and position 73 (block 9, label 1) for chord 9.

These use different positions (64, 72, 65, 73 are all distinct). And do they cross? 64 < 65 < 72 < 73. Chord (64, 72) separates 65 from 73. Cross!

So the chain strategy fails at i = 9 because chords 8 and 9 cross.

Hmm, so the simple chain strategy doesn't directly give n-1 for n > 8. Let me reconsider.

The issue is that when we use label 8 for chord 8 (connecting blocks 7-8) and label 1 for chord 9 (connecting blocks 8-9), the positions interleave: 64, 65, 72, 73.

So we need a different strategy for larger n.

Let me reconsider. The chain strategy works for the first 8 chords (using labels 1 through 8), but then we need to handle the crossing issue.

What if we use a different pattern? For example, use only odd labels for the chain? Or use a different assignment?

Actually, the issue is that consecutive chords in the chain use consecutive blocks and consecutive labels, and the positions interleave.

Let me think about this differently. Two chords (a, b) and (c, d) with a < b, c < d, and a < c (WLOG) don't cross iff c > b or d < b (i.e., they're disjoint or nested). Wait no, on a line: they don't cross iff b < c or d < a or (a < c < d < b) [nested] or (c < a < b < d) [nested]. On a circle it's more complex.

For the chain strategy, chords (8(i-1)+L_i, 8i+L_i) and (8j+L_j, 8(j+1)+L_j) with j = i+1:
- First chord: (8(i-1)+L_i, 8i+L_i)
- Second chord: (8i+L_{i+1}, 8(i+1)+L_{i+1})

These don't cross iff 8i + L_i < 8i + L_{i+1}, i.e., L_i < L_{i+1}. Since L_i = ((i-1) mod 8) + 1, we have L_{i+1} = (i mod 8) + 1. So L_i < L_{i+1} iff ((i-1) mod 8) < (i mod 8), which is true iff i mod 8 ≠ 0, i.e., i is not a multiple of 8.

So the chain works for chords 1-8 (i=1 to 7 transitions are fine), but fails at the transition from chord 8 to chord 9 (i=8, which is a multiple of 8, so L_8 = 8 > L_9 = 1).

So the chain gives 8 chords for the first 8 transitions, then breaks. We need to handle the "wrap" at every 8th transition.

One idea: at the wrap, instead of using a chord between blocks 8 and 9, skip it and use a chord between blocks 8 and 10 or something.

Alternatively, we could use a different label assignment that avoids the wrap issue.

What if we use the same label for all chords? E.g., all chords use label 1.

Chord i: (8(i-1)+1, 8i+1) for i = 1, 2, ..., n-1. These are (1,9), (9,17), (17,25), ... But position 9 is shared between chord 1 and chord 2! So they share an endpoint, which counts as intersecting. Doesn't work.

What if we use label 1 for odd chords and label 2 for even chords?
Chord 1: (1, 9) [label 1]
Chord 2: (10, 18) [label 2]
Chord 3: (17, 25) [label 1]
Chord 4: (26, 34) [label 2]

Check crossings: (1,9) and (10,18): 1 < 9 < 10 < 18. No cross. (10,18) and (17,25): 10 < 17 < 18 < 25. Chord (10,18) separates 17 from 25. Cross!

So that doesn't work either.

The issue is that when we use label 1 for chord 3 (blocks 2-3), the positions are 17 and 25, which interleave with chord 2's positions 10 and 18.

Let me think about this more carefully. The key constraint is that for two consecutive chords in the chain (between blocks i, i+1 and blocks i+1, i+2), the label of the first chord must be less than the label of the second chord (to avoid crossing).

So we need a sequence of labels L_1, L_2, ..., L_{n-1} (each in {1,...,8}) such that L_1 < L_2 < ... < L_{n-1}. But this means we can have at most 8 chords in such a chain (since labels are 1 to 8).

After 8 chords, we need to "reset." How?

One approach: after 8 chords (using labels 1 through 8), the 8th chord connects blocks 7-8 using label 8 (positions 64 and 72). Now, for the next chord, we can't use the chain between blocks 8-9 because any label would cause a crossing with chord 8 (since we'd need L_9 > L_8 = 8, which is impossible).

Instead, we could use a chord that "jumps over" block 8. For example, a chord from block 7 to block 9 (skipping block 8). But block 7's position for any label is already used by chord 8 (which uses position 64, label 8). So we could use a different label for block 7.

Wait, chord 8 uses positions 64 (block 7, label 8) and 72 (block 8, label 8). So block 7 still has positions 57-63 available (labels 1-7), and block 8 has positions 65-71 available (labels 1-7).

What if we use a chord from block 6 to block 9? Block 6 has positions 49-56 (labels 1-8), but position 56 (label 8) is used by chord 7 (which connects blocks 6-7 using label 7, positions 55 and 63). Wait, let me recalculate.

Chord 7: L_7 = 7, positions 8*6+7 = 55 and 8*7+7 = 63. So positions 55 (block 6, label 7) and 63 (block 7, label 7).

So block 6 has positions 49-56, with position 55 used. Block 7 has positions 57-64, with positions 63 and 64 used (by chords 7 and 8). Block 8 has positions 65-72, with position 72 used (by chord 8).

This is getting complicated. Let me think about the problem differently.

Let me think about it as a global optimization problem. 

Alternative approach: Think of the 320 points on the circle. We want a maximum non-crossing matching with same-label constraint.

Key insight: A non-crossing matching on a circle can be decomposed into "non-crossing" structures. The maximum non-crossing matching on n points (without label constraint) is n/2 (pair adjacent points). With the label constraint, we need to be more careful.

Let me think about an upper bound. 

Consider the 320 points. In any non-crossing matching, the chords divide the circle into regions. Each chord "uses up" some arc of the circle.

Upper bound idea: Consider any arc of 8 consecutive points (one block). These 8 points all have different labels. A chord using any of these points must connect to a point outside this block (same label). So each chord "crosses" the boundary of this block.

Hmm, this doesn't directly give a bound.

Let me think about it differently. 

Consider the 40 points of label 1, at positions 1, 9, 17, ..., 313. These divide the circle into 40 arcs, each of length 8 (containing 7 interior points). A chord of label 1 connects two of these 40 points. A chord of any other label connects two points within these arcs.

Actually, I think the key insight is about the structure of non-crossing matchings on a circle.

Let me think about the problem as follows. We have 320 points. A non-crossing matching pairs up some of them. The unmatched points are "free." The matching is non-crossing, so it forms a planar structure.

For the label constraint: each matched pair must have the same label.

Let me think about the maximum. 

Claim: The answer is 40.

Wait, let me reconsider. With n blocks, I was getting n-1 for small cases. But the chain strategy breaks at 8. Let me re-examine.

For n = 9 blocks (72 points), the chain gives 8 chords (labels 1-8, blocks 0-8). Can we do better?

After the 8 chords, the used positions are:
Chord 1: 1, 9 (label 1)
Chord 2: 10, 18 (label 2)
Chord 3: 19, 27 (label 3)
Chord 4: 28, 36 (label 4)
Chord 5: 37, 45 (label 5)
Chord 6: 46, 54 (label 6)
Chord 7: 55, 63 (label 7)
Chord 8: 64, 72 (label 8)

Used positions: 1, 9, 10, 18, 19, 27, 28, 36, 37, 45, 46, 54, 55, 63, 64, 72.
Free positions: 2-8, 11-17, 20-26, 29-35, 38-44, 47-53, 56-62, 65-71.

Each free arc (between consecutive used positions) has 6 or 7 points, all with distinct labels. So no more chords can be added.

But can we do better than 8 for 9 blocks? Let me try a different strategy.

What if we use a "nested" strategy? For example:
- Chord A: (1, 65) [label 1, blocks 0-8, spanning 8 blocks]
- Inside arc 2-64: 8 blocks minus 1 point. This is like 8 blocks with one point removed.
- Inside arc 66-72: 7 points, distinct labels. 0 chords.

For the 8 blocks minus 1 point (arc 2-64): blocks 0' (pos 2-8, labels 2-8), 1 (pos 9-16), 2 (pos 17-24), ..., 7 (pos 57-64). This is 7 full blocks plus a partial block. Hmm, this is like 8 blocks but block 0 is missing label 1.

The chain strategy on this: we need labels that are strictly increasing. We have 7 full blocks (1-7) and a partial block 0 (labels 2-8). 

Actually, let me think about this differently. The arc 2-64 has 63 points. The blocks are:
- Block 0': positions 2-8 (labels 2,3,4,5,6,7,8) — 7 points
- Block 1: positions 9-16 (labels 1,2,3,4,5,6,7,8) — 8 points
- Block 2: positions 17-24 — 8 points
- ...
- Block 7: positions 57-64 — 8 points

Total: 7 + 7*8 = 7 + 56 = 63 points.

For the chain strategy within this arc, we can use chords between consecutive blocks. The first chord could be between block 0' and block 1. Block 0' has labels 2-8, block 1 has labels 1-8. We need a label present in both, and the chord positions must not cross with subsequent chords.

If we use label 2: chord (2, 10). Then the next chord between blocks 1 and 2 must use label > 2, say label 3: (19, 27). Then label 4: (28, 36), ..., label 8: (64, 72)... wait, position 72 is outside the arc 2-64. Block 7 is positions 57-64. So the chord between blocks 6 and 7 using label 8 would be (56, 64). But position 56 is in block 6 (label 8), and position 64 is in block 7 (label 8). 

Wait, let me redo this. The arc is 2-64. Blocks within this arc:
- Block 0': pos 2-8 (labels 2-8)
- Block 1: pos 9-16 (labels 1-8)
- Block 2: pos 17-24
- Block 3: pos 25-32
- Block 4: pos 33-40
- Block 5: pos 41-48
- Block 6: pos 49-56
- Block 7: pos 57-64

Chain: 
Chord 1: block 0' to block 1, label 2: (2, 10)
Chord 2: block 1 to block 2, label 3: (19, 27)
Chord 3: block 2 to block 3, label 4: (28, 36)
Chord 4: block 3 to block 4, label 5: (37, 45)
Chord 5: block 4 to block 5, label 6: (46, 54)
Chord 6: block 5 to block 6, label 7: (55, 63)
Chord 7: block 6 to block 7, label 8: (64, 72)... 

Wait, position 72 is outside the arc. Block 7 is positions 57-64. The chord between block 6 and block 7 using label 8 would be position 56 (block 6, label 8) to position 64 (block 7, label 8). So (56, 64). 

But wait, chord 6 uses position 55 (block 5, label 7) and position 63 (block 7, label 7). Chord 7 uses position 56 (block 6, label 8) and position 64 (block 7, label 8). Do they cross? 55 < 56 < 63 < 64. Chord (55, 63) separates 56 from 64. Cross!

Hmm, so the chain breaks again at the transition from label 7 to label 8. Wait, 55 < 56, and 63 < 64, so 55 < 56 < 63 < 64. Chord (55,63) and (56,64): 55 < 56 < 63 < 64, so they interleave. Cross.

But this is the same issue: L_7 = 7 < L_8 = 8, so 55 < 56 (since 8*6+7 = 55 < 8*6+8 = 56) and 63 < 64 (8*7+7 = 63 < 8*7+8 = 64). So 55 < 56 < 63 < 64, which means they cross.

Wait, I think I made an error earlier. Let me recheck the chain for the original problem.

Chord 7: L_7 = 7, positions 8*6+7 = 55 and 8*7+7 = 63.
Chord 8: L_8 = 8, positions 8*7+8 = 64 and 8*8+8 = 72.

55 < 64? Yes. 63 < 64? Yes. So 55 < 63 < 64 < 72. No interleaving. They don't cross!

Wait, I need to check more carefully. Chord 7 is (55, 63) and chord 8 is (64, 72). 55 < 63 < 64 < 72. These are disjoint intervals, so they don't cross. ✓

But in my nested example, chord 6 was (55, 63) and chord 7 was (56, 64). 55 < 56 < 63 < 64. These interleave, so they cross. ✗

The difference is that in the original chain, chord 7 uses label 7 (positions 55, 63) and chord 8 uses label 8 (positions 64, 72). The positions are 55, 63, 64, 72 — no interleaving because 63 < 64.

In the nested example, chord 6 uses label 7 (positions 55, 63) and chord 7 uses label 8 (positions 56, 64). The positions are 55, 56, 63, 64 — interleaving because 55 < 56 < 63 < 64.

The issue is that in the nested example, the blocks are shifted. Block 6 in the nested example is positions 49-56, and block 7 is positions 57-64. So label 8 in block 6 is position 56, and label 8 in block 7 is position 64. But label 7 in block 5 is position 55, and label 7 in block 7 is position 63. So the chord (55, 63) for label 7 goes from block 5 to block 7, and (56, 64) for label 8 goes from block 6 to block 7. These interleave.

Wait, I think I messed up the nested chain. Let me redo it.

In the nested example, the arc is 2-64. The blocks are:
- Block 0': pos 2-8 (labels 2-8)
- Block 1: pos 9-16
- Block 2: pos 17-24
- Block 3: pos 25-32
- Block 4: pos 33-40
- Block 5: pos 41-48
- Block 6: pos 49-56
- Block 7: pos 57-64

Chain chords (between consecutive blocks):
Chord 1: block 0' to block 1, label 2: (2, 10)
Chord 2: block 1 to block 2, label 3: (19, 27)
Chord 3: block 2 to block 3, label 4: (28, 36)
Chord 4: block 3 to block 4, label 5: (37, 45)
Chord 5: block 4 to block 5, label 6: (46, 54)
Chord 6: block 5 to block 6, label 7: (55, 63)

Wait, block 5 is positions 41-48, label 7 is position 47. Block 6 is positions 49-56, label 7 is position 55. So chord 6 is (47, 55), not (55, 63).

Let me recalculate. Position in block b with label L is 8b + L.
- Block 0': positions 2-8, but these are positions 8*0 + L for L = 2, 3, ..., 8. So position 2 = 8*0+2, position 8 = 8*0+8.
- Block 1: positions 9-16 = 8*1 + L for L = 1, ..., 8. Position 9 = 8*1+1, position 16 = 8*1+8.
- Block 5: positions 41-48 = 8*5 + L. Position 47 = 8*5+7, position 48 = 8*5+8.
- Block 6: positions 49-56 = 8*6 + L. Position 55 = 8*6+7, position 56 = 8*6+8.
- Block 7: positions 57-64 = 8*7 + L. Position 63 = 8*7+7, position 64 = 8*7+8.

Chord 6: block 5 to block 6, label 7: (47, 55). 
Chord 7: block 6 to block 7, label 8: (56, 64).

47 < 55 < 56 < 64. No interleaving. They don't cross! ✓

I made an error earlier. Let me redo the full chain for the nested example.

Chord 1: (2, 10) — label 2, blocks 0'-1
Chord 2: (19, 27) — label 3, blocks 1-2
Chord 3: (28, 36) — label 4, blocks 2-3
Chord 4: (37, 45) — label 5, blocks 3-4
Chord 5: (46, 54) — label 6, blocks 4-5
Chord 6: (47, 55) — label 7, blocks 5-6

Wait, chord 5 is (46, 54) and chord 6 is (47, 55). 46 < 47 < 54 < 55. Interleaving! Cross!

Hmm, so the chain breaks at the transition from label 6 to label 7 here. Let me recheck.

Chord 5: block 4 to block 5, label 6: position 8*4+6 = 38 and 8*5+6 = 46. So (38, 46).
Chord 6: block 5 to block 6, label 7: position 8*5+7 = 47 and 8*6+7 = 55. So (47, 55).

38 < 46 < 47 < 55. No interleaving. ✓

I keep making arithmetic errors. Let me be very careful.

Chord i (for the nested chain): connects block (i-1) to block i, using label (i+1) (since we start from label 2).

Chord 1: block 0 to block 1, label 2: pos 8*0+2 = 2, pos 8*1+2 = 10. (2, 10).
Chord 2: block 1 to block 2, label 3: pos 8*1+3 = 11, pos 8*2+3 = 19. (11, 19).
Chord 3: block 2 to block 3, label 4: pos 8*2+4 = 20, pos 8*3+4 = 28. (20, 28).
Chord 4: block 3 to block 4, label 5: pos 8*3+5 = 29, pos 8*4+5 = 37. (29, 37).
Chord 5: block 4 to block 5, label 6: pos 8*4+6 = 38, pos 8*5+6 = 46. (38, 46).
Chord 6: block 5 to block 6, label 7: pos 8*5+7 = 47, pos 8*6+7 = 55. (47, 55).
Chord 7: block 6 to block 7, label 8: pos 8*6+8 = 56, pos 8*7+8 = 64. (56, 64).

Check non-crossing:
(2,10) and (11,19): 2 < 10 < 11 < 19. ✓
(11,19) and (20,28): 11 < 19 < 20 < 28. ✓
(20,28) and (29,37): 20 < 28 < 29 < 37. ✓
(29,37) and (38,46): 29 < 37 < 38 < 46. ✓
(38,46) and (47,55): 38 < 46 < 47 < 55. ✓
(47,55) and (56,64): 47 < 55 < 56 < 64. ✓

All non-crossing! So the nested chain gives 7 chords in the arc 2-64, plus the outer chord (1, 65), total 8 chords for 9 blocks.

But wait, the original chain (without nesting) also gave 8 chords for 9 blocks. So nesting doesn't help here.

Hmm, but can we do better than 8 for 9 blocks? Let me think...

Actually, let me reconsider the original chain for 9 blocks.

Original chain:
Chord 1: (1, 9) — label 1
Chord 2: (10, 18) — label 2
Chord 3: (19, 27) — label 3
Chord 4: (28, 36) — label 4
Chord 5: (37, 45) — label 5
Chord 6: (46, 54) — label 6
Chord 7: (55, 63) — label 7
Chord 8: (64, 72) — label 8

Check: (55, 63) and (64, 72): 55 < 63 < 64 < 72. ✓. All good. 8 chords.

Can we add a 9th? Free positions: 2-8, 11-17, 20-26, 29-35, 38-44, 47-53, 56-62, 65-71. Each arc has 7 points with distinct labels. No more chords. So 8 is the max for 9 blocks with this strategy.

Can we do better with a different strategy for 9 blocks? Let me try:

(1, 65) [label 1, blocks 0-8], and then 7 chords in arc 2-64 (as computed above). Total 8. Same.

What about (1, 33) [label 1, blocks 0-4] and (34, 66) [label 2, blocks 4-8]?
Arc 2-32: 4 blocks minus 1 point → 3 chords (chain with labels 2-4... wait, 4 blocks minus 1 point).

Hmm, let me think about this recursively. Let f(n) = max chords for n blocks.

f(1) = 0 (only 1 block, 8 points, all different labels, no chord possible)
f(2) = 1
f(3) = 2
f(4) = 3
f(5) = 4
...
f(8) = 7
f(9) = 8

It looks like f(n) = n - 1. But wait, does this hold for larger n?

For n = 10, the chain gives 8 chords (labels 1-8, blocks 0-8), and then we're stuck. Can we get 9?

After the 8 chords, the free positions in block 8 are 65-71 (labels 1-7), and block 9 is positions 73-80 (labels 1-8). Can we add a chord between block 8 and block 9?

The last chord is (64, 72) [label 8, blocks 7-8]. A new chord between blocks 8 and 9 would be (8*8+L, 8*9+L) = (72+L, 80+L) for some label L. But position 72 is used, so L ≠ 8 (since 72+8 = 80, but 72 is used). For L = 1: (73, 81). 64 < 72 < 73 < 81. No cross with (64, 72). ✓

But wait, does (73, 81) cross any earlier chord? The earlier chords are (1,9), (10,18), ..., (64,72). (73, 81) is after all of them: 72 < 73. So no cross. ✓

So we can add chord 9: (73, 81) [label 1, blocks 8-9]. But does this cross chord 1: (1, 9)? On the circle, (1, 9) and (73, 81): 1 < 9 < 73 < 81. No cross (disjoint arcs). ✓

So for 10 blocks, we get 9 chords! The chain continues: (73, 81) [label 1], (82, 90) [label 2], etc.

Wait, but (73, 81) uses label 1, and the previous chord (64, 72) uses label 8. 64 < 72 < 73 < 81. No cross. ✓

Then chord 10: (82, 90) [label 2, blocks 9-10]. 73 < 81 < 82 < 90. No cross with (73, 81). ✓

So the chain continues! The "break" at label 8 to label 1 doesn't actually cause a crossing because the positions are far apart (72 < 73).

Wait, I think I was wrong earlier about the chain breaking. Let me recheck.

The chain is:
Chord i: (8(i-1) + L_i, 8i + L_i) where L_i = ((i-1) mod 8) + 1.

Chord 8: (8*7 + 8, 8*8 + 8) = (64, 72). L_8 = 8.
Chord 9: (8*8 + 1, 8*9 + 1) = (65, 73). L_9 = 1.

64 < 65 < 72 < 73. Chord (64, 72) and (65, 73): 64 < 65 < 72 < 73. Interleaving! Cross!

So the chain DOES break at the transition from chord 8 to chord 9. I was right the first time.

But then how did I get (73, 81) to work? Because (73, 81) is not the chain chord 9. The chain chord 9 would be (65, 73), which crosses chord 8. But (73, 81) is a different chord — it connects blocks 8 and 9 using label 1, but it starts at position 73 (block 9, label 1) and goes to position 81 (block 10, label 1). Wait, that's blocks 9-10, not blocks 8-9!

Oh I see, I skipped the connection between blocks 8 and 9, and instead connected blocks 9 and 10. So the chain is:
Chords 1-8: blocks 0-1, 1-2, ..., 7-8 (labels 1-8)
Chord 9: blocks 9-10 (label 1) — skipping the blocks 8-9 connection!

So we skip one connection (blocks 8-9) and lose one potential chord. For 10 blocks, we get 8 chords from blocks 0-8, then skip blocks 8-9, then 1 chord from blocks 9-10. Total: 9. But we could have gotten 9 = 10 - 1 if the pattern f(n) = n-1 holds.

Wait, 10 blocks, 9 chords. That's still n-1 = 9. But the chain skipped one connection. Let me see if we can recover that lost connection.

After the 8 chords (blocks 0-8) and the chord (73, 81) (blocks 9-10), the free positions in block 8 are 65-71 (labels 1-7), and in block 9 are 74-80 (labels 2-8). Can we add a chord between block 8 and block 9?

A chord (65+L-1, 73+L-1) for label L, i.e., (8*8+L, 8*9+L) for L in {1,...,7} (since position 73 is used by chord 9, and position 72 is used by chord 8).

For L = 1: (65, 73). But 73 is used. ✗
For L = 2: (66, 74). Check crossing with (64, 72): 64 < 66 < 72 < 74. Interleaving! Cross. ✗
For L = 3: (67, 75). 64 < 67 < 72 < 75. Cross. ✗
...
For L = 7: (71, 79). 64 < 71 < 72 < 79. Cross. ✗

All chords between blocks 8 and 9 cross chord 8 (64, 72). So we can't add any chord between blocks 8 and 9.

What about a chord from block 8 to block 10 (or further)? (65, 81) [label 1]: but 81 is used by chord 9. (66, 82) [label 2]: 64 < 66 < 72 < 82. Cross with chord 8. ✗.

What about a chord from block 7 to block 9? (57+L, 73+L) for some L. Position 57+L must be free. Block 7 free positions: 57-62 (labels 1-6, since 63 and 64 are used). 
(57, 73) [label 1]: 73 is used. ✗
(58, 74) [label 2]: 55 < 58 < 63 < 74. Cross with chord 7 (55, 63). ✗
...

All cross chord 7. So no.

What about a chord entirely within the free positions of blocks 8-9? The free positions are 65-71 (block 8, labels 1-7) and 74-80 (block 9, labels 2-8). Same labels: label 2 (pos 66, 74), label 3 (pos 67, 75), ..., label 7 (pos 71, 79). But all these chords cross chord 8 (64, 72) as shown above. So no.

What about a chord from block 8 to somewhere after block 10? (65, 89) [label 1, blocks 8-11]: 64 < 65 < 72 < 89. Cross with chord 8. ✗.

So it seems like once we have the 8-chord chain (blocks 0-8), the block 8 is "blocked" by chord 8, and we can't use any chord that starts in block 8 (before position 72) and ends after position 72.

So the effective strategy is: chain of 8 chords (blocks 0-8), then skip to blocks 9+, and repeat.

For 40 blocks:
- Blocks 0-8: 8 chords (labels 1-8)
- Blocks 9-17: 8 chords (labels 1-8)
- Blocks 18-26: 8 chords
- Blocks 27-35: 8 chords
- Blocks 36-39: 3 chords (labels 1-3, blocks 36-37, 37-38, 38-39)

Wait, but between the groups, we skip one connection (blocks 8-9, 17-18, 26-27, 35-36). So:

Group 1: blocks 0-8, 8 chords
Gap: blocks 8-9, 0 chords
Group 2: blocks 9-17, 8 chords
Gap: blocks 17-18, 0 chords
Group 3: blocks 18-26, 8 chords
Gap: blocks 26-27, 0 chords
Group 4: blocks 27-35, 8 chords
Gap: blocks 35-36, 0 chords
Remaining: blocks 36-39, 3 chords (labels 1-3)

Total: 8 + 8 + 8 + 8 + 3 = 35 chords.

But wait, can we do better? The gaps waste potential connections. Let me think about whether we can avoid the gaps.

The gap occurs because the chain uses labels 1-8 in order, and the transition from label 8 to label 1 causes a crossing. What if we use a different label order?

For example, what if we use labels in the order 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, ...? The idea is to go up and then down.

But the constraint is L_i < L_{i+1} for non-crossing. If we go 1, 2, ..., 8, then we need L_9 > 8, which is impossible. If we go 8, 7, ..., 1, then we need L_2 < 8, which is fine, but then L_9 < 1, impossible.

What if we go 1, 2, 3, 4, 5, 6, 7, 8, then 1, 2, ...? The transition 8 → 1 causes a crossing. But what if we insert a "reset" chord that doesn't follow the chain?

Actually, let me think about this differently. The constraint for consecutive chain chords (between blocks i, i+1 and blocks i+1, i+2) is that L_i < L_{i+1} (to avoid crossing). This means the labels must be strictly increasing, so we can have at most 8 consecutive chain chords.

But what if we don't use consecutive blocks? What if we skip a block?

For example, after 8 chords (blocks 0-8), instead of connecting blocks 8-9, we connect blocks 7-9 or blocks 8-10.

Chord from block 7 to block 9: (8*7+L, 8*9+L) = (56+L, 72+L). But position 63 (block 7, label 7) and 64 (block 7, label 8) are used. So L ∈ {1,...,6}. 

(57, 73) [label 1]: 55 < 57 < 63 < 73. Cross with chord 7 (55, 63). ✗
(58, 74) [label 2]: 55 < 58 < 63 < 74. Cross. ✗
...
(62, 78) [label 6]: 55 < 62 < 63 < 78. Cross. ✗

All cross chord 7. ✗

What about block 6 to block 9? (49+L, 72+L). Block 6 used positions: 55 (label 7), 56 (label 8). So L ∈ {1,...,6}.
(49, 73) [label 1]: 46 < 49 < 54 < 73. Cross with chord 6 (46, 54). ✗
...

All cross chord 6. ✗

It seems like any chord starting before position 64 (the start of chord 8) and ending after position 72 (the end of chord 8) will cross chord 8 or one of the earlier chords.

What about a chord from block 8 to block 10? (65, 81) [label 1]: 64 < 65 < 72 < 81. Cross with chord 8 (64, 72). ✗

So any chord that "bridges" across chord 8 will cross it. This means chord 8 effectively "cuts" the circle, and we can only add chords entirely on one side or the other.

This is the key insight: each chord in the chain "cuts" the circle, and subsequent chords must be entirely on one side.

So the structure is: we have a sequence of nested or sequential chords, each cutting off a piece of the circle.

Let me think about this more carefully. The chain of 8 chords (blocks 0-8) uses 16 positions and creates 8 non-crossing chords. The remaining positions form 8 arcs of 6 positions each (plus the arc from position 73 to 320 and back to 1, but on the circle, the "last" arc is from after the last chord to before the first chord).

Wait, on the circle, the 8 chords divide the remaining 304 positions into 8 arcs of 6 positions each (between consecutive chords) plus 1 large arc (from after chord 8 to before chord 1, going around the circle).

The large arc: from position 73 to position 320, then to position 1. But position 1 is used by chord 1. So the arc is from position 73 to position 320 (248 positions) plus position 2 to position 8 (7 positions)... no, wait.

On the circle, the chords are (1,9), (10,18), (19,27), (28,36), (37,45), (46,54), (55,63), (64,72). These 8 chords divide the circle into 8 small arcs (each with 6 free positions) and 1 large arc.

The large arc goes from position 73 (after chord 8's right endpoint 72) around the circle to position 320, then to position 1 (chord 1's left endpoint). The free positions in this arc are 73-320, which is 248 positions = 31 blocks (blocks 9-39).

So the large arc has 31 blocks, and we can apply the same strategy recursively. f(31) = ?

If f(n) = n - 1, then f(31) = 30. Total = 8 + 30 = 38.

But wait, the large arc doesn't start at a block boundary. It starts at position 73, which is block 9, label 1. And it ends at position 320, which is block 39, label 8. Then it connects to position 1 (block 0, label 1), which is used. So the arc is positions 73-320, which is blocks 9-39, all 31 full blocks.

Actually, the arc from position 73 to position 1 (exclusive, since 1 is used) includes positions 73, 74, ..., 320. That's 320 - 73 + 1 = 248 positions = 31 blocks (blocks 9 through 39). All complete blocks.

So f(31) = 30 (if the pattern holds). Total = 8 + 30 = 38.

But 40 blocks should give 39 if f(n) = n-1. So we're losing 1 due to the gap.

Hmm, but maybe we can do better by not using the simple chain. Let me think about this differently.

Actually, let me reconsider. The chain of 8 chords uses blocks 0-8 (9 blocks) and gives 8 chords. The remaining 31 blocks give 30 chords (recursively). Total: 8 + 30 = 38. But 40 - 1 = 39. So we're 1 short.

Can we avoid losing that 1? The issue is that the chain of 8 chords "wastes" the connection between blocks 8 and 9. If we could use all 40 blocks without any gaps, we'd get 39.

Alternative strategy: Instead of using the chain of 8, use a different decomposition.

What if we use a single long chord that splits the problem into two roughly equal halves?

Chord (1, 161) [label 1, blocks 0-20, spanning 20 blocks]. This splits the circle into:
- Arc 1: positions 2-160 (blocks 0'-20, i.e., 20 full blocks minus 1 point + partial block 0)
- Arc 2: positions 162-320 (blocks 20-39, minus 1 point)

Arc 1 has 159 positions. Block 0' has positions 2-8 (7 points, labels 2-8), blocks 1-19 have 19 full blocks, and block 20 has positions 161... wait, position 161 = 8*20+1, which is used by the chord. So block 20 in arc 1 has positions 153-160 (labels 2-8, 7 points). 

Actually, let me reconsider. Arc 1 is positions 2 to 160. Block 0: positions 2-8 (labels 2-8, 7 points). Blocks 1-19: positions 9-160 (19 full blocks, 152 points). Block 20: position 161 is outside the arc. So arc 1 has 7 + 152 = 159 points, which is 19 full blocks + 2 partial blocks (7 points each).

Hmm, this is getting complicated. Let me think about it more carefully.

Actually, the partial blocks at the ends of an arc don't have all 8 labels, so they can't form chords internally. They can only form chords with other blocks in the arc.

Let me define the problem more precisely. An arc from position a to position b (on the circle, going clockwise) contains some blocks fully and two blocks partially (at the ends). The partial blocks have fewer than 8 labels available.

For the chain strategy within an arc, we need to find a sequence of labels L_1 < L_2 < ... < L_k such that each L_i is available in both of the consecutive blocks it connects.

This is getting quite complex. Let me try a different approach.

Let me think about the problem as a whole. We have 40 blocks, each with 8 points (labels 1-8). We want to select a maximum set of non-crossing chords, each connecting same-label points from different blocks.

Key insight: The non-crossing condition means that if we order the chords by their left endpoints, the right endpoints must also be in order (for non-nested chords) or in reverse order (for nested chords). Actually, for non-crossing chords on a circle, the structure is more complex, but essentially, the chords form a non-crossing matching.

Let me think about the problem as a maximum non-crossing matching on a circle with 320 points, where only same-label pairs are allowed.

This is a classic DP problem. Let me think about the DP.

dp[i][j] = maximum non-crossing same-label matching using points in the arc from position i to position j (clockwise).

Recurrence: dp[i][j] = max(
  dp[i+1][j],  // don't use point i
  max over k in (i, j] where label(i) == label(k) of 1 + dp[i+1][k-1] + dp[k+1][j]  // match i with k
)

Base case: dp[i][j] = 0 if i >= j.

The answer is dp[1][320] (or any rotation, since it's a circle).

For a circle, we need to handle the circularity. One way: fix one point, say position 1, and consider two cases: either position 1 is unmatched, or it's matched with some position k. If matched with k, the circle is split into two arcs.

This DP has O(n^2) states and O(n) transitions per state, so O(n^3) total. For n = 320, this is about 32 million, which is feasible computationally but not by hand.

Let me try to find the answer by reasoning about the structure.

Let me think about upper bounds more carefully.

Upper bound 1: Each chord uses 2 points, and there are 320 points, so at most 160 chords. But the label constraint means each chord uses 2 points of the same label, and there are 40 points per label, so at most 20 chords per label, giving at most 160. But non-crossing is more restrictive.

Upper bound 2: Consider the 40 points of label 1. They are at positions 1, 9, 17, ..., 313. These 40 points divide the circle into 40 arcs, each containing 7 points (of labels 2-8). Any chord of label 1 connects two of these 40 points and "cuts off" some arcs. Any chord of another label must be entirely within one of the arcs created by the label-1 chords.

Hmm, this is a useful way to think about it.

If we draw k chords of label 1, they divide the circle into k+1 regions (if non-crossing). Each region contains some number of the 40 arcs between consecutive label-1 points. Within each region, we can draw chords of other labels, but they must be within that region.

The 40 arcs between consecutive label-1 points each have 7 points (labels 2-8). A chord of label L (L ≠ 1) connects two points of label L, which are in different arcs (since each arc has at most one point of each label). So a chord of label L connects two arcs.

For non-crossing, chords within a region must not cross. The arcs within a region form a linear sequence (not a circle, since the region is bounded by label-1 chords). Within a region containing m arcs, we have m points of each label (one per arc), and we want a maximum non-crossing matching.

This is like the original problem but on a line (not a circle) with m "blocks" of 7 points each (labels 2-8).

Hmm, this recursive structure is interesting but complex. Let me try to compute the answer for small cases and find a pattern.

Let me define f(n, k) = max non-crossing same-label matching on a circle with n blocks of k labels each. Here n = 40, k = 8.

f(1, k) = 0 (no chord possible within 1 block)
f(2, k) = 1 (at most 1 chord between 2 blocks)
f(n, 1) = n/2 if n is even, (n-1)/2 if n is odd (all same label, just pair adjacent points)

Wait, f(n, 1) with n blocks of 1 label each: n points on a circle, all same label. Max non-crossing matching = n/2 if n even, (n-1)/2 if n odd. For n = 40, f(40, 1) = 20.

f(n, 2) with n blocks of 2 labels each: 2n points on a circle, labels alternating 1, 2, 1, 2, .... Max non-crossing matching where each chord connects same-label points.

For f(n, 2), the points of label 1 are at odd positions and label 2 at even positions. A chord of label 1 connects two odd positions, a chord of label 2 connects two even positions. Two chords cross iff their positions interleave.

f(2, 2) = 1 (2 blocks, 4 points: 1, 2, 1, 2. Chord (1, 3) or (2, 4). At most 1.)
f(3, 2) = 2 (3 blocks, 6 points: 1, 2, 1, 2, 1, 2. Chord (1, 3) and (4, 6): 1 < 3 < 4 < 6, no cross. 2 chords.)
f(4, 2) = ? (4 blocks, 8 points: 1, 2, 1, 2, 1, 2, 1, 2. Can we get 3?)

Chord (1, 3) [label 1], (4, 6) [label 2], (5, 7) [label 1]. Check: (4, 6) and (5, 7): 4 < 5 < 6 < 7. Cross! ✗

Chord (1, 3), (4, 6), (7, 1)? On circle, (7, 1) wraps. (7, 1) and (1, 3): share endpoint 1. ✗

Chord (1, 5) [label 1], (2, 4) [label 2], (6, 8) [label 2]. Check: (1, 5) and (2, 4): 1 < 2 < 4 < 5. Nested, no cross. ✓ (1, 5) and (6, 8): 1 < 5 < 6 < 8. No cross. ✓ (2, 4) and (6, 8): 2 < 4 < 6 < 8. No cross. ✓. 3 chords!

Can we get 4? 4 chords need 8 points, so all points used. Chord (1, 3) and (5, 7) [both label 1], (2, 4) and (6, 8) [both label 2]. Check: (1, 3) and (2, 4): 1 < 2 < 3 < 4. Cross! ✗

Chord (1, 7) and (3, 5) [label 1], (2, 4) and (6, 8) [label 2]. (1, 7) and (3, 5): nested, no cross. ✓ (1, 7) and (2, 4): 1 < 2 < 4 < 7. Nested, no cross. ✓ (1, 7) and (6, 8): 1 < 6 < 7 < 8. Cross! ✗

Chord (1, 7) and (3, 5) [label 1], (2, 8) and (4, 6) [label 2]. (1, 7) and (2, 8): 1 < 2 < 7 < 8. Cross! ✗

Chord (1, 3) and (5, 7) [label 1], (2, 8) and (4, 6) [label 2]. (1, 3) and (2, 8): 1 < 2 < 3 < 8. Cross! ✗

Hmm, seems hard to get 4. Let me try systematically.

All points: 1, 2, 3, 4, 5, 6, 7, 8 (labels 1, 2, 1, 2, 1, 2, 1, 2).
Label 1 points: 1, 3, 5, 7. Label 2 points: 2, 4, 6, 8.

For 4 chords, we need to pair all 8 points. Label 1: pair (1, 3) and (5, 7), or (1, 5) and (3, 7), or (1, 7) and (3, 5). Label 2: similarly.

(1, 3), (5, 7), (2, 4), (6, 8): (1,3) and (2,4) cross. ✗
(1, 3), (5, 7), (2, 6), (4, 8): (1,3) and (2,6) cross. ✗
(1, 3), (5, 7), (2, 8), (4, 6): (1,3) and (2,8) cross. ✗
(1, 5), (3, 7), (2, 4), (6, 8): (1,5) and (3,7): 1 < 3 < 5 < 7. Cross! ✗
(1, 5), (3, 7), (2, 6), (4, 8): (1,5) and (3,7) cross. ✗
(1, 5), (3, 7), (2, 8), (4, 6): (1,5) and (3,7) cross. ✗
(1, 7), (3, 5), (2, 4), (6, 8): (1,7) and (6,8) cross. ✗
(1, 7), (3, 5), (2, 6), (4, 8): (1,7) and (2,6): 1 < 2 < 6 < 7. Nested, ok. (1,7) and (4,8): 1 < 4 < 7 < 8. Cross! ✗
(1, 7), (3, 5), (2, 8), (4, 6): (1,7) and (2,8): 1 < 2 < 7 < 8. Cross! ✗

So f(4, 2) = 3. Pattern: f(n, 2) = n - 1 for n ≥ 2? f(2,2) = 1, f(3,2) = 2, f(4,2) = 3. Yes!

Let me check f(5, 2). 10 points: 1, 2, 1, 2, 1, 2, 1, 2, 1, 2.

Chain: (1, 3) [label 1], (4, 6) [label 2], (5, 7) [label 1]. (4,6) and (5,7): 4 < 5 < 6 < 7. Cross! ✗

Chain with increasing labels: (1, 3) [label 1], (4, 6) [label 2]. Then we need label > 2, but only 2 labels. So chain gives 2.

But we can do better: (1, 5) [label 1], (2, 4) [label 2], (6, 10) [label 1], (7, 9) [label 2]. Check: (1,5) and (2,4): nested. ✓ (1,5) and (6,10): 1 < 5 < 6 < 10. ✓ (1,5) and (7,9): 1 < 5 < 7 < 9. ✓ (2,4) and (6,10): 2 < 4 < 6 < 10. ✓ (2,4) and (7,9): 2 < 4 < 7 < 9. ✓ (6,10) and (7,9): 6 < 7 < 9 < 10. Nested. ✓. 4 chords!

Can we get 5? 5 chords need 10 points, all used. Label 1: 5 points (1, 3, 5, 7, 9), need to pair into 2 pairs + 1 unmatched, or... wait, 5 is odd, so at most 2 chords of label 1. Label 2: 5 points (2, 4, 6, 8, 10), at most 2 chords. Total at most 4. So f(5, 2) = 4 = 5 - 1. ✓

f(6, 2): 12 points. Label 1: 6 points, at most 3 chords. Label 2: 6 points, at most 3 chords. Total at most 6. But can we achieve 5 = 6 - 1?

(1, 5), (2, 4), (3, 7), (6, 10), (8, 12), (9, 11)? Wait, that's 6 chords. Let me check.
Label 1: (1, 5), (3, 7), (9, 11). Label 2: (2, 4), (6, 10), (8, 12).
(1, 5) and (3, 7): 1 < 3 < 5 < 7. Cross! ✗

Let me try: (1, 3), (5, 9), (7, 11) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 3) and (2, 4): 1 < 2 < 3 < 4. Cross! ✗

(1, 9), (3, 5), (7, 11) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 9) and (2, 4): nested. ✓ (1, 9) and (6, 8): nested. ✓ (1, 9) and (10, 12): 1 < 9 < 10 < 12. ✓ (1, 9) and (3, 5): nested. ✓ (1, 9) and (7, 11): 1 < 7 < 9 < 11. Cross! ✗

(1, 9), (3, 11), (5, 7) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 9) and (3, 11): 1 < 3 < 9 < 11. Cross! ✗

(1, 11), (3, 5), (7, 9) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 11) and (10, 12): 1 < 10 < 11 < 12. Cross! ✗

(1, 11), (3, 5), (7, 9) [label 1], (2, 12), (4, 6), (8, 10) [label 2].
(1, 11) and (2, 12): 1 < 2 < 11 < 12. Cross! ✗

Hmm, getting 6 seems hard. Let me try for 5.

(1, 5), (3, 9), (7, 11) [label 1], (2, 4), (6, 8) [label 2]. 5 chords.
(1, 5) and (3, 9): 1 < 3 < 5 < 9. Cross! ✗

(1, 5), (2, 4), (3, 9), (6, 8), (7, 11) [label 1: 1,3,7; label 2: 2,6; wait, (3, 9) is label 1, (6, 8) is label 2, (7, 11) is label 1].
(1, 5) and (3, 9): cross. ✗

(1, 3), (2, 4), (5, 9), (6, 8), (7, 11) [label 1: (1,3), (5,9), (7,11); label 2: (2,4), (6,8)].
(1, 3) and (2, 4): cross. ✗

(1, 3), (5, 7), (9, 11) [label 1], (2, 4), (6, 8), (10, 12) [label 2]. 6 chords.
(1, 3) and (2, 4): cross. ✗

It seems like any pairing of adjacent same-label points causes crosses with the other label. Let me try a different approach.

(1, 7), (3, 5) [label 1], (2, 6), (4, 12), (8, 10) [label 2]. 5 chords.
(1, 7) and (2, 6): 1 < 2 < 6 < 7. Nested. ✓
(1, 7) and (3, 5): nested. ✓
(1, 7) and (4, 12): 1 < 4 < 7 < 12. Cross! ✗

(1, 7), (3, 5) [label 1], (2, 6), (4, 8), (10, 12) [label 2]. 5 chords.
(1, 7) and (4, 8): 1 < 4 < 7 < 8. Cross! ✗

(1, 7), (3, 5), (9, 11) [label 1], (2, 6), (8, 12) [label 2]. 5 chords.
(1, 7) and (2, 6): nested. ✓
(1, 7) and (8, 12): 1 < 7 < 8 < 12. ✓
(1, 7) and (9, 11): 1 < 7 < 9 < 11. ✓
(1, 7) and (3, 5): nested. ✓
(3, 5) and (2, 6): 2 < 3 < 5 < 6. Cross! ✗

(1, 7), (3, 5), (9, 11) [label 1], (2, 8), (6, 12) [label 2]. 5 chords.
Wait, (2, 8) is label 2, (6, 12) is label 2. 
(1, 7) and (2, 8): 1 < 2 < 7 < 8        — AI历史解题过程（thinking）
#   polymath_02850         — 题目ID

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
  <problem_id>polymath_02850</problem_id>
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

Let there be 320 points arranged on a circle, labeled \(1, 2, 3, \ldots, 8, 1, 2, 3, \ldots, 8, \ldots\) in order. Line segments may only be drawn to connect points labeled with the same number. What is the largest number of non-intersecting line segments one can draw? (Two segments sharing the same endpoint are considered to be intersecting).

## Standard Solution

Let us label the points \(p_{1}, \ldots, p_{320}\). Consider the shortest line segment \(p_{a} p_{b}\). There are no lines from points on the smaller sector of the circle defined by this line, \(p \in \{p_{a+1}, p_{a+2}, \ldots, p_{b-1}\}\). Assuming the contrary, if there is a line from \(p\), any line \(pq\) must be in the same sector, as otherwise \(pq\) will intersect \(p_{a} p_{b}\), which is contradictory.

Since there are no points between \(p_{a}\) and \(p_{b}\), we can effectively remove this section, leaving the points \(p_{1}, \ldots, p_{a}, p_{b+1}, \ldots, p_{320}\). Since \(a \equiv b \pmod{8}\), some \(8k\) points are removed, for \(k \in \mathbb{N}\). We now consider the shortest line in the remaining set of points. After recursive removal of at least 8 points for each line removed, we can remove at most 39 such lines, leaving 8 points \(1, 2, \ldots, 8\) on which no further removal is possible.

We see that 39 is possible, with line segments between \(p_{4k}\) and \(p_{320-4k}\) for \(k = \{1, \ldots, 39\}\).

\(\boxed{39}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have 320 points on a circle, labeled 1,2,3,...,8,1,2,3,...,8,... in order. So 320/8 = 40 points with each label. So there are 40 points labeled 1, 40 labeled 2, ..., 40 labeled 8.

Line segments may only be drawn to connect points with the same label. So we can only draw chords connecting two points with the same number. We want the maximum number of non-intersecting line segments (chords), where two segments sharing an endpoint are also considered intersecting.

So essentially, for each label i (1 to 8), we have 40 points on the circle, and we can draw non-intersecting chords among these 40 points. But chords from different labels can also intersect each other! So we need to consider the global constraint.

Wait, let me think about this more carefully. The points are arranged on a circle with labels 1,2,3,...,8 repeating. So the positions are:
Position 1: label 1
Position 2: label 2
...
Position 8: label 8
Position 9: label 1
Position 10: label 2
...
Position 320: label 8

So there are 40 points of each label, evenly spaced (every 8th position).

A chord connects two points with the same label. Two chords intersect if they cross each other inside the circle, or if they share an endpoint.

Since each point can be used at most once (sharing endpoint = intersecting), each point is in at most one chord.

So we're selecting a set of chords (each connecting two same-labeled points) such that no two chords cross and no two share an endpoint. Maximize the number of chords.

Total points = 320, so at most 160 chords (if we could pair everything). But the constraint is that chords can only connect same-label points, and chords can't cross.

Let me think about this as a non-crossing matching problem.

For a single label with 40 points on a circle, the maximum non-crossing matching pairs up to 20 chords (pairing all 40 points in a non-crossing way, e.g., adjacent pairs). But here the 40 points of a given label are interspersed with points of other labels.

The key constraint: chords from different labels can cross each other. So we need to find a global non-crossing set of chords where each chord connects same-label points.

Let me think of this differently. We have 320 points on a circle. We want to select a set of non-crossing chords where each chord connects two points of the same label. Each point used at most once.

This is like a non-crossing matching problem with color constraints.

Let me think about upper bounds. 

One approach: Consider the structure. The points are arranged in 40 blocks of 8 consecutive points (labels 1-8). 

Let me think about what non-crossing chords look like. A set of non-crossing chords on a circle forms a planar structure. 

Key insight: If we have a non-crossing set of chords, we can think of them as dividing the circle into regions. 

Let me think about small cases first. 

Consider a simpler version: 2n points on a circle, labeled 1,2,...,k repeating. What's the max non-crossing same-label matching?

Actually, let me think about this problem more carefully.

Let me consider the problem as follows. We have 320 points on a circle. A chord between positions i and j (same label) divides the remaining points into two arcs. For non-crossing, any other chord must have both endpoints on the same arc (or be nested).

This is essentially a maximum non-crossing matching with the constraint that matched pairs must have the same label.

This can be solved with dynamic programming, but 320 points is large. Let me think about the structure.

Let me think about it differently. Consider the 40 points of label 1. They are at positions 1, 9, 17, 25, ..., 313. These are equally spaced (every 8 positions). Similarly for each label.

Now, a chord connecting two points of the same label, say label 1 at positions 1 and 9, is a short chord. A chord connecting positions 1 and 313 is a long chord.

For non-crossing matchings, short chords are generally better because they "use up" less of the circle.

Let me think about the maximum. 

Upper bound: Each label has 40 points, so at most 20 chords per label, giving at most 160 total. But chords from different labels cross, so we can't achieve this.

Let me think about which chords can coexist.

Consider two labels, say label 1 and label 2. The points of label 1 are at positions 1, 9, 17, ... and label 2 at positions 2, 10, 18, .... A chord of label 1 connecting positions a and b, and a chord of label 2 connecting positions c and d, cross if and only if the positions interleave (a < c < b < d or c < a < d < b, considering circular order).

Let me think about a specific strategy. What if we only use "short" chords connecting adjacent same-label points?

For label 1: positions 1, 9, 17, 25, ..., 313. Adjacent pairs: (1,9), (17,25), (33,41), ..., (305,313). That's 20 chords. But do these cross chords from other labels?

A chord (1,9) of label 1 spans positions 2,3,4,5,6,7,8 (the interior). A chord of label 2, say (2,10), spans positions 3,4,5,6,7,8,9. Do (1,9) and (2,10) cross? Position order: 1, 2, 9, 10. So 1 < 2 < 9 < 10, which means they interleave: 1 < 2 < 9 < 10. Yes, they cross!

So we can't use both (1,9) for label 1 and (2,10) for label 2.

Hmm, this is more constrained than I thought.

Let me reconsider. The points are at positions 1 through 320 on a circle. Label at position i is ((i-1) mod 8) + 1.

A chord from position i to position j (same label) and a chord from position k to position l (same label, possibly different) cross iff the four positions are distinct and interleave around the circle.

Since same-label points are 8 apart, the shortest chord for any label spans 8 positions (connecting position i and i+8, going through 7 intermediate positions).

Let me think about the problem differently. 

Consider the 320 points. Let's think about which pairs of same-label points can be connected without crossing.

Actually, let me think about this problem as a maximum independent set in a circle graph, but that's NP-hard in general. However, the special structure here might help.

Let me reconsider. The problem is to find a maximum non-crossing matching where each matched pair has the same label. This is actually solvable in polynomial time using DP on intervals.

For n points on a circle, the DP is: dp[i][j] = max non-crossing matching using points in the arc from i to j. The recurrence is:
dp[i][j] = max(dp[i+1][j], max over k in (i,j] where label(i)==label(k) of 1 + dp[i+1][k-1] + dp[k+1][j])

But with 320 points, this is O(320^3) which is about 32 million, feasible computationally. But I need to solve this by hand...

Let me think about the structure more.

The labels repeat with period 8. So position i has label ((i-1) mod 8) + 1. Two positions have the same label iff they differ by a multiple of 8.

So a chord connects positions i and j where j - i ≡ 0 (mod 8), i.e., j = i + 8m for some positive integer m.

The chord (i, i+8m) divides the circle into two arcs: one of length 8m-1 (positions i+1 to i+8m-1) and one of length 320-8m-1 (positions i+8m+1 to i-1, wrapping around).

For two chords to not cross, they must be "nested" or in separate arcs.

Let me think about the problem structure. 

Consider the 40 "blocks" of 8 consecutive points. Block b (for b = 0, 1, ..., 39) contains positions 8b+1, 8b+2, ..., 8b+8, with labels 1, 2, ..., 8 respectively.

A chord connects two positions with the same label, which are in blocks that differ by some amount. Specifically, position 8b + L (label L) can connect to position 8b' + L (same label L) for any b ≠ b'.

The chord from block b to block b' (with label L) spans all blocks between b and b' (in one direction).

Now, for non-crossing chords, if we have a chord from block b to block b' (spanning blocks b+1, ..., b'-1 in between), then any other chord must either be entirely within blocks b+1 to b'-1, or entirely outside (in the complementary arc).

This is like a non-crossing matching on 40 blocks, but within each block, we can use at most one chord endpoint (since each position is used at most once, and each block has one position per label).

Wait, actually each block has 8 positions (one per label), and each position can be used at most once. So from each block, we can use up to 8 positions (one per label), but each position is used in at most one chord.

Hmm, let me reconsider. Each block has 8 points, one of each label. A chord uses 2 points (of the same label) from 2 different blocks. Each point is used at most once.

So the question is: select a set of non-crossing chords, each connecting same-label points from different blocks, maximizing the total number of chords.

Let me think about this as follows. Consider the 40 blocks arranged in a circle. A chord connects block b to block b' using label L (both blocks have a point with label L). Two chords cross if their block-pairs interleave on the circle of blocks.

But wait, it's more subtle because within a block, the 8 points are at different positions, so the crossing condition depends on the exact positions, not just the blocks.

Actually, let me reconsider. Two chords (i, j) and (k, l) with i < j and k < l cross iff i < k < j < l or k < i < l < j (in linear order, assuming no wrapping). On a circle, we need to be more careful, but the idea is the same.

Since the points within a block are at consecutive positions, the crossing condition does depend on the exact positions.

Let me think about this more carefully with a specific example.

Chord A: connects position 8b+L to position 8b'+L (label L, blocks b and b').
Chord B: connects position 8c+M to position 8c'+M (label M, blocks c and c').

Assume b < b' and c < c' (in terms of block order, and the chords go "forward"). The positions are:
A: 8b+L to 8b'+L
B: 8c+M to 8c'+M

For them to cross (in the linear sense, assuming no wrapping around the circle), we need one endpoint of B between the endpoints of A and the other outside.

This is getting complicated. Let me try a different approach.

Let me think about the problem as a DP on the circle of 320 points.

Actually, let me try to think about it more cleverly.

Key observation: The labels repeat with period 8. So the configuration has a rotational symmetry of order 8 (shifting by 8 positions maps label 1 to label 1, etc., but shifts the blocks).

Wait, no. Shifting by 8 positions maps position i to position i+8, which has the same label. So the configuration is invariant under rotation by 8 positions (i.e., by 1 block). This means the problem has a 40-fold rotational symmetry (by blocks).

Hmm, but that doesn't directly help with the optimization.

Let me try to think about upper and lower bounds.

Lower bound: Can we achieve some number of chords?

Strategy 1: Use only chords within consecutive blocks. For example, connect position 8b+L to position 8(b+1)+L for each b and L. But these chords would cross each other (as we saw, (1,9) and (2,10) cross).

Actually wait. Let me reconsider. Position 1 (label 1, block 0) to position 9 (label 1, block 1). Position 2 (label 2, block 0) to position 10 (label 2, block 1). These chords: (1,9) and (2,10). In the circle, positions 1, 2, 9, 10 appear in order 1, 2, 9, 10. So 1 < 2 < 9 < 10, meaning chord (1,9) separates 2 from 10, so they cross. Yes, they cross.

So we can't use all 8 labels between the same pair of consecutive blocks.

Strategy 2: What if we pair up blocks and use only one label per pair?

If we pair block 0 with block 1 using label 1 (chord from pos 1 to pos 9), and pair block 2 with block 3 using label 1 (chord from pos 17 to pos 25), etc., then these chords don't cross (they're in disjoint arcs). We get 20 chords (from 40 blocks paired into 20 pairs, each pair using 1 chord).

But we can do better. Within each pair of consecutive blocks, we could potentially use more than one label if the chords don't cross.

Wait, chords (1,9) [label 1] and (3,11) [label 3]: positions 1, 3, 9, 11 in order 1, 3, 9, 11. Chord (1,9) separates 3 from 11, so they cross. So any two chords between the same pair of consecutive blocks will cross (since the positions interleave).

So between any pair of consecutive blocks, we can use at most 1 chord.

What about non-consecutive blocks? Chord from block 0 to block 2 (skipping block 1). E.g., position 1 (label 1, block 0) to position 17 (label 1, block 2). This spans blocks 0, 1, 2. Inside, we could have chords entirely within block 1 (but a chord needs two points of the same label, and block 1 has only one point per label, so no chord within a single block). Or chords within the arc from position 2 to position 16.

Hmm, this is getting complex. Let me think about it differently.

Let me reformulate: We have 320 points on a circle. We want a maximum non-crossing matching where each matched pair has the same label (same residue mod 8).

I think the answer might be 40. Let me think about why.

Actually, let me think about a cleaner approach. Consider the 320 points. Any non-crossing matching on a circle with n points has at most n/2 edges. Here n = 320, so at most 160. But the label constraint reduces this.

Let me think about the problem as follows. Consider the dual perspective: instead of thinking about which chords to draw, think about which points are unmatched.

In a non-crossing matching on a circle, the unmatched points and the chords form a non-crossing structure. 

Let me try to think about small cases and find a pattern.

Small case: 2 blocks (16 points), labels 1-8, 1-8. What's the max non-crossing same-label matching?

Points: 1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8 (positions 1-16).

Possible chords: (1,9), (2,10), (3,11), (4,12), (5,13), (6,14), (7,15), (8,16) — each connecting same label across the two blocks.

Any two of these cross (as argued above, positions interleave). So max is 1 chord.

With 2 blocks, max = 1.

Small case: 3 blocks (24 points). Labels: 1-8, 1-8, 1-8.

Possible chords: within blocks 0-1, blocks 1-2, blocks 0-2, or blocks 0-2 wrapping around.

Chords between blocks 0 and 1: (1,9), (2,10), ..., (8,16). At most 1 (they all cross each other).
Chords between blocks 1 and 2: (9,17), (10,18), ..., (16,24). At most 1.
Chords between blocks 0 and 2: (1,17), (2,18), ..., (8,24). At most 1 (they all cross each other).

Can we have 2 non-crossing chords? E.g., (1,9) [blocks 0-1, label 1] and (10,18) [blocks 1-2, label 2]. Positions: 1, 9, 10, 18. Chord (1,9) and (10,18): 1 < 9 < 10 < 18, so they don't interleave — they don't cross! But wait, position 9 and 10 are in the same block (block 1). Chord (1,9) uses position 9, and chord (10,18) uses position 10. These are different positions, so no shared endpoint. And they don't cross. So we can have 2 chords.

Can we have 3? We'd need 3 non-crossing chords. Let's try (1,9), (10,18), and something in the remaining arc. After drawing (1,9) and (10,18), the remaining points are: 2,3,4,5,6,7,8 (between 1 and 9, exclusive), 11,12,13,14,15,16 (between 10 and 18, exclusive), and 19,20,21,22,23,24 (between 18 and 1, wrapping around). 

In the arc 2-8 (block 0 minus position 1), we have labels 2,3,4,5,6,7,8 — all different, no same-label pair. Similarly for other arcs. So no more chords can be added. Max = 2 for 3 blocks.

Hmm wait, but we could also try chords that span multiple blocks. Let me try (1,17) [blocks 0-2, label 1] and (9,10)... no, 9 and 10 have different labels. 

What about (2,10) [label 2, blocks 0-1] and (17, 25)? No, we only have 3 blocks (24 points), so position 25 doesn't exist.

Let me try (1,17) [label 1, blocks 0-2] — this spans the entire circle almost. Then inside the arc from 2 to 16, we have blocks 0 (positions 2-8), 1 (positions 9-16). Same labels: position 2 (label 2) and position 10 (label 2), etc. We can draw one chord in this arc, say (2,10). Then inside the arc from 3 to 9, we have labels 3,4,5,6,7,8,1 — all different. And inside the arc from 11 to 16, labels 3,4,5,6,7,8 — all different. So max 2 chords.

In the complementary arc (positions 18-24, i.e., block 2 minus position 17), labels 2,3,4,5,6,7,8 — all different, no chord.

So with 3 blocks, max = 2.

Pattern so far: 2 blocks → 1, 3 blocks → 2. Let me check 4 blocks.

4 blocks (32 points). Labels: 1-8 repeated 4 times.

Can we get 4? Let's try: (1,9) [label 1, blocks 0-1], (10,18) [label 2, blocks 1-2], (19,27) [label 3, blocks 2-3]. These are non-crossing (each is in a disjoint arc region). Wait, let me check: (1,9) and (10,18): 1 < 9 < 10 < 18, no cross. (10,18) and (19,27): 10 < 18 < 19 < 27, no cross. (1,9) and (19,27): 1 < 9 < 19 < 27, no cross. 

Can we add a 4th? Remaining positions: 2-8, 11-17, 20-26, 28-32. In each of these arcs, all labels are distinct (each arc is a subset of a single block minus one position). So no more chords. Max = 3? 

Wait, but what about the arc from 28 to 1 (wrapping around)? Positions 28-32: labels 4,5,6,7,8. All distinct. And position 1 is used. So no chord there.

Hmm, but what if we use a different strategy? What about (1,25) [label 1, blocks 0-3, spanning 3 blocks], and then chords inside?

(1,25): spans positions 2-24. Inside, we have blocks 0 (pos 2-8), 1 (pos 9-16), 2 (pos 17-24). This is like the 3-block problem, which gives 2 chords. Plus the complementary arc (positions 26-32): labels 2,3,4,5,6,7,8 — no chord. So total 3.

What about (1,17) [label 1, blocks 0-2] and (25, 9)? No, that wraps around. Let me think on the circle.

On the circle, (1,17) divides into arcs: 2-16 and 18-320... wait, we only have 32 points. Arcs: 2-16 and 18-32,1 (wrapping). In arc 2-16 (blocks 0 minus pos 1, and block 1): this is like 2 blocks minus 1 point. Labels: 2,3,4,5,6,7,8,1,2,3,4,5,6,7,8. Same labels: (2,10), (3,11), ..., (8,16). But these all cross each other, so at most 1. In arc 18-32 (block 2 minus pos 17, and block 3): labels 2,3,4,5,6,7,8,1,2,3,4,5,6,7,8. Same: at most 1 chord. So total 3.

Hmm, seems like 4 blocks give 3. Pattern: n blocks → n-1?

Let me verify with 2 blocks: 2-1 = 1. ✓. 3 blocks: 3-1 = 2. ✓. 4 blocks: 4-1 = 3. ✓.

If this pattern holds, 40 blocks → 39.

But wait, let me check if we can do better with 4 blocks. 

What about using chords that don't span exactly 1 block? 

Let me try: (1,9) [label 1, blocks 0-1], (17,25) [label 1, blocks 2-3]. These don't cross (1 < 9 < 17 < 25). Can we add more? In arc 2-8: no same-label pairs. In arc 10-16: labels 2,3,4,5,6,7,8,1 — all distinct. In arc 18-24: labels 2,3,4,5,6,7,8,1 — all distinct. In arc 26-32: labels 2,3,4,5,6,7,8 — all distinct. So total 2. Worse.

What about (2,10) [label 2, blocks 0-1], (3,11) [label 3, blocks 0-1]? These cross (2 < 3 < 10 < 11). So no.

What about (1,9) [label 1, blocks 0-1], (18,26) [label 2, blocks 2-3], and something in between? Arc 10-17: labels 2,3,4,5,6,7,8,1 — all distinct. Arc 19-25: labels 3,4,5,6,7,8,1 — all distinct. Arc 27-32,1: labels 3,4,5,6,7,8 — distinct. Arc 2-8: distinct. So total 2.

What about (1,17) [label 1, blocks 0-2], (18, 26) [label 2, blocks 2-3]? Positions: 1, 17, 18, 26. 1 < 17 < 18 < 26, no cross. Arc 2-16: 2 blocks minus 1 point, at most 1 chord. Arc 19-25: distinct. Arc 27-32: distinct. Total: 1 + 1 + 1 = 3.

What about (1,9) [label 1], (10,18) [label 2], (19,27) [label 3], (28, 4)? Position 28 is label 4, position 4 is label 4. But 28 > 4, so on the circle, this chord wraps around. (28, 4) and (1, 9): on the circle, 28, 1, 4, 9 — does (28,4) separate 1 from 9? The arc from 28 to 4 (going forward) includes 29,30,31,32,1,2,3,4. So 1 is inside this arc but 9 is outside. So (28,4) and (1,9) cross. So this doesn't work.

What if instead of (28,4), we use (4, 28)? Same chord, same crossing issue.

Hmm. What about (1,9), (10,18), (19,27), and (28, 36)? But we only have 32 points (4 blocks), so position 36 doesn't exist.

So for 4 blocks, max seems to be 3.

Let me try 5 blocks (40 points). Can we get 5?

(1,9) [label 1, blocks 0-1], (10,18) [label 2, blocks 1-2], (19,27) [label 3, blocks 2-3], (28,36) [label 4, blocks 3-4]. These are all non-crossing. Can we add a 5th? Remaining arcs: 2-8 (distinct), 11-17 (distinct), 20-26 (distinct), 29-35 (distinct), 37-40 (labels 5,6,7,8 — distinct). So total 4. 

Can we do better with 5 blocks? Let me try a different strategy.

(1,17) [label 1, blocks 0-2], (18,34) [label 2, blocks 2-4]. Positions: 1, 17, 18, 34. No cross. Arc 2-16: 2 blocks minus 1 point → 1 chord. Arc 19-33: 2 blocks minus 1 point → 1 chord. Arc 35-40,1: labels 3,4,5,6,7,8 — distinct. Total: 1 + 1 + 1 + 1 = 4.

What about (1,33) [label 1, blocks 0-4, spanning 4 blocks]? Arc 2-32: 4 blocks minus 1 point. This is like 4 blocks with one point removed. Hmm, this is getting complicated.

Let me try to think about it more carefully. With 5 blocks, can we get 5?

Let me try: (1,9) [label 1], (10,18) [label 2], (19,27) [label 3], (28,36) [label 4], (37, 5) [label 5, wrapping]. (37,5) wraps around: arc from 37 to 5 includes 38,39,40,1,2,3,4,5. Does (37,5) cross (1,9)? 1 is in the arc 37-5, and 9 is outside. So yes, they cross. Doesn't work.

What about (37, 45)? Only 40 points, so no.

What if we use (40, 8) [label 8, blocks 4-0, wrapping]? Arc from 40 to 8 includes 1,2,...,8. Does this cross (1,9)? 1 is in the arc, 9 is outside. Cross. Doesn't work.

So with the "chain" strategy, we get 4 for 5 blocks. Can we do better?

Let me try: (1,25) [label 1, blocks 0-3], (26,34) [label 2, blocks 3-4]. No cross (1 < 25 < 26 < 34). Arc 2-24: 3 blocks minus 1 point. Arc 27-33: 1 block minus 1 point, distinct. Arc 35-40: distinct. Arc 2-24: this is blocks 0 (pos 2-8), 1 (pos 9-16), 2 (pos 17-24), which is like 3 blocks → 2 chords. Total: 1 + 2 + 1 = 4.

What about (1,17) [label 1, blocks 0-2], (18,26) [label 2, blocks 2-3], (27,35) [label 3, blocks 3-4]? No crosses. Arc 2-16: 2 blocks minus 1 point → 1. Arc 19-25: 1 block minus 1 point → 0. Arc 28-34: 1 block minus 1 point → 0. Arc 36-40: distinct. Total: 1 + 1 + 1 + 0 = 3. Worse.

What about (1,17) [label 1, blocks 0-2], (18,34) [label 2, blocks 2-4]? Arc 2-16: 2 blocks minus 1 → 1. Arc 19-33: 2 blocks minus 1 → 1. Arc 35-40: distinct. Total: 1 + 1 + 1 = 3. Wait, I think I miscounted. (1,17) is 1 chord, plus 1 in arc 2-16, plus 1 in arc 19-33, plus 0 in arc 35-40 = 3. But earlier I said 4. Let me recheck.

Oh wait, I think I need to be more careful. (1,17) and (18,34): positions 1, 17, 18, 34. 1 < 17 < 18 < 34. No cross. Arc 2-16: positions 2-16, which is block 0 (pos 2-8) and block 1 (pos 9-16). This is 2 full blocks minus nothing (wait, position 1 is used by the first chord, position 17 is used by the first chord). So arc 2-16 has 15 points: labels 2,3,4,5,6,7,8,1,2,3,4,5,6,7,8. Same-label pairs: (2,10), (3,11), ..., (8,16), and also (1 is at position 9, but there's no other 1 in this arc... wait, position 9 has label 1, and there's no other label 1 in positions 2-16 except position 9. So the same-label pairs are (2,10), (3,11), (4,12), (5,13), (6,14), (7,15), (8,16). These all cross each other, so at most 1.

Arc 19-33: positions 19-33, which is block 2 (pos 19-24, labels 3,4,5,6,7,8) and block 3 (pos 25-32, labels 1,2,3,4,5,6,7,8) and position 33 (label 1, block 4). Wait, I have 5 blocks (40 points). Block 3 is positions 25-32, block 4 is positions 33-40.

Arc 19-33: positions 19-33. Labels: 3,4,5,6,7,8 (block 2, pos 19-24), 1,2,3,4,5,6,7,8 (block 3, pos 25-32), 1 (block 4, pos 33). Same-label pairs: (3, 27), (4, 28), (5, 29), (6, 30), (7, 31), (8, 32), (1, 33). Wait, position 25 has label 1, position 33 has label 1. So (25, 33) is a pair. And (3, 27): position 19 has label 3, position 27 has label 3. Yes. Etc.

But all these chords span from block 2 to block 3 (or block 3 to block 4 for (25,33)). They would all cross each other (same issue as before). So at most 1.

Actually wait, (25, 33) goes from block 3 to block 4, while (19, 27) goes from block 2 to block 3. Do they cross? Positions 19, 25, 27, 33: 19 < 25 < 27 < 33. Chord (19,27) separates 25 from 33, so yes they cross.

What about (19, 27) and (26, 34)? But 34 is outside the arc 19-33. So (26,34) is not in this arc.

OK so arc 19-33 gives at most 1 chord.

Arc 35-40: positions 35-40, labels 3,4,5,6,7,8. All distinct. 0 chords.

Total: 1 (chord (1,17)) + 1 (arc 2-16) + 1 (arc 19-33) + 0 = 3. 

Hmm, but earlier with (1,25) and (26,34), I got 4. Let me recheck that.

(1,25) [label 1, blocks 0-3], (26,34) [label 2, blocks 3-4]. 
Arc 2-24: positions 2-24, blocks 0 (pos 2-8), 1 (pos 9-16), 2 (pos 17-24). 3 full blocks. This is the 3-block problem → 2 chords.
Arc 27-33: positions 27-33, labels 3,4,5,6,7,8 (block 3, pos 27-32) and 1 (block 4, pos 33). All distinct. 0 chords.
Arc 35-40: labels 3,4,5,6,7,8. Distinct. 0.
Total: 1 + 1 + 2 + 0 + 0 = 4. Yes, 4.

Can we do 5 with 5 blocks? Let me think harder.

What about (1,9) [label 1, blocks 0-1], (10,26) [label 2, blocks 1-3], (27,35) [label 3, blocks 3-4]?
Positions: 1, 9, 10, 26, 27, 35. No crosses (1 < 9 < 10 < 26 < 27 < 35).
Arc 2-8: distinct. 0.
Arc 11-25: positions 11-25, block 1 (pos 11-16, labels 3,4,5,6,7,8) and block 2 (pos 17-24, labels 1,2,3,4,5,6,7,8) and position 25 (label 1, block 3). Same-label pairs: (3,19), (4,20), (5,21), (6,22), (7,23), (8,24), (1, 25), (2, 18). Wait, position 18 has label 2, and is there another 2? Position 10 has label 2 but it's used. So in arc 11-25: labels are 3,4,5,6,7,8,1,2,3,4,5,6,7,8,1. Same pairs: (3,19), (4,20), (5,21), (6,22), (7,23), (8,24), (17,25) [both label 1]. These all cross each other, so at most 1.
Arc 28-34: positions 28-34, labels 4,5,6,7,8 (block 3) and 1,2 (block 4). Distinct. 0.
Arc 36-40: distinct. 0.
Total: 1 + 1 + 1 + 0 + 0 + 0 = 3. Worse.

What about (1,17) [label 1, blocks 0-2], (2,10) [label 2, blocks 0-1]? These cross: 1 < 2 < 17, and 10 is between 2 and 17. So 1 < 2 < 10 < 17, chord (1,17) separates 2 from 10. Cross. Doesn't work.

What about (1,17) [label 1, blocks 0-2], (18, 2) [label 2, wrapping]? (18,2) wraps around: arc from 18 to 2 includes 19,...,40,1,2. Does (1,17) cross (18,2)? 1 is in arc 18-2, 17 is outside. Cross. Doesn't work.

Hmm, it seems hard to get more than 4 with 5 blocks. Let me try another approach.

(1,9) [label 1], (17,25) [label 1, blocks 2-3], (26,34) [label 2, blocks 3-4]. No crosses. Arc 2-8: 0. Arc 10-16: 0. Arc 18-24: 0. Arc 27-33: 0. Arc 35-40: 0. Total: 3. Worse.

(1,9) [label 1], (10,18) [label 2], (19,27) [label 3], (28,36) [label 4]. 4 chords. Can we squeeze in a 5th? All remaining arcs have distinct labels. So 4.

What if we don't use the chain strategy? Let me try:

(1,25) [label 1, blocks 0-3], (2,10) [label 2, blocks 0-1]. Cross? 1 < 2 < 10 < 25. Chord (1,25) separates 2 from 10. Cross. No.

(1,25) [label 1], (26,34) [label 2], (35, 3) [label 3, wrapping]. (35,3) wraps: arc 35-3 includes 36,...,40,1,2,3. Does it cross (1,25)? 1 is in arc 35-3, 25 is outside. Cross. No.

(1,25) [label 1], (26,34) [label 2]. Arc 2-24: 3 blocks → 2 chords. Arc 27-33: 0. Arc 35-40: 0. Total: 4.

What about (1,33) [label 1, blocks 0-4]? This spans almost the entire circle. Arc 2-32: 4 blocks minus 1 point. This is like 4 blocks with position 1 removed from block 0. So blocks 0' (pos 2-8), 1 (pos 9-16), 2 (pos 17-24), 3 (pos 25-32). 4 full blocks → 3 chords. Arc 34-40: labels 2,3,4,5,6,7,8. 0. Total: 1 + 3 = 4.

Hmm, so 5 blocks consistently gives 4. The pattern n blocks → n-1 seems to hold.

Wait, but let me double-check with a different approach for 5 blocks. What about using longer chords creatively?

(1,17) [label 1, blocks 0-2], (25,33) [label 1, blocks 3-4]. No cross (1 < 17 < 25 < 33). Arc 2-16: 2 blocks minus 1 → 1. Arc 18-24: block 2 minus pos 17, labels 2,3,4,5,6,7,8. 0. Arc 26-32: block 3 minus pos 25, labels 2,3,4,5,6,7,8. 0. Arc 34-40: labels 2,3,4,5,6,7,8. 0. Total: 1 + 1 + 0 + 0 + 0 = 2. Worse.

OK so it really seems like n blocks → n-1 chords. For 40 blocks, that would be 39.

But wait, I should check this more carefully. Let me think about why n-1 is the answer and whether we can do better.

Actually, let me reconsider. With the chain strategy, we get n-1 by using chords (1,9), (10,18), (19,27), ..., (8(n-2)+1, 8(n-1)+1). Wait, let me be more precise.

For n blocks, the chain strategy: 
- Chord 1: (1, 9) [label 1, blocks 0-1]
- Chord 2: (10, 18) [label 2, blocks 1-2]
- Chord 3: (19, 27) [label 3, blocks 2-3]
- ...
- Chord k: (8(k-1)+k', 8k+k') where k' = ((k-1) mod 8) + 1

Wait, let me be more careful. Chord i connects block i-1 to block i, using label i (for i = 1, 2, ..., n-1). But labels go from 1 to 8, so for i > 8, we'd use label ((i-1) mod 8) + 1.

Chord i: position 8(i-1) + L_i to position 8i + L_i, where L_i = ((i-1) mod 8) + 1.

For i = 1: L_1 = 1, positions 1 and 9. ✓
For i = 2: L_2 = 2, positions 10 and 18. ✓
For i = 3: L_3 = 3, positions 19 and 27. ✓
...
For i = 8: L_8 = 8, positions 57 and 65. ✓
For i = 9: L_9 = 1, positions 65 and 73. But position 65 is used by chord 8! Conflict!

So the chain strategy breaks at i = 9 because position 65 (label 8, block 8) is used by chord 8, and chord 9 also wants to use position 65 (label 1, block 8)... wait, no. Position 65 = 8*8 + 1, which has label 1, not label 8. Let me recalculate.

Block 8 is positions 65-72. Position 65 has label 1, position 66 has label 2, ..., position 72 has label 8.

Chord 8: L_8 = 8, positions 8*7 + 8 = 64 and 8*8 + 8 = 72. So positions 64 and 72.
Chord 9: L_9 = 1, positions 8*8 + 1 = 65 and 8*9 + 1 = 73. So positions 65 and 73.

Position 64 (block 7, label 8) and position 72 (block 8, label 8) for chord 8.
Position 65 (block 8, label 1) and position 73 (block 9, label 1) for chord 9.

These use different positions (64, 72, 65, 73 are all distinct). And do they cross? 64 < 65 < 72 < 73. Chord (64, 72) separates 65 from 73. Cross!

So the chain strategy fails at i = 9 because chords 8 and 9 cross.

Hmm, so the simple chain strategy doesn't directly give n-1 for n > 8. Let me reconsider.

The issue is that when we use label 8 for chord 8 (connecting blocks 7-8) and label 1 for chord 9 (connecting blocks 8-9), the positions interleave: 64, 65, 72, 73.

So we need a different strategy for larger n.

Let me reconsider. The chain strategy works for the first 8 chords (using labels 1 through 8), but then we need to handle the crossing issue.

What if we use a different pattern? For example, use only odd labels for the chain? Or use a different assignment?

Actually, the issue is that consecutive chords in the chain use consecutive blocks and consecutive labels, and the positions interleave.

Let me think about this differently. Two chords (a, b) and (c, d) with a < b, c < d, and a < c (WLOG) don't cross iff c > b or d < b (i.e., they're disjoint or nested). Wait no, on a line: they don't cross iff b < c or d < a or (a < c < d < b) [nested] or (c < a < b < d) [nested]. On a circle it's more complex.

For the chain strategy, chords (8(i-1)+L_i, 8i+L_i) and (8j+L_j, 8(j+1)+L_j) with j = i+1:
- First chord: (8(i-1)+L_i, 8i+L_i)
- Second chord: (8i+L_{i+1}, 8(i+1)+L_{i+1})

These don't cross iff 8i + L_i < 8i + L_{i+1}, i.e., L_i < L_{i+1}. Since L_i = ((i-1) mod 8) + 1, we have L_{i+1} = (i mod 8) + 1. So L_i < L_{i+1} iff ((i-1) mod 8) < (i mod 8), which is true iff i mod 8 ≠ 0, i.e., i is not a multiple of 8.

So the chain works for chords 1-8 (i=1 to 7 transitions are fine), but fails at the transition from chord 8 to chord 9 (i=8, which is a multiple of 8, so L_8 = 8 > L_9 = 1).

So the chain gives 8 chords for the first 8 transitions, then breaks. We need to handle the "wrap" at every 8th transition.

One idea: at the wrap, instead of using a chord between blocks 8 and 9, skip it and use a chord between blocks 8 and 10 or something.

Alternatively, we could use a different label assignment that avoids the wrap issue.

What if we use the same label for all chords? E.g., all chords use label 1.

Chord i: (8(i-1)+1, 8i+1) for i = 1, 2, ..., n-1. These are (1,9), (9,17), (17,25), ... But position 9 is shared between chord 1 and chord 2! So they share an endpoint, which counts as intersecting. Doesn't work.

What if we use label 1 for odd chords and label 2 for even chords?
Chord 1: (1, 9) [label 1]
Chord 2: (10, 18) [label 2]
Chord 3: (17, 25) [label 1]
Chord 4: (26, 34) [label 2]

Check crossings: (1,9) and (10,18): 1 < 9 < 10 < 18. No cross. (10,18) and (17,25): 10 < 17 < 18 < 25. Chord (10,18) separates 17 from 25. Cross!

So that doesn't work either.

The issue is that when we use label 1 for chord 3 (blocks 2-3), the positions are 17 and 25, which interleave with chord 2's positions 10 and 18.

Let me think about this more carefully. The key constraint is that for two consecutive chords in the chain (between blocks i, i+1 and blocks i+1, i+2), the label of the first chord must be less than the label of the second chord (to avoid crossing).

So we need a sequence of labels L_1, L_2, ..., L_{n-1} (each in {1,...,8}) such that L_1 < L_2 < ... < L_{n-1}. But this means we can have at most 8 chords in such a chain (since labels are 1 to 8).

After 8 chords, we need to "reset." How?

One approach: after 8 chords (using labels 1 through 8), the 8th chord connects blocks 7-8 using label 8 (positions 64 and 72). Now, for the next chord, we can't use the chain between blocks 8-9 because any label would cause a crossing with chord 8 (since we'd need L_9 > L_8 = 8, which is impossible).

Instead, we could use a chord that "jumps over" block 8. For example, a chord from block 7 to block 9 (skipping block 8). But block 7's position for any label is already used by chord 8 (which uses position 64, label 8). So we could use a different label for block 7.

Wait, chord 8 uses positions 64 (block 7, label 8) and 72 (block 8, label 8). So block 7 still has positions 57-63 available (labels 1-7), and block 8 has positions 65-71 available (labels 1-7).

What if we use a chord from block 6 to block 9? Block 6 has positions 49-56 (labels 1-8), but position 56 (label 8) is used by chord 7 (which connects blocks 6-7 using label 7, positions 55 and 63). Wait, let me recalculate.

Chord 7: L_7 = 7, positions 8*6+7 = 55 and 8*7+7 = 63. So positions 55 (block 6, label 7) and 63 (block 7, label 7).

So block 6 has positions 49-56, with position 55 used. Block 7 has positions 57-64, with positions 63 and 64 used (by chords 7 and 8). Block 8 has positions 65-72, with position 72 used (by chord 8).

This is getting complicated. Let me think about the problem differently.

Let me think about it as a global optimization problem. 

Alternative approach: Think of the 320 points on the circle. We want a maximum non-crossing matching with same-label constraint.

Key insight: A non-crossing matching on a circle can be decomposed into "non-crossing" structures. The maximum non-crossing matching on n points (without label constraint) is n/2 (pair adjacent points). With the label constraint, we need to be more careful.

Let me think about an upper bound. 

Consider the 320 points. In any non-crossing matching, the chords divide the circle into regions. Each chord "uses up" some arc of the circle.

Upper bound idea: Consider any arc of 8 consecutive points (one block). These 8 points all have different labels. A chord using any of these points must connect to a point outside this block (same label). So each chord "crosses" the boundary of this block.

Hmm, this doesn't directly give a bound.

Let me think about it differently. 

Consider the 40 points of label 1, at positions 1, 9, 17, ..., 313. These divide the circle into 40 arcs, each of length 8 (containing 7 interior points). A chord of label 1 connects two of these 40 points. A chord of any other label connects two points within these arcs.

Actually, I think the key insight is about the structure of non-crossing matchings on a circle.

Let me think about the problem as follows. We have 320 points. A non-crossing matching pairs up some of them. The unmatched points are "free." The matching is non-crossing, so it forms a planar structure.

For the label constraint: each matched pair must have the same label.

Let me think about the maximum. 

Claim: The answer is 40.

Wait, let me reconsider. With n blocks, I was getting n-1 for small cases. But the chain strategy breaks at 8. Let me re-examine.

For n = 9 blocks (72 points), the chain gives 8 chords (labels 1-8, blocks 0-8). Can we do better?

After the 8 chords, the used positions are:
Chord 1: 1, 9 (label 1)
Chord 2: 10, 18 (label 2)
Chord 3: 19, 27 (label 3)
Chord 4: 28, 36 (label 4)
Chord 5: 37, 45 (label 5)
Chord 6: 46, 54 (label 6)
Chord 7: 55, 63 (label 7)
Chord 8: 64, 72 (label 8)

Used positions: 1, 9, 10, 18, 19, 27, 28, 36, 37, 45, 46, 54, 55, 63, 64, 72.
Free positions: 2-8, 11-17, 20-26, 29-35, 38-44, 47-53, 56-62, 65-71.

Each free arc (between consecutive used positions) has 6 or 7 points, all with distinct labels. So no more chords can be added.

But can we do better than 8 for 9 blocks? Let me try a different strategy.

What if we use a "nested" strategy? For example:
- Chord A: (1, 65) [label 1, blocks 0-8, spanning 8 blocks]
- Inside arc 2-64: 8 blocks minus 1 point. This is like 8 blocks with one point removed.
- Inside arc 66-72: 7 points, distinct labels. 0 chords.

For the 8 blocks minus 1 point (arc 2-64): blocks 0' (pos 2-8, labels 2-8), 1 (pos 9-16), 2 (pos 17-24), ..., 7 (pos 57-64). This is 7 full blocks plus a partial block. Hmm, this is like 8 blocks but block 0 is missing label 1.

The chain strategy on this: we need labels that are strictly increasing. We have 7 full blocks (1-7) and a partial block 0 (labels 2-8). 

Actually, let me think about this differently. The arc 2-64 has 63 points. The blocks are:
- Block 0': positions 2-8 (labels 2,3,4,5,6,7,8) — 7 points
- Block 1: positions 9-16 (labels 1,2,3,4,5,6,7,8) — 8 points
- Block 2: positions 17-24 — 8 points
- ...
- Block 7: positions 57-64 — 8 points

Total: 7 + 7*8 = 7 + 56 = 63 points.

For the chain strategy within this arc, we can use chords between consecutive blocks. The first chord could be between block 0' and block 1. Block 0' has labels 2-8, block 1 has labels 1-8. We need a label present in both, and the chord positions must not cross with subsequent chords.

If we use label 2: chord (2, 10). Then the next chord between blocks 1 and 2 must use label > 2, say label 3: (19, 27). Then label 4: (28, 36), ..., label 8: (64, 72)... wait, position 72 is outside the arc 2-64. Block 7 is positions 57-64. So the chord between blocks 6 and 7 using label 8 would be (56, 64). But position 56 is in block 6 (label 8), and position 64 is in block 7 (label 8). 

Wait, let me redo this. The arc is 2-64. Blocks within this arc:
- Block 0': pos 2-8 (labels 2-8)
- Block 1: pos 9-16 (labels 1-8)
- Block 2: pos 17-24
- Block 3: pos 25-32
- Block 4: pos 33-40
- Block 5: pos 41-48
- Block 6: pos 49-56
- Block 7: pos 57-64

Chain: 
Chord 1: block 0' to block 1, label 2: (2, 10)
Chord 2: block 1 to block 2, label 3: (19, 27)
Chord 3: block 2 to block 3, label 4: (28, 36)
Chord 4: block 3 to block 4, label 5: (37, 45)
Chord 5: block 4 to block 5, label 6: (46, 54)
Chord 6: block 5 to block 6, label 7: (55, 63)
Chord 7: block 6 to block 7, label 8: (64, 72)... 

Wait, position 72 is outside the arc. Block 7 is positions 57-64. The chord between block 6 and block 7 using label 8 would be position 56 (block 6, label 8) to position 64 (block 7, label 8). So (56, 64). 

But wait, chord 6 uses position 55 (block 5, label 7) and position 63 (block 7, label 7). Chord 7 uses position 56 (block 6, label 8) and position 64 (block 7, label 8). Do they cross? 55 < 56 < 63 < 64. Chord (55, 63) separates 56 from 64. Cross!

Hmm, so the chain breaks again at the transition from label 7 to label 8. Wait, 55 < 56, and 63 < 64, so 55 < 56 < 63 < 64. Chord (55,63) and (56,64): 55 < 56 < 63 < 64, so they interleave. Cross.

But this is the same issue: L_7 = 7 < L_8 = 8, so 55 < 56 (since 8*6+7 = 55 < 8*6+8 = 56) and 63 < 64 (8*7+7 = 63 < 8*7+8 = 64). So 55 < 56 < 63 < 64, which means they cross.

Wait, I think I made an error earlier. Let me recheck the chain for the original problem.

Chord 7: L_7 = 7, positions 8*6+7 = 55 and 8*7+7 = 63.
Chord 8: L_8 = 8, positions 8*7+8 = 64 and 8*8+8 = 72.

55 < 64? Yes. 63 < 64? Yes. So 55 < 63 < 64 < 72. No interleaving. They don't cross!

Wait, I need to check more carefully. Chord 7 is (55, 63) and chord 8 is (64, 72). 55 < 63 < 64 < 72. These are disjoint intervals, so they don't cross. ✓

But in my nested example, chord 6 was (55, 63) and chord 7 was (56, 64). 55 < 56 < 63 < 64. These interleave, so they cross. ✗

The difference is that in the original chain, chord 7 uses label 7 (positions 55, 63) and chord 8 uses label 8 (positions 64, 72). The positions are 55, 63, 64, 72 — no interleaving because 63 < 64.

In the nested example, chord 6 uses label 7 (positions 55, 63) and chord 7 uses label 8 (positions 56, 64). The positions are 55, 56, 63, 64 — interleaving because 55 < 56 < 63 < 64.

The issue is that in the nested example, the blocks are shifted. Block 6 in the nested example is positions 49-56, and block 7 is positions 57-64. So label 8 in block 6 is position 56, and label 8 in block 7 is position 64. But label 7 in block 5 is position 55, and label 7 in block 7 is position 63. So the chord (55, 63) for label 7 goes from block 5 to block 7, and (56, 64) for label 8 goes from block 6 to block 7. These interleave.

Wait, I think I messed up the nested chain. Let me redo it.

In the nested example, the arc is 2-64. The blocks are:
- Block 0': pos 2-8 (labels 2-8)
- Block 1: pos 9-16
- Block 2: pos 17-24
- Block 3: pos 25-32
- Block 4: pos 33-40
- Block 5: pos 41-48
- Block 6: pos 49-56
- Block 7: pos 57-64

Chain chords (between consecutive blocks):
Chord 1: block 0' to block 1, label 2: (2, 10)
Chord 2: block 1 to block 2, label 3: (19, 27)
Chord 3: block 2 to block 3, label 4: (28, 36)
Chord 4: block 3 to block 4, label 5: (37, 45)
Chord 5: block 4 to block 5, label 6: (46, 54)
Chord 6: block 5 to block 6, label 7: (55, 63)

Wait, block 5 is positions 41-48, label 7 is position 47. Block 6 is positions 49-56, label 7 is position 55. So chord 6 is (47, 55), not (55, 63).

Let me recalculate. Position in block b with label L is 8b + L.
- Block 0': positions 2-8, but these are positions 8*0 + L for L = 2, 3, ..., 8. So position 2 = 8*0+2, position 8 = 8*0+8.
- Block 1: positions 9-16 = 8*1 + L for L = 1, ..., 8. Position 9 = 8*1+1, position 16 = 8*1+8.
- Block 5: positions 41-48 = 8*5 + L. Position 47 = 8*5+7, position 48 = 8*5+8.
- Block 6: positions 49-56 = 8*6 + L. Position 55 = 8*6+7, position 56 = 8*6+8.
- Block 7: positions 57-64 = 8*7 + L. Position 63 = 8*7+7, position 64 = 8*7+8.

Chord 6: block 5 to block 6, label 7: (47, 55). 
Chord 7: block 6 to block 7, label 8: (56, 64).

47 < 55 < 56 < 64. No interleaving. They don't cross! ✓

I made an error earlier. Let me redo the full chain for the nested example.

Chord 1: (2, 10) — label 2, blocks 0'-1
Chord 2: (19, 27) — label 3, blocks 1-2
Chord 3: (28, 36) — label 4, blocks 2-3
Chord 4: (37, 45) — label 5, blocks 3-4
Chord 5: (46, 54) — label 6, blocks 4-5
Chord 6: (47, 55) — label 7, blocks 5-6

Wait, chord 5 is (46, 54) and chord 6 is (47, 55). 46 < 47 < 54 < 55. Interleaving! Cross!

Hmm, so the chain breaks at the transition from label 6 to label 7 here. Let me recheck.

Chord 5: block 4 to block 5, label 6: position 8*4+6 = 38 and 8*5+6 = 46. So (38, 46).
Chord 6: block 5 to block 6, label 7: position 8*5+7 = 47 and 8*6+7 = 55. So (47, 55).

38 < 46 < 47 < 55. No interleaving. ✓

I keep making arithmetic errors. Let me be very careful.

Chord i (for the nested chain): connects block (i-1) to block i, using label (i+1) (since we start from label 2).

Chord 1: block 0 to block 1, label 2: pos 8*0+2 = 2, pos 8*1+2 = 10. (2, 10).
Chord 2: block 1 to block 2, label 3: pos 8*1+3 = 11, pos 8*2+3 = 19. (11, 19).
Chord 3: block 2 to block 3, label 4: pos 8*2+4 = 20, pos 8*3+4 = 28. (20, 28).
Chord 4: block 3 to block 4, label 5: pos 8*3+5 = 29, pos 8*4+5 = 37. (29, 37).
Chord 5: block 4 to block 5, label 6: pos 8*4+6 = 38, pos 8*5+6 = 46. (38, 46).
Chord 6: block 5 to block 6, label 7: pos 8*5+7 = 47, pos 8*6+7 = 55. (47, 55).
Chord 7: block 6 to block 7, label 8: pos 8*6+8 = 56, pos 8*7+8 = 64. (56, 64).

Check non-crossing:
(2,10) and (11,19): 2 < 10 < 11 < 19. ✓
(11,19) and (20,28): 11 < 19 < 20 < 28. ✓
(20,28) and (29,37): 20 < 28 < 29 < 37. ✓
(29,37) and (38,46): 29 < 37 < 38 < 46. ✓
(38,46) and (47,55): 38 < 46 < 47 < 55. ✓
(47,55) and (56,64): 47 < 55 < 56 < 64. ✓

All non-crossing! So the nested chain gives 7 chords in the arc 2-64, plus the outer chord (1, 65), total 8 chords for 9 blocks.

But wait, the original chain (without nesting) also gave 8 chords for 9 blocks. So nesting doesn't help here.

Hmm, but can we do better than 8 for 9 blocks? Let me think...

Actually, let me reconsider the original chain for 9 blocks.

Original chain:
Chord 1: (1, 9) — label 1
Chord 2: (10, 18) — label 2
Chord 3: (19, 27) — label 3
Chord 4: (28, 36) — label 4
Chord 5: (37, 45) — label 5
Chord 6: (46, 54) — label 6
Chord 7: (55, 63) — label 7
Chord 8: (64, 72) — label 8

Check: (55, 63) and (64, 72): 55 < 63 < 64 < 72. ✓. All good. 8 chords.

Can we add a 9th? Free positions: 2-8, 11-17, 20-26, 29-35, 38-44, 47-53, 56-62, 65-71. Each arc has 7 points with distinct labels. No more chords. So 8 is the max for 9 blocks with this strategy.

Can we do better with a different strategy for 9 blocks? Let me try:

(1, 65) [label 1, blocks 0-8], and then 7 chords in arc 2-64 (as computed above). Total 8. Same.

What about (1, 33) [label 1, blocks 0-4] and (34, 66) [label 2, blocks 4-8]?
Arc 2-32: 4 blocks minus 1 point → 3 chords (chain with labels 2-4... wait, 4 blocks minus 1 point).

Hmm, let me think about this recursively. Let f(n) = max chords for n blocks.

f(1) = 0 (only 1 block, 8 points, all different labels, no chord possible)
f(2) = 1
f(3) = 2
f(4) = 3
f(5) = 4
...
f(8) = 7
f(9) = 8

It looks like f(n) = n - 1. But wait, does this hold for larger n?

For n = 10, the chain gives 8 chords (labels 1-8, blocks 0-8), and then we're stuck. Can we get 9?

After the 8 chords, the free positions in block 8 are 65-71 (labels 1-7), and block 9 is positions 73-80 (labels 1-8). Can we add a chord between block 8 and block 9?

The last chord is (64, 72) [label 8, blocks 7-8]. A new chord between blocks 8 and 9 would be (8*8+L, 8*9+L) = (72+L, 80+L) for some label L. But position 72 is used, so L ≠ 8 (since 72+8 = 80, but 72 is used). For L = 1: (73, 81). 64 < 72 < 73 < 81. No cross with (64, 72). ✓

But wait, does (73, 81) cross any earlier chord? The earlier chords are (1,9), (10,18), ..., (64,72). (73, 81) is after all of them: 72 < 73. So no cross. ✓

So we can add chord 9: (73, 81) [label 1, blocks 8-9]. But does this cross chord 1: (1, 9)? On the circle, (1, 9) and (73, 81): 1 < 9 < 73 < 81. No cross (disjoint arcs). ✓

So for 10 blocks, we get 9 chords! The chain continues: (73, 81) [label 1], (82, 90) [label 2], etc.

Wait, but (73, 81) uses label 1, and the previous chord (64, 72) uses label 8. 64 < 72 < 73 < 81. No cross. ✓

Then chord 10: (82, 90) [label 2, blocks 9-10]. 73 < 81 < 82 < 90. No cross with (73, 81). ✓

So the chain continues! The "break" at label 8 to label 1 doesn't actually cause a crossing because the positions are far apart (72 < 73).

Wait, I think I was wrong earlier about the chain breaking. Let me recheck.

The chain is:
Chord i: (8(i-1) + L_i, 8i + L_i) where L_i = ((i-1) mod 8) + 1.

Chord 8: (8*7 + 8, 8*8 + 8) = (64, 72). L_8 = 8.
Chord 9: (8*8 + 1, 8*9 + 1) = (65, 73). L_9 = 1.

64 < 65 < 72 < 73. Chord (64, 72) and (65, 73): 64 < 65 < 72 < 73. Interleaving! Cross!

So the chain DOES break at the transition from chord 8 to chord 9. I was right the first time.

But then how did I get (73, 81) to work? Because (73, 81) is not the chain chord 9. The chain chord 9 would be (65, 73), which crosses chord 8. But (73, 81) is a different chord — it connects blocks 8 and 9 using label 1, but it starts at position 73 (block 9, label 1) and goes to position 81 (block 10, label 1). Wait, that's blocks 9-10, not blocks 8-9!

Oh I see, I skipped the connection between blocks 8 and 9, and instead connected blocks 9 and 10. So the chain is:
Chords 1-8: blocks 0-1, 1-2, ..., 7-8 (labels 1-8)
Chord 9: blocks 9-10 (label 1) — skipping the blocks 8-9 connection!

So we skip one connection (blocks 8-9) and lose one potential chord. For 10 blocks, we get 8 chords from blocks 0-8, then skip blocks 8-9, then 1 chord from blocks 9-10. Total: 9. But we could have gotten 9 = 10 - 1 if the pattern f(n) = n-1 holds.

Wait, 10 blocks, 9 chords. That's still n-1 = 9. But the chain skipped one connection. Let me see if we can recover that lost connection.

After the 8 chords (blocks 0-8) and the chord (73, 81) (blocks 9-10), the free positions in block 8 are 65-71 (labels 1-7), and in block 9 are 74-80 (labels 2-8). Can we add a chord between block 8 and block 9?

A chord (65+L-1, 73+L-1) for label L, i.e., (8*8+L, 8*9+L) for L in {1,...,7} (since position 73 is used by chord 9, and position 72 is used by chord 8).

For L = 1: (65, 73). But 73 is used. ✗
For L = 2: (66, 74). Check crossing with (64, 72): 64 < 66 < 72 < 74. Interleaving! Cross. ✗
For L = 3: (67, 75). 64 < 67 < 72 < 75. Cross. ✗
...
For L = 7: (71, 79). 64 < 71 < 72 < 79. Cross. ✗

All chords between blocks 8 and 9 cross chord 8 (64, 72). So we can't add any chord between blocks 8 and 9.

What about a chord from block 8 to block 10 (or further)? (65, 81) [label 1]: but 81 is used by chord 9. (66, 82) [label 2]: 64 < 66 < 72 < 82. Cross with chord 8. ✗.

What about a chord from block 7 to block 9? (57+L, 73+L) for some L. Position 57+L must be free. Block 7 free positions: 57-62 (labels 1-6, since 63 and 64 are used). 
(57, 73) [label 1]: 73 is used. ✗
(58, 74) [label 2]: 55 < 58 < 63 < 74. Cross with chord 7 (55, 63). ✗
...

All cross chord 7. So no.

What about a chord entirely within the free positions of blocks 8-9? The free positions are 65-71 (block 8, labels 1-7) and 74-80 (block 9, labels 2-8). Same labels: label 2 (pos 66, 74), label 3 (pos 67, 75), ..., label 7 (pos 71, 79). But all these chords cross chord 8 (64, 72) as shown above. So no.

What about a chord from block 8 to somewhere after block 10? (65, 89) [label 1, blocks 8-11]: 64 < 65 < 72 < 89. Cross with chord 8. ✗.

So it seems like once we have the 8-chord chain (blocks 0-8), the block 8 is "blocked" by chord 8, and we can't use any chord that starts in block 8 (before position 72) and ends after position 72.

So the effective strategy is: chain of 8 chords (blocks 0-8), then skip to blocks 9+, and repeat.

For 40 blocks:
- Blocks 0-8: 8 chords (labels 1-8)
- Blocks 9-17: 8 chords (labels 1-8)
- Blocks 18-26: 8 chords
- Blocks 27-35: 8 chords
- Blocks 36-39: 3 chords (labels 1-3, blocks 36-37, 37-38, 38-39)

Wait, but between the groups, we skip one connection (blocks 8-9, 17-18, 26-27, 35-36). So:

Group 1: blocks 0-8, 8 chords
Gap: blocks 8-9, 0 chords
Group 2: blocks 9-17, 8 chords
Gap: blocks 17-18, 0 chords
Group 3: blocks 18-26, 8 chords
Gap: blocks 26-27, 0 chords
Group 4: blocks 27-35, 8 chords
Gap: blocks 35-36, 0 chords
Remaining: blocks 36-39, 3 chords (labels 1-3)

Total: 8 + 8 + 8 + 8 + 3 = 35 chords.

But wait, can we do better? The gaps waste potential connections. Let me think about whether we can avoid the gaps.

The gap occurs because the chain uses labels 1-8 in order, and the transition from label 8 to label 1 causes a crossing. What if we use a different label order?

For example, what if we use labels in the order 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, ...? The idea is to go up and then down.

But the constraint is L_i < L_{i+1} for non-crossing. If we go 1, 2, ..., 8, then we need L_9 > 8, which is impossible. If we go 8, 7, ..., 1, then we need L_2 < 8, which is fine, but then L_9 < 1, impossible.

What if we go 1, 2, 3, 4, 5, 6, 7, 8, then 1, 2, ...? The transition 8 → 1 causes a crossing. But what if we insert a "reset" chord that doesn't follow the chain?

Actually, let me think about this differently. The constraint for consecutive chain chords (between blocks i, i+1 and blocks i+1, i+2) is that L_i < L_{i+1} (to avoid crossing). This means the labels must be strictly increasing, so we can have at most 8 consecutive chain chords.

But what if we don't use consecutive blocks? What if we skip a block?

For example, after 8 chords (blocks 0-8), instead of connecting blocks 8-9, we connect blocks 7-9 or blocks 8-10.

Chord from block 7 to block 9: (8*7+L, 8*9+L) = (56+L, 72+L). But position 63 (block 7, label 7) and 64 (block 7, label 8) are used. So L ∈ {1,...,6}. 

(57, 73) [label 1]: 55 < 57 < 63 < 73. Cross with chord 7 (55, 63). ✗
(58, 74) [label 2]: 55 < 58 < 63 < 74. Cross. ✗
...
(62, 78) [label 6]: 55 < 62 < 63 < 78. Cross. ✗

All cross chord 7. ✗

What about block 6 to block 9? (49+L, 72+L). Block 6 used positions: 55 (label 7), 56 (label 8). So L ∈ {1,...,6}.
(49, 73) [label 1]: 46 < 49 < 54 < 73. Cross with chord 6 (46, 54). ✗
...

All cross chord 6. ✗

It seems like any chord starting before position 64 (the start of chord 8) and ending after position 72 (the end of chord 8) will cross chord 8 or one of the earlier chords.

What about a chord from block 8 to block 10? (65, 81) [label 1]: 64 < 65 < 72 < 81. Cross with chord 8 (64, 72). ✗

So any chord that "bridges" across chord 8 will cross it. This means chord 8 effectively "cuts" the circle, and we can only add chords entirely on one side or the other.

This is the key insight: each chord in the chain "cuts" the circle, and subsequent chords must be entirely on one side.

So the structure is: we have a sequence of nested or sequential chords, each cutting off a piece of the circle.

Let me think about this more carefully. The chain of 8 chords (blocks 0-8) uses 16 positions and creates 8 non-crossing chords. The remaining positions form 8 arcs of 6 positions each (plus the arc from position 73 to 320 and back to 1, but on the circle, the "last" arc is from after the last chord to before the first chord).

Wait, on the circle, the 8 chords divide the remaining 304 positions into 8 arcs of 6 positions each (between consecutive chords) plus 1 large arc (from after chord 8 to before chord 1, going around the circle).

The large arc: from position 73 to position 320, then to position 1. But position 1 is used by chord 1. So the arc is from position 73 to position 320 (248 positions) plus position 2 to position 8 (7 positions)... no, wait.

On the circle, the chords are (1,9), (10,18), (19,27), (28,36), (37,45), (46,54), (55,63), (64,72). These 8 chords divide the circle into 8 small arcs (each with 6 free positions) and 1 large arc.

The large arc goes from position 73 (after chord 8's right endpoint 72) around the circle to position 320, then to position 1 (chord 1's left endpoint). The free positions in this arc are 73-320, which is 248 positions = 31 blocks (blocks 9-39).

So the large arc has 31 blocks, and we can apply the same strategy recursively. f(31) = ?

If f(n) = n - 1, then f(31) = 30. Total = 8 + 30 = 38.

But wait, the large arc doesn't start at a block boundary. It starts at position 73, which is block 9, label 1. And it ends at position 320, which is block 39, label 8. Then it connects to position 1 (block 0, label 1), which is used. So the arc is positions 73-320, which is blocks 9-39, all 31 full blocks.

Actually, the arc from position 73 to position 1 (exclusive, since 1 is used) includes positions 73, 74, ..., 320. That's 320 - 73 + 1 = 248 positions = 31 blocks (blocks 9 through 39). All complete blocks.

So f(31) = 30 (if the pattern holds). Total = 8 + 30 = 38.

But 40 blocks should give 39 if f(n) = n-1. So we're losing 1 due to the gap.

Hmm, but maybe we can do better by not using the simple chain. Let me think about this differently.

Actually, let me reconsider. The chain of 8 chords uses blocks 0-8 (9 blocks) and gives 8 chords. The remaining 31 blocks give 30 chords (recursively). Total: 8 + 30 = 38. But 40 - 1 = 39. So we're 1 short.

Can we avoid losing that 1? The issue is that the chain of 8 chords "wastes" the connection between blocks 8 and 9. If we could use all 40 blocks without any gaps, we'd get 39.

Alternative strategy: Instead of using the chain of 8, use a different decomposition.

What if we use a single long chord that splits the problem into two roughly equal halves?

Chord (1, 161) [label 1, blocks 0-20, spanning 20 blocks]. This splits the circle into:
- Arc 1: positions 2-160 (blocks 0'-20, i.e., 20 full blocks minus 1 point + partial block 0)
- Arc 2: positions 162-320 (blocks 20-39, minus 1 point)

Arc 1 has 159 positions. Block 0' has positions 2-8 (7 points, labels 2-8), blocks 1-19 have 19 full blocks, and block 20 has positions 161... wait, position 161 = 8*20+1, which is used by the chord. So block 20 in arc 1 has positions 153-160 (labels 2-8, 7 points). 

Actually, let me reconsider. Arc 1 is positions 2 to 160. Block 0: positions 2-8 (labels 2-8, 7 points). Blocks 1-19: positions 9-160 (19 full blocks, 152 points). Block 20: position 161 is outside the arc. So arc 1 has 7 + 152 = 159 points, which is 19 full blocks + 2 partial blocks (7 points each).

Hmm, this is getting complicated. Let me think about it more carefully.

Actually, the partial blocks at the ends of an arc don't have all 8 labels, so they can't form chords internally. They can only form chords with other blocks in the arc.

Let me define the problem more precisely. An arc from position a to position b (on the circle, going clockwise) contains some blocks fully and two blocks partially (at the ends). The partial blocks have fewer than 8 labels available.

For the chain strategy within an arc, we need to find a sequence of labels L_1 < L_2 < ... < L_k such that each L_i is available in both of the consecutive blocks it connects.

This is getting quite complex. Let me try a different approach.

Let me think about the problem as a whole. We have 40 blocks, each with 8 points (labels 1-8). We want to select a maximum set of non-crossing chords, each connecting same-label points from different blocks.

Key insight: The non-crossing condition means that if we order the chords by their left endpoints, the right endpoints must also be in order (for non-nested chords) or in reverse order (for nested chords). Actually, for non-crossing chords on a circle, the structure is more complex, but essentially, the chords form a non-crossing matching.

Let me think about the problem as a maximum non-crossing matching on a circle with 320 points, where only same-label pairs are allowed.

This is a classic DP problem. Let me think about the DP.

dp[i][j] = maximum non-crossing same-label matching using points in the arc from position i to position j (clockwise).

Recurrence: dp[i][j] = max(
  dp[i+1][j],  // don't use point i
  max over k in (i, j] where label(i) == label(k) of 1 + dp[i+1][k-1] + dp[k+1][j]  // match i with k
)

Base case: dp[i][j] = 0 if i >= j.

The answer is dp[1][320] (or any rotation, since it's a circle).

For a circle, we need to handle the circularity. One way: fix one point, say position 1, and consider two cases: either position 1 is unmatched, or it's matched with some position k. If matched with k, the circle is split into two arcs.

This DP has O(n^2) states and O(n) transitions per state, so O(n^3) total. For n = 320, this is about 32 million, which is feasible computationally but not by hand.

Let me try to find the answer by reasoning about the structure.

Let me think about upper bounds more carefully.

Upper bound 1: Each chord uses 2 points, and there are 320 points, so at most 160 chords. But the label constraint means each chord uses 2 points of the same label, and there are 40 points per label, so at most 20 chords per label, giving at most 160. But non-crossing is more restrictive.

Upper bound 2: Consider the 40 points of label 1. They are at positions 1, 9, 17, ..., 313. These 40 points divide the circle into 40 arcs, each containing 7 points (of labels 2-8). Any chord of label 1 connects two of these 40 points and "cuts off" some arcs. Any chord of another label must be entirely within one of the arcs created by the label-1 chords.

Hmm, this is a useful way to think about it.

If we draw k chords of label 1, they divide the circle into k+1 regions (if non-crossing). Each region contains some number of the 40 arcs between consecutive label-1 points. Within each region, we can draw chords of other labels, but they must be within that region.

The 40 arcs between consecutive label-1 points each have 7 points (labels 2-8). A chord of label L (L ≠ 1) connects two points of label L, which are in different arcs (since each arc has at most one point of each label). So a chord of label L connects two arcs.

For non-crossing, chords within a region must not cross. The arcs within a region form a linear sequence (not a circle, since the region is bounded by label-1 chords). Within a region containing m arcs, we have m points of each label (one per arc), and we want a maximum non-crossing matching.

This is like the original problem but on a line (not a circle) with m "blocks" of 7 points each (labels 2-8).

Hmm, this recursive structure is interesting but complex. Let me try to compute the answer for small cases and find a pattern.

Let me define f(n, k) = max non-crossing same-label matching on a circle with n blocks of k labels each. Here n = 40, k = 8.

f(1, k) = 0 (no chord possible within 1 block)
f(2, k) = 1 (at most 1 chord between 2 blocks)
f(n, 1) = n/2 if n is even, (n-1)/2 if n is odd (all same label, just pair adjacent points)

Wait, f(n, 1) with n blocks of 1 label each: n points on a circle, all same label. Max non-crossing matching = n/2 if n even, (n-1)/2 if n odd. For n = 40, f(40, 1) = 20.

f(n, 2) with n blocks of 2 labels each: 2n points on a circle, labels alternating 1, 2, 1, 2, .... Max non-crossing matching where each chord connects same-label points.

For f(n, 2), the points of label 1 are at odd positions and label 2 at even positions. A chord of label 1 connects two odd positions, a chord of label 2 connects two even positions. Two chords cross iff their positions interleave.

f(2, 2) = 1 (2 blocks, 4 points: 1, 2, 1, 2. Chord (1, 3) or (2, 4). At most 1.)
f(3, 2) = 2 (3 blocks, 6 points: 1, 2, 1, 2, 1, 2. Chord (1, 3) and (4, 6): 1 < 3 < 4 < 6, no cross. 2 chords.)
f(4, 2) = ? (4 blocks, 8 points: 1, 2, 1, 2, 1, 2, 1, 2. Can we get 3?)

Chord (1, 3) [label 1], (4, 6) [label 2], (5, 7) [label 1]. Check: (4, 6) and (5, 7): 4 < 5 < 6 < 7. Cross! ✗

Chord (1, 3), (4, 6), (7, 1)? On circle, (7, 1) wraps. (7, 1) and (1, 3): share endpoint 1. ✗

Chord (1, 5) [label 1], (2, 4) [label 2], (6, 8) [label 2]. Check: (1, 5) and (2, 4): 1 < 2 < 4 < 5. Nested, no cross. ✓ (1, 5) and (6, 8): 1 < 5 < 6 < 8. No cross. ✓ (2, 4) and (6, 8): 2 < 4 < 6 < 8. No cross. ✓. 3 chords!

Can we get 4? 4 chords need 8 points, so all points used. Chord (1, 3) and (5, 7) [both label 1], (2, 4) and (6, 8) [both label 2]. Check: (1, 3) and (2, 4): 1 < 2 < 3 < 4. Cross! ✗

Chord (1, 7) and (3, 5) [label 1], (2, 4) and (6, 8) [label 2]. (1, 7) and (3, 5): nested, no cross. ✓ (1, 7) and (2, 4): 1 < 2 < 4 < 7. Nested, no cross. ✓ (1, 7) and (6, 8): 1 < 6 < 7 < 8. Cross! ✗

Chord (1, 7) and (3, 5) [label 1], (2, 8) and (4, 6) [label 2]. (1, 7) and (2, 8): 1 < 2 < 7 < 8. Cross! ✗

Chord (1, 3) and (5, 7) [label 1], (2, 8) and (4, 6) [label 2]. (1, 3) and (2, 8): 1 < 2 < 3 < 8. Cross! ✗

Hmm, seems hard to get 4. Let me try systematically.

All points: 1, 2, 3, 4, 5, 6, 7, 8 (labels 1, 2, 1, 2, 1, 2, 1, 2).
Label 1 points: 1, 3, 5, 7. Label 2 points: 2, 4, 6, 8.

For 4 chords, we need to pair all 8 points. Label 1: pair (1, 3) and (5, 7), or (1, 5) and (3, 7), or (1, 7) and (3, 5). Label 2: similarly.

(1, 3), (5, 7), (2, 4), (6, 8): (1,3) and (2,4) cross. ✗
(1, 3), (5, 7), (2, 6), (4, 8): (1,3) and (2,6) cross. ✗
(1, 3), (5, 7), (2, 8), (4, 6): (1,3) and (2,8) cross. ✗
(1, 5), (3, 7), (2, 4), (6, 8): (1,5) and (3,7): 1 < 3 < 5 < 7. Cross! ✗
(1, 5), (3, 7), (2, 6), (4, 8): (1,5) and (3,7) cross. ✗
(1, 5), (3, 7), (2, 8), (4, 6): (1,5) and (3,7) cross. ✗
(1, 7), (3, 5), (2, 4), (6, 8): (1,7) and (6,8) cross. ✗
(1, 7), (3, 5), (2, 6), (4, 8): (1,7) and (2,6): 1 < 2 < 6 < 7. Nested, ok. (1,7) and (4,8): 1 < 4 < 7 < 8. Cross! ✗
(1, 7), (3, 5), (2, 8), (4, 6): (1,7) and (2,8): 1 < 2 < 7 < 8. Cross! ✗

So f(4, 2) = 3. Pattern: f(n, 2) = n - 1 for n ≥ 2? f(2,2) = 1, f(3,2) = 2, f(4,2) = 3. Yes!

Let me check f(5, 2). 10 points: 1, 2, 1, 2, 1, 2, 1, 2, 1, 2.

Chain: (1, 3) [label 1], (4, 6) [label 2], (5, 7) [label 1]. (4,6) and (5,7): 4 < 5 < 6 < 7. Cross! ✗

Chain with increasing labels: (1, 3) [label 1], (4, 6) [label 2]. Then we need label > 2, but only 2 labels. So chain gives 2.

But we can do better: (1, 5) [label 1], (2, 4) [label 2], (6, 10) [label 1], (7, 9) [label 2]. Check: (1,5) and (2,4): nested. ✓ (1,5) and (6,10): 1 < 5 < 6 < 10. ✓ (1,5) and (7,9): 1 < 5 < 7 < 9. ✓ (2,4) and (6,10): 2 < 4 < 6 < 10. ✓ (2,4) and (7,9): 2 < 4 < 7 < 9. ✓ (6,10) and (7,9): 6 < 7 < 9 < 10. Nested. ✓. 4 chords!

Can we get 5? 5 chords need 10 points, all used. Label 1: 5 points (1, 3, 5, 7, 9), need to pair into 2 pairs + 1 unmatched, or... wait, 5 is odd, so at most 2 chords of label 1. Label 2: 5 points (2, 4, 6, 8, 10), at most 2 chords. Total at most 4. So f(5, 2) = 4 = 5 - 1. ✓

f(6, 2): 12 points. Label 1: 6 points, at most 3 chords. Label 2: 6 points, at most 3 chords. Total at most 6. But can we achieve 5 = 6 - 1?

(1, 5), (2, 4), (3, 7), (6, 10), (8, 12), (9, 11)? Wait, that's 6 chords. Let me check.
Label 1: (1, 5), (3, 7), (9, 11). Label 2: (2, 4), (6, 10), (8, 12).
(1, 5) and (3, 7): 1 < 3 < 5 < 7. Cross! ✗

Let me try: (1, 3), (5, 9), (7, 11) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 3) and (2, 4): 1 < 2 < 3 < 4. Cross! ✗

(1, 9), (3, 5), (7, 11) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 9) and (2, 4): nested. ✓ (1, 9) and (6, 8): nested. ✓ (1, 9) and (10, 12): 1 < 9 < 10 < 12. ✓ (1, 9) and (3, 5): nested. ✓ (1, 9) and (7, 11): 1 < 7 < 9 < 11. Cross! ✗

(1, 9), (3, 11), (5, 7) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 9) and (3, 11): 1 < 3 < 9 < 11. Cross! ✗

(1, 11), (3, 5), (7, 9) [label 1], (2, 4), (6, 8), (10, 12) [label 2].
(1, 11) and (10, 12): 1 < 10 < 11 < 12. Cross! ✗

(1, 11), (3, 5), (7, 9) [label 1], (2, 12), (4, 6), (8, 10) [label 2].
(1, 11) and (2, 12): 1 < 2 < 11 < 12. Cross! ✗

Hmm, getting 6 seems hard. Let me try for 5.

(1, 5), (3, 9), (7, 11) [label 1], (2, 4), (6, 8) [label 2]. 5 chords.
(1, 5) and (3, 9): 1 < 3 < 5 < 9. Cross! ✗

(1, 5), (2, 4), (3, 9), (6, 8), (7, 11) [label 1: 1,3,7; label 2: 2,6; wait, (3, 9) is label 1, (6, 8) is label 2, (7, 11) is label 1].
(1, 5) and (3, 9): cross. ✗

(1, 3), (2, 4), (5, 9), (6, 8), (7, 11) [label 1: (1,3), (5,9), (7,11); label 2: (2,4), (6,8)].
(1, 3) and (2, 4): cross. ✗

(1, 3), (5, 7), (9, 11) [label 1], (2, 4), (6, 8), (10, 12) [label 2]. 6 chords.
(1, 3) and (2, 4): cross. ✗

It seems like any pairing of adjacent same-label points causes crosses with the other label. Let me try a different approach.

(1, 7), (3, 5) [label 1], (2, 6), (4, 12), (8, 10) [label 2]. 5 chords.
(1, 7) and (2, 6): 1 < 2 < 6 < 7. Nested. ✓
(1, 7) and (3, 5): nested. ✓
(1, 7) and (4, 12): 1 < 4 < 7 < 12. Cross! ✗

(1, 7), (3, 5) [label 1], (2, 6), (4, 8), (10, 12) [label 2]. 5 chords.
(1, 7) and (4, 8): 1 < 4 < 7 < 8. Cross! ✗

(1, 7), (3, 5), (9, 11) [label 1], (2, 6), (8, 12) [label 2]. 5 chords.
(1, 7) and (2, 6): nested. ✓
(1, 7) and (8, 12): 1 < 7 < 8 < 12. ✓
(1, 7) and (9, 11): 1 < 7 < 9 < 11. ✓
(1, 7) and (3, 5): nested. ✓
(3, 5) and (2, 6): 2 < 3 < 5 < 6. Cross! ✗

(1, 7), (3, 5), (9, 11) [label 1], (2, 8), (6, 12) [label 2]. 5 chords.
Wait, (2, 8) is label 2, (6, 12) is label 2. 
(1, 7) and (2, 8): 1 < 2 < 7 < 8
