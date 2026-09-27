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
# Erdős Problem 1175

*Reference:* [erdosproblems.com/1175](https://www.erdosproblems.com/1175)

## Formalization notes

- **Chromatic cardinal**: `SimpleGraph.chromaticCardinal` is the cardinal-valued chromatic number
  defined in `FormalConjecturesForMathlib`. It extends the finite `chromaticNumber` (which takes
  values in `ℕ∞`) to a `Cardinal`, and is therefore able to distinguish between different infinite
  chromatic numbers.
- **Triangle-free subgraph**: a subgraph `H : G.Subgraph` is triangle-free when `H.coe.CliqueFree 3`.
  This is the standard Mathlib formulation: `CliqueFree 3` means the graph has no `K₃` as a clique.
- **Subgraph**: we use `G.Subgraph` (a spanning subgraph record) rather than an induced subgraph
  since the problem asks for any subgraph, not just induced ones.
-/

open Cardinal SimpleGraph

namespace Erdos1175

/--
Let $\kappa$ be an uncountable cardinal. Must there exist a cardinal $\lambda$ such that every
graph with chromatic number $\lambda$ contains a triangle-free subgraph with chromatic number
$\kappa$?

Shelah proved that a negative answer is consistent when
$\kappa = \lambda = \aleph_1$ (see `erdos_1175.variants.shelah_consistency`).
-/
@[category research open, AMS 5]
theorem erdos_1175 : answer(sorry) ↔
    ∀ (κ : Cardinal), ℵ₀ < κ →
      ∃ (μ : Cardinal),
        ∀ (V : Type*) (G : SimpleGraph V), G.chromaticCardinal = μ →
          ∃ (H : G.Subgraph), H.coe.CliqueFree 3 ∧ H.coe.chromaticCardinal = κ := by
  sorry

/--
**Shelah's consistency result**: it is consistent with ZFC that there exists a graph $G$ with
chromatic number $\aleph_1$ such that every triangle-free subgraph of $G$ has chromatic number
strictly less than $\aleph_1$.

This shows that a negative answer to Problem 1175 (with $\kappa = \lambda = \aleph_1$) is
consistent, so the main statement `erdos_1175` is not provable in ZFC.

**Formalization caveat (consistency placeholder).** Shelah's result is a *consistency*
statement — it asserts the existence of a model of ZFC, not a ZFC theorem. Lean operates
inside a single (fixed) model of its set theory, so we cannot directly express "consistent
with ZFC" without leaving ZFC. Rather than pretend that Shelah's theorem is a bare ZFC
negation, we record it here as an explicit `answer(sorry)` consistency placeholder: the
intended conjecture is the model-theoretic statement, and any concrete formalisation must
either appeal to an explicit extra axiom (such as Shelah's specific forcing extension)
or to a meta-theoretic consistency proof. Until such a wrapper exists in `FormalConjectures`,
we leave the body as `sorry`.
-/
@[category research solved, AMS 5]
theorem erdos_1175.variants.shelah_consistency : answer(sorry) ↔
    ¬ (∀ (V : Type*) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 →
         ∃ (H : G.Subgraph), H.coe.CliqueFree 3 ∧ H.coe.chromaticCardinal = ℵ_ 1) := by
  sorry

/--
**Threshold reformulation variant.** Replaces `chromaticCardinal = λ` in the hypothesis
of `erdos_1175` with `λ ≤ chromaticCardinal` (a graph of chromatic number ≥ λ has a
triangle-free subgraph of chromatic number κ). This is a strengthening of `erdos_1175`
(see `erdos_1175.test.threshold_implies_exact`).
-/
@[category research open, AMS 5]
theorem erdos_1175.variants.threshold_formulation : answer(sorry) ↔
    ∀ (κ : Cardinal), ℵ₀ < κ →
      ∃ (μ : Cardinal),
        ∀ (V : Type*) (G : SimpleGraph V), μ ≤ G.chromaticCardinal →
          ∃ (H : G.Subgraph), H.coe.CliqueFree 3 ∧ H.coe.chromaticCardinal = κ := by
  sorry

/- ## Sanity checks -/

/-- Every graph has a triangle-free subgraph: the bottom subgraph (with no edges)
witnesses triangle-freeness, so the existential
`∃ H : G.Subgraph, H.coe.CliqueFree 3` in `erdos_1175` is non-vacuous. -/
@[category test, AMS 5]
theorem erdos_1175.test.exists_triangle_free_subgraph
    (V : Type*) (G : SimpleGraph V) : ∃ H : G.Subgraph, H.coe.CliqueFree 3 :=
  ⟨⊥, by simp [SimpleGraph.cliqueFree_bot (by norm_num : 2 ≤ 3)]⟩

/-- The threshold variant `threshold_formulation` is stronger than the exact-equality
form `erdos_1175`: if every graph with `chromaticCardinal ≥ μ` has the desired
triangle-free subgraph, then in particular every graph with `chromaticCardinal = μ`
does too. -/
@[category test, AMS 5]
theorem erdos_1175.test.threshold_implies_exact :
    (∀ (κ : Cardinal.{0}), ℵ₀ < κ →
      ∃ (μ : Cardinal.{0}),
        ∀ (V : Typ

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
