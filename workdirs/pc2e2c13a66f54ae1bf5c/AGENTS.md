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
# Erdős Problem 760

*References:*
- [erdosproblems.com/760](https://www.erdosproblems.com/760)
- [AKS97] Alon, Noga and Krivelevich, Michael and Sudakov, Benny, *Subgraphs with a large
  cochromatic number*. J. Graph Theory (1997), 295-297.
-/

namespace Erdos760

/--
The cochromatic number of $G$, denoted by $\zeta(G)$, is the minimum number of colours needed to
colour the vertices of $G$ such that each colour class induces either a complete graph or
independent set.

If $G$ is a graph with chromatic number $\chi(G)=m$ then must $G$ contain a subgraph $H$ with
$$
\zeta(H) \gg \frac{m}{\log m}?
$$

A problem of Erdős and Gimbel, who proved that there must exist a subgraph $H$ with
$$
\zeta(H) \gg \left(\frac{m}{\log m}\right)^{1/2}.
$$
The proposed bound would be best possible, as shown by taking $G$ to be a complete graph.

The answer is yes, proved by Alon, Krivelevich, and Sudakov.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos760.lean"]
theorem erdos_760 : answer(True) ↔
    ∃ c > (0 : ℝ), ∀ (V : Type*) [Finite V] (G : SimpleGraph V) (m : ℕ),
      G.chromaticNumber = (m : ℕ∞) →
        ∃ H : G.Subgraph, ∃ k : ℕ, ((k : ℕ∞) ≤ H.coe.cochromaticNumber) ∧
          (c * (m : ℝ) / Real.log (m : ℝ) ≤ (k : ℝ)) := by
  sorry

/--
A problem of Erdős and Gimbel, who proved that there must exist a subgraph $H$ with
$$
\zeta(H) \gg \left(\frac{m}{\log m}\right)^{1/2}.
$$
-/
@[category research solved, AMS 5]
theorem erdos_760.variants.erdos_gimbel :
    ∃ c > (0 : ℝ), ∀ (V : Type*) [Finite V] (G : SimpleGraph V) (m : ℕ),
      G.chromaticNumber = (m : ℕ∞) →
        ∃ H : G.Subgraph, ∃ k : ℕ, ((k : ℕ∞) ≤ H.coe.cochromaticNumber) ∧
          (c * Real.sqrt ((m : ℝ) / Real.log (m : ℝ)) ≤ (k : ℝ)) := by
  sorry

end Erdos760


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
