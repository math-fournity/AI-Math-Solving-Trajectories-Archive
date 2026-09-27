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
# Erdős Problem 363

*References:*
- [erdosproblems.com/363](https://www.erdosproblems.com/363)
- [BaBe07] Bauer, Mark and Bennett, Michael A., *On a question of Erd\H{o}s
  and Graham*. Enseign. Math. (2) (2007), 259--264.
- [BeVL12] Bennett, Michael A. and Van Luijk, Ronald, *Squares from blocks of
  consecutive integers: a problem of Erd\H{o}s and Graham*. Indag. Math. (N.S.)
  (2012), 123--127.
- [Ul05] Ulas, Maciej, *On products of disjoint blocks of consecutive integers*.
  Enseign. Math. (2) (2005), 331--334.
-/

namespace Erdos363

open Finset

/-- A finite set of naturals is an interval of naturals. -/
def IsInterval (I : Finset ℕ) : Prop :=
  ∃ a b : ℕ, I = Icc a b

/-- A collection of intervals as in Erdős Problem 363. -/
def IsValidCollection (S : List (Finset ℕ)) : Prop :=
  (∀ I ∈ S, IsInterval I) ∧
  (∀ I ∈ S, 4 ≤ I.card) ∧
  S.Pairwise Disjoint ∧
  IsSquare ((S.map (fun I => ∏ m ∈ I, m)).prod)

/--
Is it true that there are only finitely many collections of disjoint intervals $I_1,\ldots,I_n$ of size $\lvert I_i\rvert \geq 4$ for $1\leq i\leq n$ such that$$\prod_{1\leq i\leq n}\prod_{m\in I_i}m$$is a square?

This is false: Ulas [Ul05] constructed infinitely many such collections.
-/
@[category research solved, AMS 11,
  formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos363.lean"]
theorem erdos_363 : answer(False) ↔ {S : List (Finset ℕ) | IsValidCollection S}.Finite := by
  sorry

end Erdos363


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
