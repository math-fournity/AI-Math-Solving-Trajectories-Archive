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
# Green's Open Problem 36

*References:*
* [Gr24] [Green's Open Problems #36](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.36)
* [CKS05] Cohn, H., Kleinberg, R., Szegedy, B., and Umans, C. "Group-theoretic Algorithms for
  Matrix Multiplication" (Problem 4.7)
-/

open Filter
open scoped Pointwise

namespace Green36

/-- The simultaneous double product property [CKS05, 4.1]. -/
def SimultaneousDoubleProduct {ι H : Type*} [AddCommGroup H]
    (A B : ι → Finset H) : Prop :=
  open scoped Classical in
  (∀ i, (A i + B i).card = (A i).card * (B i).card) ∧
  (∀ i j k, i ≠ k → Disjoint (A i + B j) (A j + B k))

/-- A variant of the simultaneous double product property, as stated in [Gr24, Problem 36]. -/
def Green36Property {ι H : Type*} [AddCommGroup H]
    (A B : ι → Finset H) : Prop :=
  open scoped Classical in
  (∀ i, (A i + B i).card = (A i).card * (B i).card) ∧
  (∀ i j k, j ≠ k → Disjoint (A i + B i) (A j + B k))

/--
Do the following exist, for arbitrarily large $n$? An abelian group $H$ with $|H| = n^{2+o(1)}$,
together with subsets $A_1, ..., A_n, B_1, ..., B_n$ satisfying $|A_i||B_i| \ge n^{2-o(1)}$ and
$|A_i + B_i| = |A_i||B_i|$, such that the sets $A_i + B_i$ are disjoint from the sets $A_j + B_k$
($j \neq k$)?

NOTE: according to [CKS05, 4.1], the conditions should be $A_i + B_j$ disjoint from $A_j + B_k$ for
$i \neq k$. See `green_36.variants.cks05`.
-/
@[category research open, AMS 5 20]
theorem green_36 :
    answer(sorry) ↔
      ∀ ε > (0 : ℝ), ∃ᶠ n in atTop,
        ∃ (H : Type) (_ : AddCommGroup H) (_ : Finite H) (A B : Fin n → Finset H),
          (n : ℝ) ^ (2 - ε) ≤ Nat.card H ∧ Nat.card H ≤ (n : ℝ) ^ (2 + ε) ∧
          (∀ i, (n : ℝ) ^ (2 - ε) ≤ (A i).card * (B i).card) ∧
          Green36Property A B := by
  sorry

/-- Variant using the exact simultaneous double product property from [CKS05, 4.1]. -/
@[category research open, AMS 5 20]
theorem green_36.variants.cks05 :
    answer(sorry) ↔
      ∀ ε > (0 : ℝ), ∃ᶠ n in atTop,
        ∃ (H : Type) (_ : AddCommGroup H) (_ : Finite H) (A B : Fin n → Finset H),
          (n : ℝ) ^ (2 - ε) ≤ Nat.card H ∧ Nat.card H ≤ (n : ℝ) ^ (2 + ε) ∧
          (∀ i, (n : ℝ) ^ (2 - ε) ≤ (A i).card * (B i).card) ∧
          SimultaneousDoubleProduct A B := by
  sorry

-- TODO(jeangud) Add variants mentioned in [Gr24, Problem 36] comments.

end Green36


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
