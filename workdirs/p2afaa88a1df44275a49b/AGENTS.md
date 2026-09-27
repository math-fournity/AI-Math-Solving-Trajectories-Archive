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
# Erdős Problem 313

*References:*
- [erdosproblems.com/313](https://www.erdosproblems.com/313)
- [A54377](https://oeis.org/A54377) (Primary pseudoperfect numbers)
-/

namespace Erdos313

/--
This set contains all solutions `(m, P)` to the Erdős problem 313.
A solution is a pair where `m` is an integer `≥ 2` and `P` is a non-empty, finite set of
distinct prime numbers, such that the sum of the reciprocals of the primes in `P` equals `1 - 1/m`.
-/
def erdos313Solutions : Set (ℕ × Finset ℕ) :=
  {(m, P) | 2 ≤ m ∧ P.Nonempty ∧ (∀ p ∈ P, p.Prime) ∧ ∑ p ∈ P, (1 : ℚ) / p = 1 - 1 / m}

/--
Are there infinitely many pairs `(m, P)` where `m ≥ 2` is an integer
and `P` is a set of distinct primes such that the following equation holds:
$\sum_{p \in P} \frac{1}{p} = 1 - \frac{1}{m}$?
-/
@[category research open, AMS 11]
theorem erdos_313 : answer(sorry) ↔ erdos313Solutions.Infinite := by
  sorry

@[category test, AMS 11]
theorem erdos_313.variants.solution_6_2_3 : (6, {2, 3}) ∈ erdos313Solutions := by
  norm_num [erdos313Solutions]

@[category test, AMS 11]
theorem erdos_313.variants.solution_42_2_3_7 : (42, {2, 3, 7}) ∈ erdos313Solutions := by
  norm_num [erdos313Solutions]

/--
An integer `n` is a **primary pseudoperfect number** if it is the denominator `m` in a
solution `(m, P)` to the Erdős 313 problem.
-/
def IsPrimaryPseudoperfect (n : ℕ) : Prop := ∃ P, (n, P) ∈ erdos313Solutions

/--
It is conjectured that the set of primary pseudoperfect numbers is infinite.
-/
@[category research open, AMS 11]
theorem erdos_313.variants.primary_pseudoperfect_are_infinite :
    Set.Infinite {n | IsPrimaryPseudoperfect n} := by
  sorry

/--
There are at least 8 primary pseudoperfect numbers. The first eight terms of
[A54377](https://oeis.org/A54377) are exhibited together with their explicit
prime decompositions.
-/
@[category textbook, AMS 11]
theorem erdos_313.variants.exists_at_least_eight_primary_pseudoperfect :
    8 ≤ (Set.encard {n | IsPrimaryPseudoperfect n}) := by
  let S : Finset ℕ :=
    {2, 6, 42, 1806, 47058, 2214502422, 52495396602,
      8490421583559688410706771261086}
  have hS : (↑S : Set ℕ) ⊆ {n | IsPrimaryPseudoperfect n} := by
    intro x hx
    simp only [S, Finset.coe_insert, Finset.coe_singleton, Set.mem_insert_iff,
      Set.mem_singleton_iff] at hx
    rcases hx with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
    · exact ⟨{2}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3, 7}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3, 7, 43}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3, 11, 23, 31}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3, 11, 23, 31, 47059}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3, 11, 17, 101, 149, 3109}, by norm_num [erdos313Solutions]⟩
    · exact ⟨{2, 3, 11, 23, 31, 47059, 2217342227, 1729101023519}, by
        refine ⟨by decide, by decide, ?_, ?_⟩
        · intro p hp
          fin_cases hp <;> native_decide
        · native_decide⟩
  calc (8 : ℕ∞)
      = ((S.card : ℕ) : ℕ∞) := by decide
    _ = (↑S : Set ℕ).encard := (Set.encard_coe_eq_coe_finsetCard S).symm
    _ ≤ Set.encard {n | IsPrimaryPseudoperfect n} := Set.encard_le_encard hS

end Erdos313


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
