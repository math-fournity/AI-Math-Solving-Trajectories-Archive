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
# Ben Green's Open Problem 57

*Reference:* [Ben Green's Open Problem 57](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.8)

Let $G$ be a finite abelian group. Consider the space $\Phi(G)$ of all functions on $G$ which
are "convex combinations" (in the sense of complex coefficients $c_i$ with
$\sum |c_i| \le 1$) of functions of the form
$$\phi(g) := \mathbb{E}_{x_1 + x_2 + x_3 = g} f_1(x_2, x_3) f_2(x_1, x_3) f_3(x_1, x_2)$$
with $\|f_i\|_\infty \le 1$ (where $f_i : G \times G \to \mathbb{C}$).

Let $\Phi'(G)$ be the space defined similarly, but with $f_3(x_1, x_2)$ required to be
a function of $x_1 + x_2$. Do $\Phi(G)$ and $\Phi'(G)$ coincide?

**Note:** The "convex combination" here uses complex coefficients whose absolute values sum to
at most 1 (cf. personal communication with B. Green, April 2026). Since the base sets are
balanced (closed under multiplication by unit complex numbers), this absolutely convex hull
equals the real convex hull of the complex-valued base set.

**Motivation:** $\Phi(G)$ is a 'generalised convolution algebra' as considered by
Conlon–Fox–Zhao, whereas $\Phi'(G)$ consists of Tao's $\text{UAP}_2(G)$-functions.
-/

namespace Green57

open scoped Pointwise

noncomputable section

variable (G : Type*) [AddCommGroup G] [Fintype G] [DecidableEq G]

/-- Uniform average over pairs `(x₁, x₂)` in `G × G`, with the third variable determined by
the relation `x₁ + x₂ + x₃ = g`. The functions `fᵢ` are complex-valued. -/
def tripleKernel (f₁ f₂ f₃ : G × G → ℂ) : G → ℂ := fun g =>
  let cardG : ℂ := Fintype.card G
  (cardG ^ 2)⁻¹ *
      ∑ x₁ : G, ∑ x₂ : G,
        f₁ (x₂, g - x₁ - x₂) * f₂ (x₁, g - x₁ - x₂) * f₃ (x₁, x₂)

/-- The generating family of functions for `Φ(G)`. The functions `fᵢ : G × G → ℂ` are
bounded by 1 in sup norm. -/
def baseΦ : Set (G → ℂ) :=
  {φ | ∃ f₁ f₂ f₃ : G × G → ℂ,
    (∀ p, ‖f₁ p‖ ≤ 1) ∧ (∀ p, ‖f₂ p‖ ≤ 1) ∧ (∀ p, ‖f₃ p‖ ≤ 1) ∧
    φ = tripleKernel G f₁ f₂ f₃}

/-- The generating family of functions for `Φ′(G)`, where the third kernel depends only on
`x₁ + x₂`. -/
def baseΦ' : Set (G → ℂ) :=
  {φ | ∃ f₁ f₂ : G × G → ℂ, ∃ h : G → ℂ,
    (∀ p, ‖f₁ p‖ ≤ 1) ∧ (∀ p, ‖f₂ p‖ ≤ 1) ∧ (∀ x, ‖h x‖ ≤ 1) ∧
    φ = tripleKernel G f₁ f₂ (fun p => h (p.1 + p.2))}

/-- The space `Φ(G)` of "convex combinations" of kernels from `baseΦ`.

Since `baseΦ G` is balanced (closed under multiplication by unit complex numbers) and
contains 0, the absolutely convex hull over ℂ (i.e., the set of
$\sum c_i \phi_i$ with $\phi_i \in \text{baseΦ}$ and $\sum |c_i| \le 1$)
coincides with the real convex hull. -/
def Φ : Set (G → ℂ) :=
  convexHull ℝ (baseΦ G)

/-- The restricted space `Φ′(G)` of "convex combinations" of kernels from `baseΦ'`. -/
def Φ' : Set (G → ℂ) :=
  convexHull ℝ (baseΦ' G)


/-- The linear functional on `G → ℂ` given by `φ ↦ Re ∑ g, a g * φ g`. -/
def functional (a : G → ℂ) (φ : G → ℂ) : ℝ :=
  (∑ g : G, a g * φ g).re

/-- The support function of a set `S` with respect to a linear functional `a`:
  `sup_{φ ∈ S} Re ⟨a, φ⟩`. -/
def supportFn (a : G → ℂ) (S : Set (G → ℂ)) : ℝ :=
  sSup (functional G a '' S)


/-- For $G = \mathbb{Z}/3\mathbb{Z}$ and the functional $a(0) = -1$, $a(1) = -3$, $a(2) = 3$,
does the support function of $\Phi$ at $a$ strictly exceed that of $\Phi'$?

Numerical evidence suggests the answer is **yes**:
$$\sup_{\varphi \in \Phi'(\mathbb{Z}/3\mathbb{Z})} \operatorname{Re}\langle a, \varphi \rangle
  \;<\; \sup_{\varphi \in \Phi(\mathbb{Z}/3\mathbb{Z})} \operatorname{Re}\langle a, \varphi \rangle.$$

The DeepMind prover agent provided a formal proof, showing that $\frac{183095}{30000}$ separates the
support functions.
-/
@[category research solved, AMS 5 11, formal_proof using formal_conjectures at
"https://github.com/mo271/formal-conjectures/blob/f5afe85e1e02611f63c32ae041b33c67b7938cba/FormalConjectures/GreensOpenProblems/57.lean#L1071"]
theorem green_57.variants.z3_functional :
    let a : ZMod 3 → ℂ := ![(-1 : ℂ), -3, 3]
    answer(True) ↔
      supportFn (ZMod 3) a (Φ' (ZMod 3)) < supportFn (ZMod 3) a (Φ (ZMod 3)) := by
  sorry

/-- Do $\Phi(\mathbb{Z}/3\mathbb{Z})$ and $\Phi'(\mathbb{Z}/3\mathbb{Z})$ coincide?

Numerical evidence suggests the answer is **no**: the integer functional $a = (-1, -3, 3)$
separates the two spaces. A branch-and-bound verification over the phase variables shows
$\max_{\Phi'} \operatorname{Re}\langle a, 

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
