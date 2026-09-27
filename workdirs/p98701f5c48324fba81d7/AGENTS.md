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
# Erdős Problem 1097

*References:*
- [erdosproblems.com/1097](https://www.erdosproblems.com/1097)
- [Bo99] Bourgain, J., On the dimension of {K}akeya sets and related maximal
inequalities. Geom. Funct. Anal. (1999), 256--282
- [KaTa99] Katz, Nets Hawk and Tao, Terence, Bounds on arithmetic projections, and applications to the
{K}akeya conjecture. Math. Res. Lett. (1999), 625--630.
- [Le15] Lemm, Marius, New counterexamples for sums-differences. Proc. Amer. Math. Soc. (2015), 3863--3868.
- [GGTW25] B. Georgiev, J. Gómez-Serrano, T. Tao, and A. Wagner, Mathematical exploration and discovery at scale. arXiv:2511.02864 (2025).
-/

namespace Erdos1097

/--
Given a finite set of integers `A` (modelled as a `Finset ℤ`), the set
`CommonDifferencesThreeTermAP A` consists of all integers `d` such that there
is a non-trivial three-term arithmetic progression `a, b, c ∈ A` with
`b - a = d` and `c - b = d`.
-/
def CommonDifferencesThreeTermAP (A : Finset ℤ) : Set ℤ :=
  {d : ℤ | d ≠ 0 ∧ ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, b - a = d ∧ c - b = d}

/--
The main conjecture: for any finite set of integers $A$ with $|A| = n$, the number of distinct
common differences in three-term arithmetic progressions is $O(n^{3/2})$.

This conjecture was resolved negatively by showing that the problem is exactly equivalent to
Bourgain's sums-differences question [Bo99], which was introduced as an arithmetic path towards
the Kakeya conjecture. Under this equivalence:
- The greatest achievable exponent for this problem is equal to the smallest constant $c$
  achievable for Bourgain's sums-differences question:
  $$|A -_G B| \ll \max(|A|, |B|, |A +_G B|)^c$$
- The $O(n^{3/2})$ prediction is disproved because the lower bound has been shown to satisfy
  $c \ge 1.77898$ (due to Zheng and AlphaEvolve [GGTW25], improving on Lemm [Le15]), which is
  strictly greater than $3/2 = 1.5$.
- The best known upper bound is $c \le 11/6 \approx 1.833$ (due to Katz and Tao [KaTa99]).
- While the specific $O(n^{3/2})$ prediction is resolved negatively, the general question of
  determining the exact optimal exponent $c$ remains open.
-/
@[category research solved, AMS 11, formal_proof using formal_conjectures at
"https://github.com/mo271/formal-conjectures/blob/f13dd54b520cdf2136fdd3a04f0f9fa50e311358/FormalConjectures/ErdosProblems/1097.lean#L306"]
theorem erdos_1097 : answer(False) ↔ ∃ C > (0 : ℝ), ∀ (A : Finset ℤ),
    (CommonDifferencesThreeTermAP A).ncard ≤ C * (A.card : ℝ) ^ (3 / 2 : ℝ) := by
  sorry

/--
A weaker bound has been proven: there are always at most $n^2$ such values of $d$.
-/
@[category textbook, AMS 11]
theorem erdos_1097.variants.weaker :
    ∀ A, (CommonDifferencesThreeTermAP A).ncard ≤ A.card ^ 2 := by
  intro A
  set D := Finset.image (fun p : ℤ × ℤ => p.2 - p.1) (A ×ˢ A)
  have h_sub : CommonDifferencesThreeTermAP A ⊆ (D : Set ℤ) := by
    rintro d ⟨-, a, ha, b, hb, -, -, hab, -⟩
    exact Finset.mem_coe.mpr (Finset.mem_image.mpr
      ⟨(a, b), Finset.mem_product.mpr ⟨ha, hb⟩, hab⟩)
  calc (CommonDifferencesThreeTermAP A).ncard
      ≤ (D : Set ℤ).ncard := Set.ncard_le_ncard h_sub D.finite_toSet
    _ = D.card := Set.ncard_coe_finset _
    _ ≤ (A ×ˢ A).card := Finset.card_image_le
    _ = A.card * A.card := Finset.card_product _ _
    _ = A.card ^ 2 := (sq _).symm

/--
A trivial lower bound: for sufficiently large `n` there exist sets $A$ with $|A| = n$ that contain at least $\Omega(n)$
distinct common differences of three-term arithmetic progressions.
-/
@[category textbook, AMS 11]
theorem erdos_1097.variants.lower_bound : ∃ c > (0 : ℝ), ∀ᶠ n in Filter.atTop, ∃ (A : Finset ℤ),
    A.card = n ∧ c * (n : ℝ) ≤ (CommonDifferencesThreeTermAP A).ncard := by
  refine ⟨1/4, by norm_num, ?_⟩
  rw [Filter.eventually_atTop]
  refine ⟨4, fun n hn => ?_⟩
  refine ⟨(Finset.range n).image (fun k : ℕ => (k : ℤ)), ?_, ?_⟩
  · rw [Finset.card_image_of_injective _ Nat.cast_injective, Finset.card_range]
  set A := (Finset.range n).image (fun k : ℕ => (k : ℤ))
  set k : ℕ := (n - 1) / 2 with hk_def
  set D : Finset ℤ := (Finset.range k).image (fun i : ℕ => ((i + 1 : ℕ) : ℤ))
  have hk_ge_nat : 4 * k ≥ n := by simp [hk_def]; omega
  have hD_card : D.card = k := by
    rw [Finset.card_image_of_injective _, Finset.card_range]
    intro a b h
    simp only at h
    have : (a + 1 : ℤ) = (b + 1 : ℤ) := by exact_mod_cast h
    omega
  have h_finite : (CommonDifferen

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
