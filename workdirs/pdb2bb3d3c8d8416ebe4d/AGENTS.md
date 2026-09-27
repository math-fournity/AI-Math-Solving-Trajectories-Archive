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
# Conjectures around homogeneous topological spaces

This file formalizes the notion of a weakly first countable topological space and some conjectures
around those.

*References:*
* [Ar2013] Arhangeliski, Alexandr. "Selected old open problems in general topology."
  Buletinul Academiei de Ştiinţe a Republicii Moldova. Matematica 73.2-3 (2013): 37-46.
  https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf
-/

open TopologicalSpace Topology Filter Set
open scoped Cardinal

namespace Homogeneous

/--
A topological space $X$ is called *homogeneous* if for all $x, y \in X$ there is homeomorphism
$f : X \to X$ with $f(x) = y$.
-/
class HomogeneousSpace (X : Type*) [TopologicalSpace X] : Prop where
  exists_equiv : ∀ x y : X, ∃ f : X ≃ₜ X, f x = y

/-- Every discrete space is homogeneous. -/
@[category test, AMS 54]
instance DiscreteTopology.toHomogeneousSpace (X : Type*) [TopologicalSpace X] [DiscreteTopology X] :
    HomogeneousSpace X where
  exists_equiv x y := by
    classical
    use IsHomeomorph.homeomorph (Equiv.swap x y)
      (IsHomeomorph.equiv_of_discreteTopology (Equiv.swap x y))
    rw [IsHomeomorph.homeomorph_apply, Equiv.swap_apply_left]

/-- Problem 13 in [Ar2013]:
Is it true that every infinite homogeneous compact hausdorff
space contains a non-trivial convergent sequence? -/
@[category research open, AMS 54]
theorem homogeneousSpace_exists_inj_tendsto :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), ¬ Finite X → T2Space X → CompactSpace X →
      HomogeneousSpace X → ∃ s : ℕ → X, s.Injective ∧ ∃ a : X, Tendsto s atTop (nhds a) := by
  sorry

/-- Problem 14 in [Ar2013]:
Is it possible to represent an arbitrary compact hausdorff space as an image
of a homogeneous compact space under a continuous mapping? -/
@[category research open, AMS 54]
theorem homogeneousSpace_exists_surjective :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      ∃ (Y : Type) (_ : TopologicalSpace Y), T2Space Y ∧ CompactSpace Y ∧ HomogeneousSpace Y ∧
        ∃ f : Y → X, Continuous f ∧ f.Surjective := by
  sorry

/-- A topological space is called ω-monolithic if
the closure of every countable subspace is metrizable. -/
class CountablyMonolithicSpace (X : Type*) [TopologicalSpace X] : Prop where
  metrizable_of_closure_of_countable : ∀ ⦃s : Set X⦄, s.Countable → MetrizableSpace (closure s)

/-- Every Metrizable space is ω-monolithic. -/
@[category test, AMS 54]
instance MetrizableSpace.countablyMonolithicSpace
    (X : Type*) [TopologicalSpace X] [MetrizableSpace X] : CountablyMonolithicSpace X := by
  refine { metrizable_of_closure_of_countable := ?_ }
  intros
  infer_instance

/-- Problem 15 in [Ar2013]:
Is every homogeneous ω-monolithic compact hausdorff space first countable? -/
@[category research open, AMS 54]
theorem firstCountableTopology_of_countablyMonolithicSpace :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      HomogeneousSpace X → CountablyMonolithicSpace X → FirstCountableTopology X := by
  sorry

/-- Problem 16 in [Ar2013]:
Is the cardinality of every homogeneous ω-monolithic compact hausdorff space not greater than 𝔠? -/
@[category research open, AMS 54]
theorem countablyMonolithicSpace_card_lt :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      HomogeneousSpace X → CountablyMonolithicSpace X → #X ≤ 𝔠 := by
  sorry

/-- Problem 17 in [Ar2013]:
Is it true that every nonempty ω-monolithic compact hausdorff space contains a point with a
first countable neighborhood basis?

Note: `Nonempty X` is required since the conclusion asserts the existence of a point.
-/
@[category research open, AMS 54]
theorem countablyMonolithicSpace_exists_nhds_generated_countable :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      Nonempty X → CountablyMonolithicSpace X → ∃ x : X, (𝓝 x).IsCountablyGenerated := by
  sorry

end Homogeneous


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
