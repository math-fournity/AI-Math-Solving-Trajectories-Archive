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
# Written on the Wall II - Conjecture 101

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

## Definitions

The **$\alpha$-core** of a graph $G$, written `alphaCore G`, is the set of vertices
$v$ such that removing $v$ strictly decreases the independence number:
$$\mathrm{alphaCore}(G) = \{v \mid \alpha(G - v) < \alpha(G)\}$$
where $G - v$ is the subgraph of $G$ induced on $V(G) \setminus \{v\}$.

These vertices are also called "critical vertices for independence."
-/

namespace WrittenOnTheWallII.GraphConjecture101

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]

/-- The independence number of the subgraph induced on $V \setminus \{v\}$
(i.e., the graph $G - v$). -/
noncomputable def indepNumDeleteVertex (G : SimpleGraph α) (v : α) : ℕ :=
  (G.induce (Set.univ \ {v})).indepNum

/-- The $\alpha$-core of $G$: the set of vertices whose removal strictly decreases the
independence number. A vertex $v$ is in the $\alpha$-core if $\alpha(G - v) < \alpha(G)$. -/
noncomputable def alphaCore (G : SimpleGraph α) : Finset α :=
  Finset.univ.filter (fun v => indepNumDeleteVertex G v < G.indepNum)

/--
WOWII [Conjecture 101](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

For a simple connected graph $G$,
$\alpha(G) \le \lfloor (n + |\mathrm{alphaCore}(G)|) / 2 \rfloor$
where $\alpha(G) = G.\mathrm{indepNum}$ is the independence number, $n$ is the
number of vertices, and $\mathrm{alphaCore}(G)$ is the set of vertices whose
removal decreases the independence number.

This is a theorem known to follow from inclusion-exclusion principles.
-/
@[category research solved, AMS 5]
theorem conjecture101 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    G.indepNum ≤ (Fintype.card α + (alphaCore G).card) / 2 := by
  sorry

-- Sanity checks

/-- The $\alpha$-core has cardinality at most $n$ (the number of vertices). -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) : (alphaCore G).card ≤ 3 := by
  apply Finset.card_le_univ

/-- The $\alpha$-core is always a subset of all vertices. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 5)) : alphaCore G ⊆ Finset.univ :=
  Finset.filter_subset _ _

/-- If a vertex $v$ is NOT in the $\alpha$-core, then removing $v$ does not decrease $\alpha$. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) (v : Fin 3)
    (hv : v ∉ alphaCore G) :
    G.indepNum ≤ indepNumDeleteVertex G v := by
  unfold alphaCore at hv
  simp [Finset.mem_filter] at hv
  exact hv

/-- If a vertex $v$ IS in the $\alpha$-core, then removing $v$ strictly decreases $\alpha$. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) (v : Fin 3)
    (hv : v ∈ alphaCore G) :
    indepNumDeleteVertex G v < G.indepNum := by
  unfold alphaCore at hv
  exact (Finset.mem_filter.mp hv).2

end WrittenOnTheWallII.GraphConjecture101


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
