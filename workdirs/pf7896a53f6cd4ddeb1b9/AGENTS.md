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
# Written on the Wall II - Conjecture 217

Per the WOWII definitions popup linked from this conjecture:

- $L(G)$ is the **maximum number of leaves of a spanning tree** of $G$
  — i.e. `Ls G` in our invariant library.
- $\chi_{\mathrm{residue}=2}(G)$ is the **characteristic function** for the
  predicate $\mathrm{residue}\, G = 2$, i.e. $1$ when $\mathrm{residue}\, G = 2$
  and $0$ otherwise. It is not a connected-component count of any 2-core.

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
-/

namespace WrittenOnTheWallII.GraphConjecture217

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]

/-- The **characteristic function** for the predicate $\mathrm{residue}\, G = 2$:
returns $1$ when $G.\mathrm{residue} = 2$ and $0$ otherwise. This is the WOWII
$\chi_{\mathrm{residue}=2}(G)$ indicator appearing in Conjecture 217. -/
noncomputable def residueEqTwoIndicator (G : SimpleGraph α) [DecidableRel G.Adj] : ℕ :=
  if residue G = 2 then 1 else 0

/--
WOWII [Conjecture 217](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj217):

If $G$ is a finite simple connected graph on $n > 1$ vertices and
$L_s(G) \le 4 \cdot \chi_{\mathrm{residue}=2}(G) + 2$,
then $G$ has a Hamiltonian path. Here $L_s(G)$ is the maximum number of
leaves over all spanning trees and $\chi_{\mathrm{residue}=2}(G)$ is the indicator
of $\mathrm{residue}(G) = 2$.
-/
@[category research solved, AMS 5,
  formal_proof using lean4 at
    "https://github.com/KitaKen1/wowii-graph-conjecture-217-lean/blob/6a2fb82fcd17aa15ec734736740794bb8bd194c0/lean/GraphConjecture217Audit.lean"]
theorem conjecture217 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected)
    (hL : Ls G ≤ 4 * (residueEqTwoIndicator G : ℝ) + 2) :
    ∃ a b : α, ∃ p : G.Walk a b, p.IsHamiltonian := by
  sorry

-- Sanity checks

/-- `residueEqTwoIndicator` is always $0$ or $1$. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 4)) [DecidableRel G.Adj] :
    residueEqTwoIndicator G ≤ 1 := by
  unfold residueEqTwoIndicator; split <;> simp

/-- `residueEqTwoIndicator` is nonneg. -/
@[category test, AMS 5]
example (G : SimpleGraph (Fin 4)) [DecidableRel G.Adj] :
    0 ≤ residueEqTwoIndicator G := Nat.zero_le _

-- The `Ls G` invariant is nonneg by construction (sSup of nonneg leaf counts);
-- proving it requires the sSup-nonempty / above-bound machinery. We omit a
-- sanity check here to avoid pulling in that infrastructure for a single test.

end WrittenOnTheWallII.GraphConjecture217


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
