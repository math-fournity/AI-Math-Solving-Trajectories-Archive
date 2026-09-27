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
# Erdős Problem 891

*References:*
- [erdosproblems.com/891](https://www.erdosproblems.com/891)
- [Po18] Pólya, Georg, Zur arithmetischen {U}ntersuchung der {P}olynome. Math. Z. (1918), 143--148.
- [Wikipedia] https://en.wikipedia.org/wiki/Dickson%27s_conjecture
-/

open Nat Filter Finset
open scoped ArithmeticFunction.omega

namespace Erdos891

/--
Let $2=p_1 < p_2 < \cdots$ be the primes and $k\geq 2$. Is it true that, for all sufficiently large
$n$, there must exist an integer in $[n,n+p_1\cdots p_k)$ with $>k$ many prime factors?
-/
@[category research open, AMS 11]
theorem erdos_891 :
    answer(sorry) ↔
      ∀ k ≥ 2, ∀ᶠ n in atTop,
      ∃ m ∈ Ico n (n + ∏ i ∈ range k, i.nth Nat.Prime), k < ω m := by
  sorry

/--
Schinzel deduced from Pólya's theorem [Po18] (that the sequence of $k$-smooth integers has unbounded
gaps) that this is true with $p_1\cdots p_k$ replaced by $p_1\cdots p_{k-1}p_{k+1}$.
-/
@[category research solved, AMS 11]
theorem erdos_891.variants.schinzel :
    ∀ k ≥ 2, ∀ᶠ n in atTop,
      ∃ m ∈ Ico n (n + (∏ i ∈ range (k - 1), i.nth Nat.Prime) * k.nth Nat.Prime),
      k < ω m := by
  sorry

/--
This is unknown even for $k=2$ - that is, is it true that in every interval of $6$
(sufficiently large) consecutive integers there must exist one with at least $3$ prime factors?
-/
@[category research open, AMS 11]
theorem erdos_891.variants.case_k_2 :
    answer(sorry) ↔ ∀ᶠ n in atTop,
      ∃ m ∈ Ico n (n + 6), 3 ≤ ω m := by
  sorry

/--
Weisenberg has observed that Dickson's conjecture implies the answer is no if we replace
$p_1\cdots p_k$ with $p_1\cdots p_k-1$. Indeed, let $L_k$ be the lowest common multiple of all
integers at most $p_1\cdots p_k$. By Dickson's conjecture [Wikipedia], there are infinitely many
$n'$ such that $\frac{L_k}{m}n'+1$ is prime for all $1\leq m < p_1\cdots p_k$. It follows that,
if $n=L_kn'+1$, then all integers in $[n,n+p_1\cdots p_k-1)$ have at most $k$ prime factors.
-/
@[category research open, AMS 11]
theorem erdos_891.variants.weisenberg (k : ℕ) (hk : k ≥ 2) :
    ∃ᶠ n in atTop,
      ∀ m ∈ Ico n (n + (∏ i ∈ range k, i.nth Nat.Prime) - 1),
      ω m ≤ k := by
  sorry

end Erdos891


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
