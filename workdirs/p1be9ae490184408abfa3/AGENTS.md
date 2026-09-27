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
# Steiner Systems

A Steiner system $S(t, k, n)$ is a collection of $k$-element subsets (called blocks) of
an $n$-element set such that every $t$-element subset is contained in exactly one block.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Steiner_system)
- [Large Steiner Systems](https://epoch.ai/frontiermath/open-problems/large-steiner-systems)
  by Kunal Marwaha
-/

namespace SteinerSystems

/--
An $S(t, k, n)$-Steiner system is a collection of $k$-element subsets (called blocks) of
$\{0, \ldots, n-1\}$ such that every $t$-element subset is contained in exactly one block.

This is the standard notation from combinatorics, where:
- $n$ is the number of points
- $k$ is the block size
- $t$ is the covering parameter (every $t$-subset is in exactly one block)
-/
structure SteinerSystem (t k n : ℕ) where
  /-- The blocks of the Steiner system. -/
  blocks : Finset (Finset (Fin n))
  /-- Every block has exactly $k$ elements. -/
  block_card : ∀ B ∈ blocks, B.card = k
  /-- Every $t$-element subset is contained in exactly one block.
  Note: We use `.filter.card = 1` instead of `∃!` because `∃! B ∈ blocks, R ⊆ B` desugars to
  a quantifier over all `Finset (Fin n)`, which loses `Decidable` and breaks `native_decide`. -/
  cover_unique : ∀ R : Finset (Fin n), R.card = t → (blocks.filter (R ⊆ ·)).card = 1

/-- Notation for Steiner systems: `S(t, k, n)` denotes a Steiner system with
covering parameter `t`, block size `k`, and `n` points. -/
scoped notation "S(" t ", " k ", " n ")" => SteinerSystem t k n

/--
A constructive witness for a large Steiner system: concrete values of $n$, $k$, $t$
satisfying $n > k > t > 5$, $t < 10$, $n < 200$, together with an explicit Steiner system.
-/
structure LargeSteinerSystemWitness where
  /-- The size of the ground set. -/
  n : ℕ
  /-- The block size. -/
  k : ℕ
  /-- The covering parameter. -/
  t : ℕ
  h_nk : n > k
  h_kt : k > t
  h_t_lower : t > 5
  h_t_upper : t < 10
  h_n_upper : n < 200
  /-- The explicit Steiner system. -/
  system : S(t, k, n)

/--
Construct an $S(t, k, n)$-Steiner system with $n > k > t > 5$, $t < 10$, and $n < 200$.

No example of a Steiner system with $t > 5$ is known, despite a 2014 existence theorem
by Keevash showing that such systems must exist for sufficiently large $n$.

*Reference:* [Large Steiner Systems](https://epoch.ai/frontiermath/open-problems/large-steiner-systems)
-/
@[category research open, AMS 5]
def large_steiner_systems : LargeSteinerSystemWitness := by
  sorry

/--
Sanity check: the Fano plane is an $S(2, 3, 7)$-Steiner system.

The Fano plane consists of $7$ blocks of size $3$ over $7$ points,
where every pair of points is contained in exactly one block.
-/
@[category test, AMS 5]
def fano_plane : S(2, 3, 7) :=
  ⟨{{(0 : Fin 7), 1, 3}, {1, 2, 4}, {2, 3, 5},
    {3, 4, 6}, {0, 4, 5}, {1, 5, 6}, {0, 2, 6}},
   by native_decide, by native_decide⟩

/--
**Existence of $S(5, 6, 12)$**: The small Witt design.

There exists a unique Steiner system $S(5, 6, 12)$, known as the small Witt design.
It was constructed by Witt (1938) and is closely related to the Mathieu group $M_{12}$.
This is one of only two known Steiner systems with $t = 5$.
-/
@[category research solved, AMS 5]
theorem steiner_system_5_6_12 : Nonempty S(5, 6, 12) :=
  ⟨⟨{{0, 1, 2, 3, 4, 9},
    {0, 1, 2, 3, 5, 11},
    {0, 1, 2, 3, 6, 7},
    {0, 1, 2, 3, 8, 10},
    {0, 1, 2, 4, 5, 7},
    {0, 1, 2, 4, 6, 8},
    {0, 1, 2, 4, 10, 11},
    {0, 1, 2, 5, 6, 10},
    {0, 1, 2, 5, 8, 9},
    {0, 1, 2, 6, 9, 11},
    {0, 1, 2, 7, 8, 11},
    {0, 1, 2, 7, 9, 10},
    {0, 1, 3, 4, 5, 8},
    {0, 1, 3, 4, 6, 10},
    {0, 1, 3, 4, 7, 11},
    {0, 1, 3, 5, 6, 9},
    {0, 1, 3, 5, 7, 10},
    {0, 1, 3, 6, 8, 11},
    {0, 1, 3, 7, 8, 9},
    {0, 1, 3, 9, 10, 11},
    {0, 1, 4, 5, 6, 11},
    {0, 1, 4, 5, 9, 10},
    {0, 1, 4, 6, 7, 9},
    {0, 1, 4, 7, 8, 10},
    {0, 1, 4, 8, 9, 11},
    {0, 1, 5, 6, 7, 8},
    {0, 1, 5, 7, 9, 11},
    {0, 1, 5, 8, 10, 11},
    {0, 1, 6, 7, 10, 11},
    {0, 1, 6, 8, 9, 10},
    {0, 2, 3, 4, 5, 6},
    {0, 2, 3, 4, 7, 10},
    {0, 2, 3, 4, 8, 11},
    {0, 2, 3, 5, 7, 8},
    {0, 2, 3, 5, 9, 10},
    {0, 2, 3, 6, 8, 9},
    {0, 2, 3, 6, 10, 11},
    {0, 2, 3, 7, 9, 11},
    {0, 2, 4, 5, 8, 10},
    {0, 2, 4, 5, 9, 11},
    {0, 2, 4, 6, 7, 11},
    {0, 2, 4, 6, 9, 10},
    {0, 2, 4, 7, 8, 9},
    {0, 2, 5, 6, 7, 9},
    {0, 2, 5, 6, 

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
