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
# Erdős Problem 593

*References:*
- [erdosproblems.com/593](https://www.erdosproblems.com/593)
- [EGH75] Erdős, Paul and Galvin, Fred and Hajnal, András, On set-systems having large
  chromatic number and not containing prescribed subsystems.
  Infinite and finite sets (Colloq., Keszthely, 1973; dedicated to P. Erdős on his 60th
  birthday), Vol. I. Colloq. Math. Soc. János Bolyai 10, North-Holland (1975), 425–513.
- [Er95d] Erdős, Paul, Some of my favourite problems in various branches of combinatorics.
  Matematiche (Catania) 47 (1992), no. 2, 231–240 (1995).
-/

open Cardinal Set SimpleGraph

namespace Erdos593

/- ## Main open problem -/

/--
**Erdős Problem 593 ($500)**: Characterize those finite 3-uniform hypergraphs which appear
in every 3-uniform hypergraph of chromatic number $> \aleph_0$.

A natural conjectural characterization, recorded here, is that the obligatory finite 3-uniform
hypergraphs are exactly the 2-colorable ones (Property B). The forward direction
(`IsObligatory → IsTwoColorable`) and converse (`IsTwoColorable → IsObligatory`) are stated as
separate variants below; in the graph case ($r = 2$), Erdős–Galvin–Hajnal [EGH75] proved the
analogous result (obligatory ⇔ bipartite).
-/
@[category research open, AMS 5]
theorem erdos_593 : answer(sorry) ↔
    ∀ (W : Type) [Fintype W] (F : ThreeUniformHypergraph W),
      IsObligatory F ↔ F.IsTwoColorable := by
  sorry

/--
**Erdős Problem 593 — Necessary direction**: Every obligatory finite 3-uniform
hypergraph is 2-colorable.

This is the natural necessary condition for the conjectural characterization in `erdos_593`:
if a finite 3-uniform hypergraph `F` is not 2-colorable, one expects to construct a
hypergraph with large chromatic number that contains no copy of `F`.
-/
@[category research open, AMS 5]
theorem erdos_593.variants.obligatory_implies_two_colorable : answer(sorry) ↔
    ∀ (W : Type) [Fintype W] (F : ThreeUniformHypergraph W),
      IsObligatory F → F.IsTwoColorable := by
  sorry

/--
**Erdős Problem 593 — Sufficient direction**: Every finite 2-colorable 3-uniform
hypergraph is obligatory.

This is the converse direction of the `erdos_593` characterization: if 2-colorability
matches the graph-case characterization (bipartite ⇔ obligatory), then every 2-colorable
finite 3-uniform hypergraph must appear in every 3-uniform hypergraph of chromatic number
$> \aleph_0$.

Together with `erdos_593.variants.obligatory_implies_two_colorable`, this implies `erdos_593`.
-/
@[category research open, AMS 5]
theorem erdos_593.variants.two_colorable_implies_obligatory : answer(sorry) ↔
    ∀ (W : Type) [Fintype W] (F : ThreeUniformHypergraph W),
      F.IsTwoColorable → IsObligatory F := by
  sorry

/--
**Conjunction of the two open implications gives the conjectured characterization**: if both
`obligatory_implies_two_colorable` and `two_colorable_implies_obligatory` hold, then the
characterization conjectured in `erdos_593` (`IsObligatory F ↔ F.IsTwoColorable`) follows by
elementary `Iff` manipulation.
-/
@[category test, AMS 5]
theorem erdos_593.variants.implications_combine
    (h₁ : ∀ (W : Type) [Fintype W] (F : ThreeUniformHypergraph W),
            IsObligatory F → F.IsTwoColorable)
    (h₂ : ∀ (W : Type) [Fintype W] (F : ThreeUniformHypergraph W),
            F.IsTwoColorable → IsObligatory F) :
    ∀ (W : Type) [Fintype W] (F : ThreeUniformHypergraph W),
      IsObligatory F ↔ F.IsTwoColorable := by
  intro W _ F
  exact ⟨h₁ W F, h₂ W F⟩

/- ## Variants and partial results -/

/--
**Graph analogue — bipartite graphs are obligatory (Erdős–Galvin–Hajnal [EGH75])**:
For the 2-uniform (graph) case, a graph of chromatic cardinal $> \aleph_0$ must contain all
finite bipartite graphs. Specifically, for every finite bipartite graph `F` and every graph
`G` with chromatic cardinal $> \aleph_0$, there is a graph embedding from `F` into `G`.

This uses `Nonempty (F ↪g G)` (graph embedding), aligned with the injective vertex map
used in the hypergraph `Appears` definition.
-/
@[category research solved, AMS 5]
theorem erdos_593.variants.graph_case_bipartite_obligatory :
    answer(True) ↔
    ∀ (V : Type*) (G : SimpleGraph V),
      ℵ₀ < G.chromaticCardinal →
      ∀ (W : Type*) [Fintype W] (F : SimpleGraph W), F.IsBipartite →
        Nonempty (F ↪g G) := by
  simp only [true_iff]
  -- This is the Erdős–Galvin–Hajnal theorem [EGH75].
  sorry

/--


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
