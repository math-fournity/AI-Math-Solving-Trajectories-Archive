# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Determine whether the vector bundle $Q(\operatorname{Gr}[p+2,2])$ is $U(p+2)$-equivariant.       — 题目文本
#   Okay, so I need to figure out whether the quotient bundle Q on the Grassmannian Gr(p+2,2) is U(p+2)-equivariant. Hmm, let me start by recalling some definitions and properties.

First, the Grassmannian Gr(n,k) is the space of all k-dimensional subspaces of an n-dimensional vector space. In this case, our Grassmannian is Gr(p+2,2), which means we're looking at 2-dimensional subspaces of a (p+2)-dimensional complex vector space. The unitary group U(p+2) acts transitively on Gr(p+2,2), right? Because unitary transformations can take any 2-dimensional subspace to any other.

Now, a vector bundle over a homogeneous space like Gr(p+2,2) is equivariant if the action of the group (here, U(p+2)) on the base space lifts to an action on the total space of the bundle, such that the projection map is equivariant. In other words, for each element g in U(p+2), applying g to a point in the Grassmannian and then taking the fiber over that point should be the same as taking the fiber first and then applying the corresponding linear transformation via g.

The quotient bundle Q on Gr(p+2,2) is defined as the quotient of the trivial bundle Gr(p+2,2) × ℂ^{p+2} by the tautological subbundle S, which consists of pairs (V, v) where V is a 2-plane in ℂ^{p+2} and v is a vector in V. So the fiber of Q over V is ℂ^{p+2}/V. 

Since the tautological bundle S is a subbundle of the trivial bundle, and the quotient bundle Q is the quotient of the trivial bundle by S, both S and Q should inherit equivariance from the trivial bundle if the action preserves the subbundle structure. Let me check that.

The group U(p+2) acts on the trivial bundle Gr(p+2,2) × ℂ^{p+2} by acting on the Grassmannian in the standard way and on ℂ^{p+2} by the defining representation. The tautological subbundle S is preserved under this action because if we have a pair (V, v) where v is in V, then applying a unitary transformation g sends V to gV and v to gv, which is in gV. Therefore, g maps the fiber S over V to the fiber S over gV. Hence, the action preserves the subbundle S, which implies that the quotient bundle Q is also preserved, meaning the action descends to the quotient.

Therefore, the quotient bundle Q should be U(p+2)-equivariant. Wait, is there more to check? Maybe I need to verify that the induced maps on the fibers are linear isomorphisms? Since the action is by linear transformations, when we quotient by the subbundle, the induced map on the quotient fibers should be linear as well, which they are. So yes, the projection is equivariant, and the bundle maps are linear.

Alternatively, another approach is to note that both the tautological bundle and the quotient bundle are homogeneous vector bundles over the Grassmannian. Since the Grassmannian is a homogeneous space for U(p+2), homogeneous vector bundles correspond to representations of the stabilizer subgroup. 

For Gr(p+2,2) = U(p+2)/(U(2) × U(p))). The stabilizer of a 2-plane V is U(2) × U(p), where U(2) acts on V and U(p) acts on the orthogonal complement. The tautological bundle S corresponds to the standard representation of U(2), and the quotient bundle Q corresponds to the representation of U(2) × U(p) on ℂ^{p+2}/V, which is the standard representation of U(p) on the orthogonal complement (since V has a U(2) action and its complement has a U(p) action). Therefore, Q is associated to the representation of the stabilizer U(2) × U(p) on ℂ^p. Since this representation is a homomorphism from U(2) × U(p) to GL(p, ℂ), the quotient bundle Q is a homogeneous vector bundle, hence U(p+2)-equivariant.

Wait, but here the quotient bundle is ℂ^{p+2}/V, which is a complex vector space of dimension p. The stabilizer acts on V via U(2) and on the orthogonal complement via U(p), so the quotient bundle's fiber is the orthogonal complement, which carries a natural U(p) action. But in the homogeneous bundle construction, the fiber over the base point (the chosen V) is the representation of the stabilizer. So if the stabilizer acts on ℂ^{p+2}/V via its U(p) factor, then yes, the quotient bundle is the homogeneous bundle induced by the U(p) representation. Hence, it's U(p+2)-equivariant.

So both from the perspective of the group action preserving the subbundle and quotienting, and from the homogeneous bundle construction, Q should be equivariant.

Is there any possible obstruction? Maybe if the action doesn't lift? But in this case, since the bundle is associated to a representation of the stabilizer, it should automatically have an equivariant structure. Equivariant bundles over homogeneous spaces G/H correspond to representations of H, and since Q is constructed from such a representation (the U(p) part), it must be equivariant.

Therefore, after considering both the direct check of the group action and the homogeneous bundle perspective, I think the answer is yes, Q(Gr(p+2,2)) is U(p+2)-equivariant.

**Final Answer**
\boxed{Yes}
</think>

To determine whether the vector bundle \( Q(\operatorname{Gr}(p+2,2)) \) is \( U(p+2) \)-equivariant, we start by noting that the Grassmannian \( \operatorname{Gr}(p+2,2) \) is a homogeneous space for the unitary group \( U(p+2) \). This group acts transitively on the Grassmannian, meaning any 2-dimensional subspace can be mapped to any other by a unitary transformation.

The quotient bundle \( Q \) is defined as the quotient of the trivial bundle \( \operatorname{Gr}(p+2,2) \times \mathbb{C}^{p+2} \) by the tautological subbundle \( S \). The fiber of \( Q \) over a subspace \( V \) is \( \mathbb{C}^{p+2}/V \). 

The key point is that the action of \( U(p+2) \) on the trivial bundle preserves the subbundle \( S \). This is because if \( (V, v) \) is in \( S \), then applying a unitary transformation \( g \) sends \( V \) to \( gV \) and \( v \) to \( gv \), which remains in \( gV \). Consequently, the action of \( U(p+2) \) descends to the quotient bundle \( Q \), making the projection map equivariant.

Additionally, considering the homogeneous vector bundle perspective, \( \operatorname{Gr}(p+2,2) \) can be written as \( U(p+2)/(U(2) \times U(p)) \). The stabilizer subgroup \( U(2) \times U(p) \) acts on the fiber \( \mathbb{C}^{p+2}/V \) (which is isomorphic to \( \mathbb{C}^p \)) through its \( U(p) \) factor. This representation induces the quotient bundle \( Q \), confirming it is a homogeneous vector bundle and thus \( U(p+2) \)-equivariant.

Therefore, the quotient bundle \( Q(\operatorname{Gr}(p+2,2)) \) is indeed \( U(p+2) \)-equivariant.

\[
\boxed{Yes}
\]  — 标准解答
#   Let me think about this problem carefully.

The problem: Given an infinite cardinal κ, determine if there exists a graph on κ vertices that contains 2^κ pairwise non-isomorphic induced subgraphs.

First, let me check for answer leaks. The problem statement is clean - no solutions, no hints, no formalization notes. Good.

Now let me think about the mathematics.

We have an infinite cardinal κ. We want a graph G on κ vertices such that G has 2^κ pairwise non-isomorphic induced subgraphs.

First, some basic counting:
- A graph on κ vertices has at most 2^κ subsets of vertices, so at most 2^κ induced subgraphs.
- The number of graphs on λ vertices (up to isomorphism) for infinite λ: this is 2^λ (since there are 2^(λ choose 2) = 2^λ labeled graphs, and each isomorphism class has size at most 2^λ... wait, let me be more careful).

Actually, the number of isomorphism classes of graphs on λ vertices:
- Number of labeled graphs on λ vertices = 2^(λ·(λ-1)/2) = 2^λ for infinite λ.
- Number of isomorphism classes: each isomorphism class has size at most λ^λ = 2^λ (number of permutations of λ). So the number of isomorphism classes is at least 2^λ / 2^λ which could be 1... that's not useful.

Actually, more carefully: the number of isomorphism classes of graphs on λ vertices is 2^λ for infinite λ. This is a classical result. The upper bound is 2^λ (since there are 2^λ labeled graphs). For the lower bound, we can construct 2^λ non-isomorphic graphs.

So the maximum possible number of non-isomorphic induced subgraphs of a graph on κ vertices is 2^κ (since there are at most 2^κ induced subgraphs total, and each isomorphism class is counted at least once).

The question is: can we achieve this maximum?

Let me think about this. We need a graph G on κ vertices such that the induced subgraphs realize all possible isomorphism types, or at least 2^κ distinct ones.

Actually, we need 2^κ pairwise non-isomorphic induced subgraphs. Since the total number of induced subgraphs is 2^κ, we essentially need "almost all" induced subgraphs to be pairwise non-isomorphic, or at least 2^κ of them to be pairwise non-isomorphic.

Let me think about what's known.

For κ = ℵ₀ (countable): We need a countable graph with 2^(ℵ₀) pairwise non-isomorphic induced subgraphs. Since there are 2^(ℵ₀) countable graphs up to isomorphism, and a countable graph has 2^(ℵ₀) induced subgraphs, we need a countable graph that "universally" realizes all countable graph types as induced subgraphs.

The Rado graph (random graph) is the universal countable graph - every countable graph appears as an induced subgraph. Since there are 2^(ℵ₀) non-isomorphic countable graphs, the Rado graph has 2^(ℵ₀) pairwise non-isomorphic induced subgraphs. So for κ = ℵ₀, the answer is yes.

Now for general infinite κ: We need a generalization.

The key question is whether there exists a "universal" graph on κ vertices that contains every graph on ≤ κ vertices as an induced subgraph. If such a graph exists, then since there are 2^κ non-isomorphic graphs on κ vertices, we'd be done.

But the existence of universal graphs on κ vertices is a subtle set-theoretic question. For κ = ℵ₀, the Rado graph works. For uncountable κ, the situation is more complex.

However, we don't need a universal graph in that strong sense. We just need 2^κ pairwise non-isomorphic induced subgraphs. We don't need to realize every possible graph type.

Let me think about this differently. 

Approach: Try to construct a graph on κ vertices with 2^κ pairwise non-isomorphic induced subgraphs directly.

Idea: Use a construction where different subsets of vertices give non-isomorphic induced subgraphs.

Let me think about a specific construction. Consider the following approach:

Take κ vertices, and partition them or structure them in a way that encodes information.

Actually, let me think about this more carefully. The question is asking us to "determine if there exists" such a graph. So the answer is either "yes for all infinite κ" or "it depends on κ" or "no for some κ".

Let me think about the Rado graph generalization. The Rado graph has the extension property: for any two disjoint finite sets A, B of vertices, there exists a vertex connected to all of A and none of B. 

For uncountable κ, we can consider a graph on κ vertices with the following extension property: for any two disjoint subsets A, B of size < κ, there exists a vertex connected to all of A and none of B. Such a graph would be universal for graphs on < κ vertices. But this requires κ to have certain properties (like κ^(<κ) = κ, which is related to κ being "accessible" or having κ^(<κ) = κ).

Hmm, but actually the question is simpler than universality. Let me reconsider.

We want 2^κ pairwise non-isomorphic induced subgraphs. Each induced subgraph is on some subset of the κ vertices. 

Key insight: If we can find a graph G on κ vertices such that for "many" subsets S of vertices, the induced subgraph G[S] has a unique isomorphism type, we're done.

Let me think about a direct construction.

Construction idea: Let the vertex set be κ. We want to design G so that different subsets give different isomorphism types.

One approach: Make each vertex "identifiable" in some sense, so that the induced subgraph on a subset S encodes S itself (up to some symmetry).

But for infinite graphs, vertices might not be distinguishable.

Let me think about the Rado graph approach more carefully for general κ.

Claim: For any infinite cardinal κ, there exists a graph on κ vertices with 2^κ pairwise non-isomorphic induced subgraphs.

Proof approach: 

Consider the "random graph" on κ vertices constructed via the Fraïssé limit approach or a direct probabilistic/existence argument.

Actually, let me think about whether we can always build a graph with the κ-extension property (for disjoint sets of size < κ). 

The number of pairs (A, B) of disjoint subsets of size < κ is κ^(<κ) · κ^(<κ) = κ^(<κ). For each such pair, we need to find a vertex with the right adjacency pattern. If we build the graph by transfinite induction, at stage α < κ, we have < κ vertices so far, and we need to extend. The number of requirements is κ^(<κ). If κ^(<κ) = κ, we can handle all requirements using κ vertices.

But κ^(<κ) = κ is not always true. For example, if κ = ℵ₁ and 2^(ℵ₀) > ℵ₁, then κ^(<κ) ≥ 2^(ℵ₀) > κ.

Hmm, so the universal graph approach might not work for all κ.

But we don't need universality! We just need 2^κ non-isomorphic induced subgraphs.

Let me think about this differently.

Alternative approach: Direct construction encoding subsets.

Let me try the following construction. Take the vertex set to be κ × {0, 1} or just κ, and build a graph that "encodes" information.

Actually, here's a cleaner idea. Let's think about what makes induced subgraphs non-isomorphic.

Construction: Let G be a graph on κ vertices. We want to find 2^κ subsets S ⊆ κ such that G[S] are pairwise non-isomorphic.

Idea: Build G so that it has a "rigid" structure, where each subset S produces a distinguishable graph.

Let me try a specific construction. 

Consider the following: Let the vertex set be κ. We'll build G by transfinite induction so that for each subset S of some large family, G[S] is distinguishable.

Actually, let me think about a simpler approach.

Approach via the Rado graph / random graph:

For any infinite cardinal κ, consider the following: Build a graph G on κ vertices with the property that for every two disjoint subsets A, B of V(G) with |A| + |B| < κ, there exists a vertex v ∉ A ∪ B adjacent to all of A and none of B.

Wait, this is the κ-saturated graph. As I noted, this requires κ^(<κ) = κ to build on κ vertices.

But actually, we can build a graph on κ vertices with a weaker extension property. Let me think...

Actually, let me reconsider. Maybe we don't need the full extension property. 

Here's another approach: 

For any infinite κ, we can build a graph G on κ vertices such that G contains an induced copy of every graph on ≤ κ vertices. This is stronger than what we need.

The existence of such a universal graph on κ vertices: This is known to exist when κ^(<κ) = κ. But in general, it's independent of ZFC for some κ.

Hmm, but the question asks to "determine if there exists" - suggesting there's a definite answer. Let me reconsider.

Wait, maybe the answer is simply "yes" for all infinite κ, and there's a construction that doesn't require κ^(<κ) = κ.

Let me think about a different construction.

Construction: Partition κ into κ many sets of size κ (possible since κ · κ = κ for infinite κ). Use the first part to build a "backbone" and the rest to encode information.

Actually, here's a key idea. Let me think about trees.

Consider the complete binary tree of height κ (or some variant). Actually, let me think about a different structure.

Let me think about the following construction:

Let G be a graph on κ vertices defined as follows. The vertex set is κ. We think of κ as 2^(<κ) or some subset thereof... hmm, this is getting complicated.

Let me try yet another approach.

Direct approach: We want to show that for any infinite κ, there's a graph on κ vertices with 2^κ pairwise non-isomorphic induced subgraphs.

Upper bound: Any graph on κ vertices has at most 2^κ induced subgraphs (one per subset), so at most 2^κ isomorphism classes.

Lower bound: We need to construct a graph achieving 2^κ.

Key observation: The number of isomorphism classes of graphs on κ vertices is exactly 2^κ. (Upper bound: 2^κ labeled graphs. Lower bound: there are 2^κ non-isomorphic graphs on κ vertices - this is a classical result.)

So we need a graph that "realizes" 2^κ of these isomorphism classes as induced subgraphs.

Now, here's a construction that might work:

Build G on κ vertices by transfinite induction. At each stage, we want to ensure that G contains induced copies of many different graph types.

But we need to be careful about the number of vertices available.

Actually, here's a cleaner idea. Let me use the following:

Lemma: For any infinite cardinal κ, there exists a graph G on κ vertices such that every graph on ≤ κ vertices is isomorphic to an induced subgraph of G.

If this lemma is true, then since there are 2^κ non-isomorphic graphs on κ vertices, G has 2^κ pairwise non-isomorphic induced subgraphs.

But as I noted, this lemma (existence of universal graph) requires κ^(<κ) = κ in general, which is not always true.

Hmm wait, actually the universal graph for graphs on κ vertices (not < κ vertices) might be different. Let me reconsider.

A universal graph for graphs on κ vertices: a graph on κ vertices containing every graph on κ vertices as an induced subgraph. This requires κ^(<κ) = κ? Or does it?

Actually, the Rado graph is universal for countable graphs and has ℵ₀ vertices. The generalization to uncountable κ: a universal graph on κ vertices for graphs on κ vertices.

The existence of such a graph is equivalent to... let me think. If G is on κ vertices and contains every graph on κ vertices as an induced subgraph, then in particular, for each graph H on κ vertices, there's an embedding of H into G. The number of graphs on κ vertices is 2^κ, and each embedding uses κ vertices. But G only has κ vertices, so we need to "pack" 2^κ different graphs into κ vertices.

This is possible because different induced subgraphs can share vertices - they just use different subsets.

The question is whether we can build such a G. The classical result is:

Theorem (Rado, generalization): A universal graph on κ vertices (for graphs on ≤ κ vertices) exists if and only if κ^(<κ) = κ.

Wait, I'm not sure about the "only if" direction. Let me think more carefully.

Actually, I recall that the existence of a universal graph on κ vertices is more subtle. Let me think about what's actually needed.

For the "if" direction: If κ^(<κ) = κ, we can build a graph with the κ-extension property (for disjoint A, B with |A|+|B| < κ, there's a vertex adjacent to all of A and none of B), and this graph is universal.

For the "only if" direction: If κ^(<κ) > κ, can we still have a universal graph? I think the answer is no, but I'm not 100% sure.

But actually, we don't need a universal graph! We just need 2^κ non-isomorphic induced subgraphs. Let me think about whether we can achieve this without full universality.

Alternative construction that doesn't need κ^(<κ) = κ:

Idea: Build a graph G on κ vertices that is "rigid" in a strong sense - so that different subsets give non-isomorphic induced subgraphs.

Construction: Let's build a graph where each vertex has a unique "signature" based on its neighborhood structure, so that the induced subgraph on any subset S is determined by S (up to automorphisms of G, but if G is rigid, then it's determined by S itself).

If G is rigid (trivial automorphism group) and has the property that the induced subgraph G[S] determines S (i.e., different subsets give non-isomorphic induced subgraphs), then we'd have 2^κ non-isomorphic induced subgraphs (one per subset, minus some collisions).

But can we build a rigid graph on κ vertices where different subsets give non-isomorphic induced subgraphs? That's a very strong requirement.

Hmm, let me think about this differently.

Actually, for the Rado graph (κ = ℵ₀ case), the Rado graph is NOT rigid - it has a huge automorphism group. Yet it still has 2^(ℵ₀) non-isomorphic induced subgraphs because it's universal. The universality is what matters, not rigidity.

So let me reconsider the universal graph approach.

Actually, I think the answer might be "yes for all infinite κ" and the construction might not require full universality.

Let me think about a weaker property. Instead of containing every graph on κ vertices, we just need 2^κ non-isomorphic ones.

Construction idea: 

Take κ = λ for some infinite cardinal. Partition the vertex set into κ many blocks, each of size κ (possible since κ × κ = κ). In block α, put a specific graph G_α. Choose the G_α to be pairwise non-isomorphic graphs on κ vertices. Then the induced subgraph on the union of any subcollection of blocks is determined (up to isomorphism) by which blocks are included, giving 2^κ non-isomorphic induced subgraphs.

Wait, but this requires 2^κ pairwise non-isomorphic graphs on κ vertices, and we need to fit them all into κ vertices. Each block has κ vertices, and we have κ blocks, so total vertices = κ · κ = κ. Good.

But we need 2^κ pairwise non-isomorphic graphs on κ vertices. We know there are 2^κ isomorphism classes of graphs on κ vertices, so we can pick 2^κ of them. But wait, we only have κ blocks, not 2^κ blocks!

Hmm, that's the problem. We have κ blocks, so we can only encode 2^κ subsets if... wait, 2^κ subsets of a set of size κ gives 2^κ subsets. So if we have κ blocks, the number of subsets of blocks is 2^κ. 

But we need the κ blocks to contain pairwise non-isomorphic graphs. We have κ blocks, so we need κ pairwise non-isomorphic graphs on κ vertices. That's easy - there are 2^κ ≥ κ such graphs.

Now, the induced subgraph on a subset S of blocks: this is the disjoint union of the graphs in the blocks indexed by S. For two different subsets S, S' of blocks, are the disjoint unions non-isomorphic?

If the graphs in different blocks are pairwise non-isomorphic, then the disjoint union of graphs from blocks in S is isomorphic to the disjoint union from blocks in S' if and only if S = S' (since the connected components / summands must match up, and each summand is a graph on κ vertices, which is uniquely identified by its isomorphism type).

Wait, but the disjoint union of graphs from blocks in S: each block contributes a connected component (if the graph in each block is connected). Then the isomorphism type of the disjoint union is determined by the multiset of isomorphism types of the components. If each block has a distinct isomorphism type, then the multiset is just the set S (since each type appears at most once). So different subsets S give different multisets, hence non-isomorphic disjoint unions.

But we need each block's graph to be connected (so that the blocks don't "merge" into larger components). We can ensure this by making each G_α a connected graph.

Also, we need the G_α to be pairwise non-isomorphic. Since there are 2^κ non-isomorphic connected graphs on κ vertices (is this true?), we can pick κ of them.

Is it true that there are 2^κ non-isomorphic connected graphs on κ vertices? For κ = ℵ₀, yes (there are 2^(ℵ₀) non-isomorphic countable connected graphs). For general κ: the number of labeled connected graphs on κ vertices is 2^κ (since almost all graphs on κ vertices are connected - the number of disconnected graphs is at most Σ_{λ<κ} (number of graphs on λ vertices) × (number of graphs on κ vertices) × (ways to choose the λ-subset) = ... hmm, this needs care for singular κ).

Actually, for regular κ, the number of disconnected graphs on κ vertices: a disconnected graph on κ vertices has a connected component of size < κ. The number of such graphs is at most Σ_{λ<κ} C(κ, λ) · 2^λ · 2^κ = Σ_{λ<κ} κ^λ · 2^κ. For regular κ, κ^λ ≤ κ^(<κ) for λ < κ. Hmm, this could be larger than 2^κ.

Let me think about this differently. Actually, I don't need connected graphs. Let me modify the construction.

Modified construction: Instead of using disjoint unions, use a different way to combine graphs that ensures distinguishability.

Alternative: Use a "tagged" construction. For each α < κ, create a block B_α of vertices, and add a special "marker" structure that identifies which block a vertex belongs to. Then the induced subgraph on a subset S of blocks is determined by S.

For example: Add a "hub" vertex h_α for each block B_α, connected to all vertices in B_α and to a central vertex. Different subsets of blocks give different induced subgraphs because the hub structure encodes which blocks are present.

Hmm, but this is getting complicated. Let me think more carefully.

Actually, let me go back to the disjoint union idea but handle the connectedness issue.

Claim: For any infinite cardinal κ, there exist κ pairwise non-isomorphic connected graphs on κ vertices.

Proof sketch: Consider graphs of the form: a path of length α (for α < κ) attached to a complete graph on κ vertices. Wait, that doesn't quite work because for infinite α, the "path of length α" might not change the isomorphism type.

Let me think of a better family. Consider the following graphs on κ vertices:
- For each subset A of κ (or each cardinal λ ≤ κ), define a graph G_λ that has a clique of size λ and the rest of the vertices form an independent set, with some specific connection pattern.

