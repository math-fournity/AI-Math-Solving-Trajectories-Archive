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
# Conjectures associated with A087719

Define $\varsigma(n)$ the smallest prime factor of $n$ (`Nat.minFac`). Let $a_n$ be the least
number such that the count of numbers $k \le a_n$ with $k > \varsigma(k)^n$ exceeds the count
of numbers with $k \le \varsigma(k)^n$.

The conjecture states that $a_n = 3^n + 3 \cdot 2^n + 6$ for $n \ge 1$.

*Reference:* [A87719](https://oeis.org/A87719)
-/

namespace OeisA87719

open Nat

/-- Count of numbers k in {1, ..., m} where k > (minFac k)^n. -/
def countExceeding (n m : ℕ) : ℕ :=
  (Finset.Icc 1 m).filter (fun k => k > k.minFac ^ n) |>.card

/-- Count of numbers k in {1, ..., m} where k ≤ (minFac k)^n. -/
def countNotExceeding (n m : ℕ) : ℕ :=
  (Finset.Icc 1 m).filter (fun k => k ≤ k.minFac ^ n) |>.card

/-- There exists m such that countExceeding n m > countNotExceeding n m. -/
@[category textbook, AMS 11]
theorem a_exists (n : ℕ) : ∃ m, countExceeding n m > countNotExceeding n m := by
    sorry

/-- The sequence a(n): least m such that countExceeding n m > countNotExceeding n m. -/
noncomputable def a (n : ℕ) : ℕ :=
  Nat.find (a_exists n)

/-- a(1) = 15. -/
@[category test, AMS 11]
theorem a_1 : a 1 = 15 := by
  rw [a, Nat.find_eq_iff]
  refine ⟨by decide +native, ?_⟩
  intro m hm
  interval_cases m <;> decide +native

/-- a(2) = 27. -/
@[category test, AMS 11]
theorem a_2 : a 2 = 27 := by
  rw [a, Nat.find_eq_iff]
  refine ⟨by decide +native, ?_⟩
  intro m hm
  interval_cases m <;> decide +native

/-- a(3) = 57. -/
@[category test, AMS 11]
theorem a_3 : a 3 = 57 := by
  rw [a, Nat.find_eq_iff]
  refine ⟨by decide +native, ?_⟩
  intro m hm
  interval_cases m <;> decide +native

/-- We have the following formula: $a(n) = 3^n + 3 * 2^n + 6$ for $n \geq 1$. -/
@[category textbook, AMS 11, formal_proof using formal_conjectures at "https://github.com/google-deepmind/formal-conjectures/pull/1894/commits/7a286754f623759d69a3dd18f482c53c1d70959b"]
theorem a_formula {n : ℕ} (hn : n ≥ 1) : a n = 3 ^ n + 3 * 2 ^ n + 6 := by
  sorry

end OeisA87719


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
