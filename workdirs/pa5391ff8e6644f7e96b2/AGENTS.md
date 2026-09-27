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
# Erdős Problem 219

*Reference:* [erdosproblems.com/219](https://www.erdosproblems.com/219)
-/

namespace Erdos219

/--
The set of arithmetic progressions of primes
-/
def primeArithmeticProgressions : Set (Set ℕ) :=
  {s | (∀ p ∈ s, p.Prime) ∧ ∃ l > 0, s.IsAPOfLength l}

@[category test, AMS 5 11]
theorem primeArithmeticProgression_3_5_7 : {3, 5, 7} ∈ primeArithmeticProgressions := by
  simp only [primeArithmeticProgressions, gt_iff_lt, Set.IsAPOfLength, Set.IsAPOfLengthWith,
    smul_eq_mul, exists_prop, exists_and_left, existsAndEq, true_and, Set.mem_setOf_eq,
    Set.mem_insert_iff, Set.mem_singleton_iff, forall_eq_or_imp, forall_eq,
    ENat.card_eq_coe_fintype_card, Fintype.card_ofFinset, Set.toFinset_insert,
    Set.toFinset_singleton, Finset.mem_insert, Nat.reduceEqDiff, Finset.mem_singleton, or_self,
    not_false_eq_true, Finset.card_insert_of_notMem, Finset.card_singleton, Nat.reduceAdd,
    Nat.cast_ofNat, Nat.ofNat_pos, Nat.cast_lt_ofNat]
  refine ⟨by norm_num, ⟨3, 2, Set.ext fun x => ?_⟩⟩
  refine ⟨?_, fun ⟨w, ⟨hl, hr⟩⟩ => by interval_cases w <;> simp_all⟩
  rintro (rfl | rfl | rfl)
  · simp
  · simpa using ⟨1, by simp⟩
  · simpa using ⟨2, by simp⟩

@[category test, AMS 5 11]
theorem not_primeArithmeticProgression_1_2 : ¬{1, 2} ∈ primeArithmeticProgressions := by
  simp [primeArithmeticProgressions]
  norm_num

@[category API, AMS 5 11]
theorem empty_not_primeArithmeticProgression : ∅ ∉ primeArithmeticProgressions := by
  simpa [primeArithmeticProgressions] using fun _ hl ↦ Set.not_isAPOfLength_empty hl

@[category API, AMS 5 11]
lemma singleton_mem_primeArithmeticProgressions
    {p : ℕ} (hp : p.Prime) : {p} ∈ primeArithmeticProgressions := by
  simpa [primeArithmeticProgressions, hp] using ⟨1, one_pos, by simp⟩

@[category API, AMS 5 11]
lemma pair_mem_primeArithmeticProgressions
    {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (hpq : p < q) :
    {p, q} ∈ primeArithmeticProgressions := by
  let ⟨n, h⟩ := Nat.exists_eq_add_of_lt hpq
  simpa [primeArithmeticProgressions, hp, hq] using ⟨2, by norm_num, Nat.isAPOfLength_pair hpq⟩

/--
Are there arbitrarily long arithmetic progressions of primes?
Solution: yes.
Ref: Green, Ben and Tao, Terence, _The primes contain arbitrarily long arithmetic progressions_
-/

@[category research solved, AMS 5 11]
theorem erdos_219 : answer(True) ↔ ∀ N : ℕ, ∃ l ∈ primeArithmeticProgressions, N ≤ ENat.card l := by
  sorry

end Erdos219


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
