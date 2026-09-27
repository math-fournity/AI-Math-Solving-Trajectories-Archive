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
# Erdős Problem 595

*References:*
- [erdosproblems.com/595](https://www.erdosproblems.com/595)
- [Er87] Erdős, Paul, Problems and results on set systems and hypergraphs. Extremal problems
  for finite sets (Visegrád, 1991), Bolyai Soc. Math. Stud. (1994), 217-227.
- [Fo70] Folkman, Jon, Graphs with monochromatic complete subgraphs in every edge coloring.
  SIAM J. Appl. Math. (1970), 19:340-345.
- [NeRo75] Nešetřil, Jaroslav and Rödl, Vojtěch, Type theory of partition problems of graphs.
  Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974),
  Academia, Prague (1975), 405-412.
-/

open SimpleGraph Set

namespace Erdos595

def IsCountableUnionOfTriangleFree {V : Type*} (G : SimpleGraph V) : Prop :=
  ∃ H : ℕ → SimpleGraph V, (∀ i, (H i).CliqueFree 3) ∧ G = ⨆ i, H i

/-
## Main open problem
-/

/--
**Erdős Problem 595 ($250)**: Is there an infinite graph $G$ which contains no $K_4$ and is
not the union of countably many triangle-free graphs?

A problem of Erdős and Hajnal [Er87].
-/
@[category research open, AMS 5]
theorem erdos_595 : answer(sorry) ↔
    ∃ (V : Type*) (_ : Infinite V) (G : SimpleGraph V),
      G.CliqueFree 4 ∧ ¬IsCountableUnionOfTriangleFree G := by
  sorry

/-
## Variants and partial results
-/

/--
**Folkman–Nešetřil–Rödl (finite version) [Fo70, NeRo75]**: For every `n ≥ 1`, there exists a
graph `G` (on a finite vertex set) that contains no $K_4$ and whose edges cannot be covered by
`n` triangle-free graphs.

More precisely: for every `n : ℕ` with `1 ≤ n`, there exist a finite type `V` and a graph
`G : SimpleGraph V` with:
1. `G.CliqueFree 4` (no $K_4$), and
2. For every family `H : Fin n → SimpleGraph V` of triangle-free graphs, `G ≠ ⨆ i, H i`.

This is the finite analogue of Problem 595. The proofs of Folkman [Fo70] and Nešetřil–Rödl
[NeRo75] give different explicit constructions.
-/
@[category research solved, AMS 5]
theorem erdos_595.variants.folkman_finite : answer(True) ↔
    ∀ n : ℕ, 1 ≤ n →
    ∃ (V : Type*) (_ : Fintype V) (G : SimpleGraph V),
      G.CliqueFree 4 ∧
      ∀ (H : Fin n → SimpleGraph V), (∀ i, (H i).CliqueFree 3) → G ≠ ⨆ i, H i := by
  -- Folkman [Fo70] and Nešetřil–Rödl [NeRo75]: explicit construction exists.
  sorry

/--
**Monotonicity**: If `G` is a countable union of triangle-free graphs and `H ≤ G` (i.e., `H` is
a subgraph of `G`), then `H` is also a countable union of triangle-free graphs.

**Proof**: If `G = ⨆ i, G_i` with each `G_i` triangle-free, then `H = ⨆ i, H ⊓ G_i`.
Each `H ⊓ G_i` is triangle-free because it is a subgraph of `G_i`.
-/
@[category textbook, AMS 5]
theorem erdos_595.variants.subgraph_of_countable_union
    {V : Type*} {G H : SimpleGraph V}
    (hH : H ≤ G) (hG : IsCountableUnionOfTriangleFree G) :
    IsCountableUnionOfTriangleFree H := by
  obtain ⟨f, hf_free, hf_eq⟩ := hG
  refine ⟨fun i => H ⊓ f i, fun i => (hf_free i).anti inf_le_right, ?_⟩
  ext a b
  simp only [iSup_adj, inf_adj]
  constructor
  · intro hab
    have habG : G.Adj a b := hH hab
    rw [hf_eq, iSup_adj] at habG
    obtain ⟨i, hi⟩ := habG
    exact ⟨i, hab, hi⟩
  · rintro ⟨i, hHab, _⟩
    exact hHab

/--
**Triangle-free graphs are trivially countable unions of triangle-free graphs**: if `G` is
already triangle-free, then `G = ⨆ i : ℕ, G_i` where `G_0 = G` and `G_i = ⊥` for `i ≥ 1`.
-/
@[category textbook, AMS 5]
theorem erdos_595.variants.triangle_free_is_union
    {V : Type*} (G : SimpleGraph V) (hG : G.CliqueFree 3) :
    IsCountableUnionOfTriangleFree G := by
  refine ⟨fun i => if i = 0 then G else ⊥, fun i => ?_, ?_⟩
  · by_cases h : i = 0
    · simp [h, hG]
    · simp [h, cliqueFree_bot (by norm_num : 2 ≤ 3)]
  · ext a b
    simp only [iSup_adj]
    constructor
    · intro hab
      exact ⟨0, by simp [hab]⟩
    · rintro ⟨i, hi⟩
      by_cases h : i = 0
      · simp [h] at hi; exact hi
      · simp [h] at hi

/--
**The complete graph `⊤` on `ℕ` is a countable union of triangle-free graphs**: we decompose
it into the family of star graphs `{H_m}_{m : ℕ}`, where `H_m` is the graph with edges `{m, n}`
for all `n ≠ m`. Each star is triangle-free (any two non-center vertices share no edge within
the star), and their union covers all edges of `⊤`.

**Proof sketch (star triangle-free):** If `{a, b, c}` were a triangle in `H_m`, then each of
the three edges `{a, b}`, `{a, c}`, `{b, c}` would pass through `m`. In particular, from
`{a, b}` we 

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
