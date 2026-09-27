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
# Are prime numbers among sums of prime numbers distributed as $\frac n{2\ln(n)}$?

*Reference:*

[mathoverflow.net/questions/434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn)

[Me18] Meštrović, R., *Curious Conjectures on the Distribution of Primes
Among the Sums of the First `2n` Primes*, [arXiv:1804.04198](https://arxiv.org/abs/1804.04198)
(2018), Conjecture 3.3.
-/

namespace MathOverflow434111

open Nat Filter Topology Asymptotics

/-- $S_n$ is the sum of the first `n` primes, i.e. $S_n=p_1+\dots+p_n$, $1$-indexed,
matching the MathOverflow question. -/
noncomputable def S (n : ℕ) : ℕ := ∑ k ∈ Finset.range n, nth Nat.Prime k

/-- $\pi_n$ counts how many of $S_1,S_2,\dots,S_n$ are themselves prime,
i.e. $\pi_n$ as used on MathOverflow (compare to $\pi_n$ in [Me18, Conjecture 3.3],
which instead ranges over $S_2,S_4,\dots,S_{2n}$). -/
noncomputable def piRestricted (n : ℕ) : ℕ :=
  ((Finset.Icc 1 n).filter (fun k => Nat.Prime (S k))).card

/-- The conjecture claims that $\pi_n\sim\frac n{2\ln(n)}$.

In other words, primes are distributed among the much sparser sequence $(S_n)_n$
with essentially the same density as in the positive integers, up to a factor of $2$.

[MathOverflow 434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn).

[Me18] Meštrović, R., *Curious Conjectures on the Distribution of Primes
Among the Sums of the First `2n` Primes*, [arXiv:1804.04198](https://arxiv.org/abs/1804.04198)
(2018).
-/
@[category research open, AMS 11]
theorem restricted_prime_number_theorem :
    answer(sorry) ↔ ((fun n : ℕ => (piRestricted n : ℝ)) ~[atTop] (fun n : ℕ => (n : ℝ) / (2 * Real.log n))) := by
  sorry

/--
Meštrović's original formulation [Me18, Conjecture 3.3]: the sequence of sums of the
first $2m$ primes satisfies the Restricted Prime Number Theorem, $\pi(m, (S_{2m})) \sim \frac{m}{\ln m}$.
-/
@[category research open, AMS 11]
theorem restricted_prime_number_theorem.variants.even_subsequence :
    answer(sorry) ↔
      ((fun m : ℕ => (((Finset.Icc 1 m).filter (fun k => Nat.Prime (S (2 * k)))).card : ℝ)) ~[atTop]
        (fun m : ℕ => (m : ℝ) / Real.log m)) := by
  sorry

end MathOverflow434111


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
