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
# Written on the Wall II - Conjecture 322

*Reference:*
[E. DeLaViña, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.uhd.edu/faculty/delavinae/research/wowII/)

The source applies the local-independence hypothesis to the complement graph. Its conclusion
also follows from the characterization of minimal total dominating sets of complete multipartite
graphs in [M. Subramanian and A. Selvakumar, *Total Domination and Minimal Total Domination
Polynomial of H-Join Graphs*](https://doi.org/10.2298/FIL2501267S).
-/


namespace WrittenOnTheWallII.GraphConjecture322

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α]

/--
WOWII [Conjecture 322](http://cms.uhd.edu/faculty/delavinae/research/wowII/open.html)

Let `G` be a simple connected graph on `n ≥ 5` vertices. If the maximum over all
vertices `v` of `l(v)` in the complement graph `Gᶜ` — the independence number of
the neighborhood `N(v)` of `v` — is at most 1, then `G` is well totally dominated.

Here `l(v) = α(Gᶜ[N(v)])` is the independence number of the subgraph induced by the
open neighborhood of `v` in `Gᶜ`.
-/
@[category research solved, AMS 5, formal_proof using formal_conjectures at
  "https://github.com/SamuelSchlesinger/formal-conjectures/blob/78f39db3ea9f5a8b2e6841e7769f538ff263dbf2/FormalConjectures/WrittenOnTheWallII/GraphConjecture322.lean#L50-L111"]
theorem conjecture322 (G : SimpleGraph α) [DecidableRel G.Adj] (_hG : G.Connected)
    (hn : 5 ≤ Fintype.card α)
    (h : ∀ v : α, indepNeighborsCard Gᶜ v ≤ 1) :
    IsWellTotallyDominated G := by
  have adj_of_local_independence_one (H : SimpleGraph α) {v x y : α}
      (hv : indepNeighborsCard H v ≤ 1) (hx : H.Adj v x) (hy : H.Adj v y)
      (hxy : x ≠ y) : H.Adj x y := by
    by_contra hnxy
    let x' : H.neighborSet v := ⟨x, hx⟩
    let y' : H.neighborSet v := ⟨y, hy⟩
    have hne : x' ≠ y' := by
      intro heq
      exact hxy (congrArg Subtype.val heq)
    have hind : (H.induce (H.neighborSet v)).IsIndepSet ({x', y'} : Finset _) := by
      rw [isIndepSet_iff]
      intro a ha b hb hab
      simp only [Finset.mem_coe, Finset.mem_insert, Finset.mem_singleton] at ha hb
      rcases ha with (rfl | rfl) <;> rcases hb with (rfl | rfl)
      · exact (hab rfl).elim
      · exact hnxy
      · exact fun hyx ↦ hnxy hyx.symm
      · exact (hab rfl).elim
    have hle := hind.card_le_indepNum
    have hcard : ({x', y'} : Finset _).card = 2 := by simp [hne]
    rw [hcard] at hle
    exact (by omega : ¬(2 ≤ indepNeighborsCard H v)) hle
  have edge_total {x y : α} (hxy : G.Adj x y) : IsTotalDominatingSet G {x, y} := by
    intro v
    by_cases hvx : G.Adj v x
    · exact ⟨x, by simp, hvx⟩
    by_cases hvy : G.Adj v y
    · exact ⟨y, by simp, hvy⟩
    exfalso
    have hvx_ne : v ≠ x := by
      rintro rfl
      exact hvy hxy
    have hvy_ne : v ≠ y := by
      rintro rfl
      exact hvx hxy.symm
    have hvx_compl : Gᶜ.Adj v x := (G.compl_adj v x).2 ⟨hvx_ne, hvx⟩
    have hvy_compl : Gᶜ.Adj v y := (G.compl_adj v y).2 ⟨hvy_ne, hvy⟩
    have hxy_compl : Gᶜ.Adj x y :=
      adj_of_local_independence_one Gᶜ (h v) hvx_compl hvy_compl hxy.ne
    exact ((G.compl_adj x y).1 hxy_compl).2 hxy
  have minimal_card_two {S : Finset α} (hS : IsMinimalTotalDominatingSet G S) :
      S.card = 2 := by
    have hcardpos : 0 < Fintype.card α := by omega
    let v : α := Classical.choice (Fintype.card_pos_iff.mp hcardpos)
    obtain ⟨w, hwS, _⟩ := hS.1 v
    obtain ⟨x, hxS, hwx⟩ := hS.1 w
    have hpair_subset : ({w, x} : Finset α) ⊆ S := by
      simpa only [Finset.insert_subset_iff, Finset.singleton_subset_iff] using
        (And.intro hwS hxS)
    have hpair_not_ssubset : ¬({w, x} : Finset α) ⊂ S := by
      intro hss
      exact hS.2 {w, x} hss (edge_total hwx)
    have hpair_eq : ({w, x} : Finset α) = S :=
      hpair_subset.eq_of_not_ssubset hpair_not_ssubset
    rw [← hpair_eq]
    simp [hwx.ne]
  intro S T hS hT
  rw [minimal_card_two hS, minimal_card_two hT]

-- Sanity checks

/-- In `K₄`, all vertices have degree 3. -/
@[category test, AMS 5]
example : (⊤ : SimpleGraph (Fin 4)).maxDegree = 3 := by decide +native

/-- In the edgeless graph `⊥` on 5 vertices, the minimum degree is 0. -/
@[category test, AMS 5]
example : (⊥ : SimpleGraph (Fin 5)).minDegree = 0 := by decide +native

end WrittenOnTheWallII.GraphConjecture322


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
