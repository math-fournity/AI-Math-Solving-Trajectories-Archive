# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Find the residue of the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) at \( z = 0 \).       — 题目文本
#   Okay, so I need to find the residue of the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) at \( z = 0 \). Hmm, residues are related to Laurent series expansions around the point in question, right? And the residue itself is the coefficient of the \( \frac{1}{z} \) term in that expansion. Let me recall how that works.

First, \( z = 0 \) is a singularity of the function \( f(z) \). Since we're dealing with \( \sin\left(\frac{1}{z^2}\right) \), which has an essential singularity at \( z = 0 \) because as \( z \) approaches 0, \( \frac{1}{z^2} \) goes to infinity, and the sine function oscillates wildly. So multiplying that by \( z^2 \), the whole function \( f(z) \) will have an essential singularity at 0 as well. Therefore, to find the residue, I need to expand \( f(z) \) in a Laurent series around 0 and find the coefficient of \( \frac{1}{z} \).

Let me start by recalling the Taylor series expansion for \( \sin(w) \), which is \( \sin(w) = w - \frac{w^3}{3!} + \frac{w^5}{5!} - \cdots \). So if I substitute \( w = \frac{1}{z^2} \), then \( \sin\left(\frac{1}{z^2}\right) = \frac{1}{z^2} - \frac{1}{3! z^6} + \frac{1}{5! z^{10}} - \cdots \). Then multiplying by \( z^2 \), the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) becomes:

\( f(z) = z^2 \left( \frac{1}{z^2} - \frac{1}{6 z^6} + \frac{1}{120 z^{10}} - \cdots \right) \)

Let me compute that term by term:

First term: \( z^2 \times \frac{1}{z^2} = 1 \)

Second term: \( z^2 \times \left( -\frac{1}{6 z^6} \right) = -\frac{1}{6 z^4} \)

Third term: \( z^2 \times \frac{1}{120 z^{10}} = \frac{1}{120 z^8} \)

Fourth term: \( z^2 \times \left( -\frac{1}{5040 z^{14}} \right) = -\frac{1}{5040 z^{12}} \)

And so on. So each term alternates in sign and involves even negative powers of z. Wait a second, but the Laurent series expansion here seems to have terms with exponents of z decreasing by 4 each time? Let's see:

First term: exponent 0 (since it's 1)

Second term: exponent -4

Third term: exponent -8

Fourth term: exponent -12

Etc.

But the residue is the coefficient of \( z^{-1} \). However, in this expansion, all exponents are 0, -4, -8, -12, etc. So there is no \( z^{-1} \) term. That would imply that the coefficient of \( z^{-1} \) is zero, hence the residue is zero.

But wait, let me check if I made a mistake here. Let me go through the steps again.

Starting with the expansion of \( \sin(w) \):

\( \sin(w) = \sum_{n=0}^{\infty} \frac{(-1)^n w^{2n+1}}{(2n+1)!} \)

Therefore, substituting \( w = \frac{1}{z^2} \):

\( \sin\left(\frac{1}{z^2}\right) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} \left( \frac{1}{z^2} \right)^{2n+1} = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n -2} \)

Then, multiplying by \( z^2 \):

\( f(z) = z^2 \times \sin\left(\frac{1}{z^2}\right) = z^2 \times \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n -2} = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n} \)

So each term in the series is \( \frac{(-1)^n}{(2n+1)!} z^{-4n} \). So when n=0, term is \( \frac{1}{1!} z^{0} = 1 \). When n=1, term is \( -\frac{1}{3!} z^{-4} \). When n=2, term is \( \frac{1}{5!} z^{-8} \), etc.

So indeed, the exponents here are 0, -4, -8, -12, etc. All exponents are multiples of -4. Therefore, there are no terms with exponent -1. Therefore, the coefficient of \( z^{-1} \) is zero, so the residue at z=0 is zero.

But I need to make sure that I didn't miss any terms or make any miscalculations. Let me see.

Alternatively, maybe there's another approach. Since the residue is the coefficient of \( z^{-1} \), and the function is even, or has some symmetry. Wait, \( f(z) = z^2 \sin(1/z^2) \). Let me check if it's an even function. Let's substitute \( z \) with \( -z \):

\( f(-z) = (-z)^2 \sin\left( \frac{1}{(-z)^2} \right) = z^2 \sin\left( \frac{1}{z^2} \right) = f(z) \). So yes, it's an even function. Therefore, its Laurent series expansion about 0 will only have even exponents. Since the residue is the coefficient of \( z^{-1} \), which is an odd exponent term, and since all terms in the expansion are even exponents (0, -4, -8, etc.), there can't be a \( z^{-1} \) term. Therefore, the residue is zero.

Alternatively, using the residue formula for essential singularities. But I think for essential singularities, there is no direct formula other than expanding the Laurent series. But since this function is a product of a polynomial and a sine function with a singularity, expanding the Laurent series seems the way to go.

Alternatively, maybe using integration. The residue is \( \frac{1}{2\pi i} \int_{C} f(z) dz \), where C is a small circle around 0. But integrating this directly might be complicated. However, since we can expand the Laurent series and see that there is no \( z^{-1} \) term, the integral would be zero, hence residue is zero.

Another way to think about it: If I consider the Laurent series of \( \sin(1/z^2) \), which is \( \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} z^{-4n -2} \), then multiplying by \( z^2 \) gives \( \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} z^{-4n} \), which as we saw has exponents 0, -4, -8, etc. So again, no \( z^{-1} \).

Alternatively, could there be a mistake in substitution? Let me check for n=0: term is 1/(1!) z^{0}, correct. For n=1: term is -1/(6) z^{-4}, correct. So no, seems correct.

Therefore, since all terms are of the form \( z^{-4n} \), there's no term with exponent -1, so residue is 0.

Thus, the residue of \( f(z) \) at z=0 is 0.

**Final Answer**
The residue of \( f(z) \) at \( z = 0 \) is \boxed{0}.
</think>

To find the residue of the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) at \( z = 0 \), we need to expand the function in a Laurent series around \( z = 0 \) and identify the coefficient of the \( \frac{1}{z} \) term.

1. **Taylor series expansion of \( \sin(w) \)**:
   \[
   \sin(w) = w - \frac{w^3}{3!} + \frac{w^5}{5!} - \cdots
   \]
   Substituting \( w = \frac{1}{z^2} \), we get:
   \[
   \sin\left(\frac{1}{z^2}\right) = \frac{1}{z^2} - \frac{1}{3! z^6} + \frac{1}{5! z^{10}} - \cdots
   \]

2. **Multiplying by \( z^2 \)**:
   \[
   z^2 \sin\left(\frac{1}{z^2}\right) = z^2 \left( \frac{1}{z^2} - \frac{1}{6 z^6} + \frac{1}{120 z^{10}} - \cdots \right)
   \]
   Simplifying term by term:
   \[
   z^2 \sin\left(\frac{1}{z^2}\right) = 1 - \frac{1}{6 z^4} + \frac{1}{120 z^8} - \cdots
   \]

3. **Laurent series expansion**:
   The resulting series is:
   \[
   z^2 \sin\left(\frac{1}{z^2}\right) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n}
   \]
   This series contains only terms with exponents \( 0, -4, -8, -12, \ldots \), which are all even multiples of -4. There is no term with the exponent -1.

Since there is no \( \frac{1}{z} \) term in the Laurent series expansion, the coefficient of \( \frac{1}{z} \) is zero. Therefore, the residue of \( f(z) \) at \( z = 0 \) is \(\boxed{0}\).  — 标准解答
#   The problem asks for the best bound constant C such that sup_{R^3/D} |u| ≤ C · sup_{∂D} |g| for the Helmholtz equation exterior Dirichlet problem.

Let me think about this carefully. This is a classic problem in scattering theory / PDE theory.

The exterior Dirichlet problem for Helmholtz: Δu + k²u = 0 in R³\D, u = g on ∂D, Sommerfeld radiation condition at infinity.

The question asks for the best (optimal) constant C in the maximum principle-type bound.

For the Laplace equation (k=0), the maximum principle gives C = 1 (harmonic functions attain max on boundary). But for Helmholtz (k ≠ 0), the maximum principle doesn't directly apply because the equation has the +k²u term, so it's not elliptic in the maximum principle sense.

Wait, actually for Helmholtz, the maximum principle fails. The solution can have interior values larger than boundary values. So the question is about the best constant.

Let me think about this more carefully. This is related to the work of various authors on maximum principles for Helmholtz equations.

Actually, let me reconsider. The problem is asking for the best bound constant C. This is a well-studied question.

For the Helmholtz equation, there's a result that relates to the "maximum principle" type estimates. The key reference is the work on the maximum modulus of solutions to the Helmholtz equation.

Actually, I recall that for the exterior problem, there's a classical result. Let me think about what the answer should be.

For the Helmholtz equation in exterior domains, the solution can be represented using the Green's function / single and double layer potentials. The maximum of |u| in the exterior can exceed the maximum of |g| on the boundary.

Hmm, but the problem says "determine the best bound constant C". This suggests there's a specific known answer.

Let me think about this differently. For the Helmholtz equation with radiation condition, the exterior Dirichlet problem has a unique solution. The question is about the operator norm of the solution operator from C(∂D) to C(R³\D).

Actually, I think the answer might be C = 1, but that can't be right for Helmholtz since the maximum principle doesn't hold.

Wait, let me reconsider. For the Helmholtz equation, there IS a version of the maximum principle. The key insight is that for the exterior problem with radiation condition, the solution decays at infinity (like 1/r), so the supremum is attained either on the boundary or in the interior.

For Helmholtz, the function |u| doesn't satisfy a maximum principle in the usual sense. However, there are results about the maximum modulus.

Let me think about the specific case. Consider the simplest case: D is a ball of radius a. Then we can solve explicitly using spherical harmonics and spherical Bessel functions.

For a ball of radius a with Dirichlet data g, the exterior solution involves h_l^(1)(kr) (Hankel functions). The ratio |u(r)|/|u(a)| for the l-th mode involves |h_l^(1)(kr)|/|h_l^(1)(ka)|.

For the maximum to exceed the boundary value, we need |h_l^(1)(kr)| > |h_l^(1)(ka)| for some r > a.

The Hankel functions h_l^(1)(x) for real x have |h_l^(1)(x)| ~ 1/x for large x (decaying). But near the origin they grow. For x > 0, |h_l^(1)(x)| is generally decreasing for large x but may have local behavior.

Actually, for the l=0 case, h_0^(1)(x) = -e^(ix)/(ix) = i·e^(ix)/x, so |h_0^(1)(x)| = 1/x, which is strictly decreasing. So for l=0, the maximum is at the boundary.

For higher l, h_l^(1)(x) = (-i)^(l+1) e^(ix)/x · (sum of terms). The modulus... let me think. Actually |h_l^(1)(x)|^2 = j_l(x)^2 + y_l(x)^2 where j_l, y_l are spherical Bessel functions.

For the l-th mode, the ratio is |h_l^(1)(kr)|/|h_l^(1)(ka)| for r ≥ a. The question is whether this can exceed 1.

I recall that |h_l^(1)(x)|^2 = j_l(x)^2 + y_l(x)^2. And there's a known result that this is a decreasing function of x for x > 0... actually no, that's not quite right.

Hmm, let me think about this differently. There's a classical result by... I think the answer to this problem is C = 1.

Actually wait. Let me reconsider the problem. The problem is about the BEST constant C. If the maximum principle held with C=1, that would be the answer. But for Helmholtz, does it?

Let me think about the maximum principle for Helmholtz more carefully. The equation is Δu + k²u = 0. If we try to apply the maximum principle: at an interior maximum of |u|, we'd need certain conditions. But the equation Δu = -k²u means that at a point where u is positive and maximal, Δu ≤ 0, but -k²u < 0, so Δu = -k²u < 0, which is consistent with a maximum. So the maximum principle doesn't prevent interior maxima.

In fact, for the Helmholtz equation, interior maxima CAN exceed boundary values. This is well known.

So C > 1 in general. The question is what the best constant is.

Hmm, but the problem says "determine the best bound constant C". This is phrased as if there's a definite answer. Let me think about whether the answer depends on k and the geometry of D, or if it's a universal constant.

If C depends on k and D, then the problem would need to specify more. Since it asks for "the best bound constant C", maybe the answer is that C = 1, achieved in some limit, or maybe the answer involves some specific value.

Actually, I think I need to reconsider. Let me re-read the problem.

"Determine the best bound constant C such that sup_{R³/D} |u| ≤ C · sup_{∂D} |g|"

This is asking for the optimal C. The answer could be:
1. C = 1 (if maximum principle holds)
2. C = some specific value > 1
3. C depends on k and D (in which case the problem is asking for the general form)

Let me think about whether there's a universal bound. 

For the exterior Helmholtz problem, the solution is given by a combination of single and double layer potentials. The mapping from boundary data to the solution is a bounded linear operator.

Actually, I recall now. There's a result that for the Helmholtz equation, the maximum principle in the form sup|u| ≤ sup|g| does NOT hold in general. However, there are modified maximum principles.

Let me think about this from the representation formula. The exterior solution can be written as:
u(x) = ∫_{∂D} [∂G/∂n(y) · μ(y) - G(x,y) · σ(y)] dS(y)

where G is the free-space Green's function G(x,y) = e^{ik|x-y|}/(4π|x-y|).

For the Dirichlet problem, u is represented as a double layer potential (or combined single-double layer).

The key question is about the maximum modulus principle for Helmholtz.

I think the answer might be C = 1. Here's my reasoning: 

Actually, no. Let me think about a specific example. Consider D = ball of radius a, and g = Y_l^m (spherical harmonic). Then the exterior solution is:
u(r,θ,φ) = [h_l^(1)(kr) / h_l^(1)(ka)] · Y_l^m(θ,φ)

The sup of |u| over R³\D is:
sup_{r≥a} |h_l^(1)(kr)| / |h_l^(1)(ka)| · sup|Y_l^m|

And sup_{∂D} |g| = sup|Y_l^m|.

So the ratio is sup_{r≥a} |h_l^(1)(kr)| / |h_l^(1)(ka)|.

For this to give C, we need sup_{r≥a} |h_l^(1)(kr)| / |h_l^(1)(ka)| ≤ C for all l and all a, k.

Now, |h_l^(1)(x)| = |j_l(x) + i·y_l(x)| = sqrt(j_l(x)^2 + y_l(x)^2).

For l=0: h_0^(1)(x) = e^{ix}/(ix) (up to sign), |h_0^(1)(x)| = 1/x. So the ratio is a/r ≤ 1. Good, C ≥ 1 works for l=0.

For general l: We know that h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · P_l(1/x) where P_l is a polynomial. More precisely:
h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · Σ_{m=0}^{l} (i)^m (l+m)!/((l-m)! m! (2x)^m)

Hmm, this is getting complicated. Let me think about whether |h_l^(1)(x)| is monotonically decreasing for x > 0.

Actually, I recall that j_l(x)^2 + y_l(x)^2 is NOT monotonically decreasing in general. Let me check for l=1.

h_1^(1)(x) = -e^{ix}(x+i)/x² (let me verify). 

Actually, h_1^(1)(x) = -e^{ix}/x · (1 + i/x) = -e^{ix}(x+i)/x².

|h_1^(1)(x)|² = (x²+1)/x⁴ = 1/x² + 1/x⁴.

So |h_1^(1)(x)| = sqrt(1/x² + 1/x⁴) = (1/x²)sqrt(x²+1) = sqrt(x²+1)/x².

Is this decreasing for x > 0? Let f(x) = sqrt(x²+1)/x². 
f'(x) = [x/sqrt(x²+1) · x² - sqrt(x²+1) · 2x] / x⁴ = [x³/sqrt(x²+1) - 2x·sqrt(x²+1)] / x⁴
= x[x²/sqrt(x²+1) - 2sqrt(x²+1)] / x⁴
= [x² - 2(x²+1)] / (x³ · sqrt(x²+1))
= [x² - 2x² - 2] / (x³ · sqrt(x²+1))
= -(x² + 2) / (x³ · sqrt(x²+1))

This is negative for all x > 0. So |h_1^(1)(x)| is strictly decreasing for x > 0.

Interesting. So for l=1, the ratio is also ≤ 1.

Let me check l=2. h_2^(1)(x) = -ie^{ix}/x · (1 + 3i/x - 3/x²).

|h_2^(1)(x)|² = (1/x²) · |1 + 3i/x - 3/x²|² = (1/x²) · [(1 - 3/x²)² + 9/x²]
= (1/x²) · [1 - 6/x² + 9/x⁴ + 9/x²]
= (1/x²) · [1 + 3/x² + 9/x⁴]
= 1/x² + 3/x⁴ + 9/x⁶.

Let me check if this is decreasing. Let t = 1/x², so |h_2^(1)|² = t + 3t² + 9t³. As x increases, t decreases, and since the polynomial in t has positive coefficients, |h_2^(1)|² decreases. So |h_2^(1)(x)| is decreasing.

In general, |h_l^(1)(x)|² = (1/x²) · |P_l(1/x)|² where P_l is a polynomial with... and the modulus squared will be a polynomial in 1/x with positive coefficients (I believe), making it a decreasing function of x.

Actually, let me think about this more carefully. The general formula:
h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · Σ_{m=0}^{l} (i)^m (l+m)!/((l-m)!(2x)^m · m!)

Wait, let me use the standard formula. The spherical Hankel function:
h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · Σ_{m=0}^{l} (i/x)^m · (l+m)!/((l-m)!m!2^m)

Hmm, I'm not sure about the exact form. Let me use a different approach.

We know that h_l^(1)(x) = j_l(x) + i y_l(x), and there's a relation:
|h_l^(1)(x)|² = j_l(x)² + y_l(x)².

There's a known identity: j_l(x)² + y_l(x)² = Σ_{m=0}^{l} (2l-m)!/(m!(l-m)!(2x)^{2l-2m+1})... no, that doesn't look right either.

Actually, there's a classical result. Let me think about it using the relation to ordinary Bessel functions. h_l^(1)(x) = sqrt(π/(2x)) H_{l+1/2}^(1)(x).

And |H_ν^(1)(x)|² = J_ν(x)² + Y_ν(x)².

For half-integer order ν = l + 1/2, the Bessel functions have closed forms in terms of exponentials and polynomials.

There's a known result that for ν ≥ 1/2 (i.e., l ≥ 0), J_ν(x)² + Y_ν(x)² is a decreasing function of x for x > 0. This is related to the fact that the function is related to the modulus of a Hankel function.

Actually, I recall that there IS a theorem that |h_l^(1)(x)| is strictly decreasing for x > 0 and all l ≥ 0. This would mean that for the ball, the maximum of |u| is always attained on the boundary, giving C = 1 for the ball.

But does this extend to general domains? For general smooth bounded D, the solution is not simply a single mode. The question is whether the maximum principle sup|u| ≤ sup|g| holds for general exterior domains.

