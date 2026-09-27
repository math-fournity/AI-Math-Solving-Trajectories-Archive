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
# Erdős Problem 394

*References:*
- [erdosproblems.com/394](https://www.erdosproblems.com/394)
- [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
  theory. Monographies de L'Enseignement Mathematique (1980).
- [ErHa78] Erdős, P. and Hall, R. R., On some unconventional problems on the divisors of integers.
  J. Austral. Math. Soc. Ser. A (1978), 479--485.
-/

open Nat Filter Finset
open scoped Asymptotics Topology Nat

namespace Erdos394

/--
Let $t_k(n)$ denote the least $m$ such that $n\mid m(m+1)(m+2)\cdots (m+k-1).$
-/
noncomputable def t (k n : ℕ) : ℕ :=
  sInf { m : ℕ | 0 < m ∧ n ∣ ∏ i ∈ range k, (m + i) }

/-- `t k n = v` when `v` works and nothing positive below it does. -/
@[category API, AMS 11]
theorem t_eq_of {n k v : ℕ} (hv : 0 < v)
    (hdvd : n ∣ ∏ i ∈ range k, (v + i))
    (hlt : ∀ m ∈ range v, 0 < m → ¬ (n ∣ ∏ i ∈ range k, (m + i))) :
    t k n = v := by
  refine le_antisymm (Nat.sInf_le ⟨hv, hdvd⟩) ?_
  by_contra hc
  push_neg at hc
  have hne : { m : ℕ | 0 < m ∧ n ∣ ∏ i ∈ range k, (m + i) }.Nonempty := ⟨v, hv, hdvd⟩
  obtain ⟨hpos, hd⟩ := Nat.sInf_mem hne
  exact hlt _ (mem_range.mpr hc) hpos hd

/-- The least positive multiple of `n` is `n`, so `t 1 n = n`. -/
@[category API, AMS 11]
theorem t_one {n : ℕ} (hn : 0 < n) : t 1 n = n := by
  refine le_antisymm (Nat.sInf_le ⟨hn, by simp⟩) ?_
  have hne : { m : ℕ | 0 < m ∧ n ∣ ∏ i ∈ range 1, (m + i) }.Nonempty := ⟨n, hn, by simp⟩
  obtain ⟨hpos, hd⟩ := Nat.sInf_mem hne
  rw [prod_range_one, add_zero] at hd
  exact Nat.le_of_dvd hpos hd

/--
Is it true that $\sum_{n\leq x}t_2(n)\ll \frac{x^2}{(\log x)^c}$ for some $c>0$?
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-394/Research/FirstQuestion.lean"]
theorem erdos_394.parts.i :
    answer(True) ↔
      ∃ c > 0, (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
      (t 2 n : ℝ)) ≪ (fun x ↦ x ^ 2 / (Real.log x) ^ c) := by
  sorry

/--
Is it true that, for $k\geq 2$, $\sum_{n\leq x}t_{k+1}(n) =o\left(\sum_{n\leq x}t_k(n)\right)?$
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-394/Research/DenseHierarchyLittleO.lean"]
theorem erdos_394.parts.ii :
    answer(True) ↔
      ∀ k ≥ 2, (fun (x : ℝ) ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
      (t (k + 1) n : ℝ)) =o[atTop]
      (fun (x : ℝ) ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
      (t k n : ℝ)) := by
  sorry

/--
In [ErGr80] they mention a conjecture of Erdős that the sum is $o(x^2)$. This was proved by Erdős
and Hall [ErHa78], who proved that in fact
$\sum_{n\leq x}t_2(n)\ll \frac{\log\log\log x}{\log\log x}x^2.$
-/
@[category research solved, AMS 11]
theorem erdos_394.variants.hall_bound :
    (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊, (t 2 n : ℝ)) ≪
    (fun x ↦ x ^ 2 * (Real.log (Real.log (Real.log x)) / Real.log (Real.log x))) := by
  sorry

/--
Erdős and Hall conjecture that the sum is $o(x^2/(\log x)^c)$ for any $c<\log 2$.
-/
@[category research open, AMS 11]
theorem erdos_394.variants.hall_conjecture :
    ∀ c < Real.log 2, (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
    (t 2 n : ℝ)) =o[atTop]
    (fun x ↦ x ^ 2 / (Real.log x) ^ c) := by
  sorry

/--
Since $t_2(p)=p-1$ for prime $p$ it is trivial that $\sum_{n\leq x}t_2(n)\gg \frac{x^2}{\log x}$.
-/
@[category research solved, AMS 11]
theorem erdos_394.variants.lower_bound :
    (fun x ↦ x ^ 2 / Real.log x) ≫
    (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊, (t 2 n : ℝ)) := by
  sorry

/--
They ask about the behaviour of $t_{n-3}(n!)$ and also ask whether, for infinitely many $n$,
$t_k(n!)< t_{k-1}(n!)-1$ for all $1\leq k < n$.
-/
@[category research open, AMS 11]
theorem erdos_394.variants.factorial_gap_conjecture :
    answer(sorry) ↔
      Set.Infinite { n : ℕ | ∀ k, 2 ≤ k → k < n →
      t k (n !) < t (k - 1) (n !) - 1 } := by
  sorry

set_option maxRecDepth 20000 in
/--
They proved (with Selfridge) that this holds for $n=10$.
-/
@[category research solved, AMS 11]
theorem erdos_394.variants.factorial_gap_10 :
    ∀ (k : ℕ), 2 ≤ k → k < 10 →
    t k (10 !) <
    t (k - 1) (10 !) - 1 := by
  have h1 : t 1 (10 !) = 3628800 := by rw [t_one] <;> norm_num [Nat.factorial]
  have h2 : t 2 (10 !) = 512000 := by
    norm_num [Nat.factorial]; exact t_eq_of (by norm_num) (by native_decide) (by native_decide)
  have

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
