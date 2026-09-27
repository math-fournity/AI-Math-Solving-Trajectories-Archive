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
# Hilbert's 17th problem

Let $f(x_1, \dots, x_n)$ be a multivariable polynomial with real coefficients that takes only
nonnegative values for all real inputs.
Hilbert's 17th problem asks whether there exist rational functions $g_1, \dots, g_m$ such that
$f = g_1^2 + g_2^2 + \cdots + g_m^2$. Resolved affirmatively by Artin in 1927.
*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_seventeenth_problem)
- Motzkin, "The arithmetic-geometric inequality". In Shisha, Oved (ed.). Inequalities. Academic Press. pp. 205–224.
-/

open Real MvPolynomial

namespace Hilbert17

/--
Hilbert's 17th problem: every non-negative multivariate polynomial is a sum of
squares of rational functions.
-/
@[category research solved, AMS 12]
theorem hilbert_17th_problem {n : ℕ} (hn : 0 < n) (f : MvPolynomial (Fin n) ℝ)
    (h : ∀ x : Fin n → ℝ, 0 ≤ f.eval x) :
    ∃ (m : ℕ) (g : Fin m → MvRatFunc (Fin n) ℝ), algebraMap _ _ f = ∑ i, (g i) ^ 2 := by
  sorry

/--
The statement is false in general if we restrict to polynomials. The polynomial (by Motzkin)
$f(x, y) = x^4 y^2 + x^2 y^4 - 3 x^2 y^2 + 1$ takes only nonnegative values but cannot be
written as a sum of squares of polynomials.
-/
noncomputable def f : MvPolynomial (Fin 2) ℝ :=
  X 0 ^ 4 * X 1 ^ 2 + X 0 ^ 2 * X 1 ^ 4 - 3 * X 0 ^ 2 * X 1 ^ 2 + 1

-- Proof taken from `motzkin_polynomial_nonneg` in mathlib
/-- The Motzkin polynomial is non-negative everywhere. -/
@[category textbook, AMS 12]
theorem f_nonneg : ∀ x y : ℝ, 0 ≤ f.eval ![x, y] := by
  intro x y
  simp only [Nat.succ_eq_add_one, Nat.reduceAdd, f, Fin.isValue, map_add, map_sub, map_mul, map_pow,
    eval_X, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_fin_one, eval_ofNat, map_one]
  by_cases hx : x = 0
  · simp [hx]
  have h : 0 < (x ^ 2 + y ^ 2) ^ 2 := by positivity
  refine nonneg_of_mul_nonneg_left ?_ h
  have H : 0 ≤ (x ^ 3 * y + x * y ^ 3 - 2 * x * y) ^ 2 * (1 + x ^ 2 + y ^ 2)
    + (x ^ 2 - y ^ 2) ^ 2 := by positivity
  linear_combination H

/-- The Motzkin polynomial cannot be written as a sum of squares of polynomials. -/
@[category textbook, AMS 12]
theorem f_not_sum_of_squares :
    ¬∃ (n : ℕ) (hn : 0 < n) (S : Fin n → MvPolynomial (Fin 2) ℝ), f = ∑ i, S i ^ 2 := by
  sorry

/--
For the polynomial version, Hilbert showed that every nonnegative homogeneous polynomial in
$n$ variables of degree $2d$ can be written as a sum of squares of polynomials if and only if
- $n = 1$
- $n = 2$
- $d = 1$
- $(n, d) = (3, 2)$.
-/
def Hilbert17thProblemHomogenousPoly (n d : ℕ) : Prop :=
  ∀ f : MvPolynomial (Fin n) ℝ, f.IsHomogeneous (2 * d) →
    (∀ x : Fin n → ℝ, 0 ≤ f.eval x) →
      ∃ (m : ℕ) (g : Fin m → MvPolynomial (Fin n) ℝ), f = ∑ i, (g i) ^ 2

@[category test, AMS 12]
theorem Hilbert17thProblemHomogenousPoly_zero_left (d : ℕ) :
    Hilbert17thProblemHomogenousPoly 0 d := by
  refine fun f hf hf₀ ↦ ⟨1, fun _ ↦ C √(f.coeff 0), ?_⟩
  have hfd := hf.totalDegree
  rw [f.eq_C_of_isEmpty] at hf₀ ⊢
  rw [Finset.sum_congr rfl fun _ _ ↦ (map_pow _ _ _).symm, Real.sq_sqrt <| by simpa using hf₀]
  simp

@[category test, AMS 12]
theorem Hilbert17thProblemHomogenousPoly_zero_right (n : ℕ) :
    Hilbert17thProblemHomogenousPoly n 0 := by
  intro f hf hf₀
  rcases eq_or_ne f 0 with (rfl | hf_zero); · exact ⟨0, 0, by simp⟩
  have hfd := f.totalDegree_eq_zero_iff_eq_C.1 <| by simpa using hf.totalDegree hf_zero
  use 1, fun _ ↦ C √(f.coeff 0)
  rw [Finset.sum_congr rfl fun _ _ ↦ (map_pow _ _ _).symm, Real.sq_sqrt <| by simpa using hf₀ 0]
  simpa using hfd

/--
Hilbert's 17th problem for homogeneous polynomials: characterization of dimensions and degrees
where non-negative polynomials are sums of squares of polynomials.
-/
@[category research solved, AMS 12]
theorem hilbert_17th_problem_poly {n d : ℕ} (hn : 0 < n) (hd : 0 < d) :
    Hilbert17thProblemHomogenousPoly n d ↔ n = 1 ∨ n = 2 ∨ d = 1 ∨ n = 3 ∧ d = 2 := by
  sorry

end Hilbert17


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
