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
# Green's Open Problem 22

*References:*
- [Gr26] [Ben Green's Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.22)
- [Mo17] Moreira, Joel. "Monochromatic sums and products in N." Annals of Mathematics 185.3 (2017):
  1069-1090.
- [GrSa25] Green, Ben, and Mehtaab Sawhney. "Bounds for monochromatic solutions to
  $\{x+ y, xy\} $." arXiv preprint arXiv:2511.09365 (2025).
- [Ri25] Richter, Florian K. "Sums and products in sets of positive density." arXiv preprint
  arXiv:2507.00515 (2025).
- [BoSa24] Bowen, Matt, and Marcin Sabok. "Monochromatic products and sums in the rationals." Forum
  of Mathematics, Pi. Vol. 12. Cambridge University Press, 2024.
- [Bo25] Bowen, Matt. "Monochromatic products and sums in 2-colorings of N." Advances in Mathematics
  462 (2025): 110095.
- [Al23] Alweiss, Ryan. "Monochromatic Sums and Products over $\mathbb {Q} $." arXiv preprint
  arXiv:2307.08901 (2023).
-/

open Finset Filter

namespace Green22

/--
The monochromatic sum-product property: a colouring $c$ of $\{1, \ldots, N\}$ has a pair $(x, y)$
with $x, y \geq 3$ such that $x + y$ and $xy$ are both in $\{1, \ldots, N\}$ and receive the same
colour.
-/
def HasMonochromaticSumProduct (N : ℕ) (r : ℕ) (coloring : Icc 1 N → Fin r) : Prop :=
  ∃ x y : ℕ, 3 ≤ x ∧ 3 ≤ y ∧
    ∃ h_sum : x + y ∈ Icc 1 N, ∃ h_prod : x * y ∈ Icc 1 N,
      coloring ⟨x + y, h_sum⟩ = coloring ⟨x * y, h_prod⟩

/--
$N_0(r)$ is the smallest $N$ such that every $r$-colouring of $\{1, \ldots, N\}$ has the
monochromatic sum-product property.
-/
noncomputable def N₀ (r : ℕ) : ℕ :=
  sInf {N | ∀ c : Icc 1 N → Fin r, HasMonochromaticSumProduct N r c}

open scoped Asymptotics

/-- The upper bound function from [GrSa25]. -/
noncomputable def GreenSawhneyBound (r : ℕ) : ℝ := Real.exp (Real.exp (r ^ 50))

/--
If $\{1, \ldots, N\}$ is $r$-coloured then, for $N \geqslant N_0(r)$, there are integers
$x, y \geqslant 3$ such that $x + y, xy$ have the same colour.

Find reasonable bounds for $N_0(r)$. The goal is to improve upon the Green-Sawhney bound.
-/
@[category research open, AMS 5 11]
theorem green_22 :
    let ans := (answer(sorry) : ℕ → ℝ)
    ∀ᶠ r in atTop, N₀ r ≤ ans r ∧
    ans =o[atTop] GreenSawhneyBound := by
  sorry

/--
[GrSa25, Theorem 1.1] found a permissible upper bound.
-/
@[category research solved, AMS 5 11]
theorem green_22.variants.green_sawhney_bound :
    ∀ᶠ r in atTop, N₀ r ≤ GreenSawhneyBound r := by
  sorry

/--
[Mo17, Corollary 1.5] For any finite coloring of $\mathbb{N}$ there exist (infinitely many)
$x, y \in \mathbb{N}$ such that $\{xy, x + y\}$ is monochromatic.

This guarantees that $N_0(r)$ is well-defined.

Note: [Mo17] also establishes that $x$ is of the same colour.
-/
@[category research solved, AMS 5 11]
theorem green_22.variants.moreira_infinite :
    ∀ (r : ℕ) (coloring : ℕ → Fin r),
    Set.Infinite { p : ℕ × ℕ |
      0 < p.1 ∧ 0 < p.2 ∧
      coloring p.1 = coloring (p.1 * p.2) ∧
      coloring p.1 = coloring (p.1 + p.2) } := by
  sorry

/--
Since $x, y \geq 3$, we must have $xy \geq 9$, so $N_0(r) \geq 9$
(assuming $N_0(r)$ is well-defined, which follows from [Mo17]).
-/
@[category research solved, AMS 5 11]
theorem green_22.variants.lower_nine : ∀ r : ℕ, r ≠ 0 → 9 ≤ N₀ r := by
  sorry

-- TODO(jeangud) Add Hindman's problem versions mentioned in [Gr26].

end Green22


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
