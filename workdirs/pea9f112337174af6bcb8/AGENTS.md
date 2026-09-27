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
# Erdős Problem 987

*References:*
- [erdosproblems.com/987](https://www.erdosproblems.com/987)
- [APSSV26b] B. Alexeev, M. Putterman, M. Sawhney, M. Sellke, and G. Valiant,
  [Short proofs in combinatorics, probability, and number theory II](https://arxiv.org/abs/2604.06609).
  arXiv:2604.06609 (2026).
- [Cl67] Clunie, J., On a problem of Erdős. J. London Math. Soc. (1967), 133--136.
- [Er64b] Erdős, P., Problems and results on diophantine approximations. Compositio Math. (1964),
  52-65.
- [Er65b] Erdős, P., Some remarks on number theory. Israel J. Math. (the actual reference
  cited by Clunie 1967 as [2]; the erdosproblems.com bibliography points to a different
  Erdős 1965 paper, "Some recent advances and current problems in number theory" (Lectures
  on Modern Mathematics III, 1965, 196-244), which does not appear to contain the
  exponential-sum log-bound proof).
- [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.
- [Li69] Lindström, B., An inequality for $B_2$-sequences. J. Combinatorial Theory (1969), 211-212.
-/

open Filter Finset Asymptotics
open scoped ExponentialSum

namespace Erdos987

/-
Here we use 0-indexing for generality and convenience, while in the original problem
formulation 1-indexing was used. This change does not affect the meaning of the problem.
In the description of the problem below we remain faithful to the original one.
-/

/--
For an infinite sequence $x_1, x_2, \ldots \in (0, 1)$, define
$$A_k = \limsup_{n \to \infty} \left\lvert \sum_{j \le n} e(k x_j) \right\rvert,$$
where $e(x) = e^{2\pi i x}$.
-/
noncomputable def A (x : ℕ → ℝ) (k : ℕ) : EReal :=
  atTop.limsup fun n : ℕ => (‖∑ j ∈ range n, e (k * x j)‖ : EReal)

/- ## Question 1 -/

/-- Question 1:

Is it true that $\limsup_{k \to \infty} A_k = \infty$?

Erdős [Er64b] remarks it is "easy to see" that $\limsup_k \sup_n |\sum_{j \le n} e(k x_j)| = \infty$.
Erdős [Er65b] later found a "very easy" proof that $A_k \gg \log k$ for infinitely many $k$.
Clunie [Cl67] proved that $A_k \gg k^{1/2}$ for infinitely many $k$, which implies the answer is
yes (Tao independently found a proof). This is Problem 7.21 in [Ha74]. -/
@[category research solved, AMS 11 40 42, formal_proof using lean4 at
"https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean"]
theorem erdos_987.parts.i :
    answer(True) ↔ ∀ (x : ℕ → ℝ) (_ : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1),
      atTop.limsup (fun k : ℕ => A x k) = ⊤ := by
  sorry

/-- Erdős [Er64b] remarks it is "easy to see" that for every infinite sequence
$x_1, x_2, \ldots \in (0, 1)$,
$$\limsup_{k \to \infty} \sup_n \left\lvert \sum_{j \le n} e(k x_j) \right\rvert = \infty.$$ -/
@[category research solved, AMS 11 40 42, formal_proof using lean4 at
"https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean"]
theorem erdos_987.variants.sup_limsup_infty
    (x : ℕ → ℝ) (hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) :
    atTop.limsup (fun k : ℕ =>
      ⨆ n : ℕ, ((‖∑ j ∈ range n, e ((k : ℝ) * x j)‖ : ℝ) : EReal)) = ⊤ := by
  sorry

/-- Erdős [Er65b] proved that, for every infinite sequence $x_1, x_2, \ldots \in (0, 1)$,
$A_k \gg \log k$ for infinitely many $k$. -/
@[category research solved, AMS 11 40 42, formal_proof using lean4 at
"https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean"]
theorem erdos_987.variants.log_lower_bound
    (x : ℕ → ℝ) (_hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) :
    ∃ c > 0, ∃ᶠ k : ℕ in atTop, ((c * Real.log k : ℝ) : EReal) ≤ A x k := by
  sorry

/-- Clunie [Cl67] proved that, for every infinite sequence $x_1, x_2, \ldots \in (0, 1)$,
$A_k \gg k^{1/2}$ for infinitely many $k$. (Tao independently found a proof.) -/
@[category research solved, AMS 11 40 42, formal_proof using lean4 at
"https://github.com/Marti2203/formal-conjectures/blob/19c63d48acce3099c242b059518c49bf8dc0eab8/FormalConjectures/ErdosProblems/987.lean"]
theorem erdos_987.variants.sqrt_lower_bound
    (x : ℕ → ℝ) (hx : ∀ j : ℕ, x j ∈ Set.Ioo (0 : ℝ) 1) :
    ∃ c > 0, ∃ᶠ k : ℕ in atTop, ((c * Real.sqrt k : ℝ) : EReal) ≤ A x k := by
  sorry

/-- **Linear upper bound (weakened).** A first weakened version of Clunie's `A_k ≤ k`: there
exists a seq

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
