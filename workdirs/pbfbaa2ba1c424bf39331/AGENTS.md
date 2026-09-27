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
# Erdős Problem 1080

*References:*
- [erdosproblems.com/1080](https://www.erdosproblems.com/1080)
- [DeSz92] de Caen, D. and Székely, L. A., The maximum size of {$4$}- and {$6$}-cycle free bipartite
  graphs on {$m,n$} vertices. (1992), 135--142.
- [Er75] Erdős, P., Some recent progress on extremal problems in graph theory. Congr. Numer. (1975),
  3-14.
- [LUW94] Lazebnik, F. and Ustimenko, V. A. and Woldar, A. J., New constructions of bipartite graphs
  on {$m,n$} vertices with many edges and without small cycles. J. Combin. Theory Ser. B (1994),
  111--117.
-/

open SimpleGraph

namespace Erdos1080

/-- `IsBipartition G X Y` means that `X` and `Y` form a bipartition of the vertices of `G`. -/
def IsBipartition {V : Type*} (G : SimpleGraph V) (X Y : Set V) : Prop :=
  Disjoint X Y ∧ X ∪ Y = Set.univ ∧ ∀ ⦃u v⦄, G.Adj u v → (u ∈ X ↔ v ∈ Y)

/--
Let $G$ be a bipartite graph on $n$ vertices such that one part has $\lfloor n^{2/3}\rfloor$
vertices. Is there a constant $c>0$ such that if $G$ has at least $cn$ edges then $G$ must
contain a $C_6$?

The answer is no, as shown by De Caen and Székely [DeSz92], who in fact show a stronger result.
Let $f(n,m)$ be the maximum number of edges of a bipartite graph between $n$ and $m$ vertices which
does not contain either a $C_4$ or $C_6$. A positive answer to this question would then imply
$f(n,\lfloor n^{2/3}\rfloor)\ll n$. De Caen and Székely prove
$n^{10/9}\gg f(n,\lfloor n^{2/3}\rfloor) \gg n^{58/57+o(1)}$ for $m\sim n^{2/3}$. They also prove
more generally that, for $n^{1/2}\leq m\leq n$, $f(n,m) \ll (nm)^{2/3},$ which was also proved by
Faudree and Simonovits.

This was formalized in Lean by Alexeev using Aristotle.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1080.lean"]
theorem erdos_1080 :
    answer(False) ↔
    ∃ c > (0 : ℝ), ∀ (V : Type) [Fintype V] [Nonempty V] (G : SimpleGraph V) (X Y : Set V),
      IsBipartition G X Y → X.ncard = ⌊(Fintype.card V : ℝ) ^ (2/3 : ℝ)⌋₊ →
      G.edgeSet.ncard ≥ c * Fintype.card V →
        ∃ (v : V) (walk : G.Walk v v), walk.IsCycle ∧ walk.length = 6 := by
  sorry

-- TODO: Add Erdos C_8 variant.
-- TODO: Add Lazebnik, Ustimenko, and Woldar's lower bound.

end Erdos1080


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
