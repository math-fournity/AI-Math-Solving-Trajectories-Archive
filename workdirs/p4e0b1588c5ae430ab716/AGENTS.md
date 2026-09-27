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
# Conjectures associated with A56777

A56777 lists composite numbers $n$ satisfying both $\varphi(n+12) = \varphi(n) + 12$ and
$\sigma(n+12) = \sigma(n) + 12$.

The conjectures state identities connecting A56777 and prime quadruples (A7530), as
well as congruences satisfied by the members of A56777.

*Reference:* [A56777](https://oeis.org/A56777)
-/

namespace OeisA56777

open Nat
open scoped ArithmeticFunction.sigma

/-- A composite number $n$ is in the sequence A56777 if it satisfies both
$\varphi(n+12) = \varphi(n) + 12$ and $\sigma(n+12) = \sigma(n) + 12$. -/
def A (n : ℕ) : Prop :=
  ¬n.Prime ∧ 1 < n ∧ totient (n + 12) = totient n + 12 ∧ σ 1 (n + 12) = σ 1 n + 12

/-- A number $n$ comes from a prime quadruple $(p, p+2, p+6, p+8)$ if
$n = p(p+8)$ for some prime $p$ where $p$, $p+2$, $p+6$, $p+8$ are all prime. -/
def ComesFromPrimeQuadruple (n : ℕ) : Prop :=
  ∃ p : ℕ, p.Prime ∧ (p + 2).Prime ∧ (p + 6).Prime ∧ (p + 8).Prime ∧ n = p * (p + 8)

/-- $65$ is in the sequence A56777. -/
@[category test, AMS 11]
theorem a_65 : A 65 := by
  refine ⟨?_, by norm_num, ?_, ?_⟩
  · simp only [show (65 : ℕ) = 5 * 13 by norm_num]
    exact not_prime_mul (by norm_num) (by norm_num)
  · decide
  · decide

/-- $209$ is in the sequence A56777. -/
@[category test, AMS 11]
theorem a_209 : A 209 := by
  unfold A
  simp only [one_lt_ofNat, reduceAdd, true_and]
  refine ⟨?_, ?_, ?_⟩
  · norm_num
  · have eq1 : 221 = 13 * 17 := by norm_num
    have eq2 : 209 = 11 * 19 := by norm_num
    rw [eq1, eq2, totient_mul (by norm_num), totient_mul (by norm_num),
      totient_prime (by norm_num), totient_prime (by norm_num), totient_prime (by norm_num),
      totient_prime (by norm_num)]
  · decide

/-- Numbers coming from prime quadruples are in the sequence A56777. -/
@[category textbook, AMS 11]
theorem a_of_comesFromPrimeQuadruple {n : ℕ} (h : ComesFromPrimeQuadruple n) : A n := by
  obtain ⟨p, hp, hp2, hp6, hp8, rfl⟩ := h
  -- n + 12 = p * (p+8) + 12 = (p+2) * (p+6)
  have hsum : p * (p + 8) + 12 = (p + 2) * (p + 6) := by ring
  -- coprimality facts between the four primes
  have hne_p_p8 : p ≠ p + 8 := by omega
  have hne_p2_p6 : p + 2 ≠ p + 6 := by omega
  have hcop1 : Nat.Coprime p (p + 8) := (Nat.coprime_primes hp hp8).mpr hne_p_p8
  have hcop2 : Nat.Coprime (p + 2) (p + 6) := (Nat.coprime_primes hp2 hp6).mpr hne_p2_p6
  refine ⟨?_, ?_, ?_, ?_⟩
  -- ¬ Prime (p * (p+8))
  · exact Nat.not_prime_mul hp.one_lt.ne' (by have := hp8.one_lt; omega)
  -- 1 < p * (p+8)
  · have h1 : 2 ≤ p := hp.two_le
    have h2 : 10 ≤ p + 8 := by omega
    nlinarith
  -- totient: φ((p+2)(p+6)) = φ(p(p+8)) + 12
  · rw [hsum, Nat.totient_mul hcop2, Nat.totient_mul hcop1,
        Nat.totient_prime hp, Nat.totient_prime hp2,
        Nat.totient_prime hp6, Nat.totient_prime hp8]
    zify [show 1 ≤ p from hp.one_lt.le, show 1 ≤ p + 2 by omega,
          show 1 ≤ p + 6 by omega, show 1 ≤ p + 8 by omega]
    ring
  -- sigma: σ₁((p+2)(p+6)) = σ₁(p(p+8)) + 12
  · rw [hsum, ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop2,
        ArithmeticFunction.isMultiplicative_sigma.map_mul_of_coprime hcop1]
    have e1 : ArithmeticFunction.sigma 1 p = p + 1 := by
      have := ArithmeticFunction.sigma_one_apply_prime_pow (p := p) (i := 1) hp
      simpa using this
    have e2 : ArithmeticFunction.sigma 1 (p + 2) = (p + 2) + 1 := by
      have := ArithmeticFunction.sigma_one_apply_prime_pow (p := p + 2) (i := 1) hp2
      simpa using this
    have e6 : ArithmeticFunction.sigma 1 (p + 6) = (p + 6) + 1 := by
      have := ArithmeticFunction.sigma_one_apply_prime_pow (p := p + 6) (i := 1) hp6
      simpa using this
    have e8 : ArithmeticFunction.sigma 1 (p + 8) = (p + 8) + 1 := by
      have := ArithmeticFunction.sigma_one_apply_prime_pow (p := p + 8) (i := 1) hp8
      simpa using this
    rw [e1, e2, e6, e8]
    ring

/-- All members of the sequence A56777 come from prime quadruples. -/
@[category research open, AMS 11]
theorem comesFromPrimeQuadruple_of_a {n : ℕ} (h : A n) : ComesFromPrimeQuadruple n := by
  sorry

/-- Numbers coming from prime quadruples satisfy $n \equiv 65 \pmod{72}$. -/
@[category textbook, AMS 11]
theorem mod_72_of_comesFromPrimeQuadruple {n : ℕ} (h : ComesFromPrimeQuadruple n) :
    n % 72 = 65 := by
  obtain ⟨p, hp, hp2, hp6, hp8, rfl⟩ := h
  have hp5 : 5 ≤ p := by
    by_contra hlt; push_neg at hlt
    interval_cases p <;> simp_

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
