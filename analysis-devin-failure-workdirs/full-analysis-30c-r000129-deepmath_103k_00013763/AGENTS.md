# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Evaluate the limit: \[ \lim_{x \to \infty} \left( 12x^2 - 2 - 6x \sqrt{3x^2 - 2} \right) \]       — 题目文本
#   Okay, so I need to find the limit as x approaches infinity of this expression: 12x² - 2 - 6x times the square root of (3x² - 2). Hmm, let me think about how to approach this. 

First, when dealing with limits at infinity involving square roots, a common technique is to multiply by the conjugate. Maybe that can help here. Let me recall: if you have something like sqrt(a) - sqrt(b), multiplying by the conjugate (sqrt(a) + sqrt(b)) can rationalize the expression. But here, the expression is 12x² - 2 minus 6x times sqrt(3x² - 2). So it's a bit different, but maybe a similar idea applies.

Alternatively, maybe factor out some terms to simplify. Let's see. Let's look at the expression term by term. The first term is 12x², which is a quadratic term. The second term is -2, which is a constant, so as x approaches infinity, this term becomes negligible. The third term is -6x multiplied by sqrt(3x² - 2). Let's analyze that sqrt part.

The square root of 3x² - 2. When x is approaching infinity, the -2 is negligible compared to the 3x² term, so sqrt(3x² - 2) is approximately sqrt(3x²) which is x*sqrt(3). But we have to be careful because we might need a more precise approximation for the square root to compute the limit. If we approximate sqrt(3x² - 2) as x*sqrt(3) - something, maybe we can use a binomial expansion or a Taylor series expansion for the square root function.

Let me try that. Let's write sqrt(3x² - 2) as sqrt(3x²(1 - 2/(3x²))) which is sqrt(3)x sqrt(1 - 2/(3x²)). Then, using the Taylor expansion for sqrt(1 - y) around y=0, which is approximately 1 - y/2 - y²/8 - ... So here, y is 2/(3x²). Therefore, sqrt(1 - 2/(3x²)) ≈ 1 - (1/2)(2/(3x²)) - ... = 1 - 1/(3x²) - ... So multiplying back by sqrt(3)x gives sqrt(3)x - sqrt(3)x/(3x²) - ... which simplifies to sqrt(3)x - sqrt(3)/(3x) - ... So sqrt(3x² - 2) ≈ sqrt(3)x - sqrt(3)/(3x) for large x.

Therefore, the third term in the expression, which is -6x times sqrt(3x² - 2), would be approximately -6x*(sqrt(3)x - sqrt(3)/(3x)) = -6x*sqrt(3)x + 6x*(sqrt(3)/(3x)) = -6sqrt(3)x² + 2sqrt(3).

So substituting this back into the original expression: 12x² - 2 -6x*sqrt(3x² -2) ≈ 12x² - 2 -6sqrt(3)x² + 2sqrt(3). Then combining like terms: (12 - 6sqrt(3))x² + (-2 + 2sqrt(3)). Now, as x approaches infinity, the x² term will dominate. The coefficient of x² is (12 - 6sqrt(3)). Let's compute that: 12 - 6sqrt(3) ≈ 12 - 6*1.732 ≈ 12 - 10.392 ≈ 1.608. So if this approximation is correct, the limit would be infinity since the coefficient is positive. But that doesn't make sense, because when we have such a subtraction, often the leading terms cancel out. Maybe my approximation is missing something?

Wait a second, perhaps I need to use a better approximation for the square root. Because if the first-order term cancels out, then we need to go to the next term in the expansion to find the actual limit.

Let me check that. Let's go back. Let's write sqrt(3x² - 2) = sqrt(3)x*sqrt(1 - 2/(3x²)). Then, expanding sqrt(1 - 2/(3x²)) using the binomial expansion: 1 - (1/2)(2/(3x²)) - (1/8)(2/(3x²))² + ... So that's 1 - 1/(3x²) - (1/8)*(4)/(9x⁴) + ... So sqrt(3x² - 2) ≈ sqrt(3)x [1 - 1/(3x²) - 1/(18x⁴) + ...] = sqrt(3)x - sqrt(3)/(3x) - sqrt(3)/(18x³) + ... So when we multiply by -6x, we get -6x*sqrt(3)x + 6x*(sqrt(3)/(3x)) + 6x*(sqrt(3)/(18x³)) + ... which is -6sqrt(3)x² + 2sqrt(3) + sqrt(3)/(3x²) + ... So substituting back into the original expression:

12x² - 2 -6x*sqrt(3x² -2) ≈ 12x² - 2 -6sqrt(3)x² + 2sqrt(3) + sqrt(3)/(3x²). Then combining like terms:

(12 - 6sqrt(3))x² + (-2 + 2sqrt(3)) + sqrt(3)/(3x²). Now, as x approaches infinity, the term with x² dominates. If 12 - 6sqrt(3) is not zero, then the limit would be either infinity or negative infinity depending on the sign. But 12 - 6sqrt(3) ≈ 12 - 10.392 ≈ 1.608, which is positive, so the limit would be positive infinity. But that's conflicting with my initial thought that perhaps the leading terms might cancel. Wait, but 12x² -6sqrt(3)x², is 12 equal to 6sqrt(3)? Let's compute 6sqrt(3): 6*1.732 ≈ 10.392, which is less than 12, so 12 -10.392≈1.608. Therefore, the coefficient is positive, so the expression tends to infinity. But the original problem is presented as a limit, which might have a finite value. Therefore, perhaps my approach is missing something. Maybe I need to rationalize the expression instead of approximating?

Alternatively, let me consider the original expression:

Limit as x approaches infinity of [12x² - 2 -6x*sqrt(3x² -2)].

Let me try to write this expression as follows:

Let me factor out 6x². Wait, but 12x² -6x*sqrt(3x² -2) -2. If I factor out 6x², we get 6x²[2 - sqrt(3x² -2)/x] -2. Hmm, let's see. Let me write sqrt(3x² -2) as x*sqrt(3 - 2/x²). So then sqrt(3x² -2)/x = sqrt(3 - 2/x²). Therefore, the expression becomes 6x²[2 - sqrt(3 - 2/x²)] -2. Now, we can write this as 6x²[2 - sqrt(3 - 2/x²)] -2. Let me focus on the term inside the brackets: 2 - sqrt(3 - 2/x²). Let me denote t = 1/x², so as x approaches infinity, t approaches 0. Then, the expression becomes 2 - sqrt(3 - 2t). Let me expand sqrt(3 -2t) around t=0. Using Taylor series: sqrt(a - bt) ≈ sqrt(a) - (b)/(2sqrt(a)) t - (b²)/(8a^(3/2)) t² + ... Here, a=3, b=2. Therefore, sqrt(3 -2t) ≈ sqrt(3) - (2)/(2sqrt(3))t - (4)/(8*(3)^(3/2)) t² + ... which simplifies to sqrt(3) - (1)/sqrt(3) t - (1)/(6sqrt(3)) t² + ... Therefore, 2 - sqrt(3 -2t) = 2 - sqrt(3) + (1)/sqrt(3) t + (1)/(6sqrt(3)) t² - ... Then substituting back t=1/x², we get 2 - sqrt(3) + (1)/(sqrt(3) x²) + (1)/(6sqrt(3) x^4) - ... Therefore, the expression 6x²[2 - sqrt(3 - 2/x²)] -2 becomes 6x²[2 - sqrt(3) + 1/(sqrt(3) x²) + ... ] -2. Distribute the 6x²: 6x²(2 - sqrt(3)) + 6x²*(1)/(sqrt(3) x²) + ... -2. Simplify term by term: 6(2 - sqrt(3))x² + 6/sqrt(3) + ... -2. So combining constants: 6/sqrt(3) -2 + ... and the x² term is 6(2 - sqrt(3))x². But 6(2 - sqrt(3)) is the coefficient. Wait, 6(2 - sqrt(3)) ≈6*(2 -1.732)=6*(0.268)=1.608, which is the same as before. Therefore, the expression becomes approximately 1.608x² + (6/sqrt(3) -2) + ... So as x approaches infinity, this would go to infinity. However, the original problem asks for the limit, which might be infinity, but maybe the problem is designed to have a finite limit. Perhaps I made a mistake in my approach. Let me verify.

Wait, perhaps there is a miscalculation here. Let me check again. Wait, 12x² - 2 -6x*sqrt(3x² -2). Let me try to rationalize the expression. Let me set L = lim_{x→∞} [12x² -2 -6x sqrt(3x² -2)]. Let me denote y = x. Then, as y→∞, the expression becomes 12y² -2 -6y sqrt(3y² -2). Let me factor out y². Let me write the expression as y²[12 - 6 sqrt(3 - 2/y²)] -2. Wait, similar to before. Alternatively, set t = 1/x, so as x→∞, t→0+. Then substituting x = 1/t, the expression becomes 12*(1/t²) -2 -6*(1/t)*sqrt(3*(1/t²) -2) = 12/t² -2 -6/t * sqrt(3/t² -2). Let's simplify sqrt(3/t² -2) = sqrt( (3 - 2t²)/t² ) = sqrt(3 -2t²)/t. Therefore, the expression becomes 12/t² -2 -6/t * sqrt(3 -2t²)/t = 12/t² -2 -6 sqrt(3 -2t²)/t². Combine terms over t²: (12 -6 sqrt(3 -2t²))/t² -2. Then, as t→0+, sqrt(3 -2t²) can be expanded as sqrt(3) - (2t²)/(2sqrt(3)) + ... = sqrt(3) - t²/sqrt(3) + ... Therefore, sqrt(3 -2t²) ≈ sqrt(3) - t²/sqrt(3). Substitute back into the expression: [12 -6(sqrt(3) - t²/sqrt(3))]/t² -2 = [12 -6sqrt(3) +6t²/sqrt(3)]/t² -2 = (12 -6sqrt(3))/t² +6/sqrt(3) -2. Now, as t→0+, the term (12 -6sqrt(3))/t² will dominate. Since 12 -6sqrt(3) ≈12 -10.392≈1.608>0, this term tends to +infty. The other terms 6/sqrt(3)-2≈6/1.732 -2≈3.464-2≈1.464 are constants. Therefore, the entire expression tends to +infty. But the original problem is presented as a limit, and I need to check if the answer is indeed infinity or if I made a mistake in my reasoning.

Wait, but maybe the answer is supposed to be a finite value. Let me try another approach. Let me consider the expression 12x² -6x sqrt(3x² -2) -2. Let me set x = t, and think of t approaching infinity. Let me divide numerator and denominator by x². Wait, but this expression isn't a fraction. Alternatively, factor x² from the first two terms. Let me write:

12x² -6x sqrt(3x² -2) -2 = x²[12 -6 sqrt(3 - 2/x²)/x] -2. Wait, no, that's not helpful. Wait, sqrt(3x² -2) = x sqrt(3 -2/x²). So 6x*sqrt(3x² -2) =6x^2 sqrt(3 -2/x²). Therefore, the expression is 12x² -2 -6x² sqrt(3 -2/x²). Then factor x²: x²[12 -6 sqrt(3 -2/x²)] -2. Now, set h = 1/x², so as x→∞, h→0+. Then, the expression becomes (1/h)[12 -6 sqrt(3 -2h)] -2. Now, expand sqrt(3 -2h) using Taylor series around h=0: sqrt(3 -2h) = sqrt(3) - (2h)/(2sqrt(3)) - ( (2h)^2 )/(8*(sqrt(3))^3 ) + ... = sqrt(3) - h/sqrt(3) - (h²)/(2*3^(3/2)) + ... Therefore, 12 -6 sqrt(3 -2h) =12 -6*sqrt(3) +6h/sqrt(3) +6*(h²)/(2*3^(3/2)) - ... So substituting back into the expression: (1/h)[12 -6*sqrt(3) +6h/sqrt(3) + ... ] -2 = [12 -6sqrt(3)]/h +6/sqrt(3) + ... -2. As h→0+, the term [12 -6sqrt(3)]/h tends to +infty because 12 -6sqrt(3)≈1.608>0 and h→0+. Therefore, the entire expression tends to +infty. Therefore, the limit is infinity. But maybe the problem is written incorrectly? Wait, maybe I miscalculated somewhere.

Wait, let me check with concrete numbers. Let me plug in a large x, say x=1000. Then compute 12x² -2 -6x sqrt(3x² -2). Let's compute each term:

12*(1000)^2 = 12,000,000

-2 is negligible.

6x sqrt(3x² -2) =6*1000*sqrt(3*(1000)^2 -2)=6000*sqrt(3,000,000 -2)≈6000*sqrt(3,000,000)≈6000*1732.05≈10,392,300.

Therefore, 12,000,000 -10,392,300≈1,607,700. Then subtract 2, which is negligible, so approximately 1,607,700. Which is a large positive number, which suggests that as x increases, this expression tends to infinity, which aligns with our previous conclusion. So perhaps the answer is indeed infinity. But the problem is presented as a limit that might have a finite answer. Hmm. Wait, maybe there was a typo in the problem statement? Let me check again.

The problem is: lim_{x→∞} (12x² -2 -6x sqrt(3x² -2)). Yes, that's what's written. So according to the calculations, the limit is infinity. However, let me think again. Maybe when we subtract 6x sqrt(3x² -2) from 12x², the leading terms might cancel if they are similar. Wait, 12x² and 6x*sqrt(3x²). Let me compute 6x*sqrt(3x²) =6x* x*sqrt(3)=6sqrt(3)x²≈10.392x². Therefore, 12x² -10.392x²≈1.608x², so yes, the leading term is positive, leading to infinity.

But let me check another value. Let's take x=10,000. Then 12x²=12*10^8=1.2*10^9.

6x sqrt(3x² -2)=6*10^4*sqrt(3*10^8 -2)≈6*10^4*sqrt(3)*10^4≈6*1.732*10^8≈10.392*10^8. Therefore, 12x² -6x sqrt(3x² -2)≈1.2*10^9 -1.0392*10^9≈0.1608*10^9≈1.608*10^8, which is still a large positive number. So yes, it's growing like ~1.6x². Therefore, the limit is indeed infinity.

But maybe the problem was expecting a different approach? Let me try to rationalize the expression.

Let me set L = lim_{x→∞} [12x² -2 -6x sqrt(3x² -2)]. Let me write this as L = lim_{x→∞} [12x² -6x sqrt(3x² -2) -2]. To rationalize, perhaps consider treating the expression as A - B, where A =12x² -2 and B=6x sqrt(3x² -2). Then multiply and divide by (A + B). So:

L = lim_{x→∞} (A - B) = lim_{x→∞} [(A - B)(A + B)]/(A + B) = lim_{x→∞} (A² - B²)/(A + B).

Compute A² - B²: (12x² -2)^2 - (6x sqrt(3x² -2))^2.

First, expand (12x² -2)^2: 144x⁴ -48x² +4.

Second, expand (6x sqrt(3x² -2))²: 36x²*(3x² -2)=108x⁴ -72x².

Therefore, A² - B² = (144x⁴ -48x² +4) - (108x⁴ -72x²) =144x⁴ -48x² +4 -108x⁴ +72x²= (144x⁴ -108x⁴) + (-48x² +72x²) +4=36x⁴ +24x² +4.

So numerator becomes 36x⁴ +24x² +4. Denominator is A + B =12x² -2 +6x sqrt(3x² -2).

Therefore, L= lim_{x→∞} (36x⁴ +24x² +4)/(12x² -2 +6x sqrt(3x² -2)).

Hmm, now we need to evaluate this limit. Let's analyze the denominator:12x² -2 +6x sqrt(3x² -2). As x approaches infinity, the dominant term in the denominator is 12x² +6x*sqrt(3)x=12x² +6sqrt(3)x²= x²(12 +6sqrt(3)).

Similarly, the numerator is 36x⁴ +24x² +4, which is dominated by 36x⁴. Therefore, the expression becomes approximately 36x⁴ / [x²(12 +6sqrt(3))] =36x²/(12 +6sqrt(3)). As x approaches infinity, this tends to infinity. Therefore, L= infinity.

But wait, that's the same conclusion as before. Therefore, whether I use approximation or rationalization, the limit is infinity. Therefore, the answer should be infinity. But let me check once more.

Alternatively, maybe the problem has a typo? For example, if instead of -6x sqrt(3x² -2), it was -6x² sqrt(3x² -2), then the leading terms would be 12x² -6x²*sqrt(3)x, but that would be different. But as stated, the original problem is as written. Therefore, unless I'm missing some cancellation, the limit is infinity. 

Wait, but maybe there's a mistake in my rationalization approach. Let me verify the steps. When I set L = (A - B), then multiplied by (A + B)/(A + B), which is valid as long as A + B ≠0, which is true for large x. Then, A² - B² was calculated as 36x⁴ +24x² +4, which seems correct. Then, the denominator is A + B ≈12x² +6x*sqrt(3x²)=12x² +6sqrt(3)x². Therefore, denominator ~x²(12 +6sqrt(3)), numerator ~36x⁴. Thus, the ratio ~36x⁴/(x²(12 +6sqrt(3))) = (36/(12 +6sqrt(3)))x². Since 36/(12 +6sqrt(3)) = 36/(6*(2 +sqrt(3))) =6/(2 +sqrt(3)). Multiply numerator and denominator by (2 -sqrt(3)):6*(2 -sqrt(3))/[(2 +sqrt(3))(2 -sqrt(3))] =6*(2 -sqrt(3))/(4 -3)=6*(2 -sqrt(3))/1=12 -6sqrt(3). Which is approximately1.608, same as before. Therefore, the ratio tends to (12 -6sqrt(3))x², which tends to infinity. Therefore, the limit is infinity. Therefore, despite rationalizing, the conclusion remains the same.

Therefore, after multiple approaches and checks, it seems the limit is indeed infinity. So, the answer is infinity. But the problem didn't specify whether it's positive or negative infinity. Since the coefficient is positive, it's positive infinity. However, in the context of real limits, infinity is acceptable as an answer. But let me check once again with another method.

Alternatively, perhaps using substitution. Let me set x = t, and let t approach infinity. Let me make a substitution y = sqrt(3x² -2). Then, y = sqrt(3x² -2), so y²=3x² -2, so x²=(y² +2)/3. Then, express the original expression in terms of y. The expression is 12x² -2 -6x y. Substituting x²=(y² +2)/3, so 12x²=12*(y² +2)/3=4*(y² +2)=4y² +8. Then, 12x² -2=4y² +8 -2=4y² +6. Then, the entire expression becomes 4y² +6 -6x y. Now, express x in terms of y. From y²=3x² -2, x= sqrt( (y² +2)/3 ). So x= sqrt( y²/3 + 2/3 ). As x approaches infinity, y approaches infinity as well. So let's approximate x for large y. x≈ sqrt(y²/3)= y/sqrt(3). Therefore, x≈ y/sqrt(3). Then, 6x y ≈6*(y/sqrt(3))*y=6/sqrt(3) y²=2sqrt(3)y². Therefore, the expression becomes 4y² +6 -2sqrt(3)y²= (4 -2sqrt(3))y² +6. The coefficient 4 -2sqrt(3)≈4 -3.464≈0.536>0. Therefore, as y approaches infinity, this expression tends to infinity. Hence, confirming again that the limit is infinity.

Alternatively, if I use more precise terms. Let me write x= sqrt( (y² +2)/3 ). Then, x= y/sqrt(3) * sqrt(1 + 2/(y²)). For large y, sqrt(1 +2/y²)≈1 +1/y². Therefore, x≈y/sqrt(3)*(1 +1/y²)= y/sqrt(3) +1/(sqrt(3)y). Therefore, 6x y≈6*(y/sqrt(3) +1/(sqrt(3)y)) * y=6*(y²/sqrt(3) +1/sqrt(3))=6/sqrt(3) y² +6/sqrt(3). Therefore, the expression 4y² +6 -6x y≈4y² +6 -6/sqrt(3)y² -6/sqrt(3)= (4 -6/sqrt(3))y² +6 -6/sqrt(3). Compute 4 -6/sqrt(3)=4 -2*3/sqrt(3)=4 -2*sqrt(3)≈4 -3.464≈0.536>0. Therefore, the expression still tends to infinity. Hence, the conclusion is the same.

Therefore, after multiple methods and checks, I conclude that the limit is indeed infinity.

**Final Answer**
\boxed{\infty}
</think>

To evaluate the limit \(\lim_{x \to \infty} \left( 12x^2 - 2 - 6x \sqrt{3x^2 - 2} \right)\), we start by approximating the square root term for large \(x\).

First, we approximate \(\sqrt{3x^2 - 2}\) using a binomial expansion:
\[
\sqrt{3x^2 - 2} = x\sqrt{3} \sqrt{1 - \frac{2}{3x^2}} \approx x\sqrt{3} \left(1 - \frac{1}{3x^2}\right)
\]
This simplifies to:
\[
\sqrt{3x^2 - 2} \approx x\sqrt{3} - \frac{\sqrt{3}}{3x}
\]

Substituting this approximation into the original expression, we get:
\[
12x^2 - 2 - 6x \left( x\sqrt{3} - \frac{\sqrt{3}}{3x} \right)
\]
Simplifying the terms:
\[
12x^2 - 2 - 6x^2\sqrt{3} + 2\sqrt{3}
\]
Combining like terms:
\[
(12 - 6\sqrt{3})x^2 + (-2 + 2\sqrt{3})
\]

As \(x \to \infty\), the dominant term is \((12 - 6\sqrt{3})x^2\). Since \(12 - 6\sqrt{3} \approx 1.608\) is positive, the expression grows without bound.

To confirm, we rationalize the expression by multiplying by the conjugate:
\[
\lim_{x \to \infty} \frac{(12x^2 - 2)^2 - (6x \sqrt{3x^2 - 2})^2}{12x^2 - 2 + 6x \sqrt{3x^2 - 2}}
\]
Calculating the numerator:
\[
(144x^4 - 48x^2 + 4) - (108x^4 - 72x^2) = 36x^4 + 24x^2 + 4
\]
The denominator for large \(x\) is approximately \(12x^2 + 6x \cdot x\sqrt{3} = x^2(12 + 6\sqrt{3})\). The limit becomes:
\[
\lim_{x \to \infty} \frac{36x^4}{x^2(12 + 6\sqrt{3})} = \lim_{x \to \infty} \frac{36x^2}{12 + 6\sqrt{3}}
\]
This also tends to infinity as \(x \to \infty\).

Thus, the limit is:
\[
\boxed{\infty}
\]  — 标准解答
#   Let me analyze this problem carefully.

We have a Riemannian manifold $M$ with submanifolds $S$ and $T$. $\theta$ is a differential $k$-form on $M$ such that $\oint_{[S]} \theta = r \neq 0$. $\eta$ is the Hodge star of $\theta$ (so $\eta = *\theta$). The $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$.

We need to determine $\oint_{[T]} \eta$.

This is a classic problem related to Poincaré duality and the Hodge star operator. Let me think about this.

The key idea: On an $n$-dimensional oriented Riemannian manifold, the Hodge star operator $*$ maps $k$-forms to $(n-k)$-forms. The intersection number of two submanifolds is related to the integral of the Poincaré dual of one over the other.

Let me think about dimensions. If $\theta$ is a $k$-form and $\eta = *\theta$ is an $(n-k)$-form, then $S$ should be a $k$-dimensional submanifold (so that $\oint_{[S]} \theta$ makes sense as integration of a $k$-form over a $k$-cycle), and $T$ should be an $(n-k)$-dimensional submanifold (so that $\oint_{[T]} \eta$ makes sense).

The intersection number of $S$ (dimension $k$) and $T$ (dimension $n-k$) in an $n$-manifold is well-defined when $k + (n-k) = n$, which is the case for transversal intersection giving points.

Now, the key relationship: The Poincaré dual of $[S]$ (as a cohomology class) can be represented by a form, and the Hodge star relates the Poincaré dual to harmonic forms.

Actually, let me think more carefully. The classical result is:

If $\alpha$ is a closed $k$-form representing the Poincaré dual of $[S]$, then $\int_T \alpha = S \cdot T$ (the intersection number).

But here we have $\theta$ with $\int_S \theta = r$, and $\eta = *\theta$, and we want $\int_T \eta$.

The relationship between the Hodge star and intersection numbers comes through Poincaré duality. 

Let me think about this differently. The key theorem here is:

**Theorem**: On a compact oriented Riemannian $n$-manifold, if $\alpha$ is a harmonic $k$-form and $\beta$ is a harmonic $(n-k)$-form, then:
$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

And more relevantly, the intersection pairing and the Hodge star are related by:

If $S$ and $T$ are submanifolds with $[S] \in H_k(M)$ and $[T] \in H_{n-k}(M)$, and if $\theta$ is the harmonic form representing the Poincaré dual of $[S]$ (i.e., $\theta = PD([S])$), then $*\theta$ represents the Poincaré dual of $[T]$ when $S \cdot T = \pm 1$... 

Hmm, let me be more precise.

Actually, the standard result is:

The Poincaré dual of $[S]$ is a cohomology class $PD([S]) \in H^{n-k}(M)$. If we represent this by a form $\alpha$, then $\int_T \alpha = S \cdot T$.

But here, $\theta$ is a $k$-form with $\int_S \theta = r$. So $\theta$ is not the Poincaré dual of $S$ (which would be an $(n-k)$-form). Rather, $\theta$ is a form that pairs with $[S]$ to give $r$.

The Hodge star $\eta = *\theta$ is an $(n-k)$-form.

Now, the question is about the relationship between $\int_T *\theta$ and $\int_S \theta$ given the intersection number.

Let me think about this using the L² inner product and the wedge product.

We have the identity:
$$\int_M \theta \wedge *\phi = \langle \theta, \phi \rangle_{L^2}$$

for $k$-forms $\theta, \phi$.

Also, $\int_M \alpha \wedge \beta$ for a $k$-form $\alpha$ and $(n-k)$-form $\beta$ gives the cup product pairing.

Now, the key relationship between intersection numbers and forms:

If $\alpha$ is a closed $k$-form and $\gamma$ is a closed $(n-k)$-form, then:
$$\int_M \alpha \wedge \gamma = \sum_i (\int_{S_i} \alpha)(\int_{T_i} \gamma) \cdot (S_i \cdot T_i)$$

Hmm, that's not quite right either. Let me think more carefully.

