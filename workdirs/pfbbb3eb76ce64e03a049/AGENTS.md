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
# Erdős Problem 633

*Reference:*
* [erdosproblems.com/633](https://www.erdosproblems.com/633)
* [So09] Soifer, Alexander, How Does One Cut a Triangle? I
* [So09c] Soifer, Alexander, Is there anything beyond the solution?
-/

open Affine
open scoped Congruent EuclideanGeometry Similar

namespace Erdos633
variable {n : ℕ} {T : Triangle ℝ ℝ²}

variable (n T) in
/-- A triangle is `n`-cuttable if it can be decomposed into `n` congruent triangles. -/
def IsCuttable : Prop :=
  ∃ Ts : Fin n → Triangle ℝ ℝ²,
    (∀ i j, (Ts i).points ≅ (Ts j).points) ∧
      Pairwise (fun i j ↦ Disjoint (Ts i).interior (Ts j).interior) ∧
      ⋃ i, (Ts i).closedInterior = T.closedInterior

/-- A triangle isn't cuttable into zero triangles. -/
@[category API, AMS 5 51]
lemma IsCuttable.ne_zero (hT : IsCuttable n T) : n ≠ 0 := by
  rintro rfl
  obtain ⟨Ts, -, -, hT⟩ := hT
  exact T.closedInterior_nonempty.ne_empty <| by simpa using hT.symm

/-- Every triangle is cuttable into any non-zero square number of congruent triangles. -/
@[category API, AMS 5 51]
protected lemma IsCuttable.sq (hn : n ≠ 0) : IsCuttable (n ^ 2) T := sorry

/-- Every triangle is cuttable into any non-zero square number of congruent triangles. -/
@[category API, AMS 5 51]
lemma IsCuttable.of_isSquare (hn₀ : n ≠ 0) (hn : IsSquare n) : IsCuttable n T := by
  obtain ⟨n, rfl⟩ := hn; rw [← sq]; exact .sq <| by simpa using hn₀

/-- A triangle whose side lengths and angles are integrally independent is cuttable only into
a non-zero square number of congruent triangles. This is proved in [So09c]. -/
@[category research solved, AMS 5 51]
lemma isCuttable_iff_isSquare_of_linearIndependent
    (hTsides : LinearIndependent ℤ
      ![dist (T.points 0) (T.points 1),
        dist (T.points 1) (T.points 2),
        dist (T.points 2) (T.points 0)])
    (hTangles : LinearIndependent ℤ
      ![∠ (T.points 0) (T.points 1) (T.points 2),
        ∠ (T.points 1) (T.points 2) (T.points 0),
        ∠ (T.points 2) (T.points 0) (T.points 1)]) :
    IsCuttable n T ↔ n ≠ 0 ∧ IsSquare n := by
  exact ⟨fun hT ↦ ⟨hT.ne_zero, sorry⟩, fun hn ↦ .of_isSquare hn.1 hn.2⟩

/-- Which triangles can only be decomposed into a square number of congruent triangles? -/
@[category research open, AMS 5 51]
lemma erdos_633 : T ∈ (answer(sorry) : Set <| Triangle ℝ ℝ²) ↔
    ∀ n, IsCuttable n T → IsSquare n := sorry

variable (n T) in
/-- A triangle is `n`-simili-cuttable if it can be decomposed into `n` similar triangles. -/
def IsSimiliCuttable (n : ℕ) (T : Triangle ℝ ℝ²) : Prop :=
  ∃ Ts : Fin n → Triangle ℝ ℝ²,
    (∀ i j, (Ts i).points ∼ (Ts j).points) ∧
      Pairwise (fun i j ↦ Disjoint (Ts i).interior (Ts j).interior) ∧
      ⋃ i, (Ts i).closedInterior = T.closedInterior

/-- A triangle isn't simili-cuttable into zero triangles. -/
@[category API, AMS 5 51]
lemma IsSimiliCuttable.ne_zero (hT : IsSimiliCuttable n T) : n ≠ 0 := by
  rintro rfl
  obtain ⟨Ts, -, -, hT⟩ := hT
  exact T.closedInterior_nonempty.ne_empty <| by simpa using hT.symm

/-- Every triangle is simili-cuttable into any number of similar triangles, except 0, 2, 3, 5.
This is proved in [So09]. -/
@[category research solved, AMS 5 51]
lemma IsSimiliCuttable.of_ne_zero_two_three_five (hn₀ : n ≠ 0) (hn₂ : n ≠ 2) (hn₃ : n ≠ 3)
    (hn₅ : n ≠ 5) : IsSimiliCuttable n T := sorry

/-- There exists a triangle which isn't simili-cuttable into 0, 2, 3, 5 parts.
This is proved in [So09]. -/
@[category research solved, AMS 5 51]
lemma exists_isSimiliCuttable_iff_ne_zero_two_three_five :
    ∃ T, ∀ n, IsSimiliCuttable n T ↔ n ≠ 0 ∧ n ≠ 2 ∧ n ≠ 3 ∧ n ≠ 5 := sorry

end Erdos633


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
