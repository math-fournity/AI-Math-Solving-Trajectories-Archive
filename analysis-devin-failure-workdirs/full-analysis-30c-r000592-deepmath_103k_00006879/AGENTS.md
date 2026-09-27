# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $f:\mathbb{C}\to \mathbb{C}$ be an entire function. Suppose that for every $z\in \mathbb{C}$, there exists $n_z\in \mathbb{N}$ such that $f^{(n_z)}(z)=0$. Is $f$ necessarily a polynomial?       — 题目文本
#   Okay, so I need to figure out if an entire function f, which for every complex number z has some derivative of order n_z that's zero, must necessarily be a polynomial. Hmm. Let me start by recalling some complex analysis concepts.

First, an entire function is a function that's holomorphic everywhere on the complex plane. Polynomials are entire functions, and their derivatives eventually become zero once you differentiate enough times—specifically, the (deg f + 1)-th derivative is zero. So polynomials certainly satisfy the given condition because for each z, once you take enough derivatives, you get zero. The question is whether there are any non-polynomial entire functions that also have this property.

The problem states that for every z in ℂ, there exists a natural number n_z such that the n_z-th derivative of f at z is zero. So, for each point z, if we keep differentiating f, eventually at some order (depending on z), the derivative is zero. If f were a polynomial, this n_z would just be one more than the degree of the polynomial for all z. But here, n_z can vary with z.

Wait, but if f is a polynomial, then all its derivatives beyond the degree are zero everywhere, not just at individual points. So in that case, the n_z would be uniform for all z. But in the problem, n_z can depend on z. So maybe there's a function that isn't a polynomial but still has this property that for each z, some derivative vanishes at z.

I need to think about whether such a function exists. Let me recall some theorems. There's a theorem in complex analysis called the Identity Theorem, which says that if two holomorphic functions agree on a set with a limit point, then they agree everywhere. Also, there's something called the Taylor series expansion, which for entire functions converges everywhere on ℂ.

If f is entire, then around any point z, f can be expressed as its Taylor series. Suppose that for each z, there is some n_z such that f^{(n_z)}(z) = 0. Let me try to see what this implies.

Suppose we fix a point z. The Taylor series of f around z is ∑_{k=0}^∞ (f^{(k)}(z)/k!)(w - z)^k. If f^{(n_z)}(z) = 0, then the coefficient of (w - z)^{n_z} in this expansion is zero. But since the function is entire, the radius of convergence is infinite, so the series converges for all w.

But if at every z, there exists some n_z such that f^{(n_z)}(z) = 0, does that force all but finitely many coefficients in the Taylor expansion (around any point) to be zero? If so, then f would be a polynomial.

Alternatively, maybe there's a way to construct a non-polynomial entire function with this property. For example, consider a function that's a polynomial on different parts of the complex plane but glued together in some way. But entire functions are globally defined by their power series, so such piecewise definitions would have to agree on overlaps, which would force them to be a single polynomial.

Wait, another approach: Suppose f is not a polynomial. Then its Taylor series around any point has infinitely many non-zero coefficients. But if for each z, some derivative at z is zero, then each Taylor series around z has at least one zero coefficient. However, even if each Taylor series has some zero coefficient, that doesn't necessarily mean that beyond a certain point all coefficients are zero. For example, maybe different terms are zero for different z. But is it possible to have an entire function with infinitely many non-zero derivatives everywhere, yet at each individual point, one of the derivatives is zero?

Alternatively, consider the set where the k-th derivative is zero. For each k, the set Z_k = { z ∈ ℂ | f^{(k)}(z) = 0 } is a closed set (since f^{(k)} is continuous). The problem states that the union of all Z_k over k ∈ ℕ is the entire complex plane. So ℂ = ∪_{k=1}^∞ Z_k. By the Baire Category Theorem, since ℂ is a complete metric space, one of the Z_k must have non-empty interior. Therefore, there exists some k such that Z_k contains an open set. Then, by the Identity Theorem, since f^{(k)} is zero on an open set (which has limit points), f^{(k)} is identically zero on ℂ. Therefore, f is a polynomial of degree at most k-1.

Wait, that seems like a solid argument. Let me recap:

1. Assume f is entire and for every z ∈ ℂ, there exists n_z ∈ ℕ such that f^{(n_z)}(z) = 0.

2. Then ℂ = ∪_{k=1}^∞ Z_k, where Z_k = { z | f^{(k)}(z) = 0 }.

3. Each Z_k is closed (as the zero set of a continuous function).

4. By the Baire Category Theorem, in a complete metric space (like ℂ), a countable union of closed sets with empty interiors cannot cover the space. Therefore, at least one Z_k must have non-empty interior.

5. So there exists k ∈ ℕ and an open set U ⊆ Z_k. Hence, f^{(k)}(z) = 0 for all z ∈ U.

6. Since f^{(k)} is holomorphic (as f is entire) and is zero on an open set, by the Identity Theorem, f^{(k)} ≡ 0 on ℂ.

7. Therefore, f is a polynomial of degree at most k-1.

Therefore, f must be a polynomial.

So, the answer is yes, f is necessarily a polynomial.

But wait, let me check if there are any gaps here. The key step is applying the Baire Category Theorem. The complex plane is a complete metric space, and each Z_k is closed. If the union of all Z_k is the entire space, then at least one Z_k has non-empty interior. Therefore, that particular derivative is identically zero, which makes f a polynomial.

Yes, that seems right. So even though the condition is that for each z, some derivative vanishes at z, the Baire Category Theorem forces one derivative to vanish on an entire open set, hence everywhere. Therefore, the function is a polynomial.

Therefore, the answer should be yes, f must be a polynomial.

**Final Answer**
\boxed{Yes}
</think>

Given an entire function \( f: \mathbb{C} \to \mathbb{C} \) such that for every \( z \in \mathbb{C} \), there exists \( n_z \in \mathbb{N} \) with \( f^{(n_z)}(z) = 0 \), we need to determine if \( f \) is necessarily a polynomial.

1. **Entire Function and Derivatives**: An entire function is holomorphic everywhere on \( \mathbb{C} \). The condition implies that for each \( z \), some derivative of \( f \) at \( z \) is zero.

2. **Closed Sets**: For each \( k \in \mathbb{N} \), define \( Z_k = \{ z \in \mathbb{C} \mid f^{(k)}(z) = 0 \} \). Each \( Z_k \) is closed because \( f^{(k)} \) is continuous.

3. **Covering the Complex Plane**: The complex plane \( \mathbb{C} \) is the union of all \( Z_k \), i.e., \( \mathbb{C} = \bigcup_{k=1}^\infty Z_k \).

4. **Baire Category Theorem**: Since \( \mathbb{C} \) is a complete metric space, by the Baire Category Theorem, at least one \( Z_k \) must have a non-empty interior. Thus, there exists \( k \in \mathbb{N} \) and an open set \( U \subseteq Z_k \).

5. **Identity Theorem**: The function \( f^{(k)} \) is holomorphic and zero on the open set \( U \). By the Identity Theorem, \( f^{(k)} \equiv 0 \) on \( \mathbb{C} \).

6. **Conclusion**: Since \( f^{(k)} \equiv 0 \), \( f \) must be a polynomial of degree at most \( k-1 \).

Therefore, \( f \) is necessarily a polynomial.

\[
\boxed{Yes}
\]  — 标准解答
#   Let me think about this problem carefully.The question: Is it true that if $k$ is a prime knot, then the double branched cover $M(k)$ of $S^3$ along the knot $k$ is a prime 3-manifold?

First, let me check for answer leaks in the problem text. The problem text is just the question itself, no solutions or hints. Good.

Now let me think about this. This is a classical question in knot theory / 3-manifold topology.

Let me recall what's known. The double branched cover of $S^3$ along a knot $k$ is denoted $M(k)$ or $\Sigma_2(k)$.

The question is whether primality of the knot implies primality of the double branched cover.

Let me think about what's known:

1. If $k$ is a composite knot $k = k_1 \# k_2$, then $M(k) = M(k_1) \# M(k_2)$. This is a standard fact — the double branched cover of a connected sum is the connected sum of the double branched covers. So if $M(k)$ is prime, then $k$ must be prime (contrapositive: composite knot gives composite cover).

2. The converse: if $k$ is prime, is $M(k)$ prime?

This is the question. Let me think about whether there are counterexamples.

Actually, I recall that this is a subtle question. Let me think about it more carefully.

For torus knots, the double branched covers are Seifert fibered spaces, which are prime.

