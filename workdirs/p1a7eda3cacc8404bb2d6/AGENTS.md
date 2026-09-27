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
# Erdős Problem 1133

*References:*
- [erdosproblems.com/1133](https://www.erdosproblems.com/1133)
- [Er67] Erdős, P., Problems and results on the convergence and divergence properties of the
  Lagrange interpolation polynomials and some extremal problems. Mathematica (Cluj) (1967), 65-73.
-/

open Filter Set

namespace Erdos1133

/--
Let $C>0$. There exists $\epsilon>0$ such that if $n$ is sufficiently large the following holds.

For any $x_1,\ldots,x_n\in [-1,1]$ there exist $y_1,\ldots,y_n\in [-1,1]$ such that, if $P$ is a
polynomial of degree $m<(1+\epsilon)n$ with $P(x_i)=y_i$ for at least $(1-\epsilon)n$ many
$1\leq i\leq n$, then $$\max_{x\in [-1,1]}\lvert P(x)\rvert >C.$$
-/
@[category research open, AMS 26 41]
theorem erdos_1133 :
    answer(sorry) ↔
    ∀ C > (0 : ℝ), ∃ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ x : Fin n → Icc (-1 : ℝ) 1,
        ∃ y : Fin n → Icc (-1 : ℝ) 1,
          ∀ P : Polynomial ℝ,
            (P.natDegree : ℝ) < (1 + ε) * (n : ℝ) →
            ((Finset.univ.filter (fun i ↦ P.eval (x i : ℝ) = (y i : ℝ))).card : ℝ) ≥
              (1 - ε) * (n : ℝ) →
            ∃ z ∈ Icc (-1 : ℝ) 1, |P.eval z| > C := by
  sorry

/--
Erdős proved that, for any $C>0$, there exists $\epsilon>0$ such that if $n$ is sufficiently
large and $m=\lfloor (1+\epsilon)n\rfloor$ then for any $x_1,\ldots,x_m\in [-1,1]$ there is a
polynomial $P$ of degree $n$ such that $\lvert P(x_i)\rvert\leq 1$ for $1\leq i\leq m$ and
$\max_{x\in [-1,1]}\lvert P(x)\rvert>C$. The conjectured statement would also imply this, but
Erdős in [Er67] says he could not even prove it for $m=n$.
-/
@[category research solved, AMS 26 41]
theorem erdos_1133.variants.weaker :
    ∀ C > (0 : ℝ), ∃ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      let m := ⌊(1 + ε) * (n : ℝ)⌋₊;
      ∀ x : Fin m → Icc (-1 : ℝ) 1,
        ∃ P : Polynomial ℝ,
          P.natDegree = n ∧
          (∀ i : Fin m, |P.eval (x i : ℝ)| ≤ 1) ∧
          ∃ z ∈ Icc (-1 : ℝ) 1, |P.eval z| > C := by
  sorry

end Erdos1133


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
