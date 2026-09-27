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
# Erdős Problem 254

*References:*
- [erdosproblems.com/254](https://www.erdosproblems.com/254)
- [Ca60] Cassels, J. W. S., On the representation of integers as the sums of distinct summands taken
  from a fixed set. Acta Sci. Math. (Szeged) (1960), 111-124.
-/

open Filter Set

namespace Erdos254

/--
An integer `n` can be written as a sum of distinct elements of `A`.
-/
def IsSumOfDistinct (A : Set ℕ) (n : ℕ) : Prop :=
  ∃ S : Finset ℕ, (S : Set ℕ) ⊆ A ∧ S.sum (fun x ↦ x) = n

/-- The hypothesis `¬ Summable (fun n : A ↦ distToNearestInt (θ * n))` used below says exactly
that the partial sums of `‖θ n‖` over `n ∈ A` diverge, which is the form the linked proof uses.
`distToNearestInt` is nonnegative, so this is an instance of
`not_summable_subtype_iff_tendsto_sum_indicator`. -/
@[category API, AMS 11]
theorem not_summable_iff_tendsto_partial_sums (A : Set ℕ) (θ : ℝ) :
    ¬ Summable (fun n : A ↦ distToNearestInt (θ * (n : ℝ))) ↔
      Tendsto (fun N : ℕ =>
          ∑ n ∈ Finset.range N, A.indicator (fun n => distToNearestInt (θ * (n : ℝ))) n)
        atTop atTop :=
  not_summable_subtype_iff_tendsto_sum_indicator
    (f := fun m : ℕ => distToNearestInt (θ * (m : ℝ))) fun _ => distToNearestInt_nonneg _

/--
Let $A\subseteq \mathbb{N}$ be such that $\lvert A\cap [1,2x]\rvert -\lvert A\cap [1,x]\rvert \to
\infty\textrm{ as }x\to \infty$ and $\sum_{n\in A} \{ \theta n\}=\infty$ for every $\theta\in
(0,1)$, where $\{x\}$ is the distance of $x$ from the nearest integer. Then every sufficiently large
integer is the sum of distinct elements of $A$.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-254/Research/Basic.lean"]
theorem erdos_254 :
    ∀ (A : Set ℕ),
      (Tendsto (fun x : ℕ ↦ (A ∩ Icc 1 (2 * x)).ncard - (A ∩ Icc 1 x).ncard) atTop atTop) ∧
      (∀ θ : ℝ, 0 < θ → θ < 1 → ¬ Summable (fun n : A ↦ distToNearestInt (θ * (n : ℝ)))) →
        ∀ᶠ m in atTop, IsSumOfDistinct A m := by
  sorry

/--
Cassels [Ca60] proved this under the alternative hypotheses $\lim \frac{\lvert A\cap [1,2x]\rvert
-\lvert A\cap [1,x]\rvert}{\log\log x}=\infty$ and $\sum_{n\in A} \{ \theta n\}^2=\infty$ for every
$\theta\in (0,1)$.
-/
@[category research solved, AMS 11]
theorem erdos_254.variants.cassels :
    ∀ (A : Set ℕ),
      (Tendsto (fun x : ℕ ↦ (((A ∩ Icc 1 (2 * x)).ncard : ℝ) -
        ((A ∩ Icc 1 x).ncard : ℝ)) / Real.log (Real.log x)) atTop atTop) ∧
      (∀ θ : ℝ, 0 < θ → θ < 1 → ¬ Summable (fun n : A ↦ (distToNearestInt (θ * (n : ℝ)))^2)) →
        ∀ᶠ m in atTop, IsSumOfDistinct A m := by
  sorry

end Erdos254


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
