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
# Erdős Problem 974

*References:*
- [erdosproblems.com/974](https://www.erdosproblems.com/974)
- [Ti66] Tijdeman, R., *On a conjecture of Turán and Erdős*. Indag. Math. (1966), 374-383.
-/

namespace Erdos974

/--
The configuration described by Tijdeman: if `n` is odd then the `z i` are exactly the `n`th roots
of unity, and if `n` is even then they are the vertices of two regular `(n / 2)`-gons with the
same circumscribed circle centred at the origin, that is, the `(n / 2)`th roots of `1` together
with the `(n / 2)`th roots of some other point `c` on the unit circle.
-/
def IsTuranConfiguration {n : ℕ} (z : Fin n → ℂ) : Prop :=
  (Odd n → Set.range z = {ζ : ℂ | ζ ^ n = 1}) ∧
    (Even n → ∃ c : ℂ, ‖c‖ = 1 ∧ c ≠ 1 ∧
      Set.range z = {ζ : ℂ | ζ ^ (n / 2) = 1} ∪ {ζ : ℂ | ζ ^ (n / 2) = c})

/--
Let $z_1,\ldots,z_n\in \mathbb{C}$ be a sequence such that $z_1=1$. Suppose that the sequence of
$$s_k=\sum_{1\leq i\leq n}z_i^k$$
contains infinitely many $(n-1)$-tuples of consecutive values of $s_k$ which are all $0$. Then
(essentially)
$$z_j=e(j/n),$$
where $e(x)=e^{2\pi ix}$.

A conjecture of Turán.

This is true (in the stronger form with only two such tuples) - in fact if $n$ is odd then the
$z_i$ must be exactly the $n$th roots of unity, and if $n$ is even they must be the vertices of
two regular $(n/2)$-gons with the same circumscribed circle centred at the origin. This was first
proved by Tijdeman [Ti66]. An independent proof of this was given in the comments section by Hu,
Tang, and Zhang.
-/
@[category research solved, AMS 11 30, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos974.lean"]
theorem erdos_974 {n : ℕ} [NeZero n] (z : Fin n → ℂ) (hz : z 0 = 1)
    (hs : Set.Infinite {k : ℕ | ∀ j < n - 1, ∑ i, z i ^ (k + j) = 0}) :
    IsTuranConfiguration z := by
  sorry

/--
Erdős speculates that this may be true if there are two distinct $(n-1)$-tuples of consecutive
values of $s_k$ which are $0$. He does not elaborate on what the 'essentially' may mean precisely.

This is true (in the stronger form with only two such tuples) - in fact if $n$ is odd then the
$z_i$ must be exactly the $n$th roots of unity, and if $n$ is even they must be the vertices of
two regular $(n/2)$-gons with the same circumscribed circle centred at the origin. This was first
proved by Tijdeman [Ti66]. An independent proof of this was given in the comments section by Hu,
Tang, and Zhang.
-/
@[category research solved, AMS 11 30]
theorem erdos_974.variants.two_tuples {n : ℕ} [NeZero n] (z : Fin n → ℂ) (hz : z 0 = 1)
    {a b : ℕ} (hab : a ≠ b) (ha : ∀ j < n - 1, ∑ i, z i ^ (a + j) = 0)
    (hb : ∀ j < n - 1, ∑ i, z i ^ (b + j) = 0) :
    IsTuranConfiguration z := by
  sorry

end Erdos974


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
