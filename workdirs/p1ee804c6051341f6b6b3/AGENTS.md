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
# Erdős Problem 968

Let `uₙ = pₙ / n`, where `pₙ` is the `n`th prime. Does the set of `n` such that `uₙ < uₙ₊₁`
have positive lower density?

Erdős and Prachar also proved that `∑_{pₙ < x} |uₙ₊₁ - uₙ| ≍ (log x)^2`, and that the set of `n`
such that `uₙ > uₙ₊₁` has positive lower density. Erdős also asked whether there are infinitely many
increasing triples `uₙ < uₙ₊₁ < uₙ₊₂` or decreasing triples `uₙ > uₙ₊₁ > uₙ₊₂`.

*Reference:* [erdosproblems.com/968](https://www.erdosproblems.com/968)

[ErPr61] Erdős, P. and Prachar, K., _Sätze und Probleme über pₖ/k_. Abh. Math. Sem. Univ. Hamburg
(1961/62), 251–256.
-/

open Filter Real
open scoped BigOperators

namespace Erdos968

/--
`u n` is the normalized `n`th prime, defined as `pₙ / (n+1)` where `pₙ` is the `n`th prime
(with `0.nth Nat.Prime = 2`).

This corresponds to the classical sequence `(p₁/1, p₂/2, p₃/3, ...)` while using `Nat.nth Prime`'s
`0`-based indexing; in particular, the denominator is always positive.
-/
noncomputable def u (n : ℕ) : ℝ :=
  (n.nth Nat.Prime : ℝ) / (n + 1)

/--
Does the set `{n | u n < u (n+1)}` have positive lower density?
-/
@[category research open, AMS 11]
theorem erdos_968 : answer(sorry) ↔ 0 < {n : ℕ | u n < u (n + 1)}.lowerDensity := by
  sorry

/--
Erdős and Prachar proved `∑_{pₙ < x} |u (n+1) - u n| ≍ (log x)^2` (see [ErPr61]).

We encode `∑_{pₙ < x}` as a sum over `n < Nat.primeCounting' x` (the number of primes `< x`).
-/
@[category research solved, AMS 11]
theorem erdos_968.variants.sum_abs_diff_isTheta_log_sq :
    (fun x : ℕ =>
        ∑ n < Nat.primeCounting' x, |u (n + 1) - u n|) =Θ[atTop]
      fun x : ℕ => log x ^ 2 := by
  sorry

/--
Erdős and Prachar proved that the set `{n | u n > u (n+1)}` has positive lower density
(see [ErPr61]).
-/
@[category research solved, AMS 11]
theorem erdos_968.variants.decreasing_steps_pos_lower_density :
    0 < {n : ℕ | u n > u (n + 1)}.lowerDensity := by
  sorry

/--
Erdős asked whether there are infinitely many solutions to `uₙ < uₙ₊₁ < uₙ₊₂`.
-/
@[category research open, AMS 11]
theorem erdos_968.variants.infinite_increasingTriples :
    answer(sorry) ↔ {n : ℕ | u n < u (n + 1) ∧ u (n + 1) < u (n + 2)}.Infinite := by
  sorry

/--
Erdős asked whether there are infinitely many solutions to `uₙ > uₙ₊₁ > uₙ₊₂`.
-/
@[category research open, AMS 11]
theorem erdos_968.variants.infinite_decreasingTriples :
    answer(sorry) ↔ {n : ℕ | u n > u (n + 1) ∧ u (n + 1) > u (n + 2)}.Infinite := by
  sorry

end Erdos968


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
