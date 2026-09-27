# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
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
  <problem_id>oda_math_460k_00004483</problem_id>
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

Three mowers mow grass from three hectares in three days. How much area will five mowers mow in five days?

## Standard Solution

<think>Okay, let's try to figure out this problem. So, the question is: Three mowers mow grass from three hectares in three days. How much area will five mowers mow in five days? Hmm, I need to find out the rate at which each mower works and then scale it up for more mowers and more days. Let's start by breaking it down.

First, let's understand the given information. Three mowers take three days to mow three hectares. Let's denote the work rate of one mower as r hectares per day. So, if one mower mows r hectares in one day, then three mowers would mow 3r hectares per day. 

Now, they work for three days. So the total work done by three mowers in three days is (3r) * 3 days. According to the problem, this equals three hectares. Let's write that as an equation:

3r * 3 = 3

Wait, let's check that. The total work (hectares) is equal to the number of mowers multiplied by their rate per mower per day multiplied by the number of days. So, total hectares = (number of mowers) * (rate per mower per day) * (days). 

So, 3 hectares = 3 mowers * r * 3 days. Let's compute that: 3 = 3 * r * 3. So 3 = 9r. Then, solving for r, we get r = 3/9 = 1/3. So each mower mows 1/3 of a hectare per day. That makes sense. Let me verify: 3 mowers, each mowing 1/3 per day, so together they mow 1 hectare per day. Over 3 days, that's 3 hectares. Yep, that matches the problem statement. Good.

Now, the question is, how much area will five mowers mow in five days? Let's use the same formula. Total hectares = (number of mowers) * (rate per mower per day) * (days). We already found the rate r is 1/3 hectare per mower per day.

So, plugging in the numbers: 5 mowers * (1/3 hectare/mower/day) * 5 days. Let's compute that. 5 * (1/3) * 5 = 25/3. Wait, 25 divided by 3 is approximately 8.333... But let's make sure. Let's check again.

Each mower's rate is 1/3 per day. So one mower in 5 days would mow (1/3)*5 = 5/3 hectares. Then five mowers would be 5*(5/3) = 25/3. That's the same as before. So 25/3 hectares. Let me confirm with the formula again. Total work = mowers * rate * days. So 5 * (1/3) * 5 = 25/3. Yep, that's correct. So the answer should be 25/3 hectares, which is approximately 8.333..., but as a fraction, it's 25/3. So the box should have \boxed{\dfrac{25}{3}}.
</think>

To solve the problem, we first determine the work rate of one mower. 

Given that 3 mowers mow 3 hectares in 3 days, we denote the work rate of one mower as \( r \) hectares per day. 

The total work done by 3 mowers in 3 days is calculated as:
\[
\text{Total work} = \text{Number of mowers} \times \text{Rate per mower per day} \times \text{Days}
\]
Substituting the given values:
\[
3 \text{ hectares} = 3 \times r \times 3
\]
Solving for \( r \):
\[
3 = 9r \implies r = \frac{3}{9} = \frac{1}{3} \text{ hectares per mower per day}
\]

Next, we calculate the area mowed by 5 mowers in 5 days using the same rate \( r \):
\[
\text{Total work} = 5 \times \frac{1}{3} \times 5
\]
\[
\text{Total work} = \frac{25}{3} \text{ hectares}
\]

Thus, the final answer is \(\boxed{\dfrac{25}{3}}\).

## AI's Thinking (Attempted Solution Process)

The problem asks about necessary and sufficient conditions for a strategy p to be an ESS in the war of attrition game. This is a standard game theory / evolutionary biology question. Let me think through it.

The war of attrition game: two players choose a "bid" or "persistence time" t ≥ 0. The player with the higher bid wins the resource of value V, and both players pay a cost equal to the lower bid (or in some formulations, both pay their own bid). Let me recall the standard formulation.

Standard war of attrition: Each player chooses a time t. The player with the larger t wins the prize V. Both players pay a cost equal to the smaller of the two times (since the contest ends when one gives up, at time min(t1, t2)). Actually there are variants. Let me use the standard Bishop-Cannings formulation.

In the standard war of attrition (Bishop & Cannings 1978): Players choose persistence times x ≥ 0. If x_i > x_j, player i wins resource V and pays cost x_j (the time the opponent persisted, which equals the contest duration). Player j pays cost x_j as well. If x_i = x_j, they split or each gets V/2 and pay x_i.

So payoff to player choosing x against opponent choosing y:
- If x > y: V - y
- If x < y: -x
- If x = y: V/2 - x

A strategy here is a mixed strategy (a probability distribution over persistence times). Let p be a mixed strategy with CDF F and density f.

The ESS condition (Maynard Smith): p is an ESS if for every other strategy q ≠ p:
1. E(p, p) ≥ E(q, p) (equilibrium condition), and
2. If E(p, p) = E(q, p), then E(p, q) > E(q, q) (strict superiority against the mutant when facing the mutant).

For the war of attrition, the unique ESS is the mixed strategy with CDF F(x) = 1 - exp(-x/V) for x ≥ 0, i.e., exponential distribution with mean V. This is the well-known result.

But the question asks for "necessary and sufficient conditions for a strategy p to be an ESS" in the war of attrition. This is asking for the characterization.

Let me think about the general characterization. The Bishop-Cannings theorem (1978) gives the ESS for the war of attrition.

The key result: A mixed strategy p with support [0, ∞) and CDF F is an ESS if and only if:
1. The support of p is an interval (connected).
2. For all x in the support of p, E(x, p) = constant = E(p, p) (equal payoff condition - every pure strategy in the support gets the same expected payoff against p).
3. For all x not in the support, E(x, p) ≤ E(p, p).
4. The second ESS condition holds.

Actually, let me be more careful. The Bishop-Cannings theorem states:

For the war of attrition with prize V and continuous strategy space [0, ∞):

A mixed strategy p is an ESS if and only if:
(i) p has no atoms (is a continuous distribution),
(ii) The support S of p is a connected set (an interval),
(iii) For all x in S: E(x, p) = E(p, p) (the "equalization" property),
(iv) For all x ∉ S: E(x, p) ≤ E(p, p),
(v) The second condition of the ESS definition is satisfied.

And the unique solution to these conditions is the exponential distribution F(x) = 1 - e^{-x/V}.

Hmm, but actually the question might be asking more generally. Let me reconsider.

Actually, I think the question is asking for the general ESS characterization conditions. Let me think about what the "necessary and sufficient conditions" are.

The standard answer for the war of attrition ESS:

A strategy p (a probability distribution over [0,∞)) is an ESS of the war of attrition if and only if:

1. **Equal payoff on support**: Every pure strategy in the support of p earns the same expected payoff against p, and this equals E(p,p). That is, E(x, p) = E(p, p) for all x ∈ supp(p).

2. **No better response outside support**: No pure strategy outside the support of p earns more than E(p, p) against p. That is, E(x, p) ≤ E(p, p) for all x ∉ supp(p).

3. **Second ESS condition**: For any mutant strategy q ≠ p with E(q, p) = E(p, p), we have E(p, q) > E(q, q).

And the Bishop-Cannings result shows that the unique strategy satisfying these conditions is the exponential distribution with mean V.

Let me write up a proper proof.

Let me define the game precisely and work through it.

**The War of Attrition Game:**

- Strategy space: [0, ∞), representing persistence time.
- Payoff to player choosing x against opponent choosing y:
  - If x > y: V - y (win the prize, pay cost equal to contest duration y)
  - If x < y: -x (lose, pay cost equal to own persistence time x = contest duration)
  - If x = y: V/2 - x (tie, split prize, pay cost x)

For mixed strategies p, q with CDFs F, G:

E(p, q) = ∫∫ payoff(x, y) dF(x) dG(y)

**ESS Definition (Maynard Smith):**

p is an ESS if for all q ≠ p:
- Either E(p, p) > E(q, p), or
- E(p, p) = E(q, p) and E(p, q) > E(q, q).

**Bishop-Cannings Theorem (1978):**

For the war of attrition, a mixed strategy p is an ESS if and only if it satisfies the following conditions:

**Necessary and sufficient conditions:**

(C1) **Continuous distribution (no atoms)**: p has no point masses. The CDF F is continuous.

(C2) **Connected support**: The support S = supp(p) is a connected subset of [0, ∞), i.e., an interval [a, b] (possibly [0, ∞)).

(C3) **Equalization condition**: For all x ∈ S, E(x, p) = E(p, p). Every pure strategy in the support earns the same expected payoff against p as p earns against itself.

(C4) **No profitable deviation outside support**: For all x ∉ S, E(x, p) ≤ E(p, p).

(C5) **Second-order condition (strict inequality for ties)**: For any q ≠ p such that E(q, p) = E(p, p), E(p, q) > E(q, q).

**The unique ESS**: The unique strategy satisfying (C1)-(C5) is the exponential distribution F(x) = 1 - exp(-x/V) for x ≥ 0, with E(p, p) = 0.

Now let me prove this properly.

**Proof:**

**Part I: Necessity.** Suppose p is an ESS. We show (C1)-(C5).

(C5) is immediate from the ESS definition.

