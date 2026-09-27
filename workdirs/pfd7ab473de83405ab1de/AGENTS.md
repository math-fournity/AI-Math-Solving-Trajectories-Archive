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
# Erdős Problem 519

*References:*
- [erdosproblems.com/519](https://www.erdosproblems.com/519)
- [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
  221-254.
- [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
  Modern Mathematics, Vol. III (1965), 196-244.
- [Bi94] Biró, A., *On a problem of Turán concerning sums of powers of complex numbers*. Acta Math.
  Hungar. (1994), 209-216.
- [Bi00] Biró, András, *An improved estimate in a power sum problem of Turán*. Indag. Math. (N.S.)
  (2000), 343-358.
- [Bi00b] Biró, A., *An upper estimate in Turán's pure power sum problem*. Indag. Math. (N.S.)
  (2000), 499--508.
- [At61b] Atkinson, F. V., *On sums of powers of complex numbers*. Acta Math. Acad.
  Sci. Hungar. (1961), 185-188.
-/

open scoped BigOperators

namespace Erdos519

/-- The $k$th power sum of a finite sequence of complex numbers. -/
noncomputable def powerSum {n : ℕ} (z : Fin n → ℂ) (k : ℕ) : ℂ :=
  ∑ i : Fin n, z i ^ k

/--
Let $z_1,\ldots,z_n\in \mathbb{C}$ with $z_1=1$. Must there exist an absolute constant $c>0$ such
that
$$
\max_{1\leq k\leq n}\left\lvert \sum_{i}z_i^k\right\rvert>c?
$$

Atkinson proved that $c=1/6$ suffices.
-/
@[category research solved, AMS 30, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos519.lean"]
theorem erdos_519 : answer(True) ↔
    ∃ c : ℝ, 0 < c ∧
      ∀ (n : ℕ) (hn : 0 < n) (z : Fin n → ℂ),
        z ⟨0, hn⟩ = 1 →
          ∃ k : Fin n, c < ‖powerSum z (k.val + 1)‖ := by
  sorry

end Erdos519


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
