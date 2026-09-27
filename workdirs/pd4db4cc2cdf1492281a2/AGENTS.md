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
# The length of an $s$-increasing sequence of $r$-tuples

This file contains the formalisation of [GoLo21] up to and
including Conjecture 1.8.

*References:*
- [arxiv/1609.08688](https://arxiv.org/abs/1609.08688)
  **The length of an $s$-increasing sequence of $r$-tuples** by *W. T. Gowers, J. Long*
- [GoLo21](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/length-of-an-sincreasing-sequence-of-rtuples/7301418D47DB1ECD6BE71C20E8A98D0A)
  **The length of an $s$-increasing sequence of $r$-tuples**
  by *W. T. Gowers, J. Long*, Combinatorics, Probability and Computing (2021), 686-721
-/

namespace Arxiv.«1609.08688»

/--
Let $a = (a_1, a_2, a_3)$ and $b = (b_1, b_2, b_3)$ be two triples of integers.
Say that $a$ is $2$-less than $b$, or $a <_2 b$, if $a_i < b_i$ for at least
two coordinates $i$.
-/
def lt₂ {α : Type*} [LT α] (a b : Fin 3 → α) : Prop :=
  ∃ (i j : Fin 3), i ≠ j ∧ a i < b i ∧ a j < b j

local infix:50 " <₂ " => lt₂

@[simp, category API, AMS 5]
theorem not_lt₂ {α : Type*} [LinearOrder α] {a b : Fin 3 → α} :
    ¬a <₂ b ↔ ∀ i j, i ≠ j → a i < b i → b j ≤ a j := by simp [lt₂]

@[category API, AMS 5]
theorem not_lt₂_of_forall_le {α : Type*} [LinearOrder α] {a b : Fin 3 → α}
    (h : ∀ i, b i ≤ a i) : ¬a <₂ b := not_lt₂.2 fun _ _ _ _ => h _

@[category API, AMS 5]
theorem not_lt₂_of_exists {α : Type*} [LinearOrder α] {a b : Fin 3 → α}
    (i j : Fin 3) (hij : i ≠ j) (hi : b i ≤ a i) (hj : b j ≤ a j) :
    ¬a <₂ b := by
  refine not_lt₂.2 fun k l hkl h => ?_
  have : k ≠ i := fun hk => not_lt.2 hi (hk ▸ h)
  have : k ≠ j := fun hk => not_lt.2 hj (hk ▸ h)
  have : l = i ∨ l = j := by omega
  rcases this with (rfl | rfl); exact hi; exact hj

@[category API, AMS 5]
theorem not_lt₂_self {α : Type*} [LinearOrder α] (a : Fin 3 → α) : ¬a <₂ a := by
  simp

/-- For example, $(3, 3, 9) <_2 (5, 6, 1)$. -/
@[category test, AMS 5]
theorem lt₂_example_1 : ![3, 3, 9] <₂ ![5, 6, 1] := ⟨0, 1, zero_ne_one, by simp⟩

/-- $(5, 6, 1) <_2 (7, 7, 7)$ -/
@[category test, AMS 5]
theorem lt₂_example_2 : ![5, 6, 1] <₂ ![7, 7, 7] := ⟨0, 2, by simp, by simp⟩

/-- $(7, 7, 7) <_2 (7, 8, 9)$ -/
@[category test, AMS 5]
theorem lt₂_example_3 : ![7, 7, 7] <₂ ![7, 8, 9] := ⟨1, 2, by simp, by simp⟩

/-- but $(1, 2, 3)$ is not $2$-less than $(1, 2, 4). -/
@[category test, AMS 5]
theorem not_lt₂_example : ¬![1, 2, 3] <₂ ![1, 2, 4] := not_lt₂_of_exists 0 1 zero_ne_one (by simp) (by simp)

/-- The $2$-less relation is not transitive on the naturals. -/
@[category API, AMS 5]
theorem not_trans_lt₂_nat : ∃ (a b c : Fin 3 → ℕ),
    a <₂ b ∧ b <₂ c ∧ ¬a <₂ c :=
  ⟨![1, 2, 3], ![2, 3, 1], ![3, 1, 2], ⟨0, 1, zero_ne_one, by simp⟩,
     ⟨0, 2, by simp, by simp⟩, not_lt₂_of_exists 1 2 (by simp) (by simp) (by simp)⟩

/--
Since the $2$-less relation is not transitive, we make a further definition to
specify transivity.
-/
def IsIncreasing₂ {α : Type*} [LT α] (s : List (Fin 3 → α)) : Prop := s.Pairwise lt₂

@[simp, category API, AMS 5]
theorem isIncreasing₂_nil {α : Type*} [LT α] : IsIncreasing₂ (α := α) [] := by
  simp [IsIncreasing₂]

@[simp, category API, AMS 5]
theorem isIncreasing₂_singleton {α : Type*} [LT α] (a : Fin 3 → α) : IsIncreasing₂ [a] := by
  simp [IsIncreasing₂]

@[category API, AMS 5]
theorem isIncreasing₂_const_length {α : Type*} [LinearOrder α] {val : α} {s : List (Fin 3 → α)}
    (h : IsIncreasing₂ s)
    (h_const : ∀ a ∈ s, ∀ j, a j = val) : s.length < 2 := by
  by_contra!
  have h₀ : s[0] = fun _ => val := funext fun i => by simp [h_const s[0] (by simp)]
  have h₁ : s[1] = fun _ => val := funext fun i => by simp [h_const s[1] (by simp)]
  have := List.pairwise_iff_getElem.1 h 0 1 (by linarith) (by linarith) zero_lt_one
  simp [h₀, h₁] at this
  exact not_lt₂_self _ this

/--
Let $F(n)$ be the maximal length of a $2$-increasing sequence of triples with each coordinate
belong to $[n]$ ($= \{1, 2, ..., n\}$).
-/
noncomputable def maximalLength (n : ℕ) : ℕ :=
  sSup { List.length s | (s) (_ : ∀ a ∈ s, Set.range a ⊆ Set.Icc 1 n) (_ : IsIncreasing₂ s) }

local notation "F" => maximalLength

@[category test, AMS 5]
theorem maximalLength_zero : maximalLength 0 = 0 := by
  have (x : ℕ) (s : List (Fin 3 → ℕ)) :
      IsIncreasing₂ s ∧ (∀ a, a ∉ s) ∧ s.length = x ↔ s = [] ∧ x = 0 := by
    refine ⟨fun ⟨ha₁, ha₂, rfl⟩ => ?_, fun ⟨h₁, h₂⟩ => by simp [h₁, h₂]⟩
    simp only [List.length_eq_zero_if

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
