# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Along a circle, there are $n$ coins, each lying heads or tails up. If two adjacent coins lie the same way (both heads or both tails), it is allowed to flip both. Let $V(n)$ be the number of equivalence classes of coin arrangements, where two arrangements are in the same class if one can be obtained from the other by applying any number of such operations. Calculate the sum $\sum_{n=1}^{20} V(n)$.       — 题目文本
#   The original solution states that for odd $n$, there are $V(n) = 2$ variants (equivalence classes). For even $n$, there are $V(n) = n+1$ variants.
We need to compute the sum $S = \sum_{n=1}^{20} V(n)$.
The odd terms are $n=1, 3, 5, 7, 9, 11, 13, 15, 17, 19$. There are 10 such terms, and for each, $V(n) = 2$. Sum of odd terms = $10 \times 2 = 20$.
The even terms are $n=2, 4, 6, 8, 10, 12, 14, 16, 18, 20$. For each, $V(n) = n+1$.
The even values are $3, 5, 7, 9, 11, 13, 15, 17, 19, 21$.
Sum of even terms = $3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 = \frac{10}{2}(3 + 21) = 5 \times 24 = 120$.
Total sum = $20 + 120 = 140$.  — 标准解答
#   Let me solve this problem. We have n coins on a circle, each heads or tails. Operation: if two adjacent coins are the same (both H or both T), flip both. V(n) = number of equivalence classes under this operation. Compute sum from n=1 to 20.

Let me think about invariants. Represent coins as bits x_1,...,x_n in {0,1} on a circle. Operation: if x_i = x_{i+1}, flip both (i.e., x_i -> 1-x_i, x_{i+1} -> 1-x_{i+1}).

Let me think in terms of "differences". Define d_i = x_i XOR x_{i+1} (whether adjacent coins differ). The operation flips x_i and x_{i+1} when they're equal, i.e., when d_{i-1}... wait let me index carefully.

Actually let me think about what the operation does to the difference pattern. Let y_i = x_i XOR x_{i+1} for i=1..n (cyclic, so y_n = x_n XOR x_1).

The operation at position (i, i+1): requires x_i = x_{i+1}, i.e., y_i = 0. It flips both x_i and x_{i+1}.

After flipping x_i and x_{i+1}:
- y_{i-1} = x_{i-1} XOR x_i changes (since x_i flipped) -> y_{i-1} flips
- y_i = x_i XOR x_{i+1}: both flipped, so y_i unchanged (still 0)
- y_{i+1} = x_{i+1} XOR x_{i+2}: x_{i+1} flipped -> y_{i+1} flips

So the operation: pick i with y_i = 0, then flip y_{i-1} and y_{i+1}.

Interesting. So in the "difference" representation, we have a binary string y_1...y_n on a circle, with the constraint that sum of y_i is even (since it's a cycle, the number of transitions must be even). The operation: choose a position i where y_i=0, and flip y_{i-1} and y_{i+1}.

Note: the all-y configuration corresponds to x being alternating... but on a circle, alternating is only possible if n is even. The constraint is that the number of 1's in y is even.

Also, two x configurations map to the same y? No—given y and one value of x (say x_1), the rest is determined. But x_1 can be 0 or 1, giving complementary configurations. Complementary x (all bits flipped) gives the same y. So configurations x come in complementary pairs mapping to the same y, except... actually each y corresponds to exactly 2 x-configurations (x and its complement), as long as n≥1. For n=1, x_1 alone, complement is the other, y is empty/trivial.

Hmm, let me reconsider. The operation preserves y_i at the chosen position (stays 0) and flips the two neighbors. So the operation acts on y-strings.

But wait—the operation also changes x. Two x's with the same y are complements. Does the operation ever connect x to its complement? Let's see: the operation flips exactly 2 coins, so it changes the parity of number of heads. Complement changes all n coins. If n is even, complement preserves parity of heads; if n odd, complement flips parity. The operation flips 2 coins so preserves parity of heads. So:
- If n even: x and complement have same parity, could be connected.
- If n odd: x and complement have different parity, cannot be connected (since operation preserves parity).

Hmm, this is getting complex. Let me think more carefully about the structure.

Actually, let me reconsider. The equivalence classes of x under the operation. Let me think about what's invariant.

The operation flips two adjacent equal coins. Let me think about the parity of the number of heads, mod 2. Flipping two coins: if both were H (heads=1), they become T, so heads count -2. If both T, they become H, heads count +2. So parity of heads is preserved. That's one invariant.

Now let me think about the y = difference representation more. The operation on y: pick i with y_i=0, flip y_{i-1}, y_{i+1}.

Let me think of this as a game on the circle. We have a binary circular string with even number of 1s. Operation: at a 0-position, flip its two neighbors.

Let me think about what's invariant here. Consider the positions of 1's. The 1's come in pairs (since even count) — actually they partition into "arcs". Let me think of the 1's as "markers" and 0's as "gaps".

Hmm, let me think differently. Let me consider the gaps between consecutive 1's. The 1's divide the circle into arcs of 0's. If there are 2k ones, there are 2k arcs of zeros (some possibly empty). The operation at a 0-position i flips its neighbors y_{i-1}, y_{i+1}.

Case analysis: position i is a 0. Its neighbors y_{i-1} and y_{i+1} can be 0 or 1.
- If y_{i-1}=1, y_{i+1}=1: both flip to 0. So two 1's disappear, replaced by... the 0 at position i stays 0, and positions i-1, i+1 become 0. So a pattern "1 0 1" becomes "0 0 0". This merges arcs.
- If y_{i-1}=0, y_{i+1}=0: both flip to 1. Pattern "0 0 0" -> "1 0 1". Creates two new 1's.
- If y_{i-1}=1, y_{i+1}=0: becomes "0 0 1". A 1 moves.
- If y_{i-1}=0, y_{i+1}=1: becomes "1 0 0". A 1 moves.

So 1's can move around, be created/destroyed in pairs. The number of 1's changes by -2, 0, or +2. So parity of number of 1's is preserved (always even, which is automatic).

Hmm, what's invariant? Let me think about the "gaps" between consecutive 1's measured along the circle. Let the 1's be at positions p_1 < p_2 < ... < p_{2k}. The gaps are g_j = p_{j+1} - p_j (cyclic). Sum of gaps = n.

Operation "1 0 1" -> "0 0 0": removes two adjacent 1's (with exactly one 0 between them). This removes two consecutive 1's and merges three arcs into one.

Operation "0 0 0" -> "1 0 1": splits an arc of ≥3 zeros... wait, it needs three consecutive 0's: y_{i-1}=0, y_i=0, y_{i+1}=0, and we act at position i. This creates two 1's at i-1 and i+1.

Operation moving a 1: "1 0 0" -> "0 0 1" or "0 0 1" -> "1 0 0": a 1 moves by 2 positions.

So a 1 can move by 2 steps along the circle. And pairs of 1's separated by exactly one 0 can annihilate; and we can create pairs of 1's with one 0 between them from three 0's.

This is reminiscent of a chip-firing or a representation in terms of... Let me think about parity of positions.

Key insight: a 1 at position p can move to p+2 or p-2. So the parity (mod 2) of a 1's position is invariant for each 1! When two 1's annihilate (1 0 1 -> 0 0 0), the two 1's are at positions i-1 and i+1, which have the same parity. When two 1's are created (0 0 0 -> 1 0 1), they're at i-1 and i+1, same parity.

So the 1's come in two "colors": even-positioned and odd-positioned. The number of even-1's and odd-1's... when a 1 moves by 2, it stays same color. When two same-color 1's annihilate, that color count decreases by 2. When two same-color 1's created, color count +2. So parity of each color count is invariant!

Let me define: E = number of 1's at even positions, O = number of 1's at odd positions. Both E and O have their parities preserved. Since E+O is even (always), E and O have the same parity. So really there's one invariant: parity of E (equivalently parity of O).

Wait, but we also need to track: can we always reduce to a canonical form? Let me think about what configurations are reachable.

Claim: the invariant is (parity of E, parity of O) but since E+O even, these are equal, so just one bit: parity of E. Plus maybe something else?

Hmm wait, but also we should check: is the operation reversible? Yes, each operation is its own inverse (flipping twice returns). So it's a group action, equivalence classes = orbits.

Let me reconsider. Actually I realize the y-representation loses information about x vs complement. Let me back up.

x configurations: 2^n total. The map x -> y (differences) is 2-to-1 (x and complement give same y) for n ≥ 2. For n=1, y is empty, both x map to same y.

The operation on x induces the operation on y as described. But two x's with same y (complements) — are they in the same orbit or not?

Let me think about it differently. Let me just directly analyze orbits of x.

Actually, let me reconsider the whole approach. Let me think about small n by hand and find the pattern, then prove.

n=1: One coin. No adjacent pair (or is the coin adjacent to itself? On a circle of 1, the coin is adjacent to itself). If x_1 = x_1 (always true), flip both... but it's the same coin, flipping it twice = no change? Or is it a single coin adjacent to itself, so "flip both" means flip it... once? This is ambiguous. 

Convention: for n=1, the single coin is adjacent to itself. "Two adjacent coins" — if it's the same coin, flipping both means flipping it once (or twice = no change). Let me think about what's standard. Actually for n=1, typically the operation does nothing meaningful. Let me consider: if we flip "both" and they're the same coin, flipping twice = identity. So V(1) = 2 (two classes: H and T, no operation possible that changes anything). Actually if the coin is adjacent to itself and they're "the same way" (trivially), flipping both = flipping the single coin once? That would make H <-> T, giving V(1)=1.

This is ambiguous. Let me consider n=1 gives V(1)=2 (no valid operation since you need two distinct adjacent coins) — more standard. Hmm, but actually many problems consider n≥2. Let me just compute and see; the sum from 1 to 20, and n=1 contributes either 1 or 2.

Let me reconsider: the problem says "two adjacent coins". For n=1 there's only one coin, so no two adjacent coins exist. So no operation possible, V(1) = 2.

For n=2: two coins, adjacent to each other (and each adjacent to the other on both sides, but it's the same pair). Configurations: HH, HT, TH, TT. Operation: if two adjacent same, flip both. HH -> TT, TT -> HH. HT: coins differ, no operation. TH: differ, no operation. So classes: {HH, TT}, {HT}, {TH}. V(2) = 3.

Let me verify with y-representation. n=2: y_1 = x_1 XOR x_2, y_2 = x_2 XOR x_1 = y_1. So y = (0,0) or (1,1). 
- y=(0,0): x = HH or TT. These are complements. Operation on y: need y_i=0, flip neighbors. y=(0,0): act at i=1, y_1=0, flip y_0=y_2 and y_2. y_2=0->1, y_2=1... wait both neighbors are y_2 (since n=2, neighbors of position 1 are position 0=2 and position 2). So flip y_2 twice? = no change. Hmm, that's a degeneracy. So y=(0,0) stays. And x=HH <-> TT via operation. So one class. Good, {HH,TT}.
- y=(1,1): x = HT or TH. No operation possible (y_i=1 for both, can't act). So HT and TH are separate classes (they're complements, both parity... HT has 1 head, TH has 1 head, same parity, but no operation connects them). So 2 classes. Total V(2)=3. ✓.

OK so the y-representation: two x's with same y may or may not be in the same orbit. For y=(0,0), the two x's (HH, TT) are in same orbit. For y=(1,1), the two x's (HT, TH) are in different orbits.

So I can't just count y-orbits. Let me think again.

Let me think about the parity of heads more carefully. The operation preserves parity of number of heads. For n=2: HH (2 heads, even), TT (0, even) -> same class. HT (1, odd), TH (1, odd) -> different classes but same parity. So parity alone doesn't determine.

Hmm. So there's more structure. Let me think about n=3.

n=3: configurations 8 total. Parity of heads: even (0 or 2 heads) or odd (1 or 3 heads).
- Even: TTT, HHT, HTH, THH (0 or 2 heads)
- Odd: HHH, HTT, THT, TTH (3 or 1 head)

Operations (circle of 3, each adjacent pair): flip adjacent equal pair.
TTT: any pair is TT. Flip pair (1,2): TTT -> HHT. Flip (2,3): TTH. Flip (3,1): HTT. So TTT connects to HHT, TTH, HTT. But HTT is odd parity! Wait, TTT has 0 heads (even), flipping two T's to H's gives 2 heads (even). TTT -> HHT (flip 1,2), TTH (flip 2,3), HTT (flip 3,1). All have 2 heads, even. Good.

HHT: coins 1,2 = HH, flip -> TTT. Coins 2,3 = HT differ. Coins 3,1 = TH differ. So HHT <-> TTT.
Similarly TTH <-> TTT, HTT <-> TTT.
So {TTT, HHT, TTH, HTT} all connected. That's 4 configs, all even parity. So all even-parity configs form one class.

Odd parity: HHH, HTT, THT, TTH... wait TTH is even. Let me redo. Odd = 1 or 3 heads.
- HHH (3 heads): flip any pair (all HH) -> HHH with two flipped to T: e.g., flip (1,2): THH. THH has 2 heads, even! Wait that crosses parity. 

Hold on: HHH, flip coins 1,2 (both H) -> T,H,H = THH, 2 heads, even. But operation should preserve parity! 3 heads -> 2 heads is parity change. Contradiction!

Wait, flipping two heads to tails: heads go from 3 to 1. 1 is odd. THH = T,H,H = 2 heads. Wait no: THH means coin1=T, coin2=H, coin3=H. That's 2 heads. 3 -> 2? Flipping two H's to T: 3 - 2 = 1 head. But THH has 2 heads. 

I think I mislabeled. HHH flip coins 1 and 2: coin1 H->T, coin2 H->T, coin3 stays H. Result: T,T,H = TTH. TTH has 1 head, odd. OK I made an error. TTH = 1 head. Let me recount: T,T,H -> 1 head, odd. Good, parity preserved.

Let me redo n=3 carefully. Label coins 1,2,3. Config = (x1,x2,x3).
Even parity (0 or 2 heads): TTT, HHT, HTH, THH.
Odd parity (1 or 3 heads): HHH, TTH, THT, HTT.

TTT: flip (1,2)-> HHT; flip (2,3)-> THT? T,T,T flip 2,3 -> T,H,H = THH. flip (3,1)-> H,T,T = HTT. So TTT -> HHT, THH, HTT. These are even? HHT=2✓, THH=2✓, HTT=1? H,T,T = 1 head, odd! 

Wait, TTT flip coins 3 and 1: coin3 T->H, coin1 T->H, coin2 stays T. Result H,T,H = HTH, 2 heads. I keep making errors. Let me be very careful.

TTT = (T,T,T). 
- Flip (1,2): (H,H,T) = HHT, 2 heads even ✓
- Flip (2,3): (T,H,H) = THH, 2 heads even ✓
- Flip (3,1): (H,T,H) = HTH, 2 heads even ✓

So TTT -> {HHT, THH, HTH}. All even. Good.

HHT = (H,H,T). Pairs: (1,2)=HH same -> flip -> (T,T,T)=TTT. (2,3)=HT diff. (3,1)=TH diff. So HHT -> TTT only.
THH = (T,H,H). (1,2)=TH diff. (2,3)=HH -> flip -> (T,T,T)=TTT. (3,1)=HT diff. So THH -> TTT.
HTH = (H,T,H). (1,2)=HT diff. (2,3)=TH diff. (3,1)=HH -> flip -> (T,T,T)... wait flip coins 3,1: coin3 H->T, coin1 H->T, coin2 stays T. (T,T,T)=TTT. So HTH -> TTT.

So all even configs {TTT, HHT, THH, HTH} form one class. ✓

Odd configs: HHH, TTH, THT, HTT.
HHH=(H,H,H). Flip (1,2)->(T,T,H)=TTH. (2,3)->(H,T,T)=HTT. (3,1)->(T,H,T)=THT. So HHH -> {TTH, HTT, THT}.
TTH=(T,T,H). (1,2)=TT->flip->(H,H,H)=HHH. (2,3)=TH diff. (3,1)=HT diff. -> HHH.
THT=(T,H,T). (1,2)=TH diff. (2,3)=HT diff. (3,1)=TT->flip->(H,H,H)? flip coins 3,1: T->H, T->H, coin2 stays H. (H,H,H)=HHH. -> HHH.
HTT=(H,T,T). (1,2)=HT diff. (2,3)=TT->flip->(H,H,H)? flip 2,3: T->H,T->H, coin1 stays H. (H,H,H). (3,1)=TH diff. -> HHH.

So all odd configs {HHH, TTH, THT, HTT} form one class.

V(3) = 2.

So far: V(1)=2, V(2)=3, V(3)=2.

n=4: Let me use the y-representation and think about orbits, being careful about x vs complement.

Actually, let me think about the structure more generally. Let me reconsider using the y (difference) representation and track the invariant.

In y-space: circular binary string of length n, even number of 1's. Operation: at a 0, flip its two neighbors. The invariant I found: parity of (number of 1's at even positions). Let me call this the "index parity" invariant.

But wait, for n=2, y can be (0,0) or (1,1). 
- (0,0): 0 ones, E=0 (even). 
- (1,1): ones at positions 1,2. E = number at even positions = 1 (position 2). O = 1 (position 1). E odd. 
So these have different index parity, can't be connected. Good, 2 y-classes.

But V(2)=3, not 2. Because y=(1,1) corresponds to two x-configs (HT, TH) that are in different orbits. So the y-orbit count undercounts.

So I need to understand: for a given y-orbit, how many x-orbits does it correspond to?

Given y, the x-configs mapping to it are x and complement(x). Are x and complement in the same orbit?

The operation preserves parity of heads. complement changes heads count from h to n-h. Parity changes iff n is odd.

- If n odd: parity of h and n-h differ, so x and complement have different parity, can't be in same orbit. So each y-orbit gives 2 x-orbits (when y is reachable / has configs).
- If n even: parity of h and n-h same, so x and complement could be in same orbit. Need to determine.

For n=2 (even): y=(0,0): x=HH,TT, same orbit (1 x-orbit). y=(1,1): x=HT,TH, different orbits (2 x-orbits). So for n even it depends on y.

Hmm. So the relationship is subtle. Let me think about n even more carefully.

For n even, when are x and complement in the same orbit? 

Let me think about another invariant. Consider the "alternating sum" or some other quantity.

Let me think about the operation's effect on x directly. Operation: flip x_i, x_{i+1} when x_i = x_{i+1}.

Consider the quantity S = sum of x_i * (-1)^i or similar. Actually, let me think about it as: assign weights w_i to positions, and look at sum w_i x_i mod something. The operation flips x_i and x_{i+1} (when equal). The change in sum w_i x_i is w_i(1-2x_i) + w_{i+1}(1-2x_{i+1}). Since x_i = x_{i+1} = v, change = (w_i + w_{i+1})(1-2v). For this to be invariant mod 2 (i.e., mod 2 always 0), need w_i + w_{i+1} even, i.e., w_i ≡ w_{i+1} mod 2. So all w_i same parity. That just gives parity of total heads (w_i=1 all). Not helpful for more.

For invariance over integers (not just mod 2): change = ±(w_i+w_{i+1}), sign depends on v. Not invariant unless w_i + w_{i+1} = 0, i.e., w_{i+1} = -w_i, alternating weights. But on a circle, alternating requires n even. So for n even, w_i = (-1)^i, and the operation changes sum by (w_i + w_{i+1})(1-2v) = ((-1)^i + (-1)^{i+1})(...) = 0. So S = sum (-1)^i x_i is invariant for n even!

Let me verify n=2: S = (-1)^1 x_1 + (-1)^2 x_2 = -x_1 + x_2 (mod something). HH: -1+1=0. TT: 0+0=0. HT: -1+0=-1. TH: 0+1=1. So S distinguishes HT (S=-1) from TH (S=1), and HH=TT (S=0). That gives 3 classes! V(2)=3 ✓.

So for n even, S = sum_{i} (-1)^i x_i is an integer invariant. Range: from -n/2 to n/2 (if we use x_i in {0,1}, S ranges over integers with same parity as... ). Actually x_i ∈{0,1}, w_i = ±1. S = sum of ±x_i. With n/2 weights +1 and n/2 weights -1. S ranges from -n/2 to n/2, all integers (since we can choose each x_i). Actually S can be any integer from -n/2 to n/2? The +1 positions contribute 0 or 1 each, -1 positions contribute 0 or -1 each. So S = (number of heads in + positions) - (number of heads in - positions). Range: [0 - n/2, n/2 - 0] = [-n/2, n/2], all integers. So n+1 possible values.

But is S the only invariant for n even (combined with parity)? Wait, S already determines parity: S = (heads in +) - (heads in -), total heads = (heads in +) + (heads in -). Parity of total heads = parity of (heads in +) + (heads in -). And S = (heads in +) - (heads in -). So parity of total = parity of S + 2*(heads in -) = parity of S. So parity of heads = parity of S. So S encodes parity. Good, S is the invariant for n even, and it takes n+1 values. But are all values achievable and do they each give exactly one orbit? V(2)=3=n+1 ✓. Let me check n=4.

For n=4, S ranges from -2 to 2, so 5 values. Is V(4)=5? Let me verify by checking if S is a complete invariant (each value = one orbit).

Hmm, I need to verify completeness. Let me think about whether within a fixed S, all configs are connected.

Let me think about the y-representation again for n even. For n even, the alternating sum S in x-space... let me relate to y. Actually let me just try to prove S is complete for n even by showing any config can be reduced to a canonical form.

Alternatively, let me think about it via the y-representation and the index-parity invariant, and reconcile.

For n even: y has even number of 1's. The index-parity invariant (parity of 1's at even positions). Since total 1's is even, parity of even-1's = parity of odd-1's. So one bit invariant in y-space. Number of y-orbits = ? And then mapping to x-orbits...

