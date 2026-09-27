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
# Erdős Problem 1034

*References:*
- [erdosproblems.com/1034](https://www.erdosproblems.com/1034)
- [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
  Quaestiones Math. (1993), 333-350.
- [MaTa25] Ma, Jie and Tang, Quanyu, *On Erdős problem #1034*.
  [staff.ustc.edu.cn/~jiema/Erdos-1034.pdf](http://staff.ustc.edu.cn/~jiema/Erdos-1034.pdf)
-/

open Filter

namespace Erdos1034

/--
`JoinedToTwo G T Y` holds when every vertex of `Y` is joined to at least two (distinct)
vertices of `T`.
-/
def JoinedToTwo {V : Type*} (G : SimpleGraph V) (T Y : Finset V) : Prop :=
  ∀ y ∈ Y, ∃ u ∈ T, ∃ v ∈ T, u ≠ v ∧ G.Adj y u ∧ G.Adj y v

/--
Let $G$ be a graph on $n$ vertices with $>n^2/4$ many edges. Must there be a triangle $T$ in $G$
and vertices $y_1,\ldots,y_t$, where $t>(\frac{1}{2}-o(1))n$, such that every $y_i$ is joined to
at least two vertices of $T$?

A conjecture of Erdős and Faudree; a stronger version of [905].

This has been solved in the negative by Ma and Tang [MaTa25], who construct a graph with $n$
vertices and $>n^2/4$ edges in which every triangle has at most $(2-(5/2)^{1/2}+o(1))n$ vertices
adjacent to at least two of its vertices (note that $2-(5/2)^{1/2}\approx 0.4189$).
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1034.lean"]
theorem erdos_1034 : answer(False) ↔
    ∀ ε : ℝ, 0 < ε → ∀ᶠ (n : ℕ) in atTop, ∀ G : SimpleGraph (Fin n),
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) →
        ∃ T : Finset (Fin n), G.IsNClique 3 T ∧ ∃ Y : Finset (Fin n),
          JoinedToTwo G T Y ∧ (1 / 2 - ε) * (n : ℝ) < (Y.card : ℝ) := by
  sorry

/--
Erdős and Faudree asked about the threshold $h(n)$ such that every graph with $n$ vertices and
$>n^2/4$ edges contained a triangle and $h(n)$ other vertices which are connected to at least two
vertices of the triangle. The fact that every graph with $>n^2/4$ edges contains a book of size
$n/6$ shows that
$$(1/6-o(1))n \leq h(n).$$
-/
@[category research solved, AMS 5]
theorem erdos_1034.variants.lower_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop, ∀ G : SimpleGraph (Fin n),
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) →
        ∃ T : Finset (Fin n), G.IsNClique 3 T ∧ ∃ Y : Finset (Fin n),
          JoinedToTwo G T Y ∧ (1 / 6 - ε) * (n : ℝ) ≤ (Y.card : ℝ) := by
  sorry

/--
The construction of Ma and Tang [MaTa25] of a graph with $n$ vertices and $>n^2/4$ edges in which
every triangle has at most $(2-(5/2)^{1/2}+o(1))n$ vertices adjacent to at least two of its
vertices shows that, for the threshold $h(n)$ of `erdos_1034.variants.lower_bound`,
$$h(n) \leq (2-(5/2)^{1/2}+o(1))n.$$
-/
@[category research solved, AMS 5]
theorem erdos_1034.variants.upper_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop, ∃ G : SimpleGraph (Fin n),
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) ∧
        ∀ T : Finset (Fin n), G.IsNClique 3 T → ∀ Y : Finset (Fin n),
          JoinedToTwo G T Y → (Y.card : ℝ) ≤ (2 - Real.sqrt (5 / 2) + ε) * (n : ℝ) := by
  sorry

/--
Erdős suggested that the answer is different if $G$ has no $K_4$. In the comments Ma and Tang
sketch a proof that the conjecture remains false even if we assume that $G$ contains no $K_4$,
constructing a graph with $n$ vertices, $>n^2/4$ edges, and no $K_4$, in which every triangle has
at most $(2\sqrt{3}-3+o(1))n$ vertices adjacent to at least two of its vertices (note that
$2\sqrt{3}-3\approx 0.464$).
-/
@[category research solved, AMS 5]
theorem erdos_1034.variants.k4_free (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop, ∃ G : SimpleGraph (Fin n), G.CliqueFree 4 ∧
      (n : ℝ) ^ 2 / 4 < (G.edgeSet.ncard : ℝ) ∧
        ∀ T : Finset (Fin n), G.IsNClique 3 T → ∀ Y : Finset (Fin n),
          JoinedToTwo G T Y → (Y.card : ℝ) ≤ (2 * Real.sqrt 3 - 3 + ε) * (n : ℝ) := by
  sorry

end Erdos1034


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
