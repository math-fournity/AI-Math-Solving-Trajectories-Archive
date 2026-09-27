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
# The 1680-Conjecture

Any nonnegative integer can be written as $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative
integers such that $x^4 + 1680 y^3 z$ is a square.

Zhi-Wei Sun has offered a prize of 1,680 RMB for the first proof.

*References:*
- [A280831](https://oeis.org/A280831)
- Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
- Z.-W. Sun, "Refining Lagrange's four-square theorem," arXiv:1604.06723 [math.NT], 2016.
-/

namespace OeisA280831

/-- The predicate that `n` can be written as $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative
integers such that $x^4 + 1680 y^3 z$ is a square. -/
def A (n : ℕ) : Prop :=
  ∃ x y z w : ℕ, n = x ^ 2 + y ^ 2 + z ^ 2 + w ^ 2 ∧ IsSquare (x ^ 4 + 1680 * y ^ 3 * z)

@[category test, AMS 11]
theorem a_0 : A 0 :=
  ⟨0, 0, 0, 0, by norm_num, 0, by norm_num⟩

@[category test, AMS 11]
theorem a_1 : A 1 :=
  ⟨1, 0, 0, 0, by norm_num, 1, by norm_num⟩

@[category test, AMS 11]
theorem a_2 : A 2 :=
  ⟨1, 0, 0, 1, by norm_num, 1, by norm_num⟩

@[category test, AMS 11]
theorem a_3 : A 3 :=
  ⟨1, 0, 1, 1, by norm_num, 1, by norm_num⟩

@[category test, AMS 11]
theorem a_4 : A 4 :=
  ⟨2, 0, 0, 0, by norm_num, 4, by norm_num⟩

@[category test, AMS 11]
theorem a_7 : A 7 :=
  ⟨1, 1, 1, 2, by norm_num, 41, by norm_num⟩

@[category test, AMS 11]
theorem a_95 : A 95 :=
  ⟨6, 3, 1, 7, by norm_num, 216, by norm_num⟩

/--
**Zhi-Wei Sun's 1680-Conjecture (A280831)**: Any nonnegative integer can be written as
$x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative integers such that $x^4 + 1680 y^3 z$ is a square.
-/
@[category research open, AMS 11]
theorem conjecture (n : ℕ) : A n := by
  sorry

end OeisA280831


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
