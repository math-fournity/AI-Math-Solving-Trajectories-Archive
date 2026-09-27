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
# Erdős Problem 105

*References:*
- [erdosproblems.com/105](https://www.erdosproblems.com/105)
- [Be83] Beck, József, *On the lattice property of the plane and some problems of Dirac, Motzkin
  and Erdős in combinatorial geometry*. Combinatorica (1983), 281-297.
- [ErPu95] Erdős, P. and Purdy, G., *Two combinatorial problems in the plane*. Discrete Comput.
  Geom. (1995), 441-443.
- [SzTr83] Szemerédi, Endre and Trotter, Jr., William T., *Extremal problems in discrete
  geometry*. Combinatorica (1983), 381-392.
-/

open EuclideanGeometry

namespace Erdos105

/--
Let $A,B\subset \mathbb{R}^2$ be disjoint sets of size $n$ and $n-3$ respectively, with not all
of $A$ contained on a single line. Is there a line which contains at least two points from $A$
and no points from $B$?

This has been disproved by Xichuan in the comments, who has found three explicit
counterexamples.
-/
@[category research solved, AMS 5 52, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos105.lean"]
theorem erdos_105 : answer(False) ↔
    ∀ A B : Finset ℝ², Disjoint A B → A.card = B.card + 3 →
      ¬ Collinear ℝ (A : Set ℝ²) →
      ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q] := by
  sorry

/--
A construction of Hickerson shows that this fails with $n-2$.
-/
@[category research solved, AMS 5 52]
theorem erdos_105.variants.hickerson : ¬ ∀ A B : Finset ℝ², Disjoint A B →
    A.card = B.card + 2 → ¬ Collinear ℝ (A : Set ℝ²) →
    ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q] := by
  sorry

/--
A result independently proved by Beck [Be83] and Szemerédi and Trotter [SzTr83] (see [211])
implies it is true with $n-3$ replaced by $cn$ for some constant $c>0$.
-/
@[category research solved, AMS 5 52]
theorem erdos_105.variants.beck_szemeredi_trotter : ∃ c > (0 : ℝ),
    ∀ A B : Finset ℝ², Disjoint A B → (B.card : ℝ) ≤ c * A.card →
      ¬ Collinear ℝ (A : Set ℝ²) →
      ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q] := by
  sorry

/--
It remains possible that this holds with $n-4$ (or in general with $n-O(1)$ or $(1-o(1))n$).
-/
@[category research open, AMS 5 52]
theorem erdos_105.variants.sub_four : answer(sorry) ↔
    ∀ A B : Finset ℝ², Disjoint A B → A.card = B.card + 4 →
      ¬ Collinear ℝ (A : Set ℝ²) →
      ∃ p ∈ A, ∃ q ∈ A, p ≠ q ∧ ∀ b ∈ B, b ∉ line[ℝ, p, q] := by
  sorry

end Erdos105


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
