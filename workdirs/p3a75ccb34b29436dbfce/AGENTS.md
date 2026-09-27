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
# Erdős Problem 369

*References:*
- [erdosproblems.com/369](https://www.erdosproblems.com/369)
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
  theory*. Monographies de L'Enseignement Mathematique (1980).
- [EgSe76] Eggleton, R. B. and Selfridge, J. L., *Consecutive integers with no large prime factors*.
  J. Austral. Math. Soc. Ser. A (1976), 1--11.
- [BFMW20] Bober, J. W. and Fretwell, D. and Martin, G. and Wooley, T. D., *Smooth values of
  polynomials*. J. Aust. Math. Soc. (2020), 245--261.
- [BaWo98] Balog, Antal and Wooley, Trevor D., *On strings of consecutive integers with no large
  prime factors*. J. Austral. Math. Soc. Ser. A (1998), 266-276.
-/

open Filter

namespace Erdos369

/--
Let $\epsilon>0$ and $k\geq 2$. Is it true that, for all sufficiently large $n$, there is a
sequence of $k$ consecutive integers in $\{1,\ldots,n\}$ all of which are $n^\epsilon$-smooth?

The problem is trivially true as written (simply taking $\{1,\ldots,k\}$ and $n>k^{1/\epsilon}$).
There are (at least) two possible variants which are non-trivial, and it is not clear which
Erdős and Graham meant. We formalize the second: each $m\in P$ (where $P$ is the sequence of $k$
consecutive integers sought for) must be in $[n/2,n]$. In this case a positive answer also
follows directly from the result of Balog and Wooley [BaWo98] for infinitely many $n$. Proving
this is true for all large $n$ does not follow immediately from [BaWo98], but can be deduced
using a similar construction, as shown by SkyYang.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos369.lean"]
theorem erdos_369 : answer(True) ↔
    ∀ (ε : ℝ) (hε : 0 < ε) (k : ℕ) (hk : 2 ≤ k),
      ∀ᶠ (n : ℕ) in atTop, ∃ a : ℕ, n / 2 ≤ a + 1 ∧ a + k ≤ n ∧
        ∀ j < k, ∀ p ∈ (a + 1 + j).primeFactors, (p : ℝ) ≤ (n : ℝ) ^ ε := by
  sorry

end Erdos369


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
