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
# Erdős Problem 796

*Reference:* [erdosproblems.com/796](https://www.erdosproblems.com/796)
-/

namespace Erdos796

open Filter
open scoped Topology

/-- The number of unordered representations `m = a₁ * a₂` by two distinct
elements `a₁ < a₂` of `A`. -/
def repCount (A : Finset ℕ) (m : ℕ) : ℕ :=
  ((A ×ˢ A).filter fun a => a.1 < a.2 ∧ a.1 * a.2 = m).card

/-- `A` has at most `k - 1` representations of every `m` (fewer than `k`). -/
def HasRepBound (k : ℕ) (A : Finset ℕ) : Prop := ∀ m : ℕ, repCount A m < k

open scoped Classical in
/-- `g k n = g_k(n)` is the largest size of a subset `A ⊆ {1, …, n}` in which
every `m` has fewer than `k` representations `m = a₁ a₂` with `a₁ < a₂ ∈ A`. -/
noncomputable def g (k n : ℕ) : ℕ :=
  ((Finset.Icc 1 n).powerset.filter (HasRepBound k)).sup Finset.card

/-- The proposed second-order rescaling of `g_3(n)`:
`(g_3(n) - (log log n / log n) · n) / (n / log n)`, whose limit is the constant
`c` in the problem. -/
noncomputable def normalizedError (n : ℕ) : ℝ :=
  ((g 3 n : ℝ) - (n : ℝ) * Real.log (Real.log n) / Real.log n) / ((n : ℝ) / Real.log n)

/--
Let $k\geq 2$ and let $g_k(n)$ be the largest possible size of
$A\subseteq \{1,\ldots,n\}$ such that every $m$ has $<k$ solutions to
$m=a_1a_2$ with $a_1<a_2\in A$. Is it true that
$$g_3(n)=\frac{\log\log n}{\log n}n+(c+o(1))\frac{n}{\log n}$$
for some constant $c$?

The answer is yes: the rescaled error `normalizedError` converges.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-796/Research/CanonicalTail.lean"]
theorem erdos_796 :
    answer(True) ↔ ∃ c : ℝ, Tendsto normalizedError atTop (𝓝 c) := by
  sorry

end Erdos796


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
