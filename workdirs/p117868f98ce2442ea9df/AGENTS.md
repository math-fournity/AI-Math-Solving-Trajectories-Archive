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
# Selfridge's conjectures

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/John_Selfridge#Selfridge's_conjecture_about_primality_testing)
-/

namespace Selfridge

section PrimalityTesting

/-- A number `p` satisfies the *Selfridge condition* if
1. `p` is odd,
2. `p ≡ ± 2 (mod 5)`,
3. `2^(p-1) ≡ 1 (mod p)`
4. `(p+1).fib ≡ 0 (mod p)`


This is the condition that is tested in the PSW conjecture.
Note: this is non-standard terminology. -/
@[mk_iff]
structure IsSelfridge (p : ℕ) where
  is_odd : Odd p
  mod_5 : p ≡ 2 [MOD 5] ∨ p ≡ 3 [MOD 5]
  pow_2 : 2^(p-1) ≡ 1 [MOD p]
  fib : (p+1).fib ≡ 0 [MOD p]

/-- A number `p` satisfies the *Pseudo Selfridge condition* if
1. `p` is odd,
2. `p ≡ ± 1 (mod 5)`,
3. `2^(p-1) ≡ 1 (mod p)`
4. `(p-1).fib ≡ 0 (mod p)`


This is a variant of the condition that is tested in the PSW conjecture, and appears in the
wiki page mentioned above.

Note: this is non-standard terminology. -/
@[mk_iff]
structure IsPseudoSelfridge (p : ℕ) where
  is_odd : Odd p
  mod_5 : p ≡ 1 [MOD 5] ∨ p ≡ 4 [MOD 5]
  pow_2 : 2^(p-1) ≡ 1 [MOD p]
  fib : (p-1).fib ≡ 0 [MOD p]

/--
**PSW conjecture** (Selfridge's test)
Let $p$ be an odd number, with $p \equiv \pm 2 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
and $F_{p+1} \equiv 0 \pmod{p}$, then $p$ is a prime number.
-/
@[category research open, AMS 11]
theorem selfridge_conjecture (p : ℕ) (hp : IsSelfridge p) : p.Prime := by
  sorry

/--
Selfridge's test variant:
Let $p$ be an odd number, with $p \equiv \pm 1 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
and $F_{p-1} \equiv 0 \pmod{p}$, then $p$ is a prime number.

This test does not work.
-/
@[category textbook, AMS 11]
theorem selfridge_conjecture.variants.exist_pseudo_counterexample :
    ∃ n : ℕ, IsPseudoSelfridge n ∧ ¬ n.Prime := by
  use 6601
  refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_⟩ <;> decide +native

/--
Selfridge's test variant:
Let $p$ be an odd number, with $p \equiv \pm 1 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
and $F_{p-1} \equiv 0 \pmod{p}$, then $p$ is a prime number.

The number $6601$ is a conterexample to this test satisfying $6601 ≡ 1 \mod 5$
-/
@[category textbook, AMS 11]
theorem selfridge_conjecture.variants.pseudo_counterexample :
    IsPseudoSelfridge 6601 ∧ ¬ (6601).Prime ∧ 6601 ≡ 1 [MOD 5] := by
  refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_, ?_⟩ <;> decide +native

/--
Selfridge's test variant:
Let $p$ be an odd number, with $p \equiv \pm 1 \pmod{5}$, $2^{p-1} \equiv 1 \pmod{p}$
and $F_{p-1} \equiv 0 \pmod{p}$, then $p$ is a prime number.

The number $30889$ is a conterexample to this test satisfying $30889 ≡ - 1 \mod 5$
-/
@[category textbook, AMS 11]
theorem selfridge_conjecture.variants.pseudo_counterexample' :
    IsPseudoSelfridge 30889 ∧ ¬ (30889).Prime ∧ 30889 ≡ 4 [MOD 5] := by
  refine ⟨⟨?_, ?_, ?_, ?_⟩, ?_, ?_⟩ <;> decide +native

end PrimalityTesting

section FermatNumbers

/-
# Selfridge's conjectures about Fermat numbers
-/

/--
**OEIS A46052**
The number of distinct prime factors of nth Fermat number.
Known terms: 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5
-/
def fermatFactors (n : ℕ) : ℕ := n.fermatNumber.primeFactors.card

/--
Selfridge conjectured that the number of prime factors of the `n`-th Fermat number does not grow
monotonically in $n$.
-/
@[category research open, AMS 11]
theorem selfridge_seq_conjecture : ¬ Monotone fermatFactors := by
  sorry

/--
Selfridge conjectured that the number of prime factors of the `n`-th Fermat number does not grow
monotonically in $n$.

A sufficient condition for this conjecture to hold is that there exists a Fermat prime larger than
65537.
-/
@[category research solved, AMS 11]
theorem selfridge_seq_conjecture.variants.sufficient_condition (n : ℕ) (hn : Prime n.fermatNumber)
    (hn' : n ≥ 5) : type_of% selfridge_seq_conjecture := by
  intro hmono
  have hp : (n.fermatNumber).Prime := hn.nat_prime
  have h1 : fermatFactors n = 1 := by
    unfold fermatFactors
    rw [hp.primeFactors, Finset.card_singleton]
  have h5 : fermatFactors 5 = 2 := by native_decide
  have hle := hmono hn'
  rw [h1, h5] at hle
  omega

end FermatNumbers

end Selfridge


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
