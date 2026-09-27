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
# Written on the Wall II - Conjecture 315

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

## Definitions

The notions `IsTotalDominatingSet`, `IsMinimalTotalDominatingSet`,
`IsWellTotallyDominated`, and `pendantVertices` live in
`FormalConjecturesForMathlib.Combinatorics.SimpleGraph.GraphConjectures.WellTotallyDominated`.
-/


namespace WrittenOnTheWallII.GraphConjecture315

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α]

/--
WOWII [Conjecture 315](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

Let $G$ be a simple connected graph and let $P$ denote the set of pendant vertices
(vertices of degree $1$). If $\alpha(G) = |P|$, then $G$ is well totally dominated.

A formal proof of this conjectures has been obtained by Goran Žužić and Moritz Firsching using an
experimental pipeline.
-/
@[category research solved, AMS 5, formal_proof using formal_conjectures at
"https://github.com/mo271/formal-conjectures/blob/9ef80e1a3709ed3eda43d9ed6ff1087681621041/FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean#L43"]
theorem conjecture315 (G : SimpleGraph α) [DecidableRel G.Adj] (hG : G.Connected)
    (h : G.indepNum = (pendantVertices G).card) :
    IsWellTotallyDominated G := by
  sorry

-- Sanity checks

/-- In the path graph $P_3$ ($0$-$1$-$2$), vertices $0$ and $2$ have degree $1$,
so there are exactly $2$ pendant vertices. -/
@[category test, AMS 5]
example : (pendantVertices (SimpleGraph.fromEdgeSet {s(0,1), s(1,2)} : SimpleGraph (Fin 3))).card = 2 := by
  unfold pendantVertices
  decide +native

/-- In $K_3$, all vertices have degree $2$, so there are no pendant vertices. -/
@[category test, AMS 5]
example : (pendantVertices (⊤ : SimpleGraph (Fin 3))).card = 0 := by
  unfold pendantVertices
  decide +native

/-- In $K_2$, both vertices have degree $1$, so both are pendant vertices. -/
@[category test, AMS 5]
example : (pendantVertices (⊤ : SimpleGraph (Fin 2))).card = 2 := by
  unfold pendantVertices
  decide +native

/-- In $K_2$, the pendant set is exactly $\{0, 1\}$. -/
@[category test, AMS 5]
example : pendantVertices (⊤ : SimpleGraph (Fin 2)) = Finset.univ := by
  unfold pendantVertices
  decide +native

/-- In the edgeless graph on $3$ vertices, no vertex has degree $1$, so there are $0$ pendant vertices. -/
@[category test, AMS 5]
example : (pendantVertices (⊥ : SimpleGraph (Fin 3))).card = 0 := by
  unfold pendantVertices
  decide +native

/-- $\{0, 1\}$ is a total dominating set of $K_2$: every vertex has a neighbor in $\{0, 1\}$. -/
@[category test, AMS 5]
example : IsTotalDominatingSet (⊤ : SimpleGraph (Fin 2)) Finset.univ := by
  unfold IsTotalDominatingSet
  intro v
  fin_cases v <;> simp

/-- $\{0, 1\}$ is NOT a total dominating set of the edgeless graph on $2$ vertices,
since no vertex has a neighbor in the empty edge set. -/
@[category test, AMS 5]
example : ¬IsTotalDominatingSet (⊥ : SimpleGraph (Fin 2)) Finset.univ := by
  unfold IsTotalDominatingSet
  push_neg
  exact ⟨0, fun w _ => by simp⟩

end WrittenOnTheWallII.GraphConjecture315


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
