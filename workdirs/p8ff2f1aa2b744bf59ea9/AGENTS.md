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
# Erdős Problem 257

*Reference:* [erdosproblems.com/257](https://www.erdosproblems.com/257)
-/

namespace Erdos257

/--
Let $A\subseteq\mathbb{N}$ be an infinite set. Is
$$
\sum_{n\in A} \frac{1}{2^n - 1}
$$
irrational?
-/
@[category research open, AMS 11]
theorem erdos_257 : answer(sorry) ↔ ∀ (A : Set ℕ), A.Infinite →
    Irrational (∑' n : A, (1 : ℝ) / (2 ^ n.1 - 1)) := by
  sorry

/--
Show that
$$
\sum_{n} \frac{1}{2^n - 1} = \sum_{n} \frac{d(n)}{2^n},
$$
where $d(n)$ is the number of divisors of $n$.
-/
@[category textbook, AMS 11]
theorem erdos_257.variants.tsum_top_eq :
    ∑' n, 1 / (2 ^ n - 1 : ℝ) = ∑' n, n.divisors.card / (2 ^ n : ℝ) := by
  have hr : ‖(1 / 2 : ℝ)‖ < 1 := by norm_num
  -- The key Lambert-series identity from Mathlib (`k = 0`):
  -- `∑' n:ℕ+, (1/2)^n / (1 - (1/2)^n) = ∑' n:ℕ+, σ 0 n * (1/2)^n`, with summands rewritten.
  have key := tsum_pow_div_one_sub_eq_tsum_sigma (𝕜 := ℝ) hr 0
  have hpos : ∀ n : ℕ, 0 < n → (2 : ℝ) ≤ 2 ^ n := fun n hn ↦ by
    simpa using pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 2) hn
  simp only [pow_zero, one_mul, ArithmeticFunction.sigma_zero_apply,
    show ∀ n : ℕ+, ((1 : ℝ) / 2) ^ (n : ℕ) / (1 - (1 / 2) ^ (n : ℕ))
        = 1 / (2 ^ (n : ℕ) - 1) from fun n ↦ by
      have h := hpos n n.2
      have hp : (0 : ℝ) < 2 ^ (n : ℕ) := by positivity
      have h1 : (1 : ℝ) / 2 ^ (n : ℕ) < 1 := (div_lt_one hp).2 (by linarith)
      rw [div_pow, one_pow, div_eq_div_iff (by linarith) (by linarith)]; field_simp,
    show ∀ n : ℕ+, ((n : ℕ).divisors.card : ℝ) * (1 / 2) ^ (n : ℕ)
        = (n : ℕ).divisors.card / 2 ^ (n : ℕ) from fun n ↦ by
      rw [div_pow, one_pow]; ring] at key
  -- Domination by geometric series gives `ℕ`-summability of both sides.
  have hsummL : Summable fun n : ℕ ↦ 1 / (2 ^ n - 1 : ℝ) :=
    .of_nonneg_of_le
      (fun n ↦ by have := one_le_pow₀ (one_le_two (α := ℝ)) (n := n); apply div_nonneg <;> linarith)
      (fun n ↦ by
        rcases Nat.eq_zero_or_pos n with h | h
        · simp [h]
        · have h2 := hpos n h
          rw [show (2 : ℝ) * (1 / 2) ^ n = 2 / 2 ^ n by rw [div_pow, one_pow]; ring,
            div_le_div_iff₀ (by linarith) (by positivity)]; nlinarith)
      ((summable_geometric_of_norm_lt_one hr).mul_left 2)
  have hsummR : Summable fun n : ℕ ↦ (n.divisors.card : ℝ) / (2 ^ n : ℝ) :=
    .of_nonneg_of_le (fun n ↦ by positivity)
      (fun n ↦ by
        rw [pow_one, show ((1 : ℝ) / 2) ^ n = 1 / 2 ^ n by rw [div_pow, one_pow], mul_one_div]
        gcongr; exact_mod_cast Nat.card_divisors_le_self n)
      (summable_pow_mul_geometric_of_norm_lt_one 1 hr)
  -- Bridge `ℕ+` to `ℕ`: the `n = 0` term is `0` on both sides.
  rw [← (tsum_zero_pnat_eq_tsum_nat hsummL), ← (tsum_zero_pnat_eq_tsum_nat hsummR)]
  simpa using key

/--
Show that
$$
\sum_{n} \frac{d(n)}{2^n}
$$
is irrational.

[Er48] Erdős, P., _On arithmetical properties of Lambert series_. J. Indian Math. Soc. (N.S.) (1948), 63-66.
-/
@[category research solved, AMS 11]
theorem erdos_257.variants.tsum_top :
    Irrational <| ∑' n, n.divisors.card / (2 ^ n : ℝ) := by
  sorry

end Erdos257


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
