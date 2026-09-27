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
# Moving Sofa Problem

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Moving_sofa_problem)
- [Ge92] Gerver, J. L., _On moving a sofa around a corner_. Geometriae Dedicata 42.3 (1992): 267-283.
- [Ro18] Romik, D. _Differential equations and exact solutions in the moving sofa problem_. Experimental mathematics 27.3 (2018): 316-330.
- [Ba24] Baek, J. _Optimality of Gerver's Sofa_. arXiv preprint arXiv:2411.19826 (2024).
-/

noncomputable section

namespace MovingSofa

open Topology
open scoped Real unitInterval EuclideanGeometry

/-- The **horizontal side** of the hallway is $(-\infty, 1] \times [0, 1]$. -/
def horizontalHallway : Set ℝ² := {!₂[x, y] | (x) (y) (_ : x ≤ 1 ∧ 0 ≤ y ∧ y ≤ 1)}

/-- The **vertical side** of the hallway is $[0, 1] \times (-\infty, 1]$. -/
def verticalHallway : Set ℝ² := {!₂[x, y] | (x) (y) (_ : 0 ≤ x ∧ x ≤ 1 ∧ y ≤ 1)}

/-- The **hallway** is the union of its horizontal and vertical sides. -/
def hallway : Set ℝ² := horizontalHallway ∪ verticalHallway

scoped notation "E(2)" => ℝ² ≃ᵃⁱ[ℝ] ℝ²

instance : TopologicalSpace E(2) :=
  .induced (·.toAffineIsometry.toContinuousAffineMap) inferInstance

/--
A connected closed set $s$ is a **moving sofa** according to a rigid motion $m:I\to\mathrm{SE}(2)$,
if the sofa is initially in the horizontal side of the hallway and ends up in the vertical side.
Here, since $\mathrm{SE}(2)$ is not in Mathlib yet, we use $\mathrm{E}(2)$ and rely on continuity
and $m(0) = \mathrm{id}$ to ensure $m$ is in $\mathrm{SE}(2)$.
-/
structure IsMovingSofa (s : Set ℝ²) (m : I → E(2)) : Prop where
  isConnected : IsConnected s
  isClosed : IsClosed s
  continuous : Continuous m
  zero : m 0 = .refl ℝ ℝ²
  initial : s ⊆ horizontalHallway
  subset_hallway : ∀ t, m t '' s ⊆ hallway
  final : m 1 '' s ⊆ verticalHallway

/-- The unit square. -/
def unitSquare : Set ℝ² := parallelepiped (EuclideanSpace.basisFun (Fin 2) ℝ)

/-- Coordinates of points in the unit square lie in `[0,1]`. -/
@[category API, AMS 49]
private lemma mem_Icc_of_mem_unitSquare {p : ℝ²} (hp : p ∈ unitSquare) (i : Fin 2) :
    p i ∈ Set.Icc (0:ℝ) 1 := by
  have h := parallelepiped_basis_eq (EuclideanSpace.basisFun (Fin 2) ℝ).toBasis
  rw [unitSquare, show parallelepiped ⇑(EuclideanSpace.basisFun (Fin 2) ℝ) =
    parallelepiped (EuclideanSpace.basisFun (Fin 2) ℝ).toBasis by
      rw [OrthonormalBasis.coe_toBasis], h] at hp
  simpa using hp i

/--
The unit square $[0,1]^2$ is a valid moving sofa (with the identity motion).
It sits in the corner where both hallways overlap, so the stationary motion works.
This is a sanity check that the `IsMovingSofa` definition is not vacuous.
-/
@[category test, AMS 49]
theorem isMovingSofa_unitSquare : ∃ m, IsMovingSofa unitSquare m := by
  refine ⟨fun _ => .refl ℝ ℝ², ?_, ?_, continuous_const, rfl, ?_, ?_, ?_⟩
  · unfold unitSquare parallelepiped
    refine ⟨⟨0, 0, by simp, by simp⟩, (convex_Icc _ _).isPreconnected.image _ ?_⟩
    exact (continuous_finset_sum _ fun i _ =>
      (continuous_apply i).smul continuous_const).continuousOn
  · unfold unitSquare parallelepiped
    exact (isCompact_Icc.image
      (continuous_finset_sum _ fun i _ =>
        (continuous_apply i).smul continuous_const)).isClosed
  · intro p hp
    have h0 := mem_Icc_of_mem_unitSquare hp 0
    have h1 := mem_Icc_of_mem_unitSquare hp 1
    exact ⟨p 0, p 1, ⟨h0.2.trans (by norm_num), h1.1, h1.2⟩,
      by ext i; fin_cases i <;> rfl⟩
  · rintro t q ⟨p, hp, rfl⟩
    rw [show (AffineIsometryEquiv.refl ℝ ℝ²) p = p from rfl]
    refine .inl ?_
    have h0 := mem_Icc_of_mem_unitSquare hp 0
    have h1 := mem_Icc_of_mem_unitSquare hp 1
    exact ⟨p 0, p 1, ⟨h0.2.trans (by norm_num), h1.1, h1.2⟩,
      by ext i; fin_cases i <;> rfl⟩
  · rintro q ⟨p, hp, rfl⟩
    rw [show (AffineIsometryEquiv.refl ℝ ℝ²) p = p from rfl]
    have h0 := mem_Icc_of_mem_unitSquare hp 0
    have h1 := mem_Icc_of_mem_unitSquare hp 1
    exact ⟨p 0, p 1, ⟨h0.1, h0.2, h1.2.trans (by norm_num)⟩,
      by ext i; fin_cases i <;> rfl⟩

/--
The rigid motion that translates by $p$ and then rotates counterclockwise by $\alpha$.
Note that [Ge92] used this definition while [Ro18] used rotation first and then translation.
-/
def rotateTranslate (α : Real.Angle) (p : ℝ²) : E(2) :=
  (EuclideanGeometry.o.rotation α).toAffineIsometryEquiv
    |>.trans (AffineIsometryEquiv.vaddConst ℝ p)

/--
The sofa according to a rotation path $p 

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
