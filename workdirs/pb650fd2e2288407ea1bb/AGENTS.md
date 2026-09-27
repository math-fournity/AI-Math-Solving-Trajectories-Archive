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
# Erdős Problem 94

*References:*
- [erdosproblems.com/94](https://www.erdosproblems.com/94)
- [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*. Eureka
  (1992), 44-48.
- [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős, I
  (1997), 47-67.
- [LeTh95] Lefmann, Hanno and Thiele, Torsten, *Point sets with distinct distances*. Combinatorica
  (1995), 379-408.
-/

open Filter EuclideanGeometry

namespace Erdos94

/-- The regular $n$-gon inscribed in the unit circle. -/
noncomputable def regularNGon (n : ℕ) : Finset ℝ² :=
  (Finset.range n).image fun k : ℕ =>
    !₂[Real.cos (2 * Real.pi * k / n), Real.sin (2 * Real.pi * k / n)]

/--
Suppose $n$ points in $\mathbb{R}^2$ determine a convex polygon and the set of distances between
them is $\{u_1,\ldots,u_t\}$. Suppose $u_i$ appears as the distance between $f(u_i)$ many pairs of
points. Then
$$\sum_i f(u_i)^2 \ll n^3.$$

In [Er97c] Erdős claims that Fishburn solved this, but gives no reference.
-/
@[category research solved, AMS 5 52, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos94.lean"]
theorem erdos_94 : ∃ C > (0 : ℝ), ∀ P : Finset ℝ², ConvexIndep (P : Set ℝ²) →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤ C * (P.card : ℝ) ^ 3 := by
  sorry

/--
Note it is trivial that $\sum f(u_i)=\binom{n}{2}$.
-/
@[category test, AMS 5 52]
theorem erdos_94.variants.sum_multiplicity (P : Finset ℝ²) :
    ∑ u ∈ distanceSet P, distanceMultiplicity P u = P.card.choose 2 := by
  sorry

/--
Lefmann and Theile [LeTh95] prove a stronger version of this question, that
$$\sum_i f(u_i)^2 \ll n^3$$
under the weaker assumption that no three points are on a line.
-/
@[category research solved, AMS 5 52]
theorem erdos_94.variants.no_three_on_a_line : ∃ C > (0 : ℝ), ∀ P : Finset ℝ²,
    NonTrilinear (P : Set ℝ²) →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤ C * (P.card : ℝ) ^ 3 := by
  sorry

/--
Erdős and Fishburn also make the stronger conjecture that $\sum f(u_i)^2$ is maximal for the
regular $n$-gon (for large enough $n$).
-/
@[category research open, AMS 5 52]
theorem erdos_94.variants.regular_ngon : ∀ᶠ n : ℕ in atTop, ∀ P : Finset ℝ²,
    P.card = n → ConvexIndep (P : Set ℝ²) →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤
      ∑ u ∈ distanceSet (regularNGon n), (distanceMultiplicity (regularNGon n) u : ℝ) ^ 2 := by
  sorry

end Erdos94


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
