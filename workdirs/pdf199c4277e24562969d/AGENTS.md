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
# Is Every Convex Polyhedron Rupert?

A polyhedron is Rupert if one can cut a hole in it and pass another
copy of the same polyhedron through that hole.

More formally: a convex body in ℝ³ is a compact, convex set with
nonempty interior. A convex body X is said to be Rupert if there are
two affine transforms T₁, T₂ ∈ SE(3) such that π(T₁(X)) ⊆
int(π(T₂(X))), where π : ℝ³ → ℝ² is the evident projection, and int
denotes topological interior.

Not all convex bodies are Rupert. For example,
- the unit ball is not Rupert
- the circular cylinder of unit diameter and height
  closed on each end by disks is not Rupert

However, many convex polyhedra are Rupert. All Platonic solids, and
most Archimedean and Catalan solids are known to be Rupert.

Question: are all convex polyhedra with nonempty interior Rupert?

*References:*

* [Platonic Passages](https://www.researchgate.net/publication/314715434_Platonic_Passages),
  R. P. Jerrard, J. E. Wetzel, and L. Yuan., Math. Mag., 90(2):87–98,
  2017. conjectures ("with a certain hesitancy") that perhaps all
  convex polyhedra are Rupert.

* However, [An Algorithmic Approach to Rupert's Problem](https://arxiv.org/pdf/2112.13754#cite.JeWeYu17)
  describes experimental evidence to suggest that three Archimedean
  solids may not be Rupert.

* [Optimizing for the Rupert property](https://arxiv.org/abs/2210.00601)
  is the source of some of the Catalan solid results, and has more
  results for Johnson polyhedra as well.

* [This video by David Renshaw](https://www.youtube.com/watch?v=evKFok65t_E) visualizes
  known results for Platonic, Archimedean, and Catalan solids.

* This problem's name comes from the fact that it is a generalization
  of [Prince Rupert's Cube](https://en.wikipedia.org/wiki/Prince_Rupert%27s_cube).

* [A convex polyhedron without Rupert's property](https://arxiv.org/abs/2508.18475),
  Jakob Steininger and Sergey Yurkevich, 2025. Constructs a convex polyhedron and
  a proof that it is not Rupert, resolving the open question.

-/

namespace Rupert

open scoped Matrix

abbrev SO3 := Matrix.specialOrthogonalGroup (Fin 3) ℝ

scoped notation "ℝ²" => Fin 2 → ℝ
scoped notation "ℝ³" => Fin 3 → ℝ

/--
The result of transforming a subset of ℝ³ by a chosen rotation and offset,
and then projected to ℝ².
-/
def transformed_shadow (X : Set ℝ³) (offset : ℝ²) (rotation : SO3) : Set ℝ² :=
  (fun p ↦ offset + (rotation *ᵥ p) ∘ Fin.castSucc) '' X

/--
A convex polyhedron (given as a finite collection of vertices) is Rupert if
there are two rotations in ℝ³ (called "inner" and "outer") and a translation in ℝ²
such that the "inner shadow" (the projection to ℝ² of the inner rotation applied
to the polyhedron, then translated) fits in the interior of the "outer shadow"
(the projection to ℝ² of the outer rotation applied to the polyhedron)

[Note: The restriction to (polyhedra determined by the convex hulls of)
*finite* sets of vertices here is deliberate. Were we to generalize to
arbitrary subsets of ℝⁿ we'd probably want to make the containment
relation more strict, e.g.
  closure inner_shadow ⊆ interior outer_shadow
to rule out, e.g. the open ball being Rupert. However, we didn't
observe any such generalization in the literature yet, so we stuck to
what was in the citations above.]
-/
def IsRupert (vertices : Finset ℝ³) : Prop :=
   ∃ (inner_rotation : SO3) (inner_offset : ℝ²) (outer_rotation : SO3),
   let inner_shadow := transformed_shadow (convexHull ℝ vertices) inner_offset inner_rotation
   let outer_shadow := transformed_shadow (convexHull ℝ vertices) 0 outer_rotation
   inner_shadow ⊆ interior outer_shadow

/--
There exists a convex polyhedron with nonempty interior for which the Rupert property does
not hold.
-/
@[category research solved, AMS 52, formal_proof using lean4 at "https://github.com/jcreedcmu/Noperthedron"]
theorem is_every_convex_polyhedron_rupert :
    answer(False) ↔ ∀ (vertices : Finset ℝ³),
       (interior (convexHull ℝ vertices : Set ℝ³)).Nonempty → IsRupert vertices := by
 sorry


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
