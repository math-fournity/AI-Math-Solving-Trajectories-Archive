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
# Erdős Problem 325
*Reference:* [erdosproblems.com/325](https://www.erdosproblems.com/325)
-/

open Asymptotics Filter

namespace Erdos325

/-- A predicate for $n$ to be the sum of three $k$th powers. -/
def IsSumThreePower (k n : ℕ) : Prop := ∃ a b c, a ^ k + b ^ k + c ^ k = n

/-- The number of integers $\leq x$ which are the sum of three $k$th powers. -/
noncomputable def cardIsSumThreePowerBelow (k x : ℕ) : ℕ :=
  {n ∈ Set.Iic x | IsSumThreePower k n}.ncard

/--
Writing $f_{k, 3}(x)$ for the number of integers $\leq x$ which are the sum of three $k$th powers,
is it true that $f_{k, 3}(x) \gg x ^ (3 / k)$?
-/
@[category research open, AMS 11]
theorem erdos_325 :
     answer(sorry) ↔ ∀ k : ℕ, 3 ≤ k → (fun x : ℕ => (x : ℝ) ^ (3 / k : ℝ)) =O[atTop]
      (fun x : ℕ => (cardIsSumThreePowerBelow k x : ℝ)) := by
  sorry

/--
Writing $f_{k, 3}(x)$ for the number of integers $\leq x$ which are the sum of three $k$th powers,
is it even true that $f_{k, 3}(x) \gg_{\epsilon} x ^ (3 / k - \epsilon)$?
-/
@[category research open, AMS 11]
theorem erdos_325.variants.weaker :
    answer(sorry) ↔ ∀ ε > 0, ∀ k : ℕ, 3 ≤ k → (fun x : ℕ => (x : ℝ) ^ ((3 / k : ℝ) - ε)) =O[atTop]
      (fun x => (cardIsSumThreePowerBelow k x : ℝ)) := by
  sorry

/--
For $k = 3$, the best known is due to Wooley [Wo15]
[Wo15] Wooley, Trevor D., Sums of three cubes, II. Acta Arith. (2015), 73-100.
-/
@[category research solved, AMS 11]
theorem erdos_325.variants.wooley :
    (fun x : ℕ => (x : ℝ) ^ (0.917 : ℝ)) =O[atTop] (fun x => (cardIsSumThreePowerBelow 3 x : ℝ)) := by
  sorry

end Erdos325


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
