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
# Erdős Problem 323

*Reference:* [erdosproblems.com/323](https://www.erdosproblems.com/323)
-/

open Filter
open scoped Asymptotics

namespace Erdos323

/--
Let $1\leq m\leq k$ and $f_{k,m}(x)$ denote the number of integers $\leq x$ which are the sum of
$m$ many nonnegative $k$th powers.
-/
noncomputable def f (k m x : ℕ) : ℕ :=
  { n : ℕ | n ≤ x ∧ ∃ (v : Fin m → ℕ), n = ∑ i, v i ^ k }.ncard

/--
Is it true that $f_{k,k}(x) \gg_\epsilon x^{1-\epsilon}$ for all $\epsilon>0$?

This would have significant applications to Waring's problem. Erdős and Graham describe this as
'unattackable by the methods at our disposal'.
-/
@[category research open, AMS 11]
theorem erdos_323.parts.i :
    answer(sorry) ↔ ∀ k ≥ 1, ∀ ε > (0 : ℝ),
      (fun (x : ℕ) ↦ (x : ℝ) ^ (1 - ε)) =O[atTop] (fun (x : ℕ) ↦ (f k k x : ℝ)) := by
  sorry

/--
Is it true that if $m < k$ then $f_{k,m}(x) \gg x^{m/k}$ for sufficiently large $x$?
-/
@[category research open, AMS 11]
theorem erdos_323.parts.ii :
    answer(sorry) ↔ ∀ k m : ℕ, 1 ≤ m → m < k →
      (fun (x : ℕ) ↦ (x : ℝ) ^ ((m : ℝ) / (k : ℝ))) =O[atTop] (fun (x : ℕ) ↦ (f k m x : ℝ)) := by
  sorry

/--
The case $k=2$ was resolved by Landau, who showed $f_{2,2}(x) \sim \frac{cx}{\sqrt{\log x}}$ for
some constant $c>0$.
-/
@[category research solved, AMS 11]
theorem erdos_323.variants.k_eq_2 :
    ∃ c > 0, (fun (x : ℕ) ↦ (f 2 2 x : ℝ)) ~[atTop]
      (fun (x : ℕ) ↦ c * (x : ℝ) / Real.sqrt (Real.log (x : ℝ))) := by
  sorry

/--
For $k>2$ it is not known if $f_{k,k}(x)=o(x)$.
-/
@[category research open, AMS 11]
theorem erdos_323.variants.k_gt_2 :
    answer(sorry) ↔ ∀ k > 2, (fun (x : ℕ) ↦ (f k k x : ℝ)) =o[atTop] (fun (x : ℕ) ↦ (x : ℝ)) := by
  sorry

end Erdos323


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