For (C3): Suppose there exist x₁, x₂ ∈ S with E(x₁, p) > E(x₂, p). Then a mutant playing x₁ would do strictly better against p than p does against itself (since E(p,p) is a weighted average of E(x, p) over x ∈ S, it's ≤ max E(x,p) = E(x₁,p) with strict inequality if E(x₁,p) > E(x₂,p) for some x₂ in support). This contradicts the first ESS condition E(p,p) ≥ E(q,p) for all q. Hence E(x, p) must be constant on S, and this constant equals E(p, p) = ∫_S E(x,p) dF(x).

For (C4): If some x₀ ∉ S has E(x₀, p) > E(p, p), then the pure strategy x₀ is a better response to p than p itself, contradicting E(p,p) ≥ E(q,p). So E(x, p) ≤ E(p, p) for x ∉ S.

For (C1): Suppose p has an atom at some point x₀, i.e., F has a jump at x₀. Consider the payoff function E(x, p) as a function of x. In the war of attrition, if the opponent plays p with an atom at x₀, then a player choosing x slightly above x₀ gets a discrete jump in winning probability (jumps from P(opponent plays ≤ x₀⁻) to P(opponent plays ≤ x₀)) while paying only slightly more cost. This creates a discontinuity: E(x₀⁺, p) > E(x₀, p). So E(x, p) is not constant in any neighborhood of x₀, contradicting (C3) if x₀ ∈ S. If x₀ is an isolated point of S, then... Actually, the atom creates a situation where strategies just above x₀ strictly dominate x₀ against p, so x₀ cannot be in the support (since E(x₀⁺, p) > E(x₀, p) = E(p,p), violating equalization). This is a contradiction since x₀ is in the support. Hence p has no atoms.

For (C2): Suppose S is not connected, so S = S₁ ∪ S₂ with a gap (a, b) between them (a < b, a ∈ S₁, b ∈ S₂, (a,b) ∩ S = ∅). Consider x in the gap (a, b). We need E(x, p) ≤ E(p, p) by (C4). But we can show that in the war of attrition, E(x, p) as a function of x is continuous (since p has no atoms by C1) and equals E(p,p) at both a and b (by C3). We need to check whether E(x, p) can dip below E(p,p) in the gap. Actually, let me think about the structure of E(x, p).

Let me compute E(x, p) explicitly. Let F be the CDF of p (continuous, no atoms).

E(x, p) = ∫₀ˣ (V - y) dF(y) + ∫_x^∞ (-x) dF(y) + [V/2 - x]·0 (no atom at x since F continuous)

Wait, let me be careful. For pure strategy x against mixed p:

E(x, p) = ∫₀^∞ payoff(x, y) dF(y)

= ∫₀ˣ (V - y) dF(y) + ∫_x^∞ (-x) dF(y) + (V/2 - x)·P(Y = x)

Since F is continuous, P(Y = x) = 0, so:

E(x, p) = ∫₀ˣ (V - y) dF(y) - x·(1 - F(x))

= V·F(x) - ∫₀ˣ y dF(y) - x·(1 - F(x))

Let me define H(x) = ∫₀ˣ y dF(y). Then:

E(x, p) = V·F(x) - H(x) - x·(1 - F(x))

= V·F(x) - H(x) - x + x·F(x)

= (V + x)·F(x) - H(x) - x

Now, the equalization condition (C3) says E(x, p) = c (constant) for x ∈ S.

Taking the derivative with respect to x (where F and H are differentiable, i.e., where f = F' exists):

dE/dx = (V + x)·f(x) + F(x) - x·f(x) - 1

= V·f(x) + F(x) - 1

Setting this to 0 for x in the interior of S:

V·f(x) + F(x) - 1 = 0

This gives the differential equation:

f(x) = (1 - F(x))/V

i.e., F'(x) = (1 - F(x))/V

With boundary condition F(0) = 0 (if 0 is in the support) or appropriate conditions.

The solution is F(x) = 1 - exp(-x/V), the exponential distribution.

Now, for the support being connected: Suppose S is not connected. Then there's a gap (a, b) ⊂ Sᶜ with a, b ∈ S. In the gap, E(x, p) ≤ c (by C4). But E(a, p) = c and E(b, p) = c. Let's look at dE/dx in the gap. In the gap, f(x) = 0 (no mass in the gap), so:

dE/dx = V·0 + F(x) - 1 = F(x) - 1

Since F(x) < 1 for finite x (assuming the support extends beyond b), dE/dx < 0 in the gap. So E(x, p) is strictly decreasing in the gap. But E(a, p) = c and E is decreasing, so E(x, p) < c for x ∈ (a, b), and then at b, E(b, p) = c. But E is continuous (no atoms) and decreasing on (a,b), so E(b⁻, p) < c = E(b, p). This means E jumps up at b, which requires either an atom at b (contradicting C1) or... Actually E is continuous since F is continuous. So E(b⁻, p) = E(b, p) = c. But E is strictly decreasing on (a, b) with E(a) = c, so E(b⁻) < c, contradiction with E(b) = c.

Wait, that's the contradiction. If E is continuous and strictly decreasing on (a, b) with E(a) = c, then E(b) < c, contradicting E(b) = c.

So the support must be connected. This proves (C2).

Actually, I need to be a bit more careful. The derivative dE/dx = F(x) - 1 in the gap only holds if F is constant in the gap (which it is, since no mass there) and F(x) < 1. If F(x) = 1 for all x in the gap, that means all mass is below a, so b is not in the support, contradiction. So F(x) < 1 in the gap, dE/dx < 0, E strictly decreasing, contradiction with E(a) = E(b) = c.

Good, so (C2) is proven.

**Part II: Sufficiency.** Suppose p satisfies (C1)-(C5). We show p is an ESS.

From (C3) and (C4): For all pure strategies x, E(x, p) ≤ E(p, p), with equality for x ∈ S. For any mixed strategy q:

E(q, p) = ∫ E(x, p) dG(x) ≤ ∫ E(p, p) dG(x) = E(p, p)

So the first ESS condition E(p, p) ≥ E(q, p) holds for all q.

If E(q, p) < E(p, p), we're done (first case of ESS).

If E(q, p) = E(p, p), then by (C5), E(p, q) > E(q, q). This is the second ESS condition.

Hence p is an ESS. □

**Part III: The unique ESS is the exponential distribution.**

From the differential equation V·f(x) + F(x) - 1 = 0 on the support, with the support being a connected interval starting at some point a ≥ 0:

If a = 0: F(0) = 0, and the solution is F(x) = 1 - e^{-x/V} for x ≥ 0, with support [0, ∞).

If a > 0: We need F(a) = 0 (start of support) and E(a, p) = c. At x = a, E(a, p) = (V+a)·F(a) - H(a) - a = (V+a)·0 - 0 - a = -a. So c = -a < 0. But also, for x = 0 (which is outside the support if a > 0), E(0, p) = V·F(0) - H(0) - 0 = 0. By (C4), E(0, p) ≤ c = -a < 0. But E(0, p) = 0 > -a, contradiction. So a = 0.

Now with a = 0, the support is [0, b] for some b ≤ ∞. The solution F(x) = 1 - e^{-x/V} on [0, b]. At x = b (if b < ∞), F(b) = 1 - e^{-b/V} < 1, so there's mass above b, meaning b is not the end of support. Contradiction unless b = ∞.

So the unique ESS is F(x) = 1 - e^{-x/V} for x ≥ 0, the exponential distribution with mean V.

Let me also verify E(p, p) = 0 for this distribution:

E(p, p) = c = E(0, p) = V·F(0) - H(0) - 0 = 0. ✓

And verify the second ESS condition. For any q ≠ p with E(q, p) = 0 (i.e., q only uses strategies in the support of p, since E(x,p) = 0 only for x in [0,∞) = supp(p)... wait, actually E(x, p) = 0 for all x ≥ 0 with the exponential, since every x ≥ 0 is in the support.

Hmm, so for the exponential distribution, E(x, p) = 0 for all x ≥ 0, meaning every pure strategy is a best response. So any q satisfies E(q, p) = 0 = E(p, p). We need to check E(p, q) > E(q, q) for all q ≠ p.

This is the key part of the Bishop-Cannings theorem. Let me think about this.

E(p, q) = ∫ E(x, q) dF(x) where F is the exponential CDF.

E(q, q) = ∫ E(x, q) dG(x) where G is the CDF of q.

So E(p, q) - E(q, q) = ∫ E(x, q) d(F-G)(x) = ∫ E(x, q) dF(x) - ∫ E(x, q) dG(x).

Now, E(x, q) = (V+x)G(x) - K(x) - x where K(x) = ∫₀ˣ y dG(y).

Hmm, this is getting complicated. Let me think of another approach.

Actually, the Bishop-Cannings theorem proves this using the specific structure. Let me think about it differently.

For the war of attrition with the exponential ESS p, the key property is:

E(p, q) - E(q, q) = ∫∫ [payoff structure] ... 

Actually, there's a cleaner way. The payoff function in the war of attrition has a special structure. Let me use the fact that:

E(p, q) = ∫₀^∞ [(V+x)G(x) - K(x) - x] dF(x)

where K(x) = ∫₀ˣ y dG(y).

And E(q, q) = ∫₀^∞ [(V+x)G(x) - K(x) - x] dG(x).

Let φ(x) = (V+x)G(x) - K(x) - x = E(x, q).

Then E(p, q) - E(q, q) = ∫ φ(x) dF(x) - ∫ φ(x) dG(x) = ∫ φ(x) d(F-G)(x).

Integration by parts: ∫ φ d(F-G) = [φ(F-G)]₀^∞ - ∫ (F-G) dφ

This requires some care. Let me try a different approach.

Actually, for the war of attrition, there's a well-known result that the exponential distribution is the unique ESS, and the proof of the second condition uses the following:

E(p, q) - E(q, q) can be written as a double integral that is strictly positive when q ≠ p.

Let me try to compute this directly.

The payoff to strategy x against strategy y:
- x > y: V - y
- x < y: -x  
- x = y: V/2 - x

For continuous distributions (no atoms), the x = y case has measure zero.

E(p, q) = ∫∫_{x>y} (V-y) dF(x)dG(y) + ∫∫_{x<y} (-x) dF(x)dG(y)

E(q, q) = ∫∫_{x>y} (V-y) dG(x)dG(y) + ∫∫_{x<y} (-x) dG(x)dG(y)

E(p, q) - E(q, q) = ∫∫_{x>y} (V-y) d(F-G)(x)dG(y) + ∫∫_{x>y} (V-y) dG(x)d(F-G)(y)
                  + ∫∫_{x<y} (-x) d(F-G)(x)dG(y) + ∫∫_{x<y} (-x) dG(x)d(F-G)(y)

This is getting messy. Let me use a known result.

Actually, the standard proof uses the following approach. Define:

E(p, q) - E(q, q) = E(p, q) - E(q, p) + E(q, p) - E(q, q)

Since E(q, p) = E(p, p) = 0 (because every strategy gets 0 against p), we have:

E(p, q) - E(q, q) = E(p, q) - 0 + 0 - E(q, q) = E(p, q) - E(q, q)

Hmm, that's circular. Let me think again.

We know E(q, p) = 0 for all q (since E(x, p) = 0 for all x). So E(p, p) = E(q, p) = 0.

We need to show E(p, q) > E(q, q) for q ≠ p.

E(p, q) - E(q, q) = ?

Let me use the specific form. With p = exponential:

E(p, q) = ∫₀^∞ E(x, q) f(x) dx where f(x) = (1/V)e^{-x/V}

E(x, q) = (V+x)G(x) - K(x) - x

where G is the CDF of q and K(x) = ∫₀ˣ y dG(y) = ∫₀ˣ y g(y) dy (assuming density exists).

So E(p, q) = ∫₀^∞ [(V+x)G(x) - K(x) - x] (1/V) e^{-x/V} dx

And E(q, q) = ∫₀^∞ [(V+x)G(x) - K(x) - x] g(x) dx

Let me define ψ(x) = (V+x)G(x) - K(x) - x. Then:

E(p, q) = ∫ ψ(x) (1/V) e^{-x/V} dx

E(q, q) = ∫ ψ(x) g(x) dx

E(p, q) - E(q, q) = ∫ ψ(x) [(1/V)e^{-x/V} - g(x)] dx = ∫ ψ(x) [f(x) - g(x)] dx

Now, ψ(x) = E(x, q). Note that ψ'(x) = V·g(x) + G(x) - 1 (derivative of (V+x)G(x) - K(x) - x = G(x) + (V+x)g(x) - x·g(x) - 1 = V·g(x) + G(x) - 1).

Also, for the exponential p, f(x) = (1/V)e^{-x/V} and F(x) = 1 - e^{-x/V}, so V·f(x) + F(x) - 1 = e^{-x/V} + 1 - e^{-x/V} - 1 = 0. ✓

Now, E(p, q) - E(q, q) = ∫ ψ(x) [f(x) - g(x)] dx.

Let me try integration by parts. Let u = ψ(x), dv = [f(x) - g(x)] dx. Then du = ψ'(x) dx = [V·g(x) + G(x) - 1] dx, and v = F(x) - G(x).

∫₀^∞ ψ(x)[f(x)-g(x)]dx = [ψ(x)(F(x)-G(x))]₀^∞ - ∫₀^∞ [F(x)-G(x)]ψ'(x)dx

At x = 0: ψ(0) = V·G(0) - 0 - 0 = V·G(0). F(0) - G(0) = 0 - G(0) = -G(0). So ψ(0)(F(0)-G(0)) = -V·G(0)².

At x → ∞: F(∞) = 1, G(∞) = 1, so F(∞) - G(∞) = 0. And ψ(∞) is bounded (it approaches some limit). So the boundary term at ∞ is 0.

So: E(p,q) - E(q,q) = -(-V·G(0)²) - ∫₀^∞ [F(x)-G(x)][V·g(x)+G(x)-1]dx

= V·G(0)² - ∫₀^∞ [F-G][Vg+G-1]dx

Now, V·g(x) + G(x) - 1 = ψ'(x). And F(x) - G(x) = (1 - e^{-x/V}) - G(x).

Hmm, this is still complex. Let me try yet another approach.

Actually, I recall that the standard proof uses the following identity for the war of attrition:

E(p, q) - E(q, q) = ∫₀^∞ [F(x) - G(x)]² · (something positive) dx

or a similar expression that's clearly non-negative and strictly positive when F ≠ G.

Let me try to derive this. 

Actually, let me try a more direct computation. Let me use the payoff structure directly.

E(p, q) = ∫₀^∞ ∫₀^∞ π(x, y) dF(x) dG(y)

where π(x, y) = V - y if x > y, -x if x < y, V/2 - x if x = y.

Since both distributions are continuous (p is continuous, and if q has atoms, we can handle that separately), the tie case has measure zero.

E(p, q) = ∫₀^∞ [∫₀^y (-x) dF(x) + ∫_y^∞ (V - y) dF(x)] dG(y)

= ∫₀^∞ [-∫₀^y x dF(x) + (V-y)(1-F(y))] dG(y)

= ∫₀^∞ [-H_F(y) + (V-y)(1-F(y))] dG(y)

where H_F(y) = ∫₀^y x dF(x).

Similarly:

E(q, q) = ∫₀^∞ [-H_G(y) + (V-y)(1-G(y))] dG(y)

So:

E(p, q) - E(q, q) = ∫₀^∞ [-H_F(y) + (V-y)(1-F(y)) + H_G(y) - (V-y)(1-G(y))] dG(y)

= ∫₀^∞ [(V-y)(G(y) - F(y)) + H_G(y) - H_F(y)] dG(y)

= ∫₀^∞ [(V-y)(G-F) + (H_G - H_F)] dG(y)

Now, H_G(y) - H_F(y) = ∫₀^y x d(G-F)(x).

Integration by parts: ∫₀^y x d(G-F)(x) = [x(G-F)(x)]₀^y - ∫₀^y (G-F)(x) dx = y(G(y)-F(y)) - ∫₀^y (G-F)(x)dx

So:

(V-y)(G-F) + (H_G - H_F) = (V-y)(G-F) + y(G-F) - ∫₀^y (G-F)dx

= V(G-F) - ∫₀^y (G-F)dx

Let D(y) = G(y) - F(y). Then:

E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - ∫₀^y D(x)dx] dG(y)

Let A(y) = ∫₀^y D(x)dx = ∫₀^y (G(x) - F(x))dx. Then:

E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - A(y)] dG(y)

Now, V·D(y) - A(y) = V·D(y) - ∫₀^y D(x)dx.

Note that dA/dy = D(y), so V·D(y) - A(y) = V·A'(y) - A(y).

Also, note that A(0) = 0 and A(∞) = ∫₀^∞ (G(x) - F(x))dx. Since both are probability distributions with the same total mass (1), and if both have finite means... actually A(∞) = E_q[X] - E_p[X] = E_q[X] - V (since the exponential has mean V). This might not be zero.

Let me try integration by parts on ∫₀^∞ [V·A'(y) - A(y)] dG(y).

∫₀^∞ V·A'(y) dG(y) = V∫₀^∞ D(y) dG(y)

∫₀^∞ A(y) dG(y) = [A(y)G(y)]₀^∞ - ∫₀^∞ A'(y)G(y)dy = A(∞)·1 - 0 - ∫₀^∞ D(y)G(y)dy

So E(p,q) - E(q,q) = V∫₀^∞ D(y)dG(y) - A(∞) + ∫₀^∞ D(y)G(y)dy

= V∫₀^∞ (G(y)-F(y))dG(y) - A(∞) + ∫₀^∞ (G(y)-F(y))G(y)dy

Hmm, this is getting complicated. Let me try a completely different approach.

Let me use the approach from Bishop & Cannings (1978) directly. 

Actually, I think the cleanest approach is:

E(p, q) - E(q, q) = E(p, q) - E(q, p) + E(q, p) - E(q, q)

We know E(q, p) = E(p, p) = 0 (since every strategy gets 0 against the exponential p). So:

E(p, q) - E(q, q) = E(p, q) - E(q, p)

Now, E(p, q) - E(q, p): is this related to some antisymmetric form?

In general, E(p, q) - E(q, p) = ∫∫ [π(x,y) - π(y,x)] dF(x)dG(y)

π(x,y) - π(y,x):
- x > y: (V - y) - (-y) = V
- x < y: (-x) - (V - x) = -V
- x = y: 0

So π(x,y) - π(y,x) = V·sign(x - y).

Therefore:

E(p, q) - E(q, p) = V·∫∫ sign(x - y) dF(x) dG(y)

= V·[P(X > Y) - P(X < Y)] where X ~ p, Y ~ q

= V·[∫₀^∞ P(X > y) dG(y) - ∫₀^∞ P(X < y) dG(y)]

= V·[∫₀^∞ (1 - F(y)) dG(y) - ∫₀^∞ F(y) dG(y)]

= V·∫₀^∞ (1 - 2F(y)) dG(y)

With F(y) = 1 - e^{-y/V}:

1 - 2F(y) = 1 - 2(1 - e^{-y/V}) = -1 + 2e^{-y/V}

So E(p, q) - E(q, p) = V·∫₀^∞ (-1 + 2e^{-y/V}) dG(y) = V·[-1 + 2∫₀^∞ e^{-y/V} dG(y)]

Now, ∫₀^∞ e^{-y/V} dG(y) is the Laplace transform of G at 1/V, denote it L_G(1/V).

For the exponential p: L_F(1/V) = ∫₀^∞ e^{-y/V} (1/V)e^{-y/V} dy = (1/V) ∫₀^∞ e^{-2y/V} dy = (1/V)(V/2) = 1/2.

So E(p, p) - E(p, p) = V·[-1 + 2·(1/2)] = 0. ✓ (Consistent.)

Now, E(p, q) - E(q, q) = E(p, q) - E(q, p) = V·[-1 + 2L_G(1/V)].

We need this to be > 0 for q ≠ p, i.e., L_G(1/V) > 1/2.

By Jensen's inequality: Since e^{-y/V} is convex in y... wait, e^{-y/V} is convex (second derivative is (1/V²)e^{-y/V} > 0). So by Jensen:

L_G(1/V) = E_G[e^{-Y/V}] ≥ e^{-E_G[Y]/V}

with equality iff G is degenerate (point mass) or... no, Jensen gives ≥ for convex functions with equality iff Y is constant a.s.

But we need L_G(1/V) > 1/2, and Jensen gives L_G(1/V) ≥ e^{-E_G[Y]/V}. This doesn't directly give us what we want unless E_G[Y] = V.

Hmm, so this approach shows E(p,q) - E(q,q) = V(2L_G(1/V) - 1), and we need L_G(1/V) > 1/2 for q ≠ p.

But this isn't always true! For example, if q is a point mass at 0, then L_G(1/V) = e^0 = 1 > 1/2. OK that works.

If q is a point mass at some large M, L_G(1/V) = e^{-M/V} which can be < 1/2 for M > V ln 2. Then E(p,q) - E(q,q) < 0, meaning p is NOT an ESS?!

Wait, that can't be right. Let me recheck.

Oh wait, I think I made an error. Let me recheck: E(p, q) - E(q, q) = E(p, q) - E(q, p) + E(q, p) - E(q, q). We have E(q, p) = 0 and E(p, p) = 0. But E(q, p) - E(q, q) ≠ 0 in general!

E(q, p) = 0 (every strategy gets 0 against p).
E(q, q) = some value.

So E(p, q) - E(q, q) = E(p, q) - E(q, p) + E(q, p) - E(q, q) = [E(p,q) - E(q,p)] + [0 - E(q,q)]

= V(2L_G(1/V) - 1) - E(q, q)

So I need to also compute E(q, q).

E(q, q) = ∫∫ π(x,y) dG(x) dG(y) = ∫₀^∞ [-H_G(y) + (V-y)(1-G(y))] dG(y)

This is getting complicated. Let me try a different approach.

Actually, let me reconsider. Maybe I should use the direct computation:

E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - A(y)] dG(y)

where D(y) = G(y) - F(y) and A(y) = ∫₀^y D(x) dx.

With F(y) = 1 - e^{-y/V}, D(y) = G(y) - 1 + e^{-y/V}.

A(y) = ∫₀^y [G(x) - 1 + e^{-x/V}] dx = ∫₀^y G(x)dx - y + V(1 - e^{-y/V})

V·D(y) - A(y) = V[G(y) - 1 + e^{-y/V}] - ∫₀^y G(x)dx + y - V(1 - e^{-y/V})

= V·G(y) - V + V·e^{-y/V} - ∫₀^y G(x)dx + y - V + V·e^{-y/V}

= V·G(y) - 2V + 2V·e^{-y/V} - ∫₀^y G(x)dx + y

Hmm, this is still messy. Let me try the direct approach for specific q to check.

Let q = δ_a (point mass at a > 0). Then G(y) = 1 for y ≥ a, 0 for y < a.

E(p, q) = E(p, δ_a) = payoff of p against a = ∫₀^a (V-a)dF(x) + ∫_a^∞ (-x)dF(x) ... wait, no.

E(p, q) where p is mixed and q = δ_a: this is the expected payoff to p when the opponent plays a.

E(p, δ_a) = ∫₀^∞ payoff(x, a) dF(x) = ∫₀^a (V - a) dF(x) + ∫_a^∞ (-x) dF(x) + (V/2 - a)·0

= (V-a)F(a) - ∫_a^∞ x dF(x)

With F exponential: F(a) = 1 - e^{-a/V}, ∫_a^∞ x (1/V)e^{-x/V} dx = [-(x+V)e^{-x/V}·... let me compute.

∫_a^∞ x (1/V) e^{-x/V} dx. Let u = x/V, dx = V du:
= ∫_{a/V}^∞ V·u · (1/V) · e^{-u} · V du = V ∫_{a/V}^∞ u e^{-u} du = V · (a/V + 1) e^{-a/V} = (a + V) e^{-a/V}

So E(p, δ_a) = (V - a)(1 - e^{-a/V}) - (a + V)e^{-a/V}

= (V - a) - (V - a)e^{-a/V} - (a + V)e^{-a/V}

= (V - a) - e^{-a/V}[(V - a) + (a + V)]

= (V - a) - e^{-a/V} · 2V

= V - a - 2V·e^{-a/V}

E(δ_a, δ_a) = payoff of a against a = V/2 - a (tie).

E(p, δ_a) - E(δ_a, δ_a) = V - a - 2V·e^{-a/V} - V/2 + a = V/2 - 2V·e^{-a/V} = V(1/2 - 2e^{-a/V})

For this to be > 0: 1/2 > 2e^{-a/V}, i.e., e^{-a/V} < 1/4, i.e., a/V > ln 4, i.e., a > V ln 4 ≈ 1.386V.

So for a > V ln 4, E(p, δ_a) > E(δ_a, δ_a). ✓
For a < V ln 4, E(p, δ_a) < E(δ_a, δ_a). ✗!!!

This means for q = δ_a with small a, the second ESS condition FAILS? That would mean the exponential is NOT an ESS, which contradicts the well-known result.

Wait, let me recheck. For q = δ_a with small a, we need to check: is E(q, p) = E(p, p) = 0? Yes, E(δ_a, p) = 0 for all a (every strategy gets 0 against p). So the first condition is E(p,p) ≥ E(q,p): 0 ≥ 0, equality. So we need the second condition: E(p, q) > E(q, q).

E(p, δ_a) - E(δ_a, δ_a) = V(1/2 - 2e^{-a/V})

For a = 0: V(1/2 - 2) = -3V/2 < 0. So E(p, δ_0) < E(δ_0, δ_0). This means the second condition fails!

But δ_0 is the strategy "give up immediately." E(δ_0, δ_0) = V/2 - 0 = V/2. E(p, δ_0) = V - 0 - 2V = -V. So E(p, δ_0) = -V < V/2 = E(δ_0, δ_0).

So the exponential strategy p does NOT satisfy the second ESS condition against δ_0!

This means... the exponential is NOT an ESS in the standard Maynard Smith sense?

Hmm, wait. Let me reconsider. Maybe I'm making an error in the payoff structure.

Let me re-examine the war of attrition payoff. There are different conventions:

**Convention 1 (Bishop-Cannings):** Both players pay the cost equal to the minimum of the two times. Winner gets V.
- x > y: player gets V - y, opponent gets -y
- x < y: player gets -x, opponent gets V - x
- x = y: both get V/2 - x

**Convention 2:** Each player pays their own bid. Winner gets V.
- x > y: player gets V - x, opponent gets -y
- x < y: player gets -x, opponent gets V - y

Let me recheck which convention gives the exponential as ESS.

With Convention 1 (both pay min(x,y)):
E(x, y) = V - y if x > y, -x if x < y, V/2 - x if x = y.

E(x, p) = ∫₀ˣ (V-y)dF(y) + ∫_x^∞ (-x)dF(y) = VF(x) - H(x) - x(1-F(x))

Setting dE/dx = 0: Vf(x) + F(x) - 1 = 0, giving F(x) = 1 - e^{-x/V}. ✓

With Convention 2 (each pays own bid):
E(x, y) = V - x if x > y, -x if x < y, V/2 - x if x = y.

E(x, p) = ∫₀ˣ (V-x)dF(y) + ∫_x^∞ (-x)dF(y) = (V-x)F(x) - x(1-F(x)) = VF(x) - xF(x) - x + xF(x) = VF(x) - x

dE/dx = Vf(x) - 1 = 0, so f(x) = 1/V, uniform distribution. That doesn't seem right for the war of attrition.

So Convention 1 is the standard one, and the exponential is the solution. But I showed the second ESS condition fails for δ_0. Let me recheck my computation.

E(p, δ_0): p is mixed, opponent plays 0. 
- If x > 0 (which happens with probability 1 since p is continuous on [0,∞)): payoff = V - 0 = V.
- If x = 0 (probability 0): V/2 - 0 = V/2.

So E(p, δ_0) = V.

E(δ_0, δ_0) = V/2 - 0 = V/2.

E(p, δ_0) - E(δ_0, δ_0) = V - V/2 = V/2 > 0. ✓

Wait, I think I made an error before! Let me recompute.

E(p, δ_a) where q = δ_a (opponent always plays a):

E(p, δ_a) = ∫₀^∞ payoff(x, a) dF(x)

payoff(x, a):
- x > a: V - a
- x < a: -x
- x = a: V/2 - a (measure 0)

E(p, δ_a) = (V - a)·P(X > a) + ∫₀^a (-x) dF(x)

= (V - a)(1 - F(a)) - H(a)

where H(a) = ∫₀^a x dF(x).

With F exponential: F(a) = 1 - e^{-a/V}, 1 - F(a) = e^{-a/V}.

H(a) = ∫₀^a x (1/V) e^{-x/V} dx = V(1 - e^{-a/V}) - a·e^{-a/V} = V - (V+a)e^{-a/V}

Wait let me recompute: ∫₀^a x (1/V) e^{-x/V} dx. 

Integration by parts: let u = x, dv = (1/V)e^{-x/V}dx, so du = dx, v = -e^{-x/V}.

= [-x·e^{-x/V}]₀^a + ∫₀^a e^{-x/V} dx = -a·e^{-a/V} + [-V·e^{-x/V}]₀^a = -a·e^{-a/V} - V·e^{-a/V} + V = V - (V+a)e^{-a/V}

So H(a) = V - (V+a)e^{-a/V}.

E(p, δ_a) = (V - a)·e^{-a/V} - [V - (V+a)e^{-a/V}]

= (V-a)e^{-a/V} - V + (V+a)e^{-a/V}

= e^{-a/V}[(V-a) + (V+a)] - V

= 2V·e^{-a/V} - V

= V(2e^{-a/V} - 1)

E(δ_a, δ_a) = V/2 - a.

E(p, δ_a) - E(δ_a, δ_a) = V(2e^{-a/V} - 1) - V/2 + a = 2V·e^{-a/V} - 3V/2 + a

For a = 0: 2V - 3V/2 + 0 = V/2 > 0. ✓

For a → ∞: 0 - 3V/2 + a → ∞ > 0. ✓

For a = V: 2V·e^{-1} - 3V/2 + V = 2V/e - V/2 ≈ 0.736V - 0.5V = 0.236V > 0. ✓

Let me check if it's always positive. Let g(a) = 2V·e^{-a/V} - 3V/2 + a.

g'(a) = -2e^{-a/V} + 1 = 0 → e^{-a/V} = 1/2 → a = V·ln 2.

g(V ln 2) = 2V·(1/2) - 3V/2 + V ln 2 = V - 3V/2 + V ln 2 = -V/2 + V ln 2 = V(ln 2 - 1/2) ≈ V(0.693 - 0.5) = 0.193V > 0. ✓

So g(a) > 0 for all a ≥ 0. The minimum is at a = V ln 2 and is positive. ✓

So I made an arithmetic error earlier. The exponential IS an ESS. Let me redo the earlier computation.

Earlier I had: E(p, δ_a) = V - a - 2V·e^{-a/V}, but the correct answer is V(2e^{-a/V} - 1). Let me see where I went wrong.

I had written: E(p, δ_a) = (V-a)(1 - e^{-a/V}) - (a+V)e^{-a/V}

But (V-a)·P(X > a) = (V-a)·(1-F(a)) = (V-a)·e^{-a/V}, and the cost part is -H(a) = -(V - (V+a)e^{-a/V}).

So E(p, δ_a) = (V-a)e^{-a/V} - V + (V+a)e^{-a/V} = e^{-a/V}(V-a+V+a) - V = 2V·e^{-a/V} - V. ✓

My earlier error was: I wrote (V-a)F(a) instead of (V-a)(1-F(a)). The payoff for x > a is V - a (win, pay cost a), and P(X > a) = 1 - F(a), not F(a). I had the winning and losing regions swapped. Good, the exponential is indeed an ESS.

Now, back to the general proof. For the second ESS condition, I need to show E(p, q) > E(q, q) for all q ≠ p with E(q, p) = E(p, p) = 0.

Since E(x, p) = 0 for all x ≥ 0 (every pure strategy is a best response to p), every q satisfies E(q, p) = 0 = E(p, p). So we need E(p, q) > E(q, q) for ALL q ≠ p.

From the computation above:

E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - A(y)] dG(y)

where D(y) = G(y) - F(y), A(y) = ∫₀^y D(x) dx, F is the exponential CDF.

Let me verify this with q = δ_a. G(y) = 1 for y ≥ a, 0 for y < a. D(y) = G(y) - F(y).

For y < a: D(y) = -F(y) = -(1 - e^{-y/V}) = e^{-y/V} - 1.
For y ≥ a: D(y) = 1 - F(y) = e^{-y/V}.

A(y) = ∫₀^y D(x) dx.
For y < a: A(y) = ∫₀^y (e^{-x/V} - 1) dx = V(1 - e^{-y/V}) - y.
For y ≥ a: A(y) = ∫₀^a (e^{-x/V} - 1) dx + ∫_a^y e^{-x/V} dx = [V(1-e^{-a/V}) - a] + V(e^{-a/V} - e^{-y/V}) = V - a - V·e^{-y/V}.

V·D(y) - A(y):
For y < a: V(e^{-y/V} - 1) - V(1 - e^{-y/V}) + y = V·e^{-y/V} - V - V + V·e^{-y/V} + y = 2V·e^{-y/V} - 2V + y.
For y ≥ a: V·e^{-y/V} - (V - a - V·e^{-y/V}) = 2V·e^{-y/V} - V + a.

∫₀^∞ [V·D(y) - A(y)] dG(y) = [V·D(a) - A(a)] since G has mass 1 at a.

At y = a (from the y ≥ a side): 2V·e^{-a/V} - V + a.

So E(p, δ_a) - E(δ_a, δ_a) = 2V·e^{-a/V} - V + a.

But we computed E(p, δ_a) - E(δ_a, δ_a) = 2V·e^{-a/V} - 3V/2 + a.

These don't match! 2V·e^{-a/V} - V + a ≠ 2V·e^{-a/V} - 3V/2 + a.

There's a discrepancy of V/2. Let me recheck.

Hmm, the issue might be with the tie case. When q = δ_a, G has an atom at a, and the tie case (x = a) has positive probability: P(X = a) = 0 (F continuous) but P(Y = a) = 1. So when computing E(p, q), the payoff at x = a uses the tie rule for the x = y part... but since F is continuous, P(X = a) = 0, so the tie doesn't contribute to E(p, q). However, for E(q, q) = E(δ_a, δ_a), the tie case is the only case: both play a, so payoff = V/2 - a.

Let me recheck the formula E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - A(y)] dG(y).