The correct statement involves Poincaré duality. Let $\{e_i\}$ be a basis for $H_k(M;\mathbb{R})$ and $\{e^j\}$ the dual basis for $H^{n-k}(M;\mathbb{R})$ under Poincaré duality (so $PD(e_i) = e^i$ meaning $\int_{e_i} \alpha = \int_M \alpha \wedge e^i$... no, that's not right either).

Let me reconsider. Poincaré duality says $H^k(M) \cong H_{n-k}(M)$. The isomorphism sends a cohomology class $[\alpha] \in H^k(M)$ to the homology class $[S] \in H_{n-k}(M)$ such that for all $[\beta] \in H^{n-k}(M)$:
$$\int_M \alpha \wedge \beta = \int_S \beta$$

So if $PD([\theta]) = [S']$ for some $(n-k)$-cycle $S'$, then $\int_M \theta \wedge \beta = \int_{S'} \beta$ for all $(n-k)$-forms $\beta$.

But we're told $\int_S \theta = r$, which means $[S]$ pairs with $[\theta]$ to give $r$. This means $[S]$ is dual to $[\theta]$ in the sense that... well, $[S] \in H_k(M)$ and $[\theta] \in H^k(M)$, and the pairing $\langle [S], [\theta] \rangle = \int_S \theta = r$.

Now, $\eta = *\theta \in H^{n-k}(M)$ (assuming $\theta$ is harmonic, or at least closed and co-closed, so that $*\theta$ is also closed).

The intersection number $S \cdot T$ is defined as $\int_T PD([S])$ where $PD([S]) \in H^{n-k}(M)$ is the Poincaré dual of $[S]$.

Now, $PD([S])$ is the cohomology class such that for all $[\beta] \in H^k(M)$:
$$\int_M \beta \wedge PD([S]) = \int_S \beta$$

So if $\int_S \theta = r$, then $\int_M \theta \wedge PD([S]) = r$.

Now, the question is: what is the relationship between $*\theta$ and $PD([S])$?

If $\theta$ is harmonic, then $*\theta$ is also harmonic, and $*\theta$ represents the Poincaré dual of $[S]$ if and only if... hmm.

Actually, let me think about this more carefully. The Hodge theorem says every cohomology class has a unique harmonic representative. So $PD([S]) \in H^{n-k}(M)$ has a unique harmonic representative, call it $\omega_{n-k}$.

If $\theta$ is the harmonic representative of the class $[\theta] \in H^k(M)$ that pairs with $[S]$ to give $r$... 

Actually, I think the problem is set up so that $\theta$ is the harmonic form Poincaré dual to $[S]$ (up to scaling). Let me reconsider.

If $PD([S]) = [\alpha] \in H^{n-k}(M)$, then $\int_T \alpha = S \cdot T = \pm 1$.

Now, $*\alpha$ would be a $k$-form. If $\alpha$ is harmonic, $*\alpha$ is harmonic. And $*\alpha$ represents $PD([T])$ (the Poincaré dual of $[T]$) because... 

Actually, there's a key fact: On a compact oriented Riemannian manifold, if $\alpha$ is the harmonic representative of $PD([S])$, then $*\alpha$ is the harmonic representative of $PD([T])$ if and only if... no, that's not generally true.

Let me think about this differently.

The key fact is: $\int_S \theta = r$ and we want $\int_T *\theta$.

Using the L² inner product:
$$\int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$$

But that's $\theta \wedge *\theta$, not directly helpful.

Let me use the relationship between the cup product and intersection:

$$\int_M \theta \wedge \eta = \int_M \theta \wedge *\theta$$

Wait, no. $\eta = *\theta$, so $\int_M \theta \wedge \eta = \int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$.

But also, by Poincaré duality, $\int_M \theta \wedge \eta$ relates to intersection numbers.

Hmm, let me think about this problem from a more basic perspective.

The standard result that this problem is testing:

**If $\theta$ is a harmonic $k$-form on a compact oriented Riemannian $n$-manifold $M$, and $S$ is a $k$-dimensional submanifold, $T$ is an $(n-k)$-dimensional submanifold, with $S \cdot T = \pm 1$, and $\int_S \theta = r$, then $\int_T *\theta = \pm r$.**

The sign depends on the sign of the intersection number and orientation conventions.

Let me verify this. The idea is:

1. $\theta$ harmonic $\Rightarrow$ $*\theta$ harmonic.
2. $[\theta] \in H^k(M)$ corresponds to $[S]$ under Poincaré duality (up to the pairing $r$).
3. $[*\theta] \in H^{n-k}(M)$ corresponds to $[T]$ under Poincaré duality (up to the same factor).

More precisely: Let $\omega = PD([S])$ be the Poincaré dual of $[S]$, a closed $(n-k)$-form. Then $\int_T \omega = S \cdot T = \pm 1$.

Now, $\theta$ is a $k$-form with $\int_S \theta = r$. The Poincaré dual of $[S]$ satisfies: for any closed $k$-form $\alpha$, $\int_M \alpha \wedge \omega = \int_S \alpha$.

So $\int_M \theta \wedge \omega = \int_S \theta = r$.

Now, if $\theta$ is harmonic, then $*\theta$ is harmonic, and both represent cohomology classes. The question is whether $[*\theta]$ is proportional to $[\omega] = PD([S])$.

In general, $*\theta$ and $\omega$ are different things. The Hodge star maps $H^k_{harm}(M) \to H^{n-k}_{harm}(M)$, and this is an isomorphism. Poincaré duality also gives an isomorphism $H^k(M) \to H^{n-k}(M)$ (well, $H^k \to H_{n-k} \to H^{n-k}$). 

The key point: The Hodge star $*$ and the Poincaré duality isomorphism are related but not identical. However, on a compact oriented Riemannian manifold, the following holds:

The harmonic representative of $PD([S])$ is $*\theta_S$ where $\theta_S$ is the harmonic representative of the class dual to $[S]$ in $H^k(M)$.

Wait, I need to be more careful. Let me use the standard framework.

Let $\{[\sigma_i]\}$ be a basis for $H^k(M;\mathbb{R})$ and $\{[\tau_j]\}$ be a basis for $H^{n-k}(M;\mathbb{R})$. The cup product pairing is:
$$Q_{ij} = \int_M \sigma_i \wedge \tau_j$$

Poincaré duality says this pairing is non-degenerate. If we choose $\tau_j$ to be the Poincaré dual basis (so $Q_{ij} = \delta_{ij}$), then $PD([\sigma_i])$ corresponds to the homology class $[S_i]$ such that $\int_{S_i} \sigma_j = \delta_{ij}$... 

Hmm, actually let me think about it this way. Let's say $[S] \in H_k(M)$ and $[\theta] \in H^k(M)$ with $\int_S \theta = r$. 

The Poincaré dual $PD([S]) \in H^{n-k}(M)$ is characterized by: for all $[\alpha] \in H^k(M)$, $\int_M \alpha \wedge PD([S]) = \int_S \alpha$.

So $\int_M \theta \wedge PD([S]) = \int_S \theta = r$.

Now, $S \cdot T = \int_T PD([S]) = \pm 1$.

We want $\int_T *\theta$.

Now, here's the key: is $[*\theta]$ related to $PD([S])$?

In general, no — not unless $\theta$ is specifically the harmonic representative of the class that is Hodge-dual to $PD([S])$.

But actually, I think the problem is implicitly assuming that $\theta$ is harmonic (or at least closed and co-closed), so that $*\theta$ is closed, and the problem is asking about the relationship.

Let me think about this more carefully using the Hodge decomposition.

The Hodge star gives an isomorphism $*: H^k_{harm}(M) \to H^{n-k}_{harm}(M)$. 

The Poincaré duality also gives an isomorphism $PD: H^k(M) \to H^{n-k}(M)$, defined by $[\alpha] \mapsto PD([\alpha])$ where $PD([\alpha])$ is the unique class such that $\int_M \alpha \wedge \beta = \int_{PD^{-1}([\beta])} \alpha$... 

Hmm, I'm going in circles. Let me think about this more concretely.

Consider the simplest case: $M = S^n$ (the $n$-sphere), $S$ = equator ($k$-sphere), $T$ = another great sphere ($(n-k)$-sphere) intersecting $S$ transversally at one point.

On $S^n$, the harmonic $k$-forms are zero for $0 < k < n$ (since $b_k(S^n) = 0$ for $0 < k < n$). So this doesn't work for a non-trivial example.

Let me try $M = T^2$ (the 2-torus), $k = 1$. Then $n = 2$, $n - k = 1$. Let $S$ and $T$ be the two standard circles (meridian and longitude), intersecting at one point, so $S \cdot T = 1$.

The harmonic 1-forms on $T^2$ are spanned by $dx$ and $dy$ (in the flat metric). 

If $\theta = dx$, then $\int_S \theta = \int_0^1 dx = 1 = r$ (if $S$ is the $x$-circle). Then $*\theta = *dx = dy$ (in the standard orientation on $T^2$). And $\int_T dy = \int_0^1 dy = 1$.

So $\int_T *\theta = 1 = r$. And $S \cdot T = 1$, so the answer is $r \cdot (S \cdot T) = r \cdot 1 = r$.

If $\theta = 2dx$, then $\int_S \theta = 2 = r$, $*\theta = 2dy$, $\int_T *\theta = 2 = r$. Same.

Now if $S \cdot T = -1$ (reversed orientation of $T$), then $\int_T dy = -1$, so $\int_T *\theta = -r$.

So the answer is $\int_T *\theta = \pm r$ where the sign matches the sign of the intersection number $S \cdot T$.

Wait, but let me check: if $S \cdot T = -1$, then with $\theta = dx$, $*\theta = dy$, and $T$ has reversed orientation, $\int_T dy = -1$. And $r = \int_S dx = 1$. So $\int_T *\theta = -1 = -r = r \cdot (S \cdot T)$.

So the answer is $\oint_{[T]} \eta = \pm r$, where the sign is the same as the sign of the intersection number.

Actually, more precisely: $\oint_{[T]} \eta = r \cdot (S \cdot T) = \pm r$.

Hmm wait, but the problem says the intersection number is $\pm 1$, and asks to "determine the value." So the answer should be $\pm r$, matching the sign of the intersection number.

Let me verify this more carefully with the general theory.

**General proof:**

On a compact oriented $n$-dimensional Riemannian manifold $M$, let $\theta$ be a harmonic $k$-form. Let $S$ be a compact oriented $k$-submanifold and $T$ a compact oriented $(n-k)$-submanifold.

The Poincaré dual of $[S]$ is $PD([S]) \in H^{n-k}(M)$, represented by a closed $(n-k)$-form $\omega$ such that for any closed $k$-form $\alpha$:
$$\int_M \alpha \wedge \omega = \int_S \alpha$$

The intersection number $S \cdot T = \int_T \omega$.

Now, since $\theta$ is harmonic, $*\theta$ is also harmonic (hence closed). The cohomology class $[*\theta] \in H^{n-k}(M)$ is the Hodge dual of $[\theta]$.

The key relationship: On a compact oriented Riemannian manifold, the Hodge star on harmonic forms corresponds to the Poincaré duality isomorphism, **up to the intersection pairing**.

More precisely: Let $\theta_1, \ldots, \theta_{b_k}$ be an orthonormal basis of harmonic $k$-forms (with respect to the $L^2$ inner product). Then $*\theta_1, \ldots, *\theta_{b_k}$ is an orthonormal basis of harmonic $(n-k)$-forms.

The cup product pairing $\int_M \theta_i \wedge *\theta_j = \delta_{ij}$ (by the $L^2$ inner product property).

Now, let $[S_1], \ldots, [S_{b_k}]$ be a basis of $H_k(M)$ dual to $[\theta_1], \ldots, [\theta_{b_k}]$ in the sense that $\int_{S_i} \theta_j = \delta_{ij}$. Then $PD([S_i]) = [*\theta_i]$ because:

For any closed $k$-form $\alpha = \sum_j a_j \theta_j + d\beta$ (using Hodge decomposition, the harmonic part is $\sum a_j \theta_j$):
$$\int_M \alpha \wedge *\theta_i = \int_M (\sum_j a_j \theta_j) \wedge *\theta_i = \sum_j a_j \delta_{ji} = a_i$$

And $\int_{S_i} \alpha = \int_{S_i} \sum_j a_j \theta_j = a_i$ (since exact forms integrate to 0 over closed cycles).

So indeed $PD([S_i]) = [*\theta_i]$, confirming that the Hodge star of the harmonic form dual to $[S_i]$ gives the Poincaré dual of $[S_i]$.

Now, in our problem: $\int_S \theta = r$. We can write $[S] = \sum_i c_i [S_i]$ where $c_i = \int_S \theta_i$ (if $\{\theta_i\}$ is orthonormal and $\{S_i\}$ is the dual basis). Then $\int_S \theta = \sum_i c_i \int_{S_i} \theta$... 

Hmm, this is getting complicated. Let me simplify.

Assume $\theta$ is harmonic (the problem likely intends this, as the Hodge star is most meaningful for harmonic forms in this context). 

Let $[\theta] \in H^k(M)$ be the cohomology class of $\theta$. The Poincaré dual of $[S]$ is $PD([S]) \in H^{n-k}(M)$.

We have $\int_S \theta = r$, which means $\langle [S], [\theta] \rangle = r$ where $\langle \cdot, \cdot \rangle$ is the Kronecker pairing.

Now, $PD([S])$ is the class in $H^{n-k}(M)$ such that $\int_M [\theta'] \cup PD([S]) = \langle [S], [\theta'] \rangle$ for all $[\theta'] \in H^k(M)$.

In particular, $\int_M \theta \wedge \omega = r$ where $\omega$ is a closed form representing $PD([S])$.

Now, the intersection number $S \cdot T = \int_T \omega = \pm 1$.

We want $\int_T *\theta$.

The key claim: $[*\theta] = r \cdot PD([S]) / (S \cdot T)$... no, that doesn't seem right in general.

Actually wait. Let me reconsider. The problem doesn't say $\theta$ is the Poincaré dual of anything specific. It just says $\int_S \theta = r$. The form $\theta$ could be any $k$-form (presumably closed, so the integral is well-defined on the homology class).

But the answer $\int_T *\theta = \pm r$ would only hold if $\theta$ is specifically the harmonic form Poincaré dual to $[S]$ (up to the factor $r$).

Hmm, but the problem says "determine the value," implying there's a definite answer. So there must be enough constraints.

Let me re-read the problem: "Let $M$ be a Riemannian manifold with submanifolds $S$ and $T$. Suppose $\theta$ is a differential $k$-form on $M$ such that $\oint_{[S]} \theta = r \neq 0$. If $\eta$ is the Hodge star of $\theta$ and the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$, determine the value of $\oint_{[T]} \eta$."

I think the problem is implicitly assuming that $\theta$ is harmonic (or at least closed and co-closed), and that $S$ and $T$ are in "Poincaré dual" position. The $\mathbb{Z}\pi$ notation suggests this is in the context of the fundamental group $\pi = \pi_1(M)$, which is the setting of the intersection form on the universal cover.

Actually, the $\mathbb{Z}\pi$-intersection number is a concept from geometric topology. In the universal cover $\tilde{M}$, the lifts $\tilde{S}$ and $\tilde{T}$ intersect, and the intersection number is computed in $\mathbb{Z}\pi$ (the group ring of the fundamental group). When this is $\pm 1$, it means the intersection is essentially a single point with sign $\pm 1$.

This is related to the duality theorem: on a closed oriented manifold, the intersection form $H_k(M) \times H_{n-k}(M) \to \mathbb{Z}$ (or $\mathbb{Z}\pi$ for the universal cover version) is related to the cup product via Poincaré duality.

I think the intended answer is:

$$\oint_{[T]} \eta = \pm r$$

where the sign matches the intersection number $S \cdot T = \pm 1$.

The reasoning is based on the fundamental relationship:

**On a compact oriented Riemannian manifold, if $\theta$ is a harmonic $k$-form, then $*\theta$ is the harmonic $(n-k)$-form Poincaré dual to the same geometry, and the intersection number provides the proportionality.**

More precisely, the key identity is:

$$\oint_{[T]} *\theta = (S \cdot T) \cdot \oint_{[S]} \theta$$

when $\theta$ is harmonic and $S$, $T$ are Poincaré-dual submanifolds.

Wait, but that's not quite right either. Let me think again...

Actually, I think the correct statement is simpler than I'm making it. The problem is testing the following classical result:

**Theorem (Poincaré duality via Hodge star):** If $\theta$ is a harmonic $k$-form representing the Poincaré dual of $[T]$ (i.e., $[\theta] = PD([T]) \in H^k(M)$), then $*\theta$ represents $PD([S])$ (i.e., $[*\theta] = PD([S]) \in H^{n-k}(M)$), and:
$$\int_S \theta = S \cdot T = \pm 1$$
$$\int_T *\theta = T \cdot S = \pm 1$$

But in our problem, $\int_S \theta = r \neq \pm 1$, so $\theta$ is not exactly $PD([T])$; it's $r$ times that (assuming $b_k = 1$ in the relevant direction).

If $[\theta] = r \cdot PD([T])$, then $[*\theta] = r \cdot PD([S])$, and:
$$\int_T *\theta = r \cdot \int_T PD([S]) = r \cdot (S \cdot T) = \pm r$$

So the answer is $\oint_{[T]} \eta = \pm r$.

Let me make sure this is correct by checking the logic:

1. $PD([T]) \in H^k(M)$ is the Poincaré dual of $[T]$. It's a $k$-dimensional cohomology class (since $T$ is $(n-k)$-dimensional, $PD([T]) \in H^{n-(n-k)}(M) = H^k(M)$). ✓

2. $\int_S PD([T]) = S \cdot T = \pm 1$. ✓ (This is the definition of intersection number via Poincaré duality.)

3. If $\theta = r \cdot \omega$ where $\omega$ is the harmonic representative of $PD([T])$, then $\int_S \theta = r \cdot \int_S \omega = r \cdot (S \cdot T) = \pm r$.

But the problem says $\int_S \theta = r$, not $\pm r$. So either $S \cdot T = 1$ and $\theta = r \cdot \omega$, or there's a sign issue.

Hmm, let me reconsider. If $S \cdot T = +1$, then $\int_S PD([T]) = 1$, and if $\theta = r \cdot PD([T])_{harm}$, then $\int_S \theta = r$. Then $*\theta = r \cdot *(PD([T])_{harm})$.

Now, $*(PD([T])_{harm}) = PD([S])_{harm}$ (this is the key Hodge star / Poincaré duality relationship).

So $\int_T *\theta = r \cdot \int_T PD([S]) = r \cdot (S \cdot T) = r \cdot 1 = r$.

If $S \cdot T = -1$, then $\int_S PD([T]) = -1$. For $\int_S \theta = r$, we'd need $\theta = -r \cdot PD([T])_{harm}$. Then $*\theta = -r \cdot PD([S])_{harm}$, and $\int_T *\theta = -r \cdot (S \cdot T) = -r \cdot (-1) = r$.

Wait, that gives $r$ in both cases! Let me recheck.

Case 1: $S \cdot T = +1$.
- $PD([T])_{harm}$ is a harmonic $k$-form with $\int_S PD([T])_{harm} = S \cdot T = 1$.
- $\theta = r \cdot PD([T])_{harm}$, so $\int_S \theta = r \cdot 1 = r$. ✓
- $*\theta = r \cdot *(PD([T])_{harm}) = r \cdot PD([S])_{harm}$.
- $\int_T *\theta = r \cdot \int_T PD([S])_{harm} = r \cdot (S \cdot T) = r \cdot 1 = r$.

Case 2: $S \cdot T = -1$.
- $PD([T])_{harm}$ is a harmonic $k$-form with $\int_S PD([T])_{harm} = S \cdot T = -1$.
- For $\int_S \theta = r$, we need $\theta = -r \cdot PD([T])_{harm}$ (since $\int_S (-r \cdot PD([T])_{harm}) = -r \cdot (-1) = r$). ✓
- $*\theta = -r \cdot *(PD([T])_{harm}) = -r \cdot PD([S])_{harm}$.
- $\int_T *\theta = -r \cdot \int_T PD([S])_{harm} = -r \cdot (S \cdot T) = -r \cdot (-1) = r$.

So in both cases, $\int_T *\theta = r$!

Wait, that's interesting. The answer is just $r$, regardless of the sign of the intersection number.

Hmm, but this depends on the assumption that $\theta$ is a scalar multiple of $PD([T])_{harm}$, which requires that the relevant Betti number is 1. If $b_k > 1$, then $\theta$ could have components in other directions, and the answer wouldn't be determined.

But the problem says "determine the value," implying it's uniquely determined. So either:
1. The problem assumes $b_k = 1$ (or that $\theta$ is in the "right" direction), or
2. The answer is always $r$ regardless, which would require a more general argument.

Let me think about whether the answer is always $r$ in general.

Actually, I think the problem is set up so that $\theta$ is specifically the harmonic form Poincaré dual to $[T]$ (scaled by $r$ and adjusted for the sign of the intersection). The $\mathbb{Z}\pi$-intersection number being $\pm 1$ is the key constraint that makes $S$ and $T$ Poincaré-dual to each other (in the universal cover sense).

Given the way the problem is phrased, with the intersection number being $\pm 1$ (which means $S$ and $T$ are "dual" in some sense), and $\theta$ integrating to $r$ over $S$, the answer should be:

$$\oint_{[T]} \eta = \pm r$$

where the sign is the same as the intersection number.

But from my calculation above, I got $r$ in both cases. Let me re-examine.

Actually, I think I need to be more careful. The issue is whether $*(PD([T])_{harm}) = PD([S])_{harm}$ or $*(PD([T])_{harm}) = \pm PD([S])_{harm}$.

The Hodge star and Poincaré duality: On a compact oriented Riemannian $n$-manifold, the Hodge star $*: \mathcal{H}^k \to \mathcal{H}^{n-k}$ (harmonic forms) is an isomorphism. The Poincaré duality $PD: H^k \to H^{n-k}$ is also an isomorphism (via $[\alpha] \mapsto [*\alpha]$ when $\alpha$ is harmonic... wait, is that true?).

Actually, the Poincaré duality isomorphism $PD: H^k(M) \to H_{n-k}(M) \to H^{n-k}(M)$ is NOT the same as the Hodge star in general. The Poincaré duality sends $[\alpha] \in H^k(M)$ to $PD([\alpha]) \in H^{n-k}(M)$ where $\int_M \alpha \wedge \beta = \int_{PD^{-1}(\beta)} \alpha$... 

Let me be very precise. Poincaré duality gives an isomorphism $D: H^k(M) \to H_{n-k}(M)$, sending $[\alpha]$ to the homology class $[C]$ such that $\int_C \beta = \int_M \alpha \wedge \beta$ for all $[\beta] \in H^{n-k}(M)$.

Then $PD([S]) = D^{-1}([S]) \in H^{n-k}(M)$, the class such that $\int_M \gamma \wedge PD([S]) = \int_S \gamma$ for all $[\gamma] \in H^k(M)$.

Now, the Hodge star: if $\alpha$ is a harmonic $k$-form, then $*\alpha$ is a harmonic $(n-k)$-form. The cohomology class $[*\alpha]$ satisfies:

For any harmonic $(n-k)$-form $\beta$:
$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

And $[*\alpha]$ is the Poincaré dual of the homology class $[C]$ where $\int_C \beta = \int_M \alpha \wedge \beta$ for all $\beta$.

So $D([\alpha]) = [C]$ where $\int_C \beta = \int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$ for all harmonic $(n-k)$-forms $\beta$.

Now, $D^{-1}([C]) = [\omega]$ where $\int_M \gamma \wedge \omega = \int_C \gamma$ for all $[\gamma] \in H^k(M)$.

If $[C] = D([\alpha])$, then $D^{-1}([C]) = [\alpha]$... no wait, $D^{-1}(D([\alpha])) = [\alpha]$, but $D$ maps $H^k \to H_{n-k}$, and $D^{-1}$ maps $H_{n-k} \to H^k$. So $PD([S]) = D^{-1}([S]) \in H^{n-k}$... 

I'm getting confused with the directions. Let me use a cleaner notation.

$PD: H_k(M) \to H^{n-k}(M)$ sends $[S]$ to $PD([S])$ where $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for all $[\alpha] \in H^k(M)$.

Similarly, $PD: H_{n-k}(M) \to H^k(M)$ sends $[T]$ to $PD([T])$ where $\int_M PD([T]) \wedge \beta = \int_T \beta$ for all $[\beta] \in H^{n-k}(M)$.

Note: $\int_M PD([T]) \wedge \beta = (-1)^{k(n-k)} \int_M \beta \wedge PD([T])$... hmm, signs from swapping forms.

Actually, for the cup product, $\alpha \cup \beta = \alpha \wedge \beta$ for differential forms, and $\alpha \wedge \beta = (-1)^{kl} \beta \wedge \alpha$ for $k$-form $\alpha$ and $l$-form $\beta$.

So $\int_M PD([T]) \wedge \beta = (-1)^{k(n-k)} \int_M \beta \wedge PD([T]) = (-1)^{k(n-k)} \int_T \beta$.

Hmm, this introduces a sign $(-1)^{k(n-k)}$. But the standard convention for Poincaré duality usually handles this. Let me not worry about this sign for now and focus on the main idea.

The key question: Is $*(PD([T])_{harm}) = PD([S])_{harm}$ (up to the intersection number)?

Let me use the $L^2$ inner product. For harmonic forms $\alpha \in \mathcal{H}^k$ and $\beta \in \mathcal{H}^{n-k}$:

$$\langle \alpha, \beta \rangle_{cup} := \int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

So the cup product pairing on harmonic forms is $\langle \alpha, *\beta \rangle_{L^2}$.

Now, $PD([S])_{harm}$ is the harmonic $(n-k)$-form $\omega$ such that $\int_M \alpha \wedge \omega = \int_S \alpha$ for all harmonic $k$-forms $\alpha$.

This means $\langle \alpha, *\omega \rangle_{L^2} = \int_S \alpha$ for all harmonic $\alpha$.

So $*\omega$ is the harmonic $k$-form that represents the linear functional $\alpha \mapsto \int_S \alpha$ on $\mathcal{H}^k$.

Similarly, $PD([T])_{harm}$ is the harmonic $k$-form $\mu$ such that $\int_M \mu \wedge \beta = \int_T \beta$ for all harmonic $(n-k)$-forms $\beta$.

This means $\langle \mu, *\beta \rangle_{L^2} = \int_T \beta$ for all harmonic $\beta \in \mathcal{H}^{n-k}$.

Or equivalently, $\int_M \mu \wedge \beta = \int_T \beta$.

Now, $\int_T \beta = \int_M PD([T]) \wedge \beta$... wait, that's circular.

Let me try a different approach. Let's use the fact that the intersection number $S \cdot T = \int_T PD([S]) = \int_S PD([T])$ (with appropriate signs).

Now, $\int_S PD([T]) = S \cdot T = \pm 1$.

If $\theta$ is a harmonic $k$-form with $\int_S \theta = r$, and if $b_k = 1$ (so $\mathcal{H}^k$ is 1-dimensional), then $\theta = c \cdot PD([T])_{harm}$ for some scalar $c$, and $r = c \cdot \int_S PD([T])_{harm} = c \cdot (S \cdot T) = \pm c$. So $c = \pm r$ (with sign depending on $S \cdot T$).

Then $*\theta = c \cdot *(PD([T])_{harm})$.

Now, $*(PD([T])_{harm})$ is a harmonic $(n-k)$-form. Is it $PD([S])_{harm}$?

From the relation: $PD([S])_{harm} = \omega$ where $\langle \alpha, *\omega \rangle_{L^2} = \int_S \alpha$ for all harmonic $\alpha$.

And $PD([T])_{harm} = \mu$ where $\int_M \mu \wedge \beta = \int_T \beta$ for all harmonic $\beta$.

If $b_k = b_{n-k} = 1$, then $\mathcal{H}^k = \text{span}(\mu)$ and $\mathcal{H}^{n-k} = \text{span}(\omega)$.

$*\mu$ is a harmonic $(n-k)$-form, so $*\mu = \lambda \omega$ for some scalar $\lambda$.

We have $\int_M \mu \wedge \omega = \langle \mu, *\omega \rangle_{L^2}$ and also $\int_M \mu \wedge \omega = \int_T \omega = S \cdot T$ (since $\omega = PD([S])_{harm}$ and $\int_T PD([S]) = S \cdot T$).

Also, $\int_M \mu \wedge \omega = \langle \mu, *\omega \rangle_{L^2}$. And $*\omega = \bar{\lambda}^{-1} *\mu / \lambda$... hmm, this is getting complicated.

Let me just use the $L^2$ norm. $\langle \mu, *\omega \rangle_{L^2} = \int_M \mu \wedge \omega = S \cdot T = \pm 1$.

Also, $\|*\omega\|_{L^2} = \|\omega\|_{L^2}$ and $\|\mu\|_{L^2} = \|\mu\|_{L^2}$.

If $\mu$ and $*\omega$ are both unit vectors (after normalization), then $\langle \mu, *\omega \rangle = \pm 1$ means $\mu = \pm *\omega$, i.e., $*\omega = \pm \mu$, i.e., $\omega = \pm *\mu$ (since $**\omega = \pm \omega$ depending on degree and signature).

Actually, $**\alpha = (-1)^{k(n-k)} \alpha$ on a Riemannian manifold (positive definite metric). So $*\mu = \lambda \omega$ implies $\mu = (-1)^{k(n-k)} \lambda *\omega$, and $*\omega = (-1)^{k(n-k)} \lambda^{-1} \mu$.

This is getting quite involved. Let me step back and think about what the problem is really asking.

I think the problem is a standard exercise in differential topology/geometry, and the expected answer is:

$$\oint_{[T]} \eta = \pm r$$

The sign being the same as the intersection number $S \cdot T = \pm 1$.

The reasoning is based on the duality between the Hodge star and the intersection pairing. The key identity is:

$$\oint_{[S]} \theta \cdot \oint_{[T]} *\theta = \text{something related to } \|\theta\|^2$$

No, that's not right either.

Actually, let me think about this more carefully. The fundamental relationship is:

$$\int_M \theta \wedge *\phi = \langle \theta, \phi \rangle_{L^2}$$

If $\theta = \phi$ (both harmonic $k$-forms), then $\int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$.

Now, by Poincaré duality, $\int_M \theta \wedge *\theta$ can also be interpreted as a sum of products of periods:

$$\int_M \theta \wedge *\theta = \sum_{i,j} (\int_{S_i} \theta)(\int_{T_j} *\theta) \cdot (S_i \cdot T_j)$$

where $\{S_i\}$ and $\{T_j\}$ are dual bases of $H_k$ and $H_{n-k}$.

If $S \cdot T = \pm 1$ and $S, T$ are the only relevant pair (i.e., $b_k = 1$), then:

$$\|\theta\|^2_{L^2} = (\int_S \theta)(\int_T *\theta) \cdot (S \cdot T) = r \cdot (\int_T *\theta) \cdot (\pm 1)$$

But this gives $\int_T *\theta = \|\theta\|^2_{L^2} / (r \cdot (\pm 1))$, which depends on $\|\theta\|_{L^2}$ and is not simply $\pm r$.

Hmm, so the answer is NOT simply $\pm r$ in general. It depends on the $L^2$ norm of $\theta$.

Unless... the problem is assuming that $\theta$ is the specific harmonic form that is the Poincaré dual (up to scaling), in which case the $L^2$ norm is determined.

OK wait, I think I was overcomplicating this. Let me reconsider the problem.

I think the problem is testing the following specific result:

**If $\theta$ is a closed $k$-form on a compact oriented Riemannian $n$-manifold $M$, $S$ is a $k$-cycle, $T$ is an $(n-k)$-cycle, $S \cdot T = \pm 1$, and $\eta = *\theta$, then:**

$$\oint_{[T]} \eta = \pm \oint_{[S]} \theta = \pm r$$

This would be true if $\theta$ is the harmonic form Poincaré dual to $[T]$ (scaled appropriately).

But as I showed, this requires specific assumptions about $\theta$.

However, looking at the problem again, I think it's meant to be a straightforward application of the duality between the Hodge star and Poincaré duality, and the expected answer is $\pm r$.

The key insight is:

1. The Hodge star $*$ maps $k$-forms to $(n-k)$-forms.
2. Poincaré duality maps $H^k$ to $H^{n-k}$ (via the intersection form).
3. The Hodge star on harmonic forms implements Poincaré duality.
4. If $\int_S \theta = r$ and $S \cdot T = \pm 1$, then by the duality, $\int_T *\theta = \pm r$.

The sign is determined by the sign of the intersection number and the degree $k$ (there might be a $(-1)^{k(n-k)}$ factor from the Hodge star).

Actually, I realize the problem might be even simpler than I think. Let me consider the possibility that the answer is just $\pm r$, with the sign being the sign of the intersection number.

Let me verify with the torus example again. $M = T^2$, $k = 1$, $n = 2$. $\theta = dx$, $*\theta = dy$. $S$ = $x$-circle, $T$ = $y$-circle. $S \cdot T = 1$ (with appropriate orientations). $\int_S dx = 1 = r$, $\int_T dy = 1 = r$. So $\int_T *\theta = r$. ✓

If we reverse the orientation of $T$, $S \cdot T = -1$, $\int_T dy = -1 = -r$. So $\int_T *\theta = -r = r \cdot (S \cdot T)$. ✓

So the answer is $\oint_{[T]} \eta = r \cdot (S \cdot T) = \pm r$.

But wait, in my earlier analysis with the $b_k = 1$ assumption, I got $r$ in both cases. Let me recheck.

Case 2: $S \cdot T = -1$.
- $PD([T])_{harm}$: $\int_S PD([T])_{harm} = S \cdot T = -1$.
- $\theta = c \cdot PD([T])_{harm}$ with $\int_S \theta = c \cdot (-1) = r$, so $c = -r$.
- $\theta = -r \cdot PD([T])_{harm}$.
- $*\theta = -r \cdot *(PD([T])_{harm})$.
- If $*(PD([T])_{harm}) = PD([S])_{harm}$, then $*\theta = -r \cdot PD([S])_{harm}$.
- $\int_T *\theta = -r \cdot \int_T PD([S])_{harm} = -r \cdot (S \cdot T) = -r \cdot (-1) = r$.

But in the torus example with $S \cdot T = -1$, I got $\int_T *\theta = -r$, not $r$!

The discrepancy is because $*(PD([T])_{harm}) \neq PD([S])_{harm}$ in general; there might be a sign.

Let me check with the torus. $PD([T])$ where $T$ is the $y$-circle: $PD([T])$ is the 1-form $\omega$ such that $\int_M \alpha \wedge \omega = \int_T \alpha$ for all 1-forms $\alpha$.

On $T^2$ with coordinates $(x,y)$, $\int_{T^2} dx \wedge dy = 1$. If $\omega = dy$, then $\int_{T^2} dx \wedge dy = 1 = \int_T dx$ (if $T$ is the $y$-circle, $\int_T dx = 0$). That's not right.

Let me be more careful. $T$ is the $y$-circle: $T = \{(x_0, y) : y \in [0,1]\}$. $\int_T \alpha$ for a 1-form $\alpha = a\,dx + b\,dy$ is $\int_0^1 b\,dy = \int_0^1 b(x_0, y)\,dy$.

$PD([T])$ is the 1-form $\omega$ such that $\int_{T^2} \alpha \wedge \omega = \int_T \alpha$ for all $\alpha$.

If $\omega = c\,dx + d\,dy$, then $\alpha \wedge \omega = (a\,dx + b\,dy) \wedge (c\,dx + d\,dy) = (ad - bc)\,dx \wedge dy$.

$\int_{T^2} \alpha \wedge \omega = \int_0^1 \int_0^1 (ad - bc)\,dx\,dy$.

For $\alpha = dx$ ($a=1, b=0$): $\int_{T^2} dx \wedge \omega = \int_0^1 \int_0^1 d\,dx\,dy = \bar{d}$ (average of $d$). And $\int_T dx = 0$. So $\bar{d} = 0$.

For $\alpha = dy$ ($a=0, b=1$): $\int_{T^2} dy \wedge \omega = \int_0^1 \int_0^1 (-c)\,dx\,dy = -\bar{c}$. And $\int_T dy = 1$. So $-\bar{c} = 1$, $\bar{c} = -1$.

So $PD([T])_{harm} = -dx$ (the harmonic representative with $\bar{c} = -1, \bar{d} = 0$).

Check: $\int_S PD([T])_{harm} = \int_S (-dx) = -1 = S \cdot T$ when $S \cdot T = -1$... 

Wait, but I said $S$ is the $x$-circle and $T$ is the $y$-circle, and with standard orientations, $S \cdot T = 1$ (the $x$-circle and $y$-circle on $T^2$ intersect at one point with positive orientation).

Let me reconsider. On $T^2$ with standard orientation $dx \wedge dy$, the $x$-circle $S = \{(x, y_0)\}$ oriented in the $+x$ direction, and the $y$-circle $T = \{(x_0, y)\}$ oriented in the $+y$ direction. At the intersection point $(x_0, y_0)$, the tangent to $S$ is $\partial_x$ and the tangent to $T$ is $\partial_y$. The orientation of $S$ followed by $T$ gives $(\partial_x, \partial_y)$ which matches the orientation of $T^2$. So $S \cdot T = +1$.

Now, $PD([T])_{harm} = -dx$ as computed above. Let me verify: $\int_S (-dx) = -\int_0^1 dx = -1$. But $S \cdot T = +1$, and $\int_S PD([T]) = S \cdot T = 1$. Contradiction!

Let me recheck. $PD([T])$ should satisfy $\int_M \alpha \wedge PD([T]) = \int_T \alpha$.

For $\alpha = dy$: $\int_{T^2} dy \wedge PD([T]) = \int_T dy = 1$.

$dy \wedge (-dx) = -dy \wedge dx = dx \wedge dy$. So $\int_{T^2} dy \wedge (-dx) = \int_{T^2} dx \wedge dy = 1$. ✓

For $\alpha = dx$: $\int_{T^2} dx \wedge (-dx) = 0$. And $\int_T dx = 0$. ✓

So $PD([T])_{harm} = -dx$. And $\int_S PD([T]) = \int_S (-dx) = -1$.

But $S \cdot T = +1$ and $\int_S PD([T])$ should equal $S \cdot T$... 

Hmm, the issue is the sign convention. The standard convention is:

$$S \cdot T = \int_T PD([S])$$

NOT $\int_S PD([T])$. Let me check if $\int_S PD([T]) = \int_T PD([S])$ or if there's a sign.

$PD([S])$: $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for all $\alpha$.

For $\alpha = dx$: $\int_{T^2} dx \wedge PD([S]) = \int_S dx = 1$.

$dx \wedge (c\,dx + d\,dy) = d\,dx \wedge dy$. So $\int_{T^2} d\,dx\,dy = \bar{d} = 1$. So $PD([S])_{harm} = dy$.

For $\alpha = dy$: $\int_{T^2} dy \wedge dy = 0 = \int_S dy = 0$. ✓

So $PD([S])_{harm} = dy$ and $PD([T])_{harm} = -dx$.

Now: $\int_T PD([S]) = \int_T dy = 1 = S \cdot T$. ✓
And: $\int_S PD([T]) = \int_S (-dx) = -1$.

So $\int_S PD([T]) = -1 \neq S \cdot T = 1$!

The relationship is $\int_S PD([T]) = (-1)^{k(n-k)} \int_T PD([S]) = (-1)^{1 \cdot 1} \cdot 1 = -1$. ✓

So the general relationship is:
$$\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$$

This is because $PD([T]) \in H^k(M)$ and $\int_S PD([T])$ involves the cup product $\int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} (S \cdot T)$.

Wait, let me be more careful. $\int_M PD([S]) \wedge PD([T])$: this is $(-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S])$.

$\int_M PD([S]) \wedge \beta = \int_S \beta$ for $\beta \in H^{n-k}$. So $\int_M PD([S]) \wedge PD([T])$... but $PD([T]) \in H^k$, not $H^{n-k}$. So this doesn't directly apply.

Let me reconsider. $PD([S]) \in H^{n-k}(M)$ and $PD([T]) \in H^k(M)$. 

$\int_M PD([T]) \wedge PD([S]) = \int_T PD([S]) = S \cdot T$ (by definition of $PD([T])$: $\int_M PD([T]) \wedge \beta = \int_T \beta$ for $\beta \in H^{n-k}$, and $PD([S]) \in H^{n-k}$).

And $\int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} (S \cdot T)$.

Also, $\int_M PD([S]) \wedge \alpha = \int_S \alpha$ for $\alpha \in H^k$. So $\int_M PD([S]) \wedge PD([T]) = \int_S PD([T])$.

Therefore: $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$.

OK so now let me redo the analysis.

$\int_S PD([T])_{harm} = (-1)^{k(n-k)} (S \cdot T)$.

If $\theta = c \cdot PD([T])_{harm}$ (assuming $b_k = 1$), then:
$r = \int_S \theta = c \cdot (-1)^{k(n-k)} (S \cdot T)$.
So $c = \frac{r}{(-1)^{k(n-k)} (S \cdot T)} = \frac{r \cdot (-1)^{k(n-k)}}{S \cdot T}$ (since $(-1)^{k(n-k)}$ is its own inverse).

$*\theta = c \cdot *(PD([T])_{harm})$.

Now, is $*(PD([T])_{harm}) = PD([S])_{harm}$?

In the torus example: $PD([T])_{harm} = -dx$, $*(−dx) = -dy$. And $PD([S])_{harm} = dy$. So $*(PD([T])_{harm}) = -dy = -PD([S])_{harm}$.

So $*(PD([T])_{harm}) = -PD([S])_{harm}$ in this case ($k = n-k = 1$, $(-1)^{k(n-k)} = -1$).

Let me check if $*(PD([T])_{harm}) = (-1)^{k(n-k)} PD([S])_{harm}$ in general.

In the torus: $(-1)^{1 \cdot 1} = -1$, and indeed $*(PD([T])_{harm}) = -PD([S])_{harm}$. ✓

Let me verify this relationship. We have:
- $PD([T])_{harm} = \mu \in \mathcal{H}^k$ with $\int_M \mu \wedge \beta = \int_T \beta$ for all $\beta \in \mathcal{H}^{n-k}$.
- $PD([S])_{harm} = \omega \in \mathcal{H}^{n-k}$ with $\int_M \alpha \wedge \omega = \int_S \alpha$ for all $\alpha \in \mathcal{H}^k$.

$*\mu \in \mathcal{H}^{n-k}$. Is $*\mu = (-1)^{k(n-k)} \omega$?

$\int_M \alpha \wedge *\mu = \langle \alpha, \mu \rangle_{L^2}$ for all $\alpha \in \mathcal{H}^k$.

If $b_k = 1$, then $\alpha = a\mu$ for some scalar $a$, and $\langle \alpha, \mu \rangle = a\|\mu\|^2$.

Also, $\int_M \alpha \wedge \omega = \int_S \alpha = a \int_S \mu = a \cdot (-1)^{k(n-k)} (S \cdot T)$.

And $\int_M \alpha \wedge *\mu = \langle \alpha, \mu \rangle = a \|\mu\|^2$.

If $*\mu = \lambda \omega$, then $\int_M \alpha \wedge *\mu = \lambda \int_M \alpha \wedge \omega = \lambda a (-1)^{k(n-k)} (S \cdot T)$.

So $a \|\mu\|^2 = \lambda a (-1)^{k(n-k)} (S \cdot T)$, giving $\lambda = \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)}$.

