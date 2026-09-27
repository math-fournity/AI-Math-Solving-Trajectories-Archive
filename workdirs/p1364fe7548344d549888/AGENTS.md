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
# Erdős Problem 1193

*References:*
- [erdosproblems.com/1193](https://www.erdosproblems.com/1193)
- [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
  (1980), 89-115.
-/

open AdditiveCombinatorics Set

namespace Erdos1193

/--
Let $A\subset \mathbb{N}$ and let $g(n)$ be a non-decreasing function of $n$ which is always $>0$.

Is the lower density of
$$\{ n : 1_A\ast 1_A(n)=g(n)\}$$
always $0$?

The answer is trivially no to both questions: indeed if $A=\mathbb{N}$ (assuming $0\in\mathbb{N}$)
then $1_A\ast 1_A(n)=n+1$ for all $n$. Presumably Erdős had some additional restrictions on either
$g$ or $A$ in mind, but these are not recorded in [Er80].
-/
@[category research solved, AMS 5 11]
theorem erdos_1193.parts.i : answer(False) ↔
    ∀ (A : Set ℕ) (g : ℕ → ℕ), Monotone g → (∀ n, 0 < g n) →
      {n : ℕ | sumRep A n = g n}.lowerDensity = 0 := by
  sorry

/--
Let $A\subset \mathbb{N}$ and let $g(n)$ be a non-decreasing function of $n$ which is always $>0$.

Is the upper density of
$$\{ n : 1_A\ast 1_A(n)=g(n)\}$$
always $<c$ for some constant $c<1$?

The answer is trivially no to both questions: indeed if $A=\mathbb{N}$ (assuming $0\in\mathbb{N}$)
then $1_A\ast 1_A(n)=n+1$ for all $n$. Presumably Erdős had some additional restrictions on either
$g$ or $A$ in mind, but these are not recorded in [Er80].
-/
@[category research solved, AMS 5 11]
theorem erdos_1193.parts.ii : answer(False) ↔
    ∃ c < (1 : ℝ), ∀ (A : Set ℕ) (g : ℕ → ℕ), Monotone g → (∀ n, 0 < g n) →
      {n : ℕ | sumRep A n = g n}.upperDensity < c := by
  sorry

/--
Indeed if $A=\mathbb{N}$ (assuming $0\in\mathbb{N}$) then $1_A\ast 1_A(n)=n+1$ for all $n$.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1193.lean"]
theorem erdos_1193.variants.sumRep_univ (n : ℕ) : sumRep (Set.univ : Set ℕ) n = n + 1 := by
  sorry

/--
Erdős writes the upper density can be positive, but he believes it is bounded away from $1$.
-/
@[category research solved, AMS 5 11]
theorem erdos_1193.variants.upper_density_pos :
    ∃ (A : Set ℕ) (g : ℕ → ℕ), Monotone g ∧ (∀ n, 0 < g n) ∧
      0 < {n : ℕ | sumRep A n = g n}.upperDensity := by
  sorry

end Erdos1193


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
