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
# Written on the Wall II - Conjecture 314

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/


namespace WrittenOnTheWallII.GraphConjecture314

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- The size of a largest induced path of $G$, as a natural number.

A subset $s \subseteq V(G)$ is an *induced path* when the induced subgraph
`G.induce s` is a tree in which every vertex has degree at most $2$
(equivalently: a tree that is itself a path graph). We define
`largestInducedPathSize G` as the supremum of `s.card` over all such subsets.

**Disambiguation.** This is *not* the `SimpleGraph.path` invariant, which is the
floor of the average distance — that one is the wrong tool for WOWII Conjecture
314, where $\mathrm{path}(G)$ denotes the **size of a largest induced path**.

TODO: it would probably be clearer to rename the `SimpleGraph.path` invariant to
something like `pathBound` / `floorAvgDist` to avoid this naming collision. -/
noncomputable def largestInducedPathSize (G : SimpleGraph α) [DecidableRel G.Adj] : ℕ :=
  sSup { n | ∃ s : Finset α,
              s.card = n ∧
              (G.induce (s : Set α)).IsTree ∧
              ∀ v : (s : Set α), (G.induce (s : Set α)).degree v ≤ 2 }

/--
WOWII [Conjecture 314](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj314):

For every finite simple connected graph $G$ with $n > 1$ vertices,
if $G$ is triangle-free and $\mathrm{path}(G) \le 4$, then $G$ is well totally
dominated.

Here $\mathrm{path}(G) = \mathrm{largestInducedPathSize}\, G$ is the **size of a
largest induced path** in $G$, defined locally above.

**Disambiguation.** Earlier revisions of this file used the `SimpleGraph.path`
invariant, but that is the *floor of the average distance*, not the size of a
largest induced path — a different quantity that makes Conjecture 314 vacuous
in many cases.
-/
@[category research open, AMS 5]
theorem conjecture314 [Nontrivial α] (G : SimpleGraph α) [DecidableRel G.Adj]
    (hG : G.Connected)
    (hTriFree : ∀ a b c : α, G.Adj a b → G.Adj b c → G.Adj c a → False)
    (hPath : largestInducedPathSize G ≤ 4) :
    IsWellTotallyDominated G := by
  sorry

-- Sanity checks

/-- The complete graph $K_3$ has a triangle. -/
@[category test, AMS 5]
example : ∃ a b c : Fin 3, (⊤ : SimpleGraph (Fin 3)).Adj a b ∧
    (⊤ : SimpleGraph (Fin 3)).Adj b c ∧ (⊤ : SimpleGraph (Fin 3)).Adj c a := by
  exact ⟨0, 1, 2, by decide, by decide, by decide⟩

/-- `largestInducedPathSize G` is nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 3)) [DecidableRel G.Adj] :
    0 ≤ largestInducedPathSize G := Nat.zero_le _

end WrittenOnTheWallII.GraphConjecture314


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
