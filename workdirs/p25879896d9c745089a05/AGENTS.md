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
import Mathlib.Combinatorics.Additive.ApproximateSubgroup

/-!
# Ben Green's Open Problem 29

*References:*
- [Ben Green's Open Problem 29](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.29)
- [Gr12] Green, Ben. "What is... an approximate group." Notices Amer. Math. Soc 59.5 (2012): 655-656.
- [Br13] Breuillard, Emmanuel, Ben Green, and Terence Tao. "Small doubling in groups."
  Erdős Centennial. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013. 129-151.
- [Sa10] Sanders, Tom. "On a nonabelian Balog–Szemerédi-type lemma." Journal of the Australian
  Mathematical Society 89.1 (2010): 127-132.
- [CrSi10] Croot, Ernie, and Olof Sisask. "A probabilistic technique for finding almost-periods of
  convolutions." Geometric and functional analysis 20.6 (2010): 1367-1396.
-/

open scoped Pointwise

namespace Green29

/-- Suppose that $A$ is a $K$-approximate group (not necessarily abelian). Is there $S \subset A$,
$|S| \gg K^{-O(1)} |A|$, with $S^8 \subset A^4$? -/
@[category research open, AMS 20]
theorem green_29 :
    answer(sorry) ↔
      ∃ C c : ℝ, 0 < C ∧ 0 < c ∧
        ∀ {G : Type*} [Group G] [DecidableEq G] (K : ℝ) (A : Finset G),
          1 ≤ K → IsApproximateSubgroup K (A : Set G) →
            ∃ S ⊆ A, C * K ^ (-c) * (A.card : ℝ) ≤ (S.card : ℝ) ∧
            S ^ 8 ⊆ A ^ 4 := by
  sorry

/-- Such a conclusion is known with $|S| \gg_K |A|$ [Br13 Problem 6.5, CrSi10, Sa10]. -/
@[category research solved, AMS 20]
theorem green_29.variant :
    ∀ K : ℝ, 1 ≤ K →
      ∃ c : ℝ, 0 < c ∧ -- Allow c to depend on K.
        ∀ {G : Type*} [Group G] [DecidableEq G] (A : Finset G),
          IsApproximateSubgroup K (A : Set G) →
            ∃ S : Finset G, -- No S ⊆ A requirement in this variant.
              c * (A.card : ℝ) ≤ (S.card : ℝ) ∧
              S ^ 8 ⊆ A ^ 4 := by
  sorry

end Green29


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
