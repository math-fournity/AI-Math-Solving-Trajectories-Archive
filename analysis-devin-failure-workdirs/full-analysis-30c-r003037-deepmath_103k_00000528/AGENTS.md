# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Use Cauchy's integral formula to compute the contour integral \( \int \limits_{\Gamma} \frac{e^{-z}}{z-1}dz \), where \( \Gamma \) is the square with sides parallel to the axes, centered at \( i \), and with side length 5, traversed in the anticlockwise direction.       — 题目文本
#   Okay, so I need to compute the contour integral of e^(-z)/(z - 1) around this square Γ. The square is centered at i, has sides parallel to the axes, and has a side length of 5. It's traversed anticlockwise. Alright, let me recall Cauchy's integral formula. 

Cauchy's integral formula states that if f(z) is analytic inside and on some simple closed contour Γ, and if a is a point inside Γ, then the integral around Γ of f(z)/(z - a) dz is 2πi times f(a). So in symbols: ∫_Γ [f(z)/(z - a)] dz = 2πi f(a). 

In this problem, the integrand is e^(-z)/(z - 1). Comparing this to the Cauchy formula, it seems like f(z) would be e^(-z), and a would be 1. So then, according to the formula, if 1 is inside the contour Γ, the integral would be 2πi times f(1) = 2πi e^{-1}. But if 1 is not inside Γ, then the integral would be zero because the integrand would be analytic inside and on Γ. 

Therefore, the key question here is: Is the point z = 1 inside the square Γ? The square is centered at i, which is (0, 1) in the complex plane, right? And the side length is 5, so each side is 5 units long. Since the sides are parallel to the axes, the square extends 2.5 units to the left, right, top, and bottom from its center. 

Let me visualize the complex plane. The center is at i, so the square is centered at (0, 1). The side length is 5, so each half-side is 2.5. Therefore, the square spans from -2.5 to +2.5 in the real (x-axis) direction and from 1 - 2.5 to 1 + 2.5 in the imaginary (y-axis) direction. Wait, but actually, the square is in the complex plane, so the x-axis is real, y-axis is imaginary. So the center is at (0, 1). The square has sides of length 5, so each side from the center extends 2.5 units. Therefore, horizontally (real direction), the square goes from 0 - 2.5 to 0 + 2.5, i.e., from -2.5 to +2.5 on the real axis. Vertically (imaginary direction), it goes from 1 - 2.5 to 1 + 2.5, which is from -1.5 to 3.5 on the imaginary axis. 

So the square spans from -2.5 to +2.5 in real and from -1.5i to 3.5i in imaginary. Now, the point z = 1 is at (1, 0) in the complex plane. So we need to check if (1, 0) is inside this square. 

Since the real part of z = 1 is 1, which is between -2.5 and +2.5. The imaginary part is 0, which is between -1.5 and +3.5. Therefore, the point z = 1 is indeed inside the square Γ. Wait, hold on. The center is at (0,1), which is 0 in real and 1 in imaginary. The square's vertical range is from 1 - 2.5 to 1 + 2.5. Wait, 1 - 2.5 is -1.5, and 1 + 2.5 is 3.5. So vertically, it goes from -1.5i to 3.5i. But the imaginary part of z = 1 is 0, which is within -1.5 to 3.5. The real part of z = 1 is 1, which is within -2.5 to 2.5. So yes, z = 1 is inside the square. 

Therefore, by Cauchy's integral formula, the integral should be 2πi times e^{-1}, which is 2πi / e. 

Wait, but let me double-check. Is there any reason the formula wouldn't apply here? The function f(z) = e^{-z} is entire, right? It's analytic everywhere in the complex plane, so there are no issues with it being analytic inside and on Γ. The denominator is z - 1, and since z = 1 is inside Γ, the integrand has a singularity at z = 1. However, because f(z) is analytic everywhere, Cauchy's integral formula applies. 

Therefore, unless there's something tricky here, the integral should just be 2πi e^{-1}. But maybe I should check the orientation. The problem states that the contour is traversed anticlockwise, which is the standard direction for Cauchy's formula. So that's good. 

Alternatively, if I were to parametrize the square and compute the integral directly, that would be very complicated. But since Cauchy's formula applies here, there's no need. 

But just to be thorough, let me confirm the dimensions again. The square is centered at i (0,1) with side length 5, so each side is 5 units. Therefore, each half-side is 2.5 units. So along the real axis (horizontal direction), the square extends from -2.5 to +2.5. Along the imaginary axis (vertical direction), from 1 - 2.5 to 1 + 2.5, which is -1.5 to 3.5. 

Therefore, the square's corners would be at ( -2.5, -1.5 ), ( +2.5, -1.5 ), ( +2.5, 3.5 ), ( -2.5, 3.5 ). Wait, no, actually, in complex terms, the corners would be:

- Real part from -2.5 to +2.5, and imaginary part from -1.5 to +3.5. Wait, actually, no. Wait, the center is at (0,1). So to get the corners, if it's a square with sides parallel to the axes, centered at (0,1), with side length 5, then each half-side is 2.5. Therefore, the real part (x-coordinate) ranges from 0 - 2.5 to 0 + 2.5, which is -2.5 to +2.5. The imaginary part (y-coordinate) ranges from 1 - 2.5 to 1 + 2.5, which is -1.5 to +3.5. So the square in the complex plane is the region:

-2.5 ≤ Re(z) ≤ 2.5

-1.5 ≤ Im(z) ≤ 3.5

So the point z = 1 has Re(z) = 1 (which is within -2.5 to 2.5) and Im(z) = 0 (which is within -1.5 to 3.5). So yes, definitely inside the square.

Therefore, applying Cauchy's integral formula, the integral is 2πi * e^{-1}, so 2πi / e. Therefore, the answer should be 2πi/e. 

But just to check, maybe I made a mistake in the sign? Let me recall: Cauchy's formula says ∫_Γ [f(z)/(z - a)] dz = 2πi f(a). Here, f(z) is e^{-z}, a is 1. So indeed, the integral is 2πi e^{-1}. There's no negative sign or anything. The function e^{-z} is just the function evaluated at a = 1. So e^{-1} is correct. 

Alternatively, if the integrand were e^{-z}/(z - a), then the formula applies with f(z) = e^{-z}, so f(a) = e^{-a}. Here, a is 1, so f(a) = e^{-1}. So yes, that's correct. 

Therefore, I think the answer is 2πi e^{-1}, or 2πi / e. 

Wait, let me make sure that the integrand is in the correct form. Cauchy's formula is for f(z)/(z - a). In our case, the integrand is e^{-z}/(z - 1). So f(z) = e^{-z}, a = 1, so indeed, the integral is 2πi f(1) = 2πi e^{-1}. That seems correct. 

Is there any other reason this might not apply? For example, if the contour was not simply connected, but since it's a square, it's a simple closed contour. The function e^{-z} is entire, so analytic everywhere. The point a = 1 is inside the contour, so all conditions are met. 

Therefore, the integral is 2πi times e^{-1}.

I think that's solid. Maybe just to check the side length again. The square has side length 5, so each half-side is 2.5. So from center at (0,1), moving left 2.5 in real direction gets to -2.5, right to +2.5. Up 2.5 in imaginary direction from center (1) gets to 3.5, down to -1.5. So yes, as before.

Therefore, the integral is 2πi/e. So \boxed{\dfrac{2\pi i}{e}}.

**Final Answer**
\boxed{\dfrac{2\pi i}{e}}
</think>

To compute the contour integral \( \int_{\Gamma} \frac{e^{-z}}{z-1} \, dz \) using Cauchy's integral formula, we first identify the function and the point of singularity. The integrand is \( \frac{e^{-z}}{z-1} \), which fits the form \( \frac{f(z)}{z-a} \) with \( f(z) = e^{-z} \) and \( a = 1 \).

Cauchy's integral formula states that if \( f(z) \) is analytic inside and on a simple closed contour \( \Gamma \) and \( a \) is inside \( \Gamma \), then the integral is \( 2\pi i f(a) \).

Next, we check if the point \( z = 1 \) lies inside the square \( \Gamma \). The square is centered at \( i \) (which is \( (0, 1) \) in the complex plane) with a side length of 5. The square extends 2.5 units in each direction from the center. Therefore, the real part ranges from \( -2.5 \) to \( 2.5 \) and the imaginary part ranges from \( -1.5 \) to \( 3.5 \).

The point \( z = 1 \) has a real part of 1 (within \( -2.5 \) to \( 2.5 \)) and an imaginary part of 0 (within \( -1.5 \) to \( 3.5 \)), confirming that \( z = 1 \) is inside the contour.

Since \( f(z) = e^{-z} \) is entire (analytic everywhere), we apply Cauchy's integral formula:
\[
\int_{\Gamma} \frac{e^{-z}}{z-1} \, dz = 2\pi i \cdot f(1) = 2\pi i \cdot e^{-1}
\]

Thus, the final answer is:
\[
\boxed{\dfrac{2\pi i}{e}}
\]  — 标准解答
#   The problem asks: Is the ring $A[x, a/x]$ always integrally closed if $A$ is a UFD and $a \in A$?

Let me think about this carefully.

$A[x, a/x]$ is the subring of $A[x, x^{-1}]$ (or rather of $\text{Frac}(A)[x, x^{-1}]$) generated by $x$ and $a/x$ over $A$. Actually, more precisely, $A[x, a/x]$ is the $A$-subalgebra of $K[x, x^{-1}]$ (where $K = \text{Frac}(A)$) generated by $x$ and $a/x$.

Note that $A[x, a/x] \cong A[X, Y] / (XY - a)$ where $X \mapsto x$, $Y \mapsto a/x$. This is because the relation $x \cdot (a/x) = a$ holds, and this is the only relation.

So the question becomes: is $A[X,Y]/(XY - a)$ integrally closed when $A$ is a UFD?

This is the coordinate ring of a "toric-like" variety. Actually $A[X,Y]/(XY-a)$ is the ring of the affine variety $XY = a$.

When is $A[X,Y]/(XY-a)$ integrally closed (or normal)?

A classical result: $A[X,Y]/(XY-a)$ is normal if and only if $a$ is square-free in $A$ (when $A$ is a UFD, or more generally when $a$ is "square-free" in an appropriate sense).

Wait, let me think more carefully. Actually, let me reconsider.

If $a$ is a unit, then $XY - a$ is... well $A[X,Y]/(XY-a)$ with $a$ a unit. Then $X$ is a unit (since $X \cdot Y = a$ and $a$ is a unit, so $X \cdot (a^{-1}Y) = 1$). So $A[X,Y]/(XY-a) \cong A[X, X^{-1}]$ which is a Laurent polynomial ring, and this is integrally closed if $A$ is integrally closed (UFD implies integrally closed). Good.

If $a = 0$, then $A[X,Y]/(XY) = A[X,Y]/(XY)$. Is this integrally closed? $XY = 0$ is the union of two axes. The ring $A[X,Y]/(XY)$ has zero divisors. Is it integrally closed? Consider $A = k$ a field. $k[X,Y]/(XY)$. The normalization of $k[X,Y]/(XY)$ is $k[X] \times k[Y]$ (the product of the normalizations of the two components). So $k[X,Y]/(XY)$ is NOT integrally closed. So for $a = 0$, it's not integrally closed.

But wait, maybe the question assumes $a \neq 0$? Let me consider the general case.

Actually, let me think about when $A[X,Y]/(XY - a)$ is normal for $A$ a UFD and $a \neq 0$.

Claim: $A[X,Y]/(XY - a)$ is integrally closed if and only if $a$ is square-free in $A$ (i.e., $a$ is not divisible by the square of any irreducible element, up to units).

Let me verify this. Suppose $a = p^2 \cdot b$ for some irreducible $p$ and $b \in A$. Then in $B = A[X,Y]/(XY - a)$, we have $XY = p^2 b$.

Consider the element $t = X/p$ in the fraction field of $B$. We have $t \cdot Y = XY/p = p^2 b / p = pb$. Hmm, let me think about whether $t$ is integral over $B$.

Actually, $t = X/p$. Then $t^2 = X^2/p^2$. And $t \cdot (Y/p) = XY/p^2 = b$. Hmm, let me think differently.

Let me consider the element $u = X/p$ in $\text{Frac}(B)$. Is $u$ integral over $B$?

$u$ satisfies: $u \cdot Y = (X/p) \cdot Y = XY/p = a/p = pb$. So $uY = pb \in B$ (since $p, b \in A \subset B$). But that doesn't directly give integrality.

Let me think about it differently. Consider $u = X/p$. Then $u^2 = X^2/p^2$. We have $X \cdot Y = p^2 b$, so $X^2 Y^2 = p^4 b^2$, thus $(X^2/p^2)(Y^2) = p^2 b^2 \cdot ... $ hmm this is getting complicated.

Let me try a specific example. Take $A = k[t]$ (a PID, hence UFD), $a = t^2$. Then $B = k[t][X,Y]/(XY - t^2)$.

Is $B$ integrally closed? Consider $s = X/t$ in $\text{Frac}(B)$. Then $s \cdot Y = XY/t = t^2/t = t \in B$. Also $s \cdot t = X \in B$. So $s$ maps things to $B$... but is $s$ itself in $B$?

$s = X/t$. Is $s$ integral over $B$? We have $s^2 = X^2/t^2$. And $X^2 = X \cdot X$. We know $XY = t^2$, so $X = t^2/Y$ (in the fraction field). Then $s = X/t = t/Y$. So $s = t/Y$, and $sY = t \in B$.

Is $s$ integral over $B$? Consider $s \cdot Y = t$, so $s = t/Y$. Also $s^2 = t^2/Y^2 = X/Y$ (since $t^2 = XY$). Hmm.

Let me check: is $s$ a root of a monic polynomial over $B$?

$s = X/t = t/Y$. We have $sY = t$ and $sX = X^2/t = X \cdot (X/t) = Xs$... that's circular.

Let me try: $s^2 Y = s \cdot (sY) = s \cdot t = st = (X/t) \cdot t = X \in B$. So $s^2 Y = X$.

Also $s^2 Y^2 = (sY)^2 = t^2 = XY$, so $s^2 Y^2 = XY$, giving $s^2 Y = X$ (dividing by $Y$ in the fraction field), consistent.

Now, is $s$ integral over $B$? Let's see if $s$ satisfies a monic polynomial. We have $sY = t$ and $sX = X^2/t$. Hmm, $sX = X \cdot s = X \cdot (X/t) = X^2/t$. And $X^2/t = X \cdot (X/t)$. Also $X^2 = X \cdot X$ and $t^2 = XY$ so $X/t = t/Y$ (already noted).

Consider the polynomial $Z^2 - sZ \cdot ...$. This is hard. Let me try a more direct approach.

Actually, I recall that for $A[X,Y]/(XY - a)$ with $A$ integrally closed, the ring is integrally closed iff $a$ is square-free (or $a$ is a unit, or more precisely, $a$ is "radical" in the sense that the ideal $(a)$ is radical... no, square-free).

Let me verify with the example $A = k[t]$, $a = t^2$.

