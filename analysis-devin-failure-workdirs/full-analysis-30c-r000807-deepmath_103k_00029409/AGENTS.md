# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Calculate the limit: \( \lim_{x\to0} \sum_{n=1}^\infty \frac{\sin x}{4+n^4x^4} \)       — 题目文本
#   Okay, so I need to find the limit as x approaches 0 of the sum from n=1 to infinity of sin(x) divided by (4 + n^4x^4). Hmm, let me start by understanding the problem. It's a limit of an infinite series as x approaches 0. The terms of the series are sin(x)/(4 + n^4x^4). 

First, let me note that when x approaches 0, sin(x) is approximately x. So maybe I can approximate sin(x) with x for small x. That might simplify things a bit. So replacing sin(x) with x, the term becomes x/(4 + n^4x^4). 

But wait, since x is approaching 0, I need to see how each term in the series behaves as x approaches 0. Let's look at a general term: for each fixed n, as x approaches 0, the denominator 4 + n^4x^4 approaches 4. So each term approaches sin(x)/4. But if I sum this over all n from 1 to infinity, sin(x)/4 summed infinitely would diverge because it's just adding a constant term infinitely. But that seems contradictory because the original sum might converge. So maybe my initial thought is wrong.

Wait, but if x is approaching 0, even though each term sin(x)/(4 + n^4x^4) approaches sin(x)/4, the sum might not necessarily diverge because as x approaches 0, sin(x) also approaches 0. So maybe the sum is something like a small number times an infinite series. Hmm, indeterminate form? Maybe 0 times infinity? So I need to analyze this more carefully.

Alternatively, maybe I can switch the limit and the summation. If that's allowed, then the limit would be the sum of the limits. So, interchanging limit and summation would give sum_{n=1}^\infty [lim_{x->0} sin(x)/(4 + n^4x^4)]. But lim_{x->0} sin(x)/(4 + n^4x^4) = lim_{x->0} sin(x)/4 = 0, since n^4x^4 goes to 0. Therefore, each term's limit is 0, so the sum would be 0 + 0 + 0 + ... = 0. So would the limit be 0?

But I need to be careful here because interchanging limits and infinite sums requires uniform convergence or some other condition. Maybe I need to justify that interchange. Alternatively, perhaps there's another approach.

Alternatively, think of the sum as an approximation of an integral when x is small. Since n is going to infinity, and x is approaching 0, maybe setting nx = t or something. Let me try a substitution. Let’s let t = n x. Then, as x approaches 0, for fixed t, n would be t/x, which goes to infinity. But since n is an integer, maybe we can approximate the sum by an integral over t.

Wait, this is similar to converting a Riemann sum into an integral. Let me think. If we set t_n = n x, then when x is small, the spacing between t_n and t_{n+1} is x. So the sum over n multiplied by x can approximate an integral over t. But in our case, the term is sin(x)/(4 + (t_n)^4). So the sum is sin(x) * sum_{n=1}^\infty 1/(4 + (n x)^4). If x is approaching 0, sin(x) ~ x, so the sum is approximately x * sum_{n=1}^\infty 1/(4 + (n x)^4). Then, if we let x approach 0, the sum can be approximated by x * sum_{n=1}^\infty 1/(4 + (n x)^4) ≈ x * integral_{t=0}^\infty 1/(4 + t^4) dt. Because as x approaches 0, the sum becomes a Riemann sum for the integral, with step size x.

Therefore, the limit would be lim_{x->0} x * integral_{t=0}^\infty 1/(4 + t^4) dt. But wait, integral_{t=0}^\infty 1/(4 + t^4) dt is a constant, so multiplying by x would give 0. Therefore, the limit is 0. But is that correct?

Wait, hold on. Let's check. The original expression is sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4). If we approximate sin(x) ~ x, then it's x * sum_{n=1}^\infty 1/(4 + n^4 x^4). Then, we can make substitution t = n x, so n = t / x. Then, the sum over n is sum_{n=1}^\infty 1/(4 + t^4) * x, since Δt = x. Therefore, the sum becomes approximately integral_{t=0}^\infty 1/(4 + t^4) dt. So the total expression becomes x * [integral_{t=0}^\infty 1/(4 + t^4) dt] / x = integral_{t=0}^\infty 1/(4 + t^4) dt. Wait, but that contradicts the previous conclusion. Wait, no, maybe substitution is different.

Wait, when we set t = n x, then as x approaches 0, n has to go to infinity to keep t finite. But in the sum, n starts from 1, so t starts from x. So as x approaches 0, the lower limit of t approaches 0. So the sum sum_{n=1}^\infty x/(4 + (n x)^4) is a Riemann sum for the integral from t=0 to t=infty of 1/(4 + t^4) dt. Because each term is x * f(n x), where f(t) = 1/(4 + t^4). So the sum is approximately the integral of f(t) from 0 to infinity as x approaches 0.

Therefore, the sum sum_{n=1}^\infty 1/(4 + (n x)^4) ≈ (1/x) * integral_{0}^\infty 1/(4 + t^4) dt. Then, multiplying by sin(x) ~ x, we get x * (1/x) * integral ... = integral. Therefore, the limit would be equal to integral_{0}^\infty 1/(4 + t^4) dt.

Wait, but this contradicts my previous thought. Wait, so perhaps the limit is actually equal to that integral? Let me check again.

Original expression: lim_{x->0} sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4).

Approximate sin(x) as x, so expression becomes x * sum_{n=1}^\infty 1/(4 + n^4 x^4).

Set t_n = n x, so t_n = x, 2x, 3x, ... Then the sum sum_{n=1}^\infty x/(4 + t_n^4) is a Riemann sum for the integral from t=0 to t=infty of 1/(4 + t^4) dt. Because each term is (t_{n+1} - t_n) * f(t_n), where the step size is x. So as x approaches 0, the Riemann sum approaches the integral. Therefore, the sum sum_{n=1}^\infty x/(4 + (n x)^4) approaches integral_{0}^\infty 1/(4 + t^4) dt. Therefore, the original expression, which is approximately x * sum ... becomes x * (1/x) * integral ... = integral.

But wait, no. Wait, the sum is sum_{n=1}^\infty x/(4 + (n x)^4). So each term is x * [1/(4 + (n x)^4)]. So as x approaches 0, this sum approaches the integral from t=0 to infinity of 1/(4 + t^4) dt. Therefore, the entire expression sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4) is approximately x * [ (1/x) * integral ... ] = integral. Therefore, the limit is the value of the integral.

Therefore, the answer should be integral_{0}^\infty 1/(4 + t^4) dt. Now, need to compute that integral.

Wait, but I need to verify this reasoning. Because if I have sum_{n=1}^\infty x/(4 + (n x)^4), and as x approaches 0, this becomes the integral from t=0 to infinity of 1/(4 + t^4) dt. So the sum is equal to (1/x) sum_{n=1}^\infty [x / (4 + (n x)^4)] which is the Riemann sum for the integral. Therefore, sum_{n=1}^\infty x / (4 + (n x)^4) ≈ integral_{0}^\infty 1/(4 + t^4) dt. Therefore, multiplying by sin(x) ~ x, the original expression is approximately x * integral, but wait, no. Wait, the original expression is sin(x) times the sum. So if the sum is approximately (1/x) integral, then sin(x) ~ x, so sin(x) * sum ~ x * (1/x) * integral = integral. Therefore, the limit is equal to the integral.

Therefore, the answer is the integral from 0 to infinity of 1/(4 + t^4) dt. Now, let's compute that integral.

To compute integral_{0}^\infty dt / (4 + t^4). Let me recall that integrals of the form ∫_{0}^\infty dx/(x^n + a^n) can be evaluated using beta or gamma functions. Alternatively, use substitution.

Let me try substitution. Let u = t^4 / 4. Then t = (4u)^{1/4}, dt = (4^{1/4}/4) u^{-3/4} du. Hmm, not sure if that helps.

Alternatively, use partial fractions or contour integration. Wait, maybe a standard integral formula.

Recall that ∫_{0}^\infty dx/(x^4 + a^4) = (π)/(2 a^3 sqrt(2)) ). Wait, not sure. Let me check.

Alternatively, use substitution. Let t = sqrt(2) u. Then, substitute t = sqrt(2) u, dt = sqrt(2) du. Then, integral becomes ∫_{0}^\infty sqrt(2) du / (4 + (sqrt(2) u)^4) = sqrt(2) ∫_{0}^\infty du / (4 + 4 u^4) = sqrt(2)/4 ∫_{0}^\infty du/(1 + u^4). 

Ah, so the integral becomes sqrt(2)/4 times ∫_{0}^\infty du/(1 + u^4). Now, I know that ∫_{0}^\infty du/(1 + u^4) = π/(2 sqrt(2)). Let me confirm that.

Yes, the integral ∫_{0}^\infty dx/(1 + x^4) can be computed using beta function. Let me recall that ∫_{0}^\infty x^{k - 1}/(1 + x^n) dx = (π/n)/sin(π k/n). For our case, n=4, k=1. So integral is (π/4)/sin(π/4) = (π/4)/(sqrt(2)/2) = π/(4) * 2/sqrt(2) = π/(2 sqrt(2)). Therefore, ∫_{0}^\infty dx/(1 + x^4) = π/(2 sqrt(2)).

Therefore, coming back, our integral was sqrt(2)/4 * π/(2 sqrt(2)) = (sqrt(2) * π)/(8 sqrt(2)) ) = π/8. 

Wait, let me check again:

Original substitution: t = sqrt(2) u. Then, t^4 = (sqrt(2))^4 u^4 = 4 u^4. So denominator becomes 4 + t^4 = 4 + 4 u^4 = 4(1 + u^4). Then, integral is ∫_{0}^\infty dt/(4 + t^4) = ∫_{0}^\infty sqrt(2) du / [4(1 + u^4)] = sqrt(2)/4 ∫_{0}^\infty du/(1 + u^4) = sqrt(2)/4 * π/(2 sqrt(2)) = (sqrt(2) * π)/(8 sqrt(2)) = π/8. 

Yes, that's correct. Therefore, the integral ∫_{0}^\infty dt/(4 + t^4) = π/8. Therefore, the limit is π/8. 

But wait, let me confirm once again the steps:

1. Original limit: lim_{x→0} sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4).

2. Approximated sin(x) ~ x.

3. Converted the sum into a Riemann sum by substituting t = n x, leading to the integral ∫_{0}^\infty 1/(4 + t^4) dt.

4. Calculated the integral and found it to be π/8.

Therefore, the answer should be π/8. But before finalizing, let me check if interchanging the sum and the limit is valid here.

Alternatively, can we use the Dominated Convergence Theorem for series? For each fixed n, the term sin(x)/(4 + n^4 x^4) approaches 0 as x approaches 0. If we can dominate the terms by something summable, then by the Dominated Convergence Theorem, the limit can be interchanged with the sum.

But as x approaches 0, sin(x) ~ x, so |sin(x)/(4 + n^4 x^4)| ≤ x/(4 + n^4 x^4). Let me see if this is dominated by something summable. For x near 0, n^4 x^4 can be small or large depending on n.

But for each fixed x, when n is large enough such that n^4 x^4 ≥ 1, then 4 + n^4 x^4 ≥ n^4 x^4, so term is ≤ x/(n^4 x^4) = 1/(n^4 x^3). Wait, but as x approaches 0, 1/(n^4 x^3) becomes large for fixed n. So this approach might not work. Therefore, maybe Dominated Convergence is not directly applicable here.

Alternatively, use comparison. Let me split the sum into two parts: n ≤ N and n > N, where N is chosen such that n^4 x^4 is small for n ≤ N and x near 0.

But this seems vague. Alternatively, use the integral test. Compare sum_{n=1}^\infty 1/(4 + n^4 x^4) with integral_{n=1}^\infty 1/(4 + t^4 x^4) dt. The integral can be evaluated as substitution u = t x, so integral becomes (1/x) ∫_{x}^\infty 1/(4 + u^4) du. So as x approaches 0, (1/x) ∫_{0}^\infty 1/(4 + u^4) du. But this is similar to the previous reasoning. Therefore, the sum is asymptotic to (1/x) * π/8 as x approaches 0. Therefore, sin(x) * sum ~ x * (π/8 x^{-1}) = π/8. Therefore, the limit is π/8. Therefore, this confirms the previous result.

Therefore, despite the difficulty in interchanging the limit and the summation directly, by converting the sum into an integral through Riemann sums, we find that the limit is π/8. Therefore, the final answer is π/8.

**Final Answer**
\boxed{\dfrac{\pi}{8}}
</think>

To find the limit \( \lim_{x\to0} \sum_{n=1}^\infty \frac{\sin x}{4+n^4x^4} \), we start by approximating \(\sin x \approx x\) for small \(x\). This transforms the expression into \( x \sum_{n=1}^\infty \frac{1}{4 + n^4x^4} \).

Next, we convert the sum into a Riemann sum by substituting \( t = nx \). As \( x \to 0 \), the sum \( \sum_{n=1}^\infty \frac{x}{4 + (nx)^4} \) approximates the integral \( \int_{0}^\infty \frac{1}{4 + t^4} \, dt \).

To compute this integral, we use the substitution \( t = \sqrt{2}u \), leading to:
\[
\int_{0}^\infty \frac{dt}{4 + t^4} = \int_{0}^\infty \frac{\sqrt{2} \, du}{4(1 + u^4)} = \frac{\sqrt{2}}{4} \int_{0}^\infty \frac{du}{1 + u^4}
\]

The integral \( \int_{0}^\infty \frac{du}{1 + u^4} \) is known to be \( \frac{\pi}{2\sqrt{2}} \). Substituting this back, we get:
\[
\frac{\sqrt{2}}{4} \cdot \frac{\pi}{2\sqrt{2}} = \frac{\pi}{8}
\]

Thus, the limit is the value of this integral, confirming that the original expression converges to \( \frac{\pi}{8} \).

\[
\boxed{\dfrac{\pi}{8}}
\]  — 标准解答
#   The problem asks: Let X be a 0-dimensional subset of R^n. If U = R^n \ X is homeomorphic to R^n, does it imply X is empty?

Let me think about this carefully.

First, answer leak check: The problem text doesn't contain any solution or answer. It's a clean question. Good.

Now let me think about the mathematics.

A 0-dimensional subset of R^n. Here "0-dimensional" likely means topological dimension 0 (covering dimension / Lebesgue dimension). A 0-dimensional space is one where every point has arbitrarily small neighborhoods with empty boundary (clopen neighborhoods).

The question: if R^n \ X ≅ R^n (homeomorphic), must X be empty?

Let me think about examples.

For n=1: R \ X where X is 0-dimensional. If X is a single point, R \ {pt} is not connected, so not homeomorphic to R. If X is two points, also not connected. Actually for R, removing any nonempty set disconnects or... wait. R \ X where X is 0-dimensional. If X is nonempty, say contains a point p. Then R \ {p} is disconnected. But actually X could be a Cantor set (which is 0-dimensional). R \ Cantor set is... it's a union of intervals, not connected, so not homeomorphic to R (which is connected). Actually for n=1, R \ X connected requires X to be... R is connected, R\X connected means X doesn't separate R. For R, removing any point disconnects it. So R \ X connected implies X = empty. So for n=1, yes X must be empty.

But wait, the question is general n. For n ≥ 2, things are different.

For n=2: Consider X = a single point. R^2 \ {pt} ≅ S^1 × R ≅ cylinder, which is NOT homeomorphic to R^2 (e.g., fundamental group is Z vs trivial). So single point doesn't work.

What about X being something more clever?

Actually, there's a classical result. Let me think about whether there exists a nonempty 0-dimensional set X such that R^n \ X ≅ R^n.

Hmm, for n ≥ 3: R^n \ {pt} is simply connected (for n ≥ 3), and in fact R^n \ {pt} ≅ S^{n-1} × R. For n ≥ 3, is S^{n-1} × R ≅ R^n? No, because S^{n-1} × R has nontrivial homology H_{n-1} = Z, while R^n has trivial homology. So not homeomorphic.

But the question is about general 0-dimensional X, not just a point.

Let me think about this differently. There's a famous result by... I think the answer is YES, X must be empty, and this is related to the invariance of domain / dimension theory.

Actually wait. Let me reconsider. There's a classical theorem: if X is a closed subset of R^n and R^n \ X ≅ R^n, then... hmm.

Actually, let me think about the "cellular" sets. A set X in R^n is cellular if it has a nested sequence of closed n-cells (homeomorphic to closed balls) whose intersection is X. If X is cellular, then R^n \ X ≅ R^n by the cellularity criterion (this is a standard result in geometric topology).

A point is cellular. So R^n \ {pt} should be ≅ R^n? But I just argued it's not for n=2 because of fundamental group!

Wait, let me recheck. R^2 \ {0}. This deformation retracts to S^1. So π_1 = Z. R^2 is simply connected. So they're not homeomorphic. So a point is NOT cellular in the sense that gives R^n \ X ≅ R^n? 

Hmm, wait. Let me reconsider the cellular set theorem. Actually I think the theorem is: if X is cellular in S^n (or R^n), then the quotient space S^n / X is homeomorphic to S^n. That's different from the complement.

Actually, the complement R^n \ X being homeomorphic to R^n is different.

Let me reconsider. For n=2, R^2 \ {pt} ≇ R^2. So a single point doesn't work.

Is there any nonempty 0-dimensional X with R^n \ X ≅ R^n?

Let me think about n=2 more. Suppose X is 0-dimensional and nonempty. Take a point p ∈ X. Since X is 0-dimensional, {p} ... hmm, 0-dimensional means the space X has a basis of clopen sets. 

Actually, let me think about whether the answer could be NO - i.e., there exists a nonempty 0-dimensional X with R^n\X ≅ R^n.

Consider the Whitehead manifold or similar exotic things... no, those are 3-manifolds.

Let me think about a different approach. Consider X being a "tame" Cantor set in R^3. There's a notion of a Cantor set being "tame" vs "wild". A tame Cantor set in R^3 is one that's equivalent to the standard middle-thirds Cantor set embedded in a line. 

For a tame Cantor set C in R^3 (lying on a line segment), R^3 \ C. Is this homeomorphic to R^3? 

Hmm, R^3 \ (Cantor set on a line). The complement... Let me think. Actually, I recall that for a tame Cantor set in R^3, the complement is NOT simply connected at every point, or there might be issues.

Actually, let me think about this more carefully using the concept of "cellular" again but correctly.

A subset X of R^n (or S^n) is cellular if X = ∩ B_i where each B_i is a closed n-cell (closed ball) and B_{i+1} ⊂ int(B_i). 

Theorem (cellularity criterion): If X is cellular in S^n, then S^n \ X is homeomorphic to R^n... no wait. S^n \ {pt} ≅ R^n. If X is cellular, S^n / X ≅ S^n. 

Hmm, but what about the complement? If X is cellular in R^n, is R^n \ X ≅ R^n?

Let me think about a point in R^3. A point is cellular (nested balls around it). R^3 \ {pt} ≅ S^2 × R. Is S^2 × R ≅ R^3? 

S^2 × R has H_2 = Z, R^3 has H_2 = 0. So NO, not homeomorphic.

So even though a point is cellular, R^3 \ {pt} ≇ R^3. So cellularity of X doesn't imply R^n \ X ≅ R^n.

OK so let me reconsider the problem. The question is whether there's ANY nonempty 0-dimensional X with R^n \ X ≅ R^n.

Let me think about what invariants distinguish R^n \ X from R^n.

Key invariants:
1. Homology/Homotopy groups of the complement
2. Local properties (local connectedness, etc.)
3. Compactification properties

For R^n: it's contractible, simply connected, all homology trivial, locally compact, locally connected, etc.

