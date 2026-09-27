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
# Erdős Problem 319

*Reference:* [erdosproblems.com/319](https://www.erdosproblems.com/319)
-/

open Filter

open scoped Topology Finset Real

namespace Erdos319

/-- What is the size of the largest $A\subseteq\{1, \dots, N\}$ such that there is a function
$\delta : A \to \{-1, 1\}$ such that
$$
  \sum_{n\in A} \frac{\delta n}{n} = 0
$$
and
$$
  \sum_{n\in A'}\frac{\delta n}{n} \neq 0
$$
for all non-empty $A'\subsetneq A$. -/
@[category research open, AMS 5]
theorem erdos_319 (N : ℕ) : IsGreatest
    { #A | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) }
    answer(sorry) := by
  sorry

-- Formalisation note: it's possible that solution to `erdos_319` needs to be
-- expressed asymptotically. To handle this we include `IsTheta`, `IsBigO`
-- and `IsLittleO` variants below. Since a solution is not known this necessitates
-- the use of an `answer(sorry)` placeholder. Trivial or sub-optimal solutions
-- will therefore exist to the asymptotic formalisations. A true solution to
-- the asymptotic variants should have a degree of optimality or non-triviality to it.
/-- Let $c(N)$ be the size of the largest $A\subseteq\{1, \dots, N\}$ such that there is a function
$\delta : A \to \{-1, 1\}$ such that
$$
  \sum_{n\in A} \frac{\delta n}{n} = 0
$$
and
$$
  \sum_{n\in A'}\frac{\delta n}{n} \neq 0
$$
for all non-empty $A'\subsetneq A$. What is $\Theta(c(N))$?-/
@[category research open, AMS 5]
theorem erdos_319.variants.isTheta (N : ℕ) (c : ℕ → ℝ)
    (h : ∀ N, IsGreatest
    { (#A : ℝ) | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) } (c N)) :
    c =Θ[atTop] (answer(sorry) : ℕ → ℝ) := by
  sorry

/-- Let $c(N)$ be the size of the largest $A\subseteq\{1, \dots, N\}$ such that there is a function
$\delta : A \to \{-1, 1\}$ such that
$$
  \sum_{n\in A} \frac{\delta n}{n} = 0
$$
and
$$
  \sum_{n\in A'}\frac{\delta n}{n} \neq 0
$$
for all non-empty $A'\subsetneq A$. Find the simplest $g(N)$ such that $c(N) = O(g(N)). -/
@[category research open, AMS 5]
theorem erdos_319.variants.isBigO (N : ℕ) (c : ℕ → ℝ)
    (h : ∀ N, IsGreatest
    { (#A : ℝ) | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) } (c N)) :
    c =O[atTop] (answer(sorry) : ℕ → ℝ) := by
  sorry

/-- Let $c(N)$ be the size of the largest $A\subseteq\{1, \dots, N\}$ such that there is a function
$\delta : A \to \{-1, 1\}$ such that
$$
  \sum_{n\in A} \frac{\delta n}{n} = 0
$$
and
$$
  \sum_{n\in A'}\frac{\delta n}{n} \neq 0
$$
for all non-empty $A'\subsetneq A$. Find the simplest $g(N)$ such that $c(N) = o(g(N)). -/
@[category research open, AMS 5]
theorem erdos_319.variants.isLittleO (N : ℕ) (c : ℕ → ℝ)
    (h : ∀ N, IsGreatest
    { (#A : ℝ) | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) } (c N)) :
    c =o[atTop] (answer(sorry) : ℕ → ℝ) := by
  sorry

/-- Adenwalla has observed that a lower bound (on the maximum size of $A$) of
$$
  |A| \geq (1 - \frac{1}{e} + o(1))N
$$
follows from the main result of Croot [Cr01].

[Cr01] Croot, III, Ernest S., _On unit fractions with denominators in short intervals_.
Acta Arith. (2001), 99-114.
-/
@[category research solved, AMS 5]
theorem erdos_319.variants.lb : ∃ (o : ℕ → ℝ), (o =o[atTop] (1 : ℕ → ℝ)) ∧
    ∀ᶠ N in atTop, (1 - 1 / rexp 1 + o N) * N ≤ sSup { (#A : ℝ) | (A) (_ : A ⊆ Finset.Icc 1 N)
      (_ : ∃ δ : ℕ → ℤˣ, ∑ n ∈ A, (δ n : ℚ) / n = 0 ∧
        ∀ A' ⊂ A, A'.Nonempty → ∑ n ∈ A', (δ n : ℚ) / n ≠ 0) } := by
  sorry

end Erdos319


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
