# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $S = \{z_1, z_2, \dots, z_{10}\}$ be a set consisting of 10 distinct complex numbers, among which exactly 7 are real numbers. Let $N$ be the maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$. Find $N$.       — 题目文本
#   The problem is equivalent to the original proof-based problem for $n=10$. The solution shows that for $n \ge 9$, since there are exactly 3 imaginary numbers in $S$ and $n-3$ real numbers, $f$ must be a real-coefficient polynomial. This implies that $f$ must map the set of imaginary numbers to itself. By considering the permutations of the three imaginary numbers and the property that $f$ is real, the solution concludes there are at most two such quadratic polynomials. Specifically, the cases show that either one or two such polynomials can exist depending on whether conjugates are present in the set of imaginary numbers.  — 标准解答
#   Let me solve this problem. It's a math problem, no tools needed. Let me think carefully.

We have S = {z_1, ..., z_10}, 10 distinct complex numbers, exactly 7 real. We want the maximum possible number of quadratic polynomials f(z) with complex coefficients such that f(S) = S (as a set).

A quadratic polynomial f(z) = az² + bz + c with a ≠ 0. We want f to permute the set S, i.e., f(S) = S as sets.

First, let me think about the structure. A quadratic polynomial is a 2-to-1 map generically. For f(S) = S with |S| = 10, we need f to map S to S. Since f is a function (not necessarily injective on S), but f(S) = S means every element of S is hit.

Actually, let me think about this more carefully. f is a quadratic, so it's at most 2-to-1. For f(S) = S, we need f restricted to S to be a surjection onto S. Since |S| = 10 and f is at most 2-to-1, the number of elements in S mapping to each element of S is at most 2, and the total count is 10 (elements of S) mapping to 10 elements (S), so on average 1 preimage per element. So some elements have 1 preimage and some have 2, but the total must be 10. If k elements have 2 preimages and the rest have 1, then 2k + (10-k) = 10, so k = 0. So f is actually a bijection (permutation) on S!

Wait, that's only if every element of S is in the image and we count preimages within S. Let me reconsider. f(S) = S means f maps S onto S. The image f(S) has at most 10 elements (could be fewer if not injective). For f(S) = S we need |f(S)| = 10, which means f is injective on S (since |S| = 10 and f(S) ⊆ S with |f(S)| = 10 = |S|). So f restricted to S is a bijection/permutation.

So f permutes S. A quadratic polynomial that permutes a finite set.

Now, a quadratic f(z) = az² + bz + c. We can conjugate: f(z) = a(z + b/(2a))² + (c - b²/(4a)). So up to affine change of variables, f is z ↦ z² (scaled). Actually f(z) = a(z - h)² + k where h = -b/(2a), k = c - b²/(4a).

So f(z) = a(z-h)² + k. The "center" is h, and f is symmetric about h: f(h + w) = f(h - w) = aw² + k.

For f to be injective on S, no two elements of S can be symmetric about h (i.e., sum to 2h), unless they're the same element.

Actually, f is injective on S means: for any two distinct z_i, z_j in S, f(z_i) ≠ f(z_j). Since f(z_i) = f(z_j) iff a(z_i - h)² = a(z_j - h)² iff (z_i - h)² = (z_j - h)² iff z_i - h = ±(z_j - h), i.e., z_i = z_j or z_i + z_j = 2h.

So f is injective on S iff no two distinct elements of S sum to 2h. (Equivalently, h is not the midpoint of any pair in S, and also no element equals h... wait, if z_i = h, then z_i - h = 0, and we'd need another element with (z_j - h)² = 0, i.e., z_j = h, but elements are distinct so only one. So that's fine.)

So the condition for f to be a permutation of S is:
1. a ≠ 0
2. No two distinct elements of S sum to 2h (where h = -b/(2a))
3. f(S) = S, i.e., {a(z_i - h)² + k : i = 1..10} = S.

Condition 3 is the hard one. Given h satisfying condition 2, we need a, k such that the map z ↦ a(z-h)² + k permutes S.

Let me think of it differently. Let's fix h. Define the map φ_h: z ↦ (z - h)². This maps S to a multiset of 10 values (all distinct by condition 2). Then f(z) = a·φ_h(z) + k. We need a·φ_h(S) + k = S as sets, i.e., the set {(z_i - h)²} when scaled by a and translated by k gives S.

So we need: there exist a, k such that a·T + k = S where T = {(z_i - h)² : i = 1..10} (a set of 10 distinct complex numbers).

This means T and S are related by an affine map: S = aT + k. Equivalently, T = (S - k)/a, i.e., T is an affine image of S.

So the question becomes: for how many values of h (with the injectivity condition) is the set {(z - h)² : z ∈ S} an affine image of S?

Hmm, this is getting complex. Let me think about the structure of S with 7 real and 3 non-real elements.

The 3 non-real elements: since complex conjugation... well, S is just a set, no symmetry required. But let me think about what constraints the real/non-real split gives.

If z is real and h is real, then (z-h)² is real. If z is non-real and h is real, (z-h)² is non-real (unless z-h is purely imaginary, giving real). Hmm.

Let me think about this more carefully. Let's denote the real elements as r_1, ..., r_7 and non-real as w_1, w_2, w_3.

Case 1: h is real.
Then (r_i - h)² is real for all i. (w_j - h)²: w_j = x_j + iy_j, so (w_j - h)² = (x_j - h)² - y_j² + 2i(x_j - h)y_j. This is real iff x_j = h (i.e., w_j - h is purely imaginary), otherwise non-real.

For T = aS + k... wait, we need T to be an affine image of S, meaning T has the same "shape" as S up to scaling and translation. S has 7 real and 3 non-real. T = {(z-h)²}. 

If h is real: the real elements of S map to real values in T. The non-real elements w_j map to (w_j - h)² which is real iff Re(w_j) = h, non-real otherwise.

For T to be an affine image of S (with a, k complex), the number of real elements in T must match the structure... actually, an affine map z ↦ az + k with complex a, k can send real numbers to non-real and vice versa. So the real/non-real split isn't directly preserved unless a, k are real.

Hmm, this is quite involved. Let me think about whether there's a cleaner approach.

Actually, let me reconsider. The problem asks for the maximum N over all choices of S (with 7 real, 3 non-real). So we get to choose S to maximize the count of quadratic polynomials permuting S.

Let me think about what sets S can have many quadratic self-maps.

Key insight: A quadratic f(z) = a(z-h)² + k permutes S iff:
- h avoids being a midpoint of any pair in S (injectivity)
- The set {(z-h)² : z ∈ S} = (S - k)/a, i.e., is an affine image of S.

Let me think about small cases or symmetric configurations.

Consider S being closed under some quadratic map. 

Let me think about the structure differently. Suppose f(z) = a(z-h)² + k permutes S. Then f is a permutation of the 10 elements. As a permutation, it has some cycle structure. 

Also, consider: if f permutes S, what about iterating f? f², f³, etc. are degree 4, 8, ... polynomials, not quadratic, so they don't count.

But here's a thought: if f and g are both quadratics permuting S, then f∘g is degree 4, not quadratic (unless one is affine, but quadratics have degree exactly 2). So the set of quadratics permuting S doesn't form a group under composition.

Let me think about the problem from the perspective of counting valid h values.

For each valid h (satisfying injectivity), we need {(z-h)² : z ∈ S} to be an affine image of S. The affine image condition: two sets of 10 points are affine-equivalent. Given the set T_h = {(z-h)²}, we need T_h = aS + k for some a ≠ 0, k.

Two sets being affine equivalent is a strong condition. Given S, how many h make T_h affine-equivalent to S?

Let me think about this using the structure of S. Let me consider specific configurations.

Approach: Think about S that is invariant under z ↦ z² (or a scaled version). 

Classic example: roots of unity. If S consists of roots of z^n = 1, then z ↦ z² permutes S (when gcd(2,n) = 1, i.e., n odd). But these are on the unit circle, not 7 real + 3 non-real.

Let me think about Chebyshev-like or special configurations.

Actually, let me think about the real line structure. 7 real points. A quadratic with real coefficients maps real to real. If f has real coefficients (a, b, c real, so h, k real), then f maps real numbers to real numbers and respects conjugation: f(z̄) = f(z)̄.

For f with real coefficients permuting S (7 real, 3 non-real): the 3 non-real elements must be permuted among themselves (since f preserves "realness" only if... wait, f(z̄) = f(z)̄ means if z is non-real, f(z) is non-real iff f(z) ≠ f(z)̄, which happens unless f(z) is real. Actually f maps non-real to non-real or real. Hmm, f(z̄) = f(z)̄, so if z is non-real, f(z) could be real or non-real.

But we need f to permute S, and S has exactly 3 non-real elements. If f has real coefficients, f(conj(z)) = conj(f(z)). The non-real elements of S come in conjugate pairs or are self-conjugate (real). With 3 non-real elements, they can't all be in conjugate pairs (3 is odd). So at least one non-real element w has conj(w) ∉ S.

If f has real coefficients and w ∈ S is non-real with conj(w) ∉ S, then f(w) ∈ S and conj(f(w)) = f(conj(w)). But conj(w) ∉ S, so f(conj(w)) is not constrained to be in S. However, f(w) ∈ S. If f(w) is non-real, then conj(f(w)) ∈ S iff f(w)'s conjugate is in S. This is getting complicated.

Let me try a different, more computational approach. Let me think about what configurations allow many quadratics.

Let me consider the possibility that S is constructed to have several quadratic self-maps. 

Think about it this way: a quadratic f(z) = a(z-h)² + k is determined by (a, h, k) with a ≠ 0. The condition f(S) = S gives 10 equations (f maps S onto S) but really it's a permutation condition. Given h (with injectivity), a and k are determined by where any 2 points go... actually, given h, the set T_h = {(z-h)²} is determined. We need T_h = (S-k)/a, so a and k are determined by matching T_h to S up to affine transformation. Two 10-point sets are affine equivalent in at most... well, if T_h and S are affine equivalent, the affine map is essentially unique (determined by 2 points, and the rest must match). So for each h, there's at most one (a,k) pair (up to the matching). Actually, there could be multiple if S has affine symmetries.

So the count of quadratics permuting S is roughly the number of h values such that T_h is affine-equivalent to S, times the number of affine self-maps of S (affine symmetries).

Hmm wait. Let me re-examine. For a given h, T_h = {(z-h)² : z ∈ S}. We need T_h = σ(S) for some affine map σ(z) = az + k. The number of such (a,k) is the number of affine maps σ such that σ(S) = T_h. If S has affine symmetry group G (affine maps preserving S), then if one σ works, the number of working σ is |G|. But each σ gives a distinct quadratic f. So the count is: (number of h with injectivity and T_h affine-equivalent to S) × |G| / ... no wait, it's not that simple because different h could give the same f.

Actually, each quadratic f corresponds to a unique h (the center h = -b/(2a)). So different h give different f. And for a fixed h, different (a,k) give different f. So the total count is:

N = sum over valid h of (number of (a,k) with a{(z-h)² : z∈S} + k = S).

For a fixed h, the number of (a,k) is the number of affine maps taking T_h to S, which equals |AffSym(S)| if T_h is affine-equivalent to S, and 0 otherwise. Wait no: the number of affine maps σ with σ(T_h) = S. If T_h is affine-equivalent to S, then the set of such σ is a coset of AffSym(S) (the affine self-maps of S... actually of T_h). Hmm, let me think again.

The number of affine maps σ(z) = az + k with σ(T_h) = S. If T_h and S are affine-equivalent, pick one σ_0 with σ_0(T_h) = S. Then all others are σ_0 ∘ τ where τ is an affine self-map of T_h. The affine self-maps of T_h correspond to affine self-maps of S (since they're affine-equivalent). So the count is |AffSym(T_h)| = |AffSym(S)|.

So N = |AffSym(S)| × (number of valid h such that T_h is affine-equivalent to S).

Where "valid h" means h is not a midpoint of any pair in S (injectivity condition), and T_h = {(z-h)² : z ∈ S} is affine-equivalent to S.

Now, |AffSym(S)|: the affine symmetry group of a 10-point set in the plane. For a generic set, this is trivial (just identity, |G| = 1). For special sets, it could be larger. But with 7 real and 3 non-real points, the symmetry is limited. The 3 non-real points can't form a symmetric configuration with the 7 real points easily.

Actually, affine symmetries of S: an affine map z ↦ az + k preserving S. It must map real elements to real elements or to non-real. Since there are 7 real and 3 non-real, an affine symmetry either preserves the real subset and non-real subset, or swaps some. But 7 ≠ 3, so it can't swap all. It could map some real to non-real and some non-real to real, but the counts must work out: if r real → non-real and s non-real → real, then 7 - r + s = 7 (real count preserved) and 3 - s + r = 3, giving r = s. And r ≤ 7, s ≤ 3, so r = s ≤ 3.

This is getting complicated. Let me try to think about specific constructions.

Let me try: S = {real points forming a nice set} ∪ {3 non-real points}.

Idea: Use a set on the real line that has a quadratic self-map, plus 3 non-real points that also work.

If all 10 points were real, the problem would be about real quadratics permuting a real set. With 7 real and 3 non-real, we need to handle the non-real ones.

Let me think about the all-real case first for intuition. If S ⊂ ℝ with |S| = 10, how many quadratics f(z) = a(z-h)² + k (with real a, h, k, or complex?) permute S? If we allow complex coefficients, f could map real points to non-real, which wouldn't be in S (all real). So f must map real to real, meaning a, h, k real (well, a(z-h)² must be real for real z, so a and h real, and k real). Actually if h is non-real, (z-h)² for real z is non-real, and a times that... we'd need a(z-h)² + k real for all z in S. That's very restrictive. Basically for all-real S, f must have real coefficients (roughly).

For real S with real quadratic f(z) = a(x-h)² + k permuting S ⊂ ℝ: this is a well-studied problem. The map x ↦ a(x-h)² + k is a "tent-map-like" or "logistic-map-like" permutation of a finite set.

Actually, for a real quadratic to permute a finite real set, the set must be very special. 

Let me think about the Chebyshev connection. The Chebyshev polynomial T_n(x) = cos(n arccos(x)) permutes certain sets. But T_n has degree n, not 2. However, T_2(x) = 2x² - 1 is quadratic! T_2 maps cos(θ) ↦ cos(2θ). So if S = {cos(2πk/n) : k = 0, ..., n-1} for appropriate n, then T_2 permutes S when gcd(2, n) = 1 (n odd) — but then |S| might be less than n due to cos symmetry (cos(θ) = cos(-θ)). 

For n odd, {cos(2πk/n) : k=0,...,n-1} has (n+1)/2 distinct values. For this to be 10, we'd need (n+1)/2 = 10, n = 19. Then T_2(x) = 2x²-1 permutes this set (since gcd(2,19)=1). But this gives only 1 quadratic (T_2 itself, or its iterates which aren't quadratic). Well, also -T_2 and shifts... hmm.

Actually, for the Chebyshev set S = {cos(2πk/19) : k = 0, ..., 9} (10 distinct real values), the quadratic 2x² - 1 permutes S. Are there other quadratics? 

Let me think more generally. The problem is asking for the maximum over all S, so we should find the best S.

Let me reconsider the structure. We want to maximize the number of quadratics permuting S. 

Let me think about what makes T_h affine-equivalent to S for many h.

Alternative approach: Think of the quadratics permuting S as follows. A quadratic f(z) = az² + bz + c permutes S. Consider the "critical point" h = -b/(2a). The map f can be written as f(z) = a(z-h)² + k. 

Now, here's a key structural observation: if f permutes S, consider the permutation σ of S induced by f. Since f is a quadratic (2-to-1 globally), and injective on S, the permutation σ is a bijection. 

Now, think about the functional graph: z → f(z) → f(f(z)) → ... Since S is finite, this eventually cycles. The cycle structure of σ on 10 elements.

But I don't think the cycle structure directly limits the count of quadratics.

Let me try yet another approach: direct construction and counting.

Let me consider S = R ∪ W where R = {r_1, ..., r_7} ⊂ ℝ and W = {w_1, w_2, w_3} ⊂ ℂ\ℝ.

For a quadratic f(z) = a(z-h)² + k to permute S:

Case A: f has real coefficients (a, h, k ∈ ℝ). Then f maps ℝ → ℝ and f(z̄) = f(z)̄. The 7 real elements are permuted among themselves (f maps real to real, and f(S) = S means the 7 real elements of S map to 7 real elements of S, since f(ℝ) ⊂ ℝ and there are exactly 7 real elements in S). Wait, f maps real elements of S to real numbers, which must be in S, so they're among the 7 real elements. So f permutes R. And f maps the 3 non-real elements to... f(w) for non-real w: f(w) ∈ S. f(w) could be real or non-real. But f(w̄) = f(w)̄. 

The 3 non-real elements: their conjugates. If w ∈ W and w̄ ∈ W, they form a conjugate pair. With 3 non-real elements, we have either 1 conjugate pair + 1 element whose conjugate is not in S, or 3 elements none of whose conjugates are in S (impossible to have all 3 in conjugate pairs since 3 is odd). So either:
- 1 conjugate pair and 1 "lonely" non-real element, or
- 0 conjugate pairs and 3 lonely non-real elements, or
- Actually we could have elements where w̄ = w (real), so non-real means w̄ ≠ w. With 3 non-real elements, the number in conjugate pairs is even (0 or 2), so 1 or 3 lonely.

If f has real coefficients and permutes S: f permutes R (7 real elements). f maps W to S. f(w) for w ∈ W: if w̄ ∈ W (conjugate pair), then f(w̄) = f(w)̄, so f(w) and f(w̄) are conjugates. If both f(w), f(w̄) ∈ S and they're conjugates, either both real (f(w) = f(w̄) ∈ ℝ, but then they're equal, contradicting injectivity unless w = w̄) or both non-real and conjugate pair in W. 

If w is lonely (w̄ ∉ S), then f(w) ∈ S and f(w̄) = f(w)̄ ∉ S (since f(w) ∈ S and if f(w)̄ ∈ S then... well f(w)̄ = f(w̄) and w̄ ∉ S so f(w̄) is not constrained). Actually f(w) ∈ S. Is f(w) real or non-real? If f(w) is real, fine. If f(w) is non-real, then f(w)̄ is its conjugate; is f(w)̄ ∈ S? Only if f(w) is part of a conjugate pair in S or lonely. f(w̄) = f(w)̄, and w̄ ∉ S, so f(w)̄ is not required to be in S. So f(w) can be any element of S (real or non-real).

But we need f to be a bijection on S. f permutes R (7 elements) and maps W (3 elements) to the remaining 3 elements of S not hit by R's images. Since f permutes R, the images of R are all of R. So the images of W must be exactly W. So f permutes W as well!

So for real-coefficient f: f permutes R (7 real elements) and permutes W (3 non-real elements) separately.

Now f|_R is a real quadratic permuting 7 real points, and f|_W is the same quadratic permuting 3 non-real points.

Case B: f has non-real coefficients. Then f doesn't preserve ℝ. The analysis is different.

This is getting quite involved. Let me try to think about it more cleverly, or consider specific constructions.

Let me think about the problem from the answer's perspective. This is likely a competition problem with a clean answer. Let me think about what N could be.

Let me consider the following construction. Take S = {0, 1, -1, 2, -2, 3, -3} ∪ {i, -i, 2i} or something. Hmm, let me think more carefully.

Actually, let me think about the problem differently. Let me consider quadratics of the form f(z) = z² + c (so h = 0, a = 1). For f to permute S, we need:
1. No two elements of S are negatives of each other (injectivity: z_i + z_j = 0 means z_i = -z_j, and 2h = 0).
2. {z² + c : z ∈ S} = S, i.e., {z² : z ∈ S} = S - c.

So {z² : z ∈ S} must be a translate of S.

Similarly, f(z) = a(z-h)² + k: {a(z-h)² : z ∈ S} = S - k.

Let me think about sets S where {z² : z ∈ S} is a translate of S. 

If S = {roots of z^10 = something}... roots of unity: {z : z^10 = 1}. Then z² ranges over {z : z^10 = 1} if gcd(2,10) = 1, but gcd(2,10) = 2, so z² ranges over {z : z^5 = 1}, which has 5 elements, not 10. So that doesn't work directly.

What about S being a union of two sets related by squaring?

Let me think about S = A ∪ B where A = {z² : z ∈ S} - c for some c. Hmm.

