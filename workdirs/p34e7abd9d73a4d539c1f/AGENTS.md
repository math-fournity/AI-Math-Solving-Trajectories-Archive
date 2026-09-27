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
# Conjectures about Mersenne primes

*References:*
- [Wikipedia: Mersenne conjectures](https://en.wikipedia.org/wiki/Mersenne_conjectures)
- [Wikipedia: Catalan's Mersenne conjecture](https://en.wikipedia.org/wiki/Catalan%27s_Mersenne_conjecture)
- [MathWorld: Catalan-Mersenne Number](https://mathworld.wolfram.com/Catalan-MersenneNumber.html)
-/

namespace Mersenne

namespace Nat

/--
A Wagstaff prime is a prime number of the form $(2^p+1)/3$.
-/
def GivesWagstaffPrime (p : ℕ) : Prop :=
  Odd p ∧ Nat.Prime ((2^p + 1) / 3)

/--
Holds when there is exists a number `k` such that $p = 2^k \\pm 1$ or $p = 4^k \\pm 3$.
-/
def IsSpecialForm (p : ℕ) : Prop :=
  ∃ k : ℕ, p = 2^k + 1 ∨ p = 2^k - 1 ∨ p = 4^k + 3 ∨ p = 4^k - 3

end Nat

open Mersenne

/--
The Catalan-Mersenne numbers, defined recursively by $c_0 = 2$ and
$c_{n+1} = 2^{c_n} - 1$.
-/
def catalanMersenne : ℕ → ℕ
  | 0 => 2
  | n + 1 => 2 ^ catalanMersenne n - 1

/--
A natural number `p` satisfies the statement of the New Mersenne Conjecture if whenever
two of the following conditions hold,
then all three must hold:
1. $2^p-1$ is prime
2. $(2^p+1)/3$ is prime
3. Exists a number `k` such that $p = 2^k \\pm 1$ or $p = 4^k \\pm 3$
-/
def NewMersenneConjectureStatement (p : ℕ) : Prop :=
  ((mersenne p).Prime ∧ p.GivesWagstaffPrime → p.IsSpecialForm) ∧
  ((mersenne p).Prime ∧ p.IsSpecialForm → p.GivesWagstaffPrime) ∧
  (p.GivesWagstaffPrime ∧ p.IsSpecialForm → (mersenne p).Prime)

/--
For any odd natural number `p` if two of the following conditions hold,
then all three must hold:
1. $2^p-1$ is prime
2. $(2^p+1)/3$ is prime
3. Exists a number `k` such that $p = 2^k \\pm 1$ or $p = 4^k \\pm 3$
-/
@[category research open, AMS 11]
theorem new_mersenne_conjecture (p : ℕ) (hp : Odd p) :
    NewMersenneConjectureStatement p := by
  sorry

/-- It suffices to check this conjecture for primes -/
@[category textbook, AMS 11]
theorem new_mersenne_conjecture_of_prime :
    (∀ p, p.Prime → NewMersenneConjectureStatement p) →
    ∀ p, Odd p → NewMersenneConjectureStatement p := by
  intro H p hp_odd
  by_cases hp_prime : p.Prime
  · exact H p hp_prime
  suffices ¬Nat.GivesWagstaffPrime p by
    have hF1 : ¬(mersenne p).Prime := fun h => hp_prime h.of_mersenne
    refine ⟨?_, ?_, ?_⟩ <;> grind
  rintro ⟨_, hP⟩
  by_cases hp1 : p = 1
  · grind
  set q := p.minFac
  have hq_dvd : q ∣ p := Nat.minFac_dvd p
  have hq_ne2 : q ≠ 2 := fun h =>
    Nat.not_even_iff_odd.mpr hp_odd (even_iff_two_dvd.mpr (h ▸ hq_dvd))
  have hq_odd : Odd q := (Nat.minFac_prime hp1).odd_of_ne_two hq_ne2
  obtain ⟨s, hs⟩ := hq_dvd
  have hs_odd : Odd s := (Nat.odd_mul.mp (hs ▸ hp_odd)).2
  have hpow_dvd : 2 ^ q + 1 ∣ 2 ^ p + 1 := by
    grind [one_pow, ← pow_mul, Odd.nat_add_dvd_pow_add_pow (x := 2 ^ q) (y := 1) hs_odd]
  have h3q : 3 ∣ 2 ^ q + 1 := by
    grind [Odd.nat_add_dvd_pow_add_pow (x := 2) (y := 1)]
  have h3p : 3 ∣ 2 ^ p + 1 := h3q.trans hpow_dvd
  obtain ⟨k, hk⟩ := hpow_dvd
  set d := (2 ^ q + 1) / 3 with hd
  have hd_dvd : d ∣ (2 ^ p + 1) / 3 := by
    use k
    grind [mul_comm, Nat.mul_div_assoc, mul_comm]
  have h8 : 8 ≤ 2 ^ q := by
    calc 8 = 2 ^ 3 := by norm_num
      _ ≤ 2 ^ q := Nat.pow_le_pow_right (by norm_num) (by grind [(Nat.minFac_prime hp1).two_le])
  have hd_lt : d < (2 ^ p + 1) / 3 := by
    have hpow : 2 ^ q < 2 ^ p := by
      apply Nat.pow_lt_pow_right <;> grind [Nat.not_prime_iff_minFac_lt]
    grind [Nat.mul_div_cancel_left]
  rcases hP.eq_one_or_self_of_dvd d hd_dvd with h | h <;> grind

/-- The New Mersenne Conjecture statement holds for odd primes. -/
@[category research open, AMS 11]
theorem new_mersenne_conjecture.variants.prime (p : ℕ) (hp : p.Prime) (h : Odd p) :
    NewMersenneConjectureStatement p := by
  sorry

/--
Are there infinitely many Mersenne primes?
-/
@[category research open, AMS 11]
theorem infinitely_many_mersenne_primes :
  answer(sorry) ↔ Set.Infinite { p : ℕ | (mersenne p).Prime } := by
    sorry

/--
The first five Catalan-Mersenne numbers $c_0, \ldots, c_4$ are known to be prime.
Catalan conjectured that they are prime "up to a certain limit".
Are all Catalan-Mersenne numbers $c_n$ with $n \geq 5$ prime?
-/
@[category research open, AMS 11]
theorem catalans_mersenne_conjecture :
    answer(sorry) ↔ ∀ n ≥ 5, Nat.Prime (catalanMersenne n) := by
  sorry

end Mersenne


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
