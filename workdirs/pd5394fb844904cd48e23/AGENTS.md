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
# The Alon-Tarsi short cycle cover conjecture

*References:*
- [AlTa85] Alon, N. and Tarsi, M., Covering multigraphs by simple circuits.
  SIAM J. Algebraic Discrete Methods (1985), 345--350.
- [arxiv/2607.06396](https://arxiv.org/abs/2607.06396)
  **Some new results on Sylvester colorings of cubic graphs**
  by *Luca Ferrarini, Vahan Mkrtchyan*, where this is Conjecture 4.

Every bridgeless graph has a list of cycles covering every edge whose lengths sum to at most
$\frac{7}{5}|E|$.
-/

open Finset SimpleGraph

namespace Arxiv.«2607.06396»

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- `C` covers `G`: every edge of `G` lies on at least one cycle of `C`. -/
def IsCycleCover (G : SimpleGraph V) [DecidableRel G.Adj] (C : Multiset (Cycle G)) : Prop :=
  ∀ e ∈ G.edgeFinset, ∃ c ∈ C, e ∈ c.edges

/-- The total length of a family of cycles. -/
def totalLength {G : SimpleGraph V} (C : Multiset (Cycle G)) : ℕ := (C.map SimpleGraph.Cycle.length).sum

/--
**Conjecture 4 (Alon-Tarsi, 1985).** Every bridgeless graph has a list of cycles covering
every edge, with $\sum_{C} |E(C)| \leq \frac{7}{5}|E(G)|$.
-/
@[category research open, AMS 5]
theorem alon_tarsi_short_cycle_cover :
    answer(sorry) ↔ ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj], G.IsBridgeless →
      ∃ C : Multiset (Cycle G), IsCycleCover G C ∧
        (totalLength C : ℚ) ≤ 7 / 5 * #G.edgeFinset := by
  sorry

omit [DecidableEq V] in
/-- The empty cover works when there are no edges, so the bound is attained with room to spare
on edgeless graphs. -/
@[category test, AMS 5]
theorem exists_cover_of_edgeFinset_eq_empty (G : SimpleGraph V) [DecidableRel G.Adj]
    (h : G.edgeFinset = ∅) :
    ∃ C : Multiset (Cycle G), IsCycleCover G C ∧
      (totalLength C : ℚ) ≤ 7 / 5 * #G.edgeFinset := by
  refine ⟨0, ?_, ?_⟩
  · intro e he
    rw [h] at he
    exact absurd he (Finset.notMem_empty e)
  · simp [totalLength, h]

omit [DecidableEq V] in
/-- Acyclic bridgeless graphs satisfy the conjecture, with the empty cover. In a forest every
edge is a bridge, so such a graph has no edges at all. -/
@[category test, AMS 5]
theorem exists_cover_of_isAcyclic (G : SimpleGraph V) [DecidableRel G.Adj]
    (hacyc : G.IsAcyclic) (hbr : G.IsBridgeless) :
    ∃ C : Multiset (Cycle G), IsCycleCover G C ∧
      (totalLength C : ℚ) ≤ 7 / 5 * #G.edgeFinset :=
  exists_cover_of_edgeFinset_eq_empty G
    (G.edgeFinset_eq_empty_of_isBridgeless_of_isAcyclic hacyc hbr)

omit [Fintype V] [DecidableEq V] in
/-- A cycle has at least three edges, so any cover of a graph with an edge has total length at
least three. This is what makes the `7/5` bound a real constraint rather than a formality. -/
@[category API, AMS 5]
theorem three_le_length {G : SimpleGraph V} (c : Cycle G) : 3 ≤ c.length :=
  c.isCycle.three_le_length

end Arxiv.«2607.06396»


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