Hmm, for the Helmholtz equation, the standard maximum principle does NOT hold. The equation Δu + k²u = 0 is not amenable to the maximum principle because of the +k²u term (it's like an eigenvalue equation).

But wait - in the exterior domain with radiation condition, the solution decays at infinity. So the supremum is attained either on ∂D or at some interior point of R³\D.

At an interior maximum point x₀ of |u| (assuming u is real-valued for simplicity, or considering |u|²), if u(x₀) > 0 is a local max of u, then Δu(x₀) ≤ 0, but Δu = -k²u, so -k²u(x₀) ≤ 0, which means u(x₀) ≥ 0. This is consistent - it doesn't give a contradiction. So the maximum principle doesn't prevent interior maxima.

However, the question is whether for the EXTERIOR problem specifically, the maximum is always on the boundary. The ball example suggests it might be.

Let me think about this differently. Consider the function v = |u|². Then:
Δv = 2|∇u|² + 2ūΔu + 2uΔū = 2|∇u|² - 2k²|u|²

So Δv = 2|∇u|² - 2k²v.

At a maximum of v in the interior, Δv ≤ 0, so 2|∇u|² - 2k²v ≤ 0, which gives |∇u|² ≤ k²v. This doesn't prevent the maximum from being in the interior.

So in general, for the Helmholtz equation, interior maxima of |u| can exceed boundary values. The maximum principle with C=1 does NOT hold in general for interior problems.

But for EXTERIOR problems with radiation condition, the situation might be different because of the decay at infinity and the specific structure.

Hmm, but I showed that for the ball, |h_l^(1)(x)| is decreasing, so the maximum is on the boundary. Does this hold for all domains?

Actually, I think the answer is C = 1, and this is a known result. Let me think about why.

The key insight might be the following: for the exterior Helmholtz problem with radiation condition, the solution can be represented using the Green's function, and there's a positivity/maximum principle argument.

Actually, wait. I don't think C = 1 is correct in general. Let me think of a counterexample.

Consider a domain D that is very thin and elongated. The exterior solution could potentially have focusing effects that amplify the field beyond the boundary values.

Actually, let me reconsider. For the Helmholtz equation, there's a concept of "scattering resonances" and the solution can be large when k is near a resonance. But for the exterior Dirichlet problem with real k, the solution exists and is unique (no resonances for the exterior Dirichlet problem with real k, I think).

Hmm, actually, the exterior Dirichlet problem for real k > 0 always has a unique solution (this is a standard result). The question is about the bound.

Let me think about this problem from the perspective of the Rellich lemma and radiation conditions.

Actually, I think I should approach this more carefully. The problem is asking for the "best bound constant C". This is a well-posed mathematical question.

Let me consider the operator T: C(∂D) → C(R³\D) that maps boundary data g to the solution u. The norm of this operator is:
||T|| = sup_{g≠0} sup_{R³\D} |u| / sup_{∂D} |g|

The best constant C is ||T||.

For the Laplace equation (k=0), C = 1 by the maximum principle.

For Helmholtz (k > 0), the situation is different. Let me think about whether C = 1 or C > 1.

I think the answer is C = 1, based on the following reasoning:

For the exterior problem, we can use the Green's representation:
u(x) = ∫_{∂D} [G(x,y) ∂u/∂n(y) - ∂G/∂n_y(x,y) u(y)] dS(y)

where G(x,y) = e^{ik|x-y|}/(4π|x-y|) and n is the outward normal to D (inward to the exterior).

But this involves both u and ∂u/∂n, so it's not directly a bound in terms of g alone.

Alternatively, using layer potentials: u = D[μ] (double layer) or u = S[σ] + D[μ] (combined).

For the Dirichlet problem, we can write u = S[σ] where σ satisfies the integral equation (for the single-layer representation, which works for k not an interior eigenvalue):
g(x) = S[σ](x) for x ∈ ∂D (first kind), or
σ/2 + K'[σ] = ∂g/∂n (second kind, but this needs Neumann data).

Actually, the standard approach for the exterior Dirichlet problem is:
u(x) = S[σ](x) for x ∈ R³\D, where σ solves S[σ] = g on ∂D (if k² is not an interior Dirichlet eigenvalue),
or u(x) = D[μ](x) where μ solves (1/2 I + K)[μ] = g on ∂D (if k² is not an interior Neumann eigenvalue, or using combined layers).

This is getting complicated. Let me step back and think about what the "expected" answer is for this type of problem.

Given the way the problem is phrased ("determine the best bound constant C"), I think the answer is C = 1. This is the maximum principle for the exterior Helmholtz problem.

But I need to verify this. Let me think about whether the maximum principle holds for the exterior Helmholtz problem.

Claim: For the exterior Dirichlet problem with radiation condition, sup_{R³\D} |u| ≤ sup_{∂D} |g|.

Proof attempt: Consider w = |u|². We have Δw = 2|∇u|² - 2k²w. At an interior maximum of w, Δw ≤ 0, so |∇u|² ≤ k²w. This doesn't give a contradiction.

But we also have the radiation condition: u decays like 1/r at infinity. So w → 0 as r → ∞. Thus the supremum of w is attained either on ∂D or at an interior point.

If the supremum is attained at an interior point x₀, then w(x₀) = M (the max), and Δw(x₀) ≤ 0. But this is consistent with the equation. So we can't rule out interior maxima this way.

Hmm, so the naive maximum principle argument doesn't work. But maybe there's a more sophisticated argument.

Let me think about the Phragmén-Lindelöf type arguments or other methods.

Actually, I recall that for the Helmholtz equation, there's a result by... I think it's related to the work of Protter and Weinberger, or maybe Rellich.

Wait, I think the key is the following. For the Helmholtz equation in an exterior domain with the Sommerfeld radiation condition, there IS a maximum principle, but it requires a more careful argument.

One approach: Use the fact that the fundamental solution G(x,y) = e^{ik|x-y|}/(4π|x-y|) satisfies |G(x,y)| = 1/(4π|x-y|), which is the same as the Laplace fundamental solution. So |G| is harmonic in each variable (away from the singularity).

If u is represented as u(x) = ∫_{∂D} G(x,y) σ(y) dS(y) (single layer), then:
|u(x)| ≤ ∫_{∂D} |G(x,y)| |σ(y)| dS(y) = ∫_{∂D} (1/(4π|x-y|)) |σ(y)| dS(y)

The right-hand side is a single-layer potential for the LAPLACE equation with density |σ|. Let's call it v(x). Then v is harmonic in R³\D, v → 0 at infinity, and v ≥ |u| on ∂D (well, we need to be more careful).

Actually, this doesn't directly give us what we want because we need to relate σ to g.

Let me think differently. 

For the Laplace exterior problem, the maximum principle gives C = 1. For Helmholtz, the equation has the +k²u term which breaks the maximum principle.

But here's an important observation: the radiation condition forces the solution to be "outgoing", and this might restore a maximum principle.

Actually, I think the answer is NOT C = 1 in general. Let me think of a specific example.

Consider the 1D case (which is simpler). The Helmholtz equation u'' + k²u = 0 on (a, ∞) with u(a) = g and radiation condition u(x) = Ce^{ikx} for large x. The solution is u(x) = g · e^{ik(x-a)}, so |u(x)| = |g| for all x. So C = 1 in 1D.

In 3D, for a ball with l=0 mode: u(r) = g · (a/r) e^{ik(r-a)}, so |u(r)| = |g| · a/r ≤ |g|. C = 1.

For l=1: u(r) = g · h_1^(1)(kr)/h_1^(1)(ka). We showed |h_1^(1)(x)| is decreasing, so |u(r)| ≤ |g|. C = 1.

For general l and ball: same argument, C = 1.

So for balls, C = 1. What about general domains?

Let me think about whether there's a general argument. 

Consider the exterior problem. Let M = sup_{∂D} |g|. We want to show |u(x)| ≤ M for all x ∈ R³\D.

Consider the function φ(x) = M (constant). Then Δφ + k²φ = k²M ≠ 0, so φ is not a solution. We can't directly compare.

But consider w = u - φ or w = |u| - M. These don't satisfy nice equations.

Alternatively, consider the auxiliary function ψ(x) = M · a/|x| (for some appropriate a). This is harmonic and decays. But Δψ + k²ψ = k²ψ ≠ 0.

Hmm, the issue is that for Helmholtz, we can't use constant or harmonic comparison functions.

Let me try a different approach. Consider the "modified" maximum principle using an auxiliary function.

Let me try: w(x) = |u(x)|² - M² · (R/|x|)² for some R. Then we want to show w ≤ 0.

Actually, this is getting complicated. Let me think about whether the result C = 1 is actually true.

I found a potential issue. Consider a domain D that is the union of two balls far apart. The scattered wave from one ball can interfere with the other. Could this create constructive interference that exceeds the boundary values?

Actually, for the Dirichlet problem, if g is supported on one ball and zero on the other, the solution near the other ball is the scattered field, which could potentially be large due to focusing. But the boundary value on the second ball is zero, and the solution there is the scattered field from the first ball, which could be nonzero. So |u| on ∂D (second ball) could be nonzero even though g = 0 there. But wait, u = g on ∂D, so if g = 0 on the second ball, then u = 0 on the second ball. So the solution is zero on the second ball's boundary. The scattered field from the first ball must be exactly canceled by the field reradiated from the second ball. This is a complicated interaction.

The point is: can the solution in the exterior exceed M = sup|g|? 

Let me think about a concrete example. Take D = ball of radius a, g = 1 (constant). Then the solution is:
u(r) = (a/r) · e^{ik(r-a)} · (h_0^(1)(kr)/h_0^(1)(ka))... wait, for l=0:
u(r) = h_0^(1)(kr)/h_0^(1)(ka) = [e^{ikr}/(ikr)] / [e^{ika}/(ika)] = (a/r) e^{ik(r-a)}.
|u(r)| = a/r ≤ 1 = M. So C = 1 for this case.

Now take g = Y_l^m for some l > 0. Then |u(r,θ,φ)| = |h_l^(1)(kr)|/|h_l^(1)(ka)| · |Y_l^m(θ,φ)|. Since |h_l^(1)(x)| is decreasing, |u| ≤ |Y_l^m| = M on ∂D... wait, M = sup_{∂D} |g| = sup |Y_l^m|, and on the boundary r = a, |u| = |g| = |Y_l^m| ≤ M. In the exterior, |u(r)| ≤ |h_l^(1)(ka)|/|h_l^(1)(ka)| · M = M. So C = 1.

OK so for balls, C = 1 always. The question is whether this extends to general domains.

I believe the answer is C = 1, and this is a known result in scattering theory. The key result is sometimes called the "maximum principle for the Helmholtz equation in exterior domains."

Let me try to prove it. The idea is to use the Green's function representation and the fact that |G(x,y)| = 1/(4π|x-y|) (the Laplace Green's function).

For the exterior Dirichlet problem, the solution can be written as:
u(x) = -∫_{∂D} ∂G_D/∂n_y (x,y) g(y) dS(y)

where G_D is the Dirichlet Green's function for the exterior Helmholtz problem. But this is circular.

Alternatively, using the free-space Green's function:
u(x) = ∫_{∂D} [G_0(x,y) ∂u/∂n(y) - ∂G_0/∂n_y(x,y) g(y)] dS(y)

where G_0(x,y) = e^{ik|x-y|}/(4π|x-y|).

Taking absolute values:
|u(x)| ≤ ∫_{∂D} [|G_0(x,y)| |∂u/∂n(y)| + |∂G_0/∂n_y(x,y)| |g(y)|] dS(y)

This involves |∂u/∂n| which we don't control. So this direct approach doesn't work.

Let me try a different approach. 

Approach via the Rellich radiation condition and uniqueness:

Actually, let me think about this problem from a higher level. The problem is asking for the "best bound constant C". In many textbooks and references on scattering theory, the maximum principle for the Helmholtz equation in exterior domains is discussed.

I recall that there is indeed a maximum principle for the exterior Helmholtz problem, and it states that C = 1. The proof typically uses the following argument:

1. The solution u can be represented via layer potentials.
2. The key property is that the free-space Green's function satisfies |G(x,y)| = 1/(4π|x-y|), which is positive and equals the Laplace Green's function in modulus.
3. Using the representation and the maximum principle for harmonic functions, one can show |u| ≤ M.

But I'm not sure about the details. Let me try to construct a proof.

Proof attempt using the Green's function:

Let me use the fact that for the exterior Dirichlet problem, the solution can be written as:
u(x) = ∫_{∂D} K(x,y) g(y) dS(y)

where K(x,y) is the Dirichlet-to-solution kernel (Poisson kernel for the exterior Helmholtz problem).

If we can show that ∫_{∂D} |K(x,y)| dS(y) ≤ 1 for all x ∈ R³\D, then |u(x)| ≤ M · ∫|K| dS ≤ M, giving C = 1.

For the Laplace equation, the Poisson kernel is positive and integrates to 1, giving C = 1. For Helmholtz, the kernel is complex-valued and not necessarily positive, so ∫|K| could exceed 1.

Hmm, so this approach suggests C might be > 1 for Helmholtz.

Let me reconsider. Maybe C = 1 is not the answer.

Actually, let me think about this more carefully with a specific non-ball example.

Consider D = ball of radius a, but with non-trivial boundary data. We showed that for each spherical harmonic mode, the ratio is ≤ 1. But for general g (sum of modes), the solution is:
u(r,θ,φ) = Σ_{l,m} g_{lm} · h_l^(1)(kr)/h_l^(1)(ka) · Y_l^m(θ,φ)

Then |u(r,θ,φ)| ≤ Σ_{l,m} |g_{lm}| · |h_l^(1)(kr)|/|h_l^(1)(ka)| · |Y_l^m(θ,φ)|

Since |h_l^(1)(kr)|/|h_l^(1)(ka)| ≤ 1, we get:
|u(r,θ,φ)| ≤ Σ_{l,m} |g_{lm}| · |Y_l^m(θ,φ)|

But sup_{∂D} |g| = sup_{θ,φ} |Σ g_{lm} Y_l^m|, which is NOT the same as Σ |g_{lm}| |Y_l^m|. So we can't directly conclude |u| ≤ M from this.

However, for the ball, we can use a different argument. For each fixed r > a, the mapping g(θ,φ) → u(r,θ,φ) is a convolution (in the spherical harmonic sense) with kernel that has |coefficient| ≤ 1. But this doesn't directly give the sup norm bound.

Actually, for the ball, we can use the following: the solution at radius r is obtained from the boundary data at radius a by applying the operator T_r that multiplies each spherical harmonic mode by h_l^(1)(kr)/h_l^(1)(ka). The norm of T_r as an operator on C(S²) (with sup norm) is... well, it's not simply the max of the coefficients.

Hmm, this is getting complicated. Let me think about whether there's a simpler approach.

Actually, for the ball with g = 1 (constant, l=0 mode), we get |u(r)| = a/r ≤ 1. For g = Y_1^0 = cos θ, we get |u(r,θ)| = |h_1^(1)(kr)|/|h_1^(1)(ka)| · |cos θ| ≤ 1. For general g, the solution is a sum, and by the triangle inequality, |u| ≤ Σ |g_{lm}| · (ratio_l) · |Y_l^m| ≤ Σ |g_{lm}| · |Y_l^m|, but this doesn't bound by sup|g|.

So actually, for the ball, the question is whether the operator norm of T_r (from C(S²) to C(S²)) is ≤ 1 for all r > a. This is NOT obvious from the modal analysis.

Let me think about this differently. For the ball, we can use the Poisson integral representation. The exterior Helmholtz solution for the ball can be written as:

u(r,θ,φ) = ∫_{S²} P(r,θ,φ; θ',φ') g(θ',φ') dΩ'

where P is the Poisson kernel for the exterior Helmholtz problem for the ball.

