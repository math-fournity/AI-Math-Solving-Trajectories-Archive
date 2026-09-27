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
# Erdős Problem 655

*Reference:* [erdosproblems.com/655](https://www.erdosproblems.com/655)
-/

open Filter Finset EuclideanGeometry

namespace Erdos655

/-- A collection $x_1, \dots, x_n\in\mathbb{R}^2$ is _valid_ if
no circle whose centre is one of the $x_i$ contains three other points. -/
def IsValid (X : Finset ℝ²) : Prop :=
  ∀ᵉ (x ∈ X) (r > 0), ¬3 ≤ (Metric.sphere x r ∩ X).ncard

/--
Let $x_1,\ldots,x_n\in \mathbb{R}^2$ be such that no circle whose centre is one
of the $x_i$ contains three other points. Are there at least
$$(1+c)\frac{n}{2}$$
distinct distances determined between the $x_i$, for some constant $c>0$ and
all $n$ sufficiently large?

The answer is **no**: as Zach Hunter observed, the regular `n`-gon (`n` points equally spaced on a
circle) is valid and determines only `⌊n/2⌋ < (1+c)n/2` distinct distances, for every `c > 0`.
(In the spirit of related conjectures of Erdős and others, presumably some kind of assumption that
the points are in general position was intended; see `erdos_655.variants.general_position`.)

The disproof — the regular `n`-gon construction together with its supporting lemmas — is formalised
at the linked commit. -/
@[category research solved, AMS 5 52, formal_proof using formal_conjectures at "https://github.com/AlperTheKing/formal-conjectures/blob/4aaaf544b6ed0ef22580787a8d8a19e85dc49556/FormalConjectures/ErdosProblems/655.lean"]
theorem erdos_655 :
    answer(False) ↔ ∃ c > (0 : ℝ), ∀ᶠ n in atTop, ∀ (X : Finset ℝ²), #X = n → IsValid X →
      (1 + c) * n / 2 ≤ distinctDistances X := by
  sorry

/-- Let $x_1,\ldots,x_n\in \mathbb{R}^2$ be such that no circle whose centre is one
of the $x_i$ contains three other points. Are there at least$$(1+c)\frac{n}{2}$$
distinct distances determined between the $x_i$, for some constant $c>0$ and
all $n$ sufficiently large?

In the spirit of related conjectures of Erdős and others, presumably
some kind of assumption that the points are in general position
(e.g. no three on a line and no four on a circle) was intended.-/
@[category research open, AMS 5 52]
theorem erdos_655.variants.general_position :
    answer(sorry) ↔ ∃ c > (0 : ℝ), ∀ᶠ n in atTop, ∀ (X : Finset ℝ²), #X = n → IsValid X →
      InGeneralPosition X → (1 + c) * n / 2 ≤ distinctDistances X := by
  sorry

end Erdos655


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
