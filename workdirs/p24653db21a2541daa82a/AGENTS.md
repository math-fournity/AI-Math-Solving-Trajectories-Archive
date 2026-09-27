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
# Erdős Problem 1109

*References:*
- [erdosproblems.com/1109](https://www.erdosproblems.com/1109)
- [ErSa87] P. Erdős and A. Sárközy, *On divisibility properties of integers of the form
  $a+a'$*, Acta Math. Hungar. (1987), 117--122.
- [Gy01] Katalin Gyarmati, *On divisibility properties of integers of the form $ab+1$*,
  Period. Math. Hungar. (2001), 71--79.
- [Ko04] S. V. Konyagin, *Problems of the set of square-free numbers*,
  Izv. Ross. Akad. Nauk Ser. Mat. (2004), 63--90.
- [Sa92c] G. N. Sárközy, *On a problem of P. Erdős*, Acta Math. Hungar.
  (1992), 271--282.
-/

open Filter Asymptotics
open scoped Pointwise

namespace Erdos1109

/--
`f N` is the largest size of a subset `A ⊆ {1, ..., N}` such that every element
of `A + A` is squarefree.
-/
noncomputable def f (N : ℕ) : ℕ :=
  sSup {k : ℕ | ∃ A : Finset ℕ,
    A ⊆ Finset.Icc 1 N ∧ (∀ n ∈ A + A, Squarefree n) ∧ A.card = k}

/--
Let $f(N)$ be the size of the largest subset $A\subseteq \{1,\ldots,N\}$ such that
every $n\in A+A$ is squarefree. Estimate $f(N)$. In particular, is it true that
$f(N)\leq N^{o(1)}$, or even $f(N) \leq (\log N)^{O(1)}$?

This theorem formalizes the subpolynomial bound as `f(N) = O(N^ε)` for every `ε > 0`.
-/
@[category research open, AMS 5 11]
theorem erdos_1109 :
    answer(sorry) ↔ ∀ ε > (0 : ℝ),
      (fun N : ℕ => (f N : ℝ)) ≪ fun N : ℕ => (N : ℝ) ^ ε := by
  sorry

/--
Is the stronger polylogarithmic bound $f(N) \leq (\log N)^{O(1)}$ true?
-/
@[category research open, AMS 5 11]
theorem erdos_1109.variants.polylog :
    answer(sorry) ↔ ∃ C > (0 : ℝ),
      (fun N : ℕ => (f N : ℝ)) ≪ fun N : ℕ => (Real.log N) ^ C := by
  sorry

/--
Erdős and Sárközy [ErSa87] proved the lower bound $\log N \ll f(N)$.
-/
@[category research solved, AMS 5 11]
theorem erdos_1109.variants.erdos_sarkozy_lower :
    (fun N : ℕ => Real.log N) ≪ fun N : ℕ => (f N : ℝ) := by
  sorry

/--
Erdős and Sárközy [ErSa87] proved the upper bound $f(N) \ll N^{3/4}\log N$.
-/
@[category research solved, AMS 5 11]
theorem erdos_1109.variants.erdos_sarkozy_upper :
    (fun N : ℕ => (f N : ℝ)) ≪
      fun N : ℕ => (N : ℝ) ^ ((3 : ℝ) / 4) * Real.log N := by
  sorry

/--
Konyagin [Ko04] improved the lower bound to
$\log\log N(\log N)^2 \ll f(N)$.
-/
@[category research solved, AMS 5 11]
theorem erdos_1109.variants.konyagin_lower :
    (fun N : ℕ => Real.log (Real.log N) * (Real.log N) ^ 2) ≪
      fun N : ℕ => (f N : ℝ) := by
  sorry

/--
Konyagin [Ko04] improved the upper bound to $f(N) \ll N^{11/15+o(1)}$.
-/
@[category research solved, AMS 5 11]
theorem erdos_1109.variants.konyagin_upper :
    ∀ ε > (0 : ℝ), (fun N : ℕ => (f N : ℝ)) ≪
      fun N : ℕ => (N : ℝ) ^ ((11 : ℝ) / 15 + ε) := by
  sorry

end Erdos1109


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
