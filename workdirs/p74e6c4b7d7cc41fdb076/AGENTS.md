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
# Ringel's Conjecture and Kotzig's Conjecture for large $n$

*Reference:* [arxiv/2001.02665](https://arxiv.org/abs/2001.02665)
**A proof of Ringel's Conjecture**
by *Richard Montgomery, Alexey Pokrovskiy, Benny Sudakov*

The original conjecture of Ringel (1963), which remains open, is stated in
`Paper/RingelConjecture.lean`. The referenced paper proves it for all sufficiently large $n$.

Montgomery–Pokrovskiy–Sudakov actually prove the strictly stronger statement conjectured by
Kotzig: the decomposition can always be realized by cyclic shifts of a single copy of $T$.
Kotzig's conjecture (all $n$) remains open; see `Paper/KotzigConjecture.lean`.
-/
namespace Arxiv.«2001.02665»

open SimpleGraph

/--
For all sufficiently large $n$, the complete graph $K_{2n+1}$ decomposes into
$2n+1$ edge-disjoint copies of any tree $T$ with $n$ edges.

A "copy" of $T$ is the image $T.\text{map}(f_i)$ of $T$ under a vertex embedding
$f_i : V \hookrightarrow \text{Fin}(2n+1)$; the copies are pairwise edge-disjoint
and together cover every edge of $K_{2n+1}$.

This follows from `kotzig_conjecture_large`; see `Paper/RingelConjecture.lean` for the open form.
-/
@[category research solved, AMS 5]
theorem ringel_conjecture_large :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∀ {V : Type} [Finite V] (T : SimpleGraph V),
      T.IsTree → T.edgeSet.ncard = n →
      ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
        Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
        ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1))) := by
  sorry

/--
For all sufficiently large $n$, the complete graph $K_{2n+1}$ decomposes into
$2n+1$ edge-disjoint copies of any tree $T$ with $n$ edges via cyclic shifts of a single
embedding.

The $2n+1$ copies are $f_0, f_1, \dots, f_{2n}$ where $f_i(v) = f_0(v) + i$ for all vertices
$v$ — that is, each copy is obtained by adding $i \pmod{2n+1}$ to every vertex of the
base copy. This is strictly stronger than `ringel_conjecture_large`.

Kotzig conjectured this holds for all $n$; see `Paper/KotzigConjecture.lean`. Montgomery,
Pokrovskiy, and Sudakov prove it for all sufficiently large $n$.
-/
@[category research solved, AMS 5]
theorem kotzig_conjecture_large :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∀ {V : Type} [Finite V] (T : SimpleGraph V),
      T.IsTree → T.edgeSet.ncard = n →
      ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
        (∀ i v, f i v = f 0 v + i) ∧
        Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
        ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1))) := by
  sorry

end Arxiv.«2001.02665»


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
