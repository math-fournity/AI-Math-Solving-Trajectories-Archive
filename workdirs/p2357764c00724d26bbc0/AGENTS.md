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
# Erdős Problem 686

*References:*
- [erdosproblems.com/686](https://www.erdosproblems.com/686)
- [Er79d] Erdős, P., *Some unconventional problems in number theory*. Acta Math.
  Acad. Sci. Hungar. (1979), 71-80.
-/

namespace Erdos686

/--
Can every integer $N≥2$ be written as
$$N=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
for some $k≥2$ and $m≥n+k$?
-/
@[category research open, AMS 11]
theorem erdos_686 :
    answer(sorry) ↔ ∀ N ≥ (2 : ℕ), ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (N : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i)) := by
  sorry

/--
Can every square $N≥2$ be written as
$$N=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
for some $k≥2$ and $m≥n+k$?
-/
@[category research open, AMS 11]
theorem erdos_686.variants.square :
    answer(sorry) ↔ ∀ N ≥ (2 : ℕ),  (IsSquare N) → ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (N : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i)) := by
  sorry

/--
Can $4$ be written as
$$4=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
for some $k≥2$ and $m≥n+k$?
-/
@[category research open, AMS 11]
theorem erdos_686.variants.four :
    answer(sorry) ↔ ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (4 : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i)) := by
  sorry

/--
The number $4$ cannot be written as
$$4=\frac{\prod_{1\leq i\leq 2}(m+i)}{\prod_{1\leq i\leq 2}(n+i)}$$
for $m≥n+2$!
-/
@[category research solved, AMS 11]
theorem erdos_686.variants.four_two :
    ¬ ∃ᵉ (n : ℕ) (m ≥ n + 2),
      (4 : ℚ) = (∏ i ∈ Finset.Icc 1 2, (m + i)) / (∏ i ∈ Finset.Icc 1 2, (n + i)) := by
  simp only [Finset.prod_Icc_succ_top (by decide : 1 ≤ 2), Finset.Icc_self,
    Finset.prod_singleton]
  push_neg
  intro n m hm
  rw [ne_eq, eq_div_iff (by positivity : (↑((n + 1) * (n + (1 + 1))) : ℚ) ≠ 0)]
  push_cast
  intro h
  have h' : 4 * ((n + 1) * (n + 2)) = (m + 1) * (m + 2) := by exact_mod_cast h
  by_cases hc : m < 2 * (n + 1) <;> nlinarith

/--
The number $4$ cannot be written as
$$4=\frac{\prod_{1\leq i\leq 3}(m+i)}{\prod_{1\leq i\leq 3}(n+i)}$$
for $m≥n+3$!

See [comment section on erdosproblems.com](https://www.erdosproblems.com/forum/thread/686#post-4599)
-/
@[category research solved, AMS 11]
theorem erdos_686.variants.four_three :
    ¬ ∃ᵉ (n : ℕ) (m ≥ n + 3),
      (4 : ℚ) = (∏ i ∈ Finset.Icc 1 3, (m + i)) / (∏ i ∈ Finset.Icc 1 3, (n + i)) := by
  sorry

/--
Can $9$ be written as
$$9=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
for some $k≥2$ and $m≥n+k$?
-/
@[category research solved, AMS 11]
theorem erdos_686.variants.nine :
    answer(True) ↔ ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (9 : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i)) := by
  -- Witness: k = 3, n = 11, m = 25, since (26·27·28)/(12·13·14) = 19656/2184 = 9.
  simp only [true_iff]
  refine ⟨3, by norm_num, 11, 25, by norm_num, ?_⟩
  norm_num [Finset.prod_Icc_succ_top, Finset.Icc_self, Finset.prod_singleton]

/--
Can $25$ be written as
$$25=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
for some $k≥2$ and $m≥n+k$?
-/
@[category research open, AMS 11]
theorem erdos_686.variants.twenty_five :
    answer(sorry) ↔ ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (25 : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i)) := by
  sorry

/--
Can every non-square $N≥2$ be written as
$$N=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
for some $k≥2$ and $m≥n+k$?
-/
@[category research solved, AMS 11]
theorem erdos_686.variants.non_square :
    answer(True) ↔ ∀ N ≥ (2 : ℕ), (¬ IsSquare N) → ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (N : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i)) := by
  refine ⟨fun _ N hN_ge_2 hN_not_square => ?_, fun _ => trivial⟩

  have hN_not_square' : ¬ ∃ s, s * s = N := fun ⟨s, hs⟩ => hN_not_square ⟨s, hs.symm⟩

  -- 1. Setup the existence for k = 2 and simplify the products
  exists 2, by valid
  field_simp
  simp [Finset.prod_Icc_succ_top, Finset.Icc_self, Finset.prod_singleton]

  -- 2. Case split on the existence of solutions for small bounds
  by_cases h : {n | ∃ k, N * ((n + 1) * (n + 2)) = (k + 1) * (k + 2)}.Nonempty
  · obtain rfl | hN_lt := hN_ge_2.eq_or_lt
    · exact mod_cast
        if a : ∃ a ∈ Finset.range 30, ∃ n ∈ Finset.range 30, _ then
          a.imp fun a s => s.2.imp fun a

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
