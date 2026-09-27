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
# Erdős Problem 358

*References:*
- [erdosproblems.com/358](https://www.erdosproblems.com/358)
- [Ta26] T. Tao, [Erdős problem 358](https://terrytao.wordpress.com/wp-content/uploads/2026/02/erdos-358-2.pdf) (2026)
-/

namespace Erdos358

open Filter Finset

/-
Let $a$ be an infinite sequence of integers. `intervalRepresentations A n` is the set of solutions
to $$n=\sum_{u\leq i\leq v}a_i.$$ where `u` and `v` are positive integers.
-/
def intervalRepresentations (A : ℕ → ℕ) (n : ℕ) : Set (ℕ × ℕ) :=
  {(u, v) | 0 < u ∧ 0 < v ∧ n = ∑ i ∈ Icc u v, A i}

/-
Let $a$ be an infinite sequence of integers. Let $f(n)$ count the number of
solutions to $$n=\sum_{u\leq i\leq v}a_i.$$
-/
noncomputable def f (A : ℕ → ℕ) (n : ℕ) : ℕ :=
  Nat.card (intervalRepresentations A n)

/-
Let $a$ be an infinite sequence of integers. `intervalRepresentationsNonTrivial A n` is the set of
solutions to $$n=\sum_{u\leq i\leq v}a_i$$ such that the sum has at least two terms.
-/
def intervalRepresentationsNonTrivial (A : ℕ → ℕ) (n : ℕ) : Set (ℕ × ℕ) :=
  {(u, v) | 0 < u ∧ 0 < v ∧ u < v ∧ n = ∑ i ∈ Icc u v, A i}

/-
Let $a$ be an infinite sequence of integers. Let $g(n)$ count the number of
solutions to $$n=\sum_{u\leq i\leq v}a_i.$$ such that the sum has at least two terms.
-/
noncomputable def g (A : ℕ → ℕ) (n : ℕ) : ℕ :=
  Nat.card (intervalRepresentationsNonTrivial A n)

/--
When $A_n = n$, the function $f$ defined above counts the number of odd divisors of $n$.
-/
@[category textbook, AMS 5 11]
theorem f_id : f id = fun n ↦ #{d ∈ n.divisors | Odd d} := by
  sorry

/--
Let $A=\{a_1 < \cdots\}$ be an infinite sequence of integers. Let $f(n)$ count the number of
solutions to $$n=\sum_{u\leq i\leq v}a_i.$$
Is there such an $A$ for which $f(n)\to \infty$ as $n\to \infty$?

Tao [Ta26] constructed such a sequence with $f(n) \gg \log n$ for all sufficiently large $n$.
-/
@[category research solved, AMS 5 11]
theorem erdos_358.parts.i :
    answer(True) ↔ ∃ A, StrictMono A ∧ atTop.Tendsto (f A) atTop := by
  sorry

/--
Let $A=\{a_1 < \cdots\}$ be an infinite sequence of integers. Let $f(n)$ count the number of
solutions to $$n=\sum_{u\leq i\leq v}a_i.$$
Is there an $A$ such that $f(n)\geq 2$ for all large $n$?

This also follows from Tao's construction with $f(n) \gg \log n$ [Ta26].
-/
@[category research solved, AMS 5 11]
theorem erdos_358.parts.ii :
    answer(True) ↔ ∃ A, StrictMono A ∧ ∀ᶠ n in atTop, 2 ≤ f A n := by
  sorry

/--
When $A =\{a_1 < \cdots\}$ corresponds to the set of primes, it is conjectured that the
$\limsup$ of the number of representations $$n=\sum_{u\leq i\leq v}a_i$$ is infinite.
-/
@[category research open, AMS 5 11]
theorem erdos_358.variants.prime_set :
    atTop.limsup (fun n ↦ (f (Nat.nth Nat.Prime) n : ℕ∞)) = ⊤ := by
  sorry

/--
When $A =\{a_1 < \cdots\}$ corresponds to the set of primes, it is conjectured that the set of
numbers $n$ that have representations $$n=\sum_{u\leq i\leq v}a_i$$ has positive upper density.
-/
@[category research open, AMS 5 11]
theorem erdos_358.variants.prime_set_density_representation :
    0 < {n : ℕ | intervalRepresentations (Nat.nth Nat.Prime) n |>.Nonempty}.upperDensity := by
  sorry

/--
It is conjectured that if $A =\{a_1 < \cdots\}$ and $g$ counts the number of representations
$$n=\sum_{u\leq i\leq v}a_i$$ such that the sum has at least two terms, then for all $n$ we have
$1 \leq g(n)$ for sufficiently large $n$.
-/
@[category research open, AMS 5 11]
theorem erdos_358.variants.one_le :
    ∃ A, StrictMono A ∧ ∀ᶠ n in atTop, 1 ≤ g A n := by
  sorry


end Erdos358


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
