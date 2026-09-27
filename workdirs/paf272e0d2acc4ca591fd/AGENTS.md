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
# Erdős Problem 445

*References:*
- [erdosproblems.com/445](https://www.erdosproblems.com/445)
- [He00] Heath-Brown, D. R., Arithmetic applications of {K}loosterman sums. Nieuw Arch. Wiskd. (5)
  (2000), 380--384.
- [MathOverflow](https://mathoverflow.net/questions/69509/small-residue-classes-with-small-reciprocal)
-/

open Filter

namespace Erdos445

/--
The property that there exist $a,b\in(n,n+p^c)$ such that $ab\equiv 1\pmod{p}$.
-/
def Erdos445Prop (c : ℝ) (p n : ℕ) : Prop :=
  ∃ a b : ℕ,
    n < a ∧ (a : ℝ) < (n : ℝ) + (p : ℝ) ^ c ∧
    n < b ∧ (b : ℝ) < (n : ℝ) + (p : ℝ) ^ c ∧
    a * b ≡ 1 [MOD p]

/--
Is it true that, for any $c>1/2$, if $p$ is a sufficiently large prime then, for any
$n\geq 0$, there exist $a,b\in(n,n+p^c)$ such that $ab\equiv 1\pmod{p}$?

This is discussed in this MathOverflow question [MathOverflow].
-/
@[category research open, AMS 11]
theorem erdos_445 :
    answer(sorry) ↔ ∀ c : ℝ, c > 1 / 2 →
      ∀ᶠ p : ℕ in atTop, p.Prime → ∀ n : ℕ, Erdos445Prop c p n := by
  sorry

/--
Heilbronn (unpublished) proved this for $c$ sufficiently close to $1$.
-/
@[category research solved, AMS 11]
theorem erdos_445.variants.heilbronn :
    ∃ c₀ < 1, ∀ c : ℝ, c > c₀ →
      ∀ᶠ p : ℕ in atTop, p.Prime → ∀ n : ℕ, Erdos445Prop c p n := by
  sorry

/--
Heath-Brown [He00] used Kloosterman sums to prove this for all $c>3/4$.
-/
@[category research solved, AMS 11]
theorem erdos_445.variants.heath_brown :
    ∀ c : ℝ, c > 3 / 4 →
      ∀ᶠ p : ℕ in atTop, p.Prime → ∀ n : ℕ, Erdos445Prop c p n := by
  sorry

/-- Small example: for $p=5$, $c=1$, $n=0$, the pair $(2,3) \in (0,5)$ satisfies
$2 \cdot 3 = 6 \equiv 1 \pmod{5}$. -/
@[category test, AMS 11]
theorem erdos_445.test.small_example : Erdos445Prop 1 5 1 := by
  refine ⟨2, 3, by omega, ?_, by omega, ?_, by native_decide⟩
  all_goals simp only [Real.rpow_one]; norm_num

end Erdos445


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
