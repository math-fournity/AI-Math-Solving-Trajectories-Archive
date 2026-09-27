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
# Erdős Problem 1037

*References:*
- [erdosproblems.com/1037](https://www.erdosproblems.com/1037)
- [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
  Quaestiones Math. (1993), 333-350.
-/

open Filter

namespace Erdos1037

/--
A set `s` of vertices of a graph `G` is *trivial* if the subgraph it induces is empty or
complete, that is, if `s` is an independent set or a clique of `G`.
-/
def IsTrivialSet {V : Type*} (G : SimpleGraph V) (s : Set V) : Prop :=
  G.IsIndepSet s ∨ G.IsClique s

/--
Let $G$ be a graph on $n$ vertices in which every degree occurs at most twice, and the number of
distinct degrees is $>(\frac{1}{2}+\epsilon)n$. Must $G$ contain a trivial (empty or complete)
subgraph of size 'much larger' than $\log n$?

A question of Chen and Erdős.

The answer is no - Cambie, Chan, and Hunter have in the comment section given a simple
construction of a graph on $n$ vertices with at least $\frac{3}{4}n$ distinct degrees, every
degree appears at most twice, and the largest trivial subgraph has size $O(\log n)$.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1037.lean"]
theorem erdos_1037 : answer(False) ↔
    ∀ ε : ℝ, 0 < ε → ∀ C : ℝ, ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (∀ d : ℕ, {v : Fin n | (G.neighborSet v).ncard = d}.ncard ≤ 2) →
      ((1 / 2 + ε) * (n : ℝ) <
        ((Set.range fun v : Fin n => (G.neighborSet v).ncard).ncard : ℝ)) →
      ∃ s : Set (Fin n), IsTrivialSet G s ∧ (C * Real.log (n : ℝ) < (s.ncard : ℝ)) := by
  sorry

/--
Cambie, Chan, and Hunter have in the comment section given a simple construction of a graph on
$n$ vertices with at least $\frac{3}{4}n$ distinct degrees, every degree appears at most twice,
and the largest trivial subgraph has size $O(\log n)$.
-/
@[category research solved, AMS 5]
theorem erdos_1037.variants.cambie_chan_hunter :
    ∃ C : ℝ, ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      (∀ d : ℕ, {v : Fin n | (G.neighborSet v).ncard = d}.ncard ≤ 2) ∧
      (3 / 4 * (n : ℝ) ≤
        ((Set.range fun v : Fin n => (G.neighborSet v).ncard).ncard : ℝ)) ∧
      ∀ s : Set (Fin n), IsTrivialSet G s → ((s.ncard : ℝ) ≤ C * Real.log (n : ℝ)) := by
  sorry

end Erdos1037


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
