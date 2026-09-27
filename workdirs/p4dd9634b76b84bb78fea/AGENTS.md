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
# Testing Graph Invariants

This file contains tests for graph invariants on 5 specific concrete graphs:
1. `HouseGraph`: A graph on 5 vertices.
2. `K4`: The complete graph on 4 vertices.
3. `PetersenGraph`: The Petersen graph on 10 vertices.
4. `C6`: The cycle graph on 6 vertices.
5. `Star5`: The star graph with 5 leaves (6 vertices total).

Tests cover:
independence_number, dominationNumber, average_distance, diameter, radius,
girth, order, size, szeged_index, wiener_index, min_degree, max_degree,
average_degree, matching_number, residue, annihilation_number, cvetkovic.
-/

open SimpleGraph

namespace WrittenOnTheWallII.Test


-- Bridge theorems for Sym2/edist-based invariants:
-- All 6 (indep_num, dom_num, dist, wiener, avg_dist, szeged) are proved in
-- FormalConjecturesForMathlib/.../Invariants.lean and exported via that module.

/-  ### Graph Definitions -/

/-- House Graph: Square 0-1-2-3-0 with roof 4 connected to 2,3. -/
abbrev HouseGraph : SimpleGraph (Fin 5) :=
  SimpleGraph.fromEdgeSet {
    s(0, 1), s(1, 2), s(2, 3), s(3, 0),
    s(2, 4), s(3, 4)
  }

/-- K4: Complete graph on 4 vertices. -/
abbrev K4 : SimpleGraph (Fin 4) := completeGraph (Fin 4)

/-- Petersen Graph on 10 vertices. -/
abbrev PetersenGraph : SimpleGraph (Fin 10) :=
  SimpleGraph.fromEdgeSet {
    -- Outer Cycle
    s(0, 1), s(1, 2), s(2, 3), s(3, 4), s(4, 0),
    -- Spokes
    s(0, 5), s(1, 6), s(2, 7), s(3, 8), s(4, 9),
    -- Inner Star
    s(5, 7), s(7, 9), s(9, 6), s(6, 8), s(8, 5)
  }

/-- C6: Cycle graph on 6 vertices. -/
abbrev C6 : SimpleGraph (Fin 6) := cycleGraph 6

/-- Star5: Star graph with center 0 and 5 leaves. -/
abbrev Star5 : SimpleGraph (Fin 1 ⊕ Fin 5) := completeBipartiteGraph (Fin 1) (Fin 5)

instance : DecidableRel Star5.Adj := by unfold Star5 completeBipartiteGraph; infer_instance


/-  ### House Graph Tests -/

@[category test, AMS 5]
theorem house_indep : α(HouseGraph) = 2 := by
  rw [indep_num_eq_computable]; decide +native

@[category test, AMS 5]
theorem house_dom : dominationNumber HouseGraph = 2 := by
  rw [dom_num_eq_computable]; decide +native

@[category test, AMS 5]
theorem house_avg_dist : averageDistance HouseGraph = 7/5 := by
  rw [avg_dist_eq_computable, show computable_avg_dist HouseGraph = (7 / 5 : ℚ) from by decide +native]
  norm_num

@[category test, AMS 5]
theorem house_diameter : ediam HouseGraph = 2 := by
  rw [ediam_eq_computable HouseGraph (by decide)]
  exact_mod_cast (by decide +native : computable_ediam HouseGraph = 2)

@[category test, AMS 5]
theorem house_radius : radius HouseGraph = 2 := by
  rw [radius_eq_computable HouseGraph (by decide)]
  exact_mod_cast (by decide +native : computable_radius HouseGraph = 2)

@[category test, AMS 5]
theorem house_girth : HouseGraph.girth = 3 := by
  have hcyc : (Walk.cons (show HouseGraph.Adj 2 3 by decide)
      (Walk.cons (show HouseGraph.Adj 3 4 by decide)
      (Walk.cons (show HouseGraph.Adj 4 2 by decide) Walk.nil))).IsCycle := by
    rw [Walk.isCycle_def]
    refine ⟨?_, ?_, ?_⟩
    · rw [Walk.isTrail_def]; decide
    · simp
    · decide
  refine le_antisymm ?_ (three_le_girth (fun hac => hac _ hcyc))
  simpa using girth_le_length hcyc

@[category test, AMS 5]
theorem house_order : Fintype.card ↥(⊤ : Subgraph HouseGraph).verts = 5 := by
  rw [Fintype.card_congr SimpleGraph.Subgraph.topIso.toEquiv]
  rfl

@[category test, AMS 5]
theorem house_size : HouseGraph.edgeFinset.card = 6 := by
  decide +native

@[category test, AMS 5]
theorem house_szeged : szegedIndex HouseGraph = 24 := by
  rw [szeged_eq_computable]; decide +native

@[category test, AMS 5]
theorem house_wiener : wienerIndex HouseGraph = 14 := by
  rw [wiener_eq_computable]; decide +native

@[category test, AMS 5]
theorem house_min_deg : HouseGraph.minDegree = 2 := by
  decide +native

@[category test, AMS 5]
theorem house_max_deg : HouseGraph.maxDegree = 3 := by
  decide +native

@[category test, AMS 5]
theorem house_avg_deg : averageDegree HouseGraph = 12/5 := by
  unfold averageDegree; simp [Fintype.card_fin]; decide +native

@[category test, AMS 5]
theorem house_matching : matchingNumber HouseGraph = 2 := by
  classical
  have hbdd : BddAbove (Set.image (fun M : Subgraph HouseGraph => (M.edgeSet.toFinset.card : ℝ)) {M | M.IsMatching}) := by
    refine ⟨(Fintype.card (Fin 5) : ℝ), ?_⟩
    rintro x ⟨M, hM, rfl⟩
    show (M.edgeSet.toFinset.card : ℝ) ≤ Fintype.card (Fin 

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
