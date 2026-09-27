# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Annie has 24 letter tiles in a bag; 8 C’s, 8 M’s, and 8 W’s. She blindly draws tiles from the bag until she has enough to spell “CMWMC.” What is the maximum number of tiles she may have to draw?       — 题目文本
#   <think>Okay, let's try to figure out this problem. The question is about Annie drawing letter tiles from a bag with 8 C's, 8 M's, and 8 W's. She needs to spell "CMWMC", and we need to find the maximum number of tiles she might have to draw to get enough to spell that word. 

First, let's figure out what letters are needed for "CMWMC". Let's spell it out: C, M, W, M, C. So that's 2 C's, 2 M's, and 1 W. So the required counts are: C:2, M:2, W:1. 

Now, the problem is asking for the maximum number of tiles she might have to draw. To maximize the number of draws, we need to consider the worst-case scenario where she draws as many tiles as possible without getting the required number of each letter, and then the next tile will give her the last one needed. 

Let's break it down by each letter. Let's think about the letters she might draw before getting the necessary ones. 

First, let's list the required letters and their counts:
- C needed: 2
- M needed: 2
- W needed: 1

To maximize the number of draws, we want to consider the scenario where she draws as many of the other letters as possible, but also not getting enough of the required ones until the last possible moment.

Wait, but all the letters are C, M, W. So there are no other letters. So the worst case is that she draws as many tiles as possible without having the required number of each needed letter, and then the next tile gives her the last one needed.

Let's think about each required letter and how many of the others she might have drawn.

First, let's see what's the maximum number of tiles she can have without having enough C's, M's, or W's. Wait, but she needs all three. So she needs at least 2 C's, 2 M's, and 1 W. So the worst case is that she has almost enough of some, but not all, and then the last tile gives the missing one.

Wait, maybe we need to consider the maximum number of tiles she could have drawn without having the exact counts needed, but then the next tile would make it possible. Let's think step by step.

Let's first note the required counts:

Total required: 2 C, 2 M, 1 W. Total letters needed: 5.

But the question is about the maximum number of tiles she may have to draw. So we need to imagine the worst possible sequence of draws where she has to draw as many as possible before getting the necessary tiles.

To maximize the number of draws, we need to consider the scenario where she draws as many tiles as possible that are not contributing to the required counts, but also not getting the required counts. Wait, but all tiles are C, M, W. So maybe she's drawing a lot of the letters that are needed but not enough, and also maybe some of the others.

Wait, let's think: What's the maximum number of tiles she can have without having 2 C's, 2 M's, and 1 W? Then the next tile would give her the last one needed.

But actually, she needs all three. So she needs to have at least 2 C's, at least 2 M's, and at least 1 W. So the worst case is that she has as many tiles as possible, but missing one of these conditions, and then the next tile gives her the missing one.

But maybe she's missing more than one condition. Let's see.

Let's consider the possible "deficiencies":

1. Not enough C's (i.e., less than 2 C's)
2. Not enough M's (i.e., less than 2 M's)
3. Not enough W's (i.e., less than 1 W)

We need to find the maximum number of tiles where at least one of these deficiencies exists, and then the next tile will resolve all deficiencies.

But to maximize the total, we need to maximize the number of tiles drawn while still having at least one deficiency, and then the next tile fixes it.

But perhaps the worst case is when she has the maximum number of tiles where she is missing the least critical deficiency. Let's think.

First, let's see what's the maximum number of tiles she can have without having 2 C's. That would be if she has 1 C, and as many M's and W's as possible. But wait, but she might already have enough M's and W's. But if she's missing C's, then even if she has enough M's and W's, she still can't spell the word. So the maximum tiles without 2 C's: 1 C + all M's + all W's. But wait, there are 8 M's and 8 W's. So 1 + 8 + 8 = 17. But wait, but if she has 1 C, 8 M's, 8 W's, that's 17 tiles. But in this case, she has 8 M's (which is more than needed 2), 8 W's (more than needed 1), but only 1 C (needs 2). So she can't spell the word yet. Then the next tile must be a C, since all other tiles are already drawn (since there are 8 C's total, and she has 1, so 7 left). Wait, no. Wait, total tiles are 24. If she has 1 C, 8 M, 8 W, that's 17 tiles. There are 24 - 17 = 7 tiles left, which are all C's (since 8 total C's, 1 drawn, 7 left). So the next tile she draws is a C, making her total C's 2. Now she has 2 C's, 8 M's, 8 W's. Now she has enough: 2 C, 2 M, 1 W. So total tiles drawn: 17 + 1 = 18. But wait, but maybe there's a worse case.

Alternatively, what if she's missing M's? Let's see. Maximum tiles without 2 M's: 1 M, and as many C's and W's as possible. So 1 M + 8 C's + 8 W's = 1 + 8 + 8 = 17. Then next tile is M, making M's 2. Total tiles: 17 + 1 = 18. Same as before.

What if she's missing W's? Maximum tiles without 1 W: 0 W's, and as many C's and M's as possible. So 0 W + 8 C's + 8 M's = 16. Then next tile is W, total tiles: 16 + 1 = 17. That's less than 18, so not the maximum.

But wait, maybe there's a scenario where she's missing more than one deficiency. For example, she has less than 2 C's and less than 2 M's. Let's see. Let's say she has 1 C and 1 M. Then how many W's can she have? Let's see. To maximize the total, she would have as many W's as possible. But W's are 8. So 1 C + 1 M + 8 W = 10. Then she's missing 1 C, 1 M, but has enough W's. But this is way less than 17, so not the maximum.

Alternatively, maybe she's missing 2 C's and has enough M's and W's. Wait, but if she has enough M's and W's, but not enough C's, that's the first case. Similarly, if she has enough C's and W's but not enough M's, that's the second case.

But maybe there's a case where she has more than the required of some letters but not enough of others, but the total is higher. Let's think again.

Wait, the required is 2 C, 2 M, 1 W. Let's think about the worst case where she has the maximum number of tiles, but still doesn't have the required counts. Then the next tile will give her the last needed.

But to maximize the number of tiles, we need to consider the scenario where she has the maximum possible tiles without having all the required counts. Let's see:

What's the maximum number of tiles she can have without having 2 C's, OR without having 2 M's, OR without having 1 W. Because as long as any of these is missing, she can't spell the word. So the worst case is the maximum among the three possibilities:

1. Max tiles without 2 C's: 1 C + all M's + all W's = 1 + 8 + 8 = 17. At this point, she has 1 C, 8 M, 8 W. She needs 1 more C. The next tile must be a C (since all other tiles are already drawn: 8 M and 8 W are all drawn, so remaining tiles are 8 - 1 = 7 C's). So next tile is C, total 18.

2. Max tiles without 2 M's: 1 M + all C's + all W's = 1 + 8 + 8 = 17. Then next tile is M, total 18.

3. Max tiles without 1 W: 0 W + all C's + all M's = 0 + 8 + 8 = 16. Next tile is W, total 17.

But wait, but maybe there's a scenario where she has more than 17 tiles but still can't form the word. Let's check. Suppose she has 2 C's, but only 1 M, and 8 W's. Let's see: 2 C + 1 M + 8 W = 11. That's less than 17, so not worse.

Alternatively, 2 C's, 2 M's, but 0 W's. Then she has 2+2+0=4 tiles. Then she needs a W. But that's way less than 17.

Wait, but what if she has 2 C's, 1 M, and 8 W's. That's 2+1+8=11. Still less than 17.

Alternatively, 1 C, 2 M's, 8 W's. 1+2+8=11. Still less.

Alternatively, 1 C, 8 M's, 7 W's. Then total tiles: 1+8+7=16. But she has 1 C (needs 2), 8 M (enough), 7 W (enough). So she's missing 1 C. But this is 16 tiles, which is less than 17.

Wait, the maximum when missing C's is 1 C + 8 M + 8 W = 17. Because if she has 1 C, and all M's and W's, that's the maximum possible without having 2 C's. Because if she has more than 1 C, then she's not missing C's anymore. So 1 C is the max for missing C's.

Similarly, missing M's: 1 M + 8 C + 8 W = 17.

Missing W's: 0 W + 8 C + 8 M = 16.

But wait, what if she's missing both C's and M's? For example, 1 C, 1 M, 8 W. That's 10 tiles. But that's less than 17, so not the maximum.

Alternatively, 1 C, 1 M, 8 W: 10 tiles. But she's missing 1 C and 1 M. But the maximum tiles in this case is 1+1+8=10, which is less than 17. So the worst case is when she's missing only one of the required letters, and that's either C or M, leading to 17 tiles drawn, then the next tile (18th) gives the needed C or M.

But wait, let's confirm. Let's take the first case: she's drawing tiles, and the first 17 tiles are 1 C, 8 M's, 8 W's. Then she has 1 C, which is not enough (needs 2). The next tile must be a C (since all M's and W's are already drawn: 8 M's and 8 W's are all in the 17 tiles, so remaining tiles are 8 C's - 1 C = 7 C's). So the 18th tile is a C, making her total C's 2. Now she has 2 C's, 8 M's, 8 W's. Now she has all required: 2 C, 2 M, 1 W. So she can spell the word. So total tiles drawn: 18.

But wait, is there a scenario where she has to draw more than 18? Let's see.

Suppose she's missing M's. Let's say she has 8 C's, 1 M, 8 W's. That's 8+1+8=17 tiles. Then the next tile is a M (since all C's and W's are already drawn: 8 C's and 8 W's, so remaining tiles are 8 M's -1 M=7 M's). So 18th tile is M, now she has 8 C, 2 M, 8 W. Now she has 2 C (needs 2), 2 M (needs 2), 1 W (needs 1). So she can spell the word. Total tiles: 18.

What if she's missing W's? She has 8 C, 8 M, 0 W. That's 16 tiles. Next tile is W (since remaining tiles are 8 W's). 17th tile is W. Now she has 8 C, 8 M, 1 W. Now she has 2 C, 2 M, 1 W. So she can spell the word. Total tiles: 17. So that's less than 18.

Is there a scenario where she has to draw more than 18? Let's think.

Wait, maybe she's not just missing one letter, but has some of the required letters but not enough, but also has some excess. Wait, but the maximum number of tiles without having the required counts would be when she has the maximum possible tiles but still missing at least one required count.

Wait, let's think differently. Let's consider the worst case where she draws as many tiles as possible that are not contributing to the required counts, but also not getting enough of the required ones. But since all tiles are required letters, maybe the worst case is when she has the maximum number of tiles that don't include enough of the least required letters.

Wait, the required letters are 2 C, 2 M, 1 W. The W is needed only once, but there are 8 W's. So maybe the worst case is when she draws a lot of W's, but not enough C's or M's.

Wait, but earlier calculation shows that the maximum when missing C's is 17, which includes 8 W's. So that's already considered.

Alternatively, what if she has 2 C's, but only 1 M, and 8 W's. Let's see: 2 C + 1 M + 8 W = 11. Then she's missing 1 M. But she has 11 tiles. The remaining tiles are 8 M's -1 M =7 M's, and 8 W's -8 W's=0 W's, 8 C's -2 C's=6 C's. So next tile could be M, C, or M. Wait, but she needs 1 more M. But the total tiles here is 11, which is way less than 17, so not the maximum.

Alternatively, what if she has 2 C's, 2 M's, but 0 W's. Then she has 4 tiles. She needs 1 W. The remaining tiles are 8 W's, 6 C's, 6 M's. Next tile is W, total 5. But that's way less than 18.

Alternatively, what if she has 3 C's, 1 M, 8 W's. That's 3+1+8=12. She's missing 1 M. But again, total tiles 12 <17.

Alternatively, 1 C, 3 M, 8 W's. 1+3+8=12. Missing 1 C. Still less than 17.

So the maximum seems to be 18. But let's confirm.

Wait, let's think about the total number of tiles. There are 24 tiles. Let's see, what's the minimum number of tiles needed to guarantee that she has the required letters. But the question is the maximum number she may have to draw, which is the worst-case scenario, i.e., the maximum possible number of tiles she could draw before getting the necessary ones.

Wait, another approach: To spell "CMWMC", she needs 2 C, 2 M, 1 W. Let's think about the worst case where she draws as many tiles as possible without having the required counts, then the next tile gives her the last one needed.

The worst case is when she has the maximum number of tiles that do not contain the required number of each letter. Let's calculate the maximum number of tiles that do not have enough C's, or not enough M's, or not enough W's.

But to maximize, we need the maximum of the three possibilities:

1. Tiles with <2 C's: maximum possible is (1 C) + all M's + all W's = 1 +8+8=17. Because if she has 1 C, and all 8 M's and 8 W's, that's 17 tiles, and she still needs 1 more C.

2. Tiles with <2 M's: maximum possible is (1 M) + all C's + all W's =1+8+8=17. Needs 1 more M.

3. Tiles with <1 W's: maximum possible is (0 W) + all C's + all M's=0+8+8=16. Needs 1 W.

So the maximum among these is 17. Then the next tile (18th) will give her the needed C or M, making the total 18.

Is there a scenario where she has more than 17 tiles but still can't form the word? Let's see. Suppose she has 2 C's, 1 M, and 8 W's. That's 2+1+8=11. But that's less than 17. What if she has 2 C's, 2 M's, and 7 W's. That's 2+2+7=11. Still less.

Alternatively, 3 C's, 1 M, 8 W's: 3+1+8=12. Still less than 17.

Alternatively, 1 C, 2 M's, 8 W's: 1+2+8=11. Still less.

Alternatively, 1 C, 8 M's, 7 W's: 1+8+7=16. That's less than 17. Because she has 1 C (needs 2), 8 M (enough), 7 W (enough). But she's missing 1 C, but the total tiles here is 16, which is less than 17. So the maximum when missing C's is indeed 17 (1 C, 8 M, 8 W).

Similarly, 8 C's, 1 M, 8 W's: 8+1+8=17. Missing 1 M.

So in both cases, the maximum tiles without having the required counts is 17. Then the next tile (18th) will be the needed one (C or M), making the total 18.

Is there a case where she has 17 tiles but still can't form the word, but the 18th tile isn't the needed one? No, because in the scenario where she has 1 C, 8 M, 8 W (17 tiles), the remaining tiles are all C's (since 8 C's total, 1 drawn, 7 left). So the next tile must be a C, which gives her 2 C's, making the total 18. Similarly, if she has 8 C, 1 M, 8 W (17 tiles), remaining tiles are M's, so next tile is M, total 18.

Wait, but what if she's in a scenario where she has some of the required letters but not enough, but also has some of the others. For example, suppose she has 1 C, 7 M's, 8 W's. That's 1+7+8=16 tiles. She's missing 1 C and 1 M. But this is less than 17, so not the maximum.

Alternatively, 1 C, 8 M's, 7 W's: 1+8+7=16. Still missing 1 C, but total tiles 16 <17.

So the maximum number of tiles she might have to draw is 18. Let's confirm with another angle.

Total required letters: 2 C, 2 M, 1 W. Let's think of the worst case where she draws all the letters that are not needed in excess, but not enough of the needed ones.

Wait, but all letters are needed. So the worst case is when she has the maximum number of letters that don't include the required counts. As we calculated, that's 17, then the next one is needed. So 18.

Yes, that makes sense. So the answer is 18.
</think>

To determine the maximum number of tiles Annie may have to draw to spell "CMWMC", we first identify the required letters and their counts: 2 C's, 2 M's, and 1 W. 

To find the worst-case scenario, we consider the maximum number of tiles she could draw without having enough of each required letter, then add one more tile to ensure she has the necessary counts.

### Key Analysis:
1. **Required Letters**: 2 C's, 2 M's, 1 W.
2. **Worst-Case Scenarios**:
   - **Missing 2 C's**: If Annie has only 1 C, but all 8 M's and 8 W's, she has \(1 + 8 + 8 = 17\) tiles. She needs 1 more C.
   - **Missing 2 M's**: If Annie has only 1 M, but all 8 C's and 8 W's, she has \(1 + 8 + 8 = 17\) tiles. She needs 1 more M.
   - **Missing 1 W**: If Annie has no W's, but all 8 C's and 8 M's, she has \(0 + 8 + 8 = 16\) tiles. She needs 1 W.

The maximum number of tiles in the worst case (before getting the required letter) is 17. The next tile drawn will provide the missing letter (either a C or M), making the total number of tiles drawn \(17 + 1 = 18\).

Thus, the maximum number of tiles Annie may have to draw is \(\boxed{18}\).  — 标准解答
#   Let me analyze this problem carefully.

The problem asks about two related questions:

1. If $f(x)$ is measurable (Lebesgue), periodic with $f(x+1) = f(x)$, and $f(x) = \pm 1$, do we have almost everywhere $\limsup_{n \to \infty} f(nx) = +1$ and $\liminf_{n \to \infty} f(nx) = -1$?

2. More generally: If $f_n(x)$ are measurable, uniformly bounded, and $f_n(x + 1/n) \equiv f_n(x)$, do we have $\limsup_{n \to \infty} f_n(x) = \text{constant a.e.}$? And $\liminf_{n \to \infty} f_n(x) = \text{constant a.e.}$?

Let me think about this carefully.

**Part 1:** $f$ is measurable, 1-periodic, $f: \mathbb{R} \to \{-1, +1\}$. We want to know if $\limsup_{n\to\infty} f(nx) = +1$ a.e. and $\liminf_{n\to\infty} f(nx) = -1$ a.e.

First, let me think about what $f(nx)$ looks like. Since $f$ is 1-periodic, $f(nx) = f(\{nx\})$ where $\{nx\}$ is the fractional part.

The key question is about the distribution of $\{nx\}$ mod 1. For a.e. $x$, the sequence $\{nx\}$ is equidistributed mod 1 (by Weyl's theorem / the ergodic theorem applied to the map $T: x \mapsto x+1$ on the circle, but actually we need to think about this differently).

Wait, let me think again. We have the sequence $x, 2x, 3x, \ldots$ and we look at $f(nx) = f(\{nx\})$.

For a.e. $x$ (with respect to Lebesgue measure on, say, $[0,1]$), the sequence $\{nx\}_{n=1}^\infty$ is equidistributed mod 1. This is a classical result.

Actually, let me be more careful. The equidistribution of $\{nx\}$ mod 1 for a.e. $x$ is indeed a classical result. It follows from the ergodic theorem: consider the transformation $T: [0,1) \to [0,1)$, $T(x) = \{x + \alpha\}$... no wait, that's not quite right either.

Actually, the equidistribution of $\{nx\}$ for a.e. $x$ is a consequence of the pointwise ergodic theorem. Consider the map $T: \mathbb{T} \to \mathbb{T}$ given by $T(x) = x$ (identity)... no.

Let me think more carefully. We want to understand the behavior of $f(nx)$ as $n \to \infty$. 

Consider the sequence $g_n(x) = f(nx)$. Each $g_n$ is measurable and 1-periodic (since $f$ is 1-periodic: $g_n(x+1) = f(n(x+1)) = f(nx + n) = f(nx) = g_n(x)$, using $f$ 1-periodic and $n$ integer).

Now, for the equidistribution: For a.e. $x \in [0,1]$, the sequence $\{nx\}$ is equidistributed mod 1. This is indeed a classical theorem. One way to see it: by the ergodic theorem applied to the rotation by $x$ on the circle. Wait, no. Let me think about this differently.

Actually, the standard result is: for irrational $\alpha$, the sequence $\{n\alpha\}$ is equidistributed mod 1. And for a.e. $x$, $x$ is irrational, so $\{nx\}$ is equidistributed mod 1 for a.e. $x$.

Yes! That's the key. For every irrational $x$, the sequence $\{nx\}_{n \geq 1}$ is equidistributed mod 1 (Weyl's theorem). Since a.e. $x$ is irrational, we have equidistribution for a.e. $x$.

Now, if $\{nx\}$ is equidistributed mod 1, then for any measurable set $A \subset [0,1]$, 
$$\frac{1}{N}\sum_{n=1}^N \mathbf{1}_A(\{nx\}) \to |A|$$
where $|A|$ is the Lebesgue measure of $A$.

In particular, let $A = \{t \in [0,1] : f(t) = 1\}$ and $B = \{t \in [0,1] : f(t) = -1\}$. Then $A \cup B = [0,1]$ (up to measure zero) and $A \cap B = \emptyset$.

If $|A| > 0$, then for a.e. $x$, infinitely many $n$ have $\{nx\} \in A$, i.e., $f(nx) = 1$ for infinitely many $n$. So $\limsup f(nx) \geq 1$, hence $\limsup f(nx) = 1$ (since $f \leq 1$).

Similarly, if $|B| > 0$, then $\liminf f(nx) = -1$ for a.e. $x$.

But what if $|A| = 0$ or $|B| = 0$? 

If $f = 1$ a.e. (i.e., $|B| = 0$), then $f(nx) = 1$ for a.e. $x$ and all $n$... wait, not exactly. $f$ could be $-1$ on a measure-zero set. But $f(nx) = f(\{nx\})$, and $\{nx\}$ for a.e. $x$ is equidistributed, so it visits the measure-zero set $B$ with frequency 0. But it could still visit it infinitely often!

Hmm, this is the subtle point. Even if $|B| = 0$, the sequence $\{nx\}$ could hit $B$ infinitely often for some $x$.

Wait, but the question says $f(x) = \pm 1$, meaning $f$ takes values in $\{-1, +1\}$. It doesn't say $f$ is a.e. equal to a constant. 

Let me reconsider. The question is whether $\limsup f(nx) = +1$ and $\liminf f(nx) = -1$ a.e. This requires both $|A| > 0$ and $|B| > 0$.

If $f$ is identically $1$, then $\limsup f(nx) = 1$ but $\liminf f(nx) = 1 \neq -1$. So the answer to the first question would be NO in general.

Wait, but maybe the problem is asking whether this is true for all such $f$, or whether it's true for "generic" $f$? Let me re-read.

"We assume that $f(x)$ IS measurable ($L$), periodic, $f(x+1) = f(x)$ and $f(x) = \pm 1$. Do we have, almost everywhere, $\limsup_{n \to \infty} f(nx) = +1$, $\liminf_{n \to \infty} f(nx) = -1$?"

So the question is: for every such $f$, is it true that a.e. $\limsup f(nx) = 1$ and $\liminf f(nx) = -1$?

If $f \equiv 1$, this fails. So the answer would be NO.

But wait, maybe the problem is more subtle. Perhaps the problem is asking whether this is true for non-constant $f$, or perhaps there's a different interpretation.

Hmm, actually, let me reconsider. Maybe the problem is from a specific context where the answer is expected to be YES, and the interesting part is the proof. Or maybe the answer is NO and we need to provide a counterexample.

Let me think about the case where $f$ is not a.e. constant. Suppose $|A| > 0$ and $|B| > 0$ where $A = f^{-1}(1)$ and $B = f^{-1}(-1)$.

For a.e. $x$, $\{nx\}$ is equidistributed mod 1. By equidistribution, the frequency of visits to $A$ is $|A| > 0$, so there are infinitely many $n$ with $f(nx) = 1$, giving $\limsup \geq 1$, hence $\limsup = 1$. Similarly $\liminf = -1$.

So for non-a.e.-constant $f$ (both $|A|, |B| > 0$), the answer is YES.

But for $f \equiv 1$ or $f \equiv -1$ (a.e.), the answer is NO.

Actually, wait. Even if $f$ is a.e. constant but not identically constant, the situation is more subtle. If $f = 1$ a.e. but $f = -1$ on a measure-zero set $B$, then for a.e. $x$, does $\{nx\}$ hit $B$ infinitely often?

By equidistribution, the frequency is 0, but that doesn't preclude infinitely many visits. For example, if $B = \{1/2\}$, then $\{nx\} = 1/2$ iff $nx \equiv 1/2 \pmod{1}$, i.e., $x = (k + 1/2)/n$ for some integer $k$. For a fixed irrational $x$, this happens for at most finitely many $n$ (since $x$ is irrational, $\{nx\}$ never exactly equals $1/2$... actually it could, but only if $x$ is rational with appropriate denominator).

Hmm, actually for irrational $x$, $\{nx\}$ is never exactly $1/2$ (since $nx - 1/2$ would need to be an integer, meaning $x = (m + 1/2)/n$ is rational). So if $B$ is a countable set, then for a.e. (irrational) $x$, $\{nx\} \notin B$ for all $n$, so $f(nx) = 1$ for all $n$.

But if $B$ is an uncountable measure-zero set (like a Cantor set), the situation could be different.

Actually, for the equidistribution result, we know that for a.e. $x$, the empirical measure $\frac{1}{N}\sum_{n=1}^N \delta_{\{nx\}}$ converges weakly to Lebesgue measure. This means that for any continuity set $A$ (i.e., $|\partial A| = 0$), the frequency converges to $|A|$. But for a measure-zero set $B$, the frequency of visits is 0, which means the number of visits is $o(N)$. This doesn't tell us whether the number of visits is finite or infinite.

