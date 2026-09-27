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
# Representations with prime conditions

Any integer $n > 1$ can be written as $x + y$ with $x, y > 0$ such that both $x + ny$ and
$x^2 + ny^2$ are prime.

Zhi-Wei Sun has offered a $200 prize for the first proof.

*References:*
- [A232174](https://oeis.org/A232174)
- Z.-W. Sun, "Conjectures on representations involving primes," in: M. Nathanson (ed.),
  Combinatorial and Additive Number Theory II: CANT, Springer Proc. in Math. & Stat.,
  Vol. 220, Springer, 2017, pp. 279-310. https://arxiv.org/abs/1211.1588
- D.A. Cox, "Primes of the Form x² + ny²," John Wiley & Sons, 1989.
-/

namespace OeisA232174

/-- The predicate that `n` can be written as $x + y$ with $x, y > 0$ such that both
$x + ny$ and $x^2 + ny^2$ are prime. -/
def A (n : ℕ) : Prop :=
  ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ n = x + y ∧ (x + n * y).Prime ∧ (x ^ 2 + n * y ^ 2).Prime

@[category test, AMS 11]
theorem a_2 : A 2 :=
  ⟨1, 1, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

@[category test, AMS 11]
theorem a_3 : A 3 :=
  ⟨2, 1, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

@[category test, AMS 11]
theorem a_4 : A 4 :=
  ⟨1, 3, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

@[category test, AMS 11]
theorem a_5 : A 5 :=
  ⟨3, 2, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

@[category test, AMS 11]
theorem a_6 : A 6 :=
  ⟨5, 1, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

@[category test, AMS 11]
theorem a_8 : A 8 :=
  ⟨5, 3, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

/--
**Zhi-Wei Sun's Conjecture (A232174)**: Any integer $n > 1$ can be written as $x + y$ with
$x, y > 0$ such that both $x + ny$ and $x^2 + ny^2$ are prime.
-/
@[category research open, AMS 11]
theorem conjecture (n : ℕ) (hn : 1 < n) : A n := by
  sorry

end OeisA232174


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
