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
# Betrothed numbers

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Betrothed_numbers)
- [OEIS A005276](https://oeis.org/A005276)
-/

namespace BetrothedNumbers

open scoped ArithmeticFunction.sigma

/--
Two natural numbers $m$ and $n$ are **betrothed**  (or quasi-amicable) if $\sigma(m) = \sigma(n) = m + n + 1$,
where $\sigma$ is the sum-of-divisors function. Equivalently, the sum of the proper divisors
of $m$ equals $n + 1$, and the sum of the proper divisors of $n$ equals $m + 1$.
-/
@[mk_iff]
structure IsBetrothed (m n : ℕ) : Prop where
  left : σ 1 m = m + n + 1
  right : σ 1 n = m + n + 1

/-- The smallest known betrothed pair $(48, 75)$. -/
@[category test, AMS 11]
theorem betrothed_48_75 : IsBetrothed 48 75 := by
  constructor <;> decide

/-- `IsBetrothed` is symmetric. -/
@[category test, AMS 11]
theorem IsBetrothed.symm {m n : ℕ} (h : IsBetrothed m n) : IsBetrothed n m := by
  rw [isBetrothed_iff] at *
  omega

/--
**Same parity betrothed numbers conjecture.**
Do there exist betrothed numbers $(m, n)$ where both have the same parity
(both even or both odd)?

All known betrothed pairs consist of one even and one odd number.

-/
@[category research open, AMS 11]
theorem same_parity_betrothed :
    answer(sorry) ↔ ∃ m n : ℕ, IsBetrothed m n ∧ (Even m ↔ Even n) := by
  sorry

/--
**Infinitude of betrothed numbers conjecture.**
Are there infinitely many betrothed number pairs?

-/
@[category research open, AMS 11]
theorem infinitely_many_betrothed :
    answer(sorry) ↔ {p : ℕ × ℕ | p.1 < p.2 ∧ IsBetrothed p.1 p.2}.Infinite := by
  sorry

end BetrothedNumbers


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
