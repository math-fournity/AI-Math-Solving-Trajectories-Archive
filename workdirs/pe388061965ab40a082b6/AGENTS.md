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
# The Pompeiu problem

Let $\Omega \subset \mathbb{R}^{N+1}$ be a bounded domain. A **rigid motion** is an isometry of
$\mathbb{R}^{N+1}$ (a composition of translations and rotations), modelled here by an
`AffineIsometryEquiv` of Euclidean space with itself.

The domain $\Omega$ has the **Pompeiu property** if the only continuous function
$f : \mathbb{R}^{N+1} \to \mathbb{R}$ with $\int_{\sigma(\Omega)} f = 0$ for every rigid motion
$\sigma$ is $f \equiv 0$.

The **Pompeiu problem** (Pompeiu's conjecture) asserts that, among bounded simply connected
domains with Lipschitz boundary, the Euclidean ball is the *only* domain that **fails** to have
the Pompeiu property. (That a ball fails is classical — radial functions built from Bessel
functions have vanishing integral over every congruent ball; the open direction is the converse.)

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Pompeiu_problem)
- [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Pompeiu_problem)
- [BST73] Brown, L., Schreiber, B. M. and Taylor, B. A., *Spectral synthesis and the Pompeiu
  problem*, Ann. Inst. Fourier 23 (1973), 125–154. (Proves a ball fails the Pompeiu property;
  for a ball of radius `R` the witness is `f(x) = sin(a x₁)` with `J_{n/2}(a R) = 0`.)
- Zalcman, L., *A bibliographic survey of the Pompeiu problem*, in Approximation by
  Solutions of Partial Differential Equations, NATO ASI Ser. 365 (1992), 185–194.
-/

open MeasureTheory Metric Topology

namespace PompeiuProblem

variable {N : ℕ}

/-- A **rigid motion** of $\mathbb{R}^{N+1}$: an affine isometry of Euclidean space onto itself
(a composition of translations and rotations/reflections). -/
abbrev RigidMotion (N : ℕ) :=
  AffineIsometryEquiv ℝ (EuclideanSpace ℝ (Fin (N + 1))) (EuclideanSpace ℝ (Fin (N + 1)))

/-- A set `Ω` has the **Pompeiu property** if the only continuous `f : ℝ^{N+1} → ℝ` whose integral
over every rigid-motion image `σ(Ω)` vanishes is the zero function. -/
def HasPompeiuProperty (Ω : Set (EuclideanSpace ℝ (Fin (N + 1)))) : Prop :=
  ∀ f : EuclideanSpace ℝ (Fin (N + 1)) → ℝ, Continuous f →
    (∀ σ : RigidMotion N, (∫ x in Set.image σ Ω, f x) = 0) → ∀ x, f x = 0

/-- `Ω` is a **Euclidean ball**: an open metric ball of positive radius. -/
def IsBall (Ω : Set (EuclideanSpace ℝ (Fin (N + 1)))) : Prop :=
  ∃ (c : EuclideanSpace ℝ (Fin (N + 1))) (r : ℝ), 0 < r ∧ Ω = Metric.ball c r

/-- `Ω` has **Lipschitz boundary** if every boundary point `p` has a neighbourhood `U` in which,
after some rigid motion `σ` (used to choose a "vertical" axis), `Ω` coincides with the strict
subgraph of a Lipschitz function `g` of the first `N` coordinates: a point `x ∈ U` lies in `Ω`
iff its last coordinate (in the `σ`-frame) is below `g` applied to its first `N` coordinates.
This is the standard definition of a Lipschitz domain. -/
def HasLipschitzBoundary (Ω : Set (EuclideanSpace ℝ (Fin (N + 1)))) : Prop :=
  ∀ p ∈ frontier Ω, ∃ (U : Set (EuclideanSpace ℝ (Fin (N + 1)))),
    U ∈ 𝓝 p ∧ ∃ (σ : RigidMotion N) (K : NNReal) (g : EuclideanSpace ℝ (Fin N) → ℝ),
      LipschitzWith K g ∧
        ∀ x ∈ U, x ∈ Ω ↔ (σ x) (Fin.last N) <
          g ((WithLp.equiv 2 (Fin N → ℝ)).symm (fun i : Fin N => (σ x) i.castSucc))

/-- The domain hypotheses of Pompeiu's problem: `Ω` is bounded, open, connected (a "domain"),
simply connected, and has Lipschitz boundary. -/
structure IsAdmissibleDomain (Ω : Set (EuclideanSpace ℝ (Fin (N + 1)))) : Prop where
  bounded            : Bornology.IsBounded Ω
  isOpen             : IsOpen Ω
  connected          : IsConnected Ω
  simplyConnected    : SimplyConnectedSpace Ω
  lipschitzBoundary  : HasLipschitzBoundary Ω

/--
**Pompeiu's conjecture.** A bounded, simply connected domain in $\mathbb{R}^{N+1}$ with Lipschitz
boundary fails to have the Pompeiu property if and only if it is a Euclidean ball. Equivalently,
the ball is the unique such domain without the Pompeiu property.
-/
@[category research open, AMS 42]
theorem pompeiu_conjecture (Ω : Set (EuclideanSpace ℝ (Fin (N + 1))))
    (hΩ : IsAdmissibleDomain Ω) :
    ¬ HasPompeiuProperty Ω ↔ IsBall Ω := by
  sorry

/--
The classical (easy) direction, proved by Brown–Schreiber–Taylor [BST73]: a Euclidean ball fails
to have the Pompeiu property. For a ball of radius `R`, an explicit witness is `f(x) = sin(a x₁)`
where `a > 0` is chosen so that the Bessel function `J_{n/2}(a R) 

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
