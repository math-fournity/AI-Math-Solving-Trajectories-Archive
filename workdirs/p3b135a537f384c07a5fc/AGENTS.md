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
# Erdős Problem 1000

*References:*
- [erdosproblems.com/1000](https://www.erdosproblems.com/1000)
- [Ca50b] Cassels, J. W. S., *Some metrical theorems in Diophantine approximation. I*. Proc.
  Cambridge Philos. Soc. (1950), 209-218.
- [Er64b] Erdős, P., *Problems and results on diophantine approximations*. Compositio Math. (1964),
  52-65.
- [Ha] Haight, J. A., *Metric Diophantine approximation and related topics*. PhD thesis.
-/

open Filter Topology

namespace Erdos1000

/--
Given an infinite sequence of integers $A = \{n_1 < n_2 < \cdots\}$, `phiSeq n k` is
$\phi_A(k)$: the number of $1\leq m\leq n_k$ such that
$$
\frac{n_k}{(m,n_k)}\neq n_j
$$
for all $1\leq j<k$.
-/
def phiSeq (n : ℕ → ℕ) (k : ℕ) : ℕ :=
  ((Finset.Icc 1 (n k)).filter fun m => ∀ j < k, n k / Nat.gcd m (n k) ≠ n j).card

/--
The average $\frac{1}{N}\sum_{k\leq N}\frac{\phi_A(k)}{n_k}$.
-/
noncomputable def phiAvg (n : ℕ → ℕ) (N : ℕ) : ℝ :=
  (∑ k ∈ Finset.range N, (phiSeq n k : ℝ) / (n k : ℝ)) / (N : ℝ)

/--
Let $A=\{n_1<n_2<\cdots\}$ be an infinite sequence of integers, and let $\phi_A(k)$ count the
number of $1\leq m\leq n_k$ such that the fraction $\frac{m}{n_k}$ does not have denominator $n_j$
for $j<k$ when written in lowest form; equivalently,
$$
\frac{n_k}{(m,n_k)}\neq n_j
$$
for all $1\leq j<k$.

Is there a sequence $A$ such that
$$
\lim_{N\to \infty}\frac{1}{N}\sum_{k\leq N}\frac{\phi_A(k)}{n_k}=0?
$$

This was solved by Haight [Ha] who proved that such a sequence does exist (contrary to Erdős'
expectations).
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1000.lean"]
theorem erdos_1000 : answer(True) ↔
    ∃ n : ℕ → ℕ, StrictMono n ∧ 0 < n 0 ∧
      Tendsto (phiAvg n) atTop (𝓝 0) := by
  sorry

/--
It is trivial that $\phi_A(k)\geq \phi(n_k)$, where $\phi$ is the Euler totient function.
-/
@[category research solved, AMS 11]
theorem erdos_1000.variants.totient_le (n : ℕ → ℕ) (hn : StrictMono n) (k : ℕ) :
    (n k).totient ≤ phiSeq n k := by
  sorry

/--
The study of $\phi_A$ was introduced by Cassels [Ca50b], who proved that there exist sequences
such that
$$
\liminf_{N\to \infty}\frac{1}{N}\sum_{k\leq N}\frac{\phi_A(k)}{n_k}=0.
$$
-/
@[category research solved, AMS 11]
theorem erdos_1000.variants.liminf_eq_zero :
    ∃ n : ℕ → ℕ, StrictMono n ∧ 0 < n 0 ∧
      atTop.liminf (phiAvg n) = 0 := by
  sorry

/--
Erdős [Er64b] proved that the limit of $\frac{\phi_A(k)}{n_k}$ as $k\to \infty$ cannot be $0$.
-/
@[category research solved, AMS 11]
theorem erdos_1000.variants.not_tendsto_zero (n : ℕ → ℕ) (hn : StrictMono n) (hn0 : 0 < n 0) :
    ¬ Tendsto (fun k : ℕ => (phiSeq n k : ℝ) / (n k : ℝ)) atTop (𝓝 0) := by
  sorry

/--
In fact he proved that if $\liminf \frac{\phi_A(k)}{n_k}=0$ then
$\limsup \frac{\phi_A(k)}{n_k}=1$.
-/
@[category research solved, AMS 11]
theorem erdos_1000.variants.limsup_eq_one (n : ℕ → ℕ) (hn : StrictMono n) (hn0 : 0 < n 0)
    (h : atTop.liminf (fun k : ℕ => (phiSeq n k : ℝ) / (n k : ℝ)) = 0) :
    atTop.limsup (fun k : ℕ => (phiSeq n k : ℝ) / (n k : ℝ)) = 1 := by
  sorry

end Erdos1000


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