So the question of whether $\{nx\}$ hits a measure-zero set infinitely often for a.e. $x$ depends on the specific set.

OK so let me reconsider the problem. I think the problem is asking the question in full generality, and the answer might be:

For the first part: If $f$ takes both values $+1$ and $-1$ on sets of positive measure, then YES, $\limsup = 1$ and $\liminf = -1$ a.e. But if $f$ is a.e. constant, then NO.

But actually, re-reading the problem, I think the intent might be different. The problem says "$f(x) = \pm 1$" which I interpret as $f$ takes values in $\{-1, +1\}$. The question "Do we have..." is asking whether this is always true.

Given the trivial counterexample $f \equiv 1$, the answer to the first question is NO in general.

But wait, maybe the problem is more interesting than I think. Let me reconsider.

Actually, I think the problem might be asking about a specific $f$ that is given to be non-trivial, or the problem might be from a context where the interesting case is the non-constant one. Let me think about what the "right" answer is.

Hmm, actually, I think the problem is a well-known problem in ergodic theory / harmonic analysis, and the answer is YES for the first part (assuming $f$ takes both values on sets of positive measure) and the generalization is also YES.

Wait, let me reconsider the generalization more carefully.

**Part 2:** $f_n$ are measurable, uniformly bounded, $f_n(x + 1/n) = f_n(x)$. Is $\limsup f_n(x) = \text{const a.e.}$? Is $\liminf f_n(x) = \text{const a.e.}$?

The condition $f_n(x + 1/n) = f_n(x)$ means $f_n$ is periodic with period $1/n$.

So $f_n$ is $1/n$-periodic. This means $f_n$ is determined by its values on $[0, 1/n)$.

The connection to Part 1: if $f$ is 1-periodic and $f_n(x) = f(nx)$, then $f_n(x + 1/n) = f(n(x + 1/n)) = f(nx + 1) = f(nx) = f_n(x)$. So Part 1 is a special case of Part 2.

Now, for Part 2, the question is whether $\limsup f_n$ and $\liminf f_n$ are constants a.e.

Let me think about this. Each $f_n$ is $1/n$-periodic, so it's a function that oscillates faster and faster. 

Key idea: Consider $g_n(x) = f_n(x)$. Since $f_n$ is $1/n$-periodic, we can write $f_n(x) = h_n(\{nx\})$ where $h_n$ is a 1-periodic function (defined by $h_n(t) = f_n(t/n)$ for $t \in [0,1)$, extended periodically).

Wait, let me be more careful. If $f_n$ is $1/n$-periodic, then $f_n(x) = f_n(\{nx\}/n)$... no. Let me think again.

$f_n$ is $1/n$-periodic means $f_n(x + k/n) = f_n(x)$ for all integers $k$. So $f_n$ is determined by its values on $[0, 1/n)$. Define $h_n: [0,1) \to \mathbb{R}$ by $h_n(t) = f_n(t/n)$. Then $f_n(x) = h_n(\{nx\})$ where $\{nx\}$ is the fractional part of $nx$.

Check: $f_n(x) = f_n(x - \lfloor nx \rfloor / n) = f_n(\{nx\}/n) = h_n(\{nx\})$. Yes.

So $f_n(x) = h_n(\{nx\})$ where $h_n$ is a measurable function on $[0,1)$.

Now, the question becomes: is $\limsup_{n\to\infty} h_n(\{nx\})$ constant a.e.?

This is more subtle because $h_n$ changes with $n$.

Let me think about what tools we have. 

For the first part, where $h_n = f$ for all $n$ (a fixed function), the equidistribution of $\{nx\}$ for a.e. $x$ gives us the answer.

For the general case, we need something more.

Hmm, let me think about this differently. Let me consider the "averaging" approach.

Consider $S_N(x) = \frac{1}{N} \sum_{n=1}^N f_n(x)$. 

Actually, let me think about what $\int_0^1 f_n(x) dx$ is. Since $f_n$ is $1/n$-periodic, $\int_0^1 f_n(x) dx = \int_0^1 h_n(\{nx\}) dx$. By the substitution $u = nx$, $du = n\,dx$, $\int_0^1 h_n(\{nx\}) dx = \frac{1}{n} \int_0^n h_n(\{u\}) du = \frac{1}{n} \cdot n \int_0^1 h_n(t) dt = \int_0^1 h_n(t) dt$.

So $\int_0^1 f_n(x) dx = \int_0^1 h_n(t) dt =: a_n$.

Now, the question is about the pointwise behavior of $f_n(x)$.

Let me think about a specific approach. Consider two points $x, y \in [0,1)$. We want to understand when $\limsup f_n(x) = \limsup f_n(y)$.

Hmm, this is getting complicated. Let me think about the problem from a higher level.

Actually, I recall that this type of problem is related to the concept of "mixing" or "weak mixing" in ergodic theory. The key insight might be that the sequence of functions $f_n(x) = h_n(\{nx\})$ has some kind of mixing property.

Let me think about the correlation. Consider $\int_0^1 f_n(x) f_m(x) dx$ for $n \neq m$.

$\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx$.

By the substitution and using the fact that $(\{nx\}, \{mx\})$ is equidistributed in $[0,1)^2$ when $\gcd(n,m) = 1$ (and more generally when $n \neq m$), we get:

$\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx = \int_0^1 \int_0^1 h_n(s) h_m(t) ds\, dt = a_n \cdot a_m$

when $\gcd(n,m) = 1$. More generally, this holds when $n/m$ is irrational, but since $n, m$ are integers, $n/m$ is always rational. So we need to be more careful.

Actually, for integers $n \neq m$, the map $x \mapsto (\{nx\}, \{mx\})$ from $[0,1)$ to $[0,1)^2$ has its image on a subtorus. Specifically, if $d = \gcd(n,m)$, $n = da$, $m = db$ with $\gcd(a,b) = 1$, then $(\{nx\}, \{mx\}) = (d\{ax\}, d\{bx\})$... hmm, this isn't quite right.

Let me think differently. The map $x \mapsto (nx \mod 1, mx \mod 1)$ is a group homomorphism from $\mathbb{T}$ to $\mathbb{T}^2$. Its image is a closed subgroup. If $\gcd(n,m) = d$, then the image is $\{(s, t) \in \mathbb{T}^2 : bs \equiv at \pmod{1}\}$ where $n = da, m = db, \gcd(a,b)=1$. Wait, I need to think about this more carefully.

Actually, the image of $x \mapsto (nx, mx) \mod 1$ is the set $\{(nx \mod 1, mx \mod 1) : x \in \mathbb{T}\}$. This is a closed subgroup of $\mathbb{T}^2$. The Haar measure on this subgroup is the pushforward of Lebesgue measure on $\mathbb{T}$.

For the integral: $\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx = \int_{\text{image}} h_n(s) h_m(t) d\mu(s,t)$

where $\mu$ is the Haar measure on the image subgroup.

This is getting complicated. Let me try a different approach.

Let me think about the problem more carefully. The key question is: for the general case, is $\limsup f_n$ constant a.e.?

I think the answer is YES, and the proof uses the following idea:

Consider the "tail" behavior. For any two points $x, y$, we want to show that $\limsup f_n(x) = \limsup f_n(y)$ for a.e. $x, y$.

Actually, let me think about this problem differently. Let me consider the specific structure.

$f_n(x) = h_n(\{nx\})$ where $h_n: [0,1) \to \mathbb{R}$ is measurable and uniformly bounded.

For a.e. $x$, $\{nx\}$ is equidistributed mod 1. But $h_n$ changes with $n$, so equidistribution alone doesn't directly help.

Let me think about what "constant a.e." means for $\limsup$. It means there exists a constant $L$ such that $\limsup_{n\to\infty} f_n(x) = L$ for a.e. $x$.

Hmm, let me think about a potential approach using the Borel-Cantelli lemma or some density argument.

Actually, I think the key insight is the following. Let me consider the set $E_{n,\epsilon} = \{x : f_n(x) > L + \epsilon\}$ for some threshold $L$. We want to understand the measure of this set.

$|E_{n,\epsilon}| = |\{x \in [0,1) : h_n(\{nx\}) > L + \epsilon\}| = |\{t \in [0,1) : h_n(t) > L + \epsilon\}|$

by the equidistribution of $\{nx\}$ (the map $x \mapsto \{nx\}$ preserves Lebesgue measure on $[0,1)$... wait, does it?).

Actually, the map $x \mapsto \{nx\}$ from $[0,1)$ to $[0,1)$ is $n$-to-1 and preserves Lebesgue measure. So $|\{x : h_n(\{nx\}) > c\}| = |\{t : h_n(t) > c\}|$.

So $|E_{n,\epsilon}| = |\{t : h_n(t) > L + \epsilon\}|$.

Now, $\limsup f_n(x) > L + \epsilon$ iff $x \in \limsup E_{n,\epsilon}$ (i.e., $x$ is in infinitely many $E_{n,\epsilon}$).

By Borel-Cantelli, if $\sum_n |E_{n,\epsilon}| < \infty$, then $|\limsup E_{n,\epsilon}| = 0$, so $\limsup f_n(x) \leq L + \epsilon$ a.e.

But we don't have control over $\sum_n |E_{n,\epsilon}|$ in general.

Hmm, let me think about this differently.

Actually, I think the answer to the general question is YES, and the proof is based on the following key lemma:

**Key Lemma:** For any measurable, uniformly bounded sequence $f_n$ with $f_n$ being $1/n$-periodic, and for any $a < b$, the set $\{x : \liminf f_n(x) < a < b < \limsup f_n(x)\}$ has measure 0.

This would imply that $\limsup f_n$ and $\liminf f_n$ are each constant a.e. (though they might not be equal, i.e., the limit might not exist).

Let me think about how to prove this. The idea is to show that for any interval $(a, b)$, the set where $\liminf < a$ and $\limsup > b$ has measure 0.

Hmm, actually, I'm not sure this is true in general. Let me think of a potential counterexample.

Consider $h_n(t) = \mathbf{1}_{[0, 1/2)}(t) - \mathbf{1}_{[1/2, 1)}(t)$, i.e., $h_n$ is the same for all $n$. Then $f_n(x) = h(\{nx\})$ where $h$ is the $\pm 1$ function that's $+1$ on $[0,1/2)$ and $-1$ on $[1/2,1)$. By equidistribution, for a.e. $x$, $\limsup f_n(x) = 1$ and $\liminf f_n(x) = -1$. So both are constant a.e. (with $\limsup = 1$ and $\liminf = -1$). Good.

Now consider a different example. Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $f_n(x) = \mathbf{1}_{[0, 1/n)}(\{nx\})$. Now $|E_n| = 1/n$, and $\sum 1/n = \infty$. By the equidistribution and the second moment method (or direct computation), we can check whether $\limsup f_n(x) = 1$ a.e.

$f_n(x) = 1$ iff $\{nx\} < 1/n$, i.e., $nx \mod 1 < 1/n$, i.e., $x \in [k/n, (k+1)/n)$ for some $k$ with $nx - k < 1/n$... wait, $\{nx\} < 1/n$ means $nx = k + \epsilon$ with $0 \leq \epsilon < 1/n$, i.e., $x \in [k/n, k/n + 1/n^2)$ for some $k = 0, 1, \ldots, n-1$.

So $E_n = \bigcup_{k=0}^{n-1} [k/n, k/n + 1/n^2)$, which has measure $n \cdot 1/n^2 = 1/n$.

For a.e. $x$, is $x \in E_n$ for infinitely many $n$? Since $\sum |E_n| = \sum 1/n = \infty$, Borel-Cantelli doesn't directly give us the answer. We need to check independence or quasi-independence.

Actually, let me check: for $x$ irrational, when is $\{nx\} < 1/n$? This is related to the continued fraction expansion of $x$. By the three-distance theorem or Diophantine approximation, for a.e. $x$, $\|nx\| < 1/n$ infinitely often (where $\|nx\|$ is the distance to the nearest integer). But we need $\{nx\} < 1/n$, not $\|nx\| < 1/n$.

Actually, $\{nx\} < 1/n$ is a one-sided condition. By the theory of continued fractions, for a.e. $x$, $\{nx\} < 1/n$ infinitely often (this follows from the Khintchine theorem or similar results in Diophantine approximation). So $\limsup f_n(x) = 1$ for a.e. $x$.

And $\liminf f_n(x) = 0$ (since $f_n \geq 0$ and $f_n(x) = 0$ for most $n$). So $\limsup = 1$ and $\liminf = 0$, both constant a.e. Good.

Now let me try to construct a counterexample where $\limsup$ is NOT constant.

Hmm, what if I make $h_n$ depend on $n$ in a way that "targets" specific $x$ values?

For instance, let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t - \{n\alpha\})$ for some fixed irrational $\alpha$... no, this doesn't quite work because $h_n$ is a function on $[0,1)$ and I need to be careful.

Actually, let me think about this more carefully. The key constraint is that $f_n(x) = h_n(\{nx\})$, and $h_n$ can be any measurable function on $[0,1)$.

Consider $h_n(t) = \mathbf{1}_{\{t < 1/n\}}$. Then $f_n(x) = 1$ iff $\{nx\} < 1/n$. As discussed, for a.e. $x$, this happens infinitely often, so $\limsup = 1$ a.e.

What if $h_n(t) = \mathbf{1}_{\{t \in [a_n, a_n + 1/n)\}}$ for some sequence $a_n$? Then $f_n(x) = 1$ iff $\{nx\} \in [a_n, a_n + 1/n)$. 

By the equidistribution of $\{nx\}$, for a.e. $x$, the sequence $\{nx\}$ is equidistributed, so it visits $[a_n, a_n + 1/n)$ with "expected frequency" $1/n$. But since the interval changes with $n$, this is more subtle.

Actually, I think the key tool here is the following. For a.e. $x$, the sequence $\{nx\}$ is not just equidistributed but has stronger properties. Specifically, for a.e. $x$, the sequence $\{nx\}$ is "Poissonian" in a certain sense (this is related to the pair correlation problem).

But I think for this problem, we might not need such deep results. Let me think about the structure more.

Let me consider the problem from the perspective of the "translation" structure. The key observation is:

$f_n(x) = h_n(\{nx\})$, and the map $x \mapsto \{nx\}$ is measure-preserving from $([0,1), \text{Lebesgue})$ to $([0,1), \text{Lebesgue})$.

So $f_n$ has the same distribution as $h_n$ (as random variables on $[0,1)$). That is, for any Borel set $B$, $|\{x : f_n(x) \in B\}| = |\{t : h_n(t) \in B\}|$.

Now, the question is about the joint distribution of $(f_1, f_2, f_3, \ldots)$ and specifically about $\limsup$ and $\liminf$.

Let me think about the correlation between $f_n$ and $f_m$.

$\int_0^1 f_n(x) f_m(x) dx = \int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx$.

As I discussed before, this involves the joint distribution of $(\{nx\}, \{mx\})$.

For $n \neq m$, the map $x \mapsto (\{nx\}, \{mx\})$ from $[0,1)$ to $[0,1)^2$ has its image on a 1-dimensional subtorus. The pushforward of Lebesgue measure is the Haar measure on this subtorus.

If $\gcd(n, m) = 1$, then the map $x \mapsto (\{nx\}, \{mx\})$ is actually a bijection (mod 1) from $[0,1)$ to the subtorus $\{(s,t) : ns \equiv mt \pmod{1}\}$... hmm, wait. Let me think again.

If $\gcd(n,m) = 1$, then there exist integers $a, b$ with $an + bm = 1$. The map $x \mapsto (nx \mod 1, mx \mod 1)$ is injective (mod 1): if $nx_1 \equiv nx_2$ and $mx_1 \equiv mx_2 \pmod{1}$, then $n(x_1 - x_2) \equiv 0$ and $m(x_1 - x_2) \equiv 0 \pmod{1}$, so $(x_1 - x_2) \equiv 0 \pmod{1}$ (since $\gcd(n,m) = 1$). So the map is a bijection from $\mathbb{T}$ to a closed subgroup of $\mathbb{T}^2$.

The image is $\{(s,t) \in \mathbb{T}^2 : ms \equiv nt \pmod{1}\}$ (this is the kernel of the map $(s,t) \mapsto ms - nt \mod 1$). This is a 1-dimensional subtorus.

The pushforward of Lebesgue measure is the Haar measure on this subtorus, which is NOT the product measure. So $\{nx\}$ and $\{mx\}$ are NOT independent (as random variables on $[0,1)$ with Lebesgue measure).

This means the correlation $\int f_n f_m$ is NOT simply $a_n \cdot a_m$ in general. It depends on the specific functions $h_n, h_m$ and the subtorus.

This makes the problem more complex. Let me think about whether the result is still true.

Actually, let me reconsider. Maybe I should think about this problem using a different approach. Let me consider the "ergodic" approach.

Consider the space $X = [0,1)^\mathbb{N}$ with the product measure, and the map $\Phi: [0,1) \to X$ given by $\Phi(x) = (\{x\}, \{2x\}, \{3x\}, \ldots)$. The pushforward of Lebesgue measure under $\Phi$ is some measure $\mu$ on $X$.

The question is about the $\mu$-a.e. behavior of $\limsup h_n(\pi_n(\cdot))$ where $\pi_n$ is the $n$-th coordinate projection.

If $\mu$ were the product measure, then the coordinates would be independent, and we could use standard tools. But $\mu$ is NOT the product measure (the coordinates are correlated).

However, there's a key property: the sequence $(\{nx\})_{n \geq 1}$ is equidistributed for a.e. $x$, and more strongly, it satisfies a "mixing" property in some sense.

Let me think about a specific approach. 

**Approach: Show that $\limsup f_n$ is invariant under translations, hence constant a.e.**

If I can show that $\limsup f_n(x) = \limsup f_n(x + \alpha)$ for a.e. $x$ and for all $\alpha$ (or for a dense set of $\alpha$), then $\limsup f_n$ is invariant under all translations, hence constant a.e.

But this seems hard because $f_n(x + \alpha) = h_n(\{n(x+\alpha)\}) = h_n(\{nx + n\alpha\})$, which is a "shifted" version of $h_n$.

Hmm, this doesn't directly work because the shift $n\alpha$ depends on $n$.

Let me try another approach.

**Approach: Use the specific structure of the problem.**

Let me think about what happens when we "average" $f_n$ over a small interval.

Consider $\frac{1}{|I|} \int_I f_n(x) dx$ for an interval $I$. Since $f_n$ is $1/n$-periodic, for $|I| \gg 1/n$, this average is approximately $\int_0^1 h_n(t) dt = a_n$.

More precisely, if $I = [y, y+\delta]$, then $\int_I f_n(x) dx = \int_y^{y+\delta} h_n(\{nx\}) dx = \frac{1}{n} \int_{ny}^{n(y+\delta)} h_n(\{u\}) du$.

If $n\delta$ is large, this is approximately $\delta \cdot a_n$ (by the periodicity of $h_n(\{u\})$ with period 1, the integral over a long interval is approximately the length times the average).

So $\frac{1}{\delta} \int_I f_n(x) dx \approx a_n$ when $n \gg 1/\delta$.

This means that for large $n$, $f_n$ "averages out" to $a_n$ on any fixed interval. This is a kind of "weak convergence" or "oscillatory convergence" property.

But this doesn't directly tell us about pointwise $\limsup$.

Let me think about the problem differently. Maybe I should consider the specific case first and then generalize.

**Part 1 revisited:**

$f$ is 1-periodic, $f: \mathbb{R} \to \{-1, +1\}$, measurable. Let $A = \{t \in [0,1) : f(t) = 1\}$, $B = \{t \in [0,1) : f(t) = -1\}$.

Case 1: $|A| = 0$. Then $f = -1$ a.e. For a.e. $x$, $\{nx\}$ is equidistributed, so $\{nx\} \in A$ with frequency 0. But does $\{nx\} \in A$ for infinitely many $n$?

If $A$ is, say, a single point $\{t_0\}$, then $\{nx\} = t_0$ iff $x = (k + t_0)/n$ for some integer $k$, which means $x$ is rational (if $t_0$ is rational) or $x$ is in a specific countable set. For a.e. $x$ (irrational), $\{nx\} \neq t_0$ for all $n$, so $f(nx) = -1$ for all $n$, and $\limsup = \liminf = -1$.

But if $A$ is a "fat" measure-zero set (like a set of Hausdorff dimension 1 but measure 0), it's possible that $\{nx\} \in A$ for infinitely many $n$ for a.e. $x$.

Hmm, actually, I think for any measure-zero set $A$, for a.e. $x$, $\{nx\} \notin A$ for all but finitely many $n$. Is this true?

No, this is NOT true in general. Consider $A = \bigcup_n \{t : \|nt\| < 1/n^2\}$... this is getting complicated.

Actually, let me think about it differently. By the Borel-Cantelli lemma, if $\sum_n |\{x : \{nx\} \in A\}| < \infty$, then for a.e. $x$, $\{nx\} \in A$ for only finitely many $n$. Now, $|\{x : \{nx\} \in A\}| = |A|$ (since $x \mapsto \{nx\}$ is measure-preserving). So $\sum_n |A| = \infty$ if $|A| > 0$, and $= 0$ if $|A| = 0$.

