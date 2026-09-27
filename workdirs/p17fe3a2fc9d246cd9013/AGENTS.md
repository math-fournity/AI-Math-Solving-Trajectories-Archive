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
# The Erdős–Moser equation

For positive integers $k$ and $m$, let

$$S_k(m)=1^k+2^k+\cdots+(m-1)^k.$$

The Erdős–Moser conjecture says that $S_k(m)=m^k$ has only the solution
$(k,m)=(1,3)$.

*References:*
* [Wikipedia: Erdős–Moser equation](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Moser_equation)
* B. C. Kellner,
  [On stronger conjectures that imply the Erdős–Moser conjecture](https://arxiv.org/abs/1003.1646)
-/

namespace ErdosMoser

/-- The power sum $S_k(m)=\sum_{i=1}^{m-1} i^k$. -/
def powerSum (k m : ℕ) : ℕ :=
  ∑ i ∈ Finset.Ico 1 m, i ^ k

/-- The only positive solution of $S_k(m)=m^k$ is $(k,m)=(1,3)$. -/
@[category research open, AMS 11]
theorem erdos_moser_conjecture :
    ∀ k m : ℕ, 0 < k → 0 < m → powerSum k m = m ^ k → k = 1 ∧ m = 3 := by
  sorry

/-- The pair $(1,3)$ is the trivial solution of the Erdős–Moser equation. -/
@[category test, AMS 11]
theorem powerSum_one_three : powerSum 1 3 = 3 ^ 1 := by
  decide

/-- For $k=2$ and $m=3$, the left side is $1^2+2^2=5$, not $3^2$. -/
@[category test, AMS 11]
theorem powerSum_two_three : powerSum 2 3 = 5 ∧ powerSum 2 3 ≠ 3 ^ 2 := by
  decide

/-- Zero is a solution for every positive exponent, so the conjecture must require $m>0$. -/
@[category test, AMS 11]
theorem powerSum_zero (k : ℕ) (hk : 0 < k) : powerSum k 0 = 0 ^ k := by
  simp [powerSum, Nat.zero_pow hk]

end ErdosMoser


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
