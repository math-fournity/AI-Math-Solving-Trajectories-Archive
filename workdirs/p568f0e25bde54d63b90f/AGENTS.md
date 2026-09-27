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
# Agrawal's conjecture

Agrawal's conjecture is a stronger version of the theorem that forms the basis
of the AKS primality test. If true, it would significantly improve the
efficiency of primality testing.

The conjecture states that for coprime $n$ and $r$, if the polynomial congruence
$(X-1)^n \equiv X^n-1 \pmod{n, X^r-1}$ holds, then $n$ is either prime or $n^2 \equiv 1 \pmod{r}$.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Agrawal%27s_conjecture)
- [AIM Math](https://aimath.org/WWN/primesinp/articles/html/50a/)
- [Paper](https://eprint.iacr.org/2009/008.pdf)
-/

open Polynomial

namespace AgrawalConjecture

/--
**Agrawal's Primality Conjecture.**

Does the congruence $(X-1)^n \equiv X^n - 1 \pmod{n, X^r-1}$ imply
$n$ is prime (with a specific exception for $n^2 \equiv 1 \pmod{r}$)?

While the "if" direction is a known theorem, the "only if" direction
remains a conjecture.
-/
@[category research open, AMS 11]
theorem agrawal_conjecture :
  answer(sorry) ↔
    ∀ (n r : ℕ), n > 1 → r > 0 → n.gcd r = 1 →
      let R := Polynomial (ZMod n)
      let X : R := Polynomial.X
      let I : Ideal R := Ideal.span ({X^r - 1} : Set R)
      Ideal.Quotient.mk I ((X - 1)^n) = Ideal.Quotient.mk I (X^n - 1) →
      (n.Prime ∨ (n^2 : ZMod r) = 1) := by
  sorry

/--
**Roman B. Popovych Conjecture.**
A stronger version of Agrawal's conjecture, which also considers the congruence
$(X+2)^n \equiv X^n + 2 \pmod{n, X^r-1}$.
If both congruences hold, then $n$ is either prime or $n^2 \equiv 1 \pmod{r}$.
This variant was proposed by Roman B. Popovych in 2018.
-/
@[category research open, AMS 11]
theorem agrawal_conjecture.variants.popovych :
  ∀ (n r : ℕ), n > 1 → r > 0 → n.gcd r = 1 →
    let R := Polynomial (ZMod n)
    let X : R := Polynomial.X
    let I : Ideal R := Ideal.span ({X^r - 1} : Set R)
    Ideal.Quotient.mk I ((X - 1)^n) = Ideal.Quotient.mk I (X^n - 1) →
    Ideal.Quotient.mk I ((X + 2)^n) = Ideal.Quotient.mk I (X^n + 2) →
    (n.Prime ∨ (n^2 : ZMod r) = 1) := by
  sorry

end AgrawalConjecture


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
