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

/-!
# Infinitude of Wall–Sun–Sun primes

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime)
-/

open Algebra (IsQuadraticExtension)
open NumberField

namespace QuadraticAlgebra
variable {d : ℤ} [Fact <| Squarefree d] [Fact <| d ≠ 1]

/-- The discriminant of `ℚ[√d]` for `d ≥ 2` squarefree congruent to 1 mod 4 is `d`. -/
@[category textbook, AMS 11, simp]
lemma discr_rat_of_modEq_one (hd₄ : d ≡ 1 [ZMOD 4]) : discr (QuadraticAlgebra ℚ d 0) = d := by
  sorry

/-- The discriminant of `ℚ[√d]` for `d ≥ 2` squarefree not congruent to 1 mod 4 is `4 * d`. -/
@[category textbook, AMS 11, simp]
lemma discr_rat_of_not_modEq_one (hd₄ : ¬ d ≡ 1 [ZMOD 4]) :
    discr (QuadraticAlgebra ℚ d 0) = 4 * d := by
  sorry

end QuadraticAlgebra

namespace Algebra
variable {K L : Type*} [Field K] [Field L] [Algebra K L]

variable (K L) in
/-- A quadratic algebra `L` over a field `K` is isomorphic to the explicit quadratic algebra
`QuadraticAlgebra K a b` for some `a b : K`. -/
@[category textbook, AMS 11]
lemma exists_quadraticAlgebra_of_isQuadraticExtension [IsQuadraticExtension K L] :
    ∃ a b, Nonempty (L ≃ₐ[K] QuadraticAlgebra K a b) := by
  sorry

/-- An algebra `L` is quadratic over a field `K` iff it is isomorphic to the explicit quadratic
algebra `QuadraticAlgebra K a b` for some `a b : K`. -/
@[category textbook, AMS 11]
lemma isQuadraticExtension_iff_exists_quadraticAlgebra :
    IsQuadraticExtension K L ↔ ∃ a b, Nonempty (L ≃ₐ[K] QuadraticAlgebra K a b) where
  mp _ := exists_quadraticAlgebra_of_isQuadraticExtension ..
  mpr := by rintro ⟨a, b, ⟨e⟩⟩; sorry

end Algebra

namespace NumberField
variable {K : Type*} [Field K] [NumberField K]

variable (K) in
/-- A quadratic number field `K` is isomorphic to the explicit quadratic field
`QuadraticAlgebra ℚ d 0` for some squarefree `d : ℤ` not equal to 1. -/
@[category textbook, AMS 11]
lemma exists_quadraticAlgebra_of_isQuadraticExtension [IsQuadraticExtension ℚ K] :
    ∃ d ≠ (1 : ℤ), Squarefree d ∧ Nonempty (K ≃+* QuadraticAlgebra ℚ d 0) := by
  sorry

/-- A number field `K` is quadratic iff it is isomorphic to the explicit quadratic field
`QuadraticAlgebra ℚ d 0` for some squarefree `d : ℤ` not equal to 1. -/
@[category textbook, AMS 11]
lemma isQuadraticExtension_iff_exists_quadraticAlgebra :
    IsQuadraticExtension ℚ K ↔
      ∃ d ≠ (1 : ℤ), Squarefree d ∧ Nonempty (K ≃+* QuadraticAlgebra ℚ d 0) where
  mp _ := exists_quadraticAlgebra_of_isQuadraticExtension _
  mpr := by rintro ⟨d, hd₁, hd, ⟨e⟩⟩; sorry

/-- Fundamental discriminants are those integers `D` that appear as discriminants of quadratic
fields.

`D` is a fundamental discriminant if it is either of the form `4m` for `m` congruent to `2` or `3`
mod `4` squarefree, or if it congruent to `1` mod `4` and squarefree. -/
def IsFundamentalDiscr (D : ℤ) : Prop :=
  4 ∣ D ∧ ¬ D / 4 ≡ 1 [ZMOD 4] ∧ Squarefree (D / 4) ∨ D ≠ 1 ∧ D ≡ 1 [ZMOD 4] ∧ Squarefree D

/-- An integer `D` is a fundamental discriminant iff it is the discriminant of the explicit
quadratic field `QuadraticAlgebra ℚ d 0` for some squarefree `d : ℤ` not equal to 1. -/
@[category textbook, AMS 11]
lemma isFundamentalDiscr_iff_exists_discr_quadraticAlgebra {D : ℤ} :
    IsFundamentalDiscr D ↔ ∃ (d : ℤ) (_ : Fact <| d ≠ 1) (_ : Fact <| Squarefree d),
      discr (QuadraticAlgebra ℚ d 0) = D where
  mp := by
    rintro (⟨⟨d, rfl⟩, hD₄, hD⟩ | ⟨hD₁, hD₄, hD⟩)
    · simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, mul_div_cancel_left₀] at hD hD₄
      have : Fact <| d ≠ 1 := ⟨by rintro rfl; simp at hD₄⟩
      have : Fact <| Squarefree d := ⟨hD⟩
      exact ⟨d, inferInstance, inferInstance, QuadraticAlgebra.discr_rat_of_not_modEq_one hD₄⟩
    · have : Fact <| D ≠ 1 := ⟨hD₁⟩
      have : Fact <| Squarefree D := ⟨hD⟩
      exact ⟨D, inferInstance, inferInstance, QuadraticAlgebra.discr_rat_of_modEq_one hD₄⟩
  mpr := by
    rintro ⟨d, _, _, rfl⟩; by_cases hd₄ : d ≡ 1 [ZMOD 4] <;> simp [*, IsFundamentalDiscr, Fact.out]

/-- An integer `D` is a fundamental discriminant iff it is the discriminant of some number field. -/
@[category textbook, AMS 11]
lemma isFundamentalDiscr_iff_exists_discr_numberField {D : ℤ} :
    IsFundamentalDiscr D ↔
      ∃ (K : Type) (_ : Field K) (_ : NumberField K), IsQuadraticExtension ℚ K ∧ discr K = D := by
  rw [isFundamentalDiscr_iff_exists_discr_quadraticAlgebra]
  constructor
  · rintro ⟨d, _,

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
