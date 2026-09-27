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
# Erdős Problem 750

*References:*
- [erdosproblems.com/750](https://www.erdosproblems.com/750)
- [EHS82] Erdős, P. and Hajnal, A. and Szemerédi, E., On almost bipartite large chromatic graphs.
  Theory and practice of combinatorics (1982), 117-123.
- [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in Graph
  Theory (1969), 27-35.
- [Er94b] Erdős, Paul, _Some problems in number theory, combinatorics and combinatorial geometry_.
  Math. Pannon. (1994), 261-269.
- [Er95d] Erdős, Paul, On some problems in combinatorial set theory. Publ. Inst. Math. (Beograd)
  (N.S.) (1995), 61-65.
- [ErHa67b] Erdős, P. and Hajnal, András, On chromatic graphs. Mat. Lapok (1967), 1--4.
- [UlamErdos750](https://www.ulam.ai/research/erdos750.pdf)
- [St85] Stiebitz, M., _Beiträge zur Theorie der färbungskritischen Graphen_. Habilitation,
  TH Ilmenau (1985).
- [SaSt89] Sachs, H. and Stiebitz, M., _On constructive methods in the theory of colour-critical
  graphs_. Discrete Math. (1989), 287-296.
- [MuSt19] Müller, T. and Stehlík, M., _Generalised Mycielski graphs and the Borsuk-Ulam theorem_.
  Electron. J. Combin. (2019), P4.8.
-/

open Filter Finset NNReal SimpleGraph

universe u

namespace Erdos750

/--
Vertices of the generalised Mycielskian $M_s(G)$: $s$ copies of the vertices of $G$, one per
level, and a single apex.
-/
abbrev MycVerts (s : ℕ) (V : Type u) : Type u := (Fin s × V) ⊕ Unit

/--
Adjacency of the generalised Mycielskian, before `SimpleGraph.fromRel` packages it as a graph.

Two level-`0` vertices are adjacent when the underlying vertices are; a level-`i` vertex and a
level-`i + 1` vertex are adjacent when the underlying vertices are; and the apex is adjacent to
every vertex on the top level. The relation is already symmetric and irreflexive, so `fromRel`
changes nothing about it.
-/
def MycAdj (s : ℕ) {V : Type u} (G : SimpleGraph V) : MycVerts s V → MycVerts s V → Prop
  | Sum.inl (i, u), Sum.inl (j, v) =>
      (i.val = 0 ∧ j.val = 0 ∧ G.Adj u v) ∨ (j.val = i.val + 1 ∧ G.Adj u v) ∨
        (i.val = j.val + 1 ∧ G.Adj u v)
  | Sum.inl (i, _), Sum.inr () => i.val + 1 = s
  | Sum.inr (), Sum.inl (i, _) => i.val + 1 = s
  | Sum.inr (), Sum.inr () => False

/--
The **generalised Mycielskian** $M_s(G)$. $M_2(G)$ is the classical Mycielskian, and $M_1(G)$
adds a vertex joined to everything.
-/
def genMyc (s : ℕ) {V : Type u} (G : SimpleGraph V) : SimpleGraph (MycVerts s V) :=
  .fromRel (MycAdj s G)

/-- The apex of $M_s(G)$ is adjacent to every vertex on the top level. -/
@[category test, AMS 5]
theorem genMyc_apex_adj_top {V : Type u} (G : SimpleGraph V) (s : ℕ) (hs : 0 < s) (v : V) :
    (genMyc s G).Adj (Sum.inr ()) (Sum.inl (⟨s - 1, by omega⟩, v)) := by
  refine ⟨by simp, Or.inl ?_⟩
  show s - 1 + 1 = s
  omega

/-- Two level-`0` vertices of $M_s(G)$ are adjacent exactly when the underlying vertices are. -/
@[category test, AMS 5]
theorem genMyc_adj_level_zero {V : Type u} (G : SimpleGraph V) {s : ℕ} (hs : 0 < s) {u v : V}
    (huv : G.Adj u v) :
    (genMyc s G).Adj (Sum.inl (⟨0, hs⟩, u)) (Sum.inl (⟨0, hs⟩, v)) := by
  refine ⟨by simpa using huv.ne, Or.inl ?_⟩
  exact Or.inl ⟨rfl, rfl, huv⟩

/--
`G` belongs to the class $M_r$, meaning it is built from $K_2$ by $r - 2$ generalised
Mycielskians. Stiebitz's theorem is about this class and not about arbitrary graphs: it is false
that $\chi(M_s(H)) = \chi(H) + 1$ for every $H$ and every $s$.
-/
def IsRecursivelyBuiltMr : ∀ (_r : ℕ) {_V : Type u} (_G : SimpleGraph _V), Prop
  | 0, _, _ => False
  | 1, _, _ => False
  | 2, _, G => Nonempty (G ≃g completeGraph (Fin 2))
  | r + 3, _, G => ∃ (W : Type u) (H : SimpleGraph W) (s : ℕ),
      1 ≤ s ∧ IsRecursivelyBuiltMr (r + 2) H ∧ Nonempty (G ≃g genMyc s H)

/--
**Stiebitz's theorem** [St85]: every graph in $M_r$ has chromatic number at least $r$. The
matching upper bound follows from the construction, so the chromatic number is exactly $r$.

This is stated ahead of `erdos_750` because the formal proof linked there assumes it, and the
`assuming` clause must name a declaration that already exists. See also [SaSt89] and [MuSt19].
-/
@[category research solved, AMS 5]
theorem erdos_750.variants.stiebitz {V : Type u} (G : SimpleGraph V) (r : ℕ)
    (h : IsRecursivelyBuiltMr r G) : (r : ℕ∞) ≤ G.chromaticNumber := by
  sorry

/--
Let $f(m)$ be some function such that $f(m)\to \infty$ as $m\to 

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
