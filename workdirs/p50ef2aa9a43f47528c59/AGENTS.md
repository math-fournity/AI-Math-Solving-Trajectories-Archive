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
# Erdős Problem 17
*Reference:* [erdosproblems.com/17](https://www.erdosproblems.com/17)
-/

open Filter Asymptotics Real

namespace Erdos17

/-- A prime $p$ is a cluster prime if every even natural number
$n \le p - 3$ can be written as a difference of two primes
$q_1 - q_2$ with $q_1, q_2 \le p$. -/
def IsClusterPrime (p : ℕ) : Prop :=
  p.Prime ∧
    ∀ {n : ℕ}, Even n → n ≤ (p - 3 : ℤ) →
      ∃ q₁ q₂ : ℕ, q₁.Prime ∧ q₂.Prime ∧
        q₁ ≤ p ∧ q₂ ≤ p ∧ n = (q₁ - q₂ : ℤ)

/-- **Erdős Problem 17.** Are there infinitely many cluster primes? -/
@[category research open, AMS 11]
theorem erdos_17 : answer(sorry) ↔ {p : ℕ | IsClusterPrime p}.Infinite := by
  sorry

/-- The counting function of cluster primes $\le n$. -/
noncomputable def clusterPrimeCount (n : ℕ) : ℕ :=
  Nat.card {p : ℕ | p ≤ n ∧ IsClusterPrime p}

/--
In 1999 Blecksmith, Erdős, and Selfridge [BES99] proved the upper bound
$$\pi^{\mathcal{C}}(x) \ll_A x(\log x)^{-A}$$ for every real $A > 0$.

[BES99] Blecksmith, Richard and Erd\H os, Paul and Selfridge, J. L., Cluster primes. Amer. Math. Monthly (1999), 43--48.
-/
@[category research solved, AMS 11]
theorem erdos_17.variants.upper_BES {A : ℝ} (hA : 0 < A) :
  (fun x ↦ (clusterPrimeCount x : ℝ)) =O[atTop] fun x ↦ x / (log x) ^ A := by
    sorry

/--
In 2003, Elsholtz [El03] refined the upper bound to
$$\pi^{\mathcal{C}}(x) \ll x\,\exp\!\bigl(-c(\log\log x)^2\bigr)$$
for every real $0 < c < 1/8$.

[El03] Elsholtz, Christian, On cluster primes. Acta Arith. (2003), 281--284.
-/
@[category research solved, AMS 11]
theorem erdos_17.variants.upper_Elsholtz :
  ∃ C : ℝ, 0 < C ∧
    ∀ c ∈ Set.Ioo 0 (1 / 8),
      IsBigOWith C atTop (fun x ↦ (clusterPrimeCount x : ℝ))
        (fun x ↦ x * exp (-c * (log (log x)) ^ 2)) := by
  sorry

/-- $97$ is the smallest prime that is not a cluster prime. -/
@[category test, AMS 11]
theorem isClusterPrime_97_isLeast_non_cluster : IsLeast {p : ℕ | p.Prime ∧ ¬ IsClusterPrime p} 97 := by
  -- For a prime `p`, being a cluster prime is equivalent to a fully bounded
  -- (hence decidable) statement over `ℕ`: every even `n ≤ p - 3` is `q₁ - q₂`
  -- for primes `q₁, q₂ ≤ p`, which (since `n ≥ 0`) amounts to a prime `q₂ ≤ p`
  -- with `q₂ + n` again prime and `≤ p`.
  have cluster_iff : ∀ p : ℕ, p.Prime →
      (IsClusterPrime p ↔
        (∀ n ∈ Finset.range (p - 2), Even n →
          ∃ q₂ ∈ Finset.range (p + 1), (Nat.Prime q₂) ∧ Nat.Prime (q₂ + n) ∧ q₂ + n ≤ p)) := by
    intro p hp
    constructor
    · rintro ⟨-, h⟩ n hn hev
      simp only [Finset.mem_range] at hn
      have hn3 : (n : ℤ) ≤ (p - 3 : ℤ) := by omega
      obtain ⟨q₁, q₂, hq1p, hq2p, hq1le, hq2le, heq⟩ := h hev hn3
      refine ⟨q₂, ?_, hq2p, ?_, ?_⟩
      · simp only [Finset.mem_range]; omega
      · have hq2n : q₂ + n = q₁ := by omega
        rw [hq2n]; exact hq1p
      · omega
    · intro h
      refine ⟨hp, ?_⟩
      intro n hev hn3
      have hnp : n ≤ p - 3 := by omega
      have hnrange : n ∈ Finset.range (p - 2) := by
        simp only [Finset.mem_range]; omega
      obtain ⟨q₂, hq2r, hq2p, hq1p, hle⟩ := h n hnrange hev
      refine ⟨q₂ + n, q₂, hq1p, hq2p, hle, ?_, ?_⟩
      · simp only [Finset.mem_range] at hq2r; omega
      · push_cast; ring
  constructor
  · -- `97` is prime but not a cluster prime: the even number `88 ≤ 94` is not a
    -- difference of two primes `≤ 97`.
    refine ⟨by norm_num, ?_⟩
    rw [cluster_iff 97 (by norm_num)]
    simp only [Nat.reduceSub, Finset.mem_range, Nat.reduceAdd, not_forall, not_exists, not_and,
      not_le]
    refine ⟨88, by norm_num, by norm_num, ?_⟩
    intro x xl hx xl
    suffices 9 < x by
      lia
    contrapose! xl
    interval_cases x <;> norm_num
    · contrapose hx
      exact Nat.not_prime_one
    · contrapose hx
      norm_num
  · -- `97` is a lower bound: every prime `< 97` is a cluster prime, so cannot lie
    -- in the set of non-cluster primes.
    rintro b ⟨hbp, hbnc⟩
    by_contra hlt
    push_neg at hlt
    interval_cases b <;>
      first
        | exact absurd hbp (by decide)
        | exact hbnc ((cluster_iff _ (by norm_num)).mpr (by set_option maxRecDepth 8000 in decide))

end Erdos17


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