Wait, if $|A| = 0$, then $|\{x : \{nx\} \in A\}| = 0$ for each $n$, so the sum is 0, and by Borel-Cantelli, for a.e. $x$, $\{nx\} \in A$ for only finitely many $n$. Actually, even stronger: the set $\{x : \{nx\} \in A \text{ for some } n\}$ has measure 0 (since it's a countable union of measure-zero sets). So for a.e. $x$, $\{nx\} \notin A$ for ALL $n$.

Wait, that's not right either. $|\{x : \{nx\} \in A\}| = |A| = 0$ for each $n$ (since the map $x \mapsto \{nx\}$ preserves measure). So $\bigcup_n \{x : \{nx\} \in A\}$ has measure 0. Therefore, for a.e. $x$, $\{nx\} \notin A$ for all $n \geq 1$.

So if $|A| = 0$, then for a.e. $x$, $f(nx) = -1$ for all $n$, and $\limsup = \liminf = -1$.

Similarly, if $|B| = 0$, then for a.e. $x$, $f(nx) = 1$ for all $n$, and $\limsup = \liminf = 1$.

If $|A| > 0$ and $|B| > 0$, then for a.e. $x$, $\{nx\}$ is equidistributed, so it visits $A$ with frequency $|A| > 0$ and $B$ with frequency $|B| > 0$. In particular, it visits both $A$ and $B$ infinitely often, so $\limsup f(nx) = 1$ and $\liminf f(nx) = -1$.

So for Part 1:
- If $f$ takes both values on sets of positive measure: $\limsup = 1$, $\liminf = -1$ a.e. ✓
- If $f = 1$ a.e.: $\limsup = \liminf = 1$ a.e.
- If $f = -1$ a.e.: $\limsup = \liminf = -1$ a.e.

In all cases, $\limsup$ is constant a.e. and $\liminf$ is constant a.e. But the specific values $\limsup = 1, \liminf = -1$ only hold when $f$ takes both values on positive measure sets.

So the answer to "do we have $\limsup = 1, \liminf = -1$ a.e.?" is: YES if $f$ takes both values $+1$ and $-1$ on sets of positive Lebesgue measure; NO in general (trivial counterexample: $f \equiv 1$).

But I think the problem is asking whether this is true for all such $f$, and the answer is NO (with the trivial counterexample). But perhaps the problem is asking about the non-trivial case, or perhaps the answer is meant to be YES with the understanding that $f$ is non-constant.

Hmm, let me re-read the problem. "We assume that $f(x)$ IS measurable ($L$), periodic, $f(x+1) = f(x)$ and $f(x) = \pm 1$. Do we have, almost everywhere, $\limsup = +1, \liminf = -1$?"

I think the problem is asking: given these conditions, is it necessarily true that $\limsup = 1$ and $\liminf = -1$ a.e.? The answer is NO if $f$ is a.e. constant, but YES if $f$ takes both values on positive measure sets.

But actually, I think the more interesting question is the general one (Part 2), and the answer there is also that $\limsup$ and $\liminf$ are constant a.e.

Let me now focus on Part 2 and try to prove that $\limsup f_n$ is constant a.e. (and similarly for $\liminf$).

**Part 2: Proof that $\limsup f_n$ is constant a.e.**

Let $f_n$ be measurable, uniformly bounded (say $|f_n| \leq M$), and $1/n$-periodic.

We write $f_n(x) = h_n(\{nx\})$ where $h_n: [0,1) \to [-M, M]$ is measurable.

**Step 1: $\limsup f_n$ is invariant under rational translations.**

Consider $f_n(x + p/q)$ for a rational $p/q$. We have $f_n(x + p/q) = h_n(\{nx + np/q\})$.

Now, $\{nx + np/q\} = \{nx + np/q\}$. The shift $np/q \mod 1$ depends on $n$.

For $n$ divisible by $q$, say $n = qm$, we have $np/q = mp$, which is an integer, so $\{nx + np/q\} = \{nx\}$. Thus $f_n(x + p/q) = f_n(x)$ for all $n$ divisible by $q$.

So $\limsup_{n \to \infty} f_n(x + p/q) \geq \limsup_{m \to \infty} f_{qm}(x + p/q) = \limsup_{m \to \infty} f_{qm}(x)$.

Similarly, $\limsup_{n \to \infty} f_n(x) \geq \limsup_{m \to \infty} f_{qm}(x)$.

But this only gives us inequalities between the limsups along subsequences, not equality.

Hmm, let me think more carefully.

Let $L(x) = \limsup_{n \to \infty} f_n(x)$ and $L_q(x) = \limsup_{m \to \infty} f_{qm}(x)$.

We have $L(x) \geq L_q(x)$ for all $q$ (since $\{qm\}$ is a subsequence of $\{n\}$).

Also, $L(x + p/q) \geq L_q(x + p/q) = L_q(x)$ (since $f_{qm}(x + p/q) = f_{qm}(x)$).

And $L(x) \geq L_q(x)$.

But we also need the reverse inequality. We have $L(x) = \max_{r=0,\ldots,q-1} L_q^{(r)}(x)$ where $L_q^{(r)}(x) = \limsup_{m \to \infty} f_{qm+r}(x)$... no, that's not right either. $\limsup$ of the full sequence is the max of the limsups of the subsequences only if we take the max over all residue classes, but actually $\limsup_{n} a_n = \max_{r=0}^{q-1} \limsup_m a_{qm+r}$.

So $L(x) = \max_{r=0}^{q-1} L_q^{(r)}(x)$ where $L_q^{(r)}(x) = \limsup_{m \to \infty} f_{qm+r}(x)$.

Now, $f_{qm+r}(x + p/q) = h_{qm+r}(\{(qm+r)x + (qm+r)p/q\}) = h_{qm+r}(\{(qm+r)x + rp/q\})$ (since $(qm)p/q = mp$ is an integer).

So $f_{qm+r}(x + p/q) = h_{qm+r}(\{(qm+r)x + rp/q\})$.

This is NOT simply $f_{qm+r}(x)$ unless $r = 0$. So the invariance under rational translations only works for the subsequence where $q | n$.

This approach is getting complicated. Let me try a different strategy.

**Step 2: Use the density of rational translates and Fubini.**

Actually, let me try a more direct approach. The key idea is:

For any $\epsilon > 0$ and any $a \in \mathbb{R}$, define $E_n(a, \epsilon) = \{x \in [0,1) : f_n(x) > a + \epsilon\}$. Then $|E_n(a, \epsilon)| = |\{t \in [0,1) : h_n(t) > a + \epsilon\}|$ (since $x \mapsto \{nx\}$ preserves measure).

Let $\alpha_n(a, \epsilon) = |E_n(a, \epsilon)| = |\{t : h_n(t) > a + \epsilon\}|$.

Now, $\{x : L(x) > a + \epsilon\} \subseteq \limsup_n E_n(a, \epsilon)$ (where $\limsup$ of sets means $\bigcap_N \bigcup_{n \geq N} E_n$).

If $\sum_n \alpha_n(a, \epsilon) < \infty$, then by Borel-Cantelli, $|\limsup_n E_n(a, \epsilon)| = 0$, so $L(x) \leq a + \epsilon$ a.e.

But we don't have control over $\sum_n \alpha_n$ in general.

Hmm, let me think about this differently. Maybe the answer is actually NO for the general case, and we need a counterexample.

**Potential counterexample for Part 2:**

Let me try to construct $f_n$ such that $\limsup f_n(x)$ is not constant.

Idea: Make $f_n$ "target" a specific set of $x$ values.

Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/n\} = \mathbf{1}_{x \in \bigcup_{k=0}^{n-1} [k/n, k/n + 1/n^2)}$.

As computed before, $|E_n| = 1/n$, and $\sum 1/n = \infty$.

For a.e. $x$, is $x \in E_n$ for infinitely many $n$? This is the question of whether $\{nx\} < 1/n$ infinitely often for a.e. $x$.

By the theory of continued fractions, for a.e. $x$, $\{nx\} < 1/n$ infinitely often. In fact, by Khintchine's theorem, for a.e. $x$, $\|nx\| < \psi(n)$ infinitely often iff $\sum \psi(n) = \infty$ (for monotone $\psi$). Here $\|nx\|$ is the distance to the nearest integer, and $\psi(n) = 1/n$ gives $\sum 1/n = \infty$. But we need $\{nx\} < 1/n$ (one-sided), not $\|nx\| < 1/n$.

By a one-sided version, for a.e. $x$, $\{nx\} < 1/n$ infinitely often. So $\limsup f_n(x) = 1$ for a.e. $x$.

And $\liminf f_n(x) = 0$ for a.e. $x$ (since $f_n(x) = 0$ for "most" $n$). So both are constant a.e.

Let me try a different counterexample. What if I make $h_n$ depend on $n$ in a way that creates non-constant limsup?

Consider $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n$ odd and $h_n(t) = \mathbf{1}_{[1/2, 1)}(t)$ for $n$ even. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/2\}$ for $n$ odd and $f_n(x) = \mathbf{1}_{\{nx\} \geq 1/2\}$ for $n$ even. For a.e. $x$, $\{nx\}$ is equidistributed, so both $\{nx\} < 1/2$ and $\{nx\} \geq 1/2$ happen infinitely often. So $\limsup f_n(x) = 1$ and $\liminf f_n(x) = 0$ for a.e. $x$. Still constant.

What if I make the sets depend on $n$ more cleverly?

Let $A_n \subset [0,1)$ be measurable sets with $|A_n| = 1/2$ for all $n$, and $h_n = \mathbf{1}_{A_n}$. Then $f_n(x) = \mathbf{1}_{A_n}(\{nx\})$, and $|\{x : f_n(x) = 1\}| = 1/2$.

For the limsup to be non-constant, I would need the set $\{x : \{nx\} \in A_n \text{ i.o.}\}$ to have measure strictly between 0 and 1.

But by the Borel-Cantelli lemma (independence version), if the events $\{x : \{nx\} \in A_n\}$ were independent, then since $\sum |A_n| = \sum 1/2 = \infty$, the limsup would have measure 1. But the events are NOT independent.

However, there might be a "quasi-independence" result that still gives measure 1 for the limsup.

Hmm, let me think about this more carefully. The events $E_n = \{x : \{nx\} \in A_n\}$ have $|E_n| = |A_n| = 1/2$. The question is whether $|\limsup E_n| = 1$.

Actually, I think there's a general result that says: for any sequence of measurable sets $A_n \subset [0,1)$ with $|A_n| = \alpha > 0$, the set $\{x : \{nx\} \in A_n \text{ i.o.}\}$ has measure 1.

This would follow from a "Borel-Cantelli with quasi-independence" result. Let me think about whether this is true.

The key is to estimate $|E_n \cap E_m|$ for $n \neq m$. We have $E_n \cap E_m = \{x : \{nx\} \in A_n \text{ and } \{mx\} \in A_m\}$.

$|E_n \cap E_m| = \int_0^1 \mathbf{1}_{A_n}(\{nx\}) \mathbf{1}_{A_m}(\{mx\}) dx$.

As discussed, this equals the integral of $\mathbf{1}_{A_n}(s) \mathbf{1}_{A_m}(t)$ over the subtorus $\{(s,t) : ms \equiv nt \pmod{1}\}$ with respect to Haar measure.

If $\gcd(n,m) = 1$, the subtorus is $\{(s,t) : ms - nt \in \mathbb{Z}\}$, which is a 1-dimensional subtorus. The Haar measure on this subtorus is the pushforward of Lebesgue measure under $x \mapsto (\{nx\}, \{mx\})$.

In general, $|E_n \cap E_m|$ can range from $\max(0, |A_n| + |A_m| - 1)$ to $\min(|A_n|, |A_m|)$, depending on the alignment of $A_n$ and $A_m$ on the subtorus.

If $A_n = A_m = [0, 1/2)$ and $\gcd(n,m) = 1$, then $|E_n \cap E_m| = |\{x : \{nx\} < 1/2, \{mx\} < 1/2\}|$. This is the measure of the set of $x$ where both $\{nx\}$ and $\{mx\}$ are in $[0, 1/2)$. By the equidistribution on the subtorus, this is $1/4$ if the subtorus is "generic" enough. But it could be different.

Actually, for $n = 1, m = 2$: $|E_1 \cap E_2| = |\{x \in [0,1) : x < 1/2, \{2x\} < 1/2\}| = |\{x \in [0, 1/4)\}| = 1/4 = |A_1| \cdot |A_2|$. So in this case, it's the product.

For $n = 1, m = 3$: $|E_1 \cap E_3| = |\{x \in [0,1) : x < 1/2, \{3x\} < 1/2\}|$. $\{3x\} < 1/2$ iff $x \in [0, 1/6) \cup [1/3, 1/2) \cup [2/3, 5/6)$. Intersecting with $[0, 1/2)$: $[0, 1/6) \cup [1/3, 1/2)$, which has measure $1/6 + 1/6 = 1/3$. This is NOT $1/4$.

So the events are not independent, and the correlation can be different from the product.

This makes the Borel-Cantelli approach more difficult. Let me think about whether there's a general theorem that handles this.

Actually, I recall that there's a result by Gallagher (or maybe it's a consequence of the Erdős–Turán inequality or the large sieve) that gives a Borel-Cantelli type result for the sequence $\{nx\}$.

Actually, I think the key result is the following: for any sequence of intervals $I_n \subset [0,1)$ with $\sum |I_n| = \infty$, the set $\{x : \{nx\} \in I_n \text{ i.o.}\}$ has full measure. This is a theorem by Khintchine (or maybe a consequence of the Duffin-Schaeffer theorem).

But for general measurable sets (not intervals), the situation might be different.

Hmm, let me think about this problem from a completely different angle.

**Alternative approach: Use the ergodic theorem.**

Consider the transformation $T: [0,1) \to [0,1)$, $T(x) = \{x + \alpha\}$ for some irrational $\alpha$. This is ergodic.

Now, $f_n(T(x)) = f_n(\{x + \alpha\}) = h_n(\{n(x + \alpha)\}) = h_n(\{nx + n\alpha\})$.

This is a "shifted" version of $h_n$, and the shift $n\alpha \mod 1$ varies with $n$.

This doesn't directly give us ergodicity of the limsup.

**Another approach: Use the fact that $f_n$ "converges weakly" to its average.**

As I noted before, for any fixed interval $I$, $\frac{1}{|I|} \int_I f_n(x) dx \to a_n$ as $n \to \infty$ (where $a_n = \int_0^1 h_n(t) dt$), because $f_n$ oscillates with period $1/n$.

More precisely, $|\frac{1}{|I|} \int_I f_n(x) dx - a_n| \leq \frac{C}{n|I|}$ for some constant $C$ depending on $M$ (the uniform bound).

This means $f_n \rightharpoonup a_n$ weakly in $L^\infty$ (against $L^1$ test functions that are "fixed").

But this doesn't directly help with pointwise limsup.

**Yet another approach: Direct computation using the structure.**

Let me try to show that $\limsup f_n(x)$ is the same for a.e. $x$ by showing that it's "translation-invariant" in some sense.

Consider two points $x$ and $y = x + \delta$ for small $\delta$. We want to compare $\limsup f_n(x)$ and $\limsup f_n(y)$.

$f_n(y) = f_n(x + \delta) = h_n(\{nx + n\delta\})$.

For large $n$, $n\delta \mod 1$ "sweeps" through $[0,1)$ rapidly (if $\delta$ is irrational). So $h_n(\{nx + n\delta\})$ is like $h_n$ evaluated at a "random" point (shifted from $\{nx\}$ by $n\delta$).

But this heuristic is hard to make rigorous.

Let me try yet another approach.

**Approach via conditional expectation and martingale-like arguments:**

Hmm, I don't see an immediate connection.

**Let me reconsider the problem statement.**

The problem asks two questions:
1. For $f$ 1-periodic, $\pm 1$-valued, measurable: is $\limsup f(nx) = 1, \liminf f(nx) = -1$ a.e.?
2. For $f_n$ uniformly bounded, measurable, $1/n$-periodic: is $\limsup f_n = \text{const}$ a.e.? Is $\liminf f_n = \text{const}$ a.e.?

I think the answer to both is YES (with the caveat for Part 1 that $f$ must take both values on positive measure sets for the specific values $+1, -1$).

For Part 2, the answer is that $\limsup$ and $\liminf$ are constant a.e., and I think this can be proved using the following key idea:

**Key Idea: For any $a$, the set $\{x : \limsup f_n(x) > a\}$ is invariant under all translations, hence has measure 0 or 1.**

To show invariance under translations, we need to show that $\limsup f_n(x) = \limsup f_n(x + \delta)$ for a.e. $x$, for any $\delta$.

Let me try to prove this. Fix $\delta \in [0,1)$.

$f_n(x + \delta) = h_n(\{n(x+\delta)\}) = h_n(\{nx + n\delta\})$.

Let $\theta_n = \{n\delta\}$. Then $f_n(x + \delta) = h_n(\{nx + \theta_n\})$.

Now, define $\tilde{h}_n(t) = h_n(\{t + \theta_n\})$. Then $f_n(x + \delta) = \tilde{h}_n(\{nx\})$.

So the question becomes: is $\limsup h_n(\{nx\}) = \limsup \tilde{h}_n(\{nx\})$ for a.e. $x$?

This is not obvious because $h_n$ and $\tilde{h}_n$ differ by a shift that depends on $n$.

Hmm, this approach doesn't seem to work directly.

**Let me try a completely different approach: the 0-1 law.**

I want to show that for any $a$, $|\{x : \limsup f_n(x) > a\}| \in \{0, 1\}$.

Consider the $\sigma$-algebra $\mathcal{F}_n = \sigma(f_n, f_{n+1}, \ldots)$ (the "tail" $\sigma$-algebra). The limsup is $\mathcal{F}_1$-measurable (it's in the tail $\sigma$-algebra $\bigcap_n \mathcal{F}_n$).

If we can show that the tail $\sigma$-algebra is trivial (i.e., contains only sets of measure 0 or 1), then $\limsup f_n$ is constant a.e.

But the tail $\sigma$-algebra being trivial is exactly a 0-1 law, which typically requires some kind of independence or mixing.

The issue is that the $f_n$ are not independent. So we need to show some form of mixing.

Let me think about the mixing property. For $n \neq m$, consider the correlation:

$\text{Cov}(f_n, f_m) = \int_0^1 f_n(x) f_m(x) dx - \left(\int_0^1 f_n\right)\left(\int_0^1 f_m\right)$

$= \int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx - a_n a_m$.

As discussed, this depends on the joint distribution of $(\{nx\}, \{mx\})$ and the specific functions $h_n, h_m$.

For $\gcd(n,m) = 1$, the joint distribution is the Haar measure on the subtorus $\{(s,t) : ms \equiv nt \pmod{1}\}$. In general, the covariance can be non-zero.

So the $f_n$ are not uncorrelated, and a standard 0-1 law doesn't apply.

However, maybe we can use a more refined argument. Let me think about the structure of the correlations.

For $n$ and $m$ with $\gcd(n,m) = d$, $n = da, m = db$, $\gcd(a,b) = 1$:

$\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx = \int_0^1 h_{da}(\{dax\}) h_{db}(\{dbx\}) dx$.

Let $u = dx$. Then $\{dax\} = \{a \cdot dx\}$ and $\{dbx\} = \{b \cdot dx\}$. Let $y = dx \mod 1$, so $y$ is uniform on $[0,1)$ (as $x$ ranges over $[0,1)$, $dx$ ranges over $[0,d)$, and $\{dx\}$ is uniform on $[0,1)$). Then:

$\int_0^1 h_{da}(\{ay\}) h_{db}(\{by\}) dy$.

Now, since $\gcd(a,b) = 1$, the map $y \mapsto (\{ay\}, \{by\})$ is a bijection from $[0,1)$ to the subtorus $T_{a,b} = \{(s,t) : bs \equiv at \pmod{1}\}$, and the pushforward of Lebesgue measure is Haar measure on $T_{a,b}$.

So $\int_0^1 h_{da}(\{ay\}) h_{by}(\{by\}) dy = \int_{T_{a,b}} h_{da}(s) h_{db}(t) d\mu_{a,b}(s,t)$.

This is NOT $\int h_{da} \int h_{db} = a_{da} \cdot a_{db}$ in general.

So the correlations are non-trivial. This makes the 0-1 law approach difficult.

Let me try to think about specific cases where the correlations might cause problems.

**Case: $f_n(x) = h(\{nx\})$ for a fixed $h$.**

In this case, $a_n = \int h$ for all $n$, and the covariance is:

$\text{Cov}(f_n, f_m) = \int_{T_{a,b}} h(s) h(t) d\mu_{a,b}(s,t) - \left(\int h\right)^2$.

For $h = \mathbf{1}_{[0,\alpha)}$ (indicator of an interval), the covariance depends on the specific subtorus.

But in this case, we already know the answer from Part 1: by equidistribution, $\limsup f_n(x) = \text{ess sup } h$ and $\liminf f_n(x) = \text{ess inf } h$ for a.e. $x$ (assuming $h$ takes its ess sup and ess inf on positive measure sets). So the limsup and liminf are constant a.e.

**Back to the general case:**

Let me try a different approach. I'll try to show that for any two points $x, y$ that are "generic" (in a suitable sense), $\limsup f_n(x) = \limsup f_n(y)$.

Actually, let me try to use the following strategy:

1. Show that $\limsup f_n(x) \geq \limsup a_n$ for a.e. $x$ (where $a_n = \int_0^1 h_n$).
2. Show that $\limsup f_n(x) \leq \limsup \text{ess sup } h_n$ for a.e. $x$.
3. Show that the actual value of $\limsup f_n(x)$ is the same for a.e. $x$.

Hmm, this is still vague. Let me think more concretely.

Actually, let me reconsider. Maybe the answer to Part 2 is actually NO, and we need a counterexample.

**Constructing a counterexample:**

Let me try to construct $f_n$ such that $\limsup f_n(x)$ depends on $x$.

Idea: Use binary expansion. Let $x = 0.x_1 x_2 x_3 \ldots$ in binary. Define $f_n(x)$ based on the $n$-th binary digit of $x$.

But $f_n$ needs to be $1/n$-periodic, which is a strong constraint. The $n$-th binary digit of $x$ is determined by $\{2^n x\}$, and the function $\mathbf{1}_{\{2^n x\} \geq 1/2}$ is $1/2^n$-periodic, not $1/n$-periodic. So this doesn't directly work.

Let me think about what $1/n$-periodic functions look like. $f_n$ is $1/n$-periodic, so it's constant on intervals of length $1/n$ (if it's a step function). More generally, $f_n(x) = h_n(\{nx\})$ where $h_n$ is 1-periodic.

To make $\limsup f_n(x)$ depend on $x$, I would need to "encode" information about $x$ into the sequence $h_n(\{nx\})$.

The key constraint is that $\{nx\}$ for a.e. $x$ is equidistributed, so the "information" about $x$ that can be extracted from $\{nx\}$ is limited.

But wait, $\{nx\}$ for different $n$ are correlated (they all depend on the same $x$). So in principle, the joint behavior of $(\{x\}, \{2x\}, \{3x\}, \ldots)$ carries a lot of information about $x$ (in fact, it determines $x$).

So the question is: can we choose $h_n$ to "decode" enough information about $x$ to make $\limsup h_n(\{nx\})$ non-constant?

Let me try a specific construction. Let $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ if $n$ is a power of 2, and $h_n(t) = 0$ otherwise. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/2\}$ for $n = 2^k$ and $f_n(x) = 0$ otherwise.

$\limsup f_n(x) = \limsup_{k \to \infty} \mathbf{1}_{\{2^k x\} < 1/2\}$.

Now, $\{2^k x\} < 1/2$ iff the $(k+1)$-th binary digit of $x$ is 0. For a.e. $x$ (with respect to Lebesgue measure, which corresponds to fair coin flips in binary), the binary digits are i.i.d. Bernoulli(1/2). So $\limsup_{k} \mathbf{1}_{\{2^k x\} < 1/2} = 1$ for a.e. $x$ (since there are infinitely many 0 digits). And $\liminf = 0$ for a.e. $x$ (since there are infinitely many 1 digits).

So $\limsup = 1$ and $\liminf = 0$, both constant a.e. Still constant.

But wait, $h_n$ for $n = 2^k$ is $1/2^k$-periodic? No, $h_n$ is 1-periodic (it's a function on $[0,1)$), and $f_n(x) = h_n(\{nx\})$ is $1/n$-periodic. So $f_{2^k}(x) = \mathbf{1}_{\{2^k x\} < 1/2}$ is $1/2^k$-periodic. ✓

But the issue is that I set $h_n = 0$ for $n$ not a power of 2, which means $f_n = 0$ for those $n$. The limsup is determined by the subsequence $n = 2^k$, and as I showed, it's constant a.e.

Let me try to make the limsup depend on $x$ more cleverly. What if I use the binary digits to construct a non-constant function?

Let $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for all $n$. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/2\}$. By equidistribution, for a.e. $x$, $\{nx\} < 1/2$ for infinitely many $n$ and $\{nx\} \geq 1/2$ for infinitely many $n$. So $\limsup = 1$ and $\liminf = 0$, constant a.e.

What if I use a "thinner" set? Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/n\}$. By Khintchine's theorem (or the theory of continued fractions), for a.e. $x$, $\{nx\} < 1/n$ infinitely often, so $\limsup = 1$. And $\liminf = 0$ since $f_n(x) = 0$ for most $n$. Constant a.e.

What if I make the set even thinner? $h_n(t) = \mathbf{1}_{[0, 1/n^2)}(t)$. Then $|E_n| = 1/n^2$ and $\sum 1/n^2 < \infty$. By Borel-Cantelli, for a.e. $x$, $f_n(x) = 1$ for only finitely many $n$. So $\limsup = 0$ a.e. Constant.

What about $h_n(t) = \mathbf{1}_{[0, 1/(n \log n))}(t)$? Then $\sum 1/(n \log n) = \infty$, so by Khintchine, $\limsup = 1$ a.e. Constant.

It seems hard to make the limsup non-constant using these "interval" constructions. The Borel-Cantelli lemma and Khintchine's theorem always give us a 0-1 behavior.

But what if I use non-interval sets? Let me try:

$h_n(t) = \mathbf{1}_{A_n}(t)$ where $A_n$ is a measurable subset of $[0,1)$ with $|A_n| = 1/2$, but $A_n$ is a "fat Cantor set" or some fractal set.

The question is whether $\{nx\} \in A_n$ infinitely often for a.e. $x$. Since $|A_n| = 1/2$ and $\sum 1/2 = \infty$, if there's a Borel-Cantelli type result that works for general measurable sets (not just intervals), then the limsup would be 1 a.e.

I believe such a result exists. Let me think about it.

**Theorem (Khintchine-type for general sets):** For any sequence of measurable sets $A_n \subset [0,1)$ with $\sum |A_n| = \infty$, the set $\{x \in [0,1) : \{nx\} \in A_n \text{ i.o.}\}$ has full measure.

Is this true? I don't think it's true in full generality. The Khintchine theorem typically requires the sets to be intervals (or at least "nice" sets). For general measurable sets, the behavior can be different.

Actually, wait. Let me think about a potential counterexample. Let $A_n = [0, 1/2)$ if $n$ is even and $A_n = [1/2, 1)$ if $n$ is odd. Then $\sum |A_n| = \infty$, and $\{nx\} \in A_n$ i.o. iff $\{nx\} < 1/2$ for infinitely many even $n$ and $\{nx\} \geq 1/2$ for infinitely many odd $n$. By equidistribution, both happen for a.e. $x$. So the limsup is 1 a.e.

What if $A_n$ "avoids" the values $\{nx\}$ takes? For example, can I choose $A_n$ such that $\{nx\} \notin A_n$ for all $n$ and for a positive measure set of $x$?

