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
# Erdős Problem 353

*References:*
- [erdosproblems.com/353](https://www.erdosproblems.com/353)
- [Er83d] Erdős, Paul, *Some combinatorial, geometric and set theoretic problems in measure
  theory*. Measure Theory, Oberwolfach 1983 (1984), 321-327.
- [Ko23] Kovač, V., *Coloring and density theorems for configurations of a given volume*.
  arXiv:2309.09973 (2023).
- [KoPr24] Kovač, V. and B. Predojević, *Polygons of unit area with vertices in sets of infinite
  planar measure*. arXiv:2412.11725 (2024).
- [Ko25] J. Koizumi, *Isosceles trapezoids of unit area with vertices in sets of infinite planar
  measure*. arXiv:2501.01914 (2025).
-/

open Affine EuclideanGeometry MeasureTheory

open scoped Real

namespace Erdos353

/--
Let $A\subseteq \mathbb{R}^2$ be a measurable set with infinite measure. Must $A$ contain the
vertices of an isosceles trapezoid of area $1$? What about an isosceles triangle, or a
right-angled triangle, or a cyclic quadrilateral, or a convex polygon with congruent sides?

Koizumi [Ko25] has resolved this question, proving that any set with infinite measure must
contain the vertices of an isosceles trapezoid, an isosceles triangle, and a right-angled
triangle, all of area $1$.

This statement formalizes the leading question, for isosceles trapezoids; the remaining
configurations are given as variants below. The area of a polygon is taken to be the Lebesgue
measure of the convex hull of its vertices.
-/
@[category research solved, AMS 28 51, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean"]
theorem erdos_353 : answer(True) ↔
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, ∃ d ∈ A,
        IsIsoscelesTrapezoid a b c d ∧
        volume (convexHull ℝ {a, b, c, d}) = 1 := by
  sorry

/--
Every measurable $A\subseteq \mathbb{R}^2$ with infinite measure contains the vertices of an
isosceles triangle of area $1$.

Koizumi [Ko25] has resolved this question, proving that any set with infinite measure must
contain the vertices of an isosceles trapezoid, an isosceles triangle, and a right-angled
triangle, all of area $1$.

Note the area condition forces `a`, `b`, `c` to be affinely independent, so no separate
non-degeneracy hypothesis is needed.
-/
@[category research solved, AMS 28 51, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean"]
theorem erdos_353.variants.isosceles_triangle :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A,
        IsIsosceles a b c ∧
        volume (convexHull ℝ {a, b, c}) = 1 := by
  sorry

/--
Every measurable $A\subseteq \mathbb{R}^2$ with infinite measure contains the vertices of a
right-angled triangle of area $1$.

Koizumi [Ko25] has resolved this question, proving that any set with infinite measure must
contain the vertices of an isosceles trapezoid, an isosceles triangle, and a right-angled
triangle, all of area $1$.

Note the area condition forces `a`, `b`, `c` to be affinely independent, so no separate
non-degeneracy hypothesis is needed.
-/
@[category research solved, AMS 28 51, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean"]
theorem erdos_353.variants.right_angled_triangle :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A,
        IsRightAngled a b c ∧
        volume (convexHull ℝ {a, b, c}) = 1 := by
  sorry

/--
Every measurable $A\subseteq \mathbb{R}^2$ with infinite measure contains the vertices of a
cyclic quadrilateral of area $1$.

Kovač and Predojević [KoPr24] have proved that this is true for cyclic quadrilaterals - that
is, every set with infinite measure contains four distinct points on a circle such that the
quadrilateral determined by these four points has area $1$. The quadrilateral determined by
four distinct concyclic points is their convex hull.
-/
@[category research solved, AMS 28 51, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean"]
theorem erdos_353.variants.cyclic_quadrilateral :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ Q : Set ℝ², Q ⊆ A ∧ Q.ncard = 4 ∧ Cospher

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
