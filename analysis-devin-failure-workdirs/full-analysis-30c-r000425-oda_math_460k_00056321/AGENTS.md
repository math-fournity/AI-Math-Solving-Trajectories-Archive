# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Determine the values of \(a \in \mathbb{R}\) for which the integral \(\int_{0}^{\frac{\pi}{2}} \log(\cos(x)) \cdot (\tan(x))^a \, dx\) converges.       — 题目文本
#   <think>Okay, let's try to figure out for which real numbers \( a \) the integral \( \int_{0}^{\frac{\pi}{2}} \log(\cos(x)) \cdot (\tan(x))^a \, dx \) converges. Hmm, first, I need to recall that when dealing with convergence of integrals, especially improper integrals, we need to check the behavior near the endpoints where the integrand might be problematic. Here, the interval is from \( 0 \) to \( \frac{\pi}{2} \), so let's check the limits as \( x \) approaches \( 0 \) and as \( x \) approaches \( \frac{\pi}{2} \).

First, let's analyze the integrand \( f(x) = \log(\cos(x)) \cdot (\tan(x))^a \). Let's rewrite \( (\tan(x))^a \) as \( \sin^a(x)/\cos^a(x) \), so \( f(x) = \log(\cos(x)) \cdot \frac{\sin^a(x)}{\cos^a(x)} \). But maybe it's better to look at the behavior near each endpoint.

Starting with \( x \to 0^+ \). Let's see what happens to \( \cos(x) \) and \( \tan(x) \) here. As \( x \to 0 \), \( \cos(x) \approx 1 - x^2/2 \), so \( \log(\cos(x)) \approx \log(1 - x^2/2) \approx -x^2/2 \) (using the Taylor expansion \( \log(1 - \epsilon) \approx -\epsilon \) for small \( \epsilon \)). Then \( \tan(x) \approx x \), so \( (\tan(x))^a \approx x^a \). Therefore, near \( x = 0 \), the integrand behaves like \( (-x^2/2) \cdot x^a = -x^{a + 2}/2 \). The integral of \( x^{a + 2} \) near 0 converges as long as the exponent is greater than -1, right? Because \( \int x^b dx \) converges near 0 if \( b > -1 \). Wait, but here the integrand is \( x^{a + 2} \), so the integral from 0 to some small \( \epsilon \) would be \( \int_0^\epsilon x^{a + 2} dx \), which converges if \( a + 2 > -1 \)? Wait, no. Wait, the integral \( \int_0^\epsilon x^b dx \) converges (i.e., the limit as \( t \to 0^+ \) of \( \int_t^\epsilon x^b dx \) exists) if \( b > -1 \). Because \( \int x^b dx = x^{b + 1}/(b + 1) \), so as \( t \to 0 \), if \( b + 1 > 0 \), i.e., \( b > -1 \), then the integral converges. So here, the leading term is \( x^{a + 2} \), so \( b = a + 2 \). So we need \( a + 2 > -1 \)? Wait, no, wait. Wait, the integrand is \( \log(\cos x) \tan^a x \approx -x^2 \cdot x^a = -x^{a + 2} \). So the integrand behaves like \( x^{a + 2} \) near 0. The integral of \( x^{a + 2} \) from 0 to \( \epsilon \) converges if \( a + 2 > -1 \)? Wait, no, the integral \( \int_0^\epsilon x^b dx \) converges (i.e., the integral is finite) when \( b > -1 \). Because if \( b \geq -1 \), then the integral is finite. Wait, if \( b = -1 \), then \( \int x^{-1} dx = \log x \), which diverges as \( x \to 0 \). If \( b < -1 \), then \( x^b \) tends to infinity as \( x \to 0 \), and the integral diverges. So for \( \int_0^\epsilon x^b dx \) to converge, we need \( b > -1 \). So here, the exponent is \( a + 2 \), so we need \( a + 2 > -1 \)? Wait, no, wait. Wait, the integrand is \( x^{a + 2} \), so \( b = a + 2 \). So to have \( \int_0^\epsilon x^b dx \) converge, we need \( b > -1 \), so \( a + 2 > -1 \implies a > -3 \). But wait, but the integrand here is \( \log(\cos x) \tan^a x \approx -x^{a + 2} \), but actually, the logarithm term is \( \log(\cos x) \approx -x^2/2 \), which is a negative term, but the sign doesn't affect convergence, only the magnitude. So near 0, the integrand is \( O(x^{a + 2}) \), so the integral near 0 converges if \( a + 2 > -1 \), i.e., \( a > -3 \). Wait, but let's confirm. Let's take \( a = -4 \), then \( a + 2 = -2 \), so the integrand behaves like \( x^{-2} \), and \( \int x^{-2} dx \) from 0 to \( \epsilon \) is \( [-x^{-1}]_0^\epsilon \), which diverges. If \( a = -3 \), then \( a + 2 = -1 \), integrand behaves like \( x^{-1} \), integral \( \int x^{-1} dx \) diverges. If \( a = -2.5 \), then \( a + 2 = -0.5 \), integral \( \int x^{-0.5} dx \) converges (since \( -0.5 > -1 \)). So yes, near 0, the condition is \( a > -3 \).

Now, let's check the other endpoint, \( x \to (\pi/2)^- \). Let's set \( t = \pi/2 - x \), so as \( x \to \pi/2^- \), \( t \to 0^+ \). Then \( \cos(x) = \cos(\pi/2 - t) = \sin(t) \approx t \), so \( \log(\cos(x)) = \log(\sin t) \approx \log t \). \( \tan(x) = \tan(\pi/2 - t) = \cot t = 1/\tan t \approx 1/t \), so \( (\tan x)^a = (\cot t)^a = t^{-a} \). Therefore, the integrand becomes \( \log(\sin t) \cdot t^{-a} \). But \( \sin t \approx t \), so \( \log(\sin t) \approx \log t \). So the integrand near \( t \to 0^+ \) (i.e., \( x \to \pi/2^- \)) is approximately \( \log t \cdot t^{-a} \). Let's write that as \( t^{-a} \log t \). Now, we need to analyze the integral of \( t^{-a} \log t \) as \( t \to 0^+ \). Let's consider the behavior of \( t^{-a} \log t \). Let's set \( u = t \), so as \( u \to 0^+ \), \( \log u \to -\infty \), but \( u^{-a} \) is \( u^{-a} \). Let's see: if \( a < 0 \), then \( -a > 0 \), so \( u^{-a} = u^{|a|} \), which tends to 0, but multiplied by \( \log u \), which tends to -infty. Wait, but let's think in terms of convergence. Let's consider the integral \( \int_{0}^{\epsilon} t^{-a} \log t \, dt \). Let's make substitution \( s = - \log t \), so \( t = e^{-s} \), \( dt = -e^{-s} ds \). When \( t \to 0 \), \( s \to \infty \); when \( t = \epsilon \), \( s = -\log \epsilon \). Then the integral becomes \( \int_{s = \infty}^{s = -\log \epsilon} e^{a s} (-\log e^{-s}) (-e^{-s} ds) \). Wait, maybe that's complicating. Alternatively, let's consider the integral \( \int t^b \log t dt \), where \( b = -a \). Let's compute \( \int t^b \log t dt \). Integration by parts: let \( u = \log t \), \( dv = t^b dt \). Then \( du = (1/t) dt \), \( v = t^{b + 1}/(b + 1) \). So \( \int t^b \log t dt = (t^{b + 1}/(b + 1)) \log t - \int t^{b + 1}/(b + 1) \cdot (1/t) dt = (t^{b + 1}/(b + 1)) \log t - (1/(b + 1)) \int t^b dt = (t^{b + 1}/(b + 1)) \log t - t^{b + 1}/(b + 1)^2 + C \). Now, as \( t \to 0^+ \), what's the behavior of this expression? Let's see:

If \( b + 1 > 0 \), i.e., \( b > -1 \), then \( t^{b + 1} \to 0 \). Then \( (t^{b + 1}/(b + 1)) \log t \): since \( t^{b + 1} \to 0 \) and \( \log t \to -\infty \), but \( t^{b + 1} \) goes to 0 faster than \( \log t \) goes to -infty if \( b + 1 > 0 \). Let's check: \( t^{b + 1} \log t = e^{(b + 1) \log t} \log t \). Let \( u = \log t \), so as \( t \to 0^+ \), \( u \to -\infty \), then it's \( e^{(b + 1) u} u \). If \( b + 1 > 0 \), then \( (b + 1) u \to -\infty \), so \( e^{(b + 1) u} \to 0 \), and multiplied by \( u \to -\infty \), but the exponential decay dominates, so the whole term tends to 0. Therefore, the first term tends to 0, and the second term \( - t^{b + 1}/(b + 1)^2 \to 0 \). So the integral converges.

If \( b + 1 = 0 \), i.e., \( b = -1 \), then \( t^{b + 1} = t^0 = 1 \), so the first term is \( (1/(0)) \log t \), but wait, \( b = -1 \), so \( b + 1 = 0 \), so the original integral becomes \( \int t^{-1} \log t dt \). Let's compute that: \( \int (\log t)/t dt = (\log t)^2 / 2 + C \). As \( t \to 0^+ \), \( (\log t)^2 \to \infty \), so the integral diverges.

If \( b + 1 < 0 \), i.e., \( b < -1 \), then \( t^{b + 1} \to \infty \) as \( t \to 0^+ \). Then \( (t^{b + 1}/(b + 1)) \log t \): \( t^{b + 1} \to \infty \), \( \log t \to -\infty \), so the product is \( \infty \times (-\infty) = -\infty \). The second term \( - t^{b + 1}/(b + 1)^2 \): \( t^{b + 1} \to \infty \), and \( (b + 1)^2 > 0 \), so this term is \( -\infty \). So the entire expression tends to \( -\infty \), so the integral diverges.

But in our case, \( b = -a \), so:

The integral \( \int t^{-a} \log t dt \) near \( t \to 0^+ \) converges if and only if \( b > -1 \), i.e., \( -a > -1 \implies a < 1 \).

Wait, let's confirm. Let's recap:

We have \( b = -a \). The integral \( \int t^b \log t dt \) converges as \( t \to 0^+ \) iff \( b > -1 \). So \( -a > -1 \implies a < 1 \).

But let's check with specific values. Let's take \( a = 2 \), so \( b = -2 \). Then \( b = -2 < -1 \), so the integral should diverge. The integrand is \( t^{-2} \log t \), which as \( t \to 0 \), \( t^{-2} \) is \( 1/t^2 \), and \( \log t \to -\infty \), so the integrand tends to \( -\infty \), and the integral \( \int t^{-2} \log t dt \) would diverge. If \( a = 0.5 \), then \( b = -0.5 \), which is \( > -1 \). Then the integrand is \( t^{-0.5} \log t \), which as \( t \to 0 \), \( t^{-0.5} = 1/\sqrt{t} \), and \( \log t \to -\infty \), but \( 1/\sqrt{t} \log t \). Let's see, does the integral converge? Let's compute \( \int t^{-0.5} \log t dt \). Using the earlier formula, \( b = -0.5 \), so \( b + 1 = 0.5 > 0 \). Then the integral is \( (t^{0.5}/0.5) \log t - t^{0.5}/(0.5)^2 + C = 2 \sqrt{t} \log t - 4 \sqrt{t} + C \). As \( t \to 0 \), \( \sqrt{t} \log t \to 0 \) (since \( \sqrt{t} \to 0 \) and \( \log t \to -\infty \), but \( \sqrt{t} \) goes to 0 faster), so the first term tends to 0, the second term tends to 0, so the integral converges. So yes, when \( a < 1 \), the integral near \( x = \pi/2 \) converges.

If \( a = 1 \), then \( b = -1 \), so the integral becomes \( \int t^{-1} \log t dt \), which we saw diverges (since \( (\log t)^2 / 2 \to \infty \) as \( t \to 0 \)). If \( a > 1 \), then \( b = -a < -1 \), so the integral diverges. So the condition near \( x = \pi/2 \) is \( a < 1 \).

Now, we need both conditions: near \( x = 0 \), we need \( a > -3 \), and near \( x = \pi/2 \), we need \( a < 1 \). But wait, we also need to check if there are any other singularities in the interval. The integrand is defined on \( (0, \pi/2) \), since \( \cos x > 0 \) there, and \( \tan x \) is positive, so \( (\tan x)^a \) is defined for real \( a \) as long as \( \tan x > 0 \), which it is in \( (0, \pi/2) \). So the only singularities are at the endpoints.

But wait, let's confirm the behavior near \( x = 0 \) again. Let's be more precise. Let's expand \( \log(\cos x) \) more accurately. \( \cos x = 1 - x^2/2 + x^4/24 - \dots \), so \( \log(\cos x) = \log(1 - x^2/2 + x^4/24 - \dots) \approx -x^2/2 - x^4/12 - \dots \) (using \( \log(1 - y) \approx -y - y^2/2 - \dots \) for small \( y \)). So \( \log(\cos x) \approx -x^2/2 \) for small \( x \). Then \( (\tan x)^a = (x + x^3/3 + \dots)^a \approx x^a (1 + a x^2/3 + \dots) \). So the product \( \log(\cos x) (\tan x)^a \approx (-x^2/2) x^a (1 + \dots) = -x^{a + 2}/2 (1 + \dots) \). So the leading term is indeed \( -x^{a + 2}/2 \), so the integrand behaves like \( x^{a + 2} \) near 0. Therefore, the integral near 0 is dominated by \( \int x^{a + 2} dx \), which converges if \( a + 2 > -1 \implies a > -3 \). That seems correct.

Now, near \( x = \pi/2 \), we did the substitution \( t = \pi/2 - x \), so \( x = \pi/2 - t \), \( dx = -dt \), and as \( x \to \pi/2^- \), \( t \to 0^+ \). Then \( \cos x = \sin t \approx t - t^3/6 + \dots \), so \( \log(\cos x) = \log(\sin t) \approx \log t + \log(1 - t^2/6 + \dots) \approx \log t - t^2/6 + \dots \). But the leading term is \( \log t \). \( \tan x = \tan(\pi/2 - t) = \cot t = 1/\tan t \approx 1/t - t/3 + \dots \), so \( (\tan x)^a \approx (1/t)^a (1 - a t^2/3 + \dots) \). Therefore, the integrand \( \log(\cos x) (\tan x)^a \approx (\log t) t^{-a} (1 + \dots) \). So the leading term is \( t^{-a} \log t \), which is what we considered earlier. Therefore, the integral near \( x = \pi/2 \) is dominated by \( \int t^{-a} \log t dt \), which converges if \( -a > -1 \implies a < 1 \), as before.

Now, we need to check if there are any other issues. For example, what if \( a \) is such that the integrand is not defined? But in \( (0, \pi/2) \), \( \cos x > 0 \), \( \tan x > 0 \), so \( (\tan x)^a \) is defined for any real \( a \) (since it's \( e^{a \ln \tan x} \)), and \( \log(\cos x) \) is defined (since \( \cos x > 0 \)), so the integrand is defined everywhere on \( (0, \pi/2) \). The only possible issues are at the endpoints, which we already checked.

Now, we need to ensure that both conditions are satisfied: \( a > -3 \) and \( a < 1 \). So the integral converges if and only if \( -3 < a < 1 \).

Wait, but let's check the endpoints of this interval. What if \( a = -3 \)? Then near \( x = 0 \), the integrand behaves like \( x^{-3 + 2} = x^{-1} \), so \( \int x^{-1} dx \) diverges. So \( a = -3 \) is excluded. What if \( a = 1 \)? Near \( x = \pi/2 \), the integrand behaves like \( t^{-1} \log t \), and the integral \( \int t^{-1} \log t dt \) diverges (as we saw earlier, it's \( (\log t)^2 / 2 \), which tends to infinity as \( t \to 0 \)). So \( a = 1 \) is also excluded.

Is there any other point where the integrand might cause divergence? For example, what if \( a \) is negative? Let's say \( a = -2 \), which is between -3 and 1. Then near 0, \( a + 2 = 0 \), so the integrand behaves like \( x^0 = 1 \), so the integral near 0 is \( \int 1 dx \), which converges. Near \( \pi/2 \), \( a = -2 < 1 \), so \( -a = 2 > -1 \), so the integral near \( \pi/2 \) converges. So that's okay.

Another example: \( a = 0 \). Then the integrand is \( \log(\cos x) \), and the integral is \( \int_0^{\pi/2} \log(\cos x) dx \), which is a known integral (it's equal to \( -\pi/2 \log 2 \)), so it converges. That's within our interval.

What if \( a = -4 \), which is less than -3? Then near 0, \( a + 2 = -2 \), so the integrand behaves like \( x^{-2} \), integral diverges. So indeed, \( a < -3 \) is bad.

What if \( a = 2 \), which is greater than 1? Near \( \pi/2 \), \( a = 2 \), so \( -a = -2 < -1 \), integral diverges. So that's bad.

Therefore, combining both conditions, the integral converges if and only if \( -3 < a < 1 \).
</think>

To determine the values of \( a \in \mathbb{R} \) for which the integral \( \int_{0}^{\frac{\pi}{2}} \log(\cos(x)) \cdot (\tan(x))^a \, dx \) converges, we analyze the behavior of the integrand near the endpoints \( x = 0 \) and \( x = \frac{\pi}{2} \).

### Behavior near \( x \to 0^+ \):
As \( x \to 0 \), we use the approximations \( \cos(x) \approx 1 - \frac{x^2}{2} \) and \( \tan(x) \approx x \). Thus:
- \( \log(\cos(x)) \approx \log\left(1 - \frac{x^2}{2}\right) \approx -\frac{x^2}{2} \)
- \( (\tan(x))^a \approx x^a \)

The integrand behaves like \( -\frac{x^2}{2} \cdot x^a = -\frac{x^{a+2}}{2} \). The integral of \( x^{a+2} \) near \( 0 \) converges if the exponent \( a+2 > -1 \), i.e., \( a > -3 \).

### Behavior near \( x \to \frac{\pi}{2}^- \):
Let \( t = \frac{\pi}{2} - x \), so \( t \to 0^+ \) as \( x \to \frac{\pi}{2}^- \). Then:
- \( \cos(x) = \sin(t) \approx t \), so \( \log(\cos(x)) \approx \log(t) \)
- \( \tan(x) = \cot(t) \approx \frac{1}{t} \), so \( (\tan(x))^a \approx t^{-a} \)

The integrand behaves like \( \log(t) \cdot t^{-a} \). The integral of \( t^{-a} \log(t) \) near \( t \to 0^+ \) converges if \( -a > -1 \), i.e., \( a < 1 \).

### Combining Conditions:
The integral converges if both conditions are satisfied: \( a > -3 \) and \( a < 1 \).

Thus, the values of \( a \) for which the integral converges are \( -3 < a < 1 \).

\[
\boxed{(-3, 1)}
\]  — 标准解答
#   Let me analyze this problem. It's about drawing Riemann surface schemes for several multi-valued functions. Let me think about each one carefully.

The problem asks to draw the schemes (topological structure) of Riemann surfaces for:
a) √z + √(z-1)
b) ³√(z²-1) + √(1/z)
c) √z + ³√z
d) ⁴√(z²-1) + ⁴√(z-1)

For Riemann surfaces, I need to identify:
1. Branch points
2. Branch orders at each branch point
3. How sheets connect (the gluing/branching structure)
4. The total number of sheets
5. The genus (if relevant)

Let me work through each.

**Part a) √z + √(z-1)**

This is a sum of two square root functions. Let me think about this carefully.

w = √z + √(z-1)

The branch points of √z are at z=0 and z=∞.
The branch points of √(z-1) are at z=1 and z=∞.

So the combined function has branch points at z=0, z=1, and z=∞.

Now, the key question is whether the branch at ∞ is a true branch point of the combined function or whether it cancels.

Let me think about this more carefully. The function w = √z + √(z-1) is a multi-valued function. Let's think about what happens when we analytically continue around each branch point.

√z has 2 sheets, branching at 0 and ∞.
√(z-1) has 2 sheets, branching at 1 and ∞.

If these were independent, we'd have up to 4 sheets. But the function w = √z + √(z-1) might have fewer sheets due to algebraic relations.

Let me compute w²:
w² = z + (z-1) + 2√(z(z-1)) = 2z - 1 + 2√(z(z-1))

So (w² - 2z + 1)² = 4z(z-1) = 4z² - 4z

w⁴ - 2(2z-1)w² + (2z-1)² = 4z² - 4z
w⁴ - (4z-2)w² + (4z²-4z+1) = 4z² - 4z
w⁴ - (4z-2)w² + 1 = 0

So w satisfies the equation w⁴ - (4z-2)w² + 1 = 0.

This is a degree 4 polynomial in w, so generically there are 4 values of w for each z. So the Riemann surface has 4 sheets.

The branch points: from the equation w⁴ - (4z-2)w² + 1 = 0, the discriminant with respect to w tells us where sheets coalesce.

Let u = w², then u² - (4z-2)u + 1 = 0, so u = [(4z-2) ± √((4z-2)² - 4)] / 2.

The discriminant is (4z-2)² - 4 = 16z² - 16z + 4 - 4 = 16z² - 16z = 16z(z-1).

So u = [(4z-2) ± 4√(z(z-1))] / 2 = (2z-1) ± 2√(z(z-1)).

Then w = ±√u, so w = ±√((2z-1) ± 2√(z(z-1))).

The branch points of the Riemann surface are where the discriminant vanishes: z(z-1) = 0, i.e., z = 0 and z = 1. Also we need to check z = ∞ and where u = 0 (which would make w = 0 a branch point of the square root).

u = 0 when (2z-1) ± 2√(z(z-1)) = 0, i.e., (2z-1) = ∓2√(z(z-1)), so (2z-1)² = 4z(z-1), which gives 4z²-4z+1 = 4z²-4z, i.e., 1 = 0. This is impossible, so u never equals 0. Good, so no additional branch points from the square root of u.

Now let's check the branch at ∞. As z → ∞:
√z ≈ √z, √(z-1) ≈ √z(1 - 1/(2z) + ...) = √z - 1/(2√z) + ...

So w = √z + √(z-1) ≈ 2√z - 1/(2√z) + ... or w = √z - √(z-1) ≈ 1/(2√z) + ... (depending on sign choices).

Actually, let me be more careful. The four values of w are:
w₁ = √z + √(z-1) (both positive branches)
w₂ = √z - √(z-1) (positive √z, negative √(z-1))
w₃ = -√z + √(z-1) = -w₂
w₄ = -√z - √(z-1) = -w₁

As z → ∞:
w₁ ≈ 2√z → ∞
w₂ ≈ 1/(2√z) → 0
w₃ ≈ -1/(2√z) → 0
w₄ ≈ -2√z → -∞

Now, going around ∞ (which is the same as going around 0 and 1 in the opposite direction, or equivalently, a large loop encircling both 0 and 1):

Going around a large circle enclosing both 0 and 1: √z picks up a factor of -1 (since we go around 0 once), and √(z-1) also picks up a factor of -1 (since we go around 1 once).

So w₁ = √z + √(z-1) → -√z - √(z-1) = w₄
w₂ = √z - √(z-1) → -√z + √(z-1) = w₃
w₃ → w₂
w₄ → w₁

So going around ∞ swaps (w₁, w₄) and (w₂, w₃). This means ∞ IS a branch point, with two transpositions. The monodromy at ∞ is the product of two transpositions: (w₁ w₄)(w₂ w₃).

Now let's check the monodromy at z = 0:
Going around z = 0 (small loop): √z picks up factor -1, √(z-1) is unchanged (since 0 is not a branch point of √(z-1), and for z near 0, z-1 ≈ -1, which is away from the branch point at 1).

w₁ = √z + √(z-1) → -√z + √(z-1) = w₃
w₂ = √z - √(z-1) → -√z - √(z-1) = w₄
w₃ → w₁
w₄ → w₂

So monodromy at 0: (w₁ w₃)(w₂ w₄).

Monodromy at z = 1:
Going around z = 1: √(z-1) picks up factor -1, √z unchanged.

w₁ → √z - √(z-1) = w₂
w₂ → √z + √(z-1) = w₁
w₃ → -√z - √(z-1) = w₄
w₄ → -√z + √(z-1) = w₃

So monodromy at 1: (w₁ w₂)(w₃ w₄).

