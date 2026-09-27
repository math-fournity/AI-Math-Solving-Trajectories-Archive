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
# Erdős Problem 1003

*Reference:* [erdosproblems.com/1003](https://www.erdosproblems.com/1003)
-/

namespace Erdos1003

open scoped Nat
open Filter

/--
Are there infinitely many solutions to $\phi(n) = \phi(n+1)$, where $\phi$ is the Euler totient
function?
-/
@[category research open, AMS 11]
theorem erdos_1003 : answer(sorry) ↔ Set.Infinite {n | φ n = φ (n + 1)} := by
  sorry

/--
Erdős [Er85e] says that, presumably, for every $k \geq 1$ the equation
$$\phi(n) = \phi(n+1) = \cdots = \phi (n+k)$$ has infinitely many solutions.

[Er85e] Erdős, P., _Some problems and results in number theory_. Number theory and combinatorics. Japan 1984 (Tokyo, Okayama and Kyoto, 1984) (1985), 65-87.
-/
@[category research open, AMS 11]
theorem erdos_1003.variants.Icc :
    answer(sorry) ↔ ∀ k ≥ 1, {n | ∀ i ∈ Set.Icc 1 k, φ n = φ (n + i)}.Infinite := by
  sorry

/--
Erdős, Pomerance, and Sárközy [EPS87] proved that for all large $x$, the number
of $n \leq x$ with $\phi(n) = \phi(n+1)$ is at most $$\frac{x}{\exp((\log x)^{1/3})}$$.

[EPS87] Erd\H os, Paul and Pomerance, Carl and S\'ark\"ozy, Andr\'as, _On locally repeated values of certain arithmetic functions_. {II}. Proc. Amer. Math. Soc. (1987), 1--7.
-/
@[category research solved, AMS 11]
theorem erdos_1003.variants.eps87 :  ∀ᶠ x in atTop,
    {(n : ℕ) | (n ≤ x) ∧ φ n = φ (n + 1)}.ncard ≤
      x / Real.exp ((x.log) ^ ((1 : ℝ) / 3)) := by
  sorry

end Erdos1003


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
