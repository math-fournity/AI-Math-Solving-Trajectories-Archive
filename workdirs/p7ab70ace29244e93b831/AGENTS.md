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
# Erdős Problem 264

*Reference:* [erdosproblems.com/264](https://www.erdosproblems.com/264)
-/

namespace Erdos264

open Filter

open scoped ENNReal Asymptotics

/--
A sequence $a_n$ of integers is called an irrationality sequence if for every bounded sequence of integers $b_n$ with $a_n + b_n \neq 0$ and
$b_n \neq 0$ for all $n$, the sum
$$
  \sum \frac{1}{a_n + b_n}
$$
is irrational.

Note: there are other possible definitions of this concept. See
FormalConjectures/ErdosProblems/263.lean for another possible definition.
-/
def IsIrrationalitySequence (a : ℕ → ℕ) : Prop := ∀ b : ℕ → ℤ,
  BddAbove (Set.range b) → BddBelow (Set.range b) →
  0 ∉ Set.range (fun n ↦ (a n : ℤ) + b n) → 0 ∉ Set.range b →
  Irrational (∑' n, (1 : ℝ) / ((a n : ℤ) + b n))

/--
Is $2^n$ an example of an irrationality sequence? Kovač and Tao proved that it is not [KoTa24]

[KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series. arXiv:2406.17593 (2024).
-/
@[category research solved, AMS 11]
theorem erdos_264.parts.i : ¬IsIrrationalitySequence (2 ^ ·) := by sorry

/--
Is $n!$ an example of an irrationality sequence?
-/
@[category research open, AMS 11]
theorem erdos_264.parts.ii : answer(sorry) ↔ IsIrrationalitySequence Nat.factorial := by sorry

/--
One example is $2^{2^n}$.
-/
@[category research solved, AMS 11]
theorem erdos_264.variants.example : IsIrrationalitySequence (fun n ↦ 2 ^ (2 ^ n)) := by sorry

/--
Kovač and Tao [KoTa24] generally proved that any strictly increasing sequence of positive integers
$a_n$ such that $\sum \frac{1}{a_n}$ converges and
$$
  \liminf_{n \to \infty} (a_n^2 \sum_{k > n} \frac{1}{a_k^2}) > 0
$$
is not an irrationality sequence.

[KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series. arXiv:2406.17593 (2024).
-/
@[category research solved, AMS 11]
theorem erdos_264.variants.ko_tao_neg {a : ℕ → ℕ} (h₁ : StrictMono a) (h₂ : 0 ∉ Set.range a)
    (h₃ : Summable ((1 : ℝ) / a ·))
    (h₄ : 0 < atTop.liminf fun n ↦ a n ^ 2 * ∑' k : Set.Ioi n, (1 : ℝ) / a k ^ 2) :
    ¬IsIrrationalitySequence a := by
  sorry

/--
On the other hand, Kovač and Tao [KoTa24] do prove that for any function $F$ with
$\lim_{n \to \infty} \frac{F(n + 1)}{F(n)} = \infty$ there exists such an irrationality sequence with $a_n \sim F(n)$.

[KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series. arXiv:2406.17593 (2024).
-/
@[category research solved, AMS 11]
theorem erdos_264.variants.ko_tao_pos {F : ℕ → ℕ}
    (hF : atTop.Tendsto (fun n ↦ (F (n + 1) : ℝ) / F n) atTop) :
    ∃ a : ℕ → ℕ, IsIrrationalitySequence a ∧ (fun n ↦ (a n : ℝ)) ~[atTop] fun n ↦ (F n : ℝ) := by
  sorry

end Erdos264


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
