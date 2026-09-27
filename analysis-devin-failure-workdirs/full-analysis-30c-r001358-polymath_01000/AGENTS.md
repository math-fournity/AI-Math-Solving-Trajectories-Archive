# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Find the maximum of \( x_{1}^{3} + \ldots + x_{10}^{3} \) for \( x_{1}, \ldots, x_{10} \in [-1, 2] \) such that \( x_{1} + \ldots + x_{10} = 10 \).       — 题目文本
#   To find the maximum value of \( x_1^3 + x_2^3 + \ldots + x_{10}^3 \) for \( x_1, x_2, \ldots, x_{10} \in [-1, 2] \) such that \( x_1 + x_2 + \ldots + x_{10} = 10 \), we need to carefully consider the constraints and the behavior of the cube function.

1. **Maximizing the Cube Function**:
   - The cube function \( x^3 \) is increasing, so to maximize the sum of cubes, we should set as many variables as possible to the maximum value of 2.
   - If all 10 variables were set to 2, the total sum would be \( 2 \times 10 = 20 \), which exceeds 10. Therefore, we need to reduce the total sum by 10 while maximizing the cube sum.

2. **Optimal Configuration**:
   - Let \( m \) variables be set to 2. The remaining \( 10 - m \) variables must sum to \( 10 - 2m \).
   - To maximize the cube sum, we should minimize the loss in the cube sum when reducing the variables. 

3. **Calculations for \( m = 6 \)**:
   - If \( m = 6 \), then 6 variables are set to 2. The remaining 4 variables must sum to \( 10 - 2 \times 6 = -2 \).
   - To minimize the loss in the cube sum, we set each of the remaining 4 variables to \(-0.5\), which is the highest possible value to minimize the cube loss.
   - Each \(-0.5\) contributes \((-0.5)^3 = -0.125\).
   - Total cube contribution from the remaining variables: \( 4 \times (-0.125) = -0.5 \).
   - Total cube sum: \( 6 \times 8 + (-0.5) = 48 - 0.5 = 47.5 \).

4. **Verification**:
   - Other configurations, such as mixing \(-1\) and 0, or different distributions, were considered but resulted in lower cube sums.
   - Using Lagrangian multipliers and KKT conditions confirmed that the maximum is achieved with the configuration described.

Thus, the maximum value of the sum of cubes is \(\boxed{\dfrac{95}{2}}\).  — 标准解答
#   Let me solve this problem. We need to find the maximum of x_1^3 + ... + x_10^3 where each x_i ∈ [-1, 2] and x_1 + ... + x_10 = 10.

First, let me check for answer leaks. The problem just states the problem, no solution given. Good.

Let me think. The sum is 10, with 10 variables each in [-1,2]. The average is 1. If all were 1, sum of cubes = 10. But we want to maximize sum of cubes.

Cubic function is convex on positive values and concave on negative. Actually x^3 has second derivative 6x, so convex for x>0, concave for x<0.

To maximize sum of cubes with fixed sum, we want to push values to extremes. Since x^3 is convex for x>0, by Jensen we want positive values at extremes (either 2 or close to 0). For negative values, concave so we want them equal.

Strategy: push some variables to 2 (max), and the rest adjust to meet the sum constraint. Let's say k variables are at 2. Then remaining 10-k variables sum to 10-2k. Each remaining in [-1,2].

For remaining variables with sum S = 10-2k, we want to maximize sum of cubes. The remaining variables: if S is positive, push to 2 as much as possible. Actually let's think about what's optimal.

Let me consider: we want to maximize. x^3 is increasing, so larger x gives larger cube. But with fixed sum, we need balance.

Consider the function. Let's think about pushing to boundary. The feasible region is a polytope (intersection of hypercube with hyperplane). The maximum of a convex-ish function... Actually sum of cubes is not convex overall.

Let me think about KKT/edge analysis. At optimum, variables are at boundary (2 or -1) except possibly some "free" ones.

Let me guess: take as many 2's as possible. If all 10 are 2, sum = 20, too much. We need sum 10.

Let's say we have k variables at 2, m variables at -1, and the rest free. Sum: 2k - m + (free sum) = 10. We want to maximize 8k - m + (free cubes).

Actually, let me think more carefully. Let's try to have variables either at 2 or at some value to balance.

Suppose we have k variables at 2, contributing 8k to cubes and 2k to sum. Remaining 10-k variables sum to 10-2k, each in [-1,2].

For the remaining, to maximize sum of cubes given fixed sum. If 10-2k ≤ 0, i.e., k ≥ 5, the remaining sum is non-positive. 

Let's think: we want remaining sum to be achieved with max cubes. For remaining variables with sum S (where S = 10-2k), if S is small/negative, we'd want to push some to -1 and others to 2? No wait, we want to maximize cubes.

Hmm, let me think about small cases. Actually, let me reconsider. The cube function: for maximizing sum with fixed total, since cube is convex for positive x, we want positive contributions concentrated. For negative x (concave), we want them spread equally.

Let me consider: put some at 2, and the rest at a common value. If k at 2, and (10-k) at value v, then 2k + (10-k)v = 10, so v = (10-2k)/(10-k). Need v ∈ [-1, 2].

Sum of cubes = 8k + (10-k)v^3.

Let me compute for various k:
- k=0: v=1, sum=10.
- k=1: v=8/9≈0.889, sum=8+9*(0.889)^3=8+9*0.702=8+6.32=14.32
- k=2: v=6/8=0.75, sum=16+8*(0.75)^3=16+8*0.4219=16+3.375=19.375
- k=3: v=4/7≈0.571, sum=24+7*(0.571)^3=24+7*0.1866=24+1.306=25.306
- k=4: v=2/6=1/3, sum=32+6*(1/3)^3=32+6/27=32+0.222=32.222
- k=5: v=0/5=0, sum=40+0=40
- k=6: v=-2/4=-0.5, sum=48+4*(-0.125)=48-0.5=47.5
- k=7: v=-4/3≈-1.333, but this is < -1, infeasible!

So k=6 gives v=-0.5 which is feasible. sum=47.5.

But wait, can we do better by not having all remaining equal? For k=6, remaining 4 variables sum to -2. To maximize sum of cubes with 4 variables in [-1,2] summing to -2. Since for negative region cube is concave, equal is optimal among negatives? Actually we want to maximize. With sum -2 over 4 vars, if all equal -0.5, cubes sum = 4*(-0.125)=-0.5. 

Alternatively, could push some to 2 and others to -1. E.g., one at 2, then remaining 3 sum to -4, each ≥-1, so min sum is -3. -4 < -3, infeasible. So can't have any at 2 among remaining when k=6.

What about mixing -1 and something? With 4 vars summing to -2: if one at -1, remaining 3 sum to -1, equal at -1/3, cubes = -1 + 3*(-1/27) = -1 - 1/9 = -1.111. Worse than -0.5.

If two at -1, remaining 2 sum to 0, equal at 0, cubes = -2 + 0 = -2. Worse.

So equal is best for k=6. Sum = 47.5.

Let me check k=5 more carefully. Remaining 5 vars sum to 0. Equal at 0 gives 0. But can we do better? Push some to 2 and others to -1. If one at 2, remaining 4 sum to -2, each ≥-1, min -4 ≥ -2 ok. To maximize, remaining 4 summing to -2: equal at -0.5 gives -0.5. Total = 8 - 0.5 = 7.5 for these 5. Plus 5*8=40 from the 2's. Total = 47.5. Same!

Hmm interesting. Let me check: k=5 with one of remaining at 2 and four at -0.5: that's actually 6 at 2 and 4 at -0.5, same as k=6 case.

What about k=5, two at 2? Then it's 7 at 2, remaining 3 sum to 10-14=-4, min -3, infeasible.

So the boundary cases converge. Let me check if we can beat 47.5.

What about k=6 but with some at -1? 6 at 2 (sum 12, cubes 48), remaining 4 sum to -2. If we use -1's: to sum -2 with 4 vars in [-1,2], and we want to maximize cubes. The minimum each can be is -1. If two at -1 (sum -2) and two at 0: cubes = -2. Total = 46. Worse than 47.5.

If one at -1, three summing to -1: equal -1/3, cubes = -1 + 3*(-1/27)=-1.111, total 46.889. Worse.

So 47.5 with 6 at 2 and 4 at -0.5 seems good. But is it the global max?

Let me reconsider. Maybe non-symmetric is better. Let me think about the general structure.

Actually, let me reconsider whether having some at -1 and more at 2 could help. The issue is sum constraint. With 7 at 2, sum=14, remaining 3 need sum -4, but min is -3. Infeasible. So max 6 at 2.

With 6 at 2, remaining 4 sum to -2. We showed equal -0.5 is optimal for these (maximizing sum of cubes). 

But wait, is equal really optimal? Let me verify. We have 4 variables in [-1,2] summing to -2, maximize sum of cubes. 

The cube function on [-1, 2]: f''(x)=6x. For x<0 concave, x>0 convex. 

Lagrangian: at interior optimum, 3x_i^2 = λ for all free i, so all free x_i equal in absolute value. 

Consider candidates: variables at boundary 2 or -1, or interior with |x| equal.

If some interior positive x=p>0 and some interior negative x=-p (same |value|): but 3p^2 = λ means same λ. Let a be count at +p, b at -p, c at 2, d at -1. Sum: ap - bp + 2c - d = -2. Cubes: a p^3 - b p^3 + 8c - d = maximize.

This is getting complex. Let me just check: is 47.5 the answer, or can we do better?

Let me try: 6 at 2, and 4 variables. What if 3 at -1 and 1 at 1? Sum: 12 - 3 + 1 = 10. ✓. Cubes: 48 - 3 + 1 = 46. Worse.

What about 6 at 2, 1 at -1, 3 at -1/3? Sum 12-1-1=10. Cubes 48-1-3/27=48-1-0.111=46.889. Worse.

6 at 2, 4 at -0.5: sum 12-2=10, cubes 48-0.5=47.5. 

What about 5 at 2, and 5 variables summing to 0? We found 5 at 0 gives 40, or 1 at 2 + 4 at -0.5 gives 47.5 (same as 6+4). What about 5 at 2, 1 at 1, 4 at -0.75? Sum 10+1-3=8? No: 5*2=10, +1=11, +4*(-0.75)=-3, total 8. Not 10. 

5 at 2 (sum 10), remaining 5 sum to 0. To maximize cubes of 5 vars summing to 0 in [-1,2]. Equal at 0: cubes 0. Mixed: 1 at 2, 4 at -0.5: sum 2-2=0, cubes 8-0.5=7.5. So total 40+7.5=47.5. Or 2 at 2, 3 at -4/3: infeasible (<-1). Or 1 at 2, 1 at -1, 3 at -1/3: sum 2-1-1=0, cubes 8-1-1/9=6.889. Worse. Or 1 at 2, 3 at -1, 1 at 1: sum 2-3+1=0, cubes 8-3+1=6. Worse.

So 47.5 keeps appearing. Let me check if anything beats it.

What about not using 2's fully? Like 6 at 2 is max possible 2's. What about 6 at 2, 4 at -0.5 = 47.5.

Could a completely different config beat it? Let me think about upper bound. 

Actually, let me try 6 at 2, and among 4 remaining, push to extremes differently. We need 4 vars in [-1,2] sum -2, maximize cubes. 

Let me parametrize: let t variables at 2, s at -1, rest equal at v. With 4 vars: 
- t=0,s=0: v=-0.5, cubes=-0.5
- t=1: remaining 3 sum -4, min -3, infeasible
- t=0,s=1: remaining 3 sum -1, v=-1/3, cubes=-1-1/9=-1.111
- t=0,s=2: remaining 2 sum 0, v=0, cubes=-2
- t=0,s=3: remaining 1 sum 1, v=1, cubes=-3+1=-2
- t=0,s=4: sum -4≠-2 infeasible

So best is t=0,s=0: -0.5. Total 47.5.

Now let me also check: maybe fewer than 6 at 2 but with creative arrangement beats 47.5.

Let me try 4 at 2, 6 variables summing to 2. Maximize cubes. 6 vars in [-1,2] sum 2. 
- All equal: 1/3, cubes 6*(1/27)=0.222. Total 32.222.
- 1 at 2, 5 at 0: sum 2, cubes 8. Total 40.
- 1 at 2, 1 at -1, 4 at 0.25: sum 2-1+1=2, cubes 8-1+4*0.0156=7.06. Total 39.06.
- 1 at 2, 4 at -1, 1 at 2: that's 2 at 2, 4 at -1, sum 4-4=0≠2.
- 2 at 2, 4 at -0.5: sum 4-2=2, cubes 16-0.5=15.5. Total 32+15.5=47.5! Same again.

Interesting, 47.5 again. So 4 at 2 + 2 at 2 + 4 at -0.5 = 6 at 2 + 4 at -0.5.

- 2 at 2, 3 at -1, 1 at 1: sum 4-3+1=2, cubes 16-3+1=14. Total 46. Worse.
- 3 at 2, 3 at -4/3: infeasible.
- 2 at 2, 1 at -1, 3 at -1/3: sum 4-1-1=2, cubes 16-1-1/9=14.889. Total 46.889.

So 47.5 is the pattern. Let me check 3 at 2, 7 vars sum 4.
- 3 at 2, 3 at 2, ... = 6 at 2, 4 at -0.5 → 47.5.
- 3 at 2, 1 at 2, 6 at 1/3: sum 6+2+2=10, cubes 24+8+6/27=32.222. Worse.

It really seems 47.5 is the max. Let me try to prove it rigorously and also double check there's nothing higher with a weird config.

Let me try: 6 at 2, 4 at -0.5. Sum = 12 - 2 = 10. ✓ Cubes = 48 - 0.5 = 47.5.

Can we get higher? Let me try 6 at 2, 3 at -1, 1 at 1: sum 12-3+1=10, cubes 48-3+1=46. No.

6 at 2, 2 at -1, 2 at 0: sum 12-2=10, cubes 48-2=46. No.

What about 6 at 2, 1 at 2... no that's 7.

Let me try asymmetric: 6 at 2, 1 at -1, 1 at 0, 2 at -0.5: sum 12-1+0-1=10, cubes 48-1+0-0.25=46.75. No.

What about 5 at 2, 1 at 2, ... same.

Let me try: 6 at 2, 4 at -0.5 = 47.5. 

What about 6 at 2, and 4 vars not all -0.5 but optimizing? We proved -0.5 equal is optimal for that subproblem.

Now, is 6 at 2 optimal number of 2's? More than 6 infeasible. With 6 at 2 we get 47.5. With 5 at 2, best remaining gives 47.5 (which reduces to 6+4). With 4 at 2, best gives 47.5. So the max is achieved at 47.5 and these are all the same point essentially (6 at 2, 4 at -0.5).

Wait, but are there configs with fewer 2's that beat 47.5? Let me check 0 at 2: all in [-1,2] sum 10. Max cubes? 10 vars sum 10 avg 1. To maximize, push to 2 and -1. If a at 2, b at -1, rest equal. a*2 - b + (10-a-b)*v = 10. To maximize cubes 8a - b + (10-a-b)v^3. We saw a=6,b=0,v=-0.5 gives 47.5. 

Let me verify there's no config beating 47.5 by considering the Lagrangian more carefully, or just trust the pattern.

Actually, let me try a potentially tricky one: 6 at 2, 1 at 2 is 7, infeasible. What about 6 at 2, and 4 vars where some are at 2? No, that makes 7+ at 2.

Let me try 6 at 2, 4 at -0.5. Could we do 6 at 2, 2 at -1, 1 at 2... no.

Hmm what about configs with values at 2 and -1 only? a at 2, b at -1, a+b=10, 2a-b=10 → 2a-(10-a)=10 → 3a=20 → a=20/3 not integer. So no pure {-1,2} solution. Need fractional.

Let me also check: 6 at 2, 4 at -0.5: 47.5. What about 6 at 2, 3 at -2/3, 1 at 0: sum 12 - 2 + 0 = 10, cubes 48 + 3*(-8/27) = 48 - 8/9 = 47.111. Worse.

What about 6 at 2, 2 at -1, 2 at 0: 48 - 2 = 46. Worse.

I'm fairly confident the answer is 47.5 = 95/2.

Let me now also verify by trying to see if we can exceed. Consider general: let a variables at 2, and the rest (10-a) at value v = (10-2a)/(10-a). Feasible when v ∈ [-1, 2].

v ≥ -1: (10-2a)/(10-a) ≥ -1 → 10-2a ≥ -(10-a) = -10+a → 10-2a ≥ -10+a → 20 ≥ 3a → a ≤ 20/3 ≈ 6.67. So a ≤ 6.
v ≤ 2: (10-2a)/(10-a) ≤ 2 → 10-2a ≤ 20-2a → 10 ≤ 20. Always true.

So a ∈ {0,...,6}. We computed:
- a=6: v=-0.5, cubes=48+4*(-0.125)=48-0.5=47.5
- a=5: v=0, cubes=40
- a=4: v=1/3, cubes=32+6/27=32.222
- a=3: v=4/7, cubes=24+7*(4/7)^3=24+7*64/343=24+448/343=24+1.306=25.306
- a=2: v=0.75, cubes=16+8*0.4219=19.375
- a=1: v=8/9, cubes=8+9*0.702=14.32
- a=0: v=1, cubes=10

Max among these "one-value" solutions: a=6, 47.5.

But the true max might use multiple distinct values. However, we showed that for the subproblem with a=6 (4 vars sum -2), equal is optimal. And for a<6, the optimal further splits also lead back to the a=6 config (e.g., a=5 then split one to 2 and rest to -0.5 gives a=6 config).

But could a non-boundary, multi-value solution beat 47.5? Let me think about KKT.

At a maximum of a continuous function on a compact set, KKT conditions. The objective f = Σx_i^3, constraint g = Σx_i - 10 = 0, box constraints -1 ≤ x_i ≤ 2.

Lagrangian: L = Σx_i^3 - λ(Σx_i - 10) + Σμ_i(x_i - 2) - Σν_i(x_i + 1).

KKT: 3x_i^2 - λ + μ_i - ν_i = 0, with μ_i ≥ 0 (active when x_i=2), ν_i ≥ 0 (active when x_i=-1), μ_i(x_i-2)=0, ν_i(x_i+1)=0.

For interior x_i (not at boundary): μ_i=ν_i=0, so 3x_i^2 = λ, meaning x_i = ±√(λ/3). So interior variables take at most two values: +p or -p where p=√(λ/3).

At our candidate: 6 at 2 (boundary, μ>0), 4 at -0.5 (interior, so 3*(0.25)=0.75=λ, p=0.5). Check boundary condition for x_i=2: 3*4 - λ + μ_i = 0 → 12 - 0.75 + μ_i = 0 → μ_i = -11.25 < 0. 

That's a problem! μ_i should be ≥ 0. This means the KKT condition fails at x_i=2 — the objective wants to increase x_i beyond 2 but can't, which is fine for a max (μ_i < 0 would mean... wait let me recheck sign convention).

Hmm, let me redo. For maximization with constraint x_i ≤ 2: we add term -μ_i(x_i - 2) with μ_i ≥ 0 (penalizing x_i > 2). Then dL/dx_i = 3x_i^2 - λ - μ_i + ν_i = 0 (with ν_i for x_i ≥ -1, term +ν_i(x_i+1), ν_i≥0).

At x_i = 2: 3*4 - λ - μ_i = 0 → 12 - 0.75 - μ_i = 0 → μ_i = 11.25 ≥ 0. ✓ Good.

At x_i = -0.5 (interior): 3*0.25 - λ = 0 → λ = 0.75. ✓

At x_i = -0.5, check ν_i = 0 (not at -1 boundary). ✓

So KKT satisfied with λ=0.75, μ_i=11.25 for the six 2's, ν_i=0. All conditions met. This is a KKT point.

Is it the global max? The feasible set is compact, objective continuous, so global max exists. KKT points are candidates. We need to check this is the global max among all KKT points.

Other KKT points: various combinations. But given the pattern that all "improvement" directions lead to this same point and all other candidates give lower values, I'm confident.

Actually, let me also check a KKT point with some at -1. Suppose b at -1, a at 2, rest interior at ±p. 

At x_i=-1: 3*1 - λ + ν_i = 0 → 3 - λ + ν_i = 0 → ν_i = λ - 3. Need ν_i ≥ 0 → λ ≥ 3. Then p = √(λ/3) ≥ 1. Interior values ±p with p≥1, but interior must be in (-1,2), so p ∈ [1,2) for +p, and -p ≤ -1 not interior (would be at boundary). So if λ ≥ 3, interior positive value p ∈ [1,2). 

