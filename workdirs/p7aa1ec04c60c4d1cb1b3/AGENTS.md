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
# Erdős Problem 1119

*References:*
- [erdosproblems.com/1119](https://www.erdosproblems.com/1119)
- [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.
- [Er64g] Erdős, P., An interpolation problem associated with the continuum hypothesis.
  Michigan Math. J. (1964), 9--10.
- [KuSh17] Kumar, Ashutosh and Shelah, Saharon, On a question about families of entire
  functions. Fund. Math. (2017), 279--288.
- [ScWe24] Schilhan, Jonathan and Weinert, Thilo, Wetzel families and the continuum.
  J. Lond. Math. Soc. (2) (2024), Paper No. e12918, 27.
-/

open Cardinal Order
open scoped Cardinal

namespace Erdos1119

/--
Let $\mathfrak{m}$ be an infinite cardinal with $\aleph_0 < \mathfrak{m} < \mathfrak{c} =
2^{\aleph_0}$. Let $\{f_\alpha\}$ be a family of entire functions such that, for every
$z_0 \in \mathbb{C}$, there are at most $\mathfrak{m}$ distinct values of $f_\alpha(z_0)$.
Must $\{f_\alpha\}$ have cardinality at most $\mathfrak{m}$?

This is Problem 2.46 in [Ha74], where it is attributed to Erdős. The question is
**independent of ZFC**, so the headline statement carries `answer(sorry)`: it is neither
provable nor refutable from the usual axioms of set theory.

The answer is yes if $\mathfrak{m}^+ < \mathfrak{c}$ (see
`erdos_1119.variants.easy_case`), so the question reduces to the case
$\mathfrak{m}^+ = \mathfrak{c}$, where it is undecidable: Kumar and Shelah [KuSh17]
produced a model of $\mathfrak{c} = \aleph_2$ in which the answer is yes (with
$\mathfrak{m} = \aleph_1$), while Schilhan and Weinert [ScWe24] produced a different
model of $\mathfrak{c} = \aleph_2$ in which the answer is no.
-/
@[category research solved, AMS 3 30]
theorem erdos_1119 : answer(sorry) ↔
    ∀ (m : Cardinal.{0}), ℵ₀ < m → m < 𝔠 →
    ∀ F : Set (ℂ → ℂ), (∀ f ∈ F, Differentiable ℂ f) →
      (∀ z₀ : ℂ, #{y : ℂ | ∃ f ∈ F, f z₀ = y} ≤ m) →
      #F ≤ m := by
  sorry

/-
**Independence of Erdős Problem 1119** (prose record; consistency statements about
models of ZFC are not directly formalizable inside Lean's fixed model):

* Kumar–Shelah [KuSh17] constructed a model of ZFC with $\mathfrak{c} = \aleph_2$ in
  which every family of entire functions taking at most $\aleph_1$ values at each point
  has cardinality at most $\aleph_1$ — so the answer to the problem is **yes** in that
  model (with $\mathfrak{m} = \aleph_1$).
* Schilhan–Weinert [ScWe24] constructed a different model of ZFC with
  $\mathfrak{c} = \aleph_2$ containing a family of $\aleph_2$ entire functions taking at
  most $\aleph_1$ values at each point — so the answer is **no** in that model.

Together with the easy case $\mathfrak{m}^+ < \mathfrak{c}$ below, these show the
problem is independent of ZFC, with the only undecidable case being
$\mathfrak{m}^+ = \mathfrak{c}$.
-/

/--
The 'easy' case of Erdős Problem 1119: if moreover $\mathfrak{m}^+ < \mathfrak{c}$, then
any family of entire functions taking at most $\mathfrak{m}$ distinct values at each
point has cardinality at most $\mathfrak{m}$. In [Ha74] it is written that this is
'easy to see'.
-/
@[category research solved, AMS 3 30]
theorem erdos_1119.variants.easy_case (m : Cardinal.{0}) (hm : ℵ₀ < m)
    (hsucc : succ m < 𝔠) (F : Set (ℂ → ℂ))
    (hF : ∀ f ∈ F, Differentiable ℂ f)
    (hval : ∀ z₀ : ℂ, #{y : ℂ | ∃ f ∈ F, f z₀ = y} ≤ m) :
    #F ≤ m := by
  sorry

/--
Erdős's theorem [Er64g], answering a question of Wetzel: if $\mathfrak{c} > \aleph_1$,
then every family of entire functions taking only countably many distinct values at each
point $z_0 \in \mathbb{C}$ is itself countable.
-/
@[category research solved, AMS 3 30]
theorem erdos_1119.variants.erdos_wetzel (h : ℵ_ 1 < 𝔠) (F : Set (ℂ → ℂ))
    (hF : ∀ f ∈ F, Differentiable ℂ f)
    (hval : ∀ z₀ : ℂ, {y : ℂ | ∃ f ∈ F, f z₀ = y}.Countable) :
    F.Countable := by
  sorry

/--
Erdős [Er64g] also showed that the previous statement fails under the continuum
hypothesis: if $\mathfrak{c} = \aleph_1$, then there is an **uncountable** family of
entire functions taking only countably many distinct values at each point
$z_0 \in \mathbb{C}$.
-/
@[category research solved, AMS 3 30]
theorem erdos_1119.variants.erdos_wetzel_ch (h : 𝔠 = ℵ_ 1) :
    ∃ F : Set (ℂ → ℂ), (∀ f ∈ F, Differentiable ℂ f) ∧
      (∀ z₀ : ℂ, {y : ℂ | ∃ f ∈ F, f z₀ = y}.Countable) ∧
      ¬ F.Countable := by
  sorry

/--
Sanity check: the empty family of e

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
