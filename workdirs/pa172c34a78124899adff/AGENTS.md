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
# Erdős Problem 1209

*References:*
- [erdosproblems.com/429](https://www.erdosproblems.com/429)
- [erdosproblems.com/1102](https://www.erdosproblems.com/1102)
- [erdosproblems.com/1209](https://www.erdosproblems.com/1209)
- [Er80] Erdős, Paul, A survey of problems in combinatorial number theory. Ann. Discrete Math.
  (1980), 89-115.
-/

open Nat Set

namespace Erdos1209

/--
Let $A=\{a_1<a_2<\cdots\}$ be a sequence of integers which tends to infinity sufficiently fast.
If there is an $n$ such that all $n+a_k$ are primes then must there exist infinitely many such $n$?

Erdős [Er80] wrote 'unless I overlook a trivial way of getting a counterexample these questions
are quite hopeless'. There is indeed a trivial counterexample (a variant of the construction in
[erdosproblems.com/429]): define $a_1=2$ and for $k\geq 2$ let $a_k>a_{k-1}$ be a prime such that
$a_k+k\equiv 0\pmod{q_k}$, where $q_k$ is some prime not dividing $k$. This sequence can be made to
grow arbitrarily fast

See also [erdosproblems.com/429] and [erdosproblems.com/1102].
-/
@[category research solved, AMS 11]
theorem erdos_1209.parts.i :
    answer(False) ↔
      ∃ f : ℕ → ℕ, ∀ a : ℕ → ℕ, StrictMono a → (∀ k, f k ≤ a k) →
        (∃ n, ∀ k, (n + a k).Prime) →
        {n | ∀ k, (n + a k).Prime}.Infinite := by
  sorry

/--
What if we ask for $n+a_k$ to be squarefree instead of prime?

A similar construction provides a counterexample to the squarefree question.
-/
@[category research solved, AMS 11]
theorem erdos_1209.parts.ii :
    answer(False) ↔
      ∃ f : ℕ → ℕ, ∀ a : ℕ → ℕ, StrictMono a → (∀ k, f k ≤ a k) →
        (∃ n, ∀ k, Squarefree (n + a k)) →
        {n | ∀ k, Squarefree (n + a k)}.Infinite := by
  sorry

/--
Are there $n$ such that $n+2^{2^k}$ is always a prime?

ebarschkis and GPT have proved that there are no $n$ such that $n+2^{2^k}$ is always prime: let
$n\geq 3$ be any odd integer. If $k$ is chosen sufficiently large, and $p=n+2^{2^{k}}$ is prime,
then the multiplicative order of $2^{2^k}\pmod{p}$, say $m$ is odd, and hence if $l$ is chosen such
that $2^l\equiv 1\pmod{m}$ then $p\mid n+2^{2^{k+rl}}$ for all $r\geq 1$.

This was formalized in Lean by Barschkis using ChatGPT.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/ebarschkis/ErdosProblem/blob/main/Problem1209/Formalization.lean"]
theorem erdos_1209.parts.iii.a :
    answer(False) ↔ ∃ n : ℕ, ∀ k : ℕ, (n + 2 ^ (2 ^ k)).Prime := by
  sorry

/--
Are there $n$ such that $n+2^{2^k}$ is always squarefree?
-/
@[category research open, AMS 11]
theorem erdos_1209.parts.iii.b :
    answer(sorry) ↔ ∃ n : ℕ, ∀ k : ℕ, Squarefree (n + 2 ^ (2 ^ k)) := by
  sorry

/--
Are there $n$ such that $n+2^{2^k}$ is infinitely often a prime?
-/
@[category research open, AMS 11]
theorem erdos_1209.parts.iii.c :
    answer(sorry) ↔ ∃ n : ℕ, {k | (n + 2 ^ (2 ^ k)).Prime}.Infinite := by
  sorry

/--
Are there $n$ such that $n+2^{2^k}$ is infinitely often squarefree?
-/
@[category research open, AMS 11]
theorem erdos_1209.parts.iii.d :
    answer(sorry) ↔ ∃ n : ℕ, {k | Squarefree (n + 2 ^ (2 ^ k))}.Infinite := by
  sorry

end Erdos1209


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