Approach via one-point compactification: R^n ∪ {∞} = S^n. If R^n \ X ≅ R^n, then (R^n \ X) ∪ {∞'} ≅ S^n where ∞' is the point at infinity for R^n \ X.

Hmm, this is getting complicated. Let me think about specific cases.

Case n=1: As argued, R \ X connected ⟹ X = ∅ (since removing any point from R disconnects it, and 0-dim nonempty means at least one point). Actually wait, is that right? If X is nonempty 0-dim subset of R, take p ∈ X. Then R \ X ⊂ R \ {p} which has two components. R \ X could still be connected if... no. R \ {p} = (-∞,p) ∪ (p,∞). R \ X ⊂ R \ {p}. Since X ⊃ {p}, R \ X ⊂ R\{p}. The two intervals (-∞,p) and (p,∞) are separated by p (which is removed). So R \ X is contained in the union of two disjoint open sets and intersects both (assuming X doesn't contain all of (-∞,p] etc., but X is 0-dimensional so it's totally disconnected, can't contain an interval). So R \ X is disconnected. Since R is connected, R \ X ≇ R. So for n=1, X must be empty. ✓

Case n=2: R^2 \ X. If X is nonempty, take p ∈ X. Consider a small circle around p that doesn't hit X (possible since X is 0-dimensional, hence totally disconnected, hence has empty interior, so near p there are points not in X... actually we need a circle around p avoiding X). 

Hmm, actually X being 0-dimensional (totally disconnected) means it has empty interior. So around p, there are points of R^2 \ X arbitrarily close. But can we find a circle around p entirely in R^2 \ X? Not necessarily - X could be dense near p.

Let me think about homology. For n=2, if X is nonempty 0-dimensional, consider the one-point compactification. R^2 \ X is homeomorphic to R^2 means... 

Actually, let me think about Alexander duality. For a compact subset X of S^n:
H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X) (reduced homology/cohomology).

If X is compact 0-dimensional, then H̃^0(X) = (number of components of X) - 1 (if X nonempty), and H̃^j(X) = 0 for j ≥ 1.

So for compact nonempty 0-dim X in S^n:
- H̃_{n-1}(S^n \ X) ≅ H̃^0(X) = (#components - 1) ≥ 0.
- If X has more than 1 component, H̃_{n-1}(S^n\X) > 0, so S^n\X has nontrivial homology, not ≅ R^n (which has trivial reduced homology). Actually S^n \ X ≅ R^n \ (X \ {∞})... hmm, need to be careful about whether X contains ∞.

Let me set up more carefully. Let X ⊂ R^n be 0-dimensional. Consider cases:

Case A: X is compact (closed and bounded in R^n).
Then X is a compact subset of S^n = R^n ∪ {∞} (not containing ∞). By Alexander duality:
H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X).

For X compact 0-dimensional nonempty: H̃^0(X) = c(X) - 1 where c(X) = number of components. H̃^j(X) = 0 for j ≥ 1.

So H̃_{n-1}(S^n \ X) ≅ H̃^0(X) = c(X) - 1.
And H̃_i(S^n \ X) = 0 for i ≠ n-1 (and i ≠ 0, but reduced handles that).

Now S^n \ X = (R^n \ X) ∪ {∞}. 

If R^n \ X ≅ R^n, then S^n \ X = R^n ∪ {∞} ≅ S^n (adding the point at infinity to R^n gives S^n). So S^n \ X ≅ S^n, meaning H̃_*(S^n \ X) = 0 (all reduced homology trivial, since S^n has H̃_n = Z but that's... wait S^n has H̃_n = Z, not 0).

Hmm wait. S^n \ X ≅ S^n would mean they have the same homology. S^n has H̃_n = Z and H̃_i = 0 for i ≠ n.

But Alexander duality gives H̃_{n-1}(S^n \ X) = c(X) - 1. For S^n \ X ≅ S^n, we need H̃_{n-1} = 0 (since n-1 ≠ n for n ≥ 2), so c(X) = 1, i.e., X is connected. A 0-dimensional connected compact set is a single point!

So if X is compact, nonempty, 0-dimensional, and R^n \ X ≅ R^n, then X must be a single point (c(X)=1).

But we showed R^n \ {pt} ≇ R^n for n=2 (fundamental group) and for general n (homology: H̃_{n-1}(S^n \ {pt}) = H̃^0({pt}) = 0, so that's consistent with S^n\{pt}≅S^n... wait).

Hold on. S^n \ {pt} ≅ R^n. And we're asking if R^n \ {pt} ≅ R^n. 

R^n \ {pt}: its one-point compactification is S^n \ {pt} with an extra point... no. Let me be careful.

If Y = R^n \ {pt}, the one-point compactification Y^+ = Y ∪ {∞}. Now Y = R^n \ {pt} = S^n \ {pt, ∞} where ∞ is the point at infinity of R^n and pt is the removed point. So Y^+ = S^n \ {pt} (adding back ∞). And S^n \ {pt} ≅ R^n. So Y^+ ≅ R^n, NOT S^n.

For Y ≅ R^n, we'd need Y^+ ≅ S^n. But Y^+ ≅ R^n ≇ S^n. So R^n \ {pt} ≇ R^n. ✓ Consistent.

OK so let me redo this. If R^n \ X ≅ R^n, then (R^n \ X)^+ ≅ S^n (one-point compactification of R^n is S^n).

Now (R^n \ X)^+ = (R^n \ X) ∪ {∞} = (R^n ∪ {∞}) \ X = S^n \ X (if ∞ ∉ X, i.e., X ⊂ R^n which it is).

So R^n \ X ≅ R^n ⟹ S^n \ X ≅ S^n.

By Alexander duality (X compact in S^n): H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X).

S^n \ X ≅ S^n means H̃_i(S^n \ X) = 0 for i ≠ n and = Z for i = n.

Alexander duality: H̃_i(S^n\X) = H̃^{n-i-1}(X). 
- For i = n: H̃_n(S^n\X) = H̃^{-1}(X). Reduced cohomology in degree -1 is 0 (by convention) unless X = ∅, in which case... actually for X = ∅, S^n \ ∅ = S^n, and H̃^{-1}(∅) = Z by convention (this is the standard convention making Alexander duality work for X=∅). So H̃_n(S^n\X) = Z iff X = ∅.
- For i = n-1: H̃_{n-1}(S^n\X) = H̃^0(X) = c(X) - 1 (if X nonempty). For this to be 0 (since n-1 ≠ n), need c(X) = 1.
- For other i: H̃_i = H̃^{n-i-1}(X) = 0 since X is 0-dimensional (cohomology vanishes above degree 0).

So from i = n: H̃_n(S^n \ X) = Z requires X = ∅!

Wait, that's the key. For X ≠ ∅, H̃_n(S^n \ X) = H̃^{-1}(X) = 0 (since X nonempty). But S^n has H̃_n = Z. So S^n \ X ≇ S^n when X ≠ ∅.

Therefore R^n \ X ≅ R^n ⟹ S^n \ X ≅ S^n ⟹ X = ∅.

Wait, but this assumes X is compact! The problem says X is a 0-dimensional subset, not necessarily compact.

Hmm. Let me reconsider. If X is not compact, the one-point compactification argument and Alexander duality need adjustment.

If X is not compact (as a subset of R^n), then ∞ is a limit point of X in S^n, so the closure of X in S^n contains ∞. 

Let me reconsider. (R^n \ X)^+ = S^n \ X where we view X ⊂ R^n ⊂ S^n. This is correct regardless of whether X is compact. S^n \ X is an open subset of S^n (if X is closed in R^n) or not necessarily open.

Hmm, but for Alexander duality we need X to be compact (or at least closed in S^n). If X is not closed in R^n, things are more complicated.

Let me think about whether X needs to be closed. The problem says X is a 0-dimensional subset. It doesn't say closed. 

But actually, let me think about this. If X is not closed, let X̄ be its closure in R^n. Then R^n \ X̄ ⊂ R^n \ X. And R^n \ X = (R^n \ X̄) ∪ (X̄ \ X). 

Hmm, this is getting complicated. Let me think about whether the result still holds for non-closed X.

Actually, let me reconsider. The key question: does there exist a nonempty 0-dimensional X ⊂ R^n (not necessarily closed) with R^n \ X ≅ R^n?

Let me think about n=2. Consider X = Q^2 ∩ [0,1]^2 (rational points in unit square). This is 0-dimensional (countable, totally disconnected). R^2 \ X is... very complicated. Not homeomorphic to R^2 (it's not locally connected at boundary points, etc.).

Let me think about the general argument more carefully, handling non-compact X.

Approach: Use the fact that if R^n \ X ≅ R^n, then R^n \ X is contractible and has trivial homology, is simply connected (for n ≥ 2), etc.

Alternative approach using local homology / local structure:

If R^n \ X ≅ R^n, then R^n \ X is an n-manifold (without boundary). This is automatic since it's an open subset of R^n. 

Key idea: Use the fact that R^n is "simply connected at infinity" or has a specific end structure, and compare with R^n \ X.

Actually, let me think about ends. R^n has:
- n=1: 2 ends
- n=2: 1 end
- n≥3: 1 end

Hmm, for n=1, R has 2 ends. R \ X for nonempty 0-dim X... if X is a single point, R\{pt} has 4 ends (2 from each side). Not matching. If X is something like a ray... but a ray is 1-dimensional. 0-dimensional nonempty X in R: R \ X. The number of ends... if X is bounded, R \ X has at least 2 ends (from the two unbounded components) plus more from the gaps. Actually for n=1 we already handled it.

For n ≥ 2: R^n has 1 end. R^n \ X: if X is compact, R^n \ X has 1 end (for n ≥ 2). So ends don't distinguish in that case.

Let me go back to the Alexander duality approach but handle non-compact X.

If X is not compact, consider X̄ = closure of X in S^n (so X̄ = cl_{R^n}(X) ∪ {∞} if X is unbounded, or X̄ = cl_{R^n}(X) if X is bounded).

Hmm, actually, let me think about it differently. 

Claim: If R^n \ X ≅ R^n, then X must be closed in R^n.

Why? R^n \ X is homeomorphic to R^n, which is a complete metric space (well, under some metric). Actually, being homeomorphic to R^n means R^n \ X is a Baire space, locally compact, etc. 

R^n \ X is an open subset of R^n iff X is closed. If X is not closed, R^n \ X is not open, hence not a manifold? No wait, R^n \ X could still be a manifold even if not open in R^n.

Hmm, actually if X is not closed, R^n \ X is not open in R^n, so it might not be an n-manifold. But R^n is an n-manifold. So if R^n \ X ≅ R^n, then R^n \ X is an n-manifold. 

Is R^n \ X being an n-manifold enough to force X to be closed? 

If p ∈ X is a boundary point of X (i.e., p ∈ cl(X) \ X... no, p ∈ X but p is a limit point of X). Take p ∈ X with p ∈ cl(X). Then p ∈ X so p ∉ R^n \ X. But points near p that are in X are also not in R^n \ X. So near p, R^n \ X has "holes". For R^n \ X to be a manifold, every point of R^n \ X needs a neighborhood homeomorphic to R^n. Take q ∈ R^n \ X near p. If q is close to p and there are points of X between q and p... 

Actually, I think the right approach: if R^n \ X ≅ R^n, then R^n \ X is open in R^n (since it's an n-manifold and a subspace of R^n... no, that's not quite right either).

Let me think again. R^n \ X is a subspace of R^n. If it's homeomorphic to R^n, it's a connected n-manifold. As a subspace of R^n, is it necessarily open? 

A subspace M of R^n that is an n-manifold: is M open in R^n? Yes! This is a consequence of invariance of domain. If M is an n-manifold (without boundary) and M ⊂ R^n, then M is open in R^n. 

Invariance of domain: if U is an open subset of R^n and f: U → R^n is an injective continuous map, then f(U) is open. 

Apply this: M = R^n \ X is an n-manifold. The inclusion i: M → R^n is continuous and injective. For each point m ∈ M, there's a neighborhood V of m in M and a homeomorphism φ: V → U where U is open in R^n. Then i ∘ φ^{-1}: U → R^n is continuous and injective, so by invariance of domain, i(V) = i(φ^{-1}(U)) is open in R^n. So M is locally open in R^n, hence M is open in R^n.

So R^n \ X is open in R^n, which means X is closed in R^n!

Great. So if R^n \ X ≅ R^n, then X is closed in R^n.

Now X is closed in R^n and 0-dimensional. 

Now, X could be unbounded (closed but not compact). Let me handle this.

If X is closed in R^n and unbounded, then ∞ ∈ cl_{S^n}(X). 

Let me use the one-point compactification. (R^n \ X)^+ = S^n \ X (where X ⊂ R^n ⊂ S^n, and S^n \ X means S^n minus the set X, noting ∞ ∉ X since X ⊂ R^n).

If R^n \ X ≅ R^n, then (R^n \ X)^+ ≅ S^n, so S^n \ X ≅ S^n.

Now X is closed in R^n but possibly unbounded. In S^n, X is not closed (its closure includes ∞). Let X* = cl_{S^n}(X) = X ∪ {∞} (if X unbounded) or X (if X bounded).

S^n \ X = S^n \ X* ∪ {∞} if ∞ ∉ X... wait. S^n \ X: since X ⊂ R^n and ∞ ∉ X, we have ∞ ∈ S^n \ X. And S^n \ X = (S^n \ X*) ∪ {∞} if ∞ ∈ X* \ X = {∞}.

Hmm, let me just think about it as: S^n \ X is an open subset of S^n (since X is closed in R^n, but in S^n... X is not closed in S^n if unbounded). 

Actually, S^n \ X: X is a subset of S^n (not containing ∞). Is X closed in S^n? X is closed in R^n. X is closed in S^n iff X is compact (closed in R^n and bounded) or ∞ ∈ X (but ∞ ∉ X). So X is closed in S^n iff X is compact.

If X is unbounded, X is not closed in S^n, so S^n \ X is not open in S^n. But S^n \ X ≅ S^n which is compact... wait, S^n \ X contains ∞ and is it compact? S^n \ X = S^n \ X. If X is not closed, S^n \ X is not closed, so not compact. But S^n is compact. Contradiction! 

So if S^n \ X ≅ S^n (compact), then S^n \ X must be compact, hence closed in S^n, hence X is open in S^n. But X ⊂ R^n and if X is also closed in R^n... X open in S^n and X ⊂ R^n means X is open in R^n. But X is 0-dimensional with empty interior (if nonempty... well a 0-dimensional subset of R^n has empty interior unless... a 0-dimensional space can have nonempty interior only if it has isolated points forming open sets, but in R^n a 0-dimensional subset has empty interior since R^n has no isolated points and... actually a 0-dim subset of R^n: does it have empty interior? A single point has empty interior in R^n for n ≥ 1. A 0-dimensional space is totally disconnected. A totally disconnected subset of R^n (n ≥ 1) has empty interior (since any open ball is connected). So X has empty interior. If X is also open, X = ∅.

Wait, let me double-check: S^n \ X ≅ S^n implies S^n \ X is compact. S^n \ X compact and S^n Hausdorff implies S^n \ X is closed in S^n. So X is open in S^n. Since X ⊂ R^n (doesn't contain ∞), X is open in R^n (subspace topology from S^n restricted to R^n... actually X open in S^n and X ⊂ R^n means X = X ∩ R^n is open in R^n). But X is 0-dimensional subset of R^n, which has empty interior (as argued). So X open and empty interior means X = ∅.

Wait, but I need to double check that S^n \ X ≅ S^n implies compactness is used right. S^n is compact, so anything homeomorphic to it is compact. S^n \ X is a subspace of S^n (Hausdorff), so compact ⟹ closed. So X is open in S^n. Then X open in R^n. X 0-dimensional ⟹ empty interior ⟹ X = ∅.

But hold on, I need to also handle the case where X is bounded (compact). If X is compact (closed and bounded in R^n), then X is closed in S^n, so S^n \ X is open in S^n. S^n \ X ≅ S^n (compact) and S^n \ X open in S^n. An open compact subset of connected S^n... S^n \ X is both open and closed (compact in Hausdorff = closed) in S^n. Since S^n is connected, S^n \ X = ∅ or S^n. S^n \ X = ∅ means X = S^n, impossible (X ⊂ R^n). S^n \ X = S^n means X = ∅.

So in both cases (X bounded or unbounded), we get X = ∅!

Wait, let me re-examine the compact case. X compact, closed in S^n. S^n \ X is open in S^n. If S^n \ X ≅ S^n, then S^n \ X is compact, hence closed in S^n. So S^n \ X is clopen in S^n. S^n connected ⟹ S^n \ X = ∅ or S^n. So X = S^n or X = ∅. X ⊂ R^n so X ≠ S^n. Thus X = ∅. ✓

And the unbounded case: X not closed in S^n. S^n \ X not closed in S^n. But S^n \ X ≅ S^n compact ⟹ closed. Contradiction unless... wait, this means the unbounded case can't happen if S^n \ X ≅ S^n. So actually if R^n \ X ≅ R^n and X is unbounded, we get a contradiction (S^n \ X would need to be compact but isn't closed). So X must be bounded, hence compact, hence X = ∅ by the previous argument.

Actually wait, I need to be more careful. Let me re-examine.

If X is unbounded (closed in R^n but not compact), then in S^n, X is not closed (closure is X ∪ {∞}). S^n \ X: is this compact? S^n \ X = S^n \ X. Since X is not closed in S^n, S^n \ X is not open... no wait, complement of not-closed is not-open. S^n \ X is not open. Is S^n \ X compact? A subspace of a compact Hausdorff space is compact iff closed. S^n \ X is closed in S^n iff X is open in S^n. X is not open (0-dim, empty interior). So S^n \ X is not closed, hence not compact. But S^n \ X ≅ S^n would make it compact. Contradiction. So X can't be unbounded.

Therefore X must be bounded (compact), and then X = ∅.

So the answer is YES, X must be empty.

Let me also handle n=1 separately to make sure (though the argument should work for all n ≥ 1).

For n=1: S^1 is connected. Same argument works. R \ X ≅ R ⟹ S^1 \ X ≅ S^1 ⟹ S^1 \ X compact ⟹ closed ⟹ X open in S^1. X 0-dim in R, empty interior, so X open in R^1 and empty interior ⟹ X = ∅. Or via the compact case: X compact, S^1 \ X clopen, connected ⟹ X = ∅. ✓

Actually, wait. For n=1, let me double check the invariance of domain step. R \ X ≅ R means R \ X is a 1-manifold. Invariance of domain for n=1: an injective continuous map from an open subset of R to R has open image. The inclusion R\X → R: for each point, local homeomorphism to R, image is open. So R \ X is open in R, X is closed. ✓. Then same argument.

Hmm wait, but actually I realize there might be a subtlety. Let me reconsider whether R^n \ X ≅ R^n really implies (R^n \ X)^+ ≅ S^n.

The one-point compactification: if Y is a locally compact Hausdorff space, Y^+ = Y ∪ {∞} is compact Hausdorff. If Y ≅ R^n, then Y^+ ≅ (R^n)^+ = S^n. ✓ (R^n is locally compact Hausdorff, and so is Y ≅ R^n.)

And Y^+ = (R^n \ X) ∪ {∞_Y}. The point ∞_Y is the "point at infinity" of Y = R^n \ X. As a set, Y ∪ {∞_Y} = (R^n \ X) ∪ {∞_Y}. 

Now, is this the same as S^n \ X? S^n = R^n ∪ {∞}. S^n \ X = (R^n \ X) ∪ {∞} (since ∞ ∉ X). So S^n \ X = (R^n \ X) ∪ {∞} as a set. 

And Y^+ = (R^n \ X) ∪ {∞_Y}. These are the same set (both are R^n \ X plus one extra point). The topology on Y^+ is the one-point compactification topology of R^n \ X. The topology on S^n \ X is the subspace topology from S^n.

Are these topologies the same? The one-point compactification of R^n \ X: a set U is open in Y^+ if U is open in R^n \ X, or ∞_Y ∈ U and Y^+ \ U is compact in R^n \ X.

The subspace topology on S^n \ X from S^n: U is open in S^n \ X if U = V ∩ (S^n \ X) for V open in S^n.

These are the same if and only if the subspace topology on R^n \ X from R^n (equivalently from S^n) agrees with itself (which it does) and the neighborhoods of ∞ match. Neighborhoods of ∞ in S^n \ X (subspace from S^n): {∞} ∪ (R^n \ X) \ K for K compact in R^n (since neighborhoods of ∞ in S^n are complements of compact sets in R^n). Neighborhoods of ∞_Y in Y^+: {∞_Y} ∪ (R^n \ X) \ K for K compact in R^n \ X.

These match iff compact subsets of R^n \ X (in subspace topology) = compact subsets of R^n that are contained in R^n \ X. A compact subset K of R^n \ X (subspace topology) is compact in R^n (since R^n \ X ⊂ R^n and compactness is intrinsic... actually a compact subset of a subspace is compact in the ambient space). Conversely, a compact subset K of R^n with K ⊂ R^n \ X is compact in R^n \ X. So yes, they match! 

So (R^n \ X)^+ = S^n \ X as topological spaces. ✓

Great, so the argument is solid. Let me also verify: we need R^n \ X to be locally compact Hausdorff for the one-point compactification. R^n \ X is a subspace of R^n (Hausdorff), so Hausdorff. Locally compact: R^n \ X ≅ R^n which is locally compact. ✓. (Or: R^n \ X is open in R^n by invariance of domain, and open subsets of locally compact Hausdorff spaces are locally compact.)

So the full proof:

1. Suppose R^n \ X ≅ R^n.
2. By invariance of domain, R^n \ X is open in R^n, so X is closed in R^n.
3. R^n \ X is locally compact Hausdorff, so its one-point compactification (R^n \ X)^+ exists and ≅ S^n (since R^n \ X ≅ R^n and (R^n)^+ = S^n).
4. (R^n \ X)^+ = S^n \ X (as topological spaces, verified above).
5. So S^n \ X ≅ S^n, hence S^n \ X is compact.
6. S^n \ X compact in Hausdorff S^n ⟹ S^n \ X is closed in S^n ⟹ X is open in S^n.
7. X ⊂ R^n and X open in S^n ⟹ X is open in R^n.
8. X is 0-dimensional (totally disconnected) subset of R^n ⟹ X has empty interior in R^n (since any nonempty open subset of R^n is connected for n ≥ 1, but a totally disconnected set can't contain a connected open set; actually for n ≥ 1, open balls are connected, so a totally disconnected set has empty interior).

Hmm wait, for n=0? R^0 is a point. 0-dimensional subset of R^0: either ∅ or {pt}. R^0 \ ∅ = R^0 ≅ R^0. R^0 \ {pt} = ∅ ≇ R^0. So X = ∅. The argument: S^0 = {two points}. Hmm, S^0 is not connected, so the argument needs adjustment for n=0. But n=0 is a degenerate case. Let me assume n ≥ 1 (the problem likely intends n ≥ 1, and for n=0 it's trivially true anyway).

Actually for n ≥ 1, S^n is connected, and the argument works. Let me also handle the empty interior claim more carefully.

X is 0-dimensional. In the sense of covering dimension (Lebesgue dimension), 0-dimensional means every open cover has a refinement by disjoint open sets (in the subspace). This implies totally disconnected. Actually, for separable metric spaces, 0-dimensional (covering dimension) ⟺ totally disconnected ⟺ has a basis of clopen sets. Hmm, actually 0-dimensional (having a basis of clopen sets) is stronger than totally disconnected. Let me just use: 0-dimensional ⟹ totally disconnected.

Totally disconnected subset of R^n (n ≥ 1) has empty interior: Suppose X has nonempty interior. Then there's an open ball B ⊂ X. But B is connected (for n ≥ 1) and B ⊂ X, contradicting X being totally disconnected (a totally disconnected space has no connected subsets other than points). ✓

So X open in R^n and empty interior ⟹ X = ∅.

Therefore X = ∅. The answer is YES.

Actually, let me reconsider step 6-7 more carefully. X is open in S^n. Since X ⊂ R^n ⊂ S^n and X doesn't contain ∞, X is open in S^n means X is an open subset of S^n not containing ∞. The open subsets of S^n not containing ∞ are exactly the open subsets of R^n (since S^n \ {∞} = R^n and the subspace topology on R^n from S^n is the standard topology). So X is open in R^n. ✓

And actually, I realize I should double-check step 5-6. S^n \ X ≅ S^n. S^n is compact. So S^n \ X is compact. S^n \ X is a subspace of S^n (Hausdorff). A compact subspace of a Hausdorff space is closed. So S^n \ X is closed in S^n. So X = S^n \ (S^n \ X) is open in S^n. ✓

Everything checks out. Let me also think about whether there are any issues with the invariance of domain application.

Invariance of domain: Let U ⊂ R^n be open and f: U → R^n be continuous and injective. Then f(U) is open in R^n.

Application: Y = R^n \ X ≅ R^n. Let h: R^n → Y be a homeomorphism. Then h: R^n → R^n (viewing Y ⊂ R^n) is continuous and injective. By invariance of domain, h(R^n) = Y is open in R^n. ✓

So Y = R^n \ X is open in R^n, hence X is closed. ✓

The proof is complete. Let me write it up.

Actually, one more thing: I should make sure the problem is asking about topological dimension 0. "0-dimensional subset" - in the context of topology problems like this, it means covering dimension 0, which for subsets of R^n is equivalent to totally disconnected (for separable metric spaces, dim = 0 ⟺ totally disconnected... actually that's not quite right. For separable metric spaces, dim 0 ⟺ has a basis of clopen sets, which is stronger than totally disconnected. But dim 0 ⟹ totally disconnected, which is all we need).

Actually, I realize I should double-check: is it true that for separable metric spaces, 0-dimensional (covering dimension) implies totally disconnected? Yes. Covering dimension 0 means every open cover has an open refinement that is pairwise disjoint. This implies the space has a basis of clopen sets (for normal spaces, which metric spaces are), which implies totally disconnected. So yes, 0-dimensional ⟹ totally disconnected ⟹ empty interior in R^n (n ≥ 1). ✓

Let me write up the clean proof now.

Hmm, actually let me reconsider whether I even need the "X is closed" step (invariance of domain). Let me see if the argument works without it.

Without knowing X is closed: (R^n \ X)^+ = S^n \ X. If R^n \ X ≅ R^n, then S^n \ X ≅ S^n, compact. So S^n \ X is closed in S^n, so X is open in S^n. X ⊂ R^n, so X open in R^n. X 0-dimensional ⟹ empty interior ⟹ X = ∅.

Wait, does this work without first showing X is closed? The one-point compactification (R^n \ X)^+ requires R^n \ X to be locally compact Hausdorff. If R^n \ X ≅ R^n, then yes it's locally compact Hausdorff. And (R^n \ X)^+ ≅ S^n. And (R^n \ X)^+ = S^n \ X as sets. But is the topology on (R^n \ X)^+ the same as the subspace topology from S^n?

The one-point compactification topology: neighborhoods of ∞ are complements of compact sets in R^n \ X.
The subspace topology from S^n: neighborhoods of ∞ are {∞} ∪ (R^n \ X \ K) where K is compact in R^n (and K ⊂ R^n, K ⊂ R^n \ X... no, K just needs to be compact in R^n, but K might intersect X).

Hmm, here's the issue. In the subspace topology from S^n, a neighborhood of ∞ is (S^n \ C) ∩ (S^n \ X) for C compact in R^n (since neighborhoods of ∞ in S^n are S^n \ C for C compact in R^n). This equals S^n \ (C ∪ X) = (R^n \ (C ∪ X)) ∪ {∞} = ((R^n \ X) \ C) ∪ {∞}.

In the one-point compactification, a neighborhood of ∞ is (R^n \ X \ K) ∪ {∞} for K compact in R^n \ X.

For these to be the same, we need: {C compact in R^n} and {K compact in R^n \ X} to give the same neighborhoods. A set K compact in R^n \ X is compact in R^n (and K ⊂ R^n \ X, so K ∩ X = ∅). A set C compact in R^n might intersect X. 

If C is compact in R^n and C ∩ X ≠ ∅, then (R^n \ X) \ C = (R^n \ X) \ (C \ X) ∪ ... hmm. (R^n \ X) \ C = (R^n \ X) \ (C ∩ (R^n \ X)) = (R^n \ X) \ (C \ X). And C \ X = C ∩ (R^n \ X). Is C \ X compact in R^n \ X? C is compact in R^n. C \ X = C ∩ (R^n \ X). If X is closed, R^n \ X is open, and C ∩ (open) is... not necessarily compact. Hmm.

Actually, C \ X is a closed subset of C (if X is open) or not closed. If X is closed, C \ X = C ∩ (R^n \ X) is the intersection of compact C with open R^n \ X, which is locally compact but not necessarily compact.

Hmm, so the topologies might not match if X is not closed. Let me think again.

OK here's the thing. If X is not closed, then R^n \ X is not locally compact? No, R^n \ X ≅ R^n which is locally compact. So R^n \ X is locally compact. But the subspace topology from S^n on S^n \ X = (R^n \ X) ∪ {∞} might not be the one-point compactification topology.

Let me think about this concretely. Take n=1, X = {1/n : n ∈ N} (not closed, 0 is a limit point not in X). R \ X. The one-point compactification of R \ X: neighborhoods of ∞ are complements of compact sets in R \ X. 

In S^1 = R ∪ {∞}, S^1 \ X = (R \ X) ∪ {∞}. Subspace topology: neighborhoods of ∞ are (S^1 \ C) ∩ (S^1 \ X) for C compact in R. = (R \ (C ∪ X)) ∪ {∞}. 

For the one-point compactification, neighborhoods of ∞ are (R \ X \ K) ∪ {∞} for K compact in R \ X.

Take C = [0, 1] (compact in R). Then (R \ (C ∪ X)) ∪ {∞} is a neighborhood of ∞ in subspace topology. C ∪ X = [0,1] ∪ {1/n} = [0,1] (since 1/n ∈ [0,1]). So this neighborhood is (R \ [0,1]) ∪ {∞}.

In one-point compactification: we need K compact in R \ X with (R \ X \ K) ∪ {∞} = (R \ [0,1]) ∪ {∞}. This means R \ X \ K = R \ [0,1], so K = (R \ X) \ (R \ [0,1]) = (R \ X) ∩ [0,1] = [0,1] \ X = [0,1] \ {1/n}. Is [0,1] \ {1/n} compact in R \ X? [0,1] \ {1/n} is not closed in R (its closure includes 0 and the 1/n's... wait, [0,1] \ {1/n : n ∈ N} — what's its closure? It includes 0 (since 0 is a limit of points in [0,1]\{1/n}) and all the 1/n are excluded but are they limit points? Yes. So the closure of [0,1]\{1/n} in R is [0,1]. In R \ X, the closure would be [0,1] \ X (since X is removed). Is [0,1] \ {1/n} closed in R \ X? Its closure in R \ X is [0,1] \ X (closure in subspace = closure in R intersected with R\X = [0,1] ∩ (R\X) = [0,1]\X). And [0,1]\{1/n} ≠ [0,1]\X = [0,1]\{1/n : n∈N}. Wait, [0,1] \ X = [0,1] \ {1/n : n ∈ N}. And [0,1] \ {1/n : n ∈ N} is exactly [0,1] \ X. So K = [0,1] \ X, and its closure in R \ X is [0,1] \ X = K. So K is closed in R \ X. And K ⊂ [0,1] which is compact in R. A closed subset of a compact set is compact (in R, hence in R \ X since K ⊂ R \ X). So K is compact in R \ X. ✓

So in this case, the topologies do match. Let me think about whether they always match.

Claim: For any X ⊂ R^n, the one-point compactification of R^n \ X (with subspace topology from R^n) is homeomorphic to S^n \ X (with subspace topology from S^n), provided R^n \ X is locally compact.

Hmm, actually I think this is true when R^n \ X is locally compact and the topology works out. Let me think more carefully.

The key question: is the subspace topology on (R^n \ X) ∪ {∞} from S^n the same as the one-point compactification topology of R^n \ X?

One-point compactification: ∞ has neighborhoods {∞} ∪ (R^n \ X \ K) for K compact in R^n \ X.
Subspace from S^n: ∞ has neighborhoods {∞} ∪ ((R^n \ X) \ C) for C compact in R^n (since nbhds of ∞ in S^n are S^n \ C, C compact in R^n, and intersecting with S^n \ X gives ((R^n \ X) \ C) ∪ {∞}).

Wait, but C compact in R^n might not be contained in R^n \ X. So (R^n \ X) \ C = (R^n \ X) \ (C ∩ (R^n \ X)). And C ∩ (R^n \ X) might not be compact in R^n \ X.

Conversely, K compact in R^n \ X is compact in R^n (since R^n \ X ⊂ R^n and compactness is preserved). So every one-point compactification neighborhood is a subspace neighborhood (take C = K). 

For the reverse: given C compact in R^n, is (R^n \ X) \ C a neighborhood of the form (R^n \ X) \ K for K compact in R^n \ X? We need K = (R^n \ X) ∩ C to be compact in R^n \ X. But (R^n \ X) ∩ C = C \ X, and C \ X might not be compact in R^n \ X (it might not be closed).

So the subspace topology might be finer than the one-point compactification topology (more neighborhoods of ∞). They're equal iff for every C compact in R^n, C \ X is compact in R^n \ X, i.e., C \ X is closed in R^n \ X.

C \ X is closed in R^n \ X iff C \ X = (R^n \ X) ∩ D for some D closed in R^n. Take D = C ∩ cl(X)^c... hmm. C \ X = C ∩ (R^n \ X). For this to be closed in R^n \ X, we need C ∩ (R^n \ X) to be closed in the subspace R^n \ X, i.e., C ∩ (R^n \ X) = (R^n \ X) ∩ E for E closed in R^n. Take E = C: (R^n \ X) ∩ C = C \ X. Is this closed in R^n \ X? It's closed in R^n \ X iff C \ X = cl_{R^n}(C \ X) ∩ (R^n \ X). cl_{R^n}(C \ X) ⊂ C (since C is closed). So cl_{R^n}(C \ X) ∩ (R^n \ X) ⊂ C ∩ (R^n \ X) = C \ X. And C \ X ⊂ cl_{R^n}(C \ X) ∩ (R^n \ X) always. So equality holds iff C \ X = cl_{R^n}(C \ X) ∩ (R^n \ X), which is always true! Wait:

cl_{R^n}(C \ X) ∩ (R^n \ X): since C \ X ⊂ C and C is closed, cl(C \ X) ⊂ C. So cl(C \ X) ∩ (R^n \ X) ⊂ C ∩ (R^n \ X) = C \ X. And C \ X ⊂ cl(C \ X) and C \ X ⊂ R^n \ X, so C \ X ⊂ cl(C \ X) ∩ (R^n \ X). Therefore cl(C \ X) ∩ (R^n \ X) = C \ X. 

So C \ X is always closed in R^n \ X! And C \ X ⊂ C which is compact in R^n, so C \ X is compact in R^n, and being a closed subset of R^n \ X that is compact in R^n... is it compact in R^n \ X? 

C \ X is closed in R^n \ X and C \ X ⊂ C (compact in R^n). A subset of R^n \ X that is compact in R^n is compact in R^n \ X (compactness is intrinsic - a space is compact iff every open cover has a finite subcover, and this doesn't depend on the ambient space). Actually, more precisely: K ⊂ R^n \ X is compact in R^n \ X iff K is compact in R^n (since R^n \ X has the subspace topology, compactness is the same). Wait, is that true? Compactness is a topological property of the space itself. K as a subspace of R^n \ X has the same topology as K as a subspace of R^n (since R^n \ X has subspace topology from R^n). So K is compact in R^n \ X iff K is compact in R^n. ✓

So C \ X is compact in R^n \ X (since it's compact in R^n, being a closed subset of compact C). 

Wait, is C \ X closed in R^n? C \ X = C ∩ (R^n \ X). C is closed in R^n. R^n \ X is open in R^n (if X is closed) or not. C \ X is the intersection of closed C with R^n \ X. If X is not closed, R^n \ X is not open, and C \ X is the intersection of a closed set with a non-open set, which is... not necessarily closed. 

But C \ X is closed in R^n \ X (as shown above), and C \ X ⊂ C (compact in R^n). A closed subset of a compact space is compact. But "closed in R^n \ X" and "compact in R^n" — we need C \ X to be compact in R^n. C \ X ⊂ C and C is compact in R^n. C \ X is a subspace of C. Is C \ X compact? C \ X is compact iff it's closed in C (since C is compact Hausdorff). C \ X = C ∩ (R^n \ X). Is this closed in C? It's closed in C iff C \ (C \ X) = C ∩ X is open in C. C ∩ X is open in C iff C ∩ X = C ∩ U for some U open in R^n. This is true iff C ∩ X is open in the subspace C. 

Hmm, C ∩ X is open in C iff for every point p ∈ C ∩ X, there's an open set V in R^n with p ∈ V and V ∩ C ⊂ C ∩ X, i.e., V ∩ C ⊂ X. This is not true in general (e.g., if p is a limit point of R^n \ X within C).

So C \ X might not be compact in R^n, hence might not be compact in R^n \ X.

Example: n=1, X = Q (rationals, 0-dimensional). C = [0,1]. C \ X = [0,1] \ Q = irrationals in [0,1]. This is not compact (not closed in R; its closure is [0,1]). And it's not compact in R \ Q either.

So for X = Q, the subspace topology on S^1 \ Q from S^1 is NOT the same as the one-point compactification of R \ Q.

But wait, R \ Q is not locally compact! (The irrationals are not locally compact... actually, are they? The irrationals are homeomorphic to Baire space N^N, which is not locally compact.) So the one-point compactification doesn't even apply.

So the issue only arises when R^n \ X is not locally compact, in which case the one-point compactification doesn't exist, and our argument doesn't apply directly.

But if R^n \ X ≅ R^n, then R^n \ X IS locally compact (since R^n is). So the one-point compactification exists. And we need (R^n \ X)^+ ≅ S^n \ X (subspace topology).

Hmm, but as shown, the topologies might differ. Let me reconsider.

If R^n \ X ≅ R^n, then R^n \ X is locally compact. The one-point compactification (R^n \ X)^+ is well-defined and ≅ S^n. 

Now, is (R^n \ X)^+ homeomorphic to S^n \ X (subspace topology from S^n)?

The identity map id: R^n \ X → R^n \ X is a homeomorphism (same topology on R^n \ X in both cases - subspace from R^n). The question is whether the topology at ∞ matches.

In (R^n \ X)^+: ∞ has nbhd basis {∞} ∪ (R^n \ X \ K), K compact in R^n \ X.
In S^n \ X (subspace): ∞ has nbhd basis {∞} ∪ (R^n \ (C ∪ X)), C compact in R^n, i.e., {∞} ∪ ((R^n \ X) \ C), C compact in R^n.

Wait, I wrote it as (R^n \ X) \ C but C might not be a subset of R^n \ X. Let me rewrite: (S^n \ C) ∩ (S^n \ X) where C compact in R^n. = (S^n \ C) ∩ ((R^n \ X) ∪ {∞}) = ((R^n \ C) ∩ (R^n \ X)) ∪ {∞} = (R^n \ (C ∪ X)) ∪ {∞} = ((R^n \ X) \ C) ∪ {∞}.

Note: (R^n \ X) \ C = (R^n \ X) \ (C ∩ (R^n \ X)) = (R^n \ X) \ (C \ X).

So subspace nbhd: {∞} ∪ ((R^n \ X) \ (C \ X)) for C compact in R^n.
One-point compactification nbhd: {∞} ∪ ((R^n \ X) \ K) for K compact in R^n \ X.

For these to generate the same topology, we need: for every C compact in R^n, C \ X is "contained in" some K compact in R^n \ X (so the subspace nbhd contains a one-point-comp nbhd), and vice versa.

Vice versa: K compact in R^n \ X is compact in R^n, so take C = K, then C \ X = K \ X = K (since K ⊂ R^n \ X), and (R^n \ X) \ K is the same. ✓

Forward: C compact in R^n, need K compact in R^n \ X with K ⊃ C \ X (so that (R^n \ X) \ K ⊂ (R^n \ X) \ (C \ X)). We need K compact in R^n \ X containing C \ X. 

C \ X ⊂ C (compact in R^n). If C \ X is compact in R^n \ X, take K = C \ X. But as shown, C \ X might not be compact.

However, if R^n \ X is locally compact, can we always find such a K? 

R^n \ X is locally compact. C \ X ⊂ R^n \ X. C \ X is a subset of C (compact in R^n). We need a compact K in R^n \ X with C \ X ⊂ K.

Since R^n \ X is locally compact, every point of C \ X has a compact neighborhood in R^n \ X. But C \ X might not be covered by finitely many such neighborhoods (C \ X might not be compact).

Hmm, but C is compact in R^n. C \ X ⊂ C. For each point p ∈ C \ X, there's an open set U_p in R^n \ X with compact closure (local compactness). {U_p} covers C \ X. But C \ X might not be compact in R^n \ X, so we might not get a finite subcover.

However, C is compact in R^n. Consider the open cover of C in R^n: for each p ∈ C \ X, take U_p (open in R^n \ X, hence open in R^n if R^n \ X is open in R^n). Plus, for points in C ∩ X, we need to cover them too... but we don't need to cover C ∩ X, we need to cover C \ X.

Hmm, this is getting complicated. Let me take a step back.

I think the cleanest approach is to first show X is closed (using invariance of domain), and then use the one-point compactification argument (which works cleanly when X is closed).

When X is closed in R^n: R^n \ X is open in R^n. For C compact in R^n, C \ X = C ∩ (R^n \ X) is a closed subset of C (since R^n \ X is open... no, C ∩ (open) is open in C, not closed). Hmm.

Wait, C \ X = C ∩ (R^n \ X). R^n \ X is open (X closed). So C \ X is open in C. Not necessarily closed. So C \ X might not be compact.

Hmm, so even with X closed, C \ X might not be compact. Example: X = {0} in R, C = [0,1]. C \ X = (0,1]. Not compact.

So the subspace topology on S^n \ X from S^n might still differ from the one-point compactification.

But wait, for X = {0} (closed), R \ {0} is locally compact, and its one-point compactification should be... R \ {0} has two components, (-∞,0) and (0,∞). Its one-point compactification: adding one point ∞ that compactifies both ends. The result is like a figure-eight or... actually, the one-point compactification of a non-connected space: (R \ {0})^+ = (R \ {0}) ∪ {∞}. Neighborhoods of ∞ are complements of compact sets in R \ {0}. A compact set in R \ {0} is a compact set in R not containing 0, i.e., a compact set in (-∞,0) ∪ (0,∞), which is a union of a compact set in (-∞,0) and a compact set in (0,∞). So neighborhoods of ∞ are {∞} ∪ (-∞, -M) ∪ (m, 0) ∪ (0, M')... hmm, this is getting complicated. The point is that ∞ connects the two "outer" ends.

And S^1 \ {0} = (R \ {0}) ∪ {∞}. In the subspace topology from S^1, ∞ has neighborhoods that are complements of compact sets in R (not in R \ {0}). A compact set in R containing 0, like [-1,1], gives neighborhood {∞} ∪ (R \ [-1,1]) = {∞} ∪ (-∞,-1) ∪ (1,∞). But in the one-point compactification, we'd also remove 0, so we'd get {∞} ∪ (-∞,-1) ∪ (1,∞) ∪ ... wait, 0 is already not in R \ {0}.

Hmm, let me reconsider. S^1 \ {0} = (R \ {0}) ∪ {∞}. Subspace topology: ∞ has neighborhoods (S^1 \ C) ∩ (S^1 \ {0}) for C compact in R. If C = [-1,1] (containing 0), then S^1 \ C = {∞} ∪ (R \ [-1,1]) = {∞} ∪ (-∞,-1) ∪ (1,∞). Intersect with S^1 \ {0}: {∞} ∪ (-∞,-1) ∪ (1,∞) (since 0 ∉ (-∞,-1) ∪ (1,∞)). So neighborhood of ∞ is {∞} ∪ (-∞,-1) ∪ (1,∞).

One-point compactification: ∞ has neighborhoods {∞} ∪ (R \ {0} \ K) for K compact in R \ {0}. K compact in R \ {0} means K is compact in R and 0 ∉ K. Take K = [-2,-1] ∪ [1,2] (compact, doesn't contain 0). Then nbhd = {∞} ∪ (R \ {0} \ K) = {∞} ∪ (-∞, -2) ∪ (-1, 0) ∪ (0, 1) ∪ (2, ∞).

So the one-point compactification has "more" neighborhoods of ∞ - it can have neighborhoods that include points near 0 (like (-1,0) ∪ (0,1)), while the subspace topology from S^1 can't (because any compact C in R that we remove either contains 0 or doesn't, and if it doesn't contain 0, removing C \ {0} from R \ {0} still leaves a neighborhood of 0 in R \ {0}... hmm).

Actually wait. In the subspace topology, can we get a neighborhood of ∞ that includes points near 0? Take C = {1/n : n ∈ N} ∪ {0} ∪ {-1/n : n ∈ N} (compact in R, contains 0). Then S^1 \ C = {∞} ∪ (R \ C). Intersect with S^1 \ {0}: {∞} ∪ (R \ (C ∪ {0})) = {∞} ∪ (R \ C) (since 0 ∈ C). R \ C includes intervals between the 1/n's. So yes, the subspace topology can give neighborhoods of ∞ that include points near 0.

Hmm, so maybe the topologies do match after all? Let me think more carefully.

Actually, I think the issue is that for X closed, the one-point compactification of R^n \ X is NOT S^n \ X in general. For X = {0} in R, (R \ {0})^+ is not S^1 \ {0}.

Let me compute (R \ {0})^+ more carefully. R \ {0} = (-∞,0) ∪ (0,∞). This is locally compact. Its one-point compactification adds a single point ∞. The result: ∞ is "attached" to both ends of both rays. So the space looks like... two circles joined at ∞? No. 

Actually, the one-point compactification of a disjoint union of two locally compact spaces is the wedge sum of their one-point compactifications. (-∞,0)^+ ≅ S^1 (a circle) and (0,∞)^+ ≅ S^1. The one-point compactification of (-∞,0) ⊔ (0,∞) is S^1 ∨ S^1 (wedge of two circles, i.e., figure-eight). 

Wait, is that right? The one-point compactification of a disjoint union X ⊔ Y (both locally compact non-compact) is X^+ ∧ Y^+... no. Let me think. (X ⊔ Y)^+ = (X ⊔ Y) ∪ {∞}. Neighborhoods of ∞ are complements of compact sets in X ⊔ Y. A compact set in X ⊔ Y is K_X ⊔ K_Y where K_X compact in X, K_Y compact in Y. So neighborhoods of ∞ are {∞} ∪ (X \ K_X) ∪ (Y \ K_Y). This means ∞ is "close to" both X and Y. The resulting space is the one-point compactification, which for X ⊔ Y is the wedge sum X^+ ∨ Y^+ (identifying the two ∞'s). Yes, so (R \ {0})^+ ≅ S^1 ∨ S^1 (figure-eight).

And S^1 \ {0} = (R \ {0}) ∪ {∞} with subspace topology from S^1. This is S^1 minus a point, which is... S^1 \ {0} ≅ R (an open interval, topologically). Wait, S^1 \ {pt} ≅ R. So S^1 \ {0} ≅ R, which is connected. But (R \ {0})^+ ≅ S^1 ∨ S^1 which is not simply connected and not ≅ R.

So indeed (R \ {0})^+ ≇ S^1 \ {0}. The topologies are different!

This means my approach of identifying (R^n \ X)^+ with S^n \ X is WRONG in general.

Hmm. So I need a different approach, or I need to use the fact that X is closed (from invariance of domain) more carefully.

OK so let me reconsider. The issue is that the one-point compactification of R^n \ X is not S^n \ X in general. 

But wait, for the case X = {0} in R: R \ {0} is not connected, hence not ≅ R. So the hypothesis R \ X ≅ R fails, and we don't need to worry about this case.

The question is: when R^n \ X ≅ R^n (so R^n \ X is connected, etc.), does the one-point compactification argument work?

Let me reconsider. If R^n \ X ≅ R^n, then (R^n \ X)^+ ≅ S^n. But (R^n \ X)^+ might not be S^n \ X (subspace topology). So I can't directly conclude S^n \ X ≅ S^n.

Hmm, so I need a different approach.

Let me think about this differently. 

Alternative approach: Use homology of the complement directly.

If X is closed in R^n (which we get from invariance of domain) and 0-dimensional, can we compute the homology of R^n \ X?

For X compact: Alexander duality gives H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X). And S^n \ X = (R^n \ X) ∪ {∞}. If R^n \ X ≅ R^n, then R^n \ X is contractible, so H̃_i(R^n \ X) = 0 for all i. 

Now S^n \ X = (R^n \ X) ∪ {∞}. The relationship between H_*(S^n \ X) and H_*(R^n \ X): S^n \ X is the one-point compactification of R^n \ X only if R^n \ X is locally compact and the topologies match, which we've seen might not be the case.

But actually, S^n \ X = (R^n \ X) ⊔ {∞} as a set, and the subspace topology from S^n. If X is closed in R^n, then R^n \ X is open in R^n, and S^n \ X is open in S^n (since X is closed in S^n when X is compact, or... if X is closed in R^n but unbounded, X is not closed in S^n).

Hmm, let me separate cases again.

Case 1: X is compact (closed and bounded in R^n).
Then X is closed in S^n. S^n \ X is open in S^n. By Alexander duality:
H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X).
X is 0-dimensional compact. H̃^0(X) = c(X) - 1 (c = number of components), H̃^j(X) = 0 for j ≥ 1.
So H̃_{n-1}(S^n \ X) = c(X) - 1, and H̃_i(S^n \ X) = 0 for i ≠ 0, n-1 (and i ≠ n).

Now S^n \ X = (R^n \ X) ∪ {∞}. We can relate this to R^n \ X. Note that S^n \ X is the union of R^n \ X and {∞}, and {∞} is an open subset of S^n \ X (since X is compact, ∞ is an interior point of S^n \ X). Also, R^n \ X is open in S^n \ X. And (R^n \ X) ∩ {∞} = ∅. So S^n \ X = (R^n \ X) ⊔ {∞} (disjoint union of open sets)? No, {∞} is a single point, which is open in S^n \ X (since X compact ⟹ ∞ has a neighborhood in S^n \ X, so {∞} is... no, {∞} is not open unless ∞ is isolated in S^n \ X, which happens iff X is compact, which it is, but {∞} being open means ∞ is an isolated point of S^n \ X, which means there's an open set in S^n containing ∞ and contained in S^n \ X, i.e., S^n \ (some compact set) ⊂ S^n \ X, i.e., X ⊂ some compact set, which is true since X is compact. So {∞} is open in S^n \ X.

Wait, that's not right. {∞} is open in S^n \ X iff there's an open set V in S^n with V ∩ (S^n \ X) = {∞}, i.e., V \ {∞} ⊂ X. V is a neighborhood of ∞ in S^n, so V = S^n \ C for some compact C ⊂ R^n. V \ {∞} = R^n \ C. So we need R^n \ C ⊂ X, i.e., R^n \ X ⊂ C. Since R^n \ X is open and C is compact, R^n \ X ⊂ C means R^n \ X is bounded, which means X contains the exterior of some ball, i.e., X is co-bounded. But X is 0-dimensional (totally disconnected), so X can't contain the exterior of a ball (which is connected for n ≥ 2). For n = 1, X could contain a ray, but a ray is 1-dimensional. So for 0-dimensional X, X can't be co-bounded (for n ≥ 1). So {∞} is NOT open in S^n \ X (for 0-dimensional compact X, n ≥ 1).

OK so S^n \ X is connected (for n ≥ 2, since S^n \ X is (n-1)-connected... actually for 0-dimensional compact X, S^n \ X is path-connected for n ≥ 2). And S^n \ X = (R^n \ X) ∪ {∞} where ∞ is a limit point of R^n \ X in S^n \ X.

So S^n \ X is a connected space, and R^n \ X is a dense open subset (dense because ∞ is a limit point).

Now, if R^n \ X ≅ R^n, then R^n \ X is contractible. What can we say about S^n \ X?

S^n \ X is obtained from R^n \ X by adding one point (∞). If R^n \ X ≅ R^n, then S^n \ X is obtained from R^n by adding one limit point. This is like a compactification of R^n. 

Hmm, but different compactifications of R^n give different spaces. The one-point compactification gives S^n. But S^n \ X might be a different compactification.

Actually, S^n \ X is a specific compactification of R^n \ X (the "end compactification" determined by how X sits in S^n). If R^n \ X ≅ R^n, then S^n \ X is a compactification of R^n. 

For X compact, S^n \ X is an open subset of S^n (since X is closed in S^n). It's an open subset of S^n that contains ∞ and is connected. By Alexander duality, H̃_{n-1}(S^n \ X) = c(X) - 1.

If R^n \ X ≅ R^n (contractible), what is H̃_{n-1}(S^n \ X)?

We can use the long exact sequence. S^n \ X = (R^n \ X) ∪ {∞}. Consider the pair (S^n \ X, R^n \ X). The relative homology H_*(S^n \ X, R^n \ X) ≅ H̃_{*-1}(point) by... hmm, (S^n \ X) / (R^n \ X) = {∞} (a point) if R^n \ X is closed in S^n \ X. But R^n \ X is open in S^n \ X (and dense), not closed. So the quotient is not a point.

This approach is getting complicated. Let me try a different angle.

Alternative: Use the fact that R^n \ X ≅ R^n implies specific topological properties, and derive a contradiction if X is nonempty.

Key property: R^n is contractible. So R^n \ X is contractible. 

For n ≥ 2 and X compact 0-dimensional nonempty: By Alexander duality, H̃_{n-1}(S^n \ X) = c(X) - 1 ≥ 0. If c(X) ≥ 2, then H̃_{n-1}(S^n \ X) > 0.

Now, S^n \ X is an open subset of S^n containing ∞. We can write S^n \ X = (R^n \ X) ∪ {∞}. 

Consider the inclusion R^n \ X ↪ S^n \ X. If R^n \ X is contractible, what is the effect on homology?

Actually, let me use a different tool. Consider the long exact sequence of the pair (S^n, X):
... → H_i(X) → H_i(S^n) → H_i(S^n, X) → H_{i-1}(X) → ...
By excision, H_i(S^n, X) ≅ H_i(S^n \ X, {∞}) ... no, excision gives H_i(S^n, X) ≅ H_i(S^n \ X, U) for some neighborhood U of X... this is getting complicated.

Let me try yet another approach. 

Direct approach using homology of R^n \ X:

For X compact 0-dimensional in R^n (n ≥ 2), we can compute H_*(R^n \ X) using Alexander duality applied to S^n.

S^n \ X = (R^n \ X) ⊔ {∞} as a set, but topologically ∞ is a limit point. 

Actually, here's a cleaner way. Consider S^n with X ⊂ R^n ⊂ S^n, X compact. Let Y = S^n \ X. Y is an open subset of S^n. Y = (R^n \ X) ∪ {∞}. 

Now ∞ ∈ Y, and Y is an n-manifold (open subset of S^n). R^n \ X is also an n-manifold (open subset of R^n, since X is closed). 

The point ∞ in Y has a neighborhood in Y homeomorphic to R^n (since Y is an n-manifold). Specifically, a neighborhood of ∞ in Y is S^n \ C for some compact C ⊂ R^n with C ⊃ X, and S^n \ C ≅ R^n (stereographic projection from a point in C). So ∞ has a neighborhood in Y homeomorphic to R^n.

Now, Y = (R^n \ X) ∪ {∞}, and ∞ has a neighborhood in Y that's homeomorphic to R^n and doesn't intersect X. So locally near ∞, Y looks like R^n.

If R^n \ X ≅ R^n, then Y = (something ≅ R^n) ∪ {∞} where ∞ is attached in a specific way. 

Hmm, I think I need to use a more sophisticated tool. Let me think about the homology of R^n \ X directly.

For X compact in R^n: Use the fact that R^n \ X = S^n \ (X ∪ {∞}) = S^n \ X* where X* = X ∪ {∞} is compact in S^n. By Alexander duality:
H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).

X* = X ∪ {∞}. X is 0-dimensional compact, and ∞ is an isolated point of X* (since X is compact, ∞ has a neighborhood in S^n not meeting X, so ∞ is isolated in X*). So X* = X ⊔ {∞} (topological disjoint union). 

H̃^0(X*) = H̃^0(X ⊔ {∞}) = (c(X) + 1) - 1 = c(X) (where c(X) = number of components of X). Wait: H̃^0 of a space with k components is k - 1. X* has c(X) + 1 components (c(X) from X plus 1 from {∞}). So H̃^0(X*) = c(X) + 1 - 1 = c(X). And H̃^j(X*) = 0 for j ≥ 1.

So H̃_i(R^n \ X) ≅ H̃^{n-i-1}(X*):
- i = n-1: H̃_{n-1}(R^n \ X) = H̃^0(X*) = c(X).
- i ≠ n-1, i ≠ 0: H̃_i(R^n \ X) = 0.
- i = 0: H̃_0(R^n \ X) = H̃^{n-1}(X*) = 0 (for n ≥ 2).

So for n ≥ 2, X compact 0-dimensional:
H̃_{n-1}(R^n \ X) = c(X) (number of components of X).
All other reduced homology is 0.

If R^n \ X ≅ R^n (contractible), then H̃_i(R^n \ X) = 0 for all i. So c(X) = 0, meaning X has 0 components, i.e., X = ∅!

This is the key result. For n ≥ 2 and X compact, R^n \ X ≅ R^n ⟹ X = ∅.

Now for n = 1: X compact 0-dimensional in R. X* = X ∪ {∞} in S^1. H̃_0(R \ X) = H̃^0(X*) = c(X). If R \ X ≅ R (connected), H̃_0(R \ X) = 0, so c(X) = 0, X = ∅. ✓

And for n = 1, we also need R \ X to be connected, which already forces X = ∅ (as argued earlier). But the homology argument also works.

Now, what about X not compact? We showed X must be closed (invariance of domain). But X could be closed and unbounded.

For X closed and unbounded in R^n: X* = cl_{S^n}(X) = X ∪ {∞} (since X is unbounded, ∞ is a limit point). X* is compact (closed in S^n). 

R^n \ X = S^n \ X* (since S^n \ X* = S^n \ (X ∪ {∞}) = (R^n \ X) ∩ (S^n \ {∞}) = R^n \ X). Wait: S^n \ (X ∪ {∞}) = (S^n \ X) \ {∞} = ((R^n \ X) ∪ {∞}) \ {∞} = R^n \ X. Yes! So R^n \ X = S^n \ X*.

By Alexander duality: H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).

Now X* = X ∪ {∞} where ∞ is a limit point of X (not isolated). X is 0-dimensional. What is the dimension of X*? 

X* is the one-point compactification of X (if X is locally compact) or just the closure in S^n. X is 0-dimensional and closed in R^n. If X is unbounded, X is not compact, but it's locally compact (closed subset of R^n is locally compact). So X* = X^+ (one-point compactification of X). 

The dimension of X*: the one-point compactification of a 0-dimensional locally compact space is 0-dimensional (I believe this is true for non-compact spaces; the one-point compactification of a 0-dimensional locally compact non-compact space is 0-dimensional). 

Hmm, actually I need to check this. If X is 0-dimensional locally compact non-compact, is X^+ 0-dimensional? 

X^+ = X ∪ {∞}. For X^+ to be 0-dimensional, every point needs a clopen neighborhood. For points in X, they have clopen neighborhoods in X (since X is 0-dimensional), and these are also clopen in X^+ if they're compact (clopen compact subsets of X are clopen in X^+). Since X is locally compact and 0-dimensional, every point has a compact clopen neighborhood. So points in X have clopen neighborhoods in X^+. 

For ∞: ∞ has a neighborhood basis of sets X^+ \ K for K compact in X. X^+ \ K is clopen in X^+ iff K is clopen in X^+... hmm, X^+ \ K is open (by definition of one-point compactification). Is it closed? X^+ \ K is closed iff K is open in X^+. K is open in X^+ iff K is open in X (and K ⊂ X). So X^+ \ K is clopen iff K is clopen in X (and compact). Since X is 0-dimensional and locally compact, we can find compact clopen K containing any given compact set... actually, we need: for any compact K' in X, there's a compact clopen K in X with K' ⊂ K. Then X^+ \ K is a clopen neighborhood of ∞ contained in X^+ \ K'. 

Is this true? In a 0-dimensional locally compact space, every compact set is contained in a compact clopen set. I believe this is true for locally compact Hausdorff 0-dimensional spaces (they have a basis of compact clopen sets, and compact sets can be covered by finitely many, whose union is compact clopen). 

Actually, let me verify: X is 0-dimensional locally compact Hausdorff. Then X has a basis of compact clopen sets (since 0-dimensional gives clopen basis, and locally compact gives compact neighborhoods; combining, we get compact clopen neighborhoods). For a compact set K' in X, cover K' with finitely many compact clopen sets U_1, ..., U_m. Their union U = U_1 ∪ ... ∪ U_m is clopen (finite union of clopen is clopen) and compact (finite union of compact). And K' ⊂ U. ✓

So X^+ is 0-dimensional. Therefore X* = X^+ is 0-dimensional (compact).

Now apply Alexander duality: H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).

X* is 0-dimensional compact. H̃^0(X*) = c(X*) - 1 (number of components minus 1). H̃^j(X*) = 0 for j ≥ 1.

So H̃_{n-1}(R^n \ X) = H̃^0(X*) = c(X*) - 1.

If R^n \ X ≅ R^n (contractible), H̃_{n-1}(R^n \ X) = 0, so c(X*) = 1, meaning X* is connected.

X* is 0-dimensional and connected, so X* is a single point. 

X* = X ∪ {∞}. If X* is a single point, then X* = {∞}, so X = ∅. (Because if X is nonempty, X* has at least 2 points: some point of X and ∞.)

Wait, X* = X ∪ {∞}. If X ≠ ∅, then X* has at least 2 points (∞ and some point of X). A 0-dimensional connected space with ≥ 2 points is impossible (0-dimensional Hausdorff spaces are totally disconnected, so connected components are points). So X* connected and 0-dimensional ⟹ X* is a single point ⟹ X = ∅. ✓

So in all cases (X compact or unbounded), R^n \ X ≅ R^n ⟹ X = ∅.

Let me also handle n = 1 with this approach. For n = 1, X closed 0-dimensional in R. 

If X compact: X* = X ∪ {∞} (disjoint, ∞ isolated). H̃_0(R \ X) = H̃^0(X*) = c(X*). Wait, for n=1: H̃_i(R \ X) = H̃^{1-i-1}(X*) = H̃^{-i}(X*). 

Hmm, for n=1: H̃_i(S^1 \ X*) ≅ H̃^{1-i-1}(X*) = H̃^{-i}(X*).

For i=0: H̃_0(S^1 \ X*) = H̃^0(X*) = c(X*) - 1.
For i=1: H̃_1(S^1 \ X*) = H̃^{-1}(X*) = Z if X* = ∅, 0 otherwise.

R \ X = S^1 \ X*. If R \ X ≅ R (contractible, connected), H̃_0 = 0, so c(X*) = 1. X* 0-dimensional connected ⟹ single point. If X compact, X* = X ⊔ {∞}, c(X*) = c(X) + 1. c(X*) = 1 ⟹ c(X) = 0 ⟹ X = ∅. ✓

If X unbounded: X* = X ∪ {∞} (∞ is limit point). X* 0-dimensional compact. c(X*) = 1 ⟹ X* = {pt} ⟹ X = ∅. ✓

Great, so the argument works for all n ≥ 1.

Let me also handle n = 0. R^0 = {pt}. 0-dimensional subset X of R^0: X = ∅ or X = {pt}. R^0 \ ∅ = {pt} ≅ R^0. R^0 \ {pt} = ∅ ≇ R^0. So X = ∅. (Trivial case, and our argument with S^0 doesn't directly apply since S^0 is disconnected, but the result holds.)

Now let me also verify the key step: Alexander duality for X* compact in S^n.

Alexander duality (for compact locally contractible... or more generally for compact subsets): For any compact subset K of S^n:
H̃_i(S^n \ K) ≅ H̃^{n-i-1}(K) for all i.
This is the Alexander duality theorem, which holds for all compact subsets K of S^n (using Čech cohomology). ✓

And 0-dimensional compact spaces have trivial Čech cohomology above degree 0, and H̃^0 = (number of components) - 1. ✓ (For compact Hausdorff spaces, Čech cohomology agrees with sheaf cohomology, and for 0-dimensional spaces, H̃^0 = number of connected components - 1, H̃^j = 0 for j > 0.)

Actually, I should be careful: for 0-dimensional compact spaces, the number of connected components equals the number of points (since totally disconnected), so c(X*) = |X*| (number of points). But we don't need this; we just need c(X*) = 1 ⟹ X* is a point.

Hmm wait, for a 0-dimensional compact space, connected components are points (totally disconnected), so c(X*) = |X*|. c(X*) = 1 ⟹ |X*| = 1 ⟹ X* is a single point. ✓

OK so the proof is:

1. Suppose R^n \ X ≅ R^n. 
2. By invariance of domain, R^n \ X is open in R^n, so X is closed in R^n.
3. Let X* = cl_{S^n}(X) (closure in the one-point compactification S^n of R^n). Then X* is compact, and R^n \ X = S^n \ X*.
4. X is 0-dimensional and closed in R^n (hence locally compact). X* is the one-point compactification of X (if X non-compact) or X ⊔ {∞} (if X compact). In either case, X* is 0-dimensional and compact.
5. By Alexander duality: H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).
6. X* is 0-dimensional compact, so H̃^j(X*) = 0 for j ≥ 1, and H̃^0(X*) = c(X*) - 1.
7. So H̃_{n-1}(R^n \ X) = c(X*) - 1, and all other reduced homology of R^n \ X is 0 (for n ≥ 2; for n = 1, H̃_0(R \ X) = c(X*) - 1).
8. R^n \ X ≅ R^n is contractible, so H̃_i(R^n \ X) = 0 for all i.
9. Therefore c(X*) - 1 = 0, so c(X*) = 1.
10. X* is 0-dimensional and compact, hence totally disconnected. c(X*) = 1 means X* is connected, so X* is a single point.
11. X* = X ∪ {∞}. If X ≠ ∅, then |X*| ≥ 2 (contains ∞ and a point of X). So X* being a single point means X = ∅.

Therefore X = ∅. The answer is YES.

Wait, I need to double-check step 4 more carefully. Is X* always 0-dimensional?

Case 1: X is compact (bounded). Then X* = X ∪ {∞} where ∞ is an isolated point (since X is compact, there's a neighborhood of ∞ in S^n not meeting X). So X* = X ⊔ {∞} (topological sum). X is 0-dimensional, {∞} is 0-dimensional, so X* is 0-dimensional. ✓

Case 2: X is unbounded (closed in R^n but not compact). Then X* = X ∪ {∞} where ∞ is a limit point of X. X is locally compact (closed in R^n) and 0-dimensional. X* is the one-point compactification X^+ of X. As argued, X^+ is 0-dimensional (since X is locally compact Hausdorff 0-dimensional). ✓

But wait, is X locally compact? X is closed in R^n. A closed subset of a locally compact Hausdorff space is locally compact. R^n is locally compact Hausdorff. So X is locally compact. ✓

And is X 0-dimensional in the sense that gives X^+ 0-dimensional? X is 0-dimensional (covering dimension 0), which for separable metric spaces means it has a basis of clopen sets. Combined with locally compact, X has a basis of compact clopen sets. Then X^+ is 0-dimensional as argued. ✓

Hmm, but actually I want to make sure X has a basis of compact clopen sets. X is 0-dimensional (has clopen basis) and locally compact (has compact neighborhoods). For each point x and neighborhood U of x, there's a clopen V with x ∈ V ⊂ U, and a compact neighborhood K of x with K ⊂ V. Then x ∈ int(K) ∩ V, which is open. There's a clopen W with x ∈ W ⊂ int(K) ∩ V. W is clopen in X, W ⊂ K (compact), so W is compact (closed subset of compact K, and W is closed since clopen). So W is a compact clopen neighborhood of x inside U. ✓

So X has a basis of compact clopen sets, and X^+ is 0-dimensional. ✓

Also, I should verify step 3: R^n \ X = S^n \ X*.

S^n = R^n ∪ {∞}. X ⊂ R^n. X* = cl_{S^n}(X). 

If X is compact: X* = X (X is already closed in S^n since compact subsets of R^n are closed in S^n... wait, is that right? X compact in R^n ⟹ X is closed in R^n and bounded. In S^n, X is closed iff X is compact (as a subset of S^n). X is compact as a subset of S^n iff X is compact as a subset of R^n (since S^n is Hausdorff and X ⊂ R^n ⊂ S^n, compactness is the same). So X is closed in S^n. So X* = X. Then S^n \ X* = S^n \ X = (R^n \ X) ∪ {∞}. But R^n \ X = S^n \ (X ∪ {∞}) = (S^n \ X) \ {∞} = (R^n \ X) ∪ {∞} \ {∞} = R^n \ X. Hmm, that's circular.

Let me redo. S^n \ X* = S^n \ X (since X* = X when X compact). S^n \ X = (R^n \ X) ∪ {∞} (since ∞ ∉ X). But R^n \ X is what we want, not (R^n \ X) ∪ {∞}. 

So R^n \ X ≠ S^n \ X* when X is compact. Instead, R^n \ X = S^n \ (X ∪ {∞}) = S^n \ X* where X* = X ∪ {∞}.

Hmm, I think I confused myself. Let me redefine.

Let X* = X ∪ {∞} (as a subset of S^n, always adding ∞). Then:
S^n \ X* = S^n \ (X ∪ {∞}) = (S^n \ X) ∩ (S^n \ {∞}) = (S^n \ X) ∩ R^n = R^n \ X. ✓

So R^n \ X = S^n \ X* where X* = X ∪ {∞}. This is always true, regardless of whether X is compact.

Now X* = X ∪ {∞}. Is X* compact? X* is compact iff X* is closed in S^n. X* = X ∪ {∞}. X is closed in R^n (from invariance of domain). 

If X is bounded (compact): X is closed in S^n, and {∞} is closed in S^n, so X* = X ∪ {∞} is closed in S^n, hence compact. ✓

If X is unbounded: X is closed in R^n but not in S^n (closure in S^n is X ∪ {∞} = X*). So X* = cl_{S^n}(X), which is closed in S^n, hence compact. ✓

So X* is always compact. ✓

And X* is 0-dimensional:
- If X compact: X* = X ⊔ {∞} (∞ isolated), both 0-dimensional, so X* is 0-dimensional. ✓
- If X unbounded: X* = cl_{S^n}(X) = X ∪ {∞} = X^+ (one-point compactification of X, since X is locally compact non-compact). X^+ is 0-dimensional as argued. ✓

Now Alexander duality: H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*). And S^n \ X* = R^n \ X. So H̃_i(R^n \ X) ≅ H̃^{n-i-1}(X*). ✓

X* is 0-dimensional compact. H̃^0(X*) = c(X*) - 1, H̃^j(X*) = 0 for j ≥ 1.

H̃_{n-1}(R^n \ X) = H̃^0(X*) = c(X*) - 1.
H̃_i(R^n \ X) = 0 for i ≠ n-1 (and i ≥ 1). (For n ≥ 2.)
For n = 1: H̃_0(R \ X) = H̃^0(X*) = c(X*) - 1.

R^n \ X ≅ R^n ⟹ contractible ⟹ H̃_i = 0 for all i ⟹ c(X*) = 1.

X* 0-dimensional compact ⟹ totally disconnected ⟹ c(X*) = |X*| (number of points). c(X*) = 1 ⟹ |X*| = 1 ⟹ X* = {∞} (since ∞ ∈ X*) ⟹ X = ∅. ✓

The proof is complete. Let me write it up cleanly.

Actually, let me reconsider one thing: for n=1, the reduced homology. H̃_0(R \ X) = c(X*) - 1. R \ X ≅ R means R \ X is connected, so H̃_0(R \ X) = 0, so c(X*) = 1. Same conclusion. ✓

And for n=1, H̃_i(R \ X) for i ≥ 1: H̃_i = H̃^{-i}(X*) = 0 for i ≥ 1 (since -i < 0 and X* is nonempty). R is contractible so H̃_i = 0 for i ≥ 1. ✓ Consistent.

Now let me also think about whether I need X to be nonempty for the argument. If X = ∅, then X* = {∞}, c(X*) = 1, H̃_{n-1}(R^n) = 0 = c(X*) - 1 = 0. ✓ Consistent. And R^n \ ∅ = R^n ≅ R^n. ✓

So the argument shows: R^n \ X ≅ R^n ⟺ X = ∅ (for 0-dimensional X). The forward direction is what we proved. The backward direction is trivial.

Let me write the final proof.

One more check: the problem says "0-dimensional subset." I'm interpreting this as covering dimension 0. For subsets of R^n (separable metric spaces), this is equivalent to having a basis of clopen sets, which implies totally disconnected. The key properties I use:
1. 0-dimensional ⟹ totally disconnected (for the empty interior argument, though I ended up not needing this in the final proof).
2. 0-dimensional compact ⟹ H̃^j = 0 for j ≥ 1, H̃^0 = c - 1 (Čech cohomology).
3. 0-dimensional locally compact ⟹ one-point compactification is 0-dimensional.

All of these are standard results in dimension theory.

Actually, in the final proof, I don't even need the "empty interior" argument or invariance of domain! Let me re-examine.

Wait, I do need X to be closed for X* to be well-behaved... actually no. X* = X ∪ {∞} is always compact (as shown). And X* is 0-dimensional... but is X* 0-dimensional if X is not closed?

If X is not closed in R^n, then X is not locally compact (a non-closed subset of a Hausdorff locally compact space is not locally compact... actually that's not true. A subset of a locally compact Hausdorff space is locally compact iff it's the intersection of an open set and a closed set, i.e., locally closed). 

If X is not closed, X might not be locally compact, and X* = X ∪ {∞} might not be the one-point compactification, and might not be 0-dimensional.

Hmm, but actually X* = X ∪ {∞} as a subset of S^n. Is X* 0-dimensional? 

If X is not closed, let X̄ = cl_{R^n}(X). Then X* = cl_{S^n}(X) = X̄ ∪ {∞} (if X is unbounded) or X̄ (if X is bounded). Wait, X* = X ∪ {∞}, not cl_{S^n}(X). Let me re-examine.

I defined X* = X ∪ {∞} (just the set X plus the point ∞). This is a subset of S^n. Is it compact? X* is compact iff X* is closed in S^n. X* = X ∪ {∞}. 

If X is not closed in R^n: X ∪ {∞} is closed in S^n iff (X ∪ {∞}) ∩ R^n = X is closed in R^n (since S^n \ {∞} = R^n is open, a subset of S^n containing ∞ is closed iff its intersection with R^n is closed in R^n... actually that's not quite right either).

Let me think about it directly. X* = X ∪ {∞} is closed in S^n iff S^n \ X* = R^n \ X is open in S^n. R^n \ X is open in S^n iff R^n \ X is open in R^n (since R^n is open in S^n) and... no, a subset of S^n is open iff it's open in the topology of S^n. R^n \ X is open in S^n iff for every point p ∈ R^n \ X, there's an open set in S^n containing p and contained in R^n \ X. Since R^n is open in S^n, open sets in R^n are open in S^n. So R^n \ X is open in S^n iff R^n \ X is open in R^n iff X is closed in R^n.

So if X is not closed in R^n, X* = X ∪ {∞} is NOT closed in S^n, hence not compact. Then Alexander duality doesn't apply directly.

So I DO need X to be closed, and I get that from invariance of domain. Good.

So the proof structure is:
1. R^n \ X ≅ R^n ⟹ (by invariance of domain) R^n \ X is open in R^n ⟹ X is closed in R^n.
2. X closed in R^n, 0-dimensional ⟹ X is locally compact, X* = X ∪ {∞} is compact and 0-dimensional.
3. R^n \ X = S^n \ X* (set-theoretically and topologically).
4. Alexander duality: H̃_i(R^n \ X) ≅ H̃^{n-i-1}(X*).
5. X* 0-dimensional compact ⟹ H̃^{n-i-1}(X*) = 0 except when n-i-1 = 0, i.e., i = n-1, where it's c(X*) - 1.
6. R^n \ X ≅ R^n ⟹ contractible ⟹ H̃_i = 0 for all i ⟹ c(X*) = 1.
7. X* 0-dimensional compact ⟹ totally disconnected ⟹ c(X*) = |X*| ⟹ |X*| = 1 ⟹ X* = {∞} ⟹ X = ∅.

This is clean. Let me write it up.

Hmm, actually one more thing. For step 2, when X is compact (bounded), X* = X ∪ {∞} where ∞ is isolated. X* is the topological disjoint union X ⊔ {∞}. X is 0-dimensional, {∞} is 0-dimensional, so X* is 0-dimensional. And X* is compact (closed in S^n). ✓

When X is unbounded, X* = X ∪ {∞} = X^+ (one-point compactification of X, since X is locally compact non-compact). X^+ is 0-dimensional (as argued). And X^+ is compact. ✓

Also, I should verify that X* = X ∪ {∞} being compact implies it's closed in S^n (which it is, since S^n is Hausdorff and compact subsets are closed). And then S^n \ X* = R^n \ X is open in S^n, hence open in R^n. This is consistent with step 1.

Actually, I realize that step 1 (invariance of domain) gives X closed, and then X* is compact (closed in S^n), and Alexander duality applies. But actually, do I even need invariance of domain? If I just define X* = cl_{S^n}(X) (the closure, not just X ∪ {∞}), then X* is always compact (closed in S^n). But then S^n \ X* might not equal R^n \ X (it would be R^n \ cl_{R^n}(X) if X is bounded, or something else).

So I do need invariance of domain to ensure X is closed, so that X* = X ∪ {∞} is compact and S^n \ X* = R^n \ X.

Alternatively, I could use cl_{S^n}(X) and note that S^n \ cl_{S^n}(X) ⊂ R^n \ X, but the inclusion might be strict if X is not closed. So invariance of domain is needed.

OK, I'm confident the proof is correct. Let me write it up.

Let me also think about whether there's a simpler proof that doesn't use Alexander duality or invariance of domain.

Simpler approach for n=1: R \ X ≅ R means R \ X is connected. R \ X ⊂ R \ {p} for any p ∈ X. R \ {p} has two components. If X is nonempty, R \ X is a subset of R \ {p} that doesn't contain p, so it's contained in the union of two separated intervals, hence disconnected (as long as X is nonempty and 0-dimensional, which means X doesn't contain an interval, so R \ X intersects both components). So X = ∅. This is elementary.

For n ≥ 2: The homology argument via Alexander duality seems necessary. I don't think there's a purely elementary argument.

Actually, for n=2, one could use the fundamental group. If X is nonempty and compact, take p ∈ X. A small loop around p in R^2 \ X is non-contractible (it links with p). So π_1(R^2 \ X) ≠ 0, but π_1(R^2) = 0. But this requires X to be "nice enough" that a loop around p doesn't contract, which needs some argument. And for non-compact X, it's trickier. The Alexander duality approach is cleaner and works for all n.

Let me write the final proof now.

Actually, I want to make sure about one subtle point: the use of Čech cohomology in Alexander duality. The standard Alexander duality theorem states:

For any compact subset K of S^n:
H̃_i(S^n \ K; G) ≅ H̃^{n-i-1}(K; G) for all i,
where the right side is Čech cohomology.

For 0-dimensional compact Hausdorff spaces, Čech cohomology: H̃^0(K) = (number of connected components) - 1, and H̃^j(K) = 0 for j ≥ 1. This is because 0-dimensional spaces have a basis of clopen sets, so the Čech complex is trivial in positive degrees.

Actually, for a 0-dimensional compact space, connected components = points (totally disconnected), so the number of components = cardinality of K. But we don't need the exact count, just that c(X*) = 1 implies X* is a point.

Also, I should note: for a totally disconnected compact space, H̃^0 = |K| - 1 (number of points minus 1) since each point is a component. So H̃^0(X*) = |X*| - 1. Setting this to 0 gives |X*| = 1.

Wait, but X* might be uncountable. H̃^0 for a compact space with infinitely many components... H̃^0(K) is the group of locally constant functions on K modulo constants, which for a totally disconnected compact space is related to the Boolean algebra of clopen sets. For a finite space with k points, H̃^0 = k - 1 (as a group, Z^{k-1}). For an infinite totally disconnected compact space, H̃^0 is more complicated (it's not just |K| - 1).

Hmm, so I need to be more careful. H̃^0(X*) = 0 means X* is connected. For a 0-dimensional (        — AI历史解题过程（thinking）
#   deepmath_103k_00029409         — 题目ID

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
  <problem_id>deepmath_103k_00029409</problem_id>
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

Calculate the limit: \( \lim_{x\to0} \sum_{n=1}^\infty \frac{\sin x}{4+n^4x^4} \)

## Standard Solution

Okay, so I need to find the limit as x approaches 0 of the sum from n=1 to infinity of sin(x) divided by (4 + n^4x^4). Hmm, let me start by understanding the problem. It's a limit of an infinite series as x approaches 0. The terms of the series are sin(x)/(4 + n^4x^4). 

First, let me note that when x approaches 0, sin(x) is approximately x. So maybe I can approximate sin(x) with x for small x. That might simplify things a bit. So replacing sin(x) with x, the term becomes x/(4 + n^4x^4). 

But wait, since x is approaching 0, I need to see how each term in the series behaves as x approaches 0. Let's look at a general term: for each fixed n, as x approaches 0, the denominator 4 + n^4x^4 approaches 4. So each term approaches sin(x)/4. But if I sum this over all n from 1 to infinity, sin(x)/4 summed infinitely would diverge because it's just adding a constant term infinitely. But that seems contradictory because the original sum might converge. So maybe my initial thought is wrong.

Wait, but if x is approaching 0, even though each term sin(x)/(4 + n^4x^4) approaches sin(x)/4, the sum might not necessarily diverge because as x approaches 0, sin(x) also approaches 0. So maybe the sum is something like a small number times an infinite series. Hmm, indeterminate form? Maybe 0 times infinity? So I need to analyze this more carefully.

Alternatively, maybe I can switch the limit and the summation. If that's allowed, then the limit would be the sum of the limits. So, interchanging limit and summation would give sum_{n=1}^\infty [lim_{x->0} sin(x)/(4 + n^4x^4)]. But lim_{x->0} sin(x)/(4 + n^4x^4) = lim_{x->0} sin(x)/4 = 0, since n^4x^4 goes to 0. Therefore, each term's limit is 0, so the sum would be 0 + 0 + 0 + ... = 0. So would the limit be 0?

But I need to be careful here because interchanging limits and infinite sums requires uniform convergence or some other condition. Maybe I need to justify that interchange. Alternatively, perhaps there's another approach.

Alternatively, think of the sum as an approximation of an integral when x is small. Since n is going to infinity, and x is approaching 0, maybe setting nx = t or something. Let me try a substitution. Let’s let t = n x. Then, as x approaches 0, for fixed t, n would be t/x, which goes to infinity. But since n is an integer, maybe we can approximate the sum by an integral over t.

Wait, this is similar to converting a Riemann sum into an integral. Let me think. If we set t_n = n x, then when x is small, the spacing between t_n and t_{n+1} is x. So the sum over n multiplied by x can approximate an integral over t. But in our case, the term is sin(x)/(4 + (t_n)^4). So the sum is sin(x) * sum_{n=1}^\infty 1/(4 + (n x)^4). If x is approaching 0, sin(x) ~ x, so the sum is approximately x * sum_{n=1}^\infty 1/(4 + (n x)^4). Then, if we let x approach 0, the sum can be approximated by x * sum_{n=1}^\infty 1/(4 + (n x)^4) ≈ x * integral_{t=0}^\infty 1/(4 + t^4) dt. Because as x approaches 0, the sum becomes a Riemann sum for the integral, with step size x.

Therefore, the limit would be lim_{x->0} x * integral_{t=0}^\infty 1/(4 + t^4) dt. But wait, integral_{t=0}^\infty 1/(4 + t^4) dt is a constant, so multiplying by x would give 0. Therefore, the limit is 0. But is that correct?

Wait, hold on. Let's check. The original expression is sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4). If we approximate sin(x) ~ x, then it's x * sum_{n=1}^\infty 1/(4 + n^4 x^4). Then, we can make substitution t = n x, so n = t / x. Then, the sum over n is sum_{n=1}^\infty 1/(4 + t^4) * x, since Δt = x. Therefore, the sum becomes approximately integral_{t=0}^\infty 1/(4 + t^4) dt. So the total expression becomes x * [integral_{t=0}^\infty 1/(4 + t^4) dt] / x = integral_{t=0}^\infty 1/(4 + t^4) dt. Wait, but that contradicts the previous conclusion. Wait, no, maybe substitution is different.

Wait, when we set t = n x, then as x approaches 0, n has to go to infinity to keep t finite. But in the sum, n starts from 1, so t starts from x. So as x approaches 0, the lower limit of t approaches 0. So the sum sum_{n=1}^\infty x/(4 + (n x)^4) is a Riemann sum for the integral from t=0 to t=infty of 1/(4 + t^4) dt. Because each term is x * f(n x), where f(t) = 1/(4 + t^4). So the sum is approximately the integral of f(t) from 0 to infinity as x approaches 0.

Therefore, the sum sum_{n=1}^\infty 1/(4 + (n x)^4) ≈ (1/x) * integral_{0}^\infty 1/(4 + t^4) dt. Then, multiplying by sin(x) ~ x, we get x * (1/x) * integral ... = integral. Therefore, the limit would be equal to integral_{0}^\infty 1/(4 + t^4) dt.

Wait, but this contradicts my previous thought. Wait, so perhaps the limit is actually equal to that integral? Let me check again.

Original expression: lim_{x->0} sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4).

Approximate sin(x) as x, so expression becomes x * sum_{n=1}^\infty 1/(4 + n^4 x^4).

Set t_n = n x, so t_n = x, 2x, 3x, ... Then the sum sum_{n=1}^\infty x/(4 + t_n^4) is a Riemann sum for the integral from t=0 to t=infty of 1/(4 + t^4) dt. Because each term is (t_{n+1} - t_n) * f(t_n), where the step size is x. So as x approaches 0, the Riemann sum approaches the integral. Therefore, the sum sum_{n=1}^\infty x/(4 + (n x)^4) approaches integral_{0}^\infty 1/(4 + t^4) dt. Therefore, the original expression, which is approximately x * sum ... becomes x * (1/x) * integral ... = integral.

But wait, no. Wait, the sum is sum_{n=1}^\infty x/(4 + (n x)^4). So each term is x * [1/(4 + (n x)^4)]. So as x approaches 0, this sum approaches the integral from t=0 to infinity of 1/(4 + t^4) dt. Therefore, the entire expression sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4) is approximately x * [ (1/x) * integral ... ] = integral. Therefore, the limit is the value of the integral.

Therefore, the answer should be integral_{0}^\infty 1/(4 + t^4) dt. Now, need to compute that integral.

Wait, but I need to verify this reasoning. Because if I have sum_{n=1}^\infty x/(4 + (n x)^4), and as x approaches 0, this becomes the integral from t=0 to infinity of 1/(4 + t^4) dt. So the sum is equal to (1/x) sum_{n=1}^\infty [x / (4 + (n x)^4)] which is the Riemann sum for the integral. Therefore, sum_{n=1}^\infty x / (4 + (n x)^4) ≈ integral_{0}^\infty 1/(4 + t^4) dt. Therefore, multiplying by sin(x) ~ x, the original expression is approximately x * integral, but wait, no. Wait, the original expression is sin(x) times the sum. So if the sum is approximately (1/x) integral, then sin(x) ~ x, so sin(x) * sum ~ x * (1/x) * integral = integral. Therefore, the limit is equal to the integral.

Therefore, the answer is the integral from 0 to infinity of 1/(4 + t^4) dt. Now, let's compute that integral.

To compute integral_{0}^\infty dt / (4 + t^4). Let me recall that integrals of the form ∫_{0}^\infty dx/(x^n + a^n) can be evaluated using beta or gamma functions. Alternatively, use substitution.

Let me try substitution. Let u = t^4 / 4. Then t = (4u)^{1/4}, dt = (4^{1/4}/4) u^{-3/4} du. Hmm, not sure if that helps.

Alternatively, use partial fractions or contour integration. Wait, maybe a standard integral formula.

Recall that ∫_{0}^\infty dx/(x^4 + a^4) = (π)/(2 a^3 sqrt(2)) ). Wait, not sure. Let me check.

Alternatively, use substitution. Let t = sqrt(2) u. Then, substitute t = sqrt(2) u, dt = sqrt(2) du. Then, integral becomes ∫_{0}^\infty sqrt(2) du / (4 + (sqrt(2) u)^4) = sqrt(2) ∫_{0}^\infty du / (4 + 4 u^4) = sqrt(2)/4 ∫_{0}^\infty du/(1 + u^4). 

Ah, so the integral becomes sqrt(2)/4 times ∫_{0}^\infty du/(1 + u^4). Now, I know that ∫_{0}^\infty du/(1 + u^4) = π/(2 sqrt(2)). Let me confirm that.

Yes, the integral ∫_{0}^\infty dx/(1 + x^4) can be computed using beta function. Let me recall that ∫_{0}^\infty x^{k - 1}/(1 + x^n) dx = (π/n)/sin(π k/n). For our case, n=4, k=1. So integral is (π/4)/sin(π/4) = (π/4)/(sqrt(2)/2) = π/(4) * 2/sqrt(2) = π/(2 sqrt(2)). Therefore, ∫_{0}^\infty dx/(1 + x^4) = π/(2 sqrt(2)).

Therefore, coming back, our integral was sqrt(2)/4 * π/(2 sqrt(2)) = (sqrt(2) * π)/(8 sqrt(2)) ) = π/8. 

Wait, let me check again:

Original substitution: t = sqrt(2) u. Then, t^4 = (sqrt(2))^4 u^4 = 4 u^4. So denominator becomes 4 + t^4 = 4 + 4 u^4 = 4(1 + u^4). Then, integral is ∫_{0}^\infty dt/(4 + t^4) = ∫_{0}^\infty sqrt(2) du / [4(1 + u^4)] = sqrt(2)/4 ∫_{0}^\infty du/(1 + u^4) = sqrt(2)/4 * π/(2 sqrt(2)) = (sqrt(2) * π)/(8 sqrt(2)) = π/8. 

Yes, that's correct. Therefore, the integral ∫_{0}^\infty dt/(4 + t^4) = π/8. Therefore, the limit is π/8. 

But wait, let me confirm once again the steps:

1. Original limit: lim_{x→0} sin(x) * sum_{n=1}^\infty 1/(4 + n^4 x^4).

2. Approximated sin(x) ~ x.

3. Converted the sum into a Riemann sum by substituting t = n x, leading to the integral ∫_{0}^\infty 1/(4 + t^4) dt.

4. Calculated the integral and found it to be π/8.

Therefore, the answer should be π/8. But before finalizing, let me check if interchanging the sum and the limit is valid here.

Alternatively, can we use the Dominated Convergence Theorem for series? For each fixed n, the term sin(x)/(4 + n^4 x^4) approaches 0 as x approaches 0. If we can dominate the terms by something summable, then by the Dominated Convergence Theorem, the limit can be interchanged with the sum.

But as x approaches 0, sin(x) ~ x, so |sin(x)/(4 + n^4 x^4)| ≤ x/(4 + n^4 x^4). Let me see if this is dominated by something summable. For x near 0, n^4 x^4 can be small or large depending on n.

But for each fixed x, when n is large enough such that n^4 x^4 ≥ 1, then 4 + n^4 x^4 ≥ n^4 x^4, so term is ≤ x/(n^4 x^4) = 1/(n^4 x^3). Wait, but as x approaches 0, 1/(n^4 x^3) becomes large for fixed n. So this approach might not work. Therefore, maybe Dominated Convergence is not directly applicable here.

Alternatively, use comparison. Let me split the sum into two parts: n ≤ N and n > N, where N is chosen such that n^4 x^4 is small for n ≤ N and x near 0.

But this seems vague. Alternatively, use the integral test. Compare sum_{n=1}^\infty 1/(4 + n^4 x^4) with integral_{n=1}^\infty 1/(4 + t^4 x^4) dt. The integral can be evaluated as substitution u = t x, so integral becomes (1/x) ∫_{x}^\infty 1/(4 + u^4) du. So as x approaches 0, (1/x) ∫_{0}^\infty 1/(4 + u^4) du. But this is similar to the previous reasoning. Therefore, the sum is asymptotic to (1/x) * π/8 as x approaches 0. Therefore, sin(x) * sum ~ x * (π/8 x^{-1}) = π/8. Therefore, the limit is π/8. Therefore, this confirms the previous result.

Therefore, despite the difficulty in interchanging the limit and the summation directly, by converting the sum into an integral through Riemann sums, we find that the limit is π/8. Therefore, the final answer is π/8.

**Final Answer**
\boxed{\dfrac{\pi}{8}}
</think>

To find the limit \( \lim_{x\to0} \sum_{n=1}^\infty \frac{\sin x}{4+n^4x^4} \), we start by approximating \(\sin x \approx x\) for small \(x\). This transforms the expression into \( x \sum_{n=1}^\infty \frac{1}{4 + n^4x^4} \).

Next, we convert the sum into a Riemann sum by substituting \( t = nx \). As \( x \to 0 \), the sum \( \sum_{n=1}^\infty \frac{x}{4 + (nx)^4} \) approximates the integral \( \int_{0}^\infty \frac{1}{4 + t^4} \, dt \).

To compute this integral, we use the substitution \( t = \sqrt{2}u \), leading to:
\[
\int_{0}^\infty \frac{dt}{4 + t^4} = \int_{0}^\infty \frac{\sqrt{2} \, du}{4(1 + u^4)} = \frac{\sqrt{2}}{4} \int_{0}^\infty \frac{du}{1 + u^4}
\]

The integral \( \int_{0}^\infty \frac{du}{1 + u^4} \) is known to be \( \frac{\pi}{2\sqrt{2}} \). Substituting this back, we get:
\[
\frac{\sqrt{2}}{4} \cdot \frac{\pi}{2\sqrt{2}} = \frac{\pi}{8}
\]

Thus, the limit is the value of this integral, confirming that the original expression converges to \( \frac{\pi}{8} \).

\[
\boxed{\dfrac{\pi}{8}}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks: Let X be a 0-dimensional subset of R^n. If U = R^n \ X is homeomorphic to R^n, does it imply X is empty?

Let me think about this carefully.

First, answer leak check: The problem text doesn't contain any solution or answer. It's a clean question. Good.

Now let me think about the mathematics.

A 0-dimensional subset of R^n. Here "0-dimensional" likely means topological dimension 0 (covering dimension / Lebesgue dimension). A 0-dimensional space is one where every point has arbitrarily small neighborhoods with empty boundary (clopen neighborhoods).

The question: if R^n \ X ≅ R^n (homeomorphic), must X be empty?

Let me think about examples.

For n=1: R \ X where X is 0-dimensional. If X is a single point, R \ {pt} is not connected, so not homeomorphic to R. If X is two points, also not connected. Actually for R, removing any nonempty set disconnects or... wait. R \ X where X is 0-dimensional. If X is nonempty, say contains a point p. Then R \ {p} is disconnected. But actually X could be a Cantor set (which is 0-dimensional). R \ Cantor set is... it's a union of intervals, not connected, so not homeomorphic to R (which is connected). Actually for n=1, R \ X connected requires X to be... R is connected, R\X connected means X doesn't separate R. For R, removing any point disconnects it. So R \ X connected implies X = empty. So for n=1, yes X must be empty.

But wait, the question is general n. For n ≥ 2, things are different.

For n=2: Consider X = a single point. R^2 \ {pt} ≅ S^1 × R ≅ cylinder, which is NOT homeomorphic to R^2 (e.g., fundamental group is Z vs trivial). So single point doesn't work.

What about X being something more clever?

Actually, there's a classical result. Let me think about whether there exists a nonempty 0-dimensional set X such that R^n \ X ≅ R^n.

Hmm, for n ≥ 3: R^n \ {pt} is simply connected (for n ≥ 3), and in fact R^n \ {pt} ≅ S^{n-1} × R. For n ≥ 3, is S^{n-1} × R ≅ R^n? No, because S^{n-1} × R has nontrivial homology H_{n-1} = Z, while R^n has trivial homology. So not homeomorphic.

But the question is about general 0-dimensional X, not just a point.

Let me think about this differently. There's a famous result by... I think the answer is YES, X must be empty, and this is related to the invariance of domain / dimension theory.

Actually wait. Let me reconsider. There's a classical theorem: if X is a closed subset of R^n and R^n \ X ≅ R^n, then... hmm.

Actually, let me think about the "cellular" sets. A set X in R^n is cellular if it has a nested sequence of closed n-cells (homeomorphic to closed balls) whose intersection is X. If X is cellular, then R^n \ X ≅ R^n by the cellularity criterion (this is a standard result in geometric topology).

A point is cellular. So R^n \ {pt} should be ≅ R^n? But I just argued it's not for n=2 because of fundamental group!

Wait, let me recheck. R^2 \ {0}. This deformation retracts to S^1. So π_1 = Z. R^2 is simply connected. So they're not homeomorphic. So a point is NOT cellular in the sense that gives R^n \ X ≅ R^n? 

Hmm, wait. Let me reconsider the cellular set theorem. Actually I think the theorem is: if X is cellular in S^n (or R^n), then the quotient space S^n / X is homeomorphic to S^n. That's different from the complement.

Actually, the complement R^n \ X being homeomorphic to R^n is different.

Let me reconsider. For n=2, R^2 \ {pt} ≇ R^2. So a single point doesn't work.

Is there any nonempty 0-dimensional X with R^n \ X ≅ R^n?

Let me think about n=2 more. Suppose X is 0-dimensional and nonempty. Take a point p ∈ X. Since X is 0-dimensional, {p} ... hmm, 0-dimensional means the space X has a basis of clopen sets. 

Actually, let me think about whether the answer could be NO - i.e., there exists a nonempty 0-dimensional X with R^n\X ≅ R^n.

Consider the Whitehead manifold or similar exotic things... no, those are 3-manifolds.

Let me think about a different approach. Consider X being a "tame" Cantor set in R^3. There's a notion of a Cantor set being "tame" vs "wild". A tame Cantor set in R^3 is one that's equivalent to the standard middle-thirds Cantor set embedded in a line. 

For a tame Cantor set C in R^3 (lying on a line segment), R^3 \ C. Is this homeomorphic to R^3? 

Hmm, R^3 \ (Cantor set on a line). The complement... Let me think. Actually, I recall that for a tame Cantor set in R^3, the complement is NOT simply connected at every point, or there might be issues.

Actually, let me think about this more carefully using the concept of "cellular" again but correctly.

A subset X of R^n (or S^n) is cellular if X = ∩ B_i where each B_i is a closed n-cell (closed ball) and B_{i+1} ⊂ int(B_i). 

Theorem (cellularity criterion): If X is cellular in S^n, then S^n \ X is homeomorphic to R^n... no wait. S^n \ {pt} ≅ R^n. If X is cellular, S^n / X ≅ S^n. 

Hmm, but what about the complement? If X is cellular in R^n, is R^n \ X ≅ R^n?

Let me think about a point in R^3. A point is cellular (nested balls around it). R^3 \ {pt} ≅ S^2 × R. Is S^2 × R ≅ R^3? 

S^2 × R has H_2 = Z, R^3 has H_2 = 0. So NO, not homeomorphic.

So even though a point is cellular, R^3 \ {pt} ≇ R^3. So cellularity of X doesn't imply R^n \ X ≅ R^n.

OK so let me reconsider the problem. The question is whether there's ANY nonempty 0-dimensional X with R^n \ X ≅ R^n.

Let me think about what invariants distinguish R^n \ X from R^n.

Key invariants:
1. Homology/Homotopy groups of the complement
2. Local properties (local connectedness, etc.)
3. Compactification properties

For R^n: it's contractible, simply connected, all homology trivial, locally compact, locally connected, etc.

Approach via one-point compactification: R^n ∪ {∞} = S^n. If R^n \ X ≅ R^n, then (R^n \ X) ∪ {∞'} ≅ S^n where ∞' is the point at infinity for R^n \ X.

Hmm, this is getting complicated. Let me think about specific cases.

Case n=1: As argued, R \ X connected ⟹ X = ∅ (since removing any point from R disconnects it, and 0-dim nonempty means at least one point). Actually wait, is that right? If X is nonempty 0-dim subset of R, take p ∈ X. Then R \ X ⊂ R \ {p} which has two components. R \ X could still be connected if... no. R \ {p} = (-∞,p) ∪ (p,∞). R \ X ⊂ R \ {p}. Since X ⊃ {p}, R \ X ⊂ R\{p}. The two intervals (-∞,p) and (p,∞) are separated by p (which is removed). So R \ X is contained in the union of two disjoint open sets and intersects both (assuming X doesn't contain all of (-∞,p] etc., but X is 0-dimensional so it's totally disconnected, can't contain an interval). So R \ X is disconnected. Since R is connected, R \ X ≇ R. So for n=1, X must be empty. ✓

Case n=2: R^2 \ X. If X is nonempty, take p ∈ X. Consider a small circle around p that doesn't hit X (possible since X is 0-dimensional, hence totally disconnected, hence has empty interior, so near p there are points not in X... actually we need a circle around p avoiding X). 

Hmm, actually X being 0-dimensional (totally disconnected) means it has empty interior. So around p, there are points of R^2 \ X arbitrarily close. But can we find a circle around p entirely in R^2 \ X? Not necessarily - X could be dense near p.

Let me think about homology. For n=2, if X is nonempty 0-dimensional, consider the one-point compactification. R^2 \ X is homeomorphic to R^2 means... 

Actually, let me think about Alexander duality. For a compact subset X of S^n:
H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X) (reduced homology/cohomology).

If X is compact 0-dimensional, then H̃^0(X) = (number of components of X) - 1 (if X nonempty), and H̃^j(X) = 0 for j ≥ 1.

So for compact nonempty 0-dim X in S^n:
- H̃_{n-1}(S^n \ X) ≅ H̃^0(X) = (#components - 1) ≥ 0.
- If X has more than 1 component, H̃_{n-1}(S^n\X) > 0, so S^n\X has nontrivial homology, not ≅ R^n (which has trivial reduced homology). Actually S^n \ X ≅ R^n \ (X \ {∞})... hmm, need to be careful about whether X contains ∞.

Let me set up more carefully. Let X ⊂ R^n be 0-dimensional. Consider cases:

Case A: X is compact (closed and bounded in R^n).
Then X is a compact subset of S^n = R^n ∪ {∞} (not containing ∞). By Alexander duality:
H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X).

For X compact 0-dimensional nonempty: H̃^0(X) = c(X) - 1 where c(X) = number of components. H̃^j(X) = 0 for j ≥ 1.

So H̃_{n-1}(S^n \ X) ≅ H̃^0(X) = c(X) - 1.
And H̃_i(S^n \ X) = 0 for i ≠ n-1 (and i ≠ 0, but reduced handles that).

Now S^n \ X = (R^n \ X) ∪ {∞}. 

If R^n \ X ≅ R^n, then S^n \ X = R^n ∪ {∞} ≅ S^n (adding the point at infinity to R^n gives S^n). So S^n \ X ≅ S^n, meaning H̃_*(S^n \ X) = 0 (all reduced homology trivial, since S^n has H̃_n = Z but that's... wait S^n has H̃_n = Z, not 0).

Hmm wait. S^n \ X ≅ S^n would mean they have the same homology. S^n has H̃_n = Z and H̃_i = 0 for i ≠ n.

But Alexander duality gives H̃_{n-1}(S^n \ X) = c(X) - 1. For S^n \ X ≅ S^n, we need H̃_{n-1} = 0 (since n-1 ≠ n for n ≥ 2), so c(X) = 1, i.e., X is connected. A 0-dimensional connected compact set is a single point!

So if X is compact, nonempty, 0-dimensional, and R^n \ X ≅ R^n, then X must be a single point (c(X)=1).

But we showed R^n \ {pt} ≇ R^n for n=2 (fundamental group) and for general n (homology: H̃_{n-1}(S^n \ {pt}) = H̃^0({pt}) = 0, so that's consistent with S^n\{pt}≅S^n... wait).

Hold on. S^n \ {pt} ≅ R^n. And we're asking if R^n \ {pt} ≅ R^n. 

R^n \ {pt}: its one-point compactification is S^n \ {pt} with an extra point... no. Let me be careful.

If Y = R^n \ {pt}, the one-point compactification Y^+ = Y ∪ {∞}. Now Y = R^n \ {pt} = S^n \ {pt, ∞} where ∞ is the point at infinity of R^n and pt is the removed point. So Y^+ = S^n \ {pt} (adding back ∞). And S^n \ {pt} ≅ R^n. So Y^+ ≅ R^n, NOT S^n.

For Y ≅ R^n, we'd need Y^+ ≅ S^n. But Y^+ ≅ R^n ≇ S^n. So R^n \ {pt} ≇ R^n. ✓ Consistent.

OK so let me redo this. If R^n \ X ≅ R^n, then (R^n \ X)^+ ≅ S^n (one-point compactification of R^n is S^n).

Now (R^n \ X)^+ = (R^n \ X) ∪ {∞} = (R^n ∪ {∞}) \ X = S^n \ X (if ∞ ∉ X, i.e., X ⊂ R^n which it is).

So R^n \ X ≅ R^n ⟹ S^n \ X ≅ S^n.

By Alexander duality (X compact in S^n): H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X).

S^n \ X ≅ S^n means H̃_i(S^n \ X) = 0 for i ≠ n and = Z for i = n.

Alexander duality: H̃_i(S^n\X) = H̃^{n-i-1}(X). 
- For i = n: H̃_n(S^n\X) = H̃^{-1}(X). Reduced cohomology in degree -1 is 0 (by convention) unless X = ∅, in which case... actually for X = ∅, S^n \ ∅ = S^n, and H̃^{-1}(∅) = Z by convention (this is the standard convention making Alexander duality work for X=∅). So H̃_n(S^n\X) = Z iff X = ∅.
- For i = n-1: H̃_{n-1}(S^n\X) = H̃^0(X) = c(X) - 1 (if X nonempty). For this to be 0 (since n-1 ≠ n), need c(X) = 1.
- For other i: H̃_i = H̃^{n-i-1}(X) = 0 since X is 0-dimensional (cohomology vanishes above degree 0).

So from i = n: H̃_n(S^n \ X) = Z requires X = ∅!

Wait, that's the key. For X ≠ ∅, H̃_n(S^n \ X) = H̃^{-1}(X) = 0 (since X nonempty). But S^n has H̃_n = Z. So S^n \ X ≇ S^n when X ≠ ∅.

Therefore R^n \ X ≅ R^n ⟹ S^n \ X ≅ S^n ⟹ X = ∅.

Wait, but this assumes X is compact! The problem says X is a 0-dimensional subset, not necessarily compact.

Hmm. Let me reconsider. If X is not compact, the one-point compactification argument and Alexander duality need adjustment.

If X is not compact (as a subset of R^n), then ∞ is a limit point of X in S^n, so the closure of X in S^n contains ∞. 

Let me reconsider. (R^n \ X)^+ = S^n \ X where we view X ⊂ R^n ⊂ S^n. This is correct regardless of whether X is compact. S^n \ X is an open subset of S^n (if X is closed in R^n) or not necessarily open.

Hmm, but for Alexander duality we need X to be compact (or at least closed in S^n). If X is not closed in R^n, things are more complicated.

Let me think about whether X needs to be closed. The problem says X is a 0-dimensional subset. It doesn't say closed. 

But actually, let me think about this. If X is not closed, let X̄ be its closure in R^n. Then R^n \ X̄ ⊂ R^n \ X. And R^n \ X = (R^n \ X̄) ∪ (X̄ \ X). 

Hmm, this is getting complicated. Let me think about whether the result still holds for non-closed X.

Actually, let me reconsider. The key question: does there exist a nonempty 0-dimensional X ⊂ R^n (not necessarily closed) with R^n \ X ≅ R^n?

Let me think about n=2. Consider X = Q^2 ∩ [0,1]^2 (rational points in unit square). This is 0-dimensional (countable, totally disconnected). R^2 \ X is... very complicated. Not homeomorphic to R^2 (it's not locally connected at boundary points, etc.).

Let me think about the general argument more carefully, handling non-compact X.

Approach: Use the fact that if R^n \ X ≅ R^n, then R^n \ X is contractible and has trivial homology, is simply connected (for n ≥ 2), etc.

Alternative approach using local homology / local structure:

If R^n \ X ≅ R^n, then R^n \ X is an n-manifold (without boundary). This is automatic since it's an open subset of R^n. 

Key idea: Use the fact that R^n is "simply connected at infinity" or has a specific end structure, and compare with R^n \ X.

Actually, let me think about ends. R^n has:
- n=1: 2 ends
- n=2: 1 end
- n≥3: 1 end

Hmm, for n=1, R has 2 ends. R \ X for nonempty 0-dim X... if X is a single point, R\{pt} has 4 ends (2 from each side). Not matching. If X is something like a ray... but a ray is 1-dimensional. 0-dimensional nonempty X in R: R \ X. The number of ends... if X is bounded, R \ X has at least 2 ends (from the two unbounded components) plus more from the gaps. Actually for n=1 we already handled it.

For n ≥ 2: R^n has 1 end. R^n \ X: if X is compact, R^n \ X has 1 end (for n ≥ 2). So ends don't distinguish in that case.

Let me go back to the Alexander duality approach but handle non-compact X.

If X is not compact, consider X̄ = closure of X in S^n (so X̄ = cl_{R^n}(X) ∪ {∞} if X is unbounded, or X̄ = cl_{R^n}(X) if X is bounded).

Hmm, actually, let me think about it differently. 

Claim: If R^n \ X ≅ R^n, then X must be closed in R^n.

Why? R^n \ X is homeomorphic to R^n, which is a complete metric space (well, under some metric). Actually, being homeomorphic to R^n means R^n \ X is a Baire space, locally compact, etc. 

R^n \ X is an open subset of R^n iff X is closed. If X is not closed, R^n \ X is not open, hence not a manifold? No wait, R^n \ X could still be a manifold even if not open in R^n.

Hmm, actually if X is not closed, R^n \ X is not open in R^n, so it might not be an n-manifold. But R^n is an n-manifold. So if R^n \ X ≅ R^n, then R^n \ X is an n-manifold. 

Is R^n \ X being an n-manifold enough to force X to be closed? 

If p ∈ X is a boundary point of X (i.e., p ∈ cl(X) \ X... no, p ∈ X but p is a limit point of X). Take p ∈ X with p ∈ cl(X). Then p ∈ X so p ∉ R^n \ X. But points near p that are in X are also not in R^n \ X. So near p, R^n \ X has "holes". For R^n \ X to be a manifold, every point of R^n \ X needs a neighborhood homeomorphic to R^n. Take q ∈ R^n \ X near p. If q is close to p and there are points of X between q and p... 

Actually, I think the right approach: if R^n \ X ≅ R^n, then R^n \ X is open in R^n (since it's an n-manifold and a subspace of R^n... no, that's not quite right either).

Let me think again. R^n \ X is a subspace of R^n. If it's homeomorphic to R^n, it's a connected n-manifold. As a subspace of R^n, is it necessarily open? 

A subspace M of R^n that is an n-manifold: is M open in R^n? Yes! This is a consequence of invariance of domain. If M is an n-manifold (without boundary) and M ⊂ R^n, then M is open in R^n. 

Invariance of domain: if U is an open subset of R^n and f: U → R^n is an injective continuous map, then f(U) is open. 

Apply this: M = R^n \ X is an n-manifold. The inclusion i: M → R^n is continuous and injective. For each point m ∈ M, there's a neighborhood V of m in M and a homeomorphism φ: V → U where U is open in R^n. Then i ∘ φ^{-1}: U → R^n is continuous and injective, so by invariance of domain, i(V) = i(φ^{-1}(U)) is open in R^n. So M is locally open in R^n, hence M is open in R^n.

So R^n \ X is open in R^n, which means X is closed in R^n!

Great. So if R^n \ X ≅ R^n, then X is closed in R^n.

Now X is closed in R^n and 0-dimensional. 

Now, X could be unbounded (closed but not compact). Let me handle this.

If X is closed in R^n and unbounded, then ∞ ∈ cl_{S^n}(X). 

Let me use the one-point compactification. (R^n \ X)^+ = S^n \ X (where X ⊂ R^n ⊂ S^n, and S^n \ X means S^n minus the set X, noting ∞ ∉ X since X ⊂ R^n).

If R^n \ X ≅ R^n, then (R^n \ X)^+ ≅ S^n, so S^n \ X ≅ S^n.

Now X is closed in R^n but possibly unbounded. In S^n, X is not closed (its closure includes ∞). Let X* = cl_{S^n}(X) = X ∪ {∞} (if X unbounded) or X (if X bounded).

S^n \ X = S^n \ X* ∪ {∞} if ∞ ∉ X... wait. S^n \ X: since X ⊂ R^n and ∞ ∉ X, we have ∞ ∈ S^n \ X. And S^n \ X = (S^n \ X*) ∪ {∞} if ∞ ∈ X* \ X = {∞}.

Hmm, let me just think about it as: S^n \ X is an open subset of S^n (since X is closed in R^n, but in S^n... X is not closed in S^n if unbounded). 

Actually, S^n \ X: X is a subset of S^n (not containing ∞). Is X closed in S^n? X is closed in R^n. X is closed in S^n iff X is compact (closed in R^n and bounded) or ∞ ∈ X (but ∞ ∉ X). So X is closed in S^n iff X is compact.

If X is unbounded, X is not closed in S^n, so S^n \ X is not open in S^n. But S^n \ X ≅ S^n which is compact... wait, S^n \ X contains ∞ and is it compact? S^n \ X = S^n \ X. If X is not closed, S^n \ X is not closed, so not compact. But S^n is compact. Contradiction! 

So if S^n \ X ≅ S^n (compact), then S^n \ X must be compact, hence closed in S^n, hence X is open in S^n. But X ⊂ R^n and if X is also closed in R^n... X open in S^n and X ⊂ R^n means X is open in R^n. But X is 0-dimensional with empty interior (if nonempty... well a 0-dimensional subset of R^n has empty interior unless... a 0-dimensional space can have nonempty interior only if it has isolated points forming open sets, but in R^n a 0-dimensional subset has empty interior since R^n has no isolated points and... actually a 0-dim subset of R^n: does it have empty interior? A single point has empty interior in R^n for n ≥ 1. A 0-dimensional space is totally disconnected. A totally disconnected subset of R^n (n ≥ 1) has empty interior (since any open ball is connected). So X has empty interior. If X is also open, X = ∅.

Wait, let me double-check: S^n \ X ≅ S^n implies S^n \ X is compact. S^n \ X compact and S^n Hausdorff implies S^n \ X is closed in S^n. So X is open in S^n. Since X ⊂ R^n (doesn't contain ∞), X is open in R^n (subspace topology from S^n restricted to R^n... actually X open in S^n and X ⊂ R^n means X = X ∩ R^n is open in R^n). But X is 0-dimensional subset of R^n, which has empty interior (as argued). So X open and empty interior means X = ∅.

Wait, but I need to double check that S^n \ X ≅ S^n implies compactness is used right. S^n is compact, so anything homeomorphic to it is compact. S^n \ X is a subspace of S^n (Hausdorff), so compact ⟹ closed. So X is open in S^n. Then X open in R^n. X 0-dimensional ⟹ empty interior ⟹ X = ∅.

But hold on, I need to also handle the case where X is bounded (compact). If X is compact (closed and bounded in R^n), then X is closed in S^n, so S^n \ X is open in S^n. S^n \ X ≅ S^n (compact) and S^n \ X open in S^n. An open compact subset of connected S^n... S^n \ X is both open and closed (compact in Hausdorff = closed) in S^n. Since S^n is connected, S^n \ X = ∅ or S^n. S^n \ X = ∅ means X = S^n, impossible (X ⊂ R^n). S^n \ X = S^n means X = ∅.

So in both cases (X bounded or unbounded), we get X = ∅!

Wait, let me re-examine the compact case. X compact, closed in S^n. S^n \ X is open in S^n. If S^n \ X ≅ S^n, then S^n \ X is compact, hence closed in S^n. So S^n \ X is clopen in S^n. S^n connected ⟹ S^n \ X = ∅ or S^n. So X = S^n or X = ∅. X ⊂ R^n so X ≠ S^n. Thus X = ∅. ✓

And the unbounded case: X not closed in S^n. S^n \ X not closed in S^n. But S^n \ X ≅ S^n compact ⟹ closed. Contradiction unless... wait, this means the unbounded case can't happen if S^n \ X ≅ S^n. So actually if R^n \ X ≅ R^n and X is unbounded, we get a contradiction (S^n \ X would need to be compact but isn't closed). So X must be bounded, hence compact, hence X = ∅ by the previous argument.

Actually wait, I need to be more careful. Let me re-examine.

If X is unbounded (closed in R^n but not compact), then in S^n, X is not closed (closure is X ∪ {∞}). S^n \ X: is this compact? S^n \ X = S^n \ X. Since X is not closed in S^n, S^n \ X is not open... no wait, complement of not-closed is not-open. S^n \ X is not open. Is S^n \ X compact? A subspace of a compact Hausdorff space is compact iff closed. S^n \ X is closed in S^n iff X is open in S^n. X is not open (0-dim, empty interior). So S^n \ X is not closed, hence not compact. But S^n \ X ≅ S^n would make it compact. Contradiction. So X can't be unbounded.

Therefore X must be bounded (compact), and then X = ∅.

So the answer is YES, X must be empty.

Let me also handle n=1 separately to make sure (though the argument should work for all n ≥ 1).

For n=1: S^1 is connected. Same argument works. R \ X ≅ R ⟹ S^1 \ X ≅ S^1 ⟹ S^1 \ X compact ⟹ closed ⟹ X open in S^1. X 0-dim in R, empty interior, so X open in R^1 and empty interior ⟹ X = ∅. Or via the compact case: X compact, S^1 \ X clopen, connected ⟹ X = ∅. ✓

Actually, wait. For n=1, let me double check the invariance of domain step. R \ X ≅ R means R \ X is a 1-manifold. Invariance of domain for n=1: an injective continuous map from an open subset of R to R has open image. The inclusion R\X → R: for each point, local homeomorphism to R, image is open. So R \ X is open in R, X is closed. ✓. Then same argument.

Hmm wait, but actually I realize there might be a subtlety. Let me reconsider whether R^n \ X ≅ R^n really implies (R^n \ X)^+ ≅ S^n.

The one-point compactification: if Y is a locally compact Hausdorff space, Y^+ = Y ∪ {∞} is compact Hausdorff. If Y ≅ R^n, then Y^+ ≅ (R^n)^+ = S^n. ✓ (R^n is locally compact Hausdorff, and so is Y ≅ R^n.)

And Y^+ = (R^n \ X) ∪ {∞_Y}. The point ∞_Y is the "point at infinity" of Y = R^n \ X. As a set, Y ∪ {∞_Y} = (R^n \ X) ∪ {∞_Y}. 

Now, is this the same as S^n \ X? S^n = R^n ∪ {∞}. S^n \ X = (R^n \ X) ∪ {∞} (since ∞ ∉ X). So S^n \ X = (R^n \ X) ∪ {∞} as a set. 

And Y^+ = (R^n \ X) ∪ {∞_Y}. These are the same set (both are R^n \ X plus one extra point). The topology on Y^+ is the one-point compactification topology of R^n \ X. The topology on S^n \ X is the subspace topology from S^n.

Are these topologies the same? The one-point compactification of R^n \ X: a set U is open in Y^+ if U is open in R^n \ X, or ∞_Y ∈ U and Y^+ \ U is compact in R^n \ X.

The subspace topology on S^n \ X from S^n: U is open in S^n \ X if U = V ∩ (S^n \ X) for V open in S^n.

These are the same if and only if the subspace topology on R^n \ X from R^n (equivalently from S^n) agrees with itself (which it does) and the neighborhoods of ∞ match. Neighborhoods of ∞ in S^n \ X (subspace from S^n): {∞} ∪ (R^n \ X) \ K for K compact in R^n (since neighborhoods of ∞ in S^n are complements of compact sets in R^n). Neighborhoods of ∞_Y in Y^+: {∞_Y} ∪ (R^n \ X) \ K for K compact in R^n \ X.

These match iff compact subsets of R^n \ X (in subspace topology) = compact subsets of R^n that are contained in R^n \ X. A compact subset K of R^n \ X (subspace topology) is compact in R^n (since R^n \ X ⊂ R^n and compactness is intrinsic... actually a compact subset of a subspace is compact in the ambient space). Conversely, a compact subset K of R^n with K ⊂ R^n \ X is compact in R^n \ X. So yes, they match! 

So (R^n \ X)^+ = S^n \ X as topological spaces. ✓

Great, so the argument is solid. Let me also verify: we need R^n \ X to be locally compact Hausdorff for the one-point compactification. R^n \ X is a subspace of R^n (Hausdorff), so Hausdorff. Locally compact: R^n \ X ≅ R^n which is locally compact. ✓. (Or: R^n \ X is open in R^n by invariance of domain, and open subsets of locally compact Hausdorff spaces are locally compact.)

So the full proof:

1. Suppose R^n \ X ≅ R^n.
2. By invariance of domain, R^n \ X is open in R^n, so X is closed in R^n.
3. R^n \ X is locally compact Hausdorff, so its one-point compactification (R^n \ X)^+ exists and ≅ S^n (since R^n \ X ≅ R^n and (R^n)^+ = S^n).
4. (R^n \ X)^+ = S^n \ X (as topological spaces, verified above).
5. So S^n \ X ≅ S^n, hence S^n \ X is compact.
6. S^n \ X compact in Hausdorff S^n ⟹ S^n \ X is closed in S^n ⟹ X is open in S^n.
7. X ⊂ R^n and X open in S^n ⟹ X is open in R^n.
8. X is 0-dimensional (totally disconnected) subset of R^n ⟹ X has empty interior in R^n (since any nonempty open subset of R^n is connected for n ≥ 1, but a totally disconnected set can't contain a connected open set; actually for n ≥ 1, open balls are connected, so a totally disconnected set has empty interior).

Hmm wait, for n=0? R^0 is a point. 0-dimensional subset of R^0: either ∅ or {pt}. R^0 \ ∅ = R^0 ≅ R^0. R^0 \ {pt} = ∅ ≇ R^0. So X = ∅. The argument: S^0 = {two points}. Hmm, S^0 is not connected, so the argument needs adjustment for n=0. But n=0 is a degenerate case. Let me assume n ≥ 1 (the problem likely intends n ≥ 1, and for n=0 it's trivially true anyway).

Actually for n ≥ 1, S^n is connected, and the argument works. Let me also handle the empty interior claim more carefully.

X is 0-dimensional. In the sense of covering dimension (Lebesgue dimension), 0-dimensional means every open cover has a refinement by disjoint open sets (in the subspace). This implies totally disconnected. Actually, for separable metric spaces, 0-dimensional (covering dimension) ⟺ totally disconnected ⟺ has a basis of clopen sets. Hmm, actually 0-dimensional (having a basis of clopen sets) is stronger than totally disconnected. Let me just use: 0-dimensional ⟹ totally disconnected.

Totally disconnected subset of R^n (n ≥ 1) has empty interior: Suppose X has nonempty interior. Then there's an open ball B ⊂ X. But B is connected (for n ≥ 1) and B ⊂ X, contradicting X being totally disconnected (a totally disconnected space has no connected subsets other than points). ✓

So X open in R^n and empty interior ⟹ X = ∅.

Therefore X = ∅. The answer is YES.

Actually, let me reconsider step 6-7 more carefully. X is open in S^n. Since X ⊂ R^n ⊂ S^n and X doesn't contain ∞, X is open in S^n means X is an open subset of S^n not containing ∞. The open subsets of S^n not containing ∞ are exactly the open subsets of R^n (since S^n \ {∞} = R^n and the subspace topology on R^n from S^n is the standard topology). So X is open in R^n. ✓

And actually, I realize I should double-check step 5-6. S^n \ X ≅ S^n. S^n is compact. So S^n \ X is compact. S^n \ X is a subspace of S^n (Hausdorff). A compact subspace of a Hausdorff space is closed. So S^n \ X is closed in S^n. So X = S^n \ (S^n \ X) is open in S^n. ✓

Everything checks out. Let me also think about whether there are any issues with the invariance of domain application.

Invariance of domain: Let U ⊂ R^n be open and f: U → R^n be continuous and injective. Then f(U) is open in R^n.

Application: Y = R^n \ X ≅ R^n. Let h: R^n → Y be a homeomorphism. Then h: R^n → R^n (viewing Y ⊂ R^n) is continuous and injective. By invariance of domain, h(R^n) = Y is open in R^n. ✓

So Y = R^n \ X is open in R^n, hence X is closed. ✓

The proof is complete. Let me write it up.

Actually, one more thing: I should make sure the problem is asking about topological dimension 0. "0-dimensional subset" - in the context of topology problems like this, it means covering dimension 0, which for subsets of R^n is equivalent to totally disconnected (for separable metric spaces, dim = 0 ⟺ totally disconnected... actually that's not quite right. For separable metric spaces, dim 0 ⟺ has a basis of clopen sets, which is stronger than totally disconnected. But dim 0 ⟹ totally disconnected, which is all we need).

Actually, I realize I should double-check: is it true that for separable metric spaces, 0-dimensional (covering dimension) implies totally disconnected? Yes. Covering dimension 0 means every open cover has an open refinement that is pairwise disjoint. This implies the space has a basis of clopen sets (for normal spaces, which metric spaces are), which implies totally disconnected. So yes, 0-dimensional ⟹ totally disconnected ⟹ empty interior in R^n (n ≥ 1). ✓

Let me write up the clean proof now.

Hmm, actually let me reconsider whether I even need the "X is closed" step (invariance of domain). Let me see if the argument works without it.

Without knowing X is closed: (R^n \ X)^+ = S^n \ X. If R^n \ X ≅ R^n, then S^n \ X ≅ S^n, compact. So S^n \ X is closed in S^n, so X is open in S^n. X ⊂ R^n, so X open in R^n. X 0-dimensional ⟹ empty interior ⟹ X = ∅.

Wait, does this work without first showing X is closed? The one-point compactification (R^n \ X)^+ requires R^n \ X to be locally compact Hausdorff. If R^n \ X ≅ R^n, then yes it's locally compact Hausdorff. And (R^n \ X)^+ ≅ S^n. And (R^n \ X)^+ = S^n \ X as sets. But is the topology on (R^n \ X)^+ the same as the subspace topology from S^n?

The one-point compactification topology: neighborhoods of ∞ are complements of compact sets in R^n \ X.
The subspace topology from S^n: neighborhoods of ∞ are {∞} ∪ (R^n \ X \ K) where K is compact in R^n (and K ⊂ R^n, K ⊂ R^n \ X... no, K just needs to be compact in R^n, but K might intersect X).

Hmm, here's the issue. In the subspace topology from S^n, a neighborhood of ∞ is (S^n \ C) ∩ (S^n \ X) for C compact in R^n (since neighborhoods of ∞ in S^n are S^n \ C for C compact in R^n). This equals S^n \ (C ∪ X) = (R^n \ (C ∪ X)) ∪ {∞} = ((R^n \ X) \ C) ∪ {∞}.

In the one-point compactification, a neighborhood of ∞ is (R^n \ X \ K) ∪ {∞} for K compact in R^n \ X.

For these to be the same, we need: {C compact in R^n} and {K compact in R^n \ X} to give the same neighborhoods. A set K compact in R^n \ X is compact in R^n (and K ⊂ R^n \ X, so K ∩ X = ∅). A set C compact in R^n might intersect X. 

If C is compact in R^n and C ∩ X ≠ ∅, then (R^n \ X) \ C = (R^n \ X) \ (C \ X) ∪ ... hmm. (R^n \ X) \ C = (R^n \ X) \ (C ∩ (R^n \ X)) = (R^n \ X) \ (C \ X). And C \ X = C ∩ (R^n \ X). Is C \ X compact in R^n \ X? C is compact in R^n. C \ X = C ∩ (R^n \ X). If X is closed, R^n \ X is open, and C ∩ (open) is... not necessarily compact. Hmm.

Actually, C \ X is a closed subset of C (if X is open) or not closed. If X is closed, C \ X = C ∩ (R^n \ X) is the intersection of compact C with open R^n \ X, which is locally compact but not necessarily compact.

Hmm, so the topologies might not match if X is not closed. Let me think again.

OK here's the thing. If X is not closed, then R^n \ X is not locally compact? No, R^n \ X ≅ R^n which is locally compact. So R^n \ X is locally compact. But the subspace topology from S^n on S^n \ X = (R^n \ X) ∪ {∞} might not be the one-point compactification topology.

Let me think about this concretely. Take n=1, X = {1/n : n ∈ N} (not closed, 0 is a limit point not in X). R \ X. The one-point compactification of R \ X: neighborhoods of ∞ are complements of compact sets in R \ X. 

In S^1 = R ∪ {∞}, S^1 \ X = (R \ X) ∪ {∞}. Subspace topology: neighborhoods of ∞ are (S^1 \ C) ∩ (S^1 \ X) for C compact in R. = (R \ (C ∪ X)) ∪ {∞}. 

For the one-point compactification, neighborhoods of ∞ are (R \ X \ K) ∪ {∞} for K compact in R \ X.

Take C = [0, 1] (compact in R). Then (R \ (C ∪ X)) ∪ {∞} is a neighborhood of ∞ in subspace topology. C ∪ X = [0,1] ∪ {1/n} = [0,1] (since 1/n ∈ [0,1]). So this neighborhood is (R \ [0,1]) ∪ {∞}.

In one-point compactification: we need K compact in R \ X with (R \ X \ K) ∪ {∞} = (R \ [0,1]) ∪ {∞}. This means R \ X \ K = R \ [0,1], so K = (R \ X) \ (R \ [0,1]) = (R \ X) ∩ [0,1] = [0,1] \ X = [0,1] \ {1/n}. Is [0,1] \ {1/n} compact in R \ X? [0,1] \ {1/n} is not closed in R (its closure includes 0 and the 1/n's... wait, [0,1] \ {1/n : n ∈ N} — what's its closure? It includes 0 (since 0 is a limit of points in [0,1]\{1/n}) and all the 1/n are excluded but are they limit points? Yes. So the closure of [0,1]\{1/n} in R is [0,1]. In R \ X, the closure would be [0,1] \ X (since X is removed). Is [0,1] \ {1/n} closed in R \ X? Its closure in R \ X is [0,1] \ X (closure in subspace = closure in R intersected with R\X = [0,1] ∩ (R\X) = [0,1]\X). And [0,1]\{1/n} ≠ [0,1]\X = [0,1]\{1/n : n∈N}. Wait, [0,1] \ X = [0,1] \ {1/n : n ∈ N}. And [0,1] \ {1/n : n ∈ N} is exactly [0,1] \ X. So K = [0,1] \ X, and its closure in R \ X is [0,1] \ X = K. So K is closed in R \ X. And K ⊂ [0,1] which is compact in R. A closed subset of a compact set is compact (in R, hence in R \ X since K ⊂ R \ X). So K is compact in R \ X. ✓

So in this case, the topologies do match. Let me think about whether they always match.

Claim: For any X ⊂ R^n, the one-point compactification of R^n \ X (with subspace topology from R^n) is homeomorphic to S^n \ X (with subspace topology from S^n), provided R^n \ X is locally compact.

Hmm, actually I think this is true when R^n \ X is locally compact and the topology works out. Let me think more carefully.

The key question: is the subspace topology on (R^n \ X) ∪ {∞} from S^n the same as the one-point compactification topology of R^n \ X?

One-point compactification: ∞ has neighborhoods {∞} ∪ (R^n \ X \ K) for K compact in R^n \ X.
Subspace from S^n: ∞ has neighborhoods {∞} ∪ ((R^n \ X) \ C) for C compact in R^n (since nbhds of ∞ in S^n are S^n \ C, C compact in R^n, and intersecting with S^n \ X gives ((R^n \ X) \ C) ∪ {∞}).

Wait, but C compact in R^n might not be contained in R^n \ X. So (R^n \ X) \ C = (R^n \ X) \ (C ∩ (R^n \ X)). And C ∩ (R^n \ X) might not be compact in R^n \ X.

Conversely, K compact in R^n \ X is compact in R^n (since R^n \ X ⊂ R^n and compactness is preserved). So every one-point compactification neighborhood is a subspace neighborhood (take C = K). 

For the reverse: given C compact in R^n, is (R^n \ X) \ C a neighborhood of the form (R^n \ X) \ K for K compact in R^n \ X? We need K = (R^n \ X) ∩ C to be compact in R^n \ X. But (R^n \ X) ∩ C = C \ X, and C \ X might not be compact in R^n \ X (it might not be closed).

So the subspace topology might be finer than the one-point compactification topology (more neighborhoods of ∞). They're equal iff for every C compact in R^n, C \ X is compact in R^n \ X, i.e., C \ X is closed in R^n \ X.

C \ X is closed in R^n \ X iff C \ X = (R^n \ X) ∩ D for some D closed in R^n. Take D = C ∩ cl(X)^c... hmm. C \ X = C ∩ (R^n \ X). For this to be closed in R^n \ X, we need C ∩ (R^n \ X) to be closed in the subspace R^n \ X, i.e., C ∩ (R^n \ X) = (R^n \ X) ∩ E for E closed in R^n. Take E = C: (R^n \ X) ∩ C = C \ X. Is this closed in R^n \ X? It's closed in R^n \ X iff C \ X = cl_{R^n}(C \ X) ∩ (R^n \ X). cl_{R^n}(C \ X) ⊂ C (since C is closed). So cl_{R^n}(C \ X) ∩ (R^n \ X) ⊂ C ∩ (R^n \ X) = C \ X. And C \ X ⊂ cl_{R^n}(C \ X) ∩ (R^n \ X) always. So equality holds iff C \ X = cl_{R^n}(C \ X) ∩ (R^n \ X), which is always true! Wait:

cl_{R^n}(C \ X) ∩ (R^n \ X): since C \ X ⊂ C and C is closed, cl(C \ X) ⊂ C. So cl(C \ X) ∩ (R^n \ X) ⊂ C ∩ (R^n \ X) = C \ X. And C \ X ⊂ cl(C \ X) and C \ X ⊂ R^n \ X, so C \ X ⊂ cl(C \ X) ∩ (R^n \ X). Therefore cl(C \ X) ∩ (R^n \ X) = C \ X. 

So C \ X is always closed in R^n \ X! And C \ X ⊂ C which is compact in R^n, so C \ X is compact in R^n, and being a closed subset of R^n \ X that is compact in R^n... is it compact in R^n \ X? 

C \ X is closed in R^n \ X and C \ X ⊂ C (compact in R^n). A subset of R^n \ X that is compact in R^n is compact in R^n \ X (compactness is intrinsic - a space is compact iff every open cover has a finite subcover, and this doesn't depend on the ambient space). Actually, more precisely: K ⊂ R^n \ X is compact in R^n \ X iff K is compact in R^n (since R^n \ X has the subspace topology, compactness is the same). Wait, is that true? Compactness is a topological property of the space itself. K as a subspace of R^n \ X has the same topology as K as a subspace of R^n (since R^n \ X has subspace topology from R^n). So K is compact in R^n \ X iff K is compact in R^n. ✓

So C \ X is compact in R^n \ X (since it's compact in R^n, being a closed subset of compact C). 

Wait, is C \ X closed in R^n? C \ X = C ∩ (R^n \ X). C is closed in R^n. R^n \ X is open in R^n (if X is closed) or not. C \ X is the intersection of closed C with R^n \ X. If X is not closed, R^n \ X is not open, and C \ X is the intersection of a closed set with a non-open set, which is... not necessarily closed. 

But C \ X is closed in R^n \ X (as shown above), and C \ X ⊂ C (compact in R^n). A closed subset of a compact space is compact. But "closed in R^n \ X" and "compact in R^n" — we need C \ X to be compact in R^n. C \ X ⊂ C and C is compact in R^n. C \ X is a subspace of C. Is C \ X compact? C \ X is compact iff it's closed in C (since C is compact Hausdorff). C \ X = C ∩ (R^n \ X). Is this closed in C? It's closed in C iff C \ (C \ X) = C ∩ X is open in C. C ∩ X is open in C iff C ∩ X = C ∩ U for some U open in R^n. This is true iff C ∩ X is open in the subspace C. 

Hmm, C ∩ X is open in C iff for every point p ∈ C ∩ X, there's an open set V in R^n with p ∈ V and V ∩ C ⊂ C ∩ X, i.e., V ∩ C ⊂ X. This is not true in general (e.g., if p is a limit point of R^n \ X within C).

So C \ X might not be compact in R^n, hence might not be compact in R^n \ X.

Example: n=1, X = Q (rationals, 0-dimensional). C = [0,1]. C \ X = [0,1] \ Q = irrationals in [0,1]. This is not compact (not closed in R; its closure is [0,1]). And it's not compact in R \ Q either.

So for X = Q, the subspace topology on S^1 \ Q from S^1 is NOT the same as the one-point compactification of R \ Q.

But wait, R \ Q is not locally compact! (The irrationals are not locally compact... actually, are they? The irrationals are homeomorphic to Baire space N^N, which is not locally compact.) So the one-point compactification doesn't even apply.

So the issue only arises when R^n \ X is not locally compact, in which case the one-point compactification doesn't exist, and our argument doesn't apply directly.

But if R^n \ X ≅ R^n, then R^n \ X IS locally compact (since R^n is). So the one-point compactification exists. And we need (R^n \ X)^+ ≅ S^n \ X (subspace topology).

Hmm, but as shown, the topologies might differ. Let me reconsider.

If R^n \ X ≅ R^n, then R^n \ X is locally compact. The one-point compactification (R^n \ X)^+ is well-defined and ≅ S^n. 

Now, is (R^n \ X)^+ homeomorphic to S^n \ X (subspace topology from S^n)?

The identity map id: R^n \ X → R^n \ X is a homeomorphism (same topology on R^n \ X in both cases - subspace from R^n). The question is whether the topology at ∞ matches.

In (R^n \ X)^+: ∞ has nbhd basis {∞} ∪ (R^n \ X \ K), K compact in R^n \ X.
In S^n \ X (subspace): ∞ has nbhd basis {∞} ∪ (R^n \ (C ∪ X)), C compact in R^n, i.e., {∞} ∪ ((R^n \ X) \ C), C compact in R^n.

Wait, I wrote it as (R^n \ X) \ C but C might not be a subset of R^n \ X. Let me rewrite: (S^n \ C) ∩ (S^n \ X) where C compact in R^n. = (S^n \ C) ∩ ((R^n \ X) ∪ {∞}) = ((R^n \ C) ∩ (R^n \ X)) ∪ {∞} = (R^n \ (C ∪ X)) ∪ {∞} = ((R^n \ X) \ C) ∪ {∞}.

Note: (R^n \ X) \ C = (R^n \ X) \ (C ∩ (R^n \ X)) = (R^n \ X) \ (C \ X).

So subspace nbhd: {∞} ∪ ((R^n \ X) \ (C \ X)) for C compact in R^n.
One-point compactification nbhd: {∞} ∪ ((R^n \ X) \ K) for K compact in R^n \ X.

For these to generate the same topology, we need: for every C compact in R^n, C \ X is "contained in" some K compact in R^n \ X (so the subspace nbhd contains a one-point-comp nbhd), and vice versa.

Vice versa: K compact in R^n \ X is compact in R^n, so take C = K, then C \ X = K \ X = K (since K ⊂ R^n \ X), and (R^n \ X) \ K is the same. ✓

Forward: C compact in R^n, need K compact in R^n \ X with K ⊃ C \ X (so that (R^n \ X) \ K ⊂ (R^n \ X) \ (C \ X)). We need K compact in R^n \ X containing C \ X. 

C \ X ⊂ C (compact in R^n). If C \ X is compact in R^n \ X, take K = C \ X. But as shown, C \ X might not be compact.

However, if R^n \ X is locally compact, can we always find such a K? 

R^n \ X is locally compact. C \ X ⊂ R^n \ X. C \ X is a subset of C (compact in R^n). We need a compact K in R^n \ X with C \ X ⊂ K.

Since R^n \ X is locally compact, every point of C \ X has a compact neighborhood in R^n \ X. But C \ X might not be covered by finitely many such neighborhoods (C \ X might not be compact).

Hmm, but C is compact in R^n. C \ X ⊂ C. For each point p ∈ C \ X, there's an open set U_p in R^n \ X with compact closure (local compactness). {U_p} covers C \ X. But C \ X might not be compact in R^n \ X, so we might not get a finite subcover.

However, C is compact in R^n. Consider the open cover of C in R^n: for each p ∈ C \ X, take U_p (open in R^n \ X, hence open in R^n if R^n \ X is open in R^n). Plus, for points in C ∩ X, we need to cover them too... but we don't need to cover C ∩ X, we need to cover C \ X.

Hmm, this is getting complicated. Let me take a step back.

I think the cleanest approach is to first show X is closed (using invariance of domain), and then use the one-point compactification argument (which works cleanly when X is closed).

When X is closed in R^n: R^n \ X is open in R^n. For C compact in R^n, C \ X = C ∩ (R^n \ X) is a closed subset of C (since R^n \ X is open... no, C ∩ (open) is open in C, not closed). Hmm.

Wait, C \ X = C ∩ (R^n \ X). R^n \ X is open (X closed). So C \ X is open in C. Not necessarily closed. So C \ X might not be compact.

Hmm, so even with X closed, C \ X might not be compact. Example: X = {0} in R, C = [0,1]. C \ X = (0,1]. Not compact.

So the subspace topology on S^n \ X from S^n might still differ from the one-point compactification.

But wait, for X = {0} (closed), R \ {0} is locally compact, and its one-point compactification should be... R \ {0} has two components, (-∞,0) and (0,∞). Its one-point compactification: adding one point ∞ that compactifies both ends. The result is like a figure-eight or... actually, the one-point compactification of a non-connected space: (R \ {0})^+ = (R \ {0}) ∪ {∞}. Neighborhoods of ∞ are complements of compact sets in R \ {0}. A compact set in R \ {0} is a compact set in R not containing 0, i.e., a compact set in (-∞,0) ∪ (0,∞), which is a union of a compact set in (-∞,0) and a compact set in (0,∞). So neighborhoods of ∞ are {∞} ∪ (-∞, -M) ∪ (m, 0) ∪ (0, M')... hmm, this is getting complicated. The point is that ∞ connects the two "outer" ends.

And S^1 \ {0} = (R \ {0}) ∪ {∞}. In the subspace topology from S^1, ∞ has neighborhoods that are complements of compact sets in R (not in R \ {0}). A compact set in R containing 0, like [-1,1], gives neighborhood {∞} ∪ (R \ [-1,1]) = {∞} ∪ (-∞,-1) ∪ (1,∞). But in the one-point compactification, we'd also remove 0, so we'd get {∞} ∪ (-∞,-1) ∪ (1,∞) ∪ ... wait, 0 is already not in R \ {0}.

Hmm, let me reconsider. S^1 \ {0} = (R \ {0}) ∪ {∞}. Subspace topology: ∞ has neighborhoods (S^1 \ C) ∩ (S^1 \ {0}) for C compact in R. If C = [-1,1] (containing 0), then S^1 \ C = {∞} ∪ (R \ [-1,1]) = {∞} ∪ (-∞,-1) ∪ (1,∞). Intersect with S^1 \ {0}: {∞} ∪ (-∞,-1) ∪ (1,∞) (since 0 ∉ (-∞,-1) ∪ (1,∞)). So neighborhood of ∞ is {∞} ∪ (-∞,-1) ∪ (1,∞).

One-point compactification: ∞ has neighborhoods {∞} ∪ (R \ {0} \ K) for K compact in R \ {0}. K compact in R \ {0} means K is compact in R and 0 ∉ K. Take K = [-2,-1] ∪ [1,2] (compact, doesn't contain 0). Then nbhd = {∞} ∪ (R \ {0} \ K) = {∞} ∪ (-∞, -2) ∪ (-1, 0) ∪ (0, 1) ∪ (2, ∞).

So the one-point compactification has "more" neighborhoods of ∞ - it can have neighborhoods that include points near 0 (like (-1,0) ∪ (0,1)), while the subspace topology from S^1 can't (because any compact C in R that we remove either contains 0 or doesn't, and if it doesn't contain 0, removing C \ {0} from R \ {0} still leaves a neighborhood of 0 in R \ {0}... hmm).

Actually wait. In the subspace topology, can we get a neighborhood of ∞ that includes points near 0? Take C = {1/n : n ∈ N} ∪ {0} ∪ {-1/n : n ∈ N} (compact in R, contains 0). Then S^1 \ C = {∞} ∪ (R \ C). Intersect with S^1 \ {0}: {∞} ∪ (R \ (C ∪ {0})) = {∞} ∪ (R \ C) (since 0 ∈ C). R \ C includes intervals between the 1/n's. So yes, the subspace topology can give neighborhoods of ∞ that include points near 0.

Hmm, so maybe the topologies do match after all? Let me think more carefully.

Actually, I think the issue is that for X closed, the one-point compactification of R^n \ X is NOT S^n \ X in general. For X = {0} in R, (R \ {0})^+ is not S^1 \ {0}.

Let me compute (R \ {0})^+ more carefully. R \ {0} = (-∞,0) ∪ (0,∞). This is locally compact. Its one-point compactification adds a single point ∞. The result: ∞ is "attached" to both ends of both rays. So the space looks like... two circles joined at ∞? No. 

Actually, the one-point compactification of a disjoint union of two locally compact spaces is the wedge sum of their one-point compactifications. (-∞,0)^+ ≅ S^1 (a circle) and (0,∞)^+ ≅ S^1. The one-point compactification of (-∞,0) ⊔ (0,∞) is S^1 ∨ S^1 (wedge of two circles, i.e., figure-eight). 

Wait, is that right? The one-point compactification of a disjoint union X ⊔ Y (both locally compact non-compact) is X^+ ∧ Y^+... no. Let me think. (X ⊔ Y)^+ = (X ⊔ Y) ∪ {∞}. Neighborhoods of ∞ are complements of compact sets in X ⊔ Y. A compact set in X ⊔ Y is K_X ⊔ K_Y where K_X compact in X, K_Y compact in Y. So neighborhoods of ∞ are {∞} ∪ (X \ K_X) ∪ (Y \ K_Y). This means ∞ is "close to" both X and Y. The resulting space is the one-point compactification, which for X ⊔ Y is the wedge sum X^+ ∨ Y^+ (identifying the two ∞'s). Yes, so (R \ {0})^+ ≅ S^1 ∨ S^1 (figure-eight).

And S^1 \ {0} = (R \ {0}) ∪ {∞} with subspace topology from S^1. This is S^1 minus a point, which is... S^1 \ {0} ≅ R (an open interval, topologically). Wait, S^1 \ {pt} ≅ R. So S^1 \ {0} ≅ R, which is connected. But (R \ {0})^+ ≅ S^1 ∨ S^1 which is not simply connected and not ≅ R.

So indeed (R \ {0})^+ ≇ S^1 \ {0}. The topologies are different!

This means my approach of identifying (R^n \ X)^+ with S^n \ X is WRONG in general.

Hmm. So I need a different approach, or I need to use the fact that X is closed (from invariance of domain) more carefully.

OK so let me reconsider. The issue is that the one-point compactification of R^n \ X is not S^n \ X in general. 

But wait, for the case X = {0} in R: R \ {0} is not connected, hence not ≅ R. So the hypothesis R \ X ≅ R fails, and we don't need to worry about this case.

The question is: when R^n \ X ≅ R^n (so R^n \ X is connected, etc.), does the one-point compactification argument work?

Let me reconsider. If R^n \ X ≅ R^n, then (R^n \ X)^+ ≅ S^n. But (R^n \ X)^+ might not be S^n \ X (subspace topology). So I can't directly conclude S^n \ X ≅ S^n.

Hmm, so I need a different approach.

Let me think about this differently. 

Alternative approach: Use homology of the complement directly.

If X is closed in R^n (which we get from invariance of domain) and 0-dimensional, can we compute the homology of R^n \ X?

For X compact: Alexander duality gives H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X). And S^n \ X = (R^n \ X) ∪ {∞}. If R^n \ X ≅ R^n, then R^n \ X is contractible, so H̃_i(R^n \ X) = 0 for all i. 

Now S^n \ X = (R^n \ X) ∪ {∞}. The relationship between H_*(S^n \ X) and H_*(R^n \ X): S^n \ X is the one-point compactification of R^n \ X only if R^n \ X is locally compact and the topologies match, which we've seen might not be the case.

But actually, S^n \ X = (R^n \ X) ⊔ {∞} as a set, and the subspace topology from S^n. If X is closed in R^n, then R^n \ X is open in R^n, and S^n \ X is open in S^n (since X is closed in S^n when X is compact, or... if X is closed in R^n but unbounded, X is not closed in S^n).

Hmm, let me separate cases again.

Case 1: X is compact (closed and bounded in R^n).
Then X is closed in S^n. S^n \ X is open in S^n. By Alexander duality:
H̃_i(S^n \ X) ≅ H̃^{n-i-1}(X).
X is 0-dimensional compact. H̃^0(X) = c(X) - 1 (c = number of components), H̃^j(X) = 0 for j ≥ 1.
So H̃_{n-1}(S^n \ X) = c(X) - 1, and H̃_i(S^n \ X) = 0 for i ≠ 0, n-1 (and i ≠ n).

Now S^n \ X = (R^n \ X) ∪ {∞}. We can relate this to R^n \ X. Note that S^n \ X is the union of R^n \ X and {∞}, and {∞} is an open subset of S^n \ X (since X is compact, ∞ is an interior point of S^n \ X). Also, R^n \ X is open in S^n \ X. And (R^n \ X) ∩ {∞} = ∅. So S^n \ X = (R^n \ X) ⊔ {∞} (disjoint union of open sets)? No, {∞} is a single point, which is open in S^n \ X (since X compact ⟹ ∞ has a neighborhood in S^n \ X, so {∞} is... no, {∞} is not open unless ∞ is isolated in S^n \ X, which happens iff X is compact, which it is, but {∞} being open means ∞ is an isolated point of S^n \ X, which means there's an open set in S^n containing ∞ and contained in S^n \ X, i.e., S^n \ (some compact set) ⊂ S^n \ X, i.e., X ⊂ some compact set, which is true since X is compact. So {∞} is open in S^n \ X.

Wait, that's not right. {∞} is open in S^n \ X iff there's an open set V in S^n with V ∩ (S^n \ X) = {∞}, i.e., V \ {∞} ⊂ X. V is a neighborhood of ∞ in S^n, so V = S^n \ C for some compact C ⊂ R^n. V \ {∞} = R^n \ C. So we need R^n \ C ⊂ X, i.e., R^n \ X ⊂ C. Since R^n \ X is open and C is compact, R^n \ X ⊂ C means R^n \ X is bounded, which means X contains the exterior of some ball, i.e., X is co-bounded. But X is 0-dimensional (totally disconnected), so X can't contain the exterior of a ball (which is connected for n ≥ 2). For n = 1, X could contain a ray, but a ray is 1-dimensional. So for 0-dimensional X, X can't be co-bounded (for n ≥ 1). So {∞} is NOT open in S^n \ X (for 0-dimensional compact X, n ≥ 1).

OK so S^n \ X is connected (for n ≥ 2, since S^n \ X is (n-1)-connected... actually for 0-dimensional compact X, S^n \ X is path-connected for n ≥ 2). And S^n \ X = (R^n \ X) ∪ {∞} where ∞ is a limit point of R^n \ X in S^n \ X.

So S^n \ X is a connected space, and R^n \ X is a dense open subset (dense because ∞ is a limit point).

Now, if R^n \ X ≅ R^n, then R^n \ X is contractible. What can we say about S^n \ X?

S^n \ X is obtained from R^n \ X by adding one point (∞). If R^n \ X ≅ R^n, then S^n \ X is obtained from R^n by adding one limit point. This is like a compactification of R^n. 

Hmm, but different compactifications of R^n give different spaces. The one-point compactification gives S^n. But S^n \ X might be a different compactification.

Actually, S^n \ X is a specific compactification of R^n \ X (the "end compactification" determined by how X sits in S^n). If R^n \ X ≅ R^n, then S^n \ X is a compactification of R^n. 

For X compact, S^n \ X is an open subset of S^n (since X is closed in S^n). It's an open subset of S^n that contains ∞ and is connected. By Alexander duality, H̃_{n-1}(S^n \ X) = c(X) - 1.

If R^n \ X ≅ R^n (contractible), what is H̃_{n-1}(S^n \ X)?

We can use the long exact sequence. S^n \ X = (R^n \ X) ∪ {∞}. Consider the pair (S^n \ X, R^n \ X). The relative homology H_*(S^n \ X, R^n \ X) ≅ H̃_{*-1}(point) by... hmm, (S^n \ X) / (R^n \ X) = {∞} (a point) if R^n \ X is closed in S^n \ X. But R^n \ X is open in S^n \ X (and dense), not closed. So the quotient is not a point.

This approach is getting complicated. Let me try a different angle.

Alternative: Use the fact that R^n \ X ≅ R^n implies specific topological properties, and derive a contradiction if X is nonempty.

Key property: R^n is contractible. So R^n \ X is contractible. 

For n ≥ 2 and X compact 0-dimensional nonempty: By Alexander duality, H̃_{n-1}(S^n \ X) = c(X) - 1 ≥ 0. If c(X) ≥ 2, then H̃_{n-1}(S^n \ X) > 0.

Now, S^n \ X is an open subset of S^n containing ∞. We can write S^n \ X = (R^n \ X) ∪ {∞}. 

Consider the inclusion R^n \ X ↪ S^n \ X. If R^n \ X is contractible, what is the effect on homology?

Actually, let me use a different tool. Consider the long exact sequence of the pair (S^n, X):
... → H_i(X) → H_i(S^n) → H_i(S^n, X) → H_{i-1}(X) → ...
By excision, H_i(S^n, X) ≅ H_i(S^n \ X, {∞}) ... no, excision gives H_i(S^n, X) ≅ H_i(S^n \ X, U) for some neighborhood U of X... this is getting complicated.

Let me try yet another approach. 

Direct approach using homology of R^n \ X:

For X compact 0-dimensional in R^n (n ≥ 2), we can compute H_*(R^n \ X) using Alexander duality applied to S^n.

S^n \ X = (R^n \ X) ⊔ {∞} as a set, but topologically ∞ is a limit point. 

Actually, here's a cleaner way. Consider S^n with X ⊂ R^n ⊂ S^n, X compact. Let Y = S^n \ X. Y is an open subset of S^n. Y = (R^n \ X) ∪ {∞}. 

Now ∞ ∈ Y, and Y is an n-manifold (open subset of S^n). R^n \ X is also an n-manifold (open subset of R^n, since X is closed). 

The point ∞ in Y has a neighborhood in Y homeomorphic to R^n (since Y is an n-manifold). Specifically, a neighborhood of ∞ in Y is S^n \ C for some compact C ⊂ R^n with C ⊃ X, and S^n \ C ≅ R^n (stereographic projection from a point in C). So ∞ has a neighborhood in Y homeomorphic to R^n.

Now, Y = (R^n \ X) ∪ {∞}, and ∞ has a neighborhood in Y that's homeomorphic to R^n and doesn't intersect X. So locally near ∞, Y looks like R^n.

If R^n \ X ≅ R^n, then Y = (something ≅ R^n) ∪ {∞} where ∞ is attached in a specific way. 

Hmm, I think I need to use a more sophisticated tool. Let me think about the homology of R^n \ X directly.

For X compact in R^n: Use the fact that R^n \ X = S^n \ (X ∪ {∞}) = S^n \ X* where X* = X ∪ {∞} is compact in S^n. By Alexander duality:
H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).

X* = X ∪ {∞}. X is 0-dimensional compact, and ∞ is an isolated point of X* (since X is compact, ∞ has a neighborhood in S^n not meeting X, so ∞ is isolated in X*). So X* = X ⊔ {∞} (topological disjoint union). 

H̃^0(X*) = H̃^0(X ⊔ {∞}) = (c(X) + 1) - 1 = c(X) (where c(X) = number of components of X). Wait: H̃^0 of a space with k components is k - 1. X* has c(X) + 1 components (c(X) from X plus 1 from {∞}). So H̃^0(X*) = c(X) + 1 - 1 = c(X). And H̃^j(X*) = 0 for j ≥ 1.

So H̃_i(R^n \ X) ≅ H̃^{n-i-1}(X*):
- i = n-1: H̃_{n-1}(R^n \ X) = H̃^0(X*) = c(X).
- i ≠ n-1, i ≠ 0: H̃_i(R^n \ X) = 0.
- i = 0: H̃_0(R^n \ X) = H̃^{n-1}(X*) = 0 (for n ≥ 2).

So for n ≥ 2, X compact 0-dimensional:
H̃_{n-1}(R^n \ X) = c(X) (number of components of X).
All other reduced homology is 0.

If R^n \ X ≅ R^n (contractible), then H̃_i(R^n \ X) = 0 for all i. So c(X) = 0, meaning X has 0 components, i.e., X = ∅!

This is the key result. For n ≥ 2 and X compact, R^n \ X ≅ R^n ⟹ X = ∅.

Now for n = 1: X compact 0-dimensional in R. X* = X ∪ {∞} in S^1. H̃_0(R \ X) = H̃^0(X*) = c(X). If R \ X ≅ R (connected), H̃_0(R \ X) = 0, so c(X) = 0, X = ∅. ✓

And for n = 1, we also need R \ X to be connected, which already forces X = ∅ (as argued earlier). But the homology argument also works.

Now, what about X not compact? We showed X must be closed (invariance of domain). But X could be closed and unbounded.

For X closed and unbounded in R^n: X* = cl_{S^n}(X) = X ∪ {∞} (since X is unbounded, ∞ is a limit point). X* is compact (closed in S^n). 

R^n \ X = S^n \ X* (since S^n \ X* = S^n \ (X ∪ {∞}) = (R^n \ X) ∩ (S^n \ {∞}) = R^n \ X). Wait: S^n \ (X ∪ {∞}) = (S^n \ X) \ {∞} = ((R^n \ X) ∪ {∞}) \ {∞} = R^n \ X. Yes! So R^n \ X = S^n \ X*.

By Alexander duality: H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).

Now X* = X ∪ {∞} where ∞ is a limit point of X (not isolated). X is 0-dimensional. What is the dimension of X*? 

X* is the one-point compactification of X (if X is locally compact) or just the closure in S^n. X is 0-dimensional and closed in R^n. If X is unbounded, X is not compact, but it's locally compact (closed subset of R^n is locally compact). So X* = X^+ (one-point compactification of X). 

The dimension of X*: the one-point compactification of a 0-dimensional locally compact space is 0-dimensional (I believe this is true for non-compact spaces; the one-point compactification of a 0-dimensional locally compact non-compact space is 0-dimensional). 

Hmm, actually I need to check this. If X is 0-dimensional locally compact non-compact, is X^+ 0-dimensional? 

X^+ = X ∪ {∞}. For X^+ to be 0-dimensional, every point needs a clopen neighborhood. For points in X, they have clopen neighborhoods in X (since X is 0-dimensional), and these are also clopen in X^+ if they're compact (clopen compact subsets of X are clopen in X^+). Since X is locally compact and 0-dimensional, every point has a compact clopen neighborhood. So points in X have clopen neighborhoods in X^+. 

For ∞: ∞ has a neighborhood basis of sets X^+ \ K for K compact in X. X^+ \ K is clopen in X^+ iff K is clopen in X^+... hmm, X^+ \ K is open (by definition of one-point compactification). Is it closed? X^+ \ K is closed iff K is open in X^+. K is open in X^+ iff K is open in X (and K ⊂ X). So X^+ \ K is clopen iff K is clopen in X (and compact). Since X is 0-dimensional and locally compact, we can find compact clopen K containing any given compact set... actually, we need: for any compact K' in X, there's a compact clopen K in X with K' ⊂ K. Then X^+ \ K is a clopen neighborhood of ∞ contained in X^+ \ K'. 

Is this true? In a 0-dimensional locally compact space, every compact set is contained in a compact clopen set. I believe this is true for locally compact Hausdorff 0-dimensional spaces (they have a basis of compact clopen sets, and compact sets can be covered by finitely many, whose union is compact clopen). 

Actually, let me verify: X is 0-dimensional locally compact Hausdorff. Then X has a basis of compact clopen sets (since 0-dimensional gives clopen basis, and locally compact gives compact neighborhoods; combining, we get compact clopen neighborhoods). For a compact set K' in X, cover K' with finitely many compact clopen sets U_1, ..., U_m. Their union U = U_1 ∪ ... ∪ U_m is clopen (finite union of clopen is clopen) and compact (finite union of compact). And K' ⊂ U. ✓

So X^+ is 0-dimensional. Therefore X* = X^+ is 0-dimensional (compact).

Now apply Alexander duality: H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).

X* is 0-dimensional compact. H̃^0(X*) = c(X*) - 1 (number of components minus 1). H̃^j(X*) = 0 for j ≥ 1.

So H̃_{n-1}(R^n \ X) = H̃^0(X*) = c(X*) - 1.

If R^n \ X ≅ R^n (contractible), H̃_{n-1}(R^n \ X) = 0, so c(X*) = 1, meaning X* is connected.

X* is 0-dimensional and connected, so X* is a single point. 

X* = X ∪ {∞}. If X* is a single point, then X* = {∞}, so X = ∅. (Because if X is nonempty, X* has at least 2 points: some point of X and ∞.)

Wait, X* = X ∪ {∞}. If X ≠ ∅, then X* has at least 2 points (∞ and some point of X). A 0-dimensional connected space with ≥ 2 points is impossible (0-dimensional Hausdorff spaces are totally disconnected, so connected components are points). So X* connected and 0-dimensional ⟹ X* is a single point ⟹ X = ∅. ✓

So in all cases (X compact or unbounded), R^n \ X ≅ R^n ⟹ X = ∅.

Let me also handle n = 1 with this approach. For n = 1, X closed 0-dimensional in R. 

If X compact: X* = X ∪ {∞} (disjoint, ∞ isolated). H̃_0(R \ X) = H̃^0(X*) = c(X*). Wait, for n=1: H̃_i(R \ X) = H̃^{1-i-1}(X*) = H̃^{-i}(X*). 

Hmm, for n=1: H̃_i(S^1 \ X*) ≅ H̃^{1-i-1}(X*) = H̃^{-i}(X*).

For i=0: H̃_0(S^1 \ X*) = H̃^0(X*) = c(X*) - 1.
For i=1: H̃_1(S^1 \ X*) = H̃^{-1}(X*) = Z if X* = ∅, 0 otherwise.

R \ X = S^1 \ X*. If R \ X ≅ R (contractible, connected), H̃_0 = 0, so c(X*) = 1. X* 0-dimensional connected ⟹ single point. If X compact, X* = X ⊔ {∞}, c(X*) = c(X) + 1. c(X*) = 1 ⟹ c(X) = 0 ⟹ X = ∅. ✓

If X unbounded: X* = X ∪ {∞} (∞ is limit point). X* 0-dimensional compact. c(X*) = 1 ⟹ X* = {pt} ⟹ X = ∅. ✓

Great, so the argument works for all n ≥ 1.

Let me also handle n = 0. R^0 = {pt}. 0-dimensional subset X of R^0: X = ∅ or X = {pt}. R^0 \ ∅ = {pt} ≅ R^0. R^0 \ {pt} = ∅ ≇ R^0. So X = ∅. (Trivial case, and our argument with S^0 doesn't directly apply since S^0 is disconnected, but the result holds.)

Now let me also verify the key step: Alexander duality for X* compact in S^n.

Alexander duality (for compact locally contractible... or more generally for compact subsets): For any compact subset K of S^n:
H̃_i(S^n \ K) ≅ H̃^{n-i-1}(K) for all i.
This is the Alexander duality theorem, which holds for all compact subsets K of S^n (using Čech cohomology). ✓

And 0-dimensional compact spaces have trivial Čech cohomology above degree 0, and H̃^0 = (number of components) - 1. ✓ (For compact Hausdorff spaces, Čech cohomology agrees with sheaf cohomology, and for 0-dimensional spaces, H̃^0 = number of connected components - 1, H̃^j = 0 for j > 0.)

Actually, I should be careful: for 0-dimensional compact spaces, the number of connected components equals the number of points (since totally disconnected), so c(X*) = |X*| (number of points). But we don't need this; we just need c(X*) = 1 ⟹ X* is a point.

Hmm wait, for a 0-dimensional compact space, connected components are points (totally disconnected), so c(X*) = |X*|. c(X*) = 1 ⟹ |X*| = 1 ⟹ X* is a single point. ✓

OK so the proof is:

1. Suppose R^n \ X ≅ R^n. 
2. By invariance of domain, R^n \ X is open in R^n, so X is closed in R^n.
3. Let X* = cl_{S^n}(X) (closure in the one-point compactification S^n of R^n). Then X* is compact, and R^n \ X = S^n \ X*.
4. X is 0-dimensional and closed in R^n (hence locally compact). X* is the one-point compactification of X (if X non-compact) or X ⊔ {∞} (if X compact). In either case, X* is 0-dimensional and compact.
5. By Alexander duality: H̃_i(R^n \ X) = H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*).
6. X* is 0-dimensional compact, so H̃^j(X*) = 0 for j ≥ 1, and H̃^0(X*) = c(X*) - 1.
7. So H̃_{n-1}(R^n \ X) = c(X*) - 1, and all other reduced homology of R^n \ X is 0 (for n ≥ 2; for n = 1, H̃_0(R \ X) = c(X*) - 1).
8. R^n \ X ≅ R^n is contractible, so H̃_i(R^n \ X) = 0 for all i.
9. Therefore c(X*) - 1 = 0, so c(X*) = 1.
10. X* is 0-dimensional and compact, hence totally disconnected. c(X*) = 1 means X* is connected, so X* is a single point.
11. X* = X ∪ {∞}. If X ≠ ∅, then |X*| ≥ 2 (contains ∞ and a point of X). So X* being a single point means X = ∅.

Therefore X = ∅. The answer is YES.

Wait, I need to double-check step 4 more carefully. Is X* always 0-dimensional?

Case 1: X is compact (bounded). Then X* = X ∪ {∞} where ∞ is an isolated point (since X is compact, there's a neighborhood of ∞ in S^n not meeting X). So X* = X ⊔ {∞} (topological sum). X is 0-dimensional, {∞} is 0-dimensional, so X* is 0-dimensional. ✓

Case 2: X is unbounded (closed in R^n but not compact). Then X* = X ∪ {∞} where ∞ is a limit point of X. X is locally compact (closed in R^n) and 0-dimensional. X* is the one-point compactification X^+ of X. As argued, X^+ is 0-dimensional (since X is locally compact Hausdorff 0-dimensional). ✓

But wait, is X locally compact? X is closed in R^n. A closed subset of a locally compact Hausdorff space is locally compact. R^n is locally compact Hausdorff. So X is locally compact. ✓

And is X 0-dimensional in the sense that gives X^+ 0-dimensional? X is 0-dimensional (covering dimension 0), which for separable metric spaces means it has a basis of clopen sets. Combined with locally compact, X has a basis of compact clopen sets. Then X^+ is 0-dimensional as argued. ✓

Hmm, but actually I want to make sure X has a basis of compact clopen sets. X is 0-dimensional (has clopen basis) and locally compact (has compact neighborhoods). For each point x and neighborhood U of x, there's a clopen V with x ∈ V ⊂ U, and a compact neighborhood K of x with K ⊂ V. Then x ∈ int(K) ∩ V, which is open. There's a clopen W with x ∈ W ⊂ int(K) ∩ V. W is clopen in X, W ⊂ K (compact), so W is compact (closed subset of compact K, and W is closed since clopen). So W is a compact clopen neighborhood of x inside U. ✓

So X has a basis of compact clopen sets, and X^+ is 0-dimensional. ✓

Also, I should verify step 3: R^n \ X = S^n \ X*.

S^n = R^n ∪ {∞}. X ⊂ R^n. X* = cl_{S^n}(X). 

If X is compact: X* = X (X is already closed in S^n since compact subsets of R^n are closed in S^n... wait, is that right? X compact in R^n ⟹ X is closed in R^n and bounded. In S^n, X is closed iff X is compact (as a subset of S^n). X is compact as a subset of S^n iff X is compact as a subset of R^n (since S^n is Hausdorff and X ⊂ R^n ⊂ S^n, compactness is the same). So X is closed in S^n. So X* = X. Then S^n \ X* = S^n \ X = (R^n \ X) ∪ {∞}. But R^n \ X = S^n \ (X ∪ {∞}) = (S^n \ X) \ {∞} = (R^n \ X) ∪ {∞} \ {∞} = R^n \ X. Hmm, that's circular.

Let me redo. S^n \ X* = S^n \ X (since X* = X when X compact). S^n \ X = (R^n \ X) ∪ {∞} (since ∞ ∉ X). But R^n \ X is what we want, not (R^n \ X) ∪ {∞}. 

So R^n \ X ≠ S^n \ X* when X is compact. Instead, R^n \ X = S^n \ (X ∪ {∞}) = S^n \ X* where X* = X ∪ {∞}.

Hmm, I think I confused myself. Let me redefine.

Let X* = X ∪ {∞} (as a subset of S^n, always adding ∞). Then:
S^n \ X* = S^n \ (X ∪ {∞}) = (S^n \ X) ∩ (S^n \ {∞}) = (S^n \ X) ∩ R^n = R^n \ X. ✓

So R^n \ X = S^n \ X* where X* = X ∪ {∞}. This is always true, regardless of whether X is compact.

Now X* = X ∪ {∞}. Is X* compact? X* is compact iff X* is closed in S^n. X* = X ∪ {∞}. X is closed in R^n (from invariance of domain). 

If X is bounded (compact): X is closed in S^n, and {∞} is closed in S^n, so X* = X ∪ {∞} is closed in S^n, hence compact. ✓

If X is unbounded: X is closed in R^n but not in S^n (closure in S^n is X ∪ {∞} = X*). So X* = cl_{S^n}(X), which is closed in S^n, hence compact. ✓

So X* is always compact. ✓

And X* is 0-dimensional:
- If X compact: X* = X ⊔ {∞} (∞ isolated), both 0-dimensional, so X* is 0-dimensional. ✓
- If X unbounded: X* = cl_{S^n}(X) = X ∪ {∞} = X^+ (one-point compactification of X, since X is locally compact non-compact). X^+ is 0-dimensional as argued. ✓

Now Alexander duality: H̃_i(S^n \ X*) ≅ H̃^{n-i-1}(X*). And S^n \ X* = R^n \ X. So H̃_i(R^n \ X) ≅ H̃^{n-i-1}(X*). ✓

X* is 0-dimensional compact. H̃^0(X*) = c(X*) - 1, H̃^j(X*) = 0 for j ≥ 1.

H̃_{n-1}(R^n \ X) = H̃^0(X*) = c(X*) - 1.
H̃_i(R^n \ X) = 0 for i ≠ n-1 (and i ≥ 1). (For n ≥ 2.)
For n = 1: H̃_0(R \ X) = H̃^0(X*) = c(X*) - 1.

R^n \ X ≅ R^n ⟹ contractible ⟹ H̃_i = 0 for all i ⟹ c(X*) = 1.

X* 0-dimensional compact ⟹ totally disconnected ⟹ c(X*) = |X*| (number of points). c(X*) = 1 ⟹ |X*| = 1 ⟹ X* = {∞} (since ∞ ∈ X*) ⟹ X = ∅. ✓

The proof is complete. Let me write it up cleanly.

Actually, let me reconsider one thing: for n=1, the reduced homology. H̃_0(R \ X) = c(X*) - 1. R \ X ≅ R means R \ X is connected, so H̃_0(R \ X) = 0, so c(X*) = 1. Same conclusion. ✓

And for n=1, H̃_i(R \ X) for i ≥ 1: H̃_i = H̃^{-i}(X*) = 0 for i ≥ 1 (since -i < 0 and X* is nonempty). R is contractible so H̃_i = 0 for i ≥ 1. ✓ Consistent.

Now let me also think about whether I need X to be nonempty for the argument. If X = ∅, then X* = {∞}, c(X*) = 1, H̃_{n-1}(R^n) = 0 = c(X*) - 1 = 0. ✓ Consistent. And R^n \ ∅ = R^n ≅ R^n. ✓

So the argument shows: R^n \ X ≅ R^n ⟺ X = ∅ (for 0-dimensional X). The forward direction is what we proved. The backward direction is trivial.

Let me write the final proof.

One more check: the problem says "0-dimensional subset." I'm interpreting this as covering dimension 0. For subsets of R^n (separable metric spaces), this is equivalent to having a basis of clopen sets, which implies totally disconnected. The key properties I use:
1. 0-dimensional ⟹ totally disconnected (for the empty interior argument, though I ended up not needing this in the final proof).
2. 0-dimensional compact ⟹ H̃^j = 0 for j ≥ 1, H̃^0 = c - 1 (Čech cohomology).
3. 0-dimensional locally compact ⟹ one-point compactification is 0-dimensional.

All of these are standard results in dimension theory.

Actually, in the final proof, I don't even need the "empty interior" argument or invariance of domain! Let me re-examine.

Wait, I do need X to be closed for X* to be well-behaved... actually no. X* = X ∪ {∞} is always compact (as shown). And X* is 0-dimensional... but is X* 0-dimensional if X is not closed?

If X is not closed in R^n, then X is not locally compact (a non-closed subset of a Hausdorff locally compact space is not locally compact... actually that's not true. A subset of a locally compact Hausdorff space is locally compact iff it's the intersection of an open set and a closed set, i.e., locally closed). 

If X is not closed, X might not be locally compact, and X* = X ∪ {∞} might not be the one-point compactification, and might not be 0-dimensional.

Hmm, but actually X* = X ∪ {∞} as a subset of S^n. Is X* 0-dimensional? 

If X is not closed, let X̄ = cl_{R^n}(X). Then X* = cl_{S^n}(X) = X̄ ∪ {∞} (if X is unbounded) or X̄ (if X is bounded). Wait, X* = X ∪ {∞}, not cl_{S^n}(X). Let me re-examine.

I defined X* = X ∪ {∞} (just the set X plus the point ∞). This is a subset of S^n. Is it compact? X* is compact iff X* is closed in S^n. X* = X ∪ {∞}. 

If X is not closed in R^n: X ∪ {∞} is closed in S^n iff (X ∪ {∞}) ∩ R^n = X is closed in R^n (since S^n \ {∞} = R^n is open, a subset of S^n containing ∞ is closed iff its intersection with R^n is closed in R^n... actually that's not quite right either).

Let me think about it directly. X* = X ∪ {∞} is closed in S^n iff S^n \ X* = R^n \ X is open in S^n. R^n \ X is open in S^n iff R^n \ X is open in R^n (since R^n is open in S^n) and... no, a subset of S^n is open iff it's open in the topology of S^n. R^n \ X is open in S^n iff for every point p ∈ R^n \ X, there's an open set in S^n containing p and contained in R^n \ X. Since R^n is open in S^n, open sets in R^n are open in S^n. So R^n \ X is open in S^n iff R^n \ X is open in R^n iff X is closed in R^n.

So if X is not closed in R^n, X* = X ∪ {∞} is NOT closed in S^n, hence not compact. Then Alexander duality doesn't apply directly.

So I DO need X to be closed, and I get that from invariance of domain. Good.

So the proof structure is:
1. R^n \ X ≅ R^n ⟹ (by invariance of domain) R^n \ X is open in R^n ⟹ X is closed in R^n.
2. X closed in R^n, 0-dimensional ⟹ X is locally compact, X* = X ∪ {∞} is compact and 0-dimensional.
3. R^n \ X = S^n \ X* (set-theoretically and topologically).
4. Alexander duality: H̃_i(R^n \ X) ≅ H̃^{n-i-1}(X*).
5. X* 0-dimensional compact ⟹ H̃^{n-i-1}(X*) = 0 except when n-i-1 = 0, i.e., i = n-1, where it's c(X*) - 1.
6. R^n \ X ≅ R^n ⟹ contractible ⟹ H̃_i = 0 for all i ⟹ c(X*) = 1.
7. X* 0-dimensional compact ⟹ totally disconnected ⟹ c(X*) = |X*| ⟹ |X*| = 1 ⟹ X* = {∞} ⟹ X = ∅.

This is clean. Let me write it up.

Hmm, actually one more thing. For step 2, when X is compact (bounded), X* = X ∪ {∞} where ∞ is isolated. X* is the topological disjoint union X ⊔ {∞}. X is 0-dimensional, {∞} is 0-dimensional, so X* is 0-dimensional. And X* is compact (closed in S^n). ✓

When X is unbounded, X* = X ∪ {∞} = X^+ (one-point compactification of X, since X is locally compact non-compact). X^+ is 0-dimensional (as argued). And X^+ is compact. ✓

Also, I should verify that X* = X ∪ {∞} being compact implies it's closed in S^n (which it is, since S^n is Hausdorff and compact subsets are closed). And then S^n \ X* = R^n \ X is open in S^n, hence open in R^n. This is consistent with step 1.

Actually, I realize that step 1 (invariance of domain) gives X closed, and then X* is compact (closed in S^n), and Alexander duality applies. But actually, do I even need invariance of domain? If I just define X* = cl_{S^n}(X) (the closure, not just X ∪ {∞}), then X* is always compact (closed in S^n). But then S^n \ X* might not equal R^n \ X (it would be R^n \ cl_{R^n}(X) if X is bounded, or something else).

So I do need invariance of domain to ensure X is closed, so that X* = X ∪ {∞} is compact and S^n \ X* = R^n \ X.

Alternatively, I could use cl_{S^n}(X) and note that S^n \ cl_{S^n}(X) ⊂ R^n \ X, but the inclusion might be strict if X is not closed. So invariance of domain is needed.

OK, I'm confident the proof is correct. Let me write it up.

Let me also think about whether there's a simpler proof that doesn't use Alexander duality or invariance of domain.

Simpler approach for n=1: R \ X ≅ R means R \ X is connected. R \ X ⊂ R \ {p} for any p ∈ X. R \ {p} has two components. If X is nonempty, R \ X is a subset of R \ {p} that doesn't contain p, so it's contained in the union of two separated intervals, hence disconnected (as long as X is nonempty and 0-dimensional, which means X doesn't contain an interval, so R \ X intersects both components). So X = ∅. This is elementary.

For n ≥ 2: The homology argument via Alexander duality seems necessary. I don't think there's a purely elementary argument.

Actually, for n=2, one could use the fundamental group. If X is nonempty and compact, take p ∈ X. A small loop around p in R^2 \ X is non-contractible (it links with p). So π_1(R^2 \ X) ≠ 0, but π_1(R^2) = 0. But this requires X to be "nice enough" that a loop around p doesn't contract, which needs some argument. And for non-compact X, it's trickier. The Alexander duality approach is cleaner and works for all n.

Let me write the final proof now.

Actually, I want to make sure about one subtle point: the use of Čech cohomology in Alexander duality. The standard Alexander duality theorem states:

For any compact subset K of S^n:
H̃_i(S^n \ K; G) ≅ H̃^{n-i-1}(K; G) for all i,
where the right side is Čech cohomology.

For 0-dimensional compact Hausdorff spaces, Čech cohomology: H̃^0(K) = (number of connected components) - 1, and H̃^j(K) = 0 for j ≥ 1. This is because 0-dimensional spaces have a basis of clopen sets, so the Čech complex is trivial in positive degrees.

Actually, for a 0-dimensional compact space, connected components = points (totally disconnected), so the number of components = cardinality of K. But we don't need the exact count, just that c(X*) = 1 implies X* is a point.

Also, I should note: for a totally disconnected compact space, H̃^0 = |K| - 1 (number of points minus 1) since each point is a component. So H̃^0(X*) = |X*| - 1. Setting this to 0 gives |X*| = 1.

Wait, but X* might be uncountable. H̃^0 for a compact space with infinitely many components... H̃^0(K) is the group of locally constant functions on K modulo constants, which for a totally disconnected compact space is related to the Boolean algebra of clopen sets. For a finite space with k points, H̃^0 = k - 1 (as a group, Z^{k-1}). For an infinite totally disconnected compact space, H̃^0 is more complicated (it's not just |K| - 1).

Hmm, so I need to be more careful. H̃^0(X*) = 0 means X* is connected. For a 0-dimensional (