This would require $A_n$ to avoid $\{nx \mod 1 : x \in E\}$ for some positive measure set $E$. But $\{nx \mod 1 : x \in E\}$ has measure $|E|$ (since $x \mapsto \{nx\}$ preserves measure), so if $|A_n| + |E| > 1$, they must overlap. But if $|A_n|$ is small, they might not overlap.

Hmm, but I need $\{nx\} \notin A_n$ for ALL $n$, not just for some $n$. This is much harder to arrange.

Let me try a different approach to constructing a counterexample.

**Counterexample attempt using the binary expansion:**

Let $x \in [0,1)$ with binary expansion $x = 0.b_1 b_2 b_3 \ldots$. The map $x \mapsto \{2^k x\}$ gives $\{2^k x\} = 0.b_{k+1} b_{k+2} \ldots$.

Now, define $h_{2^k}(t) = b_k(x)$... wait, $h_n$ can't depend on $x$. $h_n$ is a fixed function.

Let me think differently. I want to construct $h_n$ such that $\limsup h_n(\{nx\})$ is not constant.

Consider $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n = 2^k$ and $h_n(t) = 0$ otherwise. As before, $\limsup f_n(x) = \limsup_k \mathbf{1}_{\{2^k x\} < 1/2} = 1$ a.e. (since binary digits contain infinitely many 0s a.s.).

What if I use a different subsequence? $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n = k!$ and $h_n = 0$ otherwise. Then $\limsup f_n(x) = \limsup_k \mathbf{1}_{\{k! x\} < 1/2}$.

Is $\{k! x\} < 1/2$ infinitely often for a.e. $x$? Since $k!$ grows super-exponentially, the sequence $\{k! x\}$ is "almost independent" (by a result on lacunary sequences). For lacunary sequences, the Borel-Cantelli lemma works as if the events were independent. So since $\sum 1/2 = \infty$, the limsup is 1 a.e.

What about a non-lacunary subsequence? $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for all $n$. Then $\limsup = 1$ a.e. by equidistribution.

It seems very hard to make the limsup non-constant. Let me try a radically different approach.

**Approach: Make $h_n$ "encode" the value of $x$ in a way that creates a non-constant limsup.**

The idea: for each $n$, $h_n$ is a function on $[0,1)$. The value $h_n(\{nx\})$ depends on $\{nx\}$, which is a "coarse-grained" version of $x$ (at resolution $1/n$). As $n$ increases, we get finer and finer information about $x$.

Can we choose $h_n$ such that $h_n(\{nx\})$ "converges" to some non-constant function of $x$?

For example, let $h_n(t) = \mathbf{1}_{[0, x_0)}(t)$ for some fixed $x_0 \in (0,1)$. Then $f_n(x) = \mathbf{1}_{\{nx\} < x_0\}$. By equidistribution, for a.e. $x$, $\limsup f_n(x) = 1$ and $\liminf f_n(x) = 0$ (since $\{nx\}$ visits $[0, x_0)$ infinitely often and $[x_0, 1)$ infinitely often). So the limsup is constant.

What if $h_n$ "converges" to a function as $n \to \infty$? Say $h_n(t) = g(t)$ for all $n$, where $g$ is some fixed function. Then $f_n(x) = g(\{nx\})$, and by equidistribution, $\limsup f_n(x) = \text{ess sup } g$ and $\liminf f_n(x) = \text{ess inf } g$ for a.e. $x$. Constant.

What if $h_n$ converges to $g$ in some sense? Say $h_n \to g$ in $L^1$. Then $a_n \to \int g$. But the pointwise limsup of $h_n(\{nx\})$ is not directly related to $g(\{nx\})$ because the "equidistribution" and the "convergence" are happening at different rates.

Hmm, let me think about this more carefully.

Actually, I think the answer to Part 2 is YES (limsup and liminf are constant a.e.), and the proof uses a clever argument. Let me try to find the right approach.

**Key Insight: The "density" argument.**

For any $\epsilon > 0$ and any $a \in \mathbb{R}$, define:
$E_n^+ = \{x : f_n(x) > a + \epsilon\}$ and $E_n^- = \{x : f_n(x) < a - \epsilon\}$.

We have $|E_n^+| = |\{t : h_n(t) > a + \epsilon\}|$ and $|E_n^-| = |\{t : h_n(t) < a - \epsilon\}|$.

Now, suppose $L := \limsup_n \text{ess sup}_{t} h_n(t)$ (the limsup of the essential suprema). I claim that $\limsup f_n(x) = L$ for a.e. $x$.

Hmm, but this might not be true either. Let me think about what the right "constant" is.

Actually, let me consider a specific example. Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $\text{ess sup } h_n = 1$ for all $n$, so $L = 1$. And we showed $\limsup f_n(x) = 1$ a.e. ✓

Let $h_n(t) = 1 - 1/n$ for all $t$. Then $f_n(x) = 1 - 1/n$, and $\limsup f_n(x) = 1$. And $L = \limsup (1 - 1/n) = 1$. ✓

Let $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n$ odd and $h_n(t) = 0$ for $n$ even. Then $\text{ess sup } h_n = 1$ for $n$ odd, $0$ for $n$ even. $L = 1$. And $\limsup f_n(x) = \limsup_{\text{odd } n} \mathbf{1}_{\{nx\} < 1/2} = 1$ a.e. (by equidistribution on the odd subsequence). ✓

Hmm, what if $\text{ess sup } h_n \to 0$? Let $h_n(t) = 1/n$. Then $f_n(x) = 1/n \to 0$. $\limsup = 0$. And $L = \limsup 1/n = 0$. ✓

What if $\text{ess sup } h_n$ oscillates? $h_n(t) = 1$ for $n$ in a sparse set $S$ and $h_n(t) = 0$ for $n \notin S$. Then $L = 1$ (if $S$ is infinite). And $\limsup f_n(x) = 1$ iff $f_n(x) = 1$ for infinitely many $n \in S$, which happens iff $x \in \bigcup_{n \in S} [0,1)$... well, $f_n(x) = 1$ for all $x$ when $n \in S$, so $\limsup = 1$ for all $x$. ✓

OK so in all these examples, $\limsup f_n(x) = \limsup_n \text{ess sup } h_n$ a.e. Is this always true?

Let me check: $h_n(t) = \mathbf{1}_{[0, 1/n^2)}(t)$. Then $\text{ess sup } h_n = 1$ for all $n$, so $L = 1$. But $|E_n| = 1/n^2$ and $\sum 1/n^2 < \infty$, so by Borel-Cantelli, $f_n(x) = 1$ for only finitely many $n$, a.e. So $\limsup f_n(x) = 0 \neq 1 = L$.

So the conjecture $\limsup f_n = \limsup \text{ess sup } h_n$ is FALSE.

The issue is that even though $\text{ess sup } h_n = 1$, the set where $h_n$ is close to 1 has small measure, and the Borel-Cantelli lemma kicks in.

So what IS the right constant? Let me think about this more carefully.

For $h_n(t) = \mathbf{1}_{[0, 1/n^2)}(t)$: $\limsup f_n(x) = 0$ a.e. The "right" constant is 0.

For $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$: $\limsup f_n(x) = 1$ a.e. (by Khintchine). The "right" constant is 1.

The difference is $\sum |A_n|$: $< \infty$ in the first case, $= \infty$ in the second.

So the constant depends on whether $\sum |A_n|$ converges or diverges. But this is specific to indicator functions of intervals. For general $h_n$, the situation is more complex.

Let me think about the general case. For any $a \in \mathbb{R}$ and $\epsilon > 0$:

$\{x : \limsup f_n(x) > a + \epsilon\} \subseteq \limsup_n \{x : f_n(x) > a + \epsilon\}$.

$|\{x : f_n(x) > a + \epsilon\}| = |\{t : h_n(t) > a + \epsilon\}| =: \alpha_n(a + \epsilon)$.

If $\sum_n \alpha_n(a + \epsilon) < \infty$, then $|\limsup_n \{x : f_n(x) > a + \epsilon\}| = 0$ by Borel-Cantelli, so $\limsup f_n(x) \leq a + \epsilon$ a.e.

Conversely, if $\sum_n \alpha_n(a + \epsilon) = \infty$, does $\limsup f_n(x) \geq a + \epsilon$ a.e.?

This is the "converse Borel-Cantelli" question, and it requires some independence or quasi-independence.

For the sequence $\{nx\}$, there's a result (I think due to various people, maybe related to the Duffin-Schaeffer conjecture or the Khintchine theorem) that gives a converse Borel-Cantelli for intervals. But for general measurable sets, it might not hold.

Hmm, let me think about whether the converse can fail for general measurable sets.

**Potential counterexample for the converse:**

Let $A_n \subset [0,1)$ be measurable with $|A_n| = 1/2$ for all $n$, but chosen so that $\{nx\} \in A_n$ for only finitely many $n$ for a positive measure set of $x$.

Can we do this? We need to find $A_n$ with $|A_n| = 1/2$ such that $\bigcap_N \bigcup_{n \geq N} \{x : \{nx\} \in A_n\}$ has measure $< 1$.

This is equivalent to: $\bigcup_N \bigcap_{n \geq N} \{x : \{nx\} \notin A_n\}$ has measure $> 0$.

I.e., there's a positive measure set of $x$ such that $\{nx\} \notin A_n$ for all large $n$.

Can we find such $A_n$? Let me try.

Let $A_n = [0, 1/2) \setminus \{nx \mod 1 : x \in [0, 1/4)\}$... no, this doesn't make sense because $A_n$ can't depend on $x$.

Let me try a different approach. For each $n$, the set $\{x : \{nx\} \in A_n\}$ has measure $|A_n| = 1/2$. The question is whether we can make these sets "align" so that their limsup has measure $< 1$.

Consider $A_n = [1/2, 1)$ for all $n$. Then $\{x : \{nx\} \in A_n\} = \{x : \{nx\} \geq 1/2\}$, which has measure 1/2. The limsup is $\{x : \{nx\} \geq 1/2 \text{ i.o.}\}$, which has measure 1 by equidistribution.

What if $A_n$ "avoids" $\{nx\}$ for $x$ in some set? For example, let $E = [0, 1/4)$ and define $A_n = [0,1) \setminus \{\{nx\} : x \in E\}$. But $\{\{nx\} : x \in E\}$ has measure $|E| = 1/4$ (since $x \mapsto \{nx\}$ preserves measure), so $|A_n| \geq 3/4 > 1/2$. We could take a subset of measure 1/2.

But even so, for $x \in E$, $\{nx\} \in \{\{ny\} : y \in E\}$, which is the set we're trying to avoid. So $\{nx\} \notin A_n$ for $x \in E$... but $A_n$ is a subset of $[0,1) \setminus \{\{ny\} : y \in E\}$, so $\{nx\} \notin A_n$ for $x \in E$. This means $f_n(x) = 0$ for all $n$ and all $x \in E$!

Wait, but $A_n$ depends on $n$ and on $E$, and $E$ is fixed. Let me be more precise.

For each $n$, let $B_n = \{\{nx\} : x \in E\} = \{nx \mod 1 : x \in [0, 1/4)\}$. This is a set of measure 1/4 (since $x \mapsto \{nx\}$ is measure-preserving). Let $A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$. (This is possible since $|[0,1) \setminus B_n| = 3/4 > 1/2$.)

Then for $x \in E$, $\{nx\} \in B_n$, so $\{nx\} \notin A_n$, so $f_n(x) = 0$ for all $n$. Thus $\limsup f_n(x) = 0$ for $x \in E$.

For $x \notin E$, $\{nx\}$ might or might not be in $A_n$. The limsup for $x \notin E$ could be 1 (if $\{nx\} \in A_n$ i.o. for a.e. $x \notin E$).

So $\limsup f_n(x) = 0$ on $E$ (measure 1/4) and possibly 1 on $[0,1) \setminus E$ (measure 3/4). This would be a non-constant limsup!

Wait, but I need to check that $\limsup f_n(x) = 1$ for a.e. $x \notin E$. Is this true?

For $x \notin E$, $\{nx\} \notin B_n$ doesn't mean $\{nx\} \in A_n$ (since $A_n$ is a proper subset of $[0,1) \setminus B_n$). So we need $\{nx\} \in A_n$ i.o.

$|A_n| = 1/2$ and $\sum 1/2 = \infty$. If the events $\{x : \{nx\} \in A_n\}$ are "quasi-independent" for $x \notin E$, then by converse Borel-Cantelli, $\limsup = 1$ a.e. on $[0,1) \setminus E$.

But are they quasi-independent? This depends on the specific choice of $A_n$.

Hmm, but even if the limsup is not exactly 1 on $[0,1) \setminus E$, the key point is that it's different from 0 (which is the value on $E$). So the limsup would be non-constant.

Wait, but I need to be more careful. Let me re-examine the construction.

$E = [0, 1/4)$. For each $n$, $B_n = \{nx \mod 1 : x \in [0, 1/4)\}$. 

$B_n$ is the image of $[0, 1/4)$ under $x \mapsto \{nx\}$. Since $x \mapsto \{nx\}$ is $n$-to-1 and measure-preserving, $B_n$ is a union of $n$ intervals, each of length $1/(4n)$, and $|B_n| = 1/4$.

Specifically, $B_n = \bigcup_{k=0}^{n-1} [k/n, k/n + 1/(4n))$.

$A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$. For example, $A_n = [1/4, 3/4) \setminus B_n$... hmm, this might not have measure exactly 1/2. Let me just say $A_n$ is any measurable subset of $[0,1) \setminus B_n$ with $|A_n| = 1/2$.

Now, for $x \in E = [0, 1/4)$: $\{nx\} \in B_n$ (by definition of $B_n$), so $\{nx\} \notin A_n$, so $f_n(x) = 0$ for all $n$. Thus $\limsup f_n(x) = 0$.

For $x \notin E$: we need to check whether $\{nx\} \in A_n$ infinitely often. Since $|A_n| = 1/2$ and $\sum 1/2 = \infty$, if there's a converse Borel-Cantelli, then $\limsup f_n(x) = 1$ for a.e. $x \notin E$.

But even without the converse Borel-Cantelli, the key point is that $\limsup f_n(x) \geq 0$ for all $x$ (since $f_n \geq 0$), and $\limsup f_n(x) = 0$ on $E$ (measure 1/4). If $\limsup f_n(x) > 0$ on a positive measure subset of $[0,1) \setminus E$, then the limsup is non-constant.

Actually, we can make this even simpler. Let $h_n(t) = \mathbf{1}_{A_n}(t)$ where $A_n = [1/4, 3/4)$ for all $n$. Then $f_n(x) = \mathbf{1}_{\{nx\} \in [1/4, 3/4)}$.

For $x \in [0, 1/4)$: $\{nx\} \in [0, 1/4) \cup \ldots$ — actually, $\{nx\}$ for $x \in [0, 1/4)$ ranges over $[0, 1/4)$ (when $nx < 1/4$, i.e., $x < 1/(4n)$) and other intervals. By equidistribution, for a.e. $x \in [0, 1/4)$, $\{nx\}$ is equidistributed in $[0,1)$, so $\{nx\} \in [1/4, 3/4)$ with frequency $1/2$. So $\limsup f_n(x) = 1$ for a.e. $x \in [0, 1/4)$.

So this doesn't work — the limsup is still 1 everywhere.

The issue is that for a.e. $x \in E$, $\{nx\}$ is equidistributed in $[0,1)$, not confined to $B_n$. The set $B_n$ depends on $n$, and for a fixed $x$, $\{nx\}$ doesn't stay in $B_n$.

Wait, I think I made an error. Let me re-examine.

$B_n = \{\{ny\} : y \in E\}$. For a fixed $x \in E$, $\{nx\}$ is a specific value, and it's in $B_n$ by definition (since $x \in E$, $\{nx\} = \{ny\}$ for $y = x$). So $\{nx\} \in B_n$ for all $n$ and all $x \in E$.

But $A_n \subset [0,1) \setminus B_n$, so $\{nx\} \notin A_n$ for all $n$ and all $x \in E$. So $f_n(x) = 0$ for all $n$ and all $x \in E$. ✓

Now, for $x \notin E$: $\{nx\}$ might or might not be in $A_n$. The question is whether $\{nx\} \in A_n$ for infinitely many $n$.

The set $\{x : \{nx\} \in A_n\}$ has measure $|A_n| = 1/2$. But for $x \in E$, this set is empty (since $\{nx\} \in B_n$ and $A_n \cap B_n = \emptyset$). So the set $\{x : \{nx\} \in A_n\}$ is contained in $[0,1) \setminus E$, and has measure 1/2. Since $|[0,1) \setminus E| = 3/4$, the conditional probability (given $x \notin E$) is $(1/2)/(3/4) = 2/3$.

Now, $\sum_{n} |\{x \notin E : \{nx\} \in A_n\}| = \sum 1/2 = \infty$. If the converse Borel-Cantelli holds (with quasi-independence), then $\limsup f_n(x) = 1$ for a.e. $x \notin E$.

But does the converse Borel-Cantelli hold here? The sets $A_n$ are somewhat arbitrary (just subsets of $[0,1) \setminus B_n$ with measure 1/2), so the quasi-independence might fail.

However, even if the converse Borel-Cantelli fails, we might still have $\limsup f_n(x) > 0$ for some $x \notin E$, which would make the limsup non-constant.

Actually, let me think about this more carefully. For $x \notin E$, is it possible that $\{nx\} \notin A_n$ for all large $n$? This would require $\{nx\} \in B_n \cup ([0,1) \setminus (A_n \cup B_n))$ for all large $n$. Since $|A_n| = 1/2$ and $|B_n| = 1/4$, $|[0,1) \setminus (A_n \cup B_n)| = 1/4$. So the "avoidance" set has measure 1/4 + 1/4 = 1/2 for each $n$. If $\sum 1/2 = \infty$ and the events are quasi-independent, then $\{nx\}$ is in the avoidance set infinitely often, but also in $A_n$ infinitely often.

I think for "generic" choices of $A_n$, the converse Borel-Cantelli would hold and $\limsup = 1$ a.e. on $[0,1) \setminus E$. But I'm not sure how to prove this in general.

Let me try to make the counterexample more explicit. Let me choose $A_n$ specifically.

Let $E = [0, 1/4)$. For each $n$, $B_n = \bigcup_{k=0}^{n-1} [k/n, k/n + 1/(4n))$.

Let $A_n = [1/2, 1) \setminus B_n$. Then $|A_n| = |[1/2, 1)| - |B_n \cap [1/2, 1)|$. 

$B_n \cap [1/2, 1)$: The intervals $[k/n, k/n + 1/(4n))$ that intersect $[1/2, 1)$. There are about $n/2$ such intervals, each contributing $1/(4n)$, so $|B_n \cap [1/2, 1)| \approx 1/8$. So $|A_n| \approx 1/2 - 1/8 = 3/8$. Not exactly 1/2, but close enough for our purposes.

Actually, let me simplify. Let $A_n = [3/4, 1)$. Then $|A_n| = 1/4$ and $A_n \cap B_n = \emptyset$ iff $B_n \cap [3/4, 1) = \emptyset$. But $B_n$ contains intervals near $3/4$ (specifically, $[k/n, k/n + 1/(4n))$ for $k$ near $3n/4$), so $B_n \cap [3/4, 1) \neq \emptyset$ in general.

This is getting complicated. Let me just use the abstract construction: $A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$.

The key point is: for $x \in E$, $f_n(x) = 0$ for all $n$, so $\limsup = 0$. For $x \notin E$, $\limsup \geq 0$ and potentially $> 0$. So the limsup is not constant (it's 0 on $E$ and possibly positive elsewhere).

But wait, I need to verify that $\limsup f_n(x) > 0$ for at least some $x \notin E$ (on a set of positive measure). Otherwise, the limsup could be 0 everywhere, which is still constant.

For $x \notin E$, $f_n(x) = \mathbf{1}_{\{nx\} \in A_n}$. The expected value of $f_n(x)$ (over $x \notin E$) is $|A_n| / |[0,1) \setminus E| = (1/2) / (3/4) = 2/3$. So on average, $f_n(x) = 1$ about 2/3 of the time. This suggests that $\limsup f_n(x) = 1$ for a.e. $x \notin E$.

But can we prove this? The issue is the lack of independence. However, I think we can use the following argument:

For $x \notin E$, consider the sequence $\{nx\}$. This sequence is equidistributed in $[0,1)$ for a.e. $x$. But $A_n$ changes with $n$, so equidistribution alone doesn't suffice.

However, we can use the following: for any fixed interval $I \subset [0,1)$, $|\{x \notin E : \{nx\} \in I\}| \to |I| \cdot |[0,1) \setminus E|$ as $n \to \infty$ (by equidistribution). If $A_n$ contains a fixed interval $I$ for infinitely many $n$, then $\{nx\} \in I \subset A_n$ for infinitely many $n$ (for a.e. $x$), giving $\limsup \geq 1$.

But $A_n$ might not contain any fixed interval. Since $A_n \subset [0,1) \setminus B_n$ and $B_n$ becomes "dense" as $n \to \infty$ (it's a union of $n$ intervals of length $1/(4n)$, covering $1/4$ of $[0,1)$), $A_n$ could be a "fractured" set.

Hmm, but $A_n$ has measure 1/2, and it's contained in $[0,1) \setminus B_n$ which has measure 3/4. So $A_n$ is a "large" subset of $[0,1) \setminus B_n$.

I think for "most" choices of $A_n$, the limsup would be 1 a.e. on $[0,1) \setminus E$. But I'm not sure how to prove this rigorously.

Let me try a different, cleaner counterexample.

**Cleaner counterexample:**

Let $E \subset [0,1)$ be a measurable set with $0 < |E| < 1$. For each $n$, define $h_n(t) = \mathbf{1}_{[0,1) \setminus E}(\{nt\})$... no, this is circular.

Let me think about this differently. I want $f_n(x) = 0$ for $x \in E$ and $f_n(x) = 1$ for $x \notin E$ (at least for infinitely many $n$).

$f_n(x) = h_n(\{nx\})$. For $x \in E$, I want $h_n(\{nx\}) = 0$, i.e., $\{nx\} \notin A_n$ where $A_n = h_n^{-1}(1)$. This means $B_n := \{\{nx\} : x \in E\} \subset [0,1) \setminus A_n$.

So I need $A_n \subset [0,1) \setminus B_n$ where $B_n = \{\{nx\} : x \in E\}$, $|B_n| = |E|$.

If $|E| < 1/2$, then $|[0,1) \setminus B_n| = 1 - |E| > 1/2$, so I can choose $A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$.

Then for $x \in E$: $f_n(x) = 0$ for all $n$, so $\limsup = 0$.
For $x \notin E$: $f_n(x) = \mathbf{1}_{\{nx\} \in A_n}$, and $|\{x \notin E : \{nx\} \in A_n\}| = |A_n| = 1/2$ (since $\{x : \{nx\} \in A_n\} \subset [0,1) \setminus E$ because $A_n \cap B_n = \emptyset$).

Now, $\sum_n |\{x \notin E : f_n(x) = 1\}| = \sum 1/2 = \infty$.

If the converse Borel-Cantelli holds (even in a weak form), then $\limsup f_n(x) = 1$ for a.e. $x \notin E$, and the limsup is non-constant (0 on $E$, 1 on $[0,1) \setminus E$).

But does the converse Borel-Cantelli hold? The sets $\{x : \{nx\} \in A_n\}$ are not independent, but they might be "quasi-independent" enough.

Actually, I realize that the converse Borel-Cantelli might NOT hold for arbitrary measurable sets $A_n$. The sets $A_n$ could be chosen adversarially to make the limsup as small as possible.

In fact, let me think about whether we can make $\limsup f_n(x) = 0$ for ALL $x$ (not just $x \in E$). This would require $\{nx\} \notin A_n$ for all large $n$ and all $x$. But $|\{x : \{nx\} \in A_n\}| = 1/2$ for each $n$, so $\bigcup_{n \geq N} \{x : \{nx\} \in A_n\}$ has measure $\geq 1/2$ for each $N$. So $\limsup \{x : \{nx\} \in A_n\}$ has measure $\geq 1/2$... no, that's not right. The measure of the union could be less than the sum.

Actually, $\limsup_n \{x : \{nx\} \in A_n\}$ has measure $\geq \limsup_n |\{x : \{nx\} \in A_n\}| = 1/2$... no, that's not right either. The measure of the limsup of sets is not bounded below by the limsup of measures.

By Fatou's lemma: $|\limsup E_n| \geq \limsup |E_n|$ is NOT true in general. Actually, $|\liminf E_n| \leq \liminf |E_n|$ and        — AI历史解题过程（thinking）
#   oda_math_460k_00055314         — 题目ID

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
  <problem_id>oda_math_460k_00055314</problem_id>
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

Annie has 24 letter tiles in a bag; 8 C’s, 8 M’s, and 8 W’s. She blindly draws tiles from the bag until she has enough to spell “CMWMC.” What is the maximum number of tiles she may have to draw?

## Standard Solution

<think>Okay, let's try to figure out this problem. The question is about Annie drawing letter tiles from a bag with 8 C's, 8 M's, and 8 W's. She needs to spell "CMWMC", and we need to find the maximum number of tiles she might have to draw to get enough to spell that word. 

First, let's figure out what letters are needed for "CMWMC". Let's spell it out: C, M, W, M, C. So that's 2 C's, 2 M's, and 1 W. So the required counts are: C:2, M:2, W:1. 

Now, the problem is asking for the maximum number of tiles she might have to draw. To maximize the number of draws, we need to consider the worst-case scenario where she draws as many tiles as possible without getting the required number of each letter, and then the next tile will give her the last one needed. 

Let's break it down by each letter. Let's think about the letters she might draw before getting the necessary ones. 

First, let's list the required letters and their counts:
- C needed: 2
- M needed: 2
- W needed: 1

To maximize the number of draws, we want to consider the scenario where she draws as many of the other letters as possible, but also not getting enough of the required ones until the last possible moment.

Wait, but all the letters are C, M, W. So there are no other letters. So the worst case is that she draws as many tiles as possible without having the required number of each needed letter, and then the next tile gives her the last one needed.

Let's think about each required letter and how many of the others she might have drawn.

First, let's see what's the maximum number of tiles she can have without having enough C's, M's, or W's. Wait, but she needs all three. So she needs at least 2 C's, 2 M's, and 1 W. So the worst case is that she has almost enough of some, but not all, and then the last tile gives the missing one.

Wait, maybe we need to consider the maximum number of tiles she could have drawn without having the exact counts needed, but then the next tile would make it possible. Let's think step by step.

Let's first note the required counts:

Total required: 2 C, 2 M, 1 W. Total letters needed: 5.

But the question is about the maximum number of tiles she may have to draw. So we need to imagine the worst possible sequence of draws where she has to draw as many as possible before getting the necessary tiles.

To maximize the number of draws, we need to consider the scenario where she draws as many tiles as possible that are not contributing to the required counts, but also not getting the required counts. Wait, but all tiles are C, M, W. So maybe she's drawing a lot of the letters that are needed but not enough, and also maybe some of the others.

Wait, let's think: What's the maximum number of tiles she can have without having 2 C's, 2 M's, and 1 W? Then the next tile would give her the last one needed.

But actually, she needs all three. So she needs to have at least 2 C's, at least 2 M's, and at least 1 W. So the worst case is that she has as many tiles as possible, but missing one of these conditions, and then the next tile gives her the missing one.

But maybe she's missing more than one condition. Let's see.

Let's consider the possible "deficiencies":

1. Not enough C's (i.e., less than 2 C's)
2. Not enough M's (i.e., less than 2 M's)
3. Not enough W's (i.e., less than 1 W)

