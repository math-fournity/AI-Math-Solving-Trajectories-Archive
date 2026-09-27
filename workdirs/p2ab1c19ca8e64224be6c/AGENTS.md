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
# Infinite Regular Primes

We define the notion of regular primes, which are prime numbers that are coprime with the
cardinality of the class group of the `p`-th cyclotomic field. We also state that there are
infinitely many regular primes.

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Regular_prime)
-/

open scoped NumberField

variable (p : ℕ)

namespace RegularPrimes

/-- A natural prime number `p` is regular if `p` is coprime with the order of the class group
of the `p`-th cyclotomic field. -/
noncomputable def IsRegularPrime [Fact p.Prime] : Prop :=
  p.Coprime <| Fintype.card <| ClassGroup (𝓞 <| CyclotomicField p ℚ)

/-- The prime 37 is not a regular prime. -/
@[category textbook, AMS 11]
theorem not_isRegularPrime_37_first : ¬ @IsRegularPrime 37 (by decide) := by
  sorry

/-- The set of regular primes. -/
def regularPrimes : Set ℕ := { p | ∃ (hp : Nat.Prime p), @IsRegularPrime p ⟨hp⟩ }

/-- The set of irregular primes. -/
def irregularPrimes : Set ℕ := { p | ∃ (hp : Nat.Prime p), ¬ @IsRegularPrime p ⟨hp⟩ }

/-- The primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, and 31 are regular. -/
@[category textbook, AMS 11]
lemma small_regular_primes :
    { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 } ⊆ regularPrimes := by
  sorry

/-- The prime 37 is not a regular prime. -/
@[category textbook, AMS 11]
theorem not_isRegularPrime_37_second : ¬ @IsRegularPrime 37 (by decide) := by
  sorry

/-- An equivalent definition of a regular prime `p` is that it does not divide the numerator of the
first `p-3` Bernoulli numbers. Not in Mathlib. -/
@[category textbook, AMS 11]
theorem isRegularPrime_iff_Bernoulli (p : ℕ) [Fact p.Prime] :
    IsRegularPrime p ↔ ∀ k ∈ Finset.Icc 2 (p - 3), ¬ (p : ℤ) ∣ (bernoulli' k).num := by
  sorry

/-- The set of irregular primes is infinite. -/
@[category research solved, AMS 11]
theorem infinitude_of_irregularprimes : irregularPrimes.Infinite := by
  sorry

/-- Conjecture: The set of regular primes is infinite. -/
def RegularPrimeConjecture : Prop :=
  regularPrimes.Infinite

/-- Conjecture: The set of regular primes is infinite. -/
@[category research open, AMS 11]
theorem regularprime_conjecture : RegularPrimeConjecture := by
  sorry

end RegularPrimes


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
