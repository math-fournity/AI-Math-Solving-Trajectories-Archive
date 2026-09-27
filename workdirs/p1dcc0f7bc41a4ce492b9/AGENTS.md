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
# Erdős Problem 434

*References:*
- [erdosproblems.com/434](https://www.erdosproblems.com/434)
- [Ki02] Kiss, G., On the extremal Frobenius problem in a new aspect. Ann. Univ. Sci.
  Budapest. Eötvös Sect. Math. (2002), 139–142.
-/

namespace Erdos434

open Erdos434 Finset

/--
A natural $n$ is representable as a set $A$ if it can be
written as the sum of finitely many elements of $A$
(with repetition allowed).
-/
abbrev Nat.IsRepresentableAs (n : ℕ) (A : Set ℕ) :=
    ∃ (S : Multiset ℕ), (∀ a ∈ S, a ∈ A) ∧ S.sum = n

/--
The number of naturals that cannot be written as the sum of
finitely many elements of the set $A$, with repetition allowed.
-/
noncomputable abbrev Nat.NcardUnrepresentable (A : Set ℕ) :=
    { n : ℕ | ¬n.IsRepresentableAs A }.ncard

/--
Let $k \le n$. What choice of $A\subseteq\{1, \dots, n\}$ (with $\text{gcd}(A) = 1$) of size $|A| = k$
maximises the number of integers not representable as the sum of finitely
many elements from $A$ (with repetitions allowed)?
Is it $\{n, n - 1, \dots, n - k + 1\}$?

The maximal choice is indeed $\{n, \dots, n - k + 1\}$, as proved by Kiss [Ki02].

The Lean theorem assumes $2 \le k$. When $k = 1 < n$, the proposed singleton $\{n\}$ does not
have gcd $1$; the gcd condition instead forces the unique admissible choice $A = \{1\}$.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://www.erdosproblems.com/forum/thread/434#post-4437"]
theorem erdos_434.parts.i (n k : ℕ) (hn : 1 ≤ n) (hk : 2 ≤ k) (h : k ≤ n) :
    IsGreatest
      { Nat.NcardUnrepresentable S | (S : Finset ℕ) (_ : S ⊆ Finset.Icc 1 n)
        (_ : #S = k) (_ : S.gcd id = 1) }
      (Nat.NcardUnrepresentable <| answer(Set.Icc (n - k + 1 : ℕ) n)) := by
  sorry

/--
For $2 \le k \le n$, the interval $A = \{n, n - 1, \dots, n - k + 1\}$ maximises the number
of integers not representable as the sum of finitely many elements from $A$ (with repetitions
allowed), as proved by Kiss [Ki02].
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://www.erdosproblems.com/forum/thread/434#post-4437"]
theorem erdos_434.parts.ii : answer(True) ↔ ∀ᵉ (n ≥ 1) (k ≥ 2), k ≤ n →
    IsGreatest
      { Nat.NcardUnrepresentable S | (S : Finset ℕ) (_ : S ⊆ Finset.Icc 1 n)
        (_ : #S = k) (_ : S.gcd id = 1)}
      (Nat.NcardUnrepresentable <| Set.Icc (n - k + 1 : ℕ) n) := by
  sorry

end Erdos434


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
