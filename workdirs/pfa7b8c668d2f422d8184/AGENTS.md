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
# Green's Open Problem 28

References:
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.28)
- [Mathoverflow/339137](https://mathoverflow.net/questions/339137/why-do-polynomials-with-coefficients-0-1-like-to-have-only-factors-with-0-1) asked by user [Sil](https://mathoverflow.net/users/136794/sil)
- [MathStackexchange/3325163](https://math.stackexchange.com/questions/3325163/) asked by user [Emmanuel Amiot](https://math.stackexchange.com/users/403309/emmanuel-amiot)
-/

namespace Green28

/-- True if a PMF on $\mathbb{Z}$ is uniformly distributed on its support. -/
def IsUniformOnSupport (X : PMF ℤ) : Prop :=
  ∃ (s : Finset ℤ) (hs : s.Nonempty), X = PMF.uniformOfFinset s hs

/--
The discrete convolution of two PMFs on $\mathbb{Z}$, representing the distribution of the sum of
two independent random variables.
-/
noncomputable def indepSum (X Y : PMF ℤ) : PMF ℤ := do
  let x ← X
  let y ← Y
  PMF.pure (x + y)

/--
Suppose that $X, Y$ are two finitely-supported independent random variables taking integer values,
and such that $X + Y$ is uniformly distributed on its range. Are $X$ and $Y$ themselves uniformly
distributed on their ranges?
-/
@[category research open, AMS 60]
theorem green_28 : answer(sorry) ↔
  ∀ (X Y : PMF ℤ), -- marginals, independence is built into indepSum
    X.support.Finite ∧ Y.support.Finite ∧ IsUniformOnSupport (indepSum X Y) →
      IsUniformOnSupport X ∧ IsUniformOnSupport Y := by
  sorry

end Green28


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
