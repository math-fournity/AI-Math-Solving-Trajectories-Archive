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
# Erdős Problem 828

*Reference:* [erdosproblems.com/828](https://www.erdosproblems.com/828)
-/

namespace Erdos828

open scoped Nat

/--
Is it true that, for any $a \in \mathbb{Z}$, there are infinitely many $n$ such that
$$\phi(n) | n + a$$?
-/
@[category research open, AMS 11]
theorem erdos_828 : answer(sorry) ↔ ∀ a : ℤ, Set.Infinite {n : ℕ | ↑(φ n) ∣ n + a} := by
  sorry

/--
When $n > 1$, Lehmer conjectured that $\phi(n) | n - 1$ if and only if $n$ is prime.
-/
@[category research open, AMS 11]
theorem erdos_828.variants.lehmer_conjecture : answer(sorry) ↔ ∀ n > 1, φ n ∣ n - 1 ↔ Prime n := by
  sorry

/--
It is an easy exercise to show that $\phi(n) | n$ if and only if $n = 0, 1$ or $n = 2^a 3^b$ for
some $a > 0$.
-/
@[category textbook, AMS 11, formal_proof using formal_conjectures at
"https://github.com/XC0R/formal-conjectures/blob/03e00cf8d44098d0fb06e891fca30c29769df619/FormalConjectures/ErdosProblems/828.lean#L49"]
theorem erdos_828.variants.phi_dvd_self_iff_pow2_pow3 {n : ℕ} :
    φ n ∣ n ↔ n ≤ 1 ∨ ∃ᵉ (a > 0) (b), n = 2 ^ a * 3 ^ b := by
  sorry

end Erdos828


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
