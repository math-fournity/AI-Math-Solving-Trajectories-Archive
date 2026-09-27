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
# Erdős Problem 742

*References:*
- [erdosproblems.com/742](https://www.erdosproblems.com/742)
- [Pl75] Plesník, Ján, Critical graphs of given diameter. Acta Fac. Rerum Natur. Univ. Comenian.
  Math. 30 (1975), 71-93.
- [CaHa79] Caccetta, L. and Häggkvist, R., On diameter critical graphs.
  Discrete Math. 28 (1979), 223-229.
- [Fa87] Fan, Genghua, On diameter 2-critical graphs. Discrete Math. 67 (1987), 235-240.
- [Fü92] Füredi, Zoltán, The maximum number of edges in a minimal graph of diameter 2.
  J. Graph Theory 16 (1992), 81-98.
-/

open SimpleGraph

namespace Erdos742

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- A graph is diameter-2-critical if it has diameter $2$ and removing any edge
increases the diameter beyond $2$. -/
def IsDiameter2Critical (G : SimpleGraph V) : Prop :=
  G.diam = 2 ∧ ∀ e ∈ G.edgeSet, (G.deleteEdges {e}).diam ≠ 2

/--
**Murty-Simon Conjecture**

Let $G$ be a graph on $n$ vertices with diameter $2$ such that deleting any edge increases the
diameter. Is it true that $G$ has at most $\lfloor n^2 / 4 \rfloor$ edges? Equality is conjectured
to hold for the complete balanced bipartite graph $K_{\lceil n/2 \rceil, \lfloor n/2 \rfloor}$.

The conjecture is resolved up to a finite check: Fan [Fa87] verified it for $n \leq 24$ and
$n = 26$, and Füredi [Fü92] proved it for all sufficiently large $n$.
-/
@[category research open, AMS 5]
theorem erdos_742 :
    answer(sorry) ↔ ∀ (V : Type*) [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj], IsDiameter2Critical G →
    G.edgeFinset.card ≤ (Fintype.card V) ^ 2 / 4 := by
  sorry

/--
The complete bipartite graph $K_{a, b}$ has exactly $a \cdot b$ edges. The bound
$\lfloor n^2 / 4 \rfloor$ in the Murty-Simon conjecture is attained by the balanced
case $K_{\lceil n/2 \rceil, \lfloor n/2 \rfloor}$.
-/
@[category test, AMS 5]
theorem complete_bipartite_edge_count (a b : ℕ) :
    (completeBipartiteGraph (Fin a) (Fin b)).edgeSet.ncard = a * b := by
  -- The edge set equals the image of `Fin a × Fin b` under the map
  -- `(i, j) ↦ s(Sum.inl i, Sum.inr j)`.
  let φ : Fin a × Fin b → Sym2 (Fin a ⊕ Fin b) :=
    fun p => s(Sum.inl p.1, Sum.inr p.2)
  have hedge : (completeBipartiteGraph (Fin a) (Fin b)).edgeSet = φ '' Set.univ := by
    ext e
    simp only [φ, Set.mem_image, Set.mem_univ, true_and]
    constructor
    · intro hadj
      induction e using Quot.ind
      rename_i p
      cases p with | mk a b =>
      cases a <;> cases b <;> simp_all [completeBipartiteGraph]
    · rintro ⟨⟨i, j⟩, rfl⟩
      simp [completeBipartiteGraph]
  have hinj : Function.Injective φ := by
    intro ⟨i₁, j₁⟩ ⟨i₂, j₂⟩ h
    simp only [φ, Sym2.eq_iff] at h
    rcases h with ⟨h1, h2⟩ | ⟨h1, _⟩
    · exact Prod.ext (Sum.inl.inj h1) (Sum.inr.inj h2)
    · exact absurd h1 (by simp)
  rw [hedge, Set.ncard_image_of_injective _ hinj, Set.ncard_univ,
    Nat.card_prod, Nat.card_fin, Nat.card_fin]

namespace variants

/--
Plesník [Pl75] proved the bound $|E(G)| < 3n(n-1)/8$ for any diameter-$2$-critical graph
on $n$ vertices.
-/
@[category research solved, AMS 5]
theorem plesnik_bound (G : SimpleGraph V) [DecidableRel G.Adj] (hG : IsDiameter2Critical G) :
    (G.edgeFinset.card : ℝ) < 3 * (Fintype.card V : ℝ) * ((Fintype.card V : ℝ) - 1) / 8 := by
  sorry

/--
Fan [Fa87] verified the Murty-Simon conjecture for all $n \leq 24$ and for $n = 26$.
-/
@[category research solved, AMS 5]
theorem fan_bound (G : SimpleGraph V) [DecidableRel G.Adj]
    (hn : Fintype.card V ≤ 24 ∨ Fintype.card V = 26) (hG : IsDiameter2Critical G) :
    G.edgeFinset.card ≤ (Fintype.card V) ^ 2 / 4 := by
  sorry

/--
Füredi [Fü92] proved the Murty-Simon conjecture for all sufficiently large $n$, that is, there
exists $n_0$ such that every diameter-$2$-critical graph on $n \geq n_0$ vertices has at most
$\lfloor n^2 / 4 \rfloor$ edges.
-/
@[category research solved, AMS 5]
theorem furedi_bound : ∃ n₀ : ℕ, ∀ (V : Type*) [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj],
    n₀ ≤ Fintype.card V → IsDiameter2Critical G →
      G.edgeFinset.card ≤ (Fintype.card V) ^ 2 / 4 := by
  sorry

end variants

end Erdos742


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
