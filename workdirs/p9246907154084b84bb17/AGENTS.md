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
# Sum of three cubes

An integer `n : ℤ` can be written as a sum of three cubes (of integers) if and only if
`n` is not `4` or `5` mod `9`.

*References:*
 - [Wikipedia](https://en.wikipedia.org/wiki/Sums_of_three_cubes)
 - [mathoverflow/100324](https://mathoverflow.net/a/100324)
asked by user [*David Feldman*](https://mathoverflow.net/users/10909/david-feldman)
-/

namespace SumOfThreeCubes

variable {R : Type*} [Ring R]

/-- The predicate that `n : R` is a sum of three cubes. -/
def IsSumOfThreeCubes (n : R) : Prop :=
  ∃ x y z : R, n = x^3 + y^3 + z^3

@[category test, AMS 11]
theorem isSumOfThreeCubes_2 : IsSumOfThreeCubes (2 : ℤ) :=
  ⟨1, 1, 0, by norm_num⟩

@[category test, AMS 11]
theorem isSumOfThreeCubes_33 : IsSumOfThreeCubes (33 : ℤ) :=
  ⟨8866128975287528, -8778405442862239, -2736111468807040, by norm_num⟩

@[category test, AMS 11]
theorem isSumOfThreeCubes_42 : IsSumOfThreeCubes (42 : ℤ) :=
  ⟨-80538738812075974, 80435758145817515, 12602123297335631, by norm_num⟩

@[category test, AMS 11]
theorem mod_9_of_isSumOfThreeCubes (n : ℤ) (hn : IsSumOfThreeCubes n) :
    ¬(n ≡ 4 [ZMOD 9] ∨ n ≡ 5 [ZMOD 9]) := by
  rw [show (9 : ℤ) = (9 : ℕ) from rfl, ← ZMod.intCast_eq_intCast_iff _ _ 9,
    ← ZMod.intCast_eq_intCast_iff _ _ 9]
  obtain ⟨x, y, z, hn⟩ := hn
  replace hn := congrArg (fun x : ℤ ↦ (x : ZMod 9)) hn
  simp only [Int.cast_add, Int.cast_pow] at hn
  generalize (n : ZMod 9) = n at *
  generalize (x : ZMod 9) = x at *
  generalize (y : ZMod 9) = y at *
  generalize (z : ZMod 9) = z at *
  decide +revert

/--
Any rational number is a sum of three rational cubes.

First proved by Ryley in 1825, which can be found in [Ri1930].
The below parametrization is brought from the MSE answer [MSE].

[Ri1930] Richmond, H. W. "On Rational Solutions of $x^3 + y^3 + z^3 = R$." Proceedings of the Edinburgh Mathematical Society 2.2 (1930): 92-100.
[MSE] Kieren MacMillan, Proving that any rational number can be represented as the sum of the cubes of three rational numbers, https://math.stackexchange.com/q/4480969
-/
@[category research solved, AMS 11]
theorem isSumOfThreeCubesRat_any (r : ℚ) : IsSumOfThreeCubes r := by
  by_cases h : r = 0
  · exact ⟨0, 0, 0, by norm_num; exact h⟩
  · let x := (r ^ 6 + 45 * r ^ 4 - 81 * r ^ 2 + 27) / (6 * r * (r ^ 2 + 3) ^ 2)
    let y := (3 - r ^ 2) * (6 * r) / (r ^ 2 + 3) ^ 2
    let z := (r ^ 2 + 6 * r + 3) * (- r ^ 2 + 6 * r - 3) / (6 * r * (r ^ 2 + 3))
    use x, y, z
    simp only [x, y, z]
    field_simp
    ring


/-- An integer `n : ℤ` can be written as a sum of three cubes (of integers) if and only if
`n` is not `4` or `5` mod `9`. -/
@[category research open, AMS 11]
theorem isSumOfThreeCubes_iff_mod_9 :
    answer(sorry) ↔ ∀ n : ℤ, IsSumOfThreeCubes n ↔ ¬(n ≡ 4 [ZMOD 9] ∨ n ≡ 5 [ZMOD 9]) := by
  sorry

end SumOfThreeCubes


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
