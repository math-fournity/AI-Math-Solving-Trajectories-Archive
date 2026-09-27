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
# Normality of Irrational Algebraic Numbers

It is unknown whether every irrational algebraic real number is normal in any integer base.
The stronger conjecture that every irrational algebraic real number is absolutely normal is stated
separately: normality in one base and normality in every base are not equivalent definitions.

*References:*
- [Wikipedia: Normal number](https://en.wikipedia.org/wiki/Normal_number)
- [BC01] Bailey, David H., and Richard E. Crandall. "On the random character of fundamental constant
  expansions." Experimental Mathematics 10.2 (2001): 175-190.
  https://projecteuclid.org/journals/experimental-mathematics/volume-10/issue-2/On-the-random-character-of-fundamental-constant-expansions/em/999188630.full
-/

open NormalNumber

namespace AlgebraicNormality

/-- A real number is irrational algebraic if it is algebraic over `ℚ` but not rational. -/
def IsIrrationalAlgebraic (x : ℝ) : Prop :=
  IsAlgebraic ℚ x ∧ Irrational x

/-- The strong normality conjecture: every irrational algebraic real is absolutely normal. -/
@[category research open, AMS 11 12 41]
theorem irrational_algebraic_absolutely_normal :
    answer(sorry) ↔ ∀ x : ℝ, IsIrrationalAlgebraic x → IsAbsolutelyNormal x := by
  sorry

/-- The weaker normality conjecture: every irrational algebraic real is normal in at least one
integer base `b ≥ 2`. -/
@[category research open, AMS 11 12 41]
theorem irrational_algebraic_normal_in_some_base :
    answer(sorry) ↔
      ∀ x : ℝ, IsIrrationalAlgebraic x → ∃ b : ℕ, 2 ≤ b ∧ IsNormalInBase b x := by
  sorry

/-- Absolute normality implies normality in at least one base. -/
@[category API, AMS 11]
theorem normal_in_some_base_of_absolutely_normal {x : ℝ} (hx : IsAbsolutelyNormal x) :
    ∃ b : ℕ, 2 ≤ b ∧ IsNormalInBase b x :=
  ⟨2, le_rfl, hx 2 le_rfl⟩

end AlgebraicNormality


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
