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
# Erdős Problem 90: The unit distance problem

*Reference:* [erdosproblems.com/90](https://www.erdosproblems.com/90)

The conjecture asks whether every set of $n$ points in $\mathbb{R}^2$ determines at most
$n^{1 + O(1/\log\log n)}$ unit distances. It was **disproved** in May 2026: an internal model at
OpenAI produced a construction beating the conjectured bound, with the proof digested and
human-verified in two arXiv papers:

* W. Sawin, [*An explicit lower bound for the unit distance problem*](https://arxiv.org/abs/2605.20579)
  (2026), giving $u(n) \ge n^{1.014114}/C$ for infinitely many $n$;
* N. Alon, T. F. Bloom, W. T. Gowers, D. Litt, W. Sawin, A. Shankar, J. Tsimerman, V. Wang and
  M. Matchett Wood, [*Remarks on the disproof of the unit distance conjecture*](https://arxiv.org/abs/2605.20695)
  (2026), giving the qualitative form $u(n) \ge n^{1+\varepsilon}$ for some $\varepsilon > 0$.

This file records the main statement (`erdos_90`), the two constructive disproof variants, the
logical implications between them, and the load-bearing reductions of Sawin's proof
(`sawin_lattice_reduction` and `sawin_totally_real_tower`) as further benchmark challenges.
-/

open Filter EuclideanGeometry NumberField
open scoped EuclideanGeometry

namespace Erdos90
open Finset

/--
The set of all possible numbers of unit distances for a configuration of $n$ points.
-/
noncomputable def unitDistanceCounts (n : ℕ) : Set ℕ :=
  {unitDistancePairsCount points | (points : Finset ℝ²) (_ : points.card = n)}

/--
This lemma confirms that the set of possible unit distance counts is bounded above, which
ensures that taking the supremum (`sSup`) is a well-defined operation. The trivial upper bound is
the total number of pairs of points, $\binom{n}{2}$.
-/
@[category test, AMS 52]
theorem unitDistanceCounts_BddAbove (n : ℕ) : BddAbove <| unitDistanceCounts n := by
  unfold Erdos90.unitDistanceCounts
  unfold unitDistancePairsCount
  use n.choose 2
  rintro _ ⟨points, rfl, rfl⟩
  rw [points.card.choose_two_right]
  gcongr
  refine (card_filter_le _ _).trans_eq ?_
  rw [offDiag_card, Nat.mul_sub_left_distrib, mul_one]


/--
The **maximum number of unit distances** determined by any set of $n$ points in the plane.
This function is often denoted as $u(n)$ in combinatorics.
-/
noncomputable def maxUnitDistances (n : ℕ) : ℕ :=
  sSup (unitDistanceCounts n)


/--
Does every set of $n$ distinct points in $\mathbb{R}^2$ contain at most
$n^{1+O(\frac{1}{\log\log n})}$ many pairs which are distance $1$ apart?

This was
[disproved](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf)
by an internal model at OpenAI, which constructed (for infinitely many $n$) a set $P$ of $n$ points
in $\mathbb{R}^2$ such that the number of unit distance pairs in $P$ is at least $n^{1+c}$, where
$c > 0$ is an absolute constant.
-/
@[category research solved, AMS 52]
theorem erdos_90 : answer(False) ↔ ∃ (O : ℕ → ℝ) (hO : O =O[atTop] (fun n => 1 / (n : ℝ).log.log)),
    (fun n => (maxUnitDistances n : ℝ)) =ᶠ[atTop] fun (n : ℕ) => (n : ℝ) ^ (1 + O n) := by
  sorry

/--
**Constructive form of the disproof.** There is an absolute constant $c > 0$ such that
infinitely many $n$ admit a configuration realising at least $n^{1+c}$ unit distances.

This is the qualitative content of Theorem 1.1 of Alon–Bloom–Gowers–Litt–Sawin–Shankar–
Tsimerman–Wang–Matchett Wood, [*Remarks on the disproof of the unit distance conjecture*](https://arxiv.org/abs/2605.20695)
(2026). An explicit bound $c \ge 0.014114$ is given by Sawin, [*An explicit lower bound for the
unit distance problem*](https://arxiv.org/abs/2605.20579) (2026); see
`erdos_90.variants.sawin_explicit` below.
-/
@[category research solved, AMS 52]
theorem erdos_90.variants.polynomial_lower_bound :
    ∃ c > (0 : ℝ),
      {n : ℕ | (n : ℝ) ^ (1 + c) ≤ (maxUnitDistances n : ℝ)}.Infinite := by
  sorry

/--
**Sawin's explicit exponent.** The constructive disproof can be realised with $c \ge 0.014114$
(absorbing the implicit constant $C$ of Sawin's Theorem 1 into a slightly smaller exponent for
all large enough $n$). Reference: Theorem 1 of Sawin, [arXiv:2605.20579](https://arxiv.org/abs/2605.20579)
(2026).
-/
@[category research solved, AMS 52]
theorem erdos_90.variants.sawin_explicit :
    {n : ℕ | (n : ℝ) ^ (1.014114 : ℝ) ≤ (maxUnitDistances n : ℝ)}.Infinite := by
  sorry

/-- Sawin's

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
