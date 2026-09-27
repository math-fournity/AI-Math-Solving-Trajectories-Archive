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
# Erdős Problem 422

*Reference:* [erdosproblems.com/422](https://www.erdosproblems.com/422)
-/

namespace Erdos422

open Filter
open scoped Topology

/--
Let $f(1) = f(2) = 1$ and for $n > 2$
$$
f(n) = f(n - f(n - 1)) + f(n - f(n - 2)).
$$

Note: It is not known whether $f(n)$ is well-defined for all $n$.
-/
partial def f : ℕ+ → ℕ+
  | 1 => 1
  | 2 => 1
  | n => f (n - f (n - 1)) + f (n - f (n - 2))

/--
Does $f(n)$ miss infinitely many integers?
-/
@[category research open, AMS 11]
theorem erdos_422 : answer(sorry) ↔ Set.Infinite {n | ∀ x, f x ≠ n} := by
  sorry

/--
Is $f$ surjective?
-/
@[category research open, AMS 11]
theorem erdos_422.variants.surjective : answer(sorry) ↔ f.Surjective := by
  sorry

/--
How does $f$ grow?
-/
@[category research open, AMS 11]
theorem erdos_422.variants.growth_rate :
    (fun n ↦ (f n : ℝ)) =O[atTop] (answer(sorry) : ℕ+ → ℝ) := by
  sorry

/--
Does $f$ become stationary at some point?
-/
@[category research open, AMS 11]
theorem erdos_422.variants.eventually_const : answer(sorry) ↔ EventuallyConst f atTop := by
  sorry

end Erdos422


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
