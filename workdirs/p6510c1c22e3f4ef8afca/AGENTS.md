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
# Erdős Problem 1105

*References:*
- [erdosproblems.com/1105](https://www.erdosproblems.com/1105)
- [ESS75] Erdős, P. and Simonovits, M. and Sós, V. T., Anti-{R}amsey theorems. (1975), 633--643.
- [MoNe05] Montellano-Ballesteros, J. J. and Neumann-Lara, V., An anti-{R}amsey theorem on cycles.
  Graphs Combin. (2005), 343--354.
- [SiSo84] Simonovits, Miklós and Sós, Vera T., On restricted colourings of {$K_n$}. Combinatorica
  (1984), 101--110.
- [Yu21] L.-T. Yuan, The anti-Ramsey number for paths. arXiv:2102.00807 (2021).
-/

namespace Erdos1105

open SimpleGraph Asymptotics Filter

/--
The anti-Ramsey number $\mathrm{AR}(n,G)$ is the maximum possible number of colours in which the
edges of $K_n$ can be coloured without creating a rainbow copy of $G$ (i.e. one in which all edges
have different colours).

Let $C_k$ be the cycle on $k$ vertices. Is it true that
$\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1)$?

Montellano-Ballesteros and Neumann-Lara [MoNe05] gave an exact formula for $\mathrm{AR}(n,C_k)$,
which implies in particular that
$\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1).$
-/
@[category research solved, AMS 5]
theorem erdos_1105.parts.i : answer(True) ↔
    ∀ k, 3 ≤ k →
    ((fun n => (antiRamseyNum (cycleGraph k) n : ℝ) - ((k - 2 : ℝ) / 2 + 1 / (k - 1)) * n)
      =O[atTop] (fun _ => (1 : ℝ))) := by
  sorry

/--
Let $P_k$ be the path on $k$ vertices and $\ell=\lfloor\frac{k-1}{2}\rfloor$. If $n\geq k\geq 5$
then is $\mathrm{AR}(n,P_k)$ equal to $\max\left(\binom{k-2}{2}+1,
\binom{\ell-1}{2}+(\ell-1)(n-\ell+1)+\epsilon\right)$where $\epsilon=1$ if $k$ is odd and
$\epsilon=2$ otherwise?

A proof of the formula for $\mathrm{AR}(n,P_k)$ for all $n\geq k\geq 5$ has been announced by
Yuan [Yu21].
-/
@[category research solved, AMS 5]
theorem erdos_1105.parts.ii : answer(True) ↔
    ∀ (k n : ℕ), 5 ≤ k → k ≤ n →
    let ℓ := (k - 1) / 2
    let ε := if Odd k then 1 else 2
    antiRamseyNum (pathGraph k) n = max ((k - 2).choose 2 + 1) ((ℓ - 1).choose 2 +
      (ℓ - 1) * (n - ℓ + 1) + ε) := by
  sorry

-- TODO: Add Erdős, Simonovits, and Sós variant.
-- TODO: Add Simonovits and Sós variant.

end Erdos1105


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
