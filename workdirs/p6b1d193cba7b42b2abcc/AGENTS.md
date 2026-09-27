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
# Erdős Problem 844

*References:*
- [erdosproblems.com/844](https://www.erdosproblems.com/844)
- [AMS25] Alexeev, B., Mixon, D. and Sawin, W., *The independence and clique cover numbers of the
  squarefree graph*. arXiv:2507.01928 (2025).
- [Ch74] Chvátal, V., *Intersecting families of edges in hypergraphs having the hereditary
  property*. (1974), 61-66.
-/

namespace Erdos844

/-- Those $n \in \{1,\ldots,N\}$ which are even or not squarefree, that is, the set of even
numbers together with the odd non-squarefree numbers. -/
def evenOrOddNonSquarefree (N : ℕ) : Finset ℕ :=
  (Finset.Icc 1 N).filter (fun n => 2 ∣ n ∨ ¬ Squarefree n)

/--
Let $A\subseteq \{1,\ldots,N\}$ be such that, for all $a,b\in A$, the product $ab$ is not
squarefree.

Is the maximum size of such an $A$ achieved by taking $A$ to be the set of even numbers and
odd non-squarefree numbers?

A problem of Erdős and Sárközy.

Weisenberg has provided the following positive proof. It is clear that such a maximal $A$ must
contain all non-squarefree numbers. It therefore suffices to find the largest size of a subset
of all squarefree numbers in $\{1,\ldots,N\}$ such that any two have at least one prime factor
in common. By the result of Chvátal [Ch74] discussed in [701] this is maximised by the set of
all even squarefree numbers.

An alternative proof was independently found by Alexeev, Mixon, and Sawin [AMS25].

This was formalized in Lean by Jennings using Aristotle.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at
"https://gist.githubusercontent.com/JohnEdwardJennings/e32f2c412b0225091e7519d60741bd2d/raw/7d811ea413e2f7c0c0442749958aaac421eb6807/Erdos844.lean"]
theorem erdos_844 : answer(True) ↔ ∀ N : ℕ,
    IsGreatest {k : ℕ | ∃ A ⊆ Finset.Icc 1 N,
      (∀ a ∈ A, ∀ b ∈ A, ¬ Squarefree (a * b)) ∧ A.card = k}
      (evenOrOddNonSquarefree N).card := by
  sorry

end Erdos844


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