This was derived from:
E(p, q) = ∫₀^∞ [-H_F(y) + (V-y)(1-F(y))] dG(y)
E(q, q) = ∫₀^∞ [-H_G(y) + (V-y)(1-G(y))] dG(y)

E(p,q) - E(q,q) = ∫₀^∞ [(V-y)(G(y)-F(y)) + H_G(y) - H_F(y)] dG(y)

For q = δ_a: H_G(y) = ∫₀^y x dG(x) = 0 for y < a, = a for y ≥ a.

H_F(y) = ∫₀^y x dF(x) = V - (V+y)e^{-y/V} for the exponential.

For y = a:
(V-a)(G(a) - F(a)) + H_G(a) - H_F(a) = (V-a)(1 - (1-e^{-a/V})) + a - (V - (V+a)e^{-a/V})
= (V-a)e^{-a/V} + a - V + (V+a)e^{-a/V}
= e^{-a/V}(V-a+V+a) + a - V
= 2V·e^{-a/V} + a - V

So E(p, δ_a) - E(δ_a, δ_a) = 2V·e^{-a/V} + a - V.

But we computed directly: E(p, δ_a) - E(δ_a, δ_a) = V(2e^{-a/V} - 1) - (V/2 - a) = 2V·e^{-a/V} - V - V/2 + a = 2V·e^{-a/V} + a - 3V/2.

