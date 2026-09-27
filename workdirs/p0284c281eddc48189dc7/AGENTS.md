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
# Written on the Wall II - Conjecture 36

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/

namespace WrittenOnTheWallII.GraphConjecture36

open SimpleGraph

/-- `dp G` is the number of diametrical pairs of `G`: the number of unordered
pairs `{u, v}` of vertices at distance `diam(G)`.  -/
noncomputable def dp {α : Type*} [Fintype α] (G : SimpleGraph α) : ℕ :=
  open scoped Classical in
  (Finset.univ.filter
    (fun p : Sym2 α => p.lift ⟨fun u v => G.dist u v = G.diam ∧ u ≠ v,
      fun u v => by simp [SimpleGraph.dist_comm, ne_comm]⟩)).card

/--
WOWII [Conjecture 36](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj36):

For every finite simple connected graph $G$,
$\operatorname{path}(G) \ge 2 \cdot \operatorname{rad}(G) / \operatorname{dp}(G)$,
where $\operatorname{path}(G)$ is the floor of the average distance of $G$,
$\operatorname{rad}(G)$ is the radius of $G$, and $\operatorname{dp}(G)$ is the number
of *diametrical pairs* of $G$ — that is, the number of pairs of vertices at distance
$\operatorname{diam}(G)$.

Disproved by Waller in Oct 2003 (counterexample: path number 5, radius 3, dp 1).
-/
@[category research solved, AMS 5]
theorem conjecture36 : answer(False) ↔
    ∀ {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α],
      ∀ (G : SimpleGraph α) [DecidableRel G.Adj] (_ : G.Connected) (_ : 0 < dp G),
        (2 * G.radius.toNat : ℝ) / (dp G : ℝ) ≤ (path G : ℝ) := by
  sorry

-- Sanity checks

/-- The `path G` invariant is nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) : 0 ≤ (path G : ℝ) := Nat.cast_nonneg _

end WrittenOnTheWallII.GraphConjecture36


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
