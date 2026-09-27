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
# Written on the Wall II - Conjecture 65

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

## Counterexample

The conjecture is false. Start with the path $v_0-v_1-\cdots-v_{12}$ and attach one
triangle at $v_1$ and another at $v_{11}$. The resulting graph has $17$ vertices.
Its Graph_6 string is `PhCGGC@?G?_@?@O?G?G?G?@C`.
Its only minimum-degree vertices are $v_0$ and $v_{12}$, at distance $12$, while its
only maximum-degree vertices are $v_1$ and $v_{11}$, at distance $10$. Thus the
conjectured lower bound is $12 + \lceil 10/3 \rceil = 16$.

Every induced forest must omit at least one vertex from each of the two vertex-disjoint
triangles, so it has at most $15$ vertices. Conversely, deleting one non-path vertex
from each triangle leaves a tree on $15$ vertices.
-/

namespace WrittenOnTheWallII.GraphConjecture65

open SimpleGraph Finset

namespace Counterexample

/-- The counterexample: a path on vertices $0,\ldots,12$, with triangles attached at
vertices $1$ and $11$. -/
abbrev graph : SimpleGraph (Fin 17) :=
  SimpleGraph.fromEdgeSet {
    s(0, 1), s(1, 2), s(2, 3), s(3, 4), s(4, 5), s(5, 6),
    s(6, 7), s(7, 8), s(8, 9), s(9, 10), s(10, 11), s(11, 12),
    s(1, 13), s(1, 14), s(13, 14),
    s(11, 15), s(11, 16), s(15, 16)
  }

/-- The counterexample is connected. -/
@[category API, AMS 5]
lemma connected : graph.Connected := by
  rw [connected_iff_exists_forall_reachable]
  refine ⟨0, ?_⟩
  have step (u v : Fin 17) (h : graph.Reachable 0 u) (huv : graph.Adj u v) :
      graph.Reachable 0 v := h.trans huv.reachable
  have h0 : graph.Reachable 0 0 := by simp
  have h1 := step 0 1 h0 (by decide)
  have h2 := step 1 2 h1 (by decide)
  have h3 := step 2 3 h2 (by decide)
  have h4 := step 3 4 h3 (by decide)
  have h5 := step 4 5 h4 (by decide)
  have h6 := step 5 6 h5 (by decide)
  have h7 := step 6 7 h6 (by decide)
  have h8 := step 7 8 h7 (by decide)
  have h9 := step 8 9 h8 (by decide)
  have h10 := step 9 10 h9 (by decide)
  have h11 := step 10 11 h10 (by decide)
  have h12 := step 11 12 h11 (by decide)
  have h13 := step 1 13 h1 (by decide)
  have h14 := step 1 14 h1 (by decide)
  have h15 := step 11 15 h11 (by decide)
  have h16 := step 11 16 h11 (by decide)
  intro v
  fin_cases v <;> assumption

/-- The minimum-degree vertices of the counterexample are the two path endpoints. -/
@[category API, AMS 5]
lemma min_degree_vertices :
    {v | graph.degree v = graph.minDegree} = ({0, 12} : Set (Fin 17)) := by
  ext v
  fin_cases v <;> decide

/-- The maximum-degree vertices of the counterexample are the two triangle attachment points. -/
@[category API, AMS 5]
lemma max_degree_vertices :
    {v | graph.degree v = graph.maxDegree} = ({1, 11} : Set (Fin 17)) := by
  ext v
  fin_cases v <;> decide

/-- The minimum distance between minimum-degree vertices is $12$. -/
@[category API, AMS 5]
lemma distMin_min_degree_vertices : distMin graph ({0, 12} : Set (Fin 17)) = 12 := by
  rw [show ({0, 12} : Set (Fin 17)) = ↑({0, 12} : Finset (Fin 17)) by simp,
    distMin_eq_computableDistMin]
  decide

/-- The minimum distance between maximum-degree vertices is $10$. -/
@[category API, AMS 5]
lemma distMin_max_degree_vertices : distMin graph ({1, 11} : Set (Fin 17)) = 10 := by
  rw [show ({1, 11} : Set (Fin 17)) = ↑({1, 11} : Finset (Fin 17)) by simp,
    distMin_eq_computableDistMin]
  decide

/-- An acyclic induced subgraph cannot contain all three vertices of a triangle. -/
@[category API, AMS 5]
lemma triangle_not_subset_of_isAcyclic (S : Finset (Fin 17))
    (hS : (graph.induce S).IsAcyclic) {a b c : Fin 17}
    (hab : graph.Adj a b) (hbc : graph.Adj b c) (hca : graph.Adj c a) :
    ¬({a, b, c} : Finset (Fin 17)) ⊆ S := by
  intro hsub
  have ha : a ∈ S := hsub (by simp)
  have hb : b ∈ S := hsub (by simp)
  have hc : c ∈ S := hsub (by simp)
  let va : S := ⟨a, ha⟩
  let vb : S := ⟨b, hb⟩
  let vc : S := ⟨c, hc⟩
  have hab' : (graph.induce S).Adj va vb := hab
  have hbc' : (graph.induce S).Adj vb vc := hbc
  have hca' : (graph.induce S).Adj vc va := hca
  let cycle : (graph.induce S).Walk va va :=
    .cons hab' (.cons hbc' (.cons hca' .nil))
  exact hS cycle (by
    rw [Walk.isCycle_def]
    refine ⟨?_, by simp [cycle], ?_⟩
    · rw [Walk.isTrail_def]
      simp [cycle, va, vb, vc, hab.ne, hab.ne.symm, hbc.ne,
        hca.ne, 

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
