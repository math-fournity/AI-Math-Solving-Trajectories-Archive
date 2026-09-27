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
# Erdős Problem 10

*Reference:* [erdosproblems.com/10](https://www.erdosproblems.com/10)
-/

namespace Erdos10

/--
The set of natural numbers that can be written as a sum
of a prime and at most $k$ powers of $2$.
-/
abbrev sumPrimeAndTwoPows (k : ℕ) : Set ℕ :=
  { p + (pows.map (2 ^ ·)).sum | (p : ℕ) (pows : Multiset ℕ) (_ : p.Prime)
    (_ : pows.card ≤ k)}

/--
Is there some $k$ such that every integer is the sum of a prime and at most $k$
powers of $2$?
-/
@[category research open, AMS 5 11]
theorem erdos_10 : answer(sorry) ↔ ∃ k, sumPrimeAndTwoPows k = Set.univ \ {0, 1} := by
  sorry

/--
Gallagher [Ga75] has shown that for any $ϵ > 0$ there exists $k(ϵ)$
such that the set of integers which are the sum of a prime and at most $k(ϵ)$
many powers of $2$ has lower density at least $1 - ϵ$.

Ref: Gallagher, P. X., _Primes and powers of 2_.
-/
@[category research solved, AMS 5 11]
theorem erdos_10.variants.gallagher (ε : ℝ)
    (hε : 0 < ε) : ∃ k, 1 - ε ≤ (sumPrimeAndTwoPows k).lowerDensity := by
  sorry

/--
Granville and Soundararajan [GrSo98] have conjectured that at most $3$
powers of $2$ suffice for all odd integers, and hence at most $4$ powers of $2$
suffice for all even integers.

Ref: Granville, A. and Soundararajan, K., _A Binary Additive Problem of Erdős and the Order of $2$ mod $p^2$_
-/
@[category research open, AMS 5 11]
theorem erdos_10.variants.granville_soundararajan_odd :
    {n : ℕ | Odd n ∧ 1 < n} ⊆ sumPrimeAndTwoPows 3 ∧
      {n : ℕ | Even n ∧ n ≠ 0} ⊆ sumPrimeAndTwoPows 4 := by
  sorry

/--
Bogdan Grechuk has observed that `1117175146` is not the sum of a prime
and at most $3$ powers of $2$.
-/
@[category research solved, AMS 5 11]
theorem erdos_10.variants.grechuk_example :
    1117175146 ∉ sumPrimeAndTwoPows 3 := by
  sorry

/--
There are infinitely many even integers not the sum of a prime and $2$ powers of $2$
-/
@[category research solved, AMS 5 11]
theorem erdos_10.variants.two_pows :
    Set.Infinite <| {n : ℕ | Even n} \ sumPrimeAndTwoPows 2 := by
  sorry

/--
Bogdan Grechuk has observed that $1117175146$ is not the sum of a prime and at most $3$
powers of $2$, and pointed out that parity considerations, coupled with the fact that there
are many integers not the sum of a prime and $2$ powers of $2$ suggest that there exist
infinitely many even integers which are not the sum of a prime and at most $3$ powers of $2$).
-/
@[category research open, AMS 5 11]
theorem erdos_10.variants.grechuk :
    Set.Infinite <| {n : ℕ | Even n} \ sumPrimeAndTwoPows 3 := by
  sorry

end Erdos10


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
