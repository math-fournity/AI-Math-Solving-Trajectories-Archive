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
# Optimal monotone families for the discrete isoperimetric inequality

*References:*
- [mathoverflow/10799](https://mathoverflow.net/questions/10799)
  asked by user [*Gil Kalai*](https://mathoverflow.net/users/1532/gil-kalai)
- [Optimal Monotone Families for the Discrete Isoperimetric Inequality](https://gilkalai.wordpress.com/ai/optimal-monotone-families-for-the-discrete-isoperimetric-inequality/)
  by *Gil Kalai* (2026), a Polymath project with AI agents
- [An Isoperimetric Inequality for the Hamming Cube and Integrality Gaps in Bounded-Degree
  Graphs](https://arxiv.org/abs/math/0603218) by *Jeff Kahn* and *Gil Kalai* (2006)
- [A Proof of the Kahn–Kalai Conjecture](https://arxiv.org/abs/2203.17207) by *Jinyoung Park*
  and *Huy Tuan Pham* (2022)

-/

namespace Mathoverflow10799

open Finset Real

/--
Start with a set $X=\{1,2,...,n\}$ of $n$ elements and the family $2^X$ of all subsets of $X$.
For a real number $p$ between zero and one, we consider a probability distribution $\mu_p$ on
$2^X$ where the probability that $i \in S$ is $p$, independently for different $i$'s.
Thus for $p=1/2$ we get the uniform probability distribution.

For $S \subseteq \{0, \ldots, n-1\}$, its probability is $p^{|S|} (1-p)^{n - |S|}$.
-/
noncomputable def μ {n : ℕ} (p : ℝ) (S : Finset (Fin n)) : ℝ :=
  p ^ #S * (1 - p) ^ (n - #S)

/-- For $p = 1/2$, the $p$-biased measure is the uniform distribution:
$\mu_{1/2}(S) = (1/2)^n$ for every $S \subseteq [n]$. -/
@[category test, AMS 5]
theorem μ_half_eq_uniform {n : ℕ} (S : Finset (Fin n)) :
    μ (1/2) S = (1/2 : ℝ) ^ n := by
  have h : #S ≤ n := S.card_le_univ.trans_eq (Fintype.card_fin n)
  simp only [μ]
  rw [show (1 : ℝ) - 1 / 2 = 1 / 2 from by ring, ← pow_add, Nat.add_sub_cancel' h]

/--
The $p$-biased measure of a family $\mathcal F \subseteq 2^{[n]}$,
i.e. $\mu_p(\mathcal F) = \sum_{S \in \mathcal F} \mu_p(S)$.
-/
noncomputable def μFamily {n : ℕ} (p : ℝ) (F : Finset (Finset (Fin n))) : ℝ :=
  ∑ S ∈ F, μ p S

/--
Given a family $F$, for a subset $S$ of $X$, we write $h(S)$ as the number of subsets $T$ in $X$
such that
(1) $T$ differs from $S$ in exactly one element
(2) Exactly one set among $S$ and $T$ belongs to $F$.
-/
def boundaryCount (n : ℕ) (F : Finset (Finset (Fin n))) (S : Finset (Fin n)) : ℕ :=
  (Finset.univ.filter fun i : Fin n ↦ Xor' (S ∈ F) (symmDiff S {i} ∈ F)).card

/--
Test lemma showing that `boundaryCount` is equivalent to counting subsets $T$
that differ from $S$ in exactly one element and exactly one of $S, T$ belongs to $F$.
-/
@[category test, AMS 5]
theorem boundaryCount_equiv (n : ℕ) (F : Finset (Finset (Fin n))) (S : Finset (Fin n)) :
    boundaryCount n F S = (Finset.univ.filter fun T : Finset (Fin n) ↦
      (symmDiff S T).card = 1 ∧ Xor' (S ∈ F) (T ∈ F)).card := by
  unfold boundaryCount
  have h_cancel : ∀ (A : Finset (Fin n)), symmDiff S (symmDiff S A) = A := by
    intro A
    ext x
    simp only [Finset.mem_symmDiff]
    tauto
  have h_inj : Function.Injective (fun i : Fin n => symmDiff S {i}) := by
    intro i j hij
    dsimp at hij
    have h1 : symmDiff S (symmDiff S {i}) = symmDiff S (symmDiff S {j}) := by rw [hij]
    rw [h_cancel, h_cancel] at h1
    exact Finset.singleton_injective h1
  rw [← Finset.card_map ⟨fun i => symmDiff S {i}, h_inj⟩]
  congr 1
  ext T
  simp only [Finset.mem_map, Finset.mem_filter, Finset.mem_univ, true_and,
    Function.Embedding.coeFn_mk]
  constructor
  · rintro ⟨i, hi, rfl⟩
    refine ⟨?_, hi⟩
    rw [h_cancel]
    simp only [Finset.card_singleton]
  · rintro ⟨hcard, hxor⟩
    obtain ⟨i, hi⟩ := Finset.card_eq_one.mp hcard
    have hT : T = symmDiff S {i} := by
      rw [← hi, h_cancel]
    refine ⟨i, ?_, hT.symm⟩
    rwa [hT] at hxor

/--
The edge-boundary of $F$ is the expectation of $h(S)$ (according to $\mu_p$) over all
subsets $S$ of $X$. It is denoted by $I^p(F)$.
-/
noncomputable def edgeBoundary (n : ℕ) (p : ℝ) (F : Finset (Finset (Fin n))) : ℝ :=
  ∑ S : Finset (Fin n), μ p S * boundaryCount n F S

/--
A family $F$ of subsets of $2^X$ is monotone increasing if when $S$ belongs to $F$ and $T$
contains $S$ then $T$ also belongs to $F$. (Monotone increasing families also also called "filtes"
and "up-families".) From now on we will restrict our attention to the case of monotone increasing
families.

This is Mathlib's `IsUpperSet` applied to the coercion of $\mathcal F$ to a set,
using the fact that 

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
