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
# Weak tiling problems

Problems 4.1, 4.2, and 4.3 from [arxiv/2506.23631](https://arxiv.org/abs/2506.23631).

*Reference:*
* [Geometric implications of weak tiling](https://arxiv.org/abs/2506.23631)

See also `FormalConjectures.Wikipedia.Fuglede` for Fuglede's spectral set conjecture, which
motivates the study of weak tilings.
-/

open MeasureTheory Set ENNReal NNReal

namespace WeakTiling

/-- A set $A \subseteq \mathbb{R}$ is a **union of $n$ intervals** if it can be written as
    $A = \bigcup_{i=1}^{n} (a_i, b_i)$ with $a_1 < b_1 < a_2 < b_2 < \dots < a_n < b_n$,
    i.e., as a disjoint union of $n$ nondegenerate open intervals in strict order with strict
    separation. This matches the convention of [the paper](https://arxiv.org/abs/2506.23631)
    (see e.g. Theorem 3.4 there). -/
def IsUnionOfNIntervals (n : ℕ) (A : Set ℝ) : Prop :=
  ∃ (a b : Fin n → ℝ),
    (∀ i : Fin n, a i < b i) ∧
    (∀ i j : Fin n, i < j → b i < a j) ∧
    A = ⋃ i, Set.Ioo (a i) (b i)

/-- A set $A \subseteq \mathbb{R}$ is a **finite union of intervals** if it is a union of $n$
    intervals for some $n$. -/
def IsFiniteUnionOfIntervals (A : Set ℝ) : Prop :=
  ∃ n, IsUnionOfNIntervals n A

/-- A positive, locally finite Borel measure $\nu$ on $\mathbb{R}$ is a **weak tiling measure**
    for a bounded measurable set $\Omega \subset \mathbb{R}$ if the convolution
    $1_\Omega \ast \nu = 1_{\Omega^c}$ holds almost everywhere, i.e.,
    $\int 1_\Omega(x - t) \, d\nu(t) = 1_{\Omega^c}(x)$ for a.e. $x \in \mathbb{R}$.

    This is Definition 1.1 from [the paper](https://arxiv.org/abs/2506.23631). -/
def IsWeakTilingMeasure (Ω : Set ℝ) (ν : Measure ℝ) : Prop :=
  Bornology.IsBounded Ω ∧
  MeasurableSet Ω ∧
  IsLocallyFiniteMeasure ν ∧
  ∀ᵐ x ∂(volume : Measure ℝ),
    ∫ t, Ω.indicator (fun _ => (1 : ℝ)) (x - t) ∂ν =
    Ωᶜ.indicator (fun _ => (1 : ℝ)) x

/-- A **proper tiling** of $\Omega^c$ by translates of $\Omega$ is specified by a set of
    translation parameters $T \subseteq \mathbb{R}$ such that the sum of Dirac masses on $T$
    is a weak tiling measure for $\Omega$. -/
def IsProperTiling (Ω T : Set ℝ) : Prop :=
  IsWeakTilingMeasure Ω (Measure.sum (fun t : T => Measure.dirac (t : ℝ)))

/-- A set $\Lambda \subseteq \mathbb{R}$ has **bounded density** if the number of points of
    $\Lambda$ in any unit open interval is uniformly bounded:
    $\sup_{x \in \mathbb{R}} \#(\Lambda \cap (x, x + 1)) < \infty$. -/
def HasBoundedDensity (Λ : Set ℝ) : Prop :=
  ∃ C : ℕ, ∀ x : ℝ, (Λ ∩ Set.Ioo x (x + 1)).Finite ∧ (Λ ∩ Set.Ioo x (x + 1)).ncard ≤ C

/-- **Problem 4.1.** Let $\Omega \subset \mathbb{R}$ be a finite union of intervals and $\nu$
    a weak tiling measure for $\Omega$. Must $\mathrm{supp}(\nu)$ have bounded density? -/
@[category research open, AMS 42 46]
theorem problem_4_1 :
    answer(sorry) ↔ ∀ (Ω : Set ℝ) (_ : IsFiniteUnionOfIntervals Ω)
      (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν), HasBoundedDensity ν.support := by
  sorry

/-- **Problem 4.2.** Let $\Omega \subset \mathbb{R}$ be a finite union of three or more
    intervals. If $\Omega$ weakly tiles its complement, must it also tile its complement
    properly? -/
@[category research open, AMS 42 46]
theorem problem_4_2 :
    answer(sorry) ↔ ∀ (n : ℕ) (_ : 3 ≤ n) (Ω : Set ℝ)
      (_ : IsUnionOfNIntervals n Ω) (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν),
      ∃ T : Set ℝ, IsProperTiling Ω T := by
  sorry

/-- **Problem 4.3.** Let $\Omega \subset \mathbb{R}$ be a finite union of intervals and $\nu$
    a weak tiling measure for $\Omega$. Must $\nu$ be expressible as a convex combination of
    proper tiling measures? -/
@[category research open, AMS 42 46]
theorem problem_4_3 :
    answer(sorry) ↔ ∀ (Ω : Set ℝ) (_ : IsFiniteUnionOfIntervals Ω)
      (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν),
      ∃ (T : ℕ → Set ℝ) (c : ℕ → ℝ≥0), (∀ i, IsProperTiling Ω (T i)) ∧ ∑' i : ℕ, c i = 1 ∧
      ν = Measure.sum
        (fun i => (c i : ℝ≥0∞) • Measure.sum (fun t : T i => Measure.dirac (t : ℝ))) := by
  sorry

end WeakTiling


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
