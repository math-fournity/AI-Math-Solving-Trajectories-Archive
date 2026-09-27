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
# Erdős Problem 46

*References:*
- [erdosproblems.com/46](https://www.erdosproblems.com/46)
- [Cr03] Croot, III, Ernest S., *On a coloring conjecture about unit fractions*. Ann. of Math. (2)
  (2003), 545-556.
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
  theory*. Monographies de L'Enseignement Mathematique (1980).
-/

namespace Erdos46

/--
Does every finite colouring of the integers have a monochromatic solution to
$1=\sum \frac{1}{n_i}$ with $2\leq n_1<\cdots <n_k$?

The answer is yes, as proved by Croot [Cr03] - indeed, there are infinitely many disjoint such
monochromatic solutions.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos46.lean"]
theorem erdos_46 :
    answer(True) ↔
    -- For any finite colouring of the integers
    ∀ (𝓒 : ℕ → ℕ), (Set.range 𝓒).Finite →
      -- there are integers `2 ≤ n₁ < ⋯ < n_k`
      ∃ S : Finset ℕ, (∀ n ∈ S, 2 ≤ n) ∧
        -- whose reciprocals sum to `1`
        ∑ n ∈ S, (1 / n : ℚ) = 1 ∧
        -- and which all have the same colour
        (𝓒 '' (S : Set ℕ)).Subsingleton := by
  sorry

/--
Croot [Cr03] proved more: there are infinitely many disjoint such monochromatic solutions.
-/
@[category research solved, AMS 5 11]
theorem erdos_46.variants.infinitely_many_disjoint :
    answer(True) ↔
    ∀ (𝓒 : ℕ → ℕ), (Set.range 𝓒).Finite →
      ∃ S : ℕ → Finset ℕ, (∀ i j, i ≠ j → Disjoint (S i) (S j)) ∧
        ∀ i, (∀ n ∈ S i, 2 ≤ n) ∧ ∑ n ∈ S i, (1 / n : ℚ) = 1 ∧
          (𝓒 '' (S i : Set ℕ)).Subsingleton := by
  sorry

/--
In [ErGr80] they also ask for a monochromatic representation of any $\frac{a}{b}>0$.
-/
@[category research solved, AMS 5 11]
theorem erdos_46.variants.positive_rat :
    answer(True) ↔
    ∀ (𝓒 : ℕ → ℕ), (Set.range 𝓒).Finite → ∀ q : ℚ, 0 < q →
      ∃ S : Finset ℕ, (∀ n ∈ S, 2 ≤ n) ∧ ∑ n ∈ S, (1 / n : ℚ) = q ∧
        (𝓒 '' (S : Set ℕ)).Subsingleton := by
  sorry

end Erdos46


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