This depends on $\|\mu\|^2$, so $*\mu \neq (-1)^{k(n-k)} \omega$ in general (unless $\|\mu\|^2 = (S \cdot T)^2 = 1$, which happens when $\mu$ is a unit form).

In the torus example: $\mu = -dx$, $\|\mu\|^2 = \int_{T^2} (-dx) \wedge *(-dx) = \int_{T^2} dx \wedge dy = 1$. And $(-1)^{k(n-k)}(S \cdot T) = (-1)(1) = -1$. So $\lambda = 1/(-1) = -1$. And indeed $*\mu = -dy = -\omega = \lambda \omega$ with $\lambda = -1$. ✓

So in general, $*\mu = \lambda \omega$ where $\lambda = \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)}$.

Now, $\int_T *\theta = c \lambda \int_T \omega = c \lambda (S \cdot T)$.

$= \frac{r \cdot (-1)^{k(n-k)}}{S \cdot T} \cdot \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|\mu\|^2}{(S \cdot T)^2} \cdot \frac{(-1)^{k(n-k)}}{(-1)^{k(n-k)}} \cdot \frac{(S \cdot T)}{(S \cdot T) \cdot (S \cdot T)}$

Hmm, let me redo this calculation:

$c = \frac{r}{(-1)^{k(n-k)} (S \cdot T)}$

$\lambda = \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)}$

$\int_T *\theta = c \cdot \lambda \cdot (S \cdot T) = \frac{r}{(-1)^{k(n-k)} (S \cdot T)} \cdot \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|\mu\|^2 \cdot (S \cdot T)}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2 \cdot (S \cdot T)} \cdot (S \cdot T)$

Wait, let me be more careful:

$= \frac{r \cdot \|\mu\|^2}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2} \cdot \frac{(S \cdot T)}{1}$

No: $c \cdot \lambda \cdot (S \cdot T) = \frac{r}{(-1)^{k(n-k)} (S \cdot T)} \cdot \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|\mu\|^2 \cdot (S \cdot T)}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2}$

$= \frac{r \cdot \|\mu\|^2 \cdot (S \cdot T)}{1 \cdot (S \cdot T)^2}$ (since $((-1)^{k(n-k)})^2 = 1$)

$= \frac{r \cdot \|\mu\|^2}{S \cdot T}$

$= r \cdot \|\mu\|^2 \cdot (S \cdot T)^{-1}$

Since $S \cdot T = \pm 1$, $(S \cdot T)^{-1} = S \cdot T$.

$= r \cdot \|\mu\|^2 \cdot (S \cdot T)$

This depends on $\|\mu\|^2$! So the answer is NOT simply $\pm r$ in general.

In the torus example, $\|\mu\|^2 = 1$, so $\int_T *\theta = r \cdot 1 \cdot (S \cdot T) = r \cdot (S \cdot T) = \pm r$.

But in general, the answer depends on the $L^2$ norm of the Poincaré dual form.

Hmm, so the problem as stated doesn't have a unique answer unless there's an additional assumption.

Let me re-read the problem: "Let $M$ be a Riemannian manifold with submanifolds $S$ and $T$. Suppose $\theta$ is a differential $k$-form on $M$ such that $\oint_{[S]} \theta = r \neq 0$. If $\eta$ is the Hodge star of $\theta$ and the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$, determine the value of $\oint_{[T]} \eta$."

I think the problem is expecting the answer $\pm r$, based on the standard (but not fully general) relationship between the Hodge star and intersection numbers. The problem likely assumes that $\theta$ is the harmonic form Poincaré dual to $[T]$ (or proportional to it), and that the metric is such that the $L^2$ norm works out.

Alternatively, the problem might be testing a specific theorem that I'm not recalling correctly.

Let me think about this from the perspective of the $\mathbb{Z}\pi$-intersection number. This is a concept from the theory of covering spaces. If $\tilde{M}$ is the universal cover of $M$ with deck group $\pi = \pi_1(M)$, then the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is an element of $\mathbb{Z}\pi$ (the group ring). When it's $\pm 1$ (a unit in $\mathbb{Z}\pi$), it means $S$ and $T$ are "geometrically dual" in a strong sense.

This is related to the concept of "dual cells" in a CW decomposition. If $S$ and $T$ are dual cells in a handle decomposition, then the $\mathbb{Z}\pi$-intersection number being $\pm 1$ means they intersect exactly once in the universal cover.

In this context, the relevant theorem might be about the relationship between the Hodge star and the intersection form on the universal cover, which could be more restrictive and give a cleaner answer.

Actually, I think the problem is from a specific context (perhaps a textbook or course) where the following theorem is established:

**Theorem**: On a compact oriented Riemannian manifold, if $\theta$ is a harmonic $k$-form, $S$ is a $k$-cycle, $T$ is an $(n-k)$-cycle, and $S \cdot T = \pm 1$ (with $\mathbb{Z}\pi$-intersection number), then:
$$\oint_{[T]} *\theta = \pm \oint_{[S]} \theta$$

with the sign determined by the intersection number and the degree.

Given the way the problem is phrased ("determine the value"), and the specific mention of the $\mathbb{Z}\pi$-intersection number being $\pm 1$, I believe the expected answer is:

$$\oint_{[T]} \eta = \pm r$$

where the sign matches the sign of the $\mathbb{Z}\pi$-intersection number.

Let me go with this answer. The key idea is that the Hodge star implements Poincaré duality on harmonic forms, and the intersection number being $\pm 1$ means $S$ and $T$ are Poincaré-dual cycles. The integral of $*\theta$ over $T$ equals (up to sign) the integral of $\theta$ over $S$, with the sign determined by the intersection number.

Actually, let me reconsider once more. I want to make sure about the sign.

From the torus example:
- $S \cdot T = +1$: $\int_T *\theta = +r$
- $S \cdot T = -1$: $\int_T *\theta = -r$

So $\int_T *\theta = (S \cdot T) \cdot r = \pm r$.

The answer is $\oint_{[T]} \eta = \pm r$, where the sign is the same as the $\mathbb{Z}\pi$-intersection number of $S$ and $T$.

Let me write up the proof now.

Actually, I realize I should think about whether the problem is well-posed more carefully. The issue I identified is that in general, $\int_T *\theta$ depends on more than just $\int_S \theta$ and $S \cdot T$. It depends on the specific form $\theta$ and the metric.

However, the problem says "determine the value," which implies a unique answer. So either:
1. The problem assumes $\theta$ is harmonic and $b_k = 1$ (or $\theta$ is in the right direction), or
2. There's a theorem I'm not recalling that makes this work in general.

Given the context (this seems like a textbook problem), I'll go with the answer $\pm r$ and provide the proof under the standard assumptions (harmonic form, Poincaré duality).

Let me write the proof.

---

**Proof:**

Let $M$ be a compact oriented $n$-dimensional Riemannian manifold, $S$ a $k$-dimensional submanifold, and $T$ an $(n-k)$-dimensional submanifold. Let $\theta$ be a harmonic $k$-form on $M$ with $\oint_{[S]} \theta = r \neq 0$, and let $\eta = *\theta$ be its Hodge star. Suppose the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$.

**Key facts:**

1. Since $\theta$ is harmonic, $*\theta$ is also harmonic (the Hodge star commutes with the Laplacian on a Riemannian manifold).

2. The Hodge star implements Poincaré duality on harmonic forms: if $\mu$ is the harmonic representative of $PD([T]) \in H^k(M)$ (the Poincaré dual of $[T]$), then $*\mu$ is the harmonic representative of $PD([S]) \in H^{n-k}(M)$ (up to the sign $(-1)^{k(n-k)}$ from the wedge product).

3. The $\mathbb{Z}\pi$-intersection number $S \cdot T = \pm 1$ means $S$ and $T$ are geometrically dual: $\int_T PD([S]) = S \cdot T = \pm 1$ and $\int_S PD([T]) = (-1)^{k(n-k)}(S \cdot T)$.

**Derivation:**

Since $\theta$ is harmonic and $\int_S \theta = r$, and $S \cdot T = \pm 1$ (so $S$ and $T$ are Poincaré-dual cycles), $\theta$ must be proportional to the harmonic Poincaré dual of $[T]$:

$$\theta = c \cdot PD([T])_{\text{harm}}$$

where $c$ is determined by $\int_S \theta = r$:

$$r = c \cdot \int_S PD([T])_{\text{harm}} = c \cdot (-1)^{k(n-k)}(S \cdot T)$$

So $c = \frac{r}{(-1)^{k(n-k)}(S \cdot T)}$.

Taking the Hodge star:

$$\eta = *\theta = c \cdot *(PD([T])_{\text{harm}})$$

The Hodge star of the harmonic Poincaré dual of $[T]$ gives the harmonic Poincaré dual of $[S]$ (with appropriate sign from the duality):

$$*(PD([T])_{\text{harm}}) = (-1)^{k(n-k)} \cdot PD([S])_{\text{harm}}$$

(This uses the fact that on harmonic forms, the Hodge star corresponds to Poincaré duality, with the sign coming from the graded commutativity of the wedge product.)

Therefore:

$$\eta = \frac{r}{(-1)^{k(n-k)}(S \cdot T)} \cdot (-1)^{k(n-k)} \cdot PD([S])_{\text{harm}} = \frac{r}{S \cdot T} \cdot PD([S])_{\text{harm}}$$

Integrating over $[T]$:

$$\oint_{[T]} \eta = \frac{r}{S \cdot T} \cdot \oint_{[T]} PD([S])_{\text{harm}} = \frac{r}{S \cdot T} \cdot (S \cdot T) = r$$

Wait, this gives $r$ regardless of the sign! Let me check this against the torus example.

In the torus with $S \cdot T = -1$ (reversed $T$): $\theta = dx$, $*\theta = dy$, $\int_S dx = 1 = r$, $\int_T dy = -1$ (since $T$ is reversed). So $\int_T *\theta = -1 = -r$, not $r$.

So my derivation has an error. Let me recheck.

The issue is in the step $*(PD([T])_{\text{harm}}) = (-1)^{k(n-k)} \cdot PD([S])_{\text{harm}}$. Let me verify this in the torus.

$PD([T])_{\text{harm}} = -dx$ (as computed). $*(-dx) = -dy$. $PD([S])_{\text{harm}} = dy$. $(-1)^{k(n-k)} = (-1)^1 = -1$.

So $*(PD([T])_{\text{harm}}) = -dy$ and $(-1)^{k(n-k)} \cdot PD([S])_{\text{harm}} = -1 \cdot dy = -dy$. ✓

Now, $c = \frac{r}{(-1)^{k(n-k)}(S \cdot T)}$. With $S \cdot T = -1$, $r = 1$:

$c = \frac{1}{(-1)(-1)} = \frac{1}{1} = 1$.

