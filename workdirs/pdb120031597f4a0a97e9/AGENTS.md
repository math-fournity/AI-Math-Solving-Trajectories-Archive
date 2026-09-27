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
# Erdős Problem 930

*Reference:* [erdosproblems.com/930](https://www.erdosproblems.com/930)
-/

open Finset

namespace Erdos930

/--
$n$ is a perfect power if there exist natural numbers $m$ and $l$
such that $1 < l$ and $m^l = n$.
-/
def IsPower (n : ℕ) : Prop :=
  ∃ m l, 1 < l ∧ m^l = n

/--
Is it true that, for every $r$, there is a $k$ such that
if $I_1,\ldots,I_r$ are disjoint intervals of consecutive integers,
all of length at least $k$, then
$$
  \prod_{1\leq i\leq r}\prod_{m\in I_i}m
$$
is not a perfect power?
-/
@[category research open, AMS 11]
theorem erdos_930 :
    answer(sorry) ↔ ∀ r > 0, ∃ k, ∀ I₁ I₂ : Fin r → ℕ,
      (∀ i : Fin r, 0 < I₁ i ∧ I₁ i + k ≤ I₂ i + 1) →
        (∀ i j : Fin r, i < j → I₂ i < I₁ j) →
          ¬ IsPower (∏ i : Fin r, ∏ m ∈ Icc (I₁ i) (I₂ i), m) := by
  sorry

/--
Returns the least prime satisfying $k \le p$
-/
def nextPrime (k : ℕ) : ℕ :=
  Nat.find (Nat.exists_infinite_primes k)

/--
Let $k$, $l$, $n$ be integers such that $k \ge 3$, $l \ge 2$ and $n + k \ge p^{(k)}$,
where $p^{(k)}$ is the least prime satisfying $p^{(k)} \ge k$.
Then there is a prime $p \ge k$ for which $l$ does not divide
the multiplicity of the prime factor $p$ in $(n + 1) \ldots (n + k)$.

Theorem 2 from [ErSe75].

[ErSe75] Erdős, P. and Selfridge, J. L., The product of consecutive integers is never a power. Illinois J. Math. (1975), 292-301.
-/
@[category research solved, AMS 11]
theorem erdos_930.variants.consecutive_strong :
    ∀ k l n, 3 ≤ k → 2 ≤ l → nextPrime k ≤ n + k →
      ∃ p, k ≤ p ∧ p.Prime ∧
        ¬ (l ∣ Nat.factorization (∏ m ∈ Icc (n + 1) (n + k), m) p) := by
  sorry

/--
Erdos and Selfridge [ErSe75] proved that the product of
consecutive integers is never a power (establishing the case $r=1$).

Theorem 1 from [ErSe75].

It is implied from `erdos_930.variants.consecutive_strong`.

[ErSe75] Erdős, P. and Selfridge, J. L., The product of consecutive integers is never a power. Illinois J. Math. (1975), 292-301.
-/
@[category research solved, AMS 11]
theorem erdos_930.variants.consecutive_integers :
    ∀ n k, 0 ≤ n → 2 ≤ k →
      ¬ IsPower (∏ m ∈ Icc (n + 1) (n + k), m) := by
  sorry

end Erdos930


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