For the Laplace equation, P_Laplace = (a²-r²... no, for exterior, P = (r²-a²)/... hmm, for the exterior Laplace problem, the Poisson kernel is P(r,ξ) = (r²-a²)/(4πa(r²-2ar ξ·η+a²)^{3/2})... I don't remember the exact form.

For Helmholtz, the Poisson kernel is different and complex-valued. The question is whether ∫|P| dΩ' ≤ 1.

This is getting quite involved. Let me step back and think about what the "expected" answer is.

Given that this is posed as a problem to "determine the best bound constant C", and given the structure of the problem (exterior Helmholtz with radiation condition), I believe the answer is:

C = 1

This is based on the maximum principle for the Helmholtz equation in exterior domains, which holds due to the radiation condition.

Let me try to give a proof. The key idea is:

Theorem (Maximum principle for exterior Helmholtz): If u satisfies Δu + k²u = 0 in R³\D with u = g on ∂D and the Sommerfeld radiation condition, then sup_{R³\D} |u| ≤ sup_{∂D} |g|.

Proof: Let M = sup_{∂D} |g|. We want to show |u(x)| ≤ M for all x ∈ R³\D.

Consider the auxiliary function v(x) = M · h_0^(1)(k|x-x₀|) / h_0^(1)(kR) for appropriate x₀ and R... no, this doesn't work because we need a global comparison function.

Let me try another approach. The key observation is:

For the exterior problem, we can use the Green's representation:
u(x) = ∫_{∂D} [∂G/∂n_y (x,y) g(y)] dS(y)  (using the Dirichlet Green's function, where the single layer term vanishes)

Wait, actually for the Dirichlet Green's function G_D(x,y) (which vanishes when x ∈ ∂D), we have:
u(x) = -∫_{∂D} ∂G_D/∂n_y (x,y) · g(y) dS(y)

This is the Poisson integral representation. The Dirichlet Green's function for the exterior Helmholtz problem satisfies:
- (Δ_y + k²) G_D(x,y) = δ(x-y) in R³\D
- G_D(x,y) = 0 for y ∈ ∂D
- Radiation condition in y

The Poisson kernel is P(x,y) = -∂G_D/∂n_y (x,y) for x ∈ R³\D, y ∈ ∂D.

For the Laplace equation, P(x,y) > 0 and ∫_{∂D} P(x,y) dS(y) = 1, giving C = 1.

For Helmholtz, G_D is complex, so P is complex, and ∫|P| dS could exceed 1.

So the question reduces to: is ∫_{∂D} |P(x,y)| dS(y) ≤ 1 for the Helmholtz Poisson kernel?

I don't think this is true in general. The Helmholtz Poisson kernel is complex-valued and can have cancellations, but |P| could integrate to more than 1.

Hmm, so maybe C > 1 after all.

Let me think about this problem from a completely different angle. Maybe the answer is not C = 1 but rather involves some other expression.

Actually, wait. Let me reconsider the problem statement. It says "Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|". 

This is asking for the optimal C. If C = 1 works, then it's the best possible (since we can achieve equality, e.g., with constant g on a ball). If C = 1 doesn't work, then we need to find the actual optimal C.

I think the answer is C = 1, and here's a potential proof strategy:

Proof using the Green's function and the maximum principle for harmonic functions:

The free-space Green's function is G(x,y) = e^{ik|x-y|}/(4π|x-y|). Note that |G(x,y)| = 1/(4π|x-y|) =: Φ(x,y), the Laplace fundamental solution.

The solution to the exterior Dirichlet problem can be represented as:
u(x) = ∫_{∂D} [G(x,y) ∂u/∂n(y) - ∂G/∂n_y(x,y) g(y)] dS(y)

Now, let's define:
ũ(x) = ∫_{∂D} [Φ(x,y) |∂u/∂n(y)| + |∂Φ/∂n_y(x,y)| |g(y)|] dS(y)

Then |u(x)| ≤ ũ(x). But ũ involves both |∂u/∂n| and |g|, so this doesn't directly help.

Let me try yet another approach. 

Approach using the Fourier transform / plane wave representation:

The outgoing solution can be represented as a superposition of plane waves:
u(x) = ∫_{S²} A(θ̂) e^{ik θ̂·x} dθ̂

for some amplitude function A. But this is for the whole space, not the exterior of a bounded domain.

Hmm, let me think about this more carefully.

Actually, I think I should consider the possibility that the answer is C = 1 and try to prove it using a clever auxiliary function.

Key idea: Use the auxiliary function w(x) = |u(x)|² and show that it satisfies a maximum principle in a modified sense.

We have Δw = 2|∇u|² - 2k²w. At a maximum of w in the interior, Δw ≤ 0, so |∇u|² ≤ k²w. This means the gradient is bounded but doesn't prevent the maximum.

But wait, we also have the radiation condition. The solution u satisfies the Sommerfeld radiation condition:
lim_{r→∞} r(∂u/∂r - iku) = 0

This means u ~ e^{ikr}/r for large r, so |u| ~ 1/r → 0. Thus w → 0 at infinity, and the maximum of w is attained either on ∂D or at an interior point.

If the maximum is at an interior point x₀, then w(x₀) = M² (where M = sup|u|), and Δw(x₀) ≤ 0. But this is consistent with the equation. So we can't rule out interior maxima by this argument alone.

However, there's a stronger result. Let me think about whether there's a Rellich-type identity or a unique continuation argument.

Actually, I think the correct approach is to use the following theorem:

Theorem: For the exterior Dirichlet problem of the Helmholtz equation with Sommerfeld radiation condition, the maximum principle holds: sup_{R³\D} |u| = sup_{∂D} |u|.

This is indeed a known result. The proof uses the following idea:

Consider the function v(x) = Re[u(x) e^{-iα}] for some angle α. Then v satisfies Δv + k²v = 0 and v = Re[g e^{-iα}] on ∂D. Also, v satisfies the radiation condition (in a suitable sense) and v → 0 at infinity.

Now, v is real-valued and satisfies Δv + k²v = 0. At a positive maximum of v in the interior, Δv ≤ 0 and v > 0, so Δv = -k²v < 0, which is consistent. So the maximum principle for v doesn't directly work either.

Hmm. Let me think about this differently.

Actually, I recall now that for the Helmholtz equation, the maximum principle does NOT hold in general, even for exterior domains. The constant C = 1 is not always achievable.

But the problem asks to "determine the best bound constant C". If C depends on the geometry and k, then the answer would be in terms of those. But the problem seems to ask for a universal constant.

Wait, re-reading the problem: "Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|". 

Maybe the answer is that C = 1, and this is the best possible. Or maybe the answer is that no finite C exists (but that can't be right since the solution operator is bounded).

Actually, the solution operator IS bounded for each fixed k and D (this follows from the well-posedness of the exterior Dirichlet problem). So C is finite. The question is what the best (smallest) C is.

If the problem is asking for a universal C that works for ALL D and ALL k, then... hmm, that's a different question. Let me re-read.

"Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|"

I think this is asking for the best C in terms of the given data (k, D). But since no specific k or D is given, maybe it's asking for a universal bound.

If it's a universal bound over all k > 0 and all smooth bounded D, then we need to find sup over all such problems of the operator norm.

For the ball, C = 1. For general domains, C might be larger. The question is whether C = 1 universally or if there's a larger universal bound.

I think the answer is C = 1, and this is a classical result. Let me try to find the right proof.

Actually, I just realized something. Let me think about the problem using the Fourier transform / spectral approach.

For the exterior problem, the solution can be written using the Green's function. The key property of the outgoing Green's function is:

G(x,y) = e^{ik|x-y|}/(4π|x-y|)

Note that |G(x,y)| = 1/(4π|x-y|) = Φ(x,y) (the Laplace Green's function).

Now, for the exterior Dirichlet problem, using the Green's representation formula:
u(x) = ∫_{∂D} [G(x,y) ∂_n u(y) - ∂_n G(x,y) u(y)] dS(y)

where ∂_n is the normal derivative pointing into the exterior (outward from D).

Now, here's the key idea. Define:
v(x) = ∫_{∂D} [Φ(x,y) |∂_n u(y)| + |∂_n Φ(x,y)| |u(y)|] dS(y)

where Φ = 1/(4π|x-y|) is the Laplace Green's function. Then |u(x)| ≤ v(x).

Now, v is a sum of single and double layer potentials for the LAPLACE equation with non-negative densities |∂_n u| and |u|. 

The single layer potential S[|∂_n u|](x) = ∫ Φ(x,y) |∂_n u(y)| dS(y) is harmonic in R³\D and continuous everywhere.

The double layer potential D[|u|](x) = ∫ ∂_n Φ(x,y) |u(y)| dS(y) is harmonic in R³\D.

Both are harmonic in the exterior and decay at infinity. By the maximum principle for harmonic functions:
sup_{R³\D} v = max(sup_{∂D} v^+, sup_{∂D} v^-)

where v^± are the boundary values from outside and inside.

But this gives a bound in terms of both |∂_n u| and |u| on the boundary, not just |u| = |g|.

So this approach doesn't directly give C = 1.

Let me try yet another approach. 

I think the key insight might be to use the following property of the Helmholtz Green's function:

For the exterior Dirichlet problem, the Poisson kernel P(x,y) = -∂G_D/∂n_y (x,y) where G_D is the Dirichlet Green's function. The claim would be that ∫_{∂D} |P(x,y)| dS(y) ≤ 1.

For the Laplace equation, this is true because P > 0 and ∫ P dS = 1. For Helmholtz, P is complex, so we need |∫ P g dS| ≤ M ∫|P| dS, and we need ∫|P| dS ≤ 1.

But I don't think ∫|P| dS ≤ 1 is true in general for Helmholtz. The complex nature of P means that |P| can be larger than |Re P|, and the integral of |P| can exceed 1.

OK, I'm going in circles. Let me try to think about this from the perspective of what's known in the literature.

I believe the relevant result is:

For the Helmholtz equation in an exterior domain with Sommerfeld radiation condition, the maximum principle sup|u| ≤ sup_{∂D}|g| DOES hold, and the best constant is C = 1.

The proof uses a clever argument involving the radiation condition. Here's the idea:

Proof: Let M = sup_{∂D} |g|. Suppose for contradiction that |u(x₀)| > M for some x₀ ∈ R³\D.

Consider the function w(x) = u(x) - M·e^{ik|x-x₀|}/(4π|x-x₀|) · C for some constant C... no, this doesn't work.

Let me try a different approach. The key is the following lemma:

Lemma: If u satisfies Δu + k²u = 0 in R³\D, the Sommerfeld radiation condition, and |u| ≤ M on ∂D, then |u| ≤ M in R³\D.

Proof of Lemma: 
Consider the auxiliary function φ(x) = M (constant). Then Δφ + k²φ = k²M ≠ 0, so φ is not a supersolution.

Instead, consider ψ(x) = M · Re[e^{ikr}/(ikr)] = M · cos(kr)/(kr) ... no, this doesn't work either because it depends on the choice of origin.

OK let me try the approach using the real and imaginary parts separately.

Let u = v + iw where v, w are real. Then Δv + k²v = 0 and Δw + k²w = 0, with v = Re g, w = Im g on ∂D.

For v: at a maximum of v in the interior, Δv ≤ 0 and v > 0, so -k²v ≤ 0, consistent. At a minimum, Δv ≥ 0 and v < 0, so -k²v ≥ 0, consistent. So no maximum principle for v alone.

But here's the key: v satisfies the radiation condition (Re part of the outgoing condition), and v → 0 at infinity. So v attains its max and min either on ∂D or in the interior.

Hmm, I'm stuck. Let me try to look at this from the energy perspective.

Energy approach: 
∫_{R³\D} (|∇u|² - k²|u|²) dx = ∫_{∂D} ū ∂_n u dS

This is the Rellich identity. It relates the L² norm of u to boundary integrals. But this gives an L² bound, not an L∞ bound.

OK, I think I need to just go with my best understanding. Let me consider two possibilities:

1. C = 1: The maximum principle holds for the exterior Helmholtz problem.
2. C > 1: The maximum principle doesn't hold, and the best constant is something else.

Given that:
- For balls, C = 1 (shown by the monotonicity of |h_l^(1)(x)|)
- The standard maximum principle argument doesn't directly work for Helmholtz
- The problem asks to "determine the best bound constant C"

I think the answer is C = 1, and the proof uses a more sophisticated argument than the standard maximum principle.

Let me try to construct a proof using the following idea:

The solution u to the exterior Dirichlet problem can be represented as:
u(x) = ∫_{∂D} P(x,y) g(y) dS(y)

where P(x,y) is the Poisson kernel. For the Laplace equation, P ≥ 0 and ∫P dS = 1. For Helmholtz, P is complex.

The key claim is that for the Helmholtz exterior problem, the Poisson kernel satisfies:
∫_{∂D} |P(x,y)| dS(y) ≤ 1

This would give |u(x)| ≤ M ∫|P| dS ≤ M.

But I'm not sure this is true. Let me think about whether there's a proof.

Actually, I think the correct statement might be different. Let me reconsider.

For the Helmholtz equation, the Poisson kernel for the exterior of a ball of radius a is:
P(r,θ,φ; θ',φ') = Σ_{l,m} [h_l^(1)(kr)/h_l^(1)(ka)] Y_l^m(θ,φ) Ȳ_l^m(θ',φ')

The integral ∫|P| dΩ' is hard to compute in general. But for the l=0 case (g = constant), P = (a/r) e^{ik(r-a)} and |P| = a/r, so ∫|P| dΩ' = (a/r) · 4π... wait, that's not right. Let me be more careful.

For g = 1 (constant on ∂D = sphere of radius a), the solution is u(r) = (a/r) e^{ik(r-a)}. The Poisson kernel for this case is P = (a/r) e^{ik(r-a)} / (4πa²) ... no, that's not right either.

Actually, the Poisson kernel P(x,y) for x in the exterior and y on the sphere satisfies:
u(x) = ∫_{S²} P(x,y) g(y) dS(y)

For g = 1, u(x) = (a/|x|) e^{ik(|x|-a)}, so ∫ P(x,y) dS(y) = (a/|x|) e^{ik(|x|-a)}.

For the Laplace case, P ≥ 0 and ∫ P dS = a/|x| ≤ 1. For Helmholtz, |∫ P dS| = a/|x| ≤ 1, but ∫ |P| dS could be different from |∫ P dS|.

So the question is: is ∫|P| dS = |∫ P dS| = a/r? This would require P to have constant phase, which is not the case in general (for non-constant g).

Hmm, I think for the ball, the Poisson kernel for Helmholtz is:
P(r,ξ; a,η) = Σ_l (2l+1)/(4π) · [h_l^(1)(kr)/h_l^(1)(ka)] · P_l(cos γ)

where γ is the angle between ξ and η, and P_l is the Legendre polynomial.

The modulus of this sum is hard to compute. The integral ∫|P| dΩ_η is generally NOT equal to |∫ P dΩ_η| = a/r.

So for the ball, ∫|P| dS could exceed 1, which means C > 1 for the ball when using general boundary data.

Wait, but I showed earlier that for each individual mode, the ratio is ≤ 1. The issue is with superposition of modes. Let me think about this more carefully.

For the ball, consider g(θ) = P_0(cos θ) + ε P_L(cos θ) for large L and small ε. The solution is:
u(r,θ) = [h_0^(1)(kr)/h_0^(1)(ka)] P_0(cos θ) + ε [h_L^(1)(kr)/h_L^(1)(ka)] P_L(cos θ)

At r = a: u = g, so |u| ≤ |g| ≤ 1 + ε (if we normalize). Actually, sup|g| = sup|1 + ε P_L| = 1 + ε (since P_L ranges in [-1,1]).

At r > a: |u(r,θ)| = |(a/r) e^{ik(r-a)} + ε [h_L^(1)(kr)/h_L^(1)(ka)] P_L(cos θ)|

The first term has modulus a/r. The second term has modulus ε · |h_L^(1)(kr)|/|h_L^(1)(ka)| ≤ ε. So:
|u(r,θ)| ≤ a/r + ε ≤ 1 + ε = sup|g|

So for this case, C = 1 still works! The triangle inequality gives us the bound because each mode's ratio is ≤ 1.

Wait, but this is using the triangle inequality on the modal expansion, which gives:
|u| ≤ Σ_l |g_l| · |ratio_l| · |P_l| ≤ Σ_l |g_l| · |P_l|

And we need this to be ≤ sup|g| = sup|Σ g_l P_l|.

But Σ |g_l| |P_l| is NOT bounded by sup|Σ g_l P_l| in general! The triangle inequality gives |u| ≤ Σ |g_l| |ratio_l| |P_l| ≤ Σ |g_l| |P_l|, but Σ |g_l| |P_l| can be much larger than sup|g|.

For example, take g = P_0 + P_1 = 1 + cos θ. Then sup|g| = 2 (at θ = 0). And Σ |g_l| |P_l| = 1 · 1 + 1 · |cos θ| = 1 + |cos θ| ≤ 2. So in this case it works.

But take g = P_0 - P_1 = 1 - cos θ. Then sup|g| = 2 (at θ = π). And Σ |g_l| |P_l| = 1 + |cos θ| ≤ 2. Still works.

Hmm, what about g = P_0 + P_2 = 1 + (3cos²θ-1)/2? sup|g| = sup|1 + (3cos²θ-1)/2| = sup|(1 + 3cos²θ)/2| = 2 (at θ = 0). And Σ|g_l||P_l| = 1 + |(3cos²θ-1)/2| ≤ 1 + 1 = 2. Still works.

Actually, the issue is that for orthogonal polynomials, Σ |g_l| |P_l| can exceed sup|g| when the signs are chosen adversarially. But in the examples above, it seems to work.

Let me try a more extreme example. Take g = Σ_{l=0}^{L} a_l P_l where the a_l are chosen so that g is small everywhere (sup|g| is small) but Σ|a_l| is large. This is possible because the P_l are bounded by 1 but not orthogonal in L∞.

For instance, take g_L(θ) = P_L(cos θ). Then sup|g| = 1, and the solution is u(r,θ) = [h_L^(1)(kr)/h_L^(1)(ka)] P_L(cos θ), with |u| ≤ |P_L| ≤ 1 = sup|g|. So C = 1 for this case.

Take g = P_0 + P_1 + ... + P_L. Then sup|g| = sup|Σ P_l|. At θ = 0, all P_l(1) = 1, so g(0) = L+1. Thus sup|g| = L+1. And the solution:
|u(r,θ)| ≤ Σ |h_l^(1)(kr)/h_l^(1)(ka)| |P_l(cos θ)| ≤ Σ |P_l(cos θ)|

At θ = 0: Σ |P_l(1)| = L+1 = sup|g|. So |u| ≤ sup|g|. C = 1.

But what if we choose g so that the P_l interfere destructively on ∂D but constructively in the exterior? Since the ratios h_l^(1)(kr)/h_l^(1)(ka) are different for different l (they have different phases), the destructive interference on ∂D might become constructive at some r > a.

This is the key question! Let me think about this.

At r = a, the ratios are all 1 (by construction), so u(a,θ) = g(θ). At r > a, the ratios are h_l^(1)(kr)/h_l^(1)(ka), which have different magnitudes and phases for different l. So the modal sum that was g(θ) at r = a becomes a different function at r > a.

Could this different function have a larger sup norm? In principle, yes, because the phase shifts could turn destructive interference into constructive interference.

But we showed that |h_l^(1)(kr)/h_l^(1)(ka)| ≤ 1 for all l and r > a. So each mode's amplitude decreases. The question is whether the phase shifts can cause constructive interference that overcomes the amplitude decrease.

Let me try a specific example. Take l = 0 and l = 1, with g(θ) = P_0 - P_1 = 1 - cos θ. Then sup|g| = 2 (at θ = π).

The solution is:
u(r,θ) = [h_0^(1)(kr)/h_0^(1)(ka)] - [h_1^(1)(kr)/h_1^(1)(ka)] cos θ

Let me compute this at a specific r. Let's take ka = 1, kr = 2 (so r = 2a).

h_0^(1)(x) = -e^{ix}/(ix) = ie^{ix}/x (up to sign convention). Let me use h_0^(1)(x) = e^{ix}/(ix). Then:
|h_0^(1)(x)| = 1/x.
h_0^(1)(1) = e^{i}/i = -ie^{i} = -i(cos1 + i sin1) = sin1 - i cos1.
h_0^(1)(2) = e^{2i}/(2i) = -ie^{2i}/2 = (sin2 - i cos2)/2.

Ratio_0 = h_0^(1)(2)/h_0^(1)(1) = (sin2 - i cos2)/(2(sin1 - i cos1)).

Let me compute numerically:
sin1 ≈ 0.8415, cos1 ≈ 0.5403
sin2 ≈ 0.9093, cos2 ≈ -0.4161

h_0^(1)(1) = 0.8415 - 0.5403i
h_0^(1)(2) = (0.9093 + 0.4161i)/2 = 0.4547 + 0.2080i

Ratio_0 = (0.4547 + 0.2080i)/(0.8415 - 0.5403i)

Let me compute: (0.4547 + 0.2080i)(0.8415 + 0.5403i) / |0.8415 - 0.5403i|²
= (0.4547·0.8415 + 0.2080·0.5403 + i(0.2080·0.8415 - 0.4547·0.5403)) / (0.8415² + 0.5403²)
= (0.3826 + 0.1124 + i(0.1750 - 0.2457)) / (0.7081 + 0.2919)
= (0.4950 - 0.0707i) / 1.0
= 0.4950 - 0.0707i

|Ratio_0| = sqrt(0.4950² + 0.0707²) = sqrt(0.2450 + 0.0050) = sqrt(0.2500) = 0.5 = a/r. ✓

Now for l = 1:
h_1^(1)(x) = -e^{ix}(x+i)/x² (using one convention). Let me use h_1^(1)(x) = -e^{ix}/x · (1 + i/x).

Actually, let me use the standard formula. h_1^(1)(x) = -e^{ix}(x+i)/x². Let me verify: for large x, h_1^(1)(x) ≈ -e^{ix}/x, which matches the asymptotic. OK.

h_1^(1)(1) = -e^{i}(1+i)/1 = -e^{i}(1+i) = -(cos1+isin1)(1+i) = -(cos1+isin1+icos1-sin1) = -(cos1-sin1) - i(sin1+cos1) = (sin1-cos1) - i(sin1+cos1)
= (0.8415-0.5403) - i(0.8415+0.5403) = 0.3012 - 1.3818i

|h_1^(1)(1)| = sqrt(0.3012² + 1.3818²) = sqrt(0.0907 + 1.9094) = sqrt(2.0001) ≈ √2. 

Actually, |h_1^(1)(x)|² = (x²+1)/x⁴, so |h_1^(1)(1)|² = 2/1 = 2. ✓

h_1^(1)(2) = -e^{2i}(2+i)/4 = -(cos2+isin2)(2+i)/4 = -(cos2·2-sin2·1 + i(cos2·1+sin2·2))/4
= -(2cos2-sin2 + i(cos2+2sin2))/4
= -(-0.8322-0.9093 + i(-0.4161+1.8186))/4
= -(-1.7415 + 1.4025i)/4
= (1.7415 - 1.4025i)/4
= 0.4354 - 0.3506i

|h_1^(1)(2)|² = (4+1)/16 = 5/16. |h_1^(1)(2)| = √(5)/4 ≈ 0.5590. ✓ (0.4354² + 0.3506² = 0.1896 + 0.1229 = 0.3125 = 5/16 ✓)

Ratio_1 = h_1^(1)(2)/h_1^(1)(1) = (0.4354 - 0.3506i)/(0.3012 - 1.3818i)

Let me compute: (0.4354 - 0.3506i)(0.3012 + 1.3818i) / |0.3012 - 1.3818i|²
Numerator: 0.4354·0.3012 + 0.3506·1.3818 + i(0.4354·1.3818 - 0.3506·0.3012)
= 0.1311 + 0.4844 + i(0.6016 - 0.1056)
= 0.6155 + 0.4960i

Denominator: 0.3012² + 1.3818² = 0.0907 + 1.9094 = 2.0001 ≈ 2

Ratio_1 = (0.6155 + 0.4960i)/2 = 0.3078 + 0.2480i

|Ratio_1| = sqrt(0.3078² + 0.2480²) = sqrt(0.0947 + 0.0615) = sqrt(0.1562) ≈ 0.3950

And |h_1^(1)(2)|/|h_1^(1)(1)| = √(5/16)/√2 = √(5/32) ≈ √0.15625 ≈ 0.3953. ✓

Now, the solution at r = 2a (with ka=1, kr=2):
u(2a, θ) = Ratio_0 · 1 - Ratio_1 · cos θ
= (0.4950 - 0.0707i) - (0.3078 + 0.2480i) cos θ

|u(2a, θ)|² = |0.4950 - 0.0707i - (0.3078 + 0.2480i)cos θ|²
= (0.4950 - 0.3078cos θ)² + (0.0707 + 0.2480cos θ)²

Let me find the maximum over θ. Let c = cos θ ∈ [-1, 1].
f(c) = (0.4950 - 0.3078c)² + (0.0707 + 0.2480c)²
= 0.2450 - 0.3047c + 0.0947c² + 0.0050 + 0.0351c + 0.0615c²
= 0.2500 - 0.2696c + 0.1562c²

f'(c) = -0.2696 + 0.3124c = 0 → c = 0.2696/0.3124 ≈ 0.863

f(0.863) = 0.2500 - 0.2696·0.863 + 0.1562·0.863² = 0.2500 - 0.2327 + 0.1164 = 0.1337

f(-1) = 0.2500 + 0.2696 + 0.1562 = 0.6758
f(1) = 0.2500 - 0.2696 + 0.1562 = 0.1366

So the maximum is at c = -1 (θ = π): f(-1) = 0.6758, |u| = √0.6758 ≈ 0.822.

Now, sup_{∂D} |g| = sup|1 - cos θ| = 2 (at θ = π).

So |u(2a, π)| ≈ 0.822 ≤ 2 = sup|g|. ✓ C = 1 works here.

But wait, this is a weak test because the solution is much smaller than the boundary data. Let me try a case where the boundary data has destructive interference.

Take g(θ) = P_0 + P_1 = 1 + cos θ. Then sup|g| = 2 (at θ = 0).

u(2a, θ) = Ratio_0 + Ratio_1 cos θ = (0.4950 - 0.0707i) + (0.3078 + 0.2480i) cos θ

|u|² = (0.4950 + 0.3078c)² + (-0.0707 + 0.2480c)²
= 0.2450 + 0.3047c + 0.0947c² + 0.0050 - 0.0351c + 0.0615c²
= 0.2500 + 0.2696c + 0.1562c²

f'(c) = 0.2696 + 0.3124c = 0 → c = -0.863

f(-0.863) = 0.2500 - 0.2327 + 0.1164 = 0.1337
f(-1) = 0.2500 - 0.2696 + 0.1562 = 0.1366
f(1) = 0.2500 + 0.2696 + 0.1562 = 0.6758

Max at c = 1 (θ = 0): |u| = √0.6758 ≈ 0.822 ≤ 2 = sup|g|. ✓

Again, C = 1 works, but the solution is much smaller than the boundary data. This is because the ratios are significantly less than 1 at r = 2a.

Let me try r very close to a, say r = a + ε for small ε. Then the ratios are close to 1, and the solution is close to g. So |u| ≈ |g| ≤ sup|g|. C = 1 works.

The question is whether at some intermediate r, the phase shifts can cause |u| to exceed sup|g|.

Let me try a case with more modes and specific phase relationships. Take g(θ) = P_0 - ε P_L for large L, where ε is chosen so that sup|g| is not much larger than 1.

sup|g| = sup|1 - ε P_L(cos θ)|. Since |P_L| ≤ 1, sup|g| ≤ 1 + ε. And at θ = 0, g = 1 - ε. At a zero of P_L, g = 1. At a maximum of P_L (θ = 0, P_L = 1), g = 1 - ε. At a minimum (P_L = -1), g = 1 + ε. So sup|g| = 1 + ε.

The solution: u(r,θ) = Ratio_0(r) - ε Ratio_L(r) P_L(cos θ).

|u|² = |Ratio_0|² - 2ε Re[Ratio_0 · conj(Ratio_L)] P_L + ε² |Ratio_L|² P_L²

The maximum of |u|² over θ is at most:
|Ratio_0|² + 2ε |Ratio_0| |Ratio_L| |P_L| + ε² |Ratio_L|² P_L²
≤ |Ratio_0|² + 2ε |Ratio_0| |Ratio_L| + ε² |Ratio_L|²
= (|Ratio_0| + ε |Ratio_L|)²

So |u| ≤ |Ratio_0| + ε |Ratio_L| ≤ 1 + ε = sup|g|.

This uses the triangle inequality and the fact that |Ratio_l| ≤ 1. So for any two-mode case, C = 1 works!

In fact, this generalizes. For g = Σ a_l P_l:
|u(r,θ)| = |Σ a_l Ratio_l(r) P_l(cos θ)| ≤ Σ |a_l| |Ratio_l(r)| |P_l(cos θ)| ≤ Σ |a_l| |P_l(cos θ)|

But we need Σ |a_l| |P_l(cos θ)| ≤ sup_θ |Σ a_l P_l(cos θ)| = sup|g|.

This is NOT true in general! Σ |a_l| |P_l(cos θ)| can exceed sup|Σ a_l P_l(cos θ)|.

For example, take g = P_0 + P_1 - P_2 (with appropriate normalization). Then sup|g| might be smaller than Σ|a_l| sup|P_l| = 1 + 1 + 1 = 3.

But wait, the bound |u| ≤ Σ |a_l| |P_l| is a very crude bound. The actual |u| could be much smaller due to the complex phases of the ratios.

Hmm, but the question is whether there EXISTS some g and some r > a such that |u(r)| > sup|g|. The crude bound doesn't rule this out, but it also doesn't prove it.

Let me think about this more carefully. The key question is:

For the ball, is the operator T_r: C(S²) → C(S²) defined by (T_r g)(θ) = Σ a_l Ratio_l(r) P_l(cos θ) bounded by 1 in the sup norm?

The operator norm of T_r is sup_{||g||_∞=1} ||T_r g||_∞. 

For the Laplace case, Ratio_l(r) = (a/r)^{l+1} (all real and positive), and the operator is a contraction (||T_r|| ≤ 1) by the maximum principle for harmonic functions.

For Helmholtz, Ratio_l(r) = h_l^(1)(kr)/h_l^(1)(ka) (complex). The operator T_r is NOT a positive operator, so the maximum principle doesn't directly apply.

However, I showed that |Ratio_l(r)| ≤ 1 for all l and r > a. This means T_r is a contraction in the L² sense (by Parseval), but not necessarily in L∞.

The operator norm in L∞ could be larger than 1. Let me think about whether it can be.

Consider the extreme case where all Ratio_l have the same phase. Then T_r acts like a real positive operator, and ||T_r|| ≤ 1 (by the same argument as Laplace, since |Ratio_l| ≤ 1 and the Poisson kernel for Laplace has ||T|| = 1).

But the Ratio_l have DIFFERENT phases for different l. This means T_r is not a positive operator, and the L∞ norm could be larger.

Wait, but I showed in the two-mode examples that |u| ≤ sup|g| even with different phases. Let me think about why.

In the two-mode case g = a_0 P_0 + a_1 P_1:
|u|² = |a_0 R_0 + a_1 R_1 cos θ|² = |a_0|²|R_0|² + 2 Re[a_0 ā_1 R_0 R̄_1] cos θ + |a_1|²|R_1|² cos²θ

The maximum over θ ∈ [-1,1] of this quadratic in c = cos θ is:
At c = ±1: |a_0 R_0 ± a_1 R_1|² ≤ (|a_0||R_0| + |a_1||R_1|)² ≤ (|a_0| + |a_1|)²

And sup|g| = sup|a_0 + a_1 cos θ| = |a_0| + |a_1| (at θ = 0 or π).

So |u| ≤ |a_0| + |a_1| = sup|g|. ✓

This works because for two modes, sup|g| = |a_0| + |a_1| (the L∞ norm of a linear function on [-1,1] is attained at the endpoints).

For three or more modes, sup|g| < Σ|a_l| in general, and the argument breaks down.

Let me try three modes. Take g(θ) = P_0 + P_1 + P_2 = 1 + cos θ + (3cos²θ-1)/2 = (1 + 2cos θ + 3cos²θ)/2.

sup|g|: Let c = cos θ. g = (1 + 2c + 3c²)/2. g' = (2 + 6c)/2 = 1 + 3c = 0 → c = -1/3.
g(-1/3) = (1 - 2/3 + 1/3)/2 = (2/3)/2 = 1/3.
g(1) = (1+2+3)/2 = 3. g(-1) = (1-2+3)/2 = 1.
So sup|g| = 3 (at θ = 0).

Now, Σ|a_l| = 1 + 1 + 1 = 3 = sup|g|. So the crude bound gives |u| ≤ 3 = sup|g|. Still works!

Hmm, it seems like for the Legendre polynomial basis, sup|Σ a_l P_l| = Σ|a_l| when all a_l have the same sign (because P_l(1) = 1 for all l, so g(0) = Σ a_l).

What if the a_l have different signs? Take g = P_0 - P_1 + P_2 = 1 - cos θ + (3cos²θ-1)/2 = (1 - 2cos θ + 3cos²θ)/2.

sup|g|: g(c) = (1 - 2c + 3c²)/2. g' = (-2+6c)/2 = -1+3c = 0 → c = 1/3.
g(1/3) = (1 - 2/3 + 1/3)/2 = (2/3)/2 = 1/3.
g(1) = (1-2+3)/2 = 1. g(-1) = (1+2+3)/2 = 3.
sup|g| = 3 (at θ = π).

Again, Σ|a_l| = 3 = sup|g|. 

This is because P_l(-1) = (-1)^l, so g(π) = Σ a_l (-1)^l. If a_l = (-1)^l, then g(π) = Σ 1 = L+1 = Σ|a_l|.

So for the specific choice a_l = ±1, we always have sup|g| = Σ|a_l|, and the crude bound gives C = 1.

But what about more general coefficients? Take g = P_0 + 2P_1 - P_2 = 1 + 2cos θ - (3cos²θ-1)/2 = (3 - 4cos θ - 3cos²θ)/2... let me recompute.

g(c) = 1 + 2c - (3c²-1)/2 = (2 + 4c - 3c² + 1)/2 = (3 + 4c - 3c²)/2.

g'(c) = (4 - 6c)/2 = 2 - 3c = 0 → c = 2/3.
g(2/3) = (3 + 8/3 - 4/3)/2 = (3 + 4/3)/2 = (13/3)/2 = 13/6 ≈ 2.17.
g(1) = (3+4-3)/2 = 2. g(-1) = (3-4-3)/2 = -2.
sup|g| = 13/6 ≈ 2.17.

Σ|a_l| = 1 + 2 + 1 = 4.

So Σ|a_l| = 4 > 13/6 ≈ 2.17 = sup|g|. The crude bound gives |u| ≤ 4, but sup|g| ≈ 2.17. So the crude bound is NOT sufficient to show C = 1.

But this doesn't mean C > 1; it just means the crude bound is too crude. The actual |u| might still be ≤ sup|g| due to the complex phases of the ratios.

Let me compute the actual solution for this case. Take ka = 1, kr = 1.1 (r close to a, so ratios close to 1).

For r close to a, Ratio_l ≈ 1 + (r-a) · (d/dr)[h_l^(1)(kr)/h_l^(1)(ka)]|_{r=a} = 1 + (r-a) · k · h_l'^(1)(ka)/h_l^(1)(ka).

The derivatives h_l'^(1)(x) = dh_l^(1)/dx. Using the recurrence h_l'^(1)(x) = l/x · h_l^(1)(x) - h_{l+1}^(1)(x).

For l=0: h_0'^(1)(x) = -h_1^(1)(x). So Ratio_0' = k · (-h_1^(1)(ka))/h_0^(1)(ka).
For l=1: h_1'^(1)(x) = (1/x) h_1^(1)(x) - h_2^(1)(x). So Ratio_1' = k · [(1/(ka)) h_1^(1)(ka) - h_2^(1)(ka)] / h_1^(1)(ka) = k/(ka) - k h_2^(1)(ka)/h_1^(1)(ka) = 1/a - k h_2^(1)(ka)/h_1^(1)(ka).

This is getting very complicated. Let me try a different approach.

Instead of computing specific examples, let me think about the general theory.

I think the answer is C = 1, and the proof is based on the following key theorem:

Theorem (Maximum principle for exterior Helmholtz): Let u solve the exterior Dirichlet problem for the Helmholtz equation with Sommerfeld radiation condition. Then:
sup_{R³\D} |u| ≤ sup_{∂D} |u|

Proof: The proof uses the following idea. Consider the function:
v(x) = u(x) / φ(x)
where φ is a suitable positive function satisfying (Δ + k²)φ ≤ 0 in R³\D and φ > 0, with φ → ∞ or φ → 0 at infinity in a way that helps.

Actually, the standard approach for proving maximum principles for equations with lower-order terms is to use an auxiliary function. For the equation Δu + k²u = 0, we can write it as Δu = -k²u. 

If we consider w = |u|², then Δw = 2|∇u|² - 2k²w ≥ -2k²w. So Δw + 2k²w ≥ 0, meaning w is a supersolution of Δw + 2k²w = 0.

Hmm, this doesn't directly help.

Let me try the approach using the function e^{-αr} where r = |x|.

Consider w(x) = |u(x)|² · e^{α|x|} for some α > 0. Then:
∇w = e^{αr}(2 Re(ū ∇u) + α |u|² x̂)
Δw = e^{αr}(2|∇u|² + 2 Re(ū Δu) + 4α Re(ū ∇u · x̂) + α |u|² + α² |u|² r... 

This is getting messy. Let me try a different auxiliary function.

Actually, let me try the approach from the book "Inverse Acoustic and Electromagnetic Scattering" by Colton and Kress, or similar references.

I recall that in scattering theory, the following result is known:

For the exterior Dirichlet problem, the solution operator is bounded from C(∂D) to C(R³\D), and the bound depends on k and the geometry. The maximum principle with C = 1 does NOT hold in general for the Helmholtz equation.

Wait, but I showed that for the ball, C = 1 (at least for the cases I checked). And the crude bound using |Ratio_l| ≤ 1 gives C = 1 for the ball when the coefficients are all ±1. But for general coefficients, the crude bound doesn't give C = 1.

Hmm, let me think about this differently. Maybe the answer is NOT C = 1, and the problem is asking for a different kind of bound.

Actually, re-reading the problem: "Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|". 

Maybe the answer is that C = 1 is the best constant, and this is a theorem that needs to be proved. Or maybe the answer is something else entirely.

Let me think about what happens for general domains. For a non-convex domain, the scattered field could potentially focus and create regions where |u| > sup|g|. This is related to the concept of "scattering focusing" or "near-field enhancement".

Actually, I think for the Helmholtz equation, the maximum principle with C = 1 does NOT hold in general, and the best constant depends on the domain and k. But the problem asks to "determine" C, suggesting there's a specific answer.

Let me reconsider the problem. Maybe the answer is C = 1, and the proof is non-trivial but known. Or maybe the answer is that C = 1 is the best constant, achieved in the limit as k → 0 or for specific geometries.

Actually, I just thought of something. For the Helmholtz equation, there's a result known as the "maximum principle for the real part" or something similar. Let me think...

For a real-valued solution v of Δv + k²v = 0, if v has a positive local maximum at x₀, then Δv(x₀) ≤ 0 and v(x₀) > 0, so -k²v(x₀) ≤ 0, which is consistent. So no maximum principle.

But for the EXTERIOR problem with radiation condition, the solution decays at infinity. So if v is real and positive somewhere in the exterior, it must attain its maximum either on ∂D or at an interior point. If at an interior point, the above analysis shows it's consistent. So the maximum principle doesn't hold even for the exterior problem.

This means C > 1 is possible. The question is: what is the best C?

I think the problem might be asking for C = 1 as the answer, with the understanding that this is the best possible constant (achieved for the Laplace limit or for balls). But I'm not confident.

Let me try another approach. Maybe the answer is related to the following:

For the Helmholtz equation, the solution can be written as u = u_s + u_i where u_i is the incident wave and u_s is the scattered wave. But for the Dirichlet problem with boundary data g, there's no incident wave; the solution is purely determined by g.

Hmm, let me reconsider the problem from scratch. 

The problem is: Δu + k²u = 0 in R³\D, u = g on ∂D, Sommerfeld radiation condition. Find the best C such that sup_{R³\D} |u| ≤ C sup_{∂D} |g|.

I think the answer is C = 1, and here's a proof sketch:

Proof: 
Step 1: The solution u can be represented using the Green's function for the exterior Dirichlet problem:
u(x) = ∫_{∂D} P(x,y) g(y) dS(y)
where P(x,y) = -∂G_D/∂n_y (x,y) is the Poisson kernel.

Step 2: For the Laplace equation, P_Laplace ≥ 0 and ∫ P_Laplace dS = 1, giving C = 1.

Step 3: For Helmholtz, G_D(x,y) = G_0(x,y) - ∫_{∂D} G_0(x,z) μ(y,z) dS(z) (method of images / double layer correction), where G_0 is the free-space Green's function and μ is the density that makes G_D vanish on ∂D.

Step 4: The key property is that |G_0(x,y)| = Φ(x,y) (Laplace Green's function). Using this, one can show that the Poisson kernel for Helmholtz satisfies ∫|P| dS ≤ 1.

But I'm not sure about Step 4. Let me think about whether it's true.

Actually, I don't think Step 4 is true in general. The Helmholtz Poisson kernel is complex, and its modulus can integrate to more than 1.

OK, I think I need to take a different approach entirely. Let me consider the possibility that the answer is C = 1 and try to prove it using a different method.

Method: Use the Fourier transform / plane wave representation and the properties of the radiation condition.

The outgoing solution can be represented as:
u(x) = ∫_{S²} A(θ̂) e^{ik θ̂·x} dθ̂

where A is the far-field amplitude (this is the Herglotz representation for radiating solutions). Wait, this is for solutions in all of R³, not just the exterior.

Actually, for the exterior problem, the solution has the asymptotic behavior:
u(x) ~ e^{ikr}/r · f(θ̂) as r → ∞

where f is the far-field pattern. The solution is determined by the boundary data g.

Hmm, this doesn't directly help with the maximum principle.

Let me try yet another approach. 

Method: Use the fact that the solution to the exterior Helmholtz problem can be obtained as the limit of solutions to the exterior Laplace problem with a complexified wave number.

Consider the family of problems: Δu_σ + (k + iσ)² u_σ = 0 in R³\D, u_σ = g on ∂D, radiation condition. As σ → 0, u_σ → u.

For σ > 0, the equation is Δu_σ + (k² - σ² + 2ikσ) u_σ = 0, which is the Yukawa/Helmholtz equation with complex wave number. The term 2ikσ provides damping.

For the damped case, the maximum principle might hold because the damping term causes |u_σ| to decrease. Specifically, for the equation Δu + (k² - σ² + 2ikσ)u = 0, the imaginary part of the wave number provides absorption, which should give a maximum principle.

Let me check: for the equation Δu + λu = 0 with Im(λ) > 0 (absorptive), does the maximum principle hold?

Consider w = |u|². Δw = 2|∇u|² + 2 Re(ū Δu) = 2|∇u|² - 2 Re(λ) |u|².

If Re(λ) < 0 (i.e., λ = -|λ| with |Re(λ)| > 0), then Δw = 2|∇u|² + 2|Re(λ)| w ≥ 0. This means w is subharmonic, so its maximum is on the boundary. This gives the maximum principle!

For our case, λ = k² - σ² + 2ikσ. Re(λ) = k² - σ². For σ > k, Re(λ) < 0, and the maximum principle holds. For σ < k, Re(λ) > 0, and the maximum principle doesn't hold from this argument.

So for σ > k, we get sup|u_σ| ≤ sup|g|, i.e., C = 1. But we need this for σ = 0 (the original problem), where Re(λ) = k² > 0.

Hmm, so this approach works for the strongly damped case but not for the original Helmholtz equation.

Let me try a different auxiliary function. Instead of w = |u|², consider w = |u|² · φ for some positive function φ.

Δ(w) = Δ(|u|² φ) = φ Δ|u|² + 2 ∇|u|² · ∇φ + |u|² Δφ
= φ(2|∇u|² - 2k²|u|²) + 2 ∇|u|² · ∇φ + |u|² Δφ
= 2φ|∇u|² + 2∇|u|² · ∇φ + |u|²(Δφ - 2k²φ)

If we choose φ such that Δφ - 2k²φ ≥ 0 (i.e., φ is a subsolution of Δφ = 2k²φ), then:
Δw ≥ 2φ|∇u|² + 2∇|u|² · ∇φ ≥ ... 

This doesn't directly give subharmonicity because of the cross term.

Let me try φ = e^{α|x|}. Then:
∇φ = α x̂ e^{αr}
Δφ = (α² + 2α/r) e^{αr} (in 3D, Δ e^{αr} = (α² + 2α/r) e^{αr})

Δφ - 2k²φ = (α² + 2α/r - 2k²) e^{αr}

For this to be ≥ 0, we need α² + 2α/r ≥ 2k² for all r > R₀ (some large radius). For large r, this requires α² ≥ 2k², i.e., α ≥ k√2.

But then φ = e^{αr} → ∞ as r → ∞, which means w = |u|² e^{αr} → ∞ (since |u|² ~ 1/r² and e^{αr} → ∞). So w doesn't attain its maximum on ∂D; it goes to infinity. This doesn't help.

Let me try φ = e^{-αr} instead. Then:
Δφ = (α² - 2α/r) e^{-αr}
Δφ - 2k²φ = (α² - 2α/r - 2k²) e^{-αr}

For large r, this is (α² - 2k²) e^{-αr}. For this to be ≥ 0, we need α ≥ k√2.

With φ = e^{-αr} and α ≥ k√2, w = |u|² e^{-αr} → 0 as r → ∞ (since |u|² ~ 1/r² and e^{-αr} → 0). So w attains its maximum either on ∂D or at an interior point.

If w attains its maximum at an interior point x₀, then Δw(x₀) ≤ 0. But:
Δw = 2φ|∇u|² + 2∇|u|² · ∇φ + |u|²(Δφ - 2k²φ)

At the maximum, ∇w = 0, which means:
2 Re(ū ∇u) φ + |u|² ∇φ = 0
So Re(ū ∇u) = -|u|² ∇φ/(2φ) = -|u|² α x̂/2

And Δw(x₀) = 2φ|∇u|² + 2∇|u|² · ∇φ + |u|²(Δφ - 2k²φ) ≤ 0

∇|u|² = 2 Re(ū ∇u), so:
2∇|u|² · ∇φ = 4 Re(ū ∇u) · ∇φ = 4(-|u|² α x̂/2) · (α x̂ φ) = -2α² |u|² φ

So: Δw(x₀) = 2φ|∇u|² - 2α²|u|²φ + |u|²(Δφ - 2k²φ) ≤ 0
= 2φ|∇u|² + |u|²(Δφ - 2k²φ - 2α²φ) ≤ 0

Now, Δφ - 2k²φ - 2α²φ = (α² - 2α/r - 2k² - 2α²) e^{-αr} = (-α² - 2α/r - 2k²) e^{-αr} < 0.

So: Δw(x₀) = 2φ|∇u|² - |u|²(α² + 2α/r + 2k²)φ ≤ 0

This gives: 2|∇u|² ≤ |u|²(α² + 2α/r + 2k²)

This is consistent (no contradiction), so the maximum of w could be in the interior. This means w could have an interior maximum, and we can't conclude w ≤ w|_{∂D}.

Hmm, so this approach also doesn't work. The issue is that the Helmholtz equation genuinely doesn't satisfy a maximum principle in the usual sense.

Let me try a completely different approach. Maybe the answer is NOT C = 1.

Actually, let me reconsider. I've been assuming the answer should be a clean constant, but maybe the answer involves the geometry. Let me re-read the problem.

"Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|"

The problem says "the best bound constant C". This suggests there's a specific value. Given the way the problem is set up (general D, general k, general g), the answer should be a universal constant.

I think the answer is C = 1. Here's my best argument:

The key is the following theorem, which I believe is correct:

Theorem: For the exterior Dirichlet problem of the Helmholtz equation with Sommerfeld radiation condition, the maximum principle holds: sup_{R³\D} |u| ≤ sup_{∂D} |g|.

The proof uses the Rellich radiation condition and a unique continuation argument. Here's the idea:

1. Let M = sup_{∂D} |g|. Assume for contradiction that |u(x₀)| > M for some x₀ ∈ R³\D.

2. Consider the function v(x) = u(x) - M·ψ(x) where ψ is a suitable comparison function. We need ψ to satisfy (Δ + k²)ψ = 0, ψ = 1 on ∂D, and the radiation condition.

3. If such ψ exists with |ψ(x)| ≤ 1 for all x ∈ R³\D, then |v| ≤ |u| + M|ψ| and... no, this doesn't work directly.

Actually, let me think about this using the Poisson kernel approach more carefully.

For the ball of radius a, the Poisson kernel for the exterior Helmholtz problem is:
P(r,ξ;η) = Σ_{l=0}^∞ (2l+1)/(4π) · [h_l^(1)(kr)/h_l^(1)(ka)] · P_l(ξ·η)

The solution is u(r,ξ) = ∫_{S²} P(r,ξ;η) g(aη) dΩ(η).

Now, ∫_{S²} P(r,ξ;η) dΩ(η) = [h_0^(1)(kr)/h_0^(1)(ka)] = (a/r) e^{ik(r-a)} (using the addition theorem and the fact that ∫ P_l dΩ = 4π δ_{l0}).

So |∫ P dΩ| = a/r ≤ 1. But ∫|P| dΩ could be larger.

The question is: is ∫|P(r,ξ;η)| dΩ(η) ≤ 1 for all r > a and all ξ?

For the Laplace case, P ≥ 0 and ∫ P dΩ = a/r ≤ 1, so ∫|P| = ∫P ≤ 1. ✓

For Helmholtz, P is complex. Let me compute ∫|P|² dΩ first (using Parseval):
∫|P|² dΩ = Σ_{l} (2l+1)/(4π)² · |h_l^(1)(kr)/h_l^(1)(ka)|² · 4π/(2l+1) ... 

Actually, by the addition theorem, P(r,ξ;η) = Σ_l (2l+1)/(4π) R_l P_l(ξ·η) where R_l = h_l^(1)(kr)/h_l^(1)(ka). 

∫|P|² dΩ_η = Σ_l (2l+1)/(4π)² |R_l|² ∫ P_l(ξ·η)² dΩ_η = Σ_l (2l+1)/(4π)² |R_l|² · 4π/(2l+1) = Σ_l |R_l|²/(4π).

Since |R_l| ≤ 1, we have ∫|P|² dΩ ≤ Σ_l 1/(4π) = ∞. So the L² norm is infinite (the series doesn't converge). This means P is not in L², which makes sense because it's a distribution (Poisson kernel).

OK, this approach is not working well. Let me try to think about the problem from a higher level.

I think the answer is C = 1, and the proof is based on the following key insight:

For the exterior Helmholtz problem with radiation condition, the solution u satisfies a maximum principle because the radiation condition selects the "outgoing" solution, which is the one that decays at infinity. The decay at infinity, combined with the equation, forces the maximum to be on the boundary.

The formal proof might go as follows:

1. The solution u is analytic in R³\D and continuous on R³\D̄ (closure).
2. |u| → 0 as |x| → ∞ (by the radiation condition).
3. Therefore, |u| attains its maximum on the compact set R³\D̄ ∪ {∞}... well, on ∂D ∪ (R³\D).

Wait, since |u| → 0 at infinity and |u| is continuous, the supremum is attained either on ∂D or at some point in R³\D. If it's attained on ∂D, we're done. If it's attained at an interior point, we need to show it can't exceed the boundary value.

For the Laplace equation, the maximum principle prevents interior maxima. For Helmholtz, it doesn't. So the question is whether the radiation condition provides an additional constraint that prevents interior maxima from exceeding boundary values.

I think the answer is YES, and the proof uses the following argument:

Consider the Fourier transform of u (in the distributional sense). The radiation condition implies that the Fourier transform of u is supported on the sphere |ξ| = k (the Ewald sphere). This means u is a superposition of plane waves e^{ik θ̂·x} with |θ̂| = 1:

u(x) = ∫_{S²} A(θ̂) e^{ik θ̂·x} dθ̂

Wait, this is the Herglotz representation, but it's for solutions in all of R³, not just the exterior. For the exterior problem, the solution is not entire; it has a singularity (or at least non-analyticity) inside D.

Hmm, but the solution IS analytic in the exterior R³\D. The Herglotz representation applies to entire solutions. For exterior solutions, we need a different representation.

Actually, the solution to the exterior problem can be written as:
u(x) = ∫_{∂D} [G(x,y) σ(y) - ∂G/∂n_y(x,y) μ(y)] dS(y)

using single and double layer potentials. This is not a superposition of plane waves.

OK, I think I've spent too long on this. Let me just go with C = 1 and provide a proof based on the key ideas.

Actually, wait. Let me reconsider the problem. Maybe the answer is NOT C = 1, and the problem is asking for a different kind of bound.

Let me think about what happens for the interior problem. For the interior Helmholtz problem (Δu + k²u = 0 in D, u = g on ∂D), the maximum principle does NOT hold, and in fact, the solution can be arbitrarily large when k² is close to an interior Dirichlet eigenvalue. So for the interior problem, no finite C exists (uniformly over k).

For the exterior problem, there are no eigenvalues (the exterior Dirichlet problem is always uniquely solvable for real k > 0), so C is finite for each k and D. But C could depend on k and D.

If the problem is asking for a universal C (over all k > 0 and all smooth bounded D), then... for the ball, C = 1 (as I showed). For general D, C might be larger. But is there a universal bound?

I think the answer is C = 1, and this is a known result. Let me try to find the right proof.

Actually, I just thought of a potential proof using the Green's function and the maximum principle for harmonic functions.

Proof:
Let u solve the exterior Helmholtz Dirichlet problem. Let M = sup_{∂D} |g|.

The free-space Green's function is G(x,y) = e^{ik|x-y|}/(4π|x-y|), with |G(x,y)| = Φ(x,y) := 1/(4π|x-y|).

The solution can be represented as (using the Green's representation formula for the exterior):
u(x) = ∫_{∂D} [G(x,y) ∂_n u(y) - ∂_n G(x,y) g(y)] dS(y)   ... (*)

where ∂_n is the outward normal to D (inward to the exterior region).

Now, define:
v(x) = ∫_{∂D} [Φ(x,y) |∂_n u(y)| + |∂_n Φ(x,y)| |g(y)|] dS(y)

Then |u(x)| ≤ v(x) by the triangle inequality and |G| = Φ.

Now, v is the sum of a single-layer potential and a double-layer potential for the LAPLACE equation, with non-negative densities. Both are harmonic in R³\D.

The single-layer potential S[|∂_n u|](x) = ∫ Φ(x,y) |∂_n u(y)| dS(y) is harmonic in R³\D and superharmonic everywhere (subharmonic? Let me think... Φ is harmonic away from the source, so S[σ] is harmonic in R³\D for σ on ∂D). It's continuous across ∂D.

The double-layer potential D[|g|](x) = ∫ ∂_n Φ(x,y) |g(y)| dS(y) is harmonic in R³\D. It has a jump across ∂D: the exterior limit is D[|g|]_+ = -1/2 |g| + K[|g|] and the interior limit is D[|g|]_- = 1/2 |g| + K[|g|] (where K is the double-layer operator).

Hmm, the signs depend on the convention. Let me be more careful.

For the exterior region (R³\D), the outward normal to the exterior region at ∂D is -n (where n is the outward normal to D). So the double layer potential with respect to the exterior is:
D_ext[|g|](x) = ∫_{∂D} ∂_{n_ext} Φ(x,y) |g(y)| dS(y) = -∫_{∂D} ∂_n Φ(x,y) |g(y)| dS(y)

where n is the outward normal to D. The jump relation for the exterior is:
D_ext[|g|]_ext = 1/2 |g| + K_ext[|g|]  (exterior limit)
D_ext[|g|]_int = -1/2 |g| + K_ext[|g|]  (interior limit)

This is getting complicated with the signs. Let me just focus on the key idea.

The function v is harmonic in R³\D and v ≥ |u| on ∂D (we need to verify this). If v ≥ |u| on ∂D and v ≥ |u| at infinity (both → 0, but v might not → 0...), then by the maximum principle for harmonic functions, v ≥ |u| in R³\D, giving |u| ≤ v ≤ sup_{∂D} v.

But we need sup_{∂D} v ≤ M, which requires controlling the boundary values of v in terms of M = sup|g|. The boundary values of v involve both |∂_n u| and |g|, and we don't have control over |∂_n u| in terms of |g| alone.

So this approach doesn't directly work. The issue is that the Green's representation involves both u and ∂_n u, and we can't bound ∂_n u in terms of u = g on the boundary.

Let me try a different representation. For the exterior Dirichlet problem, we can use the combined field integral equation or the Brakhage-Werner approach:

u(x) = ∫_{∂D} [∂G/∂n_y(x,y) - iη G(x,y)] μ(y) dS(y)

where η > 0 is a coupling parameter and μ solves the boundary integral equation:
(1/2 I + K - iη S) μ = g   on ∂D

Here K is the double-layer operator and S is the single-layer operator.

Then:
|u(x)| ≤        — AI历史解题过程（thinking）
#   deepmath_103k_00000417         — 题目ID

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
  <problem_id>deepmath_103k_00000417</problem_id>
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

Find the residue of the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) at \( z = 0 \).

## Standard Solution

Okay, so I need to find the residue of the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) at \( z = 0 \). Hmm, residues are related to Laurent series expansions around the point in question, right? And the residue itself is the coefficient of the \( \frac{1}{z} \) term in that expansion. Let me recall how that works.

First, \( z = 0 \) is a singularity of the function \( f(z) \). Since we're dealing with \( \sin\left(\frac{1}{z^2}\right) \), which has an essential singularity at \( z = 0 \) because as \( z \) approaches 0, \( \frac{1}{z^2} \) goes to infinity, and the sine function oscillates wildly. So multiplying that by \( z^2 \), the whole function \( f(z) \) will have an essential singularity at 0 as well. Therefore, to find the residue, I need to expand \( f(z) \) in a Laurent series around 0 and find the coefficient of \( \frac{1}{z} \).

Let me start by recalling the Taylor series expansion for \( \sin(w) \), which is \( \sin(w) = w - \frac{w^3}{3!} + \frac{w^5}{5!} - \cdots \). So if I substitute \( w = \frac{1}{z^2} \), then \( \sin\left(\frac{1}{z^2}\right) = \frac{1}{z^2} - \frac{1}{3! z^6} + \frac{1}{5! z^{10}} - \cdots \). Then multiplying by \( z^2 \), the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) becomes:

\( f(z) = z^2 \left( \frac{1}{z^2} - \frac{1}{6 z^6} + \frac{1}{120 z^{10}} - \cdots \right) \)

Let me compute that term by term:

First term: \( z^2 \times \frac{1}{z^2} = 1 \)

Second term: \( z^2 \times \left( -\frac{1}{6 z^6} \right) = -\frac{1}{6 z^4} \)

Third term: \( z^2 \times \frac{1}{120 z^{10}} = \frac{1}{120 z^8} \)

Fourth term: \( z^2 \times \left( -\frac{1}{5040 z^{14}} \right) = -\frac{1}{5040 z^{12}} \)

And so on. So each term alternates in sign and involves even negative powers of z. Wait a second, but the Laurent series expansion here seems to have terms with exponents of z decreasing by 4 each time? Let's see:

First term: exponent 0 (since it's 1)

Second term: exponent -4

Third term: exponent -8

Fourth term: exponent -12

Etc.

But the residue is the coefficient of \( z^{-1} \). However, in this expansion, all exponents are 0, -4, -8, -12, etc. So there is no \( z^{-1} \) term. That would imply that the coefficient of \( z^{-1} \) is zero, hence the residue is zero.

But wait, let me check if I made a mistake here. Let me go through the steps again.

Starting with the expansion of \( \sin(w) \):

\( \sin(w) = \sum_{n=0}^{\infty} \frac{(-1)^n w^{2n+1}}{(2n+1)!} \)

Therefore, substituting \( w = \frac{1}{z^2} \):

\( \sin\left(\frac{1}{z^2}\right) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} \left( \frac{1}{z^2} \right)^{2n+1} = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n -2} \)

Then, multiplying by \( z^2 \):

\( f(z) = z^2 \times \sin\left(\frac{1}{z^2}\right) = z^2 \times \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n -2} = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n} \)

So each term in the series is \( \frac{(-1)^n}{(2n+1)!} z^{-4n} \). So when n=0, term is \( \frac{1}{1!} z^{0} = 1 \). When n=1, term is \( -\frac{1}{3!} z^{-4} \). When n=2, term is \( \frac{1}{5!} z^{-8} \), etc.

So indeed, the exponents here are 0, -4, -8, -12, etc. All exponents are multiples of -4. Therefore, there are no terms with exponent -1. Therefore, the coefficient of \( z^{-1} \) is zero, so the residue at z=0 is zero.

But I need to make sure that I didn't miss any terms or make any miscalculations. Let me see.

Alternatively, maybe there's another approach. Since the residue is the coefficient of \( z^{-1} \), and the function is even, or has some symmetry. Wait, \( f(z) = z^2 \sin(1/z^2) \). Let me check if it's an even function. Let's substitute \( z \) with \( -z \):

\( f(-z) = (-z)^2 \sin\left( \frac{1}{(-z)^2} \right) = z^2 \sin\left( \frac{1}{z^2} \right) = f(z) \). So yes, it's an even function. Therefore, its Laurent series expansion about 0 will only have even exponents. Since the residue is the coefficient of \( z^{-1} \), which is an odd exponent term, and since all terms in the expansion are even exponents (0, -4, -8, etc.), there can't be a \( z^{-1} \) term. Therefore, the residue is zero.

Alternatively, using the residue formula for essential singularities. But I think for essential singularities, there is no direct formula other than expanding the Laurent series. But since this function is a product of a polynomial and a sine function with a singularity, expanding the Laurent series seems the way to go.

Alternatively, maybe using integration. The residue is \( \frac{1}{2\pi i} \int_{C} f(z) dz \), where C is a small circle around 0. But integrating this directly might be complicated. However, since we can expand the Laurent series and see that there is no \( z^{-1} \) term, the integral would be zero, hence residue is zero.

Another way to think about it: If I consider the Laurent series of \( \sin(1/z^2) \), which is \( \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} z^{-4n -2} \), then multiplying by \( z^2 \) gives \( \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} z^{-4n} \), which as we saw has exponents 0, -4, -8, etc. So again, no \( z^{-1} \).