Let me try: b at -1, some at +p (interior, p∈[1,2)), some at 2. Let a at 2, c at p, b at -1. a+b+c=10. Sum: 2a + cp - b = 10. Cubes: 8a + cp^3 - b. λ=3p^2, and at x=2: μ = 12 - 3p^2 ≥ 0 → p^2 ≤ 4 → p ≤ 2 ✓. At x=-1: ν = 3p^2 - 3 ≥ 0 → p ≥ 1 ✓.

So p ∈ [1, 2]. Let me explore. We want to maximize 8a + cp^3 - b with 2a + cp - b = 10, a+b+c=10, a,b,c ≥ 0 integers.

From sum: b = 2a + cp - 10. From count: c = 10 - a - b = 10 - a - (2a + cp - 10) = 20 - 3a - cp. So c + cp = 20 - 3a → c(1+p) = 20 - 3a → c = (20-3a)/(1+p). And b = 2a + cp - 10.

Need b ≥ 0: 2a + cp ≥ 10. And c ≥ 0: 20 - 3a ≥ 0 → a ≤ 6.

Cubes = 8a + cp^3 - b = 8a + cp^3 - 2a - cp + 10 = 6a + cp(p^2-1) + 10.

Substitute c = (20-3a)/(1+p): cp = (20-3a)p/(1+p), cp(p^2-1) = (20-3a)p(p^2-1)/(1+p) = (20-3a)p(p-1)(p+1)/(1+p) = (20-3a)p(p-1).

So cubes = 6a + (20-3a)p(p-1) + 10.

Let me denote this as F(a,p) = 6a + 10 + (20-3a)p(p-1), with p ∈ [1,2], a ∈ {0,...,6}, and need b=2a+cp-10 ≥ 0 where c=(20-3a)/(1+p).

b = 2a + (20-3a)p/(1+p) - 10. Let me check feasibility. 

To maximize F: ∂F/∂p = (20-3a)(2p-1). For a ≤ 6, 20-3a ≥ 2 > 0, and 2p-1 > 0 for p≥1. So F increasing in p. Max at p=2.

At p=2: F = 6a + 10 + (20-3a)*2*1 = 6a + 10 + 40 - 6a = 50.

Wait, F=50 at p=2?! That's higher than 47.5! Let me check feasibility at p=2.

At p=2: c = (20-3a)/3, b = 2a + 2c - 10 = 2a + 2(20-3a)/3 - 10 = 2a + (40-6a)/3 - 10 = (6a + 40 - 6a - 30)/3 = 10/3.

So b = 10/3, c = (20-3a)/3. Need b,c ≥ 0 and a + b + c = 10. a + 10/3 + (20-3a)/3 = a + (10 + 20 - 3a)/3 = a + (30-3a)/3 = a + 10 - a = 10. ✓

But b = 10/3 is not an integer! b is the count of variables at -1, must be a non-negative integer. So p=2 with integer a,b,c is infeasible unless b is integer.

Hmm, but actually a, b, c don't all need to be integers — they're counts of variables, so they must be non-negative integers. b=10/3 is not integer. So p=2 exactly is infeasible.

But we can take p close to 2. Wait, but p is determined by λ which is free. Let me reconsider — a, b, c must be integers (counts), but p is continuous. So we need c = (20-3a)/(1+p) to be a non-negative integer, and b = 2a + cp - 10 to be a non-negative integer.

Let me reconsider. Actually we don't need c and b to make p=2 exactly. Let me find feasible (a, b, c, p) with p ∈ [1,2] and check F.

We have c = (20-3a)/(1+p) must be a non-negative integer, b = 10 - a - c must be a non-negative integer, and b = 2a + cp - 10 ≥ 0.

Let me just enumerate integer a, c and solve for p. From c(1+p) = 20 - 3a → p = (20-3a)/c - 1 = (20-3a-c)/c. Need p ∈ [1,2]: 1 ≤ (20-3a-c)/c ≤ 2 → c ≤ 20-3a-c ≤ 2c → 2c ≤ 20-3a and 20-3a ≤ 3c → c ≥ (20-3a)/3 and c ≤ (20-3a)/2.

And b = 10 - a - c ≥ 0 → c ≤ 10 - a. And b = 2a + cp - 10 = 2a + (20-3a-c) - 10 = 10 - 3a + (20-3a-c)... wait let me recompute. cp = 20-3a-c. b = 2a + cp - 10 = 2a + 20 - 3a - c - 10 = 10 - a - c. Consistent. Need b ≥ 0: c ≤ 10-a.

F = 6a + 10 + (20-3a)p(p-1) where p = (20-3a-c)/c.

Let me just enumerate. a from 0 to 6.

a=6: 20-18=2. c ∈ [2/3, 1] ∩ integers, c ≤ 4. c=1: p=(2-1)/1=1. F=36+10+2*1*0=46. b=10-6-1=3. Check: 6 at 2, 1 at p=1, 3 at -1. Sum=12+1-3=10 ✓. Cubes=48+1-3=46. Less than 47.5.

a=5: 20-15=5. c ∈ [5/3, 5/2]=[1.67,2.5], c≤5. c=2: p=(5-2)/2=1.5. F=30+10+5*1.5*0.5=40+3.75=43.75. b=10-5-2=3. Check: 5 at 2, 2 at 1.5, 3 at -1. Sum=10+3-3=10 ✓. Cubes=40+2*3.375-3=40+6.75-3=43.75. Less.

a=4: 20-12=8. c ∈ [8/3, 4]=[2.67,4], c≤6. c=3: p=(8-3)/3=5/3≈1.667. F=24+10+8*(5/3)*(2/3)=34+8*10/9=34+8.889=42.889. c=4: p=(8-4)/4=1. F=24+10+0=34. Less.

a=3: 20-9=11. c∈[11/3,11/2]=[3.67,5.5], c≤7. c=4: p=(11-4)/4=1.75. F=18+10+11*1.75*0.75=28+14.4375=42.4375. c=5: p=(11-5)/5=1.2. F=28+11*1.2*0.2=28+2.64=30.64. Less.

a=2: 20-6=14. c∈[14/3,7]=[4.67,7], c≤8. c=5: p=(14-5)/5=1.8. F=12+10+14*1.8*0.8=22+20.16=42.16. c=6: p=(14-6)/6=4/3. F=22+14*(4/3)*(1/3)=22+56/9=22+6.22=28.22. c=7: p=1. F=22. Less.

a=1: 20-3=17. c∈[17/3,17/2]=[5.67,8.5], c≤9. c=6: p=(17-6)/6=11/6≈1.833. F=6+10+17*(11/6)*(5/6)=16+17*55/36=16+25.97=41.97. c=7: p=10/7. F=16+17*(10/7)*(3/7)=16+17*30/49=16+10.41=26.41. Less.

a=0: 20. c∈[20/3,10]=[6.67,10], c≤10. c=7: p=13/7. F=10+20*(13/7)*(6/7)=10+20*78/49=10+31.84=41.84. c=8: p=12/8=1.5. F=10+20*1.5*0.5=10+15=25. c=10: p=1. F=10. Less.

So all these KKT points with some at -1 give less than 47.5. The max among them is a=6,c=1,p=1 giving 46, still less.

Now the other family: no variables at -1, interior at ±p with p ≤ 1 (so that -p > -1, interior). Actually if no -1 boundary, then interior values are ±p with p = √(λ/3), and λ < 3 means p < 1 (so -p > -1, valid interior). And 2's at boundary.

Let me set up: a at 2, c at +p, d at -p, no -1's. a+c+d=10. Sum: 2a + cp - dp = 10 → 2a + (c-d)p = 10. Cubes: 8a + (c-d)p^3 = 8a + (c-d)p^3. Let e = c - d. Then 2a + ep = 10, cubes = 8a + ep^3. Also c+d = 10-a, and e=c-d so c=(10-a+e)/2, d=(10-a-e)/2, need c,d ≥ 0 integers → 10-a ≥ |e| and parity.

From 2a + ep = 10 → ep = 10-2a → e = (10-2a)/p. Cubes = 8a + ep*p^2 = 8a + (10-2a)p^2.

To maximize over p: dF/dp = (10-2a)*2p. For a < 5, 10-2a > 0, increasing in p. For a > 5, decreasing. For a=5, constant = 40.

Constraints: p ∈ (0, 1) (interior, p<1 so -p>-1), and c,d ≥ 0 integers, e = (10-2a)/p.

Hmm, also need p such that e makes c,d integers. This is getting complicated. Let me think about it differently.

Actually, the case a=6, d=4 at -p: 2*6 + (0-4)p = 10 → 12 - 4p = 10 → p = 0.5. c=0, d=4. Cubes = 48 + (-4)(0.125) = 48 - 0.5 = 47.5. ✓ This is our solution!

For a=6, p=0.5, F = 8*6 + (10-12)*0.25 = 48 - 0.5 = 47.5. 

For a < 5, F = 8a + (10-2a)p^2, increasing in p, max at p→1 (but p<1 for interior). As p→1, F → 8a + 10-2a = 6a+10. At a=4: 34. At a=0: 10. These are less than 47.5.

Wait but at p=1, -p = -1 which is boundary, not interior. So the limit approaches the -1 boundary case. Anyway, all less than 47.5.

For a=5: F = 40 + 0 = 40 regardless of p. But need 2*5 + ep = 10 → ep = 0 → e=0 (since p>0). So c=d. c+d=5, c=d → not integer. So a=5 with this family: c=d=2.5 infeasible. Actually need c,d integers with c+d=5, c=d impossible. So no valid solution here except... hmm. Actually e=0 means c=d, but c+d=5 odd. Infeasible. So a=5 gives nothing in this family.

