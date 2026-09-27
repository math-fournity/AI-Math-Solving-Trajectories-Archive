# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   What is the maximum number of isosceles triangles that can be formed using 100 points on a straight line and one additional point outside the line as vertices?       — 题目文本
#   To determine the maximum number of isosceles triangles that can be formed using 100 points on a straight line and one additional point outside the line, we need to carefully analyze the conditions under which such triangles can be formed.

### Step-by-Step Solution:

1. **Identify the Key Components:**
   - There are 100 points on a straight line.
   - There is one additional point \( P \) outside the line.
   - Each isosceles triangle must have \( P \) as one of its vertices.

2. **Conditions for Isosceles Triangles:**
   - An isosceles triangle has at least two equal sides.
   - The external point \( P \) must be one of the vertices.
   - The other two vertices must be points on the line.

3. **Symmetric Arrangement:**
   - To maximize the number of isosceles triangles, we should arrange the points on the line symmetrically around the projection of \( P \) onto the line.
   - Let \( O \) be the projection of \( P \) onto the line.

4. **Forming Isosceles Triangles:**
   - For each pair of points \( A \) and \( B \) on the line, if \( A \) and \( B \) are equidistant from \( O \), then \( PA = PB \).
   - This configuration forms an isosceles triangle \( PAB \) with \( P \) as the apex.

5. **Counting Symmetric Pairs:**
   - With 100 points on the line, we can arrange them symmetrically around \( O \).
   - This means 50 points on one side of \( O \) and 50 points on the other side.
   - Each point on one side will have a corresponding point on the other side, forming a symmetric pair.

6. **Calculating the Number of Isosceles Triangles:**
   - Each symmetric pair \( (A, B) \) forms one isosceles triangle \( PAB \).
   - Since there are 50 such pairs, the number of isosceles triangles is 50.

### Conclusion:
By arranging the 100 points symmetrically around the projection of the external point onto the line, we maximize the number of isosceles triangles. Each pair of symmetric points forms one isosceles triangle with the external point, resulting in a total of 50 such triangles.

Thus, the maximum number of isosceles triangles is:

\[
\boxed{50}
\]  — 标准解答
#   Let me solve this problem. We have 100 points on a straight line and one additional point outside the line. We need to find the maximum number of isosceles triangles that can be formed using these 101 points as vertices.

First, let me check for answer leaks - the problem statement is clean, just asking the question. No leaked answers.

Now let me think about the problem.

We have 100 collinear points on a line L, and one point P outside the line. Total 101 points. We want to maximize the number of isosceles triangles.

A triangle needs 3 non-collinear points. Since 100 points are on the line, any triangle must use at least one point off the line. The only point off the line is P. So every triangle must include P.

Wait, can we form a triangle with 3 points on the line? No, they're collinear, so that's degenerate. So every triangle must include P and exactly 2 points from the line.

So triangles are of the form (P, A, B) where A, B are on the line.

Now, when is triangle PAB isosceles?

The three sides are PA, PB, AB.

Case 1: PA = PB (P is equidistant from A and B). This means A and B are symmetric about the foot of perpendicular from P to the line.

Case 2: PA = AB. The side from P to A equals the side from A to B (on the line).

Case 3: PB = AB. The side from P to B equals the side from A to B (on the line).

We want to maximize the total count of isosceles triangles, where each triangle is counted once.

Let me set up coordinates. Let the line be the x-axis, and P = (0, h) for some h > 0. The 100 points are at positions x_1, x_2, ..., x_100 on the x-axis.

For a triangle (P, A, B) with A = (a, 0), B = (b, 0):

- PA = sqrt(a² + h²)
- PB = sqrt(b² + h²)
- AB = |a - b|

Isosceles conditions:
1. PA = PB: a² + h² = b² + h², so a² = b², so a = -b (since a ≠ b for non-degenerate). This means A and B are symmetric about x=0 (the foot of perpendicular).

2. PA = AB: sqrt(a² + h²) = |a - b|, so a² + h² = (a-b)² = a² - 2ab + b², so h² = b² - 2ab, so b² - 2ab - h² = 0, solving for b: b = a ± sqrt(a² + h²). So b = a + sqrt(a²+h²) or b = a - sqrt(a²+h²).

3. PB = AB: similarly, a = b ± sqrt(b² + h²).

We want to choose the 100 positions to maximize the number of isosceles triangles.

Let me think about this more carefully. Each triangle (P, A, B) is determined by the unordered pair {A, B}. We want to maximize the number of pairs {A, B} such that at least one of the three isosceles conditions holds.

Let me think about each case separately and then worry about overlaps.

Case 1: PA = PB. This requires a = -b. So for each pair of points symmetric about 0, we get one isosceles triangle. If we place k points at positions and their negatives, we get floor(k/2) such pairs... actually, we need pairs (a, -a) with a ≠ 0. If we have points at positions x and -x, that's one pair. The maximum number of such pairs from 100 points: place 50 points at positive positions and 50 at their negatives. That gives 50 pairs. But we could also place a point at 0, but then it can't pair with anything (0 = -0). So max from Case 1 is 50.

Case 2: PA = AB. For a given A at position a, B must be at position a + sqrt(a²+h²) or a - sqrt(a²+h²). 

Case 3: PB = AB. For a given B at position b, A must be at position b + sqrt(b²+h²) or b - sqrt(b²+h²).

Cases 2 and 3 are symmetric (just swapping A and B labels). Let me think about them together.

For a point at position a, the "partner" positions that create an isosceles triangle where the equal sides are PA and AB (or PB and AB) are:
- b = a + sqrt(a² + h²)  (B is to the right of A, and PA = AB)
- b = a - sqrt(a² + h²)  (B is to the left of A, and PA = AB)
- a' = b + sqrt(b² + h²) → but this is case 3 from B's perspective

Actually, let me reconsider. For each ordered pair (A, B), case 2 gives PA = AB and case 3 gives PB = AB. Since we're counting unordered pairs {A, B}, we should think of it as: for the pair {A, B}, is it the case that PA = AB or PB = AB or PA = PB?

Let me think about it differently. For each point at position x_i, define:
- f(x_i) = x_i + sqrt(x_i² + h²): the position such that if another point is there, the triangle with A=x_i has PA = AB (B to the right)
- g(x_i) = x_i - sqrt(x_i² + h²): similarly to the left

Note that f(x) · g(x) = x² - (x² + h²) = -h². So f(x) and g(x) always have opposite signs, and their product is -h².

Also, f(x) = x + sqrt(x²+h²) and g(x) = x - sqrt(x²+h²). Note that g(x) = -h²/f(x).

Interesting. So if y = f(x), then x = g(y)? Let's check: if y = x + sqrt(x²+h²), then sqrt(x²+h²) = y - x, so x² + h² = y² - 2xy + x², so h² = y² - 2xy, so 2xy = y² - h², so x = (y² - h²)/(2y) = y/2 - h²/(2y). And g(y) = y - sqrt(y²+h²). Let me compute sqrt(y²+h²) where y = x + sqrt(x²+h²).

y² = x² + 2x·sqrt(x²+h²) + x² + h² = 2x² + h² + 2x·sqrt(x²+h²)
y² + h² = 2x² + 2h² + 2x·sqrt(x²+h²)

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me think about the structure more carefully. The key insight is about the function f(x) = x + sqrt(x² + h²).

Note that f is a strictly increasing function (its derivative is 1 + x/sqrt(x²+h²) > 0). Similarly g(x) = x - sqrt(x²+h²) is strictly decreasing.

Also note: f(x) > 0 for all x (since sqrt(x²+h²) > |x|), and g(x) < 0 for all x.

And f(x) · g(x) = -h², so g(x) = -h²/f(x).

Now, the relationship: if y = f(x), is x = g(y)?
g(y) = y - sqrt(y² + h²). We need to check if this equals x.
y = x + sqrt(x²+h²), so y² = x² + 2x·sqrt(x²+h²) + x² + h².
y² + h² = 2x² + 2h² + 2x·sqrt(x²+h²) = 2(x² + h²) + 2x·sqrt(x²+h²).
Let s = sqrt(x²+h²). Then y = x + s, y² + h² = 2s² + 2xs = 2s(s+x) = 2sy.
sqrt(y²+h²) = sqrt(2sy).
g(y) = y - sqrt(2sy) = (x+s) - sqrt(2s(x+s)).

Hmm, this doesn't simplify to x in general. So f and g are not inverses of each other.

Let me reconsider. The condition PA = AB means: for points at positions a and b, sqrt(a²+h²) = |a-b|. This gives b = a + sqrt(a²+h²) or b = a - sqrt(a²+h²), i.e., b = f(a) or b = g(a).

Similarly, PB = AB means sqrt(b²+h²) = |a-b|, giving a = f(b) or a = g(b).

So the pair {a, b} satisfies one of cases 2 or 3 iff b ∈ {f(a), g(a)} or a ∈ {f(b), g(b)}.

But note: b = f(a) is the same as saying a = g(b)? Let me check. If b = f(a) = a + sqrt(a²+h²), then is a = g(b)?
g(b) = b - sqrt(b²+h²). We computed sqrt(b²+h²) = sqrt(2sb) where s = sqrt(a²+h²), b = a+s.
So g(b) = (a+s) - sqrt(2s(a+s)).

This is not equal to a in general. So b = f(a) and a = g(b) are different conditions.

