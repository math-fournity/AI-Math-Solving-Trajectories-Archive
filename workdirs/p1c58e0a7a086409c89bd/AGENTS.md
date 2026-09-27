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
# Erdős Problem 965

For every 2-coloring of ℝ, is there an uncountable set $A ⊆ ℝ$ such that
all sums $a + b$ for $a, b ∈ A, a ≠ b$ have the same colour?

*References:*
- [erdosproblems.com/965](https://www.erdosproblems.com/965)
- [Er75b] Erdős, Paul, Problems and results in combinatorial number theory. Journées Arithmétiques de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974) (1975), 295-310.
- [HLS17] Hindman, Neil and Leader, Imre and Strauss, Dona, Pairwise sums in colourings of the reals. Abh. Math. Semin. Univ. Hambg. (2017), 275--287.
- [Ko16] Komjáth, Péter, A certain 2-coloring of the reals. Real Anal. Exchange (2016), 227--231.
- [SWCol] Sokoup Dániel and Weiss, William, Sums and Anti-Ramsey Colourings of ℝ. https://danieltsoukup.github.io/academic/finset_colouring.pdf
-/

namespace Erdos965

/--
Erdős asks in [Er75b] if for every 2-coloring of ℝ, there is an uncountable set $A ⊆ ℝ$ such that
all sums $a + b$ for $a, b ∈ A, a ≠ b$ have the same colour.

In [Ko16] Péter Komjáth constructed a counterexample.
The same result was proven independently in [SWCol] by Sokoup and Weiss.
-/
@[category research solved, AMS 3 5]
theorem erdos_965 :
    answer(False) ↔ ∀ f : ℝ → Fin 2, ∃ A : Set ℝ, ¬ A.Countable ∧
      ∀ᵉ (a ∈ A) (b ∈ A) (c ∈ A) (d ∈ A), a ≠ b → c ≠ d → f (a + b) = f (c + d) := by
  sorry

/--
In fact, in both [Ko16] and [SWCol] a generalized example for $k$-sums is constructed.
-/
@[category research solved, AMS 3 5]
theorem erdos_965.variants.generalization : answer(False) ↔
     ∀ᵉ (k ≥ 2), ∀ f : ℝ → Fin 2, ∃ A : Set ℝ, ¬ A.Countable ∧ ∀ s t : Finset ℝ,
      ↑s ⊆ A → ↑t ⊆ A → s.card = k → t.card = k → f (s.sum id) = f (t.sum id) := by
  sorry

end Erdos965


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
