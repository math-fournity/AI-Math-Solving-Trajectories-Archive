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
# Erdős Problem 413

*References:*
- [erdosproblems.com/413](https://www.erdosproblems.com/413)
- [A5236](https://oeis.org/A5236)

Erdős called a natural number `n` a *barrier* for `ω`, the number of distinct prime divisors,
if `m + ω(m) ≤ n` for all `m < n`. He believed there should be infinitely many such barriers, and
even posed a relaxed variant asking whether there is some `ε > 0` for which infinitely many `n`
satisfy `m + ε · ω(m) ≤ n` for every `m < n`.
-/

open ArithmeticFunction
open scoped omega Omega

namespace Erdos413

/-- `IsBarrier f n` means `n` is a barrier for the real-valued function `f`,
i.e. `(m : ℝ) + f m ≤ (n : ℝ)` for all `m < n`. -/
def IsBarrier (f : ℕ → ℝ) (n : ℕ) : Prop :=
  ∀ m < n, (m : ℝ) + f m ≤ n

/-- Are there infinitely many barriers for `ω`? -/
@[category research open, AMS 11]
theorem erdos_413.parts.i :
    answer(sorry) ↔ { n | IsBarrier (fun m => ω m) n }.Infinite := by
  sorry

/-- `expProd n` is `∏ kᵢ` when `n = ∏ pᵢ ^ kᵢ`, i.e. the product of the prime exponents of `n`. -/
def expProd (n : ℕ) : ℕ :=
  n.factorization.prod fun _ e => e

/-- Erdős proved that the barrier set for `expProd` is infinite and even has positive density.

`HasPosDensity` is the right reading rather than positive lower density. In [Er79d] this is
Theorem 1, "the density of integers satisfying (2) is positive", where `d₀(n) = ∏ αᵢ` is
`expProd`. The averaging argument there bounds the density below, but Erdős states the existence
separately on the last page: "With a little more trouble, I can prove that the density of
integers `n` for which `n` is a barrier for `d₀(n)` exists." He goes further, that if `αᵢ` is the
density of `n` with `max_{m<n} (m + d₀(m)) = n + i`, then every `αᵢ` exists and they sum to `1`.

[Er79d] Erdős, P., *Some unconventional problems in number theory*.
Acta Math. Acad. Sci. Hungar. (1979), 71-80. -/
@[category research solved, AMS 11]
theorem erdos_413.variants.hasPosDensity_barrier_expProd :
    { n | IsBarrier (fun m => expProd m) n }.HasPosDensity := by
  sorry

/-- Erdős believed there should be infinitely many barriers for `Ω`, the total prime multiplicity. -/
@[category research open, AMS 11]
theorem erdos_413.variants.bigOmega :
    answer(sorry) ↔ { n | IsBarrier (fun m => Ω m) n }.Infinite := by
  sorry

/-- Selfridge computed that the largest `Ω`-barrier below `10^5` is `99840`. -/
@[category research solved, AMS 11]
theorem erdos_413.variants.bigOmega_largest_barrier_lt_100k :
    IsGreatest {n : ℕ | n < 10 ^ 5 ∧ IsBarrier (fun m => Ω m) n} 99840 := by
  sorry

/-- Does there exist some `ε > 0` such that there are infinitely many `ε`-barriers for `ω`? -/
@[category research open, AMS 11]
theorem erdos_413.parts.ii :
    answer(sorry) ↔
        (∃ ε > (0 : ℝ), { n | IsBarrier (fun n => ε * ω n) n }.Infinite) := by
  sorry

end Erdos413


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