We need to find the maximum number of tiles where at least one of these deficiencies exists, and then the next tile will resolve all deficiencies.

But to maximize the total, we need to maximize the number of tiles drawn while still having at least one deficiency, and then the next tile fixes it.

But perhaps the worst case is when she has the maximum number of tiles where she is missing the least critical deficiency. Let's think.

First, let's see what's the maximum number of tiles she can have without having 2 C's. That would be if she has 1 C, and as many M's and W's as possible. But wait, but she might already have enough M's and W's. But if she's missing C's, then even if she has enough M's and W's, she still can't spell the word. So the maximum tiles without 2 C's: 1 C + all M's + all W's. But wait, there are 8 M's and 8 W's. So 1 + 8 + 8 = 17. But wait, but if she has 1 C, 8 M's, 8 W's, that's 17 tiles. But in this case, she has 8 M's (which is more than needed 2), 8 W's (more than needed 1), but only 1 C (needs 2). So she can't spell the word yet. Then the next tile must be a C, since all other tiles are already drawn (since there are 8 C's total, and she has 1, so 7 left). Wait, no. Wait, total tiles are 24. If she has 1 C, 8 M, 8 W, that's 17 tiles. There are 24 - 17 = 7 tiles left, which are all C's (since 8 total C's, 1 drawn, 7 left). So the next tile she draws is a C, making her total C's 2. Now she has 2 C's, 8 M's, 8 W's. Now she has enough: 2 C, 2 M, 1 W. So total tiles drawn: 17 + 1 = 18. But wait, but maybe there's a worse case.

Alternatively, what if she's missing M's? Let's see. Maximum tiles without 2 M's: 1 M, and as many C's and W's as possible. So 1 M + 8 C's + 8 W's = 1 + 8 + 8 = 17. Then next tile is M, making M's 2. Total tiles: 17 + 1 = 18. Same as before.

What if she's missing W's? Maximum tiles without 1 W: 0 W's, and as many C's and M's as possible. So 0 W + 8 C's + 8 M's = 16. Then next tile is W, total tiles: 16 + 1 = 17. That's less than 18, so not the maximum.

But wait, maybe there's a scenario where she's missing more than one deficiency. For example, she has less than 2 C's and less than 2 M's. Let's see. Let's say she has 1 C and 1 M. Then how many W's can she have? Let's see. To maximize the total, she would have as many W's as possible. But W's are 8. So 1 C + 1 M + 8 W = 10. Then she's missing 1 C, 1 M, but has enough W's. But this is way less than 17, so not the maximum.

Alternatively, maybe she's missing 2 C's and has enough M's and W's. Wait, but if she has enough M's and W's, but not enough C's, that's the first case. Similarly, if she has enough C's and W's but not enough M's, that's the second case.

But maybe there's a case where she has more than the required of some letters but not enough of others, but the total is higher. Let's think again.

Wait, the required is 2 C, 2 M, 1 W. Let's think about the worst case where she has the maximum number of tiles, but still doesn't have the required counts. Then the next tile will give her the last needed.

But to maximize the number of tiles, we need to consider the scenario where she has the maximum possible tiles without having all the required counts. Let's see:

What's the maximum number of tiles she can have without having 2 C's, OR without having 2 M's, OR without having 1 W. Because as long as any of these is missing, she can't spell the word. So the worst case is the maximum among the three possibilities:

1. Max tiles without 2 C's: 1 C + all M's + all W's = 1 + 8 + 8 = 17. At this point, she has 1 C, 8 M, 8 W. She needs 1 more C. The next tile must be a C (since all other tiles are already drawn: 8 M and 8 W are all drawn, so remaining tiles are 8 - 1 = 7 C's). So next tile is C, total 18.

2. Max tiles without 2 M's: 1 M + all C's + all W's = 1 + 8 + 8 = 17. Then next tile is M, total 18.

3. Max tiles without 1 W: 0 W + all C's + all M's = 0 + 8 + 8 = 16. Next tile is W, total 17.

But wait, but maybe there's a scenario where she has more than 17 tiles but still can't form the word. Let's check. Suppose she has 2 C's, but only 1 M, and 8 W's. Let's see: 2 C + 1 M + 8 W = 11. That's less than 17, so not worse.

Alternatively, 2 C's, 2 M's, but 0 W's. Then she has 2+2+0=4 tiles. Then she needs a W. But that's way less than 17.

Wait, but what if she has 2 C's, 1 M, and 8 W's. That's 2+1+8=11. Still less than 17.

Alternatively, 1 C, 2 M's, 8 W's. 1+2+8=11. Still less.

Alternatively, 1 C, 8 M's, 7 W's. Then total tiles: 1+8+7=16. But she has 1 C (needs 2), 8 M (enough), 7 W (enough). So she's missing 1 C. But this is 16 tiles, which is less than 17.

Wait, the maximum when missing C's is 1 C + 8 M + 8 W = 17. Because if she has 1 C, and all M's and W's, that's the maximum possible without having 2 C's. Because if she has more than 1 C, then she's not missing C's anymore. So 1 C is the max for missing C's.

Similarly, missing M's: 1 M + 8 C + 8 W = 17.

Missing W's: 0 W + 8 C + 8 M = 16.

But wait, what if she's missing both C's and M's? For example, 1 C, 1 M, 8 W. That's 10 tiles. But that's less than 17, so not the maximum.

Alternatively, 1 C, 1 M, 8 W: 10 tiles. But she's missing 1 C and 1 M. But the maximum tiles in this case is 1+1+8=10, which is less than 17. So the worst case is when she's missing only one of the required letters, and that's either C or M, leading to 17 tiles drawn, then the next tile (18th) gives the needed C or M.

But wait, let's confirm. Let's take the first case: she's drawing tiles, and the first 17 tiles are 1 C, 8 M's, 8 W's. Then she has 1 C, which is not enough (needs 2). The next tile must be a C (since all M's and W's are already drawn: 8 M's and 8 W's are all in the 17 tiles, so remaining tiles are 8 C's - 1 C = 7 C's). So the 18th tile is a C, making her total C's 2. Now she has 2 C's, 8 M's, 8 W's. Now she has all required: 2 C, 2 M, 1 W. So she can spell the word. So total tiles drawn: 18.

But wait, is there a scenario where she has to draw more than 18? Let's see.

Suppose she's missing M's. Let's say she has 8 C's, 1 M, 8 W's. That's 8+1+8=17 tiles. Then the next tile is a M (since all C's and W's are already drawn: 8 C's and 8 W's, so remaining tiles are 8 M's -1 M=7 M's). So 18th tile is M, now she has 8 C, 2 M, 8 W. Now she has 2 C (needs 2), 2 M (needs 2), 1 W (needs 1). So she can spell the word. Total tiles: 18.

What if she's missing W's? She has 8 C, 8 M, 0 W. That's 16 tiles. Next tile is W (since remaining tiles are 8 W's). 17th tile is W. Now she has 8 C, 8 M, 1 W. Now she has 2 C, 2 M, 1 W. So she can spell the word. Total tiles: 17. So that's less than 18.

Is there a scenario where she has to draw more than 18? Let's think.

Wait, maybe she's not just missing one letter, but has some of the required letters but not enough, but also has some excess. Wait, but the maximum number of tiles without having the required counts would be when she has the maximum possible tiles but still missing at least one required count.

Wait, let's think differently. Let's consider the worst case where she draws as many tiles as possible that are not contributing to the required counts, but also not getting enough of the required ones. But since all tiles are required letters, maybe the worst case is when she has the maximum number of tiles that don't include enough of the least required letters.

Wait, the required letters are 2 C, 2 M, 1 W. The W is needed only once, but there are 8 W's. So maybe the worst case is when she draws a lot of W's, but not enough C's or M's.

Wait, but earlier calculation shows that the maximum when missing C's is 17, which includes 8 W's. So that's already considered.

Alternatively, what if she has 2 C's, but only 1 M, and 8 W's. Let's see: 2 C + 1 M + 8 W = 11. Then she's missing 1 M. But she has 11 tiles. The remaining tiles are 8 M's -1 M =7 M's, and 8 W's -8 W's=0 W's, 8 C's -2 C's=6 C's. So next tile could be M, C, or M. Wait, but she needs 1 more M. But the total tiles here is 11, which is way less than 17, so not the maximum.

Alternatively, what if she has 2 C's, 2 M's, but 0 W's. Then she has 4 tiles. She needs 1 W. The remaining tiles are 8 W's, 6 C's, 6 M's. Next tile is W, total 5. But that's way less than 18.

Alternatively, what if she has 3 C's, 1 M, 8 W's. That's 3+1+8=12. She's missing 1 M. But again, total tiles 12 <17.

Alternatively, 1 C, 3 M, 8 W's. 1+3+8=12. Missing 1 C. Still less than 17.

So the maximum seems to be 18. But let's confirm.

Wait, let's think about the total number of tiles. There are 24 tiles. Let's see, what's the minimum number of tiles needed to guarantee that she has the required letters. But the question is the maximum number she may have to draw, which is the worst-case scenario, i.e., the maximum possible number of tiles she could draw before getting the necessary ones.

Wait, another approach: To spell "CMWMC", she needs 2 C, 2 M, 1 W. Let's think about the worst case where she draws as many tiles as possible without having the required counts, then the next tile gives her the last one needed.

The worst case is when she has the maximum number of tiles that do not contain the required number of each letter. Let's calculate the maximum number of tiles that do not have enough C's, or not enough M's, or not enough W's.

But to maximize, we need the maximum of the three possibilities:

1. Tiles with <2 C's: maximum possible is (1 C) + all M's + all W's = 1 +8+8=17. Because if she has 1 C, and all 8 M's and 8 W's, that's 17 tiles, and she still needs 1 more C.

2. Tiles with <2 M's: maximum possible is (1 M) + all C's + all W's =1+8+8=17. Needs 1 more M.

3. Tiles with <1 W's: maximum possible is (0 W) + all C's + all M's=0+8+8=16. Needs 1 W.

So the maximum among these is 17. Then the next tile (18th) will give her the needed C or M, making the total 18.

Is there a scenario where she has more than 17 tiles but still can't form the word? Let's see. Suppose she has 2 C's, 1 M, and 8 W's. That's 2+1+8=11. But that's less than 17. What if she has 2 C's, 2 M's, and 7 W's. That's 2+2+7=11. Still less.

Alternatively, 3 C's, 1 M, 8 W's: 3+1+8=12. Still less than 17.

Alternatively, 1 C, 2 M's, 8 W's: 1+2+8=11. Still less.

Alternatively, 1 C, 8 M's, 7 W's: 1+8+7=16. That's less than 17. Because she has 1 C (needs 2), 8 M (enough), 7 W (enough). But she's missing 1 C, but the total tiles here is 16, which is less than 17. So the maximum when missing C's is indeed 17 (1 C, 8 M, 8 W).

Similarly, 8 C's, 1 M, 8 W's: 8+1+8=17. Missing 1 M.

So in both cases, the maximum tiles without having the required counts is 17. Then the next tile (18th) will be the needed one (C or M), making the total 18.

Is there a case where she has 17 tiles but still can't form the word, but the 18th tile isn't the needed one? No, because in the scenario where she has 1 C, 8 M, 8 W (17 tiles), the remaining tiles are all C's (since 8 C's total, 1 drawn, 7 left). So the next tile must be a C, which gives her 2 C's, making the total 18. Similarly, if she has 8 C, 1 M, 8 W (17 tiles), remaining tiles are M's, so next tile is M, total 18.

Wait, but what if she's in a scenario where she has some of the required letters but not enough, but also has some of the others. For example, suppose she has 1 C, 7 M's, 8 W's. That's 1+7+8=16 tiles. She's missing 1 C and 1 M. But this is less than 17, so not the maximum.

Alternatively, 1 C, 8 M's, 7 W's: 1+8+7=16. Still missing 1 C, but total tiles 16 <17.

So the maximum number of tiles she might have to draw is 18. Let's confirm with another angle.

Total required letters: 2 C, 2 M, 1 W. Let's think of the worst case where she draws all the letters that are not needed in excess, but not enough of the needed ones.

Wait, but all letters are needed. So the worst case is when she has the maximum number of letters that don't include the required counts. As we calculated, that's 17, then the next one is needed. So 18.

Yes, that makes sense. So the answer is 18.
</think>

To determine the maximum number of tiles Annie may have to draw to spell "CMWMC", we first identify the required letters and their counts: 2 C's, 2 M's, and 1 W. 

To find the worst-case scenario, we consider the maximum number of tiles she could draw without having enough of each required letter, then add one more tile to ensure she has the necessary counts.

### Key Analysis:
1. **Required Letters**: 2 C's, 2 M's, 1 W.
2. **Worst-Case Scenarios**:
   - **Missing 2 C's**: If Annie has only 1 C, but all 8 M's and 8 W's, she has \(1 + 8 + 8 = 17\) tiles. She needs 1 more C.
   - **Missing 2 M's**: If Annie has only 1 M, but all 8 C's and 8 W's, she has \(1 + 8 + 8 = 17\) tiles. She needs 1 more M.
   - **Missing 1 W**: If Annie has no W's, but all 8 C's and 8 M's, she has \(0 + 8 + 8 = 16\) tiles. She needs 1 W.

The maximum number of tiles in the worst case (before getting the required letter) is 17. The next tile drawn will provide the missing letter (either a C or M), making the total number of tiles drawn \(17 + 1 = 18\).

