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
# Cunningham chains

A Cunningham chain is a sequence of primes satisfying either $p_{i+1}=2p_i+1$
(first kind) or $p_{i+1}=2p_i-1$ (second kind). It is conjectured that there
are infinitely many chains of every positive exact length, of both kinds.

*References:*
- Lenny Jones, [Polynomial Cunningham Chains](https://arxiv.org/abs/1104.1579)
- [OEIS A181697](https://oeis.org/A181697), first-kind chain lengths
- [OEIS A181715](https://oeis.org/A181715), second-kind chain lengths
-/

namespace CunninghamChain

/-- The `n`th term generated from `p` by the first-kind recurrence `q ↦ 2q + 1`. -/
def firstKindTerm (p : ℕ) : ℕ → ℕ
  | 0 => p
  | n + 1 => 2 * firstKindTerm p n + 1

/-- The `n`th term generated from `p` by the second-kind recurrence `q ↦ 2q - 1`. -/
def secondKindTerm (p : ℕ) : ℕ → ℕ
  | 0 => p
  | n + 1 => 2 * secondKindTerm p n - 1

/-- `p` starts a first-kind Cunningham chain of exact positive length `k`. -/
def IsFirstKindChainOfLength (p k : ℕ) : Prop :=
  0 < k ∧ (∀ i < k, (firstKindTerm p i).Prime) ∧ ¬(firstKindTerm p k).Prime

/-- `p` starts a second-kind Cunningham chain of exact positive length `k`. -/
def IsSecondKindChainOfLength (p k : ℕ) : Prop :=
  0 < k ∧ (∀ i < k, (secondKindTerm p i).Prime) ∧ ¬(secondKindTerm p k).Prime

@[category test, AMS 11]
theorem two_starts_firstKind_length_five : IsFirstKindChainOfLength 2 5 := by
  refine ⟨by norm_num, ?_, by norm_num [firstKindTerm]⟩
  intro i hi
  interval_cases i <;> norm_num [firstKindTerm]

@[category test, AMS 11]
theorem seven_starts_secondKind_length_two : IsSecondKindChainOfLength 7 2 := by
  refine ⟨by norm_num, ?_, by norm_num [secondKindTerm]⟩
  intro i hi
  interval_cases i <;> norm_num [secondKindTerm]

/-- There are infinitely many first-kind Cunningham chains of every positive exact length. -/
@[category research open, AMS 11]
theorem infinitely_many_firstKind_chains (k : ℕ) (hk : 0 < k) :
    Set.Infinite {p : ℕ | IsFirstKindChainOfLength p k} := by
  sorry

/-- There are infinitely many second-kind Cunningham chains of every positive exact length. -/
@[category research open, AMS 11]
theorem infinitely_many_secondKind_chains (k : ℕ) (hk : 0 < k) :
    Set.Infinite {p : ℕ | IsSecondKindChainOfLength p k} := by
  sorry

end CunninghamChain


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
