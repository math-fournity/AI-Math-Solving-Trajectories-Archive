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
# Erdős Problem 621

*References:*
- [erdosproblems.com/621](https://www.erdosproblems.com/621)
- [EGT96] Erdős, Paul and Gallai, Tibor and Tuza, Zsolt, *Covering and independence in triangle
  structures*. Discrete Math. (1996), 89-101.
- [Er99] Erdős, Paul, *A selection of problems and results in combinatorics*.
  Combin. Probab. Comput. (1999), 1-6.
- [NoSu16] S. Norin and Y.-R. Sun, *Triangle-free independent sets vs. cuts*. arXiv:1602.04370
  (2016).
-/

open SimpleGraph

namespace Erdos621

/--
Let $G$ be a graph on $n$ vertices, $\alpha_1(G)$ be the maximum number of edges that contain
at most one edge from every triangle, and $\tau_1(G)$ be the minimum number of edges that
contain at least one edge from every triangle.

Is it true that$$\alpha_1(G)+\tau_1(G) \leq \frac{n^2}{4}?$$

A problem of Erdős, Gallai, and Tuza [EGT96], who observe that this is probably quite difficult
since there are different examples where equality hold: the complete graph, the complete
bipartite graph, and the graph obtained from $K_{m,m}$ by adding one vertex joined to every
other.

This is true, and was proved by Norin and Sun [NoSu16], who in fact proved
that$$\alpha_1(G)+\tau_B(G) \leq \frac{n^2}{4},$$where $\tau_B(G)$ is the minimum number of
edges that need to be removed to make the graph bipartite.

Here $\alpha_1(G)$ and $\tau_1(G)$ are taken over subsets of the edge set of $G$, and the
inequality is stated multiplied through by $4$ so that it lives in the natural numbers.

The linked file states $\tau_1$ as the least number of edges whose deletion leaves $G$
triangle-free, which is the same as meeting every triangle of $G$, and quantifies over an
arbitrary `Fintype V` rather than `Fin n`.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos621.lean"]
theorem erdos_621 : answer(True) ↔
    ∀ (n : ℕ) (G : SimpleGraph (Fin n)) (a t : ℕ),
      IsGreatest {k : ℕ | ∃ A ⊆ G.edgeFinset, A.card = k ∧
        ∀ x y z : Fin n, G.Adj x y → G.Adj y z → G.Adj x z →
          (({s(x, y), s(y, z), s(x, z)} : Finset (Sym2 (Fin n))) ∩ A).card ≤ 1} a →
      IsLeast {k : ℕ | ∃ T ⊆ G.edgeFinset, T.card = k ∧
        ∀ x y z : Fin n, G.Adj x y → G.Adj y z → G.Adj x z →
          (T ∩ ({s(x, y), s(y, z), s(x, z)} : Finset (Sym2 (Fin n)))).Nonempty} t →
      4 * (a + t) ≤ n ^ 2 := by
  sorry

end Erdos621


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
