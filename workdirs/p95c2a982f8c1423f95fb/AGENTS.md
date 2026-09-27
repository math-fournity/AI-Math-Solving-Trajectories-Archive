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
# Erdős Problem 357

*Reference:* [erdosproblems.com/357](https://www.erdosproblems.com/357)
-/

namespace Erdos357

open Filter Asymptotics

def HasDistinctSums {ι α : Type*} [Preorder ι] [AddCommMonoid α] (a : ι → α) : Prop :=
  {J : Finset ι | (J : Set ι).OrdConnected}.InjOn (fun J ↦ ∑ x ∈ J, a x)

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. -/
noncomputable def f (n : ℕ) : ℕ :=
  sSup {k : ℕ | ∃ a : Fin k → ℤ, Set.range a ⊆ Set.Icc 1 n ∧ StrictMono a ∧ HasDistinctSums a}

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. Is $f(n)=o(n)$? -/
@[category research open, AMS 11]
theorem erdos_357.parts.i : (fun n ↦ (f n : ℝ)) =o[atTop] (fun n ↦ (n : ℝ)) := by
  sorry

/-
Formalisation note: the next 5 formalisations are an attempt at capturing the question "how does
$f(n)$ grow?". In addition to trivial solutions (e.g. setting `answer(sorry) = 0` in some of these),
it is possible that some of these admit easy solutions that shouldn't count as genuine solutions.
As usual in this repo, solving this problem is not simply providing a term to replace `answer(sorry)`
together with a proof of the theorem, but providing a *mathematically interesting* answer.
Note also that there might be other reasonable (and non equivalent) formal statements that capture this
question.
Similar remarks hold for the `variants.monotone` formalisations later in this file.
-/

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $g = O(f)$ ? -/
@[category research open, AMS 11]
theorem erdos_357.parts.ii.bigO_version :
    (answer(sorry) : ℕ → ℝ) =O[atTop] (fun n ↦ (f n : ℝ)) := by
  sorry

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $f = O(g)$ ? -/
@[category research open, AMS 11]
theorem erdos_357.parts.ii.bigO_version_symm :
    (fun n ↦ (f n : ℝ)) =O[atTop] (answer(sorry) : ℕ → ℝ) := by
  sorry

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $f = \Theta(g)$ ? -/
@[category research open, AMS 11]
theorem erdos_357.parts.ii.bigTheta_version :
    (fun n ↦ (f n : ℝ)) =Θ[atTop] (answer(sorry) : ℕ → ℝ) := by
  sorry

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $g = o(f)$ ? -/
@[category research open, AMS 11]
theorem erdos_357.parts.ii.littleO_version :
    (answer(sorry) : ℕ → ℝ) =o[atTop] (fun n ↦ (f n : ℝ)) := by
  sorry

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $f = o(g)$ ? -/
@[category research open, AMS 11]
theorem erdos_357.parts.ii.littleO_version_symm :
    (fun n ↦ (f n : ℝ)) =o[atTop] (answer(sorry) : ℕ → ℝ) := by
  sorry

/-- Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
It is known that $f(n) \geq (2+o(1))\sqrt{n}$.
Source: See comment by Desmond Weisenberg here: https://www.erdosproblems.com/forum/thread/357.
-/
@[category research solved, AMS 11]
theorem erdos_357.variants.weisenberg : ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧
    ∀ᶠ n in atTop, (2 + o n) * √n ≤ f n := by
  sorry

/-- Suppose $A$ is an infinite set such that all finite sums of consecutive terms of $A$ are distinct.
Then $A$ has lower density 0. -/
@[category research solved, AMS 11]
theorem erdos_357.variants.inf

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
