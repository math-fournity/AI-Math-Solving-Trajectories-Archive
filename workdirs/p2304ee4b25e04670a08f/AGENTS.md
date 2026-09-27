# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

# Problem

/-
Copyright 2025 The Formal Conjectures Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-/

import FormalConjecturesUtil
import FormalConjectures.Millenium.RiemannHypothesis

/-!
# Artin's conjecture on primitive roots

Artin's conjecture predicts, given an integer $a$, densities of primes $p$ for which
$a$ is a primitive root modulo $p$. Under certain conditions (when $a$ is not a
power and its squarefree part is $1\pmod{4}$) the density is given by Artin's constant
$$\prod_{p\ \text{prime}} \left(1 - \frac{1}{p(p - 1)}\right).$$
For more general values of $a$, this constant must be corrected by certain factors.
- When $a = b^m$, $m$ is a maximal odd power, the squarefree part of $b$ satisfies
  $b_0 \not\equiv 1\pmod{4}$. Then Artin's constant should be multiplied by
  $$\prod_{p \mid m} \frac{p(p - 2)}{p^2 - p - 1}.$$
- When $a = b^m$, $m$ is a maximal power, the squarefree part of $b$ satisfies
  $b_0\equiv 1\pmod{4}$. Then Artin's constant should be multiplied by the factor in
  the above bullet, as well as an additional entanglement factor from the primes dividing
  $\gcd(b_0, m)$ and primes dividing $b_0$:
  $$1 - \prod_{p \mid \gcd(b_0, m)} \frac{1}{2 - p}
  \prod_{p \mid b_0, p\nmid m} \frac{1}{1 + p - p^2}.$$
- When $a = -1$ or $a$ is a square, then the density is $0$.

Note that Artin's conjecture has been proved subject to the Generalized Riemann Hypothesis
[Ho67].

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Artin%27s_conjecture_on_primitive_roots)
- [A85397](https://oeis.org/A85397)
- [LMS14](https://arxiv.org/pdf/1112.4816) Lenstra, H.W. et al. "Character sums for primitive root densities" _arXiv:1112.4816_ [math.NT] (2014).
- [Ho67] Hooley, C. "On Artin's conjecture." _Journal für die reine und angewandte Mathematik_ 225 (1967): 209-220.
-/

open GRH
open scoped Topology Nat

namespace ArtinPrimitiveRootsConjecture

/-- Let $S(a)$ be the set of primes such that $a$ is a primitive root modulo $p$. -/
abbrev S (a : ℤ) : Set ℕ :=
  {p : ℕ | p.Prime ∧ orderOf (a : ZMod p) = (p-1 : ℕ)}

/--
**Artin's Constant** is defined to be the product
$$\prod_{p\ \text{prime}} \left(1 - \frac{1}{p(p - 1)}\right)$$.
-/
noncomputable def ArtinConstant : ℝ :=
  ∏' p : Nat.Primes, (1 - 1 / (p * (p - 1)) : ℝ)

/--
Artin's conjecture on $S(a)$ when $a = b^m$ is a power, where $m$ is odd and maximal,
requires a correction factor to multiply `ArtinConstant` and is given by
$$\prod_{p \mid m} \frac{p(p - 2)}{p^2 - p - 1}.$$
-/
-- Eq. (1.2) of https://arxiv.org/pdf/1112.4816
noncomputable def powCorrectionFactor (m : ℕ) : ℝ :=
  ∏ p ∈ m.primeFactors, p * (p - 2 : ℝ) / (p ^ 2 - p - 1)

/--
Artin's conjecture on $S(a)$ when $a = b^m$ is a power, and the squarefree part
of $b_0\equiv 1\pmod{4}$, requires a further correct factor to
`ArtinConstant * powCorrectionFactor m`, which modifies primes which divide
$\gcd(b_0, m)$ and primes which do not divide $m$ separately as
$$ 1 - \prod_{p \mid \gcd(b_0, m)} \frac{1}{2 - p}
  \prod_{p \mid b_0, p\nmid m} \frac{1}{1 + p - p^2}.$$
-/
-- Eq. (1.4) of https://arxiv.org/pdf/1112.4816
noncomputable def entanglementFactor (b : ℕ) (m : ℕ) : ℝ :=
  (1 - (∏ p ∈ (b.squarefreePart.gcd m).primeFactors, 1 / (2 - p : ℝ)) *
    (∏ p ∈ b.squarefreePart.primeFactors \ m.primeFactors, 1 / (1 + p - p ^ 2 : ℝ)))
/--
**Artin's Conjecture on Primitive Roots**, first half.
Let $a$ be an integer that is not a square number and not $−1$. Then the set $S(a)$
of primes $p$ such that $a$ is a primitive root modulo $p$ has a positive asymptotic
density inside the set of primes. In particular, $S(a)$ is infinite.
-/
@[category research open, AMS 11]
theorem artin_primitive_roots.parts.i (a : ℤ) (ha : ¬IsSquare a) (ha' : a ≠ -1) :
    ∃ x > 0, (S a).HasDensity x {p | p.Prime} := by
  sorry

/--
**Artin's Conjecture on Primitive Roots**, first half, conditional on GRH.
-/
@[category research solved, AMS 11]
theorem conditional_artin_primitive_roots.parts.i (a : ℤ) (ha : ¬IsSquare a) (ha' : a ≠ -1)
    (h : type_of% generalized_riemann_hypothesis) :
    ∃ x > 0, (S a).HasDensity x {p | p.Prime} := by
  sorry

/--
**Artin's Conjecture on Primitive Roots**, second half.
Write $a = a_0 b^2$ where $a_0$ is squarefree. Under the conditions that $a$ is not a perfect
power and $a_0\not\equiv 1\pmod{4}$ (sequence A85397 in the OEIS), the density of the set
$S(a)$ of primes $p$ such that $a$ is a primitive root modulo $p$ is independent of $a$ and
equals Artin's constant.
-/
@[category research open, AMS 11]
theorem artin_pri

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