For hyperbolic knots, the double branched cover is hyperbolic (by Thurston's theorem — most double branched covers of hyperbolic knots are hyperbolic), and hyperbolic 3-manifolds are prime (in fact, irreducible and atoroidal).

Wait, but is the double branched cover of a hyperbolic knot always hyperbolic? Not necessarily. There are hyperbolic knots whose double branched covers are not hyperbolic. For instance, some 2-bridge knots have non-hyperbolic double branched covers... no wait, 2-bridge knots have lens space double branched covers, which are prime.

Hmm, let me think about this differently. The key question is whether there exists a prime knot $k$ such that $M(k)$ is a connected sum $M_1 \# M_2$ with both $M_i$ nontrivial.

If $M(k) = M_1 \# M_2$, then by the equivariant sphere theorem, we might be able to find an essential sphere that is equivariant with respect to the covering involution.

The covering involution $\tau$ on $M(k)$ has fixed point set the lift of the knot, which is a knot $\tilde{k}$ in $M(k)$. The quotient $M(k)/\tau = S^3$ and $\tilde{k}/\tau = k$.

If $M(k)$ is reducible, there's an essential sphere $S$ in $M(k)$. By the equivariant sphere theorem (Meeks-Yau, or the original equivariant sphere theorem), we can find an essential sphere that is equivariant, i.e., $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

Case 1: $\tau(S) = S$. Then $S$ is invariant. The sphere $S$ either contains the fixed set or is disjoint from it. If $S$ is disjoint from the fixed set $\tilde{k}$, then $S$ projects to a sphere in $S^3$ disjoint from $k$, which must be inessential (since $S^3$ is irreducible), contradiction. If $S$ intersects $\tilde{k}$, then $S \cap \tilde{k}$ consists of points, and $S$ projects to a sphere in $S^3$ intersecting $k$ in those points (mod 2). Actually, $S$ is invariant and intersects the fixed set in an even number of points... hmm, this needs more care.

Actually, let me reconsider. The equivariant sphere theorem says: if $M$ is a 3-manifold with an involution $\tau$ and $M$ is reducible, then there exists an essential sphere $S$ such that either $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

Case A: $\tau(S) \cap S = \emptyset$. Then $S$ and $\tau(S)$ are disjoint essential spheres. The projection of $S$ to $S^3 = M(k)/\tau$ is a 2-sphere (possibly with branch points). If $S$ is disjoint from the fixed set, it projects to a sphere in $S^3 \setminus k$, which bounds a ball (since $S^3$ is irreducible), and this lifts to show $S$ is inessential, contradiction. So $S$ must intersect the fixed set.

Hmm, actually if $S$ is disjoint from the fixed set $\tilde{k}$, then the projection $\pi(S)$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $\pi(S)$ bounds a ball $B$ in $S^3$. The ball $B$ either contains part of $k$ or not. If $B \cap k = \emptyset$, then $\pi^{-1}(B)$ is two balls bounded by $S$ and $\tau(S)$, so $S$ is inessential. If $B \cap k \neq \emptyset$, then... $k$ is a single arc inside $B$ (since $k$ is connected and $\partial B = \pi(S)$ separates). Actually $k \cap B$ could be multiple arcs. Hmm.

This is getting complicated. Let me recall the actual known result.

I believe the answer is YES — if $k$ is prime, then $M(k)$ is prime. This is a theorem. Let me recall who proved it.

Actually, I think this follows from the equivariant sphere theorem. The argument goes:

Suppose $M(k)$ is reducible. By the equivariant sphere theorem (for the involution $\tau$), there exists an essential sphere $S$ in $M(k)$ that is either $\tau$-invariant or disjoint from $\tau(S)$.

If $S$ is $\tau$-invariant and disjoint from the fixed set $\tilde{k}$: Then $S/\tau$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $S/\tau$ bounds a ball. This ball lifts to give that $S$ bounds a ball in $M(k)$, contradicting essentiality. (Need to be careful about the lifting, but it works out.)

If $S$ is $\tau$-invariant and intersects $\tilde{k}$: Then $S \cap \tilde{k}$ is nonempty. Since $\tau$ fixes $\tilde{k}$ pointwise and $\tau(S) = S$, the intersection $S \cap \tilde{k}$ is a finite set of points. The projection $S/\tau$ is a sphere in $S^3$ that intersects $k$ in $|S \cap \tilde{k}|/2$ points (since the involution identifies pairs... wait no, $\tau$ fixes $\tilde{k}$ pointwise, so each point of $S \cap \tilde{k}$ is a fixed point and projects to a distinct point of $k$). So $S/\tau$ is a sphere in $S^3$ intersecting $k$ in $n = |S \cap \tilde{k}|$ points.

Now, $S/\tau$ separates $S^3$ into two balls $B_1, B_2$. The knot $k$ is divided into $n$ arcs in each ball. For $S$ to be essential in $M(k)$, we need... the sphere $S$ separates $M(k)$ into two pieces, each containing part of $\tilde{k}$.

Actually, the sphere $S$ intersects $\tilde{k}$ in $n$ points. Since $\tilde{k}$ is a knot (connected), $S$ separates $M(k)$ into two pieces, and $\tilde{k}$ passes through $S$ $n$ times. For $S$ to be essential, neither piece can be a ball (with no essential content).

The projection: $S/\tau$ separates $S^3$ into two balls $B_1, B_2$, and $k \cap B_i$ consists of $n/2$ arcs (if $n$ is even) or... wait, $n$ must be even since $\tilde{k}$ is a double cover of $k$ and $S$ is $\tau$-invariant. Actually, $\tilde{k} \to k$ is a 2-to-1 cover branched at... no, $\tilde{k}$ is the preimage of $k$ in the branched cover. The branched cover is branched along $k$, so $\tilde{k}$ maps 1-to-1 onto $k$ (each point of $k$ has one preimage on $\tilde{k}$, which is a fixed point of $\tau$). So $|S \cap \tilde{k}| = |S/\tau \cap k|$.

So $S/\tau$ intersects $k$ in $n$ points, dividing $k$ into $n$ arcs, split between $B_1$ and $B_2$. If $n$ is even, each ball gets $n/2$ arcs. If $n$ is odd... but $n$ must be even because $\tilde{k}$ is a closed curve crossing $S$ an even number of times (since $S$ separates and $\tilde{k}$ is a closed loop, it must cross $S$ an even number of times). So $n$ is even, and each $B_i$ contains $n/2$ arcs of $k$.

Now, $S$ is essential in $M(k)$. The two sides of $S$ in $M(k)$ project to $B_1$ and $B_2$ (each is a double branched cover of $B_i$ along the arcs $k \cap B_i$). For $S$ to be essential, at least one of these double branched covers must not be a ball.

The double branched cover of a ball along $n/2$ properly embedded arcs (a tangle) is a ball if and only if the tangle is "trivial" in some sense. Actually, the double branched cover of a ball along a rational tangle is a solid torus, not a ball. The double branched cover along the trivial tangle (two unknotted arcs) is... let me think. The double branched cover of $B^3$ along two unknotted, unlinked arcs is $S^1 \times D^2$ (a solid torus). Hmm, actually no.

Let me reconsider. The double branched cover of $B^3$ along $n/2$ arcs. If $n/2 = 0$ (no arcs), the double cover of a ball is two balls, but we're taking the branched cover... if there are no branch points, the double cover of a ball is two balls. But $S$ separates $M(k)$ into two pieces, each being a double branched cover of $B_i$ along $k \cap B_i$.

If $k \cap B_i = \emptyset$ (i.e., $n/2 = 0$ for one side), then that side is the double (unbranched) cover of $B_i$, which is two copies of $B_i$ if $B_i$ is a ball. But that would mean $S$ bounds two balls on that side, making $S$ inessential. So for $S$ to be essential, both sides must have $k \cap B_i \neq \emptyset$, meaning $n \geq 2$ and each side has at least 1 arc.

If each side has at least 1 arc, then $S/\tau$ is a sphere in $S^3$ intersecting $k$ in at least 2 points, with $k$ having arcs on both sides. This means $S/\tau$ is a "swallow-follow" sphere or a decomposing sphere for $k$.

If $k$ is prime, then any such sphere must be a "trivial" decomposing sphere — one side contains a trivial arc (an unknotted arc in a ball). But does that make $S$ inessential?

Hmm, let me think about this more carefully. If $k$ is prime, then for any sphere $S'$ in $S^3$ intersecting $k$ transversely in 2 points, one of the two tangles $(B_i, k \cap B_i)$ is trivial (i.e., the arc is unknotted in the ball).

If $(B_1, k \cap B_1)$ is a trivial tangle (one unknotted arc), then the double branched cover of $B_1$ along this arc is a solid torus (I think). Wait, let me reconsider.

The double branched cover of a ball along a single unknotted arc: The ball $B^3$ with a properly embedded unknotted arc. The double branched cover... Consider $B^3$ as the lower hemisphere of $S^3$, and the arc as a diameter. The double branched cover of $S^3$ along an unknotted circle is $S^3$ (since the unknot has double branched cover $S^3$). If we split $S^3$ into two balls along the equatorial sphere (intersecting the unknot in 2 points), each ball contains one unknotted arc, and the double branched cover of $S^3 = $ double branched cover of ball 1 $\cup$ double branched cover of ball 2, glued along their boundaries. Since the total is $S^3$ and by symmetry, each piece is a ball. So the double branched cover of a ball along a single unknotted arc is a ball!

OK so if $(B_1, k \cap B_1)$ is a trivial tangle with one unknotted arc, its double branched cover is a ball. Then $S$ bounds a ball on that side, so $S$ is inessential. Contradiction.

But what if $n > 2$? Then each side has $n/2 > 1$ arcs. Can $k$ still be prime? Yes — a prime knot can have a sphere intersecting it in more than 2 points where neither side is a trivial 2-strand tangle. The definition of prime knot only requires that there's no sphere intersecting $k$ in exactly 2 points that splits $k$ into two non-trivial tangles.

So the argument above only works for $n = 2$. For $n > 2$, we need a different approach.

Hmm, so the equivariant sphere theorem gives us a sphere $S$ with $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$, but $S$ might intersect $\tilde{k}$ in more than 2 points.

Let me reconsider. Maybe we should use a different approach.

Actually, I think the key result is due to the equivariant sphere theorem combined with the fact that we can choose $S$ to intersect the fixed set minimally.

Let me look at this from a different angle. There's a theorem by Heil (1970s?) or maybe it's attributed to others.

Actually, I recall now. The result that "if $k$ is prime then $M(k)$ is prime" is indeed true, and it's a consequence of the equivariant sphere theorem. The proof handles the general case.

Let me think about the case $\tau(S) \cap S = \emptyset$ more carefully.

If $\tau(S) \cap S = \emptyset$: Then $S$ and $\tau(S)$ are disjoint. Consider the projection $\pi: M(k) \to S^3$. The image $\pi(S)$ is a sphere in $S^3$ (since $\tau(S) \neq S$, the projection is 2-to-1 on $S$, so $\pi(S)$ is a sphere). This sphere $\pi(S)$ intersects $k$ in some points.

If $S \cap \tilde{k} = \emptyset$, then $\pi(S) \cap k = \emptyset$, so $\pi(S)$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $\pi(S)$ bounds a ball $B$ in $S^3$. The preimage $\pi^{-1}(B)$ is either one or two pieces. If $B \cap k = \emptyset$, then $\pi^{-1}(B)$ is two balls (double cover of a ball), and $S$ bounds one of them, so $S$ is inessential. If $B \cap k \neq \emptyset$... but we said $\pi(S) \cap k = \emptyset$, so $k$ is entirely inside or outside $B$. If $k \subset B$, then $\pi^{-1}(B) = M(k) \setminus \pi^{-1}(\overline{S^3 \setminus B})$, and $\pi^{-1}(B)$ is the double branched cover of $B$ along $k$, which is $M(k)$ minus a ball pair... this doesn't immediately give inessentiality. Hmm, but $S$ is essential and $\tau(S)$ is also essential and they're disjoint. The region between $S$ and $\tau(S)$ projects to the region between $\pi(S)$ and itself (which is $B$ or $\overline{S^3 \setminus B}$). Actually, $\pi^{-1}(\pi(S)) = S \cup \tau(S)$, and $\pi^{-1}(B)$ is the region between $S$ and $\tau(S)$ (if $k \subset B$) or the two outer regions. This is getting complicated.

Let me try a cleaner approach. I think the standard proof goes like this:

**Theorem**: If $k$ is a prime knot in $S^3$, then the double branched cover $\Sigma_2(k)$ is a prime 3-manifold.

**Proof sketch**: Suppose $\Sigma_2(k)$ is reducible. Let $\tau$ be the covering involution. By the equivariant sphere theorem, there exists an essential sphere $S$ in $\Sigma_2(k)$ such that either (i) $\tau(S) = S$ or (ii) $\tau(S) \cap S = \emptyset$.

**Case (ii)**: $\tau(S) \cap S = \emptyset$. Then $S$ and $\tau(S)$ are disjoint essential spheres. The sphere $S$ separates $\Sigma_2(k)$ into two pieces. Since $\tau(S)$ is disjoint from $S$, $\tau(S)$ lies entirely in one piece, say the piece $X$ bounded by $S$. Then $X$ contains an essential sphere $\tau(S)$, so $X$ is not a ball. But also, the other piece $Y$ (bounded by $S$ on the other side) must not be a ball (since $S$ is essential). Now, $\tau(Y)$ is the piece on the other side of $\tau(S)$ from $X$... hmm, this is getting complicated.

Actually, let me think about it differently. In case (ii), $S \cup \tau(S)$ consists of two disjoint spheres. They divide $\Sigma_2(k)$ into three pieces (or two if one sphere is nested). The projection to $S^3$ gives a sphere $\pi(S)$ (since $S$ and $\tau(S)$ project to the same sphere). This sphere $\pi(S)$ in $S^3$ intersects $k$ in some number of points.

If $\pi(S) \cap k = \emptyset$: $\pi(S)$ bounds a ball $B$ in $S^3$ (irreducibility of $S^3$). If $k \cap B = \emptyset$, then $\pi^{-1}(B)$ is two disjoint balls bounded by $S$ and $\tau(S)$, so both $S$ and $\tau(S)$ are inessential, contradiction. If $k \subset B$, then $\pi^{-1}(B) = \Sigma_2(k) \setminus \pi^{-1}(\overline{S^3 \setminus B})$, and $\pi^{-1}(\overline{S^3 \setminus B})$ is two balls (double cover of a ball with no branch points). So $\Sigma_2(k) = \pi^{-1}(B) \cup \text{(two balls)}$, meaning $\Sigma_2(k) = \pi^{-1}(B)$. But $\pi^{-1}(B)$ is bounded by $S \cup \tau(S)$, and it's the double branched cover of $B$ along $k$. The two balls $\pi^{-1}(\overline{S^3 \setminus B})$ are glued to $\pi^{-1}(B)$ along $S$ and $\tau(S)$. So $\Sigma_2(k)$ is obtained from $\pi^{-1}(B)$ by gluing two balls. This means $S$ and $\tau(S)$ each bound balls in $\Sigma_2(k)$ (the glued balls), so they're inessential. Contradiction.

So in case (ii) with $\pi(S) \cap k = \emptyset$, we get a contradiction.

If $\pi(S) \cap k \neq \emptyset$: Then $S \cap \tilde{k} \neq \emptyset$ (since points of $k$ on $\pi(S)$ correspond to fixed points on $S$ or $\tau(S)$). Actually, $\pi(S) \cap k$ consists of points where $S$ (or $\tau(S)$) intersects $\tilde{k}$. Since $\pi|_{\tilde{k}}: \tilde{k} \to k$ is a homeomorphism (1-to-1), $|\pi(S) \cap k| = |(S \cup \tau(S)) \cap \tilde{k}| = |S \cap \tilde{k}| + |\tau(S) \cap \tilde{k}| = 2|S \cap \tilde{k}|$ (by symmetry). So $|S \cap \tilde{k}| = |\pi(S) \cap k|/2$.

The sphere $\pi(S)$ intersects $k$ in $m = |\pi(S) \cap k|$ points, dividing $k$ into $m$ arcs split between the two balls bounded by $\pi(S)$. Since $S$ is essential, neither side of $S$ in $\Sigma_2(k)$ is a ball.

Hmm, I think this case is harder to handle directly. Let me look for a different approach.

Actually, maybe I should think about this problem differently. Let me recall: is the statement actually TRUE?

I believe the answer is **yes**, and this is a known result. Let me try to recall the reference. I think it might be due to the equivariant sphere theorem, and the result might be attributed to Waldhausen or to the work of Meeks-Yau on equivariant spheres.

Actually, let me reconsider. I recall that for the double branched cover, the result that prime knot implies prime double branched cover is indeed true. The proof uses the equivariant sphere theorem.

Let me try to write a cleaner proof.

**Proof**:

Suppose $k$ is prime but $M = \Sigma_2(k)$ is reducible. Let $\tau: M \to M$ be the covering involution with fixed set $\tilde{k}$ (the lift of $k$). By the Equivariant Sphere Theorem (Meeks-Yau / Meeks-Simon-Yau), there exists an essential 2-sphere $S \subset M$ such that either $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

**Case 1: $\tau(S) \cap S = \emptyset$.**

The sphere $S$ separates $M$ into two components $M_1$ and $M_2$. Since $\tau(S) \neq S$ and $\tau(S) \cap S = \emptyset$, $\tau(S) \subset M_i$ for some $i$. WLOG $\tau(S) \subset M_1$. Then $\tau(M_2) \subset M_1$ (since $\tau(S) = \partial \tau(M_2) \subset M_1$). So $M_1$ contains both $\tau(S)$ and $\tau(M_2)$, and $M_1 \setminus \tau(M_2)$ is the region between $S$ and $\tau(S)$.

The projection $\pi: M \to S^3$ maps $S$ and $\tau(S)$ to the same sphere $\Sigma = \pi(S) \subset S^3$. The sphere $\Sigma$ separates $S^3$ into two balls $B_1, B_2$.

If $\Sigma \cap k = \emptyset$: Then $k$ lies in one ball, say $B_1$. The preimage $\pi^{-1}(B_2)$ is the double (unbranched) cover of a ball, which is two disjoint balls. These two balls are bounded by $S$ and $\tau(S)$, so both $S$ and $\tau(S)$ bound balls in $M$, contradicting their essentiality.

If $\Sigma \cap k \neq \emptyset$: Let $m = |\Sigma \cap k|$. Then $m \geq 1$. Since $\tilde{k}$ is a closed curve and $S$ separates $M$, $\tilde{k}$ crosses $S$ an even number of times, so $|S \cap \tilde{k}|$ is even. Similarly for $\tau(S)$. We have $m = |S \cap \tilde{k}| + |\tau(S) \cap \tilde{k}| = 2|S \cap \tilde{k}|$, so $m$ is even, $m \geq 2$.

Now, $\Sigma$ intersects $k$ in $m \geq 2$ points. The ball $B_1$ contains $m_1$ arcs of $k$ and $B_2$ contains $m_2$ arcs, with $m_1 + m_2 = m$. The preimage $\pi^{-1}(B_i)$ is the double branched cover of $B_i$ along $m_i$ arcs, which is a 3-manifold with boundary $S \cup \tau(S)$ (two copies of $\Sigma$, i.e., two spheres).

Hmm wait, $\pi^{-1}(\Sigma) = S \cup \tau(S)$, and $\pi^{-1}(B_i)$ is bounded by $S \cup \tau(S)$. But $\pi^{-1}(B_i)$ is connected (it's the double branched cover of a ball along arcs, which is connected as long as there's at least one arc, or if there are no arcs, it's two balls). If $m_i = 0$, $\pi^{-1}(B_i)$ is two balls, and $S, \tau(S)$ each bound a ball, contradiction. If $m_i \geq 1$, $\pi^{-1}(B_i)$ is connected with boundary $S \cup \tau(S)$.

Now, $M = \pi^{-1}(B_1) \cup \pi^{-1}(B_2)$, glued along $S \cup \tau(S)$. The sphere $S$ is essential in $M$, so $S$ doesn't bound a ball in $M$. But $S$ is part of the boundary of both $\pi^{-1}(B_1)$ and $\pi^{-1}(B_2)$.

For $S$ to be essential, neither $\pi^{-1}(B_1)$ nor $\pi^{-1}(B_2)$ can be a ball with boundary $S$ (but their boundaries are $S \cup \tau(S)$, two spheres, so neither is a ball anyway, unless one sphere caps off).

Hmm, this is getting complicated. Let me think about whether we can reduce to the $m = 2$ case.

Actually, I think the key insight is: we can choose $S$ to minimize $|S \cap \tilde{k}|$. Among all essential equivariant spheres (either invariant or disjoint from their image), choose one minimizing the intersection with $\tilde{k}$.

If $S$ is $\tau$-invariant and $|S \cap \tilde{k}| = 2$: Then $\pi(S) = \Sigma$ intersects $k$ in 2 points. Since $k$ is prime, one of the two tangles is trivial. The double branched cover of a trivial tangle (ball with one unknotted arc) is a ball. So $S$ bounds a ball on one side, contradicting essentiality.

If $S$ is $\tau$-invariant and $|S \cap \tilde{k}| = 2n > 2$: Can we find an innermost disk argument to reduce? Consider $S \cap \tilde{k}$, which is $2n$ points. The sphere $S$ separates $M$ into $X$ and $Y$. The knot $\tilde{k}$ passes through $S$ $2n$ times, so $\tilde{k} \cap X$ consists of $n$ arcs and $\tilde{k} \cap Y$ consists of $n$ arcs (since $\tilde{k}$ is a closed curve crossing $S$ $2n$ times).

Now, $\pi(S) = \Sigma$ intersects $k$ in $2n$ points (since $\tau$ fixes $\tilde{k}$ pointwise, each point of $S \cap \tilde{k}$ projects to a distinct point of $k \cap \Sigma$). So $\Sigma$ intersects $k$ in $2n$ points, dividing $k$ into $2n$ arcs, $n$ in each ball $B_1, B_2$.

Hmm, but $k$ being prime doesn't directly tell us about spheres intersecting $k$ in more than 2 points.

I think the right approach is to use the fact that we can isotope $S$ to reduce intersections. Let me think about innermost circle arguments.

Consider the projection $\pi|_S: S \to \Sigma$. This is a 2-to-1 branched cover (branched at the $2n$ points $S \cap \tilde{k}$), since $S$ is $\tau$-invariant. Actually, $\tau|_S$ is an involution on $S$ with fixed points $S \cap \tilde{k}$ (an even number $2n$). The quotient $S/\tau = \Sigma$ is a sphere.

Now, the knot $k$ intersects $\Sigma$ in $2n$ points. The sphere $\Sigma$ bounds two balls $B_1, B_2$ in $S^3$, with $k \cap B_i$ consisting of $n$ arcs each.

Since $k$ is prime, can we find a sub-sphere of $\Sigma$ that intersects $k$ in exactly 2 points and splits off a trivial tangle? Not directly, because primality is about spheres intersecting $k$ in 2 points, not about arbitrary configurations.

Hmm, let me think about this differently. Maybe I should use the fact that $k$ being prime means $S^3 \setminus N(k)$ is irreducible (where $N(k)$ is a tubular neighborhood). Actually, that's not quite right either. $k$ being prime means there's no decomposing sphere (a sphere intersecting $k$ in 2 points that splits $k$ into two non-trivial tangles). The complement $S^3 \setminus \nu(k)$ being irreducible is equivalent to $k$ being non-split, not prime.

Wait, actually: $k$ is prime iff $S^3 \setminus \nu(k)$ is irreducible AND $k$ is non-trivial. No, that's not right either. A knot $k$ is prime if $k = k_1 \# k_2$ implies $k_1$ or $k_2$ is the unknot. The exterior $E(k) = S^3 \setminus \nu(k)$ is irreducible for any non-split knot (prime or not). The difference is about essential annuli or something else.

Actually, for knots: $k$ is prime iff $E(k)$ is irreducible and $E(k)$ contains no essential annulus with boundary on $\partial E(k)$ that is not boundary-parallel. Hmm, I don't think that's exactly right either.

Let me reconsider. A knot $k$ is prime if whenever $k = k_1 \# k_2$, one of $k_i$ is the unknot. Equivalently, there is no 2-sphere in $S^3$ intersecting $k$ transversely in exactly 2 points such that both tangles $(B_i, k \cap B_i)$ are non-trivial.

OK so I think the proof needs to handle the case $|S \cap \tilde{k}| > 2$ more carefully. Let me think about whether we can always reduce to the 2-point case.

Alternative approach: Maybe use the fact that if $M(k)$ is reducible, then $k$ can be written as a connected sum, contradicting primality.

Here's the idea: If $M(k) = M_1 \# M_2$, then the covering involution $\tau$ on $M(k)$ restricts to... well, by the equivariant sphere theorem, we can find the decomposing sphere to be equivariant. Then the projection gives a decomposing sphere for $k$, showing $k$ is composite.

Let me be more precise. Suppose $M(k)$ is reducible. By the equivariant sphere theorem, there exists an essential sphere $S$ with $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

**Subcase 1a: $\tau(S) = S$ and $S \cap \tilde{k} = \emptyset$.**

Then $\pi(S) = \Sigma$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $\Sigma$ bounds a ball $B$. If $B \cap k = \emptyset$, then $\pi^{-1}(B)$ is two balls (unbranched double cover), and $S$ bounds a ball, contradicting essentiality. If $k \subset B$, then $\pi^{-1}(\overline{S^3 \setminus B})$ is two balls, and $S$ bounds a ball (one of the two), contradicting essentiality. So this subcase is impossible.

**Subcase 1b: $\tau(S) = S$ and $S \cap \tilde{k} \neq \emptyset$.**

Let $|S \cap \tilde{k}| = 2n \geq 2$. The sphere $\Sigma = \pi(S)$ intersects $k$ in $2n$ points.

Now I want to show that we can find a sphere intersecting $k$ in exactly 2 points that decomposes $k$ non-trivially.

Consider the $2n$ points $p_1, \ldots, p_{2n} = \Sigma \cap k$ on the sphere $\Sigma$. These divide $k$ into $2n$ arcs. The ball $B_1$ contains $n$ of these arcs (forming a tangle $T_1$) and $B_2$ contains the other $n$ arcs (tangle $T_2$).

The double branched cover of $(B_i, T_i)$ is one side of $S$ in $M(k)$. Since $S$ is essential, neither side is a ball. The double branched cover of a ball along a tangle is a ball if and only if the tangle is "trivial" in a specific sense.

Hmm, but I need to connect this to the primality of $k$. Let me think about whether we can find a 2-point sphere from the $2n$-point sphere.

Consider the $n$ arcs of $T_1$ in $B_1$. If $n \geq 2$, consider two arcs $\alpha, \beta$ of $T_1$. There exists a disk $D$ in $B_1$ with $\partial D$ consisting of $\alpha$, $\beta$, and two arcs on $\partial B_1 = \Sigma$ connecting the endpoints of $\alpha$ and $\beta$. (This is because the arcs are properly embedded in the ball.) Using this disk, we can do surgery on $\Sigma$ to get a new sphere $\Sigma'$ that intersects $k$ in fewer points.

Actually, this is the standard innermost arc argument. Let me think about it more carefully.

The $2n$ points on $\Sigma$ divide $\Sigma$ into $2n$ arcs. The knot $k$ consists of $2n$ arcs, $n$ in $B_1$ and $n$ in $B_2$. Consider the arcs in $B_1$: they connect pairs of the $2n$ points on $\Sigma$. This gives a pairing of the $2n$ points.

Now, consider an arc $\alpha$ of $k$ in $B_1$ connecting points $p_i$ and $p_j$ on $\Sigma$. Together with an arc $\gamma$ on $\Sigma$ connecting $p_i$ and $p_j$, $\alpha \cup \gamma$ forms a loop. If we can find a disk in $B_1$ bounded by $\alpha \cup \gamma$ (for some $\gamma$ on $\Sigma$), we can use it to surger $\Sigma$ and reduce the number of intersection points.

Actually, since $B_1$ is a ball and $\alpha$ is a properly embedded arc, there always exists a disk $D$ in $B_1$ with $\alpha \subset \partial D$ and $\partial D \cap \Sigma$ being an arc $\gamma$ on $\Sigma$ connecting $p_i$ and $p_j$. We can choose $D$ to be innermost (intersecting $k$ minimally). If $D \cap k = \alpha$ (i.e., $D$ intersects $k$ only in $\alpha$), then we can surger $\Sigma$ along $D$: replace the arc $\gamma$ on $\Sigma$ with $\alpha$ to get a new sphere $\Sigma'$ that intersects $k$ in $2n - 2$ points (we've removed $p_i$ and $p_j$ from the intersection).

But this new sphere $\Sigma'$ might not be equivariantly liftable, and the corresponding sphere in $M(k)$ might not be essential.

I think this approach is getting too complicated for me to work out in full detail. Let me try to recall the actual theorem and its proof.

I believe the result is:

**Theorem** (folklore / equivariant sphere theorem): If $k$ is a prime knot, then $\Sigma_2(k)$ is prime.

And the proof goes through the equivariant sphere theorem, handling the cases as I outlined, with the key step being that an equivariant essential sphere projects to a decomposing sphere for $k$.

Let me try to think about this more carefully for the case $\tau(S) = S$ and $|S \cap \tilde{k}| = 2n$.

Actually, I think the key point is this: we choose $S$ to be an equivariant essential sphere minimizing $|S \cap \tilde{k}|$. Then we show $|S \cap \tilde{k}| = 2$ (i.e., $n = 1$), which gives a decomposing sphere for $k$, contradicting primality.

Why must $n = 1$? Suppose $n \geq 2$. Then $\Sigma = \pi(S)$ intersects $k$ in $2n \geq 4$ points. Consider the $n$ arcs of $k$ in $B_1$. Take an innermost pair: two consecutive points $p_i, p_{i+1}$ on $\Sigma$ (in the cyclic order) that are connected by an arc $\alpha$ of $k$ in $B_1$. "Consecutive" means the arc $\gamma$ on $\Sigma$ from $p_i$ to $p_{i+1}$ contains no other points of $\Sigma \cap k$.

The arc $\alpha$ in $B_1$ and the arc $\gamma$ on $\Sigma$ bound a disk $D$ in $B_1$ (since $B_1$ is a ball). We can choose $D$ to be innermost, so $D \cap k = \alpha$.

Now surger $\Sigma$ along $D$: replace $\gamma \subset \Sigma$ with $\alpha$ to get a new sphere $\Sigma'$. Then $\Sigma' \cap k = (\Sigma \cap k) \setminus \{p_i, p_{i+1}\}$, so $|\Sigma' \cap k| = 2n - 2$.

The sphere $\Sigma'$ bounds two balls $B_1', B_2'$ in $S^3$. One of them, say $B_1'$, is contained in $B_1$ (roughly $B_1$ minus a neighborhood of $D$), and $B_2'$ contains $B_2$ plus a neighborhood of $D$.

Now, does $\Sigma'$ lift to an equivariant sphere in $M(k)$ with fewer intersections with $\tilde{k}$? The sphere $\Sigma'$ intersects $k$ in $2(n-1)$ points. The double branched cover of $S^3$ along $k$ has a sphere $\tilde{S}'$ lying over $\Sigma'$ (the preimage $\pi^{-1}(\Sigma')$ is a sphere if $\Sigma'$ is equivariant... but $\Sigma'$ might not be equivariant in the right sense).

Hmm, actually $\pi^{-1}(\Sigma')$ is always a sphere (since $\Sigma'$ is a sphere in $S^3$ and the branched cover is 2-to-1). Wait, no. $\pi^{-1}(\Sigma')$ is a double branched cover of $\Sigma'$ branched at $\Sigma' \cap k$. If $|\Sigma' \cap k| = 2(n-1)$, then $\pi^{-1}(\Sigma')$ is a double branched cover of $S^2$ branched at $2(n-1)$ points. If $n-1 = 0$, this is two spheres (unbranched double cover of $S^2$). If $n-1 \geq 1$, this is a connected surface: a double branched cover of $S^2$ branched at $2m$ points (for $m \geq 1$) is a closed surface of genus... well, by Riemann-Hurwitz, $\chi(\tilde{\Sigma}) = 2\chi(\Sigma) - 2m = 4 - 2m$. For $m = 1$: $\chi = 2$, so it's a sphere. For $m = 2$: $\chi = 0$, so it's a torus. For $m \geq 3$: $\chi < 0$, higher genus.

So if $n = 2$ (so $n - 1 = 1$), $\pi^{-1}(\Sigma')$ is a sphere with $|\pi^{-1}(\Sigma') \cap \tilde{k}| = 2$, which is an equivariant sphere with fewer intersections. If $n \geq 3$, $\pi^{-1}(\Sigma')$ is not a sphere, so this doesn't directly give us a sphere.

So the surgery argument only reduces from $n = 2$ to $n = 1$. For $n \geq 3$, we get a higher-genus surface, not a sphere.

Hmm, so this approach doesn't fully work. Let me think differently.

Maybe we need to use a different minimality condition. Instead of minimizing $|S \cap \tilde{k}|$ among equivariant essential spheres, we should minimize among all essential spheres (not necessarily equivariant) and then apply the equivariant sphere theorem.

Actually, wait. Let me reconsider the equivariant sphere theorem. The theorem says: if $M$ is orientable and $\tau$ is an involution, and $M$ is reducible, then there exists a collection of disjoint essential spheres $\{S_1, \ldots, S_k\}$ such that the collection is $\tau$-invariant (as a set) and the spheres are pairwise disjoint and non-parallel, and this collection is maximal. Moreover, we can arrange that each $S_i$ is either $\tau$-invariant or $\tau(S_i) = S_j$ for some $j \neq i$.

Actually, the equivariant sphere theorem as usually stated: If $M$ is a reducible 3-manifold and $\tau$ is an involution on $M$, then $M$ contains an essential sphere $S$ such that either $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

But there's a stronger version: we can find a maximal system of disjoint non-parallel essential spheres that is $\tau$-invariant as a set.

Let me try a different approach. Let me think about what happens in Case 2.

**Case 2: $\tau(S) \cap S = \emptyset$.**

$S$ and $\tau(S)$ are disjoint essential spheres. They cobound a region $R$ in $M$ (the region between them), and $M = R \cup X \cup Y$ where $X$ is on the other side of $S$ from $R$ and $Y$ is on the other side of $\tau(S)$ from $R$. Note $\tau(X) = Y$ and $\tau(R) = R$ (with $\tau$ swapping $S$ and $\tau(S)$).

The projection $\pi(S) = \pi(\tau(S)) = \Sigma$, a sphere in $S^3$. The region $R$ projects to one of the two balls bounded by $\Sigma$, say $B_1$, and $X \cup Y$ projects to the other ball $B_2$. (Or vice versa.) Since $\tau$ swaps $X$ and $Y$ and $\tau(R) = R$, we have $\pi(R) = B_1$ (a ball) and $\pi(X \cup Y) = B_2$ (a ball), with $\pi|_R: R \to B_1$ a double branched cover (branched along $k \cap B_1$) and $\pi|_{X \cup Y}: X \cup Y \to B_2$ a double branched cover (branched along $k \cap B_2$).

If $k \cap B_1 = \emptyset$: $R$ is the double unbranched cover of a ball, which is two balls. But $R$ is bounded by $S \cup \tau(S)$ (two spheres), so $R$ being two balls means $S$ and $\tau(S)$ each bound a ball, contradicting essentiality.

If $k \cap B_2 = \emptyset$: $X \cup Y$ is the double unbranched cover of a ball, which is two balls $X$ and $Y$. So $S$ bounds the ball $X$ and $\tau(S)$ bounds the ball $Y$, contradicting essentiality.

So both $k \cap B_1$ and $k \cap B_2$ are nonempty. Let $|k \cap B_1| = m_1$ arcs and $|k \cap B_2| = m_2$ arcs, with $m_1 + m_2 = m = |\Sigma \cap k|$ and $m_1, m_2 \geq 1$.

Now, $R$ is the double branched cover of $B_1$ along $m_1$ arcs, and $X \cup Y$ is the double branched cover of $B_2$ along $m_2$ arcs. Since $S$ is essential, $X$ is not a ball (and $Y = \tau(X)$ is not a ball). Since $\tau(S)$ is essential, $R$ is not a ball (well, $R$ has two boundary components, so it can't be a ball anyway).

Hmm, for $S$ to be essential, we need $X$ to not be a ball. $X$ is one component of the double branched cover of $B_2$ along $m_2$ arcs. If $m_2 = 1$ (one arc in $B_2$), the double branched cover of a ball along one arc is a ball (as we computed earlier). So $X$ would be a ball, contradicting essentiality. So $m_2 \geq 2$.

Similarly, $m_1 \geq 1$ (we already knew this). But we also need $R$ to not be a product (otherwise $S$ and $\tau(S)$ would be parallel, which might still be OK for essentiality... actually, parallel essential spheres are still essential).

So $m_2 \geq 2$, meaning $B_2$ contains at least 2 arcs of $k$. And $m_1 \geq 1$.

Now, $\Sigma$ is a sphere in $S^3$ intersecting $k$ in $m = m_1 + m_2$ points, with $m_1 \geq 1$ arcs on one side and $m_2 \geq 2$ arcs on the other.

Can we use this to show $k$ is composite? Not directly, because $\Sigma$ intersects $k$ in more than 2 points.

OK, I think I need to take a step back and think about whether the result is actually true.

Let me consider potential counterexamples. Are there prime knots whose double branched covers are reducible?

For 2-bridge knots: double branched covers are lens spaces, which are prime (irreducible). ✓

For torus knots: double branched covers are Seifert fibered spaces over $S^2$ with 3 exceptional fibers, which are irreducible. ✓

For hyperbolic knots: the double branched cover is often hyperbolic (hence irreducible), but not always. However, even if not hyperbolic, could it be reducible?

Actually, I recall that for alternating knots, the double branched cover is irreducible. This follows from the work of Menasco or from the fact that alternating knots have essential checkerboard surfaces whose lifts give essential surfaces.

More generally, I believe the result is true for all prime knots. Let me search my memory for the precise theorem.

I think the key theorem is:

**Theorem**: Let $k$ be a knot in $S^3$. Then $k$ is prime if and only if $\Sigma_2(k)$ is prime.

The "only if" direction (prime knot → prime double branched cover) is what we need to prove. The "if" direction is easy (if $k = k_1 \# k_2$, then $\Sigma_2(k) = \Sigma_2(k_1) \# \Sigma_2(k_2)$).

For the "only if" direction, I believe the proof uses the equivariant sphere theorem. Let me try to make the argument work.

The issue was handling the case $|S \cap \tilde{k}| > 2$. Let me think about this more carefully.

Actually, maybe I should think about it in terms of the knot complement. The double branched cover $\Sigma_2(k)$ can be obtained by taking the double branched cover of $S^3$ along $k$. There's a relationship between $\Sigma_2(k)$ and the knot complement $E(k) = S^3 \setminus \nu(k)$.

Specifically, $\Sigma_2(k) \setminus \nu(\tilde{k})$ is the double cover of $E(k)$. The double cover of $E(k)$ is determined by the mod 2 linking number with $k$, which is the unique nontrivial homomorphism $\pi_1(E(k)) \to \mathbb{Z}/2$.

If $k$ is prime, then $E(k)$ is irreducible (this is true for any non-split knot). The double cover of an irreducible 3-manifold is... not necessarily irreducible. Hmm.

Actually, the double cover of $E(k)$ might be reducible even if $E(k)$ is irreducible. For example, the double cover of a knot complement can be reducible for certain knots.

But we need $\Sigma_2(k)$ to be prime, which is stronger than $\Sigma_2(k) \setminus \nu(\tilde{k})$ being irreducible (since we also need to cap off with the solid torus $\nu(\tilde{k})$).

Let me think about this differently. $\Sigma_2(k) = (\text{double cover of } E(k)) \cup_{\partial} \nu(\tilde{k})$, where $\nu(\tilde{k})$ is a solid torus. The double cover of $E(k)$ has boundary a torus $T$, and we glue in a solid torus to get $\Sigma_2(k)$.

If $\Sigma_2(k)$ is reducible, there's an essential sphere $S$ in $\Sigma_2(k)$. We can isotope $S$ to intersect $\nu(\tilde{k})$ in a minimal number of meridian disks. Then $S \cap (\Sigma_2(k) \setminus \nu(\tilde{k}))$ is a planar surface in the double cover of $E(k)$.

Hmm, this is also getting complicated. Let me try yet another approach.

Let me look at this from the perspective of the equivariant sphere theorem more carefully, and try to handle the general case.

**Claim**: We can choose the equivariant essential sphere $S$ such that $|S \cap \tilde{k}| = 2$.

**Proof of claim**: Among all equivariant essential spheres (i.e., $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$), choose $S$ minimizing $|S \cap \tilde{k}|$ (counting $|S \cap \tilde{k}| + |\tau(S) \cap \tilde{k}|$ if $\tau(S) \neq S$).

First, $|S \cap \tilde{k}| \neq 0$ (shown above: if $S \cap \tilde{k} = \emptyset$, then $S$ is inessential).

Second, $|S \cap \tilde{k}|$ is even (since $S$ separates $M$ and $\tilde{k}$ is a closed curve, it must cross $S$ an even number of times).

So $|S \cap \tilde{k}| \geq 2$. Suppose $|S \cap \tilde{k}| = 2n \geq 4$. We'll derive a contradiction by finding an equivariant essential sphere with fewer intersections.

**Subcase: $\tau(S) = S$, $|S \cap \tilde{k}| = 2n \geq 4$.**

$\Sigma = S/\tau = \pi(S)$ is a sphere in $S^3$ intersecting $k$ in $2n$ points. The $2n$ points divide $k$ into $2n$ arcs, $n$ in each ball $B_1, B_2$ bounded by $\Sigma$.

Consider the $n$ arcs of $k$ in $B_1$. Label the $2n$ points on $\Sigma$ as $p_1, \ldots, p_{2n}$ in cyclic order. The arcs in $B_1$ pair up these points. Since $n \geq 2$, there exist two points $p_i, p_j$ that are paired by an arc $\alpha$ in $B_1$ and are "adjacent" in the sense that one of the two arcs on $\Sigma$ between $p_i$ and $p_j$ contains no other $p_\ell$.

Wait, this isn't guaranteed. The pairing might not have any adjacent pairs. For example, with 4 points $p_1, p_2, p_3, p_4$ in cyclic order, the arcs in $B_1$ might pair $p_1$ with $p_3$ and $p_2$ with $p_4$ (the "crossing" pairing). In this case, no pair is adjacent.

But in that case, the arcs in $B_1$ form a non-trivial tangle. And the arcs in $B_2$ also pair the points, and the two pairings together form the knot $k$.

Hmm, let me think about this differently. If no pair of points connected by an arc in $B_1$ is adjacent on $\Sigma$, then the tangle in $B_1$ is "fully crossed". But we can still do surgery.

Take any arc $\alpha$ in $B_1$ connecting $p_i$ and $p_j$. There's a disk $D$ in $B_1$ with $\partial D = \alpha \cup \gamma$ where $\gamma$ is an arc on $\Sigma$ from $p_i$ to $p_j$. Choose $D$ to be innermost (minimizing $|D \cap k|$). The interior of $D$ might intersect $k$ in some arcs.

If $D \cap k = \alpha$ (interior of $D$ is disjoint from $k$): Surgery on $\Sigma$ along $D$ gives a new sphere $\Sigma'$ with $|\Sigma' \cap k| = 2n - 2$. If $2n - 2 = 2$ (i.e., $n = 2$), then $\Sigma'$ is a 2-point sphere, and we can analyze it using primality. If $2n - 2 \geq 4$, we can repeat.

If $D \cap k \supsetneq \alpha$: The interior of $D$ intersects $k$ in some arcs. Take an innermost subdisk $D'$ of $D$ (bounded by a sub-arc of $\alpha$ or $k$ and a sub-arc of $\gamma$ or $k$). This gives a surgery that reduces intersections.

Actually, the standard innermost disk argument works as follows: Among all disks in $B_1$ with boundary consisting of an arc of $k$ and an arc on $\Sigma$, choose one $D$ that is innermost (its interior is disjoint from $k$). Such a disk exists because we can take any disk and if its interior intersects $k$, we can find a sub-disk that is innermost.

With this innermost disk $D$ (interior disjoint from $k$, $\partial D = \alpha \cup \gamma$ where $\alpha \subset k$ and $\gamma \subset \Sigma$), surgery on $\Sigma$ gives $\Sigma'$ with $|\Sigma' \cap k| = 2n - 2$.

Now, $\Sigma'$ bounds two balls $B_1', B_2'$. The knot $k$ intersects $\Sigma'$ in $2(n-1)$ points. We need to check that $\Sigma'$ lifts to an essential equivariant sphere in $M(k)$.

$\pi^{-1}(\Sigma')$ is the double branched cover of $\Sigma'$ branched at $\Sigma' \cap k = 2(n-1)$ points. As computed earlier:
- If $n-1 = 1$ (i.e., $n = 2$): $\pi^{-1}(\Sigma')$ is a sphere (double branched cover of $S^2$ at 2 points = $S^2$).
- If $n-1 \geq 2$: $\pi^{-1}(\Sigma')$ has genus $\geq 1$, not a sphere.

So for $n = 2$, we get a sphere $\tilde{S}' = \pi^{-1}(\Sigma')$ with $|\tilde{S}' \cap \tilde{k}| = 2$, which is equivariant (since $\pi^{-1}(\Sigma')$ is always $\tau$-invariant as a set). If $\tilde{S}'$ is essential, this contradicts the minimality of $|S \cap \tilde{k}|$.

Is $\tilde{S}'$ essential? The sphere $\Sigma'$ decomposes $S^3$ into $B_1'$ and $B_2'$, with $k$ having $1$ arc in one ball and $2n - 3$ arcs in the other (wait, let me recount). Originally $\Sigma$ had $2n$ points, $n$ arcs in $B_1$, $n$ arcs in $B_2$. After surgery along $D$ (which is in $B_1$), $\Sigma'$ has $2(n-1)$ points. The ball $B_1'$ (roughly $B_1$ minus a neighborhood of $D$) contains $n - 1$ arcs, and $B_2'$ (roughly $B_2$ plus a neighborhood of $D$) contains $n - 1$ arcs as well? No, let me think again.

Actually, surgery along $D$ removes the two points $p_i, p_j$ from $\Sigma \cap k$ and the arc $\alpha$ from $k \cap B_1$. The new sphere $\Sigma'$ intersects $k$ in $2n - 2$ points. The ball $B_1'$ (the one that doesn't contain the surgery region) contains the remaining $n - 1$ arcs of the original $B_1$ tangle. The ball $B_2'$ contains the original $n$ arcs of $B_2$ plus... hmm, actually the arc $\alpha$ is now on the $B_2'$ side. So $B_2'$ contains $n$ arcs from $B_2$ and the arc $\alpha$ is now part of $k$ on the $B_2'$ side, but $\alpha$ connects to the rest of $k$ through the other arcs...

This is getting confusing. Let me think about it more carefully.

$k$ is a circle. $\Sigma$ intersects $k$ in $2n$ points, dividing $k$ into $2n$ arcs: $\alpha_1, \beta_1, \alpha_2, \beta_2, \ldots, \alpha_n, \beta_n$ where $\alpha_i$ are in $B_1$ and $\beta_i$ are in $B_2$ (alternating). So $k = \alpha_1 \beta_1 \alpha_2 \beta_2 \cdots \alpha_n \beta_n$.

Surgery along $D$ (with $\partial D = \alpha_1 \cup \gamma$) removes $\alpha_1$ from $B_1$ and replaces $\gamma \subset \Sigma$ with $\alpha_1$. The new sphere $\Sigma'$ doesn't intersect $k$ at the endpoints of $\alpha_1$ (those points are now on $\alpha_1 \subset \Sigma'$, not on $k \cap \Sigma'$). Wait, no. $\Sigma'$ is obtained from $\Sigma$ by replacing $\gamma$ with $\alpha_1$. The points $p_i, p_j$ (endpoints of $\alpha_1$) are on both $\Sigma$ and $k$. After surgery, $\Sigma'$ passes through $\alpha_1$ instead of $\gamma$. At the points $p_i, p_j$, $\Sigma'$ meets $k$ (since $\alpha_1 \subset k$ and $\alpha_1 \subset \Sigma'$). Hmm, so actually $\Sigma' \cap k$ still contains $p_i$ and $p_j$?

No wait. $\Sigma'$ is a new sphere obtained by surgery. $\Sigma' = (\Sigma \setminus \gamma) \cup \alpha_1$. The intersection $\Sigma' \cap k$: $\Sigma \setminus \gamma$ intersects $k$ at the $2n - 2$ points other than $p_i, p_j$. And $\alpha_1 \subset k$, so $\alpha_1 \cap k = \alpha_1$, but $\alpha_1$ is part of $\Sigma'$ and part of $k$, so $\Sigma' \cap k$ includes $\alpha_1$. But we want transverse intersection. We should push $\Sigma'$ slightly off $k$ along $\alpha_1$.

After a small perturbation, $\Sigma' \cap k$ consists of the $2n - 2$ points (we've removed $p_i$ and $p_j$). The arc $\alpha_1$ is now on one side of $\Sigma'$.

So $k$ is divided by $\Sigma'$ into $2(n-1)$ arcs. The arc $\alpha_1$ is now entirely on one side (say $B_2'$). The remaining arcs: $n - 1$ arcs from the original $B_1$ (minus $\alpha_1$) are on the $B_1'$ side, and $n$ arcs from $B_2$ plus $\alpha_1$ are on the $B_2'$ side. But wait, $\alpha_1$ connects to $\beta$-arcs on both ends. After removing $p_i, p_j$ from the intersection, the arcs of $k$ on the $B_2'$ side are: $\beta_{i-1} \alpha_1 \beta_i$ (merged into one arc) and the other $\beta$-arcs. So $B_2'$ has $n - 1$ arcs (one of which is $\beta_{i-1} \alpha_1 \beta_i$, and the rest are the other $\beta$-arcs). And $B_1'$ has $n - 1$ arcs.

So both sides have $n - 1$ arcs. Good.

Now, for $n = 2$: both sides have 1 arc. $\Sigma'$ intersects $k$ in 2 points. $\pi^{-1}(\Sigma')$ is a sphere with $|\pi^{-1}(\Sigma') \cap \tilde{k}| = 2$.

Is this sphere essential? The sphere $\Sigma'$ decomposes $(S^3, k)$ into two tangles, each with 1 arc. The double branched cover of each side is a 3-manifold bounded by $\pi^{-1}(\Sigma')$. For $\pi^{-1}(\Sigma')$ to be essential, neither side's double branched cover should be a ball.

The double branched cover of a ball along 1 arc is a ball (as we showed). So if either tangle is a trivial 1-arc tangle (unknotted arc), the corresponding side's double branched cover is a ball, and $\pi^{-1}(\Sigma')$ is inessential.

But if both tangles are non-trivial (knotted arcs), then both sides' double branched covers are not balls, and $\pi^{-1}(\Sigma')$ is essential.

Hmm, but if both tangles are non-trivial, then $\Sigma'$ is a decomposing sphere for $k$ showing $k$ is composite. But we assumed $k$ is prime, so one tangle must be trivial, making $\pi^{-1}(\Sigma')$ inessential.

So for $n = 2$: the surgery gives an equivariant sphere $\tilde{S}'$ with $|\tilde{S}' \cap \tilde{k}| = 2$, but it's inessential (because $k$ is prime). So we can't use it to contradict minimality.

Hmm, so the minimality argument doesn't directly work because the surgically reduced sphere might be inessential.

But wait — if $\tilde{S}'$ is inessential, it bounds a ball in $M(k)$. The ball is the double branched cover of the trivial tangle. Can we use this to simplify $S$?

If $\tilde{S}'$ bounds a ball $B$ in $M(k)$, and $|\tilde{S}' \cap \tilde{k}| = 2$, then $B$ contains an arc of $\tilde{k}$ (the lift of the trivial arc). We can use $B$ to isotope $S$ and reduce $|S \cap \tilde{k}|$.

Here's the idea: $S$ and $\tilde{S}'$ are both spheres in $M(k)$. $\tilde{S}'$ has 2 intersections with $\tilde{k}$ and $S$ has $2n = 4$ intersections. We can use the ball $B$ bounded by $\tilde{S}'$ to isotope part of $S$ through $B$, reducing the intersection with $\tilde{k}$.

Actually, let me think about this more carefully. $S$ and $\tilde{S}'$ are two spheres in $M(k)$. We can isotope them to be transverse and consider their intersection circles. An innermost circle of $S \cap \tilde{S}'$ on $\tilde{S}'$ bounds a disk $D'$ on $\tilde{S}'$ that is either inside or outside $B$. If $D' \subset B$, we can surger $S$ along $D'$ (replacing a disk of $S$ with $D'$), which doesn't change the topological type of $S$ (it's still a sphere) but might change $|S \cap \tilde{k}|$.

This is getting very involved. Let me try to think about whether there's a cleaner proof.

Actually, I recall now that there's a cleaner approach using the following fact:

**Fact**: The double branched cover of $S^3$ along $k$ is irreducible if and only if $k$ is prime.

Wait, is this actually a known theorem? Let me think about whether it's true.

The "if" direction: $k$ prime $\Rightarrow$ $\Sigma_2(k)$ irreducible (hence prime, since $\Sigma_2(k)$ is a closed orientable 3-manifold $\neq S^3$ for non-trivial $k$, and irreducible closed 3-manifolds are prime).

Actually, for a closed orientable 3-manifold, irreducible is equivalent to prime (with the exception of $S^1 \times S^2$, which is prime but not irreducible). And $\Sigma_2(k)$ for a non-trivial knot $k$ is not $S^1 \times S^2$ (since $H_1(\Sigma_2(k)) = \mathbb{Z}/2$-torsion related... actually $H_1(\Sigma_2(k))$ is the 2-torsion part of the knot group abelianized, which for a knot is related to the determinant of the knot). For the unknot, $\Sigma_2 = S^3$, which is irreducible. For a non-trivial knot, $\Sigma_2(k) \neq S^1 \times S^2$ (since $H_1(S^1 \times S^2) = \mathbb{Z}$, but $H_1(\Sigma_2(k))$ is finite for any knot). So for knots, prime = irreducible for the double branched cover.

So the question reduces to: $k$ prime $\Rightarrow$ $\Sigma_2(k)$ irreducible?

I believe this is true and is a consequence of the equivariant sphere theorem. Let me try to find the cleanest proof.

Here's another approach using the knot complement:

$\Sigma_2(k) = \widetilde{E(k)} \cup V$ where $\widetilde{E(k)}$ is the double cover of the knot exterior $E(k) = S^3 \setminus \nu(k)$ and $V = \nu(\tilde{k})$ is a solid torus glued along the boundary.

If $\Sigma_2(k)$ is reducible, there's an essential sphere $S$. Isotope $S$ to minimize $|S \cap V|$. Then $S \cap \widetilde{E(k)}$ is a planar surface (sphere minus disks) properly embedded in $\widetilde{E(k)}$.

If $|S \cap V| = 0$: $S \subset \widetilde{E(k)}$, and $S$ is a closed essential surface in $\widetilde{E(k)}$. But $\widetilde{E(k)}$ is a double cover of $E(k)$, which is irreducible (for a non-split knot). Is the double cover of an irreducible 3-manifold irreducible? Not necessarily in general, but...

Hmm, actually the double cover of an irreducible 3-manifold can be reducible. For example, the double cover of a certain knot complement can be reducible. But for the specific case of knot complements in $S^3$, maybe it's OK.

Actually, I don't think the double cover of $E(k)$ is always irreducible even for prime $k$. The issue is more subtle.

Let me go back to the equivariant sphere theorem approach and try to make it work.

I think the key insight I was missing is: we should choose $S$ to minimize $|S \cap \tilde{k}|$ among all essential spheres (not just equivariant ones), and then show that the equivariant sphere theorem gives us an equivariant sphere with the same or fewer intersections.

Actually, here's a cleaner approach. Let me use the following version of the equivariant sphere theorem:

**Equivariant Sphere Theorem (Meeks-Yau)**: Let $M$ be an orientable 3-manifold with an involution $\tau$. If $M$ is reducible, then $M$ contains an essential sphere $S$ such that $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$, and $S$ can be chosen to minimize $|S \cap \text{Fix}(\tau)|$ among all essential spheres (not just equivariant ones).

Wait, I don't think the equivariant sphere theorem says that. It says there exists an equivariant essential sphere, but not necessarily one that minimizes intersections globally.

Let me try yet another approach. Maybe I should think about this in terms of the following lemma:

**Lemma**: If $S$ is an essential sphere in $\Sigma_2(k)$ that is $\tau$-invariant and $|S \cap \tilde{k}| = 2n$, then $k$ can be written as a connected sum of $n$ knots (some of which might be unknots).

If this lemma is true, then for $k$ prime, $n = 1$, and $|S \cap \tilde{k}| = 2$. But then $\pi(S)$ is a sphere intersecting $k$ in 2 points, and since $k$ is prime, one tangle is trivial, so the double branched cover of that side is a ball, making $S$ inessential. Contradiction.

Is the lemma true? If $S$ is $\tau$-invariant with $|S \cap \tilde{k}| = 2n$, then $\pi(S) = \Sigma$ intersects $k$ in $2n$ points. The sphere $\Sigma$ decomposes $(S^3, k)$ into two tangles $(B_1, T_1)$ and $(B_2, T_2)$, each with $n$ arcs. The knot $k$ is recovered by gluing these tangles.

Now, each tangle with $n$ arcs can be further decomposed. If $n \geq 2$, we can find a sphere in $B_1$ (or $B_2$) that intersects $T_1$ in 2 points and splits off one arc. This gives a decomposition of $k$ into a connected sum.

More precisely: In $B_1$, the $n$ arcs $T_1$ can be separated by a sphere $\Sigma_1 \subset B_1$ intersecting $T_1$ in 2 points, splitting $T_1$ into a 1-arc tangle and an $(n-1)$-arc tangle. (This is always possible: take a small sphere around one arc.) Then $\Sigma_1$ together with a disk on $\Sigma$ forms a sphere in $S^3$ intersecting $k$ in 2 points, giving a connected sum decomposition of $k$.

But this decomposition might be trivial (one summand is the unknot). For $k$ prime, all such decompositions are trivial. So each 1-arc tangle we split off is trivial.

Hmm, but this doesn't directly give us that $S$ is inessential. Let me think more.

OK here's another approach. Let me consider the case $\tau(S) = S$, $|S \cap \tilde{k}| = 2n$, and try to show directly that $S$ being essential implies $k$ is composite.

$S$ is essential in $M = \Sigma_2(k)$. $S$ separates $M$ into $X$ and $Y$, with $\tau(X) = X$ and $\tau(Y) = Y$ (since $\tau(S) = S$). The fixed set $\tilde{k}$ intersects $S$ in $2n$ points, so $\tilde{k} \cap X$ consists of $n$ arcs and $\tilde{k} \cap Y$ consists of $n$ arcs.

$X$ is the double branched cover of $B_1$ along $T_1$ (the $n$-arc tangle in $B_1$), and $Y$ is the double branched cover of $B_2$ along $T_2$.

$S$ is essential means neither $X$ nor $Y$ is a 3-ball. The double branched cover of a ball along an $n$-arc tangle is a ball if and only if the tangle is "trivial" (i.e., consists of $n$ pairwise unknotted, unlinked arcs). Actually, I'm not sure about the "only if" direction for $n \geq 2$.

For $n = 1$: double branched cover of a ball along 1 arc is a ball iff the arc is unknotted. (If the arc is knotted, the double branched cover is not a ball — it's the double branched cover of $S^3$ along the knot formed by closing the arc, minus a ball.)

For $n \geq 2$: it's more complicated. The double branched cover of a ball along a rational tangle (2 arcs) is a solid torus, not a ball. So for $n = 2$, the double branched cover is never a ball (it's a solid torus or something more complicated).

Wait, that's important. For $n = 2$: $X$ is the double branched cover of $B_1$ along a 2-arc tangle $T_1$. The boundary of $X$ is $S$ (a sphere). But the double branched cover of a ball along 2 arcs has boundary... let me think. The double branched cover of $B^3$ along 2 properly embedded arcs: the boundary of $B^3$ is $S^2$, and the double branched cover of $S^2$ along 4 points (the endpoints of the arcs) is a torus (by Riemann-Hurwitz: $\chi = 2 \cdot 2 - 4 = 0$, so genus 1). So $\partial X$ is a torus, not a sphere!

But $S$ is a sphere and $S = \partial X$. Contradiction! So $n = 2$ is impossible for $\tau(S) = S$.

Wait, let me recheck. $S$ is $\tau$-invariant, and $S$ is the boundary of $X$. The double branched cover of $B_1$ along $T_1$: the boundary of this cover is the double branched cover of $\partial B_1 = \Sigma$ along $\partial T_1 = \Sigma \cap k$ (which is $2n$ points). The double branched cover of $S^2$ along $2n$ points has Euler characteristic $\chi = 2 \cdot 2 - 2n = 4 - 2n$. For $n = 1$: $\chi = 2$, sphere. For $n = 2$: $\chi = 0$, torus. For $n \geq 3$: $\chi < 0$, higher genus.

But $S$ is a sphere ($\chi = 2$). So we need $4 - 2n = 2$, i.e., $n = 1$.

Wait, but $S$ is the boundary of $X$, and $\partial X$ is the double branched cover of $\Sigma$ along $2n$ points. If $n = 1$, $\partial X$ is a sphere, which matches $S$ being a sphere. If $n \geq 2$, $\partial X$ is not a sphere, which contradicts $S$ being a sphere.

So for $\tau(S) = S$ and $S$ a sphere, we must have $n = 1$, i.e., $|S \cap \tilde{k}| = 2$!

This is the key insight I was missing. The topology of the double branched cover constrains $n$ to be 1.

Let me double-check: $S$ is $\tau$-invariant, so $\tau|_S$ is an involution on $S = S^2$ with $2n$ fixed points. The quotient $S/\tau = \Sigma = S^2$. The double branched cover of $S^2$ along $2n$ points: by Riemann-Hurwitz, $\chi(S) = 2\chi(\Sigma) - 2n$, so $2 = 4 - 2n$, giving $n = 1$. ✓

So for $\tau(S) = S$, we must have $|S \cap \tilde{k}| = 2$.

Now, with $|S \cap \tilde{k}| = 2$: $\Sigma = \pi(S)$ intersects $k$ in 2 points. Since $k$ is prime, one of the two tangles $(B_1, T_1)$ or $(B_2, T_2)$ is trivial (a single unknotted arc). WLOG $(B_1, T_1)$ is trivial. The double branched cover of $B_1$ along a trivial arc is a ball (as we showed). So $X$ is a ball, and $S = \partial X$ bounds a ball, contradicting the essentiality of $S$.

Now for **Case 2: $\tau(S) \cap S = \emptyset$**.

$S$ and $\tau(S)$ are disjoint. Let $\Sigma = \pi(S) = \pi(\tau(S))$. The preimage $\pi^{-1}(\Sigma) = S \cup \tau(S)$.

$S$ separates $M$ into $X$ and $Y$, with $\tau(S) \subset X$ (WLOG) and $\tau(Y) \subset X$. Actually, $\tau(X)$ contains $S$ and $Y$... let me be more careful.

$S$ separates $M$ into $X$ and $Y$. $\tau(S)$ is disjoint from $S$, so $\tau(S) \subset X$ or $\tau(S) \subset Y$. WLOG $\tau(S) \subset X$. Then $\tau(X) \supset S$ (since $\tau(\tau(S)) = S \subset \tau(X)$) and $\tau(Y) \subset X$ (since $\tau(Y)$ is bounded by $\tau(S) \subset X$). Also $\tau(X) \supset Y$ (since $\tau(Y) \subset X$ means $Y \subset \tau(X)$). So $\tau(X) \supset Y \cup S$ and $\tau(Y) \subset X$.

The region between $S$ and $\tau(S)$ (inside $X$) is $R = X \setminus \tau(Y)$. We have $\tau(R) = R$ (since $\tau$ swaps $S$ and $\tau(S)$, and swaps the two sides of $R$).

$\pi(R) = B_1$ (one of the two balls bounded by $\Sigma$) and $\pi(Y \cup \tau(Y)) = B_2$ (the other ball). Actually, $\pi(Y) = \pi(\tau(Y)) = B_2$ (since $Y$ and $\tau(Y)$ are related by $\tau$ and both project to the same thing). And $\pi(R) = B_1$.

$R$ is the double branched cover of $B_1$ along $k \cap B_1$ (which is $m_1$ arcs). $Y$ is one component of the double branched cover of $B_2$ along $k \cap B_2$ (which is $m_2$ arcs), and $\tau(Y)$ is the other component.

The boundary of $R$ is $S \cup \tau(S)$ (two spheres). The boundary of $Y$ is $S$ (one sphere), and the boundary of $\tau(Y)$ is $\tau(S)$.

Now, $\partial R = S \cup \tau(S)$. $R$ is the double branched cover of $B_1$ along $m_1$ arcs. The boundary of this cover is the double branched cover of $\partial B_1 = \Sigma$ along $m_1 \cdot 2$ points (each arc has 2 endpoints on $\Sigma$). Wait, $k \cap B_1$ consists of $m_1$ arcs, and the endpoints of these arcs are $2m_1$ points on $\Sigma$. But $\Sigma \cap k$ has $m = 2m_1 + 2m_2$... no, $m = m_1 + m_2$ where $m_1$ is the number of arcs in $B_1$ and $m_2$ is the number of arcs in $B_2$. Each arc has 2 endpoints, so $|\Sigma \cap k| = 2m_1 = 2m_2$... no, that's not right either.

Let me recount. $k$ is a circle. $\Sigma$ intersects $k$ in $m$ points. These $m$ points divide $k$ into $m$ arcs. Each arc is in $B_1$ or $B_2$. Since $k$ alternates between $B_1$ and $B_2$ (each time it crosses $\Sigma$), the number of arcs in $B_1$ equals the number in $B_2$ (both are $m/2$). So $m$ must be even, $m = 2m'$, with $m'$ arcs in each ball.

So $m_1 = m_2 = m' = m/2$.

The boundary of $R$ (double branched cover of $B_1$ along $m'$ arcs) is the double branched cover of $\Sigma = S^2$ along $2m'$ points (the endpoints of the $m'$ arcs). By Riemann-Hurwitz: $\chi(\partial R) = 2 \cdot 2 - 2m' = 4 - 2m'$. But $\partial R = S \cup \tau(S)$, two spheres, so $\chi(\partial R) = 4$. Thus $4 - 2m' = 4$, giving $m' = 0$.

But $m' = 0$ means $k \cap B_1 = \emptyset$, which we already showed leads to $S$ being inessential. Contradiction!

Wait, that can't be right. Let me recheck.

$\partial R = S \cup \tau(S)$. Each of $S$ and $\tau(S)$ is a sphere, so $\chi(\partial R) = 2 + 2 = 4$. The double branched cover of $\Sigma$ along $2m'$ points has $\chi = 4 - 2m'$. Setting $4 - 2m' = 4$ gives $m' = 0$.

But if $m' = 0$, there are no arcs in $B_1$, so $k \subset B_2$. Then $R$ is the double unbranched cover of $B_1$, which is two balls. So $R = B_R \cup B_R'$ (two balls), with $\partial B_R = S$ and $\partial B_R' = \tau(S)$. So $S$ bounds a ball, contradicting essentiality.

So **Case 2 is impossible** (for an essential sphere)!

Wait, I need to be more careful. $\partial R$ is the preimage of $\partial B_1 = \Sigma$ under the branched cover $\pi|_R: R \to B_1$. The branching is along $k \cap B_1 = m'$ arcs. The preimage of $\Sigma$ under this branched cover is the double branched cover of $\Sigma$ along the $2m'$ endpoints of these arcs. But actually, the boundary of $R$ is $\pi^{-1}(\Sigma) \cap R$, which is $S \cup \tau(S)$.

Hmm, but is $\partial R$ exactly the double branched cover of $\Sigma$ along $2m'$ points? Let me think again.

$R$ is a component of $\pi^{-1}(B_1)$. $\pi^{-1}(\Sigma) = S \cup \tau(S)$. So $\partial R \subset S \cup \tau(S)$. Since $R$ is between $S$ and $\tau(S)$, $\partial R = S \cup \tau(S)$. Yes.

Now, $\pi|_{\partial R}: \partial R \to \Sigma$ is a 2-to-1 map. It's the restriction of the branched cover to the boundary. The branching points on $\Sigma$ are $\Sigma \cap k = 2m'$ points. At each branching point, the map is 1-to-1 (locally like $z \mapsto z^2$). So $\pi|_{\partial R}$ is a double branched cover of $\Sigma$ branched at $2m'$ points.

By Riemann-Hurwitz: $\chi(\partial R) = 2\chi(\Sigma) - (2m' - 0) = 4 - 2m'$. (The Riemann-Hurwitz formula for a degree-2 map branched at $r$ points: $\chi(\text{cover}) = 2\chi(\text{base}) - r$. Here $r = 2m'$.)

$\chi(\partial R) = \chi(S) + \chi(\tau(S)) = 2 + 2 = 4$.

So $4 = 4 - 2m'$, giving $m' = 0$.

This means Case 2 always leads to $m' = 0$, i.e., no arcs in $B_1$, which makes $S$ inessential. So **Case 2 is impossible for an essential sphere**.

So the only possible case is Case 1: $\tau(S) = S$, which forces $|S \cap \tilde{k}| = 2$ (by the Riemann-Hurwitz argument), which then forces $S$ to be inessential (by primality of $k$). Therefore, no essential sphere exists, and $\Sigma_2(k)$ is irreducible, hence prime.

Wait, I need to double-check the Riemann-Hurwitz argument for Case 1 as well.

**Case 1: $\tau(S) = S$.**

$S$ is $\tau$-invariant. $S$ separates $M$ into $X$ and $Y$ with $\tau(X) = X$, $\tau(Y) = Y$. $\pi|_X: X \to B_1$ is a double branched cover (branched along $k \cap B_1$), and $\pi|_Y: Y \to B_2$ is a double branched cover (branched along $k \cap B_2$).

$\partial X = S$. $\pi|_S: S \to \Sigma$ is a double branched cover of $\Sigma$ branched at $\Sigma \cap k = 2m'$ points (where $m' = m/2$ is the number of arcs in each ball). By Riemann-Hurwitz: $\chi(S) = 2\chi(\Sigma) - 2m' = 4 - 2m'$. Since $S$ is a sphere, $\chi(S) = 2$. So $2 = 4 - 2m'$, giving $m' = 1$.

So $m' = 1$, meaning each ball contains exactly 1 arc of $k$, and $|\Sigma \cap k| = 2$.

Since $k$ is prime, one of the two 1-arc tangles is trivial. WLOG $(B_1, T_1)$ is a trivial tangle (unknotted arc). The double branched cover of $B_1$ along a trivial arc is a ball (as shown: the double branched cover of $S^3$ along the unknot is $S^3$, and splitting along the equatorial sphere gives two balls, each being the double branched cover of a ball along a trivial arc).

So $X$ is a ball, $S = \partial X$ bounds a ball, and $S$ is inessential. Contradiction.

Therefore, $\Sigma_2(k)$ is irreducible, hence prime (since $\Sigma_2(k)$ is a closed orientable 3-manifold and not $S^1 \times S^2$).

Wait, I should also verify that $\Sigma_2(k) \neq S^1 \times S^2$ for a prime knot $k$. For the unknot, $\Sigma_2 = S^3$, which is irreducible. For a non-trivial prime knot, $H_1(\Sigma_2(k))$ is finite (it's the 2-torsion of the abelianized knot group, related to the determinant $|\Delta_k(-1)|$ of the knot). Since $H_1(S^1 \times S^2) = \mathbb{Z}$, which is infinite, $\Sigma_2(k) \neq S^1 \times S^2$ for any non-trivial knot. For the unknot, $\Sigma_2 = S^3 \neq S^1 \times S^2$. So in all cases, $\Sigma_2(k) \neq S^1 \times S^2$, and irreducibility implies primality.

Actually, for the unknot, $\Sigma_2(S^3, \text{unknot}) = S^3$, which is irreducible and prime. So the statement holds trivially for the unknot.

Great, so the proof is:

1. Suppose $k$ is prime and $\Sigma_2(k)$ is reducible.
2. By the equivariant sphere theorem, there exists an essential sphere $S$ with $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.
3. If $\tau(S) \cap S = \emptyset$: Riemann-Hurwitz on $\partial R$ (the region between $S$ and $\tau(S)$) shows $k \cap B_1 = \emptyset$, making $S$ bound a ball. Contradiction.
4. If $\tau(S) = S$: Riemann-Hurwitz on $S$ shows $|S \cap \tilde{k}| = 2$, so $\pi(S)$ intersects $k$ in 2 points. Primality of $k$ makes one tangle trivial, so $S$ bounds a ball. Contradiction.
5. Therefore $\Sigma_2(k)$ is irreducible, hence prime.

Let me also handle the subcase of Case 1 where $S \cap \tilde{k} = \emptyset$ (i.e., $m' = 0$). In this case, $\pi(S)$ is a sphere in $S^3 \setminus k$, which bounds a ball $B$ with $k \cap B = \emptyset$ (since $k$ is a knot, not a link, and $S^3$ is irreducible). The preimage $\pi^{-1}(B)$ is two balls (unbranched double cover), so $S$ bounds a ball. Contradiction. (This is consistent with the Riemann-Hurwitz argument: $m' = 0$ gives $\chi(S) = 4$, but $S$ is a sphere with $\chi = 2$, contradiction. So actually $m' = 0$ is ruled out by Riemann-Hurwitz directly.)

Wait, hmm. If $S \cap \tilde{k} = \emptyset$, then $\tau|_S$ has no fixed points, so $S/\tau = \Sigma$ and $\pi|_S: S \to \Sigma$ is an unbranched double cover. An unbranched double cover of $S^2$ is two copies of $S^2$, so $S$ would be two spheres, not one. Contradiction. So $S \cap \tilde{k} = \emptyset$ is impossible for $\tau(S) = S$ (since $S$ is connected and $\tau|_S$ is a fixed-point-free involution on $S^2$, which would make $S^2 \to S^2/\tau$ a double cover, but $\pi_1(S^2) = 0$ so there's no nontrivial double cover). Actually, a fixed-point-free involution on $S^2$ would give $S^2 \to \mathbb{R}P^2$, but $S^2$ is simply connected and $\mathbb{R}P^2$ has $\pi_1 = \mathbb{Z}/2$, so the map $S^2 \to \mathbb{R}P^2$ is the universal cover, which is fine. But $\Sigma = S/\tau$ would be $\mathbb{R}P^2$, not $S^2$. But $\Sigma = \pi(S) \subset S^3$, and $\Sigma$ is a sphere (image of a sphere under a continuous map into $S^3$... well, $\pi|_S$ is a double cover of $\Sigma$, so $\Sigma$ is a surface. If $\tau|_S$ has no fixed points, $\Sigma = S/\tau$ is $\mathbb{R}P^2$. But $\pi(S) \subset S^3$ and $\pi(S)$ is a closed surface in $S^3$. $\mathbb{R}P^2$ cannot be embedded in $S^3$ (since $S^3$ is orientable and $\mathbb{R}P^2$ is non-orientable). Contradiction. So $S \cap \tilde{k} \neq \emptyset$ when $\tau(S) = S$.)

Good, so $S \cap \tilde{k} \neq \emptyset$ is automatic for $\tau(S) = S$, and the Riemann-Hurwitz argument gives $|S \cap \tilde{k}| = 2$.

Now let me also verify the claim that the double branched cover of a ball along a single unknotted arc is a ball.

Consider $S^3$ with the unknot $u$. $\Sigma_2(S^3, u) = S^3$. The unknot lies on a standard sphere $\Sigma_0$ in $S^3$ that intersects $u$ in 2 points. This sphere divides $S^3$ into two balls $B_1, B_2$, each containing one unknotted arc of $u$. The preimage $\pi^{-1}(\Sigma_0)$ is a sphere $\tilde{\Sigma}_0$ in $\Sigma_2(S^3, u) = S^3$ (by Riemann-Hurwitz: $\chi = 4 - 2 = 2$, sphere). This sphere divides $S^3$ into two balls, which are the double branched covers of $B_1$ and $B_2$ along their respective arcs. So the double branched cover of a ball along a single unknotted arc is a ball. ✓

And if the arc is knotted: Consider a knotted arc $\alpha$ in a ball $B$. Close it up to a knot $k_\alpha$ by adding an arc on $\partial B$. The double branched cover of $B$ along $\alpha$ is $\Sigma_2(S^3, k_\alpha)$ minus a ball (the double branched cover of the complementary ball along the closing arc, which is unknotted, is a ball). So the double branched cover of $B$ along $\alpha$ is $\Sigma_2(S^3, k_\alpha) \setminus B^3$. This is a ball iff $\Sigma_2(S^3, k_\alpha) = S^3$ iff $k_\alpha$ is the unknot (by the unknotting theorem for double branched covers... actually, is it true that $\Sigma_2(k) = S^3$ iff $k$ is the unknot? For 2-bridge knots, the double branched cover is a lens space, and $L(1,0) = S^3$ corresponds to the unknot. But in general, there might be non-trivial knots with $\Sigma_2 = S^3$... Hmm, actually I think it's an open question or has a positive answer. Let me not worry about this — for our proof, we only need the "if" direction: unknotted arc → double branched cover is a ball, which we've verified.)

Actually, we need: if the tangle is trivial (unknotted arc), then the double branched cover is a ball. We've verified this. We don't need the converse.

So the proof is complete. Let me also handle the edge case where $k$ is the unknot. For the unknot, $\Sigma_2(k) = S^3$, which is irreducible and prime. ✓

Let me now also think about whether we need $k$ to be non-trivial for the proof. The proof shows that if $k$ is prime (including the unknot), then $\Sigma_2(k)$ is irreducible. For the unknot, $\Sigma_2 = S^3$ is irreducible. For a non-trivial prime knot, the proof by contradiction works: assuming $\Sigma_2(k)$ is reducible, the equivariant sphere theorem gives an essential sphere, and we derive a contradiction.

Actually, wait. For the unknot, $\Sigma_2 = S^3$ is irreducible, so there's no essential sphere, and the proof by contradiction vacuously works (there's nothing to prove). For a non-trivial prime knot, the proof works as above.

I think the proof is solid. Let me write it up cleanly.

Actually, let me reconsider one thing. In Case 2, I need to verify that $R$ is indeed the double branched cover of $B_1$ along $k \cap B_1$, and that $\partial R = S \cup \tau(S)$ is the double branched cover of $\Sigma$ along $\Sigma \cap k \cap B_1$ (the endpoints of the arcs in $B_1$).

$\pi^{-1}(B_1)$: Since $\pi: M \to S^3$ is a double branched cover branched along $k$, $\pi^{-1}(B_1)$ is the double branched cover of $B_1$ along $k \cap B_1$. Now, $\pi^{-1}(B_1) = R$ or $\pi^{-1}(B_1) = Y \cup \tau(Y)$, depending on which ball we call $B_1$.

Since $\pi^{-1}(\Sigma) = S \cup \tau(S)$, and $\Sigma = \partial B_1 = \partial B_2$, we have $\pi^{-1}(B_1) \cap \pi^{-1}(B_2) = S \cup \tau(S)$. The region $R$ (between $S$ and $\tau(S)$) is one of $\pi^{-1}(B_1)$ or $\pi^{-1}(B_2)$, and $Y \cup \tau(Y)$ is the other.

If $R = \pi^{-1}(B_1)$: $\partial R = S \cup \tau(S)$ is the double branched cover of $\Sigma$ along $\Sigma \cap k \cap B_1$ (the endpoints of arcs in $B_1$). The number of branch points is $2m_1$ where $m_1$ is the number of arcs in $B_1$. By Riemann-Hurwitz: $\chi(\partial R) = 4 - 2m_1$. But $\chi(\partial R) = 4$ (two spheres). So $m_1 = 0$.

If $R = \pi^{-1}(B_2)$: similarly $m_2 = 0$.

Either way, one of the balls has no arcs of $k$, meaning $k$ is entirely in the other ball. Then the double branched cover of the empty ball is two balls (unbranched), so $R$ is two balls, and $S$ (and $\tau(S)$) bound balls. Contradiction.

Wait, but $R$ is connected (it's the region between two disjoint spheres). If $m_1 = 0$, the double branched cover of $B_1$ along no arcs is the double unbranched cover of a ball, which is two disjoint balls. But $R$ is connected (region between $S$ and $\tau(S)$). Contradiction. So actually, $R$ can't be the double branched cover of a ball along 0 arcs if $R$ is connected.

Hmm, let me reconsider. If $m_1 = 0$ (no arcs in $B_1$), then $\pi^{-1}(B_1)$ is the double unbranched cover of $B_1$. Since $B_1$ is a ball (simply connected), the double unbranched cover is two disjoint balls. So $\pi^{-1}(B_1)$ is two disjoint balls, each bounded by one of $S, \tau(S)$. So $S$ bounds a ball and $\tau(S)$ bounds a ball, both inessential. Contradiction.

But which is $\pi^{-1}(B_1)$: $R$ or $Y \cup \tau(Y)$? If $\pi^{-1}(B_1)$ is two disjoint balls, it must be $Y \cup \tau(Y)$ (since $Y$ and $\tau(Y)$ are disjoint, each bounded by $S$ and $\tau(S)$ respectively). Then $R = \pi^{-1}(B_2)$, which is the double branched cover of $B_2$ along $m_2$ arcs (all of $k$, since $k \subset B_2$). And $Y, \tau(Y)$ are the two balls of the unbranched double cover of $B_1$.

So $S = \partial Y$ bounds the ball $Y$, contradicting essentiality. ✓

OK so the proof works. Let me also make sure about the Riemann-Hurwitz formula. For a degree-$d$ branched cover $f: \tilde{F} \to F$ of surfaces, branched at points $p_1, \ldots, p_r$ with ramification indices $e_1, \ldots, e_r$:

$$\chi(\tilde{F}) = d \cdot \chi(F) - \sum_{i=1}^r (e_i - 1)$$

For a double cover ($d = 2$) branched at $r$ points (each with $e_i = 2$):

$$\chi(\tilde{F}) = 2\chi(F) - r$$

In our Case 1: $f = \pi|_S: S \to \Sigma$, $d = 2$, $F = \Sigma = S^2$, $\chi(F) = 2$, $r = |S \cap \tilde{k}|$ (number of fixed points of $\tau|_S$, which equals the number of branch points). So $\chi(S) = 4 - r$. Since $S = S^2$, $\chi(S) = 2$, so $r = 2$.

In Case 2: $f = \pi|_{\partial R}: \partial R \to \Sigma$, $d = 2$, $F = \Sigma = S^2$, $\chi(F) = 2$, $r = |\Sigma \cap k \cap B_i|$ (the number of branch points, which is the number of endpoints of arcs in $B_i$, where $R = \pi^{-1}(B_i)$). So $\chi(\partial R) = 4 - r$. Since $\partial R = S \cup \tau(S)$ (two spheres), $\chi(\partial R) = 4$, so $r = 0$.

Everything checks out. Let me write the final proof.

One more thing: I should make sure that the equivariant sphere theorem applies. The equivariant sphere theorem (Meeks-Yau, 1980) states: If $M$ is an orientable 3-manifold with a finite group action $G$ (here $G = \mathbb{Z}/2$ generated by $\tau$), and $M$ is reducible (contains an essential sphere), then there exists an essential sphere $S$ such that $g(S) = S$ or $g(S) \cap S = \emptyset$ for all $g \in G$.

For $G = \mathbb{Z}/2 = \{1, \tau\}$, this means $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$. ✓

$M = \Sigma_2(k)$ is orientable (double branched cover of $S^3$ along a knot). ✓

The fixed set of $\tau$ is $\tilde{k}$, a knot in $M$. ✓

I think the proof is complete. Let me write it up.

Actually, let me also think about whether we need to worry about the case where $S$ intersects $\tilde{k}$ non-transversely. We can always isotope $S$ to be transverse to $\tilde{k}$, so this is not an issue.

Also, I should note that in Case 1, the fact that $\tau|_S$ has fixed points (so $S \cap \tilde{k} \neq \emptyset$) follows from the topological constraint: $\tau|_S$ is an involution on $S^2$ and $S/\tau = \Sigma \subset S^3$ is a 2-sphere (since $\pi(S)$ is a sphere in $S^3$). If $\tau|_S$ had no fixed points, $S/\tau$ would be $\mathbb{R}P^2$, which can't be embedded in $S^3$. So $\tau|_S$ must have fixed points, and by Riemann-Hurwitz, exactly 2.

Actually, I realize I need to be a bit more careful about why $\pi(S)$ is a sphere. $\pi|_S: S \to S^3$ is a continuous map from $S^2$ to $S^3$. The image $\pi(S)$ is a subset of $S^3$. Since $\pi$ is a branched cover and $S$ is $\tau$-invariant, $\pi|_S$ factors through $S/\tau$, and $\pi(S) = S/\tau$ (as a set). If $\tau|_S$ has fixed points, $S/\tau$ is a topological sphere (by the classification of involutions on $S^2$: an involution with fixed points is conjugate to a reflection, and the quotient is a disk; wait, that gives a disk, not a sphere).

Hmm, let me reconsider. An involution on $S^2$ with fixed points: by the classification, it's conjugate to a reflection across an equator. The quotient is a disk $D^2$, not $S^2$. But the fixed set is a circle (the equator), not isolated points.

But in our case, the fixed points of $\tau|_S$ are $S \cap \tilde{k}$, which is a finite set of points (since $S$ is transverse to $\tilde{k}$). An involution on $S^2$ with finitely many fixed points: by the Lefschetz fixed point theorem, $\chi(S^2) = 2 = \sum (-1)^i \text{tr}(\tau_*|_{H_i})$. For an involution, $\tau_*$ has eigenvalues $\pm 1$. On $H_0$: $\tau_* = 1$ (trace 1). On $H_2$: $\tau_* = \pm 1$. If $\tau_* = 1$ on $H_2$ (orientation-pres        — AI历史解题过程（thinking）
#   deepmath_103k_00006879         — 题目ID

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
  <problem_id>deepmath_103k_00006879</problem_id>
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

Let $f:\mathbb{C}\to \mathbb{C}$ be an entire function. Suppose that for every $z\in \mathbb{C}$, there exists $n_z\in \mathbb{N}$ such that $f^{(n_z)}(z)=0$. Is $f$ necessarily a polynomial?

## Standard Solution

Okay, so I need to figure out if an entire function f, which for every complex number z has some derivative of order n_z that's zero, must necessarily be a polynomial. Hmm. Let me start by recalling some complex analysis concepts.

First, an entire function is a function that's holomorphic everywhere on the complex plane. Polynomials are entire functions, and their derivatives eventually become zero once you differentiate enough times—specifically, the (deg f + 1)-th derivative is zero. So polynomials certainly satisfy the given condition because for each z, once you take enough derivatives, you get zero. The question is whether there are any non-polynomial entire functions that also have this property.

The problem states that for every z in ℂ, there exists a natural number n_z such that the n_z-th derivative of f at z is zero. So, for each point z, if we keep differentiating f, eventually at some order (depending on z), the derivative is zero. If f were a polynomial, this n_z would just be one more than the degree of the polynomial for all z. But here, n_z can vary with z.

Wait, but if f is a polynomial, then all its derivatives beyond the degree are zero everywhere, not just at individual points. So in that case, the n_z would be uniform for all z. But in the problem, n_z can depend on z. So maybe there's a function that isn't a polynomial but still has this property that for each z, some derivative vanishes at z.

I need to think about whether such a function exists. Let me recall some theorems. There's a theorem in complex analysis called the Identity Theorem, which says that if two holomorphic functions agree on a set with a limit point, then they agree everywhere. Also, there's something called the Taylor series expansion, which for entire functions converges everywhere on ℂ.

If f is entire, then around any point z, f can be expressed as its Taylor series. Suppose that for each z, there is some n_z such that f^{(n_z)}(z) = 0. Let me try to see what this implies.

Suppose we fix a point z. The Taylor series of f around z is ∑_{k=0}^∞ (f^{(k)}(z)/k!)(w - z)^k. If f^{(n_z)}(z) = 0, then the coefficient of (w - z)^{n_z} in this expansion is zero. But since the function is entire, the radius of convergence is infinite, so the series converges for all w.

But if at every z, there exists some n_z such that f^{(n_z)}(z) = 0, does that force all but finitely many coefficients in the Taylor expansion (around any point) to be zero? If so, then f would be a polynomial.

Alternatively, maybe there's a way to construct a non-polynomial entire function with this property. For example, consider a function that's a polynomial on different parts of the complex plane but glued together in some way. But entire functions are globally defined by their power series, so such piecewise definitions would have to agree on overlaps, which would force them to be a single polynomial.

Wait, another approach: Suppose f is not a polynomial. Then its Taylor series around any point has infinitely many non-zero coefficients. But if for each z, some derivative at z is zero, then each Taylor series around z has at least one zero coefficient. However, even if each Taylor series has some zero coefficient, that doesn't necessarily mean that beyond a certain point all coefficients are zero. For example, maybe different terms are zero for different z. But is it possible to have an entire function with infinitely many non-zero derivatives everywhere, yet at each individual point, one of the derivatives is zero?

Alternatively, consider the set where the k-th derivative is zero. For each k, the set Z_k = { z ∈ ℂ | f^{(k)}(z) = 0 } is a closed set (since f^{(k)} is continuous). The problem states that the union of all Z_k over k ∈ ℕ is the entire complex plane. So ℂ = ∪_{k=1}^∞ Z_k. By the Baire Category Theorem, since ℂ is a complete metric space, one of the Z_k must have non-empty interior. Therefore, there exists some k such that Z_k contains an open set. Then, by the Identity Theorem, since f^{(k)} is zero on an open set (which has limit points), f^{(k)} is identically zero on ℂ. Therefore, f is a polynomial of degree at most k-1.

Wait, that seems like a solid argument. Let me recap:

1. Assume f is entire and for every z ∈ ℂ, there exists n_z ∈ ℕ such that f^{(n_z)}(z) = 0.

2. Then ℂ = ∪_{k=1}^∞ Z_k, where Z_k = { z | f^{(k)}(z) = 0 }.

3. Each Z_k is closed (as the zero set of a continuous function).

4. By the Baire Category Theorem, in a complete metric space (like ℂ), a countable union of closed sets with empty interiors cannot cover the space. Therefore, at least one Z_k must have non-empty interior.

5. So there exists k ∈ ℕ and an open set U ⊆ Z_k. Hence, f^{(k)}(z) = 0 for all z ∈ U.

6. Since f^{(k)} is holomorphic (as f is entire) and is zero on an open set, by the Identity Theorem, f^{(k)} ≡ 0 on ℂ.

7. Therefore, f is a polynomial of degree at most k-1.

Therefore, f must be a polynomial.

So, the answer is yes, f is necessarily a polynomial.

But wait, let me check if there are any gaps here. The key step is applying the Baire Category Theorem. The complex plane is a complete metric space, and each Z_k is closed. If the union of all Z_k is the entire space, then at least one Z_k has non-empty interior. Therefore, that particular derivative is identically zero, which makes f a polynomial.

Yes, that seems right. So even though the condition is that for each z, some derivative vanishes at z, the Baire Category Theorem forces one derivative to vanish on an entire open set, hence everywhere. Therefore, the function is a polynomial.

Therefore, the answer should be yes, f must be a polynomial.

**Final Answer**
\boxed{Yes}
</think>

Given an entire function \( f: \mathbb{C} \to \mathbb{C} \) such that for every \( z \in \mathbb{C} \), there exists \( n_z \in \mathbb{N} \) with \( f^{(n_z)}(z) = 0 \), we need to determine if \( f \) is necessarily a polynomial.

1. **Entire Function and Derivatives**: An entire function is holomorphic everywhere on \( \mathbb{C} \). The condition implies that for each \( z \), some derivative of \( f \) at \( z \) is zero.

2. **Closed Sets**: For each \( k \in \mathbb{N} \), define \( Z_k = \{ z \in \mathbb{C} \mid f^{(k)}(z) = 0 \} \). Each \( Z_k \) is closed because \( f^{(k)} \) is continuous.

3. **Covering the Complex Plane**: The complex plane \( \mathbb{C} \) is the union of all \( Z_k \), i.e., \( \mathbb{C} = \bigcup_{k=1}^\infty Z_k \).

4. **Baire Category Theorem**: Since \( \mathbb{C} \) is a complete metric space, by the Baire Category Theorem, at least one \( Z_k \) must have a non-empty interior. Thus, there exists \( k \in \mathbb{N} \) and an open set \( U \subseteq Z_k \).

5. **Identity Theorem**: The function \( f^{(k)} \) is holomorphic and zero on the open set \( U \). By the Identity Theorem, \( f^{(k)} \equiv 0 \) on \( \mathbb{C} \).

6. **Conclusion**: Since \( f^{(k)} \equiv 0 \), \( f \) must be a polynomial of degree at most \( k-1 \).

Therefore, \( f \) is necessarily a polynomial.

\[
\boxed{Yes}
\]

## AI's Thinking (Attempted Solution Process)

Let me think about this problem carefully.The question: Is it true that if $k$ is a prime knot, then the double branched cover $M(k)$ of $S^3$ along the knot $k$ is a prime 3-manifold?

First, let me check for answer leaks in the problem text. The problem text is just the question itself, no solutions or hints. Good.

Now let me think about this. This is a classical question in knot theory / 3-manifold topology.

Let me recall what's known. The double branched cover of $S^3$ along a knot $k$ is denoted $M(k)$ or $\Sigma_2(k)$.

The question is whether primality of the knot implies primality of the double branched cover.

Let me think about what's known:

1. If $k$ is a composite knot $k = k_1 \# k_2$, then $M(k) = M(k_1) \# M(k_2)$. This is a standard fact — the double branched cover of a connected sum is the connected sum of the double branched covers. So if $M(k)$ is prime, then $k$ must be prime (contrapositive: composite knot gives composite cover).

2. The converse: if $k$ is prime, is $M(k)$ prime?

This is the question. Let me think about whether there are counterexamples.

Actually, I recall that this is a subtle question. Let me think about it more carefully.

For torus knots, the double branched covers are Seifert fibered spaces, which are prime.

For hyperbolic knots, the double branched cover is hyperbolic (by Thurston's theorem — most double branched covers of hyperbolic knots are hyperbolic), and hyperbolic 3-manifolds are prime (in fact, irreducible and atoroidal).

Wait, but is the double branched cover of a hyperbolic knot always hyperbolic? Not necessarily. There are hyperbolic knots whose double branched covers are not hyperbolic. For instance, some 2-bridge knots have non-hyperbolic double branched covers... no wait, 2-bridge knots have lens space double branched covers, which are prime.

Hmm, let me think about this differently. The key question is whether there exists a prime knot $k$ such that $M(k)$ is a connected sum $M_1 \# M_2$ with both $M_i$ nontrivial.

If $M(k) = M_1 \# M_2$, then by the equivariant sphere theorem, we might be able to find an essential sphere that is equivariant with respect to the covering involution.

The covering involution $\tau$ on $M(k)$ has fixed point set the lift of the knot, which is a knot $\tilde{k}$ in $M(k)$. The quotient $M(k)/\tau = S^3$ and $\tilde{k}/\tau = k$.

If $M(k)$ is reducible, there's an essential sphere $S$ in $M(k)$. By the equivariant sphere theorem (Meeks-Yau, or the original equivariant sphere theorem), we can find an essential sphere that is equivariant, i.e., $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

Case 1: $\tau(S) = S$. Then $S$ is invariant. The sphere $S$ either contains the fixed set or is disjoint from it. If $S$ is disjoint from the fixed set $\tilde{k}$, then $S$ projects to a sphere in $S^3$ disjoint from $k$, which must be inessential (since $S^3$ is irreducible), contradiction. If $S$ intersects $\tilde{k}$, then $S \cap \tilde{k}$ consists of points, and $S$ projects to a sphere in $S^3$ intersecting $k$ in those points (mod 2). Actually, $S$ is invariant and intersects the fixed set in an even number of points... hmm, this needs more care.

Actually, let me reconsider. The equivariant sphere theorem says: if $M$ is a 3-manifold with an involution $\tau$ and $M$ is reducible, then there exists an essential sphere $S$ such that either $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

Case A: $\tau(S) \cap S = \emptyset$. Then $S$ and $\tau(S)$ are disjoint essential spheres. The projection of $S$ to $S^3 = M(k)/\tau$ is a 2-sphere (possibly with branch points). If $S$ is disjoint from the fixed set, it projects to a sphere in $S^3 \setminus k$, which bounds a ball (since $S^3$ is irreducible), and this lifts to show $S$ is inessential, contradiction. So $S$ must intersect the fixed set.

Hmm, actually if $S$ is disjoint from the fixed set $\tilde{k}$, then the projection $\pi(S)$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $\pi(S)$ bounds a ball $B$ in $S^3$. The ball $B$ either contains part of $k$ or not. If $B \cap k = \emptyset$, then $\pi^{-1}(B)$ is two balls bounded by $S$ and $\tau(S)$, so $S$ is inessential. If $B \cap k \neq \emptyset$, then... $k$ is a single arc inside $B$ (since $k$ is connected and $\partial B = \pi(S)$ separates). Actually $k \cap B$ could be multiple arcs. Hmm.

This is getting complicated. Let me recall the actual known result.

I believe the answer is YES — if $k$ is prime, then $M(k)$ is prime. This is a theorem. Let me recall who proved it.

Actually, I think this follows from the equivariant sphere theorem. The argument goes:

Suppose $M(k)$ is reducible. By the equivariant sphere theorem (for the involution $\tau$), there exists an essential sphere $S$ in $M(k)$ that is either $\tau$-invariant or disjoint from $\tau(S)$.

If $S$ is $\tau$-invariant and disjoint from the fixed set $\tilde{k}$: Then $S/\tau$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $S/\tau$ bounds a ball. This ball lifts to give that $S$ bounds a ball in $M(k)$, contradicting essentiality. (Need to be careful about the lifting, but it works out.)

If $S$ is $\tau$-invariant and intersects $\tilde{k}$: Then $S \cap \tilde{k}$ is nonempty. Since $\tau$ fixes $\tilde{k}$ pointwise and $\tau(S) = S$, the intersection $S \cap \tilde{k}$ is a finite set of points. The projection $S/\tau$ is a sphere in $S^3$ that intersects $k$ in $|S \cap \tilde{k}|/2$ points (since the involution identifies pairs... wait no, $\tau$ fixes $\tilde{k}$ pointwise, so each point of $S \cap \tilde{k}$ is a fixed point and projects to a distinct point of $k$). So $S/\tau$ is a sphere in $S^3$ intersecting $k$ in $n = |S \cap \tilde{k}|$ points.

Now, $S/\tau$ separates $S^3$ into two balls $B_1, B_2$. The knot $k$ is divided into $n$ arcs in each ball. For $S$ to be essential in $M(k)$, we need... the sphere $S$ separates $M(k)$ into two pieces, each containing part of $\tilde{k}$.

Actually, the sphere $S$ intersects $\tilde{k}$ in $n$ points. Since $\tilde{k}$ is a knot (connected), $S$ separates $M(k)$ into two pieces, and $\tilde{k}$ passes through $S$ $n$ times. For $S$ to be essential, neither piece can be a ball (with no essential content).

The projection: $S/\tau$ separates $S^3$ into two balls $B_1, B_2$, and $k \cap B_i$ consists of $n/2$ arcs (if $n$ is even) or... wait, $n$ must be even since $\tilde{k}$ is a double cover of $k$ and $S$ is $\tau$-invariant. Actually, $\tilde{k} \to k$ is a 2-to-1 cover branched at... no, $\tilde{k}$ is the preimage of $k$ in the branched cover. The branched cover is branched along $k$, so $\tilde{k}$ maps 1-to-1 onto $k$ (each point of $k$ has one preimage on $\tilde{k}$, which is a fixed point of $\tau$). So $|S \cap \tilde{k}| = |S/\tau \cap k|$.

So $S/\tau$ intersects $k$ in $n$ points, dividing $k$ into $n$ arcs, split between $B_1$ and $B_2$. If $n$ is even, each ball gets $n/2$ arcs. If $n$ is odd... but $n$ must be even because $\tilde{k}$ is a closed curve crossing $S$ an even number of times (since $S$ separates and $\tilde{k}$ is a closed loop, it must cross $S$ an even number of times). So $n$ is even, and each $B_i$ contains $n/2$ arcs of $k$.

Now, $S$ is essential in $M(k)$. The two sides of $S$ in $M(k)$ project to $B_1$ and $B_2$ (each is a double branched cover of $B_i$ along the arcs $k \cap B_i$). For $S$ to be essential, at least one of these double branched covers must not be a ball.

The double branched cover of a ball along $n/2$ properly embedded arcs (a tangle) is a ball if and only if the tangle is "trivial" in some sense. Actually, the double branched cover of a ball along a rational tangle is a solid torus, not a ball. The double branched cover along the trivial tangle (two unknotted arcs) is... let me think. The double branched cover of $B^3$ along two unknotted, unlinked arcs is $S^1 \times D^2$ (a solid torus). Hmm, actually no.

Let me reconsider. The double branched cover of $B^3$ along $n/2$ arcs. If $n/2 = 0$ (no arcs), the double cover of a ball is two balls, but we're taking the branched cover... if there are no branch points, the double cover of a ball is two balls. But $S$ separates $M(k)$ into two pieces, each being a double branched cover of $B_i$ along $k \cap B_i$.

If $k \cap B_i = \emptyset$ (i.e., $n/2 = 0$ for one side), then that side is the double (unbranched) cover of $B_i$, which is two copies of $B_i$ if $B_i$ is a ball. But that would mean $S$ bounds two balls on that side, making $S$ inessential. So for $S$ to be essential, both sides must have $k \cap B_i \neq \emptyset$, meaning $n \geq 2$ and each side has at least 1 arc.

If each side has at least 1 arc, then $S/\tau$ is a sphere in $S^3$ intersecting $k$ in at least 2 points, with $k$ having arcs on both sides. This means $S/\tau$ is a "swallow-follow" sphere or a decomposing sphere for $k$.

If $k$ is prime, then any such sphere must be a "trivial" decomposing sphere — one side contains a trivial arc (an unknotted arc in a ball). But does that make $S$ inessential?

Hmm, let me think about this more carefully. If $k$ is prime, then for any sphere $S'$ in $S^3$ intersecting $k$ transversely in 2 points, one of the two tangles $(B_i, k \cap B_i)$ is trivial (i.e., the arc is unknotted in the ball).

If $(B_1, k \cap B_1)$ is a trivial tangle (one unknotted arc), then the double branched cover of $B_1$ along this arc is a solid torus (I think). Wait, let me reconsider.

The double branched cover of a ball along a single unknotted arc: The ball $B^3$ with a properly embedded unknotted arc. The double branched cover... Consider $B^3$ as the lower hemisphere of $S^3$, and the arc as a diameter. The double branched cover of $S^3$ along an unknotted circle is $S^3$ (since the unknot has double branched cover $S^3$). If we split $S^3$ into two balls along the equatorial sphere (intersecting the unknot in 2 points), each ball contains one unknotted arc, and the double branched cover of $S^3 = $ double branched cover of ball 1 $\cup$ double branched cover of ball 2, glued along their boundaries. Since the total is $S^3$ and by symmetry, each piece is a ball. So the double branched cover of a ball along a single unknotted arc is a ball!

OK so if $(B_1, k \cap B_1)$ is a trivial tangle with one unknotted arc, its double branched cover is a ball. Then $S$ bounds a ball on that side, so $S$ is inessential. Contradiction.

But what if $n > 2$? Then each side has $n/2 > 1$ arcs. Can $k$ still be prime? Yes — a prime knot can have a sphere intersecting it in more than 2 points where neither side is a trivial 2-strand tangle. The definition of prime knot only requires that there's no sphere intersecting $k$ in exactly 2 points that splits $k$ into two non-trivial tangles.

So the argument above only works for $n = 2$. For $n > 2$, we need a different approach.

Hmm, so the equivariant sphere theorem gives us a sphere $S$ with $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$, but $S$ might intersect $\tilde{k}$ in more than 2 points.

Let me reconsider. Maybe we should use a different approach.

Actually, I think the key result is due to the equivariant sphere theorem combined with the fact that we can choose $S$ to intersect the fixed set minimally.

Let me look at this from a different angle. There's a theorem by Heil (1970s?) or maybe it's attributed to others.

Actually, I recall now. The result that "if $k$ is prime then $M(k)$ is prime" is indeed true, and it's a consequence of the equivariant sphere theorem. The proof handles the general case.

Let me think about the case $\tau(S) \cap S = \emptyset$ more carefully.

If $\tau(S) \cap S = \emptyset$: Then $S$ and $\tau(S)$ are disjoint. Consider the projection $\pi: M(k) \to S^3$. The image $\pi(S)$ is a sphere in $S^3$ (since $\tau(S) \neq S$, the projection is 2-to-1 on $S$, so $\pi(S)$ is a sphere). This sphere $\pi(S)$ intersects $k$ in some points.

If $S \cap \tilde{k} = \emptyset$, then $\pi(S) \cap k = \emptyset$, so $\pi(S)$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $\pi(S)$ bounds a ball $B$ in $S^3$. The preimage $\pi^{-1}(B)$ is either one or two pieces. If $B \cap k = \emptyset$, then $\pi^{-1}(B)$ is two balls (double cover of a ball), and $S$ bounds one of them, so $S$ is inessential. If $B \cap k \neq \emptyset$... but we said $\pi(S) \cap k = \emptyset$, so $k$ is entirely inside or outside $B$. If $k \subset B$, then $\pi^{-1}(B) = M(k) \setminus \pi^{-1}(\overline{S^3 \setminus B})$, and $\pi^{-1}(B)$ is the double branched cover of $B$ along $k$, which is $M(k)$ minus a ball pair... this doesn't immediately give inessentiality. Hmm, but $S$ is essential and $\tau(S)$ is also essential and they're disjoint. The region between $S$ and $\tau(S)$ projects to the region between $\pi(S)$ and itself (which is $B$ or $\overline{S^3 \setminus B}$). Actually, $\pi^{-1}(\pi(S)) = S \cup \tau(S)$, and $\pi^{-1}(B)$ is the region between $S$ and $\tau(S)$ (if $k \subset B$) or the two outer regions. This is getting complicated.

Let me try a cleaner approach. I think the standard proof goes like this:

**Theorem**: If $k$ is a prime knot in $S^3$, then the double branched cover $\Sigma_2(k)$ is a prime 3-manifold.

**Proof sketch**: Suppose $\Sigma_2(k)$ is reducible. Let $\tau$ be the covering involution. By the equivariant sphere theorem, there exists an essential sphere $S$ in $\Sigma_2(k)$ such that either (i) $\tau(S) = S$ or (ii) $\tau(S) \cap S = \emptyset$.

**Case (ii)**: $\tau(S) \cap S = \emptyset$. Then $S$ and $\tau(S)$ are disjoint essential spheres. The sphere $S$ separates $\Sigma_2(k)$ into two pieces. Since $\tau(S)$ is disjoint from $S$, $\tau(S)$ lies entirely in one piece, say the piece $X$ bounded by $S$. Then $X$ contains an essential sphere $\tau(S)$, so $X$ is not a ball. But also, the other piece $Y$ (bounded by $S$ on the other side) must not be a ball (since $S$ is essential). Now, $\tau(Y)$ is the piece on the other side of $\tau(S)$ from $X$... hmm, this is getting complicated.

Actually, let me think about it differently. In case (ii), $S \cup \tau(S)$ consists of two disjoint spheres. They divide $\Sigma_2(k)$ into three pieces (or two if one sphere is nested). The projection to $S^3$ gives a sphere $\pi(S)$ (since $S$ and $\tau(S)$ project to the same sphere). This sphere $\pi(S)$ in $S^3$ intersects $k$ in some number of points.

If $\pi(S) \cap k = \emptyset$: $\pi(S)$ bounds a ball $B$ in $S^3$ (irreducibility of $S^3$). If $k \cap B = \emptyset$, then $\pi^{-1}(B)$ is two disjoint balls bounded by $S$ and $\tau(S)$, so both $S$ and $\tau(S)$ are inessential, contradiction. If $k \subset B$, then $\pi^{-1}(B) = \Sigma_2(k) \setminus \pi^{-1}(\overline{S^3 \setminus B})$, and $\pi^{-1}(\overline{S^3 \setminus B})$ is two balls (double cover of a ball with no branch points). So $\Sigma_2(k) = \pi^{-1}(B) \cup \text{(two balls)}$, meaning $\Sigma_2(k) = \pi^{-1}(B)$. But $\pi^{-1}(B)$ is bounded by $S \cup \tau(S)$, and it's the double branched cover of $B$ along $k$. The two balls $\pi^{-1}(\overline{S^3 \setminus B})$ are glued to $\pi^{-1}(B)$ along $S$ and $\tau(S)$. So $\Sigma_2(k)$ is obtained from $\pi^{-1}(B)$ by gluing two balls. This means $S$ and $\tau(S)$ each bound balls in $\Sigma_2(k)$ (the glued balls), so they're inessential. Contradiction.

So in case (ii) with $\pi(S) \cap k = \emptyset$, we get a contradiction.

If $\pi(S) \cap k \neq \emptyset$: Then $S \cap \tilde{k} \neq \emptyset$ (since points of $k$ on $\pi(S)$ correspond to fixed points on $S$ or $\tau(S)$). Actually, $\pi(S) \cap k$ consists of points where $S$ (or $\tau(S)$) intersects $\tilde{k}$. Since $\pi|_{\tilde{k}}: \tilde{k} \to k$ is a homeomorphism (1-to-1), $|\pi(S) \cap k| = |(S \cup \tau(S)) \cap \tilde{k}| = |S \cap \tilde{k}| + |\tau(S) \cap \tilde{k}| = 2|S \cap \tilde{k}|$ (by symmetry). So $|S \cap \tilde{k}| = |\pi(S) \cap k|/2$.

The sphere $\pi(S)$ intersects $k$ in $m = |\pi(S) \cap k|$ points, dividing $k$ into $m$ arcs split between the two balls bounded by $\pi(S)$. Since $S$ is essential, neither side of $S$ in $\Sigma_2(k)$ is a ball.

Hmm, I think this case is harder to handle directly. Let me look for a different approach.

Actually, maybe I should think about this problem differently. Let me recall: is the statement actually TRUE?

I believe the answer is **yes**, and this is a known result. Let me try to recall the reference. I think it might be due to the equivariant sphere theorem, and the result might be attributed to Waldhausen or to the work of Meeks-Yau on equivariant spheres.

Actually, let me reconsider. I recall that for the double branched cover, the result that prime knot implies prime double branched cover is indeed true. The proof uses the equivariant sphere theorem.

Let me try to write a cleaner proof.

**Proof**:

Suppose $k$ is prime but $M = \Sigma_2(k)$ is reducible. Let $\tau: M \to M$ be the covering involution with fixed set $\tilde{k}$ (the lift of $k$). By the Equivariant Sphere Theorem (Meeks-Yau / Meeks-Simon-Yau), there exists an essential 2-sphere $S \subset M$ such that either $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

**Case 1: $\tau(S) \cap S = \emptyset$.**

The sphere $S$ separates $M$ into two components $M_1$ and $M_2$. Since $\tau(S) \neq S$ and $\tau(S) \cap S = \emptyset$, $\tau(S) \subset M_i$ for some $i$. WLOG $\tau(S) \subset M_1$. Then $\tau(M_2) \subset M_1$ (since $\tau(S) = \partial \tau(M_2) \subset M_1$). So $M_1$ contains both $\tau(S)$ and $\tau(M_2)$, and $M_1 \setminus \tau(M_2)$ is the region between $S$ and $\tau(S)$.

The projection $\pi: M \to S^3$ maps $S$ and $\tau(S)$ to the same sphere $\Sigma = \pi(S) \subset S^3$. The sphere $\Sigma$ separates $S^3$ into two balls $B_1, B_2$.

If $\Sigma \cap k = \emptyset$: Then $k$ lies in one ball, say $B_1$. The preimage $\pi^{-1}(B_2)$ is the double (unbranched) cover of a ball, which is two disjoint balls. These two balls are bounded by $S$ and $\tau(S)$, so both $S$ and $\tau(S)$ bound balls in $M$, contradicting their essentiality.

If $\Sigma \cap k \neq \emptyset$: Let $m = |\Sigma \cap k|$. Then $m \geq 1$. Since $\tilde{k}$ is a closed curve and $S$ separates $M$, $\tilde{k}$ crosses $S$ an even number of times, so $|S \cap \tilde{k}|$ is even. Similarly for $\tau(S)$. We have $m = |S \cap \tilde{k}| + |\tau(S) \cap \tilde{k}| = 2|S \cap \tilde{k}|$, so $m$ is even, $m \geq 2$.

Now, $\Sigma$ intersects $k$ in $m \geq 2$ points. The ball $B_1$ contains $m_1$ arcs of $k$ and $B_2$ contains $m_2$ arcs, with $m_1 + m_2 = m$. The preimage $\pi^{-1}(B_i)$ is the double branched cover of $B_i$ along $m_i$ arcs, which is a 3-manifold with boundary $S \cup \tau(S)$ (two copies of $\Sigma$, i.e., two spheres).

Hmm wait, $\pi^{-1}(\Sigma) = S \cup \tau(S)$, and $\pi^{-1}(B_i)$ is bounded by $S \cup \tau(S)$. But $\pi^{-1}(B_i)$ is connected (it's the double branched cover of a ball along arcs, which is connected as long as there's at least one arc, or if there are no arcs, it's two balls). If $m_i = 0$, $\pi^{-1}(B_i)$ is two balls, and $S, \tau(S)$ each bound a ball, contradiction. If $m_i \geq 1$, $\pi^{-1}(B_i)$ is connected with boundary $S \cup \tau(S)$.

Now, $M = \pi^{-1}(B_1) \cup \pi^{-1}(B_2)$, glued along $S \cup \tau(S)$. The sphere $S$ is essential in $M$, so $S$ doesn't bound a ball in $M$. But $S$ is part of the boundary of both $\pi^{-1}(B_1)$ and $\pi^{-1}(B_2)$.

For $S$ to be essential, neither $\pi^{-1}(B_1)$ nor $\pi^{-1}(B_2)$ can be a ball with boundary $S$ (but their boundaries are $S \cup \tau(S)$, two spheres, so neither is a ball anyway, unless one sphere caps off).

Hmm, this is getting complicated. Let me think about whether we can reduce to the $m = 2$ case.

Actually, I think the key insight is: we can choose $S$ to minimize $|S \cap \tilde{k}|$. Among all essential equivariant spheres (either invariant or disjoint from their image), choose one minimizing the intersection with $\tilde{k}$.

If $S$ is $\tau$-invariant and $|S \cap \tilde{k}| = 2$: Then $\pi(S) = \Sigma$ intersects $k$ in 2 points. Since $k$ is prime, one of the two tangles is trivial. The double branched cover of a trivial tangle (ball with one unknotted arc) is a ball. So $S$ bounds a ball on one side, contradicting essentiality.

If $S$ is $\tau$-invariant and $|S \cap \tilde{k}| = 2n > 2$: Can we find an innermost disk argument to reduce? Consider $S \cap \tilde{k}$, which is $2n$ points. The sphere $S$ separates $M$ into $X$ and $Y$. The knot $\tilde{k}$ passes through $S$ $2n$ times, so $\tilde{k} \cap X$ consists of $n$ arcs and $\tilde{k} \cap Y$ consists of $n$ arcs (since $\tilde{k}$ is a closed curve crossing $S$ $2n$ times).

Now, $\pi(S) = \Sigma$ intersects $k$ in $2n$ points (since $\tau$ fixes $\tilde{k}$ pointwise, each point of $S \cap \tilde{k}$ projects to a distinct point of $k \cap \Sigma$). So $\Sigma$ intersects $k$ in $2n$ points, dividing $k$ into $2n$ arcs, $n$ in each ball $B_1, B_2$.

Hmm, but $k$ being prime doesn't directly tell us about spheres intersecting $k$ in more than 2 points.

I think the right approach is to use the fact that we can isotope $S$ to reduce intersections. Let me think about innermost circle arguments.

Consider the projection $\pi|_S: S \to \Sigma$. This is a 2-to-1 branched cover (branched at the $2n$ points $S \cap \tilde{k}$), since $S$ is $\tau$-invariant. Actually, $\tau|_S$ is an involution on $S$ with fixed points $S \cap \tilde{k}$ (an even number $2n$). The quotient $S/\tau = \Sigma$ is a sphere.

Now, the knot $k$ intersects $\Sigma$ in $2n$ points. The sphere $\Sigma$ bounds two balls $B_1, B_2$ in $S^3$, with $k \cap B_i$ consisting of $n$ arcs each.

Since $k$ is prime, can we find a sub-sphere of $\Sigma$ that intersects $k$ in exactly 2 points and splits off a trivial tangle? Not directly, because primality is about spheres intersecting $k$ in 2 points, not about arbitrary configurations.

Hmm, let me think about this differently. Maybe I should use the fact that $k$ being prime means $S^3 \setminus N(k)$ is irreducible (where $N(k)$ is a tubular neighborhood). Actually, that's not quite right either. $k$ being prime means there's no decomposing sphere (a sphere intersecting $k$ in 2 points that splits $k$ into two non-trivial tangles). The complement $S^3 \setminus \nu(k)$ being irreducible is equivalent to $k$ being non-split, not prime.

Wait, actually: $k$ is prime iff $S^3 \setminus \nu(k)$ is irreducible AND $k$ is non-trivial. No, that's not right either. A knot $k$ is prime if $k = k_1 \# k_2$ implies $k_1$ or $k_2$ is the unknot. The exterior $E(k) = S^3 \setminus \nu(k)$ is irreducible for any non-split knot (prime or not). The difference is about essential annuli or something else.

Actually, for knots: $k$ is prime iff $E(k)$ is irreducible and $E(k)$ contains no essential annulus with boundary on $\partial E(k)$ that is not boundary-parallel. Hmm, I don't think that's exactly right either.

Let me reconsider. A knot $k$ is prime if whenever $k = k_1 \# k_2$, one of $k_i$ is the unknot. Equivalently, there is no 2-sphere in $S^3$ intersecting $k$ transversely in exactly 2 points such that both tangles $(B_i, k \cap B_i)$ are non-trivial.

OK so I think the proof needs to handle the case $|S \cap \tilde{k}| > 2$ more carefully. Let me think about whether we can always reduce to the 2-point case.

Alternative approach: Maybe use the fact that if $M(k)$ is reducible, then $k$ can be written as a connected sum, contradicting primality.

Here's the idea: If $M(k) = M_1 \# M_2$, then the covering involution $\tau$ on $M(k)$ restricts to... well, by the equivariant sphere theorem, we can find the decomposing sphere to be equivariant. Then the projection gives a decomposing sphere for $k$, showing $k$ is composite.

Let me be more precise. Suppose $M(k)$ is reducible. By the equivariant sphere theorem, there exists an essential sphere $S$ with $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

**Subcase 1a: $\tau(S) = S$ and $S \cap \tilde{k} = \emptyset$.**

Then $\pi(S) = \Sigma$ is a sphere in $S^3 \setminus k$. Since $S^3$ is irreducible, $\Sigma$ bounds a ball $B$. If $B \cap k = \emptyset$, then $\pi^{-1}(B)$ is two balls (unbranched double cover), and $S$ bounds a ball, contradicting essentiality. If $k \subset B$, then $\pi^{-1}(\overline{S^3 \setminus B})$ is two balls, and $S$ bounds a ball (one of the two), contradicting essentiality. So this subcase is impossible.

**Subcase 1b: $\tau(S) = S$ and $S \cap \tilde{k} \neq \emptyset$.**

Let $|S \cap \tilde{k}| = 2n \geq 2$. The sphere $\Sigma = \pi(S)$ intersects $k$ in $2n$ points.

Now I want to show that we can find a sphere intersecting $k$ in exactly 2 points that decomposes $k$ non-trivially.

Consider the $2n$ points $p_1, \ldots, p_{2n} = \Sigma \cap k$ on the sphere $\Sigma$. These divide $k$ into $2n$ arcs. The ball $B_1$ contains $n$ of these arcs (forming a tangle $T_1$) and $B_2$ contains the other $n$ arcs (tangle $T_2$).

The double branched cover of $(B_i, T_i)$ is one side of $S$ in $M(k)$. Since $S$ is essential, neither side is a ball. The double branched cover of a ball along a tangle is a ball if and only if the tangle is "trivial" in a specific sense.

Hmm, but I need to connect this to the primality of $k$. Let me think about whether we can find a 2-point sphere from the $2n$-point sphere.

Consider the $n$ arcs of $T_1$ in $B_1$. If $n \geq 2$, consider two arcs $\alpha, \beta$ of $T_1$. There exists a disk $D$ in $B_1$ with $\partial D$ consisting of $\alpha$, $\beta$, and two arcs on $\partial B_1 = \Sigma$ connecting the endpoints of $\alpha$ and $\beta$. (This is because the arcs are properly embedded in the ball.) Using this disk, we can do surgery on $\Sigma$ to get a new sphere $\Sigma'$ that intersects $k$ in fewer points.

Actually, this is the standard innermost arc argument. Let me think about it more carefully.

The $2n$ points on $\Sigma$ divide $\Sigma$ into $2n$ arcs. The knot $k$ consists of $2n$ arcs, $n$ in $B_1$ and $n$ in $B_2$. Consider the arcs in $B_1$: they connect pairs of the $2n$ points on $\Sigma$. This gives a pairing of the $2n$ points.

Now, consider an arc $\alpha$ of $k$ in $B_1$ connecting points $p_i$ and $p_j$ on $\Sigma$. Together with an arc $\gamma$ on $\Sigma$ connecting $p_i$ and $p_j$, $\alpha \cup \gamma$ forms a loop. If we can find a disk in $B_1$ bounded by $\alpha \cup \gamma$ (for some $\gamma$ on $\Sigma$), we can use it to surger $\Sigma$ and reduce the number of intersection points.

Actually, since $B_1$ is a ball and $\alpha$ is a properly embedded arc, there always exists a disk $D$ in $B_1$ with $\alpha \subset \partial D$ and $\partial D \cap \Sigma$ being an arc $\gamma$ on $\Sigma$ connecting $p_i$ and $p_j$. We can choose $D$ to be innermost (intersecting $k$ minimally). If $D \cap k = \alpha$ (i.e., $D$ intersects $k$ only in $\alpha$), then we can surger $\Sigma$ along $D$: replace the arc $\gamma$ on $\Sigma$ with $\alpha$ to get a new sphere $\Sigma'$ that intersects $k$ in $2n - 2$ points (we've removed $p_i$ and $p_j$ from the intersection).

But this new sphere $\Sigma'$ might not be equivariantly liftable, and the corresponding sphere in $M(k)$ might not be essential.

I think this approach is getting too complicated for me to work out in full detail. Let me try to recall the actual theorem and its proof.

I believe the result is:

**Theorem** (folklore / equivariant sphere theorem): If $k$ is a prime knot, then $\Sigma_2(k)$ is prime.

And the proof goes through the equivariant sphere theorem, handling the cases as I outlined, with the key step being that an equivariant essential sphere projects to a decomposing sphere for $k$.

Let me try to think about this more carefully for the case $\tau(S) = S$ and $|S \cap \tilde{k}| = 2n$.

Actually, I think the key point is this: we choose $S$ to be an equivariant essential sphere minimizing $|S \cap \tilde{k}|$. Then we show $|S \cap \tilde{k}| = 2$ (i.e., $n = 1$), which gives a decomposing sphere for $k$, contradicting primality.

Why must $n = 1$? Suppose $n \geq 2$. Then $\Sigma = \pi(S)$ intersects $k$ in $2n \geq 4$ points. Consider the $n$ arcs of $k$ in $B_1$. Take an innermost pair: two consecutive points $p_i, p_{i+1}$ on $\Sigma$ (in the cyclic order) that are connected by an arc $\alpha$ of $k$ in $B_1$. "Consecutive" means the arc $\gamma$ on $\Sigma$ from $p_i$ to $p_{i+1}$ contains no other points of $\Sigma \cap k$.

The arc $\alpha$ in $B_1$ and the arc $\gamma$ on $\Sigma$ bound a disk $D$ in $B_1$ (since $B_1$ is a ball). We can choose $D$ to be innermost, so $D \cap k = \alpha$.

Now surger $\Sigma$ along $D$: replace $\gamma \subset \Sigma$ with $\alpha$ to get a new sphere $\Sigma'$. Then $\Sigma' \cap k = (\Sigma \cap k) \setminus \{p_i, p_{i+1}\}$, so $|\Sigma' \cap k| = 2n - 2$.

The sphere $\Sigma'$ bounds two balls $B_1', B_2'$ in $S^3$. One of them, say $B_1'$, is contained in $B_1$ (roughly $B_1$ minus a neighborhood of $D$), and $B_2'$ contains $B_2$ plus a neighborhood of $D$.

Now, does $\Sigma'$ lift to an equivariant sphere in $M(k)$ with fewer intersections with $\tilde{k}$? The sphere $\Sigma'$ intersects $k$ in $2(n-1)$ points. The double branched cover of $S^3$ along $k$ has a sphere $\tilde{S}'$ lying over $\Sigma'$ (the preimage $\pi^{-1}(\Sigma')$ is a sphere if $\Sigma'$ is equivariant... but $\Sigma'$ might not be equivariant in the right sense).

Hmm, actually $\pi^{-1}(\Sigma')$ is always a sphere (since $\Sigma'$ is a sphere in $S^3$ and the branched cover is 2-to-1). Wait, no. $\pi^{-1}(\Sigma')$ is a double branched cover of $\Sigma'$ branched at $\Sigma' \cap k$. If $|\Sigma' \cap k| = 2(n-1)$, then $\pi^{-1}(\Sigma')$ is a double branched cover of $S^2$ branched at $2(n-1)$ points. If $n-1 = 0$, this is two spheres (unbranched double cover of $S^2$). If $n-1 \geq 1$, this is a connected surface: a double branched cover of $S^2$ branched at $2m$ points (for $m \geq 1$) is a closed surface of genus... well, by Riemann-Hurwitz, $\chi(\tilde{\Sigma}) = 2\chi(\Sigma) - 2m = 4 - 2m$. For $m = 1$: $\chi = 2$, so it's a sphere. For $m = 2$: $\chi = 0$, so it's a torus. For $m \geq 3$: $\chi < 0$, higher genus.

So if $n = 2$ (so $n - 1 = 1$), $\pi^{-1}(\Sigma')$ is a sphere with $|\pi^{-1}(\Sigma') \cap \tilde{k}| = 2$, which is an equivariant sphere with fewer intersections. If $n \geq 3$, $\pi^{-1}(\Sigma')$ is not a sphere, so this doesn't directly give us a sphere.

So the surgery argument only reduces from $n = 2$ to $n = 1$. For $n \geq 3$, we get a higher-genus surface, not a sphere.

Hmm, so this approach doesn't fully work. Let me think differently.

Maybe we need to use a different minimality condition. Instead of minimizing $|S \cap \tilde{k}|$ among equivariant essential spheres, we should minimize among all essential spheres (not necessarily equivariant) and then apply the equivariant sphere theorem.

Actually, wait. Let me reconsider the equivariant sphere theorem. The theorem says: if $M$ is orientable and $\tau$ is an involution, and $M$ is reducible, then there exists a collection of disjoint essential spheres $\{S_1, \ldots, S_k\}$ such that the collection is $\tau$-invariant (as a set) and the spheres are pairwise disjoint and non-parallel, and this collection is maximal. Moreover, we can arrange that each $S_i$ is either $\tau$-invariant or $\tau(S_i) = S_j$ for some $j \neq i$.

Actually, the equivariant sphere theorem as usually stated: If $M$ is a reducible 3-manifold and $\tau$ is an involution on $M$, then $M$ contains an essential sphere $S$ such that either $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.

But there's a stronger version: we can find a maximal system of disjoint non-parallel essential spheres that is $\tau$-invariant as a set.

Let me try a different approach. Let me think about what happens in Case 2.

**Case 2: $\tau(S) \cap S = \emptyset$.**

$S$ and $\tau(S)$ are disjoint essential spheres. They cobound a region $R$ in $M$ (the region between them), and $M = R \cup X \cup Y$ where $X$ is on the other side of $S$ from $R$ and $Y$ is on the other side of $\tau(S)$ from $R$. Note $\tau(X) = Y$ and $\tau(R) = R$ (with $\tau$ swapping $S$ and $\tau(S)$).

The projection $\pi(S) = \pi(\tau(S)) = \Sigma$, a sphere in $S^3$. The region $R$ projects to one of the two balls bounded by $\Sigma$, say $B_1$, and $X \cup Y$ projects to the other ball $B_2$. (Or vice versa.) Since $\tau$ swaps $X$ and $Y$ and $\tau(R) = R$, we have $\pi(R) = B_1$ (a ball) and $\pi(X \cup Y) = B_2$ (a ball), with $\pi|_R: R \to B_1$ a double branched cover (branched along $k \cap B_1$) and $\pi|_{X \cup Y}: X \cup Y \to B_2$ a double branched cover (branched along $k \cap B_2$).

If $k \cap B_1 = \emptyset$: $R$ is the double unbranched cover of a ball, which is two balls. But $R$ is bounded by $S \cup \tau(S)$ (two spheres), so $R$ being two balls means $S$ and $\tau(S)$ each bound a ball, contradicting essentiality.

If $k \cap B_2 = \emptyset$: $X \cup Y$ is the double unbranched cover of a ball, which is two balls $X$ and $Y$. So $S$ bounds the ball $X$ and $\tau(S)$ bounds the ball $Y$, contradicting essentiality.

So both $k \cap B_1$ and $k \cap B_2$ are nonempty. Let $|k \cap B_1| = m_1$ arcs and $|k \cap B_2| = m_2$ arcs, with $m_1 + m_2 = m = |\Sigma \cap k|$ and $m_1, m_2 \geq 1$.

Now, $R$ is the double branched cover of $B_1$ along $m_1$ arcs, and $X \cup Y$ is the double branched cover of $B_2$ along $m_2$ arcs. Since $S$ is essential, $X$ is not a ball (and $Y = \tau(X)$ is not a ball). Since $\tau(S)$ is essential, $R$ is not a ball (well, $R$ has two boundary components, so it can't be a ball anyway).

Hmm, for $S$ to be essential, we need $X$ to not be a ball. $X$ is one component of the double branched cover of $B_2$ along $m_2$ arcs. If $m_2 = 1$ (one arc in $B_2$), the double branched cover of a ball along one arc is a ball (as we computed earlier). So $X$ would be a ball, contradicting essentiality. So $m_2 \geq 2$.

Similarly, $m_1 \geq 1$ (we already knew this). But we also need $R$ to not be a product (otherwise $S$ and $\tau(S)$ would be parallel, which might still be OK for essentiality... actually, parallel essential spheres are still essential).

So $m_2 \geq 2$, meaning $B_2$ contains at least 2 arcs of $k$. And $m_1 \geq 1$.

Now, $\Sigma$ is a sphere in $S^3$ intersecting $k$ in $m = m_1 + m_2$ points, with $m_1 \geq 1$ arcs on one side and $m_2 \geq 2$ arcs on the other.

Can we use this to show $k$ is composite? Not directly, because $\Sigma$ intersects $k$ in more than 2 points.

OK, I think I need to take a step back and think about whether the result is actually true.

Let me consider potential counterexamples. Are there prime knots whose double branched covers are reducible?

For 2-bridge knots: double branched covers are lens spaces, which are prime (irreducible). ✓

For torus knots: double branched covers are Seifert fibered spaces over $S^2$ with 3 exceptional fibers, which are irreducible. ✓

For hyperbolic knots: the double branched cover is often hyperbolic (hence irreducible), but not always. However, even if not hyperbolic, could it be reducible?

Actually, I recall that for alternating knots, the double branched cover is irreducible. This follows from the work of Menasco or from the fact that alternating knots have essential checkerboard surfaces whose lifts give essential surfaces.

More generally, I believe the result is true for all prime knots. Let me search my memory for the precise theorem.

I think the key theorem is:

**Theorem**: Let $k$ be a knot in $S^3$. Then $k$ is prime if and only if $\Sigma_2(k)$ is prime.

The "only if" direction (prime knot → prime double branched cover) is what we need to prove. The "if" direction is easy (if $k = k_1 \# k_2$, then $\Sigma_2(k) = \Sigma_2(k_1) \# \Sigma_2(k_2)$).

For the "only if" direction, I believe the proof uses the equivariant sphere theorem. Let me try to make the argument work.

The issue was handling the case $|S \cap \tilde{k}| > 2$. Let me think about this more carefully.

Actually, maybe I should think about it in terms of the knot complement. The double branched cover $\Sigma_2(k)$ can be obtained by taking the double branched cover of $S^3$ along $k$. There's a relationship between $\Sigma_2(k)$ and the knot complement $E(k) = S^3 \setminus \nu(k)$.

Specifically, $\Sigma_2(k) \setminus \nu(\tilde{k})$ is the double cover of $E(k)$. The double cover of $E(k)$ is determined by the mod 2 linking number with $k$, which is the unique nontrivial homomorphism $\pi_1(E(k)) \to \mathbb{Z}/2$.

If $k$ is prime, then $E(k)$ is irreducible (this is true for any non-split knot). The double cover of an irreducible 3-manifold is... not necessarily irreducible. Hmm.

Actually, the double cover of $E(k)$ might be reducible even if $E(k)$ is irreducible. For example, the double cover of a knot complement can be reducible for certain knots.

But we need $\Sigma_2(k)$ to be prime, which is stronger than $\Sigma_2(k) \setminus \nu(\tilde{k})$ being irreducible (since we also need to cap off with the solid torus $\nu(\tilde{k})$).

Let me think about this differently. $\Sigma_2(k) = (\text{double cover of } E(k)) \cup_{\partial} \nu(\tilde{k})$, where $\nu(\tilde{k})$ is a solid torus. The double cover of $E(k)$ has boundary a torus $T$, and we glue in a solid torus to get $\Sigma_2(k)$.

If $\Sigma_2(k)$ is reducible, there's an essential sphere $S$ in $\Sigma_2(k)$. We can isotope $S$ to intersect $\nu(\tilde{k})$ in a minimal number of meridian disks. Then $S \cap (\Sigma_2(k) \setminus \nu(\tilde{k}))$ is a planar surface in the double cover of $E(k)$.

Hmm, this is also getting complicated. Let me try yet another approach.

Let me look at this from the perspective of the equivariant sphere theorem more carefully, and try to handle the general case.

**Claim**: We can choose the equivariant essential sphere $S$ such that $|S \cap \tilde{k}| = 2$.

**Proof of claim**: Among all equivariant essential spheres (i.e., $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$), choose $S$ minimizing $|S \cap \tilde{k}|$ (counting $|S \cap \tilde{k}| + |\tau(S) \cap \tilde{k}|$ if $\tau(S) \neq S$).

First, $|S \cap \tilde{k}| \neq 0$ (shown above: if $S \cap \tilde{k} = \emptyset$, then $S$ is inessential).

Second, $|S \cap \tilde{k}|$ is even (since $S$ separates $M$ and $\tilde{k}$ is a closed curve, it must cross $S$ an even number of times).

So $|S \cap \tilde{k}| \geq 2$. Suppose $|S \cap \tilde{k}| = 2n \geq 4$. We'll derive a contradiction by finding an equivariant essential sphere with fewer intersections.

**Subcase: $\tau(S) = S$, $|S \cap \tilde{k}| = 2n \geq 4$.**

$\Sigma = S/\tau = \pi(S)$ is a sphere in $S^3$ intersecting $k$ in $2n$ points. The $2n$ points divide $k$ into $2n$ arcs, $n$ in each ball $B_1, B_2$ bounded by $\Sigma$.

Consider the $n$ arcs of $k$ in $B_1$. Label the $2n$ points on $\Sigma$ as $p_1, \ldots, p_{2n}$ in cyclic order. The arcs in $B_1$ pair up these points. Since $n \geq 2$, there exist two points $p_i, p_j$ that are paired by an arc $\alpha$ in $B_1$ and are "adjacent" in the sense that one of the two arcs on $\Sigma$ between $p_i$ and $p_j$ contains no other $p_\ell$.

Wait, this isn't guaranteed. The pairing might not have any adjacent pairs. For example, with 4 points $p_1, p_2, p_3, p_4$ in cyclic order, the arcs in $B_1$ might pair $p_1$ with $p_3$ and $p_2$ with $p_4$ (the "crossing" pairing). In this case, no pair is adjacent.

But in that case, the arcs in $B_1$ form a non-trivial tangle. And the arcs in $B_2$ also pair the points, and the two pairings together form the knot $k$.

Hmm, let me think about this differently. If no pair of points connected by an arc in $B_1$ is adjacent on $\Sigma$, then the tangle in $B_1$ is "fully crossed". But we can still do surgery.

Take any arc $\alpha$ in $B_1$ connecting $p_i$ and $p_j$. There's a disk $D$ in $B_1$ with $\partial D = \alpha \cup \gamma$ where $\gamma$ is an arc on $\Sigma$ from $p_i$ to $p_j$. Choose $D$ to be innermost (minimizing $|D \cap k|$). The interior of $D$ might intersect $k$ in some arcs.

If $D \cap k = \alpha$ (interior of $D$ is disjoint from $k$): Surgery on $\Sigma$ along $D$ gives a new sphere $\Sigma'$ with $|\Sigma' \cap k| = 2n - 2$. If $2n - 2 = 2$ (i.e., $n = 2$), then $\Sigma'$ is a 2-point sphere, and we can analyze it using primality. If $2n - 2 \geq 4$, we can repeat.

If $D \cap k \supsetneq \alpha$: The interior of $D$ intersects $k$ in some arcs. Take an innermost subdisk $D'$ of $D$ (bounded by a sub-arc of $\alpha$ or $k$ and a sub-arc of $\gamma$ or $k$). This gives a surgery that reduces intersections.

Actually, the standard innermost disk argument works as follows: Among all disks in $B_1$ with boundary consisting of an arc of $k$ and an arc on $\Sigma$, choose one $D$ that is innermost (its interior is disjoint from $k$). Such a disk exists because we can take any disk and if its interior intersects $k$, we can find a sub-disk that is innermost.

With this innermost disk $D$ (interior disjoint from $k$, $\partial D = \alpha \cup \gamma$ where $\alpha \subset k$ and $\gamma \subset \Sigma$), surgery on $\Sigma$ gives $\Sigma'$ with $|\Sigma' \cap k| = 2n - 2$.

Now, $\Sigma'$ bounds two balls $B_1', B_2'$. The knot $k$ intersects $\Sigma'$ in $2(n-1)$ points. We need to check that $\Sigma'$ lifts to an essential equivariant sphere in $M(k)$.

$\pi^{-1}(\Sigma')$ is the double branched cover of $\Sigma'$ branched at $\Sigma' \cap k = 2(n-1)$ points. As computed earlier:
- If $n-1 = 1$ (i.e., $n = 2$): $\pi^{-1}(\Sigma')$ is a sphere (double branched cover of $S^2$ at 2 points = $S^2$).
- If $n-1 \geq 2$: $\pi^{-1}(\Sigma')$ has genus $\geq 1$, not a sphere.

So for $n = 2$, we get a sphere $\tilde{S}' = \pi^{-1}(\Sigma')$ with $|\tilde{S}' \cap \tilde{k}| = 2$, which is equivariant (since $\pi^{-1}(\Sigma')$ is always $\tau$-invariant as a set). If $\tilde{S}'$ is essential, this contradicts the minimality of $|S \cap \tilde{k}|$.

Is $\tilde{S}'$ essential? The sphere $\Sigma'$ decomposes $S^3$ into $B_1'$ and $B_2'$, with $k$ having $1$ arc in one ball and $2n - 3$ arcs in the other (wait, let me recount). Originally $\Sigma$ had $2n$ points, $n$ arcs in $B_1$, $n$ arcs in $B_2$. After surgery along $D$ (which is in $B_1$), $\Sigma'$ has $2(n-1)$ points. The ball $B_1'$ (roughly $B_1$ minus a neighborhood of $D$) contains $n - 1$ arcs, and $B_2'$ (roughly $B_2$ plus a neighborhood of $D$) contains $n - 1$ arcs as well? No, let me think again.

Actually, surgery along $D$ removes the two points $p_i, p_j$ from $\Sigma \cap k$ and the arc $\alpha$ from $k \cap B_1$. The new sphere $\Sigma'$ intersects $k$ in $2n - 2$ points. The ball $B_1'$ (the one that doesn't contain the surgery region) contains the remaining $n - 1$ arcs of the original $B_1$ tangle. The ball $B_2'$ contains the original $n$ arcs of $B_2$ plus... hmm, actually the arc $\alpha$ is now on the $B_2'$ side. So $B_2'$ contains $n$ arcs from $B_2$ and the arc $\alpha$ is now part of $k$ on the $B_2'$ side, but $\alpha$ connects to the rest of $k$ through the other arcs...

This is getting confusing. Let me think about it more carefully.

$k$ is a circle. $\Sigma$ intersects $k$ in $2n$ points, dividing $k$ into $2n$ arcs: $\alpha_1, \beta_1, \alpha_2, \beta_2, \ldots, \alpha_n, \beta_n$ where $\alpha_i$ are in $B_1$ and $\beta_i$ are in $B_2$ (alternating). So $k = \alpha_1 \beta_1 \alpha_2 \beta_2 \cdots \alpha_n \beta_n$.

Surgery along $D$ (with $\partial D = \alpha_1 \cup \gamma$) removes $\alpha_1$ from $B_1$ and replaces $\gamma \subset \Sigma$ with $\alpha_1$. The new sphere $\Sigma'$ doesn't intersect $k$ at the endpoints of $\alpha_1$ (those points are now on $\alpha_1 \subset \Sigma'$, not on $k \cap \Sigma'$). Wait, no. $\Sigma'$ is obtained from $\Sigma$ by replacing $\gamma$ with $\alpha_1$. The points $p_i, p_j$ (endpoints of $\alpha_1$) are on both $\Sigma$ and $k$. After surgery, $\Sigma'$ passes through $\alpha_1$ instead of $\gamma$. At the points $p_i, p_j$, $\Sigma'$ meets $k$ (since $\alpha_1 \subset k$ and $\alpha_1 \subset \Sigma'$). Hmm, so actually $\Sigma' \cap k$ still contains $p_i$ and $p_j$?

No wait. $\Sigma'$ is a new sphere obtained by surgery. $\Sigma' = (\Sigma \setminus \gamma) \cup \alpha_1$. The intersection $\Sigma' \cap k$: $\Sigma \setminus \gamma$ intersects $k$ at the $2n - 2$ points other than $p_i, p_j$. And $\alpha_1 \subset k$, so $\alpha_1 \cap k = \alpha_1$, but $\alpha_1$ is part of $\Sigma'$ and part of $k$, so $\Sigma' \cap k$ includes $\alpha_1$. But we want transverse intersection. We should push $\Sigma'$ slightly off $k$ along $\alpha_1$.

After a small perturbation, $\Sigma' \cap k$ consists of the $2n - 2$ points (we've removed $p_i$ and $p_j$). The arc $\alpha_1$ is now on one side of $\Sigma'$.

So $k$ is divided by $\Sigma'$ into $2(n-1)$ arcs. The arc $\alpha_1$ is now entirely on one side (say $B_2'$). The remaining arcs: $n - 1$ arcs from the original $B_1$ (minus $\alpha_1$) are on the $B_1'$ side, and $n$ arcs from $B_2$ plus $\alpha_1$ are on the $B_2'$ side. But wait, $\alpha_1$ connects to $\beta$-arcs on both ends. After removing $p_i, p_j$ from the intersection, the arcs of $k$ on the $B_2'$ side are: $\beta_{i-1} \alpha_1 \beta_i$ (merged into one arc) and the other $\beta$-arcs. So $B_2'$ has $n - 1$ arcs (one of which is $\beta_{i-1} \alpha_1 \beta_i$, and the rest are the other $\beta$-arcs). And $B_1'$ has $n - 1$ arcs.

So both sides have $n - 1$ arcs. Good.

Now, for $n = 2$: both sides have 1 arc. $\Sigma'$ intersects $k$ in 2 points. $\pi^{-1}(\Sigma')$ is a sphere with $|\pi^{-1}(\Sigma') \cap \tilde{k}| = 2$.

Is this sphere essential? The sphere $\Sigma'$ decomposes $(S^3, k)$ into two tangles, each with 1 arc. The double branched cover of each side is a 3-manifold bounded by $\pi^{-1}(\Sigma')$. For $\pi^{-1}(\Sigma')$ to be essential, neither side's double branched cover should be a ball.

The double branched cover of a ball along 1 arc is a ball (as we showed). So if either tangle is a trivial 1-arc tangle (unknotted arc), the corresponding side's double branched cover is a ball, and $\pi^{-1}(\Sigma')$ is inessential.

But if both tangles are non-trivial (knotted arcs), then both sides' double branched covers are not balls, and $\pi^{-1}(\Sigma')$ is essential.

Hmm, but if both tangles are non-trivial, then $\Sigma'$ is a decomposing sphere for $k$ showing $k$ is composite. But we assumed $k$ is prime, so one tangle must be trivial, making $\pi^{-1}(\Sigma')$ inessential.

So for $n = 2$: the surgery gives an equivariant sphere $\tilde{S}'$ with $|\tilde{S}' \cap \tilde{k}| = 2$, but it's inessential (because $k$ is prime). So we can't use it to contradict minimality.

Hmm, so the minimality argument doesn't directly work because the surgically reduced sphere might be inessential.

But wait — if $\tilde{S}'$ is inessential, it bounds a ball in $M(k)$. The ball is the double branched cover of the trivial tangle. Can we use this to simplify $S$?

If $\tilde{S}'$ bounds a ball $B$ in $M(k)$, and $|\tilde{S}' \cap \tilde{k}| = 2$, then $B$ contains an arc of $\tilde{k}$ (the lift of the trivial arc). We can use $B$ to isotope $S$ and reduce $|S \cap \tilde{k}|$.

Here's the idea: $S$ and $\tilde{S}'$ are both spheres in $M(k)$. $\tilde{S}'$ has 2 intersections with $\tilde{k}$ and $S$ has $2n = 4$ intersections. We can use the ball $B$ bounded by $\tilde{S}'$ to isotope part of $S$ through $B$, reducing the intersection with $\tilde{k}$.

Actually, let me think about this more carefully. $S$ and $\tilde{S}'$ are two spheres in $M(k)$. We can isotope them to be transverse and consider their intersection circles. An innermost circle of $S \cap \tilde{S}'$ on $\tilde{S}'$ bounds a disk $D'$ on $\tilde{S}'$ that is either inside or outside $B$. If $D' \subset B$, we can surger $S$ along $D'$ (replacing a disk of $S$ with $D'$), which doesn't change the topological type of $S$ (it's still a sphere) but might change $|S \cap \tilde{k}|$.

This is getting very involved. Let me try to think about whether there's a cleaner proof.

Actually, I recall now that there's a cleaner approach using the following fact:

**Fact**: The double branched cover of $S^3$ along $k$ is irreducible if and only if $k$ is prime.

Wait, is this actually a known theorem? Let me think about whether it's true.

The "if" direction: $k$ prime $\Rightarrow$ $\Sigma_2(k)$ irreducible (hence prime, since $\Sigma_2(k)$ is a closed orientable 3-manifold $\neq S^3$ for non-trivial $k$, and irreducible closed 3-manifolds are prime).

Actually, for a closed orientable 3-manifold, irreducible is equivalent to prime (with the exception of $S^1 \times S^2$, which is prime but not irreducible). And $\Sigma_2(k)$ for a non-trivial knot $k$ is not $S^1 \times S^2$ (since $H_1(\Sigma_2(k)) = \mathbb{Z}/2$-torsion related... actually $H_1(\Sigma_2(k))$ is the 2-torsion part of the knot group abelianized, which for a knot is related to the determinant of the knot). For the unknot, $\Sigma_2 = S^3$, which is irreducible. For a non-trivial knot, $\Sigma_2(k) \neq S^1 \times S^2$ (since $H_1(S^1 \times S^2) = \mathbb{Z}$, but $H_1(\Sigma_2(k))$ is finite for any knot). So for knots, prime = irreducible for the double branched cover.

So the question reduces to: $k$ prime $\Rightarrow$ $\Sigma_2(k)$ irreducible?

I believe this is true and is a consequence of the equivariant sphere theorem. Let me try to find the cleanest proof.

Here's another approach using the knot complement:

$\Sigma_2(k) = \widetilde{E(k)} \cup V$ where $\widetilde{E(k)}$ is the double cover of the knot exterior $E(k) = S^3 \setminus \nu(k)$ and $V = \nu(\tilde{k})$ is a solid torus glued along the boundary.

If $\Sigma_2(k)$ is reducible, there's an essential sphere $S$. Isotope $S$ to minimize $|S \cap V|$. Then $S \cap \widetilde{E(k)}$ is a planar surface (sphere minus disks) properly embedded in $\widetilde{E(k)}$.

If $|S \cap V| = 0$: $S \subset \widetilde{E(k)}$, and $S$ is a closed essential surface in $\widetilde{E(k)}$. But $\widetilde{E(k)}$ is a double cover of $E(k)$, which is irreducible (for a non-split knot). Is the double cover of an irreducible 3-manifold irreducible? Not necessarily in general, but...

Hmm, actually the double cover of an irreducible 3-manifold can be reducible. For example, the double cover of a certain knot complement can be reducible. But for the specific case of knot complements in $S^3$, maybe it's OK.

Actually, I don't think the double cover of $E(k)$ is always irreducible even for prime $k$. The issue is more subtle.

Let me go back to the equivariant sphere theorem approach and try to make it work.

I think the key insight I was missing is: we should choose $S$ to minimize $|S \cap \tilde{k}|$ among all essential spheres (not just equivariant ones), and then show that the equivariant sphere theorem gives us an equivariant sphere with the same or fewer intersections.

Actually, here's a cleaner approach. Let me use the following version of the equivariant sphere theorem:

**Equivariant Sphere Theorem (Meeks-Yau)**: Let $M$ be an orientable 3-manifold with an involution $\tau$. If $M$ is reducible, then $M$ contains an essential sphere $S$ such that $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$, and $S$ can be chosen to minimize $|S \cap \text{Fix}(\tau)|$ among all essential spheres (not just equivariant ones).

Wait, I don't think the equivariant sphere theorem says that. It says there exists an equivariant essential sphere, but not necessarily one that minimizes intersections globally.

Let me try yet another approach. Maybe I should think about this in terms of the following lemma:

**Lemma**: If $S$ is an essential sphere in $\Sigma_2(k)$ that is $\tau$-invariant and $|S \cap \tilde{k}| = 2n$, then $k$ can be written as a connected sum of $n$ knots (some of which might be unknots).

If this lemma is true, then for $k$ prime, $n = 1$, and $|S \cap \tilde{k}| = 2$. But then $\pi(S)$ is a sphere intersecting $k$ in 2 points, and since $k$ is prime, one tangle is trivial, so the double branched cover of that side is a ball, making $S$ inessential. Contradiction.

Is the lemma true? If $S$ is $\tau$-invariant with $|S \cap \tilde{k}| = 2n$, then $\pi(S) = \Sigma$ intersects $k$ in $2n$ points. The sphere $\Sigma$ decomposes $(S^3, k)$ into two tangles $(B_1, T_1)$ and $(B_2, T_2)$, each with $n$ arcs. The knot $k$ is recovered by gluing these tangles.

Now, each tangle with $n$ arcs can be further decomposed. If $n \geq 2$, we can find a sphere in $B_1$ (or $B_2$) that intersects $T_1$ in 2 points and splits off one arc. This gives a decomposition of $k$ into a connected sum.

More precisely: In $B_1$, the $n$ arcs $T_1$ can be separated by a sphere $\Sigma_1 \subset B_1$ intersecting $T_1$ in 2 points, splitting $T_1$ into a 1-arc tangle and an $(n-1)$-arc tangle. (This is always possible: take a small sphere around one arc.) Then $\Sigma_1$ together with a disk on $\Sigma$ forms a sphere in $S^3$ intersecting $k$ in 2 points, giving a connected sum decomposition of $k$.

But this decomposition might be trivial (one summand is the unknot). For $k$ prime, all such decompositions are trivial. So each 1-arc tangle we split off is trivial.

Hmm, but this doesn't directly give us that $S$ is inessential. Let me think more.

OK here's another approach. Let me consider the case $\tau(S) = S$, $|S \cap \tilde{k}| = 2n$, and try to show directly that $S$ being essential implies $k$ is composite.

$S$ is essential in $M = \Sigma_2(k)$. $S$ separates $M$ into $X$ and $Y$, with $\tau(X) = X$ and $\tau(Y) = Y$ (since $\tau(S) = S$). The fixed set $\tilde{k}$ intersects $S$ in $2n$ points, so $\tilde{k} \cap X$ consists of $n$ arcs and $\tilde{k} \cap Y$ consists of $n$ arcs.

$X$ is the double branched cover of $B_1$ along $T_1$ (the $n$-arc tangle in $B_1$), and $Y$ is the double branched cover of $B_2$ along $T_2$.

$S$ is essential means neither $X$ nor $Y$ is a 3-ball. The double branched cover of a ball along an $n$-arc tangle is a ball if and only if the tangle is "trivial" (i.e., consists of $n$ pairwise unknotted, unlinked arcs). Actually, I'm not sure about the "only if" direction for $n \geq 2$.

For $n = 1$: double branched cover of a ball along 1 arc is a ball iff the arc is unknotted. (If the arc is knotted, the double branched cover is not a ball — it's the double branched cover of $S^3$ along the knot formed by closing the arc, minus a ball.)

For $n \geq 2$: it's more complicated. The double branched cover of a ball along a rational tangle (2 arcs) is a solid torus, not a ball. So for $n = 2$, the double branched cover is never a ball (it's a solid torus or something more complicated).

Wait, that's important. For $n = 2$: $X$ is the double branched cover of $B_1$ along a 2-arc tangle $T_1$. The boundary of $X$ is $S$ (a sphere). But the double branched cover of a ball along 2 arcs has boundary... let me think. The double branched cover of $B^3$ along 2 properly embedded arcs: the boundary of $B^3$ is $S^2$, and the double branched cover of $S^2$ along 4 points (the endpoints of the arcs) is a torus (by Riemann-Hurwitz: $\chi = 2 \cdot 2 - 4 = 0$, so genus 1). So $\partial X$ is a torus, not a sphere!

But $S$ is a sphere and $S = \partial X$. Contradiction! So $n = 2$ is impossible for $\tau(S) = S$.

Wait, let me recheck. $S$ is $\tau$-invariant, and $S$ is the boundary of $X$. The double branched cover of $B_1$ along $T_1$: the boundary of this cover is the double branched cover of $\partial B_1 = \Sigma$ along $\partial T_1 = \Sigma \cap k$ (which is $2n$ points). The double branched cover of $S^2$ along $2n$ points has Euler characteristic $\chi = 2 \cdot 2 - 2n = 4 - 2n$. For $n = 1$: $\chi = 2$, sphere. For $n = 2$: $\chi = 0$, torus. For $n \geq 3$: $\chi < 0$, higher genus.

But $S$ is a sphere ($\chi = 2$). So we need $4 - 2n = 2$, i.e., $n = 1$.

Wait, but $S$ is the boundary of $X$, and $\partial X$ is the double branched cover of $\Sigma$ along $2n$ points. If $n = 1$, $\partial X$ is a sphere, which matches $S$ being a sphere. If $n \geq 2$, $\partial X$ is not a sphere, which contradicts $S$ being a sphere.

So for $\tau(S) = S$ and $S$ a sphere, we must have $n = 1$, i.e., $|S \cap \tilde{k}| = 2$!

This is the key insight I was missing. The topology of the double branched cover constrains $n$ to be 1.

Let me double-check: $S$ is $\tau$-invariant, so $\tau|_S$ is an involution on $S = S^2$ with $2n$ fixed points. The quotient $S/\tau = \Sigma = S^2$. The double branched cover of $S^2$ along $2n$ points: by Riemann-Hurwitz, $\chi(S) = 2\chi(\Sigma) - 2n$, so $2 = 4 - 2n$, giving $n = 1$. ✓

So for $\tau(S) = S$, we must have $|S \cap \tilde{k}| = 2$.

Now, with $|S \cap \tilde{k}| = 2$: $\Sigma = \pi(S)$ intersects $k$ in 2 points. Since $k$ is prime, one of the two tangles $(B_1, T_1)$ or $(B_2, T_2)$ is trivial (a single unknotted arc). WLOG $(B_1, T_1)$ is trivial. The double branched cover of $B_1$ along a trivial arc is a ball (as we showed). So $X$ is a ball, and $S = \partial X$ bounds a ball, contradicting the essentiality of $S$.

Now for **Case 2: $\tau(S) \cap S = \emptyset$**.

$S$ and $\tau(S)$ are disjoint. Let $\Sigma = \pi(S) = \pi(\tau(S))$. The preimage $\pi^{-1}(\Sigma) = S \cup \tau(S)$.

$S$ separates $M$ into $X$ and $Y$, with $\tau(S) \subset X$ (WLOG) and $\tau(Y) \subset X$. Actually, $\tau(X)$ contains $S$ and $Y$... let me be more careful.

$S$ separates $M$ into $X$ and $Y$. $\tau(S)$ is disjoint from $S$, so $\tau(S) \subset X$ or $\tau(S) \subset Y$. WLOG $\tau(S) \subset X$. Then $\tau(X) \supset S$ (since $\tau(\tau(S)) = S \subset \tau(X)$) and $\tau(Y) \subset X$ (since $\tau(Y)$ is bounded by $\tau(S) \subset X$). Also $\tau(X) \supset Y$ (since $\tau(Y) \subset X$ means $Y \subset \tau(X)$). So $\tau(X) \supset Y \cup S$ and $\tau(Y) \subset X$.

The region between $S$ and $\tau(S)$ (inside $X$) is $R = X \setminus \tau(Y)$. We have $\tau(R) = R$ (since $\tau$ swaps $S$ and $\tau(S)$, and swaps the two sides of $R$).

$\pi(R) = B_1$ (one of the two balls bounded by $\Sigma$) and $\pi(Y \cup \tau(Y)) = B_2$ (the other ball). Actually, $\pi(Y) = \pi(\tau(Y)) = B_2$ (since $Y$ and $\tau(Y)$ are related by $\tau$ and both project to the same thing). And $\pi(R) = B_1$.

$R$ is the double branched cover of $B_1$ along $k \cap B_1$ (which is $m_1$ arcs). $Y$ is one component of the double branched cover of $B_2$ along $k \cap B_2$ (which is $m_2$ arcs), and $\tau(Y)$ is the other component.

The boundary of $R$ is $S \cup \tau(S)$ (two spheres). The boundary of $Y$ is $S$ (one sphere), and the boundary of $\tau(Y)$ is $\tau(S)$.

Now, $\partial R = S \cup \tau(S)$. $R$ is the double branched cover of $B_1$ along $m_1$ arcs. The boundary of this cover is the double branched cover of $\partial B_1 = \Sigma$ along $m_1 \cdot 2$ points (each arc has 2 endpoints on $\Sigma$). Wait, $k \cap B_1$ consists of $m_1$ arcs, and the endpoints of these arcs are $2m_1$ points on $\Sigma$. But $\Sigma \cap k$ has $m = 2m_1 + 2m_2$... no, $m = m_1 + m_2$ where $m_1$ is the number of arcs in $B_1$ and $m_2$ is the number of arcs in $B_2$. Each arc has 2 endpoints, so $|\Sigma \cap k| = 2m_1 = 2m_2$... no, that's not right either.

Let me recount. $k$ is a circle. $\Sigma$ intersects $k$ in $m$ points. These $m$ points divide $k$ into $m$ arcs. Each arc is in $B_1$ or $B_2$. Since $k$ alternates between $B_1$ and $B_2$ (each time it crosses $\Sigma$), the number of arcs in $B_1$ equals the number in $B_2$ (both are $m/2$). So $m$ must be even, $m = 2m'$, with $m'$ arcs in each ball.

So $m_1 = m_2 = m' = m/2$.

The boundary of $R$ (double branched cover of $B_1$ along $m'$ arcs) is the double branched cover of $\Sigma = S^2$ along $2m'$ points (the endpoints of the $m'$ arcs). By Riemann-Hurwitz: $\chi(\partial R) = 2 \cdot 2 - 2m' = 4 - 2m'$. But $\partial R = S \cup \tau(S)$, two spheres, so $\chi(\partial R) = 4$. Thus $4 - 2m' = 4$, giving $m' = 0$.

But $m' = 0$ means $k \cap B_1 = \emptyset$, which we already showed leads to $S$ being inessential. Contradiction!

Wait, that can't be right. Let me recheck.

$\partial R = S \cup \tau(S)$. Each of $S$ and $\tau(S)$ is a sphere, so $\chi(\partial R) = 2 + 2 = 4$. The double branched cover of $\Sigma$ along $2m'$ points has $\chi = 4 - 2m'$. Setting $4 - 2m' = 4$ gives $m' = 0$.

But if $m' = 0$, there are no arcs in $B_1$, so $k \subset B_2$. Then $R$ is the double unbranched cover of $B_1$, which is two balls. So $R = B_R \cup B_R'$ (two balls), with $\partial B_R = S$ and $\partial B_R' = \tau(S)$. So $S$ bounds a ball, contradicting essentiality.

So **Case 2 is impossible** (for an essential sphere)!

Wait, I need to be more careful. $\partial R$ is the preimage of $\partial B_1 = \Sigma$ under the branched cover $\pi|_R: R \to B_1$. The branching is along $k \cap B_1 = m'$ arcs. The preimage of $\Sigma$ under this branched cover is the double branched cover of $\Sigma$ along the $2m'$ endpoints of these arcs. But actually, the boundary of $R$ is $\pi^{-1}(\Sigma) \cap R$, which is $S \cup \tau(S)$.

Hmm, but is $\partial R$ exactly the double branched cover of $\Sigma$ along $2m'$ points? Let me think again.

$R$ is a component of $\pi^{-1}(B_1)$. $\pi^{-1}(\Sigma) = S \cup \tau(S)$. So $\partial R \subset S \cup \tau(S)$. Since $R$ is between $S$ and $\tau(S)$, $\partial R = S \cup \tau(S)$. Yes.

Now, $\pi|_{\partial R}: \partial R \to \Sigma$ is a 2-to-1 map. It's the restriction of the branched cover to the boundary. The branching points on $\Sigma$ are $\Sigma \cap k = 2m'$ points. At each branching point, the map is 1-to-1 (locally like $z \mapsto z^2$). So $\pi|_{\partial R}$ is a double branched cover of $\Sigma$ branched at $2m'$ points.

By Riemann-Hurwitz: $\chi(\partial R) = 2\chi(\Sigma) - (2m' - 0) = 4 - 2m'$. (The Riemann-Hurwitz formula for a degree-2 map branched at $r$ points: $\chi(\text{cover}) = 2\chi(\text{base}) - r$. Here $r = 2m'$.)

$\chi(\partial R) = \chi(S) + \chi(\tau(S)) = 2 + 2 = 4$.

So $4 = 4 - 2m'$, giving $m' = 0$.

This means Case 2 always leads to $m' = 0$, i.e., no arcs in $B_1$, which makes $S$ inessential. So **Case 2 is impossible for an essential sphere**.

So the only possible case is Case 1: $\tau(S) = S$, which forces $|S \cap \tilde{k}| = 2$ (by the Riemann-Hurwitz argument), which then forces $S$ to be inessential (by primality of $k$). Therefore, no essential sphere exists, and $\Sigma_2(k)$ is irreducible, hence prime.

Wait, I need to double-check the Riemann-Hurwitz argument for Case 1 as well.

**Case 1: $\tau(S) = S$.**

$S$ is $\tau$-invariant. $S$ separates $M$ into $X$ and $Y$ with $\tau(X) = X$, $\tau(Y) = Y$. $\pi|_X: X \to B_1$ is a double branched cover (branched along $k \cap B_1$), and $\pi|_Y: Y \to B_2$ is a double branched cover (branched along $k \cap B_2$).

$\partial X = S$. $\pi|_S: S \to \Sigma$ is a double branched cover of $\Sigma$ branched at $\Sigma \cap k = 2m'$ points (where $m' = m/2$ is the number of arcs in each ball). By Riemann-Hurwitz: $\chi(S) = 2\chi(\Sigma) - 2m' = 4 - 2m'$. Since $S$ is a sphere, $\chi(S) = 2$. So $2 = 4 - 2m'$, giving $m' = 1$.

So $m' = 1$, meaning each ball contains exactly 1 arc of $k$, and $|\Sigma \cap k| = 2$.

Since $k$ is prime, one of the two 1-arc tangles is trivial. WLOG $(B_1, T_1)$ is a trivial tangle (unknotted arc). The double branched cover of $B_1$ along a trivial arc is a ball (as shown: the double branched cover of $S^3$ along the unknot is $S^3$, and splitting along the equatorial sphere gives two balls, each being the double branched cover of a ball along a trivial arc).

So $X$ is a ball, $S = \partial X$ bounds a ball, and $S$ is inessential. Contradiction.

Therefore, $\Sigma_2(k)$ is irreducible, hence prime (since $\Sigma_2(k)$ is a closed orientable 3-manifold and not $S^1 \times S^2$).

Wait, I should also verify that $\Sigma_2(k) \neq S^1 \times S^2$ for a prime knot $k$. For the unknot, $\Sigma_2 = S^3$, which is irreducible. For a non-trivial prime knot, $H_1(\Sigma_2(k))$ is finite (it's the 2-torsion of the abelianized knot group, related to the determinant $|\Delta_k(-1)|$ of the knot). Since $H_1(S^1 \times S^2) = \mathbb{Z}$, which is infinite, $\Sigma_2(k) \neq S^1 \times S^2$ for any non-trivial knot. For the unknot, $\Sigma_2 = S^3 \neq S^1 \times S^2$. So in all cases, $\Sigma_2(k) \neq S^1 \times S^2$, and irreducibility implies primality.

Actually, for the unknot, $\Sigma_2(S^3, \text{unknot}) = S^3$, which is irreducible and prime. So the statement holds trivially for the unknot.

Great, so the proof is:

1. Suppose $k$ is prime and $\Sigma_2(k)$ is reducible.
2. By the equivariant sphere theorem, there exists an essential sphere $S$ with $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$.
3. If $\tau(S) \cap S = \emptyset$: Riemann-Hurwitz on $\partial R$ (the region between $S$ and $\tau(S)$) shows $k \cap B_1 = \emptyset$, making $S$ bound a ball. Contradiction.
4. If $\tau(S) = S$: Riemann-Hurwitz on $S$ shows $|S \cap \tilde{k}| = 2$, so $\pi(S)$ intersects $k$ in 2 points. Primality of $k$ makes one tangle trivial, so $S$ bounds a ball. Contradiction.
5. Therefore $\Sigma_2(k)$ is irreducible, hence prime.

Let me also handle the subcase of Case 1 where $S \cap \tilde{k} = \emptyset$ (i.e., $m' = 0$). In this case, $\pi(S)$ is a sphere in $S^3 \setminus k$, which bounds a ball $B$ with $k \cap B = \emptyset$ (since $k$ is a knot, not a link, and $S^3$ is irreducible). The preimage $\pi^{-1}(B)$ is two balls (unbranched double cover), so $S$ bounds a ball. Contradiction. (This is consistent with the Riemann-Hurwitz argument: $m' = 0$ gives $\chi(S) = 4$, but $S$ is a sphere with $\chi = 2$, contradiction. So actually $m' = 0$ is ruled out by Riemann-Hurwitz directly.)

Wait, hmm. If $S \cap \tilde{k} = \emptyset$, then $\tau|_S$ has no fixed points, so $S/\tau = \Sigma$ and $\pi|_S: S \to \Sigma$ is an unbranched double cover. An unbranched double cover of $S^2$ is two copies of $S^2$, so $S$ would be two spheres, not one. Contradiction. So $S \cap \tilde{k} = \emptyset$ is impossible for $\tau(S) = S$ (since $S$ is connected and $\tau|_S$ is a fixed-point-free involution on $S^2$, which would make $S^2 \to S^2/\tau$ a double cover, but $\pi_1(S^2) = 0$ so there's no nontrivial double cover). Actually, a fixed-point-free involution on $S^2$ would give $S^2 \to \mathbb{R}P^2$, but $S^2$ is simply connected and $\mathbb{R}P^2$ has $\pi_1 = \mathbb{Z}/2$, so the map $S^2 \to \mathbb{R}P^2$ is the universal cover, which is fine. But $\Sigma = S/\tau$ would be $\mathbb{R}P^2$, not $S^2$. But $\Sigma = \pi(S) \subset S^3$, and $\Sigma$ is a sphere (image of a sphere under a continuous map into $S^3$... well, $\pi|_S$ is a double cover of $\Sigma$, so $\Sigma$ is a surface. If $\tau|_S$ has no fixed points, $\Sigma = S/\tau$ is $\mathbb{R}P^2$. But $\pi(S) \subset S^3$ and $\pi(S)$ is a closed surface in $S^3$. $\mathbb{R}P^2$ cannot be embedded in $S^3$ (since $S^3$ is orientable and $\mathbb{R}P^2$ is non-orientable). Contradiction. So $S \cap \tilde{k} \neq \emptyset$ when $\tau(S) = S$.)

Good, so $S \cap \tilde{k} \neq \emptyset$ is automatic for $\tau(S) = S$, and the Riemann-Hurwitz argument gives $|S \cap \tilde{k}| = 2$.

Now let me also verify the claim that the double branched cover of a ball along a single unknotted arc is a ball.

Consider $S^3$ with the unknot $u$. $\Sigma_2(S^3, u) = S^3$. The unknot lies on a standard sphere $\Sigma_0$ in $S^3$ that intersects $u$ in 2 points. This sphere divides $S^3$ into two balls $B_1, B_2$, each containing one unknotted arc of $u$. The preimage $\pi^{-1}(\Sigma_0)$ is a sphere $\tilde{\Sigma}_0$ in $\Sigma_2(S^3, u) = S^3$ (by Riemann-Hurwitz: $\chi = 4 - 2 = 2$, sphere). This sphere divides $S^3$ into two balls, which are the double branched covers of $B_1$ and $B_2$ along their respective arcs. So the double branched cover of a ball along a single unknotted arc is a ball. ✓

And if the arc is knotted: Consider a knotted arc $\alpha$ in a ball $B$. Close it up to a knot $k_\alpha$ by adding an arc on $\partial B$. The double branched cover of $B$ along $\alpha$ is $\Sigma_2(S^3, k_\alpha)$ minus a ball (the double branched cover of the complementary ball along the closing arc, which is unknotted, is a ball). So the double branched cover of $B$ along $\alpha$ is $\Sigma_2(S^3, k_\alpha) \setminus B^3$. This is a ball iff $\Sigma_2(S^3, k_\alpha) = S^3$ iff $k_\alpha$ is the unknot (by the unknotting theorem for double branched covers... actually, is it true that $\Sigma_2(k) = S^3$ iff $k$ is the unknot? For 2-bridge knots, the double branched cover is a lens space, and $L(1,0) = S^3$ corresponds to the unknot. But in general, there might be non-trivial knots with $\Sigma_2 = S^3$... Hmm, actually I think it's an open question or has a positive answer. Let me not worry about this — for our proof, we only need the "if" direction: unknotted arc → double branched cover is a ball, which we've verified.)

Actually, we need: if the tangle is trivial (unknotted arc), then the double branched cover is a ball. We've verified this. We don't need the converse.

So the proof is complete. Let me also handle the edge case where $k$ is the unknot. For the unknot, $\Sigma_2(k) = S^3$, which is irreducible and prime. ✓

Let me now also think about whether we need $k$ to be non-trivial for the proof. The proof shows that if $k$ is prime (including the unknot), then $\Sigma_2(k)$ is irreducible. For the unknot, $\Sigma_2 = S^3$ is irreducible. For a non-trivial prime knot, the proof by contradiction works: assuming $\Sigma_2(k)$ is reducible, the equivariant sphere theorem gives an essential sphere, and we derive a contradiction.

Actually, wait. For the unknot, $\Sigma_2 = S^3$ is irreducible, so there's no essential sphere, and the proof by contradiction vacuously works (there's nothing to prove). For a non-trivial prime knot, the proof works as above.

I think the proof is solid. Let me write it up cleanly.

Actually, let me reconsider one thing. In Case 2, I need to verify that $R$ is indeed the double branched cover of $B_1$ along $k \cap B_1$, and that $\partial R = S \cup \tau(S)$ is the double branched cover of $\Sigma$ along $\Sigma \cap k \cap B_1$ (the endpoints of the arcs in $B_1$).

$\pi^{-1}(B_1)$: Since $\pi: M \to S^3$ is a double branched cover branched along $k$, $\pi^{-1}(B_1)$ is the double branched cover of $B_1$ along $k \cap B_1$. Now, $\pi^{-1}(B_1) = R$ or $\pi^{-1}(B_1) = Y \cup \tau(Y)$, depending on which ball we call $B_1$.

Since $\pi^{-1}(\Sigma) = S \cup \tau(S)$, and $\Sigma = \partial B_1 = \partial B_2$, we have $\pi^{-1}(B_1) \cap \pi^{-1}(B_2) = S \cup \tau(S)$. The region $R$ (between $S$ and $\tau(S)$) is one of $\pi^{-1}(B_1)$ or $\pi^{-1}(B_2)$, and $Y \cup \tau(Y)$ is the other.

If $R = \pi^{-1}(B_1)$: $\partial R = S \cup \tau(S)$ is the double branched cover of $\Sigma$ along $\Sigma \cap k \cap B_1$ (the endpoints of arcs in $B_1$). The number of branch points is $2m_1$ where $m_1$ is the number of arcs in $B_1$. By Riemann-Hurwitz: $\chi(\partial R) = 4 - 2m_1$. But $\chi(\partial R) = 4$ (two spheres). So $m_1 = 0$.

If $R = \pi^{-1}(B_2)$: similarly $m_2 = 0$.

Either way, one of the balls has no arcs of $k$, meaning $k$ is entirely in the other ball. Then the double branched cover of the empty ball is two balls (unbranched), so $R$ is two balls, and $S$ (and $\tau(S)$) bound balls. Contradiction.

Wait, but $R$ is connected (it's the region between two disjoint spheres). If $m_1 = 0$, the double branched cover of $B_1$ along no arcs is the double unbranched cover of a ball, which is two disjoint balls. But $R$ is connected (region between $S$ and $\tau(S)$). Contradiction. So actually, $R$ can't be the double branched cover of a ball along 0 arcs if $R$ is connected.

Hmm, let me reconsider. If $m_1 = 0$ (no arcs in $B_1$), then $\pi^{-1}(B_1)$ is the double unbranched cover of $B_1$. Since $B_1$ is a ball (simply connected), the double unbranched cover is two disjoint balls. So $\pi^{-1}(B_1)$ is two disjoint balls, each bounded by one of $S, \tau(S)$. So $S$ bounds a ball and $\tau(S)$ bounds a ball, both inessential. Contradiction.

But which is $\pi^{-1}(B_1)$: $R$ or $Y \cup \tau(Y)$? If $\pi^{-1}(B_1)$ is two disjoint balls, it must be $Y \cup \tau(Y)$ (since $Y$ and $\tau(Y)$ are disjoint, each bounded by $S$ and $\tau(S)$ respectively). Then $R = \pi^{-1}(B_2)$, which is the double branched cover of $B_2$ along $m_2$ arcs (all of $k$, since $k \subset B_2$). And $Y, \tau(Y)$ are the two balls of the unbranched double cover of $B_1$.

So $S = \partial Y$ bounds the ball $Y$, contradicting essentiality. ✓

OK so the proof works. Let me also make sure about the Riemann-Hurwitz formula. For a degree-$d$ branched cover $f: \tilde{F} \to F$ of surfaces, branched at points $p_1, \ldots, p_r$ with ramification indices $e_1, \ldots, e_r$:

$$\chi(\tilde{F}) = d \cdot \chi(F) - \sum_{i=1}^r (e_i - 1)$$

For a double cover ($d = 2$) branched at $r$ points (each with $e_i = 2$):

$$\chi(\tilde{F}) = 2\chi(F) - r$$

In our Case 1: $f = \pi|_S: S \to \Sigma$, $d = 2$, $F = \Sigma = S^2$, $\chi(F) = 2$, $r = |S \cap \tilde{k}|$ (number of fixed points of $\tau|_S$, which equals the number of branch points). So $\chi(S) = 4 - r$. Since $S = S^2$, $\chi(S) = 2$, so $r = 2$.

In Case 2: $f = \pi|_{\partial R}: \partial R \to \Sigma$, $d = 2$, $F = \Sigma = S^2$, $\chi(F) = 2$, $r = |\Sigma \cap k \cap B_i|$ (the number of branch points, which is the number of endpoints of arcs in $B_i$, where $R = \pi^{-1}(B_i)$). So $\chi(\partial R) = 4 - r$. Since $\partial R = S \cup \tau(S)$ (two spheres), $\chi(\partial R) = 4$, so $r = 0$.

Everything checks out. Let me write the final proof.

One more thing: I should make sure that the equivariant sphere theorem applies. The equivariant sphere theorem (Meeks-Yau, 1980) states: If $M$ is an orientable 3-manifold with a finite group action $G$ (here $G = \mathbb{Z}/2$ generated by $\tau$), and $M$ is reducible (contains an essential sphere), then there exists an essential sphere $S$ such that $g(S) = S$ or $g(S) \cap S = \emptyset$ for all $g \in G$.

For $G = \mathbb{Z}/2 = \{1, \tau\}$, this means $\tau(S) = S$ or $\tau(S) \cap S = \emptyset$. ✓

$M = \Sigma_2(k)$ is orientable (double branched cover of $S^3$ along a knot). ✓

The fixed set of $\tau$ is $\tilde{k}$, a knot in $M$. ✓

I think the proof is complete. Let me write it up.

Actually, let me also think about whether we need to worry about the case where $S$ intersects $\tilde{k}$ non-transversely. We can always isotope $S$ to be transverse to $\tilde{k}$, so this is not an issue.

Also, I should note that in Case 1, the fact that $\tau|_S$ has fixed points (so $S \cap \tilde{k} \neq \emptyset$) follows from the topological constraint: $\tau|_S$ is an involution on $S^2$ and $S/\tau = \Sigma \subset S^3$ is a 2-sphere (since $\pi(S)$ is a sphere in $S^3$). If $\tau|_S$ had no fixed points, $S/\tau$ would be $\mathbb{R}P^2$, which can't be embedded in $S^3$. So $\tau|_S$ must have fixed points, and by Riemann-Hurwitz, exactly 2.

Actually, I realize I need to be a bit more careful about why $\pi(S)$ is a sphere. $\pi|_S: S \to S^3$ is a continuous map from $S^2$ to $S^3$. The image $\pi(S)$ is a subset of $S^3$. Since $\pi$ is a branched cover and $S$ is $\tau$-invariant, $\pi|_S$ factors through $S/\tau$, and $\pi(S) = S/\tau$ (as a set). If $\tau|_S$ has fixed points, $S/\tau$ is a topological sphere (by the classification of involutions on $S^2$: an involution with fixed points is conjugate to a reflection, and the quotient is a disk; wait, that gives a disk, not a sphere).

Hmm, let me reconsider. An involution on $S^2$ with fixed points: by the classification, it's conjugate to a reflection across an equator. The quotient is a disk $D^2$, not $S^2$. But the fixed set is a circle (the equator), not isolated points.

But in our case, the fixed points of $\tau|_S$ are $S \cap \tilde{k}$, which is a finite set of points (since $S$ is transverse to $\tilde{k}$). An involution on $S^2$ with finitely many fixed points: by the Lefschetz fixed point theorem, $\chi(S^2) = 2 = \sum (-1)^i \text{tr}(\tau_*|_{H_i})$. For an involution, $\tau_*$ has eigenvalues $\pm 1$. On $H_0$: $\tau_* = 1$ (trace 1). On $H_2$: $\tau_* = \pm 1$. If $\tau_* = 1$ on $H_2$ (orientation-pres
