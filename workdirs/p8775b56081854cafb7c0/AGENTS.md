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
# The Goormaghtigh conjecture

A repunit is a number whose digits in some base are all $1$. Here a nontrivial representation has
at least three digits. The Goormaghtigh conjecture says that $31$ and $8191$ are the only numbers
having nontrivial repunit representations in two different bases.

*References:*
* [Wikipedia](https://en.wikipedia.org/wiki/Goormaghtigh_conjecture)
* J. Grantham,
  [No new Goormaghtigh primes up to $10^{700}$](https://math.colgate.edu/~integers/y98/y98.pdf)
-/

namespace Goormaghtigh

/-- The repunit with `digits` digits in the given base, expressed without division. -/
def repunit (base digits : ℕ) : ℕ :=
  ∑ i ∈ Finset.range digits, base ^ i

/-- A number having repunit representations of at least three digits in two distinct bases. -/
def IsGoormaghtighNumber (N : ℕ) : Prop :=
  ∃ base₁ base₂ digits₁ digits₂ : ℕ,
    2 ≤ base₁ ∧ 2 ≤ base₂ ∧ base₁ ≠ base₂ ∧
      3 ≤ digits₁ ∧ 3 ≤ digits₂ ∧
        repunit base₁ digits₁ = N ∧ repunit base₂ digits₂ = N

/-- The only Goormaghtigh numbers are $31$ and $8191$. -/
@[category research open, AMS 11]
theorem goormaghtigh_conjecture (N : ℕ) (hN : IsGoormaghtighNumber N) :
    N = 31 ∨ N = 8191 := by
  sorry

/-- The number $31$ is a repunit in bases $2$ and $5$. -/
@[category test, AMS 11]
theorem isGoormaghtighNumber_31 : IsGoormaghtighNumber 31 := by
  refine ⟨2, 5, 5, 3, ?_⟩
  norm_num [repunit]

/-- The number $8191$ is a repunit in bases $2$ and $90$. -/
@[category test, AMS 11]
theorem isGoormaghtighNumber_8191 : IsGoormaghtighNumber 8191 := by
  refine ⟨2, 90, 13, 3, ?_⟩
  norm_num [repunit]

/-- Allowing two-digit repunits would make $13$ a representation in two distinct bases. -/
@[category test, AMS 11]
theorem repunit_two_digits : repunit 3 3 = 13 ∧ repunit 12 2 = 13 := by
  norm_num [repunit]

end Goormaghtigh


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