This is getting complicated. Let me just try to compute V(n) for small n by reasoning and find the pattern, then verify.

Let me think about the problem more cleanly. I'll consider two cases.

Case n odd: The operation preserves parity of heads. complement has opposite parity, so x and complement are in different orbits. The y-map is 2-to-1 and the two preimages are in different orbits. So V(n) = 2 * (number of y-orbits).

Wait, but is that right? Each y corresponds to exactly 2 x-configs (x and complement), and they're in different orbits (different parity). And the operation on y corresponds to operations on x. So the x-orbits are in bijection with pairs (y-orbit, parity-bit)? Not exactly—each y-orbit O_y, the x-configs above it split into two x-orbits (by parity). But could two different y-orbits give x-orbits that... no, because x-orbits project to y-orbits (the map x->y is equivariant). So x-orbits refine y-orbits, and each y-orbit splits into exactly 2 x-orbits (since the 2 preimages per y are in different parity classes, and parity is preserved). Wait, need: within a y-orbit, does each y have both parities represented among its preimages? Yes: each y has preimages x and complement, which have opposite parity (n odd). And operations preserve parity. So the x-configs over a y-orbit split into two sets by parity, each set is a union of x-orbits. Are they each a single x-orbit? 

The x-configs over y-orbit O_y with, say, even parity: is this connected? The operation on x that keeps y within O_y... Actually any operation on x induces an operation on y within O_y. Conversely, given an operation on y (flip y_{i-1}, y_{i+1} at a 0-position i), does it lift to an operation on x? The operation on y corresponds to flipping x_i, x_{i+1} (when x_i=x_{i+1}, i.e., y_i=0). Given y and a choice of x (say x_1 fixed), the operation is determined. So yes, the x-orbits over a y-orbit, with fixed parity, form... let me think. Fix parity (say even). The even-parity preimages over O_y: for each y in O_y, exactly one of {x, complement} is even. So there's one even x per y. The operations connect them following the y-orbit connectivity. So the even x's over O_y form exactly one x-orbit (since y-orbit is connected and operations lift). Similarly odd. So each y-orbit gives exactly 2 x-orbits for n odd.

