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
Copyright 2025 The Formal Conjectures Authors.

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
# Erdős Problem 541

*References:*
- [erdosproblems.com/541](https://www.erdosproblems.com/541)
- [ErSz76] Erdős, E. and Szemerédi, E., On a problem of Graham. Publ. Math. Debrecen (1976),
  123--127.
- [GHW10] Gao, Weidong and Hamidoune, Yahya Ould and Wang, Guoqing, Distinct length modular zero-sum
  subsequences: a proof of Graham's conjecture. J. Number Theory (2010), 1425--1431.
-/

open Filter

namespace Erdos541

/--
Let $a_1, \dots, a_p$ be (not necessarily distinct) residues modulo a prime $p$, such that there
exists some $r$ so that if $S \subseteq [p]$ is non-empty and
$$\sum_{i \in S} a_i \equiv 0 \pmod{p}$$
then $|S| = r$.

Must there be at most two distinct residues amongst the $a_i$?

This was formalized in Lean by Alexeev using Aristotle and ChatGPT.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos541.lean"]
theorem erdos_541 : answer(True) ↔ (∀ p, Fact p.Prime → ∀ (a : Fin p → ZMod p),
    (∃ r, ∀ (S : Finset (Fin p)), S ≠ ∅ → ∑ i ∈ S, a i = 0 → S.card = r) →
      (Set.range a).ncard ≤ 2) := by
  sorry

/-- Gao, Hamidoune, and Wang [GHW10] solved this for all moduli `p` (not necessarily prime). -/
@[category research solved, AMS 11]
theorem erdos_541.variants.general_moduli (p : ℕ) (a : Fin p → ZMod p)
    (ha₀ : ∃ r, ∀ (S : Finset (Fin p)), S ≠ ∅ → ∑ i ∈ S, a i = 0 → S.card = r) :
      (Set.range a).ncard ≤ 2 := by
  sorry

/-- This was proved by Erdős and Szemerédi [ErSz76] for p sufficiently large. -/
@[category research solved, AMS 11]
theorem erdos_541.variants.large_primes : ∀ᶠ p in atTop, p.Prime → ∀ a : Fin p → ZMod p,
    (∃ r, ∀ (S : Finset (Fin p)), S ≠ ∅ → ∑ i ∈ S, a i = 0 → S.card = r) →
      (Set.range a).ncard ≤ 2 := by
  sorry

end Erdos541


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
