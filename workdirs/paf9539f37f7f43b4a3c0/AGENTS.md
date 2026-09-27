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
# Erdős Problem 821

*References:*
- [erdosproblems.com/821](https://www.erdosproblems.com/821)
- [BaHa98] Baker, R. C. and Harman, G., Shifted primes without large prime factors. Acta Arith.
  (1998), 331--361.
- [Er35b] Erdős, P., On the normal number of prime factors of $p-1$ and some related problems
  concerning Euler's $\varphi$-function. Quart. J. Math. (1935), 205-213.
- [Er74b] Erdős, P., Remarks on some problems in number theory. Math. Balkanica (1974), 197-202.
- [Li22] J. D. Lichtman, Primes in arithmetic progressions to large moduli and shifted primes
  without large prime factors. arXiv:2211.09641 (2022).
- [LuPo11] Luca, Florian and Pollack, Paul, An arithmetic function arising from {C}armichael's
  conjecture. J. Théor. Nombres Bordeaux (2011), 697--714.
-/

open Nat Filter

namespace Erdos821

/--
Let $g(n)$ count the number of $m$ such that $\phi(m)=n$.
-/
noncomputable def g (n : ℕ) : ℕ :=
  { m : ℕ | totient m = n }.ncard

/--
Is it true that, for every $\epsilon>0$, there exist infinitely many $n$ such that
$g(n) > n^{1-\epsilon}$?
-/
@[category research open, AMS 11]
theorem erdos_821 :
    answer(sorry) ↔ ∀ ε > (0 : ℝ), { n : ℕ | (g n : ℝ) > (n : ℝ) ^ (1 - ε) }.Infinite := by
  sorry

/--
Pillai proved that $\limsup g(n)=\infty$.
-/
@[category research solved, AMS 11]
theorem erdos_821.variants.pillai :
    atTop.limsup (fun n : ℕ ↦ (g n : EReal)) = ⊤ := by
  sorry

/--
Erdős [Er35b] proved that there exists some constant $c>0$ such that $g(n) > n^c$ for infinitely
many $n$.
-/
@[category research solved, AMS 11]
theorem erdos_821.variants.erdos :
    ∃ c > (0 : ℝ), { n : ℕ | (n : ℝ) ^ c < (g n : ℝ) }.Infinite := by
  sorry

/--
The best known bound is that there are infinitely many $n$ such that $g(n) > n^{0.71568\cdots}$,
obtained by Lichtman [Li22] as a consequence of proving that there are
$\geq \frac{x}{(\log x)^{O(1)}}$ many primes $p\leq x$ such that all prime factors of $p-1$ are
$\leq x^{0.2843\cdots}$ (which improves a number of previous exponents, most recently Baker and
Harman [BaHa98]).
-/
@[category research solved, AMS 11]
theorem erdos_821.variants.lichtman :
    ∃ c > (0.71568 : ℝ), { n : ℕ | (n : ℝ) ^ c < (g n : ℝ) }.Infinite := by
  sorry

end Erdos821


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