Hmm wait, but actually b = f(a) means PA = AB (with B to the right of A). And a = g(b) means PB = AB (with A to the left of B). These are different isosceles conditions for the same triangle. A triangle could satisfy both, making it isosceles in two ways (which would actually make it equilateral, but that's impossible here since P is off the line).

Actually, let me reconsider. For the pair {A, B} with A at position a, B at position b:
- PA = AB: sqrt(a²+h²) = |a-b|
- PB = AB: sqrt(b²+h²) = |a-b|

Both can't hold simultaneously unless PA = PB, which is case 1. So if PA = AB and PB = AB, then PA = PB, which means a = -b, and then |a-b| = 2|a|, and sqrt(a²+h²) = 2|a|, so a² + h² = 4a², h² = 3a². This is a special case.

OK so let me think about this problem differently. Let me think about what configuration of 100 points maximizes the count.

Let me consider the "chain" structure. Define a directed graph where we connect x → f(x) and x → g(x). If we have points at positions that form chains under f and g, we can count the isosceles triangles.

Actually, let me think about it as follows. For each unordered pair {a, b} of points on the line, the triangle PAB is isosceles iff:
- a = -b (Case 1), or
- b = f(a) or b = g(a) (Case 2: PA = AB), or
- a = f(b) or a = g(b) (Case 3: PB = AB)

But Case 2 and Case 3 overlap: b = f(a) is a specific condition, and a = g(b) is another. They're different conditions that could both hold for the same pair.

Let me think about the total count. We want to count the number of unordered pairs {a, b} that satisfy at least one of these conditions.

Let me think about the structure of f and g more carefully.

f(x) = x + sqrt(x² + h²), g(x) = x - sqrt(x² + h²).

Properties:
- f(x) > 0, g(x) < 0 for all x
- f is strictly increasing, g is strictly decreasing
- f(x) · g(x) = -h²
- f(-x) = -x + sqrt(x²+h²) = -g(x), and g(-x) = -x - sqrt(x²+h²) = -f(x)

So f(-x) = -g(x) and g(-x) = -f(x). This means f and g are related by reflection.

Now, consider the map T: x → f(x). This is a bijection from ℝ to (0, ∞). And the map S: x → g(x) is a bijection from ℝ to (-∞, 0).

For the isosceles condition PA = AB with B to the right: b = f(a). Since f maps ℝ to (0,∞), b must be positive. And a can be anything.

For PA = AB with B to the left: b = g(a). Since g maps ℝ to (-∞,0), b must be negative.

Similarly for PB = AB: a = f(b) (a positive) or a = g(b) (a negative).

So let me think about chains. Consider the sequence: x, f(x), f(f(x)), f(f(f(x))), .... If we place points at consecutive elements of such a chain, each consecutive pair gives an isosceles triangle (PA = AB type).

But we can also use g. Note that g(x) = -h²/f(x). And f and g are related.

Let me think about this differently. Let me consider the substitution x = h·sinh(t). Then:
- sqrt(x² + h²) = h·cosh(t)
- f(x) = h·sinh(t) + h·cosh(t) = h·e^t
- g(x) = h·sinh(t) - h·cosh(t) = -h·e^{-t}

So in terms of the parameter t:
- f maps x = h·sinh(t) to h·e^t
- g maps x = h·sinh(t) to -h·e^{-t}

Now let's see what f and g do in terms of the parameter. If x = h·sinh(t), then f(x) = h·e^t. To apply f again, we need to express h·e^t as h·sinh(s) for some s: sinh(s) = e^t, so s = arcsinh(e^t). Then f(f(x)) = h·e^{arcsinh(e^t)}.

This is getting complicated. Let me try a different parametrization.

Let me use x = h·sinh(t) so that sqrt(x²+h²) = h·cosh(t), and the distance from P=(0,h) to (x,0) is h·cosh(t).

Then:
- f(x) = h·e^t (position to the right where PA = AB)
- g(x) = -h·e^{-t} (position to the left where PA = AB)

Now, for a pair {a, b} with a = h·sinh(s), b = h·sinh(u):
- PA = h·cosh(s), PB = h·cosh(u), AB = h·|sinh(s) - sinh(u)|

Case 1 (PA = PB): cosh(s) = cosh(u), so s = ±u. Since a ≠ b, s = -u, meaning a = -b. ✓

Case 2 (PA = AB): h·cosh(s) = h·|sinh(s) - sinh(u)|, so cosh(s) = |sinh(s) - sinh(u)|.
If u > s: sinh(u) - sinh(s) = cosh(s), so sinh(u) = sinh(s) + cosh(s) = e^s, so u = arcsinh(e^s).
If u < s: sinh(s) - sinh(u) = cosh(s), so sinh(u) = sinh(s) - cosh(s) = -e^{-s}, so u = arcsinh(-e^{-s}) = -arcsinh(e^{-s}).

So in Case 2:
- b = f(a): u = arcsinh(e^s), i.e., sinh(u) = e^s, i.e., b = h·e^s. (Note: f(a) = h·e^s ✓)
- b = g(a): u = -arcsinh(e^{-s}), i.e., sinh(u) = -e^{-s}, i.e., b = -h·e^{-s}. (Note: g(a) = -h·e^{-s} ✓)

Case 3 (PB = AB): h·cosh(u) = h·|sinh(s) - sinh(u)|, so cosh(u) = |sinh(s) - sinh(u)|.
If s > u: sinh(s) - sinh(u) = cosh(u), so sinh(s) = sinh(u) + cosh(u) = e^u, so s = arcsinh(e^u), i.e., a = f(b).
If s < u: sinh(u) - sinh(s) = cosh(u), so sinh(s) = sinh(u) - cosh(u) = -e^{-u}, so s = -arcsinh(e^{-u}), i.e., a = g(b).

So Case 3 gives a = f(b) or a = g(b), as expected.

Now, let me think about the structure. We have the map f and g. Let me think about what happens when we compose them.

If b = f(a), meaning sinh(u) = e^s (where a = h·sinh(s), b = h·sinh(u)):
Then what is f(b)? f(b) = h·e^u where sinh(u) = e^s. So u = arcsinh(e^s) = ln(e^s + sqrt(e^{2s}+1)). So e^u = e^s + sqrt(e^{2s}+1).

And g(b) = -h·e^{-u} = -h/(e^s + sqrt(e^{2s}+1)) = -h·(sqrt(e^{2s}+1) - e^s) = -h·sqrt(e^{2s}+1) + h·e^s.

Hmm, this is getting complex. Let me try to think about the problem from a higher level.

The key question is: what is the maximum number of isosceles triangles?

Each isosceles triangle corresponds to an unordered pair {A, B} from the 100 points. There are C(100,2) = 4950 pairs total. We want to maximize how many of these are isosceles.

Let me think about the "graph" where vertices are the 100 points on the line, and edges connect pairs that form isosceles triangles with P. We want to maximize the number of edges.

The edges come from three types:
1. Symmetric pairs: {a, -a} — at most 50 such pairs.
2. f-edges: {a, f(a)} — for each point a, at most one f-edge (if f(a) is also a point).
3. g-edges: {a, g(a)} — for each point a, at most one g-edge (if g(a) is also a point).

But wait, f-edges and g-edges from Case 2, and also from Case 3. Let me be more careful.

For a pair {a, b}:
- It's a Case 2 edge if b = f(a) or b = g(a) (PA = AB)
- It's a Case 3 edge if a = f(b) or a = g(b) (PB = AB)

Now, b = f(a) is the same pair as a = g(b)? No, I showed earlier they're different. Let me re-examine.

b = f(a) means b = a + sqrt(a²+h²). This is PA = AB with B to the right.
a = g(b) means a = b - sqrt(b²+h²). This is PB = AB with A to the left of B.

For the same pair {a, b} with a < b:
- b = f(a): PA = AB, i.e., sqrt(a²+h²) = b - a
- a = g(b): PB = AB, i.e., sqrt(b²+h²) = b - a

These are different conditions. Both could hold, but that would mean sqrt(a²+h²) = sqrt(b²+h²), so a² = b², so a = -b (since a < b). Then b - a = 2b and sqrt(b²+h²) = 2b, so b² + h² = 4b², h² = 3b². Special case.

So in general, for a pair {a, b} with a < b, the possible isosceles conditions are:
- a = -b (Case 1)
- b = f(a) = a + sqrt(a²+h²) (Case 2, PA = AB)
- a = g(b) = b - sqrt(b²+h²) (Case 3, PB = AB)
- b = g(a)? No, g(a) < 0 and if a < b, then b could be negative or positive. Actually g(a) < 0 always. So b = g(a) requires b < 0, and then a > b since g is decreasing and g(a) < a... wait, g(a) = a - sqrt(a²+h²) < a always. So if b = g(a), then b < a, contradicting a < b. So for a < b, b = g(a) is impossible.
- Similarly, a = f(b) requires a > 0 and a = f(b) > b, contradicting a < b. So a = f(b) is impossible for a < b.

So for a < b, the isosceles conditions are exactly:
1. a = -b (symmetric pair)
2. b = f(a) (PA = AB)
3. a = g(b) (PB = AB)

And these are three distinct conditions (except in the special equilateral-like case).

Now, let me think about the structure. We have three types of "connections":
- Type S (symmetric): connects a and -a
- Type F: connects a to f(a) (a can be any real, f(a) > 0)
- Type G: connects b to g(b) (b can be any real, g(b) < 0), but equivalently, connects g(b) to b, i.e., for a < 0, connects a to the b such that a = g(b), i.e., b = g^{-1}(a).

Wait, let me reconsider. For a < b:
- Type F: b = f(a). Since f is increasing and f(a) > a always, this gives a < b. ✓
- Type G: a = g(b). Since g is decreasing and g(b) < b always, this gives a < b. ✓

So Type F connects a → f(a) (always to the right), and Type G connects g(b) → b (from left to right, since g(b) < b).

Now, let me think about chains. Consider starting from some point and following f repeatedly: x, f(x), f(f(x)), .... Each consecutive pair is a Type F isosceles triangle. Similarly for g.

But we can also mix. Let me think about what f and g look like in the sinh parametrization.

With x = h·sinh(t):
- f(x) = h·e^t
- g(x) = -h·e^{-t}

Let me define the "t-parameter" of a point at position x as t = arcsinh(x/h). Then:
- f sends t → arcsinh(e^t) (since f(x) = h·e^t, and the t-param of h·e^t is arcsinh(e^t/h·h) = arcsinh(e^t))

Wait, let me redo. If x = h·sinh(t), then f(x) = h·e^t. The t-parameter of f(x) is t' = arcsinh(f(x)/h) = arcsinh(e^t).

Similarly, g(x) = -h·e^{-t}, and the t-parameter is t' = arcsinh(g(x)/h) = arcsinh(-e^{-t}) = -arcsinh(e^{-t}).

So in t-space:
- F: t → arcsinh(e^t)
- G: t → -arcsinh(e^{-t})

Let me denote F(t) = arcsinh(e^t) and G(t) = -arcsinh(e^{-t}).

Note: arcsinh(u) = ln(u + sqrt(u²+1)). So:
- F(t) = ln(e^t + sqrt(e^{2t}+1))
- G(t) = -ln(e^{-t} + sqrt(e^{-2t}+1))

Let me check: F(t) = arcsinh(e^t) = ln(e^t + sqrt(e^{2t}+1)).
G(t) = -arcsinh(e^{-t}) = -ln(e^{-t} + sqrt(e^{-2t}+1)) = ln(1/(e^{-t} + sqrt(e^{-2t}+1))) = ln((sqrt(e^{-2t}+1) - e^{-t})/((e^{-2t}+1) - e^{-2t})) = ln(sqrt(e^{-2t}+1) - e^{-t}) + t.

Hmm, let me simplify. Note that arcsinh(e^{-t}) = ln(e^{-t} + sqrt(e^{-2t}+1)). And 1/(e^{-t} + sqrt(e^{-2t}+1)) = sqrt(e^{-2t}+1) - e^{-t} (rationalizing). So G(t) = -ln(e^{-t} + sqrt(e^{-2t}+1)) = ln(sqrt(e^{-2t}+1) - e^{-t}).

Also note: sqrt(e^{-2t}+1) = e^{-t}·sqrt(1+e^{2t}). So G(t) = ln(e^{-t}(sqrt(1+e^{2t}) - 1)) = -t + ln(sqrt(1+e^{2t}) - 1).

And F(t) = ln(e^t + sqrt(e^{2t}+1)) = t + ln(1 + sqrt(1+e^{-2t})).

Hmm, these are getting messy. Let me try another substitution. Let u = e^t. Then:
- F: u → e^{arcsinh(u)} = u + sqrt(u²+1)
- G: u → e^{-arcsinh(1/u)} = 1/(1/u + sqrt(1/u²+1)) = u/(1 + sqrt(1+u²)) = u(sqrt(1+u²)-1)/u² = (sqrt(1+u²)-1)/u

So in u-space (where u = e^t > 0):
- F: u → u + sqrt(u²+1)
- G: u → (sqrt(1+u²)-1)/u

Note that F(u) · G(u) = (u + sqrt(u²+1)) · (sqrt(1+u²)-1)/u = (u²+1 - 1)/u · ... wait let me compute:
(u + sqrt(u²+1)) · (sqrt(1+u²)-1)/u = [(u + sqrt(u²+1))(sqrt(u²+1)-1)]/u = [u·sqrt(u²+1) - u + u²+1 - sqrt(u²+1)]/u = [u·sqrt(u²+1) - sqrt(u²+1) + u² - u + 1]/u

Hmm, that doesn't simplify nicely. Let me try differently.

F(u) = u + sqrt(u²+1), G(u) = (sqrt(u²+1)-1)/u.

F(u) · G(u) = (u + sqrt(u²+1))(sqrt(u²+1)-1)/u = (u²+1 - u + u·sqrt(u²+1) - sqrt(u²+1))/u... 

Actually let me just compute: (u + s)(s - 1)/u where s = sqrt(u²+1).
= (us - u + s² - s)/u = (us - u + u² + 1 - s)/u = s - 1 + u + (1-s)/u = s - 1 + u - (s-1)/u.

Hmm, not clean. Let me try: F(u) = u + s, G(u) = (s-1)/u where s = sqrt(u²+1).

F(u) · G(u) = (u+s)(s-1)/u. And note that (s-1)(s+1) = s²-1 = u². So (s-1)/u = u/(s+1). Therefore G(u) = u/(s+1) = u/(sqrt(u²+1)+1).

And F(u) = u + s = u + sqrt(u²+1).

So F(u) · G(u) = (u + sqrt(u²+1)) · u/(sqrt(u²+1)+1) = u · (u + sqrt(u²+1))/(sqrt(u²+1)+1) = u · 1 = u.

Wait, that's because (u + sqrt(u²+1))/(sqrt(u²+1)+1)... hmm, u + sqrt(u²+1) ≠ sqrt(u²+1) + 1 in general.

Let me recompute. F(u) = u + sqrt(u²+1). G(u) = u/(sqrt(u²+1)+1).

F(u) · G(u) = (u + sqrt(u²+1)) · u / (sqrt(u²+1) + 1).

Let s = sqrt(u²+1). Then F(u)·G(u) = u(u+s)/(s+1). This is not simply u unless u+s = s+1, i.e., u=1.

OK this algebraic approach isn't leading anywhere clean. Let me think about the problem differently.

Let me think about the problem in terms of the original coordinates and try to find the maximum by construction.

Key insight: We want to choose 100 points on a line to maximize isosceles triangles with a fixed external point P. The three types of isosceles conditions give us three types of "edges" between points. We want to maximize the total number of edges.

Let me think about what structures allow many edges.

Type S (symmetric): {a, -a}. At most 50 edges (50 pairs of symmetric points).

Type F: {a, f(a)}. Each point a has at most one F-edge (to f(a)). So at most 100 F-edges, but each edge is counted once, so at most 100/... well, each F-edge connects a to f(a), and f is injective, so each point is the "source" of at most one F-edge and the "target" of at most one F-edge (since f is injective, f^{-1} exists). So the F-edges form a matching-like structure, but actually they can form chains: a → f(a) → f(f(a)) → .... In a chain of length k (k points), there are k-1 F-edges. But also, a point could be both a source and target: if b = f(a) and c = f(b), then a → b → c is a chain with 2 edges from 3 points.

Wait, but f is a bijection from ℝ to (0,∞). So f is injective. Each point has at most one outgoing F-edge and at most one incoming F-edge. So the F-edges form a collection of paths (chains). In a chain of k points, there are k-1 F-edges. With 100 points, if all are in one chain, we get 99 F-edges. But can all 100 points be in one F-chain?

A chain would be: a, f(a), f(f(a)), f(f(f(a))), .... For this to work, all these must be among our 100 points. Since f maps ℝ to (0,∞), after the first step, all subsequent points are positive. And f is increasing, so the chain is increasing. So we'd need 100 points in an increasing sequence where each is f of the previous. That's certainly possible (just pick any a and iterate f).

Similarly for G-edges: g is a bijection from ℝ to (-∞, 0). G-edges connect b to g(b) (i.e., g(b) → b). Each point has at most one outgoing G-edge (to g(b), which is to the left) and at most one incoming G-edge (from g^{-1}(b), which is from the right). So G-edges also form chains, going leftward.

Now, can we have both F-chains and G-chains simultaneously? A point a can have an F-edge (to f(a)) and a G-edge (to g(a)). So the F-edges and G-edges together form a graph where each point has at most degree 4 (one F-out, one F-in, one G-out, one G-in), but actually at most degree 2 in each direction.

Wait, but we need to be careful. The F-edge from a goes to f(a) (rightward), and the G-edge from a goes to g(a) (leftward). The F-edge to a comes from f^{-1}(a) (from the left, since f^{-1}(a) < a), and the G-edge to a comes from g^{-1}(a) (from the right, since g^{-1}(a) > a).

So each point has:
- F-out: to f(a) (right)
- F-in: from f^{-1}(a) (left)
- G-out: to g(a) (left)
- G-in: from g^{-1}(a) (right)

So the combined F+G graph has each point with up to 4 neighbors: f(a) and g^{-1}(a) to the right, f^{-1}(a) and g(a) to the left.

But wait, could f(a) = g^{-1}(a)? That would mean the F-out neighbor equals the G-in neighbor. Let me check: f(a) = g^{-1}(a) means g(f(a)) = a. g(f(a)) = f(a) - sqrt(f(a)²+h²). With f(a) = a + sqrt(a²+h²), this is a + sqrt(a²+h²) - sqrt((a+sqrt(a²+h²))²+h²). For this to equal a, we need sqrt(a²+h²) = sqrt((a+sqrt(a²+h²))²+h²), which means a²+h² = (a+sqrt(a²+h²))²+h², so a² = a² + 2a·sqrt(a²+h²) + a²+h², so 0 = 2a·sqrt(a²+h²) + a² + h². If a < 0, this could have solutions. 2a·sqrt(a²+h²) = -(a²+h²), so 4a²(a²+h²) = (a²+h²)², so 4a² = a²+h², so 3a² = h², so a = -h/sqrt(3) (taking a < 0). Then f(a) = -h/sqrt(3) + sqrt(h²/3+h²) = -h/sqrt(3) + 2h/sqrt(3) = h/sqrt(3). And g(f(a)) = g(h/sqrt(3)) = h/sqrt(3) - sqrt(h²/3+h²) = h/sqrt(3) - 2h/sqrt(3) = -h/sqrt(3) = a. ✓

So at the special point a = -h/sqrt(3), we have f(a) = h/sqrt(3) and g(f(a)) = a. This means the pair {a, f(a)} = {-h/sqrt(3), h/sqrt(3)} is both an F-edge and a G-edge. But it's also a symmetric pair (Type S)! So this is the special equilateral case I mentioned earlier.

OK, this is getting very complex. Let me step back and think about the problem from a competition math perspective.

The answer to this problem is likely 100·99/2 - (something) or related to a nice formula. Let me think about upper bounds and constructions.

Upper bound: Each of the 100 points can be the "apex" of isosceles triangles (where the two equal sides meet at that point) or the "base" point.

Actually, let me reconsider. In triangle PAB:
- If PA = PB, the apex is P. (Type S)
- If PA = AB, the apex is A. (Type F, with B = f(a) or g(a))
- If PB = AB, the apex is B. (Type G, with A = f(b) or g(b))

For Type S: P is the apex. Each pair {a, -a} gives one triangle. Max 50.

For Type F (apex at A): For each point A at position a, the possible B's are f(a) and g(a). So each point A is the apex of at most 2 isosceles triangles (one with B = f(a), one with B = g(a)). So at most 200 Type F triangles. But wait, each triangle {A, B} with PA = AB is counted once (with apex A). And each triangle {A, B} with PB = AB is counted once (with apex B). So the total from Types F and G is at most 200 (each of 100 points is apex of at most 2 triangles).

Wait, but a triangle could be both Type F and Type G (if PA = AB and PB = AB, which means PA = PB, so it's also Type S). So there could be double-counting. But for counting distinct triangles, we need to be careful.

Hmm, let me reconsider. For each point A at position a, A can be the apex of at most 2 isosceles triangles: {A, f(a)} and {A, g(a)} (where PA = AB). So the total number of triangles where the apex is on the line is at most 200.

Additionally, P can be the apex (Type S), giving at most 50 triangles.

But some triangles might be counted in both categories. A triangle {A, B} is Type S if a = -b, and it's Type F (apex A) if b = f(a) or b = g(a). For it to be both Type S and Type F, we need b = -a and b = f(a) (or g(a)). b = -a and b = f(a) = a + sqrt(a²+h²): -a = a + sqrt(a²+h²), so sqrt(a²+h²) = -2a, so a < 0 and a²+h² = 4a², h² = 3a², a = -h/sqrt(3). Similarly for g(a).

So the overlap is small (at most 2 triangles, corresponding to a = ±h/sqrt(3)).

So the upper bound is approximately 200 + 50 = 250, minus small overlaps.

But wait, I need to be more careful. The 200 bound comes from: each of 100 points is the apex of at most 2 triangles. But can all 100 points simultaneously be the apex of 2 triangles each? That requires f(a) and g(a) to both be among the 100 points, for every point a. This is a strong constraint.

Let me think about whether we can achieve close to 200 + 50 = 250.

Actually, let me reconsider the problem. The 200 bound might not be tight. Let me think about it as a graph problem.

We have 100 points. We want to place them to maximize the number of "isosceles pairs." The isosceles pairs come from:
- S-edges: {a, -a} (at most 50)
- F-edges: {a, f(a)} (each point has at most 1 outgoing and 1 incoming, forming chains)
- G-edges: {a, g(a)} (each point has at most 1 outgoing and 1 incoming, forming chains)

The total number of edges is |S| + |F| + |G| - |overlaps|.

Now, F-edges: since each point has at most 1 F-out and 1 F-in, the F-edges form a union of directed paths. With 100 points, the maximum number of F-edges is 99 (one long chain). But we need all 100 points to be in the chain, and the chain is a, f(a), f²(a), ..., f^{99}(a). This is possible if we choose a appropriately.

Similarly, G-edges: maximum 99, with a chain a, g(a), g²(a), ..., g^{99}(a).

But can we have both a long F-chain and a long G-chain simultaneously? The F-chain goes rightward (increasing), and the G-chain goes leftward (decreasing). A point can be in both chains. But the F-chain requires f(a_i) = a_{i+1} and the G-chain requires g(a_j) = a_{j-1}.

If a point a is in the F-chain (with successor f(a)) and in the G-chain (with predecessor g^{-1}(a) and successor g(a)), then a has F-out to f(a), G-out to g(a), F-in from f^{-1}(a), G-in from g^{-1}(a). So a has up to 4 neighbors in the combined graph.

The combined F+G graph is a directed graph where each node has out-degree ≤ 2 (F-out and G-out) and in-degree ≤ 2 (F-in and G-in). The total number of edges is at most 2·100 = 200 (from out-degree) or 2·100 = 200 (from in-degree). But since each edge contributes 1 to total out-degree and 1 to total in-degree, the total is at most 200.

But can we achieve 200? That would require every point to have both F-out and G-out, meaning f(a) and g(a) are both among the 100 points, for every point a. Is this possible?

If every point a has f(a) in the set, then the set is closed under f. If every point a has g(a) in the set, then the set is closed under g. So the set is closed under both f and g. 

Since f maps to (0,∞) and g maps to (-∞,0), and f and g are bijections, a finite set closed under both f and g would need to be... well, f sends any real to a positive number, and g sends any real to a negative number. If we start with a positive number p and apply g, we get a negative number. Apply f to that negative number, we get a positive number. Etc.

So the orbit of a point under f and g alternates between positive and negative. For a finite set closed under both f and g, we'd need the orbit to be finite, which means it must cycle. But f is strictly increasing and sends everything to positive, while g is strictly decreasing and sends everything to negative. Can we have a cycle?

A cycle would be: a → f(a) → g(f(a)) → f(g(f(a))) → ... → a. But f always increases the value (f(a) > a) and g always decreases it (g(a) < a). So f(g(f(a))) could be larger or smaller than f(a) depending on whether f "wins" or g "wins."

Actually, f(a) > a always, and g(a) < a always. So:
- f moves right
- g moves left

A cycle would require equal numbers of f-steps and g-steps (to return to start). But the composition might not return exactly.

Let me think about this differently. Can a finite set be closed under both f and g?

Consider the map T = g ∘ f (apply f first, then g). T(a) = g(f(a)) = f(a) - sqrt(f(a)²+h²). Since f(a) > 0, T(a) = f(a) - sqrt(f(a)²+h²) < 0. And T(a) = g(f(a)), and since g maps to (-∞,0), T(a) < 0.

Also, T(a) = f(a) - sqrt(f(a)²+h²) = -h²/(f(a) + sqrt(f(a)²+h²)) = -h²/(2f(a) + ...). Hmm.

Actually, recall that g(x) = -h²/f(x) (since f(x)·g(x) = -h²). Wait, is that right? f(x)·g(x) = (x+sqrt(x²+h²))(x-sqrt(x²+h²)) = x² - (x²+h²) = -h². Yes! So g(x) = -h²/f(x).

So T(a) = g(f(a)) = -h²/f(f(a)).

And f(f(a)) > f(a) > 0 (since f is increasing and f(x) > x for all x... wait, is f(x) > x? f(x) = x + sqrt(x²+h²) > x. Yes, since sqrt(x²+h²) > 0.)

So f(f(a)) > f(a) > 0, and T(a) = -h²/f(f(a)) ∈ (-h²/f(a), 0) ⊂ (-∞, 0).

Now, |T(a)| = h²/f(f(a)) < h²/f(a) = |g(a)|. So |T(a)| < |g(a)|, meaning T(a) is closer to 0 than g(a).

So the map T = g∘f sends a to a point closer to 0 (in absolute value) than g(a). If we iterate T, we get closer and closer to 0. So there's no finite cycle (except possibly 0 itself, but 0 is not in the range of f or g since f(x) > 0 and g(x) < 0).

This means a finite set cannot be closed under both f and g (unless it's empty). So we cannot achieve 200 F+G edges.

Hmm, so what's the actual maximum?

Let me reconsider. We don't need the set to be closed under f and g. We just need to maximize the number of edges. Let me think about this as follows.

Consider the combined graph (F-edges + G-edges + S-edges). Each point has:
- At most 1 F-out edge (to f(a))
- At most 1 F-in edge (from f^{-1}(a))
- At most 1 G-out edge (to g(a))
- At most 1 G-in edge (from g^{-1}(a))
- At most 1 S-edge (to -a)

The S-edge is symmetric (if {a,-a} is an S-edge, it's the same from both ends).

Total edges ≤ (100 F-out + 100 G-out + 50 S) / 1 = 250. But this overcounts because:
- An F-edge and G-edge could be the same pair (the special equilateral case)
- An F-edge or G-edge could also be an S-edge

But more importantly, the 200 F+G bound assumes every point has both F-out and G-out, which we showed is impossible for a finite set.

Let me think about this more carefully.

Let me consider the structure of the F+G graph. The F-edges form chains (rightward), and the G-edges form chains (leftward). A point can be in both an F-chain and a G-chain.

Think of it as: each point has a "right neighbor" (F-out, if f(a) is in the set) and a "left neighbor" (G-out, if g(a) is in the set). Also, each point has a "left F-neighbor" (F-in, if f^{-1}(a) is in the set) and a "right G-neighbor" (G-in, if g^{-1}(a) is in the set).

The F-out and G-in are both "rightward" edges, and F-in and G-out are both "leftward" edges. But F-out and G-in could go to different points (or the same point in the special case).

Let me think about the rightward edges from a point a: f(a) and g^{-1}(a). Are these always different?

f(a) = g^{-1}(a) iff g(f(a)) = a iff T(a) = a. We showed T(a) is closer to 0 than g(a), and T(a) < 0. For T(a) = a, we need a < 0 and |T(a)| = |a|. But |T(a)| < |g(a)| = h²/f(a). And |a| vs h²/f(a): f(a) = a + sqrt(a²+h²). For a < 0, f(a) = a + sqrt(a²+h²) < sqrt(a²+h²) (since a < 0). So h²/f(a) > h²/sqrt(a²+h²) > h²/sqrt(a²+h²). And |a| vs h²/sqrt(a²+h²): |a|·sqrt(a²+h²) vs h². If |a| is large, |a|·sqrt(a²+h²) ≈ a² > h², so |a| > h²/sqrt(a²+h²) > |T(a)|. So T(a) ≠ a for large |a|.

We already found that T(a) = a iff a = -h/sqrt(3). So f(a) = g^{-1}(a) only at a = -h/sqrt(3).

So in general, the rightward neighbors f(a) and g^{-1}(a) are different (except at one special point). Similarly, the leftward neighbors f^{-1}(a) and g(a) are different (except at a = h/sqrt(3)).

So the combined graph (F + G) is essentially a graph where each node has up to 2 rightward edges and 2 leftward edges, forming a kind of "double chain" structure.

Now, the total number of F+G edges. Let's think of it as: each point contributes its F-out and G-out edges. The total is the number of points a such that f(a) is in the set, plus the number of points a such that g(a) is in the set.

Let me denote the set of 100 points as S. The number of F-edges is |{a ∈ S : f(a) ∈ S}|, and the number of G-edges is |{a ∈ S : g(a) ∈ S}|.

We want to maximize |{a ∈ S : f(a) ∈ S}| + |{a ∈ S : g(a) ∈ S}| + |{a ∈ S : -a ∈ S, a > 0}| (the S-edges, counting each pair once).

Now, the constraint is that S is a finite set of 100 real numbers.

Let me think about the F-edges. If we order the points as x_1 < x_2 < ... < x_100, then f(x_i) > x_i, so if f(x_i) ∈ S, it must be some x_j with j > i. The F-edges form a set of "forward jumps" in the ordered sequence.

Similarly, g(x_i) < x_i, so if g(x_i) ∈ S, it must be some x_j with j < i. The G-edges form "backward jumps."

Now, the key constraint: f is a bijection ℝ → (0,∞), so f^{-1} exists. If f(x_i) = x_j, then x_j = f(x_i), and this is the unique F-edge from x_i. Also, x_i = f^{-1}(x_j), so x_i is the unique F-predecessor of x_j. So the F-edges form a partial matching between consecutive elements in F-chains.

Let me think about the maximum number of F-edges. If we have a chain x_1, x_2, ..., x_k where f(x_i) = x_{i+1}, that's k-1 F-edges from k points. The remaining 100-k points could form another chain, etc. The maximum is 99 (one chain of 100 points).

Similarly for G-edges: maximum 99.

But can we have both many F-edges and many G-edges?

Consider a point x_i. It has an F-edge to f(x_i) = x_j (j > i) and a G-edge to g(x_i) = x_k (k < i). For the F-chain, x_i's successor is x_j, and for the G-chain, x_i's successor is x_k (going leftward). 

The F-chain and G-chain are independent in the sense that the F-successor and G-successor of x_i are generally different points. So in principle, we could have a long F-chain and a long G-chain sharing the same 100 points.

But the constraint is that the points must satisfy f(x_i) = x_j AND g(x_i) = x_k for the edges to exist. The positions are determined by the f and g relationships.

Let me think about this differently. Suppose we want a set S closed under f (so every point's f-image is in S). Then S must be an F-chain: {a, f(a), f²(a), ..., f^{99}(a)}. This gives 99 F-edges. But then, how many G-edges does this set have?

For a point x in the F-chain, g(x) is generally not in the chain (since the chain is determined by f-iteration, and g is a different function). So the G-edges would be few.

Alternatively, can we find a set that has many F-edges and many G-edges simultaneously?

Let me think about the problem from the perspective of the parametrization x = h·sinh(t).

In t-space:
- F: t → arcsinh(e^t) (let's call this φ(t))
- G: t → -arcsinh(e^{-t}) (let's call this γ(t))

Note: φ(t) = arcsinh(e^t) and γ(t) = -arcsinh(e^{-t}).

Observe: γ(t) = -arcsinh(e^{-t}) = -φ(-t). So γ(t) = -φ(-t).

Also, φ(t) > 0 for all t (since e^t > 0 and arcsinh of a positive number is positive). And γ(t) < 0 for all t.

Now, φ is increasing (derivative: e^t/sqrt(e^{2t}+1) > 0). And γ is also increasing (derivative: e^{-t}/sqrt(e^{-2t}+1) > 0). Wait, let me check: γ(t) = -arcsinh(e^{-t}), dγ/dt = -(-e^{-t})/sqrt(e^{-2t}+1) = e^{-t}/sqrt(e^{-2t}+1) > 0. Yes, γ is increasing.

Also, φ(t) → ∞ as t → ∞ and φ(t) → 0 as t → -∞. γ(t) → 0 as t → ∞ and γ(t) → -∞ as t → -∞.

Now, φ(t) > t? φ(t) = arcsinh(e^t). For large t, arcsinh(e^t) ≈ t (since arcsinh(e^t) = ln(e^t + sqrt(e^{2t}+1)) ≈ ln(2e^t) = t + ln 2). So φ(t) ≈ t + ln 2 for large t. So φ(t) > t for all t.

Similarly, γ(t) < t? γ(t) = -arcsinh(e^{-t}). For large t, γ(t) ≈ -e^{-t} → 0. And t is large, so γ(t) < t. For t → -∞, γ(t) ≈ -(-t) = t... wait, arcsinh(e^{-t}) for t → -∞ is arcsinh(e^{|t|}) ≈ |t| = -t. So γ(t) ≈ -(-t) = t. More precisely, γ(t) ≈ t - ln 2 for t → -∞. So γ(t) < t for all t.

So in t-space, φ moves right (φ(t) > t) and γ also moves... γ(t) < t, so γ moves left. Wait, but I said γ is increasing. Let me re-examine.

γ(t) = -arcsinh(e^{-t}). As t increases, e^{-t} decreases, arcsinh(e^{-t}) decreases, so -arcsinh(e^{-t}) increases. So γ is increasing. And γ(t) < t (moves left in t-space). But since γ is increasing, if t_1 < t_2, then γ(t_1) < γ(t_2). So the G-edges in t-space go from t to γ(t) which is to the left, but the ordering is preserved.

Hmm, I realize the t-space doesn't directly correspond to the left-right ordering on the line, because x = h·sinh(t) is an increasing function of t, so t-space ordering = x-space ordering. So F-edges go right (φ(t) > t) and G-edges go left (γ(t) < t) in both t-space and x-space. Good.

Now, the key question: can we have a set of 100 t-values that has many φ-edges and many γ-edges?

Let me think about the composition. Consider the map ψ = γ ∘ φ (apply φ first, then γ). ψ(t) = γ(φ(t)) = -arcsinh(e^{-φ(t)}) = -arcsinh(e^{-arcsinh(e^t)}).

For large t: φ(t) ≈ t + ln 2, so e^{-φ(t)} ≈ e^{-t-2} = e^{-t}/e^2... wait, e^{-φ(t)} ≈ e^{-(t+ln 2)} = e^{-t}/2. Then arcsinh(e^{-t}/2) ≈ e^{-t}/2 for large t. So ψ(t) ≈ -e^{-t}/2 → 0 for large t.

So ψ(t) → 0 as t → ∞. And ψ(t) < 0 for all t (since γ maps to negative).

Similarly, consider ψ'(t) = φ ∘ γ (apply γ first, then φ). ψ'(t) = φ(γ(t)) = arcsinh(e^{γ(t)}) = arcsinh(e^{-arcsinh(e^{-t})}).

For t → -∞: γ(t) ≈ t - ln 2, so e^{γ(t)} ≈ e^{t-2}... wait, e^{γ(t)} ≈ e^{t - ln 2} = e^t / 2. Then arcsinh(e^t/2) ≈ e^t/2 → 0. So ψ'(t) → 0 as t → -∞.

So the compositions tend to bring values toward 0. This means iterating φ and γ alternately brings values toward 0, preventing long chains that use both.

Now I think the key insight is:

The F-edges and G-edges together form a graph that is essentially a union of paths, where each path alternates between F-edges and G-edges (or uses only one type). The total number of edges is bounded by the structure of these paths.

Let me think about it as a graph where each node has at most 2 outgoing edges (F-out and G-out) and at most 2 incoming edges (F-in and G-in). The graph is a union of paths and cycles. But we showed there are no cycles (since φ and γ both move in specific directions and their compositions tend toward 0). So the graph is a union of paths.

In a path with k nodes, there are k-1 edges. With 100 nodes, the maximum number of edges in a union of paths is 99 (one path). But wait, each node can have up to 2 outgoing edges, so the graph isn't just a simple path—it's a more general DAG.

Hmm, let me reconsider. The F-edges form chains (each node has at most 1 F-out and 1 F-in), and the G-edges form chains (each node has at most 1 G-out and 1 G-in). Together, a node can have F-out, F-in, G-out, G-in—up to 4 edges. So the combined graph can have up to 200 edges (100 F-edges + 100 G-edges) if every node has both F-out and G-out.

But we showed that a finite set can't be closed under both f and g. So we can't have 100 F-edges and 100 G-edges simultaneously. The question is: what's the maximum of (F-edges + G-edges)?

Let me think about this more carefully. Consider the "rightward" edges from each node: F-out (to f(a)) and G-in (from g^{-1}(a), but this is an incoming edge, not outgoing). Wait, I need to be more careful about direction.

Let me re-define. An F-edge from a to b means b = f(a) (a < b, PA = AB). A G-edge from a to b means b = g(a) (a > b, but wait, g(a) < a, so this goes left). Hmm, but in terms of the triangle, a G-edge from a to b = g(a) means PA = AB where A is at position a and B is at position g(a) < a. So the "apex" is A (at position a).

Actually, I think I should think about it differently. Let me count edges, not worrying about direction.

Each unordered pair {a, b} with a < b can be:
- An S-edge if a = -b
- An F-edge if b = f(a) (equivalently, a = f^{-1}(b))
- A G-edge if a = g(b) (equivalently, b = g^{-1}(a))

And these are generally distinct (except at special points).

Now, the F-edges: each point is the left endpoint of at most 1 F-edge (to f(a)) and the right endpoint of at most 1 F-edge (from f^{-1}(a)). So F-edges form a matching in the "left-to-right" sense—actually a union of chains.

Similarly, G-edges: each point is the right endpoint of at most 1 G-edge (to g(a), which is to the left) and the left endpoint of at most 1 G-edge (from g^{-1}(a), which is to the right). So G-edges also form chains.

Now, the combined F+G graph: each point has at most 1 F-edge going right, 1 F-edge going left (from the chain), 1 G-edge going left, 1 G-edge going right (from the G-chain). So at most 2 edges going right (F-out and G-in) and 2 going left (F-in and G-out). But F-out and G-in are different edges (going to different points, in general).

The total number of F+G edges = (number of F-edges) + (number of G-edges). Each is at most 99. But can both be close to 99?

Let me think about a specific construction. Suppose we use the t-parametrization and try to find a set that's a long chain under φ (F-edges) and also has many γ-edges (G-edges).

If the set is {t_0, φ(t_0), φ²(t_0), ..., φ^{99}(t_0)}, then all 99 F-edges exist. For G-edges, we need γ(t_i) to also be in the set for many i. But γ(t_i) is generally not of the form φ^j(t_0), so G-edges would be rare.

Alternatively, can we find a set that's a chain under both φ and γ? That would require φ(t_i) = t_{i+1} and γ(t_i) = t_{i-1} for all i. This means t_{i+1} = φ(t_i) and t_{i-1} = γ(t_i), so t_{i+1} = φ(t_i) and t_i = φ(t_{i-1}) (from the first relation shifted), and also t_{i-1} = γ(t_i) (from the second). So we need γ(t_i) = t_{i-1} and φ(t_{i-1}) = t_i, i.e., φ(γ(t_i)) = t_i. So we need φ ∘ γ = identity, i.e., φ(γ(t)) = t for all t in the chain.

But φ(γ(t)) = arcsinh(e^{γ(t)}) = arcsinh(e^{-arcsinh(e^{-t})}). For this to equal t, we need e^{-arcsinh(e^{-t})} = sinh(t), i.e., -arcsinh(e^{-t}) = ln(sinh(t) + sqrt(sinh²(t)+1)) = arcsinh(sinh(t)) = t (for t > 0). So we need -arcsinh(e^{-t}) = t, i.e., arcsinh(e^{-t}) = -t, i.e., e^{-t} = sinh(-t) = -sinh(t). But e^{-t} > 0 and -sinh(t) < 0 for t > 0. Contradiction. So φ ∘ γ ≠ identity.

So we can't have a set that's simultaneously a chain under both φ and γ. The F-chains and G-chains are incompatible.

This means there's a tradeoff: more F-edges means fewer G-edges and vice versa. The question is: what's the maximum of F + G?

Let me think about this differently. Consider the "doubly-linked" structure. If a point a has both F-out (to f(a)) and G-out (to g(a)), then a is an "internal" node of both an F-chain and a G-chain. The F-chain goes right from a, and the G-chain goes left from a.

Now, consider the "zigzag" path: start at some point, go right via F, then left via G, then right via F, etc. This is the path a, f(a), g(f(a)), f(g(f(a))), .... We showed this tends toward 0, so it can't be a long path in a finite set.

Alternatively, start at some point, go left via G, then right via F, etc.: a, g(a), f(g(a)), g(f(g(a))), .... This also tends toward 0 (from the other side).

So the "zigzag" paths are short. The long paths must be "straight" (all F or all G).

This suggests that the maximum F + G is achieved by having one long F-chain (99 edges) and no G-edges, or one long G-chain (99 edges) and no F-edges, or some compromise.

But wait, maybe we can do better by having some F-edges and some G-edges that don't interfere. For example, if the F-chain uses points in one region and the G-chain uses points in another region.

Let me think about it. Suppose we split the 100 points into two groups: 50 points forming an F-chain (49 F-edges) and 50 points forming a G-chain (49 G-edges). Total: 98 edges. That's less than 99.

But maybe we can do better by interleaving. Consider a set where some points have F-edges and other points have G-edges, and the two types don't conflict.

Actually, let me reconsider. The F-edges and G-edges don't conflict in the sense that they're different pairs. The issue is whether the set of points can simultaneously support many F-edges and many G-edges.

A point a supports an F-edge if f(a) is in the set. A point a supports a G-edge if g(a) is in the set. These are independent conditions on the set. The question is: can we choose a set of 100 points such that many points have f(a) in the set AND many points have g(a) in the set?

The answer depends on the structure of f and g. Since f maps to (0,∞) and g maps to (-∞,0), the F-edges connect points across the positive/negative divide (or within the positive side), and G-edges similarly.

Hmm, let me think about a specific example. Let h = 1 for simplicity.

f(x) = x + sqrt(x²+1), g(x) = x - sqrt(x²+1) = -1/f(x).

Let's compute some values:
- f(0) = 1, g(0) = -1
- f(1) = 1 + sqrt(2) ≈ 2.414, g(1) = 1 - sqrt(2) ≈ -0.414
- f(-1) = -1 + sqrt(2) ≈ 0.414, g(-1) = -1 - sqrt(2) ≈ -2.414
- f(0.414) ≈ 0.414 + sqrt(0.171+1) = 0.414 + 1.082 = 1.496
- g(0.414) ≈ 0.414 - 1.082 = -0.668

Let me try to build a set with many edges. Start with 0:
- f(0) = 1, g(0) = -1. So {0, 1, -1} has F-edge {0,1} and G-edge {0,-1} and S-edge {-1,1}. That's 3 edges from 3 points.

Now add f(1) = 1+sqrt(2) ≈ 2.414 and g(-1) = -1-sqrt(2) ≈ -2.414:
- F-edge {1, 2.414}, G-edge {-1, -2.414}, S-edge {-2.414, 2.414}.
- Set: {-2.414, -1, 0, 1, 2.414}. Edges: F: {0,1}, {1,2.414}; G: {0,-1}, {-1,-2.414}; S: {-1,1}, {-2.414,2.414}. Total: 6 edges from 5 points.

Continue: f(2.414) = 2.414 + sqrt(5.827+1) = 2.414 + 2.613 = 5.027. g(-2.414) = -2.414 - 2.613 = -5.027.
- F-edge {2.414, 5.027}, G-edge {-2.414, -5.027}, S-edge {-5.027, 5.027}.
- Set: {-5.027, -2.414, -1, 0, 1, 2.414, 5.027}. Edges: F: {0,1}, {1,2.414}, {2.414,5.027}; G: {0,-1}, {-1,-2.414}, {-2.414,-5.027}; S: {-1,1}, {-2.414,2.414}, {-5.027,5.027}. Total: 9 edges from 7 points.

I see a pattern! The set is symmetric about 0: {-a_n, ..., -a_1, 0, a_1, ..., a_n} where a_{i+1} = f(a_i). With 2n+1 points, we get:
- F-edges: {a_i, a_{i+1}} for i = 0, 1, ..., n-1 (where a_0 = 0). That's n F-edges.
- G-edges: {-a_i, -a_{i+1}} for i = 0, 1, ..., n-1. That's n G-edges. (Since g(-a_i) = -f(a_i) = -a_{i+1}.)
- S-edges: {-a_i, a_i} for i = 1, ..., n. That's n S-edges.
- Total: 3n edges from 2n+1 points.

With 100 points, we can't quite get 2n+1 = 100 (since 100 is even). Let me adjust.

If we use 2n+1 points (symmetric set with 0), we get 3n edges. For 100 points, we could use 99 points in this symmetric arrangement (n = 49, giving 147 edges) and 1 extra point somewhere. Or we could use 100 points in a different arrangement.

Wait, but with 100 points, if we use a symmetric set of 100 points (50 positive, 50 negative, no zero), we get:
- F-edges: {a_i, a_{i+1}} for i = 1, ..., 49 (if a_1, ..., a_50 are the positive points with a_{i+1} = f(a_i)). That's 49 F-edges. But wait, we also need f(a_0) = a_1 where a_0 = 0, but 0 is not in the set. So the F-edge from 0 doesn't exist. We only get F-edges among the positive points: {a_i, a_{i+1}} for i = 1, ..., 49, giving 49 F-edges. But actually, f(a_i) = a_{i+1} requires a_{i+1} = f(a_i), and this chain starts from a_1. So we need a_2 = f(a_1), a_3 = f(a_2), etc. That gives 49 F-edges.
- G-edges: similarly, {-a_i, -a_{i+1}} for i = 1, ..., 49, giving 49 G-edges.
- S-edges: {-a_i, a_i} for i = 1, ..., 50, giving 50 S-edges.
- Total: 49 + 49 + 50 = 148 edges.

But wait, can we do better? What if we include 0 and use 99 points symmetrically (n=49, 2n+1=99) plus 1 extra point?

With 99 points: 3·49 = 147 edges. The extra point could add a few more edges. But where to place it?

If we place the extra point at some position x, it could form:
- An F-edge if f(x) is in the set or f^{-1}(x) is in the set.
- A G-edge if g(x) is in the set or g^{-1}(x) is in the set.
- An S-edge if -x is in the set.

If we place x = a_{50} = f(a_{49}) (continuing the F-chain), then:
- F-edge {a_{49}, a_{50}}: +1
- S-edge {-a_{50}, a_{50}}: +1 (if -a_{50} is in the set, but it's not since we only had up to ±a_{49})

Hmm, so the extra point at a_{50} gives F-edge {a_{49}, a_{50}} (+1) but no S-edge (since -a_{50} is not in the set). And G-edge? g(a_{50}) is some negative number, probably not in the set. So +1 edge, total 148.

Alternatively, place x = -a_{50} (symmetric to the above). Then G-edge {-a_{49}, -a_{50}} (+1) and S-edge {a_{50}, -a_{50}}? No, a_{50} is not in the set. So +1 edge, total 148.

What if we place both a_{50} and -a_{50} and remove 0? Then we have 100 points: ±a_1, ..., ±a_{50}. 
- F-edges: {a_i, a_{i+1}} for i=1,...,49: 49 edges.
- G-edges: {-a_i, -a_{i+1}} for i=1,...,49: 49 edges.
- S-edges: {-a_i, a_i} for i=1,...,50: 50 edges.
- Total: 148 edges.

Same as before. Can we do better?

What if we don't use a symmetric set? Let me think about other constructions.

Actually, wait. In the symmetric construction, we're using the fact that g(-a) = -f(a) (which follows from g(-x) = -f(x)). This means the G-chain on the negative side mirrors the F-chain on the positive side. So we get equal numbers of F and G edges, plus S-edges.

But what if we use an asymmetric construction that gets more total edges?

Let me think about the upper bound more carefully.

Each point can be the apex of at most 2 isosceles triangles (PA = AB with B = f(a), and PA = AB with B = g(a)). Wait, but a point can also be part of triangles where it's not the apex. Let me re-examine.

A triangle {P, A, B} is isosceles if:
1. PA = PB (apex P): A and B are symmetric. Each point A is in at most 1 such triangle (paired with -A).
2. PA = AB (apex A): B = f(A) or B = g(A). Each point A is the apex of at most 2 such triangles.
3. PB = AB (apex B): A = f(B) or A = g(B). Each point B is the apex of at most 2 such triangles.

Now, each isosceles triangle has exactly one apex (the vertex where the two equal sides meet), unless it's equilateral (all three sides equal), which is impossible here since P is off the line.

Wait, actually an isosceles triangle has exactly one apex unless it's equilateral. Since equilateral is impossible (P is off the line, so PA = PB = AB would require A and B on the line with PA = PB = AB, but PA = sqrt(a²+h²) and AB = |a-b|, and for PA = PB we need a = -b, then AB = 2|a| and PA = sqrt(a²+h²) = 2|a| requires h² = 3a², which is possible for specific a but not for all). So for most triangles, there's a unique apex.

But some triangles could be isosceles in two different ways (two pairs of equal sides), which would make them equilateral. As noted, this requires h² = 3a², which happens for at most 2 values of a (namely a = ±h/sqrt(3)). So at most 2 triangles are equilateral, and the rest have a unique apex.

For triangles with a unique apex:
- Apex P: at most 50 (one for each symmetric pair).
- Apex on the line (A or B): each of the 100 points is the apex of at most 2 triangles, so at most 200.

But the 200 bound counts each triangle once (by its apex). And the 50 bound counts triangles with apex P. These are disjoint (a triangle can't have two apexes unless equilateral). So the total is at most 50 + 200 = 250, minus the number of equilateral triangles (which are counted twice, once for each apex on the line, and also as apex P).

Wait, I need to be more careful. An equilateral triangle has all three sides equal, so all three vertices are "apexes." But we're counting it as one triangle. In the apex counting:
- It's counted once as apex P (PA = PB).
- It's counted once as apex A (PA = AB).
- It's counted once as apex B (PB = AB).
So it's counted 3 times in the 50 + 200 bound, but should be counted once. So we need to subtract 2 for each equilateral triangle.

But there are at most 2 equilateral triangles (for a = ±h/sqrt(3), with b = ∓h/sqrt(3)). Actually, for a = h/sqrt(3), b = -h/sqrt(3): PA = sqrt(h²/3 + h²) = 2h/sqrt(3), PB = 2h/sqrt(3), AB = 2h/sqrt(3). Yes, equilateral. And for a = -h/sqrt(3), b = h/sqrt(3): same triangle. So there's only 1 equilateral triangle (the pair {h/sqrt(3), -h/sqrt(3)}).

So the upper bound is 50 + 200 - 2 = 248, if there's 1 equilateral triangle. But if the set doesn't include ±h/sqrt(3), there are 0 equilateral triangles, and the bound is 250.

But wait, the 200 bound assumes every point is the apex of 2 triangles, which requires f(a) and g(a) to both be in the set for every a. We showed this is impossible for a finite set. So the actual bound is less than 250.

Let me reconsider. The 200 bound is: each of 100 points is the apex of at most 2 triangles (with equal sides PA = AB). But for a point a to be the apex of 2 triangles, both f(a) and g(a) must be in the set. For a point a to be the apex of 1 triangle, at least one of f(a), g(a) must be in the set.

Let me define:
- n_F = number of points a with f(a) in the set (F-out edges)
- n_G = number of points a with g(a) in the set (G-out edges)
- n_S = number of S-edges = number of pairs {a, -a} with both in the set and a > 0

The total number of isosceles triangles (with apex on the line) = n_F + n_G (each F-out or G-out edge gives one triangle with the apex at the source point). Plus n_S triangles with apex P.

But we need to subtract overlaps: a triangle that is both Type S and Type F/G (the equilateral case). There's at most 1 such triangle.

Also, a triangle could be both Type F and Type G? That would mean PA = AB and PB = AB, so PA = PB, which is Type S. So Type F and Type G overlap only in the equilateral case. So no additional overlaps.

Total = n_F + n_G + n_S - (equilateral overlaps).

Now, n_F ≤ 99 (F-edges form chains, max 99 in one chain of 100).
n_G ≤ 99 (similarly).
n_S ≤ 50.

But n_F + n_G can't be 198 because of the incompatibility of F and G.

Let me think about the maximum of n_F + n_G.

Consider the F-edges and G-edges as a directed graph. Each node has out-degree ≤ 2 (F-out and G-out) and in-degree ≤ 2 (F-in and G-in). The total number of edges is n_F + n_G.

Now, the F-edges form a union of chains (each node has at most 1 F-out and 1 F-in). Similarly for G-edges. The combined graph has each node with out-degree ≤ 2 and in-degree ≤ 2.

The maximum number of edges in a DAG with 100 nodes and max degree 4 is... well, it's at most 200 (from the degree bound). But the specific structure of f and g prevents achieving this.

Let me think about the constraint more carefully. The F-out edge from a goes to f(a), and the G-out edge from a goes to g(a). Now, f(a) > 0 and g(a) < 0. So:
- If a > 0: f(a) > a (F-out goes further right), g(a) < 0 (G-out jumps to negative side).
- If a < 0: f(a) > 0 (F-out jumps to positive side), g(a) < a (G-out goes further left).
- If a = 0: f(0) = h, g(0) = -h.

So for positive points, F-out stays positive and G-out goes negative. For negative points, F-out goes positive and G-out stays negative.

This means:
- F-edges from positive points go to positive points (staying on the positive side).
- F-edges from negative points go to positive points (crossing to the positive side).
- G-edges from positive points go to negative points (crossing to the negative side).
- G-edges from negative points go to negative points (staying on the negative side).

So the F-edges on the positive side form chains among positive points, and F-edges from negative points jump to the positive side. Similarly, G-edges on the negative side form chains among negative points, and G-edges from positive points jump to the negative side.

Now, consider the positive points. Among k positive points, the F-edges form chains (each positive point has at most 1 F-out to another positive point, and at most 1 F-in from another positive point or from a negative point). The G-edges from positive points go to negative points, so they don't contribute to edges among positive points.

Similarly, among the negative points, G-edges form chains, and F-edges from negative points go to positive points.

Let me denote:
- p = number of positive points
- q = number of negative points
- z = number of zeros (0 or 1)
- p + q + z = 100

F-edges:
- Among positive points: at most p - 1 (if they form one chain). But actually, the F-edges among positive points form chains, and the max is p - 1 (one chain) plus possibly F-edges from negative points to positive points.
- From negative points to positive points: at most q (each negative point has at most 1 F-out, going to a positive point). But the target must be in the set.
- From zero to positive: at most 1 (if 0 is in the set, f(0) = h must be in the set).

Wait, I need to think about this more carefully. The F-edges form chains. A chain can start from a negative point (F-out goes to positive), then continue among positive points (F-out stays positive). So a single F-chain can include both negative and positive points.

Let me think about the F-chains. An F-chain is a sequence a_1, a_2, ..., a_k where f(a_i) = a_{i+1}. Since f maps everything to positive, a_2, a_3, ..., a_k are all positive. a_1 can be anything (positive, negative, or zero). So each F-chain has at most 1 non-positive point (the first one) and the rest are positive.

If we have p positive points and q negative points and z zeros, the F-chains can include at most q + z non-positive starting points and p positive points. Each chain has at most 1 non-positive point. So we can have at most q + z chains, each using 1 non-positive point and some positive points. The total number of positive points used is at most p, and the total F-edges is (total points in chains) - (number of chains) = (p + q + z used) - (number of chains).

Hmm, this is getting complicated. Let me think about it differently.

The F-edges form a forest of directed paths. Each path has at most 1 non-positive node (the first node). The remaining nodes are positive. So the number of paths is at most q + z (the number of non-positive nodes), and the total nodes in all paths is at most 100. The total F-edges = total nodes - number of paths ≤ 100 - 1 = 99 (if there's only 1 path, starting from 1 non-positive node).

But if we have many non-positive nodes, each must start its own path, so the number of paths is at least the number of non-positive nodes that have F-edges. If all q + z non-positive nodes have F-edges, we have at least q + z paths, and the total F-edges ≤ 100 - (q + z).

Similarly, G-edges form paths, each with at most 1 non-negative node (the first one, since g maps to negative). The number of G-paths is at most p + z, and total G-edges ≤ 100 - (p + z) = q.

Wait, let me re-examine. G-edges: g maps everything to negative. So a G-chain a_1, a_2, ..., a_k with g(a_i) = a_{i+1} has a_2, ..., a_k all negative. a_1 can be anything. So each G-chain has at most 1 non-negative node.

If we have p positive nodes and z zeros, the number of G-chains is at most p + z (each starting from a non-negative node). Total G-edges ≤ 100 - (number of G-chains) ≥ ... well, to maximize G-edges, minimize the number of chains, which is 1 (if only 1 non-negative node has a G-edge). But if all p + z non-negative nodes have G-edges, we have p + z chains, and G-edges ≤ 100 - (p + z) = q.

Hmm wait, that's not right either. The G-chains use nodes from the set. If a G-chain starts from a positive node and goes to negative nodes, it uses 1 positive node and some negative nodes. The total nodes used across all G-chains is at most 100. The number of chains is the number of non-negative nodes that have G-out edges. If all p + z non-negative nodes have G-out edges, there are p + z chains, using at most 100 nodes total, so G-edges = 100 - (p + z) = q. But this requires all q negative nodes to be in G-chains, and each chain uses 1 non-negative node and some negative nodes.

Actually, I think the constraint is:
- F-edges: at most 100 - (number of F-chains). Number of F-chains ≥ (number of non-positive nodes with F-out edges). To maximize F-edges, minimize chains. If no non-positive node has an F-out edge, all F-chains are among positive nodes, and the number of chains is (number of positive nodes) - (F-edges among positive nodes). Hmm, this is circular.

Let me think about it more simply.

F-edges: The F-edges form a union of directed paths. In a union of directed paths with n nodes and c connected components (paths), the number of edges is n - c. To maximize edges, minimize c. The minimum c is 1 (one path), giving n - 1 = 99 edges. But the path must be a valid F-chain: a, f(a), f²(a), ..., f^{99}(a). This is always possible (just pick any a and iterate f 99 times). So n_F ≤ 99.

Similarly, n_G ≤ 99.

But can n_F + n_G be large? The constraint is that the F-edges and G-edges share the same set of 100 points.

Let me think about the tradeoff. Suppose we have n_F F-edges. These use some of the 100 points in F-chains. The remaining points (not in any F-chain, or in F-chains but with available G-edges) can have G-edges.

Actually, every point is potentially in both an F-chain and a G-chain. The F-chain and G-chain are independent. A point a can have F-out to f(a) and G-out to g(a), and these are different points (in general). So the F-edges and G-edges are independent edge sets on the same vertex set.

The question is: for a given set of 100 points, what is n_F + n_G?

n_F = |{a ∈ S : f(a) ∈ S}|, n_G = |{a ∈ S : g(a) ∈ S}|.

We want to choose S (|S| = 100) to maximize n_F + n_G + n_S.

Let me think about the symmetric construction again. S = {±a_1, ±a_2, ..., ±a_50} where a_{i+1} = f(a_i) for i = 1, ..., 49.

n_F: For positive points a_i, f(a_i) = a_{i+1} ∈ S for i = 1, ..., 49. That's 49. For negative points -a_i, f(-a_i) = -g(a_i) = -(-a_{i+1}) = a_{i+1}... wait, let me recompute. f(-a_i) = -a_i + sqrt(a_i² + h²). And g(a_i) = a_i - sqrt(a_i² + h²) = -a_{i+1}... no. g(a_i) = a_i - sqrt(a_i² + h²). And a_{i+1} = f(a_i) = a_i + sqrt(a_i² + h²). So sqrt(a_i² + h²) = a_{i+1} - a_i. Then g(a_i) = a_i - (a_{i+1} - a_i) = 2a_i - a_{i+1}. Hmm, that doesn't simplify to -a_{i+1} in general.

Wait, I think I made an error earlier. Let me recompute. g(-x) = -x - sqrt(x² + h²) = -(x + sqrt(x² + h²)) = -f(x). So g(-a_i) = -f(a_i) = -a_{i+1}. So the G-edge from -a_i goes to -a_{i+1}. ✓

And f(-a_i) = -a_i + sqrt(a_i² + h²) = -a_i + (a_{i+1} - a_i) = a_{i+1} - 2a_i. This is not necessarily in S.

So for the symmetric set S = {±a_1, ..., ±a_50}:
- F-edges from positive points: f(a_i) = a_{i+1} for i = 1, ..., 49. That's 49 F-edges.
- F-edges from negative points: f(-a_i) = a_{i+1} - 2a_i. This is generally not in S. So 0 F-edges from negative points (unless a_{i+1} - 2a_i happens to equal some a_j or -a_j, which is unlikely in general).

Wait, but f(-a_i) = -g(a_i) (since f(-x) = -g(x)). And g(a_i) = a_i - sqrt(a_i² + h²). If a_{i+1} = f(a_i) = a_i + sqrt(a_i² + h²), then sqrt(a_i² + h²) = a_{i+1} - a_i, so g(a_i) = a_i - (a_{i+1} - a_i) = 2a_i - a_{i+1}. And f(-a_i) = -g(a_i) = a_{i+1} - 2a_i.

For f(-a_i) to be in S, we need a_{i+1} - 2a_i ∈ {±a_1, ..., ±a_50}. In general, this won't hold.

So n_F = 49 (only from positive points) in the symmetric construction.

Similarly, n_G: G-edges from negative points: g(-a_i) = -a_{i+1} for i = 1, ..., 49. That's 49 G-edges. G-edges from positive points: g(a_i) = 2a_i - a_{i+1}, generally not in S. So n_G = 49.

n_S = 50 (pairs {a_i, -a_i} for i = 1, ..., 50).

Total: 49 + 49 + 50 = 148.

Can we do better? Let me think about including 0 in the set.

S = {0, ±a_1, ..., ±a_49} (99 points) plus one more point. With 0:
- f(0) = h. If h = a_1, then F-edge {0, a_1}. Similarly g(0) = -h = -a_1, G-edge {0, -a_1}.
- F-edges from positive: {a_i, a_{i+1}} for i = 1, ..., 48. 48 edges. Plus {0, a_1}: 49 F-edges.
- G-edges from negative: {-a_i, -a_{i+1}} for i = 1, ..., 48. 48 edges. Plus {0, -a_1}: 49 G-edges.
- S-edges: {a_i, -a_i} for i = 1, ..., 49. 49 edges. (0 is not paired with anything.)
- Total: 49 + 49 + 49 = 147 from 99 points.

With the 100th point, we can add at most a few edges. If we add a_50 = f(a_49):
- F-edge {a_49, a_50}: +1.
- S-edge {-a_50, a_50}? -a_50 is not in S. So no.
- G-edge from a_50? g(a_50) probably not in S.
- Total: 147 + 1 = 148.

If instead we add -a_50 = g(-a_49):
- G-edge {-a_49, -a_50}: +1.
- Total: 147 + 1 = 148.

If we add both a_50 and -a_50 and remove 0: S = {±a_1, ..., ±a_50}, 100 points.
- F-edges: {a_i, a_{i+1}} for i=1,...,49: 49.
- G-edges: {-a_i, -a_{i+1}} for i=1,...,49: 49.
- S-edges: 50.
- Total: 148.

So the symmetric construction gives 148. Can we beat this?

Let me think about asymmetric constructions. What if we don't require symmetry?

Consider a set that's a single long F-chain: {a, f(a), f²(a), ..., f^{99}(a)}. This gives 99 F-edges. G-edges: for each point in the chain, g(point) is generally not in the chain. So n_G ≈ 0. S-edges: if the chain happens to contain symmetric pairs, but generally it won't. So total ≈ 99.

That's much worse than 148.

What about a mixed construction? Let me think about what happens if we have p positive points forming an F-chain and q negative points forming a G-chain, with p + q = 100.

F-edges: p - 1 (from the F-chain among positive points) + possibly some F-edges from negative points to positive points.
G-edges: q - 1 (from the G-chain among negative points) + possibly some G-edges from positive points to negative points.
S-edges: however many symmetric pairs exist.

If the positive and negative points are not related by symmetry, S-edges = 0. Total: (p-1) + (q-1) = 98. Worse than 148.

If we add symmetry: positive points are a_1, ..., a_p and negative points are -a_1, ..., -a_q with p = q = 50. Then:
- F-edges: 49 (among positive) + F-edges from negative points.
- G-edges: 49 (among negative) + G-edges from positive points.
- S-edges: 50 (if p = q = 50 and the sets are symmetric).
- F-edges from negative: f(-a_i) = -g(a_i). For this to be in S (i.e., in {a_1, ..., a_50} or {-a_1, ..., -a_50}), we need -g(a_i) = a_j or -g(a_i) = -a_j. Since -g(a_i) > 0 (because g(a_i) < 0), we need -g(a_i) = a_j, i.e., g(a_i) = -a_j. But g(a_i) = 2a_i - a_{i+1} (where a_{i+1} = f(a_i)). So 2a_i - a_{i+1} = -a_j, i.e., a_{i+1} = 2a_i + a_j. This is a specific condition that might hold for some i, j but not in general.

So in the symmetric construction, we get 49 + 49 + 50 = 148, and possibly a few more from cross-edges (F from negative, G from positive) if the positions align.

Can we choose the positions to make some cross-edges work? Let me think.

We want g(a_i) = -a_j for some i, j, i.e., 2a_i - a_{i+1} = -a_j, i.e., a_{i+1} = 2a_i + a_j. Since a_{i+1} = f(a_i) is determined by a_i (and h), this is a constraint on the a values.

Actually, the a values are determined by the F-chain: a_{i+1} = f(a_i). So a_1 is free, and a_2 = f(a_1), a_3 = f(a_2), etc. The condition a_{i+1} = 2a_i + a_j becomes f(a_i) = 2a_i + a_j, i.e., a_i + sqrt(a_i² + h²) = 2a_i + a_j, i.e., sqrt(a_i² + h²) = a_i + a_j, i.e., a_i² + h² = a_i² + 2a_i·a_j + a_j², i.e., h² = 2a_i·a_j + a_j², i.e., a_j² + 2a_i·a_j - h² = 0, i.e., a_j = (-2a_i ± sqrt(4a_i² + 4h²))/2 = -a_i ± sqrt(a_i² + h²) = -a_i ± (a_{i+1} - a_i).

So a_j = -a_i + (a_{i+1} - a_i) = a_{i+1} - 2a_i, or a_j = -a_i - (a_{i+1} - a_i) = -a_{i+1}.

The second solution: a_j = -a_{i+1}. But a_j > 0 and a_{i+1} > 0, so a_j = -a_{i+1} < 0. Contradiction. So only the first solution: a_j = a_{i+1} - 2a_i.

For this to be a valid positive point in our set, we need a_j = a_{i+1} - 2a_i > 0, i.e., a_{i+1} > 2a_i, i.e., f(a_i) > 2a_i, i.e., a_i + sqrt(a_i² + h²) > 2a_i, i.e., sqrt(a_i² + h²) > a_i, which is always true. So a_j = a_{i+1} - 2a_i > 0 always. But we need a_j to be one of our existing points a_1, ..., a_50.

So the cross-edge condition is: a_{i+1} - 2a_i = a_j for some j. This means g(a_i) = -(a_{i+1} - 2a_i) = -a_j, so the G-edge from a_i goes to -a_j, which is in our set. This gives an additional G-edge.

But a_j = a_{i+1} - 2a_i is a specific value determined by a_i and a_{i+1}. For it to be in our set, it must equal one of the a_k values. Since the a_k values are determined by the F-chain (a_{k+1} = f(a_k)), this is a constraint on a_1 (the starting point of the chain).

This seems hard to satisfy for many i values simultaneously. Let me think about whether we can choose a_1 to satisfy multiple such conditions.

Actually, let me think about this problem from a higher level. The answer 148 from the symmetric construction seems good, but maybe there's a better construction.

Let me reconsider the upper bound. We have:
- n_F + n_G + n_S - (overlaps) ≤ n_F + n_G + n_S

And n_F + n_G ≤ ? (the key constraint).

Let me think about n_F + n_G differently. Each point a contributes 1 to n_F if f(a) ∈ S, and 1 to n_G if g(a) ∈ S. So n_F + n_G = |{a ∈ S : f(a) ∈ S}| + |{a ∈ S : g(a) ∈ S}|.

Now, f(a) ∈ S means a is the "predecessor" in an F-chain. g(a) ∈ S means a is the "predecessor" in a G-chain. 

Consider the map F: S → S defined by F(a) = f(a) if f(a) ∈ S, undefined otherwise. This is a partial function. Similarly G(a) = g(a) if g(a) ∈ S.

The number of F-edges is the number of points where F is defined, and similarly for G.

Now, consider the "rightward" edges from each point. A point a has:
- F(a) = f(a) if f(a) ∈ S (rightward, since f(a) > a)
- G^{-1}(a) = g^{-1}(a) if g^{-1}(a) ∈ S (rightward, since g^{-1}(a) > a)

These are two different rightward edges (to different points, in general). Similarly, two leftward edges.

The total number of rightward edges = n_F + (number of points with G-in edges). The number of G-in edges equals n_G (since each G-edge has one source and one target, so the number of G-in edges = number of G-out edges = n_G). So total rightward edges = n_F + n_G.

Similarly, total leftward edges = n_F + n_G (by symmetry of counting).

Now, the rightward edges go from each point to a point further right. Consider the points ordered x_1 < x_2 < ... < x_100. A rightward edge from x_i goes to x_j with j > i. Each point x_i has at most 2 rightward edges (F-out and G-in). So the total number of rightward edges is at most 2 · 100 = 200, but also at most the number of pairs (i, j) with i < j, which is C(100, 2) = 4950. The binding constraint is 200.

But we also have the constraint that F-out and G-in from the same point go to different points (in general). So the 2 rightward edges from each point go to 2 different points. This means the rightward edges form a graph where each node has out-degree ≤ 2 and in-degree ≤ 2 (since each point can be the target of at most 1 F-edge and at most 1 G-edge). This is a union of paths and cycles in a directed graph with max degree 4.

But we showed there are no cycles. So it's a union of paths. With 100 nodes, the maximum number of edges in a union of paths is 99 (one path). But with max out-degree 2 and max in-degree 2, we can have a "thicker" structure.

Wait, a directed graph with max out-degree 2 and max in-degree 2, and no cycles, can have up to 2 · 100 - 2 = 198 edges? No, that's not right. In a DAG with n nodes, the maximum number of edges is n(n-1)/2 (complete DAG). But with max degree constraints, it's different.

Actually, in a directed graph with max out-degree d_out and max in-degree d_in, the maximum number of edges is min(n · d_out, n · d_in). Here, d_out = d_in = 2, so max edges = 200. But we also need the graph to be a DAG (no cycles), which is automatically satisfied since all edges go rightward.

So the maximum number of rightward edges is 200, achieved when every point has 2 rightward edges (F-out and G-in) and 2 leftward edges (F-in and G-out). But this requires every point to have both f(a) ∈ S and g^{-1}(a) ∈ S, which means S is closed under f and under g^{-1}. Since g^{-1}(a) = f(-a)·... hmm, let me think.

g^{-1}: if b = g(a) = a - sqrt(a² + h²), then a = ? We need to solve for a: b = a - sqrt(a² + h²), so sqrt(a² + h²) = a - b, so a² + h² = a² - 2ab + b², so h² = b² - 2ab, so a = (b² - h²)/(2b) (for b ≠ 0). So g^{-1}(b) = (b² - h²)/(2b) = b/2 - h²/(2b).

And f(a) = a + sqrt(a² + h²). f^{-1}(b) = (b² - h²)/(2b) as well? Let me check: if b = f(a) = a + sqrt(a² + h²), then sqrt(a² + h²) = b - a, so a² + h² = b² - 2ab + a², so h² = b² - 2ab, so a = (b² - h²)/(2b). Yes, f^{-1}(b) = (b² - h²)/(2b) = g^{-1}(b).

Wait, that can't be right. f and g are different functions, so their inverses should be different.

Let me recheck. f(a) = a + sqrt(a² + h²). If b = f(a), then b - a = sqrt(a² + h²) > 0, so b > a. And a = (b² - h²)/(2b).

g(a) = a - sqrt(a² + h²). If b = g(a), then a - b = sqrt(a² + h²) > 0, so a > b. And a = (b² - h²)/(2b).

So f^{-1}(b) = (b² - h²)/(2b) and g^{-1}(b) = (b² - h²)/(2b). They're the same! That makes sense because f and g are related: f(a) = a + sqrt(a² + h²) and g(a) = a - sqrt(a² + h²). If b = f(a), then a = f^{-1}(b). If b = g(a), then a = g^{-1}(b). And in both cases, a = (b² - h²)/(2b).

But wait, f maps ℝ to (0, ∞) and g maps ℝ to (-∞, 0). So f^{-1} is defined on (0, ∞) and g^{-1} is defined on (-∞, 0). They're the same formula but defined on different domains. So f^{-1}(b) for b > 0 gives the unique a with f(a) = b, and g^{-1}(b) for b < 0 gives the unique a with g(a) = b.

So the "F-in" edge to a point b > 0 comes from f^{-1        — AI历史解题过程（thinking）
#   polymath_04875         — 题目ID

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
  <problem_id>polymath_04875</problem_id>
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

What is the maximum number of isosceles triangles that can be formed using 100 points on a straight line and one additional point outside the line as vertices?

## Standard Solution

To determine the maximum number of isosceles triangles that can be formed using 100 points on a straight line and one additional point outside the line, we need to carefully analyze the conditions under which such triangles can be formed.

### Step-by-Step Solution:

1. **Identify the Key Components:**
   - There are 100 points on a straight line.
   - There is one additional point \( P \) outside the line.
   - Each isosceles triangle must have \( P \) as one of its vertices.

2. **Conditions for Isosceles Triangles:**
   - An isosceles triangle has at least two equal sides.
   - The external point \( P \) must be one of the vertices.
   - The other two vertices must be points on the line.

3. **Symmetric Arrangement:**
   - To maximize the number of isosceles triangles, we should arrange the points on the line symmetrically around the projection of \( P \) onto the line.
   - Let \( O \) be the projection of \( P \) onto the line.

4. **Forming Isosceles Triangles:**
   - For each pair of points \( A \) and \( B \) on the line, if \( A \) and \( B \) are equidistant from \( O \), then \( PA = PB \).
   - This configuration forms an isosceles triangle \( PAB \) with \( P \) as the apex.

5. **Counting Symmetric Pairs:**
   - With 100 points on the line, we can arrange them symmetrically around \( O \).
   - This means 50 points on one side of \( O \) and 50 points on the other side.
   - Each point on one side will have a corresponding point on the other side, forming a symmetric pair.

6. **Calculating the Number of Isosceles Triangles:**
   - Each symmetric pair \( (A, B) \) forms one isosceles triangle \( PAB \).
   - Since there are 50 such pairs, the number of isosceles triangles is 50.

### Conclusion:
By arranging the 100 points symmetrically around the projection of the external point onto the line, we maximize the number of isosceles triangles. Each pair of symmetric points forms one isosceles triangle with the external point, resulting in a total of 50 such triangles.

Thus, the maximum number of isosceles triangles is:

\[
\boxed{50}
\]

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have 100 points on a straight line and one additional point outside the line. We need to find the maximum number of isosceles triangles that can be formed using these 101 points as vertices.

First, let me check for answer leaks - the problem statement is clean, just asking the question. No leaked answers.

Now let me think about the problem.

We have 100 collinear points on a line L, and one point P outside the line. Total 101 points. We want to maximize the number of isosceles triangles.

A triangle needs 3 non-collinear points. Since 100 points are on the line, any triangle must use at least one point off the line. The only point off the line is P. So every triangle must include P.

Wait, can we form a triangle with 3 points on the line? No, they're collinear, so that's degenerate. So every triangle must include P and exactly 2 points from the line.

So triangles are of the form (P, A, B) where A, B are on the line.

Now, when is triangle PAB isosceles?

The three sides are PA, PB, AB.

Case 1: PA = PB (P is equidistant from A and B). This means A and B are symmetric about the foot of perpendicular from P to the line.

Case 2: PA = AB. The side from P to A equals the side from A to B (on the line).

Case 3: PB = AB. The side from P to B equals the side from A to B (on the line).

We want to maximize the total count of isosceles triangles, where each triangle is counted once.

Let me set up coordinates. Let the line be the x-axis, and P = (0, h) for some h > 0. The 100 points are at positions x_1, x_2, ..., x_100 on the x-axis.

For a triangle (P, A, B) with A = (a, 0), B = (b, 0):

- PA = sqrt(a² + h²)
- PB = sqrt(b² + h²)
- AB = |a - b|

Isosceles conditions:
1. PA = PB: a² + h² = b² + h², so a² = b², so a = -b (since a ≠ b for non-degenerate). This means A and B are symmetric about x=0 (the foot of perpendicular).

2. PA = AB: sqrt(a² + h²) = |a - b|, so a² + h² = (a-b)² = a² - 2ab + b², so h² = b² - 2ab, so b² - 2ab - h² = 0, solving for b: b = a ± sqrt(a² + h²). So b = a + sqrt(a²+h²) or b = a - sqrt(a²+h²).

3. PB = AB: similarly, a = b ± sqrt(b² + h²).

We want to choose the 100 positions to maximize the number of isosceles triangles.

Let me think about this more carefully. Each triangle (P, A, B) is determined by the unordered pair {A, B}. We want to maximize the number of pairs {A, B} such that at least one of the three isosceles conditions holds.

Let me think about each case separately and then worry about overlaps.

Case 1: PA = PB. This requires a = -b. So for each pair of points symmetric about 0, we get one isosceles triangle. If we place k points at positions and their negatives, we get floor(k/2) such pairs... actually, we need pairs (a, -a) with a ≠ 0. If we have points at positions x and -x, that's one pair. The maximum number of such pairs from 100 points: place 50 points at positive positions and 50 at their negatives. That gives 50 pairs. But we could also place a point at 0, but then it can't pair with anything (0 = -0). So max from Case 1 is 50.

Case 2: PA = AB. For a given A at position a, B must be at position a + sqrt(a²+h²) or a - sqrt(a²+h²). 

Case 3: PB = AB. For a given B at position b, A must be at position b + sqrt(b²+h²) or b - sqrt(b²+h²).

Cases 2 and 3 are symmetric (just swapping A and B labels). Let me think about them together.

For a point at position a, the "partner" positions that create an isosceles triangle where the equal sides are PA and AB (or PB and AB) are:
- b = a + sqrt(a² + h²)  (B is to the right of A, and PA = AB)
- b = a - sqrt(a² + h²)  (B is to the left of A, and PA = AB)
- a' = b + sqrt(b² + h²) → but this is case 3 from B's perspective

Actually, let me reconsider. For each ordered pair (A, B), case 2 gives PA = AB and case 3 gives PB = AB. Since we're counting unordered pairs {A, B}, we should think of it as: for the pair {A, B}, is it the case that PA = AB or PB = AB or PA = PB?

Let me think about it differently. For each point at position x_i, define:
- f(x_i) = x_i + sqrt(x_i² + h²): the position such that if another point is there, the triangle with A=x_i has PA = AB (B to the right)
- g(x_i) = x_i - sqrt(x_i² + h²): similarly to the left

Note that f(x) · g(x) = x² - (x² + h²) = -h². So f(x) and g(x) always have opposite signs, and their product is -h².

Also, f(x) = x + sqrt(x²+h²) and g(x) = x - sqrt(x²+h²). Note that g(x) = -h²/f(x).

Interesting. So if y = f(x), then x = g(y)? Let's check: if y = x + sqrt(x²+h²), then sqrt(x²+h²) = y - x, so x² + h² = y² - 2xy + x², so h² = y² - 2xy, so 2xy = y² - h², so x = (y² - h²)/(2y) = y/2 - h²/(2y). And g(y) = y - sqrt(y²+h²). Let me compute sqrt(y²+h²) where y = x + sqrt(x²+h²).

y² = x² + 2x·sqrt(x²+h²) + x² + h² = 2x² + h² + 2x·sqrt(x²+h²)
y² + h² = 2x² + 2h² + 2x·sqrt(x²+h²)

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me think about the structure more carefully. The key insight is about the function f(x) = x + sqrt(x² + h²).

Note that f is a strictly increasing function (its derivative is 1 + x/sqrt(x²+h²) > 0). Similarly g(x) = x - sqrt(x²+h²) is strictly decreasing.

Also note: f(x) > 0 for all x (since sqrt(x²+h²) > |x|), and g(x) < 0 for all x.

And f(x) · g(x) = -h², so g(x) = -h²/f(x).

Now, the relationship: if y = f(x), is x = g(y)?
g(y) = y - sqrt(y² + h²). We need to check if this equals x.
y = x + sqrt(x²+h²), so y² = x² + 2x·sqrt(x²+h²) + x² + h².
y² + h² = 2x² + 2h² + 2x·sqrt(x²+h²) = 2(x² + h²) + 2x·sqrt(x²+h²).
Let s = sqrt(x²+h²). Then y = x + s, y² + h² = 2s² + 2xs = 2s(s+x) = 2sy.
sqrt(y²+h²) = sqrt(2sy).
g(y) = y - sqrt(2sy) = (x+s) - sqrt(2s(x+s)).

Hmm, this doesn't simplify to x in general. So f and g are not inverses of each other.

Let me reconsider. The condition PA = AB means: for points at positions a and b, sqrt(a²+h²) = |a-b|. This gives b = a + sqrt(a²+h²) or b = a - sqrt(a²+h²), i.e., b = f(a) or b = g(a).

Similarly, PB = AB means sqrt(b²+h²) = |a-b|, giving a = f(b) or a = g(b).

So the pair {a, b} satisfies one of cases 2 or 3 iff b ∈ {f(a), g(a)} or a ∈ {f(b), g(b)}.

But note: b = f(a) is the same as saying a = g(b)? Let me check. If b = f(a) = a + sqrt(a²+h²), then is a = g(b)?
g(b) = b - sqrt(b²+h²). We computed sqrt(b²+h²) = sqrt(2sb) where s = sqrt(a²+h²), b = a+s.
So g(b) = (a+s) - sqrt(2s(a+s)).

This is not equal to a in general. So b = f(a) and a = g(b) are different conditions.

Hmm wait, but actually b = f(a) means PA = AB (with B to the right of A). And a = g(b) means PB = AB (with A to the left of B). These are different isosceles conditions for the same triangle. A triangle could satisfy both, making it isosceles in two ways (which would actually make it equilateral, but that's impossible here since P is off the line).

Actually, let me reconsider. For the pair {A, B} with A at position a, B at position b:
- PA = AB: sqrt(a²+h²) = |a-b|
- PB = AB: sqrt(b²+h²) = |a-b|

Both can't hold simultaneously unless PA = PB, which is case 1. So if PA = AB and PB = AB, then PA = PB, which means a = -b, and then |a-b| = 2|a|, and sqrt(a²+h²) = 2|a|, so a² + h² = 4a², h² = 3a². This is a special case.

OK so let me think about this problem differently. Let me think about what configuration of 100 points maximizes the count.

Let me consider the "chain" structure. Define a directed graph where we connect x → f(x) and x → g(x). If we have points at positions that form chains under f and g, we can count the isosceles triangles.

Actually, let me think about it as follows. For each unordered pair {a, b} of points on the line, the triangle PAB is isosceles iff:
- a = -b (Case 1), or
- b = f(a) or b = g(a) (Case 2: PA = AB), or
- a = f(b) or a = g(b) (Case 3: PB = AB)

But Case 2 and Case 3 overlap: b = f(a) is a specific condition, and a = g(b) is another. They're different conditions that could both hold for the same pair.

Let me think about the total count. We want to count the number of unordered pairs {a, b} that satisfy at least one of these conditions.

Let me think about the structure of f and g more carefully.

f(x) = x + sqrt(x² + h²), g(x) = x - sqrt(x² + h²).

Properties:
- f(x) > 0, g(x) < 0 for all x
- f is strictly increasing, g is strictly decreasing
- f(x) · g(x) = -h²
- f(-x) = -x + sqrt(x²+h²) = -g(x), and g(-x) = -x - sqrt(x²+h²) = -f(x)

So f(-x) = -g(x) and g(-x) = -f(x). This means f and g are related by reflection.

Now, consider the map T: x → f(x). This is a bijection from ℝ to (0, ∞). And the map S: x → g(x) is a bijection from ℝ to (-∞, 0).

For the isosceles condition PA = AB with B to the right: b = f(a). Since f maps ℝ to (0,∞), b must be positive. And a can be anything.

For PA = AB with B to the left: b = g(a). Since g maps ℝ to (-∞,0), b must be negative.

Similarly for PB = AB: a = f(b) (a positive) or a = g(b) (a negative).

So let me think about chains. Consider the sequence: x, f(x), f(f(x)), f(f(f(x))), .... If we place points at consecutive elements of such a chain, each consecutive pair gives an isosceles triangle (PA = AB type).

But we can also use g. Note that g(x) = -h²/f(x). And f and g are related.

Let me think about this differently. Let me consider the substitution x = h·sinh(t). Then:
- sqrt(x² + h²) = h·cosh(t)
- f(x) = h·sinh(t) + h·cosh(t) = h·e^t
- g(x) = h·sinh(t) - h·cosh(t) = -h·e^{-t}

So in terms of the parameter t:
- f maps x = h·sinh(t) to h·e^t
- g maps x = h·sinh(t) to -h·e^{-t}

Now let's see what f and g do in terms of the parameter. If x = h·sinh(t), then f(x) = h·e^t. To apply f again, we need to express h·e^t as h·sinh(s) for some s: sinh(s) = e^t, so s = arcsinh(e^t). Then f(f(x)) = h·e^{arcsinh(e^t)}.

This is getting complicated. Let me try a different parametrization.

Let me use x = h·sinh(t) so that sqrt(x²+h²) = h·cosh(t), and the distance from P=(0,h) to (x,0) is h·cosh(t).

Then:
- f(x) = h·e^t (position to the right where PA = AB)
- g(x) = -h·e^{-t} (position to the left where PA = AB)

Now, for a pair {a, b} with a = h·sinh(s), b = h·sinh(u):
- PA = h·cosh(s), PB = h·cosh(u), AB = h·|sinh(s) - sinh(u)|

Case 1 (PA = PB): cosh(s) = cosh(u), so s = ±u. Since a ≠ b, s = -u, meaning a = -b. ✓

Case 2 (PA = AB): h·cosh(s) = h·|sinh(s) - sinh(u)|, so cosh(s) = |sinh(s) - sinh(u)|.
If u > s: sinh(u) - sinh(s) = cosh(s), so sinh(u) = sinh(s) + cosh(s) = e^s, so u = arcsinh(e^s).
If u < s: sinh(s) - sinh(u) = cosh(s), so sinh(u) = sinh(s) - cosh(s) = -e^{-s}, so u = arcsinh(-e^{-s}) = -arcsinh(e^{-s}).

So in Case 2:
- b = f(a): u = arcsinh(e^s), i.e., sinh(u) = e^s, i.e., b = h·e^s. (Note: f(a) = h·e^s ✓)
- b = g(a): u = -arcsinh(e^{-s}), i.e., sinh(u) = -e^{-s}, i.e., b = -h·e^{-s}. (Note: g(a) = -h·e^{-s} ✓)

Case 3 (PB = AB): h·cosh(u) = h·|sinh(s) - sinh(u)|, so cosh(u) = |sinh(s) - sinh(u)|.
If s > u: sinh(s) - sinh(u) = cosh(u), so sinh(s) = sinh(u) + cosh(u) = e^u, so s = arcsinh(e^u), i.e., a = f(b).
If s < u: sinh(u) - sinh(s) = cosh(u), so sinh(s) = sinh(u) - cosh(u) = -e^{-u}, so s = -arcsinh(e^{-u}), i.e., a = g(b).

So Case 3 gives a = f(b) or a = g(b), as expected.

Now, let me think about the structure. We have the map f and g. Let me think about what happens when we compose them.

If b = f(a), meaning sinh(u) = e^s (where a = h·sinh(s), b = h·sinh(u)):
Then what is f(b)? f(b) = h·e^u where sinh(u) = e^s. So u = arcsinh(e^s) = ln(e^s + sqrt(e^{2s}+1)). So e^u = e^s + sqrt(e^{2s}+1).

And g(b) = -h·e^{-u} = -h/(e^s + sqrt(e^{2s}+1)) = -h·(sqrt(e^{2s}+1) - e^s) = -h·sqrt(e^{2s}+1) + h·e^s.

Hmm, this is getting complex. Let me try to think about the problem from a higher level.

The key question is: what is the maximum number of isosceles triangles?

Each isosceles triangle corresponds to an unordered pair {A, B} from the 100 points. There are C(100,2) = 4950 pairs total. We want to maximize how many of these are isosceles.

Let me think about the "graph" where vertices are the 100 points on the line, and edges connect pairs that form isosceles triangles with P. We want to maximize the number of edges.

The edges come from three types:
1. Symmetric pairs: {a, -a} — at most 50 such pairs.
2. f-edges: {a, f(a)} — for each point a, at most one f-edge (if f(a) is also a point).
3. g-edges: {a, g(a)} — for each point a, at most one g-edge (if g(a) is also a point).

But wait, f-edges and g-edges from Case 2, and also from Case 3. Let me be more careful.

For a pair {a, b}:
- It's a Case 2 edge if b = f(a) or b = g(a) (PA = AB)
- It's a Case 3 edge if a = f(b) or a = g(b) (PB = AB)

Now, b = f(a) is the same pair as a = g(b)? No, I showed earlier they're different. Let me re-examine.

b = f(a) means b = a + sqrt(a²+h²). This is PA = AB with B to the right.
a = g(b) means a = b - sqrt(b²+h²). This is PB = AB with A to the left of B.

For the same pair {a, b} with a < b:
- b = f(a): PA = AB, i.e., sqrt(a²+h²) = b - a
- a = g(b): PB = AB, i.e., sqrt(b²+h²) = b - a

These are different conditions. Both could hold, but that would mean sqrt(a²+h²) = sqrt(b²+h²), so a² = b², so a = -b (since a < b). Then b - a = 2b and sqrt(b²+h²) = 2b, so b² + h² = 4b², h² = 3b². Special case.

So in general, for a pair {a, b} with a < b, the possible isosceles conditions are:
- a = -b (Case 1)
- b = f(a) = a + sqrt(a²+h²) (Case 2, PA = AB)
- a = g(b) = b - sqrt(b²+h²) (Case 3, PB = AB)
- b = g(a)? No, g(a) < 0 and if a < b, then b could be negative or positive. Actually g(a) < 0 always. So b = g(a) requires b < 0, and then a > b since g is decreasing and g(a) < a... wait, g(a) = a - sqrt(a²+h²) < a always. So if b = g(a), then b < a, contradicting a < b. So for a < b, b = g(a) is impossible.
- Similarly, a = f(b) requires a > 0 and a = f(b) > b, contradicting a < b. So a = f(b) is impossible for a < b.

So for a < b, the isosceles conditions are exactly:
1. a = -b (symmetric pair)
2. b = f(a) (PA = AB)
3. a = g(b) (PB = AB)

And these are three distinct conditions (except in the special equilateral-like case).

Now, let me think about the structure. We have three types of "connections":
- Type S (symmetric): connects a and -a
- Type F: connects a to f(a) (a can be any real, f(a) > 0)
- Type G: connects b to g(b) (b can be any real, g(b) < 0), but equivalently, connects g(b) to b, i.e., for a < 0, connects a to the b such that a = g(b), i.e., b = g^{-1}(a).

Wait, let me reconsider. For a < b:
- Type F: b = f(a). Since f is increasing and f(a) > a always, this gives a < b. ✓
- Type G: a = g(b). Since g is decreasing and g(b) < b always, this gives a < b. ✓

So Type F connects a → f(a) (always to the right), and Type G connects g(b) → b (from left to right, since g(b) < b).

Now, let me think about chains. Consider starting from some point and following f repeatedly: x, f(x), f(f(x)), .... Each consecutive pair is a Type F isosceles triangle. Similarly for g.

But we can also mix. Let me think about what f and g look like in the sinh parametrization.

With x = h·sinh(t):
- f(x) = h·e^t
- g(x) = -h·e^{-t}

Let me define the "t-parameter" of a point at position x as t = arcsinh(x/h). Then:
- f sends t → arcsinh(e^t) (since f(x) = h·e^t, and the t-param of h·e^t is arcsinh(e^t/h·h) = arcsinh(e^t))

Wait, let me redo. If x = h·sinh(t), then f(x) = h·e^t. The t-parameter of f(x) is t' = arcsinh(f(x)/h) = arcsinh(e^t).

Similarly, g(x) = -h·e^{-t}, and the t-parameter is t' = arcsinh(g(x)/h) = arcsinh(-e^{-t}) = -arcsinh(e^{-t}).

So in t-space:
- F: t → arcsinh(e^t)
- G: t → -arcsinh(e^{-t})

Let me denote F(t) = arcsinh(e^t) and G(t) = -arcsinh(e^{-t}).

Note: arcsinh(u) = ln(u + sqrt(u²+1)). So:
- F(t) = ln(e^t + sqrt(e^{2t}+1))
- G(t) = -ln(e^{-t} + sqrt(e^{-2t}+1))

Let me check: F(t) = arcsinh(e^t) = ln(e^t + sqrt(e^{2t}+1)).
G(t) = -arcsinh(e^{-t}) = -ln(e^{-t} + sqrt(e^{-2t}+1)) = ln(1/(e^{-t} + sqrt(e^{-2t}+1))) = ln((sqrt(e^{-2t}+1) - e^{-t})/((e^{-2t}+1) - e^{-2t})) = ln(sqrt(e^{-2t}+1) - e^{-t}) + t.

Hmm, let me simplify. Note that arcsinh(e^{-t}) = ln(e^{-t} + sqrt(e^{-2t}+1)). And 1/(e^{-t} + sqrt(e^{-2t}+1)) = sqrt(e^{-2t}+1) - e^{-t} (rationalizing). So G(t) = -ln(e^{-t} + sqrt(e^{-2t}+1)) = ln(sqrt(e^{-2t}+1) - e^{-t}).

Also note: sqrt(e^{-2t}+1) = e^{-t}·sqrt(1+e^{2t}). So G(t) = ln(e^{-t}(sqrt(1+e^{2t}) - 1)) = -t + ln(sqrt(1+e^{2t}) - 1).

And F(t) = ln(e^t + sqrt(e^{2t}+1)) = t + ln(1 + sqrt(1+e^{-2t})).

Hmm, these are getting messy. Let me try another substitution. Let u = e^t. Then:
- F: u → e^{arcsinh(u)} = u + sqrt(u²+1)
- G: u → e^{-arcsinh(1/u)} = 1/(1/u + sqrt(1/u²+1)) = u/(1 + sqrt(1+u²)) = u(sqrt(1+u²)-1)/u² = (sqrt(1+u²)-1)/u

So in u-space (where u = e^t > 0):
- F: u → u + sqrt(u²+1)
- G: u → (sqrt(1+u²)-1)/u

Note that F(u) · G(u) = (u + sqrt(u²+1)) · (sqrt(1+u²)-1)/u = (u²+1 - 1)/u · ... wait let me compute:
(u + sqrt(u²+1)) · (sqrt(1+u²)-1)/u = [(u + sqrt(u²+1))(sqrt(u²+1)-1)]/u = [u·sqrt(u²+1) - u + u²+1 - sqrt(u²+1)]/u = [u·sqrt(u²+1) - sqrt(u²+1) + u² - u + 1]/u

Hmm, that doesn't simplify nicely. Let me try differently.

F(u) = u + sqrt(u²+1), G(u) = (sqrt(u²+1)-1)/u.

F(u) · G(u) = (u + sqrt(u²+1))(sqrt(u²+1)-1)/u = (u²+1 - u + u·sqrt(u²+1) - sqrt(u²+1))/u... 

Actually let me just compute: (u + s)(s - 1)/u where s = sqrt(u²+1).
= (us - u + s² - s)/u = (us - u + u² + 1 - s)/u = s - 1 + u + (1-s)/u = s - 1 + u - (s-1)/u.

Hmm, not clean. Let me try: F(u) = u + s, G(u) = (s-1)/u where s = sqrt(u²+1).

F(u) · G(u) = (u+s)(s-1)/u. And note that (s-1)(s+1) = s²-1 = u². So (s-1)/u = u/(s+1). Therefore G(u) = u/(s+1) = u/(sqrt(u²+1)+1).

And F(u) = u + s = u + sqrt(u²+1).

So F(u) · G(u) = (u + sqrt(u²+1)) · u/(sqrt(u²+1)+1) = u · (u + sqrt(u²+1))/(sqrt(u²+1)+1) = u · 1 = u.

Wait, that's because (u + sqrt(u²+1))/(sqrt(u²+1)+1)... hmm, u + sqrt(u²+1) ≠ sqrt(u²+1) + 1 in general.

Let me recompute. F(u) = u + sqrt(u²+1). G(u) = u/(sqrt(u²+1)+1).

F(u) · G(u) = (u + sqrt(u²+1)) · u / (sqrt(u²+1) + 1).

Let s = sqrt(u²+1). Then F(u)·G(u) = u(u+s)/(s+1). This is not simply u unless u+s = s+1, i.e., u=1.

OK this algebraic approach isn't leading anywhere clean. Let me think about the problem differently.

Let me think about the problem in terms of the original coordinates and try to find the maximum by construction.

Key insight: We want to choose 100 points on a line to maximize isosceles triangles with a fixed external point P. The three types of isosceles conditions give us three types of "edges" between points. We want to maximize the total number of edges.

Let me think about what structures allow many edges.

Type S (symmetric): {a, -a}. At most 50 edges (50 pairs of symmetric points).

Type F: {a, f(a)}. Each point a has at most one F-edge (to f(a)). So at most 100 F-edges, but each edge is counted once, so at most 100/... well, each F-edge connects a to f(a), and f is injective, so each point is the "source" of at most one F-edge and the "target" of at most one F-edge (since f is injective, f^{-1} exists). So the F-edges form a matching-like structure, but actually they can form chains: a → f(a) → f(f(a)) → .... In a chain of length k (k points), there are k-1 F-edges. But also, a point could be both a source and target: if b = f(a) and c = f(b), then a → b → c is a chain with 2 edges from 3 points.

Wait, but f is a bijection from ℝ to (0,∞). So f is injective. Each point has at most one outgoing F-edge and at most one incoming F-edge. So the F-edges form a collection of paths (chains). In a chain of k points, there are k-1 F-edges. With 100 points, if all are in one chain, we get 99 F-edges. But can all 100 points be in one F-chain?

A chain would be: a, f(a), f(f(a)), f(f(f(a))), .... For this to work, all these must be among our 100 points. Since f maps ℝ to (0,∞), after the first step, all subsequent points are positive. And f is increasing, so the chain is increasing. So we'd need 100 points in an increasing sequence where each is f of the previous. That's certainly possible (just pick any a and iterate f).

Similarly for G-edges: g is a bijection from ℝ to (-∞, 0). G-edges connect b to g(b) (i.e., g(b) → b). Each point has at most one outgoing G-edge (to g(b), which is to the left) and at most one incoming G-edge (from g^{-1}(b), which is from the right). So G-edges also form chains, going leftward.

Now, can we have both F-chains and G-chains simultaneously? A point a can have an F-edge (to f(a)) and a G-edge (to g(a)). So the F-edges and G-edges together form a graph where each point has at most degree 4 (one F-out, one F-in, one G-out, one G-in), but actually at most degree 2 in each direction.

Wait, but we need to be careful. The F-edge from a goes to f(a) (rightward), and the G-edge from a goes to g(a) (leftward). The F-edge to a comes from f^{-1}(a) (from the left, since f^{-1}(a) < a), and the G-edge to a comes from g^{-1}(a) (from the right, since g^{-1}(a) > a).

So each point has:
- F-out: to f(a) (right)
- F-in: from f^{-1}(a) (left)
- G-out: to g(a) (left)
- G-in: from g^{-1}(a) (right)

So the combined F+G graph has each point with up to 4 neighbors: f(a) and g^{-1}(a) to the right, f^{-1}(a) and g(a) to the left.

But wait, could f(a) = g^{-1}(a)? That would mean the F-out neighbor equals the G-in neighbor. Let me check: f(a) = g^{-1}(a) means g(f(a)) = a. g(f(a)) = f(a) - sqrt(f(a)²+h²). With f(a) = a + sqrt(a²+h²), this is a + sqrt(a²+h²) - sqrt((a+sqrt(a²+h²))²+h²). For this to equal a, we need sqrt(a²+h²) = sqrt((a+sqrt(a²+h²))²+h²), which means a²+h² = (a+sqrt(a²+h²))²+h², so a² = a² + 2a·sqrt(a²+h²) + a²+h², so 0 = 2a·sqrt(a²+h²) + a² + h². If a < 0, this could have solutions. 2a·sqrt(a²+h²) = -(a²+h²), so 4a²(a²+h²) = (a²+h²)², so 4a² = a²+h², so 3a² = h², so a = -h/sqrt(3) (taking a < 0). Then f(a) = -h/sqrt(3) + sqrt(h²/3+h²) = -h/sqrt(3) + 2h/sqrt(3) = h/sqrt(3). And g(f(a)) = g(h/sqrt(3)) = h/sqrt(3) - sqrt(h²/3+h²) = h/sqrt(3) - 2h/sqrt(3) = -h/sqrt(3) = a. ✓

So at the special point a = -h/sqrt(3), we have f(a) = h/sqrt(3) and g(f(a)) = a. This means the pair {a, f(a)} = {-h/sqrt(3), h/sqrt(3)} is both an F-edge and a G-edge. But it's also a symmetric pair (Type S)! So this is the special equilateral case I mentioned earlier.

OK, this is getting very complex. Let me step back and think about the problem from a competition math perspective.

The answer to this problem is likely 100·99/2 - (something) or related to a nice formula. Let me think about upper bounds and constructions.

Upper bound: Each of the 100 points can be the "apex" of isosceles triangles (where the two equal sides meet at that point) or the "base" point.

Actually, let me reconsider. In triangle PAB:
- If PA = PB, the apex is P. (Type S)
- If PA = AB, the apex is A. (Type F, with B = f(a) or g(a))
- If PB = AB, the apex is B. (Type G, with A = f(b) or g(b))

For Type S: P is the apex. Each pair {a, -a} gives one triangle. Max 50.

For Type F (apex at A): For each point A at position a, the possible B's are f(a) and g(a). So each point A is the apex of at most 2 isosceles triangles (one with B = f(a), one with B = g(a)). So at most 200 Type F triangles. But wait, each triangle {A, B} with PA = AB is counted once (with apex A). And each triangle {A, B} with PB = AB is counted once (with apex B). So the total from Types F and G is at most 200 (each of 100 points is apex of at most 2 triangles).

Wait, but a triangle could be both Type F and Type G (if PA = AB and PB = AB, which means PA = PB, so it's also Type S). So there could be double-counting. But for counting distinct triangles, we need to be careful.

Hmm, let me reconsider. For each point A at position a, A can be the apex of at most 2 isosceles triangles: {A, f(a)} and {A, g(a)} (where PA = AB). So the total number of triangles where the apex is on the line is at most 200.

Additionally, P can be the apex (Type S), giving at most 50 triangles.

But some triangles might be counted in both categories. A triangle {A, B} is Type S if a = -b, and it's Type F (apex A) if b = f(a) or b = g(a). For it to be both Type S and Type F, we need b = -a and b = f(a) (or g(a)). b = -a and b = f(a) = a + sqrt(a²+h²): -a = a + sqrt(a²+h²), so sqrt(a²+h²) = -2a, so a < 0 and a²+h² = 4a², h² = 3a², a = -h/sqrt(3). Similarly for g(a).

So the overlap is small (at most 2 triangles, corresponding to a = ±h/sqrt(3)).

So the upper bound is approximately 200 + 50 = 250, minus small overlaps.

But wait, I need to be more careful. The 200 bound comes from: each of 100 points is the apex of at most 2 triangles. But can all 100 points simultaneously be the apex of 2 triangles each? That requires f(a) and g(a) to both be among the 100 points, for every point a. This is a strong constraint.

Let me think about whether we can achieve close to 200 + 50 = 250.

Actually, let me reconsider the problem. The 200 bound might not be tight. Let me think about it as a graph problem.

We have 100 points. We want to place them to maximize the number of "isosceles pairs." The isosceles pairs come from:
- S-edges: {a, -a} (at most 50)
- F-edges: {a, f(a)} (each point has at most 1 outgoing and 1 incoming, forming chains)
- G-edges: {a, g(a)} (each point has at most 1 outgoing and 1 incoming, forming chains)

The total number of edges is |S| + |F| + |G| - |overlaps|.

Now, F-edges: since each point has at most 1 F-out and 1 F-in, the F-edges form a union of directed paths. With 100 points, the maximum number of F-edges is 99 (one long chain). But we need all 100 points to be in the chain, and the chain is a, f(a), f²(a), ..., f^{99}(a). This is possible if we choose a appropriately.

Similarly, G-edges: maximum 99, with a chain a, g(a), g²(a), ..., g^{99}(a).

But can we have both a long F-chain and a long G-chain simultaneously? The F-chain goes rightward (increasing), and the G-chain goes leftward (decreasing). A point can be in both chains. But the F-chain requires f(a_i) = a_{i+1} and the G-chain requires g(a_j) = a_{j-1}.

If a point a is in the F-chain (with successor f(a)) and in the G-chain (with predecessor g^{-1}(a) and successor g(a)), then a has F-out to f(a), G-out to g(a), F-in from f^{-1}(a), G-in from g^{-1}(a). So a has up to 4 neighbors in the combined graph.

The combined F+G graph is a directed graph where each node has out-degree ≤ 2 (F-out and G-out) and in-degree ≤ 2 (F-in and G-in). The total number of edges is at most 2·100 = 200 (from out-degree) or 2·100 = 200 (from in-degree). But since each edge contributes 1 to total out-degree and 1 to total in-degree, the total is at most 200.

But can we achieve 200? That would require every point to have both F-out and G-out, meaning f(a) and g(a) are both among the 100 points, for every point a. Is this possible?

If every point a has f(a) in the set, then the set is closed under f. If every point a has g(a) in the set, then the set is closed under g. So the set is closed under both f and g. 

Since f maps to (0,∞) and g maps to (-∞,0), and f and g are bijections, a finite set closed under both f and g would need to be... well, f sends any real to a positive number, and g sends any real to a negative number. If we start with a positive number p and apply g, we get a negative number. Apply f to that negative number, we get a positive number. Etc.

So the orbit of a point under f and g alternates between positive and negative. For a finite set closed under both f and g, we'd need the orbit to be finite, which means it must cycle. But f is strictly increasing and sends everything to positive, while g is strictly decreasing and sends everything to negative. Can we have a cycle?

A cycle would be: a → f(a) → g(f(a)) → f(g(f(a))) → ... → a. But f always increases the value (f(a) > a) and g always decreases it (g(a) < a). So f(g(f(a))) could be larger or smaller than f(a) depending on whether f "wins" or g "wins."

Actually, f(a) > a always, and g(a) < a always. So:
- f moves right
- g moves left

A cycle would require equal numbers of f-steps and g-steps (to return to start). But the composition might not return exactly.

Let me think about this differently. Can a finite set be closed under both f and g?

Consider the map T = g ∘ f (apply f first, then g). T(a) = g(f(a)) = f(a) - sqrt(f(a)²+h²). Since f(a) > 0, T(a) = f(a) - sqrt(f(a)²+h²) < 0. And T(a) = g(f(a)), and since g maps to (-∞,0), T(a) < 0.

Also, T(a) = f(a) - sqrt(f(a)²+h²) = -h²/(f(a) + sqrt(f(a)²+h²)) = -h²/(2f(a) + ...). Hmm.

Actually, recall that g(x) = -h²/f(x) (since f(x)·g(x) = -h²). Wait, is that right? f(x)·g(x) = (x+sqrt(x²+h²))(x-sqrt(x²+h²)) = x² - (x²+h²) = -h². Yes! So g(x) = -h²/f(x).

So T(a) = g(f(a)) = -h²/f(f(a)).

And f(f(a)) > f(a) > 0 (since f is increasing and f(x) > x for all x... wait, is f(x) > x? f(x) = x + sqrt(x²+h²) > x. Yes, since sqrt(x²+h²) > 0.)

So f(f(a)) > f(a) > 0, and T(a) = -h²/f(f(a)) ∈ (-h²/f(a), 0) ⊂ (-∞, 0).

Now, |T(a)| = h²/f(f(a)) < h²/f(a) = |g(a)|. So |T(a)| < |g(a)|, meaning T(a) is closer to 0 than g(a).

So the map T = g∘f sends a to a point closer to 0 (in absolute value) than g(a). If we iterate T, we get closer and closer to 0. So there's no finite cycle (except possibly 0 itself, but 0 is not in the range of f or g since f(x) > 0 and g(x) < 0).

This means a finite set cannot be closed under both f and g (unless it's empty). So we cannot achieve 200 F+G edges.

Hmm, so what's the actual maximum?

Let me reconsider. We don't need the set to be closed under f and g. We just need to maximize the number of edges. Let me think about this as follows.

Consider the combined graph (F-edges + G-edges + S-edges). Each point has:
- At most 1 F-out edge (to f(a))
- At most 1 F-in edge (from f^{-1}(a))
- At most 1 G-out edge (to g(a))
- At most 1 G-in edge (from g^{-1}(a))
- At most 1 S-edge (to -a)

The S-edge is symmetric (if {a,-a} is an S-edge, it's the same from both ends).

Total edges ≤ (100 F-out + 100 G-out + 50 S) / 1 = 250. But this overcounts because:
- An F-edge and G-edge could be the same pair (the special equilateral case)
- An F-edge or G-edge could also be an S-edge

But more importantly, the 200 F+G bound assumes every point has both F-out and G-out, which we showed is impossible for a finite set.

Let me think about this more carefully.

Let me consider the structure of the F+G graph. The F-edges form chains (rightward), and the G-edges form chains (leftward). A point can be in both an F-chain and a G-chain.

Think of it as: each point has a "right neighbor" (F-out, if f(a) is in the set) and a "left neighbor" (G-out, if g(a) is in the set). Also, each point has a "left F-neighbor" (F-in, if f^{-1}(a) is in the set) and a "right G-neighbor" (G-in, if g^{-1}(a) is in the set).

The F-out and G-in are both "rightward" edges, and F-in and G-out are both "leftward" edges. But F-out and G-in could go to different points (or the same point in the special case).

Let me think about the rightward edges from a point a: f(a) and g^{-1}(a). Are these always different?

f(a) = g^{-1}(a) iff g(f(a)) = a iff T(a) = a. We showed T(a) is closer to 0 than g(a), and T(a) < 0. For T(a) = a, we need a < 0 and |T(a)| = |a|. But |T(a)| < |g(a)| = h²/f(a). And |a| vs h²/f(a): f(a) = a + sqrt(a²+h²). For a < 0, f(a) = a + sqrt(a²+h²) < sqrt(a²+h²) (since a < 0). So h²/f(a) > h²/sqrt(a²+h²) > h²/sqrt(a²+h²). And |a| vs h²/sqrt(a²+h²): |a|·sqrt(a²+h²) vs h². If |a| is large, |a|·sqrt(a²+h²) ≈ a² > h², so |a| > h²/sqrt(a²+h²) > |T(a)|. So T(a) ≠ a for large |a|.

We already found that T(a) = a iff a = -h/sqrt(3). So f(a) = g^{-1}(a) only at a = -h/sqrt(3).

So in general, the rightward neighbors f(a) and g^{-1}(a) are different (except at one special point). Similarly, the leftward neighbors f^{-1}(a) and g(a) are different (except at a = h/sqrt(3)).

So the combined graph (F + G) is essentially a graph where each node has up to 2 rightward edges and 2 leftward edges, forming a kind of "double chain" structure.

Now, the total number of F+G edges. Let's think of it as: each point contributes its F-out and G-out edges. The total is the number of points a such that f(a) is in the set, plus the number of points a such that g(a) is in the set.

Let me denote the set of 100 points as S. The number of F-edges is |{a ∈ S : f(a) ∈ S}|, and the number of G-edges is |{a ∈ S : g(a) ∈ S}|.

We want to maximize |{a ∈ S : f(a) ∈ S}| + |{a ∈ S : g(a) ∈ S}| + |{a ∈ S : -a ∈ S, a > 0}| (the S-edges, counting each pair once).

Now, the constraint is that S is a finite set of 100 real numbers.

Let me think about the F-edges. If we order the points as x_1 < x_2 < ... < x_100, then f(x_i) > x_i, so if f(x_i) ∈ S, it must be some x_j with j > i. The F-edges form a set of "forward jumps" in the ordered sequence.

Similarly, g(x_i) < x_i, so if g(x_i) ∈ S, it must be some x_j with j < i. The G-edges form "backward jumps."

Now, the key constraint: f is a bijection ℝ → (0,∞), so f^{-1} exists. If f(x_i) = x_j, then x_j = f(x_i), and this is the unique F-edge from x_i. Also, x_i = f^{-1}(x_j), so x_i is the unique F-predecessor of x_j. So the F-edges form a partial matching between consecutive elements in F-chains.

Let me think about the maximum number of F-edges. If we have a chain x_1, x_2, ..., x_k where f(x_i) = x_{i+1}, that's k-1 F-edges from k points. The remaining 100-k points could form another chain, etc. The maximum is 99 (one chain of 100 points).

Similarly for G-edges: maximum 99.

But can we have both many F-edges and many G-edges?

Consider a point x_i. It has an F-edge to f(x_i) = x_j (j > i) and a G-edge to g(x_i) = x_k (k < i). For the F-chain, x_i's successor is x_j, and for the G-chain, x_i's successor is x_k (going leftward). 

The F-chain and G-chain are independent in the sense that the F-successor and G-successor of x_i are generally different points. So in principle, we could have a long F-chain and a long G-chain sharing the same 100 points.

But the constraint is that the points must satisfy f(x_i) = x_j AND g(x_i) = x_k for the edges to exist. The positions are determined by the f and g relationships.

Let me think about this differently. Suppose we want a set S closed under f (so every point's f-image is in S). Then S must be an F-chain: {a, f(a), f²(a), ..., f^{99}(a)}. This gives 99 F-edges. But then, how many G-edges does this set have?

For a point x in the F-chain, g(x) is generally not in the chain (since the chain is determined by f-iteration, and g is a different function). So the G-edges would be few.

Alternatively, can we find a set that has many F-edges and many G-edges simultaneously?

Let me think about the problem from the perspective of the parametrization x = h·sinh(t).

In t-space:
- F: t → arcsinh(e^t) (let's call this φ(t))
- G: t → -arcsinh(e^{-t}) (let's call this γ(t))

Note: φ(t) = arcsinh(e^t) and γ(t) = -arcsinh(e^{-t}).

Observe: γ(t) = -arcsinh(e^{-t}) = -φ(-t). So γ(t) = -φ(-t).

Also, φ(t) > 0 for all t (since e^t > 0 and arcsinh of a positive number is positive). And γ(t) < 0 for all t.

Now, φ is increasing (derivative: e^t/sqrt(e^{2t}+1) > 0). And γ is also increasing (derivative: e^{-t}/sqrt(e^{-2t}+1) > 0). Wait, let me check: γ(t) = -arcsinh(e^{-t}), dγ/dt = -(-e^{-t})/sqrt(e^{-2t}+1) = e^{-t}/sqrt(e^{-2t}+1) > 0. Yes, γ is increasing.

Also, φ(t) → ∞ as t → ∞ and φ(t) → 0 as t → -∞. γ(t) → 0 as t → ∞ and γ(t) → -∞ as t → -∞.

Now, φ(t) > t? φ(t) = arcsinh(e^t). For large t, arcsinh(e^t) ≈ t (since arcsinh(e^t) = ln(e^t + sqrt(e^{2t}+1)) ≈ ln(2e^t) = t + ln 2). So φ(t) ≈ t + ln 2 for large t. So φ(t) > t for all t.

Similarly, γ(t) < t? γ(t) = -arcsinh(e^{-t}). For large t, γ(t) ≈ -e^{-t} → 0. And t is large, so γ(t) < t. For t → -∞, γ(t) ≈ -(-t) = t... wait, arcsinh(e^{-t}) for t → -∞ is arcsinh(e^{|t|}) ≈ |t| = -t. So γ(t) ≈ -(-t) = t. More precisely, γ(t) ≈ t - ln 2 for t → -∞. So γ(t) < t for all t.

So in t-space, φ moves right (φ(t) > t) and γ also moves... γ(t) < t, so γ moves left. Wait, but I said γ is increasing. Let me re-examine.

γ(t) = -arcsinh(e^{-t}). As t increases, e^{-t} decreases, arcsinh(e^{-t}) decreases, so -arcsinh(e^{-t}) increases. So γ is increasing. And γ(t) < t (moves left in t-space). But since γ is increasing, if t_1 < t_2, then γ(t_1) < γ(t_2). So the G-edges in t-space go from t to γ(t) which is to the left, but the ordering is preserved.

Hmm, I realize the t-space doesn't directly correspond to the left-right ordering on the line, because x = h·sinh(t) is an increasing function of t, so t-space ordering = x-space ordering. So F-edges go right (φ(t) > t) and G-edges go left (γ(t) < t) in both t-space and x-space. Good.

Now, the key question: can we have a set of 100 t-values that has many φ-edges and many γ-edges?

Let me think about the composition. Consider the map ψ = γ ∘ φ (apply φ first, then γ). ψ(t) = γ(φ(t)) = -arcsinh(e^{-φ(t)}) = -arcsinh(e^{-arcsinh(e^t)}).

For large t: φ(t) ≈ t + ln 2, so e^{-φ(t)} ≈ e^{-t-2} = e^{-t}/e^2... wait, e^{-φ(t)} ≈ e^{-(t+ln 2)} = e^{-t}/2. Then arcsinh(e^{-t}/2) ≈ e^{-t}/2 for large t. So ψ(t) ≈ -e^{-t}/2 → 0 for large t.

So ψ(t) → 0 as t → ∞. And ψ(t) < 0 for all t (since γ maps to negative).

Similarly, consider ψ'(t) = φ ∘ γ (apply γ first, then φ). ψ'(t) = φ(γ(t)) = arcsinh(e^{γ(t)}) = arcsinh(e^{-arcsinh(e^{-t})}).

For t → -∞: γ(t) ≈ t - ln 2, so e^{γ(t)} ≈ e^{t-2}... wait, e^{γ(t)} ≈ e^{t - ln 2} = e^t / 2. Then arcsinh(e^t/2) ≈ e^t/2 → 0. So ψ'(t) → 0 as t → -∞.

So the compositions tend to bring values toward 0. This means iterating φ and γ alternately brings values toward 0, preventing long chains that use both.

Now I think the key insight is:

The F-edges and G-edges together form a graph that is essentially a union of paths, where each path alternates between F-edges and G-edges (or uses only one type). The total number of edges is bounded by the structure of these paths.

Let me think about it as a graph where each node has at most 2 outgoing edges (F-out and G-out) and at most 2 incoming edges (F-in and G-in). The graph is a union of paths and cycles. But we showed there are no cycles (since φ and γ both move in specific directions and their compositions tend toward 0). So the graph is a union of paths.

In a path with k nodes, there are k-1 edges. With 100 nodes, the maximum number of edges in a union of paths is 99 (one path). But wait, each node can have up to 2 outgoing edges, so the graph isn't just a simple path—it's a more general DAG.

Hmm, let me reconsider. The F-edges form chains (each node has at most 1 F-out and 1 F-in), and the G-edges form chains (each node has at most 1 G-out and 1 G-in). Together, a node can have F-out, F-in, G-out, G-in—up to 4 edges. So the combined graph can have up to 200 edges (100 F-edges + 100 G-edges) if every node has both F-out and G-out.

But we showed that a finite set can't be closed under both f and g. So we can't have 100 F-edges and 100 G-edges simultaneously. The question is: what's the maximum of (F-edges + G-edges)?

Let me think about this more carefully. Consider the "rightward" edges from each node: F-out (to f(a)) and G-in (from g^{-1}(a), but this is an incoming edge, not outgoing). Wait, I need to be more careful about direction.

Let me re-define. An F-edge from a to b means b = f(a) (a < b, PA = AB). A G-edge from a to b means b = g(a) (a > b, but wait, g(a) < a, so this goes left). Hmm, but in terms of the triangle, a G-edge from a to b = g(a) means PA = AB where A is at position a and B is at position g(a) < a. So the "apex" is A (at position a).

Actually, I think I should think about it differently. Let me count edges, not worrying about direction.

Each unordered pair {a, b} with a < b can be:
- An S-edge if a = -b
- An F-edge if b = f(a) (equivalently, a = f^{-1}(b))
- A G-edge if a = g(b) (equivalently, b = g^{-1}(a))

And these are generally distinct (except at special points).

Now, the F-edges: each point is the left endpoint of at most 1 F-edge (to f(a)) and the right endpoint of at most 1 F-edge (from f^{-1}(a)). So F-edges form a matching in the "left-to-right" sense—actually a union of chains.

Similarly, G-edges: each point is the right endpoint of at most 1 G-edge (to g(a), which is to the left) and the left endpoint of at most 1 G-edge (from g^{-1}(a), which is to the right). So G-edges also form chains.

Now, the combined F+G graph: each point has at most 1 F-edge going right, 1 F-edge going left (from the chain), 1 G-edge going left, 1 G-edge going right (from the G-chain). So at most 2 edges going right (F-out and G-in) and 2 going left (F-in and G-out). But F-out and G-in are different edges (going to different points, in general).

The total number of F+G edges = (number of F-edges) + (number of G-edges). Each is at most 99. But can both be close to 99?

Let me think about a specific construction. Suppose we use the t-parametrization and try to find a set that's a long chain under φ (F-edges) and also has many γ-edges (G-edges).

If the set is {t_0, φ(t_0), φ²(t_0), ..., φ^{99}(t_0)}, then all 99 F-edges exist. For G-edges, we need γ(t_i) to also be in the set for many i. But γ(t_i) is generally not of the form φ^j(t_0), so G-edges would be rare.

Alternatively, can we find a set that's a chain under both φ and γ? That would require φ(t_i) = t_{i+1} and γ(t_i) = t_{i-1} for all i. This means t_{i+1} = φ(t_i) and t_{i-1} = γ(t_i), so t_{i+1} = φ(t_i) and t_i = φ(t_{i-1}) (from the first relation shifted), and also t_{i-1} = γ(t_i) (from the second). So we need γ(t_i) = t_{i-1} and φ(t_{i-1}) = t_i, i.e., φ(γ(t_i)) = t_i. So we need φ ∘ γ = identity, i.e., φ(γ(t)) = t for all t in the chain.

But φ(γ(t)) = arcsinh(e^{γ(t)}) = arcsinh(e^{-arcsinh(e^{-t})}). For this to equal t, we need e^{-arcsinh(e^{-t})} = sinh(t), i.e., -arcsinh(e^{-t}) = ln(sinh(t) + sqrt(sinh²(t)+1)) = arcsinh(sinh(t)) = t (for t > 0). So we need -arcsinh(e^{-t}) = t, i.e., arcsinh(e^{-t}) = -t, i.e., e^{-t} = sinh(-t) = -sinh(t). But e^{-t} > 0 and -sinh(t) < 0 for t > 0. Contradiction. So φ ∘ γ ≠ identity.

So we can't have a set that's simultaneously a chain under both φ and γ. The F-chains and G-chains are incompatible.

This means there's a tradeoff: more F-edges means fewer G-edges and vice versa. The question is: what's the maximum of F + G?

Let me think about this differently. Consider the "doubly-linked" structure. If a point a has both F-out (to f(a)) and G-out (to g(a)), then a is an "internal" node of both an F-chain and a G-chain. The F-chain goes right from a, and the G-chain goes left from a.

Now, consider the "zigzag" path: start at some point, go right via F, then left via G, then right via F, etc. This is the path a, f(a), g(f(a)), f(g(f(a))), .... We showed this tends toward 0, so it can't be a long path in a finite set.

Alternatively, start at some point, go left via G, then right via F, etc.: a, g(a), f(g(a)), g(f(g(a))), .... This also tends toward 0 (from the other side).

So the "zigzag" paths are short. The long paths must be "straight" (all F or all G).

This suggests that the maximum F + G is achieved by having one long F-chain (99 edges) and no G-edges, or one long G-chain (99 edges) and no F-edges, or some compromise.

But wait, maybe we can do better by having some F-edges and some G-edges that don't interfere. For example, if the F-chain uses points in one region and the G-chain uses points in another region.

Let me think about it. Suppose we split the 100 points into two groups: 50 points forming an F-chain (49 F-edges) and 50 points forming a G-chain (49 G-edges). Total: 98 edges. That's less than 99.

But maybe we can do better by interleaving. Consider a set where some points have F-edges and other points have G-edges, and the two types don't conflict.

Actually, let me reconsider. The F-edges and G-edges don't conflict in the sense that they're different pairs. The issue is whether the set of points can simultaneously support many F-edges and many G-edges.

A point a supports an F-edge if f(a) is in the set. A point a supports a G-edge if g(a) is in the set. These are independent conditions on the set. The question is: can we choose a set of 100 points such that many points have f(a) in the set AND many points have g(a) in the set?

The answer depends on the structure of f and g. Since f maps to (0,∞) and g maps to (-∞,0), the F-edges connect points across the positive/negative divide (or within the positive side), and G-edges similarly.

Hmm, let me think about a specific example. Let h = 1 for simplicity.

f(x) = x + sqrt(x²+1), g(x) = x - sqrt(x²+1) = -1/f(x).

Let's compute some values:
- f(0) = 1, g(0) = -1
- f(1) = 1 + sqrt(2) ≈ 2.414, g(1) = 1 - sqrt(2) ≈ -0.414
- f(-1) = -1 + sqrt(2) ≈ 0.414, g(-1) = -1 - sqrt(2) ≈ -2.414
- f(0.414) ≈ 0.414 + sqrt(0.171+1) = 0.414 + 1.082 = 1.496
- g(0.414) ≈ 0.414 - 1.082 = -0.668

Let me try to build a set with many edges. Start with 0:
- f(0) = 1, g(0) = -1. So {0, 1, -1} has F-edge {0,1} and G-edge {0,-1} and S-edge {-1,1}. That's 3 edges from 3 points.

Now add f(1) = 1+sqrt(2) ≈ 2.414 and g(-1) = -1-sqrt(2) ≈ -2.414:
- F-edge {1, 2.414}, G-edge {-1, -2.414}, S-edge {-2.414, 2.414}.
- Set: {-2.414, -1, 0, 1, 2.414}. Edges: F: {0,1}, {1,2.414}; G: {0,-1}, {-1,-2.414}; S: {-1,1}, {-2.414,2.414}. Total: 6 edges from 5 points.

Continue: f(2.414) = 2.414 + sqrt(5.827+1) = 2.414 + 2.613 = 5.027. g(-2.414) = -2.414 - 2.613 = -5.027.
- F-edge {2.414, 5.027}, G-edge {-2.414, -5.027}, S-edge {-5.027, 5.027}.
- Set: {-5.027, -2.414, -1, 0, 1, 2.414, 5.027}. Edges: F: {0,1}, {1,2.414}, {2.414,5.027}; G: {0,-1}, {-1,-2.414}, {-2.414,-5.027}; S: {-1,1}, {-2.414,2.414}, {-5.027,5.027}. Total: 9 edges from 7 points.

I see a pattern! The set is symmetric about 0: {-a_n, ..., -a_1, 0, a_1, ..., a_n} where a_{i+1} = f(a_i). With 2n+1 points, we get:
- F-edges: {a_i, a_{i+1}} for i = 0, 1, ..., n-1 (where a_0 = 0). That's n F-edges.
- G-edges: {-a_i, -a_{i+1}} for i = 0, 1, ..., n-1. That's n G-edges. (Since g(-a_i) = -f(a_i) = -a_{i+1}.)
- S-edges: {-a_i, a_i} for i = 1, ..., n. That's n S-edges.
- Total: 3n edges from 2n+1 points.

With 100 points, we can't quite get 2n+1 = 100 (since 100 is even). Let me adjust.

If we use 2n+1 points (symmetric set with 0), we get 3n edges. For 100 points, we could use 99 points in this symmetric arrangement (n = 49, giving 147 edges) and 1 extra point somewhere. Or we could use 100 points in a different arrangement.

Wait, but with 100 points, if we use a symmetric set of 100 points (50 positive, 50 negative, no zero), we get:
- F-edges: {a_i, a_{i+1}} for i = 1, ..., 49 (if a_1, ..., a_50 are the positive points with a_{i+1} = f(a_i)). That's 49 F-edges. But wait, we also need f(a_0) = a_1 where a_0 = 0, but 0 is not in the set. So the F-edge from 0 doesn't exist. We only get F-edges among the positive points: {a_i, a_{i+1}} for i = 1, ..., 49, giving 49 F-edges. But actually, f(a_i) = a_{i+1} requires a_{i+1} = f(a_i), and this chain starts from a_1. So we need a_2 = f(a_1), a_3 = f(a_2), etc. That gives 49 F-edges.
- G-edges: similarly, {-a_i, -a_{i+1}} for i = 1, ..., 49, giving 49 G-edges.
- S-edges: {-a_i, a_i} for i = 1, ..., 50, giving 50 S-edges.
- Total: 49 + 49 + 50 = 148 edges.

But wait, can we do better? What if we include 0 and use 99 points symmetrically (n=49, 2n+1=99) plus 1 extra point?

With 99 points: 3·49 = 147 edges. The extra point could add a few more edges. But where to place it?

If we place the extra point at some position x, it could form:
- An F-edge if f(x) is in the set or f^{-1}(x) is in the set.
- A G-edge if g(x) is in the set or g^{-1}(x) is in the set.
- An S-edge if -x is in the set.

If we place x = a_{50} = f(a_{49}) (continuing the F-chain), then:
- F-edge {a_{49}, a_{50}}: +1
- S-edge {-a_{50}, a_{50}}: +1 (if -a_{50} is in the set, but it's not since we only had up to ±a_{49})

Hmm, so the extra point at a_{50} gives F-edge {a_{49}, a_{50}} (+1) but no S-edge (since -a_{50} is not in the set). And G-edge? g(a_{50}) is some negative number, probably not in the set. So +1 edge, total 148.

Alternatively, place x = -a_{50} (symmetric to the above). Then G-edge {-a_{49}, -a_{50}} (+1) and S-edge {a_{50}, -a_{50}}? No, a_{50} is not in the set. So +1 edge, total 148.

What if we place both a_{50} and -a_{50} and remove 0? Then we have 100 points: ±a_1, ..., ±a_{50}. 
- F-edges: {a_i, a_{i+1}} for i=1,...,49: 49 edges.
- G-edges: {-a_i, -a_{i+1}} for i=1,...,49: 49 edges.
- S-edges: {-a_i, a_i} for i=1,...,50: 50 edges.
- Total: 148 edges.

Same as before. Can we do better?

What if we don't use a symmetric set? Let me think about other constructions.

Actually, wait. In the symmetric construction, we're using the fact that g(-a) = -f(a) (which follows from g(-x) = -f(x)). This means the G-chain on the negative side mirrors the F-chain on the positive side. So we get equal numbers of F and G edges, plus S-edges.

But what if we use an asymmetric construction that gets more total edges?

Let me think about the upper bound more carefully.

Each point can be the apex of at most 2 isosceles triangles (PA = AB with B = f(a), and PA = AB with B = g(a)). Wait, but a point can also be part of triangles where it's not the apex. Let me re-examine.

A triangle {P, A, B} is isosceles if:
1. PA = PB (apex P): A and B are symmetric. Each point A is in at most 1 such triangle (paired with -A).
2. PA = AB (apex A): B = f(A) or B = g(A). Each point A is the apex of at most 2 such triangles.
3. PB = AB (apex B): A = f(B) or A = g(B). Each point B is the apex of at most 2 such triangles.

Now, each isosceles triangle has exactly one apex (the vertex where the two equal sides meet), unless it's equilateral (all three sides equal), which is impossible here since P is off the line.

Wait, actually an isosceles triangle has exactly one apex unless it's equilateral. Since equilateral is impossible (P is off the line, so PA = PB = AB would require A and B on the line with PA = PB = AB, but PA = sqrt(a²+h²) and AB = |a-b|, and for PA = PB we need a = -b, then AB = 2|a| and PA = sqrt(a²+h²) = 2|a| requires h² = 3a², which is possible for specific a but not for all). So for most triangles, there's a unique apex.

But some triangles could be isosceles in two different ways (two pairs of equal sides), which would make them equilateral. As noted, this requires h² = 3a², which happens for at most 2 values of a (namely a = ±h/sqrt(3)). So at most 2 triangles are equilateral, and the rest have a unique apex.

For triangles with a unique apex:
- Apex P: at most 50 (one for each symmetric pair).
- Apex on the line (A or B): each of the 100 points is the apex of at most 2 triangles, so at most 200.

But the 200 bound counts each triangle once (by its apex). And the 50 bound counts triangles with apex P. These are disjoint (a triangle can't have two apexes unless equilateral). So the total is at most 50 + 200 = 250, minus the number of equilateral triangles (which are counted twice, once for each apex on the line, and also as apex P).

Wait, I need to be more careful. An equilateral triangle has all three sides equal, so all three vertices are "apexes." But we're counting it as one triangle. In the apex counting:
- It's counted once as apex P (PA = PB).
- It's counted once as apex A (PA = AB).
- It's counted once as apex B (PB = AB).
So it's counted 3 times in the 50 + 200 bound, but should be counted once. So we need to subtract 2 for each equilateral triangle.

But there are at most 2 equilateral triangles (for a = ±h/sqrt(3), with b = ∓h/sqrt(3)). Actually, for a = h/sqrt(3), b = -h/sqrt(3): PA = sqrt(h²/3 + h²) = 2h/sqrt(3), PB = 2h/sqrt(3), AB = 2h/sqrt(3). Yes, equilateral. And for a = -h/sqrt(3), b = h/sqrt(3): same triangle. So there's only 1 equilateral triangle (the pair {h/sqrt(3), -h/sqrt(3)}).

So the upper bound is 50 + 200 - 2 = 248, if there's 1 equilateral triangle. But if the set doesn't include ±h/sqrt(3), there are 0 equilateral triangles, and the bound is 250.

But wait, the 200 bound assumes every point is the apex of 2 triangles, which requires f(a) and g(a) to both be in the set for every a. We showed this is impossible for a finite set. So the actual bound is less than 250.

Let me reconsider. The 200 bound is: each of 100 points is the apex of at most 2 triangles (with equal sides PA = AB). But for a point a to be the apex of 2 triangles, both f(a) and g(a) must be in the set. For a point a to be the apex of 1 triangle, at least one of f(a), g(a) must be in the set.

Let me define:
- n_F = number of points a with f(a) in the set (F-out edges)
- n_G = number of points a with g(a) in the set (G-out edges)
- n_S = number of S-edges = number of pairs {a, -a} with both in the set and a > 0

The total number of isosceles triangles (with apex on the line) = n_F + n_G (each F-out or G-out edge gives one triangle with the apex at the source point). Plus n_S triangles with apex P.

But we need to subtract overlaps: a triangle that is both Type S and Type F/G (the equilateral case). There's at most 1 such triangle.

Also, a triangle could be both Type F and Type G? That would mean PA = AB and PB = AB, so PA = PB, which is Type S. So Type F and Type G overlap only in the equilateral case. So no additional overlaps.

Total = n_F + n_G + n_S - (equilateral overlaps).

Now, n_F ≤ 99 (F-edges form chains, max 99 in one chain of 100).
n_G ≤ 99 (similarly).
n_S ≤ 50.

But n_F + n_G can't be 198 because of the incompatibility of F and G.

Let me think about the maximum of n_F + n_G.

Consider the F-edges and G-edges as a directed graph. Each node has out-degree ≤ 2 (F-out and G-out) and in-degree ≤ 2 (F-in and G-in). The total number of edges is n_F + n_G.

Now, the F-edges form a union of chains (each node has at most 1 F-out and 1 F-in). Similarly for G-edges. The combined graph has each node with out-degree ≤ 2 and in-degree ≤ 2.

The maximum number of edges in a DAG with 100 nodes and max degree 4 is... well, it's at most 200 (from the degree bound). But the specific structure of f and g prevents achieving this.

Let me think about the constraint more carefully. The F-out edge from a goes to f(a), and the G-out edge from a goes to g(a). Now, f(a) > 0 and g(a) < 0. So:
- If a > 0: f(a) > a (F-out goes further right), g(a) < 0 (G-out jumps to negative side).
- If a < 0: f(a) > 0 (F-out jumps to positive side), g(a) < a (G-out goes further left).
- If a = 0: f(0) = h, g(0) = -h.

So for positive points, F-out stays positive and G-out goes negative. For negative points, F-out goes positive and G-out stays negative.

This means:
- F-edges from positive points go to positive points (staying on the positive side).
- F-edges from negative points go to positive points (crossing to the positive side).
- G-edges from positive points go to negative points (crossing to the negative side).
- G-edges from negative points go to negative points (staying on the negative side).

So the F-edges on the positive side form chains among positive points, and F-edges from negative points jump to the positive side. Similarly, G-edges on the negative side form chains among negative points, and G-edges from positive points jump to the negative side.

Now, consider the positive points. Among k positive points, the F-edges form chains (each positive point has at most 1 F-out to another positive point, and at most 1 F-in from another positive point or from a negative point). The G-edges from positive points go to negative points, so they don't contribute to edges among positive points.

Similarly, among the negative points, G-edges form chains, and F-edges from negative points go to positive points.

Let me denote:
- p = number of positive points
- q = number of negative points
- z = number of zeros (0 or 1)
- p + q + z = 100

F-edges:
- Among positive points: at most p - 1 (if they form one chain). But actually, the F-edges among positive points form chains, and the max is p - 1 (one chain) plus possibly F-edges from negative points to positive points.
- From negative points to positive points: at most q (each negative point has at most 1 F-out, going to a positive point). But the target must be in the set.
- From zero to positive: at most 1 (if 0 is in the set, f(0) = h must be in the set).

Wait, I need to think about this more carefully. The F-edges form chains. A chain can start from a negative point (F-out goes to positive), then continue among positive points (F-out stays positive). So a single F-chain can include both negative and positive points.

Let me think about the F-chains. An F-chain is a sequence a_1, a_2, ..., a_k where f(a_i) = a_{i+1}. Since f maps everything to positive, a_2, a_3, ..., a_k are all positive. a_1 can be anything (positive, negative, or zero). So each F-chain has at most 1 non-positive point (the first one) and the rest are positive.

If we have p positive points and q negative points and z zeros, the F-chains can include at most q + z non-positive starting points and p positive points. Each chain has at most 1 non-positive point. So we can have at most q + z chains, each using 1 non-positive point and some positive points. The total number of positive points used is at most p, and the total F-edges is (total points in chains) - (number of chains) = (p + q + z used) - (number of chains).

Hmm, this is getting complicated. Let me think about it differently.

The F-edges form a forest of directed paths. Each path has at most 1 non-positive node (the first node). The remaining nodes are positive. So the number of paths is at most q + z (the number of non-positive nodes), and the total nodes in all paths is at most 100. The total F-edges = total nodes - number of paths ≤ 100 - 1 = 99 (if there's only 1 path, starting from 1 non-positive node).

But if we have many non-positive nodes, each must start its own path, so the number of paths is at least the number of non-positive nodes that have F-edges. If all q + z non-positive nodes have F-edges, we have at least q + z paths, and the total F-edges ≤ 100 - (q + z).

Similarly, G-edges form paths, each with at most 1 non-negative node (the first one, since g maps to negative). The number of G-paths is at most p + z, and total G-edges ≤ 100 - (p + z) = q.

Wait, let me re-examine. G-edges: g maps everything to negative. So a G-chain a_1, a_2, ..., a_k with g(a_i) = a_{i+1} has a_2, ..., a_k all negative. a_1 can be anything. So each G-chain has at most 1 non-negative node.

If we have p positive nodes and z zeros, the number of G-chains is at most p + z (each starting from a non-negative node). Total G-edges ≤ 100 - (number of G-chains) ≥ ... well, to maximize G-edges, minimize the number of chains, which is 1 (if only 1 non-negative node has a G-edge). But if all p + z non-negative nodes have G-edges, we have p + z chains, and G-edges ≤ 100 - (p + z) = q.

Hmm wait, that's not right either. The G-chains use nodes from the set. If a G-chain starts from a positive node and goes to negative nodes, it uses 1 positive node and some negative nodes. The total nodes used across all G-chains is at most 100. The number of chains is the number of non-negative nodes that have G-out edges. If all p + z non-negative nodes have G-out edges, there are p + z chains, using at most 100 nodes total, so G-edges = 100 - (p + z) = q. But this requires all q negative nodes to be in G-chains, and each chain uses 1 non-negative node and some negative nodes.

Actually, I think the constraint is:
- F-edges: at most 100 - (number of F-chains). Number of F-chains ≥ (number of non-positive nodes with F-out edges). To maximize F-edges, minimize chains. If no non-positive node has an F-out edge, all F-chains are among positive nodes, and the number of chains is (number of positive nodes) - (F-edges among positive nodes). Hmm, this is circular.

Let me think about it more simply.

F-edges: The F-edges form a union of directed paths. In a union of directed paths with n nodes and c connected components (paths), the number of edges is n - c. To maximize edges, minimize c. The minimum c is 1 (one path), giving n - 1 = 99 edges. But the path must be a valid F-chain: a, f(a), f²(a), ..., f^{99}(a). This is always possible (just pick any a and iterate f 99 times). So n_F ≤ 99.

Similarly, n_G ≤ 99.

But can n_F + n_G be large? The constraint is that the F-edges and G-edges share the same set of 100 points.

Let me think about the tradeoff. Suppose we have n_F F-edges. These use some of the 100 points in F-chains. The remaining points (not in any F-chain, or in F-chains but with available G-edges) can have G-edges.

Actually, every point is potentially in both an F-chain and a G-chain. The F-chain and G-chain are independent. A point a can have F-out to f(a) and G-out to g(a), and these are different points (in general). So the F-edges and G-edges are independent edge sets on the same vertex set.

The question is: for a given set of 100 points, what is n_F + n_G?

n_F = |{a ∈ S : f(a) ∈ S}|, n_G = |{a ∈ S : g(a) ∈ S}|.

We want to choose S (|S| = 100) to maximize n_F + n_G + n_S.

Let me think about the symmetric construction again. S = {±a_1, ±a_2, ..., ±a_50} where a_{i+1} = f(a_i) for i = 1, ..., 49.

n_F: For positive points a_i, f(a_i) = a_{i+1} ∈ S for i = 1, ..., 49. That's 49. For negative points -a_i, f(-a_i) = -g(a_i) = -(-a_{i+1}) = a_{i+1}... wait, let me recompute. f(-a_i) = -a_i + sqrt(a_i² + h²). And g(a_i) = a_i - sqrt(a_i² + h²) = -a_{i+1}... no. g(a_i) = a_i - sqrt(a_i² + h²). And a_{i+1} = f(a_i) = a_i + sqrt(a_i² + h²). So sqrt(a_i² + h²) = a_{i+1} - a_i. Then g(a_i) = a_i - (a_{i+1} - a_i) = 2a_i - a_{i+1}. Hmm, that doesn't simplify to -a_{i+1} in general.

Wait, I think I made an error earlier. Let me recompute. g(-x) = -x - sqrt(x² + h²) = -(x + sqrt(x² + h²)) = -f(x). So g(-a_i) = -f(a_i) = -a_{i+1}. So the G-edge from -a_i goes to -a_{i+1}. ✓

And f(-a_i) = -a_i + sqrt(a_i² + h²) = -a_i + (a_{i+1} - a_i) = a_{i+1} - 2a_i. This is not necessarily in S.

So for the symmetric set S = {±a_1, ..., ±a_50}:
- F-edges from positive points: f(a_i) = a_{i+1} for i = 1, ..., 49. That's 49 F-edges.
- F-edges from negative points: f(-a_i) = a_{i+1} - 2a_i. This is generally not in S. So 0 F-edges from negative points (unless a_{i+1} - 2a_i happens to equal some a_j or -a_j, which is unlikely in general).

Wait, but f(-a_i) = -g(a_i) (since f(-x) = -g(x)). And g(a_i) = a_i - sqrt(a_i² + h²). If a_{i+1} = f(a_i) = a_i + sqrt(a_i² + h²), then sqrt(a_i² + h²) = a_{i+1} - a_i, so g(a_i) = a_i - (a_{i+1} - a_i) = 2a_i - a_{i+1}. And f(-a_i) = -g(a_i) = a_{i+1} - 2a_i.

For f(-a_i) to be in S, we need a_{i+1} - 2a_i ∈ {±a_1, ..., ±a_50}. In general, this won't hold.

So n_F = 49 (only from positive points) in the symmetric construction.

Similarly, n_G: G-edges from negative points: g(-a_i) = -a_{i+1} for i = 1, ..., 49. That's 49 G-edges. G-edges from positive points: g(a_i) = 2a_i - a_{i+1}, generally not in S. So n_G = 49.

n_S = 50 (pairs {a_i, -a_i} for i = 1, ..., 50).

Total: 49 + 49 + 50 = 148.

Can we do better? Let me think about including 0 in the set.

S = {0, ±a_1, ..., ±a_49} (99 points) plus one more point. With 0:
- f(0) = h. If h = a_1, then F-edge {0, a_1}. Similarly g(0) = -h = -a_1, G-edge {0, -a_1}.
- F-edges from positive: {a_i, a_{i+1}} for i = 1, ..., 48. 48 edges. Plus {0, a_1}: 49 F-edges.
- G-edges from negative: {-a_i, -a_{i+1}} for i = 1, ..., 48. 48 edges. Plus {0, -a_1}: 49 G-edges.
- S-edges: {a_i, -a_i} for i = 1, ..., 49. 49 edges. (0 is not paired with anything.)
- Total: 49 + 49 + 49 = 147 from 99 points.

With the 100th point, we can add at most a few edges. If we add a_50 = f(a_49):
- F-edge {a_49, a_50}: +1.
- S-edge {-a_50, a_50}? -a_50 is not in S. So no.
- G-edge from a_50? g(a_50) probably not in S.
- Total: 147 + 1 = 148.

If instead we add -a_50 = g(-a_49):
- G-edge {-a_49, -a_50}: +1.
- Total: 147 + 1 = 148.

If we add both a_50 and -a_50 and remove 0: S = {±a_1, ..., ±a_50}, 100 points.
- F-edges: {a_i, a_{i+1}} for i=1,...,49: 49.
- G-edges: {-a_i, -a_{i+1}} for i=1,...,49: 49.
- S-edges: 50.
- Total: 148.

So the symmetric construction gives 148. Can we beat this?

Let me think about asymmetric constructions. What if we don't require symmetry?

Consider a set that's a single long F-chain: {a, f(a), f²(a), ..., f^{99}(a)}. This gives 99 F-edges. G-edges: for each point in the chain, g(point) is generally not in the chain. So n_G ≈ 0. S-edges: if the chain happens to contain symmetric pairs, but generally it won't. So total ≈ 99.

That's much worse than 148.

What about a mixed construction? Let me think about what happens if we have p positive points forming an F-chain and q negative points forming a G-chain, with p + q = 100.

F-edges: p - 1 (from the F-chain among positive points) + possibly some F-edges from negative points to positive points.
G-edges: q - 1 (from the G-chain among negative points) + possibly some G-edges from positive points to negative points.
S-edges: however many symmetric pairs exist.

If the positive and negative points are not related by symmetry, S-edges = 0. Total: (p-1) + (q-1) = 98. Worse than 148.

If we add symmetry: positive points are a_1, ..., a_p and negative points are -a_1, ..., -a_q with p = q = 50. Then:
- F-edges: 49 (among positive) + F-edges from negative points.
- G-edges: 49 (among negative) + G-edges from positive points.
- S-edges: 50 (if p = q = 50 and the sets are symmetric).
- F-edges from negative: f(-a_i) = -g(a_i). For this to be in S (i.e., in {a_1, ..., a_50} or {-a_1, ..., -a_50}), we need -g(a_i) = a_j or -g(a_i) = -a_j. Since -g(a_i) > 0 (because g(a_i) < 0), we need -g(a_i) = a_j, i.e., g(a_i) = -a_j. But g(a_i) = 2a_i - a_{i+1} (where a_{i+1} = f(a_i)). So 2a_i - a_{i+1} = -a_j, i.e., a_{i+1} = 2a_i + a_j. This is a specific condition that might hold for some i, j but not in general.

So in the symmetric construction, we get 49 + 49 + 50 = 148, and possibly a few more from cross-edges (F from negative, G from positive) if the positions align.

Can we choose the positions to make some cross-edges work? Let me think.

We want g(a_i) = -a_j for some i, j, i.e., 2a_i - a_{i+1} = -a_j, i.e., a_{i+1} = 2a_i + a_j. Since a_{i+1} = f(a_i) is determined by a_i (and h), this is a constraint on the a values.

Actually, the a values are determined by the F-chain: a_{i+1} = f(a_i). So a_1 is free, and a_2 = f(a_1), a_3 = f(a_2), etc. The condition a_{i+1} = 2a_i + a_j becomes f(a_i) = 2a_i + a_j, i.e., a_i + sqrt(a_i² + h²) = 2a_i + a_j, i.e., sqrt(a_i² + h²) = a_i + a_j, i.e., a_i² + h² = a_i² + 2a_i·a_j + a_j², i.e., h² = 2a_i·a_j + a_j², i.e., a_j² + 2a_i·a_j - h² = 0, i.e., a_j = (-2a_i ± sqrt(4a_i² + 4h²))/2 = -a_i ± sqrt(a_i² + h²) = -a_i ± (a_{i+1} - a_i).

So a_j = -a_i + (a_{i+1} - a_i) = a_{i+1} - 2a_i, or a_j = -a_i - (a_{i+1} - a_i) = -a_{i+1}.

The second solution: a_j = -a_{i+1}. But a_j > 0 and a_{i+1} > 0, so a_j = -a_{i+1} < 0. Contradiction. So only the first solution: a_j = a_{i+1} - 2a_i.

For this to be a valid positive point in our set, we need a_j = a_{i+1} - 2a_i > 0, i.e., a_{i+1} > 2a_i, i.e., f(a_i) > 2a_i, i.e., a_i + sqrt(a_i² + h²) > 2a_i, i.e., sqrt(a_i² + h²) > a_i, which is always true. So a_j = a_{i+1} - 2a_i > 0 always. But we need a_j to be one of our existing points a_1, ..., a_50.

So the cross-edge condition is: a_{i+1} - 2a_i = a_j for some j. This means g(a_i) = -(a_{i+1} - 2a_i) = -a_j, so the G-edge from a_i goes to -a_j, which is in our set. This gives an additional G-edge.

But a_j = a_{i+1} - 2a_i is a specific value determined by a_i and a_{i+1}. For it to be in our set, it must equal one of the a_k values. Since the a_k values are determined by the F-chain (a_{k+1} = f(a_k)), this is a constraint on a_1 (the starting point of the chain).

This seems hard to satisfy for many i values simultaneously. Let me think about whether we can choose a_1 to satisfy multiple such conditions.

Actually, let me think about this problem from a higher level. The answer 148 from the symmetric construction seems good, but maybe there's a better construction.

Let me reconsider the upper bound. We have:
- n_F + n_G + n_S - (overlaps) ≤ n_F + n_G + n_S

And n_F + n_G ≤ ? (the key constraint).

Let me think about n_F + n_G differently. Each point a contributes 1 to n_F if f(a) ∈ S, and 1 to n_G if g(a) ∈ S. So n_F + n_G = |{a ∈ S : f(a) ∈ S}| + |{a ∈ S : g(a) ∈ S}|.

Now, f(a) ∈ S means a is the "predecessor" in an F-chain. g(a) ∈ S means a is the "predecessor" in a G-chain. 

Consider the map F: S → S defined by F(a) = f(a) if f(a) ∈ S, undefined otherwise. This is a partial function. Similarly G(a) = g(a) if g(a) ∈ S.

The number of F-edges is the number of points where F is defined, and similarly for G.

Now, consider the "rightward" edges from each point. A point a has:
- F(a) = f(a) if f(a) ∈ S (rightward, since f(a) > a)
- G^{-1}(a) = g^{-1}(a) if g^{-1}(a) ∈ S (rightward, since g^{-1}(a) > a)

These are two different rightward edges (to different points, in general). Similarly, two leftward edges.

The total number of rightward edges = n_F + (number of points with G-in edges). The number of G-in edges equals n_G (since each G-edge has one source and one target, so the number of G-in edges = number of G-out edges = n_G). So total rightward edges = n_F + n_G.

Similarly, total leftward edges = n_F + n_G (by symmetry of counting).

Now, the rightward edges go from each point to a point further right. Consider the points ordered x_1 < x_2 < ... < x_100. A rightward edge from x_i goes to x_j with j > i. Each point x_i has at most 2 rightward edges (F-out and G-in). So the total number of rightward edges is at most 2 · 100 = 200, but also at most the number of pairs (i, j) with i < j, which is C(100, 2) = 4950. The binding constraint is 200.

But we also have the constraint that F-out and G-in from the same point go to different points (in general). So the 2 rightward edges from each point go to 2 different points. This means the rightward edges form a graph where each node has out-degree ≤ 2 and in-degree ≤ 2 (since each point can be the target of at most 1 F-edge and at most 1 G-edge). This is a union of paths and cycles in a directed graph with max degree 4.

But we showed there are no cycles. So it's a union of paths. With 100 nodes, the maximum number of edges in a union of paths is 99 (one path). But with max out-degree 2 and max in-degree 2, we can have a "thicker" structure.

Wait, a directed graph with max out-degree 2 and max in-degree 2, and no cycles, can have up to 2 · 100 - 2 = 198 edges? No, that's not right. In a DAG with n nodes, the maximum number of edges is n(n-1)/2 (complete DAG). But with max degree constraints, it's different.

Actually, in a directed graph with max out-degree d_out and max in-degree d_in, the maximum number of edges is min(n · d_out, n · d_in). Here, d_out = d_in = 2, so max edges = 200. But we also need the graph to be a DAG (no cycles), which is automatically satisfied since all edges go rightward.

So the maximum number of rightward edges is 200, achieved when every point has 2 rightward edges (F-out and G-in) and 2 leftward edges (F-in and G-out). But this requires every point to have both f(a) ∈ S and g^{-1}(a) ∈ S, which means S is closed under f and under g^{-1}. Since g^{-1}(a) = f(-a)·... hmm, let me think.

g^{-1}: if b = g(a) = a - sqrt(a² + h²), then a = ? We need to solve for a: b = a - sqrt(a² + h²), so sqrt(a² + h²) = a - b, so a² + h² = a² - 2ab + b², so h² = b² - 2ab, so a = (b² - h²)/(2b) (for b ≠ 0). So g^{-1}(b) = (b² - h²)/(2b) = b/2 - h²/(2b).

And f(a) = a + sqrt(a² + h²). f^{-1}(b) = (b² - h²)/(2b) as well? Let me check: if b = f(a) = a + sqrt(a² + h²), then sqrt(a² + h²) = b - a, so a² + h² = b² - 2ab + a², so h² = b² - 2ab, so a = (b² - h²)/(2b). Yes, f^{-1}(b) = (b² - h²)/(2b) = g^{-1}(b).

Wait, that can't be right. f and g are different functions, so their inverses should be different.

Let me recheck. f(a) = a + sqrt(a² + h²). If b = f(a), then b - a = sqrt(a² + h²) > 0, so b > a. And a = (b² - h²)/(2b).

g(a) = a - sqrt(a² + h²). If b = g(a), then a - b = sqrt(a² + h²) > 0, so a > b. And a = (b² - h²)/(2b).

So f^{-1}(b) = (b² - h²)/(2b) and g^{-1}(b) = (b² - h²)/(2b). They're the same! That makes sense because f and g are related: f(a) = a + sqrt(a² + h²) and g(a) = a - sqrt(a² + h²). If b = f(a), then a = f^{-1}(b). If b = g(a), then a = g^{-1}(b). And in both cases, a = (b² - h²)/(2b).

But wait, f maps ℝ to (0, ∞) and g maps ℝ to (-∞, 0). So f^{-1} is defined on (0, ∞) and g^{-1} is defined on (-∞, 0). They're the same formula but defined on different domains. So f^{-1}(b) for b > 0 gives the unique a with f(a) = b, and g^{-1}(b) for b < 0 gives the unique a with g(a) = b.

So the "F-in" edge to a point b > 0 comes from f^{-1
