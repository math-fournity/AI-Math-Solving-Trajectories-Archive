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
# Pollock's (tetrahedral numbers) conjecture

Every positive integer is the sum of at most 5 tetrahedral numbers.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Pollock%27s_conjectures)
- [A797](https://oeis.org/A797)
- L. E. Dickson, *History of the Theory of Numbers, Vol. II: Diophantine Analysis*, Dover (2005), pp. 22–23
- Frederick Pollock, *On the extension of the principle of Fermat's theorem on the polygonal numbers to the higher order of series whose ultimate differences are constant*, Abstracts of the Papers Communicated to the Royal Society of London **5** (1850), 922–924
- H. E. Salzer and N. Levine, *Table of integers not exceeding 100000 that are not expressible as the sum of four tetrahedral numbers*, Math. Comp. **12** (1958), 141–144
- [MathWorld: Pollock's Conjecture](https://mathworld.wolfram.com/PollocksConjecture.html)
-/

namespace PollocksConjecture

open scoped BigOperators

/-  ## Definitions -/

/-- The $n$-th tetrahedral number: $T_n = \frac{n(n+1)(n+2)}{6}$. -/
def tetrahedral (n : ℕ) : ℕ :=
  n * (n + 1) * (n + 2) / 6

/-  ## Auxiliary definition -/

/-- The set of natural numbers that are **not** a sum of $4$ tetrahedral numbers. -/
def NotSumOfFourTetrahedral : Set ℕ :=
  {N : ℕ | ∀ f : Fin 4 → ℕ, N ≠ ∑ i, tetrahedral (f i)}

/-  ## Statements -/

/--
Pollock's (tetrahedral numbers) conjecture:
every integer is the sum of at most $5$ tetrahedral numbers.
-/
@[category research open, AMS 11]
theorem pollock_tetrahedral (N : ℕ) :
    ∃ f : Fin 5 → ℕ, N = ∑ i, tetrahedral (f i) := by
  sorry

/--
Salzer–Levine strengthening (as stated on Wikipedia/OEIS):
there are exactly $241$ integers that are not a sum of $4$ tetrahedral numbers, and the largest is $343867$.
-/
@[category research open, AMS 11]
theorem pollock_tetrahedral.salzer_levine :
    IsGreatest NotSumOfFourTetrahedral 343867 := by
  sorry

/-- As stated on Wikipedia/OEIS (A797), the set of exceptions has cardinality $241$. -/
@[category textbook, AMS 11]
theorem pollock_tetrahedral.ncard_exceptions :
    type_of% pollock_tetrahedral.salzer_levine ↔
    NotSumOfFourTetrahedral.ncard = 241 := by
  sorry

end PollocksConjecture


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
