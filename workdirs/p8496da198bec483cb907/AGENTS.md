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
# Ben Green's Open Problem 72

More commonly known as the **no-three-in-line problem**.

Given $N > 2$ and more than $2 * N$ points on an $N \times N$-grid,
are there $3$ of the points on a common line?

*References:*
- [Ben Green's Open Problem 72](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.72)
- [Wikipedia](https://en.wikipedia.org/wiki/No-three-in-line_problem)
- [GK2025] Grebennikov, A. Kwan, M. No $(k + 1)$-in-line problem for large constant $k$.
  https://arxiv.org/abs/2510.17743
-/

namespace Green72

/-- We say a subset of $[N]^2$ is allowed for some $k$ if it contains no $k$ points
which lie on a common line. -/
structure AllowedSet (k : ℕ) (N : ℕ) (s : Finset (ℕ × ℕ)) : Prop where
  is_bounded : ∀ i ∈ s, i.1 < N ∧ i.2 < N
  not_collinear : ∀ ⦃t : Finset (ℕ × ℕ)⦄, t ⊆ s → t.card = k →
    ¬ Collinear ℝ ({r | ∃ i ∈ t, r = ((↑i.1 : ℝ), (↑i.2 : ℝ))} : Set (ℝ × ℝ))

/-- The maximal size of an allowed set -/
noncomputable def AllowedSetSize (k : ℕ) (N : ℕ) : ℕ :=
  sSup {r | ∃ s, r = s.card ∧ AllowedSet k N s}

/-- By the pigeon hole principle, the size of a subset of an $N \times N$ grid such that no $k$
points lie on a line is bounded by $\leq (k - 1) * N$. -/
@[category textbook, AMS 5 52]
theorem allowedSetSize_le {k : ℕ} {N : ℕ} :
    AllowedSetSize k N ≤ (k - 1) * N := by
  refine csSup_le' ?_
  rintro r ⟨s, rfl, hs⟩
  -- Every column of the grid meets an allowed set in at most $k - 1$ points, since $k$ points
  -- sharing a first coordinate lie on a common vertical line.
  have key : ∀ x ∈ Finset.range N, (s.filter fun i => i.1 = x).card ≤ k - 1 := by
    intro x _
    by_contra hc
    obtain ⟨t, hts, htc⟩ := Finset.exists_subset_card_eq (n := k)
      (s := s.filter fun i => i.1 = x) (by omega)
    refine hs.not_collinear (hts.trans (Finset.filter_subset _ _)) htc ?_
    rw [collinear_iff_exists_forall_eq_smul_vadd]
    refine ⟨((x : ℝ), 0), (0, 1), ?_⟩
    rintro p ⟨i, hi, rfl⟩
    exact ⟨i.2, by simp [(Finset.mem_filter.mp (hts hi)).2]⟩
  calc s.card
      = ∑ x ∈ Finset.range N, (s.filter fun i => i.1 = x).card :=
        Finset.card_eq_sum_card_fiberwise fun i hi => Finset.mem_range.mpr (hs.is_bounded i hi).1
    _ ≤ ∑ _x ∈ Finset.range N, (k - 1) := Finset.sum_le_sum key
    _ = (k - 1) * N := by simp [mul_comm]

/-- The proposition that the allowed-set size for $k$ and $N$ is $(k - 1) * N$. -/
def NoKInLineFor (k : ℕ) (N : ℕ) : Prop :=
  AllowedSetSize k N = (k - 1) * N

/-- The **no-k-in-line problem**:
For $N \geq k$ and $k > 2$, the AllowedSetSize is $(k - 1) N$, i. e. on an $N \times N$ subset,
there is a set of $(k - 1) N$ points for which no $k$ lie on a line (and not such a set of bigger size).
-/
@[category research open, AMS 5 52]
theorem NoKInLine {k : ℕ} {N : ℕ} (hk : 2 < k) (h : k ≤ N) : NoKInLineFor k N := by
  sorry

/-- **Green's Open Problem 72 / No-three-in-line problem**:
The no-k-in-line conjecture holds for $k = 3$. -/
@[category research open, AMS 5 52]
theorem green_72 {N : ℕ} (hN : 3 ≤ N) : NoKInLineFor 3 N := by
  sorry

alias no_three_in_line := green_72

/-- Does the no-three-in-line problem hold when $N$ is big enough? -/
@[category research open, AMS 5 52]
theorem green_72.variants.eventually : answer(sorry) ↔ ∀ᶠ N in Filter.atTop, NoKInLineFor 3 N := by
  sorry

/-- For $N \leq 60$, this has been verified with computers. -/
@[category research solved, AMS 5 52]
theorem no_three_in_line_le {N : ℕ} (hN : 3 ≤ N) (hN' : N ≤ 60) :
    NoKInLineFor 3 N := by
  sorry

/-- In [GK2025] Grebennikov and Kwan prove the no-k-in-line conjecture for $k > 10 ^ 37$
and $N \geq k$. -/
@[category research solved, AMS 5 52]
theorem no_k_in_line_big {k : ℕ} (N : ℕ) (h : 10 ^ 37 < k) (hN : k ≤ N) :
    NoKInLineFor k N := by
  sorry

-- TODO: Add lower bound for no-three-in-line

end Green72


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
