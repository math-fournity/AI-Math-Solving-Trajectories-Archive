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
# Erdős Problem 318

*References:*
  - [erdosproblems.com/318](https://www.erdosproblems.com/318)
  - [ErSt75] Erdős, P. and Straus, E. G., Solution to Problem 387. Nieuw Arch. Wisk. (1975), 183.
  - [Sa75] Sattler, R., Solution to Problem 387. Nieuw Arch. Wisk. (1975), 184-189.
  - [Sa82b] Sattler, R., On Erdős property P₁ for the arithmetical sequence. Nederl. Akad. Wetensch.
    Indag. Math. (1982), 347--352.
  - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
    theory. Monographies de L'Enseignement Mathematique (1980).
  - [La26] D. Larsen, [Erdős problem 318](https://github.com/Larsen-Daniel/Erdos-318/blob/main/318.pdf) (2026)
-/

open Set Real

namespace Erdos318

/-- A set `A : Set ℕ` is said to have property `P₁` if for any nonconstant sequence
`f : A → {-1, 1}`, one can always select a finite, nonempty subset `S ⊆ A \ {0}` such that
`∑ n ∈ S, fₙ / n = 0`. This is defined in [Sa82b]. -/
def P₁ (A : Set ℕ) : Prop := ∀ (f : ℕ → ℝ),
  f ∘ (Subtype.val : (A \ {0} : Set ℕ) → ℕ) ≠ (fun _ => 1) →
  f ∘ (Subtype.val : (A \ {0} : Set ℕ) → ℕ) ≠ (fun _ => - 1) →
  Set.range f ⊆ {1, -1} →
  ∃ S : Finset ℕ, S.Nonempty ∧ ↑S ⊆ A \ {0} ∧ ∑ n ∈ S, f n / n = 0

/-- `ℕ` has property `P₁`. This is proved in [ErSt75]. -/
@[category research solved, AMS 11]
theorem erdos_318.variants.univ : P₁ univ := by
  sorry

/-- Sattler proved in [Sa75] that the set of odd numbers has property `P₁`. -/
@[category research solved, AMS 11]
theorem erdos_318.variants.odd : P₁ {n | Odd n} := by
  sorry

/-- The set of squares does not have property `P₁`. -/
@[category test, AMS 11]
theorem erdos_318.variants.squares : ¬ P₁ ({n | IsSquare n}) := by
  simp only [P₁, not_forall, not_exists, not_and]
  -- Consider the function `f` that sends `1` to `1` and sends all other numbers to `-1`.
  refine ⟨fun n => if n = 1 then 1 else - 1, fun h => ?_, fun h => ?_,
    fun x ⟨y, hy⟩ => ?_, fun S h hs => ?_⟩
  · have : (- 1 : ℝ) = 1 := by simpa using congr_fun h ⟨4, ⟨⟨2, by grind⟩, by grind⟩⟩
    grind
  · have : 1 = (- 1 : ℝ) := by simpa using congr_fun h ⟨1, ⟨IsSquare.one, by grind⟩⟩
    grind
  · by_cases x = 1 <;> grind
  -- Consider two cases: `1 ∈ S` or `1 ∉ S`. In the first case, the finite sum over `S` is bounded
  -- below by `1 - (π ^ 2 / 6 - 1)`, which is positive. In the second case, the finite sum over `S`
  -- is negative.
  by_cases h1 : 1 ∈ S
  · rw [Finset.sum_eq_add_sum_diff_singleton h1, Finset.sum_congr rfl
      (g := fun n : ℕ => (- 1 : ℝ) / n)]
    · simp only [↓reduceIte, Nat.cast_one, div_self one_ne_zero, ← ne_eq, div_eq_mul_one_div
        (- 1 : ℝ), ← Finset.mul_sum, neg_one_mul (∑ x ∈ S \ {1}, 1 / (x : ℝ)), ← sub_eq_add_neg]
      apply ne_of_gt
      calc
      _ < 1 - (π ^ 2 / 6 - 1) := by
        have : π ^ 2 < 3.15 ^ 2 := by gcongr; exact Real.pi_lt_d2
        linarith
      _ = 1 - (∑' n : ℕ, 1 / (n : ℝ) ^ 2 - 1) := by congr; exact hasSum_zeta_two.tsum_eq.symm
      _ ≤ 1 - ∑ n ∈ S \ {1}, 1 / (n : ℝ) := by
        gcongr
        have : 1 = 1 / ((1 : ℕ) : ℝ) := by norm_cast; grind
        nth_rewrite 3 [this]
        rw [le_sub_iff_add_le, ← Finset.sum_eq_sum_diff_singleton_add h1]
        let S' := S.preimage (· ^ 2) (Function.Injective.injOn
          (Nat.pow_left_injective (by decide)))
        have hS' : S'.map ⟨(· ^ 2), Nat.pow_left_injective (by decide)⟩ = S := by
          apply Finset.coe_injective
          have h : (S : Set ℕ) ⊆ Set.range (· ^ 2) :=
            hs.trans (by simp [isSquare_iff_exists_sq, Set.subset_def])
          simpa [S', Set.image_preimage_eq_iff] using h
        rw [← hS', Finset.sum_map, Function.Embedding.coeFn_mk]
        simpa [Nat.cast_pow] using Summable.sum_le_tsum S' (fun _ _ => by positivity) (by simp)
    · intro _ _; grind
  · suffices ∑ n ∈ S, (fun n ↦ if n = 1 then 1 else - 1) n / (n : ℝ) < 0 from by linarith
    refine Finset.sum_neg (fun p hp => ?_) h
    have : p ≠ 1 := by grind
    simp_all [neg_div, zero_lt_iff, (not_iff_not.2 mem_singleton_iff).1 (hs hp).2]

/-- For any set `A` containing exactly one even number, `A` does not have property `P₁`. Sattler
[Sa82] credits this observation to Erdős, who presumably found this after [ErGr80]. -/
@[category research solved, AMS 11]
theorem erdos_318.variants.contain_single_even {A : Set ℕ} (hA : {n | n ∈ A ∧ Even n}.ncard = 1) :
    ¬ P₁ A := by
  sorry

/-- There exists a se

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
