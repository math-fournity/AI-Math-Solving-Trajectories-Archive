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
# Erdős Problem 61 -- Erdős–Hajnal Conjecture

*Reference:* [erdosproblems.com/61](https://www.erdosproblems.com/61)
-/

open Filter
open SimpleGraph
open Real

namespace Erdos61

/-
For a graph $H$, consider all graphs $G$ that do not contain $H$ as an induced subgraph.
We would like to find a lower bound $f(n)$ such that every such $G$ on $n$ vertices
has a clique or independent set of size $\ge f(n)$ for sufficiently large $n$.
-/
def IsErdosHajnalLowerBound {α : Type*} [Fintype α] [DecidableEq α]
  (H : SimpleGraph α) (f : ℕ → ℝ) : Prop :=
  ∀ᶠ n in atTop, ∀ G : SimpleGraph (Fin n),
    (¬∃ g : α ↪ Fin n, H = G.comap g) → G.indepNum ≥ f n ∨ G.cliqueNum ≥ f n

/--
The Erdős–Hajnal Conjecture states that there is a constant $c(H) > 0$ for each
$H$ such that we can take $f(n) = n^{c(H)}$ in the above formulation.
-/
@[category research open, AMS 5]
theorem erdos_61 :
    answer(sorry) ↔ ∀ {α : Type*} [Fintype α] [DecidableEq α] (H : SimpleGraph α),
      ∃ c > (0 : ℝ), IsErdosHajnalLowerBound H (fun n : ℕ => (n : ℝ) ^ c) := by
  sorry

/--
Erdős and Hajnal [ErHa89] proved that we can take $f(n) = \exp(c_H \sqrt{\log n})$
for some constant $c_H > 0$ depending on $H$.

[ErHa89] Erdős, P. and Hajnal, A., Ramsey-type theorems. Discrete Appl. Math. (1989), 37-52.
-/
@[category research solved, AMS 5]
theorem erdos_61.variants.erha89 :
    ∀ {α : Type*} [Fintype α] [DecidableEq α] (H : SimpleGraph α),
      ∃ c > (0 : ℝ), IsErdosHajnalLowerBound H (fun n : ℕ => exp (c * sqrt (log n))) := by
  sorry

/--
Bucić, Nguyen, Scott, and Seymour [BNSS23] improved this to
$f(n) = \exp(c_H \sqrt{\log n \log \log n})$ for some constant $c_H > 0$ depending on $H$.

[BNSS23] Bucić, M. and Nguyen, T. and Scott, A. and Seymour, P., A loglog step towards Erdos-Hajnal
-/
@[category research solved, AMS 5]
theorem erdos_61.variants.bnss23 :
    ∀ {α : Type*} [Fintype α] [DecidableEq α] (H : SimpleGraph α),
      ∃ c > (0 : ℝ), IsErdosHajnalLowerBound H (fun n : ℕ => exp (c * sqrt (log n * log (log n)))) := by
  sorry

/--
Nguyen, Scott, and Seymour [NSS23] proved the conjecture for $H = P_5$, the path on five
vertices: every $P_5$-free graph on $n$ vertices has a clique or independent set of
polynomial size.

[NSS23] Nguyen, T., Scott, A. and Seymour, P., Induced subgraph density. VII. The
five-vertex path. [arXiv:2312.15333](https://arxiv.org/abs/2312.15333)
-/
@[category research solved, AMS 5]
theorem erdos_61.variants.p5 :
    ∃ c > (0 : ℝ), IsErdosHajnalLowerBound (pathGraph 5) (fun n : ℕ => (n : ℝ) ^ c) := by
  sorry

/--
Chudnovsky, Scott, Seymour, and Spirkl [CSSS23] proved the conjecture for $H = C_5$, the
cycle on five vertices: every graph with no induced five-cycle has a clique or independent
set of polynomial size.

[CSSS23] Chudnovsky, M., Scott, A., Seymour, P. and Spirkl, S., Erdős–Hajnal for graphs with
no 5-hole. Proc. Lond. Math. Soc. (3) 126 (2023), 997–1014.
-/
@[category research solved, AMS 5]
theorem erdos_61.variants.c5 :
    ∃ c > (0 : ℝ), IsErdosHajnalLowerBound (cycleGraph 5) (fun n : ℕ => (n : ℝ) ^ c) := by
  sorry

end Erdos61


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