Actually, a simpler family: For each infinite cardinal λ ≤ κ, let G_λ be the complete graph K_λ together with κ \ λ isolated vertices. But the number of infinite cardinals ≤ κ is at most countable (for κ = ℵ_ω) or finite, so this doesn't give κ non-isomorphic graphs.

Better: For each α < κ, let G_α be a graph on κ vertices defined as follows. Take a set of α "special" vertices forming a path P_α, and the remaining κ vertices form a clique, with each special vertex connected to exactly one clique vertex. For different α, these are non-isomorphic (the path length distinguishes them). But for infinite α, we need to be careful - paths of different infinite lengths might be distinguishable.

Actually, for α < κ, the path P_α has α vertices. If α ≠ β, then P_α and P_β have different numbers of vertices, so G_α and G_β are non-isomorphic (since the "path part" has different cardinality). Wait, but both G_α and G_β have κ vertices total. The path part has α vs β vertices, and the clique part has κ vs κ vertices. If α ≠ β and both are < κ, then... hmm, the clique parts both have κ vertices (since κ - α = κ for α < κ). So the clique parts are isomorphic. The path parts have α vs β vertices. If α ≠ β, the paths are non-isomorphic (different cardinalities). But in G_α, the path is attached to the clique, so the isomorphism type of G_α depends on α.

Actually, I think this works but let me be more careful. In G_α, the structure is: a clique C of size κ, a path P of size α, and each vertex of P is connected to a unique vertex of C (say, the first vertex of P is connected to one vertex of C). The key distinguishing feature is the path P_α, which has α vertices. For α ≠ β (both < κ), the paths have different cardinalities, so G_α ≇ G_β.

But wait, for infinite α, β < κ with α ≠ β, do the paths P_α and P_β have different cardinalities? Yes, |P_α| = α and |P_β| = β, and if α ≠ β then |P_α| ≠ |P_β|... no wait, different ordinals can have the same cardinality. E.g., α = ω and β = ω + ω both have cardinality ℵ₀.

So I should use cardinals, not ordinals. For each cardinal λ < κ, define G_λ with a path of cardinality λ. The number of cardinals < κ is at most κ (and for κ = ℵ₀, it's just finite cardinals, which is countable = κ). Hmm, for κ = ℵ₀, the cardinals < κ are the finite cardinals and... wait, there are no infinite cardinals < ℵ₀. So we'd only get countably many (the finite ones), which is ℵ₀ = κ. Good.

For κ = ℵ₁, the cardinals < κ are the finite ones and ℵ₀, giving countably many, which is < κ = ℵ₁. That's not enough!

So this approach doesn't give κ non-isomorphic graphs for all κ.

Let me think of a better family.

Better family: For each α < κ (as an ordinal), define G_α to be a graph that encodes α in its structure. For instance, use a well-ordering structure.

Actually, here's a cleaner approach. For each subset S ⊆ κ, define a graph G_S on κ vertices. But we need κ pairwise non-isomorphic ones, and there are 2^κ subsets, so we can certainly find κ non-isomorphic ones (since there are 2^κ ≥ κ isomorphism classes).

Wait, I think I'm overcomplicating this. The key fact is:

Fact: For any infinite cardinal κ, there are 2^κ non-isomorphic graphs on κ vertices.

This is well-known. The upper bound is 2^κ (number of labeled graphs). For the lower bound, one can construct 2^κ non-isomorphic graphs explicitly.

Given this fact, there are certainly at least κ non-isomorphic graphs on κ vertices (since 2^κ ≥ κ for infinite κ). So we can pick κ pairwise non-isomorphic graphs G_α (α < κ) on κ vertices each.

Now, the construction: 
- Vertex set: κ × κ (which has cardinality κ).
- For each α < κ, the α-th block is {α} × κ, and the induced subgraph on this block is G_α.
- No edges between different blocks.

The resulting graph G has κ vertices and is the disjoint union of the G_α.

Now, for any subset S ⊆ κ, the induced subgraph G[S × κ] is the disjoint union of {G_α : α ∈ S}.

Question: For different subsets S, S' ⊆ κ, are the disjoint unions ⊔_{α∈S} G_α and ⊔_{α∈S'} G_α non-isomorphic?

If the G_α are pairwise non-isomorphic AND each G_α is connected, then yes: the connected components of the disjoint union are exactly the G_α for α ∈ S, and since they're pairwise non-isomorphic, the isomorphism type of the disjoint union determines S.

But we need each G_α to be connected. Can we find κ pairwise non-isomorphic connected graphs on κ vertices?

For this, we need: there are at least κ non-isomorphic connected graphs on κ vertices.

Claim: For any infinite cardinal κ, there are 2^κ non-isomorphic connected graphs on κ vertices.

Proof of claim: 
- Upper bound: 2^κ (total number of graphs on κ vertices).
- Lower bound: We construct 2^κ non-isomorphic connected graphs on κ vertices.

Construction for lower bound: Take any graph H on κ vertices. Form H' by adding a new vertex connected to all vertices of H... but that adds a vertex, making it κ+1 vertices. Instead, take H and pick one vertex v, connecting v to all other vertices. This makes H' connected (every vertex is at distance ≤ 2 from v). But different H might give isomorphic H'.

Better: Take H on κ vertices, and form H* by adding a "universal vertex" - but we need to stay on κ vertices. 

Alternative: Take H on κ vertices with a distinguished vertex v. Form H* = H ∪ {edges from v to all other vertices}. H* is connected. If H₁* ≅ H₂*, then... the universal vertex in H₁* (the one connected to all others) must map to the universal vertex in H₂*. But there might be multiple universal vertices. 

Hmm, let me think of a cleaner construction.

Cleaner construction: For each graph H on κ vertices (with vertex set κ), define H* as follows: the vertex set is κ × {0, 1}. For each n, (α, 0) is connected to (β, 0) iff α ~ β in H. Also, (α, 0) is connected to (α, 1) for all α. And (α, 1) is connected to (β, 1) for all α, β (i.e., the {1}-layer is a clique). No edges between (α, 1) and (β, 0) for α ≠ β.

Wait, this doubles the vertex count to 2κ = κ, which is fine. H* is connected because the {1}-layer is a clique and every (α, 0) is connected to (α, 1).

If H₁* ≅ H₂*, then the {1}-layer (clique of size κ) must map to the {1}-layer. So the {0}-layer maps to the {0}-layer, and the edges within the {0}-layer are preserved. So H₁ ≅ H₂.

This gives 2^κ non-isomorphic connected graphs on κ vertices (one for each isomorphism class of graphs on κ vertices).

Wait, I need to be more careful. The {1}-layer is a clique of size κ. In H*, is the {1}-layer the unique maximum clique? Not necessarily - H might have a large clique too. But the {1}-layer has the property that each vertex in it is connected to exactly one vertex in the {0}-layer (namely, (α,1) is connected to (α,0)). The {0}-layer vertices are connected to their H-neighbors in the {0}-layer and to exactly one {1}-layer vertex.

Hmm, the issue is that an isomorphism might not preserve the layers. Let me make the layers more distinguishable.

Modified construction: H* has vertex set κ × {0, 1, 2}. 
- Layer 0: (α, 0) ~ (β, 0) iff α ~ β in H.
- Layer 1: (α, 1) ~ (β, 1) for all α, β (clique). (α, 1) ~ (α, 0) for all α.
- Layer 2: (α, 2) ~ (β, 2) for all α, β (clique). (α, 2) ~ (α, 1) for all α. (α, 2) ~ (α, 0) for all α.
- No other edges.

So each (α, 2) is connected to (α, 0), (α, 1), and all (β, 2). Each (α, 1) is connected to (α, 0), (α, 2), and all (β, 1). Each (α, 0) is connected to (α, 1), (α, 2), and (β, 0) for β ~ α in H.

