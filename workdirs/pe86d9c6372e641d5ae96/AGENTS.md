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
# Erdős Problem 700

*Reference:* [erdosproblems.com/700](https://www.erdosproblems.com/700)

A problem of Erdős and Szekeres [ErSz78].

*References:*
 * [ErSz78] Erdős, P. and Szekeres, G., _Some number theoretic problems on binomial coefficients_,
   Austral. Math. Soc. Gaz. (1978), 97-99.
 * [OEIS A091963](https://oeis.org/A091963)
 * Guy, R. K., _Unsolved Problems in Number Theory_, B31, B33.
-/

namespace Erdos700

open Finset

/-- `f n = min_{1 < k ≤ n/2} gcd(n, C(n,k))`. (The infimum is `0` when the range is empty, i.e.
`n < 4`.) -/
noncomputable def f (n : ℕ) : ℕ :=
  sInf {m | ∃ k, 1 < k ∧ k ≤ n / 2 ∧ m = Nat.gcd n (n.choose k)}

/-- `P n` is the largest prime factor of `n` (and `0` if `n ≤ 1`). -/
noncomputable def P (n : ℕ) : ℕ := n.primeFactors.sup id

/-- The set whose infimum defines `f`. -/
def fSet (n : ℕ) : Set ℕ := {m | ∃ k, 1 < k ∧ k ≤ n / 2 ∧ m = Nat.gcd n (n.choose k)}

/-- `f n` unfolds to the infimum of `fSet n`. -/
@[category API, AMS 11]
lemma f_eq (n : ℕ) : f n = sInf (fSet n) := rfl

/-- Each `gcd(n, C(n,k))` with `1 < k ≤ n/2` belongs to `fSet n`. -/
@[category API, AMS 11]
lemma f_mem (n k : ℕ) (h1 : 1 < k) (h2 : k ≤ n / 2) :
    Nat.gcd n (n.choose k) ∈ fSet n := ⟨k, h1, h2, rfl⟩

/-- `f n` is a lower bound: `f n ≤ gcd(n, C(n,k))` for every `1 < k ≤ n/2`. -/
@[category API, AMS 11]
lemma f_le (n k : ℕ) (h1 : 1 < k) (h2 : k ≤ n / 2) :
    f n ≤ Nat.gcd n (n.choose k) := Nat.sInf_le (f_mem n k h1 h2)

/-- Let $f(n) = \min_{1 < k \le n/2} \gcd(n, \binom{n}{k})$ and let $P(n)$ be the largest prime
dividing $n$.

**(a)** Characterise those composite $n$ such that $f(n) = n/P(n)$.

Erdős–Szekeres [ErSz78] note that $f(n) = n/P(n)$ when $n$ is a product of two primes
(`erdos_700.variants.prime_mul`), with $n = 30$ a further example. The characterisation itself is
open; we state it as the (unknown) predicate that is equivalent to being such an `n`. -/
@[category research open, AMS 11]
theorem erdos_700.parts.i (n : ℕ) (hn : ¬ n.Prime) (hn1 : 1 < n) :
    f n = n / P n ↔ answer(sorry) := by
  sorry

/-- Let $f(n) = \min_{1 < k \le n/2} \gcd(n, \binom{n}{k})$.

**(b)** Are there infinitely many composite $n$ such that $f(n) > n^{1/2}$?

Erdős–Szekeres [ErSz78] could not prove this. (Since $f(n) \ge p(n)$, the least prime factor of
$n$, there are infinitely many $n$ — those of the form $p^2$ — with $f(n) \ge n^{1/2}$; the
question asks for the strict inequality.) Here $f(n) > n^{1/2}$ is written as `(f n) ^ 2 > n`. -/
@[category research open, AMS 11]
theorem erdos_700.parts.ii :
    answer(sorry) ↔ {n : ℕ | ¬ n.Prime ∧ 1 < n ∧ (f n) ^ 2 > n}.Infinite := by
  sorry

/-- Let $f(n) = \min_{1 < k \le n/2} \gcd(n, \binom{n}{k})$.

**(c)** Is it true that, for every composite $n$, $f(n) \ll_A n/(\log n)^A$ for every $A > 0$?

Erdős–Szekeres [ErSz78] prove the weaker bound $f(n) \le (1 + o(1)) n/\log n$ (the case $A = 1$).
Here $f(n) \ll_A n/(\log n)^A$ is spelled out as: for every `A > 0` there is a constant `C`
(depending on `A`) with `f(n) ≤ C · n/(log n)^A` for every composite `n`. -/
@[category research open, AMS 11]
theorem erdos_700.parts.iii :
    answer(sorry) ↔ (∀ A : ℝ, 0 < A → ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, ¬ n.Prime → 1 < n →
      (f n : ℝ) ≤ C * (n : ℝ) / (Real.log n) ^ A) := by
  sorry

/- ## Proven partial results toward (a) -/

/-- Lucas (one step): for prime `P ∣ n`, if `P ∤ C(n,k)` then `P ∣ k`. -/
@[category API, AMS 11]
lemma prime_dvd_of_not_dvd_choose (P n k : ℕ) (hP : P.Prime) (hPn : P ∣ n)
    (h : ¬ P ∣ n.choose k) : P ∣ k := by
  haveI := Fact.mk hP
  by_contra hk
  apply h
  have hmod : n.choose k ≡ (n % P).choose (k % P) * (n / P).choose (k / P) [MOD P] :=
    Choose.choose_modEq_choose_mod_mul_choose_div_nat
  have hn0 : n % P = 0 := by
    have h := (Nat.modEq_zero_iff_dvd).2 hPn; simpa [Nat.ModEq, Nat.zero_mod] using h
  have hkP : 0 < k % P := Nat.pos_of_ne_zero (fun hh => hk (Nat.dvd_of_mod_eq_zero hh))
  rw [hn0, Nat.choose_eq_zero_of_lt hkP, zero_mul] at hmod
  exact (Nat.modEq_zero_iff_dvd).1 hmod

/-- `f(p^a) = p` for a prime `p` and `a ≥ 2` (recorded by Erdős–Szekeres [ErSz78]). In particular,
since `(p^a) / P(p^a) = p^{a-1}`, the prime power `p^a` is a "hit" (`f(n) = n / P(n)`) if and only
if `a = 2`. -/
@[category research solved, AMS 11]
theorem erdos_700.variants.prime_pow (p a : ℕ) (hp : p.Prime) (ha : 2 ≤ a) : f (p ^ a) = p := by
  have hp2 : 2 ≤ p := 

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
