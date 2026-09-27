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
# Erdős Problem 193

References:
- [erdosproblems.com/193](https://www.erdosproblems.com/193)
- [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
  theory. Monographies de L'Enseignement Mathematique (1980).
- [GeRa79] Gerver, Joseph L. and Ramsey, L. Thomas, "On certain sequences of lattice points."
  Pacific J. Math. (1979), 357-363.
-/

open Set

namespace Erdos193

/-- An $S$-walk is a sequence where every difference is in $S$. -/
def IsSWalk {V : Type*} [AddCommGroup V] (S : Set V) (a : ℕ → V) : Prop :=
  ∀ n, a (n + 1) - a n ∈ S

/-- True if set $A$ contains 3 distinct collinear points over $R$. -/
def HasCollinearTriple (R) {V : Type*} [DivisionRing R] [AddCommGroup V] [Module R V] (A : Set V) : Prop :=
  ∃ x ∈ A, ∃ y ∈ A, ∃ z ∈ A, x ≠ y ∧ y ≠ z ∧ x ≠ z ∧ Collinear R ({x, y, z} : Set V)

/--
Let $S \subseteq \mathbb{Z}^3$ be a finite set and let $A = \lbrace a_1, a_2, \ldots \rbrace$ be
an infinite $S$-walk, so that $a_{i+1} - a_i \in S$ for all $i$. Must $A$ contain three collinear
points?
-/
@[category research open, AMS 5]
theorem erdos_193 :
    answer(sorry) ↔ ∀ S : Set (Fin 3 → ℤ), S.Finite →
      /- The statement's $A = \lbrace a_1, a_2, \ldots \rbrace$ is an infinite set.

      If the sequence only takes finitely many values, one value has to repeat infinitely many
      times, which would yield a trivial collinear triple (x, x, x). In this case, the conjecture
      would hold for degenerate S-walks. Another case is constant S-walks, which would render the
      conjecture trivially false (finite loop ranges have no 3 distinct points).

      Assuming the authors intend to stay away from these degenerate cases, we formalize this by
      requiring an infinite range (and require distinct points). -/
      ∀ a : ℕ → Fin 3 → ℤ, IsSWalk S a → (range a).Infinite →
      HasCollinearTriple ℚ (range (fun n ↦ (↑) ∘ a n : ℕ → Fin 3 → ℚ)) := by
  sorry

/--
[GeRa79] showed that the answer is yes for $\mathbb{Z}^2$
-/
@[category research solved, AMS 5]
theorem erdos_193_z2 :
    ∀ S : Set (Fin 2 → ℤ), S.Finite →
      ∀ a : ℕ → Fin 2 → ℤ, IsSWalk S a → (range a).Infinite →
      HasCollinearTriple ℚ (range (fun n ↦ (↑) ∘ a n : ℕ → Fin 2 → ℚ)) := by
  sorry

-- TODO(jeangud): For $\mathbb{Z}^3$ the largest number of collinear points can be bounded [GeRa79].

end Erdos193


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
