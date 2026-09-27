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
# Erdős Problem 387

*References:*
 - [erdosproblems.com/387](https://www.erdosproblems.com/387)
 - [ErGr76b] Erdős, P. and Graham, R. L., *On the prime factors of
   ${n \choose k}$*. Fibonacci Quart. (1976), 348-352.
 - [Er78g] Erdős, Pál, *On prime factors of binomial coefficients. II*. Mat. Lapok
   (1978/82), 307-316.
 - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
   number theory*. Monographies de L'Enseignement Mathematique (1980).
 - [Sc58] Schinzel, A., *Sur un problème de P. Erdős*. Colloq. Math. (1958), 198-204.
 - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
 - [Fa66] Faulkner, M. "On a theorem of Sylvester and Schur." Journal of the London Mathematical
    Society 1.1 (1966): 107-110.
 - [BNPZ26] Bui, H., Naprienko, S., Pratt, K., and Zaharescu, A. Binomial coefficients with
    divisors avoiding an interval. arXiv:2605.21221 (2026).
-/

open Filter

namespace Erdos387

/--
Is there an absolute constant $c > 0$ such that, for all $1 \leq k < n$, the binomial coefficient
$\binom{n}{k}$ has a divisor in $(cn, n]$?

Bui, Naprienko, Pratt, and Zaharescu [BNPZ26] answered this negatively.
-/
@[category research solved, AMS 11]
theorem erdos_387 : answer(False) ↔ ∃ c : ℝ, 0 < c ∧ ∀ n k : ℕ, 1 ≤ k → k < n →
    ∃ d : ℕ, (d : ℝ) ∈ Set.Ioc (c * n) n ∧ d ∣ n.choose k := by
  sorry

@[category research solved, AMS 11]
example : ∀ i < 15, ¬ 99215 - i ∣ Nat.choose 99215 15 :=
  fun i hi => by interval_cases i <;> native_decide

/-- The following is Schinzel's conjecture, which appears in [Gu04]. -/
@[category research open, AMS 11]
theorem erdos_387.variants.schinzel : answer(sorry) ↔
    ∀ᶠ k in atTop, ¬ IsPrimePow k → ∃ n : ℕ, ∀ i < k, ¬ n - i ∣ n.choose k := by
  sorry

/-- It is easy to see that `n.choose k` has a divisor in `[n / k, n]`. -/
@[category research solved, AMS 11]
theorem erdos_387.variants.easy {n : ℕ} {k : ℕ} (hn : 1 ≤ n) (hk : k ≤ n) : ∃ d : ℕ,
    (d : ℝ) ∈ Set.Icc (n / k : ℝ) n ∧ d ∣ n.choose k := by
  by_cases k = 0 <;> simp_all
  refine ⟨(n.choose k).gcd n, ⟨?_, ?_⟩, gcd_dvd_left _ _⟩
  · rw [div_le_iff₀ (by positivity)]
    norm_cast
    rw [← Nat.gcd_mul_right]
    refine Nat.le_of_dvd ?_ (Nat.dvd_gcd ⟨(n - 1).choose (k - 1), ?_⟩ (dvd_mul_right _ _))
    · exact Nat.gcd_pos_of_pos_right _ (by positivity)
    · cases n <;> cases k <;> simp_all [Nat.add_one_mul_choose_eq]
  · exact Nat.le_of_dvd (by linarith) (gcd_dvd_right _ _)

/--
Is it true for any $c < 1$ and all $n$ sufficiently large, for all $1 \leq k < n$,
$\binom{n}{k}$ has a divisor in $(cn, n]$?

This variant appears in [Gu04]. Bui, Naprienko, Pratt, and Zaharescu [BNPZ26] answered it
negatively.
-/
@[category research solved, AMS 11]
theorem erdos_387.variants.guy : answer(False) ↔ ∀ c : ℝ, c < 1 → ∀ᶠ n : ℕ in atTop, ∀ k : ℕ, 1 ≤ k →
    k < n → ∃ d : ℕ, (d : ℝ) ∈ Set.Ioc (c * n) n ∧ d ∣ n.choose k := by
  sorry

end Erdos387


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
