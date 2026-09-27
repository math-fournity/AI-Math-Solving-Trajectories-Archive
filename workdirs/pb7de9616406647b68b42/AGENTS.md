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
# Conjectures about the Mandelbrot and Multibrot sets
This file adds three conjectures about the Mandelbrot and Multibrot sets:
- the *MLC conjecture*, stating that these sets are locally connected
- the *density of hyperbolicity* conjecture, stating that parameters with attracting cycles are
  dense in the Mandelbrot and Multibrot sets
- the conjecture that the boundaries of these sets have zero area.
The first two conjectures are related in that the former implies the latter.

*References:*
 - [Wikipedia](https://en.wikipedia.org/wiki/Mandelbrot_set#Local_connectivity)
 - [arxiv/math/9902155](https://arxiv.org/abs/math/9902155)
 - [mathoverflow/37229](https://mathoverflow.net/questions/37229/)
-/

open Topology Set Function Filter Bornology Metric MeasureTheory

namespace Mandelbrot

/-- The Multibrot set of power `n` is the set of all parameters `c : ℂ` for which `0` does not
escape to infinity under repeated application of `z ↦ z ^ n + c`. -/
def multibrotSet (n : ℕ) : Set ℂ :=
  {c | ¬ Tendsto (fun k ↦ (fun z ↦ z ^ n + c)^[k] 0) atTop (cobounded ℂ)}

/-- The Mandelbrot set is the special case of the multibrot set for n = 2. In other words, it is the
set of all parameters `c : ℂ` for which `0` does not escape to infinity under repeated application
of `z ↦ z ^ 2 + c`. -/
abbrev mandelbrotSet := multibrotSet 2

/-- The `multibrotSet n` is equivalently the set of all parameters `c` for which the orbit of `0`
under `z ↦ z ^ n + c` does not leave the closed disk of radius `2 ^ (n - 1)⁻¹` around the origin. -/
@[category API, AMS 37]
theorem multibrotSet_eq {n : ℕ} (hn : 2 ≤ n) :
    multibrotSet n = {c | ∀ k, ‖(fun z ↦ z ^ n + c)^[k] 0‖ ≤ 2 ^ (n - 1 : ℝ)⁻¹} := by
  replace hn := one_lt_two.trans_le hn
  set r : ℝ := 2 ^ (n - 1 : ℝ)⁻¹
  have hr : 0 < r := by positivity
  have hr' : r ^ (n - 1) = 2 := by
    simp [r, ← Real.rpow_natCast, ← Real.rpow_mul two_pos.le, hn.le,
      show (n - 1 : ℝ) ≠ 0 by simpa [sub_ne_zero] using hn.ne.symm]
  have hr'' : r ^ n = 2 * r := by simp [← hr', ← pow_succ, hn.le]
  ext c; refine ⟨fun h k ↦ ?_, fun h h' ↦ ?_⟩ <;> dsimp [mandelbrotSet, multibrotSet] at h ⊢
  · refine of_not_not fun h' ↦ h ?_
    replace ⟨k, h, h'⟩ :
        ∃ k, r < ‖(fun z ↦ z ^ n + c)^[k] 0‖ ∧ ‖c‖ ≤ ‖(fun z ↦ z ^ n + c)^[k] 0‖ := by
      refine (le_or_gt ‖c‖ r).elim (fun h ↦ ⟨k, ?_, ?_⟩) fun h ↦ ⟨1, by
        simp [h, zero_pow (M₀ := ℂ) (one_pos.trans hn).ne.symm]⟩ <;> linarith
    let a := ‖(fun z ↦ z ^ n + c)^[k] 0‖ - r
    have ha : 0 < a := by unfold a; linarith
    have h' m : r + a * n ^ m ≤ ‖(fun z ↦ z ^ n + c)^[k + m] 0‖ := by
      induction' m with m hm
      · simp [a]
      · rw [← add_assoc, iterate_succ_apply']
        refine .trans ?_ <| norm_sub_le_norm_add _ _
        replace hm :
            r ^ n + a * n ^ m * r ^ (n - 1) * ↑n ≤ ‖(fun z ↦ z ^ n + c)^[k + m] 0‖ ^ n := by
          grw [← hm]
          cases n
          · simp
          rw [add_comm r _, add_pow]
          refine .trans ?_ <| Finset.add_le_sum (by intros; positivity) ?_ ?_ zero_ne_one <;> simp
        rw [norm_pow, pow_succ]
        grw [← hm, h']
        rw [hr', hr'', show ‖(fun z ↦ z ^ n + c)^[k] 0‖ = a + r by simp [a]]
        suffices a ≤ a * (n * n ^ m) by linarith
        rw [le_mul_iff_one_le_right ha]
        have hn : 1 ≤ (n : ℝ) := Nat.one_le_cast.2 hn.le
        simpa using mul_le_mul hn (one_le_pow₀ hn)
    rw [← tendsto_norm_atTop_iff_cobounded]
    suffices h' : Tendsto (fun m ↦ ‖(fun z ↦ z ^ n + c)^[k + m] 0‖) atTop atTop by
      rw [tendsto_atTop_atTop] at h' ⊢
      intro x; let ⟨l, h'⟩ := h' x
      refine ⟨k + l, fun m hm ↦ ?_⟩
      specialize h' (m - k) (Nat.le_sub_of_add_le' hm)
      rwa [Nat.add_sub_cancel' <| (Nat.le_add_right _ _).trans hm] at h'
    exact tendsto_atTop_mono h' <| tendsto_atTop_add_const_left _ _ <| .const_mul_atTop ha <|
      tendsto_pow_atTop_atTop_of_one_lt <| Nat.one_lt_cast.2 hn
  · specialize h' (isBounded_closedBall (x := 0) (r := r))
    rw [mem_map, mem_atTop_sets] at h'; replace ⟨n, h'⟩ := h'
    exact not_lt_of_ge (h n) (by simpa using h' n)

/-- The mandelbrot set is equivalently the set of all parameters `c` for which the orbit of `0`
under `z ↦ z ^ 2 + c` does not leave the closed disk of radius two around the origin. -/
@[category API, AMS 37]
theorem mandelbrotSet_eq : mandelbrotSet = {c | ∀ k, ‖(fun z ↦ z ^ 2 + c)^[k] 0‖ ≤ 2} := by
  simpa [show (2 - 1 :

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
