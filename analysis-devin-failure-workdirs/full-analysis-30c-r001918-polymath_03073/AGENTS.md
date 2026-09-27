# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $n=200$ and $k=50$. There are $2n+1$ students standing in a circle. Suppose that $n+1$ of the students are girls, and the other $n$ are boys. Each student $S$ has $2k$ neighbors: the $k$ students closest to $S$ on the right, and the $k$ students closest to $S$ on the left. Let $G$ be the number of girls who have at least $k$ girls among their $2k$ neighbors. What is the minimum possible value of $G$?       — 题目文本
#   The original problem asks to prove that there is at least one such girl, which means $G \ge 1$. The solution shows that by defining $b_i = a_i + a_{i-k-1} - 1$, the sum over a full cycle is $\sum_{i=1}^{2n+1} b_i = 1$. By applying Raney's Lemma or the Gas Station Theorem logic, it establishes the existence of at least one index $i$ such that $a_i = 1$ (the student is a girl) and the sum of her $2k$ neighbors is at least $k$. Since the proof only guarantees the existence of one such student, the minimum value is 1.  — 标准解答
#   Let me solve this problem. We have $2n+1 = 401$ students in a circle, $n+1 = 201$ girls and $n = 200$ boys. $k = 50$. Each student has $2k = 100$ neighbors (50 on each side). $G$ = number of girls with at least $k = 50$ girls among their 100 neighbors. Find minimum $G$.

Let me think about this carefully.

Let me denote the circle as a sequence of 0s (boys) and 1s (girls), with 201 ones and 200 zeros, arranged in a circle of 401.

For each girl at position $i$, her neighbors are the 50 closest on the left and 50 closest on the right (100 total). She counts as "good" if at least 50 of these 100 are girls.

We want to minimize the number of good girls.

Let me think about this more generally. Let $n = 200, k = 50$. So $n = 4k$.

Total students: $2n+1 = 401$. Girls: $n+1 = 201$, Boys: $n = 200$.

Let me think about a double-counting / averaging argument first.

For each girl, let $g_i$ = number of girls among her 100 neighbors. We want to count girls with $g_i \geq 50$.

Sum of $g_i$ over all girls: Each ordered pair of girls $(A, B)$ where $B$ is a neighbor of $A$ contributes 1. For two girls at distance $d$ (circular distance, $1 \leq d \leq 200$), they are neighbors of each other if $d \leq 50$ (on one side) — actually, $B$ is a neighbor of $A$ if $B$ is among the 50 closest on left or 50 closest on right, i.e., circular distance $\leq 50$.

So $\sum g_i = \sum_{\text{pairs of girls}} 2 \cdot [\text{dist} \leq 50]$... no wait, it's ordered pairs. $\sum g_i = \sum_{\text{ordered pairs } (A,B), A \neq B, \text{both girls}} [\text{dist}(A,B) \leq 50]$.

Hmm, this depends on the arrangement. Let me think differently.

Actually, let me think about what arrangement minimizes $G$.

Intuition: To minimize the number of girls with many girl-neighbors, we want to spread out the girls... but there are more girls than boys (201 vs 200), so girls are the majority. 

Actually, let me think about it. If we alternate G and B as much as possible: 201 girls, 200 boys. In a circle of 401, we can't perfectly alternate. We'd have something like GBGBGB...GBG with one extra G somewhere, creating a GG pair.

But with alternating, each girl has neighbors that are mostly boys. Let's see: in alternating arrangement G B G B G B ... the 50 neighbors on each side of a girl would be B G B G B G ... so 25 boys and 25 girls on each side, total 50 boys and 50 girls. So $g_i = 50$ for most girls, which means $g_i \geq 50$, so they're all good. That gives $G = 201$, which is bad (we want minimum).

Hmm, so alternating is bad. We want to cluster girls together so that some girls have many girl neighbors (good) but others have few (bad), minimizing the total count of good ones.

Wait, but we want to MINIMIZE $G$, the number of good girls. So we want as many girls as possible to have FEW girl neighbors.

Strategy: cluster the boys together to create regions where girls are surrounded by boys.

Actually, let me reconsider. If we put all 200 boys consecutively, then the remaining 201 girls are consecutive. A girl in the middle of the girl block has 50 girls on left and 50 girls on right = 100 girls, so $g_i = 100 \geq 50$, good. A girl near the boundary of the girl block... Let's think. The girl block has 201 girls. The first girl (adjacent to a boy) has 1 boy on one side (the immediate neighbor) and then 49 more positions on that side which are girls (since the boy block is on the other side). Wait, let me set up coordinates.

Place 200 boys at positions 1-200, and 201 girls at positions 201-401 (circularly). Position 200 is a boy, position 201 is a girl, position 401 is a girl, position 1 is a boy.

Girl at position 201: left neighbors (positions 200, 199, ..., 151) = 1 boy (pos 200) + 49 boys (pos 199-151) = 50 boys. Right neighbors (positions 202-251) = 50 girls. So $g_i = 50$. Good.

Girl at position 202: left neighbors (201, 200, ..., 152) = 1 girl (201) + 49 boys = 1 girl + 49 boys. Right neighbors (203-252) = 50 girls. $g_i = 51$. Good.

Girl at position 250: left neighbors (249, 248, ..., 200) = 49 girls + 1 boy = 49 girls. Right neighbors (251-300) = 50 girls. $g_i = 99$. Good.

