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
import FormalConjectures.Wikipedia.LegendreConjecture

/-!
# Erdős Problem 375

*References:*
 - [erdosproblems.com/375](https://www.erdosproblems.com/375)
 - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
    theory. Monographies de L'Enseignement Mathematique (1980).
 - [RST75] Ramachandra, K. and Shorey, T. N. and Tijdeman, R., On Grimm's problem relating to
    factorisation of a block of consecutive integers. J. Reine Angew. Math. (1975), 109-124.
 -
-/

open Set Filter Topology Asymptotics

namespace Erdos375

/-- This is a proposition saying that for any `n ≥ 1` and any `k`, if `n + 1, ..., n + k` are all
composite, then there are distinct primes `p₁, ... pₖ` such that `pᵢ ∣ n + i` for all `1 ≤ i ≤ k`.
-/
def Erdos375Prop : Prop := ∀ n ≥ 1, ∀ k, (∀ i < k, ¬ (n + i + 1).Prime) →
    ∃ p : Fin k → ℕ, p.Injective ∧ ∀ i, (p i).Prime ∧ p i ∣ n + i + 1

/-- Is `Erdos375Prop` true? -/
@[category research open, AMS 11]
theorem erdos_375 : answer(sorry) ↔ Erdos375Prop := by
  sorry

/-- If `Erdos375Prop` is true, then `(n + 1).nth Prime - n.nth Prime < (n.nth Prime) ^ (1 / 2 - c)`
for some `c > 0`. -/
@[category research solved, AMS 11]
theorem erdos_375.variants.bounded_gap : Erdos375Prop →
    ∃ c > 0, ∀ᶠ n in atTop, (n + 1).nth Nat.Prime - n.nth Nat.Prime
    < (n.nth Nat.Prime : ℝ) ^ (1 / (2 : ℝ) - c) := by
  sorry

/-- In particular, if `Erdos375Prop` is true, then Legendre's conjecture is asymptotically true. -/
@[category research solved, AMS 11]
theorem erdos_375.variants.legendre : Erdos375Prop →
    (∀ᶠ n in atTop, ∃ p ∈ Set.Ioo (n ^ 2) ((n + 1) ^ 2), Nat.Prime p) :=
  fun hp => LegendreConjecture.bounded_gap_legendre (erdos_375.variants.bounded_gap hp)

/-- It is easy to see that for any `n ≥ 1` and `k ≤ 2`, if `n + 1, ..., n + k` are all composite,
then there are distinct primes `p₁, ... pₖ` such that `pᵢ ∣ n + i` for all `1 ≤ i ≤ k`. -/
@[category research solved, AMS 11]
theorem erdos_375.variants.le_two : ∀ n ≥ 1, ∀ k ≤ 2, (∀ i < k, ¬ (n + i + 1).Prime) →
    ∃ p : Fin k → ℕ, p.Injective ∧ ∀ i, (p i).Prime ∧ p i ∣ n + i + 1 := by
  intro n hn k hk
  interval_cases k <;> intro h
  · simp_all; intro; grind
  · choose! p hp using (n + 1).exists_prime_and_dvd (by linarith)
    exact ⟨fun x => p, fun x => by grind, fun i => by simpa using hp⟩
  · choose! p hp using (fun i : Fin 2 => (n + i + 1).exists_prime_and_dvd (by linarith))
    refine ⟨p, fun x y hxy => ?_, hp⟩
    by_contra! hr
    wlog hq : x < y
    · exact this n hn k hk h p hp y x hxy.symm hr.symm (by grind)
    · have hy : y = x + 1 := by grind
      have := hy ▸ Nat.dvd_sub (hp y).2 (hxy ▸ (hp x).2)
      have := (hp 1).1
      simp_all [Nat.not_prime_one]

/-- There exists a constant `c > 0` such that for all `n`, if
`k < c * (log n / (log (log n))) ^ 3 → (∀ i < k, ¬ (n + i + 1).Prime)`, then
there are distinct primes `p₁, ... pₖ` such that `pᵢ ∣ n + i` for all `1 ≤ i ≤ k`. This is proved
in [RST75]. There is no need to only consider sufficiently large `n` because one can always take
`c` small enough so that `k < c * (log n / (log (log n))) ^ 3` implies that `k = 0` until `n` is
large. -/
@[category research solved, AMS 11]
theorem erdos_375.variants.log : ∃ c > 0, ∀ n k : ℕ,
    k < c * (Real.log n / (Real.log (Real.log n))) ^ 3 → (∀ i < k, ¬ (n + i + 1).Prime) →
    ∃ p : Fin k → ℕ, p.Injective ∧ ∀ i, (p i).Prime ∧ p i ∣ n + i + 1 := by
  sorry

end Erdos375


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