For a=6: F = 48 + (-2)p^2 = 48 - 2p^2, decreasing in p. Min... we want max, so p as small as possible. p=0.5 from constraint (e=(10-12)/p=-2/p, need d=(10-6-e)/2... let me recompute. a=6, c+d=4, e=c-d. 2*6+ep=10→ep=-2→e=-2/p. d=(4-e)/2=(4+2/p)/2=2+1/p. Need d ≤ 4 (since c+d=4, d≥0): 2+1/p ≤ 4 → 1/p ≤ 2 → p ≥ 0.5. And d integer, c=4-d integer. At p=0.5: d=2+2=4, c=0. ✓ F=48-2*0.25=47.5. At p>0.5, d=2+1/p, need integer. p=2/3: d=2+1.5=3.5 not integer. p=1: d=3, c=1, but p=1 means -p=-1 boundary. F=48-2=46. So p=0.5 is the feasible max for a=6.

Great, so 47.5 is confirmed as the global max.

So the maximum is 47.5 = 95/2.

Now let me write the proof.

Proof structure:
1. Show 47.5 is achievable: x_1=...=x_6=2, x_7=...=x_10=-1/2. Sum=12-2=10. Cubes=48-4/8=48-0.5=47.5.
2. Show it's the maximum.

For the upper bound, I'll use a tangent line / supporting parabola argument. We want to find a quadratic (or linear) function that dominates x^3 on [-1,2] and use the sum constraint.

Actually, a clean approach: find constants α, β such that x^3 ≤ αx + β for all x ∈ [-1,2], with equality at x=2 and x=-1/2. Then Σx_i^3 ≤ αΣx_i + 10β = 10α + 10β... wait, Σx_i = 10, so Σx_i^3 ≤ α*10 + 10β = 10(α+β). We want this to equal 47.5.

The quadratic αx + β tangent to x^3 at x=2 and x=-1/2. At x=2: 8 = 2α+β. At x=-1/2: -1/8 = -α/2+β. Subtract: 8+1/8 = 2α+α/2 = 5α/2 → 65/8 = 5α/2 → α = 65/8 * 2/5 = 130/40 = 13/4. β = 8 - 2*13/4 = 8 - 13/2 = 3/2.

So claim: x^3 ≤ (13/4)x + 3/2 for all x ∈ [-1,2].

Check: x^3 - (13/4)x - 3/2 ≤ 0. Factor: we know roots at x=2 and x=-1/2. x^3 - (13/4)x - 3/2 = (x-2)(x+1/2)(x - r). Expand (x-2)(x+1/2) = x^2 - 3x/2 - 1. Times (x-r): x^3 - rx^2 - 3x^2/2 + 3rx/2 - x + r = x^3 - (r+3/2)x^2 + (3r/2 - 1)x + r. 

Compare to x^3 - (13/4)x - 3/2: coefficient of x^2 is 0 → r = -3/2. Then coefficient of x: 3(-3/2)/2 - 1 = -9/4 - 1 = -13/4. ✓ Constant: r = -3/2. ✓

So x^3 - (13/4)x - 3/2 = (x-2)(x+1/2)(x+3/2).

On [-1, 2]: x-2 ≤ 0, x+1/2 ≥ -1/2 (can be negative when x < -1/2), x+3/2 ≥ 1/2 > 0.

So sign = (x-2)(x+1/2)(x+3/2). x+3/2 > 0 always on [-1,2]. x-2 ≤ 0 always. So sign = -(positive)(x+1/2) = ... let me think. (x-2) ≤ 0, (x+3/2) > 0, so (x-2)(x+3/2) ≤ 0. Then times (x+1/2): 

If x ≥ -1/2: (x+1/2) ≥ 0, so product ≤ 0. ✓ (x^3 ≤ line)
If x < -1/2: (x+1/2) < 0, and (x-2)(x+3/2) < 0, so product = (neg)(neg) > 0. ✗!

So the inequality x^3 ≤ (13/4)x + 3/2 FAILS for x ∈ [-1, -1/2). 

Hmm. So this linear bound doesn't work globally. The cubic exceeds the line on [-1, -1/2).

So I need a different supporting function. The issue is that x^3 is concave on [-1, 0], so a chord/secant might be needed, or a quadratic upper bound.

Let me reconsider. Since x^3 is concave on [-1,0], the secant line on [-1, -1/2] lies below the curve, not above. So a single line can't dominate x^3 on all of [-1,2] while being tight at 2 and -1/2.

Alternative: use a quadratic upper bound. Find αx^2 + βx + γ ≥ x^3 on [-1,2], tight at x=2 and x=-1/2 (double root at -1/2 since it's an interior tangent point).

At interior tangent point x=-1/2: the quadratic touches x^3, so q(x) - x^3 has a double root at x=-1/2. And q(2) = 8.

q(x) - x^3 = -(x+1/2)^2(x-2) (degree 3, leading coeff -1 to match -x^3... wait x^3 has leading coeff 1, q is degree 2, so q-x^3 has leading coeff -1). 

q(x) - x^3 = -(x+1/2)^2(x-2). Check leading coeff: -(x^2)(x) = -x^3. ✓

So q(x) = x^3 - (x+1/2)^2(x-2). Let me expand (x+1/2)^2 = x^2 + x + 1/4. Times (x-2): x^3 - 2x^2 + x^2 - 2x + x/4 - 1/2 = x^3 - x^2 - 7x/4 - 1/2. 

So q(x) = x^3 - (x^3 - x^2 - 7x/4 - 1/2) = x^2 + 7x/4 + 1/2.

Check: q(2) = 4 + 7/2 + 1/2 = 4 + 4 = 8. ✓ q(-1/2) = 1/4 - 7/8 + 1/2 = 2/8 - 7/8 + 4/8 = -1/8. ✓ (equals (-1/2)^3 = -1/8).

Now need q(x) ≥ x^3 on [-1,2], i.e., q(x) - x^3 = -(x+1/2)^2(x-2) ≥ 0. Since (x+1/2)^2 ≥ 0 and (x-2) ≤ 0 on [-1,2], we have -(x+1/2)^2(x-2) ≥ 0. ✓✓✓

So x^3 ≤ x^2 + 7x/4 + 1/2 for all x ∈ [-1,2], with equality at x=2 and x=-1/2.

Now sum: Σx_i^3 ≤ Σx_i^2 + (7/4)Σx_i + 10*(1/2) = Σx_i^2 + (7/4)*10 + 5 = Σx_i^2 + 35/2 + 5 = Σx_i^2 + 45/2.

Hmm, but this involves Σx_i^2 which we don't know. We need another relation.

We have Σx_i = 10. We need to bound Σx_i^2. By Cauchy-Schwarz or other... Actually we want to show Σx_i^3 ≤ 95/2. From above, Σx_i^3 ≤ Σx_i^2 + 45/2. So need Σx_i^2 ≤ 25.

Is Σx_i^2 ≤ 25 given Σx_i = 10, x_i ∈ [-1,2]? At our optimum, 6 at 2, 4 at -1/2: Σx_i^2 = 6*4 + 4*(1/4) = 24 + 1 = 25. So Σx_i^2 = 25 at optimum.

Is Σx_i^2 ≤ 25 always? Σx_i^2 is convex, maximized at vertices of the polytope. The vertices have variables at 2 or -1. With a at 2, b at -1, a+b=10, 2a-b=10 → a=20/3, not integer. So no vertex with only {-1,2}. The polytope has vertices where 9 variables are at boundary and 1 is free. 

Hmm, this is getting complicated. Let me think differently. Actually, maybe I should find a linear bound that works, by being tight at x=2 and x=-1 (the two endpoints), and check it's an upper bound.

Line through (2, 8) and (-1, -1): slope = 9/3 = 3. Line: y = 3x + 2 (since 3*2+2=8, 3*(-1)+2=-1). 

Is x^3 ≤ 3x + 2 on [-1,2]? x^3 - 3x - 2 = (x-2)(x+1)^2. On [-1,2]: (x-2) ≤ 0, (x+1)^2 ≥ 0, so product ≤ 0. ✓✓✓ 

So x^3 ≤ 3x + 2 on [-1,2], with equality at x=2 and x=-1.

Sum: Σx_i^3 ≤ 3Σx_i + 2*10 = 30 + 20 = 50.

This gives upper bound 50, but our candidate is 47.5. Not tight enough.

The issue: equality requires all x_i ∈ {2, -1}, but that's infeasible (sum would be 2a - (10-a) = 3a-10 = 10 → a=20/3, not integer).

So the linear bound gives 50 but it's not achievable. We need a tighter bound.

Let me go back to the quadratic approach but handle Σx_i^2.

We have x^3 ≤ x^2 + 7x/4 + 1/2 (tight at 2 and -1/2). Sum gives Σx_i^3 ≤ Σx_i^2 + 45/2.

Now I need to show Σx_i^2 ≤ 25 when Σx_i = 10, x_i ∈ [-1,2].

Claim: Σx_i^2 ≤ 25. Proof: Consider x_i^2 on [-1,2]. We want an upper bound. x^2 ≤ ? Linear bound tight at x=2 and x=-1/2: line through (2,4) and (-1/2, 1/4): slope = (4-1/4)/(2+1/2) = (15/4)/(5/2) = 15/4 * 2/5 = 3/2. Line: y - 4 = (3/2)(x-2) → y = (3/2)x + 1. Check at -1/2: -3/4 + 1 = 1/4. ✓

Is x^2 ≤ (3/2)x + 1 on [-1,2]? x^2 - (3/2)x - 1 = (x-2)(x+1/2). On [-1,2]: (x-2) ≤ 0. (x+1/2) ≥ -1/2. So product: if x ≥ -1/2, (x+1/2)≥0, product ≤ 0 ✓. If x < -1/2, (x+1/2) < 0, (x-2) < 0, product > 0 ✗.

Same issue. Fails on [-1, -1/2).

Hmm. Let me try a quadratic bound for x^2. Actually x^2 is convex, so a line can't dominate it on an interval unless... a secant line of a convex function lies above. Wait, for convex functions, the secant line lies ABOVE the function. So x^2 ≤ secant on [-1,2]. Secant through (-1,1) and (2,4): slope=1, y = x+2. Check: x^2 ≤ x+2 → x^2-x-2 ≤ 0 → (x-2)(x+1) ≤ 0 on [-1,2] ✓. 

So x^2 ≤ x + 2 on [-1,2]. Sum: Σx_i^2 ≤ Σx_i + 20 = 10 + 20 = 30. Not tight (gives Σx_i^3 ≤ 30 + 22.5 = 52.5).

This isn't working well. Let me think of a direct approach.

Alternative direct proof: We want to show Σx_i^3 ≤ 95/2.

Let me use the quadratic bound x^3 ≤ x^2 + 7x/4 + 1/2 (tight at 2, -1/2) AND separately bound Σx_i^2.

Actually, let me combine. We have:
- x^3 ≤ x^2 + (7/4)x + 1/2, equality at x=2, x=-1/2.

Σx_i^3 ≤ Σx_i^2 + (7/4)(10) + 5 = Σx_i^2 + 45/2.

Now bound Σx_i^2. Use x^2 ≤ (3/2)x + 1 (tight at 2, -1/2) but this fails on [-1,-1/2). 

Alternatively use a quadratic in x that upper bounds x^2 and uses both Σx_i and Σx_i^2... circular.

Let me try yet another approach. Directly find the best linear upper bound for x^3 that, combined with Σx_i = 10, gives 95/2. We need a line αx + β ≥ x^3 on [-1,2] with 10α + 10β = 95/2, i.e., α + β = 19/4.

But we showed the line through (2,8) and (-1/2,-1/8) gives α=13/4, β=3/2, α+β = 13/4+3/2 = 13/4+6/4 = 19/4. ✓ And 10*(19/4) = 190/4 = 47.5 = 95/2. ✓✓

But this line does NOT dominate x^3 on [-1, -1/2). So we can't use it directly.

The problem is that on [-1, -1/2), x^3 > line. So if any x_i ∈ [-1, -1/2), the bound fails.

But at the optimum, all x_i are either 2 or -1/2, so all are at equality points. The issue is proving no other config does better.

Key insight: we need to handle the region [-1, -1/2) separately. 

Let me think about it more carefully. The function g(x) = x^3 - (13/4)x - 3/2 = (x-2)(x+1/2)(x+3/2). On [-1,2]:
- x ∈ [-1, -1/2): g(x) > 0 (cubic exceeds line)
- x = -1/2: g = 0
- x ∈ (-1/2, 2): g(x) < 0
- x = 2: g = 0

So for x ∈ [-1, -1/2), the cubic is above the line. The excess is g(x) > 0.

So Σx_i^3 = Σ[(13/4)x_i + 3/2 + g(x_i)] = (13/4)(10) + 15 + Σg(x_i) = 65/2 + 15 + Σg(x_i) = 95/2 + Σg(x_i).

So Σx_i^3 = 95/2 + Σg(x_i). We need to show Σg(x_i) ≤ 0.

g(x) = (x-2)(x+1/2)(x+3/2). g(x) > 0 for x ∈ [-1, -1/2), g(x) ≤ 0 for x ∈ [-1/2, 2], g(x) = 0 at x=-1/2, 2.

So if any x_i ∈ [-1, -1/2), it contributes positively to Σg. We need to show the negative contributions from other variables outweigh.

Hmm, this requires using the sum constraint. Let me think.

Let me define the "bad" variables (in [-1,-1/2)) and "good" variables (in [-1/2, 2]). 

For bad variables, g(x) > 0. For good variables not at {2, -1/2}, g(x) < 0.

This is getting complicated. Let me try a cleaner approach.

Alternative: Use the fact that on [-1, 2], we can write x^3 = (13/4)x + 3/2 + (x-2)(x+1/2)(x+3/2), and then show that Σ(x_i - 2)(x_i + 1/2)(x_i + 3/2) ≤ 0 given Σx_i = 10.

Let h(x) = (x-2)(x+1/2)(x+3/2) = x^3 - (13/4)x - 3/2.

We need Σh(x_i) ≤ 0.

Note h(x) = (x-2)(x+1/2)(x+3/2). Let's substitute y_i = x_i + 1/2, so x_i = y_i - 1/2, y_i ∈ [-1/2, 5/2]. Sum: Σy_i = 10 + 5 = 15.

h(x_i) = (y_i - 5/2)(y_i)(y_i + 1) = y_i(y_i+1)(y_i - 5/2).

Hmm, let me try another substitution. Let me think about what makes this tractable.

Actually, let me try a different, more direct proof using convexity/concavity arguments.

The function φ(x) = x^3 is convex on [0,2] and concave on [-1,0].

Claim: At the maximum, all x_i ∈ {2} ∪ (-1, 0) or at -1/2. 

Actually, let me use a cleaner method. Let me prove that the maximum is 95/2 by showing any feasible point has Σx_i^3 ≤ 95/2.

Approach via "smoothing/merging": Show that if two variables are both in (0, 2) (interior of convex region), we can increase the objective by pushing them apart (one toward 2, other toward 0). Similarly for other cases. This leads to the conclusion that at optimum, at most one variable is in the interior of (0,2) and at most one in interior of (-1, 0), etc.

This is the standard "mixing variables" technique. Let me sketch:

Lemma (convex region): If x_i, x_j ∈ [0, 2] with x_i + x_j = S (fixed), then x_i^3 + x_j^3 is maximized when one is as large as possible (2 or S-0) and other as small. Because x^3 convex on [0,2], sum is maximized at endpoints.

Lemma (concave region): If x_i, x_j ∈ [-1, 0] with fixed sum, x_i^3 + x_j^3 is maximized when they're equal (concavity).

Lemma (mixed): If x_i ∈ [-1,0], x_j ∈ [0,2], with fixed sum... need analysis.

This gets complicated with the mixing across regions. Let me try the algebraic approach more carefully.

Let me revisit: Σx_i^3 = 95/2 + Σh(x_i) where h(x) = (x-2)(x+1/2)(x+3/2). Need Σh(x_i) ≤ 0.

Let me split variables: Let A = {i : x_i ≥ -1/2} and B = {i : x_i < -1/2}. For i ∈ A, h(x_i) ≤ 0. For i ∈ B, h(x_i) > 0.

For i ∈ B, x_i ∈ [-1, -1/2). h(x_i) = (x_i - 2)(x_i + 1/2)(x_i + 3/2). Here x_i - 2 < 0, x_i + 1/2 < 0, x_i + 3/2 > 0 (since x_i ≥ -1 > -3/2). So h = (neg)(neg)(pos) > 0. ✓

Let me bound h on [-1, -1/2). h(-1) = (-3)(-1/2)(1/2) = 3/4. h(-1/2) = 0. h is... let me compute h'(x) = 3x^2 - 13/4. At x ∈ [-1,-1/2], 3x^2 ∈ [3/4, 3], so h'(x) = 3x^2 - 13/4 ∈ [3/4 - 13/4, 3 - 13/4] = [-10/4, -1/4] = [-2.5, -0.25]. So h' < 0 on this interval, h decreasing from h(-1)=3/4 to h(-1/2)=0.

For i ∈ A, x_i ∈ [-1/2, 2]. h(x_i) ≤ 0. The most negative is somewhere in the interior. h'(x) = 3x^2 - 13/4 = 0 → x = ±√(13/12) ≈ ±1.04. On [-1/2, 2], critical point at x = √(13/12) ≈ 1.04. h(√(13/12)) = minimum. 

This is getting messy. Let me try to bound differently.

For x ∈ [-1, -1/2): h(x) ≤ h(-1) = 3/4 (since h decreasing). Actually h(x) ∈ (0, 3/4].

For x ∈ [-1/2, 2]: h(x) ≤ 0, and h(x) ≥ h(√(13/12)).

Hmm. Let me try to use the sum constraint more directly.

Let me denote the variables in B as having x_i = -1/2 - δ_i where δ_i ∈ (0, 1/2] (since x_i ∈ [-1, -1/2)). And variables in A have x_i = -1/2 + ε_i where ε_i ∈ [0, 5/2] (x_i ∈ [-1/2, 2]).

Sum constraint: Σx_i = 10. Σ(-1/2 + ε_i for A) + Σ(-1/2 - δ_i for B) = 10. Let |A| = a, |B| = b, a+b=10. -5 + Σε_i - Σδ_i = 10 → Σε_i - Σδ_i = 15.

h(x_i) for i ∈ A: h(-1/2 + ε) = (ε - 5/2)(ε)(ε + 1) = ε(ε+1)(ε - 5/2). For ε ∈ [0, 5/2], this is ≤ 0 (since ε ≥ 0, ε+1 > 0, ε-5/2 ≤ 0).

h(x_i) for i ∈ B: h(-1/2 - δ) = (-δ - 5/2)(-δ)(-δ + 1) = -(δ + 5/2)(δ)(1 - δ)... let me compute. x = -1/2 - δ. x - 2 = -5/2 - δ. x + 1/2 = -δ. x + 3/2 = 1 - δ. h = (-5/2 - δ)(-δ)(1 - δ) = δ(5/2 + δ)(1 - δ). For δ ∈ (0, 1/2], this is > 0 (δ > 0, 5/2+δ > 0, 1-δ > 0). ✓

So Σh = Σ_{A} ε_i(ε_i+1)(ε_i - 5/2) + Σ_{B} δ_i(5/2 + δ_i)(1 - δ_i).

Need Σh ≤ 0, i.e., Σ_{B} δ_i(5/2 + δ_i)(1 - δ_i) ≤ -Σ_{A} ε_i(ε_i+1)(ε_i - 5/2) = Σ_{A} ε_i(ε_i+1)(5/2 - ε_i).

With constraint Σε_i - Σδ_i = 15, i.e., Σε_i = 15 + Σδ_i.

This is still complex. Let me try to bound each term.

For i ∈ B: δ_i(5/2 + δ_i)(1 - δ_i) ≤ ? Since δ_i ∈ (0, 1/2], and the function is increasing in δ on (0, 1/2]? Let me check: f(δ) = δ(5/2+δ)(1-δ). f'(δ) = (5/2+δ)(1-δ) + δ(1-δ) + δ(5/2+δ)(-1) = (5/2+δ)(1-δ) + δ(1-δ) - δ(5/2+δ). = (1-δ)(5/2+δ+δ) - δ(5/2+δ) = (1-δ)(5/2+2δ) - δ(5/2+δ). = 5/2 + 2δ - 5δ/2 - 2δ^2 - 5δ/2 - δ^2 = 5/2 + 2δ - 5δ - 3δ^2 = 5/2 - 3δ - 3δ^2. At δ=1/2: 5/2 - 3/2 - 3/4 = 5/2 - 9/4 = 1/4 > 0. So f increasing on (0, 1/2]. Max at δ=1/2: f(1/2) = (1/2)(3)(1/2) = 3/4. So each B variable contributes at most 3/4 to Σh.

For i ∈ A: ε_i(ε_i+1)(5/2 - ε_i) ≥ 0 (this is the positive contribution that offsets). We need the A contributions to outweigh B.

Hmm, this approach is getting too algebraically heavy. Let me try a cleaner proof.

Let me reconsider. Maybe use a different supporting function. 

What if I use a piecewise argument: show that for x ∈ [-1, -1/2], x^3 ≤ some function, and for x ∈ [-1/2, 2], x^3 ≤ (13/4)x + 3/2, and combine?

On [-1/2, 2]: x^3 ≤ (13/4)x + 3/2 (proved, since (x-2)(x+1/2)(x+3/2) ≤ 0 here).

On [-1, -1/2]: x^3 is concave (since x < 0). For concave function, x^3 ≤ secant line on [-1, -1/2]. Secant through (-1, -1) and (-1/2, -1/8): slope = (-1/8 + 1)/(1/2) = (7/8)/(1/2) = 7/4. Line: y + 1 = (7/4)(x+1) → y = (7/4)x + 7/4 - 1 = (7/4)x + 3/4. Check at -1/2: -7/8 + 3/4 = -7/8 + 6/8 = -1/8. ✓

So on [-1, -1/2]: x^3 ≤ (7/4)x + 3/4 (concavity, secant above).

Now, for variables in [-1, -1/2]: x_i^3 ≤ (7/4)x_i + 3/4.
For variables in [-1/2, 2]: x_i^3 ≤ (13/4)x_i + 3/2.

Sum: Σx_i^3 ≤ (7/4)Σ_{B} x_i + (3/4)|B| + (13/4)Σ_{A} x_i + (3/2)|A|.

Let |A| = a, |B| = b = 10 - a. Σ_A x_i + Σ_B x_i = 10.

= (7/4)Σ_B x_i + (13/4)Σ_A x_i + 3b/4 + 3a/2
= (13/4)(Σ_A x_i + Σ_B x_i) + (7/4 - 13/4)Σ_B x_i + 3b/4 + 3a/2
= (13/4)(10) - (6/4)Σ_B x_i + 3b/4 + 3a/2
= 65/2 - (3/2)Σ_B x_i + 3b/4 + 3a/2

Now a = 10 - b, so 3a/2 = 15 - 3b/2.

= 65/2 - (3/2)Σ_B x_i + 3b/4 + 15 - 3b/2
= 65/2 + 15 - (3/2)Σ_B x_i + 3b/4 - 3b/2
= 65/2 + 15 - (3/2)Σ_B x_i - 3b/4
= 95/2 - (3/2)Σ_B x_i - 3b/4

Now for i ∈ B, x_i ∈ [-1, -1/2], so Σ_B x_i ∈ [-b, -b/2]. Thus -(3/2)Σ_B x_i ∈ [3b/4, 3b/2].

So Σx_i^3 ≤ 95/2 - (3/2)Σ_B x_i - 3b/4. Since -(3/2)Σ_B x_i ≥ 3b/4 (because Σ_B x_i ≤ -b/2), we get... wait that gives Σx_i^3 ≤ 95/2 + (something ≥ 0). That's the wrong direction!

Let me recompute. -(3/2)Σ_B x_i - 3b/4. Σ_B x_i ≤ -b/2 (most negative is -b, least negative is -b/2). So -(3/2)Σ_B x_i ranges from -(3/2)(-b) = 3b/2 (when Σ_B x_i = -b) to -(3/2)(-b/2) = 3b/4 (when Σ_B x_i = -b/2).

So -(3/2)Σ_B x_i - 3b/4 ranges from 3b/2 - 3b/4 = 3b/4 (when Σ_B x_i = -b) to 3b/4 - 3b/4 = 0 (when Σ_B x_i = -b/2).

So Σx_i^3 ≤ 95/2 + [-(3/2)Σ_B x_i - 3b/4] ≤ 95/2 + 3b/4.

This gives Σx_i^3 ≤ 95/2 + 3b/4, which is > 95/2 when b > 0. Not tight enough!

The bound is tight only when b = 0 (no variables in [-1, -1/2)), giving Σx_i^3 ≤ 95/2. 

So: if all x_i ≥ -1/2, then Σx_i^3 ≤ 95/2, with equality when all x_i ∈ {2, -1/2} and the sum is 10 (which gives 6 at 2, 4 at -1/2).

But what if some x_i < -1/2? We need to show that even then, Σx_i^3 ≤ 95/2.

Hmm, so the piecewise approach shows the bound when b=0 but not when b>0. I need to handle b > 0.

Let me think about this differently. When some variables are in [-1, -1/2), can we "improve" the objective by moving them to -1/2 and adjusting others?

Intuition: if x_i ∈ [-1, -1/2), moving it to -1/2 increases x_i (so we need to decrease others to maintain sum). Since x^3 is increasing, increasing x_i increases its cube, but we must decrease others. The net effect...

Actually, let me think about it as: suppose x_i < -1/2. Consider replacing x_i with -1/2 and decreasing some x_j ∈ [-1/2, 2] by (x_i - (-1/2)) = x_i + 1/2 < 0, i.e., increasing x_j by |x_i + 1/2|... no wait. If x_i increases to -1/2, sum increases by (-1/2 - x_i) > 0, so we need to decrease some other variable by that amount.

This is the mixing/smoothing approach. Let me formalize.

Suppose x_1 ∈ [-1, -1/2) and x_2 ∈ [-1/2, 2]. Replace (x_1, x_2) with (x_1 + t, x_2 - t) for small t > 0 (move x_1 toward -1/2, x_2 down). Sum preserved. Change in objective: (x_1+t)^3 + (x_2-t)^3 - x_1^3 - x_2^3 = 3t(x_1^2 - x_2^2) + 3t^2(x_1 + x_2) + ... 

d/dt [(x_1+t)^3 + (x_2-t)^3] at t=0 = 3x_1^2 - 3x_2^2 = 3(x_1^2 - x_2^2) = 3(x_1 - x_2)(x_1 + x_2).

Since x_1 < -1/2 ≤ x_2, we have x_1 < x_2, so x_1 - x_2 < 0. And x_1 + x_2: could be positive or negative.

If x_1 + x_2 < 0 (i.e., x_2 < -x_1 ≤ 1), then 3(x_1-x_2)(x_1+x_2) = (neg)(neg) > 0, so increasing t increases objective. Good, move x_1 up.

If x_1 + x_2 > 0 (i.e., x_2 > -x_1), then derivative < 0, moving x_1 up decreases objective. So we'd want to move x_1 down (t < 0), toward -1.

So the optimal direction depends on the sign of x_1 + x_2. This means the smoothing isn't always in one direction. Complicated.

Let me reconsider. Maybe the maximum with b > 0 (some variables < -1/2) is actually less than 95/2, and I need a better bound for that case.

Let me just try to verify computationally (in my head) some cases with b > 0.

Case: 7 at 2 is infeasible (sum 14, remaining 3 need -4, min -3). 

Case: 6 at 2, 1 at -1, 3 at -1/3: sum 12 - 1 - 1 = 10. Cubes 48 - 1 - 3/27 = 48 - 1 - 1/9 = 46.889. < 47.5.

Case: 6 at 2, 2 at -1, 2 at 0: sum 12 - 2 = 10. Cubes 48 - 2 = 46. < 47.5.

Case: 6 at 2, 3 at -1, 1 at 1: sum 12 - 3 + 1 = 10. Cubes 48 - 3 + 1 = 46. < 47.5.

Case: 5 at 2, 1 at -1, 4 at 1/4: sum 10 - 1 + 1 = 10. Cubes 40 - 1 + 4/64 = 39 + 1/16 = 39.0625. < 47.5.

Case: 6 at 2, 1 at -0.9, 3 at (-2+0.9)/3 = -1.1/3 ≈ -0.367: sum 12 - 0.9 - 1.1 = 10. Cubes 48 - 0.729 + 3*(-0.0494) = 48 - 0.729 - 0.148 = 47.12. < 47.5.

Case: 6 at 2, 1 at -1, 1 at -1/2, 2 at -1/4: sum 12 - 1 - 0.5 - 0.5 = 10. Cubes 48 - 1 - 0.125 - 2*0.0156 = 46.72. < 47.5.

It really seems 47.5 is the max. Let me try to find a cleaner proof.

Cleaner approach: Let me use the substitution and a single inequality.

We want to show: for x ∈ [-1, 2], x^3 ≤ (13/4)x + 3/2 + c·(x + 1/2)·(something)...

Actually, let me try to find a quadratic q(x) = αx^2 + βx + γ such that x^3 ≤ q(x) on [-1,2] and Σq(x_i) can be bounded using Σx_i = 10 and known bounds on Σx_i^2.

We had q(x) = x^2 + 7x/4 + 1/2 (tight at 2, -1/2, double root). This gives Σx_i^3 ≤ Σx_i^2 + 45/2. Need Σx_i^2 ≤ 25.

So let me prove Σx_i^2 ≤ 25 given Σx_i = 10, x_i ∈ [-1, 2].

Σx_i^2 ≤ 25: This is equivalent to Σx_i^2 ≤ 25. Using x_i^2 = (x_i - 1)^2 + 2x_i - 1... hmm. Σx_i^2 = Σ(x_i - 1)^2 + 2Σx_i - 10 = Σ(x_i-1)^2 + 20 - 10 = Σ(x_i-1)^2 + 10. So Σx_i^2 ≤ 25 ⟺ Σ(x_i - 1)^2 ≤ 15.

Let y_i = x_i - 1 ∈ [-2, 1], Σy_i = 0. Need Σy_i^2 ≤ 15.

Hmm, is this true? y_i ∈ [-2, 1], Σy_i = 0. Maximize Σy_i^2. Since y^2 is convex, max at vertices: y_i ∈ {-2, 1}. Let a at -2, b at 1, a+b=10, -2a+b=0 → b=2a, 3a=10, a=10/3. Not integer. So no pure vertex solution.

Vertices of the polytope {y ∈ [-2,1]^10 : Σy = 0}: 9 variables at boundary, 1 free. Let's say k at -2, (9-k) at 1, one free at v. Sum: -2k + (9-k) + v = 0 → v = 3k - 9. Need v ∈ [-2, 1]: -2 ≤ 3k-9 ≤ 1 → 7 ≤ 3k ≤ 10 → k ∈ {3} (k=3: v=0; k=7/3 no). Wait 7/3 ≤ k ≤ 10/3, so k=3 (v=0) or... k must be integer, k=3 gives v=0. k=10/3 not integer. Actually k can be 3 only (since 7/3 ≈ 2.33 and 10/3 ≈ 3.33, integer k = 3).

Wait, also need to check: with k at -2 and (9-k) at 1, that's 9 variables. The 10th is free. k=3: 3 at -2, 6 at 1, 1 at 0. Σy^2 = 3*4 + 6*1 + 0 = 18. That's > 15!

So Σy_i^2 can be 18 > 15. So Σx_i^2 can be 28 > 25. So the bound Σx_i^2 ≤ 25 is FALSE!

Let me verify: y = (-2,-2,-2,1,1,1,1,1,1,0), x = y+1 = (-1,-1,-1,2,2,2,2,2,2,1). Σx = -3+12+1 = 10. ✓ Σx^2 = 3+24+1 = 28. Σx^3 = -3+48+1 = 46. < 47.5. OK so Σx^2 = 28 but Σx^3 = 46 < 47.5.

So Σx_i^2 ≤ 25 is false, meaning the quadratic bound approach (q = x^2 + 7x/4 + 1/2) gives Σx_i^3 ≤ 28 + 22.5 = 50.5, not tight.

So that approach fails. Back to the drawing board.

Let me reconsider. The piecewise linear approach gave: if all x_i ≥ -1/2, then Σx_i^3 ≤ 95/2. I need to handle the case where some x_i < -1/2.

Let me think about what happens when some x_i < -1/2. Intuitively, pushing a variable below -1/2 "wastes" sum budget (the variable contributes negatively to sum but its cube is also very negative), and the remaining variables can't compensate enough.

Let me try to prove: if any x_i < -1/2, then Σx_i^3 < 95/2.

Approach: Suppose x_1 < -1/2. Consider modifying the solution: set x_1' = -1/2 and adjust. We need to increase sum by (x_1' - x_1) = -1/2 - x_1 > 0, so decrease some other variables. 

Actually, let me think about it as: we want to show that the maximum over the full feasible set equals the maximum over the restricted set {x_i ≥ -1/2 for all i}.

Claim: If (x_1, ..., x_10) is feasible with some x_i < -1/2, then there exists a feasible point with all x_j ≥ -1/2 and Σx_j^3 ≥ Σx_i^3.

If true, then the max over the full set = max over restricted set = 95/2.

To prove the claim: take x_1 < -1/2. We want to increase x_1 to -1/2 (gaining cube since x^3 increasing) and decrease some other variable x_2 > -1/2 by the same amount. The net change in cubes: 

Δ = [(-1/2)^3 - x_1^3] + [(x_2 - (-1/2 - x_1))^3 - x_2^3] where we decrease x_2 by d = -1/2 - x_1 > 0.

Wait, we increase x_1 by d = -1/2 - x_1 > 0 (to -1/2), and decrease x_2 by d (to x_2 - d). Need x_2 - d ≥ -1/2, i.e., x_2 ≥ -1/2 + d = -1/2 + (-1/2 - x_1) = -1 - x_1. Since x_1 ≥ -1, -1 - x_1 ≤ 0. And x_2 ≥ -1/2 > 0 ≥ -1-x_1 when x_1 ≥ -1. Actually -1 - x_1 ∈ [-0, 0] when x_1 ∈ [-1, 0]. And x_2 ≥ -1/2. Is -1/2 ≥ -1 - x_1? -1/2 ≥ -1 - x_1 ⟺ x_1 ≥ -1/2. But x_1 < -1/2! So -1 - x_1 > -1/2, meaning we need x_2 > -1/2, which is true if x_2 > -1/2. But x_2 might equal -1/2.

Hmm, need x_2 - d ≥ -1, i.e., x_2 ≥ -1 + d = -1 + (-1/2 - x_1) = -3/2 - x_1. Since x_1 ≥ -1, -3/2 - x_1 ≤ -1/2. And x_2 ≥ -1 ≥ -3/2 - x_1 (since -3/2 - x_1 ≤ -1/2 < -1... wait -3/2 - x_1 when x_1 = -1 is -3/2 + 1 = -1/2; when x_1 = -1/2 it's -3/2 + 1/2 = -1). So -3/2 - x_1 ∈ [-1, -1/2] for x_1 ∈ [-1, -1/2]. And x_2 ≥ -1. So x_2 ≥ -1 ≥ -3/2 - x_1? Need -1 ≥ -3/2 - x_1 ⟺ x_1 ≥ -1/2. Not always true. When x_1 < -1/2, -3/2 - x_1 > -1, so we need x_2 > -1. 

OK this is getting complicated. Let me just require x_2 > -1 (strictly interior from below) or handle boundary cases separately.

Assume x_2 > -1 (and x_2 > -1/2 since all others ≥ -1/2 or we pick one that is). Actually, if x_1 is the only variable < -1/2, then x_2, ..., x_10 ≥ -1/2 > -1, so x_2 > -1. Good.

If multiple variables < -1/2, pick x_1 < -1/2 and x_2 ≥ -1/2 (there must be some since sum = 10 > 10*(-1/2) = -5, so not all < -1/2). Then x_2 ≥ -1/2 > -1.

OK so assume x_2 ≥ -1/2 and x_2 - d ≥ -1 where d = -1/2 - x_1 ∈ (0, 1/2]. Since x_2 ≥ -1/2 and d ≤ 1/2, x_2 - d ≥ -1. ✓ (And if x_2 - d < -1/2, that's OK, we just might need to iterate.)

Change in cubes: Δ = [(-1/2)^3 - x_1^3] + [(x_2 - d)^3 - x_2^3].

= [-1/8 - x_1^3] + [(x_2 - d)^3 - x_2^3].

Let me use the identity: (x_2 - d)^3 - x_2^3 = -3x_2^2 d + 3x_2 d^2 - d^3 = -d(3x_2^2 - 3x_2 d + d^2).

And -1/8 - x_1^3 = -(x_1^3 + 1/8) = -(x_1 + 1/2)(x_1^2 - x_1/2 + 1/4). Since x_1 < -1/2, x_1 + 1/2 < 0, so -(x_1+1/2) > 0, and x_1^2 - x_1/2 + 1/4 > 0 (discriminant 1/4 - 1 < 0). So -1/8 - x_1^3 > 0. Good, first term positive.

Δ = -(x_1 + 1/2)(x_1^2 - x_1/2 + 1/4) - d(3x_2^2 - 3x_2 d + d^2) where d = -1/2 - x_1 = -(x_1 + 1/2).

So Δ = d(x_1^2 - x_1/2 + 1/4) - d(3x_2^2 - 3x_2 d + d^2) = d[(x_1^2 - x_1/2 + 1/4) - (3x_2^2 - 3x_2 d + d^2)].

Need Δ ≥ 0, i.e., x_1^2 - x_1/2 + 1/4 ≥ 3x_2^2 - 3x_2 d + d^2.

This is not always true. For example, if x_2 = 2, RHS = 12 - 6d + d^2, LHS = x_1^2 - x_1/2 + 1/4 ≤ 1 + 1/2 + 1/4 = 1.75 (for x_1 = -1). So Δ < 0. Moving mass from x_2=2 to x_1 decreases objective.

This makes sense: if x_2 = 2 (at max), we don't want to decrease it. We'd want to decrease a variable that's not at 2.

So the smoothing argument needs to choose x_2 carefully. We should decrease a variable that's "less valuable" - i.e., not at 2.

This is getting quite involved. Let me try a completely different, cleaner proof strategy.

Proof via Lagrange multipliers / KKT, showing the unique KKT point with all conditions satisfied and highest objective is our candidate.

Actually, let me try to use a cleaner inequality. 

Key inequality: For x ∈ [-1, 2], 
x^3 ≤ (13/4)x + 3/2 + (3/4)(x + 1/2)(1 - (x+1/2)/(5/2))... no, too ad hoc.

Let me try: find the best quadratic upper bound ax^2 + bx + c ≥ x^3 on [-1, 2] such that 10a·(avg of x^2)... no, we don't know Σx^2.

Hmm. Let me try using both Σx_i = 10 and the constraint x_i ≤ 2 more cleverly.

Note that (2 - x_i) ≥ 0 for all i. And Σx_i = 10, so Σ(2 - x_i) = 20 - 10 = 10.

Also (x_i + 1) ≥ 0. Σ(x_i + 1) = 20.

Let me write x_i^3 in terms of (x_i - 2) and (x_i + 1/2) and (x_i + 3/2) as before: x_i^3 = (13/4)x_i + 3/2 + (x_i - 2)(x_i + 1/2)(x_i + 3/2).

Σx_i^3 = 95/2 + Σ(x_i - 2)(x_i + 1/2)(x_i + 3/2).

Let u_i = x_i + 1/2 ∈ [-1/2, 5/2]. Then x_i - 2 = u_i - 5/2, x_i + 3/2 = u_i + 1. Σu_i = 15.

Σx_i^3 = 95/2 + Σ(u_i - 5/2)(u_i)(u_i + 1) = 95/2 + Σ u_i(u_i+1)(u_i - 5/2).

Need to show Σ u_i(u_i+1)(u_i - 5/2) ≤ 0, where u_i ∈ [-1/2, 5/2], Σu_i = 15.

Let f(u) = u(u+1)(u - 5/2) = u^3 - (3/2)u^2 - (5/2)u.

Σf(u_i) = Σu_i^3 - (3/2)Σu_i^2 - (5/2)Σu_i = Σu_i^3 - (3/2)Σu_i^2 - 75/2.

Need Σu_i^3 - (3/2)Σu_i^2 ≤ 75/2.

Hmm, still involves Σu^2 and Σu^3.

Let me try yet another angle. Let me use the constraint x_i ≤ 2 directly.

Since x_i ≤ 2, we have x_i^3 ≤ 2x_i^2 (because x_i^3 = x_i · x_i^2 ≤ 2x_i^2 when x_i ≤ 2; but this fails when x_i < 0 since x_i^3 < 0 < 2x_i^2, actually it holds: if x_i ≥ 0, x_i^3 ≤ 2x_i^2; if x_i < 0, x_i^3 < 0 ≤ 2x_i^2). So x_i^3 ≤ 2x_i^2 for all x_i ∈ [-1, 2]. ✓

So Σx_i^3 ≤ 2Σx_i^2. But we showed Σx_i^2 can be up to 28, giving 56. Not helpful.

Also x_i^3 ≤ 4x_i (for x_i ∈ [0,2], x_i^2 ≤ 4 so x_i^3 ≤ 4x_i; for x_i < 0, x_i^3 < 0 ≤ 4x_i... no, 4x_i < 0 when x_i < 0, and x_i^3 < 4x_i iff x_i^2 > 4 iff |x_i| > 2, not the case). So for x_i ∈ [-1, 0): x_i^3 vs 4x_i: x_i^3 - 4x_i = x_i(x_i^2 - 4). x_i < 0, x_i^2 < 1 < 4, so x_i^2 - 4 < 0, product > 0. So x_i^3 > 4x_i for x_i ∈ [-1, 0). So x_i^3 ≤ 4x_i fails for negative x_i.

Let me try to combine inequalities. For x ∈ [-1, 2]:
- x^3 ≤ 4x for x ∈ [0, 2] (since x^2 ≤ 4)
- x^3 ≤ ? for x ∈ [-1, 0]

For x ∈ [-1, 0]: x^3 = x · x^2, and x^2 ≤ 1, x ≤ 0, so x^3 ≥ x · 1 = x (more negative). Actually x^3 ≥ -1 and x ≥ -1. x^3 - x = x(x^2-1) = x(x-1)(x+1). For x ∈ [-1,0]: x < 0, x-1 < 0, x+1 ≥ 0, so x(x-1)(x+1) ≥ 0, i.e., x^3 ≥ x. So x^3 ≥ x on [-1, 0]. That's a lower bound, not upper.

For upper bound on [-1,0]: x^3 ≤ 0 (since x ≤ 0). And x^3 = x·x^2 ≤ 0. Also x^3 ≤ x^2 (since x ≤ 1, x^3 ≤ x^2 when x ≤ 1 and x ≥ 0... no). For x ∈ [-1, 0]: x^3 ≤ 0 and we want an upper bound involving x. x^3 ≤ 0 = 0·x + 0. Or x^3 ≤ -x (since x^3 + x = x(x^2+1) ≤ 0 for x ≤ 0, so x^3 ≤ -x). So x^3 ≤ -x on [-1, 0]. And -x ∈ [0, 1].

Hmm, let me try: for x ∈ [-1, 0], x^3 ≤ -x. For x ∈ [0, 2], x^3 ≤ 4x. 

Σx_i^3 ≤ Σ_{x_i<0} (-x_i) + Σ_{x_i≥0} 4x_i. Let P = {i: x_i ≥ 0}, N = {i: x_i < 0}. = -Σ_N x_i + 4Σ_P x_i = 4Σ_P x_i - Σ_N x_i = 4Σ_P x_i + (Σx_i - Σ_P x_i)·(-1)... wait. Σ_N x_i = 10 - Σ_P x_i. So -Σ_N x_i = Σ_P x_i - 10. Thus Σx_i^3 ≤ 4Σ_P x_i + Σ_P x_i - 10 = 5Σ_P x_i - 10.

Σ_P x_i ≤ 2|P|. To maximize 5Σ_P x_i - 10, maximize Σ_P x_i. But Σ_P x_i = 10 - Σ_N x_i, and Σ_N x_i ≥ -|N| = -(10-|P|). So Σ_P x_i ≤ 10 + (10 - |P|) = 20 - |P|. Also Σ_P x_i ≤ 2|P|. So Σ_P x_i ≤ min(2|P|, 20 - |P|).

Max of min(2|P|, 20-|P|) over |P|: 2|P| = 20 - |P| → 3|P| = 20 → |P| = 20/3 ≈ 6.67. At |P|=6: min(12, 14) = 12. At |P|=7: min(14, 13) = 13. So max at |P|=7: 13.

Then Σx_i^3 ≤ 5*13 - 10 = 55. Not tight.

This approach is too loose. Let me go back to the KKT/case analysis approach and present it cleanly.

Actually, let me try the following clean approach using the structure of the problem.

Step 1: Show that at the maximum, at most one variable is in the interior (-1, 2) \ {-1/2}, and if so, it must be -1/2.

Hmm, that's not quite right either. At our solution, 4 variables are at -1/2 (interior).

Let me think about it via the "convex envelope" or "upper concave envelope" of x^3 on [-1, 2].

The upper concave envelope of x^3 on [-1, 2]: Since we're maximizing a sum with a sum constraint, the maximum is related to the concave envelope. Specifically, by the theory of moments / linear programming relaxation, the maximum of Σf(x_i) subject to Σx_i = S and x_i ∈ [a,b] is related to the concave envelope of f.

The concave envelope of f(x) = x^3 on [-1, 2]: 

f is concave on [-1, 0] and convex on [0, 2]. The concave envelope on [0, 2] is the secant line from (0, 0) to (2, 8): y = 4x. On [-1, 0], f is already concave, so the envelope is f itself. But we need the envelope to be concave on all of [-1, 2], so we need to connect them.

The concave envelope: on [-1, 0], it's x^3 (concave). On [0, 2], it's the line 4x. But at x=0, x^3 = 0 and 4x = 0, continuous. Is the combined function concave? At x=0, left derivative of x^3 is 0, right derivative of 4x is 4. For concavity, we need left derivative ≥ right derivative, but 0 < 4. So NOT concave. 

So the concave envelope needs adjustment. The concave envelope is the smallest concave function ≥ x^3 on [-1, 2].

Let me find it. The concave envelope will be x^3 on some interval [-1, c] and a line on [c, 2], where the line is tangent to x^3 at c and passes through (2, 8).

Line through (c, c^3) and (2, 8) with slope matching 3c^2 at c: slope = 3c^2 = (8 - c^3)/(2 - c). So 3c^2(2-c) = 8 - c^3 → 6c^2 - 3c^3 = 8 - c^3 → 6c^2 - 2c^3 = 8 → 2c^3 - 6c^2 + 8 = 0 → c^3 - 3c^2 + 4 = 0 → (c-2)(c^2 - c - 2) = (c-2)(c-2)(c+1) = (c-2)^2(c+1) = 0. So c = 2 or c = -1. 

That gives the line through (2, 8) tangent at x=2, which is y = 12x - 16 (slope 12). At x=-1: 12(-1)-16 = -28 < -1 = (-1)^3. So this line is below x^3 at x=-1, not an upper bound. 

Hmm, so the tangent from (2,8) to the curve only touches at 2 (double root) and -1. The line through (2,8) and (-1,-1) is y = 3x + 2, slope 3. At x=-1, slope of x^3 is 3(-1)^2 = 3. So the line y = 3x+2 is tangent to x^3 at x = -1! And passes through (2, 8). 

So the concave envelope is: the line 3x + 2 on [-1, 2]? But we need to check it's ≥ x^3. We showed (x-2)(x+1)^2 ≤ 0 on [-1, 2], so x^3 ≤ 3x + 2. ✓ And the line is tangent at x=-1 and passes through (2,8). 

But is 3x+2 concave (yes, linear) and ≥ x^3? Yes. Is it the smallest concave majorant? At x=-1, both equal -1 and same slope, so it's tight there. At x=2, both equal 8. In between, 3x+2 > x^3 (strictly for x ∈ (-1, 2)). 

So the concave envelope of x^3 on [-1, 2] is 3x + 2. Then by Jensen's inequality for the concave envelope:

Σx_i^3 ≤ Σ(3x_i + 2) = 3·10 + 20 = 50.

But this gives 50, not 47.5. The issue is that the concave envelope gives the LP relaxation bound, which is 50, but it's not achievable because achieving equality requires all x_i at the contact points {-1, 2}, and no feasible solution has all x_i ∈ {-1, 2} with sum 10.

So the concave envelope approach gives 50, which is the LP bound but not tight due to integrality-like constraints (we need exactly 10 variables).

This means the problem is more subtle. The maximum 47.5 is less than the concave envelope bound 50 because we can't achieve the envelope's equality conditions.

So I need a proof that accounts for the discrete nature (10 variables). 

Let me think about this more carefully using the "moment" approach. We have 10 variables. Think of it as a distribution: let the empirical distribution be μ = (1/10)Σδ_{x_i}. Then Σx_i = 10 → E_μ[x] = 1. Σx_i^3 = 10·E_μ[x^3]. We want to maximize E[x^3] subject to E[x] = 1 and support in [-1, 2], with the constraint that μ is a uniform distribution on 10 points (i.e., each point has mass 1/10).

Without the "10 points" constraint, the max of E[x^3] with E[x]=1, support [-1,2] is given by the concave envelope: E[x^3] ≤ E[3x+2] = 3+2 = 5, so Σx_i^3 ≤ 50. Achieved by a distribution on {-1, 2} with E[x]=1: P(x=2) = p, P(x=-1) = 1-p, 2p - (1-p) = 1 → 3p = 2 → p = 2/3. So 2/3 of mass at 2, 1/3 at -1. With 10 variables, that's 20/3 at 2 and 10/3 at -1, not integer.

So the problem reduces to: we need 10 points (with repetition) in [-1, 2] summing to 10, maximizing Σx_i^3. The continuous relaxation gives 50 but requires non-integer counts at {-1, 2}.

Now, the key insight: since we can't have all points at {-1, 2}, some points must be in the interior, where x^3 < 3x + 2 strictly. The "loss" from the envelope is Σ(3x_i + 2 - x_i^3) = 50 - Σx_i^3 = Σ[-(x_i-2)(x_i+1)^2] = Σ(2-x_i)(x_i+1)^2.

So Σx_i^3 = 50 - Σ(2-x_i)(x_i+1)^2. We want to minimize Σ(2-x_i)(x_i+1)^2 subject to Σx_i = 10, x_i ∈ [-1, 2].

Let φ(x) = (2-x)(x+1)^2 ≥ 0 on [-1, 2]. We want to minimize Σφ(x_i) with Σx_i = 10.

At x = 2: φ = 0. At x = -1: φ = 0. At x = -1/2: φ = (5/2)(1/2)^2 = 5/8. At x = 0: φ = 2. At x = 1: φ = 1·4 = 4.

So φ is 0 at the endpoints, positive in between. To minimize Σφ, we want variables at endpoints (2 or -1). But we can't have all at endpoints with sum 10 (as shown).

So we need some variables in the interior, and we want to minimize the total φ. 

If we have a at 2, b at -1, and the rest in interior: 2a - b + (interior sum) = 10. To minimize Σφ, we want as many at endpoints as possible and the interior ones to have small φ.

φ(x) = (2-x)(x+1)^2. φ'(x) = -(x+1)^2 + 2(2-x)(x+1) = (x+1)[-(x+1) + 2(2-x)] = (x+1)[-x-1+4-2x] = (x+1)(3-3x) = 3(x+1)(1-x). Zero at x=-1, x=1. φ''(x) = 3[(1-x) - (x+1)] = 3(1-x-x-1) = -6x. At x=1: φ''=-6 < 0, local max. At x=-1: φ''=6 > 0, local min (φ=0).

So φ increases from 0 at x=-1 to max at x=1 (φ(1)=4), then decreases to 0 at x=2. 

To minimize Σφ with fixed Σx_i = 10: we want variables where φ is small, i.e., near -1 or near 2. 

If we must have interior variables, they should be near -1 or near 2 (where φ is small). But near -1, x ≈ -1 contributes ≈ -1 to sum; near 2, x ≈ 2 contributes ≈ 2.

Let me think about it as: suppose we have a variables at 2, b at -1, and c = 10 - a - b interior variables. Sum: 2a - b + S_int = 10, where S_int is the sum of interior variables. φ contribution: 0 + 0 + Σφ(interior) = Σφ(interior). We want to minimize Σφ(interior) subject to Σ(interior) = 10 - 2a + b, and interior vars in (-1, 2).

To minimize Σφ with fixed sum, by convexity/concavity analysis... φ is convex        — AI历史解题过程（thinking）
#   polymath_01000         — 题目ID

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
  <problem_id>polymath_01000</problem_id>
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

Find the maximum of \( x_{1}^{3} + \ldots + x_{10}^{3} \) for \( x_{1}, \ldots, x_{10} \in [-1, 2] \) such that \( x_{1} + \ldots + x_{10} = 10 \).

## Standard Solution

To find the maximum value of \( x_1^3 + x_2^3 + \ldots + x_{10}^3 \) for \( x_1, x_2, \ldots, x_{10} \in [-1, 2] \) such that \( x_1 + x_2 + \ldots + x_{10} = 10 \), we need to carefully consider the constraints and the behavior of the cube function.

1. **Maximizing the Cube Function**:
   - The cube function \( x^3 \) is increasing, so to maximize the sum of cubes, we should set as many variables as possible to the maximum value of 2.
   - If all 10 variables were set to 2, the total sum would be \( 2 \times 10 = 20 \), which exceeds 10. Therefore, we need to reduce the total sum by 10 while maximizing the cube sum.

2. **Optimal Configuration**:
   - Let \( m \) variables be set to 2. The remaining \( 10 - m \) variables must sum to \( 10 - 2m \).
   - To maximize the cube sum, we should minimize the loss in the cube sum when reducing the variables. 

3. **Calculations for \( m = 6 \)**:
   - If \( m = 6 \), then 6 variables are set to 2. The remaining 4 variables must sum to \( 10 - 2 \times 6 = -2 \).
   - To minimize the loss in the cube sum, we set each of the remaining 4 variables to \(-0.5\), which is the highest possible value to minimize the cube loss.
   - Each \(-0.5\) contributes \((-0.5)^3 = -0.125\).
   - Total cube contribution from the remaining variables: \( 4 \times (-0.125) = -0.5 \).
   - Total cube sum: \( 6 \times 8 + (-0.5) = 48 - 0.5 = 47.5 \).

4. **Verification**:
   - Other configurations, such as mixing \(-1\) and 0, or different distributions, were considered but resulted in lower cube sums.
   - Using Lagrangian multipliers and KKT conditions confirmed that the maximum is achieved with the configuration described.

Thus, the maximum value of the sum of cubes is \(\boxed{\dfrac{95}{2}}\).

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We need to find the maximum of x_1^3 + ... + x_10^3 where each x_i ∈ [-1, 2] and x_1 + ... + x_10 = 10.

First, let me check for answer leaks. The problem just states the problem, no solution given. Good.

Let me think. The sum is 10, with 10 variables each in [-1,2]. The average is 1. If all were 1, sum of cubes = 10. But we want to maximize sum of cubes.

Cubic function is convex on positive values and concave on negative. Actually x^3 has second derivative 6x, so convex for x>0, concave for x<0.

To maximize sum of cubes with fixed sum, we want to push values to extremes. Since x^3 is convex for x>0, by Jensen we want positive values at extremes (either 2 or close to 0). For negative values, concave so we want them equal.

Strategy: push some variables to 2 (max), and the rest adjust to meet the sum constraint. Let's say k variables are at 2. Then remaining 10-k variables sum to 10-2k. Each remaining in [-1,2].

For remaining variables with sum S = 10-2k, we want to maximize sum of cubes. The remaining variables: if S is positive, push to 2 as much as possible. Actually let's think about what's optimal.

Let me consider: we want to maximize. x^3 is increasing, so larger x gives larger cube. But with fixed sum, we need balance.

Consider the function. Let's think about pushing to boundary. The feasible region is a polytope (intersection of hypercube with hyperplane). The maximum of a convex-ish function... Actually sum of cubes is not convex overall.

Let me think about KKT/edge analysis. At optimum, variables are at boundary (2 or -1) except possibly some "free" ones.

Let me guess: take as many 2's as possible. If all 10 are 2, sum = 20, too much. We need sum 10.

Let's say we have k variables at 2, m variables at -1, and the rest free. Sum: 2k - m + (free sum) = 10. We want to maximize 8k - m + (free cubes).

Actually, let me think more carefully. Let's try to have variables either at 2 or at some value to balance.

Suppose we have k variables at 2, contributing 8k to cubes and 2k to sum. Remaining 10-k variables sum to 10-2k, each in [-1,2].

For the remaining, to maximize sum of cubes given fixed sum. If 10-2k ≤ 0, i.e., k ≥ 5, the remaining sum is non-positive. 

Let's think: we want remaining sum to be achieved with max cubes. For remaining variables with sum S (where S = 10-2k), if S is small/negative, we'd want to push some to -1 and others to 2? No wait, we want to maximize cubes.

Hmm, let me think about small cases. Actually, let me reconsider. The cube function: for maximizing sum with fixed total, since cube is convex for positive x, we want positive contributions concentrated. For negative x (concave), we want them spread equally.

Let me consider: put some at 2, and the rest at a common value. If k at 2, and (10-k) at value v, then 2k + (10-k)v = 10, so v = (10-2k)/(10-k). Need v ∈ [-1, 2].

Sum of cubes = 8k + (10-k)v^3.

Let me compute for various k:
- k=0: v=1, sum=10.
- k=1: v=8/9≈0.889, sum=8+9*(0.889)^3=8+9*0.702=8+6.32=14.32
- k=2: v=6/8=0.75, sum=16+8*(0.75)^3=16+8*0.4219=16+3.375=19.375
- k=3: v=4/7≈0.571, sum=24+7*(0.571)^3=24+7*0.1866=24+1.306=25.306
- k=4: v=2/6=1/3, sum=32+6*(1/3)^3=32+6/27=32+0.222=32.222
- k=5: v=0/5=0, sum=40+0=40
- k=6: v=-2/4=-0.5, sum=48+4*(-0.125)=48-0.5=47.5
- k=7: v=-4/3≈-1.333, but this is < -1, infeasible!

So k=6 gives v=-0.5 which is feasible. sum=47.5.

But wait, can we do better by not having all remaining equal? For k=6, remaining 4 variables sum to -2. To maximize sum of cubes with 4 variables in [-1,2] summing to -2. Since for negative region cube is concave, equal is optimal among negatives? Actually we want to maximize. With sum -2 over 4 vars, if all equal -0.5, cubes sum = 4*(-0.125)=-0.5. 

Alternatively, could push some to 2 and others to -1. E.g., one at 2, then remaining 3 sum to -4, each ≥-1, so min sum is -3. -4 < -3, infeasible. So can't have any at 2 among remaining when k=6.

What about mixing -1 and something? With 4 vars summing to -2: if one at -1, remaining 3 sum to -1, equal at -1/3, cubes = -1 + 3*(-1/27) = -1 - 1/9 = -1.111. Worse than -0.5.

If two at -1, remaining 2 sum to 0, equal at 0, cubes = -2 + 0 = -2. Worse.

So equal is best for k=6. Sum = 47.5.

Let me check k=5 more carefully. Remaining 5 vars sum to 0. Equal at 0 gives 0. But can we do better? Push some to 2 and others to -1. If one at 2, remaining 4 sum to -2, each ≥-1, min -4 ≥ -2 ok. To maximize, remaining 4 summing to -2: equal at -0.5 gives -0.5. Total = 8 - 0.5 = 7.5 for these 5. Plus 5*8=40 from the 2's. Total = 47.5. Same!

Hmm interesting. Let me check: k=5 with one of remaining at 2 and four at -0.5: that's actually 6 at 2 and 4 at -0.5, same as k=6 case.

What about k=5, two at 2? Then it's 7 at 2, remaining 3 sum to 10-14=-4, min -3, infeasible.

So the boundary cases converge. Let me check if we can beat 47.5.

What about k=6 but with some at -1? 6 at 2 (sum 12, cubes 48), remaining 4 sum to -2. If we use -1's: to sum -2 with 4 vars in [-1,2], and we want to maximize cubes. The minimum each can be is -1. If two at -1 (sum -2) and two at 0: cubes = -2. Total = 46. Worse than 47.5.

If one at -1, three summing to -1: equal -1/3, cubes = -1 + 3*(-1/27)=-1.111, total 46.889. Worse.

So 47.5 with 6 at 2 and 4 at -0.5 seems good. But is it the global max?

Let me reconsider. Maybe non-symmetric is better. Let me think about the general structure.

Actually, let me reconsider whether having some at -1 and more at 2 could help. The issue is sum constraint. With 7 at 2, sum=14, remaining 3 need sum -4, but min is -3. Infeasible. So max 6 at 2.

With 6 at 2, remaining 4 sum to -2. We showed equal -0.5 is optimal for these (maximizing sum of cubes). 

But wait, is equal really optimal? Let me verify. We have 4 variables in [-1,2] summing to -2, maximize sum of cubes. 

The cube function on [-1, 2]: f''(x)=6x. For x<0 concave, x>0 convex. 

Lagrangian: at interior optimum, 3x_i^2 = λ for all free i, so all free x_i equal in absolute value. 

Consider candidates: variables at boundary 2 or -1, or interior with |x| equal.

If some interior positive x=p>0 and some interior negative x=-p (same |value|): but 3p^2 = λ means same λ. Let a be count at +p, b at -p, c at 2, d at -1. Sum: ap - bp + 2c - d = -2. Cubes: a p^3 - b p^3 + 8c - d = maximize.

This is getting complex. Let me just check: is 47.5 the answer, or can we do better?

Let me try: 6 at 2, and 4 variables. What if 3 at -1 and 1 at 1? Sum: 12 - 3 + 1 = 10. ✓. Cubes: 48 - 3 + 1 = 46. Worse.

What about 6 at 2, 1 at -1, 3 at -1/3? Sum 12-1-1=10. Cubes 48-1-3/27=48-1-0.111=46.889. Worse.

6 at 2, 4 at -0.5: sum 12-2=10, cubes 48-0.5=47.5. 

What about 5 at 2, and 5 variables summing to 0? We found 5 at 0 gives 40, or 1 at 2 + 4 at -0.5 gives 47.5 (same as 6+4). What about 5 at 2, 1 at 1, 4 at -0.75? Sum 10+1-3=8? No: 5*2=10, +1=11, +4*(-0.75)=-3, total 8. Not 10. 

5 at 2 (sum 10), remaining 5 sum to 0. To maximize cubes of 5 vars summing to 0 in [-1,2]. Equal at 0: cubes 0. Mixed: 1 at 2, 4 at -0.5: sum 2-2=0, cubes 8-0.5=7.5. So total 40+7.5=47.5. Or 2 at 2, 3 at -4/3: infeasible (<-1). Or 1 at 2, 1 at -1, 3 at -1/3: sum 2-1-1=0, cubes 8-1-1/9=6.889. Worse. Or 1 at 2, 3 at -1, 1 at 1: sum 2-3+1=0, cubes 8-3+1=6. Worse.

So 47.5 keeps appearing. Let me check if anything beats it.

What about not using 2's fully? Like 6 at 2 is max possible 2's. What about 6 at 2, 4 at -0.5 = 47.5.

Could a completely different config beat it? Let me think about upper bound. 

Actually, let me try 6 at 2, and among 4 remaining, push to extremes differently. We need 4 vars in [-1,2] sum -2, maximize cubes. 

Let me parametrize: let t variables at 2, s at -1, rest equal at v. With 4 vars: 
- t=0,s=0: v=-0.5, cubes=-0.5
- t=1: remaining 3 sum -4, min -3, infeasible
- t=0,s=1: remaining 3 sum -1, v=-1/3, cubes=-1-1/9=-1.111
- t=0,s=2: remaining 2 sum 0, v=0, cubes=-2
- t=0,s=3: remaining 1 sum 1, v=1, cubes=-3+1=-2
- t=0,s=4: sum -4≠-2 infeasible

So best is t=0,s=0: -0.5. Total 47.5.

Now let me also check: maybe fewer than 6 at 2 but with creative arrangement beats 47.5.

Let me try 4 at 2, 6 variables summing to 2. Maximize cubes. 6 vars in [-1,2] sum 2. 
- All equal: 1/3, cubes 6*(1/27)=0.222. Total 32.222.
- 1 at 2, 5 at 0: sum 2, cubes 8. Total 40.
- 1 at 2, 1 at -1, 4 at 0.25: sum 2-1+1=2, cubes 8-1+4*0.0156=7.06. Total 39.06.
- 1 at 2, 4 at -1, 1 at 2: that's 2 at 2, 4 at -1, sum 4-4=0≠2.
- 2 at 2, 4 at -0.5: sum 4-2=2, cubes 16-0.5=15.5. Total 32+15.5=47.5! Same again.

Interesting, 47.5 again. So 4 at 2 + 2 at 2 + 4 at -0.5 = 6 at 2 + 4 at -0.5.

- 2 at 2, 3 at -1, 1 at 1: sum 4-3+1=2, cubes 16-3+1=14. Total 46. Worse.
- 3 at 2, 3 at -4/3: infeasible.
- 2 at 2, 1 at -1, 3 at -1/3: sum 4-1-1=2, cubes 16-1-1/9=14.889. Total 46.889.

So 47.5 is the pattern. Let me check 3 at 2, 7 vars sum 4.
- 3 at 2, 3 at 2, ... = 6 at 2, 4 at -0.5 → 47.5.
- 3 at 2, 1 at 2, 6 at 1/3: sum 6+2+2=10, cubes 24+8+6/27=32.222. Worse.

It really seems 47.5 is the max. Let me try to prove it rigorously and also double check there's nothing higher with a weird config.

Let me try: 6 at 2, 4 at -0.5. Sum = 12 - 2 = 10. ✓ Cubes = 48 - 0.5 = 47.5.

Can we get higher? Let me try 6 at 2, 3 at -1, 1 at 1: sum 12-3+1=10, cubes 48-3+1=46. No.

6 at 2, 2 at -1, 2 at 0: sum 12-2=10, cubes 48-2=46. No.

What about 6 at 2, 1 at 2... no that's 7.

Let me try asymmetric: 6 at 2, 1 at -1, 1 at 0, 2 at -0.5: sum 12-1+0-1=10, cubes 48-1+0-0.25=46.75. No.

What about 5 at 2, 1 at 2, ... same.

Let me try: 6 at 2, 4 at -0.5 = 47.5. 

What about 6 at 2, and 4 vars not all -0.5 but optimizing? We proved -0.5 equal is optimal for that subproblem.

Now, is 6 at 2 optimal number of 2's? More than 6 infeasible. With 6 at 2 we get 47.5. With 5 at 2, best remaining gives 47.5 (which reduces to 6+4). With 4 at 2, best gives 47.5. So the max is achieved at 47.5 and these are all the same point essentially (6 at 2, 4 at -0.5).

Wait, but are there configs with fewer 2's that beat 47.5? Let me check 0 at 2: all in [-1,2] sum 10. Max cubes? 10 vars sum 10 avg 1. To maximize, push to 2 and -1. If a at 2, b at -1, rest equal. a*2 - b + (10-a-b)*v = 10. To maximize cubes 8a - b + (10-a-b)v^3. We saw a=6,b=0,v=-0.5 gives 47.5. 

Let me verify there's no config beating 47.5 by considering the Lagrangian more carefully, or just trust the pattern.

Actually, let me try a potentially tricky one: 6 at 2, 1 at 2 is 7, infeasible. What about 6 at 2, and 4 vars where some are at 2? No, that makes 7+ at 2.

Let me try 6 at 2, 4 at -0.5. Could we do 6 at 2, 2 at -1, 1 at 2... no.

Hmm what about configs with values at 2 and -1 only? a at 2, b at -1, a+b=10, 2a-b=10 → 2a-(10-a)=10 → 3a=20 → a=20/3 not integer. So no pure {-1,2} solution. Need fractional.

Let me also check: 6 at 2, 4 at -0.5: 47.5. What about 6 at 2, 3 at -2/3, 1 at 0: sum 12 - 2 + 0 = 10, cubes 48 + 3*(-8/27) = 48 - 8/9 = 47.111. Worse.

What about 6 at 2, 2 at -1, 2 at 0: 48 - 2 = 46. Worse.

I'm fairly confident the answer is 47.5 = 95/2.

Let me now also verify by trying to see if we can exceed. Consider general: let a variables at 2, and the rest (10-a) at value v = (10-2a)/(10-a). Feasible when v ∈ [-1, 2].

v ≥ -1: (10-2a)/(10-a) ≥ -1 → 10-2a ≥ -(10-a) = -10+a → 10-2a ≥ -10+a → 20 ≥ 3a → a ≤ 20/3 ≈ 6.67. So a ≤ 6.
v ≤ 2: (10-2a)/(10-a) ≤ 2 → 10-2a ≤ 20-2a → 10 ≤ 20. Always true.

So a ∈ {0,...,6}. We computed:
- a=6: v=-0.5, cubes=48+4*(-0.125)=48-0.5=47.5
- a=5: v=0, cubes=40
- a=4: v=1/3, cubes=32+6/27=32.222
- a=3: v=4/7, cubes=24+7*(4/7)^3=24+7*64/343=24+448/343=24+1.306=25.306
- a=2: v=0.75, cubes=16+8*0.4219=19.375
- a=1: v=8/9, cubes=8+9*0.702=14.32
- a=0: v=1, cubes=10

Max among these "one-value" solutions: a=6, 47.5.

But the true max might use multiple distinct values. However, we showed that for the subproblem with a=6 (4 vars sum -2), equal is optimal. And for a<6, the optimal further splits also lead back to the a=6 config (e.g., a=5 then split one to 2 and rest to -0.5 gives a=6 config).

But could a non-boundary, multi-value solution beat 47.5? Let me think about KKT.

At a maximum of a continuous function on a compact set, KKT conditions. The objective f = Σx_i^3, constraint g = Σx_i - 10 = 0, box constraints -1 ≤ x_i ≤ 2.

Lagrangian: L = Σx_i^3 - λ(Σx_i - 10) + Σμ_i(x_i - 2) - Σν_i(x_i + 1).

KKT: 3x_i^2 - λ + μ_i - ν_i = 0, with μ_i ≥ 0 (active when x_i=2), ν_i ≥ 0 (active when x_i=-1), μ_i(x_i-2)=0, ν_i(x_i+1)=0.

For interior x_i (not at boundary): μ_i=ν_i=0, so 3x_i^2 = λ, meaning x_i = ±√(λ/3). So interior variables take at most two values: +p or -p where p=√(λ/3).

At our candidate: 6 at 2 (boundary, μ>0), 4 at -0.5 (interior, so 3*(0.25)=0.75=λ, p=0.5). Check boundary condition for x_i=2: 3*4 - λ + μ_i = 0 → 12 - 0.75 + μ_i = 0 → μ_i = -11.25 < 0. 

That's a problem! μ_i should be ≥ 0. This means the KKT condition fails at x_i=2 — the objective wants to increase x_i beyond 2 but can't, which is fine for a max (μ_i < 0 would mean... wait let me recheck sign convention).

Hmm, let me redo. For maximization with constraint x_i ≤ 2: we add term -μ_i(x_i - 2) with μ_i ≥ 0 (penalizing x_i > 2). Then dL/dx_i = 3x_i^2 - λ - μ_i + ν_i = 0 (with ν_i for x_i ≥ -1, term +ν_i(x_i+1), ν_i≥0).

At x_i = 2: 3*4 - λ - μ_i = 0 → 12 - 0.75 - μ_i = 0 → μ_i = 11.25 ≥ 0. ✓ Good.

At x_i = -0.5 (interior): 3*0.25 - λ = 0 → λ = 0.75. ✓

At x_i = -0.5, check ν_i = 0 (not at -1 boundary). ✓

So KKT satisfied with λ=0.75, μ_i=11.25 for the six 2's, ν_i=0. All conditions met. This is a KKT point.

Is it the global max? The feasible set is compact, objective continuous, so global max exists. KKT points are candidates. We need to check this is the global max among all KKT points.

Other KKT points: various combinations. But given the pattern that all "improvement" directions lead to this same point and all other candidates give lower values, I'm confident.

Actually, let me also check a KKT point with some at -1. Suppose b at -1, a at 2, rest interior at ±p. 

At x_i=-1: 3*1 - λ + ν_i = 0 → 3 - λ + ν_i = 0 → ν_i = λ - 3. Need ν_i ≥ 0 → λ ≥ 3. Then p = √(λ/3) ≥ 1. Interior values ±p with p≥1, but interior must be in (-1,2), so p ∈ [1,2) for +p, and -p ≤ -1 not interior (would be at boundary). So if λ ≥ 3, interior positive value p ∈ [1,2). 

Let me try: b at -1, some at +p (interior, p∈[1,2)), some at 2. Let a at 2, c at p, b at -1. a+b+c=10. Sum: 2a + cp - b = 10. Cubes: 8a + cp^3 - b. λ=3p^2, and at x=2: μ = 12 - 3p^2 ≥ 0 → p^2 ≤ 4 → p ≤ 2 ✓. At x=-1: ν = 3p^2 - 3 ≥ 0 → p ≥ 1 ✓.

So p ∈ [1, 2]. Let me explore. We want to maximize 8a + cp^3 - b with 2a + cp - b = 10, a+b+c=10, a,b,c ≥ 0 integers.

From sum: b = 2a + cp - 10. From count: c = 10 - a - b = 10 - a - (2a + cp - 10) = 20 - 3a - cp. So c + cp = 20 - 3a → c(1+p) = 20 - 3a → c = (20-3a)/(1+p). And b = 2a + cp - 10.

Need b ≥ 0: 2a + cp ≥ 10. And c ≥ 0: 20 - 3a ≥ 0 → a ≤ 6.

Cubes = 8a + cp^3 - b = 8a + cp^3 - 2a - cp + 10 = 6a + cp(p^2-1) + 10.

Substitute c = (20-3a)/(1+p): cp = (20-3a)p/(1+p), cp(p^2-1) = (20-3a)p(p^2-1)/(1+p) = (20-3a)p(p-1)(p+1)/(1+p) = (20-3a)p(p-1).

So cubes = 6a + (20-3a)p(p-1) + 10.

Let me denote this as F(a,p) = 6a + 10 + (20-3a)p(p-1), with p ∈ [1,2], a ∈ {0,...,6}, and need b=2a+cp-10 ≥ 0 where c=(20-3a)/(1+p).

b = 2a + (20-3a)p/(1+p) - 10. Let me check feasibility. 

To maximize F: ∂F/∂p = (20-3a)(2p-1). For a ≤ 6, 20-3a ≥ 2 > 0, and 2p-1 > 0 for p≥1. So F increasing in p. Max at p=2.

At p=2: F = 6a + 10 + (20-3a)*2*1 = 6a + 10 + 40 - 6a = 50.

Wait, F=50 at p=2?! That's higher than 47.5! Let me check feasibility at p=2.

At p=2: c = (20-3a)/3, b = 2a + 2c - 10 = 2a + 2(20-3a)/3 - 10 = 2a + (40-6a)/3 - 10 = (6a + 40 - 6a - 30)/3 = 10/3.

So b = 10/3, c = (20-3a)/3. Need b,c ≥ 0 and a + b + c = 10. a + 10/3 + (20-3a)/3 = a + (10 + 20 - 3a)/3 = a + (30-3a)/3 = a + 10 - a = 10. ✓

But b = 10/3 is not an integer! b is the count of variables at -1, must be a non-negative integer. So p=2 with integer a,b,c is infeasible unless b is integer.

Hmm, but actually a, b, c don't all need to be integers — they're counts of variables, so they must be non-negative integers. b=10/3 is not integer. So p=2 exactly is infeasible.

But we can take p close to 2. Wait, but p is determined by λ which is free. Let me reconsider — a, b, c must be integers (counts), but p is continuous. So we need c = (20-3a)/(1+p) to be a non-negative integer, and b = 2a + cp - 10 to be a non-negative integer.

Let me reconsider. Actually we don't need c and b to make p=2 exactly. Let me find feasible (a, b, c, p) with p ∈ [1,2] and check F.

We have c = (20-3a)/(1+p) must be a non-negative integer, b = 10 - a - c must be a non-negative integer, and b = 2a + cp - 10 ≥ 0.

Let me just enumerate integer a, c and solve for p. From c(1+p) = 20 - 3a → p = (20-3a)/c - 1 = (20-3a-c)/c. Need p ∈ [1,2]: 1 ≤ (20-3a-c)/c ≤ 2 → c ≤ 20-3a-c ≤ 2c → 2c ≤ 20-3a and 20-3a ≤ 3c → c ≥ (20-3a)/3 and c ≤ (20-3a)/2.

And b = 10 - a - c ≥ 0 → c ≤ 10 - a. And b = 2a + cp - 10 = 2a + (20-3a-c) - 10 = 10 - 3a + (20-3a-c)... wait let me recompute. cp = 20-3a-c. b = 2a + cp - 10 = 2a + 20 - 3a - c - 10 = 10 - a - c. Consistent. Need b ≥ 0: c ≤ 10-a.

F = 6a + 10 + (20-3a)p(p-1) where p = (20-3a-c)/c.

Let me just enumerate. a from 0 to 6.

a=6: 20-18=2. c ∈ [2/3, 1] ∩ integers, c ≤ 4. c=1: p=(2-1)/1=1. F=36+10+2*1*0=46. b=10-6-1=3. Check: 6 at 2, 1 at p=1, 3 at -1. Sum=12+1-3=10 ✓. Cubes=48+1-3=46. Less than 47.5.

a=5: 20-15=5. c ∈ [5/3, 5/2]=[1.67,2.5], c≤5. c=2: p=(5-2)/2=1.5. F=30+10+5*1.5*0.5=40+3.75=43.75. b=10-5-2=3. Check: 5 at 2, 2 at 1.5, 3 at -1. Sum=10+3-3=10 ✓. Cubes=40+2*3.375-3=40+6.75-3=43.75. Less.

a=4: 20-12=8. c ∈ [8/3, 4]=[2.67,4], c≤6. c=3: p=(8-3)/3=5/3≈1.667. F=24+10+8*(5/3)*(2/3)=34+8*10/9=34+8.889=42.889. c=4: p=(8-4)/4=1. F=24+10+0=34. Less.

a=3: 20-9=11. c∈[11/3,11/2]=[3.67,5.5], c≤7. c=4: p=(11-4)/4=1.75. F=18+10+11*1.75*0.75=28+14.4375=42.4375. c=5: p=(11-5)/5=1.2. F=28+11*1.2*0.2=28+2.64=30.64. Less.

a=2: 20-6=14. c∈[14/3,7]=[4.67,7], c≤8. c=5: p=(14-5)/5=1.8. F=12+10+14*1.8*0.8=22+20.16=42.16. c=6: p=(14-6)/6=4/3. F=22+14*(4/3)*(1/3)=22+56/9=22+6.22=28.22. c=7: p=1. F=22. Less.

a=1: 20-3=17. c∈[17/3,17/2]=[5.67,8.5], c≤9. c=6: p=(17-6)/6=11/6≈1.833. F=6+10+17*(11/6)*(5/6)=16+17*55/36=16+25.97=41.97. c=7: p=10/7. F=16+17*(10/7)*(3/7)=16+17*30/49=16+10.41=26.41. Less.

a=0: 20. c∈[20/3,10]=[6.67,10], c≤10. c=7: p=13/7. F=10+20*(13/7)*(6/7)=10+20*78/49=10+31.84=41.84. c=8: p=12/8=1.5. F=10+20*1.5*0.5=10+15=25. c=10: p=1. F=10. Less.

So all these KKT points with some at -1 give less than 47.5. The max among them is a=6,c=1,p=1 giving 46, still less.

Now the other family: no variables at -1, interior at ±p with p ≤ 1 (so that -p > -1, interior). Actually if no -1 boundary, then interior values are ±p with p = √(λ/3), and λ < 3 means p < 1 (so -p > -1, valid interior). And 2's at boundary.

Let me set up: a at 2, c at +p, d at -p, no -1's. a+c+d=10. Sum: 2a + cp - dp = 10 → 2a + (c-d)p = 10. Cubes: 8a + (c-d)p^3 = 8a + (c-d)p^3. Let e = c - d. Then 2a + ep = 10, cubes = 8a + ep^3. Also c+d = 10-a, and e=c-d so c=(10-a+e)/2, d=(10-a-e)/2, need c,d ≥ 0 integers → 10-a ≥ |e| and parity.

From 2a + ep = 10 → ep = 10-2a → e = (10-2a)/p. Cubes = 8a + ep*p^2 = 8a + (10-2a)p^2.

To maximize over p: dF/dp = (10-2a)*2p. For a < 5, 10-2a > 0, increasing in p. For a > 5, decreasing. For a=5, constant = 40.

Constraints: p ∈ (0, 1) (interior, p<1 so -p>-1), and c,d ≥ 0 integers, e = (10-2a)/p.

Hmm, also need p such that e makes c,d integers. This is getting complicated. Let me think about it differently.

Actually, the case a=6, d=4 at -p: 2*6 + (0-4)p = 10 → 12 - 4p = 10 → p = 0.5. c=0, d=4. Cubes = 48 + (-4)(0.125) = 48 - 0.5 = 47.5. ✓ This is our solution!

For a=6, p=0.5, F = 8*6 + (10-12)*0.25 = 48 - 0.5 = 47.5. 

For a < 5, F = 8a + (10-2a)p^2, increasing in p, max at p→1 (but p<1 for interior). As p→1, F → 8a + 10-2a = 6a+10. At a=4: 34. At a=0: 10. These are less than 47.5.

Wait but at p=1, -p = -1 which is boundary, not interior. So the limit approaches the -1 boundary case. Anyway, all less than 47.5.

For a=5: F = 40 + 0 = 40 regardless of p. But need 2*5 + ep = 10 → ep = 0 → e=0 (since p>0). So c=d. c+d=5, c=d → not integer. So a=5 with this family: c=d=2.5 infeasible. Actually need c,d integers with c+d=5, c=d impossible. So no valid solution here except... hmm. Actually e=0 means c=d, but c+d=5 odd. Infeasible. So a=5 gives nothing in this family.

For a=6: F = 48 + (-2)p^2 = 48 - 2p^2, decreasing in p. Min... we want max, so p as small as possible. p=0.5 from constraint (e=(10-12)/p=-2/p, need d=(10-6-e)/2... let me recompute. a=6, c+d=4, e=c-d. 2*6+ep=10→ep=-2→e=-2/p. d=(4-e)/2=(4+2/p)/2=2+1/p. Need d ≤ 4 (since c+d=4, d≥0): 2+1/p ≤ 4 → 1/p ≤ 2 → p ≥ 0.5. And d integer, c=4-d integer. At p=0.5: d=2+2=4, c=0. ✓ F=48-2*0.25=47.5. At p>0.5, d=2+1/p, need integer. p=2/3: d=2+1.5=3.5 not integer. p=1: d=3, c=1, but p=1 means -p=-1 boundary. F=48-2=46. So p=0.5 is the feasible max for a=6.

Great, so 47.5 is confirmed as the global max.

So the maximum is 47.5 = 95/2.

Now let me write the proof.

Proof structure:
1. Show 47.5 is achievable: x_1=...=x_6=2, x_7=...=x_10=-1/2. Sum=12-2=10. Cubes=48-4/8=48-0.5=47.5.
2. Show it's the maximum.

For the upper bound, I'll use a tangent line / supporting parabola argument. We want to find a quadratic (or linear) function that dominates x^3 on [-1,2] and use the sum constraint.

Actually, a clean approach: find constants α, β such that x^3 ≤ αx + β for all x ∈ [-1,2], with equality at x=2 and x=-1/2. Then Σx_i^3 ≤ αΣx_i + 10β = 10α + 10β... wait, Σx_i = 10, so Σx_i^3 ≤ α*10 + 10β = 10(α+β). We want this to equal 47.5.

The quadratic αx + β tangent to x^3 at x=2 and x=-1/2. At x=2: 8 = 2α+β. At x=-1/2: -1/8 = -α/2+β. Subtract: 8+1/8 = 2α+α/2 = 5α/2 → 65/8 = 5α/2 → α = 65/8 * 2/5 = 130/40 = 13/4. β = 8 - 2*13/4 = 8 - 13/2 = 3/2.

So claim: x^3 ≤ (13/4)x + 3/2 for all x ∈ [-1,2].

Check: x^3 - (13/4)x - 3/2 ≤ 0. Factor: we know roots at x=2 and x=-1/2. x^3 - (13/4)x - 3/2 = (x-2)(x+1/2)(x - r). Expand (x-2)(x+1/2) = x^2 - 3x/2 - 1. Times (x-r): x^3 - rx^2 - 3x^2/2 + 3rx/2 - x + r = x^3 - (r+3/2)x^2 + (3r/2 - 1)x + r. 

Compare to x^3 - (13/4)x - 3/2: coefficient of x^2 is 0 → r = -3/2. Then coefficient of x: 3(-3/2)/2 - 1 = -9/4 - 1 = -13/4. ✓ Constant: r = -3/2. ✓

So x^3 - (13/4)x - 3/2 = (x-2)(x+1/2)(x+3/2).

On [-1, 2]: x-2 ≤ 0, x+1/2 ≥ -1/2 (can be negative when x < -1/2), x+3/2 ≥ 1/2 > 0.

So sign = (x-2)(x+1/2)(x+3/2). x+3/2 > 0 always on [-1,2]. x-2 ≤ 0 always. So sign = -(positive)(x+1/2) = ... let me think. (x-2) ≤ 0, (x+3/2) > 0, so (x-2)(x+3/2) ≤ 0. Then times (x+1/2): 

If x ≥ -1/2: (x+1/2) ≥ 0, so product ≤ 0. ✓ (x^3 ≤ line)
If x < -1/2: (x+1/2) < 0, and (x-2)(x+3/2) < 0, so product = (neg)(neg) > 0. ✗!

So the inequality x^3 ≤ (13/4)x + 3/2 FAILS for x ∈ [-1, -1/2). 

Hmm. So this linear bound doesn't work globally. The cubic exceeds the line on [-1, -1/2).

So I need a different supporting function. The issue is that x^3 is concave on [-1, 0], so a chord/secant might be needed, or a quadratic upper bound.

Let me reconsider. Since x^3 is concave on [-1,0], the secant line on [-1, -1/2] lies below the curve, not above. So a single line can't dominate x^3 on all of [-1,2] while being tight at 2 and -1/2.

Alternative: use a quadratic upper bound. Find αx^2 + βx + γ ≥ x^3 on [-1,2], tight at x=2 and x=-1/2 (double root at -1/2 since it's an interior tangent point).

At interior tangent point x=-1/2: the quadratic touches x^3, so q(x) - x^3 has a double root at x=-1/2. And q(2) = 8.

q(x) - x^3 = -(x+1/2)^2(x-2) (degree 3, leading coeff -1 to match -x^3... wait x^3 has leading coeff 1, q is degree 2, so q-x^3 has leading coeff -1). 

q(x) - x^3 = -(x+1/2)^2(x-2). Check leading coeff: -(x^2)(x) = -x^3. ✓

So q(x) = x^3 - (x+1/2)^2(x-2). Let me expand (x+1/2)^2 = x^2 + x + 1/4. Times (x-2): x^3 - 2x^2 + x^2 - 2x + x/4 - 1/2 = x^3 - x^2 - 7x/4 - 1/2. 

So q(x) = x^3 - (x^3 - x^2 - 7x/4 - 1/2) = x^2 + 7x/4 + 1/2.

Check: q(2) = 4 + 7/2 + 1/2 = 4 + 4 = 8. ✓ q(-1/2) = 1/4 - 7/8 + 1/2 = 2/8 - 7/8 + 4/8 = -1/8. ✓ (equals (-1/2)^3 = -1/8).

Now need q(x) ≥ x^3 on [-1,2], i.e., q(x) - x^3 = -(x+1/2)^2(x-2) ≥ 0. Since (x+1/2)^2 ≥ 0 and (x-2) ≤ 0 on [-1,2], we have -(x+1/2)^2(x-2) ≥ 0. ✓✓✓

So x^3 ≤ x^2 + 7x/4 + 1/2 for all x ∈ [-1,2], with equality at x=2 and x=-1/2.

Now sum: Σx_i^3 ≤ Σx_i^2 + (7/4)Σx_i + 10*(1/2) = Σx_i^2 + (7/4)*10 + 5 = Σx_i^2 + 35/2 + 5 = Σx_i^2 + 45/2.

Hmm, but this involves Σx_i^2 which we don't know. We need another relation.

We have Σx_i = 10. We need to bound Σx_i^2. By Cauchy-Schwarz or other... Actually we want to show Σx_i^3 ≤ 95/2. From above, Σx_i^3 ≤ Σx_i^2 + 45/2. So need Σx_i^2 ≤ 25.

Is Σx_i^2 ≤ 25 given Σx_i = 10, x_i ∈ [-1,2]? At our optimum, 6 at 2, 4 at -1/2: Σx_i^2 = 6*4 + 4*(1/4) = 24 + 1 = 25. So Σx_i^2 = 25 at optimum.

Is Σx_i^2 ≤ 25 always? Σx_i^2 is convex, maximized at vertices of the polytope. The vertices have variables at 2 or -1. With a at 2, b at -1, a+b=10, 2a-b=10 → a=20/3, not integer. So no vertex with only {-1,2}. The polytope has vertices where 9 variables are at boundary and 1 is free. 

Hmm, this is getting complicated. Let me think differently. Actually, maybe I should find a linear bound that works, by being tight at x=2 and x=-1 (the two endpoints), and check it's an upper bound.

Line through (2, 8) and (-1, -1): slope = 9/3 = 3. Line: y = 3x + 2 (since 3*2+2=8, 3*(-1)+2=-1). 

Is x^3 ≤ 3x + 2 on [-1,2]? x^3 - 3x - 2 = (x-2)(x+1)^2. On [-1,2]: (x-2) ≤ 0, (x+1)^2 ≥ 0, so product ≤ 0. ✓✓✓ 

So x^3 ≤ 3x + 2 on [-1,2], with equality at x=2 and x=-1.

Sum: Σx_i^3 ≤ 3Σx_i + 2*10 = 30 + 20 = 50.

This gives upper bound 50, but our candidate is 47.5. Not tight enough.

The issue: equality requires all x_i ∈ {2, -1}, but that's infeasible (sum would be 2a - (10-a) = 3a-10 = 10 → a=20/3, not integer).

So the linear bound gives 50 but it's not achievable. We need a tighter bound.

Let me go back to the quadratic approach but handle Σx_i^2.

We have x^3 ≤ x^2 + 7x/4 + 1/2 (tight at 2 and -1/2). Sum gives Σx_i^3 ≤ Σx_i^2 + 45/2.

Now I need to show Σx_i^2 ≤ 25 when Σx_i = 10, x_i ∈ [-1,2].

Claim: Σx_i^2 ≤ 25. Proof: Consider x_i^2 on [-1,2]. We want an upper bound. x^2 ≤ ? Linear bound tight at x=2 and x=-1/2: line through (2,4) and (-1/2, 1/4): slope = (4-1/4)/(2+1/2) = (15/4)/(5/2) = 15/4 * 2/5 = 3/2. Line: y - 4 = (3/2)(x-2) → y = (3/2)x + 1. Check at -1/2: -3/4 + 1 = 1/4. ✓

Is x^2 ≤ (3/2)x + 1 on [-1,2]? x^2 - (3/2)x - 1 = (x-2)(x+1/2). On [-1,2]: (x-2) ≤ 0. (x+1/2) ≥ -1/2. So product: if x ≥ -1/2, (x+1/2)≥0, product ≤ 0 ✓. If x < -1/2, (x+1/2) < 0, (x-2) < 0, product > 0 ✗.

Same issue. Fails on [-1, -1/2).

Hmm. Let me try a quadratic bound for x^2. Actually x^2 is convex, so a line can't dominate it on an interval unless... a secant line of a convex function lies above. Wait, for convex functions, the secant line lies ABOVE the function. So x^2 ≤ secant on [-1,2]. Secant through (-1,1) and (2,4): slope=1, y = x+2. Check: x^2 ≤ x+2 → x^2-x-2 ≤ 0 → (x-2)(x+1) ≤ 0 on [-1,2] ✓. 

So x^2 ≤ x + 2 on [-1,2]. Sum: Σx_i^2 ≤ Σx_i + 20 = 10 + 20 = 30. Not tight (gives Σx_i^3 ≤ 30 + 22.5 = 52.5).

This isn't working well. Let me think of a direct approach.

Alternative direct proof: We want to show Σx_i^3 ≤ 95/2.

Let me use the quadratic bound x^3 ≤ x^2 + 7x/4 + 1/2 (tight at 2, -1/2) AND separately bound Σx_i^2.

Actually, let me combine. We have:
- x^3 ≤ x^2 + (7/4)x + 1/2, equality at x=2, x=-1/2.

Σx_i^3 ≤ Σx_i^2 + (7/4)(10) + 5 = Σx_i^2 + 45/2.

Now bound Σx_i^2. Use x^2 ≤ (3/2)x + 1 (tight at 2, -1/2) but this fails on [-1,-1/2). 

Alternatively use a quadratic in x that upper bounds x^2 and uses both Σx_i and Σx_i^2... circular.

Let me try yet another approach. Directly find the best linear upper bound for x^3 that, combined with Σx_i = 10, gives 95/2. We need a line αx + β ≥ x^3 on [-1,2] with 10α + 10β = 95/2, i.e., α + β = 19/4.

But we showed the line through (2,8) and (-1/2,-1/8) gives α=13/4, β=3/2, α+β = 13/4+3/2 = 13/4+6/4 = 19/4. ✓ And 10*(19/4) = 190/4 = 47.5 = 95/2. ✓✓

But this line does NOT dominate x^3 on [-1, -1/2). So we can't use it directly.

The problem is that on [-1, -1/2), x^3 > line. So if any x_i ∈ [-1, -1/2), the bound fails.

But at the optimum, all x_i are either 2 or -1/2, so all are at equality points. The issue is proving no other config does better.

Key insight: we need to handle the region [-1, -1/2) separately. 

Let me think about it more carefully. The function g(x) = x^3 - (13/4)x - 3/2 = (x-2)(x+1/2)(x+3/2). On [-1,2]:
- x ∈ [-1, -1/2): g(x) > 0 (cubic exceeds line)
- x = -1/2: g = 0
- x ∈ (-1/2, 2): g(x) < 0
- x = 2: g = 0

So for x ∈ [-1, -1/2), the cubic is above the line. The excess is g(x) > 0.

So Σx_i^3 = Σ[(13/4)x_i + 3/2 + g(x_i)] = (13/4)(10) + 15 + Σg(x_i) = 65/2 + 15 + Σg(x_i) = 95/2 + Σg(x_i).

So Σx_i^3 = 95/2 + Σg(x_i). We need to show Σg(x_i) ≤ 0.

g(x) = (x-2)(x+1/2)(x+3/2). g(x) > 0 for x ∈ [-1, -1/2), g(x) ≤ 0 for x ∈ [-1/2, 2], g(x) = 0 at x=-1/2, 2.

So if any x_i ∈ [-1, -1/2), it contributes positively to Σg. We need to show the negative contributions from other variables outweigh.

Hmm, this requires using the sum constraint. Let me think.

Let me define the "bad" variables (in [-1,-1/2)) and "good" variables (in [-1/2, 2]). 

For bad variables, g(x) > 0. For good variables not at {2, -1/2}, g(x) < 0.

This is getting complicated. Let me try a cleaner approach.

Alternative: Use the fact that on [-1, 2], we can write x^3 = (13/4)x + 3/2 + (x-2)(x+1/2)(x+3/2), and then show that Σ(x_i - 2)(x_i + 1/2)(x_i + 3/2) ≤ 0 given Σx_i = 10.

Let h(x) = (x-2)(x+1/2)(x+3/2) = x^3 - (13/4)x - 3/2.

We need Σh(x_i) ≤ 0.

Note h(x) = (x-2)(x+1/2)(x+3/2). Let's substitute y_i = x_i + 1/2, so x_i = y_i - 1/2, y_i ∈ [-1/2, 5/2]. Sum: Σy_i = 10 + 5 = 15.

h(x_i) = (y_i - 5/2)(y_i)(y_i + 1) = y_i(y_i+1)(y_i - 5/2).

Hmm, let me try another substitution. Let me think about what makes this tractable.

Actually, let me try a different, more direct proof using convexity/concavity arguments.

The function φ(x) = x^3 is convex on [0,2] and concave on [-1,0].

Claim: At the maximum, all x_i ∈ {2} ∪ (-1, 0) or at -1/2. 

Actually, let me use a cleaner method. Let me prove that the maximum is 95/2 by showing any feasible point has Σx_i^3 ≤ 95/2.

Approach via "smoothing/merging": Show that if two variables are both in (0, 2) (interior of convex region), we can increase the objective by pushing them apart (one toward 2, other toward 0). Similarly for other cases. This leads to the conclusion that at optimum, at most one variable is in the interior of (0,2) and at most one in interior of (-1, 0), etc.

This is the standard "mixing variables" technique. Let me sketch:

Lemma (convex region): If x_i, x_j ∈ [0, 2] with x_i + x_j = S (fixed), then x_i^3 + x_j^3 is maximized when one is as large as possible (2 or S-0) and other as small. Because x^3 convex on [0,2], sum is maximized at endpoints.

Lemma (concave region): If x_i, x_j ∈ [-1, 0] with fixed sum, x_i^3 + x_j^3 is maximized when they're equal (concavity).

Lemma (mixed): If x_i ∈ [-1,0], x_j ∈ [0,2], with fixed sum... need analysis.

This gets complicated with the mixing across regions. Let me try the algebraic approach more carefully.

Let me revisit: Σx_i^3 = 95/2 + Σh(x_i) where h(x) = (x-2)(x+1/2)(x+3/2). Need Σh(x_i) ≤ 0.

Let me split variables: Let A = {i : x_i ≥ -1/2} and B = {i : x_i < -1/2}. For i ∈ A, h(x_i) ≤ 0. For i ∈ B, h(x_i) > 0.

For i ∈ B, x_i ∈ [-1, -1/2). h(x_i) = (x_i - 2)(x_i + 1/2)(x_i + 3/2). Here x_i - 2 < 0, x_i + 1/2 < 0, x_i + 3/2 > 0 (since x_i ≥ -1 > -3/2). So h = (neg)(neg)(pos) > 0. ✓

Let me bound h on [-1, -1/2). h(-1) = (-3)(-1/2)(1/2) = 3/4. h(-1/2) = 0. h is... let me compute h'(x) = 3x^2 - 13/4. At x ∈ [-1,-1/2], 3x^2 ∈ [3/4, 3], so h'(x) = 3x^2 - 13/4 ∈ [3/4 - 13/4, 3 - 13/4] = [-10/4, -1/4] = [-2.5, -0.25]. So h' < 0 on this interval, h decreasing from h(-1)=3/4 to h(-1/2)=0.

For i ∈ A, x_i ∈ [-1/2, 2]. h(x_i) ≤ 0. The most negative is somewhere in the interior. h'(x) = 3x^2 - 13/4 = 0 → x = ±√(13/12) ≈ ±1.04. On [-1/2, 2], critical point at x = √(13/12) ≈ 1.04. h(√(13/12)) = minimum. 

This is getting messy. Let me try to bound differently.

For x ∈ [-1, -1/2): h(x) ≤ h(-1) = 3/4 (since h decreasing). Actually h(x) ∈ (0, 3/4].

For x ∈ [-1/2, 2]: h(x) ≤ 0, and h(x) ≥ h(√(13/12)).

Hmm. Let me try to use the sum constraint more directly.

Let me denote the variables in B as having x_i = -1/2 - δ_i where δ_i ∈ (0, 1/2] (since x_i ∈ [-1, -1/2)). And variables in A have x_i = -1/2 + ε_i where ε_i ∈ [0, 5/2] (x_i ∈ [-1/2, 2]).

Sum constraint: Σx_i = 10. Σ(-1/2 + ε_i for A) + Σ(-1/2 - δ_i for B) = 10. Let |A| = a, |B| = b, a+b=10. -5 + Σε_i - Σδ_i = 10 → Σε_i - Σδ_i = 15.

h(x_i) for i ∈ A: h(-1/2 + ε) = (ε - 5/2)(ε)(ε + 1) = ε(ε+1)(ε - 5/2). For ε ∈ [0, 5/2], this is ≤ 0 (since ε ≥ 0, ε+1 > 0, ε-5/2 ≤ 0).

h(x_i) for i ∈ B: h(-1/2 - δ) = (-δ - 5/2)(-δ)(-δ + 1) = -(δ + 5/2)(δ)(1 - δ)... let me compute. x = -1/2 - δ. x - 2 = -5/2 - δ. x + 1/2 = -δ. x + 3/2 = 1 - δ. h = (-5/2 - δ)(-δ)(1 - δ) = δ(5/2 + δ)(1 - δ). For δ ∈ (0, 1/2], this is > 0 (δ > 0, 5/2+δ > 0, 1-δ > 0). ✓

So Σh = Σ_{A} ε_i(ε_i+1)(ε_i - 5/2) + Σ_{B} δ_i(5/2 + δ_i)(1 - δ_i).

Need Σh ≤ 0, i.e., Σ_{B} δ_i(5/2 + δ_i)(1 - δ_i) ≤ -Σ_{A} ε_i(ε_i+1)(ε_i - 5/2) = Σ_{A} ε_i(ε_i+1)(5/2 - ε_i).

With constraint Σε_i - Σδ_i = 15, i.e., Σε_i = 15 + Σδ_i.

This is still complex. Let me try to bound each term.

For i ∈ B: δ_i(5/2 + δ_i)(1 - δ_i) ≤ ? Since δ_i ∈ (0, 1/2], and the function is increasing in δ on (0, 1/2]? Let me check: f(δ) = δ(5/2+δ)(1-δ). f'(δ) = (5/2+δ)(1-δ) + δ(1-δ) + δ(5/2+δ)(-1) = (5/2+δ)(1-δ) + δ(1-δ) - δ(5/2+δ). = (1-δ)(5/2+δ+δ) - δ(5/2+δ) = (1-δ)(5/2+2δ) - δ(5/2+δ). = 5/2 + 2δ - 5δ/2 - 2δ^2 - 5δ/2 - δ^2 = 5/2 + 2δ - 5δ - 3δ^2 = 5/2 - 3δ - 3δ^2. At δ=1/2: 5/2 - 3/2 - 3/4 = 5/2 - 9/4 = 1/4 > 0. So f increasing on (0, 1/2]. Max at δ=1/2: f(1/2) = (1/2)(3)(1/2) = 3/4. So each B variable contributes at most 3/4 to Σh.

For i ∈ A: ε_i(ε_i+1)(5/2 - ε_i) ≥ 0 (this is the positive contribution that offsets). We need the A contributions to outweigh B.

Hmm, this approach is getting too algebraically heavy. Let me try a cleaner proof.

Let me reconsider. Maybe use a different supporting function. 

What if I use a piecewise argument: show that for x ∈ [-1, -1/2], x^3 ≤ some function, and for x ∈ [-1/2, 2], x^3 ≤ (13/4)x + 3/2, and combine?

On [-1/2, 2]: x^3 ≤ (13/4)x + 3/2 (proved, since (x-2)(x+1/2)(x+3/2) ≤ 0 here).

On [-1, -1/2]: x^3 is concave (since x < 0). For concave function, x^3 ≤ secant line on [-1, -1/2]. Secant through (-1, -1) and (-1/2, -1/8): slope = (-1/8 + 1)/(1/2) = (7/8)/(1/2) = 7/4. Line: y + 1 = (7/4)(x+1) → y = (7/4)x + 7/4 - 1 = (7/4)x + 3/4. Check at -1/2: -7/8 + 3/4 = -7/8 + 6/8 = -1/8. ✓

So on [-1, -1/2]: x^3 ≤ (7/4)x + 3/4 (concavity, secant above).

Now, for variables in [-1, -1/2]: x_i^3 ≤ (7/4)x_i + 3/4.
For variables in [-1/2, 2]: x_i^3 ≤ (13/4)x_i + 3/2.

Sum: Σx_i^3 ≤ (7/4)Σ_{B} x_i + (3/4)|B| + (13/4)Σ_{A} x_i + (3/2)|A|.

Let |A| = a, |B| = b = 10 - a. Σ_A x_i + Σ_B x_i = 10.

= (7/4)Σ_B x_i + (13/4)Σ_A x_i + 3b/4 + 3a/2
= (13/4)(Σ_A x_i + Σ_B x_i) + (7/4 - 13/4)Σ_B x_i + 3b/4 + 3a/2
= (13/4)(10) - (6/4)Σ_B x_i + 3b/4 + 3a/2
= 65/2 - (3/2)Σ_B x_i + 3b/4 + 3a/2

Now a = 10 - b, so 3a/2 = 15 - 3b/2.

= 65/2 - (3/2)Σ_B x_i + 3b/4 + 15 - 3b/2
= 65/2 + 15 - (3/2)Σ_B x_i + 3b/4 - 3b/2
= 65/2 + 15 - (3/2)Σ_B x_i - 3b/4
= 95/2 - (3/2)Σ_B x_i - 3b/4

Now for i ∈ B, x_i ∈ [-1, -1/2], so Σ_B x_i ∈ [-b, -b/2]. Thus -(3/2)Σ_B x_i ∈ [3b/4, 3b/2].

So Σx_i^3 ≤ 95/2 - (3/2)Σ_B x_i - 3b/4. Since -(3/2)Σ_B x_i ≥ 3b/4 (because Σ_B x_i ≤ -b/2), we get... wait that gives Σx_i^3 ≤ 95/2 + (something ≥ 0). That's the wrong direction!

Let me recompute. -(3/2)Σ_B x_i - 3b/4. Σ_B x_i ≤ -b/2 (most negative is -b, least negative is -b/2). So -(3/2)Σ_B x_i ranges from -(3/2)(-b) = 3b/2 (when Σ_B x_i = -b) to -(3/2)(-b/2) = 3b/4 (when Σ_B x_i = -b/2).

So -(3/2)Σ_B x_i - 3b/4 ranges from 3b/2 - 3b/4 = 3b/4 (when Σ_B x_i = -b) to 3b/4 - 3b/4 = 0 (when Σ_B x_i = -b/2).

So Σx_i^3 ≤ 95/2 + [-(3/2)Σ_B x_i - 3b/4] ≤ 95/2 + 3b/4.

This gives Σx_i^3 ≤ 95/2 + 3b/4, which is > 95/2 when b > 0. Not tight enough!

The bound is tight only when b = 0 (no variables in [-1, -1/2)), giving Σx_i^3 ≤ 95/2. 

So: if all x_i ≥ -1/2, then Σx_i^3 ≤ 95/2, with equality when all x_i ∈ {2, -1/2} and the sum is 10 (which gives 6 at 2, 4 at -1/2).

But what if some x_i < -1/2? We need to show that even then, Σx_i^3 ≤ 95/2.

Hmm, so the piecewise approach shows the bound when b=0 but not when b>0. I need to handle b > 0.

Let me think about this differently. When some variables are in [-1, -1/2), can we "improve" the objective by moving them to -1/2 and adjusting others?

Intuition: if x_i ∈ [-1, -1/2), moving it to -1/2 increases x_i (so we need to decrease others to maintain sum). Since x^3 is increasing, increasing x_i increases its cube, but we must decrease others. The net effect...

Actually, let me think about it as: suppose x_i < -1/2. Consider replacing x_i with -1/2 and decreasing some x_j ∈ [-1/2, 2] by (x_i - (-1/2)) = x_i + 1/2 < 0, i.e., increasing x_j by |x_i + 1/2|... no wait. If x_i increases to -1/2, sum increases by (-1/2 - x_i) > 0, so we need to decrease some other variable by that amount.

This is the mixing/smoothing approach. Let me formalize.

Suppose x_1 ∈ [-1, -1/2) and x_2 ∈ [-1/2, 2]. Replace (x_1, x_2) with (x_1 + t, x_2 - t) for small t > 0 (move x_1 toward -1/2, x_2 down). Sum preserved. Change in objective: (x_1+t)^3 + (x_2-t)^3 - x_1^3 - x_2^3 = 3t(x_1^2 - x_2^2) + 3t^2(x_1 + x_2) + ... 

d/dt [(x_1+t)^3 + (x_2-t)^3] at t=0 = 3x_1^2 - 3x_2^2 = 3(x_1^2 - x_2^2) = 3(x_1 - x_2)(x_1 + x_2).

Since x_1 < -1/2 ≤ x_2, we have x_1 < x_2, so x_1 - x_2 < 0. And x_1 + x_2: could be positive or negative.

If x_1 + x_2 < 0 (i.e., x_2 < -x_1 ≤ 1), then 3(x_1-x_2)(x_1+x_2) = (neg)(neg) > 0, so increasing t increases objective. Good, move x_1 up.

If x_1 + x_2 > 0 (i.e., x_2 > -x_1), then derivative < 0, moving x_1 up decreases objective. So we'd want to move x_1 down (t < 0), toward -1.

So the optimal direction depends on the sign of x_1 + x_2. This means the smoothing isn't always in one direction. Complicated.

Let me reconsider. Maybe the maximum with b > 0 (some variables < -1/2) is actually less than 95/2, and I need a better bound for that case.

Let me just try to verify computationally (in my head) some cases with b > 0.

Case: 7 at 2 is infeasible (sum 14, remaining 3 need -4, min -3). 

Case: 6 at 2, 1 at -1, 3 at -1/3: sum 12 - 1 - 1 = 10. Cubes 48 - 1 - 3/27 = 48 - 1 - 1/9 = 46.889. < 47.5.

Case: 6 at 2, 2 at -1, 2 at 0: sum 12 - 2 = 10. Cubes 48 - 2 = 46. < 47.5.

Case: 6 at 2, 3 at -1, 1 at 1: sum 12 - 3 + 1 = 10. Cubes 48 - 3 + 1 = 46. < 47.5.

Case: 5 at 2, 1 at -1, 4 at 1/4: sum 10 - 1 + 1 = 10. Cubes 40 - 1 + 4/64 = 39 + 1/16 = 39.0625. < 47.5.

Case: 6 at 2, 1 at -0.9, 3 at (-2+0.9)/3 = -1.1/3 ≈ -0.367: sum 12 - 0.9 - 1.1 = 10. Cubes 48 - 0.729 + 3*(-0.0494) = 48 - 0.729 - 0.148 = 47.12. < 47.5.

Case: 6 at 2, 1 at -1, 1 at -1/2, 2 at -1/4: sum 12 - 1 - 0.5 - 0.5 = 10. Cubes 48 - 1 - 0.125 - 2*0.0156 = 46.72. < 47.5.

It really seems 47.5 is the max. Let me try to find a cleaner proof.

Cleaner approach: Let me use the substitution and a single inequality.

We want to show: for x ∈ [-1, 2], x^3 ≤ (13/4)x + 3/2 + c·(x + 1/2)·(something)...

Actually, let me try to find a quadratic q(x) = αx^2 + βx + γ such that x^3 ≤ q(x) on [-1,2] and Σq(x_i) can be bounded using Σx_i = 10 and known bounds on Σx_i^2.

We had q(x) = x^2 + 7x/4 + 1/2 (tight at 2, -1/2, double root). This gives Σx_i^3 ≤ Σx_i^2 + 45/2. Need Σx_i^2 ≤ 25.

So let me prove Σx_i^2 ≤ 25 given Σx_i = 10, x_i ∈ [-1, 2].

Σx_i^2 ≤ 25: This is equivalent to Σx_i^2 ≤ 25. Using x_i^2 = (x_i - 1)^2 + 2x_i - 1... hmm. Σx_i^2 = Σ(x_i - 1)^2 + 2Σx_i - 10 = Σ(x_i-1)^2 + 20 - 10 = Σ(x_i-1)^2 + 10. So Σx_i^2 ≤ 25 ⟺ Σ(x_i - 1)^2 ≤ 15.

Let y_i = x_i - 1 ∈ [-2, 1], Σy_i = 0. Need Σy_i^2 ≤ 15.

Hmm, is this true? y_i ∈ [-2, 1], Σy_i = 0. Maximize Σy_i^2. Since y^2 is convex, max at vertices: y_i ∈ {-2, 1}. Let a at -2, b at 1, a+b=10, -2a+b=0 → b=2a, 3a=10, a=10/3. Not integer. So no pure vertex solution.

Vertices of the polytope {y ∈ [-2,1]^10 : Σy = 0}: 9 variables at boundary, 1 free. Let's say k at -2, (9-k) at 1, one free at v. Sum: -2k + (9-k) + v = 0 → v = 3k - 9. Need v ∈ [-2, 1]: -2 ≤ 3k-9 ≤ 1 → 7 ≤ 3k ≤ 10 → k ∈ {3} (k=3: v=0; k=7/3 no). Wait 7/3 ≤ k ≤ 10/3, so k=3 (v=0) or... k must be integer, k=3 gives v=0. k=10/3 not integer. Actually k can be 3 only (since 7/3 ≈ 2.33 and 10/3 ≈ 3.33, integer k = 3).

Wait, also need to check: with k at -2 and (9-k) at 1, that's 9 variables. The 10th is free. k=3: 3 at -2, 6 at 1, 1 at 0. Σy^2 = 3*4 + 6*1 + 0 = 18. That's > 15!

So Σy_i^2 can be 18 > 15. So Σx_i^2 can be 28 > 25. So the bound Σx_i^2 ≤ 25 is FALSE!

Let me verify: y = (-2,-2,-2,1,1,1,1,1,1,0), x = y+1 = (-1,-1,-1,2,2,2,2,2,2,1). Σx = -3+12+1 = 10. ✓ Σx^2 = 3+24+1 = 28. Σx^3 = -3+48+1 = 46. < 47.5. OK so Σx^2 = 28 but Σx^3 = 46 < 47.5.

So Σx_i^2 ≤ 25 is false, meaning the quadratic bound approach (q = x^2 + 7x/4 + 1/2) gives Σx_i^3 ≤ 28 + 22.5 = 50.5, not tight.

So that approach fails. Back to the drawing board.

Let me reconsider. The piecewise linear approach gave: if all x_i ≥ -1/2, then Σx_i^3 ≤ 95/2. I need to handle the case where some x_i < -1/2.

Let me think about what happens when some x_i < -1/2. Intuitively, pushing a variable below -1/2 "wastes" sum budget (the variable contributes negatively to sum but its cube is also very negative), and the remaining variables can't compensate enough.

Let me try to prove: if any x_i < -1/2, then Σx_i^3 < 95/2.

Approach: Suppose x_1 < -1/2. Consider modifying the solution: set x_1' = -1/2 and adjust. We need to increase sum by (x_1' - x_1) = -1/2 - x_1 > 0, so decrease some other variables. 

Actually, let me think about it as: we want to show that the maximum over the full feasible set equals the maximum over the restricted set {x_i ≥ -1/2 for all i}.

Claim: If (x_1, ..., x_10) is feasible with some x_i < -1/2, then there exists a feasible point with all x_j ≥ -1/2 and Σx_j^3 ≥ Σx_i^3.

If true, then the max over the full set = max over restricted set = 95/2.

To prove the claim: take x_1 < -1/2. We want to increase x_1 to -1/2 (gaining cube since x^3 increasing) and decrease some other variable x_2 > -1/2 by the same amount. The net change in cubes: 

Δ = [(-1/2)^3 - x_1^3] + [(x_2 - (-1/2 - x_1))^3 - x_2^3] where we decrease x_2 by d = -1/2 - x_1 > 0.

Wait, we increase x_1 by d = -1/2 - x_1 > 0 (to -1/2), and decrease x_2 by d (to x_2 - d). Need x_2 - d ≥ -1/2, i.e., x_2 ≥ -1/2 + d = -1/2 + (-1/2 - x_1) = -1 - x_1. Since x_1 ≥ -1, -1 - x_1 ≤ 0. And x_2 ≥ -1/2 > 0 ≥ -1-x_1 when x_1 ≥ -1. Actually -1 - x_1 ∈ [-0, 0] when x_1 ∈ [-1, 0]. And x_2 ≥ -1/2. Is -1/2 ≥ -1 - x_1? -1/2 ≥ -1 - x_1 ⟺ x_1 ≥ -1/2. But x_1 < -1/2! So -1 - x_1 > -1/2, meaning we need x_2 > -1/2, which is true if x_2 > -1/2. But x_2 might equal -1/2.

Hmm, need x_2 - d ≥ -1, i.e., x_2 ≥ -1 + d = -1 + (-1/2 - x_1) = -3/2 - x_1. Since x_1 ≥ -1, -3/2 - x_1 ≤ -1/2. And x_2 ≥ -1 ≥ -3/2 - x_1 (since -3/2 - x_1 ≤ -1/2 < -1... wait -3/2 - x_1 when x_1 = -1 is -3/2 + 1 = -1/2; when x_1 = -1/2 it's -3/2 + 1/2 = -1). So -3/2 - x_1 ∈ [-1, -1/2] for x_1 ∈ [-1, -1/2]. And x_2 ≥ -1. So x_2 ≥ -1 ≥ -3/2 - x_1? Need -1 ≥ -3/2 - x_1 ⟺ x_1 ≥ -1/2. Not always true. When x_1 < -1/2, -3/2 - x_1 > -1, so we need x_2 > -1. 

OK this is getting complicated. Let me just require x_2 > -1 (strictly interior from below) or handle boundary cases separately.

Assume x_2 > -1 (and x_2 > -1/2 since all others ≥ -1/2 or we pick one that is). Actually, if x_1 is the only variable < -1/2, then x_2, ..., x_10 ≥ -1/2 > -1, so x_2 > -1. Good.

If multiple variables < -1/2, pick x_1 < -1/2 and x_2 ≥ -1/2 (there must be some since sum = 10 > 10*(-1/2) = -5, so not all < -1/2). Then x_2 ≥ -1/2 > -1.

OK so assume x_2 ≥ -1/2 and x_2 - d ≥ -1 where d = -1/2 - x_1 ∈ (0, 1/2]. Since x_2 ≥ -1/2 and d ≤ 1/2, x_2 - d ≥ -1. ✓ (And if x_2 - d < -1/2, that's OK, we just might need to iterate.)

Change in cubes: Δ = [(-1/2)^3 - x_1^3] + [(x_2 - d)^3 - x_2^3].

= [-1/8 - x_1^3] + [(x_2 - d)^3 - x_2^3].

Let me use the identity: (x_2 - d)^3 - x_2^3 = -3x_2^2 d + 3x_2 d^2 - d^3 = -d(3x_2^2 - 3x_2 d + d^2).

And -1/8 - x_1^3 = -(x_1^3 + 1/8) = -(x_1 + 1/2)(x_1^2 - x_1/2 + 1/4). Since x_1 < -1/2, x_1 + 1/2 < 0, so -(x_1+1/2) > 0, and x_1^2 - x_1/2 + 1/4 > 0 (discriminant 1/4 - 1 < 0). So -1/8 - x_1^3 > 0. Good, first term positive.

Δ = -(x_1 + 1/2)(x_1^2 - x_1/2 + 1/4) - d(3x_2^2 - 3x_2 d + d^2) where d = -1/2 - x_1 = -(x_1 + 1/2).

So Δ = d(x_1^2 - x_1/2 + 1/4) - d(3x_2^2 - 3x_2 d + d^2) = d[(x_1^2 - x_1/2 + 1/4) - (3x_2^2 - 3x_2 d + d^2)].

Need Δ ≥ 0, i.e., x_1^2 - x_1/2 + 1/4 ≥ 3x_2^2 - 3x_2 d + d^2.

This is not always true. For example, if x_2 = 2, RHS = 12 - 6d + d^2, LHS = x_1^2 - x_1/2 + 1/4 ≤ 1 + 1/2 + 1/4 = 1.75 (for x_1 = -1). So Δ < 0. Moving mass from x_2=2 to x_1 decreases objective.

This makes sense: if x_2 = 2 (at max), we don't want to decrease it. We'd want to decrease a variable that's not at 2.

So the smoothing argument needs to choose x_2 carefully. We should decrease a variable that's "less valuable" - i.e., not at 2.

This is getting quite involved. Let me try a completely different, cleaner proof strategy.

Proof via Lagrange multipliers / KKT, showing the unique KKT point with all conditions satisfied and highest objective is our candidate.

Actually, let me try to use a cleaner inequality. 

Key inequality: For x ∈ [-1, 2], 
x^3 ≤ (13/4)x + 3/2 + (3/4)(x + 1/2)(1 - (x+1/2)/(5/2))... no, too ad hoc.

Let me try: find the best quadratic upper bound ax^2 + bx + c ≥ x^3 on [-1, 2] such that 10a·(avg of x^2)... no, we don't know Σx^2.

Hmm. Let me try using both Σx_i = 10 and the constraint x_i ≤ 2 more cleverly.

Note that (2 - x_i) ≥ 0 for all i. And Σx_i = 10, so Σ(2 - x_i) = 20 - 10 = 10.

Also (x_i + 1) ≥ 0. Σ(x_i + 1) = 20.

Let me write x_i^3 in terms of (x_i - 2) and (x_i + 1/2) and (x_i + 3/2) as before: x_i^3 = (13/4)x_i + 3/2 + (x_i - 2)(x_i + 1/2)(x_i + 3/2).

Σx_i^3 = 95/2 + Σ(x_i - 2)(x_i + 1/2)(x_i + 3/2).

Let u_i = x_i + 1/2 ∈ [-1/2, 5/2]. Then x_i - 2 = u_i - 5/2, x_i + 3/2 = u_i + 1. Σu_i = 15.

Σx_i^3 = 95/2 + Σ(u_i - 5/2)(u_i)(u_i + 1) = 95/2 + Σ u_i(u_i+1)(u_i - 5/2).

Need to show Σ u_i(u_i+1)(u_i - 5/2) ≤ 0, where u_i ∈ [-1/2, 5/2], Σu_i = 15.

Let f(u) = u(u+1)(u - 5/2) = u^3 - (3/2)u^2 - (5/2)u.

Σf(u_i) = Σu_i^3 - (3/2)Σu_i^2 - (5/2)Σu_i = Σu_i^3 - (3/2)Σu_i^2 - 75/2.

Need Σu_i^3 - (3/2)Σu_i^2 ≤ 75/2.

Hmm, still involves Σu^2 and Σu^3.

Let me try yet another angle. Let me use the constraint x_i ≤ 2 directly.

Since x_i ≤ 2, we have x_i^3 ≤ 2x_i^2 (because x_i^3 = x_i · x_i^2 ≤ 2x_i^2 when x_i ≤ 2; but this fails when x_i < 0 since x_i^3 < 0 < 2x_i^2, actually it holds: if x_i ≥ 0, x_i^3 ≤ 2x_i^2; if x_i < 0, x_i^3 < 0 ≤ 2x_i^2). So x_i^3 ≤ 2x_i^2 for all x_i ∈ [-1, 2]. ✓

So Σx_i^3 ≤ 2Σx_i^2. But we showed Σx_i^2 can be up to 28, giving 56. Not helpful.

Also x_i^3 ≤ 4x_i (for x_i ∈ [0,2], x_i^2 ≤ 4 so x_i^3 ≤ 4x_i; for x_i < 0, x_i^3 < 0 ≤ 4x_i... no, 4x_i < 0 when x_i < 0, and x_i^3 < 4x_i iff x_i^2 > 4 iff |x_i| > 2, not the case). So for x_i ∈ [-1, 0): x_i^3 vs 4x_i: x_i^3 - 4x_i = x_i(x_i^2 - 4). x_i < 0, x_i^2 < 1 < 4, so x_i^2 - 4 < 0, product > 0. So x_i^3 > 4x_i for x_i ∈ [-1, 0). So x_i^3 ≤ 4x_i fails for negative x_i.

Let me try to combine inequalities. For x ∈ [-1, 2]:
- x^3 ≤ 4x for x ∈ [0, 2] (since x^2 ≤ 4)
- x^3 ≤ ? for x ∈ [-1, 0]

For x ∈ [-1, 0]: x^3 = x · x^2, and x^2 ≤ 1, x ≤ 0, so x^3 ≥ x · 1 = x (more negative). Actually x^3 ≥ -1 and x ≥ -1. x^3 - x = x(x^2-1) = x(x-1)(x+1). For x ∈ [-1,0]: x < 0, x-1 < 0, x+1 ≥ 0, so x(x-1)(x+1) ≥ 0, i.e., x^3 ≥ x. So x^3 ≥ x on [-1, 0]. That's a lower bound, not upper.

For upper bound on [-1,0]: x^3 ≤ 0 (since x ≤ 0). And x^3 = x·x^2 ≤ 0. Also x^3 ≤ x^2 (since x ≤ 1, x^3 ≤ x^2 when x ≤ 1 and x ≥ 0... no). For x ∈ [-1, 0]: x^3 ≤ 0 and we want an upper bound involving x. x^3 ≤ 0 = 0·x + 0. Or x^3 ≤ -x (since x^3 + x = x(x^2+1) ≤ 0 for x ≤ 0, so x^3 ≤ -x). So x^3 ≤ -x on [-1, 0]. And -x ∈ [0, 1].

Hmm, let me try: for x ∈ [-1, 0], x^3 ≤ -x. For x ∈ [0, 2], x^3 ≤ 4x. 

Σx_i^3 ≤ Σ_{x_i<0} (-x_i) + Σ_{x_i≥0} 4x_i. Let P = {i: x_i ≥ 0}, N = {i: x_i < 0}. = -Σ_N x_i + 4Σ_P x_i = 4Σ_P x_i - Σ_N x_i = 4Σ_P x_i + (Σx_i - Σ_P x_i)·(-1)... wait. Σ_N x_i = 10 - Σ_P x_i. So -Σ_N x_i = Σ_P x_i - 10. Thus Σx_i^3 ≤ 4Σ_P x_i + Σ_P x_i - 10 = 5Σ_P x_i - 10.

Σ_P x_i ≤ 2|P|. To maximize 5Σ_P x_i - 10, maximize Σ_P x_i. But Σ_P x_i = 10 - Σ_N x_i, and Σ_N x_i ≥ -|N| = -(10-|P|). So Σ_P x_i ≤ 10 + (10 - |P|) = 20 - |P|. Also Σ_P x_i ≤ 2|P|. So Σ_P x_i ≤ min(2|P|, 20 - |P|).

Max of min(2|P|, 20-|P|) over |P|: 2|P| = 20 - |P| → 3|P| = 20 → |P| = 20/3 ≈ 6.67. At |P|=6: min(12, 14) = 12. At |P|=7: min(14, 13) = 13. So max at |P|=7: 13.

Then Σx_i^3 ≤ 5*13 - 10 = 55. Not tight.

This approach is too loose. Let me go back to the KKT/case analysis approach and present it cleanly.

Actually, let me try the following clean approach using the structure of the problem.

Step 1: Show that at the maximum, at most one variable is in the interior (-1, 2) \ {-1/2}, and if so, it must be -1/2.

Hmm, that's not quite right either. At our solution, 4 variables are at -1/2 (interior).

Let me think about it via the "convex envelope" or "upper concave envelope" of x^3 on [-1, 2].

The upper concave envelope of x^3 on [-1, 2]: Since we're maximizing a sum with a sum constraint, the maximum is related to the concave envelope. Specifically, by the theory of moments / linear programming relaxation, the maximum of Σf(x_i) subject to Σx_i = S and x_i ∈ [a,b] is related to the concave envelope of f.

The concave envelope of f(x) = x^3 on [-1, 2]: 

f is concave on [-1, 0] and convex on [0, 2]. The concave envelope on [0, 2] is the secant line from (0, 0) to (2, 8): y = 4x. On [-1, 0], f is already concave, so the envelope is f itself. But we need the envelope to be concave on all of [-1, 2], so we need to connect them.

The concave envelope: on [-1, 0], it's x^3 (concave). On [0, 2], it's the line 4x. But at x=0, x^3 = 0 and 4x = 0, continuous. Is the combined function concave? At x=0, left derivative of x^3 is 0, right derivative of 4x is 4. For concavity, we need left derivative ≥ right derivative, but 0 < 4. So NOT concave. 

So the concave envelope needs adjustment. The concave envelope is the smallest concave function ≥ x^3 on [-1, 2].

Let me find it. The concave envelope will be x^3 on some interval [-1, c] and a line on [c, 2], where the line is tangent to x^3 at c and passes through (2, 8).

Line through (c, c^3) and (2, 8) with slope matching 3c^2 at c: slope = 3c^2 = (8 - c^3)/(2 - c). So 3c^2(2-c) = 8 - c^3 → 6c^2 - 3c^3 = 8 - c^3 → 6c^2 - 2c^3 = 8 → 2c^3 - 6c^2 + 8 = 0 → c^3 - 3c^2 + 4 = 0 → (c-2)(c^2 - c - 2) = (c-2)(c-2)(c+1) = (c-2)^2(c+1) = 0. So c = 2 or c = -1. 

That gives the line through (2, 8) tangent at x=2, which is y = 12x - 16 (slope 12). At x=-1: 12(-1)-16 = -28 < -1 = (-1)^3. So this line is below x^3 at x=-1, not an upper bound. 

Hmm, so the tangent from (2,8) to the curve only touches at 2 (double root) and -1. The line through (2,8) and (-1,-1) is y = 3x + 2, slope 3. At x=-1, slope of x^3 is 3(-1)^2 = 3. So the line y = 3x+2 is tangent to x^3 at x = -1! And passes through (2, 8). 

So the concave envelope is: the line 3x + 2 on [-1, 2]? But we need to check it's ≥ x^3. We showed (x-2)(x+1)^2 ≤ 0 on [-1, 2], so x^3 ≤ 3x + 2. ✓ And the line is tangent at x=-1 and passes through (2,8). 

But is 3x+2 concave (yes, linear) and ≥ x^3? Yes. Is it the smallest concave majorant? At x=-1, both equal -1 and same slope, so it's tight there. At x=2, both equal 8. In between, 3x+2 > x^3 (strictly for x ∈ (-1, 2)). 

So the concave envelope of x^3 on [-1, 2] is 3x + 2. Then by Jensen's inequality for the concave envelope:

Σx_i^3 ≤ Σ(3x_i + 2) = 3·10 + 20 = 50.

But this gives 50, not 47.5. The issue is that the concave envelope gives the LP relaxation bound, which is 50, but it's not achievable because achieving equality requires all x_i at the contact points {-1, 2}, and no feasible solution has all x_i ∈ {-1, 2} with sum 10.

So the concave envelope approach gives 50, which is the LP bound but not tight due to integrality-like constraints (we need exactly 10 variables).

This means the problem is more subtle. The maximum 47.5 is less than the concave envelope bound 50 because we can't achieve the envelope's equality conditions.

So I need a proof that accounts for the discrete nature (10 variables). 

Let me think about this more carefully using the "moment" approach. We have 10 variables. Think of it as a distribution: let the empirical distribution be μ = (1/10)Σδ_{x_i}. Then Σx_i = 10 → E_μ[x] = 1. Σx_i^3 = 10·E_μ[x^3]. We want to maximize E[x^3] subject to E[x] = 1 and support in [-1, 2], with the constraint that μ is a uniform distribution on 10 points (i.e., each point has mass 1/10).

Without the "10 points" constraint, the max of E[x^3] with E[x]=1, support [-1,2] is given by the concave envelope: E[x^3] ≤ E[3x+2] = 3+2 = 5, so Σx_i^3 ≤ 50. Achieved by a distribution on {-1, 2} with E[x]=1: P(x=2) = p, P(x=-1) = 1-p, 2p - (1-p) = 1 → 3p = 2 → p = 2/3. So 2/3 of mass at 2, 1/3 at -1. With 10 variables, that's 20/3 at 2 and 10/3 at -1, not integer.

So the problem reduces to: we need 10 points (with repetition) in [-1, 2] summing to 10, maximizing Σx_i^3. The continuous relaxation gives 50 but requires non-integer counts at {-1, 2}.

Now, the key insight: since we can't have all points at {-1, 2}, some points must be in the interior, where x^3 < 3x + 2 strictly. The "loss" from the envelope is Σ(3x_i + 2 - x_i^3) = 50 - Σx_i^3 = Σ[-(x_i-2)(x_i+1)^2] = Σ(2-x_i)(x_i+1)^2.

So Σx_i^3 = 50 - Σ(2-x_i)(x_i+1)^2. We want to minimize Σ(2-x_i)(x_i+1)^2 subject to Σx_i = 10, x_i ∈ [-1, 2].

Let φ(x) = (2-x)(x+1)^2 ≥ 0 on [-1, 2]. We want to minimize Σφ(x_i) with Σx_i = 10.

At x = 2: φ = 0. At x = -1: φ = 0. At x = -1/2: φ = (5/2)(1/2)^2 = 5/8. At x = 0: φ = 2. At x = 1: φ = 1·4 = 4.

So φ is 0 at the endpoints, positive in between. To minimize Σφ, we want variables at endpoints (2 or -1). But we can't have all at endpoints with sum 10 (as shown).

So we need some variables in the interior, and we want to minimize the total φ. 

If we have a at 2, b at -1, and the rest in interior: 2a - b + (interior sum) = 10. To minimize Σφ, we want as many at endpoints as possible and the interior ones to have small φ.

φ(x) = (2-x)(x+1)^2. φ'(x) = -(x+1)^2 + 2(2-x)(x+1) = (x+1)[-(x+1) + 2(2-x)] = (x+1)[-x-1+4-2x] = (x+1)(3-3x) = 3(x+1)(1-x). Zero at x=-1, x=1. φ''(x) = 3[(1-x) - (x+1)] = 3(1-x-x-1) = -6x. At x=1: φ''=-6 < 0, local max. At x=-1: φ''=6 > 0, local min (φ=0).

So φ increases from 0 at x=-1 to max at x=1 (φ(1)=4), then decreases to 0 at x=2. 

To minimize Σφ with fixed Σx_i = 10: we want variables where φ is small, i.e., near -1 or near 2. 

If we must have interior variables, they should be near -1 or near 2 (where φ is small). But near -1, x ≈ -1 contributes ≈ -1 to sum; near 2, x ≈ 2 contributes ≈ 2.

Let me think about it as: suppose we have a variables at 2, b at -1, and c = 10 - a - b interior variables. Sum: 2a - b + S_int = 10, where S_int is the sum of interior variables. φ contribution: 0 + 0 + Σφ(interior) = Σφ(interior). We want to minimize Σφ(interior) subject to Σ(interior) = 10 - 2a + b, and interior vars in (-1, 2).

To minimize Σφ with fixed sum, by convexity/concavity analysis... φ is convex