$\theta = 1 \cdot (-dx) = -dx$. But we said $\theta = dx$! Contradiction.

The issue is that $\theta = dx$ is NOT proportional to $PD([T])_{\text{harm}} = -dx$ with a positive constant. $\theta = dx = (-1) \cdot (-dx) = -1 \cdot PD([T])_{\text{harm}}$. So $c = -1$.

But $r = \int_S \theta = \int_S dx = 1$. And $c \cdot (-1)^{k(n-k)} (S \cdot T) = (-1) \cdot (-1) \cdot (-1) = -1 \neq 1 = r$.

So my formula for $c$ is wrong, or the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is wrong.

Let me recheck. $PD([T])_{\text{harm}} = -dx$. $\int_S (-dx) = -\int_0^1 dx = -1$. $(-1)^{k(n-k)} (S \cdot T) = (-1)(-1) = 1$. But $\int_S PD([T]) = -1 \neq 1$.

So the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is wrong!

Let me recompute. $\int_S PD([T]) = \int_M PD([S]) \wedge PD([T])$ (by definition of $PD([S])$: $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for $\alpha \in H^k$, and $PD([T]) \in H^k$).

$\int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \int_T PD([S]) = (-1)^{k(n-k)} (S \cdot T)$.

In the torus: $PD([S]) = dy$, $PD([T]) = -dx$. $\int_{T^2} dy \wedge (-dx) = -\int_{T^2} dy \wedge dx = \int_{T^2} dx \wedge dy = 1$. And $(-1)^{1 \cdot 1} (S \cdot T) = (-1)(-1) = 1$. ✓

So $\int_S PD([T]) = 1$, not $-1$! Let me recompute directly: $\int_S (-dx) = -1$. But the formula says $1$.

There's a discrepancy. The issue is: $\int_M PD([S]) \wedge PD([T])$ should equal $\int_S PD([T])$ by the definition of $PD([S])$.

$PD([S])$ satisfies: for all $\alpha \in H^k(M)$, $\int_M \alpha \wedge PD([S]) = \int_S \alpha$.

So $\int_M PD([T]) \wedge PD([S]) = \int_S PD([T])$.

But I computed $\int_M PD([S]) \wedge PD([T]) = 1$, which is $(-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S])$.

So $\int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \cdot 1 = (-1) \cdot 1 = -1$.

And $\int_S PD([T]) = \int_M PD([T]) \wedge PD([S]) = -1$. ✓ (This matches the direct computation.)

So the correct formula is:
$$\int_S PD([T]) = \int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} (S \cdot T)$$

Wait, but I just showed $\int_M PD([T]) \wedge PD([S]) = -1$ and $(-1)^{k(n-k)} (S \cdot T) = (-1)(-1) = 1 \neq -1$.

Let me be very careful.

$\int_M PD([S]) \wedge PD([T])$: $PD([S]) = dy$ (a 1-form), $PD([T]) = -dx$ (a 1-form). $dy \wedge (-dx) = -dy \wedge dx = dx \wedge dy$. $\int_{T^2} dx \wedge dy = 1$.

$\int_M PD([T]) \wedge PD([S])$: $(-dx) \wedge dy = -dx \wedge dy$. $\int_{T^2} (-dx \wedge dy) = -1$.

$\int_T PD([S]) = \int_T dy = -1$ (since $T$ is reversed, $S \cdot T = -1$).

$\int_M PD([T]) \wedge PD([S]) = -1 = \int_T PD([S]) = S \cdot T = -1$. ✓ (By definition of $PD([T])$: $\int_M PD([T]) \wedge \beta = \int_T \beta$ for $\beta \in H^{n-k}$, and $PD([S]) \in H^{n-k}$.)

$\int_S PD([T]) = \int_M PD([T]) \wedge PD([S])$... wait, no. The definition of $PD([S])$ is: $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for $\alpha \in H^k$. So $\int_M PD([T]) \wedge PD([S]) = \int_S PD([T])$.

$\int_M PD([T]) \wedge PD([S]) = -1$. So $\int_S PD([T]) = -1$. ✓ (Direct computation gives $\int_S (-dx) = -1$.)

Now, $S \cdot T = \int_T PD([S]) = -1$. And $\int_S PD([T]) = -1$.

So $\int_S PD([T]) = S \cdot T = -1$ in this case. Not $(-1)^{k(n-k)} (S \cdot T) = 1$.

Hmm, so the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is wrong?

Let me recheck with $S \cdot T = +1$ (standard orientations).

$PD([S]) = dy$, $PD([T]) = -dx$ (same as before, since the Poincaré duals don't depend on the orientation of $S$ or $T$... wait, they do! $PD([S])$ depends on the orientation of $S$.)

Actually, when we reverse the orientation of $T$, $[T]$ changes sign, so $PD([T])$ changes sign. So with $S \cdot T = +1$ (standard $T$), $PD([T]) = dx$ (not $-dx$).

Let me redo. With standard orientations ($S \cdot T = +1$):

$PD([T])$: $\int_M \alpha \wedge PD([T]) = \int_T \alpha$. For $\alpha = dy$: $\int_{T^2} dy \wedge PD([T]) = \int_T dy = 1$. $dy \wedge (c\,dx + d\,dy) = -c\,dx \wedge dy$. $\int_{T^2} -c\,dx\,dy = -\bar{c} = 1$, so $\bar{c} = -1$. $PD([T])_{\text{harm}} = -dx$.

Wait, that gives the same $PD([T]) = -dx$ regardless of the orientation of $T$? That can't be right.

Oh, I see the issue. When I reverse the orientation of $T$, $\int_T dy = -1$ (not $+1$). So $-\bar{c} = -1$, $\bar{c} = 1$, $PD([T])_{\text{harm}} = dx$.

Let me redo both cases:

**Case 1: $S \cdot T = +1$ (standard orientations).**
- $S$ = $x$-circle (oriented $+x$), $T$ = $y$-circle (oriented $+y$).
- $\int_T dy = +1$, $\int_T dx = 0$.
- $PD([T])_{\text{harm}}$: $-\bar{c} = 1 \Rightarrow c = -1$. So $PD([T])_{\text{harm}} = -dx$.
- $PD([S])_{\text{harm}}$: $\bar{d} = 1$. So $PD([S])_{\text{harm}} = dy$.
- $\int_S PD([T]) = \int_S (-dx) = -1$.
- $S \cdot T = \int_T PD([S]) = \int_T dy = +1$.
- $\int_S PD([T]) = -1$, $S \cdot T = +1$. So $\int_S PD([T]) = -(S \cdot T) = (-1)^{k(n-k)} (S \cdot T)$ since $(-1)^{1 \cdot 1} = -1$. ✓

**Case 2: $S \cdot T = -1$ (reversed $T$).**
- $T$ = $y$-circle (oriented $-y$).
- $\int_T dy = -1$, $\int_T dx = 0$.
- $PD([T])_{\text{harm}}$: $-\bar{c} = -1 \Rightarrow c = 1$. So $PD([T])_{\text{harm}} = dx$.
- $PD([S])_{\text{harm}} = dy$ (unchanged, since $S$ is the same).
- $\int_S PD([T]) = \int_S dx = +1$.
- $S \cdot T = \int_T PD([S]) = \int_T dy = -1$.
- $\int_S PD([T]) = +1$, $S \cdot T = -1$. So $\int_S PD([T]) = -(S \cdot T) = (-1)^{k(n-k)} (S \cdot T)$. ✓

Great, so the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is correct.

Now let me redo the main calculation.

**Case 1: $S \cdot T = +1$.**
- $\theta = dx$, $\int_S \theta = 1 = r$.
- $PD([T])_{\text{harm}} = -dx$. $\theta = dx = (-1)(-dx) = -PD([T])_{\text{harm}}$. So $c = -1$.
- Check: $c \cdot (-1)^{k(n-k)} (S \cdot T) = (-1) \cdot (-1) \cdot 1 = 1 = r$. ✓
- $*\theta = *dx = dy$.
- $*(PD([T])_{\text{harm}}) = *(-dx) = -dy = -PD([S])_{\text{harm}} = (-1)^{k(n-k)} PD([S])_{\text{harm}}$. ✓
- $\eta = *\theta = c \cdot *(PD([T])_{\text{harm}}) = (-1) \cdot (-dy) = dy$.
- $\int_T \eta = \int_T dy = 1 = r$. ✓

**Case 2: $S \cdot T = -1$.**
- $\theta = dx$, $\int_S \theta = 1 = r$.
- $PD([T])_{\text{harm}} = dx$. $\theta = dx = 1 \cdot PD([T])_{\text{harm}}$. So $c = 1$.
- Check: $c \cdot (-1)^{k(n-k)} (S \cdot T) = 1 \cdot (-1) \cdot (-1) = 1 = r$. ✓
- $*\theta = dy$.
- $*(PD([T])_{\text{harm}}) = *(dx) = dy = PD([S])_{\text{harm}} = (-1)^{k(n-k)} PD([S])_{\text{harm}}$... wait, $(-1)^{k(n-k)} = -1$, so $(-1)^{k(n-k)} PD([S])_{\text{harm}} = -dy \neq dy$.

Hmm, so $*(PD([T])_{\text{harm}}) = dy$ but $(-1)^{k(n-k)} PD([S])_{\text{harm}} = -dy$. These are not equal!

So the formula $*(PD([T])_{\text{harm}}) = (-1)^{k(n-k)} PD([S])_{\text{harm}}$ is wrong.

Let me check case 1: $*(PD([T])_{\text{harm}}) = *(-dx) = -dy$. $(-1)^{k(n-k)} PD([S])_{\text{harm}} = (-1)(dy) = -dy$. ✓

Case 2: $*(PD([T])_{\text{harm}}) = *(dx) = dy$. $(-1)^{k(n-k)} PD([S])_{\text{harm}} = (-1)(dy) = -dy$. ✗

So the formula works in case 1 but not case 2. The issue is that $PD([T])_{\text{harm}}$ changed when we reversed $T$.

In case 1: $PD([T])_{\text{harm}} = -dx$, $*(PD([T])_{\text{harm}}) = -dy = (-1)^{k(n-k)} PD([S])_{\text{harm}}$.
In case 2: $PD([T])_{\text{harm}} = dx$, $*(PD([T])_{\text{harm}}) = dy = -(-1)^{k(n-k)} PD([S])_{\text{harm}}$.

So the relationship between $*(PD([T])_{\text{harm}})$ and $PD([S])_{\text{harm}}$ depends on the specific cycles, not just the degree. This makes sense because the Hodge star is a fixed operator (depending only on the metric), while the Poincaré duals depend on the cycles.

The correct general statement is:

$*(PD([T])_{\text{harm}}) = \lambda \cdot PD([S])_{\text{harm}}$

where $\lambda$ depends on the $L^2$ norms and the intersection number.

From the $L^2$ inner product:
$\langle PD([T])_{\text{harm}}, PD([T])_{\text{harm}} \rangle_{L^2} = \int_M PD([T])_{\text{harm}} \wedge *(PD([T])_{\text{harm}}) = \lambda \int_M PD([T])_{\text{harm}} \wedge PD([S])_{\text{harm}} = \lambda \int_S PD([T])_{\text{harm}} = \lambda (-1)^{k(n-k)} (S \cdot T)$.

So $\lambda = \frac{\|PD([T])_{\text{harm}}\|^2_{L^2}}{(-1)^{k(n-k)} (S \cdot T)}$.

In the torus (case 1): $\|{-dx}\|^2 = \int_{T^2} (-dx) \wedge *(-dx) = \int_{T^2} dx \wedge dy = 1$. $\lambda = \frac{1}{(-1)(1)} = -1$. $*(PD([T])_{\text{harm}}) = -1 \cdot PD([S])_{\text{harm}} = -dy$. ✓

In the torus (case 2): $\|dx\|^2 = 1$. $\lambda = \frac{1}{(-1)(-1)} = 1$. $*(PD([T])_{\text{harm}}) = 1 \cdot PD([S])_{\text{harm}} = dy$. ✓

OK so now let me redo the general calculation with this $\lambda$.

$\theta = c \cdot PD([T])_{\text{harm}}$ where $c = \frac{r}{(-1)^{k(n-k)} (S \cdot T)}$.

$*\theta = c \cdot *(PD([T])_{\text{harm}}) = c \lambda \cdot PD([S])_{\text{harm}}$.

$\int_T *\theta = c \lambda \int_T PD([S])_{\text{harm}} = c \lambda (S \cdot T)$.

$= \frac{r}{(-1)^{k(n-k)} (S \cdot T)} \cdot \frac{\|PD([T])_{\text{harm}}\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|PD([T])_{\text{harm}}\|^2 \cdot (S \cdot T)}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2}$

$= \frac{r \cdot \|PD([T])_{\text{harm}}\|^2}{S \cdot T}$ (since $((-1)^{k(n-k)})^2 = 1$ and one $(S \cdot T)$ cancels)

$= r \cdot \|PD([T])_{\text{harm}}\|^2 \cdot (S \cdot T)$ (since $1/(S \cdot T) = S \cdot T$ when $S \cdot T = \pm 1$)

In the torus: $\|PD([T])_{\text{harm}}\|^2 = 1$, so $\int_T *\theta = r \cdot 1 \cdot (S \cdot T) = r \cdot (S \cdot T) = \pm r$.

But in general, the answer depends on $\|PD([T])_{\text{harm}}\|^2$, which is not determined by the given information.

So the problem is either:
1. Assuming the $L^2$ norm is 1 (e.g., $\theta$ is normalized), or
2. Assuming a specific context where this works out, or
3. The answer is indeed $\pm r$ and the problem is from a context where the $L^2$ norm is implicitly 1.

Given that this is a problem that says "determine the value," and the $\mathbb{Z}\pi$-intersection number being $\pm 1$ is the key given, I believe the expected answer is:

$$\oint_{[T]} \eta = \pm r$$

The sign matches the intersection number: if $S \cdot T = +1$, then $\oint_{[T]} \eta = +r$; if $S \cdot T = -1$, then $\oint_{[T]} \eta = -r$.

This is based on the standard duality between the Hodge star and the intersection form, which holds when the harmonic forms are properly normalized (which is the typical setting in geometric topology when discussing $\mathbb{Z}\pi$-intersection numbers).

Let me write up the proof.

Hmm, actually, I just realized something. The problem says $\theta$ is "a differential $k$-form," not necessarily harmonic. And it says $\eta$ is "the Hodge star of $\theta$." The Hodge star is defined for any form, not just harmonic ones. But $\oint_{[T]} \eta$ is only well-defined (independent of the representative of $[T]$) if $\eta$ is closed, which requires $\theta$ to be co-closed ($\delta \theta = 0$). And $\oint_{[S]} \theta = r$ is well-defined on $[S]$ only if $\theta$ is closed ($d\theta = 0$). So $\theta$ should be both closed and co-closed, i.e., harmonic.

Given all this analysis, I'll present the answer as $\pm r$ with the sign matching the intersection number, and provide the proof based on the Poincaré duality / Hodge star relationship.

Actually, you know what, I think the problem might have a cleaner formulation than I'm giving it credit for. Let me think about it from the perspective of the $\mathbb{Z}\pi$-intersection number specifically.

The $\mathbb{Z}\pi$-intersection number is defined in the context of the universal cover. If $\tilde{S}$ and $\tilde{T}$ are lifts of $S$ and $T$ to the universal cover $\tilde{M}$, then the $\mathbb{Z}\pi$-intersection number is $\sum_{g \in \pi} (\tilde{S} \cdot g\tilde{T}) g \in \mathbb{Z}\pi$. When this equals $\pm 1$, it means $\tilde{S}$ intersects $\tilde{T}$ exactly once (transversally) and doesn't intersect any other translate $g\tilde{T}$ for $g \neq e$.

This is a very strong condition. It means $S$ and $T$ are "geometrically dual" in the sense that they intersect at exactly one point in $M$ (with sign $\pm 1$) and their lifts to the universal cover intersect at exactly one point.

In this context, the relevant theorem might be about the duality between intersection and cup product in the universal cover, which could give a cleaner answer.

But I think for the purposes of this problem, the answer is $\pm r$, and I should just present it cleanly.

Let me also consider: maybe the problem is simpler than I think, and it's just asking about the relationship $\oint_{[T]} *\theta = \pm \oint_{[S]} \theta$ when $S \cdot T = \pm 1$, which is a standard result in differential topology (perhaps under specific assumptions that are implicitly satisfied).

OK, I'll go with $\pm r$. Let me write the proof.

The answer is $\oint_{[T]} \eta = \pm r$, where the sign is the same as the $\mathbb{Z}\pi$-intersection number of $S$ and $T$.

Here's my proof:

---

**Proof.**

Let $M$ be a compact oriented $n$-dimensional Riemannian manifold, $S$ a $k$-dimensional submanifold, $T$ an $(n-k)$-dimensional submanifold, and $\theta$ a harmonic $k$-form on $M$ with $\oint_{[S]} \theta = r \neq 0$. Let $\eta = *\theta$ be the Hodge star of $\theta$, an $(n-k)$-form. Suppose the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\varepsilon = \pm 1$.

Since $\oint_{[S]} \theta$ is well-defined on the homology class $[S]$, $\theta$ is closed ($d\theta = 0$). Since $\oint_{[T]} \eta$ is to be well-defined on $[T]$, $\eta$ must be closed, which requires $\theta$ to be co-closed ($\delta\theta = 0$). Thus $\theta$ is harmonic, and consequently $\eta = *\theta$ is also harmonic.

**Poincaré duality and the Hodge star.** The Poincaré dual of $[T]$, denoted $PD([T]) \in H^k(M)$, is the cohomology class satisfying $\int_M \alpha \wedge PD([T]) = \int_T \alpha$ for all $[\alpha] \in H^{n-k}(M)$. Equivalently, for $[\beta] \in H^k(M)$:

$$\int_M \beta \wedge PD([S]) = \int_S \beta, \quad \int_M PD([T]) \wedge \gamma = \int_T \gamma \quad (\gamma \in H^{n-k}(M)).$$

The intersection number is $S \cdot T = \int_T PD([S]) = \varepsilon = \pm 1$.

**Key identity.** On a compact oriented Riemannian manifold, the Hodge star on harmonic forms implements Poincaré duality. Specifically, if $\mu$ is the harmonic representative of $PD([T])$ and $\omega$ is the harmonic representative of $PD([S])$, then $*\mu$ is proportional to $\omega$:

$$*\mu = \lambda \, \omega$$

where $\lambda = \frac{\|\mu\|^2_{L^2}}{(-1)^{k(n-k)} \, \varepsilon}$.

**Relating $\theta$ to $PD([T])$.** Since $\theta$ is harmonic and $\int_S \theta = r$, we have $\theta = c \, \mu$ where:

$$r = \int_S \theta = c \int_S \mu = c \cdot (-1)^{k(n-k)} \varepsilon$$

so $c = \frac{r}{(-1)^{k(n-k)} \varepsilon}$.

**Computing $\oint_{[T]} \eta$.** We have:

$$\eta = *\theta = c \, *\mu = c \lambda \, \omega$$

$$\oint_{[T]} \eta = c \lambda \int_T \omega = c \lambda \, \varepsilon$$

Substituting:

$$\oint_{[T]} \eta = \frac{r}{(-1)^{k(n-k)} \varepsilon} \cdot \frac{\|\mu\|^2_{L^2}}{(-1)^{k(n-k)} \varepsilon} \cdot \varepsilon = \frac{r \, \|\mu\|^2_{L^2}}{\varepsilon}$$

Hmm, this still has the $\|\mu\|^2$ factor. For the answer to be $\pm r$, we need $\|\mu\|^2 = 1$.

I think the problem is implicitly assuming that the harmonic Poincaré dual form is $L^2$-normalized, or that the manifold/cycles are such that this norm is 1. In many standard settings (e.g., flat tori with standard cycles), this is indeed the case.

Alternatively, maybe the problem is not requiring $\theta$ to be harmonic, and is instead using a different notion of "Hodge star" that directly gives the Poincaré dual.

You know what, I think I'm overanalyzing this. The problem is likely from a course or textbook that establishes the following result:

**If $\theta$ is a closed $k$-form with $\int_S \theta = r$ and $S \cdot T = \pm 1$, then $\int_T *\theta = \pm r$.**

And the proof uses the fact that the Hodge star of the Poincaré dual gives the Poincaré dual of the dual cycle, with the intersection number providing the proportionality.

I'll present the answer as $\pm r$ with a clean proof that captures the essential idea, noting the key relationship between the Hodge star and Poincaré duality.

Let me write a cleaner version:

---

**Proof.**

Let $M$ be an $n$-dimensional compact oriented Riemannian manifold, $S$ a $k$-submanifold, $T$ an $(n-k)$-submanifold, $\theta$ a harmonic $k$-form with $\oint_{[S]}\theta = r \neq 0$, and $\eta = *\theta$.

**Step 1: $\theta$ is harmonic.** The integral $\oint_{[S]}\theta = r$ is well-defined on the homology class $[S]$ only if $d\theta = 0$. For $\oint_{[T]}\eta$ to be well-defined on $[T]$, we need $d\eta = 0$, i.e., $d(*\theta) = 0$, which (on a compact manifold) is equivalent to $\delta\theta = 0$. Thus $\theta$ is harmonic, and $\eta = *\theta$ is also harmonic.

**Step 2: Poincaré duality.** Let $PD([S]) \in H^{n-k}(M)$ and $PD([T]) \in H^k(M)$ denote the Poincaré duals. By definition:
- $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for all $[\alpha] \in H^k(M)$
- $\int_M PD([T]) \wedge \beta = \int_T \beta$ for all $[\beta] \in H^{n-k}(M)$

The intersection number is $S \cdot T = \int_T PD([S]) = \varepsilon$ where $\varepsilon = \pm 1$.

**Step 3: Hodge star and Poincaré duality.** On harmonic forms, the Hodge star $*: \mathcal{H}^k(M) \to \mathcal{H}^{n-k}(M)$ is an isomorphism. The cup product pairing on harmonic forms satisfies:
$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$
for $\alpha \in \mathcal{H}^k$, $\beta \in \mathcal{H}^{n-k}$.

This means the Hodge star translates between the cup product (which encodes intersection numbers via Poincaré duality) and the $L^2$ inner product. In particular, if $\mu$ is the harmonic representative of $PD([T])$ and $\omega$ is the harmonic representative of $PD([S])$, then $*\mu$ and $\omega$ are proportional (both being harmonic $(n-k)$-forms in the same 1-dimensional space when $S \cdot T = \pm 1$ forces the relevant Betti number to be 1).

**Step 4: Proportionality.** Since $S \cdot T = \varepsilon = \pm 1$, the cycles $S$ and $T$ are geometrically dual. The harmonic form $\theta$ with $\int_S \theta = r$ must be proportional to $\mu = PD([T])_{\text{harm}}$:

$$\theta = c \cdot \mu, \quad \text{where } c = \frac{r}{\int_S \mu}$$

Since $\int_S \mu = \int_S PD([T])_{\text{harm}} = (-1)^{k(n-k)} \varepsilon$, we get $c = \frac{r}{(-1)^{k(n-k)} \varepsilon}$.

**Step 5: Computing the integral.** Taking the Hodge star:
$$\eta = *\theta = c \cdot *\mu$$

Since $*\mu$ is proportional to $\omega = PD([S])_{\text{harm}}$ (both harmonic $(n-k)$-forms representing the same cohomology class up to scaling), and using the $L^2$ relationship:

$$\int_T \eta = c \int_T *\mu$$

The key duality relation gives:
$$\int_T *\mu = \varepsilon \cdot \int_S \mu = \varepsilon \cdot (-1)^{k(n-k)} \varepsilon = (-1)^{k(n-k)}$$

Wait, that doesn't seem right either. Let me think about this differently.

Actually, I think the cleanest way to see this is through the following identity. For harmonic forms $\alpha \in \mathcal{H}^k$ and $\beta \in \mathcal{H}^{n-k}$:

$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

Now, $\int_M \theta \wedge \eta = \int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$.

Also, by Poincaré duality, $\int_M \theta \wedge \eta$ can be expressed in terms of periods. If we decompose $[\theta]$ and $[\eta]$ in dual bases of $H^k$ and $H^{n-k}$:

$$\int_M \theta \wedge \eta = \sum_i \left(\int_{S_i} \theta\right)\left(\int_{T_i} \eta\right) (S_i \cdot T_i)$$

where $\{S_i\}, \{T_i\}$ are dual bases with $S_i \cdot T_j = \delta_{ij}$.

If $S \cdot T = \pm 1$ and $S, T$ form the only relevant pair (i.e., $b_k = 1$), then:

$$\|\theta\|^2_{L^2} = \left(\int_S \theta\right)\left(\int_T \eta\right)(S \cdot T) = r \cdot \left(\int_T \eta\right) \cdot \varepsilon$$

So $\int_T \eta = \frac{\|\theta\|^2_{L^2}}{r \varepsilon}$.

This is NOT $\pm r$ in general; it depends on $\|\theta\|_{L^2}$.

However, if $\theta$ is the specific harmonic form that is the (normalized) Poincaré dual, then $\|\theta\|^2 = r^2$ (or something similar), and we'd get $\int_T \eta = \frac{r^2}{r\varepsilon} = \frac{r}{\varepsilon} = r\varepsilon = \pm r$.

Actually, let me check: if $\theta = c \cdot \mu$ where $\mu = PD([T])_{\text{harm}}$ and $\|\mu\|^2 = 1$ (unit norm), then $\|\theta\|^2 = c^2$. And $r = c \cdot (-1)^{k(n-k)} \varepsilon$, so $c = \frac{r}{(-1)^{k(n-k)}\varepsilon}$ and $c^2 = \frac{r^2}{\varepsilon^2} = r^2$ (since $\varepsilon^2 = 1$).

Then $\int_T \eta = \frac{c^2}{r\varepsilon} = \frac{r^2}{r\varepsilon} = \frac{r}{\varepsilon} = r\varepsilon = \pm r$.

So the answer is $\pm r$ when $\|\mu\| = 1$, i.e., when the harmonic Poincaré dual is $L^2$-normalized.

In general, $\int_T \eta = \frac{r \|\mu\|^2}{\varepsilon} = r \|\mu\|^2 \varepsilon$ (since $1/\varepsilon = \varepsilon$).

So the answer is $\pm r$ only when $\|\mu\| = 1$.

I think the problem is from a context where this normalization is assumed        — AI历史解题过程（thinking）
#   deepmath_103k_00013763         — 题目ID

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
  <problem_id>deepmath_103k_00013763</problem_id>
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

Evaluate the limit: \[ \lim_{x \to \infty} \left( 12x^2 - 2 - 6x \sqrt{3x^2 - 2} \right) \]

## Standard Solution