So the formula gives 2V·e^{-a/V} + a - V but the direct computation gives 2V·e^{-a/V} + a - 3V/2. Discrepancy of V/2.

The issue is that E(q, q) for q = δ_a includes the tie case V/2 - a, but the integral formula ∫₀^∞ [-H_G(y) + (V-y)(1-G(y))] dG(y) doesn't account for ties properly when G has atoms.

When G has an atom at a, the integral ∫₀^∞ ... dG(y) evaluates the integrand at y = a. But the formula -H_G(y) + (V-y)(1-G(y)) was derived assuming continuous distributions (no ties). For the tie case, the payoff is V/2 - y, not V - y or -x.

So the formula E(q, q) = ∫₀^∞ [-H_G(y) + (V-y)(1-G(y))] dG(y) is only valid when G is continuous. For distributions with atoms, we need to add a correction for ties.

This means my general formula E(p,q) - E(q,q) = ∫[V·D(y) - A(y)]dG(y) is only valid when q is continuous. For the ESS proof, I need to handle both continuous and discrete (and mixed) q.

This is getting quite involved. Let me take a step back and think about what level of rigor is expected here.

The question asks: "what are the necessary and sufficient conditions for a strategy p to be an ESS?" in the war of attrition. This is a well-known result from Bishop & Cannings (1978). The answer is the set of conditions (C1)-(C5) I listed, and the unique ESS is the exponential distribution.

