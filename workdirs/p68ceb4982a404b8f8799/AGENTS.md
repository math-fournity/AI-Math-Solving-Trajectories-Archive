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
import FormalConjectures.Wikipedia.Schinzel

/-!
# Erdős Problem 252

*References:*
 - [erdosproblems.com/252](https://www.erdosproblems.com/252)
 - [ErSt71] Erdös, P., and E. G. Straus. "Some number theoretic results." Pacific J. Math 36 (1971):
    635-646.
 - [ErSt74] Erdős, Paul, and Ernst Straus. "On the irrationality of certain series." Pacific journal
    of mathematics 55.1 (1974): 85-92.
 - [ErKa54] P. Erdős, M. Kac, Amer. Math. Monthly 61 (1954), Problem 4518.
 - [ScPu06] Schlage-Puchta, J. C., The irrationality of a number theoretical series. Ramanujan J.
    (2006), 455-460.
 - [FLC07] Friedlander, J. B. and Luca, F. and Stoiciu, M., On the irrationality of a divisor
    function series. Integers (2007).
 - [Pr22] Pratt, K., The irrationality of a divisor function series of Erdős and Kac.
    arXiv:2209.11124 (2022).
-/

open scoped Nat ArithmeticFunction.sigma

namespace Erdos252


/-- The series `∑ σ k n / n!`. -/
noncomputable def erdos_252_sum (k : ℕ) : ℝ := ∑' n, σ k n / (n ! : ℝ)

/-- Erdős Problem 252: irrationality of the sum for a given $k$. -/
@[category research open, AMS 11]
theorem erdos_252 :
    answer(sorry) ↔ ∀ k ≥ 1, Irrational (erdos_252_sum k) := by
  sorry

/-- `∑ σ 0 n / n!` is irrational. This is proved in [ErSt71]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.k_eq_zero : Irrational (erdos_252_sum 0) := by
  sorry

/-- `∑ σ 1 n / n!` is irrational. This is proved in [ErSt74]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.k_eq_one : Irrational (erdos_252_sum 1) := by
  sorry


/-- `∑ σ 2 n / n!` is irrational. This is proved in [ErKa54]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.k_eq_two : Irrational (erdos_252_sum 2) := by
  sorry

/-- `∑ σ 3 n / n!` is irrational. This is proved in [ScPu06] and [FLC07]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.k_eq_three : Irrational (erdos_252_sum 3) := by
  sorry

/-- `∑ σ 4 n / n!` is irrational. This is proved in [Pr22]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.k_eq_four : Irrational (erdos_252_sum 4) := by
  sorry

/-- For a fixed `k ≥ 5`, is `∑ σ k n / n!` irrational?. -/
@[category research open, AMS 11]
theorem erdos_252.variants.k_ge_five :
    answer(sorry) ↔ ∀ k ≥ 5, Irrational (erdos_252_sum k) := by
  sorry

/-- If Schinzel's conjecture is true, then `∑ σ k n / n!` is irrational for all `k`. This is proved
in [ScPu06]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.schinzel (hs : ∀ (fs : Finset (Polynomial ℤ)),
    (∀ f ∈ fs, BunyakovskyCondition f) → SchinzelCondition fs →
    Infinite ↑{n | ∀ f ∈ fs, Prime (Polynomial.eval (↑n) f).natAbs}) :
    ∀ k, Irrational (erdos_252_sum k) := by
  sorry

/-- If the prime `k`-tuples conjecture is true, then `∑ σ k n / n!` is irrational. This is proved
in [FLC07]. -/
@[category research solved, AMS 11]
theorem erdos_252.variants.prime_tuples {k : ℕ} (hk : 4 ≤ k) (hp : ∀ (a : Fin k → ℕ+)
    (b : Fin k → ℕ) (hab : ∀ p, p.Prime → ∃ n, ¬ p ∣ ∏ i, (a i * n + b i)),
    Set.Infinite {n | ∀ i : Fin k, (a i * n + b i).Prime} ) :
    Irrational (erdos_252_sum k) := by
  sorry

end Erdos252


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