Thus, the maximum number of tiles Annie may have to draw is \(\boxed{18}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

The problem asks about two related questions:

1. If $f(x)$ is measurable (Lebesgue), periodic with $f(x+1) = f(x)$, and $f(x) = \pm 1$, do we have almost everywhere $\limsup_{n \to \infty} f(nx) = +1$ and $\liminf_{n \to \infty} f(nx) = -1$?

2. More generally: If $f_n(x)$ are measurable, uniformly bounded, and $f_n(x + 1/n) \equiv f_n(x)$, do we have $\limsup_{n \to \infty} f_n(x) = \text{constant a.e.}$? And $\liminf_{n \to \infty} f_n(x) = \text{constant a.e.}$?

Let me think about this carefully.

**Part 1:** $f$ is measurable, 1-periodic, $f: \mathbb{R} \to \{-1, +1\}$. We want to know if $\limsup_{n\to\infty} f(nx) = +1$ a.e. and $\liminf_{n\to\infty} f(nx) = -1$ a.e.

First, let me think about what $f(nx)$ looks like. Since $f$ is 1-periodic, $f(nx) = f(\{nx\})$ where $\{nx\}$ is the fractional part.

The key question is about the distribution of $\{nx\}$ mod 1. For a.e. $x$, the sequence $\{nx\}$ is equidistributed mod 1 (by Weyl's theorem / the ergodic theorem applied to the map $T: x \mapsto x+1$ on the circle, but actually we need to think about this differently).

Wait, let me think again. We have the sequence $x, 2x, 3x, \ldots$ and we look at $f(nx) = f(\{nx\})$.

For a.e. $x$ (with respect to Lebesgue measure on, say, $[0,1]$), the sequence $\{nx\}_{n=1}^\infty$ is equidistributed mod 1. This is a classical result.

Actually, let me be more careful. The equidistribution of $\{nx\}$ mod 1 for a.e. $x$ is indeed a classical result. It follows from the ergodic theorem: consider the transformation $T: [0,1) \to [0,1)$, $T(x) = \{x + \alpha\}$... no wait, that's not quite right either.

Actually, the equidistribution of $\{nx\}$ for a.e. $x$ is a consequence of the pointwise ergodic theorem. Consider the map $T: \mathbb{T} \to \mathbb{T}$ given by $T(x) = x$ (identity)... no.

Let me think more carefully. We want to understand the behavior of $f(nx)$ as $n \to \infty$. 

Consider the sequence $g_n(x) = f(nx)$. Each $g_n$ is measurable and 1-periodic (since $f$ is 1-periodic: $g_n(x+1) = f(n(x+1)) = f(nx + n) = f(nx) = g_n(x)$, using $f$ 1-periodic and $n$ integer).

Now, for the equidistribution: For a.e. $x \in [0,1]$, the sequence $\{nx\}$ is equidistributed mod 1. This is indeed a classical theorem. One way to see it: by the ergodic theorem applied to the rotation by $x$ on the circle. Wait, no. Let me think about this differently.

Actually, the standard result is: for irrational $\alpha$, the sequence $\{n\alpha\}$ is equidistributed mod 1. And for a.e. $x$, $x$ is irrational, so $\{nx\}$ is equidistributed mod 1 for a.e. $x$.

Yes! That's the key. For every irrational $x$, the sequence $\{nx\}_{n \geq 1}$ is equidistributed mod 1 (Weyl's theorem). Since a.e. $x$ is irrational, we have equidistribution for a.e. $x$.

Now, if $\{nx\}$ is equidistributed mod 1, then for any measurable set $A \subset [0,1]$, 
$$\frac{1}{N}\sum_{n=1}^N \mathbf{1}_A(\{nx\}) \to |A|$$
where $|A|$ is the Lebesgue measure of $A$.

In particular, let $A = \{t \in [0,1] : f(t) = 1\}$ and $B = \{t \in [0,1] : f(t) = -1\}$. Then $A \cup B = [0,1]$ (up to measure zero) and $A \cap B = \emptyset$.

If $|A| > 0$, then for a.e. $x$, infinitely many $n$ have $\{nx\} \in A$, i.e., $f(nx) = 1$ for infinitely many $n$. So $\limsup f(nx) \geq 1$, hence $\limsup f(nx) = 1$ (since $f \leq 1$).

Similarly, if $|B| > 0$, then $\liminf f(nx) = -1$ for a.e. $x$.

But what if $|A| = 0$ or $|B| = 0$? 

If $f = 1$ a.e. (i.e., $|B| = 0$), then $f(nx) = 1$ for a.e. $x$ and all $n$... wait, not exactly. $f$ could be $-1$ on a measure-zero set. But $f(nx) = f(\{nx\})$, and $\{nx\}$ for a.e. $x$ is equidistributed, so it visits the measure-zero set $B$ with frequency 0. But it could still visit it infinitely often!

Hmm, this is the subtle point. Even if $|B| = 0$, the sequence $\{nx\}$ could hit $B$ infinitely often for some $x$.

Wait, but the question says $f(x) = \pm 1$, meaning $f$ takes values in $\{-1, +1\}$. It doesn't say $f$ is a.e. equal to a constant. 

Let me reconsider. The question is whether $\limsup f(nx) = +1$ and $\liminf f(nx) = -1$ a.e. This requires both $|A| > 0$ and $|B| > 0$.

If $f$ is identically $1$, then $\limsup f(nx) = 1$ but $\liminf f(nx) = 1 \neq -1$. So the answer to the first question would be NO in general.

Wait, but maybe the problem is asking whether this is true for all such $f$, or whether it's true for "generic" $f$? Let me re-read.

"We assume that $f(x)$ IS measurable ($L$), periodic, $f(x+1) = f(x)$ and $f(x) = \pm 1$. Do we have, almost everywhere, $\limsup_{n \to \infty} f(nx) = +1$, $\liminf_{n \to \infty} f(nx) = -1$?"

So the question is: for every such $f$, is it true that a.e. $\limsup f(nx) = 1$ and $\liminf f(nx) = -1$?

If $f \equiv 1$, this fails. So the answer would be NO.

But wait, maybe the problem is more subtle. Perhaps the problem is asking whether this is true for non-constant $f$, or perhaps there's a different interpretation.

Hmm, actually, let me reconsider. Maybe the problem is from a specific context where the answer is expected to be YES, and the interesting part is the proof. Or maybe the answer is NO and we need to provide a counterexample.

Let me think about the case where $f$ is not a.e. constant. Suppose $|A| > 0$ and $|B| > 0$ where $A = f^{-1}(1)$ and $B = f^{-1}(-1)$.

For a.e. $x$, $\{nx\}$ is equidistributed mod 1. By equidistribution, the frequency of visits to $A$ is $|A| > 0$, so there are infinitely many $n$ with $f(nx) = 1$, giving $\limsup \geq 1$, hence $\limsup = 1$. Similarly $\liminf = -1$.

So for non-a.e.-constant $f$ (both $|A|, |B| > 0$), the answer is YES.

But for $f \equiv 1$ or $f \equiv -1$ (a.e.), the answer is NO.

Actually, wait. Even if $f$ is a.e. constant but not identically constant, the situation is more subtle. If $f = 1$ a.e. but $f = -1$ on a measure-zero set $B$, then for a.e. $x$, does $\{nx\}$ hit $B$ infinitely often?

By equidistribution, the frequency is 0, but that doesn't preclude infinitely many visits. For example, if $B = \{1/2\}$, then $\{nx\} = 1/2$ iff $nx \equiv 1/2 \pmod{1}$, i.e., $x = (k + 1/2)/n$ for some integer $k$. For a fixed irrational $x$, this happens for at most finitely many $n$ (since $x$ is irrational, $\{nx\}$ never exactly equals $1/2$... actually it could, but only if $x$ is rational with appropriate denominator).

Hmm, actually for irrational $x$, $\{nx\}$ is never exactly $1/2$ (since $nx - 1/2$ would need to be an integer, meaning $x = (m + 1/2)/n$ is rational). So if $B$ is a countable set, then for a.e. (irrational) $x$, $\{nx\} \notin B$ for all $n$, so $f(nx) = 1$ for all $n$.

But if $B$ is an uncountable measure-zero set (like a Cantor set), the situation could be different.

Actually, for the equidistribution result, we know that for a.e. $x$, the empirical measure $\frac{1}{N}\sum_{n=1}^N \delta_{\{nx\}}$ converges weakly to Lebesgue measure. This means that for any continuity set $A$ (i.e., $|\partial A| = 0$), the frequency converges to $|A|$. But for a measure-zero set $B$, the frequency of visits is 0, which means the number of visits is $o(N)$. This doesn't tell us whether the number of visits is finite or infinite.

So the question of whether $\{nx\}$ hits a measure-zero set infinitely often for a.e. $x$ depends on the specific set.

OK so let me reconsider the problem. I think the problem is asking the question in full generality, and the answer might be:

For the first part: If $f$ takes both values $+1$ and $-1$ on sets of positive measure, then YES, $\limsup = 1$ and $\liminf = -1$ a.e. But if $f$ is a.e. constant, then NO.

But actually, re-reading the problem, I think the intent might be different. The problem says "$f(x) = \pm 1$" which I interpret as $f$ takes values in $\{-1, +1\}$. The question "Do we have..." is asking whether this is always true.

Given the trivial counterexample $f \equiv 1$, the answer to the first question is NO in general.

But wait, maybe the problem is more interesting than I think. Let me reconsider.

Actually, I think the problem might be asking about a specific $f$ that is given to be non-trivial, or the problem might be from a context where the interesting case is the non-constant one. Let me think about what the "right" answer is.

Hmm, actually, I think the problem is a well-known problem in ergodic theory / harmonic analysis, and the answer is YES for the first part (assuming $f$ takes both values on sets of positive measure) and the generalization is also YES.

Wait, let me reconsider the generalization more carefully.

**Part 2:** $f_n$ are measurable, uniformly bounded, $f_n(x + 1/n) = f_n(x)$. Is $\limsup f_n(x) = \text{const a.e.}$? Is $\liminf f_n(x) = \text{const a.e.}$?

The condition $f_n(x + 1/n) = f_n(x)$ means $f_n$ is periodic with period $1/n$.

So $f_n$ is $1/n$-periodic. This means $f_n$ is determined by its values on $[0, 1/n)$.

The connection to Part 1: if $f$ is 1-periodic and $f_n(x) = f(nx)$, then $f_n(x + 1/n) = f(n(x + 1/n)) = f(nx + 1) = f(nx) = f_n(x)$. So Part 1 is a special case of Part 2.

Now, for Part 2, the question is whether $\limsup f_n$ and $\liminf f_n$ are constants a.e.

Let me think about this. Each $f_n$ is $1/n$-periodic, so it's a function that oscillates faster and faster. 

Key idea: Consider $g_n(x) = f_n(x)$. Since $f_n$ is $1/n$-periodic, we can write $f_n(x) = h_n(\{nx\})$ where $h_n$ is a 1-periodic function (defined by $h_n(t) = f_n(t/n)$ for $t \in [0,1)$, extended periodically).

Wait, let me be more careful. If $f_n$ is $1/n$-periodic, then $f_n(x) = f_n(\{nx\}/n)$... no. Let me think again.

$f_n$ is $1/n$-periodic means $f_n(x + k/n) = f_n(x)$ for all integers $k$. So $f_n$ is determined by its values on $[0, 1/n)$. Define $h_n: [0,1) \to \mathbb{R}$ by $h_n(t) = f_n(t/n)$. Then $f_n(x) = h_n(\{nx\})$ where $\{nx\}$ is the fractional part of $nx$.

Check: $f_n(x) = f_n(x - \lfloor nx \rfloor / n) = f_n(\{nx\}/n) = h_n(\{nx\})$. Yes.

So $f_n(x) = h_n(\{nx\})$ where $h_n$ is a measurable function on $[0,1)$.

Now, the question becomes: is $\limsup_{n\to\infty} h_n(\{nx\})$ constant a.e.?

This is more subtle because $h_n$ changes with $n$.

Let me think about what tools we have. 

For the first part, where $h_n = f$ for all $n$ (a fixed function), the equidistribution of $\{nx\}$ for a.e. $x$ gives us the answer.

For the general case, we need something more.

Hmm, let me think about this differently. Let me consider the "averaging" approach.

Consider $S_N(x) = \frac{1}{N} \sum_{n=1}^N f_n(x)$. 

Actually, let me think about what $\int_0^1 f_n(x) dx$ is. Since $f_n$ is $1/n$-periodic, $\int_0^1 f_n(x) dx = \int_0^1 h_n(\{nx\}) dx$. By the substitution $u = nx$, $du = n\,dx$, $\int_0^1 h_n(\{nx\}) dx = \frac{1}{n} \int_0^n h_n(\{u\}) du = \frac{1}{n} \cdot n \int_0^1 h_n(t) dt = \int_0^1 h_n(t) dt$.

So $\int_0^1 f_n(x) dx = \int_0^1 h_n(t) dt =: a_n$.

Now, the question is about the pointwise behavior of $f_n(x)$.

Let me think about a specific approach. Consider two points $x, y \in [0,1)$. We want to understand when $\limsup f_n(x) = \limsup f_n(y)$.

Hmm, this is getting complicated. Let me think about the problem from a higher level.

Actually, I recall that this type of problem is related to the concept of "mixing" or "weak mixing" in ergodic theory. The key insight might be that the sequence of functions $f_n(x) = h_n(\{nx\})$ has some kind of mixing property.

Let me think about the correlation. Consider $\int_0^1 f_n(x) f_m(x) dx$ for $n \neq m$.

$\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx$.

By the substitution and using the fact that $(\{nx\}, \{mx\})$ is equidistributed in $[0,1)^2$ when $\gcd(n,m) = 1$ (and more generally when $n \neq m$), we get:

$\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx = \int_0^1 \int_0^1 h_n(s) h_m(t) ds\, dt = a_n \cdot a_m$

when $\gcd(n,m) = 1$. More generally, this holds when $n/m$ is irrational, but since $n, m$ are integers, $n/m$ is always rational. So we need to be more careful.

Actually, for integers $n \neq m$, the map $x \mapsto (\{nx\}, \{mx\})$ from $[0,1)$ to $[0,1)^2$ has its image on a subtorus. Specifically, if $d = \gcd(n,m)$, $n = da$, $m = db$ with $\gcd(a,b) = 1$, then $(\{nx\}, \{mx\}) = (d\{ax\}, d\{bx\})$... hmm, this isn't quite right.

Let me think differently. The map $x \mapsto (nx \mod 1, mx \mod 1)$ is a group homomorphism from $\mathbb{T}$ to $\mathbb{T}^2$. Its image is a closed subgroup. If $\gcd(n,m) = d$, then the image is $\{(s, t) \in \mathbb{T}^2 : bs \equiv at \pmod{1}\}$ where $n = da, m = db, \gcd(a,b)=1$. Wait, I need to think about this more carefully.

Actually, the image of $x \mapsto (nx, mx) \mod 1$ is the set $\{(nx \mod 1, mx \mod 1) : x \in \mathbb{T}\}$. This is a closed subgroup of $\mathbb{T}^2$. The Haar measure on this subgroup is the pushforward of Lebesgue measure on $\mathbb{T}$.

For the integral: $\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx = \int_{\text{image}} h_n(s) h_m(t) d\mu(s,t)$

where $\mu$ is the Haar measure on the image subgroup.

This is getting complicated. Let me try a different approach.

Let me think about the problem more carefully. The key question is: for the general case, is $\limsup f_n$ constant a.e.?

I think the answer is YES, and the proof uses the following idea:

Consider the "tail" behavior. For any two points $x, y$, we want to show that $\limsup f_n(x) = \limsup f_n(y)$ for a.e. $x, y$.

Actually, let me think about this problem differently. Let me consider the specific structure.

$f_n(x) = h_n(\{nx\})$ where $h_n: [0,1) \to \mathbb{R}$ is measurable and uniformly bounded.

For a.e. $x$, $\{nx\}$ is equidistributed mod 1. But $h_n$ changes with $n$, so equidistribution alone doesn't directly help.

Let me think about what "constant a.e." means for $\limsup$. It means there exists a constant $L$ such that $\limsup_{n\to\infty} f_n(x) = L$ for a.e. $x$.

Hmm, let me think about a potential approach using the Borel-Cantelli lemma or some density argument.

Actually, I think the key insight is the following. Let me consider the set $E_{n,\epsilon} = \{x : f_n(x) > L + \epsilon\}$ for some threshold $L$. We want to understand the measure of this set.

$|E_{n,\epsilon}| = |\{x \in [0,1) : h_n(\{nx\}) > L + \epsilon\}| = |\{t \in [0,1) : h_n(t) > L + \epsilon\}|$

by the equidistribution of $\{nx\}$ (the map $x \mapsto \{nx\}$ preserves Lebesgue measure on $[0,1)$... wait, does it?).

Actually, the map $x \mapsto \{nx\}$ from $[0,1)$ to $[0,1)$ is $n$-to-1 and preserves Lebesgue measure. So $|\{x : h_n(\{nx\}) > c\}| = |\{t : h_n(t) > c\}|$.

So $|E_{n,\epsilon}| = |\{t : h_n(t) > L + \epsilon\}|$.

Now, $\limsup f_n(x) > L + \epsilon$ iff $x \in \limsup E_{n,\epsilon}$ (i.e., $x$ is in infinitely many $E_{n,\epsilon}$).

By Borel-Cantelli, if $\sum_n |E_{n,\epsilon}| < \infty$, then $|\limsup E_{n,\epsilon}| = 0$, so $\limsup f_n(x) \leq L + \epsilon$ a.e.

But we don't have control over $\sum_n |E_{n,\epsilon}|$ in general.

Hmm, let me think about this differently.

Actually, I think the answer to the general question is YES, and the proof is based on the following key lemma:

**Key Lemma:** For any measurable, uniformly bounded sequence $f_n$ with $f_n$ being $1/n$-periodic, and for any $a < b$, the set $\{x : \liminf f_n(x) < a < b < \limsup f_n(x)\}$ has measure 0.

This would imply that $\limsup f_n$ and $\liminf f_n$ are each constant a.e. (though they might not be equal, i.e., the limit might not exist).

Let me think about how to prove this. The idea is to show that for any interval $(a, b)$, the set where $\liminf < a$ and $\limsup > b$ has measure 0.

Hmm, actually, I'm not sure this is true in general. Let me think of a potential counterexample.

Consider $h_n(t) = \mathbf{1}_{[0, 1/2)}(t) - \mathbf{1}_{[1/2, 1)}(t)$, i.e., $h_n$ is the same for all $n$. Then $f_n(x) = h(\{nx\})$ where $h$ is the $\pm 1$ function that's $+1$ on $[0,1/2)$ and $-1$ on $[1/2,1)$. By equidistribution, for a.e. $x$, $\limsup f_n(x) = 1$ and $\liminf f_n(x) = -1$. So both are constant a.e. (with $\limsup = 1$ and $\liminf = -1$). Good.

Now consider a different example. Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $f_n(x) = \mathbf{1}_{[0, 1/n)}(\{nx\})$. Now $|E_n| = 1/n$, and $\sum 1/n = \infty$. By the equidistribution and the second moment method (or direct computation), we can check whether $\limsup f_n(x) = 1$ a.e.

$f_n(x) = 1$ iff $\{nx\} < 1/n$, i.e., $nx \mod 1 < 1/n$, i.e., $x \in [k/n, (k+1)/n)$ for some $k$ with $nx - k < 1/n$... wait, $\{nx\} < 1/n$ means $nx = k + \epsilon$ with $0 \leq \epsilon < 1/n$, i.e., $x \in [k/n, k/n + 1/n^2)$ for some $k = 0, 1, \ldots, n-1$.

So $E_n = \bigcup_{k=0}^{n-1} [k/n, k/n + 1/n^2)$, which has measure $n \cdot 1/n^2 = 1/n$.

For a.e. $x$, is $x \in E_n$ for infinitely many $n$? Since $\sum |E_n| = \sum 1/n = \infty$, Borel-Cantelli doesn't directly give us the answer. We need to check independence or quasi-independence.

Actually, let me check: for $x$ irrational, when is $\{nx\} < 1/n$? This is related to the continued fraction expansion of $x$. By the three-distance theorem or Diophantine approximation, for a.e. $x$, $\|nx\| < 1/n$ infinitely often (where $\|nx\|$ is the distance to the nearest integer). But we need $\{nx\} < 1/n$, not $\|nx\| < 1/n$.

Actually, $\{nx\} < 1/n$ is a one-sided condition. By the theory of continued fractions, for a.e. $x$, $\{nx\} < 1/n$ infinitely often (this follows from the Khintchine theorem or similar results in Diophantine approximation). So $\limsup f_n(x) = 1$ for a.e. $x$.

And $\liminf f_n(x) = 0$ (since $f_n \geq 0$ and $f_n(x) = 0$ for most $n$). So $\limsup = 1$ and $\liminf = 0$, both constant a.e. Good.

Now let me try to construct a counterexample where $\limsup$ is NOT constant.

Hmm, what if I make $h_n$ depend on $n$ in a way that "targets" specific $x$ values?

For instance, let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t - \{n\alpha\})$ for some fixed irrational $\alpha$... no, this doesn't quite work because $h_n$ is a function on $[0,1)$ and I need to be careful.

Actually, let me think about this more carefully. The key constraint is that $f_n(x) = h_n(\{nx\})$, and $h_n$ can be any measurable function on $[0,1)$.

Consider $h_n(t) = \mathbf{1}_{\{t < 1/n\}}$. Then $f_n(x) = 1$ iff $\{nx\} < 1/n$. As discussed, for a.e. $x$, this happens infinitely often, so $\limsup = 1$ a.e.

What if $h_n(t) = \mathbf{1}_{\{t \in [a_n, a_n + 1/n)\}}$ for some sequence $a_n$? Then $f_n(x) = 1$ iff $\{nx\} \in [a_n, a_n + 1/n)$. 

By the equidistribution of $\{nx\}$, for a.e. $x$, the sequence $\{nx\}$ is equidistributed, so it visits $[a_n, a_n + 1/n)$ with "expected frequency" $1/n$. But since the interval changes with $n$, this is more subtle.

Actually, I think the key tool here is the following. For a.e. $x$, the sequence $\{nx\}$ is not just equidistributed but has stronger properties. Specifically, for a.e. $x$, the sequence $\{nx\}$ is "Poissonian" in a certain sense (this is related to the pair correlation problem).

But I think for this problem, we might not need such deep results. Let me think about the structure more.

Let me consider the problem from the perspective of the "translation" structure. The key observation is:

$f_n(x) = h_n(\{nx\})$, and the map $x \mapsto \{nx\}$ is measure-preserving from $([0,1), \text{Lebesgue})$ to $([0,1), \text{Lebesgue})$.

So $f_n$ has the same distribution as $h_n$ (as random variables on $[0,1)$). That is, for any Borel set $B$, $|\{x : f_n(x) \in B\}| = |\{t : h_n(t) \in B\}|$.

Now, the question is about the joint distribution of $(f_1, f_2, f_3, \ldots)$ and specifically about $\limsup$ and $\liminf$.

Let me think about the correlation between $f_n$ and $f_m$.

$\int_0^1 f_n(x) f_m(x) dx = \int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx$.

As I discussed before, this involves the joint distribution of $(\{nx\}, \{mx\})$.

For $n \neq m$, the map $x \mapsto (\{nx\}, \{mx\})$ from $[0,1)$ to $[0,1)^2$ has its image on a 1-dimensional subtorus. The pushforward of Lebesgue measure is the Haar measure on this subtorus.

If $\gcd(n, m) = 1$, then the map $x \mapsto (\{nx\}, \{mx\})$ is actually a bijection (mod 1) from $[0,1)$ to the subtorus $\{(s,t) : ns \equiv mt \pmod{1}\}$... hmm, wait. Let me think again.

If $\gcd(n,m) = 1$, then there exist integers $a, b$ with $an + bm = 1$. The map $x \mapsto (nx \mod 1, mx \mod 1)$ is injective (mod 1): if $nx_1 \equiv nx_2$ and $mx_1 \equiv mx_2 \pmod{1}$, then $n(x_1 - x_2) \equiv 0$ and $m(x_1 - x_2) \equiv 0 \pmod{1}$, so $(x_1 - x_2) \equiv 0 \pmod{1}$ (since $\gcd(n,m) = 1$). So the map is a bijection from $\mathbb{T}$ to a closed subgroup of $\mathbb{T}^2$.

The image is $\{(s,t) \in \mathbb{T}^2 : ms \equiv nt \pmod{1}\}$ (this is the kernel of the map $(s,t) \mapsto ms - nt \mod 1$). This is a 1-dimensional subtorus.

The pushforward of Lebesgue measure is the Haar measure on this subtorus, which is NOT the product measure. So $\{nx\}$ and $\{mx\}$ are NOT independent (as random variables on $[0,1)$ with Lebesgue measure).

This means the correlation $\int f_n f_m$ is NOT simply $a_n \cdot a_m$ in general. It depends on the specific functions $h_n, h_m$ and the subtorus.

This makes the problem more complex. Let me think about whether the result is still true.

Actually, let me reconsider. Maybe I should think about this problem using a different approach. Let me consider the "ergodic" approach.

Consider the space $X = [0,1)^\mathbb{N}$ with the product measure, and the map $\Phi: [0,1) \to X$ given by $\Phi(x) = (\{x\}, \{2x\}, \{3x\}, \ldots)$. The pushforward of Lebesgue measure under $\Phi$ is some measure $\mu$ on $X$.

The question is about the $\mu$-a.e. behavior of $\limsup h_n(\pi_n(\cdot))$ where $\pi_n$ is the $n$-th coordinate projection.

If $\mu$ were the product measure, then the coordinates would be independent, and we could use standard tools. But $\mu$ is NOT the product measure (the coordinates are correlated).

However, there's a key property: the sequence $(\{nx\})_{n \geq 1}$ is equidistributed for a.e. $x$, and more strongly, it satisfies a "mixing" property in some sense.

Let me think about a specific approach. 

**Approach: Show that $\limsup f_n$ is invariant under translations, hence constant a.e.**

If I can show that $\limsup f_n(x) = \limsup f_n(x + \alpha)$ for a.e. $x$ and for all $\alpha$ (or for a dense set of $\alpha$), then $\limsup f_n$ is invariant under all translations, hence constant a.e.

But this seems hard because $f_n(x + \alpha) = h_n(\{n(x+\alpha)\}) = h_n(\{nx + n\alpha\})$, which is a "shifted" version of $h_n$.

Hmm, this doesn't directly work because the shift $n\alpha$ depends on $n$.

Let me try another approach.

**Approach: Use the specific structure of the problem.**

Let me think about what happens when we "average" $f_n$ over a small interval.

Consider $\frac{1}{|I|} \int_I f_n(x) dx$ for an interval $I$. Since $f_n$ is $1/n$-periodic, for $|I| \gg 1/n$, this average is approximately $\int_0^1 h_n(t) dt = a_n$.

More precisely, if $I = [y, y+\delta]$, then $\int_I f_n(x) dx = \int_y^{y+\delta} h_n(\{nx\}) dx = \frac{1}{n} \int_{ny}^{n(y+\delta)} h_n(\{u\}) du$.

If $n\delta$ is large, this is approximately $\delta \cdot a_n$ (by the periodicity of $h_n(\{u\})$ with period 1, the integral over a long interval is approximately the length times the average).

So $\frac{1}{\delta} \int_I f_n(x) dx \approx a_n$ when $n \gg 1/\delta$.

This means that for large $n$, $f_n$ "averages out" to $a_n$ on any fixed interval. This is a kind of "weak convergence" or "oscillatory convergence" property.

But this doesn't directly tell us about pointwise $\limsup$.

Let me think about the problem differently. Maybe I should consider the specific case first and then generalize.

**Part 1 revisited:**

$f$ is 1-periodic, $f: \mathbb{R} \to \{-1, +1\}$, measurable. Let $A = \{t \in [0,1) : f(t) = 1\}$, $B = \{t \in [0,1) : f(t) = -1\}$.

Case 1: $|A| = 0$. Then $f = -1$ a.e. For a.e. $x$, $\{nx\}$ is equidistributed, so $\{nx\} \in A$ with frequency 0. But does $\{nx\} \in A$ for infinitely many $n$?

If $A$ is, say, a single point $\{t_0\}$, then $\{nx\} = t_0$ iff $x = (k + t_0)/n$ for some integer $k$, which means $x$ is rational (if $t_0$ is rational) or $x$ is in a specific countable set. For a.e. $x$ (irrational), $\{nx\} \neq t_0$ for all $n$, so $f(nx) = -1$ for all $n$, and $\limsup = \liminf = -1$.

But if $A$ is a "fat" measure-zero set (like a set of Hausdorff dimension 1 but measure 0), it's possible that $\{nx\} \in A$ for infinitely many $n$ for a.e. $x$.

Hmm, actually, I think for any measure-zero set $A$, for a.e. $x$, $\{nx\} \notin A$ for all but finitely many $n$. Is this true?

No, this is NOT true in general. Consider $A = \bigcup_n \{t : \|nt\| < 1/n^2\}$... this is getting complicated.

Actually, let me think about it differently. By the Borel-Cantelli lemma, if $\sum_n |\{x : \{nx\} \in A\}| < \infty$, then for a.e. $x$, $\{nx\} \in A$ for only finitely many $n$. Now, $|\{x : \{nx\} \in A\}| = |A|$ (since $x \mapsto \{nx\}$ is measure-preserving). So $\sum_n |A| = \infty$ if $|A| > 0$, and $= 0$ if $|A| = 0$.

