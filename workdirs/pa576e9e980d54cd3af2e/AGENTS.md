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
# Erdős Problem 762

*References:*
- [erdosproblems.com/762](https://www.erdosproblems.com/762)
- [EGS90] Erdős, Paul and Gimbel, John and Straight, H. Joseph, *Chromatic number versus
  cochromatic number in graphs with bounded clique number*. European J. Combin. (1990), 235-240.
- [St24b] R. Steiner, *On the difference between the chromatic and cochromatic number*.
  arXiv:2408.02400 (2024).
-/

namespace Erdos762

/--
The cochromatic number of $G$, denoted by $\zeta(G)$, is the minimum number of colours needed to
colour the vertices of $G$ such that each colour class induces either a complete graph or empty
graph.

Is it true that if $G$ has no $K_5$ and $\zeta(G)\geq 4$ then $\chi(G) \leq \zeta(G)+2$?

This has been disproved by Steiner [St24b], who constructed a graph $G$ with $\omega(G)=4$,
$\zeta(G)=4$, and $\chi(G)=7$.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos762.lean"]
theorem erdos_762 : answer(False) ↔
    ∀ (V : Type*) [Fintype V] (G : SimpleGraph V),
      G.CliqueFree 5 → 4 ≤ G.cochromaticNumber →
        G.chromaticNumber ≤ G.cochromaticNumber + 2 := by
  sorry

/--
A conjecture of Erdős, Gimbel, and Straight [EGS90], who proved that for every $n>2$ there exists
some $f(n)$ such that if $G$ contains no clique on $n$ vertices then $\chi(G)\leq \zeta(G)+f(n)$.
-/
@[category research solved, AMS 5]
theorem erdos_762.variants.bounded_clique_number (n : ℕ) (hn : 2 < n) :
    ∃ f : ℕ, ∀ (V : Type*) [Fintype V] (G : SimpleGraph V),
      G.CliqueFree n → G.chromaticNumber ≤ G.cochromaticNumber + f := by
  sorry

/--
This has been disproved by Steiner [St24b], who constructed a graph $G$ with $\omega(G)=4$,
$\zeta(G)=4$, and $\chi(G)=7$.
-/
@[category research solved, AMS 5]
theorem erdos_762.variants.steiner :
    ∃ (n : ℕ) (G : SimpleGraph (Fin n)),
      G.cliqueNum = 4 ∧ G.cochromaticNumber = 4 ∧ G.chromaticNumber = 7 := by
  sorry

end Erdos762


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
