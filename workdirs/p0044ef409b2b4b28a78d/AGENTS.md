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
import FormalConjectures.ErdosProblems.«1041»

/-!
# Erdős Problem 1044

*References:*
- [erdosproblems.com/1044](https://www.erdosproblems.com/1044)
- [EHP58] Erdős, P. and Herzog, F. and Piranian, G., *Metric properties of polynomials*.
  J. Analyse Math. (1958), 125-148.
- [Ta26] Tang, Quanyu, *On Erdős Problem 1044* (2026),
  [github.com/QuanyuTang/erdos-problem-1044](https://github.com/QuanyuTang/erdos-problem-1044).
-/

open Polynomial ENNReal

namespace Erdos1044

/--
The polynomials under consideration: those of the form $f(z)=\prod_{i=1}^n(z-z_i)$, for some
$n\geq 1$, where $\lvert z_i\rvert\leq 1$ for all $i$.
-/
def IsAdmissible (f : ℂ[X]) : Prop :=
  ∃ n : ℕ, 0 < n ∧ ∃ z : Fin n → ℂ, (∀ i, ‖z i‖ ≤ 1) ∧ f = ∏ i, (X - C (z i))

/--
$\Lambda(f)$, the maximum of the lengths of the boundaries of the connected components of
$\{ z: \lvert f(z)\rvert<1\}$, where the length of a subset of $\mathbb{C}$ is its
$1$-dimensional Hausdorff measure.
-/
noncomputable def maxBoundaryLength (f : ℂ[X]) : ℝ≥0∞ :=
  ⨆ z ∈ {w : ℂ | ‖f.eval w‖ < 1},
    Erdos1041.length (frontier (connectedComponentIn {w : ℂ | ‖f.eval w‖ < 1} z))

/--
Let $f(z)=\prod_{i=1}^n(z-z_i)\in\mathbb{C}[x]$ where $\lvert z_i\rvert\leq 1$ for all $i$.
If $\Lambda(f)$ is the maximum of the lengths of the boundaries of the connected components of
$$
\{ z: \lvert f(z)\rvert<1\}
$$
then determine the infimum of $\Lambda(f)$.

A problem of Erdős, Herzog, and Piranian [EHP58].

This has been resolved by Tang, who proved that the infimum of $\Lambda(f)$ over all such $f$
is $2$.
-/
@[category research solved, AMS 30, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1044.lean"]
theorem erdos_1044 :
    IsGLB {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ maxBoundaryLength f = L} answer(2) := by
  sorry

/--
This has been resolved by Tang, who proved that the infimum of $\Lambda(f)$ over all such $f$
is $2$.
-/
@[category research solved, AMS 30, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1044.lean"]
theorem erdos_1044.variants.infimum_eq_two :
    IsGLB {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ maxBoundaryLength f = L} 2 := by
  sorry

/--
Tang also suggests that, if the degree $n$ is fixed, then the infimum over all such $f$ of
degree $n$ is attained by $f_n(z)=z^n-1$.
-/
@[category research open, AMS 30]
theorem erdos_1044.variants.fixed_degree (n : ℕ) (hn : 0 < n) :
    IsLeast {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ f.natDegree = n ∧ maxBoundaryLength f = L}
      (maxBoundaryLength (X ^ n - 1)) := by
  sorry

/--
Tang also suggests that, if the degree $n$ is fixed, then the infimum over all such $f$ of
degree $n$ is attained by $f_n(z)=z^n-1$ (and proves this for $n=1$ and $n=2$).
-/
@[category research solved, AMS 30]
theorem erdos_1044.variants.fixed_degree_of_le_two (n : ℕ) (hn : n = 1 ∨ n = 2) :
    IsLeast {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ f.natDegree = n ∧ maxBoundaryLength f = L}
      (maxBoundaryLength (X ^ n - 1)) := by
  sorry

end Erdos1044


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