Wait, if $|A| = 0$, then $|\{x : \{nx\} \in A\}| = 0$ for each $n$, so the sum is 0, and by Borel-Cantelli, for a.e. $x$, $\{nx\} \in A$ for only finitely many $n$. Actually, even stronger: the set $\{x : \{nx\} \in A \text{ for some } n\}$ has measure 0 (since it's a countable union of measure-zero sets). So for a.e. $x$, $\{nx\} \notin A$ for ALL $n$.

Wait, that's not right either. $|\{x : \{nx\} \in A\}| = |A| = 0$ for each $n$ (since the map $x \mapsto \{nx\}$ preserves measure). So $\bigcup_n \{x : \{nx\} \in A\}$ has measure 0. Therefore, for a.e. $x$, $\{nx\} \notin A$ for all $n \geq 1$.

So if $|A| = 0$, then for a.e. $x$, $f(nx) = -1$ for all $n$, and $\limsup = \liminf = -1$.

Similarly, if $|B| = 0$, then for a.e. $x$, $f(nx) = 1$ for all $n$, and $\limsup = \liminf = 1$.

If $|A| > 0$ and $|B| > 0$, then for a.e. $x$, $\{nx\}$ is equidistributed, so it visits $A$ with frequency $|A| > 0$ and $B$ with frequency $|B| > 0$. In particular, it visits both $A$ and $B$ infinitely often, so $\limsup f(nx) = 1$ and $\liminf f(nx) = -1$.

So for Part 1:
- If $f$ takes both values on sets of positive measure: $\limsup = 1$, $\liminf = -1$ a.e. ✓
- If $f = 1$ a.e.: $\limsup = \liminf = 1$ a.e.
- If $f = -1$ a.e.: $\limsup = \liminf = -1$ a.e.

In all cases, $\limsup$ is constant a.e. and $\liminf$ is constant a.e. But the specific values $\limsup = 1, \liminf = -1$ only hold when $f$ takes both values on positive measure sets.

So the answer to "do we have $\limsup = 1, \liminf = -1$ a.e.?" is: YES if $f$ takes both values $+1$ and $-1$ on sets of positive Lebesgue measure; NO in general (trivial counterexample: $f \equiv 1$).

But I think the problem is asking whether this is true for all such $f$, and the answer is NO (with the trivial counterexample). But perhaps the problem is asking about the non-trivial case, or perhaps the answer is meant to be YES with the understanding that $f$ is non-constant.

Hmm, let me re-read the problem. "We assume that $f(x)$ IS measurable ($L$), periodic, $f(x+1) = f(x)$ and $f(x) = \pm 1$. Do we have, almost everywhere, $\limsup = +1, \liminf = -1$?"

I think the problem is asking: given these conditions, is it necessarily true that $\limsup = 1$ and $\liminf = -1$ a.e.? The answer is NO if $f$ is a.e. constant, but YES if $f$ takes both values on positive measure sets.

But actually, I think the more interesting question is the general one (Part 2), and the answer there is also that $\limsup$ and $\liminf$ are constant a.e.

Let me now focus on Part 2 and try to prove that $\limsup f_n$ is constant a.e. (and similarly for $\liminf$).

**Part 2: Proof that $\limsup f_n$ is constant a.e.**

Let $f_n$ be measurable, uniformly bounded (say $|f_n| \leq M$), and $1/n$-periodic.

We write $f_n(x) = h_n(\{nx\})$ where $h_n: [0,1) \to [-M, M]$ is measurable.

**Step 1: $\limsup f_n$ is invariant under rational translations.**

Consider $f_n(x + p/q)$ for a rational $p/q$. We have $f_n(x + p/q) = h_n(\{nx + np/q\})$.

Now, $\{nx + np/q\} = \{nx + np/q\}$. The shift $np/q \mod 1$ depends on $n$.

For $n$ divisible by $q$, say $n = qm$, we have $np/q = mp$, which is an integer, so $\{nx + np/q\} = \{nx\}$. Thus $f_n(x + p/q) = f_n(x)$ for all $n$ divisible by $q$.

So $\limsup_{n \to \infty} f_n(x + p/q) \geq \limsup_{m \to \infty} f_{qm}(x + p/q) = \limsup_{m \to \infty} f_{qm}(x)$.

Similarly, $\limsup_{n \to \infty} f_n(x) \geq \limsup_{m \to \infty} f_{qm}(x)$.

But this only gives us inequalities between the limsups along subsequences, not equality.

Hmm, let me think more carefully.

Let $L(x) = \limsup_{n \to \infty} f_n(x)$ and $L_q(x) = \limsup_{m \to \infty} f_{qm}(x)$.

We have $L(x) \geq L_q(x)$ for all $q$ (since $\{qm\}$ is a subsequence of $\{n\}$).

Also, $L(x + p/q) \geq L_q(x + p/q) = L_q(x)$ (since $f_{qm}(x + p/q) = f_{qm}(x)$).

And $L(x) \geq L_q(x)$.

But we also need the reverse inequality. We have $L(x) = \max_{r=0,\ldots,q-1} L_q^{(r)}(x)$ where $L_q^{(r)}(x) = \limsup_{m \to \infty} f_{qm+r}(x)$... no, that's not right either. $\limsup$ of the full sequence is the max of the limsups of the subsequences only if we take the max over all residue classes, but actually $\limsup_{n} a_n = \max_{r=0}^{q-1} \limsup_m a_{qm+r}$.

So $L(x) = \max_{r=0}^{q-1} L_q^{(r)}(x)$ where $L_q^{(r)}(x) = \limsup_{m \to \infty} f_{qm+r}(x)$.

Now, $f_{qm+r}(x + p/q) = h_{qm+r}(\{(qm+r)x + (qm+r)p/q\}) = h_{qm+r}(\{(qm+r)x + rp/q\})$ (since $(qm)p/q = mp$ is an integer).

So $f_{qm+r}(x + p/q) = h_{qm+r}(\{(qm+r)x + rp/q\})$.

This is NOT simply $f_{qm+r}(x)$ unless $r = 0$. So the invariance under rational translations only works for the subsequence where $q | n$.

This approach is getting complicated. Let me try a different strategy.

**Step 2: Use the density of rational translates and Fubini.**

Actually, let me try a more direct approach. The key idea is:

For any $\epsilon > 0$ and any $a \in \mathbb{R}$, define $E_n(a, \epsilon) = \{x \in [0,1) : f_n(x) > a + \epsilon\}$. Then $|E_n(a, \epsilon)| = |\{t \in [0,1) : h_n(t) > a + \epsilon\}|$ (since $x \mapsto \{nx\}$ preserves measure).

Let $\alpha_n(a, \epsilon) = |E_n(a, \epsilon)| = |\{t : h_n(t) > a + \epsilon\}|$.

Now, $\{x : L(x) > a + \epsilon\} \subseteq \limsup_n E_n(a, \epsilon)$ (where $\limsup$ of sets means $\bigcap_N \bigcup_{n \geq N} E_n$).

If $\sum_n \alpha_n(a, \epsilon) < \infty$, then by Borel-Cantelli, $|\limsup_n E_n(a, \epsilon)| = 0$, so $L(x) \leq a + \epsilon$ a.e.

But we don't have control over $\sum_n \alpha_n$ in general.

Hmm, let me think about this differently. Maybe the answer is actually NO for the general case, and we need a counterexample.

**Potential counterexample for Part 2:**

Let me try to construct $f_n$ such that $\limsup f_n(x)$ is not constant.

Idea: Make $f_n$ "target" a specific set of $x$ values.

Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/n\} = \mathbf{1}_{x \in \bigcup_{k=0}^{n-1} [k/n, k/n + 1/n^2)}$.

As computed before, $|E_n| = 1/n$, and $\sum 1/n = \infty$.

For a.e. $x$, is $x \in E_n$ for infinitely many $n$? This is the question of whether $\{nx\} < 1/n$ infinitely often for a.e. $x$.

By the theory of continued fractions, for a.e. $x$, $\{nx\} < 1/n$ infinitely often. In fact, by Khintchine's theorem, for a.e. $x$, $\|nx\| < \psi(n)$ infinitely often iff $\sum \psi(n) = \infty$ (for monotone $\psi$). Here $\|nx\|$ is the distance to the nearest integer, and $\psi(n) = 1/n$ gives $\sum 1/n = \infty$. But we need $\{nx\} < 1/n$ (one-sided), not $\|nx\| < 1/n$.

By a one-sided version, for a.e. $x$, $\{nx\} < 1/n$ infinitely often. So $\limsup f_n(x) = 1$ for a.e. $x$.

And $\liminf f_n(x) = 0$ for a.e. $x$ (since $f_n(x) = 0$ for "most" $n$). So both are constant a.e.

Let me try a different counterexample. What if I make $h_n$ depend on $n$ in a way that creates non-constant limsup?

Consider $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n$ odd and $h_n(t) = \mathbf{1}_{[1/2, 1)}(t)$ for $n$ even. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/2\}$ for $n$ odd and $f_n(x) = \mathbf{1}_{\{nx\} \geq 1/2\}$ for $n$ even. For a.e. $x$, $\{nx\}$ is equidistributed, so both $\{nx\} < 1/2$ and $\{nx\} \geq 1/2$ happen infinitely often. So $\limsup f_n(x) = 1$ and $\liminf f_n(x) = 0$ for a.e. $x$. Still constant.

What if I make the sets depend on $n$ more cleverly?

Let $A_n \subset [0,1)$ be measurable sets with $|A_n| = 1/2$ for all $n$, and $h_n = \mathbf{1}_{A_n}$. Then $f_n(x) = \mathbf{1}_{A_n}(\{nx\})$, and $|\{x : f_n(x) = 1\}| = 1/2$.

For the limsup to be non-constant, I would need the set $\{x : \{nx\} \in A_n \text{ i.o.}\}$ to have measure strictly between 0 and 1.

But by the Borel-Cantelli lemma (independence version), if the events $\{x : \{nx\} \in A_n\}$ were independent, then since $\sum |A_n| = \sum 1/2 = \infty$, the limsup would have measure 1. But the events are NOT independent.

However, there might be a "quasi-independence" result that still gives measure 1 for the limsup.

Hmm, let me think about this more carefully. The events $E_n = \{x : \{nx\} \in A_n\}$ have $|E_n| = |A_n| = 1/2$. The question is whether $|\limsup E_n| = 1$.

Actually, I think there's a general result that says: for any sequence of measurable sets $A_n \subset [0,1)$ with $|A_n| = \alpha > 0$, the set $\{x : \{nx\} \in A_n \text{ i.o.}\}$ has measure 1.

This would follow from a "Borel-Cantelli with quasi-independence" result. Let me think about whether this is true.

The key is to estimate $|E_n \cap E_m|$ for $n \neq m$. We have $E_n \cap E_m = \{x : \{nx\} \in A_n \text{ and } \{mx\} \in A_m\}$.

$|E_n \cap E_m| = \int_0^1 \mathbf{1}_{A_n}(\{nx\}) \mathbf{1}_{A_m}(\{mx\}) dx$.

As discussed, this equals the integral of $\mathbf{1}_{A_n}(s) \mathbf{1}_{A_m}(t)$ over the subtorus $\{(s,t) : ms \equiv nt \pmod{1}\}$ with respect to Haar measure.

If $\gcd(n,m) = 1$, the subtorus is $\{(s,t) : ms - nt \in \mathbb{Z}\}$, which is a 1-dimensional subtorus. The Haar measure on this subtorus is the pushforward of Lebesgue measure under $x \mapsto (\{nx\}, \{mx\})$.

In general, $|E_n \cap E_m|$ can range from $\max(0, |A_n| + |A_m| - 1)$ to $\min(|A_n|, |A_m|)$, depending on the alignment of $A_n$ and $A_m$ on the subtorus.

If $A_n = A_m = [0, 1/2)$ and $\gcd(n,m) = 1$, then $|E_n \cap E_m| = |\{x : \{nx\} < 1/2, \{mx\} < 1/2\}|$. This is the measure of the set of $x$ where both $\{nx\}$ and $\{mx\}$ are in $[0, 1/2)$. By the equidistribution on the subtorus, this is $1/4$ if the subtorus is "generic" enough. But it could be different.

Actually, for $n = 1, m = 2$: $|E_1 \cap E_2| = |\{x \in [0,1) : x < 1/2, \{2x\} < 1/2\}| = |\{x \in [0, 1/4)\}| = 1/4 = |A_1| \cdot |A_2|$. So in this case, it's the product.

For $n = 1, m = 3$: $|E_1 \cap E_3| = |\{x \in [0,1) : x < 1/2, \{3x\} < 1/2\}|$. $\{3x\} < 1/2$ iff $x \in [0, 1/6) \cup [1/3, 1/2) \cup [2/3, 5/6)$. Intersecting with $[0, 1/2)$: $[0, 1/6) \cup [1/3, 1/2)$, which has measure $1/6 + 1/6 = 1/3$. This is NOT $1/4$.

So the events are not independent, and the correlation can be different from the product.

This makes the Borel-Cantelli approach more difficult. Let me think about whether there's a general theorem that handles this.

Actually, I recall that there's a result by Gallagher (or maybe it's a consequence of the Erdős–Turán inequality or the large sieve) that gives a Borel-Cantelli type result for the sequence $\{nx\}$.

Actually, I think the key result is the following: for any sequence of intervals $I_n \subset [0,1)$ with $\sum |I_n| = \infty$, the set $\{x : \{nx\} \in I_n \text{ i.o.}\}$ has full measure. This is a theorem by Khintchine (or maybe a consequence of the Duffin-Schaeffer theorem).

But for general measurable sets (not intervals), the situation might be different.

Hmm, let me think about this problem from a completely different angle.

**Alternative approach: Use the ergodic theorem.**

Consider the transformation $T: [0,1) \to [0,1)$, $T(x) = \{x + \alpha\}$ for some irrational $\alpha$. This is ergodic.

Now, $f_n(T(x)) = f_n(\{x + \alpha\}) = h_n(\{n(x + \alpha)\}) = h_n(\{nx + n\alpha\})$.

This is a "shifted" version of $h_n$, and the shift $n\alpha \mod 1$ varies with $n$.

This doesn't directly give us ergodicity of the limsup.

**Another approach: Use the fact that $f_n$ "converges weakly" to its average.**

As I noted before, for any fixed interval $I$, $\frac{1}{|I|} \int_I f_n(x) dx \to a_n$ as $n \to \infty$ (where $a_n = \int_0^1 h_n(t) dt$), because $f_n$ oscillates with period $1/n$.

More precisely, $|\frac{1}{|I|} \int_I f_n(x) dx - a_n| \leq \frac{C}{n|I|}$ for some constant $C$ depending on $M$ (the uniform bound).

This means $f_n \rightharpoonup a_n$ weakly in $L^\infty$ (against $L^1$ test functions that are "fixed").

But this doesn't directly help with pointwise limsup.

**Yet another approach: Direct computation using the structure.**

Let me try to show that $\limsup f_n(x)$ is the same for a.e. $x$ by showing that it's "translation-invariant" in some sense.

Consider two points $x$ and $y = x + \delta$ for small $\delta$. We want to compare $\limsup f_n(x)$ and $\limsup f_n(y)$.

$f_n(y) = f_n(x + \delta) = h_n(\{nx + n\delta\})$.

For large $n$, $n\delta \mod 1$ "sweeps" through $[0,1)$ rapidly (if $\delta$ is irrational). So $h_n(\{nx + n\delta\})$ is like $h_n$ evaluated at a "random" point (shifted from $\{nx\}$ by $n\delta$).

But this heuristic is hard to make rigorous.

Let me try yet another approach.

**Approach via conditional expectation and martingale-like arguments:**

Hmm, I don't see an immediate connection.

**Let me reconsider the problem statement.**

The problem asks two questions:
1. For $f$ 1-periodic, $\pm 1$-valued, measurable: is $\limsup f(nx) = 1, \liminf f(nx) = -1$ a.e.?
2. For $f_n$ uniformly bounded, measurable, $1/n$-periodic: is $\limsup f_n = \text{const}$ a.e.? Is $\liminf f_n = \text{const}$ a.e.?

I think the answer to both is YES (with the caveat for Part 1 that $f$ must take both values on positive measure sets for the specific values $+1, -1$).

For Part 2, the answer is that $\limsup$ and $\liminf$ are constant a.e., and I think this can be proved using the following key idea:

**Key Idea: For any $a$, the set $\{x : \limsup f_n(x) > a\}$ is invariant under all translations, hence has measure 0 or 1.**

To show invariance under translations, we need to show that $\limsup f_n(x) = \limsup f_n(x + \delta)$ for a.e. $x$, for any $\delta$.

Let me try to prove this. Fix $\delta \in [0,1)$.

$f_n(x + \delta) = h_n(\{n(x+\delta)\}) = h_n(\{nx + n\delta\})$.

Let $\theta_n = \{n\delta\}$. Then $f_n(x + \delta) = h_n(\{nx + \theta_n\})$.

Now, define $\tilde{h}_n(t) = h_n(\{t + \theta_n\})$. Then $f_n(x + \delta) = \tilde{h}_n(\{nx\})$.

So the question becomes: is $\limsup h_n(\{nx\}) = \limsup \tilde{h}_n(\{nx\})$ for a.e. $x$?

This is not obvious because $h_n$ and $\tilde{h}_n$ differ by a shift that depends on $n$.

Hmm, this approach doesn't seem to work directly.

**Let me try a completely different approach: the 0-1 law.**

I want to show that for any $a$, $|\{x : \limsup f_n(x) > a\}| \in \{0, 1\}$.

Consider the $\sigma$-algebra $\mathcal{F}_n = \sigma(f_n, f_{n+1}, \ldots)$ (the "tail" $\sigma$-algebra). The limsup is $\mathcal{F}_1$-measurable (it's in the tail $\sigma$-algebra $\bigcap_n \mathcal{F}_n$).

If we can show that the tail $\sigma$-algebra is trivial (i.e., contains only sets of measure 0 or 1), then $\limsup f_n$ is constant a.e.

But the tail $\sigma$-algebra being trivial is exactly a 0-1 law, which typically requires some kind of independence or mixing.

The issue is that the $f_n$ are not independent. So we need to show some form of mixing.

Let me think about the mixing property. For $n \neq m$, consider the correlation:

$\text{Cov}(f_n, f_m) = \int_0^1 f_n(x) f_m(x) dx - \left(\int_0^1 f_n\right)\left(\int_0^1 f_m\right)$

$= \int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx - a_n a_m$.

As discussed, this depends on the joint distribution of $(\{nx\}, \{mx\})$ and the specific functions $h_n, h_m$.

For $\gcd(n,m) = 1$, the joint distribution is the Haar measure on the subtorus $\{(s,t) : ms \equiv nt \pmod{1}\}$. In general, the covariance can be non-zero.

So the $f_n$ are not uncorrelated, and a standard 0-1 law doesn't apply.

However, maybe we can use a more refined argument. Let me think about the structure of the correlations.

For $n$ and $m$ with $\gcd(n,m) = d$, $n = da, m = db$, $\gcd(a,b) = 1$:

$\int_0^1 h_n(\{nx\}) h_m(\{mx\}) dx = \int_0^1 h_{da}(\{dax\}) h_{db}(\{dbx\}) dx$.

Let $u = dx$. Then $\{dax\} = \{a \cdot dx\}$ and $\{dbx\} = \{b \cdot dx\}$. Let $y = dx \mod 1$, so $y$ is uniform on $[0,1)$ (as $x$ ranges over $[0,1)$, $dx$ ranges over $[0,d)$, and $\{dx\}$ is uniform on $[0,1)$). Then:

$\int_0^1 h_{da}(\{ay\}) h_{db}(\{by\}) dy$.

Now, since $\gcd(a,b) = 1$, the map $y \mapsto (\{ay\}, \{by\})$ is a bijection from $[0,1)$ to the subtorus $T_{a,b} = \{(s,t) : bs \equiv at \pmod{1}\}$, and the pushforward of Lebesgue measure is Haar measure on $T_{a,b}$.

So $\int_0^1 h_{da}(\{ay\}) h_{by}(\{by\}) dy = \int_{T_{a,b}} h_{da}(s) h_{db}(t) d\mu_{a,b}(s,t)$.

This is NOT $\int h_{da} \int h_{db} = a_{da} \cdot a_{db}$ in general.

So the correlations are non-trivial. This makes the 0-1 law approach difficult.

Let me try to think about specific cases where the correlations might cause problems.

**Case: $f_n(x) = h(\{nx\})$ for a fixed $h$.**

In this case, $a_n = \int h$ for all $n$, and the covariance is:

$\text{Cov}(f_n, f_m) = \int_{T_{a,b}} h(s) h(t) d\mu_{a,b}(s,t) - \left(\int h\right)^2$.

For $h = \mathbf{1}_{[0,\alpha)}$ (indicator of an interval), the covariance depends on the specific subtorus.

But in this case, we already know the answer from Part 1: by equidistribution, $\limsup f_n(x) = \text{ess sup } h$ and $\liminf f_n(x) = \text{ess inf } h$ for a.e. $x$ (assuming $h$ takes its ess sup and ess inf on positive measure sets). So the limsup and liminf are constant a.e.

**Back to the general case:**

Let me try a different approach. I'll try to show that for any two points $x, y$ that are "generic" (in a suitable sense), $\limsup f_n(x) = \limsup f_n(y)$.

Actually, let me try to use the following strategy:

1. Show that $\limsup f_n(x) \geq \limsup a_n$ for a.e. $x$ (where $a_n = \int_0^1 h_n$).
2. Show that $\limsup f_n(x) \leq \limsup \text{ess sup } h_n$ for a.e. $x$.
3. Show that the actual value of $\limsup f_n(x)$ is the same for a.e. $x$.

Hmm, this is still vague. Let me think more concretely.

Actually, let me reconsider. Maybe the answer to Part 2 is actually NO, and we need a counterexample.

**Constructing a counterexample:**

Let me try to construct $f_n$ such that $\limsup f_n(x)$ depends on $x$.

Idea: Use binary expansion. Let $x = 0.x_1 x_2 x_3 \ldots$ in binary. Define $f_n(x)$ based on the $n$-th binary digit of $x$.

But $f_n$ needs to be $1/n$-periodic, which is a strong constraint. The $n$-th binary digit of $x$ is determined by $\{2^n x\}$, and the function $\mathbf{1}_{\{2^n x\} \geq 1/2}$ is $1/2^n$-periodic, not $1/n$-periodic. So this doesn't directly work.

Let me think about what $1/n$-periodic functions look like. $f_n$ is $1/n$-periodic, so it's constant on intervals of length $1/n$ (if it's a step function). More generally, $f_n(x) = h_n(\{nx\})$ where $h_n$ is 1-periodic.

To make $\limsup f_n(x)$ depend on $x$, I would need to "encode" information about $x$ into the sequence $h_n(\{nx\})$.

The key constraint is that $\{nx\}$ for a.e. $x$ is equidistributed, so the "information" about $x$ that can be extracted from $\{nx\}$ is limited.

But wait, $\{nx\}$ for different $n$ are correlated (they all depend on the same $x$). So in principle, the joint behavior of $(\{x\}, \{2x\}, \{3x\}, \ldots)$ carries a lot of information about $x$ (in fact, it determines $x$).

So the question is: can we choose $h_n$ to "decode" enough information about $x$ to make $\limsup h_n(\{nx\})$ non-constant?

Let me try a specific construction. Let $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ if $n$ is a power of 2, and $h_n(t) = 0$ otherwise. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/2\}$ for $n = 2^k$ and $f_n(x) = 0$ otherwise.

$\limsup f_n(x) = \limsup_{k \to \infty} \mathbf{1}_{\{2^k x\} < 1/2\}$.

Now, $\{2^k x\} < 1/2$ iff the $(k+1)$-th binary digit of $x$ is 0. For a.e. $x$ (with respect to Lebesgue measure, which corresponds to fair coin flips in binary), the binary digits are i.i.d. Bernoulli(1/2). So $\limsup_{k} \mathbf{1}_{\{2^k x\} < 1/2} = 1$ for a.e. $x$ (since there are infinitely many 0 digits). And $\liminf = 0$ for a.e. $x$ (since there are infinitely many 1 digits).

So $\limsup = 1$ and $\liminf = 0$, both constant a.e. Still constant.

But wait, $h_n$ for $n = 2^k$ is $1/2^k$-periodic? No, $h_n$ is 1-periodic (it's a function on $[0,1)$), and $f_n(x) = h_n(\{nx\})$ is $1/n$-periodic. So $f_{2^k}(x) = \mathbf{1}_{\{2^k x\} < 1/2}$ is $1/2^k$-periodic. ✓

But the issue is that I set $h_n = 0$ for $n$ not a power of 2, which means $f_n = 0$ for those $n$. The limsup is determined by the subsequence $n = 2^k$, and as I showed, it's constant a.e.

Let me try to make the limsup depend on $x$ more cleverly. What if I use the binary digits to construct a non-constant function?

Let $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for all $n$. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/2\}$. By equidistribution, for a.e. $x$, $\{nx\} < 1/2$ for infinitely many $n$ and $\{nx\} \geq 1/2$ for infinitely many $n$. So $\limsup = 1$ and $\liminf = 0$, constant a.e.

What if I use a "thinner" set? Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $f_n(x) = \mathbf{1}_{\{nx\} < 1/n\}$. By Khintchine's theorem (or the theory of continued fractions), for a.e. $x$, $\{nx\} < 1/n$ infinitely often, so $\limsup = 1$. And $\liminf = 0$ since $f_n(x) = 0$ for most $n$. Constant a.e.

What if I make the set even thinner? $h_n(t) = \mathbf{1}_{[0, 1/n^2)}(t)$. Then $|E_n| = 1/n^2$ and $\sum 1/n^2 < \infty$. By Borel-Cantelli, for a.e. $x$, $f_n(x) = 1$ for only finitely many $n$. So $\limsup = 0$ a.e. Constant.

What about $h_n(t) = \mathbf{1}_{[0, 1/(n \log n))}(t)$? Then $\sum 1/(n \log n) = \infty$, so by Khintchine, $\limsup = 1$ a.e. Constant.

It seems hard to make the limsup non-constant using these "interval" constructions. The Borel-Cantelli lemma and Khintchine's theorem always give us a 0-1 behavior.

But what if I use non-interval sets? Let me try:

$h_n(t) = \mathbf{1}_{A_n}(t)$ where $A_n$ is a measurable subset of $[0,1)$ with $|A_n| = 1/2$, but $A_n$ is a "fat Cantor set" or some fractal set.

The question is whether $\{nx\} \in A_n$ infinitely often for a.e. $x$. Since $|A_n| = 1/2$ and $\sum 1/2 = \infty$, if there's a Borel-Cantelli type result that works for general measurable sets (not just intervals), then the limsup would be 1 a.e.

I believe such a result exists. Let me think about it.

**Theorem (Khintchine-type for general sets):** For any sequence of measurable sets $A_n \subset [0,1)$ with $\sum |A_n| = \infty$, the set $\{x \in [0,1) : \{nx\} \in A_n \text{ i.o.}\}$ has full measure.

Is this true? I don't think it's true in full generality. The Khintchine theorem typically requires the sets to be intervals (or at least "nice" sets). For general measurable sets, the behavior can be different.

Actually, wait. Let me think about a potential counterexample. Let $A_n = [0, 1/2)$ if $n$ is even and $A_n = [1/2, 1)$ if $n$ is odd. Then $\sum |A_n| = \infty$, and $\{nx\} \in A_n$ i.o. iff $\{nx\} < 1/2$ for infinitely many even $n$ and $\{nx\} \geq 1/2$ for infinitely many odd $n$. By equidistribution, both happen for a.e. $x$. So the limsup is 1 a.e.

What if $A_n$ "avoids" the values $\{nx\}$ takes? For example, can I choose $A_n$ such that $\{nx\} \notin A_n$ for all $n$ and for a positive measure set of $x$?