Girl at position 251: left = 250 girls (positions 250 down to 201, that's 50 girls). Right = 252-301 = 50 girls. $g_i = 100$. Good.

So in this arrangement, essentially all girls are good. $G = 201$. That's the maximum, not minimum.

So clustering girls is bad for minimization. We need to spread girls out but in a way that many girls have $g_i < 50$.

Hmm, so we want girls to be isolated, surrounded by boys. But there are 201 girls and only 200 boys. 

Let me think about it differently. Consider a girl $S$. She has 100 neighbors. For $g_i < 50$, she needs at least 51 boys among her 100 neighbors. But there are only 200 boys total. 

Let me think about the complement. Let $b_i$ = number of boys among the 100 neighbors of girl $i$. Then $g_i = 100 - b_i$, and $g_i \geq 50 \iff b_i \leq 50$. So $G$ = number of girls with $b_i \leq 50$, and we want to minimize this, i.e., maximize the number of girls with $b_i \geq 51$.

So we want as many girls as possible to have at least 51 boy-neighbors.

Total boy-neighbor count: $\sum_{i \text{ girl}} b_i = \sum_{\text{ordered pairs } (G, B)} [\text{dist} \leq 50]$.

For a boy at position $j$, the number of girls within distance 50 is the number of girls in positions $j-50, \ldots, j-1, j+1, \ldots, j+50$ (circularly). Call this $c_j$. Then $\sum b_i = \sum_{j \text{ boy}} c_j$.

To maximize the number of girls with $b_i \geq 51$, we'd want to concentrate the boy-neighbor counts. 

Hmm, let me think about upper bounds. If $m$ girls have $b_i \geq 51$ and $201 - m$ girls have $b_i \leq 50$ (actually $b_i$ can be at most 100, and at least... well, at least 0). 

$\sum b_i \geq 51m + 0 \cdot (201 - m) = 51m$.

Also $\sum b_i = \sum_{j \text{ boy}} c_j$. What's the maximum of $\sum_{j \text{ boy}} c_j$?

Each boy $j$ has $c_j \leq 100$ (at most 100 neighbors, all could be girls). But more usefully, $\sum_{j \text{ boy}} c_j = \sum_{\text{ordered pairs } (G, B), \text{dist} \leq 50} 1$.

The total number of ordered pairs $(G, B)$ with distance $\leq 50$... For each girl, she has 100 neighbors, at most 100 of which are boys. So $\sum b_i \leq 201 \cdot 100 = 20100$. But also $\sum b_i \leq 200 \cdot 100 = 20000$ (each boy has at most 100 girl neighbors). So $\sum b_i \leq 20000$.

So $51m \leq 20000$, giving $m \leq 392.16...$, so $m \leq 392$. But $m \leq 201$ anyway, so this bound is $m \leq 201$, not useful.

Let me think more carefully. We need a better upper bound on $\sum b_i$.

Actually, let's think about it as: for each unordered pair $(G, B)$ at distance $d \leq 50$, it contributes 2 to $\sum b_i$ (once for the girl counting the boy, once for... no). Wait, $\sum_{i \text{ girl}} b_i$ counts, for each girl, the boys in her neighborhood. And $\sum_{j \text{ boy}} c_j$ counts, for each boy, the girls in his neighborhood. These are the same sum (both count ordered pairs $(G, B)$ at distance $\leq 50$). Yes.

So $\sum b_i = \sum_{j \text{ boy}} c_j$ where $c_j$ = number of girls within distance 50 of boy $j$.

Now, the key constraint is the arrangement. Let me think about what arrangement maximizes $\sum b_i$ or more precisely, what arrangement allows the most girls to have $b_i \geq 51$.

Let me think about small cases or a pattern.

Alternative approach: Think of it as a sliding window. For each position $i$ (a student), define $w_i$ = number of girls in the window of 100 neighbors (positions $i-50$ to $i+50$, excluding $i$). If position $i$ is a girl, then $g_i = w_i$ and she's good if $w_i \geq 50$.

Note: the window of 100 neighbors of position $i$ is positions $i-50, \ldots, i-1, i+1, \ldots, i+50$, which is 100 positions. Equivalently, it's the window $\{i-50, \ldots, i+50\} \setminus \{i\}$, which is 101 positions minus 1.

Let $W_i$ = number of girls in positions $i-50, \ldots, i+50$ (101 positions including $i$). If position $i$ is a girl, then $w_i = W_i - 1$, and she's good iff $W_i - 1 \geq 50$ iff $W_i \geq 51$.

If position $i$ is a boy, then $w_i = W_i$ (the number of girls in the 101-window, since $i$ itself is a boy).

So: a girl at position $i$ is good iff $W_i \geq 51$.

We want to minimize the number of girls $i$ with $W_i \geq 51$.

Now, $W_i$ is the number of girls in a window of 101 consecutive positions (centered at $i$). There are 401 such windows (one for each position), and they're all the windows of length 101 in the circle.

The sum $\sum_{i=1}^{401} W_i = 101 \cdot 201 = 20301$ (each girl is in 101 windows).

Average $W_i = 20301 / 401 \approx 50.63$.

So on average, $W_i \approx 50.63$, which is just above 51... wait, 50.63 < 51. So the average is below 51.

We want to minimize the number of positions $i$ that are girls AND have $W_i \geq 51$.

Hmm, let me think about this as an optimization problem. We have 201 girls and 200 boys in a circle of 401. We want to place them to minimize the count of girl-positions with $W_i \geq 51$.

Let me think about what happens if we try to make $W_i < 51$ for as many girls as possible, i.e., $W_i \leq 50$ for as many girls as possible.

If a girl at position $i$ has $W_i \leq 50$, that means among the 101 positions centered at $i$, at most 50 are girls, so at least 51 are boys. But there are only 200 boys total. 

Let me think about a construction. Suppose we arrange the circle as blocks. Let's try to have blocks of boys that are large enough to "cover" girls with few girl-neighbors.

Consider a girl who is isolated, surrounded by many boys. If a girl has 50 boys on her left and 50 boys on her right (all 100 neighbors are boys), then $b_i = 100$, $g_i = 0 < 50$, not good. But this requires 100 boys near her, and we only have 200 boys.

Let me think about a periodic construction. Suppose we have a pattern that repeats. 

Let me try: a block of $a$ boys followed by a block of $b$ girls, repeating. We need $a \cdot r = 200$ and $b \cdot r = 201$ for some number of repeats $r$. Since $\gcd(200, 201) = 1$, we'd need $r = 1$, which is the all-boys-then-all-girls case (bad).

Let me try a different approach. Let me think about two types of blocks.

Actually, let me think about the problem more carefully with the specific numbers. $n = 200, k = 50$, so $n = 4k$.

Let me consider a general approach. Place the students so that there are some "blocks of consecutive boys" interspersed with "blocks of consecutive girls."

For a girl in a block of consecutive girls of length $L$, her girl-neighbors depend on her position in the block and the sizes of neighboring boy blocks.

Let me think about a girl at the center of a large girl block. She'll have many girl neighbors. A girl at the edge of a girl block, adjacent to a large boy block, will have fewer girl neighbors.

To minimize $G$, we want most girls to be at the edges of girl blocks, adjacent to large boy blocks. But the total number of boys is limited.

Let me try a specific construction. Suppose we have blocks of 100 boys and 100 girls, alternating... but 200 boys and 201 girls. So: 100 boys, 100 girls, 100 boys, 101 girls. That's 4 blocks in a circle.

Let me compute $W_i$ for girls in different positions.

Block 1: positions 1-100, boys.
Block 2: positions 101-200, girls.
Block 3: positions 201-300, boys.
Block 4: positions 301-401, girls.

Girl at position 101 (start of block 2, adjacent to boy at 100):
$W_{101}$ = girls in positions 51-151. Positions 51-100 are boys (50 boys), position 101 is a girl, positions 102-151 are girls (50 girls). So $W_{101} = 51$. Good (since $W_i \geq 51$).

Girl at position 102: $W_{102}$ = girls in 52-152. Positions 52-100: boys (49). Position 101-152: girls (52). $W_{102} = 52$. Good.

Girl at position 150: $W_{150}$ = girls in 100-200. Position 100: boy. Positions 101-200: girls (100). $W_{150} = 100$. Good.

Girl at position 200 (end of block 2, adjacent to boy at 201): $W_{200}$ = girls in 150-250. Positions 150-200: girls (51). Positions 201-250: boys (50). $W_{200} = 51$. Good.

So all 100 girls in block 2 have $W_i \geq 51$. Similarly for block 4 (101 girls). So $G = 201$. Still bad.

The issue is that with blocks of 100, the girl blocks are too large—every girl in a block of 100 has at least 51 girls in her 101-window.

What if we make the girl blocks smaller? If a girl block has length $L$, the minimum $W_i$ for a girl in that block is achieved at the edges. For a girl at the edge of a block of length $L$, with boy blocks of length $a$ on one side and $b$ on the other:

The 101-window centered at this girl includes: some boys from the left block, the girl herself, and $L-1$ other girls, and some boys from the right block.

Let me be more precise. Consider a girl at the left edge of a girl block of length $L$, with a boy block of length $a$ to the left and a boy block of length $b$ to the right (of the girl block).

The 50 positions to her left: if $a \geq 50$, all 50 are boys. If $a < 50$, then $a$ boys and $50 - a$ girls (from the girl block wrapping around... no, in a circle with just these blocks).

Hmm, this is getting complicated with the circle. Let me think about it more carefully.

Let me consider a simpler model: a circle made of alternating boy-blocks and girl-blocks. Let the boy blocks have sizes $a_1, a_2, \ldots, a_r$ and girl blocks have sizes $b_1, b_2, \ldots, b_r$, with $\sum a_i = 200, \sum b_i = 201$.

For a girl at position $j$ within girl block $i$ (of size $b_i$), at distance $d$ from the left edge (so $d = 0$ is the leftmost girl, adjacent to boy block $a_i$... wait, I need to be careful about the ordering).

Let me say the circle goes: boy block $a_1$, girl block $b_1$, boy block $a_2$, girl block $b_2$, ..., boy block $a_r$, girl block $b_r$.

A girl at distance $d$ from the left edge of girl block $b_i$ (so $d = 0, 1, \ldots, b_i - 1$; $d = 0$ is adjacent to boy block $a_i$, $d = b_i - 1$ is adjacent to boy block $a_{i+1}$).

Her 50 left neighbors: first $\min(d, 50)$ are girls (from her own block), then if $d < 50$, the next $\min(50 - d, a_i)$ are boys (from boy block $a_i$), and if $d + a_i < 50$, we continue into girl block $b_{i-1}$, etc.

This is getting complex. Let me simplify by assuming all boy blocks are large (size $\geq 50$) and all girl blocks are small (size $\leq 50$ or so).

If boy blocks are all $\geq 50$ and girl blocks are all $\leq 51$, let's see what happens.

For a girl at the left edge ($d = 0$) of a girl block of size $b$:
- 50 left neighbors: all from boy block $a_i$ (if $a_i \geq 50$), all boys. So 0 girls on left.
- 50 right neighbors: $\min(50, b-1)$ girls from her own block, then boys from the next boy block.
  - If $b - 1 \geq 50$, i.e., $b \geq 51$: 50 girls on right. $g_i = 50$. Good.
  - If $b - 1 < 50$, i.e., $b \leq 50$: $b - 1$ girls on right, $50 - (b-1)$ boys. $g_i = b - 1 < 50$. Not good!

For a girl at distance $d$ from the left edge ($1 \leq d \leq b-1$):
- Left neighbors: $\min(d, 50)$ girls from own block, then boys.
  - If $d \leq 50$: $d$ girls on left (assuming $a_i \geq 50 - d$, which is true if $a_i \geq 50$).
- Right neighbors: $\min(50, b - 1 - d)$ girls from own block, then boys.
  - If $b - 1 - d \geq 50$: 50 girls on right. But $b \leq 50$ means $b - 1 - d \leq 49 < 50$. So $b - 1 - d$ girls on right.
  
  So $g_i = d + (b - 1 - d) = b - 1$ (when $d \leq 50$ and $b - 1 - d \leq 49$, which is always true when $b \leq 50$).
  
  Wait, that's interesting. If $b \leq 50$ and both neighboring boy blocks are $\geq 50$, then for any girl in this block, $g_i = b - 1$.

  Because: left neighbors include $d$ girls (from own block) + $(50 - d)$ boys (from left boy block, since $a_i \geq 50 \geq 50 - d$). Right neighbors include $(b - 1 - d)$ girls (from own block) + $(50 - (b - 1 - d))$ boys (from right boy block, since $a_{i+1} \geq 50 \geq 50 - (b-1-d)$). So $g_i = d + (b - 1 - d) = b - 1$.

So if $b \leq 50$, all girls in this block have $g_i = b - 1 < 50$, so none are good!

And if $b = 51$, all girls have $g_i = 50$, so all are good.

Wait, let me recheck for $b = 51$. Girl at $d = 0$: left = 0 girls, right = $\min(50, 50) = 50$ girls. $g_i = 50$. Good. Girl at $d = 25$: left = 25 girls, right = $\min(50, 25) = 25$ girls. $g_i = 50$. Good. Girl at $d = 50$: left = 50 girls, right = $\min(50, 0) = 0$ girls. $g_i = 50$. Good. So yes, all 51 girls are good.

So the threshold is exactly at $b = 51$: blocks of $\leq 50$ girls contribute 0 good girls, blocks of $\geq 51$ girls contribute all good girls (assuming boy blocks are $\geq 50$).

Now, we have 201 girls to distribute into blocks, and 200 boys into blocks, with boy blocks $\geq 50$.

If we have $r$ boy blocks each of size $\geq 50$, then $r \leq 4$ (since $200 / 50 = 4$). And we have $r$ girl blocks.

With $r = 4$: 4 boy blocks of size 50 each, 4 girl blocks summing to 201. To minimize good girls, we want as many girl blocks as possible to have size $\leq 50$. With 4 blocks summing to 201, at most 3 can be $\leq 50$ (since $3 \times 50 = 150 < 201$, the 4th would be $201 - 150 = 51$). Actually, we want to minimize the number of girls in blocks of size $\geq 51$.

If 3 blocks have size 50 and 1 has size 51: good girls = 51 (from the size-51 block). Total girls = 151 + 51 = 201. ✓. $G = 51$.

Can we do better? With 4 blocks: 3 of size 50, 1 of size 51. $G = 51$.

What if we use $r = 3$ boy blocks? Then 3 boy blocks summing to 200, each $\geq 50$. E.g., 66, 67, 67. And 3 girl blocks summing to 201. To minimize good girls: at most 2 blocks $\leq 50$ (since $2 \times 50 = 100$, 3rd = 101). Good girls = 101. Worse.

Or: 2 blocks of 50, 1 block of 100. Girl blocks: 2 of 50, 1 of 101. Good = 101. Worse.

What about $r = 4$ with different sizes? Boy blocks: 50, 50, 50, 50. Girl blocks: 50, 50, 50, 51. $G = 51$.

Can we get $G < 51$? We need all girl blocks to be $\leq 50$, but $\sum b_i = 201$ and with 4 blocks, max sum with all $\leq 50$ is 200 < 201. So at least one block must be $\geq 51$, contributing at least 51 good girls.

But wait—can we use more than 4 boy blocks? If boy blocks can be smaller than 50, our analysis changes. Let me reconsider.

If a boy block has size $a < 50$, then for a girl at the edge of an adjacent girl block, some of her 50 neighbors on that side would be girls from the next girl block (wrapping around the boy block). This could increase $g_i$.

Let me reconsider. With smaller boy blocks, the analysis is more complex. Let me think about whether using more, smaller boy blocks could help.

Suppose we have $r$ boy blocks and $r$ girl blocks, with boy blocks of sizes $a_1, \ldots, a_r$ (sum 200) and girl blocks $b_1, \ldots, b_r$ (sum 201).

For a girl at distance $d$ from the left edge of girl block $b_i$:
- Left neighbors (50 positions): $d$ girls from own block, then $a_i$ boys from boy block $a_i$, then if $d + a_i < 50$, girls from girl block $b_{i-1}$.
- Right neighbors (50 positions): $(b_i - 1 - d)$ girls from own block, then $a_{i+1}$ boys from boy block $a_{i+1}$, then if $(b_i - 1 - d) + a_{i+1} < 50$, girls from girl block $b_{i+1}$.

This is complex. Let me think about whether we can do better than 51.

Actually, let me reconsider the problem. The key insight is that we need at least one "large" girl block (size $\geq 51$) because 201 > 4 × 50 = 200. But maybe with a cleverer arrangement (not just alternating blocks), we can do better.

Wait, but maybe we don't need to use the block structure at all. Let me think about whether a non-block arrangement could achieve $G < 51$.

Hmm, but the block arrangement with $r = 4$ boy blocks of size 50 gives $G = 51$. Let me see if we can prove $G \geq 51$ in general, or find a better construction.

Let me think about a lower bound. 

Consider the 401 windows of size 101 (centered at each position). Each window $W_i$ has $W_i$ girls. $\sum W_i = 101 \times 201 = 20301$.

A girl at position $i$ is good iff $W_i \geq 51$.

Let $G$ = number of good girls. Let $B$ = number of good boys (boys with $W_i \geq 51$, though we don't care about this). Let's think about it differently.

Let $S$ = number of positions $i$ (girl or boy) with $W_i \geq 51$. Then $G \leq S$ (since good girls are a subset of positions with $W_i \geq 51$).

Actually, we want a lower bound on $G$, the number of girls with $W_i \geq 51$.

Hmm, let me think about it from the perspective of the girls. We have 201 girls. For each girl $i$, $W_i \geq 51$ means she's good. We want to minimize the count of such girls.

Let me think about the sum $\sum_{i: \text{girl}} W_i$. This equals $\sum_{i: \text{girl}} (\text{girls in window } i) = \sum_{j: \text{girl}} (\text{number of girl-windows containing } j)$.

For a girl at position $j$, the number of girl-centered windows containing $j$ is the number of girls $i$ with $|i - j|_{\text{circ}} \leq 50$. This depends on the arrangement.

This is getting complicated. Let me try a different approach.

Let me think about the problem as follows. Consider the 201 girls. For each girl, look at her 101-window (centered at her). We want to minimize the number of girls whose 101-window contains $\geq 51$ girls.

Alternative: think of the 401 positions on the circle. Color 201 of them as girls. For each girl-position $i$, let $W_i$ = number of girls in $\{i-50, \ldots, i+50\}$. Minimize $|\{i : \text{girl}, W_i \geq 51\}|$.

Let me think about a potential function or a clever counting argument.

Consider the "sliding window" of size 101. As we slide it around the circle, $W_i$ changes by at most 1 at each step (we lose one position and gain one). The sequence $W_1, W_2, \ldots, W_{401}, W_1$ is a cyclic sequence where consecutive terms differ by at most 1.

$\sum W_i = 20301$, average $\approx 50.63$.

Now, the girls are at some subset of positions. We want to minimize the number of girl-positions where $W_i \geq 51$.

Key idea: Since the average is 50.63, and $W_i$ changes by at most 1, there must be many positions where $W_i \geq 51$. Specifically, since the average is above 50, there must be positions with $W_i \geq 51$.

But we want to minimize the number of GIRL positions with $W_i \geq 51$, not the total number of positions with $W_i \geq 51$.

Hmm, can we arrange it so that the positions with $W_i \geq 51$ are mostly boys?

Let me think about this. In the block construction (4 boy blocks of 50, 4 girl blocks of 50, 50, 50, 51):

The $W_i$ values: in a boy block of 50, the $W_i$ values range from... let me compute.

Boy block of 50 (positions 1-50), girl block of 50 (positions 51-100), boy block of 50 (positions 101-150), girl block of 50 (positions 151-200), boy block of 50 (positions 201-250), girl block of 51 (positions 251-301), boy block of 50 (positions 302-351), girl block of 50 (positions 352-401).

Wait, let me recompute. 4 boy blocks of 50 = 200, 4 girl blocks of 50, 50, 50, 51 = 201. Total = 401. ✓

Let me compute $W_i$ for a few positions.

Position 1 (boy, in boy block 1-50): window is positions 352-401 (wait, 1-50=51, so positions 1-50 to 1+50 = positions -49 to 51 = positions 353-401, 1-51). Hmm, let me use modular arithmetic. Positions 1 to 401. Window for position $i$ is $\{i-50, \ldots, i+50\} \pmod{401}$.

Position 1: window = $\{352, \ldots, 401, 1, 2, \ldots, 51\}$. That's positions 352-401 (50 positions) + positions 1-51 (51 positions) = 101 positions. Positions 352-401 are girl block (50 girls). Positions 1-50 are boy block (50 boys). Position 51 is a girl. So $W_1 = 50 + 1 = 51$.

Hmm, so position 1 (a boy) has $W_1 = 51 \geq 51$. So this boy is "good" (in the sense of $W_i \geq 51$), but we only count girls.

Position 25 (boy, middle of boy block): window = $\{25-50, \ldots, 25+50\} = \{-25, \ldots, 75\} = \{377, \ldots, 401, 1, \ldots, 75\}$. Positions 377-401: 25 positions, all in girl block 352-401 (girls). Positions 1-50: boys. Positions 51-75: girls (25 girls). $W_{25} = 25 + 25 = 50 < 51$. Not good.

Position 50 (boy, end of boy block): window = $\{0, \ldots, 100\} = \{401, 1, \ldots, 100\}$. Position 401: girl. Positions 1-50: boys. Positions 51-100: girls (50). $W_{50} = 1 + 50 = 51$. Good (but it's a boy).

Position 51 (girl, start of girl block): window = $\{1, \ldots, 101\}$. Positions 1-50: boys. Positions 51-100: girls (50). Position 101: boy. $W_{51} = 50$. Not good! Great, this girl is not good.

Wait, but earlier I computed that a girl at the edge of a girl block of size 50 (with boy blocks of size 50 on both sides) has $g_i = 49$, so $W_i = 50$. Let me recheck. $W_{51}$ = girls in positions 1-101 = positions 51-100 (50 girls). $W_{51} = 50 < 51$. Not good. ✓

Position 75 (girl, middle of girl block 51-100): window = $\{25, \ldots, 125\}$. Positions 25-50: boys (26). Positions 51-100: girls (50). Positions 101-125: boys (25). $W_{75} = 50$. Not good. ✓

Position 100 (girl, end of girl block): window = $\{50, \ldots, 150\}$. Position 50: boy. Positions 51-100: girls (50). Positions 101-150: boys (50). $W_{100} = 50$. Not good. ✓

So all 50 girls in the girl block of size 50 have $W_i = 50$, not good. 

Now the girl block of size 51 (positions 251-301):

Position 251 (girl, start): window = $\{201, \ldots, 301\}$. Positions 201-250: boys (50). Positions 251-301: girls (51). $W_{251} = 51$. Good.

Position 276 (girl, middle): window = $\{226, \ldots, 326\}$. Positions 226-250: boys (25). Positions 251-301: girls (51). Positions 302-326: boys (25). $W_{276} = 51$. Good.

Position 301 (girl, end): window = $\{251, \ldots, 351\}$. Positions 251-301: girls (51). Positions 302-351: boys (50). $W_{301} = 51$. Good.

So all 51 girls in the size-51 block are good. $G = 51$.

Now, can we do better? Let me think about whether $G = 51$ is optimal or if we can achieve $G < 51$.

The constraint is: 201 girls in a circle of 401, and we need at least one "cluster" of girls that forces some to be good.

Let me think about a lower bound argument.

Claim: $G \geq 51$.

Approach: Consider the 201 girls. For each girl $i$, let $W_i$ be the number of girls in her 101-window. We have $\sum_{i: \text{girl}} W_i = ?$.

Actually, $\sum_{i: \text{girl}} W_i = \sum_{i: \text{girl}} \sum_{j: \text{girl}} [|i-j|_{\text{circ}} \leq 50] = \sum_{j: \text{girl}} \sum_{i: \text{girl}} [|i-j| \leq 50]$.

For each girl $j$, the number of girls $i$ with $|i-j| \leq 50$ is the number of girls in $j$'s 101-window, which is $W_j$. So $\sum_{i: \text{girl}} W_i = \sum_{j: \text{girl}} W_j$. That's circular.

Let me instead compute $\sum_{i: \text{girl}} W_i$ differently. $\sum_{i: \text{girl}} W_i = \sum_{i: \text{girl}} |\{j: \text{girl}, |i-j| \leq 50\}|$. This is the number of ordered pairs of girls at circular distance $\leq 50$.

This depends on the arrangement, so it's not a fixed number. Hmm.

Let me try a different approach for the lower bound.

Alternative approach: Think about it in terms of "coverage." 

Consider the girls that are NOT good, i.e., $W_i \leq 50$. For such a girl, her 101-window contains at most 50 girls, meaning at least 51 boys.

Let me think about the boys. There are 200 boys. Each non-good girl "consumes" at least 51 boys in her window. But boys can be shared.

Hmm, let me think about it differently. Let me consider the "girl intervals."

Actually, let me try to think about whether we can beat 51 with a non-block arrangement.

What if we use 5 boy blocks? Then we need 5 boy blocks summing to 200, each at least... well, they don't all need to be $\geq 50$. But if some are $< 50$, the analysis changes.

Let me try: 5 boy blocks of size 40 each (total 200), and 5 girl blocks summing to 201.

With boy blocks of size 40 < 50, a girl at the edge of a girl block might have some girls from the neighboring girl block in her window.

For a girl at the left edge ($d = 0$) of a girl block of size $b$, with boy block of size $a = 40$ to the left:
- 50 left neighbors: 40 boys (from boy block), then 10 girls (from the previous girl block, if it has $\geq 10$ girls).
- So $g_i$ from left = 10 (if previous girl block has $\geq 10$ girls).

- 50 right neighbors: $\min(50, b-1)$ girls from own block, then boys.
  - If $b \leq 51$: $b - 1$ girls from own block, $50 - (b-1)$ boys (if next boy block $\geq 50 - (b-1)$, which is $\leq 50$, and boy block is 40... if $b - 1 \leq 10$, i.e., $b \leq 11$, then $50 - (b-1) \geq 40$, so we need the boy block to be $\geq 50 - (b-1)$. If boy block is 40 and $50 - (b-1) > 40$, i.e., $b < 11$, then we'd also get girls from the next girl block on the right.

This is getting complicated. Let me think about it more carefully for a specific case.

5 boy blocks of 40, 5 girl blocks. Let's say girl blocks are $b_1, \ldots, b_5$ with $\sum b_i = 201$.

For a girl at position $d$ in girl block $i$ (size $b_i$), with boy block of size 40 on each side:

Left neighbors (50): $d$ girls from own block, then 40 boys, then $50 - d - 40 = 10 - d$ girls from previous girl block (if $d < 10$ and previous block has enough).

Right neighbors (50): $b_i - 1 - d$ girls from own block, then 40 boys, then $50 - (b_i - 1 - d) - 40 = 11 - b_i + d$ girls from next girl block (if $b_i - 1 - d < 10$, i.e., $d > b_i - 11$, and next block has enough).

Case 1: $d \geq 10$ and $d \leq b_i - 11$ (i.e., girl is "deep inside" the block, at least 10 from each edge). This requires $b_i \geq 21$.
- Left: $d$ girls + 40 boys. Right: $(b_i - 1 - d)$ girls + 40 boys. But $d + 40 \leq 50$ requires $d \leq 10$, and $d \geq 10$, so $d = 10$. And $b_i - 1 - d + 40 \leq 50$ requires $b_i - 1 - d \leq 10$, i.e., $d \geq b_i - 11$. With $d = 10$, need $b_i \leq 21$. So $b_i = 21, d = 10$.
  - $g_i = 10 + 10 = 20$. Not good.

Case 2: $d < 10$ (near left edge).
- Left: $d$ girls + 40 boys + $(10 - d)$ girls from previous block. $g_{\text{left}} = d + (10 - d) = 10$ (assuming previous block has $\geq 10 - d$ girls).
- Right: $(b_i - 1 - d)$ girls + 40 boys + $(11 - b_i + d)$ girls from next block (if $b_i - 1 - d < 10$).
  - If $b_i - 1 - d \geq 10$ (i.e., $d \leq b_i - 11$): $g_{\text{right}} = b_i - 1 - d$. Total $g_i = 10 + (b_i - 1 - d) = b_i + 9 - d$.
  - If $b_i - 1 - d < 10$ (i.e., $d > b_i - 11$): $g_{\text{right}} = (b_i - 1 - d) + (11 - b_i + d) = 10$. Total $g_i = 10 + 10 = 20$.

So for $d < 10$:
- If $d \leq b_i - 11$: $g_i = b_i + 9 - d$. For $d = 0$: $g_i = b_i + 9$. For $d = 9$: $g_i = b_i$.
- If $d > b_i - 11$ (i.e., $b_i \leq 10 + d < 20$): $g_i = 20$.

For $g_i < 50$, we need:
- In the first subcase: $b_i + 9 - d < 50$, i.e., $b_i < 41 + d$. Since $d < 10$, need $b_i < 51$. So if $b_i \leq 50$, $g_i < 50$ for all $d$ in this range. If $b_i = 51$, $g_i = 51 + 9 - d = 60 - d \geq 51$ for $d \leq 9$. Good.
- In the second subcase: $g_i = 20 < 50$. Not good.

Case 3: $d > b_i - 11$ (near right edge, $d \geq 10$). By symmetry with Case 2 (swapping left/right):
- $g_i = 20$ (if also $d < 10$... no, $d \geq 10$ here).

Hmm, let me redo this. By symmetry (left-right), for $d > b_i - 11$ and $d \geq 10$:
- Right: $(b_i - 1 - d)$ girls + 40 boys + $(11 - b_i + d)$ girls from next block. $g_{\text{right}} = (b_i - 1 - d) + (11 - b_i + d) = 10$.
- Left: $d$ girls + 40 boys + $(10 - d)$ girls from previous block. But $d \geq 10$, so $10 - d \leq 0$, meaning left is just $d$ girls + 40 boys, with $d + 40 \leq 50$ requiring $d \leq 10$. So $d = 10$.
  - $g_{\text{left}} = 10$. Total $g_i = 10 + 10 = 20$.

Wait, I think I need to be more careful. Let me redo this.

For $d \geq 10$: left neighbors are $d$ girls (from own block) + $(50 - d)$ positions which are boys (from left boy block of size 40) and then possibly girls. Since $50 - d \leq 40$ when $d \geq 10$, all $(50 - d)$ are boys. So $g_{\text{left}} = d$.

For $d \leq b_i - 11$ (i.e., $b_i - 1 - d \geq 10$): right neighbors are $(b_i - 1 - d)$ girls + $(50 - (b_i - 1 - d))$ positions. Since $b_i - 1 - d \geq 10$, $50 - (b_i - 1 - d) \leq 40$, so all are boys. $g_{\text{right}} = b_i - 1 - d$.

Total: $g_i = d + (b_i - 1 - d) = b_i - 1$.

For $d > b_i - 11$ and $d \geq 10$ (i.e., $b_i - 1 - d < 10$ and $d \geq 10$): right neighbors are $(b_i - 1 - d)$ girls + 40 boys + $(50 - (b_i - 1 - d) - 40) = (11 - b_i + d)$ girls from next block. $g_{\text{right}} = (b_i - 1 - d) + (11 - b_i + d) = 10$.

Left: $d$ girls (since $d \geq 10$, all 50 left are $d$ girls + $(50-d)$ boys). $g_{\text{left}} = d$.

Total: $g_i = d + 10$.

For this to be $< 50$: $d + 10 < 50$, i.e., $d < 40$. Since $d \leq b_i - 1$ and $d > b_i - 11$, we have $b_i - 10 < d < 40$, which requires $b_i < 50$. If $b_i \leq 49$, then $d \leq 48 < 40$... wait, $d < 40$ is needed. $d$ can be up to $b_i - 1$. If $b_i \leq 40$, then $d \leq 39 < 40$. OK. If $b_i = 49$, $d$ can be up to 48, and $d > 38$. So $d \in \{39, 40, ..., 48\}$. For $d = 39$: $g_i = 49 < 50$. For $d = 40$: $g_i = 50 \geq 50$. Good!

Hmm wait, so for $b_i = 49$ and $d = 40$: $g_i = 40 + 10 = 50 \geq 50$. Good. And for $d = 39$: $g_i = 39 + 10 = 49 < 50$. Not good.

But wait, for $d = 39$ and $b_i = 49$: is $d > b_i - 11 = 38$? Yes, $39 > 38$. And $d \geq 10$? Yes. So $g_i = 39 + 10 = 49$. Not good.

For $d = 40, b_i = 49$: $d > 38$, $d \geq 10$. $g_i = 40 + 10 = 50$. Good.

But also, for $d = 40, b_i = 49$: $d \leq b_i - 11 = 38$? No, $40 > 38$. So we're in the second case. $g_i = 40 + 10 = 50$. Good.

Hmm, so for $b_i = 49$, girls at $d = 40, 41, ..., 48$ are good (9 girls), and girls at $d = 0, ..., 39$ are not good (wait, I need to check $d < 10$ too).

For $d < 10, b_i = 49$: $d \leq b_i - 11 = 38$, so first subcase. $g_i = b_i + 9 - d = 58 - d$. For $d = 0$: $g_i = 58 \geq 50$. Good! For $d = 8$: $g_i = 50$. Good. For $d = 9$: $g_i = 49$. Not good.

Wait, so for $b_i = 49$:
- $d = 0$: $g_i = 58$. Good.
- $d = 1$: $g_i = 57$. Good.
- ...
- $d = 8$: $g_i = 50$. Good.
- $d = 9$: $g_i = 49$. Not good.
- $d = 10$ to $d = 38$: $g_i = b_i - 1 = 48$. Not good.
- $d = 39$: $g_i = 49$. Not good.
- $d = 40$ to $d = 48$: $g_i = d + 10 = 50, 51, ..., 58$. Good.

So good girls in this block: $d = 0..8$ (9 girls) and $d = 40..48$ (9 girls) = 18 good girls out of 49.

That's worse than the block arrangement where a block of 50 has 0 good girls!

So using smaller boy blocks (40 instead of 50) makes things worse because girls "leak" into each other's neighborhoods.

This suggests that larger boy blocks are better, and the optimal is boy blocks of size exactly 50.

Let me verify: with boy blocks of size $\geq 50$, girl blocks of size $\leq 50$ have 0 good girls, and girl blocks of size 51 have all 51 good. With 4 boy blocks of 50 and girl blocks 50, 50, 50, 51, we get $G = 51$.

Can we use boy blocks larger than 50? If boy blocks are larger, we have fewer boy blocks, hence fewer girl blocks, and the girl blocks must be larger (since total is 201). E.g., 3 boy blocks of 67 (total 201, too much). 3 boy blocks summing to 200, e.g., 66, 67, 67. 3 girl blocks summing to 201. Best: 50, 50, 101. Good girls = 101. Worse.

Or 2 boy blocks of 100, 2 girl blocks summing to 201: 50, 151 or 100, 101. Best is 100, 101: good = 101. Or 50, 151: good = 151. Worse.

So 4 boy blocks of 50 is optimal among block arrangements, giving $G = 51$.

But can a non-block arrangement do better? Let me think about this.

The key question: is $G \geq 51$?

Let me try to prove $G \geq 51$.

Approach: Consider the 201 girls on the circle. We want to show at least 51 of them have $W_i \geq 51$.

Equivalently, at most 150 girls can have $W_i \leq 50$.

Let me think about it. Suppose at most 150 girls have $W_i \leq 50$. These 150 girls each have at most 50 girls in their 101-window, meaning at least 51 boys. 

Hmm, let me think about a cleaner argument.

Consider the circle as a sequence of 401 positions. Let's think about "runs" of consecutive girls.

Actually, let me think about the problem differently. Let me consider the complement: boys. There are 200 boys. For each boy, define $W'_i$ = number of boys in his 101-window. Then $W'_i = 101 - W_i$ (since the 101-window has 101 positions, either girl or boy). Wait, no: $W_i$ = number of girls in the 101-window, and the 101-window has 101 positions, so number of boys = $101 - W_i$. So $W'_i = 101 - W_i$.

A girl at position $i$ is good iff $W_i \geq 51$ iff $W'_i \leq 50$ (at most 50 boys in her window).

Now, $\sum_{i=1}^{401} W'_i = 101 \times 200 = 20200$ (each boy is in 101 windows). Average $W'_i = 20200/401 \approx 50.37$.

A girl is good iff $W'_i \leq 50$. We want to minimize the number of girls with $W'_i \leq 50$.

Hmm, I need to think about this more cleverly.

Let me try a direct approach. I'll try to prove that $G \geq n/(2k) \cdot ... $ no, let me think about the specific numbers.

Actually, let me think about a cleaner formulation. Let me use the "sliding window" perspective.

Define $f(i) = W_i$ = number of girls in the window $\{i-50, \ldots, i+50\}$ (101 positions). As $i$ increases by 1, the window shifts by 1: we lose position $i-50$ and gain position $i+51$. So $f(i+1) = f(i) - [\text{pos } i-50 \text{ is girl}] + [\text{pos } i+51 \text{ is girl}]$.

The sequence $f(1), f(2), \ldots, f(401)$ is a cyclic sequence with $f(i+1) - f(i) \in \{-1, 0, 1\}$.

$\sum f(i) = 20301$. Average $\approx 50.63$.

Now, a girl at position $i$ is good iff $f(i) \geq 51$.

We want to minimize the number of girl-positions $i$ with $f(i) \geq 51$.

Let me think about the positions where $f(i) \geq 51$. Since the average is 50.63 > 50, and $f$ changes by at most 1, there's a contiguous arc of the circle where $f \geq 51$ (well, possibly multiple arcs).

Actually, $f$ can go above and below 51 multiple times. But the total "excess" above 50 is $\sum (f(i) - 50) = 20301 - 50 \times 401 = 20301 - 20050 = 251$.

And the total "deficit" below 51 is $\sum (51 - f(i))$ for $f(i) < 51$... hmm, this isn't leading anywhere clean.

Let me try yet another approach. Think about it as: we have 201 girls. We want to show that at least 51 of them are "good" (have $\geq 51$ girls in their 101-window, including themselves).

Consider the girls in order around the circle: $g_1, g_2, \ldots, g_{201}$ (in circular order). Let $d_j$ = circular distance from $g_j$ to $g_{j+1}$ (number of steps, so $d_j \geq 1$ and $\sum d_j = 401$).

For girl $g_j$, the number of girls in her 101-window is the number of $g_l$ with circular distance $\leq 50$ from $g_j$. This is 1 (herself) plus the number of other girls within distance 50.

The girls within distance 50 to the right of $g_j$ are $g_{j+1}, g_{j+2}, \ldots$ as long as the cumulative distance $\leq 50$. Similarly to the left.

Let $r_j$ = number of girls to the right of $g_j$ within distance 50 (i.e., the largest $m$ such that $\sum_{l=0}^{m-1} d_{j+l} \leq 50$, where $d_{j+l}$ is the distance from $g_{j+l}$ to $g_{j+l+1}$). Wait, I need to be careful. The distance from $g_j$ to $g_{j+m}$ is $\sum_{l=0}^{m-1} d_{j+l}$. We need this $\leq 50$.

Similarly, $l_j$ = number of girls to the left of $g_j$ within distance 50.

Then $W_{g_j} = 1 + r_j + l_j$, and $g_j$ is good iff $r_j + l_j \geq 50$.

We want to minimize the number of $j$ with $r_j + l_j \geq 50$.

Now, $r_j$ is the number of girls in $(g_j, g_j + 50]$ (the 50 positions to the right). And $l_j$ is the number of girls in $[g_j - 50, g_j)$ (the 50 positions to the left).

Note that $r_j + l_j$ = number of girls in the 100 neighbors of $g_j$ = $g_j$'s girl-neighbor count.

Also, $r_j$ depends on the gaps $d_j, d_{j+1}, \ldots$. Specifically, $r_j = \max\{m : d_j + d_{j+1} + \cdots + d_{j+m-1} \leq 50\}$.

And $l_j = \max\{m : d_{j-1} + d_{j-2} + \cdots + d_{j-m} \leq 50\}$.

Note that $r_j + l_j$ = number of girls among the 100 neighbors. And $r_j$ counts girls to the right, $l_j$ counts girls to the left.

Key observation: $r_j$ is the number of $d$'s starting from $d_j$ that sum to $\leq 50$, and $l_j$ is the number of $d$'s ending at $d_{j-1}$ that sum to $\leq 50$.

Now, $r_j + l_j \geq 50$ iff $g_j$ is good. We want to minimize the count of good $g_j$'s.

Let me think about the relationship between $r_j$ and the gaps.

If all gaps are 2 (alternating G B G B...), then $r_j = 25$ (since $25 \times 2 = 50$) and $l_j = 25$, so $r_j + l_j = 50$, all good. $G = 201$.

If gaps are large (girls spread out), $r_j$ and $l_j$ are small.

We have $\sum d_j = 401$ and $d_j \geq 1$. There are 201 gaps.

Average gap $= 401/201 \approx 1.995$. So on average, gaps are about 2.

If a gap is 1 (two adjacent girls), that "uses up" less distance, allowing more girls to fit in the 50-distance window.

To minimize good girls, we want $r_j + l_j < 50$ for as many girls as possible. Since $r_j + l_j$ counts girls in the 100-neighborhood, and the average number of girls in a 100-neighborhood (of a girl) is... let me compute.

$\sum_{j=1}^{201} (r_j + l_j) = \sum_j r_j + \sum_j l_j$. 

$\sum_j r_j$ = number of ordered pairs $(g_j, g_l)$ with $g_l$ to the right of $g_j$ at distance $\leq 50$. By symmetry (the circle is symmetric), $\sum_j r_j = \sum_j l_j$. So $\sum_j (r_j + l_j) = 2 \sum_j r_j$.

$\sum_j r_j$ = number of ordered pairs of girls at circular distance $\leq 50$ (in one direction). This is the number of pairs $(j, l)$ with $l > j$ (circularly) and distance $\leq 50$.

Hmm, this depends on the arrangement. Let me think about it differently.

Actually, $\sum_j (r_j + l_j) = \sum_j W_{g_j} - 201$ (since $W_{g_j} = 1 + r_j + l_j$). And $\sum_j W_{g_j} = \sum_{j: \text{girl}} W_j$.

$\sum_{j: \text{girl}} W_j = \sum_{j: \text{girl}} |\{l: \text{girl}, |j - l| \leq 50\}| = $ number of ordered pairs of girls at distance $\leq 50$.

This is arrangement-dependent. But we can bound it.

For each girl $j$, $W_j \leq 101$ (at most 101 girls in 101 positions). Also, $W_j \geq 1$ (at least herself).

The total $\sum_{j: \text{girl}} W_j$ is maximized when girls are clustered (many girls close together) and minimized when spread out.

To minimize $G$ (good girls), we want to minimize $\sum_{j: \text{girl}} W_j$? Not necessarily, but it's related.

If $G$ girls have $W_j \geq 51$ and $201 - G$ girls have $W_j \leq 50$:
$\sum_{j: \text{girl}} W_j \geq 51 G + 1 \cdot (201 - G) = 50 G + 201$.
$\sum_{j: \text{girl}} W_j \leq 101 G + 50 (201 - G) = 51 G + 10050$.

So $G \geq (\sum W_j - 10050) / 51$ and $G \leq (\sum W_j - 201) / 50$.

To get a lower bound on $G$, we need a lower bound on $\sum W_j$.

What's the minimum of $\sum_{j: \text{girl}} W_j$? This is the minimum number of ordered pairs of girls at distance $\leq 50$.

To minimize this, we want to spread girls out as much as possible. But with 201 girls in 401 positions, the average gap is ~2, so girls are close together.

Hmm, let me think about the minimum of $\sum_{j: \text{girl}} W_j$ more carefully.

$\sum_{j: \text{girl}} W_j = \sum_{j: \text{girl}} \sum_{l: \text{girl}} [|j-l| \leq 50] = \sum_{\text{ordered pairs of girls}} [\text{dist} \leq 50]$.

For each unordered pair of girls at distance $d \leq 50$, it contributes 2 to the sum. For $d > 50$ (i.e., $d \geq 51$), it contributes 0. (Note: max circular distance is 200.)

So $\sum W_j = 2 \times |\{\text{unordered pairs of girls at distance} \leq 50\}|$.

To minimize this, we want to maximize the number of pairs at distance $> 50$.

The number of unordered pairs of girls is $\binom{201}{2} = 20100$.

For each pair at distance $d$ (circular distance, $1 \leq d \leq 200$), the pair is "close" if $d \leq 50$ and "far" if $d \geq 51$.

We want to maximize far pairs. For each girl, the number of positions at distance $> 50$ is $401 - 1 - 100 = 300$ (excluding herself and the 100 neighbors). So each girl can have at most 300 far girls. But there are only 200 other girls.

Hmm, this isn't directly helpful. Let me think about it differently.

For a given arrangement, the number of close pairs (distance $\leq 50$) is what we want to minimize. 

Consider the girls as points on a circle of circumference 401. The number of pairs at distance $\leq 50$ is what we want to minimize.

This is related to the "energy" of the point configuration. To minimize close pairs, we want to spread the points evenly.

If girls are perfectly evenly spaced (gap 401/201 ≈ 1.995), the number of girls within distance 50 of any girl is about 50/1.995 ≈ 25 on each side, so about 50 total. So $W_j \approx 51$ for all girls, and all are good. That gives $G = 201$.

If girls are clustered, some have many close neighbors (high $W_j$) and some have few (low $W_j$). The total $\sum W_j$ might be higher or lower.

Actually, let me think about it. When girls are clustered, the close-pair count can be very high within clusters. When spread out, it's more uniform.

To minimize $\sum W_j$ (close pairs), spreading out is better. But spreading out makes all girls good (as we saw). To minimize $G$, we want some girls to have $W_j \leq 50$, which requires clustering (so some girls are "isolated" from other clusters).

This is a trade-off. Let me think about the block construction and compute $\sum W_j$.

Block construction: 4 boy blocks of 50, girl blocks of 50, 50, 50, 51.

For a girl in a block of 50 (with boy blocks of 50 on both sides): $W_j = 50$ (as computed). For a girl in the block of 51: $W_j = 51$.

$\sum W_j = 3 \times 50 \times 50 + 51 \times 51 = 7500 + 2601 = 10101$.

Now, $G = 51$, and $\sum W_j = 10101$. Check: $51 \times 51 + 150 \times 50 = 2601 + 7500 = 10101$. ✓ (51 good girls with $W = 51$, 150 non-good with $W = 50$.)

Can we achieve $\sum W_j < 10101$? If so, potentially $G < 51$.

But actually, $G$ depends on the distribution, not just the sum. Let me think about whether we can have $G < 51$.

Suppose $G = 50$. Then 50 girls have $W_j \geq 51$ and 151 girls have $W_j \leq 50$.

$\sum W_j \geq 51 \times 50 + 1 \times 151 = 2550 + 151 = 2701$. And $\sum W_j \leq 101 \times 50 + 50 \times 151 = 5050 + 7550 = 12600$.

So the sum doesn't directly give us a contradiction. We need a better argument.

Let me think about a different lower bound approach.

Alternative approach: Consider the 401 positions. For each position $i$, let $x_i = 1$ if girl, 0 if boy. $\sum x_i = 201$.

$f(i) = \sum_{j: |j-i| \leq 50} x_j$ (sum over 101 positions). $\sum f(i) = 101 \times 201 = 20301$.

Girl $i$ is good iff $f(i) \geq 51$.

Now, consider the "excess" $e(i) = f(i) - 50$. $\sum e(i) = 20301 - 50 \times 401 = 251$.

Girl $i$ is good iff $e(i) \geq 1$.

We want to minimize the number of girls with $e(i) \geq 1$.

Now, $e(i) = f(i) - 50 = \sum_{|j-i| \leq 50} x_j - 50$. 

Hmm, let me think about the positions where $e(i) \geq 1$ (i.e., $f(i) \geq 51$). These form some arcs on the circle. Within each arc, $f(i) \geq 51$, and outside, $f(i) \leq 50$.

The total excess is 251. If the good positions (where $f \geq 51$) have $f$ values summing to $S$, and the non-good positions have $f$ values summing to $20301 - S$, then:

$S \geq 51 \times |\text{good positions}|$ and $20301 - S \leq 50 \times (401 - |\text{good positions}|)$.

From the second: $20301 - S \leq 50 \times 401 - 50 \times |\text{good}| = 20050 - 50 |\text{good}|$. So $S \geq 20301 - 20050 + 50 |\text{good}| = 251 + 50 |\text{good}|$.

From the first: $S \geq 51 |\text{good}|$.

So $S \geq \max(51 |\text{good}|, 251 + 50 |\text{good}|)$. The second bound is stronger when $251 + 50 |\text{good}| > 51 |\text{good}|$, i.e., $251 > |\text{good}|$, i.e., $|\text{good}| < 251$. Since $|\text{good}| \leq 401$, this is usually the case.

So $|\text{good positions}| \geq 251$ (from $S \leq 101 |\text{good}|$ and $S \geq 251 + 50 |\text{good}|$: $101 |\text{good}| \geq 251 + 50 |\text{good}|$, so $51 |\text{good}| \geq 251$, $|\text{good}| \geq 251/51 \approx 4.92$, so $|\text{good}| \geq 5$).

Wait, that gives $|\text{good positions}| \geq 5$, which is weak. We need $|\text{good girls}| \geq 51$, not $|\text{good positions}| \geq 5$.

The issue is that good positions can be boys. We need to relate good positions to good girls.

Hmm. Let me think about this differently.

Let me consider the following: in the block construction, the good positions (where $f \geq 51$) include the 51 girls in the large block AND some boys near the boundaries. Let me count.

In the block construction (boy blocks of 50, girl blocks of 50, 50, 50, 51):

For the girl block of 51 (positions 251-301), the $f$ values:
- Position 251 (girl): $f = 51$. Good.
- Position 252 (girl): $f = 52$. Good.
- ...
- Position 276 (girl, center): $f = 51$. Good.
- ...
- Position 301 (girl): $f = 51$. Good.

Actually, let me recompute. For the girl block of 51 surrounded by boy blocks of 50:
- Position 251 (first girl): window 201-301. Boys 201-250 (50), girls 251-301 (51). $f = 51$.
- Position 252: window 202-302. Boys 202-250 (49), girls 251-301 (51), boy 302 (1). $f = 51$.
- Position 276 (center): window 226-326. Boys 226-250 (25), girls 251-301 (51), boys 302-326 (25). $f = 51$.
- Position 301 (last girl): window 251-351. Girls 251-301 (51), boys 302-351 (50). $f = 51$.

So all 51 girls have $f = 51$. Now the boys near the boundary:
- Position 250 (boy, just before girl block): window 200-300. Boys 200-250 (51), girls 251-300 (50). $f = 50$. Not good.
- Position 249 (boy): window 199-299. Boys 199-250 (52), girls 251-299 (49). $f = 49$. Not good.

So the boys adjacent to the large girl block are NOT good. Let me check the other side.
- Position 302 (boy, just after girl block): window 252-352. Girls 252-301 (50), boys 302-352 (51). $f = 50$. Not good.

So the only good positions are the 51 girls in the large block. $|\text{good positions}| = 51 = G$.

Now, for the girl blocks of 50: all girls have $f = 50$, not good. And the boys near them also have $f \leq 50$.

So in this construction, $|\text{good positions}| = 51$ and $G = 51$.

Now I need to prove $G \geq 51$ in general. Let me think about a proof.

Approach: Consider the 201 girls. I want to show at least 51 have $f(i) \geq 51$.

Let me think about the "girl-only" subsequence. Consider the girls $g_1, \ldots, g_{201}$ in circular order, with gaps $d_1, \ldots, d_{201}$ (sum = 401).

For each girl $g_j$, $f(g_j) = 1 + r_j + l_j$ where $r_j$ = number of girls to the right within distance 50, $l_j$ = number to the left within distance 50.

$r_j$ = max $m$ such that $d_j + d_{j+1} + \cdots + d_{j+m-1} \leq 50$.

Good iff $r_j + l_j \geq 50$.

Now, note that $r_j + l_j$ = number of girls (other than $g_j$) within distance 50. And $r_j$ girls to the right means the $(r_j + 1)$-th girl to the right is at distance $> 50$.

Key insight: $r_j + l_j + 1 = f(g_j)$, and $f(g_j) \geq 51$ iff $r_j + l_j \geq 50$.

Let me think about the relationship between $r_j$ and $l_j$ and the gaps.

Consider the "right reach" $R_j = d_j + d_{j+1} + \cdots + d_{j+r_j-1}$ (sum of $r_j$ gaps, which is the distance to the $r_j$-th girl to the right). We have $R_j \leq 50$ and $R_j + d_{j+r_j} > 50$ (the next girl is too far).

Similarly, $L_j = d_{j-1} + d_{j-2} + \cdots + d_{j-l_j}$ (distance to the $l_j$-th girl to the left). $L_j \leq 50$ and $L_j + d_{j-l_j-1} > 50$.

Now, $r_j + l_j \geq 50$ iff good. 

Let me think about a counting argument. Consider the sum $\sum_j (r_j + l_j) = 2 \sum_j r_j$ (by symmetry of the circle).

$\sum_j r_j$ = number of ordered pairs $(g_j, g_l)$ with $g_l$ to the right of $g_j$ at distance $\leq 50$.

For each pair of girls at distance $d \leq 50$, it contributes 1 to $\sum r_j$ (the left girl counts the right girl) and 1 to $\sum l_j$ (the right girl counts the left girl). So $\sum r_j = \sum l_j = $ number of unordered close pairs.

$\sum (r_j + l_j) = 2 \times $ (number of unordered close pairs).

In the block construction: close pairs = pairs within the same girl block (since different blocks are separated by 50 boys, distance > 50). 

Block of 50: $\binom{50}{2} = 1225$ close pairs. Three such blocks: $3 \times 1225 = 3675$.
Block of 51: $\binom{51}{2} = 1275$ close pairs.
Total: $3675 + 1275 = 4950$.

$\sum (r_j + l_j) = 2 \times 4950 = 9900$. And $\sum f(g_j) = 201 + 9900 = 10101$. ✓ (matches earlier).

Now, for the lower bound on $G$: we have 201 girls, $G$ good (with $r_j + l_j \geq 50$, i.e., $f \geq 51$) and $201 - G$ not good (with $r_j + l_j \leq 49$, i.e., $f \leq 50$).

$\sum (r_j + l_j) \geq 50 G + 0 \cdot (201 - G) = 50G$ (since non-good girls have $r_j + l_j \geq 0$).

Also $\sum (r_j + l_j) \leq 100 G + 49(201 - G) = 51G + 9849$.

So $G \leq (\sum (r_j + l_j) - 9849) / 51$ and $G \geq \sum (r_j + l_j) / 100$... no, $G \geq \sum (r_j + l_j) / 100$ only if all good girls have $r_j + l_j \leq 100$, which is true. But this gives $G \geq 9900/100 = 99$ in the block construction, which contradicts $G = 51$. So this bound is wrong.

Wait, I think I messed up. $\sum (r_j + l_j) \leq 100 \cdot G + 49 \cdot (201 - G)$ is an UPPER bound on the sum, not a lower bound on $G$. Let me redo.

We have:
- $G$ good girls with $r_j + l_j \geq 50$ (and $\leq 100$).
- $201 - G$ non-good girls with $r_j + l_j \leq 49$ (and $\geq 0$).

Lower bound on sum: $\sum (r_j + l_j) \geq 50G + 0 = 50G$.
Upper bound on sum: $\sum (r_j + l_j) \leq 100G + 49(201-G) = 51G + 9849$.

So $G \geq \sum (r_j + l_j) / 100$... no. From the lower bound: $50G \leq \sum (r_j + l_j)$, so $G \leq \sum / 50$. From the upper bound: $\sum \leq 51G + 9849$, so $G \geq (\sum - 9849)/51$.

In the block construction, $\sum = 9900$, so $G \geq (9900 - 9849)/51 = 51/51 = 1$. That's very weak.

The problem is that the sum $\sum (r_j + l_j)$ can vary a lot depending on the arrangement. To get a strong lower bound on $G$, I need either a lower bound on $\sum (r_j + l_j)$ that's high enough, or a different approach.

Let me think about the minimum of $\sum (r_j + l_j) = 2 \times $ (close pairs).

What's the minimum number of close pairs (pairs of girls at distance $\leq 50$)?

We have 201 girls on a circle of 401. We want to minimize the number of pairs at distance $\leq 50$.

This is an optimization problem. To minimize close pairs, we want to spread girls out. But with 201 girls in 401 positions, the density is about 1/2, so many pairs will be close.

In the block construction, close pairs = 4950. Can we do better (fewer close pairs)?

If we spread girls evenly (gap ~2), each girl has about 50 close neighbors (25 on each side), so close pairs $\approx 201 \times 50 / 2 = 5025$. That's more than 4950!

So the block construction actually has fewer close pairs than the even arrangement. Interesting.

Can we do even better? What if we have larger boy blocks?

With 2 boy blocks of 100 and 2 girl blocks of 100 and 101:
Close pairs within block of 100: $\binom{100}{2} = 4950$. But wait, in a block of 100, two girls at the opposite ends are at distance 99 > 50. So not all pairs within a block are close.

Hmm, I need to be more careful. In a block of 100 consecutive girls, the distance between the first and last is 99. So pairs at distance $\leq 50$ within the block: for a girl at position $d$ in the block (0-indexed, $d = 0, \ldots, 99$), the girls within distance 50 are those at positions $d-50, \ldots, d+50$ (within the block). The count is $\min(d, 50) + \min(99-d, 50) + 1$ (including herself, but for pairs we exclude her).

Actually, the number of close pairs in a block of $L$ consecutive girls (with boy blocks of $\geq 50$ on both sides, so no close pairs between blocks):

For a girl at position $d$ ($0 \leq d \leq L-1$) in the block, the number of girls within distance 50 (excluding herself) is:
- To the right: $\min(L - 1 - d, 50)$.
- To the left: $\min(d, 50)$.
- Total: $\min(d, 50) + \min(L - 1 - d, 50)$.

Sum over all girls in the block: $\sum_{d=0}^{L-1} [\min(d, 50) + \min(L-1-d, 50)]$.

By symmetry, this is $2 \sum_{d=0}^{L-1} \min(d, 50)$... no, it's $\sum_{d=0}^{L-1} \min(d, 50) + \sum_{d=0}^{L-1} \min(L-1-d, 50) = 2 \sum_{d=0}^{L-1} \min(d, 50)$ (by substituting $d \to L-1-d$ in the second sum).

$\sum_{d=0}^{L-1} \min(d, 50) = \sum_{d=0}^{50} d + \sum_{d=51}^{L-1} 50 = \frac{50 \cdot 51}{2} + 50(L - 51) = 1275 + 50L - 2550 = 50L - 1275$ (for $L \geq 51$).

For $L \leq 51$: $\sum_{d=0}^{L-1} \min(d, 50) = \sum_{d=0}^{L-1} d = \frac{(L-1)L}{2}$.

So the number of close pairs in a block of $L$ (with $L \leq 51$) is $2 \cdot \frac{(L-1)L}{2} / 2$... wait, I need to be careful. The sum $\sum_{d=0}^{L-1} [\min(d,50) + \min(L-1-d,50)]$ counts, for each girl, the number of close girls. The total number of close pairs is this sum divided by 2 (each pair counted twice).

For $L \leq 51$: sum $= 2 \sum_{d=0}^{L-1} d = 2 \cdot \frac{(L-1)L}{2} = L(L-1)$. Close pairs $= L(L-1)/2 = \binom{L}{2}$. Makes sense—all pairs are close.

For $L \geq 52$: sum $= 2(50L - 1275) = 100L - 2550$. Close pairs $= (100L - 2550)/2 = 50L - 1275$.

Now, total close pairs for the block construction with blocks $b_1, \ldots, b_r$ (each $\leq 51$, with boy blocks $\geq 50$):

Close pairs $= \sum_{i: b_i \leq 51} \binom{b_i}{2} + \sum_{i: b_i \geq 52} (50 b_i - 1275)$.

For the construction with blocks 50, 50, 50, 51:
Close pairs $= 3 \binom{50}{2} + \binom{51}{2} = 3 \times 1225 + 1275 = 3675 + 1275 = 4950$. ✓

For blocks 100, 101 (with boy blocks of 100):
Close pairs $= (50 \times 100 - 1275) + (50 \times 101 - 1275) = 3725 + 3775 = 7500$. Much more!

For blocks 50, 50, 50, 51 (boy blocks 50): 4950.
For blocks 40, 40, 40, 40, 41 (boy blocks 40): but boy blocks < 50, so cross-block pairs exist. Need to account for those.

Hmm, with boy blocks < 50, there are cross-block close pairs, which increases the total. So the block construction with boy blocks $\geq 50$ is better for minimizing close pairs.

Among constructions with boy blocks $\geq 50$: we need $\sum b_i = 201$ and $\sum a_i = 200$ with $a_i \geq 50$, so $r \leq 4$.

With $r = 4$: $a_i = 50$ each, $b_i$ summing to 201. Close pairs $= \sum \binom{b_i}{2}$ (if all $b_i \leq 51$) or with the larger formula.

To minimize $\sum \binom{b_i}{2}$ with $\sum b_i = 201$ and $b_i \leq 51$ (to avoid the larger formula, but actually even with $b_i > 51$ the formula $50b_i - 1275$ vs $\binom{b_i}{2}$... for $b_i = 51$: $\binom{51}{2} = 1275$ and $50 \times 51 - 1275 = 1275$. Same. For $b_i = 52$: $\binom{52}{2} = 1326$ vs $50 \times 52 - 1275 = 1325$. So the formula gives slightly less. But $b_i = 52$ means all 52 girls are good, which is bad for $G$.)

Anyway, to minimize close pairs with $r = 4$ and $\sum b_i = 201$: by convexity, we want the $b_i$ as equal as possible. $201 / 4 = 50.25$, so blocks of 50, 50, 50, 51. Close pairs $= 3 \times 1225 + 1275 = 4950$.

With $r = 3$: $a_i$ summing to 200, each $\geq 50$. $b_i$ summing to 201. To minimize close pairs, equal blocks: 67, 67, 67. Close pairs $= 3 \times (50 \times 67 - 1275) = 3 \times 2075 = 6225$. More than 4950.

With $r = 2$: $b_i$ = 100, 101. Close pairs $= 7500$. More.

So the minimum close pairs with block structure is 4950, achieved by $r = 4$, blocks 50, 50, 50, 51.

But could a non-block arrangement have fewer close pairs? Let me think...

Actually, the minimum number of close pairs over ALL arrangements (not just block arrangements) might be even lower. But I suspect the block arrangement is optimal or near-optimal.

Hmm, but I don't need to minimize close pairs. I need to minimize $G$. Let me think about whether $G = 51$ is truly optimal.

Let me try to construct an arrangement with $G < 51$.

Idea: What if we don't use a pure block structure? For instance, what if we have 4 boy blocks of 50, but the girl blocks are not all consecutive? Well, in a circle with alternating boy and girl blocks, the girl blocks are determined.

What if we have 5 boy blocks, some smaller than 50? Let's try 5 boy blocks of 40 each (total 200) and 5 girl blocks summing to 201.

As computed earlier, with boy blocks of 40, a girl block of size $b$ has some good girls. Let me compute for $b = 40$:

For a girl at distance $d$ from the left edge of a block of 40, with boy blocks of 40 on both sides:

If $d \geq 10$ and $d \leq 29$ (i.e., $b - 1 - d = 39 - d \geq 10$): $g_i = b - 1 = 39 < 50$. Not good.

If $d < 10$: $g_i = b + 9 - d = 49 - d$. For $d = 0$: $g_i = 49 < 50$. Not good! For $d = 9$: $g_i = 40$... wait, $49 - 9 = 40 < 50$. Not good.

Hmm wait, let me recompute. With boy blocks of 40:

For $d < 10$ and $d \leq b - 11 = 29$: $g_i = b + 9 - d = 49 - d$. For $d = 0$: $g_i = 49$. Not good!

For $d < 10$ and $d > b - 11$ (i.e., $b < 10 + d < 20$): $g_i = 20$. Not good.

For $d \geq 10$ and $d \leq b - 11 = 29$: $g_i = b - 1 = 39$. Not good.

For $d > b - 11 = 29$ and $d \geq 10$: $g_i = d + 10$. For $d = 30$: $g_i = 40$. Not good. For $d = 39$: $g_i = 49$. Not good.

So for $b = 40$ with boy blocks of 40: ALL girls have $g_i \leq 49 < 50$. None are good!

Wait, that's great! Let me double-check.

Girl at $d = 0$ (left edge): left neighbors = 40 boys + 10 girls from previous block. Right neighbors = 39 girls + 11 boys (from right boy block of 40, we get 40 boys but only need 11). Wait, right neighbors: 39 girls (positions $d+1$ to $d+39$, i.e., $b-1 = 39$ girls) + 40 boys + ... but 39 + 40 = 79 > 50, so only 39 girls + 11 boys = 50. $g_{\text{right}} = 39$. $g_i = 10 + 39 = 49$. Not good. ✓

Girl at $d = 39$ (right edge): left neighbors = 39 girls + 11 boys. $g_{\text{left}} = 39$. Right neighbors = 40 boys + 10 girls from next block. $g_{\text{right}} = 10$. $g_i = 39 + 10 = 49$. Not good. ✓

Girl at $d = 20$ (middle): left = 20 girls + 30 boys. $g_{\text{left}} = 20$. Right = 19 girls + 31 boys. $g_{\text{right}} = 19$. $g_i = 39$. Not good. ✓

So with 5 boy blocks of 40 and 5 girl blocks of 40 each (total girls = 200), all girls have $g_i \leq 49$. But we need 201 girls, not 200!

So we need one extra girl. We can make one girl block of size 41 instead of 40.

For $b = 41$ with boy blocks of 40:

Girl at $d = 0$: $g_i = b + 9 - d = 50$. Good! (Since $d = 0 \leq b - 11 = 30$.)

Wait, $g_i = 49 + 1 - 0 = 50$? Let me recompute. $g_i = b + 9 - d = 41 + 9 - 0 = 50$. Yes, $g_i = 50 \geq 50$. Good!

Girl at $d = 1$: $g_i = 41 + 9 - 1 = 49$. Not good.

Girl at $d = 30$: $g_i = 41 + 9 - 30 = 20$. Not good. (And $d = 30 \leq b - 11 = 30$, so first subcase.)

Girl at $d = 31$: $d > b - 11 = 30$ and $d \geq 10$. $g_i = d + 10 = 41$. Not good.

Girl at $d = 40$ (right edge): $g_i = 40 + 10 = 50$. Good!

So for $b = 41$: good girls at $d = 0$ and $d = 40$. That's 2 good girls.

So with 5 boy blocks of 40 and girl blocks 40, 40, 40, 40, 41: $G = 2$.

Wait, that's way better than 51! Let me verify this more carefully.

Hmm, wait. I need to check whether the "previous girl block has enough girls" assumption holds. When I said "10 girls from previous block," I assumed the previous girl block has $\geq 10$ girls. With blocks of 40, yes, each has 40 $\geq$ 10.

But also, I need to check: when a girl at $d = 0$ in a block of 40 looks left, she sees 40 boys (from the boy block) and then 10 girls from the previous girl block. But the previous girl block is of size 40 (or 41), so it has $\geq 10$ girls. ✓

And when she looks right, she sees 39 girls from her own block, then 11 boys from the right boy block (which has 40 boys, so $\geq 11$). ✓

So the computation is correct. Let me also check the cross-block interactions more carefully.

Circle: B40, G40, B40, G40, B40, G40, B40, G40, B40, G41.

Let me label positions. Total = 5×40 + 4×40 + 41 = 200 + 160 + 41 = 401. ✓

Boy blocks: positions 1-40, 81-120, 161-200, 241-280, 321-360.
Girl blocks: positions 41-80, 121-160, 201-240, 281-320, 361-401.

Girl block 5 (positions 361-401, size 41):
- Position 361 (d=0): left neighbors = positions 311-360. Positions 311-320: girls (10), positions 321-360: boys (40). $g_{\text{left}} = 10$. Right neighbors = positions 362-401. All girls (40). $g_{\text{right}} = 40$. $g_i = 10 + 40 = 50$. Good. ✓

- Position 401 (d=40): left neighbors = positions 351-400. Positions 351-360: boys (10), positions 361-400: girls (40). $g_{\text{left}} = 40$. Right neighbors = positions 1-40 (wrapping around). Wait, position 401 + 1 = 402 → 1 (mod 401). So right neighbors = positions 1-50. Positions 1-40: boys (40), positions 41-50: girls (10). $g_{\text{right}} = 10$. $g_i = 40 + 10 = 50$. Good. ✓

- Position 381 (d=20, middle): left = 371-390. Wait, left neighbors of 381 are 381-50=331 to 380. Positions 331-360: boys (30), positions 361-380: girls (20). $g_{\text{left}} = 20$. Right = 382-401. Girls (20). $g_{\text{right}} = 20$. $g_i = 40$. Not good. ✓

Girl block 1 (positions 41-80, size 40):
- Position 41 (d=0): left = 1-40. Boys (40). $g_{\text{left}} = 0$. Right = 42-80. Girls (39), then position 81-91: boys (11). Wait, right neighbors are 42 to 91 (50 positions). 42-80: girls (39), 81-91: boys (11). $g_{\text{right}} = 39$. $g_i = 0 + 39 = 39$. Not good.

Hmm wait, that doesn't match my formula. My formula said $g_i = b + 9 - d = 40 + 9 - 0 = 49$ for $d = 0$. But I'm getting 39. Let me recheck.

Oh, I think the issue is that the previous girl block (block 5, positions 361-401) is not adjacent to block 1 on the left. The left of block 1 is boy block 5 (positions 321-360), and before that is girl block 4 (positions 281-320).

Wait, the circle is: B1(1-40), G1(41-80), B2(81-120), G2(121-160), B3(161-200), G3(201-240), B4(241-280), G4(281-320), B5(321-360), G5(361-401).

So the left neighbor of G1 is B1 (positions 1-40), and the left of B1 is G5 (positions 361-401).

For position 41 (d=0 in G1): left neighbors = positions -9 to 40 = positions 393-401, 1-40. Positions 393-401: girls (9, from G5), positions 1-40: boys (40). Wait, 41 - 50 = -9, which mod 401 is 392. So left neighbors are positions 392 to 40 (going left from 41): 392, 393, ..., 401, 1, 2, ..., 40. That's 50 positions.

Positions 392-401: 10 positions. G5 is 361-401, so 392-401 are all girls (10 girls). Positions 1-40: boys (40). $g_{\text{left}} = 10$.

Right neighbors: 42-91. Positions 42-80: girls (39), positions 81-91: boys (11). $g_{\text{right}} = 39$.

$g_i = 10 + 39 = 49$. Not good. ✓ This matches the formula now!

I made an error before. The left neighbors wrap around through G5, not just B1. Let me recheck position 41.

Position 41's 50 left neighbors: positions 41-50=−9 ≡ 392 (mod 401) up to position 40. So positions 392, 393, ..., 401, 1, 2, ..., 40. That's 10 + 40 = 50 positions. Positions 392-401 are in G5 (361-401), so 10 girls. Positions 1-40 are in B1, so 40 boys. $g_{\text{left}} = 10$. ✓

So $g_i = 10 + 39 = 49$. Not good. ✓

Great, so the formula is correct. Let me recheck the G5 block (size 41).

Position 361 (d=0 in G5): left neighbors = 311-360. Positions 311-320: G4 (281-320), so 10 girls. Positions 321-360: B5, so 40 boys. $g_{\text{left}} = 10$. Right neighbors = 362-411 = 362-401, 1-10. Positions 362-401: G5, 40 girls. Positions 1-10: B1, 10 boys. $g_{\text{right}} = 40$. $g_i = 10 + 40 = 50$. Good. ✓

Position 401 (d=40 in G5): left = 351-400. Positions 351-360: B5, 10 boys. Positions 361-400: G5, 40 girls. $g_{\text{left}} = 40$. Right = 1-50. Positions 1-40: B1, 40 boys. Positions 41-50: G1, 10 girls. $g_{\text{right}} = 10$. $g_i = 40 + 10 = 50$. Good. ✓

So $G = 2$ (only positions 361 and 401 are good). That's much better than 51!

Can we do even better? Let me try 5 girl blocks of 40, 40, 40, 41, 40 and see if we can reduce to $G = 2$ or even $G = 0$.

Wait, we need $\sum b_i = 201$ with 5 blocks. $5 \times 40 = 200$, so one block must be 41. With the 41-block, we get 2 good girls (at the two edges). So $G = 2$.

Can we use more blocks? 6 boy blocks of size $200/6 \approx 33.3$, say 34, 33, 33, 33, 33, 34 (sum 200). 6 girl blocks summing to 201, say 34, 33, 34, 33, 34, 33 (sum 201). With boy blocks of ~33 < 40, the "leak" from neighboring girl blocks is larger.

For a girl at $d = 0$ in a block of size $b$ with boy blocks of size $a$ on both sides:
- Left: $a$ boys + $(50 - a)$ girls from previous block (if previous block has $\geq 50 - a$ girls).
- Right: $(b - 1)$ girls + $(50 - (b-1))$ boys from right boy block (if $b - 1 \leq 50$ and right boy block $\geq 50 - (b-1)$). If $50 - (b-1) > a$, then we also get girls from the next-next block.

With $a = 33, b = 34$:
- Left: 33 boys + 17 girls from previous block. $g_{\text{left}} = 17$.
- Right: 33 girls + 17 boys (from right boy block of 33, but we need 17, and 33 ≥ 17). $g_{\text{right}} = 33$.
- $g_i = 17 + 33 = 50$. Good!

Hmm, so with $a = 33, b = 34$: edge girls have $g_i = 50$, which is good. That's not better.

Let me try $a = 34, b = 33$:
- Left: 34 boys + 16 girls. $g_{\text{left}} = 16$.
- Right: 32 girls + 18 boys. $g_{\text{right}} = 32$.
- $g_i = 16 + 32 = 48$. Not good.

And for a girl at $d = 16$ (middle-ish):
- Left: 16 girls + 34 boys. $g_{\text{left}} = 16$.
- Right: 16 girls + 34 boys. $g_{\text{right}} = 16$.
- $g_i = 32$. Not good.

For $d = 0$: $g_i = 16 + 32 = 48$. Not good.
For $d = 32$ (right edge): $g_{\text{left}} = 32$, $g_{\text{right}} = 16$. $g_i = 48$. Not good.

So with $a = 34, b = 33$: all girls have $g_i \leq 48$. Not good.

But we need $\sum b_i = 201$ with 6 blocks. If all $b_i = 33$: $6 \times 33 = 198 < 201$. Need 3 more. So blocks like 34, 33, 34, 33, 34, 33 (sum 201).

For $b = 34$ with $a = 34$: edge girl has $g_i = 16 + 33 = 49$. Not good!

Wait, let me recompute. $a = 34, b = 34$:
- $d = 0$: left = 34 boys + 16 girls. $g_{\text{left}} = 16$. Right = 33 girls + 17 boys. $g_{\text{right}} = 33$. $g_i = 49$. Not good!
- $d = 33$ (right edge): left = 33 girls + 17 boys. $g_{\text{left}} = 33$. Right = 34 boys + 16 girls. $g_{\text{right}} = 16$. $g_i = 49$. Not good.
- $d = 17$ (middle): left = 17 girls + 33 boys. $g_{\text{left}} = 17$. Right = 16 girls + 34 boys. $g_{\text{right}} = 16$. $g_i = 33$. Not good.

So with $a = 34, b = 34$: all girls have $g_i \leq 49$. Not good!

So if we use 6 boy blocks of 34, 33, 33        — AI历史解题过程（thinking）
#   polymath_03073         — 题目ID

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
  <problem_id>polymath_03073</problem_id>
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

Let $n=200$ and $k=50$. There are $2n+1$ students standing in a circle. Suppose that $n+1$ of the students are girls, and the other $n$ are boys. Each student $S$ has $2k$ neighbors: the $k$ students closest to $S$ on the right, and the $k$ students closest to $S$ on the left. Let $G$ be the number of girls who have at least $k$ girls among their $2k$ neighbors. What is the minimum possible value of $G$?

## Standard Solution

The original problem asks to prove that there is at least one such girl, which means $G \ge 1$. The solution shows that by defining $b_i = a_i + a_{i-k-1} - 1$, the sum over a full cycle is $\sum_{i=1}^{2n+1} b_i = 1$. By applying Raney's Lemma or the Gas Station Theorem logic, it establishes the existence of at least one index $i$ such that $a_i = 1$ (the student is a girl) and the sum of her $2k$ neighbors is at least $k$. Since the proof only guarantees the existence of one such student, the minimum value is 1.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have $2n+1 = 401$ students in a circle, $n+1 = 201$ girls and $n = 200$ boys. $k = 50$. Each student has $2k = 100$ neighbors (50 on each side). $G$ = number of girls with at least $k = 50$ girls among their 100 neighbors. Find minimum $G$.

Let me think about this carefully.

Let me denote the circle as a sequence of 0s (boys) and 1s (girls), with 201 ones and 200 zeros, arranged in a circle of 401.

For each girl at position $i$, her neighbors are the 50 closest on the left and 50 closest on the right (100 total). She counts as "good" if at least 50 of these 100 are girls.

We want to minimize the number of good girls.

Let me think about this more generally. Let $n = 200, k = 50$. So $n = 4k$.

Total students: $2n+1 = 401$. Girls: $n+1 = 201$, Boys: $n = 200$.

Let me think about a double-counting / averaging argument first.

For each girl, let $g_i$ = number of girls among her 100 neighbors. We want to count girls with $g_i \geq 50$.

Sum of $g_i$ over all girls: Each ordered pair of girls $(A, B)$ where $B$ is a neighbor of $A$ contributes 1. For two girls at distance $d$ (circular distance, $1 \leq d \leq 200$), they are neighbors of each other if $d \leq 50$ (on one side) — actually, $B$ is a neighbor of $A$ if $B$ is among the 50 closest on left or 50 closest on right, i.e., circular distance $\leq 50$.

So $\sum g_i = \sum_{\text{pairs of girls}} 2 \cdot [\text{dist} \leq 50]$... no wait, it's ordered pairs. $\sum g_i = \sum_{\text{ordered pairs } (A,B), A \neq B, \text{both girls}} [\text{dist}(A,B) \leq 50]$.

Hmm, this depends on the arrangement. Let me think differently.

Actually, let me think about what arrangement minimizes $G$.

Intuition: To minimize the number of girls with many girl-neighbors, we want to spread out the girls... but there are more girls than boys (201 vs 200), so girls are the majority. 

Actually, let me think about it. If we alternate G and B as much as possible: 201 girls, 200 boys. In a circle of 401, we can't perfectly alternate. We'd have something like GBGBGB...GBG with one extra G somewhere, creating a GG pair.

But with alternating, each girl has neighbors that are mostly boys. Let's see: in alternating arrangement G B G B G B ... the 50 neighbors on each side of a girl would be B G B G B G ... so 25 boys and 25 girls on each side, total 50 boys and 50 girls. So $g_i = 50$ for most girls, which means $g_i \geq 50$, so they're all good. That gives $G = 201$, which is bad (we want minimum).

Hmm, so alternating is bad. We want to cluster girls together so that some girls have many girl neighbors (good) but others have few (bad), minimizing the total count of good ones.

Wait, but we want to MINIMIZE $G$, the number of good girls. So we want as many girls as possible to have FEW girl neighbors.

Strategy: cluster the boys together to create regions where girls are surrounded by boys.

Actually, let me reconsider. If we put all 200 boys consecutively, then the remaining 201 girls are consecutive. A girl in the middle of the girl block has 50 girls on left and 50 girls on right = 100 girls, so $g_i = 100 \geq 50$, good. A girl near the boundary of the girl block... Let's think. The girl block has 201 girls. The first girl (adjacent to a boy) has 1 boy on one side (the immediate neighbor) and then 49 more positions on that side which are girls (since the boy block is on the other side). Wait, let me set up coordinates.

Place 200 boys at positions 1-200, and 201 girls at positions 201-401 (circularly). Position 200 is a boy, position 201 is a girl, position 401 is a girl, position 1 is a boy.

Girl at position 201: left neighbors (positions 200, 199, ..., 151) = 1 boy (pos 200) + 49 boys (pos 199-151) = 50 boys. Right neighbors (positions 202-251) = 50 girls. So $g_i = 50$. Good.

Girl at position 202: left neighbors (201, 200, ..., 152) = 1 girl (201) + 49 boys = 1 girl + 49 boys. Right neighbors (203-252) = 50 girls. $g_i = 51$. Good.

Girl at position 250: left neighbors (249, 248, ..., 200) = 49 girls + 1 boy = 49 girls. Right neighbors (251-300) = 50 girls. $g_i = 99$. Good.

Girl at position 251: left = 250 girls (positions 250 down to 201, that's 50 girls). Right = 252-301 = 50 girls. $g_i = 100$. Good.

So in this arrangement, essentially all girls are good. $G = 201$. That's the maximum, not minimum.

So clustering girls is bad for minimization. We need to spread girls out but in a way that many girls have $g_i < 50$.

Hmm, so we want girls to be isolated, surrounded by boys. But there are 201 girls and only 200 boys. 

Let me think about it differently. Consider a girl $S$. She has 100 neighbors. For $g_i < 50$, she needs at least 51 boys among her 100 neighbors. But there are only 200 boys total. 

Let me think about the complement. Let $b_i$ = number of boys among the 100 neighbors of girl $i$. Then $g_i = 100 - b_i$, and $g_i \geq 50 \iff b_i \leq 50$. So $G$ = number of girls with $b_i \leq 50$, and we want to minimize this, i.e., maximize the number of girls with $b_i \geq 51$.

So we want as many girls as possible to have at least 51 boy-neighbors.

Total boy-neighbor count: $\sum_{i \text{ girl}} b_i = \sum_{\text{ordered pairs } (G, B)} [\text{dist} \leq 50]$.

For a boy at position $j$, the number of girls within distance 50 is the number of girls in positions $j-50, \ldots, j-1, j+1, \ldots, j+50$ (circularly). Call this $c_j$. Then $\sum b_i = \sum_{j \text{ boy}} c_j$.

To maximize the number of girls with $b_i \geq 51$, we'd want to concentrate the boy-neighbor counts. 

Hmm, let me think about upper bounds. If $m$ girls have $b_i \geq 51$ and $201 - m$ girls have $b_i \leq 50$ (actually $b_i$ can be at most 100, and at least... well, at least 0). 

$\sum b_i \geq 51m + 0 \cdot (201 - m) = 51m$.

Also $\sum b_i = \sum_{j \text{ boy}} c_j$. What's the maximum of $\sum_{j \text{ boy}} c_j$?

Each boy $j$ has $c_j \leq 100$ (at most 100 neighbors, all could be girls). But more usefully, $\sum_{j \text{ boy}} c_j = \sum_{\text{ordered pairs } (G, B), \text{dist} \leq 50} 1$.

The total number of ordered pairs $(G, B)$ with distance $\leq 50$... For each girl, she has 100 neighbors, at most 100 of which are boys. So $\sum b_i \leq 201 \cdot 100 = 20100$. But also $\sum b_i \leq 200 \cdot 100 = 20000$ (each boy has at most 100 girl neighbors). So $\sum b_i \leq 20000$.

So $51m \leq 20000$, giving $m \leq 392.16...$, so $m \leq 392$. But $m \leq 201$ anyway, so this bound is $m \leq 201$, not useful.

Let me think more carefully. We need a better upper bound on $\sum b_i$.

Actually, let's think about it as: for each unordered pair $(G, B)$ at distance $d \leq 50$, it contributes 2 to $\sum b_i$ (once for the girl counting the boy, once for... no). Wait, $\sum_{i \text{ girl}} b_i$ counts, for each girl, the boys in her neighborhood. And $\sum_{j \text{ boy}} c_j$ counts, for each boy, the girls in his neighborhood. These are the same sum (both count ordered pairs $(G, B)$ at distance $\leq 50$). Yes.

So $\sum b_i = \sum_{j \text{ boy}} c_j$ where $c_j$ = number of girls within distance 50 of boy $j$.

Now, the key constraint is the arrangement. Let me think about what arrangement maximizes $\sum b_i$ or more precisely, what arrangement allows the most girls to have $b_i \geq 51$.

Let me think about small cases or a pattern.

Alternative approach: Think of it as a sliding window. For each position $i$ (a student), define $w_i$ = number of girls in the window of 100 neighbors (positions $i-50$ to $i+50$, excluding $i$). If position $i$ is a girl, then $g_i = w_i$ and she's good if $w_i \geq 50$.

Note: the window of 100 neighbors of position $i$ is positions $i-50, \ldots, i-1, i+1, \ldots, i+50$, which is 100 positions. Equivalently, it's the window $\{i-50, \ldots, i+50\} \setminus \{i\}$, which is 101 positions minus 1.

Let $W_i$ = number of girls in positions $i-50, \ldots, i+50$ (101 positions including $i$). If position $i$ is a girl, then $w_i = W_i - 1$, and she's good iff $W_i - 1 \geq 50$ iff $W_i \geq 51$.

If position $i$ is a boy, then $w_i = W_i$ (the number of girls in the 101-window, since $i$ itself is a boy).

So: a girl at position $i$ is good iff $W_i \geq 51$.

We want to minimize the number of girls $i$ with $W_i \geq 51$.

Now, $W_i$ is the number of girls in a window of 101 consecutive positions (centered at $i$). There are 401 such windows (one for each position), and they're all the windows of length 101 in the circle.

The sum $\sum_{i=1}^{401} W_i = 101 \cdot 201 = 20301$ (each girl is in 101 windows).

Average $W_i = 20301 / 401 \approx 50.63$.

So on average, $W_i \approx 50.63$, which is just above 51... wait, 50.63 < 51. So the average is below 51.

We want to minimize the number of positions $i$ that are girls AND have $W_i \geq 51$.

Hmm, let me think about this as an optimization problem. We have 201 girls and 200 boys in a circle of 401. We want to place them to minimize the count of girl-positions with $W_i \geq 51$.

Let me think about what happens if we try to make $W_i < 51$ for as many girls as possible, i.e., $W_i \leq 50$ for as many girls as possible.

If a girl at position $i$ has $W_i \leq 50$, that means among the 101 positions centered at $i$, at most 50 are girls, so at least 51 are boys. But there are only 200 boys total. 

Let me think about a construction. Suppose we arrange the circle as blocks. Let's try to have blocks of boys that are large enough to "cover" girls with few girl-neighbors.

Consider a girl who is isolated, surrounded by many boys. If a girl has 50 boys on her left and 50 boys on her right (all 100 neighbors are boys), then $b_i = 100$, $g_i = 0 < 50$, not good. But this requires 100 boys near her, and we only have 200 boys.

Let me think about a periodic construction. Suppose we have a pattern that repeats. 

Let me try: a block of $a$ boys followed by a block of $b$ girls, repeating. We need $a \cdot r = 200$ and $b \cdot r = 201$ for some number of repeats $r$. Since $\gcd(200, 201) = 1$, we'd need $r = 1$, which is the all-boys-then-all-girls case (bad).

Let me try a different approach. Let me think about two types of blocks.

Actually, let me think about the problem more carefully with the specific numbers. $n = 200, k = 50$, so $n = 4k$.

Let me consider a general approach. Place the students so that there are some "blocks of consecutive boys" interspersed with "blocks of consecutive girls."

For a girl in a block of consecutive girls of length $L$, her girl-neighbors depend on her position in the block and the sizes of neighboring boy blocks.

Let me think about a girl at the center of a large girl block. She'll have many girl neighbors. A girl at the edge of a girl block, adjacent to a large boy block, will have fewer girl neighbors.

To minimize $G$, we want most girls to be at the edges of girl blocks, adjacent to large boy blocks. But the total number of boys is limited.

Let me try a specific construction. Suppose we have blocks of 100 boys and 100 girls, alternating... but 200 boys and 201 girls. So: 100 boys, 100 girls, 100 boys, 101 girls. That's 4 blocks in a circle.

Let me compute $W_i$ for girls in different positions.

Block 1: positions 1-100, boys.
Block 2: positions 101-200, girls.
Block 3: positions 201-300, boys.
Block 4: positions 301-401, girls.

Girl at position 101 (start of block 2, adjacent to boy at 100):
$W_{101}$ = girls in positions 51-151. Positions 51-100 are boys (50 boys), position 101 is a girl, positions 102-151 are girls (50 girls). So $W_{101} = 51$. Good (since $W_i \geq 51$).

Girl at position 102: $W_{102}$ = girls in 52-152. Positions 52-100: boys (49). Position 101-152: girls (52). $W_{102} = 52$. Good.

Girl at position 150: $W_{150}$ = girls in 100-200. Position 100: boy. Positions 101-200: girls (100). $W_{150} = 100$. Good.

Girl at position 200 (end of block 2, adjacent to boy at 201): $W_{200}$ = girls in 150-250. Positions 150-200: girls (51). Positions 201-250: boys (50). $W_{200} = 51$. Good.

So all 100 girls in block 2 have $W_i \geq 51$. Similarly for block 4 (101 girls). So $G = 201$. Still bad.

The issue is that with blocks of 100, the girl blocks are too large—every girl in a block of 100 has at least 51 girls in her 101-window.

What if we make the girl blocks smaller? If a girl block has length $L$, the minimum $W_i$ for a girl in that block is achieved at the edges. For a girl at the edge of a block of length $L$, with boy blocks of length $a$ on one side and $b$ on the other:

The 101-window centered at this girl includes: some boys from the left block, the girl herself, and $L-1$ other girls, and some boys from the right block.

Let me be more precise. Consider a girl at the left edge of a girl block of length $L$, with a boy block of length $a$ to the left and a boy block of length $b$ to the right (of the girl block).

The 50 positions to her left: if $a \geq 50$, all 50 are boys. If $a < 50$, then $a$ boys and $50 - a$ girls (from the girl block wrapping around... no, in a circle with just these blocks).

Hmm, this is getting complicated with the circle. Let me think about it more carefully.

Let me consider a simpler model: a circle made of alternating boy-blocks and girl-blocks. Let the boy blocks have sizes $a_1, a_2, \ldots, a_r$ and girl blocks have sizes $b_1, b_2, \ldots, b_r$, with $\sum a_i = 200, \sum b_i = 201$.

For a girl at position $j$ within girl block $i$ (of size $b_i$), at distance $d$ from the left edge (so $d = 0$ is the leftmost girl, adjacent to boy block $a_i$... wait, I need to be careful about the ordering).

Let me say the circle goes: boy block $a_1$, girl block $b_1$, boy block $a_2$, girl block $b_2$, ..., boy block $a_r$, girl block $b_r$.

A girl at distance $d$ from the left edge of girl block $b_i$ (so $d = 0, 1, \ldots, b_i - 1$; $d = 0$ is adjacent to boy block $a_i$, $d = b_i - 1$ is adjacent to boy block $a_{i+1}$).

Her 50 left neighbors: first $\min(d, 50)$ are girls (from her own block), then if $d < 50$, the next $\min(50 - d, a_i)$ are boys (from boy block $a_i$), and if $d + a_i < 50$, we continue into girl block $b_{i-1}$, etc.

This is getting complex. Let me simplify by assuming all boy blocks are large (size $\geq 50$) and all girl blocks are small (size $\leq 50$ or so).

If boy blocks are all $\geq 50$ and girl blocks are all $\leq 51$, let's see what happens.

For a girl at the left edge ($d = 0$) of a girl block of size $b$:
- 50 left neighbors: all from boy block $a_i$ (if $a_i \geq 50$), all boys. So 0 girls on left.
- 50 right neighbors: $\min(50, b-1)$ girls from her own block, then boys from the next boy block.
  - If $b - 1 \geq 50$, i.e., $b \geq 51$: 50 girls on right. $g_i = 50$. Good.
  - If $b - 1 < 50$, i.e., $b \leq 50$: $b - 1$ girls on right, $50 - (b-1)$ boys. $g_i = b - 1 < 50$. Not good!

For a girl at distance $d$ from the left edge ($1 \leq d \leq b-1$):
- Left neighbors: $\min(d, 50)$ girls from own block, then boys.
  - If $d \leq 50$: $d$ girls on left (assuming $a_i \geq 50 - d$, which is true if $a_i \geq 50$).
- Right neighbors: $\min(50, b - 1 - d)$ girls from own block, then boys.
  - If $b - 1 - d \geq 50$: 50 girls on right. But $b \leq 50$ means $b - 1 - d \leq 49 < 50$. So $b - 1 - d$ girls on right.
  
  So $g_i = d + (b - 1 - d) = b - 1$ (when $d \leq 50$ and $b - 1 - d \leq 49$, which is always true when $b \leq 50$).
  
  Wait, that's interesting. If $b \leq 50$ and both neighboring boy blocks are $\geq 50$, then for any girl in this block, $g_i = b - 1$.

  Because: left neighbors include $d$ girls (from own block) + $(50 - d)$ boys (from left boy block, since $a_i \geq 50 \geq 50 - d$). Right neighbors include $(b - 1 - d)$ girls (from own block) + $(50 - (b - 1 - d))$ boys (from right boy block, since $a_{i+1} \geq 50 \geq 50 - (b-1-d)$). So $g_i = d + (b - 1 - d) = b - 1$.

So if $b \leq 50$, all girls in this block have $g_i = b - 1 < 50$, so none are good!

And if $b = 51$, all girls have $g_i = 50$, so all are good.

Wait, let me recheck for $b = 51$. Girl at $d = 0$: left = 0 girls, right = $\min(50, 50) = 50$ girls. $g_i = 50$. Good. Girl at $d = 25$: left = 25 girls, right = $\min(50, 25) = 25$ girls. $g_i = 50$. Good. Girl at $d = 50$: left = 50 girls, right = $\min(50, 0) = 0$ girls. $g_i = 50$. Good. So yes, all 51 girls are good.

So the threshold is exactly at $b = 51$: blocks of $\leq 50$ girls contribute 0 good girls, blocks of $\geq 51$ girls contribute all good girls (assuming boy blocks are $\geq 50$).

Now, we have 201 girls to distribute into blocks, and 200 boys into blocks, with boy blocks $\geq 50$.

If we have $r$ boy blocks each of size $\geq 50$, then $r \leq 4$ (since $200 / 50 = 4$). And we have $r$ girl blocks.

With $r = 4$: 4 boy blocks of size 50 each, 4 girl blocks summing to 201. To minimize good girls, we want as many girl blocks as possible to have size $\leq 50$. With 4 blocks summing to 201, at most 3 can be $\leq 50$ (since $3 \times 50 = 150 < 201$, the 4th would be $201 - 150 = 51$). Actually, we want to minimize the number of girls in blocks of size $\geq 51$.

If 3 blocks have size 50 and 1 has size 51: good girls = 51 (from the size-51 block). Total girls = 151 + 51 = 201. ✓. $G = 51$.

Can we do better? With 4 blocks: 3 of size 50, 1 of size 51. $G = 51$.

What if we use $r = 3$ boy blocks? Then 3 boy blocks summing to 200, each $\geq 50$. E.g., 66, 67, 67. And 3 girl blocks summing to 201. To minimize good girls: at most 2 blocks $\leq 50$ (since $2 \times 50 = 100$, 3rd = 101). Good girls = 101. Worse.

Or: 2 blocks of 50, 1 block of 100. Girl blocks: 2 of 50, 1 of 101. Good = 101. Worse.

What about $r = 4$ with different sizes? Boy blocks: 50, 50, 50, 50. Girl blocks: 50, 50, 50, 51. $G = 51$.

Can we get $G < 51$? We need all girl blocks to be $\leq 50$, but $\sum b_i = 201$ and with 4 blocks, max sum with all $\leq 50$ is 200 < 201. So at least one block must be $\geq 51$, contributing at least 51 good girls.

But wait—can we use more than 4 boy blocks? If boy blocks can be smaller than 50, our analysis changes. Let me reconsider.

If a boy block has size $a < 50$, then for a girl at the edge of an adjacent girl block, some of her 50 neighbors on that side would be girls from the next girl block (wrapping around the boy block). This could increase $g_i$.

Let me reconsider. With smaller boy blocks, the analysis is more complex. Let me think about whether using more, smaller boy blocks could help.

Suppose we have $r$ boy blocks and $r$ girl blocks, with boy blocks of sizes $a_1, \ldots, a_r$ (sum 200) and girl blocks $b_1, \ldots, b_r$ (sum 201).

For a girl at distance $d$ from the left edge of girl block $b_i$:
- Left neighbors (50 positions): $d$ girls from own block, then $a_i$ boys from boy block $a_i$, then if $d + a_i < 50$, girls from girl block $b_{i-1}$.
- Right neighbors (50 positions): $(b_i - 1 - d)$ girls from own block, then $a_{i+1}$ boys from boy block $a_{i+1}$, then if $(b_i - 1 - d) + a_{i+1} < 50$, girls from girl block $b_{i+1}$.

This is complex. Let me think about whether we can do better than 51.

Actually, let me reconsider the problem. The key insight is that we need at least one "large" girl block (size $\geq 51$) because 201 > 4 × 50 = 200. But maybe with a cleverer arrangement (not just alternating blocks), we can do better.

Wait, but maybe we don't need to use the block structure at all. Let me think about whether a non-block arrangement could achieve $G < 51$.

Hmm, but the block arrangement with $r = 4$ boy blocks of size 50 gives $G = 51$. Let me see if we can prove $G \geq 51$ in general, or find a better construction.

Let me think about a lower bound. 

Consider the 401 windows of size 101 (centered at each position). Each window $W_i$ has $W_i$ girls. $\sum W_i = 101 \times 201 = 20301$.

A girl at position $i$ is good iff $W_i \geq 51$.

Let $G$ = number of good girls. Let $B$ = number of good boys (boys with $W_i \geq 51$, though we don't care about this). Let's think about it differently.

Let $S$ = number of positions $i$ (girl or boy) with $W_i \geq 51$. Then $G \leq S$ (since good girls are a subset of positions with $W_i \geq 51$).

Actually, we want a lower bound on $G$, the number of girls with $W_i \geq 51$.

Hmm, let me think about it from the perspective of the girls. We have 201 girls. For each girl $i$, $W_i \geq 51$ means she's good. We want to minimize the count of such girls.

Let me think about the sum $\sum_{i: \text{girl}} W_i$. This equals $\sum_{i: \text{girl}} (\text{girls in window } i) = \sum_{j: \text{girl}} (\text{number of girl-windows containing } j)$.

For a girl at position $j$, the number of girl-centered windows containing $j$ is the number of girls $i$ with $|i - j|_{\text{circ}} \leq 50$. This depends on the arrangement.

This is getting complicated. Let me try a different approach.

Let me think about the problem as follows. Consider the 201 girls. For each girl, look at her 101-window (centered at her). We want to minimize the number of girls whose 101-window contains $\geq 51$ girls.

Alternative: think of the 401 positions on the circle. Color 201 of them as girls. For each girl-position $i$, let $W_i$ = number of girls in $\{i-50, \ldots, i+50\}$. Minimize $|\{i : \text{girl}, W_i \geq 51\}|$.

Let me think about a potential function or a clever counting argument.

Consider the "sliding window" of size 101. As we slide it around the circle, $W_i$ changes by at most 1 at each step (we lose one position and gain one). The sequence $W_1, W_2, \ldots, W_{401}, W_1$ is a cyclic sequence where consecutive terms differ by at most 1.

$\sum W_i = 20301$, average $\approx 50.63$.

Now, the girls are at some subset of positions. We want to minimize the number of girl-positions where $W_i \geq 51$.

Key idea: Since the average is 50.63, and $W_i$ changes by at most 1, there must be many positions where $W_i \geq 51$. Specifically, since the average is above 50, there must be positions with $W_i \geq 51$.

But we want to minimize the number of GIRL positions with $W_i \geq 51$, not the total number of positions with $W_i \geq 51$.

Hmm, can we arrange it so that the positions with $W_i \geq 51$ are mostly boys?

Let me think about this. In the block construction (4 boy blocks of 50, 4 girl blocks of 50, 50, 50, 51):

The $W_i$ values: in a boy block of 50, the $W_i$ values range from... let me compute.

Boy block of 50 (positions 1-50), girl block of 50 (positions 51-100), boy block of 50 (positions 101-150), girl block of 50 (positions 151-200), boy block of 50 (positions 201-250), girl block of 51 (positions 251-301), boy block of 50 (positions 302-351), girl block of 50 (positions 352-401).

Wait, let me recompute. 4 boy blocks of 50 = 200, 4 girl blocks of 50, 50, 50, 51 = 201. Total = 401. ✓

Let me compute $W_i$ for a few positions.

Position 1 (boy, in boy block 1-50): window is positions 352-401 (wait, 1-50=51, so positions 1-50 to 1+50 = positions -49 to 51 = positions 353-401, 1-51). Hmm, let me use modular arithmetic. Positions 1 to 401. Window for position $i$ is $\{i-50, \ldots, i+50\} \pmod{401}$.

Position 1: window = $\{352, \ldots, 401, 1, 2, \ldots, 51\}$. That's positions 352-401 (50 positions) + positions 1-51 (51 positions) = 101 positions. Positions 352-401 are girl block (50 girls). Positions 1-50 are boy block (50 boys). Position 51 is a girl. So $W_1 = 50 + 1 = 51$.

Hmm, so position 1 (a boy) has $W_1 = 51 \geq 51$. So this boy is "good" (in the sense of $W_i \geq 51$), but we only count girls.

Position 25 (boy, middle of boy block): window = $\{25-50, \ldots, 25+50\} = \{-25, \ldots, 75\} = \{377, \ldots, 401, 1, \ldots, 75\}$. Positions 377-401: 25 positions, all in girl block 352-401 (girls). Positions 1-50: boys. Positions 51-75: girls (25 girls). $W_{25} = 25 + 25 = 50 < 51$. Not good.

Position 50 (boy, end of boy block): window = $\{0, \ldots, 100\} = \{401, 1, \ldots, 100\}$. Position 401: girl. Positions 1-50: boys. Positions 51-100: girls (50). $W_{50} = 1 + 50 = 51$. Good (but it's a boy).

Position 51 (girl, start of girl block): window = $\{1, \ldots, 101\}$. Positions 1-50: boys. Positions 51-100: girls (50). Position 101: boy. $W_{51} = 50$. Not good! Great, this girl is not good.

Wait, but earlier I computed that a girl at the edge of a girl block of size 50 (with boy blocks of size 50 on both sides) has $g_i = 49$, so $W_i = 50$. Let me recheck. $W_{51}$ = girls in positions 1-101 = positions 51-100 (50 girls). $W_{51} = 50 < 51$. Not good. ✓

Position 75 (girl, middle of girl block 51-100): window = $\{25, \ldots, 125\}$. Positions 25-50: boys (26). Positions 51-100: girls (50). Positions 101-125: boys (25). $W_{75} = 50$. Not good. ✓

Position 100 (girl, end of girl block): window = $\{50, \ldots, 150\}$. Position 50: boy. Positions 51-100: girls (50). Positions 101-150: boys (50). $W_{100} = 50$. Not good. ✓

So all 50 girls in the girl block of size 50 have $W_i = 50$, not good. 

Now the girl block of size 51 (positions 251-301):

Position 251 (girl, start): window = $\{201, \ldots, 301\}$. Positions 201-250: boys (50). Positions 251-301: girls (51). $W_{251} = 51$. Good.

Position 276 (girl, middle): window = $\{226, \ldots, 326\}$. Positions 226-250: boys (25). Positions 251-301: girls (51). Positions 302-326: boys (25). $W_{276} = 51$. Good.

Position 301 (girl, end): window = $\{251, \ldots, 351\}$. Positions 251-301: girls (51). Positions 302-351: boys (50). $W_{301} = 51$. Good.

So all 51 girls in the size-51 block are good. $G = 51$.

Now, can we do better? Let me think about whether $G = 51$ is optimal or if we can achieve $G < 51$.

The constraint is: 201 girls in a circle of 401, and we need at least one "cluster" of girls that forces some to be good.

Let me think about a lower bound argument.

Claim: $G \geq 51$.

Approach: Consider the 201 girls. For each girl $i$, let $W_i$ be the number of girls in her 101-window. We have $\sum_{i: \text{girl}} W_i = ?$.

Actually, $\sum_{i: \text{girl}} W_i = \sum_{i: \text{girl}} \sum_{j: \text{girl}} [|i-j|_{\text{circ}} \leq 50] = \sum_{j: \text{girl}} \sum_{i: \text{girl}} [|i-j| \leq 50]$.

For each girl $j$, the number of girls $i$ with $|i-j| \leq 50$ is the number of girls in $j$'s 101-window, which is $W_j$. So $\sum_{i: \text{girl}} W_i = \sum_{j: \text{girl}} W_j$. That's circular.

Let me instead compute $\sum_{i: \text{girl}} W_i$ differently. $\sum_{i: \text{girl}} W_i = \sum_{i: \text{girl}} |\{j: \text{girl}, |i-j| \leq 50\}|$. This is the number of ordered pairs of girls at circular distance $\leq 50$.

This depends on the arrangement, so it's not a fixed number. Hmm.

Let me try a different approach for the lower bound.

Alternative approach: Think about it in terms of "coverage." 

Consider the girls that are NOT good, i.e., $W_i \leq 50$. For such a girl, her 101-window contains at most 50 girls, meaning at least 51 boys.

Let me think about the boys. There are 200 boys. Each non-good girl "consumes" at least 51 boys in her window. But boys can be shared.

Hmm, let me think about it differently. Let me consider the "girl intervals."

Actually, let me try to think about whether we can beat 51 with a non-block arrangement.

What if we use 5 boy blocks? Then we need 5 boy blocks summing to 200, each at least... well, they don't all need to be $\geq 50$. But if some are $< 50$, the analysis changes.

Let me try: 5 boy blocks of size 40 each (total 200), and 5 girl blocks summing to 201.

With boy blocks of size 40 < 50, a girl at the edge of a girl block might have some girls from the neighboring girl block in her window.

For a girl at the left edge ($d = 0$) of a girl block of size $b$, with boy block of size $a = 40$ to the left:
- 50 left neighbors: 40 boys (from boy block), then 10 girls (from the previous girl block, if it has $\geq 10$ girls).
- So $g_i$ from left = 10 (if previous girl block has $\geq 10$ girls).

- 50 right neighbors: $\min(50, b-1)$ girls from own block, then boys.
  - If $b \leq 51$: $b - 1$ girls from own block, $50 - (b-1)$ boys (if next boy block $\geq 50 - (b-1)$, which is $\leq 50$, and boy block is 40... if $b - 1 \leq 10$, i.e., $b \leq 11$, then $50 - (b-1) \geq 40$, so we need the boy block to be $\geq 50 - (b-1)$. If boy block is 40 and $50 - (b-1) > 40$, i.e., $b < 11$, then we'd also get girls from the next girl block on the right.

This is getting complicated. Let me think about it more carefully for a specific case.

5 boy blocks of 40, 5 girl blocks. Let's say girl blocks are $b_1, \ldots, b_5$ with $\sum b_i = 201$.

For a girl at position $d$ in girl block $i$ (size $b_i$), with boy block of size 40 on each side:

Left neighbors (50): $d$ girls from own block, then 40 boys, then $50 - d - 40 = 10 - d$ girls from previous girl block (if $d < 10$ and previous block has enough).

Right neighbors (50): $b_i - 1 - d$ girls from own block, then 40 boys, then $50 - (b_i - 1 - d) - 40 = 11 - b_i + d$ girls from next girl block (if $b_i - 1 - d < 10$, i.e., $d > b_i - 11$, and next block has enough).

Case 1: $d \geq 10$ and $d \leq b_i - 11$ (i.e., girl is "deep inside" the block, at least 10 from each edge). This requires $b_i \geq 21$.
- Left: $d$ girls + 40 boys. Right: $(b_i - 1 - d)$ girls + 40 boys. But $d + 40 \leq 50$ requires $d \leq 10$, and $d \geq 10$, so $d = 10$. And $b_i - 1 - d + 40 \leq 50$ requires $b_i - 1 - d \leq 10$, i.e., $d \geq b_i - 11$. With $d = 10$, need $b_i \leq 21$. So $b_i = 21, d = 10$.
  - $g_i = 10 + 10 = 20$. Not good.

Case 2: $d < 10$ (near left edge).
- Left: $d$ girls + 40 boys + $(10 - d)$ girls from previous block. $g_{\text{left}} = d + (10 - d) = 10$ (assuming previous block has $\geq 10 - d$ girls).
- Right: $(b_i - 1 - d)$ girls + 40 boys + $(11 - b_i + d)$ girls from next block (if $b_i - 1 - d < 10$).
  - If $b_i - 1 - d \geq 10$ (i.e., $d \leq b_i - 11$): $g_{\text{right}} = b_i - 1 - d$. Total $g_i = 10 + (b_i - 1 - d) = b_i + 9 - d$.
  - If $b_i - 1 - d < 10$ (i.e., $d > b_i - 11$): $g_{\text{right}} = (b_i - 1 - d) + (11 - b_i + d) = 10$. Total $g_i = 10 + 10 = 20$.

So for $d < 10$:
- If $d \leq b_i - 11$: $g_i = b_i + 9 - d$. For $d = 0$: $g_i = b_i + 9$. For $d = 9$: $g_i = b_i$.
- If $d > b_i - 11$ (i.e., $b_i \leq 10 + d < 20$): $g_i = 20$.

For $g_i < 50$, we need:
- In the first subcase: $b_i + 9 - d < 50$, i.e., $b_i < 41 + d$. Since $d < 10$, need $b_i < 51$. So if $b_i \leq 50$, $g_i < 50$ for all $d$ in this range. If $b_i = 51$, $g_i = 51 + 9 - d = 60 - d \geq 51$ for $d \leq 9$. Good.
- In the second subcase: $g_i = 20 < 50$. Not good.

Case 3: $d > b_i - 11$ (near right edge, $d \geq 10$). By symmetry with Case 2 (swapping left/right):
- $g_i = 20$ (if also $d < 10$... no, $d \geq 10$ here).

Hmm, let me redo this. By symmetry (left-right), for $d > b_i - 11$ and $d \geq 10$:
- Right: $(b_i - 1 - d)$ girls + 40 boys + $(11 - b_i + d)$ girls from next block. $g_{\text{right}} = (b_i - 1 - d) + (11 - b_i + d) = 10$.
- Left: $d$ girls + 40 boys + $(10 - d)$ girls from previous block. But $d \geq 10$, so $10 - d \leq 0$, meaning left is just $d$ girls + 40 boys, with $d + 40 \leq 50$ requiring $d \leq 10$. So $d = 10$.
  - $g_{\text{left}} = 10$. Total $g_i = 10 + 10 = 20$.

Wait, I think I need to be more careful. Let me redo this.

For $d \geq 10$: left neighbors are $d$ girls (from own block) + $(50 - d)$ positions which are boys (from left boy block of size 40) and then possibly girls. Since $50 - d \leq 40$ when $d \geq 10$, all $(50 - d)$ are boys. So $g_{\text{left}} = d$.

For $d \leq b_i - 11$ (i.e., $b_i - 1 - d \geq 10$): right neighbors are $(b_i - 1 - d)$ girls + $(50 - (b_i - 1 - d))$ positions. Since $b_i - 1 - d \geq 10$, $50 - (b_i - 1 - d) \leq 40$, so all are boys. $g_{\text{right}} = b_i - 1 - d$.

Total: $g_i = d + (b_i - 1 - d) = b_i - 1$.

For $d > b_i - 11$ and $d \geq 10$ (i.e., $b_i - 1 - d < 10$ and $d \geq 10$): right neighbors are $(b_i - 1 - d)$ girls + 40 boys + $(50 - (b_i - 1 - d) - 40) = (11 - b_i + d)$ girls from next block. $g_{\text{right}} = (b_i - 1 - d) + (11 - b_i + d) = 10$.

Left: $d$ girls (since $d \geq 10$, all 50 left are $d$ girls + $(50-d)$ boys). $g_{\text{left}} = d$.

Total: $g_i = d + 10$.

For this to be $< 50$: $d + 10 < 50$, i.e., $d < 40$. Since $d \leq b_i - 1$ and $d > b_i - 11$, we have $b_i - 10 < d < 40$, which requires $b_i < 50$. If $b_i \leq 49$, then $d \leq 48 < 40$... wait, $d < 40$ is needed. $d$ can be up to $b_i - 1$. If $b_i \leq 40$, then $d \leq 39 < 40$. OK. If $b_i = 49$, $d$ can be up to 48, and $d > 38$. So $d \in \{39, 40, ..., 48\}$. For $d = 39$: $g_i = 49 < 50$. For $d = 40$: $g_i = 50 \geq 50$. Good!

Hmm wait, so for $b_i = 49$ and $d = 40$: $g_i = 40 + 10 = 50 \geq 50$. Good. And for $d = 39$: $g_i = 39 + 10 = 49 < 50$. Not good.

But wait, for $d = 39$ and $b_i = 49$: is $d > b_i - 11 = 38$? Yes, $39 > 38$. And $d \geq 10$? Yes. So $g_i = 39 + 10 = 49$. Not good.

For $d = 40, b_i = 49$: $d > 38$, $d \geq 10$. $g_i = 40 + 10 = 50$. Good.

But also, for $d = 40, b_i = 49$: $d \leq b_i - 11 = 38$? No, $40 > 38$. So we're in the second case. $g_i = 40 + 10 = 50$. Good.

Hmm, so for $b_i = 49$, girls at $d = 40, 41, ..., 48$ are good (9 girls), and girls at $d = 0, ..., 39$ are not good (wait, I need to check $d < 10$ too).

For $d < 10, b_i = 49$: $d \leq b_i - 11 = 38$, so first subcase. $g_i = b_i + 9 - d = 58 - d$. For $d = 0$: $g_i = 58 \geq 50$. Good! For $d = 8$: $g_i = 50$. Good. For $d = 9$: $g_i = 49$. Not good.

Wait, so for $b_i = 49$:
- $d = 0$: $g_i = 58$. Good.
- $d = 1$: $g_i = 57$. Good.
- ...
- $d = 8$: $g_i = 50$. Good.
- $d = 9$: $g_i = 49$. Not good.
- $d = 10$ to $d = 38$: $g_i = b_i - 1 = 48$. Not good.
- $d = 39$: $g_i = 49$. Not good.
- $d = 40$ to $d = 48$: $g_i = d + 10 = 50, 51, ..., 58$. Good.

So good girls in this block: $d = 0..8$ (9 girls) and $d = 40..48$ (9 girls) = 18 good girls out of 49.

That's worse than the block arrangement where a block of 50 has 0 good girls!

So using smaller boy blocks (40 instead of 50) makes things worse because girls "leak" into each other's neighborhoods.

This suggests that larger boy blocks are better, and the optimal is boy blocks of size exactly 50.

Let me verify: with boy blocks of size $\geq 50$, girl blocks of size $\leq 50$ have 0 good girls, and girl blocks of size 51 have all 51 good. With 4 boy blocks of 50 and girl blocks 50, 50, 50, 51, we get $G = 51$.

Can we use boy blocks larger than 50? If boy blocks are larger, we have fewer boy blocks, hence fewer girl blocks, and the girl blocks must be larger (since total is 201). E.g., 3 boy blocks of 67 (total 201, too much). 3 boy blocks summing to 200, e.g., 66, 67, 67. 3 girl blocks summing to 201. Best: 50, 50, 101. Good girls = 101. Worse.

Or 2 boy blocks of 100, 2 girl blocks summing to 201: 50, 151 or 100, 101. Best is 100, 101: good = 101. Or 50, 151: good = 151. Worse.

So 4 boy blocks of 50 is optimal among block arrangements, giving $G = 51$.

But can a non-block arrangement do better? Let me think about this.

The key question: is $G \geq 51$?

Let me try to prove $G \geq 51$.

Approach: Consider the 201 girls on the circle. We want to show at least 51 of them have $W_i \geq 51$.

Equivalently, at most 150 girls can have $W_i \leq 50$.

Let me think about it. Suppose at most 150 girls have $W_i \leq 50$. These 150 girls each have at most 50 girls in their 101-window, meaning at least 51 boys. 

Hmm, let me think about a cleaner argument.

Consider the circle as a sequence of 401 positions. Let's think about "runs" of consecutive girls.

Actually, let me think about the problem differently. Let me consider the complement: boys. There are 200 boys. For each boy, define $W'_i$ = number of boys in his 101-window. Then $W'_i = 101 - W_i$ (since the 101-window has 101 positions, either girl or boy). Wait, no: $W_i$ = number of girls in the 101-window, and the 101-window has 101 positions, so number of boys = $101 - W_i$. So $W'_i = 101 - W_i$.

A girl at position $i$ is good iff $W_i \geq 51$ iff $W'_i \leq 50$ (at most 50 boys in her window).

Now, $\sum_{i=1}^{401} W'_i = 101 \times 200 = 20200$ (each boy is in 101 windows). Average $W'_i = 20200/401 \approx 50.37$.

A girl is good iff $W'_i \leq 50$. We want to minimize the number of girls with $W'_i \leq 50$.

Hmm, I need to think about this more cleverly.

Let me try a direct approach. I'll try to prove that $G \geq n/(2k) \cdot ... $ no, let me think about the specific numbers.

Actually, let me think about a cleaner formulation. Let me use the "sliding window" perspective.

Define $f(i) = W_i$ = number of girls in the window $\{i-50, \ldots, i+50\}$ (101 positions). As $i$ increases by 1, the window shifts by 1: we lose position $i-50$ and gain position $i+51$. So $f(i+1) = f(i) - [\text{pos } i-50 \text{ is girl}] + [\text{pos } i+51 \text{ is girl}]$.

The sequence $f(1), f(2), \ldots, f(401)$ is a cyclic sequence with $f(i+1) - f(i) \in \{-1, 0, 1\}$.

$\sum f(i) = 20301$. Average $\approx 50.63$.

Now, a girl at position $i$ is good iff $f(i) \geq 51$.

We want to minimize the number of girl-positions $i$ with $f(i) \geq 51$.

Let me think about the positions where $f(i) \geq 51$. Since the average is 50.63 > 50, and $f$ changes by at most 1, there's a contiguous arc of the circle where $f \geq 51$ (well, possibly multiple arcs).

Actually, $f$ can go above and below 51 multiple times. But the total "excess" above 50 is $\sum (f(i) - 50) = 20301 - 50 \times 401 = 20301 - 20050 = 251$.

And the total "deficit" below 51 is $\sum (51 - f(i))$ for $f(i) < 51$... hmm, this isn't leading anywhere clean.

Let me try yet another approach. Think about it as: we have 201 girls. We want to show that at least 51 of them are "good" (have $\geq 51$ girls in their 101-window, including themselves).

Consider the girls in order around the circle: $g_1, g_2, \ldots, g_{201}$ (in circular order). Let $d_j$ = circular distance from $g_j$ to $g_{j+1}$ (number of steps, so $d_j \geq 1$ and $\sum d_j = 401$).

For girl $g_j$, the number of girls in her 101-window is the number of $g_l$ with circular distance $\leq 50$ from $g_j$. This is 1 (herself) plus the number of other girls within distance 50.

The girls within distance 50 to the right of $g_j$ are $g_{j+1}, g_{j+2}, \ldots$ as long as the cumulative distance $\leq 50$. Similarly to the left.

Let $r_j$ = number of girls to the right of $g_j$ within distance 50 (i.e., the largest $m$ such that $\sum_{l=0}^{m-1} d_{j+l} \leq 50$, where $d_{j+l}$ is the distance from $g_{j+l}$ to $g_{j+l+1}$). Wait, I need to be careful. The distance from $g_j$ to $g_{j+m}$ is $\sum_{l=0}^{m-1} d_{j+l}$. We need this $\leq 50$.

Similarly, $l_j$ = number of girls to the left of $g_j$ within distance 50.

Then $W_{g_j} = 1 + r_j + l_j$, and $g_j$ is good iff $r_j + l_j \geq 50$.

We want to minimize the number of $j$ with $r_j + l_j \geq 50$.

Now, $r_j$ is the number of girls in $(g_j, g_j + 50]$ (the 50 positions to the right). And $l_j$ is the number of girls in $[g_j - 50, g_j)$ (the 50 positions to the left).

Note that $r_j + l_j$ = number of girls in the 100 neighbors of $g_j$ = $g_j$'s girl-neighbor count.

Also, $r_j$ depends on the gaps $d_j, d_{j+1}, \ldots$. Specifically, $r_j = \max\{m : d_j + d_{j+1} + \cdots + d_{j+m-1} \leq 50\}$.

And $l_j = \max\{m : d_{j-1} + d_{j-2} + \cdots + d_{j-m} \leq 50\}$.

Note that $r_j + l_j$ = number of girls among the 100 neighbors. And $r_j$ counts girls to the right, $l_j$ counts girls to the left.

Key observation: $r_j$ is the number of $d$'s starting from $d_j$ that sum to $\leq 50$, and $l_j$ is the number of $d$'s ending at $d_{j-1}$ that sum to $\leq 50$.

Now, $r_j + l_j \geq 50$ iff $g_j$ is good. We want to minimize the count of good $g_j$'s.

Let me think about the relationship between $r_j$ and the gaps.

If all gaps are 2 (alternating G B G B...), then $r_j = 25$ (since $25 \times 2 = 50$) and $l_j = 25$, so $r_j + l_j = 50$, all good. $G = 201$.

If gaps are large (girls spread out), $r_j$ and $l_j$ are small.

We have $\sum d_j = 401$ and $d_j \geq 1$. There are 201 gaps.

Average gap $= 401/201 \approx 1.995$. So on average, gaps are about 2.

If a gap is 1 (two adjacent girls), that "uses up" less distance, allowing more girls to fit in the 50-distance window.

To minimize good girls, we want $r_j + l_j < 50$ for as many girls as possible. Since $r_j + l_j$ counts girls in the 100-neighborhood, and the average number of girls in a 100-neighborhood (of a girl) is... let me compute.

$\sum_{j=1}^{201} (r_j + l_j) = \sum_j r_j + \sum_j l_j$. 

$\sum_j r_j$ = number of ordered pairs $(g_j, g_l)$ with $g_l$ to the right of $g_j$ at distance $\leq 50$. By symmetry (the circle is symmetric), $\sum_j r_j = \sum_j l_j$. So $\sum_j (r_j + l_j) = 2 \sum_j r_j$.

$\sum_j r_j$ = number of ordered pairs of girls at circular distance $\leq 50$ (in one direction). This is the number of pairs $(j, l)$ with $l > j$ (circularly) and distance $\leq 50$.

Hmm, this depends on the arrangement. Let me think about it differently.

Actually, $\sum_j (r_j + l_j) = \sum_j W_{g_j} - 201$ (since $W_{g_j} = 1 + r_j + l_j$). And $\sum_j W_{g_j} = \sum_{j: \text{girl}} W_j$.

$\sum_{j: \text{girl}} W_j = \sum_{j: \text{girl}} |\{l: \text{girl}, |j - l| \leq 50\}| = $ number of ordered pairs of girls at distance $\leq 50$.

This is arrangement-dependent. But we can bound it.

For each girl $j$, $W_j \leq 101$ (at most 101 girls in 101 positions). Also, $W_j \geq 1$ (at least herself).

The total $\sum_{j: \text{girl}} W_j$ is maximized when girls are clustered (many girls close together) and minimized when spread out.

To minimize $G$ (good girls), we want to minimize $\sum_{j: \text{girl}} W_j$? Not necessarily, but it's related.

If $G$ girls have $W_j \geq 51$ and $201 - G$ girls have $W_j \leq 50$:
$\sum_{j: \text{girl}} W_j \geq 51 G + 1 \cdot (201 - G) = 50 G + 201$.
$\sum_{j: \text{girl}} W_j \leq 101 G + 50 (201 - G) = 51 G + 10050$.

So $G \geq (\sum W_j - 10050) / 51$ and $G \leq (\sum W_j - 201) / 50$.

To get a lower bound on $G$, we need a lower bound on $\sum W_j$.

What's the minimum of $\sum_{j: \text{girl}} W_j$? This is the minimum number of ordered pairs of girls at distance $\leq 50$.

To minimize this, we want to spread girls out as much as possible. But with 201 girls in 401 positions, the average gap is ~2, so girls are close together.

Hmm, let me think about the minimum of $\sum_{j: \text{girl}} W_j$ more carefully.

$\sum_{j: \text{girl}} W_j = \sum_{j: \text{girl}} \sum_{l: \text{girl}} [|j-l| \leq 50] = \sum_{\text{ordered pairs of girls}} [\text{dist} \leq 50]$.

For each unordered pair of girls at distance $d \leq 50$, it contributes 2 to the sum. For $d > 50$ (i.e., $d \geq 51$), it contributes 0. (Note: max circular distance is 200.)

So $\sum W_j = 2 \times |\{\text{unordered pairs of girls at distance} \leq 50\}|$.

To minimize this, we want to maximize the number of pairs at distance $> 50$.

The number of unordered pairs of girls is $\binom{201}{2} = 20100$.

For each pair at distance $d$ (circular distance, $1 \leq d \leq 200$), the pair is "close" if $d \leq 50$ and "far" if $d \geq 51$.

We want to maximize far pairs. For each girl, the number of positions at distance $> 50$ is $401 - 1 - 100 = 300$ (excluding herself and the 100 neighbors). So each girl can have at most 300 far girls. But there are only 200 other girls.

Hmm, this isn't directly helpful. Let me think about it differently.

For a given arrangement, the number of close pairs (distance $\leq 50$) is what we want to minimize. 

Consider the girls as points on a circle of circumference 401. The number of pairs at distance $\leq 50$ is what we want to minimize.

This is related to the "energy" of the point configuration. To minimize close pairs, we want to spread the points evenly.

If girls are perfectly evenly spaced (gap 401/201 ≈ 1.995), the number of girls within distance 50 of any girl is about 50/1.995 ≈ 25 on each side, so about 50 total. So $W_j \approx 51$ for all girls, and all are good. That gives $G = 201$.

If girls are clustered, some have many close neighbors (high $W_j$) and some have few (low $W_j$). The total $\sum W_j$ might be higher or lower.

Actually, let me think about it. When girls are clustered, the close-pair count can be very high within clusters. When spread out, it's more uniform.

To minimize $\sum W_j$ (close pairs), spreading out is better. But spreading out makes all girls good (as we saw). To minimize $G$, we want some girls to have $W_j \leq 50$, which requires clustering (so some girls are "isolated" from other clusters).

This is a trade-off. Let me think about the block construction and compute $\sum W_j$.

Block construction: 4 boy blocks of 50, girl blocks of 50, 50, 50, 51.

For a girl in a block of 50 (with boy blocks of 50 on both sides): $W_j = 50$ (as computed). For a girl in the block of 51: $W_j = 51$.

$\sum W_j = 3 \times 50 \times 50 + 51 \times 51 = 7500 + 2601 = 10101$.

Now, $G = 51$, and $\sum W_j = 10101$. Check: $51 \times 51 + 150 \times 50 = 2601 + 7500 = 10101$. ✓ (51 good girls with $W = 51$, 150 non-good with $W = 50$.)

Can we achieve $\sum W_j < 10101$? If so, potentially $G < 51$.

But actually, $G$ depends on the distribution, not just the sum. Let me think about whether we can have $G < 51$.

Suppose $G = 50$. Then 50 girls have $W_j \geq 51$ and 151 girls have $W_j \leq 50$.

$\sum W_j \geq 51 \times 50 + 1 \times 151 = 2550 + 151 = 2701$. And $\sum W_j \leq 101 \times 50 + 50 \times 151 = 5050 + 7550 = 12600$.

So the sum doesn't directly give us a contradiction. We need a better argument.

Let me think about a different lower bound approach.

Alternative approach: Consider the 401 positions. For each position $i$, let $x_i = 1$ if girl, 0 if boy. $\sum x_i = 201$.

$f(i) = \sum_{j: |j-i| \leq 50} x_j$ (sum over 101 positions). $\sum f(i) = 101 \times 201 = 20301$.

Girl $i$ is good iff $f(i) \geq 51$.

Now, consider the "excess" $e(i) = f(i) - 50$. $\sum e(i) = 20301 - 50 \times 401 = 251$.

Girl $i$ is good iff $e(i) \geq 1$.

We want to minimize the number of girls with $e(i) \geq 1$.

Now, $e(i) = f(i) - 50 = \sum_{|j-i| \leq 50} x_j - 50$. 

Hmm, let me think about the positions where $e(i) \geq 1$ (i.e., $f(i) \geq 51$). These form some arcs on the circle. Within each arc, $f(i) \geq 51$, and outside, $f(i) \leq 50$.

The total excess is 251. If the good positions (where $f \geq 51$) have $f$ values summing to $S$, and the non-good positions have $f$ values summing to $20301 - S$, then:

$S \geq 51 \times |\text{good positions}|$ and $20301 - S \leq 50 \times (401 - |\text{good positions}|)$.

From the second: $20301 - S \leq 50 \times 401 - 50 \times |\text{good}| = 20050 - 50 |\text{good}|$. So $S \geq 20301 - 20050 + 50 |\text{good}| = 251 + 50 |\text{good}|$.

From the first: $S \geq 51 |\text{good}|$.

So $S \geq \max(51 |\text{good}|, 251 + 50 |\text{good}|)$. The second bound is stronger when $251 + 50 |\text{good}| > 51 |\text{good}|$, i.e., $251 > |\text{good}|$, i.e., $|\text{good}| < 251$. Since $|\text{good}| \leq 401$, this is usually the case.

So $|\text{good positions}| \geq 251$ (from $S \leq 101 |\text{good}|$ and $S \geq 251 + 50 |\text{good}|$: $101 |\text{good}| \geq 251 + 50 |\text{good}|$, so $51 |\text{good}| \geq 251$, $|\text{good}| \geq 251/51 \approx 4.92$, so $|\text{good}| \geq 5$).

Wait, that gives $|\text{good positions}| \geq 5$, which is weak. We need $|\text{good girls}| \geq 51$, not $|\text{good positions}| \geq 5$.

The issue is that good positions can be boys. We need to relate good positions to good girls.

Hmm. Let me think about this differently.

Let me consider the following: in the block construction, the good positions (where $f \geq 51$) include the 51 girls in the large block AND some boys near the boundaries. Let me count.

In the block construction (boy blocks of 50, girl blocks of 50, 50, 50, 51):

For the girl block of 51 (positions 251-301), the $f$ values:
- Position 251 (girl): $f = 51$. Good.
- Position 252 (girl): $f = 52$. Good.
- ...
- Position 276 (girl, center): $f = 51$. Good.
- ...
- Position 301 (girl): $f = 51$. Good.

Actually, let me recompute. For the girl block of 51 surrounded by boy blocks of 50:
- Position 251 (first girl): window 201-301. Boys 201-250 (50), girls 251-301 (51). $f = 51$.
- Position 252: window 202-302. Boys 202-250 (49), girls 251-301 (51), boy 302 (1). $f = 51$.
- Position 276 (center): window 226-326. Boys 226-250 (25), girls 251-301 (51), boys 302-326 (25). $f = 51$.
- Position 301 (last girl): window 251-351. Girls 251-301 (51), boys 302-351 (50). $f = 51$.

So all 51 girls have $f = 51$. Now the boys near the boundary:
- Position 250 (boy, just before girl block): window 200-300. Boys 200-250 (51), girls 251-300 (50). $f = 50$. Not good.
- Position 249 (boy): window 199-299. Boys 199-250 (52), girls 251-299 (49). $f = 49$. Not good.

So the boys adjacent to the large girl block are NOT good. Let me check the other side.
- Position 302 (boy, just after girl block): window 252-352. Girls 252-301 (50), boys 302-352 (51). $f = 50$. Not good.

So the only good positions are the 51 girls in the large block. $|\text{good positions}| = 51 = G$.

Now, for the girl blocks of 50: all girls have $f = 50$, not good. And the boys near them also have $f \leq 50$.

So in this construction, $|\text{good positions}| = 51$ and $G = 51$.

Now I need to prove $G \geq 51$ in general. Let me think about a proof.

Approach: Consider the 201 girls. I want to show at least 51 have $f(i) \geq 51$.

Let me think about the "girl-only" subsequence. Consider the girls $g_1, \ldots, g_{201}$ in circular order, with gaps $d_1, \ldots, d_{201}$ (sum = 401).

For each girl $g_j$, $f(g_j) = 1 + r_j + l_j$ where $r_j$ = number of girls to the right within distance 50, $l_j$ = number to the left within distance 50.

$r_j$ = max $m$ such that $d_j + d_{j+1} + \cdots + d_{j+m-1} \leq 50$.

Good iff $r_j + l_j \geq 50$.

Now, note that $r_j + l_j$ = number of girls (other than $g_j$) within distance 50. And $r_j$ girls to the right means the $(r_j + 1)$-th girl to the right is at distance $> 50$.

Key insight: $r_j + l_j + 1 = f(g_j)$, and $f(g_j) \geq 51$ iff $r_j + l_j \geq 50$.

Let me think about the relationship between $r_j$ and $l_j$ and the gaps.

Consider the "right reach" $R_j = d_j + d_{j+1} + \cdots + d_{j+r_j-1}$ (sum of $r_j$ gaps, which is the distance to the $r_j$-th girl to the right). We have $R_j \leq 50$ and $R_j + d_{j+r_j} > 50$ (the next girl is too far).

Similarly, $L_j = d_{j-1} + d_{j-2} + \cdots + d_{j-l_j}$ (distance to the $l_j$-th girl to the left). $L_j \leq 50$ and $L_j + d_{j-l_j-1} > 50$.

Now, $r_j + l_j \geq 50$ iff good. 

Let me think about a counting argument. Consider the sum $\sum_j (r_j + l_j) = 2 \sum_j r_j$ (by symmetry of the circle).

$\sum_j r_j$ = number of ordered pairs $(g_j, g_l)$ with $g_l$ to the right of $g_j$ at distance $\leq 50$.

For each pair of girls at distance $d \leq 50$, it contributes 1 to $\sum r_j$ (the left girl counts the right girl) and 1 to $\sum l_j$ (the right girl counts the left girl). So $\sum r_j = \sum l_j = $ number of unordered close pairs.

$\sum (r_j + l_j) = 2 \times $ (number of unordered close pairs).

In the block construction: close pairs = pairs within the same girl block (since different blocks are separated by 50 boys, distance > 50). 

Block of 50: $\binom{50}{2} = 1225$ close pairs. Three such blocks: $3 \times 1225 = 3675$.
Block of 51: $\binom{51}{2} = 1275$ close pairs.
Total: $3675 + 1275 = 4950$.

$\sum (r_j + l_j) = 2 \times 4950 = 9900$. And $\sum f(g_j) = 201 + 9900 = 10101$. ✓ (matches earlier).

Now, for the lower bound on $G$: we have 201 girls, $G$ good (with $r_j + l_j \geq 50$, i.e., $f \geq 51$) and $201 - G$ not good (with $r_j + l_j \leq 49$, i.e., $f \leq 50$).

$\sum (r_j + l_j) \geq 50 G + 0 \cdot (201 - G) = 50G$ (since non-good girls have $r_j + l_j \geq 0$).

Also $\sum (r_j + l_j) \leq 100 G + 49(201 - G) = 51G + 9849$.

So $G \leq (\sum (r_j + l_j) - 9849) / 51$ and $G \geq \sum (r_j + l_j) / 100$... no, $G \geq \sum (r_j + l_j) / 100$ only if all good girls have $r_j + l_j \leq 100$, which is true. But this gives $G \geq 9900/100 = 99$ in the block construction, which contradicts $G = 51$. So this bound is wrong.

Wait, I think I messed up. $\sum (r_j + l_j) \leq 100 \cdot G + 49 \cdot (201 - G)$ is an UPPER bound on the sum, not a lower bound on $G$. Let me redo.

We have:
- $G$ good girls with $r_j + l_j \geq 50$ (and $\leq 100$).
- $201 - G$ non-good girls with $r_j + l_j \leq 49$ (and $\geq 0$).

Lower bound on sum: $\sum (r_j + l_j) \geq 50G + 0 = 50G$.
Upper bound on sum: $\sum (r_j + l_j) \leq 100G + 49(201-G) = 51G + 9849$.

So $G \geq \sum (r_j + l_j) / 100$... no. From the lower bound: $50G \leq \sum (r_j + l_j)$, so $G \leq \sum / 50$. From the upper bound: $\sum \leq 51G + 9849$, so $G \geq (\sum - 9849)/51$.

In the block construction, $\sum = 9900$, so $G \geq (9900 - 9849)/51 = 51/51 = 1$. That's very weak.

The problem is that the sum $\sum (r_j + l_j)$ can vary a lot depending on the arrangement. To get a strong lower bound on $G$, I need either a lower bound on $\sum (r_j + l_j)$ that's high enough, or a different approach.

Let me think about the minimum of $\sum (r_j + l_j) = 2 \times $ (close pairs).

What's the minimum number of close pairs (pairs of girls at distance $\leq 50$)?

We have 201 girls on a circle of 401. We want to minimize the number of pairs at distance $\leq 50$.

This is an optimization problem. To minimize close pairs, we want to spread girls out. But with 201 girls in 401 positions, the density is about 1/2, so many pairs will be close.

In the block construction, close pairs = 4950. Can we do better (fewer close pairs)?

If we spread girls evenly (gap ~2), each girl has about 50 close neighbors (25 on each side), so close pairs $\approx 201 \times 50 / 2 = 5025$. That's more than 4950!

So the block construction actually has fewer close pairs than the even arrangement. Interesting.

Can we do even better? What if we have larger boy blocks?

With 2 boy blocks of 100 and 2 girl blocks of 100 and 101:
Close pairs within block of 100: $\binom{100}{2} = 4950$. But wait, in a block of 100, two girls at the opposite ends are at distance 99 > 50. So not all pairs within a block are close.

Hmm, I need to be more careful. In a block of 100 consecutive girls, the distance between the first and last is 99. So pairs at distance $\leq 50$ within the block: for a girl at position $d$ in the block (0-indexed, $d = 0, \ldots, 99$), the girls within distance 50 are those at positions $d-50, \ldots, d+50$ (within the block). The count is $\min(d, 50) + \min(99-d, 50) + 1$ (including herself, but for pairs we exclude her).

Actually, the number of close pairs in a block of $L$ consecutive girls (with boy blocks of $\geq 50$ on both sides, so no close pairs between blocks):

For a girl at position $d$ ($0 \leq d \leq L-1$) in the block, the number of girls within distance 50 (excluding herself) is:
- To the right: $\min(L - 1 - d, 50)$.
- To the left: $\min(d, 50)$.
- Total: $\min(d, 50) + \min(L - 1 - d, 50)$.

Sum over all girls in the block: $\sum_{d=0}^{L-1} [\min(d, 50) + \min(L-1-d, 50)]$.

By symmetry, this is $2 \sum_{d=0}^{L-1} \min(d, 50)$... no, it's $\sum_{d=0}^{L-1} \min(d, 50) + \sum_{d=0}^{L-1} \min(L-1-d, 50) = 2 \sum_{d=0}^{L-1} \min(d, 50)$ (by substituting $d \to L-1-d$ in the second sum).

$\sum_{d=0}^{L-1} \min(d, 50) = \sum_{d=0}^{50} d + \sum_{d=51}^{L-1} 50 = \frac{50 \cdot 51}{2} + 50(L - 51) = 1275 + 50L - 2550 = 50L - 1275$ (for $L \geq 51$).

For $L \leq 51$: $\sum_{d=0}^{L-1} \min(d, 50) = \sum_{d=0}^{L-1} d = \frac{(L-1)L}{2}$.

So the number of close pairs in a block of $L$ (with $L \leq 51$) is $2 \cdot \frac{(L-1)L}{2} / 2$... wait, I need to be careful. The sum $\sum_{d=0}^{L-1} [\min(d,50) + \min(L-1-d,50)]$ counts, for each girl, the number of close girls. The total number of close pairs is this sum divided by 2 (each pair counted twice).

For $L \leq 51$: sum $= 2 \sum_{d=0}^{L-1} d = 2 \cdot \frac{(L-1)L}{2} = L(L-1)$. Close pairs $= L(L-1)/2 = \binom{L}{2}$. Makes sense—all pairs are close.

For $L \geq 52$: sum $= 2(50L - 1275) = 100L - 2550$. Close pairs $= (100L - 2550)/2 = 50L - 1275$.

Now, total close pairs for the block construction with blocks $b_1, \ldots, b_r$ (each $\leq 51$, with boy blocks $\geq 50$):

Close pairs $= \sum_{i: b_i \leq 51} \binom{b_i}{2} + \sum_{i: b_i \geq 52} (50 b_i - 1275)$.

For the construction with blocks 50, 50, 50, 51:
Close pairs $= 3 \binom{50}{2} + \binom{51}{2} = 3 \times 1225 + 1275 = 3675 + 1275 = 4950$. ✓

For blocks 100, 101 (with boy blocks of 100):
Close pairs $= (50 \times 100 - 1275) + (50 \times 101 - 1275) = 3725 + 3775 = 7500$. Much more!

For blocks 50, 50, 50, 51 (boy blocks 50): 4950.
For blocks 40, 40, 40, 40, 41 (boy blocks 40): but boy blocks < 50, so cross-block pairs exist. Need to account for those.

Hmm, with boy blocks < 50, there are cross-block close pairs, which increases the total. So the block construction with boy blocks $\geq 50$ is better for minimizing close pairs.

Among constructions with boy blocks $\geq 50$: we need $\sum b_i = 201$ and $\sum a_i = 200$ with $a_i \geq 50$, so $r \leq 4$.

With $r = 4$: $a_i = 50$ each, $b_i$ summing to 201. Close pairs $= \sum \binom{b_i}{2}$ (if all $b_i \leq 51$) or with the larger formula.

To minimize $\sum \binom{b_i}{2}$ with $\sum b_i = 201$ and $b_i \leq 51$ (to avoid the larger formula, but actually even with $b_i > 51$ the formula $50b_i - 1275$ vs $\binom{b_i}{2}$... for $b_i = 51$: $\binom{51}{2} = 1275$ and $50 \times 51 - 1275 = 1275$. Same. For $b_i = 52$: $\binom{52}{2} = 1326$ vs $50 \times 52 - 1275 = 1325$. So the formula gives slightly less. But $b_i = 52$ means all 52 girls are good, which is bad for $G$.)

Anyway, to minimize close pairs with $r = 4$ and $\sum b_i = 201$: by convexity, we want the $b_i$ as equal as possible. $201 / 4 = 50.25$, so blocks of 50, 50, 50, 51. Close pairs $= 3 \times 1225 + 1275 = 4950$.

With $r = 3$: $a_i$ summing to 200, each $\geq 50$. $b_i$ summing to 201. To minimize close pairs, equal blocks: 67, 67, 67. Close pairs $= 3 \times (50 \times 67 - 1275) = 3 \times 2075 = 6225$. More than 4950.

With $r = 2$: $b_i$ = 100, 101. Close pairs $= 7500$. More.

So the minimum close pairs with block structure is 4950, achieved by $r = 4$, blocks 50, 50, 50, 51.

But could a non-block arrangement have fewer close pairs? Let me think...

Actually, the minimum number of close pairs over ALL arrangements (not just block arrangements) might be even lower. But I suspect the block arrangement is optimal or near-optimal.

Hmm, but I don't need to minimize close pairs. I need to minimize $G$. Let me think about whether $G = 51$ is truly optimal.

Let me try to construct an arrangement with $G < 51$.

Idea: What if we don't use a pure block structure? For instance, what if we have 4 boy blocks of 50, but the girl blocks are not all consecutive? Well, in a circle with alternating boy and girl blocks, the girl blocks are determined.

What if we have 5 boy blocks, some smaller than 50? Let's try 5 boy blocks of 40 each (total 200) and 5 girl blocks summing to 201.

As computed earlier, with boy blocks of 40, a girl block of size $b$ has some good girls. Let me compute for $b = 40$:

For a girl at distance $d$ from the left edge of a block of 40, with boy blocks of 40 on both sides:

If $d \geq 10$ and $d \leq 29$ (i.e., $b - 1 - d = 39 - d \geq 10$): $g_i = b - 1 = 39 < 50$. Not good.

If $d < 10$: $g_i = b + 9 - d = 49 - d$. For $d = 0$: $g_i = 49 < 50$. Not good! For $d = 9$: $g_i = 40$... wait, $49 - 9 = 40 < 50$. Not good.

Hmm wait, let me recompute. With boy blocks of 40:

For $d < 10$ and $d \leq b - 11 = 29$: $g_i = b + 9 - d = 49 - d$. For $d = 0$: $g_i = 49$. Not good!

For $d < 10$ and $d > b - 11$ (i.e., $b < 10 + d < 20$): $g_i = 20$. Not good.

For $d \geq 10$ and $d \leq b - 11 = 29$: $g_i = b - 1 = 39$. Not good.

For $d > b - 11 = 29$ and $d \geq 10$: $g_i = d + 10$. For $d = 30$: $g_i = 40$. Not good. For $d = 39$: $g_i = 49$. Not good.

So for $b = 40$ with boy blocks of 40: ALL girls have $g_i \leq 49 < 50$. None are good!

Wait, that's great! Let me double-check.

Girl at $d = 0$ (left edge): left neighbors = 40 boys + 10 girls from previous block. Right neighbors = 39 girls + 11 boys (from right boy block of 40, we get 40 boys but only need 11). Wait, right neighbors: 39 girls (positions $d+1$ to $d+39$, i.e., $b-1 = 39$ girls) + 40 boys + ... but 39 + 40 = 79 > 50, so only 39 girls + 11 boys = 50. $g_{\text{right}} = 39$. $g_i = 10 + 39 = 49$. Not good. ✓

Girl at $d = 39$ (right edge): left neighbors = 39 girls + 11 boys. $g_{\text{left}} = 39$. Right neighbors = 40 boys + 10 girls from next block. $g_{\text{right}} = 10$. $g_i = 39 + 10 = 49$. Not good. ✓

Girl at $d = 20$ (middle): left = 20 girls + 30 boys. $g_{\text{left}} = 20$. Right = 19 girls + 31 boys. $g_{\text{right}} = 19$. $g_i = 39$. Not good. ✓

So with 5 boy blocks of 40 and 5 girl blocks of 40 each (total girls = 200), all girls have $g_i \leq 49$. But we need 201 girls, not 200!

So we need one extra girl. We can make one girl block of size 41 instead of 40.

For $b = 41$ with boy blocks of 40:

Girl at $d = 0$: $g_i = b + 9 - d = 50$. Good! (Since $d = 0 \leq b - 11 = 30$.)

Wait, $g_i = 49 + 1 - 0 = 50$? Let me recompute. $g_i = b + 9 - d = 41 + 9 - 0 = 50$. Yes, $g_i = 50 \geq 50$. Good!

Girl at $d = 1$: $g_i = 41 + 9 - 1 = 49$. Not good.

Girl at $d = 30$: $g_i = 41 + 9 - 30 = 20$. Not good. (And $d = 30 \leq b - 11 = 30$, so first subcase.)

Girl at $d = 31$: $d > b - 11 = 30$ and $d \geq 10$. $g_i = d + 10 = 41$. Not good.

Girl at $d = 40$ (right edge): $g_i = 40 + 10 = 50$. Good!

So for $b = 41$: good girls at $d = 0$ and $d = 40$. That's 2 good girls.

So with 5 boy blocks of 40 and girl blocks 40, 40, 40, 40, 41: $G = 2$.

Wait, that's way better than 51! Let me verify this more carefully.

Hmm, wait. I need to check whether the "previous girl block has enough girls" assumption holds. When I said "10 girls from previous block," I assumed the previous girl block has $\geq 10$ girls. With blocks of 40, yes, each has 40 $\geq$ 10.

But also, I need to check: when a girl at $d = 0$ in a block of 40 looks left, she sees 40 boys (from the boy block) and then 10 girls from the previous girl block. But the previous girl block is of size 40 (or 41), so it has $\geq 10$ girls. ✓

And when she looks right, she sees 39 girls from her own block, then 11 boys from the right boy block (which has 40 boys, so $\geq 11$). ✓

So the computation is correct. Let me also check the cross-block interactions more carefully.

Circle: B40, G40, B40, G40, B40, G40, B40, G40, B40, G41.

Let me label positions. Total = 5×40 + 4×40 + 41 = 200 + 160 + 41 = 401. ✓

Boy blocks: positions 1-40, 81-120, 161-200, 241-280, 321-360.
Girl blocks: positions 41-80, 121-160, 201-240, 281-320, 361-401.

Girl block 5 (positions 361-401, size 41):
- Position 361 (d=0): left neighbors = positions 311-360. Positions 311-320: girls (10), positions 321-360: boys (40). $g_{\text{left}} = 10$. Right neighbors = positions 362-401. All girls (40). $g_{\text{right}} = 40$. $g_i = 10 + 40 = 50$. Good. ✓

- Position 401 (d=40): left neighbors = positions 351-400. Positions 351-360: boys (10), positions 361-400: girls (40). $g_{\text{left}} = 40$. Right neighbors = positions 1-40 (wrapping around). Wait, position 401 + 1 = 402 → 1 (mod 401). So right neighbors = positions 1-50. Positions 1-40: boys (40), positions 41-50: girls (10). $g_{\text{right}} = 10$. $g_i = 40 + 10 = 50$. Good. ✓

- Position 381 (d=20, middle): left = 371-390. Wait, left neighbors of 381 are 381-50=331 to 380. Positions 331-360: boys (30), positions 361-380: girls (20). $g_{\text{left}} = 20$. Right = 382-401. Girls (20). $g_{\text{right}} = 20$. $g_i = 40$. Not good. ✓

Girl block 1 (positions 41-80, size 40):
- Position 41 (d=0): left = 1-40. Boys (40). $g_{\text{left}} = 0$. Right = 42-80. Girls (39), then position 81-91: boys (11). Wait, right neighbors are 42 to 91 (50 positions). 42-80: girls (39), 81-91: boys (11). $g_{\text{right}} = 39$. $g_i = 0 + 39 = 39$. Not good.

Hmm wait, that doesn't match my formula. My formula said $g_i = b + 9 - d = 40 + 9 - 0 = 49$ for $d = 0$. But I'm getting 39. Let me recheck.

Oh, I think the issue is that the previous girl block (block 5, positions 361-401) is not adjacent to block 1 on the left. The left of block 1 is boy block 5 (positions 321-360), and before that is girl block 4 (positions 281-320).

Wait, the circle is: B1(1-40), G1(41-80), B2(81-120), G2(121-160), B3(161-200), G3(201-240), B4(241-280), G4(281-320), B5(321-360), G5(361-401).

So the left neighbor of G1 is B1 (positions 1-40), and the left of B1 is G5 (positions 361-401).

For position 41 (d=0 in G1): left neighbors = positions -9 to 40 = positions 393-401, 1-40. Positions 393-401: girls (9, from G5), positions 1-40: boys (40). Wait, 41 - 50 = -9, which mod 401 is 392. So left neighbors are positions 392 to 40 (going left from 41): 392, 393, ..., 401, 1, 2, ..., 40. That's 50 positions.

Positions 392-401: 10 positions. G5 is 361-401, so 392-401 are all girls (10 girls). Positions 1-40: boys (40). $g_{\text{left}} = 10$.

Right neighbors: 42-91. Positions 42-80: girls (39), positions 81-91: boys (11). $g_{\text{right}} = 39$.

$g_i = 10 + 39 = 49$. Not good. ✓ This matches the formula now!

I made an error before. The left neighbors wrap around through G5, not just B1. Let me recheck position 41.

Position 41's 50 left neighbors: positions 41-50=−9 ≡ 392 (mod 401) up to position 40. So positions 392, 393, ..., 401, 1, 2, ..., 40. That's 10 + 40 = 50 positions. Positions 392-401 are in G5 (361-401), so 10 girls. Positions 1-40 are in B1, so 40 boys. $g_{\text{left}} = 10$. ✓

So $g_i = 10 + 39 = 49$. Not good. ✓

Great, so the formula is correct. Let me recheck the G5 block (size 41).

Position 361 (d=0 in G5): left neighbors = 311-360. Positions 311-320: G4 (281-320), so 10 girls. Positions 321-360: B5, so 40 boys. $g_{\text{left}} = 10$. Right neighbors = 362-411 = 362-401, 1-10. Positions 362-401: G5, 40 girls. Positions 1-10: B1, 10 boys. $g_{\text{right}} = 40$. $g_i = 10 + 40 = 50$. Good. ✓

Position 401 (d=40 in G5): left = 351-400. Positions 351-360: B5, 10 boys. Positions 361-400: G5, 40 girls. $g_{\text{left}} = 40$. Right = 1-50. Positions 1-40: B1, 40 boys. Positions 41-50: G1, 10 girls. $g_{\text{right}} = 10$. $g_i = 40 + 10 = 50$. Good. ✓

So $G = 2$ (only positions 361 and 401 are good). That's much better than 51!

Can we do even better? Let me try 5 girl blocks of 40, 40, 40, 41, 40 and see if we can reduce to $G = 2$ or even $G = 0$.

Wait, we need $\sum b_i = 201$ with 5 blocks. $5 \times 40 = 200$, so one block must be 41. With the 41-block, we get 2 good girls (at the two edges). So $G = 2$.

Can we use more blocks? 6 boy blocks of size $200/6 \approx 33.3$, say 34, 33, 33, 33, 33, 34 (sum 200). 6 girl blocks summing to 201, say 34, 33, 34, 33, 34, 33 (sum 201). With boy blocks of ~33 < 40, the "leak" from neighboring girl blocks is larger.

For a girl at $d = 0$ in a block of size $b$ with boy blocks of size $a$ on both sides:
- Left: $a$ boys + $(50 - a)$ girls from previous block (if previous block has $\geq 50 - a$ girls).
- Right: $(b - 1)$ girls + $(50 - (b-1))$ boys from right boy block (if $b - 1 \leq 50$ and right boy block $\geq 50 - (b-1)$). If $50 - (b-1) > a$, then we also get girls from the next-next block.

With $a = 33, b = 34$:
- Left: 33 boys + 17 girls from previous block. $g_{\text{left}} = 17$.
- Right: 33 girls + 17 boys (from right boy block of 33, but we need 17, and 33 ≥ 17). $g_{\text{right}} = 33$.
- $g_i = 17 + 33 = 50$. Good!

Hmm, so with $a = 33, b = 34$: edge girls have $g_i = 50$, which is good. That's not better.

Let me try $a = 34, b = 33$:
- Left: 34 boys + 16 girls. $g_{\text{left}} = 16$.
- Right: 32 girls + 18 boys. $g_{\text{right}} = 32$.
- $g_i = 16 + 32 = 48$. Not good.

And for a girl at $d = 16$ (middle-ish):
- Left: 16 girls + 34 boys. $g_{\text{left}} = 16$.
- Right: 16 girls + 34 boys. $g_{\text{right}} = 16$.
- $g_i = 32$. Not good.

For $d = 0$: $g_i = 16 + 32 = 48$. Not good.
For $d = 32$ (right edge): $g_{\text{left}} = 32$, $g_{\text{right}} = 16$. $g_i = 48$. Not good.

So with $a = 34, b = 33$: all girls have $g_i \leq 48$. Not good.

But we need $\sum b_i = 201$ with 6 blocks. If all $b_i = 33$: $6 \times 33 = 198 < 201$. Need 3 more. So blocks like 34, 33, 34, 33, 34, 33 (sum 201).

For $b = 34$ with $a = 34$: edge girl has $g_i = 16 + 33 = 49$. Not good!

Wait, let me recompute. $a = 34, b = 34$:
- $d = 0$: left = 34 boys + 16 girls. $g_{\text{left}} = 16$. Right = 33 girls + 17 boys. $g_{\text{right}} = 33$. $g_i = 49$. Not good!
- $d = 33$ (right edge): left = 33 girls + 17 boys. $g_{\text{left}} = 33$. Right = 34 boys + 16 girls. $g_{\text{right}} = 16$. $g_i = 49$. Not good.
- $d = 17$ (middle): left = 17 girls + 33 boys. $g_{\text{left}} = 17$. Right = 16 girls + 34 boys. $g_{\text{right}} = 16$. $g_i = 33$. Not good.

So with $a = 34, b = 34$: all girls have $g_i \leq 49$. Not good!

So if we use 6 boy blocks of 34, 33, 33
