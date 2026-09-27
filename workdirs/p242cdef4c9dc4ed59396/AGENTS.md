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

import FormalConjectures.Wikipedia.RamseyNumbers
import FormalConjecturesUtil

/-!
# Erdős Problem 1014

*References:*
- [erdosproblems.com/1014](https://www.erdosproblems.com/1014)
- [Er71] Erdős, P., Some unsolved problems in graph theory and combinatorial analysis. Combinatorial
  Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
- [OpenAI26] *On the ratio of $R(k,\ell)$ and $R(k,\ell+1)$*, proof due to an internal model at
  OpenAI (2026).
  https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/Ramsey.pdf
-/

open Filter

open scoped Topology

namespace Erdos1014

open RamseyNumbers

/--
Let $R(k,l)$ be the Ramsey number, so the minimal $n$ such that every graph on at least $n$
vertices contains either a $K_k$ or an independent set on $l$ vertices.

Prove, for fixed $k\geq 3$, that
$$\lim_{l\to \infty}\frac{R(k,l+1)}{R(k,l)}=1.$$

This has been
[solved](https://cdn.openai.com/pdf/6dc7175d-d9e7-4b8d-96b8-48fe5798cd5b/Ramsey.pdf)
by an internal model at OpenAI.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1014.lean"]
theorem erdos_1014 : ∀ k : ℕ, 3 ≤ k →
    Tendsto (fun l : ℕ ↦ (R(k, l + 1) : ℝ) / (R(k, l) : ℝ)) atTop (𝓝 1) := by
  sorry

/--
That proof in fact shows that
$$R(k,l+1)\leq (1+O(l^{-c/k^2}))R(k,l)$$
for some constant $c>0$.
-/
@[category research solved, AMS 5]
theorem erdos_1014.variants.upper_bound :
    ∃ c : ℝ, 0 < c ∧ ∀ k : ℕ, 3 ≤ k → ∃ C : ℝ, ∀ᶠ l : ℕ in atTop,
      (R(k, l + 1) : ℝ) ≤ (1 + C * (l : ℝ) ^ (-c / (k : ℝ) ^ 2)) * (R(k, l) : ℝ) := by
  sorry

end Erdos1014


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
