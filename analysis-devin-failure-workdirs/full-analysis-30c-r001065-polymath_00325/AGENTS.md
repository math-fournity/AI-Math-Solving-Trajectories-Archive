# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Call a number feared if it contains the digits \(13\) as a contiguous substring and fearless otherwise. (For example, \(132\) is feared, while \(123\) is fearless.) Compute the smallest positive integer \(n\) such that there exists a positive integer \(a<100\) such that \(n\) and \(n+10a\) are fearless while \(n+a, n+2a, \ldots, n+9a\) are all feared.       — 题目文本
#   Solution: First, note that \(n, n+a, \ldots, n+10a\) cannot all be less than \(1000\), since a fearless number cannot have \(13\) as its last two digits. Numbers like \(129, 130, 131, \ldots, 139\) do not work because \(139\) is feared.

Thus, we must consider numbers of the form \(13xy\), where \(1, 3, x\), and \(y\) are digits. If all of \(n+a, n+2a, \ldots, n+9a\) start with \(13\), then \(a \leq 12\). The minimum we can achieve is:

\[
1288, 1300, 1312, \ldots, 1384, 1396, 1408
\]

However, if \(n+9a = 1413\), we can take \(a = 14\) to get:

\[
1287, 1301, 1315, \ldots, 1399, 1413, 1427
\]

Thus, the minimum possible value for \(n\) is \(1287\).

\(\boxed{1287}\)  — 标准解答
#   Let me analyze this problem carefully.

We need to find the smallest positive integer $n$ such that there exists a positive integer $a < 100$ where:
- $n$ is fearless (no "13" as contiguous substring)
- $n + 10a$ is fearless
- $n + a, n + 2a, \ldots, n + 9a$ are all feared (contain "13")

So we have 11 numbers: $n, n+a, n+2a, \ldots, n+10a$. The first and last are fearless, the middle 9 are feared.

Let me think about this systematically. The numbers form an arithmetic progression with common difference $a$.

Let me think about what makes a number feared - it contains "13" as a contiguous substring in its decimal representation.

Let me think about the structure. We have $n$ and $n+10a$ fearless, and $n+ka$ for $k=1,...,9$ all feared.

Let me consider the last two digits. If $a$ is small relative to the number, the higher digits stay mostly fixed while the last digits change.

Actually, let me think about this differently. Let's consider the decimal representation.

Let me try small values of $a$ first and search for the smallest $n$.

For a given $a$, we need $n$ fearless, $n+10a$ fearless, and all intermediate values feared.

Let me think about the digit structure. The key insight is that "13" needs to appear in the decimal representation.

Let me consider the case where the "13" appears in the last two digits. If $n + ka$ has last two digits forming "13" (i.e., $\equiv 13 \pmod{100}$), then it's feared.

But we need this for $k=1,...,9$ simultaneously, which means $n+a \equiv n+2a \equiv \ldots \equiv n+9a \equiv 13 \pmod{100}$, which requires $a \equiv 0 \pmod{100}$, but $a < 100$, so $a = 0$, not positive. So the "13" can't always be in the last two digits.

So the "13" must appear in different positions for different $k$ values, or in higher digits.

Let me think about this more carefully. The numbers $n, n+a, \ldots, n+10a$ span a range of $10a$. Since $a < 100$, the range is at most 990.

Let me think about when "13" appears in the tens-hundreds boundary or similar.

Let me consider the structure where the number has the form ...X... where X is some digit pattern.

Actually, let me think about this more concretely. Let's say $n$ has digits $d_m d_{m-1} \ldots d_1 d_0$.

For $n + ka$ to be feared, "13" must appear somewhere. The position where "13" appears could depend on $k$.

Let me think about a specific approach. Consider numbers around 1300. If $n$ is slightly below 1300, then $n + ka$ might cross 1300, making some of them feared (containing "13" at the thousands-hundreds position).

Wait, but we need $n+1a$ through $n+9a$ ALL feared, and $n$ and $n+10a$ fearless.

Let me think about the range $[n, n+10a]$. The total spread is $10a < 1000$.

Strategy: Find a range where crossing certain boundaries creates "13" patterns.

Let me think about the hundreds digit. If we're in a range like 1250-1350, numbers in [1300, 1399] contain "13" at the thousands-hundreds position (digits "13" at positions 3,2).

So if $n + ka$ falls in [1300, 1399] for $k=1,...,9$, they're all feared. And $n$ and $n+10a$ are outside this range (and fearless otherwise).

For this: $n < 1300$, $n + a \geq 1300$, $n + 9a \leq 1399$, $n + 10a > 1399$ (or $n + 10a \leq 1399$ but fearless for another reason... no, if $n+10a \in [1300, 1399]$ it would be feared).

So we need:
- $n + a \geq 1300 \Rightarrow n \geq 1300 - a$
- $n + 9a \leq 1399 \Rightarrow n \leq 1399 - 9a$
- $n + 10a > 1399 \Rightarrow n > 1399 - 10a$, i.e., $n \geq 1400 - 10a$
- $n < 1300$
- $n$ is fearless
- $n + 10a$ is fearless

From the first and fourth: $1300 - a \leq n < 1300$, so $n \in [1300-a, 1299]$.
From the second and third: $1400 - 10a \leq n \leq 1399 - 9a$.

We need both ranges to overlap: $\max(1300-a, 1400-10a) \leq n \leq \min(1299, 1399-9a)$.

For the upper bound: $1399 - 9a \geq 1300 - a \Rightarrow 99 \geq 8a \Rightarrow a \leq 12$.
Also $1299 \geq 1400 - 10a \Rightarrow 10a \geq 101 \Rightarrow a \geq 11$.

So $a \in \{11, 12\}$.

For $a = 11$: $n \in [\max(1289, 1290), \min(1299, 1300)] = [1290, 1299]$.
$n + 10a = n + 110 \in [1400, 1409]$.
We need $n$ fearless and $n+110$ fearless.
$n \in [1290, 1299]$: none of these contain "13", so all fearless. ✓
$n + 110 \in [1400, 1409]$: none contain "13", so all fearless. ✓
And $n + ka$ for $k=1,...,9$: $n + ka \in [1301, 1399+11-1]$. Wait let me compute.
$n = 1290$: $n+11 = 1301$ (feared, "13"), ..., $n+99 = 1389$ (feared), $n+110 = 1400$ (fearless). ✓
$n = 1299$: $n+11 = 1310$ (feared), ..., $n+99 = 1398$ (feared), $n+110 = 1409$ (fearless). ✓

So for $a = 11$, $n = 1290$ works! Let me verify:
- $n = 1290$: digits "1290", no "13" → fearless ✓
- $n + 11 = 1301$: "1301" contains "13" → feared ✓
- $n + 22 = 1312$: "1312" contains "13" → feared ✓
- $n + 33 = 1323$: "1323" contains "13" → feared ✓
- $n + 44 = 1334$: "1334" contains "13" → feared ✓
- $n + 55 = 1345$: "1345" contains "13" → feared ✓
- $n + 66 = 1356$: "1356" contains "13" → feared ✓
- $n + 77 = 1367$: "1367" contains "13" → feared ✓
- $n + 88 = 1378$: "1378" contains "13" → feared ✓
- $n + 99 = 1389$: "1389" contains "13" → feared ✓
- $n + 110 = 1400$: "1400", no "13" → fearless ✓

So $n = 1290$ works with $a = 11$.

But can we do better? Can we find a smaller $n$?

Let me think about whether there's a smaller $n$ with a different $a$.

The approach above used the "13" appearing at the thousands-hundreds boundary (1300-1399). We could also use:
- 130-139 (hundreds-tens boundary)
- 13 (tens-ones, i.e., numbers ending in 13 or containing 13 in last two digits)
- Larger: 13000-13999, etc.

For the 130-139 range: $n + ka \in [130, 139]$ for $k=1,...,9$.
- $n + a \geq 130 \Rightarrow n \geq 130 - a$
- $n + 9a \leq 139 \Rightarrow n \leq 139 - 9a$
- $n + 10a > 139 \Rightarrow n \geq 140 - 10a$
- $n < 130$

Overlap: $\max(130-a, 140-10a) \leq n \leq \min(129, 139-9a)$.
$139 - 9a \geq 130 - a \Rightarrow 9 \geq 8a \Rightarrow a \leq 1$.
$129 \geq 140 - 10a \Rightarrow 10a \geq 11 \Rightarrow a \geq 2$.

Contradiction! So $a \leq 1$ and $a \geq 2$ can't both hold. So this range doesn't work with the simple boundary approach.

Hmm, but maybe the "13" doesn't have to be at the same position for all $k$. Let me reconsider.

Actually, for the 130-139 range, the issue is that the range [130, 139] has only 10 numbers, and we need 9 consecutive multiples to fall in it, plus the endpoints outside. The spread is $10a$ and the range is only 10 wide, so $10a \leq 10$ roughly, meaning $a = 1$. But then $n+10a = n+10$ must be $> 139$, so $n \geq 130$, but $n < 130$. Contradiction.

So for the 130-139 range, we can't fit 9 values inside and both endpoints outside.

What about using "13" in the last two digits? A number ends in "13" if it's $\equiv 13 \pmod{100}$. But we need 9 consecutive values $n+a, \ldots, n+9a$ to all be feared. If they all end in 13, then $a \equiv 0 \pmod{100}$, impossible.

But "13" could appear in other positions too. For example, a number like 213, 313, 413, etc. contains "13" in the middle.

Let me think about smaller $n$ more carefully. We need $n < 1290$ potentially.

Let me think about what other ranges could work. The "13" substring can appear at various positions. Let me think about numbers below 1290.

For $n < 100$: The numbers $n, n+a, \ldots, n+10a$ are all at most $99 + 990 = 1089$. Actually $n + 10a < 100 + 990 = 1090$. So they're at most 3 digits (or barely 4 digits).

For $n$ in range [0, 129], the feared numbers in this range are: 13, 113, 130-139. Wait, 113 contains "13"? "113" - yes, "13" appears at positions 1,0 (the "13" in "113"). Actually "113" = digits 1,1,3. The substring "13" would need consecutive digits 1,3. In "113", we have "11" and "13" - yes, "13" appears (the last two digits are "13"). So 113 is feared.

Numbers containing "13" below 130: 13, 113. And 130-139.

For small $n$, let me think about what ranges of feared numbers exist.

Feared numbers (containing "13") up to ~1400:
- 13
- 113
- 130-139
- 213
- 313
- 413
- 513
- 613
- 713
- 813
- 913
- 1013, 1113
- 1130-1139
- 1213
- 1300-1399

So the feared numbers form clusters. For our problem, we need 9 consecutive terms of an AP to all be feared, with the 0th and 10th terms fearless.

The largest cluster is 1300-1399 (100 numbers). The next largest is 130-139 (10 numbers) and 1130-1139 (10 numbers).

For 1300-1399: we found $n = 1290, a = 11$.

For 1130-1139: similar analysis. $n + ka \in [1130, 1139]$ for $k=1,...,9$.
- $n + a \geq 1130 \Rightarrow n \geq 1130 - a$
- $n + 9a \leq 1139 \Rightarrow n \leq 1139 - 9a$
- $n + 10a > 1139 \Rightarrow n \geq 1140 - 10a$
- $n < 1130$

$\max(1130-a, 1140-10a) \leq n \leq \min(1129, 1139-9a)$.
$1139 - 9a \geq 1130 - a \Rightarrow 9 \geq 8a \Rightarrow a \leq 1$.
$1129 \geq 1140 - 10a \Rightarrow 10a \geq 11 \Rightarrow a \geq 2$.
Contradiction again. So 1130-1139 doesn't work with this simple approach.

What about combining multiple clusters? The "13" doesn't have to be at the same position for all $k$. For example, some $n+ka$ could be feared because they're in 130-139, and others because they end in 13, etc.

Let me think about this more creatively. We need 9 values $n+a, \ldots, n+9a$ to each contain "13" somewhere, but the position can vary.

Let me think about $a = 100$. No, $a < 100$.

Let me think about $a = 50$. Then $n, n+50, n+100, \ldots, n+500$. The spread is 500. We need $n+50, n+100, \ldots, n+450$ all feared, and $n, n+500$ fearless.

Hmm, this is getting complex. Let me think about whether we can beat 1290.

Let me think about the structure differently. We need a "gap" in fearless numbers. Specifically, we need 9 consecutive AP terms (with step $a$) to all be feared, bracketed by two fearless terms.

The fearless numbers are those NOT containing "13". The density of fearless numbers among $k$-digit numbers can be computed, but let me think about specific gaps.

The largest contiguous block of feared numbers below 1300 is 130-139 (10 numbers). Can we use this?

For the block 130-139 (10 feared numbers), we need $n+a, \ldots, n+9a$ to all be in this block (or feared for other reasons), with $n$ and $n+10a$ fearless.

If all 9 are in [130, 139]: as computed, this requires $a \leq 1$ and $a \geq 2$, impossible.

But what if some of the 9 are in [130, 139] and others are feared for different reasons?

For example, with $a = 1$: $n, n+1, \ldots, n+10$. We need $n+1, \ldots, n+9$ feared, $n$ and $n+10$ fearless. This means 9 consecutive integers are feared, bracketed by fearless. The longest run of consecutive feared numbers is 10 (130-139, 1130-1139, etc.). So we need 9 consecutive feared with fearless on both sides.

130-139: 130 is feared (starts with 13), 139 is feared. What about 129? "129" - fearless. 140? "140" - fearless. So 129 is fearless, 130-139 are feared (10 numbers), 140 is fearless.

With $a = 1$: $n = 129$, then $n+1 = 130, \ldots, n+9 = 138$ are all feared, $n+10 = 139$ is also feared. But we need $n+10$ to be fearless! 139 is feared. So this doesn't work.

$n = 130$: $n$ is feared. Doesn't work.

What about $n = 129, a = 1$: $n+10 = 139$ which is feared. ✗.

$n = 130, a = 1$: $n$ is feared. ✗.

Hmm. With $a = 1$, we need exactly 9 consecutive feared numbers with fearless on both sides. The block 130-139 has 10 feared numbers. So $n = 129$: $n+1=130$ to $n+9=138$ feared, $n+10=139$ feared. ✗. $n=130$: $n$ feared. ✗.

Is there a block of exactly 9 feared numbers? Or a block where we can pick 9 with fearless neighbors?

Actually, we need $n+1$ through $n+9$ feared (9 numbers) and $n, n+10$ fearless. So we need a run of at least 9 feared numbers, and the number just before and just after must be fearless.

Block 130-139 (10 feared): The number before (129) is fearless, the number after (140) is fearless. But the block has 10 feared numbers. We need 9 consecutive feared with fearless on both sides. 

If we take $n+1 = 130, \ldots, n+9 = 138$: $n = 129$ (fearless ✓), $n+10 = 139$ (feared ✗).
If we take $n+1 = 131, \ldots, n+9 = 139$: $n = 130$ (feared ✗), $n+10 = 140$ (fearless ✓).

Neither works because the block is 10 long, not 9.

What about the block 1130-1139? Same issue - 10 feared numbers.

What about other blocks? Let me look for blocks of feared numbers that are exactly 9 long, or where we can find 9 consecutive feared with fearless neighbors.

Actually, let me reconsider. Maybe the "13" appears at different positions for different terms, not all in the same block.

Let me think about $a = 1$ more carefully. We need 9 consecutive integers $n+1, \ldots, n+9$ all feared, with $n$ and $n+10$ fearless.

The feared numbers up to 200: 13, 113, 130-139.
So: ..., 112 (fearless), 113 (feared), 114 (fearless), ..., 129 (fearless), 130-139 (feared), 140 (fearless), ...

There's no run of 9 consecutive feared numbers with $a=1$ except possibly in the 130-139 block, but that's 10 long.

What about combining? E.g., 113 is feared, 114-129 are fearless, 130-139 are feared. No run of 9.

So $a = 1$ doesn't seem to work for small $n$.

Let me try $a = 2$. We need $n+2, n+4, \ldots, n+18$ all feared, $n$ and $n+20$ fearless.

Hmm, this is getting complicated. Let me think about it differently.

Actually, let me reconsider the 1300-1399 approach but see if we can get a smaller $n$ using a different cluster or combination.

What about using the cluster around 1130-1139 combined with 1213?

Let me think about $a = 100 - 1 = 99$. Then $n, n+99, n+198, \ldots, n+990$. The spread is 990.

Hmm, let me think about this differently. Let me consider what happens with various $a$ values and try to find the minimum $n$.

Actually, let me reconsider. The answer $n = 1290$ might not be minimal. Let me think about whether there's a smaller $n$ using a different approach.

Key insight: The "13" can appear at any position in the number. For different values of $k$, the "13" might appear at different positions.

Let me think about numbers around 1130. The feared numbers near 1130:
- 1113 (contains "13" at end)
- 1130-1139 (contains "13" at hundreds-tens)
- 1213 (contains "13" at end)

What about $a = 11$? Then $n, n+11, n+22, \ldots, n+110$.
If $n = 1119$: $n+11 = 1130$ (feared), $n+22 = 1141$ (fearless? "1141" - no "13" - fearless). ✗.

If $n = 1129$: $n+11 = 1140$ (fearless). ✗.

Hmm, the 1130-1139 block is only 10 numbers wide, and with $a = 11$, we can only fit one term in it.

Let me think about combining the 1113 and 1130-1139 clusters.

With $a = 17$: $n = 1096$. $n+17 = 1113$ (feared), $n+34 = 1130$ (feared), $n+51 = 1147$ (fearless). ✗.

This approach of combining clusters seems hard because the clusters are far apart relative to $a$.

Let me think about a completely different approach. What if "13" appears in the last two digits for some terms and in other positions for other terms?

A number ends in "13" if it's $\equiv 13 \pmod{100}$. So $n + ka \equiv 13 \pmod{100}$ for some specific $k$.

For different $k$ values, $n + ka \pmod{100}$ takes different values (since $a \not\equiv 0 \pmod{100}$ for $a < 100$). So at most one or two values of $k$ give $n + ka \equiv 13 \pmod{100}$.

Similarly, $n + ka \equiv 113 \pmod{1000}$ (i.e., last 3 digits are 113, which contains "13") for at most one $k$.

This is getting complex. Let me try to be more systematic and think about what values of $n < 1290$ could work.

Let me think about the problem from the perspective of digit carrying. When we add $ka$ to $n$, carries propagate. The "13" pattern needs to appear somewhere.

Let me consider the approach where "13" appears at the hundreds-tens position (i.e., the number mod 1000 is in [130, 139]) or at the thousands-hundreds position (mod 10000 in [1300, 1399]) etc.

For the 130-139 block (mod 1000): As computed, we can't fit 9 AP terms in a 10-wide block with $a \geq 2$ and have endpoints outside. With $a = 1$, the block is 10 wide but we need endpoints outside, giving 9 inside, but the endpoints fall inside the block.

Wait, let me recheck. With $a = 1$ and the block [130, 139]:
- $n + 1 = 130, \ldots, n + 9 = 138$: $n = 129$, $n + 10 = 139$ (feared). ✗.
- $n + 1 = 131, \ldots, n + 9 = 139$: $n = 130$ (feared). ✗.

