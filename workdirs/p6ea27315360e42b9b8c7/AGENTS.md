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
# Erdős Problem 91

*Reference:*
- [Er87b] Erdős, P., Some combinatorial and metric problems in geometry.
  Intuitive geometry (Siófok, 1985) (1987), 167-177.
- [Ko24c] Z. Kovács, A note on Erdős's mysterious remark. arXiv:2412.05190 (2024).
- [erdosproblems.com/91](https://www.erdosproblems.com/91)
-/

open Finset EuclideanGeometry Filter

namespace Erdos91

/-- A set $A$ is 'optimal' if it has $n$ points and achieves the minimum distance count. -/
noncomputable def IsOptimal (A : Finset ℝ²) (n : ℕ) : Prop :=
  A.card = n ∧ distinctDistances A = minimalDistinctDistances n

/-- Two finite sets of points in $\mathbb{R}^2$ are similar if one can be mapped to the other by a
DilationEquiv. -/
def DilationEquivSimilar (A B : Finset ℝ²) : Prop :=
  ∃ f : ℝ² ≃ᵈ ℝ², (f '' A) = B

/-- Equilateral triangle with unit side length, resting on the x-axis with one vertex at the origin. -/
noncomputable def equiTriangle : Finset ℝ² := {!₂[0, 0], !₂[1, 0], !₂[1 / 2, Real.sqrt 3 / 2]}

noncomputable def unitSquare : Finset ℝ² := {!₂[0, 0], !₂[0, 1], !₂[1, 0], !₂[1, 1]}

/-- Regular 7-gon with unit side length, touching both axes in the first quadrant. -/
noncomputable def circleSeven : Finset ℝ² :=
  let r := 1 / (2 * Real.sin (Real.pi / 7))
  let cx := r * Real.cos (Real.pi / 7)
  let cy := r * Real.sin (4 * Real.pi / 7)
  (Finset.range 7).image fun k : ℕ =>
    !₂[r * Real.cos (2 * Real.pi * ↑k / 7) + cx, r * Real.sin (2 * Real.pi * ↑k / 7) + cy]

/-- Wheel graph on 7 vertices (center + regular hexagon) with unit side length,
touching both axes in the first quadrant. -/
noncomputable def wheelSeven : Finset ℝ² :=
  {!₂[1, Real.sqrt 3 / 2],
   !₂[2, Real.sqrt 3 / 2],
   !₂[3 / 2, Real.sqrt 3],
   !₂[1 / 2, Real.sqrt 3],
   !₂[0, Real.sqrt 3 / 2],
   !₂[1 / 2, 0],
   !₂[3 / 2, 0]}

@[category test, AMS 52]
lemma erdos_91.test.equiTriangle_optimal : IsOptimal equiTriangle 3 := by
  have hcard : equiTriangle.card = 3 := by
    simp [equiTriangle, Finset.mem_insert, Finset.mem_singleton]
  have hdist : distinctDistances equiTriangle = 1 := by
    unfold distinctDistances distanceSet equiTriangle
    have eucl_dist_one_of_sq : ∀ {x y : ℝ²}, dist x y ^ 2 = 1 → dist x y = 1 := by
      intro x y h; nlinarith [dist_nonneg (x := x) (y := y), sq_nonneg (dist x y)]
    have hd01 : dist (!₂[(0 : ℝ), 0]) (!₂[(1 : ℝ), 0]) = 1 := eucl_dist_one_of_sq <| by
      rw [EuclideanSpace.dist_sq_eq, Fin.sum_univ_two]; simp [Real.dist_eq]
    have hd02 : dist (!₂[(0 : ℝ), 0]) (!₂[(1 : ℝ) / 2, Real.sqrt 3 / 2]) = 1 :=
      eucl_dist_one_of_sq <| by
        rw [EuclideanSpace.dist_sq_eq, Fin.sum_univ_two, Real.dist_eq, Real.dist_eq]
        simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
        nlinarith [Real.sq_sqrt (show (3 : ℝ) ≥ 0 by norm_num), Real.sqrt_nonneg 3,
          sq_abs ((0 : ℝ) - 1 / 2), sq_abs ((0 : ℝ) - Real.sqrt 3 / 2)]
    have hd12 : dist (!₂[(1 : ℝ), 0]) (!₂[(1 : ℝ) / 2, Real.sqrt 3 / 2]) = 1 :=
      eucl_dist_one_of_sq <| by
        rw [EuclideanSpace.dist_sq_eq, Fin.sum_univ_two, Real.dist_eq, Real.dist_eq]
        simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
        nlinarith [Real.sq_sqrt (show (3 : ℝ) ≥ 0 by norm_num), Real.sqrt_nonneg 3,
          sq_abs ((1 : ℝ) - 1 / 2), sq_abs ((0 : ℝ) - Real.sqrt 3 / 2)]
    suffices h : ({!₂[(0 : ℝ), 0], !₂[(1 : ℝ), 0], !₂[(1 : ℝ) / 2, Real.sqrt 3 / 2]} :
        Finset ℝ²).offDiag.image (fun (pair : ℝ² × ℝ²) => dist pair.1 pair.2) = {1} by
      simp only [h, Finset.card_singleton]
    refine Finset.eq_singleton_iff_unique_mem.mpr ⟨Finset.mem_image.mpr
      ⟨⟨!₂[0, 0], !₂[1, 0]⟩, by simp [Finset.mem_offDiag], hd01⟩, fun d hd => ?_⟩
    obtain ⟨⟨a, b⟩, hab, rfl⟩ := Finset.mem_image.mp hd
    simp only [Finset.mem_offDiag, Finset.mem_insert, Finset.mem_singleton] at hab
    obtain ⟨ha, hb, _⟩ := hab
    rcases ha with rfl | rfl | rfl <;> rcases hb with rfl | rfl | rfl <;> first
      | contradiction | exact hd01 | exact hd02 | exact hd12
      | (rw [dist_comm]; first | exact hd01 | exact hd02 | exact hd12)
  have hmin : minimalDistinctDistances 3 = 1 := by
    unfold minimalDistinctDistances
    apply le_antisymm
    · exact Nat.sInf_le ⟨equiTriangle, hcard, by exact_mod_cast hdist⟩
    · apply le_csInf
      · exact ⟨_, equiTriangle, hcard, rfl⟩
      rintro d ⟨points, hcard', hd⟩
      rw [← show distinctDistances points = d from by exact_mod_cast hd]
      ex

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
