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
# Erdős Problem 950

*References:*
- [erdosproblems.com/855](https://www.erdosproblems.com/855)
- [erdosproblems.com/950](https://www.erdosproblems.com/950)
- [Er77c] Erdős, Paul, Problems and results on combinatorial number theory. III. Number theory day
  (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
- [mathoverflow/508491](https://mathoverflow.net/questions/508491)
-/

open Filter
open scoped Asymptotics Nat.Prime

namespace Erdos950

/--
Let $f(n) = \sum_{p<n}\frac{1}{n-p}$.
-/
noncomputable def f (n : ℕ) : ℝ :=
  ∑ p ∈ (Finset.range n).filter Prime, (1 : ℝ) / (n - p : ℝ)

/--
Is it true that $\liminf f(n)=1$?
-/
@[category research open, AMS 11]
theorem erdos_950.parts.i :
    answer(sorry) ↔ atTop.liminf (fun n : ℕ ↦ (f n : EReal)) = 1 := by
  sorry

/--
Is it true that $\limsup f(n)=\infty$?
-/
@[category research open, AMS 11]
theorem erdos_950.parts.ii :
    answer(sorry) ↔ atTop.limsup (fun n : ℕ ↦ (f n : EReal)) = ⊤ := by
  sorry

/--
Is it true that $f(n)=o(\log\log n)$ for all $n$?
-/
@[category research open, AMS 11]
theorem erdos_950.parts.iii :
    answer(sorry) ↔ f =o[atTop] (fun n : ℕ ↦ Real.log (Real.log n)) := by
  sorry

/--
This function was considered by de Bruijn, Erdős, and Turán, who showed that
$\sum_{n<x}f(n)\sim \sum_{n<x}f(n)^2\sim x$. They gave no proofs, but a proof of the (harder) second
claim is given by Gorodetsky here [mathoverflow/508491].
-/
@[category research solved, AMS 11]
theorem erdos_950.variants.debruijn_erdos_turan :
    (fun x : ℕ ↦ ∑ n ∈ Finset.range x, f n) ~[atTop] (fun x : ℕ ↦ (x : ℝ)) ∧
    (fun x : ℕ ↦ ∑ n ∈ Finset.range x, (f n) ^ 2) ~[atTop] (fun x : ℕ ↦ (x : ℝ)) := by
  sorry

/--
Erdős writes that a 'weaker conjecture which is perhaps not quite inaccessible' is that,
for every $\epsilon>0$, if $x$ is sufficiently large there exists $y<x$ such that
$\pi(x)< \pi(y)+\epsilon \pi(x-y)$. Compare this to [855].
-/
@[category research open, AMS 11]
theorem erdos_950.variants.weaker_pi :
    answer(sorry) ↔ ∀ ε > 0, ∀ᶠ x in atTop, ∃ y < x,
      (π x : ℝ) < (π y : ℝ) + ε * (π (x - y) : ℝ) := by
  sorry

/--
He notes that if $\pi(x)< \pi(y)+O\left(\frac{x-y}{\log x}\right)$ for all $y<x-(\log x)^C$ for
some constant $C>0$ then $f(n)\ll \log\log\log n$.
-/
@[category research solved, AMS 11]
theorem erdos_950.variants.weaker_pi_implies_f
    (h : ∃ C > (0 : ℝ), ∃ K > (0 : ℝ), ∀ᶠ x : ℕ in atTop, ∀ y : ℕ,
      (y : ℝ) < x - (Real.log x) ^ C →
      (π x : ℝ) < (π y : ℝ) + K * ((x - y : ℝ) / Real.log x)) :
    f =O[atTop] fun n : ℕ ↦ Real.log (Real.log (Real.log n)) := by
  sorry

/--
The study of $f(p)$ is even harder, and Erdős could not prove that
$\sum_{p<x}f(p)^2\sim \pi(x)$.
-/
@[category research open, AMS 11]
theorem erdos_950.variants.sum_primes :
    answer(sorry) ↔
      (fun x : ℕ ↦ ∑ p ∈ (Finset.range x).filter Prime, (f p) ^ 2) ~[atTop]
        fun x ↦ (π x : ℝ) := by
  sorry

end Erdos950


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
