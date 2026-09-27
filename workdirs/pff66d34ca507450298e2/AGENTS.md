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
# Erdős Problem 314

*References:*
- [erdosproblems.com/314](https://www.erdosproblems.com/314)
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
  theory*. Monographies de L'Enseignement Mathematique (1980).
- [LiSt24] J. Lim and Steinerberger, S., *On differences of two harmonic numbers*.
  arXiv:2405.11354 (2024).
-/

open Filter

namespace Erdos314

/-- `mMin n` is the minimal `m` such that $\sum_{n\leq k\leq m}\frac{1}{k}\geq 1$; such an `m`
exists for `n ≥ 1` since the harmonic series diverges. -/
noncomputable def mMin (n : ℕ) : ℕ := sInf {m | 1 ≤ harmonicBlock n m}

/-- $\epsilon(n) = \sum_{n\leq k\leq m}\frac{1}{k}-1$, the overshoot of the minimal block sum
reaching $1$. -/
noncomputable def epsilon (n : ℕ) : ℝ := (harmonicBlock n (mMin n) : ℝ) - 1

/--
Let $n\geq 1$ and let $m$ be minimal such that $\sum_{n\leq k\leq m}\frac{1}{k}\geq 1$. We define
$$\epsilon(n) = \sum_{n\leq k\leq m}\frac{1}{k}-1.$$
How small can $\epsilon(n)$ be? Is it true that
$$\liminf n^2\epsilon(n)=0?$$

This is true, and shown by Lim and Steinerberger [LiSt24], who further proved that, for any
$\delta>0$, there exist infinitely many $n$ and $m$ such that
$$n^2\left\lvert \sum_{n\leq k\leq m}\frac{1}{k}-1\right\rvert\ll \frac{1}{(\log n)^{5/4-\delta}}.$$
Erdős and Graham (and also Lim and Steinerberger) believe that the exponent of $2$ is best
possible here, in that $\liminf \epsilon(n) n^{2+\delta}=\infty$ for all $\delta>0$.
-/
@[category research solved, AMS 11 40, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos314.lean"]
theorem erdos_314 : answer(True) ↔
    atTop.liminf (fun n : ℕ => (n : ℝ) ^ 2 * epsilon n) = 0 := by
  sorry

end Erdos314


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
