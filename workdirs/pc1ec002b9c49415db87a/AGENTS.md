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
# Ben Green's Open Problem 21

*References:*
- [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.21)
- [Ra33] Rado, Richard, *Studien zur Kombinatorik*. Math. Zeit. 36 (1933), 242-280.
- [FoKl06] Fox, Jacob and Kleitman, Daniel, *On Rado's boundedness conjecture*. J. Combin. Theory
  Ser. A 113 (2006), no. 1, 84-100.
- [ElJo23] Ellis, David and Johnson, Robert (editors), *A collection of open problems in
  celebration of Imre Leader's 60th birthday*. arXiv preprint arXiv:2310.18163 (2023).
-/

open Finset

namespace Green21

/--
The coefficients $a_1, \dots, a_k$ satisfy **Rado's condition** if $\sum_{i \in I} a_i = 0$ for
some non-empty $I \subseteq [k]$.

For a single homogeneous equation this is exactly the criterion of Rado's theorem [Ra33]:
$a_1x_1 + \cdots + a_kx_k = 0$ is partition regular if and only if the coefficients satisfy it.
-/
def RadoCondition {k : ℕ} (a : Fin k → ℤ) : Prop :=
  ∃ I : Finset (Fin k), I.Nonempty ∧ ∑ i ∈ I, a i = 0

/--
$c(a_1, \dots, a_k)$, the least number of colours required in order to colour $\mathbb{N}$ so
that there is no monochromatic solution to $a_1x_1 + \cdots + a_kx_k = 0$.

The solutions $x_i$ are required to be *positive*, as in [FoKl06]: were $0$ admitted then
$x_1 = \cdots = x_k = 0$ would be a monochromatic solution for every colouring, and no number of
colours would ever suffice. The $x_i$ are not required to be distinct.

When the coefficients do not satisfy `RadoCondition`, Rado's theorem [Ra33] guarantees that some
finite colouring has no monochromatic solution, so the set below is non-empty and this `sInf` is
a genuine minimum.
-/
noncomputable def minColours {k : ℕ} (a : Fin k → ℤ) : ℕ :=
  sInf {r | ∃ col : ℕ → Fin r, ∀ x : Fin k → ℕ, (∀ i, 0 < x i) →
    (∀ i j, col (x i) = col (x j)) → ∑ i, a i * x i ≠ 0}

/--
Suppose that $a_1, \dots, a_k$ are integers which do not satisfy Rado's condition: thus if
$\sum_{i \in I} a_i = 0$ then $I = \emptyset$. It then follows from Rado's theorem that the
equation $a_1x_1 + \cdots + a_kx_k = 0$ is not partition regular. Write $c(a_1, \dots, a_k)$ for
the least number of colours required in order to colour $\mathbb{N}$ so that there is no
monochromatic solution to $a_1x_1 + \cdots + a_kx_k = 0$. Is $c(a_1, \dots, a_k)$ bounded in
terms of $k$ only?

This problem, which is known as Rado's boundedness conjecture, dates back to 1933 [Ra33]. It is
open for all $k \geq 4$.
-/
@[category research open, AMS 5 11]
theorem green_21 : answer(sorry) ↔ ∃ B : ℕ → ℕ, ∀ (k : ℕ) (a : Fin k → ℤ),
    ¬ RadoCondition a → minColours a ≤ B k := by
  sorry

/--
The answer was shown to be affirmative for $k = 3$ by Fox and Kleitman [FoKl06], who showed that
$c(a_1, a_2, a_3) \leq 24$.
-/
@[category research solved, AMS 5 11]
theorem green_21.variants.fox_kleitman (a : Fin 3 → ℤ) (ha : ¬ RadoCondition a) :
    minColours a ≤ 24 := by
  sorry

/--
Green [Gr24] is not sure that the constant $24$ of [FoKl06] is sharp, and remarks that it might
be interesting to determine the sharp constant.

The largest value of $c(a_1, a_2, a_3)$ is attained, since by `green_21.variants.fox_kleitman`
the values form a non-empty set of naturals bounded above by $24$.
-/
@[category research open, AMS 5 11]
theorem green_21.variants.fox_kleitman_sharp :
    IsGreatest {c | ∃ a : Fin 3 → ℤ, ¬ RadoCondition a ∧ minColours a = c} answer(sorry) := by
  sorry

/--
A question [FoKl06, Conjecture 5] of Fox and Kleitman, which they call a 'modular analogue' of
Rado's Boundedness Conjecture. Let $p$ be a prime, and suppose that $a_1, \dots, a_k$ are
integers with $\sum_{i \in I} a_i \equiv 0 \pmod p$ only when $I = \emptyset$. Does there exist
an $f(k)$-colouring of $(\mathbb{Z}/p\mathbb{Z})^*$ with no monochromatic solution to
$a_1x_1 + \cdots + a_kx_k = 0$? This seems to be open even when $k = 3$; Green [Gr24] suspects
the answer may be negative.

The point of the question is that the number of colours $f(k)$ must not depend on $p$.
-/
@[category research open, AMS 5 11]
theorem green_21.variants.fox_kleitman_modular : answer(sorry) ↔ ∃ f : ℕ → ℕ,
    ∀ (k p : ℕ), p.Prime → ∀ a : Fin k → ℤ,
      (∀ I : Finset (Fin k), (p : ℤ) ∣ ∑ i ∈ I, a i → I = ∅) →
      ∃ col : (ZMod p)ˣ → Fin (f k), ∀ x : Fin k → (ZMod p)ˣ,
        (∀ i j, col (x i) = col (x j)) → ∑ i, (a i : ZMod p) * (x i : ZMod p) ≠ 0 :=

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
