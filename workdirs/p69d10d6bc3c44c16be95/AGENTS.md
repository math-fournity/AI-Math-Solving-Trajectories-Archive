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
# Erdős Problem 512

*References:*
- [erdosproblems.com/512](https://www.erdosproblems.com/512)
- [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl.
  (1961), 221-254.
- [Ko81] Konyagin, S. V., *On the Littlewood problem*. Izv. Akad. Nauk SSSR Ser. Mat. (1981),
  243-265, 463.
- [MPS81] McGehee, O. Carruth and Pigno, Louis and Smith, Brent, *Hardy's inequality and the
  $L^1$ norm of exponential sums*. Ann. of Math. (2) (1981), 613-618.
-/

open scoped ExponentialSum

namespace Erdos512

/--
Is it true that, if $A\subset \mathbb{Z}$ is a finite set of size $N$, then
$$\int_0^1 \left\lvert \sum_{n\in A}e(n\theta)\right\rvert \mathrm{d}\theta \gg \log N,$$
where $e(x)=e^{2\pi ix }$?

Littlewood's conjecture, proved independently by Konyagin [Ko81] and McGehee, Pigno, and
Smith [MPS81].
-/
@[category research solved, AMS 11 42, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/512/Erdos512.lean"]
theorem erdos_512 : answer(True) ↔
    ∃ c > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℤ), A.card = N →
      c * Real.log N ≤ ∫ θ in (0 : ℝ)..1, ‖∑ n ∈ A, e (n * θ)‖ := by
  sorry

end Erdos512


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
