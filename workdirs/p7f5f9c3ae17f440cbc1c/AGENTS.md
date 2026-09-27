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
# Erdős Problem 42: Maximal Sidon Sets and Disjoint Difference Sets

*Reference:* [erdosproblems.com/42](https://www.erdosproblems.com/42)

This problem asks whether maximal Sidon sets can coexist with other Sidon sets that have
disjoint difference sets (apart from 0).
-/

open Function Set Filter
open scoped Pointwise

namespace Erdos42

/--
**Erdős Problem 42**: Let M ≥ 1 and N be sufficiently large in terms of M. Is it true that for every
maximal Sidon set `A ⊆ {1,…,N}` there is another Sidon set `B ⊆ {1,…,N}` of size M such that
`(A - A) ∩ (B - B) = {0}`?

This was proved for all $M$ by GPT 5.5 Pro (prompted by Sandhu), see discussion thread for more details.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/Shashi456/erdos-formalizations/blob/main/Erdos/P42/CompactCayley/Proof.lean"]
theorem erdos_42 : answer(True) ↔
    ∀ M ≥ 1, ∀ᶠ N in atTop, ∀ (A : Set ℕ) (_ : IsMaximalSidonSetIn A N),
    ∃ᵉ (B : Set ℕ), B ⊆ Set.Icc 1 N ∧ IsSidon B ∧ B.ncard = M ∧
    ((A - A) ∩ (B - B)) = {0} := by
  sorry

/--
A variant asking for explicit bounds on how large N needs to be in terms of M.

This version provides a constructive function f such that for all M ≥ 1 and N ≥ f(M),
every maximal Sidon set A ⊆ {1,…,N} has another Sidon set B ⊆ {1,…,N} of size M with
disjoint difference sets (apart from 0).
-/
@[category research solved, AMS 5 11,
  formal_proof using formal_conjectures at "https://github.com/KitaKen1/erdos-42-constructive-variant/blob/1f82c76be43cb56f22e2f7f792e392d5fb3ff78c/lean/Erdos42Constructive.lean"]
theorem erdos_42.variants.constructive : answer(True) ↔
    ∃ (f : ℕ → ℕ), ∀ (M N : ℕ) (_ : 1 ≤ M) (_ : f M ≤ N),
    ∀ (A : Set ℕ) (_ : IsMaximalSidonSetIn A N), ∃ᵉ (B : Set ℕ),
      B ⊆ Set.Icc 1 N ∧ IsSidon B ∧ B.ncard = M ∧
      ((A - A) ∩ (B - B)) = {0} := by
  sorry


/-  ## Related results and examples -/

/--
The set `{1, 2, 4}` is a maximal Sidon set in `{1, ..., 4}`.
-/
@[category textbook, AMS 5 11]
theorem example_maximal_sidon : IsMaximalSidonSetIn {1, 2, 4} 4 := by
  refine ⟨?_, ?_, ?_⟩
  · intro x hx
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hx
    rcases hx with rfl | rfl | rfl <;> simp [Set.mem_Icc]
  · intro i₁ hi₁ j₁ hj₁ i₂ hi₂ j₂ hj₂ hsum
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hi₁ hj₁ hi₂ hj₂
    rcases hi₁ with rfl | rfl | rfl <;>
    rcases hj₁ with rfl | rfl | rfl <;>
    rcases hi₂ with rfl | rfl | rfl <;>
    rcases hj₂ with rfl | rfl | rfl <;>
    simp_all
  · intro x hx hxA
    simp only [Set.mem_Icc] at hx; obtain ⟨hx1, hx2⟩ := hx
    simp only [Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hxA
    obtain ⟨hne1, hne2, hne4⟩ := hxA
    have hx3 : x = 3 := (by omega); subst hx3
    intro hbad
    have := hbad 1 (by simp) 2 (by simp) 3 (by simp) 2 (by simp) (by norm_num)
    rcases this with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> omega

/--
The difference set of `{1, 2, 4}` is `{0, 1, 2, 3}`.
-/
@[category textbook, AMS 5 11]
theorem example_difference_set : ({1, 2, 4} : Set ℕ) - {1, 2, 4} = {0, 1, 2, 3} := by
  ext x
  simp only [Set.mem_sub, Set.mem_insert_iff, Set.mem_singleton_iff]
  constructor
  · rintro ⟨a, ha, b, hb, rfl⟩
    rcases ha with rfl | rfl | rfl <;>
    rcases hb with rfl | rfl | rfl <;>
    simp
  · rintro (rfl | rfl | rfl | rfl)
    · exact ⟨1, by decide, 1, by decide, by decide⟩
    · exact ⟨2, by decide, 1, by decide, by decide⟩
    · exact ⟨4, by decide, 2, by decide, by decide⟩
    · exact ⟨4, by decide, 1, by decide, by decide⟩

/--
For any maximal Sidon set, the difference set contains 0.
-/
@[category textbook, AMS 5 11]
theorem maximal_sidon_contains_zero (A : Set ℕ) (N : ℕ) (hN : 1 ≤ N)
    (hA : IsMaximalSidonSetIn A N) : 0 ∈ A - A := by
  obtain ⟨hAsub, hAsidon, hAmax⟩ := hA
  have hne : A.Nonempty
  · by_contra hemp; rw [Set.not_nonempty_iff_eq_empty] at hemp
    exact hAmax (Set.mem_Icc.mpr ⟨le_refl 1, hN⟩)
      (by rw [hemp]; exact id) (by
        rw [hemp, Set.empty_union]
        exact fun _ hi _ hj _ hk _ hl _ => by
          simp only [Set.mem_singleton_iff] at hi hj hk hl
          subst hi
          subst hj
          subst hk
          subst hl
          exact Or.inl ⟨rfl, rfl⟩)
  obtain ⟨a, ha⟩ := hne
  have := Set.sub_mem_sub ha ha
  rwa [Nat.sub_self] at this

end Erdos42


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
