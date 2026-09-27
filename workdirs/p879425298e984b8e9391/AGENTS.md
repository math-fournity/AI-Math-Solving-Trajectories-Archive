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
# Written on the Wall II - Conjecture 3

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/


universe u

namespace WrittenOnTheWallII.GraphConjecture3

open SimpleGraph

variable {α : Type u} [Fintype α] [DecidableEq α]

/--
WOWII [Conjecture 3](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

For a connected simple graph `G`, the number of leaves in a maximum spanning
tree satisfies `Ls(G) ≥ G.indepDominationNumber * MaxTemp(G)`, where `G.indepDominationNumber` is the independent
domination number and `MaxTemp(G)` is `max_v deg(v)/(n(G) - deg(v))`.
-/
@[category research solved, AMS 5]
theorem conjecture3 {G : SimpleGraph α} [DecidableEq α] [DecidableRel G.Adj] [Nontrivial α]
    (h_conn : G.Connected) :
    G.indepDominationNumber * MaxTemp G ≤ Ls G := by
  sorry

-- Sanity checks

/-- The number of vertices of the two-vertex graph `K₂` is 2. -/
@[category test, AMS 5]
example : Fintype.card (Fin 2) = 2 := rfl

/-- In `K₂`, the temperature of vertex 0 is `deg(0) / (n - deg(0)) = 1 / 1 = 1`. -/
@[category test, AMS 5]
example : temp_v (⊤ : SimpleGraph (Fin 2)) ⟨0, by omega⟩ = 1 := by
  unfold temp_v
  have hdeg : (⊤ : SimpleGraph (Fin 2)).degree ⟨0, by omega⟩ = 1 := rfl
  rw [show Fintype.card (Fin 2) = 2 from rfl, hdeg]
  norm_num

end WrittenOnTheWallII.GraphConjecture3


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
