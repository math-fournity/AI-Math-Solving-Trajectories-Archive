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
# Erdős Problem 862

*References:*
- [erdosproblems.com/862](https://www.erdosproblems.com/862)
- [Er92c] Erdős, P., *Some of my forgotten problems in number theory*. Hardy-Ramanujan J. (1992),
  34-50.
- [SaTh15] Saxton, David and Thomason, Andrew, *Hypergraph containers*. Invent. Math. (2015),
  925-992.
-/

open Finset Filter

namespace Erdos862

/--
$A_1(N)$, the number of maximal Sidon subsets of $\{1, \dots, N\}$.
-/
noncomputable def numMaximalSidonSets (N : ℕ) : ℕ :=
  {A : Finset ℕ | A ⊆ Icc 1 N ∧ Set.IsMaximalSidonSetIn (A : Set ℕ) N}.ncard

/--
Let $A_1(N)$ be the number of maximal Sidon subsets of $\{1,\ldots,N\}$. Is it true that
$$A_1(N) < 2^{o(N^{1/2})}?$$

A problem of Cameron and Erdős. This is resolved as a consequence of results of Saxton and
Thomason [SaTh15] - they prove that the number of Sidon sets in $\{1,\ldots,N\}$ is at least
$2^{(1.16+o(1))N^{1/2}}$. Since each Sidon set is contained in a maximal Sidon set, and each
maximal Sidon set contains at most $2^{(1+o(1))N^{1/2}}$ Sidon sets, it follows that
$$A_1(N) \geq 2^{(0.16+o(1))N^{1/2}}.$$
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos862.lean"]
theorem erdos_862.parts.i : answer(False) ↔
    (fun N : ℕ => Real.logb 2 (numMaximalSidonSets N : ℝ)) =o[atTop]
      (fun N : ℕ => (N : ℝ) ^ (1 / 2 : ℝ)) := by
  sorry

/--
Let $A_1(N)$ be the number of maximal Sidon subsets of $\{1,\ldots,N\}$. Is it true that
$$A_1(N) > 2^{N^c}$$
for some constant $c>0$?

A problem of Cameron and Erdős. This is resolved as a consequence of results of Saxton and
Thomason [SaTh15] - they prove that the number of Sidon sets in $\{1,\ldots,N\}$ is at least
$2^{(1.16+o(1))N^{1/2}}$. Since each Sidon set is contained in a maximal Sidon set, and each
maximal Sidon set contains at most $2^{(1+o(1))N^{1/2}}$ Sidon sets, it follows that
$$A_1(N) \geq 2^{(0.16+o(1))N^{1/2}}.$$
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos862.lean"]
theorem erdos_862.parts.ii : answer(True) ↔
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N : ℕ in atTop,
      (2 : ℝ) ^ ((N : ℝ) ^ c) < (numMaximalSidonSets N : ℝ) := by
  sorry

/--
This is resolved as a consequence of results of Saxton and Thomason [SaTh15] - they prove that
the number of Sidon sets in $\{1,\ldots,N\}$ is at least $2^{(1.16+o(1))N^{1/2}}$. Since each
Sidon set is contained in a maximal Sidon set, and each maximal Sidon set contains at most
$2^{(1+o(1))N^{1/2}}$ Sidon sets, it follows that
$$A_1(N) \geq 2^{(0.16+o(1))N^{1/2}}.$$
-/
@[category research solved, AMS 5 11]
theorem erdos_862.variants.lower_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop,
      (2 : ℝ) ^ (((0.16 : ℝ) - ε) * (N : ℝ) ^ (1 / 2 : ℝ)) ≤ (numMaximalSidonSets N : ℝ) := by
  sorry

end Erdos862


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
