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
# Erdős Problem 403

*References:*
- [erdosproblems.com/403](https://www.erdosproblems.com/403)
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
  number theory*. Monographies de L'Enseignement Mathématique (1980).
- [Li76] Lin, S., *On two problems of Erdős concerning sums of distinct factorials*.
  Bell Laboratories internal memorandum (1960).
-/

namespace Erdos403

/--
Does the equation
$$2^m=a_1!+\cdots+a_k!$$
with $a_1<a_2<\cdots <a_k$ have only finitely many solutions?

Asked by Burr and Erdős. Frankl and Lin [Li76] independently showed that the answer is yes, and
the largest solution is
$$2^7=2!+3!+5!.$$
In fact Lin showed that the largest power of $2$ which can divide a sum of distinct factorials
containing $2$ is $2^{254}$, and that there are only 5 solutions to $3^m=a_1!+\cdots+a_k!$
(when $m=0,1,2,3,6$).

See also [404].

A solution is encoded below as a pair $(m, s)$ where $s$ is the finite set
$\{a_1 < a_2 < \cdots < a_k\}$ of positive integers, so the distinctness of the $a_i$ is
given by set membership. The empty set contributes no solutions since $2^m \geq 1 > 0$.

The linked proof gives more than finiteness: it classifies the solutions outright, as
$(0,\{1\})$, $(1,\{2\})$, $(3,\{2,3\})$, $(5,\{2,3,4\})$ and $(7,\{2,3,5\})$, so the set below
has exactly five elements.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/403/Erdos403.lean"]
theorem erdos_403 : answer(True) ↔
    {p : ℕ × Finset ℕ | (∀ a ∈ p.2, 0 < a) ∧
      2 ^ p.1 = ∑ a ∈ p.2, a.factorial}.Finite := by
  sorry

end Erdos403


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
