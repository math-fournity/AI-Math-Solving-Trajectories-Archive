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
Copyright 2026 The Formal Conjectures Authors.

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

/-!
# Erdős Problem 521

*Reference:* [erdosproblems.com/521](https://www.erdosproblems.com/521)
-/

namespace Erdos521

open MeasureTheory Filter Polynomial
open scoped Topology

/-- `true` encodes the sign `+1`, `false` the sign `-1`. -/
def sign (b : Bool) : ℝ := if b then 1 else -1

/-- One fair coin: the uniform probability measure on `Bool`. -/
noncomputable def fairCoin : Measure Bool :=
  (2 : ENNReal)⁻¹ • (Measure.dirac true + Measure.dirac false)

/-- `fairCoin` gives each of the two signs mass `1/2`. Together with
`fairCoin_isProbabilityMeasure` this pins the definition down, so a proof stating the
same problem with a `Bernoulli(1/2)` measure is stating the same thing. -/
@[category API, AMS 60]
theorem fairCoin_apply (b : Bool) : fairCoin {b} = 2⁻¹ := by
  cases b <;> simp [fairCoin]

/-- `fairCoin` is a probability measure. -/
@[category API, AMS 60]
theorem fairCoin_isProbabilityMeasure : IsProbabilityMeasure fairCoin := by
  constructor
  simp [fairCoin]
  rw [ENNReal.inv_two_add_inv_two]

/-- The law of an infinite sequence of independent fair coins `(ε_k)_{k ≥ 0}`,
each uniform on `{-1, +1}`. -/
noncomputable def rademacherMeasure : Measure (ℕ → Bool) :=
  Measure.infinitePi (fun _ : ℕ ↦ fairCoin)

/-- The degree-`n` Littlewood polynomial `f_n(z) = ∑_{0 ≤ k ≤ n} ε_k z^k`. -/
noncomputable def littlewoodPolynomial (ω : ℕ → Bool) (n : ℕ) : ℝ[X] :=
  ∑ k ∈ Finset.range (n + 1), Polynomial.monomial k (sign (ω k))

/-- `R_n`: the number of distinct real roots of `f_n`. -/
noncomputable def realRootCount (ω : ℕ → Bool) (n : ℕ) : ℕ :=
  Set.ncard ((littlewoodPolynomial ω n).rootSet ℝ)

/-- The assertion asked about in Problem 521: almost surely `R_n / log n → 2/π`. -/
def Claim : Prop :=
  ∀ᵐ ω ∂rademacherMeasure,
    Tendsto (fun n : ℕ ↦ (realRootCount ω n : ℝ) / Real.log (n : ℝ))
      atTop (𝓝 ((2 : ℝ) / Real.pi))

/--
Let $(\epsilon_k)_{k\geq 0}$ be independently uniformly chosen at random from
$\{-1,1\}$. If $R_n$ counts the number of real roots of
$f_n(z)=\sum_{0\leq k\leq n}\epsilon_k z^k$ then is it true that, almost surely,
$$\lim_{n\to \infty}\frac{R_n}{\log n}=\frac{2}{\pi}?$$

The answer is no: this almost-sure limit fails. This result was obtained first by others, who
deserve the credit for the problem; the link is to an independent machine-checked proof by
Star Fleet Math.
-/
@[category research solved, AMS 11 60, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-521/Research/LateFourthFinal.lean"]
theorem erdos_521 : answer(False) ↔ Claim := by
  sorry

end Erdos521


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