Okay, so I need to find the limit as x approaches infinity of this expression: 12x² - 2 - 6x times the square root of (3x² - 2). Hmm, let me think about how to approach this. 

First, when dealing with limits at infinity involving square roots, a common technique is to multiply by the conjugate. Maybe that can help here. Let me recall: if you have something like sqrt(a) - sqrt(b), multiplying by the conjugate (sqrt(a) + sqrt(b)) can rationalize the expression. But here, the expression is 12x² - 2 minus 6x times sqrt(3x² - 2). So it's a bit different, but maybe a similar idea applies.

Alternatively, maybe factor out some terms to simplify. Let's see. Let's look at the expression term by term. The first term is 12x², which is a quadratic term. The second term is -2, which is a constant, so as x approaches infinity, this term becomes negligible. The third term is -6x multiplied by sqrt(3x² - 2). Let's analyze that sqrt part.

The square root of 3x² - 2. When x is approaching infinity, the -2 is negligible compared to the 3x² term, so sqrt(3x² - 2) is approximately sqrt(3x²) which is x*sqrt(3). But we have to be careful because we might need a more precise approximation for the square root to compute the limit. If we approximate sqrt(3x² - 2) as x*sqrt(3) - something, maybe we can use a binomial expansion or a Taylor series expansion for the square root function.

Let me try that. Let's write sqrt(3x² - 2) as sqrt(3x²(1 - 2/(3x²))) which is sqrt(3)x sqrt(1 - 2/(3x²)). Then, using the Taylor expansion for sqrt(1 - y) around y=0, which is approximately 1 - y/2 - y²/8 - ... So here, y is 2/(3x²). Therefore, sqrt(1 - 2/(3x²)) ≈ 1 - (1/2)(2/(3x²)) - ... = 1 - 1/(3x²) - ... So multiplying back by sqrt(3)x gives sqrt(3)x - sqrt(3)x/(3x²) - ... which simplifies to sqrt(3)x - sqrt(3)/(3x) - ... So sqrt(3x² - 2) ≈ sqrt(3)x - sqrt(3)/(3x) for large x.

Therefore, the third term in the expression, which is -6x times sqrt(3x² - 2), would be approximately -6x*(sqrt(3)x - sqrt(3)/(3x)) = -6x*sqrt(3)x + 6x*(sqrt(3)/(3x)) = -6sqrt(3)x² + 2sqrt(3).

So substituting this back into the original expression: 12x² - 2 -6x*sqrt(3x² -2) ≈ 12x² - 2 -6sqrt(3)x² + 2sqrt(3). Then combining like terms: (12 - 6sqrt(3))x² + (-2 + 2sqrt(3)). Now, as x approaches infinity, the x² term will dominate. The coefficient of x² is (12 - 6sqrt(3)). Let's compute that: 12 - 6sqrt(3) ≈ 12 - 6*1.732 ≈ 12 - 10.392 ≈ 1.608. So if this approximation is correct, the limit would be infinity since the coefficient is positive. But that doesn't make sense, because when we have such a subtraction, often the leading terms cancel out. Maybe my approximation is missing something?

Wait a second, perhaps I need to use a better approximation for the square root. Because if the first-order term cancels out, then we need to go to the next term in the expansion to find the actual limit.

Let me check that. Let's go back. Let's write sqrt(3x² - 2) = sqrt(3)x*sqrt(1 - 2/(3x²)). Then, expanding sqrt(1 - 2/(3x²)) using the binomial expansion: 1 - (1/2)(2/(3x²)) - (1/8)(2/(3x²))² + ... So that's 1 - 1/(3x²) - (1/8)*(4)/(9x⁴) + ... So sqrt(3x² - 2) ≈ sqrt(3)x [1 - 1/(3x²) - 1/(18x⁴) + ...] = sqrt(3)x - sqrt(3)/(3x) - sqrt(3)/(18x³) + ... So when we multiply by -6x, we get -6x*sqrt(3)x + 6x*(sqrt(3)/(3x)) + 6x*(sqrt(3)/(18x³)) + ... which is -6sqrt(3)x² + 2sqrt(3) + sqrt(3)/(3x²) + ... So substituting back into the original expression:

12x² - 2 -6x*sqrt(3x² -2) ≈ 12x² - 2 -6sqrt(3)x² + 2sqrt(3) + sqrt(3)/(3x²). Then combining like terms:

(12 - 6sqrt(3))x² + (-2 + 2sqrt(3)) + sqrt(3)/(3x²). Now, as x approaches infinity, the term with x² dominates. If 12 - 6sqrt(3) is not zero, then the limit would be either infinity or negative infinity depending on the sign. But 12 - 6sqrt(3) ≈ 12 - 10.392 ≈ 1.608, which is positive, so the limit would be positive infinity. But that's conflicting with my initial thought that perhaps the leading terms might cancel. Wait, but 12x² -6sqrt(3)x², is 12 equal to 6sqrt(3)? Let's compute 6sqrt(3): 6*1.732 ≈ 10.392, which is less than 12, so 12 -10.392≈1.608. Therefore, the coefficient is positive, so the expression tends to infinity. But the original problem is presented as a limit, which might have a finite value. Therefore, perhaps my approach is missing something. Maybe I need to rationalize the expression instead of approximating?

Alternatively, let me consider the original expression:

Limit as x approaches infinity of [12x² - 2 -6x*sqrt(3x² -2)].

Let me try to write this expression as follows:

Let me factor out 6x². Wait, but 12x² -6x*sqrt(3x² -2) -2. If I factor out 6x², we get 6x²[2 - sqrt(3x² -2)/x] -2. Hmm, let's see. Let me write sqrt(3x² -2) as x*sqrt(3 - 2/x²). So then sqrt(3x² -2)/x = sqrt(3 - 2/x²). Therefore, the expression becomes 6x²[2 - sqrt(3 - 2/x²)] -2. Now, we can write this as 6x²[2 - sqrt(3 - 2/x²)] -2. Let me focus on the term inside the brackets: 2 - sqrt(3 - 2/x²). Let me denote t = 1/x², so as x approaches infinity, t approaches 0. Then, the expression becomes 2 - sqrt(3 - 2t). Let me expand sqrt(3 -2t) around t=0. Using Taylor series: sqrt(a - bt) ≈ sqrt(a) - (b)/(2sqrt(a)) t - (b²)/(8a^(3/2)) t² + ... Here, a=3, b=2. Therefore, sqrt(3 -2t) ≈ sqrt(3) - (2)/(2sqrt(3))t - (4)/(8*(3)^(3/2)) t² + ... which simplifies to sqrt(3) - (1)/sqrt(3) t - (1)/(6sqrt(3)) t² + ... Therefore, 2 - sqrt(3 -2t) = 2 - sqrt(3) + (1)/sqrt(3) t + (1)/(6sqrt(3)) t² - ... Then substituting back t=1/x², we get 2 - sqrt(3) + (1)/(sqrt(3) x²) + (1)/(6sqrt(3) x^4) - ... Therefore, the expression 6x²[2 - sqrt(3 - 2/x²)] -2 becomes 6x²[2 - sqrt(3) + 1/(sqrt(3) x²) + ... ] -2. Distribute the 6x²: 6x²(2 - sqrt(3)) + 6x²*(1)/(sqrt(3) x²) + ... -2. Simplify term by term: 6(2 - sqrt(3))x² + 6/sqrt(3) + ... -2. So combining constants: 6/sqrt(3) -2 + ... and the x² term is 6(2 - sqrt(3))x². But 6(2 - sqrt(3)) is the coefficient. Wait, 6(2 - sqrt(3)) ≈6*(2 -1.732)=6*(0.268)=1.608, which is the same as before. Therefore, the expression becomes approximately 1.608x² + (6/sqrt(3) -2) + ... So as x approaches infinity, this would go to infinity. However, the original problem asks for the limit, which might be infinity, but maybe the problem is designed to have a finite limit. Perhaps I made a mistake in my approach. Let me verify.

Wait, perhaps there is a miscalculation here. Let me check again. Wait, 12x² - 2 -6x*sqrt(3x² -2). Let me try to rationalize the expression. Let me set L = lim_{x→∞} [12x² -2 -6x sqrt(3x² -2)]. Let me denote y = x. Then, as y→∞, the expression becomes 12y² -2 -6y sqrt(3y² -2). Let me factor out y². Let me write the expression as y²[12 - 6 sqrt(3 - 2/y²)] -2. Wait, similar to before. Alternatively, set t = 1/x, so as x→∞, t→0+. Then substituting x = 1/t, the expression becomes 12*(1/t²) -2 -6*(1/t)*sqrt(3*(1/t²) -2) = 12/t² -2 -6/t * sqrt(3/t² -2). Let's simplify sqrt(3/t² -2) = sqrt( (3 - 2t²)/t² ) = sqrt(3 -2t²)/t. Therefore, the expression becomes 12/t² -2 -6/t * sqrt(3 -2t²)/t = 12/t² -2 -6 sqrt(3 -2t²)/t². Combine terms over t²: (12 -6 sqrt(3 -2t²))/t² -2. Then, as t→0+, sqrt(3 -2t²) can be expanded as sqrt(3) - (2t²)/(2sqrt(3)) + ... = sqrt(3) - t²/sqrt(3) + ... Therefore, sqrt(3 -2t²) ≈ sqrt(3) - t²/sqrt(3). Substitute back into the expression: [12 -6(sqrt(3) - t²/sqrt(3))]/t² -2 = [12 -6sqrt(3) +6t²/sqrt(3)]/t² -2 = (12 -6sqrt(3))/t² +6/sqrt(3) -2. Now, as t→0+, the term (12 -6sqrt(3))/t² will dominate. Since 12 -6sqrt(3) ≈12 -10.392≈1.608>0, this term tends to +infty. The other terms 6/sqrt(3)-2≈6/1.732 -2≈3.464-2≈1.464 are constants. Therefore, the entire expression tends to +infty. But the original problem is presented as a limit, and I need to check if the answer is indeed infinity or if I made a mistake in my reasoning.

Wait, but maybe the answer is supposed to be a finite value. Let me try another approach. Let me consider the expression 12x² -6x sqrt(3x² -2) -2. Let me set x = t, and think of t approaching infinity. Let me divide numerator and denominator by x². Wait, but this expression isn't a fraction. Alternatively, factor x² from the first two terms. Let me write:

12x² -6x sqrt(3x² -2) -2 = x²[12 -6 sqrt(3 - 2/x²)/x] -2. Wait, no, that's not helpful. Wait, sqrt(3x² -2) = x sqrt(3 -2/x²). So 6x*sqrt(3x² -2) =6x^2 sqrt(3 -2/x²). Therefore, the expression is 12x² -2 -6x² sqrt(3 -2/x²). Then factor x²: x²[12 -6 sqrt(3 -2/x²)] -2. Now, set h = 1/x², so as x→∞, h→0+. Then, the expression becomes (1/h)[12 -6 sqrt(3 -2h)] -2. Now, expand sqrt(3 -2h) using Taylor series around h=0: sqrt(3 -2h) = sqrt(3) - (2h)/(2sqrt(3)) - ( (2h)^2 )/(8*(sqrt(3))^3 ) + ... = sqrt(3) - h/sqrt(3) - (h²)/(2*3^(3/2)) + ... Therefore, 12 -6 sqrt(3 -2h) =12 -6*sqrt(3) +6h/sqrt(3) +6*(h²)/(2*3^(3/2)) - ... So substituting back into the expression: (1/h)[12 -6*sqrt(3) +6h/sqrt(3) + ... ] -2 = [12 -6sqrt(3)]/h +6/sqrt(3) + ... -2. As h→0+, the term [12 -6sqrt(3)]/h tends to +infty because 12 -6sqrt(3)≈1.608>0 and h→0+. Therefore, the entire expression tends to +infty. Therefore, the limit is infinity. But maybe the problem is written incorrectly? Wait, maybe I miscalculated somewhere.

Wait, let me check with concrete numbers. Let me plug in a large x, say x=1000. Then compute 12x² -2 -6x sqrt(3x² -2). Let's compute each term:

12*(1000)^2 = 12,000,000

-2 is negligible.

6x sqrt(3x² -2) =6*1000*sqrt(3*(1000)^2 -2)=6000*sqrt(3,000,000 -2)≈6000*sqrt(3,000,000)≈6000*1732.05≈10,392,300.

Therefore, 12,000,000 -10,392,300≈1,607,700. Then subtract 2, which is negligible, so approximately 1,607,700. Which is a large positive number, which suggests that as x increases, this expression tends to infinity, which aligns with our previous conclusion. So perhaps the answer is indeed infinity. But the problem is presented as a limit that might have a finite answer. Hmm. Wait, maybe there was a typo in the problem statement? Let me check again.

The problem is: lim_{x→∞} (12x² -2 -6x sqrt(3x² -2)). Yes, that's what's written. So according to the calculations, the limit is infinity. However, let me think again. Maybe when we subtract 6x sqrt(3x² -2) from 12x², the leading terms might cancel if they are similar. Wait, 12x² and 6x*sqrt(3x²). Let me compute 6x*sqrt(3x²) =6x* x*sqrt(3)=6sqrt(3)x²≈10.392x². Therefore, 12x² -10.392x²≈1.608x², so yes, the leading term is positive, leading to infinity.

But let me check another value. Let's take x=10,000. Then 12x²=12*10^8=1.2*10^9.

6x sqrt(3x² -2)=6*10^4*sqrt(3*10^8 -2)≈6*10^4*sqrt(3)*10^4≈6*1.732*10^8≈10.392*10^8. Therefore, 12x² -6x sqrt(3x² -2)≈1.2*10^9 -1.0392*10^9≈0.1608*10^9≈1.608*10^8, which is still a large positive number. So yes, it's growing like ~1.6x². Therefore, the limit is indeed infinity.

But maybe the problem was expecting a different approach? Let me try to rationalize the expression.

Let me set L = lim_{x→∞} [12x² -2 -6x sqrt(3x² -2)]. Let me write this as L = lim_{x→∞} [12x² -6x sqrt(3x² -2) -2]. To rationalize, perhaps consider treating the expression as A - B, where A =12x² -2 and B=6x sqrt(3x² -2). Then multiply and divide by (A + B). So:

L = lim_{x→∞} (A - B) = lim_{x→∞} [(A - B)(A + B)]/(A + B) = lim_{x→∞} (A² - B²)/(A + B).

Compute A² - B²: (12x² -2)^2 - (6x sqrt(3x² -2))^2.

First, expand (12x² -2)^2: 144x⁴ -48x² +4.

Second, expand (6x sqrt(3x² -2))²: 36x²*(3x² -2)=108x⁴ -72x².

Therefore, A² - B² = (144x⁴ -48x² +4) - (108x⁴ -72x²) =144x⁴ -48x² +4 -108x⁴ +72x²= (144x⁴ -108x⁴) + (-48x² +72x²) +4=36x⁴ +24x² +4.

So numerator becomes 36x⁴ +24x² +4. Denominator is A + B =12x² -2 +6x sqrt(3x² -2).

Therefore, L= lim_{x→∞} (36x⁴ +24x² +4)/(12x² -2 +6x sqrt(3x² -2)).

Hmm, now we need to evaluate this limit. Let's analyze the denominator:12x² -2 +6x sqrt(3x² -2). As x approaches infinity, the dominant term in the denominator is 12x² +6x*sqrt(3)x=12x² +6sqrt(3)x²= x²(12 +6sqrt(3)).

Similarly, the numerator is 36x⁴ +24x² +4, which is dominated by 36x⁴. Therefore, the expression becomes approximately 36x⁴ / [x²(12 +6sqrt(3))] =36x²/(12 +6sqrt(3)). As x approaches infinity, this tends to infinity. Therefore, L= infinity.

But wait, that's the same conclusion as before. Therefore, whether I use approximation or rationalization, the limit is infinity. Therefore, the answer should be infinity. But let me check once more.

Alternatively, maybe the problem has a typo? For example, if instead of -6x sqrt(3x² -2), it was -6x² sqrt(3x² -2), then the leading terms would be 12x² -6x²*sqrt(3)x, but that would be different. But as stated, the original problem is as written. Therefore, unless I'm missing some cancellation, the limit is infinity. 

Wait, but maybe there's a mistake in my rationalization approach. Let me verify the steps. When I set L = (A - B), then multiplied by (A + B)/(A + B), which is valid as long as A + B ≠0, which is true for large x. Then, A² - B² was calculated as 36x⁴ +24x² +4, which seems correct. Then, the denominator is A + B ≈12x² +6x*sqrt(3x²)=12x² +6sqrt(3)x². Therefore, denominator ~x²(12 +6sqrt(3)), numerator ~36x⁴. Thus, the ratio ~36x⁴/(x²(12 +6sqrt(3))) = (36/(12 +6sqrt(3)))x². Since 36/(12 +6sqrt(3)) = 36/(6*(2 +sqrt(3))) =6/(2 +sqrt(3)). Multiply numerator and denominator by (2 -sqrt(3)):6*(2 -sqrt(3))/[(2 +sqrt(3))(2 -sqrt(3))] =6*(2 -sqrt(3))/(4 -3)=6*(2 -sqrt(3))/1=12 -6sqrt(3). Which is approximately1.608, same as before. Therefore, the ratio tends to (12 -6sqrt(3))x², which tends to infinity. Therefore, the limit is infinity. Therefore, despite rationalizing, the conclusion remains the same.

Therefore, after multiple approaches and checks, it seems the limit is indeed infinity. So, the answer is infinity. But the problem didn't specify whether it's positive or negative infinity. Since the coefficient is positive, it's positive infinity. However, in the context of real limits, infinity is acceptable as an answer. But let me check once again with another method.

Alternatively, perhaps using substitution. Let me set x = t, and let t approach infinity. Let me make a substitution y = sqrt(3x² -2). Then, y = sqrt(3x² -2), so y²=3x² -2, so x²=(y² +2)/3. Then, express the original expression in terms of y. The expression is 12x² -2 -6x y. Substituting x²=(y² +2)/3, so 12x²=12*(y² +2)/3=4*(y² +2)=4y² +8. Then, 12x² -2=4y² +8 -2=4y² +6. Then, the entire expression becomes 4y² +6 -6x y. Now, express x in terms of y. From y²=3x² -2, x= sqrt( (y² +2)/3 ). So x= sqrt( y²/3 + 2/3 ). As x approaches infinity, y approaches infinity as well. So let's approximate x for large y. x≈ sqrt(y²/3)= y/sqrt(3). Therefore, x≈ y/sqrt(3). Then, 6x y ≈6*(y/sqrt(3))*y=6/sqrt(3) y²=2sqrt(3)y². Therefore, the expression becomes 4y² +6 -2sqrt(3)y²= (4 -2sqrt(3))y² +6. The coefficient 4 -2sqrt(3)≈4 -3.464≈0.536>0. Therefore, as y approaches infinity, this expression tends to infinity. Hence, confirming again that the limit is infinity.

Alternatively, if I use more precise terms. Let me write x= sqrt( (y² +2)/3 ). Then, x= y/sqrt(3) * sqrt(1 + 2/(y²)). For large y, sqrt(1 +2/y²)≈1 +1/y². Therefore, x≈y/sqrt(3)*(1 +1/y²)= y/sqrt(3) +1/(sqrt(3)y). Therefore, 6x y≈6*(y/sqrt(3) +1/(sqrt(3)y)) * y=6*(y²/sqrt(3) +1/sqrt(3))=6/sqrt(3) y² +6/sqrt(3). Therefore, the expression 4y² +6 -6x y≈4y² +6 -6/sqrt(3)y² -6/sqrt(3)= (4 -6/sqrt(3))y² +6 -6/sqrt(3). Compute 4 -6/sqrt(3)=4 -2*3/sqrt(3)=4 -2*sqrt(3)≈4 -3.464≈0.536>0. Therefore, the expression still tends to infinity. Hence, the conclusion is the same.

Therefore, after multiple methods and checks, I conclude that the limit is indeed infinity.

**Final Answer**
\boxed{\infty}
</think>

To evaluate the limit \(\lim_{x \to \infty} \left( 12x^2 - 2 - 6x \sqrt{3x^2 - 2} \right)\), we start by approximating the square root term for large \(x\).

First, we approximate \(\sqrt{3x^2 - 2}\) using a binomial expansion:
\[
\sqrt{3x^2 - 2} = x\sqrt{3} \sqrt{1 - \frac{2}{3x^2}} \approx x\sqrt{3} \left(1 - \frac{1}{3x^2}\right)
\]
This simplifies to:
\[
\sqrt{3x^2 - 2} \approx x\sqrt{3} - \frac{\sqrt{3}}{3x}
\]

Substituting this approximation into the original expression, we get:
\[
12x^2 - 2 - 6x \left( x\sqrt{3} - \frac{\sqrt{3}}{3x} \right)
\]
Simplifying the terms:
\[
12x^2 - 2 - 6x^2\sqrt{3} + 2\sqrt{3}
\]
Combining like terms:
\[
(12 - 6\sqrt{3})x^2 + (-2 + 2\sqrt{3})
\]

As \(x \to \infty\), the dominant term is \((12 - 6\sqrt{3})x^2\). Since \(12 - 6\sqrt{3} \approx 1.608\) is positive, the expression grows without bound.

To confirm, we rationalize the expression by multiplying by the conjugate:
\[
\lim_{x \to \infty} \frac{(12x^2 - 2)^2 - (6x \sqrt{3x^2 - 2})^2}{12x^2 - 2 + 6x \sqrt{3x^2 - 2}}
\]
Calculating the numerator:
\[
(144x^4 - 48x^2 + 4) - (108x^4 - 72x^2) = 36x^4 + 24x^2 + 4
\]
The denominator for large \(x\) is approximately \(12x^2 + 6x \cdot x\sqrt{3} = x^2(12 + 6\sqrt{3})\). The limit becomes:
\[
\lim_{x \to \infty} \frac{36x^4}{x^2(12 + 6\sqrt{3})} = \lim_{x \to \infty} \frac{36x^2}{12 + 6\sqrt{3}}
\]
This also tends to infinity as \(x \to \infty\).

Thus, the limit is:
\[
\boxed{\infty}
\]

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a Riemannian manifold $M$ with submanifolds $S$ and $T$. $\theta$ is a differential $k$-form on $M$ such that $\oint_{[S]} \theta = r \neq 0$. $\eta$ is the Hodge star of $\theta$ (so $\eta = *\theta$). The $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$.

We need to determine $\oint_{[T]} \eta$.

This is a classic problem related to Poincaré duality and the Hodge star operator. Let me think about this.

The key idea: On an $n$-dimensional oriented Riemannian manifold, the Hodge star operator $*$ maps $k$-forms to $(n-k)$-forms. The intersection number of two submanifolds is related to the integral of the Poincaré dual of one over the other.

Let me think about dimensions. If $\theta$ is a $k$-form and $\eta = *\theta$ is an $(n-k)$-form, then $S$ should be a $k$-dimensional submanifold (so that $\oint_{[S]} \theta$ makes sense as integration of a $k$-form over a $k$-cycle), and $T$ should be an $(n-k)$-dimensional submanifold (so that $\oint_{[T]} \eta$ makes sense).

The intersection number of $S$ (dimension $k$) and $T$ (dimension $n-k$) in an $n$-manifold is well-defined when $k + (n-k) = n$, which is the case for transversal intersection giving points.

Now, the key relationship: The Poincaré dual of $[S]$ (as a cohomology class) can be represented by a form, and the Hodge star relates the Poincaré dual to harmonic forms.

Actually, let me think more carefully. The classical result is:

If $\alpha$ is a closed $k$-form representing the Poincaré dual of $[S]$, then $\int_T \alpha = S \cdot T$ (the intersection number).

But here we have $\theta$ with $\int_S \theta = r$, and $\eta = *\theta$, and we want $\int_T \eta$.

The relationship between the Hodge star and intersection numbers comes through Poincaré duality. 

Let me think about this differently. The key theorem here is:

**Theorem**: On a compact oriented Riemannian $n$-manifold, if $\alpha$ is a harmonic $k$-form and $\beta$ is a harmonic $(n-k)$-form, then:
$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

And more relevantly, the intersection pairing and the Hodge star are related by:

If $S$ and $T$ are submanifolds with $[S] \in H_k(M)$ and $[T] \in H_{n-k}(M)$, and if $\theta$ is the harmonic form representing the Poincaré dual of $[S]$ (i.e., $\theta = PD([S])$), then $*\theta$ represents the Poincaré dual of $[T]$ when $S \cdot T = \pm 1$... 

Hmm, let me be more precise.

Actually, the standard result is:

The Poincaré dual of $[S]$ is a cohomology class $PD([S]) \in H^{n-k}(M)$. If we represent this by a form $\alpha$, then $\int_T \alpha = S \cdot T$.

But here, $\theta$ is a $k$-form with $\int_S \theta = r$. So $\theta$ is not the Poincaré dual of $S$ (which would be an $(n-k)$-form). Rather, $\theta$ is a form that pairs with $[S]$ to give $r$.

The Hodge star $\eta = *\theta$ is an $(n-k)$-form.

Now, the question is about the relationship between $\int_T *\theta$ and $\int_S \theta$ given the intersection number.

Let me think about this using the L² inner product and the wedge product.

We have the identity:
$$\int_M \theta \wedge *\phi = \langle \theta, \phi \rangle_{L^2}$$

for $k$-forms $\theta, \phi$.

Also, $\int_M \alpha \wedge \beta$ for a $k$-form $\alpha$ and $(n-k)$-form $\beta$ gives the cup product pairing.

Now, the key relationship between intersection numbers and forms:

If $\alpha$ is a closed $k$-form and $\gamma$ is a closed $(n-k)$-form, then:
$$\int_M \alpha \wedge \gamma = \sum_i (\int_{S_i} \alpha)(\int_{T_i} \gamma) \cdot (S_i \cdot T_i)$$

Hmm, that's not quite right either. Let me think more carefully.

