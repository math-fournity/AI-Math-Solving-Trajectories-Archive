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
# Erdős Problem 867

*References:*
- [erdosproblems.com/867](https://www.erdosproblems.com/867)
- [CoPh96] Coppersmith, Don and Phillips, Steven, *On a question of Erdős on subsequence sums*.
  SIAM J. Discrete Math. (1996), 173-177.
- [Fr93] Freud, R., *Adding numbers - on a problem of P. Erdős*. James Cook Mathematical
  Notes (1993), 6199-6202.
-/

open Filter

namespace Erdos867

/-- A finite set of naturals $A=\{a_1<\cdots<a_t\}$ is *consecutive-sum-free* if it has no
solutions to $a_i+a_{i+1}+\cdots+a_j\in A$ with $i<j$; equivalently, whenever an interval
$[m,n]$ contains at least two elements of $A$, the sum of the elements of $A$ lying in
$[m,n]$ is not itself an element of $A$. -/
def ConsecutiveSumFree (A : Finset ℕ) : Prop :=
  ∀ m n : ℕ, 2 ≤ (Finset.Icc m n ∩ A).card → (∑ a ∈ Finset.Icc m n ∩ A, a) ∉ A

/--
Is it true that if $A=\{a_1<\cdots <a_t\}\subseteq \{1,\ldots,N\}$ has no solutions to
$$a_i+a_{i+1}+\cdots+a_j\in A$$
then
$$\lvert A\rvert \leq \frac{N}{2}+O(1)?$$

In fact this problem is false. Freud [Fr93] constructed a sequence with density $\geq 19/36$.
The current best bounds are due to Coppersmith and Phillips [CoPh96], who prove that the
maximal size of such an $A$ satisfies
$$\frac{13}{24}N -O(1)\leq \lvert A\rvert \leq \left(\frac{2}{3}-\frac{1}{512}\right)N+\log N.$$
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos867.lean"]
theorem erdos_867 : answer(False) ↔
    ∃ C : ℝ, ∀ N : ℕ, ∀ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A →
      (A.card : ℝ) ≤ (N : ℝ) / 2 + C := by
  sorry

/--
Taking $A=(N/2,N]\cap \mathbb{N}$ shows $\lvert A\rvert \geq N/2-O(1)$ is possible.
-/
@[category research solved, AMS 5 11]
theorem erdos_867.variants.lower_bound :
    ∃ C : ℝ, ∀ N : ℕ, ∃ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A ∧
      ((N : ℝ) / 2 - C ≤ (A.card : ℝ)) := by
  sorry

/--
Adenwalla has observed that
$$\lvert A\rvert \leq (\tfrac{2}{3}+o(1))N.$$
-/
@[category research solved, AMS 5 11]
theorem erdos_867.variants.adenwalla (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop, ∀ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A →
      (A.card : ℝ) ≤ (2 / 3 + ε) * (N : ℝ) := by
  sorry

/--
Freud [Fr93] constructed a sequence with density $\geq 19/36$.
-/
@[category research solved, AMS 5 11]
theorem erdos_867.variants.freud :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N : ℕ in atTop, ∃ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A ∧
      (((19 / 36 : ℝ) - ε) * (N : ℝ) ≤ (A.card : ℝ)) := by
  sorry

/--
The current best bounds are due to Coppersmith and Phillips [CoPh96], who prove that the
maximal size of such an $A$ satisfies
$$\frac{13}{24}N -O(1)\leq \lvert A\rvert.$$
-/
@[category research solved, AMS 5 11]
theorem erdos_867.variants.coppersmith_phillips_lower_bound :
    ∃ C : ℝ, ∀ N : ℕ, ∃ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A ∧
      ((13 / 24 : ℝ) * (N : ℝ) - C ≤ (A.card : ℝ)) := by
  sorry

/--
The current best bounds are due to Coppersmith and Phillips [CoPh96], who prove that the
maximal size of such an $A$ satisfies
$$\lvert A\rvert \leq \left(\frac{2}{3}-\frac{1}{512}\right)N+\log N.$$
-/
@[category research solved, AMS 5 11]
theorem erdos_867.variants.coppersmith_phillips_upper_bound :
    ∀ᶠ N : ℕ in atTop, ∀ A ⊆ Finset.Icc 1 N, ConsecutiveSumFree A →
      (A.card : ℝ) ≤ (2 / 3 - 1 / 512) * (N : ℝ) + Real.log (N : ℝ) := by
  sorry

end Erdos867


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
