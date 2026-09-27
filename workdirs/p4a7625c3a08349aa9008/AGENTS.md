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
# Green's Open Problem 9

References:
- [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.9)
- [BlSi20] Bloom, Thomas F., and Olof Sisask. "Breaking the logarithmic barrier in Roth's theorem on
  arithmetic progressions." arXiv preprint arXiv:2007.03528 (2020).
-/

open Filter

namespace Green9

/--
The quantity $r_k(N)$, defined as the size of the largest subset of $\{1, \dots, N\}$ without
non-trivial $k$-term arithmetic progressions.
-/
noncomputable def r (k N : ℕ) : ℕ := (Finset.Icc 1 N).maxAPFreeCard k

/--
Problem 9 (i): is $r_3(N) \ll N(\log N)^{-10}$?

Solved in [BlSi20].
-/
@[category research solved, AMS 5]
theorem green_9_i :
    (fun (N : ℕ) ↦ (r 3 N : ℝ)) ≪ fun (N : ℕ) ↦ (N : ℝ) * (Real.log N) ^ (-10 : ℝ) := by
  sorry

/--
Problem 9 (ii): is $r_5(N) \ll N(\log N)^{-c}$?
-/
@[category research open, AMS 5]
theorem green_9_ii : answer(sorry) ↔
    ∃ c > (0 : ℝ), (fun (N : ℕ) ↦ (r 5 N : ℝ))
      ≪ fun (N : ℕ) ↦ (N : ℝ) * (Real.log N) ^ (-c) := by
  sorry

/--
Problem 9 (iii): is $r_4(\mathbf{F}_5^n) \ll N^{1-c}$, where $N=5^n$?
-/
@[category research open, AMS 5]
theorem green_9_iii : answer(sorry) ↔
    ∃ c > (0 : ℝ), (fun (n : ℕ) ↦ ((Finset.univ : Finset (𝔽₅ n)).maxAPFreeCard 4 : ℝ))
      ≪ fun (n : ℕ) ↦ ((5 : ℝ) ^ n) ^ (1 - c) := by
  sorry

-- TODO(jeangud): Add some additional bounds from the literature.

end Green9


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
