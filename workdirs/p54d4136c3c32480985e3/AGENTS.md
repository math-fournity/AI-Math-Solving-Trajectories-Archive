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
# Green's Open Problem 47

*References:*
- [Gr24] [Ben Green's 100 Open Problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.47)
- [GH14] Green, Ben, and Adam J. Harper. "Inverse questions for the large sieve."
  Geometric and Functional Analysis 24.4 (2014): 1167-1203.
- [HV09] Helfgott, Harald Andrés, and Akshay Venkatesh. "How small must ill-distributed sets be."
  Analytic number theory 2 (2009): 224-234.
- [Wa12] Walsh, Miguel N. "The inverse sieve problem in high dimensions." (2012): 2001-2022.
- [Wa14] Walsh, Miguel N. "The algebraicity of ill-distributed sets."
  Geometric and Functional Analysis 24.3 (2014): 959-967.
-/

open Filter

namespace Green47

/--
Suppose that a large sieve process leaves a set of quadratic size. Is that set quadratic?

The following very particular instance is probably the simplest [Gr24]:
Suppose that $A \subset \mathbb{N}$ is a set with the property that
$|A \pmod p| \leqslant \frac{1}{2}(p + 1)$ for all sufficiently large $p$.
Is it true that either $|A \cap [X]| \ll X^{1/2} / \log^{100} X$, or $A$ is contained in the
image of $\mathbb{Z}$ under a quadratic map $\phi : \mathbb{Q} \to \mathbb{Q}$?
-/
@[category research open, AMS 11]
theorem green_47 :
    answer(sorry) ↔ ∀ A : Set ℕ,
      (∀ᶠ p in atTop, Nat.Prime p → Set.ncard (Set.image (fun a : ℕ => (a : ZMod p)) A) ≤ (p + 1) / 2) →
      ((fun X : ℕ => ((A ∩ Set.Iic X).ncard : ℝ)) ≪ (fun X : ℕ => Real.sqrt (X : ℝ) / (Real.log (X : ℝ)) ^ 100))
      ∨ (∃ P : Polynomial ℚ, P.degree = 2 ∧ ∀ a ∈ A, ∃ z : ℤ, (a : ℚ) = P.eval (z : ℚ)) := by
  sorry

end Green47


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