The degree of (α, 2) in H*: connected to all (β, 2) for β ≠ α (that's κ-1 = κ vertices), plus (α, 0) and (α, 1). So degree = κ + 2 = κ.
The degree of (α, 1) in H*: connected to all (β, 1) for β ≠ α (κ vertices), plus (α, 0) and (α, 2). Degree = κ.
The degree of (α, 0) in H*: connected to (α, 1), (α, 2), and deg_H(α) vertices in layer 0. Degree = 2 + deg_H(α).

So vertices in layer 0 have degree 2 + deg_H(α), while vertices in layers 1 and 2 have degree κ. For most H (where deg_H(α) < κ for all α), the layer 0 vertices have degree < κ + 2, while layers 1, 2 have degree κ. But if H has vertices of degree κ, this doesn't distinguish.

This is getting complicated. Let me use a different approach to ensure the layers are distinguishable.

Actually, let me use a much simpler approach. Instead of trying to make connected graphs, let me modify the main construction to not require connectedness.

Revised main construction:

Instead of using disjoint unions (which requires connected components to be distinguishable), use a different combining method.

Construction: Build a graph G on κ vertices as follows. Partition V(G) = κ into blocks B_α (α < κ), each of size κ. For each α, the induced subgraph G[B_α] is some graph H_α on κ vertices. Additionally, add a "marker" structure between blocks to make them distinguishable.

Specifically: Add a special vertex c (a "center") connected to all vertices. Wait, but then the center is in some block.

Let me try a different approach. Let me use the following:

Construction: 
- V(G) = κ × κ (cardinality κ).
- For each α < κ, block B_α = {α} × κ.
- G[B_α] = H_α (a specific graph on κ vertices, to be chosen).
- Between blocks: (α, β) is connected to (α', β') for α ≠ α' if and only if β = 0 and β' = 0 (i.e., the "first" vertex of each block forms a clique across blocks).

Hmm, this is getting messy. Let me think about this more carefully.

Actually, let me try a completely different approach.

Approach: Use the fact that for any infinite κ, there's a graph on κ vertices that is "sufficiently rich."

Let me think about the problem from the perspective of the answer. The question asks "determine if there exists" - I believe the answer is YES for all infinite κ, and the proof should work in ZFC.

Let me try the following clean construction:

Construction:
Let V = κ. We build G by specifying edges.

For each α < κ, let f_α: α → {0, 1} be a function (we'll choose these later). Define G such that for β < α < κ, there is an edge between β and α iff f_α(β) = 1.

So G is a graph where vertex α is connected to vertex β (for β < α) according to f_α(β). This is like a "triangle-free" construction where edges only go from lower to higher indices (well, the graph is undirected, but we're defining it via a tournament-like structure).

Now, for a subset S ⊆ κ, the induced subgraph G[S] is determined by the functions f_α restricted to S ∩ α for α ∈ S.

If we choose the f_α cleverly, different subsets S will give non-isomorphic induced subgraphs.

But how to choose f_α? And how to ensure 2^κ non-isomorphic induced subgraphs?

This is related to the Rado graph construction. The Rado graph can be defined exactly this way: vertex n is connected to vertex m (m < n) iff the m-th bit of n is 1. The Rado graph is universal for countable graphs.

For uncountable κ, we can try a similar construction, but the universality might fail.

Hmm, let me think about this problem from a higher level.

I think the answer is YES for all infinite κ, and here's why:

The key insight is that we don't need universality. We just need 2^κ non-isomorphic induced subgraphs, which is the maximum possible. 

Here's a construction that I think works:

Step 1: Note that there are 2^κ non-isomorphic graphs on κ vertices (classical fact).

Step 2: We want to "embed" 2^κ non-isomorphic graphs into a single graph on κ vertices as induced subgraphs.

Step 3: The construction: Partition κ into κ blocks of size κ. In each block, place a graph. Use a marker structure to distinguish blocks. Then subsets of blocks give 2^κ non-isomorphic induced subgraphs.

The challenge is Step 3 - making the marker structure work. Let me think about this more carefully.

Marker structure idea: 

For each α < κ, block B_α = {α} × κ. 

Define G as follows:
1. Within each block B_α, the induced subgraph is H_α (a connected graph on κ vertices, with the H_α pairwise non-isomorphic).
2. Between blocks: for α < α' < κ, connect (α, 0) to (α', 0). (So the "0-th" vertex of each block forms a path/clique across blocks.)

With this structure, the vertex (α, 0) in block B_α is the unique vertex in B_α that has neighbors outside B_α. So in any induced subgraph that includes entire blocks, the "connector" vertices are identifiable.

But we're taking induced subgraphs on arbitrary subsets, not just unions of blocks. So this doesn't directly work.

Let me reconsider. The issue is that we want to take induced subgraphs on arbitrary subsets of V(G), not just unions of blocks. But if we take the induced subgraph on a union of blocks (S × κ for some S ⊆ κ), then the connector vertices help identify the blocks.

So the plan is:
- For each S ⊆ κ, consider the induced subgraph G_S = G[S × κ].
- Show that different S give non-isomorphic G_S.
- This gives 2^κ non-isomorphic induced subgraphs.

For this to work, we need:
1. The H_α are pairwise non-isomorphic connected graphs on κ vertices.
2. The connector structure allows us to identify which blocks are present.

For (2): In G_S, the connector vertices are {(α, 0) : α ∈ S}. These are the vertices that have neighbors in other blocks. But actually, in G_S = G[S × κ], the connector vertex (α, 0) is connected to (α', 0) for α' ∈ S, α' ≠ α (if we made them a clique) or just to adjacent ones (if we made them a path). 

Hmm, but the non-connector vertices in block B_α (i.e., (α, β) for β > 0) have all their neighbors within B_α. So in G_S, the connected components are... well, if H_α is connected and the connector vertices link the blocks, then G_S might be connected. That's a problem because then we can't decompose it into blocks.

Let me modify: Don't connect the blocks at all. Make G the disjoint union of the H_α.

Then G_S = G[S × κ] = ⊔_{α ∈ S} H_α.

If the H_α are pairwise non-isomorphic and connected, then the connected components of G_S are exactly {H_α : α ∈ S}, and since they're pairwise non-isomorphic, G_S determines S (as a set of isomorphism types). So different S give non-isomorphic G_S.

This gives 2^κ non-isomorphic induced subgraphs (one for each S ⊆ κ).

The only thing we need is: κ pairwise non-isomorphic connected graphs on κ vertices.

As I discussed above, there are 2^κ non-isomorphic connected graphs on κ vertices (I gave a construction). So we can certainly pick κ of them.

Wait, but I need to verify the claim that there are 2^κ non-isomorphic connected graphs on κ vertices more carefully.

Claim: For any infinite cardinal κ, there are 2^κ non-isomorphic connected graphs on κ vertices.

Proof: 
- Upper bound: 2^κ (total graphs on κ vertices).
- Lower bound: Given any graph H on κ vertices, construct a connected graph H* on κ vertices such that H can be recovered from H* up to isomorphism. This gives an injection from isomorphism classes of graphs on κ vertices to isomorphism classes of connected graphs on κ vertices, proving the lower bound.

Construction of H*: 
Let H have vertex set V. H* has vertex set V × {0, 1} (cardinality 2κ = κ).
- Edges within V × {0}: (u, 0) ~ (v, 0) iff u ~ v in H.
- Edges within V × {1}: (u, 1) ~ (v, 1) for all u ≠ v (clique).
- Edges between layers: (u, 0) ~ (u, 1) for all u (matching).
- No other edges between layers.

H* is connected: every (u, 0) is connected to (u, 1), and all (u, 1) are connected to each other.

Recovery: Given H* up to isomorphism, can we recover H up to isomorphism?

In H*, the V × {1} layer is a clique of size κ. The V × {0} layer has the structure of H. Each vertex in V × {1} has degree κ (connected to all other V × {1} vertices plus one V × {0} vertex). Each vertex in V × {0} has degree deg_H(u) + 1.

If H has a vertex of degree κ, then (u, 0) has degree κ + 1 = κ, same as (u, 1). So we can't distinguish layers by degree alone.

But we can distinguish by structure: vertices in V × {1} form a clique, while vertices in V × {0} form H (which is generally not a clique). 

More precisely: In H*, consider the relation "u and v have κ common neighbors." Two vertices in V × {1} have κ common neighbors (all other V × {1} vertices). A vertex in V × {1} and a vertex in V × {0} have... let me compute. (u, 1) and (v, 0) with u ≠ v: common neighbors are (u, 0) [neighbor of (u,1) via matching, and of (v,0) iff u~v in H] and (w, 1) for w ≠ u [neighbor of (u,1) via clique, and of (v,0)? No, (v,0) is only connected to (v,1) in the {1} layer, not to (w,1) for w ≠ v]. So common neighbors of (u,1) and (v,0) (u ≠ v) are: {(u,0)} if u~v in H, plus possibly some others... 

Actually (v,0) is connected to (v,1) and to (w,0) for w~v in H. (u,1) is connected to (u,0) and (w,1) for all w ≠ u. Common neighbors: (u,0) is a neighbor of (u,1) [yes, via matching] and of (v,0) [yes, iff u~v in H]. (v,1) is a neighbor of (v,0) [yes, via matching] and of (u,1) [yes, iff u ≠ v, which is true]. So (v,1) is a common neighbor. Any (w,1) for w ≠ u, v: neighbor of (u,1) [yes] and of (v,0) [no, (v,0) is only connected to (v,1) in layer 1]. Any (w,0) for w ~ v in H, w ≠ u: neighbor of (v,0) [yes] and of (u,1) [no, (u,1) is only connected to (u,0) in layer 0]. 

So common neighbors of (u,1) and (v,0) (u ≠ v) are: (v,1) always, and (u,0) iff u~v in H. That's 1 or 2 common neighbors.

Two vertices in V × {0}: (u,0) and (v,0), u ≠ v. Common neighbors: (u,1) [neighbor of (u,0) via matching, of (v,0)? No, (v,0) is connected to (v,1) not (u,1)]. (v,1) [neighbor of (v,0) via matching, of (u,0)? No]. (w,0) for w ~ u and w ~ v in H. (w,1) for... (w,1) is a neighbor of (u,0)? No, (u,0) is only connected to (u,1) in layer 1. So common neighbors of (u,0) and (v,0) are: {(w,0) : w ~ u and w ~ v in H} ∪ {(u,1) if v ~ u in H} ∪ {(v,1) if u ~ v in H}. 

Hmm wait, (u,1) is a neighbor of (u,0) [matching] and of (v,0)? (v,0) is connected to (v,1) and (w,0) for w~v. (u,1) is not (v,1) (since u≠v) and not a (w,0). So (u,1) is NOT a neighbor of (v,0). Similarly (v,1) is not a neighbor of (u,0).

So common neighbors of (u,0) and (v,0) are {(w,0) : w ~ u and w ~ v in H}. This could be anywhere from 0 to κ.

Two vertices in V × {1}: (u,1) and (v,1), u ≠ v. Common neighbors: all (w,1) for w ≠ u, v [that's κ - 2 = κ vertices], plus (u,0) [neighbor of (u,1), and of (v,1)? (v,1) is connected to (v,0) and all (w,1). (u,0) is not (v,0) and not a (w,1). So no]. Similarly (v,0) is not a common neighbor. So common neighbors = {(w,1) : w ≠ u, v}, which has cardinality κ.

So:
- Two vertices in V×{1}: κ common neighbors.
- (u,1) and (v,0), u≠v: 1 or 2 common neighbors.
- Two vertices in V×{0}: variable, depends on H.

The key distinguishing feature: vertices in V×{1} have the property that they share κ common neighbors with other V×{1} vertices. Vertices in V×{0} don't have this property (unless H is very special).

More precisely, define a vertex v in H* to be "clique-type" if there exists another vertex w such that v and w have κ common neighbors. The V×{1} vertices are clique-type (pair with any other V×{1} vertex). A V×{0} vertex (u,0) is clique-type only if there exists w such that (u,0) and w have κ common neighbors. 

For (u,0) and (v,1) (v ≠ u): common neighbors are 1 or 2 (as computed). Not κ.
For (u,0) and (v,0) (v ≠ u): common neighbors are {(w,0) : w ~ u, w ~ v in H}. This is κ only if u and v have κ common neighbors in H.

So if H is a graph where no two vertices have κ common neighbors, then the clique-type vertices are exactly V×{1}, and we can identify the V×{1} layer. Then the V×{0} layer is the complement, and H is recovered as the induced subgraph on V×{0} minus the matching edges to V×{1}.

But what if H does have pairs with κ common neighbors? Then some V×{0} vertices might also be "clique-type," and we can't distinguish the layers.

To handle this, we can restrict to graphs H where no two vertices have κ common neighbors. Are there 2^κ such graphs? 

For κ = ℵ₀: a graph where no two vertices have infinitely many common neighbors. There are 2^(ℵ₀) such graphs (e.g., graphs with bounded degree, or more generally, graphs where each pair has finitely many common neighbors). Actually, we need to be more careful. The number of graphs on ℵ₀ vertices where every pair has finitely many common neighbors: this is a large class, certainly 2^(ℵ₀).

For general κ: graphs where every pair has < κ common neighbors. The number of such graphs is... well, "most" graphs have this property. Specifically, a random graph on κ vertices (in a suitable sense) will have this property. But let me think about whether there are 2^κ such graphs.

Actually, consider graphs of bounded degree (degree < κ for all vertices, or even finite degree). There are 2^κ such graphs on κ vertices (e.g., for each subset S of κ, define a graph where vertex α is connected to vertex α+1 iff α ∈ S, giving a graph of maximum degree 2 with 2^κ non-isomorphic types... hmm, actually this gives only κ non-isomorphic types since the graph is determined by S up to shift).

Let me think of a better family. For each function f: κ → {0, 1, 2}, define a graph H_f on κ × {0, 1} vertices... this is getting complicated.

Actually, let me just use a different construction for H* that doesn't have this issue.

Alternative construction of H*: 

H* has vertex set V × {0, 1, 2} (cardinality 3κ = κ).
- Layer 0: (u, 0) ~ (v, 0) iff u ~ v in H.
- Layer 1: (u, 1) ~ (v, 1) for all u, v (clique). (u, 1) ~ (u, 0) for all u.
- Layer 2: (u, 2) is connected to (u, 1) for all u, and to no other vertices.

So layer 2 vertices are "leaves" - each (u, 2) has degree 1, connected only to (u, 1). Layer 1 is a clique, each (u, 1) connected to (u, 0) and (u, 2) and all (v, 1). Layer 0 has the structure of H, each (u, 0) connected to (u, 1) and H-neighbors.

H* is connected (via layer 1 clique).

Recovery: The degree-1 vertices are exactly layer 2. Each degree-1 vertex (u, 2) is connected to (u, 1). So we can identify layer 1 as the neighbors of degree-1 vertices. Then layer 0 is the rest. H is the induced subgraph on layer 0.

Wait, but (u, 1) might also have other degree-1 neighbors? No, (u, 1) is connected to (u, 0), (u, 2), and all (v, 1) for v ≠ u. So (u, 2) is the only degree-1 neighbor of (u, 1). And (u, 2) has degree 1 (connected only to (u, 1)).

But could a vertex in layer 0 have degree 1? (u, 0) is connected to (u, 1) and to H-neighbors. If u is isolated in H, then (u, 0) has degree 1 (connected only to (u, 1)). So degree-1 vertices include all of layer 2 and possibly some of layer 0 (corresponding to isolated vertices in H).

Hmm, so we can't cleanly separate layer 2 from layer 0 using degree alone.

But we can use a different distinguishing feature. A degree-1 vertex in layer 2, (u, 2), is connected to (u, 1), which has degree κ (connected to all (v, 1) plus (u, 0) and (u, 2)). A degree-1 vertex in layer 0, (u, 0) (where u is isolated in H), is connected to (u, 1), which also has degree κ. So both types of degree-1 vertices are connected to degree-κ vertices. We can't distinguish them this way.

Let me add another layer to make the distinction clearer.

H* with vertex set V × {0, 1, 2, 3}:
- Layer 0: (u,0) ~ (v,0) iff u~v in H.
- Layer 1: (u,1) ~ (v,1) for all u,v (clique). (u,1) ~ (u,0) for all u.
- Layer 2: (u,2) ~ (u,1) for all u. No other edges for layer 2.
- Layer 3: (u,3) ~ (u,2) for all u. No other edges for layer 3.

So we have a chain: (u,3) - (u,2) - (u,1) - (u,0), with layer 1 being a clique.

Degree of (u,3): 1 (connected to (u,2) only).
Degree of (u,2): 2 (connected to (u,1) and (u,3)).
Degree of (u,1): κ (connected to all (v,1), plus (u,0) and (u,2)).
Degree of (u,0): deg_H(u) + 1 (connected to (u,1) and H-neighbors).

Now, the degree-1 vertices are: (u,3) for all u, and (u,0) for isolated u in H.
The degree-2 vertices are: (u,2) for all u, and (u,0) for u with deg_H(u) = 1.

A degree-1 vertex (u,3) is connected to (u,2) which has degree 2. A degree-1 vertex (u,0) (isolated in H) is connected to (u,1) which has degree κ. So we can distinguish: degree-1 vertices connected to degree-2 vertices are in layer 3, and degree-1 vertices connected to degree-κ vertices are in layer 0 (isolated in H).

Similarly, degree-2 vertices (u,2) are connected to (u,1) [degree κ] and (u,3) [degree 1]. A degree-2 vertex (u,0) with deg_H(u) = 1 is connected to (u,1) [degree κ] and one H-neighbor [variable degree]. So (u,2) has a degree-1 neighbor, while (u,0) with deg_H = 1 has a neighbor of degree deg_H(neighbor) + 1, which is not necessarily 1.

So we can identify layer 3 (degree-1 vertices whose neighbor has degree 2), then layer 2 (degree-2 vertices connected to a layer-3 vertex), then layer 1 (degree-κ vertices connected to a layer-2 vertex), then layer 0 (the rest).

From layer 0, we recover H.

This works! But it's getting complicated. Let me simplify.

Actually, the simplest approach: use a long enough "tail" to make the layers unambiguously identifiable.

Even simpler: Let me just use the following construction.

For each graph H on κ vertices, define H* on κ vertices as follows:

H* has vertex set V(H) × {0, 1}.
- (u, 0) ~ (v, 0) iff u ~ v in H.
- (u, 1) ~ (v, 1) for all u, v (clique).
- (u, 0) ~ (u, 1) for all u.
- No other cross-layer edges.

H* is connected. |V(H*)| = 2κ = κ.

Now, I claim that H₁* ≅ H₂* implies H₁ ≅ H₂, provided H₁ and H₂ are "nice" (e.g., have no clique of size κ).

If H has no clique of size κ, then in H*, the unique clique of size κ is the layer 1. So any isomorphism H₁* → H₂* must map layer 1 of H₁* to layer 1 of H₂*. Then it maps layer 0 to layer 0, and the induced subgraph on layer 0 is H, so H₁ ≅ H₂.

So for graphs H with no κ-clique, H ↦ H* is an injection on isomorphism classes.

Are there 2^κ non-isomorphic graphs on κ vertices with no clique of size κ? Yes! For example, triangle-free graphs. The number of non-isomorphic triangle-free graphs on κ vertices is 2^κ (this is a classical result - one can construct 2^κ non-isomorphic triangle-free graphs, e.g., using bipartite graphs or other constructions).

Actually, let me verify: the number of non-isomorphic triangle-free graphs on κ vertices is 2^κ.

Upper bound: 2^κ.
Lower bound: Consider bipartite graphs with parts A and B, each of size κ. A bipartite graph is triangle-free. The number of non-isomorphic bipartite graphs on κ + κ vertices... hmm, but we need graphs on κ vertices, not 2κ.

Let me think again. A bipartite graph on κ vertices with parts of size κ/2 = κ each (for infinite κ, κ = κ + κ). So a bipartite graph on κ vertices with parts A, B each of size κ. The number of such graphs is 2^(κ·κ) = 2^κ. The number of isomorphism classes: each isomorphism class has size at most κ^κ = 2^κ (permutations of κ vertices). So the number of isomorphism classes is at least 2^κ / 2^κ = 1, which is useless.

Hmm, let me think about this differently. 

Actually, for the lower bound on non-isomorphic triangle-free graphs: we can use the following. For each subset S of κ, define a graph G_S on κ vertices that is triangle-free and such that different S give non-isomorphic graphs. 

One construction: Let V = κ × {0, 1}. For each S ⊆ κ, define G_S as a bipartite graph with parts A = κ × {0} and B = κ × {1}, where (α, 0) ~ (β, 1) iff (α, β) ∈ some set determined by S. 

For instance, fix an injection φ: κ → κ × κ (possible since κ × κ = κ). For S ⊆ κ, define (α, 0) ~ (β, 1) iff φ(α) = (β, s) for some s ∈ S. Hmm, this is getting complicated.

Let me use a simpler approach. For each S ⊆ κ, define G_S on vertex set κ as follows: vertex α is connected to vertex β (α < β) iff α ∈ S and β = α + 1. Wait, this gives a graph that's a union of paths, and the isomorphism type depends on the pattern of S, but many different S give the same isomorphism type.

OK let me try yet another approach. I think the cleanest way is:

Fact: For any infinite cardinal κ, there are 2^κ non-isomorphic graphs on κ vertices.

This is a standard result. The proof: upper bound is 2^κ. For the lower bound, one can use the following construction. For each binary sequence s ∈ 2^κ, define a graph G_s on κ vertices. The graphs G_s are pairwise non-isomorphic. 

One such construction: For each s: κ → {0, 1}, define G_s on vertex set κ × {0, 1, 2} as follows:
- (α, 0) ~ (β, 0) for all α, β (clique of size κ).
- (α, 1) ~ (α, 0) for all α.
- (α, 2) ~ (α, 1) for all α.
- (α, 1) ~ (β, 2) iff s(α) = 1 and β = α. (Wait, this doesn't use s meaningfully.)

Hmm, let me think of a better construction.

Actually, here's a clean construction for 2^κ non-isomorphic graphs on κ vertices:

For each s ∈ 2^κ, define G_s on vertex set κ × {0, 1} (size 2κ = κ):
- Layer 0: κ × {0} is a clique.
- Layer 1: κ × {1} is an independent set.
- (α, 0) ~ (β, 1) iff s(α) = 1 and β = α. Wait, this connects (α, 0) to (α, 1) based on s(α). But then the degree of (α, 1) is 0 or 1, and the degree of (α, 0) is κ (from the clique) plus 0 or 1.

The isomorphism type of G_s: the vertices of degree κ+1 = κ in the clique are those (α, 0) with s(α) = 1, and those with s(α) = 0 have degree κ. But κ+1 = κ, so all clique vertices have degree κ. The independent set vertices have degree 0 or 1.

Hmm, the issue is that for infinite cardinals, κ + 1 = κ, so degree doesn't distinguish.

Let me use a different approach. For each s ∈ 2^κ, define G_s on vertex set κ:
- G_s is a graph where the degree sequence "encodes" s.

But for infinite graphs, the degree of each vertex is a cardinal ≤ κ, and there are only κ+1 possible degrees. So we can encode at most (κ+1)^κ = 2^κ different degree sequences, which is enough. But the issue is that many graphs share the same degree sequence.

OK, I think I'm overcomplicating this. Let me just use the well-known fact and move on.

Well-known fact: For any infinite cardinal κ, the number of non-isomorphic graphs on κ vertices is 2^κ.

This is proved in many combinatorics/set theory textbooks. The upper bound is clear. For the lower bound, one standard proof uses the fact that there are 2^κ non-isomorphic linear orders on κ (or similar structures), and these can be encoded into graphs.

Given this fact, there are 2^κ ≥ κ non-isomorphic graphs on κ vertices. We need κ pairwise non-isomorphic connected graphs on κ vertices.

For the connectedness, we can use the H* construction I described (with the 4-layer version that's unambiguously recoverable). Since there are 2^κ non-isomorphic graphs on κ vertices, and the H* construction is injective (for graphs without κ-cliques, or using the 4-layer version for all graphs), there are 2^κ non-isomorphic connected graphs on κ vertices. In particular, there are at least κ of them.

Wait, I need to be more careful with the H* construction. Let me use the 4-layer version which I argued is unambiguously recoverable.

H* construction (4-layer version):
- Vertex set: V(H) × {0, 1, 2, 3}, cardinality 4κ = κ.
- Layer 0: (u,0) ~ (v,0) iff u ~ v in H.
- Layer 1: (u,1) ~ (v,1) for all u,v (clique). (u,1) ~ (u,0) for all u.
- Layer 2: (u,2) ~ (u,1) for all u. No other edges for layer 2.
- Layer 3: (u,3) ~ (u,2) for all u. No other edges for layer 3.

H* is connected (via layer 1 clique).

Recovery from H*:
1. Layer 3 vertices have degree 1 and their unique neighbor has degree 2. (A layer 0 vertex with deg_H = 0 has degree 1, but its neighbor (u,1) has degree κ, not 2. A layer 0 vertex with deg_H = 1 has degree 2, but its neighbors are (u,1) [degree κ] and one H-neighbor [variable degree]. So layer 3 vertices are the degree-1 vertices whose neighbor has degree 2.)

Wait, I need to recheck. (u,3) has degree 1, connected to (u,2). (u,2) has degree 2, connected to (u,1) and (u,3). (u,1) has degree κ (connected to all (v,1) for v≠u [κ-1 vertices], plus (u,0) and (u,2), total = κ+1 = κ). (u,0) has degree deg_H(u) + 1.

A layer 0 vertex (u,0) with deg_H(u) = 0: degree 1, connected to (u,1) which has degree κ. So it's a degree-1 vertex whose neighbor has degree κ, not 2. Different from layer 3.

A layer 0 vertex (u,0) with deg_H(u) = 1: degree 2, connected to (u,1) [degree κ] and one H-neighbor (v,0) [degree deg_H(v)+1]. So it's a degree-2 vertex, but its neighbors have degrees κ and deg_H(v)+1. A layer 2 vertex (u,2) has degree 2, connected to (u,1) [degree κ] and (u,3) [degree 1]. So a layer 2 vertex has a degree-1 neighbor, while a layer 0 vertex with deg_H = 1 has no degree-1 neighbor (unless deg_H(v) = 0, in which case (v,0) has degree 1).

Hmm, so if (u,0) has deg_H(u) = 1 and its H-neighbor v has deg_H(v) = 0, then (u,0) has degree 2 with neighbors (u,1) [degree κ] and (v,0) [degree 1]. This looks like a layer 2 vertex! So we can't distinguish (u,0) from (u,2) in this case.

This is a problem. The 4-layer construction doesn't cleanly separate layers when H has specific degree patterns.

Let me use a longer tail. Use n layers for the tail, where the tail is a path of length n (for finite n). But for any finite n, there might be H-structures that mimic the tail.

Alternative: Use an infinite tail. For each u, attach a ray (one-way infinite path) to (u,1). But that uses κ · ℵ₀ = κ vertices for the tails, plus κ for layer 0 and κ for layer 1, total = κ. But then the tails are all isomorphic (rays), so they don't help distinguish.

Actually, the tails don't need to be distinguishable - they just need to be identifiable as tails. If each (u,1) has a ray attached, then the "tail" structure is: a ray starting from (u,1). The vertex (u,1) is the start of the ray and also part of the clique. So (u,1) is identifiable as a vertex that's in a κ-clique and has a ray attached.

But the issue is: could a layer 0 vertex also have a ray-like structure? If H has a ray starting from u, then (u,0) has a path-like structure in layer 0. But the ray in layer 0 is part of H, while the tail ray is a separate structure. The key difference is that the tail ray is a "pendant" structure (attached to the clique vertex), while the H-ray is part of the H-structure.

This is getting too complicated. Let me use a completely different approach.

Simplest approach: Don't require the graphs to be connected. Instead, use a different method to ensure that disjoint unions are distinguishable.

Revised construction:

Instead of using disjoint unions of connected graphs, use the following:

For each α < κ, let H_α be a graph on κ vertices with a distinguished "marker" - a specific substructure that identifies α.

For example, H_α has a clique of size |α| (the cardinality of α) as a marker. Since different α < κ can have different cardinalities, and the number of distinct cardinalities ≤ κ is at most κ, this gives at most κ different markers. But we need κ pairwise non-isomorphic H_α, and the markers help distinguish them.

Hmm, but different ordinals can have the same cardinality, so the clique size doesn't uniquely identify α.

Let me use a different marker. For each α < κ, let H_α contain a path of length α (as an ordinal). But for infinite α, a "path of length α" is a well-ordered path, which is a specific graph. Different ordinals α give non-isomorphic paths (since the order type is different). But wait, for undirected graphs, a path of length ω and a path of length ω+ω might be isomorphic as graphs (both are countably infinite paths, i.e., double rays or rays).

Actually, a path of length α (as a graph) is a connected graph where each vertex has degree ≤ 2 and the graph is a path. For finite α, this is a finite path. For α = ω, it's a ray. For α = ω + ω, it's... two rays joined at a point? No, a path of length ω + ω would be a ray of length ω + ω, which as a graph is still just a ray (since the graph structure doesn't encode the order type beyond the path structure). Actually, as an undirected graph, a one-way infinite path is a ray regardless of the ordinal length (as long as it's a limit ordinal). So this doesn't distinguish ordinals.

OK, I think the issue is that for infinite structures, graph isomorphism is coarser than order type.

Let me take a step back and think about what we really need.

We need: κ pairwise non-isomorphic graphs on κ vertices, such that their disjoint union is "decomposable" - i.e., from the isomorphism type of the disjoint union, we can recover which graphs are included.

For this, we need the graphs to be "indecomposable" with respect to disjoint union - i.e., each H_α is connected (so it's a connected component of the disjoint union). And we need them to be pairwise non-isomorphic.

So we're back to needing κ pairwise non-isomorphic connected graphs on κ vertices.

Let me try to prove this directly.

Claim: For any infinite cardinal κ, there are 2^κ non-isomorphic connected graphs on κ vertices.

Proof: 
We use the following construction. For each graph H on κ vertices, define H* as a connected graph on κ vertices, such that H ↦ H* is injective up to isomorphism.

Construction: H* has vertex set V(H) ⊔ (V(H) × ω) (disjoint union), where ω = {0, 1, 2, ...}. The cardinality is κ + κ · ℵ₀ = κ.

Edges:
1. H-edges: u ~ v in H* iff u ~ v in H (for u, v ∈ V(H)).
2. Tail: for each u ∈ V(H), (u, 0) ~ u, (u, n) ~ (u, n+1) for all n. So each u has a ray (u, 0) - (u, 1) - (u, 2) - ... attached to it.
3. No other edges.

H* is connected: every vertex is either in V(H) (connected to its ray) or in a ray (connected to the rest of the ray and eventually to V(H)). But wait, if H is disconnected, then H* might still be disconnected - two vertices in different components of H are not connected through H, but their rays are separate too. So H* is connected iff H is connected.

That's a problem. Let me add a universal vertex.

Modified construction: H* has vertex set V(H) ⊔ (V(H) × ω) ⊔ {*}, where * is a new vertex. Cardinality = κ + κ·ℵ₀ + 1 = κ.

Edges:
1. H-edges: u ~ v for u, v ∈ V(H) iff u ~ v in H.
2. * ~ u for all u ∈ V(H) (* is connected to all H-vertices).
3. Tail: (u, 0) ~ u, (u, n) ~ (u, n+1) for all n.
4. No other edges.

H* is connected: * connects all H-vertices, and each ray is attached to an H-vertex.

Recovery: The vertex * has degree κ (connected to all H-vertices). The H-vertices have degree deg_H(u) + 1 + 1 = deg_H(u) + 2 (H-neighbors, plus *, plus (u,0)). The ray vertices (u, n) have degree 2 for n ≥ 1, and (u, 0) has degree 2 (connected to u and (u, 1)).

Wait, (u, 0) is connected to u and (u, 1), so degree 2. (u, n) for n ≥ 1 is connected to (u, n-1) and (u, n+1), so degree 2. Except (u, 0) is connected to u [which is an H-vertex, degree deg_H(u)+2] and (u,1) [degree 2]. So (u,0) has degree 2 with one neighbor of degree 2 and one neighbor of degree deg_H(u)+2.

Hmm, the issue is identifying * and the H-vertices. * has degree κ. An H-vertex u with deg_H(u) = κ has degree κ + 2 = κ, same as *. So we can't distinguish * from high-degree H-vertices.

Let me add more structure to *. Instead of a single vertex, use a clique of size κ as the "hub."

Modified construction: H* has vertex set V(H) ⊔ K ⊔ (V(H) × ω), where K is a set of size κ (the hub clique). Cardinality = κ + κ + κ·ℵ₀ = κ.

Edges:
1. H-edges: u ~ v for u, v ∈ V(H) iff u ~ v in H.
2. Hub: K is a clique. Each k ∈ K is connected to all H-vertices? No, that would make the hub vertices have degree κ + κ = κ, same as before.

Hmm, let me think differently. Let me use a structure that's definitely not present in H.

Construction: H* has vertex set V(H) ⊔ (V(H) × ω) ⊔ {c} ⊔ {d_n : n ∈ ω}.

Edges:
1. H-edges: u ~ v for u, v ∈ V(H) iff u ~ v in H.
2. c ~ u for all u ∈ V(H) (c is a universal vertex for H).
3. Tail: (u, 0) ~ u, (u, n) ~ (u, n+1) for all n.
4. c ~ d_0, d_n ~ d_{n+1} for all n (a ray attached to c).
5. No other edges.

H* is connected (via c).

Now, c has degree κ + 1 = κ (connected to all H-vertices and d_0). An H-vertex u has degree deg_H(u) + 2 (H-neighbors, c, and (u,0)). The ray vertices have degree 2. d_n has degree 2 for n ≥ 1, d_0 has degree 2 (c and d_1).

The vertex c has a ray (d_0, d_1, ...) attached, and also has κ H-neighbors. An H-vertex u has a ray ((u,0), (u,1), ...) attached, and deg_H(u) + 1 other neighbors (H-neighbors and c).

To identify c: c is the unique vertex that has a ray attached AND is connected to all H-vertices. But "connected to all H-vertices" is not a local property.

Hmm, this is still tricky. Let me try a different approach entirely.

Instead of trying to construct connected graphs with a recovery property, let me directly construct the graph G on κ vertices with 2^κ non-isomorphic induced subgraphs, without going through the "disjoint union of connected graphs" approach.

Direct construction:

Let V(G) = κ × κ (cardinality κ). For each α < κ and β < κ, define the edge relation as follows:

(α, β) ~ (α', β') iff one of the following:
1. α = α' and β ~ β' in some fixed graph F_α on κ (the "intra-block" edges).
2. α ≠ α' and β = β' = 0 (the "inter-block" edges: the 0-th vertex of each block forms a clique).

Wait, I already considered this. The issue is that induced subgraphs on arbitrary subsets don't respect block boundaries.

But actually, I only need to find 2^κ subsets that give non-isomorphic induced subgraphs. I don't need ALL subsets to give non-isomorphic ones. So I can restrict to subsets that are unions of blocks: S = A × κ for A ⊆ κ.

For such a subset, G[A × κ] has:
- Intra-block edges: F_α[A × κ ∩ block α] = F_α for α ∈ A.
- Inter-block edges: (α, 0) ~ (α', 0) for α, α' ∈ A, α ≠ α'.

So G[A × κ] is the disjoint union of the F_α (α ∈ A), plus a clique on {(α, 0) : α ∈ A}.

If the F_α are connected, then the connected components of G[A × κ] are... well, the inter-block clique connects all the (α, 0) vertices, which are in different blocks. So if each F_α is connected, then G[A × κ] is connected (all blocks are connected through the (α, 0) clique). So we can't decompose it into blocks.

Hmm. Let me not add inter-block edges. Then G[A × κ] = ⊔_{α ∈ A} F_α, and if the F_α are connected and pairwise non-isomorphic, different A give non-isomorphic graphs.

So the construction is simply: G = disjoint union of κ pairwise non-isomorphic connected graphs on κ vertices each. Total vertices = κ · κ = κ.

And I need to show: there exist κ pairwise non-isomorphic connected graphs on κ vertices.

Let me try to prove this more carefully.

Approach: Show that there are 2^κ non-isomorphic connected graphs on κ vertices.

Sub-claim: There are 2^κ non-isomorphic graphs on κ vertices that are connected and have a "unique hub" - a vertex connected to all others.

A graph with a universal vertex is connected. If H is a graph on κ vertices with a universal vertex u, then H is determined (up to isomorphism) by the induced subgraph on V(H) \ {u}, which is an arbitrary graph on κ vertices (since κ - 1 = κ). 

But different graphs on κ vertices can give isomorphic graphs with universal vertices, because the universal vertex might not be unique.

If H has a unique universal vertex, then H is determined by H \ {u} (the induced subgraph on non-universal vertices). Two such graphs H₁, H₂ are isomorphic iff H₁ \ {u₁} ≅ H₂ \ {u₂}.

When is the universal vertex unique? If H \ {u} has no universal vertex, then u is the unique universal vertex of H. So if we start with a graph F on κ vertices with no universal vertex, and add a universal vertex u, we get a graph H with a unique universal vertex, and H is determined by F.

But adding a vertex gives κ + 1 = κ vertices, which is fine. But we need to be careful: H has κ vertices (F has κ - 1 vertices plus u). Since κ - 1 = κ for infinite κ, F has κ vertices and H has κ + 1 = κ vertices. Wait, no: if F has κ vertices, then H has κ + 1 vertices = κ vertices (for infinite κ). But we need H to have exactly κ vertices. Since κ + 1 = κ, this is fine in terms of cardinality, but we need to actually construct H on a set of size κ.

Let me be more precise. Let F be a graph on κ vertices with no universal vertex. Define H on κ vertices as follows: take V(F) (which has κ elements) and add one more vertex u. But |V(F)| + 1 = κ + 1 = κ, so we can biject V(F) ∪ {u} with κ. H has edges: all edges of F, plus u ~ v for all v ∈ V(F). H is connected (u connects to everything). u is the unique universal vertex (since F has no universal vertex). H is determined by F up to isomorphism.

So the number of non-isomorphic such H is equal to the number of non-isomorphic F on κ vertices with no universal vertex.

How many non-isomorphic graphs on κ vertices have no universal vertex? At least 2^κ / (something). Actually, the number of graphs on κ vertices with a universal vertex is at most κ · 2^κ = 2^κ (choose the universal vertex, then the rest is arbitrary). So the number without a universal vertex is 2^κ - 2^κ, which could be 0. That's not useful.

Let me think about this differently. The number of isomorphism classes of graphs on κ vertices with a universal vertex: each such graph is determined by the universal vertex (up to automorphism) and the graph on the remaining κ vertices. The number of isomorphism classes is at most (number of isomorphism classes of graphs on κ vertices) = 2^κ. So the number without a universal vertex is at least 2^κ - 2^κ, which is not helpful.

But actually, the number of isomorphism classes of graphs with a universal vertex is at most the number of isomorphism classes of graphs on κ vertices (since each such graph is determined by its non-universal part, which is a graph on κ vertices). So the number of isomorphism classes with a universal vertex is ≤ 2^κ. And the total is 2^κ. So the number without is ≥ 2^κ - 2^κ, which is ≥ 0. Not helpful.

But we can be more precise. The map F ↦ H (adding a universal vertex) is a function from isomorphism classes of graphs on κ vertices to isomorphism classes of graphs on κ vertices with a universal vertex. This map is surjective (every graph with a universal vertex comes from some F). Is it injective? Only if the universal vertex is unique. 

If F has no universal vertex, then H has a unique universal vertex, and the map is injective on such F. So the number of isomorphism classes of H with a unique universal vertex is equal to the number of isomorphism classes of F with no universal vertex.

Now, I claim there are 2^κ non-isomorphic graphs on κ vertices with no universal vertex. 

Proof: Consider graphs on κ vertices with maximum degree < κ (i.e., every vertex has degree < κ). Such graphs have no universal vertex (a universal vertex has degree κ). The number of non-isomorphic such graphs is 2^κ.

Why 2^κ? For κ = ℵ₀: graphs with bounded degree. There are 2^(ℵ₀) non-isomorphic such graphs (e.g., 2^(ℵ₀) non-isomorphic graphs of maximum degree 3, by a classical result).

For general κ: graphs with maximum degree < κ. For regular κ, the number of such graphs on κ vertices is... let me think. A graph with max degree < κ is determined by the neighborhoods, each of size < κ. The number of such graphs is at most κ^(κ·(<κ)) = ... hmm.

Actually, let me just use a specific family. For each S ⊆ κ, define a graph G_S on κ × {0, 1} (cardinality 2κ = κ) as follows:
- (α, 0) ~ (β, 0) for all α, β (clique on layer 0).
- (α, 1) ~ (α, 0) for all α (matching).
- (α, 1) ~ (β, 1) iff α = β and ... no, let me think.

Actually, here's a cleaner family. For each S ⊆ κ, define G_S on vertex set κ:
- α ~ β (α < β) iff β = α + 1 and α ∈ S.

This is a graph where edges form a subset of the path α - (α+1). The graph is a union of paths (some edges present, some absent). The isomorphism type depends on the pattern of S.

But for infinite κ, many different S give isomorphic graphs (e.g., shifting S by 1 gives an isomorphic graph if κ is a limit ordinal). So this doesn't give 2^κ non-isomorphic graphs.

Let me try a different family. For each S ⊆ κ, define G_S on vertex set κ × κ (cardinality κ):
- (α, β) ~ (α, γ) for all β, γ (each "row" α is a clique).
- (α, 0) ~ (α', 0) iff α, α' ∈ S (the "first column" restricted to S is a clique).

Hmm, this is getting complicated and I'm not sure it gives 2^κ non-isomorphic graphs.

Let me try yet another approach. I'll use the fact that there are 2^κ non-isomorphic linear orders on κ, and encode linear orders into graphs.

Fact: For any infinite cardinal κ, there are 2^κ non-isomorphic linear orders on κ.

This is well-known. For κ = ℵ₀, there are 2^(ℵ₀) non-isomorphic countable linear orders. For general κ, similarly.

Encoding: Given a linear order (L, <), define a graph G_L on L × {0, 1}:
- (x, 0) ~ (y, 0) for all x, y (clique).
- (x, 1) ~ (x, 0) for all x (matching).
- (x, 1) ~ (y, 1) iff x < y or y < x (i.e., all distinct pairs - this makes layer 1 a clique too). 

No, that doesn't encode the order. Let me think.

Encoding linear orders into graphs: Given (L, <), define G_L on L × {0, 1, 2}:
- (x, 0) ~ (y, 0) for all x, y (clique).
- (x, 1) ~ (x, 0) for all x.
- (x, 2) ~ (x, 1) for all x.
- (x, 1) ~ (y, 2) iff x < y (i.e., (x,1) is connected to (y,2) when x < y).
- No other edges.

Hmm, this might work but the recovery is complicated. Let me use a known encoding.

Actually, there's a standard way to encode any relational structure into a graph (using gadgets). But for infinite structures, this might use more vertices.

Let me try a more direct approach.

Standard result: The number of non-isomorphic graphs on κ vertices is 2^κ. (This is truly standard - see e.g., Truss or other set theory texts.)

Given this, there are 2^κ ≥ κ non-isomorphic graphs on κ vertices. Now, I need κ of them to be connected.

Claim: At least 2^κ of the 2^κ non-isomorphic graphs on κ vertices are connected.

Proof: The number of disconnected graphs on κ vertices is at most Σ_{λ < κ, λ infinite} (number of graphs on λ vertices) × (number of graphs on κ vertices) × C(κ, λ) + (number of graphs on finite vertices) × ...

Actually, a disconnected graph on κ vertices has a connected component of size < κ (for infinite κ, if all components have size κ, there can be at most one, making it connected). Wait, no: a disconnected graph on κ vertices could have two components each of size κ (if κ = κ + κ, which is true for infinite κ). So a disconnected graph on κ vertices could have all components of size κ, with at least 2 components.

Hmm, so the counting is more subtle. Let me think about it differently.

The number of isomorphism classes of disconnected graphs on κ vertices: a disconnected graph is a disjoint union of at least 2 connected graphs. The number of such disjoint unions is bounded by... the number of multisets of isomorphism classes of connected graphs on ≤ κ vertices, with total size κ. This is hard to bound directly.

Alternative approach: Instead of counting, directly construct 2^κ non-isomorphic connected graphs.

Construction: For each graph H on κ vertices, define C(H) as a connected graph on κ vertices, such that H₁ ≇ H₂ implies C(H₁) ≇ C(H₂).

I'll use the following construction:

C(H) has vertex set V(H) × {0, 1} ∪ {*}.
- |V(H) × {0,1}| + 1 = 2κ + 1 = κ. Good.
- Layer 0: (u, 0) ~ (v, 0) iff u ~ v in H.
- Layer 1: (u, 1) ~ (v, 1) iff u ~ v in H. (Copy of H)
- * ~ (u, 0) for all u. (* is universal for layer 0)
- * ~ (u, 1) for all u. (* is universal for layer 1)
- (u, 0) ~ (u, 1) for all u. (Matching)
- No other edges between layers.

C(H) is connected (* connects to everything).

Now, * has degree 2κ = κ. Each (u, 0) has degree deg_H(u) + κ + 1 = κ (H-neighbors, all (v,1) via *, and (u,1)). Wait, (u,0) is connected to H-neighbors in layer 0, to * (which connects to all), and to (u,1). So degree = deg_H(u) + 1 + 1 = deg_H(u) + 2. No wait, * is a single vertex, (u,0) is connected to * and (u,1) and H-neighbors. So degree = deg_H(u) + 2.

But (u, 0) is NOT connected to (v, 1) for v ≠ u (no cross-layer edges except matching). Let me re-read my construction. I said:
- * ~ (u, 0) for all u.
- * ~ (u, 1) for all u.
- (u, 0) ~ (u, 1) for all u.
- No other edges between layers (i.e., (u,0) ~ (v,1) only if u = v).

So (u, 0) is connected to: H-neighbors in layer 0, *, and (u, 1). Degree = deg_H(u) + 2.
(u, 1) is connected to: H-neighbors in layer 1, *, and (u, 0). Degree = deg_H(u) + 2.
* is connected to: all (u, 0) and all (u, 1). Degree = 2κ = κ.

So * is the unique vertex of degree κ (assuming all H-degrees are < κ). If H has a vertex of degree κ, then (u, 0) and (u, 1) also have degree κ + 2 = κ, same as *.

To avoid this issue, restrict to graphs H with maximum degree < κ. There are 2^κ non-isomorphic such graphs (I'll argue this below). For such H, * is the unique degree-κ vertex.

Given that * is identifiable, we can remove * and get the graph on V(H) × {0, 1}, which is two copies of H with a matching. From this, we can recover H (the two layers are identifiable because... hmm, actually they're symmetric - there's an automorphism swapping layer 0 and layer 1).

The symmetry between layers means we can recover H up to isomorphism (which is all we need). Specifically, the graph on V(H) × {0, 1} with the matching and two copies of H is determined by H up to isomorphism. And from this graph, we can recover H: the matching edges (u,0)-(u,1) partition the vertices into pairs, and each pair has the same H-neighborhood structure. The quotient (identifying matched pairs) gives H.

More formally: in C(H) \ {*} (removing *), the matching edges (u,0)-(u,1) are the edges between the two layers. The graph induced on each layer is H. The matching is a perfect matching between the layers. An isomorphism C(H₁) → C(H₂) must map * to * (unique degree-κ vertex), and then map the remaining graph to the remaining graph. The remaining graph has a unique perfect matching between two copies (well, the matching might not be unique, but the structure is determined by H).

Actually, the perfect matching might not be unique. If H has automorphisms, there could be other matchings. But the key point is that the isomorphism type of C(H) \ {*} determines the isomorphism type of H. 

Let me argue this more carefully. C(H) \ {*} is a graph on V(H) × {0, 1} with:
- Two copies of H (layers 0 and 1).
- Matching (u,0) - (u,1).

This graph is the "double" of H with a matching. I claim that H can be recovered up to isomorphism.

Consider the relation on vertices of C(H) \ {*}: u ≡ v iff u and v are matched (i.e., {u, v} is a matching edge). The matching edges can be identified as follows: (u, 0) and (u, 1) are twins in the graph C(H) \ {*} restricted to non-* vertices? No, they're not twins because they have different neighborhoods within their layers.

Hmm, let me think about this differently. In C(H) \ {*}, the vertex (u, 0) has neighbors: {(v, 0) : v ~ u in H} ∪ {(u, 1)}. The vertex (u, 1) has neighbors: {(v, 1) : v ~ u in H} ∪ {(u, 0)}. 

The matching edge (u,0)-(u,1) is special because (u,0) and (u,1) have "corresponding" neighborhoods. Specifically, (u,0) is connected to (u,1), and (u,1) is connected to (u,0), and the H-neighborhoods are in different layers.

Actually, I think the cleanest way to see that H is recoverable is: the matching edges are exactly the edges {x, y} such that x and y have no common neighbors in C(H) \ {*} (other than possibly through *). Wait, * is removed, so let me check.

In C(H) \ {*}, common neighbors of (u, 0) and (u, 1): 
- (v, 0) is a neighbor of (u, 0) iff v ~ u in H. Is (v, 0) a neighbor of (u, 1)? Only if v = u (matching), but (v, 0) ≠ (u, 0) since v ~ u means v ≠ u. So no.
- (v, 1) is a neighbor of (u, 1) iff v ~ u in H. Is (v, 1) a neighbor of (u, 0)? Only if v = u (matching), but v ≠ u. So no.
- (u, 0) is a neighbor of (u, 1) [matching] and vice versa, but we're looking for common neighbors, not the vertices themselves.

So (u, 0) and (u, 1) have NO common neighbors in C(H) \ {*} (when * is removed). 

What about two non-matched vertices? (u, 0) and (v, 0) with u ≠ v: common neighbors are {(w, 0) : w ~ u, w ~ v in H}. This could be non-empty.
(u, 0) and (v, 1) with u ≠ v: common neighbors: (w, 0) is a neighbor of (u,0) iff w~u, and of (v,1) iff w=v (matching). So (v,0) is a common neighbor iff v~u in H. (w,1) is a neighbor of (v,1) iff w~v, and of (u,0) iff w=u (matching). So (u,1) is a common neighbor iff u~v in H. So common neighbors of (u,0) and (v,1) (u≠v) are {(v,0), (u,1)} ∩ {w : w~u or w~v in H}... more precisely, (v,0) is a common neighbor iff v~u in H, and (u,1) is a common neighbor iff u~v in H. So if u~v in H, they have 2 common neighbors; if not, 0.

So in C(H) \ {*}, two matched vertices (u,0) and (u,1) have 0 common neighbors, and two non-matched vertices (u,0) and (v,1) (u≠v) have 0 common neighbors iff u ≁ v in H, and 2 common neighbors iff u ~ v in H.

Hmm, so "0 common neighbors" doesn't uniquely identify matching edges. A non-matched pair (u,0), (v,1) with u ≁ v in H also has 0 common neighbors.

So this approach doesn't cleanly identify the matching. Let me modify the construction.

OK, I think I'm overcomplicating this. Let me use a much simpler approach to get connected graphs.

Simplest construction of connected graphs from arbitrary graphs:

Given a graph H on κ vertices (with max degree < κ), define C(H) on κ vertices as follows:
- Vertex set: V(H) ∪ {*} (where * is a new vertex). |V(H)| + 1 = κ + 1 = κ.
- Edges: all edges of H, plus * ~ v for all v ∈ V(H).
- C(H) is connected (* is universal).
- * has degree κ (connected to all of V(H)).
- Each v ∈ V(H) has degree deg_H(v) + 1 < κ + 1 = κ (since deg_H(v) < κ).
- So * is the unique vertex of degree κ.
- Removing * gives H.
- So C(H₁) ≅ C(H₂) iff H₁ ≅ H₂.

This is much simpler! The key requirement is that H has max degree < κ, so that * is the unique degree-κ vertex.

Now, are there 2^κ non-isomorphic graphs on κ vertices with max degree < κ?

For κ = ℵ₀: graphs with finite max degree. There are 2^(ℵ₀) non-isomorphic such graphs (e.g., 2^(ℵ₀) non-isomorphic 3-regular graphs, or 2^(ℵ₀) non-isomorphic paths with varying attachments).

For general κ: graphs with max degree < κ. 

Upper bound on number of such graphs: each vertex has < κ neighbors, so the graph is determined by κ many choices of < κ-sized subsets. The number is at most (κ^(<κ))^κ = κ^(κ·(<κ)) = κ^(<κ·κ) = ... hmm, this depends on κ.

For regular κ: κ^(<κ) could be > κ. The number of graphs with max degree < κ is at most (number of ways to choose < κ neighbors for each of κ vertices) = (κ^(<κ))^κ. If κ^(<κ) = κ, this is κ^κ = 2^κ. If κ^(<κ) > κ, this could be larger than 2^κ, but the total number of graphs is 2^κ, so it's at most 2^κ.

For the lower bound: we need to construct 2^κ non-isomorphic graphs on κ vertices with max degree < κ.

Construction: For each S ⊆ κ, define G_S on κ × {0, 1} (cardinality 2κ = κ):
- (α, 0) ~ (β, 0) for β = α + 1 (path on layer 0).
- (α, 1) ~ (α, 0) for all α (matching).
- (α, 1) ~ (β, 1) for β = α + 1 iff α ∈ S (path on layer 1, with edges depending on S).

Max degree: (α, 0) has degree ≤ 3 (two path neighbors in layer 0, plus (α, 1)). (α, 1) has degree ≤ 3 (one matching edge, plus 0-2 path edges in layer 1). So max degree ≤ 3 < κ for infinite κ.

Now, are different S giving non-isomorphic G_S? The graph G_S is a "ladder" graph (two paths with rungs), where some rungs of the second path are missing based on S. The isomorphism type depends on the pattern of S.

But for infinite κ, the "path" on layer 0 is a path of length κ (which is a specific graph), and the pattern of S on layer 1 determines which edges are present. Two different S, S' might give isomorphic graphs if there's a "shift" automorphism.

To avoid this, we can "anchor" the path. For example, make the first vertex of layer 0 have a special structure (like a pendant vertex).

Modified construction: For each S ⊆ κ, define G_S on κ × {0, 1} ∪ {p}:
- (α, 0) ~ (β, 0) for β = α + 1 (path on layer 0).
- (α, 1) ~ (α, 0) for all α (matching).
- (α, 1) ~ (β, 1) for β = α + 1 iff α ∈ S.
- p ~ (0, 0) (pendant vertex attached to the start of the path).

Now the path is "anchored" at (0, 0) by the pendant p. An isomorphism must map p to p (the unique degree-1 vertex whose neighbor has degree 3... well, (0, 0) has degree 3: p, (1, 0), (0, 1)). Other degree-1 vertices: (α, 1) might have degree 1 if α ∉ S and α + 1 ∉ S (no path edges in layer 1) - then (α, 1) has degree 1 (just the matching edge to (α, 0)). And (α, 1)'s neighbor (α, 0) has degree 2 or 3.

Hmm, this is getting complicated and I'm not sure the anchoring works perfectly. But the general idea is sound: we can construct 2^κ non-isomorphic graphs of bounded degree on κ vertices.

Actually, let me use a cleaner construction. 

For each S ⊆ κ, define G_S on vertex set κ × {0, 1}:
- (α, 0) ~ (α+1, 0) for all α < κ (path on layer 0, indexed by ordinals < κ).
- (α, 0) ~ (α, 1) for all α (matching).
- No other edges.

Wait, this doesn't use S. Let me incorporate S.

For each S ⊆ κ, define G_S on vertex set κ × {0, 1, 2}:
- (α, 0) ~ (α+1, 0) for all α (path on layer 0).
- (α, 0) ~ (α, 1) for all α (matching between layers 0 and 1).
- (α, 1) ~ (α, 2) for all α (matching between layers 1 and 2).
- (α, 2) ~ (β, 2) for β = α + 1 iff α ∈ S (path on layer 2, edges determined by S).

Max degree: (α, 0) has degree ≤ 3. (α, 1) has degree 2. (α, 2) has degree ≤ 3.

The graph has a "spine" (layer 0 path with layer 1 vertices as "rungs"), and layer 2 has a path whose edges are determined by S.

The isomorphism type: the spine is a path of length κ (on layer 0), which is a specific graph. Layer 1 vertices are degree-2 vertices attached to the spine. Layer 2 vertices are attached to layer 1 and have path edges determined by S.

An isomorphism G_S → G_S' must preserve the spine (the unique path of length κ with specific degree-3 vertices at each position... actually, all layer 0 vertices have degree 2 or 3, depending on whether they're at the "end" of the path or not).

Hmm, for a path of length κ (κ infinite), there's no "end" - it's a one-way infinite path (ray) or a two-way infinite path (double ray) or a longer path. For κ = ω, it's a ray. For κ = ω₁, it's a path of length ω₁, which as a graph is... a well-ordered path, which is a specific graph.

Actually, for a path indexed by ordinals < κ, the graph structure is: vertex α is connected to vertex α+1. For κ = ω, this is a ray. For κ = ω + ω, this is two consecutive rays, which as a graph is still a ray (since the graph doesn't distinguish the "break" at ω). Wait, no: vertex ω is connected to vertex ω+1, and vertex ω-1 doesn't exist (ω is a limit ordinal). So the path has vertex ω connected only to ω+1 (and to (ω, 1) via matching). So vertex (ω, 0) has degree 2 (connected to (ω+1, 0) and (ω, 1)), while vertex (n, 0) for finite n > 0 has degree 3 (connected to (n-1, 0), (n+1, 0), and (n, 1)). And vertex (0, 0) has degree 2 (connected to (1, 0) and (0, 1)).

So the path on layer 0 has "breakpoints" at limit ordinals, where the degree drops from 3 to 2. These breakpoints are graph-theoretically identifiable. So the spine is not just a path - it has a specific structure determined by the ordinal structure of κ.

For two different ordinals κ, the spine would be different. But we're fixing κ, so the spine is the same for all S. The question is whether different S give non-isomorphic G_S.

An isomorphism G_S → G_S' must map the spine to itself (since the spine is the unique maximal path with the specific degree pattern). Actually, the spine might have automorphisms. For κ = ω (ray), the ray has no non-trivial automorphisms (it's rigid). For κ = ω + ω, the path has a "break" at ω, and the automorphism group is trivial. In general, a well-ordered path is rigid (no non-trivial automorphisms) because the ordinal structure is encoded in the degree pattern.

Wait, is a well-ordered path rigid? Consider the path on ω: 0 - 1 - 2 - .... This is a ray, and it's rigid (the endpoint 0 is the unique degree-1 vertex, and the rest follows). For the path on ω + ω: 0 - 1 - ... - ω - (ω+1) - .... Vertex 0 has degree 1, vertex ω has degree 1 (connected only to ω+1, since ω-1 doesn't exist). So there are two degree-1 vertices: 0 and ω. An automorphism could swap the two rays... but the first ray (0, 1, 2, ...) starts at 0, and the second ray (ω, ω+1, ...) starts at ω. Both are rays. An automorphism mapping 0 to ω would map the first ray to the second, which is fine. So the path on ω + ω is NOT rigid.

Hmm, so the spine might have automorphisms. This complicates things.

OK, I think I need to step back and use a cleaner, more abstract approach.

Let me use the following well-known result:

Theorem: For any infinite cardinal κ, there exist 2^κ non-isomorphic graphs on κ vertices.

This is standard. The proof typically goes: 
- Upper bound: 2^κ labeled graphs.
- Lower bound: Construct 2^κ non-isomorphic graphs. One way: for each subset S of κ, construct a graph G_S such that S can be recovered from G_S up to isomorphism. This can be done using a "rigid" base graph and encoding S into it.

Given this theorem, there are 2^κ non-isomorphic graphs on κ vertices. Now:

Theorem: For any infinite cardinal κ, there exist 2^κ non-isomorphic connected graphs on κ vertices.

Proof: Using the C(H) construction (add a universal vertex to a max-degree-<κ graph H), we get an injection from isomorphism classes of max-degree-<κ graphs to isomorphism classes of connected graphs. We need 2^κ non-isomorphic max-degree-<κ graphs on κ vertices.

For the existence of 2^κ non-isomorphic max-degree-<κ graphs on κ vertices: 

Consider the following. For each S ⊆ κ, define a graph G_S on κ vertices as a graph of max degree ≤ 2 (a union of paths and cycles) that encodes S. 

Actually, here's a clean construction. For each binary sequence s: κ → {0, 1}, define G_s on vertex set κ × {0, 1}:

- (α, 0) ~ (α, 1) for all α (perfect matching).
- (α, 0) ~ (α+1, 0) for all α with s(α) = 1 (path edges on layer 0, determined by s).
- No other edges.

Max degree: (α, 0) has degree 1 + s(α) + s(α-1) ≤ 3 (matching, plus path edges). (α, 1) has degree 1. So max degree ≤ 3 < κ.

Now, G_s is a graph where layer 1 is an independent set (all degree 1, connected to layer 0 via matching), and layer 0 is a subgraph of the path on κ (with edges determined by s).

The isomorphism type of G_s: the degree-1 vertices connected to degree-≥2 vertices are the layer 1 vertices. Wait, all layer 1 vertices have degree 1. Their neighbors (layer 0 vertices) have degree 1 + (number of path edges incident), which is 1, 2, or 3.

A layer 0 vertex (α, 0) with no path edges (s(α-1) = 0 and s(α) = 0, where we define s(-1) = 0 for α = 0... hmm, this is getting into ordinal arithmetic) has degree 1 (just the matching). A layer 0 vertex with one path edge has degree 2. With two path edges, degree 3.

So the degree-1 vertices in G_s include all of layer 1 and some of layer 0 (those with no path edges). This makes it hard to distinguish layers.

Let me modify: make layer 1 vertices have degree 2 instead of 1.

For each s: κ → {0, 1}, define G_s on κ × {0, 1, 2}:
- (α, 0) ~ (α+1, 0) for all α (full path on layer 0).
- (α, 0) ~ (α, 1) for all α (matching).
- (α, 1) ~ (α, 2) for all α (matching).
- (α, 2) ~ (α+1, 2) iff s(α) = 1 (path on layer 2, determined by s).

Max degree: (α, 0) has degree 2 + 1 = 3 (two path        — AI历史解题过程（thinking）
#   deepmath_103k_00005360         — 题目ID

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
  <problem_id>deepmath_103k_00005360</problem_id>
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

Determine whether the vector bundle $Q(\operatorname{Gr}[p+2,2])$ is $U(p+2)$-equivariant.

## Standard Solution

Okay, so I need to figure out whether the quotient bundle Q on the Grassmannian Gr(p+2,2) is U(p+2)-equivariant. Hmm, let me start by recalling some definitions and properties.

First, the Grassmannian Gr(n,k) is the space of all k-dimensional subspaces of an n-dimensional vector space. In this case, our Grassmannian is Gr(p+2,2), which means we're looking at 2-dimensional subspaces of a (p+2)-dimensional complex vector space. The unitary group U(p+2) acts transitively on Gr(p+2,2), right? Because unitary transformations can take any 2-dimensional subspace to any other.

Now, a vector bundle over a homogeneous space like Gr(p+2,2) is equivariant if the action of the group (here, U(p+2)) on the base space lifts to an action on the total space of the bundle, such that the projection map is equivariant. In other words, for each element g in U(p+2), applying g to a point in the Grassmannian and then taking the fiber over that point should be the same as taking the fiber first and then applying the corresponding linear transformation via g.

The quotient bundle Q on Gr(p+2,2) is defined as the quotient of the trivial bundle Gr(p+2,2) × ℂ^{p+2} by the tautological subbundle S, which consists of pairs (V, v) where V is a 2-plane in ℂ^{p+2} and v is a vector in V. So the fiber of Q over V is ℂ^{p+2}/V. 

Since the tautological bundle S is a subbundle of the trivial bundle, and the quotient bundle Q is the quotient of the trivial bundle by S, both S and Q should inherit equivariance from the trivial bundle if the action preserves the subbundle structure. Let me check that.

The group U(p+2) acts on the trivial bundle Gr(p+2,2) × ℂ^{p+2} by acting on the Grassmannian in the standard way and on ℂ^{p+2} by the defining representation. The tautological subbundle S is preserved under this action because if we have a pair (V, v) where v is in V, then applying a unitary transformation g sends V to gV and v to gv, which is in gV. Therefore, g maps the fiber S over V to the fiber S over gV. Hence, the action preserves the subbundle S, which implies that the quotient bundle Q is also preserved, meaning the action descends to the quotient.

Therefore, the quotient bundle Q should be U(p+2)-equivariant. Wait, is there more to check? Maybe I need to verify that the induced maps on the fibers are linear isomorphisms? Since the action is by linear transformations, when we quotient by the subbundle, the induced map on the quotient fibers should be linear as well, which they are. So yes, the projection is equivariant, and the bundle maps are linear.

Alternatively, another approach is to note that both the tautological bundle and the quotient bundle are homogeneous vector bundles over the Grassmannian. Since the Grassmannian is a homogeneous space for U(p+2), homogeneous vector bundles correspond to representations of the stabilizer subgroup. 

For Gr(p+2,2) = U(p+2)/(U(2) × U(p))). The stabilizer of a 2-plane V is U(2) × U(p), where U(2) acts on V and U(p) acts on the orthogonal complement. The tautological bundle S corresponds to the standard representation of U(2), and the quotient bundle Q corresponds to the representation of U(2) × U(p) on ℂ^{p+2}/V, which is the standard representation of U(p) on the orthogonal complement (since V has a U(2) action and its complement has a U(p) action). Therefore, Q is associated to the representation of the stabilizer U(2) × U(p) on ℂ^p. Since this representation is a homomorphism from U(2) × U(p) to GL(p, ℂ), the quotient bundle Q is a homogeneous vector bundle, hence U(p+2)-equivariant.

Wait, but here the quotient bundle is ℂ^{p+2}/V, which is a complex vector space of dimension p. The stabilizer acts on V via U(2) and on the orthogonal complement via U(p), so the quotient bundle's fiber is the orthogonal complement, which carries a natural U(p) action. But in the homogeneous bundle construction, the fiber over the base point (the chosen V) is the representation of the stabilizer. So if the stabilizer acts on ℂ^{p+2}/V via its U(p) factor, then yes, the quotient bundle is the homogeneous bundle induced by the U(p) representation. Hence, it's U(p+2)-equivariant.

So both from the perspective of the group action preserving the subbundle and quotienting, and from the homogeneous bundle construction, Q should be equivariant.

Is there any possible obstruction? Maybe if the action doesn't lift? But in this case, since the bundle is associated to a representation of the stabilizer, it should automatically have an equivariant structure. Equivariant bundles over homogeneous spaces G/H correspond to representations of H, and since Q is constructed from such a representation (the U(p) part), it must be equivariant.

Therefore, after considering both the direct check of the group action and the homogeneous bundle perspective, I think the answer is yes, Q(Gr(p+2,2)) is U(p+2)-equivariant.

**Final Answer**
\boxed{Yes}
</think>

To determine whether the vector bundle \( Q(\operatorname{Gr}(p+2,2)) \) is \( U(p+2) \)-equivariant, we start by noting that the Grassmannian \( \operatorname{Gr}(p+2,2) \) is a homogeneous space for the unitary group \( U(p+2) \). This group acts transitively on the Grassmannian, meaning any 2-dimensional subspace can be mapped to any other by a unitary transformation.

The quotient bundle \( Q \) is defined as the quotient of the trivial bundle \( \operatorname{Gr}(p+2,2) \times \mathbb{C}^{p+2} \) by the tautological subbundle \( S \). The fiber of \( Q \) over a subspace \( V \) is \( \mathbb{C}^{p+2}/V \). 

The key point is that the action of \( U(p+2) \) on the trivial bundle preserves the subbundle \( S \). This is because if \( (V, v) \) is in \( S \), then applying a unitary transformation \( g \) sends \( V \) to \( gV \) and \( v \) to \( gv \), which remains in \( gV \). Consequently, the action of \( U(p+2) \) descends to the quotient bundle \( Q \), making the projection map equivariant.

Additionally, considering the homogeneous vector bundle perspective, \( \operatorname{Gr}(p+2,2) \) can be written as \( U(p+2)/(U(2) \times U(p)) \). The stabilizer subgroup \( U(2) \times U(p) \) acts on the fiber \( \mathbb{C}^{p+2}/V \) (which is isomorphic to \( \mathbb{C}^p \)) through its \( U(p) \) factor. This representation induces the quotient bundle \( Q \), confirming it is a homogeneous vector bundle and thus \( U(p+2) \)-equivariant.

Therefore, the quotient bundle \( Q(\operatorname{Gr}(p+2,2)) \) is indeed \( U(p+2) \)-equivariant.

\[
\boxed{Yes}
\]

## AI's Thinking (Attempted Solution Process)

Let me think about this problem carefully.

The problem: Given an infinite cardinal κ, determine if there exists a graph on κ vertices that contains 2^κ pairwise non-isomorphic induced subgraphs.

First, let me check for answer leaks. The problem statement is clean - no solutions, no hints, no formalization notes. Good.

Now let me think about the mathematics.

We have an infinite cardinal κ. We want a graph G on κ vertices such that G has 2^κ pairwise non-isomorphic induced subgraphs.

First, some basic counting:
- A graph on κ vertices has at most 2^κ subsets of vertices, so at most 2^κ induced subgraphs.
- The number of graphs on λ vertices (up to isomorphism) for infinite λ: this is 2^λ (since there are 2^(λ choose 2) = 2^λ labeled graphs, and each isomorphism class has size at most 2^λ... wait, let me be more careful).

Actually, the number of isomorphism classes of graphs on λ vertices:
- Number of labeled graphs on λ vertices = 2^(λ·(λ-1)/2) = 2^λ for infinite λ.
- Number of isomorphism classes: each isomorphism class has size at most λ^λ = 2^λ (number of permutations of λ). So the number of isomorphism classes is at least 2^λ / 2^λ which could be 1... that's not useful.

Actually, more carefully: the number of isomorphism classes of graphs on λ vertices is 2^λ for infinite λ. This is a classical result. The upper bound is 2^λ (since there are 2^λ labeled graphs). For the lower bound, we can construct 2^λ non-isomorphic graphs.

So the maximum possible number of non-isomorphic induced subgraphs of a graph on κ vertices is 2^κ (since there are at most 2^κ induced subgraphs total, and each isomorphism class is counted at least once).

The question is: can we achieve this maximum?

Let me think about this. We need a graph G on κ vertices such that the induced subgraphs realize all possible isomorphism types, or at least 2^κ distinct ones.

Actually, we need 2^κ pairwise non-isomorphic induced subgraphs. Since the total number of induced subgraphs is 2^κ, we essentially need "almost all" induced subgraphs to be pairwise non-isomorphic, or at least 2^κ of them to be pairwise non-isomorphic.

Let me think about what's known.

For κ = ℵ₀ (countable): We need a countable graph with 2^(ℵ₀) pairwise non-isomorphic induced subgraphs. Since there are 2^(ℵ₀) countable graphs up to isomorphism, and a countable graph has 2^(ℵ₀) induced subgraphs, we need a countable graph that "universally" realizes all countable graph types as induced subgraphs.

The Rado graph (random graph) is the universal countable graph - every countable graph appears as an induced subgraph. Since there are 2^(ℵ₀) non-isomorphic countable graphs, the Rado graph has 2^(ℵ₀) pairwise non-isomorphic induced subgraphs. So for κ = ℵ₀, the answer is yes.

Now for general infinite κ: We need a generalization.

The key question is whether there exists a "universal" graph on κ vertices that contains every graph on ≤ κ vertices as an induced subgraph. If such a graph exists, then since there are 2^κ non-isomorphic graphs on κ vertices, we'd be done.

But the existence of universal graphs on κ vertices is a subtle set-theoretic question. For κ = ℵ₀, the Rado graph works. For uncountable κ, the situation is more complex.

However, we don't need a universal graph in that strong sense. We just need 2^κ pairwise non-isomorphic induced subgraphs. We don't need to realize every possible graph type.

Let me think about this differently. 

Approach: Try to construct a graph on κ vertices with 2^κ pairwise non-isomorphic induced subgraphs directly.

Idea: Use a construction where different subsets of vertices give non-isomorphic induced subgraphs.

Let me think about a specific construction. Consider the following approach:

Take κ vertices, and partition them or structure them in a way that encodes information.

Actually, let me think about this more carefully. The question is asking us to "determine if there exists" such a graph. So the answer is either "yes for all infinite κ" or "it depends on κ" or "no for some κ".

Let me think about the Rado graph generalization. The Rado graph has the extension property: for any two disjoint finite sets A, B of vertices, there exists a vertex connected to all of A and none of B. 

For uncountable κ, we can consider a graph on κ vertices with the following extension property: for any two disjoint subsets A, B of size < κ, there exists a vertex connected to all of A and none of B. Such a graph would be universal for graphs on < κ vertices. But this requires κ to have certain properties (like κ^(<κ) = κ, which is related to κ being "accessible" or having κ^(<κ) = κ).

Hmm, but actually the question is simpler than universality. Let me reconsider.

We want 2^κ pairwise non-isomorphic induced subgraphs. Each induced subgraph is on some subset of the κ vertices. 

Key insight: If we can find a graph G on κ vertices such that for "many" subsets S of vertices, the induced subgraph G[S] has a unique isomorphism type, we're done.

Let me think about a direct construction.

Construction idea: Let the vertex set be κ. We want to design G so that different subsets give different isomorphism types.

One approach: Make each vertex "identifiable" in some sense, so that the induced subgraph on a subset S encodes S itself (up to some symmetry).

But for infinite graphs, vertices might not be distinguishable.

Let me think about the Rado graph approach more carefully for general κ.

Claim: For any infinite cardinal κ, there exists a graph on κ vertices with 2^κ pairwise non-isomorphic induced subgraphs.

Proof approach: 

Consider the "random graph" on κ vertices constructed via the Fraïssé limit approach or a direct probabilistic/existence argument.

Actually, let me think about whether we can always build a graph with the κ-extension property (for disjoint sets of size < κ). 

The number of pairs (A, B) of disjoint subsets of size < κ is κ^(<κ) · κ^(<κ) = κ^(<κ). For each such pair, we need to find a vertex with the right adjacency pattern. If we build the graph by transfinite induction, at stage α < κ, we have < κ vertices so far, and we need to extend. The number of requirements is κ^(<κ). If κ^(<κ) = κ, we can handle all requirements using κ vertices.

But κ^(<κ) = κ is not always true. For example, if κ = ℵ₁ and 2^(ℵ₀) > ℵ₁, then κ^(<κ) ≥ 2^(ℵ₀) > κ.

Hmm, so the universal graph approach might not work for all κ.

But we don't need universality! We just need 2^κ non-isomorphic induced subgraphs.

Let me think about this differently.

Alternative approach: Direct construction encoding subsets.

Let me try the following construction. Take the vertex set to be κ × {0, 1} or just κ, and build a graph that "encodes" information.

Actually, here's a cleaner idea. Let's think about what makes induced subgraphs non-isomorphic.

Construction: Let G be a graph on κ vertices. We want to find 2^κ subsets S ⊆ κ such that G[S] are pairwise non-isomorphic.

Idea: Build G so that it has a "rigid" structure, where each subset S produces a distinguishable graph.

Let me try a specific construction. 

Consider the following: Let the vertex set be κ. We'll build G by transfinite induction so that for each subset S of some large family, G[S] is distinguishable.

Actually, let me think about a simpler approach.

Approach via the Rado graph / random graph:

For any infinite cardinal κ, consider the following: Build a graph G on κ vertices with the property that for every two disjoint subsets A, B of V(G) with |A| + |B| < κ, there exists a vertex v ∉ A ∪ B adjacent to all of A and none of B.

Wait, this is the κ-saturated graph. As I noted, this requires κ^(<κ) = κ to build on κ vertices.

But actually, we can build a graph on κ vertices with a weaker extension property. Let me think...

Actually, let me reconsider. Maybe we don't need the full extension property. 

Here's another approach: 

For any infinite κ, we can build a graph G on κ vertices such that G contains an induced copy of every graph on ≤ κ vertices. This is stronger than what we need.

The existence of such a universal graph on κ vertices: This is known to exist when κ^(<κ) = κ. But in general, it's independent of ZFC for some κ.

Hmm, but the question asks to "determine if there exists" - suggesting there's a definite answer. Let me reconsider.

Wait, maybe the answer is simply "yes" for all infinite κ, and there's a construction that doesn't require κ^(<κ) = κ.

Let me think about a different construction.

Construction: Partition κ into κ many sets of size κ (possible since κ · κ = κ for infinite κ). Use the first part to build a "backbone" and the rest to encode information.

Actually, here's a key idea. Let me think about trees.

Consider the complete binary tree of height κ (or some variant). Actually, let me think about a different structure.

Let me think about the following construction:

Let G be a graph on κ vertices defined as follows. The vertex set is κ. We think of κ as 2^(<κ) or some subset thereof... hmm, this is getting complicated.

Let me try yet another approach.

Direct approach: We want to show that for any infinite κ, there's a graph on κ vertices with 2^κ pairwise non-isomorphic induced subgraphs.

Upper bound: Any graph on κ vertices has at most 2^κ induced subgraphs (one per subset), so at most 2^κ isomorphism classes.

Lower bound: We need to construct a graph achieving 2^κ.

Key observation: The number of isomorphism classes of graphs on κ vertices is exactly 2^κ. (Upper bound: 2^κ labeled graphs. Lower bound: there are 2^κ non-isomorphic graphs on κ vertices - this is a classical result.)

So we need a graph that "realizes" 2^κ of these isomorphism classes as induced subgraphs.

Now, here's a construction that might work:

Build G on κ vertices by transfinite induction. At each stage, we want to ensure that G contains induced copies of many different graph types.

But we need to be careful about the number of vertices available.

Actually, here's a cleaner idea. Let me use the following:

Lemma: For any infinite cardinal κ, there exists a graph G on κ vertices such that every graph on ≤ κ vertices is isomorphic to an induced subgraph of G.

If this lemma is true, then since there are 2^κ non-isomorphic graphs on κ vertices, G has 2^κ pairwise non-isomorphic induced subgraphs.

But as I noted, this lemma (existence of universal graph) requires κ^(<κ) = κ in general, which is not always true.

Hmm wait, actually the universal graph for graphs on κ vertices (not < κ vertices) might be different. Let me reconsider.

A universal graph for graphs on κ vertices: a graph on κ vertices containing every graph on κ vertices as an induced subgraph. This requires κ^(<κ) = κ? Or does it?

Actually, the Rado graph is universal for countable graphs and has ℵ₀ vertices. The generalization to uncountable κ: a universal graph on κ vertices for graphs on κ vertices.

The existence of such a graph is equivalent to... let me think. If G is on κ vertices and contains every graph on κ vertices as an induced subgraph, then in particular, for each graph H on κ vertices, there's an embedding of H into G. The number of graphs on κ vertices is 2^κ, and each embedding uses κ vertices. But G only has κ vertices, so we need to "pack" 2^κ different graphs into κ vertices.

This is possible because different induced subgraphs can share vertices - they just use different subsets.

The question is whether we can build such a G. The classical result is:

Theorem (Rado, generalization): A universal graph on κ vertices (for graphs on ≤ κ vertices) exists if and only if κ^(<κ) = κ.

Wait, I'm not sure about the "only if" direction. Let me think more carefully.

Actually, I recall that the existence of a universal graph on κ vertices is more subtle. Let me think about what's actually needed.

For the "if" direction: If κ^(<κ) = κ, we can build a graph with the κ-extension property (for disjoint A, B with |A|+|B| < κ, there's a vertex adjacent to all of A and none of B), and this graph is universal.

For the "only if" direction: If κ^(<κ) > κ, can we still have a universal graph? I think the answer is no, but I'm not 100% sure.

But actually, we don't need a universal graph! We just need 2^κ non-isomorphic induced subgraphs. Let me think about whether we can achieve this without full universality.

Alternative construction that doesn't need κ^(<κ) = κ:

Idea: Build a graph G on κ vertices that is "rigid" in a strong sense - so that different subsets give non-isomorphic induced subgraphs.

Construction: Let's build a graph where each vertex has a unique "signature" based on its neighborhood structure, so that the induced subgraph on any subset S is determined by S (up to automorphisms of G, but if G is rigid, then it's determined by S itself).

If G is rigid (trivial automorphism group) and has the property that the induced subgraph G[S] determines S (i.e., different subsets give non-isomorphic induced subgraphs), then we'd have 2^κ non-isomorphic induced subgraphs (one per subset, minus some collisions).

But can we build a rigid graph on κ vertices where different subsets give non-isomorphic induced subgraphs? That's a very strong requirement.

Hmm, let me think about this differently.

Actually, for the Rado graph (κ = ℵ₀ case), the Rado graph is NOT rigid - it has a huge automorphism group. Yet it still has 2^(ℵ₀) non-isomorphic induced subgraphs because it's universal. The universality is what matters, not rigidity.

So let me reconsider the universal graph approach.

Actually, I think the answer might be "yes for all infinite κ" and the construction might not require full universality.

Let me think about a weaker property. Instead of containing every graph on κ vertices, we just need 2^κ non-isomorphic ones.

Construction idea: 

Take κ = λ for some infinite cardinal. Partition the vertex set into κ many blocks, each of size κ (possible since κ × κ = κ). In block α, put a specific graph G_α. Choose the G_α to be pairwise non-isomorphic graphs on κ vertices. Then the induced subgraph on the union of any subcollection of blocks is determined (up to isomorphism) by which blocks are included, giving 2^κ non-isomorphic induced subgraphs.

Wait, but this requires 2^κ pairwise non-isomorphic graphs on κ vertices, and we need to fit them all into κ vertices. Each block has κ vertices, and we have κ blocks, so total vertices = κ · κ = κ. Good.

But we need 2^κ pairwise non-isomorphic graphs on κ vertices. We know there are 2^κ isomorphism classes of graphs on κ vertices, so we can pick 2^κ of them. But wait, we only have κ blocks, not 2^κ blocks!

Hmm, that's the problem. We have κ blocks, so we can only encode 2^κ subsets if... wait, 2^κ subsets of a set of size κ gives 2^κ subsets. So if we have κ blocks, the number of subsets of blocks is 2^κ. 

But we need the κ blocks to contain pairwise non-isomorphic graphs. We have κ blocks, so we need κ pairwise non-isomorphic graphs on κ vertices. That's easy - there are 2^κ ≥ κ such graphs.

Now, the induced subgraph on a subset S of blocks: this is the disjoint union of the graphs in the blocks indexed by S. For two different subsets S, S' of blocks, are the disjoint unions non-isomorphic?

If the graphs in different blocks are pairwise non-isomorphic, then the disjoint union of graphs from blocks in S is isomorphic to the disjoint union from blocks in S' if and only if S = S' (since the connected components / summands must match up, and each summand is a graph on κ vertices, which is uniquely identified by its isomorphism type).

Wait, but the disjoint union of graphs from blocks in S: each block contributes a connected component (if the graph in each block is connected). Then the isomorphism type of the disjoint union is determined by the multiset of isomorphism types of the components. If each block has a distinct isomorphism type, then the multiset is just the set S (since each type appears at most once). So different subsets S give different multisets, hence non-isomorphic disjoint unions.

But we need each block's graph to be connected (so that the blocks don't "merge" into larger components). We can ensure this by making each G_α a connected graph.

Also, we need the G_α to be pairwise non-isomorphic. Since there are 2^κ non-isomorphic connected graphs on κ vertices (is this true?), we can pick κ of them.

Is it true that there are 2^κ non-isomorphic connected graphs on κ vertices? For κ = ℵ₀, yes (there are 2^(ℵ₀) non-isomorphic countable connected graphs). For general κ: the number of labeled connected graphs on κ vertices is 2^κ (since almost all graphs on κ vertices are connected - the number of disconnected graphs is at most Σ_{λ<κ} (number of graphs on λ vertices) × (number of graphs on κ vertices) × (ways to choose the λ-subset) = ... hmm, this needs care for singular κ).

Actually, for regular κ, the number of disconnected graphs on κ vertices: a disconnected graph on κ vertices has a connected component of size < κ. The number of such graphs is at most Σ_{λ<κ} C(κ, λ) · 2^λ · 2^κ = Σ_{λ<κ} κ^λ · 2^κ. For regular κ, κ^λ ≤ κ^(<κ) for λ < κ. Hmm, this could be larger than 2^κ.

Let me think about this differently. Actually, I don't need connected graphs. Let me modify the construction.

Modified construction: Instead of using disjoint unions, use a different way to combine graphs that ensures distinguishability.

Alternative: Use a "tagged" construction. For each α < κ, create a block B_α of vertices, and add a special "marker" structure that identifies which block a vertex belongs to. Then the induced subgraph on a subset S of blocks is determined by S.

For example: Add a "hub" vertex h_α for each block B_α, connected to all vertices in B_α and to a central vertex. Different subsets of blocks give different induced subgraphs because the hub structure encodes which blocks are present.

Hmm, but this is getting complicated. Let me think more carefully.

Actually, let me go back to the disjoint union idea but handle the connectedness issue.

Claim: For any infinite cardinal κ, there exist κ pairwise non-isomorphic connected graphs on κ vertices.

Proof sketch: Consider graphs of the form: a path of length α (for α < κ) attached to a complete graph on κ vertices. Wait, that doesn't quite work because for infinite α, the "path of length α" might not change the isomorphism type.

Let me think of a better family. Consider the following graphs on κ vertices:
- For each subset A of κ (or each cardinal λ ≤ κ), define a graph G_λ that has a clique of size λ and the rest of the vertices form an independent set, with some specific connection pattern.

Actually, a simpler family: For each infinite cardinal λ ≤ κ, let G_λ be the complete graph K_λ together with κ \ λ isolated vertices. But the number of infinite cardinals ≤ κ is at most countable (for κ = ℵ_ω) or finite, so this doesn't give κ non-isomorphic graphs.

Better: For each α < κ, let G_α be a graph on κ vertices defined as follows. Take a set of α "special" vertices forming a path P_α, and the remaining κ vertices form a clique, with each special vertex connected to exactly one clique vertex. For different α, these are non-isomorphic (the path length distinguishes them). But for infinite α, we need to be careful - paths of different infinite lengths might be distinguishable.

Actually, for α < κ, the path P_α has α vertices. If α ≠ β, then P_α and P_β have different numbers of vertices, so G_α and G_β are non-isomorphic (since the "path part" has different cardinality). Wait, but both G_α and G_β have κ vertices total. The path part has α vs β vertices, and the clique part has κ vs κ vertices. If α ≠ β and both are < κ, then... hmm, the clique parts both have κ vertices (since κ - α = κ for α < κ). So the clique parts are isomorphic. The path parts have α vs β vertices. If α ≠ β, the paths are non-isomorphic (different cardinalities). But in G_α, the path is attached to the clique, so the isomorphism type of G_α depends on α.

Actually, I think this works but let me be more careful. In G_α, the structure is: a clique C of size κ, a path P of size α, and each vertex of P is connected to a unique vertex of C (say, the first vertex of P is connected to one vertex of C). The key distinguishing feature is the path P_α, which has α vertices. For α ≠ β (both < κ), the paths have different cardinalities, so G_α ≇ G_β.

But wait, for infinite α, β < κ with α ≠ β, do the paths P_α and P_β have different cardinalities? Yes, |P_α| = α and |P_β| = β, and if α ≠ β then |P_α| ≠ |P_β|... no wait, different ordinals can have the same cardinality. E.g., α = ω and β = ω + ω both have cardinality ℵ₀.

So I should use cardinals, not ordinals. For each cardinal λ < κ, define G_λ with a path of cardinality λ. The number of cardinals < κ is at most κ (and for κ = ℵ₀, it's just finite cardinals, which is countable = κ). Hmm, for κ = ℵ₀, the cardinals < κ are the finite cardinals and... wait, there are no infinite cardinals < ℵ₀. So we'd only get countably many (the finite ones), which is ℵ₀ = κ. Good.

For κ = ℵ₁, the cardinals < κ are the finite ones and ℵ₀, giving countably many, which is < κ = ℵ₁. That's not enough!

So this approach doesn't give κ non-isomorphic graphs for all κ.

Let me think of a better family.

Better family: For each α < κ (as an ordinal), define G_α to be a graph that encodes α in its structure. For instance, use a well-ordering structure.

Actually, here's a cleaner approach. For each subset S ⊆ κ, define a graph G_S on κ vertices. But we need κ pairwise non-isomorphic ones, and there are 2^κ subsets, so we can certainly find κ non-isomorphic ones (since there are 2^κ ≥ κ isomorphism classes).

Wait, I think I'm overcomplicating this. The key fact is:

Fact: For any infinite cardinal κ, there are 2^κ non-isomorphic graphs on κ vertices.

This is well-known. The upper bound is 2^κ (number of labeled graphs). For the lower bound, one can construct 2^κ non-isomorphic graphs explicitly.

Given this fact, there are certainly at least κ non-isomorphic graphs on κ vertices (since 2^κ ≥ κ for infinite κ). So we can pick κ pairwise non-isomorphic graphs G_α (α < κ) on κ vertices each.

Now, the construction: 
- Vertex set: κ × κ (which has cardinality κ).
- For each α < κ, the α-th block is {α} × κ, and the induced subgraph on this block is G_α.
- No edges between different blocks.

The resulting graph G has κ vertices and is the disjoint union of the G_α.

Now, for any subset S ⊆ κ, the induced subgraph G[S × κ] is the disjoint union of {G_α : α ∈ S}.

Question: For different subsets S, S' ⊆ κ, are the disjoint unions ⊔_{α∈S} G_α and ⊔_{α∈S'} G_α non-isomorphic?

If the G_α are pairwise non-isomorphic AND each G_α is connected, then yes: the connected components of the disjoint union are exactly the G_α for α ∈ S, and since they're pairwise non-isomorphic, the isomorphism type of the disjoint union determines S.

But we need each G_α to be connected. Can we find κ pairwise non-isomorphic connected graphs on κ vertices?

For this, we need: there are at least κ non-isomorphic connected graphs on κ vertices.

Claim: For any infinite cardinal κ, there are 2^κ non-isomorphic connected graphs on κ vertices.

Proof of claim: 
- Upper bound: 2^κ (total number of graphs on κ vertices).
- Lower bound: We construct 2^κ non-isomorphic connected graphs on κ vertices.

Construction for lower bound: Take any graph H on κ vertices. Form H' by adding a new vertex connected to all vertices of H... but that adds a vertex, making it κ+1 vertices. Instead, take H and pick one vertex v, connecting v to all other vertices. This makes H' connected (every vertex is at distance ≤ 2 from v). But different H might give isomorphic H'.

Better: Take H on κ vertices, and form H* by adding a "universal vertex" - but we need to stay on κ vertices. 

Alternative: Take H on κ vertices with a distinguished vertex v. Form H* = H ∪ {edges from v to all other vertices}. H* is connected. If H₁* ≅ H₂*, then... the universal vertex in H₁* (the one connected to all others) must map to the universal vertex in H₂*. But there might be multiple universal vertices. 

Hmm, let me think of a cleaner construction.

Cleaner construction: For each graph H on κ vertices (with vertex set κ), define H* as follows: the vertex set is κ × {0, 1}. For each n, (α, 0) is connected to (β, 0) iff α ~ β in H. Also, (α, 0) is connected to (α, 1) for all α. And (α, 1) is connected to (β, 1) for all α, β (i.e., the {1}-layer is a clique). No edges between (α, 1) and (β, 0) for α ≠ β.

Wait, this doubles the vertex count to 2κ = κ, which is fine. H* is connected because the {1}-layer is a clique and every (α, 0) is connected to (α, 1).

If H₁* ≅ H₂*, then the {1}-layer (clique of size κ) must map to the {1}-layer. So the {0}-layer maps to the {0}-layer, and the edges within the {0}-layer are preserved. So H₁ ≅ H₂.

This gives 2^κ non-isomorphic connected graphs on κ vertices (one for each isomorphism class of graphs on κ vertices).

Wait, I need to be more careful. The {1}-layer is a clique of size κ. In H*, is the {1}-layer the unique maximum clique? Not necessarily - H might have a large clique too. But the {1}-layer has the property that each vertex in it is connected to exactly one vertex in the {0}-layer (namely, (α,1) is connected to (α,0)). The {0}-layer vertices are connected to their H-neighbors in the {0}-layer and to exactly one {1}-layer vertex.

Hmm, the issue is that an isomorphism might not preserve the layers. Let me make the layers more distinguishable.

Modified construction: H* has vertex set κ × {0, 1, 2}. 
- Layer 0: (α, 0) ~ (β, 0) iff α ~ β in H.
- Layer 1: (α, 1) ~ (β, 1) for all α, β (clique). (α, 1) ~ (α, 0) for all α.
- Layer 2: (α, 2) ~ (β, 2) for all α, β (clique). (α, 2) ~ (α, 1) for all α. (α, 2) ~ (α, 0) for all α.
- No other edges.

So each (α, 2) is connected to (α, 0), (α, 1), and all (β, 2). Each (α, 1) is connected to (α, 0), (α, 2), and all (β, 1). Each (α, 0) is connected to (α, 1), (α, 2), and (β, 0) for β ~ α in H.

The degree of (α, 2) in H*: connected to all (β, 2) for β ≠ α (that's κ-1 = κ vertices), plus (α, 0) and (α, 1). So degree = κ + 2 = κ.
The degree of (α, 1) in H*: connected to all (β, 1) for β ≠ α (κ vertices), plus (α, 0) and (α, 2). Degree = κ.
The degree of (α, 0) in H*: connected to (α, 1), (α, 2), and deg_H(α) vertices in layer 0. Degree = 2 + deg_H(α).

So vertices in layer 0 have degree 2 + deg_H(α), while vertices in layers 1 and 2 have degree κ. For most H (where deg_H(α) < κ for all α), the layer 0 vertices have degree < κ + 2, while layers 1, 2 have degree κ. But if H has vertices of degree κ, this doesn't distinguish.

This is getting complicated. Let me use a different approach to ensure the layers are distinguishable.

Actually, let me use a much simpler approach. Instead of trying to make connected graphs, let me modify the main construction to not require connectedness.

Revised main construction:

Instead of using disjoint unions (which requires connected components to be distinguishable), use a different combining method.

Construction: Build a graph G on κ vertices as follows. Partition V(G) = κ into blocks B_α (α < κ), each of size κ. For each α, the induced subgraph G[B_α] is some graph H_α on κ vertices. Additionally, add a "marker" structure between blocks to make them distinguishable.

Specifically: Add a special vertex c (a "center") connected to all vertices. Wait, but then the center is in some block.

Let me try a different approach. Let me use the following:

Construction: 
- V(G) = κ × κ (cardinality κ).
- For each α < κ, block B_α = {α} × κ.
- G[B_α] = H_α (a specific graph on κ vertices, to be chosen).
- Between blocks: (α, β) is connected to (α', β') for α ≠ α' if and only if β = 0 and β' = 0 (i.e., the "first" vertex of each block forms a clique across blocks).

Hmm, this is getting messy. Let me think about this more carefully.

Actually, let me try a completely different approach.

Approach: Use the fact that for any infinite κ, there's a graph on κ vertices that is "sufficiently rich."

Let me think about the problem from the perspective of the answer. The question asks "determine if there exists" - I believe the answer is YES for all infinite κ, and the proof should work in ZFC.

Let me try the following clean construction:

Construction:
Let V = κ. We build G by specifying edges.

For each α < κ, let f_α: α → {0, 1} be a function (we'll choose these later). Define G such that for β < α < κ, there is an edge between β and α iff f_α(β) = 1.

So G is a graph where vertex α is connected to vertex β (for β < α) according to f_α(β). This is like a "triangle-free" construction where edges only go from lower to higher indices (well, the graph is undirected, but we're defining it via a tournament-like structure).

Now, for a subset S ⊆ κ, the induced subgraph G[S] is determined by the functions f_α restricted to S ∩ α for α ∈ S.

If we choose the f_α cleverly, different subsets S will give non-isomorphic induced subgraphs.

But how to choose f_α? And how to ensure 2^κ non-isomorphic induced subgraphs?

This is related to the Rado graph construction. The Rado graph can be defined exactly this way: vertex n is connected to vertex m (m < n) iff the m-th bit of n is 1. The Rado graph is universal for countable graphs.

For uncountable κ, we can try a similar construction, but the universality might fail.

Hmm, let me think about this problem from a higher level.

I think the answer is YES for all infinite κ, and here's why:

The key insight is that we don't need universality. We just need 2^κ non-isomorphic induced subgraphs, which is the maximum possible. 

Here's a construction that I think works:

Step 1: Note that there are 2^κ non-isomorphic graphs on κ vertices (classical fact).

Step 2: We want to "embed" 2^κ non-isomorphic graphs into a single graph on κ vertices as induced subgraphs.

Step 3: The construction: Partition κ into κ blocks of size κ. In each block, place a graph. Use a marker structure to distinguish blocks. Then subsets of blocks give 2^κ non-isomorphic induced subgraphs.

The challenge is Step 3 - making the marker structure work. Let me think about this more carefully.

Marker structure idea: 

For each α < κ, block B_α = {α} × κ. 

Define G as follows:
1. Within each block B_α, the induced subgraph is H_α (a connected graph on κ vertices, with the H_α pairwise non-isomorphic).
2. Between blocks: for α < α' < κ, connect (α, 0) to (α', 0). (So the "0-th" vertex of each block forms a path/clique across blocks.)

With this structure, the vertex (α, 0) in block B_α is the unique vertex in B_α that has neighbors outside B_α. So in any induced subgraph that includes entire blocks, the "connector" vertices are identifiable.

But we're taking induced subgraphs on arbitrary subsets, not just unions of blocks. So this doesn't directly work.

Let me reconsider. The issue is that we want to take induced subgraphs on arbitrary subsets of V(G), not just unions of blocks. But if we take the induced subgraph on a union of blocks (S × κ for some S ⊆ κ), then the connector vertices help identify the blocks.

So the plan is:
- For each S ⊆ κ, consider the induced subgraph G_S = G[S × κ].
- Show that different S give non-isomorphic G_S.
- This gives 2^κ non-isomorphic induced subgraphs.

For this to work, we need:
1. The H_α are pairwise non-isomorphic connected graphs on κ vertices.
2. The connector structure allows us to identify which blocks are present.

For (2): In G_S, the connector vertices are {(α, 0) : α ∈ S}. These are the vertices that have neighbors in other blocks. But actually, in G_S = G[S × κ], the connector vertex (α, 0) is connected to (α', 0) for α' ∈ S, α' ≠ α (if we made them a clique) or just to adjacent ones (if we made them a path). 

Hmm, but the non-connector vertices in block B_α (i.e., (α, β) for β > 0) have all their neighbors within B_α. So in G_S, the connected components are... well, if H_α is connected and the connector vertices link the blocks, then G_S might be connected. That's a problem because then we can't decompose it into blocks.

Let me modify: Don't connect the blocks at all. Make G the disjoint union of the H_α.

Then G_S = G[S × κ] = ⊔_{α ∈ S} H_α.

If the H_α are pairwise non-isomorphic and connected, then the connected components of G_S are exactly {H_α : α ∈ S}, and since they're pairwise non-isomorphic, G_S determines S (as a set of isomorphism types). So different S give non-isomorphic G_S.

This gives 2^κ non-isomorphic induced subgraphs (one for each S ⊆ κ).

The only thing we need is: κ pairwise non-isomorphic connected graphs on κ vertices.

As I discussed above, there are 2^κ non-isomorphic connected graphs on κ vertices (I gave a construction). So we can certainly pick κ of them.

Wait, but I need to verify the claim that there are 2^κ non-isomorphic connected graphs on κ vertices more carefully.

Claim: For any infinite cardinal κ, there are 2^κ non-isomorphic connected graphs on κ vertices.

Proof: 
- Upper bound: 2^κ (total graphs on κ vertices).
- Lower bound: Given any graph H on κ vertices, construct a connected graph H* on κ vertices such that H can be recovered from H* up to isomorphism. This gives an injection from isomorphism classes of graphs on κ vertices to isomorphism classes of connected graphs on κ vertices, proving the lower bound.

Construction of H*: 
Let H have vertex set V. H* has vertex set V × {0, 1} (cardinality 2κ = κ).
- Edges within V × {0}: (u, 0) ~ (v, 0) iff u ~ v in H.
- Edges within V × {1}: (u, 1) ~ (v, 1) for all u ≠ v (clique).
- Edges between layers: (u, 0) ~ (u, 1) for all u (matching).
- No other edges between layers.

H* is connected: every (u, 0) is connected to (u, 1), and all (u, 1) are connected to each other.

Recovery: Given H* up to isomorphism, can we recover H up to isomorphism?

In H*, the V × {1} layer is a clique of size κ. The V × {0} layer has the structure of H. Each vertex in V × {1} has degree κ (connected to all other V × {1} vertices plus one V × {0} vertex). Each vertex in V × {0} has degree deg_H(u) + 1.

If H has a vertex of degree κ, then (u, 0) has degree κ + 1 = κ, same as (u, 1). So we can't distinguish layers by degree alone.

But we can distinguish by structure: vertices in V × {1} form a clique, while vertices in V × {0} form H (which is generally not a clique). 

More precisely: In H*, consider the relation "u and v have κ common neighbors." Two vertices in V × {1} have κ common neighbors (all other V × {1} vertices). A vertex in V × {1} and a vertex in V × {0} have... let me compute. (u, 1) and (v, 0) with u ≠ v: common neighbors are (u, 0) [neighbor of (u,1) via matching, and of (v,0) iff u~v in H] and (w, 1) for w ≠ u [neighbor of (u,1) via clique, and of (v,0)? No, (v,0) is only connected to (v,1) in the {1} layer, not to (w,1) for w ≠ v]. So common neighbors of (u,1) and (v,0) (u ≠ v) are: {(u,0)} if u~v in H, plus possibly some others... 

Actually (v,0) is connected to (v,1) and to (w,0) for w~v in H. (u,1) is connected to (u,0) and (w,1) for all w ≠ u. Common neighbors: (u,0) is a neighbor of (u,1) [yes, via matching] and of (v,0) [yes, iff u~v in H]. (v,1) is a neighbor of (v,0) [yes, via matching] and of (u,1) [yes, iff u ≠ v, which is true]. So (v,1) is a common neighbor. Any (w,1) for w ≠ u, v: neighbor of (u,1) [yes] and of (v,0) [no, (v,0) is only connected to (v,1) in layer 1]. Any (w,0) for w ~ v in H, w ≠ u: neighbor of (v,0) [yes] and of (u,1) [no, (u,1) is only connected to (u,0) in layer 0]. 

So common neighbors of (u,1) and (v,0) (u ≠ v) are: (v,1) always, and (u,0) iff u~v in H. That's 1 or 2 common neighbors.

Two vertices in V × {0}: (u,0) and (v,0), u ≠ v. Common neighbors: (u,1) [neighbor of (u,0) via matching, of (v,0)? No, (v,0) is connected to (v,1) not (u,1)]. (v,1) [neighbor of (v,0) via matching, of (u,0)? No]. (w,0) for w ~ u and w ~ v in H. (w,1) for... (w,1) is a neighbor of (u,0)? No, (u,0) is only connected to (u,1) in layer 1. So common neighbors of (u,0) and (v,0) are: {(w,0) : w ~ u and w ~ v in H} ∪ {(u,1) if v ~ u in H} ∪ {(v,1) if u ~ v in H}. 

Hmm wait, (u,1) is a neighbor of (u,0) [matching] and of (v,0)? (v,0) is connected to (v,1) and (w,0) for w~v. (u,1) is not (v,1) (since u≠v) and not a (w,0). So (u,1) is NOT a neighbor of (v,0). Similarly (v,1) is not a neighbor of (u,0).

So common neighbors of (u,0) and (v,0) are {(w,0) : w ~ u and w ~ v in H}. This could be anywhere from 0 to κ.

Two vertices in V × {1}: (u,1) and (v,1), u ≠ v. Common neighbors: all (w,1) for w ≠ u, v [that's κ - 2 = κ vertices], plus (u,0) [neighbor of (u,1), and of (v,1)? (v,1) is connected to (v,0) and all (w,1). (u,0) is not (v,0) and not a (w,1). So no]. Similarly (v,0) is not a common neighbor. So common neighbors = {(w,1) : w ≠ u, v}, which has cardinality κ.

So:
- Two vertices in V×{1}: κ common neighbors.
- (u,1) and (v,0), u≠v: 1 or 2 common neighbors.
- Two vertices in V×{0}: variable, depends on H.

The key distinguishing feature: vertices in V×{1} have the property that they share κ common neighbors with other V×{1} vertices. Vertices in V×{0} don't have this property (unless H is very special).

More precisely, define a vertex v in H* to be "clique-type" if there exists another vertex w such that v and w have κ common neighbors. The V×{1} vertices are clique-type (pair with any other V×{1} vertex). A V×{0} vertex (u,0) is clique-type only if there exists w such that (u,0) and w have κ common neighbors. 

For (u,0) and (v,1) (v ≠ u): common neighbors are 1 or 2 (as computed). Not κ.
For (u,0) and (v,0) (v ≠ u): common neighbors are {(w,0) : w ~ u, w ~ v in H}. This is κ only if u and v have κ common neighbors in H.

So if H is a graph where no two vertices have κ common neighbors, then the clique-type vertices are exactly V×{1}, and we can identify the V×{1} layer. Then the V×{0} layer is the complement, and H is recovered as the induced subgraph on V×{0} minus the matching edges to V×{1}.

But what if H does have pairs with κ common neighbors? Then some V×{0} vertices might also be "clique-type," and we can't distinguish the layers.

To handle this, we can restrict to graphs H where no two vertices have κ common neighbors. Are there 2^κ such graphs? 

For κ = ℵ₀: a graph where no two vertices have infinitely many common neighbors. There are 2^(ℵ₀) such graphs (e.g., graphs with bounded degree, or more generally, graphs where each pair has finitely many common neighbors). Actually, we need to be more careful. The number of graphs on ℵ₀ vertices where every pair has finitely many common neighbors: this is a large class, certainly 2^(ℵ₀).

For general κ: graphs where every pair has < κ common neighbors. The number of such graphs is... well, "most" graphs have this property. Specifically, a random graph on κ vertices (in a suitable sense) will have this property. But let me think about whether there are 2^κ such graphs.

Actually, consider graphs of bounded degree (degree < κ for all vertices, or even finite degree). There are 2^κ such graphs on κ vertices (e.g., for each subset S of κ, define a graph where vertex α is connected to vertex α+1 iff α ∈ S, giving a graph of maximum degree 2 with 2^κ non-isomorphic types... hmm, actually this gives only κ non-isomorphic types since the graph is determined by S up to shift).

Let me think of a better family. For each function f: κ → {0, 1, 2}, define a graph H_f on κ × {0, 1} vertices... this is getting complicated.

Actually, let me just use a different construction for H* that doesn't have this issue.

Alternative construction of H*: 

H* has vertex set V × {0, 1, 2} (cardinality 3κ = κ).
- Layer 0: (u, 0) ~ (v, 0) iff u ~ v in H.
- Layer 1: (u, 1) ~ (v, 1) for all u, v (clique). (u, 1) ~ (u, 0) for all u.
- Layer 2: (u, 2) is connected to (u, 1) for all u, and to no other vertices.

So layer 2 vertices are "leaves" - each (u, 2) has degree 1, connected only to (u, 1). Layer 1 is a clique, each (u, 1) connected to (u, 0) and (u, 2) and all (v, 1). Layer 0 has the structure of H, each (u, 0) connected to (u, 1) and H-neighbors.

H* is connected (via layer 1 clique).

Recovery: The degree-1 vertices are exactly layer 2. Each degree-1 vertex (u, 2) is connected to (u, 1). So we can identify layer 1 as the neighbors of degree-1 vertices. Then layer 0 is the rest. H is the induced subgraph on layer 0.

Wait, but (u, 1) might also have other degree-1 neighbors? No, (u, 1) is connected to (u, 0), (u, 2), and all (v, 1) for v ≠ u. So (u, 2) is the only degree-1 neighbor of (u, 1). And (u, 2) has degree 1 (connected only to (u, 1)).

But could a vertex in layer 0 have degree 1? (u, 0) is connected to (u, 1) and to H-neighbors. If u is isolated in H, then (u, 0) has degree 1 (connected only to (u, 1)). So degree-1 vertices include all of layer 2 and possibly some of layer 0 (corresponding to isolated vertices in H).

Hmm, so we can't cleanly separate layer 2 from layer 0 using degree alone.

But we can use a different distinguishing feature. A degree-1 vertex in layer 2, (u, 2), is connected to (u, 1), which has degree κ (connected to all (v, 1) plus (u, 0) and (u, 2)). A degree-1 vertex in layer 0, (u, 0) (where u is isolated in H), is connected to (u, 1), which also has degree κ. So both types of degree-1 vertices are connected to degree-κ vertices. We can't distinguish them this way.

Let me add another layer to make the distinction clearer.

H* with vertex set V × {0, 1, 2, 3}:
- Layer 0: (u,0) ~ (v,0) iff u~v in H.
- Layer 1: (u,1) ~ (v,1) for all u,v (clique). (u,1) ~ (u,0) for all u.
- Layer 2: (u,2) ~ (u,1) for all u. No other edges for layer 2.
- Layer 3: (u,3) ~ (u,2) for all u. No other edges for layer 3.

So we have a chain: (u,3) - (u,2) - (u,1) - (u,0), with layer 1 being a clique.

Degree of (u,3): 1 (connected to (u,2) only).
Degree of (u,2): 2 (connected to (u,1) and (u,3)).
Degree of (u,1): κ (connected to all (v,1), plus (u,0) and (u,2)).
Degree of (u,0): deg_H(u) + 1 (connected to (u,1) and H-neighbors).

Now, the degree-1 vertices are: (u,3) for all u, and (u,0) for isolated u in H.
The degree-2 vertices are: (u,2) for all u, and (u,0) for u with deg_H(u) = 1.

A degree-1 vertex (u,3) is connected to (u,2) which has degree 2. A degree-1 vertex (u,0) (isolated in H) is connected to (u,1) which has degree κ. So we can distinguish: degree-1 vertices connected to degree-2 vertices are in layer 3, and degree-1 vertices connected to degree-κ vertices are in layer 0 (isolated in H).

Similarly, degree-2 vertices (u,2) are connected to (u,1) [degree κ] and (u,3) [degree 1]. A degree-2 vertex (u,0) with deg_H(u) = 1 is connected to (u,1) [degree κ] and one H-neighbor [variable degree]. So (u,2) has a degree-1 neighbor, while (u,0) with deg_H = 1 has a neighbor of degree deg_H(neighbor) + 1, which is not necessarily 1.

So we can identify layer 3 (degree-1 vertices whose neighbor has degree 2), then layer 2 (degree-2 vertices connected to a layer-3 vertex), then layer 1 (degree-κ vertices connected to a layer-2 vertex), then layer 0 (the rest).

From layer 0, we recover H.

This works! But it's getting complicated. Let me simplify.

Actually, the simplest approach: use a long enough "tail" to make the layers unambiguously identifiable.

Even simpler: Let me just use the following construction.

For each graph H on κ vertices, define H* on κ vertices as follows:

H* has vertex set V(H) × {0, 1}.
- (u, 0) ~ (v, 0) iff u ~ v in H.
- (u, 1) ~ (v, 1) for all u, v (clique).
- (u, 0) ~ (u, 1) for all u.
- No other cross-layer edges.

H* is connected. |V(H*)| = 2κ = κ.

Now, I claim that H₁* ≅ H₂* implies H₁ ≅ H₂, provided H₁ and H₂ are "nice" (e.g., have no clique of size κ).

If H has no clique of size κ, then in H*, the unique clique of size κ is the layer 1. So any isomorphism H₁* → H₂* must map layer 1 of H₁* to layer 1 of H₂*. Then it maps layer 0 to layer 0, and the induced subgraph on layer 0 is H, so H₁ ≅ H₂.

So for graphs H with no κ-clique, H ↦ H* is an injection on isomorphism classes.

Are there 2^κ non-isomorphic graphs on κ vertices with no clique of size κ? Yes! For example, triangle-free graphs. The number of non-isomorphic triangle-free graphs on κ vertices is 2^κ (this is a classical result - one can construct 2^κ non-isomorphic triangle-free graphs, e.g., using bipartite graphs or other constructions).

Actually, let me verify: the number of non-isomorphic triangle-free graphs on κ vertices is 2^κ.

Upper bound: 2^κ.
Lower bound: Consider bipartite graphs with parts A and B, each of size κ. A bipartite graph is triangle-free. The number of non-isomorphic bipartite graphs on κ + κ vertices... hmm, but we need graphs on κ vertices, not 2κ.

Let me think again. A bipartite graph on κ vertices with parts of size κ/2 = κ each (for infinite κ, κ = κ + κ). So a bipartite graph on κ vertices with parts A, B each of size κ. The number of such graphs is 2^(κ·κ) = 2^κ. The number of isomorphism classes: each isomorphism class has size at most κ^κ = 2^κ (permutations of κ vertices). So the number of isomorphism classes is at least 2^κ / 2^κ = 1, which is useless.

Hmm, let me think about this differently. 

Actually, for the lower bound on non-isomorphic triangle-free graphs: we can use the following. For each subset S of κ, define a graph G_S on κ vertices that is triangle-free and such that different S give non-isomorphic graphs. 

One construction: Let V = κ × {0, 1}. For each S ⊆ κ, define G_S as a bipartite graph with parts A = κ × {0} and B = κ × {1}, where (α, 0) ~ (β, 1) iff (α, β) ∈ some set determined by S. 

For instance, fix an injection φ: κ → κ × κ (possible since κ × κ = κ). For S ⊆ κ, define (α, 0) ~ (β, 1) iff φ(α) = (β, s) for some s ∈ S. Hmm, this is getting complicated.

Let me use a simpler approach. For each S ⊆ κ, define G_S on vertex set κ as follows: vertex α is connected to vertex β (α < β) iff α ∈ S and β = α + 1. Wait, this gives a graph that's a union of paths, and the isomorphism type depends on the pattern of S, but many different S give the same isomorphism type.

OK let me try yet another approach. I think the cleanest way is:

Fact: For any infinite cardinal κ, there are 2^κ non-isomorphic graphs on κ vertices.

This is a standard result. The proof: upper bound is 2^κ. For the lower bound, one can use the following construction. For each binary sequence s ∈ 2^κ, define a graph G_s on κ vertices. The graphs G_s are pairwise non-isomorphic. 

One such construction: For each s: κ → {0, 1}, define G_s on vertex set κ × {0, 1, 2} as follows:
- (α, 0) ~ (β, 0) for all α, β (clique of size κ).
- (α, 1) ~ (α, 0) for all α.
- (α, 2) ~ (α, 1) for all α.
- (α, 1) ~ (β, 2) iff s(α) = 1 and β = α. (Wait, this doesn't use s meaningfully.)

Hmm, let me think of a better construction.

Actually, here's a clean construction for 2^κ non-isomorphic graphs on κ vertices:

For each s ∈ 2^κ, define G_s on vertex set κ × {0, 1} (size 2κ = κ):
- Layer 0: κ × {0} is a clique.
- Layer 1: κ × {1} is an independent set.
- (α, 0) ~ (β, 1) iff s(α) = 1 and β = α. Wait, this connects (α, 0) to (α, 1) based on s(α). But then the degree of (α, 1) is 0 or 1, and the degree of (α, 0) is κ (from the clique) plus 0 or 1.

The isomorphism type of G_s: the vertices of degree κ+1 = κ in the clique are those (α, 0) with s(α) = 1, and those with s(α) = 0 have degree κ. But κ+1 = κ, so all clique vertices have degree κ. The independent set vertices have degree 0 or 1.

Hmm, the issue is that for infinite cardinals, κ + 1 = κ, so degree doesn't distinguish.

Let me use a different approach. For each s ∈ 2^κ, define G_s on vertex set κ:
- G_s is a graph where the degree sequence "encodes" s.

But for infinite graphs, the degree of each vertex is a cardinal ≤ κ, and there are only κ+1 possible degrees. So we can encode at most (κ+1)^κ = 2^κ different degree sequences, which is enough. But the issue is that many graphs share the same degree sequence.

OK, I think I'm overcomplicating this. Let me just use the well-known fact and move on.

Well-known fact: For any infinite cardinal κ, the number of non-isomorphic graphs on κ vertices is 2^κ.

This is proved in many combinatorics/set theory textbooks. The upper bound is clear. For the lower bound, one standard proof uses the fact that there are 2^κ non-isomorphic linear orders on κ (or similar structures), and these can be encoded into graphs.

Given this fact, there are 2^κ ≥ κ non-isomorphic graphs on κ vertices. We need κ pairwise non-isomorphic connected graphs on κ vertices.

For the connectedness, we can use the H* construction I described (with the 4-layer version that's unambiguously recoverable). Since there are 2^κ non-isomorphic graphs on κ vertices, and the H* construction is injective (for graphs without κ-cliques, or using the 4-layer version for all graphs), there are 2^κ non-isomorphic connected graphs on κ vertices. In particular, there are at least κ of them.

Wait, I need to be more careful with the H* construction. Let me use the 4-layer version which I argued is unambiguously recoverable.

H* construction (4-layer version):
- Vertex set: V(H) × {0, 1, 2, 3}, cardinality 4κ = κ.
- Layer 0: (u,0) ~ (v,0) iff u ~ v in H.
- Layer 1: (u,1) ~ (v,1) for all u,v (clique). (u,1) ~ (u,0) for all u.
- Layer 2: (u,2) ~ (u,1) for all u. No other edges for layer 2.
- Layer 3: (u,3) ~ (u,2) for all u. No other edges for layer 3.

H* is connected (via layer 1 clique).

Recovery from H*:
1. Layer 3 vertices have degree 1 and their unique neighbor has degree 2. (A layer 0 vertex with deg_H = 0 has degree 1, but its neighbor (u,1) has degree κ, not 2. A layer 0 vertex with deg_H = 1 has degree 2, but its neighbors are (u,1) [degree κ] and one H-neighbor [variable degree]. So layer 3 vertices are the degree-1 vertices whose neighbor has degree 2.)

Wait, I need to recheck. (u,3) has degree 1, connected to (u,2). (u,2) has degree 2, connected to (u,1) and (u,3). (u,1) has degree κ (connected to all (v,1) for v≠u [κ-1 vertices], plus (u,0) and (u,2), total = κ+1 = κ). (u,0) has degree deg_H(u) + 1.

A layer 0 vertex (u,0) with deg_H(u) = 0: degree 1, connected to (u,1) which has degree κ. So it's a degree-1 vertex whose neighbor has degree κ, not 2. Different from layer 3.

A layer 0 vertex (u,0) with deg_H(u) = 1: degree 2, connected to (u,1) [degree κ] and one H-neighbor (v,0) [degree deg_H(v)+1]. So it's a degree-2 vertex, but its neighbors have degrees κ and deg_H(v)+1. A layer 2 vertex (u,2) has degree 2, connected to (u,1) [degree κ] and (u,3) [degree 1]. So a layer 2 vertex has a degree-1 neighbor, while a layer 0 vertex with deg_H = 1 has no degree-1 neighbor (unless deg_H(v) = 0, in which case (v,0) has degree 1).

Hmm, so if (u,0) has deg_H(u) = 1 and its H-neighbor v has deg_H(v) = 0, then (u,0) has degree 2 with neighbors (u,1) [degree κ] and (v,0) [degree 1]. This looks like a layer 2 vertex! So we can't distinguish (u,0) from (u,2) in this case.

This is a problem. The 4-layer construction doesn't cleanly separate layers when H has specific degree patterns.

Let me use a longer tail. Use n layers for the tail, where the tail is a path of length n (for finite n). But for any finite n, there might be H-structures that mimic the tail.

Alternative: Use an infinite tail. For each u, attach a ray (one-way infinite path) to (u,1). But that uses κ · ℵ₀ = κ vertices for the tails, plus κ for layer 0 and κ for layer 1, total = κ. But then the tails are all isomorphic (rays), so they don't help distinguish.

Actually, the tails don't need to be distinguishable - they just need to be identifiable as tails. If each (u,1) has a ray attached, then the "tail" structure is: a ray starting from (u,1). The vertex (u,1) is the start of the ray and also part of the clique. So (u,1) is identifiable as a vertex that's in a κ-clique and has a ray attached.

But the issue is: could a layer 0 vertex also have a ray-like structure? If H has a ray starting from u, then (u,0) has a path-like structure in layer 0. But the ray in layer 0 is part of H, while the tail ray is a separate structure. The key difference is that the tail ray is a "pendant" structure (attached to the clique vertex), while the H-ray is part of the H-structure.

This is getting too complicated. Let me use a completely different approach.

Simplest approach: Don't require the graphs to be connected. Instead, use a different method to ensure that disjoint unions are distinguishable.

Revised construction:

Instead of using disjoint unions of connected graphs, use the following:

For each α < κ, let H_α be a graph on κ vertices with a distinguished "marker" - a specific substructure that identifies α.

For example, H_α has a clique of size |α| (the cardinality of α) as a marker. Since different α < κ can have different cardinalities, and the number of distinct cardinalities ≤ κ is at most κ, this gives at most κ different markers. But we need κ pairwise non-isomorphic H_α, and the markers help distinguish them.

Hmm, but different ordinals can have the same cardinality, so the clique size doesn't uniquely identify α.

Let me use a different marker. For each α < κ, let H_α contain a path of length α (as an ordinal). But for infinite α, a "path of length α" is a well-ordered path, which is a specific graph. Different ordinals α give non-isomorphic paths (since the order type is different). But wait, for undirected graphs, a path of length ω and a path of length ω+ω might be isomorphic as graphs (both are countably infinite paths, i.e., double rays or rays).

Actually, a path of length α (as a graph) is a connected graph where each vertex has degree ≤ 2 and the graph is a path. For finite α, this is a finite path. For α = ω, it's a ray. For α = ω + ω, it's... two rays joined at a point? No, a path of length ω + ω would be a ray of length ω + ω, which as a graph is still just a ray (since the graph structure doesn't encode the order type beyond the path structure). Actually, as an undirected graph, a one-way infinite path is a ray regardless of the ordinal length (as long as it's a limit ordinal). So this doesn't distinguish ordinals.

OK, I think the issue is that for infinite structures, graph isomorphism is coarser than order type.

Let me take a step back and think about what we really need.

We need: κ pairwise non-isomorphic graphs on κ vertices, such that their disjoint union is "decomposable" - i.e., from the isomorphism type of the disjoint union, we can recover which graphs are included.

For this, we need the graphs to be "indecomposable" with respect to disjoint union - i.e., each H_α is connected (so it's a connected component of the disjoint union). And we need them to be pairwise non-isomorphic.

So we're back to needing κ pairwise non-isomorphic connected graphs on κ vertices.

Let me try to prove this directly.

Claim: For any infinite cardinal κ, there are 2^κ non-isomorphic connected graphs on κ vertices.

Proof: 
We use the following construction. For each graph H on κ vertices, define H* as a connected graph on κ vertices, such that H ↦ H* is injective up to isomorphism.

Construction: H* has vertex set V(H) ⊔ (V(H) × ω) (disjoint union), where ω = {0, 1, 2, ...}. The cardinality is κ + κ · ℵ₀ = κ.

Edges:
1. H-edges: u ~ v in H* iff u ~ v in H (for u, v ∈ V(H)).
2. Tail: for each u ∈ V(H), (u, 0) ~ u, (u, n) ~ (u, n+1) for all n. So each u has a ray (u, 0) - (u, 1) - (u, 2) - ... attached to it.
3. No other edges.

H* is connected: every vertex is either in V(H) (connected to its ray) or in a ray (connected to the rest of the ray and eventually to V(H)). But wait, if H is disconnected, then H* might still be disconnected - two vertices in different components of H are not connected through H, but their rays are separate too. So H* is connected iff H is connected.

That's a problem. Let me add a universal vertex.

Modified construction: H* has vertex set V(H) ⊔ (V(H) × ω) ⊔ {*}, where * is a new vertex. Cardinality = κ + κ·ℵ₀ + 1 = κ.

Edges:
1. H-edges: u ~ v for u, v ∈ V(H) iff u ~ v in H.
2. * ~ u for all u ∈ V(H) (* is connected to all H-vertices).
3. Tail: (u, 0) ~ u, (u, n) ~ (u, n+1) for all n.
4. No other edges.

H* is connected: * connects all H-vertices, and each ray is attached to an H-vertex.

Recovery: The vertex * has degree κ (connected to all H-vertices). The H-vertices have degree deg_H(u) + 1 + 1 = deg_H(u) + 2 (H-neighbors, plus *, plus (u,0)). The ray vertices (u, n) have degree 2 for n ≥ 1, and (u, 0) has degree 2 (connected to u and (u, 1)).

Wait, (u, 0) is connected to u and (u, 1), so degree 2. (u, n) for n ≥ 1 is connected to (u, n-1) and (u, n+1), so degree 2. Except (u, 0) is connected to u [which is an H-vertex, degree deg_H(u)+2] and (u,1) [degree 2]. So (u,0) has degree 2 with one neighbor of degree 2 and one neighbor of degree deg_H(u)+2.

Hmm, the issue is identifying * and the H-vertices. * has degree κ. An H-vertex u with deg_H(u) = κ has degree κ + 2 = κ, same as *. So we can't distinguish * from high-degree H-vertices.

Let me add more structure to *. Instead of a single vertex, use a clique of size κ as the "hub."

Modified construction: H* has vertex set V(H) ⊔ K ⊔ (V(H) × ω), where K is a set of size κ (the hub clique). Cardinality = κ + κ + κ·ℵ₀ = κ.

Edges:
1. H-edges: u ~ v for u, v ∈ V(H) iff u ~ v in H.
2. Hub: K is a clique. Each k ∈ K is connected to all H-vertices? No, that would make the hub vertices have degree κ + κ = κ, same as before.

Hmm, let me think differently. Let me use a structure that's definitely not present in H.

Construction: H* has vertex set V(H) ⊔ (V(H) × ω) ⊔ {c} ⊔ {d_n : n ∈ ω}.

Edges:
1. H-edges: u ~ v for u, v ∈ V(H) iff u ~ v in H.
2. c ~ u for all u ∈ V(H) (c is a universal vertex for H).
3. Tail: (u, 0) ~ u, (u, n) ~ (u, n+1) for all n.
4. c ~ d_0, d_n ~ d_{n+1} for all n (a ray attached to c).
5. No other edges.

H* is connected (via c).

Now, c has degree κ + 1 = κ (connected to all H-vertices and d_0). An H-vertex u has degree deg_H(u) + 2 (H-neighbors, c, and (u,0)). The ray vertices have degree 2. d_n has degree 2 for n ≥ 1, d_0 has degree 2 (c and d_1).

The vertex c has a ray (d_0, d_1, ...) attached, and also has κ H-neighbors. An H-vertex u has a ray ((u,0), (u,1), ...) attached, and deg_H(u) + 1 other neighbors (H-neighbors and c).

To identify c: c is the unique vertex that has a ray attached AND is connected to all H-vertices. But "connected to all H-vertices" is not a local property.

Hmm, this is still tricky. Let me try a different approach entirely.

Instead of trying to construct connected graphs with a recovery property, let me directly construct the graph G on κ vertices with 2^κ non-isomorphic induced subgraphs, without going through the "disjoint union of connected graphs" approach.

Direct construction:

Let V(G) = κ × κ (cardinality κ). For each α < κ and β < κ, define the edge relation as follows:

(α, β) ~ (α', β') iff one of the following:
1. α = α' and β ~ β' in some fixed graph F_α on κ (the "intra-block" edges).
2. α ≠ α' and β = β' = 0 (the "inter-block" edges: the 0-th vertex of each block forms a clique).

Wait, I already considered this. The issue is that induced subgraphs on arbitrary subsets don't respect block boundaries.

But actually, I only need to find 2^κ subsets that give non-isomorphic induced subgraphs. I don't need ALL subsets to give non-isomorphic ones. So I can restrict to subsets that are unions of blocks: S = A × κ for A ⊆ κ.

For such a subset, G[A × κ] has:
- Intra-block edges: F_α[A × κ ∩ block α] = F_α for α ∈ A.
- Inter-block edges: (α, 0) ~ (α', 0) for α, α' ∈ A, α ≠ α'.

So G[A × κ] is the disjoint union of the F_α (α ∈ A), plus a clique on {(α, 0) : α ∈ A}.

If the F_α are connected, then the connected components of G[A × κ] are... well, the inter-block clique connects all the (α, 0) vertices, which are in different blocks. So if each F_α is connected, then G[A × κ] is connected (all blocks are connected through the (α, 0) clique). So we can't decompose it into blocks.

Hmm. Let me not add inter-block edges. Then G[A × κ] = ⊔_{α ∈ A} F_α, and if the F_α are connected and pairwise non-isomorphic, different A give non-isomorphic graphs.

So the construction is simply: G = disjoint union of κ pairwise non-isomorphic connected graphs on κ vertices each. Total vertices = κ · κ = κ.

And I need to show: there exist κ pairwise non-isomorphic connected graphs on κ vertices.

Let me try to prove this more carefully.

Approach: Show that there are 2^κ non-isomorphic connected graphs on κ vertices.

Sub-claim: There are 2^κ non-isomorphic graphs on κ vertices that are connected and have a "unique hub" - a vertex connected to all others.

A graph with a universal vertex is connected. If H is a graph on κ vertices with a universal vertex u, then H is determined (up to isomorphism) by the induced subgraph on V(H) \ {u}, which is an arbitrary graph on κ vertices (since κ - 1 = κ). 

But different graphs on κ vertices can give isomorphic graphs with universal vertices, because the universal vertex might not be unique.

If H has a unique universal vertex, then H is determined by H \ {u} (the induced subgraph on non-universal vertices). Two such graphs H₁, H₂ are isomorphic iff H₁ \ {u₁} ≅ H₂ \ {u₂}.

When is the universal vertex unique? If H \ {u} has no universal vertex, then u is the unique universal vertex of H. So if we start with a graph F on κ vertices with no universal vertex, and add a universal vertex u, we get a graph H with a unique universal vertex, and H is determined by F.

But adding a vertex gives κ + 1 = κ vertices, which is fine. But we need to be careful: H has κ vertices (F has κ - 1 vertices plus u). Since κ - 1 = κ for infinite κ, F has κ vertices and H has κ + 1 = κ vertices. Wait, no: if F has κ vertices, then H has κ + 1 vertices = κ vertices (for infinite κ). But we need H to have exactly κ vertices. Since κ + 1 = κ, this is fine in terms of cardinality, but we need to actually construct H on a set of size κ.

Let me be more precise. Let F be a graph on κ vertices with no universal vertex. Define H on κ vertices as follows: take V(F) (which has κ elements) and add one more vertex u. But |V(F)| + 1 = κ + 1 = κ, so we can biject V(F) ∪ {u} with κ. H has edges: all edges of F, plus u ~ v for all v ∈ V(F). H is connected (u connects to everything). u is the unique universal vertex (since F has no universal vertex). H is determined by F up to isomorphism.

So the number of non-isomorphic such H is equal to the number of non-isomorphic F on κ vertices with no universal vertex.

How many non-isomorphic graphs on κ vertices have no universal vertex? At least 2^κ / (something). Actually, the number of graphs on κ vertices with a universal vertex is at most κ · 2^κ = 2^κ (choose the universal vertex, then the rest is arbitrary). So the number without a universal vertex is 2^κ - 2^κ, which could be 0. That's not useful.

Let me think about this differently. The number of isomorphism classes of graphs on κ vertices with a universal vertex: each such graph is determined by the universal vertex (up to automorphism) and the graph on the remaining κ vertices. The number of isomorphism classes is at most (number of isomorphism classes of graphs on κ vertices) = 2^κ. So the number without a universal vertex is at least 2^κ - 2^κ, which is not helpful.

But actually, the number of isomorphism classes of graphs with a universal vertex is at most the number of isomorphism classes of graphs on κ vertices (since each such graph is determined by its non-universal part, which is a graph on κ vertices). So the number of isomorphism classes with a universal vertex is ≤ 2^κ. And the total is 2^κ. So the number without is ≥ 2^κ - 2^κ, which is ≥ 0. Not helpful.

But we can be more precise. The map F ↦ H (adding a universal vertex) is a function from isomorphism classes of graphs on κ vertices to isomorphism classes of graphs on κ vertices with a universal vertex. This map is surjective (every graph with a universal vertex comes from some F). Is it injective? Only if the universal vertex is unique. 

If F has no universal vertex, then H has a unique universal vertex, and the map is injective on such F. So the number of isomorphism classes of H with a unique universal vertex is equal to the number of isomorphism classes of F with no universal vertex.

Now, I claim there are 2^κ non-isomorphic graphs on κ vertices with no universal vertex. 

Proof: Consider graphs on κ vertices with maximum degree < κ (i.e., every vertex has degree < κ). Such graphs have no universal vertex (a universal vertex has degree κ). The number of non-isomorphic such graphs is 2^κ.

Why 2^κ? For κ = ℵ₀: graphs with bounded degree. There are 2^(ℵ₀) non-isomorphic such graphs (e.g., 2^(ℵ₀) non-isomorphic graphs of maximum degree 3, by a classical result).

For general κ: graphs with maximum degree < κ. For regular κ, the number of such graphs on κ vertices is... let me think. A graph with max degree < κ is determined by the neighborhoods, each of size < κ. The number of such graphs is at most κ^(κ·(<κ)) = ... hmm.

Actually, let me just use a specific family. For each S ⊆ κ, define a graph G_S on κ × {0, 1} (cardinality 2κ = κ) as follows:
- (α, 0) ~ (β, 0) for all α, β (clique on layer 0).
- (α, 1) ~ (α, 0) for all α (matching).
- (α, 1) ~ (β, 1) iff α = β and ... no, let me think.

Actually, here's a cleaner family. For each S ⊆ κ, define G_S on vertex set κ:
- α ~ β (α < β) iff β = α + 1 and α ∈ S.

This is a graph where edges form a subset of the path α - (α+1). The graph is a union of paths (some edges present, some absent). The isomorphism type depends on the pattern of S.

But for infinite κ, many different S give isomorphic graphs (e.g., shifting S by 1 gives an isomorphic graph if κ is a limit ordinal). So this doesn't give 2^κ non-isomorphic graphs.

Let me try a different family. For each S ⊆ κ, define G_S on vertex set κ × κ (cardinality κ):
- (α, β) ~ (α, γ) for all β, γ (each "row" α is a clique).
- (α, 0) ~ (α', 0) iff α, α' ∈ S (the "first column" restricted to S is a clique).

Hmm, this is getting complicated and I'm not sure it gives 2^κ non-isomorphic graphs.

Let me try yet another approach. I'll use the fact that there are 2^κ non-isomorphic linear orders on κ, and encode linear orders into graphs.

Fact: For any infinite cardinal κ, there are 2^κ non-isomorphic linear orders on κ.

This is well-known. For κ = ℵ₀, there are 2^(ℵ₀) non-isomorphic countable linear orders. For general κ, similarly.

Encoding: Given a linear order (L, <), define a graph G_L on L × {0, 1}:
- (x, 0) ~ (y, 0) for all x, y (clique).
- (x, 1) ~ (x, 0) for all x (matching).
- (x, 1) ~ (y, 1) iff x < y or y < x (i.e., all distinct pairs - this makes layer 1 a clique too). 

No, that doesn't encode the order. Let me think.

Encoding linear orders into graphs: Given (L, <), define G_L on L × {0, 1, 2}:
- (x, 0) ~ (y, 0) for all x, y (clique).
- (x, 1) ~ (x, 0) for all x.
- (x, 2) ~ (x, 1) for all x.
- (x, 1) ~ (y, 2) iff x < y (i.e., (x,1) is connected to (y,2) when x < y).
- No other edges.

Hmm, this might work but the recovery is complicated. Let me use a known encoding.

Actually, there's a standard way to encode any relational structure into a graph (using gadgets). But for infinite structures, this might use more vertices.

Let me try a more direct approach.

Standard result: The number of non-isomorphic graphs on κ vertices is 2^κ. (This is truly standard - see e.g., Truss or other set theory texts.)

Given this, there are 2^κ ≥ κ non-isomorphic graphs on κ vertices. Now, I need κ of them to be connected.

Claim: At least 2^κ of the 2^κ non-isomorphic graphs on κ vertices are connected.

Proof: The number of disconnected graphs on κ vertices is at most Σ_{λ < κ, λ infinite} (number of graphs on λ vertices) × (number of graphs on κ vertices) × C(κ, λ) + (number of graphs on finite vertices) × ...

Actually, a disconnected graph on κ vertices has a connected component of size < κ (for infinite κ, if all components have size κ, there can be at most one, making it connected). Wait, no: a disconnected graph on κ vertices could have two components each of size κ (if κ = κ + κ, which is true for infinite κ). So a disconnected graph on κ vertices could have all components of size κ, with at least 2 components.

Hmm, so the counting is more subtle. Let me think about it differently.

The number of isomorphism classes of disconnected graphs on κ vertices: a disconnected graph is a disjoint union of at least 2 connected graphs. The number of such disjoint unions is bounded by... the number of multisets of isomorphism classes of connected graphs on ≤ κ vertices, with total size κ. This is hard to bound directly.

Alternative approach: Instead of counting, directly construct 2^κ non-isomorphic connected graphs.

Construction: For each graph H on κ vertices, define C(H) as a connected graph on κ vertices, such that H₁ ≇ H₂ implies C(H₁) ≇ C(H₂).

I'll use the following construction:

C(H) has vertex set V(H) × {0, 1} ∪ {*}.
- |V(H) × {0,1}| + 1 = 2κ + 1 = κ. Good.
- Layer 0: (u, 0) ~ (v, 0) iff u ~ v in H.
- Layer 1: (u, 1) ~ (v, 1) iff u ~ v in H. (Copy of H)
- * ~ (u, 0) for all u. (* is universal for layer 0)
- * ~ (u, 1) for all u. (* is universal for layer 1)
- (u, 0) ~ (u, 1) for all u. (Matching)
- No other edges between layers.

C(H) is connected (* connects to everything).

Now, * has degree 2κ = κ. Each (u, 0) has degree deg_H(u) + κ + 1 = κ (H-neighbors, all (v,1) via *, and (u,1)). Wait, (u,0) is connected to H-neighbors in layer 0, to * (which connects to all), and to (u,1). So degree = deg_H(u) + 1 + 1 = deg_H(u) + 2. No wait, * is a single vertex, (u,0) is connected to * and (u,1) and H-neighbors. So degree = deg_H(u) + 2.

But (u, 0) is NOT connected to (v, 1) for v ≠ u (no cross-layer edges except matching). Let me re-read my construction. I said:
- * ~ (u, 0) for all u.
- * ~ (u, 1) for all u.
- (u, 0) ~ (u, 1) for all u.
- No other edges between layers (i.e., (u,0) ~ (v,1) only if u = v).

So (u, 0) is connected to: H-neighbors in layer 0, *, and (u, 1). Degree = deg_H(u) + 2.
(u, 1) is connected to: H-neighbors in layer 1, *, and (u, 0). Degree = deg_H(u) + 2.
* is connected to: all (u, 0) and all (u, 1). Degree = 2κ = κ.

So * is the unique vertex of degree κ (assuming all H-degrees are < κ). If H has a vertex of degree κ, then (u, 0) and (u, 1) also have degree κ + 2 = κ, same as *.

To avoid this issue, restrict to graphs H with maximum degree < κ. There are 2^κ non-isomorphic such graphs (I'll argue this below). For such H, * is the unique degree-κ vertex.

Given that * is identifiable, we can remove * and get the graph on V(H) × {0, 1}, which is two copies of H with a matching. From this, we can recover H (the two layers are identifiable because... hmm, actually they're symmetric - there's an automorphism swapping layer 0 and layer 1).

The symmetry between layers means we can recover H up to isomorphism (which is all we need). Specifically, the graph on V(H) × {0, 1} with the matching and two copies of H is determined by H up to isomorphism. And from this graph, we can recover H: the matching edges (u,0)-(u,1) partition the vertices into pairs, and each pair has the same H-neighborhood structure. The quotient (identifying matched pairs) gives H.

More formally: in C(H) \ {*} (removing *), the matching edges (u,0)-(u,1) are the edges between the two layers. The graph induced on each layer is H. The matching is a perfect matching between the layers. An isomorphism C(H₁) → C(H₂) must map * to * (unique degree-κ vertex), and then map the remaining graph to the remaining graph. The remaining graph has a unique perfect matching between two copies (well, the matching might not be unique, but the structure is determined by H).

Actually, the perfect matching might not be unique. If H has automorphisms, there could be other matchings. But the key point is that the isomorphism type of C(H) \ {*} determines the isomorphism type of H. 

Let me argue this more carefully. C(H) \ {*} is a graph on V(H) × {0, 1} with:
- Two copies of H (layers 0 and 1).
- Matching (u,0) - (u,1).

This graph is the "double" of H with a matching. I claim that H can be recovered up to isomorphism.

Consider the relation on vertices of C(H) \ {*}: u ≡ v iff u and v are matched (i.e., {u, v} is a matching edge). The matching edges can be identified as follows: (u, 0) and (u, 1) are twins in the graph C(H) \ {*} restricted to non-* vertices? No, they're not twins because they have different neighborhoods within their layers.

Hmm, let me think about this differently. In C(H) \ {*}, the vertex (u, 0) has neighbors: {(v, 0) : v ~ u in H} ∪ {(u, 1)}. The vertex (u, 1) has neighbors: {(v, 1) : v ~ u in H} ∪ {(u, 0)}. 

The matching edge (u,0)-(u,1) is special because (u,0) and (u,1) have "corresponding" neighborhoods. Specifically, (u,0) is connected to (u,1), and (u,1) is connected to (u,0), and the H-neighborhoods are in different layers.

Actually, I think the cleanest way to see that H is recoverable is: the matching edges are exactly the edges {x, y} such that x and y have no common neighbors in C(H) \ {*} (other than possibly through *). Wait, * is removed, so let me check.

In C(H) \ {*}, common neighbors of (u, 0) and (u, 1): 
- (v, 0) is a neighbor of (u, 0) iff v ~ u in H. Is (v, 0) a neighbor of (u, 1)? Only if v = u (matching), but (v, 0) ≠ (u, 0) since v ~ u means v ≠ u. So no.
- (v, 1) is a neighbor of (u, 1) iff v ~ u in H. Is (v, 1) a neighbor of (u, 0)? Only if v = u (matching), but v ≠ u. So no.
- (u, 0) is a neighbor of (u, 1) [matching] and vice versa, but we're looking for common neighbors, not the vertices themselves.

So (u, 0) and (u, 1) have NO common neighbors in C(H) \ {*} (when * is removed). 

What about two non-matched vertices? (u, 0) and (v, 0) with u ≠ v: common neighbors are {(w, 0) : w ~ u, w ~ v in H}. This could be non-empty.
(u, 0) and (v, 1) with u ≠ v: common neighbors: (w, 0) is a neighbor of (u,0) iff w~u, and of (v,1) iff w=v (matching). So (v,0) is a common neighbor iff v~u in H. (w,1) is a neighbor of (v,1) iff w~v, and of (u,0) iff w=u (matching). So (u,1) is a common neighbor iff u~v in H. So common neighbors of (u,0) and (v,1) (u≠v) are {(v,0), (u,1)} ∩ {w : w~u or w~v in H}... more precisely, (v,0) is a common neighbor iff v~u in H, and (u,1) is a common neighbor iff u~v in H. So if u~v in H, they have 2 common neighbors; if not, 0.

So in C(H) \ {*}, two matched vertices (u,0) and (u,1) have 0 common neighbors, and two non-matched vertices (u,0) and (v,1) (u≠v) have 0 common neighbors iff u ≁ v in H, and 2 common neighbors iff u ~ v in H.

Hmm, so "0 common neighbors" doesn't uniquely identify matching edges. A non-matched pair (u,0), (v,1) with u ≁ v in H also has 0 common neighbors.

So this approach doesn't cleanly identify the matching. Let me modify the construction.

OK, I think I'm overcomplicating this. Let me use a much simpler approach to get connected graphs.

Simplest construction of connected graphs from arbitrary graphs:

Given a graph H on κ vertices (with max degree < κ), define C(H) on κ vertices as follows:
- Vertex set: V(H) ∪ {*} (where * is a new vertex). |V(H)| + 1 = κ + 1 = κ.
- Edges: all edges of H, plus * ~ v for all v ∈ V(H).
- C(H) is connected (* is universal).
- * has degree κ (connected to all of V(H)).
- Each v ∈ V(H) has degree deg_H(v) + 1 < κ + 1 = κ (since deg_H(v) < κ).
- So * is the unique vertex of degree κ.
- Removing * gives H.
- So C(H₁) ≅ C(H₂) iff H₁ ≅ H₂.

This is much simpler! The key requirement is that H has max degree < κ, so that * is the unique degree-κ vertex.

Now, are there 2^κ non-isomorphic graphs on κ vertices with max degree < κ?

For κ = ℵ₀: graphs with finite max degree. There are 2^(ℵ₀) non-isomorphic such graphs (e.g., 2^(ℵ₀) non-isomorphic 3-regular graphs, or 2^(ℵ₀) non-isomorphic paths with varying attachments).

For general κ: graphs with max degree < κ. 

Upper bound on number of such graphs: each vertex has < κ neighbors, so the graph is determined by κ many choices of < κ-sized subsets. The number is at most (κ^(<κ))^κ = κ^(κ·(<κ)) = κ^(<κ·κ) = ... hmm, this depends on κ.

For regular κ: κ^(<κ) could be > κ. The number of graphs with max degree < κ is at most (number of ways to choose < κ neighbors for each of κ vertices) = (κ^(<κ))^κ. If κ^(<κ) = κ, this is κ^κ = 2^κ. If κ^(<κ) > κ, this could be larger than 2^κ, but the total number of graphs is 2^κ, so it's at most 2^κ.

For the lower bound: we need to construct 2^κ non-isomorphic graphs on κ vertices with max degree < κ.

Construction: For each S ⊆ κ, define G_S on κ × {0, 1} (cardinality 2κ = κ):
- (α, 0) ~ (β, 0) for β = α + 1 (path on layer 0).
- (α, 1) ~ (α, 0) for all α (matching).
- (α, 1) ~ (β, 1) for β = α + 1 iff α ∈ S (path on layer 1, with edges depending on S).

Max degree: (α, 0) has degree ≤ 3 (two path neighbors in layer 0, plus (α, 1)). (α, 1) has degree ≤ 3 (one matching edge, plus 0-2 path edges in layer 1). So max degree ≤ 3 < κ for infinite κ.

Now, are different S giving non-isomorphic G_S? The graph G_S is a "ladder" graph (two paths with rungs), where some rungs of the second path are missing based on S. The isomorphism type depends on the pattern of S.

But for infinite κ, the "path" on layer 0 is a path of length κ (which is a specific graph), and the pattern of S on layer 1 determines which edges are present. Two different S, S' might give isomorphic graphs if there's a "shift" automorphism.

To avoid this, we can "anchor" the path. For example, make the first vertex of layer 0 have a special structure (like a pendant vertex).

Modified construction: For each S ⊆ κ, define G_S on κ × {0, 1} ∪ {p}:
- (α, 0) ~ (β, 0) for β = α + 1 (path on layer 0).
- (α, 1) ~ (α, 0) for all α (matching).
- (α, 1) ~ (β, 1) for β = α + 1 iff α ∈ S.
- p ~ (0, 0) (pendant vertex attached to the start of the path).

Now the path is "anchored" at (0, 0) by the pendant p. An isomorphism must map p to p (the unique degree-1 vertex whose neighbor has degree 3... well, (0, 0) has degree 3: p, (1, 0), (0, 1)). Other degree-1 vertices: (α, 1) might have degree 1 if α ∉ S and α + 1 ∉ S (no path edges in layer 1) - then (α, 1) has degree 1 (just the matching edge to (α, 0)). And (α, 1)'s neighbor (α, 0) has degree 2 or 3.

Hmm, this is getting complicated and I'm not sure the anchoring works perfectly. But the general idea is sound: we can construct 2^κ non-isomorphic graphs of bounded degree on κ vertices.

Actually, let me use a cleaner construction. 

For each S ⊆ κ, define G_S on vertex set κ × {0, 1}:
- (α, 0) ~ (α+1, 0) for all α < κ (path on layer 0, indexed by ordinals < κ).
- (α, 0) ~ (α, 1) for all α (matching).
- No other edges.

Wait, this doesn't use S. Let me incorporate S.

For each S ⊆ κ, define G_S on vertex set κ × {0, 1, 2}:
- (α, 0) ~ (α+1, 0) for all α (path on layer 0).
- (α, 0) ~ (α, 1) for all α (matching between layers 0 and 1).
- (α, 1) ~ (α, 2) for all α (matching between layers 1 and 2).
- (α, 2) ~ (β, 2) for β = α + 1 iff α ∈ S (path on layer 2, edges determined by S).

Max degree: (α, 0) has degree ≤ 3. (α, 1) has degree 2. (α, 2) has degree ≤ 3.

The graph has a "spine" (layer 0 path with layer 1 vertices as "rungs"), and layer 2 has a path whose edges are determined by S.

The isomorphism type: the spine is a path of length κ (on layer 0), which is a specific graph. Layer 1 vertices are degree-2 vertices attached to the spine. Layer 2 vertices are attached to layer 1 and have path edges determined by S.

An isomorphism G_S → G_S' must preserve the spine (the unique path of length κ with specific degree-3 vertices at each position... actually, all layer 0 vertices have degree 2 or 3, depending on whether they're at the "end" of the path or not).

Hmm, for a path of length κ (κ infinite), there's no "end" - it's a one-way infinite path (ray) or a two-way infinite path (double ray) or a longer path. For κ = ω, it's a ray. For κ = ω₁, it's a path of length ω₁, which as a graph is... a well-ordered path, which is a specific graph.

Actually, for a path indexed by ordinals < κ, the graph structure is: vertex α is connected to vertex α+1. For κ = ω, this is a ray. For κ = ω + ω, this is two consecutive rays, which as a graph is still a ray (since the graph doesn't distinguish the "break" at ω). Wait, no: vertex ω is connected to vertex ω+1, and vertex ω-1 doesn't exist (ω is a limit ordinal). So the path has vertex ω connected only to ω+1 (and to (ω, 1) via matching). So vertex (ω, 0) has degree 2 (connected to (ω+1, 0) and (ω, 1)), while vertex (n, 0) for finite n > 0 has degree 3 (connected to (n-1, 0), (n+1, 0), and (n, 1)). And vertex (0, 0) has degree 2 (connected to (1, 0) and (0, 1)).

So the path on layer 0 has "breakpoints" at limit ordinals, where the degree drops from 3 to 2. These breakpoints are graph-theoretically identifiable. So the spine is not just a path - it has a specific structure determined by the ordinal structure of κ.

For two different ordinals κ, the spine would be different. But we're fixing κ, so the spine is the same for all S. The question is whether different S give non-isomorphic G_S.

An isomorphism G_S → G_S' must map the spine to itself (since the spine is the unique maximal path with the specific degree pattern). Actually, the spine might have automorphisms. For κ = ω (ray), the ray has no non-trivial automorphisms (it's rigid). For κ = ω + ω, the path has a "break" at ω, and the automorphism group is trivial. In general, a well-ordered path is rigid (no non-trivial automorphisms) because the ordinal structure is encoded in the degree pattern.

Wait, is a well-ordered path rigid? Consider the path on ω: 0 - 1 - 2 - .... This is a ray, and it's rigid (the endpoint 0 is the unique degree-1 vertex, and the rest follows). For the path on ω + ω: 0 - 1 - ... - ω - (ω+1) - .... Vertex 0 has degree 1, vertex ω has degree 1 (connected only to ω+1, since ω-1 doesn't exist). So there are two degree-1 vertices: 0 and ω. An automorphism could swap the two rays... but the first ray (0, 1, 2, ...) starts at 0, and the second ray (ω, ω+1, ...) starts at ω. Both are rays. An automorphism mapping 0 to ω would map the first ray to the second, which is fine. So the path on ω + ω is NOT rigid.

Hmm, so the spine might have automorphisms. This complicates things.

OK, I think I need to step back and use a cleaner, more abstract approach.

Let me use the following well-known result:

Theorem: For any infinite cardinal κ, there exist 2^κ non-isomorphic graphs on κ vertices.

This is standard. The proof typically goes: 
- Upper bound: 2^κ labeled graphs.
- Lower bound: Construct 2^κ non-isomorphic graphs. One way: for each subset S of κ, construct a graph G_S such that S can be recovered from G_S up to isomorphism. This can be done using a "rigid" base graph and encoding S into it.

Given this theorem, there are 2^κ non-isomorphic graphs on κ vertices. Now:

Theorem: For any infinite cardinal κ, there exist 2^κ non-isomorphic connected graphs on κ vertices.

Proof: Using the C(H) construction (add a universal vertex to a max-degree-<κ graph H), we get an injection from isomorphism classes of max-degree-<κ graphs to isomorphism classes of connected graphs. We need 2^κ non-isomorphic max-degree-<κ graphs on κ vertices.

For the existence of 2^κ non-isomorphic max-degree-<κ graphs on κ vertices: 

Consider the following. For each S ⊆ κ, define a graph G_S on κ vertices as a graph of max degree ≤ 2 (a union of paths and cycles) that encodes S. 

Actually, here's a clean construction. For each binary sequence s: κ → {0, 1}, define G_s on vertex set κ × {0, 1}:

- (α, 0) ~ (α, 1) for all α (perfect matching).
- (α, 0) ~ (α+1, 0) for all α with s(α) = 1 (path edges on layer 0, determined by s).
- No other edges.

Max degree: (α, 0) has degree 1 + s(α) + s(α-1) ≤ 3 (matching, plus path edges). (α, 1) has degree 1. So max degree ≤ 3 < κ.

Now, G_s is a graph where layer 1 is an independent set (all degree 1, connected to layer 0 via matching), and layer 0 is a subgraph of the path on κ (with edges determined by s).

The isomorphism type of G_s: the degree-1 vertices connected to degree-≥2 vertices are the layer 1 vertices. Wait, all layer 1 vertices have degree 1. Their neighbors (layer 0 vertices) have degree 1 + (number of path edges incident), which is 1, 2, or 3.

A layer 0 vertex (α, 0) with no path edges (s(α-1) = 0 and s(α) = 0, where we define s(-1) = 0 for α = 0... hmm, this is getting into ordinal arithmetic) has degree 1 (just the matching). A layer 0 vertex with one path edge has degree 2. With two path edges, degree 3.

So the degree-1 vertices in G_s include all of layer 1 and some of layer 0 (those with no path edges). This makes it hard to distinguish layers.

Let me modify: make layer 1 vertices have degree 2 instead of 1.

For each s: κ → {0, 1}, define G_s on κ × {0, 1, 2}:
- (α, 0) ~ (α+1, 0) for all α (full path on layer 0).
- (α, 0) ~ (α, 1) for all α (matching).
- (α, 1) ~ (α, 2) for all α (matching).
- (α, 2) ~ (α+1, 2) iff s(α) = 1 (path on layer 2, determined by s).

Max degree: (α, 0) has degree 2 + 1 = 3 (two path
