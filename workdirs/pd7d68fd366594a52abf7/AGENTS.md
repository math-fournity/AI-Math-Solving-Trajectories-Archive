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
# Erdős Problem 755

*References:*
- [erdosproblems.com/755](https://www.erdosproblems.com/755)
- [ErPu75] Erdős, Paul and Purdy, George, Some extremal problems in geometry. III.
  (1975), 291--308.
- [Er94b] Erdős, Paul, Some problems in number theory, combinatorics and
  combinatorial geometry. Math. Pannon. (1994), 261--269.
- [CDL25b] Clemen, Felix Christian, Dumitrescu, Adrian, and Liu, Dingyuan,
  The number of regular simplices in higher dimensions. arXiv:2507.19841 (2025).
-/

open Filter Metric
open scoped EuclideanGeometry Asymptotics

namespace Erdos755

/-- A three-point set whose pairwise distances are all equal to `side`. -/
def IsEquilateralTriangle {d : ℕ} (side : ℝ)
    (T : Finset (EuclideanSpace ℝ (Fin d))) : Prop :=
  T.card = 3 ∧ ∀ p ∈ T, ∀ q ∈ T, p ≠ q → dist p q = side

/-- A unit equilateral triangle in Euclidean `d`-space. -/
def IsUnitEquilateralTriangle {d : ℕ}
    (T : Finset (EuclideanSpace ℝ (Fin d))) : Prop :=
  IsEquilateralTriangle 1 T

/-- An equilateral triangle of any positive side length in Euclidean `d`-space. -/
def IsAnySizeEquilateralTriangle {d : ℕ}
    (T : Finset (EuclideanSpace ℝ (Fin d))) : Prop :=
  ∃ side : ℝ, 0 < side ∧ IsEquilateralTriangle side T

/-- Number of unit equilateral triangles spanned by a finite point set. -/
noncomputable def unitEquilateralTriangleCount (d : ℕ)
    (P : Finset (EuclideanSpace ℝ (Fin d))) : ℕ :=
  open scoped Classical in
  ((P.powersetCard 3).filter fun T => IsUnitEquilateralTriangle T).card

/-- Number of equilateral triangles of any positive side length spanned by a finite point set. -/
noncomputable def anySizeEquilateralTriangleCount (d : ℕ)
    (P : Finset (EuclideanSpace ℝ (Fin d))) : ℕ :=
  open scoped Classical in
  ((P.powersetCard 3).filter fun T => IsAnySizeEquilateralTriangle T).card

/-- Maximum number of unit equilateral triangles spanned by $n$ points in $\mathbb{R}^d$. -/
noncomputable def TUnit (d n : ℕ) : ℕ :=
  sSup {m : ℕ | ∃ P : Finset (EuclideanSpace ℝ (Fin d)),
    P.card = n ∧ unitEquilateralTriangleCount d P = m}

/-- Maximum number of equilateral triangles of any size spanned by $n$ points in $\mathbb{R}^d$. -/
noncomputable def TAnySize (d n : ℕ) : ℕ :=
  sSup {m : ℕ | ∃ P : Finset (EuclideanSpace ℝ (Fin d)),
    P.card = n ∧ anySizeEquilateralTriangleCount d P = m}

@[category test, AMS 52]
theorem erdos_755.test_dim_one :
    unitEquilateralTriangleCount 1 (∅ : Finset (EuclideanSpace ℝ (Fin 1))) = 0 := by
  simp [unitEquilateralTriangleCount]

/--
Erdős asked whether every $n$-point set in
$\mathbb{R}^6$ spans at most $(1/27 + o(1)) n^3$ unit equilateral triangles.

Clemen, Dumitrescu, and Liu [CDL25b] proved the stronger any-size statement
$T_6(n) = (1/27 + o(1)) n^3$. The unit-triangle upper bound follows as a
corollary, since unit equilateral triangles are a subset of equilateral
triangles of any positive side length: $T_\mathrm{unit} \leq T_\mathrm{anysize}$.
-/
@[category research solved, AMS 52]
theorem erdos_755 :
    answer(True) ↔ ∃ o : ℕ → ℝ,
      o =o[atTop] (fun _ : ℕ => (1 : ℝ)) ∧
        ∀ᶠ n in atTop,
          (TUnit 6 n : ℝ) ≤ ((1 / 27 : ℝ) + o n) * (n : ℝ) ^ 3 := by
  sorry

/--
Clemen, Dumitrescu, and Liu [CDL25b] proved the stronger version where
equilateral triangles of all positive side lengths are counted.
-/
@[category research solved, AMS 52]
theorem erdos_755.variants.any_size_cdl :
    (fun n : ℕ => (TAnySize 6 n : ℝ)) ~[atTop]
      (fun n : ℕ => (1 / 27 : ℝ) * (n : ℝ) ^ 3) := by
  sorry

end Erdos755


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
