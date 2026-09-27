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
# Erdős Problem 756

*References:*
- [erdosproblems.com/756](https://www.erdosproblems.com/756)
- [Bh24] Bhowmick, K., *A problem of Erdős about rich distances*. arXiv:2407.01174 (2024).
- [CDL25] Clemen, F., Dumitrescu, A. and Liu, D., *On multiplicities of interpoint distances*.
  arXiv:2505.04283 (2025).
- [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*.
  Discrete Math. (1997), 227-231.
- [ErPa90] Erdős, P. and Pach, J., *Variations on the theme of repeated distances*.
  Combinatorica (1990), 261-269.
- [HoPa34] Hopf, H. and Pannwitz, E., *Aufgabe 167*. Jber. Deutsch. Math. Verein. (1934), 114.
-/

open Filter
open scoped EuclideanGeometry Asymptotics

namespace Erdos756

/-- The number of unordered pairs of distinct points of `A` which are at distance exactly `d`.
The division by two accounts for `Finset.offDiag` listing each unordered pair twice. -/
noncomputable def distanceMultiplicity (A : Finset ℝ²) (d : ℝ) : ℕ :=
  (A.offDiag.filter fun pair : ℝ² × ℝ² => dist pair.1 pair.2 = d).card / 2

/-- The distances determined by `A` which occur for at least `k` many pairs of points of `A`. -/
noncomputable def richDistances (A : Finset ℝ²) (k : ℕ) : Finset ℝ :=
  (A.offDiag.image fun pair : ℝ² × ℝ² => dist pair.1 pair.2).filter
    fun d => k ≤ distanceMultiplicity A d

/-- The largest number of distinct distances that a set of `n` points in $\mathbb{R}^2$ can
determine, each of which occurs for more than `n` many pairs of points of the set. -/
noncomputable def maxRichDistances (n : ℕ) : ℕ :=
  sSup {(richDistances A (n + 1)).card | (A : Finset ℝ²) (_ : A.card = n)}

/--
Let $A\subset \mathbb{R}^2$ be a set of $n$ points. Can there be $\gg n$ many distinct distances
each of which occurs for more than $n$ many pairs from $A$?

The answer is yes: Bhowmick [Bh24] constructs a set of $n$ points in $\mathbb{R}^2$ such that
$\lfloor\frac{n}{4}\rfloor$ distances occur at least $n+1$ times.
-/
@[category research solved, AMS 52]
theorem erdos_756 : answer(True) ↔
    (fun n : ℕ => (n : ℝ)) =O[atTop] (fun n : ℕ => (maxRichDistances n : ℝ)) := by
  sorry

/--
Bhowmick [Bh24] constructs a set of $n$ points in $\mathbb{R}^2$ such that
$\lfloor\frac{n}{4}\rfloor$ distances occur at least $n+1$ times.
-/
@[category research solved, AMS 52, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos756.lean"]
theorem erdos_756.variants.bhowmick (n : ℕ) :
    ∃ A : Finset ℝ², A.card = n ∧ n / 4 ≤ (richDistances A (n + 1)).card := by
  sorry

/--
More generally, they construct, for any $m$ and large $n$, a set of $n$ points such that
$\lfloor \frac{n}{2(m+1)}\rfloor$ distances occur at least $n+m$ times.
-/
@[category research solved, AMS 52]
theorem erdos_756.variants.bhowmick_general (m : ℕ) :
    ∀ᶠ n : ℕ in atTop, ∃ A : Finset ℝ², A.card = n ∧
      n / (2 * (m + 1)) ≤ (richDistances A (n + m)).card := by
  sorry

end Erdos756


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