So indeed $a = 1$ doesn't work with this block because the block is 10 wide and we need the 10th term to be outside.

But what if some terms are feared for OTHER reasons, not because they're in [130, 139]?

For example, with $a = 1$: $n = 112$. $n+1 = 113$ (feared, "113" contains "13"). $n+2 = 114$ (fearless). ✗.

What about combining 113 and 130-139? These are 17 apart, so with $a = 1$ they can't both be covered.

OK let me try a different approach. Let me think about what $a$ values could give $n < 1290$.

For $n < 1300$, the feared numbers are scattered. The main clusters are:
- 13 (single)
- 113 (single)
- 130-139 (block of 10)
- 213, 313, 413, 513, 613, 713, 813, 913 (singles, each 100 apart)
- 1013, 1113 (singles)
- 1130-1139 (block of 10)
- 1213 (single)

For $n < 1300$, we need 9 AP terms (step $a$) to all be feared. The AP terms are $n+a, n+2a, \ldots, n+9a$.

The singles (like 213, 313, ...) are 100 apart. If $a = 100$, we could hit 213, 313, 413, ..., 913 - that's 8 values. But $a < 100$, so $a = 100$ is not allowed. With $a = 99$: $n + 99, n + 198, \ldots, n + 891$. These are 99 apart. 213, 312, 411, ... - no, 312 doesn't contain "13".

Hmm. Let me think about $a$ values that align with the spacing of feared numbers.

The singles 213, 313, 413, ..., 913 are 100 apart. With $a$ close to 100, we might hit several of these, but they won't be exactly aligned unless $a = 100$.

What about $a = 100 - 1 = 99$? Then $n + 99k$. If $n + 99 = 213$, then $n = 114$. $n + 198 = 312$ (fearless). ✗.

$a = 100 + 1 = 101$? No, $a < 100$.

What about $a = 50$? $n + 50k$. The feared numbers at positions 50 apart... 113, 163 (fearless), 213 (feared), 263 (fearless)... doesn't work.

Let me try to think about this more carefully. For $n < 1290$, we need to find $a < 100$ such that $n + a, \ldots, n + 9a$ are all feared. The spread is $9a < 900$.

For $n$ around 1000-1290, the feared numbers in this range are:
- 1013, 1113, 1130-1139, 1213.

That's very sparse. 1013, 1113 are 100 apart. 1113, 1130 are 17 apart. 1130-1139 is a block. 1213 is separate.

For 9 AP terms to all be feared in this range, we'd need them to all fall on these sparse feared numbers. Seems very unlikely unless $a$ is very small and they all fall in the 1130-1139 block, which we showed doesn't work.

For $n$ around 130-139: same issue as before.

For $n$ around 200-900: feared numbers are 213, 313, 413, 513, 613, 713, 813, 913. These are 100 apart. With $a < 100$, we can't hit more than one or two of these.

Wait, but what about numbers like 130-139? If $n$ is around 130, the spread $9a$ could reach up to $130 + 9 \cdot 99 = 130 + 891 = 1021$. So the AP terms could span from ~130 to ~1021, hitting feared numbers at various positions.

Let me think about this. With $a = 100 - 13 = 87$? Or some other value.

Actually, let me think about it differently. Let me consider $a$ such that $n + ka$ hits feared numbers for $k = 1, \ldots, 9$.

The feared numbers below 1300 are: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

Let me list them more carefully:
- 13
- 113
- 130, 131, 132, 133, 134, 135, 136, 137, 138, 139
- 213
- 313
- 413
- 513
- 613
- 713
- 813
- 913
- 1013
- 1113
- 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139
- 1213

Now, for an AP with step $a$, we need 9 consecutive terms to be feared. Let me see if there's an AP that hits 9 of these.

The numbers 213, 313, 413, 513, 613, 713, 813, 913 are 100 apart. An AP with $a = 100$ would hit all 8, but $a < 100$.

What if we use $a = 100$? Not allowed. $a = 99$?

With $a = 99$: if $n + 99 = 213$, then $n = 114$. The terms are:
- $n + 99 = 213$ (feared ✓)
- $n + 198 = 312$ (fearless ✗)

Doesn't work.

What about $a = 100$? Not allowed.

Hmm, let me think about whether the "13" could appear in a different way. For example, 1313 contains "13" twice. 1300-1399 all contain "13". 

What if we use a combination where some terms are in [130, 139] and others are in [1300, 1399]? But the spread would need to be at least 1161, requiring $9a \geq 1161$, so $a \geq 130$, but $a < 100$. Impossible.

What about terms in [130, 139] and [1130, 1139]? Spread $\geq 991$, $a \geq 111$. Impossible.

OK so for $n < 1300$, it seems very hard to get 9 feared terms. Let me reconsider.

What about $n$ slightly less than 1300, like $n = 1290$? We already found this works with $a = 11$.

Can we do better? Let me check $n$ values from 1200 to 1290.

For $n$ in [1200, 1299], $n + 10a < 1300 + 990 = 2290$. The feared numbers in [1200, 2290]:
- 1213
- 1300-1399
- 1413
- 1513
- 1613
- 1713
- 1813
- 1913
- 2013
- 2113
- 2130-2139
- 2213

The block 1300-1399 is the big one. For $n$ in [1200, 1299], if we use $a$ such that $n + a, \ldots, n + 9a$ all fall in [1300, 1399], we need:
- $n + a \geq 1300$
- $n + 9a \leq 1399$
- $n + 10a > 1399$ (or $n + 10a$ is fearless for another reason)
- $n < 1300$

From $n + a \geq 1300$ and $n < 1300$: $a > 0$ (always true) and $n \geq 1300 - a$.
From $n + 9a \leq 1399$: $n \leq 1399 - 9a$.
From $n + 10a > 1399$: $n > 1399 - 10a$, i.e., $n \geq 1400 - 10a$.

So $n \in [\max(1300 - a, 1400 - 10a), \min(1299, 1399 - 9a)]$.

For this to be non-empty:
1. $1300 - a \leq 1299 \Rightarrow a \geq 1$ ✓
2. $1400 - 10a \leq 1299 \Rightarrow 10a \geq 101 \Rightarrow a \geq 11$
3. $1300 - a \leq 1399 - 9a \Rightarrow 8a \leq 99 \Rightarrow a \leq 12$
4. $1400 - 10a \leq 1399 - 9a \Rightarrow a \geq 1$ ✓

So $a \in \{11, 12\}$.

For $a = 11$: $n \in [\max(1289, 1290), \min(1299, 1300)] = [1290, 1299]$.
For $a = 12$: $n \in [\max(1288, 1280), \min(1299, 1291)] = [1288, 1291]$.

For $a = 12$, $n = 1288$: $n + 12 = 1300$ (feared), ..., $n + 108 = 1396$ (feared), $n + 120 = 1408$ (fearless? "1408" - no "13" - fearless ✓). $n = 1288$ (fearless ✓).

So $n = 1288$ works with $a = 12$! That's smaller than 1290.

Let me verify $n = 1288, a = 12$:
- $n = 1288$: "1288", no "13" → fearless ✓
- $n + 12 = 1300$: "1300", contains "13" → feared ✓
- $n + 24 = 1312$: "1312", contains "13" → feared ✓
- $n + 36 = 1324$: "1324", contains "13" → feared ✓
- $n + 48 = 1336$: "1336", contains "13" → feared ✓
- $n + 60 = 1348$: "1348", contains "13" → feared ✓
- $n + 72 = 1360$: "1360", contains "13" → feared ✓
- $n + 84 = 1372$: "1372", contains "13" → feared ✓
- $n + 96 = 1384$: "1384", contains "13" → feared ✓
- $n + 108 = 1396$: "1396", contains "13" → feared ✓
- $n + 120 = 1408$: "1408", no "13" → fearless ✓

All checks pass. $n = 1288$ works.

Can we do even better? For $a = 12$, $n = 1288$ is the minimum in that range. For $a = 11$, $n = 1290$ is the minimum.

But maybe there are other approaches that give smaller $n$?

Let me think about whether we can use a different block of feared numbers. What about the block 130-139?

For the block [130, 139] with the same approach:
- $n + a \geq 130$, $n + 9a \leq 139$, $n + 10a > 139$, $n < 130$.
- $n \in [\max(130-a, 140-10a), \min(129, 139-9a)]$.
- Need $140 - 10a \leq 129 \Rightarrow a \geq 2$ and $130 - a \leq 139 - 9a \Rightarrow 8a \leq 9 \Rightarrow a \leq 1$.
- Contradiction. So this doesn't work.

What about using the block [130, 139] but allowing $n + 10a$ to be in the block (and feared for a different reason)? No, $n + 10a$ must be fearless.

What about using a block of feared numbers that's wider? The only wide blocks are [130, 139], [1130, 1139], [1300, 1399], [2130, 2139], etc. The 1300-1399 block is the first one wide enough.

Wait, but what about combining multiple sources of "13"? For example, some terms could be feared because they're in [130, 139], and others because they end in "13" (like 213, 313, etc.), and others because they're in [1300, 1399].

Let me think about this. For $n$ around 130, with a large enough $a$, the AP could span from ~130 to ~1300, hitting feared numbers at various positions.

For example, $a = 130$. No, $a < 100$.

$a = 99$: $n + 99k$ for $k = 1, \ldots, 9$. Spread = 891. If $n = 130 - 99 = 31$, then:
- $n + 99 = 130$ (feared ✓)
- $n + 198 = 229$ (fearless ✗)

Doesn't work.

$a = 100 - 1 = 99$: The terms would be roughly 100 apart, but not exactly hitting the feared singles.

Let me try $a = 100 - 13 = 87$. If $n + 87 = 130$, $n = 43$.
- $n + 87 = 130$ (feared ✓)
- $n + 174 = 217$ (fearless ✗)

$a = 100$: not allowed.

Hmm, the problem is that the feared singles (213, 313, ...) are exactly 100 apart, and we need $a < 100$, so we can't hit them all.

What if we use a different set of feared numbers? Let me think about numbers containing "13" that are closer together.

In the range [1300, 1399], all 100 numbers are feared. That's the key. And we showed the minimum $n$ using this block is 1288.

But what about using the block [130, 139] (10 numbers) combined with other feared numbers?

For $n$ slightly below 130, with $a$ such that some terms fall in [130, 139] and others fall on feared singles.

Let me try $a = 100 - 1 = 99$. If $n + 99 = 130$, $n = 31$.
- $n = 31$ (fearless ✓)
- $n + 99 = 130$ (feared ✓)
- $n + 198 = 229$ (fearless ✗)

No. The gap between 139 and 213 is 74, and between 213 and 313 is 100. With $a = 99$, we can't hit both 130-139 and 213.

Let me try $a = 83$. If $n + 83 = 130$, $n = 47$.
- $n + 83 = 130$ (feared ✓)
- $n + 166 = 213$ (feared ✓)
- $n + 249 = 296$ (fearless ✗)

$a = 83$ hits 130 and 213 (83 apart), but then 296 is fearless.

What about $a = 100$? Not allowed. The fundamental issue is that the feared singles are 100 apart and we need $a < 100$.

Let me try to find $a$ such that the AP hits multiple feared numbers that aren't 100 apart.

Feared numbers and their differences:
- 13 to 113: 100
- 113 to 130: 17
- 130 to 139: consecutive
- 139 to 213: 74
- 213 to 313: 100
- 313 to 413: 100
- ...

The differences are mostly 100, except around the blocks. So with $a < 100$, we can hit at most 2-3 feared numbers that are in the blocks, but not 9.

What about using the block [130, 139] more creatively? The block has 10 numbers. With $a = 1$, we can hit all 10, but we need the 10th term ($n + 10$) to be fearless, and the block is exactly 10 wide, so $n + 10$ would be 140 (fearless) only if $n + 1 = 131, \ldots, n + 9 = 139$, but then $n = 130$ (feared). Or $n + 1 = 130, \ldots, n + 9 = 138$, $n + 10 = 139$ (feared). Neither works.

With $a = 2$: we can hit 5 numbers in [130, 139] (every other one). Not enough.

What about $a = 1$ but using a different block? Is there a block of exactly 9 feared numbers with fearless on both sides?

The blocks are all 10 wide (130-139, 1130-1139, 1300-1399 is 100 wide, 2130-2139, etc.).

For a 10-wide block with $a = 1$: we need 9 consecutive in the block, with the term before and after being fearless. But the term before the block is fearless and the term after is fearless. So if we take 9 from the 10-wide block:
- Take 130-138 (9 numbers): $n = 129$ (fearless ✓), $n + 10 = 139$ (feared ✗).
- Take 131-139 (9 numbers): $n = 130$ (feared ✗), $n + 10 = 140$ (fearless ✓).

Neither works because one endpoint falls inside the block.

What if there's a number just outside the block that's also feared? For example, is 129 feared? "129" - no "13" - fearless. Is 140 feared? "140" - no "13" - fearless. So no.

What about 1129? "1129" - no "13" - fearless. 1140? "1140" - no "13" - fearless.

Hmm, so the 10-wide blocks don't work with $a = 1$.

What about the 100-wide block [1300, 1399] with $a = 1$? We need 9 consecutive in [1300, 1399] with $n$ and $n + 10$ fearless. Since the block is 100 wide, there's plenty of room.

$n = 1299$ (fearless? "1299" - no "13" - fearless ✓). $n + 1 = 1300, \ldots, n + 9 = 1308$ (all feared ✓). $n + 10 = 1309$ (feared ✗).

$n = 1290$ (fearless ✓). $n + 1 = 1291$ (fearless ✗).

So with $a = 1$, we need $n + 1$ through $n + 9$ all in [1300, 1399], and $n, n + 10$ outside (and fearless). $n + 1 \geq 1300 \Rightarrow n \geq 1299$. $n + 9 \leq 1399 \Rightarrow n \leq 1390$. $n + 10 > 1399 \Rightarrow n \geq 1390$. So $n = 1390$: $n + 10 = 1400$ (fearless ✓). But $n = 1390$ is feared! ✗.

$n = 1390$: "1390" contains "13" → feared. ✗.

So with $a = 1$ and the block [1300, 1399], $n$ must be $\geq 1299$ and $\leq 1390$ and $\geq 1390$, so $n = 1390$, which is feared. Doesn't work.

Actually wait, I need $n$ to be fearless AND $n < 1300$ (or $n \geq 1400$ but then $n + 1 \geq 1401$ which is outside the block). So $n < 1300$ and $n + 1 \geq 1300$, giving $n = 1299$. Then $n + 10 = 1309$ (feared). ✗.

So $a = 1$ doesn't work with this block either.

OK so let me go back to $a = 12, n = 1288$ and see if we can find anything smaller.

Let me think about whether there's a completely different approach. What if the "13" appears in a higher position?

For example, numbers like 13000-13999. But $n$ would need to be around 13000, which is much larger than 1288.

What about 4-digit numbers where "13" appears in the middle, like X13Y? For example, 2130-2139, 1130-1139, etc. We already considered 1130-1139.

Let me reconsider 1130-1139. The block is 10 wide. With $a = 1$: same issue as before (10-wide block, need 9 inside with endpoints outside).

But what if we combine 1113 (feared) with 1130-1139 (feared)? 1113 and 1130 are 17 apart. With $a = 17$:
- $n + 17 = 1113 \Rightarrow n = 1096$
- $n + 34 = 1130$ (feared ✓)
- $n + 51 = 1147$ (fearless ✗)

Only 2 terms. Not enough.

What about $a = 1$ and using the range [1113, 1139]? The feared numbers in this range: 1113, 1130-1139. That's 1113, then a gap (1114-1129 fearless), then 1130-1139. Not 9 consecutive.

Hmm. Let me think about whether there are other blocks of feared numbers I'm missing.

What about numbers like 13000? No, too large.

What about 2-digit numbers? Only 13 is feared. Not enough.

What about 3-digit numbers? 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913. The only block is 130-139 (10 numbers).

What about numbers where "13" appears not at a "natural" boundary? Like 413 - the "13" is in the last two digits. Or 1301 - the "13" is in the first two digits. Or 2130 - "13" in the middle.

I think I've been comprehensive. The blocks of consecutive feared numbers are:
- 130-139 (10)
- 1130-1139 (10)
- 1300-1399 (100)
- 2130-2139 (10)
- 13130-13139 (10) [but this is within 13000-13999 which is all feared]
- etc.

And the singles (numbers with "13" not in a block): 13, 113, 213, 313, ..., 1213, 1413, etc.

For 9 AP terms to all be feared, the most promising approach is the 100-wide block [1300, 1399], which gives $n = 1288$.

But wait, can we use the block [1300, 1399] with a different $a$ to get a smaller $n$?

We need $n + a \geq 1300$ and $n + 9a \leq 1399$ and $n + 10a > 1399$ (or $n + 10a$ fearless for another reason) and $n < 1300$ and $n$ fearless.

What if $n + 10a$ is in [1300, 1399] but fearless? No, all numbers in [1300, 1399] contain "13", so they're all feared.

What if $n + 10a \leq 1399$ but $n + 10a$ is fearless? Impossible since all numbers in [1300, 1399] are feared.

So we need $n + 10a \geq 1400$ or $n + 10a < 1300$. Since $n + 10a > n + 9a \geq n + a \geq 1300$, we need $n + 10a \geq 1400$.

Also, what if $n + 10a \geq 1400$ but contains "13"? Like 1413. Then $n + 10a$ would be feared, which is bad.

$n + 10a \in [1400, 1400 + 10a - 1]$ roughly. For $a = 12$, $n + 10a = n + 120 \in [1408, 1411]$ (for $n \in [1288, 1291]$). Let me check: 1408, 1409, 1410, 1411 - none contain "13". ✓.

For $a = 11$, $n + 10a = n + 110 \in [1400, 1409]$ (for $n \in [1290, 1299]$). 1400-1409: none contain "13". ✓.

Now, can we use $a = 13$? Then $n + 13 \geq 1300 \Rightarrow n \geq 1287$. $n + 117 \leq 1399 \Rightarrow n \leq 1282$. But $1287 > 1282$, contradiction. So $a = 13$ doesn't work (the block isn't wide enough: $9 \times 13 = 117 > 99$).

