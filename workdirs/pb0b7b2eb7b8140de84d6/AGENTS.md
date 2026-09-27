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
# Erdős Problem 533

*References:*
- [erdosproblems.com/533](https://www.erdosproblems.com/533)
- [EHSSS94] P. Erdős, A. Hajnal, M. Simonovits, V. T. Sós and E. Szemerédi,
  *Turán-Ramsey theorems and $K_p$-independence numbers*,
  Combin. Probab. Comput. **3** (1994), 297–325.
- [ErRo62] P. Erdős and C. A. Rogers, *The construction of certain graphs*,
  Canad. J. Math. **14** (1962), 702–707.
- [BaLe13] J. Balogh and J. Lenz, *On the Ramsey–Turán numbers of graphs and hypergraphs*,
  Israel J. Math. **194** (2013), 45–68.
- [LRSS21] H. Liu, C. Reiher, M. Sharifzadeh and K. Staden,
  *Geometric constructions for Ramsey–Turán theory*,
  [arXiv:2103.10423](https://arxiv.org/abs/2103.10423) (2021).
-/

open Filter SimpleGraph

namespace Erdos533

/--
Let $\delta > 0$. If $n$ is sufficiently large and $G$ is a graph on $n$ vertices with no
$K_5$ and at least $\delta n^2$ edges, must $G$ contain a set of $\gg_\delta n$ vertices
spanning no triangle?

Equivalently, writing $\mathrm{RT}_3(n, K_5, m)$ for the maximum number of edges of a
$K_5$-free graph on $n$ vertices in which every triangle-free vertex set has fewer than $m$
vertices (the *triangle Ramsey–Turán number*), is
$$\delta_3(5) = \lim_{\epsilon \to 0} \lim_{n \to \infty}
  \frac{\mathrm{RT}_3(n, K_5, \epsilon n)}{n^2} = 0?$$

This is a problem of Erdős, Hajnal, Simonovits, Sós, and Szemerédi [EHSSS94], who proved
$\delta_3(5) \leq 1/12$ and the analogous $\delta_3(4) = 0$, and observed $\delta_3(7) \geq 1/4$
via a construction of Erdős and Rogers [ErRo62].

The answer is **no**: Balogh and Lenz [BaLe13] disproved it by showing $\delta_3(5) > 0$, and
the exact value $\delta_3(5) = 1/12$ was determined by the matching lower-bound construction of
Liu, Reiher, Sharifzadeh, and Staden [LRSS21] (see `erdos_533.variants.lrss_lower`).
-/
@[category research solved, AMS 5]
theorem erdos_533 : answer(False) ↔
    ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 5 →
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card →
          ∃ S : Finset (Fin n), c * n ≤ (S.card : ℝ) ∧
            G.CliqueFreeOn (S : Set (Fin n)) 3 := by
  sorry

/--
The upper bound $\delta_3(5) \leq 1/12$ of Erdős, Hajnal, Simonovits, Sós, and Szemerédi
[EHSSS94]: for every $\epsilon > 0$ there is a $\delta > 0$ such that for all sufficiently
large $n$, every $K_5$-free graph $G$ on $n$ vertices in which every triangle-free vertex
set has at most $\delta n$ vertices has at most $(1/12 + \epsilon)n^2$ edges.
-/
@[category research solved, AMS 5]
theorem erdos_533.variants.ehsss_upper (ε : ℝ) (hε : 0 < ε) :
    ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 5 →
        (∀ S : Finset (Fin n),
            G.CliqueFreeOn (S : Set (Fin n)) 3 → (S.card : ℝ) ≤ δ * n) →
          (G.edgeFinset.card : ℝ) ≤ (1 / 12 + ε) * n ^ 2 := by
  sorry

/--
The matching lower bound $\delta_3(5) \geq 1/12$, from the construction of Liu, Reiher,
Sharifzadeh, and Staden [LRSS21] (improving the earlier $\delta_3(5) > 0$ of Balogh and Lenz
[BaLe13]): for every $\epsilon, \delta > 0$ and all sufficiently large $n$ there is a
$K_5$-free graph $G$ on $n$ vertices in which every triangle-free vertex set has at most
$\delta n$ vertices, yet which has at least $(1/12 - \epsilon)n^2$ edges. In particular this
refutes `erdos_533`.
-/
@[category research solved, AMS 5]
theorem erdos_533.variants.lrss_lower (ε δ : ℝ) (hε : 0 < ε) (hδ : 0 < δ) :
    ∀ᶠ n : ℕ in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 5 ∧
        (∀ S : Finset (Fin n),
            G.CliqueFreeOn (S : Set (Fin n)) 3 → (S.card : ℝ) ≤ δ * n) ∧
        (1 / 12 - ε) * (n : ℝ) ^ 2 ≤ G.edgeFinset.card := by
  sorry

/--
The contrasting positive result $\delta_3(4) = 0$ of Erdős, Hajnal, Simonovits, Sós, and
Szemerédi [EHSSS94]: the $K_4$ analogue of `erdos_533` is **true**. For every $\delta > 0$
there is a $c > 0$ such that for all sufficiently large $n$, every $K_4$-free graph $G$ on
$n$ vertices with at least $\delta n^2$ edges contains a triangle-free vertex set of size at
least $c n$.
-/
@[category research solved, AMS 5]
theorem erdos_533.variants.delta_four_eq_zero :
    ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 4 →
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card →
          ∃ S : Finset (Fin n), c * n ≤ (S.card : ℝ) ∧
 

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