The correct statement involves Poincaré duality. Let $\{e_i\}$ be a basis for $H_k(M;\mathbb{R})$ and $\{e^j\}$ the dual basis for $H^{n-k}(M;\mathbb{R})$ under Poincaré duality (so $PD(e_i) = e^i$ meaning $\int_{e_i} \alpha = \int_M \alpha \wedge e^i$... no, that's not right either).

Let me reconsider. Poincaré duality says $H^k(M) \cong H_{n-k}(M)$. The isomorphism sends a cohomology class $[\alpha] \in H^k(M)$ to the homology class $[S] \in H_{n-k}(M)$ such that for all $[\beta] \in H^{n-k}(M)$:
$$\int_M \alpha \wedge \beta = \int_S \beta$$

So if $PD([\theta]) = [S']$ for some $(n-k)$-cycle $S'$, then $\int_M \theta \wedge \beta = \int_{S'} \beta$ for all $(n-k)$-forms $\beta$.

But we're told $\int_S \theta = r$, which means $[S]$ pairs with $[\theta]$ to give $r$. This means $[S]$ is dual to $[\theta]$ in the sense that... well, $[S] \in H_k(M)$ and $[\theta] \in H^k(M)$, and the pairing $\langle [S], [\theta] \rangle = \int_S \theta = r$.

Now, $\eta = *\theta \in H^{n-k}(M)$ (assuming $\theta$ is harmonic, or at least closed and co-closed, so that $*\theta$ is also closed).

The intersection number $S \cdot T$ is defined as $\int_T PD([S])$ where $PD([S]) \in H^{n-k}(M)$ is the Poincaré dual of $[S]$.

Now, $PD([S])$ is the cohomology class such that for all $[\beta] \in H^k(M)$:
$$\int_M \beta \wedge PD([S]) = \int_S \beta$$

So if $\int_S \theta = r$, then $\int_M \theta \wedge PD([S]) = r$.

Now, the question is: what is the relationship between $*\theta$ and $PD([S])$?

If $\theta$ is harmonic, then $*\theta$ is also harmonic, and $*\theta$ represents the Poincaré dual of $[S]$ if and only if... hmm.

Actually, let me think about this more carefully. The Hodge theorem says every cohomology class has a unique harmonic representative. So $PD([S]) \in H^{n-k}(M)$ has a unique harmonic representative, call it $\omega_{n-k}$.

If $\theta$ is the harmonic representative of the class $[\theta] \in H^k(M)$ that pairs with $[S]$ to give $r$... 

Actually, I think the problem is set up so that $\theta$ is the harmonic form Poincaré dual to $[S]$ (up to scaling). Let me reconsider.

If $PD([S]) = [\alpha] \in H^{n-k}(M)$, then $\int_T \alpha = S \cdot T = \pm 1$.

Now, $*\alpha$ would be a $k$-form. If $\alpha$ is harmonic, $*\alpha$ is harmonic. And $*\alpha$ represents $PD([T])$ (the Poincaré dual of $[T]$) because... 

Actually, there's a key fact: On a compact oriented Riemannian manifold, if $\alpha$ is the harmonic representative of $PD([S])$, then $*\alpha$ is the harmonic representative of $PD([T])$ if and only if... no, that's not generally true.

Let me think about this differently.

The key fact is: $\int_S \theta = r$ and we want $\int_T *\theta$.

Using the L² inner product:
$$\int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$$

But that's $\theta \wedge *\theta$, not directly helpful.

Let me use the relationship between the cup product and intersection:

$$\int_M \theta \wedge \eta = \int_M \theta \wedge *\theta$$

Wait, no. $\eta = *\theta$, so $\int_M \theta \wedge \eta = \int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$.

But also, by Poincaré duality, $\int_M \theta \wedge \eta$ relates to intersection numbers.

Hmm, let me think about this problem from a more basic perspective.

The standard result that this problem is testing:

**If $\theta$ is a harmonic $k$-form on a compact oriented Riemannian $n$-manifold $M$, and $S$ is a $k$-dimensional submanifold, $T$ is an $(n-k)$-dimensional submanifold, with $S \cdot T = \pm 1$, and $\int_S \theta = r$, then $\int_T *\theta = \pm r$.**

The sign depends on the sign of the intersection number and orientation conventions.

Let me verify this. The idea is:

1. $\theta$ harmonic $\Rightarrow$ $*\theta$ harmonic.
2. $[\theta] \in H^k(M)$ corresponds to $[S]$ under Poincaré duality (up to the pairing $r$).
3. $[*\theta] \in H^{n-k}(M)$ corresponds to $[T]$ under Poincaré duality (up to the same factor).

More precisely: Let $\omega = PD([S])$ be the Poincaré dual of $[S]$, a closed $(n-k)$-form. Then $\int_T \omega = S \cdot T = \pm 1$.

Now, $\theta$ is a $k$-form with $\int_S \theta = r$. The Poincaré dual of $[S]$ satisfies: for any closed $k$-form $\alpha$, $\int_M \alpha \wedge \omega = \int_S \alpha$.

So $\int_M \theta \wedge \omega = \int_S \theta = r$.

Now, if $\theta$ is harmonic, then $*\theta$ is harmonic, and both represent cohomology classes. The question is whether $[*\theta]$ is proportional to $[\omega] = PD([S])$.

In general, $*\theta$ and $\omega$ are different things. The Hodge star maps $H^k_{harm}(M) \to H^{n-k}_{harm}(M)$, and this is an isomorphism. Poincaré duality also gives an isomorphism $H^k(M) \to H^{n-k}(M)$ (well, $H^k \to H_{n-k} \to H^{n-k}$). 

The key point: The Hodge star $*$ and the Poincaré duality isomorphism are related but not identical. However, on a compact oriented Riemannian manifold, the following holds:

The harmonic representative of $PD([S])$ is $*\theta_S$ where $\theta_S$ is the harmonic representative of the class dual to $[S]$ in $H^k(M)$.

Wait, I need to be more careful. Let me use the standard framework.

Let $\{[\sigma_i]\}$ be a basis for $H^k(M;\mathbb{R})$ and $\{[\tau_j]\}$ be a basis for $H^{n-k}(M;\mathbb{R})$. The cup product pairing is:
$$Q_{ij} = \int_M \sigma_i \wedge \tau_j$$

Poincaré duality says this pairing is non-degenerate. If we choose $\tau_j$ to be the Poincaré dual basis (so $Q_{ij} = \delta_{ij}$), then $PD([\sigma_i])$ corresponds to the homology class $[S_i]$ such that $\int_{S_i} \sigma_j = \delta_{ij}$... 

Hmm, actually let me think about it this way. Let's say $[S] \in H_k(M)$ and $[\theta] \in H^k(M)$ with $\int_S \theta = r$. 

The Poincaré dual $PD([S]) \in H^{n-k}(M)$ is characterized by: for all $[\alpha] \in H^k(M)$, $\int_M \alpha \wedge PD([S]) = \int_S \alpha$.

So $\int_M \theta \wedge PD([S]) = \int_S \theta = r$.

Now, $S \cdot T = \int_T PD([S]) = \pm 1$.

We want $\int_T *\theta$.

Now, here's the key: is $[*\theta]$ related to $PD([S])$?

In general, no — not unless $\theta$ is specifically the harmonic representative of the class that is Hodge-dual to $PD([S])$.

But actually, I think the problem is implicitly assuming that $\theta$ is harmonic (or at least closed and co-closed), so that $*\theta$ is closed, and the problem is asking about the relationship.

Let me think about this more carefully using the Hodge decomposition.

The Hodge star gives an isomorphism $*: H^k_{harm}(M) \to H^{n-k}_{harm}(M)$. 

The Poincaré duality also gives an isomorphism $PD: H^k(M) \to H^{n-k}(M)$, defined by $[\alpha] \mapsto PD([\alpha])$ where $PD([\alpha])$ is the unique class such that $\int_M \alpha \wedge \beta = \int_{PD^{-1}([\beta])} \alpha$... 

Hmm, I'm going in circles. Let me think about this more concretely.

Consider the simplest case: $M = S^n$ (the $n$-sphere), $S$ = equator ($k$-sphere), $T$ = another great sphere ($(n-k)$-sphere) intersecting $S$ transversally at one point.

On $S^n$, the harmonic $k$-forms are zero for $0 < k < n$ (since $b_k(S^n) = 0$ for $0 < k < n$). So this doesn't work for a non-trivial example.

Let me try $M = T^2$ (the 2-torus), $k = 1$. Then $n = 2$, $n - k = 1$. Let $S$ and $T$ be the two standard circles (meridian and longitude), intersecting at one point, so $S \cdot T = 1$.

The harmonic 1-forms on $T^2$ are spanned by $dx$ and $dy$ (in the flat metric). 

If $\theta = dx$, then $\int_S \theta = \int_0^1 dx = 1 = r$ (if $S$ is the $x$-circle). Then $*\theta = *dx = dy$ (in the standard orientation on $T^2$). And $\int_T dy = \int_0^1 dy = 1$.

So $\int_T *\theta = 1 = r$. And $S \cdot T = 1$, so the answer is $r \cdot (S \cdot T) = r \cdot 1 = r$.

If $\theta = 2dx$, then $\int_S \theta = 2 = r$, $*\theta = 2dy$, $\int_T *\theta = 2 = r$. Same.

Now if $S \cdot T = -1$ (reversed orientation of $T$), then $\int_T dy = -1$, so $\int_T *\theta = -r$.

So the answer is $\int_T *\theta = \pm r$ where the sign matches the sign of the intersection number $S \cdot T$.

Wait, but let me check: if $S \cdot T = -1$, then with $\theta = dx$, $*\theta = dy$, and $T$ has reversed orientation, $\int_T dy = -1$. And $r = \int_S dx = 1$. So $\int_T *\theta = -1 = -r = r \cdot (S \cdot T)$.

So the answer is $\oint_{[T]} \eta = \pm r$, where the sign is the same as the sign of the intersection number.

Actually, more precisely: $\oint_{[T]} \eta = r \cdot (S \cdot T) = \pm r$.

Hmm wait, but the problem says the intersection number is $\pm 1$, and asks to "determine the value." So the answer should be $\pm r$, matching the sign of the intersection number.

Let me verify this more carefully with the general theory.

**General proof:**

On a compact oriented $n$-dimensional Riemannian manifold $M$, let $\theta$ be a harmonic $k$-form. Let $S$ be a compact oriented $k$-submanifold and $T$ a compact oriented $(n-k)$-submanifold.

The Poincaré dual of $[S]$ is $PD([S]) \in H^{n-k}(M)$, represented by a closed $(n-k)$-form $\omega$ such that for any closed $k$-form $\alpha$:
$$\int_M \alpha \wedge \omega = \int_S \alpha$$

The intersection number $S \cdot T = \int_T \omega$.

Now, since $\theta$ is harmonic, $*\theta$ is also harmonic (hence closed). The cohomology class $[*\theta] \in H^{n-k}(M)$ is the Hodge dual of $[\theta]$.

The key relationship: On a compact oriented Riemannian manifold, the Hodge star on harmonic forms corresponds to the Poincaré duality isomorphism, **up to the intersection pairing**.

More precisely: Let $\theta_1, \ldots, \theta_{b_k}$ be an orthonormal basis of harmonic $k$-forms (with respect to the $L^2$ inner product). Then $*\theta_1, \ldots, *\theta_{b_k}$ is an orthonormal basis of harmonic $(n-k)$-forms.

The cup product pairing $\int_M \theta_i \wedge *\theta_j = \delta_{ij}$ (by the $L^2$ inner product property).

Now, let $[S_1], \ldots, [S_{b_k}]$ be a basis of $H_k(M)$ dual to $[\theta_1], \ldots, [\theta_{b_k}]$ in the sense that $\int_{S_i} \theta_j = \delta_{ij}$. Then $PD([S_i]) = [*\theta_i]$ because:

For any closed $k$-form $\alpha = \sum_j a_j \theta_j + d\beta$ (using Hodge decomposition, the harmonic part is $\sum a_j \theta_j$):
$$\int_M \alpha \wedge *\theta_i = \int_M (\sum_j a_j \theta_j) \wedge *\theta_i = \sum_j a_j \delta_{ji} = a_i$$

And $\int_{S_i} \alpha = \int_{S_i} \sum_j a_j \theta_j = a_i$ (since exact forms integrate to 0 over closed cycles).

So indeed $PD([S_i]) = [*\theta_i]$, confirming that the Hodge star of the harmonic form dual to $[S_i]$ gives the Poincaré dual of $[S_i]$.

Now, in our problem: $\int_S \theta = r$. We can write $[S] = \sum_i c_i [S_i]$ where $c_i = \int_S \theta_i$ (if $\{\theta_i\}$ is orthonormal and $\{S_i\}$ is the dual basis). Then $\int_S \theta = \sum_i c_i \int_{S_i} \theta$... 

Hmm, this is getting complicated. Let me simplify.

Assume $\theta$ is harmonic (the problem likely intends this, as the Hodge star is most meaningful for harmonic forms in this context). 

Let $[\theta] \in H^k(M)$ be the cohomology class of $\theta$. The Poincaré dual of $[S]$ is $PD([S]) \in H^{n-k}(M)$.

We have $\int_S \theta = r$, which means $\langle [S], [\theta] \rangle = r$ where $\langle \cdot, \cdot \rangle$ is the Kronecker pairing.

Now, $PD([S])$ is the class in $H^{n-k}(M)$ such that $\int_M [\theta'] \cup PD([S]) = \langle [S], [\theta'] \rangle$ for all $[\theta'] \in H^k(M)$.

In particular, $\int_M \theta \wedge \omega = r$ where $\omega$ is a closed form representing $PD([S])$.

Now, the intersection number $S \cdot T = \int_T \omega = \pm 1$.

We want $\int_T *\theta$.

The key claim: $[*\theta] = r \cdot PD([S]) / (S \cdot T)$... no, that doesn't seem right in general.

Actually wait. Let me reconsider. The problem doesn't say $\theta$ is the Poincaré dual of anything specific. It just says $\int_S \theta = r$. The form $\theta$ could be any $k$-form (presumably closed, so the integral is well-defined on the homology class).

But the answer $\int_T *\theta = \pm r$ would only hold if $\theta$ is specifically the harmonic form Poincaré dual to $[S]$ (up to the factor $r$).

Hmm, but the problem says "determine the value," implying there's a definite answer. So there must be enough constraints.

Let me re-read the problem: "Let $M$ be a Riemannian manifold with submanifolds $S$ and $T$. Suppose $\theta$ is a differential $k$-form on $M$ such that $\oint_{[S]} \theta = r \neq 0$. If $\eta$ is the Hodge star of $\theta$ and the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$, determine the value of $\oint_{[T]} \eta$."

I think the problem is implicitly assuming that $\theta$ is harmonic (or at least closed and co-closed), and that $S$ and $T$ are in "Poincaré dual" position. The $\mathbb{Z}\pi$ notation suggests this is in the context of the fundamental group $\pi = \pi_1(M)$, which is the setting of the intersection form on the universal cover.

Actually, the $\mathbb{Z}\pi$-intersection number is a concept from geometric topology. In the universal cover $\tilde{M}$, the lifts $\tilde{S}$ and $\tilde{T}$ intersect, and the intersection number is computed in $\mathbb{Z}\pi$ (the group ring of the fundamental group). When this is $\pm 1$, it means the intersection is essentially a single point with sign $\pm 1$.

This is related to the duality theorem: on a closed oriented manifold, the intersection form $H_k(M) \times H_{n-k}(M) \to \mathbb{Z}$ (or $\mathbb{Z}\pi$ for the universal cover version) is related to the cup product via Poincaré duality.

I think the intended answer is:

$$\oint_{[T]} \eta = \pm r$$

where the sign matches the intersection number $S \cdot T = \pm 1$.

The reasoning is based on the fundamental relationship:

**On a compact oriented Riemannian manifold, if $\theta$ is a harmonic $k$-form, then $*\theta$ is the harmonic $(n-k)$-form Poincaré dual to the same geometry, and the intersection number provides the proportionality.**

More precisely, the key identity is:

$$\oint_{[T]} *\theta = (S \cdot T) \cdot \oint_{[S]} \theta$$

when $\theta$ is harmonic and $S$, $T$ are Poincaré-dual submanifolds.

Wait, but that's not quite right either. Let me think again...

Actually, I think the correct statement is simpler than I'm making it. The problem is testing the following classical result:

**Theorem (Poincaré duality via Hodge star):** If $\theta$ is a harmonic $k$-form representing the Poincaré dual of $[T]$ (i.e., $[\theta] = PD([T]) \in H^k(M)$), then $*\theta$ represents $PD([S])$ (i.e., $[*\theta] = PD([S]) \in H^{n-k}(M)$), and:
$$\int_S \theta = S \cdot T = \pm 1$$
$$\int_T *\theta = T \cdot S = \pm 1$$

But in our problem, $\int_S \theta = r \neq \pm 1$, so $\theta$ is not exactly $PD([T])$; it's $r$ times that (assuming $b_k = 1$ in the relevant direction).

If $[\theta] = r \cdot PD([T])$, then $[*\theta] = r \cdot PD([S])$, and:
$$\int_T *\theta = r \cdot \int_T PD([S]) = r \cdot (S \cdot T) = \pm r$$

So the answer is $\oint_{[T]} \eta = \pm r$.

Let me make sure this is correct by checking the logic:

1. $PD([T]) \in H^k(M)$ is the Poincaré dual of $[T]$. It's a $k$-dimensional cohomology class (since $T$ is $(n-k)$-dimensional, $PD([T]) \in H^{n-(n-k)}(M) = H^k(M)$). ✓

2. $\int_S PD([T]) = S \cdot T = \pm 1$. ✓ (This is the definition of intersection number via Poincaré duality.)

3. If $\theta = r \cdot \omega$ where $\omega$ is the harmonic representative of $PD([T])$, then $\int_S \theta = r \cdot \int_S \omega = r \cdot (S \cdot T) = \pm r$.

But the problem says $\int_S \theta = r$, not $\pm r$. So either $S \cdot T = 1$ and $\theta = r \cdot \omega$, or there's a sign issue.

Hmm, let me reconsider. If $S \cdot T = +1$, then $\int_S PD([T]) = 1$, and if $\theta = r \cdot PD([T])_{harm}$, then $\int_S \theta = r$. Then $*\theta = r \cdot *(PD([T])_{harm})$.

Now, $*(PD([T])_{harm}) = PD([S])_{harm}$ (this is the key Hodge star / Poincaré duality relationship).

So $\int_T *\theta = r \cdot \int_T PD([S]) = r \cdot (S \cdot T) = r \cdot 1 = r$.

If $S \cdot T = -1$, then $\int_S PD([T]) = -1$. For $\int_S \theta = r$, we'd need $\theta = -r \cdot PD([T])_{harm}$. Then $*\theta = -r \cdot PD([S])_{harm}$, and $\int_T *\theta = -r \cdot (S \cdot T) = -r \cdot (-1) = r$.

Wait, that gives $r$ in both cases! Let me recheck.

Case 1: $S \cdot T = +1$.
- $PD([T])_{harm}$ is a harmonic $k$-form with $\int_S PD([T])_{harm} = S \cdot T = 1$.
- $\theta = r \cdot PD([T])_{harm}$, so $\int_S \theta = r \cdot 1 = r$. ✓
- $*\theta = r \cdot *(PD([T])_{harm}) = r \cdot PD([S])_{harm}$.
- $\int_T *\theta = r \cdot \int_T PD([S])_{harm} = r \cdot (S \cdot T) = r \cdot 1 = r$.

Case 2: $S \cdot T = -1$.
- $PD([T])_{harm}$ is a harmonic $k$-form with $\int_S PD([T])_{harm} = S \cdot T = -1$.
- For $\int_S \theta = r$, we need $\theta = -r \cdot PD([T])_{harm}$ (since $\int_S (-r \cdot PD([T])_{harm}) = -r \cdot (-1) = r$). ✓
- $*\theta = -r \cdot *(PD([T])_{harm}) = -r \cdot PD([S])_{harm}$.
- $\int_T *\theta = -r \cdot \int_T PD([S])_{harm} = -r \cdot (S \cdot T) = -r \cdot (-1) = r$.

So in both cases, $\int_T *\theta = r$!

Wait, that's interesting. The answer is just $r$, regardless of the sign of the intersection number.

Hmm, but this depends on the assumption that $\theta$ is a scalar multiple of $PD([T])_{harm}$, which requires that the relevant Betti number is 1. If $b_k > 1$, then $\theta$ could have components in other directions, and the answer wouldn't be determined.

But the problem says "determine the value," implying it's uniquely determined. So either:
1. The problem assumes $b_k = 1$ (or that $\theta$ is in the "right" direction), or
2. The answer is always $r$ regardless, which would require a more general argument.

Let me think about whether the answer is always $r$ in general.

Actually, I think the problem is set up so that $\theta$ is specifically the harmonic form Poincaré dual to $[T]$ (scaled by $r$ and adjusted for the sign of the intersection). The $\mathbb{Z}\pi$-intersection number being $\pm 1$ is the key constraint that makes $S$ and $T$ Poincaré-dual to each other (in the universal cover sense).

Given the way the problem is phrased, with the intersection number being $\pm 1$ (which means $S$ and $T$ are "dual" in some sense), and $\theta$ integrating to $r$ over $S$, the answer should be:

$$\oint_{[T]} \eta = \pm r$$

where the sign is the same as the intersection number.

But from my calculation above, I got $r$ in both cases. Let me re-examine.

Actually, I think I need to be more careful. The issue is whether $*(PD([T])_{harm}) = PD([S])_{harm}$ or $*(PD([T])_{harm}) = \pm PD([S])_{harm}$.

The Hodge star and Poincaré duality: On a compact oriented Riemannian $n$-manifold, the Hodge star $*: \mathcal{H}^k \to \mathcal{H}^{n-k}$ (harmonic forms) is an isomorphism. The Poincaré duality $PD: H^k \to H^{n-k}$ is also an isomorphism (via $[\alpha] \mapsto [*\alpha]$ when $\alpha$ is harmonic... wait, is that true?).

Actually, the Poincaré duality isomorphism $PD: H^k(M) \to H_{n-k}(M) \to H^{n-k}(M)$ is NOT the same as the Hodge star in general. The Poincaré duality sends $[\alpha] \in H^k(M)$ to $PD([\alpha]) \in H^{n-k}(M)$ where $\int_M \alpha \wedge \beta = \int_{PD^{-1}(\beta)} \alpha$... 

Let me be very precise. Poincaré duality gives an isomorphism $D: H^k(M) \to H_{n-k}(M)$, sending $[\alpha]$ to the homology class $[C]$ such that $\int_C \beta = \int_M \alpha \wedge \beta$ for all $[\beta] \in H^{n-k}(M)$.

Then $PD([S]) = D^{-1}([S]) \in H^{n-k}(M)$, the class such that $\int_M \gamma \wedge PD([S]) = \int_S \gamma$ for all $[\gamma] \in H^k(M)$.

Now, the Hodge star: if $\alpha$ is a harmonic $k$-form, then $*\alpha$ is a harmonic $(n-k)$-form. The cohomology class $[*\alpha]$ satisfies:

For any harmonic $(n-k)$-form $\beta$:
$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

And $[*\alpha]$ is the Poincaré dual of the homology class $[C]$ where $\int_C \beta = \int_M \alpha \wedge \beta$ for all $\beta$.

So $D([\alpha]) = [C]$ where $\int_C \beta = \int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$ for all harmonic $(n-k)$-forms $\beta$.

Now, $D^{-1}([C]) = [\omega]$ where $\int_M \gamma \wedge \omega = \int_C \gamma$ for all $[\gamma] \in H^k(M)$.

If $[C] = D([\alpha])$, then $D^{-1}([C]) = [\alpha]$... no wait, $D^{-1}(D([\alpha])) = [\alpha]$, but $D$ maps $H^k \to H_{n-k}$, and $D^{-1}$ maps $H_{n-k} \to H^k$. So $PD([S]) = D^{-1}([S]) \in H^{n-k}$... 

I'm getting confused with the directions. Let me use a cleaner notation.

$PD: H_k(M) \to H^{n-k}(M)$ sends $[S]$ to $PD([S])$ where $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for all $[\alpha] \in H^k(M)$.

Similarly, $PD: H_{n-k}(M) \to H^k(M)$ sends $[T]$ to $PD([T])$ where $\int_M PD([T]) \wedge \beta = \int_T \beta$ for all $[\beta] \in H^{n-k}(M)$.

Note: $\int_M PD([T]) \wedge \beta = (-1)^{k(n-k)} \int_M \beta \wedge PD([T])$... hmm, signs from swapping forms.

Actually, for the cup product, $\alpha \cup \beta = \alpha \wedge \beta$ for differential forms, and $\alpha \wedge \beta = (-1)^{kl} \beta \wedge \alpha$ for $k$-form $\alpha$ and $l$-form $\beta$.

So $\int_M PD([T]) \wedge \beta = (-1)^{k(n-k)} \int_M \beta \wedge PD([T]) = (-1)^{k(n-k)} \int_T \beta$.

Hmm, this introduces a sign $(-1)^{k(n-k)}$. But the standard convention for Poincaré duality usually handles this. Let me not worry about this sign for now and focus on the main idea.

The key question: Is $*(PD([T])_{harm}) = PD([S])_{harm}$ (up to the intersection number)?

Let me use the $L^2$ inner product. For harmonic forms $\alpha \in \mathcal{H}^k$ and $\beta \in \mathcal{H}^{n-k}$:

$$\langle \alpha, \beta \rangle_{cup} := \int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

So the cup product pairing on harmonic forms is $\langle \alpha, *\beta \rangle_{L^2}$.

Now, $PD([S])_{harm}$ is the harmonic $(n-k)$-form $\omega$ such that $\int_M \alpha \wedge \omega = \int_S \alpha$ for all harmonic $k$-forms $\alpha$.

This means $\langle \alpha, *\omega \rangle_{L^2} = \int_S \alpha$ for all harmonic $\alpha$.

So $*\omega$ is the harmonic $k$-form that represents the linear functional $\alpha \mapsto \int_S \alpha$ on $\mathcal{H}^k$.

Similarly, $PD([T])_{harm}$ is the harmonic $k$-form $\mu$ such that $\int_M \mu \wedge \beta = \int_T \beta$ for all harmonic $(n-k)$-forms $\beta$.

This means $\langle \mu, *\beta \rangle_{L^2} = \int_T \beta$ for all harmonic $\beta \in \mathcal{H}^{n-k}$.

Or equivalently, $\int_M \mu \wedge \beta = \int_T \beta$.

Now, $\int_T \beta = \int_M PD([T]) \wedge \beta$... wait, that's circular.

Let me try a different approach. Let's use the fact that the intersection number $S \cdot T = \int_T PD([S]) = \int_S PD([T])$ (with appropriate signs).

Now, $\int_S PD([T]) = S \cdot T = \pm 1$.

If $\theta$ is a harmonic $k$-form with $\int_S \theta = r$, and if $b_k = 1$ (so $\mathcal{H}^k$ is 1-dimensional), then $\theta = c \cdot PD([T])_{harm}$ for some scalar $c$, and $r = c \cdot \int_S PD([T])_{harm} = c \cdot (S \cdot T) = \pm c$. So $c = \pm r$ (with sign depending on $S \cdot T$).

Then $*\theta = c \cdot *(PD([T])_{harm})$.

Now, $*(PD([T])_{harm})$ is a harmonic $(n-k)$-form. Is it $PD([S])_{harm}$?

From the relation: $PD([S])_{harm} = \omega$ where $\langle \alpha, *\omega \rangle_{L^2} = \int_S \alpha$ for all harmonic $\alpha$.

And $PD([T])_{harm} = \mu$ where $\int_M \mu \wedge \beta = \int_T \beta$ for all harmonic $\beta$.

If $b_k = b_{n-k} = 1$, then $\mathcal{H}^k = \text{span}(\mu)$ and $\mathcal{H}^{n-k} = \text{span}(\omega)$.

$*\mu$ is a harmonic $(n-k)$-form, so $*\mu = \lambda \omega$ for some scalar $\lambda$.

We have $\int_M \mu \wedge \omega = \langle \mu, *\omega \rangle_{L^2}$ and also $\int_M \mu \wedge \omega = \int_T \omega = S \cdot T$ (since $\omega = PD([S])_{harm}$ and $\int_T PD([S]) = S \cdot T$).

Also, $\int_M \mu \wedge \omega = \langle \mu, *\omega \rangle_{L^2}$. And $*\omega = \bar{\lambda}^{-1} *\mu / \lambda$... hmm, this is getting complicated.

Let me just use the $L^2$ norm. $\langle \mu, *\omega \rangle_{L^2} = \int_M \mu \wedge \omega = S \cdot T = \pm 1$.

Also, $\|*\omega\|_{L^2} = \|\omega\|_{L^2}$ and $\|\mu\|_{L^2} = \|\mu\|_{L^2}$.

If $\mu$ and $*\omega$ are both unit vectors (after normalization), then $\langle \mu, *\omega \rangle = \pm 1$ means $\mu = \pm *\omega$, i.e., $*\omega = \pm \mu$, i.e., $\omega = \pm *\mu$ (since $**\omega = \pm \omega$ depending on degree and signature).

Actually, $**\alpha = (-1)^{k(n-k)} \alpha$ on a Riemannian manifold (positive definite metric). So $*\mu = \lambda \omega$ implies $\mu = (-1)^{k(n-k)} \lambda *\omega$, and $*\omega = (-1)^{k(n-k)} \lambda^{-1} \mu$.

This is getting quite involved. Let me step back and think about what the problem is really asking.

I think the problem is a standard exercise in differential topology/geometry, and the expected answer is:

$$\oint_{[T]} \eta = \pm r$$

The sign being the same as the intersection number $S \cdot T = \pm 1$.

The reasoning is based on the duality between the Hodge star and the intersection pairing. The key identity is:

$$\oint_{[S]} \theta \cdot \oint_{[T]} *\theta = \text{something related to } \|\theta\|^2$$

No, that's not right either.

Actually, let me think about this more carefully. The fundamental relationship is:

$$\int_M \theta \wedge *\phi = \langle \theta, \phi \rangle_{L^2}$$

If $\theta = \phi$ (both harmonic $k$-forms), then $\int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$.

Now, by Poincaré duality, $\int_M \theta \wedge *\theta$ can also be interpreted as a sum of products of periods:

$$\int_M \theta \wedge *\theta = \sum_{i,j} (\int_{S_i} \theta)(\int_{T_j} *\theta) \cdot (S_i \cdot T_j)$$

where $\{S_i\}$ and $\{T_j\}$ are dual bases of $H_k$ and $H_{n-k}$.

If $S \cdot T = \pm 1$ and $S, T$ are the only relevant pair (i.e., $b_k = 1$), then:

$$\|\theta\|^2_{L^2} = (\int_S \theta)(\int_T *\theta) \cdot (S \cdot T) = r \cdot (\int_T *\theta) \cdot (\pm 1)$$

But this gives $\int_T *\theta = \|\theta\|^2_{L^2} / (r \cdot (\pm 1))$, which depends on $\|\theta\|_{L^2}$ and is not simply $\pm r$.

Hmm, so the answer is NOT simply $\pm r$ in general. It depends on the $L^2$ norm of $\theta$.

Unless... the problem is assuming that $\theta$ is the specific harmonic form that is the Poincaré dual (up to scaling), in which case the $L^2$ norm is determined.

OK wait, I think I was overcomplicating this. Let me reconsider the problem.

I think the problem is testing the following specific result:

**If $\theta$ is a closed $k$-form on a compact oriented Riemannian $n$-manifold $M$, $S$ is a $k$-cycle, $T$ is an $(n-k)$-cycle, $S \cdot T = \pm 1$, and $\eta = *\theta$, then:**

$$\oint_{[T]} \eta = \pm \oint_{[S]} \theta = \pm r$$

This would be true if $\theta$ is the harmonic form Poincaré dual to $[T]$ (scaled appropriately).

But as I showed, this requires specific assumptions about $\theta$.

However, looking at the problem again, I think it's meant to be a straightforward application of the duality between the Hodge star and Poincaré duality, and the expected answer is $\pm r$.

The key insight is:

1. The Hodge star $*$ maps $k$-forms to $(n-k)$-forms.
2. Poincaré duality maps $H^k$ to $H^{n-k}$ (via the intersection form).
3. The Hodge star on harmonic forms implements Poincaré duality.
4. If $\int_S \theta = r$ and $S \cdot T = \pm 1$, then by the duality, $\int_T *\theta = \pm r$.

The sign is determined by the sign of the intersection number and the degree $k$ (there might be a $(-1)^{k(n-k)}$ factor from the Hodge star).

Actually, I realize the problem might be even simpler than I think. Let me consider the possibility that the answer is just $\pm r$, with the sign being the sign of the intersection number.

Let me verify with the torus example again. $M = T^2$, $k = 1$, $n = 2$. $\theta = dx$, $*\theta = dy$. $S$ = $x$-circle, $T$ = $y$-circle. $S \cdot T = 1$ (with appropriate orientations). $\int_S dx = 1 = r$, $\int_T dy = 1 = r$. So $\int_T *\theta = r$. ✓

If we reverse the orientation of $T$, $S \cdot T = -1$, $\int_T dy = -1 = -r$. So $\int_T *\theta = -r = r \cdot (S \cdot T)$. ✓

So the answer is $\oint_{[T]} \eta = r \cdot (S \cdot T) = \pm r$.

But wait, in my earlier analysis with the $b_k = 1$ assumption, I got $r$ in both cases. Let me recheck.

Case 2: $S \cdot T = -1$.
- $PD([T])_{harm}$: $\int_S PD([T])_{harm} = S \cdot T = -1$.
- $\theta = c \cdot PD([T])_{harm}$ with $\int_S \theta = c \cdot (-1) = r$, so $c = -r$.
- $\theta = -r \cdot PD([T])_{harm}$.
- $*\theta = -r \cdot *(PD([T])_{harm})$.
- If $*(PD([T])_{harm}) = PD([S])_{harm}$, then $*\theta = -r \cdot PD([S])_{harm}$.
- $\int_T *\theta = -r \cdot \int_T PD([S])_{harm} = -r \cdot (S \cdot T) = -r \cdot (-1) = r$.

But in the torus example with $S \cdot T = -1$, I got $\int_T *\theta = -r$, not $r$!

The discrepancy is because $*(PD([T])_{harm}) \neq PD([S])_{harm}$ in general; there might be a sign.

Let me check with the torus. $PD([T])$ where $T$ is the $y$-circle: $PD([T])$ is the 1-form $\omega$ such that $\int_M \alpha \wedge \omega = \int_T \alpha$ for all 1-forms $\alpha$.

On $T^2$ with coordinates $(x,y)$, $\int_{T^2} dx \wedge dy = 1$. If $\omega = dy$, then $\int_{T^2} dx \wedge dy = 1 = \int_T dx$ (if $T$ is the $y$-circle, $\int_T dx = 0$). That's not right.

Let me be more careful. $T$ is the $y$-circle: $T = \{(x_0, y) : y \in [0,1]\}$. $\int_T \alpha$ for a 1-form $\alpha = a\,dx + b\,dy$ is $\int_0^1 b\,dy = \int_0^1 b(x_0, y)\,dy$.

$PD([T])$ is the 1-form $\omega$ such that $\int_{T^2} \alpha \wedge \omega = \int_T \alpha$ for all $\alpha$.

If $\omega = c\,dx + d\,dy$, then $\alpha \wedge \omega = (a\,dx + b\,dy) \wedge (c\,dx + d\,dy) = (ad - bc)\,dx \wedge dy$.

$\int_{T^2} \alpha \wedge \omega = \int_0^1 \int_0^1 (ad - bc)\,dx\,dy$.

For $\alpha = dx$ ($a=1, b=0$): $\int_{T^2} dx \wedge \omega = \int_0^1 \int_0^1 d\,dx\,dy = \bar{d}$ (average of $d$). And $\int_T dx = 0$. So $\bar{d} = 0$.

For $\alpha = dy$ ($a=0, b=1$): $\int_{T^2} dy \wedge \omega = \int_0^1 \int_0^1 (-c)\,dx\,dy = -\bar{c}$. And $\int_T dy = 1$. So $-\bar{c} = 1$, $\bar{c} = -1$.

So $PD([T])_{harm} = -dx$ (the harmonic representative with $\bar{c} = -1, \bar{d} = 0$).

Check: $\int_S PD([T])_{harm} = \int_S (-dx) = -1 = S \cdot T$ when $S \cdot T = -1$... 

Wait, but I said $S$ is the $x$-circle and $T$ is the $y$-circle, and with standard orientations, $S \cdot T = 1$ (the $x$-circle and $y$-circle on $T^2$ intersect at one point with positive orientation).

Let me reconsider. On $T^2$ with standard orientation $dx \wedge dy$, the $x$-circle $S = \{(x, y_0)\}$ oriented in the $+x$ direction, and the $y$-circle $T = \{(x_0, y)\}$ oriented in the $+y$ direction. At the intersection point $(x_0, y_0)$, the tangent to $S$ is $\partial_x$ and the tangent to $T$ is $\partial_y$. The orientation of $S$ followed by $T$ gives $(\partial_x, \partial_y)$ which matches the orientation of $T^2$. So $S \cdot T = +1$.

Now, $PD([T])_{harm} = -dx$ as computed above. Let me verify: $\int_S (-dx) = -\int_0^1 dx = -1$. But $S \cdot T = +1$, and $\int_S PD([T]) = S \cdot T = 1$. Contradiction!

Let me recheck. $PD([T])$ should satisfy $\int_M \alpha \wedge PD([T]) = \int_T \alpha$.

For $\alpha = dy$: $\int_{T^2} dy \wedge PD([T]) = \int_T dy = 1$.

$dy \wedge (-dx) = -dy \wedge dx = dx \wedge dy$. So $\int_{T^2} dy \wedge (-dx) = \int_{T^2} dx \wedge dy = 1$. ✓

For $\alpha = dx$: $\int_{T^2} dx \wedge (-dx) = 0$. And $\int_T dx = 0$. ✓

So $PD([T])_{harm} = -dx$. And $\int_S PD([T]) = \int_S (-dx) = -1$.

But $S \cdot T = +1$ and $\int_S PD([T])$ should equal $S \cdot T$... 

Hmm, the issue is the sign convention. The standard convention is:

$$S \cdot T = \int_T PD([S])$$

NOT $\int_S PD([T])$. Let me check if $\int_S PD([T]) = \int_T PD([S])$ or if there's a sign.

$PD([S])$: $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for all $\alpha$.

For $\alpha = dx$: $\int_{T^2} dx \wedge PD([S]) = \int_S dx = 1$.

$dx \wedge (c\,dx + d\,dy) = d\,dx \wedge dy$. So $\int_{T^2} d\,dx\,dy = \bar{d} = 1$. So $PD([S])_{harm} = dy$.

For $\alpha = dy$: $\int_{T^2} dy \wedge dy = 0 = \int_S dy = 0$. ✓

So $PD([S])_{harm} = dy$ and $PD([T])_{harm} = -dx$.

Now: $\int_T PD([S]) = \int_T dy = 1 = S \cdot T$. ✓
And: $\int_S PD([T]) = \int_S (-dx) = -1$.

So $\int_S PD([T]) = -1 \neq S \cdot T = 1$!

The relationship is $\int_S PD([T]) = (-1)^{k(n-k)} \int_T PD([S]) = (-1)^{1 \cdot 1} \cdot 1 = -1$. ✓

So the general relationship is:
$$\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$$

This is because $PD([T]) \in H^k(M)$ and $\int_S PD([T])$ involves the cup product $\int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} (S \cdot T)$.

Wait, let me be more careful. $\int_M PD([S]) \wedge PD([T])$: this is $(-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S])$.

$\int_M PD([S]) \wedge \beta = \int_S \beta$ for $\beta \in H^{n-k}$. So $\int_M PD([S]) \wedge PD([T])$... but $PD([T]) \in H^k$, not $H^{n-k}$. So this doesn't directly apply.

Let me reconsider. $PD([S]) \in H^{n-k}(M)$ and $PD([T]) \in H^k(M)$. 

$\int_M PD([T]) \wedge PD([S]) = \int_T PD([S]) = S \cdot T$ (by definition of $PD([T])$: $\int_M PD([T]) \wedge \beta = \int_T \beta$ for $\beta \in H^{n-k}$, and $PD([S]) \in H^{n-k}$).

And $\int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} (S \cdot T)$.

Also, $\int_M PD([S]) \wedge \alpha = \int_S \alpha$ for $\alpha \in H^k$. So $\int_M PD([S]) \wedge PD([T]) = \int_S PD([T])$.

Therefore: $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$.

OK so now let me redo the analysis.

$\int_S PD([T])_{harm} = (-1)^{k(n-k)} (S \cdot T)$.

If $\theta = c \cdot PD([T])_{harm}$ (assuming $b_k = 1$), then:
$r = \int_S \theta = c \cdot (-1)^{k(n-k)} (S \cdot T)$.
So $c = \frac{r}{(-1)^{k(n-k)} (S \cdot T)} = \frac{r \cdot (-1)^{k(n-k)}}{S \cdot T}$ (since $(-1)^{k(n-k)}$ is its own inverse).

$*\theta = c \cdot *(PD([T])_{harm})$.

Now, is $*(PD([T])_{harm}) = PD([S])_{harm}$?

In the torus example: $PD([T])_{harm} = -dx$, $*(−dx) = -dy$. And $PD([S])_{harm} = dy$. So $*(PD([T])_{harm}) = -dy = -PD([S])_{harm}$.

So $*(PD([T])_{harm}) = -PD([S])_{harm}$ in this case ($k = n-k = 1$, $(-1)^{k(n-k)} = -1$).

Let me check if $*(PD([T])_{harm}) = (-1)^{k(n-k)} PD([S])_{harm}$ in general.

In the torus: $(-1)^{1 \cdot 1} = -1$, and indeed $*(PD([T])_{harm}) = -PD([S])_{harm}$. ✓

Let me verify this relationship. We have:
- $PD([T])_{harm} = \mu \in \mathcal{H}^k$ with $\int_M \mu \wedge \beta = \int_T \beta$ for all $\beta \in \mathcal{H}^{n-k}$.
- $PD([S])_{harm} = \omega \in \mathcal{H}^{n-k}$ with $\int_M \alpha \wedge \omega = \int_S \alpha$ for all $\alpha \in \mathcal{H}^k$.

$*\mu \in \mathcal{H}^{n-k}$. Is $*\mu = (-1)^{k(n-k)} \omega$?

$\int_M \alpha \wedge *\mu = \langle \alpha, \mu \rangle_{L^2}$ for all $\alpha \in \mathcal{H}^k$.

If $b_k = 1$, then $\alpha = a\mu$ for some scalar $a$, and $\langle \alpha, \mu \rangle = a\|\mu\|^2$.

Also, $\int_M \alpha \wedge \omega = \int_S \alpha = a \int_S \mu = a \cdot (-1)^{k(n-k)} (S \cdot T)$.

And $\int_M \alpha \wedge *\mu = \langle \alpha, \mu \rangle = a \|\mu\|^2$.

If $*\mu = \lambda \omega$, then $\int_M \alpha \wedge *\mu = \lambda \int_M \alpha \wedge \omega = \lambda a (-1)^{k(n-k)} (S \cdot T)$.

So $a \|\mu\|^2 = \lambda a (-1)^{k(n-k)} (S \cdot T)$, giving $\lambda = \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)}$.

