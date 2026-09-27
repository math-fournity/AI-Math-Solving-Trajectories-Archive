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
# Bloch and Landau constants

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_analysis))
- [CP96] Chen, H., Gauthier, P. M. "On Bloch's constant." Journal d'Analyse Mathématique 69 (1996),
  275–291.
- [AG37] Ahlfors, L. V., Grunsky, H. "Über die Blochsche Konstante." Mathematische Zeitschrift 42
  (1937), 671–673.
- [Ya95] Yanagihara, H. "On the locally univalent Bloch constant." Journal d'Analyse Mathématique
  65 (1995), 1–17.
- [Ra43] Rademacher, H. "On the Bloch-Landau Constant."" American Journal of Mathematics 65 (1943),
  387–390.
- [OptimizationConstants](https://teorth.github.io/optimizationproblems/constants/57c.html)
- [Skin2009] Skinner, Brian. The univalent Bloch constant problem. Complex Variables and Elliptic
  Equations 54 (2009), no. 10, 951–955.
- [MathWorld](https://mathworld.wolfram.com/BlochConstant.html)
- [Bhowmik–Sen](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/improved-bloch-and-landau-constants-for-meromorphic-functions/FD465D1F2CEF7E8C62AFF16C3E89B7B4)
-/
open scoped Topology ENNReal
open Metric Set Filter
namespace Bloch

/-- The **Bloch radius** $B_f$ of a function $f$ is the supremum of radii of univalent disks in the
image of the unit disk under $f$. Takes values in `ℝ≥0∞` so that functions whose image contains
arbitrarily large univalent disks correctly get radius `⊤` rather than `0`. -/
noncomputable def blochRadius (f : ℂ → ℂ) : ℝ≥0∞ :=
  sSup (ENNReal.ofReal '' {r : ℝ | ∃ S ⊆ ball (0 : ℂ) 1, ∃ x, ball x r ⊆ f '' S ∧ InjOn f S})

@[category API, AMS 30]
lemma zero_le_blochRadius (f : ℂ → ℂ) : 0 ≤ blochRadius f := zero_le _

@[category API, AMS 54]
lemma dis_add_radius_le_of_ball_subset_ball {X 𝕜 : Type*} [RCLike 𝕜] [NormedAddCommGroup X]
    [NormedSpace 𝕜 X] [Nontrivial X] {x y : X} {r d : ℝ} (hpos : 0 < r) (hsub : ball x r ⊆ ball y d) :
    dist x y + r ≤ d := by
  have : Tendsto (fun s => dist x y + s) (𝓝[<] r) (𝓝 (dist x y + r)) :=
      (tendsto_nhds_of_tendsto_nhdsWithin tendsto_id).const_add _
  refine le_of_tendsto this ?_
  filter_upwards [Ioo_mem_nhdsLT hpos] with t ⟨hl, hr⟩
  by_cases! hxy : x = y
  · obtain ⟨v, hv⟩ := exists_ne (0 : X)
    simp_all only [dist_self, zero_add]
    let u := (‖v‖⁻¹ : 𝕜) • v
    have : ‖u‖ = 1 := by apply norm_smul_inv_norm; grind
    calc
    _ = ‖y + (t : 𝕜) • u - y‖ := by simp_all [norm_smul, abs_of_nonneg hl.le]
    _ ≤ d := by
      refine (mem_ball_iff_norm.1 (hsub (mem_ball_iff_norm.2 ?_))).le
      simp_all [norm_smul, abs_of_nonneg hl.le]
  · let u := (‖x - y‖⁻¹ : 𝕜) • (x - y)
    have : ‖u‖ = 1 := by apply norm_smul_inv_norm; grind
    calc
    _ = ‖x - y‖ + t := by simp [NormedAddCommGroup.dist_eq]
    _ = ‖x + (t : 𝕜) • u - y‖ := by
      simp [u, add_sub_right_comm, ← smul_assoc]
      nth_rw 2 [← one_smul 𝕜 (x - y)]
      rw [← add_smul, norm_smul]
      norm_cast
      rw [abs_of_nonneg (by positivity), add_mul, one_mul, mul_assoc, inv_mul_cancel₀ (by aesop),
        mul_one]
    _ ≤ d := by
      refine (mem_ball_iff_norm.1 (hsub (mem_ball_iff_norm.2 ?_))).le
      simp_all [norm_smul, abs_of_nonneg hl.le]

@[category API, AMS 54]
lemma radius_le_of_ball_subset_ball {X 𝕜 : Type*} [RCLike 𝕜] [NormedAddCommGroup X]
    [NormedSpace 𝕜 X] [Nontrivial X] {x y : X} {r d : ℝ} (hpos : 0 < r)
    (hsub : ball x r ⊆ ball y d) : r ≤ d :=
  trans (by simp) (dis_add_radius_le_of_ball_subset_ball (𝕜 := 𝕜) hpos hsub)

@[category API, AMS 30]
lemma blochRadius_id_eq_one : blochRadius id = 1 := by
  apply le_antisymm
  · -- blochRadius id ≤ 1: every valid radius r satisfies r ≤ 1
    apply sSup_le
    rintro _ ⟨r, ⟨S, hS, x, hball, -⟩, rfl⟩
    simp only [image_id] at hball
    by_cases hpos : 0 < r
    · exact (ENNReal.ofReal_le_ofReal
        (radius_le_of_ball_subset_ball (𝕜 := ℂ) hpos (hball.trans hS))).trans
        (by simp [ENNReal.ofReal_one])
    · exact (ENNReal.ofReal_of_nonpos (by linarith)).le.trans (zero_le _)
  · -- 1 ≤ blochRadius id: ball 0 1 ⊆ id '' ball 0 1
    rw [show (1 : ℝ≥0∞) = ENNReal.ofReal 1 from by simp]
    exact le_sSup ⟨1, ⟨ball (0 : ℂ) 1, Subset.rfl, 0, by simp⟩, rfl⟩

/-- The **Landau radius** $L_f$ of a function $f$ is the supremum of radii of disks contained in
the image of the unit disk under $f$. Takes values in `ℝ≥0∞` so that functions with unbounded
image correctly get radius `⊤`. -/
noncomputable def landauRadius (f : ℂ →

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
