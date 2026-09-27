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
# Erdős Problem 1036

*References:*
- [erdosproblems.com/1036](https://www.erdosproblems.com/1036)
- [AlHa91] Alon, N. and Hajnal, A., *Ramsey graphs contain many distinct induced subgraphs*.
  Graphs Combin. (1991), 1-6.
- [ErHa89b] Erdős, P. and Hajnal, A., *On the number of distinct induced subgraphs of a graph*.
  Discrete Math. (1989), 145-154.
- [Sh98] Shelah, Saharon, *Erdős and Rényi conjecture*. J. Combin. Theory Ser. A (1998), 179-185.
-/

open Filter

namespace Erdos1036

/--
`G` contains at least `k` many induced subgraphs which are not pairwise isomorphic, that is,
there is a family of at least `k` many sets of vertices whose induced subgraphs are pairwise
non-isomorphic.
-/
def HasManyNonIsomorphicInducedSubgraphs {V : Type*} (G : SimpleGraph V) (k : ℝ) : Prop :=
  ∃ 𝒮 : Set (Set V), (𝒮.Pairwise fun s t => IsEmpty (G.induce s ≃g G.induce t)) ∧
    k ≤ (𝒮.ncard : ℝ)

/--
`G` contains no complete bipartite graph, and no complement of a complete bipartite graph, on
more than `m` vertices as an induced subgraph.
-/
def NoLargeInducedBipartite {V : Type*} (G : SimpleGraph V) (m : ℝ) : Prop :=
  ∀ (s : Set V) (a b : ℕ),
    (Nonempty (G.induce s ≃g completeBipartiteGraph (Fin a) (Fin b)) ∨
      Nonempty (G.induce s ≃g (completeBipartiteGraph (Fin a) (Fin b))ᶜ)) →
    (s.ncard : ℝ) ≤ m

/--
Let $G$ be a graph on $n$ vertices which does not contain a trivial (empty or complete) graph on
more than $c\log n$ vertices. Must $G$ contain at least $2^{\Omega_c(n)}$ many induced subgraphs
which are not pairwise isomorphic?

This is true, and was proved by Shelah [Sh98].
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1036.lean"]
theorem erdos_1036 : answer(True) ↔
    ∀ c : ℝ, 0 < c → ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) ≤ c * Real.log (n : ℝ) → (G.indepNum : ℝ) ≤ c * Real.log (n : ℝ) →
        HasManyNonIsomorphicInducedSubgraphs G ((2 : ℝ) ^ (δ * (n : ℝ))) := by
  sorry

/--
Alon and Hajnal [AlHa91] proved that $G$ must contain at least
$$\exp\left(n(\log n)^{-O(\log\log n)}\right)$$
many non-isomorphic induced subgraphs.
-/
@[category research solved, AMS 5]
theorem erdos_1036.variants.alon_hajnal :
    ∀ c : ℝ, 0 < c → ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (G.cliqueNum : ℝ) ≤ c * Real.log (n : ℝ) → (G.indepNum : ℝ) ≤ c * Real.log (n : ℝ) →
        HasManyNonIsomorphicInducedSubgraphs G
          (Real.exp ((n : ℝ) * Real.log (n : ℝ) ^ (-(C * Real.log (Real.log (n : ℝ)))))) := by
  sorry

/--
Erdős and Hajnal [ErHa89b] proved that if $G$ does not contain a complete bipartite graph or its
complement on more than $c\log n$ vertices then $G$ contains at least $2^{\Omega_c(n)}$ many
non-isomorphic induced subgraphs.
-/
@[category research solved, AMS 5]
theorem erdos_1036.variants.erdos_hajnal :
    ∀ c : ℝ, 0 < c → ∃ δ : ℝ, 0 < δ ∧ ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      NoLargeInducedBipartite G (c * Real.log (n : ℝ)) →
        HasManyNonIsomorphicInducedSubgraphs G ((2 : ℝ) ^ (δ * (n : ℝ))) := by
  sorry

end Erdos1036


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