Alternatively, could there be a mistake in substitution? Let me check for n=0: term is 1/(1!) z^{0}, correct. For n=1: term is -1/(6) z^{-4}, correct. So no, seems correct.

Therefore, since all terms are of the form \( z^{-4n} \), there's no term with exponent -1, so residue is 0.

Thus, the residue of \( f(z) \) at z=0 is 0.

**Final Answer**
The residue of \( f(z) \) at \( z = 0 \) is \boxed{0}.
</think>

To find the residue of the function \( f(z) = z^2 \sin\left(\frac{1}{z^2}\right) \) at \( z = 0 \), we need to expand the function in a Laurent series around \( z = 0 \) and identify the coefficient of the \( \frac{1}{z} \) term.

1. **Taylor series expansion of \( \sin(w) \)**:
   \[
   \sin(w) = w - \frac{w^3}{3!} + \frac{w^5}{5!} - \cdots
   \]
   Substituting \( w = \frac{1}{z^2} \), we get:
   \[
   \sin\left(\frac{1}{z^2}\right) = \frac{1}{z^2} - \frac{1}{3! z^6} + \frac{1}{5! z^{10}} - \cdots
   \]

2. **Multiplying by \( z^2 \)**:
   \[
   z^2 \sin\left(\frac{1}{z^2}\right) = z^2 \left( \frac{1}{z^2} - \frac{1}{6 z^6} + \frac{1}{120 z^{10}} - \cdots \right)
   \]
   Simplifying term by term:
   \[
   z^2 \sin\left(\frac{1}{z^2}\right) = 1 - \frac{1}{6 z^4} + \frac{1}{120 z^8} - \cdots
   \]

