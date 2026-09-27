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
# Erdős Problem 36

*References:*
 - [erdosproblems.com/36](https://www.erdosproblems.com/36)
 - [Wikipedial: Minimum overlap problem](https://en.wikipedia.org/wiki/Minimum_overlap_problem)
-/
open scoped Topology
open Filter
namespace Erdos36

/--
The number of solutions to the equation $a - b = k$, for $a \in A$ and $b \in B$.
This represents the "overlap" between sets $A$ and $B$ for a given difference $k$.
-/
def Overlap (A B : Finset ℤ) (k : ℤ) : ℕ := ((A.product B).filter <| fun (a, b) => a - b = k).card

/--
The maximum overlap for a given pair of sets $A$ and $B$,
taken over all possible integer differences $k$.
-/
noncomputable def MaxOverlap (A B : Finset ℤ) : ℕ := iSup <| Overlap A B

/--
Let $A$ and $B$ be two complementary subsets, a splitting of the numbers $\{1, 2, \dots, 2n\}$,
such that both have the same cardinality $n$.
Define $M(n)$ to be the minimum `MaxOverlap` that can be achieved,
ranging over all such partitions $(A, B)$.
-/
noncomputable def M (n : ℕ) : ℕ :=
  sInf {MaxOverlap A B | (A : Finset ℤ) (B : Finset ℤ)
    (_disjoint : Disjoint A B)
    (_union : A ∪ B = Finset.Icc (1 : ℤ) (2 * n))
    (_same_card : A.card = B.card)}

/-- A small API lemma: every pair `(a, b) ∈ A × B` contributes to `Overlap A B (a - b)`. -/
@[category API, AMS 5 11]
private lemma one_le_overlap {A B : Finset ℤ} {a b : ℤ}
    (ha : a ∈ A) (hb : b ∈ B) : 1 ≤ Overlap A B (a - b) :=
  Finset.card_pos.mpr ⟨(a, b), Finset.mem_filter.mpr
    ⟨Finset.mem_product.mpr ⟨ha, hb⟩, rfl⟩⟩

/-- For a fixed difference `k`, the first coordinate determines the second, so an overlap is
never larger than either side. This is what makes `MaxOverlap` a supremum of a bounded set. -/
@[category API, AMS 5 11]
private lemma overlap_le_card_left (A B : Finset ℤ) (k : ℤ) : Overlap A B k ≤ A.card := by
  refine Finset.card_le_card_of_injOn Prod.fst (fun p hp => ?_) (fun p hp q hq h => ?_)
  · exact (Finset.mem_product.mp (Finset.mem_filter.mp hp).1).1
  · obtain ⟨-, hpk⟩ := Finset.mem_filter.mp hp
    obtain ⟨-, hqk⟩ := Finset.mem_filter.mp hq
    exact Prod.ext h (by omega)

/-- The range of `Overlap A B` is bounded, so `MaxOverlap` is a genuine supremum rather than
the junk value `sSup` returns on an unbounded set. -/
@[category API, AMS 5 11]
private lemma bddAbove_range_overlap (A B : Finset ℤ) :
    BddAbove (Set.range (Overlap A B)) := by
  refine ⟨A.card, ?_⟩
  rintro x ⟨k, rfl⟩
  exact overlap_le_card_left A B k

@[category API, AMS 5 11]
private lemma maxOverlap_le_card_left (A B : Finset ℤ) : MaxOverlap A B ≤ A.card :=
  ciSup_le fun k => overlap_le_card_left A B k

/-- An overlap can only be nonzero for a difference that is actually realised, which confines
the search for `MaxOverlap` to a finite set. -/
@[category API, AMS 5 11]
private lemma overlap_eq_zero_of_notMem_sub (A B : Finset ℤ) {k : ℤ}
    (hk : k ∉ (A ×ˢ B).image fun p => p.1 - p.2) : Overlap A B k = 0 := by
  rw [Overlap, Finset.card_eq_zero, Finset.filter_eq_empty_iff]
  rintro ⟨a, b⟩ hab rfl
  exact hk (Finset.mem_image.mpr ⟨(a, b), hab, rfl⟩)

/-- `MaxOverlap` as a supremum over a finite set of differences. This is the form that makes it
possible to evaluate: the `iSup` in the definition ranges over all of `ℤ`, but every difference
outside `A - B` contributes `0`. -/
@[category API, AMS 5 11]
private lemma maxOverlap_eq_sup (A B : Finset ℤ) :
    MaxOverlap A B = ((A ×ˢ B).image fun p => p.1 - p.2).sup (Overlap A B) := by
  refine le_antisymm (ciSup_le fun k => ?_) (Finset.sup_le fun k _ => ?_)
  · by_cases hk : k ∈ (A ×ˢ B).image fun p => p.1 - p.2
    · exact Finset.le_sup hk
    · simp [overlap_eq_zero_of_notMem_sub A B hk]
  · exact le_ciSup (bddAbove_range_overlap A B) k

/-- The pairs `M n` ranges over are exactly the `n`-element subsets of `{1, …, 2n}`, each paired
with its complement. This turns the `sInf` over an unbounded family of `Finset ℤ` into an
infimum over a `Finset`. -/
@[category API, AMS 5 11]
private lemma M_eq_image (n : ℕ) :
    M n = sInf ((fun A : Finset ℤ => MaxOverlap A (Finset.Icc (1 : ℤ) (2 * n) \ A)) ''
      {A | A ⊆ Finset.Icc (1 : ℤ) (2 * n) ∧ A.card = n}) := by
  rw [M]
  congr 1
  ext m
  constructor
  · rintro ⟨A, B, hdisj, hunion, hcard, rfl⟩
    have hA : A ⊆ Finset.Icc (1 : ℤ) (2 * n) := hunion ▸ Finset.subset_union_left
    have hB : B = Finset.Icc (1 : ℤ) (2 * n) \ A := by
      rw [← hunion, Finset.union_sdiff_c

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
