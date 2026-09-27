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
# Erdős Problem 1047

*References:*
- [erdosproblems.com/1047](https://www.erdosproblems.com/1047)
- [EHP58] Erdős, P. and Herzog, F. and Piranian, G., *Metric properties of polynomials*.
  J. Analyse Math. (1958), 125-148.
- [Go66] Goodman, A. W., *On the convexity of the level curves of a polynomial*.
  Proc. Amer. Math. Soc. (1966), 358-361.
- [Po61] Pommerenke, Ch., *On metric properties of complex polynomials*. Michigan Math. J.
  (1961), 97-115.
-/

open Polynomial

namespace Erdos1047

/-- The sublevel set $\{ z: \lvert f(z)\rvert\leq c\}$ of a polynomial $f\in\mathbb{C}[x]$. -/
def sublevelSet (f : ℂ[X]) (c : ℝ) : Set ℂ := {z : ℂ | ‖f.eval z‖ ≤ c}

/-- The strict sublevel set $\{ z: \lvert f(z)\rvert< c\}$ of a polynomial $f\in\mathbb{C}[x]$. -/
def strictSublevelSet (f : ℂ[X]) (c : ℝ) : Set ℂ := {z : ℂ | ‖f.eval z‖ < c}

/-- The connected components of a set `s ⊆ ℂ`, viewed as subsets of `ℂ`. -/
def componentsIn (s : Set ℂ) : Set (Set ℂ) :=
  {t : Set ℂ | ∃ z ∈ s, t = connectedComponentIn s z}

/--
Let $f\in \mathbb{C}[x]$ be a monic polynomial with $m$ distinct roots, and let $c>0$ be a
constant small enough such that $\{ z: \lvert f(z)\rvert\leq c\}$ has $m$ distinct connected
components.

Must all these components be convex?

A question of Grunsky, which was reported by Erdős, Herzog, and Piranian [EHP58].

The answer is no, as shown by Pommerenke [Po61], who showed that, if $k$ is sufficiently large,
and $f(z)=z^k(z-a)$ where $a$ is sufficiently close to $(1+\frac{1}{k})k^{\frac{1}{k+1}}$, then
$\{ z: \lvert f(z)\rvert\leq 1\}$ has two components, and the component which contains $0$ is
not convex.

This was formalized in Lean by Alexeev using Aristotle.
-/
@[category research solved, AMS 30 52, formal_proof using lean4 at
"https://github.com/plby/lean-proofs/blob/main/src/latest/ErdosProblems/Erdos1047.lean"]
theorem erdos_1047 : answer(False) ↔
    ∀ (f : ℂ[X]) (m : ℕ) (c : ℝ), f.Monic → (f.rootSet ℂ).ncard = m → 0 < c →
      (componentsIn (sublevelSet f c)).ncard = m →
        ∀ t ∈ componentsIn (sublevelSet f c), Convex ℝ t := by
  sorry

/--
The answer is no, as shown by Pommerenke [Po61], who showed that, if $k$ is sufficiently large,
and $f(z)=z^k(z-a)$ where $a$ is sufficiently close to $(1+\frac{1}{k})k^{\frac{1}{k+1}}$, then
$\{ z: \lvert f(z)\rvert\leq 1\}$ has two components, and the component which contains $0$ is
not convex.
-/
@[category research solved, AMS 30 52]
theorem erdos_1047.variants.pommerenke :
    ∀ᶠ k : ℕ in Filter.atTop, ∃ δ : ℝ, 0 < δ ∧ ∀ a : ℝ,
      (1 + 1 / (k : ℝ)) * (k : ℝ) ^ ((1 : ℝ) / ((k : ℝ) + 1)) < a →
        a < (1 + 1 / (k : ℝ)) * (k : ℝ) ^ ((1 : ℝ) / ((k : ℝ) + 1)) + δ →
          (componentsIn (sublevelSet (X ^ k * (X - C (a : ℂ))) 1)).ncard = 2 ∧
          ¬ Convex ℝ (connectedComponentIn (sublevelSet (X ^ k * (X - C (a : ℂ))) 1) 0) := by
  sorry

/--
Goodman [Go66] proved that one of the three components of
$$\{ z: \lvert (z^2+1)(z-2)^2\rvert < 5^{3/2}/4\}$$
is not convex.
-/
@[category research solved, AMS 30 52]
theorem erdos_1047.variants.goodman :
    (componentsIn (strictSublevelSet ((X ^ 2 + 1) * (X - C 2) ^ 2)
        ((5 : ℝ) ^ ((3 : ℝ) / 2) / 4))).ncard = 3 ∧
      ∃ t ∈ componentsIn (strictSublevelSet ((X ^ 2 + 1) * (X - C 2) ^ 2)
        ((5 : ℝ) ^ ((3 : ℝ) / 2) / 4)), ¬ Convex ℝ t := by
  sorry

/--
Goodman [Go66] constructed an example with simple roots, of degree $4$.
-/
@[category research solved, AMS 30 52]
theorem erdos_1047.variants.goodman_simple_roots :
    ∃ (f : ℂ[X]) (c : ℝ), f.Monic ∧ f.natDegree = 4 ∧ (f.rootSet ℂ).ncard = 4 ∧ 0 < c ∧
      (componentsIn (sublevelSet f c)).ncard = 4 ∧
      ∃ t ∈ componentsIn (sublevelSet f c), ¬ Convex ℝ t := by
  sorry

/--
The referee of the paper [Go66] also gave the example of $\lvert z(z^5-1)\rvert< 5\cdot 6^{-6/5}$.
-/
@[category research solved, AMS 30 52]
theorem erdos_1047.variants.referee :
    (componentsIn (strictSublevelSet (X * (X ^ 5 - 1))
        (5 * (6 : ℝ) ^ (-(6 : ℝ) / 5)))).ncard = 6 ∧
      ∃ t ∈ componentsIn (strictSublevelSet (X * (X ^ 5 - 1))
        (5 * (6 : ℝ) ^ (-(6 : ℝ) / 5))), ¬ Convex ℝ t := by
  sorry

/--
Goodman raises the question of the maximum number of non-convex components that are possible as
a function of the degree of $f$.
-/
@[category research open, AMS 30 52]
theorem erdos_1047.variants.max_non_convex_components (n : ℕ) :
    IsGreatest {k :

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
