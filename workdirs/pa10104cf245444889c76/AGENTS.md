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
# Erdős Problem 11

*Reference:* [erdosproblems.com/11](https://www.erdosproblems.com/11)
-/

namespace Erdos11

/--
Is every odd $n > 1$ the sum of a squarefree number and a power of 2?
-/
@[category research open, AMS 11]
theorem erdos_11 (n : ℕ) (hn : Odd n) (hn' : 1 < n) :
    ∃ k l : ℕ, Squarefree k ∧ n = k + 2 ^ l := by
  sorry

/--
Erdős often asked this under the weaker assumption that $n > 1$
is not divisible by 4.
-/
@[category research open, AMS 11]
theorem erdos_11.variants.not_four_dvd (n : ℕ) (hn : ¬ 4 ∣ n) (hn' : 1 < n) :
    ∃ k l : ℕ , Squarefree k ∧ n = k + 2^l := by
  sorry

/--
Is every odd $n > 1$ the sum of a squarefree number and two powers of 2?
-/
@[category research open, AMS 11]
theorem erdos_11.variants.two_pow_two (n : ℕ) (hn : Odd n) (hn' : 1 < n) :
    ∃ k l m : ℕ , Squarefree k ∧ n = k + 2^l + 2^m := by
  sorry

/--
Every odd $1 < n < 10^7$ is the sum of a squarefree number and a power of 2.
-/
@[category research solved, AMS 11]
theorem erdos_11.variants.finite_bound1 (n : ℕ) (hn : Odd n) (h : n < 10^7) (hn' : 1 < n) :
    ∃ k l : ℕ , Squarefree k ∧ n = k + 2^l := by
  sorry

/--
Every odd $1 < n < 2^50$ is the sum of a squarefree number and a power of 2.
-/
@[category research solved, AMS 11]
theorem erdos_11.variants.finite_bound2 (n : ℕ) (hn : Odd n) (h : n < 2^50) (hn' : 1 < n) :
    ∃ k l : ℕ , Squarefree k ∧ n = k + 2^l := by
  sorry

/--
Suppose that every odd $n$ is the sum of a squarefree number and a power of 2. Then the set of primes
$p$ such that $2 ^ p ≡ 2 \mod p ^ 2$ is infinite. This is Theorem 1 in [GrSo98].
[GrSo98] Granville, A. and Soundararajan, K., A Binary Additive Problem of Erdős and the Order of $2$ mod $p^2$. The Ramanujan Journal (1998), 283-298.
-/
@[category research solved, AMS 11]
theorem erdos_11.variants.granville_soundararajan (H : type_of% erdos_11) :
    {p : ℕ | p.Prime ∧ 2 ^ p ≡ 2 [MOD p ^ 2]}.Infinite := by
  sorry

end Erdos11


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
