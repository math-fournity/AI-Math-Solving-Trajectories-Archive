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
# Erdős Problem 944

*Reference:* [erdosproblems.com/944](https://www.erdosproblems.com/944)
-/

universe u
variable {V : Type u}

namespace Erdos944

open Erdos944

/--
The predicate that graph $G$ with chromatic number $k$ is such that every vertex is critical, yet
every critical set of edges has size $>r$
-/
def SimpleGraph.IsErdos944 (G : SimpleGraph V) (k r : ℕ) : Prop :=  G.IsCritical k ∧
    (∀ (edges : Set (Sym2 V)), G.IsCriticalEdges edges → r < edges.ncard)

/--
Let $k \ge 4$ and $r\ge 1$. Must there exist a graph $G$ with chromatic number $k$
 such that every vertex is critical, yet every critical set of edges has size $>r$?
-/
@[category research open, AMS 11]
theorem erdos_944 :
    answer(sorry) ↔ ∀ k ≥ 4, ∀ r ≥ 1, ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k r := by
  sorry

/--
Let $k \ge 4$. Must there exist a graph $G$ with chromatic number $k$
such that every vertex is critical, yet every critical set of edges has size $>1$?

This was conjectured by Dirac in 1970.
-/
@[category research open, AMS 11]
theorem erdos_944.variants.dirac_conjecture :
    answer(sorry) ↔ ∀ k ≥ 4, ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k 1 := by
  sorry


/--
Dirac's conjecture was proved, for $k=5$: There exists a graph $G$ with chromatic number $5$, such
that every vertex is critical, yet every critical set of edges has size $>1$, or in other words:
has no critical edge.

[Br92] Brown, Jason I., A vertex critical graph without critical edges. Discrete Math. (1992), 99--101
-/
@[category research solved, AMS 11]
theorem erdos_944.variants.dirac_conjecture.k_eq_5 :
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 5 1 := by
  sorry

/--
Lattanzio [La02] proved there exist $k$-critical graphs without critical edges for all $k$ such that
$k - 1$ is not prime.

[La02] Lattanzio, John J., A note on a conjecture of {D}irac. Discrete Math. (2002), 323--330
-/
@[category research solved, AMS 11]
theorem erdos_944.variants.dirac_conjecture.k_sub_one_not_prime (k : ℕ) (hk : 4 ≤ k)
    (h : ¬ (k - 1).Prime) : ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k 1 := by
  sorry

/--
Jensen [Je02] gave an construction for $k$-critical graphs without any critical edges for all $k ≥ 5$.

[Je02] Jensen, Tommy R., Dense critical and vertex-critical graphs. Discrete Math. (2002), 63--84.
-/
@[category research solved, AMS 11]
theorem erdos_944.variants.dirac_conjecture.k_ge_five (k : ℕ) (hk : 5 ≤ k) :
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k 1 := by
  sorry

/--
The case $k=4$ and $r=1$ remains open: Are there $4$-critical graphs without any critical edges?
-/
@[category research open, AMS 11]
theorem erdos_944.variants.dirac_conjecture.k_eq_four :
    answer(sorry) ↔ ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 4 1 := by
  sorry

/--
Martinsson and Steiner [MaSt25] proved for every $r \ge 1$ if $k$ is sufficiently large, depending
on $r$, there exist a graph $G$ with chromatic number $k$ such that every vertex is critical,
yet every critical set of edges has size $>r$.

[MaSt25] Martinsson, Anders and Steiner, Raphael, Vertex-critical graphs far from edge-criticality. Combin. Probab. Comput. (2025), 151--157
-/
@[category research solved, AMS 11]
theorem erdos_944.variants.large_k_for_any_r (r : ℕ) (hr : 1 ≤ r) : ∀ᶠ k in Filter.atTop,
    ∃ (V : Type u) (G : SimpleGraph V), G.IsErdos944 k r := by
  sorry

  end Erdos944


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