$B = k[t, X, Y]/(XY - t^2)$. This is the coordinate ring of the surface singularity $XY = t^2$ in $\mathbb{A}^3$, which is an $A_1$ surface singularity (rational double point of type $A_1$). This is well-known to NOT be integrally closed (it's a singular point, and the normalization is $k[t, X, Y]/(XY - t^2) \to k[u, v]/(uv - ... )$... actually let me think).

The normalization of $k[t,X,Y]/(XY-t^2)$: Set $s = X/t = t/Y$. Then $X = st$, $Y = t/s$ (in the fraction field). The normalization should be $k[s, t]$ (or something like that). Indeed, $X = st$, $Y = t/s$... wait, $Y = t^2/X = t^2/(st) = t/s$. So in the fraction field, $X = st$ and $Y = t/s$. But $t/s$ is not a polynomial. Hmm.

Actually, let me reconsider. The map $k[t, X, Y]/(XY - t^2) \to k[u, v]$ given by $t \mapsto uv$, $X \mapsto u^2$, $Y \mapsto v^2$. Check: $XY = u^2 v^2 = (uv)^2 = t^2$. ✓. And $k[u,v]$ is integrally closed (it's a UFD). The image is $k[u^2, v^2, uv]$, which is the subring of $k[u,v]$ generated by $u^2, v^2, uv$. This is exactly the second Veronese subring, which is the coordinate ring of the $A_1$ singularity. The element $u$ (or $v$) is in the fraction field of $k[u^2, v^2, uv]$ (since $u = u^2 \cdot v / (uv) = u \cdot v / v$... hmm, $u = (u^2 v)/(uv)$... wait $u^2 v / (uv) = u$, yes). And $u$ is integral over $k[u^2, v^2, uv]$ since $u^2 \in k[u^2, v^2, uv]$. But $u \notin k[u^2, v^2, uv]$ (the Veronese subring consists of elements of even degree). So $k[u^2, v^2, uv]$ is not integrally closed, and its normalization is $k[u,v]$.

Great, so this confirms: for $a = t^2$ (not square-free), $A[x, a/x]$ is NOT integrally closed.

Now let me also verify the positive direction: if $a$ is square-free, is $A[X,Y]/(XY-a)$ integrally closed?

Take $A = k[t]$, $a = t$ (square-free, since $t$ is irreducible). Then $B = k[t, X, Y]/(XY - t)$. This is $k[X, Y]$ (since $t = XY$). Indeed, $B \cong k[X, Y]$ via $t \mapsto XY$. And $k[X,Y]$ is a UFD, hence integrally closed. ✓.

More generally, if $a$ is square-free in a UFD $A$, write $a = p_1 p_2 \cdots p_r$ (product of distinct irreducibles, up to units). Then $A[X,Y]/(XY - a)$.

Hmm, is this always integrally closed? Let me think about $A = k[s, t]$, $a = st$ (square-free since $s$ and $t$ are distinct irreducibles). Then $B = k[s, t, X, Y]/(XY - st)$.

Is this integrally closed? This is the coordinate ring of $XY = st$ in $\mathbb{A}^4$. This is a 3-dimensional variety. Is it normal?

Actually, $XY - st$ is a determinantal variety (it's the condition that the $2\times 2$ matrix $\begin{pmatrix} X & s \\ t & Y \end{pmatrix}$... no, $XY - st = 0$ is the determinant of $\begin{pmatrix} X & s \\ t & Y \end{pmatrix}$). Determinantal varieties defined by minors of generic matrices are known to be normal (or at least the ideal of maximal minors of a generic matrix is prime and the variety is normal). Actually, the variety cut out by a single $2\times 2$ minor of a $2\times 2$ matrix of indeterminates is a quadric cone, which is normal in dimension $\geq 2$... hmm, but it has an isolated singularity at the origin.

Wait, actually the quadric cone $XY - ZW = 0$ in $\mathbb{A}^4$ is known to be normal. It's a 3-dimensional variety with an isolated singularity at the origin, and it's normal (in fact, it has rational singularities). So $k[X,Y,s,t]/(XY-st)$ is integrally closed. ✓.

So the pattern seems to be: $A[X,Y]/(XY - a)$ is integrally closed iff $a$ is square-free (in a UFD).

Hmm wait, but I should be more careful. Let me think about whether square-free is sufficient in general.

Actually, I think the correct statement is: $A[X,Y]/(XY - a)$ is integrally closed if and only if $a$ is square-free in $A$ (assuming $A$ is integrally closed, or at least a UFD).

Let me think about why square-free is sufficient. Suppose $A$ is a UFD and $a$ is square-free. Write $a = u \cdot p_1 \cdots p_r$ where $u$ is a unit and $p_i$ are distinct irreducibles.

We can factor the construction. Note that $A[X,Y]/(XY - a)$ can be built up as follows. If $a = bc$ with $\gcd(b,c) = 1$ (in a UFD), then... hmm, actually there's a nice way to see this.

Consider $A = \bigcap A_{(p_i)}$ (intersection of localizations at height-1 primes, since $A$ is a UFD and thus Krull, it's the intersection of its DVR localizations at height-1 primes). 

Actually, let me think about it more algebraically. The key fact is:

**Lemma**: If $A$ is an integrally closed domain and $a \in A$ is square-free (i.e., $v(a) \leq 1$ for every DVR valuation $v$ of $K = \text{Frac}(A)$), then $A[X,Y]/(XY - a)$ is integrally closed.

Proof sketch: $B = A[X,Y]/(XY-a)$. The fraction field of $B$ is $K(X)$ where $Y = a/X$. An element of $K(X)$ integral over $B$ must be integral over $B_\mathfrak{p}$ for every prime $\mathfrak{p}$ of $B$, and $B$ is integrally closed iff $B_\mathfrak{p}$ is integrally closed for every prime $\mathfrak{p}$ (actually, $B$ is integrally closed iff $B_\mathfrak{p}$ is a DVR or field for every height-1 prime $\mathfrak{p}$, i.e., $B$ is normal iff it's regular in codimension 1, by Serre's criterion $R_1 + S_2$).

Hmm, this is getting complicated. Let me use a different approach.

Actually, I think the cleanest approach is:

$B = A[X,Y]/(XY - a)$. Note that $B \cong A[X, a/X] \subset K[X, X^{-1}]$ (or $K[X]$ if we think of $a/X$ as $a \cdot X^{-1}$, but $X^{-1}$ might not be in $K[X]$... actually $a/X = a \cdot X^{-1}$ and this is in $K[X, X^{-1}]$).

Wait, more precisely: $A[x, a/x]$ is the subring of $K[x, x^{-1}]$ (Laurent polynomial ring) generated by $A$, $x$, and $a/x = a \cdot x^{-1}$. So $A[x, a/x] = A[x, ax^{-1}] \subset K[x, x^{-1}]$.

Now, $K[x, x^{-1}]$ is integrally closed (it's a Laurent polynomial ring over a field, hence a UFD). So $A[x, a/x]$ is a subring of an integrally closed ring. The question is whether $A[x, a/x]$ itself is integrally closed.

$A[x, ax^{-1}]$ consists of all finite sums $\sum_{i} c_i x^i + \sum_j d_j a^j x^{-j}$ where... actually, let me think about what elements look like.

An element of $A[x, ax^{-1}]$ is a polynomial in $x$ and $ax^{-1}$ with coefficients in $A$. So it's of the form $\sum_{i \geq 0} \sum_{j \geq 0} c_{ij} x^i (ax^{-1})^j = \sum_{i,j \geq 0} c_{ij} a^j x^{i-j}$.

So elements are $\sum_k f_k x^k$ where $f_k \in A$ for $k \geq 0$ and $f_k \in a^{-k} A$ for $k < 0$ (i.e., $f_{-j} \in a^j A$ for $j > 0$, meaning $f_{-j} = a^j \cdot g_{-j}$ for some $g_{-j} \in A$).

Wait, let me redo this. For $k = i - j$ where $i, j \geq 0$:
- If $k \geq 0$: $i = k, j = 0$ gives $c_{k,0} x^k$, and also $i = k+1, j = 1$ gives $c_{k+1,1} a x^k$, etc. So the coefficient of $x^k$ (for $k \geq 0$) is $\sum_{j \geq 0} c_{k+j, j} a^j \in A$.
- If $k < 0$, say $k = -m$ with $m > 0$: $i = 0, j = m$ gives $c_{0,m} a^m x^{-m}$, $i=1, j=m+1$ gives $c_{1,m+1} a^{m+1} x^{-m}$, etc. So the coefficient of $x^{-m}$ is $\sum_{i \geq 0} c_{i, m+i} a^{m+i} = a^m \sum_{i \geq 0} c_{i,m+i} a^i \in a^m A$.

So $A[x, ax^{-1}] = \bigoplus_{k \in \mathbb{Z}} I_k x^k$ where $I_k = A$ for $k \geq 0$ and $I_k = a^{-k} A = a^{|k|} A$ for $k < 0$.

This is a "Z-graded" ring with $I_k = A$ for $k \geq 0$ and $I_{-m} = a^m A$ for $m > 0$.

For this to be a ring, we need $I_k \cdot I_l \subset I_{k+l}$. Check: for $k, l \geq 0$: $A \cdot A = A \subset A = I_{k+l}$. ✓. For $k \geq 0, l = -m < 0$: $A \cdot a^m A = a^m A = I_{k-m}$. If $k \geq m$, $I_{k-m} = A \supset a^m A$. ✓. If $k < m$, $I_{k-m} = I_{-(m-k)} = a^{m-k} A \supset a^m A$. ✓ (since $a^m A \subset a^{m-k} A$). For $k = -m, l = -n$ both negative: $a^m A \cdot a^n A = a^{m+n} A = I_{-(m+n)}$. ✓.

Good. So $B = A[x, ax^{-1}] = \bigoplus_{k \geq 0} A x^k \oplus \bigoplus_{m > 0} a^m A x^{-m}$.

Now, the integral closure of $B$ in $K(x) = \text{Frac}(B)$: An element $f \in K(x)$ integral over $B$ must be integral over $B_\mathfrak{p}$ for every prime ideal $\mathfrak{p}$ of $B$. By Serre's criterion, $B$ is integrally closed iff $B$ satisfies $R_1$ (regular in codimension 1) and $S_2$ (Serre's condition).

Actually, let me think about this differently. The ring $B = A[x, ax^{-1}]$ is $\mathbb{Z}$-graded. The integral closure of a graded ring in its fraction field is also graded (with the same grading group). So the integral closure $\bar{B}$ is $\bigoplus_{k \in \mathbb{Z}} J_k x^k$ for some $A$-submodules $J_k$ of $K$ with $J_k \supset I_k$.

An element $\alpha x^k \in K \cdot x^k$ (with $\alpha \in K$) is in $\bar{B}$ iff it's integral over $B$. Since $B$ is graded, $\alpha x^k$ is integral over $B$ iff $\alpha x^k$ satisfies a homogeneous monic polynomial... actually, integrality in graded rings: $\alpha x^k$ is integral over $B$ iff there exist $b_1, \ldots, b_n \in B$ such that $(\alpha x^k)^n + b_1 (\alpha x^k)^{n-1} + \cdots + b_n = 0$.

Hmm, this is getting complicated. Let me use a more concrete approach.

Let me use the characterization: $B$ is integrally closed iff $B = \bigcap_{\text{ht}(\mathfrak{p})=1} B_\mathfrak{p}$ (intersection over height-1 primes, in the fraction field).

The height-1 primes of $B = A[x, ax^{-1}]$: These come from height-1 primes of $A$ (extended) and possibly the "boundary" primes related to $x = 0$ or $ax^{-1} = 0$ (i.e., $a = 0$).

Actually, let me think about it via the covering $K[x, x^{-1}] \supset B$. The ring $K[x, x^{-1}]$ is a PID (Laurent polynomial ring over a field), so it's integrally closed. The relationship between $B$ and $K[x, x^{-1}]$ is:

$B = A[x, ax^{-1}]$ and $K[x, x^{-1}]$ is the localization of $B$ at $S = A \setminus \{0\}$ (roughly). Actually, $S^{-1} B = K[x, ax^{-1}]$. And $K[x, ax^{-1}] = K[x, x^{-1}]$ since $a/x = a \cdot x^{-1}$ and $a \in K^*$, so $x^{-1} = a^{-1} \cdot (a/x) \in K[x, ax^{-1}]$. So $S^{-1}B = K[x, x^{-1}]$.

Now, $B$ is integrally closed iff $B = \bar{B}$ where $\bar{B}$ is the integral closure in $K(x)$. Since $K[x, x^{-1}]$ is integrally closed and contains $B$, $\bar{B} \subset K[x, x^{-1}]$.

So $\bar{B} \subset K[x, x^{-1}] = \bigoplus_{k \in \mathbb{Z}} K x^k$.

An element $f = \sum_k c_k x^k \in K[x, x^{-1}]$ is in $\bar{B}$ iff $f$ is integral over $B$.

Since $B$ is $\mathbb{Z}$-graded and the grading is compatible, $f$ is integral over $B$ iff each homogeneous component $c_k x^k$ is integral over $B$ (this is a standard fact for graded rings: the integral closure of a $\mathbb{Z}$-graded domain in its fraction field is $\mathbb{Z}$-graded, and a homogeneous element $\alpha x^k$ is integral iff $\alpha$ is integral over a certain ring).

Actually, let me be more precise. For a $\mathbb{Z}$-graded domain $B = \bigoplus B_k$ with fraction field $L$, the integral closure $\bar{B}$ is also $\mathbb{Z}$-graded: $\bar{B} = \bigoplus \bar{B}_k$ where $\bar{B}_k = \bar{B} \cap L \cdot e^k$ (where $e$ is a homogeneous element of degree 1, here $x$). And $\alpha x^k \in \bar{B}_k$ iff $\alpha x^k$ is integral over $B$.

Now, $\alpha x^k$ is integral over $B$ iff $\alpha x^k$ satisfies a monic polynomial with coefficients in $B$. By the grading, we can assume the polynomial is "weighted homogeneous" in some sense. Specifically, $\alpha x^k$ is integral over $B$ iff there exist $n$ and $b_i \in B_{ki}$ (the degree $ki$ part of $B$) such that $(\alpha x^k)^n + b_1 (\alpha x^k)^{n-1} + \cdots + b_n = 0$, i.e., $\alpha^n x^{kn} + b_1 \alpha^{n-1} x^{k(n-1)} + \cdots + b_n = 0$ with $b_i \in B_{ki}$.

This means $\alpha^n + c_1 \alpha^{n-1} + \cdots + c_n = 0$ where $c_i = b_i / x^{ki} \in B_{ki} / x^{ki} \subset K$ (since $B_{ki} \subset K \cdot x^{ki}$, dividing by $x^{ki}$ gives an element of $K$).

So $\alpha x^k$ is integral over $B$ iff $\alpha$ is integral over the subring $R_k := \{b / x^k : b \in B_k\} \subset K$... no, that's not quite right either. Let me reconsider.

$\alpha x^k$ integral over $B$ means: $\exists n, \exists b_1 \in B_{k}, b_2 \in B_{2k}, \ldots, b_n \in B_{nk}$ such that $(\alpha x^k)^n + b_1 (\alpha x^k)^{n-1} + \cdots + b_n = 0$.

Dividing by $x^{kn}$: $\alpha^n + (b_1/x^k) \alpha^{n-1} + (b_2/x^{2k}) \alpha^{n-2} + \cdots + (b_n/x^{nk}) = 0$.

So $\alpha$ is integral over the ring generated by $\{b/x^{ik} : b \in B_{ik}, i \geq 1\} \subset K$.

Hmm, this depends on $k$. Let me consider different cases.

**Case $k \geq 0$**: $B_k = A x^k$, so $B_k / x^k = A$. For $ik \geq 0$, $B_{ik} = A x^{ik}$, so $b/x^{ik} \in A$. So $\alpha$ is integral over $A$. Since $A$ is a UFD (hence integrally closed), $\alpha \in A$. So $\bar{B}_k = A x^k = B_k$ for $k \geq 0$.

**Case $k < 0$, say $k = -m$ with $m > 0$**: $B_{-m} = a^m A x^{-m}$, so $B_{-m}/x^{-m} = a^m A$. For $ik = -im$, $B_{-im} = a^{im} A x^{-im}$, so $b/x^{-im} \in a^{im} A$.

So $\alpha$ is integral over the subring of $K$ generated by $\{a^{im} A : i \geq 1\} = a^m A$ (since $a^{im} A \subset a^m A$ for $i \geq 1$, and $a^m A$ is already a ring... wait, is $a^m A$ a ring? It's an ideal, not a ring (it doesn't contain 1 unless $a$ is a unit).)

Hmm, the subring generated by $a^m A$ (as a set) inside $K$: this is $A[a^m A] = A$ (since $a^m A \subset A$ and $A$ is already a ring). Wait, no. The set $\{b/x^{-im} : b \in B_{-im}\} = a^{im} A$ for $i \geq 1$. The subring of $K$ generated by $\bigcup_{i \geq 1} a^{im} A$ is just $A$ (since all these are subsets of $A$, and $A$ is the smallest subring containing them... well, $A$ contains all of them, and the subring generated by them is contained in $A$, but does it equal $A$? It contains $a^m A$, and the subring generated by $a^m A$ is $\mathbb{Z}[a^m A]$... hmm, if $A$ is a $k$-algebra, then it's $k[a^m A] = k[a^m \cdot A]$. Since $a^m \cdot 1 = a^m \in a^m A$, we get $a^m$ is in the generated subring, and then $a^m \cdot (a^{-m} \cdot a^m) $... this is getting circular.

Let me reconsider. The subring of $K$ generated by $\bigcup_{i \geq 1} a^{im} A$ is the smallest subring of $K$ containing all elements of $a^{im} A$ for all $i \geq 1$. Since $a^m A \supset a^{2m} A \supset \cdots$, the union is just $a^m A$ (the largest one). The subring generated by $a^m A$ (as a subset of $K$) is the set of all finite sums of products of elements in $a^m A$ and their... no, subring generated means: all polynomial expressions in elements of $a^m A$ with integer (or base ring) coefficients. Since $a^m A$ is closed under multiplication ($(a^m r)(a^m s) = a^{2m} rs \in a^{2m} A \subset a^m A$) and addition, the subring generated by $a^m A$ is $a^m A \cup \{0\}$... no, a subring must contain 1 (depending on convention) or at least be closed under the operations.

Actually, the subring generated by a subset $S$ of a ring $R$ is the intersection of all subrings containing $S$. If we require subrings to contain 1, then the subring generated by $a^m A$ is $A$ itself (since $A$ is the smallest subring of $K$ containing $a^m A$ and 1, because $a^m \in a^m A$ and if $a^m$ is in the subring, then... well, we need $a^{-m}$ to get back to $A$, but $a^{-m}$ might not be in the subring).

Hmm, I think I'm overcomplicating this. Let me reconsider.

The condition is: $\alpha$ is integral over the ring $R$ where $R$ is the subring of $K$ generated by $\{c \in K : c = b/x^{ik} \text{ for some } b \in B_{ik}, i \geq 1\}$.

For $k = -m$: $R$ is generated by $\bigcup_{i \geq 1} a^{im} A$. Since $a^m \in a^m A$ and $a^{2m} \in a^{2m} A \subset a^m A$, etc., and $a^m A$ is closed under multiplication, $R$ is the subring generated by $a^m A$, which (if we include 1) is $A[a^m A] = A$ (since $a^m A \subset A$). Wait, but that would mean $\alpha$ is integral over $A$, hence $\alpha \in A$ (since $A$ is integrally closed), and then $\alpha x^{-m} \in A x^{-m}$. But $B_{-m} = a^m A x^{-m}$, so we'd need $\alpha \in a^m A$ for $\alpha x^{-m} \in B_{-m}$.

So if $\alpha \in A$ but $\alpha \notin a^m A$, then $\alpha x^{-m} \in \bar{B}_{-m}$ but $\alpha x^{-m} \notin B_{-m}$. This would mean $B$ is not integrally closed!

But wait, I need to double-check that $\alpha$ integral over $R = A$ is the right condition. Let me re-examine.

$\alpha x^{-m}$ is integral over $B$ means there exist $b_1 \in B_{-m}, b_2 \in B_{-2m}, \ldots, b_n \in B_{-nm}$ such that:
$$(\alpha x^{-m})^n + b_1 (\alpha x^{-m})^{n-1} + \cdots + b_n = 0$$

This gives: $\alpha^n x^{-mn} + b_1 \alpha^{n-1} x^{-m(n-1)} + \cdots + b_n = 0$.

Now $b_i \in B_{-im} = a^{im} A x^{-im}$, so $b_i = a^{im} c_i x^{-im}$ for some $c_i \in A$.

Substituting: $\alpha^n x^{-mn} + a^m c_1 \alpha^{n-1} x^{-m(n-1)} + a^{2m} c_2 \alpha^{n-2} x^{-m(n-2)} + \cdots + a^{nm} c_n = 0$.

Dividing by $x^{-mn}$ (i.e., multiplying by $x^{mn}$): $\alpha^n + a^m c_1 \alpha^{n-1} x^{m} + a^{2m} c_2 \alpha^{n-2} x^{2m} + \cdots + a^{nm} c_n x^{nm} = 0$.

But this is an equation in $K(x)$, and the terms have different powers of $x$! So for this to be zero, each coefficient must be zero:
- $\alpha^n = 0$ (coefficient of $x^0$) — but $\alpha \neq 0$ in a domain, contradiction!

Wait, that can't be right. Let me reconsider.

Oh, I see the issue. The equation $(\alpha x^{-m})^n + b_1 (\alpha x^{-m})^{n-1} + \cdots + b_n = 0$ is an equation in $K(x)$, and all terms should have the same degree for it to be a "homogeneous" integrality relation. But I was assuming the $b_i$ are homogeneous of degree $-im$, which makes the $i$-th term have degree $-m(n-i) + (-im) = -mn + im - im = -mn$. Wait, let me recompute.

$(\alpha x^{-m})^{n-i}$ has degree $-m(n-i)$. And $b_i$ has degree $-im$. So the product $b_i (\alpha x^{-m})^{n-i}$ has degree $-m(n-i) - im = -mn + mi - im = -mn$. And $(\alpha x^{-m})^n$ has degree $-mn$. So all terms have degree $-mn$. Good, so the equation is homogeneous of degree $-mn$.

So dividing by $x^{-mn}$ (multiplying by $x^{mn}$):
$\alpha^n + a^m c_1 \alpha^{n-1} + a^{2m} c_2 \alpha^{n-2} + \cdots + a^{nm} c_n = 0$.

This is an equation in $K$ (no $x$ anymore). So $\alpha$ satisfies:
$$\alpha^n + a^m c_1 \alpha^{n-1} + a^{2m} c_2 \alpha^{n-2} + \cdots + a^{nm} c_n = 0$$
with $c_i \in A$.

This means $\alpha$ is integral over the ring $A[a^m] = A$ (since $a^m \in A$). Wait, more precisely, $\alpha$ is integral over the subring of $K$ generated by $a^m A$ (and 1). But $a^m A \subset A$, so this subring is contained in $A$. And it contains $a^m$ (take $c = 1 \in A$, then $a^m \cdot 1 = a^m$). 

Hmm, but the subring generated by $a^m A$ (and 1) might be smaller than $A$. It's $A$ iff $a^m$ is a unit or generates $A$ as a ring... no. The subring generated by $1$ and $a^m A$ is $\mathbb{Z}[a^m A]$ (or $k[a^m A]$ if $A$ is a $k$-algebra). This is the set of all polynomial expressions in elements of $a^m A$ with coefficients in $\mathbb{Z}$ (or $k$). Since $a^m A$ is an ideal of $A$ closed under multiplication, $k[a^m A]$ consists of elements of the form $c_0 + c_1 s_1 + c_2 s_1 s_2 + \cdots$ where $c_i \in k$ and $s_i \in a^m A$. But $s_1 s_2 \in a^{2m} A \subset a^m A$, etc. So $k[a^m A] = k + a^m A$ (as a $k$-vector space, it's $k \cdot 1 + a^m A$, since products of elements in $a^m A$ land in $a^{2m} A \subset a^m A$).

So the subring is $k + a^m A$ (assuming $A$ is a $k$-algebra; more generally, it's $\mathbb{Z} + a^m A$ or the image of $\mathbb{Z} \to A$ plus $a^m A$). Let me call this $R_m = k + a^m A$.

So $\alpha x^{-m} \in \bar{B}$ iff $\alpha$ is integral over $R_m = k + a^m A$.

Now, $R_m \subset A$, and $A$ is integral over $R_m$? Not necessarily. But we need: what is the integral closure of $R_m$ in $K$?

If $a$ is square-free, is $A$ integral over $R_m = k + a^m A$? 

Hmm, this is getting complicated. Let me try a different, cleaner approach.

Let me use the fact that $B = A[x, ax^{-1}]$ and consider the normalization.

Actually, I think there's a cleaner way using the theory of Rees-like algebras or blow-up algebras.

Note that $A[x, ax^{-1}]$ is related to the blow-up of $\text{Spec}(A)$ along the ideal $(a)$. Specifically, the blow-up algebra is $\text{Rees}(a) = A[at] = \bigoplus_{n \geq 0} a^n t^n \subset A[t]$, and the associated graded ring is $\text{gr}_a(A) = \bigoplus a^n / a^{n+1}$.

Actually, $A[x, ax^{-1}]$ is the "affine chart" of the blow-up. More precisely, if we blow up $\text{Spec}(A)$ at the ideal $(a)$, one affine chart is $\text{Spec}(A[a/x])$ where $x$ is the blow-up variable. But $A[x, ax^{-1}]$ includes both $x$ and $a/x$, so it's more like the "full" blow-up algebra in some sense.

Hmm, actually I think $A[x, ax^{-1}]$ is the symbolic Rees algebra or something related. Let me think again.

$A[x, ax^{-1}] = \bigoplus_{n \in \mathbb{Z}} I_n x^n$ where $I_n = A$ for $n \geq 0$ and $I_n = a^{-n} A = a^{|n|} A$ for $n < 0$.

This is the "extended Rees algebra" of the ideal $(a)$! The extended Rees algebra is $A[t, t^{-1}]$ with a specific grading... no. The extended Rees algebra of an ideal $I$ is $R = \bigoplus_{n \in \mathbb{Z}} I^n t^n$ where $I^n = A$ for $n \leq 0$ (by convention) and $I^n$ for $n > 0$. Wait, that's $A[t, It^{-1}] = \bigoplus_{n \geq 0} A t^n \oplus \bigoplus_{n > 0} I^n t^{-n}$.

Yes! $A[x, ax^{-1}]$ with $I = (a)$ is exactly the extended Rees algebra $A[t, at^{-1}]$ (with $t = x$). The extended Rees algebra of $I = (a)$ is:
$$R = A[t, at^{-1}] = \bigoplus_{n \geq 0} A t^n \oplus \bigoplus_{n > 0} a^n A t^{-n}$$

And there's a well-known result: **the extended Rees algebra $A[t, It^{-1}]$ is integrally closed if and only if $A$ is integrally closed and $I$ is integrally closed** (as an ideal, meaning $I = \bar{I}$, the integral closure of the ideal).

Wait, is that right? Let me recall. The integral closure of an ideal $I$ in a domain $A$ is $\bar{I} = \{x \in A : x \text{ is integral over } I\}$, where $x$ integral over $I$ means $x$ satisfies $x^n + a_1 x^{n-1} + \cdots + a_n = 0$ with $a_i \in I^i$.

And the result is: the Rees algebra $A[It] = \bigoplus_{n \geq 0} I^n t^n$ is integrally closed iff $A$ is integrally closed and $I$ is integrally closed (i.e., $I = \bar{I}$).

For the extended Rees algebra, I believe a similar result holds: $A[t, It^{-1}]$ is integrally closed iff $A$ is integrally closed and $I$ is integrally closed.

Now, in a UFD, when is the principal ideal $(a)$ integrally closed? 

The integral closure of $(a)$ is $\bar{(a)} = \{x \in A : x \text{ integral over } (a)\}$. For a principal ideal $(a)$ in a UFD, $\bar{(a)} = (\sqrt{a})$... no, that's not right either.

Actually, the integral closure of a principal ideal $(a)$ in an integrally closed domain is $(a)$ itself... no, that's not right. Let me think.

In a UFD (or more generally, a Krull domain), the integral closure of an ideal $I$ is $\bar{I} = \bigcap_{v} \{x : v(x) \geq v(I)\}$ where the intersection is over all DVR valuations $v$ of $K$ associated to height-1 primes, and $v(I) = \min_{y \in I} v(y)$.

For $I = (a)$: $v((a)) = v(a)$ for each valuation $v$. So $\bar{(a)} = \{x \in A : v(x) \geq v(a) \text{ for all } v\} = \{x \in A : v(x) \geq v(a) \text{ for all height-1 primes } \mathfrak{p}\}$.

In a UFD, the height-1 primes are $(p)$ for irreducible $p$, and $v_p(x)$ is the $p$-adic valuation. So $\bar{(a)} = \{x \in A : v_p(x) \geq v_p(a) \text{ for all irreducible } p\}$.

If $a = u \prod p_i^{e_i}$, then $v_{p_i}(a) = e_i$ and $v_q(a) = 0$ for $q \neq p_i$. So $\bar{(a)} = \{x \in A : v_{p_i}(x) \geq e_i \text{ for all } i, \text{ and } v_q(x) \geq 0 \text{ for } q \neq p_i\} = \{x \in A : p_i^{e_i} | x \text{ for all } i\} = (\prod p_i^{e_i}) \cdot A = (a)$.

Wait, so $\bar{(a)} = (a)$ always? That would mean principal ideals in UFDs are always integrally closed, and hence the extended Rees algebra is always integrally closed, contradicting my earlier example.

Let me re-examine. In my example, $A = k[t]$, $a = t^2$. Then $(a) = (t^2)$, and $\bar{(t^2)} = \{x \in k[t] : v_t(x) \geq 2\} = (t^2)$. So $(t^2)$ is integrally closed as an ideal. Then by the theorem, $A[x, ax^{-1}] = k[t][x, t^2 x^{-1}]$ should be integrally closed. But I showed earlier that it's NOT integrally closed (the $A_1$ singularity).

So either my recollection of the theorem is wrong, or my example is wrong. Let me re-examine the example.

$B = k[t, X, Y]/(XY - t^2)$. I claimed this is the $A_1$ singularity and is not integrally closed, with normalization $k[u, v]$ via $t \mapsto uv, X \mapsto u^2, Y \mapsto v^2$.

Let me verify: is $u$ in the fraction field of $B$? $u = X/t = u^2/(uv) = u/v$... hmm, $u = X/t$ in $\text{Frac}(B)$. And $u^2 = X \in B$, so $u$ satisfies $Z^2 - X = 0$, which is monic with coefficients in $B$. So $u$ is integral over $B$. And $u \notin B$ (since $B$ maps to $k[u^2, v^2, uv]$, the Veronese subring, and $u$ has odd degree). So $B$ is not integrally closed. ✓.

Now, is $B = k[t][x, t^2/x]$? We have $B = k[t, X, Y]/(XY - t^2)$. Setting $x = X$ and $t^2/x = Y$ (i.e., $Y = t^2/X$), we get $B = k[t][X, t^2/X]$. Yes, this is $A[x, ax^{-1}]$ with $A = k[t]$, $a = t^2$.

So the extended Rees algebra $k[t][x, t^2 x^{-1}]$ is NOT integrally closed, even though $(t^2)$ is integrally closed as an ideal in $k[t]$.

So my recollection of the theorem must be wrong. Let me reconsider.

Actually, I think the correct theorem is about the Rees algebra $A[It] = \bigoplus_{n \geq 0} I^n t^n$, not the extended Rees algebra. And the result is:

- $A[It]$ is integrally closed iff $A$ is integrally closed and $I$ is integrally closed.

But the extended Rees algebra $A[t, It^{-1}]$ is a different beast. Let me think about what its integral closure is.

The extended Rees algebra $R = A[t, It^{-1}]$ has the property that $R/(t^{-1}) \cong \text{gr}_I(A)$ (the associated graded ring) and $R[t^{-1}] \cong A[t, t^{-1}]$ (which is integrally closed if $A$ is).

Hmm, I think the integral closure of the extended Rees algebra $A[t, It^{-1}]$ is $\bigoplus_{n \in \mathbb{Z}} \overline{I^n} t^n$ where $\overline{I^n}$ is the integral closure of $I^n$ (with $I^0 = A$ and $I^n = A$ for $n \leq 0$ by convention). Wait, but for $n \leq 0$, $I^n = A$, and for $n > 0$, $I^n = (a^n)$.

So the integral closure of $A[x, ax^{-1}]$ would be $\bigoplus_{n \geq 0} A x^n \oplus \bigoplus_{n > 0} \overline{(a^n)} x^{-n}$.

In a UFD, $\overline{(a^n)} = (a^n)$ (as I computed, principal ideals in UFDs are integrally closed). So the integral closure would be $A[x, ax^{-1}]$ itself, contradicting the example.

Something is wrong. Let me reconsider.

Oh wait, I think the issue is that the integral closure of the extended Rees algebra is NOT simply $\bigoplus \overline{I^n} t^n$. The grading argument I was making earlier showed that the integral closure is graded, but the graded pieces are not simply $\overline{I^n}$.

Let me redo the computation. We have $B = \bigoplus_{n \geq 0} A x^n \oplus \bigoplus_{n > 0} a^n A x^{-n}$, and $\bar{B} = \bigoplus_{n \in \mathbb{Z}} \bar{B}_n$ where $\bar{B}_n \subset K x^n$.

For $n \geq 0$: I showed $\bar{B}_n = A x^n$ (since $\alpha$ integral over $A$ implies $\alpha \in A$). ✓.

For $n = -m < 0$: $\alpha x^{-m} \in \bar{B}_{-m}$ iff $\alpha$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + a^{2m} c_2 \alpha^{N-2} + \cdots + a^{Nm} c_N = 0$ for some $c_i \in A$.

This means $\alpha$ is integral over the ideal $(a^m)$ in a specific sense. Let me think about what this means.

The equation is $\alpha^N + \sum_{i=1}^N a^{im} c_i \alpha^{N-i} = 0$, which can be rewritten as $\alpha^N \in (a^m \alpha^{N-1}, a^{2m} \alpha^{N-2}, \ldots, a^{Nm})$.

This is the condition that $\alpha$ is integral over the ideal $(a^m)$ in the sense of integral dependence on ideals: $\alpha$ is integral over the ideal $J = (a^m)$ means $\alpha$ satisfies a monic polynomial $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i \in J^i = (a^{mi})$.

So $\alpha x^{-m} \in \bar{B}_{-m}$ iff $\alpha \in \overline{(a^m)}$ (the integral closure of the ideal $(a^m)$).

Now, in a UFD, what is $\overline{(a^m)}$?

As I computed, for a principal ideal $(b)$ in a UFD, $\overline{(b)} = (b)$. So $\overline{(a^m)} = (a^m)$.

But this gives $\bar{B}_{-m} = a^m A x^{-m} = B_{-m}$, so $\bar{B} = B$, meaning $B$ is integrally closed. This contradicts the example!

Let me re-examine the example more carefully. $A = k[t]$, $a = t^2$, $B = k[t][x, t^2 x^{-1}]$.

The element $u = x/t$ is in $\text{Frac}(B)$. We have $u^2 = x^2/t^2$. And $x \cdot (t^2/x) = t^2$, so $t^2 = x \cdot (t^2 x^{-1})$. Then $u^2 = x^2/t^2 = x/(t^2/x) = x/(t^2 x^{-1})$.

In terms of the grading: $x$ has degree 1, $t^2 x^{-1}$ has degree $-1$, $t$ has degree 0. So $u = x/t$ has degree 1. And $u^2 = x^2/t^2$ has degree 2.

Now, $u^2 = x^2/t^2$. Is $u^2 \in B$? $u^2 = x^2/t^2$. The degree-2 part of $B$ is $A x^2 = k[t] x^2$. Is $x^2/t^2 \in k[t] x^2$? That would require $1/t^2 \in k[t]$, which is false. So $u^2 \notin B$.

But $u^2 = x^2/t^2$ and $u$ satisfies $u^2 - x^2/t^2 = 0$, which is $Z^2 - x^2/t^2 = 0$. But $x^2/t^2 \notin B$ (it's in $K$ but not in $A = k[t]$). So this is NOT a monic polynomial with coefficients in $B$!

Wait, but I said $u^2 = X$ where $X = x$ in the original notation... no. Let me redo. In the example, $B = k[t, X, Y]/(XY - t^2)$ with $x = X$, $Y = t^2/x$. And the normalization map is $t \mapsto uv, X \mapsto u^2, Y \mapsto v^2$. So $u^2 = X = x$ and $v^2 = Y = t^2/x$.

So $u^2 = x \in B$! And $u$ satisfies $Z^2 - x = 0$, which IS monic with coefficient $x \in B$. So $u$ is integral over $B$.

Now, $u = x/t$. In the grading, $x$ has degree 1 and $t$ has degree 0, so $u$ has degree 1. And $u^2 = x$ has degree 1... wait, $u^2$ should have degree 2 if $u$ has degree 1. But $x$ has degree 1. Contradiction!

The issue is that $u = x/t$ is NOT homogeneous of degree 1 in the $\mathbb{Z}$-grading of $B$. The grading is on $B$, and $u \in \text{Frac}(B)$, but $u$ is not a homogeneous element of $\text{Frac}(B)$ with respect to this grading... or is it?

Actually, the fraction field of a graded ring doesn't have a natural grading. The grading extends to the fraction field only in a limited way. Let me reconsider.

$B = \bigoplus_{n \in \mathbb{Z}} B_n$ where $B_n = A x^n$ for $n \geq 0$ and $B_n = a^{|n|} A x^n$ for $n < 0$. The fraction field of $B$ is $K(x)$ where $K = \text{Frac}(A)$, since $B \subset K[x, x^{-1}]$ and $K[x, x^{-1}]$ has fraction field $K(x)$... actually $K[x, x^{-1}]$ is already a field? No, $K[x, x^{-1}]$ is the Laurent polynomial ring, which is not a field. Its fraction field is $K(x)$, the field of rational functions.

So $\text{Frac}(B) = K(x)$.

Now, $u = x/t$ where $t \in A \subset B_0$. So $u = x \cdot t^{-1}$. In the "graded fraction field," $x$ has degree 1 and $t^{-1}$ has degree 0, so $u$ has degree 1. And $u^2 = x^2/t^2$ has degree 2. But $u^2 = x$ (from the normalization map)... 

Wait, no! $u^2 = x$ is in the normalization, not in $B$ itself. Let me be more careful. In the normalization $k[u,v]$, we have $x = u^2$, $t = uv$, $Y = v^2$. So $u = x/t = u^2/(uv) = u/v$. And $u^2 = x$. But this is in $k[u,v]$, not in $B$.

In $B$, $u$ is an element of $\text{Frac}(B) = K(x)$ where $K = k(t)$. We have $u = x/t \in K(x)$ (since $x \in B$ and $t \in B$). And $u^2 = x^2/t^2 \in K(x)$. The relation $u^2 = x$ would mean $x^2/t^2 = x$, i.e., $x = t^2$, which is NOT true in $B$ (there's no such relation).

So I made an error. The normalization map sends $x \mapsto u^2$, but that doesn't mean $u^2 = x$ in $\text{Frac}(B)$. It means that under the inclusion $B \hookrightarrow k[u,v]$, $x$ maps to $u^2$. But $u$ is not in $\text{Frac}(B)$ in a way that makes $u^2 = x$.

Hmm, wait. The normalization of $B$ is the integral closure $\bar{B}$ in $\text{Frac}(B)$. The map $B \to k[u,v]$ given by $t \mapsto uv, x \mapsto u^2, Y \mapsto v^2$ is an inclusion (since $B = k[u^2, v^2, uv] \subset k[u,v]$). And $k[u,v]$ is the integral closure of $B$ in... what field?

$\text{Frac}(B) = \text{Frac}(k[u^2, v^2, uv])$. What is this fraction field? $u^2, v^2, uv$ generate the fraction field $k(u,v)$ (since $u = u^2 \cdot v / (uv) \cdot ... $ hmm, $u = (u^2 v)/(uv)$... but $v$ is not in the fraction field of $B$ directly. Actually, $u^2 / (uv) = u/v$ and $v^2/(uv) = v/u$, so $u/v \in \text{Frac}(B)$ and $v/u \in \text{Frac}(B)$. And $uv \in B$. So $(u/v) \cdot (uv) = u^2 \in B$ and $(u/v)^2 \cdot (uv)^2 = u^2 v^2 \cdot ... $ hmm. Let me think: $\text{Frac}(B)$ contains $u^2, v^2, uv$. From these, $u^2 \cdot v^2 / (uv)^2 = 1$, so that's trivial. $u^2/(uv) = u/v$ and $v^2/(uv) = v/u$. So $u/v \in \text{Frac}(B)$. Then $(uv) \cdot (u/v) = u^2 \in B$ and $(uv)/(u/v) = v^2 \in B$. Can we get $u$ itself? $u = \sqrt{u^2}$, but square roots aren't in the fraction field in general. Actually, $u = (uv) \cdot u / (uv) $... we need $u$ in terms of $u^2, v^2, uv$. We have $u^2$ and $uv$, so $u = u^2 \cdot v / (uv \cdot v) $... this is circular.

Actually, $\text{Frac}(k[u^2, v^2, uv])$: the transcendence degree is 2 (since $k[u^2, v^2, uv]$ has Krull dimension 2). And $k(u,v)$ also has transcendence degree 2 over $k$. Is $\text{Frac}(k[u^2, v^2, uv]) = k(u,v)$? 

We need to check if $u \in \text{Frac}(k[u^2, v^2, uv])$. $u = u^2 / u$, but $u$ is not in the ring. However, $u^2 \cdot v = u \cdot (uv)$, so $u = (u^2 v)/(uv)$. But $v$ is not in $\text{Frac}(B)$ either (by the same argument). Hmm, but $v = v^2 / v$ and $v = (uv)/u$, both circular.

Let me think about it differently. $k(u^2, v^2, uv) \subset k(u,v)$. The extension $k(u,v) / k(u^2, v^2, uv)$: note that $u^2, v^2, uv$ are all invariant under the involution $(u,v) \mapsto (-u, -v)$. So $k(u^2, v^2, uv) = k(u,v)^{\langle \sigma \rangle}$ where $\sigma(u,v) = (-u,-v)$, and $[k(u,v) : k(u^2, v^2, uv)] = 2$.

So $\text{Frac}(B) = k(u^2, v^2, uv) \neq k(u,v)$. The integral closure of $B$ is in $\text{Frac}(B) = k(u^2, v^2, uv)$, not in $k(u,v)$.

So is $u \in \text{Frac}(B) = k(u^2, v^2, uv)$? No! $u \notin k(u^2, v^2, uv)$ (since $u$ is not invariant under $\sigma$). So $u$ is NOT in the fraction field of $B$, and the "normalization" $k[u,v]$ is NOT the integral closure of $B$ in its fraction field.

This means my earlier analysis was wrong. $k[u,v]$ is not the integral closure of $B$ in $\text{Frac}(B)$. The integral closure of $B$ in $\text{Frac}(B) = k(u^2, v^2, uv)$ is something else.

So maybe $B = k[t, X, Y]/(XY - t^2)$ IS integrally closed? Let me check using Serre's criterion.

$B = k[t, X, Y]/(XY - t^2)$. This is a 2-dimensional domain (since $k[t,X,Y]$ is 3-dimensional and we quotient by one equation). The singular locus is where the Jacobian matrix has rank $< 1$: $\partial(XY - t^2)/\partial X = Y$, $\partial/\partial Y = X$, $\partial/\partial t = -2t$. The singular locus is $X = Y = t = 0$, which is the origin, a point of codimension 2.

By Serre's criterion, $B$ is normal iff $R_1$ (regular in codimension 1) and $S_2$ (Serre's condition). $R_1$: the singular locus has codimension 2, so $B$ is regular in codimension 1. ✓. $S_2$: $B$ is a hypersurface (complete intersection), hence Cohen-Macaulay, hence $S_2$. ✓.

So $B = k[t,X,Y]/(XY - t^2)$ IS integrally closed! My earlier claim that it's the $A_1$ singularity and not integrally closed was WRONG.

Wait, but the $A_1$ surface singularity $k[u^2, v^2, uv]$ is well-known to not be integrally closed (its normalization is $k[u,v]$). And $k[u^2, v^2, uv] \cong k[t,X,Y]/(XY - t^2)$ via $t = uv, X = u^2, Y = v^2$. So there's a contradiction.

The resolution: $k[u^2, v^2, uv]$ is NOT integrally closed IN $k(u,v)$, but its fraction field is $k(u^2, v^2, uv) \neq k(u,v)$. The integral closure of $k[u^2, v^2, uv]$ in its OWN fraction field $k(u^2, v^2, uv)$ might be itself!

Let me check: is $k[u^2, v^2, uv]$ integrally closed in $k(u^2, v^2, uv)$?

An element of $k(u^2, v^2, uv)$ integral over $k[u^2, v^2, uv]$: since $k[u^2, v^2, uv]$ is the invariant ring $k[u,v]^{\langle \sigma \rangle}$ where $\sigma: (u,v) \mapsto (-u,-v)$, and $k[u,v]$ is integral over $k[u^2, v^2, uv]$ (since $u$ satisfies $Z^2 - u^2 = 0$), the integral closure of $k[u^2, v^2, uv]$ in $k(u,v)$ is $k[u,v]$.

But in $k(u^2, v^2, uv)$: an element $\alpha \in k(u^2, v^2, uv)$ integral over $k[u^2, v^2, uv]$ is also in $k(u,v)$ (since $k(u^2, v^2, uv) \subset k(u,v)$) and integral over $k[u^2, v^2, uv]$, hence in $k[u,v]$ (the integral closure in $k(u,v)$). So $\alpha \in k[u,v] \cap k(u^2, v^2, uv)$.

Now, $k[u,v] \cap k(u^2, v^2, uv)$: an element of $k[u,v]$ that is in $k(u^2, v^2, uv)$ must be invariant under $\sigma$ (since $k(u^2, v^2, uv) = k(u,v)^{\sigma}$). So $k[u,v] \cap k(u^2, v^2, uv) = k[u,v]^{\sigma} = k[u^2, v^2, uv]$.

So the integral closure of $k[u^2, v^2, uv]$ in $k(u^2, v^2, uv)$ is $k[u^2, v^2, uv]$ itself. It IS integrally closed!

This makes sense with the Serre's criterion argument. The $A_1$ singularity $k[u^2, v^2, uv]$ is a normal surface (it's a rational double point, which is normal). The fact that $k[u,v]$ is "bigger" is because $k[u,v]$ is the normalization in a BIGGER field $k(u,v)$, not in the fraction field of $k[u^2, v^2, uv]$.

OK so I was wrong. $B = k[t,X,Y]/(XY - t^2)$ IS integrally closed. So the example with $a = t^2$ doesn't give a counterexample.

Let me reconsider the problem. Maybe $A[x, a/x]$ is always integrally closed when $A$ is a UFD?

Going back to the grading argument: $\bar{B}_{-m} = \overline{(a^m)} x^{-m}$ where $\overline{(a^m)}$ is the integral closure of the ideal $(a^m)$ in $A$. And in a UFD, $\overline{(a^m)} = (a^m)$ (principal ideals in integrally closed domains are integrally closed... wait, is that true?).

Hmm, actually, I need to be more careful. The integral closure of an ideal $I$ in a domain $A$ is $\bar{I} = \{x \in A : x^n + a_1 x^{n-1} + \cdots + a_n = 0, a_i \in I^i\}$. For a principal ideal $(a)$ in a UFD, is $\overline{(a)} = (a)$?

In a Krull domain (which includes UFDs), the integral closure of an ideal $I$ is $\bar{I} = \{x \in A : v(x) \geq v(I) \text{ for all essential valuations } v\}$, where $v(I) = \min_{y \in I} v(y)$.

For $I = (a^m)$: $v((a^m)) = m \cdot v(a)$ for each valuation $v$. So $\overline{(a^m)} = \{x \in A : v(x) \geq m \cdot v(a) \text{ for all } v\}$.

In a UFD, the essential valuations are $v_p$ for irreducible $p$. If $a = u \prod p_i^{e_i}$, then $v_{p_i}(a) = e_i$ and $v_q(a) = 0$ for $q \neq p_i$. So $v_{p_i}((a^m)) = me_i$ and $v_q((a^m)) = 0$.

$\overline{(a^m)} = \{x \in A : v_{p_i}(x) \geq me_i \text{ for all } i\} = (\prod p_i^{me_i}) A = (a^m)$.

So yes, $\overline{(a^m)} = (a^m)$ in a UFD. This means $\bar{B}_{-m} = (a^m) x^{-m} = B_{-m}$, and hence $\bar{B} = B$, i.e., $B$ is integrally closed.

Wait, but I need to double-check the step where I claimed $\alpha x^{-m} \in \bar{B}_{-m}$ iff $\alpha \in \overline{(a^m)}$. Let me re-examine.

$\alpha x^{-m}$ is integral over $B$ iff there exist $b_1, \ldots, b_N \in B$ such that $(\alpha x^{-m})^N + b_1 (\alpha x^{-m})^{N-1} + \cdots + b_N = 0$.

I claimed we can take $b_i$ to be homogeneous of degree $-im$. Is this justified?

The general theory of graded rings says: if $B$ is a $\mathbb{Z}$-graded ring and $f$ is a homogeneous element of degree $d$ in some graded extension, then $f$ is integral over $B$ iff $f$ satisfies a monic polynomial with homogeneous coefficients of appropriate degrees. But here, $\alpha x^{-m}$ is an element of $K(x)$, and we need to be careful about what "homogeneous" means.

Actually, $K(x)$ has a $\mathbb{Z}$-grading (as a $K$-vector space) where $x$ has degree 1. An element $\alpha x^{-m}$ with $\alpha \in K$ is homogeneous of degree $-m$. And $B$ is a graded subring. The integral closure of a graded domain in its fraction field is graded (this is a standard result, see e.g., Eisenbud or Bruns-Herzog).

But the fraction field of $B$ is $K(x)$, the field of rational functions, which is NOT graded (it's a field, so the only homogeneous elements are 0). The grading on $K[x, x^{-1}]$ extends to $K(x)$ in the sense that $K(x) = \bigcup_n K[x, x^{-1}] \cdot x^{-n}$... hmm, actually $K(x)$ doesn't have a $\mathbb{Z}$-grading in the usual sense.

Let me reconsider. The correct statement is: $B \subset K[x, x^{-1}] \subset K(x)$, and $K[x, x^{-1}]$ is $\mathbb{Z}$-graded. The integral closure of $B$ in $K(x)$ is contained in $K[x, x^{-1}]$ (since $K[x, x^{-1}]$ is integrally closed and contains $B$). And the integral closure of a $\mathbb{Z}$-graded ring $B$ in a $\mathbb{Z}$-graded over-ring (like $K[x, x^{-1}]$) is $\mathbb{Z}$-graded.

More precisely: $\bar{B} = \{f \in K[x, x^{-1}] : f \text{ integral over } B\}$, and if $f = \sum_k f_k x^k \in \bar{B}$ (with $f_k \in K$), then each $f_k x^k \in \bar{B}$.

This is because: if $f$ satisfies $f^N + b_1 f^{N-1} + \cdots + b_N = 0$ with $b_i \in B$, we can decompose by degree. Write $b_i = \sum_j b_{i,j}$ (degree decomposition). Then the degree-$d$ component of the equation gives a relation for the degree-$d$ component of $f^N + \cdots$. By a standard argument (using the "leading term" or induction on degree), each homogeneous component of $f$ is integral over $B$.

OK so I'll accept that $\bar{B}$ is graded and $\bar{B}_{-m} = \{\alpha \in K : \alpha x^{-m} \in \bar{B}\} \cdot x^{-m}$.

Now, $\alpha x^{-m} \in \bar{B}$ (with $\alpha \in K$) iff $\alpha x^{-m}$ is integral over $B$. Since $\alpha x^{-m}$ is homogeneous of degree $-m$, it satisfies a monic polynomial with homogeneous coefficients: $(\alpha x^{-m})^N + b_1 (\alpha x^{-m})^{N-1} + \cdots + b_N = 0$ where $b_i$ is homogeneous of degree $-im$ (so that each term has degree $-mN$).

$b_i \in B_{-im}$. For $i \geq 1$: $B_{-im} = a^{im} A x^{-im}$ (when $im > 0$, i.e., always since $m > 0$). So $b_i = a^{im} c_i x^{-im}$ for some $c_i \in A$.

The equation becomes: $\alpha^N x^{-mN} + a^m c_1 \alpha^{N-1} x^{-m(N-1)} + a^{2m} c_2 \alpha^{N-2} x^{-m(N-2)} + \cdots + a^{Nm} c_N = 0$.

All terms have degree $-mN$, so dividing by $x^{-mN}$: $\alpha^N + a^m c_1 \alpha^{N-1} + a^{2m} c_2 \alpha^{N-2} + \cdots + a^{Nm} c_N = 0$.

This is exactly the condition that $\alpha$ is integral over the ideal $(a^m)$ (in the sense of integral dependence on ideals): $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i \in (a^m)^i = (a^{mi})$.

BUT: integral dependence on an ideal is usually defined for $\alpha \in A$ (not $\alpha \in K$). The integral closure of an ideal $I$ in $A$ is $\bar{I} = \{\alpha \in A : \alpha \text{ integral over } I\}$. Here, $\alpha \in K$, not necessarily in $A$.

So the condition is: $\alpha \in K$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + \cdots + a^{Nm} c_N = 0$ with $c_i \in A$. This means $\alpha$ is integral over the subring $A[a^m] = A$ (since $a^m \in A$)... no, the coefficients are $a^{im} c_i \in (a^{mi}) \subset A$, not arbitrary elements of $A$.

Hmm, the condition is that $\alpha$ is integral over the "ideal" $(a^m)$ but with $\alpha \in K$ (not necessarily in $A$). Let me think about what this means.

If $\alpha \in K$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + \cdots + a^{Nm} c_N = 0$ with $c_i \in A$, then $\alpha$ is integral over $A$ (since all coefficients $a^{im} c_i \in A$). Since $A$ is integrally closed (UFD), $\alpha \in A$.

So $\alpha \in A$ and $\alpha$ is integral over the ideal $(a^m)$, meaning $\alpha \in \overline{(a^m)} = (a^m)$ (in a UFD).

Therefore $\bar{B}_{-m} = (a^m) x^{-m} = B_{-m}$, and $\bar{B} = B$.

So $B = A[x, ax^{-1}]$ IS integrally closed when $A$ is a UFD!

Wait, but let me also handle the case $a = 0$. If $a = 0$, then $B = A[x, 0 \cdot x^{-1}] = A[x]$. And $A[x]$ is a UFD if $A$ is a UFD (by Gauss's lemma), hence integrally closed. So $a = 0$ is fine too.

Hmm wait, $a/x$ when $a = 0$ is just $0$, so $A[x, a/x] = A[x, 0] = A[x]$. And $A[x]$ is a polynomial ring over a UFD, which is a UFD, hence integrally closed. ✓.

What about $a$ being a unit? If $a$ is a unit, $B = A[x, ax^{-1}] = A[x, x^{-1}]$ (since $x^{-1} = a^{-1} \cdot ax^{-1}$). This is a Laurent polynomial ring over $A$, which is integrally closed if $A$ is. ✓.

So it seems like $A[x, a/x]$ is always integrally closed when $A$ is a UFD, for any $a \in A$.

But wait, I should double-check my argument more carefully. The key step was: $\alpha \in K$ integral over $A$ (with the specific polynomial having coefficients in $(a^{mi})$) implies $\alpha \in A$ (since $A$ is integrally closed) and then $\alpha \in \overline{(a^m)} = (a^m)$.

The first part: $\alpha$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + \cdots + a^{Nm} c_N = 0$ with $c_i \in A$. The coefficients $a^{im} c_i$ are in $A$, so this is a monic polynomial with coefficients in $A$, hence $\alpha$ is integral over $A$, hence $\alpha \in A$ (since $A$ is integrally closed). ✓.

The second part: $\alpha \in A$ and $\alpha$ satisfies $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i \in (a^m)^i = (a^{mi})$. This means $\alpha$ is in the integral closure of the ideal $(a^m)$ in $A$. In a UFD, $\overline{(a^m)} = (a^m)$. ✓.

So the argument is complete. Let me also verify with a potential counterexample to make sure.

Take $A = k[s,t]$, $a = s^2 t$ (not square-free). Then $B = A[x, s^2 t / x] = k[s,t][x, s^2 t x^{-1}]$.

By my argument, $B$ should be integrally closed. Let me verify with Serre's criterion. $B \cong k[s,t,X,Y]/(XY - s^2 t)$. This is a 3-dimensional hypersurface. The singular locus is where $Y = X = s^2 t$'s partial derivatives vanish: $\partial/\partial X = Y$, $\partial/\partial Y = X$, $\partial/\partial s = 2st$, $\partial/\partial t = s^2$. Singular locus: $X = Y = 0$ and ($s = 0$ or $t = 0$) and $s^2 = 0$, so $s = 0$. So the singular locus is $X = Y = s = 0$, which is the $t$-axis, a 1-dimensional variety in a 3-dimensional variety, codimension 2. By Serre's criterion ($R_1$: regular in codim 1 ✓, $S_2$: hypersurface hence CM hence $S_2$ ✓), $B$ is integrally closed. ✓.

Another example: $A = k[s,t]$, $a = s^2$. $B = k[s,t,X,Y]/(XY - s^2)$. Singular locus: $X = Y = s = 0$, the $t$-axis, codimension 2 in the 3-dimensional variety. $R_1$ ✓, $S_2$ ✓. Integrally closed. ✓.

Hmm, but what if $A$ has dimension 1? Take $A = k[t]$, $a = t^2$. $B = k[t,X,Y]/(XY - t^2)$. This is 2-dimensional. Singular locus: $X = Y = t = 0$, the origin, codimension 2. $R_1$ ✓, $S_2$ ✓ (hypersurface). Integrally closed. ✓. (This is the $A_1$ surface singularity, which is indeed normal.)

What about $A = k[t]$, $a = t^3$? $B = k[t,X,Y]/(XY - t^3)$. Singular locus: $X = Y = t = 0$, origin, codim 2. $R_1$ ✓, $S_2$ ✓. Integrally closed. ✓. (This is the $A_2$ surface singularity, also normal.)

So it seems like the answer is YES, $A[x, a/x]$ is always integrally closed when $A$ is a UFD.

But wait, I want to make sure my argument about the graded integral closure is rigorous. Let me also consider whether there could be non-homogeneous elements in the integral closure that I'm missing.

The claim is: $\bar{B} = \bigoplus_{n \in \mathbb{Z}} \bar{B}_n$ (graded). This is a standard result. Let me cite it properly.

**Theorem** (see e.g., Bruns-Herzog, or Eisenbud): Let $R = \bigoplus_{n \geq 0} R_n$ be a graded ring (or $\mathbb{Z}$-graded), and let $\bar{R}$ be its integral closure in its total fraction ring. Then $\bar{R}$ is also graded (with the same grading group), and a homogeneous element $f$ of degree $d$ is in $\bar{R}$ iff $f$ is integral over $R$.

For a $\mathbb{Z}$-graded domain $B = \bigoplus_{n \in \mathbb{Z}} B_n$ with fraction field $L$, the integral closure $\bar{B}$ in $L$ is $\mathbb{Z}$-graded, and $\bar{B}_d = \{f \in L_d : f \text{ integral over } B\}$ where $L_d$ is the degree-$d$ part of the "graded fraction field."

But as I noted, the fraction field $K(x)$ doesn't have a natural $\mathbb{Z}$-grading. However, $K[x, x^{-1}]$ does, and $\bar{B} \subset K[x, x^{-1}]$ (since $K[x, x^{-1}]$ is integrally closed). The grading on $K[x, x^{-1}]$ restricts to a grading on $\bar{B}$.

The key fact is: if $f \in K[x, x^{-1}]$ is integral over $B$, then each homogeneous component of $f$ is integral over $B$. This follows from the "graded integral closure" theory.

Proof sketch: Write $f = \sum_{k=a}^{b} f_k x^k$ (finite sum). Suppose $f^N + c_1 f^{N-1} + \cdots + c_N = 0$ with $c_i \in B$. Look at the highest degree term. The degree-$bN$ component gives $f_b^N x^{bN} + (\text{terms from } c_i \text{ of appropriate degree}) = 0$. This gives a monic polynomial for $f_b x^b$ over $B$. Then subtract and proceed by induction.

More carefully: the degree $bN$ component of $f^N$ is $f_b^N x^{bN}$. The degree $bN$ component of $c_i f^{N-i}$ is (the degree $bN - (N-i)b = ib$... hmm, wait, $c_i$ can have various degrees. Let me think again.

Actually, the standard proof uses the following: consider the grading automorphism. For a $\mathbb{Z}$-graded ring, there are automorphisms $\phi_\lambda$ (for $\lambda$ in the base field, if it's a $k$-algebra) that scale the degree-$n$ part by $\lambda^n$. Applying $\phi_\lambda$ to the integral equation gives another integral equation for $\phi_\lambda(f) = \sum f_k \lambda^k x^k$. Since this holds for all $\lambda$, we can extract the homogeneous components.

But this requires $B$ to be a $k$-algebra with $k$ infinite. For general UFDs (not necessarily $k$-algebras), we need a different argument.

Actually, the general result doesn't require a base field. The integral closure of a $\mathbb{Z}$-graded domain in its fraction field is $\mathbb{Z}$-graded. This is proved in, e.g., Bourbaki or Gilmer's book on multiplicative ideal theory. The proof uses the fact that if $f$ is integral over $B$, and we write $f = f_a + f_{a+1} + \cdots + f_b$ (homogeneous decomposition), then $f_a$ (the lowest degree component) is integral over $B$ (by looking at the lowest degree term of the integral equation), and then $f - f_a$ is integral over $B$ (since $f_a \in \bar{B}$ and $f \in \bar{B}$, and $\bar{B}$ is a ring), and proceed by induction.

OK, I'm fairly convinced the argument is correct. Let me also think about whether there's a simpler proof.

**Simpler approach using Serre's criterion:**

$B = A[X,Y]/(XY - a) \cong A[x, ax^{-1}]$. We want to show $B$ is integrally closed (i.e., normal) when $A$ is a UFD.

By Serre's criterion, $B$ is normal iff $R_1$ (regular in codimension 1) and $S_2$.

$S_2$: $B = A[X,Y]/(XY-a)$ is a hypersurface (principal ideal in a polynomial ring), hence a complete intersection, hence Cohen-Macaulay (since $A[X,Y]$ is CM when $A$ is CM, and a quotient by a regular sequence preserves CM). A UFD is CM (it's a domain, and... actually, is a UFD always CM? A UFD is not necessarily CM in general. Hmm.)

Wait, actually, a UFD is not necessarily Cohen-Macaulay. There are UFDs that are not CM. So this approach might not work in full generality.

Hmm, but $S_2$ is weaker than CM. $S_2$ says: $\text{depth}(B_\mathfrak{p}) \geq \min(2, \text{ht}(\mathfrak{p}))$ for all primes $\mathfrak{p}$. 

Actually, let me think about whether $B = A[X,Y]/(XY-a)$ satisfies $S_2$ when $A$ is a UFD.

$B$ is a free $A$-module? No, $B$ is not free over $A$ in general. But $B$ is $A$-flat? $A[X,Y]$ is $A$-flat (free), and $B = A[X,Y]/(XY-a)$. The element $XY - a$ is a non-zero-divisor in $A[X,Y]$ (since $A[X,Y]$ is a domain and $XY - a \neq 0$). So $B$ is $A$-flat (quotient of a flat module by a non-zero-divisor... no, that's not right in general. $A[X,Y]$ is $A$-free, and $B = A[X,Y]/(XY-a)$. The sequence $0 \to A[X,Y] \xrightarrow{\cdot(XY-a)} A[X,Y] \to B \to 0$ is exact. Since $A[X,Y]$ is $A$-free, it's $A$-flat, and tensoring with any $A$-module $M$: $0 \to M[X,Y] \xrightarrow{\cdot(XY-a)} M[X,Y] \to B \otimes_A M \to 0$. This is exact iff $XY - a$ is a non-zero-divisor on $M[X,Y]$, which is true iff $a$ is a non-zero-divisor on $M$ (since $XY - a$ is monic in $X$... hmm, actually $XY - a$ is not monic in $X$ or $Y$).

Hmm, let me think differently. Is $XY - a$ a non-zero-divisor on $M[X,Y]$ for all $A$-modules $M$? If $a = 0$, then $XY - a = XY$, which is a zero-divisor on $M[X,Y]$ if $M \neq 0$ (since $X \cdot Y = XY$ and $X, Y$ are zero-divisors on $k[X,Y]/(XY)$... wait, I mean $XY$ is a zero-divisor in $M[X,Y]$ since $X \cdot (XY) = X^2 Y$ and $Y \cdot (XY) = XY^2$, but $XY$ itself: is $XY$ a zero-divisor? $X \cdot Y \cdot f = XYf$, and if $XYf = 0$ then $f = 0$ (since $M[X,Y]$ is a polynomial ring and $XY$ is not a zero-divisor in $(M[X,Y])$... actually $XY$ could be a zero-divisor if $M$ has torsion).

This is getting complicated. Let me just go with the graded ring argument, which I believe is correct.

Actually, let me also consider the case where $A$ is a UFD but not a $k$-algebra, e.g., $A = \mathbb{Z}$. Take $a = 4$. Then $B = \mathbb{Z}[x, 4/x] = \mathbb{Z}[X,Y]/(XY - 4)$. Is this integrally closed?

$B = \mathbb{Z}[X,Y]/(XY-4)$. Consider the element $2 \in B$. Is $2$ a non-zero-divisor? Yes (since $B$ is a domain). Consider $X/2$ in $\text{Frac}(B)$. $(X/2) \cdot Y = XY/2 = 4/2 = 2 \in B$. And $(X/2)^2 = X^2/4$. Is $X/2$ integral over $B$? $(X/2)^2 = X^2/4$. And $X^2 = X \cdot X$, $XY = 4$, so $X = 4/Y$, $X^2 = 16/Y^2$, $(X/2)^2 = 4/Y^2$. Hmm.

Is $X/2$ integral over $B$? We need a monic polynomial. $(X/2) \cdot Y = 2$, so $X/2 = 2/Y$. And $(2/Y) \cdot X = 2X/Y = 2 \cdot 4/Y^2 = 8/Y^2$... this is getting messy.

Let me use the grading. $B = \bigoplus_{n \geq 0} \mathbb{Z} x^n \oplus \bigoplus_{n > 0} 4^n \mathbb{Z} x^{-n}$. The element $X/2 = x/2$ has degree 1. For degree 1, $\bar{B}_1 = \bar{B} \cap K x$. An element $\alpha x \in \bar{B}_1$ iff $\alpha$ is integral over $A = \mathbb{Z}$ (from the $k \geq 0$ case), so $\alpha \in \mathbb{Z}$. Thus $\bar{B}_1 = \mathbb{Z} x = B_1$, and $x/2 \notin \bar{B}_1$ (since $1/2 \notin \mathbb{Z}$). So $x/2$ is NOT in the integral closure. Good.

What about degree $-1$? $\bar{B}_{-1} = \overline{(4)} \mathbb{Z} \cdot x^{-1}$. $\overline{(4)}$ in $\mathbb{Z}$: $\overline{(4)} = \{n \in \mathbb{Z} : v_2(n) \geq 2, v_p(n) \geq 0 \text{ for } p \neq 2\} = 4\mathbb{Z}$. So $\bar{B}_{-1} = 4\mathbb{Z} x^{-1} = B_{-1}$. ✓.

So $B = \mathbb{Z}[x, 4/x]$ is integrally closed. Makes sense.

Let me also try $A = \mathbb{Z}$, $a = 2$. $B = \mathbb{Z}[x, 2/x]$. $\bar{B}_{-1} = \overline{(2)} x^{-1} = 2\mathbb{Z} x^{-1} = B_{-1}$. ✓. Integrally closed.

OK, I'm now confident the answer is YES.

Let me also think about whether the UFD assumption is necessary, or if integrally closed suffices.

If $A$ is just integrally closed (not UFD), is $A[x, ax^{-1}]$ integrally closed? The argument used: (1) $A$ integrally closed → $\alpha \in A$, (2) $\overline{(a^m)} = (a^m)$ in a UFD. Step (2) uses UFD. In a general integrally closed domain, $\overline{(a^m)}$ might be larger than $(a^m)$.

For example, if $A$ is integrally closed but not a UFD, and $a$ is an element such that $(a^m)$ is not integrally closed as an ideal, then $B$ might not be integrally closed.

But the question only asks about UFDs, so this is fine.

Actually, wait. Let me reconsider step (2) more carefully. In a Krull domain (which includes UFDs), the integral closure of a principal ideal $(b)$ is $\bar{(b)} = \{x \in A : v(x) \geq v(b) \text{ for all essential valuations } v\}$. For a UFD, this equals $(b)$ since $v(x) \geq v(b)$ for all $v$ iff $b | x$ (in a UFD). For a general Krull domain, this might not equal $(b)$.

But actually, in any Krull domain, $\bar{(b)} = (b)$ for principal ideals? No, that's not true. In a Dedekind domain that's not a PID, a principal ideal $(b)$ might have $\bar{(b)} \neq (b)$... actually, in a Dedekind domain, every ideal is integrally closed (since Dedekind domains are Noetherian, integrally closed, and every nonzero ideal factors into primes, and the integral closure of a product of prime ideals is itself). Hmm, actually in a Dedekind domain, $\bar{I} = I$ for all ideals $I$? No, that's not right either.

OK, this is a tangent. The question is about UFDs, and in UFDs, principal ideals are integrally closed (as I showed). So the answer is YES.

Let me now also think about whether there's an issue with $a = 0$ or $a$ being a zero-divisor. In a UFD (which is a domain), $a = 0$ is the only zero-divisor. And $A[x, 0/x] = A[x, 0] = A[x]$, which is a UFD (polynomial ring over UFD is UFD), hence integrally closed. ✓.

So the answer is: **Yes, $A[x, a/x]$ is always integrally closed when $A$ is a UFD.**

Now let me write up a clean proof.

**Proof:**

Let $A$ be a UFD and $a \in A$. We want to show $B = A[x, a/x]$ is integrally closed.

First, note that $B \cong A[X,Y]/(XY - a)$ via $X \mapsto x$, $Y \mapsto a/x$. If $a = 0$, then $B = A[x]$, which is a UFD (polynomial ring over UFD), hence integrally closed. So assume $a \neq 0$.

Since $A$ is a UFD, it is an integrally closed domain. Let $K = \text{Frac}(A)$. Then $B = A[x, ax^{-1}] \subset K[x, x^{-1}]$ (the Laurent polynomial ring). Since $K[x, x^{-1}]$ is a UFD (hence integrally closed), the integral closure $\bar{B}$ of $B$ in $\text{Frac}(B) = K(x)$ satisfies $\bar{B} \subset K[x, x^{-1}]$.

The ring $B$ is $\mathbb{Z}$-graded: $B = \bigoplus_{n \in \mathbb{Z}} B_n$ where $B_n = A x^n$ for $n \geq 0$ and $B_n = a^{|n|} A x^n$ for $n < 0$. (This is because $B$ is generated by $A$ (degree 0), $x$ (degree 1), and $ax^{-1}$ (degree $-1$), and the relation $x \cdot (ax^{-1}) = a$ (degree 0) is consistent.)

Since $B$ is $\mathbb{Z}$-graded and $\bar{B} \subset K[x, x^{-1}]$ (which is also $\mathbb{Z}$-graded), the integral closure $\bar{B}$ is $\mathbb{Z}$-graded: $\bar{B} = \bigoplus_{n \in \mathbb{Z}} \bar{B}_n$ where $\bar{B}_n = \bar{B} \cap K x^n$. (This is a standard result: the integral closure of a graded domain in a graded over-ring is graded.)

We show $\bar{B}_n = B_n$ for all $n$.

**Case $n \geq 0$:** Let $\alpha x^n \in \bar{B}_n$ with $\alpha \in K$. Then $\alpha x^n$ is integral over $B$, so it satisfies a monic polynomial with homogeneous coefficients: $(\alpha x^n)^N + b_1 (\alpha x^n)^{N-1} + \cdots + b_N = 0$ where $b_i \in B_{in}$. For $n \geq 0$, $B_{in} = A x^{in}$, so $b_i = c_i x^{in}$ with $c_i \in A$. Dividing by $x^{nN}$: $\alpha^N + c_1 \alpha^{N-1} + \cdots + c_N = 0$ with $c_i \in A$. So $\alpha$ is integral over $A$. Since $A$ is integrally closed, $\alpha \in A$. Thus $\bar{B}_n = A x^n = B_n$.

**Case $n < 0$, say $n = -m$ with $m > 0$:** Let $\alpha x^{-m} \in \bar{B}_{-m}$ with $\alpha \in K$. Then $\alpha x^{-m}$ satisfies $(\alpha x^{-m})^N + b_1 (\alpha x^{-m})^{N-1} + \cdots + b_N = 0$ with $b_i \in B_{-im} = a^{im} A x^{-im}$. Write $b_i = a^{im} c_i x^{-im}$ with $c_i \in A$. Dividing by $x^{-mN}$: $\alpha^N + a^m c_1 \alpha^{N-1} + a^{2m} c_2 \alpha^{N-2} + \cdots + a^{Nm} c_N = 0$.

Since $a^{im} c_i \in A$ for all $i$, this is a monic polynomial with coefficients in $A$, so $\alpha$ is integral over $A$, hence $\alpha \in A$ (as $A$ is integrally closed).

Now, $\alpha \in A$ satisfies $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i = a^{im} c_i \in (a^m)^i$. This means $\alpha$ is in the integral closure of the ideal $(a^m)$ in $A$.

**Claim:** In a UFD, the integral closure of any principal ideal $(b)$ is $(b)$ itself.

*Proof of claim:* In a Krull domain (hence in a UFD), the integral closure of an ideal $I$ is $\bar{I} = \{x \in A : v(x) \geq v(I) \text{ for all essential valuations } v\}$, where $v(I) = \min_{y \in I} v(y)$. For $I = (b)$, $v((b)) = v(b)$ for each valuation $v$. In a UFD, the essential valuations are the $p$-adic valuations $v_p$ for irreducible elements $p$. Writing $b = u \prod p_i^{e_i}$ (unique factorization), $v_{p_i}(b) = e_i$ and $v_q(b) = 0$ for $q \neq p_i$. So $\overline{(b)} = \{x \in A : v_{p_i}(x) \geq e_i \text{ for all } i\} = (b)$. (The last equality uses that in a UFD, $v_p(x) \geq e$ for all $p$ iff $x \in (b)$.)

Applying the claim with $b = a^m$: $\overline{(a^m)} = (a^m)$, so $\alpha \in (a^m) = a^m A$. Thus $\bar{B}_{-m} = a^m A x^{-m} = B_{-m}$.

**Conclusion:** $\bar{B}_n = B_n$ for all $n \in \mathbb{Z}$, so $\bar{B} = B$. Therefore $B = A[x, a/x]$ is integrally closed. $\blacksquare$

Wait, I should also justify the "standard result" that the integral closure of a graded domain is graded. Let me include a brief justification.

Actually, let me also double-check: is the integral closure of an ideal in a Krull domain really given by that valuation formula? Yes, this is a well-known result. In a Krull domain $A$ with essential valuations $\{v_\mathfrak{p}\}_{\mathfrak{p} \in X^{(1)}(A)}$ (valuations associated to height-1 primes), the integral closure of an ideal $I$ is $\bar{I} = \{x \in A : v_\mathfrak{p}(x) \geq v_\mathfrak{p}(I) \text{ for all } \mathfrak{p} \in X^{(1)}(A)\}$ where $v_\mathfrak{p}(I) = \min\{v_\mathfrak{p}(y) : y \in I\}$. This is proved in, e.g., Bourbaki's Commutative Algebra or Swanson-Huneke's "Integral Closure of Ideals, Rings, and Modules."

For a UFD, the height-1 primes are principal ideals $(p)$ for irreducible $p$, and $v_{(p)}$ is the $p$-adic valuation.

I think the proof is complete. Let me also mention that the key ingredients are:
1. $A$ integrally closed (to get $\alpha \in A$ from integrality over $A$).
2. Principal ideals in UFD are integrally closed (to get $\alpha \in (a^m)$ from integrality over $(a^m)$).
3. The graded structure of $B$ and the fact that integral closure preserves grading.

The answer is **Yes**.

Let me write the final clean version.

Actually, one more thing: I should verify that $B$ is indeed a domain (so that "integrally closed" makes sense). $B = A[X,Y]/(XY - a)$. If $a \neq 0$, is $XY - a$ irreducible (hence prime, since $A[X,Y]$ is a UFD)? $XY - a$ is linear in $X$ (and in $Y$), so it's irreducible in $A[X,Y]$ (as a polynomial of degree 1 in $X$ over $A[Y]$, it's irreducible iff it has no root in $\text{Frac}(A[Y])$, i.e., $a/Y \notin A[Y]$... actually, a degree-1 polynomial is always irreducible). More precisely, $XY - a$ is degree 1 in $X$ over $A[Y]$, and a degree-1 polynomial over any domain is irreducible. So $XY - a$ is irreducible in $A[Y][X] = A[X,Y]$, hence prime (since $A[X,Y]$ is a UFD), so $B$ is a domain. ✓.

(If $a = 0$, $B = A[X,Y]/(XY) = A[x]$, which is a domain since $A$ is. Wait, $A[X,Y]/(XY) \neq A[x]$. $A[X,Y]/(XY)$ is not a domain! But $A[x, 0/x] = A[x, 0] = A[x]$, which is a domain. The issue is that $A[X,Y]/(XY - 0) = A[X,Y]/(XY)$ is NOT isomorphic to $A[x]$ when $a = 0$.

Hmm, let me reconsider. $A[x, a/x]$ with $a = 0$: this is $A[x, 0 \cdot x^{-1}] = A[x, 0] = A[x]$. But $A[X,Y]/(XY - 0) = A[X,Y]/(XY) \        — AI历史解题过程（thinking）
#   deepmath_103k_00000528         — 题目ID

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
  <problem_id>deepmath_103k_00000528</problem_id>
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

Use Cauchy's integral formula to compute the contour integral \( \int \limits_{\Gamma} \frac{e^{-z}}{z-1}dz \), where \( \Gamma \) is the square with sides parallel to the axes, centered at \( i \), and with side length 5, traversed in the anticlockwise direction.

## Standard Solution

Okay, so I need to compute the contour integral of e^(-z)/(z - 1) around this square Γ. The square is centered at i, has sides parallel to the axes, and has a side length of 5. It's traversed anticlockwise. Alright, let me recall Cauchy's integral formula. 

Cauchy's integral formula states that if f(z) is analytic inside and on some simple closed contour Γ, and if a is a point inside Γ, then the integral around Γ of f(z)/(z - a) dz is 2πi times f(a). So in symbols: ∫_Γ [f(z)/(z - a)] dz = 2πi f(a). 

In this problem, the integrand is e^(-z)/(z - 1). Comparing this to the Cauchy formula, it seems like f(z) would be e^(-z), and a would be 1. So then, according to the formula, if 1 is inside the contour Γ, the integral would be 2πi times f(1) = 2πi e^{-1}. But if 1 is not inside Γ, then the integral would be zero because the integrand would be analytic inside and on Γ. 

Therefore, the key question here is: Is the point z = 1 inside the square Γ? The square is centered at i, which is (0, 1) in the complex plane, right? And the side length is 5, so each side is 5 units long. Since the sides are parallel to the axes, the square extends 2.5 units to the left, right, top, and bottom from its center. 

Let me visualize the complex plane. The center is at i, so the square is centered at (0, 1). The side length is 5, so each half-side is 2.5. Therefore, the square spans from -2.5 to +2.5 in the real (x-axis) direction and from 1 - 2.5 to 1 + 2.5 in the imaginary (y-axis) direction. Wait, but actually, the square is in the complex plane, so the x-axis is real, y-axis is imaginary. So the center is at (0, 1). The square has sides of length 5, so each side from the center extends 2.5 units. Therefore, horizontally (real direction), the square goes from 0 - 2.5 to 0 + 2.5, i.e., from -2.5 to +2.5 on the real axis. Vertically (imaginary direction), it goes from 1 - 2.5 to 1 + 2.5, which is from -1.5 to 3.5 on the imaginary axis. 

So the square spans from -2.5 to +2.5 in real and from -1.5i to 3.5i in imaginary. Now, the point z = 1 is at (1, 0) in the complex plane. So we need to check if (1, 0) is inside this square. 

Since the real part of z = 1 is 1, which is between -2.5 and +2.5. The imaginary part is 0, which is between -1.5 and +3.5. Therefore, the point z = 1 is indeed inside the square Γ. Wait, hold on. The center is at (0,1), which is 0 in real and 1 in imaginary. The square's vertical range is from 1 - 2.5 to 1 + 2.5. Wait, 1 - 2.5 is -1.5, and 1 + 2.5 is 3.5. So vertically, it goes from -1.5i to 3.5i. But the imaginary part of z = 1 is 0, which is within -1.5 to 3.5. The real part of z = 1 is 1, which is within -2.5 to 2.5. So yes, z = 1 is inside the square. 

Therefore, by Cauchy's integral formula, the integral should be 2πi times e^{-1}, which is 2πi / e. 

Wait, but let me double-check. Is there any reason the formula wouldn't apply here? The function f(z) = e^{-z} is entire, right? It's analytic everywhere in the complex plane, so there are no issues with it being analytic inside and on Γ. The denominator is z - 1, and since z = 1 is inside Γ, the integrand has a singularity at z = 1. However, because f(z) is analytic everywhere, Cauchy's integral formula applies. 

Therefore, unless there's something tricky here, the integral should just be 2πi e^{-1}. But maybe I should check the orientation. The problem states that the contour is traversed anticlockwise, which is the standard direction for Cauchy's formula. So that's good. 

Alternatively, if I were to parametrize the square and compute the integral directly, that would be very complicated. But since Cauchy's formula applies here, there's no need. 

But just to be thorough, let me confirm the dimensions again. The square is centered at i (0,1) with side length 5, so each side is 5 units. Therefore, each half-side is 2.5 units. So along the real axis (horizontal direction), the square extends from -2.5 to +2.5. Along the imaginary axis (vertical direction), from 1 - 2.5 to 1 + 2.5, which is -1.5 to 3.5. 

Therefore, the square's corners would be at ( -2.5, -1.5 ), ( +2.5, -1.5 ), ( +2.5, 3.5 ), ( -2.5, 3.5 ). Wait, no, actually, in complex terms, the corners would be:

- Real part from -2.5 to +2.5, and imaginary part from -1.5 to +3.5. Wait, actually, no. Wait, the center is at (0,1). So to get the corners, if it's a square with sides parallel to the axes, centered at (0,1), with side length 5, then each half-side is 2.5. Therefore, the real part (x-coordinate) ranges from 0 - 2.5 to 0 + 2.5, which is -2.5 to +2.5. The imaginary part (y-coordinate) ranges from 1 - 2.5 to 1 + 2.5, which is -1.5 to +3.5. So the square in the complex plane is the region:

-2.5 ≤ Re(z) ≤ 2.5

-1.5 ≤ Im(z) ≤ 3.5

So the point z = 1 has Re(z) = 1 (which is within -2.5 to 2.5) and Im(z) = 0 (which is within -1.5 to 3.5). So yes, definitely inside the square.

Therefore, applying Cauchy's integral formula, the integral is 2πi * e^{-1}, so 2πi / e. Therefore, the answer should be 2πi/e. 

But just to check, maybe I made a mistake in the sign? Let me recall: Cauchy's formula says ∫_Γ [f(z)/(z - a)] dz = 2πi f(a). Here, f(z) is e^{-z}, a is 1. So indeed, the integral is 2πi e^{-1}. There's no negative sign or anything. The function e^{-z} is just the function evaluated at a = 1. So e^{-1} is correct. 

Alternatively, if the integrand were e^{-z}/(z - a), then the formula applies with f(z) = e^{-z}, so f(a) = e^{-a}. Here, a is 1, so f(a) = e^{-1}. So yes, that's correct. 

Therefore, I think the answer is 2πi e^{-1}, or 2πi / e. 

Wait, let me make sure that the integrand is in the correct form. Cauchy's formula is for f(z)/(z - a). In our case, the integrand is e^{-z}/(z - 1). So f(z) = e^{-z}, a = 1, so indeed, the integral is 2πi f(1) = 2πi e^{-1}. That seems correct. 

Is there any other reason this might not apply? For example, if the contour was not simply connected, but since it's a square, it's a simple closed contour. The function e^{-z} is entire, so analytic everywhere. The point a = 1 is inside the contour, so all conditions are met. 

Therefore, the integral is 2πi times e^{-1}.

I think that's solid. Maybe just to check the side length again. The square has side length 5, so each half-side is 2.5. So from center at (0,1), moving left 2.5 in real direction gets to -2.5, right to +2.5. Up 2.5 in imaginary direction from center (1) gets to 3.5, down to -1.5. So yes, as before.

Therefore, the integral is 2πi/e. So \boxed{\dfrac{2\pi i}{e}}.

**Final Answer**
\boxed{\dfrac{2\pi i}{e}}
</think>

To compute the contour integral \( \int_{\Gamma} \frac{e^{-z}}{z-1} \, dz \) using Cauchy's integral formula, we first identify the function and the point of singularity. The integrand is \( \frac{e^{-z}}{z-1} \), which fits the form \( \frac{f(z)}{z-a} \) with \( f(z) = e^{-z} \) and \( a = 1 \).

Cauchy's integral formula states that if \( f(z) \) is analytic inside and on a simple closed contour \( \Gamma \) and \( a \) is inside \( \Gamma \), then the integral is \( 2\pi i f(a) \).

Next, we check if the point \( z = 1 \) lies inside the square \( \Gamma \). The square is centered at \( i \) (which is \( (0, 1) \) in the complex plane) with a side length of 5. The square extends 2.5 units in each direction from the center. Therefore, the real part ranges from \( -2.5 \) to \( 2.5 \) and the imaginary part ranges from \( -1.5 \) to \( 3.5 \).

The point \( z = 1 \) has a real part of 1 (within \( -2.5 \) to \( 2.5 \)) and an imaginary part of 0 (within \( -1.5 \) to \( 3.5 \)), confirming that \( z = 1 \) is inside the contour.

Since \( f(z) = e^{-z} \) is entire (analytic everywhere), we apply Cauchy's integral formula:
\[
\int_{\Gamma} \frac{e^{-z}}{z-1} \, dz = 2\pi i \cdot f(1) = 2\pi i \cdot e^{-1}
\]

Thus, the final answer is:
\[
\boxed{\dfrac{2\pi i}{e}}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks: Is the ring $A[x, a/x]$ always integrally closed if $A$ is a UFD and $a \in A$?

Let me think about this carefully.

$A[x, a/x]$ is the subring of $A[x, x^{-1}]$ (or rather of $\text{Frac}(A)[x, x^{-1}]$) generated by $x$ and $a/x$ over $A$. Actually, more precisely, $A[x, a/x]$ is the $A$-subalgebra of $K[x, x^{-1}]$ (where $K = \text{Frac}(A)$) generated by $x$ and $a/x$.

Note that $A[x, a/x] \cong A[X, Y] / (XY - a)$ where $X \mapsto x$, $Y \mapsto a/x$. This is because the relation $x \cdot (a/x) = a$ holds, and this is the only relation.

So the question becomes: is $A[X,Y]/(XY - a)$ integrally closed when $A$ is a UFD?

This is the coordinate ring of a "toric-like" variety. Actually $A[X,Y]/(XY-a)$ is the ring of the affine variety $XY = a$.

When is $A[X,Y]/(XY-a)$ integrally closed (or normal)?

A classical result: $A[X,Y]/(XY-a)$ is normal if and only if $a$ is square-free in $A$ (when $A$ is a UFD, or more generally when $a$ is "square-free" in an appropriate sense).

Wait, let me think more carefully. Actually, let me reconsider.

If $a$ is a unit, then $XY - a$ is... well $A[X,Y]/(XY-a)$ with $a$ a unit. Then $X$ is a unit (since $X \cdot Y = a$ and $a$ is a unit, so $X \cdot (a^{-1}Y) = 1$). So $A[X,Y]/(XY-a) \cong A[X, X^{-1}]$ which is a Laurent polynomial ring, and this is integrally closed if $A$ is integrally closed (UFD implies integrally closed). Good.

If $a = 0$, then $A[X,Y]/(XY) = A[X,Y]/(XY)$. Is this integrally closed? $XY = 0$ is the union of two axes. The ring $A[X,Y]/(XY)$ has zero divisors. Is it integrally closed? Consider $A = k$ a field. $k[X,Y]/(XY)$. The normalization of $k[X,Y]/(XY)$ is $k[X] \times k[Y]$ (the product of the normalizations of the two components). So $k[X,Y]/(XY)$ is NOT integrally closed. So for $a = 0$, it's not integrally closed.

But wait, maybe the question assumes $a \neq 0$? Let me consider the general case.

Actually, let me think about when $A[X,Y]/(XY - a)$ is normal for $A$ a UFD and $a \neq 0$.

Claim: $A[X,Y]/(XY - a)$ is integrally closed if and only if $a$ is square-free in $A$ (i.e., $a$ is not divisible by the square of any irreducible element, up to units).

Let me verify this. Suppose $a = p^2 \cdot b$ for some irreducible $p$ and $b \in A$. Then in $B = A[X,Y]/(XY - a)$, we have $XY = p^2 b$.

Consider the element $t = X/p$ in the fraction field of $B$. We have $t \cdot Y = XY/p = p^2 b / p = pb$. Hmm, let me think about whether $t$ is integral over $B$.

Actually, $t = X/p$. Then $t^2 = X^2/p^2$. And $t \cdot (Y/p) = XY/p^2 = b$. Hmm, let me think differently.

Let me consider the element $u = X/p$ in $\text{Frac}(B)$. Is $u$ integral over $B$?

$u$ satisfies: $u \cdot Y = (X/p) \cdot Y = XY/p = a/p = pb$. So $uY = pb \in B$ (since $p, b \in A \subset B$). But that doesn't directly give integrality.

Let me think about it differently. Consider $u = X/p$. Then $u^2 = X^2/p^2$. We have $X \cdot Y = p^2 b$, so $X^2 Y^2 = p^4 b^2$, thus $(X^2/p^2)(Y^2) = p^2 b^2 \cdot ... $ hmm this is getting complicated.

Let me try a specific example. Take $A = k[t]$ (a PID, hence UFD), $a = t^2$. Then $B = k[t][X,Y]/(XY - t^2)$.

Is $B$ integrally closed? Consider $s = X/t$ in $\text{Frac}(B)$. Then $s \cdot Y = XY/t = t^2/t = t \in B$. Also $s \cdot t = X \in B$. So $s$ maps things to $B$... but is $s$ itself in $B$?

$s = X/t$. Is $s$ integral over $B$? We have $s^2 = X^2/t^2$. And $X^2 = X \cdot X$. We know $XY = t^2$, so $X = t^2/Y$ (in the fraction field). Then $s = X/t = t/Y$. So $s = t/Y$, and $sY = t \in B$.

Is $s$ integral over $B$? Consider $s \cdot Y = t$, so $s = t/Y$. Also $s^2 = t^2/Y^2 = X/Y$ (since $t^2 = XY$). Hmm.

Let me check: is $s$ a root of a monic polynomial over $B$?

$s = X/t = t/Y$. We have $sY = t$ and $sX = X^2/t = X \cdot (X/t) = Xs$... that's circular.

Let me try: $s^2 Y = s \cdot (sY) = s \cdot t = st = (X/t) \cdot t = X \in B$. So $s^2 Y = X$.

Also $s^2 Y^2 = (sY)^2 = t^2 = XY$, so $s^2 Y^2 = XY$, giving $s^2 Y = X$ (dividing by $Y$ in the fraction field), consistent.

Now, is $s$ integral over $B$? Let's see if $s$ satisfies a monic polynomial. We have $sY = t$ and $sX = X^2/t$. Hmm, $sX = X \cdot s = X \cdot (X/t) = X^2/t$. And $X^2/t = X \cdot (X/t)$. Also $X^2 = X \cdot X$ and $t^2 = XY$ so $X/t = t/Y$ (already noted).

Consider the polynomial $Z^2 - sZ \cdot ...$. This is hard. Let me try a more direct approach.

Actually, I recall that for $A[X,Y]/(XY - a)$ with $A$ integrally closed, the ring is integrally closed iff $a$ is square-free (or $a$ is a unit, or more precisely, $a$ is "radical" in the sense that the ideal $(a)$ is radical... no, square-free).

Let me verify with the example $A = k[t]$, $a = t^2$.

$B = k[t, X, Y]/(XY - t^2)$. This is the coordinate ring of the surface singularity $XY = t^2$ in $\mathbb{A}^3$, which is an $A_1$ surface singularity (rational double point of type $A_1$). This is well-known to NOT be integrally closed (it's a singular point, and the normalization is $k[t, X, Y]/(XY - t^2) \to k[u, v]/(uv - ... )$... actually let me think).

The normalization of $k[t,X,Y]/(XY-t^2)$: Set $s = X/t = t/Y$. Then $X = st$, $Y = t/s$ (in the fraction field). The normalization should be $k[s, t]$ (or something like that). Indeed, $X = st$, $Y = t/s$... wait, $Y = t^2/X = t^2/(st) = t/s$. So in the fraction field, $X = st$ and $Y = t/s$. But $t/s$ is not a polynomial. Hmm.

Actually, let me reconsider. The map $k[t, X, Y]/(XY - t^2) \to k[u, v]$ given by $t \mapsto uv$, $X \mapsto u^2$, $Y \mapsto v^2$. Check: $XY = u^2 v^2 = (uv)^2 = t^2$. ✓. And $k[u,v]$ is integrally closed (it's a UFD). The image is $k[u^2, v^2, uv]$, which is the subring of $k[u,v]$ generated by $u^2, v^2, uv$. This is exactly the second Veronese subring, which is the coordinate ring of the $A_1$ singularity. The element $u$ (or $v$) is in the fraction field of $k[u^2, v^2, uv]$ (since $u = u^2 \cdot v / (uv) = u \cdot v / v$... hmm, $u = (u^2 v)/(uv)$... wait $u^2 v / (uv) = u$, yes). And $u$ is integral over $k[u^2, v^2, uv]$ since $u^2 \in k[u^2, v^2, uv]$. But $u \notin k[u^2, v^2, uv]$ (the Veronese subring consists of elements of even degree). So $k[u^2, v^2, uv]$ is not integrally closed, and its normalization is $k[u,v]$.

Great, so this confirms: for $a = t^2$ (not square-free), $A[x, a/x]$ is NOT integrally closed.

Now let me also verify the positive direction: if $a$ is square-free, is $A[X,Y]/(XY-a)$ integrally closed?

Take $A = k[t]$, $a = t$ (square-free, since $t$ is irreducible). Then $B = k[t, X, Y]/(XY - t)$. This is $k[X, Y]$ (since $t = XY$). Indeed, $B \cong k[X, Y]$ via $t \mapsto XY$. And $k[X,Y]$ is a UFD, hence integrally closed. ✓.

More generally, if $a$ is square-free in a UFD $A$, write $a = p_1 p_2 \cdots p_r$ (product of distinct irreducibles, up to units). Then $A[X,Y]/(XY - a)$.

Hmm, is this always integrally closed? Let me think about $A = k[s, t]$, $a = st$ (square-free since $s$ and $t$ are distinct irreducibles). Then $B = k[s, t, X, Y]/(XY - st)$.

Is this integrally closed? This is the coordinate ring of $XY = st$ in $\mathbb{A}^4$. This is a 3-dimensional variety. Is it normal?

Actually, $XY - st$ is a determinantal variety (it's the condition that the $2\times 2$ matrix $\begin{pmatrix} X & s \\ t & Y \end{pmatrix}$... no, $XY - st = 0$ is the determinant of $\begin{pmatrix} X & s \\ t & Y \end{pmatrix}$). Determinantal varieties defined by minors of generic matrices are known to be normal (or at least the ideal of maximal minors of a generic matrix is prime and the variety is normal). Actually, the variety cut out by a single $2\times 2$ minor of a $2\times 2$ matrix of indeterminates is a quadric cone, which is normal in dimension $\geq 2$... hmm, but it has an isolated singularity at the origin.

Wait, actually the quadric cone $XY - ZW = 0$ in $\mathbb{A}^4$ is known to be normal. It's a 3-dimensional variety with an isolated singularity at the origin, and it's normal (in fact, it has rational singularities). So $k[X,Y,s,t]/(XY-st)$ is integrally closed. ✓.

So the pattern seems to be: $A[X,Y]/(XY - a)$ is integrally closed iff $a$ is square-free (in a UFD).

Hmm wait, but I should be more careful. Let me think about whether square-free is sufficient in general.

Actually, I think the correct statement is: $A[X,Y]/(XY - a)$ is integrally closed if and only if $a$ is square-free in $A$ (assuming $A$ is integrally closed, or at least a UFD).

Let me think about why square-free is sufficient. Suppose $A$ is a UFD and $a$ is square-free. Write $a = u \cdot p_1 \cdots p_r$ where $u$ is a unit and $p_i$ are distinct irreducibles.

We can factor the construction. Note that $A[X,Y]/(XY - a)$ can be built up as follows. If $a = bc$ with $\gcd(b,c) = 1$ (in a UFD), then... hmm, actually there's a nice way to see this.

Consider $A = \bigcap A_{(p_i)}$ (intersection of localizations at height-1 primes, since $A$ is a UFD and thus Krull, it's the intersection of its DVR localizations at height-1 primes). 

Actually, let me think about it more algebraically. The key fact is:

**Lemma**: If $A$ is an integrally closed domain and $a \in A$ is square-free (i.e., $v(a) \leq 1$ for every DVR valuation $v$ of $K = \text{Frac}(A)$), then $A[X,Y]/(XY - a)$ is integrally closed.

Proof sketch: $B = A[X,Y]/(XY-a)$. The fraction field of $B$ is $K(X)$ where $Y = a/X$. An element of $K(X)$ integral over $B$ must be integral over $B_\mathfrak{p}$ for every prime $\mathfrak{p}$ of $B$, and $B$ is integrally closed iff $B_\mathfrak{p}$ is integrally closed for every prime $\mathfrak{p}$ (actually, $B$ is integrally closed iff $B_\mathfrak{p}$ is a DVR or field for every height-1 prime $\mathfrak{p}$, i.e., $B$ is normal iff it's regular in codimension 1, by Serre's criterion $R_1 + S_2$).

Hmm, this is getting complicated. Let me use a different approach.

Actually, I think the cleanest approach is:

$B = A[X,Y]/(XY - a)$. Note that $B \cong A[X, a/X] \subset K[X, X^{-1}]$ (or $K[X]$ if we think of $a/X$ as $a \cdot X^{-1}$, but $X^{-1}$ might not be in $K[X]$... actually $a/X = a \cdot X^{-1}$ and this is in $K[X, X^{-1}]$).

Wait, more precisely: $A[x, a/x]$ is the subring of $K[x, x^{-1}]$ (Laurent polynomial ring) generated by $A$, $x$, and $a/x = a \cdot x^{-1}$. So $A[x, a/x] = A[x, ax^{-1}] \subset K[x, x^{-1}]$.

Now, $K[x, x^{-1}]$ is integrally closed (it's a Laurent polynomial ring over a field, hence a UFD). So $A[x, a/x]$ is a subring of an integrally closed ring. The question is whether $A[x, a/x]$ itself is integrally closed.

$A[x, ax^{-1}]$ consists of all finite sums $\sum_{i} c_i x^i + \sum_j d_j a^j x^{-j}$ where... actually, let me think about what elements look like.

An element of $A[x, ax^{-1}]$ is a polynomial in $x$ and $ax^{-1}$ with coefficients in $A$. So it's of the form $\sum_{i \geq 0} \sum_{j \geq 0} c_{ij} x^i (ax^{-1})^j = \sum_{i,j \geq 0} c_{ij} a^j x^{i-j}$.

So elements are $\sum_k f_k x^k$ where $f_k \in A$ for $k \geq 0$ and $f_k \in a^{-k} A$ for $k < 0$ (i.e., $f_{-j} \in a^j A$ for $j > 0$, meaning $f_{-j} = a^j \cdot g_{-j}$ for some $g_{-j} \in A$).

Wait, let me redo this. For $k = i - j$ where $i, j \geq 0$:
- If $k \geq 0$: $i = k, j = 0$ gives $c_{k,0} x^k$, and also $i = k+1, j = 1$ gives $c_{k+1,1} a x^k$, etc. So the coefficient of $x^k$ (for $k \geq 0$) is $\sum_{j \geq 0} c_{k+j, j} a^j \in A$.
- If $k < 0$, say $k = -m$ with $m > 0$: $i = 0, j = m$ gives $c_{0,m} a^m x^{-m}$, $i=1, j=m+1$ gives $c_{1,m+1} a^{m+1} x^{-m}$, etc. So the coefficient of $x^{-m}$ is $\sum_{i \geq 0} c_{i, m+i} a^{m+i} = a^m \sum_{i \geq 0} c_{i,m+i} a^i \in a^m A$.

So $A[x, ax^{-1}] = \bigoplus_{k \in \mathbb{Z}} I_k x^k$ where $I_k = A$ for $k \geq 0$ and $I_k = a^{-k} A = a^{|k|} A$ for $k < 0$.

This is a "Z-graded" ring with $I_k = A$ for $k \geq 0$ and $I_{-m} = a^m A$ for $m > 0$.

For this to be a ring, we need $I_k \cdot I_l \subset I_{k+l}$. Check: for $k, l \geq 0$: $A \cdot A = A \subset A = I_{k+l}$. ✓. For $k \geq 0, l = -m < 0$: $A \cdot a^m A = a^m A = I_{k-m}$. If $k \geq m$, $I_{k-m} = A \supset a^m A$. ✓. If $k < m$, $I_{k-m} = I_{-(m-k)} = a^{m-k} A \supset a^m A$. ✓ (since $a^m A \subset a^{m-k} A$). For $k = -m, l = -n$ both negative: $a^m A \cdot a^n A = a^{m+n} A = I_{-(m+n)}$. ✓.

Good. So $B = A[x, ax^{-1}] = \bigoplus_{k \geq 0} A x^k \oplus \bigoplus_{m > 0} a^m A x^{-m}$.

Now, the integral closure of $B$ in $K(x) = \text{Frac}(B)$: An element $f \in K(x)$ integral over $B$ must be integral over $B_\mathfrak{p}$ for every prime ideal $\mathfrak{p}$ of $B$. By Serre's criterion, $B$ is integrally closed iff $B$ satisfies $R_1$ (regular in codimension 1) and $S_2$ (Serre's condition).

Actually, let me think about this differently. The ring $B = A[x, ax^{-1}]$ is $\mathbb{Z}$-graded. The integral closure of a graded ring in its fraction field is also graded (with the same grading group). So the integral closure $\bar{B}$ is $\bigoplus_{k \in \mathbb{Z}} J_k x^k$ for some $A$-submodules $J_k$ of $K$ with $J_k \supset I_k$.

An element $\alpha x^k \in K \cdot x^k$ (with $\alpha \in K$) is in $\bar{B}$ iff it's integral over $B$. Since $B$ is graded, $\alpha x^k$ is integral over $B$ iff $\alpha x^k$ satisfies a homogeneous monic polynomial... actually, integrality in graded rings: $\alpha x^k$ is integral over $B$ iff there exist $b_1, \ldots, b_n \in B$ such that $(\alpha x^k)^n + b_1 (\alpha x^k)^{n-1} + \cdots + b_n = 0$.

Hmm, this is getting complicated. Let me use a more concrete approach.

Let me use the characterization: $B$ is integrally closed iff $B = \bigcap_{\text{ht}(\mathfrak{p})=1} B_\mathfrak{p}$ (intersection over height-1 primes, in the fraction field).

The height-1 primes of $B = A[x, ax^{-1}]$: These come from height-1 primes of $A$ (extended) and possibly the "boundary" primes related to $x = 0$ or $ax^{-1} = 0$ (i.e., $a = 0$).

Actually, let me think about it via the covering $K[x, x^{-1}] \supset B$. The ring $K[x, x^{-1}]$ is a PID (Laurent polynomial ring over a field), so it's integrally closed. The relationship between $B$ and $K[x, x^{-1}]$ is:

$B = A[x, ax^{-1}]$ and $K[x, x^{-1}]$ is the localization of $B$ at $S = A \setminus \{0\}$ (roughly). Actually, $S^{-1} B = K[x, ax^{-1}]$. And $K[x, ax^{-1}] = K[x, x^{-1}]$ since $a/x = a \cdot x^{-1}$ and $a \in K^*$, so $x^{-1} = a^{-1} \cdot (a/x) \in K[x, ax^{-1}]$. So $S^{-1}B = K[x, x^{-1}]$.

Now, $B$ is integrally closed iff $B = \bar{B}$ where $\bar{B}$ is the integral closure in $K(x)$. Since $K[x, x^{-1}]$ is integrally closed and contains $B$, $\bar{B} \subset K[x, x^{-1}]$.

So $\bar{B} \subset K[x, x^{-1}] = \bigoplus_{k \in \mathbb{Z}} K x^k$.

An element $f = \sum_k c_k x^k \in K[x, x^{-1}]$ is in $\bar{B}$ iff $f$ is integral over $B$.

Since $B$ is $\mathbb{Z}$-graded and the grading is compatible, $f$ is integral over $B$ iff each homogeneous component $c_k x^k$ is integral over $B$ (this is a standard fact for graded rings: the integral closure of a $\mathbb{Z}$-graded domain in its fraction field is $\mathbb{Z}$-graded, and a homogeneous element $\alpha x^k$ is integral iff $\alpha$ is integral over a certain ring).

Actually, let me be more precise. For a $\mathbb{Z}$-graded domain $B = \bigoplus B_k$ with fraction field $L$, the integral closure $\bar{B}$ is also $\mathbb{Z}$-graded: $\bar{B} = \bigoplus \bar{B}_k$ where $\bar{B}_k = \bar{B} \cap L \cdot e^k$ (where $e$ is a homogeneous element of degree 1, here $x$). And $\alpha x^k \in \bar{B}_k$ iff $\alpha x^k$ is integral over $B$.

Now, $\alpha x^k$ is integral over $B$ iff $\alpha x^k$ satisfies a monic polynomial with coefficients in $B$. By the grading, we can assume the polynomial is "weighted homogeneous" in some sense. Specifically, $\alpha x^k$ is integral over $B$ iff there exist $n$ and $b_i \in B_{ki}$ (the degree $ki$ part of $B$) such that $(\alpha x^k)^n + b_1 (\alpha x^k)^{n-1} + \cdots + b_n = 0$, i.e., $\alpha^n x^{kn} + b_1 \alpha^{n-1} x^{k(n-1)} + \cdots + b_n = 0$ with $b_i \in B_{ki}$.

This means $\alpha^n + c_1 \alpha^{n-1} + \cdots + c_n = 0$ where $c_i = b_i / x^{ki} \in B_{ki} / x^{ki} \subset K$ (since $B_{ki} \subset K \cdot x^{ki}$, dividing by $x^{ki}$ gives an element of $K$).

So $\alpha x^k$ is integral over $B$ iff $\alpha$ is integral over the subring $R_k := \{b / x^k : b \in B_k\} \subset K$... no, that's not quite right either. Let me reconsider.

$\alpha x^k$ integral over $B$ means: $\exists n, \exists b_1 \in B_{k}, b_2 \in B_{2k}, \ldots, b_n \in B_{nk}$ such that $(\alpha x^k)^n + b_1 (\alpha x^k)^{n-1} + \cdots + b_n = 0$.

Dividing by $x^{kn}$: $\alpha^n + (b_1/x^k) \alpha^{n-1} + (b_2/x^{2k}) \alpha^{n-2} + \cdots + (b_n/x^{nk}) = 0$.

So $\alpha$ is integral over the ring generated by $\{b/x^{ik} : b \in B_{ik}, i \geq 1\} \subset K$.

Hmm, this depends on $k$. Let me consider different cases.

**Case $k \geq 0$**: $B_k = A x^k$, so $B_k / x^k = A$. For $ik \geq 0$, $B_{ik} = A x^{ik}$, so $b/x^{ik} \in A$. So $\alpha$ is integral over $A$. Since $A$ is a UFD (hence integrally closed), $\alpha \in A$. So $\bar{B}_k = A x^k = B_k$ for $k \geq 0$.

**Case $k < 0$, say $k = -m$ with $m > 0$**: $B_{-m} = a^m A x^{-m}$, so $B_{-m}/x^{-m} = a^m A$. For $ik = -im$, $B_{-im} = a^{im} A x^{-im}$, so $b/x^{-im} \in a^{im} A$.

So $\alpha$ is integral over the subring of $K$ generated by $\{a^{im} A : i \geq 1\} = a^m A$ (since $a^{im} A \subset a^m A$ for $i \geq 1$, and $a^m A$ is already a ring... wait, is $a^m A$ a ring? It's an ideal, not a ring (it doesn't contain 1 unless $a$ is a unit).)

Hmm, the subring generated by $a^m A$ (as a set) inside $K$: this is $A[a^m A] = A$ (since $a^m A \subset A$ and $A$ is already a ring). Wait, no. The set $\{b/x^{-im} : b \in B_{-im}\} = a^{im} A$ for $i \geq 1$. The subring of $K$ generated by $\bigcup_{i \geq 1} a^{im} A$ is just $A$ (since all these are subsets of $A$, and $A$ is the smallest subring containing them... well, $A$ contains all of them, and the subring generated by them is contained in $A$, but does it equal $A$? It contains $a^m A$, and the subring generated by $a^m A$ is $\mathbb{Z}[a^m A]$... hmm, if $A$ is a $k$-algebra, then it's $k[a^m A] = k[a^m \cdot A]$. Since $a^m \cdot 1 = a^m \in a^m A$, we get $a^m$ is in the generated subring, and then $a^m \cdot (a^{-m} \cdot a^m) $... this is getting circular.

Let me reconsider. The subring of $K$ generated by $\bigcup_{i \geq 1} a^{im} A$ is the smallest subring of $K$ containing all elements of $a^{im} A$ for all $i \geq 1$. Since $a^m A \supset a^{2m} A \supset \cdots$, the union is just $a^m A$ (the largest one). The subring generated by $a^m A$ (as a subset of $K$) is the set of all finite sums of products of elements in $a^m A$ and their... no, subring generated means: all polynomial expressions in elements of $a^m A$ with integer (or base ring) coefficients. Since $a^m A$ is closed under multiplication ($(a^m r)(a^m s) = a^{2m} rs \in a^{2m} A \subset a^m A$) and addition, the subring generated by $a^m A$ is $a^m A \cup \{0\}$... no, a subring must contain 1 (depending on convention) or at least be closed under the operations.

Actually, the subring generated by a subset $S$ of a ring $R$ is the intersection of all subrings containing $S$. If we require subrings to contain 1, then the subring generated by $a^m A$ is $A$ itself (since $A$ is the smallest subring of $K$ containing $a^m A$ and 1, because $a^m \in a^m A$ and if $a^m$ is in the subring, then... well, we need $a^{-m}$ to get back to $A$, but $a^{-m}$ might not be in the subring).

Hmm, I think I'm overcomplicating this. Let me reconsider.

The condition is: $\alpha$ is integral over the ring $R$ where $R$ is the subring of $K$ generated by $\{c \in K : c = b/x^{ik} \text{ for some } b \in B_{ik}, i \geq 1\}$.

For $k = -m$: $R$ is generated by $\bigcup_{i \geq 1} a^{im} A$. Since $a^m \in a^m A$ and $a^{2m} \in a^{2m} A \subset a^m A$, etc., and $a^m A$ is closed under multiplication, $R$ is the subring generated by $a^m A$, which (if we include 1) is $A[a^m A] = A$ (since $a^m A \subset A$). Wait, but that would mean $\alpha$ is integral over $A$, hence $\alpha \in A$ (since $A$ is integrally closed), and then $\alpha x^{-m} \in A x^{-m}$. But $B_{-m} = a^m A x^{-m}$, so we'd need $\alpha \in a^m A$ for $\alpha x^{-m} \in B_{-m}$.

So if $\alpha \in A$ but $\alpha \notin a^m A$, then $\alpha x^{-m} \in \bar{B}_{-m}$ but $\alpha x^{-m} \notin B_{-m}$. This would mean $B$ is not integrally closed!

But wait, I need to double-check that $\alpha$ integral over $R = A$ is the right condition. Let me re-examine.

$\alpha x^{-m}$ is integral over $B$ means there exist $b_1 \in B_{-m}, b_2 \in B_{-2m}, \ldots, b_n \in B_{-nm}$ such that:
$$(\alpha x^{-m})^n + b_1 (\alpha x^{-m})^{n-1} + \cdots + b_n = 0$$

This gives: $\alpha^n x^{-mn} + b_1 \alpha^{n-1} x^{-m(n-1)} + \cdots + b_n = 0$.

Now $b_i \in B_{-im} = a^{im} A x^{-im}$, so $b_i = a^{im} c_i x^{-im}$ for some $c_i \in A$.

Substituting: $\alpha^n x^{-mn} + a^m c_1 \alpha^{n-1} x^{-m(n-1)} + a^{2m} c_2 \alpha^{n-2} x^{-m(n-2)} + \cdots + a^{nm} c_n = 0$.

Dividing by $x^{-mn}$ (i.e., multiplying by $x^{mn}$): $\alpha^n + a^m c_1 \alpha^{n-1} x^{m} + a^{2m} c_2 \alpha^{n-2} x^{2m} + \cdots + a^{nm} c_n x^{nm} = 0$.

But this is an equation in $K(x)$, and the terms have different powers of $x$! So for this to be zero, each coefficient must be zero:
- $\alpha^n = 0$ (coefficient of $x^0$) — but $\alpha \neq 0$ in a domain, contradiction!

Wait, that can't be right. Let me reconsider.

Oh, I see the issue. The equation $(\alpha x^{-m})^n + b_1 (\alpha x^{-m})^{n-1} + \cdots + b_n = 0$ is an equation in $K(x)$, and all terms should have the same degree for it to be a "homogeneous" integrality relation. But I was assuming the $b_i$ are homogeneous of degree $-im$, which makes the $i$-th term have degree $-m(n-i) + (-im) = -mn + im - im = -mn$. Wait, let me recompute.

$(\alpha x^{-m})^{n-i}$ has degree $-m(n-i)$. And $b_i$ has degree $-im$. So the product $b_i (\alpha x^{-m})^{n-i}$ has degree $-m(n-i) - im = -mn + mi - im = -mn$. And $(\alpha x^{-m})^n$ has degree $-mn$. So all terms have degree $-mn$. Good, so the equation is homogeneous of degree $-mn$.

So dividing by $x^{-mn}$ (multiplying by $x^{mn}$):
$\alpha^n + a^m c_1 \alpha^{n-1} + a^{2m} c_2 \alpha^{n-2} + \cdots + a^{nm} c_n = 0$.

This is an equation in $K$ (no $x$ anymore). So $\alpha$ satisfies:
$$\alpha^n + a^m c_1 \alpha^{n-1} + a^{2m} c_2 \alpha^{n-2} + \cdots + a^{nm} c_n = 0$$
with $c_i \in A$.

This means $\alpha$ is integral over the ring $A[a^m] = A$ (since $a^m \in A$). Wait, more precisely, $\alpha$ is integral over the subring of $K$ generated by $a^m A$ (and 1). But $a^m A \subset A$, so this subring is contained in $A$. And it contains $a^m$ (take $c = 1 \in A$, then $a^m \cdot 1 = a^m$). 

Hmm, but the subring generated by $a^m A$ (and 1) might be smaller than $A$. It's $A$ iff $a^m$ is a unit or generates $A$ as a ring... no. The subring generated by $1$ and $a^m A$ is $\mathbb{Z}[a^m A]$ (or $k[a^m A]$ if $A$ is a $k$-algebra). This is the set of all polynomial expressions in elements of $a^m A$ with coefficients in $\mathbb{Z}$ (or $k$). Since $a^m A$ is an ideal of $A$ closed under multiplication, $k[a^m A]$ consists of elements of the form $c_0 + c_1 s_1 + c_2 s_1 s_2 + \cdots$ where $c_i \in k$ and $s_i \in a^m A$. But $s_1 s_2 \in a^{2m} A \subset a^m A$, etc. So $k[a^m A] = k + a^m A$ (as a $k$-vector space, it's $k \cdot 1 + a^m A$, since products of elements in $a^m A$ land in $a^{2m} A \subset a^m A$).

So the subring is $k + a^m A$ (assuming $A$ is a $k$-algebra; more generally, it's $\mathbb{Z} + a^m A$ or the image of $\mathbb{Z} \to A$ plus $a^m A$). Let me call this $R_m = k + a^m A$.

So $\alpha x^{-m} \in \bar{B}$ iff $\alpha$ is integral over $R_m = k + a^m A$.

Now, $R_m \subset A$, and $A$ is integral over $R_m$? Not necessarily. But we need: what is the integral closure of $R_m$ in $K$?

If $a$ is square-free, is $A$ integral over $R_m = k + a^m A$? 

Hmm, this is getting complicated. Let me try a different, cleaner approach.

Let me use the fact that $B = A[x, ax^{-1}]$ and consider the normalization.

Actually, I think there's a cleaner way using the theory of Rees-like algebras or blow-up algebras.

Note that $A[x, ax^{-1}]$ is related to the blow-up of $\text{Spec}(A)$ along the ideal $(a)$. Specifically, the blow-up algebra is $\text{Rees}(a) = A[at] = \bigoplus_{n \geq 0} a^n t^n \subset A[t]$, and the associated graded ring is $\text{gr}_a(A) = \bigoplus a^n / a^{n+1}$.

Actually, $A[x, ax^{-1}]$ is the "affine chart" of the blow-up. More precisely, if we blow up $\text{Spec}(A)$ at the ideal $(a)$, one affine chart is $\text{Spec}(A[a/x])$ where $x$ is the blow-up variable. But $A[x, ax^{-1}]$ includes both $x$ and $a/x$, so it's more like the "full" blow-up algebra in some sense.

Hmm, actually I think $A[x, ax^{-1}]$ is the symbolic Rees algebra or something related. Let me think again.

$A[x, ax^{-1}] = \bigoplus_{n \in \mathbb{Z}} I_n x^n$ where $I_n = A$ for $n \geq 0$ and $I_n = a^{-n} A = a^{|n|} A$ for $n < 0$.

This is the "extended Rees algebra" of the ideal $(a)$! The extended Rees algebra is $A[t, t^{-1}]$ with a specific grading... no. The extended Rees algebra of an ideal $I$ is $R = \bigoplus_{n \in \mathbb{Z}} I^n t^n$ where $I^n = A$ for $n \leq 0$ (by convention) and $I^n$ for $n > 0$. Wait, that's $A[t, It^{-1}] = \bigoplus_{n \geq 0} A t^n \oplus \bigoplus_{n > 0} I^n t^{-n}$.

Yes! $A[x, ax^{-1}]$ with $I = (a)$ is exactly the extended Rees algebra $A[t, at^{-1}]$ (with $t = x$). The extended Rees algebra of $I = (a)$ is:
$$R = A[t, at^{-1}] = \bigoplus_{n \geq 0} A t^n \oplus \bigoplus_{n > 0} a^n A t^{-n}$$

And there's a well-known result: **the extended Rees algebra $A[t, It^{-1}]$ is integrally closed if and only if $A$ is integrally closed and $I$ is integrally closed** (as an ideal, meaning $I = \bar{I}$, the integral closure of the ideal).

Wait, is that right? Let me recall. The integral closure of an ideal $I$ in a domain $A$ is $\bar{I} = \{x \in A : x \text{ is integral over } I\}$, where $x$ integral over $I$ means $x$ satisfies $x^n + a_1 x^{n-1} + \cdots + a_n = 0$ with $a_i \in I^i$.

And the result is: the Rees algebra $A[It] = \bigoplus_{n \geq 0} I^n t^n$ is integrally closed iff $A$ is integrally closed and $I$ is integrally closed (i.e., $I = \bar{I}$).

For the extended Rees algebra, I believe a similar result holds: $A[t, It^{-1}]$ is integrally closed iff $A$ is integrally closed and $I$ is integrally closed.

Now, in a UFD, when is the principal ideal $(a)$ integrally closed? 

The integral closure of $(a)$ is $\bar{(a)} = \{x \in A : x \text{ integral over } (a)\}$. For a principal ideal $(a)$ in a UFD, $\bar{(a)} = (\sqrt{a})$... no, that's not right either.

Actually, the integral closure of a principal ideal $(a)$ in an integrally closed domain is $(a)$ itself... no, that's not right. Let me think.

In a UFD (or more generally, a Krull domain), the integral closure of an ideal $I$ is $\bar{I} = \bigcap_{v} \{x : v(x) \geq v(I)\}$ where the intersection is over all DVR valuations $v$ of $K$ associated to height-1 primes, and $v(I) = \min_{y \in I} v(y)$.

For $I = (a)$: $v((a)) = v(a)$ for each valuation $v$. So $\bar{(a)} = \{x \in A : v(x) \geq v(a) \text{ for all } v\} = \{x \in A : v(x) \geq v(a) \text{ for all height-1 primes } \mathfrak{p}\}$.

In a UFD, the height-1 primes are $(p)$ for irreducible $p$, and $v_p(x)$ is the $p$-adic valuation. So $\bar{(a)} = \{x \in A : v_p(x) \geq v_p(a) \text{ for all irreducible } p\}$.

If $a = u \prod p_i^{e_i}$, then $v_{p_i}(a) = e_i$ and $v_q(a) = 0$ for $q \neq p_i$. So $\bar{(a)} = \{x \in A : v_{p_i}(x) \geq e_i \text{ for all } i, \text{ and } v_q(x) \geq 0 \text{ for } q \neq p_i\} = \{x \in A : p_i^{e_i} | x \text{ for all } i\} = (\prod p_i^{e_i}) \cdot A = (a)$.

Wait, so $\bar{(a)} = (a)$ always? That would mean principal ideals in UFDs are always integrally closed, and hence the extended Rees algebra is always integrally closed, contradicting my earlier example.

Let me re-examine. In my example, $A = k[t]$, $a = t^2$. Then $(a) = (t^2)$, and $\bar{(t^2)} = \{x \in k[t] : v_t(x) \geq 2\} = (t^2)$. So $(t^2)$ is integrally closed as an ideal. Then by the theorem, $A[x, ax^{-1}] = k[t][x, t^2 x^{-1}]$ should be integrally closed. But I showed earlier that it's NOT integrally closed (the $A_1$ singularity).

So either my recollection of the theorem is wrong, or my example is wrong. Let me re-examine the example.

$B = k[t, X, Y]/(XY - t^2)$. I claimed this is the $A_1$ singularity and is not integrally closed, with normalization $k[u, v]$ via $t \mapsto uv, X \mapsto u^2, Y \mapsto v^2$.

Let me verify: is $u$ in the fraction field of $B$? $u = X/t = u^2/(uv) = u/v$... hmm, $u = X/t$ in $\text{Frac}(B)$. And $u^2 = X \in B$, so $u$ satisfies $Z^2 - X = 0$, which is monic with coefficients in $B$. So $u$ is integral over $B$. And $u \notin B$ (since $B$ maps to $k[u^2, v^2, uv]$, the Veronese subring, and $u$ has odd degree). So $B$ is not integrally closed. ✓.

Now, is $B = k[t][x, t^2/x]$? We have $B = k[t, X, Y]/(XY - t^2)$. Setting $x = X$ and $t^2/x = Y$ (i.e., $Y = t^2/X$), we get $B = k[t][X, t^2/X]$. Yes, this is $A[x, ax^{-1}]$ with $A = k[t]$, $a = t^2$.

So the extended Rees algebra $k[t][x, t^2 x^{-1}]$ is NOT integrally closed, even though $(t^2)$ is integrally closed as an ideal in $k[t]$.

So my recollection of the theorem must be wrong. Let me reconsider.

Actually, I think the correct theorem is about the Rees algebra $A[It] = \bigoplus_{n \geq 0} I^n t^n$, not the extended Rees algebra. And the result is:

- $A[It]$ is integrally closed iff $A$ is integrally closed and $I$ is integrally closed.

But the extended Rees algebra $A[t, It^{-1}]$ is a different beast. Let me think about what its integral closure is.

The extended Rees algebra $R = A[t, It^{-1}]$ has the property that $R/(t^{-1}) \cong \text{gr}_I(A)$ (the associated graded ring) and $R[t^{-1}] \cong A[t, t^{-1}]$ (which is integrally closed if $A$ is).

Hmm, I think the integral closure of the extended Rees algebra $A[t, It^{-1}]$ is $\bigoplus_{n \in \mathbb{Z}} \overline{I^n} t^n$ where $\overline{I^n}$ is the integral closure of $I^n$ (with $I^0 = A$ and $I^n = A$ for $n \leq 0$ by convention). Wait, but for $n \leq 0$, $I^n = A$, and for $n > 0$, $I^n = (a^n)$.

So the integral closure of $A[x, ax^{-1}]$ would be $\bigoplus_{n \geq 0} A x^n \oplus \bigoplus_{n > 0} \overline{(a^n)} x^{-n}$.

In a UFD, $\overline{(a^n)} = (a^n)$ (as I computed, principal ideals in UFDs are integrally closed). So the integral closure would be $A[x, ax^{-1}]$ itself, contradicting the example.

Something is wrong. Let me reconsider.

Oh wait, I think the issue is that the integral closure of the extended Rees algebra is NOT simply $\bigoplus \overline{I^n} t^n$. The grading argument I was making earlier showed that the integral closure is graded, but the graded pieces are not simply $\overline{I^n}$.

Let me redo the computation. We have $B = \bigoplus_{n \geq 0} A x^n \oplus \bigoplus_{n > 0} a^n A x^{-n}$, and $\bar{B} = \bigoplus_{n \in \mathbb{Z}} \bar{B}_n$ where $\bar{B}_n \subset K x^n$.

For $n \geq 0$: I showed $\bar{B}_n = A x^n$ (since $\alpha$ integral over $A$ implies $\alpha \in A$). ✓.

For $n = -m < 0$: $\alpha x^{-m} \in \bar{B}_{-m}$ iff $\alpha$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + a^{2m} c_2 \alpha^{N-2} + \cdots + a^{Nm} c_N = 0$ for some $c_i \in A$.

This means $\alpha$ is integral over the ideal $(a^m)$ in a specific sense. Let me think about what this means.

The equation is $\alpha^N + \sum_{i=1}^N a^{im} c_i \alpha^{N-i} = 0$, which can be rewritten as $\alpha^N \in (a^m \alpha^{N-1}, a^{2m} \alpha^{N-2}, \ldots, a^{Nm})$.

This is the condition that $\alpha$ is integral over the ideal $(a^m)$ in the sense of integral dependence on ideals: $\alpha$ is integral over the ideal $J = (a^m)$ means $\alpha$ satisfies a monic polynomial $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i \in J^i = (a^{mi})$.

So $\alpha x^{-m} \in \bar{B}_{-m}$ iff $\alpha \in \overline{(a^m)}$ (the integral closure of the ideal $(a^m)$).

Now, in a UFD, what is $\overline{(a^m)}$?

As I computed, for a principal ideal $(b)$ in a UFD, $\overline{(b)} = (b)$. So $\overline{(a^m)} = (a^m)$.

But this gives $\bar{B}_{-m} = a^m A x^{-m} = B_{-m}$, so $\bar{B} = B$, meaning $B$ is integrally closed. This contradicts the example!

Let me re-examine the example more carefully. $A = k[t]$, $a = t^2$, $B = k[t][x, t^2 x^{-1}]$.

The element $u = x/t$ is in $\text{Frac}(B)$. We have $u^2 = x^2/t^2$. And $x \cdot (t^2/x) = t^2$, so $t^2 = x \cdot (t^2 x^{-1})$. Then $u^2 = x^2/t^2 = x/(t^2/x) = x/(t^2 x^{-1})$.

In terms of the grading: $x$ has degree 1, $t^2 x^{-1}$ has degree $-1$, $t$ has degree 0. So $u = x/t$ has degree 1. And $u^2 = x^2/t^2$ has degree 2.

Now, $u^2 = x^2/t^2$. Is $u^2 \in B$? $u^2 = x^2/t^2$. The degree-2 part of $B$ is $A x^2 = k[t] x^2$. Is $x^2/t^2 \in k[t] x^2$? That would require $1/t^2 \in k[t]$, which is false. So $u^2 \notin B$.

But $u^2 = x^2/t^2$ and $u$ satisfies $u^2 - x^2/t^2 = 0$, which is $Z^2 - x^2/t^2 = 0$. But $x^2/t^2 \notin B$ (it's in $K$ but not in $A = k[t]$). So this is NOT a monic polynomial with coefficients in $B$!

Wait, but I said $u^2 = X$ where $X = x$ in the original notation... no. Let me redo. In the example, $B = k[t, X, Y]/(XY - t^2)$ with $x = X$, $Y = t^2/x$. And the normalization map is $t \mapsto uv, X \mapsto u^2, Y \mapsto v^2$. So $u^2 = X = x$ and $v^2 = Y = t^2/x$.

So $u^2 = x \in B$! And $u$ satisfies $Z^2 - x = 0$, which IS monic with coefficient $x \in B$. So $u$ is integral over $B$.

Now, $u = x/t$. In the grading, $x$ has degree 1 and $t$ has degree 0, so $u$ has degree 1. And $u^2 = x$ has degree 1... wait, $u^2$ should have degree 2 if $u$ has degree 1. But $x$ has degree 1. Contradiction!

The issue is that $u = x/t$ is NOT homogeneous of degree 1 in the $\mathbb{Z}$-grading of $B$. The grading is on $B$, and $u \in \text{Frac}(B)$, but $u$ is not a homogeneous element of $\text{Frac}(B)$ with respect to this grading... or is it?

Actually, the fraction field of a graded ring doesn't have a natural grading. The grading extends to the fraction field only in a limited way. Let me reconsider.

$B = \bigoplus_{n \in \mathbb{Z}} B_n$ where $B_n = A x^n$ for $n \geq 0$ and $B_n = a^{|n|} A x^n$ for $n < 0$. The fraction field of $B$ is $K(x)$ where $K = \text{Frac}(A)$, since $B \subset K[x, x^{-1}]$ and $K[x, x^{-1}]$ has fraction field $K(x)$... actually $K[x, x^{-1}]$ is already a field? No, $K[x, x^{-1}]$ is the Laurent polynomial ring, which is not a field. Its fraction field is $K(x)$, the field of rational functions.

So $\text{Frac}(B) = K(x)$.

Now, $u = x/t$ where $t \in A \subset B_0$. So $u = x \cdot t^{-1}$. In the "graded fraction field," $x$ has degree 1 and $t^{-1}$ has degree 0, so $u$ has degree 1. And $u^2 = x^2/t^2$ has degree 2. But $u^2 = x$ (from the normalization map)... 

Wait, no! $u^2 = x$ is in the normalization, not in $B$ itself. Let me be more careful. In the normalization $k[u,v]$, we have $x = u^2$, $t = uv$, $Y = v^2$. So $u = x/t = u^2/(uv) = u/v$. And $u^2 = x$. But this is in $k[u,v]$, not in $B$.

In $B$, $u$ is an element of $\text{Frac}(B) = K(x)$ where $K = k(t)$. We have $u = x/t \in K(x)$ (since $x \in B$ and $t \in B$). And $u^2 = x^2/t^2 \in K(x)$. The relation $u^2 = x$ would mean $x^2/t^2 = x$, i.e., $x = t^2$, which is NOT true in $B$ (there's no such relation).

So I made an error. The normalization map sends $x \mapsto u^2$, but that doesn't mean $u^2 = x$ in $\text{Frac}(B)$. It means that under the inclusion $B \hookrightarrow k[u,v]$, $x$ maps to $u^2$. But $u$ is not in $\text{Frac}(B)$ in a way that makes $u^2 = x$.

Hmm, wait. The normalization of $B$ is the integral closure $\bar{B}$ in $\text{Frac}(B)$. The map $B \to k[u,v]$ given by $t \mapsto uv, x \mapsto u^2, Y \mapsto v^2$ is an inclusion (since $B = k[u^2, v^2, uv] \subset k[u,v]$). And $k[u,v]$ is the integral closure of $B$ in... what field?

$\text{Frac}(B) = \text{Frac}(k[u^2, v^2, uv])$. What is this fraction field? $u^2, v^2, uv$ generate the fraction field $k(u,v)$ (since $u = u^2 \cdot v / (uv) \cdot ... $ hmm, $u = (u^2 v)/(uv)$... but $v$ is not in the fraction field of $B$ directly. Actually, $u^2 / (uv) = u/v$ and $v^2/(uv) = v/u$, so $u/v \in \text{Frac}(B)$ and $v/u \in \text{Frac}(B)$. And $uv \in B$. So $(u/v) \cdot (uv) = u^2 \in B$ and $(u/v)^2 \cdot (uv)^2 = u^2 v^2 \cdot ... $ hmm. Let me think: $\text{Frac}(B)$ contains $u^2, v^2, uv$. From these, $u^2 \cdot v^2 / (uv)^2 = 1$, so that's trivial. $u^2/(uv) = u/v$ and $v^2/(uv) = v/u$. So $u/v \in \text{Frac}(B)$. Then $(uv) \cdot (u/v) = u^2 \in B$ and $(uv)/(u/v) = v^2 \in B$. Can we get $u$ itself? $u = \sqrt{u^2}$, but square roots aren't in the fraction field in general. Actually, $u = (uv) \cdot u / (uv) $... we need $u$ in terms of $u^2, v^2, uv$. We have $u^2$ and $uv$, so $u = u^2 \cdot v / (uv \cdot v) $... this is circular.

Actually, $\text{Frac}(k[u^2, v^2, uv])$: the transcendence degree is 2 (since $k[u^2, v^2, uv]$ has Krull dimension 2). And $k(u,v)$ also has transcendence degree 2 over $k$. Is $\text{Frac}(k[u^2, v^2, uv]) = k(u,v)$? 

We need to check if $u \in \text{Frac}(k[u^2, v^2, uv])$. $u = u^2 / u$, but $u$ is not in the ring. However, $u^2 \cdot v = u \cdot (uv)$, so $u = (u^2 v)/(uv)$. But $v$ is not in $\text{Frac}(B)$ either (by the same argument). Hmm, but $v = v^2 / v$ and $v = (uv)/u$, both circular.

Let me think about it differently. $k(u^2, v^2, uv) \subset k(u,v)$. The extension $k(u,v) / k(u^2, v^2, uv)$: note that $u^2, v^2, uv$ are all invariant under the involution $(u,v) \mapsto (-u, -v)$. So $k(u^2, v^2, uv) = k(u,v)^{\langle \sigma \rangle}$ where $\sigma(u,v) = (-u,-v)$, and $[k(u,v) : k(u^2, v^2, uv)] = 2$.

So $\text{Frac}(B) = k(u^2, v^2, uv) \neq k(u,v)$. The integral closure of $B$ is in $\text{Frac}(B) = k(u^2, v^2, uv)$, not in $k(u,v)$.

So is $u \in \text{Frac}(B) = k(u^2, v^2, uv)$? No! $u \notin k(u^2, v^2, uv)$ (since $u$ is not invariant under $\sigma$). So $u$ is NOT in the fraction field of $B$, and the "normalization" $k[u,v]$ is NOT the integral closure of $B$ in its fraction field.

This means my earlier analysis was wrong. $k[u,v]$ is not the integral closure of $B$ in $\text{Frac}(B)$. The integral closure of $B$ in $\text{Frac}(B) = k(u^2, v^2, uv)$ is something else.

So maybe $B = k[t, X, Y]/(XY - t^2)$ IS integrally closed? Let me check using Serre's criterion.

$B = k[t, X, Y]/(XY - t^2)$. This is a 2-dimensional domain (since $k[t,X,Y]$ is 3-dimensional and we quotient by one equation). The singular locus is where the Jacobian matrix has rank $< 1$: $\partial(XY - t^2)/\partial X = Y$, $\partial/\partial Y = X$, $\partial/\partial t = -2t$. The singular locus is $X = Y = t = 0$, which is the origin, a point of codimension 2.

By Serre's criterion, $B$ is normal iff $R_1$ (regular in codimension 1) and $S_2$ (Serre's condition). $R_1$: the singular locus has codimension 2, so $B$ is regular in codimension 1. ✓. $S_2$: $B$ is a hypersurface (complete intersection), hence Cohen-Macaulay, hence $S_2$. ✓.

So $B = k[t,X,Y]/(XY - t^2)$ IS integrally closed! My earlier claim that it's the $A_1$ singularity and not integrally closed was WRONG.

Wait, but the $A_1$ surface singularity $k[u^2, v^2, uv]$ is well-known to not be integrally closed (its normalization is $k[u,v]$). And $k[u^2, v^2, uv] \cong k[t,X,Y]/(XY - t^2)$ via $t = uv, X = u^2, Y = v^2$. So there's a contradiction.

The resolution: $k[u^2, v^2, uv]$ is NOT integrally closed IN $k(u,v)$, but its fraction field is $k(u^2, v^2, uv) \neq k(u,v)$. The integral closure of $k[u^2, v^2, uv]$ in its OWN fraction field $k(u^2, v^2, uv)$ might be itself!

Let me check: is $k[u^2, v^2, uv]$ integrally closed in $k(u^2, v^2, uv)$?

An element of $k(u^2, v^2, uv)$ integral over $k[u^2, v^2, uv]$: since $k[u^2, v^2, uv]$ is the invariant ring $k[u,v]^{\langle \sigma \rangle}$ where $\sigma: (u,v) \mapsto (-u,-v)$, and $k[u,v]$ is integral over $k[u^2, v^2, uv]$ (since $u$ satisfies $Z^2 - u^2 = 0$), the integral closure of $k[u^2, v^2, uv]$ in $k(u,v)$ is $k[u,v]$.

But in $k(u^2, v^2, uv)$: an element $\alpha \in k(u^2, v^2, uv)$ integral over $k[u^2, v^2, uv]$ is also in $k(u,v)$ (since $k(u^2, v^2, uv) \subset k(u,v)$) and integral over $k[u^2, v^2, uv]$, hence in $k[u,v]$ (the integral closure in $k(u,v)$). So $\alpha \in k[u,v] \cap k(u^2, v^2, uv)$.

Now, $k[u,v] \cap k(u^2, v^2, uv)$: an element of $k[u,v]$ that is in $k(u^2, v^2, uv)$ must be invariant under $\sigma$ (since $k(u^2, v^2, uv) = k(u,v)^{\sigma}$). So $k[u,v] \cap k(u^2, v^2, uv) = k[u,v]^{\sigma} = k[u^2, v^2, uv]$.

So the integral closure of $k[u^2, v^2, uv]$ in $k(u^2, v^2, uv)$ is $k[u^2, v^2, uv]$ itself. It IS integrally closed!

This makes sense with the Serre's criterion argument. The $A_1$ singularity $k[u^2, v^2, uv]$ is a normal surface (it's a rational double point, which is normal). The fact that $k[u,v]$ is "bigger" is because $k[u,v]$ is the normalization in a BIGGER field $k(u,v)$, not in the fraction field of $k[u^2, v^2, uv]$.

OK so I was wrong. $B = k[t,X,Y]/(XY - t^2)$ IS integrally closed. So the example with $a = t^2$ doesn't give a counterexample.

Let me reconsider the problem. Maybe $A[x, a/x]$ is always integrally closed when $A$ is a UFD?

Going back to the grading argument: $\bar{B}_{-m} = \overline{(a^m)} x^{-m}$ where $\overline{(a^m)}$ is the integral closure of the ideal $(a^m)$ in $A$. And in a UFD, $\overline{(a^m)} = (a^m)$ (principal ideals in integrally closed domains are integrally closed... wait, is that true?).

Hmm, actually, I need to be more careful. The integral closure of an ideal $I$ in a domain $A$ is $\bar{I} = \{x \in A : x^n + a_1 x^{n-1} + \cdots + a_n = 0, a_i \in I^i\}$. For a principal ideal $(a)$ in a UFD, is $\overline{(a)} = (a)$?

In a Krull domain (which includes UFDs), the integral closure of an ideal $I$ is $\bar{I} = \{x \in A : v(x) \geq v(I) \text{ for all essential valuations } v\}$, where $v(I) = \min_{y \in I} v(y)$.

For $I = (a^m)$: $v((a^m)) = m \cdot v(a)$ for each valuation $v$. So $\overline{(a^m)} = \{x \in A : v(x) \geq m \cdot v(a) \text{ for all } v\}$.

In a UFD, the essential valuations are $v_p$ for irreducible $p$. If $a = u \prod p_i^{e_i}$, then $v_{p_i}(a) = e_i$ and $v_q(a) = 0$ for $q \neq p_i$. So $v_{p_i}((a^m)) = me_i$ and $v_q((a^m)) = 0$.

$\overline{(a^m)} = \{x \in A : v_{p_i}(x) \geq me_i \text{ for all } i\} = (\prod p_i^{me_i}) A = (a^m)$.

So yes, $\overline{(a^m)} = (a^m)$ in a UFD. This means $\bar{B}_{-m} = (a^m) x^{-m} = B_{-m}$, and hence $\bar{B} = B$, i.e., $B$ is integrally closed.

Wait, but I need to double-check the step where I claimed $\alpha x^{-m} \in \bar{B}_{-m}$ iff $\alpha \in \overline{(a^m)}$. Let me re-examine.

$\alpha x^{-m}$ is integral over $B$ iff there exist $b_1, \ldots, b_N \in B$ such that $(\alpha x^{-m})^N + b_1 (\alpha x^{-m})^{N-1} + \cdots + b_N = 0$.

I claimed we can take $b_i$ to be homogeneous of degree $-im$. Is this justified?

The general theory of graded rings says: if $B$ is a $\mathbb{Z}$-graded ring and $f$ is a homogeneous element of degree $d$ in some graded extension, then $f$ is integral over $B$ iff $f$ satisfies a monic polynomial with homogeneous coefficients of appropriate degrees. But here, $\alpha x^{-m}$ is an element of $K(x)$, and we need to be careful about what "homogeneous" means.

Actually, $K(x)$ has a $\mathbb{Z}$-grading (as a $K$-vector space) where $x$ has degree 1. An element $\alpha x^{-m}$ with $\alpha \in K$ is homogeneous of degree $-m$. And $B$ is a graded subring. The integral closure of a graded domain in its fraction field is graded (this is a standard result, see e.g., Eisenbud or Bruns-Herzog).

But the fraction field of $B$ is $K(x)$, the field of rational functions, which is NOT graded (it's a field, so the only homogeneous elements are 0). The grading on $K[x, x^{-1}]$ extends to $K(x)$ in the sense that $K(x) = \bigcup_n K[x, x^{-1}] \cdot x^{-n}$... hmm, actually $K(x)$ doesn't have a $\mathbb{Z}$-grading in the usual sense.

Let me reconsider. The correct statement is: $B \subset K[x, x^{-1}] \subset K(x)$, and $K[x, x^{-1}]$ is $\mathbb{Z}$-graded. The integral closure of $B$ in $K(x)$ is contained in $K[x, x^{-1}]$ (since $K[x, x^{-1}]$ is integrally closed and contains $B$). And the integral closure of a $\mathbb{Z}$-graded ring $B$ in a $\mathbb{Z}$-graded over-ring (like $K[x, x^{-1}]$) is $\mathbb{Z}$-graded.

More precisely: $\bar{B} = \{f \in K[x, x^{-1}] : f \text{ integral over } B\}$, and if $f = \sum_k f_k x^k \in \bar{B}$ (with $f_k \in K$), then each $f_k x^k \in \bar{B}$.

This is because: if $f$ satisfies $f^N + b_1 f^{N-1} + \cdots + b_N = 0$ with $b_i \in B$, we can decompose by degree. Write $b_i = \sum_j b_{i,j}$ (degree decomposition). Then the degree-$d$ component of the equation gives a relation for the degree-$d$ component of $f^N + \cdots$. By a standard argument (using the "leading term" or induction on degree), each homogeneous component of $f$ is integral over $B$.

OK so I'll accept that $\bar{B}$ is graded and $\bar{B}_{-m} = \{\alpha \in K : \alpha x^{-m} \in \bar{B}\} \cdot x^{-m}$.

Now, $\alpha x^{-m} \in \bar{B}$ (with $\alpha \in K$) iff $\alpha x^{-m}$ is integral over $B$. Since $\alpha x^{-m}$ is homogeneous of degree $-m$, it satisfies a monic polynomial with homogeneous coefficients: $(\alpha x^{-m})^N + b_1 (\alpha x^{-m})^{N-1} + \cdots + b_N = 0$ where $b_i$ is homogeneous of degree $-im$ (so that each term has degree $-mN$).

$b_i \in B_{-im}$. For $i \geq 1$: $B_{-im} = a^{im} A x^{-im}$ (when $im > 0$, i.e., always since $m > 0$). So $b_i = a^{im} c_i x^{-im}$ for some $c_i \in A$.

The equation becomes: $\alpha^N x^{-mN} + a^m c_1 \alpha^{N-1} x^{-m(N-1)} + a^{2m} c_2 \alpha^{N-2} x^{-m(N-2)} + \cdots + a^{Nm} c_N = 0$.

All terms have degree $-mN$, so dividing by $x^{-mN}$: $\alpha^N + a^m c_1 \alpha^{N-1} + a^{2m} c_2 \alpha^{N-2} + \cdots + a^{Nm} c_N = 0$.

This is exactly the condition that $\alpha$ is integral over the ideal $(a^m)$ (in the sense of integral dependence on ideals): $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i \in (a^m)^i = (a^{mi})$.

BUT: integral dependence on an ideal is usually defined for $\alpha \in A$ (not $\alpha \in K$). The integral closure of an ideal $I$ in $A$ is $\bar{I} = \{\alpha \in A : \alpha \text{ integral over } I\}$. Here, $\alpha \in K$, not necessarily in $A$.

So the condition is: $\alpha \in K$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + \cdots + a^{Nm} c_N = 0$ with $c_i \in A$. This means $\alpha$ is integral over the subring $A[a^m] = A$ (since $a^m \in A$)... no, the coefficients are $a^{im} c_i \in (a^{mi}) \subset A$, not arbitrary elements of $A$.

Hmm, the condition is that $\alpha$ is integral over the "ideal" $(a^m)$ but with $\alpha \in K$ (not necessarily in $A$). Let me think about what this means.

If $\alpha \in K$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + \cdots + a^{Nm} c_N = 0$ with $c_i \in A$, then $\alpha$ is integral over $A$ (since all coefficients $a^{im} c_i \in A$). Since $A$ is integrally closed (UFD), $\alpha \in A$.

So $\alpha \in A$ and $\alpha$ is integral over the ideal $(a^m)$, meaning $\alpha \in \overline{(a^m)} = (a^m)$ (in a UFD).

Therefore $\bar{B}_{-m} = (a^m) x^{-m} = B_{-m}$, and $\bar{B} = B$.

So $B = A[x, ax^{-1}]$ IS integrally closed when $A$ is a UFD!

Wait, but let me also handle the case $a = 0$. If $a = 0$, then $B = A[x, 0 \cdot x^{-1}] = A[x]$. And $A[x]$ is a UFD if $A$ is a UFD (by Gauss's lemma), hence integrally closed. So $a = 0$ is fine too.

Hmm wait, $a/x$ when $a = 0$ is just $0$, so $A[x, a/x] = A[x, 0] = A[x]$. And $A[x]$ is a polynomial ring over a UFD, which is a UFD, hence integrally closed. ✓.

What about $a$ being a unit? If $a$ is a unit, $B = A[x, ax^{-1}] = A[x, x^{-1}]$ (since $x^{-1} = a^{-1} \cdot ax^{-1}$). This is a Laurent polynomial ring over $A$, which is integrally closed if $A$ is. ✓.

So it seems like $A[x, a/x]$ is always integrally closed when $A$ is a UFD, for any $a \in A$.

But wait, I should double-check my argument more carefully. The key step was: $\alpha \in K$ integral over $A$ (with the specific polynomial having coefficients in $(a^{mi})$) implies $\alpha \in A$ (since $A$ is integrally closed) and then $\alpha \in \overline{(a^m)} = (a^m)$.

The first part: $\alpha$ satisfies $\alpha^N + a^m c_1 \alpha^{N-1} + \cdots + a^{Nm} c_N = 0$ with $c_i \in A$. The coefficients $a^{im} c_i$ are in $A$, so this is a monic polynomial with coefficients in $A$, hence $\alpha$ is integral over $A$, hence $\alpha \in A$ (since $A$ is integrally closed). ✓.

The second part: $\alpha \in A$ and $\alpha$ satisfies $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i \in (a^m)^i = (a^{mi})$. This means $\alpha$ is in the integral closure of the ideal $(a^m)$ in $A$. In a UFD, $\overline{(a^m)} = (a^m)$. ✓.

So the argument is complete. Let me also verify with a potential counterexample to make sure.

Take $A = k[s,t]$, $a = s^2 t$ (not square-free). Then $B = A[x, s^2 t / x] = k[s,t][x, s^2 t x^{-1}]$.

By my argument, $B$ should be integrally closed. Let me verify with Serre's criterion. $B \cong k[s,t,X,Y]/(XY - s^2 t)$. This is a 3-dimensional hypersurface. The singular locus is where $Y = X = s^2 t$'s partial derivatives vanish: $\partial/\partial X = Y$, $\partial/\partial Y = X$, $\partial/\partial s = 2st$, $\partial/\partial t = s^2$. Singular locus: $X = Y = 0$ and ($s = 0$ or $t = 0$) and $s^2 = 0$, so $s = 0$. So the singular locus is $X = Y = s = 0$, which is the $t$-axis, a 1-dimensional variety in a 3-dimensional variety, codimension 2. By Serre's criterion ($R_1$: regular in codim 1 ✓, $S_2$: hypersurface hence CM hence $S_2$ ✓), $B$ is integrally closed. ✓.

Another example: $A = k[s,t]$, $a = s^2$. $B = k[s,t,X,Y]/(XY - s^2)$. Singular locus: $X = Y = s = 0$, the $t$-axis, codimension 2 in the 3-dimensional variety. $R_1$ ✓, $S_2$ ✓. Integrally closed. ✓.

Hmm, but what if $A$ has dimension 1? Take $A = k[t]$, $a = t^2$. $B = k[t,X,Y]/(XY - t^2)$. This is 2-dimensional. Singular locus: $X = Y = t = 0$, the origin, codimension 2. $R_1$ ✓, $S_2$ ✓ (hypersurface). Integrally closed. ✓. (This is the $A_1$ surface singularity, which is indeed normal.)

What about $A = k[t]$, $a = t^3$? $B = k[t,X,Y]/(XY - t^3)$. Singular locus: $X = Y = t = 0$, origin, codim 2. $R_1$ ✓, $S_2$ ✓. Integrally closed. ✓. (This is the $A_2$ surface singularity, also normal.)

So it seems like the answer is YES, $A[x, a/x]$ is always integrally closed when $A$ is a UFD.

But wait, I want to make sure my argument about the graded integral closure is rigorous. Let me also consider whether there could be non-homogeneous elements in the integral closure that I'm missing.

The claim is: $\bar{B} = \bigoplus_{n \in \mathbb{Z}} \bar{B}_n$ (graded). This is a standard result. Let me cite it properly.

**Theorem** (see e.g., Bruns-Herzog, or Eisenbud): Let $R = \bigoplus_{n \geq 0} R_n$ be a graded ring (or $\mathbb{Z}$-graded), and let $\bar{R}$ be its integral closure in its total fraction ring. Then $\bar{R}$ is also graded (with the same grading group), and a homogeneous element $f$ of degree $d$ is in $\bar{R}$ iff $f$ is integral over $R$.

For a $\mathbb{Z}$-graded domain $B = \bigoplus_{n \in \mathbb{Z}} B_n$ with fraction field $L$, the integral closure $\bar{B}$ in $L$ is $\mathbb{Z}$-graded, and $\bar{B}_d = \{f \in L_d : f \text{ integral over } B\}$ where $L_d$ is the degree-$d$ part of the "graded fraction field."

But as I noted, the fraction field $K(x)$ doesn't have a natural $\mathbb{Z}$-grading. However, $K[x, x^{-1}]$ does, and $\bar{B} \subset K[x, x^{-1}]$ (since $K[x, x^{-1}]$ is integrally closed). The grading on $K[x, x^{-1}]$ restricts to a grading on $\bar{B}$.

The key fact is: if $f \in K[x, x^{-1}]$ is integral over $B$, then each homogeneous component of $f$ is integral over $B$. This follows from the "graded integral closure" theory.

Proof sketch: Write $f = \sum_{k=a}^{b} f_k x^k$ (finite sum). Suppose $f^N + c_1 f^{N-1} + \cdots + c_N = 0$ with $c_i \in B$. Look at the highest degree term. The degree-$bN$ component gives $f_b^N x^{bN} + (\text{terms from } c_i \text{ of appropriate degree}) = 0$. This gives a monic polynomial for $f_b x^b$ over $B$. Then subtract and proceed by induction.

More carefully: the degree $bN$ component of $f^N$ is $f_b^N x^{bN}$. The degree $bN$ component of $c_i f^{N-i}$ is (the degree $bN - (N-i)b = ib$... hmm, wait, $c_i$ can have various degrees. Let me think again.

Actually, the standard proof uses the following: consider the grading automorphism. For a $\mathbb{Z}$-graded ring, there are automorphisms $\phi_\lambda$ (for $\lambda$ in the base field, if it's a $k$-algebra) that scale the degree-$n$ part by $\lambda^n$. Applying $\phi_\lambda$ to the integral equation gives another integral equation for $\phi_\lambda(f) = \sum f_k \lambda^k x^k$. Since this holds for all $\lambda$, we can extract the homogeneous components.

But this requires $B$ to be a $k$-algebra with $k$ infinite. For general UFDs (not necessarily $k$-algebras), we need a different argument.

Actually, the general result doesn't require a base field. The integral closure of a $\mathbb{Z}$-graded domain in its fraction field is $\mathbb{Z}$-graded. This is proved in, e.g., Bourbaki or Gilmer's book on multiplicative ideal theory. The proof uses the fact that if $f$ is integral over $B$, and we write $f = f_a + f_{a+1} + \cdots + f_b$ (homogeneous decomposition), then $f_a$ (the lowest degree component) is integral over $B$ (by looking at the lowest degree term of the integral equation), and then $f - f_a$ is integral over $B$ (since $f_a \in \bar{B}$ and $f \in \bar{B}$, and $\bar{B}$ is a ring), and proceed by induction.

OK, I'm fairly convinced the argument is correct. Let me also think about whether there's a simpler proof.

**Simpler approach using Serre's criterion:**

$B = A[X,Y]/(XY - a) \cong A[x, ax^{-1}]$. We want to show $B$ is integrally closed (i.e., normal) when $A$ is a UFD.

By Serre's criterion, $B$ is normal iff $R_1$ (regular in codimension 1) and $S_2$.

$S_2$: $B = A[X,Y]/(XY-a)$ is a hypersurface (principal ideal in a polynomial ring), hence a complete intersection, hence Cohen-Macaulay (since $A[X,Y]$ is CM when $A$ is CM, and a quotient by a regular sequence preserves CM). A UFD is CM (it's a domain, and... actually, is a UFD always CM? A UFD is not necessarily CM in general. Hmm.)

Wait, actually, a UFD is not necessarily Cohen-Macaulay. There are UFDs that are not CM. So this approach might not work in full generality.

Hmm, but $S_2$ is weaker than CM. $S_2$ says: $\text{depth}(B_\mathfrak{p}) \geq \min(2, \text{ht}(\mathfrak{p}))$ for all primes $\mathfrak{p}$. 

Actually, let me think about whether $B = A[X,Y]/(XY-a)$ satisfies $S_2$ when $A$ is a UFD.

$B$ is a free $A$-module? No, $B$ is not free over $A$ in general. But $B$ is $A$-flat? $A[X,Y]$ is $A$-flat (free), and $B = A[X,Y]/(XY-a)$. The element $XY - a$ is a non-zero-divisor in $A[X,Y]$ (since $A[X,Y]$ is a domain and $XY - a \neq 0$). So $B$ is $A$-flat (quotient of a flat module by a non-zero-divisor... no, that's not right in general. $A[X,Y]$ is $A$-free, and $B = A[X,Y]/(XY-a)$. The sequence $0 \to A[X,Y] \xrightarrow{\cdot(XY-a)} A[X,Y] \to B \to 0$ is exact. Since $A[X,Y]$ is $A$-free, it's $A$-flat, and tensoring with any $A$-module $M$: $0 \to M[X,Y] \xrightarrow{\cdot(XY-a)} M[X,Y] \to B \otimes_A M \to 0$. This is exact iff $XY - a$ is a non-zero-divisor on $M[X,Y]$, which is true iff $a$ is a non-zero-divisor on $M$ (since $XY - a$ is monic in $X$... hmm, actually $XY - a$ is not monic in $X$ or $Y$).

Hmm, let me think differently. Is $XY - a$ a non-zero-divisor on $M[X,Y]$ for all $A$-modules $M$? If $a = 0$, then $XY - a = XY$, which is a zero-divisor on $M[X,Y]$ if $M \neq 0$ (since $X \cdot Y = XY$ and $X, Y$ are zero-divisors on $k[X,Y]/(XY)$... wait, I mean $XY$ is a zero-divisor in $M[X,Y]$ since $X \cdot (XY) = X^2 Y$ and $Y \cdot (XY) = XY^2$, but $XY$ itself: is $XY$ a zero-divisor? $X \cdot Y \cdot f = XYf$, and if $XYf = 0$ then $f = 0$ (since $M[X,Y]$ is a polynomial ring and $XY$ is not a zero-divisor in $(M[X,Y])$... actually $XY$ could be a zero-divisor if $M$ has torsion).

This is getting complicated. Let me just go with the graded ring argument, which I believe is correct.

Actually, let me also consider the case where $A$ is a UFD but not a $k$-algebra, e.g., $A = \mathbb{Z}$. Take $a = 4$. Then $B = \mathbb{Z}[x, 4/x] = \mathbb{Z}[X,Y]/(XY - 4)$. Is this integrally closed?

$B = \mathbb{Z}[X,Y]/(XY-4)$. Consider the element $2 \in B$. Is $2$ a non-zero-divisor? Yes (since $B$ is a domain). Consider $X/2$ in $\text{Frac}(B)$. $(X/2) \cdot Y = XY/2 = 4/2 = 2 \in B$. And $(X/2)^2 = X^2/4$. Is $X/2$ integral over $B$? $(X/2)^2 = X^2/4$. And $X^2 = X \cdot X$, $XY = 4$, so $X = 4/Y$, $X^2 = 16/Y^2$, $(X/2)^2 = 4/Y^2$. Hmm.

Is $X/2$ integral over $B$? We need a monic polynomial. $(X/2) \cdot Y = 2$, so $X/2 = 2/Y$. And $(2/Y) \cdot X = 2X/Y = 2 \cdot 4/Y^2 = 8/Y^2$... this is getting messy.

Let me use the grading. $B = \bigoplus_{n \geq 0} \mathbb{Z} x^n \oplus \bigoplus_{n > 0} 4^n \mathbb{Z} x^{-n}$. The element $X/2 = x/2$ has degree 1. For degree 1, $\bar{B}_1 = \bar{B} \cap K x$. An element $\alpha x \in \bar{B}_1$ iff $\alpha$ is integral over $A = \mathbb{Z}$ (from the $k \geq 0$ case), so $\alpha \in \mathbb{Z}$. Thus $\bar{B}_1 = \mathbb{Z} x = B_1$, and $x/2 \notin \bar{B}_1$ (since $1/2 \notin \mathbb{Z}$). So $x/2$ is NOT in the integral closure. Good.

What about degree $-1$? $\bar{B}_{-1} = \overline{(4)} \mathbb{Z} \cdot x^{-1}$. $\overline{(4)}$ in $\mathbb{Z}$: $\overline{(4)} = \{n \in \mathbb{Z} : v_2(n) \geq 2, v_p(n) \geq 0 \text{ for } p \neq 2\} = 4\mathbb{Z}$. So $\bar{B}_{-1} = 4\mathbb{Z} x^{-1} = B_{-1}$. ✓.

So $B = \mathbb{Z}[x, 4/x]$ is integrally closed. Makes sense.

Let me also try $A = \mathbb{Z}$, $a = 2$. $B = \mathbb{Z}[x, 2/x]$. $\bar{B}_{-1} = \overline{(2)} x^{-1} = 2\mathbb{Z} x^{-1} = B_{-1}$. ✓. Integrally closed.

OK, I'm now confident the answer is YES.

Let me also think about whether the UFD assumption is necessary, or if integrally closed suffices.

If $A$ is just integrally closed (not UFD), is $A[x, ax^{-1}]$ integrally closed? The argument used: (1) $A$ integrally closed → $\alpha \in A$, (2) $\overline{(a^m)} = (a^m)$ in a UFD. Step (2) uses UFD. In a general integrally closed domain, $\overline{(a^m)}$ might be larger than $(a^m)$.

For example, if $A$ is integrally closed but not a UFD, and $a$ is an element such that $(a^m)$ is not integrally closed as an ideal, then $B$ might not be integrally closed.

But the question only asks about UFDs, so this is fine.

Actually, wait. Let me reconsider step (2) more carefully. In a Krull domain (which includes UFDs), the integral closure of a principal ideal $(b)$ is $\bar{(b)} = \{x \in A : v(x) \geq v(b) \text{ for all essential valuations } v\}$. For a UFD, this equals $(b)$ since $v(x) \geq v(b)$ for all $v$ iff $b | x$ (in a UFD). For a general Krull domain, this might not equal $(b)$.

But actually, in any Krull domain, $\bar{(b)} = (b)$ for principal ideals? No, that's not true. In a Dedekind domain that's not a PID, a principal ideal $(b)$ might have $\bar{(b)} \neq (b)$... actually, in a Dedekind domain, every ideal is integrally closed (since Dedekind domains are Noetherian, integrally closed, and every nonzero ideal factors into primes, and the integral closure of a product of prime ideals is itself). Hmm, actually in a Dedekind domain, $\bar{I} = I$ for all ideals $I$? No, that's not right either.

OK, this is a tangent. The question is about UFDs, and in UFDs, principal ideals are integrally closed (as I showed). So the answer is YES.

Let me now also think about whether there's an issue with $a = 0$ or $a$ being a zero-divisor. In a UFD (which is a domain), $a = 0$ is the only zero-divisor. And $A[x, 0/x] = A[x, 0] = A[x]$, which is a UFD (polynomial ring over UFD is UFD), hence integrally closed. ✓.

So the answer is: **Yes, $A[x, a/x]$ is always integrally closed when $A$ is a UFD.**

Now let me write up a clean proof.

**Proof:**

Let $A$ be a UFD and $a \in A$. We want to show $B = A[x, a/x]$ is integrally closed.

First, note that $B \cong A[X,Y]/(XY - a)$ via $X \mapsto x$, $Y \mapsto a/x$. If $a = 0$, then $B = A[x]$, which is a UFD (polynomial ring over UFD), hence integrally closed. So assume $a \neq 0$.

Since $A$ is a UFD, it is an integrally closed domain. Let $K = \text{Frac}(A)$. Then $B = A[x, ax^{-1}] \subset K[x, x^{-1}]$ (the Laurent polynomial ring). Since $K[x, x^{-1}]$ is a UFD (hence integrally closed), the integral closure $\bar{B}$ of $B$ in $\text{Frac}(B) = K(x)$ satisfies $\bar{B} \subset K[x, x^{-1}]$.

The ring $B$ is $\mathbb{Z}$-graded: $B = \bigoplus_{n \in \mathbb{Z}} B_n$ where $B_n = A x^n$ for $n \geq 0$ and $B_n = a^{|n|} A x^n$ for $n < 0$. (This is because $B$ is generated by $A$ (degree 0), $x$ (degree 1), and $ax^{-1}$ (degree $-1$), and the relation $x \cdot (ax^{-1}) = a$ (degree 0) is consistent.)

Since $B$ is $\mathbb{Z}$-graded and $\bar{B} \subset K[x, x^{-1}]$ (which is also $\mathbb{Z}$-graded), the integral closure $\bar{B}$ is $\mathbb{Z}$-graded: $\bar{B} = \bigoplus_{n \in \mathbb{Z}} \bar{B}_n$ where $\bar{B}_n = \bar{B} \cap K x^n$. (This is a standard result: the integral closure of a graded domain in a graded over-ring is graded.)

We show $\bar{B}_n = B_n$ for all $n$.

**Case $n \geq 0$:** Let $\alpha x^n \in \bar{B}_n$ with $\alpha \in K$. Then $\alpha x^n$ is integral over $B$, so it satisfies a monic polynomial with homogeneous coefficients: $(\alpha x^n)^N + b_1 (\alpha x^n)^{N-1} + \cdots + b_N = 0$ where $b_i \in B_{in}$. For $n \geq 0$, $B_{in} = A x^{in}$, so $b_i = c_i x^{in}$ with $c_i \in A$. Dividing by $x^{nN}$: $\alpha^N + c_1 \alpha^{N-1} + \cdots + c_N = 0$ with $c_i \in A$. So $\alpha$ is integral over $A$. Since $A$ is integrally closed, $\alpha \in A$. Thus $\bar{B}_n = A x^n = B_n$.

**Case $n < 0$, say $n = -m$ with $m > 0$:** Let $\alpha x^{-m} \in \bar{B}_{-m}$ with $\alpha \in K$. Then $\alpha x^{-m}$ satisfies $(\alpha x^{-m})^N + b_1 (\alpha x^{-m})^{N-1} + \cdots + b_N = 0$ with $b_i \in B_{-im} = a^{im} A x^{-im}$. Write $b_i = a^{im} c_i x^{-im}$ with $c_i \in A$. Dividing by $x^{-mN}$: $\alpha^N + a^m c_1 \alpha^{N-1} + a^{2m} c_2 \alpha^{N-2} + \cdots + a^{Nm} c_N = 0$.

Since $a^{im} c_i \in A$ for all $i$, this is a monic polynomial with coefficients in $A$, so $\alpha$ is integral over $A$, hence $\alpha \in A$ (as $A$ is integrally closed).

Now, $\alpha \in A$ satisfies $\alpha^N + j_1 \alpha^{N-1} + \cdots + j_N = 0$ with $j_i = a^{im} c_i \in (a^m)^i$. This means $\alpha$ is in the integral closure of the ideal $(a^m)$ in $A$.

**Claim:** In a UFD, the integral closure of any principal ideal $(b)$ is $(b)$ itself.

*Proof of claim:* In a Krull domain (hence in a UFD), the integral closure of an ideal $I$ is $\bar{I} = \{x \in A : v(x) \geq v(I) \text{ for all essential valuations } v\}$, where $v(I) = \min_{y \in I} v(y)$. For $I = (b)$, $v((b)) = v(b)$ for each valuation $v$. In a UFD, the essential valuations are the $p$-adic valuations $v_p$ for irreducible elements $p$. Writing $b = u \prod p_i^{e_i}$ (unique factorization), $v_{p_i}(b) = e_i$ and $v_q(b) = 0$ for $q \neq p_i$. So $\overline{(b)} = \{x \in A : v_{p_i}(x) \geq e_i \text{ for all } i\} = (b)$. (The last equality uses that in a UFD, $v_p(x) \geq e$ for all $p$ iff $x \in (b)$.)

Applying the claim with $b = a^m$: $\overline{(a^m)} = (a^m)$, so $\alpha \in (a^m) = a^m A$. Thus $\bar{B}_{-m} = a^m A x^{-m} = B_{-m}$.

**Conclusion:** $\bar{B}_n = B_n$ for all $n \in \mathbb{Z}$, so $\bar{B} = B$. Therefore $B = A[x, a/x]$ is integrally closed. $\blacksquare$

Wait, I should also justify the "standard result" that the integral closure of a graded domain is graded. Let me include a brief justification.

Actually, let me also double-check: is the integral closure of an ideal in a Krull domain really given by that valuation formula? Yes, this is a well-known result. In a Krull domain $A$ with essential valuations $\{v_\mathfrak{p}\}_{\mathfrak{p} \in X^{(1)}(A)}$ (valuations associated to height-1 primes), the integral closure of an ideal $I$ is $\bar{I} = \{x \in A : v_\mathfrak{p}(x) \geq v_\mathfrak{p}(I) \text{ for all } \mathfrak{p} \in X^{(1)}(A)\}$ where $v_\mathfrak{p}(I) = \min\{v_\mathfrak{p}(y) : y \in I\}$. This is proved in, e.g., Bourbaki's Commutative Algebra or Swanson-Huneke's "Integral Closure of Ideals, Rings, and Modules."

For a UFD, the height-1 primes are principal ideals $(p)$ for irreducible $p$, and $v_{(p)}$ is the $p$-adic valuation.

I think the proof is complete. Let me also mention that the key ingredients are:
1. $A$ integrally closed (to get $\alpha \in A$ from integrality over $A$).
2. Principal ideals in UFD are integrally closed (to get $\alpha \in (a^m)$ from integrality over $(a^m)$).
3. The graded structure of $B$ and the fact that integral closure preserves grading.

The answer is **Yes**.

Let me write the final clean version.

Actually, one more thing: I should verify that $B$ is indeed a domain (so that "integrally closed" makes sense). $B = A[X,Y]/(XY - a)$. If $a \neq 0$, is $XY - a$ irreducible (hence prime, since $A[X,Y]$ is a UFD)? $XY - a$ is linear in $X$ (and in $Y$), so it's irreducible in $A[X,Y]$ (as a polynomial of degree 1 in $X$ over $A[Y]$, it's irreducible iff it has no root in $\text{Frac}(A[Y])$, i.e., $a/Y \notin A[Y]$... actually, a degree-1 polynomial is always irreducible). More precisely, $XY - a$ is degree 1 in $X$ over $A[Y]$, and a degree-1 polynomial over any domain is irreducible. So $XY - a$ is irreducible in $A[Y][X] = A[X,Y]$, hence prime (since $A[X,Y]$ is a UFD), so $B$ is a domain. ✓.

(If $a = 0$, $B = A[X,Y]/(XY) = A[x]$, which is a domain since $A$ is. Wait, $A[X,Y]/(XY) \neq A[x]$. $A[X,Y]/(XY)$ is not a domain! But $A[x, 0/x] = A[x, 0] = A[x]$, which is a domain. The issue is that $A[X,Y]/(XY - 0) = A[X,Y]/(XY)$ is NOT isomorphic to $A[x]$ when $a = 0$.

Hmm, let me reconsider. $A[x, a/x]$ with $a = 0$: this is $A[x, 0 \cdot x^{-1}] = A[x, 0] = A[x]$. But $A[X,Y]/(XY - 0) = A[X,Y]/(XY) \
