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
# Lonely runner conjecture

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Lonely_runner_conjecture)
-/

namespace LonelyRunnerConjecture

/--
Consider $n$ runners on a circular track of unit length. At the initial time
$t = 0$, all runners are at the same position and start to run; the runners'
speeds are constant, all distinct, and may be negative. A runner is said to be
lonely at time $t$ if they are at a distance (measured along the circle) of at
least $\frac 1 n$ from every other runner. The lonely runner conjecture states that each
runner is lonely at some time, no matter the choice of speeds.
-/
@[category research open, AMS 11]
theorem lonely_runner_conjecture (n : ℕ)
    (speed : Fin n ↪ ℝ) (lonely : Fin n → ℝ → Prop)
    (lonely_def :
      ∀ r t, lonely r t ↔
        ∀ r2 : Fin n, r2 ≠ r →
        dist (t * speed r : UnitAddCircle) (t * speed r2) ≥ 1 / n)
    (r : Fin n) : ∃ t ≥ 0, lonely r t := by
  sorry

/-
## Variant: Tao (2017)
-/

/--
For an $n$-tuple of distinct integer velocities $v_1,\dots,v_n$,
`deltaTuple v` is the maximal value of $\min_i \|t v_i\|_{\mathbb{R}/\mathbb{Z}}$ over time.
-/
noncomputable def deltaTuple {n : ℕ} (v : Fin n → ℤ) : ℝ :=
  sSup { δ : ℝ | ∃ t : AddCircle (1 : ℝ), ∀ i : Fin n, δ ≤ dist (v i • t : AddCircle (1 : ℝ)) 0 }

/--
The $n$th *gap of loneliness* $\delta_n$: the infimum of `deltaTuple`
over all $n$-tuples of distinct nonzero integer velocities.
-/
noncomputable def deltaGap (n : ℕ) : ℝ :=
  sInf { d : ℝ | ∃ v : Fin n ↪ ℤ, (∀ i : Fin n, v i ≠ 0) ∧ d = deltaTuple v }

/--
**Theorem 1.3 (Tao, 2017; arXiv:1701.02048).**
There exists an absolute constant $c > 0$ such that for all sufficiently large $n$,
the gap of loneliness satisfies
$\delta_n \ge \frac{1}{2n} + \frac{c \log n}{n^2 (\log \log n)^2}$.
-/
@[category research solved, AMS 11]
theorem lonely_runner_conjecture.variants.tao_2017 :
    ∃ c : ℝ, 0 < c ∧
      (∀ᶠ n : ℕ in Filter.atTop,
        deltaGap n ≥
          ((1 : ℝ) / (2 * (n : ℝ))
            + c * Real.log (n : ℝ) /
                ((n : ℝ) ^ 2 * (Real.log (Real.log (n : ℝ))) ^ 2))) := by
  sorry

end LonelyRunnerConjecture


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
