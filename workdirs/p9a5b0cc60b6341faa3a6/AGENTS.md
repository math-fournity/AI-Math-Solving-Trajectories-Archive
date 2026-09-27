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
# Congruent Number

A natural number $n$ is called a congruent number if there exists a right triangle with rational
sides $a$, $b$, and hypotenuse $c$ such that the area of the triangle is $\frac{1}{2}ab = n$.

*References:*
- [Wikipedia (Congruent number)](https://en.wikipedia.org/wiki/Congruent_number)
- [Wikipedia (Tunnell's theorem)](https://en.wikipedia.org/wiki/Tunnell%27s_theorem)
- [Keith Conrad's note](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/congnumber.pdf)
-/

namespace CongruentNumber

def congruentNumber (n : ℕ) : Prop :=
  ∃ (a b c : ℚ), a ^ 2 + b ^ 2 = c ^ 2 ∧ n = (2⁻¹ : ℚ) * a * b

/-- 1 is not a congruent number, as proved by Fermat via infinite descent. -/
@[category textbook, AMS 11]
theorem not_congruentNumber_1 : ¬ congruentNumber 1 := by
  sorry

/--
The rational right triangle with side lengths $\frac{3}{2}$, $\frac{20}{3}$, and
$\frac{41}{6}$ witnesses that $5$ is a congruent number.
-/
@[category test, AMS 11]
theorem congruentNumber_5 : congruentNumber 5 := by
  use 3 / 2, 20 / 3, 41 / 6
  norm_num

/--
The $3$-$4$-$5$ right triangle witnesses that $6$ is a congruent number.
-/
@[category test, AMS 11]
theorem congruentNumber_6 : congruentNumber 6 := by
  use 3, 4, 5
  norm_num

/--
The rational right triangle with side lengths $\frac{35}{12}$, $\frac{24}{5}$, and
$\frac{337}{60}$ witnesses that $7$ is a congruent number.
-/
@[category test, AMS 11]
theorem congruentNumber_7 : congruentNumber 7 := by
  use 35 / 12, 24 / 5, 337 / 60
  norm_num

/--
Zagier's rational right triangle witnesses that $157$ is a congruent number.
-/
@[category test, AMS 11]
theorem congruentNumber_157_zagier : congruentNumber 157 := by
  use 411340519227716149383203 / 21666555693714761309610,
    6803298487826435051217540 / 411340519227716149383203,
    224403517704336969924557513090674863160948472041 /
      8912332268928859588025535178967163570016480830
  norm_num
/-
Tunnell's theorem:
Let $A_n$, $B_n$, $C_n$, and $D_n$ be the sets defined as follows:
- $A_n = \{(x, y, z) \in \mathbb{Z}^3 : n = 2x^2 + y^2 + 32z^2\}$
- $B_n = \{(x, y, z) \in \mathbb{Z}^3 : n = 2x^2 + y^2 + 8z^2\}$
- $C_n = \{(x, y, z) \in \mathbb{Z}^3 : n = 8x^2 + 2y^2 + 64z^2\}$
- $D_n = \{(x, y, z) \in \mathbb{Z}^3 : n = 8x^2 + 2y^2 + 16z^2\}$

If $n$ is a squarefree congruent number, then:
- If $n$ is odd, then $2 |A_n| = |B_n|$.
- If $n$ is even, then $2 |C_n| = |D_n|$.

Converse is true under the BSD conjecture.
-/

def A (n : ℕ) : Set (ℤ × ℤ × ℤ) := {(x, y, z) | n = 2 * x ^ 2 + y ^ 2 + 32 * z ^ 2}
def B (n : ℕ) : Set (ℤ × ℤ × ℤ) := {(x, y, z) | n = 2 * x ^ 2 + y ^ 2 + 8 * z ^ 2}
def C (n : ℕ) : Set (ℤ × ℤ × ℤ) := {(x, y, z) | n = 8 * x ^ 2 + 2 * y ^ 2 + 64 * z ^ 2}
def D (n : ℕ) : Set (ℤ × ℤ × ℤ) := {(x, y, z) | n = 8 * x ^ 2 + 2 * y ^ 2 + 16 * z ^ 2}

/-  Tunnell's theorem. -/

/-- Tunnell's theorem (necessary condition) for odd squarefree congruent numbers. -/
@[category research solved, AMS 11]
theorem Tunnell_odd (n : ℕ) (hsqf : Squarefree n) (hodd : Odd n) :
    congruentNumber n → 2 * (A n).ncard = (B n).ncard := by
  sorry

/-- Tunnell's theorem (necessary condition) for even squarefree congruent numbers. -/
@[category research solved, AMS 11]
theorem Tunnell_even (n : ℕ) (hsqf : Squarefree n) (heven : Even n) :
    congruentNumber n → 2 * (C n).ncard = (D n).ncard := by
  sorry

/-  Converse of Tunnell's theorem. -/

/-- Tunnell's theorem (sufficient condition assuming BSD) for odd squarefree congruent numbers. -/
@[category research open, AMS 11]
theorem Tunnell_odd_converse (n : ℕ) (hsqf : Squarefree n) (hodd : Odd n) :
    2 * (A n).ncard = (B n).ncard → congruentNumber n := by
  sorry

/-- Tunnell's theorem (sufficient condition assuming BSD) for even squarefree congruent numbers. -/
@[category research open, AMS 11]
theorem Tunnell_even_converse (n : ℕ) (hsqf : Squarefree n) (heven : Even n) :
    2 * (C n).ncard = (D n).ncard → congruentNumber n := by
  sorry

end CongruentNumber


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
