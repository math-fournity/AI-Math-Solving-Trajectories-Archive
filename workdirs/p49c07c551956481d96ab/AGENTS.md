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
# Erdős Problem 933

*References:*
- [erdosproblems.com/933](https://www.erdosproblems.com/933)
- [Er76d] Erdős, P, Problems and results on number theoretic properties of consecutive integers and
  related questions. Proceedings of the Fifth Manitoba Conference on Numerical Mathematics (Univ.
  Manitoba, Winnipeg, Man., 1975) (1976), 25-44.
-/

open Filter

namespace Erdos933

/-- The 2-adic valuation of $n(n+1)$. -/
def k (n : ℕ) : ℕ := padicValNat 2 (n * (n + 1))

/-- The 3-adic valuation of $n(n+1)$. -/
def l (n : ℕ) : ℕ := padicValNat 3 (n * (n + 1))

/--
If $n(n+1)=2^k3^lm$, where $(m,6)=1$, then is it true that
$\limsup_{n\to \infty} \frac{2^k3^l}{n\log n}=\infty$?
-/
@[category research open, AMS 11]
theorem erdos_933 :
    answer(sorry) ↔
      atTop.limsup (fun n : ℕ ↦
        ((((2 ^ k n * 3 ^ l n : ℕ) : ℝ) / ((n : ℝ) * Real.log (n : ℝ))) : EReal)) = ⊤ := by
  sorry

/--
Mahler proved (a more general result that implies in particular) that $2^k3^l<n^{1+o(1)}$.
-/
@[category research solved, AMS 11]
theorem erdos_933.variants.mahler :
    ∃ c : ℕ → ℝ, (c =o[atTop] (1 : ℕ → ℝ)) ∧
      ∀ᶠ n in atTop, ((2 ^ k n * 3 ^ l n : ℕ) : ℝ) < (n : ℝ) ^ (1 + c n) := by
  sorry

/--
Erdős [Er76d] wrote 'it is easy to see' that for infinitely many $n$, $2^k 3^l > n\log n$.

Steinerberger has noted a simple proof of this fact follows from taking $n=2^{3^r}$ for any
integer $r\geq 1$, when $k=3^r$ and $l=r+1$.
-/
@[category research solved, AMS 11]
theorem erdos_933.variants.lower_bound :
    Set.Infinite { n : ℕ | ((2 ^ k n * 3 ^ l n : ℕ) : ℝ) > (n : ℝ) * Real.log (n : ℝ) } := by
  -- Witness: n = 2^(3^(r+1)); k n = 3^(r+1), l n = r+2 by LTE, and 3 > log 2.
  refine Set.infinite_of_injective_forall_mem
    (f := fun r : ℕ ↦ 2 ^ (3 ^ (r + 1))) ?_ fun r ↦ ?_
  · exact (Nat.pow_right_injective (a := 2) (by norm_num)).comp
      ((Nat.pow_right_injective (a := 3) (by norm_num)).comp (add_left_injective 1))
  let m := 3 ^ (r + 1)
  have hk : k (2 ^ m) = m := by
    rw [k, padicValNat.mul (by positivity) (by positivity), padicValNat.prime_pow,
      padicValNat.eq_zero_of_not_dvd
        ((Even.pow_of_ne_zero (by norm_num) (by positivity)).add_one).not_two_dvd_nat, add_zero]
  have hl : l (2 ^ m) = r + 2 := by
    rw [l, padicValNat.mul (by positivity) (by positivity),
      padicValNat_prime_prime_pow (p := 3) (q := 2) m (by norm_num), zero_add]
    rw [show 2 ^ m + 1 = 2 ^ m + 1 ^ m by simp,
      padicValNat.pow_add_pow (p := 3) (x := 2) (y := 1) (by norm_num)
        (by norm_num) (by norm_num) (by simpa [m] using (by norm_num : Odd 3).pow)]
    simp [m, padicValNat.prime_pow]
    omega
  have hlog : (m : ℝ) * Real.log 2 < (3 : ℝ) ^ (r + 2) := by
    calc
      _ < (m : ℝ) * 3 := mul_lt_mul_of_pos_left (by linarith [Real.log_two_lt_d9]) (by positivity)
      _ = _ := by norm_num [m, pow_succ]
  change 2 ^ m ∈ {n | ((2 ^ k n * 3 ^ l n : ℕ) : ℝ) > (n : ℝ) * Real.log (n : ℝ)}
  simp only [Set.mem_setOf_eq, hk, hl]
  push_cast
  rw [Real.log_pow]
  exact mul_lt_mul_of_pos_left hlog (by positivity)

end Erdos933



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
