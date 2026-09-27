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
# Erdős Problem 753

*References:*
- [erdosproblems.com/753](https://www.erdosproblems.com/753)
- [Al92] Alon, Noga, *Choice numbers of graphs: a probabilistic approach*. Combin. Probab.
  Comput. (1992), 107-114.
-/

namespace Erdos753

/--
A graph $G$ is $k$-choosable if for any assignment of a list of $k$ colours to each vertex of $G$
(perhaps different lists for different vertices) a colouring of each vertex by a colour on its list
can be chosen such that adjacent vertices receive distinct colours.
-/
def IsKChoosable {V : Type*} (G : SimpleGraph V) (k : ℕ) : Prop :=
  ∀ L : V → Finset ℕ, (∀ v, (L v).card = k) → ∃ C : G.Coloring ℕ, ∀ v, C v ∈ L v

/--
The list chromatic number $\chi_L(G)$, defined to be the minimal $k$ such that $G$ is
$k$-choosable.
-/
noncomputable def listChromaticNumber {V : Type*} (G : SimpleGraph V) : ℕ :=
  sInf {k : ℕ | IsKChoosable G k}

/--
The list chromatic number $\chi_L(G)$ is defined to be the minimal $k$ such that for any
assignment of a list of $k$ colours to each vertex of $G$ (perhaps different lists for different
vertices) a colouring of each vertex by a colour on its list can be chosen such that adjacent
vertices receive distinct colours.

Does there exist some constant $c>0$ such that
$$\chi_L(G)+\chi_L(G^c)> n^{1/2+c}$$
for every graph $G$ on $n$ vertices (where $G^c$ is the complement of $G$)?

A problem of Erdős, Rubin, and Taylor.

The answer is no: Alon [Al92] proved that, for every $n$, there exists a graph $G$ on $n$ vertices
such that
$$\chi_L(G)+\chi_L(G^c)\ll (n\log n)^{1/2},$$
where the implied constant is absolute.
-/
@[category research solved, AMS 5, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos753.lean"]
theorem erdos_753 : answer(False) ↔
    ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 0 < n → ∀ G : SimpleGraph (Fin n),
      (n : ℝ) ^ ((1 : ℝ) / 2 + c) <
        (listChromaticNumber G : ℝ) + (listChromaticNumber Gᶜ : ℝ) := by
  sorry

/--
Alon [Al92] proved that, for every $n$, there exists a graph $G$ on $n$ vertices such that
$$\chi_L(G)+\chi_L(G^c)\ll (n\log n)^{1/2},$$
where the implied constant is absolute.
-/
@[category research solved, AMS 5]
theorem erdos_753.variants.alon :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, 2 ≤ n → ∃ G : SimpleGraph (Fin n),
      (listChromaticNumber G : ℝ) + (listChromaticNumber Gᶜ : ℝ) ≤
        C * ((n : ℝ) * Real.log (n : ℝ)) ^ ((1 : ℝ) / 2) := by
  sorry

end Erdos753


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
