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
# Ben Green's Open Problem 31

Write $F(N)$ for the largest Sidon subset of $[N]$.
Improve, at least for infinitely many $N$, the bounds $N^{1/2} + O(1) \le F(N) \le N^{1/2} + N^{1/4} + O(1)$.

Note: the upper bound was improved to $N^{1/2} + 0.98183 N^{1/4} + O(1)$ in [CHO25].

Related to Erdős Problem 30.

*References:*
- [Gr24] [Ben Green's Open Problem 31](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.7 Problem 31)
- [Gr01] Green, Ben. "The number of squares and $ B_h [g] $ sets."
  Acta Arithmetica 100.4 (2001): 365-390.
- [BFR23] Balogh, József, Zoltán Füredi, and Souktik Roy. "An upper bound on the size of Sidon sets."
  The American Mathematical Monthly 130.5 (2023): 437-445.
- [CHO25] Carter, Daniel, Zach Hunter, and Kevin O’Bryant. "On the diameter of finite Sidon sets."
  Acta Mathematica Hungarica 175.1 (2025): 108-126.
- [ET41] Erdos, Paul, and Pál Turán. "On a problem of Sidon in additive number theory, and on some
  related problems." J. London Math. Soc 16.4 (1941): 212-215.
- [Li69] Lindström, Bernt. “A remark on B4-Sequences.” Journal of Combinatorial Theory,
  Series A 7 (1969): 276-277.
- [CLZ01] Cohen, G.D., Litsyn, S., & Zémor, G. (2001). Binary B2-Sequences : A New Upper Bound.
  J. Comb. Theory A, 94, 152-155.
-/

namespace Green31

open Filter

/-- Let $F(N)$ be the largest Sidon subset of $[N]$. -/
noncomputable def F (N : ℕ) : ℝ := Finset.maxSidonSubsetCard (Finset.Icc 1 N)

/-- Can we improve the lower bound $N^{1/2} + O(1)$, at least for infinitely many $N$? -/
@[category research open, AMS 5 11]
theorem green_31.lower :
    let ans := (answer(sorry) : ℕ → ℝ)
    Filter.Tendsto (fun N ↦ ans N - Real.sqrt (N : ℝ)) atTop atTop ∧ -- Break the O(1) barrier
    ∃ᶠ N in atTop, ans N ≤ F N := by
  sorry

/-- Can we improve the lower bound $N^{1/2} + O(1)$, for all sufficiently large $N$? -/
@[category research open, AMS 5 11]
theorem green_31.variants.lower_eventually :
    let ans := (answer(sorry) : ℕ → ℝ)
    Filter.Tendsto (fun N ↦ ans N - Real.sqrt (N : ℝ)) atTop atTop ∧ -- Break the O(1) barrier
    ∀ᶠ N in atTop, ans N ≤ F N := by
  sorry

/--
Can we improve the upper bound $N^{1/2} + 0.98183 N^{1/4} + O(1)$ [CHO25], at least for infinitely
many $N$?
-/
@[category research open, AMS 5 11]
theorem green_31.upper :
    let ans := (answer(sorry) : ℕ → ℝ)
    (∃ᶠ N in atTop, F N ≤ ans N) ∧
    ∃ c < (0.98183 : ℝ), ∃ C : ℝ, ∀ᶠ N in atTop, ans N - Real.sqrt (N : ℝ) ≤ c * (N : ℝ) ^ (4⁻¹ : ℝ) + C := by
  sorry

/--
Can we improve the upper bound $N^{1/2} + 0.98183 N^{1/4} + O(1)$ [CHO25], for all sufficiently
large $N$?
-/
@[category research open, AMS 5 11]
theorem green_31.variants.upper_eventually :
    let ans := (answer(sorry) : ℕ → ℝ)
    (∀ᶠ N in atTop, F N ≤ ans N) ∧
    ∃ c < (0.98183 : ℝ), ∃ C : ℝ, ∀ᶠ N in atTop, ans N - Real.sqrt (N : ℝ) ≤ c * (N : ℝ) ^ (4⁻¹ : ℝ) + C := by
  sorry

/-- [Li69] proved $F(n) \le n^{1/2} + n^{1/4} + O(1)$. -/
@[category research solved, AMS 5 11]
theorem green_31.variants.upper_li69 :
    ∃ C : ℝ, ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (N : ℝ) ^ (4⁻¹ : ℝ) + C := by
  sorry

/--
[BFR23] obtained a small improvement, getting an upper bound of $F(N) \le N^{1/2} + 0.998 N^{1/4}$
for large $N$.
-/
@[category research solved, AMS 5 11]
theorem green_31.variants.upper_bfr23 :
    ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (0.998 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ) := by
  sorry

/-- The upper bound was further improved to $N^{1/2} + 0.98183 N^{1/4} + O(1)$ [CHO25]. -/
@[category research solved, AMS 5 11]
theorem green_31.variants.upper_cho25 :
    ∃ C : ℝ, ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (0.98183 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ) + C := by
  sorry

/--
It is not known whether or not there exists a Sidon subset of $\mathbb{Z}/p\mathbb{Z}$ of size
$(1 + o(1))\sqrt{p}$, for all $p$ [Gr24].
-/
@[category research open, AMS 5 11]
theorem green_31.variants.zmod_p : answer(sorry) ↔
    ∃ S : (n : ℕ) → Finset (ZMod n),
    ∃ o : ℕ → ℝ,
      (o =o[atTop] fun _ : ℕ ↦ (1 : ℝ)) ∧
      (∀ p, p.Prime → IsSidon (S p : Set (ZMod p))) ∧
      (∀ p, p.Prime → ((S p).card : ℝ) = (1 + o p) * Real.sqrt (p : ℝ)) := by
  sorry

/--
It is not known whether, if $G$ is an abelian group of size $n$, there always exists a Sidon subset
of $G$ of size $0.01\sqrt{n}$ [Gr24].
-/
@[category research open, AMS 5 11]
theorem green_31.variants.abelian : answer(sorry

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
