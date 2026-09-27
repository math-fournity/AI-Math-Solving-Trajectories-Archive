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
# Erdős Problem 71

*References:*
- [erdosproblems.com/71](https://www.erdosproblems.com/71)
- [Bo77] Bollobás, Béla, *Cycles modulo $k$*. Bull. London Math. Soc. (1977), 97-98.
- [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
  (1982), 59--79.
- [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
  geometry*. Resenhas (1995), 165-186.
- [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*.
  Discrete Math. (1997), 227-231.
-/

namespace Erdos71

/--
Is it true that for every infinite arithmetic progression $P$ which contains even numbers
there is some constant $c=c(P)$ such that every graph with average degree at least $c$
contains a cycle whose length is in $P$?

In [Er82e] Erdős credits this conjecture to himself and Burr. This has been proved by
Bollobás [Bo77]. The best dependence of the constant $c(P)$ is unknown.

The infinite arithmetic progression is encoded as a set $P \subseteq \mathbb{N}$ satisfying
`P.IsAPOfLength ⊤` (which forces a positive common difference), and "contains even numbers"
as the existence of an even element. The average degree of a finite simple graph is
`SimpleGraph.averageDegree`, i.e. $(\sum_v \deg v)/|V| \in \mathbb{Q}$, and a cycle whose
length is in $P$ is a cycle walk `w` with `w.length ∈ P`.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/71/Erdos71.lean"]
theorem erdos_71 : answer(True) ↔
    ∀ P : Set ℕ, P.IsAPOfLength ⊤ → (∃ n ∈ P, Even n) →
      ∃ c : ℚ, ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
        [DecidableRel G.Adj], c ≤ G.averageDegree →
          ∃ (v : V) (w : G.Walk v v), w.IsCycle ∧ w.length ∈ P := by
  sorry

end Erdos71


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