3. **Laurent series expansion**:
   The resulting series is:
   \[
   z^2 \sin\left(\frac{1}{z^2}\right) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} z^{-4n}
   \]
   This series contains only terms with exponents \( 0, -4, -8, -12, \ldots \), which are all even multiples of -4. There is no term with the exponent -1.

Since there is no \( \frac{1}{z} \) term in the Laurent series expansion, the coefficient of \( \frac{1}{z} \) is zero. Therefore, the residue of \( f(z) \) at \( z = 0 \) is \(\boxed{0}\).

## AI's Thinking (Attempted Solution Process)

The problem asks for the best bound constant C such that sup_{R^3/D} |u| ≤ C · sup_{∂D} |g| for the Helmholtz equation exterior Dirichlet problem.

Let me think about this carefully. This is a classic problem in scattering theory / PDE theory.

The exterior Dirichlet problem for Helmholtz: Δu + k²u = 0 in R³\D, u = g on ∂D, Sommerfeld radiation condition at infinity.

The question asks for the best (optimal) constant C in the maximum principle-type bound.

For the Laplace equation (k=0), the maximum principle gives C = 1 (harmonic functions attain max on boundary). But for Helmholtz (k ≠ 0), the maximum principle doesn't directly apply because the equation has the +k²u term, so it's not elliptic in the maximum principle sense.

Wait, actually for Helmholtz, the maximum principle fails. The solution can have interior values larger than boundary values. So the question is about the best constant.

Let me think about this more carefully. This is related to the work of various authors on maximum principles for Helmholtz equations.

Actually, let me reconsider. The problem is asking for the best bound constant C. This is a well-studied question.

For the Helmholtz equation, there's a result that relates to the "maximum principle" type estimates. The key reference is the work on the maximum modulus of solutions to the Helmholtz equation.

Actually, I recall that for the exterior problem, there's a classical result. Let me think about what the answer should be.

For the Helmholtz equation in exterior domains, the solution can be represented using the Green's function / single and double layer potentials. The maximum of |u| in the exterior can exceed the maximum of |g| on the boundary.

Hmm, but the problem says "determine the best bound constant C". This suggests there's a specific known answer.

Let me think about this differently. For the Helmholtz equation with radiation condition, the exterior Dirichlet problem has a unique solution. The question is about the operator norm of the solution operator from C(∂D) to C(R³\D).

Actually, I think the answer might be C = 1, but that can't be right for Helmholtz since the maximum principle doesn't hold.

Wait, let me reconsider. For the Helmholtz equation, there IS a version of the maximum principle. The key insight is that for the exterior problem with radiation condition, the solution decays at infinity (like 1/r), so the supremum is attained either on the boundary or in the interior.

For Helmholtz, the function |u| doesn't satisfy a maximum principle in the usual sense. However, there are results about the maximum modulus.

Let me think about the specific case. Consider the simplest case: D is a ball of radius a. Then we can solve explicitly using spherical harmonics and spherical Bessel functions.

For a ball of radius a with Dirichlet data g, the exterior solution involves h_l^(1)(kr) (Hankel functions). The ratio |u(r)|/|u(a)| for the l-th mode involves |h_l^(1)(kr)|/|h_l^(1)(ka)|.

For the maximum to exceed the boundary value, we need |h_l^(1)(kr)| > |h_l^(1)(ka)| for some r > a.

The Hankel functions h_l^(1)(x) for real x have |h_l^(1)(x)| ~ 1/x for large x (decaying). But near the origin they grow. For x > 0, |h_l^(1)(x)| is generally decreasing for large x but may have local behavior.

Actually, for the l=0 case, h_0^(1)(x) = -e^(ix)/(ix) = i·e^(ix)/x, so |h_0^(1)(x)| = 1/x, which is strictly decreasing. So for l=0, the maximum is at the boundary.

For higher l, h_l^(1)(x) = (-i)^(l+1) e^(ix)/x · (sum of terms). The modulus... let me think. Actually |h_l^(1)(x)|^2 = j_l(x)^2 + y_l(x)^2 where j_l, y_l are spherical Bessel functions.

For the l-th mode, the ratio is |h_l^(1)(kr)|/|h_l^(1)(ka)| for r ≥ a. The question is whether this can exceed 1.

I recall that |h_l^(1)(x)|^2 = j_l(x)^2 + y_l(x)^2. And there's a known result that this is a decreasing function of x for x > 0... actually no, that's not quite right.

Hmm, let me think about this differently. There's a classical result by... I think the answer to this problem is C = 1.

Actually wait. Let me reconsider the problem. The problem is about the BEST constant C. If the maximum principle held with C=1, that would be the answer. But for Helmholtz, does it?

Let me think about the maximum principle for Helmholtz more carefully. The equation is Δu + k²u = 0. If we try to apply the maximum principle: at an interior maximum of |u|, we'd need certain conditions. But the equation Δu = -k²u means that at a point where u is positive and maximal, Δu ≤ 0, but -k²u < 0, so Δu = -k²u < 0, which is consistent with a maximum. So the maximum principle doesn't prevent interior maxima.

In fact, for the Helmholtz equation, interior maxima CAN exceed boundary values. This is well known.

So C > 1 in general. The question is what the best constant is.

Hmm, but the problem says "determine the best bound constant C". This is phrased as if there's a definite answer. Let me think about whether the answer depends on k and the geometry of D, or if it's a universal constant.

If C depends on k and D, then the problem would need to specify more. Since it asks for "the best bound constant C", maybe the answer is that C = 1, achieved in some limit, or maybe the answer involves some specific value.

Actually, I think I need to reconsider. Let me re-read the problem.

"Determine the best bound constant C such that sup_{R³/D} |u| ≤ C · sup_{∂D} |g|"

This is asking for the optimal C. The answer could be:
1. C = 1 (if maximum principle holds)
2. C = some specific value > 1
3. C depends on k and D (in which case the problem is asking for the general form)

Let me think about whether there's a universal bound. 

For the exterior Helmholtz problem, the solution is given by a combination of single and double layer potentials. The mapping from boundary data to the solution is a bounded linear operator.

Actually, I recall now. There's a result that for the Helmholtz equation, the maximum principle in the form sup|u| ≤ sup|g| does NOT hold in general. However, there are modified maximum principles.

Let me think about this from the representation formula. The exterior solution can be written as:
u(x) = ∫_{∂D} [∂G/∂n(y) · μ(y) - G(x,y) · σ(y)] dS(y)

where G is the free-space Green's function G(x,y) = e^{ik|x-y|}/(4π|x-y|).

For the Dirichlet problem, u is represented as a double layer potential (or combined single-double layer).

The key question is about the maximum modulus principle for Helmholtz.

I think the answer might be C = 1. Here's my reasoning: 

Actually, no. Let me think about a specific example. Consider D = ball of radius a, and g = Y_l^m (spherical harmonic). Then the exterior solution is:
u(r,θ,φ) = [h_l^(1)(kr) / h_l^(1)(ka)] · Y_l^m(θ,φ)

The sup of |u| over R³\D is:
sup_{r≥a} |h_l^(1)(kr)| / |h_l^(1)(ka)| · sup|Y_l^m|

And sup_{∂D} |g| = sup|Y_l^m|.

So the ratio is sup_{r≥a} |h_l^(1)(kr)| / |h_l^(1)(ka)|.

For this to give C, we need sup_{r≥a} |h_l^(1)(kr)| / |h_l^(1)(ka)| ≤ C for all l and all a, k.

Now, |h_l^(1)(x)| = |j_l(x) + i·y_l(x)| = sqrt(j_l(x)^2 + y_l(x)^2).

For l=0: h_0^(1)(x) = e^{ix}/(ix) (up to sign), |h_0^(1)(x)| = 1/x. So the ratio is a/r ≤ 1. Good, C ≥ 1 works for l=0.

For general l: We know that h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · P_l(1/x) where P_l is a polynomial. More precisely:
h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · Σ_{m=0}^{l} (i)^m (l+m)!/((l-m)! m! (2x)^m)

Hmm, this is getting complicated. Let me think about whether |h_l^(1)(x)| is monotonically decreasing for x > 0.

Actually, I recall that j_l(x)^2 + y_l(x)^2 is NOT monotonically decreasing in general. Let me check for l=1.

h_1^(1)(x) = -e^{ix}(x+i)/x² (let me verify). 

Actually, h_1^(1)(x) = -e^{ix}/x · (1 + i/x) = -e^{ix}(x+i)/x².

|h_1^(1)(x)|² = (x²+1)/x⁴ = 1/x² + 1/x⁴.

So |h_1^(1)(x)| = sqrt(1/x² + 1/x⁴) = (1/x²)sqrt(x²+1) = sqrt(x²+1)/x².

Is this decreasing for x > 0? Let f(x) = sqrt(x²+1)/x². 
f'(x) = [x/sqrt(x²+1) · x² - sqrt(x²+1) · 2x] / x⁴ = [x³/sqrt(x²+1) - 2x·sqrt(x²+1)] / x⁴
= x[x²/sqrt(x²+1) - 2sqrt(x²+1)] / x⁴
= [x² - 2(x²+1)] / (x³ · sqrt(x²+1))
= [x² - 2x² - 2] / (x³ · sqrt(x²+1))
= -(x² + 2) / (x³ · sqrt(x²+1))

This is negative for all x > 0. So |h_1^(1)(x)| is strictly decreasing for x > 0.

Interesting. So for l=1, the ratio is also ≤ 1.

Let me check l=2. h_2^(1)(x) = -ie^{ix}/x · (1 + 3i/x - 3/x²).

|h_2^(1)(x)|² = (1/x²) · |1 + 3i/x - 3/x²|² = (1/x²) · [(1 - 3/x²)² + 9/x²]
= (1/x²) · [1 - 6/x² + 9/x⁴ + 9/x²]
= (1/x²) · [1 + 3/x² + 9/x⁴]
= 1/x² + 3/x⁴ + 9/x⁶.

Let me check if this is decreasing. Let t = 1/x², so |h_2^(1)|² = t + 3t² + 9t³. As x increases, t decreases, and since the polynomial in t has positive coefficients, |h_2^(1)|² decreases. So |h_2^(1)(x)| is decreasing.

In general, |h_l^(1)(x)|² = (1/x²) · |P_l(1/x)|² where P_l is a polynomial with... and the modulus squared will be a polynomial in 1/x with positive coefficients (I believe), making it a decreasing function of x.

Actually, let me think about this more carefully. The general formula:
h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · Σ_{m=0}^{l} (i)^m (l+m)!/((l-m)!(2x)^m · m!)

Wait, let me use the standard formula. The spherical Hankel function:
h_l^(1)(x) = (-i)^{l+1} e^{ix}/x · Σ_{m=0}^{l} (i/x)^m · (l+m)!/((l-m)!m!2^m)

Hmm, I'm not sure about the exact form. Let me use a different approach.

We know that h_l^(1)(x) = j_l(x) + i y_l(x), and there's a relation:
|h_l^(1)(x)|² = j_l(x)² + y_l(x)².

There's a known identity: j_l(x)² + y_l(x)² = Σ_{m=0}^{l} (2l-m)!/(m!(l-m)!(2x)^{2l-2m+1})... no, that doesn't look right either.

Actually, there's a classical result. Let me think about it using the relation to ordinary Bessel functions. h_l^(1)(x) = sqrt(π/(2x)) H_{l+1/2}^(1)(x).

And |H_ν^(1)(x)|² = J_ν(x)² + Y_ν(x)².

For half-integer order ν = l + 1/2, the Bessel functions have closed forms in terms of exponentials and polynomials.

There's a known result that for ν ≥ 1/2 (i.e., l ≥ 0), J_ν(x)² + Y_ν(x)² is a decreasing function of x for x > 0. This is related to the fact that the function is related to the modulus of a Hankel function.

Actually, I recall that there IS a theorem that |h_l^(1)(x)| is strictly decreasing for x > 0 and all l ≥ 0. This would mean that for the ball, the maximum of |u| is always attained on the boundary, giving C = 1 for the ball.

But does this extend to general domains? For general smooth bounded D, the solution is not simply a single mode. The question is whether the maximum principle sup|u| ≤ sup|g| holds for general exterior domains.

