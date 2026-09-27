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
# Dickson's conjecture

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Dickson%27s_conjecture)
- [PrimePages glossary](https://t5k.org/glossary/xpage/DicksonsConjecture.html)
- [OEIS Wiki](https://oeis.org/wiki/Dickson%27s_conjecture)
- [MathWorld](https://mathworld.wolfram.com/DicksonsConjecture.html)
- [Leonard Eugene Dickson, *History of the Theory of Numbers, Vol. I: Divisibility and Primality*](https://archive.org/details/historyoftheoryo01dickuoft)
- [Arxiv](https://arxiv.org/pdf/0906.3850)
-/
open Polynomial
namespace Dickson

/--
**Dickson's conjecture**
If a finite set of linear integer forms $f_i(n) = a_i n+b_i$ satisfies Schinzel condition,
there exist infinitely many natural numbers $m$ such that $f_i(m)$ are primes for all $i$.
-/
@[category research open, AMS 11]
theorem dickson_conjecture (fs : Finset ℤ[X]) (hfs : ∀ f ∈ fs, f.degree = 1 ∧ BunyakovskyCondition f)
    (hfs' : SchinzelCondition fs) : Infinite {n : ℕ | ∀ f ∈ fs, (f.eval (n : ℤ)).natAbs.Prime} := by
  sorry

/-  ## Special cases -/

/--
**Polignac's conjecture**
For any integer $k$ there are infinitely many primes $p$ such that $p + 2k$ is prime.
-/
@[category research open, AMS 11]
theorem polignac_conjecture (k : ℕ) :
    Infinite {p : ℕ | p.Prime ∧ (p + 2 * k).Prime} := by
  sorry

/--
**The infinitude of Sophie Germain primes**
There are infinitely many primes $p$ such that $2p + 1$ is prime.
-/
@[category research open, AMS 11]
theorem infinite_safe_primes :
    Infinite {p : ℕ | Prime p ∧ Prime (2 * p + 1)} := by
  sorry

/--
**The infinitude of cousin primes**
There are infinitely many primes $p$ such that $p + 4$ is prime.
-/
@[category research open, AMS 11]
theorem infinite_cousin_primes :
    Infinite {p : ℕ | Prime p ∧ Prime (p + 4)} := by
  sorry

/--
**The infinitude of sexy primes**
There are infinitely many primes $p$ such that $p + 6$ is prime.
-/
@[category research open, AMS 11]
theorem infinite_sexy_primes :
    Infinite {p : ℕ | Prime p ∧ Prime (p + 6)} := by
  sorry

/-
## Other consequences
- Landau's fourth problem (primes and perfect squares)
- Twin prime conjecture
- Artin's primitive root conjecture
- First Hardy–Littlewood conjecture

*Reference:* [Arxiv](https://arxiv.org/pdf/0906.3850)
-/

end Dickson


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
