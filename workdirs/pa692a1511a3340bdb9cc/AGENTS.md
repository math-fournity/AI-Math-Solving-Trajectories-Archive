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
# Existence And Smoothness Of The Navier–Stokes Equation

This file formalizes the Clay Mathematics Institute millennium problem concerning
the existence and smoothness of solutions to the Navier-Stokes equations in three
spatial dimensions. While the definitions are generalized to arbitrary dimension n,
the millennium problem specifically concerns the case n = 3.

## References
- [Wikipedia](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness)
- [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)

## Main Theorems (Clay Millennium Problem for n = 3)

The Clay Millennium Problem asks for a proof of one of the following four statements:

- `navier_stokes_existence_and_smoothness_R3`: (A) Global existence on ℝ³
- `navier_stokes_existence_and_smoothness_periodic`: (B) Global existence on ℝ³/ℤ³
- `navier_stokes_breakdown_R3`: (C) Existence of breakdown scenario on ℝ³
- `navier_stokes_breakdown_periodic`: (D) Existence of breakdown scenario on ℝ³/ℤ³

## Variable conventions

Fefferman writes the velocity as $u(x,t)$, the initial velocity as $u^\circ(x)$, the
pressure as $p(x,t)$, the force as $f(x,t)$, and the viscosity as $\nu$. In Lean,
`u₀ : ℝ^n → ℝ^n` denotes the initial velocity, while `v : ℝ^n → ℝ → ℝ^n`
denotes the solution velocity. The curried order `v x t`, `p x t`, and `f x t`
keeps the source convention that position comes before time.

Since the Clay statement gives equation (1) on the closed time half-line $t \ge 0$,
the time derivative is encoded with `derivWithin` relative to `Set.Ici 0`. The Clay
PDF also includes errata; in particular, we include spatial 1-periodicity of the
pressure in the periodic case. The sign correction to the weak-solution identity in
the errata is not represented here, since this file formalizes the four prize
alternatives rather than the later weak-solution discussion.
-/

open ContDiff Set InnerProductSpace MeasureTheory EuclideanGeometry
open scoped Laplacian

namespace NavierStokes

variable {n : ℕ}

/--
The divergence $\nabla \cdot v$ of a vector field $v : \mathbb{R}^n \to \mathbb{R}^n$
at a point $x$, computed as the trace of the Jacobian matrix.

In coordinates, $\nabla \cdot v = \sum_i \partial v_i / \partial x_i$.

This is available as the notation `∇⬝ v`. If `v` is not differentiable at `x`, then
`fderiv` is the zero map, so this definition has the corresponding junk value $0$.
-/
noncomputable
def divergence (v : ℝ^n → ℝ^n) (x : ℝ^n) : ℝ := (fderiv ℝ v x).trace ℝ (ℝ^n)

@[inherit_doc]
notation "∇⬝" => divergence

/-- The divergence of a vector field is $0$ at points where `fderiv` has its junk value. -/
@[simp, category API, AMS 35]
theorem divergence_of_not_differentiableAt {v : ℝ^n → ℝ^n} {x : ℝ^n}
    (hv : ¬ DifferentiableAt ℝ v x) : ∇⬝ v x = 0 := by
  simp [divergence, fderiv_zero_of_not_differentiableAt hv]

/-- The divergence of the zero vector field is zero. -/
@[simp, category API, AMS 35]
theorem divergence_zero (x : ℝ^n) : ∇⬝ (0 : ℝ^n → ℝ^n) x = 0 := by
  simp [divergence]

/-- The divergence of a constant vector field is zero. -/
@[simp, category API, AMS 35]
theorem divergence_const (c : ℝ^n) (x : ℝ^n) :
    ∇⬝ (fun _ : ℝ^n => c) x = 0 := by
  simp [divergence]

/-- Divergence is additive at points where both vector fields are differentiable. -/
@[category API, AMS 35]
theorem divergence_add {v w : ℝ^n → ℝ^n} {x : ℝ^n}
    (hv : DifferentiableAt ℝ v x) (hw : DifferentiableAt ℝ w x) :
    ∇⬝ (fun y => v y + w y) x = ∇⬝ v x + ∇⬝ w x := by
  rw [divergence, fderiv_fun_add hv hw]
  exact map_add _ _ _

/-- Divergence commutes with scalar multiplication at differentiability points. -/
@[category API, AMS 35]
theorem divergence_smul (c : ℝ) {v : ℝ^n → ℝ^n} {x : ℝ^n}
    (hv : DifferentiableAt ℝ v x) : ∇⬝ (fun y => c • v y) x = c * ∇⬝ v x := by
  rw [divergence, fderiv_fun_const_smul hv c]
  simp [divergence]

/--
A function $f : \mathbb{R}^n \to \alpha$ is 1-periodic if it is periodic in each
coordinate with period $1$, i.e. $f(x + e_i) = f(x)$ for each unit vector $e_i$.
This captures functions on the $n$-torus $\mathbb{R}^n/\mathbb{Z}^n$.
-/
def IsOnePeriodic {α : Sort*} (f : ℝ^n → α) : Prop :=
  ∀ x i, f (x + EuclideanSpace.single i 1) = f x

/--
Basic conditions on initial velocity field for the Navier-Stokes equations
in $n$-dimensional space.

The initial velocity must be:


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
