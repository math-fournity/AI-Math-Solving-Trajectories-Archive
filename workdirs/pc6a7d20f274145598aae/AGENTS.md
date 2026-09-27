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
# Written on the Wall II - Conjecture 160

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

## Definitions

For a vertex $v$ in $G$, **$T(v)$** is the number of triangles incident to $v$:
$$T(v) = |\{\{u, w\} \subseteq N(v) \mid u \sim w\}|$$
i.e., the number of pairs of neighbors of $v$ that are themselves adjacent.

The invariant `maxTrianglesAtVertex G` is the maximum of $T(v)$ over all vertices.

Conjecture 160 uses both $\max_v T(v)$ and $\chi_{C_4}(G)$, the $C_4$-free
characteristic function: it is `1` when $G$ contains no cycle of length four
and `0` otherwise. The cycle need not be induced. These invariants lower-bound
the WOWII invariant $L_s(G)$, the maximum number of leaves over all spanning
trees of $G$ (exposed as `SimpleGraph.Ls G : ℝ`).

The earlier formalization used the number of induced four-cycles. The historical
conjecture instead uses this binary $C_4$-free indicator.

-/

namespace WrittenOnTheWallII.GraphConjecture160

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]

/-- The maximum number of triangles incident to any vertex in $G$. -/
noncomputable def maxTrianglesAtVertex (G : SimpleGraph α) [DecidableRel G.Adj] : ℕ :=
  (Finset.univ.image (numTrianglesAtVertex G)).max' (Finset.image_nonempty.mpr Finset.univ_nonempty)

open scoped Classical in
/--
WOWII [Conjecture 160](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

For a simple connected graph $G$,
$L_s(G) \ge \max_v l(v) + \max_v T(v) \cdot \chi_{C_4}(G)$
where:

- $L_s(G) = \mathrm{SimpleGraph.Ls}\, G$ is the maximum number of leaves over all
  spanning trees of $G$,
- $\max_v l(v)$ is the maximum local independence number over vertices,
- $\max_v T(v)$ is the maximum number of triangles incident to any vertex,
- $\chi_{C_4}(G)$ is `1` if $G$ has no cycle of length four and `0` otherwise.
-/
@[category research open, AMS 5]
theorem conjecture160 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let maxL := (Finset.univ.image (indepNeighborsCard G)).max' (by simp)
    let maxT := maxTrianglesAtVertex G
    let cC4 : ℕ := if ∃ v : α, ∃ c : G.Walk v v, c.IsCycle ∧ c.length = 4 then 0 else 1
    (maxL : ℝ) + (maxT : ℝ) * (cC4 : ℝ) ≤ Ls G := by
  sorry

-- Sanity checks

/-- In $K_3$, every vertex has $1$ triangle incident to it. -/
@[category test, AMS 5]
example : numTrianglesAtVertex (⊤ : SimpleGraph (Fin 3)) (0 : Fin 3) = 1 := by
  unfold numTrianglesAtVertex
  decide +native

/-- In $K_3$, `maxTrianglesAtVertex = 1`. -/
@[category test, AMS 5]
example : maxTrianglesAtVertex (⊤ : SimpleGraph (Fin 3)) = 1 := by
  unfold maxTrianglesAtVertex numTrianglesAtVertex
  decide +native

/-- In the path $P_3$, vertex $1$ is adjacent to $0$ and $2$, but $0$ and $2$ are not adjacent.
So $T(1) = 0$. -/
@[category test, AMS 5]
example : numTrianglesAtVertex
    (SimpleGraph.fromEdgeSet {s(0,1), s(1,2)} : SimpleGraph (Fin 3)) (1 : Fin 3) = 0 := by
  unfold numTrianglesAtVertex
  decide +native

end WrittenOnTheWallII.GraphConjecture160


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
