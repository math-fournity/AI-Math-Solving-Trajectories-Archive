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
# Written on the Wall II - Conjecture 142

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/

namespace WrittenOnTheWallII.GraphConjecture142

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]

/--
WOWII [Conjecture 142](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/):

For a simple connected graph $G$,
$\mathrm{tree}(G) \ge (2/3) \cdot \mathrm{girth}(G) + \mathrm{ecc}(B)$
where $\mathrm{tree}(G)$ is the largest induced tree size, $\mathrm{girth}(G)$
is the length of the shortest cycle ($0$ if acyclic), $B$ is the set of
boundary vertices (those of maximum eccentricity), and $\mathrm{ecc}(B)$ is
the eccentricity of the set $B$.

**Proof sketch.** The proof first strengthens the real-valued target to the
integral bound
$$
\mathrm{ecc}(B) + \mathrm{girth}(G)
  - \lfloor \mathrm{girth}(G) / 3 \rfloor \leq \mathrm{tree}(G).
$$
For a cyclic graph, start with a shortest cycle $K$. It is chordless, so
removing one vertex leaves an induced path on $\mathrm{girth}(G)-1$ vertices.
Shortest paths from selected vertices to $K$ are called *descents*. Pairwise
noninteracting descents attach to the retained cycle path as disjoint branches.
If two descents interact, the proof cuts at the first interaction encountered
from the outer endpoint toward the cycle and splices the paths there.
Minimality of that interaction makes the retained prefix disjoint and
nonadjacent to the first descent; geodesicity excludes chords, while girth at
least five rules out extra cross-edges and cycle attachments.

Choose a vertex realizing $\mathrm{ecc}(B)$ and two endpoints of a diametral
geodesic. Either two of their descents interact, directly giving a sufficiently
long spliced tree, or all three are separate, in which case a three-point
distance inequality forces their total length to be large enough. This proves
the integral bound in the main range. Girths three and four, small
$\mathrm{ecc}(B)$, and the two remaining congruence cases are handled by
separate geodesic/cycle certificates with one or two descents; the acyclic case
follows from a diametral path. Finally,
$$
\mathrm{girth}(G)-\lfloor\mathrm{girth}(G)/3\rfloor
  = \lceil 2\,\mathrm{girth}(G)/3\rceil
  \geq 2\,\mathrm{girth}(G)/3,
$$
which gives the stated real-valued inequality.

The argument was developed with assistance from ChatGPT Pro. The linked Lean 4
formalization was produced with assistance from OpenAI Codex and checked by
Lean.
-/
@[category research solved, AMS 5,
  formal_proof using formal_conjectures at "https://github.com/AlperTheKing/formal-conjectures/blob/46bf39015f5c3c3ba3bfcf9f752b4b1e49b584ac/FormalConjecturesForMathlib/WrittenOnTheWallII/GraphConjecture142Proof.lean#L3927-L3932"]
theorem conjecture142 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let B : Set α := (maxEccentricityVertices G : Set α)
    (2 : ℝ) / 3 * (G.girth : ℝ) + (eccSet G B : ℝ) ≤ (largestInducedTreeSize G : ℝ) := by
  sorry

-- Sanity checks

/-- The `largestInducedTreeSize` is nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) : 0 ≤ largestInducedTreeSize G := Nat.zero_le _

/-- `eccSet G` returns a natural number (nonneg). -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) [DecidableRel G.Adj] :
    0 ≤ eccSet G (maxEccentricityVertices G) :=
  Nat.zero_le _

end WrittenOnTheWallII.GraphConjecture142


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
