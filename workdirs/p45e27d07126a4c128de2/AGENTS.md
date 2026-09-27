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
# Erdős Problem 946

*References:*
 - [erdosproblems.com/946](https://www.erdosproblems.com/946)
 - [ErMi52] Erdős, P. and Mirsky, L., The distribution of values of the divisor function {$d(n)$}.
   Proc. London Math. Soc. (3) (1952), 257--271.
 - [Sp81] Spiro, C. A., The frequency with which an integral-valued, prime-independent,
   multiplicative or additive function of n divides a polynomial function of n.
 - [He84] Heath-Brown, D. R., The divisor function at consecutive integers.
   Mathematika 31 (1984), no. 2, 141--149.
 - [Hi85] Hildebrand, A., The divisor function at consecutive integers. Pacific J. Math.
   (1987), 307--319
 - [EPS87] Erdős, P., Pomerance, C., and Sarkőzy, A., On locally repeated values of
   arithmetic functions. III. Proc. Amer. Math. Soc. (1987), 1--7.
-/

open Filter Real
open scoped ArithmeticFunction.sigma

namespace Erdos946

/--
There are infinitely many $n$ such that $τ(n) = τ(n+1)$. Proved in [He84].
Here τ is the divisor counting function, which is `σ 0` in mathlib.
-/
@[category research solved, AMS 11]
theorem erdos_946 : {n : ℕ | σ 0 n = σ 0 (n + 1)}.Infinite := by
  sorry

/--
There are infinitely many $n$ such that $τ(n) = τ(n + 5040)$. Proved in [Sp81].
-/
@[category research solved, AMS 11]
theorem erdos_946.variants.spiro_5040 : {n : ℕ | σ 0 n = σ 0 (n + 5040)}.Infinite := by
  sorry

/-- Number of $n \le x$ with $τ(n) = τ(n+1)$. -/
noncomputable def erdos946Count (x : ℝ) : ℝ :=
  ((Finset.range (⌊x⌋₊ + 1)).filter (fun n => σ 0 n = σ 0 (n + 1))).card

/--
The number of $n \le x$ with $τ(n) = τ(n+1)$ is at least $x / (\log x)^7$ for all sufficiently
large $x$. Proved in [He84].
-/
@[category research solved, AMS 11]
theorem erdos_946.variants.heathbrown_lower_bound :
    (fun x => x / (x.log)^7) =O[atTop] erdos946Count := by
  sorry

/--
Improved lower bound in [Hi85]: $Ω(x / (\log \log x)^3)$.
-/
@[category research solved, AMS 11]
theorem erdos_946.variants.hildebrand_lower_bound :
    (fun x => x / (x.log.log)^3) =O[atTop] erdos946Count := by
  sorry

/--
Upper bound in [EPS87]: $O(x / \sqrt{\log \log x})$.
-/
@[category research solved, AMS 11]
theorem erdos_946.variants.upper_bound : erdos946Count =O[atTop] (fun x => x / √x.log.log ) := by
  sorry

end Erdos946


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