Let me write up a clean proof that states the conditions, proves necessity and sufficiency, and identifies the unique ESS. For the second ESS condition (sufficiency), I'll use the approach that works for continuous q and note the extension.

Actually, let me think about this more carefully. The key insight for the second condition is:

For the exponential ESS p, E(p, q) - E(q, q) can be written as:

E(p, q) - E(q, q) = ∫₀^∞ ∫₀^∞ [π(x,y) dF(x) - π(x,y) dG(x)] dG(y) + (correction for ties)

Hmm, let me try yet another approach. Let me use the fact that:

E(p, q) - E(q, q) = E(p, q) - E(q, p) + E(q, p) - E(q, q)

= [E(p, q) - E(q, p)] + [E(q, p) - E(q, q)]

We know E(q, p) = 0 for all q (every strategy gets 0 against p).

So E(p, q) - E(q, q) = E(p, q) - E(q, p) + 0 - E(q, q) = [E(p,q) - E(q,p)] - E(q,q).

Now E(p, q) - E(q, p) = V·[P(X > Y) - P(X < Y)] where X ~ p, Y ~ q (this accounts for ties as 0, which is correct since π(x,y) - π(y,x) = 0 for x = y).

And E(q, q) = E(q, q) which includes tie payoffs.

So E(p, q) - E(q, q) = V·[P(X > Y) - P(X < Y)] - E(q, q).

Hmm, this doesn't simplify things much.

Let me try to directly prove E(p, q) > E(q, q) for the exponential p and any q ≠ p.

Actually, I think the cleanest approach is to use the following:

**Claim:** For the exponential ESS p with mean V, and any strategy q ≠ p:

E(p, q) - E(q, q) = ∫₀^∞ [F(x) - G(x)]² V f(x) dx + (positive terms from atoms)

Wait, I don't think that's exactly right. Let me try to derive it properly.

Let me go back to the formula (for continuous q):

E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - A(y)] dG(y)

where D(y) = G(y) - F(y), A(y) = ∫₀^y D(x) dx, F is exponential.

Let me substitute. With F(y) = 1 - e^{-y/V}, f(y) = (1/V)e^{-y/V}:

D(y) = G(y) - 1 + e^{-y/V}

A(y) = ∫₀^y [G(x) - 1 + e^{-x/V}] dx = ∫₀^y G(x) dx - y + V(1 - e^{-y/V})

V·D(y) - A(y) = V·G(y) - V + V·e^{-y/V} - ∫₀^y G(x) dx + y - V + V·e^{-y/V}

= V·G(y) - 2V + 2V·e^{-y/V} - ∫₀^y G(x) dx + y

Now, ∫₀^∞ [V·D(y) - A(y)] dG(y) = ∫₀^∞ [V·G(y) - 2V + 2V·e^{-y/V} - ∫₀^y G(x) dx + y] dG(y)

= V·∫₀^∞ G(y) dG(y) - 2V + 2V·∫₀^∞ e^{-y/V} dG(y) - ∫₀^∞ ∫₀^y G(x) dx dG(y) + ∫₀^∞ y dG(y)

Now, ∫₀^∞ G(y) dG(y) = [G(y)²/2]₀^∞ ... no, that's not right since G is a CDF, not a density.

∫₀^∞ G(y) dG(y) = ∫₀^∞ G(y) g(y) dy = [G(y)²/2]₀^∞ = 1/2 (if G is continuous with G(0)=0, G(∞)=1).

∫₀^∞ ∫₀^y G(x) dx dG(y) = ∫₀^∞ G(x) ∫_x^∞ dG(y) dx = ∫₀^∞ G(x)(1-G(x)) dx (by Fubini, for continuous G).

∫₀^∞ y dG(y) = E_q[Y] = μ_q.

∫₀^∞ e^{-y/V} dG(y) = L_G(1/V) (Laplace transform).

So:

E(p, q) - E(q, q) = V/2 - 2V + 2V·L_G(1/V) - ∫₀^∞ G(x)(1-G(x)) dx + μ_q

= -3V/2 + 2V·L_G(1/V) - ∫₀^∞ G(1-G) dx + μ_q

For q = p (exponential): L_F(1/V) = 1/2, ∫₀^∞ F(1-F) dx = ∫₀^∞ (1-e^{-x/V})e^{-x/V} dx = ∫₀^∞ e^{-x/V} dx - ∫₀^∞ e^{-2x/V} dx = V - V/2 = V/2. μ_p = V.

E(p,p) - E(p,p) = -3V/2 + 2V(1/2) - V/2 + V = -3V/2 + V - V/2 + V = 0. ✓

Now, for general continuous q, I need to show:

-3V/2 + 2V·L_G(1/V) - ∫₀^∞ G(1-G) dx + μ_q > 0 when G ≠ F.

This is still complex. Let me try a different decomposition.

Actually, let me try to express E(p, q) - E(q, q) in terms of (F - G)².

Let me define φ(x) = G(x) - F(x) = D(x). I want to express the difference in terms of D².

E(p, q) - E(q, q) = ∫₀^∞ [V·D(y) - A(y)] dG(y) (for continuous q)

= ∫₀^∞ [V·D(y) - A(y)] (g(y)) dy

