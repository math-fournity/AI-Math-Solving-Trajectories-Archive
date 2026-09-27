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
# Erdős Problem 786

*Reference:* [erdosproblems.com/786](https://www.erdosproblems.com/786)
-/

open Filter Real

open scoped Topology

namespace Erdos786

open Erdos786

-- TODO : add variants that allow repetition.
-- According to the updated website, Erdos likely intended repetitions to be allowed here
-- however, the analogous questions without repetition are also open.
/--
`Nat.IsMulCardSet A` means that `A` is a set of natural numbers that
satisfies the property that $a_1\cdots a_r = b_1\cdots b_s$ with $a_i, b_j\in A$
can only hold when $r = s$.
-/
def Set.IsMulCardSet {α : Type*} [CommMonoid α] (A : Set α) :=
  ∀ (a b : Finset α) (_ :↑a ⊆ A) (_ : ↑b ⊆ A) (_ : a.prod id = b.prod id),
    a.card = b.card

/--
Let $\epsilon > 0$. Is there some set $A\subset\mathbb{N}$ of density $> 1 - \epsilon$
such that $a_1\cdots a_r = b_1\cdots b_s$ with $a_i, b_j\in A$ can only hold when
$r = s$?
-/
@[category research open, AMS 11]
theorem erdos_786.parts.i : answer(sorry) ↔ ∀ ε > 0, ε ≤ 1 →
    ∃ (A : Set ℕ) (δ : ℝ), 0 ∉ A ∧ 1 - ε < δ ∧ A.HasDensity δ ∧ A.IsMulCardSet := by
  sorry

/--
Is there some set $A\subset\{1, ..., N\}$ of size $\geq (1 - o(1))N$ such that
$a_1\cdots a_r = b_1\cdots b_s$ with $a_i, b_j\in A$ can only hold when
$r = s$?
-/
@[category research open, AMS 11]
theorem erdos_786.parts.ii : answer(sorry) ↔
    ∃ (A : ℕ → Set ℕ) (f : ℕ → ℝ) (_ : f =o[atTop] (1 : ℕ → ℝ)),
    ∀ N, A N ⊆ Set.Icc 1 (N + 1) ∧ (1 - f N) * N ≤ (A N).ncard ∧ (A N).IsMulCardSet := by
  sorry

/--
An example of such a set with density $\frac 1 4$ is given by the integers $\equiv 2\pmod{4}$
-/
@[category textbook, AMS 11]
theorem erdos_786.parts.i.example (A : Set ℕ) (hA : A = { n | n % 4 = 2 }) :
    A.HasDensity (1 / 4) ∧ A.IsMulCardSet := by
  subst hA
  constructor
  · -- Exactly `(n + 1) / 4` of the naturals below `n` are `≡ 2 (mod 4)`.
    have hfin : ∀ n : ℕ, ((Finset.range n).filter fun m ↦ m % 4 = 2).card = (n + 1) / 4 := by
      intro n
      induction n with
      | zero => simp
      | succ n ih =>
        rw [Finset.range_add_one, Finset.filter_insert]
        split
        · rw [Finset.card_insert_of_notMem (by simp)]; omega
        · omega
    have hcard : ∀ n : ℕ, ({m : ℕ | m % 4 = 2} ∩ Set.Iio n).ncard = (n + 1) / 4 := by
      intro n
      have hset : {m : ℕ | m % 4 = 2} ∩ Set.Iio n
          = ↑((Finset.range n).filter fun m ↦ m % 4 = 2) := by
        ext m; simp [Set.mem_Iio, and_comm]
      rw [hset, Set.ncard_coe_finset, hfin]
    rw [Set.HasDensity]
    have hpd : ∀ n : ℕ, ({m : ℕ | m % 4 = 2}).partialDensity Set.univ n
        = (((n + 1) / 4 : ℕ) : ℝ) / (n : ℝ) := by
      intro n
      rw [Set.partialDensity, Set.inter_univ, Set.univ_inter, hcard, Nat.ncard_Iio]
    simp only [hpd]
    -- Squeeze `⌊(n + 1) / 4⌋ / n` between `1 / 4 - 1 / n` and `1 / 4 + 1 / n`.
    have hbdd : ∀ n : ℕ, 1 ≤ n →
        1 / 4 - 1 / (n : ℝ) ≤ (((n + 1) / 4 : ℕ) : ℝ) / (n : ℝ) ∧
          (((n + 1) / 4 : ℕ) : ℝ) / (n : ℝ) ≤ 1 / 4 + 1 / (n : ℝ) := by
      intro n hn
      have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
      have h1 : 4 * ((n + 1) / 4) ≤ n + 1 := by omega
      have h2 : n + 1 < 4 * ((n + 1) / 4) + 4 := by omega
      have c1 : (4 : ℝ) * (((n + 1) / 4 : ℕ) : ℝ) ≤ (n : ℝ) + 1 := by exact_mod_cast h1
      have c2 : (n : ℝ) + 1 < 4 * (((n + 1) / 4 : ℕ) : ℝ) + 4 := by exact_mod_cast h2
      constructor
      · rw [le_div_iff₀ hn0]; field_simp; linarith
      · rw [div_le_iff₀ hn0]; field_simp; linarith
    have hlim : ∀ c : ℝ, Tendsto (fun n : ℕ ↦ 1 / 4 + c * (1 / (n : ℝ))) atTop (𝓝 (1 / 4)) := by
      intro c
      simpa using Tendsto.const_add (1 / 4 : ℝ)
        (Tendsto.const_mul c tendsto_one_div_atTop_nhds_zero_nat)
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le'
      (by simpa using hlim (-1)) (by simpa using hlim 1)
      (eventually_atTop.2 ⟨1, fun n hn ↦ ?_⟩) (eventually_atTop.2 ⟨1, fun n hn ↦ ?_⟩)
    · simpa using (hbdd n hn).1
    · simpa using (hbdd n hn).2
  · -- Every element of the set is exactly divisible by `2`, so the `2`-adic valuation of a
    -- product of distinct such elements is the number of factors.
    have key : ∀ s : Finset ℕ, ↑s ⊆ {n : ℕ | n % 4 = 2} →
        (s.prod id).factorization 2 = s.card := by
      intro s hs
      have hmem : ∀ i ∈ s, i % 4 = 2 := fun i hi ↦ hs hi
      have h0 : ∀ i ∈ s, id i ≠ 0 := fun i hi ↦ by
        have := hmem i hi; simp onl

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
