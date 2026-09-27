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
# Idoneal numbers completeness conjecture

An integer $D>0$ is **idoneal** if every
integer that can be expressed in exactly one way (up to order and signs)
as $x^2 + D y^2$ with gcd(x, Dy)=1 is a prime power or twice a prime power.

The Idoneal Numbers Completeness Conjecture asserts that the following list of
65 numbers is complete:
1,2,3,4,5,6,7,8,9,10,12,13,15,16,18,21,22,24,25,28,30,33,37,40,42,45,48,
57,58,60,70,72,78,85,88,93,102,105,112,120,130,133,165,168,177,190,210,232,
240,253,273,280,312,330,345,357,385,408,462,520,760,840,1320,1365,1848.
*References:*
- [Wikipedia: Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
- [OEIS A000926](https://oeis.org/A000926)
-/

namespace Idoneal

/--
Equivalent definition: A positive integer $n$ is idoneal if and only if it cannot be written as
$ab + bc + ac$ for distinct positive integers $a, b,$ and $c$.
-/
def IsIdoneal (n : ℕ) : Prop :=
  0 < n ∧
    ¬ ∃ a b c : ℕ,
      0 < a ∧ a < b ∧ b < c ∧ n = a * b + b * c + a * c

/--
The 65 known idoneal numbers that are conjectured to be the only idoneal numbers.
-/
def knownIdonealNumbers : Finset ℕ :=
  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 21, 22, 24, 25, 28,
   30, 33, 37, 40, 42, 45, 48, 57, 58, 60, 70, 72, 78, 85, 88, 93, 102, 105,
   112, 120, 130, 133, 165, 168, 177, 190, 210, 232, 240, 253, 273, 280, 312,
   330, 345, 357, 385, 408, 462, 520, 760, 840, 1320, 1365, 1848}

/--
Reduces the unbounded search for a representation `n = a*b + b*c + a*c` (with
`0 < a < b < c`) to a *bounded, decidable* double search over `a, b ∈ range (n+1)`.

The third variable is not searched: for a fixed pair `a, b` the equation
`n = a*b + c*(a+b)` pins down `c = (n - a*b) / (a+b)`, so the witness `c` is
recovered by exact division. The forward direction uses `a, b ≤ n` (each pairwise
product is at most `n`) to land the pair in `range (n+1)`.
-/
@[category API, AMS 11]
private theorem exists_triple_iff_bounded (n : ℕ) :
    (∃ a b c : ℕ, 0 < a ∧ a < b ∧ b < c ∧ n = a * b + b * c + a * c) ↔
      (∃ a ∈ Finset.range (n + 1), ∃ b ∈ Finset.range (n + 1),
        0 < a ∧ a < b ∧ b < (n - a * b) / (a + b) ∧
          n = a * b + b * ((n - a * b) / (a + b)) + a * ((n - a * b) / (a + b))) := by
  constructor
  · rintro ⟨a, b, c, ha, hab, hbc, heq⟩
    have hbn : b ≤ n := by nlinarith
    have han : a ≤ n := by nlinarith
    have hsum : n - a * b = c * (a + b) := by
      have : n = a * b + c * (a + b) := by ring_nf; ring_nf at heq; linarith
      omega
    have hpos : 0 < a + b := by omega
    have hc : (n - a * b) / (a + b) = c := by rw [hsum]; exact Nat.mul_div_cancel _ hpos
    exact ⟨a, Finset.mem_range.mpr (by omega), b, Finset.mem_range.mpr (by omega),
      ha, hab, hc ▸ hbc, hc ▸ heq⟩
  · rintro ⟨a, _, b, _, ha, hab, hbc, heq⟩
    exact ⟨a, b, (n - a * b) / (a + b), ha, hab, hbc, heq⟩

set_option maxRecDepth 4096 in
/-- All 65 known idoneal numbers are indeed idoneal. -/
@[category test, AMS 11]
theorem knownIdonealNumbers_are_idoneal : ∀ n ∈ knownIdonealNumbers, IsIdoneal n := by
  intro n hn
  fin_cases hn <;>
    refine ⟨by norm_num, ?_⟩ <;>
    rw [exists_triple_iff_bounded] <;>
    native_decide

/--
Idoneal numbers completeness conjecture.
-/
@[category research open, AMS 11]
theorem idoneal_numbers_completeness :
    answer(sorry) ↔
      ∀ n : ℕ, IsIdoneal n → n ∈ knownIdonealNumbers := by
  sorry

end Idoneal


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
