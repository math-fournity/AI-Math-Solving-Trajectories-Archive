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
# Erdős Problem 498

*References:*
- [erdosproblems.com/498](https://www.erdosproblems.com/498)
- [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
  221-254.
- [Er45] Erdős, P., _On a lemma of Littlewood and Offord_. Bull. Amer. Math. Soc. (1945), 898-902.
- [Kl65] Kleitman, Daniel J., _On a lemma of Littlewood and Offord on the distribution of certain
  sums_. Math. Z. (1965), 251-259.
- [Kl70] Kleitman, Daniel J., _On a lemma of Littlewood and Offord on the distributions of linear
  combinations of vectors_. Advances in Math. (1970), 155-157.
-/

namespace Erdos498

/--
Let $z_1,\ldots,z_n\in\mathbb{C}$ with $1\leq \lvert z_i\rvert$ for $1\leq i\leq n$. Let $D$ be an
arbitrary disc of radius $1$. Is it true that the number of sums of the shape
$$\sum_{i=1}^n\epsilon_iz_i \textrm{ for }\epsilon_i\in \{-1,1\}$$
which lie in $D$ is at most $\binom{n}{\lfloor n/2\rfloor}$?

A strong form of the Littlewood-Offord problem. Erdős [Er45] proved this is true if
$z_i\in\mathbb{R}$, and for general $z_i\in\mathbb{C}$ proved a weaker upper bound of
$$\ll \frac{2^n}{\sqrt{n}}.$$
This was solved in the affirmative by Kleitman [Kl65], who also later generalised this to
arbitrary Hilbert spaces [Kl70].

See also [395].
-/
@[category research solved, AMS 5]
theorem erdos_498 : answer(True) ↔
    ∀ (n : ℕ) (z : Fin n → ℂ), (∀ i, 1 ≤ ‖z i‖) → ∀ c : ℂ,
      {ε : Fin n → ℤ | (∀ i, ε i = -1 ∨ ε i = 1) ∧
        (∑ i, (ε i : ℂ) * z i) ∈ Metric.ball c 1}.ncard ≤ n.choose (n / 2) := by
  sorry

end Erdos498


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
