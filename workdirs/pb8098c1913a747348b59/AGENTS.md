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
# Erdős Problem 650

*References:*
- [erdosproblems.com/650](https://www.erdosproblems.com/650)
- [Er78] Erdős, Paul, *Problems and results in combinatorial analysis and combinatorial number
  theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
  Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
- [Er86c] Erdős, P., *Some problems on number theory*. (1986), 53-67.
- [Er95c] Erdős, Paul, *Some problems in number theory*. Octogon Math. Mag. (1995), 3-5.
- [ErSu59] Erdős, Pál and Surányi, János, *Bemerkungen zu einer Aufgabe eines mathematischen
  Wettbewerbs*. Mat. Lapok (1959), 39-48.
- [VLT26] W. Van Doorn, Y. Li, and Q. Tang, *Optimal bounds for an Erdős problem on matching
  integers to distinct multiples*. arXiv:2603.28636 (2026).
-/

namespace Erdos650

/--
`f m` is the largest `r` such that whenever `A ⊆ {1, …, N}` has `m` elements, every interval
in `[1, ∞)` of length `2 * N` contains `r` distinct integers `b 0, …, b (r - 1)`, each `b i`
being divisible by some `a i ∈ A`, where `a 0, …, a (r - 1)` are distinct. -/
noncomputable def f (m : ℕ) : ℕ :=
  sSup {r : ℕ | ∀ N : ℕ, ∀ A ⊆ Finset.Icc 1 N, A.card = m → ∀ x : ℝ, 1 ≤ x →
    ∃ a b : Fin r → ℕ, (Function.Injective a) ∧ (Function.Injective b) ∧
      (∀ i, a i ∈ A) ∧ (∀ i, (b i : ℝ) ∈ Set.Ioo x (x + 2 * (N : ℝ))) ∧ (∀ i, a i ∣ b i)}

/--
Let $f(m)$ be such that if $A\subseteq \{1,\ldots,N\}$ has $\lvert A\rvert=m$ then every interval
in $[1,\infty)$ of length $2N$ contains $\geq f(m)$ many distinct integers $b_1,\ldots,b_r$ where
each $b_i$ is divisible by some $a_i\in A$, where $a_1,\ldots,a_r$ are distinct.

Estimate $f(m)$.

GPT 5.4 Pro (prompted by He, Li, and Tang) proved $f(m)\leq \lceil 2\sqrt{m}\rceil$. A
corresponding lower bound was given by GPT 5.4 Pro and Aristotle; it is now known (see the paper
of van Doorn, Li, and Tang [VLT26]) that
$$f(m) = \min(m, \lceil 2\sqrt{m}\rceil)$$
for all $m$.

This was formalized in Lean by van Doorn using Aristotle.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at
"https://github.com/Woett/Lean-files/blob/main/ErdosProblem650.lean"]
theorem erdos_650.parts.i (m : ℕ) : f m = min m ⌈2 * Real.sqrt m⌉₊ := by
  sorry

/--
Let $f(m)$ be such that if $A\subseteq \{1,\ldots,N\}$ has $\lvert A\rvert=m$ then every interval
in $[1,\infty)$ of length $2N$ contains $\geq f(m)$ many distinct integers $b_1,\ldots,b_r$ where
each $b_i$ is divisible by some $a_i\in A$, where $a_1,\ldots,a_r$ are distinct.

In particular is it true that $f(m)\leq \sqrt{m}$?

GPT 5.4 Pro (prompted by He, Li, and Tang) proved $f(m)\leq \lceil 2\sqrt{m}\rceil$. A
corresponding lower bound was given by GPT 5.4 Pro and Aristotle; it is now known (see the paper
of van Doorn, Li, and Tang [VLT26]) that
$$f(m) = \min(m, \lceil 2\sqrt{m}\rceil)$$
for all $m$.

This was formalized in Lean by van Doorn using Aristotle.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at
"https://github.com/Woett/Lean-files/blob/main/ErdosProblem650.lean"]
theorem erdos_650.parts.ii : answer(False) ↔ ∀ m : ℕ, (f m : ℝ) ≤ Real.sqrt m := by
  sorry

/--
Erdős and Surányi [ErSu59] proved that $f(m)\geq\sqrt{m}$.
-/
@[category research solved, AMS 5 11]
theorem erdos_650.variants.erdos_suranyi (m : ℕ) : Real.sqrt m ≤ (f m : ℝ) := by
  sorry

/--
Erdős and Selfridge proved (see [Er78] and [Er86c]) that $f(m^2)\leq 2m$, which implies
$f(m)\leq 2\lceil \sqrt{m}\rceil$ for all $m$.
-/
@[category research solved, AMS 5 11]
theorem erdos_650.variants.erdos_selfridge (m : ℕ) : f (m ^ 2) ≤ 2 * m := by
  sorry

end Erdos650


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
