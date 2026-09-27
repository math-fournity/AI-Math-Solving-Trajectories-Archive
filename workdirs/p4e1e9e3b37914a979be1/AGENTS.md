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
# Erdős Problem 538

*Reference:* [erdosproblems.com/538](https://www.erdosproblems.com/538)
-/

open Filter
open scoped Topology

namespace Erdos538

open scoped Classical in
/-- The representations `m = p * a` with `p` prime and `a ∈ A`. -/
def representations (A : Finset ℕ) (m : ℕ) : Finset (ℕ × ℕ) :=
  (Finset.range (m + 1) ×ˢ A).filter (fun pa => Nat.Prime pa.1 ∧ m = pa.1 * pa.2)

/-- `A ⊆ {1, …, N}` and every `m` has at most `r` representations `m = p a`. -/
def Admissible (r N : ℕ) (A : Finset ℕ) : Prop :=
  (∀ a ∈ A, 1 ≤ a ∧ a ≤ N) ∧ ∀ m : ℕ, (representations A m).card ≤ r

/-- The reciprocal sum `∑_{n ∈ A} 1/n` of the problem. -/
def reciprocalMass (A : Finset ℕ) : ℚ := ∑ a ∈ A, (1 : ℚ) / a

/-- The largest reciprocal sum `∑_{n ∈ A} 1/n` over admissible `A ⊆ {1, …, N}`. -/
noncomputable def maxMass (r N : ℕ) : ℝ :=
  sSup ((fun A => (reciprocalMass A : ℝ)) '' {A : Finset ℕ | Admissible r N A})

/--
Let $r\geq 2$ and suppose that $A\subseteq\{1,\ldots,N\}$ is such that, for any
$m$, there are at most $r$ solutions to $m=pa$ where $p$ is prime and $a\in A$.
Give the best possible upper bound for $\sum_{n\in A}\frac{1}{n}$.

The order is known — `∑ 1/n = Θ_r(log N / loglog N)` (see `erdos_538.matching_order`) —
but the sharp constant is not. This asks whether `maxMass r N` has a well-defined
leading constant `c_r` in `c_r · log N / loglog N`.
-/
@[category research open, AMS 11]
theorem erdos_538 : answer(sorry) ↔ ∀ r : ℕ, 2 ≤ r →
    ∃ c : ℝ, 0 < c ∧
      Tendsto (fun N : ℕ => maxMass r N * Real.log (Real.log N) / Real.log N) atTop (𝓝 c) := by
  sorry

/--
The reciprocal sum has matching order `Θ_r(log N / loglog N)`: an explicit
upper bound for every admissible `A`, together with a witnessing construction
achieving the same order. This pins the order (up to the one iterated-logarithm
factor) but not the sharp constant asked for in `erdos_538`.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-538/Research/FinalMatchingOrder.lean"]
theorem erdos_538.matching_order (r N : ℕ) (hr : 2 ≤ r) (hN : 2 ≤ N) :
    (∀ A : Finset ℕ, Admissible r N A →
      Real.log (Real.log (N + 1)) * (reciprocalMass A : ℝ) ≤
        2 * r * (1 + Real.log (N * N))) ∧
    (∃ A : Finset ℕ, Admissible r N A ∧
      Real.log (N + 1) ≤
        4 + (8192 * (Nat.log 2 (Nat.log 2 N) + 1) : ℝ) * (reciprocalMass A : ℝ)) := by
  sorry

end Erdos538


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