Let me try a very different approach. Let me think about the problem as follows:

We want to count quadratics f(z) = az² + bz + c (a ≠ 0) with f(S) = S. Each such f is a permutation of S. 

Consider the map Φ: (a,b,c) ↦ f. The condition f(S) = S means f permutes S. 

Now, a key idea: if f and g are two quadratics permuting S, then g⁻¹ ∘ f is a permutation of S (not necessarily a polynomial). The quadratics permuting S form a subset of the symmetric group Sym(S).

Let me think about upper bounds. How many quadratics can permute a 10-element set?

Each quadratic is determined by (a, b, c) with a ≠ 0, i.e., 3 complex parameters = 6 real parameters. The condition f(S) = S is very restrictive.

Given h (the critical point), the quadratic is f(z) = a(z-h)² + k. For f to permute S, we need the injectivity condition on h and the affine-equivalence condition. The injectivity condition rules out finitely many h values (midpoints of pairs). The affine-equivalence condition is the main constraint.

Let me think about how many h can make T_h = {(z-h)² : z ∈ S} affine-equivalent to S.

T_h is a set of 10 points. As h varies, T_h varies. The condition that T_h is affine-equivalent to S is a strong algebraic condition on h.

Let me think about invariants. If T_h = aS + k, then certain affine invariants of T_h and S must match. For instance, consider the "second difference" or cross-ratio type invariants.

Actually, here's a cleaner way to think: T_h = aS + k means there's a bijection π: S → S such that (z - h)² = a·π(z) + k for all z ∈ S. Wait, that's not quite right since T_h is a set, not an ordered thing. Let me write: there's a permutation σ of S such that for each z ∈ S, (σ(z) - h)²... no. Let me write: there exists a permutation σ of S and constants a, k such that for all z ∈ S:

f(z) = a(z - h)² + k = σ(z)

where σ is a permutation of S. So f(z) = σ(z) for all z ∈ S, meaning the quadratic f agrees with the permutation σ on S. Since f is degree 2 and we have 10 points, f is the unique degree ≤ 9 polynomial interpolating σ on S, but it happens to be degree 2. So σ must be such that the interpolating polynomial of (z, σ(z)) for z ∈ S has degree exactly 2.

So the count is: the number of permutations σ of S such that the Lagrange interpolating polynomial of σ through S has degree 2 (i.e., is a quadratic).

Equivalently, σ is a permutation of S such that σ(z) = az² + bz + c for some a ≠ 0, for all z ∈ S.

This is equivalent to: the permutation σ, viewed as a function on S, extends to a quadratic polynomial.

Now, the number of such permutations. We need az² + bz + c to take 10 distinct values on S (which it does iff injective, i.e., no pair sums to -b/a = 2h) and those values are exactly S.

Let me think about this combinatorially. We have 10 points. A quadratic az² + bz + c is determined by 3 parameters (a,b,c). Given a, b, c, the values on S are determined. We need these to be a permutation of S.

Alternatively: pick 3 points z_1, z_2, z_3 ∈ S and their images σ(z_1), σ(z_2), σ(z_3) ∈ S (distinct). This determines a, b, c (if the z_i are distinct, which they are). Then check if this quadratic permutes S. The number of quadratics permuting S is at most C(10,3) × P(10,3) / (overcounting), but really it's the number of (a,b,c) that work, which is what we want.

But this doesn't directly help. Let me think about specific constructions.

Construction idea: Let me use a set S that is a union of orbits under a quadratic map.

Consider f(z) = z² - 2. This is related to Chebyshev: if z = 2cos(θ), then z² - 2 = 4cos²(θ) - 2 = 2(2cos²(θ) - 1) = 2cos(2θ). So f(2cos(θ)) = 2cos(2θ). The map θ ↦ 2θ on angles.

