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
# Erdős Problem 1128

*Reference:* [erdosproblems.com/1128](https://www.erdosproblems.com/1128)
-/

open Cardinal Set Ordinal Order

namespace Erdos1128

/-- A subset $A_1 \times B_1 \times C_1$ of $A \times B \times C$ is **monochromatic**
under a 2-colouring $f : A \to B \to C \to \operatorname{Fin} 2$ if $f$ is constant on
$A_1 \times B_1 \times C_1$. -/
def IsMonochromaticBox {A B C : Type*} (f : A → B → C → Fin 2)
    (A₁ : Set A) (B₁ : Set B) (C₁ : Set C) : Prop :=
  ∃ c : Fin 2, ∀ a ∈ A₁, ∀ b ∈ B₁, ∀ c' ∈ C₁, f a b c' = c

/-
Auxiliary lemmas for the Prikry–Mills construction.
These establish key countability and boundedness properties of ω₁.
-/

/-- The set of countable ordinals, expressed using Mathlib's `ω_ 1`. -/
private abbrev Omega1 := {o : Ordinal.{0} // o < ω_ 1}

/-- The set of ordinals strictly below any $\gamma < \omega_1$ is countable. -/
@[category API, AMS 5]
private lemma countable_Iio_of_lt_omega1 {γ : Ordinal} (hγ : γ < ω_ 1) :
    (Set.Iio γ).Countable := by
  rwa [countable_iff_lt_aleph_one, mk_Iio_ordinal, lift_lt_aleph_one,
    ← lt_omega_iff_card_lt]

/-- Initial segments of ω₁ (as sets of `Omega1` elements) are countable.
This is the subtype-order version of `countable_Iio_of_lt_omega1`. -/
@[category API, AMS 5]
private lemma countable_Iio_omega1 (γ : Omega1) : (Set.Iio γ : Set Omega1).Countable := by
  -- The injection a ↦ ⟨a.1.val, a.2⟩ sends ↑(Iio γ : Set Omega1) into ↑(Iio γ.val : Set Ord)
  -- and the codomain is countable by countable_Iio_of_lt_omega1.
  haveI hcount := (countable_Iio_of_lt_omega1 γ.2).to_subtype
  -- Goal: (Set.Iio γ : Set Omega1).Countable = Set.Countable (Set.Iio γ)
  -- = Countable ↥(Set.Iio γ : Set Omega1) (by definition of Set.Countable)
  show Countable ↑(Set.Iio γ : Set Omega1)
  -- Use Function.Injective.countable with the injection a ↦ ⟨a.1.val, a.2⟩.
  apply Function.Injective.countable (β := ↑(Set.Iio γ.val : Set Ordinal.{0}))
    (f := fun (a : ↑(Set.Iio γ : Set Omega1)) => (⟨a.1.val, a.2⟩ : ↑(Set.Iio γ.val)))
  intro ⟨⟨av, hav_ω₁⟩, hav_γ⟩ ⟨⟨bv, hbv_ω₁⟩, hbv_γ⟩ h
  simp only [Subtype.mk.injEq] at h
  exact Subtype.ext (Subtype.ext h)

/-- Any countable subset of $\omega_1$ is bounded strictly below some element of $\omega_1$.
This uses the key property that $\omega_1$ has uncountable cofinality (it is regular). -/
@[category API, AMS 5]
private lemma countable_subset_bdd (S : Set Omega1) (hS : S.Countable) :
    ∃ γ : Omega1, ∀ s ∈ S, s < γ := by
  by_cases hemp : S.Nonempty
  · obtain ⟨f, hf⟩ := hS.exists_eq_range hemp
    have hf_lt' : ∀ n, (f n).1 < (ℵ_ 1).ord :=
      fun n => lt_of_lt_of_eq (f n).2 (ord_aleph 1).symm
    have hbdd : BddAbove (Set.range (fun n => (f n).1)) :=
      ⟨ω_ 1, fun o ⟨m, hm⟩ => hm ▸ (f m).2.le⟩
    have hlt : ⨆ n, (f n).1 < ω_ 1 :=
      lt_of_lt_of_eq (iSup_sequence_lt_omega_one _ hf_lt') (ord_aleph 1)
    -- `ω_ 1` is a limit ordinal (no ord_aleph rewrite needed).
    have hsucc_lt : (⨆ n, (f n).1) + 1 < ω_ 1 := by
      rw [← succ_eq_add_one]; exact (isSuccLimit_omega 1).succ_lt hlt
    refine ⟨⟨(⨆ n, (f n).1) + 1, hsucc_lt⟩, ?_⟩
    intro s hs; rw [hf] at hs; obtain ⟨n, rfl⟩ := hs
    show (f n).1 < (⨆ n, (f n).1) + 1
    rw [← succ_eq_add_one]
    exact lt_succ_of_le (le_ciSup hbdd n)
  · rw [Set.not_nonempty_iff_eq_empty] at hemp; rw [hemp]
    exact ⟨⟨0, omega_pos 1⟩, fun s hs => absurd hs (Set.notMem_empty _)⟩

/--
**Prikry–Mills counterexample** (key lemma):

There exists a 2-colouring $f$ of a set of cardinality $\aleph_1$ cubed such that
no countable box $A_1 \times B_1 \times C_1$ is monochromatic.

This is the unpublished result of Prikry and Mills (1978). The proof proceeds by
transfinite induction along $\omega_1$, which has uncountable cofinality, ensuring
every countable box is non-monochromatic.
-/
@[category research solved, AMS 3 5]
theorem erdos_1128.prikryMills :
    ∃ (X : Type) (_ : #X = aleph 1) (f : X → X → X → Fin 2),
      ∀ (A₁ B₁ C₁ : Set X),
        #A₁ = aleph 0 → #B₁ = aleph 0 → #C₁ = aleph 0 →
        ¬ IsMonochromaticBox f A₁ B₁ C₁ := by
  -- The Prikry–Mills construction (1978, unpublished):
  -- Take X = ω_ 1.ToType, which has cardinality ℵ₁ (by mk_ord_toType).
  --
  -- Construction by transfinite induction on γ < ω₁:
  -- * For each γ, since Iio γ is countable (card_le_aleph0_of_lt_omega1), choose an
  --   injection e_γ : Iio γ → ℕ. The injection is chosen to "kill" al

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