Hmm, for the Helmholtz equation, the standard maximum principle does NOT hold. The equation Δu + k²u = 0 is not amenable to the maximum principle because of the +k²u term (it's like an eigenvalue equation).

But wait - in the exterior domain with radiation condition, the solution decays at infinity. So the supremum is attained either on ∂D or at some interior point of R³\D.

At an interior maximum point x₀ of |u| (assuming u is real-valued for simplicity, or considering |u|²), if u(x₀) > 0 is a local max of u, then Δu(x₀) ≤ 0, but Δu = -k²u, so -k²u(x₀) ≤ 0, which means u(x₀) ≥ 0. This is consistent - it doesn't give a contradiction. So the maximum principle doesn't prevent interior maxima.

However, the question is whether for the EXTERIOR problem specifically, the maximum is always on the boundary. The ball example suggests it might be.

Let me think about this differently. Consider the function v = |u|². Then:
Δv = 2|∇u|² + 2ūΔu + 2uΔū = 2|∇u|² - 2k²|u|²

So Δv = 2|∇u|² - 2k²v.

At a maximum of v in the interior, Δv ≤ 0, so 2|∇u|² - 2k²v ≤ 0, which gives |∇u|² ≤ k²v. This doesn't prevent the maximum from being in the interior.

So in general, for the Helmholtz equation, interior maxima of |u| can exceed boundary values. The maximum principle with C=1 does NOT hold in general for interior problems.

But for EXTERIOR problems with radiation condition, the situation might be different because of the decay at infinity and the specific structure.

Hmm, but I showed that for the ball, |h_l^(1)(x)| is decreasing, so the maximum is on the boundary. Does this hold for all domains?

Actually, I think the answer is C = 1, and this is a known result. Let me think about why.

The key insight might be the following: for the exterior Helmholtz problem with radiation condition, the solution can be represented using the Green's function, and there's a positivity/maximum principle argument.

Actually, wait. I don't think C = 1 is correct in general. Let me think of a counterexample.

Consider a domain D that is very thin and elongated. The exterior solution could potentially have focusing effects that amplify the field beyond the boundary values.

Actually, let me reconsider. For the Helmholtz equation, there's a concept of "scattering resonances" and the solution can be large when k is near a resonance. But for the exterior Dirichlet problem with real k, the solution exists and is unique (no resonances for the exterior Dirichlet problem with real k, I think).

Hmm, actually, the exterior Dirichlet problem for real k > 0 always has a unique solution (this is a standard result). The question is about the bound.

Let me think about this problem from the perspective of the Rellich lemma and radiation conditions.

Actually, I think I should approach this more carefully. The problem is asking for the "best bound constant C". This is a well-posed mathematical question.

Let me consider the operator T: C(∂D) → C(R³\D) that maps boundary data g to the solution u. The norm of this operator is:
||T|| = sup_{g≠0} sup_{R³\D} |u| / sup_{∂D} |g|

The best constant C is ||T||.

For the Laplace equation (k=0), C = 1 by the maximum principle.

For Helmholtz (k > 0), the situation is different. Let me think about whether C = 1 or C > 1.

I think the answer is C = 1, based on the following reasoning:

For the exterior problem, we can use the Green's representation:
u(x) = ∫_{∂D} [G(x,y) ∂u/∂n(y) - ∂G/∂n_y(x,y) u(y)] dS(y)

where G(x,y) = e^{ik|x-y|}/(4π|x-y|) and n is the outward normal to D (inward to the exterior).

But this involves both u and ∂u/∂n, so it's not directly a bound in terms of g alone.

Alternatively, using layer potentials: u = D[μ] (double layer) or u = S[σ] + D[μ] (combined).

For the Dirichlet problem, we can write u = S[σ] where σ satisfies the integral equation (for the single-layer representation, which works for k not an interior eigenvalue):
g(x) = S[σ](x) for x ∈ ∂D (first kind), or
σ/2 + K'[σ] = ∂g/∂n (second kind, but this needs Neumann data).

Actually, the standard approach for the exterior Dirichlet problem is:
u(x) = S[σ](x) for x ∈ R³\D, where σ solves S[σ] = g on ∂D (if k² is not an interior Dirichlet eigenvalue),
or u(x) = D[μ](x) where μ solves (1/2 I + K)[μ] = g on ∂D (if k² is not an interior Neumann eigenvalue, or using combined layers).

This is getting complicated. Let me step back and think about what the "expected" answer is for this type of problem.

Given the way the problem is phrased ("determine the best bound constant C"), I think the answer is C = 1. This is the maximum principle for the exterior Helmholtz problem.

But I need to verify this. Let me think about whether the maximum principle holds for the exterior Helmholtz problem.

Claim: For the exterior Dirichlet problem with radiation condition, sup_{R³\D} |u| ≤ sup_{∂D} |g|.

Proof attempt: Consider w = |u|². We have Δw = 2|∇u|² - 2k²w. At an interior maximum of w, Δw ≤ 0, so |∇u|² ≤ k²w. This doesn't give a contradiction.

But we also have the radiation condition: u decays like 1/r at infinity. So w → 0 as r → ∞. Thus the supremum of w is attained either on ∂D or at an interior point.

If the supremum is attained at an interior point x₀, then w(x₀) = M (the max), and Δw(x₀) ≤ 0. But this is consistent with the equation. So we can't rule out interior maxima this way.

Hmm, so the naive maximum principle argument doesn't work. But maybe there's a more sophisticated argument.

Let me think about the Phragmén-Lindelöf type arguments or other methods.

Actually, I recall that for the Helmholtz equation, there's a result by... I think it's related to the work of Protter and Weinberger, or maybe Rellich.

Wait, I think the key is the following. For the Helmholtz equation in an exterior domain with the Sommerfeld radiation condition, there IS a maximum principle, but it requires a more careful argument.

One approach: Use the fact that the fundamental solution G(x,y) = e^{ik|x-y|}/(4π|x-y|) satisfies |G(x,y)| = 1/(4π|x-y|), which is the same as the Laplace fundamental solution. So |G| is harmonic in each variable (away from the singularity).

If u is represented as u(x) = ∫_{∂D} G(x,y) σ(y) dS(y) (single layer), then:
|u(x)| ≤ ∫_{∂D} |G(x,y)| |σ(y)| dS(y) = ∫_{∂D} (1/(4π|x-y|)) |σ(y)| dS(y)

The right-hand side is a single-layer potential for the LAPLACE equation with density |σ|. Let's call it v(x). Then v is harmonic in R³\D, v → 0 at infinity, and v ≥ |u| on ∂D (well, we need to be more careful).

Actually, this doesn't directly give us what we want because we need to relate σ to g.

Let me think differently. 

For the Laplace exterior problem, the maximum principle gives C = 1. For Helmholtz, the equation has the +k²u term which breaks the maximum principle.

But here's an important observation: the radiation condition forces the solution to be "outgoing", and this might restore a maximum principle.

Actually, I think the answer is NOT C = 1 in general. Let me think of a specific example.

Consider the 1D case (which is simpler). The Helmholtz equation u'' + k²u = 0 on (a, ∞) with u(a) = g and radiation condition u(x) = Ce^{ikx} for large x. The solution is u(x) = g · e^{ik(x-a)}, so |u(x)| = |g| for all x. So C = 1 in 1D.

In 3D, for a ball with l=0 mode: u(r) = g · (a/r) e^{ik(r-a)}, so |u(r)| = |g| · a/r ≤ |g|. C = 1.

For l=1: u(r) = g · h_1^(1)(kr)/h_1^(1)(ka). We showed |h_1^(1)(x)| is decreasing, so |u(r)| ≤ |g|. C = 1.

For general l and ball: same argument, C = 1.

So for balls, C = 1. What about general domains?

Let me think about whether there's a general argument. 

Consider the exterior problem. Let M = sup_{∂D} |g|. We want to show |u(x)| ≤ M for all x ∈ R³\D.

Consider the function φ(x) = M (constant). Then Δφ + k²φ = k²M ≠ 0, so φ is not a solution. We can't directly compare.

But consider w = u - φ or w = |u| - M. These don't satisfy nice equations.

Alternatively, consider the auxiliary function ψ(x) = M · a/|x| (for some appropriate a). This is harmonic and decays. But Δψ + k²ψ = k²ψ ≠ 0.

Hmm, the issue is that for Helmholtz, we can't use constant or harmonic comparison functions.

Let me try a different approach. Consider the "modified" maximum principle using an auxiliary function.

Let me try: w(x) = |u(x)|² - M² · (R/|x|)² for some R. Then we want to show w ≤ 0.

Actually, this is getting complicated. Let me think about whether the result C = 1 is actually true.

I found a potential issue. Consider a domain D that is the union of two balls far apart. The scattered wave from one ball can interfere with the other. Could this create constructive interference that exceeds the boundary values?

Actually, for the Dirichlet problem, if g is supported on one ball and zero on the other, the solution near the other ball is the scattered field, which could potentially be large due to focusing. But the boundary value on the second ball is zero, and the solution there is the scattered field from the first ball, which could be nonzero. So |u| on ∂D (second ball) could be nonzero even though g = 0 there. But wait, u = g on ∂D, so if g = 0 on the second ball, then u = 0 on the second ball. So the solution is zero on the second ball's boundary. The scattered field from the first ball must be exactly canceled by the field reradiated from the second ball. This is a complicated interaction.

The point is: can the solution in the exterior exceed M = sup|g|? 

Let me think about a concrete example. Take D = ball of radius a, g = 1 (constant). Then the solution is:
u(r) = (a/r) · e^{ik(r-a)} · (h_0^(1)(kr)/h_0^(1)(ka))... wait, for l=0:
u(r) = h_0^(1)(kr)/h_0^(1)(ka) = [e^{ikr}/(ikr)] / [e^{ika}/(ika)] = (a/r) e^{ik(r-a)}.
|u(r)| = a/r ≤ 1 = M. So C = 1 for this case.

Now take g = Y_l^m for some l > 0. Then |u(r,θ,φ)| = |h_l^(1)(kr)|/|h_l^(1)(ka)| · |Y_l^m(θ,φ)|. Since |h_l^(1)(x)| is decreasing, |u| ≤ |Y_l^m| = M on ∂D... wait, M = sup_{∂D} |g| = sup |Y_l^m|, and on the boundary r = a, |u| = |g| = |Y_l^m| ≤ M. In the exterior, |u(r)| ≤ |h_l^(1)(ka)|/|h_l^(1)(ka)| · M = M. So C = 1.

OK so for balls, C = 1 always. The question is whether this extends to general domains.

I believe the answer is C = 1, and this is a known result in scattering theory. The key result is sometimes called the "maximum principle for the Helmholtz equation in exterior domains."

Let me try to prove it. The idea is to use the Green's function representation and the fact that |G(x,y)| = 1/(4π|x-y|) (the Laplace Green's function).

For the exterior Dirichlet problem, the solution can be written as:
u(x) = -∫_{∂D} ∂G_D/∂n_y (x,y) g(y) dS(y)

where G_D is the Dirichlet Green's function for the exterior Helmholtz problem. But this is circular.

Alternatively, using the free-space Green's function:
u(x) = ∫_{∂D} [G_0(x,y) ∂u/∂n(y) - ∂G_0/∂n_y(x,y) g(y)] dS(y)

where G_0(x,y) = e^{ik|x-y|}/(4π|x-y|).

Taking absolute values:
|u(x)| ≤ ∫_{∂D} [|G_0(x,y)| |∂u/∂n(y)| + |∂G_0/∂n_y(x,y)| |g(y)|] dS(y)

This involves |∂u/∂n| which we don't control. So this direct approach doesn't work.

Let me try a different approach. 

Approach via the Rellich radiation condition and uniqueness:

Actually, let me think about this problem from a higher level. The problem is asking for the "best bound constant C". In many textbooks and references on scattering theory, the maximum principle for the Helmholtz equation in exterior domains is discussed.

I recall that there is indeed a maximum principle for the exterior Helmholtz problem, and it states that C = 1. The proof typically uses the following argument:

1. The solution u can be represented via layer potentials.
2. The key property is that the free-space Green's function satisfies |G(x,y)| = 1/(4π|x-y|), which is positive and equals the Laplace Green's function in modulus.
3. Using the representation and the maximum principle for harmonic functions, one can show |u| ≤ M.

But I'm not sure about the details. Let me try to construct a proof.

Proof attempt using the Green's function:

Let me use the fact that for the exterior Dirichlet problem, the solution can be written as:
u(x) = ∫_{∂D} K(x,y) g(y) dS(y)

where K(x,y) is the Dirichlet-to-solution kernel (Poisson kernel for the exterior Helmholtz problem).

If we can show that ∫_{∂D} |K(x,y)| dS(y) ≤ 1 for all x ∈ R³\D, then |u(x)| ≤ M · ∫|K| dS ≤ M, giving C = 1.

For the Laplace equation, the Poisson kernel is positive and integrates to 1, giving C = 1. For Helmholtz, the kernel is complex-valued and not necessarily positive, so ∫|K| could exceed 1.

Hmm, so this approach suggests C might be > 1 for Helmholtz.

Let me reconsider. Maybe C = 1 is not the answer.

Actually, let me think about this more carefully with a specific non-ball example.

Consider D = ball of radius a, but with non-trivial boundary data. We showed that for each spherical harmonic mode, the ratio is ≤ 1. But for general g (sum of modes), the solution is:
u(r,θ,φ) = Σ_{l,m} g_{lm} · h_l^(1)(kr)/h_l^(1)(ka) · Y_l^m(θ,φ)

Then |u(r,θ,φ)| ≤ Σ_{l,m} |g_{lm}| · |h_l^(1)(kr)|/|h_l^(1)(ka)| · |Y_l^m(θ,φ)|

Since |h_l^(1)(kr)|/|h_l^(1)(ka)| ≤ 1, we get:
|u(r,θ,φ)| ≤ Σ_{l,m} |g_{lm}| · |Y_l^m(θ,φ)|

But sup_{∂D} |g| = sup_{θ,φ} |Σ g_{lm} Y_l^m|, which is NOT the same as Σ |g_{lm}| |Y_l^m|. So we can't directly conclude |u| ≤ M from this.

However, for the ball, we can use a different argument. For each fixed r > a, the mapping g(θ,φ) → u(r,θ,φ) is a convolution (in the spherical harmonic sense) with kernel that has |coefficient| ≤ 1. But this doesn't directly give the sup norm bound.

Actually, for the ball, we can use the following: the solution at radius r is obtained from the boundary data at radius a by applying the operator T_r that multiplies each spherical harmonic mode by h_l^(1)(kr)/h_l^(1)(ka). The norm of T_r as an operator on C(S²) (with sup norm) is... well, it's not simply the max of the coefficients.

Hmm, this is getting complicated. Let me think about whether there's a simpler approach.

Actually, for the ball with g = 1 (constant, l=0 mode), we get |u(r)| = a/r ≤ 1. For g = Y_1^0 = cos θ, we get |u(r,θ)| = |h_1^(1)(kr)|/|h_1^(1)(ka)| · |cos θ| ≤ 1. For general g, the solution is a sum, and by the triangle inequality, |u| ≤ Σ |g_{lm}| · (ratio_l) · |Y_l^m| ≤ Σ |g_{lm}| · |Y_l^m|, but this doesn't bound by sup|g|.

So actually, for the ball, the question is whether the operator norm of T_r (from C(S²) to C(S²)) is ≤ 1 for all r > a. This is NOT obvious from the modal analysis.

Let me think about this differently. For the ball, we can use the Poisson integral representation. The exterior Helmholtz solution for the ball can be written as:

u(r,θ,φ) = ∫_{S²} P(r,θ,φ; θ',φ') g(θ',φ') dΩ'

where P is the Poisson kernel for the exterior Helmholtz problem for the ball.