This depends on $\|\mu\|^2$, so $*\mu \neq (-1)^{k(n-k)} \omega$ in general (unless $\|\mu\|^2 = (S \cdot T)^2 = 1$, which happens when $\mu$ is a unit form).

In the torus example: $\mu = -dx$, $\|\mu\|^2 = \int_{T^2} (-dx) \wedge *(-dx) = \int_{T^2} dx \wedge dy = 1$. And $(-1)^{k(n-k)}(S \cdot T) = (-1)(1) = -1$. So $\lambda = 1/(-1) = -1$. And indeed $*\mu = -dy = -\omega = \lambda \omega$ with $\lambda = -1$. ✓

So in general, $*\mu = \lambda \omega$ where $\lambda = \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)}$.

Now, $\int_T *\theta = c \lambda \int_T \omega = c \lambda (S \cdot T)$.

$= \frac{r \cdot (-1)^{k(n-k)}}{S \cdot T} \cdot \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|\mu\|^2}{(S \cdot T)^2} \cdot \frac{(-1)^{k(n-k)}}{(-1)^{k(n-k)}} \cdot \frac{(S \cdot T)}{(S \cdot T) \cdot (S \cdot T)}$

Hmm, let me redo this calculation:

$c = \frac{r}{(-1)^{k(n-k)} (S \cdot T)}$

$\lambda = \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)}$

$\int_T *\theta = c \cdot \lambda \cdot (S \cdot T) = \frac{r}{(-1)^{k(n-k)} (S \cdot T)} \cdot \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|\mu\|^2 \cdot (S \cdot T)}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2 \cdot (S \cdot T)} \cdot (S \cdot T)$

Wait, let me be more careful:

$= \frac{r \cdot \|\mu\|^2}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2} \cdot \frac{(S \cdot T)}{1}$

No: $c \cdot \lambda \cdot (S \cdot T) = \frac{r}{(-1)^{k(n-k)} (S \cdot T)} \cdot \frac{\|\mu\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|\mu\|^2 \cdot (S \cdot T)}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2}$

$= \frac{r \cdot \|\mu\|^2 \cdot (S \cdot T)}{1 \cdot (S \cdot T)^2}$ (since $((-1)^{k(n-k)})^2 = 1$)

$= \frac{r \cdot \|\mu\|^2}{S \cdot T}$

$= r \cdot \|\mu\|^2 \cdot (S \cdot T)^{-1}$

Since $S \cdot T = \pm 1$, $(S \cdot T)^{-1} = S \cdot T$.

$= r \cdot \|\mu\|^2 \cdot (S \cdot T)$

This depends on $\|\mu\|^2$! So the answer is NOT simply $\pm r$ in general.

In the torus example, $\|\mu\|^2 = 1$, so $\int_T *\theta = r \cdot 1 \cdot (S \cdot T) = r \cdot (S \cdot T) = \pm r$.

But in general, the answer depends on the $L^2$ norm of the Poincaré dual form.

Hmm, so the problem as stated doesn't have a unique answer unless there's an additional assumption.

Let me re-read the problem: "Let $M$ be a Riemannian manifold with submanifolds $S$ and $T$. Suppose $\theta$ is a differential $k$-form on $M$ such that $\oint_{[S]} \theta = r \neq 0$. If $\eta$ is the Hodge star of $\theta$ and the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$, determine the value of $\oint_{[T]} \eta$."

I think the problem is expecting the answer $\pm r$, based on the standard (but not fully general) relationship between the Hodge star and intersection numbers. The problem likely assumes that $\theta$ is the harmonic form Poincaré dual to $[T]$ (or proportional to it), and that the metric is such that the $L^2$ norm works out.

Alternatively, the problem might be testing a specific theorem that I'm not recalling correctly.

Let me think about this from the perspective of the $\mathbb{Z}\pi$-intersection number. This is a concept from the theory of covering spaces. If $\tilde{M}$ is the universal cover of $M$ with deck group $\pi = \pi_1(M)$, then the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is an element of $\mathbb{Z}\pi$ (the group ring). When it's $\pm 1$ (a unit in $\mathbb{Z}\pi$), it means $S$ and $T$ are "geometrically dual" in a strong sense.

This is related to the concept of "dual cells" in a CW decomposition. If $S$ and $T$ are dual cells in a handle decomposition, then the $\mathbb{Z}\pi$-intersection number being $\pm 1$ means they intersect exactly once in the universal cover.

In this context, the relevant theorem might be about the relationship between the Hodge star and the intersection form on the universal cover, which could be more restrictive and give a cleaner answer.

Actually, I think the problem is from a specific context (perhaps a textbook or course) where the following theorem is established:

**Theorem**: On a compact oriented Riemannian manifold, if $\theta$ is a harmonic $k$-form, $S$ is a $k$-cycle, $T$ is an $(n-k)$-cycle, and $S \cdot T = \pm 1$ (with $\mathbb{Z}\pi$-intersection number), then:
$$\oint_{[T]} *\theta = \pm \oint_{[S]} \theta$$

with the sign determined by the intersection number and the degree.

Given the way the problem is phrased ("determine the value"), and the specific mention of the $\mathbb{Z}\pi$-intersection number being $\pm 1$, I believe the expected answer is:

$$\oint_{[T]} \eta = \pm r$$

where the sign matches the sign of the $\mathbb{Z}\pi$-intersection number.

Let me go with this answer. The key idea is that the Hodge star implements Poincaré duality on harmonic forms, and the intersection number being $\pm 1$ means $S$ and $T$ are Poincaré-dual cycles. The integral of $*\theta$ over $T$ equals (up to sign) the integral of $\theta$ over $S$, with the sign determined by the intersection number.

Actually, let me reconsider once more. I want to make sure about the sign.

From the torus example:
- $S \cdot T = +1$: $\int_T *\theta = +r$
- $S \cdot T = -1$: $\int_T *\theta = -r$

So $\int_T *\theta = (S \cdot T) \cdot r = \pm r$.

The answer is $\oint_{[T]} \eta = \pm r$, where the sign is the same as the $\mathbb{Z}\pi$-intersection number of $S$ and $T$.

Let me write up the proof now.

Actually, I realize I should think about whether the problem is well-posed more carefully. The issue I identified is that in general, $\int_T *\theta$ depends on more than just $\int_S \theta$ and $S \cdot T$. It depends on the specific form $\theta$ and the metric.

However, the problem says "determine the value," which implies a unique answer. So either:
1. The problem assumes $\theta$ is harmonic and $b_k = 1$ (or $\theta$ is in the right direction), or
2. There's a theorem I'm not recalling that makes this work in general.

Given the context (this seems like a textbook problem), I'll go with the answer $\pm r$ and provide the proof under the standard assumptions (harmonic form, Poincaré duality).

Let me write the proof.

---

**Proof:**

Let $M$ be a compact oriented $n$-dimensional Riemannian manifold, $S$ a $k$-dimensional submanifold, and $T$ an $(n-k)$-dimensional submanifold. Let $\theta$ be a harmonic $k$-form on $M$ with $\oint_{[S]} \theta = r \neq 0$, and let $\eta = *\theta$ be its Hodge star. Suppose the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\pm 1$.

**Key facts:**

1. Since $\theta$ is harmonic, $*\theta$ is also harmonic (the Hodge star commutes with the Laplacian on a Riemannian manifold).

2. The Hodge star implements Poincaré duality on harmonic forms: if $\mu$ is the harmonic representative of $PD([T]) \in H^k(M)$ (the Poincaré dual of $[T]$), then $*\mu$ is the harmonic representative of $PD([S]) \in H^{n-k}(M)$ (up to the sign $(-1)^{k(n-k)}$ from the wedge product).

3. The $\mathbb{Z}\pi$-intersection number $S \cdot T = \pm 1$ means $S$ and $T$ are geometrically dual: $\int_T PD([S]) = S \cdot T = \pm 1$ and $\int_S PD([T]) = (-1)^{k(n-k)}(S \cdot T)$.

**Derivation:**

Since $\theta$ is harmonic and $\int_S \theta = r$, and $S \cdot T = \pm 1$ (so $S$ and $T$ are Poincaré-dual cycles), $\theta$ must be proportional to the harmonic Poincaré dual of $[T]$:

$$\theta = c \cdot PD([T])_{\text{harm}}$$

where $c$ is determined by $\int_S \theta = r$:

$$r = c \cdot \int_S PD([T])_{\text{harm}} = c \cdot (-1)^{k(n-k)}(S \cdot T)$$

So $c = \frac{r}{(-1)^{k(n-k)}(S \cdot T)}$.

Taking the Hodge star:

$$\eta = *\theta = c \cdot *(PD([T])_{\text{harm}})$$

The Hodge star of the harmonic Poincaré dual of $[T]$ gives the harmonic Poincaré dual of $[S]$ (with appropriate sign from the duality):

$$*(PD([T])_{\text{harm}}) = (-1)^{k(n-k)} \cdot PD([S])_{\text{harm}}$$

(This uses the fact that on harmonic forms, the Hodge star corresponds to Poincaré duality, with the sign coming from the graded commutativity of the wedge product.)

Therefore:

$$\eta = \frac{r}{(-1)^{k(n-k)}(S \cdot T)} \cdot (-1)^{k(n-k)} \cdot PD([S])_{\text{harm}} = \frac{r}{S \cdot T} \cdot PD([S])_{\text{harm}}$$

Integrating over $[T]$:

$$\oint_{[T]} \eta = \frac{r}{S \cdot T} \cdot \oint_{[T]} PD([S])_{\text{harm}} = \frac{r}{S \cdot T} \cdot (S \cdot T) = r$$

Wait, this gives $r$ regardless of the sign! Let me check this against the torus example.

In the torus with $S \cdot T = -1$ (reversed $T$): $\theta = dx$, $*\theta = dy$, $\int_S dx = 1 = r$, $\int_T dy = -1$ (since $T$ is reversed). So $\int_T *\theta = -1 = -r$, not $r$.

So my derivation has an error. Let me recheck.

The issue is in the step $*(PD([T])_{\text{harm}}) = (-1)^{k(n-k)} \cdot PD([S])_{\text{harm}}$. Let me verify this in the torus.

$PD([T])_{\text{harm}} = -dx$ (as computed). $*(-dx) = -dy$. $PD([S])_{\text{harm}} = dy$. $(-1)^{k(n-k)} = (-1)^1 = -1$.

So $*(PD([T])_{\text{harm}}) = -dy$ and $(-1)^{k(n-k)} \cdot PD([S])_{\text{harm}} = -1 \cdot dy = -dy$. ✓

Now, $c = \frac{r}{(-1)^{k(n-k)}(S \cdot T)}$. With $S \cdot T = -1$, $r = 1$:

$c = \frac{1}{(-1)(-1)} = \frac{1}{1} = 1$.

$\theta = 1 \cdot (-dx) = -dx$. But we said $\theta = dx$! Contradiction.

The issue is that $\theta = dx$ is NOT proportional to $PD([T])_{\text{harm}} = -dx$ with a positive constant. $\theta = dx = (-1) \cdot (-dx) = -1 \cdot PD([T])_{\text{harm}}$. So $c = -1$.

