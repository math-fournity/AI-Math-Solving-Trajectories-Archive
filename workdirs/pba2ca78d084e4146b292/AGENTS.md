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
# Written on the Wall II - Conjecture 327

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/

namespace WrittenOnTheWallII.GraphConjecture327

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α]

/--
WOWII [Conjecture 327](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

Let `G` be a simple connected graph. If `3 · γ(G) = γ_i(G)`, then `G` is well
totally dominated, where `γ(G)` is the domination number of `G` and `γ_i(G)` is
the independent domination number of `G`.

**Proof Sketch:**
The conjecture states that if $3\gamma(G) = i(G)$ for a connected graph $G$, then $G$ is well totally dominated.
However, this conjecture is **FALSE**.

**Counterexample:**
Consider a graph $G$ with 12 vertices: $u, v, a_0, a_1, a_2, a_3, a_4, b_0, b_1, b_2, b_3, b_4$.
The edges are:
- $(u, v)$
- $(u, a_i)$ for all $i \in \{0, 1, 2, 3, 4\}$
- $(v, b_i)$ for all $i \in \{0, 1, 2, 3, 4\}$
- $(a_0, b_3), (a_1, b_3), (a_2, b_0), (a_3, b_0), (a_4, b_3), (a_4, b_4)$

Properties of $G$:
1. **Connected**: Yes, path exists between any two vertices through $u$ and $v$.
2. **Domination Number $\gamma(G)$**: The set $\{u, v\}$ dominates all vertices. Since there is no universal vertex, $\gamma(G) = 2$.
3. **Independent Domination Number $i(G)$**: The minimum independent dominating set has size 6 (e.g., $\{u, b_0, b_1, b_2, b_3, b_4\}$). Thus $i(G) = 6$.
4. **Condition**: $3 \gamma(G) = 3 \times 2 = 6 = i(G)$. The condition holds.
5. **Well Totally Dominated**: A graph is well totally dominated if all minimal total dominating sets have the same size.
   - $\{u, v\}$ is a minimal total dominating set of size 2.
   - $\{v, b_0, b_3\}$ is a minimal total dominating set of size 3.
   Since $2 \neq 3$, $G$ is NOT well totally dominated.

The counterexample has been found by Moritz Firsching and Goran Žužić using an
experimental pipeline.
-/
@[category research solved, AMS 5, formal_proof using formal_conjectures at
"https://github.com/mo271/formal-conjectures/blob/6e85aabe821e6ddf718d050a5bd8f19a48e4f2d9/FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean#L233"]
theorem conjecture327 : answer(False) ↔
    ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj] (_hG : G.Connected)
      (_h : 3 * G.dominationNumber = G.indepDominationNumber),
      IsWellTotallyDominated G := by
  sorry

-- Sanity checks

/-- In `K₂`, the max degree is 1 (each vertex has exactly one neighbor). -/
@[category test, AMS 5]
example : (⊤ : SimpleGraph (Fin 2)).maxDegree = 1 := by decide +native

/-- In the path graph `P₃`, vertex 1 has degree 2. -/
@[category test, AMS 5]
example : (SimpleGraph.fromEdgeSet {s(0,1), s(1,2)} : SimpleGraph (Fin 3)).degree 1 = 2 := by
  decide +native
end WrittenOnTheWallII.GraphConjecture327


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
