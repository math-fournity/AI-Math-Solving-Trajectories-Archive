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
# Erdős Problem 115

*References:*
- [erdosproblems.com/115](https://www.erdosproblems.com/115)
- [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
  221-254.
- [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
  467-478.
- [ErLe94] Erëmenko, A. and Lempert, L., *An extremal problem for polynomials*. Proc. Amer. Math.
  Soc. (1994), 191-193.
- [Po59a] Pommerenke, Ch., *On the derivative of a polynomial*. Michigan Math. J. (1959), 373-375.
-/

open Filter

namespace Erdos115

/--
If $p(z)$ is a polynomial of degree $n$ such that $\{z : \lvert p(z)\rvert\leq 1\}$ is connected
then is it true that
$$\max_{\substack{z\in\mathbb{C}\\ \lvert p(z)\rvert\leq 1}} \lvert p'(z)\rvert
\leq (\tfrac{1}{2}+o(1))n^2?$$

Eremenko and Lempert [ErLe94] have shown this is true, and in fact Chebyshev polynomials are the
extreme examples.
-/
@[category research solved, AMS 30, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos115.lean"]
theorem erdos_115 : answer(True) ↔
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ p : Polynomial ℂ, p.Monic → p.natDegree = n →
      IsConnected {z : ℂ | ‖p.eval z‖ ≤ 1} → ∀ z : ℂ, ‖p.eval z‖ ≤ 1 →
        ‖p.derivative.eval z‖ ≤ (1 / 2 + ε) * (n : ℝ) ^ 2 := by
  sorry

end Erdos115


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