For the Laplace equation, P_Laplace = (a²-r²... no, for exterior, P = (r²-a²)/... hmm, for the exterior Laplace problem, the Poisson kernel is P(r,ξ) = (r²-a²)/(4πa(r²-2ar ξ·η+a²)^{3/2})... I don't remember the exact form.

For Helmholtz, the Poisson kernel is different and complex-valued. The question is whether ∫|P| dΩ' ≤ 1.

This is getting quite involved. Let me step back and think about what the "expected" answer is.

Given that this is posed as a problem to "determine the best bound constant C", and given the structure of the problem (exterior Helmholtz with radiation condition), I believe the answer is:

C = 1

This is based on the maximum principle for the Helmholtz equation in exterior domains, which holds due to the radiation condition.

Let me try to give a proof. The key idea is:

Theorem (Maximum principle for exterior Helmholtz): If u satisfies Δu + k²u = 0 in R³\D with u = g on ∂D and the Sommerfeld radiation condition, then sup_{R³\D} |u| ≤ sup_{∂D} |g|.

Proof: Let M = sup_{∂D} |g|. We want to show |u(x)| ≤ M for all x ∈ R³\D.

Consider the auxiliary function v(x) = M · h_0^(1)(k|x-x₀|) / h_0^(1)(kR) for appropriate x₀ and R... no, this doesn't work because we need a global comparison function.

Let me try another approach. The key observation is:

For the exterior problem, we can use the Green's representation:
u(x) = ∫_{∂D} [∂G/∂n_y (x,y) g(y)] dS(y)  (using the Dirichlet Green's function, where the single layer term vanishes)

Wait, actually for the Dirichlet Green's function G_D(x,y) (which vanishes when x ∈ ∂D), we have:
u(x) = -∫_{∂D} ∂G_D/∂n_y (x,y) · g(y) dS(y)

This is the Poisson integral representation. The Dirichlet Green's function for the exterior Helmholtz problem satisfies:
- (Δ_y + k²) G_D(x,y) = δ(x-y) in R³\D
- G_D(x,y) = 0 for y ∈ ∂D
- Radiation condition in y

The Poisson kernel is P(x,y) = -∂G_D/∂n_y (x,y) for x ∈ R³\D, y ∈ ∂D.

For the Laplace equation, P(x,y) > 0 and ∫_{∂D} P(x,y) dS(y) = 1, giving C = 1.

For Helmholtz, G_D is complex, so P is complex, and ∫|P| dS could exceed 1.

So the question reduces to: is ∫_{∂D} |P(x,y)| dS(y) ≤ 1 for the Helmholtz Poisson kernel?

I don't think this is true in general. The Helmholtz Poisson kernel is complex-valued and can have cancellations, but |P| could integrate to more than 1.

Hmm, so maybe C > 1 after all.

Let me think about this problem from a completely different angle. Maybe the answer is not C = 1 but rather involves some other expression.

Actually, wait. Let me reconsider the problem statement. It says "Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|". 

This is asking for the optimal C. If C = 1 works, then it's the best possible (since we can achieve equality, e.g., with constant g on a ball). If C = 1 doesn't work, then we need to find the actual optimal C.

I think the answer is C = 1, and here's a potential proof strategy:

Proof using the Green's function and the maximum principle for harmonic functions:

The free-space Green's function is G(x,y) = e^{ik|x-y|}/(4π|x-y|). Note that |G(x,y)| = 1/(4π|x-y|) =: Φ(x,y), the Laplace fundamental solution.

The solution to the exterior Dirichlet problem can be represented as:
u(x) = ∫_{∂D} [G(x,y) ∂u/∂n(y) - ∂G/∂n_y(x,y) g(y)] dS(y)

Now, let's define:
ũ(x) = ∫_{∂D} [Φ(x,y) |∂u/∂n(y)| + |∂Φ/∂n_y(x,y)| |g(y)|] dS(y)

Then |u(x)| ≤ ũ(x). But ũ involves both |∂u/∂n| and |g|, so this doesn't directly help.

Let me try yet another approach. 

Approach using the Fourier transform / plane wave representation:

The outgoing solution can be represented as a superposition of plane waves:
u(x) = ∫_{S²} A(θ̂) e^{ik θ̂·x} dθ̂

for some amplitude function A. But this is for the whole space, not the exterior of a bounded domain.

Hmm, let me think about this more carefully.

Actually, I think I should consider the possibility that the answer is C = 1 and try to prove it using a clever auxiliary function.

Key idea: Use the auxiliary function w(x) = |u(x)|² and show that it satisfies a maximum principle in a modified sense.

We have Δw = 2|∇u|² - 2k²w. At a maximum of w in the interior, Δw ≤ 0, so |∇u|² ≤ k²w. This means the gradient is bounded but doesn't prevent the maximum.

But wait, we also have the radiation condition. The solution u satisfies the Sommerfeld radiation condition:
lim_{r→∞} r(∂u/∂r - iku) = 0

This means u ~ e^{ikr}/r for large r, so |u| ~ 1/r → 0. Thus w → 0 at infinity, and the maximum of w is attained either on ∂D or at an interior point.

If the maximum is at an interior point x₀, then w(x₀) = M² (where M = sup|u|), and Δw(x₀) ≤ 0. But this is consistent with the equation. So we can't rule out interior maxima by this argument alone.

However, there's a stronger result. Let me think about whether there's a Rellich-type identity or a unique continuation argument.

Actually, I think the correct approach is to use the following theorem:

Theorem: For the exterior Dirichlet problem of the Helmholtz equation with Sommerfeld radiation condition, the maximum principle holds: sup_{R³\D} |u| = sup_{∂D} |u|.

This is indeed a known result. The proof uses the following idea:

Consider the function v(x) = Re[u(x) e^{-iα}] for some angle α. Then v satisfies Δv + k²v = 0 and v = Re[g e^{-iα}] on ∂D. Also, v satisfies the radiation condition (in a suitable sense) and v → 0 at infinity.

Now, v is real-valued and satisfies Δv + k²v = 0. At a positive maximum of v in the interior, Δv ≤ 0 and v > 0, so Δv = -k²v < 0, which is consistent. So the maximum principle for v doesn't directly work either.

Hmm. Let me think about this differently.

Actually, I recall now that for the Helmholtz equation, the maximum principle does NOT hold in general, even for exterior domains. The constant C = 1 is not always achievable.

But the problem asks to "determine the best bound constant C". If C depends on the geometry and k, then the answer would be in terms of those. But the problem seems to ask for a universal constant.

Wait, re-reading the problem: "Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|". 

Maybe the answer is that C = 1, and this is the best possible. Or maybe the answer is that no finite C exists (but that can't be right since the solution operator is bounded).

Actually, the solution operator IS bounded for each fixed k and D (this follows from the well-posedness of the exterior Dirichlet problem). So C is finite. The question is what the best (smallest) C is.

If the problem is asking for a universal C that works for ALL D and ALL k, then... hmm, that's a different question. Let me re-read.

"Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|"

I think this is asking for the best C in terms of the given data (k, D). But since no specific k or D is given, maybe it's asking for a universal bound.

If it's a universal bound over all k > 0 and all smooth bounded D, then we need to find sup over all such problems of the operator norm.

For the ball, C = 1. For general domains, C might be larger. The question is whether C = 1 universally or if there's a larger universal bound.

I think the answer is C = 1, and this is a classical result. Let me try to find the right proof.

Actually, I just realized something. Let me think about the problem using the Fourier transform / spectral approach.

For the exterior problem, the solution can be written using the Green's function. The key property of the outgoing Green's function is:

G(x,y) = e^{ik|x-y|}/(4π|x-y|)

Note that |G(x,y)| = 1/(4π|x-y|) = Φ(x,y) (the Laplace Green's function).

Now, for the exterior Dirichlet problem, using the Green's representation formula:
u(x) = ∫_{∂D} [G(x,y) ∂_n u(y) - ∂_n G(x,y) u(y)] dS(y)

where ∂_n is the normal derivative pointing into the exterior (outward from D).

Now, here's the key idea. Define:
v(x) = ∫_{∂D} [Φ(x,y) |∂_n u(y)| + |∂_n Φ(x,y)| |u(y)|] dS(y)

where Φ = 1/(4π|x-y|) is the Laplace Green's function. Then |u(x)| ≤ v(x).

Now, v is a sum of single and double layer potentials for the LAPLACE equation with non-negative densities |∂_n u| and |u|. 

The single layer potential S[|∂_n u|](x) = ∫ Φ(x,y) |∂_n u(y)| dS(y) is harmonic in R³\D and continuous everywhere.

The double layer potential D[|u|](x) = ∫ ∂_n Φ(x,y) |u(y)| dS(y) is harmonic in R³\D.

Both are harmonic in the exterior and decay at infinity. By the maximum principle for harmonic functions:
sup_{R³\D} v = max(sup_{∂D} v^+, sup_{∂D} v^-)

where v^± are the boundary values from outside and inside.

But this gives a bound in terms of both |∂_n u| and |u| on the boundary, not just |u| = |g|.

So this approach doesn't directly give C = 1.

Let me try yet another approach. 

I think the key insight might be to use the following property of the Helmholtz Green's function:

For the exterior Dirichlet problem, the Poisson kernel P(x,y) = -∂G_D/∂n_y (x,y) where G_D is the Dirichlet Green's function. The claim would be that ∫_{∂D} |P(x,y)| dS(y) ≤ 1.

For the Laplace equation, this is true because P > 0 and ∫ P dS = 1. For Helmholtz, P is complex, so we need |∫ P g dS| ≤ M ∫|P| dS, and we need ∫|P| dS ≤ 1.

But I don't think ∫|P| dS ≤ 1 is true in general for Helmholtz. The complex nature of P means that |P| can be larger than |Re P|, and the integral of |P| can exceed 1.

OK, I'm going in circles. Let me try to think about this from the perspective of what's known in the literature.

I believe the relevant result is:

For the Helmholtz equation in an exterior domain with Sommerfeld radiation condition, the maximum principle sup|u| ≤ sup_{∂D}|g| DOES hold, and the best constant is C = 1.

The proof uses a clever argument involving the radiation condition. Here's the idea:

Proof: Let M = sup_{∂D} |g|. Suppose for contradiction that |u(x₀)| > M for some x₀ ∈ R³\D.

Consider the function w(x) = u(x) - M·e^{ik|x-x₀|}/(4π|x-x₀|) · C for some constant C... no, this doesn't work.

Let me try a different approach. The key is the following lemma:

Lemma: If u satisfies Δu + k²u = 0 in R³\D, the Sommerfeld radiation condition, and |u| ≤ M on ∂D, then |u| ≤ M in R³\D.

Proof of Lemma: 
Consider the auxiliary function φ(x) = M (constant). Then Δφ + k²φ = k²M ≠ 0, so φ is not a supersolution.

Instead, consider ψ(x) = M · Re[e^{ikr}/(ikr)] = M · cos(kr)/(kr) ... no, this doesn't work either because it depends on the choice of origin.

OK let me try the approach using the real and imaginary parts separately.

Let u = v + iw where v, w are real. Then Δv + k²v = 0 and Δw + k²w = 0, with v = Re g, w = Im g on ∂D.

For v: at a maximum of v in the interior, Δv ≤ 0 and v > 0, so -k²v ≤ 0, consistent. At a minimum, Δv ≥ 0 and v < 0, so -k²v ≥ 0, consistent. So no maximum principle for v alone.

But here's the key: v satisfies the radiation condition (Re part of the outgoing condition), and v → 0 at infinity. So v attains its max and min either on ∂D or in the interior.

Hmm, I'm stuck. Let me try to look at this from the energy perspective.

Energy approach: 
∫_{R³\D} (|∇u|² - k²|u|²) dx = ∫_{∂D} ū ∂_n u dS

This is the Rellich identity. It relates the L² norm of u to boundary integrals. But this gives an L² bound, not an L∞ bound.

OK, I think I need to just go with my best understanding. Let me consider two possibilities:

1. C = 1: The maximum principle holds for the exterior Helmholtz problem.
2. C > 1: The maximum principle doesn't hold, and the best constant is something else.

Given that:
- For balls, C = 1 (shown by the monotonicity of |h_l^(1)(x)|)
- The standard maximum principle argument doesn't directly work for Helmholtz
- The problem asks to "determine the best bound constant C"

I think the answer is C = 1, and the proof uses a more sophisticated argument than the standard maximum principle.

Let me try to construct a proof using the following idea:

The solution u to the exterior Dirichlet problem can be represented as:
u(x) = ∫_{∂D} P(x,y) g(y) dS(y)

where P(x,y) is the Poisson kernel. For the Laplace equation, P ≥ 0 and ∫P dS = 1. For Helmholtz, P is complex.

The key claim is that for the Helmholtz exterior problem, the Poisson kernel satisfies:
∫_{∂D} |P(x,y)| dS(y) ≤ 1

This would give |u(x)| ≤ M ∫|P| dS ≤ M.

But I'm not sure this is true. Let me think about whether there's a proof.

Actually, I think the correct statement might be different. Let me reconsider.

For the Helmholtz equation, the Poisson kernel for the exterior of a ball of radius a is:
P(r,θ,φ; θ',φ') = Σ_{l,m} [h_l^(1)(kr)/h_l^(1)(ka)] Y_l^m(θ,φ) Ȳ_l^m(θ',φ')

The integral ∫|P| dΩ' is hard to compute in general. But for the l=0 case (g = constant), P = (a/r) e^{ik(r-a)} and |P| = a/r, so ∫|P| dΩ' = (a/r) · 4π... wait, that's not right. Let me be more careful.

For g = 1 (constant on ∂D = sphere of radius a), the solution is u(r) = (a/r) e^{ik(r-a)}. The Poisson kernel for this case is P = (a/r) e^{ik(r-a)} / (4πa²) ... no, that's not right either.

Actually, the Poisson kernel P(x,y) for x in the exterior and y on the sphere satisfies:
u(x) = ∫_{S²} P(x,y) g(y) dS(y)

For g = 1, u(x) = (a/|x|) e^{ik(|x|-a)}, so ∫ P(x,y) dS(y) = (a/|x|) e^{ik(|x|-a)}.

For the Laplace case, P ≥ 0 and ∫ P dS = a/|x| ≤ 1. For Helmholtz, |∫ P dS| = a/|x| ≤ 1, but ∫ |P| dS could be different from |∫ P dS|.

So the question is: is ∫|P| dS = |∫ P dS| = a/r? This would require P to have constant phase, which is not the case in general (for non-constant g).

Hmm, I think for the ball, the Poisson kernel for Helmholtz is:
P(r,ξ; a,η) = Σ_l (2l+1)/(4π) · [h_l^(1)(kr)/h_l^(1)(ka)] · P_l(cos γ)

where γ is the angle between ξ and η, and P_l is the Legendre polynomial.

The modulus of this sum is hard to compute. The integral ∫|P| dΩ_η is generally NOT equal to |∫ P dΩ_η| = a/r.

So for the ball, ∫|P| dS could exceed 1, which means C > 1 for the ball when using general boundary data.

Wait, but I showed earlier that for each individual mode, the ratio is ≤ 1. The issue is with superposition of modes. Let me think about this more carefully.

For the ball, consider g(θ) = P_0(cos θ) + ε P_L(cos θ) for large L and small ε. The solution is:
u(r,θ) = [h_0^(1)(kr)/h_0^(1)(ka)] P_0(cos θ) + ε [h_L^(1)(kr)/h_L^(1)(ka)] P_L(cos θ)

At r = a: u = g, so |u| ≤ |g| ≤ 1 + ε (if we normalize). Actually, sup|g| = sup|1 + ε P_L| = 1 + ε (since P_L ranges in [-1,1]).

At r > a: |u(r,θ)| = |(a/r) e^{ik(r-a)} + ε [h_L^(1)(kr)/h_L^(1)(ka)] P_L(cos θ)|

The first term has modulus a/r. The second term has modulus ε · |h_L^(1)(kr)|/|h_L^(1)(ka)| ≤ ε. So:
|u(r,θ)| ≤ a/r + ε ≤ 1 + ε = sup|g|

So for this case, C = 1 still works! The triangle inequality gives us the bound because each mode's ratio is ≤ 1.

Wait, but this is using the triangle inequality on the modal expansion, which gives:
|u| ≤ Σ_l |g_l| · |ratio_l| · |P_l| ≤ Σ_l |g_l| · |P_l|

And we need this to be ≤ sup|g| = sup|Σ g_l P_l|.

But Σ |g_l| |P_l| is NOT bounded by sup|Σ g_l P_l| in general! The triangle inequality gives |u| ≤ Σ |g_l| |ratio_l| |P_l| ≤ Σ |g_l| |P_l|, but Σ |g_l| |P_l| can be much larger than sup|g|.

For example, take g = P_0 + P_1 = 1 + cos θ. Then sup|g| = 2 (at θ = 0). And Σ |g_l| |P_l| = 1 · 1 + 1 · |cos θ| = 1 + |cos θ| ≤ 2. So in this case it works.

But take g = P_0 - P_1 = 1 - cos θ. Then sup|g| = 2 (at θ = π). And Σ |g_l| |P_l| = 1 + |cos θ| ≤ 2. Still works.

Hmm, what about g = P_0 + P_2 = 1 + (3cos²θ-1)/2? sup|g| = sup|1 + (3cos²θ-1)/2| = sup|(1 + 3cos²θ)/2| = 2 (at θ = 0). And Σ|g_l||P_l| = 1 + |(3cos²θ-1)/2| ≤ 1 + 1 = 2. Still works.

Actually, the issue is that for orthogonal polynomials, Σ |g_l| |P_l| can exceed sup|g| when the signs are chosen adversarially. But in the examples above, it seems to work.

Let me try a more extreme example. Take g = Σ_{l=0}^{L} a_l P_l where the a_l are chosen so that g is small everywhere (sup|g| is small) but Σ|a_l| is large. This is possible because the P_l are bounded by 1 but not orthogonal in L∞.

For instance, take g_L(θ) = P_L(cos θ). Then sup|g| = 1, and the solution is u(r,θ) = [h_L^(1)(kr)/h_L^(1)(ka)] P_L(cos θ), with |u| ≤ |P_L| ≤ 1 = sup|g|. So C = 1 for this case.

Take g = P_0 + P_1 + ... + P_L. Then sup|g| = sup|Σ P_l|. At θ = 0, all P_l(1) = 1, so g(0) = L+1. Thus sup|g| = L+1. And the solution:
|u(r,θ)| ≤ Σ |h_l^(1)(kr)/h_l^(1)(ka)| |P_l(cos θ)| ≤ Σ |P_l(cos θ)|

At θ = 0: Σ |P_l(1)| = L+1 = sup|g|. So |u| ≤ sup|g|. C = 1.

But what if we choose g so that the P_l interfere destructively on ∂D but constructively in the exterior? Since the ratios h_l^(1)(kr)/h_l^(1)(ka) are different for different l (they have different phases), the destructive interference on ∂D might become constructive at some r > a.

This is the key question! Let me think about this.

At r = a, the ratios are all 1 (by construction), so u(a,θ) = g(θ). At r > a, the ratios are h_l^(1)(kr)/h_l^(1)(ka), which have different magnitudes and phases for different l. So the modal sum that was g(θ) at r = a becomes a different function at r > a.

Could this different function have a larger sup norm? In principle, yes, because the phase shifts could turn destructive interference into constructive interference.

But we showed that |h_l^(1)(kr)/h_l^(1)(ka)| ≤ 1 for all l and r > a. So each mode's amplitude decreases. The question is whether the phase shifts can cause constructive interference that overcomes the amplitude decrease.

Let me try a specific example. Take l = 0 and l = 1, with g(θ) = P_0 - P_1 = 1 - cos θ. Then sup|g| = 2 (at θ = π).

The solution is:
u(r,θ) = [h_0^(1)(kr)/h_0^(1)(ka)] - [h_1^(1)(kr)/h_1^(1)(ka)] cos θ

Let me compute this at a specific r. Let's take ka = 1, kr = 2 (so r = 2a).

h_0^(1)(x) = -e^{ix}/(ix) = ie^{ix}/x (up to sign convention). Let me use h_0^(1)(x) = e^{ix}/(ix). Then:
|h_0^(1)(x)| = 1/x.
h_0^(1)(1) = e^{i}/i = -ie^{i} = -i(cos1 + i sin1) = sin1 - i cos1.
h_0^(1)(2) = e^{2i}/(2i) = -ie^{2i}/2 = (sin2 - i cos2)/2.

Ratio_0 = h_0^(1)(2)/h_0^(1)(1) = (sin2 - i cos2)/(2(sin1 - i cos1)).

Let me compute numerically:
sin1 ≈ 0.8415, cos1 ≈ 0.5403
sin2 ≈ 0.9093, cos2 ≈ -0.4161

h_0^(1)(1) = 0.8415 - 0.5403i
h_0^(1)(2) = (0.9093 + 0.4161i)/2 = 0.4547 + 0.2080i

Ratio_0 = (0.4547 + 0.2080i)/(0.8415 - 0.5403i)

Let me compute: (0.4547 + 0.2080i)(0.8415 + 0.5403i) / |0.8415 - 0.5403i|²
= (0.4547·0.8415 + 0.2080·0.5403 + i(0.2080·0.8415 - 0.4547·0.5403)) / (0.8415² + 0.5403²)
= (0.3826 + 0.1124 + i(0.1750 - 0.2457)) / (0.7081 + 0.2919)
= (0.4950 - 0.0707i) / 1.0
= 0.4950 - 0.0707i

|Ratio_0| = sqrt(0.4950² + 0.0707²) = sqrt(0.2450 + 0.0050) = sqrt(0.2500) = 0.5 = a/r. ✓

Now for l = 1:
h_1^(1)(x) = -e^{ix}(x+i)/x² (using one convention). Let me use h_1^(1)(x) = -e^{ix}/x · (1 + i/x).

Actually, let me use the standard formula. h_1^(1)(x) = -e^{ix}(x+i)/x². Let me verify: for large x, h_1^(1)(x) ≈ -e^{ix}/x, which matches the asymptotic. OK.

h_1^(1)(1) = -e^{i}(1+i)/1 = -e^{i}(1+i) = -(cos1+isin1)(1+i) = -(cos1+isin1+icos1-sin1) = -(cos1-sin1) - i(sin1+cos1) = (sin1-cos1) - i(sin1+cos1)
= (0.8415-0.5403) - i(0.8415+0.5403) = 0.3012 - 1.3818i

|h_1^(1)(1)| = sqrt(0.3012² + 1.3818²) = sqrt(0.0907 + 1.9094) = sqrt(2.0001) ≈ √2. 

Actually, |h_1^(1)(x)|² = (x²+1)/x⁴, so |h_1^(1)(1)|² = 2/1 = 2. ✓

h_1^(1)(2) = -e^{2i}(2+i)/4 = -(cos2+isin2)(2+i)/4 = -(cos2·2-sin2·1 + i(cos2·1+sin2·2))/4
= -(2cos2-sin2 + i(cos2+2sin2))/4
= -(-0.8322-0.9093 + i(-0.4161+1.8186))/4
= -(-1.7415 + 1.4025i)/4
= (1.7415 - 1.4025i)/4
= 0.4354 - 0.3506i

|h_1^(1)(2)|² = (4+1)/16 = 5/16. |h_1^(1)(2)| = √(5)/4 ≈ 0.5590. ✓ (0.4354² + 0.3506² = 0.1896 + 0.1229 = 0.3125 = 5/16 ✓)

Ratio_1 = h_1^(1)(2)/h_1^(1)(1) = (0.4354 - 0.3506i)/(0.3012 - 1.3818i)

Let me compute: (0.4354 - 0.3506i)(0.3012 + 1.3818i) / |0.3012 - 1.3818i|²
Numerator: 0.4354·0.3012 + 0.3506·1.3818 + i(0.4354·1.3818 - 0.3506·0.3012)
= 0.1311 + 0.4844 + i(0.6016 - 0.1056)
= 0.6155 + 0.4960i

Denominator: 0.3012² + 1.3818² = 0.0907 + 1.9094 = 2.0001 ≈ 2

Ratio_1 = (0.6155 + 0.4960i)/2 = 0.3078 + 0.2480i

|Ratio_1| = sqrt(0.3078² + 0.2480²) = sqrt(0.0947 + 0.0615) = sqrt(0.1562) ≈ 0.3950

And |h_1^(1)(2)|/|h_1^(1)(1)| = √(5/16)/√2 = √(5/32) ≈ √0.15625 ≈ 0.3953. ✓

Now, the solution at r = 2a (with ka=1, kr=2):
u(2a, θ) = Ratio_0 · 1 - Ratio_1 · cos θ
= (0.4950 - 0.0707i) - (0.3078 + 0.2480i) cos θ

|u(2a, θ)|² = |0.4950 - 0.0707i - (0.3078 + 0.2480i)cos θ|²
= (0.4950 - 0.3078cos θ)² + (0.0707 + 0.2480cos θ)²

Let me find the maximum over θ. Let c = cos θ ∈ [-1, 1].
f(c) = (0.4950 - 0.3078c)² + (0.0707 + 0.2480c)²
= 0.2450 - 0.3047c + 0.0947c² + 0.0050 + 0.0351c + 0.0615c²
= 0.2500 - 0.2696c + 0.1562c²

f'(c) = -0.2696 + 0.3124c = 0 → c = 0.2696/0.3124 ≈ 0.863

f(0.863) = 0.2500 - 0.2696·0.863 + 0.1562·0.863² = 0.2500 - 0.2327 + 0.1164 = 0.1337

f(-1) = 0.2500 + 0.2696 + 0.1562 = 0.6758
f(1) = 0.2500 - 0.2696 + 0.1562 = 0.1366

So the maximum is at c = -1 (θ = π): f(-1) = 0.6758, |u| = √0.6758 ≈ 0.822.

Now, sup_{∂D} |g| = sup|1 - cos θ| = 2 (at θ = π).

So |u(2a, π)| ≈ 0.822 ≤ 2 = sup|g|. ✓ C = 1 works here.

But wait, this is a weak test because the solution is much smaller than the boundary data. Let me try a case where the boundary data has destructive interference.

Take g(θ) = P_0 + P_1 = 1 + cos θ. Then sup|g| = 2 (at θ = 0).

u(2a, θ) = Ratio_0 + Ratio_1 cos θ = (0.4950 - 0.0707i) + (0.3078 + 0.2480i) cos θ

|u|² = (0.4950 + 0.3078c)² + (-0.0707 + 0.2480c)²
= 0.2450 + 0.3047c + 0.0947c² + 0.0050 - 0.0351c + 0.0615c²
= 0.2500 + 0.2696c + 0.1562c²

f'(c) = 0.2696 + 0.3124c = 0 → c = -0.863

f(-0.863) = 0.2500 - 0.2327 + 0.1164 = 0.1337
f(-1) = 0.2500 - 0.2696 + 0.1562 = 0.1366
f(1) = 0.2500 + 0.2696 + 0.1562 = 0.6758

Max at c = 1 (θ = 0): |u| = √0.6758 ≈ 0.822 ≤ 2 = sup|g|. ✓

Again, C = 1 works, but the solution is much smaller than the boundary data. This is because the ratios are significantly less than 1 at r = 2a.

Let me try r very close to a, say r = a + ε for small ε. Then the ratios are close to 1, and the solution is close to g. So |u| ≈ |g| ≤ sup|g|. C = 1 works.

The question is whether at some intermediate r, the phase shifts can cause |u| to exceed sup|g|.

Let me try a case with more modes and specific phase relationships. Take g(θ) = P_0 - ε P_L for large L, where ε is chosen so that sup|g| is not much larger than 1.

sup|g| = sup|1 - ε P_L(cos θ)|. Since |P_L| ≤ 1, sup|g| ≤ 1 + ε. And at θ = 0, g = 1 - ε. At a zero of P_L, g = 1. At a maximum of P_L (θ = 0, P_L = 1), g = 1 - ε. At a minimum (P_L = -1), g = 1 + ε. So sup|g| = 1 + ε.

The solution: u(r,θ) = Ratio_0(r) - ε Ratio_L(r) P_L(cos θ).

|u|² = |Ratio_0|² - 2ε Re[Ratio_0 · conj(Ratio_L)] P_L + ε² |Ratio_L|² P_L²

The maximum of |u|² over θ is at most:
|Ratio_0|² + 2ε |Ratio_0| |Ratio_L| |P_L| + ε² |Ratio_L|² P_L²
≤ |Ratio_0|² + 2ε |Ratio_0| |Ratio_L| + ε² |Ratio_L|²
= (|Ratio_0| + ε |Ratio_L|)²

So |u| ≤ |Ratio_0| + ε |Ratio_L| ≤ 1 + ε = sup|g|.

This uses the triangle inequality and the fact that |Ratio_l| ≤ 1. So for any two-mode case, C = 1 works!

In fact, this generalizes. For g = Σ a_l P_l:
|u(r,θ)| = |Σ a_l Ratio_l(r) P_l(cos θ)| ≤ Σ |a_l| |Ratio_l(r)| |P_l(cos θ)| ≤ Σ |a_l| |P_l(cos θ)|

But we need Σ |a_l| |P_l(cos θ)| ≤ sup_θ |Σ a_l P_l(cos θ)| = sup|g|.

This is NOT true in general! Σ |a_l| |P_l(cos θ)| can exceed sup|Σ a_l P_l(cos θ)|.

For example, take g = P_0 + P_1 - P_2 (with appropriate normalization). Then sup|g| might be smaller than Σ|a_l| sup|P_l| = 1 + 1 + 1 = 3.

But wait, the bound |u| ≤ Σ |a_l| |P_l| is a very crude bound. The actual |u| could be much smaller due to the complex phases of the ratios.

Hmm, but the question is whether there EXISTS some g and some r > a such that |u(r)| > sup|g|. The crude bound doesn't rule this out, but it also doesn't prove it.

Let me think about this more carefully. The key question is:

For the ball, is the operator T_r: C(S²) → C(S²) defined by (T_r g)(θ) = Σ a_l Ratio_l(r) P_l(cos θ) bounded by 1 in the sup norm?

The operator norm of T_r is sup_{||g||_∞=1} ||T_r g||_∞. 

For the Laplace case, Ratio_l(r) = (a/r)^{l+1} (all real and positive), and the operator is a contraction (||T_r|| ≤ 1) by the maximum principle for harmonic functions.

For Helmholtz, Ratio_l(r) = h_l^(1)(kr)/h_l^(1)(ka) (complex). The operator T_r is NOT a positive operator, so the maximum principle doesn't directly apply.

However, I showed that |Ratio_l(r)| ≤ 1 for all l and r > a. This means T_r is a contraction in the L² sense (by Parseval), but not necessarily in L∞.

The operator norm in L∞ could be larger than 1. Let me think about whether it can be.

Consider the extreme case where all Ratio_l have the same phase. Then T_r acts like a real positive operator, and ||T_r|| ≤ 1 (by the same argument as Laplace, since |Ratio_l| ≤ 1 and the Poisson kernel for Laplace has ||T|| = 1).

But the Ratio_l have DIFFERENT phases for different l. This means T_r is not a positive operator, and the L∞ norm could be larger.

Wait, but I showed in the two-mode examples that |u| ≤ sup|g| even with different phases. Let me think about why.

In the two-mode case g = a_0 P_0 + a_1 P_1:
|u|² = |a_0 R_0 + a_1 R_1 cos θ|² = |a_0|²|R_0|² + 2 Re[a_0 ā_1 R_0 R̄_1] cos θ + |a_1|²|R_1|² cos²θ

The maximum over θ ∈ [-1,1] of this quadratic in c = cos θ is:
At c = ±1: |a_0 R_0 ± a_1 R_1|² ≤ (|a_0||R_0| + |a_1||R_1|)² ≤ (|a_0| + |a_1|)²

And sup|g| = sup|a_0 + a_1 cos θ| = |a_0| + |a_1| (at θ = 0 or π).

So |u| ≤ |a_0| + |a_1| = sup|g|. ✓

This works because for two modes, sup|g| = |a_0| + |a_1| (the L∞ norm of a linear function on [-1,1] is attained at the endpoints).

For three or more modes, sup|g| < Σ|a_l| in general, and the argument breaks down.

Let me try three modes. Take g(θ) = P_0 + P_1 + P_2 = 1 + cos θ + (3cos²θ-1)/2 = (1 + 2cos θ + 3cos²θ)/2.

sup|g|: Let c = cos θ. g = (1 + 2c + 3c²)/2. g' = (2 + 6c)/2 = 1 + 3c = 0 → c = -1/3.
g(-1/3) = (1 - 2/3 + 1/3)/2 = (2/3)/2 = 1/3.
g(1) = (1+2+3)/2 = 3. g(-1) = (1-2+3)/2 = 1.
So sup|g| = 3 (at θ = 0).

Now, Σ|a_l| = 1 + 1 + 1 = 3 = sup|g|. So the crude bound gives |u| ≤ 3 = sup|g|. Still works!

Hmm, it seems like for the Legendre polynomial basis, sup|Σ a_l P_l| = Σ|a_l| when all a_l have the same sign (because P_l(1) = 1 for all l, so g(0) = Σ a_l).

What if the a_l have different signs? Take g = P_0 - P_1 + P_2 = 1 - cos θ + (3cos²θ-1)/2 = (1 - 2cos θ + 3cos²θ)/2.

sup|g|: g(c) = (1 - 2c + 3c²)/2. g' = (-2+6c)/2 = -1+3c = 0 → c = 1/3.
g(1/3) = (1 - 2/3 + 1/3)/2 = (2/3)/2 = 1/3.
g(1) = (1-2+3)/2 = 1. g(-1) = (1+2+3)/2 = 3.
sup|g| = 3 (at θ = π).

Again, Σ|a_l| = 3 = sup|g|. 

This is because P_l(-1) = (-1)^l, so g(π) = Σ a_l (-1)^l. If a_l = (-1)^l, then g(π) = Σ 1 = L+1 = Σ|a_l|.

So for the specific choice a_l = ±1, we always have sup|g| = Σ|a_l|, and the crude bound gives C = 1.

But what about more general coefficients? Take g = P_0 + 2P_1 - P_2 = 1 + 2cos θ - (3cos²θ-1)/2 = (3 - 4cos θ - 3cos²θ)/2... let me recompute.

g(c) = 1 + 2c - (3c²-1)/2 = (2 + 4c - 3c² + 1)/2 = (3 + 4c - 3c²)/2.

g'(c) = (4 - 6c)/2 = 2 - 3c = 0 → c = 2/3.
g(2/3) = (3 + 8/3 - 4/3)/2 = (3 + 4/3)/2 = (13/3)/2 = 13/6 ≈ 2.17.
g(1) = (3+4-3)/2 = 2. g(-1) = (3-4-3)/2 = -2.
sup|g| = 13/6 ≈ 2.17.

Σ|a_l| = 1 + 2 + 1 = 4.

So Σ|a_l| = 4 > 13/6 ≈ 2.17 = sup|g|. The crude bound gives |u| ≤ 4, but sup|g| ≈ 2.17. So the crude bound is NOT sufficient to show C = 1.

But this doesn't mean C > 1; it just means the crude bound is too crude. The actual |u| might still be ≤ sup|g| due to the complex phases of the ratios.

Let me compute the actual solution for this case. Take ka = 1, kr = 1.1 (r close to a, so ratios close to 1).

For r close to a, Ratio_l ≈ 1 + (r-a) · (d/dr)[h_l^(1)(kr)/h_l^(1)(ka)]|_{r=a} = 1 + (r-a) · k · h_l'^(1)(ka)/h_l^(1)(ka).

The derivatives h_l'^(1)(x) = dh_l^(1)/dx. Using the recurrence h_l'^(1)(x) = l/x · h_l^(1)(x) - h_{l+1}^(1)(x).

For l=0: h_0'^(1)(x) = -h_1^(1)(x). So Ratio_0' = k · (-h_1^(1)(ka))/h_0^(1)(ka).
For l=1: h_1'^(1)(x) = (1/x) h_1^(1)(x) - h_2^(1)(x). So Ratio_1' = k · [(1/(ka)) h_1^(1)(ka) - h_2^(1)(ka)] / h_1^(1)(ka) = k/(ka) - k h_2^(1)(ka)/h_1^(1)(ka) = 1/a - k h_2^(1)(ka)/h_1^(1)(ka).

This is getting very complicated. Let me try a different approach.

Instead of computing specific examples, let me think about the general theory.

I think the answer is C = 1, and the proof is based on the following key theorem:

Theorem (Maximum principle for exterior Helmholtz): Let u solve the exterior Dirichlet problem for the Helmholtz equation with Sommerfeld radiation condition. Then:
sup_{R³\D} |u| ≤ sup_{∂D} |u|

Proof: The proof uses the following idea. Consider the function:
v(x) = u(x) / φ(x)
where φ is a suitable positive function satisfying (Δ + k²)φ ≤ 0 in R³\D and φ > 0, with φ → ∞ or φ → 0 at infinity in a way that helps.

Actually, the standard approach for proving maximum principles for equations with lower-order terms is to use an auxiliary function. For the equation Δu + k²u = 0, we can write it as Δu = -k²u. 

If we consider w = |u|², then Δw = 2|∇u|² - 2k²w ≥ -2k²w. So Δw + 2k²w ≥ 0, meaning w is a supersolution of Δw + 2k²w = 0.

Hmm, this doesn't directly help.

Let me try the approach using the function e^{-αr} where r = |x|.

Consider w(x) = |u(x)|² · e^{α|x|} for some α > 0. Then:
∇w = e^{αr}(2 Re(ū ∇u) + α |u|² x̂)
Δw = e^{αr}(2|∇u|² + 2 Re(ū Δu) + 4α Re(ū ∇u · x̂) + α |u|² + α² |u|² r... 

This is getting messy. Let me try a different auxiliary function.

Actually, let me try the approach from the book "Inverse Acoustic and Electromagnetic Scattering" by Colton and Kress, or similar references.

I recall that in scattering theory, the following result is known:

For the exterior Dirichlet problem, the solution operator is bounded from C(∂D) to C(R³\D), and the bound depends on k and the geometry. The maximum principle with C = 1 does NOT hold in general for the Helmholtz equation.

Wait, but I showed that for the ball, C = 1 (at least for the cases I checked). And the crude bound using |Ratio_l| ≤ 1 gives C = 1 for the ball when the coefficients are all ±1. But for general coefficients, the crude bound doesn't give C = 1.

Hmm, let me think about this differently. Maybe the answer is NOT C = 1, and the problem is asking for a different kind of bound.

Actually, re-reading the problem: "Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|". 

Maybe the answer is that C = 1 is the best constant, and this is a theorem that needs to be proved. Or maybe the answer is something else entirely.

Let me think about what happens for general domains. For a non-convex domain, the scattered field could potentially focus and create regions where |u| > sup|g|. This is related to the concept of "scattering focusing" or "near-field enhancement".

Actually, I think for the Helmholtz equation, the maximum principle with C = 1 does NOT hold in general, and the best constant depends on the domain and k. But the problem asks to "determine" C, suggesting there's a specific answer.

Let me reconsider the problem. Maybe the answer is C = 1, and the proof is non-trivial but known. Or maybe the answer is that C = 1 is the best constant, achieved in the limit as k → 0 or for specific geometries.

Actually, I just thought of something. For the Helmholtz equation, there's a result known as the "maximum principle for the real part" or something similar. Let me think...

For a real-valued solution v of Δv + k²v = 0, if v has a positive local maximum at x₀, then Δv(x₀) ≤ 0 and v(x₀) > 0, so -k²v(x₀) ≤ 0, which is consistent. So no maximum principle.

But for the EXTERIOR problem with radiation condition, the solution decays at infinity. So if v is real and positive somewhere in the exterior, it must attain its maximum either on ∂D or at an interior point. If at an interior point, the above analysis shows it's consistent. So the maximum principle doesn't hold even for the exterior problem.

This means C > 1 is possible. The question is: what is the best C?

I think the problem might be asking for C = 1 as the answer, with the understanding that this is the best possible constant (achieved for the Laplace limit or for balls). But I'm not confident.

Let me try another approach. Maybe the answer is related to the following:

For the Helmholtz equation, the solution can be written as u = u_s + u_i where u_i is the incident wave and u_s is the scattered wave. But for the Dirichlet problem with boundary data g, there's no incident wave; the solution is purely determined by g.

Hmm, let me reconsider the problem from scratch. 

The problem is: Δu + k²u = 0 in R³\D, u = g on ∂D, Sommerfeld radiation condition. Find the best C such that sup_{R³\D} |u| ≤ C sup_{∂D} |g|.

I think the answer is C = 1, and here's a proof sketch:

Proof: 
Step 1: The solution u can be represented using the Green's function for the exterior Dirichlet problem:
u(x) = ∫_{∂D} P(x,y) g(y) dS(y)
where P(x,y) = -∂G_D/∂n_y (x,y) is the Poisson kernel.

Step 2: For the Laplace equation, P_Laplace ≥ 0 and ∫ P_Laplace dS = 1, giving C = 1.

Step 3: For Helmholtz, G_D(x,y) = G_0(x,y) - ∫_{∂D} G_0(x,z) μ(y,z) dS(z) (method of images / double layer correction), where G_0 is the free-space Green's function and μ is the density that makes G_D vanish on ∂D.

Step 4: The key property is that |G_0(x,y)| = Φ(x,y) (Laplace Green's function). Using this, one can show that the Poisson kernel for Helmholtz satisfies ∫|P| dS ≤ 1.

But I'm not sure about Step 4. Let me think about whether it's true.

Actually, I don't think Step 4 is true in general. The Helmholtz Poisson kernel is complex, and its modulus can integrate to more than 1.

OK, I think I need to take a different approach entirely. Let me consider the possibility that the answer is C = 1 and try to prove it using a different method.

Method: Use the Fourier transform / plane wave representation and the properties of the radiation condition.

The outgoing solution can be represented as:
u(x) = ∫_{S²} A(θ̂) e^{ik θ̂·x} dθ̂

where A is the far-field amplitude (this is the Herglotz representation for radiating solutions). Wait, this is for solutions in all of R³, not just the exterior.

Actually, for the exterior problem, the solution has the asymptotic behavior:
u(x) ~ e^{ikr}/r · f(θ̂) as r → ∞

where f is the far-field pattern. The solution is determined by the boundary data g.

Hmm, this doesn't directly help with the maximum principle.

Let me try yet another approach. 

Method: Use the fact that the solution to the exterior Helmholtz problem can be obtained as the limit of solutions to the exterior Laplace problem with a complexified wave number.

Consider the family of problems: Δu_σ + (k + iσ)² u_σ = 0 in R³\D, u_σ = g on ∂D, radiation condition. As σ → 0, u_σ → u.

For σ > 0, the equation is Δu_σ + (k² - σ² + 2ikσ) u_σ = 0, which is the Yukawa/Helmholtz equation with complex wave number. The term 2ikσ provides damping.

For the damped case, the maximum principle might hold because the damping term causes |u_σ| to decrease. Specifically, for the equation Δu + (k² - σ² + 2ikσ)u = 0, the imaginary part of the wave number provides absorption, which should give a maximum principle.

Let me check: for the equation Δu + λu = 0 with Im(λ) > 0 (absorptive), does the maximum principle hold?

Consider w = |u|². Δw = 2|∇u|² + 2 Re(ū Δu) = 2|∇u|² - 2 Re(λ) |u|².

If Re(λ) < 0 (i.e., λ = -|λ| with |Re(λ)| > 0), then Δw = 2|∇u|² + 2|Re(λ)| w ≥ 0. This means w is subharmonic, so its maximum is on the boundary. This gives the maximum principle!

For our case, λ = k² - σ² + 2ikσ. Re(λ) = k² - σ². For σ > k, Re(λ) < 0, and the maximum principle holds. For σ < k, Re(λ) > 0, and the maximum principle doesn't hold from this argument.

So for σ > k, we get sup|u_σ| ≤ sup|g|, i.e., C = 1. But we need this for σ = 0 (the original problem), where Re(λ) = k² > 0.

Hmm, so this approach works for the strongly damped case but not for the original Helmholtz equation.

Let me try a different auxiliary function. Instead of w = |u|², consider w = |u|² · φ for some positive function φ.

Δ(w) = Δ(|u|² φ) = φ Δ|u|² + 2 ∇|u|² · ∇φ + |u|² Δφ
= φ(2|∇u|² - 2k²|u|²) + 2 ∇|u|² · ∇φ + |u|² Δφ
= 2φ|∇u|² + 2∇|u|² · ∇φ + |u|²(Δφ - 2k²φ)

If we choose φ such that Δφ - 2k²φ ≥ 0 (i.e., φ is a subsolution of Δφ = 2k²φ), then:
Δw ≥ 2φ|∇u|² + 2∇|u|² · ∇φ ≥ ... 

This doesn't directly give subharmonicity because of the cross term.

Let me try φ = e^{α|x|}. Then:
∇φ = α x̂ e^{αr}
Δφ = (α² + 2α/r) e^{αr} (in 3D, Δ e^{αr} = (α² + 2α/r) e^{αr})

Δφ - 2k²φ = (α² + 2α/r - 2k²) e^{αr}

For this to be ≥ 0, we need α² + 2α/r ≥ 2k² for all r > R₀ (some large radius). For large r, this requires α² ≥ 2k², i.e., α ≥ k√2.

But then φ = e^{αr} → ∞ as r → ∞, which means w = |u|² e^{αr} → ∞ (since |u|² ~ 1/r² and e^{αr} → ∞). So w doesn't attain its maximum on ∂D; it goes to infinity. This doesn't help.

Let me try φ = e^{-αr} instead. Then:
Δφ = (α² - 2α/r) e^{-αr}
Δφ - 2k²φ = (α² - 2α/r - 2k²) e^{-αr}

For large r, this is (α² - 2k²) e^{-αr}. For this to be ≥ 0, we need α ≥ k√2.

With φ = e^{-αr} and α ≥ k√2, w = |u|² e^{-αr} → 0 as r → ∞ (since |u|² ~ 1/r² and e^{-αr} → 0). So w attains its maximum either on ∂D or at an interior point.

If w attains its maximum at an interior point x₀, then Δw(x₀) ≤ 0. But:
Δw = 2φ|∇u|² + 2∇|u|² · ∇φ + |u|²(Δφ - 2k²φ)

At the maximum, ∇w = 0, which means:
2 Re(ū ∇u) φ + |u|² ∇φ = 0
So Re(ū ∇u) = -|u|² ∇φ/(2φ) = -|u|² α x̂/2

And Δw(x₀) = 2φ|∇u|² + 2∇|u|² · ∇φ + |u|²(Δφ - 2k²φ) ≤ 0

∇|u|² = 2 Re(ū ∇u), so:
2∇|u|² · ∇φ = 4 Re(ū ∇u) · ∇φ = 4(-|u|² α x̂/2) · (α x̂ φ) = -2α² |u|² φ

So: Δw(x₀) = 2φ|∇u|² - 2α²|u|²φ + |u|²(Δφ - 2k²φ) ≤ 0
= 2φ|∇u|² + |u|²(Δφ - 2k²φ - 2α²φ) ≤ 0

Now, Δφ - 2k²φ - 2α²φ = (α² - 2α/r - 2k² - 2α²) e^{-αr} = (-α² - 2α/r - 2k²) e^{-αr} < 0.

So: Δw(x₀) = 2φ|∇u|² - |u|²(α² + 2α/r + 2k²)φ ≤ 0

This gives: 2|∇u|² ≤ |u|²(α² + 2α/r + 2k²)

This is consistent (no contradiction), so the maximum of w could be in the interior. This means w could have an interior maximum, and we can't conclude w ≤ w|_{∂D}.

Hmm, so this approach also doesn't work. The issue is that the Helmholtz equation genuinely doesn't satisfy a maximum principle in the usual sense.

Let me try a completely different approach. Maybe the answer is NOT C = 1.

Actually, let me reconsider. I've been assuming the answer should be a clean constant, but maybe the answer involves the geometry. Let me re-read the problem.

"Determine the best bound constant C such that sup_{R³/D}|u| ≤ C · sup_{∂D}|g|"

The problem says "the best bound constant C". This suggests there's a specific value. Given the way the problem is set up (general D, general k, general g), the answer should be a universal constant.

I think the answer is C = 1. Here's my best argument:

The key is the following theorem, which I believe is correct:

Theorem: For the exterior Dirichlet problem of the Helmholtz equation with Sommerfeld radiation condition, the maximum principle holds: sup_{R³\D} |u| ≤ sup_{∂D} |g|.

The proof uses the Rellich radiation condition and a unique continuation argument. Here's the idea:

1. Let M = sup_{∂D} |g|. Assume for contradiction that |u(x₀)| > M for some x₀ ∈ R³\D.

2. Consider the function v(x) = u(x) - M·ψ(x) where ψ is a suitable comparison function. We need ψ to satisfy (Δ + k²)ψ = 0, ψ = 1 on ∂D, and the radiation condition.

3. If such ψ exists with |ψ(x)| ≤ 1 for all x ∈ R³\D, then |v| ≤ |u| + M|ψ| and... no, this doesn't work directly.

Actually, let me think about this using the Poisson kernel approach more carefully.

For the ball of radius a, the Poisson kernel for the exterior Helmholtz problem is:
P(r,ξ;η) = Σ_{l=0}^∞ (2l+1)/(4π) · [h_l^(1)(kr)/h_l^(1)(ka)] · P_l(ξ·η)

The solution is u(r,ξ) = ∫_{S²} P(r,ξ;η) g(aη) dΩ(η).

Now, ∫_{S²} P(r,ξ;η) dΩ(η) = [h_0^(1)(kr)/h_0^(1)(ka)] = (a/r) e^{ik(r-a)} (using the addition theorem and the fact that ∫ P_l dΩ = 4π δ_{l0}).

So |∫ P dΩ| = a/r ≤ 1. But ∫|P| dΩ could be larger.

The question is: is ∫|P(r,ξ;η)| dΩ(η) ≤ 1 for all r > a and all ξ?

For the Laplace case, P ≥ 0 and ∫ P dΩ = a/r ≤ 1, so ∫|P| = ∫P ≤ 1. ✓

For Helmholtz, P is complex. Let me compute ∫|P|² dΩ first (using Parseval):
∫|P|² dΩ = Σ_{l} (2l+1)/(4π)² · |h_l^(1)(kr)/h_l^(1)(ka)|² · 4π/(2l+1) ... 

Actually, by the addition theorem, P(r,ξ;η) = Σ_l (2l+1)/(4π) R_l P_l(ξ·η) where R_l = h_l^(1)(kr)/h_l^(1)(ka). 

∫|P|² dΩ_η = Σ_l (2l+1)/(4π)² |R_l|² ∫ P_l(ξ·η)² dΩ_η = Σ_l (2l+1)/(4π)² |R_l|² · 4π/(2l+1) = Σ_l |R_l|²/(4π).

Since |R_l| ≤ 1, we have ∫|P|² dΩ ≤ Σ_l 1/(4π) = ∞. So the L² norm is infinite (the series doesn't converge). This means P is not in L², which makes sense because it's a distribution (Poisson kernel).

OK, this approach is not working well. Let me try to think about the problem from a higher level.

I think the answer is C = 1, and the proof is based on the following key insight:

For the exterior Helmholtz problem with radiation condition, the solution u satisfies a maximum principle because the radiation condition selects the "outgoing" solution, which is the one that decays at infinity. The decay at infinity, combined with the equation, forces the maximum to be on the boundary.

The formal proof might go as follows:

1. The solution u is analytic in R³\D and continuous on R³\D̄ (closure).
2. |u| → 0 as |x| → ∞ (by the radiation condition).
3. Therefore, |u| attains its maximum on the compact set R³\D̄ ∪ {∞}... well, on ∂D ∪ (R³\D).

Wait, since |u| → 0 at infinity and |u| is continuous, the supremum is attained either on ∂D or at some point in R³\D. If it's attained on ∂D, we're done. If it's attained at an interior point, we need to show it can't exceed the boundary value.

For the Laplace equation, the maximum principle prevents interior maxima. For Helmholtz, it doesn't. So the question is whether the radiation condition provides an additional constraint that prevents interior maxima from exceeding boundary values.

I think the answer is YES, and the proof uses the following argument:

Consider the Fourier transform of u (in the distributional sense). The radiation condition implies that the Fourier transform of u is supported on the sphere |ξ| = k (the Ewald sphere). This means u is a superposition of plane waves e^{ik θ̂·x} with |θ̂| = 1:

u(x) = ∫_{S²} A(θ̂) e^{ik θ̂·x} dθ̂

Wait, this is the Herglotz representation, but it's for solutions in all of R³, not just the exterior. For the exterior problem, the solution is not entire; it has a singularity (or at least non-analyticity) inside D.

Hmm, but the solution IS analytic in the exterior R³\D. The Herglotz representation applies to entire solutions. For exterior solutions, we need a different representation.

Actually, the solution to the exterior problem can be written as:
u(x) = ∫_{∂D} [G(x,y) σ(y) - ∂G/∂n_y(x,y) μ(y)] dS(y)

using single and double layer potentials. This is not a superposition of plane waves.

OK, I think I've spent too long on this. Let me just go with C = 1 and provide a proof based on the key ideas.

Actually, wait. Let me reconsider the problem. Maybe the answer is NOT C = 1, and the problem is asking for a different kind of bound.

Let me think about what happens for the interior problem. For the interior Helmholtz problem (Δu + k²u = 0 in D, u = g on ∂D), the maximum principle does NOT hold, and in fact, the solution can be arbitrarily large when k² is close to an interior Dirichlet eigenvalue. So for the interior problem, no finite C exists (uniformly over k).

For the exterior problem, there are no eigenvalues (the exterior Dirichlet problem is always uniquely solvable for real k > 0), so C is finite for each k and D. But C could depend on k and D.

If the problem is asking for a universal C (over all k > 0 and all smooth bounded D), then... for the ball, C = 1 (as I showed). For general D, C might be larger. But is there a universal bound?

I think the answer is C = 1, and this is a known result. Let me try to find the right proof.

Actually, I just thought of a potential proof using the Green's function and the maximum principle for harmonic functions.

Proof:
Let u solve the exterior Helmholtz Dirichlet problem. Let M = sup_{∂D} |g|.

The free-space Green's function is G(x,y) = e^{ik|x-y|}/(4π|x-y|), with |G(x,y)| = Φ(x,y) := 1/(4π|x-y|).

The solution can be represented as (using the Green's representation formula for the exterior):
u(x) = ∫_{∂D} [G(x,y) ∂_n u(y) - ∂_n G(x,y) g(y)] dS(y)   ... (*)

where ∂_n is the outward normal to D (inward to the exterior region).

Now, define:
v(x) = ∫_{∂D} [Φ(x,y) |∂_n u(y)| + |∂_n Φ(x,y)| |g(y)|] dS(y)

Then |u(x)| ≤ v(x) by the triangle inequality and |G| = Φ.

Now, v is the sum of a single-layer potential and a double-layer potential for the LAPLACE equation, with non-negative densities. Both are harmonic in R³\D.

The single-layer potential S[|∂_n u|](x) = ∫ Φ(x,y) |∂_n u(y)| dS(y) is harmonic in R³\D and superharmonic everywhere (subharmonic? Let me think... Φ is harmonic away from the source, so S[σ] is harmonic in R³\D for σ on ∂D). It's continuous across ∂D.

The double-layer potential D[|g|](x) = ∫ ∂_n Φ(x,y) |g(y)| dS(y) is harmonic in R³\D. It has a jump across ∂D: the exterior limit is D[|g|]_+ = -1/2 |g| + K[|g|] and the interior limit is D[|g|]_- = 1/2 |g| + K[|g|] (where K is the double-layer operator).

Hmm, the signs depend on the convention. Let me be more careful.

For the exterior region (R³\D), the outward normal to the exterior region at ∂D is -n (where n is the outward normal to D). So the double layer potential with respect to the exterior is:
D_ext[|g|](x) = ∫_{∂D} ∂_{n_ext} Φ(x,y) |g(y)| dS(y) = -∫_{∂D} ∂_n Φ(x,y) |g(y)| dS(y)

where n is the outward normal to D. The jump relation for the exterior is:
D_ext[|g|]_ext = 1/2 |g| + K_ext[|g|]  (exterior limit)
D_ext[|g|]_int = -1/2 |g| + K_ext[|g|]  (interior limit)

This is getting complicated with the signs. Let me just focus on the key idea.

The function v is harmonic in R³\D and v ≥ |u| on ∂D (we need to verify this). If v ≥ |u| on ∂D and v ≥ |u| at infinity (both → 0, but v might not → 0...), then by the maximum principle for harmonic functions, v ≥ |u| in R³\D, giving |u| ≤ v ≤ sup_{∂D} v.

But we need sup_{∂D} v ≤ M, which requires controlling the boundary values of v in terms of M = sup|g|. The boundary values of v involve both |∂_n u| and |g|, and we don't have control over |∂_n u| in terms of |g| alone.

So this approach doesn't directly work. The issue is that the Green's representation involves both u and ∂_n u, and we can't bound ∂_n u in terms of u = g on the boundary.

Let me try a different representation. For the exterior Dirichlet problem, we can use the combined field integral equation or the Brakhage-Werner approach:

u(x) = ∫_{∂D} [∂G/∂n_y(x,y) - iη G(x,y)] μ(y) dS(y)

where η > 0 is a coupling parameter and μ solves the boundary integral equation:
(1/2 I + K - iη S) μ = g   on ∂D

Here K is the double-layer operator and S is the single-layer operator.

Then:
|u(x)| ≤
