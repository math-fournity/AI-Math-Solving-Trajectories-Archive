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
# Erdős Problem 659

*References:*
- [erdosproblems.com/659](https://www.erdosproblems.com/659)
- [MoOs06] Moree, Pieter and Osburn, Robert, Two-dimensional lattices with few distances. Enseign. Math. (2) (2006), 361--380
- [ErFi96] Erdős, Paul and Fishburn, Peter, Maximum planar sets that determine {$k$} distances. Discrete Math. (1996), 115--125.
- [Gr26](https://arxiv.org/abs/2601.09102): Benjamin Grayzel, Solution to a Problem of Erdős Concerning Distances and Points
-/

open EuclideanGeometry Finset Real

namespace Erdos659

/--
Is there a set of $n$ points in $\mathbb{R}^2$ such that every subset of $4$ points determines at
least $3$ distances, yet the total number of distinct distances is $\ll \frac{n}{\sqrt{\log n}}$?

There does exist such a set: a suitable truncation of the lattice
$\{(a,b\sqrt{2}): a,b\in\mathbb{Z}\}$ suffices. This construction appears to have been first
considered by Moree and Osburn \cite{MoOs06}, who proved that it has
 $\ll \frac{n}{\sqrt{\log n}}$ many distinct distances. This construction was independently found by
 [Lund and Sheffer](https://adamsheffer.wordpress.com/2014/07/16/point-sets-with-few-distinct-distances/),
 who further noted that this configuration contains no squares or equilateral triangles.

There are only six possible configurations of $4$ points which determine only $2$ distances
(first noted by Erdős and Fishburn [ErFi96]), and five of them contain either a square or an
equilateral triangle. The remaining configuration contains four points from a regular pentagon,
and Grayzel [Gr26] (using Gemini) has noted in the comments that this configuration can also be
ruled out, thus giving a complete solution to this problem.

Boris Alexeev provides a formalisation of the reduction, which is conditional on Bernays' theorem
(assumed as an axiom in the proof to obtain the $O(n/\sqrt{\log n})$ bound).
See the [formal proof](https://github.com/plby/lean-proofs/blob/226d5fad7143dcebea2bbb5ec87f18a3a1dcea69/src/v4.24.0/ErdosProblems/Erdos659.lean).
-/
@[category research solved, AMS 52]
theorem erdos_659 : answer(True) ↔ ∃ A : ℕ → Finset ℝ²,
   (∀ n, #(A n) = n ∧ ∀ S ⊆ A n, #S = 4 → 3 ≤ distinctDistances S) ∧
    (fun n ↦ distinctDistances (A n)) ≪ fun n ↦ n / sqrt (log n) := by
  sorry

end Erdos659


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
