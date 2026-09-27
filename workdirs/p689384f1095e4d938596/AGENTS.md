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
# Lander, Parkin, and Selfridge Conjecture

**Reference:** https://en.wikipedia.org/wiki/Lander,_Parkin,_and_Selfridge_conjecture
-/

namespace LanderParkinSelfridge

/-- The Lander–Parkin–Selfridge conjecture: if the sum of $n$ positive integer $k$-th powers
equals the sum of $m$ positive integer $k$-th powers, with all values on the left distinct from
all values on the right, then $n + m \geq k$.

Formally, for positive integers $k, n, m \in \mathbb{N}$ and sequences
$x : \{0, \ldots, n-1\} \to \mathbb{N}$ and $y : \{0, \ldots, m-1\} \to \mathbb{N}$
with $x_i > 0$, $y_j > 0$, and $x_i \neq y_j$ for all $i, j$, if
$$\sum_{i=0}^{n-1} x_i^k = \sum_{j=0}^{m-1} y_j^k,$$
then $k \leq n + m$. -/
@[category research open, AMS 11]
theorem lander_parkin_selfridge :
    ∀ (k n m : ℕ) (x : Fin n → ℕ) (y : Fin m → ℕ),
      0 < n → 0 < m →
      (∀ i, 0 < x i) → (∀ j, 0 < y j) →
      (∀ i j, x i ≠ y j) →
      ∑ i, x i ^ k = ∑ j, y j ^ k →
      k ≤ n + m := by
  sorry

/-- Special case of the Lander–Parkin–Selfridge conjecture: there is no solution in positive
integers to
$$x_1^5 + x_2^5 + x_3^5 = y^5.$$
That is, for all $x_1, x_2, x_3, y \in \mathbb{N}$ with $x_1, x_2, x_3, y > 0$,
$$x_1^5 + x_2^5 + x_3^5 \neq y^5.$$
This corresponds to the case $k = 5$, $n = 3$, $m = 1$ of the general conjecture,
where $n + m = 4 < 5 = k$ would be required to yield a counterexample. -/
@[category research open, AMS 11]
theorem lander_parkin_selfridge.variants.five_three :
    ∀ x₁ x₂ x₃ y : ℕ,
      0 < x₁ → 0 < x₂ → 0 < x₃ → 0 < y →
      x₁ ^ 5 + x₂ ^ 5 + x₃ ^ 5 ≠ y ^ 5 := by
  sorry

end LanderParkinSelfridge


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
