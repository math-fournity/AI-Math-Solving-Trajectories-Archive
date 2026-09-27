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
# Mean value problem

*Reference:*
- [Wikipedia](https://en.wikipedia.org/wiki/Mean_value_problem)
- [The fundamental theorem of algebra and complexity theory](https://www.ams.org/journals/bull/1981-04-01/S0273-0979-1981-14858-8/)
by Steve Smale

Given a complex polynomial $p$ of degree $d ≥ 2$ and a complex number $z$
there is a critical point $c$ of $p$, such that $|p(z)-p(c)|/|z-c| ≤ K* |p'(z)|$ for $K=1$.


The conjecture has been proven for:
* `K = 4`
  [The fundamental theorem of algebra and complexity theory](https://www.ams.org/journals/bull/1981-04-01/S0273-0979-1981-14858-8/)
  by *Steve Smale*
* `K = (d-1)/d` if $p$ has real roots or all the roots of $p$ have the same norm.
  [Critical points and values of complex polynomials](https://doi.org/10.1016/0885-064X(89)90019-8)
  by *David Tischler*
-/

namespace MeanValueProblem

/--
Given a complex polynomial $p$ of degree $d ≥ 2$ and a complex number $z$
there is a critical point $c$ of $p$, such that $|p(z)-p(c)|/|z-c| ≤ |p'(z)|$.
-/
@[category research open, AMS 12]
lemma mean_value_problem (p : Polynomial ℂ) (hp : 2 ≤ p.degree) (z : ℂ) (K : ℝ):
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ ‖p.derivative.eval z‖ := by
  sorry

/--
The following weaker version of the mean value problem has been proven.
Given a complex polynomial $p$ of degree $d ≥ 2$ and a complex number $z$
there a critical point $c$ of $p$, such that $|p(z)-p(c)|/|z-c| ≤ 4|p'(z)|$.
-/
@[category research solved, AMS 12]
lemma mean_value_problem_leq_4 (p : Polynomial ℂ) (hp : 2 ≤ p.degree) (z : ℂ) (K : ℝ):
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ 4 *‖p.derivative.eval z‖ := by
  sorry

/--
The following tighter bound depending on the degree $d$ of the polynomial $p$,
in the case of $p$ only having real roots has been shown by Tischler.
$|p(z)-p(c)|/|z-c| \le (d-1)/d \cdot |p'(z)|$
-/

@[category research solved, AMS 12]
lemma mean_value_problem_of_real_roots (p : Polynomial ℂ) (hp : 2 ≤ p.natDegree)
    (h : ∀ x : ℂ, p.IsRoot x → x.im = 0) (z : ℂ) (K : ℝ) :
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ (p.natDegree - 1)/ p.natDegree * ‖p.derivative.eval z‖ := by
  sorry

/--
The following tighter bound depending on the degree $d$ of the polynomial $p$,
in the case of $p$ all roots having the same norm has been shown by Tischler.
$|p(z) - p(c)|/|z-c| \le (d-1)/d \cdot |p'(z)|$.
-/

@[category research solved, AMS 12]
lemma mean_value_problem_of_roots_same_norm (p : Polynomial ℂ) (hp : 2 ≤ p.natDegree)
    (h : ∀ x y : ℂ, p.IsRoot x ∧ p.IsRoot y → ‖x‖=‖y‖) (z : ℂ) (K : ℝ) :
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ (p.natDegree - 1)/ p.natDegree * ‖p.derivative.eval z‖ := by
  sorry

end MeanValueProblem


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
