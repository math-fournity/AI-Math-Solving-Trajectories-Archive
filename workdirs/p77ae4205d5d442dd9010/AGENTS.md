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
# Erdős Problem 1148

*References:*
- [erdosproblems.com/1148](https://www.erdosproblems.com/1148)
- [Ch26] P. Chojecki, [Bounded Representations by $x^2 + y^2 - z^2$](https://www.ulam.ai/research/erdos1148-full.pdf) (2026)
- [Va99] Various, Some of Paul's favorite problems. Booklet produced for the conference "Paul Erdős
  and his mathematics", Budapest, July 1999 (1999).
-/

open Filter

namespace Erdos1148

/--
A natural number $n$ which can be written as $n$ if $n = x^2 + y^2 - z^2$ with $\max(x^2, y^2, z^2)
\leq n$.
-/
def Erdos1148Prop (n : ℕ) : Prop :=
  ∃ x y z : ℕ, n = x ^ 2 + y ^ 2 - z ^ 2 ∧ x ^ 2 ≤ n ∧ y ^ 2 ≤ n ∧ z ^ 2 ≤ n

/--
Can every large integer $n$ be written as $n=x^2+y^2-z^2$ with $\max(x^2,y^2,z^2)\leq n$?

This was proved affirmatively by Chojecki [Ch26], using a Duke-type equidistribution theorem.
A Lean formalisation of the reduction (conditional on a Duke-type equidistribution theorem) exists;
see the [forum discussion](https://www.erdosproblems.com/forum/thread/1148#post-4849).
-/
@[category research solved, AMS 11]
theorem erdos_1148 : answer(True) ↔ ∀ᶠ n in atTop, Erdos1148Prop n := by
  sorry

/--
The largest integer known which cannot be written this way is $6563$.
-/
private instance (n : ℕ) : Decidable (Erdos1148Prop n) :=
  decidable_of_iff
    (∃ x ∈ Finset.range (Nat.sqrt n + 1), ∃ y ∈ Finset.range (Nat.sqrt n + 1),
      ∃ z ∈ Finset.range (Nat.sqrt n + 1),
      n = x ^ 2 + y ^ 2 - z ^ 2 ∧ x ^ 2 ≤ n ∧ y ^ 2 ≤ n ∧ z ^ 2 ≤ n)
    (by
      constructor
      · rintro ⟨x, -, y, -, z, -, h⟩; exact ⟨x, y, z, h⟩
      · rintro ⟨x, y, z, h1, h2, h3, h4⟩
        refine ⟨x, Finset.mem_range.mpr ?_, y, Finset.mem_range.mpr ?_,
                z, Finset.mem_range.mpr ?_, h1, h2, h3, h4⟩
        all_goals (simp only [Nat.lt_succ_iff]; exact Nat.le_sqrt'.mpr ‹_›))

/--
The integer $6563$ cannot be written as $x^2 + y^2 - z^2$ with $\max(x^2, y^2, z^2) \leq 6563$.
-/
@[category textbook, AMS 11]
theorem erdos_1148.variants.lower_bound : ¬ Erdos1148Prop 6563 := by
  decide +native

/--
The weaker property: $n = x^2 + y^2 - z^2$ such that $\max(x^2, y^2, z^2) \leq n + 2\sqrt{n}$.
-/
def erdos_1148_weaker_prop (n : ℕ) : Prop :=
  ∃ x y z : ℕ, n = x ^ 2 + y ^ 2 - z ^ 2 ∧
    (x ^ 2 : ℝ) ≤ n + 2 * Real.sqrt n ∧
    (y ^ 2 : ℝ) ≤ n + 2 * Real.sqrt n ∧
    (z ^ 2 : ℝ) ≤ n + 2 * Real.sqrt n

/--
[Va99] reports this is 'obvious' if we replace $\leq n$ with $\leq n+2\sqrt{n}$.
-/
@[category research solved, AMS 11]
theorem erdos_1148.variants.weaker : ∀ n, erdos_1148_weaker_prop n := by
  sorry

end Erdos1148


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
