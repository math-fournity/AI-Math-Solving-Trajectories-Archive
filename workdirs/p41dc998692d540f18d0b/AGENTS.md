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
# Erdős Problem 364

*Reference:* [erdosproblems.com/364](https://www.erdosproblems.com/364)
-/

open Nat

namespace Erdos364

/-- There is no consecutive triple of powerful numbers. -/
@[category research open, AMS 11]
theorem erdos_364 :
    ¬ ∃ (n : ℕ), Powerful n ∧ Powerful (n + 1) ∧ Powerful (n + 2) := by
  sorry

/--
Erdős [Er76d] conjectured a stronger statement: if $n_k$ is the $k$th powerful number,
then $n_{k+2} - n_k > n_k^c$ for some constant $c > 0$.

[Er76d] Erdős, P., Problems and results on number theoretic properties of consecutive integers and related questions. Proceedings of the Fifth Manitoba Conference on Numerical Mathematics (Univ. Manitoba, Winnipeg, Man., 1975) (1976), 25-44.
-/
@[category research open, AMS 11]
theorem erdos_364.variants.strong :
    ∃ (c : ℝ) (h : c > 0), ∀ (k : ℕ),
    Nat.nth Powerful (k + 2) - Nat.nth Powerful k > (Nat.nth Powerful k : ℝ) ^ c := by
  sorry

/--
There is no quadruple of powerful numbers, since at least one of the four numbers must be
$2 \pmod{4}$, which cannot be powerful (since $2$ divides it, but $2^2$ does not).
-/
@[category textbook, AMS 11]
theorem erdos_364.variants.weak :
    ¬ ∃ (n : ℕ), Powerful n ∧ Powerful (n + 1) ∧ Powerful (n + 2) ∧ Powerful (n + 3) := by
  intro h
  obtain ⟨n, hn⟩ := h
  have h2mod4 : n % 4 = 2 ∨ (n + 1) % 4 = 2 ∨ (n + 2) % 4 = 2 ∨ (n + 3) % 4 = 2 := by omega
  rcases h2mod4 with (_|_|_|_) <;>
  simp_all [not_full_of_prime_mod_prime_sq _ 1 (Nat.prime_two)]

end Erdos364


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
