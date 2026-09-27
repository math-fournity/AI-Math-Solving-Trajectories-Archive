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
# Erdős Problem 914

*References:*
- [erdosproblems.com/914](https://www.erdosproblems.com/914)
- [CoHa63] Corrádi, K. and Hajnal, A., *On the maximal number of independent circuits in a graph*.
  Acta Math. Acad. Sci. Hungar. (1963), 423-439.
- [HaSz70] Hajnal, A. and Szemerédi, E., *Proof of a conjecture of P. Erdős*. (1970), 601-623.
- [KiKo08] Kierstead, H. A. and Kostochka, A. V., *A short proof of the Hajnal-Szemerédi theorem on
  equitable colouring*. Combin. Probab. Comput. (2008), 265-270.
-/

namespace Erdos914

/--
Let $r\geq 2$ and $m\geq 1$. Every graph with $rm$ vertices and minimum degree at least $m(r-1)$
contains $m$ vertex disjoint copies of $K_r$.

When $r=2$ this follows from Dirac's theorem. Corrádi and Hajnal [CoHa63] proved this when $r=3$.
Hajnal and Szemerédi [HaSz70] proved this for all $r\geq 4$.

A shorter proof was given by Kierstead and Kostochka [KiKo08].
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos914.lean"]
theorem erdos_914 {r m : ℕ} (hr : 2 ≤ r) (hm : 1 ≤ m) {V : Type*} [Fintype V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hV : Fintype.card V = r * m)
    (hdeg : m * (r - 1) ≤ G.minDegree) :
    ∃ K : Fin m → Finset V, (∀ i, G.IsNClique r (K i)) ∧
      Pairwise fun i j => Disjoint (K i) (K j) := by
  sorry

/--
Equivalently, every graph with $rm$ vertices and maximum degree at most $m-1$ has a proper vertex
colouring with $m$ colours in which every colour class has exactly $r$ vertices (an equitable
colouring).
-/
@[category research solved, AMS 5]
theorem erdos_914.variants.equitable_colouring {r m : ℕ} (hr : 2 ≤ r) (hm : 1 ≤ m) {V : Type*}
    [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj] (hV : Fintype.card V = r * m)
    (hdeg : G.maxDegree ≤ m - 1) :
    ∃ C : G.Coloring (Fin m), ∀ i, (C.colorClass i).ncard = r := by
  sorry

end Erdos914


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
