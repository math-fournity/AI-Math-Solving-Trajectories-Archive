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
# Suffix-prefix avoidance bound

Let $A$ and $B$ be sets of words of length $n$ over an alphabet with $q$ letters. If no
(nonempty) suffix of any word in $A$ coincides with a prefix of any word in $B$, then
$$|A| \cdot |B| \leq \frac{q^{2n}}{en}.$$

*References:*
- [X post by Dmitry Rybin](https://x.com/DmitryRybin1/status/2027278135847428577)
- [Maximal sets of strings with no prefix-suffix overlap]
  (https://mathoverflow.net/questions/508648/maximal-sets-of-strings-with-no-prefix-suffix-overlap)
  by *Dmitry Rybin*, MathOverflow (2026)
- [An isoperimetric inequality for word overlap](https://arxiv.org/abs/2602.20143)
  by *Dmitrii Zakharov* (2026)
-/

open Finset Real

namespace SuffixPrefixAvoidance

variable {n q : ℕ}

/-- The suffix of a word `w : Fin n → Fin q` of length `k + 1` (the last `k + 1` characters). -/
def wordSuffix (w : Fin n → Fin q) (k : Fin n) : Fin (k + 1) → Fin q :=
  fun i => w ⟨n - k - 1 + i, by omega⟩

/-- The prefix of a word `w : Fin n → Fin q` of length `k + 1` (the first `k + 1` characters). -/
def wordPrefix (w : Fin n → Fin q) (k : Fin n) : Fin (k + 1) → Fin q :=
  fun i => w ⟨i, by omega⟩

/-- Two sets of words $A, B$ over `Fin q` of length `n` are suffix-prefix avoiding if no
nonempty suffix of any word in $A$ equals any prefix of any word in $B$ of the same length. -/
def IsSuffixPrefixAvoiding (A B : Finset (Fin n → Fin q)) : Prop :=
  ∀ a ∈ A, ∀ b ∈ B, ∀ k : Fin n, wordSuffix a k ≠ wordPrefix b k

/--
$A$ and $B$ are sets of words of length $n$ over alphabet with $q$ letters.
Trivially then $|A| \cdot |B|$ is at most $q^{2n}$.
-/
@[category test, AMS 5]
theorem words_naive_bound
    (A B : Finset (Fin n → Fin q)) :
    A.card * B.card ≤ q ^ (2 * n) := by
  simp [Nat.mul_le_mul, two_mul, pow_add, (Finset.card_le_univ _).trans_eq]

/--
$A$ and $B$ are sets of words of length $n$ over alphabet with $q \geq 1$ letters.
No suffix of a word in $A$ coincides with a prefix of a word in $B$.
Then $|A| \cdot |B|$ is at most $\frac{q^{2n}}{en}$.

This problem is from *Maximal sets of strings with no prefix-suffix overlap* and was proved in
*An isoperimetric inequality for word overlap*.
-/
@[category research solved, AMS 5]
theorem suffix_prefix_avoidance_bound
    (A B : Finset (Fin n → Fin q))
    (hq : 0 < q) (hn : 0 < n)
    (h : IsSuffixPrefixAvoiding A B) :
    (A.card : ℝ) * B.card ≤ (q : ℝ) ^ (2 * n) / (exp 1 * n) := by
  sorry

/--
$A$ and $B$ are sets of words of length $n$ over alphabet with $q \geq 1$ letters.
No suffix of a word in $A$ coincides with a prefix of a word in $B$.
Then $|A| \cdot |B|$ is at most $\frac{q^{2n}}{n}$.
-/
@[category research solved, AMS 5,
  formal_proof using formal_conjectures at "https://github.com/google-deepmind/formal-conjectures/blob/102e47fee802d461946e3a4e0b47fdbe7db4c1ed/FormalConjectures/Other/SuffixPrefixAvoidance.lean#L157"]
theorem suffix_prefix_avoidance_weaker_bound
    (A B : Finset (Fin n → Fin q))
    (_hq : 0 < q) (hn : 0 < n)
    (h : IsSuffixPrefixAvoiding A B) :
    (A.card : ℚ) * B.card ≤ (q : ℚ) ^ (2 * n) / n := by
  sorry

end SuffixPrefixAvoidance


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
