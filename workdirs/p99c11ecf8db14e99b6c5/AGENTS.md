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
# Erdős Problem 979

*Reference:* [erdosproblems.com/979](https://www.erdosproblems.com/979)
-/

namespace Erdos979

def solutionSet (n k : ℕ) : Set (Multiset ℕ) :=
  {P | P.card = k ∧ (∀ p ∈ P, Nat.Prime p) ∧ n = (P.map (. ^ k)).sum}

/--
Let $k ≥ 2$, and let $f_k(n)$ count the number of solutions to $n = p_1^k + \dots + p_k^k$,
where the $p_i$ are prime numbers. Is it true that $\limsup f_k(n) = \infty$?
-/
@[category research open, AMS 11]
theorem erdos_979 : answer(sorry) ↔
    ∀ k ≥ 2, Filter.limsup (fun n => (solutionSet n k).encard) Filter.atTop = ⊤ := by
  sorry

/--
Erdős [Er37b] proved that if $f_2(n)$ counts the number of solutions to $n = p_1^2 + p_2^2$, where $p_1$ and $p_2$ are prime numbers, then $\limsup f_2(n) = \infty$.

[Er37b] Erdős, Paul, On the Sum and Difference of Squares of Primes. J. London Math. Soc. (1937), 133--136.
-/
@[category research solved, AMS 11]
theorem erdos_979.variants.k2 :
    Filter.limsup (fun n => (solutionSet n 2).encard) Filter.atTop = ⊤ := by
  sorry

/--
Erdős (unpublished)
-/
@[category research solved, AMS 11]
theorem erdos_979.variants.k3 :
    Filter.limsup (fun n => (solutionSet n 3).encard) Filter.atTop = ⊤ := by
  sorry

end Erdos979


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
