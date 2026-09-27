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
# Erdős Problem 1049

*References:*
- [erdosproblems.com/1049](https://www.erdosproblems.com/1049)
- [Er48] Erdős, P., On arithmetical properties of Lambert series. J. Indian Math. Soc. (N.S.)
  (1948), 63-66.
-/

namespace Erdos1049

open ArithmeticFunction Filter

/--
Let $t>1$ be a rational number. Is
$\sum_{n=1}^\infty\frac{1}{t^n-1}=\sum_{n=1}^\infty \frac{\tau(n)}{t^n}$ irrational, where
$\tau(n)$ counts the divisors of $n$?

A conjecture of Chowla.
-/
@[category research open, AMS 11]
theorem erdos_1049 :
    answer(sorry) ↔ ∀ t : ℚ, t > 1 → Irrational (∑' n : ℕ+, 1 / ((t : ℝ) ^ (n : ℕ) - 1)) := by
  sorry

/--
Erdős [Er48] proved that this is true if $t\geq 2$ is an integer.
-/
@[category research solved, AMS 11]
theorem erdos_1049.variants.geq_2_integer :
     ∀ t : ℤ, t ≥ 2 → Irrational (∑' n : ℕ+, 1 / ((t : ℝ) ^ (n : ℕ) - 1)) := by
  sorry

/--
Convergent case (`|t| > 1`).

Substitute `r := t⁻¹` so `‖r‖ < 1`, then apply Mathlib's series identity
`tsum_pow_div_one_sub_eq_tsum_sigma` at `k = 0`:
$$\sum_{n \ge 1} \frac{r^n}{1 - r^n} = \sum_{n \ge 1} \sigma_0(n) \cdot r^n.$$
After clearing denominators, both sides match the Lambert identity:
LHS becomes `1/(t^n - 1)` and RHS becomes `τ(n) / t^n`.
-/
@[category API, AMS 11]
private lemma lambert_convergent (t : ℝ) (ht : 1 < |t|) :
    ∑' n : ℕ+, 1 / (t ^ (n : ℕ) - 1) =
    ∑' n : ℕ+, ((n : ℕ).divisors.card : ℝ) / (t ^ (n : ℕ)) := by
  -- `|t| > 1` implies `t ≠ 0`, hence `t^n ≠ 0` for all n.
  have ht0 : t ≠ 0 := fun h => by subst h; simp at ht; linarith [abs_nonneg (0:ℝ)]
  have htn : ∀ n : ℕ, t ^ n ≠ 0 := fun n => pow_ne_zero n ht0
  -- Substitution `r := t⁻¹`, so `|r| < 1`.
  set r : ℝ := t⁻¹ with hr_def
  have hr_norm : ‖r‖ < 1 := by
    rw [Real.norm_eq_abs, hr_def, abs_inv]; exact inv_lt_one_of_one_lt₀ ht
  -- Apply the Mathlib identity. Now reduce each side of our goal to its form.
  have h := tsum_pow_div_one_sub_eq_tsum_sigma (k := 0) hr_norm
  convert h using 1
  -- LHS: show `1 / (t^n - 1) = r^n / (1 - r^n)`. After substituting `r = 1/t`,
  -- this is the algebraic identity `1/(t^n - 1) = (1/t^n) / (1 - 1/t^n)`,
  -- valid when `t^n ≠ 0` and `t^n ≠ 1`.
  · apply tsum_congr; intro n
    have hp : t ^ (n : ℕ) ≠ 0 := htn n
    have hrn : r ^ (n : ℕ) = (t ^ (n : ℕ))⁻¹ := by rw [hr_def, inv_pow]
    -- `t^n ≠ 1`: would imply `|t|^n = 1`, but `|t| > 1` gives `|t|^n > 1` since `n ≥ 1`.
    have hne1 : t ^ (n : ℕ) - 1 ≠ 0 := by
      intro hc
      have ht1 : t ^ (n : ℕ) = 1 := by linarith [sub_eq_zero.mp hc]
      have habs1 : |t| ^ (n : ℕ) = 1 := by rw [← abs_pow, ht1]; simp
      have hlt : 1 < |t| ^ (n : ℕ) := one_lt_pow₀ ht n.pos.ne'
      linarith
    rw [hrn]; field_simp
  -- RHS: `σ_0(n) · r^n = τ(n) / t^n` since `σ_0 = τ` and `r = 1/t`.
  · apply tsum_congr; intro n
    have hp : t ^ (n : ℕ) ≠ 0 := htn n
    have hrn : r ^ (n : ℕ) = (t ^ (n : ℕ))⁻¹ := by rw [hr_def, inv_pow]
    rw [hrn, ArithmeticFunction.sigma_zero_apply]; field_simp

/--
Divergent case (`|t| ≤ 1`).

Both `tsum`s equal `0` in this regime, but for different reasons in each
sub-case. We split on `t ∈ {1, 0, -1}` and the generic `|t| < 1, t ≠ 0`
remainder, and use the same `key` non-summability lemma below to handle
the cases where the series diverges.

- `t = 1`: every LHS term is `1 / (1 - 1) = 0` (Lean convention), so the
  LHS sum is trivially `0`. RHS is `Σ τ(n)`, non-summable.
- `t = 0`: every RHS term is `τ(n) / 0 = 0` (Lean convention), so the RHS
  sum is trivially `0`. LHS is `Σ (-1)`, non-summable.
- `t = -1`: alternating; LHS vanishes at even `n` but odd `n` give terms
  of magnitude `1/2`, an infinite set. RHS terms have magnitude `τ(n) ≥ 1`.
- `|t| < 1, t ≠ 0`: standard; bounded denominator gives lower-bounded
  reciprocal on LHS, and `|t^n| ≤ 1` plus `τ(n) ≥ 1` gives the RHS bound.

In every case, Lean's `tsum_eq_zero_of_not_summable` collapses the non-
summable side to `0`, matching the `0` on the other side.
-/
@[category API, AMS 11]
private lemma lambert_divergent (t : ℝ) (ht : |t| ≤ 1) :
    ∑' n : ℕ+, 1 / (t ^ (n : ℕ) - 1) =
    ∑' n : ℕ+, ((n : ℕ).divisors.card : ℝ) / (t ^ (n : ℕ)) := by
  -- `key`: a function with infinitely many terms bounded away from zero is
  -- not summable. Standard contrapositive of `Summable.tendsto_cofinite_zero`.
  have key : ∀ (f : ℕ+ → ℝ) (c : ℝ), 0 < c →
      Set.Infinite {n : ℕ+ | c ≤ |f n|} → ¬Summable f := by
    int

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
