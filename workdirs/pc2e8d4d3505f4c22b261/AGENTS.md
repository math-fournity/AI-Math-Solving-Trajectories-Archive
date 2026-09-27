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
# Erdős Problem 18

*Reference:*
* [erdosproblems.com/18](https://www.erdosproblems.com/18)
* [ErGr80] Erdős, P. and Graham, R. L. (1980). Old and New Problems and Results in Combinatorial Number
Theory. Monographies de L'Enseignement Mathématique, 28. Université de Genève. (See the
sections on Egyptian fractions or practical numbers).
* [Vo85] Vose, Michael D., Egyptian fractions. Bull. London Math. Soc. (1985), 21-24.
-/

open Filter Asymptotics Real

namespace Erdos18

/-- For a practical number $n$, $h(n)$ is the maximum over all $1 ≤ m ≤ n$ of
the minimum number of divisors of $n$ needed to represent $m$ as a sum of
distinct divisors. -/
noncomputable def practicalH (n : ℕ) : ℕ :=
  Finset.sup (Finset.Icc 1 n) fun m =>
    sInf {k | ∃ D : Finset ℕ, D ⊆ n.divisors ∧ D.card = k ∧ m ∈ subsetSums D}

/- ### Examples for `practicalH` -/

/-- $h(1) = 1$: we need the single divisor {1} to represent 1. -/
@[category test, AMS 11]
theorem practicalH_one : practicalH 1 = 1 := by
  norm_num [subsetSums, practicalH]

/-- $h(2) = 1$: divisors are {1, 2}, each of m=1,2 needs only 1 divisor. -/
@[category test, AMS 11]
theorem practicalH_two : practicalH 2 = 1 := by
  simp only [practicalH, (by decide : Finset.Icc 1 2 = ({1, 2} : Finset ℕ)),
    (by decide : Nat.divisors 2 = ({1, 2} : Finset ℕ)), Finset.sup_insert, Finset.sup_singleton]
  have h1 : sInf {k | ∃ D : Finset ℕ, D ⊆ {1, 2} ∧ D.card = k ∧ 1 ∈ subsetSums D} = 1 :=
    le_antisymm (Nat.sInf_le ⟨{1}, by simp, rfl, {1}, rfl.subset, by simp⟩)
      (le_csInf ⟨1, {1}, by simp, rfl, {1}, rfl.subset, by simp⟩ fun k ⟨D, _, hD, B, hB, hm⟩ =>
        hD ▸ Finset.one_le_card.mpr ((Finset.nonempty_iff_ne_empty.mpr fun h => by simp [h] at hm).mono hB))
  have h2 : sInf {k | ∃ D : Finset ℕ, D ⊆ {1, 2} ∧ D.card = k ∧ 2 ∈ subsetSums D} = 1 :=
    le_antisymm (Nat.sInf_le ⟨{2}, by simp, rfl, {2}, rfl.subset, by simp⟩)
      (le_csInf ⟨1, {2}, by simp, rfl, {2}, rfl.subset, by simp⟩ fun k ⟨D, _, hD, B, hB, hm⟩ =>
        hD ▸ Finset.one_le_card.mpr ((Finset.nonempty_iff_ne_empty.mpr fun h => by simp [h] at hm).mono hB))
  simp [h1, h2]

/-- $h(6) = 2$: divisors are {1, 2, 3, 6}. The hardest m to represent is
m=4 or m=5, each requiring 2 divisors: 4=1+3, 5=2+3. -/
@[category test, AMS 11]
theorem practicalH_six : practicalH 6 = 2 := by
  have hdiv : Nat.divisors 6 = ({1, 2, 3, 6} : Finset ℕ) := by decide
  apply le_antisymm
  · -- practicalH 6 ≤ 2 : each m in [1,6] is a sum of at most two divisors of 6.
    apply Finset.sup_le
    intro m hm
    rw [Finset.mem_Icc] at hm
    obtain ⟨hm1, hm2⟩ := hm
    interval_cases m
    · exact Nat.sInf_le ⟨{1, 2}, by rw [hdiv]; decide, by decide, {1}, by simp, by decide⟩
    · exact Nat.sInf_le ⟨{1, 2}, by rw [hdiv]; decide, by decide, {2}, by simp, by decide⟩
    · exact Nat.sInf_le ⟨{1, 2}, by rw [hdiv]; decide, by decide, {1, 2}, by simp, by decide⟩
    · exact Nat.sInf_le ⟨{1, 3}, by rw [hdiv]; decide, by decide, {1, 3}, by simp, by decide⟩
    · exact Nat.sInf_le ⟨{2, 3}, by rw [hdiv]; decide, by decide, {2, 3}, by simp, by decide⟩
    · exact Nat.sInf_le ⟨{1, 6}, by rw [hdiv]; decide, by decide, {6}, by simp, by decide⟩
  · -- 2 ≤ practicalH 6, witnessed by m = 4 (which needs two divisors: 4 = 1 + 3).
    have h4 : (4 : ℕ) ∈ Finset.Icc 1 6 := by decide
    refine le_trans ?_ (Finset.le_sup h4)
    apply le_csInf
    · exact ⟨2, {1, 3}, by rw [hdiv]; decide, by decide, {1, 3}, by simp, by decide⟩
    · rintro k ⟨D, hDsub, hDcard, B, hBsub, hBsum⟩
      by_contra hk
      push_neg at hk
      interval_cases k
      · -- D.card = 0 : D = ∅, so B = ∅ and the sum is 0 ≠ 4.
        rw [Finset.card_eq_zero] at hDcard
        subst hDcard
        rw [Finset.coe_empty, Set.subset_empty_iff, Finset.coe_eq_empty] at hBsub
        subst hBsub
        simp at hBsum
      · -- D.card = 1 : D = {d} with d ∣ 6, so the sum is 0 or d, neither equal to 4.
        rw [Finset.card_eq_one] at hDcard
        obtain ⟨d, rfl⟩ := hDcard
        have hd : d ∈ Nat.divisors 6 := hDsub (by simp)
        rw [hdiv] at hd
        rw [Finset.coe_subset, Finset.subset_singleton_iff] at hBsub
        fin_cases hd <;>
          rcases hBsub with h | h <;> subst h <;> simp at hBsum

/-- $h(12) = 3$: divisors are {1, 2, 3, 4, 6, 12}. The hardest m is
m=11, requiring 3 divisors: 11=1+4+6. -/
@[category test, AMS 11]
theorem practicalH_twelve : practicalH 12 = 3 := by
  

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