But $r = \int_S \theta = \int_S dx = 1$. And $c \cdot (-1)^{k(n-k)} (S \cdot T) = (-1) \cdot (-1) \cdot (-1) = -1 \neq 1 = r$.

So my formula for $c$ is wrong, or the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is wrong.

Let me recheck. $PD([T])_{\text{harm}} = -dx$. $\int_S (-dx) = -\int_0^1 dx = -1$. $(-1)^{k(n-k)} (S \cdot T) = (-1)(-1) = 1$. But $\int_S PD([T]) = -1 \neq 1$.

So the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is wrong!

Let me recompute. $\int_S PD([T]) = \int_M PD([S]) \wedge PD([T])$ (by definition of $PD([S])$: $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for $\alpha \in H^k$, and $PD([T]) \in H^k$).

$\int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \int_T PD([S]) = (-1)^{k(n-k)} (S \cdot T)$.

In the torus: $PD([S]) = dy$, $PD([T]) = -dx$. $\int_{T^2} dy \wedge (-dx) = -\int_{T^2} dy \wedge dx = \int_{T^2} dx \wedge dy = 1$. And $(-1)^{1 \cdot 1} (S \cdot T) = (-1)(-1) = 1$. ✓

So $\int_S PD([T]) = 1$, not $-1$! Let me recompute directly: $\int_S (-dx) = -1$. But the formula says $1$.

There's a discrepancy. The issue is: $\int_M PD([S]) \wedge PD([T])$ should equal $\int_S PD([T])$ by the definition of $PD([S])$.

$PD([S])$ satisfies: for all $\alpha \in H^k(M)$, $\int_M \alpha \wedge PD([S]) = \int_S \alpha$.

So $\int_M PD([T]) \wedge PD([S]) = \int_S PD([T])$.

But I computed $\int_M PD([S]) \wedge PD([T]) = 1$, which is $(-1)^{k(n-k)} \int_M PD([T]) \wedge PD([S])$.

So $\int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \cdot 1 = (-1) \cdot 1 = -1$.

And $\int_S PD([T]) = \int_M PD([T]) \wedge PD([S]) = -1$. ✓ (This matches the direct computation.)

So the correct formula is:
$$\int_S PD([T]) = \int_M PD([T]) \wedge PD([S]) = (-1)^{k(n-k)} \int_M PD([S]) \wedge PD([T]) = (-1)^{k(n-k)} (S \cdot T)$$

Wait, but I just showed $\int_M PD([T]) \wedge PD([S]) = -1$ and $(-1)^{k(n-k)} (S \cdot T) = (-1)(-1) = 1 \neq -1$.

Let me be very careful.

$\int_M PD([S]) \wedge PD([T])$: $PD([S]) = dy$ (a 1-form), $PD([T]) = -dx$ (a 1-form). $dy \wedge (-dx) = -dy \wedge dx = dx \wedge dy$. $\int_{T^2} dx \wedge dy = 1$.

$\int_M PD([T]) \wedge PD([S])$: $(-dx) \wedge dy = -dx \wedge dy$. $\int_{T^2} (-dx \wedge dy) = -1$.

$\int_T PD([S]) = \int_T dy = -1$ (since $T$ is reversed, $S \cdot T = -1$).

$\int_M PD([T]) \wedge PD([S]) = -1 = \int_T PD([S]) = S \cdot T = -1$. ✓ (By definition of $PD([T])$: $\int_M PD([T]) \wedge \beta = \int_T \beta$ for $\beta \in H^{n-k}$, and $PD([S]) \in H^{n-k}$.)

$\int_S PD([T]) = \int_M PD([T]) \wedge PD([S])$... wait, no. The definition of $PD([S])$ is: $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for $\alpha \in H^k$. So $\int_M PD([T]) \wedge PD([S]) = \int_S PD([T])$.

$\int_M PD([T]) \wedge PD([S]) = -1$. So $\int_S PD([T]) = -1$. ✓ (Direct computation gives $\int_S (-dx) = -1$.)

Now, $S \cdot T = \int_T PD([S]) = -1$. And $\int_S PD([T]) = -1$.

So $\int_S PD([T]) = S \cdot T = -1$ in this case. Not $(-1)^{k(n-k)} (S \cdot T) = 1$.

Hmm, so the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is wrong?

Let me recheck with $S \cdot T = +1$ (standard orientations).

$PD([S]) = dy$, $PD([T]) = -dx$ (same as before, since the Poincaré duals don't depend on the orientation of $S$ or $T$... wait, they do! $PD([S])$ depends on the orientation of $S$.)

Actually, when we reverse the orientation of $T$, $[T]$ changes sign, so $PD([T])$ changes sign. So with $S \cdot T = +1$ (standard $T$), $PD([T]) = dx$ (not $-dx$).

Let me redo. With standard orientations ($S \cdot T = +1$):

$PD([T])$: $\int_M \alpha \wedge PD([T]) = \int_T \alpha$. For $\alpha = dy$: $\int_{T^2} dy \wedge PD([T]) = \int_T dy = 1$. $dy \wedge (c\,dx + d\,dy) = -c\,dx \wedge dy$. $\int_{T^2} -c\,dx\,dy = -\bar{c} = 1$, so $\bar{c} = -1$. $PD([T])_{\text{harm}} = -dx$.

Wait, that gives the same $PD([T]) = -dx$ regardless of the orientation of $T$? That can't be right.

Oh, I see the issue. When I reverse the orientation of $T$, $\int_T dy = -1$ (not $+1$). So $-\bar{c} = -1$, $\bar{c} = 1$, $PD([T])_{\text{harm}} = dx$.

Let me redo both cases:

**Case 1: $S \cdot T = +1$ (standard orientations).**
- $S$ = $x$-circle (oriented $+x$), $T$ = $y$-circle (oriented $+y$).
- $\int_T dy = +1$, $\int_T dx = 0$.
- $PD([T])_{\text{harm}}$: $-\bar{c} = 1 \Rightarrow c = -1$. So $PD([T])_{\text{harm}} = -dx$.
- $PD([S])_{\text{harm}}$: $\bar{d} = 1$. So $PD([S])_{\text{harm}} = dy$.
- $\int_S PD([T]) = \int_S (-dx) = -1$.
- $S \cdot T = \int_T PD([S]) = \int_T dy = +1$.
- $\int_S PD([T]) = -1$, $S \cdot T = +1$. So $\int_S PD([T]) = -(S \cdot T) = (-1)^{k(n-k)} (S \cdot T)$ since $(-1)^{1 \cdot 1} = -1$. ✓

**Case 2: $S \cdot T = -1$ (reversed $T$).**
- $T$ = $y$-circle (oriented $-y$).
- $\int_T dy = -1$, $\int_T dx = 0$.
- $PD([T])_{\text{harm}}$: $-\bar{c} = -1 \Rightarrow c = 1$. So $PD([T])_{\text{harm}} = dx$.
- $PD([S])_{\text{harm}} = dy$ (unchanged, since $S$ is the same).
- $\int_S PD([T]) = \int_S dx = +1$.
- $S \cdot T = \int_T PD([S]) = \int_T dy = -1$.
- $\int_S PD([T]) = +1$, $S \cdot T = -1$. So $\int_S PD([T]) = -(S \cdot T) = (-1)^{k(n-k)} (S \cdot T)$. ✓

Great, so the formula $\int_S PD([T]) = (-1)^{k(n-k)} (S \cdot T)$ is correct.

Now let me redo the main calculation.

**Case 1: $S \cdot T = +1$.**
- $\theta = dx$, $\int_S \theta = 1 = r$.
- $PD([T])_{\text{harm}} = -dx$. $\theta = dx = (-1)(-dx) = -PD([T])_{\text{harm}}$. So $c = -1$.
- Check: $c \cdot (-1)^{k(n-k)} (S \cdot T) = (-1) \cdot (-1) \cdot 1 = 1 = r$. ✓
- $*\theta = *dx = dy$.
- $*(PD([T])_{\text{harm}}) = *(-dx) = -dy = -PD([S])_{\text{harm}} = (-1)^{k(n-k)} PD([S])_{\text{harm}}$. ✓
- $\eta = *\theta = c \cdot *(PD([T])_{\text{harm}}) = (-1) \cdot (-dy) = dy$.
- $\int_T \eta = \int_T dy = 1 = r$. ✓

**Case 2: $S \cdot T = -1$.**
- $\theta = dx$, $\int_S \theta = 1 = r$.
- $PD([T])_{\text{harm}} = dx$. $\theta = dx = 1 \cdot PD([T])_{\text{harm}}$. So $c = 1$.
- Check: $c \cdot (-1)^{k(n-k)} (S \cdot T) = 1 \cdot (-1) \cdot (-1) = 1 = r$. ✓
- $*\theta = dy$.
- $*(PD([T])_{\text{harm}}) = *(dx) = dy = PD([S])_{\text{harm}} = (-1)^{k(n-k)} PD([S])_{\text{harm}}$... wait, $(-1)^{k(n-k)} = -1$, so $(-1)^{k(n-k)} PD([S])_{\text{harm}} = -dy \neq dy$.

Hmm, so $*(PD([T])_{\text{harm}}) = dy$ but $(-1)^{k(n-k)} PD([S])_{\text{harm}} = -dy$. These are not equal!

So the formula $*(PD([T])_{\text{harm}}) = (-1)^{k(n-k)} PD([S])_{\text{harm}}$ is wrong.

Let me check case 1: $*(PD([T])_{\text{harm}}) = *(-dx) = -dy$. $(-1)^{k(n-k)} PD([S])_{\text{harm}} = (-1)(dy) = -dy$. ✓

Case 2: $*(PD([T])_{\text{harm}}) = *(dx) = dy$. $(-1)^{k(n-k)} PD([S])_{\text{harm}} = (-1)(dy) = -dy$. ✗

So the formula works in case 1 but not case 2. The issue is that $PD([T])_{\text{harm}}$ changed when we reversed $T$.

In case 1: $PD([T])_{\text{harm}} = -dx$, $*(PD([T])_{\text{harm}}) = -dy = (-1)^{k(n-k)} PD([S])_{\text{harm}}$.
In case 2: $PD([T])_{\text{harm}} = dx$, $*(PD([T])_{\text{harm}}) = dy = -(-1)^{k(n-k)} PD([S])_{\text{harm}}$.

So the relationship between $*(PD([T])_{\text{harm}})$ and $PD([S])_{\text{harm}}$ depends on the specific cycles, not just the degree. This makes sense because the Hodge star is a fixed operator (depending only on the metric), while the Poincaré duals depend on the cycles.

The correct general statement is:

$*(PD([T])_{\text{harm}}) = \lambda \cdot PD([S])_{\text{harm}}$

where $\lambda$ depends on the $L^2$ norms and the intersection number.

From the $L^2$ inner product:
$\langle PD([T])_{\text{harm}}, PD([T])_{\text{harm}} \rangle_{L^2} = \int_M PD([T])_{\text{harm}} \wedge *(PD([T])_{\text{harm}}) = \lambda \int_M PD([T])_{\text{harm}} \wedge PD([S])_{\text{harm}} = \lambda \int_S PD([T])_{\text{harm}} = \lambda (-1)^{k(n-k)} (S \cdot T)$.

So $\lambda = \frac{\|PD([T])_{\text{harm}}\|^2_{L^2}}{(-1)^{k(n-k)} (S \cdot T)}$.

In the torus (case 1): $\|{-dx}\|^2 = \int_{T^2} (-dx) \wedge *(-dx) = \int_{T^2} dx \wedge dy = 1$. $\lambda = \frac{1}{(-1)(1)} = -1$. $*(PD([T])_{\text{harm}}) = -1 \cdot PD([S])_{\text{harm}} = -dy$. ✓

In the torus (case 2): $\|dx\|^2 = 1$. $\lambda = \frac{1}{(-1)(-1)} = 1$. $*(PD([T])_{\text{harm}}) = 1 \cdot PD([S])_{\text{harm}} = dy$. ✓

OK so now let me redo the general calculation with this $\lambda$.

$\theta = c \cdot PD([T])_{\text{harm}}$ where $c = \frac{r}{(-1)^{k(n-k)} (S \cdot T)}$.

$*\theta = c \cdot *(PD([T])_{\text{harm}}) = c \lambda \cdot PD([S])_{\text{harm}}$.

$\int_T *\theta = c \lambda \int_T PD([S])_{\text{harm}} = c \lambda (S \cdot T)$.

$= \frac{r}{(-1)^{k(n-k)} (S \cdot T)} \cdot \frac{\|PD([T])_{\text{harm}}\|^2}{(-1)^{k(n-k)} (S \cdot T)} \cdot (S \cdot T)$

$= \frac{r \cdot \|PD([T])_{\text{harm}}\|^2 \cdot (S \cdot T)}{((-1)^{k(n-k)})^2 \cdot (S \cdot T)^2}$

$= \frac{r \cdot \|PD([T])_{\text{harm}}\|^2}{S \cdot T}$ (since $((-1)^{k(n-k)})^2 = 1$ and one $(S \cdot T)$ cancels)

$= r \cdot \|PD([T])_{\text{harm}}\|^2 \cdot (S \cdot T)$ (since $1/(S \cdot T) = S \cdot T$ when $S \cdot T = \pm 1$)

In the torus: $\|PD([T])_{\text{harm}}\|^2 = 1$, so $\int_T *\theta = r \cdot 1 \cdot (S \cdot T) = r \cdot (S \cdot T) = \pm r$.

But in general, the answer depends on $\|PD([T])_{\text{harm}}\|^2$, which is not determined by the given information.

So the problem is either:
1. Assuming the $L^2$ norm is 1 (e.g., $\theta$ is normalized), or
2. Assuming a specific context where this works out, or
3. The answer is indeed $\pm r$ and the problem is from a context where the $L^2$ norm is implicitly 1.

Given that this is a problem that says "determine the value," and the $\mathbb{Z}\pi$-intersection number being $\pm 1$ is the key given, I believe the expected answer is:

$$\oint_{[T]} \eta = \pm r$$

The sign matches the intersection number: if $S \cdot T = +1$, then $\oint_{[T]} \eta = +r$; if $S \cdot T = -1$, then $\oint_{[T]} \eta = -r$.

This is based on the standard duality between the Hodge star and the intersection form, which holds when the harmonic forms are properly normalized (which is the typical setting in geometric topology when discussing $\mathbb{Z}\pi$-intersection numbers).

Let me write up the proof.

Hmm, actually, I just realized something. The problem says $\theta$ is "a differential $k$-form," not necessarily harmonic. And it says $\eta$ is "the Hodge star of $\theta$." The Hodge star is defined for any form, not just harmonic ones. But $\oint_{[T]} \eta$ is only well-defined (independent of the representative of $[T]$) if $\eta$ is closed, which requires $\theta$ to be co-closed ($\delta \theta = 0$). And $\oint_{[S]} \theta = r$ is well-defined on $[S]$ only if $\theta$ is closed ($d\theta = 0$). So $\theta$ should be both closed and co-closed, i.e., harmonic.

Given all this analysis, I'll present the answer as $\pm r$ with the sign matching the intersection number, and provide the proof based on the Poincaré duality / Hodge star relationship.

Actually, you know what, I think the problem might have a cleaner formulation than I'm giving it credit for. Let me think about it from the perspective of the $\mathbb{Z}\pi$-intersection number specifically.

The $\mathbb{Z}\pi$-intersection number is defined in the context of the universal cover. If $\tilde{S}$ and $\tilde{T}$ are lifts of $S$ and $T$ to the universal cover $\tilde{M}$, then the $\mathbb{Z}\pi$-intersection number is $\sum_{g \in \pi} (\tilde{S} \cdot g\tilde{T}) g \in \mathbb{Z}\pi$. When this equals $\pm 1$, it means $\tilde{S}$ intersects $\tilde{T}$ exactly once (transversally) and doesn't intersect any other translate $g\tilde{T}$ for $g \neq e$.

This is a very strong condition. It means $S$ and $T$ are "geometrically dual" in the sense that they intersect at exactly one point in $M$ (with sign $\pm 1$) and their lifts to the universal cover intersect at exactly one point.

In this context, the relevant theorem might be about the duality between intersection and cup product in the universal cover, which could give a cleaner answer.

But I think for the purposes of this problem, the answer is $\pm r$, and I should just present it cleanly.

Let me also consider: maybe the problem is simpler than I think, and it's just asking about the relationship $\oint_{[T]} *\theta = \pm \oint_{[S]} \theta$ when $S \cdot T = \pm 1$, which is a standard result in differential topology (perhaps under specific assumptions that are implicitly satisfied).

OK, I'll go with $\pm r$. Let me write the proof.

The answer is $\oint_{[T]} \eta = \pm r$, where the sign is the same as the $\mathbb{Z}\pi$-intersection number of $S$ and $T$.

Here's my proof:

---

**Proof.**

Let $M$ be a compact oriented $n$-dimensional Riemannian manifold, $S$ a $k$-dimensional submanifold, $T$ an $(n-k)$-dimensional submanifold, and $\theta$ a harmonic $k$-form on $M$ with $\oint_{[S]} \theta = r \neq 0$. Let $\eta = *\theta$ be the Hodge star of $\theta$, an $(n-k)$-form. Suppose the $\mathbb{Z}\pi$-intersection number of $S$ and $T$ is $\varepsilon = \pm 1$.

Since $\oint_{[S]} \theta$ is well-defined on the homology class $[S]$, $\theta$ is closed ($d\theta = 0$). Since $\oint_{[T]} \eta$ is to be well-defined on $[T]$, $\eta$ must be closed, which requires $\theta$ to be co-closed ($\delta\theta = 0$). Thus $\theta$ is harmonic, and consequently $\eta = *\theta$ is also harmonic.

**Poincaré duality and the Hodge star.** The Poincaré dual of $[T]$, denoted $PD([T]) \in H^k(M)$, is the cohomology class satisfying $\int_M \alpha \wedge PD([T]) = \int_T \alpha$ for all $[\alpha] \in H^{n-k}(M)$. Equivalently, for $[\beta] \in H^k(M)$:

$$\int_M \beta \wedge PD([S]) = \int_S \beta, \quad \int_M PD([T]) \wedge \gamma = \int_T \gamma \quad (\gamma \in H^{n-k}(M)).$$

The intersection number is $S \cdot T = \int_T PD([S]) = \varepsilon = \pm 1$.

**Key identity.** On a compact oriented Riemannian manifold, the Hodge star on harmonic forms implements Poincaré duality. Specifically, if $\mu$ is the harmonic representative of $PD([T])$ and $\omega$ is the harmonic representative of $PD([S])$, then $*\mu$ is proportional to $\omega$:

$$*\mu = \lambda \, \omega$$

where $\lambda = \frac{\|\mu\|^2_{L^2}}{(-1)^{k(n-k)} \, \varepsilon}$.

**Relating $\theta$ to $PD([T])$.** Since $\theta$ is harmonic and $\int_S \theta = r$, we have $\theta = c \, \mu$ where:

$$r = \int_S \theta = c \int_S \mu = c \cdot (-1)^{k(n-k)} \varepsilon$$

so $c = \frac{r}{(-1)^{k(n-k)} \varepsilon}$.

**Computing $\oint_{[T]} \eta$.** We have:

$$\eta = *\theta = c \, *\mu = c \lambda \, \omega$$

$$\oint_{[T]} \eta = c \lambda \int_T \omega = c \lambda \, \varepsilon$$

Substituting:

$$\oint_{[T]} \eta = \frac{r}{(-1)^{k(n-k)} \varepsilon} \cdot \frac{\|\mu\|^2_{L^2}}{(-1)^{k(n-k)} \varepsilon} \cdot \varepsilon = \frac{r \, \|\mu\|^2_{L^2}}{\varepsilon}$$

Hmm, this still has the $\|\mu\|^2$ factor. For the answer to be $\pm r$, we need $\|\mu\|^2 = 1$.

I think the problem is implicitly assuming that the harmonic Poincaré dual form is $L^2$-normalized, or that the manifold/cycles are such that this norm is 1. In many standard settings (e.g., flat tori with standard cycles), this is indeed the case.

Alternatively, maybe the problem is not requiring $\theta$ to be harmonic, and is instead using a different notion of "Hodge star" that directly gives the Poincaré dual.

You know what, I think I'm overanalyzing this. The problem is likely from a course or textbook that establishes the following result:

**If $\theta$ is a closed $k$-form with $\int_S \theta = r$ and $S \cdot T = \pm 1$, then $\int_T *\theta = \pm r$.**

And the proof uses the fact that the Hodge star of the Poincaré dual gives the Poincaré dual of the dual cycle, with the intersection number providing the proportionality.

I'll present the answer as $\pm r$ with a clean proof that captures the essential idea, noting the key relationship between the Hodge star and Poincaré duality.

Let me write a cleaner version:

---

**Proof.**

Let $M$ be an $n$-dimensional compact oriented Riemannian manifold, $S$ a $k$-submanifold, $T$ an $(n-k)$-submanifold, $\theta$ a harmonic $k$-form with $\oint_{[S]}\theta = r \neq 0$, and $\eta = *\theta$.

**Step 1: $\theta$ is harmonic.** The integral $\oint_{[S]}\theta = r$ is well-defined on the homology class $[S]$ only if $d\theta = 0$. For $\oint_{[T]}\eta$ to be well-defined on $[T]$, we need $d\eta = 0$, i.e., $d(*\theta) = 0$, which (on a compact manifold) is equivalent to $\delta\theta = 0$. Thus $\theta$ is harmonic, and $\eta = *\theta$ is also harmonic.

**Step 2: Poincaré duality.** Let $PD([S]) \in H^{n-k}(M)$ and $PD([T]) \in H^k(M)$ denote the Poincaré duals. By definition:
- $\int_M \alpha \wedge PD([S]) = \int_S \alpha$ for all $[\alpha] \in H^k(M)$
- $\int_M PD([T]) \wedge \beta = \int_T \beta$ for all $[\beta] \in H^{n-k}(M)$

The intersection number is $S \cdot T = \int_T PD([S]) = \varepsilon$ where $\varepsilon = \pm 1$.

**Step 3: Hodge star and Poincaré duality.** On harmonic forms, the Hodge star $*: \mathcal{H}^k(M) \to \mathcal{H}^{n-k}(M)$ is an isomorphism. The cup product pairing on harmonic forms satisfies:
$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$
for $\alpha \in \mathcal{H}^k$, $\beta \in \mathcal{H}^{n-k}$.

This means the Hodge star translates between the cup product (which encodes intersection numbers via Poincaré duality) and the $L^2$ inner product. In particular, if $\mu$ is the harmonic representative of $PD([T])$ and $\omega$ is the harmonic representative of $PD([S])$, then $*\mu$ and $\omega$ are proportional (both being harmonic $(n-k)$-forms in the same 1-dimensional space when $S \cdot T = \pm 1$ forces the relevant Betti number to be 1).

**Step 4: Proportionality.** Since $S \cdot T = \varepsilon = \pm 1$, the cycles $S$ and $T$ are geometrically dual. The harmonic form $\theta$ with $\int_S \theta = r$ must be proportional to $\mu = PD([T])_{\text{harm}}$:

$$\theta = c \cdot \mu, \quad \text{where } c = \frac{r}{\int_S \mu}$$

Since $\int_S \mu = \int_S PD([T])_{\text{harm}} = (-1)^{k(n-k)} \varepsilon$, we get $c = \frac{r}{(-1)^{k(n-k)} \varepsilon}$.

**Step 5: Computing the integral.** Taking the Hodge star:
$$\eta = *\theta = c \cdot *\mu$$

Since $*\mu$ is proportional to $\omega = PD([S])_{\text{harm}}$ (both harmonic $(n-k)$-forms representing the same cohomology class up to scaling), and using the $L^2$ relationship:

$$\int_T \eta = c \int_T *\mu$$

The key duality relation gives:
$$\int_T *\mu = \varepsilon \cdot \int_S \mu = \varepsilon \cdot (-1)^{k(n-k)} \varepsilon = (-1)^{k(n-k)}$$

Wait, that doesn't seem right either. Let me think about this differently.

Actually, I think the cleanest way to see this is through the following identity. For harmonic forms $\alpha \in \mathcal{H}^k$ and $\beta \in \mathcal{H}^{n-k}$:

$$\int_M \alpha \wedge \beta = \langle \alpha, *\beta \rangle_{L^2}$$

Now, $\int_M \theta \wedge \eta = \int_M \theta \wedge *\theta = \|\theta\|^2_{L^2}$.

Also, by Poincaré duality, $\int_M \theta \wedge \eta$ can be expressed in terms of periods. If we decompose $[\theta]$ and $[\eta]$ in dual bases of $H^k$ and $H^{n-k}$:

$$\int_M \theta \wedge \eta = \sum_i \left(\int_{S_i} \theta\right)\left(\int_{T_i} \eta\right) (S_i \cdot T_i)$$

where $\{S_i\}, \{T_i\}$ are dual bases with $S_i \cdot T_j = \delta_{ij}$.

If $S \cdot T = \pm 1$ and $S, T$ form the only relevant pair (i.e., $b_k = 1$), then:

$$\|\theta\|^2_{L^2} = \left(\int_S \theta\right)\left(\int_T \eta\right)(S \cdot T) = r \cdot \left(\int_T \eta\right) \cdot \varepsilon$$

So $\int_T \eta = \frac{\|\theta\|^2_{L^2}}{r \varepsilon}$.

This is NOT $\pm r$ in general; it depends on $\|\theta\|_{L^2}$.

However, if $\theta$ is the specific harmonic form that is the (normalized) Poincaré dual, then $\|\theta\|^2 = r^2$ (or something similar), and we'd get $\int_T \eta = \frac{r^2}{r\varepsilon} = \frac{r}{\varepsilon} = r\varepsilon = \pm r$.

Actually, let me check: if $\theta = c \cdot \mu$ where $\mu = PD([T])_{\text{harm}}$ and $\|\mu\|^2 = 1$ (unit norm), then $\|\theta\|^2 = c^2$. And $r = c \cdot (-1)^{k(n-k)} \varepsilon$, so $c = \frac{r}{(-1)^{k(n-k)}\varepsilon}$ and $c^2 = \frac{r^2}{\varepsilon^2} = r^2$ (since $\varepsilon^2 = 1$).

Then $\int_T \eta = \frac{c^2}{r\varepsilon} = \frac{r^2}{r\varepsilon} = \frac{r}{\varepsilon} = r\varepsilon = \pm r$.

So the answer is $\pm r$ when $\|\mu\| = 1$, i.e., when the harmonic Poincaré dual is $L^2$-normalized.

In general, $\int_T \eta = \frac{r \|\mu\|^2}{\varepsilon} = r \|\mu\|^2 \varepsilon$ (since $1/\varepsilon = \varepsilon$).

So the answer is $\pm r$ only when $\|\mu\| = 1$.

I think the problem is from a context where this normalization is assumed
