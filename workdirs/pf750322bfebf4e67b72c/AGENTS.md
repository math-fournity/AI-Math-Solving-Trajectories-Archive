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
# Erdős Problem 503

*Reference:* [erdosproblems.com/503](https://www.erdosproblems.com/503)
-/

namespace Erdos503

open scoped EuclideanGeometry

/--
What is the size of the largest $A \subseteq \mathbb{R}^n$ such that every three points from $A$
determine an isosceles triangle? That is, for any three points $x$, $y$, $z$ from $A$, at least two
of the distances $|x - y|$, $|y - z|$, $|x - z|$ are equal.
-/
@[category research open, AMS 51]
theorem erdos_503 (n : ℕ) :
    IsGreatest {(A.ncard) | (A : Set (ℝ^n)) (hA : A.IsIsosceles)} answer(sorry) := by
  sorry

/--
When $n = 2$, the answer is 6 (due to Kelly [ErKe47] - an alternative proof is given by Kovács [Ko24c]).

[ErKe47] Erdős, Paul and Kelly, L. M., Elementary Problems and Solutions: Solutions: E735. Amer. Math. Monthly (1947), 227-229.
[Ko24c] Z. Kovács, A note on Erdős's mysterious remark. arXiv:2412.05190 (2024).
-/
@[category research solved, AMS 51]
theorem erdos_503.variants.R2 :
    IsGreatest {(A.ncard) | (A : Set ℝ²) (hA : A.IsIsosceles)} 6 := by
  sorry

/--
When $n = 3$, the answer is 8 (due to Croft [Cr62]).

[Cr62] Croft, H. T., $9$-point and $7$-point configurations in $3$-space. Proc. London Math. Soc. (3) (1962), 400-424.
-/
@[category research solved, AMS 51]
theorem erdos_503.variants.R3 :
    IsGreatest {(A.ncard) | (A : Set ℝ³) (hA : A.IsIsosceles)} 8 := by
  sorry

/--
The best upper bound known in general is due to Blokhius [Bl84] who showed that
$$
|A| \leq \binom{n + 2}{2}
$$

[Bl84] Blokhuis, A., Few-distance sets. (1984), iv+70.
-/
@[category research solved, AMS 51]
theorem erdos_503.variants.upper_bound (n : ℕ) :
    ∀ m ∈ {(A.ncard) | (A : Set (ℝ^n)) (hA : A.IsIsosceles)}, m ≤ (n + 2).choose 2 := by
  sorry

/--
Alweiss has observed a lower bound of $\binom{n + 1}{2}$ follows from considering the subset of
$\mathbb{R}^{n + 1}$ formed of all vectors $e_i + e_j$ where $e_i$, $e_j$ are distinct coordinate
vectors. This set can be viewed as a subset of some $\mathbb{R}^n$, and is easily checked to have
the required property.
-/
@[category research solved, AMS 51]
theorem erdos_503.variants.lower_bound (n : ℕ) :
    (n + 1).choose 2 ≤ sSup {(A.ncard) | (A : Set (ℝ^n)) (hA : A.IsIsosceles)} := by
  sorry

end Erdos503


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
