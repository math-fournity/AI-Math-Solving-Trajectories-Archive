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
# Main conjecture on fusible numbers

*References:*
- [Fusible numbers and Peano Arithmetic](https://arxiv.org/abs/2003.14342),
  by Jeff Erickson, Gabriel Nivasch, and Junyan Xu.
- [Fusible numbers and Peano Arithmetic](https://doi.org/10.46298/lmcs-18%283%3A6%292022),
  Logical Methods in Computer Science, Volume 18, Issue 3 (July 28, 2022).
-/

namespace FusibleNumber

/--
A rational number is fusible if it belongs to the smallest set containing $0$ and closed under
the operation
$$
a \sim b = \frac{a + b + 1}{2}
$$
whenever $|a-b| < 1$.
-/
inductive IsFusible : ℚ → Prop
  | zero : IsFusible 0
  | fuse (a b : ℚ) : IsFusible a → IsFusible b → |a - b| < 1 → IsFusible ((a + b + 1) / 2)

/-- The rational number $1/2$ is fusible. -/
@[category test, AMS 5]
theorem isFusible_one_half : IsFusible (1 / 2 : ℚ) := by
  have h := IsFusible.fuse 0 0 IsFusible.zero IsFusible.zero (by norm_num)
  norm_num at h
  exact h

/-- The rational number $1$ is fusible. -/
@[category test, AMS 5]
theorem isFusible_one : IsFusible (1 : ℚ) := by
  have h := IsFusible.fuse (1 / 2) (1 / 2) isFusible_one_half isFusible_one_half (by norm_num)
  norm_num at h
  exact h

/-- If `x` is a fusible number and `y` is its successor, then the interval `[x + 1, y + 1)` can be
divided into intervals `[ℓₙ, ℓₙ₊₁)`, such that the fusible numbers in `[ℓₙ, ℓₙ₊₁)` are obtained by
fusing the `n + 1`st successor of `x` with a fusible number.
This formalization differs from Conjecture 7.1 in the paper in four ways:
(1) it is obtained from Conjecture 7.1 by plugging in `n + 1` into `n`, which simplifies the expressions
  and removes the need to assume `n ≥ 1`;
(2) the `n + 1`st successor `s^(n+1)(x)` is replaced by the explicit value `x + (2 - 1 / 2 ^ n) * m`;
(3) instead of defining `y` to be the successor of `x`, we assert that there is no fusible number
  strictly between `x` and `y`;
(4) instead of using `∃ z, IsFusible z ∧ q = s^(n+1)(x) ~ z` we use the value of `z` determined by the equality,
  namely `z = 2 * q - 1 - s^(n+1)(x)`, and it is easy to see `z ∈ [x + 1 - m / 2 ^ n, x + 1)` as required. -/
@[category research open, AMS 5]
theorem conj_7_1 (x y q : ℚ) (n : ℕ) (fus_x : IsFusible x) (fus_y : IsFusible y) (lt : x < y)
    (nmem_Ioo : ∀ z, IsFusible z → z ∉ Set.Ioo x y) :
    let m := y - x
    let ℓ (n : ℕ) := y + 1 - m / 2 ^ n
    IsFusible q → q ∈ Set.Ico (ℓ n) (ℓ (n + 1)) → IsFusible (2 * q - 1 - x - (2 - 1 / 2 ^ n) * m) := by
  sorry

end FusibleNumber


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
