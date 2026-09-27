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
# Convergence of the Borwein Series with Sinusoidal Coefficient

*References:*
- [MathWorld, Harmonic Series](https://mathworld.wolfram.com/HarmonicSeries.html)
- Borwein, J.; Bailey, D.; Girgensohn, R. *Experimentation in Mathematics: Computational Paths
  to Discovery*, A K Peters, 2004, p. 56.
-/

namespace BorweinSineSeries

/--
Does the series
$$
  \sum_{n=1}^{\infty} \frac{\left(\frac{2}{3} + \frac{1}{3}\sin n\right)^n}{n}
$$
converge?

After computing approximately $10^7$ terms, the partial sums approximate $2.163$.

See https://arxiv.org/abs/2007.11017 for a proof of the convergence,
relying on an irrationality measure for pi.

Also see
https://github.com/AxiomMath/gdm-formal-conjectures/blob/main/docs/BorweinSineSeries.md
for a partial formalization of the conjecture,
conditional on such an irrationality measure of pi (cf https://arxiv.org/abs/1912.06345).
-/
@[category research solved, formal_proof using lean4 at "https://github.com/AxiomMath/gdm-formal-conjectures/blob/main/BorweinSineSeries/solution.lean",  AMS 26 40]
theorem borwein_sine_series :
    answer(True) ↔
      Summable fun n : ℕ+ ↦ ((2 / 3 + 1 / 3 * Real.sin (n : ℝ)) ^ (n : ℕ)) / (n : ℝ) := by
  sorry

end BorweinSineSeries


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
