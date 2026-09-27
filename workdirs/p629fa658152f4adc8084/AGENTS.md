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
# Komlós conjecture

The Komlós conjecture in discrepancy theory: there is a universal constant $K$ such
that for all $n, m$ and all vectors $v_1, \dots, v_n \in \mathbb{R}^m$ with
$\|v_i\|_2 \le 1$, there exist signs $\varepsilon_i \in \{-1, +1\}$ such that
$$\left\|\sum_{i=1}^n \varepsilon_i v_i\right\|_\infty \le K.$$

The best known bound is due to Banaszczyk, who proved that one can always achieve
$O(\sqrt{\log n})$. The Beck–Fiala theorem on the discrepancy of sparse set systems
is a special case (up to scaling), and the conjecture would imply the Beck–Fiala
conjecture that set systems of degree $t$ have discrepancy $O(\sqrt{t})$.

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Discrepancy_theory#Major_open_problems)
- [W. Banaszczyk, *Balancing vectors and Gaussian measures of n-dimensional convex bodies*,
  Random Structures & Algorithms **12** (1998), 351–360](https://doi.org/10.1002/(SICI)1098-2418(199807)12:4%3C351::AID-RSA3%3E3.0.CO;2-S)
- [J. Spencer, *Six standard deviations suffice*,
  Trans. Amer. Math. Soc. **289** (1985), 679–706](https://doi.org/10.1090/S0002-9947-1985-0784009-0)
-/

namespace KomlosConjecture

/--
**The Komlós conjecture**

There exists a universal constant $K > 0$ such that for all $n, m \in \mathbb{N}$ and
all vectors $v_1, \dots, v_n \in \mathbb{R}^m$ with $\|v_i\|_2 \le 1$ (encoded here as
$\sum_j v_{ij}^2 \le 1$), there exist signs $\varepsilon_i \in \{-1, +1\}$ such that
$\left\|\sum_i \varepsilon_i v_i\right\|_\infty \le K$, i.e.
$\left|\sum_i \varepsilon_i v_{ij}\right| \le K$ for every coordinate $j$.
-/
@[category research open, AMS 5]
theorem komlos_conjecture :
    ∃ K : ℝ, 0 < K ∧ ∀ (n m : ℕ) (v : Fin n → Fin m → ℝ),
      (∀ i, ∑ j, (v i j) ^ 2 ≤ 1) →
      ∃ ε : Fin n → ℝ, (∀ i, ε i = 1 ∨ ε i = -1) ∧
        ∀ j, |∑ i, ε i * v i j| ≤ K := by
  sorry

/--
**Banaszczyk's theorem**

There exists a constant $C > 0$ such that for all $n, m \in \mathbb{N}$ and all vectors
$v_1, \dots, v_n \in \mathbb{R}^m$ with $\|v_i\|_2 \le 1$, there exist signs
$\varepsilon_i \in \{-1, +1\}$ such that
$\left\|\sum_i \varepsilon_i v_i\right\|_\infty \le C \sqrt{\log(n + 2)}$.
This is the best known bound towards the Komlós conjecture. (The shift $n + 2$ inside
the logarithm is a harmless normalization keeping it positive for $n \in \{0, 1\}$.)

[W. Banaszczyk, *Balancing vectors and Gaussian measures of n-dimensional convex bodies*,
Random Structures & Algorithms **12** (1998), 351–360.]
-/
@[category research solved, AMS 5]
theorem komlos_conjecture.variants.banaszczyk :
    ∃ C : ℝ, 0 < C ∧ ∀ (n m : ℕ) (v : Fin n → Fin m → ℝ),
      (∀ i, ∑ j, (v i j) ^ 2 ≤ 1) →
      ∃ ε : Fin n → ℝ, (∀ i, ε i = 1 ∨ ε i = -1) ∧
        ∀ j, |∑ i, ε i * v i j| ≤ C * Real.sqrt (Real.log (n + 2)) := by
  sorry

/--
Sanity check: with no vectors at all ($n = 0$), the empty signed sum is $0$ in every
coordinate, so any constant bound holds.
-/
@[category test, AMS 5]
theorem komlos_conjecture.variants.zero_vectors (m : ℕ) (v : Fin 0 → Fin m → ℝ) :
    ∃ ε : Fin 0 → ℝ, (∀ i, ε i = 1 ∨ ε i = -1) ∧
      ∀ j, |∑ i, ε i * v i j| ≤ 1 :=
  ⟨Fin.elim0, fun i => i.elim0, by simp⟩

end KomlosConjecture


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
