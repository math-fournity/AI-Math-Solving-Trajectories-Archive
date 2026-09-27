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
# Erdős Problem 304
*Reference:* [erdosproblems.com/304](https://www.erdosproblems.com/304)
-/

open Asymptotics Filter

namespace Erdos304

/--
The set of `k` for which `a / b` can be expressed as a sum of `k` distinct unit fractions.
-/
def unitFractionExpressible (a b : ℕ) : Set ℕ :=
  {k | ∃ s : Finset ℕ, s.card = k ∧ (∀ n ∈ s, n > 1) ∧ (a / b : ℚ) = ∑ n ∈ s, (n : ℚ)⁻¹}

@[category API, simp, AMS 11]
lemma zero_mem_unitFractionExpressible_iff {a b : ℕ} :
    0 ∈ unitFractionExpressible a b ↔ a = 0 ∨ b = 0 := by
  simp_all [unitFractionExpressible]

@[category API, AMS 11]
lemma unitFractionExpressible_of_zero {a b : ℕ} (h : a = 0 ∨ b = 0) :
    unitFractionExpressible a b = {0} := by
  simp only [Set.eq_singleton_iff_unique_mem, zero_mem_unitFractionExpressible_iff, *]
  have : (a / b : ℚ) = 0 := by simpa
  simp only [unitFractionExpressible, gt_iff_lt, Set.mem_setOf_eq, forall_exists_index, and_imp,
    true_and, this]
  rintro _ s rfl hs h
  rw [eq_comm, Finset.sum_eq_zero_iff_of_nonneg (fun i hi ↦ by positivity)] at h
  simp only [inv_eq_zero, Nat.cast_eq_zero] at h
  rw [Finset.card_eq_zero, Finset.eq_empty_iff_forall_notMem]
  intro i hi
  linarith [h i hi, hs i hi]

@[category API, AMS 11]
lemma unitFractionExpressible_zero_left {b : ℕ} :
    unitFractionExpressible 0 b = {0} := unitFractionExpressible_of_zero (by simp)

@[category API, AMS 11]
lemma unitFractionExpressible_zero_right {a : ℕ} :
    unitFractionExpressible a 0 = {0} := unitFractionExpressible_of_zero (by simp)

@[category API, AMS 11]
lemma zero_notMem_unitFractionExpressible {a b : ℕ} :
    0 ∉ unitFractionExpressible a b ↔ a ≠ 0 ∧ b ≠ 0 := by
  simp_all [unitFractionExpressible]

@[category API, AMS 11]
lemma eq_inv_of_one_mem_unitFractionExpressible {a b : ℕ}
    (h : 1 ∈ unitFractionExpressible a b) : ∃ m : ℕ, 1 < m ∧ (a / b : ℚ) = (m : ℚ)⁻¹ := by
  simp only [unitFractionExpressible, gt_iff_lt, Set.mem_setOf_eq, Finset.card_eq_one] at h
  obtain ⟨_, ⟨m, rfl⟩, h₁, h₂⟩ := h
  simp only [Finset.mem_singleton, forall_eq, Finset.sum_singleton] at h₁ h₂
  use m

@[category API, AMS 11]
lemma dvd_of_one_mem_unitFractionExpressible {a b : ℕ}
    (h : 1 ∈ unitFractionExpressible a b) : a ∣ b := by
  obtain ⟨m, hm₁, hm⟩ := eq_inv_of_one_mem_unitFractionExpressible h
  have : b ≠ 0 := by
    rintro rfl
    simp [eq_comm] at hm
    omega
  use m
  field_simp at hm
  exact mod_cast hm.symm

/-- Let $$N(a, b)$$, denoted here by `smallestCollection a b` be the minimal k such that there
exist integers $1 < n_1 < n_2 < \dots < n_k$ with
$$\frac{a}{b} = \sum_{i=1}^k \frac{1}{n_i}$$ -/
noncomputable def smallestCollection (a b : ℕ) : ℕ := sInf (unitFractionExpressible a b)

-- in fact `(unitFractionExpressible a b).Nonempty` should always be true, but we do not prove it
-- for now
@[category API, AMS 11]
lemma smallestCollection_pos {a b : ℕ} (ha : a ≠ 0) (hb : b ≠ 0)
    (h : (unitFractionExpressible a b).Nonempty) :
    0 < smallestCollection a b := by
  suffices smallestCollection a b ≠ 0 by omega
  intro h'
  have : 0 ∈ unitFractionExpressible a b := h' ▸ Nat.sInf_mem h
  simp_all

@[category API, AMS 11]
lemma smallestCollection_left_one (b : ℕ) (hb : 1 < b) : smallestCollection 1 b = 1 := by
  have : 1 ∈ unitFractionExpressible 1 b := ⟨{b}, by simpa⟩
  have : smallestCollection 1 b ≤ 1 := Nat.sInf_le this
  have : 0 ∉ unitFractionExpressible 1 b := by simp; omega
  have : smallestCollection 1 b ≠ 0 := ne_of_mem_of_not_mem (Nat.sInf_mem ⟨_, ‹_›⟩) this
  omega

@[category API, AMS 11]
lemma eq_one_of_smallestCollection_eq_one {a b : ℕ}
    (h : smallestCollection a b = 1) : ∃ m : ℕ, 1 < m ∧ (a / b : ℚ) = (m : ℚ)⁻¹ := by
  have : 1 ∈ unitFractionExpressible a b := h ▸ Nat.sInf_mem (Nat.nonempty_of_sInf_eq_succ h)
  apply eq_inv_of_one_mem_unitFractionExpressible this

@[category API, AMS 11]
lemma dvd_of_smallestCollection_eq_one {a b : ℕ}
    (h : smallestCollection a b = 1) : a ∣ b := by
  have : 1 ∈ unitFractionExpressible a b := h ▸ Nat.sInf_mem (Nat.nonempty_of_sInf_eq_succ h)
  apply dvd_of_one_mem_unitFractionExpressible this

@[category test, AMS 11]
lemma smallestCollection_two_fifteen : smallestCollection 2 15 = 2 := by
  have h : 2 ∈ unitFractionExpressible 2 15 := by
    use {10, 30}
    norm_num [Finset.card_insert_of_notMem, Finset.card_singleton]
  have : smallestCollection 2 15 ≤ 2 := Nat.sInf_le h
  have : 0 < smallestColle

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
