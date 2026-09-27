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
# Erdős Problem 288

*Reference:* [erdosproblems.com/288](https://www.erdosproblems.com/288)
-/

namespace Erdos288

/--
Is it true that there are only finitely many pairs of intervals $I_1$, $I_2$ such that
$$
\sum_{n_1 \in I_1} \frac{1}{n_1} + \sum_{n_2 \in I_2} \frac{1}{n_2} \in \mathbb{N}?
$$
-/
@[category research open, AMS 11]
theorem erdos_288 : answer(sorry) ↔ Set.Finite { I : Fin 2 → ℕ+ × ℕ+ |
    ∀ j, (I j).1 ≤ (I j).2 ∧
      ∃ n : ℕ+, (∑ j : Fin 2, ∑ nⱼ ∈ Set.Icc (I j).1 (I j).2, (nⱼ⁻¹ : ℚ)) = n } := by
  sorry

/--
This is still open even if $|I_2| = 1$.
-/
@[category research open, AMS 11]
theorem erdos_288.variants.i2_card_eq_1 : answer(sorry) ↔ Set.Finite { (I, n₂) : (ℕ+ × ℕ+) × ℕ+ |
    I.1 ≤ I.2 ∧ ∃ n : ℕ+, ∑ n₁ ∈ Set.Icc I.1 I.2, (n₁⁻¹ : ℚ) + (n₂⁻¹ : ℚ) = n } := by
  sorry

/--
It is perhaps true with two intervals replaced by any $k$ intervals.
-/
@[category research open, AMS 11]
theorem erdos_288.variants.k_intervals : answer(sorry) ↔ ∀ k, Set.Finite { I : Fin k → ℕ+ × ℕ+ |
    ∀ j, (I j).1 ≤ (I j).2 ∧
      ∃ n : ℕ+, (∑ j : Fin k, ∑ nⱼ ∈ Set.Icc (I j).1 (I j).2, (nⱼ⁻¹ : ℚ)) = n } := by
  sorry

/--
Is it true for any $k > 2$ that only finitely many $k$ intervals satisfy this condition?
-/
@[category research open, AMS 11]
theorem erdos_288.variants.exists_k_gt_2 : answer(sorry) ↔
    ∃ k > 2, Set.Finite { I : Fin k → ℕ+ × ℕ+ |
      ∀ j, (I j).1 ≤ (I j).2 ∧
        ∃ n : ℕ+, (∑ j : Fin k, ∑ nⱼ ∈ Set.Icc (I j).1 (I j).2, (nⱼ⁻¹ : ℚ)) = n } := by
  sorry

end Erdos288


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
