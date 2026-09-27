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
# Erdős Problem 889

*Reference:* [erdosproblems.com/889](https://www.erdosproblems.com/889)
-/

open Finset Nat Filter Topology

namespace Erdos889

/--
$v(n,k)$ counts the prime factors of $n+k$ which do not divide $n+i$
for all $0 \le i < k$.
-/
def v (n k : ℕ) : ℕ :=
  ((n + k).primeFactors.filter (fun p =>
    ∀ i ∈ range k, ¬ p ∣ n + i)).card

/--
$v_0(n)$ is the supremum of $v(n,k)$ for all $k \ge 0$.
-/
noncomputable def v₀ (n : ℕ) : ℕ∞ :=
  ⨆ k, (v n k : ℕ∞)

/--
Let $v(n,k)$ count the prime factors of $n+k$ which
do not divide $n+i$ for $0\leq i < k$. Is it true that
$v_0(n)=\max_{k\geq 0}v(n,k)\to \infty$ as $n\to \infty$?
-/
@[category research open, AMS 11]
theorem erdos_889 : Tendsto v₀ atTop (𝓝 ⊤) := by
  sorry

/--
$v_0(n) > 1$ for all $n$ except $n$ = 0, 1, 2, 3, 4, 7, 8, 16

[ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.
-/
@[category research solved, AMS 11]
theorem erdos_889.variants.v0_gt_1 :
    ∀ n : ℕ, n ∉ ({0, 1, 2, 3, 4, 7, 8, 16} : Finset ℕ) → 1 < v₀ n := by
  sorry

/--
$v_l(n)$ is the supremum of $v(n,k)$ for all $k \ge l$
-/
noncomputable def v_l (l n : ℕ) : ℕ∞ :=
  ⨆ k ≥ l, (v n k : ℕ∞)

/--
Let $v_l(n) = \max_{k\geq l} v(n,k)$. For every fixed $l$,
$v_l(n) \to \infty$ as $n \to \infty$

[ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.
-/
@[category research open, AMS 11]
theorem erdos_889.variants.general :
    ∀ l, Tendsto (v_l l) atTop (𝓝 ⊤) := by
  sorry

/--
Does $v_1(n) = 1$ have finite solutions?

[ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.
-/
@[category research open, AMS 11]
theorem erdos_889.variants.v1_eq_1_finite :
    answer(sorry) ↔ {n | v_l 1 n = 1}.Finite := by
  sorry

/--
$V(n,k)$ is the number of primes $p$ such that
$p^\alpha$ exactly divides $n+k$ and
for all $0 \le i < k$, $p^\alpha$ does not divide $n+i$,
where $\alpha$ is the multiplicity of $p$ in the factorization of $n+k$.
-/
def V (n k : ℕ) : ℕ :=
  ((n + k).primeFactors.filter (fun p =>
    ∀ i ∈ range k, ¬ p ^ ((n + k).factorization p) ∣ n + i)).card

/--
$V_l(n)$ is the supremum of $V(n,k)$ for all $k \ge l$
-/
noncomputable def V_l (l n : ℕ) : ℕ∞ :=
  ⨆ k ≥ l, (V n k : ℕ∞)

/--
Does $V_1(n) = 1$ have finite solutions?

This is a modification of `erdos_889.variants.v1_eq_1_finite`,
which might make it more amenable to attack according to [ErSe67].

[ErSe67] Erdős, P. and Selfridge, J. L., Some problems on the prime factors of consecutive integers. Illinois J. Math. (1967), 428--430.
-/
@[category research open, AMS 11]
theorem erdos_889.variants.V1_eq_1_finite :
    answer(sorry) ↔ {n | V_l 1 n = 1}.Finite := by
  sorry

end Erdos889


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
