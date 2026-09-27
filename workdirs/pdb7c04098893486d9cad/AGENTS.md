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
# Erdős Problem 851

*References:*
- [erdosproblems.com/851](https://www.erdosproblems.com/851)
- [Pr26] D. Price and GPT-5.2 Pro, [Erdős problem 851](https://www.overleaf.com/read/svgbjzpxxppv#4eea7e) (2026)
-/

namespace Erdos851

/--
`TwoPowAddSet r` is the set of integers of the form `2^k+n`, where `k ≥ 0` and `n` has at most `r`
prime divisors.
-/
def TwoPowAddSet (r : ℕ) := {(2 ^ k + n) | (k : ℕ) (n : ℕ) (_ : n.primeFactors.card ≤ r)}

/-- The set of integers of the form `2^k+p`, where `k ≥ 0` and `p` is prime. -/
def twoPowAddPrimeSet : Set ℕ := {(2 ^ k + p) | (k : ℕ) (p : ℕ) (_ : p.Prime)}

/--
The set of integers of the form `2^k+p` (where `p` is prime) has positive lower density.
-/
@[category research solved, AMS 11]
theorem erdos_851.variants.romanoff : 0 < Set.lowerDensity twoPowAddPrimeSet := by
  sorry

/--
Let $\epsilon > 0$. Is there some $r \ll_\epsilon 1$ such that the density of integers of the
form $2^k+n$, where $k \geq 0$ and $n$ has at most $r$ prime divisors, is at least $1-\epsilon$?

This was proved affirmatively by Price and GPT-5.2 Pro [Pr26].
-/
@[category research solved, AMS 11]
theorem erdos_851 (ε : ℝ) (hε : ε ∈ Set.Ioo 0 1) : ∃ r d,
    (TwoPowAddSet r).HasDensity d ∧ 1 - ε ≤ d := by
  sorry

end Erdos851


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
