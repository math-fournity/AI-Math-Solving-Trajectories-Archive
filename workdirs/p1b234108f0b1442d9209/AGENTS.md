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
# First Proof, Theorem 4

*Reference:* [arxiv/2602.05192v2](https://arxiv.org/abs/2602.05192v2)
**First Proof**
by *Mohammed Abouzaid, Andrew J. Blumberg, Martin Hairer, Joe Kileel, Tamara G. Kolda, Paul D. Nelson, Daniel Spielman, Nikhil Srivastava, Rachel Ward, Shmuel Weinberger, Lauren Williams*
-/

open Polynomial Finset ENNReal
open scoped Nat


namespace Arxiv.«2602.05192»

variable {F : Type} [Field F]

/--
Define $p \boxplus_n q(x)$ to be the polynomial
$$
(p \boxplus_n q)(x) = \sum_{k=0}^n c_k x^{n-k}
$$
where the coefficients $c_k$ are given by the formula:
$$
c_k = \sum_{i+j=k} \frac{(n-i)! (n-j)!}{n! (n-k)!} a_i b_j
$$
for $k = 0, 1, \dots, n$.
 -/
noncomputable def finiteAdditiveConvolution (n : ℕ) (p q : F[X]) : F[X] :=
  let c := fun k => ∑ ij ∈ antidiagonal (k : ℕ),
      ((n - ij.1)! * (n - ij.2)! : F) / (n ! * (n - k)! : F) *
      p.coeff (n - ij.1) * q.coeff (n - ij.2)
  ∑ k ∈ range (n + 1), c k • X^(n - k)

local notation p " (⊞_"n ")" q:65  => finiteAdditiveConvolution n p q

@[category test, AMS 26]
theorem finiteAdditiveConvolution_comm (n : ℕ) (p q : F[X]) :
    p (⊞_n) q = q (⊞_n) p := by
  show ∑ a ∈_, _= ∑ a ∈_, _
  exact sum_congr rfl fun m hm =>
    (congr_arg₂ _) (sum_equiv (.prodComm _ _) (by simp [add_comm]) fun _ _ => by ring!) rfl

@[category test, AMS 26]
theorem finiteAdditiveConvolution_degree (n : ℕ) (p q : ℝ[X])
  (hp : p.degree = n) (hq : q.degree = n):
    (p (⊞_n) q).degree = n := by
  sorry

@[category test, AMS 26]
theorem finiteAdditiveConvolution_monic' (n : ℕ) (p q : ℝ[X]) (hn : 0 < n)
    (hp_deg : p.degree = n) (hq_deg : q.degree = n) (hp_monic : p.Monic) (hq_monic : q.Monic) :
    (p (⊞_n) q).Monic := by
  have hc0 : ∑ ij ∈ antidiagonal 0, ((n - ij.1)! * (n - ij.2)! : ℝ) / (n ! * (n - 0)! : ℝ) *
      p.coeff (n - ij.1) * q.coeff (n - ij.2) = 1 := by
    rw [antidiagonal_zero]
    simp
    have hp1 : p.coeff n = 1 := by
      have : p.natDegree = n := natDegree_eq_of_degree_eq_some hp_deg
      rw [← this]
      exact hp_monic
    have hq1 : q.coeff n = 1 := by
      have : q.natDegree = n := natDegree_eq_of_degree_eq_some hq_deg
      rw [← this]
      exact hq_monic
    rw [hp1, hq1]
    have h_ne : (n ! : ℝ) ≠ 0 := by positivity
    simp [h_ne]
  -- The polynomial is ∑ k ∈ range (n+1), c(k) • X^(n-k).
  -- Show coeff n equals 1 (from the k=0 term) and natDegree ≤ n.
  set r := p (⊞_n) q
  suffices h : r.coeff n = 1 ∧ r.natDegree ≤ n by
    rw [Polynomial.Monic, Polynomial.leadingCoeff]
    rcases Nat.eq_or_lt_of_le h.2 with heq | hlt
    · rw [heq]; exact h.1
    · exfalso; rw [Polynomial.coeff_eq_zero_of_natDegree_lt hlt] at h; linarith [h.1]
  constructor
  · -- coeff n of (∑ k ∈ range (n+1), c(k) • X^(n-k)) = c(0) = 1
    change (finiteAdditiveConvolution n p q).coeff n = 1
    simp only [finiteAdditiveConvolution]
    rw [Polynomial.finset_sum_coeff]
    conv_lhs =>
      arg 2; ext k
      rw [Polynomial.coeff_smul, Polynomial.coeff_X_pow]
    simp only [smul_eq_mul]
    -- Now: ∑ k ∈ range (n+1), c(k) * if n = n - k then 1 else 0
    -- Only k=0 contributes (since n = n - k ↔ k = 0 for k ≤ n)
    rw [Finset.sum_eq_single 0]
    · -- The k=0 term: simplify n - 0 = n, if-cond = true, then use hc0
      simp only [Nat.sub_zero, ite_true, mul_one]
      exact hc0
    · -- All other terms are 0
      intro k _ hk0
      have : n ≠ n - k := by omega
      simp [this]
    · -- 0 ∈ range (n+1)
      intro h; exact absurd (Finset.mem_range.mpr (by omega)) h
  · -- natDegree ≤ n: each term has degree ≤ n since n - k ≤ n
    change (finiteAdditiveConvolution n p q).natDegree ≤ n
    simp only [finiteAdditiveConvolution]
    apply (Polynomial.natDegree_sum_le _ _).trans
    apply Finset.sup_le
    intro k hk
    apply (Polynomial.natDegree_smul_le _ _).trans
    exact (Polynomial.natDegree_X_pow_le (n - k)).trans (Nat.sub_le n k)

/--
For a monic polynomial $p(x)=\prod_{i\le n}(x- \lambda_i)$, define
$$\Phi_n(p):=\sum_{i\le n}(\sum_{j\neq i} \frac1{\lambda_i-\lambda_j})^2$$
and $\Phi_n(p):=\infty$ if $p$ has a multiple root.
-/
noncomputable def Φ (p : ℝ[X]) : ℝ≥0∞ :=
  if p.roots.Nodup then
    let roots := p.roots.toFinset
    (∑ i ∈ roots, (∑ j ∈ roots.erase i, 1 / (i - j)) ^ 2).toNNReal
  else
    ⊤

/--
A predicate that holds if $p(x)$ and $q(x)$ are monic real-rooted polynomials of
degree $n$, then
$$\frac{1}{\Phi_n(p\boxplus_n q)} \ge \frac{1}{\Phi_n(

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
