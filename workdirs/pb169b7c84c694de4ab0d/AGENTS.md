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
# Ben Green's Open Problem 18

*Reference:*
- [Gr26] [Ben Green's Open Problem 18](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.18)
- [Au16] Austin, Tim. "Ajtai–Szemerédi theorems over quasirandom groups." Recent trends in
  combinatorics. Cham: Springer International Publishing, 2016. 453-484.
- [So13] Solymosi, Jozsef. "Roth-type theorems in finite groups." European Journal of Combinatorics
  34.8 (2013): 1454-1458.
- [Go01] Gowers, William T. "A new proof of Szemerédi's theorem." Geometric & Functional Analysis
  GAFA 11.3 (2001): 465-588.
-/

open Finset

namespace Green18

/--
The number of triples $(x, y, g)$ in $G^3$ such that $g \neq e$, and $(x, y), (gx, y), (x, gy)$ are
all in $A$. These are called "naive corners" by [Au16].

Note: the shortened formulation from [Gr26] does not mention $g \neq e$, but this is the original
statement from [Au16], which ensure non-trivial corners. Note however that [Au16] use more
generally compact groups and not just finite discrete groups.
-/
def numNaiveCorners {G : Type*} [Group G] [Fintype G] [DecidableEq G] (A : Finset (G × G)) : ℕ :=
  ( (univ : Finset (G × G × G)).filter
    fun ⟨x, y, g⟩ => g ≠ 1 ∧ (x, y) ∈ A ∧ (g * x, y) ∈ A ∧ (x, g * y) ∈ A
  ).card

/--
Suppose that $G$ is a finite group, and let $A \subset G \times G$ be a subset of density $\alpha$.
Is it true that there are $\gg_\alpha |G|^3$ triples $x, y, g$ such that $(x, y), (gx, y), (x, gy)$
all lie in $A$?

Note: A is taken as $\alpha$-dense, i.e. $|A| \ge \alpha |G|^2$ [Au16, Question 2]
-/
@[category research open, AMS 5 11 20]
theorem green_18 : answer(sorry) ↔
    ∀ α > 0, ∃ c > 0, ∃ m₀ : ℕ,
      ∀ (G : Type*) [Group G] [Fintype G] [DecidableEq G] (A : Finset (G × G)),
      Fintype.card G ≥ m₀ →
      (A.card : ℝ) ≥ α * (Fintype.card G) ^ 2 →
      (numNaiveCorners A : ℝ) ≥ c * (Fintype.card G) ^ 3 := by
  sorry

/--
The number of triples $(x, y, g)$ in $G^3$ such that $g \neq e$, and $(x, y), (xg, y), (x, gy)$ are
all in $A$. These are called "BMZ corners" by [Au16].
-/
def numBmzCorners {G : Type*} [Group G] [Fintype G] [DecidableEq G] (A : Finset (G × G)) : ℕ :=
  (
    (univ : Finset (G × G × G)).filter
    fun ⟨x, y, g⟩ => g ≠ 1 ∧ (x, y) ∈ A ∧ (x * g, y) ∈ A ∧ (x, g * y) ∈ A
  ).card

/--
[So13] proved this is true for "BMZ corners". Follows from the proof of Theorem 2.1, p.1456-1457.
-/
@[category research solved, AMS 5 11 20]
theorem green_18.bmz_corners : ∀ α > 0, ∃ c > 0, ∃ m₀ : ℕ,
    ∀ (G : Type*) [Group G] [Fintype G] [DecidableEq G] (A : Finset (G × G)),
    Fintype.card G ≥ m₀ →
    (A.card : ℝ) ≥ α * (Fintype.card G) ^ 2 →
    (numBmzCorners A : ℝ) ≥ c * (Fintype.card G) ^ 3 := by
  sorry

end Green18


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
