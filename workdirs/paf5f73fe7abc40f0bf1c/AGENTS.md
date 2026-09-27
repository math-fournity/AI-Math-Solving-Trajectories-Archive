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
# Erdős Problem 351

*Reference:* [erdosproblems.com/351](https://www.erdosproblems.com/351)
-/

open Polynomial

namespace Erdos351

/-- The set of rational numbers of the form `P(n) + 1 / n` where `n` is a natural number
and `P` is a polynomial with rational coefficients.

Note: We include `P 0` in there (since `1 / 0 = 0`), but this doesn't change the validity of the
conjecture -/
def imageSet {α : Type*} [Semifield α] (P : α[X]) : Set α :=
  Set.range (fun (n : ℕ) ↦ P.eval ↑n + 1 / n)

/-- The predicate that a set `A` is strongly complete, i.e. that for every finite set `B`, every sufficiently
large integer is a sum of elements of the set `A \ B`. -/
def IsStronglyComplete {α : Type*} [Semiring α] (A : Set α) : Prop :=
  ∀ B : Finset α,
    ∀ᶠ (m : ℕ) in Filter.atTop,
      ↑m ∈ { ∑ n ∈ X, n | (X : Finset α) (_ : ↑X ⊆ A \ B) }

/-- The predicate that the rational polynomial `P` has a complete image. -/
def HasCompleteImage (P : ℚ[X]) : Prop := IsStronglyComplete (imageSet P)

/--
Let $p(x) \in \mathbb{Q}[x]$ be a non-constant rational polynomial with positive leading
coefficient. Is it true that $$A=\{ p(n)+1/n : n \in \mathbb{N}\}$$ is strongly complete,
in the sense that, for any finite set $B$,
$$\left\{\sum_{a \in X} a : X \subseteq A \setminus B, X \textrm{ is finite}\right\}$$
contains all sufficiently large integers? -/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos351.lean"]
theorem erdos_351 :
    answer(True) ↔ ∀ P : ℚ[X], 0 < P.natDegree → 0 < P.leadingCoeff → HasCompleteImage P := by
  sorry

/--
Let $p(x) = x \in \mathbb{Q}[x]$. It has been shown that
$$A=\{ p(n)+1/n : n \in \mathbb{N}\}$$
is strongly complete, in the sense that, for any finite set $B$,
$$\left\{\sum_{a \in X} a : X \subseteq A \setminus B, X \textrm{ is finite}\right\}$$
contains all sufficiently large integers.
-/
@[category research solved, AMS 11]
protected theorem erdos_351.variants.X : HasCompleteImage X := by
  sorry

/-- Let $p(x) = x ^ 2 \in \mathbb{Q}[x]$. It has been shown that
$$A=\{ p(n)+1/n : n \in \mathbb{N}\}$$
is strongly complete, in the sense that, for any finite set $B$,
$$\left\{\sum_{a \in X} a : X \subseteq A \setminus B, X \textrm{ is finite}\right\}$$
contains all sufficiently large integers. -/
@[category research solved, AMS 11]
theorem erdos_351.variants.X_sq : HasCompleteImage (X ^ 2) := by
  sorry

end Erdos351


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