This would require $A_n$ to avoid $\{nx \mod 1 : x \in E\}$ for some positive measure set $E$. But $\{nx \mod 1 : x \in E\}$ has measure $|E|$ (since $x \mapsto \{nx\}$ preserves measure), so if $|A_n| + |E| > 1$, they must overlap. But if $|A_n|$ is small, they might not overlap.

Hmm, but I need $\{nx\} \notin A_n$ for ALL $n$, not just for some $n$. This is much harder to arrange.

Let me try a different approach to constructing a counterexample.

**Counterexample attempt using the binary expansion:**

Let $x \in [0,1)$ with binary expansion $x = 0.b_1 b_2 b_3 \ldots$. The map $x \mapsto \{2^k x\}$ gives $\{2^k x\} = 0.b_{k+1} b_{k+2} \ldots$.

Now, define $h_{2^k}(t) = b_k(x)$... wait, $h_n$ can't depend on $x$. $h_n$ is a fixed function.

Let me think differently. I want to construct $h_n$ such that $\limsup h_n(\{nx\})$ is not constant.

Consider $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n = 2^k$ and $h_n(t) = 0$ otherwise. As before, $\limsup f_n(x) = \limsup_k \mathbf{1}_{\{2^k x\} < 1/2} = 1$ a.e. (since binary digits contain infinitely many 0s a.s.).

What if I use a different subsequence? $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n = k!$ and $h_n = 0$ otherwise. Then $\limsup f_n(x) = \limsup_k \mathbf{1}_{\{k! x\} < 1/2}$.

Is $\{k! x\} < 1/2$ infinitely often for a.e. $x$? Since $k!$ grows super-exponentially, the sequence $\{k! x\}$ is "almost independent" (by a result on lacunary sequences). For lacunary sequences, the Borel-Cantelli lemma works as if the events were independent. So since $\sum 1/2 = \infty$, the limsup is 1 a.e.

What about a non-lacunary subsequence? $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for all $n$. Then $\limsup = 1$ a.e. by equidistribution.

It seems very hard to make the limsup non-constant. Let me try a radically different approach.

**Approach: Make $h_n$ "encode" the value of $x$ in a way that creates a non-constant limsup.**

The idea: for each $n$, $h_n$ is a function on $[0,1)$. The value $h_n(\{nx\})$ depends on $\{nx\}$, which is a "coarse-grained" version of $x$ (at resolution $1/n$). As $n$ increases, we get finer and finer information about $x$.

Can we choose $h_n$ such that $h_n(\{nx\})$ "converges" to some non-constant function of $x$?

For example, let $h_n(t) = \mathbf{1}_{[0, x_0)}(t)$ for some fixed $x_0 \in (0,1)$. Then $f_n(x) = \mathbf{1}_{\{nx\} < x_0\}$. By equidistribution, for a.e. $x$, $\limsup f_n(x) = 1$ and $\liminf f_n(x) = 0$ (since $\{nx\}$ visits $[0, x_0)$ infinitely often and $[x_0, 1)$ infinitely often). So the limsup is constant.

What if $h_n$ "converges" to a function as $n \to \infty$? Say $h_n(t) = g(t)$ for all $n$, where $g$ is some fixed function. Then $f_n(x) = g(\{nx\})$, and by equidistribution, $\limsup f_n(x) = \text{ess sup } g$ and $\liminf f_n(x) = \text{ess inf } g$ for a.e. $x$. Constant.

What if $h_n$ converges to $g$ in some sense? Say $h_n \to g$ in $L^1$. Then $a_n \to \int g$. But the pointwise limsup of $h_n(\{nx\})$ is not directly related to $g(\{nx\})$ because the "equidistribution" and the "convergence" are happening at different rates.

Hmm, let me think about this more carefully.

Actually, I think the answer to Part 2 is YES (limsup and liminf are constant a.e.), and the proof uses a clever argument. Let me try to find the right approach.

**Key Insight: The "density" argument.**

For any $\epsilon > 0$ and any $a \in \mathbb{R}$, define:
$E_n^+ = \{x : f_n(x) > a + \epsilon\}$ and $E_n^- = \{x : f_n(x) < a - \epsilon\}$.

We have $|E_n^+| = |\{t : h_n(t) > a + \epsilon\}|$ and $|E_n^-| = |\{t : h_n(t) < a - \epsilon\}|$.

Now, suppose $L := \limsup_n \text{ess sup}_{t} h_n(t)$ (the limsup of the essential suprema). I claim that $\limsup f_n(x) = L$ for a.e. $x$.

Hmm, but this might not be true either. Let me think about what the right "constant" is.

Actually, let me consider a specific example. Let $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$. Then $\text{ess sup } h_n = 1$ for all $n$, so $L = 1$. And we showed $\limsup f_n(x) = 1$ a.e. ✓

Let $h_n(t) = 1 - 1/n$ for all $t$. Then $f_n(x) = 1 - 1/n$, and $\limsup f_n(x) = 1$. And $L = \limsup (1 - 1/n) = 1$. ✓

Let $h_n(t) = \mathbf{1}_{[0, 1/2)}(t)$ for $n$ odd and $h_n(t) = 0$ for $n$ even. Then $\text{ess sup } h_n = 1$ for $n$ odd, $0$ for $n$ even. $L = 1$. And $\limsup f_n(x) = \limsup_{\text{odd } n} \mathbf{1}_{\{nx\} < 1/2} = 1$ a.e. (by equidistribution on the odd subsequence). ✓

Hmm, what if $\text{ess sup } h_n \to 0$? Let $h_n(t) = 1/n$. Then $f_n(x) = 1/n \to 0$. $\limsup = 0$. And $L = \limsup 1/n = 0$. ✓

What if $\text{ess sup } h_n$ oscillates? $h_n(t) = 1$ for $n$ in a sparse set $S$ and $h_n(t) = 0$ for $n \notin S$. Then $L = 1$ (if $S$ is infinite). And $\limsup f_n(x) = 1$ iff $f_n(x) = 1$ for infinitely many $n \in S$, which happens iff $x \in \bigcup_{n \in S} [0,1)$... well, $f_n(x) = 1$ for all $x$ when $n \in S$, so $\limsup = 1$ for all $x$. ✓

OK so in all these examples, $\limsup f_n(x) = \limsup_n \text{ess sup } h_n$ a.e. Is this always true?

Let me check: $h_n(t) = \mathbf{1}_{[0, 1/n^2)}(t)$. Then $\text{ess sup } h_n = 1$ for all $n$, so $L = 1$. But $|E_n| = 1/n^2$ and $\sum 1/n^2 < \infty$, so by Borel-Cantelli, $f_n(x) = 1$ for only finitely many $n$, a.e. So $\limsup f_n(x) = 0 \neq 1 = L$.

So the conjecture $\limsup f_n = \limsup \text{ess sup } h_n$ is FALSE.

The issue is that even though $\text{ess sup } h_n = 1$, the set where $h_n$ is close to 1 has small measure, and the Borel-Cantelli lemma kicks in.

So what IS the right constant? Let me think about this more carefully.

For $h_n(t) = \mathbf{1}_{[0, 1/n^2)}(t)$: $\limsup f_n(x) = 0$ a.e. The "right" constant is 0.

For $h_n(t) = \mathbf{1}_{[0, 1/n)}(t)$: $\limsup f_n(x) = 1$ a.e. (by Khintchine). The "right" constant is 1.

The difference is $\sum |A_n|$: $< \infty$ in the first case, $= \infty$ in the second.

So the constant depends on whether $\sum |A_n|$ converges or diverges. But this is specific to indicator functions of intervals. For general $h_n$, the situation is more complex.

Let me think about the general case. For any $a \in \mathbb{R}$ and $\epsilon > 0$:

$\{x : \limsup f_n(x) > a + \epsilon\} \subseteq \limsup_n \{x : f_n(x) > a + \epsilon\}$.

$|\{x : f_n(x) > a + \epsilon\}| = |\{t : h_n(t) > a + \epsilon\}| =: \alpha_n(a + \epsilon)$.

If $\sum_n \alpha_n(a + \epsilon) < \infty$, then $|\limsup_n \{x : f_n(x) > a + \epsilon\}| = 0$ by Borel-Cantelli, so $\limsup f_n(x) \leq a + \epsilon$ a.e.

Conversely, if $\sum_n \alpha_n(a + \epsilon) = \infty$, does $\limsup f_n(x) \geq a + \epsilon$ a.e.?

This is the "converse Borel-Cantelli" question, and it requires some independence or quasi-independence.

For the sequence $\{nx\}$, there's a result (I think due to various people, maybe related to the Duffin-Schaeffer conjecture or the Khintchine theorem) that gives a converse Borel-Cantelli for intervals. But for general measurable sets, it might not hold.

Hmm, let me think about whether the converse can fail for general measurable sets.

**Potential counterexample for the converse:**

Let $A_n \subset [0,1)$ be measurable with $|A_n| = 1/2$ for all $n$, but chosen so that $\{nx\} \in A_n$ for only finitely many $n$ for a positive measure set of $x$.

Can we do this? We need to find $A_n$ with $|A_n| = 1/2$ such that $\bigcap_N \bigcup_{n \geq N} \{x : \{nx\} \in A_n\}$ has measure $< 1$.

This is equivalent to: $\bigcup_N \bigcap_{n \geq N} \{x : \{nx\} \notin A_n\}$ has measure $> 0$.

I.e., there's a positive measure set of $x$ such that $\{nx\} \notin A_n$ for all large $n$.

Can we find such $A_n$? Let me try.

Let $A_n = [0, 1/2) \setminus \{nx \mod 1 : x \in [0, 1/4)\}$... no, this doesn't make sense because $A_n$ can't depend on $x$.

Let me try a different approach. For each $n$, the set $\{x : \{nx\} \in A_n\}$ has measure $|A_n| = 1/2$. The question is whether we can make these sets "align" so that their limsup has measure $< 1$.

Consider $A_n = [1/2, 1)$ for all $n$. Then $\{x : \{nx\} \in A_n\} = \{x : \{nx\} \geq 1/2\}$, which has measure 1/2. The limsup is $\{x : \{nx\} \geq 1/2 \text{ i.o.}\}$, which has measure 1 by equidistribution.

What if $A_n$ "avoids" $\{nx\}$ for $x$ in some set? For example, let $E = [0, 1/4)$ and define $A_n = [0,1) \setminus \{\{nx\} : x \in E\}$. But $\{\{nx\} : x \in E\}$ has measure $|E| = 1/4$ (since $x \mapsto \{nx\}$ preserves measure), so $|A_n| \geq 3/4 > 1/2$. We could take a subset of measure 1/2.

But even so, for $x \in E$, $\{nx\} \in \{\{ny\} : y \in E\}$, which is the set we're trying to avoid. So $\{nx\} \notin A_n$ for $x \in E$... but $A_n$ is a subset of $[0,1) \setminus \{\{ny\} : y \in E\}$, so $\{nx\} \notin A_n$ for $x \in E$. This means $f_n(x) = 0$ for all $n$ and all $x \in E$!

Wait, but $A_n$ depends on $n$ and on $E$, and $E$ is fixed. Let me be more precise.

For each $n$, let $B_n = \{\{nx\} : x \in E\} = \{nx \mod 1 : x \in [0, 1/4)\}$. This is a set of measure 1/4 (since $x \mapsto \{nx\}$ is measure-preserving). Let $A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$. (This is possible since $|[0,1) \setminus B_n| = 3/4 > 1/2$.)

Then for $x \in E$, $\{nx\} \in B_n$, so $\{nx\} \notin A_n$, so $f_n(x) = 0$ for all $n$. Thus $\limsup f_n(x) = 0$ for $x \in E$.

For $x \notin E$, $\{nx\}$ might or might not be in $A_n$. The limsup for $x \notin E$ could be 1 (if $\{nx\} \in A_n$ i.o. for a.e. $x \notin E$).

So $\limsup f_n(x) = 0$ on $E$ (measure 1/4) and possibly 1 on $[0,1) \setminus E$ (measure 3/4). This would be a non-constant limsup!

Wait, but I need to check that $\limsup f_n(x) = 1$ for a.e. $x \notin E$. Is this true?

For $x \notin E$, $\{nx\} \notin B_n$ doesn't mean $\{nx\} \in A_n$ (since $A_n$ is a proper subset of $[0,1) \setminus B_n$). So we need $\{nx\} \in A_n$ i.o.

$|A_n| = 1/2$ and $\sum 1/2 = \infty$. If the events $\{x : \{nx\} \in A_n\}$ are "quasi-independent" for $x \notin E$, then by converse Borel-Cantelli, $\limsup = 1$ a.e. on $[0,1) \setminus E$.

But are they quasi-independent? This depends on the specific choice of $A_n$.

Hmm, but even if the limsup is not exactly 1 on $[0,1) \setminus E$, the key point is that it's different from 0 (which is the value on $E$). So the limsup would be non-constant.

Wait, but I need to be more careful. Let me re-examine the construction.

$E = [0, 1/4)$. For each $n$, $B_n = \{nx \mod 1 : x \in [0, 1/4)\}$. 

$B_n$ is the image of $[0, 1/4)$ under $x \mapsto \{nx\}$. Since $x \mapsto \{nx\}$ is $n$-to-1 and measure-preserving, $B_n$ is a union of $n$ intervals, each of length $1/(4n)$, and $|B_n| = 1/4$.

Specifically, $B_n = \bigcup_{k=0}^{n-1} [k/n, k/n + 1/(4n))$.

$A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$. For example, $A_n = [1/4, 3/4) \setminus B_n$... hmm, this might not have measure exactly 1/2. Let me just say $A_n$ is any measurable subset of $[0,1) \setminus B_n$ with $|A_n| = 1/2$.

Now, for $x \in E = [0, 1/4)$: $\{nx\} \in B_n$ (by definition of $B_n$), so $\{nx\} \notin A_n$, so $f_n(x) = 0$ for all $n$. Thus $\limsup f_n(x) = 0$.

For $x \notin E$: we need to check whether $\{nx\} \in A_n$ infinitely often. Since $|A_n| = 1/2$ and $\sum 1/2 = \infty$, if there's a converse Borel-Cantelli, then $\limsup f_n(x) = 1$ for a.e. $x \notin E$.

But even without the converse Borel-Cantelli, the key point is that $\limsup f_n(x) \geq 0$ for all $x$ (since $f_n \geq 0$), and $\limsup f_n(x) = 0$ on $E$ (measure 1/4). If $\limsup f_n(x) > 0$ on a positive measure subset of $[0,1) \setminus E$, then the limsup is non-constant.

Actually, we can make this even simpler. Let $h_n(t) = \mathbf{1}_{A_n}(t)$ where $A_n = [1/4, 3/4)$ for all $n$. Then $f_n(x) = \mathbf{1}_{\{nx\} \in [1/4, 3/4)}$.

For $x \in [0, 1/4)$: $\{nx\} \in [0, 1/4) \cup \ldots$ — actually, $\{nx\}$ for $x \in [0, 1/4)$ ranges over $[0, 1/4)$ (when $nx < 1/4$, i.e., $x < 1/(4n)$) and other intervals. By equidistribution, for a.e. $x \in [0, 1/4)$, $\{nx\}$ is equidistributed in $[0,1)$, so $\{nx\} \in [1/4, 3/4)$ with frequency $1/2$. So $\limsup f_n(x) = 1$ for a.e. $x \in [0, 1/4)$.

So this doesn't work — the limsup is still 1 everywhere.

The issue is that for a.e. $x \in E$, $\{nx\}$ is equidistributed in $[0,1)$, not confined to $B_n$. The set $B_n$ depends on $n$, and for a fixed $x$, $\{nx\}$ doesn't stay in $B_n$.

Wait, I think I made an error. Let me re-examine.

$B_n = \{\{ny\} : y \in E\}$. For a fixed $x \in E$, $\{nx\}$ is a specific value, and it's in $B_n$ by definition (since $x \in E$, $\{nx\} = \{ny\}$ for $y = x$). So $\{nx\} \in B_n$ for all $n$ and all $x \in E$.

But $A_n \subset [0,1) \setminus B_n$, so $\{nx\} \notin A_n$ for all $n$ and all $x \in E$. So $f_n(x) = 0$ for all $n$ and all $x \in E$. ✓

Now, for $x \notin E$: $\{nx\}$ might or might not be in $A_n$. The question is whether $\{nx\} \in A_n$ for infinitely many $n$.

The set $\{x : \{nx\} \in A_n\}$ has measure $|A_n| = 1/2$. But for $x \in E$, this set is empty (since $\{nx\} \in B_n$ and $A_n \cap B_n = \emptyset$). So the set $\{x : \{nx\} \in A_n\}$ is contained in $[0,1) \setminus E$, and has measure 1/2. Since $|[0,1) \setminus E| = 3/4$, the conditional probability (given $x \notin E$) is $(1/2)/(3/4) = 2/3$.

Now, $\sum_{n} |\{x \notin E : \{nx\} \in A_n\}| = \sum 1/2 = \infty$. If the converse Borel-Cantelli holds (with quasi-independence), then $\limsup f_n(x) = 1$ for a.e. $x \notin E$.

But does the converse Borel-Cantelli hold here? The sets $A_n$ are somewhat arbitrary (just subsets of $[0,1) \setminus B_n$ with measure 1/2), so the quasi-independence might fail.

However, even if the converse Borel-Cantelli fails, we might still have $\limsup f_n(x) > 0$ for some $x \notin E$, which would make the limsup non-constant.

Actually, let me think about this more carefully. For $x \notin E$, is it possible that $\{nx\} \notin A_n$ for all large $n$? This would require $\{nx\} \in B_n \cup ([0,1) \setminus (A_n \cup B_n))$ for all large $n$. Since $|A_n| = 1/2$ and $|B_n| = 1/4$, $|[0,1) \setminus (A_n \cup B_n)| = 1/4$. So the "avoidance" set has measure 1/4 + 1/4 = 1/2 for each $n$. If $\sum 1/2 = \infty$ and the events are quasi-independent, then $\{nx\}$ is in the avoidance set infinitely often, but also in $A_n$ infinitely often.

I think for "generic" choices of $A_n$, the converse Borel-Cantelli would hold and $\limsup = 1$ a.e. on $[0,1) \setminus E$. But I'm not sure how to prove this in general.

Let me try to make the counterexample more explicit. Let me choose $A_n$ specifically.

Let $E = [0, 1/4)$. For each $n$, $B_n = \bigcup_{k=0}^{n-1} [k/n, k/n + 1/(4n))$.

Let $A_n = [1/2, 1) \setminus B_n$. Then $|A_n| = |[1/2, 1)| - |B_n \cap [1/2, 1)|$. 

$B_n \cap [1/2, 1)$: The intervals $[k/n, k/n + 1/(4n))$ that intersect $[1/2, 1)$. There are about $n/2$ such intervals, each contributing $1/(4n)$, so $|B_n \cap [1/2, 1)| \approx 1/8$. So $|A_n| \approx 1/2 - 1/8 = 3/8$. Not exactly 1/2, but close enough for our purposes.

Actually, let me simplify. Let $A_n = [3/4, 1)$. Then $|A_n| = 1/4$ and $A_n \cap B_n = \emptyset$ iff $B_n \cap [3/4, 1) = \emptyset$. But $B_n$ contains intervals near $3/4$ (specifically, $[k/n, k/n + 1/(4n))$ for $k$ near $3n/4$), so $B_n \cap [3/4, 1) \neq \emptyset$ in general.

This is getting complicated. Let me just use the abstract construction: $A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$.

The key point is: for $x \in E$, $f_n(x) = 0$ for all $n$, so $\limsup = 0$. For $x \notin E$, $\limsup \geq 0$ and potentially $> 0$. So the limsup is not constant (it's 0 on $E$ and possibly positive elsewhere).

But wait, I need to verify that $\limsup f_n(x) > 0$ for at least some $x \notin E$ (on a set of positive measure). Otherwise, the limsup could be 0 everywhere, which is still constant.

For $x \notin E$, $f_n(x) = \mathbf{1}_{\{nx\} \in A_n}$. The expected value of $f_n(x)$ (over $x \notin E$) is $|A_n| / |[0,1) \setminus E| = (1/2) / (3/4) = 2/3$. So on average, $f_n(x) = 1$ about 2/3 of the time. This suggests that $\limsup f_n(x) = 1$ for a.e. $x \notin E$.

But can we prove this? The issue is the lack of independence. However, I think we can use the following argument:

For $x \notin E$, consider the sequence $\{nx\}$. This sequence is equidistributed in $[0,1)$ for a.e. $x$. But $A_n$ changes with $n$, so equidistribution alone doesn't suffice.

However, we can use the following: for any fixed interval $I \subset [0,1)$, $|\{x \notin E : \{nx\} \in I\}| \to |I| \cdot |[0,1) \setminus E|$ as $n \to \infty$ (by equidistribution). If $A_n$ contains a fixed interval $I$ for infinitely many $n$, then $\{nx\} \in I \subset A_n$ for infinitely many $n$ (for a.e. $x$), giving $\limsup \geq 1$.

But $A_n$ might not contain any fixed interval. Since $A_n \subset [0,1) \setminus B_n$ and $B_n$ becomes "dense" as $n \to \infty$ (it's a union of $n$ intervals of length $1/(4n)$, covering $1/4$ of $[0,1)$), $A_n$ could be a "fractured" set.

Hmm, but $A_n$ has measure 1/2, and it's contained in $[0,1) \setminus B_n$ which has measure 3/4. So $A_n$ is a "large" subset of $[0,1) \setminus B_n$.

I think for "most" choices of $A_n$, the limsup would be 1 a.e. on $[0,1) \setminus E$. But I'm not sure how to prove this rigorously.

Let me try a different, cleaner counterexample.

**Cleaner counterexample:**

Let $E \subset [0,1)$ be a measurable set with $0 < |E| < 1$. For each $n$, define $h_n(t) = \mathbf{1}_{[0,1) \setminus E}(\{nt\})$... no, this is circular.

Let me think about this differently. I want $f_n(x) = 0$ for $x \in E$ and $f_n(x) = 1$ for $x \notin E$ (at least for infinitely many $n$).

$f_n(x) = h_n(\{nx\})$. For $x \in E$, I want $h_n(\{nx\}) = 0$, i.e., $\{nx\} \notin A_n$ where $A_n = h_n^{-1}(1)$. This means $B_n := \{\{nx\} : x \in E\} \subset [0,1) \setminus A_n$.

So I need $A_n \subset [0,1) \setminus B_n$ where $B_n = \{\{nx\} : x \in E\}$, $|B_n| = |E|$.

If $|E| < 1/2$, then $|[0,1) \setminus B_n| = 1 - |E| > 1/2$, so I can choose $A_n \subset [0,1) \setminus B_n$ with $|A_n| = 1/2$.

Then for $x \in E$: $f_n(x) = 0$ for all $n$, so $\limsup = 0$.
For $x \notin E$: $f_n(x) = \mathbf{1}_{\{nx\} \in A_n}$, and $|\{x \notin E : \{nx\} \in A_n\}| = |A_n| = 1/2$ (since $\{x : \{nx\} \in A_n\} \subset [0,1) \setminus E$ because $A_n \cap B_n = \emptyset$).

Now, $\sum_n |\{x \notin E : f_n(x) = 1\}| = \sum 1/2 = \infty$.

If the converse Borel-Cantelli holds (even in a weak form), then $\limsup f_n(x) = 1$ for a.e. $x \notin E$, and the limsup is non-constant (0 on $E$, 1 on $[0,1) \setminus E$).

But does the converse Borel-Cantelli hold? The sets $\{x : \{nx\} \in A_n\}$ are not independent, but they might be "quasi-independent" enough.

Actually, I realize that the converse Borel-Cantelli might NOT hold for arbitrary measurable sets $A_n$. The sets $A_n$ could be chosen adversarially to make the limsup as small as possible.

In fact, let me think about whether we can make $\limsup f_n(x) = 0$ for ALL $x$ (not just $x \in E$). This would require $\{nx\} \notin A_n$ for all large $n$ and all $x$. But $|\{x : \{nx\} \in A_n\}| = 1/2$ for each $n$, so $\bigcup_{n \geq N} \{x : \{nx\} \in A_n\}$ has measure $\geq 1/2$ for each $N$. So $\limsup \{x : \{nx\} \in A_n\}$ has measure $\geq 1/2$... no, that's not right. The measure of the union could be less than the sum.

Actually, $\limsup_n \{x : \{nx\} \in A_n\}$ has measure $\geq \limsup_n |\{x : \{nx\} \in A_n\}| = 1/2$... no, that's not right either. The measure of the limsup of sets is not bounded below by the limsup of measures.

By Fatou's lemma: $|\limsup E_n| \geq \limsup |E_n|$ is NOT true in general. Actually, $|\liminf E_n| \leq \liminf |E_n|$ and
