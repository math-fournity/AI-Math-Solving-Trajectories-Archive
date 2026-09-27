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
# Euler's sum of powers conjecture

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Euler's_sum_of_powers_conjecture)
-/

namespace EulerSumOfPowers

/--
Euler's sum of powers conjecture states that for integers $n > 1$ and $k > 1$,
if the sum of $n$ positive integers each raised to the $k$-th power equals another integer
raised to the $k$-th power, then $n ≥ k$.

The conjecture is known to be false for $k = 4$ and $k = 5$,
but remains open for $k ≥ 6$.
-/
@[category research open, AMS 11]
theorem eulers_sum_of_powers_conjecture (n k b : ℕ) (hn : 1 < n) (hk : 5 < k) (a : Fin n → ℕ)
    (ha : ∀ i, a i > 0) (hsum : ∑ i, (a i) ^ k = b ^ k) : k ≤ n := by
  sorry

/-- Euler's sum of powers conjecture is false for $k=4$ (counterexample exists). -/
@[category research solved, AMS 11]
theorem eulers_sum_of_powers_conjecture.false_for_k4 : ¬ (∀ (n b : ℕ) (_ : 1 < n)
    (a: Fin n → ℕ) (_ : ∀ i, a i > 0) (_ : ∑ i, (a i) ^ 4 = b ^ 4), 4 ≤ n) := by
  push_neg
  use 3, 422481
  norm_num
  use ![95800, 217519, 414560]
  decide

/-- Euler's sum of powers conjecture is false for $k=5$ (counterexample exists). -/
@[category research solved, AMS 11]
theorem eulers_sum_of_powers_conjecture.false_for_k5 : ¬ (∀ (n b : ℕ) (_ : 1 < n)
    (a: Fin n → ℕ) (_ : ∀ i, a i > 0) (_ : ∑ i, (a i) ^ 5 = b ^ 5), 5 ≤ n) := by
  push_neg
  use 4, 144
  norm_num
  use ![27, 84, 110, 133]
  decide

end EulerSumOfPowers


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
