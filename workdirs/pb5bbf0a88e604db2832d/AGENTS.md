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
# Erdős Problem 501

*References:*
- [erdosproblems.com/501](https://www.erdosproblems.com/501)
- [Er61] Erdős, Paul, Some unsolved problems. Magyar Tud. Akad. Mat. Kutató Int. Közl. 6
  (1961), 221-254.
- [ErHa71] Erdős, Paul and Hajnal, András, Unsolved problems in set theory. Axiomatic Set
  Theory, Proc. Sympos. Pure Math. XIII Part I (1971), 17-48.
- [ErHa60] Erdős, Paul and Hajnal, András. On some combinatorial problems involving
  complete graphs. Acta Math. Acad. Sci. Hungar. (1960), 395-424.
- [Gl62] Gladysz, S. Some topological properties of independent sets. Colloq. Math. (1962).
- [He72] Hechler, S. H. A dozen small uncountable cardinals. TOPO 72, Lecture Notes
  in Math. (1972), 207-218.
- [NPS87] Newelski, L., Pawlikowski, J., and Seredyński, F. Infinite independent sets in
  the closed case. Acta Math. Acad. Sci. Hungar. (1987).
-/

open Set MeasureTheory
open scoped Cardinal ENNReal

namespace Erdos501

/- ## Setup

For every `x : ℝ` we are given a set `A x ⊆ ℝ`. We say that `X ⊆ ℝ` is an
**independent set** for the family `A` if `x ∉ A y` for all distinct `x y ∈ X`.
This is exactly `X.Pairwise (fun x y => x ∉ A y)`; we inline this rather than
introducing a custom predicate so that all `Set.Pairwise` lemmas apply.

The problem concerns outer measure `< 1` on ℝ. For a set `s : Set ℝ` we use
`(MeasureTheory.volume.toOuterMeasure) s`, which equals the Lebesgue outer measure
of `s` (defined for all sets, whether measurable or not). The condition `< 1` is
stated in `ℝ≥0∞` (extended non-negative reals). -/

/- ## Main open problem -/

/--
For every $x \in \mathbb{R}$ let $A_x \subset \mathbb{R}$ be a bounded set with outer measure
$< 1$. Must there exist an infinite independent set, that is, some infinite $X \subseteq
\mathbb{R}$ such that $x \notin A_y$ for all $x \neq y \in X$?

If the sets $A_x$ are closed and have measure $< 1$, then must there exist an independent set
of size $3$?

Known results: Erdős–Hajnal [ErHa60] proved the existence of arbitrarily large finite
independent sets. Hechler [He72] showed the answer is **no** assuming the continuum
hypothesis. -/
@[category research open, AMS 5 28]
theorem erdos_501 : answer(sorry) ↔
    ∀ (A : ℝ → Set ℝ),
      (∀ x, Bornology.IsBounded (A x)) →
      (∀ x, volume.toOuterMeasure (A x) < 1) →
      ∃ X : Set ℝ, X.Infinite ∧ X.Pairwise (fun x y => x ∉ A y) := by
  sorry

/- ## Variants and partial results -/

/--
**Erdős–Hajnal (1960): arbitrarily large finite independent sets exist.**

For every `n : ℕ` and every family `A : ℝ → Set ℝ` of bounded sets with Lebesgue
outer measure `< 1`, there exists a finite independent set of size at least `n`.

This was proved by Erdős and Hajnal [ErHa60]. -/
@[category research solved, AMS 5 28]
theorem erdos_501.variants.erdosHajnal_finite : answer(True) ↔
    ∀ (n : ℕ) (A : ℝ → Set ℝ),
      (∀ x, Bornology.IsBounded (A x)) →
      (∀ x, volume.toOuterMeasure (A x) < 1) →
      ∃ X : Finset ℝ, n ≤ X.card ∧ (X : Set ℝ).Pairwise (fun x y => x ∉ A y) := by
  sorry

/--
**Hechler (1972) [He72]: the answer to the main question is NO, assuming the continuum
hypothesis.**

Assuming CH (`ℵ₁ = 𝔠`), there exists a family `A : ℝ → Set ℝ` of bounded sets with
Lebesgue outer measure `< 1` for which no infinite independent set exists. -/
@[category research solved, AMS 5 28]
theorem erdos_501.variants.hechler_CH : answer(True) ↔
    (ℵ₁ = 𝔠) →
    ∃ (A : ℝ → Set ℝ),
      (∀ x, Bornology.IsBounded (A x)) ∧
      (∀ x, volume.toOuterMeasure (A x) < 1) ∧
      ¬ ∃ X : Set ℝ, X.Infinite ∧ X.Pairwise (fun x y => x ∉ A y) := by
  sorry

/--
**Closed sets case: existence of an independent set of size 3.**

If the sets `A x` are closed with Lebesgue measure `< 1`, must there exist an
independent set of size 3?

This is implied by the stronger theorem of Newelski–Pawlikowski–Seredyński [NPS87] below;
Gladysz [Gl62] earlier proved the existence of an independent set of size 2. -/
@[category research solved, AMS 5 28]
theorem erdos_501.variants.closed_size3 : answer(True) ↔
    ∀ (A : ℝ → Set ℝ),
      (∀ x, IsClosed (A x)) →
      (∀ x, volume (A x) < 1) →
      ∃ X : Set ℝ, 3 ≤ X.ncard ∧ X.Pairwise (fun x y => x ∉ A y) := by
  simp only [true_iff]
  sorry

/--
**Newelski–Pawlikowski–Seredyński (1987) [NPS87]: infinite independent set in the closed case.**

If all the sets `A x` are closed with Lebesgue measure `< 1`, then th

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
