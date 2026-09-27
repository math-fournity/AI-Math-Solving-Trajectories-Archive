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
# Erdős Problem 1023

*References:*
- [erdosproblems.com/1023](https://www.erdosproblems.com/1023)
- [Er71, p.105] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
  Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
-/

open Filter

open scoped Asymptotics

namespace Erdos1023

/--
`F n` is the maximal size of a family of subsets of $\{1,\ldots,n\}$ such that no set in this
family is the union of other members of the family.
-/
noncomputable def F (n : ℕ) : ℕ :=
  sSup {m | ∃ S ⊆ (Finset.Icc 1 n).powerset, S.SubfamilyUnionFree ∧ S.card = m}

/--
Let $F(n)$ be the maximal size of a family of subsets of $\{1,\ldots,n\}$ such that no set in
this family is the union of other members of the family. Is it true that there is a constant
$c>0$ such that
$$F(n)\sim c \frac{2^n}{n^{1/2}}?$$

Hunter observes in the comments that this follows from the solution to [447], which implies
$F(n)\sim \binom{n}{n/2}$.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1023.lean"]
theorem erdos_1023 : answer(True) ↔
    ∃ c : ℝ, 0 < c ∧
      ((fun n : ℕ => (F n : ℝ)) ~[atTop]
        (fun n : ℕ => c * 2 ^ n / (n : ℝ) ^ (1 / 2 : ℝ))) := by
  sorry

/--
Erdős and Kleitman proved in unpublished work that
$$F(n)\asymp \frac{2^n}{n^{1/2}}.$$
([Er71] has an exponent of $3/2$, but this is presumably a typo.)
-/
@[category research solved, AMS 5]
theorem erdos_1023.variants.erdos_kleitman :
    (fun n : ℕ => (F n : ℝ)) =Θ[atTop] (fun n : ℕ => (2 : ℝ) ^ n / (n : ℝ) ^ (1 / 2 : ℝ)) := by
  sorry

/--
Hunter observes in the comments that this follows from the solution to [447], which implies
$F(n)\sim \binom{n}{n/2}$.
-/
@[category research solved, AMS 5]
theorem erdos_1023.variants.hunter :
    (fun n : ℕ => (F n : ℝ)) ~[atTop] (fun n : ℕ => (n.choose (n / 2) : ℝ)) := by
  sorry

end Erdos1023


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