Let's verify: the product of monodromies at 0, 1, ∞ should be identity.
0: (w₁ w₃)(w₂ w₄)
1: (w₁ w₂)(w₃ w₄)
∞: (w₁ w₄)(w₂ w₃)

Product: Let's compute. Start with w₁.
After ∞: w₁ → w₄
After 1: w₄ → w₃
After 0: w₃ → w₁
So w₁ → w₁. ✓

Start with w₂:
After ∞: w₂ → w₃
After 1: w₃ → w₄
After 0: w₄ → w₂
So w₂ → w₂. ✓

Good, the product is identity.

So the Riemann surface of part (a) has:
- 4 sheets
- 3 branch points: z = 0, z = 1, z = ∞
- Each branch point has branch order 2 (simple branch point, connecting 2 pairs of sheets)
- Monodromy at 0: (1 3)(2 4)
- Monodromy at 1: (1 2)(3 4)
- Monodromy at ∞: (1 4)(2 3)

The genus: Using Riemann-Hurwitz. The covering has degree 4, base genus 0. Each branch point contributes 2 to the ramification (since each has two simple branch points, each contributing 1 to the Riemann-Hurwitz sum per sheet... wait, let me be more careful).

Actually, each branch point here has two transpositions, meaning two pairs of sheets are swapped. Each transposition corresponds to a simple ramification point (ramification index 2 for one point, contributing e-1 = 1 to the sum). With two transpositions at each branch point, each branch point contributes 2 to the total ramification sum.

Total ramification = 3 × 2 = 6.

Riemann-Hurwitz: 2g - 2 = n(2·0 - 2) + R = 4(-2) + 6 = -8 + 6 = -2.
So 2g = 0, g = 0.

The Riemann surface is a sphere (genus 0), with 4 sheets and 3 branch points, each connecting 2 pairs of sheets.

**Scheme description for (a):**
- 4 sheets labeled 1, 2, 3, 4
- Branch cut from 0 to 1: connects sheets (1,2) and (3,4) [based on monodromy at 0 and 1... actually, the branch cut structure depends on how we choose cuts]

Actually, let me think about the scheme more carefully in terms of branch cuts.

The standard way to describe the scheme: we choose branch cuts and describe how sheets are connected across them.

