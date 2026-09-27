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
# Erdős Problem 426

*References:*
- [erdosproblems.com/426](https://www.erdosproblems.com/426)
- [Er76b] Erdős, P., *Problems and results in graph theory and combinatorial analysis*.
  Proceedings of the Fifth British Combinatorial Conference (1976), 169-192.
- [EnEr72] Entringer, R. C. and Erdős, Paul, *On the number of unique subgraphs of a graph*.
  J. Combinatorial Theory Ser. B (1972), 112-115.
- [HaSc73] Harary, Frank and Schwenk, Allen J., *On the number of unique subgraphs*.
  J. Combinatorial Theory Ser. B (1973), 156-160.
- [Br75] Brouwer, A. E., *Note: "On the number of unique subgraphs of a graph"
  (J. Combinatorial Theory Ser. B 13 (1972), 112-115) by R. C. Entringer and P. Erdős*.
  J. Combinatorial Theory Ser. B (1975), 184-185.
- [BrCh24] Bradač, D. and Christoph, M., *Unique subgraphs are rare*. arXiv:2410.16233 (2024).
-/

open Filter SimpleGraph

namespace Erdos426

/-- Sanity check: the empty graph `⊥` is a unique subgraph of itself. Its only subgraph is `⊥`
(everything `≤ ⊥` equals `⊥`), which is isomorphic to `⊥` via the identity. -/
@[category test, AMS 5]
theorem isUniqueSubgraph_bot_bot {V : Type*} : IsUniqueSubgraph (⊥ : SimpleGraph V) ⊥ := by
  refine ⟨⊥, ⟨le_refl _, ⟨Iso.refl⟩⟩, ?_⟩
  rintro G' ⟨hle, -⟩
  exact le_bot_iff.mp hle

/--
We say $H$ is a unique subgraph of $G$ if there is exactly one way to find $H$ as a subgraph
(not necessarily induced) of $G$. Is there a graph on $n$ vertices with
$$\gg \frac{2^{\binom{n}{2}}}{n!}$$
many distinct unique subgraphs?

Bradač and Christoph [BrCh24] have proved the answer is no: if $f(n)$ is the maximum number of
unique subgraphs in a graph on $n$ vertices then
$$f(n) = o\left(\frac{2^{\binom{n}{2}}}{n!}\right).$$

The $\gg$ below is read as: some constant $c>0$ works for arbitrarily large $n$. The negation
of the proposition on the right is then exactly $f(n) = o(2^{\binom{n}{2}}/n!)$, the form in
which Bradač and Christoph [BrCh24] resolved the problem.

The linked file states the resolution in that negated form, as
`Tendsto fSeq atTop (nhds 0)`. It counts the isomorphism classes occurring as unique subgraphs,
whereas `uniqueSubgraphCount` counts their representatives $G\leq H$; uniqueness forces exactly
one representative per class, so the two counts agree.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos426.lean"]
theorem erdos_426 : answer(False) ↔
    ∃ c : ℝ, 0 < c ∧ ∃ᶠ (n : ℕ) in atTop, ∃ H : SimpleGraph (Fin n),
      c * ((2 : ℝ) ^ n.choose 2 / n.factorial) ≤ (uniqueSubgraphCount H : ℝ) := by
  sorry

end Erdos426


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