Now, dG = g dy, and also dF = f dy. So dG = dF + D' dy = f dy + D' dy = (f + D') dy. But D' = g - f, so dG = g dy. That's circular.

Let me try: dG = dF + dD, so:

∫₀^∞ [V·D - A] dG = ∫₀^∞ [V·D - A] dF + ∫₀^∞ [V·D - A] dD

= ∫₀^∞ [V·D - A] f dy + ∫₀^∞ [V·D - A] D' dy

The second part: ∫₀^∞ [V·D - A] D' dy. Note that A' = D, so:

∫₀^∞ [V·A' - A] A'' dy ... hmm, not quite. D' = A'' and D = A'.

∫₀^∞ [V·A' - A] A'' dy = ∫₀^∞ V·A'·A'' dy - ∫₀^∞ A·A'' dy

= V·[A'²/2]₀^∞ - [A·A']₀^∞ + ∫₀^∞ A'² dy

= V·D(∞)²/2 - V·D(0)²/2 - A(∞)·D(∞) + A(0)·D(0) + ∫₀^∞ D² dy

D(0) = G(0) - F(0) = G(0) - 0 = G(0). If G(0) = 0 (no mass at 0), then D(0) = 0, A(0) = 0.

D(∞) = G(∞) - F(∞) = 1 - 1 = 0. A(∞) = ∫₀^∞ D(x) dx = μ_q - V (difference of means, assuming both finite).

So the second part = 0 - 0 - 0 + 0 + ∫₀^∞ D² dy = ∫₀^∞ D² dy.

The first part: ∫₀^∞ [V·D - A] f dy where f = (1/V)e^{-y/V}.

= ∫₀^∞ V·D·f dy - ∫₀^∞ A·f dy

= V·∫₀^∞ D·(1/V)e^{-y/V} dy - ∫₀^∞ A·(1/V)e^{-y/V} dy

= ∫₀^∞ D·e^{-y/V} dy - (1/V)∫₀^∞ A·e^{-y/V} dy

Now, D(y) = G(y) - 1 + e^{-y/V}, so e^{-y/V} = D(y) - G(y) + 1.

∫₀^∞ D·e^{-y/V} dy = ∫₀^∞ D(D - G + 1) dy = ∫₀^∞ D² dy - ∫₀^∞ D·G dy + ∫₀^∞ D dy

∫₀^∞ D dy = A(∞) = μ_q - V.

∫₀^∞ D·G dy = ∫₀^∞ (G - F)·G dy = ∫₀^∞ G² dy - ∫₀^∞ F·G dy.

This is getting very messy. Let me try a completely different approach.

**Alternative approach using the payoff difference directly:**

E(p, q) - E(q, q) = ∫∫ π(x,y) dF(x)dG(y) - ∫∫ π(x,y) dG(x)dG(y)

= ∫∫ π(x,y) [dF(x) - dG(x)] dG(y)

Let me write dF - dG = (f - g) dy for continuous distributions.

= ∫∫ π(x,y) (f(x) - g(x)) dx dG(y)

= ∫∫ π(x,y) (f(x) - g(x)) dx g(y) dy

Now, π(x, y) = V - y for x > y, -x for x < y (ignoring ties for continuous case).

= ∫₀^∞ g(y) [∫₀^y (-x)(f(x)-g(x)) dx + ∫_y^∞ (V-y)(f(x)-g(x)) dx] dy

= ∫₀^∞ g(y) [-∫₀^y x(f-g) dx + (V-y)∫_y^∞ (f-g) dx] dy

Let h(x) = f(x) - g(x), H(y) = ∫₀^y h(x) dx = F(y) - G(y) = -D(y).

∫_y^∞ h(x) dx = -H(y) = D(y).

∫₀^y x·h(x) dx: let me call this J(y).

So the inner bracket = -J(y) + (V-y)·D(y).

E(p,q) - E(q,q) = ∫₀^∞ g(y) [-J(y) + (V-y)D(y)] dy

Now, J(y) = ∫₀^y x·h(x) dx = ∫₀^y x(f(x)-g(x)) dx = H_F(y) - H_G(y) where H_F, H_G are the partial means.

(V-y)D(y) - J(y) = (V-y)(G(y)-F(y)) - (H_F(y) - H_G(y))

= (V-y)(G-F) + H_G - H_F

This is the same as before. Let me try the substitution approach.

E(p,q) - E(q,q) = ∫₀^∞ g(y) [(V-y)D(y) - J(y)] dy

Let me integrate by parts. Let u = (V-y)D(y) - J(y), dv = g(y)dy. Then du = [(V-y)D'(y) - D(y) - J'(y)] dy = [(V-y)(g-f) - D(y) - y·h(y)] dy.

Wait, J'(y) = y·h(y) = y(f(y)-g(y)). And D'(y) = g(y) - f(y) = -h(y).

du = [-D(y) + (V-y)(-h(y)) - y·h(y)] dy = [-D(y) - V·h(y) + y·h(y) - y·h(y)] dy = [-D(y) - V·h(y)] dy

= [-D(y) + V·D'(y)] dy  (since h = -D')

v = G(y).

∫₀^∞ u·g dy = [u·G]₀^∞ - ∫₀^∞ G·du

At y = ∞: D(∞) = 0, J(∞) = ∫₀^∞ x(f-g)dx = μ_p - μ_q = V - μ_q. u(∞) = (V-∞)·0 - (V - μ_q) = -(V - μ_q) = μ_q - V. G(∞) = 1. So u(∞)·G(∞) = μ_q - V.

At y = 0: D(0) = G(0) - F(0) = G(0). J(0) = 0. u(0) = V·G(0). G(0) = G(0). u(0)·G(0) = V·G(0)².

So [u·G]₀^∞ = (μ_q - V) - V·G(0)².

-∫₀^∞ G·du = -∫₀^∞ G·[-D + V·D'] dy = ∫₀^∞ G·D dy - V∫₀^∞ G·D' dy

= ∫₀^∞ G·D dy - V·[G·D]₀^∞ + V∫₀^∞ G'·D dy

= ∫₀^∞ G·D dy - V·(1·0 - G(0)·G(0)) + V∫₀^∞ g·D dy

= ∫₀^∞ G·D dy + V·G(0)² + V∫₀^∞ g·D dy

So E(p,q) - E(q,q) = (μ_q - V) - V·G(0)² + ∫₀^∞ G·D dy + V·G(0)² + V∫₀^∞ g·D dy

= μ_q - V + ∫₀^∞ G·D dy + V∫₀^∞ g·D dy

= μ_q - V + ∫₀^∞ (G + V·g)·D dy

Now, D = G - F, and for the exponential, V·f + F = 1, i.e., F = 1 - V·f.

So G + V·g = (F + D) + V·g = F + D + V·g = (1 - V·f) + D + V·g = 1 + D + V·(g - f) = 1 + D + V·D' = 1 + D + V·D'.

Hmm wait: D' = g - f, so V·D' = V(g-f). And G + Vg = F + D + Vg = (1 - Vf) + D + Vg = 1 + D + V(g - f) = 1 + D + V·D'.

So (G + V·g)·D = (1 + D + V·D')·D = D + D² + V·D·D'.

∫₀^∞ (D + D² + V·D·D') dy = ∫₀^∞ D dy + ∫₀^∞ D² dy + V·∫₀^∞ D·D' dy

= A(∞) + ∫₀^∞ D² dy + V·[D²/2]₀^∞

= (μ_q - V) + ∫₀^∞ D² dy + V·(0 - G(0)²/2)

= (μ_q - V) + ∫₀^∞ D² dy - V·G(0)²/2

So E(p,q) - E(q,q) = (μ_q - V) + (μ_q - V) + ∫₀^∞ D² dy - V·G(0)²/2

= 2(μ_q - V) + ∫₀^∞ D² dy - V·G(0)²/2

Hmm, this doesn't look right because for q = p, we should get 0.

For q = p: μ_q = V, D = 0, G(0) = 0. So 2(0) + 0 - 0 = 0. ✓

For q = δ_a (a > 0): μ_q = a, D(y) = G(y) - F(y), G(0) = 0 (if a > 0).

∫₀^∞ D² dy = ∫₀^a F(y)² dy + ∫_a^∞ (1 - F(y))² dy = ∫₀^a (1-e^{-y/V})² dy + ∫_a^∞ e^{-2y/V} dy

This is getting complicated. Let me check with a specific value, say a = V.

μ_q = V, so 2(μ_q - V) = 0.

D(y) = 0 for y < V (G(y) = 0, F(y) = 1-e^{-y/V}, wait no: G(y) = 0 for y < V, F(y) = 1-e^{-y/V} for all y. So D(y) = 0 - (1-e^{-y/V}) = e^{-y/V} - 1 for y < V, and D(y) = 1 - (1-e^{-y/V}) = e^{-y/V} for y ≥ V.

∫₀^∞ D² dy = ∫₀^V (1 - e^{-y/V})² dy + ∫_V^∞ e^{-2y/V} dy

= ∫₀^V (1 - 2e^{-y/V} + e^{-2y/V}) dy + V/2·e^{-2}

= [y + 2V·e^{-y/V} - V/2·e^{-2y/V}]₀^V + V/(2e²)

= [V + 2V/e - V/(2e²)] - [0 + 2V - V/2] + V/(2e²)

= V + 2V/e - V/(2e²) - 2V + V/2 + V/(2e²)

= V/2 - V + 2V/e = -V/2 + 2V/e ≈ -0.5V + 0.736V = 0.236V

So E(p, δ_V) - E(δ_V, δ_V) = 0 + 0.236V - 0 = 0.236V.

Direct computation: 2V·e^{-1} + V - V = 2V/e ≈ 0.736V. 

That doesn't match! 0.236V ≠ 0.736V.

I must have an error somewhere. Let me recheck.

Actually, wait. For q = δ_a, G is not continuous, so the formula E(p,q) - E(q,q) = ∫₀^∞ [V·D(y) - A(y)] dG(y) might not be correct because of the tie term.

Let me reconsider. The issue is that for q with atoms, E(q, q) includes tie payoffs V/2 - x, but the integral formula doesn't account for this.

Let me be more careful. For general q (possibly with atoms):

E(q, q) = ∫∫_{x>y} (V-y) dG(x)dG(y) + ∫∫_{x<y} (-x) dG(x)dG(y) + ∫ (V/2 - x) dG(x)·P(Y=x)

The last term is the tie contribution: ∫ (V/2 - x) P(Y=x) dG(x) = ∫ (V/2 - x) ΔG(x) dG(x) where ΔG(x) = G(x) - G(x⁻) is the jump.

For continuous q, this is 0. For q = δ_a, this is (V/2 - a)·1·1 = V/2 - a.

The formula without ties gives: ∫₀^∞ [-H_G(y) + (V-y)(1-G(y))] dG(y) which for δ_a gives:

At y = a: -a + (V-a)(1-1) = -a + 0 = -a. So the formula gives -a, but E(δ_a, δ_a) = V/2 - a. The difference is V/2, which is exactly the tie correction.

So for continuous q, the formula is correct, and for q with atoms, we need to add the tie correction.

OK so let me restrict to continuous q for the proof of the second condition, and then handle atoms separately.

For continuous q (no atoms, G(0) = 0):

E(p, q) - E(q, q) = 2(μ_q - V) + ∫₀^∞ D² dy - V·G(0)²/2

Wait, but I showed this gives 0.236V for q = δ_V, but δ_V is not continuous. Let me check with a continuous q.

Hmm, actually let me recheck my derivation. I think I might have an error.

Let me redo the integration by parts more carefully.

E(p,q) - E(q,q) = ∫₀^∞ g(y) [(V-y)D(y) - J(y)] dy

where D(y) = G(y) - F(y), J(y) = ∫₀^y x(f(x)-g(x))dx = H_F(y) - H_G(y).

Let me define u(y) = (V-y)D(y) - J(y).

u'(y) = -D(y) + (V-y)D'(y) - J'(y) = -D(y) + (V-y)(g-f) - y(f-g) = -D(y) + (V-y)(g-f) + y(g-f) = -D(y) + V(g-f) = -D(y) - V·h(y) where h = f - g.

Wait: (V-y)(g-f) + y(g-f) = (V-y+y)(g-f) = V(g-f) = -V(f-g) = -V·h. And -D(y) = -(G-F) = F - G.

So u'(y) = (F - G) - V(f - g) = -D - V·h = -D + V·D' (since D' = g - f = -h).

So u' = -D + V·D'.

Integration by parts: ∫₀^∞ u·g dy = [u·G]₀^∞ - ∫₀^∞ G·u' dy

[u·G]₀^∞: 
- At ∞: u(∞) = (V-∞)·D(∞) - J(∞) = -∞·0 - (μ_p - μ_q). Need to be careful. D(∞) = 0, but (V-∞)·D(∞) is 0·∞ indeterminate. Let me think.

Actually, D(y) → 0 as y → ∞, and (V-y) → -∞. The product (V-y)·D(y) needs to be analyzed. For the exponential, F(y) = 1 - e^{-y/V}, so D(y) = G(y) - 1 + e^{-y/V}. As y → ∞, D(y) → 0 and (V-y)·D(y) → (V-y)(G(y) - 1 + e^{-y/V}).

If G(y) → 1 fast enough, D(y) ~ e^{-y/V} - (1-G(y)), and (V-y)·D(y) ~ (V-y)·e^{-y/V} → 0 (exponential decay dominates). Also J(∞) = μ_p - μ_q = V - μ_q. So u(∞) = 0 - (V - μ_q) = μ_q - V. And G(∞) = 1. So u(∞)·G(∞) = μ_q - V.

- At 0: u(0) = V·D(0) - 0 = V·D(0) = V·(G(0) - F(0)) = V·G(0) (since F(0) = 0 for exponential). G(0) = 0 for continuous q with no atom at 0. So u(0)·G(0) = 0.

[u·G]₀^∞ = (μ_q - V) - 0 = μ_q - V.

-∫₀^∞ G·u' dy = -∫₀^∞ G·(-D + V·D') dy = ∫₀^∞ G·D dy - V∫₀^∞ G·D' dy

∫₀^∞ G·D' dy = [G·D]₀^∞ - ∫₀^∞ G'·D dy = (1·0 - 0·D(0)) - ∫₀^∞ g·D dy = -∫₀^∞ g·D dy

So -V∫₀^∞ G·D' dy = -V·(-∫₀^∞ g·D dy) = V∫₀^∞ g·D dy.

Therefore: -∫₀^∞ G·u' dy = ∫₀^∞ G·D dy + V∫₀^∞ g·D dy = ∫₀^∞ (G + Vg)·D dy.

E(p,q) - E(q,q) = (μ_q - V) + ∫₀^∞ (G + Vg)·D dy.

Now, G + Vg = (F + D) + V(g) = F + D + Vg. And F = 1 - Vf (from Vf + F = 1), so:

G + Vg = 1 - Vf + D + Vg = 1 + D + V(g - f) = 1 + D + V·D'.

So (G + Vg)·D = (1 + D + V·D')·D = D + D² + V·D·D'.

∫₀^∞ (D + D² + V·D·D') dy = ∫₀^∞ D dy + ∫₀^∞ D² dy + V·[D²/2]₀^∞

= A(∞) + ∫₀^∞ D² dy + V·(D(∞)²/2 - D(0)²/2)

= (μ_q - V) + ∫₀^∞ D² dy + V·(0 - 0)  [for continuous q with G(0) = 0, D(0) = 0, D(∞) = 0]

= (μ_q - V) + ∫₀^∞ D² dy

So E(p,q) - E(q,q) = (μ_q - V) + (μ_q - V) + ∫₀^∞ D² dy = 2(μ_q - V) + ∫₀^∞ D² dy.

For q = p: μ_q = V, D = 0, so 0 + 0 = 0. ✓

Now I need to show 2(μ_q - V) + ∫₀^∞ D² dy > 0 for q ≠ p (continuous, G(0) = 0).

Hmm, but μ_q - V can be negative (if q has mean < V). So this isn't obviously positive.

Let me check with a specific continuous q. Let q be uniform on [0, 2V], so g(y) = 1/(2V) for y ∈ [0, 2V], G(y) = y/(2V) for y ∈ [0, 2V], 0 for y < 0, 1 for y > 2V. μ_q = V.

E(p,q) - E(q,q) = 2(0) + ∫₀^∞ D² dy = ∫₀^∞ (G - F)² dy.

D(y) = y/(2V) - (1 - e^{-y/V}) for y ∈ [0, 2V], = 1 - (1 - e^{-y/V}) = e^{-y/V} for y > 2V.

∫₀^{2V} (y/(2V) - 1 + e^{-y/V})² dy + ∫_{2V}^∞ e^{-2y/V} dy

This is clearly > 0 since D is not identically 0 (q ≠ p). ✓

But what if μ_q ≠ V? Let q be uniform on [0, V], so μ_q = V/2. G(y) = y/V for y ∈ [0,V], 1 for y > V.

E(p,q) - E(q,q) = 2(V/2 - V) + ∫₀^∞ D² dy = -V + ∫₀^∞ D² dy.

D(y) = y/V - 1 + e^{-y/V} for y ∈ [0, V], = e^{-y/V} for y > V.

∫₀^V (y/V - 1 + e^{-y/V})² dy + ∫_V^∞ e^{-2y/V} dy.

Let me compute numerically. Let t = y/V, dy = V dt.

∫₀^1 (t - 1 + e^{-t})² V dt + ∫_1^∞ e^{-2t} V dt

= V[∫₀^1 (t - 1 + e^{-t})² dt + ∫_1^∞ e^{-2t} dt]

∫_1^∞ e^{-2t} dt = e^{-2}/2 ≈ 0.0677.

∫₀^1 (t - 1 + e^{-t})² dt: Let me expand. (t-1+e^{-t})² = (t-1)² + 2(t-1)e^{-t} + e^{-2t}.

∫₀^1 (t-1)² dt = 1/3.
∫₀^1 2(t-1)e^{-t} dt = 2[∫₀^1 t·e^{-t} dt - ∫₀^1 e^{-t} dt] = 2[(1-2/e) - (1-1/e)] = 2[-1/e] = -2/e ≈ -0.736.
∫₀^1 e^{-2t} dt = (1-e^{-2})/2 ≈ 0.432.

Total: 1/3 - 2/e + (1-e^{-2})/2 ≈ 0.333 - 0.736 + 0.432 = 0.029.

So ∫₀^∞ D² dy ≈ V(0.029 + 0.068) = 0.097V.

E(p,q) - E(q,q) ≈ -V + 0.097V = -0.903V < 0!

This means E(p, q) < E(q, q) for q = uniform[0, V], which would mean p is NOT an ESS!

But the exponential is supposed to be the ESS of the war of attrition. Something is wrong.

Let me double-check by direct computation.

q = uniform[0, V], g(y) = 1/V for y ∈ [0, V].

E(q, q) = ∫₀^V ∫₀^V π(x, y) (1/V²) dx dy

= (1/V²) ∫₀^V ∫₀^V π(x, y) dx dy

By symmetry (swapping x and y): ∫∫ π(x,y) dx dy = ∫∫ π(y,x) dx dy. And π(x,y) + π(y,x) = V for x ≠ y (one wins V - min, other loses -min, total = V - 2·min... wait no.

π(x,y) = V - y if x > y, -x if x < y.
π(y,x) = V - x if y > x (i.e., x < y), -y if y < x (i.e., x > y).

For x > y: π(x,y) + π(y,x) = (V - y) + (-y) = V - 2y.
For x < y: π(x,y) + π(y,x) = (-x) + (V - x) = V - 2x.

So the sum is V - 2·min(x,y). Not simply V.

∫∫ π(x,y) dx dy = (1/2)∫∫ [π(x,y) + π(y,x)] dx dy = (1/2)∫∫ [V - 2min(x,y)] dx dy

= (1/2)[V·V² - 2∫∫ min(x,y) dx dy] over [0,V]²

∫₀^V ∫₀^V min(x,y) dx dy = 2∫₀^V ∫₀^y x dx dy = 2∫₀^V y²/2 dy = ∫₀^V y² dy = V³/3.

So ∫∫ π dx dy = (1/2)[V³ - 2V³/3] = (1/2)(V³/3) = V³/6.

E(q, q) = (1/V²)·V³/6 = V/6.

Now E(p, q) = ∫₀^V E(x, q) f(x) dx where f(x) = (1/V)e^{-x/V} and E(x, q) = (V+x)G(x) - H_G(x) - x.

For x ∈ [0, V]: G(x) = x/V, H_G(x) = ∫₀^x y·(1/V) dy = x²/(2V).

E(x, q) = (V+x)(x/V) - x²/(2V) - x = x + x²/V - x²/(2V) - x = x²/(2V).

For x > V: G(x) = 1, H_G(x) = ∫₀^V y/V dy + 0 = V/2.

E(x, q) = (V+x)·1 - V/2 - x = V + x - V/2 - x = V/2.

E(p, q) = ∫₀^V (x²/(2V))·(1/V)e^{-x/V} dx + ∫_V^∞ (V/2)·(1/V)e^{-x/V} dx

= (1/(2V²))∫₀^V x² e^{-x/V} dx + (1/2)∫_V^∞ e^{-x/V} dx

∫_V^∞ e^{-x/V} dx = V·e^{-1}.

∫₀^V x² e^{-x/V} dx: Let u = x/V, dx = V du:
= V³ ∫₀^1 u² e^{-u} du = V³ [-(u²+2u+2)e^{-u}]₀^1 = V³ [-(1+2+2)/e + 2] = V³[2 - 5/e].

So E(p, q) = (1/(2V²))·V³(2 - 5/e) + (1/2)·V·e^{-1}

= (V/2)(2 - 5/e) + V/(2e)

= V - 5V/(2e) + V/(2e)

= V - 4V/(2e)

= V - 2V/e

= V(1 - 2/e) ≈ V(1 - 0.736) = 0.264V.

E(p, q) - E(q, q) = 0.264V - V/6 ≈ 0.264V - 0.167V = 0.097V > 0. ✓

So E(p, q) > E(q, q) after all! My formula 2(μ_q - V) + ∫D² dy must be wrong.

Let me recheck. For q = uniform[0, V]: μ_q = V/2, so 2(μ_q - V) = 2(-V/2) = -V. And I computed ∫D² dy ≈ 0.097V. So the formula gives -V + 0.097V = -0.903V, but the actual answer is +0.097V.

So there's an error in my derivation. The formula should give 0.097V, not -0.903V. The difference is V, which is 2V(μ_q - V) + V = 2μ_q - 2V + V = 2μ_q - V. For μ_q = V/2, that's V - V = 0... no.

Actually, -0.903V + V = 0.097V. So the error is exactly V. Let me find where I lost a V.

Hmm, let me recheck the step where I computed [u·G]₀^∞.

u(∞) = lim_{y→∞} [(V-y)D(y) - J(y)]

D(y) = G(y) - F(y). As y → ∞, G(y) → 1, F(y) → 1, D(y) → 0.
J(y) = H_F(y) - H_G(y) = ∫₀^y x(f-g)dx → μ_p - μ_q = V - μ_q.

(V-y)D(y): D(y) → 0, (V-y) → -∞. Need to check the rate.

For the exponential, 1 - F(y) = e^{-y/V}, so D(y) = G(y) - 1 + e^{-y/V} = -(1-G(y)) + e^{-y/V}.

(V-y)D(y) = (V-y)[-(1-G(y)) + e^{-y/V}] = -(V-y)(1-G(y)) + (V-y)e^{-y/V}.

(V-y)e^{-y/V} → 0 (exponential decay).
(1-G(y)) → 0. (V-y)(1-G(y)): if 1-G(y) decays slower than 1/y, this could diverge. For uniform[0,V], 1-G(y) = 0 for y > V, so (V-y)D(y) = 0 for y > V. So u(∞) = 0 - (V - V/2) = -V/2. And G(∞) = 1. So u(∞)·G(∞) = -V/2 = μ_q - V = V/2 - V = -V/2. ✓

For q = p (exponential): 1-G(y) = e^{-y/V}, D(y) = 0, J(∞) = 0. u(∞) = 0 - 0 = 0. ✓

OK so [u·G]₀^∞ = (μ_q - V) - 0 = μ_q - V = -V/2 for uniform[0,V].

Now -∫₀^∞ G·u' dy = ∫₀^∞ (G + Vg)·D dy.

For uniform[0,V]: G(y) = y/V for y ∈ [0,V], 1 for y > V. g(y) = 1/V for y ∈ [0,V], 0 for y > V.

G + Vg = y/V + 1 for y ∈ [0,V], 1 + 0 = 1 for y > V.

D(y) = y/V - 1 + e^{-y/V} for y ∈ [0,V], e^{-y/V} for y > V.

∫₀^V (y/V + 1)(y/V - 1 + e^{-y/V}) dy + ∫_V^∞ 1·e^{-y/V} dy

First integral: ∫₀^V (y/V + 1)(y/V - 1) dy + ∫₀^V (y/V + 1)e^{-y/V} dy

= ∫₀^V (y²/V² - 1) dy + ∫₀^V (y/V + 1)e^{-y/V} dy

= [y³/(3V²) - y]₀^V + ∫₀^V (y/V)e^{-y/V} dy + ∫₀^V e^{-y/V} dy

= V/3 - V + V∫₀^1 u·e^{-u} du + V∫₀^1 e^{-u} du

= -2V/3 + V(1 - 1/e) + V(1 - 1/e)

Wait, ∫₀^1 u·e^{-u} du = [-(u+1)e^{-u}]₀^1 = -2/e + 1 = 1 - 1/e.

∫₀^1 e^{-u} du = 1 - 1/e.

So first integral = -2V/3 + V(1 - 1/e) + V(1 - 1/e) = -2V/3 + 2V(1 - 1/e) = -2V/3 + 2V - 2V/e = 4V/3 - 2V/e.

Second integral: ∫_V^∞ e^{-y/V} dy = V·e^{-1} = V/e.

Total: 4V/3 - 2V/e + V/e = 4V/3 - V/e.

So -∫₀^∞ G·u' dy = 4V/3 - V/e ≈ 1.333V - 0.368V = 0.965V.

E(p,q) - E(q,q) = (μ_q - V) + 0.965V = -V/2 + 0.965V = 0.465V.

But the actual answer is 0.097V. So there's still an error!

Hmm, let me recheck the direct computation.

E(p, q) = V(1 - 2/e) ≈ 0.264V.
E(q, q) = V/6 ≈ 0.167V.
E(p,q) - E(q,q) ≈ 0.097V.

And my formula gives 0.465V. So there's a significant error.

Let me recheck the integration by parts. Actually, let me recheck the formula:

E(p,q) - E(q,q) = ∫₀^∞ g(y) [(V-y)D(y) - J(y)] dy

For uniform[0,V], g(y) = 1/V for y ∈ [0,V]:

E(p,q) - E(q,q) = (1/V) ∫₀^V [(V-y)D(y) - J(y)] dy

D(y) = y/V - 1 + e^{-y/V} for y ∈ [0,V].
J(y) = H_F(y) - H_G(y) = [V - (V+y)e^{-y/V}] - y²/(2V) for y ∈ [0,V].

(V-y)D(y) = (V-y)(y/V - 1 + e^{-y/V}) = (V-y)(y/V - 1) + (V-y)e^{-y/V}

(V-y)(y/V - 1) = (V-y)(y-V)/V = -(V-y)²/V.

(V-y)D(y) - J(y) = -(V-y)²/V + (V-y)e^{-y/V} - V + (V+y)e^{-y/V} + y²/(2V)

= -(V² - 2Vy + y²)/V + (V-y)e^{-y/V} - V + (V+y)e^{-y/V} + y²/(2V)

= -V + 2y - y²/V + (V-y+V+y)e^{-y/V} - V + y²/(2V)

= -V + 2y - y²/V + 2V·e^{-y/V} - V + y²/(2V)

= -2V + 2y - y²/(2V) + 2V·e^{-y/V}

∫₀^V [-2V + 2y - y²/(2V) + 2V·e^{-y/V}] dy

= [-2Vy + y² - y³/(6V) - 2V²·e^{-y/V}]₀^V

= [-2V² + V² - V²/6 - 2V²/e] - [0 + 0 - 0 - 2V²]

= [-2V² + V² - V²/6 - 2V²/e + 2V²]

= V² - V²/6 - 2V²/e

= V²(5/6 - 2/e)

E(p,q) - E(q,q) = (1/V) · V²(5/6 - 2/e) = V(5/6 - 2/e) ≈ V(0.833 - 0.736) = 0.097V. ✓

So the direct computation of the integral gives 0.097V, matching the direct payoff computation. The error is in my integration by parts.

Let me redo the IBP carefully.

E(p,q) - E(q,q) = ∫₀^∞ g(y)·u(y) dy where u(y) = (V-y)D(y) - J(y).

IBP: ∫₀^∞ g·u dy = [G·u]₀^∞ - ∫₀^∞ G·u' dy.

I need u'(y):
u = (V-y)D - J
u' = -D + (V-y)D' - J'

D' = g - f (for continuous distributions)
J' = y(f - g) = -y·D' (wait, J = H_F - H_G = ∫₀^y x(f-g)dx, so J' = y(f-g) = y·h where h = f - g = -D')

So u' = -D + (V-y)(g-f) - y(f-g) = -D + (V-y)(g-f) + y(g-f) = -D + V(g-f) = -D - V(f-g) = -D - V·h

Since h = f - g and D = G - F, D' = g - f = -h, so h = -D'. Thus:

u' = -D - V(-D') = -D + V·D'

OK so u' = -D + V·D'. This is what I had before.

Now for uniform[0,V]:

For y ∈ [0,V]: D = y/V - 1 + e^{-y/V}, D' = 1/V - (1/V)e^{-y/V} = (1 - e^{-y/V})/V.
u' = -(y/V - 1 + e^{-y/V}) + V·(1 - e^{-y/V})/V = -y/V + 1 - e^{-y/V} + 1 - e^{-y/V} = 2 - y/V - 2e^{-y/V}.

For y > V: D = e^{-y/V}, D' = -(1/V)e^{-y/V}.
u' = -e^{-y/V} + V·(-(1/V)e^{-y/V}) = -e^{-y/V} - e^{-y/V} = -2e^{-y/V}.

Now ∫₀^∞ G·u' dy = ∫₀^V (y/V)(2 - y/V - 2e^{-y/V}) dy + ∫_V^∞ 1·(-2e^{-y/V}) dy

First: ∫₀^V (2y/V - y²/V² - 2y·e^{-y/V}/V) dy = [y²/V - y³/(3V²)]₀^V - (2/V)∫₀^V y·e^{-y/V} dy

= V - V/3 - (2/V)·V²(1 - 2/e) = 2V/3 - 2V(1 - 2/e) = 2V/3 - 2V + 4V/e = -4V/3 + 4V/e.

Wait, ∫₀^V y·e^{-y/V} dy = V²∫₀^1 u·e^{-u} du = V²(1 - 2/e). (Using ∫₀^1 ue^{-u}du = 1 - 2/e.)

So first part = 2V/3 - (2/V)·V²(1-2/e) = 2V/3 - 2V(1-2/e) = 2V/3 - 2V + 4V/e = -4V/3 + 4V/e.

Second: ∫_V^∞ -2e^{-y/V} dy = -2V·e^{-1} = -2V/e.

Total: -4V/3 + 4V/e - 2V/e = -4V/3 + 2V/e.

∫₀^∞ G·u' dy = -4V/3 + 2V/e ≈ -1.333V + 0.736V = -0.597V.

[u·G]₀^∞: u(∞)·G(∞) - u(0)·G(0).

u(∞) = (V-∞)·D(∞) - J(∞). For y > V: D(y) = e^{-y/V}, J(y) = H_F(y) - H_G(y) = [V - (V+y)e^{-y/V}] - V/2 (since H_G(y) = V/2 for y > V).

u(y) = (V-y)e^{-y/V} - V + (V+y)e^{-y/V} + V/2 = (V-y+V+y)e^{-y/V} - V/2 = 2V·e^{-y/V} - V/2.

u(∞) = 0 - V/2 = -V/2. G(∞) = 1. So u(∞)·G(∞) = -V/2.

u(0) = V·D(0) - 0 = V·(0 - 0 + 1) = V. Wait, D(0) = G(0) - F(0) = 0 - 0 = 0. So u(0) = 0. G(0) = 0. u(0)·G(0) = 0.

[u·G]₀^∞ = -V/2 - 0 = -V/2.

E(p,q) - E(q,q) = [u·G]₀^∞ - ∫₀^∞ G·u' dy = -V/2 - (-4V/3 + 2V/e) = -V/2 + 4V/3 - 2V/e = V(-1/2 + 4/3 - 2/e) = V(5/6 - 2/e) ≈ V(0.833 - 0.736) = 0.097V. ✓

So the IBP is correct. My error was in the subsequent simplification where I tried to express things in terms of D².

Let me redo that part. We have:

E(p,q) - E(q,q) = (μ_q - V) + ∫₀^∞ (G + Vg)·D dy

Wait, I had: E(p,q) - E(q,q) = [u·G]₀^∞ - ∫₀^∞ G·u' dy = (μ_q - V) - ∫₀^∞ G·(-D + V·D') dy

= (μ_q - V) + ∫₀^∞ G·D dy - V∫₀^∞ G·D' dy

∫₀^∞ G·D' dy = [G·D]₀^∞ - ∫₀^∞ g·D dy = (1·0 - 0·0) - ∫₀^∞ g·D dy = -∫₀^∞ g·D dy

So -V∫₀^∞ G·D' dy = V∫₀^∞ g·D dy.

E(p,q) - E(q,q) = (μ_q - V) + ∫₀^∞ G·D dy + V∫₀^∞ g·D dy = (μ_q - V) + ∫₀^∞ (G + Vg)·D dy.

For uniform[0,V]: μ_q - V = -V/2.

∫₀^∞ (G + Vg)·D dy: I computed this as 4V/3 - V/e ≈ 0.965V.

So E(p,q) - E(q,q) = -V/2 + 0.965V = 0.465V.

But the correct answer is 0.097V! So there's an error in my computation of ∫₀^∞ (G + Vg)·D dy.

Let me recompute. For uniform[0,V]:

G + Vg: for y ∈ [0,V]: y/V + V·(1/V) = y/V + 1. For y > V: 1 + 0 = 1.

D: for y ∈ [0,V]: y/V - 1 + e^{-y/V}. For y > V: e^{-y/V}.

∫₀^V (y
