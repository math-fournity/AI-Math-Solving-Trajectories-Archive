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
# Erdős Problem 939

*Reference:* [erdosproblems.com/939](https://www.erdosproblems.com/939)
-/
open Nat

namespace Erdos939

/--
A set `S` belongs to `Erdos939Sums r` if it meets the following criteria:
- The size of the set is `$|S| = r - 2$`.
- The elements of the set are coprime (their greatest common divisor is 1).
- Every element in `S` is an `$r$-powerful` number.
- The sum of the elements in `S`, i.e., `$\sum_{s \in S} s$`, is also an `$r$-powerful` number.
-/
def Erdos939Sums (r : ℕ) :=
    {S : Finset ℕ | S.card = r - 2 ∧ S.Coprime ∧ r.Full (∑ s ∈ S, s) ∧ ∀ s ∈ S, r.Full s}

/--
If $r≥4$ then can the sum of $r-2$ coprime $r$-powerful numbers ever be itself $r$-powerful?
-/
@[category research open, AMS 11]
theorem erdos_939 : answer(sorry) ↔ ∀ r ≥ 4, (Erdos939Sums r).Nonempty := by
  sorry

/--
If $r≥4$ are there infinitely many sums of $r-2$ coprime $r$-powerful numbers
that are themselves $r$-powerful?
-/
@[category research open, AMS 11]
theorem erdos_939.variants.infinite : answer(sorry) ↔ ∀ r ≥ 4, (Erdos939Sums r).Infinite := by
  sorry

/--
Are there infinitely many triples of coprime $3$-powerful numbers $a, b, c$ such that $a + b = c$?
-/
@[category research open, AMS 11]
theorem erdos_939.variants.triples :
    answer(sorry) ↔ {(a,b,c) | ({a, b, c} : Finset ℕ).Coprime ∧
      (3).Full a ∧ (3).Full b ∧ (3).Full c ∧
      a + b = c}.Infinite := by
  sorry

/--
Cambie has found several examples of the sum of $r - 2$ coprime $r$-powerful numbers being itself
$r$-powerful. For example when $r=5$ we have
$$3761^5=2^8\cdot3^{10}\cdot 5^7 + 2^{12}\cdot 23^6 + 11^5\cdot 13^5$$.
-/
@[category research solved, AMS 11]
theorem erdos_939.variants.examples : (∃ r ≥ 4, (Erdos939Sums r).Nonempty) := by
  use 5
  simp only [ge_iff_le, reduceLeDiff, true_and]
  unfold Erdos939Sums
  simp [Set.Nonempty]
  use {2^8 * 3^10 * 5^7, 2^12 * 23^6, 11^5 * 13^5}
  simp
  constructor
  · unfold Finset.Coprime
    aesop
  · norm_num [Nat.Full, Nat.primeFactors, Nat.primeFactorsList]


/-- Cambie has also found solutions when $r=7$. -/
@[category research solved, AMS 11]
theorem erdos_939.variants.seven : (Erdos939Sums 7).Nonempty := by
  sorry

/-- Cambie has also found solutions when $r=8$. -/
@[category research solved, AMS 11]
theorem erdos_939.variants.eight : (Erdos939Sums 8).Nonempty := by
  sorry

/--
Euler had conjectured that the sum of $k - 1$ many $k$-th powers is never a
$k$-th power, but this is false for $k=5$, as Lander and Parkin [LaPa67] found
$$27^5+84^5+110^5+133^5=144^5$$.

[LaPa67] Lander, L. J. and Parkin, T. R., "A counterexample to Euler's sum of powers conjecture."
  Math. Comp. (1967), 101--103.
-/
@[category research solved, AMS 11]
theorem erdos_939.variants.euler : ¬ (∀ k ≥ 4, ∀ S : Finset ℕ, S.card = k - 1 →
    ¬ (∃ q, ∑ s ∈ S, s ^ k = q ^k)) := by
  push_neg
  use 5
  norm_num
  use {27, 84, 110, 133}
  constructor
  · decide
  · use 144
    norm_num

end Erdos939


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
