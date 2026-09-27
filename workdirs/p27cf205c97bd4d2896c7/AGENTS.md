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
# Gottschalk's surjunctivity conjecture

A group $G$ is *surjunctive* if every injective, continuous, $G$-equivariant map
$A^G \to A^G$ (for any finite alphabet $A$) is surjective.

Here equivariance is with respect to the left shift action of $G$ on $A^G$,
defined by $(g \cdot x)(h) = x(g^{-1} h)$, and continuity is with respect to
the product topology on $A^G$ (where $A$ carries the discrete topology).

Gottschalk's conjecture (1973) states that every group is surjunctive.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Surjunctive_group)
- Gottschalk, W. H. (1973), "Some general dynamical notions"
-/

namespace GottschalkSurjunctivity

variable (G : Type*) [Group G]

/-- The left shift of `x : G → A` by `g : G`, defined by `(shift g x)(h) = x(g⁻¹ * h)`.
This is the standard left shift action of `G` on `A^G`. We define it as a plain function
rather than a `MulAction` instance to avoid conflict with the pointwise `Pi.instMulAction`. -/
def shift {A : Type*} (g : G) (x : G → A) : G → A :=
  fun h => x (g⁻¹ * h)

@[simp, category API, AMS 20 37]
theorem shift_apply {A : Type*} (g : G) (x : G → A) (h : G) :
    shift G g x h = x (g⁻¹ * h) := rfl

@[simp, category API, AMS 20 37]
theorem shift_one {A : Type*} (x : G → A) :
    shift G 1 x = x := by
  ext h; simp [shift]

@[category API, AMS 20 37]
theorem shift_mul {A : Type*} (g₁ g₂ : G) (x : G → A) :
    shift G (g₁ * g₂) x = shift G g₁ (shift G g₂ x) := by
  ext h; simp [shift, mul_assoc]

/-- A map `τ : (G → A) → (G → A)` is *equivariant* (with respect to the left shift action)
if `τ(shift g x) = shift g (τ x)` for all `g : G` and `x : G → A`. -/
def IsShiftEquivariant {A : Type*} (τ : (G → A) → (G → A)) : Prop :=
  ∀ (g : G) (x : G → A), τ (shift G g x) = shift G g (τ x)

/-- A group `G` is *surjunctive* if for every finite nonempty type `A`, every injective,
continuous, shift-equivariant map `(G → A) → (G → A)` is also surjective.

Continuity is with respect to the product topology on `G → A` where `A` carries the
discrete topology. -/
def IsSurjunctive : Prop :=
  ∀ (A : Type) [Fintype A] [Nonempty A] [TopologicalSpace A] [DiscreteTopology A]
    (τ : (G → A) → (G → A)),
    Continuous τ →
    IsShiftEquivariant G τ →
    Function.Injective τ →
    Function.Surjective τ

/-- **Gottschalk's surjunctivity conjecture** (1973): every group is surjunctive.
That is, for every group `G` and every finite alphabet `A`, every injective cellular
automaton on `A^G` is surjective. -/
@[category research open, AMS 20 37]
theorem gottschalk_surjunctivity_conjecture (G : Type) [Group G] :
    IsSurjunctive G := by
  sorry

/-- Every finite group is surjunctive. This is a classical result: an injective
endomorphism of a finite set is surjective. -/
@[category textbook, AMS 20 37]
theorem isSurjunctive_of_finite (G : Type) [Group G] [Finite G] :
    IsSurjunctive G := by
  intro A _ _ _ _ τ _ _ hInj
  exact Finite.surjective_of_injective hInj

end GottschalkSurjunctivity


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
