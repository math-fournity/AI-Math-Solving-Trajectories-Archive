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
# Erdős Problem 1098

*References:*
- [erdosproblems.com/1098](https://www.erdosproblems.com/1098)
- [Ne76] Neumann, B. H., *A problem of Paul Erdős on groups*. J. Austral. Math. Soc. Ser. A (1976),
  467-472.
-/

namespace Erdos1098

/-- The non-commuting graph $\Gamma = \Gamma(G)$ of a group `G`, with vertices the elements of `G`
and an edge between `g` and `h` if and only if `g` and `h` do not commute, $gh \neq hg$. -/
def nonCommutingGraph (G : Type*) [Group G] : SimpleGraph G where
  Adj g h := g * h ≠ h * g
  symm := fun _ _ h => h.symm
  loopless := fun _ h => h rfl

@[simp, category API, AMS 5 20]
theorem nonCommutingGraph_adj {G : Type*} [Group G] (g h : G) :
    (nonCommutingGraph G).Adj g h ↔ g * h ≠ h * g := Iff.rfl

/--
Let $G$ be a group and $\Gamma=\Gamma(G)$ be the non-commuting graph, with vertices the elements
of $G$ and an edge between $g$ and $h$ if and only if $g$ and $h$ do not commute, $gh\neq hg$.

If $\Gamma$ contains no infinite complete subgraph, then is there a finite bound on the size of
complete subgraphs of $\Gamma$?

This was solved by Neumann [Ne76], who proved that $\Gamma$ contains no infinite complete subgraph
if and only if the centre of the group has finite index, and noted that if the centre has index $n$
then $\Gamma$ contains no complete subgraph on $>n$ vertices.
-/
@[category research solved, AMS 5 20, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1098.lean"]
theorem erdos_1098 : answer(True) ↔
    ∀ (G : Type*) [Group G],
      (∀ s : Set G, (nonCommutingGraph G).IsClique s → s.Finite) →
        ∃ n : ℕ, ∀ s : Finset G, (nonCommutingGraph G).IsClique (s : Set G) → s.card ≤ n := by
  sorry

/--
Neumann [Ne76] proved that $\Gamma$ contains no infinite complete subgraph if and only if the
centre of the group has finite index.
-/
@[category research solved, AMS 5 20]
theorem erdos_1098.variants.center_finiteIndex (G : Type*) [Group G] :
    (∀ s : Set G, (nonCommutingGraph G).IsClique s → s.Finite) ↔
      (Subgroup.center G).FiniteIndex := by
  sorry

/--
Neumann [Ne76] noted that if the centre has index $n$ then $\Gamma$ contains no complete subgraph
on $>n$ vertices.
-/
@[category research solved, AMS 5 20]
theorem erdos_1098.variants.upper_bound (G : Type*) [Group G]
    [(Subgroup.center G).FiniteIndex] :
    (nonCommutingGraph G).CliqueFree ((Subgroup.center G).index + 1) := by
  sorry

end Erdos1098


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