Let me choose branch cuts from 0 to 1, and from 1 to ∞ (or equivalently, from 0 to ∞ passing through 1, but that's not standard). Actually, let me choose:
- Cut 1: from 0 to 1
- Cut 2: from 1 to ∞ (i.e., from 1 along the positive real axis to +∞, or just a cut from 1 to ∞)

Hmm, actually, the standard approach for these problems is to describe the branch cuts and how sheets are glued.

Let me reconsider. The branch points are at 0, 1, ∞. We need to connect them with branch cuts. One natural choice:
- Cut A: from 0 to 1
- Cut B: from 1 to ∞

Across cut A (from 0 to 1): Going around 0 gives (1 3)(2 4), going around 1 gives (1 2)(3 4). The cut from 0 to 1 separates these. When we cross the cut from 0 to 1, the monodromy is the product of going around 0 (or equivalently, the monodromy associated with the cut).

Hmm, I think I'm overcomplicating this. Let me think about it differently.

Actually, for a cut from 0 to 1, crossing this cut corresponds to the monodromy of going around either 0 or 1 (they're on opposite sides). The monodromy of a loop around the cut [0,1] is the product of monodromies at 0 and 1... no, that's not right either.

Let me think again. If we have branch cuts from 0 to 1 and from 1 to ∞, then:
- Crossing the cut [0,1] corresponds to the monodromy of a loop that goes around 0 (but not 1) — this is (1 3)(2 4). Wait, no. If the cut goes from 0 to 1, then crossing it means going from one side to the other, which is equivalent to going around either 0 or 1 (depending on which part of the cut you cross).

Actually, the standard picture: if we have a cut from 0 to 1, then a loop crossing this cut and coming back on the other side is equivalent to going around either 0 or 1. The monodromy of crossing the cut [0,1] is the same as the monodromy at 0 (or equivalently at 1, since going around both 0 and 1 gives the monodromy at ∞, which is different).

Hmm, I think the cleanest way is:

For the cut from 0 to 1: a path that crosses this cut once and returns corresponds to going around 0 (if it crosses near 0) or around 1 (if it crosses near 1). But for a straight cut, crossing it anywhere gives the same monodromy, which is the monodromy of a loop around 0 (equivalently, around 1, since the cut connects them and the monodromy of going around the cut as a whole is the monodromy at ∞).

Wait, I need to be more careful. Let me think about this properly.

If we have cuts [0,1] and [1,∞], then the complement of these cuts in the sphere is simply connected. On this simply connected region, we can define single-valued branches. The monodromy when crossing a cut tells us how sheets are glued.

Crossing the cut [0,1]: This is equivalent to going around 0 (and not around ∞), or equivalently going around 1 (and not around ∞). But going around 0 gives monodromy (1 3)(2 4), and going around 1 gives (1 2)(3 4). These are different! So the cut [0,1] can't have a single monodromy...

Oh, I see the issue. The cut [0,1] connects two branch points with different monodromies. So crossing different parts of the cut gives different monodromies. This means we can't have a single cut from 0 to 1 with a uniform gluing.

The correct approach: we need separate cuts. Let me use:
- Cut from 0 to ∞ (not passing through 1)
- Cut from 1 to ∞ (not passing through 0)

Or more standardly:
- Cut from 0 to 1
- Cut from 1 to ∞

But the issue is that at z=1, both cuts meet, and the monodromy at 1 is (1 2)(3 4).

Actually, I think the standard way to handle this is: the cut from 0 to 1 carries the monodromy of going around 0 (which equals the monodromy of going around 1 times the monodromy of going around ∞, by the relation that the product of all monodromies is identity). No wait, the product of monodromies at 0, 1, ∞ is identity, so monodromy at 0 = (monodromy at 1)⁻¹ × (monodromy at ∞)⁻¹... no, monodromy at 0 × monodromy at 1 × monodromy at ∞ = identity.

So monodromy at 0 = (monodromy at 1 × monodromy at ∞)⁻¹ = (monodromy at ∞)⁻¹ × (monodromy at 1)⁻¹.

Since all our monodromies are involutions (products of disjoint transpositions), they're their own inverses.

monodromy at 0 = (1 3)(2 4) = (1 4)(2 3) × (1 2)(3 4) = monodromy at ∞ × monodromy at 1.

Let me verify: (1 4)(2 3) × (1 2)(3 4).
1 → (1 2) → 2 → (2 3) → 3. So 1 → 3.
3 → (3 4) → 4 → (1 4) → 1. So 3 → 1. Good, (1 3) ✓
2 → (1 2) → 1 → (1 4) → 4. So 2 → 4.
4 → (3 4) → 3 → (2 3) → 2. So 4 → 2. Good, (2 4) ✓

Great, so monodromy at 0 = monodromy at ∞ × monodromy at 1. This is consistent.

Now, for the scheme: we choose cuts and describe the gluing.

**Standard approach for the scheme:**

Let me use cuts [0,1] and [1,∞].

For the cut [0,1]: A loop going around this cut (encircling both 0 and 1 but not ∞) has monodromy = (monodromy at 0) × (monodromy at 1) = (1 3)(2 4) × (1 2)(3 4).

Let me compute: (1 3)(2 4) × (1 2)(3 4) (applying right to left):
1 → (1 2) → 2 → (2 4) → 4. So 1 → 4.
4 → (3 4) → 3 → (1 3) → 1. So 4 → 1. Good, (1 4).
2 → (1 2) → 1 → (1 3) → 3. So 2 → 3.
3 → (3 4) → 4 → (2 4) → 2. So 3 → 2. Good, (2 3).

So monodromy around the cut [0,1] = (1 4)(2 3) = monodromy at ∞. This makes sense! A loop around the cut [0,1] is the same as a loop around ∞ (in the opposite direction, but since these are involutions, direction doesn't matter).

So crossing the cut [0,1] gives monodromy (1 4)(2 3).
Crossing the cut [1,∞] gives monodromy at 1 = (1 2)(3 4).

Wait, but that's not quite right. Let me reconsider.

If we have cuts [0,1] and [1,∞], then:
- A loop around the cut [0,1] (encircling 0 and 1) gives monodromy = monodromy(0) × monodromy(1) = (1 4)(2 3).
- A loop around the cut [1,∞] (encircling 1 and ∞) gives monodromy = monodromy(1) × monodromy(∞) = (1 2)(3 4) × (1 4)(2 3).

Let me compute (1 2)(3 4) × (1 4)(2 3):
1 → (1 4) → 4 → (3 4) → 3. So 1 → 3.
3 → (2 3) → 2 → (1 2) → 1. So 3 → 1. Good, (1 3).
2 → (2 3) → 3 → (3 4) → 4. So 2 → 4.
4 → (1 4) → 1 → (1 2) → 2. So 4 → 2. Good, (2 4).

So monodromy around [1,∞] = (1 3)(2 4) = monodromy at 0. Makes sense.

But actually, I think the standard way to describe the scheme is not in terms of "loops around cuts" but in terms of how sheets are glued across each cut.

When we cross a cut, we move from one sheet to another. The gluing across a cut is determined by the monodromy of a path that crosses the cut once.

For the cut [0,1]: crossing it corresponds to going around 0 (or equivalently around 1, but these give different monodromies...). 

Hmm, I think the issue is that a cut from 0 to 1 doesn't have a well-defined single monodromy because 0 and 1 have different monodromies. The correct interpretation is:

If we cross the cut [0,1] near 0, we get monodromy at 0 = (1 3)(2 4).
If we cross the cut [0,1] near 1, we get monodromy at 1 = (1 2)(3 4).

But for a straight-line cut, the monodromy should be constant along the cut (for a simple branch point). The issue here is that each branch point has TWO transpositions, not one. So each branch point is actually a "double branch point" — it connects two pairs of sheets.

I think the correct picture is:

At z = 0: sheets 1↔3 and 2↔4 are connected (two branch points at z=0, each connecting one pair).
At z = 1: sheets 1↔2 and 3↔4 are connected.
At z = ∞: sheets 1↔4 and 2↔3 are connected.

For the scheme, we can describe it as follows:

Choose cuts [0,1] and [1,∞] (on the real axis).

Actually, I think for these problems, the standard approach in Russian textbooks (this looks like it's from a Russian textbook, probably Shabat or similar) is to describe the branch cuts and sheet connections.

Let me reconsider the problem. The "scheme" of a Riemann surface typically means:
1. The number of sheets
2. The branch points and their orders
3. How the sheets are connected (the branch cut structure)

Let me describe each part.

**Part a) √z + √(z-1)**

As computed: 4 sheets, branch points at 0, 1, ∞, each of order 2 (connecting 2 pairs of sheets).

The monodromy group is generated by:
- σ₀ = (1 3)(2 4) at z = 0
- σ₁ = (1 2)(3 4) at z = 1
- σ∞ = (1 4)(2 3) at z = ∞

The scheme: We can draw cuts from 0 to 1 and from 1 to ∞. 

Across the cut [0,1]: sheets are connected as 1↔3, 2↔4 (monodromy at 0) — wait, but crossing [0,1] should give a single monodromy. 

I think the issue is that with two transpositions at each branch point, we need to think of each branch point as two simple branch points. So at z=0, there are two branch points (one connecting 1↔3, one connecting 2↔4), both at z=0.

For the scheme, we can separate these. Let me choose:
- Cut from 0 to 1 for the pair (1,2)↔(3,4): i.e., at z=0, sheets 1↔3 and 2↔4 are connected; at z=1, sheets 1↔2 and 3↔4 are connected.

Actually, I think the standard way to describe this is:

The Riemann surface has 4 sheets. We make cuts [0,1] and [1,∞]. 

Across cut [0,1]: the connection is determined by the monodromy at 0 (going around 0). When we cross [0,1] (going around 0), sheets 1↔3 and 2↔4 swap.

Across cut [1,∞]: the connection is determined by the monodromy at 1 (going around 1). When we cross [1,∞] (going around 1), sheets 1↔2 and 3↔4 swap.

Wait, I need to think about this more carefully. If we have cuts [0,1] and [1,∞], then:
- Crossing [0,1] means going around 0 (but not 1 or ∞), which gives monodromy at 0.
- Crossing [1,∞] means going around 1 (but not 0 or ∞)... no, going around 1 and ∞.

Hmm, actually with cuts [0,1] and [1,∞], the point 1 is where the two cuts meet. A loop crossing [0,1] goes around 0 (and not 1 or ∞). A loop crossing [1,∞] goes around 1 and ∞ (and not 0). But monodromy(1) × monodromy(∞) = monodromy(0)⁻¹ = monodromy(0) (since it's an involution).

Hmm, this doesn't seem right. Let me think about it differently.

With cuts [0,1] and [1,∞] (both on the positive real axis, say), the complement is simply connected. On this region, we have 4 single-valued branches. Crossing a cut moves us to a different branch.

Crossing [0,1] from above to below: this is equivalent to going around 0 (a small loop around 0 crosses [0,1] twice, but going from above to below across [0,1] near 0 is half of such a loop). The monodromy is that of going around 0, which is (1 3)(2 4).

But wait, crossing [0,1] near 1 gives the monodromy of going around 1, which is (1 2)(3 4). So the monodromy is NOT constant along the cut [0,1]!

This means we can't use a single cut [0,1] with uniform gluing. We need to separate the branch points.

I think the correct approach is to use cuts that go from each finite branch point to ∞, or to use a different cut configuration.

Let me use cuts from 0 to ∞ and from 1 to ∞, not passing through each other. For example:
- Cut A: from 0 to ∞ along the negative real axis
- Cut B: from 1 to ∞ along the positive real axis

Then:
- Crossing cut A (from 0 to ∞) corresponds to going around 0, giving monodromy (1 3)(2 4).
- Crossing cut B (from 1 to ∞) corresponds to going around 1, giving monodromy (1 2)(3 4).

But each cut has two transpositions, meaning two pairs of sheets are swapped. This is fine — it just means the cut connects two pairs of sheets simultaneously.

So the scheme for (a):
- 4 sheets
- Cut from 0 to ∞: connects sheets 1↔3 and 2↔4
- Cut from 1 to ∞: connects sheets 1↔2 and 3↔4

At ∞, both cuts meet, and the combined monodromy is (1 3)(2 4) × (1 2)(3 4) = (1 4)(2 3), which is the monodromy at ∞. ✓

Actually, I realize I should think about this differently. In the standard treatment (e.g., in Shabat's book), the "scheme" of a Riemann surface is described by:
1. The number of sheets
2. The branch points
3. The branch cuts and how sheets are connected across them

For a function like √z + √(z-1), the standard approach would be:

Since w⁴ - (4z-2)w² + 1 = 0, this is a 4-sheeted surface. The branch points are at z = 0, 1, ∞, each with two simple branch points (order 2 each).

The scheme can be described as follows:
- 4 sheets
- Branch cuts: [0, ∞) and [1, ∞) (or [0,1] and [1,∞], etc.)
- At z = 0: sheets 1↔3 and 2↔4 are connected
- At z = 1: sheets 1↔2 and 3↔4 are connected
- At z = ∞: sheets 1↔4 and 2↔3 are connected

Genus 0.

OK let me now move on to the other parts and then write up the complete solution.

**Part b) ³√(z²-1) + √(1/z)**

w = ³√(z²-1) + √(1/z) = ³√(z²-1) + z^{-1/2}

Let me identify the branch points.

³√(z²-1) = ³√((z-1)(z+1)): branch points at z = 1, z = -1, and z = ∞.
- At z = 1: z²-1 has a simple zero, so ³√(z²-1) has a branch point of order 3.
- At z = -1: same, branch point of order 3.
- At z = ∞: z²-1 ~ z², so ³√(z²-1) ~ ³√(z²) = z^{2/3}. Going around ∞, z → ze^{2πi}, so z^{2/3} → z^{2/3} e^{4πi/3}. This is a non-trivial monodromy, so ∞ is a branch point of order 3.

√(1/z) = z^{-1/2}: branch points at z = 0 and z = ∞.
- At z = 0: branch point of order 2.
- At z = ∞: z^{-1/2} → (ze^{2πi})^{-1/2} = z^{-1/2} e^{-πi} = -z^{-1/2}. So ∞ is a branch point of order 2.

Now, the combined function w = ³√(z²-1) + z^{-1/2}.

The branch points are at z = -1, 0, 1, ∞.

Let me figure out the number of sheets. ³√(z²-1) has 3 values, z^{-1/2} has 2 values. If independent, 6 sheets. But they might not be independent.

Let me check: is there an algebraic relation that reduces the number of sheets?

Let u = ³√(z²-1), v = z^{-1/2}. Then w = u + v.
u³ = z² - 1, v² = 1/z, so z = 1/v², and u³ = 1/v⁴ - 1 = (1 - v⁴)/v⁴.

So u³v⁴ = 1 - v⁴, i.e., u³v⁴ + v⁴ = 1, v⁴(u³ + 1) = 1.

Also w = u + v, so u = w - v.
(w-v)³ v⁴ + v⁴ = 1
v⁴((w-v)³ + 1) = 1

This is a polynomial relation between w and v (and z = 1/v²). The degree in w is 3 (from (w-v)³), and the degree in v is... let me expand:
(w-v)³ = w³ - 3w²v + 3wv² - v³
So v⁴(w³ - 3w²v + 3wv² - v³ + 1) = 1
w³v⁴ - 3w²v⁵ + 3wv⁶ - v⁷ + v⁴ - 1 = 0

This is degree 3 in w and degree 7 in v. But we also have z = 1/v², so v = ±1/√z.

The number of sheets is the number of values of w for generic z. For generic z, u has 3 values and v has 2 values, giving 6 values of w = u + v. Are any of these equal? For generic z, u₁ + v₁ = u₂ + v₂ would require u₁ - u₂ = v₂ - v₁. Since u takes 3 values that are related by multiplication by cube roots of unity, and v takes 2 values that are negatives of each other, the differences u₁ - u₂ are generally not equal to ±(v₁ - v₂) for generic z. So we have 6 sheets.

Now let me determine the monodromy at each branch point.

Label the 6 sheets as (i, j) where i = 0, 1, 2 (for the 3 values of u = ³√(z²-1)) and j = 0, 1 (for the 2 values of v = z^{-1/2}).

The values are:
u_i = ωⁱ · u₀ where ω = e^{2πi/3}
v_j = (-1)^j · v₀

Sheet (i,j) corresponds to w = u_i + v_j = ωⁱ u₀ + (-1)^j v₀.

**Monodromy at z = 1:**
Going around z = 1: z²-1 = (z-1)(z+1) → (z-1) picks up e^{2πi}, so z²-1 → z²-1 (unchanged as a function, but the cube root...).

Wait, let me be more careful. Near z = 1, z²-1 ≈ 2(z-1). Going around z = 1, (z-1) → (z-1)e^{2πi}, so z²-1 → z²-1 · e^{2πi} = z²-1. But ³√(z²-1) → ³√(z²-1) · e^{2πi/3}. So u → u · ω, meaning u₀ → u₁ → u₂ → u₀.

Meanwhile, v = z^{-1/2} is unchanged (z = 1 is not a branch point of v, and near z = 1, z is away from 0).

So the monodromy at z = 1 is: (i, j) → (i+1 mod 3, j). This is a 3-cycle on the u-index: (0→1→2→0) for each j.

In terms of the 6 sheets (0,0), (1,0), (2,0), (0,1), (1,1), (2,1):
σ₁ = ((0,0) (1,0) (2,0)) ((0,1) (1,1) (2,1))

This is two 3-cycles. Each 3-cycle corresponds to a branch point of order 3.

**Monodromy at z = -1:**
Similarly, near z = -1, z²-1 ≈ -2(z+1). Going around z = -1, (z+1) → (z+1)e^{2πi}, so z²-1 → z²-1 · e^{2πi} = z²-1. And ³√(z²-1) → ³√(z²-1) · e^{2πi/3}.

Wait, that's the same as at z = 1. Let me double-check.

z²-1 = (z-1)(z+1). Near z = -1, z-1 ≈ -2 (constant), z+1 ≈ 0. So z²-1 ≈ -2(z+1). Going around z = -1: z+1 → (z+1)e^{2πi}, so z²-1 → -2(z+1)e^{2πi} = z²-1 · e^{2πi}. So ³√(z²-1) → ³√(z²-1) · e^{2πi/3}.

v = z^{-1/2} is unchanged near z = -1 (z ≈ -1, away from 0).

So monodromy at z = -1 is the same as at z = 1: (i, j) → (i+1 mod 3, j).

Hmm, but that would mean the product of monodromies at -1 and 1 is (i → i+2 mod 3, j → j), which is also a 3-cycle (the inverse). And then the monodromy at 0 and ∞ together must give (i → i+1 mod 3, j → j) to make the total product identity.

Wait, let me reconsider. The product of ALL monodromies must be identity. The branch points are -1, 0, 1, ∞.

σ_{-1} = (i → i+1, j → j) [3-cycle on u]
σ₀ = (i → i, j → j+1 mod 2) [2-cycle on v, since going around 0: z → ze^{2πi}, z^{-1/2} → z^{-1/2}e^{-πi} = -z^{-1/2}, so v → -v, meaning j → j+1 mod 2. And u = ³√(z²-1) is unchanged since z²-1 is unchanged when z → ze^{2πi}... wait, z² → z²e^{4πi} = z², so z²-1 → z²-1. So u is unchanged.]

σ₁ = (i → i+1, j → j) [3-cycle on u]
σ∞ = ?

Product must be identity: σ_{-1} · σ₀ · σ₁ · σ∞ = id.

σ_{-1} · σ₁ = (i → i+2, j → j) [since each adds 1 to i]
σ_{-1} · σ₀ · σ₁ = (i → i+2, j → j+1)

So σ∞ = (i → i+1, j → j+1) [to make the product identity: (i+2+1, j+1+1) = (i, j) ✓ since i+3 ≡ i mod 3 and j+2 ≡ j mod 2]

Let me verify σ∞ directly. At z = ∞, going around ∞ means z → ze^{-2πi} (or equivalently, a large loop clockwise). Let's use z → ze^{2πi} (counterclockwise around 0, which is clockwise around ∞ on the sphere).

u = ³√(z²-1) ~ ³√(z²) = z^{2/3}. z → ze^{2πi}, so z^{2/3} → z^{2/3} e^{4πi/3} = u · ω². So i → i+2 mod 3.

v = z^{-1/2}. z → ze^{2πi}, so z^{-1/2} → z^{-1/2} e^{-πi} = -v. So j → j+1 mod 2.

So σ∞ = (i → i+2, j → j+1).

But I computed σ∞ = (i → i+1, j → j+1) from the product condition. Let me recheck.

The product of monodromies around all branch points (in order around the sphere) must be identity. The order matters. Let me be more careful.

On the Riemann sphere, if we list the branch points in order (say counterclockwise), the product of monodromies (in the right order) is identity. But the order and direction matter.

Let me just directly compute all monodromies and verify.

σ_{-1}: z → z (loop around -1), u → u·ω (i → i+1), v → v (j → j). So σ_{-1} = (i+1, j).
σ₀: z → ze^{2πi} (loop around 0), u → u (i → i, since z²-1 → z²-1), v → -v (j → j+1). So σ₀ = (i, j+1).
σ₁: z → z (loop around 1), u → u·ω (i → i+1), v → v (j → j). So σ₁ = (i+1, j).
σ∞: z → ze^{2πi} (loop around ∞ = loop around 0, but we need to be careful about direction).

Actually, a loop around ∞ counterclockwise (on the sphere) corresponds to a loop around 0 clockwise (in the plane), i.e., z → ze^{-2πi}.

With z → ze^{-2πi}:
u ~ z^{2/3} → z^{2/3} e^{-4πi/3} = u · ω (since e^{-4πi/3} = e^{2πi/3} = ω). So i → i+1.
v = z^{-1/2} → z^{-1/2} e^{πi} = -v. So j → j+1.

So σ∞ = (i+1, j+1).

Now the product: σ_{-1} · σ₀ · σ₁ · σ∞ = (i+1, j) · (i, j+1) · (i+1, j) · (i+1, j+1).

Applying right to left:
Start: (i, j)
After σ∞: (i+1, j+1)
After σ₁: (i+2, j+1)
After σ₀: (i+2, j+2) = (i+2, j) [since j+2 ≡ j mod 2]
After σ_{-1}: (i+3, j) = (i, j) ✓

Great, the product is identity.

So the monodromies are:
- σ_{-1} = (i → i+1, j → j): two 3-cycles
- σ₀ = (i → i, j → j+1): three 2-cycles
- σ₁ = (i → i+1, j → j): two 3-cycles
- σ∞ = (i → i+1, j → j+1): one 6-cycle

Let me verify σ∞ is a 6-cycle. The permutation (i → i+1 mod 3, j → j+1 mod 2) on 6 elements:
(0,0) → (1,1) → (2,0) → (0,1) → (1,0) → (2,1) → (0,0). Yes, it's a single 6-cycle!

So the Riemann surface for (b) has:
- 6 sheets
- Branch points at z = -1, 0, 1, ∞
- At z = -1: two 3-cycles (branch order 3, two branch points)
- At z = 0: three 2-cycles (branch order 2, three branch points)
- At z = 1: two 3-cycles (branch order 3, two branch points)
- At z = ∞: one 6-cycle (branch order 6, one branch point)

Genus by Riemann-Hurwitz:
2g - 2 = 6(-2) + R
R = sum of (e_p - 1) over all ramification points.

At z = -1: two 3-cycles, each contributes (3-1) = 2, total 4.
At z = 0: three 2-cycles, each contributes (2-1) = 1, total 3.
At z = 1: two 3-cycles, each contributes (3-1) = 2, total 4.
At z = ∞: one 6-cycle, contributes (6-1) = 5, total 5.

R = 4 + 3 + 4 + 5 = 16.
2g - 2 = -12 + 16 = 4.
2g = 6, g = 3.

So the Riemann surface has genus 3.

**Scheme for (b):**
- 6 sheets, labeled (i, j) with i = 0,1,2 and j = 0,1
- Branch points: -1, 0, 1, ∞
- At z = -1: 3-cycles on i (u-branch), j fixed. Two cycles: (0,0)→(1,0)→(2,0) and (0,1)→(1,1)→(2,1)
- At z = 0: 2-cycles on j (v-branch), i fixed. Three cycles: (0,0)↔(0,1), (1,0)↔(1,1), (2,0)↔(2,1)
- At z = 1: same as z = -1
- At z = ∞: 6-cycle (0,0)→(1,1)→(2,0)→(0,1)→(1,0)→(2,1)→(0,0)

For the branch cut scheme, we can choose:
- Cut from -1 to 1 (passing through 0, or we can use separate cuts)
- Cut from 1 to ∞

Or more naturally:
- Cut from -1 to 0 (for the v-branch at 0 and u-branch at -1)
- Cut from 0 to 1 (for the v-branch at 0 and u-branch at 1)
- Cut from 1 to ∞ (for the branch at ∞)

Actually, let me think about this more carefully. The standard way is:

For ³√(z²-1): branch cuts from -1 to 1 (or from -1 to -∞ and 1 to ∞, etc.). With a cut from -1 to 1, the function ³√(z²-1) is single-valued on the complement. The 3 sheets are connected via 3-cycles at -1 and 1.

For √(1/z) = z^{-1/2}: branch cut from 0 to ∞. The 2 sheets are connected via a 2-cycle at 0 (and at ∞).

But the combined function has interactions at ∞. Let me think about the cuts.

Actually, for the scheme, I think the clearest description is:

Choose cuts:
- [-1, 0]: crossing this cut swaps u-index (3-cycle) and v-index (2-cycle)... no, that's not right.

Hmm, let me think about this differently. The cuts should be chosen so that each cut has a well-defined monodromy.

Since the branch points -1, 0, 1, ∞ have monodromies:
- σ_{-1} = (i+1, j): acts on u only
- σ₀ = (i, j+1): acts on v only
- σ₁ = (i+1, j): acts on u only
- σ∞ = (i+1, j+1): acts on both

If we choose cuts from -1 to ∞ and from 0 to ∞ and from 1 to ∞ (all going to ∞), then:
- Crossing cut [-1, ∞]: monodromy σ_{-1} = (i+1, j)
- Crossing cut [0, ∞]: monodromy σ₀ = (i, j+1)
- Crossing cut [1, ∞]: monodromy σ₁ = (i+1, j)

At ∞, all three cuts meet, and the combined monodromy is σ_{-1} · σ₀ · σ₁ = (i+2, j+1). But σ∞ = (i+1, j+1). These don't match, which means... hmm.

Actually, the monodromy at ∞ should be the product of the monodromies at the finite branch points (in the right order). Going around ∞ counterclockwise (on the sphere) = going around all finite branch points clockwise. So σ∞ = (σ_{-1} · σ₀ · σ₁)^{-1} = (i+2, j+1)^{-1} = (i-2, j-1) = (i+1, j+1) [since -2 ≡ 1 mod 3 and -1 ≡ 1 mod 2]. So σ∞ = (i+1, j+1). ✓

OK so the scheme with cuts to ∞ works. But having three cuts all going to ∞ is a bit unusual. Let me use a different configuration.

Alternative: cuts [-1, 0], [0, 1], [1, ∞].
- Crossing [-1, 0]: monodromy = σ_{-1} = (i+1, j) [going around -1]
- Crossing [0, 1]: monodromy = σ₀ = (i, j+1) [going around 0]
- Crossing [1, ∞]: monodromy = σ₁ = (i+1, j) [going around 1]

At ∞: σ∞ = (σ_{-1} · σ₀ · σ₁)^{-1} = (i+1, j+1). ✓

This works! Each cut has a well-defined monodromy.

So the scheme for (b):
- 6 sheets labeled (i,j), i∈{0,1,2}, j∈{0,1}
- Cut [-1, 0]: 3-cycles on i (sheets (0,j)→(1,j)→(2,j)→(0,j) for j=0,1)
- Cut [0, 1]: 2-cycles on j (sheets (i,0)↔(i,1) for i=0,1,2)
- Cut [1, ∞]: 3-cycles on i (same as cut [-1, 0])
- At ∞: 6-cycle

Genus 3.

**Part c) √z + ³√z**

w = √z + ³√z = z^{1/2} + z^{1/3}

Let u = z^{1/2} (2 values), v = z^{1/3} (3 values). w = u + v.

Branch points: z = 0 and z = ∞ (both u and v branch at these points).

Number of sheets: u has 2 values, v has 3 values. If independent, 6 sheets. But are they independent?

u² = z, v³ = z, so u² = v³. This means u = v^{3/2}... hmm, but u and v are both determined by z. Actually, u = z^{1/2} and v = z^{1/3}, so u = v^{3/2} and v = u^{2/3}. The relation u² = v³ constrains them.

Given z, u = ±√z (2 choices), v = ³√z (3 choices). But u² = v³ = z. So once we pick v, u is determined up to sign: u = ±√(v³). But √(v³) = v^{3/2}, and v is a cube root of z, so v³ = z, and √(v³) = √z = u. So u = ±√z regardless of which v we pick. The choice of v doesn't constrain u.

Wait, but u² = v³ = z. So for a given z, u = ±√z and v = ωⁱ ³√z for i = 0, 1, 2. These are independent choices (2 × 3 = 6). So we have 6 sheets.

But wait, is there an algebraic relation between w and z that has degree less than 6?

w = u + v, u² = z, v³ = z. So u = w - v, (w-v)² = z, v³ = z. From v³ = z, (w-v)² = v³. So w² - 2wv + v² = v³, i.e., v³ - v² + 2wv - w² = 0. This is degree 3 in v and degree 2 in w. The resultant in v would give a polynomial in w of degree... let me think.

From v³ = z and (w-v)² = z, we get v³ = (w-v)². So v³ - (w-v)² = 0, i.e., v³ - w² + 2wv - v² = 0.

This is a cubic in v: v³ - v² + 2wv - w² = 0.

For each w, this gives up to 3 values of v, and then z = v³. But we want, for each z, the number of w values. 

Alternatively, from u² = z and v³ = z, w = u + v. The number of (u,v) pairs for given z is 2 × 3 = 6 (since u and v are independent). Each gives a w = u + v. Are any two w values equal? u₁ + v₁ = u₂ + v₂ requires u₁ - u₂ = v₂ - v₁. For generic z, the 2 values of u are ±√z and the 3 values of v are ωⁱ ³√z. The differences u₁ - u₂ are 0 or ±2√z. The differences v₂ - v₁ are 0 or (ω-1)³√z or (ω²-1)³√z or (ω²-ω)³√z. For these to be equal (for generic z), we'd need ±2√z = c · ³√z for some constant c, i.e., ±2z^{1/2} = c·z^{1/3}, i.e., ±2z^{1/6} = c. This only holds for specific z, not generically. So for generic z, all 6 values are distinct. 6 sheets.

Now the monodromy. Label sheets (i, j) where i = 0, 1 (for u = (-1)^i √z) and j = 0, 1, 2 (for v = ω^j ³√z).

**Monodromy at z = 0:**
Going around 0: z → ze^{2πi}.
u = z^{1/2} → z^{1/2} e^{πi} = -u. So i → i+1 mod 2.
v = z^{1/3} → z^{1/3} e^{2πi/3} = v · ω. So j → j+1 mod 3.

σ₀ = (i → i+1 mod 2, j → j+1 mod 3).

This is a single 6-cycle! Let me verify:
(0,0) → (1,1) → (0,2) → (1,0) → (0,1) → (1,2) → (0,0). Yes, 6-cycle.

**Monodromy at z = ∞:**
Going around ∞ (counterclockwise on sphere) = z → ze^{-2πi}.
u = z^{1/2} → z^{1/2} e^{-πi} = -u. So i → i+1 mod 2.
v = z^{1/3} → z^{1/3} e^{-2πi/3} = v · ω². So j → j+2 mod 3 = j-1 mod 3.

σ∞ = (i → i+1 mod 2, j → j-1 mod 3).

Let me verify the product σ₀ · σ∞ = identity:
σ₀: (i+1, j+1), σ∞: (i+1, j-1).
Product (right to left): (i, j) → σ∞ → (i+1, j-1) → σ₀ → (i+2, j) = (i, j) [since i+2 ≡ i mod 2]. ✓

So σ∞ = (i+1, j-1). Let me trace the cycle:
(0,0) → (1,2) → (0,1) → (1,0) → (0,2) → (1,1) → (0,0). Also a 6-cycle.

So the Riemann surface for (c) has:
- 6 sheets
- 2 branch points: z = 0 and z = ∞
- At z = 0: one 6-cycle (branch order 6)
- At z = ∞: one 6-cycle (branch order 6)

Genus by Riemann-Hurwitz:
2g - 2 = 6(-2) + R
R = (6-1) + (6-1) = 10.
2g - 2 = -12 + 10 = -2.
2g = 0, g = 0.

Genus 0.

**Scheme for (c):**
- 6 sheets
- Branch cut from 0 to ∞
- Crossing the cut: 6-cycle (0,0)→(1,1)→(0,2)→(1,0)→(0,1)→(1,2)→(0,0)
- At both 0 and ∞: branch order 6

This is a cyclic 6-sheeted cover of the sphere, branched at 0 and ∞.

**Part d) ⁴√(z²-1) + ⁴√(z-1)**

w = ⁴√(z²-1) + ⁴√(z-1) = ⁴√((z-1)(z+1)) + ⁴√(z-1)

Let u = ⁴√(z²-1) = ⁴√((z-1)(z+1)), v = ⁴√(z-1).

u⁴ = z² - 1 = (z-1)(z+1), v⁴ = z - 1.

So u⁴ = v⁴(z+1), i.e., u⁴/v⁴ = z+1, (u/v)⁴ = z+1.

Also z = v⁴ + 1, so u⁴ = (v⁴+1)² - 1 = v⁸ + 2v⁴ = v⁴(v⁴ + 2).
So u = v · ⁴√(v⁴ + 2).

w = u + v = v(⁴√(v⁴ + 2) + 1).

Number of sheets: u has 4 values, v has 4 values. But u⁴ = v⁴(z+1), so given v, u⁴ = v⁴(z+1) = v⁴(v⁴+2). So u = v · ⁴√(v⁴+2), which has 4 values. But v itself has 4 values. So total: 4 × 4 = 16? But we need to check if the relation u⁴ = v⁴(z+1) reduces this.

Given z, v = ⁴√(z-1) has 4 values: v_k = ζ^k · v₀ where ζ = e^{2πi/4} = i, k = 0,1,2,3.
Given v, u = ⁴√(v⁴(z+1)) = ⁴√(v⁴ · (v⁴+2)) = v · ⁴√(v⁴+2). But v⁴ = z-1, so u = ⁴√((z-1)(z+1)) = ⁴√(z²-1), which has 4 values: u_m = ζ^m · u₀.

Are u and v independent? u⁴ = (z-1)(z+1) = v⁴(z+1). So u⁴ = v⁴(z+1). Given z, v is one of 4 values, and u is one of 4 values, with the constraint u⁴ = v⁴(z+1). But v⁴ = z-1 for all 4 values of v (since (ζ^k v₀)⁴ = ζ^{4k} v₀⁴ = v₀⁴ = z-1). So u⁴ = (z-1)(z+1) = z²-1 regardless of which v we pick. So u and v are indeed independent: 4 × 4 = 16 sheets.

Wait, but that seems like a lot. Let me double-check by finding the algebraic equation.

w = u + v, u⁴ = z²-1, v⁴ = z-1.
u = w - v, (w-v)⁴ = z²-1, v⁴ = z-1.
z = v⁴ + 1, (w-v)⁴ = (v⁴+1)² - 1 = v⁸ + 2v⁴.

So (w-v)⁴ = v⁸ + 2v⁴ = v⁴(v⁴+2).

This is degree 4 in w and degree 8 in v. The number of (w, v) pairs for given z is... for given z, v has 4 values, and for each v, w = v + u where u has 4 values, giving 4 w values. So 16 values of w.

But are all 16 distinct? For generic z, yes (by a similar argument as before).

Hmm, but 16 sheets seems like a lot. Let me reconsider.

Actually, wait. Let me reconsider whether u and v are truly independent. We have u⁴ = z²-1 and v⁴ = z-1. Note that z²-1 = (z-1)(z+1) = v⁴(v⁴+2). So u⁴ = v⁴(v⁴+2), which means (u/v)⁴ = v⁴+2 = z+1. So u/v = ⁴√(z+1), which has 4 values. And v = ⁴√(z-1) has 4 values. So w = u + v = v(⁴√(z+1) + 1).

Let me set a = ⁴√(z+1) (4 values) and b = ⁴√(z-1) (4 values). Then u = ab and v = b, so w = b(a+1).

Are a and b independent? a⁴ = z+1, b⁴ = z-1. These are independent (different functions of z). So 4 × 4 = 16 values of w = b(a+1).

For generic z, are all 16 values distinct? w = b(a+1) where a = ζ^i a₀, b = ζ^j b₀. w_{ij} = ζ^j b₀ (ζ^i a₀ + 1). For w_{ij} = w_{kl}, we need ζ^j b₀(ζ^i a₀ + 1) = ζ^l b₀(ζ^k a₀ + 1), i.e., ζ^j(ζ^i a₀ + 1) = ζ^l(ζ^k a₀ + 1). For generic a₀, this requires j = l and i = k. So yes, 16 distinct values.

So 16 sheets. That's a lot. Let me reconsider...

Actually, I wonder if the problem is asking for something simpler. Let me re-read the problem.

"Draw the schemes of the Riemann surfaces of the following functions"

OK so it's asking for the scheme (topological structure) of each Riemann surface. For part (d), 16 sheets is correct if u and v are independent.

Let me identify the branch points.

u = ⁴√(z²-1) = ⁴√((z-1)(z+1)):
- z = 1: z²-1 has a simple zero, so ⁴√(z²-1) has a branch point of order 4.
- z = -1: same, branch point of order 4.
- z = ∞: z²-1 ~ z², ⁴√(z²-1) ~ z^{1/2}. Going around ∞: z → ze^{2πi}, z^{1/2} → -z^{1/2}. So branch point of order 2 (since z^{1/2} has period 2 under z → ze^{2πi}).

Wait, let me be more careful. ⁴√(z²) = z^{2/4} = z^{1/2}. Going around ∞ (z → ze^{2πi}): z^{1/2} → z^{1/2} e^{πi} = -z^{1/2}. So the monodromy is of order 2 (going around twice gives identity). So at ∞, u has a branch point of order 2 (not 4).

v = ⁴√(z-1):
- z = 1: branch point of order 4.
- z = ∞: ⁴√(z-1) ~ z^{1/4}. Going around ∞: z → ze^{2πi}, z^{1/4} → z^{1/4} e^{πi/2} = iz^{1/4}. So branch point of order 4.

So the branch points are: z = -1, 1, ∞.

At z = 1: both u and v branch. u has order 4, v has order 4.
At z = -1: only u branches, order 4.
At z = ∞: u has order 2, v has order 4.

Let me work out the monodromies.

Label sheets as (i, j) where i = 0,1,2,3 (for u = ζ^i u₀, ζ = i = e^{2πi/4}) and j = 0,1,2,3 (for v = ζ^j v₀).

**Monodromy at z = 1:**
Near z = 1: z²-1 ≈ 2(z-1), z-1 ≈ (z-1).
Going around z = 1: (z-1) → (z-1)e^{2πi}.
u = ⁴√(z²-1) ≈ ⁴√(2(z-1)) → ⁴√(2(z-1)) · e^{2πi/4} = u · ζ. So i → i+1 mod 4.
v = ⁴√(z-1) → ⁴√(z-1) · e^{2πi/4} = v · ζ. So j → j+1 mod 4.

σ₁ = (i → i+1, j → j+1).

This is a permutation on 16 elements. Let me trace the cycles:
(0,0) → (1,1) → (2,2) → (3,3) → (0,0): 4-cycle.
(0,1) → (1,2) → (2,3) → (3,0) → (0,1): 4-cycle.
(0,2) → (1,3) → (2,0) → (3,1) → (0,2): 4-cycle.
(0,3) → (1,0) → (2,1) → (3,2) → (0,3): 4-cycle.

So σ₁ consists of four 4-cycles.

**Monodromy at z = -1:**
Near z = -1: z²-1 ≈ -2(z+1), z-1 ≈ -2 (constant).
Going around z = -1: (z+1) → (z+1)e^{2πi}.
u = ⁴√(z²-1) ≈ ⁴√(-2(z+1)) → u · e^{2πi/4} = u · ζ. So i → i+1 mod 4.
v = ⁴√(z-1) is unchanged (z-1 ≈ -2, not near 0). So j → j.

σ_{-1} = (i → i+1, j → j).

Cycles: for each j, (0,j) → (1,j) → (2,j) → (3,j) → (0,j). Four 4-cycles.

**Monodromy at z = ∞:**
Going around ∞ (counterclockwise on sphere) = z → ze^{-2πi}.
u ~ z^{1/2} → z^{1/2} e^{-πi} = -u. So i → i+2 mod 4 (since -1 = ζ²).
v ~ z^{1/4} → z^{1/4} e^{-πi/2} = v · ζ^{-1} = v · ζ³. So j → j+3 mod 4 = j-1 mod 4.

σ∞ = (i → i+2, j → j-1).

Let me verify the product: σ_{-1} · σ₁ · σ∞ = identity.
σ_{-1}: (i+1, j)
σ₁: (i+1, j+1)
σ∞: (i+2, j-1)

Product (right to left): (i,j) → σ∞ → (i+2, j-1) → σ₁ → (i+3, j) → σ_{-1} → (i+4, j) = (i, j). ✓

Now let me trace the cycles of σ∞ = (i+2, j-1):
(0,0) → (2,3) → (0,2) → (2,1) → (0,0): 4-cycle.
(0,1) → (2,0) → (0,3) → (2,2) → (0,1): 4-cycle.
(1,0) → (3,3) → (1,2) → (3,1) → (1,0): 4-cycle.
(1,1) → (3,0) → (1,3) → (3,2) → (1,1): 4-cycle.

So σ∞ also consists of four 4-cycles.

Genus by Riemann-Hurwitz:
2g - 2 = 16(-2) + R

R = sum of (e-1) over all ramification points.
At z = -1: four 4-cycles, each contributes (4-1) = 3, total 12.
At z = 1: four 4-cycles, each contributes (4-1) = 3, total 12.
At z = ∞: four 4-cycles, each contributes (4-1) = 3, total 12.

R = 12 + 12 + 12 = 36.
2g - 2 = -32 + 36 = 4.
2g = 6, g = 3.

Genus 3.

**Scheme for (d):**
- 16 sheets labeled (i, j), i, j ∈ {0,1,2,3}
- Branch points: -1, 1, ∞
- At z = -1: four 4-cycles, (i → i+1, j fixed)
- At z = 1: four 4-cycles, (i → i+1, j → j+1)
- At z = ∞: four 4-cycles, (i → i+2, j → j-1)

For cuts: [-1, 0] (or [-1, 1]), [1, ∞].

Actually, let me choose cuts [-1, 1] and [1, ∞].
- Crossing [-1, 1]: monodromy = σ_{-1} = (i+1, j) [going around -1]
- Crossing [1, ∞]: monodromy = σ₁ = (i+1, j+1) [going around 1]

At ∞: σ∞ = (σ_{-1} · σ₁)^{-1} = ((i+2, j+1))^{-1} = (i-2, j-1) = (i+2, j-1). ✓

Hmm wait, I need to be more careful about which monodromy corresponds to which cut.

With cuts [-1, 1] and [1, ∞]:
- Crossing [-1, 1] near -1: going around -1, monodromy σ_{-1} = (i+1, j).
- Crossing [-1, 1] near 1: going around 1, monodromy σ₁ = (i+1, j+1).

But these are different! So the cut [-1, 1] doesn't have a uniform monodromy. This is the same issue as in part (a).

The issue is that -1 and 1 have different monodromies, so a cut connecting them doesn't have a single monodromy. We need cuts from each branch point to ∞ (or some other configuration where each cut has a single monodromy).

Let me use cuts from -1 to ∞ and from 1 to ∞ (not passing through each other).
- Crossing cut [-1, ∞]: monodromy σ_{-1} = (i+1, j)
- Crossing cut [1, ∞]: monodromy σ₁ = (i+1, j+1)

At ∞: σ∞ = (σ_{-1} · σ₁)^{-1} = (i+2, j+1)^{-1} = (i+2, j-1). ✓

This works. Each cut has a well-defined monodromy.

Now let me write up the complete solution.

Actually, let me reconsider the problem. It says "draw the schemes." In the context of a textbook problem (likely from Shabat's "Introduction to Complex Analysis"), the "scheme" of a Riemann surface refers to a picture showing:
1. The number of sheets
2. The branch cuts
3. How sheets are connected across the cuts

Since I can't actually draw pictures, I'll describe the schemes in detail.

Let me also double-check my work on part (a) regarding the genus and the structure.

For part (a), I found genus 0, 4 sheets, 3 branch points each with two 2-cycles. Let me reconsider the cut structure.

For part (a), the monodromies are:
- σ₀ = (1 3)(2 4) at z = 0
- σ₁ = (1 2)(3 4) at z = 1
- σ∞ = (1 4)(2 3) at z = ∞

With cuts [0, ∞) and [1, ∞):
- Crossing [0, ∞): σ₀ = (1 3)(2 4)
- Crossing [1, ∞): σ₁ = (1 2)(3 4)
- At ∞: σ∞ = (σ₀ · σ₁)^{-1} = ((1 3)(2 4) · (1 2)(3 4))^{-1} = (1 4)(2 3)^{-1} = (1 4)(2 3). ✓

So the scheme for (a):
- 4 sheets
- Cut from 0 to ∞: connects sheets 1↔3 and 2↔4
- Cut from 1 to ∞: connects sheets 1↔2 and 3↔4

Now let me write up the full solution.

Actually, let me reconsider whether I should present the cuts differently. In many textbooks, the scheme is presented with cuts between finite branch points when possible, and cuts to ∞ otherwise.

For part (a), we could also use a cut [0,1] and a cut [1,∞]. But as I noted, the cut [0,1] doesn't have a uniform monodromy since 0 and 1 have different monodromies. However, in the standard treatment, when we have a cut between two branch points, the monodromy of crossing the cut is well-defined: it's the monodromy of going around one of the branch points (say the one on the left), and the other branch point's monodromy is "absorbed" into the other cut.

Actually, I think the standard approach is: with a cut from 0 to 1, crossing this cut corresponds to going around 0 (giving σ₀) if we think of the cut as emanating from 0, or going around 1 (giving σ₁) if we think of it as emanating from 1. The key point is that the cut [0,1] separates the plane into two regions, and crossing it changes sheets according to the monodromy of a loop that crosses the cut once. This loop goes around either 0 or 1 (but not both), and the monodromy depends on which one.

But in practice, for a cut between two branch points, the monodromy is the same everywhere along the cut IF the two branch points have the same monodromy. If they have different monodromies (as in our case), the cut doesn't have a uniform monodromy, and we need to use cuts to ∞ instead.

Hmm, but actually, in many standard treatments, cuts between branch points are used even when the monodromies differ. The idea is that the cut [0,1] has the monodromy of going around 0 (which equals the monodromy of going around 1 times the monodromy of going around ∞, by the relation σ₀ · σ₁ · σ∞ = id, so σ₀ = σ∞^{-1} · σ₁^{-1} = σ∞ · σ₁ since they're involutions).

Wait, I think I'm overcomplicating this. Let me reconsider.

The standard way to think about it: we make a cut from 0 to 1. The function is single-valued on the complement. When we cross the cut, we move to a different sheet. The specific monodromy of crossing the cut is determined by the branch point that the cut emanates from. But since the cut connects 0 and 1, crossing it near 0 gives σ₀ and crossing it near 1 gives σ₁. If σ₀ ≠ σ₁, the monodromy changes along the cut.

In the standard scheme drawing, this is handled by noting that the cut [0,1] has the monodromy σ₀ at the 0-end and σ₁ at the 1-end, and the monodromy "changes" somewhere along the cut. But this is not a clean picture.

The cleaner approach for the scheme: use cuts from each branch point to ∞. Then each cut has a well-defined monodromy.

For part (a): cuts [0, ∞) and [1, ∞).
- Cut [0, ∞): monodromy (1 3)(2 4) — sheets 1↔3, 2↔4
- Cut [1, ∞): monodromy (1 2)(3 4) — sheets 1↔2, 3↔4

For part (b): cuts [-1, ∞), [0, ∞), [1, ∞).
- Cut [-1, ∞): monodromy (i+1, j) — 3-cycles on u
- Cut [0, ∞): monodromy (i, j+1) — 2-cycles on v
- Cut [1, ∞): monodromy (i+1, j) — 3-cycles on u

For part (c): cut [0, ∞).
- Cut [0, ∞): monodromy (i+1, j+1) — 6-cycle

For part (d): cuts [-1, ∞) and [1, ∞).
- Cut [-1, ∞): monodromy (i+1, j) — 4-cycles on u
- Cut [1, ∞): monodromy (i+1, j+1) — 4-cycles on u and v

OK, I think I have a good understanding now. Let me write up the solution.

Let me also reconsider the branch order at ∞ for each part.

For part (a): σ∞ = (1 4)(2 3), which is two 2-cycles. So ∞ has two branch points of order 2.

For part (b): σ∞ = (i+1, j+1), which is one 6-cycle. So ∞ has one branch point of order 6.

For part (c): σ₀ and σ∞ are both 6-cycles. So 0 and ∞ each have one branch point of order 6.

For part (d): σ∞ = (i+2, j-1), which is four 4-cycles. So ∞ has four branch points of order 4.

Wait, for part (d) at ∞, I said u has order 2 and v has order 4. The combined monodromy is (i+2, j-1), which has order lcm(2, 4) = 4. And it decomposes into four 4-cycles. So each ramification point at ∞ has e = 4, and there are 4 of them.

Let me recheck: the cycle structure of (i+2, j-1) on 16 elements:
Fix j-1 = j' (shift), then i → i+2. For fixed j', the i-cycle is (0 → 2 → 0), a 2-cycle. But we also have j → j-1, so after 2 steps: i → i+4 = i, j → j-2. After 4 steps: i → i+8 = i, j → j-4 = j. So the order is 4, and each cycle has length 4.

Let me trace: (0,0) → (2,3) → (0,2) → (2,1) → (0,0). Length 4. ✓
There are 16/4 = 4 cycles. ✓

So at ∞, we have 4 ramification points with e = 4, each contributing 3 to R. Total from ∞: 12.

At -1: (i+1, j), order 4, cycles of length 4. 16/4 = 4 cycles. Each contributes 3. Total: 12.
At 1: (i+1, j+1), order 4, cycles of length 4. 16/4 = 4 cycles. Each contributes 3. Total: 12.

R = 36, 2g-2 = -32+36 = 4, g = 3. ✓

Now let me write the solution. I'll describe each scheme clearly.

One more thing to verify for part (b): the branch order at ∞.

σ∞ = (i+1, j+1) on 6 elements. Order = lcm(3, 2) = 6. One 6-cycle. So ∞ has one branch point of order 6, contributing 5 to R. ✓

And for part (b) at z = 0: σ₀ = (i, j+1), which is three 2-cycles. Order 2. Three cycles, each contributing 1. Total: 3. ✓

At z = ±1: σ = (i+1, j), which is two 3-cycles. Order 3. Two cycles, each contributing 2. Total: 4 each. ✓

R = 4 + 3 + 4 + 5 = 16. 2g-2 = -12+16 = 4. g = 3. ✓

Now, let me also think about whether the problem expects a simpler answer. The problem says "draw the schemes," which in a complex analysis course typically means describing the branch cuts and sheet connections. Let me present this clearly.

Let me also reconsider: for part (a), I should double-check that the function is indeed 4-sheeted and not 2-sheeted.

w = √z + √(z-1). The four values are:
w₁ = √z + √(z-1)
w₂ = √z - √(z-1)
w₃ = -√z + √(z-1) = -(√z - √(z-1)) = -w₂
w₄ = -√z - √(z-1) = -w₁

So w₃ = -w₂ and w₄ = -w₁. The four values come in pairs (w₁, -w₁) and (w₂, -w₂). For generic z, w₁ ≠ ±w₂, so we have 4 distinct values. ✓

Also, w₁ · w₂ = (√z + √(z-1))(√z - √(z-1)) = z - (z-1) = 1. So w₂ = 1/w₁. And w₃ = -1/w₁, w₄ = -w₁. So the four values are w₁, 1/w₁, -1/w₁, -w₁. This is consistent with the equation w⁴ - (4z-2)w² + 1 = 0 (which is a quadratic in w²).

OK, I'm confident in my analysis. Let me write the solution.

Let me also think about how to present the "scheme" clearly. The scheme of a Riemann surface is a topological description consisting of:
1. Number of sheets
2. Branch points and their locations
3. Branch cuts
4. How sheets are connected across each cut (the monodromy)

I'll present each part with these elements.

Let me also reconsider the branch cut choices to make them more standard.

For part (a): Branch points at 0, 1, ∞. Standard cuts: [0,1] and [1,∞], or [0,∞) and [1,∞). I'll use [0,∞) and [1,∞) for clarity (each cut has a single monodromy).

Actually, for a more standard presentation, let me use [0,1] and [1,∞] for part (a). Even though the monodromy isn't uniform along [0,1], in practice the scheme is drawn with the understanding that the cut [0,1] carries the monodromy of the branch point at 0 (or 1), and the other branch point's monodromy is carried by the other cut.

Hmm, actually, I think the standard approach in Russian textbooks is different. Let me reconsider.

In Shabat's textbook, the scheme is typically drawn as follows: you have n sheets (n = number of values), and you draw branch cuts. Across each cut, you indicate which sheets are connected. The cuts are chosen so that each cut connects two branch points (or a branch point to ∞), and the monodromy is indicated.

For a cut between two branch points a and b, the monodromy of crossing the cut is the monodromy of going around a (which is the same as going around b, if a and b are the only branch points connected by this cut and the monodromy at ∞ accounts for the rest).

Wait, that's not right either. The monodromy of crossing a cut [a,b] is the monodromy of a loop that goes around a but not b (or vice versa). If a and b have different monodromies, the cut [a,b] has a well-defined monodromy only if we specify which end we're crossing.

I think the cleanest approach for this problem is:

For each function, I'll describe:
1. The algebraic equation satisfied by w
2. The number of sheets
3. The branch points and their monodromies (as permutations)
4. A choice of branch cuts and the sheet connections across each cut
5. The genus

Let me write this up now.

Actually, I realize there's a subtlety I should address for part (a). Let me reconsider whether we can use a cut [0,1].

With a cut [0,1], the complement of [0,1] in the sphere (plus the cut [1,∞]) is simply connected. On this region, we can define single-valued branches. The monodromy of crossing [0,1] is the monodromy of a loop that goes around 0 (but not 1 or ∞). This is σ₀ = (1 3)(2 4). The monodromy of crossing [1,∞] is the monodromy of a loop that goes around 1 and ∞ (but not 0). This is σ₁ · σ∞ = σ₀^{-1} = σ₀ (since σ₀ is an involution). Wait, that gives the same monodromy for both cuts, which can't be right.

Let me reconsider. With cuts [0,1] and [1,∞]:
- A loop crossing [0,1] once (going from upper half-plane to lower) corresponds to going around 0. Monodromy: σ₀ = (1 3)(2 4).
- A loop crossing [1,∞] once corresponds to going around ∞ (and 1). Monodromy: σ₁ · σ∞... no.

Actually, a loop that crosses [1,∞] once goes around 1 (and ∞). The monodromy is σ₁ if the loop goes around 1 but not ∞, or σ₁ · σ∞ if it goes around both. But with the cut [1,∞], a loop crossing this cut goes around 1 but not ∞ (since ∞ is on the cut). Hmm, this is getting confusing.

Let me think about it more carefully. With cuts [0,1] and [1,∞] (both on the real axis), the complement is the plane minus these two intervals. This is simply connected. A path from the upper half-plane to the lower half-plane crossing [0,1] goes around 0. A path crossing [1,∞] goes around 1 (and also ∞, since the cut extends to ∞).

Actually, crossing [1,∞] from above to below is equivalent to going around 1 (a small loop around 1 crosses [1,∞] on one side and [0,1] on the other... no, 1 is the junction point).

I think the issue is that 1 is where the two cuts meet, so loops around 1 cross both cuts. Let me use non-intersecting cuts instead.

Let me use:
- Cut A: from 0 to ∞ along the negative real axis (i.e., [0, -∞))
- Cut B: from 1 to ∞ along the positive real axis (i.e., [1, +∞))

These don't intersect (except at ∞). The complement is simply connected.

- Crossing cut A (from 0 to -∞): going around 0. Monodromy: σ₀ = (1 3)(2 4).
- Crossing cut B (from 1 to +∞): going around 1. Monodromy: σ₁ = (1 2)(3 4).

At ∞: σ∞ = (σ₀ · σ₁)^{-1} = (1 4)(2 3). ✓

This is clean. Each cut has a well-defined monodromy.

OK, I think for the solution, I'll use cuts to ∞ for all parts, as this gives the cleanest description.

Let me now write the complete solution.

Hmm, actually, I want to reconsider part (a) once more. Is the genus really 0?

We have 4 sheets, 3 branch points, each with two 2-cycles (i.e., two simple branch points at each location).

Riemann-Hurwitz: 2g - 2 = 4(2·0 - 2) + R = -8 + R.
R = 3 × 2 × (2-1) = 6 (three branch points, each with two simple ramification points, each contributing 1).
2g - 2 = -8 + 6 = -2, g = 0. ✓

Yes, genus 0. The Riemann surface is topologically a sphere.

Now let me also verify: can we see this directly? The function w = √z + √(z-1) with w₁ · w₂ = 1 (where w₂ = √z - √(z-1)). So w and 1/w are both values. The equation w⁴ - (4z-2)w² + 1 = 0 is a quadratic in w², so w² = [(4z-2) ± 4√(z(z-1))]/2 = (2z-1) ± 2√(z(z-1)).

Let t = w². Then t = (2z-1) ± 2√(z(z-1)). This is a 2-sheeted function of z (branched at 0 and 1). Then w = ±√t, which is a 2-sheeted function of t (branched at t = 0 and t = ∞). But we showed t never equals 0, so w = √t is branched only at t = ∞.

As z → ∞, t₊ = (2z-1) + 2√(z(z-1)) ≈ 2z - 1 + 2z = 4z → ∞, and t₋ = (2z-1) - 2√(z(z-1)) ≈ 2z - 1 - 2z = -1 → -1. So t₊ → ∞ and t₋ → -1.

So the map z → t is 2-sheeted (branched at 0, 1, ∞), and the map t → w is 2-sheeted (branched at t = ∞, which corresponds to z = ∞ via t₊, and at t = -1... wait, w = √t is branched at t = 0 and t = ∞. t₋ → -1 as z → ∞, so t = 0 is not in the image of t₋ for large z. But t₊ → ∞, so t = ∞ is in the image.

Hmm, this is getting complicated. Let me just trust the Riemann-Hurwitz calculation. Genus 0.

Now, let me write the solution. I'll describe each scheme clearly, including the number of sheets, branch points, monodromies, cuts, and genus.

One more consideration: for part (b), I should double-check the branch at ∞.

σ∞ = (i+1, j+1) on 6 elements. This is a 6-cycle, so it's a single branch point of order 6 at ∞. But let me verify this makes sense.

u = ³√(z²-1) ~ z^{2/3} as z → ∞. Going around ∞ (z → ze^{-2πi}): z^{2/3} → z^{2/3} e^{-4πi/3} = z^{2/3} e^{2πi/3} = u · ω. So i → i+1. ✓
v = z^{-1/2} → z^{-1/2} e^{πi} = -v. So j → j+1. ✓
Combined: (i+1, j+1), which is a 6-cycle. ✓

OK, everything checks out. Let me write the solution.

Let me also think about how to describe the schemes in a way that could be "drawn." The scheme is typically a picture with:
- Horizontal lines representing sheets
- Branch cuts shown as gaps or connections between sheets
- Labels indicating which sheets are connected

Since I can't draw, I'll describe this verbally.

Let me write the solution now.

For part (b), let me reconsider the branch cut structure. We have branch points at -1, 0, 1, ∞. Using cuts to ∞:
- Cut from -1 to ∞: monodromy (i+1, j) — 3-cycles on u
- Cut from 0 to ∞: monodromy (i, j+1) — 2-cycles on v
- Cut from 1 to ∞: monodromy (i+1, j) — 3-cycles on u

But having three cuts all going to ∞ is a bit unusual. An alternative is:
- Cut from -1 to 0: monodromy σ_{-1} = (i+1, j) — 3-cycles on u
- Cut from 0 to 1: monodromy σ₀ = (i, j+1) — 2-cycles on v
- Cut from 1 to ∞: monodromy σ₁ = (i+1, j) — 3-cycles on u

This works because each cut connects two branch points with different monodromies, and the monodromy of crossing each cut is well-defined (it's the monodromy of the branch point on the left, say).

Wait, but I said earlier that a cut between two branch points with different monodromies doesn't have a uniform monodromy. Let me reconsider.

Actually, I think the key insight is: if we have a cut from a to b, the monodromy of crossing this cut is the monodromy of going around a (which is σ_a). This is well-defined because the cut separates the plane, and crossing it from one side to the other is equivalent to going around a (but not b). The monodromy at b is then carried by a different cut emanating from b.

So with cuts [-1, 0], [0, 1], [1, ∞]:
- Crossing [-1, 0]: go around -1, monodromy σ_{-1} = (i+1, j)
- Crossing [0, 1]: go around 0, monodromy σ₀ = (i, j+1)
- Crossing [1, ∞]: go around 1, monodromy σ₁ = (i+1, j)

At ∞: σ∞ = (σ_{-1} · σ₀ · σ₁)^{-1} = (i+1, j+1). ✓

This is clean and standard. Each cut connects consecutive branch points, and the monodromy is that of the left endpoint.

Similarly for part (a), with cuts [0, 1] and [1, ∞]:
- Crossing [0, 1]: go around 0, monodromy σ₀ = (1 3)(2 4)
- Crossing [1, ∞]: go around 1, monodromy σ₁ = (1 2)(3 4)

At ∞: σ∞ = (σ₀ · σ₁)^{-1} = (1 4)(2 3). ✓

This is clean! I was overcomplicating things earlier. The cut [0,1] has monodromy σ₀ (going around 0), and the cut [1,∞] has monodromy σ₁ (going around 1). The fact that 0 and 1 have different monodromies is fine — each cut carries the monodromy of its left endpoint.

Wait, but what about the right endpoint? The cut [0,1] also connects to 1, which has monodromy σ₁. When we cross [0,1] near 1, do we get σ₁ instead of σ₀?

I think the answer is no. The cut [0,1] is a single cut, and crossing it anywhere gives the same monodromy, which is σ₀ (the monodromy of going around 0). The monodromy σ₁ is carried by the cut [1,∞]. The point 1 is where the two cuts meet, and going around 1 requires crossing both cuts.

Let me verify: a small loop around 1 crosses both [0,1] and [1,∞]. The monodromy is σ₀ (from crossing [0,1]) followed by σ₁ (from crossing [1,∞]) = σ₀ · σ₁. But the monodromy around 1 should be σ₁, not σ₀ · σ₁.

Hmm, that's a contradiction. Let me reconsider.

Actually, a small loop around 1 crosses [1,∞] once (going from one side to the other and back). It doesn't cross [0,1] if the loop is small enough. So the monodromy around 1 is just σ₁ (from crossing [1,∞]). ✓

And a small loop around 0 crosses [0,1] once. Monodromy: σ₀. ✓

A loop around ∞ crosses [1,∞] once (going around ∞ means going around the "outside" of the cut [1,∞]). Monodromy: σ₁. But σ∞ should be (σ₀ · σ₁)^{-1} = σ₀ · σ₁ (since they're involutions). So σ∞ = σ₀ · σ₁ = (1 3)(2 4) · (1 2)(3 4) = (1 4)(2 3). ✓

But wait, a loop around ∞ crosses [1,∞] once, giving monodromy σ₁ = (1 2)(3 4). But σ∞ = (1 4)(2 3) ≠ σ₁. Contradiction!

Let me reconsider. A loop around ∞ (counterclockwise on the sphere) is a large loop in the plane going clockwise. This loop crosses [1,∞] (if [1,∞] is on the positive real axis). Going clockwise around ∞, we cross [1,∞] from below to above (or vice versa). The monodromy of this crossing is... hmm.

Actually, I think the issue is the direction. Crossing [1,∞] from above to below gives monodromy σ₁, and crossing from below to above gives σ₁^{-1} = σ₁ (since it's an involution). So the direction doesn't matter for involutions.

But a loop around ∞ should give σ∞, not σ₁. The resolution is that a loop around ∞ doesn't just cross [1,∞]; it also crosses [0,1] if the loop is large enough to enclose 0.

Wait, no. If the cuts are [0,1] and [1,∞] (both on the real axis), a large loop around ∞ (clockwise in the plane, counterclockwise on the sphere) crosses [1,∞] once but doesn't cross [0,1] (since [0,1] is inside the loop). Hmm, but the loop goes around everything, so it should cross both cuts.

I think I'm getting confused by the topology. Let me think about this more carefully.

The cuts [0,1] and [1,∞] divide the sphere into a simply connected region. A loop around ∞ on the sphere corresponds to a large clockwise loop in the plane. This loop starts in the upper half-plane, goes clockwise (to the right, then down, then left, then up). It crosses [1,∞] once (going from above to below, say) and doesn't cross [0,1] (since [0,1] is enclosed by the loop). 

Wait, actually, a large clockwise loop in the plane encloses everything. It crosses [1,∞] once (at some point x > 1) and crosses [0,1] zero times (since [0,1] is inside the loop, and the loop doesn't cross the real axis between 0 and 1... actually, it does cross the real axis, but at a point x > 1 or x < 0).

Hmm, let me think about this differently. The loop goes around ∞, which means it's a large circle traversed clockwise. It crosses the positive real axis at some point x > 1 (crossing [1,∞]) and crosses the negative real axis at some point x < 0 (not crossing any cut). So it crosses [1,∞] once and [0,1] zero times. Monodromy: σ₁.

But σ∞ should be (1 4)(2 3), and σ₁ = (1 2)(3 4). These are different!

I think the issue is that the loop around ∞ also crosses the cut [1,∞] in a specific direction that might give σ₁^{-1} instead of σ₁. But since σ₁ is an involution, σ₁ = σ₁^{-1}. So the monodromy is σ₁, which should equal σ∞. But σ₁ ≠ σ∞. Contradiction!

OK, I think I'm making an error somewhere. Let me reconsider.

The issue might be with how the cuts are set up. Let me reconsider.

With cuts [0,1] and [1,∞] on the real axis, the complement in the Riemann sphere is simply connected. On this complement, we have 4 single-valued branches of w. The monodromy of crossing a cut tells us how to move between sheets.

A loop around 0 (small, counterclockwise): crosses [0,1] once. Monodromy: σ₀.
A loop around 1 (small, counterclockwise): crosses [0,1] once and [1,∞] once. Monodromy: σ₀ · σ₁ (or σ₁ · σ₀, depending on the order of crossings).

Hmm, this is the issue. A small loop around 1 crosses both cuts (since 1 is the junction point). The monodromy is the product of the two crossings.

But the monodromy around 1 should be σ₁. So σ₁ = (product of crossings of [0,1] and [1,∞]).

If the loop around 1 first crosses [0,1] and then [1,∞], the monodromy is σ_{[0,1]} · σ_{[1,∞]}. If σ_{[0,1]} = σ₀ and σ_{[1,∞]} = σ₁, then the product is σ₀ · σ₁, which should equal σ₁. This gives σ₀ = identity, which is wrong.

So my assignment of monodromies to cuts is incorrect!

Let me reconsider. The correct assignment should be:
- Crossing [0,1] gives monodromy A
- Crossing [1,∞] gives monodromy B
- Loop around 0: crosses [0,1] once, monodromy = A = σ₀
- Loop around 1: crosses [0,1] once and [1,∞] once, monodromy = A · B = σ₁ (or B · A = σ₁)
- Loop around ∞: crosses [1,∞] once, monodromy = B = σ∞

From loop around 0: A = σ₀ = (1 3)(2 4).
From loop around ∞: B = σ∞ = (1 4)(2 3).
From loop around 1: A · B = σ₀ · σ∞ = (1 3)(2 4) · (1 4)(2 3).

Let me compute: (1 3)(2 4) · (1 4)(2 3) (right to left):
1 → (1 4) → 4 → (2 4) → 2. So 1 → 2.
2 → (2 3) → 3 → (1 3) → 1. So 2 → 1. Good, (1 2).
3 → (2 3) → 2 → (2 4) → 4. So 3 → 4.
4 → (1 4) → 1 → (1 3) → 3. So 4 → 3. Good, (3 4).

So A · B = (1 2)(3 4) = σ₁. ✓

So the correct assignment is:
- Crossing [0,1]: monodromy σ₀ = (1 3)(2 4)
- Crossing [1,∞]: monodromy σ∞ = (1 4)(2 3)

And σ₁ = σ₀ · σ∞ (from the loop around 1 crossing both cuts).

This makes sense! The cut [1,∞] carries the monodromy of ∞, not of 1. The monodromy of 1 is the product of monodromies of the two cuts that meet at 1.

So the general rule is: if a cut goes from branch point a to branch point b, the monodromy of crossing this cut is the monodromy at b (the endpoint, not the starting point). Or maybe it's the monodromy at a. Let me reconsider.

With cuts [0,1] and [1,∞]:
- Cut [0,1]: connects 0 and 1. Monodromy = σ₀ (from loop around 0, which crosses only this cut).
- Cut [1,∞]: connects 1 and ∞. Monodromy = σ∞ (from loop around ∞, which crosses only this cut).
- Loop around 1 crosses both cuts: monodromy = σ₀ · σ∞ = σ₁. ✓

So the monodromy of a cut [a,b] is the monodromy of the branch point that is NOT shared with another cut. For [0,1], 0 is not shared (only 1 is shared with [1,∞]), so the monodromy is σ₀. For [1,∞], ∞ is not shared, so the monodromy is σ∞.

Alternatively: the monodromy of a cut [a,b] is σ_a if a is an endpoint that is only on this cut (not shared), and σ_b if b is only on this cut. If both endpoints are shared (on multiple cuts), then... well, in our case, 1 is shared between [0,1] and [1,∞], and its monodromy is the product of the two cut monodromies.

OK so the correct scheme for part (a) is:
- 4 sheets
- Cuts [0,1        — AI历史解题过程（thinking）
#   oda_math_460k_00056321         — 题目ID

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
  <problem_id>oda_math_460k_00056321</problem_id>
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

Determine the values of \(a \in \mathbb{R}\) for which the integral \(\int_{0}^{\frac{\pi}{2}} \log(\cos(x)) \cdot (\tan(x))^a \, dx\) converges.

## Standard Solution

<think>Okay, let's try to figure out for which real numbers \( a \) the integral \( \int_{0}^{\frac{\pi}{2}} \log(\cos(x)) \cdot (\tan(x))^a \, dx \) converges. Hmm, first, I need to recall that when dealing with convergence of integrals, especially improper integrals, we need to check the behavior near the endpoints where the integrand might be problematic. Here, the interval is from \( 0 \) to \( \frac{\pi}{2} \), so let's check the limits as \( x \) approaches \( 0 \) and as \( x \) approaches \( \frac{\pi}{2} \).

First, let's analyze the integrand \( f(x) = \log(\cos(x)) \cdot (\tan(x))^a \). Let's rewrite \( (\tan(x))^a \) as \( \sin^a(x)/\cos^a(x) \), so \( f(x) = \log(\cos(x)) \cdot \frac{\sin^a(x)}{\cos^a(x)} \). But maybe it's better to look at the behavior near each endpoint.

Starting with \( x \to 0^+ \). Let's see what happens to \( \cos(x) \) and \( \tan(x) \) here. As \( x \to 0 \), \( \cos(x) \approx 1 - x^2/2 \), so \( \log(\cos(x)) \approx \log(1 - x^2/2) \approx -x^2/2 \) (using the Taylor expansion \( \log(1 - \epsilon) \approx -\epsilon \) for small \( \epsilon \)). Then \( \tan(x) \approx x \), so \( (\tan(x))^a \approx x^a \). Therefore, near \( x = 0 \), the integrand behaves like \( (-x^2/2) \cdot x^a = -x^{a + 2}/2 \). The integral of \( x^{a + 2} \) near 0 converges as long as the exponent is greater than -1, right? Because \( \int x^b dx \) converges near 0 if \( b > -1 \). Wait, but here the integrand is \( x^{a + 2} \), so the integral from 0 to some small \( \epsilon \) would be \( \int_0^\epsilon x^{a + 2} dx \), which converges if \( a + 2 > -1 \)? Wait, no. Wait, the integral \( \int_0^\epsilon x^b dx \) converges (i.e., the limit as \( t \to 0^+ \) of \( \int_t^\epsilon x^b dx \) exists) if \( b > -1 \). Because \( \int x^b dx = x^{b + 1}/(b + 1) \), so as \( t \to 0 \), if \( b + 1 > 0 \), i.e., \( b > -1 \), then the integral converges. So here, the leading term is \( x^{a + 2} \), so \( b = a + 2 \). So we need \( a + 2 > -1 \)? Wait, no, wait. Wait, the integrand is \( \log(\cos x) \tan^a x \approx -x^2 \cdot x^a = -x^{a + 2} \). So the integrand behaves like \( x^{a + 2} \) near 0. The integral of \( x^{a + 2} \) from 0 to \( \epsilon \) converges if \( a + 2 > -1 \)? Wait, no, the integral \( \int_0^\epsilon x^b dx \) converges (i.e., the integral is finite) when \( b > -1 \). Because if \( b \geq -1 \), then the integral is finite. Wait, if \( b = -1 \), then \( \int x^{-1} dx = \log x \), which diverges as \( x \to 0 \). If \( b < -1 \), then \( x^b \) tends to infinity as \( x \to 0 \), and the integral diverges. So for \( \int_0^\epsilon x^b dx \) to converge, we need \( b > -1 \). So here, the exponent is \( a + 2 \), so we need \( a + 2 > -1 \)? Wait, no, wait. Wait, the integrand is \( x^{a + 2} \), so \( b = a + 2 \). So to have \( \int_0^\epsilon x^b dx \) converge, we need \( b > -1 \), so \( a + 2 > -1 \implies a > -3 \). But wait, but the integrand here is \( \log(\cos x) \tan^a x \approx -x^{a + 2} \), but actually, the logarithm term is \( \log(\cos x) \approx -x^2/2 \), which is a negative term, but the sign doesn't affect convergence, only the magnitude. So near 0, the integrand is \( O(x^{a + 2}) \), so the integral near 0 converges if \( a + 2 > -1 \), i.e., \( a > -3 \). Wait, but let's confirm. Let's take \( a = -4 \), then \( a + 2 = -2 \), so the integrand behaves like \( x^{-2} \), and \( \int x^{-2} dx \) from 0 to \( \epsilon \) is \( [-x^{-1}]_0^\epsilon \), which diverges. If \( a = -3 \), then \( a + 2 = -1 \), integrand behaves like \( x^{-1} \), integral \( \int x^{-1} dx \) diverges. If \( a = -2.5 \), then \( a + 2 = -0.5 \), integral \( \int x^{-0.5} dx \) converges (since \( -0.5 > -1 \)). So yes, near 0, the condition is \( a > -3 \).

Now, let's check the other endpoint, \( x \to (\pi/2)^- \). Let's set \( t = \pi/2 - x \), so as \( x \to \pi/2^- \), \( t \to 0^+ \). Then \( \cos(x) = \cos(\pi/2 - t) = \sin(t) \approx t \), so \( \log(\cos(x)) = \log(\sin t) \approx \log t \). \( \tan(x) = \tan(\pi/2 - t) = \cot t = 1/\tan t \approx 1/t \), so \( (\tan x)^a = (\cot t)^a = t^{-a} \). Therefore, the integrand becomes \( \log(\sin t) \cdot t^{-a} \). But \( \sin t \approx t \), so \( \log(\sin t) \approx \log t \). So the integrand near \( t \to 0^+ \) (i.e., \( x \to \pi/2^- \)) is approximately \( \log t \cdot t^{-a} \). Let's write that as \( t^{-a} \log t \). Now, we need to analyze the integral of \( t^{-a} \log t \) as \( t \to 0^+ \). Let's consider the behavior of \( t^{-a} \log t \). Let's set \( u = t \), so as \( u \to 0^+ \), \( \log u \to -\infty \), but \( u^{-a} \) is \( u^{-a} \). Let's see: if \( a < 0 \), then \( -a > 0 \), so \( u^{-a} = u^{|a|} \), which tends to 0, but multiplied by \( \log u \), which tends to -infty. Wait, but let's think in terms of convergence. Let's consider the integral \( \int_{0}^{\epsilon} t^{-a} \log t \, dt \). Let's make substitution \( s = - \log t \), so \( t = e^{-s} \), \( dt = -e^{-s} ds \). When \( t \to 0 \), \( s \to \infty \); when \( t = \epsilon \), \( s = -\log \epsilon \). Then the integral becomes \( \int_{s = \infty}^{s = -\log \epsilon} e^{a s} (-\log e^{-s}) (-e^{-s} ds) \). Wait, maybe that's complicating. Alternatively, let's consider the integral \( \int t^b \log t dt \), where \( b = -a \). Let's compute \( \int t^b \log t dt \). Integration by parts: let \( u = \log t \), \( dv = t^b dt \). Then \( du = (1/t) dt \), \( v = t^{b + 1}/(b + 1) \). So \( \int t^b \log t dt = (t^{b + 1}/(b + 1)) \log t - \int t^{b + 1}/(b + 1) \cdot (1/t) dt = (t^{b + 1}/(b + 1)) \log t - (1/(b + 1)) \int t^b dt = (t^{b + 1}/(b + 1)) \log t - t^{b + 1}/(b + 1)^2 + C \). Now, as \( t \to 0^+ \), what's the behavior of this expression? Let's see:

If \( b + 1 > 0 \), i.e., \( b > -1 \), then \( t^{b + 1} \to 0 \). Then \( (t^{b + 1}/(b + 1)) \log t \): since \( t^{b + 1} \to 0 \) and \( \log t \to -\infty \), but \( t^{b + 1} \) goes to 0 faster than \( \log t \) goes to -infty if \( b + 1 > 0 \). Let's check: \( t^{b + 1} \log t = e^{(b + 1) \log t} \log t \). Let \( u = \log t \), so as \( t \to 0^+ \), \( u \to -\infty \), then it's \( e^{(b + 1) u} u \). If \( b + 1 > 0 \), then \( (b + 1) u \to -\infty \), so \( e^{(b + 1) u} \to 0 \), and multiplied by \( u \to -\infty \), but the exponential decay dominates, so the whole term tends to 0. Therefore, the first term tends to 0, and the second term \( - t^{b + 1}/(b + 1)^2 \to 0 \). So the integral converges.

If \( b + 1 = 0 \), i.e., \( b = -1 \), then \( t^{b + 1} = t^0 = 1 \), so the first term is \( (1/(0)) \log t \), but wait, \( b = -1 \), so \( b + 1 = 0 \), so the original integral becomes \( \int t^{-1} \log t dt \). Let's compute that: \( \int (\log t)/t dt = (\log t)^2 / 2 + C \). As \( t \to 0^+ \), \( (\log t)^2 \to \infty \), so the integral diverges.

If \( b + 1 < 0 \), i.e., \( b < -1 \), then \( t^{b + 1} \to \infty \) as \( t \to 0^+ \). Then \( (t^{b + 1}/(b + 1)) \log t \): \( t^{b + 1} \to \infty \), \( \log t \to -\infty \), so the product is \( \infty \times (-\infty) = -\infty \). The second term \( - t^{b + 1}/(b + 1)^2 \): \( t^{b + 1} \to \infty \), and \( (b + 1)^2 > 0 \), so this term is \( -\infty \). So the entire expression tends to \( -\infty \), so the integral diverges.

But in our case, \( b = -a \), so:

The integral \( \int t^{-a} \log t dt \) near \( t \to 0^+ \) converges if and only if \( b > -1 \), i.e., \( -a > -1 \implies a < 1 \).

Wait, let's confirm. Let's recap:

We have \( b = -a \). The integral \( \int t^b \log t dt \) converges as \( t \to 0^+ \) iff \( b > -1 \). So \( -a > -1 \implies a < 1 \).

But let's check with specific values. Let's take \( a = 2 \), so \( b = -2 \). Then \( b = -2 < -1 \), so the integral should diverge. The integrand is \( t^{-2} \log t \), which as \( t \to 0 \), \( t^{-2} \) is \( 1/t^2 \), and \( \log t \to -\infty \), so the integrand tends to \( -\infty \), and the integral \( \int t^{-2} \log t dt \) would diverge. If \( a = 0.5 \), then \( b = -0.5 \), which is \( > -1 \). Then the integrand is \( t^{-0.5} \log t \), which as \( t \to 0 \), \( t^{-0.5} = 1/\sqrt{t} \), and \( \log t \to -\infty \), but \( 1/\sqrt{t} \log t \). Let's see, does the integral converge? Let's compute \( \int t^{-0.5} \log t dt \). Using the earlier formula, \( b = -0.5 \), so \( b + 1 = 0.5 > 0 \). Then the integral is \( (t^{0.5}/0.5) \log t - t^{0.5}/(0.5)^2 + C = 2 \sqrt{t} \log t - 4 \sqrt{t} + C \). As \( t \to 0 \), \( \sqrt{t} \log t \to 0 \) (since \( \sqrt{t} \to 0 \) and \( \log t \to -\infty \), but \( \sqrt{t} \) goes to 0 faster), so the first term tends to 0, the second term tends to 0, so the integral converges. So yes, when \( a < 1 \), the integral near \( x = \pi/2 \) converges.

If \( a = 1 \), then \( b = -1 \), so the integral becomes \( \int t^{-1} \log t dt \), which we saw diverges (since \( (\log t)^2 / 2 \to \infty \) as \( t \to 0 \)). If \( a > 1 \), then \( b = -a < -1 \), so the integral diverges. So the condition near \( x = \pi/2 \) is \( a < 1 \).

Now, we need both conditions: near \( x = 0 \), we need \( a > -3 \), and near \( x = \pi/2 \), we need \( a < 1 \). But wait, we also need to check if there are any other singularities in the interval. The integrand is defined on \( (0, \pi/2) \), since \( \cos x > 0 \) there, and \( \tan x \) is positive, so \( (\tan x)^a \) is defined for real \( a \) as long as \( \tan x > 0 \), which it is in \( (0, \pi/2) \). So the only singularities are at the endpoints.

But wait, let's confirm the behavior near \( x = 0 \) again. Let's be more precise. Let's expand \( \log(\cos x) \) more accurately. \( \cos x = 1 - x^2/2 + x^4/24 - \dots \), so \( \log(\cos x) = \log(1 - x^2/2 + x^4/24 - \dots) \approx -x^2/2 - x^4/12 - \dots \) (using \( \log(1 - y) \approx -y - y^2/2 - \dots \) for small \( y \)). So \( \log(\cos x) \approx -x^2/2 \) for small \( x \). Then \( (\tan x)^a = (x + x^3/3 + \dots)^a \approx x^a (1 + a x^2/3 + \dots) \). So the product \( \log(\cos x) (\tan x)^a \approx (-x^2/2) x^a (1 + \dots) = -x^{a + 2}/2 (1 + \dots) \). So the leading term is indeed \( -x^{a + 2}/2 \), so the integrand behaves like \( x^{a + 2} \) near 0. Therefore, the integral near 0 is dominated by \( \int x^{a + 2} dx \), which converges if \( a + 2 > -1 \implies a > -3 \). That seems correct.

Now, near \( x = \pi/2 \), we did the substitution \( t = \pi/2 - x \), so \( x = \pi/2 - t \), \( dx = -dt \), and as \( x \to \pi/2^- \), \( t \to 0^+ \). Then \( \cos x = \sin t \approx t - t^3/6 + \dots \), so \( \log(\cos x) = \log(\sin t) \approx \log t + \log(1 - t^2/6 + \dots) \approx \log t - t^2/6 + \dots \). But the leading term is \( \log t \). \( \tan x = \tan(\pi/2 - t) = \cot t = 1/\tan t \approx 1/t - t/3 + \dots \), so \( (\tan x)^a \approx (1/t)^a (1 - a t^2/3 + \dots) \). Therefore, the integrand \( \log(\cos x) (\tan x)^a \approx (\log t) t^{-a} (1 + \dots) \). So the leading term is \( t^{-a} \log t \), which is what we considered earlier. Therefore, the integral near \( x = \pi/2 \) is dominated by \( \int t^{-a} \log t dt \), which converges if \( -a > -1 \implies a < 1 \), as before.

Now, we need to check if there are any other issues. For example, what if \( a \) is such that the integrand is not defined? But in \( (0, \pi/2) \), \( \cos x > 0 \), \( \tan x > 0 \), so \( (\tan x)^a \) is defined for any real \( a \) (since it's \( e^{a \ln \tan x} \)), and \( \log(\cos x) \) is defined (since \( \cos x > 0 \)), so the integrand is defined everywhere on \( (0, \pi/2) \). The only possible issues are at the endpoints, which we already checked.

Now, we need to ensure that both conditions are satisfied: \( a > -3 \) and \( a < 1 \). So the integral converges if and only if \( -3 < a < 1 \).

Wait, but let's check the endpoints of this interval. What if \( a = -3 \)? Then near \( x = 0 \), the integrand behaves like \( x^{-3 + 2} = x^{-1} \), so \( \int x^{-1} dx \) diverges. So \( a = -3 \) is excluded. What if \( a = 1 \)? Near \( x = \pi/2 \), the integrand behaves like \( t^{-1} \log t \), and the integral \( \int t^{-1} \log t dt \) diverges (as we saw earlier, it's \( (\log t)^2 / 2 \), which tends to infinity as \( t \to 0 \)). So \( a = 1 \) is also excluded.

Is there any other point where the integrand might cause divergence? For example, what if \( a \) is negative? Let's say \( a = -2 \), which is between -3 and 1. Then near 0, \( a + 2 = 0 \), so the integrand behaves like \( x^0 = 1 \), so the integral near 0 is \( \int 1 dx \), which converges. Near \( \pi/2 \), \( a = -2 < 1 \), so \( -a = 2 > -1 \), so the integral near \( \pi/2 \) converges. So that's okay.

Another example: \( a = 0 \). Then the integrand is \( \log(\cos x) \), and the integral is \( \int_0^{\pi/2} \log(\cos x) dx \), which is a known integral (it's equal to \( -\pi/2 \log 2 \)), so it converges. That's within our interval.

What if \( a = -4 \), which is less than -3? Then near 0, \( a + 2 = -2 \), so the integrand behaves like \( x^{-2} \), integral diverges. So indeed, \( a < -3 \) is bad.

What if \( a = 2 \), which is greater than 1? Near \( \pi/2 \), \( a = 2 \), so \( -a = -2 < -1 \), integral diverges. So that's bad.

Therefore, combining both conditions, the integral converges if and only if \( -3 < a < 1 \).
</think>

To determine the values of \( a \in \mathbb{R} \) for which the integral \( \int_{0}^{\frac{\pi}{2}} \log(\cos(x)) \cdot (\tan(x))^a \, dx \) converges, we analyze the behavior of the integrand near the endpoints \( x = 0 \) and \( x = \frac{\pi}{2} \).

### Behavior near \( x \to 0^+ \):
As \( x \to 0 \), we use the approximations \( \cos(x) \approx 1 - \frac{x^2}{2} \) and \( \tan(x) \approx x \). Thus:
- \( \log(\cos(x)) \approx \log\left(1 - \frac{x^2}{2}\right) \approx -\frac{x^2}{2} \)
- \( (\tan(x))^a \approx x^a \)

The integrand behaves like \( -\frac{x^2}{2} \cdot x^a = -\frac{x^{a+2}}{2} \). The integral of \( x^{a+2} \) near \( 0 \) converges if the exponent \( a+2 > -1 \), i.e., \( a > -3 \).

### Behavior near \( x \to \frac{\pi}{2}^- \):
Let \( t = \frac{\pi}{2} - x \), so \( t \to 0^+ \) as \( x \to \frac{\pi}{2}^- \). Then:
- \( \cos(x) = \sin(t) \approx t \), so \( \log(\cos(x)) \approx \log(t) \)
- \( \tan(x) = \cot(t) \approx \frac{1}{t} \), so \( (\tan(x))^a \approx t^{-a} \)

The integrand behaves like \( \log(t) \cdot t^{-a} \). The integral of \( t^{-a} \log(t) \) near \( t \to 0^+ \) converges if \( -a > -1 \), i.e., \( a < 1 \).

### Combining Conditions:
The integral converges if both conditions are satisfied: \( a > -3 \) and \( a < 1 \).

Thus, the values of \( a \) for which the integral converges are \( -3 < a < 1 \).

\[
\boxed{(-3, 1)}
\]

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem. It's about drawing Riemann surface schemes for several multi-valued functions. Let me think about each one carefully.

The problem asks to draw the schemes (topological structure) of Riemann surfaces for:
a) √z + √(z-1)
b) ³√(z²-1) + √(1/z)
c) √z + ³√z
d) ⁴√(z²-1) + ⁴√(z-1)

For Riemann surfaces, I need to identify:
1. Branch points
2. Branch orders at each branch point
3. How sheets connect (the gluing/branching structure)
4. The total number of sheets
5. The genus (if relevant)

Let me work through each.

**Part a) √z + √(z-1)**

This is a sum of two square root functions. Let me think about this carefully.

w = √z + √(z-1)

The branch points of √z are at z=0 and z=∞.
The branch points of √(z-1) are at z=1 and z=∞.

So the combined function has branch points at z=0, z=1, and z=∞.

Now, the key question is whether the branch at ∞ is a true branch point of the combined function or whether it cancels.

Let me think about this more carefully. The function w = √z + √(z-1) is a multi-valued function. Let's think about what happens when we analytically continue around each branch point.

√z has 2 sheets, branching at 0 and ∞.
√(z-1) has 2 sheets, branching at 1 and ∞.

If these were independent, we'd have up to 4 sheets. But the function w = √z + √(z-1) might have fewer sheets due to algebraic relations.

Let me compute w²:
w² = z + (z-1) + 2√(z(z-1)) = 2z - 1 + 2√(z(z-1))

So (w² - 2z + 1)² = 4z(z-1) = 4z² - 4z

w⁴ - 2(2z-1)w² + (2z-1)² = 4z² - 4z
w⁴ - (4z-2)w² + (4z²-4z+1) = 4z² - 4z
w⁴ - (4z-2)w² + 1 = 0

So w satisfies the equation w⁴ - (4z-2)w² + 1 = 0.

This is a degree 4 polynomial in w, so generically there are 4 values of w for each z. So the Riemann surface has 4 sheets.

The branch points: from the equation w⁴ - (4z-2)w² + 1 = 0, the discriminant with respect to w tells us where sheets coalesce.

Let u = w², then u² - (4z-2)u + 1 = 0, so u = [(4z-2) ± √((4z-2)² - 4)] / 2.

The discriminant is (4z-2)² - 4 = 16z² - 16z + 4 - 4 = 16z² - 16z = 16z(z-1).

So u = [(4z-2) ± 4√(z(z-1))] / 2 = (2z-1) ± 2√(z(z-1)).

Then w = ±√u, so w = ±√((2z-1) ± 2√(z(z-1))).

The branch points of the Riemann surface are where the discriminant vanishes: z(z-1) = 0, i.e., z = 0 and z = 1. Also we need to check z = ∞ and where u = 0 (which would make w = 0 a branch point of the square root).

u = 0 when (2z-1) ± 2√(z(z-1)) = 0, i.e., (2z-1) = ∓2√(z(z-1)), so (2z-1)² = 4z(z-1), which gives 4z²-4z+1 = 4z²-4z, i.e., 1 = 0. This is impossible, so u never equals 0. Good, so no additional branch points from the square root of u.

Now let's check the branch at ∞. As z → ∞:
√z ≈ √z, √(z-1) ≈ √z(1 - 1/(2z) + ...) = √z - 1/(2√z) + ...

So w = √z + √(z-1) ≈ 2√z - 1/(2√z) + ... or w = √z - √(z-1) ≈ 1/(2√z) + ... (depending on sign choices).

Actually, let me be more careful. The four values of w are:
w₁ = √z + √(z-1) (both positive branches)
w₂ = √z - √(z-1) (positive √z, negative √(z-1))
w₃ = -√z + √(z-1) = -w₂
w₄ = -√z - √(z-1) = -w₁

As z → ∞:
w₁ ≈ 2√z → ∞
w₂ ≈ 1/(2√z) → 0
w₃ ≈ -1/(2√z) → 0
w₄ ≈ -2√z → -∞

Now, going around ∞ (which is the same as going around 0 and 1 in the opposite direction, or equivalently, a large loop encircling both 0 and 1):

Going around a large circle enclosing both 0 and 1: √z picks up a factor of -1 (since we go around 0 once), and √(z-1) also picks up a factor of -1 (since we go around 1 once).

So w₁ = √z + √(z-1) → -√z - √(z-1) = w₄
w₂ = √z - √(z-1) → -√z + √(z-1) = w₃
w₃ → w₂
w₄ → w₁

So going around ∞ swaps (w₁, w₄) and (w₂, w₃). This means ∞ IS a branch point, with two transpositions. The monodromy at ∞ is the product of two transpositions: (w₁ w₄)(w₂ w₃).

Now let's check the monodromy at z = 0:
Going around z = 0 (small loop): √z picks up factor -1, √(z-1) is unchanged (since 0 is not a branch point of √(z-1), and for z near 0, z-1 ≈ -1, which is away from the branch point at 1).

w₁ = √z + √(z-1) → -√z + √(z-1) = w₃
w₂ = √z - √(z-1) → -√z - √(z-1) = w₄
w₃ → w₁
w₄ → w₂

So monodromy at 0: (w₁ w₃)(w₂ w₄).

Monodromy at z = 1:
Going around z = 1: √(z-1) picks up factor -1, √z unchanged.

w₁ → √z - √(z-1) = w₂
w₂ → √z + √(z-1) = w₁
w₃ → -√z - √(z-1) = w₄
w₄ → -√z + √(z-1) = w₃

So monodromy at 1: (w₁ w₂)(w₃ w₄).

Let's verify: the product of monodromies at 0, 1, ∞ should be identity.
0: (w₁ w₃)(w₂ w₄)
1: (w₁ w₂)(w₃ w₄)
∞: (w₁ w₄)(w₂ w₃)

Product: Let's compute. Start with w₁.
After ∞: w₁ → w₄
After 1: w₄ → w₃
After 0: w₃ → w₁
So w₁ → w₁. ✓

Start with w₂:
After ∞: w₂ → w₃
After 1: w₃ → w₄
After 0: w₄ → w₂
So w₂ → w₂. ✓

Good, the product is identity.

So the Riemann surface of part (a) has:
- 4 sheets
- 3 branch points: z = 0, z = 1, z = ∞
- Each branch point has branch order 2 (simple branch point, connecting 2 pairs of sheets)
- Monodromy at 0: (1 3)(2 4)
- Monodromy at 1: (1 2)(3 4)
- Monodromy at ∞: (1 4)(2 3)

The genus: Using Riemann-Hurwitz. The covering has degree 4, base genus 0. Each branch point contributes 2 to the ramification (since each has two simple branch points, each contributing 1 to the Riemann-Hurwitz sum per sheet... wait, let me be more careful).

Actually, each branch point here has two transpositions, meaning two pairs of sheets are swapped. Each transposition corresponds to a simple ramification point (ramification index 2 for one point, contributing e-1 = 1 to the sum). With two transpositions at each branch point, each branch point contributes 2 to the total ramification sum.

Total ramification = 3 × 2 = 6.

Riemann-Hurwitz: 2g - 2 = n(2·0 - 2) + R = 4(-2) + 6 = -8 + 6 = -2.
So 2g = 0, g = 0.

The Riemann surface is a sphere (genus 0), with 4 sheets and 3 branch points, each connecting 2 pairs of sheets.

**Scheme description for (a):**
- 4 sheets labeled 1, 2, 3, 4
- Branch cut from 0 to 1: connects sheets (1,2) and (3,4) [based on monodromy at 0 and 1... actually, the branch cut structure depends on how we choose cuts]

Actually, let me think about the scheme more carefully in terms of branch cuts.

The standard way to describe the scheme: we choose branch cuts and describe how sheets are connected across them.

Let me choose branch cuts from 0 to 1, and from 1 to ∞ (or equivalently, from 0 to ∞ passing through 1, but that's not standard). Actually, let me choose:
- Cut 1: from 0 to 1
- Cut 2: from 1 to ∞ (i.e., from 1 along the positive real axis to +∞, or just a cut from 1 to ∞)

Hmm, actually, the standard approach for these problems is to describe the branch cuts and how sheets are glued.

Let me reconsider. The branch points are at 0, 1, ∞. We need to connect them with branch cuts. One natural choice:
- Cut A: from 0 to 1
- Cut B: from 1 to ∞

Across cut A (from 0 to 1): Going around 0 gives (1 3)(2 4), going around 1 gives (1 2)(3 4). The cut from 0 to 1 separates these. When we cross the cut from 0 to 1, the monodromy is the product of going around 0 (or equivalently, the monodromy associated with the cut).

Hmm, I think I'm overcomplicating this. Let me think about it differently.

Actually, for a cut from 0 to 1, crossing this cut corresponds to the monodromy of going around either 0 or 1 (they're on opposite sides). The monodromy of a loop around the cut [0,1] is the product of monodromies at 0 and 1... no, that's not right either.

Let me think again. If we have branch cuts from 0 to 1 and from 1 to ∞, then:
- Crossing the cut [0,1] corresponds to the monodromy of a loop that goes around 0 (but not 1) — this is (1 3)(2 4). Wait, no. If the cut goes from 0 to 1, then crossing it means going from one side to the other, which is equivalent to going around either 0 or 1 (depending on which part of the cut you cross).

Actually, the standard picture: if we have a cut from 0 to 1, then a loop crossing this cut and coming back on the other side is equivalent to going around either 0 or 1. The monodromy of crossing the cut [0,1] is the same as the monodromy at 0 (or equivalently at 1, since going around both 0 and 1 gives the monodromy at ∞, which is different).

Hmm, I think the cleanest way is:

For the cut from 0 to 1: a path that crosses this cut once and returns corresponds to going around 0 (if it crosses near 0) or around 1 (if it crosses near 1). But for a straight cut, crossing it anywhere gives the same monodromy, which is the monodromy of a loop around 0 (equivalently, around 1, since the cut connects them and the monodromy of going around the cut as a whole is the monodromy at ∞).

Wait, I need to be more careful. Let me think about this properly.

If we have cuts [0,1] and [1,∞], then the complement of these cuts in the sphere is simply connected. On this simply connected region, we can define single-valued branches. The monodromy when crossing a cut tells us how sheets are glued.

Crossing the cut [0,1]: This is equivalent to going around 0 (and not around ∞), or equivalently going around 1 (and not around ∞). But going around 0 gives monodromy (1 3)(2 4), and going around 1 gives (1 2)(3 4). These are different! So the cut [0,1] can't have a single monodromy...

Oh, I see the issue. The cut [0,1] connects two branch points with different monodromies. So crossing different parts of the cut gives different monodromies. This means we can't have a single cut from 0 to 1 with a uniform gluing.

The correct approach: we need separate cuts. Let me use:
- Cut from 0 to ∞ (not passing through 1)
- Cut from 1 to ∞ (not passing through 0)

Or more standardly:
- Cut from 0 to 1
- Cut from 1 to ∞

But the issue is that at z=1, both cuts meet, and the monodromy at 1 is (1 2)(3 4).

Actually, I think the standard way to handle this is: the cut from 0 to 1 carries the monodromy of going around 0 (which equals the monodromy of going around 1 times the monodromy of going around ∞, by the relation that the product of all monodromies is identity). No wait, the product of monodromies at 0, 1, ∞ is identity, so monodromy at 0 = (monodromy at 1)⁻¹ × (monodromy at ∞)⁻¹... no, monodromy at 0 × monodromy at 1 × monodromy at ∞ = identity.

So monodromy at 0 = (monodromy at 1 × monodromy at ∞)⁻¹ = (monodromy at ∞)⁻¹ × (monodromy at 1)⁻¹.

Since all our monodromies are involutions (products of disjoint transpositions), they're their own inverses.

monodromy at 0 = (1 3)(2 4) = (1 4)(2 3) × (1 2)(3 4) = monodromy at ∞ × monodromy at 1.

Let me verify: (1 4)(2 3) × (1 2)(3 4).
1 → (1 2) → 2 → (2 3) → 3. So 1 → 3.
3 → (3 4) → 4 → (1 4) → 1. So 3 → 1. Good, (1 3) ✓
2 → (1 2) → 1 → (1 4) → 4. So 2 → 4.
4 → (3 4) → 3 → (2 3) → 2. So 4 → 2. Good, (2 4) ✓

Great, so monodromy at 0 = monodromy at ∞ × monodromy at 1. This is consistent.

Now, for the scheme: we choose cuts and describe the gluing.

**Standard approach for the scheme:**

Let me use cuts [0,1] and [1,∞].

For the cut [0,1]: A loop going around this cut (encircling both 0 and 1 but not ∞) has monodromy = (monodromy at 0) × (monodromy at 1) = (1 3)(2 4) × (1 2)(3 4).

Let me compute: (1 3)(2 4) × (1 2)(3 4) (applying right to left):
1 → (1 2) → 2 → (2 4) → 4. So 1 → 4.
4 → (3 4) → 3 → (1 3) → 1. So 4 → 1. Good, (1 4).
2 → (1 2) → 1 → (1 3) → 3. So 2 → 3.
3 → (3 4) → 4 → (2 4) → 2. So 3 → 2. Good, (2 3).

So monodromy around the cut [0,1] = (1 4)(2 3) = monodromy at ∞. This makes sense! A loop around the cut [0,1] is the same as a loop around ∞ (in the opposite direction, but since these are involutions, direction doesn't matter).

So crossing the cut [0,1] gives monodromy (1 4)(2 3).
Crossing the cut [1,∞] gives monodromy at 1 = (1 2)(3 4).

Wait, but that's not quite right. Let me reconsider.

If we have cuts [0,1] and [1,∞], then:
- A loop around the cut [0,1] (encircling 0 and 1) gives monodromy = monodromy(0) × monodromy(1) = (1 4)(2 3).
- A loop around the cut [1,∞] (encircling 1 and ∞) gives monodromy = monodromy(1) × monodromy(∞) = (1 2)(3 4) × (1 4)(2 3).

Let me compute (1 2)(3 4) × (1 4)(2 3):
1 → (1 4) → 4 → (3 4) → 3. So 1 → 3.
3 → (2 3) → 2 → (1 2) → 1. So 3 → 1. Good, (1 3).
2 → (2 3) → 3 → (3 4) → 4. So 2 → 4.
4 → (1 4) → 1 → (1 2) → 2. So 4 → 2. Good, (2 4).

So monodromy around [1,∞] = (1 3)(2 4) = monodromy at 0. Makes sense.

But actually, I think the standard way to describe the scheme is not in terms of "loops around cuts" but in terms of how sheets are glued across each cut.

When we cross a cut, we move from one sheet to another. The gluing across a cut is determined by the monodromy of a path that crosses the cut once.

For the cut [0,1]: crossing it corresponds to going around 0 (or equivalently around 1, but these give different monodromies...). 

Hmm, I think the issue is that a cut from 0 to 1 doesn't have a well-defined single monodromy because 0 and 1 have different monodromies. The correct interpretation is:

If we cross the cut [0,1] near 0, we get monodromy at 0 = (1 3)(2 4).
If we cross the cut [0,1] near 1, we get monodromy at 1 = (1 2)(3 4).

But for a straight-line cut, the monodromy should be constant along the cut (for a simple branch point). The issue here is that each branch point has TWO transpositions, not one. So each branch point is actually a "double branch point" — it connects two pairs of sheets.

I think the correct picture is:

At z = 0: sheets 1↔3 and 2↔4 are connected (two branch points at z=0, each connecting one pair).
At z = 1: sheets 1↔2 and 3↔4 are connected.
At z = ∞: sheets 1↔4 and 2↔3 are connected.

For the scheme, we can describe it as follows:

Choose cuts [0,1] and [1,∞] (on the real axis).

Actually, I think for these problems, the standard approach in Russian textbooks (this looks like it's from a Russian textbook, probably Shabat or similar) is to describe the branch cuts and sheet connections.

Let me reconsider the problem. The "scheme" of a Riemann surface typically means:
1. The number of sheets
2. The branch points and their orders
3. How the sheets are connected (the branch cut structure)

Let me describe each part.

**Part a) √z + √(z-1)**

As computed: 4 sheets, branch points at 0, 1, ∞, each of order 2 (connecting 2 pairs of sheets).

The monodromy group is generated by:
- σ₀ = (1 3)(2 4) at z = 0
- σ₁ = (1 2)(3 4) at z = 1
- σ∞ = (1 4)(2 3) at z = ∞

The scheme: We can draw cuts from 0 to 1 and from 1 to ∞. 

Across the cut [0,1]: sheets are connected as 1↔3, 2↔4 (monodromy at 0) — wait, but crossing [0,1] should give a single monodromy. 

I think the issue is that with two transpositions at each branch point, we need to think of each branch point as two simple branch points. So at z=0, there are two branch points (one connecting 1↔3, one connecting 2↔4), both at z=0.

For the scheme, we can separate these. Let me choose:
- Cut from 0 to 1 for the pair (1,2)↔(3,4): i.e., at z=0, sheets 1↔3 and 2↔4 are connected; at z=1, sheets 1↔2 and 3↔4 are connected.

Actually, I think the standard way to describe this is:

The Riemann surface has 4 sheets. We make cuts [0,1] and [1,∞]. 

Across cut [0,1]: the connection is determined by the monodromy at 0 (going around 0). When we cross [0,1] (going around 0), sheets 1↔3 and 2↔4 swap.

Across cut [1,∞]: the connection is determined by the monodromy at 1 (going around 1). When we cross [1,∞] (going around 1), sheets 1↔2 and 3↔4 swap.

Wait, I need to think about this more carefully. If we have cuts [0,1] and [1,∞], then:
- Crossing [0,1] means going around 0 (but not 1 or ∞), which gives monodromy at 0.
- Crossing [1,∞] means going around 1 (but not 0 or ∞)... no, going around 1 and ∞.

Hmm, actually with cuts [0,1] and [1,∞], the point 1 is where the two cuts meet. A loop crossing [0,1] goes around 0 (and not 1 or ∞). A loop crossing [1,∞] goes around 1 and ∞ (and not 0). But monodromy(1) × monodromy(∞) = monodromy(0)⁻¹ = monodromy(0) (since it's an involution).

Hmm, this doesn't seem right. Let me think about it differently.

With cuts [0,1] and [1,∞] (both on the positive real axis, say), the complement is simply connected. On this region, we have 4 single-valued branches. Crossing a cut moves us to a different branch.

Crossing [0,1] from above to below: this is equivalent to going around 0 (a small loop around 0 crosses [0,1] twice, but going from above to below across [0,1] near 0 is half of such a loop). The monodromy is that of going around 0, which is (1 3)(2 4).

But wait, crossing [0,1] near 1 gives the monodromy of going around 1, which is (1 2)(3 4). So the monodromy is NOT constant along the cut [0,1]!

This means we can't use a single cut [0,1] with uniform gluing. We need to separate the branch points.

I think the correct approach is to use cuts that go from each finite branch point to ∞, or to use a different cut configuration.

Let me use cuts from 0 to ∞ and from 1 to ∞, not passing through each other. For example:
- Cut A: from 0 to ∞ along the negative real axis
- Cut B: from 1 to ∞ along the positive real axis

Then:
- Crossing cut A (from 0 to ∞) corresponds to going around 0, giving monodromy (1 3)(2 4).
- Crossing cut B (from 1 to ∞) corresponds to going around 1, giving monodromy (1 2)(3 4).

But each cut has two transpositions, meaning two pairs of sheets are swapped. This is fine — it just means the cut connects two pairs of sheets simultaneously.

So the scheme for (a):
- 4 sheets
- Cut from 0 to ∞: connects sheets 1↔3 and 2↔4
- Cut from 1 to ∞: connects sheets 1↔2 and 3↔4

At ∞, both cuts meet, and the combined monodromy is (1 3)(2 4) × (1 2)(3 4) = (1 4)(2 3), which is the monodromy at ∞. ✓

Actually, I realize I should think about this differently. In the standard treatment (e.g., in Shabat's book), the "scheme" of a Riemann surface is described by:
1. The number of sheets
2. The branch points
3. The branch cuts and how sheets are connected across them

For a function like √z + √(z-1), the standard approach would be:

Since w⁴ - (4z-2)w² + 1 = 0, this is a 4-sheeted surface. The branch points are at z = 0, 1, ∞, each with two simple branch points (order 2 each).

The scheme can be described as follows:
- 4 sheets
- Branch cuts: [0, ∞) and [1, ∞) (or [0,1] and [1,∞], etc.)
- At z = 0: sheets 1↔3 and 2↔4 are connected
- At z = 1: sheets 1↔2 and 3↔4 are connected
- At z = ∞: sheets 1↔4 and 2↔3 are connected

Genus 0.

OK let me now move on to the other parts and then write up the complete solution.

**Part b) ³√(z²-1) + √(1/z)**

w = ³√(z²-1) + √(1/z) = ³√(z²-1) + z^{-1/2}

Let me identify the branch points.

³√(z²-1) = ³√((z-1)(z+1)): branch points at z = 1, z = -1, and z = ∞.
- At z = 1: z²-1 has a simple zero, so ³√(z²-1) has a branch point of order 3.
- At z = -1: same, branch point of order 3.
- At z = ∞: z²-1 ~ z², so ³√(z²-1) ~ ³√(z²) = z^{2/3}. Going around ∞, z → ze^{2πi}, so z^{2/3} → z^{2/3} e^{4πi/3}. This is a non-trivial monodromy, so ∞ is a branch point of order 3.

√(1/z) = z^{-1/2}: branch points at z = 0 and z = ∞.
- At z = 0: branch point of order 2.
- At z = ∞: z^{-1/2} → (ze^{2πi})^{-1/2} = z^{-1/2} e^{-πi} = -z^{-1/2}. So ∞ is a branch point of order 2.

Now, the combined function w = ³√(z²-1) + z^{-1/2}.

The branch points are at z = -1, 0, 1, ∞.

Let me figure out the number of sheets. ³√(z²-1) has 3 values, z^{-1/2} has 2 values. If independent, 6 sheets. But they might not be independent.

Let me check: is there an algebraic relation that reduces the number of sheets?

Let u = ³√(z²-1), v = z^{-1/2}. Then w = u + v.
u³ = z² - 1, v² = 1/z, so z = 1/v², and u³ = 1/v⁴ - 1 = (1 - v⁴)/v⁴.

So u³v⁴ = 1 - v⁴, i.e., u³v⁴ + v⁴ = 1, v⁴(u³ + 1) = 1.

Also w = u + v, so u = w - v.
(w-v)³ v⁴ + v⁴ = 1
v⁴((w-v)³ + 1) = 1

This is a polynomial relation between w and v (and z = 1/v²). The degree in w is 3 (from (w-v)³), and the degree in v is... let me expand:
(w-v)³ = w³ - 3w²v + 3wv² - v³
So v⁴(w³ - 3w²v + 3wv² - v³ + 1) = 1
w³v⁴ - 3w²v⁵ + 3wv⁶ - v⁷ + v⁴ - 1 = 0

This is degree 3 in w and degree 7 in v. But we also have z = 1/v², so v = ±1/√z.

The number of sheets is the number of values of w for generic z. For generic z, u has 3 values and v has 2 values, giving 6 values of w = u + v. Are any of these equal? For generic z, u₁ + v₁ = u₂ + v₂ would require u₁ - u₂ = v₂ - v₁. Since u takes 3 values that are related by multiplication by cube roots of unity, and v takes 2 values that are negatives of each other, the differences u₁ - u₂ are generally not equal to ±(v₁ - v₂) for generic z. So we have 6 sheets.

Now let me determine the monodromy at each branch point.

Label the 6 sheets as (i, j) where i = 0, 1, 2 (for the 3 values of u = ³√(z²-1)) and j = 0, 1 (for the 2 values of v = z^{-1/2}).

The values are:
u_i = ωⁱ · u₀ where ω = e^{2πi/3}
v_j = (-1)^j · v₀

Sheet (i,j) corresponds to w = u_i + v_j = ωⁱ u₀ + (-1)^j v₀.

**Monodromy at z = 1:**
Going around z = 1: z²-1 = (z-1)(z+1) → (z-1) picks up e^{2πi}, so z²-1 → z²-1 (unchanged as a function, but the cube root...).

Wait, let me be more careful. Near z = 1, z²-1 ≈ 2(z-1). Going around z = 1, (z-1) → (z-1)e^{2πi}, so z²-1 → z²-1 · e^{2πi} = z²-1. But ³√(z²-1) → ³√(z²-1) · e^{2πi/3}. So u → u · ω, meaning u₀ → u₁ → u₂ → u₀.

Meanwhile, v = z^{-1/2} is unchanged (z = 1 is not a branch point of v, and near z = 1, z is away from 0).

So the monodromy at z = 1 is: (i, j) → (i+1 mod 3, j). This is a 3-cycle on the u-index: (0→1→2→0) for each j.

In terms of the 6 sheets (0,0), (1,0), (2,0), (0,1), (1,1), (2,1):
σ₁ = ((0,0) (1,0) (2,0)) ((0,1) (1,1) (2,1))

This is two 3-cycles. Each 3-cycle corresponds to a branch point of order 3.

**Monodromy at z = -1:**
Similarly, near z = -1, z²-1 ≈ -2(z+1). Going around z = -1, (z+1) → (z+1)e^{2πi}, so z²-1 → z²-1 · e^{2πi} = z²-1. And ³√(z²-1) → ³√(z²-1) · e^{2πi/3}.

Wait, that's the same as at z = 1. Let me double-check.

z²-1 = (z-1)(z+1). Near z = -1, z-1 ≈ -2 (constant), z+1 ≈ 0. So z²-1 ≈ -2(z+1). Going around z = -1: z+1 → (z+1)e^{2πi}, so z²-1 → -2(z+1)e^{2πi} = z²-1 · e^{2πi}. So ³√(z²-1) → ³√(z²-1) · e^{2πi/3}.

v = z^{-1/2} is unchanged near z = -1 (z ≈ -1, away from 0).

So monodromy at z = -1 is the same as at z = 1: (i, j) → (i+1 mod 3, j).

Hmm, but that would mean the product of monodromies at -1 and 1 is (i → i+2 mod 3, j → j), which is also a 3-cycle (the inverse). And then the monodromy at 0 and ∞ together must give (i → i+1 mod 3, j → j) to make the total product identity.

Wait, let me reconsider. The product of ALL monodromies must be identity. The branch points are -1, 0, 1, ∞.

σ_{-1} = (i → i+1, j → j) [3-cycle on u]
σ₀ = (i → i, j → j+1 mod 2) [2-cycle on v, since going around 0: z → ze^{2πi}, z^{-1/2} → z^{-1/2}e^{-πi} = -z^{-1/2}, so v → -v, meaning j → j+1 mod 2. And u = ³√(z²-1) is unchanged since z²-1 is unchanged when z → ze^{2πi}... wait, z² → z²e^{4πi} = z², so z²-1 → z²-1. So u is unchanged.]

σ₁ = (i → i+1, j → j) [3-cycle on u]
σ∞ = ?

Product must be identity: σ_{-1} · σ₀ · σ₁ · σ∞ = id.

σ_{-1} · σ₁ = (i → i+2, j → j) [since each adds 1 to i]
σ_{-1} · σ₀ · σ₁ = (i → i+2, j → j+1)

So σ∞ = (i → i+1, j → j+1) [to make the product identity: (i+2+1, j+1+1) = (i, j) ✓ since i+3 ≡ i mod 3 and j+2 ≡ j mod 2]

Let me verify σ∞ directly. At z = ∞, going around ∞ means z → ze^{-2πi} (or equivalently, a large loop clockwise). Let's use z → ze^{2πi} (counterclockwise around 0, which is clockwise around ∞ on the sphere).

u = ³√(z²-1) ~ ³√(z²) = z^{2/3}. z → ze^{2πi}, so z^{2/3} → z^{2/3} e^{4πi/3} = u · ω². So i → i+2 mod 3.

v = z^{-1/2}. z → ze^{2πi}, so z^{-1/2} → z^{-1/2} e^{-πi} = -v. So j → j+1 mod 2.

So σ∞ = (i → i+2, j → j+1).

But I computed σ∞ = (i → i+1, j → j+1) from the product condition. Let me recheck.

The product of monodromies around all branch points (in order around the sphere) must be identity. The order matters. Let me be more careful.

On the Riemann sphere, if we list the branch points in order (say counterclockwise), the product of monodromies (in the right order) is identity. But the order and direction matter.

Let me just directly compute all monodromies and verify.

σ_{-1}: z → z (loop around -1), u → u·ω (i → i+1), v → v (j → j). So σ_{-1} = (i+1, j).
σ₀: z → ze^{2πi} (loop around 0), u → u (i → i, since z²-1 → z²-1), v → -v (j → j+1). So σ₀ = (i, j+1).
σ₁: z → z (loop around 1), u → u·ω (i → i+1), v → v (j → j). So σ₁ = (i+1, j).
σ∞: z → ze^{2πi} (loop around ∞ = loop around 0, but we need to be careful about direction).

Actually, a loop around ∞ counterclockwise (on the sphere) corresponds to a loop around 0 clockwise (in the plane), i.e., z → ze^{-2πi}.

With z → ze^{-2πi}:
u ~ z^{2/3} → z^{2/3} e^{-4πi/3} = u · ω (since e^{-4πi/3} = e^{2πi/3} = ω). So i → i+1.
v = z^{-1/2} → z^{-1/2} e^{πi} = -v. So j → j+1.

So σ∞ = (i+1, j+1).

Now the product: σ_{-1} · σ₀ · σ₁ · σ∞ = (i+1, j) · (i, j+1) · (i+1, j) · (i+1, j+1).

Applying right to left:
Start: (i, j)
After σ∞: (i+1, j+1)
After σ₁: (i+2, j+1)
After σ₀: (i+2, j+2) = (i+2, j) [since j+2 ≡ j mod 2]
After σ_{-1}: (i+3, j) = (i, j) ✓

Great, the product is identity.

So the monodromies are:
- σ_{-1} = (i → i+1, j → j): two 3-cycles
- σ₀ = (i → i, j → j+1): three 2-cycles
- σ₁ = (i → i+1, j → j): two 3-cycles
- σ∞ = (i → i+1, j → j+1): one 6-cycle

Let me verify σ∞ is a 6-cycle. The permutation (i → i+1 mod 3, j → j+1 mod 2) on 6 elements:
(0,0) → (1,1) → (2,0) → (0,1) → (1,0) → (2,1) → (0,0). Yes, it's a single 6-cycle!

So the Riemann surface for (b) has:
- 6 sheets
- Branch points at z = -1, 0, 1, ∞
- At z = -1: two 3-cycles (branch order 3, two branch points)
- At z = 0: three 2-cycles (branch order 2, three branch points)
- At z = 1: two 3-cycles (branch order 3, two branch points)
- At z = ∞: one 6-cycle (branch order 6, one branch point)

Genus by Riemann-Hurwitz:
2g - 2 = 6(-2) + R
R = sum of (e_p - 1) over all ramification points.

At z = -1: two 3-cycles, each contributes (3-1) = 2, total 4.
At z = 0: three 2-cycles, each contributes (2-1) = 1, total 3.
At z = 1: two 3-cycles, each contributes (3-1) = 2, total 4.
At z = ∞: one 6-cycle, contributes (6-1) = 5, total 5.

R = 4 + 3 + 4 + 5 = 16.
2g - 2 = -12 + 16 = 4.
2g = 6, g = 3.

So the Riemann surface has genus 3.

**Scheme for (b):**
- 6 sheets, labeled (i, j) with i = 0,1,2 and j = 0,1
- Branch points: -1, 0, 1, ∞
- At z = -1: 3-cycles on i (u-branch), j fixed. Two cycles: (0,0)→(1,0)→(2,0) and (0,1)→(1,1)→(2,1)
- At z = 0: 2-cycles on j (v-branch), i fixed. Three cycles: (0,0)↔(0,1), (1,0)↔(1,1), (2,0)↔(2,1)
- At z = 1: same as z = -1
- At z = ∞: 6-cycle (0,0)→(1,1)→(2,0)→(0,1)→(1,0)→(2,1)→(0,0)

For the branch cut scheme, we can choose:
- Cut from -1 to 1 (passing through 0, or we can use separate cuts)
- Cut from 1 to ∞

Or more naturally:
- Cut from -1 to 0 (for the v-branch at 0 and u-branch at -1)
- Cut from 0 to 1 (for the v-branch at 0 and u-branch at 1)
- Cut from 1 to ∞ (for the branch at ∞)

Actually, let me think about this more carefully. The standard way is:

For ³√(z²-1): branch cuts from -1 to 1 (or from -1 to -∞ and 1 to ∞, etc.). With a cut from -1 to 1, the function ³√(z²-1) is single-valued on the complement. The 3 sheets are connected via 3-cycles at -1 and 1.

For √(1/z) = z^{-1/2}: branch cut from 0 to ∞. The 2 sheets are connected via a 2-cycle at 0 (and at ∞).

But the combined function has interactions at ∞. Let me think about the cuts.

Actually, for the scheme, I think the clearest description is:

Choose cuts:
- [-1, 0]: crossing this cut swaps u-index (3-cycle) and v-index (2-cycle)... no, that's not right.

Hmm, let me think about this differently. The cuts should be chosen so that each cut has a well-defined monodromy.

Since the branch points -1, 0, 1, ∞ have monodromies:
- σ_{-1} = (i+1, j): acts on u only
- σ₀ = (i, j+1): acts on v only
- σ₁ = (i+1, j): acts on u only
- σ∞ = (i+1, j+1): acts on both

If we choose cuts from -1 to ∞ and from 0 to ∞ and from 1 to ∞ (all going to ∞), then:
- Crossing cut [-1, ∞]: monodromy σ_{-1} = (i+1, j)
- Crossing cut [0, ∞]: monodromy σ₀ = (i, j+1)
- Crossing cut [1, ∞]: monodromy σ₁ = (i+1, j)

At ∞, all three cuts meet, and the combined monodromy is σ_{-1} · σ₀ · σ₁ = (i+2, j+1). But σ∞ = (i+1, j+1). These don't match, which means... hmm.

Actually, the monodromy at ∞ should be the product of the monodromies at the finite branch points (in the right order). Going around ∞ counterclockwise (on the sphere) = going around all finite branch points clockwise. So σ∞ = (σ_{-1} · σ₀ · σ₁)^{-1} = (i+2, j+1)^{-1} = (i-2, j-1) = (i+1, j+1) [since -2 ≡ 1 mod 3 and -1 ≡ 1 mod 2]. So σ∞ = (i+1, j+1). ✓

OK so the scheme with cuts to ∞ works. But having three cuts all going to ∞ is a bit unusual. Let me use a different configuration.

Alternative: cuts [-1, 0], [0, 1], [1, ∞].
- Crossing [-1, 0]: monodromy = σ_{-1} = (i+1, j) [going around -1]
- Crossing [0, 1]: monodromy = σ₀ = (i, j+1) [going around 0]
- Crossing [1, ∞]: monodromy = σ₁ = (i+1, j) [going around 1]

At ∞: σ∞ = (σ_{-1} · σ₀ · σ₁)^{-1} = (i+1, j+1). ✓

This works! Each cut has a well-defined monodromy.

So the scheme for (b):
- 6 sheets labeled (i,j), i∈{0,1,2}, j∈{0,1}
- Cut [-1, 0]: 3-cycles on i (sheets (0,j)→(1,j)→(2,j)→(0,j) for j=0,1)
- Cut [0, 1]: 2-cycles on j (sheets (i,0)↔(i,1) for i=0,1,2)
- Cut [1, ∞]: 3-cycles on i (same as cut [-1, 0])
- At ∞: 6-cycle

Genus 3.

**Part c) √z + ³√z**

w = √z + ³√z = z^{1/2} + z^{1/3}

Let u = z^{1/2} (2 values), v = z^{1/3} (3 values). w = u + v.

Branch points: z = 0 and z = ∞ (both u and v branch at these points).

Number of sheets: u has 2 values, v has 3 values. If independent, 6 sheets. But are they independent?

u² = z, v³ = z, so u² = v³. This means u = v^{3/2}... hmm, but u and v are both determined by z. Actually, u = z^{1/2} and v = z^{1/3}, so u = v^{3/2} and v = u^{2/3}. The relation u² = v³ constrains them.

Given z, u = ±√z (2 choices), v = ³√z (3 choices). But u² = v³ = z. So once we pick v, u is determined up to sign: u = ±√(v³). But √(v³) = v^{3/2}, and v is a cube root of z, so v³ = z, and √(v³) = √z = u. So u = ±√z regardless of which v we pick. The choice of v doesn't constrain u.

Wait, but u² = v³ = z. So for a given z, u = ±√z and v = ωⁱ ³√z for i = 0, 1, 2. These are independent choices (2 × 3 = 6). So we have 6 sheets.

But wait, is there an algebraic relation between w and z that has degree less than 6?

w = u + v, u² = z, v³ = z. So u = w - v, (w-v)² = z, v³ = z. From v³ = z, (w-v)² = v³. So w² - 2wv + v² = v³, i.e., v³ - v² + 2wv - w² = 0. This is degree 3 in v and degree 2 in w. The resultant in v would give a polynomial in w of degree... let me think.

From v³ = z and (w-v)² = z, we get v³ = (w-v)². So v³ - (w-v)² = 0, i.e., v³ - w² + 2wv - v² = 0.

This is a cubic in v: v³ - v² + 2wv - w² = 0.

For each w, this gives up to 3 values of v, and then z = v³. But we want, for each z, the number of w values. 

Alternatively, from u² = z and v³ = z, w = u + v. The number of (u,v) pairs for given z is 2 × 3 = 6 (since u and v are independent). Each gives a w = u + v. Are any two w values equal? u₁ + v₁ = u₂ + v₂ requires u₁ - u₂ = v₂ - v₁. For generic z, the 2 values of u are ±√z and the 3 values of v are ωⁱ ³√z. The differences u₁ - u₂ are 0 or ±2√z. The differences v₂ - v₁ are 0 or (ω-1)³√z or (ω²-1)³√z or (ω²-ω)³√z. For these to be equal (for generic z), we'd need ±2√z = c · ³√z for some constant c, i.e., ±2z^{1/2} = c·z^{1/3}, i.e., ±2z^{1/6} = c. This only holds for specific z, not generically. So for generic z, all 6 values are distinct. 6 sheets.

Now the monodromy. Label sheets (i, j) where i = 0, 1 (for u = (-1)^i √z) and j = 0, 1, 2 (for v = ω^j ³√z).

**Monodromy at z = 0:**
Going around 0: z → ze^{2πi}.
u = z^{1/2} → z^{1/2} e^{πi} = -u. So i → i+1 mod 2.
v = z^{1/3} → z^{1/3} e^{2πi/3} = v · ω. So j → j+1 mod 3.

σ₀ = (i → i+1 mod 2, j → j+1 mod 3).

This is a single 6-cycle! Let me verify:
(0,0) → (1,1) → (0,2) → (1,0) → (0,1) → (1,2) → (0,0). Yes, 6-cycle.

**Monodromy at z = ∞:**
Going around ∞ (counterclockwise on sphere) = z → ze^{-2πi}.
u = z^{1/2} → z^{1/2} e^{-πi} = -u. So i → i+1 mod 2.
v = z^{1/3} → z^{1/3} e^{-2πi/3} = v · ω². So j → j+2 mod 3 = j-1 mod 3.

σ∞ = (i → i+1 mod 2, j → j-1 mod 3).

Let me verify the product σ₀ · σ∞ = identity:
σ₀: (i+1, j+1), σ∞: (i+1, j-1).
Product (right to left): (i, j) → σ∞ → (i+1, j-1) → σ₀ → (i+2, j) = (i, j) [since i+2 ≡ i mod 2]. ✓

So σ∞ = (i+1, j-1). Let me trace the cycle:
(0,0) → (1,2) → (0,1) → (1,0) → (0,2) → (1,1) → (0,0). Also a 6-cycle.

So the Riemann surface for (c) has:
- 6 sheets
- 2 branch points: z = 0 and z = ∞
- At z = 0: one 6-cycle (branch order 6)
- At z = ∞: one 6-cycle (branch order 6)

Genus by Riemann-Hurwitz:
2g - 2 = 6(-2) + R
R = (6-1) + (6-1) = 10.
2g - 2 = -12 + 10 = -2.
2g = 0, g = 0.

Genus 0.

**Scheme for (c):**
- 6 sheets
- Branch cut from 0 to ∞
- Crossing the cut: 6-cycle (0,0)→(1,1)→(0,2)→(1,0)→(0,1)→(1,2)→(0,0)
- At both 0 and ∞: branch order 6

This is a cyclic 6-sheeted cover of the sphere, branched at 0 and ∞.

**Part d) ⁴√(z²-1) + ⁴√(z-1)**

w = ⁴√(z²-1) + ⁴√(z-1) = ⁴√((z-1)(z+1)) + ⁴√(z-1)

Let u = ⁴√(z²-1) = ⁴√((z-1)(z+1)), v = ⁴√(z-1).

u⁴ = z² - 1 = (z-1)(z+1), v⁴ = z - 1.

So u⁴ = v⁴(z+1), i.e., u⁴/v⁴ = z+1, (u/v)⁴ = z+1.

Also z = v⁴ + 1, so u⁴ = (v⁴+1)² - 1 = v⁸ + 2v⁴ = v⁴(v⁴ + 2).
So u = v · ⁴√(v⁴ + 2).

w = u + v = v(⁴√(v⁴ + 2) + 1).

Number of sheets: u has 4 values, v has 4 values. But u⁴ = v⁴(z+1), so given v, u⁴ = v⁴(z+1) = v⁴(v⁴+2). So u = v · ⁴√(v⁴+2), which has 4 values. But v itself has 4 values. So total: 4 × 4 = 16? But we need to check if the relation u⁴ = v⁴(z+1) reduces this.

Given z, v = ⁴√(z-1) has 4 values: v_k = ζ^k · v₀ where ζ = e^{2πi/4} = i, k = 0,1,2,3.
Given v, u = ⁴√(v⁴(z+1)) = ⁴√(v⁴ · (v⁴+2)) = v · ⁴√(v⁴+2). But v⁴ = z-1, so u = ⁴√((z-1)(z+1)) = ⁴√(z²-1), which has 4 values: u_m = ζ^m · u₀.

Are u and v independent? u⁴ = (z-1)(z+1) = v⁴(z+1). So u⁴ = v⁴(z+1). Given z, v is one of 4 values, and u is one of 4 values, with the constraint u⁴ = v⁴(z+1). But v⁴ = z-1 for all 4 values of v (since (ζ^k v₀)⁴ = ζ^{4k} v₀⁴ = v₀⁴ = z-1). So u⁴ = (z-1)(z+1) = z²-1 regardless of which v we pick. So u and v are indeed independent: 4 × 4 = 16 sheets.

Wait, but that seems like a lot. Let me double-check by finding the algebraic equation.

w = u + v, u⁴ = z²-1, v⁴ = z-1.
u = w - v, (w-v)⁴ = z²-1, v⁴ = z-1.
z = v⁴ + 1, (w-v)⁴ = (v⁴+1)² - 1 = v⁸ + 2v⁴.

So (w-v)⁴ = v⁸ + 2v⁴ = v⁴(v⁴+2).

This is degree 4 in w and degree 8 in v. The number of (w, v) pairs for given z is... for given z, v has 4 values, and for each v, w = v + u where u has 4 values, giving 4 w values. So 16 values of w.

But are all 16 distinct? For generic z, yes (by a similar argument as before).

Hmm, but 16 sheets seems like a lot. Let me reconsider.

Actually, wait. Let me reconsider whether u and v are truly independent. We have u⁴ = z²-1 and v⁴ = z-1. Note that z²-1 = (z-1)(z+1) = v⁴(v⁴+2). So u⁴ = v⁴(v⁴+2), which means (u/v)⁴ = v⁴+2 = z+1. So u/v = ⁴√(z+1), which has 4 values. And v = ⁴√(z-1) has 4 values. So w = u + v = v(⁴√(z+1) + 1).

Let me set a = ⁴√(z+1) (4 values) and b = ⁴√(z-1) (4 values). Then u = ab and v = b, so w = b(a+1).

Are a and b independent? a⁴ = z+1, b⁴ = z-1. These are independent (different functions of z). So 4 × 4 = 16 values of w = b(a+1).

For generic z, are all 16 values distinct? w = b(a+1) where a = ζ^i a₀, b = ζ^j b₀. w_{ij} = ζ^j b₀ (ζ^i a₀ + 1). For w_{ij} = w_{kl}, we need ζ^j b₀(ζ^i a₀ + 1) = ζ^l b₀(ζ^k a₀ + 1), i.e., ζ^j(ζ^i a₀ + 1) = ζ^l(ζ^k a₀ + 1). For generic a₀, this requires j = l and i = k. So yes, 16 distinct values.

So 16 sheets. That's a lot. Let me reconsider...

Actually, I wonder if the problem is asking for something simpler. Let me re-read the problem.

"Draw the schemes of the Riemann surfaces of the following functions"

OK so it's asking for the scheme (topological structure) of each Riemann surface. For part (d), 16 sheets is correct if u and v are independent.

Let me identify the branch points.

u = ⁴√(z²-1) = ⁴√((z-1)(z+1)):
- z = 1: z²-1 has a simple zero, so ⁴√(z²-1) has a branch point of order 4.
- z = -1: same, branch point of order 4.
- z = ∞: z²-1 ~ z², ⁴√(z²-1) ~ z^{1/2}. Going around ∞: z → ze^{2πi}, z^{1/2} → -z^{1/2}. So branch point of order 2 (since z^{1/2} has period 2 under z → ze^{2πi}).

Wait, let me be more careful. ⁴√(z²) = z^{2/4} = z^{1/2}. Going around ∞ (z → ze^{2πi}): z^{1/2} → z^{1/2} e^{πi} = -z^{1/2}. So the monodromy is of order 2 (going around twice gives identity). So at ∞, u has a branch point of order 2 (not 4).

v = ⁴√(z-1):
- z = 1: branch point of order 4.
- z = ∞: ⁴√(z-1) ~ z^{1/4}. Going around ∞: z → ze^{2πi}, z^{1/4} → z^{1/4} e^{πi/2} = iz^{1/4}. So branch point of order 4.

So the branch points are: z = -1, 1, ∞.

At z = 1: both u and v branch. u has order 4, v has order 4.
At z = -1: only u branches, order 4.
At z = ∞: u has order 2, v has order 4.

Let me work out the monodromies.

Label sheets as (i, j) where i = 0,1,2,3 (for u = ζ^i u₀, ζ = i = e^{2πi/4}) and j = 0,1,2,3 (for v = ζ^j v₀).

**Monodromy at z = 1:**
Near z = 1: z²-1 ≈ 2(z-1), z-1 ≈ (z-1).
Going around z = 1: (z-1) → (z-1)e^{2πi}.
u = ⁴√(z²-1) ≈ ⁴√(2(z-1)) → ⁴√(2(z-1)) · e^{2πi/4} = u · ζ. So i → i+1 mod 4.
v = ⁴√(z-1) → ⁴√(z-1) · e^{2πi/4} = v · ζ. So j → j+1 mod 4.

σ₁ = (i → i+1, j → j+1).

This is a permutation on 16 elements. Let me trace the cycles:
(0,0) → (1,1) → (2,2) → (3,3) → (0,0): 4-cycle.
(0,1) → (1,2) → (2,3) → (3,0) → (0,1): 4-cycle.
(0,2) → (1,3) → (2,0) → (3,1) → (0,2): 4-cycle.
(0,3) → (1,0) → (2,1) → (3,2) → (0,3): 4-cycle.

So σ₁ consists of four 4-cycles.

**Monodromy at z = -1:**
Near z = -1: z²-1 ≈ -2(z+1), z-1 ≈ -2 (constant).
Going around z = -1: (z+1) → (z+1)e^{2πi}.
u = ⁴√(z²-1) ≈ ⁴√(-2(z+1)) → u · e^{2πi/4} = u · ζ. So i → i+1 mod 4.
v = ⁴√(z-1) is unchanged (z-1 ≈ -2, not near 0). So j → j.

σ_{-1} = (i → i+1, j → j).

Cycles: for each j, (0,j) → (1,j) → (2,j) → (3,j) → (0,j). Four 4-cycles.

**Monodromy at z = ∞:**
Going around ∞ (counterclockwise on sphere) = z → ze^{-2πi}.
u ~ z^{1/2} → z^{1/2} e^{-πi} = -u. So i → i+2 mod 4 (since -1 = ζ²).
v ~ z^{1/4} → z^{1/4} e^{-πi/2} = v · ζ^{-1} = v · ζ³. So j → j+3 mod 4 = j-1 mod 4.

σ∞ = (i → i+2, j → j-1).

Let me verify the product: σ_{-1} · σ₁ · σ∞ = identity.
σ_{-1}: (i+1, j)
σ₁: (i+1, j+1)
σ∞: (i+2, j-1)

Product (right to left): (i,j) → σ∞ → (i+2, j-1) → σ₁ → (i+3, j) → σ_{-1} → (i+4, j) = (i, j). ✓

Now let me trace the cycles of σ∞ = (i+2, j-1):
(0,0) → (2,3) → (0,2) → (2,1) → (0,0): 4-cycle.
(0,1) → (2,0) → (0,3) → (2,2) → (0,1): 4-cycle.
(1,0) → (3,3) → (1,2) → (3,1) → (1,0): 4-cycle.
(1,1) → (3,0) → (1,3) → (3,2) → (1,1): 4-cycle.

So σ∞ also consists of four 4-cycles.

Genus by Riemann-Hurwitz:
2g - 2 = 16(-2) + R

R = sum of (e-1) over all ramification points.
At z = -1: four 4-cycles, each contributes (4-1) = 3, total 12.
At z = 1: four 4-cycles, each contributes (4-1) = 3, total 12.
At z = ∞: four 4-cycles, each contributes (4-1) = 3, total 12.

R = 12 + 12 + 12 = 36.
2g - 2 = -32 + 36 = 4.
2g = 6, g = 3.

Genus 3.

**Scheme for (d):**
- 16 sheets labeled (i, j), i, j ∈ {0,1,2,3}
- Branch points: -1, 1, ∞
- At z = -1: four 4-cycles, (i → i+1, j fixed)
- At z = 1: four 4-cycles, (i → i+1, j → j+1)
- At z = ∞: four 4-cycles, (i → i+2, j → j-1)

For cuts: [-1, 0] (or [-1, 1]), [1, ∞].

Actually, let me choose cuts [-1, 1] and [1, ∞].
- Crossing [-1, 1]: monodromy = σ_{-1} = (i+1, j) [going around -1]
- Crossing [1, ∞]: monodromy = σ₁ = (i+1, j+1) [going around 1]

At ∞: σ∞ = (σ_{-1} · σ₁)^{-1} = ((i+2, j+1))^{-1} = (i-2, j-1) = (i+2, j-1). ✓

Hmm wait, I need to be more careful about which monodromy corresponds to which cut.

With cuts [-1, 1] and [1, ∞]:
- Crossing [-1, 1] near -1: going around -1, monodromy σ_{-1} = (i+1, j).
- Crossing [-1, 1] near 1: going around 1, monodromy σ₁ = (i+1, j+1).

But these are different! So the cut [-1, 1] doesn't have a uniform monodromy. This is the same issue as in part (a).

The issue is that -1 and 1 have different monodromies, so a cut connecting them doesn't have a single monodromy. We need cuts from each branch point to ∞ (or some other configuration where each cut has a single monodromy).

Let me use cuts from -1 to ∞ and from 1 to ∞ (not passing through each other).
- Crossing cut [-1, ∞]: monodromy σ_{-1} = (i+1, j)
- Crossing cut [1, ∞]: monodromy σ₁ = (i+1, j+1)

At ∞: σ∞ = (σ_{-1} · σ₁)^{-1} = (i+2, j+1)^{-1} = (i+2, j-1). ✓

This works. Each cut has a well-defined monodromy.

Now let me write up the complete solution.

Actually, let me reconsider the problem. It says "draw the schemes." In the context of a textbook problem (likely from Shabat's "Introduction to Complex Analysis"), the "scheme" of a Riemann surface refers to a picture showing:
1. The number of sheets
2. The branch cuts
3. How sheets are connected across the cuts

Since I can't actually draw pictures, I'll describe the schemes in detail.

Let me also double-check my work on part (a) regarding the genus and the structure.

For part (a), I found genus 0, 4 sheets, 3 branch points each with two 2-cycles. Let me reconsider the cut structure.

For part (a), the monodromies are:
- σ₀ = (1 3)(2 4) at z = 0
- σ₁ = (1 2)(3 4) at z = 1
- σ∞ = (1 4)(2 3) at z = ∞

With cuts [0, ∞) and [1, ∞):
- Crossing [0, ∞): σ₀ = (1 3)(2 4)
- Crossing [1, ∞): σ₁ = (1 2)(3 4)
- At ∞: σ∞ = (σ₀ · σ₁)^{-1} = ((1 3)(2 4) · (1 2)(3 4))^{-1} = (1 4)(2 3)^{-1} = (1 4)(2 3). ✓

So the scheme for (a):
- 4 sheets
- Cut from 0 to ∞: connects sheets 1↔3 and 2↔4
- Cut from 1 to ∞: connects sheets 1↔2 and 3↔4

Now let me write up the full solution.

Actually, let me reconsider whether I should present the cuts differently. In many textbooks, the scheme is presented with cuts between finite branch points when possible, and cuts to ∞ otherwise.

For part (a), we could also use a cut [0,1] and a cut [1,∞]. But as I noted, the cut [0,1] doesn't have a uniform monodromy since 0 and 1 have different monodromies. However, in the standard treatment, when we have a cut between two branch points, the monodromy of crossing the cut is well-defined: it's the monodromy of going around one of the branch points (say the one on the left), and the other branch point's monodromy is "absorbed" into the other cut.

Actually, I think the standard approach is: with a cut from 0 to 1, crossing this cut corresponds to going around 0 (giving σ₀) if we think of the cut as emanating from 0, or going around 1 (giving σ₁) if we think of it as emanating from 1. The key point is that the cut [0,1] separates the plane into two regions, and crossing it changes sheets according to the monodromy of a loop that crosses the cut once. This loop goes around either 0 or 1 (but not both), and the monodromy depends on which one.

But in practice, for a cut between two branch points, the monodromy is the same everywhere along the cut IF the two branch points have the same monodromy. If they have different monodromies (as in our case), the cut doesn't have a uniform monodromy, and we need to use cuts to ∞ instead.

Hmm, but actually, in many standard treatments, cuts between branch points are used even when the monodromies differ. The idea is that the cut [0,1] has the monodromy of going around 0 (which equals the monodromy of going around 1 times the monodromy of going around ∞, by the relation σ₀ · σ₁ · σ∞ = id, so σ₀ = σ∞^{-1} · σ₁^{-1} = σ∞ · σ₁ since they're involutions).

Wait, I think I'm overcomplicating this. Let me reconsider.

The standard way to think about it: we make a cut from 0 to 1. The function is single-valued on the complement. When we cross the cut, we move to a different sheet. The specific monodromy of crossing the cut is determined by the branch point that the cut emanates from. But since the cut connects 0 and 1, crossing it near 0 gives σ₀ and crossing it near 1 gives σ₁. If σ₀ ≠ σ₁, the monodromy changes along the cut.

In the standard scheme drawing, this is handled by noting that the cut [0,1] has the monodromy σ₀ at the 0-end and σ₁ at the 1-end, and the monodromy "changes" somewhere along the cut. But this is not a clean picture.

The cleaner approach for the scheme: use cuts from each branch point to ∞. Then each cut has a well-defined monodromy.

For part (a): cuts [0, ∞) and [1, ∞).
- Cut [0, ∞): monodromy (1 3)(2 4) — sheets 1↔3, 2↔4
- Cut [1, ∞): monodromy (1 2)(3 4) — sheets 1↔2, 3↔4

For part (b): cuts [-1, ∞), [0, ∞), [1, ∞).
- Cut [-1, ∞): monodromy (i+1, j) — 3-cycles on u
- Cut [0, ∞): monodromy (i, j+1) — 2-cycles on v
- Cut [1, ∞): monodromy (i+1, j) — 3-cycles on u

For part (c): cut [0, ∞).
- Cut [0, ∞): monodromy (i+1, j+1) — 6-cycle

For part (d): cuts [-1, ∞) and [1, ∞).
- Cut [-1, ∞): monodromy (i+1, j) — 4-cycles on u
- Cut [1, ∞): monodromy (i+1, j+1) — 4-cycles on u and v

OK, I think I have a good understanding now. Let me write up the solution.

Let me also reconsider the branch order at ∞ for each part.

For part (a): σ∞ = (1 4)(2 3), which is two 2-cycles. So ∞ has two branch points of order 2.

For part (b): σ∞ = (i+1, j+1), which is one 6-cycle. So ∞ has one branch point of order 6.

For part (c): σ₀ and σ∞ are both 6-cycles. So 0 and ∞ each have one branch point of order 6.

For part (d): σ∞ = (i+2, j-1), which is four 4-cycles. So ∞ has four branch points of order 4.

Wait, for part (d) at ∞, I said u has order 2 and v has order 4. The combined monodromy is (i+2, j-1), which has order lcm(2, 4) = 4. And it decomposes into four 4-cycles. So each ramification point at ∞ has e = 4, and there are 4 of them.

Let me recheck: the cycle structure of (i+2, j-1) on 16 elements:
Fix j-1 = j' (shift), then i → i+2. For fixed j', the i-cycle is (0 → 2 → 0), a 2-cycle. But we also have j → j-1, so after 2 steps: i → i+4 = i, j → j-2. After 4 steps: i → i+8 = i, j → j-4 = j. So the order is 4, and each cycle has length 4.

Let me trace: (0,0) → (2,3) → (0,2) → (2,1) → (0,0). Length 4. ✓
There are 16/4 = 4 cycles. ✓

So at ∞, we have 4 ramification points with e = 4, each contributing 3 to R. Total from ∞: 12.

At -1: (i+1, j), order 4, cycles of length 4. 16/4 = 4 cycles. Each contributes 3. Total: 12.
At 1: (i+1, j+1), order 4, cycles of length 4. 16/4 = 4 cycles. Each contributes 3. Total: 12.

R = 36, 2g-2 = -32+36 = 4, g = 3. ✓

Now let me write the solution. I'll describe each scheme clearly.

One more thing to verify for part (b): the branch order at ∞.

σ∞ = (i+1, j+1) on 6 elements. Order = lcm(3, 2) = 6. One 6-cycle. So ∞ has one branch point of order 6, contributing 5 to R. ✓

And for part (b) at z = 0: σ₀ = (i, j+1), which is three 2-cycles. Order 2. Three cycles, each contributing 1. Total: 3. ✓

At z = ±1: σ = (i+1, j), which is two 3-cycles. Order 3. Two cycles, each contributing 2. Total: 4 each. ✓

R = 4 + 3 + 4 + 5 = 16. 2g-2 = -12+16 = 4. g = 3. ✓

Now, let me also think about whether the problem expects a simpler answer. The problem says "draw the schemes," which in a complex analysis course typically means describing the branch cuts and sheet connections. Let me present this clearly.

Let me also reconsider: for part (a), I should double-check that the function is indeed 4-sheeted and not 2-sheeted.

w = √z + √(z-1). The four values are:
w₁ = √z + √(z-1)
w₂ = √z - √(z-1)
w₃ = -√z + √(z-1) = -(√z - √(z-1)) = -w₂
w₄ = -√z - √(z-1) = -w₁

So w₃ = -w₂ and w₄ = -w₁. The four values come in pairs (w₁, -w₁) and (w₂, -w₂). For generic z, w₁ ≠ ±w₂, so we have 4 distinct values. ✓

Also, w₁ · w₂ = (√z + √(z-1))(√z - √(z-1)) = z - (z-1) = 1. So w₂ = 1/w₁. And w₃ = -1/w₁, w₄ = -w₁. So the four values are w₁, 1/w₁, -1/w₁, -w₁. This is consistent with the equation w⁴ - (4z-2)w² + 1 = 0 (which is a quadratic in w²).

OK, I'm confident in my analysis. Let me write the solution.

Let me also think about how to present the "scheme" clearly. The scheme of a Riemann surface is a topological description consisting of:
1. Number of sheets
2. Branch points and their locations
3. Branch cuts
4. How sheets are connected across each cut (the monodromy)

I'll present each part with these elements.

Let me also reconsider the branch cut choices to make them more standard.

For part (a): Branch points at 0, 1, ∞. Standard cuts: [0,1] and [1,∞], or [0,∞) and [1,∞). I'll use [0,∞) and [1,∞) for clarity (each cut has a single monodromy).

Actually, for a more standard presentation, let me use [0,1] and [1,∞] for part (a). Even though the monodromy isn't uniform along [0,1], in practice the scheme is drawn with the understanding that the cut [0,1] carries the monodromy of the branch point at 0 (or 1), and the other branch point's monodromy is carried by the other cut.

Hmm, actually, I think the standard approach in Russian textbooks is different. Let me reconsider.

In Shabat's textbook, the scheme is typically drawn as follows: you have n sheets (n = number of values), and you draw branch cuts. Across each cut, you indicate which sheets are connected. The cuts are chosen so that each cut connects two branch points (or a branch point to ∞), and the monodromy is indicated.

For a cut between two branch points a and b, the monodromy of crossing the cut is the monodromy of going around a (which is the same as going around b, if a and b are the only branch points connected by this cut and the monodromy at ∞ accounts for the rest).

Wait, that's not right either. The monodromy of crossing a cut [a,b] is the monodromy of a loop that goes around a but not b (or vice versa). If a and b have different monodromies, the cut [a,b] has a well-defined monodromy only if we specify which end we're crossing.

I think the cleanest approach for this problem is:

For each function, I'll describe:
1. The algebraic equation satisfied by w
2. The number of sheets
3. The branch points and their monodromies (as permutations)
4. A choice of branch cuts and the sheet connections across each cut
5. The genus

Let me write this up now.

Actually, I realize there's a subtlety I should address for part (a). Let me reconsider whether we can use a cut [0,1].

With a cut [0,1], the complement of [0,1] in the sphere (plus the cut [1,∞]) is simply connected. On this region, we can define single-valued branches. The monodromy of crossing [0,1] is the monodromy of a loop that goes around 0 (but not 1 or ∞). This is σ₀ = (1 3)(2 4). The monodromy of crossing [1,∞] is the monodromy of a loop that goes around 1 and ∞ (but not 0). This is σ₁ · σ∞ = σ₀^{-1} = σ₀ (since σ₀ is an involution). Wait, that gives the same monodromy for both cuts, which can't be right.

Let me reconsider. With cuts [0,1] and [1,∞]:
- A loop crossing [0,1] once (going from upper half-plane to lower) corresponds to going around 0. Monodromy: σ₀ = (1 3)(2 4).
- A loop crossing [1,∞] once corresponds to going around ∞ (and 1). Monodromy: σ₁ · σ∞... no.

Actually, a loop that crosses [1,∞] once goes around 1 (and ∞). The monodromy is σ₁ if the loop goes around 1 but not ∞, or σ₁ · σ∞ if it goes around both. But with the cut [1,∞], a loop crossing this cut goes around 1 but not ∞ (since ∞ is on the cut). Hmm, this is getting confusing.

Let me think about it more carefully. With cuts [0,1] and [1,∞] (both on the real axis), the complement is the plane minus these two intervals. This is simply connected. A path from the upper half-plane to the lower half-plane crossing [0,1] goes around 0. A path crossing [1,∞] goes around 1 (and also ∞, since the cut extends to ∞).

Actually, crossing [1,∞] from above to below is equivalent to going around 1 (a small loop around 1 crosses [1,∞] on one side and [0,1] on the other... no, 1 is the junction point).

I think the issue is that 1 is where the two cuts meet, so loops around 1 cross both cuts. Let me use non-intersecting cuts instead.

Let me use:
- Cut A: from 0 to ∞ along the negative real axis (i.e., [0, -∞))
- Cut B: from 1 to ∞ along the positive real axis (i.e., [1, +∞))

These don't intersect (except at ∞). The complement is simply connected.

- Crossing cut A (from 0 to -∞): going around 0. Monodromy: σ₀ = (1 3)(2 4).
- Crossing cut B (from 1 to +∞): going around 1. Monodromy: σ₁ = (1 2)(3 4).

At ∞: σ∞ = (σ₀ · σ₁)^{-1} = (1 4)(2 3). ✓

This is clean. Each cut has a well-defined monodromy.

OK, I think for the solution, I'll use cuts to ∞ for all parts, as this gives the cleanest description.

Let me now write the complete solution.

Hmm, actually, I want to reconsider part (a) once more. Is the genus really 0?

We have 4 sheets, 3 branch points, each with two 2-cycles (i.e., two simple branch points at each location).

Riemann-Hurwitz: 2g - 2 = 4(2·0 - 2) + R = -8 + R.
R = 3 × 2 × (2-1) = 6 (three branch points, each with two simple ramification points, each contributing 1).
2g - 2 = -8 + 6 = -2, g = 0. ✓

Yes, genus 0. The Riemann surface is topologically a sphere.

Now let me also verify: can we see this directly? The function w = √z + √(z-1) with w₁ · w₂ = 1 (where w₂ = √z - √(z-1)). So w and 1/w are both values. The equation w⁴ - (4z-2)w² + 1 = 0 is a quadratic in w², so w² = [(4z-2) ± 4√(z(z-1))]/2 = (2z-1) ± 2√(z(z-1)).

Let t = w². Then t = (2z-1) ± 2√(z(z-1)). This is a 2-sheeted function of z (branched at 0 and 1). Then w = ±√t, which is a 2-sheeted function of t (branched at t = 0 and t = ∞). But we showed t never equals 0, so w = √t is branched only at t = ∞.

As z → ∞, t₊ = (2z-1) + 2√(z(z-1)) ≈ 2z - 1 + 2z = 4z → ∞, and t₋ = (2z-1) - 2√(z(z-1)) ≈ 2z - 1 - 2z = -1 → -1. So t₊ → ∞ and t₋ → -1.

So the map z → t is 2-sheeted (branched at 0, 1, ∞), and the map t → w is 2-sheeted (branched at t = ∞, which corresponds to z = ∞ via t₊, and at t = -1... wait, w = √t is branched at t = 0 and t = ∞. t₋ → -1 as z → ∞, so t = 0 is not in the image of t₋ for large z. But t₊ → ∞, so t = ∞ is in the image.

Hmm, this is getting complicated. Let me just trust the Riemann-Hurwitz calculation. Genus 0.

Now, let me write the solution. I'll describe each scheme clearly, including the number of sheets, branch points, monodromies, cuts, and genus.

One more consideration: for part (b), I should double-check the branch at ∞.

σ∞ = (i+1, j+1) on 6 elements. This is a 6-cycle, so it's a single branch point of order 6 at ∞. But let me verify this makes sense.

u = ³√(z²-1) ~ z^{2/3} as z → ∞. Going around ∞ (z → ze^{-2πi}): z^{2/3} → z^{2/3} e^{-4πi/3} = z^{2/3} e^{2πi/3} = u · ω. So i → i+1. ✓
v = z^{-1/2} → z^{-1/2} e^{πi} = -v. So j → j+1. ✓
Combined: (i+1, j+1), which is a 6-cycle. ✓

OK, everything checks out. Let me write the solution.

Let me also think about how to describe the schemes in a way that could be "drawn." The scheme is typically a picture with:
- Horizontal lines representing sheets
- Branch cuts shown as gaps or connections between sheets
- Labels indicating which sheets are connected

Since I can't draw, I'll describe this verbally.

Let me write the solution now.

For part (b), let me reconsider the branch cut structure. We have branch points at -1, 0, 1, ∞. Using cuts to ∞:
- Cut from -1 to ∞: monodromy (i+1, j) — 3-cycles on u
- Cut from 0 to ∞: monodromy (i, j+1) — 2-cycles on v
- Cut from 1 to ∞: monodromy (i+1, j) — 3-cycles on u

But having three cuts all going to ∞ is a bit unusual. An alternative is:
- Cut from -1 to 0: monodromy σ_{-1} = (i+1, j) — 3-cycles on u
- Cut from 0 to 1: monodromy σ₀ = (i, j+1) — 2-cycles on v
- Cut from 1 to ∞: monodromy σ₁ = (i+1, j) — 3-cycles on u

This works because each cut connects two branch points with different monodromies, and the monodromy of crossing each cut is well-defined (it's the monodromy of the branch point on the left, say).

Wait, but I said earlier that a cut between two branch points with different monodromies doesn't have a uniform monodromy. Let me reconsider.

Actually, I think the key insight is: if we have a cut from a to b, the monodromy of crossing this cut is the monodromy of going around a (which is σ_a). This is well-defined because the cut separates the plane, and crossing it from one side to the other is equivalent to going around a (but not b). The monodromy at b is then carried by a different cut emanating from b.

So with cuts [-1, 0], [0, 1], [1, ∞]:
- Crossing [-1, 0]: go around -1, monodromy σ_{-1} = (i+1, j)
- Crossing [0, 1]: go around 0, monodromy σ₀ = (i, j+1)
- Crossing [1, ∞]: go around 1, monodromy σ₁ = (i+1, j)

At ∞: σ∞ = (σ_{-1} · σ₀ · σ₁)^{-1} = (i+1, j+1). ✓

This is clean and standard. Each cut connects consecutive branch points, and the monodromy is that of the left endpoint.

Similarly for part (a), with cuts [0, 1] and [1, ∞]:
- Crossing [0, 1]: go around 0, monodromy σ₀ = (1 3)(2 4)
- Crossing [1, ∞]: go around 1, monodromy σ₁ = (1 2)(3 4)

At ∞: σ∞ = (σ₀ · σ₁)^{-1} = (1 4)(2 3). ✓

This is clean! I was overcomplicating things earlier. The cut [0,1] has monodromy σ₀ (going around 0), and the cut [1,∞] has monodromy σ₁ (going around 1). The fact that 0 and 1 have different monodromies is fine — each cut carries the monodromy of its left endpoint.

Wait, but what about the right endpoint? The cut [0,1] also connects to 1, which has monodromy σ₁. When we cross [0,1] near 1, do we get σ₁ instead of σ₀?

I think the answer is no. The cut [0,1] is a single cut, and crossing it anywhere gives the same monodromy, which is σ₀ (the monodromy of going around 0). The monodromy σ₁ is carried by the cut [1,∞]. The point 1 is where the two cuts meet, and going around 1 requires crossing both cuts.

Let me verify: a small loop around 1 crosses both [0,1] and [1,∞]. The monodromy is σ₀ (from crossing [0,1]) followed by σ₁ (from crossing [1,∞]) = σ₀ · σ₁. But the monodromy around 1 should be σ₁, not σ₀ · σ₁.

Hmm, that's a contradiction. Let me reconsider.

Actually, a small loop around 1 crosses [1,∞] once (going from one side to the other and back). It doesn't cross [0,1] if the loop is small enough. So the monodromy around 1 is just σ₁ (from crossing [1,∞]). ✓

And a small loop around 0 crosses [0,1] once. Monodromy: σ₀. ✓

A loop around ∞ crosses [1,∞] once (going around ∞ means going around the "outside" of the cut [1,∞]). Monodromy: σ₁. But σ∞ should be (σ₀ · σ₁)^{-1} = σ₀ · σ₁ (since they're involutions). So σ∞ = σ₀ · σ₁ = (1 3)(2 4) · (1 2)(3 4) = (1 4)(2 3). ✓

But wait, a loop around ∞ crosses [1,∞] once, giving monodromy σ₁ = (1 2)(3 4). But σ∞ = (1 4)(2 3) ≠ σ₁. Contradiction!

Let me reconsider. A loop around ∞ (counterclockwise on the sphere) is a large loop in the plane going clockwise. This loop crosses [1,∞] (if [1,∞] is on the positive real axis). Going clockwise around ∞, we cross [1,∞] from below to above (or vice versa). The monodromy of this crossing is... hmm.

Actually, I think the issue is the direction. Crossing [1,∞] from above to below gives monodromy σ₁, and crossing from below to above gives σ₁^{-1} = σ₁ (since it's an involution). So the direction doesn't matter for involutions.

But a loop around ∞ should give σ∞, not σ₁. The resolution is that a loop around ∞ doesn't just cross [1,∞]; it also crosses [0,1] if the loop is large enough to enclose 0.

Wait, no. If the cuts are [0,1] and [1,∞] (both on the real axis), a large loop around ∞ (clockwise in the plane, counterclockwise on the sphere) crosses [1,∞] once but doesn't cross [0,1] (since [0,1] is inside the loop). Hmm, but the loop goes around everything, so it should cross both cuts.

I think I'm getting confused by the topology. Let me think about this more carefully.

The cuts [0,1] and [1,∞] divide the sphere into a simply connected region. A loop around ∞ on the sphere corresponds to a large clockwise loop in the plane. This loop starts in the upper half-plane, goes clockwise (to the right, then down, then left, then up). It crosses [1,∞] once (going from above to below, say) and doesn't cross [0,1] (since [0,1] is enclosed by the loop). 

Wait, actually, a large clockwise loop in the plane encloses everything. It crosses [1,∞] once (at some point x > 1) and crosses [0,1] zero times (since [0,1] is inside the loop, and the loop doesn't cross the real axis between 0 and 1... actually, it does cross the real axis, but at a point x > 1 or x < 0).

Hmm, let me think about this differently. The loop goes around ∞, which means it's a large circle traversed clockwise. It crosses the positive real axis at some point x > 1 (crossing [1,∞]) and crosses the negative real axis at some point x < 0 (not crossing any cut). So it crosses [1,∞] once and [0,1] zero times. Monodromy: σ₁.

But σ∞ should be (1 4)(2 3), and σ₁ = (1 2)(3 4). These are different!

I think the issue is that the loop around ∞ also crosses the cut [1,∞] in a specific direction that might give σ₁^{-1} instead of σ₁. But since σ₁ is an involution, σ₁ = σ₁^{-1}. So the monodromy is σ₁, which should equal σ∞. But σ₁ ≠ σ∞. Contradiction!

OK, I think I'm making an error somewhere. Let me reconsider.

The issue might be with how the cuts are set up. Let me reconsider.

With cuts [0,1] and [1,∞] on the real axis, the complement in the Riemann sphere is simply connected. On this complement, we have 4 single-valued branches of w. The monodromy of crossing a cut tells us how to move between sheets.

A loop around 0 (small, counterclockwise): crosses [0,1] once. Monodromy: σ₀.
A loop around 1 (small, counterclockwise): crosses [0,1] once and [1,∞] once. Monodromy: σ₀ · σ₁ (or σ₁ · σ₀, depending on the order of crossings).

Hmm, this is the issue. A small loop around 1 crosses both cuts (since 1 is the junction point). The monodromy is the product of the two crossings.

But the monodromy around 1 should be σ₁. So σ₁ = (product of crossings of [0,1] and [1,∞]).

If the loop around 1 first crosses [0,1] and then [1,∞], the monodromy is σ_{[0,1]} · σ_{[1,∞]}. If σ_{[0,1]} = σ₀ and σ_{[1,∞]} = σ₁, then the product is σ₀ · σ₁, which should equal σ₁. This gives σ₀ = identity, which is wrong.

So my assignment of monodromies to cuts is incorrect!

Let me reconsider. The correct assignment should be:
- Crossing [0,1] gives monodromy A
- Crossing [1,∞] gives monodromy B
- Loop around 0: crosses [0,1] once, monodromy = A = σ₀
- Loop around 1: crosses [0,1] once and [1,∞] once, monodromy = A · B = σ₁ (or B · A = σ₁)
- Loop around ∞: crosses [1,∞] once, monodromy = B = σ∞

From loop around 0: A = σ₀ = (1 3)(2 4).
From loop around ∞: B = σ∞ = (1 4)(2 3).
From loop around 1: A · B = σ₀ · σ∞ = (1 3)(2 4) · (1 4)(2 3).

Let me compute: (1 3)(2 4) · (1 4)(2 3) (right to left):
1 → (1 4) → 4 → (2 4) → 2. So 1 → 2.
2 → (2 3) → 3 → (1 3) → 1. So 2 → 1. Good, (1 2).
3 → (2 3) → 2 → (2 4) → 4. So 3 → 4.
4 → (1 4) → 1 → (1 3) → 3. So 4 → 3. Good, (3 4).

So A · B = (1 2)(3 4) = σ₁. ✓

So the correct assignment is:
- Crossing [0,1]: monodromy σ₀ = (1 3)(2 4)
- Crossing [1,∞]: monodromy σ∞ = (1 4)(2 3)

And σ₁ = σ₀ · σ∞ (from the loop around 1 crossing both cuts).

This makes sense! The cut [1,∞] carries the monodromy of ∞, not of 1. The monodromy of 1 is the product of monodromies of the two cuts that meet at 1.

So the general rule is: if a cut goes from branch point a to branch point b, the monodromy of crossing this cut is the monodromy at b (the endpoint, not the starting point). Or maybe it's the monodromy at a. Let me reconsider.

With cuts [0,1] and [1,∞]:
- Cut [0,1]: connects 0 and 1. Monodromy = σ₀ (from loop around 0, which crosses only this cut).
- Cut [1,∞]: connects 1 and ∞. Monodromy = σ∞ (from loop around ∞, which crosses only this cut).
- Loop around 1 crosses both cuts: monodromy = σ₀ · σ∞ = σ₁. ✓

So the monodromy of a cut [a,b] is the monodromy of the branch point that is NOT shared with another cut. For [0,1], 0 is not shared (only 1 is shared with [1,∞]), so the monodromy is σ₀. For [1,∞], ∞ is not shared, so the monodromy is σ∞.

Alternatively: the monodromy of a cut [a,b] is σ_a if a is an endpoint that is only on this cut (not shared), and σ_b if b is only on this cut. If both endpoints are shared (on multiple cuts), then... well, in our case, 1 is shared between [0,1] and [1,∞], and its monodromy is the product of the two cut monodromies.

OK so the correct scheme for part (a) is:
- 4 sheets
- Cuts [0,1
