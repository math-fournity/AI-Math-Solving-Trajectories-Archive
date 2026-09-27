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
# Erdős Problem 340

*Reference:* [erdosproblems.com/340](https://www.erdosproblems.com/340)
-/

open Filter Finset
open scoped Real Pointwise

namespace Erdos340

@[category test, AMS 5]
theorem greedySidon_go_singleton_two : (greedySidon.go {1} (by simp [IsSidon]) 2).val = 2 := by
  decide +native

@[category test, AMS 5]
theorem greedySidon_go_pair_three : (greedySidon.go {1, 2} (by simp [IsSidon]) 3).val = 4 := by
  decide +native

@[category test, AMS 5]
theorem greedySidon_zero : greedySidon 0 = 1 := rfl

@[category test, AMS 5]
theorem greedySidon_one : greedySidon 1 = 2 := by
  decide +native

@[category test, AMS 5]
theorem greedySidon_two : greedySidon 2 = 4 := by
  decide +native

@[category test, AMS 5]
theorem greedySidon_three : greedySidon 3 = 8 := by
  decide +native
@[category test, AMS 5]
theorem greedySidon_four : greedySidon 4 = 13 := by
  decide +native

@[category test, AMS 5]
theorem greedySidon_five : greedySidon 5 = 21 := by
  decide +native

@[category test, AMS 5]
theorem greedySidon_ten : greedySidon 10 = 97 := by
  decide +native

/--
Let $A = \{1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, \ldots\}$ be the greedy Sidon sequence:
we begin with $1$ and iteratively include the next smallest integer that preserves the
Sidon property (i.e. there are no non-trivial solutions to $a + b = c + d$). What is the
order of growth of $A$? Is it true that $|A \cap \{1, \ldots, N\}| \gg N^{1/2 - \varepsilon}$
for all $\varepsilon > 0$ and large $N$?
-/
@[category research open, AMS 5]
theorem erdos_340 (ε : ℝ) (hε : ε > 0) :
    (fun n : ℕ ↦ √n / n ^ ε) =O[atTop]
      fun n : ℕ ↦ ((Set.range greedySidon ∩ Set.Icc 1 n).ncard : ℝ) := by
  sorry

/--
Let $A = \{1, 2, 4, 8, 13, 21, 31, 45, 66, 81, 97, \ldots\}$ be the greedy Sidon sequence:
we begin with $1$ and iteratively include the next smallest integer that preserves the
Sidon property (i.e. there are no non-trivial solutions to $a + b = c + d$). What is the
order of growth of $A$? Is it true that $|A \cap \{1, \ldots, N\}| \gg N^{1/2 - \varepsilon}$
for all $\varepsilon > 0$ and large $N$?
-/
@[category research open, AMS 5]
theorem erdos_340.variants.isTheta (ε : ℝ) (hε : ε > 0) :
    (fun n : ℕ ↦ ((Set.range greedySidon ∩ Set.Icc 1 n).ncard : ℝ)) =Θ[atTop]
      (answer(sorry) : ℕ → ℝ) := by
  sorry

/--
It is trivial that this sequence grows at least like $\gg N^{1/3}$.
-/
@[category textbook, AMS 5]
theorem erdos_340.variants.third (ε : ℝ) (hε : ε > 0) :
    (fun n : ℕ ↦ (n : ℝ) ^ ((1 : ℝ) / 3)) =O[atTop]
      fun n : ℕ ↦ ((Set.range greedySidon ∩ Set.Icc 1 n).ncard : ℝ) := by
  sorry

/--
Erdős and Graham [ErGr80] also asked about the difference set $A - A$ and whether this has
positive density.

[ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
theory. Monographies de L'Enseignement Mathematique (1980).
-/
@[category research open, AMS 5]
theorem erdos_340.variants.sub_hasPosDensity :
    Set.HasPosDensity (Set.range greedySidon - Set.range greedySidon) := by
  sorry

/--
Erdős and Graham [ErGr80] also asked about the difference set $A - A$ and whether this
contains $22$, which it does.

[ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
theory. Monographies de L'Enseignement Mathematique (1980).
-/
@[category research solved, AMS 5]
theorem erdos_340.variants._22_mem_sub :
    22 ∈ Set.range greedySidon - Set.range greedySidon := by
  have h : (22 : ℕ) = greedySidon 14 - greedySidon 13 := by decide +native
  rw [h]
  exact Set.sub_mem_sub (Set.mem_range_self 14) (Set.mem_range_self 13)

/--
The smallest integer which is unknown to be in $A - A$ is $33$.
 -/
@[category research open, AMS 5]
theorem erdos_340.variants._33_mem_sub : answer(sorry) ↔
    33 ∈ Set.range greedySidon - Set.range greedySidon := by
  sorry

-- Formalisation note: there is some slight ambiguity in the meaning of
-- "almost all" so we provide two variants for "all but finitely many"
-- and "outside of a set of density zero"; there may be other reasonable
-- interpretations
/--
It may be true that all or almost all integers are in $A - A$.
-/
@[category research open, AMS 5]
theorem erdos_340.variants.cofinite_sub : answer(sorry) ↔
    ∀ᶠ n in cofinite, n ∈ Set.range greedySidon - Set.range greedySidon := by
  sorry

/--
It may be true that all or almost all integers are in $A - A$.
-

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
