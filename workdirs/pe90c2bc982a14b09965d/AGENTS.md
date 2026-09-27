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
# Erdős Problem 955

*References:*
- [erdosproblems.com/955](https://www.erdosproblems.com/955)
- [EGPS90] Erdős, P. and Granville, A. and Pomerance, C. and Spiro, C., On the normal behavior of
  the iterates of some arithmetic functions. Analytic number theory (Allerton Park, IL, 1989)
  (1990), 165-204.
- [Er73b] Erdős, P., Über die Zahlen der Form $\sigma(n) - n$ und $n - \phi(n)$. Elem. Math.
  (1973), 83--86.
- [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
- [PPT18] Pollack, Paul and Pomerance, Carl and Thompson, Lola, Divisor-sum fibers. Mathematika
  (2018), 330--342.
- [Po14b] Pollack, Paul, Some arithmetic properties of the sum of proper divisors and the sum of
  prime divisors. Illinois J. Math. (2014), 125--147.
- [Tr15] Troupe, Lee, On the number of prime factors of values of the sum-of-proper-divisors
  function. J. Number Theory (2015), 120--135.
- [Tr20] Troupe, Lee, Divisor sums representable as the sum of two squares. Proc. Amer. Math. Soc.
  (2020), 4189--4202.
-/

open Nat Filter
open scoped ArithmeticFunction ArithmeticFunction.sigma Topology

namespace Erdos955

/--
Let $s(n)=\sigma(n)-n=\sum_{\substack{d\mid n\\ d<n}}d$ be the sum of proper divisors function.
-/
def s (n : ℕ) : ℕ := σ 1 n - n

@[category test, AMS 11]
theorem s_one : s 1 = 0 := by decide

@[category test, AMS 11]
theorem s_two : s 2 = 1 := by decide

@[category test, AMS 11]
theorem s_six : s 6 = 6 := by decide

@[category test, AMS 11]
theorem s_twelve : s 12 = 16 := by decide

@[category test, AMS 11]
theorem s_twenty_eight : s 28 = 28 := by decide

/--
If $A\subset \mathbb{N}$ has density $0$ then $s^{-1}(A)$ must also have density $0$.

A conjecture of Erdős, Granville, Pomerance, and Spiro [EGPS90].
-/
@[category research open, AMS 11]
theorem erdos_955 :
    answer(sorry) ↔
      ∀ A : Set ℕ, A.HasDensity 0 → { x | s x ∈ A }.HasDensity 0 := by
  sorry

/--
It is possible for $s(A)$ to have positive density even if $A$ has zero density (for example
taking $A$ to be the product of two distinct primes).
-/
@[category research solved, AMS 11]
theorem erdos_955.variants.positive_density :
    ∃ A : Set ℕ, A.HasDensity 0 ∧ (∃ d > 0, (s '' A).HasDensity d) := by
  sorry

/--
Erdős [Er73b] proved that there are sets $A$ of positive density such that $s^{-1}(A)$ is empty.
-/
@[category research solved, AMS 11]
theorem erdos_955.variants.empty_preimage :
    ∃ A : Set ℕ, (∃ d > 0, A.HasDensity d) ∧ { x | s x ∈ A } = ∅ := by
  sorry

/--
Pollack [Po14b] has shown that this is true if $A$ is the set of primes.
-/
@[category research solved, AMS 11]
theorem erdos_955.variants.pollack_primes :
    { x | Nat.Prime (s x) }.HasDensity 0 := by
  sorry

/--
Troupe [Tr15] has shown that this is true if $A$ is the set of integers with unusually many prime
factors.
-/
@[category research solved, AMS 11]
theorem erdos_955.variants.troupe_unusually_many_prime_factors :
    ∀ ε > 0, { x | (1 + ε) * Real.log (Real.log (s x)) <
      (ArithmeticFunction.cardDistinctFactors (s x) : ℝ) }.HasDensity 0 := by
  sorry

/--
Troupe [Tr20] has also shown this is true if $A$ is the set of integers which are the sum of two
squares.
-/
@[category research solved, AMS 11]
theorem erdos_955.variants.troupe_sum_of_two_squares :
    { x | ∃ a b : ℕ, s x = a^2 + b^2 }.HasDensity 0 := by
  sorry

open scoped Classical in
/--
Pollack, Pomerance, and Thompson [PPT18] prove that if $\epsilon(x)=o(1)$ and $A\subset \mathbb{N}$
has size at most $x^{1/2+\epsilon(x)}$ then $\#\{ n\leq x: s(n)\in A\} =o(x)$ as $x\to \infty$. It
follows that (using $s(n)\ll n\log\log n$) if $A$ grows like
$\lvert A\cap [1,x]\rvert\leq x^{1/2+o(1)}$ then $s^{-1}(A)$ has density $0$.
-/
@[category research solved, AMS 11]
theorem erdos_955.variants.pollack_pomerance_thompson_bound :
    ∀ (A : Set ℕ) (ε : ℕ → ℝ),
      Tendsto ε atTop (𝓝 0) →
      (∀ᶠ n : ℕ in atTop, (count A n : ℝ) ≤ (n : ℝ) ^ ((1 / 2 : ℝ) + ε n)) →
      { x | s x ∈ A }.HasDensity 0 := by
  sorry

end Erdos955


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
