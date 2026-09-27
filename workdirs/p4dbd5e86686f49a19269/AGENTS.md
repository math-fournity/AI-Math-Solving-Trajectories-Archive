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
# Green's Open Problem 26

References:
- [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.26)
- [JLP92] Jaeger, François, et al. "Group connectivity of graphs—a nonhomogeneous analogue of
  nowhere-zero flow properties." Journal of Combinatorial Theory, Series B 56.2 (1992): 165-182.
- [ALM91] Alon, Noga, Nathan Linial, and Roy Meshulam. "Additive bases of vector spaces over prime
  fields." Journal of Combinatorial Theory, Series A 57.2 (1991): 203-210.
- [Yu25] Yu, Yang. "Note on the Additive Basis Conjecture." arXiv preprint arXiv:2510.01300 (2025).
-/

open Set
open scoped Pointwise

namespace Green26


/-- The standard cube in $\mathbb{F}_p^n$ is the set of points with coordinates in $\{0, 1\}$. -/
def StandardCube {p : ℕ} [Fact p.Prime] (n : ℕ) : Set (𝔽 p n) :=
  {x | ∀ i, x i = 0 ∨ x i = 1}

/-- A cube is the image of $\lbrace 0, 1\rbrace^n$ under a linear automorphism. -/
def IsCube {p n : ℕ} [Fact p.Prime] (A : Set (𝔽 p n)) : Prop :=
  ∃ φ : 𝔽 p n ≃ₗ[ZMod p] 𝔽 p n, A = φ '' StandardCube n

/--
Let $A_1, \dots, A_{100}$ be "cubes" in $\mathbb{F}^n_3$.
Is it true that $A_1 + \dots + A_{100} = \mathbb{F}^n_3$?
-/
@[category research solved, AMS 5 11 15]
theorem green_26 :
    ∀ n : ℕ,
      ∀ A : Fin 100 → Set (𝔽₃ n), (∀ i, IsCube (A i)) →
      ∑ i, A i = univ := by
  sorry

/-- [Yu25] has solved the original problem (with 100 replaced by 4) -/
@[category research solved, AMS 5 11 15]
theorem green_26.variants.yu25 :
    ∀ n : ℕ,
    ∀ A : Fin 4 → Set (𝔽₃ n), (∀ i, IsCube (A i)) →
      ∑ i, A i = univ := by
  sorry

open Asymptotics Filter

/--
[ALM91] showed that if 100 is replaced by $\leq c(p) \log n$ then the result is true for
$\mathbb{F}^n_p$.
-/
@[category research solved, AMS 5 11 15]
theorem green_26.variants.alm91 :
    ∀ (p : ℕ) [Fact p.Prime],
      ∃ (k : ℕ → ℕ),
        ((fun n ↦ (k n : ℝ)) =O[atTop] fun n ↦ Real.log n) ∧
        ∀ᶠ n in atTop,
          ∀ A : Fin (k n) → Set (𝔽 p n), (∀ i, IsCube (A i)) →
          ∑ i, A i = univ := by
  sorry

/-- The analogous problem in $\mathbb{F}^n_p$ remains open. [Gr24] -/
@[category research open, AMS 5 11 15]
theorem green_26.variants.open :
    answer(sorry) ↔ ∀ (p : ℕ) [Fact p.Prime],
      (∃ C, ∀ n, ∀ A : Fin C → Set (𝔽 p n), (∀ i, IsCube (A i)) →
      ∑ i, A i = univ) := by
  sorry

end Green26


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