Therefore V(n) = 2 * (# y-orbits) for n odd.

Case n even: x and complement have same parity. The invariant S = sum (-1)^i x_i. complement changes S to -S (since complement flips all x_i, S -> sum (-1)^i(1-x_i) = sum(-1)^i - S = 0 - S = -S, since sum (-1)^i = 0 for n even). So complement negates S. x and complement in same orbit iff S = -S, i.e., S=0. 

Hmm, so for n even, the y-orbits and S... Let me think. For n even, each y gives 2 x-configs (x, complement) with S and -S. If S ≠ 0, they're in different orbits (different S). If S = 0, they might be in the same orbit.

Let me reconsider. For n even, is S a complete invariant? Let me check: does every operation preserve S? Yes (shown). Is every pair of configs with same S connected? 

Let me verify n=4 by brute force reasoning. Configs with S=0: e.g., HHTT (x=1,1,0,0): S = -1+1-0+0... wait let me set up indexing. Let me use positions 1,2,3,4 with weights -1,+1,-1,+1 (i.e., (-1)^i). S = -x1 + x2 - x3 + x4.

HHTT = (1,1,0,0): S = -1+1-0+0 = 0.
TTHH = (0,0,1,1): S = 0+0-1+1 = 0. (complement of HHTT, S=0).
HTHT = (1,0,1,0): S = -1+0-1+0 = -2.
THTH = (0,1,0,1): S = 0+1+0+1 = 2. (complement, S=2=-(-2) ✓).
HHHH = (1,1,1,1): S = -1+1-1+1 = 0.
TTTT = (0,0,0,0): S = 0. (complement, S=0).
HTTH = (1,0,0,1): S = -1+0-0+1 = 0.
THHT = (0,1,1,0): S = 0+1-1+0 = 0. (complement of HTTH? HTTH=(1,0,0,1), complement=(0,1,1,0)=THHT ✓, S=0).
HHHT=(1,1,1,0): S=-1+1-1+0=-1.
TTTH=(0,0,0,1): S=0+0-0+1=1. complement of HHHT, S=1=-(-1)✓.
HHTH=(1,1,0,1): S=-1+1-0+1=1.
TTHT=(0,0,1,0): S=0+0-1+0=-1. complement ✓.
HTHH=(1,0,1,1): S=-1+0-1+1=-1.
THTT=(0,1,0,0): S=0+1+0+0=1. complement ✓.
THHH=(0,1,1,1): S=0+1-1+1=1.
HTTT=(1,0,0,0): S=-1+0-0+0=-1. complement ✓.

So S values: -2 (HTHT), 2 (THTH), -1 (HHHT, HHTH... wait let me recount). 

S=-1: HHHT(1,1,1,0), HTHH(1,0,1,1), HTTT(1,0,0,0), TTHT(0,0,1,0). Let me verify: HHHT S=-1✓. HTHH S=-1✓. HTTT S=-1✓. TTHT S=-1✓. That's 4 configs.
S=1: TTTH, HHTH, THTT, THHH. 4 configs.
S=0: HHTT, TTHH, HHHH, TTTT, HTTH, THHT. 6 configs.
S=-2: HTHT. 1 config.
S=2: THTH. 1 config.
Total: 4+4+6+1+1 = 16 = 2^4 ✓.

If S is complete, V(4) = 5 (S ∈ {-2,-1,0,1,2}).

Let me verify S=0 configs are all connected (6 configs: HHTT, TTHH, HHHH, TTTT, HTTH, THHT).
HHHH: flip any adjacent pair (all same). Flip (1,2): (0,0,1,1)=TTHH. So HHHH -> TTHH. 
TTTT -> HHTT (flip 1,2). 
HHTT: (1,2)=HH->flip->TTTT. (2,3)=HT diff. (3,4)=TT->flip->(1,1,0,0)... wait flip 3,4: (1,1,1,1)=HHHH. (4,1)=TH... (4,1): x4=0,x1=1 diff. So HHTT -> TTTT, HHHH.
TTHH: (1,2)=TT->flip->HHHH. (3,4)=HH->flip->HHTT? flip 3,4: (0,0,0,0)=TTTT. Wait (0,0,1,1) flip 3,4 -> (0,0,0,0)=TTTT. (2,3)=TH diff. (4,1)=HT diff. So TTHH -> HHHH, TTTT.
So {HHHH, TTTT, HHTT, TTHH} connected.
HTTH=(1,0,0,1): (1,2)=HT diff. (2,3)=TT->flip->(1,1,1,1)=HHHH. (3,4)=TH diff. (4,1)=HH... x4=1,x1=1 same->flip->(0,0,0,0)? flip 4,1: (0,0,0,0)=TTTT. So HTTH -> HHHH, TTTT. Connected!
THHT=(0,1,1,0): (1,2)=TH diff. (2,3)=HH->flip->(0,0,0,0)=TTTT. (3,4)=HT diff. (4,1)=TT->flip->(1,1,1,1)=HHHH. Connected!
So all 6 S=0 configs connected. 

S=-1 configs: HHHT, HTHH, HTTT, TTHT. Let me check connectivity.
HHHT=(1,1,1,0): (1,2)=HH->flip->(0,0,1,0)=TTHT. (2,3)=HH->flip->(1,0,0,0)=HTTT. (3,4)=HT diff. (4,1)=TH diff. So HHHT -> TTHT, HTTT.
HTHH=(1,0,1,1): (1,2)=HT diff. (2,3)=TH diff. (3,4)=HH->flip->(1,0,0,0)=HTTT. (4,1)=HH->flip->(0,0,1,0)=TTHT. So HTHH -> HTTT, TTHT.
All 4 connected. ✓
S=1 similarly connected (by symmetry/complement). S=-2: only HTHT, one config. S=2: only THTH. So V(4)=5. ✓ S is complete for n=4.

So conjecture: for n even, V(n) = n+1 (S ranges over n+1 values, each one orbit). For n odd, V(n) = 2*(# y-orbits).

Now I need # y-orbits for n odd. Let me figure out the y-orbit structure.

In y-space: circular binary string length n, even number of 1's, operation: at 0-position, flip two neighbors. Invariant: index-parity (parity of 1's at even positions). For n odd, positions 1..n on circle. Even positions: 2,4,...,n-1 (that's (n-1)/2 positions). Odd positions: 1,3,...,n (that's (n+1)/2 positions).

Hmm wait, for n odd, the circle has odd length, so "even" and "odd" positions aren't symmetric. Let me reconsider the index-parity invariant.

The operation moves a 1 by ±2 positions, or annihilates/creates pairs of 1's at positions differing by 2 (same parity). So 1's at even positions stay at even positions (mod 2), 1's at odd positions stay at odd positions. The count of even-1's changes by ±2 or 0, so its parity is invariant. Same for odd-1's. Since total is even, both parities equal. So one invariant bit: parity of even-1's.

For n odd: even positions are {2,4,...,n-1}, odd positions {1,3,...,n}. A 1 at an even position can move among even positions (by ±2, but mod n which is odd, so ±2 generates all positions... wait, moving by 2 mod n where n is odd: 2 is invertible mod n, so ±2 generates everything. But we said 1's stay at even positions! Contradiction?

Wait, I need to be careful. Moving by 2 on a circle of odd length: starting at position 2 (even), +2 = 4 (even), ..., but mod n (odd), eventually we wrap: 2 + 2k mod n. Since gcd(2,n)=1, this hits all positions. So a 1 can reach any position! So the "even/odd position" distinction isn't preserved when n is odd, because wrapping around the circle changes parity.

Let me reconsider. The index-parity invariant: is it really invariant for n odd?

The operation "1 0 1 -> 0 0 0" removes 1's at positions i-1 and i+1. For n odd, i-1 and i+1 have the same parity (differ by 2). But when we count "even positions" on the circle, position i-1 and i+1 — if neither wraps, same parity. But the notion of even/odd position on an odd circle isn't well-defined globally (since going around changes parity). 

So the index-parity invariant only works for n even. For n odd, there's no such invariant because the circle has odd length and parity isn't consistent.

Let me reconsider. For n odd, what are the invariants in y-space?

Let me reconsider the operation in y-space: at position i with y_i=0, flip y_{i-1}, y_{i+1}. 

Let me think of y as a vector over GF(2). The operation adds the vector e_{i-1} + e_{i+1} (mod 2) to y, but only allowed when y_i = 0. Hmm, the constraint makes it not purely linear.

But actually, let me reconsider: maybe the constraint y_i=0 is automatically satisfiable in some sense, or maybe the reachable set is determined by linear invariants plus the constraint.

Let me think about it as: the operation toggles y_{i-1} and y_{i+1} simultaneously (adds e_{i-1}+e_{i+1}), provided y_i=0. 

Linear invariants: a linear functional f(y) = sum a_j y_j mod 2 is invariant if f(e_{i-1}+e_{i+1}) = a_{i-1}+a_{i+1} = 0 for all i (where the operation is allowed, but for linear invariant we need it for all i regardless of constraint). a_{i-1} + a_{i+1} = 0 for all i means a_{i+1} = a_{i-1}, so a is constant on positions of same parity. For n even: a even = c1, a odd = c2, and we need... a_{i-1}=a_{i+1} means consecutive same-parity positions equal, which is automatic. So a is determined by (a_even, a_odd) = (c1, c2). Two linear invariants? But also the total sum (a_j=1 all) is invariant: sum y_j = a_{i-1}+a_{i+1} = 1+1 = 0 mod 2 ✓. And the index-parity: a_j = 1 if j even, 0 if odd: a_{i-1}+a_{i+1}: i-1,i+1 same parity, so = 2*a or 0, = 0 mod 2 ✓. So for n even, two linear invariants: total sum (always even, so trivially 0) and index-parity. But total sum is always even (constraint), so the only nontrivial linear invariant is index-parity. That matches.

For n odd: a_{i-1} = a_{i+1} for all i. Since n is odd, stepping by 2 covers all positions, so all a_j equal. So a = (c,c,...,c). Only invariant: total sum (c=1), which is always even. So no nontrivial linear invariant for n odd. 

So for n odd, there are no linear invariants (beyond the always-even constraint). This suggests all y-strings with even number of 1's are in one orbit (for n odd), provided the operations are "connected enough." But we need to account for the constraint (y_i=0 required).

Hmm, but the constraint might split things. Let me check n=3: y-strings with even 1's: 000, 110, 101, 011. (4 strings). Are they all in one orbit?
000: all 0's. Operation at any i (y_i=0): flip neighbors. At i=1: flip y_0=y_3 and y_2. y=(0,0,0)-> flip y_3,y_2: (0,1,1)=011. At i=2: flip y_1,y_3: (1,0,1)=101. At i=3: flip y_2,y_1: (1,1,0)=110. So 000 -> {011, 101, 110}. All three! And from those, can we get back? 011=(0,1,1): y_i=0 only at i=1. Flip y_3,y_2: (0,0,0)... y_3=1->0, y_2=1->0: (0,0,0)=000. So 011->000. Similarly others. So all 4 y-strings in one orbit. # y-orbits = 1. V(3) = 2*1 = 2 ✓.

n=5: y-strings with even 1's: C(5,0)+C(5,2)+C(5,4) = 1+10+5 = 16. If all in one orbit, # y-orbits=1, V(5)=2. Let me check if that's plausible. Hmm, let me verify with a small check. Actually let me think about whether the constraint prevents full connectivity.

The all-zeros string 00000: from it, acting at any i gives a string with exactly two 1's at positions i-1, i+1. So from 00000 we reach all "two 1's at distance 2" strings: {1,3}, {2,4}, {3,5}, {4,1}, {5,2} = positions (mod 5): {1,3},{2,4},{3,5},{4,1},{5,2}. That's 5 strings. From these, can we reach all 16? 

From {1,3} (y=10100): y_i=0 at i=2,4,5. 
- Act at i=2: flip y_1,y_3: 1->0,1->0: 00000.
- Act at i=4: flip y_3,y_5: y_3=1->0, y_5=0->1: 10001 = {1,5}.
- Act at i=5: flip y_4,y_1: y_4=0->1, y_1=1->0: 00110 = {3,4}? wait y=(1,0,1,0,0), act at i=5: flip y_4, y_1: y_4=0->1, y_1=1->0: (0,0,1,1,0)={3,4}. 
So from {1,3} we reach 00000, {1,5}, {3,4}. {1,5}: distance along circle = 1 (positions 5 and 1 are adjacent). So we can get 1's at distance 1! Good. From {1,5}: y=(1,0,0,0,1). y_i=0 at i=2,3,4. Act at i=3: flip y_2,y_4: (1,1,0,1,1) = {1,2,4,5}, four 1's. So we reach 4-one strings. Seems like it's connecting well. I'll conjecture for n odd, all even-1 y-strings form one orbit, so # y-orbits = 1, V(n) = 2 for all odd n ≥ 3.

But wait, n=1: V(1)=2 (no operations). And n=1 is odd. # y-strings: y is length 1, even 1's means y=0 only. 1 y-string, 1 y-orbit. V(1) = 2*1 = 2 ✓ (if we accept the formula). Actually for n=1, x and complement (H and T) are different parity (n odd), different orbits, V=2. ✓.

So for n odd: V(n) = 2. For n even: V(n) = n+1.

Wait let me double check n=5 gives V=2 and n=7 gives V=2, etc. And n even: V(2)=3, V(4)=5, V(6)=7, etc.

Hold on, I should double-check the n even case more carefully—is S really complete for all even n? Let me think about n=6.

For n even, S = -x1+x2-x3+x4-x5+x6, ranges from -3 to 3, 7 values. Conjecture V(6)=7.

Let me try to prove S is complete for n even. I'll show any config can be reduced to a canonical config with the same S.

Canonical configs: for S = s (s ∈ {-n/2, ..., n/2}), the canonical config is: put heads in the "+ positions" (even indices, weight +1) first, then in "- positions" if needed. Specifically, if s ≥ 0: s heads all in + positions (e.g., first s of them), 0 heads in - positions. If s < 0: |s| heads in - positions, 0 in + positions. Wait, S = (heads in +) - (heads in -). To get S=s with minimal... actually any config with (heads in +) - (heads in -) = s. Canonical: if s≥0, heads in + = s, heads in - = 0. If s<0, heads in + = 0, heads in - = -s.

So canonical configs have all heads on one side. E.g., s=2, n=6: heads at positions 2,4 (the + positions), rest tails: (0,1,0,1,0,0). S = 0+1+0+1+0+0 = 2 ✓.

I need to show every config reduces to canonical. This requires showing operations can move heads around and cancel appropriately. This is essentially showing the y-orbit structure with the index-parity invariant is complete, and that S corresponds to index-parity.

Actually, let me connect S to the y-invariant. For n even, S = sum (-1)^i x_i. The y_j = x_j XOR x_{j+1}. Hmm, the relationship between S and index-parity of y... 

Let me think about it differently. For n even, I claimed the y-invariant is index-parity (parity of 1's at even positions). And there are 2 y-orbits (for each... no). Wait, how many y-orbits are there for n even?

For n even, y-strings with even number of 1's, invariant = index-parity (1 bit). So at least 2 y-orbits (index-parity 0 or 1). But could there be more (non-linear invariants)? For n=2: y-strings even 1's: 00, 11. 00 has index-parity 0, 11 has index-parity 1 (position 2 is even, has a 1). 2 y-orbits. V(2)=3. With n even, V(n) = 2*(#y-orbits) adjusted for complement... 

Hmm wait, for n even the relationship between x-orbits and y-orbits is different (complement has same parity, S -> -S). Let me recompute.

For n even: each y has 2 preimages x, complement(x), with S and -S. If S≠0: different orbits (2 x-orbits per y-orbit... but y-orbit contains many y's). If S=0: maybe same orbit.

This is getting complicated. Let me just directly argue S is complete for n even by proving connectivity within each S-value, and separately argue V(n)=2 for n odd by proving all even-y-strings are one orbit.

Let me focus on proving the key lemmas.

Lemma 1 (n odd): All y-strings with even number of 1's are in a single orbit.

Lemma 2 (n even): S = sum (-1)^i x_i is a complete invariant, so V(n) = n+1.

Let me prove Lemma 2 first. 

Proof of Lemma 2: S is invariant (shown). Need: any two configs with same S are connected. Equivalently, any config can be transformed to the canonical config with the same S.

Sub-lemma: We can "move" a head by 2 positions (in x-space) when there's an appropriate configuration. Actually, let me think in terms of operations on x.

Operation: flip adjacent equal pair. 

Key moves:
(a) If x_i = x_{i+1}, flip them: (v,v) -> (1-v, 1-v). This is the basic operation.

Let me think about what sequences allow. Consider three consecutive coins (a, b, c). 
- If a=b: flip to (1-a, 1-a, c) = (1-a, 1-a, c). 
- If b=c: flip to (a, 1-b, 1-b).

Hmm, let me think about moving a single head. Consider H T T (1,0,0): flip (2,3) (both T) -> (1,1,1) = H H H. Then flip (1,2) (both H) -> (0,0,1) = T T H. So H T T -> H H H -> T T H. Effect: (1,0,0) -> (0,0,1): the head moved from position 1 to position 3 (moved by 2). And the middle changed too. Actually (1,0,0)->(0,0,1): head moved from pos 1 to pos 3, pos 2 stayed 0. So a head at an odd position moved to another odd position (by 2), with a tail in between staying tail. 

More precisely: pattern T H T -> ... let me redo. (0,1,0) = T H T. Flip (1,2)? x1=0,x2=1 differ. Flip (2,3)? 1,0 differ. So no operation on THT. Hmm. But (1,0,0)=H T T: flip (2,3): (1,1,1). flip (1,2): (0,0,1). So HTT -> HHH -> TTH. Net: HTT -> TTH. Head moved from pos 1 to pos 3. 

Similarly TTH -> HHH -> HTT. So HTT <-> TTH. This swaps a head between positions 1 and 3 (distance 2), when position 2 is T. Wait, HTT has pos2=T, TTH has pos2=T. So the move is: H T T <-> T T H, head moves by 2, middle stays T.

What about H H T (1,1,0)? Flip (1,2): (0,0,0)... no wait (0,0,0)? (1,1,0) flip 1,2 -> (0,0,0)=TTT. Then TTT flip (2,3)->(0,1,1)=THH. So HHT -> TTT -> THH. HHT -> THH: (1,1,0)->(0,1,1). Head count 2->2. Positions of heads: {1,2} -> {2,3}. So a pair of adjacent heads shifted by 1. Hmm.

This is getting complicated. Let me think more cleverly.

Alternative approach: Let me prove Lemma 2 via the y-representation. For n even, y-orbits are classified by index-parity (1 bit). I need to show index-parity is complete (only 2 y-orbits for n even: one for each index-parity value). Then relate to S.

Actually, wait. For n=4, V(4)=5, but 2 y-orbits would give... let me compute. For n even, if there are 2 y-orbits, and the mapping to x... V(4)=5 is odd, so it's not simply 2*(something). Let me recount y-orbits for n=4.

n=4, y-strings with even 1's: 0000, 1100, 0110, 0011, 1001, 1010, 0101, 1111. (C(4,0)+C(4,2)+C(4,4)=1+6+1=8).
Index-parity (parity of 1's at even positions {2,4}):
- 0000: 0 (even)
- 1100: pos2=1, so 1 (odd)
- 0110: pos2=1,pos4=0: 1 (odd)
- 0011: pos2=0,pos4=1: 1 (odd)
- 1001: pos2=0,pos4=0: 0 (even)
- 1010: pos2=0,pos4=0: 0 (even)
- 0101: pos2=1,pos4=1: 0 (even)
- 1111: pos2=1,pos4=1: 0 (even)
So index-parity 0: {0000, 1001, 1010, 0101, 1111} (5 strings), index-parity 1: {1100, 0110, 0011} (3 strings).

If index-parity is complete, 2 y-orbits. Now map to x-orbits. V(4)=5. Hmm, 5 x-orbits from 2 y-orbits? Let me see.

For n=4 (even), each y has 2 x-preimages with S and -S. 
- y=0000: x=HHHH (S=0) or TTTT (S=0). Both S=0.
- y=1111: x=HTHT (S=-2) or THTH (S=2). S=±2.
- y=1010: x? y=(1,0,1,0) means x1≠x2, x2=x3, x3≠x4, x4=x1. So x1=1: x2=0,x3=0,x4=1: HTTH (S=-1+0-0+1=0). x1=0: THHT (S=0+1-1+0=0). Both S=0.
- y=0101: x1≠x2? y1=0: x1=x2. y2=1: x2≠x3. y3=0: x3=x4. y4=1: x4≠x1. x1=1: x2=1,x3=0,x4=0: HHTT (S=-1+1-0+0=0). x1=0: TTHH (S=0). Both S=0.
- y=1001: y1=1:x1≠x2. y2=0:x2=x3. y3=0:x3=x4. y4=1:x4≠x1. x1=1:x2=0,x3=0,x4=0: HTTT (S=-1). x1=0: THHH (S=1). S=±1.
- y=1100: y1=1,y2=1,y3=0,y4=0. x1≠x2,x2≠x3,x3=x4,x4=x1. x1=1:x2=0,x3=1,x4=1: HTHH (S=-1+0-1+1=-1). x1=0: THTT (S=0+1+0+0=1). S=±1.
- y=0110: y1=0,y2=1,y3=1,y4=0. x1=x2,x2≠x3,x3≠x4,x4=x1. x1=1:x2=1,x3=0,x4=1: HH TH=(1,1,0,1) S=-1+1-0+1=1. x1=0: TTHH? x2=0,x3=1,x4=0: (0,0,1,0) S=0+0-1+0=-1. S=±1.
- y=0011: y1=0,y2=0,y3=1,y4=1. x1=x2,x2=x3,x3≠x4,x4≠x1. x1=1:x2=1,x3=1,x4=0: HHHT S=-1+1-1+0=-1. x1=0: TTTH S=0+0-0+1=1. S=±1.

So:
- y-orbit (index-parity 0): {0000, 1010, 0101, 1001, 1111}. x-preimages: 
  - 0000 -> S=0 (HHHH, TTTT)
  - 1010 -> S=0 (HTTH, THHT)
  - 0101 -> S=0 (HHTT, TTHH)
  - 1001 -> S=±1 (HTTT S=-1, THHH S=1)
  - 1111 -> S=±2 (HTHT S=-2, THTH S=2)
- y-orbit (index-parity 1): {1100, 0110, 0011}. x-preimages:
  - 1100 -> S=±1 (HTHH S=-1, THTT S=1)
  - 0110 -> S=±1 (HHTH S=1, TTHT S=-1)
  - 0011 -> S=±1 (HHHT S=-1, TTTH S=1)

So within y-orbit 0, we have x-configs with S ∈ {0, ±1, ±2}. Within y-orbit 1, x-configs with S ∈ {±1} only. So the x-orbits are NOT simply determined by y-orbit. S is a finer invariant. And S=0 configs all come from y-orbit 0. S=±1 configs come from both y-orbits. S=±2 from y-orbit 0.

Since V(4)=5 (S=-2,-1,0,1,2 each one orbit), and S=±1 each one orbit despite coming from two y-orbits... So within a fixed S, configs from different y-orbits are still connected. That means the y-orbit structure is NOT the right way to think about it; S is the true invariant and it's complete, and the y-index-parity is a coarser invariant that doesn't fully separate x-orbits.

OK so let me just directly prove S is complete for n even, and V(n)=2 for n odd. Let me think about a clean proof.

Let me reconsider. I'll prove both cases by showing we can reduce any configuration to a canonical form.

Reformulation: Let me use 0/1 for coins. Operation: if x_i = x_{i+1}, set both to 1-x_i.

For n even, invariant S = sum_{i=1}^n (-1)^i x_i (using (-1)^i, so odd positions contribute -x_i, even positions +x_i). Equivalently S = (sum of x at even positions) - (sum of x at odd positions).

Claim: Two configs are equivalent iff they have the same S.

Proof of "if": Show any config can be reduced to canonical form C(S) = (all heads on even positions if S≥0, or all heads on odd positions if S<0), specifically: if S = s ≥ 0, place s heads at the first s even positions, rest tails. If s < 0, place |s| heads at first |s| odd positions, rest tails.

To show this, I'll prove we can perform the following moves:
1. Move a head from an even position to an adjacent even position (i.e., by 2 steps), keeping everything else fixed, when there's a tail in between.
2. Cancel a head at an even position with a head at an odd position (reducing both counts, preserving S? No—canceling one even head and one odd head changes S by -1 - (+1) ... wait S = even_heads - odd_heads. Removing one even head: S -> S-1. Removing one odd head: S -> S+1. Both: S unchanged. So canceling an even head and odd head preserves S. Good.)
3. Create a head at even and odd position (both new), preserving S.

Hmm, but actually the operation flips two equal adjacent coins. Let me think about what "cancel" means. If we have H at an even position and H at an adjacent odd position (i.e., two adjacent heads), flipping them gives T T: removes both heads. That's canceling an even head and odd head (adjacent). S unchanged. ✓. Conversely, two adjacent tails -> two adjacent heads: creates even+odd head. S unchanged.

And "moving a head by 2": H T T -> T T H (shown earlier): head at odd pos i, tail at i+1, tail at i+2 -> tail, tail, head at i+2. Wait that moves head from i to i+2, both odd (if i odd). But it requires the pattern H T T. Alternatively T T H -> H T T. So a head at an odd position can move by ±2 through a T T or H H... let me re-examine. H T T -> H H H -> T T H. The intermediate is all H. Hmm, this changes the config non-locally but net effect is head moves by 2.

Actually, the net effect H T T -> T T H: this is moving a head from position i to i+2, where positions i+1, i+2 were both T. After: position i is T, i+1 is T, i+2 is H. So the head moved right by 2, and the two T's stayed T. 

But wait, this requires i+1 and i+2 to both be T initially. What if they're not? Let me think about when we can move a head.

Actually, let me think about it as: the operation allows us to "propagate" a boundary. Let me think in terms of the y-representation after all, but more carefully, combining with S.

Hmm, let me step back and think about whether there's a cleaner way.

Let me reconsider the problem using the y = transitions representation, but now track everything including the "absolute" information.

Actually, here's a cleaner idea. Let me define the problem on a path vs circle and use known results.

Let me reconsider. I'll prove the two lemmas by explicit construction of moves.

Lemma A (Move): On a circle of n ≥ 3 coins, if there exist three consecutive coins with pattern H T T or T H H (i.e., a single coin followed by two of the opposite), we can move the single coin by 2 positions. Specifically, H T T -> T T H (move H right by 2) and dually T H H -> H H T.

Proof: H T T: flip the T T pair (positions 2,3) -> H H H. Then flip the H H pair (positions 1,2) -> T T H. Net: H T T -> T T H. ✓ (requires the two operations to be valid, which they are). Similarly T H H -> H H T.

Lemma B (Cancel/Create): Two adjacent equal coins can be flipped: H H -> T T or T T -> H H. This is the basic operation.

Now, using these, let me show connectivity.

Case n even, prove S is complete.

Given any config, I want to reduce it to canonical form. 

Step 1: Use cancel/create to make the number of "transitions" small, and use moves to consolidate heads.

Hmm, this is still vague. Let me think about it more carefully.

Let me think about the "blocks": maximal runs of equal coins. The operation flips an adjacent equal pair, which is within a block of length ≥ 2.

Actually, let me think about the y-representation and prove Lemma 1 (n odd: one y-orbit) and a corresponding result for n even, then handle the x-level.

Let me prove Lemma 1: For n odd (n ≥ 3), all y-strings with even number of 1's form one orbit.

In y-space, operation: at position i with y_i=0, flip y_{i-1}, y_{i+1}.

Sub-moves in y-space:
- "1 0 1 -> 0 0 0": annihilate two 1's separated by one 0 (at positions i-1, i+1, act at i).
- "0 0 0 -> 1 0 1": create two 1's.
- "1 0 0 -> 0 0 1" or "0 0 1 -> 1 0 0": move a 1 by 2 (act at the 0 adjacent to a 1 and another 0).

Wait let me recheck the move. y = (...,1,0,0,...) with the 1 at position j, 0 at j+1, 0 at j+2. Act at position j+1 (y_{j+1}=0): flip y_j and y_{j+2}: y_j 1->0, y_{j+2} 0->1. Result: (...,0,0,1,...). So 1 at j moves to 1 at j+2. ✓. This is "move 1 right by 2." Similarly move left by 2.

So in y-space, a 1 can move by ±2 (through 0's), and pairs "1 0 1" can annihilate, and "0 0 0" can create "1 0 1".

For n odd: moving by 2 generates all positions (since gcd(2,n)=1). So a 1 can move anywhere. Given any two 1's, we can move them to be separated by exactly one 0 (positions i, i+2), then annihilate. So any config with ≥2 ones can be reduced to fewer ones. Repeating, reduce to 0 ones (if even count) — but wait, we can only annihilate pairs, and we start with even number. So reduce to 0 ones = all zeros. But can we always arrange two 1's to be at distance 2 (separated by one 0)? 

Move a 1 to any position. Take two 1's, move one to position p and the other to position p+2 (mod n). Since we can move freely (n odd, ±2 generates all), yes. But we need the path to be clear (the 1 moves through 0's). If there are other 1's in the way, move them away first. Since we can move 1's around freely, we can always arrange. So: move all but two 1's to annihilate with each other, then annihilate the last two. Result: all zeros. 

Wait, but to annihilate two 1's at positions p, p+2, we need y_p=1, y_{p+1}=0, y_{p+2}=1, and act at p+1. The position p+1 must be 0. If we've moved the two 1's to p and p+2, and all others are gone (annihilated), then p+1 is 0. ✓. 

But actually, can we always reduce? Let me reconsider: we have 2k ones. Pair them up, move each pair to (p, p+2) and annihilate. But moving might be blocked by other 1's. However, since we can move 1's one at a time and the circle has room (n ≥ 2k+1 for the zeros to exist... well if 2k = n, all ones, but n odd means 2k ≠ n, so there's at least one 0). Actually if all positions are 1 (2k = n), but n is odd so 2k can't equal n. So there's always at least one 0. Good. And we can move 1's through 0's. With at least one 0, we can maneuver. 

Hmm, but moving a 1 by 2 requires the landing spot to be 0 and the middle to be 0. Let me re-examine: to move 1 from j to j+2, need y_{j+1}=0 and y_{j+2}=0 (act at j+1, flips y_j and y_{j+2}). After: y_j=0, y_{j+1}=0, y_{j+2}=1. So need both j+1 and j+2 to be 0. If there's a 1 at j+2, can't move there directly. But we can move other 1's away first. Since there's at least one 0 and n is odd, we have room to shuffle. I think this works but let me just accept it for the proof sketch; the key insight is that for n odd, the y-orbit is everything (one orbit).

Actually, let me also handle the creation direction: from all zeros, we can create "1 0 1" anywhere (act at any 0 in all-zeros, creates two 1's at distance 2). So from all-zeros we can reach any config with 2 ones (at distance 2, then move them around to any positions). And from 2 ones, create more, etc. So all-zeros reaches everything. Combined with everything reduces to all-zeros, it's one orbit. ✓.

So Lemma 1: for n odd, # y-orbits = 1, V(n) = 2*1 = 2.

Wait, I need to double-check the step "from all-zeros, reach any config with 2 ones at any positions." From all-zeros, act at position i: creates 1's at i-1, i+1 (distance 2). Then move them around by ±2. Since gcd(2,n)=1 (n odd), a 1 can reach any position. So two 1's can be placed at any two positions. ✓. And from 2 ones, act at a 0-position far from them to create 2 more, etc. So yes, one orbit. ✓.

Now Lemma 2: for n even, V(n) = n + 1.

For n even, I'll prove S is a complete invariant. S = sum_{i even} x_i - sum_{i odd} x_i, ranging over {-n/2, ..., n/2}, n+1 values.

S is invariant (proven). Need: any config with S = s can be reduced to canonical C(s).

Let me prove by showing we can:
(i) Move a head at an even position to any other even position (by 2 steps), and similarly odd to odd.
(ii) Cancel a head at even position and adjacent head at odd position (HH -> TT), reducing both even-head-count and odd-head-count by 1, S unchanged.
(iii) Create a head at even and adjacent odd position (TT -> HH), S unchanged.

Using (i), (ii), (iii): Given a config with S = s = E - O (E = even heads, O = odd heads). 
- If E > O (s > 0): cancel min(E,O) = O pairs of (even head, odd head) by bringing them adjacent and canceling. This leaves E - O = s even-heads and 0 odd-heads. Then move the s even-heads to the first s even positions. Result: canonical C(s). 
- If E < O (s < 0): cancel E pairs, leaving O - E = -s odd-heads, move to first |s| odd positions. Canonical C(s).
- If E = O (s = 0): cancel all pairs. Result: all tails (canonical C(0), since s=0 canonical is all tails). Wait, canonical C(0): s=0 ≥ 0, so s heads at even positions = 0 heads = all tails. ✓.

But wait, I need to make sure (i), (ii), (iii) are always executable.

(ii) Cancel: need an even head and odd head that are adjacent. Using (i), move an even head next to an odd head (adjacent positions are one even, one odd). Bring them adjacent, then flip (HH -> TT). ✓. But need them to both be H and adjacent; after moving, they are. ✓.

(i) Move even head by 2: need the move H T T -> T T H or similar. To move a head at even position j to j+2 (even), need positions j+1 (odd) and j+2 (even) to be T T. If they're not, we need to clear them. Hmm, this could be circular. Let me think.

Actually, the move H T T -> T T H requires the next two to be T T. What if position j+1 is H? Then we have H H at j, j+1 — we could cancel them (but that removes our head). Alternatively, think of it as: we can move a head through a region of tails. If the path is blocked by heads, we deal with those heads first (cancel or move them).

Let me think about this more carefully. Actually, since we can cancel any adjacent HH pair and create any adjacent TT->HH pair, and move heads through tails, the system is quite flexible. Let me argue as follows:

Claim: For n even, within a fixed S, all configs are connected.

Proof: I'll show any config reduces to canonical. 

First, note that the operation HH->TT (adjacent) and TT->HH (adjacent) are available. Also, the "move" H T T -> T T H (and symmetrically) is available.

Consider the config. While there exists an adjacent HH pair with one even and one odd (which is any adjacent HH pair since adjacent positions have opposite parity), and we want to reduce: flip it to TT. This reduces both E and O by 1, S unchanged. 

But this might not always lead to canonical because after removing all adjacent HH pairs, we might have isolated heads (no two adjacent). Then we need to move them together.

Hmm, let me think about isolated heads. If no two heads are adjacent, every head is surrounded by tails. Then H T T -> T T H moves a head by 2 (through tails). Since all non-head positions are tails (in the isolated case), we can move heads freely by 2. Even heads move among even positions, odd among odd. So we can bring an even head and odd head to adjacent positions, then cancel. Repeat until only same-parity heads remain, then consolidate to canonical positions.

But what if after some cancellations, heads become adjacent and we can continue? Let me structure the proof:

1. Repeatedly cancel adjacent HH pairs (HH->TT) until no adjacent heads remain. (Each cancellation preserves S.) Now all heads are isolated (separated by ≥1 tail).

2. Now move isolated heads by 2 (using H T T -> T T H, valid since neighbors are tails) to consolidate: bring an even head and an odd head adjacent, cancel them. Repeat until only one parity of heads remains.

3. If S > 0 (remaining even heads): move them to the first S even positions. If S < 0 (remaining odd heads): move to first |S| odd positions. If S = 0: no heads remain (all tails).

Wait, after step 2, if S > 0, we have S even heads and 0 odd heads, all isolated. Move them to canonical positions (first S even positions). Since they're isolated and move through tails, and there are enough even positions (S ≤ n/2), this works. Similarly for S < 0.

But hold on—in step 1, after canceling adjacent HH pairs, could we get stuck with a config that has adjacent heads re-forming? No: HH->TT removes heads, doesn't create new adjacent heads (it creates tails). Actually it could make previously non-adjacent heads become... no, removing heads only increases separation. So step 1 terminates with all heads isolated. ✓.

In step 2: we have isolated heads. Move an even head by 2 toward an odd head. Since all heads are isolated and separated by tails, the path between them (through tails) allows moving by 2. But moving by 2 keeps the head on even positions. To bring an even head adjacent to an odd head: an even head at position j, odd head at position k. Adjacent means |j-k|=1. Move even head to j' = k±1 (which is even, since k is odd, k±1 is even). Can we move it there? Move by 2's through tails. The even head travels through even positions, all of which must be tails (except start). If some even position in between has a head, move that head away first. Since we can move all even heads independently through tails (odd positions between them are tails in the isolated config), we can rearrange. 

Hmm, actually there's a subtlety: moving an even head from j to j+2 requires positions j+1 (odd) and j+2 (even) to be T T. Position j+1 is odd; in the isolated config, it's T unless there's an odd head there. If there's an odd head at j+1, then we have H (at j) T... no, H at j (even), odd head at j+1: they're adjacent! But we said all heads are isolated (no adjacent heads). Contradiction. So j+1 is T. And j+2 (even) is T unless there's an even head there. If there's an even head at j+2, then j, j+2 both heads with j+1 tail between: they're not adjacent (separated by j+1), so isolated config allows this. But then we can't move j to j+2 (j+2 is occupied). Move the head at j+2 first, or move j in the other direction. 

I think the point is: in the isolated config, even heads are at even positions with at least one even position between consecutive even heads (since they're separated by ≥1 position, and if two even heads are at j, j+2, they're separated by one odd position, which is fine for "isolated" since they're not adjacent). Hmm, actually "isolated" means no two heads adjacent, so even heads at j and j+2 are OK (not adjacent). But then moving is blocked.

Let me reconsider. Maybe I should allow creating space. We can also do TT -> HH (create adjacent pair), which might help. This is getting complicated for a rigorous proof. Let me think if there's a cleaner approach.

Alternative clean approach: Let me use the y-representation for n even and prove there are exactly 2 y-orbits (index-parity 0 and 1), then count x-orbits via S.

Hmm, but I showed for n=4 that S is finer than y-index-parity. So that doesn't directly work.

Let me reconsider. Actually, maybe I should prove S is complete by a different method: show that the operation group acts transitively on each S-level.

Let me think about the "generators" more carefully. The operation at (i,i+1) when x_i=x_{i+1}: this is an involution g_i that acts only when x_i = x_{i+1}.

Let me think about compositions that give useful permutations.

Key composition: g_{i+1} ∘ g_i when applicable. Consider x = (..., a, b, c, ...) with a=b (so g_i applies) and after g_i, check g_{i+1}.

g_i: (a, a, c) -> (1-a, 1-a, c). Now for g_{i+1}: need x_{i+1} = x_{i+2}, i.e., 1-a = c, i.e., c = 1-a. So if original (a, a, 1-a), then g_i g_{i+1}: (a,a,1-a) -> (1-a,1-a,1-a) -> (1-a, a, a). Net: (a,a,1-a) -> (1-a,a,a). This shifts the "odd one out." 

Hmm, (a, a, 1-a) -> (1-a, a, a): the position of the "different" coin moved from i+2 to i. So a single different coin moves left by 2. Dually it can move right by 2. This is the same move as before.

Let me think about the problem differently. Let me consider the quantity S and show that the orbit of any config with S=s contains the canonical config, by induction on some measure.

Measure: number of heads. 

If the config has an adjacent HH pair: cancel it (HH->TT), reducing heads by 2, S unchanged. By induction, the reduced config (fewer heads, same S) reaches canonical. So original reaches canonical. ✓. (Base case: no adjacent HH pairs, i.e., all heads isolated.)

If no adjacent HH pair (all heads isolated): 
- If there are both even and odd heads: take an even head and odd head. They're not adjacent (isolated). Move them together (by 2-steps through tails) to become adjacent, then cancel. This reduces heads by 2, S unchanged. By induction, reaches canonical.
- If only even heads (S > 0) or only odd heads (S < 0): move them to canonical positions. No cancellation needed; just rearrange. 
- If no heads (S=0): already canonical (all tails).

The induction is on number of heads, which decreases by 2 in each cancellation step. The rearrangement step (only same-parity heads) doesn't change head count but reaches canonical directly.

Now I need to rigorously justify "move them together through tails." In the isolated config, all non-head positions are tails. To move an even head from position j to j+2: need j+1, j+2 both tails. j+1 is odd: it's a tail (if it were a head, it'd be an odd head adjacent to even head at j, contradicting isolated). j+2 is even: it's a tail unless there's an even head there. If there's an even head at j+2, we have two even heads at j, j+2 (not adjacent, OK). To move past it, first move the j+2 head further right. But this could cascade. 

However, since the circle is finite and there are tails somewhere (if not all heads, and if all heads then n even all heads means S = n/2 - n/2... wait all heads: E = n/2, O = n/2, S = 0. But all heads has adjacent heads, so step 1 would cancel. So isolated config with only even heads has E = S ≤ n/2 heads at even positions, and n/2 even positions total, so at least n/2 - S ≥ 0 even positions are tails. If S < n/2, there's at least one even tail. 

To move even heads to the first S even positions: process from left to right. For position 2 (first even), if it should have a head (S ≥ 1) but doesn't, find the nearest even head to the right and move it left by 2 repeatedly until it reaches position 2. Moving left by 2: from j to j-2, need j-1, j-2 both tails. j-1 is odd: tail (isolated, and if odd head there it'd be adjacent to even head—wait, we might have odd heads too if we're in the "both parities" case). 

Hmm, I'm in the "only even heads" subcase, so all odd positions are tails. So j-1 (odd) is always tail. j-2 (even) is tail unless there's an even head there. If there's an even head at j-2, then position 2 might already be filled or we process in order. Let me process from left to right: ensure position 2 has a head (move nearest right head to position 2), then position 4, etc. When moving a head to position 2k, the positions 2,4,...,2k-2 already have heads (placed), and 2k+2,... might have heads. Move the nearest head at position 2m (m > k) leftward to 2k. Path: 2m -> 2m-2 -> ... -> 2k. Each step needs 2m-1 (odd, tail ✓) and 2m-2 (even). 2m-2: if m-1 > k, it might have a head (one of the remaining heads). Hmm. 

OK this is getting tedious but I believe it works. The key point: in the "only even heads, all odd positions tail" config, even heads can be moved freely among even positions (since odd positions are all tails, providing the "buffer"), as long as there's at least one even tail to allow passing. Actually, with all odd positions as tails, moving an even head from j to j+2 needs j+1 (tail ✓) and j+2 (even, need tail). If j+2 has a head, swap roles: think of it as moving the "gap" (even tail) instead. There's at least one even gap (since S < n/2 or S = n/2 means all even positions are heads = canonical already). Moving the gap by 2: T at even position, move it by 2: T H H -> H H T (dual of H T T -> T T H). T H H -> H H T: flip HH (positions j+1, j+2)... wait T at even position j, then j+1 (odd) = H? But odd positions are all tails in this subcase. Contradiction. So T H H can't occur (odd position is T, not H). 

Hmm, so in the "only even heads" config, odd positions are all T. So the config looks like: (T/H at even, T at odd). E.g., n=6: positions 1-6, even positions 2,4,6: (x1, x2, x3, x4, x5, x6) = (T, ?, T, ?, T, ?) where ? ∈ {H,T}. So config is T ? T ? T ?. Adjacent pairs: (1,2)=(T,?), (2,3)=(?,T), (3,4)=(T,?), etc. For an operation, need adjacent equal. (1,2)=(T,?): equal iff ?=T. So if x2=T, flip (1,2): both T->H: (H,H,T,?,T,?). Now x1=H (odd position head!). This breaks the "only even heads" property. Hmm. So the operation can create odd heads. That's fine—we're trying to reach canonical, and intermediate steps can have any config.

OK I think the proof is essentially correct but the details are messy. Let me just present the clean version: S is invariant, and by cancellation and moves, any config reduces to canonical. I'll state the moves clearly and argue they suffice.

Actually, let me reconsider and find a cleaner proof. 

Clean proof idea using y-representation for both cases:

For n even: Let me reconsider what S corresponds to in y-space. 

S = sum_{i even} x_i - sum_{i odd} x_i. 

Hmm, let me compute S in terms of y. We have x_{i+1} = x_i XOR y_i. So x_j = x_1 XOR y_1 XOR ... XOR y_{j-1}. This expresses all x in terms of x_1 and y. Then S = sum (-1)^j x_j = sum (-1)^j (x_1 XOR y_1 XOR ... XOR y_{j-1}). This is messy.

Let me try a different invariant connection. For n even, consider the "checkerboard" weighting. Actually, let me just go with the direct proof.

Let me reconsider: maybe the cleanest is to prove the move lemmas and argue connectivity, accepting some handwaving on the rearrangement, since this is a competition problem and the key insight (invariant + completeness) is what matters.

Let me also reconsider whether V(n) = 2 for all odd n and V(n) = n+1 for all even n is correct by checking n=5 or n=6 partially.

n=5, V(5)=2 (conjectured). Let me spot check: S not defined for n=5 (odd). Parity of heads is invariant. Configs: 32 total, 16 even parity, 16 odd. If V(5)=2, all even-parity configs are one class, all odd-parity another. Let me verify a piece: TTTTT (0 heads, even) and HHTTT (2 heads, even) should be connected. TTTTT: flip (1,2)->HHTTT. ✓ directly. Good. HHTTT and HTHTT (2 heads, even)? HHTTT=(1,1,0,0,0). HTHTT=(1,0,1,0,0). HHTTT: flip (1,2)->TTTTT. TTTTT: flip(3,4)->TTHTT? (0,0,1,1,0)? wait flip (3,4) of TTTTT: (0,0,1,1,0)=TTHHT. Hmm. Let me get HTHTT from TTTTT. TTTTT -> flip(1,2) -> HHTTT. HHTTT: flip(3,4)? (3,4)=(0,0) TT -> flip -> (1,1,1,1,0)? No: HHTTT=(1,1,0,0,0), flip (3,4): (1,1,1,1,0)=HHHHT. Then flip (2,3): (1,0,0,1,0)=HTTHT. Then flip (4,5): (4,5)=(1,0) differ. flip(3,4): (0,0,1,0)... (1,0,0,1,0) flip (3,4): (1,0,1,0,0)=HTHTT. ✓. So connected. Good, consistent with V(5)=2.

Let me also verify n=6 partially. V(6)=7 conjectured. S ranges -3..3. Let me check S=3: only HHTHTH? No. S=3 means E-O=3, max E=3 (all even heads), O=0. So config = all even positions H, all odd T: (T,H,T,H,T,H) = THTHTH. S = 0+1+0+1+0+1 = 3 ✓. Only one config with S=3. So one orbit. ✓. S=-3: HTHTHT, one config. S=2: E-O=2. E=3,O=1 or E=2,O=0. Multiple configs. Should be one orbit. I'll trust it.

So the answer: sum_{n=1}^{20} V(n).
- n odd: 1,3,5,7,9,11,13,15,17,19 (10 values), each V=2. Sum = 20.
- n even: 2,4,6,8,10,12,14,16,18,20 (10 values), V(n)=n+1. Sum = (3+5+7+9+11+13+15+17+19+21) = sum of (n+1) for n=2,4,...,20 = sum of 3,5,...,21 = 10 terms, average (3+21)/2=12, sum=120. Or: sum_{n even, 2 to 20} (n+1) = (2+4+...+20) + 10 = 110/2*... wait sum 2+4+...+20 = 2*(1+2+...+10)=2*55=110. Plus 10 = 120.
- Total = 20 + 120 = 140.

Let me double-check: sum of odd n from 1 to 19: V=2 each, 10 odd numbers, 10*2=20. Sum of even n from 2 to 20: V=n+1, sum = (3+5+7+9+11+13+15+17+19+21). Let me add: 3+5=8, +7=15, +9=24, +11=35, +13=48, +15=63, +17=80, +19=99, +21=120. Yes 120. Total 140.

Now let me write up the proof cleanly.

Let me reconsider the proof of completeness for n even once more to make it rigorous enough.

I'll prove: For n even, two configurations are equivalent iff they have the same S.

"Invariant" direction: S is preserved by operations (proven).

"Complete" direction: Show every config reduces to canonical C(s).

I'll use these moves:
- Cancel: adjacent HH -> TT (basic operation).
- Create: adjacent TT -> HH (basic operation).
- Hop: H T T -> T T H and T H H -> H H T (two-step sequences), moving a head by 2 positions through two equal coins.

Proof of Hop: H T T: the pair (positions 2,3) is TT, flip -> H H H; then pair (1,2) is HH, flip -> T T H. Net H T T -> T T H. ✓. Similarly T H H -> H H T.

Now the reduction:
1. If there's an adjacent HH pair, cancel it (reduces head count by 2, S unchanged). Repeat until no adjacent HH. (Terminates since heads decrease.)
2. Now all heads are isolated (no two adjacent). 
   - If there are both an even-positioned head and an odd-positioned head: I want to bring them adjacent and cancel. 
   - Claim: using Hops, we can move an isolated head by 2 positions to any position of the same parity, as long as the path's odd/even intermediate positions are clear. 

Hmm, the issue is when the path is blocked. Let me think about whether in the isolated config, we can always bring an even head and odd head adjacent.

In the isolated config, heads are separated by ≥1 tail. Consider an even head at position p and an odd head at position q. WLOG p < q (in cyclic order). The arc from p to q contains some positions. Since heads are isolated, between p and q there might be other heads, each isolated. 

Alternative: Let me use Create to help. We can create adjacent HH from TT. So even if heads are isolated, we can create new adjacent pairs to facilitate movement, then cancel. 

Actually, here's a cleaner approach: I'll show that from any config, we can reach a config with an adjacent HH pair (unless it's already canonical with ≤1 head or all-same-parity isolated). 

Hmm, let me think about it yet differently. Let me just prove that the canonical form is reachable by showing the moves generate a transitive action on each S-level, using the fact that we can simulate "moving a head by 1" via create+cancel.

Move a head by 1 position: H T -> ? We want to move H from position i to i+1. Consider H T T T (head at i, tails at i+1,i+2,i+3). Create at (i+1,i+2): TT->HH: H H H T. Cancel at (i,i+1): HH->TT: T T H T. Net: H T T T -> T T H T. Head moved from i to i+2 (by 2). That's the Hop again, not by 1.

To move by 1: H T -> T H? Consider H T H (heads at i, i+2, tail at i+1). This is isolated. Hmm. H T H: no adjacent equal (HT, TH, and cyclically H...H at distance 2). For n=3 circle H T H: pairs (1,2)=HT, (2,3)=TH, (3,1)=HH. Oh (3,1) is HH (cyclic)! So cancel: H T H -> T T T (flip 3,1). So HTH -> TTT. That reduces heads. Not a move.

I think moving by 1 isn't directly possible, but moving by 2 is, and for n even, even positions and odd positions are separate, so moving by 2 within a parity class is enough to reach any position of that parity. The issue is only blocking.

Let me just argue the blocking can be resolved: In the isolated config with both even and odd heads, pick the even head and odd head that are closest (cyclically). Between them, all positions are tails (since they're the closest pair of opposite parity, and any head between would be same-parity to one of them... hmm, not necessarily). 

Ugh, let me think about this more carefully with a cleaner invariant argument.

Actually, you know what, let me just use the y-representation result and connect it properly. Let me prove:

For n even: there are exactly 2 y-orbits (index-parity 0 and 1). Then I'll count x-orbits.

Wait, but I showed n=4 has S finer than index-parity. So 2 y-orbits but 5 x-orbits. The relationship is not straightforward. Let me recompute.

For n=4: y-orbit 0 (index-parity 0) contains y-strings {0000, 1001, 1010, 0101, 1111}. The x-configs over this y-orbit have S ∈ {0, ±1, ±2}. y-orbit 1 (index-parity 1) contains {1100, 0110, 0011}, x-configs have S ∈ {±1}. 

The x-orbits: S=0 (from y-orbit 0 only), S=±1 (from both y-orbits), S=±2 (from y-orbit 0 only). And each S-value is one x-orbit. So S=1 configs come from both y-orbits but are all connected. That means within the x-level, operations connect across y-orbits? But the y-map is equivariant, so x-operations project to y-operations, keeping y within its y-orbit. So an x-orbit projects to a single y-orbit. Contradiction with S=1 coming from two y-orbits!

Wait, that means S=1 is NOT one x-orbit. Let me recheck V(4).

Let me recheck: are the S=1 configs all connected? S=1 configs: TTTH, HHTH, THTT, THHH (from my earlier list). Let me check their y-values:
- TTTH=(0,0,0,1): y1=0,y2=0,y3=1,y4=1: y=0011 (index-parity 1).
- HHTH=(1,1,0,1): y1=0,y2=1,y3=1,y4=0: y=0110 (index-parity 1).
- THTT=(0,1,0,0): y1=1,y2=1,y3=0,y4=0: y=1100 (index-parity 1).
- THHH=(0,1,1,1): y1=1,y2=0,y3=0,y4=1: y=1001 (index-parity 0).

So S=1 configs: three from y-orbit 1 (TTTH, HHTH, THTT) and one from y-orbit 0 (THHH). If x-orbits project to y-orbits, then THHH (y-orbit 0) is NOT in the same x-orbit as the other three (y-orbit 1). So S=1 splits into at least 2 x-orbits!

Let me recheck V(4) by direct computation. I earlier claimed all S=0 connected and all S=-1 connected, but I didn't check S=1 carefully. Let me recheck.

S=1 configs: TTTH=(0,0,0,1), HHTH=(1,1,0,1), THTT=(0,1,0,0), THHH=(0,1,1,1).

Check connectivity:
TTTH=(0,0,0,1): pairs (1,2)=TT->flip->(1,1,0,1)=HHTH. (2,3)=TT->flip->(0,1,1,1)=THHH. (3,4)=TH diff. (4,1)=HT... (4,1): x4=1,x1=0 differ. So TTTH -> HHTH, THHH.
So TTTH connects to HHTH and THHH! But TTTH is y-orbit 1 and THHH is y-orbit 0. So they ARE in the same x-orbit, meaning x-operations can change the y-orbit?! 

But the y-map is equivariant... let me recheck. TTTH=(0,0,0,1), y=0011. Operation flip (1,2): (1,1,0,1)=HHTH, y = 0,1,1,0 = 0110. So y changed from 0011 to 0110. Both index-parity 1. OK same y-orbit. Operation flip (2,3): (0,1,1,1)=THHH, y=1,0,0,1=1001. y changed from 0011 (index-parity 1) to 1001 (index-parity 0)! 

So the y-orbit changed! That means index-parity is NOT invariant under the operation for n=4?! Let me recheck.

y=0011: index-parity = parity of 1's at even positions {2,4}: y2=0, y4=1, so 1 (odd). 
Operation: flip (2,3) in x: x=(0,0,0,1)->(0,1,1,1). y: y1=x1^x2=0^1=1, y2=x2^x3=1^1=0, y3=x3^x4=1^1=0, y4=x4^x1=1^0=1. y=1001. index-parity: y2=0,y4=1: 1 (odd). 

Wait, I need to recompute. y4 = x4 XOR x1. For THHH=(0,1,1,1): x4=1, x1=0, y4=1. y2 = x2 XOR x3 = 1 XOR 1 = 0. So index-parity = y2 + y4 = 0 + 1 = 1 (odd). Same as before! I made an error earlier. Let me recompute the index-parity for 1001.

y=1001: positions 1,2,3,4 = 1,0,0,1. Even positions {2,4}: y2=0, y4=1. Count of 1's at even positions = 1 (odd). So index-parity = 1 (odd). 

Earlier I listed 1001 as index-parity 0. That was wrong! Let me recompute all.

y=0000: even 1's count = 0, parity 0.
y=1100: y2=1,y4=0: count 1, parity 1.
y=0110: y2=1,y4=0: count 1, parity 1.
y=0011: y2=0,y4=1: count 1, parity 1.
y=1001: y2=0,y4=1: count 1, parity 1.
y=1010: y2=0,y4=0: count 0, parity 0.
y=0101: y2=1,y4=1: count 2, parity 0.
y=1111: y2=1,y4=1: count 2, parity 0.

So index-parity 0: {0000, 1010, 0101, 1111} (4 strings). Index-parity 1: {1100, 0110, 0011, 1001} (4 strings). I had misclassified 1001 earlier. Good, so 1001 is index-parity 1, same as 0011. So the operation 0011 -> 1001 stays in index-parity 1. ✓. No contradiction.

So let me redo the x-orbit analysis for n=4.
y-orbit 0 (index-parity 0): {0000, 1010, 0101, 1111}.
- 0000: x=HHHH(S=0)/TTTT(S=0).
- 1010: x=HTTH(S=0)/THHT(S=0).
- 0101: x=HHTT(S=0)/TTHH(S=0).
- 1111: x=HTHT(S=-2)/THTH(S=2).
y-orbit 1 (index-parity 1): {1100, 0110, 0011, 1001}.
- 1100: x=HTHH(S=-1)/THTT(S=1).
- 0110: x=HHTH(S=1)/TTHT(S=-1).
- 0011: x=HHHT(S=-1)/TTTH(S=1).
- 1001: x=HTTT(S=-1)/THHH(S=1).

So y-orbit 0 has x-configs with S ∈ {0, ±2}. y-orbit 1 has x-configs with S ∈ {±1}. 

So S=0 and S=±2 come from y-orbit 0; S=±1 from y-orbit 1. So S is determined by y-orbit (for n=4): y-orbit 0 ↔ S even (0, ±2), y-orbit 1 ↔ S odd (±1). And within each y-orbit, the x-configs split by S. 

y-orbit 0: S ∈ {0, 2, -2}. S=0: {HHHH, TTTT, HTTH, THHT, HHTT, TTHH} (6 configs). S=2: {THTH}. S=-2: {HTHT}. Are the S=0 configs all connected? Yes (verified earlier). So y-orbit 0 gives 3 x-orbits (S=0, S=2, S=-2).
y-orbit 1: S ∈ {1, -1}. S=1: {THTT, HHTH, TTTH, THHH} (4 configs). S=-1: {HTHH, TTHT, HHHT, HTTT} (4 configs). Are S=1 configs all connected? TTTH -> HHTH, THHH (shown). HHTH=(1,1,0,1): (1,2)=HH->flip->(0,0,0,1)=TTTH. (2,3)=HT diff. (3,4)=TH diff. (4,1)=HH->flip->(0,1,1,0)=THHT? wait (4,1): x4=1,x1=1 same->flip both: x4->0,x1->0:        — AI历史解题过程（thinking）
#   polymath_01307         — 题目ID

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
  <problem_id>polymath_01307</problem_id>
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

Along a circle, there are $n$ coins, each lying heads or tails up. If two adjacent coins lie the same way (both heads or both tails), it is allowed to flip both. Let $V(n)$ be the number of equivalence classes of coin arrangements, where two arrangements are in the same class if one can be obtained from the other by applying any number of such operations. Calculate the sum $\sum_{n=1}^{20} V(n)$.

## Standard Solution

The original solution states that for odd $n$, there are $V(n) = 2$ variants (equivalence classes). For even $n$, there are $V(n) = n+1$ variants.
We need to compute the sum $S = \sum_{n=1}^{20} V(n)$.
The odd terms are $n=1, 3, 5, 7, 9, 11, 13, 15, 17, 19$. There are 10 such terms, and for each, $V(n) = 2$. Sum of odd terms = $10 \times 2 = 20$.
The even terms are $n=2, 4, 6, 8, 10, 12, 14, 16, 18, 20$. For each, $V(n) = n+1$.
The even values are $3, 5, 7, 9, 11, 13, 15, 17, 19, 21$.
Sum of even terms = $3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 = \frac{10}{2}(3 + 21) = 5 \times 24 = 120$.
Total sum = $20 + 120 = 140$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have n coins on a circle, each heads or tails. Operation: if two adjacent coins are the same (both H or both T), flip both. V(n) = number of equivalence classes under this operation. Compute sum from n=1 to 20.

Let me think about invariants. Represent coins as bits x_1,...,x_n in {0,1} on a circle. Operation: if x_i = x_{i+1}, flip both (i.e., x_i -> 1-x_i, x_{i+1} -> 1-x_{i+1}).

Let me think in terms of "differences". Define d_i = x_i XOR x_{i+1} (whether adjacent coins differ). The operation flips x_i and x_{i+1} when they're equal, i.e., when d_{i-1}... wait let me index carefully.

Actually let me think about what the operation does to the difference pattern. Let y_i = x_i XOR x_{i+1} for i=1..n (cyclic, so y_n = x_n XOR x_1).

The operation at position (i, i+1): requires x_i = x_{i+1}, i.e., y_i = 0. It flips both x_i and x_{i+1}.

After flipping x_i and x_{i+1}:
- y_{i-1} = x_{i-1} XOR x_i changes (since x_i flipped) -> y_{i-1} flips
- y_i = x_i XOR x_{i+1}: both flipped, so y_i unchanged (still 0)
- y_{i+1} = x_{i+1} XOR x_{i+2}: x_{i+1} flipped -> y_{i+1} flips

So the operation: pick i with y_i = 0, then flip y_{i-1} and y_{i+1}.

Interesting. So in the "difference" representation, we have a binary string y_1...y_n on a circle, with the constraint that sum of y_i is even (since it's a cycle, the number of transitions must be even). The operation: choose a position i where y_i=0, and flip y_{i-1} and y_{i+1}.

Note: the all-y configuration corresponds to x being alternating... but on a circle, alternating is only possible if n is even. The constraint is that the number of 1's in y is even.

Also, two x configurations map to the same y? No—given y and one value of x (say x_1), the rest is determined. But x_1 can be 0 or 1, giving complementary configurations. Complementary x (all bits flipped) gives the same y. So configurations x come in complementary pairs mapping to the same y, except... actually each y corresponds to exactly 2 x-configurations (x and its complement), as long as n≥1. For n=1, x_1 alone, complement is the other, y is empty/trivial.

Hmm, let me reconsider. The operation preserves y_i at the chosen position (stays 0) and flips the two neighbors. So the operation acts on y-strings.

But wait—the operation also changes x. Two x's with the same y are complements. Does the operation ever connect x to its complement? Let's see: the operation flips exactly 2 coins, so it changes the parity of number of heads. Complement changes all n coins. If n is even, complement preserves parity of heads; if n odd, complement flips parity. The operation flips 2 coins so preserves parity of heads. So:
- If n even: x and complement have same parity, could be connected.
- If n odd: x and complement have different parity, cannot be connected (since operation preserves parity).

Hmm, this is getting complex. Let me think more carefully about the structure.

Actually, let me reconsider. The equivalence classes of x under the operation. Let me think about what's invariant.

The operation flips two adjacent equal coins. Let me think about the parity of the number of heads, mod 2. Flipping two coins: if both were H (heads=1), they become T, so heads count -2. If both T, they become H, heads count +2. So parity of heads is preserved. That's one invariant.

Now let me think about the y = difference representation more. The operation on y: pick i with y_i=0, flip y_{i-1}, y_{i+1}.

Let me think of this as a game on the circle. We have a binary circular string with even number of 1s. Operation: at a 0-position, flip its two neighbors.

Let me think about what's invariant here. Consider the positions of 1's. The 1's come in pairs (since even count) — actually they partition into "arcs". Let me think of the 1's as "markers" and 0's as "gaps".

Hmm, let me think differently. Let me consider the gaps between consecutive 1's. The 1's divide the circle into arcs of 0's. If there are 2k ones, there are 2k arcs of zeros (some possibly empty). The operation at a 0-position i flips its neighbors y_{i-1}, y_{i+1}.

Case analysis: position i is a 0. Its neighbors y_{i-1} and y_{i+1} can be 0 or 1.
- If y_{i-1}=1, y_{i+1}=1: both flip to 0. So two 1's disappear, replaced by... the 0 at position i stays 0, and positions i-1, i+1 become 0. So a pattern "1 0 1" becomes "0 0 0". This merges arcs.
- If y_{i-1}=0, y_{i+1}=0: both flip to 1. Pattern "0 0 0" -> "1 0 1". Creates two new 1's.
- If y_{i-1}=1, y_{i+1}=0: becomes "0 0 1". A 1 moves.
- If y_{i-1}=0, y_{i+1}=1: becomes "1 0 0". A 1 moves.

So 1's can move around, be created/destroyed in pairs. The number of 1's changes by -2, 0, or +2. So parity of number of 1's is preserved (always even, which is automatic).

Hmm, what's invariant? Let me think about the "gaps" between consecutive 1's measured along the circle. Let the 1's be at positions p_1 < p_2 < ... < p_{2k}. The gaps are g_j = p_{j+1} - p_j (cyclic). Sum of gaps = n.

Operation "1 0 1" -> "0 0 0": removes two adjacent 1's (with exactly one 0 between them). This removes two consecutive 1's and merges three arcs into one.

Operation "0 0 0" -> "1 0 1": splits an arc of ≥3 zeros... wait, it needs three consecutive 0's: y_{i-1}=0, y_i=0, y_{i+1}=0, and we act at position i. This creates two 1's at i-1 and i+1.

Operation moving a 1: "1 0 0" -> "0 0 1" or "0 0 1" -> "1 0 0": a 1 moves by 2 positions.

So a 1 can move by 2 steps along the circle. And pairs of 1's separated by exactly one 0 can annihilate; and we can create pairs of 1's with one 0 between them from three 0's.

This is reminiscent of a chip-firing or a representation in terms of... Let me think about parity of positions.

Key insight: a 1 at position p can move to p+2 or p-2. So the parity (mod 2) of a 1's position is invariant for each 1! When two 1's annihilate (1 0 1 -> 0 0 0), the two 1's are at positions i-1 and i+1, which have the same parity. When two 1's are created (0 0 0 -> 1 0 1), they're at i-1 and i+1, same parity.

So the 1's come in two "colors": even-positioned and odd-positioned. The number of even-1's and odd-1's... when a 1 moves by 2, it stays same color. When two same-color 1's annihilate, that color count decreases by 2. When two same-color 1's created, color count +2. So parity of each color count is invariant!

Let me define: E = number of 1's at even positions, O = number of 1's at odd positions. Both E and O have their parities preserved. Since E+O is even (always), E and O have the same parity. So really there's one invariant: parity of E (equivalently parity of O).

Wait, but we also need to track: can we always reduce to a canonical form? Let me think about what configurations are reachable.

Claim: the invariant is (parity of E, parity of O) but since E+O even, these are equal, so just one bit: parity of E. Plus maybe something else?

Hmm wait, but also we should check: is the operation reversible? Yes, each operation is its own inverse (flipping twice returns). So it's a group action, equivalence classes = orbits.

Let me reconsider. Actually I realize the y-representation loses information about x vs complement. Let me back up.

x configurations: 2^n total. The map x -> y (differences) is 2-to-1 (x and complement give same y) for n ≥ 2. For n=1, y is empty, both x map to same y.

The operation on x induces the operation on y as described. But two x's with same y (complements) — are they in the same orbit or not?

Let me think about it differently. Let me just directly analyze orbits of x.

Actually, let me reconsider the whole approach. Let me think about small n by hand and find the pattern, then prove.

n=1: One coin. No adjacent pair (or is the coin adjacent to itself? On a circle of 1, the coin is adjacent to itself). If x_1 = x_1 (always true), flip both... but it's the same coin, flipping it twice = no change? Or is it a single coin adjacent to itself, so "flip both" means flip it... once? This is ambiguous. 

Convention: for n=1, the single coin is adjacent to itself. "Two adjacent coins" — if it's the same coin, flipping both means flipping it once (or twice = no change). Let me think about what's standard. Actually for n=1, typically the operation does nothing meaningful. Let me consider: if we flip "both" and they're the same coin, flipping twice = identity. So V(1) = 2 (two classes: H and T, no operation possible that changes anything). Actually if the coin is adjacent to itself and they're "the same way" (trivially), flipping both = flipping the single coin once? That would make H <-> T, giving V(1)=1.

This is ambiguous. Let me consider n=1 gives V(1)=2 (no valid operation since you need two distinct adjacent coins) — more standard. Hmm, but actually many problems consider n≥2. Let me just compute and see; the sum from 1 to 20, and n=1 contributes either 1 or 2.

Let me reconsider: the problem says "two adjacent coins". For n=1 there's only one coin, so no two adjacent coins exist. So no operation possible, V(1) = 2.

For n=2: two coins, adjacent to each other (and each adjacent to the other on both sides, but it's the same pair). Configurations: HH, HT, TH, TT. Operation: if two adjacent same, flip both. HH -> TT, TT -> HH. HT: coins differ, no operation. TH: differ, no operation. So classes: {HH, TT}, {HT}, {TH}. V(2) = 3.

Let me verify with y-representation. n=2: y_1 = x_1 XOR x_2, y_2 = x_2 XOR x_1 = y_1. So y = (0,0) or (1,1). 
- y=(0,0): x = HH or TT. These are complements. Operation on y: need y_i=0, flip neighbors. y=(0,0): act at i=1, y_1=0, flip y_0=y_2 and y_2. y_2=0->1, y_2=1... wait both neighbors are y_2 (since n=2, neighbors of position 1 are position 0=2 and position 2). So flip y_2 twice? = no change. Hmm, that's a degeneracy. So y=(0,0) stays. And x=HH <-> TT via operation. So one class. Good, {HH,TT}.
- y=(1,1): x = HT or TH. No operation possible (y_i=1 for both, can't act). So HT and TH are separate classes (they're complements, both parity... HT has 1 head, TH has 1 head, same parity, but no operation connects them). So 2 classes. Total V(2)=3. ✓.

OK so the y-representation: two x's with same y may or may not be in the same orbit. For y=(0,0), the two x's (HH, TT) are in same orbit. For y=(1,1), the two x's (HT, TH) are in different orbits.

So I can't just count y-orbits. Let me think again.

Let me think about the parity of heads more carefully. The operation preserves parity of number of heads. For n=2: HH (2 heads, even), TT (0, even) -> same class. HT (1, odd), TH (1, odd) -> different classes but same parity. So parity alone doesn't determine.

Hmm. So there's more structure. Let me think about n=3.

n=3: configurations 8 total. Parity of heads: even (0 or 2 heads) or odd (1 or 3 heads).
- Even: TTT, HHT, HTH, THH (0 or 2 heads)
- Odd: HHH, HTT, THT, TTH (3 or 1 head)

Operations (circle of 3, each adjacent pair): flip adjacent equal pair.
TTT: any pair is TT. Flip pair (1,2): TTT -> HHT. Flip (2,3): TTH. Flip (3,1): HTT. So TTT connects to HHT, TTH, HTT. But HTT is odd parity! Wait, TTT has 0 heads (even), flipping two T's to H's gives 2 heads (even). TTT -> HHT (flip 1,2), TTH (flip 2,3), HTT (flip 3,1). All have 2 heads, even. Good.

HHT: coins 1,2 = HH, flip -> TTT. Coins 2,3 = HT differ. Coins 3,1 = TH differ. So HHT <-> TTT.
Similarly TTH <-> TTT, HTT <-> TTT.
So {TTT, HHT, TTH, HTT} all connected. That's 4 configs, all even parity. So all even-parity configs form one class.

Odd parity: HHH, HTT, THT, TTH... wait TTH is even. Let me redo. Odd = 1 or 3 heads.
- HHH (3 heads): flip any pair (all HH) -> HHH with two flipped to T: e.g., flip (1,2): THH. THH has 2 heads, even! Wait that crosses parity. 

Hold on: HHH, flip coins 1,2 (both H) -> T,H,H = THH, 2 heads, even. But operation should preserve parity! 3 heads -> 2 heads is parity change. Contradiction!

Wait, flipping two heads to tails: heads go from 3 to 1. 1 is odd. THH = T,H,H = 2 heads. Wait no: THH means coin1=T, coin2=H, coin3=H. That's 2 heads. 3 -> 2? Flipping two H's to T: 3 - 2 = 1 head. But THH has 2 heads. 

I think I mislabeled. HHH flip coins 1 and 2: coin1 H->T, coin2 H->T, coin3 stays H. Result: T,T,H = TTH. TTH has 1 head, odd. OK I made an error. TTH = 1 head. Let me recount: T,T,H -> 1 head, odd. Good, parity preserved.

Let me redo n=3 carefully. Label coins 1,2,3. Config = (x1,x2,x3).
Even parity (0 or 2 heads): TTT, HHT, HTH, THH.
Odd parity (1 or 3 heads): HHH, TTH, THT, HTT.

TTT: flip (1,2)-> HHT; flip (2,3)-> THT? T,T,T flip 2,3 -> T,H,H = THH. flip (3,1)-> H,T,T = HTT. So TTT -> HHT, THH, HTT. These are even? HHT=2✓, THH=2✓, HTT=1? H,T,T = 1 head, odd! 

Wait, TTT flip coins 3 and 1: coin3 T->H, coin1 T->H, coin2 stays T. Result H,T,H = HTH, 2 heads. I keep making errors. Let me be very careful.

TTT = (T,T,T). 
- Flip (1,2): (H,H,T) = HHT, 2 heads even ✓
- Flip (2,3): (T,H,H) = THH, 2 heads even ✓
- Flip (3,1): (H,T,H) = HTH, 2 heads even ✓

So TTT -> {HHT, THH, HTH}. All even. Good.

HHT = (H,H,T). Pairs: (1,2)=HH same -> flip -> (T,T,T)=TTT. (2,3)=HT diff. (3,1)=TH diff. So HHT -> TTT only.
THH = (T,H,H). (1,2)=TH diff. (2,3)=HH -> flip -> (T,T,T)=TTT. (3,1)=HT diff. So THH -> TTT.
HTH = (H,T,H). (1,2)=HT diff. (2,3)=TH diff. (3,1)=HH -> flip -> (T,T,T)... wait flip coins 3,1: coin3 H->T, coin1 H->T, coin2 stays T. (T,T,T)=TTT. So HTH -> TTT.

So all even configs {TTT, HHT, THH, HTH} form one class. ✓

Odd configs: HHH, TTH, THT, HTT.
HHH=(H,H,H). Flip (1,2)->(T,T,H)=TTH. (2,3)->(H,T,T)=HTT. (3,1)->(T,H,T)=THT. So HHH -> {TTH, HTT, THT}.
TTH=(T,T,H). (1,2)=TT->flip->(H,H,H)=HHH. (2,3)=TH diff. (3,1)=HT diff. -> HHH.
THT=(T,H,T). (1,2)=TH diff. (2,3)=HT diff. (3,1)=TT->flip->(H,H,H)? flip coins 3,1: T->H, T->H, coin2 stays H. (H,H,H)=HHH. -> HHH.
HTT=(H,T,T). (1,2)=HT diff. (2,3)=TT->flip->(H,H,H)? flip 2,3: T->H,T->H, coin1 stays H. (H,H,H). (3,1)=TH diff. -> HHH.

So all odd configs {HHH, TTH, THT, HTT} form one class.

V(3) = 2.

So far: V(1)=2, V(2)=3, V(3)=2.

n=4: Let me use the y-representation and think about orbits, being careful about x vs complement.

Actually, let me think about the structure more generally. Let me reconsider using the y (difference) representation and track the invariant.

In y-space: circular binary string of length n, even number of 1's. Operation: at a 0, flip its two neighbors. The invariant I found: parity of (number of 1's at even positions). Let me call this the "index parity" invariant.

But wait, for n=2, y can be (0,0) or (1,1). 
- (0,0): 0 ones, E=0 (even). 
- (1,1): ones at positions 1,2. E = number at even positions = 1 (position 2). O = 1 (position 1). E odd. 
So these have different index parity, can't be connected. Good, 2 y-classes.

But V(2)=3, not 2. Because y=(1,1) corresponds to two x-configs (HT, TH) that are in different orbits. So the y-orbit count undercounts.

So I need to understand: for a given y-orbit, how many x-orbits does it correspond to?

Given y, the x-configs mapping to it are x and complement(x). Are x and complement in the same orbit?

The operation preserves parity of heads. complement changes heads count from h to n-h. Parity changes iff n is odd.

- If n odd: parity of h and n-h differ, so x and complement have different parity, can't be in same orbit. So each y-orbit gives 2 x-orbits (when y is reachable / has configs).
- If n even: parity of h and n-h same, so x and complement could be in same orbit. Need to determine.

For n=2 (even): y=(0,0): x=HH,TT, same orbit (1 x-orbit). y=(1,1): x=HT,TH, different orbits (2 x-orbits). So for n even it depends on y.

Hmm. So the relationship is subtle. Let me think about n even more carefully.

For n even, when are x and complement in the same orbit? 

Let me think about another invariant. Consider the "alternating sum" or some other quantity.

Let me think about the operation's effect on x directly. Operation: flip x_i, x_{i+1} when x_i = x_{i+1}.

Consider the quantity S = sum of x_i * (-1)^i or similar. Actually, let me think about it as: assign weights w_i to positions, and look at sum w_i x_i mod something. The operation flips x_i and x_{i+1} (when equal). The change in sum w_i x_i is w_i(1-2x_i) + w_{i+1}(1-2x_{i+1}). Since x_i = x_{i+1} = v, change = (w_i + w_{i+1})(1-2v). For this to be invariant mod 2 (i.e., mod 2 always 0), need w_i + w_{i+1} even, i.e., w_i ≡ w_{i+1} mod 2. So all w_i same parity. That just gives parity of total heads (w_i=1 all). Not helpful for more.

For invariance over integers (not just mod 2): change = ±(w_i+w_{i+1}), sign depends on v. Not invariant unless w_i + w_{i+1} = 0, i.e., w_{i+1} = -w_i, alternating weights. But on a circle, alternating requires n even. So for n even, w_i = (-1)^i, and the operation changes sum by (w_i + w_{i+1})(1-2v) = ((-1)^i + (-1)^{i+1})(...) = 0. So S = sum (-1)^i x_i is invariant for n even!

Let me verify n=2: S = (-1)^1 x_1 + (-1)^2 x_2 = -x_1 + x_2 (mod something). HH: -1+1=0. TT: 0+0=0. HT: -1+0=-1. TH: 0+1=1. So S distinguishes HT (S=-1) from TH (S=1), and HH=TT (S=0). That gives 3 classes! V(2)=3 ✓.

So for n even, S = sum_{i} (-1)^i x_i is an integer invariant. Range: from -n/2 to n/2 (if we use x_i in {0,1}, S ranges over integers with same parity as... ). Actually x_i ∈{0,1}, w_i = ±1. S = sum of ±x_i. With n/2 weights +1 and n/2 weights -1. S ranges from -n/2 to n/2, all integers (since we can choose each x_i). Actually S can be any integer from -n/2 to n/2? The +1 positions contribute 0 or 1 each, -1 positions contribute 0 or -1 each. So S = (number of heads in + positions) - (number of heads in - positions). Range: [0 - n/2, n/2 - 0] = [-n/2, n/2], all integers. So n+1 possible values.

But is S the only invariant for n even (combined with parity)? Wait, S already determines parity: S = (heads in +) - (heads in -), total heads = (heads in +) + (heads in -). Parity of total heads = parity of (heads in +) + (heads in -). And S = (heads in +) - (heads in -). So parity of total = parity of S + 2*(heads in -) = parity of S. So parity of heads = parity of S. So S encodes parity. Good, S is the invariant for n even, and it takes n+1 values. But are all values achievable and do they each give exactly one orbit? V(2)=3=n+1 ✓. Let me check n=4.

For n=4, S ranges from -2 to 2, so 5 values. Is V(4)=5? Let me verify by checking if S is a complete invariant (each value = one orbit).

Hmm, I need to verify completeness. Let me think about whether within a fixed S, all configs are connected.

Let me think about the y-representation again for n even. For n even, the alternating sum S in x-space... let me relate to y. Actually let me just try to prove S is complete for n even by showing any config can be reduced to a canonical form.

Alternatively, let me think about it via the y-representation and the index-parity invariant, and reconcile.

For n even: y has even number of 1's. The index-parity invariant (parity of 1's at even positions). Since total 1's is even, parity of even-1's = parity of odd-1's. So one bit invariant in y-space. Number of y-orbits = ? And then mapping to x-orbits...

This is getting complicated. Let me just try to compute V(n) for small n by reasoning and find the pattern, then verify.

Let me think about the problem more cleanly. I'll consider two cases.

Case n odd: The operation preserves parity of heads. complement has opposite parity, so x and complement are in different orbits. The y-map is 2-to-1 and the two preimages are in different orbits. So V(n) = 2 * (number of y-orbits).

Wait, but is that right? Each y corresponds to exactly 2 x-configs (x and complement), and they're in different orbits (different parity). And the operation on y corresponds to operations on x. So the x-orbits are in bijection with pairs (y-orbit, parity-bit)? Not exactly—each y-orbit O_y, the x-configs above it split into two x-orbits (by parity). But could two different y-orbits give x-orbits that... no, because x-orbits project to y-orbits (the map x->y is equivariant). So x-orbits refine y-orbits, and each y-orbit splits into exactly 2 x-orbits (since the 2 preimages per y are in different parity classes, and parity is preserved). Wait, need: within a y-orbit, does each y have both parities represented among its preimages? Yes: each y has preimages x and complement, which have opposite parity (n odd). And operations preserve parity. So the x-configs over a y-orbit split into two sets by parity, each set is a union of x-orbits. Are they each a single x-orbit? 

The x-configs over y-orbit O_y with, say, even parity: is this connected? The operation on x that keeps y within O_y... Actually any operation on x induces an operation on y within O_y. Conversely, given an operation on y (flip y_{i-1}, y_{i+1} at a 0-position i), does it lift to an operation on x? The operation on y corresponds to flipping x_i, x_{i+1} (when x_i=x_{i+1}, i.e., y_i=0). Given y and a choice of x (say x_1 fixed), the operation is determined. So yes, the x-orbits over a y-orbit, with fixed parity, form... let me think. Fix parity (say even). The even-parity preimages over O_y: for each y in O_y, exactly one of {x, complement} is even. So there's one even x per y. The operations connect them following the y-orbit connectivity. So the even x's over O_y form exactly one x-orbit (since y-orbit is connected and operations lift). Similarly odd. So each y-orbit gives exactly 2 x-orbits for n odd.

Therefore V(n) = 2 * (# y-orbits) for n odd.

Case n even: x and complement have same parity. The invariant S = sum (-1)^i x_i. complement changes S to -S (since complement flips all x_i, S -> sum (-1)^i(1-x_i) = sum(-1)^i - S = 0 - S = -S, since sum (-1)^i = 0 for n even). So complement negates S. x and complement in same orbit iff S = -S, i.e., S=0. 

Hmm, so for n even, the y-orbits and S... Let me think. For n even, each y gives 2 x-configs (x, complement) with S and -S. If S ≠ 0, they're in different orbits (different S). If S = 0, they might be in the same orbit.

Let me reconsider. For n even, is S a complete invariant? Let me check: does every operation preserve S? Yes (shown). Is every pair of configs with same S connected? 

Let me verify n=4 by brute force reasoning. Configs with S=0: e.g., HHTT (x=1,1,0,0): S = -1+1-0+0... wait let me set up indexing. Let me use positions 1,2,3,4 with weights -1,+1,-1,+1 (i.e., (-1)^i). S = -x1 + x2 - x3 + x4.

HHTT = (1,1,0,0): S = -1+1-0+0 = 0.
TTHH = (0,0,1,1): S = 0+0-1+1 = 0. (complement of HHTT, S=0).
HTHT = (1,0,1,0): S = -1+0-1+0 = -2.
THTH = (0,1,0,1): S = 0+1+0+1 = 2. (complement, S=2=-(-2) ✓).
HHHH = (1,1,1,1): S = -1+1-1+1 = 0.
TTTT = (0,0,0,0): S = 0. (complement, S=0).
HTTH = (1,0,0,1): S = -1+0-0+1 = 0.
THHT = (0,1,1,0): S = 0+1-1+0 = 0. (complement of HTTH? HTTH=(1,0,0,1), complement=(0,1,1,0)=THHT ✓, S=0).
HHHT=(1,1,1,0): S=-1+1-1+0=-1.
TTTH=(0,0,0,1): S=0+0-0+1=1. complement of HHHT, S=1=-(-1)✓.
HHTH=(1,1,0,1): S=-1+1-0+1=1.
TTHT=(0,0,1,0): S=0+0-1+0=-1. complement ✓.
HTHH=(1,0,1,1): S=-1+0-1+1=-1.
THTT=(0,1,0,0): S=0+1+0+0=1. complement ✓.
THHH=(0,1,1,1): S=0+1-1+1=1.
HTTT=(1,0,0,0): S=-1+0-0+0=-1. complement ✓.

So S values: -2 (HTHT), 2 (THTH), -1 (HHHT, HHTH... wait let me recount). 

S=-1: HHHT(1,1,1,0), HTHH(1,0,1,1), HTTT(1,0,0,0), TTHT(0,0,1,0). Let me verify: HHHT S=-1✓. HTHH S=-1✓. HTTT S=-1✓. TTHT S=-1✓. That's 4 configs.
S=1: TTTH, HHTH, THTT, THHH. 4 configs.
S=0: HHTT, TTHH, HHHH, TTTT, HTTH, THHT. 6 configs.
S=-2: HTHT. 1 config.
S=2: THTH. 1 config.
Total: 4+4+6+1+1 = 16 = 2^4 ✓.

If S is complete, V(4) = 5 (S ∈ {-2,-1,0,1,2}).

Let me verify S=0 configs are all connected (6 configs: HHTT, TTHH, HHHH, TTTT, HTTH, THHT).
HHHH: flip any adjacent pair (all same). Flip (1,2): (0,0,1,1)=TTHH. So HHHH -> TTHH. 
TTTT -> HHTT (flip 1,2). 
HHTT: (1,2)=HH->flip->TTTT. (2,3)=HT diff. (3,4)=TT->flip->(1,1,0,0)... wait flip 3,4: (1,1,1,1)=HHHH. (4,1)=TH... (4,1): x4=0,x1=1 diff. So HHTT -> TTTT, HHHH.
TTHH: (1,2)=TT->flip->HHHH. (3,4)=HH->flip->HHTT? flip 3,4: (0,0,0,0)=TTTT. Wait (0,0,1,1) flip 3,4 -> (0,0,0,0)=TTTT. (2,3)=TH diff. (4,1)=HT diff. So TTHH -> HHHH, TTTT.
So {HHHH, TTTT, HHTT, TTHH} connected.
HTTH=(1,0,0,1): (1,2)=HT diff. (2,3)=TT->flip->(1,1,1,1)=HHHH. (3,4)=TH diff. (4,1)=HH... x4=1,x1=1 same->flip->(0,0,0,0)? flip 4,1: (0,0,0,0)=TTTT. So HTTH -> HHHH, TTTT. Connected!
THHT=(0,1,1,0): (1,2)=TH diff. (2,3)=HH->flip->(0,0,0,0)=TTTT. (3,4)=HT diff. (4,1)=TT->flip->(1,1,1,1)=HHHH. Connected!
So all 6 S=0 configs connected. 

S=-1 configs: HHHT, HTHH, HTTT, TTHT. Let me check connectivity.
HHHT=(1,1,1,0): (1,2)=HH->flip->(0,0,1,0)=TTHT. (2,3)=HH->flip->(1,0,0,0)=HTTT. (3,4)=HT diff. (4,1)=TH diff. So HHHT -> TTHT, HTTT.
HTHH=(1,0,1,1): (1,2)=HT diff. (2,3)=TH diff. (3,4)=HH->flip->(1,0,0,0)=HTTT. (4,1)=HH->flip->(0,0,1,0)=TTHT. So HTHH -> HTTT, TTHT.
All 4 connected. ✓
S=1 similarly connected (by symmetry/complement). S=-2: only HTHT, one config. S=2: only THTH. So V(4)=5. ✓ S is complete for n=4.

So conjecture: for n even, V(n) = n+1 (S ranges over n+1 values, each one orbit). For n odd, V(n) = 2*(# y-orbits).

Now I need # y-orbits for n odd. Let me figure out the y-orbit structure.

In y-space: circular binary string length n, even number of 1's, operation: at 0-position, flip two neighbors. Invariant: index-parity (parity of 1's at even positions). For n odd, positions 1..n on circle. Even positions: 2,4,...,n-1 (that's (n-1)/2 positions). Odd positions: 1,3,...,n (that's (n+1)/2 positions).

Hmm wait, for n odd, the circle has odd length, so "even" and "odd" positions aren't symmetric. Let me reconsider the index-parity invariant.

The operation moves a 1 by ±2 positions, or annihilates/creates pairs of 1's at positions differing by 2 (same parity). So 1's at even positions stay at even positions (mod 2), 1's at odd positions stay at odd positions. The count of even-1's changes by ±2 or 0, so its parity is invariant. Same for odd-1's. Since total is even, both parities equal. So one invariant bit: parity of even-1's.

For n odd: even positions are {2,4,...,n-1}, odd positions {1,3,...,n}. A 1 at an even position can move among even positions (by ±2, but mod n which is odd, so ±2 generates all positions... wait, moving by 2 mod n where n is odd: 2 is invertible mod n, so ±2 generates everything. But we said 1's stay at even positions! Contradiction?

Wait, I need to be careful. Moving by 2 on a circle of odd length: starting at position 2 (even), +2 = 4 (even), ..., but mod n (odd), eventually we wrap: 2 + 2k mod n. Since gcd(2,n)=1, this hits all positions. So a 1 can reach any position! So the "even/odd position" distinction isn't preserved when n is odd, because wrapping around the circle changes parity.

Let me reconsider. The index-parity invariant: is it really invariant for n odd?

The operation "1 0 1 -> 0 0 0" removes 1's at positions i-1 and i+1. For n odd, i-1 and i+1 have the same parity (differ by 2). But when we count "even positions" on the circle, position i-1 and i+1 — if neither wraps, same parity. But the notion of even/odd position on an odd circle isn't well-defined globally (since going around changes parity). 

So the index-parity invariant only works for n even. For n odd, there's no such invariant because the circle has odd length and parity isn't consistent.

Let me reconsider. For n odd, what are the invariants in y-space?

Let me reconsider the operation in y-space: at position i with y_i=0, flip y_{i-1}, y_{i+1}. 

Let me think of y as a vector over GF(2). The operation adds the vector e_{i-1} + e_{i+1} (mod 2) to y, but only allowed when y_i = 0. Hmm, the constraint makes it not purely linear.

But actually, let me reconsider: maybe the constraint y_i=0 is automatically satisfiable in some sense, or maybe the reachable set is determined by linear invariants plus the constraint.

Let me think about it as: the operation toggles y_{i-1} and y_{i+1} simultaneously (adds e_{i-1}+e_{i+1}), provided y_i=0. 

Linear invariants: a linear functional f(y) = sum a_j y_j mod 2 is invariant if f(e_{i-1}+e_{i+1}) = a_{i-1}+a_{i+1} = 0 for all i (where the operation is allowed, but for linear invariant we need it for all i regardless of constraint). a_{i-1} + a_{i+1} = 0 for all i means a_{i+1} = a_{i-1}, so a is constant on positions of same parity. For n even: a even = c1, a odd = c2, and we need... a_{i-1}=a_{i+1} means consecutive same-parity positions equal, which is automatic. So a is determined by (a_even, a_odd) = (c1, c2). Two linear invariants? But also the total sum (a_j=1 all) is invariant: sum y_j = a_{i-1}+a_{i+1} = 1+1 = 0 mod 2 ✓. And the index-parity: a_j = 1 if j even, 0 if odd: a_{i-1}+a_{i+1}: i-1,i+1 same parity, so = 2*a or 0, = 0 mod 2 ✓. So for n even, two linear invariants: total sum (always even, so trivially 0) and index-parity. But total sum is always even (constraint), so the only nontrivial linear invariant is index-parity. That matches.

For n odd: a_{i-1} = a_{i+1} for all i. Since n is odd, stepping by 2 covers all positions, so all a_j equal. So a = (c,c,...,c). Only invariant: total sum (c=1), which is always even. So no nontrivial linear invariant for n odd. 

So for n odd, there are no linear invariants (beyond the always-even constraint). This suggests all y-strings with even number of 1's are in one orbit (for n odd), provided the operations are "connected enough." But we need to account for the constraint (y_i=0 required).

Hmm, but the constraint might split things. Let me check n=3: y-strings with even 1's: 000, 110, 101, 011. (4 strings). Are they all in one orbit?
000: all 0's. Operation at any i (y_i=0): flip neighbors. At i=1: flip y_0=y_3 and y_2. y=(0,0,0)-> flip y_3,y_2: (0,1,1)=011. At i=2: flip y_1,y_3: (1,0,1)=101. At i=3: flip y_2,y_1: (1,1,0)=110. So 000 -> {011, 101, 110}. All three! And from those, can we get back? 011=(0,1,1): y_i=0 only at i=1. Flip y_3,y_2: (0,0,0)... y_3=1->0, y_2=1->0: (0,0,0)=000. So 011->000. Similarly others. So all 4 y-strings in one orbit. # y-orbits = 1. V(3) = 2*1 = 2 ✓.

n=5: y-strings with even 1's: C(5,0)+C(5,2)+C(5,4) = 1+10+5 = 16. If all in one orbit, # y-orbits=1, V(5)=2. Let me check if that's plausible. Hmm, let me verify with a small check. Actually let me think about whether the constraint prevents full connectivity.

The all-zeros string 00000: from it, acting at any i gives a string with exactly two 1's at positions i-1, i+1. So from 00000 we reach all "two 1's at distance 2" strings: {1,3}, {2,4}, {3,5}, {4,1}, {5,2} = positions (mod 5): {1,3},{2,4},{3,5},{4,1},{5,2}. That's 5 strings. From these, can we reach all 16? 

From {1,3} (y=10100): y_i=0 at i=2,4,5. 
- Act at i=2: flip y_1,y_3: 1->0,1->0: 00000.
- Act at i=4: flip y_3,y_5: y_3=1->0, y_5=0->1: 10001 = {1,5}.
- Act at i=5: flip y_4,y_1: y_4=0->1, y_1=1->0: 00110 = {3,4}? wait y=(1,0,1,0,0), act at i=5: flip y_4, y_1: y_4=0->1, y_1=1->0: (0,0,1,1,0)={3,4}. 
So from {1,3} we reach 00000, {1,5}, {3,4}. {1,5}: distance along circle = 1 (positions 5 and 1 are adjacent). So we can get 1's at distance 1! Good. From {1,5}: y=(1,0,0,0,1). y_i=0 at i=2,3,4. Act at i=3: flip y_2,y_4: (1,1,0,1,1) = {1,2,4,5}, four 1's. So we reach 4-one strings. Seems like it's connecting well. I'll conjecture for n odd, all even-1 y-strings form one orbit, so # y-orbits = 1, V(n) = 2 for all odd n ≥ 3.

But wait, n=1: V(1)=2 (no operations). And n=1 is odd. # y-strings: y is length 1, even 1's means y=0 only. 1 y-string, 1 y-orbit. V(1) = 2*1 = 2 ✓ (if we accept the formula). Actually for n=1, x and complement (H and T) are different parity (n odd), different orbits, V=2. ✓.

So for n odd: V(n) = 2. For n even: V(n) = n+1.

Wait let me double check n=5 gives V=2 and n=7 gives V=2, etc. And n even: V(2)=3, V(4)=5, V(6)=7, etc.

Hold on, I should double-check the n even case more carefully—is S really complete for all even n? Let me think about n=6.

For n even, S = -x1+x2-x3+x4-x5+x6, ranges from -3 to 3, 7 values. Conjecture V(6)=7.

Let me try to prove S is complete for n even. I'll show any config can be reduced to a canonical config with the same S.

Canonical configs: for S = s (s ∈ {-n/2, ..., n/2}), the canonical config is: put heads in the "+ positions" (even indices, weight +1) first, then in "- positions" if needed. Specifically, if s ≥ 0: s heads all in + positions (e.g., first s of them), 0 heads in - positions. If s < 0: |s| heads in - positions, 0 in + positions. Wait, S = (heads in +) - (heads in -). To get S=s with minimal... actually any config with (heads in +) - (heads in -) = s. Canonical: if s≥0, heads in + = s, heads in - = 0. If s<0, heads in + = 0, heads in - = -s.

So canonical configs have all heads on one side. E.g., s=2, n=6: heads at positions 2,4 (the + positions), rest tails: (0,1,0,1,0,0). S = 0+1+0+1+0+0 = 2 ✓.

I need to show every config reduces to canonical. This requires showing operations can move heads around and cancel appropriately. This is essentially showing the y-orbit structure with the index-parity invariant is complete, and that S corresponds to index-parity.

Actually, let me connect S to the y-invariant. For n even, S = sum (-1)^i x_i. The y_j = x_j XOR x_{j+1}. Hmm, the relationship between S and index-parity of y... 

Let me think about it differently. For n even, I claimed the y-invariant is index-parity (parity of 1's at even positions). And there are 2 y-orbits (for each... no). Wait, how many y-orbits are there for n even?

For n even, y-strings with even number of 1's, invariant = index-parity (1 bit). So at least 2 y-orbits (index-parity 0 or 1). But could there be more (non-linear invariants)? For n=2: y-strings even 1's: 00, 11. 00 has index-parity 0, 11 has index-parity 1 (position 2 is even, has a 1). 2 y-orbits. V(2)=3. With n even, V(n) = 2*(#y-orbits) adjusted for complement... 

Hmm wait, for n even the relationship between x-orbits and y-orbits is different (complement has same parity, S -> -S). Let me recompute.

For n even: each y has 2 preimages x, complement(x), with S and -S. If S≠0: different orbits (2 x-orbits per y-orbit... but y-orbit contains many y's). If S=0: maybe same orbit.

This is getting complicated. Let me just directly argue S is complete for n even by proving connectivity within each S-value, and separately argue V(n)=2 for n odd by proving all even-y-strings are one orbit.

Let me focus on proving the key lemmas.

Lemma 1 (n odd): All y-strings with even number of 1's are in a single orbit.

Lemma 2 (n even): S = sum (-1)^i x_i is a complete invariant, so V(n) = n+1.

Let me prove Lemma 2 first. 

Proof of Lemma 2: S is invariant (shown). Need: any two configs with same S are connected. Equivalently, any config can be transformed to the canonical config with the same S.

Sub-lemma: We can "move" a head by 2 positions (in x-space) when there's an appropriate configuration. Actually, let me think in terms of operations on x.

Operation: flip adjacent equal pair. 

Key moves:
(a) If x_i = x_{i+1}, flip them: (v,v) -> (1-v, 1-v). This is the basic operation.

Let me think about what sequences allow. Consider three consecutive coins (a, b, c). 
- If a=b: flip to (1-a, 1-a, c) = (1-a, 1-a, c). 
- If b=c: flip to (a, 1-b, 1-b).

Hmm, let me think about moving a single head. Consider H T T (1,0,0): flip (2,3) (both T) -> (1,1,1) = H H H. Then flip (1,2) (both H) -> (0,0,1) = T T H. So H T T -> H H H -> T T H. Effect: (1,0,0) -> (0,0,1): the head moved from position 1 to position 3 (moved by 2). And the middle changed too. Actually (1,0,0)->(0,0,1): head moved from pos 1 to pos 3, pos 2 stayed 0. So a head at an odd position moved to another odd position (by 2), with a tail in between staying tail. 

More precisely: pattern T H T -> ... let me redo. (0,1,0) = T H T. Flip (1,2)? x1=0,x2=1 differ. Flip (2,3)? 1,0 differ. So no operation on THT. Hmm. But (1,0,0)=H T T: flip (2,3): (1,1,1). flip (1,2): (0,0,1). So HTT -> HHH -> TTH. Net: HTT -> TTH. Head moved from pos 1 to pos 3. 

Similarly TTH -> HHH -> HTT. So HTT <-> TTH. This swaps a head between positions 1 and 3 (distance 2), when position 2 is T. Wait, HTT has pos2=T, TTH has pos2=T. So the move is: H T T <-> T T H, head moves by 2, middle stays T.

What about H H T (1,1,0)? Flip (1,2): (0,0,0)... no wait (0,0,0)? (1,1,0) flip 1,2 -> (0,0,0)=TTT. Then TTT flip (2,3)->(0,1,1)=THH. So HHT -> TTT -> THH. HHT -> THH: (1,1,0)->(0,1,1). Head count 2->2. Positions of heads: {1,2} -> {2,3}. So a pair of adjacent heads shifted by 1. Hmm.

This is getting complicated. Let me think more cleverly.

Alternative approach: Let me prove Lemma 2 via the y-representation. For n even, y-orbits are classified by index-parity (1 bit). I need to show index-parity is complete (only 2 y-orbits for n even: one for each index-parity value). Then relate to S.

Actually, wait. For n=4, V(4)=5, but 2 y-orbits would give... let me compute. For n even, if there are 2 y-orbits, and the mapping to x... V(4)=5 is odd, so it's not simply 2*(something). Let me recount y-orbits for n=4.

n=4, y-strings with even 1's: 0000, 1100, 0110, 0011, 1001, 1010, 0101, 1111. (C(4,0)+C(4,2)+C(4,4)=1+6+1=8).
Index-parity (parity of 1's at even positions {2,4}):
- 0000: 0 (even)
- 1100: pos2=1, so 1 (odd)
- 0110: pos2=1,pos4=0: 1 (odd)
- 0011: pos2=0,pos4=1: 1 (odd)
- 1001: pos2=0,pos4=0: 0 (even)
- 1010: pos2=0,pos4=0: 0 (even)
- 0101: pos2=1,pos4=1: 0 (even)
- 1111: pos2=1,pos4=1: 0 (even)
So index-parity 0: {0000, 1001, 1010, 0101, 1111} (5 strings), index-parity 1: {1100, 0110, 0011} (3 strings).

If index-parity is complete, 2 y-orbits. Now map to x-orbits. V(4)=5. Hmm, 5 x-orbits from 2 y-orbits? Let me see.

For n=4 (even), each y has 2 x-preimages with S and -S. 
- y=0000: x=HHHH (S=0) or TTTT (S=0). Both S=0.
- y=1111: x=HTHT (S=-2) or THTH (S=2). S=±2.
- y=1010: x? y=(1,0,1,0) means x1≠x2, x2=x3, x3≠x4, x4=x1. So x1=1: x2=0,x3=0,x4=1: HTTH (S=-1+0-0+1=0). x1=0: THHT (S=0+1-1+0=0). Both S=0.
- y=0101: x1≠x2? y1=0: x1=x2. y2=1: x2≠x3. y3=0: x3=x4. y4=1: x4≠x1. x1=1: x2=1,x3=0,x4=0: HHTT (S=-1+1-0+0=0). x1=0: TTHH (S=0). Both S=0.
- y=1001: y1=1:x1≠x2. y2=0:x2=x3. y3=0:x3=x4. y4=1:x4≠x1. x1=1:x2=0,x3=0,x4=0: HTTT (S=-1). x1=0: THHH (S=1). S=±1.
- y=1100: y1=1,y2=1,y3=0,y4=0. x1≠x2,x2≠x3,x3=x4,x4=x1. x1=1:x2=0,x3=1,x4=1: HTHH (S=-1+0-1+1=-1). x1=0: THTT (S=0+1+0+0=1). S=±1.
- y=0110: y1=0,y2=1,y3=1,y4=0. x1=x2,x2≠x3,x3≠x4,x4=x1. x1=1:x2=1,x3=0,x4=1: HH TH=(1,1,0,1) S=-1+1-0+1=1. x1=0: TTHH? x2=0,x3=1,x4=0: (0,0,1,0) S=0+0-1+0=-1. S=±1.
- y=0011: y1=0,y2=0,y3=1,y4=1. x1=x2,x2=x3,x3≠x4,x4≠x1. x1=1:x2=1,x3=1,x4=0: HHHT S=-1+1-1+0=-1. x1=0: TTTH S=0+0-0+1=1. S=±1.

So:
- y-orbit (index-parity 0): {0000, 1010, 0101, 1001, 1111}. x-preimages: 
  - 0000 -> S=0 (HHHH, TTTT)
  - 1010 -> S=0 (HTTH, THHT)
  - 0101 -> S=0 (HHTT, TTHH)
  - 1001 -> S=±1 (HTTT S=-1, THHH S=1)
  - 1111 -> S=±2 (HTHT S=-2, THTH S=2)
- y-orbit (index-parity 1): {1100, 0110, 0011}. x-preimages:
  - 1100 -> S=±1 (HTHH S=-1, THTT S=1)
  - 0110 -> S=±1 (HHTH S=1, TTHT S=-1)
  - 0011 -> S=±1 (HHHT S=-1, TTTH S=1)

So within y-orbit 0, we have x-configs with S ∈ {0, ±1, ±2}. Within y-orbit 1, x-configs with S ∈ {±1} only. So the x-orbits are NOT simply determined by y-orbit. S is a finer invariant. And S=0 configs all come from y-orbit 0. S=±1 configs come from both y-orbits. S=±2 from y-orbit 0.

Since V(4)=5 (S=-2,-1,0,1,2 each one orbit), and S=±1 each one orbit despite coming from two y-orbits... So within a fixed S, configs from different y-orbits are still connected. That means the y-orbit structure is NOT the right way to think about it; S is the true invariant and it's complete, and the y-index-parity is a coarser invariant that doesn't fully separate x-orbits.

OK so let me just directly prove S is complete for n even, and V(n)=2 for n odd. Let me think about a clean proof.

Let me reconsider. I'll prove both cases by showing we can reduce any configuration to a canonical form.

Reformulation: Let me use 0/1 for coins. Operation: if x_i = x_{i+1}, set both to 1-x_i.

For n even, invariant S = sum_{i=1}^n (-1)^i x_i (using (-1)^i, so odd positions contribute -x_i, even positions +x_i). Equivalently S = (sum of x at even positions) - (sum of x at odd positions).

Claim: Two configs are equivalent iff they have the same S.

Proof of "if": Show any config can be reduced to canonical form C(S) = (all heads on even positions if S≥0, or all heads on odd positions if S<0), specifically: if S = s ≥ 0, place s heads at the first s even positions, rest tails. If s < 0, place |s| heads at first |s| odd positions, rest tails.

To show this, I'll prove we can perform the following moves:
1. Move a head from an even position to an adjacent even position (i.e., by 2 steps), keeping everything else fixed, when there's a tail in between.
2. Cancel a head at an even position with a head at an odd position (reducing both counts, preserving S? No—canceling one even head and one odd head changes S by -1 - (+1) ... wait S = even_heads - odd_heads. Removing one even head: S -> S-1. Removing one odd head: S -> S+1. Both: S unchanged. So canceling an even head and odd head preserves S. Good.)
3. Create a head at even and odd position (both new), preserving S.

Hmm, but actually the operation flips two equal adjacent coins. Let me think about what "cancel" means. If we have H at an even position and H at an adjacent odd position (i.e., two adjacent heads), flipping them gives T T: removes both heads. That's canceling an even head and odd head (adjacent). S unchanged. ✓. Conversely, two adjacent tails -> two adjacent heads: creates even+odd head. S unchanged.

And "moving a head by 2": H T T -> T T H (shown earlier): head at odd pos i, tail at i+1, tail at i+2 -> tail, tail, head at i+2. Wait that moves head from i to i+2, both odd (if i odd). But it requires the pattern H T T. Alternatively T T H -> H T T. So a head at an odd position can move by ±2 through a T T or H H... let me re-examine. H T T -> H H H -> T T H. The intermediate is all H. Hmm, this changes the config non-locally but net effect is head moves by 2.

Actually, the net effect H T T -> T T H: this is moving a head from position i to i+2, where positions i+1, i+2 were both T. After: position i is T, i+1 is T, i+2 is H. So the head moved right by 2, and the two T's stayed T. 

But wait, this requires i+1 and i+2 to both be T initially. What if they're not? Let me think about when we can move a head.

Actually, let me think about it as: the operation allows us to "propagate" a boundary. Let me think in terms of the y-representation after all, but more carefully, combining with S.

Hmm, let me step back and think about whether there's a cleaner way.

Let me reconsider the problem using the y = transitions representation, but now track everything including the "absolute" information.

Actually, here's a cleaner idea. Let me define the problem on a path vs circle and use known results.

Let me reconsider. I'll prove the two lemmas by explicit construction of moves.

Lemma A (Move): On a circle of n ≥ 3 coins, if there exist three consecutive coins with pattern H T T or T H H (i.e., a single coin followed by two of the opposite), we can move the single coin by 2 positions. Specifically, H T T -> T T H (move H right by 2) and dually T H H -> H H T.

Proof: H T T: flip the T T pair (positions 2,3) -> H H H. Then flip the H H pair (positions 1,2) -> T T H. Net: H T T -> T T H. ✓ (requires the two operations to be valid, which they are). Similarly T H H -> H H T.

Lemma B (Cancel/Create): Two adjacent equal coins can be flipped: H H -> T T or T T -> H H. This is the basic operation.

Now, using these, let me show connectivity.

Case n even, prove S is complete.

Given any config, I want to reduce it to canonical form. 

Step 1: Use cancel/create to make the number of "transitions" small, and use moves to consolidate heads.

Hmm, this is still vague. Let me think about it more carefully.

Let me think about the "blocks": maximal runs of equal coins. The operation flips an adjacent equal pair, which is within a block of length ≥ 2.

Actually, let me think about the y-representation and prove Lemma 1 (n odd: one y-orbit) and a corresponding result for n even, then handle the x-level.

Let me prove Lemma 1: For n odd (n ≥ 3), all y-strings with even number of 1's form one orbit.

In y-space, operation: at position i with y_i=0, flip y_{i-1}, y_{i+1}.

Sub-moves in y-space:
- "1 0 1 -> 0 0 0": annihilate two 1's separated by one 0 (at positions i-1, i+1, act at i).
- "0 0 0 -> 1 0 1": create two 1's.
- "1 0 0 -> 0 0 1" or "0 0 1 -> 1 0 0": move a 1 by 2 (act at the 0 adjacent to a 1 and another 0).

Wait let me recheck the move. y = (...,1,0,0,...) with the 1 at position j, 0 at j+1, 0 at j+2. Act at position j+1 (y_{j+1}=0): flip y_j and y_{j+2}: y_j 1->0, y_{j+2} 0->1. Result: (...,0,0,1,...). So 1 at j moves to 1 at j+2. ✓. This is "move 1 right by 2." Similarly move left by 2.

So in y-space, a 1 can move by ±2 (through 0's), and pairs "1 0 1" can annihilate, and "0 0 0" can create "1 0 1".

For n odd: moving by 2 generates all positions (since gcd(2,n)=1). So a 1 can move anywhere. Given any two 1's, we can move them to be separated by exactly one 0 (positions i, i+2), then annihilate. So any config with ≥2 ones can be reduced to fewer ones. Repeating, reduce to 0 ones (if even count) — but wait, we can only annihilate pairs, and we start with even number. So reduce to 0 ones = all zeros. But can we always arrange two 1's to be at distance 2 (separated by one 0)? 

Move a 1 to any position. Take two 1's, move one to position p and the other to position p+2 (mod n). Since we can move freely (n odd, ±2 generates all), yes. But we need the path to be clear (the 1 moves through 0's). If there are other 1's in the way, move them away first. Since we can move 1's around freely, we can always arrange. So: move all but two 1's to annihilate with each other, then annihilate the last two. Result: all zeros. 

Wait, but to annihilate two 1's at positions p, p+2, we need y_p=1, y_{p+1}=0, y_{p+2}=1, and act at p+1. The position p+1 must be 0. If we've moved the two 1's to p and p+2, and all others are gone (annihilated), then p+1 is 0. ✓. 

But actually, can we always reduce? Let me reconsider: we have 2k ones. Pair them up, move each pair to (p, p+2) and annihilate. But moving might be blocked by other 1's. However, since we can move 1's one at a time and the circle has room (n ≥ 2k+1 for the zeros to exist... well if 2k = n, all ones, but n odd means 2k ≠ n, so there's at least one 0). Actually if all positions are 1 (2k = n), but n is odd so 2k can't equal n. So there's always at least one 0. Good. And we can move 1's through 0's. With at least one 0, we can maneuver. 

Hmm, but moving a 1 by 2 requires the landing spot to be 0 and the middle to be 0. Let me re-examine: to move 1 from j to j+2, need y_{j+1}=0 and y_{j+2}=0 (act at j+1, flips y_j and y_{j+2}). After: y_j=0, y_{j+1}=0, y_{j+2}=1. So need both j+1 and j+2 to be 0. If there's a 1 at j+2, can't move there directly. But we can move other 1's away first. Since there's at least one 0 and n is odd, we have room to shuffle. I think this works but let me just accept it for the proof sketch; the key insight is that for n odd, the y-orbit is everything (one orbit).

Actually, let me also handle the creation direction: from all zeros, we can create "1 0 1" anywhere (act at any 0 in all-zeros, creates two 1's at distance 2). So from all-zeros we can reach any config with 2 ones (at distance 2, then move them around to any positions). And from 2 ones, create more, etc. So all-zeros reaches everything. Combined with everything reduces to all-zeros, it's one orbit. ✓.

So Lemma 1: for n odd, # y-orbits = 1, V(n) = 2*1 = 2.

Wait, I need to double-check the step "from all-zeros, reach any config with 2 ones at any positions." From all-zeros, act at position i: creates 1's at i-1, i+1 (distance 2). Then move them around by ±2. Since gcd(2,n)=1 (n odd), a 1 can reach any position. So two 1's can be placed at any two positions. ✓. And from 2 ones, act at a 0-position far from them to create 2 more, etc. So yes, one orbit. ✓.

Now Lemma 2: for n even, V(n) = n + 1.

For n even, I'll prove S is a complete invariant. S = sum_{i even} x_i - sum_{i odd} x_i, ranging over {-n/2, ..., n/2}, n+1 values.

S is invariant (proven). Need: any config with S = s can be reduced to canonical C(s).

Let me prove by showing we can:
(i) Move a head at an even position to any other even position (by 2 steps), and similarly odd to odd.
(ii) Cancel a head at even position and adjacent head at odd position (HH -> TT), reducing both even-head-count and odd-head-count by 1, S unchanged.
(iii) Create a head at even and adjacent odd position (TT -> HH), S unchanged.

Using (i), (ii), (iii): Given a config with S = s = E - O (E = even heads, O = odd heads). 
- If E > O (s > 0): cancel min(E,O) = O pairs of (even head, odd head) by bringing them adjacent and canceling. This leaves E - O = s even-heads and 0 odd-heads. Then move the s even-heads to the first s even positions. Result: canonical C(s). 
- If E < O (s < 0): cancel E pairs, leaving O - E = -s odd-heads, move to first |s| odd positions. Canonical C(s).
- If E = O (s = 0): cancel all pairs. Result: all tails (canonical C(0), since s=0 canonical is all tails). Wait, canonical C(0): s=0 ≥ 0, so s heads at even positions = 0 heads = all tails. ✓.

But wait, I need to make sure (i), (ii), (iii) are always executable.

(ii) Cancel: need an even head and odd head that are adjacent. Using (i), move an even head next to an odd head (adjacent positions are one even, one odd). Bring them adjacent, then flip (HH -> TT). ✓. But need them to both be H and adjacent; after moving, they are. ✓.

(i) Move even head by 2: need the move H T T -> T T H or similar. To move a head at even position j to j+2 (even), need positions j+1 (odd) and j+2 (even) to be T T. If they're not, we need to clear them. Hmm, this could be circular. Let me think.

Actually, the move H T T -> T T H requires the next two to be T T. What if position j+1 is H? Then we have H H at j, j+1 — we could cancel them (but that removes our head). Alternatively, think of it as: we can move a head through a region of tails. If the path is blocked by heads, we deal with those heads first (cancel or move them).

Let me think about this more carefully. Actually, since we can cancel any adjacent HH pair and create any adjacent TT->HH pair, and move heads through tails, the system is quite flexible. Let me argue as follows:

Claim: For n even, within a fixed S, all configs are connected.

Proof: I'll show any config reduces to canonical. 

First, note that the operation HH->TT (adjacent) and TT->HH (adjacent) are available. Also, the "move" H T T -> T T H (and symmetrically) is available.

Consider the config. While there exists an adjacent HH pair with one even and one odd (which is any adjacent HH pair since adjacent positions have opposite parity), and we want to reduce: flip it to TT. This reduces both E and O by 1, S unchanged. 

But this might not always lead to canonical because after removing all adjacent HH pairs, we might have isolated heads (no two adjacent). Then we need to move them together.

Hmm, let me think about isolated heads. If no two heads are adjacent, every head is surrounded by tails. Then H T T -> T T H moves a head by 2 (through tails). Since all non-head positions are tails (in the isolated case), we can move heads freely by 2. Even heads move among even positions, odd among odd. So we can bring an even head and odd head to adjacent positions, then cancel. Repeat until only same-parity heads remain, then consolidate to canonical positions.

But what if after some cancellations, heads become adjacent and we can continue? Let me structure the proof:

1. Repeatedly cancel adjacent HH pairs (HH->TT) until no adjacent heads remain. (Each cancellation preserves S.) Now all heads are isolated (separated by ≥1 tail).

2. Now move isolated heads by 2 (using H T T -> T T H, valid since neighbors are tails) to consolidate: bring an even head and an odd head adjacent, cancel them. Repeat until only one parity of heads remains.

3. If S > 0 (remaining even heads): move them to the first S even positions. If S < 0 (remaining odd heads): move to first |S| odd positions. If S = 0: no heads remain (all tails).

Wait, after step 2, if S > 0, we have S even heads and 0 odd heads, all isolated. Move them to canonical positions (first S even positions). Since they're isolated and move through tails, and there are enough even positions (S ≤ n/2), this works. Similarly for S < 0.

But hold on—in step 1, after canceling adjacent HH pairs, could we get stuck with a config that has adjacent heads re-forming? No: HH->TT removes heads, doesn't create new adjacent heads (it creates tails). Actually it could make previously non-adjacent heads become... no, removing heads only increases separation. So step 1 terminates with all heads isolated. ✓.

In step 2: we have isolated heads. Move an even head by 2 toward an odd head. Since all heads are isolated and separated by tails, the path between them (through tails) allows moving by 2. But moving by 2 keeps the head on even positions. To bring an even head adjacent to an odd head: an even head at position j, odd head at position k. Adjacent means |j-k|=1. Move even head to j' = k±1 (which is even, since k is odd, k±1 is even). Can we move it there? Move by 2's through tails. The even head travels through even positions, all of which must be tails (except start). If some even position in between has a head, move that head away first. Since we can move all even heads independently through tails (odd positions between them are tails in the isolated config), we can rearrange. 

Hmm, actually there's a subtlety: moving an even head from j to j+2 requires positions j+1 (odd) and j+2 (even) to be T T. Position j+1 is odd; in the isolated config, it's T unless there's an odd head there. If there's an odd head at j+1, then we have H (at j) T... no, H at j (even), odd head at j+1: they're adjacent! But we said all heads are isolated (no adjacent heads). Contradiction. So j+1 is T. And j+2 (even) is T unless there's an even head there. If there's an even head at j+2, then j, j+2 both heads with j+1 tail between: they're not adjacent (separated by j+1), so isolated config allows this. But then we can't move j to j+2 (j+2 is occupied). Move the head at j+2 first, or move j in the other direction. 

I think the point is: in the isolated config, even heads are at even positions with at least one even position between consecutive even heads (since they're separated by ≥1 position, and if two even heads are at j, j+2, they're separated by one odd position, which is fine for "isolated" since they're not adjacent). Hmm, actually "isolated" means no two heads adjacent, so even heads at j and j+2 are OK (not adjacent). But then moving is blocked.

Let me reconsider. Maybe I should allow creating space. We can also do TT -> HH (create adjacent pair), which might help. This is getting complicated for a rigorous proof. Let me think if there's a cleaner approach.

Alternative clean approach: Let me use the y-representation for n even and prove there are exactly 2 y-orbits (index-parity 0 and 1), then count x-orbits via S.

Hmm, but I showed for n=4 that S is finer than y-index-parity. So that doesn't directly work.

Let me reconsider. Actually, maybe I should prove S is complete by a different method: show that the operation group acts transitively on each S-level.

Let me think about the "generators" more carefully. The operation at (i,i+1) when x_i=x_{i+1}: this is an involution g_i that acts only when x_i = x_{i+1}.

Let me think about compositions that give useful permutations.

Key composition: g_{i+1} ∘ g_i when applicable. Consider x = (..., a, b, c, ...) with a=b (so g_i applies) and after g_i, check g_{i+1}.

g_i: (a, a, c) -> (1-a, 1-a, c). Now for g_{i+1}: need x_{i+1} = x_{i+2}, i.e., 1-a = c, i.e., c = 1-a. So if original (a, a, 1-a), then g_i g_{i+1}: (a,a,1-a) -> (1-a,1-a,1-a) -> (1-a, a, a). Net: (a,a,1-a) -> (1-a,a,a). This shifts the "odd one out." 

Hmm, (a, a, 1-a) -> (1-a, a, a): the position of the "different" coin moved from i+2 to i. So a single different coin moves left by 2. Dually it can move right by 2. This is the same move as before.

Let me think about the problem differently. Let me consider the quantity S and show that the orbit of any config with S=s contains the canonical config, by induction on some measure.

Measure: number of heads. 

If the config has an adjacent HH pair: cancel it (HH->TT), reducing heads by 2, S unchanged. By induction, the reduced config (fewer heads, same S) reaches canonical. So original reaches canonical. ✓. (Base case: no adjacent HH pairs, i.e., all heads isolated.)

If no adjacent HH pair (all heads isolated): 
- If there are both even and odd heads: take an even head and odd head. They're not adjacent (isolated). Move them together (by 2-steps through tails) to become adjacent, then cancel. This reduces heads by 2, S unchanged. By induction, reaches canonical.
- If only even heads (S > 0) or only odd heads (S < 0): move them to canonical positions. No cancellation needed; just rearrange. 
- If no heads (S=0): already canonical (all tails).

The induction is on number of heads, which decreases by 2 in each cancellation step. The rearrangement step (only same-parity heads) doesn't change head count but reaches canonical directly.

Now I need to rigorously justify "move them together through tails." In the isolated config, all non-head positions are tails. To move an even head from position j to j+2: need j+1, j+2 both tails. j+1 is odd: it's a tail (if it were a head, it'd be an odd head adjacent to even head at j, contradicting isolated). j+2 is even: it's a tail unless there's an even head there. If there's an even head at j+2, we have two even heads at j, j+2 (not adjacent, OK). To move past it, first move the j+2 head further right. But this could cascade. 

However, since the circle is finite and there are tails somewhere (if not all heads, and if all heads then n even all heads means S = n/2 - n/2... wait all heads: E = n/2, O = n/2, S = 0. But all heads has adjacent heads, so step 1 would cancel. So isolated config with only even heads has E = S ≤ n/2 heads at even positions, and n/2 even positions total, so at least n/2 - S ≥ 0 even positions are tails. If S < n/2, there's at least one even tail. 

To move even heads to the first S even positions: process from left to right. For position 2 (first even), if it should have a head (S ≥ 1) but doesn't, find the nearest even head to the right and move it left by 2 repeatedly until it reaches position 2. Moving left by 2: from j to j-2, need j-1, j-2 both tails. j-1 is odd: tail (isolated, and if odd head there it'd be adjacent to even head—wait, we might have odd heads too if we're in the "both parities" case). 

Hmm, I'm in the "only even heads" subcase, so all odd positions are tails. So j-1 (odd) is always tail. j-2 (even) is tail unless there's an even head there. If there's an even head at j-2, then position 2 might already be filled or we process in order. Let me process from left to right: ensure position 2 has a head (move nearest right head to position 2), then position 4, etc. When moving a head to position 2k, the positions 2,4,...,2k-2 already have heads (placed), and 2k+2,... might have heads. Move the nearest head at position 2m (m > k) leftward to 2k. Path: 2m -> 2m-2 -> ... -> 2k. Each step needs 2m-1 (odd, tail ✓) and 2m-2 (even). 2m-2: if m-1 > k, it might have a head (one of the remaining heads). Hmm. 

OK this is getting tedious but I believe it works. The key point: in the "only even heads, all odd positions tail" config, even heads can be moved freely among even positions (since odd positions are all tails, providing the "buffer"), as long as there's at least one even tail to allow passing. Actually, with all odd positions as tails, moving an even head from j to j+2 needs j+1 (tail ✓) and j+2 (even, need tail). If j+2 has a head, swap roles: think of it as moving the "gap" (even tail) instead. There's at least one even gap (since S < n/2 or S = n/2 means all even positions are heads = canonical already). Moving the gap by 2: T at even position, move it by 2: T H H -> H H T (dual of H T T -> T T H). T H H -> H H T: flip HH (positions j+1, j+2)... wait T at even position j, then j+1 (odd) = H? But odd positions are all tails in this subcase. Contradiction. So T H H can't occur (odd position is T, not H). 

Hmm, so in the "only even heads" config, odd positions are all T. So the config looks like: (T/H at even, T at odd). E.g., n=6: positions 1-6, even positions 2,4,6: (x1, x2, x3, x4, x5, x6) = (T, ?, T, ?, T, ?) where ? ∈ {H,T}. So config is T ? T ? T ?. Adjacent pairs: (1,2)=(T,?), (2,3)=(?,T), (3,4)=(T,?), etc. For an operation, need adjacent equal. (1,2)=(T,?): equal iff ?=T. So if x2=T, flip (1,2): both T->H: (H,H,T,?,T,?). Now x1=H (odd position head!). This breaks the "only even heads" property. Hmm. So the operation can create odd heads. That's fine—we're trying to reach canonical, and intermediate steps can have any config.

OK I think the proof is essentially correct but the details are messy. Let me just present the clean version: S is invariant, and by cancellation and moves, any config reduces to canonical. I'll state the moves clearly and argue they suffice.

Actually, let me reconsider and find a cleaner proof. 

Clean proof idea using y-representation for both cases:

For n even: Let me reconsider what S corresponds to in y-space. 

S = sum_{i even} x_i - sum_{i odd} x_i. 

Hmm, let me compute S in terms of y. We have x_{i+1} = x_i XOR y_i. So x_j = x_1 XOR y_1 XOR ... XOR y_{j-1}. This expresses all x in terms of x_1 and y. Then S = sum (-1)^j x_j = sum (-1)^j (x_1 XOR y_1 XOR ... XOR y_{j-1}). This is messy.

Let me try a different invariant connection. For n even, consider the "checkerboard" weighting. Actually, let me just go with the direct proof.

Let me reconsider: maybe the cleanest is to prove the move lemmas and argue connectivity, accepting some handwaving on the rearrangement, since this is a competition problem and the key insight (invariant + completeness) is what matters.

Let me also reconsider whether V(n) = 2 for all odd n and V(n) = n+1 for all even n is correct by checking n=5 or n=6 partially.

n=5, V(5)=2 (conjectured). Let me spot check: S not defined for n=5 (odd). Parity of heads is invariant. Configs: 32 total, 16 even parity, 16 odd. If V(5)=2, all even-parity configs are one class, all odd-parity another. Let me verify a piece: TTTTT (0 heads, even) and HHTTT (2 heads, even) should be connected. TTTTT: flip (1,2)->HHTTT. ✓ directly. Good. HHTTT and HTHTT (2 heads, even)? HHTTT=(1,1,0,0,0). HTHTT=(1,0,1,0,0). HHTTT: flip (1,2)->TTTTT. TTTTT: flip(3,4)->TTHTT? (0,0,1,1,0)? wait flip (3,4) of TTTTT: (0,0,1,1,0)=TTHHT. Hmm. Let me get HTHTT from TTTTT. TTTTT -> flip(1,2) -> HHTTT. HHTTT: flip(3,4)? (3,4)=(0,0) TT -> flip -> (1,1,1,1,0)? No: HHTTT=(1,1,0,0,0), flip (3,4): (1,1,1,1,0)=HHHHT. Then flip (2,3): (1,0,0,1,0)=HTTHT. Then flip (4,5): (4,5)=(1,0) differ. flip(3,4): (0,0,1,0)... (1,0,0,1,0) flip (3,4): (1,0,1,0,0)=HTHTT. ✓. So connected. Good, consistent with V(5)=2.

Let me also verify n=6 partially. V(6)=7 conjectured. S ranges -3..3. Let me check S=3: only HHTHTH? No. S=3 means E-O=3, max E=3 (all even heads), O=0. So config = all even positions H, all odd T: (T,H,T,H,T,H) = THTHTH. S = 0+1+0+1+0+1 = 3 ✓. Only one config with S=3. So one orbit. ✓. S=-3: HTHTHT, one config. S=2: E-O=2. E=3,O=1 or E=2,O=0. Multiple configs. Should be one orbit. I'll trust it.

So the answer: sum_{n=1}^{20} V(n).
- n odd: 1,3,5,7,9,11,13,15,17,19 (10 values), each V=2. Sum = 20.
- n even: 2,4,6,8,10,12,14,16,18,20 (10 values), V(n)=n+1. Sum = (3+5+7+9+11+13+15+17+19+21) = sum of (n+1) for n=2,4,...,20 = sum of 3,5,...,21 = 10 terms, average (3+21)/2=12, sum=120. Or: sum_{n even, 2 to 20} (n+1) = (2+4+...+20) + 10 = 110/2*... wait sum 2+4+...+20 = 2*(1+2+...+10)=2*55=110. Plus 10 = 120.
- Total = 20 + 120 = 140.

Let me double-check: sum of odd n from 1 to 19: V=2 each, 10 odd numbers, 10*2=20. Sum of even n from 2 to 20: V=n+1, sum = (3+5+7+9+11+13+15+17+19+21). Let me add: 3+5=8, +7=15, +9=24, +11=35, +13=48, +15=63, +17=80, +19=99, +21=120. Yes 120. Total 140.

Now let me write up the proof cleanly.

Let me reconsider the proof of completeness for n even once more to make it rigorous enough.

I'll prove: For n even, two configurations are equivalent iff they have the same S.

"Invariant" direction: S is preserved by operations (proven).

"Complete" direction: Show every config reduces to canonical C(s).

I'll use these moves:
- Cancel: adjacent HH -> TT (basic operation).
- Create: adjacent TT -> HH (basic operation).
- Hop: H T T -> T T H and T H H -> H H T (two-step sequences), moving a head by 2 positions through two equal coins.

Proof of Hop: H T T: the pair (positions 2,3) is TT, flip -> H H H; then pair (1,2) is HH, flip -> T T H. Net H T T -> T T H. ✓. Similarly T H H -> H H T.

Now the reduction:
1. If there's an adjacent HH pair, cancel it (reduces head count by 2, S unchanged). Repeat until no adjacent HH. (Terminates since heads decrease.)
2. Now all heads are isolated (no two adjacent). 
   - If there are both an even-positioned head and an odd-positioned head: I want to bring them adjacent and cancel. 
   - Claim: using Hops, we can move an isolated head by 2 positions to any position of the same parity, as long as the path's odd/even intermediate positions are clear. 

Hmm, the issue is when the path is blocked. Let me think about whether in the isolated config, we can always bring an even head and odd head adjacent.

In the isolated config, heads are separated by ≥1 tail. Consider an even head at position p and an odd head at position q. WLOG p < q (in cyclic order). The arc from p to q contains some positions. Since heads are isolated, between p and q there might be other heads, each isolated. 

Alternative: Let me use Create to help. We can create adjacent HH from TT. So even if heads are isolated, we can create new adjacent pairs to facilitate movement, then cancel. 

Actually, here's a cleaner approach: I'll show that from any config, we can reach a config with an adjacent HH pair (unless it's already canonical with ≤1 head or all-same-parity isolated). 

Hmm, let me think about it yet differently. Let me just prove that the canonical form is reachable by showing the moves generate a transitive action on each S-level, using the fact that we can simulate "moving a head by 1" via create+cancel.

Move a head by 1 position: H T -> ? We want to move H from position i to i+1. Consider H T T T (head at i, tails at i+1,i+2,i+3). Create at (i+1,i+2): TT->HH: H H H T. Cancel at (i,i+1): HH->TT: T T H T. Net: H T T T -> T T H T. Head moved from i to i+2 (by 2). That's the Hop again, not by 1.

To move by 1: H T -> T H? Consider H T H (heads at i, i+2, tail at i+1). This is isolated. Hmm. H T H: no adjacent equal (HT, TH, and cyclically H...H at distance 2). For n=3 circle H T H: pairs (1,2)=HT, (2,3)=TH, (3,1)=HH. Oh (3,1) is HH (cyclic)! So cancel: H T H -> T T T (flip 3,1). So HTH -> TTT. That reduces heads. Not a move.

I think moving by 1 isn't directly possible, but moving by 2 is, and for n even, even positions and odd positions are separate, so moving by 2 within a parity class is enough to reach any position of that parity. The issue is only blocking.

Let me just argue the blocking can be resolved: In the isolated config with both even and odd heads, pick the even head and odd head that are closest (cyclically). Between them, all positions are tails (since they're the closest pair of opposite parity, and any head between would be same-parity to one of them... hmm, not necessarily). 

Ugh, let me think about this more carefully with a cleaner invariant argument.

Actually, you know what, let me just use the y-representation result and connect it properly. Let me prove:

For n even: there are exactly 2 y-orbits (index-parity 0 and 1). Then I'll count x-orbits.

Wait, but I showed n=4 has S finer than index-parity. So 2 y-orbits but 5 x-orbits. The relationship is not straightforward. Let me recompute.

For n=4: y-orbit 0 (index-parity 0) contains y-strings {0000, 1001, 1010, 0101, 1111}. The x-configs over this y-orbit have S ∈ {0, ±1, ±2}. y-orbit 1 (index-parity 1) contains {1100, 0110, 0011}, x-configs have S ∈ {±1}. 

The x-orbits: S=0 (from y-orbit 0 only), S=±1 (from both y-orbits), S=±2 (from y-orbit 0 only). And each S-value is one x-orbit. So S=1 configs come from both y-orbits but are all connected. That means within the x-level, operations connect across y-orbits? But the y-map is equivariant, so x-operations project to y-operations, keeping y within its y-orbit. So an x-orbit projects to a single y-orbit. Contradiction with S=1 coming from two y-orbits!

Wait, that means S=1 is NOT one x-orbit. Let me recheck V(4).

Let me recheck: are the S=1 configs all connected? S=1 configs: TTTH, HHTH, THTT, THHH (from my earlier list). Let me check their y-values:
- TTTH=(0,0,0,1): y1=0,y2=0,y3=1,y4=1: y=0011 (index-parity 1).
- HHTH=(1,1,0,1): y1=0,y2=1,y3=1,y4=0: y=0110 (index-parity 1).
- THTT=(0,1,0,0): y1=1,y2=1,y3=0,y4=0: y=1100 (index-parity 1).
- THHH=(0,1,1,1): y1=1,y2=0,y3=0,y4=1: y=1001 (index-parity 0).

So S=1 configs: three from y-orbit 1 (TTTH, HHTH, THTT) and one from y-orbit 0 (THHH). If x-orbits project to y-orbits, then THHH (y-orbit 0) is NOT in the same x-orbit as the other three (y-orbit 1). So S=1 splits into at least 2 x-orbits!

Let me recheck V(4) by direct computation. I earlier claimed all S=0 connected and all S=-1 connected, but I didn't check S=1 carefully. Let me recheck.

S=1 configs: TTTH=(0,0,0,1), HHTH=(1,1,0,1), THTT=(0,1,0,0), THHH=(0,1,1,1).

Check connectivity:
TTTH=(0,0,0,1): pairs (1,2)=TT->flip->(1,1,0,1)=HHTH. (2,3)=TT->flip->(0,1,1,1)=THHH. (3,4)=TH diff. (4,1)=HT... (4,1): x4=1,x1=0 differ. So TTTH -> HHTH, THHH.
So TTTH connects to HHTH and THHH! But TTTH is y-orbit 1 and THHH is y-orbit 0. So they ARE in the same x-orbit, meaning x-operations can change the y-orbit?! 

But the y-map is equivariant... let me recheck. TTTH=(0,0,0,1), y=0011. Operation flip (1,2): (1,1,0,1)=HHTH, y = 0,1,1,0 = 0110. So y changed from 0011 to 0110. Both index-parity 1. OK same y-orbit. Operation flip (2,3): (0,1,1,1)=THHH, y=1,0,0,1=1001. y changed from 0011 (index-parity 1) to 1001 (index-parity 0)! 

So the y-orbit changed! That means index-parity is NOT invariant under the operation for n=4?! Let me recheck.

y=0011: index-parity = parity of 1's at even positions {2,4}: y2=0, y4=1, so 1 (odd). 
Operation: flip (2,3) in x: x=(0,0,0,1)->(0,1,1,1). y: y1=x1^x2=0^1=1, y2=x2^x3=1^1=0, y3=x3^x4=1^1=0, y4=x4^x1=1^0=1. y=1001. index-parity: y2=0,y4=1: 1 (odd). 

Wait, I need to recompute. y4 = x4 XOR x1. For THHH=(0,1,1,1): x4=1, x1=0, y4=1. y2 = x2 XOR x3 = 1 XOR 1 = 0. So index-parity = y2 + y4 = 0 + 1 = 1 (odd). Same as before! I made an error earlier. Let me recompute the index-parity for 1001.

y=1001: positions 1,2,3,4 = 1,0,0,1. Even positions {2,4}: y2=0, y4=1. Count of 1's at even positions = 1 (odd). So index-parity = 1 (odd). 

Earlier I listed 1001 as index-parity 0. That was wrong! Let me recompute all.

y=0000: even 1's count = 0, parity 0.
y=1100: y2=1,y4=0: count 1, parity 1.
y=0110: y2=1,y4=0: count 1, parity 1.
y=0011: y2=0,y4=1: count 1, parity 1.
y=1001: y2=0,y4=1: count 1, parity 1.
y=1010: y2=0,y4=0: count 0, parity 0.
y=0101: y2=1,y4=1: count 2, parity 0.
y=1111: y2=1,y4=1: count 2, parity 0.

So index-parity 0: {0000, 1010, 0101, 1111} (4 strings). Index-parity 1: {1100, 0110, 0011, 1001} (4 strings). I had misclassified 1001 earlier. Good, so 1001 is index-parity 1, same as 0011. So the operation 0011 -> 1001 stays in index-parity 1. ✓. No contradiction.

So let me redo the x-orbit analysis for n=4.
y-orbit 0 (index-parity 0): {0000, 1010, 0101, 1111}.
- 0000: x=HHHH(S=0)/TTTT(S=0).
- 1010: x=HTTH(S=0)/THHT(S=0).
- 0101: x=HHTT(S=0)/TTHH(S=0).
- 1111: x=HTHT(S=-2)/THTH(S=2).
y-orbit 1 (index-parity 1): {1100, 0110, 0011, 1001}.
- 1100: x=HTHH(S=-1)/THTT(S=1).
- 0110: x=HHTH(S=1)/TTHT(S=-1).
- 0011: x=HHHT(S=-1)/TTTH(S=1).
- 1001: x=HTTT(S=-1)/THHH(S=1).

So y-orbit 0 has x-configs with S ∈ {0, ±2}. y-orbit 1 has x-configs with S ∈ {±1}. 

So S=0 and S=±2 come from y-orbit 0; S=±1 from y-orbit 1. So S is determined by y-orbit (for n=4): y-orbit 0 ↔ S even (0, ±2), y-orbit 1 ↔ S odd (±1). And within each y-orbit, the x-configs split by S. 

y-orbit 0: S ∈ {0, 2, -2}. S=0: {HHHH, TTTT, HTTH, THHT, HHTT, TTHH} (6 configs). S=2: {THTH}. S=-2: {HTHT}. Are the S=0 configs all connected? Yes (verified earlier). So y-orbit 0 gives 3 x-orbits (S=0, S=2, S=-2).
y-orbit 1: S ∈ {1, -1}. S=1: {THTT, HHTH, TTTH, THHH} (4 configs). S=-1: {HTHH, TTHT, HHHT, HTTT} (4 configs). Are S=1 configs all connected? TTTH -> HHTH, THHH (shown). HHTH=(1,1,0,1): (1,2)=HH->flip->(0,0,0,1)=TTTH. (2,3)=HT diff. (3,4)=TH diff. (4,1)=HH->flip->(0,1,1,0)=THHT? wait (4,1): x4=1,x1=1 same->flip both: x4->0,x1->0:
