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
# Written on the Wall II - Conjecture 103

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/

namespace WrittenOnTheWallII.GraphConjecture103

open SimpleGraph

/-- The 11-vertex counterexample: a triangle with four leaves on each of two vertices. -/
abbrev wowii103Counterexample : SimpleGraph (Fin 11) :=
  SimpleGraph.fromEdgeSet {
    s(0, 1), s(0, 2), s(1, 2),
    s(0, 3), s(0, 4), s(0, 5), s(0, 6),
    s(1, 7), s(1, 8), s(1, 9), s(1, 10)
  }

/-- The counterexample is connected. -/
@[category test, AMS 5]
theorem wowii103Counterexample_connected : wowii103Counterexample.Connected := by
  decide +native

/-- The counterexample has independence number nine. -/
@[category test, AMS 5]
theorem wowii103Counterexample_indepNum : wowii103Counterexample.indepNum = 9 := by
  rw [indep_num_eq_computable]
  decide +native

/-- The largest induced bipartite subgraph of the counterexample has ten vertices. -/
@[category test, AMS 5]
theorem wowii103Counterexample_bipartiteSize :
    wowii103Counterexample.largestInducedBipartiteSubgraphSize = 10 := by
  rw [largestInducedBipartiteSubgraphSize_eq_computable]
  decide +native

/-- The counterexample has average eccentricity $30/11$. -/
@[category test, AMS 5]
theorem wowii103Counterexample_averageEccentricity :
    averageEccentricity wowii103Counterexample = 30 / 11 := by
  unfold averageEccentricity
  have hsum : (∑ v : Fin 11, (wowii103Counterexample.eccent v).toNat) = 30 := by
    simp_rw [eccent_eq_computable wowii103Counterexample wowii103Counterexample_connected]
    decide +native
  rw [hsum]
  norm_num

/-- The logarithm of the counterexample's average eccentricity lies strictly between one and two. -/
@[category test, AMS 5]
theorem one_lt_log_thirty_eleven_and_lt_two :
    1 < Real.log (30 / 11 : ℝ) ∧ Real.log (30 / 11 : ℝ) < 2 := by
  constructor
  · rw [Real.lt_log_iff_exp_lt (by norm_num)]
    exact Real.exp_one_lt_d9.trans (by norm_num)
  · exact (Real.log_lt_sub_one_of_pos (by norm_num) (by norm_num)).trans (by norm_num)

/--
WOWII [Conjecture 103](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

For a simple connected graph $G$,
$\alpha(G) \le \lfloor b(G) - \ln(\mathrm{ecc\_avg}(G)) \rfloor$
where $\alpha(G) = G.\mathrm{indepNum}$ is the independence number,
$b(G)$ is the largest induced bipartite subgraph size, and
$\mathrm{ecc\_avg}(G) = G.\mathrm{averageEccentricity}$ is the average
eccentricity of $G$. Uses `Real.log` (natural logarithm).

This conjecture is false. The graph `wowii103Counterexample` has independence number $9$,
largest induced bipartite subgraph size $10$, and average eccentricity $30/11$. Since
$1 < \ln(30/11) < 2$, the proposed upper bound is $8$.
-/
@[category research solved, AMS 5]
theorem conjecture103 : answer(False) ↔
    ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) (_h : G.Connected),
      (G.indepNum : ℝ) ≤ ⌊b G - Real.log (averageEccentricity G)⌋ := by
  show False ↔ _
  rw [false_iff]
  intro h
  have hbad := h (Fin 11) wowii103Counterexample wowii103Counterexample_connected
  rw [wowii103Counterexample_indepNum, b, wowii103Counterexample_bipartiteSize,
    wowii103Counterexample_averageEccentricity] at hbad
  have hfloor : ⌊(10 : ℝ) - Real.log (30 / 11 : ℝ)⌋ = (8 : ℤ) := by
    rw [Int.floor_eq_iff]
    constructor <;> norm_num <;> linarith [one_lt_log_thirty_eleven_and_lt_two.1,
      one_lt_log_thirty_eleven_and_lt_two.2]
  norm_num [hfloor] at hbad

end WrittenOnTheWallII.GraphConjecture103


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
