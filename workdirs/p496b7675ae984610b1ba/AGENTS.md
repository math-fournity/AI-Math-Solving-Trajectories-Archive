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
# Erdős Problem 959

*Reference:* [erdosproblems.com/959](https://www.erdosproblems.com/959)
-/

namespace Erdos959

open EuclideanGeometry Filter
open scoped Topology

noncomputable section

/-- The unordered index pairs, represented uniquely by the orientation `i < j`. -/
def indexPairs (n : ℕ) : Finset (Fin n × Fin n) :=
  (Finset.univ ×ˢ Finset.univ).filter fun ij => ij.1 < ij.2

/-- The finite set of distinct distances determined by a configuration. -/
def distanceValues {n : ℕ} (P : Fin n → ℝ²) : Finset ℝ :=
  (indexPairs n).image fun ij => dist (P ij.1) (P ij.2)

/-- $f(d)$: the number of unordered pairs in $P$ determining distance $d$. -/
def frequency {n : ℕ} (P : Fin n → ℝ²) (d : ℝ) : ℕ :=
  ((indexPairs n).filter fun ij => dist (P ij.1) (P ij.2) = d).card

/-- For a fixed distance $d$, the largest multiplicity among all *other*
represented distances (`Finset.sup` returns $0$ when there is no other value). -/
def runnerUpFrequency {n : ℕ} (P : Fin n → ℝ²) (d : ℝ) : ℕ :=
  ((distanceValues P).erase d).sup (frequency P)

/-- $f(d_1) - f(d_2)$: the gap between the largest and second-largest distance
multiplicities. The supremum over $d$ handles both a unique winner and a tie:
non-winners contribute $0$ by truncated subtraction, and tied winners also
contribute $0$. -/
def multiplicityGap {n : ℕ} (P : Fin n → ℝ²) : ℕ :=
  (distanceValues P).sup fun d => frequency P d - runnerUpFrequency P d

/-- A configuration represents a set of size $n$ (injective) and has at least
two distinct distances, so that $d_2$ exists. -/
def Admissible {n : ℕ} (P : Fin n → ℝ²) : Prop :=
  Function.Injective P ∧ 2 ≤ (distanceValues P).card

/-- A natural number occurs as the top-two multiplicity gap of some admissible
$n$-point configuration. -/
def AttainableGap (n g : ℕ) : Prop :=
  ∃ P : Fin n → ℝ², Admissible P ∧ multiplicityGap P = g

/-- The extremal quantity of the problem, $\max_{|A| = n} (f(d_1) - f(d_2))$. There
are `Nat.choose n 2` unordered pairs, so this is a valid finite search interval. -/
def extremalGap (n : ℕ) : ℕ := by
  classical
  exact Nat.findGreatest (AttainableGap n) (Nat.choose n 2)

/--
Let $A\subseteq \mathbb{R}^2$ be a set of size $n$ and let $\{d_1,\ldots,d_k\}$ be
the set of distinct distances determined by $A$. Let $f(d)$ be the number of times
the distance $d$ is determined, ordered so that
$f(d_1)\geq f(d_2)\geq \cdots \geq f(d_k)$. Estimate
$$\max (f(d_1)-f(d_2)),$$
where the maximum is taken over all $A$ of size $n$ (this is `extremalGap n`).

The asymptotic order of `extremalGap` is not known; a natural formalization of
"estimate" asks whether it has a well-defined polynomial growth exponent.
-/
@[category research open, AMS 52]
theorem erdos_959 : answer(sorry) ↔
    ∃ γ : ℝ, Tendsto (fun n : ℕ => Real.log (extremalGap n) / Real.log n) atTop (𝓝 γ) := by
  sorry

/--
A superlinear lower bound: there is a $c>0$ with
$$\text{extremalGap}(n)\geq n^{1 + c/\log\log n}$$
for all large $n$, so $\max (f(d_1)-f(d_2))$ grows faster than any linear function
of $n$. Determining the exact order remains open, which is `erdos_959`.
-/
@[category research solved, AMS 52, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-959/Research/FinalLowerBound.lean"]
theorem erdos_959.lower_bound :
    ∃ c : ℝ, 0 < c ∧ ∃ N : ℕ, ∀ n ≥ N,
      (n : ℝ) ^ (1 + c / Real.log (Real.log n)) ≤ extremalGap n := by
  sorry

end

end Erdos959


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