If S = {2cos(2πk/11) : k = 0, 1, ..., 9}, these are 10 distinct real values (since 11 is prime, cos(2πk/11) for k=0,...,10 gives 11 values, but cos(2πk/11) = cos(2π(11-k)/11), so k and 11-k give the same value. k=0 gives 2, k=1,...,5 give 5 values, k=6,...,10 mirror. So distinct values: k=0,1,2,3,4,5 → 6 distinct values. That's only 6, not 10.

Hmm. Let me reconsider. For n points 2cos(2πk/n), the number of distinct values is ⌈n/2⌉ + 1 or similar. For 10 distinct values, I'd need n around 19 or 20.

For n = 19 (prime): {2cos(2πk/19) : k = 0, 1, ..., 18}. Distinct values: k and 19-k give same, so k=0,1,...,9 → 10 distinct values. And f(z) = z² - 2 maps 2cos(2πk/19) ↦ 2cos(4πk/19) = 2cos(2π(2k)/19). Since gcd(2,19) = 1, the map k ↦ 2k mod 19 permutes {0,...,18}, and the cos identification means it permutes the 10 distinct values. So f(z) = z² - 2 permutes S = {2cos(2πk/19) : k = 0,...,9}.

But this S is all real (10 real values). We need 7 real and 3 non-real. So this exact construction doesn't work, but it's a starting point.

Now, for this all-real S, how many quadratics permute it? f(z) = z² - 2 is one. Are there others?

The affine symmetries of S = {2cos(2πk/19) : k=0,...,9}: S is a subset of [-2, 2]. The affine maps preserving S: identity, and possibly z ↦ -z (since cos(2πk/19) and -cos(2πk/19) = cos(π - 2πk/19)... hmm, -2cos(2πk/19) = 2cos(π - 2πk/19) = 2cos(2π(19/2 - k)/19), but 19/2 is not integer, so this doesn't map to another element of S in general). Actually, -z maps 2cos(2πk/19) to -2cos(2πk/19) = 2cos(2πk/19 + π)... this isn't of the form 2cos(2πj/19) unless π = 2πj/19 - 2πk/19, i.e., 1/2 = (j-k)/19, which has no integer solution. So -z doesn't preserve S. So AffSym(S) is likely trivial (just identity) for this set.

Hmm, so this gives just 1 quadratic. Not great for maximizing.

Let me think differently. To maximize the number of quadratics, we want S to have lots of structure.

Key realization: Let me think about what sets have many quadratic self-maps.

If S is an arithmetic progression on the real line, say S = {0, 1, 2, ..., 9}, then a quadratic f(x) = ax² + bx + c permutes S. The quadratic takes integer values on integers 0-9 and permutes them. How many such quadratics are there? This is a finite counting problem. For a quadratic to permute {0,...,9}, it must be injective on this set (no two sum to -b/a) and map onto {0,...,9}. 

Actually, for {0, 1, ..., n-1}, quadratics permuting this set: the critical point h = -b/(2a) must not be a half-integer midpoint of any pair. Pairs (i,j) with i+j = 2h, so 2h must not be any integer from 1 to 2n-3 (sum of two distinct elements). For {0,...,9}, sums range from 1 to 17, so 2h ∉ {1,...,17}, i.e., h ∉ {0.5, 1, 1.5, ..., 8.5}. So h must be outside [0.5, 8.5] or... wait, h can be any value not equal to a half-integer midpoint. The midpoints are {(i+j)/2 : 0 ≤ i < j ≤ 9} = {0.5, 1, 1.5, ..., 8.5}. So h ∉ {0.5, 1, 1.5, ..., 8.5}.

But we also need f(S) = S. For an arithmetic progression, this is quite restrictive. I doubt many quadratics work. Let me not pursue this.

Let me think about the problem from a higher level. 

The answer is likely a specific number. Let me think about what structures give many quadratics.

Important insight: Consider the group of affine transformations that preserve S. If S has a large affine symmetry group, and there are several h values making T_h affine-equivalent to S, the count multiplies.

But with 7 real and 3 non-real, the affine symmetry group is limited. An affine map z ↦ az + k preserving S must map the 7 real points among themselves (or to non-real). If a, k are real, it preserves ℝ, so maps real to real. The 7 real points must be preserved as a set, and the 3 non-real as a set.

For the 7 real points to have affine symmetry, they could form an arithmetic progression: {r, r+d, ..., r+6d}, which has affine symmetry z ↦ -z + 2r + 6d (reflection) and identity. So |AffSym(R)| = 2 if R is an AP.

For the 3 non-real points to have affine symmetry: 3 points in the plane. An affine map preserving 3 non-collinear points is the identity (3 non-collinear points determine the affine map). If they're collinear, there could be a reflection. If the 3 non-real points are collinear (on a line in ℂ), say an AP on some line, then reflection gives |AffSym(W)| = 2.

But the affine symmetry of S must simultaneously preserve R and W. If R is an AP on ℝ and W is an AP on some line, the affine map preserving both must preserve ℝ (since R ⊂ ℝ with ≥ 2 points determines the real line) and preserve the line containing W. An affine map preserving ℝ is z ↦ az + k with a, k ∈ ℝ (or a ∈ ℝ, k ∈ ℝ). Wait, z ↦ az + k preserves ℝ iff a, k ∈ ℝ. Then it maps the line containing W to a parallel line (or the same line). For it to preserve W (3 points on a line), the line must be preserved or mapped to a parallel line containing W. If W is on a line not parallel to ℝ (i.e., not horizontal), then a real affine map z ↦ az + k (a,k ∈ ℝ) maps this line to a parallel line (shifted by real amounts), which won't be the same line unless the line is horizontal (parallel to ℝ). 

Hmm, this is getting complicated. Let me try to think about the problem more cleverly.

Let me reconsider. Maybe I should think about specific small examples and build up.

Let me consider the simplest structure: S symmetric about a point.

If S is symmetric about h₀ (i.e., z ∈ S iff 2h₀ - z ∈ S), then h₀ is a midpoint of many pairs, so h₀ is NOT a valid critical point (injectivity fails). But other h values might work.

Let me think about the problem from the perspective of the answer. Competition problems of this type... Let me think about what N could be.

Actually, let me reconsider the structure. We have 10 points, 7 real, 3 non-real. Let me think about the non-real points.

3 non-real points: w₁, w₂, w₃. For a quadratic f(z) = a(z-h)² + k permuting S:

If f has real coefficients (h, a, k ∈ ℝ): f permutes R (7 real) and W (3 non-real) separately, as shown above. f|_R is a real quadratic permuting 7 real points, f|_W is the same quadratic permuting 3 non-real points.

If f has non-real coefficients: f mixes real and non-real points.

Let me focus on real-coefficient quadratics first.

For f|_R (real quadratic permuting 7 real points): A real quadratic x ↦ a(x-h)² + k permuting 7 real points. The critical point h must not be a midpoint of any pair in R. And {a(x-h)² + k : x ∈ R} = R.

For 7 real points, how many real quadratics permute them? This depends on the structure of R.

For f|_W (same quadratic permuting 3 non-real points): {a(w-h)² + k : w ∈ W} = W.

So we need a single quadratic that permutes both R and W.

Let me think about 3 non-real points and a quadratic permuting them. 3 points, quadratic (2-to-1). For injectivity on 3 points, no two sum to 2h. For the quadratic to permute 3 points, it's a permutation of 3 elements, which is either identity, a transposition, or a 3-cycle. But a quadratic can't be the identity on 3 distinct points (a quadratic is determined by 3 points, and if it's identity on 3 points, it's the identity polynomial z, which is degree 1, not 2). So f|_W is either a transposition or a 3-cycle.

If f|_W is a transposition (swaps 2, fixes 1): f(w_i) = w_i for some i, and f(w_j) = w_k, f(w_k) = w_j. f fixes w_i means a(w_i - h)² + k = w_i. And f swaps w_j, w_k.

If f|_W is a 3-cycle: f(w_1) = w_2, f(w_2) = w_3, f(w_3) = w_1.

Now, for the same f to permute R (7 real points): f|_R is a permutation of 7 elements. The cycle structure must be compatible with f being a quadratic.

This is getting very involved. Let me try to think about the problem from a cleaner angle.

Let me reconsider: maybe the answer involves thinking about this as a group action problem.

The set of quadratics permuting S: each is z ↦ a(z-h)² + k. Let me think about the "center" h. 

Claim: The centers h of quadratics permuting S are related to the structure of S.

Let me think about a specific nice construction.

Construction: Let S = {0, ±1, ±2, ±3} ∪ {w₁, w₂, w₃} where the real part is symmetric about 0.

R = {-3, -2, -1, 0, 1, 2, 3} (7 real points, symmetric about 0).

For a real quadratic f(x) = a(x-h)² + k permuting R:
- h ≠ midpoint of any pair in R. Midpoints of pairs in R: (i+j)/2 for -3 ≤ i < j ≤ 3. These include 0, ±0.5, ±1, ±1.5, ±2, ±2.5. So h ∉ {0, ±0.5, ±1, ±1.5, ±2, ±2.5}.
- {a(x-h)² + k : x ∈ R} = R.

Since R = {-3,-2,-1,0,1,2,3} is symmetric about 0, the map x ↦ a(x-h)² + k sends x and 2h-x to the same value. For injectivity, no two elements of R sum to 2h. The sums of pairs in R range from -5 to 5 (specifically: -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, and half-integers). 2h must avoid all these.

For f to permute R = {-3,...,3}: the set {a(x-h)² + k : x ∈ R} must equal {-3,...,3}. 

The values a(x-h)² for x ∈ R are a·{(x-h)² : x ∈ R}. Since (x-h)² = (h-x)², and R is symmetric about 0, if h = 0, then (x)² = x² and {x² : x ∈ R} = {0, 1, 4, 9} — only 4 distinct values, not 7. So h = 0 doesn't give injectivity (since x and -x map to same value), and indeed 0 is a midpoint.

Let me try h not symmetric. Say h = 3 (outside R). Then (x-3)² for x ∈ {-3,...,3}: (−6)², (−5)², (−4)², (−3)², (−2)², (−1)², 0² = 36, 25, 16, 9, 4, 1, 0. These are 7 distinct values {0, 1, 4, 9, 16, 25, 36}. We need a·{0,1,4,9,16,25,36} + k = {-3,-2,-1,0,1,2,3}. So a·{0,1,4,9,16,25,36} + k must be 7 consecutive integers. But {0,1,4,9,16,25,36} are not in arithmetic progression, so no affine map makes them consecutive integers. So h = 3 doesn't work.

Hmm. So for R = {-3,...,3}, it's hard to find real quadratics permuting R. Let me think about what 7-point real sets admit quadratic self-maps.

A real quadratic x ↦ ax² + bx + c permuting a finite real set R of size 7. The quadratic is a parabola. For it to permute R, it must be injective on R (so the axis of symmetry h = -b/(2a) is not a midpoint of any pair in R) and map R onto R.

Since the parabola opens up or down, and R is on the real line, the quadratic maps R to R. The image of R under the quadratic is a set of 7 real numbers (since a, b, c real and R ⊂ ℝ). For this to equal R, the quadratic permutes R.

On the real line, a quadratic is decreasing then increasing (or vice versa), with minimum (or maximum) at h. For x < h, it's monotone; for x > h, it's monotone. So on R, if h is not in R and h separates R into two groups, the quadratic is monotone on each group.

For the quadratic to permute R (a set of 7 real numbers), think of R as sorted: r_1 < r_2 < ... < r_7. If h is between r_k and r_{k+1}, then the quadratic is monotone on {r_1,...,r_k} and monotone on {r_{k+1},...,r_7}. The images of the left group are monotone (say decreasing if parabola opens up), and images of the right group are monotone (increasing). The combined image must be R.

This is like a "shuffle" of two monotone sequences. The number of such shuffles that give a permutation of R is limited.

This is related to the concept of "quadratic permutations" of finite sets. Let me think about specific cases.

For R = {r_1, ..., r_7} and quadratic f permuting R with critical point h between r_k and r_{k+1}:

f is decreasing on {r_1,...,r_k} and increasing on {r_{k+1},...,r_7} (assuming a > 0). So f(r_1) > f(r_2) > ... > f(r_k) and f(r_{k+1}) < f(r_{k+2}) < ... < f(r_7). The image is {f(r_1),...,f(r_k)} ∪ {f(r_{k+1}),...,f(r_7)} = R, and these are 7 distinct values forming R = {r_1 < ... < r_7}.

The minimum of f is at h, so f(r_k) and f(r_{k+1}) are the two smallest images (closest to h). Actually f(r_k) ≥ f(h) and f(r_{k+1}) ≥ f(h), and these are the two closest to the minimum. If a > 0, the minimum value is f(h) = k, and the images increase away from h.

For the image to be R = {r_1,...,r_7}: the smallest image is min(f(r_k), f(r_{k+1})) which should be r_1, and the largest is max(f(r_1), f(r_7)) which should be r_7.

This is getting complicated. Let me try to think about the problem from a completely different angle.

Let me reconsider the problem. Maybe I should think about it in terms of the number of "quadratic permutations" of a set with 7 real and 3 non-real elements, and find the maximum.

Let me think about upper bounds first. 

Upper bound approach: Each quadratic permuting S is determined by its action on any 3 points of S (since 3 points determine a quadratic). But the quadratic must permute S, so it's a permutation of S that happens to be quadratic. The number of permutations of S that are quadratic is what we want.

A quadratic is determined by (a, b, c) with a ≠ 0. Given 3 points z₁, z₂, z₃ ∈ S and their images w₁, w₂, w₃ ∈ S (distinct), there's a unique quadratic (if z₁, z₂, z₃ are distinct, which they are). So the number of quadratics permuting S is at most the number of injective maps from 3 points of S to S such that the resulting quadratic permutes S. But this overcounts since each quadratic is counted C(10,3) times (once for each choice of 3 points). So:

# quadratics = (# triples (z₁,z₂,z₃, σ(z₁),σ(z₂),σ(z₃)) giving a permuting quadratic) / C(10,3)

This doesn't directly give an upper bound. Let me think differently.

Upper bound via critical points: Each quadratic has a unique critical point h. Different quadratics permuting S could share the same h (if there are multiple (a,k) for that h). For a given h, the number of (a,k) making f permute S is at most |AffSym(S)| (as discussed). And the number of valid h is... hard to bound directly.

Let me try to think about this more concretely with a specific construction.

Let me try S = {0, 1, 4, 9, 16, 25, 36} ∪ {w₁, w₂, w₃} where the real part is {0, 1, 4, 9, 16, 25, 36} = {k² : k = 0,...,6}.

Then f(z) = z + c (affine, not quadratic) or... hmm, {z² : z ∈ R} where R = {0,1,...,6} gives {0,1,4,9,16,25,36}. But we need quadratics permuting S, not affine maps.

Let me try: R = {0, 1, 4, 9, 16, 25, 36} and f(z) = (z - h)² + k. If h = 0, f(z) = z² + k, and f(R) = {0, 1, 16, 81, 256, ...} + k, which is not R. So that doesn't work.

OK let me try yet another approach. Let me think about the Chebyshev construction but modified for 7 real + 3 non-real.

Chebyshev: T₂(x) = 2x² - 1. If x = cos(θ), T₂(x) = cos(2θ). 

Consider S = {cos(2πk/n) : k = 0, ..., m} for appropriate n, m. But we need 7 real and 3 non-real.

What if we use a complex version? Consider z ↦ z² on a set that includes both real and non-real elements.

Let me think about the map z ↦ z² on a set S. If S is closed under z ↦ z² (up to the set being preserved), and S has 7 real and 3 non-real elements.

z ↦ z²: real numbers map to real (non-negative). Non-real numbers map to non-real (unless purely imaginary, mapping to negative real).

For S to be preserved by z ↦ z²: the 7 real elements must map to real elements of S, and the 3 non-real must map to elements of S.

Real elements: if r ∈ R ⊂ ℝ, r² ∈ ℝ. For r² ∈ S, r² must be in R (since it's real). So z ↦ z² permutes R. But z ↦ z² on real numbers: r and -r map to the same value. For injectivity, R can't contain both r and -r (unless r = 0). So R has at most one of each {r, -r} pair, plus possibly 0.

If R = {0, 1, 4, 9, 16, 25, 36} (all non-negative, no ±pairs), then z ↦ z² maps 0→0, 1→1, 4→16, 9→81, ... 81 ∉ R. So this doesn't permute R.

For z ↦ z² to permute R ⊂ ℝ: we need R to be closed under squaring and the squaring to be a bijection on R. Since squaring on ℝ is not injective (except on ℝ≥0 or ℝ≤0), R must be in ℝ≥0 or ℝ≤0. Say R ⊂ ℝ≥0. Then z ↦ z² is injective on R iff no two elements are negatives (which is automatic for ℝ≥0 except 0). Actually on ℝ≥0, z ↦ z² is injective. For it to permute R, we need {r² : r ∈ R} = R. So R is closed under squaring and square-rooting (within R). 

For a finite set R ⊂ ℝ≥0 closed under squaring: if r ∈ R, then r², r⁴, r⁸, ... ∈ R. Since R is finite, this sequence must cycle: r^(2^k) = r for some k. So r^(2^k - 1) = 1, meaning r = 0 or r is a (2^k - 1)-th root of unity. For real r ≥ 0, r = 0 or r = 1. So R ⊂ {0, 1} for real non-negative! That gives at most 2 real elements. Not enough for 7.

So z ↦ z² can't permute 7 real points. We need a different quadratic.

Let me go back to the Chebyshev idea. T₂(x) = 2x² - 1 permutes {cos(2πk/n) : k = 0, ..., ⌊n/2⌋} when n is odd. For 7 real points, we need ⌊n/2⌋ + 1 = 7, so n = 13 (⌊13/2⌋ = 6, +1 = 7). So R = {cos(2πk/13) : k = 0, 1, ..., 6} has 7 elements, and T₂(x) = 2x² - 1 permutes R (since gcd(2,13) = 1).

Now, T₂(x) = 2x² - 1 has critical point h = 0, a = 2, k = -1. The injectivity condition: no two elements of R sum to 0. R = {cos(2πk/13) : k = 0,...,6}. cos(2πk/13) + cos(2πj/13) = 0 iff cos(2πk/13) = -cos(2πj/13) = cos(π - 2πj/13) = cos(2π(13/2 - j)/13). Since 13/2 is not integer, this doesn't give another element of R. Actually, cos(2πk/13) = -cos(2πj/13) iff 2πk/13 = π - 2πj/13 + 2πm, i.e., 2k/13 = 1 - 2j/13 + 2m, i.e., 2k + 2j = 13 + 26m, i.e., 2(k+j) = 13(1 + 2m). LHS is even, RHS is odd. No solution. So no two elements of R sum to 0. Good, injectivity holds.

So T₂(x) = 2x² - 1 permutes R = {cos(2πk/13) : k = 0,...,6}. Now I need to add 3 non-real elements W = {w₁, w₂, w₃} such that T₂ also permutes W, and possibly other quadratics also permute S = R ∪ W.

T₂(z) = 2z² - 1 permutes W: {2w² - 1 : w ∈ W} = W. So W is closed under z ↦ 2z² - 1. For 3 elements, the map z ↦ 2z² - 1 must be a permutation of W (bijection). As discussed, it's either a transposition or a 3-cycle.

If it's a 3-cycle: w₁ ↦ w₂ ↦ w₃ ↦ w₁. Then 2w₁² - 1 = w₂, 2w₂² - 1 = w₃, 2w₃² - 1 = w₁. These are 3 equations. The w's are non-real.

If it's a transposition: say w₁ ↦ w₁ (fixed) and w₂ ↔ w₃. Then 2w₁² - 1 = w₁, so 2w₁² - w₁ - 1 = 0, (2w₁ + 1)(w₁ - 1) = 0, w₁ = 1 or w₁ = -1/2. Both real! So w₁ can't be non-real if it's fixed. So the transposition case with a fixed point doesn't work for non-real W (the fixed point would be real).

Wait, unless the fixed point is real and in R. But we said f permutes R and W separately (for real coefficients). If w₁ is fixed and real, it's in R, not W. So for W (all non-real), the transposition case requires the fixed point to be in W, but fixed points of T₂ are 1 and -1/2 (both real). So transposition doesn't work for non-real W.

So T₂ must act as a 3-cycle on W. We need non-real w₁, w₂, w₃ with 2w₁² - 1 = w₂, 2w₂² - 1 = w₃, 2w₃² - 1 = w₁.

This means w₁ is a periodic point of T₂ with period 3 (or period dividing 3, but period 1 gives real, period 3 gives the 3-cycle). The period-3 points of T₂(z) = 2z² - 1 are solutions of T₂³(z) = z, i.e., 2(2(2z²-1)²-1)² - 1 = z. This is a degree 8 polynomial. The fixed points (period 1) are z = 1 and z = -1/2. So period-3 points satisfy T₂³(z) = z but not T₂(z) = z. The degree 8 polynomial T₂³(z) - z = 0 has 8 roots. Two are the fixed points. The remaining 6 are period-3 points (forming two 3-cycles, since each 3-cycle has 3 elements). 

Are these period-3 points real or non-real? T₂ maps [-1,1] to [-1,1]. The Chebyshev dynamics on [-1,1]: T₂(cos θ) = cos 2θ. Period-3 points: cos(2³θ) = cos(θ), so 8θ = ±θ + 2πk. 8θ = θ + 2πk → 7θ = 2πk → θ = 2πk/7. 8θ = -θ + 2πk → 9θ = 2πk → θ = 2πk/9.

For θ = 2πk/7: cos(2πk/7) for k = 0,...,6. k=0 gives 1 (fixed point). k=1,...,6: cos(2πk/7), and cos(2πk/7) = cos(2π(7-k)/7), so distinct values: k=0,1,2,3 → 4 values. But k=0 is the fixed point 1. So 3 distinct non-trivial values: cos(2π/7), cos(4π/7), cos(6π/7). These are all real! And they form a 3-cycle under T₂ (since k ↦ 2k mod 7 permutes {1,2,3,4,5,6} and the cos identification pairs k with 7-k, so the 3-cycle is on {1,2,3} ↔ {6,5,4}).

Wait, so the period-3 points from θ = 2πk/7 are real. What about θ = 2πk/9? cos(2πk/9) for k = 0,...,8. k=0 gives 1 (fixed). The map k ↦ 2k mod 9: 1→2→4→8→7→5→1 (6-cycle) and 3→6→3 (2-cycle) and 0→0. So cos(2πk/9) for k=1,2,4,8,7,5 form a 6-cycle (period 6 under T₂), and k=3,6 form a 2-cycle (period 2). So θ = 2πk/9 gives period 6 and period 2 points, not period 3.

Hmm wait, I need to be more careful. T₂(cos θ) = cos(2θ). T₂^n(cos θ) = cos(2^n θ). Period n means cos(2^n θ) = cos(θ), i.e., 2^n θ ≡ ±θ (mod 2π).

For period 3: 8θ ≡ ±θ (mod 2π).
- 8θ ≡ θ: 7θ ≡ 0 (mod 2π), θ = 2πk/7. Period divides 3, and since 7 is prime and doesn't divide 2^d - 1 for d < 3 (2^1-1=1, 2^2-1=3, neither divisible by 7), the period is exactly 3. So these are genuine period-3 points. They're cos(2πk/7), all real.
- 8θ ≡ -θ: 9θ ≡ 0 (mod 2π), θ = 2πk/9. Period divides 3. 2^1+1=3, 2^2+1=5, 2^3+1=9. So 9 | 2^3+1, and 9 doesn't divide 2^d+1 for d < 3 (3 doesn't divide 2^1+1=3... wait 3 | 3. So θ = 2π/3 gives period 1? cos(2π/3) = -1/2, and T₂(-1/2) = 2(1/4)-1 = -1/2. Yes, -1/2 is a fixed point! So θ = 2πk/9 with 9θ = 2πk, and we need to check which give period 3 vs period 1.

The fixed points are θ = 0 (cos 0 = 1) and θ = 2π/3 (cos(2π/3) = -1/2). θ = 2πk/9: k=0 → θ=0 (fixed), k=3 → θ=2π/3 (fixed). The others: k=1,2,4,5,7,8. k=1: θ=2π/9, k=2: θ=4π/9, k=4: θ=8π/9, k=5: θ=10π/9, k=7: θ=14π/9, k=8: θ=16π/9. Under k ↦ 2k mod 9 (for the +case) or k ↦ -2k mod 9 (for the -case)... 

Actually, the dynamics: T₂(cos θ) = cos(2θ). The map on θ is θ ↦ 2θ (mod 2π), but with the identification θ ~ -θ (since cos). So the dynamics on θ ∈ [0,π] is θ ↦ 2θ if 2θ ≤ π, θ ↦ 2π - 2θ if 2θ > π. This is the "tent map" or "doubling map" on [0,π].

For period 3 under this map: the orbit of θ under the doubling map (mod the identification) has period 3.

From the 7θ = 2πk analysis: θ = 2πk/7, k=1,2,3 (up to identification k ~ 7-k). These give 3 real period-3 points forming one 3-cycle.

From the 9θ = 2πk analysis: θ = 2πk/9, k=1,2,4,5,7,8 (excluding k=0,3 which are fixed). Under the doubling map: 1→2→4→8→7→5→1 (mod 9), but with identification k ~ 9-k: 1~8, 2~7, 4~5. So the orbit: 1→2→4→8~1, so 1→2→4→1, a 3-cycle! Similarly 5→1, 7→2, etc. So {1,2,4} (identified with {8,7,5}) form a 3-cycle. cos(2π/9), cos(4π/9), cos(8π/9) — all real.

So ALL period-3 points of T₂ are real! There are 6 period-3 points (two 3-cycles), all real: {cos(2π/7), cos(4π/7), cos(6π/7)} and {cos(2π/9), cos(4π/9), cos(8π/9)}.

Wait, but T₂³(z) - z is degree 8, with 2 fixed points and 6 period-3 points. All 8 roots are real? Let me verify: the 8 roots are cos(2πk/7) for k=0,...,6 (7 values, but k=0 is the fixed point 1) and... no wait. Let me recount.

T₂³(z) - z = 0 has degree 8. The roots are z such that T₂³(z) = z. These include:
- Fixed points: T₂(z) = z, i.e., 2z² - z - 1 = 0, z = 1, -1/2. (2 roots)
- Period-3 points: T₂³(z) = z but T₂(z) ≠ z. (6 roots)

From the Chebyshev analysis, the period-3 points are cos(2πk/7) for k=1,...,6 (but cos(2πk/7) = cos(2π(7-k)/7), so 3 distinct values) and cos(2πk/9) for k=1,2,4,5,7,8 (but with identification, 3 distinct values). So 3 + 3 = 6 period-3 points, all real.

So T₂³(z) - z has all 8 roots real: {1, -1/2, cos(2π/7), cos(4π/7), cos(6π/7), cos(2π/9), cos(4π/9), cos(8π/9)}.

This means T₂ has NO non-real period-3 points! So we can't find 3 non-real points forming a 3-cycle under T₂.

Hmm. So the Chebyshev approach with T₂ doesn't directly give us non-real 3-cycles.

But wait — we don't have to use T₂. We can use any quadratic. And the 3 non-real points don't have to be in a single 3-cycle under the same quadratic that permutes R. We could have different quadratics permuting S, some of which act differently on R and W.

Let me reconsider. We want to MAXIMIZE the number of quadratics permuting S. We get to choose S (7 real, 3 non-real) and count all quadratics (real or complex coefficients) permuting S.

Let me think about this more broadly. Let me consider quadratics with complex (non-real) coefficients too.

For a quadratic f(z) = a(z-h)² + k with non-real h (or non-real a, k), f doesn't preserve ℝ. So f can map real elements to non-real and vice versa.

Let me think about the problem differently. Let me consider the set of all quadratics permuting S. Each is z ↦ a(z-h)² + k. The critical point h can be real or non-real.

For f to permute S (10 elements, injective on S): no two elements of S sum to 2h. The "forbidden" values of 2h are {z_i + z_j : i < j}, which are C(10,2) = 45 values. So h avoids 45 values in ℂ. The valid h are all of ℂ except these 45 values (and we need the affine-equivalence condition).

Now, the affine-equivalence condition: T_h = {(z-h)² : z ∈ S} must be an affine image of S. This is a very strong condition. Let me think about how many h can satisfy it.

T_h = aS + k means: there's a permutation σ of S with (z-h)² = aσ(z) + k for all z ∈ S. So for each z ∈ S, (z-h)² = aσ(z) + k. This gives 10 equations. The unknowns are a, k, h, and the permutation σ. Given σ (a permutation of S), we have 10 equations (z-h)² = aσ(z) + k in 3 unknowns (a, k, h). For a generic σ, this is overdetermined (10 equations, 3 unknowns) and has no solution. For special σ, it might have a solution.

Given σ, the equations are: (z_i - h)² = a·σ(z_i) + k for i = 1,...,10. Expanding: z_i² - 2hz_i + h² = a·σ(z_i) + k. So z_i² - 2hz_i + h² - a·σ(z_i) - k = 0 for all i. This means the quadratic polynomial z² - 2hz + h² - a·σ(z) - k vanishes on S... but σ(z) is only defined on S, not as a polynomial. 

Let me think of it as: the polynomial P(z) = z² - 2hz + (h² - k) agrees with a·σ(z) on S. So σ(z) = (z² - 2hz + h² - k)/a = (1/a)z² - (2h/a)z + (h²-k)/a on S. So σ is the restriction of a quadratic to S. This is just saying f(z) = az² + bz + c with a = 1 (wait, I'm confusing myself).

Let me restart the parametrization. f(z) = Az² + Bz + C (A ≠ 0) permutes S. f(z) = A(z - h)² + K where h = -B/(2A), K = C - B²/(4A). The condition is f(S) = S (as sets, i.e., f is a bijection on S).

So the count is: number of (A, B, C) with A ≠ 0 such that f(z) = Az² + Bz + C permutes S.

Equivalently: number of permutations σ of S such that σ(z) = Az² + Bz + C for some A ≠ 0, for all z ∈ S. I.e., σ extends to a quadratic polynomial.

Given a permutation σ of S, when does it extend to a quadratic? The interpolating polynomial of σ through S has degree ≤ 9. It's a quadratic iff the degree is exactly 2 (or less, but degree 1 or 0 can't give a bijection on 10 points). So we need the interpolating polynomial to have degree 2.

The interpolating polynomial has degree ≤ 2 iff the third and higher divided differences are 0. Equivalently, σ(z) = Az² + Bz + C on S.

So the count is the number of permutations of S that are "quadratic permutations" (extend to degree-2 polynomials).

Now, let me think about this combinatorially. A quadratic Az² + Bz + C is determined by 3 parameters. Given 3 points of S and their images, the quadratic is determined. For it to permute S, the remaining 7 points must also map to S.

So: pick 3 points z₁, z₂, z₃ ∈ S and 3 distinct images w₁, w₂, w₃ ∈ S. This determines a quadratic f. Check if f permutes S. The number of quadratics permuting S equals the number of such (z₁,z₂,z₃,w₁,w₂,w₃) that work, divided by C(10,3) (since each quadratic is counted once for each choice of 3 points from S, and the images are determined).

Wait, actually each quadratic permuting S is counted C(10,3) times (once for each 3-element subset of S, with the images being f of those 3 points). So:

# quadratics = (# valid 6-tuples) / C(10,3)

But this is hard to compute directly. Let me think about upper bounds.

Upper bound: The number of quadratics permuting S is at most the number of triples (z₁, z₂, z₃, w₁, w₂, w₃) with z's distinct in S, w's distinct in S, divided by C(10,3). The total number of such triples is C(10,3) × P(10,3) = C(10,3) × 10·9·8. So the upper bound is P(10,3) = 720. But this is a very loose bound.

Better upper bound: For each choice of (z₁, w₁) (10 × 10 = 100 choices, but w₁ ≠ z₁ for a non-identity permutation, or w₁ = z₁), the quadratic is not determined. We need 3 points. 

Hmm, let me think about it differently. Let me think about the critical point h.

For each valid h (not a midpoint of any pair in S), the quadratic f(z) = A(z-h)² + K permutes S iff {A(z-h)² + K : z ∈ S} = S, i.e., {A(z-h)² : z ∈ S} = S - K. Let T_h = {(z-h)² : z ∈ S} (a set of 10 distinct values since h is valid). We need T_h to be an affine image of S: T_h = (1/A)(S - K) = S/A - K/A. So T_h and S are affine-equivalent.

The number of affine maps taking T_h to S is the number of (A, K) with A·T_h + K = S, which is |AffSym(S)| (if T_h ≅ S affinely) or 0.

So # quadratics = |AffSym(S)| × #{valid h : T_h ≅ S affinely}.

Now I need to figure out:
1. |AffSym(S)| for the best S.
2. The number of valid h with T_h ≅ S.

Let me think about AffSym(S). S has 7 real and 3 non-real points. An affine map z ↦ αz + β preserving S. 

If α, β ∈ ℝ: the map preserves ℝ, so it maps R (7 real) to R and W (3 non-real) to W. It's an affine self-map of R (7 real points) and of W (3 non-real points) simultaneously.

If α, β ∉ ℝ (or one of them): the map doesn't preserve ℝ, so it can mix real and non-real points.

For maximizing |AffSym(S)|, we want S to have affine symmetries. But the 7+3 split (7 real, 3 non-real) is constraining.

Case 1: α, β ∈ ℝ. AffSym_ℝ(S) = {z ↦ αz + β : α, β ∈ ℝ, αR + β = R, αW + β = W}.
- αR + β = R: R is a 7-point set on ℝ. Affine symmetries of 7 points on a line. If R is an arithmetic progression {r, r+d, ..., r+6d}, the affine symmetries are z ↦ z (identity) and z ↦ -z + 2r + 6d (reflection). So |AffSym(R)| = 2.
- αW + β = W: W is 3 non-real points. For a real affine map to preserve W, W must be on a line stable under real affine maps. z ↦ αz + β with α, β ∈ ℝ maps a point x+iy to (αx+β) + i(αy). So the imaginary parts are scaled by α. For W = {w₁, w₂, w₃} to be preserved, the imaginary parts of w₁, w₂, w₃ must be scaled by α and the real parts by α then shifted by β. 

If W is an arithmetic progression on a horizontal line (all same imaginary part): W = {x₁+iy, x₂+iy, x₃+iy} with x₁, x₂, x₃ in AP. Then z ↦ αz + β maps to {(αx_i+β) + iαy}. For this to equal W, we need αy = y (so α = 1, since y ≠ 0) and {αx_i + β} = {x₁, x₂, x₃}. With α = 1, {x_i + β} = {x_i}, so β = 0. So only the identity. Alternatively, α = -1 (reflection): then imaginary parts become -y, so W must also have points with imaginary part -y. But W has all points with imaginary part y (same horizontal line), so -y ≠ y (since y ≠ 0), contradiction. So if W is on a horizontal line, only identity preserves it (among real affine maps). Unless W is symmetric about a real point: W = {x-iy, x₀+iy, x+iy}... no, that's not on one horizontal line.

Hmm, let me reconsider. If W = {w₁, w₂, w₃} and we want z ↦ -z + β (reflection, α = -1) to preserve W: -w_i + β ∈ W for all i. So W is symmetric about β/2. If W = {β/2 + u, β/2 + v, β/2 - u} (symmetric about β/2, with v being the center), then -w_i + β = β/2 - u, β/2 - v, β/2 + u. For this to equal W, we need β/2 - v = β/2 + v, so v = 0, meaning w₂ = β/2 (the center is in W). And W = {β/2 + u, β/2, β/2 - u}. If β/2 is real, then w₂ is real, contradicting W being non-real. If β/2 is non-real, then the reflection z ↦ -z + β has β non-real, so it's not a real affine map. 

So for real affine maps (α, β ∈ ℝ), the reflection z ↦ -z + β (β ∈ ℝ) preserves W only if W is symmetric about a real point β/2, with the center β/2 ∈ W. But β/2 ∈ ℝ, so W would contain a real point, contradiction. So no non-trivial real affine map preserves W (if W has no real points and the map has α = -1).

What about α = 1, β ≠ 0? Then z ↦ z + β (translation by real β). This preserves W iff W + β = W, i.e., W is invariant under translation by β. For a finite set, this requires β = 0. So only identity.

What about other α? For |α| ≠ 1, the map scales distances. For a finite set to be preserved, we'd need the set to be scale-invariant, which for 3 points means they're in geometric progression or similar. But with the constraint that α is real and the map preserves W (non-real points), and also preserves R...

This is getting very complicated. Let me step back and think about whether |AffSym(S)| can be > 1 for a good choice of S, and whether non-real affine symmetries are possible.

Case 2: Non-real affine maps. z ↦ αz + β with α or β non-real. This maps ℝ to a line in ℂ (not ℝ unless α, β ∈ ℝ). So real points of S map to non-real points (generally). For the map to preserve S (7 real, 3 non-real), some real points must map to non-real and some non-real to real. If r real points map to non-real and s non-real map to real, then 7 - r + s = 7 (real count in image) and 3 - s + r = 3 (non-real count). So r = s. And r ≤ 7, s ≤ 3, so r = s ≤ 3.

So a non-real affine symmetry maps r ≤ 3 real points to non-real positions and r non-real points to real positions. The remaining 7 - r real points stay real, and 3 - r non-real points stay non-real.

For r = 3: all 3 non-real points map to real, and 3 real points map to non-real. The 4 remaining real points stay real. This is possible in principle.

This is very flexible and hard to analyze in general. Let me try to think about the problem from the answer side.

Let me consider the possibility that the answer is related to a specific number. Let me think about what kinds of sets S could have many quadratic self-maps.

Alternative approach: Let me think about the problem in terms of the functional structure.

A quadratic f(z) = Az² + Bz + C permuting S. The key constraint is that f is 2-to-1 (generically), and on S it's 1-to-1 (bijective). The "folding" of the quadratic must not identify any two points of S.

Let me think about the problem for small cases and see if there's a pattern.

For |S| = n with all real, the number of real quadratics permuting S is related to the structure. For the Chebyshev set {cos(2πk/(2n-1)) : k=0,...,n-1} (n points, with 2n-1 prime), T₂ permutes it, giving 1 quadratic. But maybe other quadratics also work.

Hmm, let me think about this differently. Let me consider the problem as maximizing over S, and think about what S gives the most quadratics.

Let me consider S = R ∪ W where R is chosen to have many quadratic self-maps and W is chosen to be compatible.

For R (7 real points), the maximum number of real quadratics permuting R: Let me think about this. A real quadratic permuting 7 real points. The critical point h splits R into two groups (left and right of h), and the quadratic is monotone on each. The image is a "merge" of two monotone sequences.

For 7 points, the number of such "quadratic permutations" depends on the specific set R. For a set like an arithmetic progression, there might be several.

Actually, let me think about the arithmetic progression R = {0, 1, 2, 3, 4, 5, 6}. A quadratic f(x) = Ax² + Bx + C permuting R. The critical point h = -B/(2A) must not be a midpoint of any pair in R. Midpoints of pairs in {0,...,6}: {(i+j)/2 : 0 ≤ i < j ≤ 6} = {0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5}. So h ∉ {0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5}.

For f to permute {0,...,6}: f takes 7 distinct values on {0,...,6} and these must be {0,...,6}. 

The sum of f(0) + f(1) + ... + f(6) = A(0+1+4+9+16+25+36) + B(0+1+2+3+4+5+6) + 7C = 91A + 21B + 7C. This must equal 0+1+2+...+6 = 21. So 91A + 21B + 7C = 21, i.e., 13A + 3B + C = 3.

Also, f(i) ∈ {0,...,6} for each i, and f is a bijection. This is a strong constraint. Let me just try to find all quadratics permuting {0,...,6}.

This is a finite problem. Let me think about it. The quadratic f(x) = Ax² + Bx + C with f({0,...,6}) = {0,...,6}.

Since f is a bijection on {0,...,6}, and f is a quadratic (parabola), the graph of f on {0,...,6} is a permutation that's "V-shaped" or "Λ-shaped" (decreasing then increasing, or increasing then decreasing).

For A > 0 (upward parabola, V-shaped): f decreases on (-∞, h) and increases on (h, ∞). On {0,...,6}, if h is between k and k+1, f is decreasing on {0,...,k} and increasing on {k+1,...,6}. The minimum is near h. The image values: f(k) and f(k+1) are the two smallest (closest to the minimum). The largest values are f(0) and f(6) (the endpoints).

For the image to be {0,...,6}: the minimum value is 0 (achieved at the point closest to h) and the maximum is 6 (achieved at one of the endpoints). 

Actually, the minimum of f on {0,...,6} is min(f(k), f(k+1)) (the two points closest to h). This must be 0. The maximum is max(f(0), f(6)), which must be 6.

This is getting complicated. Let me just try small cases computationally in my head... or better, let me think about the problem structure.

Actually, I realize I should think about this problem more cleverly. Let me reconsider.

The key formula: # quadratics permuting S = |AffSym(S)| × #{valid h : T_h ≅ S affinely}.

To maximize this, we want both |AffSym(S)| and #{valid h} to be large.

Let me think about #{valid h : T_h ≅ S}. T_h = {(z-h)² : z ∈ S}. For T_h to be affine-equivalent to S, there must be a permutation σ of S with (z-h)² = ασ(z) + β for some α, β. This means z² - 2hz + h² = ασ(z) + β, so σ(z) = (z² - 2hz + h² - β)/α = (1/α)z² - (2h/α)z + (h²-β)/α. So σ is a quadratic function of z (with leading coefficient 1/α, linear coefficient -2h/α). 

So σ(z) = Az² + Bz + C where A = 1/α, B = -2h/α, C = (h²-β)/α. And h = -B/(2A), which is consistent (h is the critical point of f(z) = Az² + Bz + C... wait, f(z) = Az² + Bz + C and h = -B/(2A). Yes.)

So the number of valid h is the number of distinct critical points h among all quadratic permutations of S. And the total count is:

# quadratics = sum over valid h of (number of quadratics with critical point h permuting S)

= sum over valid h of |AffSym(S)| [if T_h ≅ S]

Wait, I derived earlier that for each valid h with T_h ≅ S, the number of (A,K) is |AffSym(S)|. But actually, the number of affine maps from T_h to S is |AffSym(T_h)| = |AffSym(S)| (since T_h ≅ S). But each such affine map gives a distinct quadratic f(z) = A(z-h)² + K. And different h give different quadratics (different critical points). So:

# quadratics = |AffSym(S)| × #{valid h : T_h ≅ S affinely}

But wait, I need to double-check: could two different h give the same quadratic? No, because h = -B/(2A) is uniquely determined by the quadratic. So different h ⟹ different quadratics. And for the same h, different (A,K) give different quadratics. So the formula holds.

Now, #{valid h : T_h ≅ S} is the number of distinct critical points of quadratic permutations of S. Each quadratic permutation has a unique critical point, and for each critical point h, there are |AffSym(S)| quadratics. So:

# quadratics = |AffSym(S)| × (# distinct critical points)

And # distinct critical points = # quadratics / |AffSym(S)|, which is circular. Let me re-derive.

Let Q = set of quadratics permuting S. |Q| = N.
Let H = set of critical points of quadratics in Q. |H| = number of distinct h.
For each h ∈ H, the number of quadratics with critical point h is the number of (A,K) with A·T_h + K = S, which is |AffSym(S)| (if T_h ≅ S).

So N = |H| × |AffSym(S)|.

Now I need to find max over S of |H| × |AffSym(S)|.

Let me think about |H|. H is the set of h such that T_h = {(z-h)² : z ∈ S} is affine-equivalent to S and h is not a midpoint of any pair in S.

T_h ≅ S means there's a permutation σ of S with σ(z) = (z² - 2hz + h² - β)/α, i.e., σ is a quadratic in z with specific coefficients related to h. The leading coefficient is 1/α (free), the linear coefficient is -2h/α = -2h · (leading coeff). So given the leading coefficient A = 1/α, the linear coefficient is B = -2hA, so h = -B/(2A). And C = (h² - β)/α = A(h² - β), so β = h² - C/A.

So for each quadratic permutation σ(z) = Az² + Bz + C of S, the critical point is h = -B/(2A). The number of distinct h is |H|.

Now, |H| is the number of distinct values of -B/(2A) among all quadratic permutations Az² + Bz + C of S.

Hmm, this is still complex. Let me try to think about specific constructions and compute.

Let me try a concrete approach. Let me consider S with specific structure and count.

Construction 1: S = R ∪ W where R = {cos(2πk/13) : k = 0,...,6} (7 real Chebyshev points) and W = {3 non-real points}.

For R, T₂(z) = 2z² - 1 permutes R. The critical point of T₂ is h = 0. Are there other quadratics permuting R?

For the Chebyshev set R = {cos(2πk/13) : k = 0,...,6}, the quadratics permuting R: T₂(z) = 2z² - 1 is one. Are there others?

The affine symmetries of R: R = {cos(2πk/13) : k=0,...,6}. Is there a non-trivial affine map preserving R? R ⊂ [-1, 1]. The map z ↦ -z: -cos(2πk/13) = cos(π - 2πk/13) = cos(2π(13/2 - k)/13). Since 13/2 is not an integer, this is not of the form cos(2πj/13) for integer j. So -z doesn't preserve R. So |AffSym(R)| = 1.

So for R alone, the quadratics permuting R: T₂ is one (h = 0). Are there others? 

Let me think... for the Chebyshev set, the only quadratic self-map is T₂ (up to affine conjugation). Actually, I think for the set {cos(2πk/p) : k = 0,...,(p-1)/2} with p prime, the only polynomial self-maps of degree d with gcd(d, p) = 1 are the Chebyshev T_d. But we're looking at all quadratics, not just Chebyshev. 

Hmm, but a quadratic permuting this set doesn't have to be a Chebyshev polynomial. It could be any quadratic that happens to permute the set. Let me think about whether there are others.

For R = {cos(2πk/13) : k = 0,...,6}, a quadratic f(z) = Az² + Bz + C permuting R. We need f(cos(2πk/13)) ∈ R for k = 0,...,6, and f is a bijection on R.

Using the Chebyshev identity: cos(2θ) = 2cos²(θ) - 1. So T₂(cos θ) = cos(2θ). A general quadratic Az² + Bz + C applied to cos(θ) gives A·cos²(θ) + B·cos(θ) + C = (A/2)(1 + cos(2θ)) + B·cos(θ) + C = (A/2)cos(2θ) + B·cos(θ) + (A/2 + C).

For this to be in R = {cos(2πk/13) : k = 0,...,6} for all θ = 2πk/13, we need (A/2)cos(2θ) + B·cos(θ) + (A/2 + C) ∈ R for all θ = 2πk/13, k = 0,...,6.

This is a linear combination of cos(2θ), cos(θ), and 1, evaluated at θ = 2πk/13. For this to always be in R (a specific finite set), the coefficients must be very special.

If B = 0: f(cos θ) = (A/2)cos(2θ) + (A/2 + C). This is an affine function of cos(2θ). Since cos(2θ) ranges over {cos(4πk/13) : k = 0,...,6} = R (because the map k ↦ 2k mod 13 permutes {0,...,12} and cos identifies k with 13-k, so {cos(4πk/13) : k=0,...,6} = {cos(2πj/13) : j = 0,...,6} = R). So f(cos θ) = (A/2)·(element of R) + (A/2 + C). For f to permute R, we need (A/2)·R + (A/2 + C) = R, i.e., R is invariant under the affine map z ↦ (A/2)z + (A/2 + C). Since |AffSym(R)| = 1 (only identity), we need A/2 = 1 and A/2 + C = 0, so A = 2, C = -1. This gives f(z) = 2z² - 1 = T₂(z). 

If B ≠ 0: f(cos θ) = (A/2)cos(2θ) + B·cos(θ) + (A/2 + C). This involves both cos(2θ) and cos(θ). For θ = 2πk/13, cos(θ) and cos(2θ) are both in R, but their linear combination being in R for all k is very restrictive. I believe the only solution is B = 0 (giving T₂), but I'm not 100% sure. Let me think about whether B ≠ 0 could work.

For k = 0: cos(0) = 1, cos(0) = 1. f(1) = A + B + C. This must be in R.
For k = 1: cos(2π/13), cos(4π/13). f(cos(2π/13)) = (A/2)cos(4π/13) + B·cos(2π/13) + (A/2 + C). Must be in R.

This gives a system where f maps 7 points to 7 points in R. With 3 free parameters (A, B, C) and 7 constraints (each f value in R), it's overdetermined. The only solution is likely T₂ (B = 0, A = 2, C = -1).

Actually, I realize there might be other solutions. Let me think about it differently. The quadratic f permutes R, so it's a permutation of 7 elements that extends to a quadratic. The number of such permutations is what we want for R alone.

For the Chebyshev set, I believe the only quadratic permutation is T₂. But let me consider other sets R.

Let me try R = {0, 1, 2, 3, 4, 5, 6} (arithmetic progression). Let me find all quadratics permuting R.

f(x) = Ax² + Bx + C permuting {0,1,2,3,4,5,6}. 

Conditions:
- f(i) ∈ {0,...,6} for i = 0,...,6
- f is injective on {0,...,6}
- f({0,...,6}) = {0,...,6}

The sum condition: Σf(i) = 21, giving 13A + 3B + C = 3 (derived earlier, wait let me recheck: Σf(i) = A·Σi² + B·Σi + 7C = A·91 + B·21 + 7C = 21. So 91A + 21B + 7C = 21, divide by 7: 13A + 3B + C = 3.)

Also, Σf(i)² = Σi² = 91. Σf(i)² = Σ(Ai² + Bi + C)² = Σ(A²i⁴ + 2ABi³ + (B² + 2AC)i² + 2BCi + C²) = A²·Σi⁴ + 2AB·Σi³ + (B²+2AC)·Σi² + 2BC·Σi + 7C².

Σi⁴ for i=0..6 = 0+1+16+81+256+625+1296 = 2275.
Σi³ = (6·7/2)² = 441.
Σi² = 91.
Σi = 21.

So Σf(i)² = 2275A² + 882AB + 91(B²+2AC) + 42BC + 7C² = 91.

And Σf(i)³ = Σi³ = 441. This gives another equation. And so on.

This system of equations (power sums) determines the possible (A, B, C). With enough equations, we can solve.

From 13A + 3B + C = 3 (first power sum).
From the second power sum: 2275A² + 882AB + 91B² + 182AC + 42BC + 7C² = 91.

Let me substitute C = 3 - 13A - 3B:

Second equation: 2275A² + 882AB + 91B² + 182A(3-13A-3B) + 42B(3-13A-3B) + 7(3-13A-3B)² = 91.

Let me expand:
182A(3-13A-3B) = 546A - 2366A² - 546AB
42B(3-13A-3B) = 126B - 546AB - 126B²
7(3-13A-3B)² = 7(9 - 78A - 18B + 169A² + 78AB + 9B²) = 63 - 546A - 126B + 1183A² + 546AB + 63B²

Sum: 2275A² + 882AB + 91B² + 546A - 2366A² - 546AB + 126B - 546AB - 126B² + 63 - 546A - 126B + 1183A² + 546AB + 63B²

A² terms: 2275 - 2366 + 1183 = 1092
AB terms: 882 - 546 - 546 + 546 = 336
B² terms: 91 - 126 + 63 = 28
A terms: 546 - 546 = 0
B terms: 126 - 126 = 0
Constant: 63

So: 1092A² + 336AB + 28B² + 63 = 91
→ 1092A² + 336AB + 28B² = 28
→ 39A² + 12AB + B² = 1
→ (3A + B)² + 30A² = 1... let me check: (3A+B)² = 9A² + 6AB + B². So 39A² + 12AB + B² = (9A² + 6AB + B²) + 30A² + 6AB = (3A+B)² + 6A(5A + B). Hmm, that doesn't simplify nicely.

Let me try: 39A² + 12AB + B² = 1. This is a quadratic in B: B² + 12AB + 39A² - 1 = 0. B = (-12A ± √(144A² - 4(39A² - 1)))/2 = (-12A ± √(144A² - 156A² + 4))/2 = (-12A ± √(4 - 12A²))/2 = -6A ± √(1 - 3A²).

For B to be real, 1 - 3A² ≥ 0, so |A| ≤ 1/√3.

Now I also need the third power sum: Σf(i)³ = 441. And higher power sums. Each gives another equation, further constraining A, B, C.

This is getting very computational. Let me try a different approach.

Let me think about the problem more cleverly. 

I think the key insight might be related to the following: a quadratic f(z) = a(z-h)² + k permuting S. The map z ↦ (z-h)² "folds" the plane about h. For f to permute S, the folded set T_h must be affine-equivalent to S.

Let me think about the problem in terms of the "folding" structure. The 10 points of S are folded about h: points equidistant from h (on opposite sides) map to the same value. Since f is injective on S, no two points of S are symmetric about h. The folded set T_h has 10 distinct points, and these must form an affine copy of S.

Now, here's a key structural observation: the map z ↦ (z-h)² sends z and 2h-z to the same value. So T_h "identifies" pairs symmetric about h. But since no two points of S are symmetric about h, T_h has 10 distinct points. However, the structure of T_h is constrained: it's the image of S under a 2-to-1 map (with no collisions on S).

Let me think about the real and non-real structure. 

Let me consider h real. Then (z-h)² for real z is real and non-negative. For non-real z = x+iy, (z-h)² = (x-h)² - y² + 2i(x-h)y. 

If h is real:
- Real elements r ∈ R: (r-h)² ∈ ℝ≥0. So T_h contains 7 non-negative real values from R.
- Non-real elements w = x+iy ∈ W: (w-h)² = (x-h)² - y² + 2i(x-h)y. This is real iff x = h (i.e., w is directly above/below h), otherwise non-real.

For T_h to be affine-equivalent to S (7 real, 3 non-real): T_h must have 7 real and 3 non-real points (up to affine transformation). But an affine transformation z ↦ αz + β can change the real/non-real split. If α, β ∈ ℝ, the split is preserved. If α or β is non-real, the split changes.

Case: T_h affine-equivalent to S via a real affine map (α, β ∈ ℝ). Then T_h has 7 real and 3 non-real points. T_h has 7 non-negative real values (from R) and 3 values from W. The 3 values from W: (w_j - h)² for j = 1,2,3. For T_h to have exactly 7 real and 3 non-real: the 7 values from R are real (✓), and the 3 values from W must be non-real. (w_j - h)² is non-real iff Re(w_j) ≠ h. So we need Re(w_j) ≠ h for all j. If any Re(w_j) = h, then (w_j - h)² is real, and T_h would have 8+ real values, not matching 7.

Alternatively, if some (w_j - h)² is real and some (r_i - h)² ... no, all (r_i - h)² are real. So T_h has 7 real (from R) + (number of w_j with Re(w_j) = h) real values. For T_h to have 7 real (matching S via real affine map), we need all 3 (w_j - h)² to be non-real, i.e., Re(w_j) ≠ h for all j.

OK so with h real and Re(w_j) ≠ h for all j, T_h has 7 real (from R, all ≥ 0) and 3 non-real (from W). For T_h to be a real affine image of S: T_h = αS + β with α, β ∈ ℝ. Then:
- The 7 real values of T_h (= {(r-h)² : r ∈ R}) must be α · (7 real values of S) + β = αR + β.
- The 3 non-real values of T_h (= {(w-h)² : w ∈ W}) must be αW + β.

So {(r-h)² : r ∈ R} = αR + β and {(w-h)² : w ∈ W} = αW + β, with the same α, β.

The first condition: the set of squared distances from h to the real points, {(r-h)²}, is an affine image of R. The second: {(w-h)²} is the same affine image of W.

This is a strong condition. Let me think about what R and W satisfy this.

For the first condition with R = {cos(2πk/13) : k=0,...,6} and h = 0: {(r-0)² : r ∈ R} = {cos²(2πk/13) : k=0,...,6} = {(1+cos(4πk/13))/2 : k=0,...,6} = {1/2 + cos(4πk/13)/2 : k=0,...,6}. Since k ↦ 2k mod 13 permutes and cos identifies, {cos(4πk/13) : k=0,...,6} = R. So {(r)² : r ∈ R} = {1/2 + r/2 : r ∈ R} = (1/2)R + 1/2. So α = 1/2, β = 1/2. ✓ (This is just T₂(z) = 2z² - 1 rearranged: (z-0)² = (1/2)(2z²-1) + 1/2, so T_h = (1/2)·T₂(S) + 1/2... hmm, let me recheck. T₂(r) = 2r² - 1, so r² = (T₂(r) + 1)/2. Since T₂ permutes R, {r² : r ∈ R} = {(T₂(r)+1)/2 : r ∈ R} = {(s+1)/2 : s ∈ R} = R/2 + 1/2. Yes, α = 1/2, β = 1/2.)

Now the second condition: {(w-h)² : w ∈ W} = {w² : w ∈ W} = (        — AI历史解题过程（thinking）
#   polymath_01263         — 题目ID

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
  <problem_id>polymath_01263</problem_id>
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

Let $S = \{z_1, z_2, \dots, z_{10}\}$ be a set consisting of 10 distinct complex numbers, among which exactly 7 are real numbers. Let $N$ be the maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$. Find $N$.

## Standard Solution

The problem is equivalent to the original proof-based problem for $n=10$. The solution shows that for $n \ge 9$, since there are exactly 3 imaginary numbers in $S$ and $n-3$ real numbers, $f$ must be a real-coefficient polynomial. This implies that $f$ must map the set of imaginary numbers to itself. By considering the permutations of the three imaginary numbers and the property that $f$ is real, the solution concludes there are at most two such quadratic polynomials. Specifically, the cases show that either one or two such polynomials can exist depending on whether conjugates are present in the set of imaginary numbers.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. It's a math problem, no tools needed. Let me think carefully.

We have S = {z_1, ..., z_10}, 10 distinct complex numbers, exactly 7 real. We want the maximum possible number of quadratic polynomials f(z) with complex coefficients such that f(S) = S (as a set).

A quadratic polynomial f(z) = az² + bz + c with a ≠ 0. We want f to permute the set S, i.e., f(S) = S as sets.

First, let me think about the structure. A quadratic polynomial is a 2-to-1 map generically. For f(S) = S with |S| = 10, we need f to map S to S. Since f is a function (not necessarily injective on S), but f(S) = S means every element of S is hit.

Actually, let me think about this more carefully. f is a quadratic, so it's at most 2-to-1. For f(S) = S, we need f restricted to S to be a surjection onto S. Since |S| = 10 and f is at most 2-to-1, the number of elements in S mapping to each element of S is at most 2, and the total count is 10 (elements of S) mapping to 10 elements (S), so on average 1 preimage per element. So some elements have 1 preimage and some have 2, but the total must be 10. If k elements have 2 preimages and the rest have 1, then 2k + (10-k) = 10, so k = 0. So f is actually a bijection (permutation) on S!

Wait, that's only if every element of S is in the image and we count preimages within S. Let me reconsider. f(S) = S means f maps S onto S. The image f(S) has at most 10 elements (could be fewer if not injective). For f(S) = S we need |f(S)| = 10, which means f is injective on S (since |S| = 10 and f(S) ⊆ S with |f(S)| = 10 = |S|). So f restricted to S is a bijection/permutation.

So f permutes S. A quadratic polynomial that permutes a finite set.

Now, a quadratic f(z) = az² + bz + c. We can conjugate: f(z) = a(z + b/(2a))² + (c - b²/(4a)). So up to affine change of variables, f is z ↦ z² (scaled). Actually f(z) = a(z - h)² + k where h = -b/(2a), k = c - b²/(4a).

So f(z) = a(z-h)² + k. The "center" is h, and f is symmetric about h: f(h + w) = f(h - w) = aw² + k.

For f to be injective on S, no two elements of S can be symmetric about h (i.e., sum to 2h), unless they're the same element.

Actually, f is injective on S means: for any two distinct z_i, z_j in S, f(z_i) ≠ f(z_j). Since f(z_i) = f(z_j) iff a(z_i - h)² = a(z_j - h)² iff (z_i - h)² = (z_j - h)² iff z_i - h = ±(z_j - h), i.e., z_i = z_j or z_i + z_j = 2h.

So f is injective on S iff no two distinct elements of S sum to 2h. (Equivalently, h is not the midpoint of any pair in S, and also no element equals h... wait, if z_i = h, then z_i - h = 0, and we'd need another element with (z_j - h)² = 0, i.e., z_j = h, but elements are distinct so only one. So that's fine.)

So the condition for f to be a permutation of S is:
1. a ≠ 0
2. No two distinct elements of S sum to 2h (where h = -b/(2a))
3. f(S) = S, i.e., {a(z_i - h)² + k : i = 1..10} = S.

Condition 3 is the hard one. Given h satisfying condition 2, we need a, k such that the map z ↦ a(z-h)² + k permutes S.

Let me think of it differently. Let's fix h. Define the map φ_h: z ↦ (z - h)². This maps S to a multiset of 10 values (all distinct by condition 2). Then f(z) = a·φ_h(z) + k. We need a·φ_h(S) + k = S as sets, i.e., the set {(z_i - h)²} when scaled by a and translated by k gives S.

So we need: there exist a, k such that a·T + k = S where T = {(z_i - h)² : i = 1..10} (a set of 10 distinct complex numbers).

This means T and S are related by an affine map: S = aT + k. Equivalently, T = (S - k)/a, i.e., T is an affine image of S.

So the question becomes: for how many values of h (with the injectivity condition) is the set {(z - h)² : z ∈ S} an affine image of S?

Hmm, this is getting complex. Let me think about the structure of S with 7 real and 3 non-real elements.

The 3 non-real elements: since complex conjugation... well, S is just a set, no symmetry required. But let me think about what constraints the real/non-real split gives.

If z is real and h is real, then (z-h)² is real. If z is non-real and h is real, (z-h)² is non-real (unless z-h is purely imaginary, giving real). Hmm.

Let me think about this more carefully. Let's denote the real elements as r_1, ..., r_7 and non-real as w_1, w_2, w_3.

Case 1: h is real.
Then (r_i - h)² is real for all i. (w_j - h)²: w_j = x_j + iy_j, so (w_j - h)² = (x_j - h)² - y_j² + 2i(x_j - h)y_j. This is real iff x_j = h (i.e., w_j - h is purely imaginary), otherwise non-real.

For T = aS + k... wait, we need T to be an affine image of S, meaning T has the same "shape" as S up to scaling and translation. S has 7 real and 3 non-real. T = {(z-h)²}. 

If h is real: the real elements of S map to real values in T. The non-real elements w_j map to (w_j - h)² which is real iff Re(w_j) = h, non-real otherwise.

For T to be an affine image of S (with a, k complex), the number of real elements in T must match the structure... actually, an affine map z ↦ az + k with complex a, k can send real numbers to non-real and vice versa. So the real/non-real split isn't directly preserved unless a, k are real.

Hmm, this is quite involved. Let me think about whether there's a cleaner approach.

Actually, let me reconsider. The problem asks for the maximum N over all choices of S (with 7 real, 3 non-real). So we get to choose S to maximize the count of quadratic polynomials permuting S.

Let me think about what sets S can have many quadratic self-maps.

Key insight: A quadratic f(z) = a(z-h)² + k permutes S iff:
- h avoids being a midpoint of any pair in S (injectivity)
- The set {(z-h)² : z ∈ S} = (S - k)/a, i.e., is an affine image of S.

Let me think about small cases or symmetric configurations.

Consider S being closed under some quadratic map. 

Let me think about the structure differently. Suppose f(z) = a(z-h)² + k permutes S. Then f is a permutation of the 10 elements. As a permutation, it has some cycle structure. 

Also, consider: if f permutes S, what about iterating f? f², f³, etc. are degree 4, 8, ... polynomials, not quadratic, so they don't count.

But here's a thought: if f and g are both quadratics permuting S, then f∘g is degree 4, not quadratic (unless one is affine, but quadratics have degree exactly 2). So the set of quadratics permuting S doesn't form a group under composition.

Let me think about the problem from the perspective of counting valid h values.

For each valid h (satisfying injectivity), we need {(z-h)² : z ∈ S} to be an affine image of S. The affine image condition: two sets of 10 points are affine-equivalent. Given the set T_h = {(z-h)²}, we need T_h = aS + k for some a ≠ 0, k.

Two sets being affine equivalent is a strong condition. Given S, how many h make T_h affine-equivalent to S?

Let me think about this using the structure of S. Let me consider specific configurations.

Approach: Think about S that is invariant under z ↦ z² (or a scaled version). 

Classic example: roots of unity. If S consists of roots of z^n = 1, then z ↦ z² permutes S (when gcd(2,n) = 1, i.e., n odd). But these are on the unit circle, not 7 real + 3 non-real.

Let me think about Chebyshev-like or special configurations.

Actually, let me think about the real line structure. 7 real points. A quadratic with real coefficients maps real to real. If f has real coefficients (a, b, c real, so h, k real), then f maps real numbers to real numbers and respects conjugation: f(z̄) = f(z)̄.

For f with real coefficients permuting S (7 real, 3 non-real): the 3 non-real elements must be permuted among themselves (since f preserves "realness" only if... wait, f(z̄) = f(z)̄ means if z is non-real, f(z) is non-real iff f(z) ≠ f(z)̄, which happens unless f(z) is real. Actually f maps non-real to non-real or real. Hmm, f(z̄) = f(z)̄, so if z is non-real, f(z) could be real or non-real.

But we need f to permute S, and S has exactly 3 non-real elements. If f has real coefficients, f(conj(z)) = conj(f(z)). The non-real elements of S come in conjugate pairs or are self-conjugate (real). With 3 non-real elements, they can't all be in conjugate pairs (3 is odd). So at least one non-real element w has conj(w) ∉ S.

If f has real coefficients and w ∈ S is non-real with conj(w) ∉ S, then f(w) ∈ S and conj(f(w)) = f(conj(w)). But conj(w) ∉ S, so f(conj(w)) is not constrained to be in S. However, f(w) ∈ S. If f(w) is non-real, then conj(f(w)) ∈ S iff f(w)'s conjugate is in S. This is getting complicated.

Let me try a different, more computational approach. Let me think about what configurations allow many quadratics.

Let me consider the possibility that S is constructed to have several quadratic self-maps. 

Think about it this way: a quadratic f(z) = a(z-h)² + k is determined by (a, h, k) with a ≠ 0. The condition f(S) = S gives 10 equations (f maps S onto S) but really it's a permutation condition. Given h (with injectivity), a and k are determined by where any 2 points go... actually, given h, the set T_h = {(z-h)²} is determined. We need T_h = (S-k)/a, so a and k are determined by matching T_h to S up to affine transformation. Two 10-point sets are affine equivalent in at most... well, if T_h and S are affine equivalent, the affine map is essentially unique (determined by 2 points, and the rest must match). So for each h, there's at most one (a,k) pair (up to the matching). Actually, there could be multiple if S has affine symmetries.

So the count of quadratics permuting S is roughly the number of h values such that T_h is affine-equivalent to S, times the number of affine self-maps of S (affine symmetries).

Hmm wait. Let me re-examine. For a given h, T_h = {(z-h)² : z ∈ S}. We need T_h = σ(S) for some affine map σ(z) = az + k. The number of such (a,k) is the number of affine maps σ such that σ(S) = T_h. If S has affine symmetry group G (affine maps preserving S), then if one σ works, the number of working σ is |G|. But each σ gives a distinct quadratic f. So the count is: (number of h with injectivity and T_h affine-equivalent to S) × |G| / ... no wait, it's not that simple because different h could give the same f.

Actually, each quadratic f corresponds to a unique h (the center h = -b/(2a)). So different h give different f. And for a fixed h, different (a,k) give different f. So the total count is:

N = sum over valid h of (number of (a,k) with a{(z-h)² : z∈S} + k = S).

For a fixed h, the number of (a,k) is the number of affine maps taking T_h to S, which equals |AffSym(S)| if T_h is affine-equivalent to S, and 0 otherwise. Wait no: the number of affine maps σ with σ(T_h) = S. If T_h is affine-equivalent to S, then the set of such σ is a coset of AffSym(S) (the affine self-maps of S... actually of T_h). Hmm, let me think again.

The number of affine maps σ(z) = az + k with σ(T_h) = S. If T_h and S are affine-equivalent, pick one σ_0 with σ_0(T_h) = S. Then all others are σ_0 ∘ τ where τ is an affine self-map of T_h. The affine self-maps of T_h correspond to affine self-maps of S (since they're affine-equivalent). So the count is |AffSym(T_h)| = |AffSym(S)|.

So N = |AffSym(S)| × (number of valid h such that T_h is affine-equivalent to S).

Where "valid h" means h is not a midpoint of any pair in S (injectivity condition), and T_h = {(z-h)² : z ∈ S} is affine-equivalent to S.

Now, |AffSym(S)|: the affine symmetry group of a 10-point set in the plane. For a generic set, this is trivial (just identity, |G| = 1). For special sets, it could be larger. But with 7 real and 3 non-real points, the symmetry is limited. The 3 non-real points can't form a symmetric configuration with the 7 real points easily.

Actually, affine symmetries of S: an affine map z ↦ az + k preserving S. It must map real elements to real elements or to non-real. Since there are 7 real and 3 non-real, an affine symmetry either preserves the real subset and non-real subset, or swaps some. But 7 ≠ 3, so it can't swap all. It could map some real to non-real and some non-real to real, but the counts must work out: if r real → non-real and s non-real → real, then 7 - r + s = 7 (real count preserved) and 3 - s + r = 3, giving r = s. And r ≤ 7, s ≤ 3, so r = s ≤ 3.

This is getting complicated. Let me try to think about specific constructions.

Let me try: S = {real points forming a nice set} ∪ {3 non-real points}.

Idea: Use a set on the real line that has a quadratic self-map, plus 3 non-real points that also work.

If all 10 points were real, the problem would be about real quadratics permuting a real set. With 7 real and 3 non-real, we need to handle the non-real ones.

Let me think about the all-real case first for intuition. If S ⊂ ℝ with |S| = 10, how many quadratics f(z) = a(z-h)² + k (with real a, h, k, or complex?) permute S? If we allow complex coefficients, f could map real points to non-real, which wouldn't be in S (all real). So f must map real to real, meaning a, h, k real (well, a(z-h)² must be real for real z, so a and h real, and k real). Actually if h is non-real, (z-h)² for real z is non-real, and a times that... we'd need a(z-h)² + k real for all z in S. That's very restrictive. Basically for all-real S, f must have real coefficients (roughly).

For real S with real quadratic f(z) = a(x-h)² + k permuting S ⊂ ℝ: this is a well-studied problem. The map x ↦ a(x-h)² + k is a "tent-map-like" or "logistic-map-like" permutation of a finite set.

Actually, for a real quadratic to permute a finite real set, the set must be very special. 

Let me think about the Chebyshev connection. The Chebyshev polynomial T_n(x) = cos(n arccos(x)) permutes certain sets. But T_n has degree n, not 2. However, T_2(x) = 2x² - 1 is quadratic! T_2 maps cos(θ) ↦ cos(2θ). So if S = {cos(2πk/n) : k = 0, ..., n-1} for appropriate n, then T_2 permutes S when gcd(2, n) = 1 (n odd) — but then |S| might be less than n due to cos symmetry (cos(θ) = cos(-θ)). 

For n odd, {cos(2πk/n) : k=0,...,n-1} has (n+1)/2 distinct values. For this to be 10, we'd need (n+1)/2 = 10, n = 19. Then T_2(x) = 2x²-1 permutes this set (since gcd(2,19)=1). But this gives only 1 quadratic (T_2 itself, or its iterates which aren't quadratic). Well, also -T_2 and shifts... hmm.

Actually, for the Chebyshev set S = {cos(2πk/19) : k = 0, ..., 9} (10 distinct real values), the quadratic 2x² - 1 permutes S. Are there other quadratics? 

Let me think more generally. The problem is asking for the maximum over all S, so we should find the best S.

Let me reconsider the structure. We want to maximize the number of quadratics permuting S. 

Let me think about what makes T_h affine-equivalent to S for many h.

Alternative approach: Think of the quadratics permuting S as follows. A quadratic f(z) = az² + bz + c permutes S. Consider the "critical point" h = -b/(2a). The map f can be written as f(z) = a(z-h)² + k. 

Now, here's a key structural observation: if f permutes S, consider the permutation σ of S induced by f. Since f is a quadratic (2-to-1 globally), and injective on S, the permutation σ is a bijection. 

Now, think about the functional graph: z → f(z) → f(f(z)) → ... Since S is finite, this eventually cycles. The cycle structure of σ on 10 elements.

But I don't think the cycle structure directly limits the count of quadratics.

Let me try yet another approach: direct construction and counting.

Let me consider S = R ∪ W where R = {r_1, ..., r_7} ⊂ ℝ and W = {w_1, w_2, w_3} ⊂ ℂ\ℝ.

For a quadratic f(z) = a(z-h)² + k to permute S:

Case A: f has real coefficients (a, h, k ∈ ℝ). Then f maps ℝ → ℝ and f(z̄) = f(z)̄. The 7 real elements are permuted among themselves (f maps real to real, and f(S) = S means the 7 real elements of S map to 7 real elements of S, since f(ℝ) ⊂ ℝ and there are exactly 7 real elements in S). Wait, f maps real elements of S to real numbers, which must be in S, so they're among the 7 real elements. So f permutes R. And f maps the 3 non-real elements to... f(w) for non-real w: f(w) ∈ S. f(w) could be real or non-real. But f(w̄) = f(w)̄. 

The 3 non-real elements: their conjugates. If w ∈ W and w̄ ∈ W, they form a conjugate pair. With 3 non-real elements, we have either 1 conjugate pair + 1 element whose conjugate is not in S, or 3 elements none of whose conjugates are in S (impossible to have all 3 in conjugate pairs since 3 is odd). So either:
- 1 conjugate pair and 1 "lonely" non-real element, or
- 0 conjugate pairs and 3 lonely non-real elements, or
- Actually we could have elements where w̄ = w (real), so non-real means w̄ ≠ w. With 3 non-real elements, the number in conjugate pairs is even (0 or 2), so 1 or 3 lonely.

If f has real coefficients and permutes S: f permutes R (7 real elements). f maps W to S. f(w) for w ∈ W: if w̄ ∈ W (conjugate pair), then f(w̄) = f(w)̄, so f(w) and f(w̄) are conjugates. If both f(w), f(w̄) ∈ S and they're conjugates, either both real (f(w) = f(w̄) ∈ ℝ, but then they're equal, contradicting injectivity unless w = w̄) or both non-real and conjugate pair in W. 

If w is lonely (w̄ ∉ S), then f(w) ∈ S and f(w̄) = f(w)̄ ∉ S (since f(w) ∈ S and if f(w)̄ ∈ S then... well f(w)̄ = f(w̄) and w̄ ∉ S so f(w̄) is not constrained). Actually f(w) ∈ S. Is f(w) real or non-real? If f(w) is real, fine. If f(w) is non-real, then f(w)̄ is its conjugate; is f(w)̄ ∈ S? Only if f(w) is part of a conjugate pair in S or lonely. f(w̄) = f(w)̄, and w̄ ∉ S, so f(w)̄ is not required to be in S. So f(w) can be any element of S (real or non-real).

But we need f to be a bijection on S. f permutes R (7 elements) and maps W (3 elements) to the remaining 3 elements of S not hit by R's images. Since f permutes R, the images of R are all of R. So the images of W must be exactly W. So f permutes W as well!

So for real-coefficient f: f permutes R (7 real elements) and permutes W (3 non-real elements) separately.

Now f|_R is a real quadratic permuting 7 real points, and f|_W is the same quadratic permuting 3 non-real points.

Case B: f has non-real coefficients. Then f doesn't preserve ℝ. The analysis is different.

This is getting quite involved. Let me try to think about it more cleverly, or consider specific constructions.

Let me think about the problem from the answer's perspective. This is likely a competition problem with a clean answer. Let me think about what N could be.

Let me consider the following construction. Take S = {0, 1, -1, 2, -2, 3, -3} ∪ {i, -i, 2i} or something. Hmm, let me think more carefully.

Actually, let me think about the problem differently. Let me consider quadratics of the form f(z) = z² + c (so h = 0, a = 1). For f to permute S, we need:
1. No two elements of S are negatives of each other (injectivity: z_i + z_j = 0 means z_i = -z_j, and 2h = 0).
2. {z² + c : z ∈ S} = S, i.e., {z² : z ∈ S} = S - c.

So {z² : z ∈ S} must be a translate of S.

Similarly, f(z) = a(z-h)² + k: {a(z-h)² : z ∈ S} = S - k.

Let me think about sets S where {z² : z ∈ S} is a translate of S. 

If S = {roots of z^10 = something}... roots of unity: {z : z^10 = 1}. Then z² ranges over {z : z^10 = 1} if gcd(2,10) = 1, but gcd(2,10) = 2, so z² ranges over {z : z^5 = 1}, which has 5 elements, not 10. So that doesn't work directly.

What about S being a union of two sets related by squaring?

Let me think about S = A ∪ B where A = {z² : z ∈ S} - c for some c. Hmm.

Let me try a very different approach. Let me think about the problem as follows:

We want to count quadratics f(z) = az² + bz + c (a ≠ 0) with f(S) = S. Each such f is a permutation of S. 

Consider the map Φ: (a,b,c) ↦ f. The condition f(S) = S means f permutes S. 

Now, a key idea: if f and g are two quadratics permuting S, then g⁻¹ ∘ f is a permutation of S (not necessarily a polynomial). The quadratics permuting S form a subset of the symmetric group Sym(S).

Let me think about upper bounds. How many quadratics can permute a 10-element set?

Each quadratic is determined by (a, b, c) with a ≠ 0, i.e., 3 complex parameters = 6 real parameters. The condition f(S) = S is very restrictive.

Given h (the critical point), the quadratic is f(z) = a(z-h)² + k. For f to permute S, we need the injectivity condition on h and the affine-equivalence condition. The injectivity condition rules out finitely many h values (midpoints of pairs). The affine-equivalence condition is the main constraint.

Let me think about how many h can make T_h = {(z-h)² : z ∈ S} affine-equivalent to S.

T_h is a set of 10 points. As h varies, T_h varies. The condition that T_h is affine-equivalent to S is a strong algebraic condition on h.

Let me think about invariants. If T_h = aS + k, then certain affine invariants of T_h and S must match. For instance, consider the "second difference" or cross-ratio type invariants.

Actually, here's a cleaner way to think: T_h = aS + k means there's a bijection π: S → S such that (z - h)² = a·π(z) + k for all z ∈ S. Wait, that's not quite right since T_h is a set, not an ordered thing. Let me write: there's a permutation σ of S such that for each z ∈ S, (σ(z) - h)²... no. Let me write: there exists a permutation σ of S and constants a, k such that for all z ∈ S:

f(z) = a(z - h)² + k = σ(z)

where σ is a permutation of S. So f(z) = σ(z) for all z ∈ S, meaning the quadratic f agrees with the permutation σ on S. Since f is degree 2 and we have 10 points, f is the unique degree ≤ 9 polynomial interpolating σ on S, but it happens to be degree 2. So σ must be such that the interpolating polynomial of (z, σ(z)) for z ∈ S has degree exactly 2.

So the count is: the number of permutations σ of S such that the Lagrange interpolating polynomial of σ through S has degree 2 (i.e., is a quadratic).

Equivalently, σ is a permutation of S such that σ(z) = az² + bz + c for some a ≠ 0, for all z ∈ S.

This is equivalent to: the permutation σ, viewed as a function on S, extends to a quadratic polynomial.

Now, the number of such permutations. We need az² + bz + c to take 10 distinct values on S (which it does iff injective, i.e., no pair sums to -b/a = 2h) and those values are exactly S.

Let me think about this combinatorially. We have 10 points. A quadratic az² + bz + c is determined by 3 parameters (a,b,c). Given a, b, c, the values on S are determined. We need these to be a permutation of S.

Alternatively: pick 3 points z_1, z_2, z_3 ∈ S and their images σ(z_1), σ(z_2), σ(z_3) ∈ S (distinct). This determines a, b, c (if the z_i are distinct, which they are). Then check if this quadratic permutes S. The number of quadratics permuting S is at most C(10,3) × P(10,3) / (overcounting), but really it's the number of (a,b,c) that work, which is what we want.

But this doesn't directly help. Let me think about specific constructions.

Construction idea: Let me use a set S that is a union of orbits under a quadratic map.

Consider f(z) = z² - 2. This is related to Chebyshev: if z = 2cos(θ), then z² - 2 = 4cos²(θ) - 2 = 2(2cos²(θ) - 1) = 2cos(2θ). So f(2cos(θ)) = 2cos(2θ). The map θ ↦ 2θ on angles.

If S = {2cos(2πk/11) : k = 0, 1, ..., 9}, these are 10 distinct real values (since 11 is prime, cos(2πk/11) for k=0,...,10 gives 11 values, but cos(2πk/11) = cos(2π(11-k)/11), so k and 11-k give the same value. k=0 gives 2, k=1,...,5 give 5 values, k=6,...,10 mirror. So distinct values: k=0,1,2,3,4,5 → 6 distinct values. That's only 6, not 10.

Hmm. Let me reconsider. For n points 2cos(2πk/n), the number of distinct values is ⌈n/2⌉ + 1 or similar. For 10 distinct values, I'd need n around 19 or 20.

For n = 19 (prime): {2cos(2πk/19) : k = 0, 1, ..., 18}. Distinct values: k and 19-k give same, so k=0,1,...,9 → 10 distinct values. And f(z) = z² - 2 maps 2cos(2πk/19) ↦ 2cos(4πk/19) = 2cos(2π(2k)/19). Since gcd(2,19) = 1, the map k ↦ 2k mod 19 permutes {0,...,18}, and the cos identification means it permutes the 10 distinct values. So f(z) = z² - 2 permutes S = {2cos(2πk/19) : k = 0,...,9}.

But this S is all real (10 real values). We need 7 real and 3 non-real. So this exact construction doesn't work, but it's a starting point.

Now, for this all-real S, how many quadratics permute it? f(z) = z² - 2 is one. Are there others?

The affine symmetries of S = {2cos(2πk/19) : k=0,...,9}: S is a subset of [-2, 2]. The affine maps preserving S: identity, and possibly z ↦ -z (since cos(2πk/19) and -cos(2πk/19) = cos(π - 2πk/19)... hmm, -2cos(2πk/19) = 2cos(π - 2πk/19) = 2cos(2π(19/2 - k)/19), but 19/2 is not integer, so this doesn't map to another element of S in general). Actually, -z maps 2cos(2πk/19) to -2cos(2πk/19) = 2cos(2πk/19 + π)... this isn't of the form 2cos(2πj/19) unless π = 2πj/19 - 2πk/19, i.e., 1/2 = (j-k)/19, which has no integer solution. So -z doesn't preserve S. So AffSym(S) is likely trivial (just identity) for this set.

Hmm, so this gives just 1 quadratic. Not great for maximizing.

Let me think differently. To maximize the number of quadratics, we want S to have lots of structure.

Key realization: Let me think about what sets have many quadratic self-maps.

If S is an arithmetic progression on the real line, say S = {0, 1, 2, ..., 9}, then a quadratic f(x) = ax² + bx + c permutes S. The quadratic takes integer values on integers 0-9 and permutes them. How many such quadratics are there? This is a finite counting problem. For a quadratic to permute {0,...,9}, it must be injective on this set (no two sum to -b/a) and map onto {0,...,9}. 

Actually, for {0, 1, ..., n-1}, quadratics permuting this set: the critical point h = -b/(2a) must not be a half-integer midpoint of any pair. Pairs (i,j) with i+j = 2h, so 2h must not be any integer from 1 to 2n-3 (sum of two distinct elements). For {0,...,9}, sums range from 1 to 17, so 2h ∉ {1,...,17}, i.e., h ∉ {0.5, 1, 1.5, ..., 8.5}. So h must be outside [0.5, 8.5] or... wait, h can be any value not equal to a half-integer midpoint. The midpoints are {(i+j)/2 : 0 ≤ i < j ≤ 9} = {0.5, 1, 1.5, ..., 8.5}. So h ∉ {0.5, 1, 1.5, ..., 8.5}.

But we also need f(S) = S. For an arithmetic progression, this is quite restrictive. I doubt many quadratics work. Let me not pursue this.

Let me think about the problem from a higher level. 

The answer is likely a specific number. Let me think about what structures give many quadratics.

Important insight: Consider the group of affine transformations that preserve S. If S has a large affine symmetry group, and there are several h values making T_h affine-equivalent to S, the count multiplies.

But with 7 real and 3 non-real, the affine symmetry group is limited. An affine map z ↦ az + k preserving S must map the 7 real points among themselves (or to non-real). If a, k are real, it preserves ℝ, so maps real to real. The 7 real points must be preserved as a set, and the 3 non-real as a set.

For the 7 real points to have affine symmetry, they could form an arithmetic progression: {r, r+d, ..., r+6d}, which has affine symmetry z ↦ -z + 2r + 6d (reflection) and identity. So |AffSym(R)| = 2 if R is an AP.

For the 3 non-real points to have affine symmetry: 3 points in the plane. An affine map preserving 3 non-collinear points is the identity (3 non-collinear points determine the affine map). If they're collinear, there could be a reflection. If the 3 non-real points are collinear (on a line in ℂ), say an AP on some line, then reflection gives |AffSym(W)| = 2.

But the affine symmetry of S must simultaneously preserve R and W. If R is an AP on ℝ and W is an AP on some line, the affine map preserving both must preserve ℝ (since R ⊂ ℝ with ≥ 2 points determines the real line) and preserve the line containing W. An affine map preserving ℝ is z ↦ az + k with a, k ∈ ℝ (or a ∈ ℝ, k ∈ ℝ). Wait, z ↦ az + k preserves ℝ iff a, k ∈ ℝ. Then it maps the line containing W to a parallel line (or the same line). For it to preserve W (3 points on a line), the line must be preserved or mapped to a parallel line containing W. If W is on a line not parallel to ℝ (i.e., not horizontal), then a real affine map z ↦ az + k (a,k ∈ ℝ) maps this line to a parallel line (shifted by real amounts), which won't be the same line unless the line is horizontal (parallel to ℝ). 

Hmm, this is getting complicated. Let me try to think about the problem more cleverly.

Let me reconsider. Maybe I should think about specific small examples and build up.

Let me consider the simplest structure: S symmetric about a point.

If S is symmetric about h₀ (i.e., z ∈ S iff 2h₀ - z ∈ S), then h₀ is a midpoint of many pairs, so h₀ is NOT a valid critical point (injectivity fails). But other h values might work.

Let me think about the problem from the perspective of the answer. Competition problems of this type... Let me think about what N could be.

Actually, let me reconsider the structure. We have 10 points, 7 real, 3 non-real. Let me think about the non-real points.

3 non-real points: w₁, w₂, w₃. For a quadratic f(z) = a(z-h)² + k permuting S:

If f has real coefficients (h, a, k ∈ ℝ): f permutes R (7 real) and W (3 non-real) separately, as shown above. f|_R is a real quadratic permuting 7 real points, f|_W is the same quadratic permuting 3 non-real points.

If f has non-real coefficients: f mixes real and non-real points.

Let me focus on real-coefficient quadratics first.

For f|_R (real quadratic permuting 7 real points): A real quadratic x ↦ a(x-h)² + k permuting 7 real points. The critical point h must not be a midpoint of any pair in R. And {a(x-h)² + k : x ∈ R} = R.

For 7 real points, how many real quadratics permute them? This depends on the structure of R.

For f|_W (same quadratic permuting 3 non-real points): {a(w-h)² + k : w ∈ W} = W.

So we need a single quadratic that permutes both R and W.

Let me think about 3 non-real points and a quadratic permuting them. 3 points, quadratic (2-to-1). For injectivity on 3 points, no two sum to 2h. For the quadratic to permute 3 points, it's a permutation of 3 elements, which is either identity, a transposition, or a 3-cycle. But a quadratic can't be the identity on 3 distinct points (a quadratic is determined by 3 points, and if it's identity on 3 points, it's the identity polynomial z, which is degree 1, not 2). So f|_W is either a transposition or a 3-cycle.

If f|_W is a transposition (swaps 2, fixes 1): f(w_i) = w_i for some i, and f(w_j) = w_k, f(w_k) = w_j. f fixes w_i means a(w_i - h)² + k = w_i. And f swaps w_j, w_k.

If f|_W is a 3-cycle: f(w_1) = w_2, f(w_2) = w_3, f(w_3) = w_1.

Now, for the same f to permute R (7 real points): f|_R is a permutation of 7 elements. The cycle structure must be compatible with f being a quadratic.

This is getting very involved. Let me try to think about the problem from a cleaner angle.

Let me reconsider: maybe the answer involves thinking about this as a group action problem.

The set of quadratics permuting S: each is z ↦ a(z-h)² + k. Let me think about the "center" h. 

Claim: The centers h of quadratics permuting S are related to the structure of S.

Let me think about a specific nice construction.

Construction: Let S = {0, ±1, ±2, ±3} ∪ {w₁, w₂, w₃} where the real part is symmetric about 0.

R = {-3, -2, -1, 0, 1, 2, 3} (7 real points, symmetric about 0).

For a real quadratic f(x) = a(x-h)² + k permuting R:
- h ≠ midpoint of any pair in R. Midpoints of pairs in R: (i+j)/2 for -3 ≤ i < j ≤ 3. These include 0, ±0.5, ±1, ±1.5, ±2, ±2.5. So h ∉ {0, ±0.5, ±1, ±1.5, ±2, ±2.5}.
- {a(x-h)² + k : x ∈ R} = R.

Since R = {-3,-2,-1,0,1,2,3} is symmetric about 0, the map x ↦ a(x-h)² + k sends x and 2h-x to the same value. For injectivity, no two elements of R sum to 2h. The sums of pairs in R range from -5 to 5 (specifically: -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, and half-integers). 2h must avoid all these.

For f to permute R = {-3,...,3}: the set {a(x-h)² + k : x ∈ R} must equal {-3,...,3}. 

The values a(x-h)² for x ∈ R are a·{(x-h)² : x ∈ R}. Since (x-h)² = (h-x)², and R is symmetric about 0, if h = 0, then (x)² = x² and {x² : x ∈ R} = {0, 1, 4, 9} — only 4 distinct values, not 7. So h = 0 doesn't give injectivity (since x and -x map to same value), and indeed 0 is a midpoint.

Let me try h not symmetric. Say h = 3 (outside R). Then (x-3)² for x ∈ {-3,...,3}: (−6)², (−5)², (−4)², (−3)², (−2)², (−1)², 0² = 36, 25, 16, 9, 4, 1, 0. These are 7 distinct values {0, 1, 4, 9, 16, 25, 36}. We need a·{0,1,4,9,16,25,36} + k = {-3,-2,-1,0,1,2,3}. So a·{0,1,4,9,16,25,36} + k must be 7 consecutive integers. But {0,1,4,9,16,25,36} are not in arithmetic progression, so no affine map makes them consecutive integers. So h = 3 doesn't work.

Hmm. So for R = {-3,...,3}, it's hard to find real quadratics permuting R. Let me think about what 7-point real sets admit quadratic self-maps.

A real quadratic x ↦ ax² + bx + c permuting a finite real set R of size 7. The quadratic is a parabola. For it to permute R, it must be injective on R (so the axis of symmetry h = -b/(2a) is not a midpoint of any pair in R) and map R onto R.

Since the parabola opens up or down, and R is on the real line, the quadratic maps R to R. The image of R under the quadratic is a set of 7 real numbers (since a, b, c real and R ⊂ ℝ). For this to equal R, the quadratic permutes R.

On the real line, a quadratic is decreasing then increasing (or vice versa), with minimum (or maximum) at h. For x < h, it's monotone; for x > h, it's monotone. So on R, if h is not in R and h separates R into two groups, the quadratic is monotone on each group.

For the quadratic to permute R (a set of 7 real numbers), think of R as sorted: r_1 < r_2 < ... < r_7. If h is between r_k and r_{k+1}, then the quadratic is monotone on {r_1,...,r_k} and monotone on {r_{k+1},...,r_7}. The images of the left group are monotone (say decreasing if parabola opens up), and images of the right group are monotone (increasing). The combined image must be R.

This is like a "shuffle" of two monotone sequences. The number of such shuffles that give a permutation of R is limited.

This is related to the concept of "quadratic permutations" of finite sets. Let me think about specific cases.

For R = {r_1, ..., r_7} and quadratic f permuting R with critical point h between r_k and r_{k+1}:

f is decreasing on {r_1,...,r_k} and increasing on {r_{k+1},...,r_7} (assuming a > 0). So f(r_1) > f(r_2) > ... > f(r_k) and f(r_{k+1}) < f(r_{k+2}) < ... < f(r_7). The image is {f(r_1),...,f(r_k)} ∪ {f(r_{k+1}),...,f(r_7)} = R, and these are 7 distinct values forming R = {r_1 < ... < r_7}.

The minimum of f is at h, so f(r_k) and f(r_{k+1}) are the two smallest images (closest to h). Actually f(r_k) ≥ f(h) and f(r_{k+1}) ≥ f(h), and these are the two closest to the minimum. If a > 0, the minimum value is f(h) = k, and the images increase away from h.

For the image to be R = {r_1,...,r_7}: the smallest image is min(f(r_k), f(r_{k+1})) which should be r_1, and the largest is max(f(r_1), f(r_7)) which should be r_7.

This is getting complicated. Let me try to think about the problem from a completely different angle.

Let me reconsider the problem. Maybe I should think about it in terms of the number of "quadratic permutations" of a set with 7 real and 3 non-real elements, and find the maximum.

Let me think about upper bounds first. 

Upper bound approach: Each quadratic permuting S is determined by its action on any 3 points of S (since 3 points determine a quadratic). But the quadratic must permute S, so it's a permutation of S that happens to be quadratic. The number of permutations of S that are quadratic is what we want.

A quadratic is determined by (a, b, c) with a ≠ 0. Given 3 points z₁, z₂, z₃ ∈ S and their images w₁, w₂, w₃ ∈ S (distinct), there's a unique quadratic (if z₁, z₂, z₃ are distinct, which they are). So the number of quadratics permuting S is at most the number of injective maps from 3 points of S to S such that the resulting quadratic permutes S. But this overcounts since each quadratic is counted C(10,3) times (once for each choice of 3 points). So:

# quadratics = (# triples (z₁,z₂,z₃, σ(z₁),σ(z₂),σ(z₃)) giving a permuting quadratic) / C(10,3)

This doesn't directly give an upper bound. Let me think differently.

Upper bound via critical points: Each quadratic has a unique critical point h. Different quadratics permuting S could share the same h (if there are multiple (a,k) for that h). For a given h, the number of (a,k) making f permute S is at most |AffSym(S)| (as discussed). And the number of valid h is... hard to bound directly.

Let me try to think about this more concretely with a specific construction.

Let me try S = {0, 1, 4, 9, 16, 25, 36} ∪ {w₁, w₂, w₃} where the real part is {0, 1, 4, 9, 16, 25, 36} = {k² : k = 0,...,6}.

Then f(z) = z + c (affine, not quadratic) or... hmm, {z² : z ∈ R} where R = {0,1,...,6} gives {0,1,4,9,16,25,36}. But we need quadratics permuting S, not affine maps.

Let me try: R = {0, 1, 4, 9, 16, 25, 36} and f(z) = (z - h)² + k. If h = 0, f(z) = z² + k, and f(R) = {0, 1, 16, 81, 256, ...} + k, which is not R. So that doesn't work.

OK let me try yet another approach. Let me think about the Chebyshev construction but modified for 7 real + 3 non-real.

Chebyshev: T₂(x) = 2x² - 1. If x = cos(θ), T₂(x) = cos(2θ). 

Consider S = {cos(2πk/n) : k = 0, ..., m} for appropriate n, m. But we need 7 real and 3 non-real.

What if we use a complex version? Consider z ↦ z² on a set that includes both real and non-real elements.

Let me think about the map z ↦ z² on a set S. If S is closed under z ↦ z² (up to the set being preserved), and S has 7 real and 3 non-real elements.

z ↦ z²: real numbers map to real (non-negative). Non-real numbers map to non-real (unless purely imaginary, mapping to negative real).

For S to be preserved by z ↦ z²: the 7 real elements must map to real elements of S, and the 3 non-real must map to elements of S.

Real elements: if r ∈ R ⊂ ℝ, r² ∈ ℝ. For r² ∈ S, r² must be in R (since it's real). So z ↦ z² permutes R. But z ↦ z² on real numbers: r and -r map to the same value. For injectivity, R can't contain both r and -r (unless r = 0). So R has at most one of each {r, -r} pair, plus possibly 0.

If R = {0, 1, 4, 9, 16, 25, 36} (all non-negative, no ±pairs), then z ↦ z² maps 0→0, 1→1, 4→16, 9→81, ... 81 ∉ R. So this doesn't permute R.

For z ↦ z² to permute R ⊂ ℝ: we need R to be closed under squaring and the squaring to be a bijection on R. Since squaring on ℝ is not injective (except on ℝ≥0 or ℝ≤0), R must be in ℝ≥0 or ℝ≤0. Say R ⊂ ℝ≥0. Then z ↦ z² is injective on R iff no two elements are negatives (which is automatic for ℝ≥0 except 0). Actually on ℝ≥0, z ↦ z² is injective. For it to permute R, we need {r² : r ∈ R} = R. So R is closed under squaring and square-rooting (within R). 

For a finite set R ⊂ ℝ≥0 closed under squaring: if r ∈ R, then r², r⁴, r⁸, ... ∈ R. Since R is finite, this sequence must cycle: r^(2^k) = r for some k. So r^(2^k - 1) = 1, meaning r = 0 or r is a (2^k - 1)-th root of unity. For real r ≥ 0, r = 0 or r = 1. So R ⊂ {0, 1} for real non-negative! That gives at most 2 real elements. Not enough for 7.

So z ↦ z² can't permute 7 real points. We need a different quadratic.

Let me go back to the Chebyshev idea. T₂(x) = 2x² - 1 permutes {cos(2πk/n) : k = 0, ..., ⌊n/2⌋} when n is odd. For 7 real points, we need ⌊n/2⌋ + 1 = 7, so n = 13 (⌊13/2⌋ = 6, +1 = 7). So R = {cos(2πk/13) : k = 0, 1, ..., 6} has 7 elements, and T₂(x) = 2x² - 1 permutes R (since gcd(2,13) = 1).

Now, T₂(x) = 2x² - 1 has critical point h = 0, a = 2, k = -1. The injectivity condition: no two elements of R sum to 0. R = {cos(2πk/13) : k = 0,...,6}. cos(2πk/13) + cos(2πj/13) = 0 iff cos(2πk/13) = -cos(2πj/13) = cos(π - 2πj/13) = cos(2π(13/2 - j)/13). Since 13/2 is not integer, this doesn't give another element of R. Actually, cos(2πk/13) = -cos(2πj/13) iff 2πk/13 = π - 2πj/13 + 2πm, i.e., 2k/13 = 1 - 2j/13 + 2m, i.e., 2k + 2j = 13 + 26m, i.e., 2(k+j) = 13(1 + 2m). LHS is even, RHS is odd. No solution. So no two elements of R sum to 0. Good, injectivity holds.

So T₂(x) = 2x² - 1 permutes R = {cos(2πk/13) : k = 0,...,6}. Now I need to add 3 non-real elements W = {w₁, w₂, w₃} such that T₂ also permutes W, and possibly other quadratics also permute S = R ∪ W.

T₂(z) = 2z² - 1 permutes W: {2w² - 1 : w ∈ W} = W. So W is closed under z ↦ 2z² - 1. For 3 elements, the map z ↦ 2z² - 1 must be a permutation of W (bijection). As discussed, it's either a transposition or a 3-cycle.

If it's a 3-cycle: w₁ ↦ w₂ ↦ w₃ ↦ w₁. Then 2w₁² - 1 = w₂, 2w₂² - 1 = w₃, 2w₃² - 1 = w₁. These are 3 equations. The w's are non-real.

If it's a transposition: say w₁ ↦ w₁ (fixed) and w₂ ↔ w₃. Then 2w₁² - 1 = w₁, so 2w₁² - w₁ - 1 = 0, (2w₁ + 1)(w₁ - 1) = 0, w₁ = 1 or w₁ = -1/2. Both real! So w₁ can't be non-real if it's fixed. So the transposition case with a fixed point doesn't work for non-real W (the fixed point would be real).

Wait, unless the fixed point is real and in R. But we said f permutes R and W separately (for real coefficients). If w₁ is fixed and real, it's in R, not W. So for W (all non-real), the transposition case requires the fixed point to be in W, but fixed points of T₂ are 1 and -1/2 (both real). So transposition doesn't work for non-real W.

So T₂ must act as a 3-cycle on W. We need non-real w₁, w₂, w₃ with 2w₁² - 1 = w₂, 2w₂² - 1 = w₃, 2w₃² - 1 = w₁.

This means w₁ is a periodic point of T₂ with period 3 (or period dividing 3, but period 1 gives real, period 3 gives the 3-cycle). The period-3 points of T₂(z) = 2z² - 1 are solutions of T₂³(z) = z, i.e., 2(2(2z²-1)²-1)² - 1 = z. This is a degree 8 polynomial. The fixed points (period 1) are z = 1 and z = -1/2. So period-3 points satisfy T₂³(z) = z but not T₂(z) = z. The degree 8 polynomial T₂³(z) - z = 0 has 8 roots. Two are the fixed points. The remaining 6 are period-3 points (forming two 3-cycles, since each 3-cycle has 3 elements). 

Are these period-3 points real or non-real? T₂ maps [-1,1] to [-1,1]. The Chebyshev dynamics on [-1,1]: T₂(cos θ) = cos 2θ. Period-3 points: cos(2³θ) = cos(θ), so 8θ = ±θ + 2πk. 8θ = θ + 2πk → 7θ = 2πk → θ = 2πk/7. 8θ = -θ + 2πk → 9θ = 2πk → θ = 2πk/9.

For θ = 2πk/7: cos(2πk/7) for k = 0,...,6. k=0 gives 1 (fixed point). k=1,...,6: cos(2πk/7), and cos(2πk/7) = cos(2π(7-k)/7), so distinct values: k=0,1,2,3 → 4 values. But k=0 is the fixed point 1. So 3 distinct non-trivial values: cos(2π/7), cos(4π/7), cos(6π/7). These are all real! And they form a 3-cycle under T₂ (since k ↦ 2k mod 7 permutes {1,2,3,4,5,6} and the cos identification pairs k with 7-k, so the 3-cycle is on {1,2,3} ↔ {6,5,4}).

Wait, so the period-3 points from θ = 2πk/7 are real. What about θ = 2πk/9? cos(2πk/9) for k = 0,...,8. k=0 gives 1 (fixed). The map k ↦ 2k mod 9: 1→2→4→8→7→5→1 (6-cycle) and 3→6→3 (2-cycle) and 0→0. So cos(2πk/9) for k=1,2,4,8,7,5 form a 6-cycle (period 6 under T₂), and k=3,6 form a 2-cycle (period 2). So θ = 2πk/9 gives period 6 and period 2 points, not period 3.

Hmm wait, I need to be more careful. T₂(cos θ) = cos(2θ). T₂^n(cos θ) = cos(2^n θ). Period n means cos(2^n θ) = cos(θ), i.e., 2^n θ ≡ ±θ (mod 2π).

For period 3: 8θ ≡ ±θ (mod 2π).
- 8θ ≡ θ: 7θ ≡ 0 (mod 2π), θ = 2πk/7. Period divides 3, and since 7 is prime and doesn't divide 2^d - 1 for d < 3 (2^1-1=1, 2^2-1=3, neither divisible by 7), the period is exactly 3. So these are genuine period-3 points. They're cos(2πk/7), all real.
- 8θ ≡ -θ: 9θ ≡ 0 (mod 2π), θ = 2πk/9. Period divides 3. 2^1+1=3, 2^2+1=5, 2^3+1=9. So 9 | 2^3+1, and 9 doesn't divide 2^d+1 for d < 3 (3 doesn't divide 2^1+1=3... wait 3 | 3. So θ = 2π/3 gives period 1? cos(2π/3) = -1/2, and T₂(-1/2) = 2(1/4)-1 = -1/2. Yes, -1/2 is a fixed point! So θ = 2πk/9 with 9θ = 2πk, and we need to check which give period 3 vs period 1.

The fixed points are θ = 0 (cos 0 = 1) and θ = 2π/3 (cos(2π/3) = -1/2). θ = 2πk/9: k=0 → θ=0 (fixed), k=3 → θ=2π/3 (fixed). The others: k=1,2,4,5,7,8. k=1: θ=2π/9, k=2: θ=4π/9, k=4: θ=8π/9, k=5: θ=10π/9, k=7: θ=14π/9, k=8: θ=16π/9. Under k ↦ 2k mod 9 (for the +case) or k ↦ -2k mod 9 (for the -case)... 

Actually, the dynamics: T₂(cos θ) = cos(2θ). The map on θ is θ ↦ 2θ (mod 2π), but with the identification θ ~ -θ (since cos). So the dynamics on θ ∈ [0,π] is θ ↦ 2θ if 2θ ≤ π, θ ↦ 2π - 2θ if 2θ > π. This is the "tent map" or "doubling map" on [0,π].

For period 3 under this map: the orbit of θ under the doubling map (mod the identification) has period 3.

From the 7θ = 2πk analysis: θ = 2πk/7, k=1,2,3 (up to identification k ~ 7-k). These give 3 real period-3 points forming one 3-cycle.

From the 9θ = 2πk analysis: θ = 2πk/9, k=1,2,4,5,7,8 (excluding k=0,3 which are fixed). Under the doubling map: 1→2→4→8→7→5→1 (mod 9), but with identification k ~ 9-k: 1~8, 2~7, 4~5. So the orbit: 1→2→4→8~1, so 1→2→4→1, a 3-cycle! Similarly 5→1, 7→2, etc. So {1,2,4} (identified with {8,7,5}) form a 3-cycle. cos(2π/9), cos(4π/9), cos(8π/9) — all real.

So ALL period-3 points of T₂ are real! There are 6 period-3 points (two 3-cycles), all real: {cos(2π/7), cos(4π/7), cos(6π/7)} and {cos(2π/9), cos(4π/9), cos(8π/9)}.

Wait, but T₂³(z) - z is degree 8, with 2 fixed points and 6 period-3 points. All 8 roots are real? Let me verify: the 8 roots are cos(2πk/7) for k=0,...,6 (7 values, but k=0 is the fixed point 1) and... no wait. Let me recount.

T₂³(z) - z = 0 has degree 8. The roots are z such that T₂³(z) = z. These include:
- Fixed points: T₂(z) = z, i.e., 2z² - z - 1 = 0, z = 1, -1/2. (2 roots)
- Period-3 points: T₂³(z) = z but T₂(z) ≠ z. (6 roots)

From the Chebyshev analysis, the period-3 points are cos(2πk/7) for k=1,...,6 (but cos(2πk/7) = cos(2π(7-k)/7), so 3 distinct values) and cos(2πk/9) for k=1,2,4,5,7,8 (but with identification, 3 distinct values). So 3 + 3 = 6 period-3 points, all real.

So T₂³(z) - z has all 8 roots real: {1, -1/2, cos(2π/7), cos(4π/7), cos(6π/7), cos(2π/9), cos(4π/9), cos(8π/9)}.

This means T₂ has NO non-real period-3 points! So we can't find 3 non-real points forming a 3-cycle under T₂.

Hmm. So the Chebyshev approach with T₂ doesn't directly give us non-real 3-cycles.

But wait — we don't have to use T₂. We can use any quadratic. And the 3 non-real points don't have to be in a single 3-cycle under the same quadratic that permutes R. We could have different quadratics permuting S, some of which act differently on R and W.

Let me reconsider. We want to MAXIMIZE the number of quadratics permuting S. We get to choose S (7 real, 3 non-real) and count all quadratics (real or complex coefficients) permuting S.

Let me think about this more broadly. Let me consider quadratics with complex (non-real) coefficients too.

For a quadratic f(z) = a(z-h)² + k with non-real h (or non-real a, k), f doesn't preserve ℝ. So f can map real elements to non-real and vice versa.

Let me think about the problem differently. Let me consider the set of all quadratics permuting S. Each is z ↦ a(z-h)² + k. The critical point h can be real or non-real.

For f to permute S (10 elements, injective on S): no two elements of S sum to 2h. The "forbidden" values of 2h are {z_i + z_j : i < j}, which are C(10,2) = 45 values. So h avoids 45 values in ℂ. The valid h are all of ℂ except these 45 values (and we need the affine-equivalence condition).

Now, the affine-equivalence condition: T_h = {(z-h)² : z ∈ S} must be an affine image of S. This is a very strong condition. Let me think about how many h can satisfy it.

T_h = aS + k means: there's a permutation σ of S with (z-h)² = aσ(z) + k for all z ∈ S. So for each z ∈ S, (z-h)² = aσ(z) + k. This gives 10 equations. The unknowns are a, k, h, and the permutation σ. Given σ (a permutation of S), we have 10 equations (z-h)² = aσ(z) + k in 3 unknowns (a, k, h). For a generic σ, this is overdetermined (10 equations, 3 unknowns) and has no solution. For special σ, it might have a solution.

Given σ, the equations are: (z_i - h)² = a·σ(z_i) + k for i = 1,...,10. Expanding: z_i² - 2hz_i + h² = a·σ(z_i) + k. So z_i² - 2hz_i + h² - a·σ(z_i) - k = 0 for all i. This means the quadratic polynomial z² - 2hz + h² - a·σ(z) - k vanishes on S... but σ(z) is only defined on S, not as a polynomial. 

Let me think of it as: the polynomial P(z) = z² - 2hz + (h² - k) agrees with a·σ(z) on S. So σ(z) = (z² - 2hz + h² - k)/a = (1/a)z² - (2h/a)z + (h²-k)/a on S. So σ is the restriction of a quadratic to S. This is just saying f(z) = az² + bz + c with a = 1 (wait, I'm confusing myself).

Let me restart the parametrization. f(z) = Az² + Bz + C (A ≠ 0) permutes S. f(z) = A(z - h)² + K where h = -B/(2A), K = C - B²/(4A). The condition is f(S) = S (as sets, i.e., f is a bijection on S).

So the count is: number of (A, B, C) with A ≠ 0 such that f(z) = Az² + Bz + C permutes S.

Equivalently: number of permutations σ of S such that σ(z) = Az² + Bz + C for some A ≠ 0, for all z ∈ S. I.e., σ extends to a quadratic polynomial.

Given a permutation σ of S, when does it extend to a quadratic? The interpolating polynomial of σ through S has degree ≤ 9. It's a quadratic iff the degree is exactly 2 (or less, but degree 1 or 0 can't give a bijection on 10 points). So we need the interpolating polynomial to have degree 2.

The interpolating polynomial has degree ≤ 2 iff the third and higher divided differences are 0. Equivalently, σ(z) = Az² + Bz + C on S.

So the count is the number of permutations of S that are "quadratic permutations" (extend to degree-2 polynomials).

Now, let me think about this combinatorially. A quadratic Az² + Bz + C is determined by 3 parameters. Given 3 points of S and their images, the quadratic is determined. For it to permute S, the remaining 7 points must also map to S.

So: pick 3 points z₁, z₂, z₃ ∈ S and 3 distinct images w₁, w₂, w₃ ∈ S. This determines a quadratic f. Check if f permutes S. The number of quadratics permuting S equals the number of such (z₁,z₂,z₃,w₁,w₂,w₃) that work, divided by C(10,3) (since each quadratic is counted once for each choice of 3 points from S, and the images are determined).

Wait, actually each quadratic permuting S is counted C(10,3) times (once for each 3-element subset of S, with the images being f of those 3 points). So:

# quadratics = (# valid 6-tuples) / C(10,3)

But this is hard to compute directly. Let me think about upper bounds.

Upper bound: The number of quadratics permuting S is at most the number of triples (z₁, z₂, z₃, w₁, w₂, w₃) with z's distinct in S, w's distinct in S, divided by C(10,3). The total number of such triples is C(10,3) × P(10,3) = C(10,3) × 10·9·8. So the upper bound is P(10,3) = 720. But this is a very loose bound.

Better upper bound: For each choice of (z₁, w₁) (10 × 10 = 100 choices, but w₁ ≠ z₁ for a non-identity permutation, or w₁ = z₁), the quadratic is not determined. We need 3 points. 

Hmm, let me think about it differently. Let me think about the critical point h.

For each valid h (not a midpoint of any pair in S), the quadratic f(z) = A(z-h)² + K permutes S iff {A(z-h)² + K : z ∈ S} = S, i.e., {A(z-h)² : z ∈ S} = S - K. Let T_h = {(z-h)² : z ∈ S} (a set of 10 distinct values since h is valid). We need T_h to be an affine image of S: T_h = (1/A)(S - K) = S/A - K/A. So T_h and S are affine-equivalent.

The number of affine maps taking T_h to S is the number of (A, K) with A·T_h + K = S, which is |AffSym(S)| (if T_h ≅ S affinely) or 0.

So # quadratics = |AffSym(S)| × #{valid h : T_h ≅ S affinely}.

Now I need to figure out:
1. |AffSym(S)| for the best S.
2. The number of valid h with T_h ≅ S.

Let me think about AffSym(S). S has 7 real and 3 non-real points. An affine map z ↦ αz + β preserving S. 

If α, β ∈ ℝ: the map preserves ℝ, so it maps R (7 real) to R and W (3 non-real) to W. It's an affine self-map of R (7 real points) and of W (3 non-real points) simultaneously.

If α, β ∉ ℝ (or one of them): the map doesn't preserve ℝ, so it can mix real and non-real points.

For maximizing |AffSym(S)|, we want S to have affine symmetries. But the 7+3 split (7 real, 3 non-real) is constraining.

Case 1: α, β ∈ ℝ. AffSym_ℝ(S) = {z ↦ αz + β : α, β ∈ ℝ, αR + β = R, αW + β = W}.
- αR + β = R: R is a 7-point set on ℝ. Affine symmetries of 7 points on a line. If R is an arithmetic progression {r, r+d, ..., r+6d}, the affine symmetries are z ↦ z (identity) and z ↦ -z + 2r + 6d (reflection). So |AffSym(R)| = 2.
- αW + β = W: W is 3 non-real points. For a real affine map to preserve W, W must be on a line stable under real affine maps. z ↦ αz + β with α, β ∈ ℝ maps a point x+iy to (αx+β) + i(αy). So the imaginary parts are scaled by α. For W = {w₁, w₂, w₃} to be preserved, the imaginary parts of w₁, w₂, w₃ must be scaled by α and the real parts by α then shifted by β. 

If W is an arithmetic progression on a horizontal line (all same imaginary part): W = {x₁+iy, x₂+iy, x₃+iy} with x₁, x₂, x₃ in AP. Then z ↦ αz + β maps to {(αx_i+β) + iαy}. For this to equal W, we need αy = y (so α = 1, since y ≠ 0) and {αx_i + β} = {x₁, x₂, x₃}. With α = 1, {x_i + β} = {x_i}, so β = 0. So only the identity. Alternatively, α = -1 (reflection): then imaginary parts become -y, so W must also have points with imaginary part -y. But W has all points with imaginary part y (same horizontal line), so -y ≠ y (since y ≠ 0), contradiction. So if W is on a horizontal line, only identity preserves it (among real affine maps). Unless W is symmetric about a real point: W = {x-iy, x₀+iy, x+iy}... no, that's not on one horizontal line.

Hmm, let me reconsider. If W = {w₁, w₂, w₃} and we want z ↦ -z + β (reflection, α = -1) to preserve W: -w_i + β ∈ W for all i. So W is symmetric about β/2. If W = {β/2 + u, β/2 + v, β/2 - u} (symmetric about β/2, with v being the center), then -w_i + β = β/2 - u, β/2 - v, β/2 + u. For this to equal W, we need β/2 - v = β/2 + v, so v = 0, meaning w₂ = β/2 (the center is in W). And W = {β/2 + u, β/2, β/2 - u}. If β/2 is real, then w₂ is real, contradicting W being non-real. If β/2 is non-real, then the reflection z ↦ -z + β has β non-real, so it's not a real affine map. 

So for real affine maps (α, β ∈ ℝ), the reflection z ↦ -z + β (β ∈ ℝ) preserves W only if W is symmetric about a real point β/2, with the center β/2 ∈ W. But β/2 ∈ ℝ, so W would contain a real point, contradiction. So no non-trivial real affine map preserves W (if W has no real points and the map has α = -1).

What about α = 1, β ≠ 0? Then z ↦ z + β (translation by real β). This preserves W iff W + β = W, i.e., W is invariant under translation by β. For a finite set, this requires β = 0. So only identity.

What about other α? For |α| ≠ 1, the map scales distances. For a finite set to be preserved, we'd need the set to be scale-invariant, which for 3 points means they're in geometric progression or similar. But with the constraint that α is real and the map preserves W (non-real points), and also preserves R...

This is getting very complicated. Let me step back and think about whether |AffSym(S)| can be > 1 for a good choice of S, and whether non-real affine symmetries are possible.

Case 2: Non-real affine maps. z ↦ αz + β with α or β non-real. This maps ℝ to a line in ℂ (not ℝ unless α, β ∈ ℝ). So real points of S map to non-real points (generally). For the map to preserve S (7 real, 3 non-real), some real points must map to non-real and some non-real to real. If r real points map to non-real and s non-real map to real, then 7 - r + s = 7 (real count in image) and 3 - s + r = 3 (non-real count). So r = s. And r ≤ 7, s ≤ 3, so r = s ≤ 3.

So a non-real affine symmetry maps r ≤ 3 real points to non-real positions and r non-real points to real positions. The remaining 7 - r real points stay real, and 3 - r non-real points stay non-real.

For r = 3: all 3 non-real points map to real, and 3 real points map to non-real. The 4 remaining real points stay real. This is possible in principle.

This is very flexible and hard to analyze in general. Let me try to think about the problem from the answer side.

Let me consider the possibility that the answer is related to a specific number. Let me think about what kinds of sets S could have many quadratic self-maps.

Alternative approach: Let me think about the problem in terms of the functional structure.

A quadratic f(z) = Az² + Bz + C permuting S. The key constraint is that f is 2-to-1 (generically), and on S it's 1-to-1 (bijective). The "folding" of the quadratic must not identify any two points of S.

Let me think about the problem for small cases and see if there's a pattern.

For |S| = n with all real, the number of real quadratics permuting S is related to the structure. For the Chebyshev set {cos(2πk/(2n-1)) : k=0,...,n-1} (n points, with 2n-1 prime), T₂ permutes it, giving 1 quadratic. But maybe other quadratics also work.

Hmm, let me think about this differently. Let me consider the problem as maximizing over S, and think about what S gives the most quadratics.

Let me consider S = R ∪ W where R is chosen to have many quadratic self-maps and W is chosen to be compatible.

For R (7 real points), the maximum number of real quadratics permuting R: Let me think about this. A real quadratic permuting 7 real points. The critical point h splits R into two groups (left and right of h), and the quadratic is monotone on each. The image is a "merge" of two monotone sequences.

For 7 points, the number of such "quadratic permutations" depends on the specific set R. For a set like an arithmetic progression, there might be several.

Actually, let me think about the arithmetic progression R = {0, 1, 2, 3, 4, 5, 6}. A quadratic f(x) = Ax² + Bx + C permuting R. The critical point h = -B/(2A) must not be a midpoint of any pair in R. Midpoints of pairs in {0,...,6}: {(i+j)/2 : 0 ≤ i < j ≤ 6} = {0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5}. So h ∉ {0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5}.

For f to permute {0,...,6}: f takes 7 distinct values on {0,...,6} and these must be {0,...,6}. 

The sum of f(0) + f(1) + ... + f(6) = A(0+1+4+9+16+25+36) + B(0+1+2+3+4+5+6) + 7C = 91A + 21B + 7C. This must equal 0+1+2+...+6 = 21. So 91A + 21B + 7C = 21, i.e., 13A + 3B + C = 3.

Also, f(i) ∈ {0,...,6} for each i, and f is a bijection. This is a strong constraint. Let me just try to find all quadratics permuting {0,...,6}.

This is a finite problem. Let me think about it. The quadratic f(x) = Ax² + Bx + C with f({0,...,6}) = {0,...,6}.

Since f is a bijection on {0,...,6}, and f is a quadratic (parabola), the graph of f on {0,...,6} is a permutation that's "V-shaped" or "Λ-shaped" (decreasing then increasing, or increasing then decreasing).

For A > 0 (upward parabola, V-shaped): f decreases on (-∞, h) and increases on (h, ∞). On {0,...,6}, if h is between k and k+1, f is decreasing on {0,...,k} and increasing on {k+1,...,6}. The minimum is near h. The image values: f(k) and f(k+1) are the two smallest (closest to the minimum). The largest values are f(0) and f(6) (the endpoints).

For the image to be {0,...,6}: the minimum value is 0 (achieved at the point closest to h) and the maximum is 6 (achieved at one of the endpoints). 

Actually, the minimum of f on {0,...,6} is min(f(k), f(k+1)) (the two points closest to h). This must be 0. The maximum is max(f(0), f(6)), which must be 6.

This is getting complicated. Let me just try small cases computationally in my head... or better, let me think about the problem structure.

Actually, I realize I should think about this problem more cleverly. Let me reconsider.

The key formula: # quadratics permuting S = |AffSym(S)| × #{valid h : T_h ≅ S affinely}.

To maximize this, we want both |AffSym(S)| and #{valid h} to be large.

Let me think about #{valid h : T_h ≅ S}. T_h = {(z-h)² : z ∈ S}. For T_h to be affine-equivalent to S, there must be a permutation σ of S with (z-h)² = ασ(z) + β for some α, β. This means z² - 2hz + h² = ασ(z) + β, so σ(z) = (z² - 2hz + h² - β)/α = (1/α)z² - (2h/α)z + (h²-β)/α. So σ is a quadratic function of z (with leading coefficient 1/α, linear coefficient -2h/α). 

So σ(z) = Az² + Bz + C where A = 1/α, B = -2h/α, C = (h²-β)/α. And h = -B/(2A), which is consistent (h is the critical point of f(z) = Az² + Bz + C... wait, f(z) = Az² + Bz + C and h = -B/(2A). Yes.)

So the number of valid h is the number of distinct critical points h among all quadratic permutations of S. And the total count is:

# quadratics = sum over valid h of (number of quadratics with critical point h permuting S)

= sum over valid h of |AffSym(S)| [if T_h ≅ S]

Wait, I derived earlier that for each valid h with T_h ≅ S, the number of (A,K) is |AffSym(S)|. But actually, the number of affine maps from T_h to S is |AffSym(T_h)| = |AffSym(S)| (since T_h ≅ S). But each such affine map gives a distinct quadratic f(z) = A(z-h)² + K. And different h give different quadratics (different critical points). So:

# quadratics = |AffSym(S)| × #{valid h : T_h ≅ S affinely}

But wait, I need to double-check: could two different h give the same quadratic? No, because h = -B/(2A) is uniquely determined by the quadratic. So different h ⟹ different quadratics. And for the same h, different (A,K) give different quadratics. So the formula holds.

Now, #{valid h : T_h ≅ S} is the number of distinct critical points of quadratic permutations of S. Each quadratic permutation has a unique critical point, and for each critical point h, there are |AffSym(S)| quadratics. So:

# quadratics = |AffSym(S)| × (# distinct critical points)

And # distinct critical points = # quadratics / |AffSym(S)|, which is circular. Let me re-derive.

Let Q = set of quadratics permuting S. |Q| = N.
Let H = set of critical points of quadratics in Q. |H| = number of distinct h.
For each h ∈ H, the number of quadratics with critical point h is the number of (A,K) with A·T_h + K = S, which is |AffSym(S)| (if T_h ≅ S).

So N = |H| × |AffSym(S)|.

Now I need to find max over S of |H| × |AffSym(S)|.

Let me think about |H|. H is the set of h such that T_h = {(z-h)² : z ∈ S} is affine-equivalent to S and h is not a midpoint of any pair in S.

T_h ≅ S means there's a permutation σ of S with σ(z) = (z² - 2hz + h² - β)/α, i.e., σ is a quadratic in z with specific coefficients related to h. The leading coefficient is 1/α (free), the linear coefficient is -2h/α = -2h · (leading coeff). So given the leading coefficient A = 1/α, the linear coefficient is B = -2hA, so h = -B/(2A). And C = (h² - β)/α = A(h² - β), so β = h² - C/A.

So for each quadratic permutation σ(z) = Az² + Bz + C of S, the critical point is h = -B/(2A). The number of distinct h is |H|.

Now, |H| is the number of distinct values of -B/(2A) among all quadratic permutations Az² + Bz + C of S.

Hmm, this is still complex. Let me try to think about specific constructions and compute.

Let me try a concrete approach. Let me consider S with specific structure and count.

Construction 1: S = R ∪ W where R = {cos(2πk/13) : k = 0,...,6} (7 real Chebyshev points) and W = {3 non-real points}.

For R, T₂(z) = 2z² - 1 permutes R. The critical point of T₂ is h = 0. Are there other quadratics permuting R?

For the Chebyshev set R = {cos(2πk/13) : k = 0,...,6}, the quadratics permuting R: T₂(z) = 2z² - 1 is one. Are there others?

The affine symmetries of R: R = {cos(2πk/13) : k=0,...,6}. Is there a non-trivial affine map preserving R? R ⊂ [-1, 1]. The map z ↦ -z: -cos(2πk/13) = cos(π - 2πk/13) = cos(2π(13/2 - k)/13). Since 13/2 is not an integer, this is not of the form cos(2πj/13) for integer j. So -z doesn't preserve R. So |AffSym(R)| = 1.

So for R alone, the quadratics permuting R: T₂ is one (h = 0). Are there others? 

Let me think... for the Chebyshev set, the only quadratic self-map is T₂ (up to affine conjugation). Actually, I think for the set {cos(2πk/p) : k = 0,...,(p-1)/2} with p prime, the only polynomial self-maps of degree d with gcd(d, p) = 1 are the Chebyshev T_d. But we're looking at all quadratics, not just Chebyshev. 

Hmm, but a quadratic permuting this set doesn't have to be a Chebyshev polynomial. It could be any quadratic that happens to permute the set. Let me think about whether there are others.

For R = {cos(2πk/13) : k = 0,...,6}, a quadratic f(z) = Az² + Bz + C permuting R. We need f(cos(2πk/13)) ∈ R for k = 0,...,6, and f is a bijection on R.

Using the Chebyshev identity: cos(2θ) = 2cos²(θ) - 1. So T₂(cos θ) = cos(2θ). A general quadratic Az² + Bz + C applied to cos(θ) gives A·cos²(θ) + B·cos(θ) + C = (A/2)(1 + cos(2θ)) + B·cos(θ) + C = (A/2)cos(2θ) + B·cos(θ) + (A/2 + C).

For this to be in R = {cos(2πk/13) : k = 0,...,6} for all θ = 2πk/13, we need (A/2)cos(2θ) + B·cos(θ) + (A/2 + C) ∈ R for all θ = 2πk/13, k = 0,...,6.

This is a linear combination of cos(2θ), cos(θ), and 1, evaluated at θ = 2πk/13. For this to always be in R (a specific finite set), the coefficients must be very special.

If B = 0: f(cos θ) = (A/2)cos(2θ) + (A/2 + C). This is an affine function of cos(2θ). Since cos(2θ) ranges over {cos(4πk/13) : k = 0,...,6} = R (because the map k ↦ 2k mod 13 permutes {0,...,12} and cos identifies k with 13-k, so {cos(4πk/13) : k=0,...,6} = {cos(2πj/13) : j = 0,...,6} = R). So f(cos θ) = (A/2)·(element of R) + (A/2 + C). For f to permute R, we need (A/2)·R + (A/2 + C) = R, i.e., R is invariant under the affine map z ↦ (A/2)z + (A/2 + C). Since |AffSym(R)| = 1 (only identity), we need A/2 = 1 and A/2 + C = 0, so A = 2, C = -1. This gives f(z) = 2z² - 1 = T₂(z). 

If B ≠ 0: f(cos θ) = (A/2)cos(2θ) + B·cos(θ) + (A/2 + C). This involves both cos(2θ) and cos(θ). For θ = 2πk/13, cos(θ) and cos(2θ) are both in R, but their linear combination being in R for all k is very restrictive. I believe the only solution is B = 0 (giving T₂), but I'm not 100% sure. Let me think about whether B ≠ 0 could work.

For k = 0: cos(0) = 1, cos(0) = 1. f(1) = A + B + C. This must be in R.
For k = 1: cos(2π/13), cos(4π/13). f(cos(2π/13)) = (A/2)cos(4π/13) + B·cos(2π/13) + (A/2 + C). Must be in R.

This gives a system where f maps 7 points to 7 points in R. With 3 free parameters (A, B, C) and 7 constraints (each f value in R), it's overdetermined. The only solution is likely T₂ (B = 0, A = 2, C = -1).

Actually, I realize there might be other solutions. Let me think about it differently. The quadratic f permutes R, so it's a permutation of 7 elements that extends to a quadratic. The number of such permutations is what we want for R alone.

For the Chebyshev set, I believe the only quadratic permutation is T₂. But let me consider other sets R.

Let me try R = {0, 1, 2, 3, 4, 5, 6} (arithmetic progression). Let me find all quadratics permuting R.

f(x) = Ax² + Bx + C permuting {0,1,2,3,4,5,6}. 

Conditions:
- f(i) ∈ {0,...,6} for i = 0,...,6
- f is injective on {0,...,6}
- f({0,...,6}) = {0,...,6}

The sum condition: Σf(i) = 21, giving 13A + 3B + C = 3 (derived earlier, wait let me recheck: Σf(i) = A·Σi² + B·Σi + 7C = A·91 + B·21 + 7C = 21. So 91A + 21B + 7C = 21, divide by 7: 13A + 3B + C = 3.)

Also, Σf(i)² = Σi² = 91. Σf(i)² = Σ(Ai² + Bi + C)² = Σ(A²i⁴ + 2ABi³ + (B² + 2AC)i² + 2BCi + C²) = A²·Σi⁴ + 2AB·Σi³ + (B²+2AC)·Σi² + 2BC·Σi + 7C².

Σi⁴ for i=0..6 = 0+1+16+81+256+625+1296 = 2275.
Σi³ = (6·7/2)² = 441.
Σi² = 91.
Σi = 21.

So Σf(i)² = 2275A² + 882AB + 91(B²+2AC) + 42BC + 7C² = 91.

And Σf(i)³ = Σi³ = 441. This gives another equation. And so on.

This system of equations (power sums) determines the possible (A, B, C). With enough equations, we can solve.

From 13A + 3B + C = 3 (first power sum).
From the second power sum: 2275A² + 882AB + 91B² + 182AC + 42BC + 7C² = 91.

Let me substitute C = 3 - 13A - 3B:

Second equation: 2275A² + 882AB + 91B² + 182A(3-13A-3B) + 42B(3-13A-3B) + 7(3-13A-3B)² = 91.

Let me expand:
182A(3-13A-3B) = 546A - 2366A² - 546AB
42B(3-13A-3B) = 126B - 546AB - 126B²
7(3-13A-3B)² = 7(9 - 78A - 18B + 169A² + 78AB + 9B²) = 63 - 546A - 126B + 1183A² + 546AB + 63B²

Sum: 2275A² + 882AB + 91B² + 546A - 2366A² - 546AB + 126B - 546AB - 126B² + 63 - 546A - 126B + 1183A² + 546AB + 63B²

A² terms: 2275 - 2366 + 1183 = 1092
AB terms: 882 - 546 - 546 + 546 = 336
B² terms: 91 - 126 + 63 = 28
A terms: 546 - 546 = 0
B terms: 126 - 126 = 0
Constant: 63

So: 1092A² + 336AB + 28B² + 63 = 91
→ 1092A² + 336AB + 28B² = 28
→ 39A² + 12AB + B² = 1
→ (3A + B)² + 30A² = 1... let me check: (3A+B)² = 9A² + 6AB + B². So 39A² + 12AB + B² = (9A² + 6AB + B²) + 30A² + 6AB = (3A+B)² + 6A(5A + B). Hmm, that doesn't simplify nicely.

Let me try: 39A² + 12AB + B² = 1. This is a quadratic in B: B² + 12AB + 39A² - 1 = 0. B = (-12A ± √(144A² - 4(39A² - 1)))/2 = (-12A ± √(144A² - 156A² + 4))/2 = (-12A ± √(4 - 12A²))/2 = -6A ± √(1 - 3A²).

For B to be real, 1 - 3A² ≥ 0, so |A| ≤ 1/√3.

Now I also need the third power sum: Σf(i)³ = 441. And higher power sums. Each gives another equation, further constraining A, B, C.

This is getting very computational. Let me try a different approach.

Let me think about the problem more cleverly. 

I think the key insight might be related to the following: a quadratic f(z) = a(z-h)² + k permuting S. The map z ↦ (z-h)² "folds" the plane about h. For f to permute S, the folded set T_h must be affine-equivalent to S.

Let me think about the problem in terms of the "folding" structure. The 10 points of S are folded about h: points equidistant from h (on opposite sides) map to the same value. Since f is injective on S, no two points of S are symmetric about h. The folded set T_h has 10 distinct points, and these must form an affine copy of S.

Now, here's a key structural observation: the map z ↦ (z-h)² sends z and 2h-z to the same value. So T_h "identifies" pairs symmetric about h. But since no two points of S are symmetric about h, T_h has 10 distinct points. However, the structure of T_h is constrained: it's the image of S under a 2-to-1 map (with no collisions on S).

Let me think about the real and non-real structure. 

Let me consider h real. Then (z-h)² for real z is real and non-negative. For non-real z = x+iy, (z-h)² = (x-h)² - y² + 2i(x-h)y. 

If h is real:
- Real elements r ∈ R: (r-h)² ∈ ℝ≥0. So T_h contains 7 non-negative real values from R.
- Non-real elements w = x+iy ∈ W: (w-h)² = (x-h)² - y² + 2i(x-h)y. This is real iff x = h (i.e., w is directly above/below h), otherwise non-real.

For T_h to be affine-equivalent to S (7 real, 3 non-real): T_h must have 7 real and 3 non-real points (up to affine transformation). But an affine transformation z ↦ αz + β can change the real/non-real split. If α, β ∈ ℝ, the split is preserved. If α or β is non-real, the split changes.

Case: T_h affine-equivalent to S via a real affine map (α, β ∈ ℝ). Then T_h has 7 real and 3 non-real points. T_h has 7 non-negative real values (from R) and 3 values from W. The 3 values from W: (w_j - h)² for j = 1,2,3. For T_h to have exactly 7 real and 3 non-real: the 7 values from R are real (✓), and the 3 values from W must be non-real. (w_j - h)² is non-real iff Re(w_j) ≠ h. So we need Re(w_j) ≠ h for all j. If any Re(w_j) = h, then (w_j - h)² is real, and T_h would have 8+ real values, not matching 7.

Alternatively, if some (w_j - h)² is real and some (r_i - h)² ... no, all (r_i - h)² are real. So T_h has 7 real (from R) + (number of w_j with Re(w_j) = h) real values. For T_h to have 7 real (matching S via real affine map), we need all 3 (w_j - h)² to be non-real, i.e., Re(w_j) ≠ h for all j.

OK so with h real and Re(w_j) ≠ h for all j, T_h has 7 real (from R, all ≥ 0) and 3 non-real (from W). For T_h to be a real affine image of S: T_h = αS + β with α, β ∈ ℝ. Then:
- The 7 real values of T_h (= {(r-h)² : r ∈ R}) must be α · (7 real values of S) + β = αR + β.
- The 3 non-real values of T_h (= {(w-h)² : w ∈ W}) must be αW + β.

So {(r-h)² : r ∈ R} = αR + β and {(w-h)² : w ∈ W} = αW + β, with the same α, β.

The first condition: the set of squared distances from h to the real points, {(r-h)²}, is an affine image of R. The second: {(w-h)²} is the same affine image of W.

This is a strong condition. Let me think about what R and W satisfy this.

For the first condition with R = {cos(2πk/13) : k=0,...,6} and h = 0: {(r-0)² : r ∈ R} = {cos²(2πk/13) : k=0,...,6} = {(1+cos(4πk/13))/2 : k=0,...,6} = {1/2 + cos(4πk/13)/2 : k=0,...,6}. Since k ↦ 2k mod 13 permutes and cos identifies, {cos(4πk/13) : k=0,...,6} = R. So {(r)² : r ∈ R} = {1/2 + r/2 : r ∈ R} = (1/2)R + 1/2. So α = 1/2, β = 1/2. ✓ (This is just T₂(z) = 2z² - 1 rearranged: (z-0)² = (1/2)(2z²-1) + 1/2, so T_h = (1/2)·T₂(S) + 1/2... hmm, let me recheck. T₂(r) = 2r² - 1, so r² = (T₂(r) + 1)/2. Since T₂ permutes R, {r² : r ∈ R} = {(T₂(r)+1)/2 : r ∈ R} = {(s+1)/2 : s ∈ R} = R/2 + 1/2. Yes, α = 1/2, β = 1/2.)

Now the second condition: {(w-h)² : w ∈ W} = {w² : w ∈ W} = (