For $a = 12$: $9 \times 12 = 108 < 100$? No, $108 > 99$. Wait, the block is 100 wide (1300 to 1399 inclusive, that's 100 numbers). $9a = 108 > 99$. So $n + 9a - (n + a) = 8a = 96 \leq 99$. ✓. The condition is $8a \leq 99$, i.e., $a \leq 12$.

For $a = 12$: $n \in [1288, 1291]$. Minimum $n = 1288$.
For $a = 11$: $n \in [1290, 1299]$. Minimum $n = 1290$.

So $a = 12$ gives the smallest $n = 1288$ from this block.

Now, can we use a different approach entirely to get $n < 1288$?

Let me think about using the block [130, 139] combined with other feared numbers, with a carefully chosen $a$.

The idea: some of the 9 terms $n + a, \ldots, n + 9a$ are in [130, 139], and others are feared singles like 213, 313, etc.

For a term to be in [130, 139]: $n + ka \in [130, 139]$.
For a term to be a feared single: $n + ka \in \{13, 113, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1213\}$.

The singles are roughly 100 apart. If $a \approx 100$, we could hit multiple singles. But $a < 100$.

Let me try $a = 99$. The AP terms are $n + 99, n + 198, \ldots, n + 891$.

If $n + 99 = 130$, $n = 31$. Terms: 130, 229, 328, 427, 526, 625, 724, 823, 922. Only 130 is feared. ✗.

If $n + 99 = 213$, $n = 114$. Terms: 213, 312, 411, 510, 609, 708, 807, 906, 1005. Only 213 is feared. ✗.

The problem is that with $a = 99$, consecutive terms are 99 apart, and the feared singles are 100 apart, so we miss them.

What about $a = 100 - 1 = 99$ but starting from a different point? The feared singles are at 213, 313, 413, ..., 913 (100 apart). With $a = 99$, the terms drift by 1 each step. So if the first term is 213, the next is 312 (off by 1 from 313). If the first is 214, it's not feared. 

What if we use $a = 100$? Not allowed.

What about $a = 50$? Terms are 50 apart. Feared numbers 50 apart? 113 and 163 (not feared). 130 and 180 (not feared). 213 and 263 (not feared). Doesn't seem to work.

What about $a = 25$? 113, 138 (feared, in [130,139]), 163 (not feared). Only 2.

$a = 17$? 113, 130 (feared), 147 (not feared). Only 2.

$a = 83$? 130, 213 (feared), 296 (not). Only 2.

$a = 74$? 139, 213 (feared), 287 (not). Only 2.

Hmm, it seems really hard to get 9 feared terms without using a wide block.

Let me try yet another approach. What if we use the block [1130, 1139] (10 wide) with a small $a$, and some terms are also feared because they contain "13" elsewhere?

With $a = 1$: terms $n+1, \ldots, n+9$ in [1130, 1138] or [1131, 1139]. As before, one endpoint falls in the block.

But what if $n + 10$ is feared for a DIFFERENT reason? We need $n + 10$ to be fearless, not feared. So this doesn't help.

What if $n$ is feared for a different reason? We need $n$ to be fearless. So this doesn't help either.

What if some terms outside the [1130, 1139] block are feared for other reasons? For example, with $a = 1$ and $n = 1112$: $n + 1 = 1113$ (feared), $n + 2 = 1114$ (fearless). ✗.

With $a = 1$ and $n = 1129$: $n + 1 = 1130, \ldots, n + 9 = 1138$ (all feared), $n + 10 = 1139$ (feared). ✗.

With $a = 1$ and $n = 1130$: $n$ is feared. ✗.

So $a = 1$ doesn't work with the 1130-1139 block.

What about $a = 2$ with the 1130-1139 block? We need 9 terms ($n+2, n+4, \ldots, n+18$) all feared. The block has 10 numbers, and with step 2, we can hit at most 5 of them. The other 4 need to be feared for other reasons. The nearest other feared numbers are 1113 (17 below 1130) and 1213 (74 above 1139). With $a = 2$, the terms outside the block would be at most 18 away from the block, so they'd be in [1112, 1129] or [1140, 1157]. In [1112, 1129], only 1113 is feared. In [1140, 1157], none are feared. So at most 1 additional feared number. Total: 5 + 1 = 6 < 9. ✗.

What about $a = 3$? Similar analysis. Block hits at most 4, plus maybe 1113. Not enough.

I'm becoming more convinced that 1288 is the answer, but let me think about whether there's a cleverer approach.

What about using TWO blocks? Like [130, 139] and [1130, 1139]? They're 1000 apart. With $a \approx 125$, we could have some terms in each block. But $a < 100$, so the spread $9a < 900 < 1000$. Can't reach both blocks.

What about [130, 139] and [1300, 1399]? They're about 1160-1270 apart. $9a < 900$. Can't reach both.

What about using the block [1300, 1399] but with $n$ much smaller, and some terms before the block are feared for other reasons?

For example, $n = 1200, a = 12$. Terms: 1212, 1224, 1236, 1248, 1260, 1272, 1284, 1296, 1308. Only 1308 is in [1300, 1399]. The rest: 1212 (fearless), 1224 (fearless), etc. ✗.

For $n = 1200, a = 13$. Terms: 1213 (feared ✓), 1226 (fearless ✗).

$n = 1200, a = 100$: not allowed.

Hmm. What if $a$ is chosen so that multiple terms land on feared singles AND in the block?

The feared singles near 1300: 1213, 1313 (but 1313 is in [1300, 1399], so it's already counted).

Actually, 1213 is the last feared single before 1300. The next is 1413 (after 1399).

So for $n < 1300$, the only feared numbers near 1300 are 1213 and then the block [1300, 1399].

If we want some terms to be 1213 and others in [1300, 1399]:
$1213 + a \approx 1300 \Rightarrow a \approx 87$.
With $a = 87$: $n + 87 = 1213 \Rightarrow n = 1126$. Terms: 1213 (feared), 1300 (feared), 1387 (feared), 1474 (fearless). Only 3 feared. ✗.

With $a = 87$ and $n + 87 = 1213$: $n = 1126$. Terms: 1213, 1300, 1387, 1474, 1561, 1648, 1735, 1822, 1909. Feared: 1213 ✓, 1300 ✓, 1387 ✓, 1474 ✗. Only 3.

What about $a = 87$ and starting differently? $n + 87 = 1300 \Rightarrow n = 1213$ (feared). ✗.

I don't think combining singles with the block works well because the singles are too sparse.

Let me try another approach: what if "13" appears in a different position, like the ten-thousands position?

For 5-digit numbers: 13000-13999 (10000 numbers, all feared). But $n$ would be around 13000, much larger than 1288.

What about 4-digit numbers where "13" appears in the middle two digits? Like X13Y where X ≠ 0. These are 2130-2139, 1130-1139, 3130-3139, etc. Wait, no. X13Y means the number is X*1000 + 130 + Y = X*1000 + 13Y. For X=1: 1130-1139. For X=2: 2130-2139. Etc.

We already considered 1130-1139. The next is 2130-2139, which would give $n \approx 2128$, much larger.

What about numbers where "13" appears in the last two digits? These are numbers ending in 13: 13, 113, 213, 313, ..., 1213, 1313, 1413, etc. These are 100 apart.

And numbers where "13" appears in the first two digits of a 4-digit number: 1300-1399 (all 100 of them).

I think 1288 is likely the answer. But let me also check: can we use the block [1300, 1399] with $n < 1288$ by having $n + 10a$ be outside [1400, ...) and fearless, while $n + 10a < 1400$?

We need $n + 10a$ to be fearless and $n + 10a \leq 1399$. But all numbers in [1300, 1399] are feared. So $n + 10a \leq 1299$ or $n + 10a \geq 1400$.

If $n + 10a \leq 1299$: then $n + 9a < n + 10a \leq 1299 < 1300$, so $n + 9a < 1300$, meaning $n + 9a$ is not in [1300, 1399]. But we need $n + 9a$ to be feared. So $n + 9a$ must be feared for another reason. The nearest feared number below 1300 is 1213. So $n + 9a = 1213$ and $n + 10a \leq 1299$.

$n + 9a = 1213$ and $n + a \geq 1300$? That gives $n \geq 1300 - a$ and $n = 1213 - 9a$. So $1213 - 9a \geq 1300 - a \Rightarrow -87 \geq 8a \Rightarrow a \leq -11$. Impossible since $a > 0$.

So $n + 9a$ can't be below 1300 while $n + a \geq 1300$. So all 9 terms must be in [1300, 1399], and $n + 10a \geq 1400$.

This confirms: $n \in [1288, 1299]$ for $a \in \{11, 12\}$, with minimum $n = 1288$ at $a = 12$.

But wait, I should also check: can we have $n + 10a \geq 1400$ but $n + 10a$ is feared (contains "13")? Then it wouldn't work. Let me check for $a = 12, n = 1288$: $n + 120 = 1408$. "1408" - no "13" - fearless. ✓.

For $a = 12, n = 1289$: $n + 120 = 1409$. "1409" - no "13" - fearless. ✓.
For $a = 12, n = 1290$: $n + 120 = 1410$. "1410" - no "13" - fearless. ✓.
For $a = 12, n = 1291$: $n + 120 = 1411$. "1411" - no "13" - fearless. ✓.

All good. And $n = 1288$ is the minimum.

Now, let me also think about whether there might be a solution with $n < 1288$ using a completely different mechanism that I haven't considered.

What if the "13" appears due to carrying? For example, if $n = 1299$ and $a = 1$, then $n + 1 = 1300$ which has "13". But we already considered $a = 1$.

What if we use numbers where "13" appears in a non-standard way? Like 1300 has "13" at the start, 1130 has "13" in the middle, 1313 has "13" twice. I think I've covered all cases.

Let me also consider: what if $n$ is a 1-digit or 2-digit number? Then $n + 10a < 100 + 990 = 1090$. The feared numbers up to 1090: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013.

For 9 AP terms to all be feared: we need 9 of these to be in AP with common difference $a < 100$. The differences between consecutive feared numbers: 13→113: 100, 113→130: 17, 130→139: 1, 139→213: 74, 213→313: 100, etc.

For an AP with 9 terms, the differences between consecutive terms must all equal $a$. So we need 9 feared numbers in AP. The feared numbers up to 1090 are: 13, 113, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 213, 313, 413, 513, 613, 713, 813, 913, 1013.

An AP of 9 terms from these: the common difference must be constant. Looking at the list, the only AP-like sequences are:
- 130, 131, 132, ..., 139 (AP with $a = 1$, 10 terms)
- 213, 313, 413, 513, 613, 713, 813, 913 (AP with $a = 100$, 8 terms - but $a = 100$ not allowed)

With $a = 1$ and the 130-139 block: we need 9 terms, but the 10th term (either 129 or 140) must be fearless, and the other endpoint must also be fearless. As computed, this doesn't work because one of $n, n+10$ falls in the block.

So no solution with $n < 100$.

For $n < 1300$ in general: I've shown that the only AP of 9 feared numbers with $a < 100$ that works is using the block [1300, 1399], giving $n = 1288$.

Actually wait, I haven't fully explored all possibilities. Let me think about whether there could be an AP of 9 feared numbers with $a < 100$ that doesn't use a single block but combines multiple sources.

For example, could we have an AP where some terms are in [130, 139], some are singles like 213, 313, etc.?

The key constraint is that all 9 terms must be in AP with the same $a$. So the differences between consecutive terms are all $a$.

If one term is 130 and another is 213, then $a | (213 - 130) = 83$. So $a$ divides 83. Since 83 is prime, $a = 83$ or $a = 1$.

With $a = 83$: terms are $n + 83, n + 166, \ldots, n + 747$. If $n + 83 = 130$, terms are: 130, 213, 296, 379, 462, 545, 628, 711, 794. Feared: 130 ✓, 213 ✓, 296 ✗. Only 2.

If $n + 83 = 47$, terms: 130, 213, 296, ... same thing.

With $a = 1$: we need 9 consecutive feared numbers. The only runs of consecutive feared numbers are the blocks (130-139, 1130-1139, 1300-1399, etc.). We've shown these don't work with $a = 1$.

What about terms that are 100 apart (the singles)? $a = 100$ not allowed.

What about $a = 50$? Terms 50 apart. Feared numbers 50 apart? 113 and 163 (not feared). 130 and 180 (not). 213 and 263 (not). No.

$a = 25$? 113, 138 (feared), 163 (not). Only 2.

$a = 17$? 113, 130 (feared), 147 (not). Only 2.

$a = 74$? 139, 213 (feared), 287 (not). Only 2.

I really can't find any AP of 9 feared numbers with $a < 100$ other than using the [1300, 1399] block.

Let me also consider: what about using the block [1300, 1399] with a non-standard $a$ where not all 9 terms are in the block, but some are feared for other reasons?

For example, $a = 12, n = 1287$: $n + 12 = 1299$ (fearless ✗). Doesn't work.

$a = 12, n = 1288$: all 9 terms in [1300, 1399]. ✓. This is our solution.

$a = 13, n = 1287$: $n + 13 = 1300$ (feared), $n + 26 = 1313$ (feared), ..., $n + 117 = 1404$ (fearless). Wait, $n + 9 \times 13 = 1287 + 117 = 1404$. But 1404 is not in [1300, 1399]. Let me check: $n + 13 = 1300$, $n + 26 = 1313$, $n + 39 = 1326$, $n + 52 = 1339$, $n + 65 = 1352$, $n + 78 = 1365$, $n + 91 = 1378$, $n + 104 = 1391$, $n + 117 = 1404$. 

So $n + 9a = 1404$ which is outside [1300, 1399]. Is 1404 feared? "1404" - no "13" - fearless. ✗. So the 9th term is fearless. Doesn't work.

But wait, what if $n + 9a = 1391$ is feared (it's in [1300, 1399]) and $n + 10a = 1404$ is fearless? Let me recount. $n + ka$ for $k = 1, \ldots, 9$:
- $k=1$: 1300 (feared ✓)
- $k=2$: 1313 (feared ✓)
- $k=3$: 1326 (feared ✓)
- $k=4$: 1339 (feared ✓)
- $k=5$: 1352 (feared ✓)
- $k=6$: 1365 (feared ✓)
- $k=7$: 1378 (feared ✓)
- $k=8$: 1391 (feared ✓)
- $k=9$: 1404 (fearless ✗)

So $k=9$ gives 1404 which is fearless. We need all 9 to be feared. ✗.

So $a = 13$ doesn't work because $9 \times 13 = 117 > 99$, so the 9th term escapes the block.

This confirms $a \leq 12$ for the [1300, 1399] block, and $a = 12$ gives the minimum $n = 1288$.

Now let me also think about whether there's a solution with $n < 1288$ using the block [1300, 1399] but with $n + 10a$ being in [1300, 1399] and somehow fearless. But all numbers in [1300, 1399] contain "13", so none are fearless. So $n + 10a$ must be $\geq 1400$.

And $n$ must be $< 1300$ (if $n \geq 1300$, it's feared). Actually, $n$ could be $\geq 1400$ if $n$ is fearless, but then $n + a > n \geq 1400$, and we'd need $n + a, \ldots, n + 9a$ to be feared. The next block is [13000, 13999] which is way too far. Or we'd need to use singles, which we've shown don't work for 9 terms.

So $n < 1300$, and the minimum is $n = 1288$.

Actually, hold on. Let me reconsider. What if $n$ is between 1400 and 12999, and we use a different block or combination?

The next block after [1300, 1399] is [1130, 1139] (already considered, doesn't work) and [2130, 2139] (10 wide, same issue as [130, 139]).

What about [13130, 13139]? This is within [13000, 13999] which is all feared. But $n$ would be around 13000+, much larger than 1288.

What about using the block [1300, 1399] from above, i.e., $n$ slightly below 1300? We've found $n = 1288$.

I'm now fairly confident the answer is $n = 1288$. But let me do one more check: are there any feared numbers between 1288 and 1300 that I might be missing?

1288: "1288" - no "13" - fearless
1289: "1289" - no "13" - fearless
1290: "1290" - no "13" - fearless
...
1299: "1299" - no "13" - fearless

All fearless. Good.

And 1400-1411:
1400: "1400" - no "13" - fearless
...
1411: "1411" - no "13" - fearless

All fearless. Good.

So the answer is $n = 1288$.

Wait, actually I want to double-check one more thing. Let me make sure there's no solution with $n < 1288$ using a completely different approach that I might have missed.

What if we use numbers where "13" appears due to the interaction of different digit positions? For example, consider a number like 130. The "13" is in the hundreds-tens position. Or 1300, where "13" is in the thousands-hundreds position.

I've been considering blocks where "13" appears at a fixed position. But what if "13" appears at different positions for different terms?

For example, with $a = 87$:
- $n + 87 = 1130$ (feared, "13" at hundreds-tens)
- $n + 174 = 1217$ (fearless)

No, this doesn't help because the terms are too far apart to all be feared.

What about $a = 100 - 87 = 13$? We already checked $a = 13$ doesn't work with the [1300, 1399] block.

What about $a = 13$ with a different block? [130, 139]: $9 \times 13 = 117 > 9$ (block width is 10). Doesn't fit.

I think I've been thorough enough. Let me also consider whether there might be a solution using numbers in the 10000-13000 range with a smaller $n$... no, those are all larger than 1288.

Let me also consider: what if $n$ is very small, like $n = 1$, and $a$ is chosen carefully?

$n = 1, a = 12$: terms 13, 25, 37, 49, 61, 73, 85, 97, 109. Only 13 is feared. ✗.

$n = 1, a = 14$: terms 15, 29, 43, 57, 71, 85, 99, 113, 127. Only 113 is feared. ✗.

$n = 1, a = 56$: terms 57, 113, 169, 225, 281, 337, 393, 449, 505. Only 113 is feared. ✗.

No luck with small $n$.

Let me try to think about this more carefully. Is there any set of 9 feared numbers in AP with common difference $< 100$ that are all below 1300?

The feared numbers below 1300: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

For 9 of these to be in AP with $a < 100$:
- The 130-139 block has 10 consecutive numbers. An AP with $a = 1$ gives 9 consecutive, but we showed the endpoints don't work.
- An AP with $a = 1$ and 9 terms from 130-139: e.g., 130-138. Then $n = 129, n + 10 = 139$ (feared). ✗. Or 131-139: $n = 130$ (feared). ✗.
- Any other AP? The singles are 100 apart, so $a = 100$ (not allowed). Mixed blocks and singles: differences vary, hard to form AP.

I'm convinced: the answer is $\boxed{1288}$.

Actually, let me reconsider one more time. I want to make sure I haven't missed any feared numbers.

A number is feared if its decimal representation contains "13" as a contiguous substring. Let me list all feared numbers up to 1300:

1-digit: none
2-digit: 13
3-digit: 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913
4-digit (up to 1299): 1013, 1113, 1130-1139, 1213

Let me verify:
- 113: "113" contains "13" ✓
- 130-139: "13X" contains "13" ✓
- 213: "213" contains "13" ✓
- 313-913: same pattern ✓
- 1013: "1013" contains "13" ✓
- 1113: "1113" contains "13" ✓
- 1130-1139: "113X" contains "13" ✓
- 1213: "1213" contains "13" ✓

Any others? What about 131? "131" contains "13" ✓ (already in 130-139). 132? ✓ (in 130-139).

What about 1031? "1031" - does it contain "13"? "10", "03", "31" - no "13". Fearless. ✓ (not feared).

What about 1103? "1103" - "11", "10", "03" - no "13". Fearless.

What about 1203? "1203" - no "13". Fearless.

What about 1013? Already listed. ✓.

What about 1103-1112? Let me check 1113: "1113" - "11", "11", "13" - yes, "13" at the end. ✓.

What about 1231? "1231" - "12", "23", "31" - no "13". Fearless.

What about 1293? "1293" - no "13". Fearless.

I think my list is complete. The feared numbers below 1300 are exactly: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

No 9 of these form an AP with $a < 100$ (other than the 130-139 block with $a = 1$, which doesn't work due to endpoint issues).

Therefore, the smallest $n$ is $\boxed{1288}$.

Let me write up the proof now.

Actually, let me reconsider once more whether the 130-139 block with $a=1$ truly doesn't work, but with a twist: what if $n$ or $n+10$ is feared for a different reason but we need them fearless?

With $a = 1$:
- Option 1: $n+1 = 130, \ldots, n+9 = 138$. Then $n = 129$ (fearless ✓), $n+10 = 139$ (feared ✗).
- Option 2: $n+1 = 131, \ldots, n+9 = 139$. Then $n = 130$ (feared ✗), $n+10 = 140$ (fearless ✓).

Neither works. Confirmed.

What about $a = 1$ with a different set of 9 feared numbers? We need 9 consecutive integers all feared, with the neighbors fearless. The only runs of consecutive feared numbers below 1300 are:
- 130-139 (10 long): neighbors 129 (fearless) and 140 (fearless), but the run is 10 long, not 9.
- 1130-1139 (10 long): same issue.

So there's no run of exactly 9 consecutive feared numbers with fearless neighbors. The runs are all 10 long.

What about $a = 1$ with the 100-long block [1300, 1399]? We need 9 consecutive in [1300, 1399] with $n$ and $n+10$ fearless. $n$ must be $< 1300$ (else feared) and $n + 10$ must be $> 1399$ (else feared) or $< 1300$ (impossible since $n + 10 > n + 9 \geq 1300$). So $n + 10 \geq 1400$, meaning $n \geq 1390$. But $n < 1300$. Contradiction. So $a = 1$ doesn't work with [1300, 1399] either.

OK, I'm now fully confident. The answer is $n = 1288$.

Let me write a clean proof.

Proof outline:
1. Show that $n = 1288$ works with $a = 12$.
2. Show that no $n < 1288$ works.

For part 2, I need to show that for any $n < 1288$ and any $a < 100$, it's impossible to have $n, n+10a$ fearless and $n+a, \ldots, n+9a$ all feared.

The key argument: for $n + a, \ldots, n + 9a$ to all be feared, they must all contain "13". The spread is $8a \leq 8 \times 99 = 792$. 

For $n < 1288$, the range $[n+a, n+9a] \subseteq [1, 1288 + 792] = [1, 2080]$.

The feared numbers up to 2080: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213, 1300-1399, 1413, 1513, 1613, 1713, 1813, 1913, 2013.

Hmm wait, for $n < 1288$, $n + 9a$ could be up to $1287 + 891 = 2178$. So the range extends beyond 1300.

So for $n < 1288$, the 9 terms could potentially span across 1300, using the [1300, 1399] block. Let me reconsider.

If $n < 1288$ and some terms are in [1300, 1399]:
- $n + a \geq 1300 \Rightarrow n \geq 1300 - a$
- $n + 9a \leq 1399 \Rightarrow n \leq 1399 - 9a$
- $n + 10a \geq 1400 \Rightarrow n \geq 1400 - 10a$
- $n < 1300$

From $n \geq 1300 - a$ and $n < 1300$: $a \geq 1$.
From $n \geq 1400 - 10a$ and $n < 1300$: $10a > 100 \Rightarrow a \geq 11$.
From $n \leq 1399 - 9a$ and $n \geq 1300 - a$: $8a \leq 99 \Rightarrow a \leq 12$.

So $a \in \{11, 12\}$, same as before.

For $a = 12$: $n \in [1288, 1291]$. Minimum $n = 1288$.
For $a = 11$: $n \in [1290, 1299]$. Minimum $n = 1290$.

Both give $n \geq 1288$. So for $n < 1288$, we can't have all 9 terms in [1300, 1399].

But could some terms be in [1300, 1399] and others feared for different reasons? Let me think about this.

If not all 9 terms are in [1300, 1399], then some terms are below 1300 or above 1399. 

Case 1: Some terms below 1300. These must be feared for other reasons (being in [130, 139], or being a single like 1213, etc.).

Case 2: Some terms above 1399. These must be feared for other reasons (being 1413, 1513, etc.).

For Case 1: The feared numbers just below 1300 are: 1213 (at 1213), and 1130-1139 (at 1130-1139). The gap between 1213 and 1300 is 87. The gap between 1139 and 1300 is 161.

If a term is at 1213 and the next term is in [1300, 1399], then $a \geq 1300 - 1213 = 87$. With $a = 87$: the terms would be 1213, 1300, 1387, 1474, ... The third term (1387) is in [1300, 1399] ✓, but the fourth (1474) is fearless ✗. So only 3 terms are feared.

For more terms to be feared, we'd need more terms in [1300, 1399]. With $a = 87$: $n + 87 = 1213 \Rightarrow n = 1126$. Terms: 1213, 1300, 1387, 1474, 1561, 1648, 1735, 1822, 1909. Feared: 1213 ✓, 1300 ✓, 1387 ✓, 1474 ✗. Only 3.

With $a = 87$ and different starting point: $n + 87 = 1300 \Rightarrow n = 1213$ (feared). ✗.

With $a = 43$: $n + 43 = 1213 \Rightarrow n = 1170$. Terms: 1213, 1256, 1299, 1342, 1385, 1428, 1471, 1514, 1557. Feared: 1213 ✓, 1342 ✓, 1385 ✓, 1514 ✗. Only 3.

Hmm, it seems like we can get at most 3-4 feared terms this way, not 9.

For Case 2: The feared numbers just above 1399 are: 1413 (at 1413), 1513, etc. With $a$ small enough, some terms could be in [1300, 1399] and some at 1413.

$1413 - 1399 = 14$. So if $a = 14$ and the last term in the block is 1399, the next would be 1413. But we need 9 terms total. With $a = 14$: $n + 14, n + 28, \ldots, n + 126$. If $n + 14 = 1300$, terms: 1300, 1314, 1328, 1342, 1356, 1370, 1384, 1398, 1412. 1412 is fearless ("1412" - no "13"). ✗. Only 8 feared.

If $n + 14 = 1286$, $n = 1272$. Terms: 1286 (fearless ✗). 

If $n + 14 = 1300$, $n = 1286$. Terms: 1300, 1314, 1328, 1342, 1356, 1370, 1384, 1398, 1412. 1412 is fearless. ✗.

If $n + 14 = 1299$, $n = 1285$. Terms: 1299 (fearless ✗).

With $a = 14$, the 9th term is $n + 126$. If $n + 14 = 1300$, $n + 126 = 1412$ (fearless). If $n + 14 = 1301$, $n + 126 = 1413$ (feared!). Let me check: $n = 1287$, $n + 14 = 1301$ (feared ✓), $n + 28 = 1315$ (feared ✓), ..., $n + 112 = 1399$ (feared ✓), $n + 126 = 1413$ (feared ✓). 

Wait, let me recalculate. $n = 1287, a = 14$:
- $n + 14 = 1301$ (feared ✓)
- $n + 28 = 1315$ (feared ✓)
- $n + 42 = 1329$ (feared ✓)
- $n + 56 = 1343$ (feared ✓)
- $n + 70 = 1357$ (feared ✓)
- $n + 84 = 1371$ (feared ✓)
- $n + 98 = 1385$ (feared ✓)
- $n + 112 = 1399$ (feared ✓)
- $n + 126 = 1413$ (feared ✓)

All 9 are feared! Now check $n$ and $n + 10a$:
- $n = 1287$: "1287" - no "13" - fearless ✓
- $n + 140 = 1427$: "1427" - no "13" - fearless ✓

This works! $n = 1287$ with $a = 14$!

That's smaller than 1288! Let me double-check all the terms.

$n = 1287, a = 14$:
- $n = 1287$: "1287" → fearless ✓
- $n + a = 1301$: "1301" → "13" at start → feared ✓
- $n + 2a = 1315$: "1315" → "13" at start → feared ✓
- $n + 3a = 1329$: "1329" → "13" at start → feared ✓
- $n + 4a = 1343$: "1343" → "13" at start → feared ✓
- $n + 5a = 1357$: "1357" → "13" at start → feared ✓
- $n + 6a = 1371$: "1371" → "13" at start → feared ✓
- $n + 7a = 1385$: "1385" → "13" at start → feared ✓
- $n + 8a = 1399$: "1399" → "13" at start → feared ✓
- $n + 9a = 1413$: "1413" → "13" at end → feared ✓
- $n + 10a = 1427$: "1427" → no "13" → fearless ✓

All conditions satisfied! $n = 1287 < 1288$.

So my earlier analysis was incomplete - I only considered the case where all 9 terms are in [1300, 1399], but here the 9th term (1413) is outside the block and feared for a different reason (it ends in "13").

Can we do even better? Let me explore this direction.

The idea: 8 terms in [1300, 1399] and 1 term at 1413 (which is $\equiv 13 \pmod{100}$).

$1413 - 1300 = 113$. The 8 terms in [1300, 1399] span $7a$ (from first to 8th), and the 9th term is at $1413$. So the 8th term is at $1413 - a$, and the 1st term is at $1413 - 8a$.

We need:
- $1413 - 8a \geq 1300 \Rightarrow 8a \leq 113 \Rightarrow a \leq 14$
- $1413 - a \leq 1399 \Rightarrow a \geq 14$

So $a = 14$ exactly. And $n + 9a = 1413 \Rightarrow n = 1413 - 126 = 1287$.
$n + a = 1301 \geq 1300$ ✓.
$n + 8a = 1399 \leq 1399$ ✓.
$n = 1287 < 1300$ ✓.
$n + 10a = 1427$. Is 1427 fearless? "1427" - no "13" - fearless ✓.

So $n = 1287$ works. Can we extend this idea further?

What if we have 7 terms in [1300, 1399], 1 at 1413, and 1 at 1513?

$1513 - 1413 = 100$. So $a | 100$. And $a | (1413 - 1300) = 113$... wait, the terms need to be equally spaced. If the 8th term is 1413 and the 9th is 1513, then $a = 100$. Not allowed.

What about 7 terms in [1300, 1399], 1 at 1413, and 1 below 1300 (like 1213)?

$1413 - 1213 = 200$. If these are 8 apart in the AP, $a = 200/8 = 25$. Let me check: $n + a = 1213, n + 2a = 1238, \ldots$. Wait, I need to figure out which terms are which.

Let me think about this differently. We have 9 terms: $n+a, n+2a, \ldots, n+9a$. Some are in [1300, 1399], some are at 1413, some at 1213, etc.

The terms $n+ka$ for $k = 1, \ldots, 9$ form an AP with common difference $a$. The feared numbers we can use are:
- 1213 (single)
- 1300-1399 (block)
- 1413 (single)
- 1513 (single)
- etc.

For a term to be at 1213: $n + ka = 1213$ for some $k$.
For a term to be at 1413: $n + ja = 1413$ for some $j$.
$1413 - 1213 = 200 = (j - k) \cdot a$. So $a | 200$ and $a < 100$. Possible: $a \in \{1, 2, 4, 5, 8, 10, 20, 25, 40, 50\}$.

And the terms between 1213 and 1413 (i.e., $n + (k+1)a, \ldots, n + (j-1)a$) must all be feared. These terms are in the range $(1213, 1413)$. The feared numbers in this range are: 1300-1399. So all intermediate terms must be in [1300, 1399].

Number of intermediate terms: $j - k - 1$. These span from $1213 + a$ to $1413 - a$, and must all be in [1300, 1399].

$1213 + a \geq 1300 \Rightarrow a \geq 87$.
$1413 - a \leq 1399 \Rightarrow a \geq 14$.

So $a \geq 87$. Combined with $a | 200$ and $a < 100$: $a = 100$ (not < 100) or... $200 / 87 \approx 2.3$, not integer. The divisors of 200 that are $\geq 87$ and $< 100$: 100 (excluded). So none. 

Hmm, so we can't have both 1213 and 1413 as terms with all intermediates in [1300, 1399].

What about using 1413 and 1513? $1513 - 1413 = 100$. $a | 100$, $a < 100$. The intermediates between 1413 and 1513 must be feared. Feared numbers in (1413, 1513): none (1414-1512 are all fearless except... let me check. 1413 is feared. 1414: "1414" - no "13" - fearless. ... 1512: "1512" - no "13" - fearless. So no feared numbers between 1413 and 1513.) So we can't have intermediates between 1413 and 1513 that are feared. This means 1413 and 1513 must be consecutive terms, so $a = 100$. Not allowed.

What about using 1413 and having more terms above 1413 that are feared? The next feared number after 1413 is 1513 (100 away). With $a < 100$, we can't reach it.

What about using 1413 and having terms below 1300 that are feared? The feared number just below 1300 is 1213 (87 away). With $a = 14$ (our current solution), $1413 - 1213 = 200 = 14 \times 14.28...$, not a multiple of 14. So 1213 is not a term in the AP with $a = 14$.

Let me check: with $a = 14, n = 1287$: the terms are 1301, 1315, 1329, 1343, 1357, 1371, 1385, 1399, 1413. None of these is 1213. ✓.

Can we get $n < 1287$ by using a different combination?

Let me think about having terms at 1413 and 1313 (both feared, 100 apart). $a | 100$, $a < 100$. The intermediates between 1313 and 1413 must be feared. Feared numbers in (1313, 1413): 1314-1399 (all in [1300, 1399], all feared). So intermediates must be in [1314, 1399].

$1313 + a \geq 1314 \Rightarrow a \geq 1$ (trivially true).
$1413 - a \leq 1399 \Rightarrow a \geq 14$.

So $a \geq 14$ and $a | 100$ and $a < 100$: $a \in \{20, 25, 50\}$.

With $a = 20$: 1313 and 1413 are $100/20 = 5$ terms apart. So if 1313 is the $k$-th term and 1413 is the $(k+5)$-th term. The intermediates (4 terms) are at 1333, 1353, 1373, 1393 - all in [1300, 1399] ✓.

Now, we need 9 terms total. We have 6 terms (1313, 1333, 1353, 1373, 1393, 1413). We need 3 more, which must be feared. These could be below 1313 or above 1413.

Below 1313: the term before 1313 is $1313 - 20 = 1293$ (fearless ✗). So we can't extend below.

Above 1413: the term after 1413 is $1413 + 20 = 1433$ (fearless ✗). Can't extend above.

So with $a = 20$, we only get 6 feared terms. Not enough.

With $a = 25$: 1313 and 1413 are $100/25 = 4$ terms apart. Intermediates: 1338, 1363, 1388 - all in [1300, 1399] ✓. Total: 5 terms. Need 4 more.

Before 1313: $1313 - 25 = 1288$ (fearless ✗).
After 1413: $1413 + 25 = 1438$ (fearless ✗).

Only 5 terms. Not enough.

With $a = 50$: 1313 and 1413 are 2 terms apart. Intermediate: 1363 (in [1300, 1399] ✓). Total: 3 terms. Not enough.

So using both 1313 and 1413 doesn't give enough terms.

Let me go back to the approach that worked: 8 terms in [1300, 1399] and 1 at 1413, with $a = 14$.

Can we have 7 terms in [1300, 1399], 1 at 1413, and 1 at 1213?

$1413 - 1213 = 200$. With $a = 14$: $200/14 = 14.28...$, not integer. So 1213 and 1413 can't both be terms with $a = 14$.

What about 7 in [1300, 1399], 1 at 1413, and 1 at some other feared number below 1300?

The feared numbers below 1300: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

With $a = 14$: the terms are $n + 14, n + 28, \ldots, n + 126$. If $n + 126 = 1413$, $n = 1287$. The terms are 1301, 1315, ..., 1399, 1413. The term before 1301 would be $1301 - 14 = 1287 = n$, which is fearless. So we can't add a term below 1300.

What if we use a different $a$? Let me think about having 7 terms in [1300, 1399], 1 at 1413, and 1 at 1213.

$1413 - 1213 = 200$. The 9 terms span $8a$. If 1213 is the 1st term and 1413 is the 9th: $8a = 200$, $a = 25$. Terms: 1213, 1238, 1263, 1288, 1313, 1338, 1363, 1388, 1413.

Check: 1213 (feared ✓), 1238 (fearless ✗). Doesn't work.

If 1213 is the 1st term and 1413 is the 8th: $7a = 200$, $a = 200/7$ (not integer).

If 1213 is the 2nd term and 1413 is the 9th: $7a = 200$, not integer.

If 1213 is the 1st and 1413 is the 7th: $6a = 200$, not integer.

Hmm, 200 = 8 × 25. So the only way is $a = 25$ with 1213 and 1413 being 8 terms apart (1st and 9th). But then the intermediate terms include 1238, 1263, 1288 which are fearless.

What about using 1130-1139 block? With $a = 14$: $1413 - 1130 = 283$. $283/14 = 20.2$, not integer. $1413 - 1139 = 274$. $274/14 = 19.57$, not integer.

What about using 1113? $1413 - 1113 = 300$. $300/14 = 21.4$, not integer.

OK so with $a = 14$, we can't combine 1413 with any feared number below 1300 to get more terms.

Let me try other values of $a$ where we can have 8 terms in [1300, 1399] and 1 at 1413.

We need: the 9th term is 1413, and terms 1-8 are in [1300, 1399].
- $n + 9a = 1413 \Rightarrow n = 1413 - 9a$
- $n + a \geq 1300 \Rightarrow 1413 - 8a \geq 1300 \Rightarrow a \leq 14$
- $n + 8a \leq 1399 \Rightarrow 1413 - a \leq 1399 \Rightarrow a \geq 14$

So $a = 14$ is the only option. $n = 1287$.

What about having 7 terms in [1300, 1399], 1 at 1413, and 1 at 1513?

$1513 - 1413 = 100$. $a | 100$. And the term at 1413 and 1513 are consecutive terms (since no feared numbers between them), so $a = 100$. Not allowed.

What about 7 in [1300, 1399], 1 at 1413, and 1 more that's also in [1300, 1399]? That's just 8 in [1300, 1399] and 1 at 1413, which is the case we already solved.

What about 8 in [1300, 1399] and 1 at 1513? $1513 - 1300 = 213$ (if 1st term is 1300 and 9th is 1513, $8a = 213$, not integer). $1513 - 1399 = 114$ (if 8th term is 1399 and 9th is 1513, $a = 114$, too big). 

Actually, let me be more careful. If the 9th term is 1513 and the 1st through 8th are in [1300, 1399]:
- $n + 9a = 1513 \Rightarrow n = 1513 - 9a$
- $n + a \geq 1300 \Rightarrow 1513 - 8a \geq 1300 \Rightarrow a \leq 26$
- $n + 8a \leq 1399 \Rightarrow 1513 - a \leq 1399 \Rightarrow a \geq 114$

$a \geq 114$ and $a \leq 26$: contradiction. So this doesn't work.

What about 7 in [1300, 1399], 1 at 1413, and 1 at 1513?

The 1413 and 1513 terms: $1513 - 1413 = 100$, so $a | 100$ and they are $100/a$ terms apart. Since there are no feared numbers between 1413 and 1513, they must be consecutive terms: $a = 100$. Not allowed.

What about 8 in [1300, 1399] and 1 at 1427? 1427 is "1427" -        — AI历史解题过程（thinking）
#   polymath_00325         — 题目ID

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
  <problem_id>polymath_00325</problem_id>
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

Call a number feared if it contains the digits \(13\) as a contiguous substring and fearless otherwise. (For example, \(132\) is feared, while \(123\) is fearless.) Compute the smallest positive integer \(n\) such that there exists a positive integer \(a<100\) such that \(n\) and \(n+10a\) are fearless while \(n+a, n+2a, \ldots, n+9a\) are all feared.

## Standard Solution

Solution: First, note that \(n, n+a, \ldots, n+10a\) cannot all be less than \(1000\), since a fearless number cannot have \(13\) as its last two digits. Numbers like \(129, 130, 131, \ldots, 139\) do not work because \(139\) is feared.

Thus, we must consider numbers of the form \(13xy\), where \(1, 3, x\), and \(y\) are digits. If all of \(n+a, n+2a, \ldots, n+9a\) start with \(13\), then \(a \leq 12\). The minimum we can achieve is:

\[
1288, 1300, 1312, \ldots, 1384, 1396, 1408
\]

However, if \(n+9a = 1413\), we can take \(a = 14\) to get:

\[
1287, 1301, 1315, \ldots, 1399, 1413, 1427
\]

Thus, the minimum possible value for \(n\) is \(1287\).

\(\boxed{1287}\)

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the smallest positive integer $n$ such that there exists a positive integer $a < 100$ where:
- $n$ is fearless (no "13" as contiguous substring)
- $n + 10a$ is fearless
- $n + a, n + 2a, \ldots, n + 9a$ are all feared (contain "13")

So we have 11 numbers: $n, n+a, n+2a, \ldots, n+10a$. The first and last are fearless, the middle 9 are feared.

Let me think about this systematically. The numbers form an arithmetic progression with common difference $a$.

Let me think about what makes a number feared - it contains "13" as a contiguous substring in its decimal representation.

Let me think about the structure. We have $n$ and $n+10a$ fearless, and $n+ka$ for $k=1,...,9$ all feared.

Let me consider the last two digits. If $a$ is small relative to the number, the higher digits stay mostly fixed while the last digits change.

Actually, let me think about this differently. Let's consider the decimal representation.

Let me try small values of $a$ first and search for the smallest $n$.

For a given $a$, we need $n$ fearless, $n+10a$ fearless, and all intermediate values feared.

Let me think about the digit structure. The key insight is that "13" needs to appear in the decimal representation.

Let me consider the case where the "13" appears in the last two digits. If $n + ka$ has last two digits forming "13" (i.e., $\equiv 13 \pmod{100}$), then it's feared.

But we need this for $k=1,...,9$ simultaneously, which means $n+a \equiv n+2a \equiv \ldots \equiv n+9a \equiv 13 \pmod{100}$, which requires $a \equiv 0 \pmod{100}$, but $a < 100$, so $a = 0$, not positive. So the "13" can't always be in the last two digits.

So the "13" must appear in different positions for different $k$ values, or in higher digits.

Let me think about this more carefully. The numbers $n, n+a, \ldots, n+10a$ span a range of $10a$. Since $a < 100$, the range is at most 990.

Let me think about when "13" appears in the tens-hundreds boundary or similar.

Let me consider the structure where the number has the form ...X... where X is some digit pattern.

Actually, let me think about this more concretely. Let's say $n$ has digits $d_m d_{m-1} \ldots d_1 d_0$.

For $n + ka$ to be feared, "13" must appear somewhere. The position where "13" appears could depend on $k$.

Let me think about a specific approach. Consider numbers around 1300. If $n$ is slightly below 1300, then $n + ka$ might cross 1300, making some of them feared (containing "13" at the thousands-hundreds position).

Wait, but we need $n+1a$ through $n+9a$ ALL feared, and $n$ and $n+10a$ fearless.

Let me think about the range $[n, n+10a]$. The total spread is $10a < 1000$.

Strategy: Find a range where crossing certain boundaries creates "13" patterns.

Let me think about the hundreds digit. If we're in a range like 1250-1350, numbers in [1300, 1399] contain "13" at the thousands-hundreds position (digits "13" at positions 3,2).

So if $n + ka$ falls in [1300, 1399] for $k=1,...,9$, they're all feared. And $n$ and $n+10a$ are outside this range (and fearless otherwise).

For this: $n < 1300$, $n + a \geq 1300$, $n + 9a \leq 1399$, $n + 10a > 1399$ (or $n + 10a \leq 1399$ but fearless for another reason... no, if $n+10a \in [1300, 1399]$ it would be feared).

So we need:
- $n + a \geq 1300 \Rightarrow n \geq 1300 - a$
- $n + 9a \leq 1399 \Rightarrow n \leq 1399 - 9a$
- $n + 10a > 1399 \Rightarrow n > 1399 - 10a$, i.e., $n \geq 1400 - 10a$
- $n < 1300$
- $n$ is fearless
- $n + 10a$ is fearless

From the first and fourth: $1300 - a \leq n < 1300$, so $n \in [1300-a, 1299]$.
From the second and third: $1400 - 10a \leq n \leq 1399 - 9a$.

We need both ranges to overlap: $\max(1300-a, 1400-10a) \leq n \leq \min(1299, 1399-9a)$.

For the upper bound: $1399 - 9a \geq 1300 - a \Rightarrow 99 \geq 8a \Rightarrow a \leq 12$.
Also $1299 \geq 1400 - 10a \Rightarrow 10a \geq 101 \Rightarrow a \geq 11$.

So $a \in \{11, 12\}$.

For $a = 11$: $n \in [\max(1289, 1290), \min(1299, 1300)] = [1290, 1299]$.
$n + 10a = n + 110 \in [1400, 1409]$.
We need $n$ fearless and $n+110$ fearless.
$n \in [1290, 1299]$: none of these contain "13", so all fearless. ✓
$n + 110 \in [1400, 1409]$: none contain "13", so all fearless. ✓
And $n + ka$ for $k=1,...,9$: $n + ka \in [1301, 1399+11-1]$. Wait let me compute.
$n = 1290$: $n+11 = 1301$ (feared, "13"), ..., $n+99 = 1389$ (feared), $n+110 = 1400$ (fearless). ✓
$n = 1299$: $n+11 = 1310$ (feared), ..., $n+99 = 1398$ (feared), $n+110 = 1409$ (fearless). ✓

So for $a = 11$, $n = 1290$ works! Let me verify:
- $n = 1290$: digits "1290", no "13" → fearless ✓
- $n + 11 = 1301$: "1301" contains "13" → feared ✓
- $n + 22 = 1312$: "1312" contains "13" → feared ✓
- $n + 33 = 1323$: "1323" contains "13" → feared ✓
- $n + 44 = 1334$: "1334" contains "13" → feared ✓
- $n + 55 = 1345$: "1345" contains "13" → feared ✓
- $n + 66 = 1356$: "1356" contains "13" → feared ✓
- $n + 77 = 1367$: "1367" contains "13" → feared ✓
- $n + 88 = 1378$: "1378" contains "13" → feared ✓
- $n + 99 = 1389$: "1389" contains "13" → feared ✓
- $n + 110 = 1400$: "1400", no "13" → fearless ✓

So $n = 1290$ works with $a = 11$.

But can we do better? Can we find a smaller $n$?

Let me think about whether there's a smaller $n$ with a different $a$.

The approach above used the "13" appearing at the thousands-hundreds boundary (1300-1399). We could also use:
- 130-139 (hundreds-tens boundary)
- 13 (tens-ones, i.e., numbers ending in 13 or containing 13 in last two digits)
- Larger: 13000-13999, etc.

For the 130-139 range: $n + ka \in [130, 139]$ for $k=1,...,9$.
- $n + a \geq 130 \Rightarrow n \geq 130 - a$
- $n + 9a \leq 139 \Rightarrow n \leq 139 - 9a$
- $n + 10a > 139 \Rightarrow n \geq 140 - 10a$
- $n < 130$

Overlap: $\max(130-a, 140-10a) \leq n \leq \min(129, 139-9a)$.
$139 - 9a \geq 130 - a \Rightarrow 9 \geq 8a \Rightarrow a \leq 1$.
$129 \geq 140 - 10a \Rightarrow 10a \geq 11 \Rightarrow a \geq 2$.

Contradiction! So $a \leq 1$ and $a \geq 2$ can't both hold. So this range doesn't work with the simple boundary approach.

Hmm, but maybe the "13" doesn't have to be at the same position for all $k$. Let me reconsider.

Actually, for the 130-139 range, the issue is that the range [130, 139] has only 10 numbers, and we need 9 consecutive multiples to fall in it, plus the endpoints outside. The spread is $10a$ and the range is only 10 wide, so $10a \leq 10$ roughly, meaning $a = 1$. But then $n+10a = n+10$ must be $> 139$, so $n \geq 130$, but $n < 130$. Contradiction.

So for the 130-139 range, we can't fit 9 values inside and both endpoints outside.

What about using "13" in the last two digits? A number ends in "13" if it's $\equiv 13 \pmod{100}$. But we need 9 consecutive values $n+a, \ldots, n+9a$ to all be feared. If they all end in 13, then $a \equiv 0 \pmod{100}$, impossible.

But "13" could appear in other positions too. For example, a number like 213, 313, 413, etc. contains "13" in the middle.

Let me think about smaller $n$ more carefully. We need $n < 1290$ potentially.

Let me think about what other ranges could work. The "13" substring can appear at various positions. Let me think about numbers below 1290.

For $n < 100$: The numbers $n, n+a, \ldots, n+10a$ are all at most $99 + 990 = 1089$. Actually $n + 10a < 100 + 990 = 1090$. So they're at most 3 digits (or barely 4 digits).

For $n$ in range [0, 129], the feared numbers in this range are: 13, 113, 130-139. Wait, 113 contains "13"? "113" - yes, "13" appears at positions 1,0 (the "13" in "113"). Actually "113" = digits 1,1,3. The substring "13" would need consecutive digits 1,3. In "113", we have "11" and "13" - yes, "13" appears (the last two digits are "13"). So 113 is feared.

Numbers containing "13" below 130: 13, 113. And 130-139.

For small $n$, let me think about what ranges of feared numbers exist.

Feared numbers (containing "13") up to ~1400:
- 13
- 113
- 130-139
- 213
- 313
- 413
- 513
- 613
- 713
- 813
- 913
- 1013, 1113
- 1130-1139
- 1213
- 1300-1399

So the feared numbers form clusters. For our problem, we need 9 consecutive terms of an AP to all be feared, with the 0th and 10th terms fearless.

The largest cluster is 1300-1399 (100 numbers). The next largest is 130-139 (10 numbers) and 1130-1139 (10 numbers).

For 1300-1399: we found $n = 1290, a = 11$.

For 1130-1139: similar analysis. $n + ka \in [1130, 1139]$ for $k=1,...,9$.
- $n + a \geq 1130 \Rightarrow n \geq 1130 - a$
- $n + 9a \leq 1139 \Rightarrow n \leq 1139 - 9a$
- $n + 10a > 1139 \Rightarrow n \geq 1140 - 10a$
- $n < 1130$

$\max(1130-a, 1140-10a) \leq n \leq \min(1129, 1139-9a)$.
$1139 - 9a \geq 1130 - a \Rightarrow 9 \geq 8a \Rightarrow a \leq 1$.
$1129 \geq 1140 - 10a \Rightarrow 10a \geq 11 \Rightarrow a \geq 2$.
Contradiction again. So 1130-1139 doesn't work with this simple approach.

What about combining multiple clusters? The "13" doesn't have to be at the same position for all $k$. For example, some $n+ka$ could be feared because they're in 130-139, and others because they end in 13, etc.

Let me think about this more creatively. We need 9 values $n+a, \ldots, n+9a$ to each contain "13" somewhere, but the position can vary.

Let me think about $a = 100$. No, $a < 100$.

Let me think about $a = 50$. Then $n, n+50, n+100, \ldots, n+500$. The spread is 500. We need $n+50, n+100, \ldots, n+450$ all feared, and $n, n+500$ fearless.

Hmm, this is getting complex. Let me think about whether we can beat 1290.

Let me think about the structure differently. We need a "gap" in fearless numbers. Specifically, we need 9 consecutive AP terms (with step $a$) to all be feared, bracketed by two fearless terms.

The fearless numbers are those NOT containing "13". The density of fearless numbers among $k$-digit numbers can be computed, but let me think about specific gaps.

The largest contiguous block of feared numbers below 1300 is 130-139 (10 numbers). Can we use this?

For the block 130-139 (10 feared numbers), we need $n+a, \ldots, n+9a$ to all be in this block (or feared for other reasons), with $n$ and $n+10a$ fearless.

If all 9 are in [130, 139]: as computed, this requires $a \leq 1$ and $a \geq 2$, impossible.

But what if some of the 9 are in [130, 139] and others are feared for different reasons?

For example, with $a = 1$: $n, n+1, \ldots, n+10$. We need $n+1, \ldots, n+9$ feared, $n$ and $n+10$ fearless. This means 9 consecutive integers are feared, bracketed by fearless. The longest run of consecutive feared numbers is 10 (130-139, 1130-1139, etc.). So we need 9 consecutive feared with fearless on both sides.

130-139: 130 is feared (starts with 13), 139 is feared. What about 129? "129" - fearless. 140? "140" - fearless. So 129 is fearless, 130-139 are feared (10 numbers), 140 is fearless.

With $a = 1$: $n = 129$, then $n+1 = 130, \ldots, n+9 = 138$ are all feared, $n+10 = 139$ is also feared. But we need $n+10$ to be fearless! 139 is feared. So this doesn't work.

$n = 130$: $n$ is feared. Doesn't work.

What about $n = 129, a = 1$: $n+10 = 139$ which is feared. ✗.

$n = 130, a = 1$: $n$ is feared. ✗.

Hmm. With $a = 1$, we need exactly 9 consecutive feared numbers with fearless on both sides. The block 130-139 has 10 feared numbers. So $n = 129$: $n+1=130$ to $n+9=138$ feared, $n+10=139$ feared. ✗. $n=130$: $n$ feared. ✗.

Is there a block of exactly 9 feared numbers? Or a block where we can pick 9 with fearless neighbors?

Actually, we need $n+1$ through $n+9$ feared (9 numbers) and $n, n+10$ fearless. So we need a run of at least 9 feared numbers, and the number just before and just after must be fearless.

Block 130-139 (10 feared): The number before (129) is fearless, the number after (140) is fearless. But the block has 10 feared numbers. We need 9 consecutive feared with fearless on both sides. 

If we take $n+1 = 130, \ldots, n+9 = 138$: $n = 129$ (fearless ✓), $n+10 = 139$ (feared ✗).
If we take $n+1 = 131, \ldots, n+9 = 139$: $n = 130$ (feared ✗), $n+10 = 140$ (fearless ✓).

Neither works because the block is 10 long, not 9.

What about the block 1130-1139? Same issue - 10 feared numbers.

What about other blocks? Let me look for blocks of feared numbers that are exactly 9 long, or where we can find 9 consecutive feared with fearless neighbors.

Actually, let me reconsider. Maybe the "13" appears at different positions for different terms, not all in the same block.

Let me think about $a = 1$ more carefully. We need 9 consecutive integers $n+1, \ldots, n+9$ all feared, with $n$ and $n+10$ fearless.

The feared numbers up to 200: 13, 113, 130-139.
So: ..., 112 (fearless), 113 (feared), 114 (fearless), ..., 129 (fearless), 130-139 (feared), 140 (fearless), ...

There's no run of 9 consecutive feared numbers with $a=1$ except possibly in the 130-139 block, but that's 10 long.

What about combining? E.g., 113 is feared, 114-129 are fearless, 130-139 are feared. No run of 9.

So $a = 1$ doesn't seem to work for small $n$.

Let me try $a = 2$. We need $n+2, n+4, \ldots, n+18$ all feared, $n$ and $n+20$ fearless.

Hmm, this is getting complicated. Let me think about it differently.

Actually, let me reconsider the 1300-1399 approach but see if we can get a smaller $n$ using a different cluster or combination.

What about using the cluster around 1130-1139 combined with 1213?

Let me think about $a = 100 - 1 = 99$. Then $n, n+99, n+198, \ldots, n+990$. The spread is 990.

Hmm, let me think about this differently. Let me consider what happens with various $a$ values and try to find the minimum $n$.

Actually, let me reconsider. The answer $n = 1290$ might not be minimal. Let me think about whether there's a smaller $n$ using a different approach.

Key insight: The "13" can appear at any position in the number. For different values of $k$, the "13" might appear at different positions.

Let me think about numbers around 1130. The feared numbers near 1130:
- 1113 (contains "13" at end)
- 1130-1139 (contains "13" at hundreds-tens)
- 1213 (contains "13" at end)

What about $a = 11$? Then $n, n+11, n+22, \ldots, n+110$.
If $n = 1119$: $n+11 = 1130$ (feared), $n+22 = 1141$ (fearless? "1141" - no "13" - fearless). ✗.

If $n = 1129$: $n+11 = 1140$ (fearless). ✗.

Hmm, the 1130-1139 block is only 10 numbers wide, and with $a = 11$, we can only fit one term in it.

Let me think about combining the 1113 and 1130-1139 clusters.

With $a = 17$: $n = 1096$. $n+17 = 1113$ (feared), $n+34 = 1130$ (feared), $n+51 = 1147$ (fearless). ✗.

This approach of combining clusters seems hard because the clusters are far apart relative to $a$.

Let me think about a completely different approach. What if "13" appears in the last two digits for some terms and in other positions for other terms?

A number ends in "13" if it's $\equiv 13 \pmod{100}$. So $n + ka \equiv 13 \pmod{100}$ for some specific $k$.

For different $k$ values, $n + ka \pmod{100}$ takes different values (since $a \not\equiv 0 \pmod{100}$ for $a < 100$). So at most one or two values of $k$ give $n + ka \equiv 13 \pmod{100}$.

Similarly, $n + ka \equiv 113 \pmod{1000}$ (i.e., last 3 digits are 113, which contains "13") for at most one $k$.

This is getting complex. Let me try to be more systematic and think about what values of $n < 1290$ could work.

Let me think about the problem from the perspective of digit carrying. When we add $ka$ to $n$, carries propagate. The "13" pattern needs to appear somewhere.

Let me consider the approach where "13" appears at the hundreds-tens position (i.e., the number mod 1000 is in [130, 139]) or at the thousands-hundreds position (mod 10000 in [1300, 1399]) etc.

For the 130-139 block (mod 1000): As computed, we can't fit 9 AP terms in a 10-wide block with $a \geq 2$ and have endpoints outside. With $a = 1$, the block is 10 wide but we need endpoints outside, giving 9 inside, but the endpoints fall inside the block.

Wait, let me recheck. With $a = 1$ and the block [130, 139]:
- $n + 1 = 130, \ldots, n + 9 = 138$: $n = 129$, $n + 10 = 139$ (feared). ✗.
- $n + 1 = 131, \ldots, n + 9 = 139$: $n = 130$ (feared). ✗.

So indeed $a = 1$ doesn't work with this block because the block is 10 wide and we need the 10th term to be outside.

But what if some terms are feared for OTHER reasons, not because they're in [130, 139]?

For example, with $a = 1$: $n = 112$. $n+1 = 113$ (feared, "113" contains "13"). $n+2 = 114$ (fearless). ✗.

What about combining 113 and 130-139? These are 17 apart, so with $a = 1$ they can't both be covered.

OK let me try a different approach. Let me think about what $a$ values could give $n < 1290$.

For $n < 1300$, the feared numbers are scattered. The main clusters are:
- 13 (single)
- 113 (single)
- 130-139 (block of 10)
- 213, 313, 413, 513, 613, 713, 813, 913 (singles, each 100 apart)
- 1013, 1113 (singles)
- 1130-1139 (block of 10)
- 1213 (single)

For $n < 1300$, we need 9 AP terms (step $a$) to all be feared. The AP terms are $n+a, n+2a, \ldots, n+9a$.

The singles (like 213, 313, ...) are 100 apart. If $a = 100$, we could hit 213, 313, 413, ..., 913 - that's 8 values. But $a < 100$, so $a = 100$ is not allowed. With $a = 99$: $n + 99, n + 198, \ldots, n + 891$. These are 99 apart. 213, 312, 411, ... - no, 312 doesn't contain "13".

Hmm. Let me think about $a$ values that align with the spacing of feared numbers.

The singles 213, 313, 413, ..., 913 are 100 apart. With $a$ close to 100, we might hit several of these, but they won't be exactly aligned unless $a = 100$.

What about $a = 100 - 1 = 99$? Then $n + 99k$. If $n + 99 = 213$, then $n = 114$. $n + 198 = 312$ (fearless). ✗.

$a = 100 + 1 = 101$? No, $a < 100$.

What about $a = 50$? $n + 50k$. The feared numbers at positions 50 apart... 113, 163 (fearless), 213 (feared), 263 (fearless)... doesn't work.

Let me try to think about this more carefully. For $n < 1290$, we need to find $a < 100$ such that $n + a, \ldots, n + 9a$ are all feared. The spread is $9a < 900$.

For $n$ around 1000-1290, the feared numbers in this range are:
- 1013, 1113, 1130-1139, 1213.

That's very sparse. 1013, 1113 are 100 apart. 1113, 1130 are 17 apart. 1130-1139 is a block. 1213 is separate.

For 9 AP terms to all be feared in this range, we'd need them to all fall on these sparse feared numbers. Seems very unlikely unless $a$ is very small and they all fall in the 1130-1139 block, which we showed doesn't work.

For $n$ around 130-139: same issue as before.

For $n$ around 200-900: feared numbers are 213, 313, 413, 513, 613, 713, 813, 913. These are 100 apart. With $a < 100$, we can't hit more than one or two of these.

Wait, but what about numbers like 130-139? If $n$ is around 130, the spread $9a$ could reach up to $130 + 9 \cdot 99 = 130 + 891 = 1021$. So the AP terms could span from ~130 to ~1021, hitting feared numbers at various positions.

Let me think about this. With $a = 100 - 13 = 87$? Or some other value.

Actually, let me think about it differently. Let me consider $a$ such that $n + ka$ hits feared numbers for $k = 1, \ldots, 9$.

The feared numbers below 1300 are: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

Let me list them more carefully:
- 13
- 113
- 130, 131, 132, 133, 134, 135, 136, 137, 138, 139
- 213
- 313
- 413
- 513
- 613
- 713
- 813
- 913
- 1013
- 1113
- 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139
- 1213

Now, for an AP with step $a$, we need 9 consecutive terms to be feared. Let me see if there's an AP that hits 9 of these.

The numbers 213, 313, 413, 513, 613, 713, 813, 913 are 100 apart. An AP with $a = 100$ would hit all 8, but $a < 100$.

What if we use $a = 100$? Not allowed. $a = 99$?

With $a = 99$: if $n + 99 = 213$, then $n = 114$. The terms are:
- $n + 99 = 213$ (feared ✓)
- $n + 198 = 312$ (fearless ✗)

Doesn't work.

What about $a = 100$? Not allowed.

Hmm, let me think about whether the "13" could appear in a different way. For example, 1313 contains "13" twice. 1300-1399 all contain "13". 

What if we use a combination where some terms are in [130, 139] and others are in [1300, 1399]? But the spread would need to be at least 1161, requiring $9a \geq 1161$, so $a \geq 130$, but $a < 100$. Impossible.

What about terms in [130, 139] and [1130, 1139]? Spread $\geq 991$, $a \geq 111$. Impossible.

OK so for $n < 1300$, it seems very hard to get 9 feared terms. Let me reconsider.

What about $n$ slightly less than 1300, like $n = 1290$? We already found this works with $a = 11$.

Can we do better? Let me check $n$ values from 1200 to 1290.

For $n$ in [1200, 1299], $n + 10a < 1300 + 990 = 2290$. The feared numbers in [1200, 2290]:
- 1213
- 1300-1399
- 1413
- 1513
- 1613
- 1713
- 1813
- 1913
- 2013
- 2113
- 2130-2139
- 2213

The block 1300-1399 is the big one. For $n$ in [1200, 1299], if we use $a$ such that $n + a, \ldots, n + 9a$ all fall in [1300, 1399], we need:
- $n + a \geq 1300$
- $n + 9a \leq 1399$
- $n + 10a > 1399$ (or $n + 10a$ is fearless for another reason)
- $n < 1300$

From $n + a \geq 1300$ and $n < 1300$: $a > 0$ (always true) and $n \geq 1300 - a$.
From $n + 9a \leq 1399$: $n \leq 1399 - 9a$.
From $n + 10a > 1399$: $n > 1399 - 10a$, i.e., $n \geq 1400 - 10a$.

So $n \in [\max(1300 - a, 1400 - 10a), \min(1299, 1399 - 9a)]$.

For this to be non-empty:
1. $1300 - a \leq 1299 \Rightarrow a \geq 1$ ✓
2. $1400 - 10a \leq 1299 \Rightarrow 10a \geq 101 \Rightarrow a \geq 11$
3. $1300 - a \leq 1399 - 9a \Rightarrow 8a \leq 99 \Rightarrow a \leq 12$
4. $1400 - 10a \leq 1399 - 9a \Rightarrow a \geq 1$ ✓

So $a \in \{11, 12\}$.

For $a = 11$: $n \in [\max(1289, 1290), \min(1299, 1300)] = [1290, 1299]$.
For $a = 12$: $n \in [\max(1288, 1280), \min(1299, 1291)] = [1288, 1291]$.

For $a = 12$, $n = 1288$: $n + 12 = 1300$ (feared), ..., $n + 108 = 1396$ (feared), $n + 120 = 1408$ (fearless? "1408" - no "13" - fearless ✓). $n = 1288$ (fearless ✓).

So $n = 1288$ works with $a = 12$! That's smaller than 1290.

Let me verify $n = 1288, a = 12$:
- $n = 1288$: "1288", no "13" → fearless ✓
- $n + 12 = 1300$: "1300", contains "13" → feared ✓
- $n + 24 = 1312$: "1312", contains "13" → feared ✓
- $n + 36 = 1324$: "1324", contains "13" → feared ✓
- $n + 48 = 1336$: "1336", contains "13" → feared ✓
- $n + 60 = 1348$: "1348", contains "13" → feared ✓
- $n + 72 = 1360$: "1360", contains "13" → feared ✓
- $n + 84 = 1372$: "1372", contains "13" → feared ✓
- $n + 96 = 1384$: "1384", contains "13" → feared ✓
- $n + 108 = 1396$: "1396", contains "13" → feared ✓
- $n + 120 = 1408$: "1408", no "13" → fearless ✓

All checks pass. $n = 1288$ works.

Can we do even better? For $a = 12$, $n = 1288$ is the minimum in that range. For $a = 11$, $n = 1290$ is the minimum.

But maybe there are other approaches that give smaller $n$?

Let me think about whether we can use a different block of feared numbers. What about the block 130-139?

For the block [130, 139] with the same approach:
- $n + a \geq 130$, $n + 9a \leq 139$, $n + 10a > 139$, $n < 130$.
- $n \in [\max(130-a, 140-10a), \min(129, 139-9a)]$.
- Need $140 - 10a \leq 129 \Rightarrow a \geq 2$ and $130 - a \leq 139 - 9a \Rightarrow 8a \leq 9 \Rightarrow a \leq 1$.
- Contradiction. So this doesn't work.

What about using the block [130, 139] but allowing $n + 10a$ to be in the block (and feared for a different reason)? No, $n + 10a$ must be fearless.

What about using a block of feared numbers that's wider? The only wide blocks are [130, 139], [1130, 1139], [1300, 1399], [2130, 2139], etc. The 1300-1399 block is the first one wide enough.

Wait, but what about combining multiple sources of "13"? For example, some terms could be feared because they're in [130, 139], and others because they end in "13" (like 213, 313, etc.), and others because they're in [1300, 1399].

Let me think about this. For $n$ around 130, with a large enough $a$, the AP could span from ~130 to ~1300, hitting feared numbers at various positions.

For example, $a = 130$. No, $a < 100$.

$a = 99$: $n + 99k$ for $k = 1, \ldots, 9$. Spread = 891. If $n = 130 - 99 = 31$, then:
- $n + 99 = 130$ (feared ✓)
- $n + 198 = 229$ (fearless ✗)

Doesn't work.

$a = 100 - 1 = 99$: The terms would be roughly 100 apart, but not exactly hitting the feared singles.

Let me try $a = 100 - 13 = 87$. If $n + 87 = 130$, $n = 43$.
- $n + 87 = 130$ (feared ✓)
- $n + 174 = 217$ (fearless ✗)

$a = 100$: not allowed.

Hmm, the problem is that the feared singles (213, 313, ...) are exactly 100 apart, and we need $a < 100$, so we can't hit them all.

What if we use a different set of feared numbers? Let me think about numbers containing "13" that are closer together.

In the range [1300, 1399], all 100 numbers are feared. That's the key. And we showed the minimum $n$ using this block is 1288.

But what about using the block [130, 139] (10 numbers) combined with other feared numbers?

For $n$ slightly below 130, with $a$ such that some terms fall in [130, 139] and others fall on feared singles.

Let me try $a = 100 - 1 = 99$. If $n + 99 = 130$, $n = 31$.
- $n = 31$ (fearless ✓)
- $n + 99 = 130$ (feared ✓)
- $n + 198 = 229$ (fearless ✗)

No. The gap between 139 and 213 is 74, and between 213 and 313 is 100. With $a = 99$, we can't hit both 130-139 and 213.

Let me try $a = 83$. If $n + 83 = 130$, $n = 47$.
- $n + 83 = 130$ (feared ✓)
- $n + 166 = 213$ (feared ✓)
- $n + 249 = 296$ (fearless ✗)

$a = 83$ hits 130 and 213 (83 apart), but then 296 is fearless.

What about $a = 100$? Not allowed. The fundamental issue is that the feared singles are 100 apart and we need $a < 100$.

Let me try to find $a$ such that the AP hits multiple feared numbers that aren't 100 apart.

Feared numbers and their differences:
- 13 to 113: 100
- 113 to 130: 17
- 130 to 139: consecutive
- 139 to 213: 74
- 213 to 313: 100
- 313 to 413: 100
- ...

The differences are mostly 100, except around the blocks. So with $a < 100$, we can hit at most 2-3 feared numbers that are in the blocks, but not 9.

What about using the block [130, 139] more creatively? The block has 10 numbers. With $a = 1$, we can hit all 10, but we need the 10th term ($n + 10$) to be fearless, and the block is exactly 10 wide, so $n + 10$ would be 140 (fearless) only if $n + 1 = 131, \ldots, n + 9 = 139$, but then $n = 130$ (feared). Or $n + 1 = 130, \ldots, n + 9 = 138$, $n + 10 = 139$ (feared). Neither works.

With $a = 2$: we can hit 5 numbers in [130, 139] (every other one). Not enough.

What about $a = 1$ but using a different block? Is there a block of exactly 9 feared numbers with fearless on both sides?

The blocks are all 10 wide (130-139, 1130-1139, 1300-1399 is 100 wide, 2130-2139, etc.).

For a 10-wide block with $a = 1$: we need 9 consecutive in the block, with the term before and after being fearless. But the term before the block is fearless and the term after is fearless. So if we take 9 from the 10-wide block:
- Take 130-138 (9 numbers): $n = 129$ (fearless ✓), $n + 10 = 139$ (feared ✗).
- Take 131-139 (9 numbers): $n = 130$ (feared ✗), $n + 10 = 140$ (fearless ✓).

Neither works because one endpoint falls inside the block.

What if there's a number just outside the block that's also feared? For example, is 129 feared? "129" - no "13" - fearless. Is 140 feared? "140" - no "13" - fearless. So no.

What about 1129? "1129" - no "13" - fearless. 1140? "1140" - no "13" - fearless.

Hmm, so the 10-wide blocks don't work with $a = 1$.

What about the 100-wide block [1300, 1399] with $a = 1$? We need 9 consecutive in [1300, 1399] with $n$ and $n + 10$ fearless. Since the block is 100 wide, there's plenty of room.

$n = 1299$ (fearless? "1299" - no "13" - fearless ✓). $n + 1 = 1300, \ldots, n + 9 = 1308$ (all feared ✓). $n + 10 = 1309$ (feared ✗).

$n = 1290$ (fearless ✓). $n + 1 = 1291$ (fearless ✗).

So with $a = 1$, we need $n + 1$ through $n + 9$ all in [1300, 1399], and $n, n + 10$ outside (and fearless). $n + 1 \geq 1300 \Rightarrow n \geq 1299$. $n + 9 \leq 1399 \Rightarrow n \leq 1390$. $n + 10 > 1399 \Rightarrow n \geq 1390$. So $n = 1390$: $n + 10 = 1400$ (fearless ✓). But $n = 1390$ is feared! ✗.

$n = 1390$: "1390" contains "13" → feared. ✗.

So with $a = 1$ and the block [1300, 1399], $n$ must be $\geq 1299$ and $\leq 1390$ and $\geq 1390$, so $n = 1390$, which is feared. Doesn't work.

Actually wait, I need $n$ to be fearless AND $n < 1300$ (or $n \geq 1400$ but then $n + 1 \geq 1401$ which is outside the block). So $n < 1300$ and $n + 1 \geq 1300$, giving $n = 1299$. Then $n + 10 = 1309$ (feared). ✗.

So $a = 1$ doesn't work with this block either.

OK so let me go back to $a = 12, n = 1288$ and see if we can find anything smaller.

Let me think about whether there's a completely different approach. What if the "13" appears in a higher position?

For example, numbers like 13000-13999. But $n$ would need to be around 13000, which is much larger than 1288.

What about 4-digit numbers where "13" appears in the middle, like X13Y? For example, 2130-2139, 1130-1139, etc. We already considered 1130-1139.

Let me reconsider 1130-1139. The block is 10 wide. With $a = 1$: same issue as before (10-wide block, need 9 inside with endpoints outside).

But what if we combine 1113 (feared) with 1130-1139 (feared)? 1113 and 1130 are 17 apart. With $a = 17$:
- $n + 17 = 1113 \Rightarrow n = 1096$
- $n + 34 = 1130$ (feared ✓)
- $n + 51 = 1147$ (fearless ✗)

Only 2 terms. Not enough.

What about $a = 1$ and using the range [1113, 1139]? The feared numbers in this range: 1113, 1130-1139. That's 1113, then a gap (1114-1129 fearless), then 1130-1139. Not 9 consecutive.

Hmm. Let me think about whether there are other blocks of feared numbers I'm missing.

What about numbers like 13000? No, too large.

What about 2-digit numbers? Only 13 is feared. Not enough.

What about 3-digit numbers? 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913. The only block is 130-139 (10 numbers).

What about numbers where "13" appears not at a "natural" boundary? Like 413 - the "13" is in the last two digits. Or 1301 - the "13" is in the first two digits. Or 2130 - "13" in the middle.

I think I've been comprehensive. The blocks of consecutive feared numbers are:
- 130-139 (10)
- 1130-1139 (10)
- 1300-1399 (100)
- 2130-2139 (10)
- 13130-13139 (10) [but this is within 13000-13999 which is all feared]
- etc.

And the singles (numbers with "13" not in a block): 13, 113, 213, 313, ..., 1213, 1413, etc.

For 9 AP terms to all be feared, the most promising approach is the 100-wide block [1300, 1399], which gives $n = 1288$.

But wait, can we use the block [1300, 1399] with a different $a$ to get a smaller $n$?

We need $n + a \geq 1300$ and $n + 9a \leq 1399$ and $n + 10a > 1399$ (or $n + 10a$ fearless for another reason) and $n < 1300$ and $n$ fearless.

What if $n + 10a$ is in [1300, 1399] but fearless? No, all numbers in [1300, 1399] contain "13", so they're all feared.

What if $n + 10a \leq 1399$ but $n + 10a$ is fearless? Impossible since all numbers in [1300, 1399] are feared.

So we need $n + 10a \geq 1400$ or $n + 10a < 1300$. Since $n + 10a > n + 9a \geq n + a \geq 1300$, we need $n + 10a \geq 1400$.

Also, what if $n + 10a \geq 1400$ but contains "13"? Like 1413. Then $n + 10a$ would be feared, which is bad.

$n + 10a \in [1400, 1400 + 10a - 1]$ roughly. For $a = 12$, $n + 10a = n + 120 \in [1408, 1411]$ (for $n \in [1288, 1291]$). Let me check: 1408, 1409, 1410, 1411 - none contain "13". ✓.

For $a = 11$, $n + 10a = n + 110 \in [1400, 1409]$ (for $n \in [1290, 1299]$). 1400-1409: none contain "13". ✓.

Now, can we use $a = 13$? Then $n + 13 \geq 1300 \Rightarrow n \geq 1287$. $n + 117 \leq 1399 \Rightarrow n \leq 1282$. But $1287 > 1282$, contradiction. So $a = 13$ doesn't work (the block isn't wide enough: $9 \times 13 = 117 > 99$).

For $a = 12$: $9 \times 12 = 108 < 100$? No, $108 > 99$. Wait, the block is 100 wide (1300 to 1399 inclusive, that's 100 numbers). $9a = 108 > 99$. So $n + 9a - (n + a) = 8a = 96 \leq 99$. ✓. The condition is $8a \leq 99$, i.e., $a \leq 12$.

For $a = 12$: $n \in [1288, 1291]$. Minimum $n = 1288$.
For $a = 11$: $n \in [1290, 1299]$. Minimum $n = 1290$.

So $a = 12$ gives the smallest $n = 1288$ from this block.

Now, can we use a different approach entirely to get $n < 1288$?

Let me think about using the block [130, 139] combined with other feared numbers, with a carefully chosen $a$.

The idea: some of the 9 terms $n + a, \ldots, n + 9a$ are in [130, 139], and others are feared singles like 213, 313, etc.

For a term to be in [130, 139]: $n + ka \in [130, 139]$.
For a term to be a feared single: $n + ka \in \{13, 113, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1213\}$.

The singles are roughly 100 apart. If $a \approx 100$, we could hit multiple singles. But $a < 100$.

Let me try $a = 99$. The AP terms are $n + 99, n + 198, \ldots, n + 891$.

If $n + 99 = 130$, $n = 31$. Terms: 130, 229, 328, 427, 526, 625, 724, 823, 922. Only 130 is feared. ✗.

If $n + 99 = 213$, $n = 114$. Terms: 213, 312, 411, 510, 609, 708, 807, 906, 1005. Only 213 is feared. ✗.

The problem is that with $a = 99$, consecutive terms are 99 apart, and the feared singles are 100 apart, so we miss them.

What about $a = 100 - 1 = 99$ but starting from a different point? The feared singles are at 213, 313, 413, ..., 913 (100 apart). With $a = 99$, the terms drift by 1 each step. So if the first term is 213, the next is 312 (off by 1 from 313). If the first is 214, it's not feared. 

What if we use $a = 100$? Not allowed.

What about $a = 50$? Terms are 50 apart. Feared numbers 50 apart? 113 and 163 (not feared). 130 and 180 (not feared). 213 and 263 (not feared). Doesn't seem to work.

What about $a = 25$? 113, 138 (feared, in [130,139]), 163 (not feared). Only 2.

$a = 17$? 113, 130 (feared), 147 (not feared). Only 2.

$a = 83$? 130, 213 (feared), 296 (not). Only 2.

$a = 74$? 139, 213 (feared), 287 (not). Only 2.

Hmm, it seems really hard to get 9 feared terms without using a wide block.

Let me try yet another approach. What if we use the block [1130, 1139] (10 wide) with a small $a$, and some terms are also feared because they contain "13" elsewhere?

With $a = 1$: terms $n+1, \ldots, n+9$ in [1130, 1138] or [1131, 1139]. As before, one endpoint falls in the block.

But what if $n + 10$ is feared for a DIFFERENT reason? We need $n + 10$ to be fearless, not feared. So this doesn't help.

What if $n$ is feared for a different reason? We need $n$ to be fearless. So this doesn't help either.

What if some terms outside the [1130, 1139] block are feared for other reasons? For example, with $a = 1$ and $n = 1112$: $n + 1 = 1113$ (feared), $n + 2 = 1114$ (fearless). ✗.

With $a = 1$ and $n = 1129$: $n + 1 = 1130, \ldots, n + 9 = 1138$ (all feared), $n + 10 = 1139$ (feared). ✗.

With $a = 1$ and $n = 1130$: $n$ is feared. ✗.

So $a = 1$ doesn't work with the 1130-1139 block.

What about $a = 2$ with the 1130-1139 block? We need 9 terms ($n+2, n+4, \ldots, n+18$) all feared. The block has 10 numbers, and with step 2, we can hit at most 5 of them. The other 4 need to be feared for other reasons. The nearest other feared numbers are 1113 (17 below 1130) and 1213 (74 above 1139). With $a = 2$, the terms outside the block would be at most 18 away from the block, so they'd be in [1112, 1129] or [1140, 1157]. In [1112, 1129], only 1113 is feared. In [1140, 1157], none are feared. So at most 1 additional feared number. Total: 5 + 1 = 6 < 9. ✗.

What about $a = 3$? Similar analysis. Block hits at most 4, plus maybe 1113. Not enough.

I'm becoming more convinced that 1288 is the answer, but let me think about whether there's a cleverer approach.

What about using TWO blocks? Like [130, 139] and [1130, 1139]? They're 1000 apart. With $a \approx 125$, we could have some terms in each block. But $a < 100$, so the spread $9a < 900 < 1000$. Can't reach both blocks.

What about [130, 139] and [1300, 1399]? They're about 1160-1270 apart. $9a < 900$. Can't reach both.

What about using the block [1300, 1399] but with $n$ much smaller, and some terms before the block are feared for other reasons?

For example, $n = 1200, a = 12$. Terms: 1212, 1224, 1236, 1248, 1260, 1272, 1284, 1296, 1308. Only 1308 is in [1300, 1399]. The rest: 1212 (fearless), 1224 (fearless), etc. ✗.

For $n = 1200, a = 13$. Terms: 1213 (feared ✓), 1226 (fearless ✗).

$n = 1200, a = 100$: not allowed.

Hmm. What if $a$ is chosen so that multiple terms land on feared singles AND in the block?

The feared singles near 1300: 1213, 1313 (but 1313 is in [1300, 1399], so it's already counted).

Actually, 1213 is the last feared single before 1300. The next is 1413 (after 1399).

So for $n < 1300$, the only feared numbers near 1300 are 1213 and then the block [1300, 1399].

If we want some terms to be 1213 and others in [1300, 1399]:
$1213 + a \approx 1300 \Rightarrow a \approx 87$.
With $a = 87$: $n + 87 = 1213 \Rightarrow n = 1126$. Terms: 1213 (feared), 1300 (feared), 1387 (feared), 1474 (fearless). Only 3 feared. ✗.

With $a = 87$ and $n + 87 = 1213$: $n = 1126$. Terms: 1213, 1300, 1387, 1474, 1561, 1648, 1735, 1822, 1909. Feared: 1213 ✓, 1300 ✓, 1387 ✓, 1474 ✗. Only 3.

What about $a = 87$ and starting differently? $n + 87 = 1300 \Rightarrow n = 1213$ (feared). ✗.

I don't think combining singles with the block works well because the singles are too sparse.

Let me try another approach: what if "13" appears in a different position, like the ten-thousands position?

For 5-digit numbers: 13000-13999 (10000 numbers, all feared). But $n$ would be around 13000, much larger than 1288.

What about 4-digit numbers where "13" appears in the middle two digits? Like X13Y where X ≠ 0. These are 2130-2139, 1130-1139, 3130-3139, etc. Wait, no. X13Y means the number is X*1000 + 130 + Y = X*1000 + 13Y. For X=1: 1130-1139. For X=2: 2130-2139. Etc.

We already considered 1130-1139. The next is 2130-2139, which would give $n \approx 2128$, much larger.

What about numbers where "13" appears in the last two digits? These are numbers ending in 13: 13, 113, 213, 313, ..., 1213, 1313, 1413, etc. These are 100 apart.

And numbers where "13" appears in the first two digits of a 4-digit number: 1300-1399 (all 100 of them).

I think 1288 is likely the answer. But let me also check: can we use the block [1300, 1399] with $n < 1288$ by having $n + 10a$ be outside [1400, ...) and fearless, while $n + 10a < 1400$?

We need $n + 10a$ to be fearless and $n + 10a \leq 1399$. But all numbers in [1300, 1399] are feared. So $n + 10a \leq 1299$ or $n + 10a \geq 1400$.

If $n + 10a \leq 1299$: then $n + 9a < n + 10a \leq 1299 < 1300$, so $n + 9a < 1300$, meaning $n + 9a$ is not in [1300, 1399]. But we need $n + 9a$ to be feared. So $n + 9a$ must be feared for another reason. The nearest feared number below 1300 is 1213. So $n + 9a = 1213$ and $n + 10a \leq 1299$.

$n + 9a = 1213$ and $n + a \geq 1300$? That gives $n \geq 1300 - a$ and $n = 1213 - 9a$. So $1213 - 9a \geq 1300 - a \Rightarrow -87 \geq 8a \Rightarrow a \leq -11$. Impossible since $a > 0$.

So $n + 9a$ can't be below 1300 while $n + a \geq 1300$. So all 9 terms must be in [1300, 1399], and $n + 10a \geq 1400$.

This confirms: $n \in [1288, 1299]$ for $a \in \{11, 12\}$, with minimum $n = 1288$ at $a = 12$.

But wait, I should also check: can we have $n + 10a \geq 1400$ but $n + 10a$ is feared (contains "13")? Then it wouldn't work. Let me check for $a = 12, n = 1288$: $n + 120 = 1408$. "1408" - no "13" - fearless. ✓.

For $a = 12, n = 1289$: $n + 120 = 1409$. "1409" - no "13" - fearless. ✓.
For $a = 12, n = 1290$: $n + 120 = 1410$. "1410" - no "13" - fearless. ✓.
For $a = 12, n = 1291$: $n + 120 = 1411$. "1411" - no "13" - fearless. ✓.

All good. And $n = 1288$ is the minimum.

Now, let me also think about whether there might be a solution with $n < 1288$ using a completely different mechanism that I haven't considered.

What if the "13" appears due to carrying? For example, if $n = 1299$ and $a = 1$, then $n + 1 = 1300$ which has "13". But we already considered $a = 1$.

What if we use numbers where "13" appears in a non-standard way? Like 1300 has "13" at the start, 1130 has "13" in the middle, 1313 has "13" twice. I think I've covered all cases.

Let me also consider: what if $n$ is a 1-digit or 2-digit number? Then $n + 10a < 100 + 990 = 1090$. The feared numbers up to 1090: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013.

For 9 AP terms to all be feared: we need 9 of these to be in AP with common difference $a < 100$. The differences between consecutive feared numbers: 13→113: 100, 113→130: 17, 130→139: 1, 139→213: 74, 213→313: 100, etc.

For an AP with 9 terms, the differences between consecutive terms must all equal $a$. So we need 9 feared numbers in AP. The feared numbers up to 1090 are: 13, 113, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 213, 313, 413, 513, 613, 713, 813, 913, 1013.

An AP of 9 terms from these: the common difference must be constant. Looking at the list, the only AP-like sequences are:
- 130, 131, 132, ..., 139 (AP with $a = 1$, 10 terms)
- 213, 313, 413, 513, 613, 713, 813, 913 (AP with $a = 100$, 8 terms - but $a = 100$ not allowed)

With $a = 1$ and the 130-139 block: we need 9 terms, but the 10th term (either 129 or 140) must be fearless, and the other endpoint must also be fearless. As computed, this doesn't work because one of $n, n+10$ falls in the block.

So no solution with $n < 100$.

For $n < 1300$ in general: I've shown that the only AP of 9 feared numbers with $a < 100$ that works is using the block [1300, 1399], giving $n = 1288$.

Actually wait, I haven't fully explored all possibilities. Let me think about whether there could be an AP of 9 feared numbers with $a < 100$ that doesn't use a single block but combines multiple sources.

For example, could we have an AP where some terms are in [130, 139], some are singles like 213, 313, etc.?

The key constraint is that all 9 terms must be in AP with the same $a$. So the differences between consecutive terms are all $a$.

If one term is 130 and another is 213, then $a | (213 - 130) = 83$. So $a$ divides 83. Since 83 is prime, $a = 83$ or $a = 1$.

With $a = 83$: terms are $n + 83, n + 166, \ldots, n + 747$. If $n + 83 = 130$, terms are: 130, 213, 296, 379, 462, 545, 628, 711, 794. Feared: 130 ✓, 213 ✓, 296 ✗. Only 2.

If $n + 83 = 47$, terms: 130, 213, 296, ... same thing.

With $a = 1$: we need 9 consecutive feared numbers. The only runs of consecutive feared numbers are the blocks (130-139, 1130-1139, 1300-1399, etc.). We've shown these don't work with $a = 1$.

What about terms that are 100 apart (the singles)? $a = 100$ not allowed.

What about $a = 50$? Terms 50 apart. Feared numbers 50 apart? 113 and 163 (not feared). 130 and 180 (not). 213 and 263 (not). No.

$a = 25$? 113, 138 (feared), 163 (not). Only 2.

$a = 17$? 113, 130 (feared), 147 (not). Only 2.

$a = 74$? 139, 213 (feared), 287 (not). Only 2.

I really can't find any AP of 9 feared numbers with $a < 100$ other than using the [1300, 1399] block.

Let me also consider: what about using the block [1300, 1399] with a non-standard $a$ where not all 9 terms are in the block, but some are feared for other reasons?

For example, $a = 12, n = 1287$: $n + 12 = 1299$ (fearless ✗). Doesn't work.

$a = 12, n = 1288$: all 9 terms in [1300, 1399]. ✓. This is our solution.

$a = 13, n = 1287$: $n + 13 = 1300$ (feared), $n + 26 = 1313$ (feared), ..., $n + 117 = 1404$ (fearless). Wait, $n + 9 \times 13 = 1287 + 117 = 1404$. But 1404 is not in [1300, 1399]. Let me check: $n + 13 = 1300$, $n + 26 = 1313$, $n + 39 = 1326$, $n + 52 = 1339$, $n + 65 = 1352$, $n + 78 = 1365$, $n + 91 = 1378$, $n + 104 = 1391$, $n + 117 = 1404$. 

So $n + 9a = 1404$ which is outside [1300, 1399]. Is 1404 feared? "1404" - no "13" - fearless. ✗. So the 9th term is fearless. Doesn't work.

But wait, what if $n + 9a = 1391$ is feared (it's in [1300, 1399]) and $n + 10a = 1404$ is fearless? Let me recount. $n + ka$ for $k = 1, \ldots, 9$:
- $k=1$: 1300 (feared ✓)
- $k=2$: 1313 (feared ✓)
- $k=3$: 1326 (feared ✓)
- $k=4$: 1339 (feared ✓)
- $k=5$: 1352 (feared ✓)
- $k=6$: 1365 (feared ✓)
- $k=7$: 1378 (feared ✓)
- $k=8$: 1391 (feared ✓)
- $k=9$: 1404 (fearless ✗)

So $k=9$ gives 1404 which is fearless. We need all 9 to be feared. ✗.

So $a = 13$ doesn't work because $9 \times 13 = 117 > 99$, so the 9th term escapes the block.

This confirms $a \leq 12$ for the [1300, 1399] block, and $a = 12$ gives the minimum $n = 1288$.

Now let me also think about whether there's a solution with $n < 1288$ using the block [1300, 1399] but with $n + 10a$ being in [1300, 1399] and somehow fearless. But all numbers in [1300, 1399] contain "13", so none are fearless. So $n + 10a$ must be $\geq 1400$.

And $n$ must be $< 1300$ (if $n \geq 1300$, it's feared). Actually, $n$ could be $\geq 1400$ if $n$ is fearless, but then $n + a > n \geq 1400$, and we'd need $n + a, \ldots, n + 9a$ to be feared. The next block is [13000, 13999] which is way too far. Or we'd need to use singles, which we've shown don't work for 9 terms.

So $n < 1300$, and the minimum is $n = 1288$.

Actually, hold on. Let me reconsider. What if $n$ is between 1400 and 12999, and we use a different block or combination?

The next block after [1300, 1399] is [1130, 1139] (already considered, doesn't work) and [2130, 2139] (10 wide, same issue as [130, 139]).

What about [13130, 13139]? This is within [13000, 13999] which is all feared. But $n$ would be around 13000+, much larger than 1288.

What about using the block [1300, 1399] from above, i.e., $n$ slightly below 1300? We've found $n = 1288$.

I'm now fairly confident the answer is $n = 1288$. But let me do one more check: are there any feared numbers between 1288 and 1300 that I might be missing?

1288: "1288" - no "13" - fearless
1289: "1289" - no "13" - fearless
1290: "1290" - no "13" - fearless
...
1299: "1299" - no "13" - fearless

All fearless. Good.

And 1400-1411:
1400: "1400" - no "13" - fearless
...
1411: "1411" - no "13" - fearless

All fearless. Good.

So the answer is $n = 1288$.

Wait, actually I want to double-check one more thing. Let me make sure there's no solution with $n < 1288$ using a completely different approach that I might have missed.

What if we use numbers where "13" appears due to the interaction of different digit positions? For example, consider a number like 130. The "13" is in the hundreds-tens position. Or 1300, where "13" is in the thousands-hundreds position.

I've been considering blocks where "13" appears at a fixed position. But what if "13" appears at different positions for different terms?

For example, with $a = 87$:
- $n + 87 = 1130$ (feared, "13" at hundreds-tens)
- $n + 174 = 1217$ (fearless)

No, this doesn't help because the terms are too far apart to all be feared.

What about $a = 100 - 87 = 13$? We already checked $a = 13$ doesn't work with the [1300, 1399] block.

What about $a = 13$ with a different block? [130, 139]: $9 \times 13 = 117 > 9$ (block width is 10). Doesn't fit.

I think I've been thorough enough. Let me also consider whether there might be a solution using numbers in the 10000-13000 range with a smaller $n$... no, those are all larger than 1288.

Let me also consider: what if $n$ is very small, like $n = 1$, and $a$ is chosen carefully?

$n = 1, a = 12$: terms 13, 25, 37, 49, 61, 73, 85, 97, 109. Only 13 is feared. ✗.

$n = 1, a = 14$: terms 15, 29, 43, 57, 71, 85, 99, 113, 127. Only 113 is feared. ✗.

$n = 1, a = 56$: terms 57, 113, 169, 225, 281, 337, 393, 449, 505. Only 113 is feared. ✗.

No luck with small $n$.

Let me try to think about this more carefully. Is there any set of 9 feared numbers in AP with common difference $< 100$ that are all below 1300?

The feared numbers below 1300: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

For 9 of these to be in AP with $a < 100$:
- The 130-139 block has 10 consecutive numbers. An AP with $a = 1$ gives 9 consecutive, but we showed the endpoints don't work.
- An AP with $a = 1$ and 9 terms from 130-139: e.g., 130-138. Then $n = 129, n + 10 = 139$ (feared). ✗. Or 131-139: $n = 130$ (feared). ✗.
- Any other AP? The singles are 100 apart, so $a = 100$ (not allowed). Mixed blocks and singles: differences vary, hard to form AP.

I'm convinced: the answer is $\boxed{1288}$.

Actually, let me reconsider one more time. I want to make sure I haven't missed any feared numbers.

A number is feared if its decimal representation contains "13" as a contiguous substring. Let me list all feared numbers up to 1300:

1-digit: none
2-digit: 13
3-digit: 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913
4-digit (up to 1299): 1013, 1113, 1130-1139, 1213

Let me verify:
- 113: "113" contains "13" ✓
- 130-139: "13X" contains "13" ✓
- 213: "213" contains "13" ✓
- 313-913: same pattern ✓
- 1013: "1013" contains "13" ✓
- 1113: "1113" contains "13" ✓
- 1130-1139: "113X" contains "13" ✓
- 1213: "1213" contains "13" ✓

Any others? What about 131? "131" contains "13" ✓ (already in 130-139). 132? ✓ (in 130-139).

What about 1031? "1031" - does it contain "13"? "10", "03", "31" - no "13". Fearless. ✓ (not feared).

What about 1103? "1103" - "11", "10", "03" - no "13". Fearless.

What about 1203? "1203" - no "13". Fearless.

What about 1013? Already listed. ✓.

What about 1103-1112? Let me check 1113: "1113" - "11", "11", "13" - yes, "13" at the end. ✓.

What about 1231? "1231" - "12", "23", "31" - no "13". Fearless.

What about 1293? "1293" - no "13". Fearless.

I think my list is complete. The feared numbers below 1300 are exactly: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

No 9 of these form an AP with $a < 100$ (other than the 130-139 block with $a = 1$, which doesn't work due to endpoint issues).

Therefore, the smallest $n$ is $\boxed{1288}$.

Let me write up the proof now.

Actually, let me reconsider once more whether the 130-139 block with $a=1$ truly doesn't work, but with a twist: what if $n$ or $n+10$ is feared for a different reason but we need them fearless?

With $a = 1$:
- Option 1: $n+1 = 130, \ldots, n+9 = 138$. Then $n = 129$ (fearless ✓), $n+10 = 139$ (feared ✗).
- Option 2: $n+1 = 131, \ldots, n+9 = 139$. Then $n = 130$ (feared ✗), $n+10 = 140$ (fearless ✓).

Neither works. Confirmed.

What about $a = 1$ with a different set of 9 feared numbers? We need 9 consecutive integers all feared, with the neighbors fearless. The only runs of consecutive feared numbers below 1300 are:
- 130-139 (10 long): neighbors 129 (fearless) and 140 (fearless), but the run is 10 long, not 9.
- 1130-1139 (10 long): same issue.

So there's no run of exactly 9 consecutive feared numbers with fearless neighbors. The runs are all 10 long.

What about $a = 1$ with the 100-long block [1300, 1399]? We need 9 consecutive in [1300, 1399] with $n$ and $n+10$ fearless. $n$ must be $< 1300$ (else feared) and $n + 10$ must be $> 1399$ (else feared) or $< 1300$ (impossible since $n + 10 > n + 9 \geq 1300$). So $n + 10 \geq 1400$, meaning $n \geq 1390$. But $n < 1300$. Contradiction. So $a = 1$ doesn't work with [1300, 1399] either.

OK, I'm now fully confident. The answer is $n = 1288$.

Let me write a clean proof.

Proof outline:
1. Show that $n = 1288$ works with $a = 12$.
2. Show that no $n < 1288$ works.

For part 2, I need to show that for any $n < 1288$ and any $a < 100$, it's impossible to have $n, n+10a$ fearless and $n+a, \ldots, n+9a$ all feared.

The key argument: for $n + a, \ldots, n + 9a$ to all be feared, they must all contain "13". The spread is $8a \leq 8 \times 99 = 792$. 

For $n < 1288$, the range $[n+a, n+9a] \subseteq [1, 1288 + 792] = [1, 2080]$.

The feared numbers up to 2080: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213, 1300-1399, 1413, 1513, 1613, 1713, 1813, 1913, 2013.

Hmm wait, for $n < 1288$, $n + 9a$ could be up to $1287 + 891 = 2178$. So the range extends beyond 1300.

So for $n < 1288$, the 9 terms could potentially span across 1300, using the [1300, 1399] block. Let me reconsider.

If $n < 1288$ and some terms are in [1300, 1399]:
- $n + a \geq 1300 \Rightarrow n \geq 1300 - a$
- $n + 9a \leq 1399 \Rightarrow n \leq 1399 - 9a$
- $n + 10a \geq 1400 \Rightarrow n \geq 1400 - 10a$
- $n < 1300$

From $n \geq 1300 - a$ and $n < 1300$: $a \geq 1$.
From $n \geq 1400 - 10a$ and $n < 1300$: $10a > 100 \Rightarrow a \geq 11$.
From $n \leq 1399 - 9a$ and $n \geq 1300 - a$: $8a \leq 99 \Rightarrow a \leq 12$.

So $a \in \{11, 12\}$, same as before.

For $a = 12$: $n \in [1288, 1291]$. Minimum $n = 1288$.
For $a = 11$: $n \in [1290, 1299]$. Minimum $n = 1290$.

Both give $n \geq 1288$. So for $n < 1288$, we can't have all 9 terms in [1300, 1399].

But could some terms be in [1300, 1399] and others feared for different reasons? Let me think about this.

If not all 9 terms are in [1300, 1399], then some terms are below 1300 or above 1399. 

Case 1: Some terms below 1300. These must be feared for other reasons (being in [130, 139], or being a single like 1213, etc.).

Case 2: Some terms above 1399. These must be feared for other reasons (being 1413, 1513, etc.).

For Case 1: The feared numbers just below 1300 are: 1213 (at 1213), and 1130-1139 (at 1130-1139). The gap between 1213 and 1300 is 87. The gap between 1139 and 1300 is 161.

If a term is at 1213 and the next term is in [1300, 1399], then $a \geq 1300 - 1213 = 87$. With $a = 87$: the terms would be 1213, 1300, 1387, 1474, ... The third term (1387) is in [1300, 1399] ✓, but the fourth (1474) is fearless ✗. So only 3 terms are feared.

For more terms to be feared, we'd need more terms in [1300, 1399]. With $a = 87$: $n + 87 = 1213 \Rightarrow n = 1126$. Terms: 1213, 1300, 1387, 1474, 1561, 1648, 1735, 1822, 1909. Feared: 1213 ✓, 1300 ✓, 1387 ✓, 1474 ✗. Only 3.

With $a = 87$ and different starting point: $n + 87 = 1300 \Rightarrow n = 1213$ (feared). ✗.

With $a = 43$: $n + 43 = 1213 \Rightarrow n = 1170$. Terms: 1213, 1256, 1299, 1342, 1385, 1428, 1471, 1514, 1557. Feared: 1213 ✓, 1342 ✓, 1385 ✓, 1514 ✗. Only 3.

Hmm, it seems like we can get at most 3-4 feared terms this way, not 9.

For Case 2: The feared numbers just above 1399 are: 1413 (at 1413), 1513, etc. With $a$ small enough, some terms could be in [1300, 1399] and some at 1413.

$1413 - 1399 = 14$. So if $a = 14$ and the last term in the block is 1399, the next would be 1413. But we need 9 terms total. With $a = 14$: $n + 14, n + 28, \ldots, n + 126$. If $n + 14 = 1300$, terms: 1300, 1314, 1328, 1342, 1356, 1370, 1384, 1398, 1412. 1412 is fearless ("1412" - no "13"). ✗. Only 8 feared.

If $n + 14 = 1286$, $n = 1272$. Terms: 1286 (fearless ✗). 

If $n + 14 = 1300$, $n = 1286$. Terms: 1300, 1314, 1328, 1342, 1356, 1370, 1384, 1398, 1412. 1412 is fearless. ✗.

If $n + 14 = 1299$, $n = 1285$. Terms: 1299 (fearless ✗).

With $a = 14$, the 9th term is $n + 126$. If $n + 14 = 1300$, $n + 126 = 1412$ (fearless). If $n + 14 = 1301$, $n + 126 = 1413$ (feared!). Let me check: $n = 1287$, $n + 14 = 1301$ (feared ✓), $n + 28 = 1315$ (feared ✓), ..., $n + 112 = 1399$ (feared ✓), $n + 126 = 1413$ (feared ✓). 

Wait, let me recalculate. $n = 1287, a = 14$:
- $n + 14 = 1301$ (feared ✓)
- $n + 28 = 1315$ (feared ✓)
- $n + 42 = 1329$ (feared ✓)
- $n + 56 = 1343$ (feared ✓)
- $n + 70 = 1357$ (feared ✓)
- $n + 84 = 1371$ (feared ✓)
- $n + 98 = 1385$ (feared ✓)
- $n + 112 = 1399$ (feared ✓)
- $n + 126 = 1413$ (feared ✓)

All 9 are feared! Now check $n$ and $n + 10a$:
- $n = 1287$: "1287" - no "13" - fearless ✓
- $n + 140 = 1427$: "1427" - no "13" - fearless ✓

This works! $n = 1287$ with $a = 14$!

That's smaller than 1288! Let me double-check all the terms.

$n = 1287, a = 14$:
- $n = 1287$: "1287" → fearless ✓
- $n + a = 1301$: "1301" → "13" at start → feared ✓
- $n + 2a = 1315$: "1315" → "13" at start → feared ✓
- $n + 3a = 1329$: "1329" → "13" at start → feared ✓
- $n + 4a = 1343$: "1343" → "13" at start → feared ✓
- $n + 5a = 1357$: "1357" → "13" at start → feared ✓
- $n + 6a = 1371$: "1371" → "13" at start → feared ✓
- $n + 7a = 1385$: "1385" → "13" at start → feared ✓
- $n + 8a = 1399$: "1399" → "13" at start → feared ✓
- $n + 9a = 1413$: "1413" → "13" at end → feared ✓
- $n + 10a = 1427$: "1427" → no "13" → fearless ✓

All conditions satisfied! $n = 1287 < 1288$.

So my earlier analysis was incomplete - I only considered the case where all 9 terms are in [1300, 1399], but here the 9th term (1413) is outside the block and feared for a different reason (it ends in "13").

Can we do even better? Let me explore this direction.

The idea: 8 terms in [1300, 1399] and 1 term at 1413 (which is $\equiv 13 \pmod{100}$).

$1413 - 1300 = 113$. The 8 terms in [1300, 1399] span $7a$ (from first to 8th), and the 9th term is at $1413$. So the 8th term is at $1413 - a$, and the 1st term is at $1413 - 8a$.

We need:
- $1413 - 8a \geq 1300 \Rightarrow 8a \leq 113 \Rightarrow a \leq 14$
- $1413 - a \leq 1399 \Rightarrow a \geq 14$

So $a = 14$ exactly. And $n + 9a = 1413 \Rightarrow n = 1413 - 126 = 1287$.
$n + a = 1301 \geq 1300$ ✓.
$n + 8a = 1399 \leq 1399$ ✓.
$n = 1287 < 1300$ ✓.
$n + 10a = 1427$. Is 1427 fearless? "1427" - no "13" - fearless ✓.

So $n = 1287$ works. Can we extend this idea further?

What if we have 7 terms in [1300, 1399], 1 at 1413, and 1 at 1513?

$1513 - 1413 = 100$. So $a | 100$. And $a | (1413 - 1300) = 113$... wait, the terms need to be equally spaced. If the 8th term is 1413 and the 9th is 1513, then $a = 100$. Not allowed.

What about 7 terms in [1300, 1399], 1 at 1413, and 1 below 1300 (like 1213)?

$1413 - 1213 = 200$. If these are 8 apart in the AP, $a = 200/8 = 25$. Let me check: $n + a = 1213, n + 2a = 1238, \ldots$. Wait, I need to figure out which terms are which.

Let me think about this differently. We have 9 terms: $n+a, n+2a, \ldots, n+9a$. Some are in [1300, 1399], some are at 1413, some at 1213, etc.

The terms $n+ka$ for $k = 1, \ldots, 9$ form an AP with common difference $a$. The feared numbers we can use are:
- 1213 (single)
- 1300-1399 (block)
- 1413 (single)
- 1513 (single)
- etc.

For a term to be at 1213: $n + ka = 1213$ for some $k$.
For a term to be at 1413: $n + ja = 1413$ for some $j$.
$1413 - 1213 = 200 = (j - k) \cdot a$. So $a | 200$ and $a < 100$. Possible: $a \in \{1, 2, 4, 5, 8, 10, 20, 25, 40, 50\}$.

And the terms between 1213 and 1413 (i.e., $n + (k+1)a, \ldots, n + (j-1)a$) must all be feared. These terms are in the range $(1213, 1413)$. The feared numbers in this range are: 1300-1399. So all intermediate terms must be in [1300, 1399].

Number of intermediate terms: $j - k - 1$. These span from $1213 + a$ to $1413 - a$, and must all be in [1300, 1399].

$1213 + a \geq 1300 \Rightarrow a \geq 87$.
$1413 - a \leq 1399 \Rightarrow a \geq 14$.

So $a \geq 87$. Combined with $a | 200$ and $a < 100$: $a = 100$ (not < 100) or... $200 / 87 \approx 2.3$, not integer. The divisors of 200 that are $\geq 87$ and $< 100$: 100 (excluded). So none. 

Hmm, so we can't have both 1213 and 1413 as terms with all intermediates in [1300, 1399].

What about using 1413 and 1513? $1513 - 1413 = 100$. $a | 100$, $a < 100$. The intermediates between 1413 and 1513 must be feared. Feared numbers in (1413, 1513): none (1414-1512 are all fearless except... let me check. 1413 is feared. 1414: "1414" - no "13" - fearless. ... 1512: "1512" - no "13" - fearless. So no feared numbers between 1413 and 1513.) So we can't have intermediates between 1413 and 1513 that are feared. This means 1413 and 1513 must be consecutive terms, so $a = 100$. Not allowed.

What about using 1413 and having more terms above 1413 that are feared? The next feared number after 1413 is 1513 (100 away). With $a < 100$, we can't reach it.

What about using 1413 and having terms below 1300 that are feared? The feared number just below 1300 is 1213 (87 away). With $a = 14$ (our current solution), $1413 - 1213 = 200 = 14 \times 14.28...$, not a multiple of 14. So 1213 is not a term in the AP with $a = 14$.

Let me check: with $a = 14, n = 1287$: the terms are 1301, 1315, 1329, 1343, 1357, 1371, 1385, 1399, 1413. None of these is 1213. ✓.

Can we get $n < 1287$ by using a different combination?

Let me think about having terms at 1413 and 1313 (both feared, 100 apart). $a | 100$, $a < 100$. The intermediates between 1313 and 1413 must be feared. Feared numbers in (1313, 1413): 1314-1399 (all in [1300, 1399], all feared). So intermediates must be in [1314, 1399].

$1313 + a \geq 1314 \Rightarrow a \geq 1$ (trivially true).
$1413 - a \leq 1399 \Rightarrow a \geq 14$.

So $a \geq 14$ and $a | 100$ and $a < 100$: $a \in \{20, 25, 50\}$.

With $a = 20$: 1313 and 1413 are $100/20 = 5$ terms apart. So if 1313 is the $k$-th term and 1413 is the $(k+5)$-th term. The intermediates (4 terms) are at 1333, 1353, 1373, 1393 - all in [1300, 1399] ✓.

Now, we need 9 terms total. We have 6 terms (1313, 1333, 1353, 1373, 1393, 1413). We need 3 more, which must be feared. These could be below 1313 or above 1413.

Below 1313: the term before 1313 is $1313 - 20 = 1293$ (fearless ✗). So we can't extend below.

Above 1413: the term after 1413 is $1413 + 20 = 1433$ (fearless ✗). Can't extend above.

So with $a = 20$, we only get 6 feared terms. Not enough.

With $a = 25$: 1313 and 1413 are $100/25 = 4$ terms apart. Intermediates: 1338, 1363, 1388 - all in [1300, 1399] ✓. Total: 5 terms. Need 4 more.

Before 1313: $1313 - 25 = 1288$ (fearless ✗).
After 1413: $1413 + 25 = 1438$ (fearless ✗).

Only 5 terms. Not enough.

With $a = 50$: 1313 and 1413 are 2 terms apart. Intermediate: 1363 (in [1300, 1399] ✓). Total: 3 terms. Not enough.

So using both 1313 and 1413 doesn't give enough terms.

Let me go back to the approach that worked: 8 terms in [1300, 1399] and 1 at 1413, with $a = 14$.

Can we have 7 terms in [1300, 1399], 1 at 1413, and 1 at 1213?

$1413 - 1213 = 200$. With $a = 14$: $200/14 = 14.28...$, not integer. So 1213 and 1413 can't both be terms with $a = 14$.

What about 7 in [1300, 1399], 1 at 1413, and 1 at some other feared number below 1300?

The feared numbers below 1300: 13, 113, 130-139, 213, 313, 413, 513, 613, 713, 813, 913, 1013, 1113, 1130-1139, 1213.

With $a = 14$: the terms are $n + 14, n + 28, \ldots, n + 126$. If $n + 126 = 1413$, $n = 1287$. The terms are 1301, 1315, ..., 1399, 1413. The term before 1301 would be $1301 - 14 = 1287 = n$, which is fearless. So we can't add a term below 1300.

What if we use a different $a$? Let me think about having 7 terms in [1300, 1399], 1 at 1413, and 1 at 1213.

$1413 - 1213 = 200$. The 9 terms span $8a$. If 1213 is the 1st term and 1413 is the 9th: $8a = 200$, $a = 25$. Terms: 1213, 1238, 1263, 1288, 1313, 1338, 1363, 1388, 1413.

Check: 1213 (feared ✓), 1238 (fearless ✗). Doesn't work.

If 1213 is the 1st term and 1413 is the 8th: $7a = 200$, $a = 200/7$ (not integer).

If 1213 is the 2nd term and 1413 is the 9th: $7a = 200$, not integer.

If 1213 is the 1st and 1413 is the 7th: $6a = 200$, not integer.

Hmm, 200 = 8 × 25. So the only way is $a = 25$ with 1213 and 1413 being 8 terms apart (1st and 9th). But then the intermediate terms include 1238, 1263, 1288 which are fearless.

What about using 1130-1139 block? With $a = 14$: $1413 - 1130 = 283$. $283/14 = 20.2$, not integer. $1413 - 1139 = 274$. $274/14 = 19.57$, not integer.

What about using 1113? $1413 - 1113 = 300$. $300/14 = 21.4$, not integer.

OK so with $a = 14$, we can't combine 1413 with any feared number below 1300 to get more terms.

Let me try other values of $a$ where we can have 8 terms in [1300, 1399] and 1 at 1413.

We need: the 9th term is 1413, and terms 1-8 are in [1300, 1399].
- $n + 9a = 1413 \Rightarrow n = 1413 - 9a$
- $n + a \geq 1300 \Rightarrow 1413 - 8a \geq 1300 \Rightarrow a \leq 14$
- $n + 8a \leq 1399 \Rightarrow 1413 - a \leq 1399 \Rightarrow a \geq 14$

So $a = 14$ is the only option. $n = 1287$.

What about having 7 terms in [1300, 1399], 1 at 1413, and 1 at 1513?

$1513 - 1413 = 100$. $a | 100$. And the term at 1413 and 1513 are consecutive terms (since no feared numbers between them), so $a = 100$. Not allowed.

What about 7 in [1300, 1399], 1 at 1413, and 1 more that's also in [1300, 1399]? That's just 8 in [1300, 1399] and 1 at 1413, which is the case we already solved.

What about 8 in [1300, 1399] and 1 at 1513? $1513 - 1300 = 213$ (if 1st term is 1300 and 9th is 1513, $8a = 213$, not integer). $1513 - 1399 = 114$ (if 8th term is 1399 and 9th is 1513, $a = 114$, too big). 

Actually, let me be more careful. If the 9th term is 1513 and the 1st through 8th are in [1300, 1399]:
- $n + 9a = 1513 \Rightarrow n = 1513 - 9a$
- $n + a \geq 1300 \Rightarrow 1513 - 8a \geq 1300 \Rightarrow a \leq 26$
- $n + 8a \leq 1399 \Rightarrow 1513 - a \leq 1399 \Rightarrow a \geq 114$

$a \geq 114$ and $a \leq 26$: contradiction. So this doesn't work.

What about 7 in [1300, 1399], 1 at 1413, and 1 at 1513?

The 1413 and 1513 terms: $1513 - 1413 = 100$, so $a | 100$ and they are $100/a$ terms apart. Since there are no feared numbers between 1413 and 1513, they must be consecutive terms: $a = 100$. Not allowed.

What about 8 in [1300, 1399] and 1 at 1427? 1427 is "1427" -
