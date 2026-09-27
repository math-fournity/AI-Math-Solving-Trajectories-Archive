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
# Erdős Problem 299

*References:*
- [erdosproblems.com/298](https://www.erdosproblems.com/298)
- [erdosproblems.com/299](https://www.erdosproblems.com/299)
- [Bl21] Bloom, T. F., On a density conjecture about unit fractions. arXiv:2112.03726 (2021).
-/

open Filter

namespace Erdos299

/--
Is there an infinite sequence $a_1 < a_2 < \dots$ such that $a_{i+1} - a_i = O(1)$ and no finite
sum of $\frac{1}{a_i}$ is equal to 1?

There does not exist such a sequence, which follows from the positive solution to
[erdosproblems.com/298] by Bloom [Bl21].

This was formalized in Lean 3 by Bloom and Mehta.
-/
@[category research solved, AMS 11 40, formal_proof using other_system at "https://github.com/b-mehta/unit-fractions/blob/master/src/final_results.lean"]
theorem erdos_299 : answer(False) ↔ (∃ (a : ℕ → ℕ),
    StrictMono a ∧ (∀ n, 0 < a n) ∧
    (fun n ↦ (a (n + 1) : ℝ) - a n) =O[atTop] (1 : ℕ → ℝ) ∧
    ∀ S : Finset ℕ, ∑ i ∈ S, (1 : ℝ) / a i ≠ 1) := by
  sorry

/--
The corresponding question is also false if one replaces sequences such that $a_{i+1} - a_i = O(1)$
with sets of positive density, as follows from [Bl21].

The statement is as follows:
If $A \subset \mathbb{N}$ has positive upper density (and hence certainly if $A$ has positive
density) then there is a finite $S \subset A$ such that $\sum_{n \in S} \frac{1}{n} = 1$.
-/
@[category research solved, AMS 11 40]
theorem erdos_299.variants.density : ∀ (A : Set ℕ), 0 ∉ A → 0 < A.upperDensity →
    ∃ S : Finset ℕ, ↑S ⊆ A ∧ ∑ n ∈ S, (1 : ℝ) / n = 1 := by
  sorry

end Erdos299


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
