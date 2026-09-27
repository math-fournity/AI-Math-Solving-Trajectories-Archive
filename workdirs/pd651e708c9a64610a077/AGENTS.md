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
# Equidistributed Sequences

Corollary 4.2 of Chapter 1 states that the sequence $(x^n), n = 1, 2, ... ,$ is equidistributed modulo 1 for
almost all x > 1. And a little bit further down:
"one does not know whether sequences such as $(e^n)$, $(π^n)$, or even $((\frac 3 2)^n)$"
are equidistributed modulo 1 or not.

*References:*
  - [Uniform Distribution of Sequences](https://store.doverpublications.com/products/9780486149998)
by *L. Kuipers* and *H. Niederreiter*, 1974
  - [Wikipedia](https://en.wikipedia.org/wiki/Equidistributed_sequence)
-/

namespace Equidistribution

open scoped Topology

/--
A point `x` is an accumulation point of a sequence `s_0, s_1, ...`
if any neighbourhood of `x` contains a point of the sequence distinct
from `x`.
-/
def IsAccumulationPoint (x : ℝ) (s : ℕ → ℝ) : Prop :=
  x ∈ closure (Set.range s \ {x})

/--
If a point `x` is an accumulation point of a sequence `s_0, s_1, ...` then
there is a subsequence of `s` that tends to `x`
-/
def isAccumulationPoint_iff_exists_subsequence_tendsto
    (x : ℝ) (s : ℕ → ℝ) (hx : IsAccumulationPoint x s) :
    ∃ (u : ℕ → ℕ), StrictMono u ∧ Filter.atTop.Tendsto (s ∘ u) (𝓝 x) := by
  sorry

/--
The sequence `(3/2)^n` is equidistributed modulo `1`.
-/
@[category research open, AMS 11]
theorem isEquidistributedModuloOne_three_halves_pow :
    IsEquidistributedModuloOne (fun n => (3 / 2 : ℝ)^n) := by
  sorry

/-- For any transcendental number `x`, the sequence `x * (3 / 2) ^ n` is
equidistributed modulo 1. -/
@[category research open, AMS 11]
theorem isEquidistributedModuloOne_transcendental_three_halves_pow (x : ℝ)
    (hx : Transcendental ℚ x) :
    IsEquidistributedModuloOne (fun n ↦ x * (3 / 2 : ℝ) ^ n) := by
  sorry

/--
The sequence `(3/2)^n` has infinitely many accumulation points modulo `1`.
-/
@[category research solved, AMS 11]
theorem isAccumulationPoint_three_halves_pow_infinite :
    {x | IsAccumulationPoint x (fun n => Int.fract <| (3 / 2 : ℝ)^n)}.Infinite := by
  sorry

/--
Find an accumulation point of the sequence `(3/2)^n` modulo `1`.
-/
@[category research open, AMS 11]
theorem isAccumulationPoint_three_halves_pow :
    IsAccumulationPoint answer(sorry) (fun n => Int.fract <| (3 / 2 : ℝ)^n) := by
  sorry

/--
There is an accumulation point of the sequence `(3/2)^n` modulo `1`.
-/
@[category test, AMS 11]
theorem isAccumulationPoint_three_halves_pow_exists :
    ∃ p, (IsAccumulationPoint p (fun n => Int.fract <| (3 / 2 : ℝ)^n)) := by
  sorry

end Equidistribution


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
