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
# Written on the Wall II - Conjecture 145

The WOWII HTML uses $\lambda_{\min}(\overline{G})$ (the bar denotes graph complement).
The formal statement below uses the local-independence minimum of $G^c$.

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

## Definitions

The **local independence minimum** $\mathrm{lMin}(G)$ is:
$$\mathrm{lMin}(G) = \min_{v \in V(G)} l(v)$$
where $l(v) = \mathrm{indepNeighborsCard}(G, v)$ is the independence number of the
neighbourhood of $v$. This is the minimum over all vertices of the local
independence number.

The **boundary vertices** $B(G)$ of a connected graph are the vertices $v$ such
that the eccentricity of $v$ equals the diameter of $G$.

The **eccentricity of a set** $\mathrm{ecc}(S) = \max_{u \notin S} \min_{w \in S}
\mathrm{dist}(u, w)$. In the conjecture below, $\mathrm{ecc}(B)$ is the
eccentricity of the boundary set.

**Conjecture 145:** $\mathrm{tree}(G) \ge 2 \cdot \mathrm{ecc}(B) /
\lambda_{\min}(\overline{G})$ where $\mathrm{tree}(G)$ is `largestInducedTreeSize G`,
$\mathrm{ecc}(B)$ is the eccentricity of the boundary vertices, and
$\lambda_{\min}(\overline{G})$ is the local independence minimum of the complement
$\overline{G}$.
-/

namespace WrittenOnTheWallII.GraphConjecture145

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]

/-- `localIndependenceMin G` is the minimum over all vertices of the local independence
number `indepNeighborsCard G v`. This equals $\mathrm{lMin}$ from DeLaVina's notation. -/
noncomputable def localIndependenceMin (G : SimpleGraph α) : ℕ :=
  Finset.univ.inf' Finset.univ_nonempty (indepNeighborsCard G)

/--
WOWII [Conjecture 145](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

For a simple connected graph $G$,
$\mathrm{tree}(G) \ge 2 \cdot \mathrm{ecc}(B) / \lambda_{\min}(\overline{G})$
where $\mathrm{tree}(G)$ is the number of vertices in a largest induced subtree,
$\mathrm{ecc}(B)$ is the eccentricity of the boundary vertices (`eccSet` and
`boundaryVertices`), and $\lambda_{\min}(\overline{G})$ is the minimum local
independence number of the complement graph.

We state the inequality in the form
$\mathrm{tree}(G) \cdot \mathrm{lMin}(\overline{G}) \ge 2 \cdot \mathrm{ecc}(B)$
to avoid division.
-/
@[category research open, AMS 5]
theorem conjecture145 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hlMin : 0 < localIndependenceMin Gᶜ) :
    2 * eccSet G (maxEccentricityVertices G : Set α) ≤
    largestInducedTreeSize G * localIndependenceMin Gᶜ := by
  sorry

-- Sanity checks

/-- `largestInducedTreeSize` is nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) : 0 ≤ largestInducedTreeSize G := Nat.zero_le _

/-- `localIndependenceMin` is nonneg (it is a natural number). -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) : 0 ≤ localIndependenceMin G := Nat.zero_le _

/-- For any graph on `Fin 3`, `eccSet` is nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) [DecidableRel G.Adj] : 0 ≤ eccSet G (maxEccentricityVertices G) :=
  Nat.zero_le _

/-- `maxEccentricityVertices` is a subset of all vertices. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 4)) : maxEccentricityVertices G ⊆ Set.univ := by
  intro v _; exact Set.mem_univ v

/-- `localIndependenceMin G` is at most `indepNeighborsCard G v` for any vertex `v`.
This follows from the definition of `inf'` as the minimum. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 4)) (v : Fin 4) :
    localIndependenceMin G ≤ indepNeighborsCard G v := by
  unfold localIndependenceMin
  apply Finset.inf'_le
  exact Finset.mem_univ v

/-- `localIndependenceMin G` is a natural number, hence nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 4)) : 0 ≤ localIndependenceMin G := Nat.zero_le _

end WrittenOnTheWallII.GraphConjecture145


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
