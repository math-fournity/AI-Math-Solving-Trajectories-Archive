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
# Erdős Problem 951

*References:*
 - [erdosproblems.com/951](https://www.erdosproblems.com/951)
 - [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III. Number theory day (Proc. Conf., Rockefeller Univ.,
    New York, 1976) (1977), 43-72.
-/

open scoped Finsupp Nat.Prime Topology
open Filter

namespace Erdos951

/-- A sequence `a : ℕ → ℝ` is said to have property `Erdos951Prop` if for any pair of distinct
finitely supported sequences `k l : ℕ →₀ ℕ` their corresponding Beurling integers are of distance
at least one apart. -/
def Erdos951Prop (a : ℕ → ℝ) : Prop :=
  ∀ (k ℓ : ℕ →₀ ℕ), k ≠ ℓ → |beurlingInteger a k - beurlingInteger a ℓ| ≥ 1

/-- If `a` has property `Erdos951Prop` and `1 < a 0`, then `a` is a set of Beurling
prime numbers. -/
@[category API, AMS 11]
theorem erdos_951.variants.isBeurlingPrimes {a : ℕ → ℝ} (ha : 1 < a 0)
    (hm : StrictMono a) (he : Erdos951Prop a) :
    IsBeurlingPrimes a := by
  refine ⟨ha, hm, tendsto_atTop_atTop.2 fun x => ?_⟩
  by_contra h_contra
  obtain ⟨L, hL⟩ : ∃ L, Filter.Tendsto a Filter.atTop (𝓝 L) :=
    ⟨_, tendsto_atTop_isLUB hm.monotone (isLUB_ciSup ⟨x, Set.forall_mem_range.2 fun n =>
    le_of_not_ge fun hn => h_contra ⟨n, fun m hm' => hn.trans (hm.monotone hm')⟩⟩)⟩
  obtain ⟨N, hN⟩ := Metric.tendsto_atTop.mp hL (1 / 2) (by norm_num)
  have := hm (by linarith : N < N + 1)
  have h_diff : a (N + 1) - a N ≥ 1 := by
    rw [← abs_of_nonneg (by linarith : 0 ≤ a _ - _)]
    simpa using he (.single (N + 1) 1) (.single N 1) (by simpa [Finsupp.ext_iff] using ⟨N, by simp⟩)
  linarith [abs_lt.1 (hN N le_rfl), abs_lt.1 (hN (N + 1) (by grind))]

/-- If `1 < a 0 < ...` has property `Erdos951Prop`, is it true that `#{a i ≤ x} ≤ π x`? -/
@[category research open, AMS 11]
theorem erdos_951 : answer(sorry) ↔
    ∀ a : ℕ → ℝ, 1 < a 0 → StrictMono a → Erdos951Prop a →
      ∀ᶠ (x : ℝ) in Filter.atTop, {i : ℕ | a i ≤ x}.ncard ≤ π ⌊x⌋₊ := by
  sorry

/-- Beurling conjectured that if the number of Beurling integer in `[1, x]`
is `x + o(log x)`, then `a` must be the sequence of primes. -/
@[category research solved, AMS 11]
theorem erdos_951.variants.beurling :
    ∀ a : ℕ → ℝ, IsBeurlingPrimes a →
    ((fun x => (BeurlingIntegers a ∩ .Iic x).ncard - x) =o[atTop] Real.log) →
    a = Nat.cast ∘ Nat.nth Nat.Prime := by
  sorry

end Erdos951


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
