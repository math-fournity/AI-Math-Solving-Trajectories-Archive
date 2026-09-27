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
import FormalConjecturesForMathlib.Combinatorics.SimpleGraph.HomDensity

/-!
# Sidorenko's conjecture (1993)

*References:*
* [Wikipedia](https://en.wikipedia.org/wiki/Sidorenko%27s_conjecture)
* [Si93] Sidorenko, A. (1993). "A correlation inequality for bipartite graphs."
  *Graphs Combin.* 9, pp. 201--204.
* [CoFo10] Conlon, D. and Fox, J. (2010). "Bounds for graph regularity and removal lemmas."
  *Geom. Funct. Anal.* 22, pp. 1191--1256.
* [KLL18] Kim, J.H., Lee, C., Lee, J. (2018). "Two approaches to Sidorenko's conjecture."
  *Trans. Amer. Math. Soc.* 370, pp. 8515--8552.
-/

open Finset SimpleGraph

namespace SidorenkoConjecture

/- ## Homomorphism density

We use `SimpleGraph.homCount` / `SimpleGraph.homDensity` from
`FormalConjecturesForMathlib.Combinatorics.SimpleGraph.HomDensity`. The extension to
infinite hosts uses the same formula with `Fintype.card` replaced by measure-theoretic
integrals; we do not need that generality for Sidorenko. -/

variable {V W : Type*}

/- ## The conjecture -/

/--
**Sidorenko's conjecture (1993).**

For every finite bipartite simple graph $H$ and every finite simple graph $G$:
$t(H, G) \ge t(K_2, G)^{e(H)}$, where $K_2$ denotes the single-edge graph on 2 vertices
(i.e. `completeGraph (Fin 2)`).
-/
@[category research open, AMS 5]
theorem sidorenko_conjecture : answer(sorry) ↔
    ∀ {V W : Type} [Fintype V] [Fintype W] [DecidableEq V] [DecidableEq W] [Nonempty W]
      (H : SimpleGraph V) (G : SimpleGraph W)
      [DecidableRel H.Adj] [DecidableRel G.Adj],
      H.IsBipartite →
      homDensity (completeGraph (Fin 2)) G ^ H.edgeFinset.card ≤ homDensity H G := by
  sorry

/- ## Proved special cases -/

/--
**Case `H = K_2` (single edge): Sidorenko's inequality holds trivially with equality.**

When `H` is `K_2` (the single-edge graph on 2 vertices), `e(H) = 1`, so the RHS of Sidorenko's
inequality is just `t(K_2, G)^1 = t(K_2, G) = t(H, G)`, which equals the LHS. Hence the
inequality holds as equality.

The proof records that `(completeGraph (Fin 2)).edgeFinset.card = 1` and then reduces the claim
to `t(K_2, G) ≤ t(K_2, G)`, which is `le_refl`.
-/
@[category research solved, AMS 5]
theorem sidorenko_K2 {W : Type} [Fintype W] [DecidableEq W]
    (G : SimpleGraph W) [DecidableRel G.Adj] :
    homDensity (completeGraph (Fin 2)) G ^
      ((completeGraph (Fin 2)).edgeFinset.card) ≤
      homDensity (completeGraph (Fin 2)) G := by
  -- `(completeGraph (Fin 2)).edgeFinset.card = 1`, so the inequality is `x^1 ≤ x`, i.e. `x ≤ x`.
  have hK2 : (completeGraph (Fin 2)).edgeFinset.card = 1 := by
    rw [SimpleGraph.card_edgeFinset_completeGraph_fin, Nat.choose_self]
  rw [hK2, pow_one]

/- ## Sidorenko for `K_{2,2}`: auxiliary lemmas -/

open scoped Classical in
/-- `edgeCount` of `K_{2,2}` (complete bipartite graph on `Fin 2 + Fin 2`) is `4`.

The four edges are `{inl 0, inr 0}`, `{inl 0, inr 1}`, `{inl 1, inr 0}`, `{inl 1, inr 1}`. -/
@[category API, AMS 5]
lemma edgeCount_completeBipartiteGraph_fin_two :
    (completeBipartiteGraph (Fin 2) (Fin 2)).edgeFinset.card = 4 := by
  -- Every vertex of `K_{2,2}` has degree 2, and there are 4 vertices; so by the
  -- handshake formula `2 * #E = ∑ deg = 4 * 2 = 8`, hence `#E = 4`.
  have hdeg : ∀ v : Fin 2 ⊕ Fin 2, (completeBipartiteGraph (Fin 2) (Fin 2)).degree v = 2 := by
    intro v
    rw [show (completeBipartiteGraph (Fin 2) (Fin 2)).degree v =
        ((completeBipartiteGraph (Fin 2) (Fin 2)).neighborFinset v).card from rfl]
    cases v with
    | inl i =>
      -- Neighbours of `inl i`: exactly `{inr 0, inr 1}`.
      rw [neighborFinset_eq_filter]
      rw [show (Finset.univ : Finset (Fin 2 ⊕ Fin 2)).filter
          (fun w => (completeBipartiteGraph (Fin 2) (Fin 2)).Adj (Sum.inl i) w)
          = {Sum.inr (0 : Fin 2), Sum.inr (1 : Fin 2)} from ?_]
      · decide
      · ext w
        cases w with
        | inl k =>
          simp [completeBipartiteGraph_adj]
        | inr k =>
          simp [completeBipartiteGraph_adj]
          fin_cases k <;> decide
    | inr j =>
      rw [neighborFinset_eq_filter]
      rw [show (Finset.univ : Finset (Fin 2 ⊕ Fin 2)).filter
          (fun w => (completeBipartiteGraph (Fin 2) (Fin 2)).Adj (Sum.inr j) w)
          = {Sum.inl (0 : Fin 2), Sum.inl (1 : Fin 2)} from ?_]
      · decide
      · ext w
        cases w with
        | inl k =>
          simp [completeBipartiteGraph_adj]
          fin_case

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
