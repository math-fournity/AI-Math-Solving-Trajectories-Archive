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
# Erdős Problem 618

*References:*
- [erdosproblems.com/618](https://www.erdosproblems.com/618)
- [Er99] Erdős, Paul, *A selection of problems and results in combinatorics*. Combin. Probab.
  Comput. (1999), 1-6.
- [EGR98] Erdős, Paul and Gyárfás, András and Ruszinkó, Miklós, *How to decrease the diameter
  of triangle-free graphs*. Combinatorica (1998), 493-501.
-/

namespace Erdos618

open Filter Asymptotics

open scoped Classical in
/-- For a graph `G` on `Fin n`, `h2 G` is the smallest number of edges that need to be added
to `G` so that the resulting supergraph has diameter at most `2` (every two distinct vertices
are adjacent or have a common neighbour) and is still triangle-free (`CliqueFree 3`).
By the `sInf` convention on `ℕ`, `h2 G = 0` if no such supergraph exists. -/
noncomputable def h2 {n : ℕ} (G : SimpleGraph (Fin n)) : ℕ :=
  sInf {k : ℕ | ∃ H : SimpleGraph (Fin n),
    G ≤ H ∧
    H.CliqueFree 3 ∧
    (∀ x y : Fin n, x ≠ y → H.Adj x y ∨ ∃ z, H.Adj x z ∧ H.Adj z y) ∧
    (H.edgeFinset \ G.edgeFinset).card = k}

open scoped Classical in
/--
For a triangle-free graph $G$ let $h_2(G)$ be the smallest number of edges that need to be
added to $G$ so that it has diameter $2$ and is still triangle-free. Is it true that if $G$
has maximum degree $o(n^{1/2})$ then $h(G)=o(n^2)$?

A problem of Erdős, Gyárfás, and Ruszinkó [EGR98]. Simonovits showed that there exist graphs
$G$ with maximum degree $\gg n^{1/2}$ and $h_2(G)\gg n^2$. Alon has observed this problem is
essentially identical to [134], and his solution in
[this note](https://web.math.princeton.edu/~nalon/PDFS/remark1901.pdf) also solves this
problem in the affirmative.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos618.lean"]
theorem erdos_618 : answer(True) ↔
    ∀ (G : ∀ n : ℕ, SimpleGraph (Fin n)),
      (∀ n, (G n).CliqueFree 3) →
      (fun n => ((G n).maxDegree : ℝ)) =o[atTop] (fun n => (n : ℝ) ^ ((1 : ℝ) / 2)) →
      (fun n => (h2 (G n) : ℝ)) =o[atTop] (fun n => (n : ℝ) ^ 2) := by
  sorry

end Erdos618


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
