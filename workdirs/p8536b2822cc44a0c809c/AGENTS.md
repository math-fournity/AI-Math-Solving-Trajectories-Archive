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
# Erdős Problem 660

*References:*
- [erdosproblems.com/660](https://www.erdosproblems.com/660)
- [Er97e] Erdős, Paul, *Some of my favorite problems and results*, The mathematics of Paul Erdős,
  I (1997), 47–67.
- [Al63] Altman, E., *On a problem of P. Erdős*, Amer. Math. Monthly (1963), 148–157.
- [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*, Ann. Mat. Pura
  Appl. (4) (1975), 99–108.
-/

open scoped EuclideanGeometry

namespace Erdos660

/--
`P` is the set of vertices of a (full-dimensional) convex polyhedron in $\mathbb{R}^3$: the points
are in convex position and they affinely span $\mathbb{R}^3$ (so the polyhedron is genuinely
three-dimensional).
-/
def IsPolyhedronVertices (P : Finset ℝ³) : Prop :=
  ConvexIndependent ℝ ((↑) : ↥(P : Set ℝ³) → ℝ³) ∧ affineSpan ℝ (P : Set ℝ³) = ⊤

/--
Let $x_1, \ldots, x_n \in \mathbb{R}^3$ be the vertices of a convex polyhedron. Are there at least
$$(1 - o(1)) \frac{n}{2}$$
many distinct distances between the $x_i$?

The $(1 - o(1)) \frac{n}{2}$ lower bound is formalised as: for every $\varepsilon > 0$, every set
of $n$ vertices of a convex polyhedron with $n$ sufficiently large determines at least
$(1 - \varepsilon) \frac{n}{2}$ distinct distances.
-/
@[category research open, AMS 51 52]
theorem erdos_660 :
    answer(sorry) ↔
      ∀ ε : ℝ, 0 < ε → ∀ᶠ n in Filter.atTop, ∀ P : Finset ℝ³,
        P.card = n → IsPolyhedronVertices P →
        (1 - ε) * ((n : ℝ) / 2) ≤ (distinctDistances P : ℝ) := by
  sorry

/--
For the similar problem in $\mathbb{R}^2$ there are always at least $n/2$ distances, as proved by
Altman [Al63].
-/
@[category research solved, AMS 51 52]
theorem erdos_660.variants.altman_planar (n : ℕ) (P : Finset ℝ²)
    (hcard : P.card = n) (hconv : ConvexIndependent ℝ ((↑) : ↥(P : Set ℝ²) → ℝ²))
    (haff : affineSpan ℝ (P : Set ℝ²) = ⊤) :
    n / 2 ≤ distinctDistances P := by
  sorry

/--
In [Er75f] Erdős claims that Altman proved that the vertices determine $\gg n$ many distinct
distances, but gives no reference.
-/
@[category research open, AMS 51 52]
theorem erdos_660.variants.Er75f :
    answer(sorry) ↔ ∃ c > (0 : ℝ), ∀ᶠ n in Filter.atTop, ∀ P : Finset ℝ³,
      P.card = n → IsPolyhedronVertices P →
      c * n ≤ (distinctDistances P : ℝ) := by
  sorry

end Erdos660


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
