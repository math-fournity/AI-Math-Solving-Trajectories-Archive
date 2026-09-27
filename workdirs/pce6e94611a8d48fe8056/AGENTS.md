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
# Erdős Problem 453

*References:*
- [erdosproblems.com/453](https://www.erdosproblems.com/453)
- [Er70b] Erdős, P., *Some applications of graph theory to number theory*. Proc. Second Chapel Hill
  Conf. on Combinatorial Mathematics and its Applications (Univ. North Carolina, Chapel Hill, N.C.,
  1970) (1970), 136-145.
- [Er74b] Erdős, P., *Remarks on some problems in number theory*. Math. Balkanica (1974), 197-202.
- [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory day
  (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
- [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
  (1980), 89-115.
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
  theory*. Monographies de L'Enseignement Mathematique (1980).
- [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
- [Po79] Pomerance, Carl, *The prime number graph*. Math. Comp. (1979), 399-408.
-/

namespace Erdos453

/-- The eventual prime inequality asked in Erdős Problem 453, using Mathlib's zero-based primes. -/
def EventuallyHasPrimeWitness : Prop :=
  ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
    ∃ i : ℕ, i < n ∧
      (Nat.nth Nat.Prime n) ^ (2 : ℕ) <
        Nat.nth Nat.Prime (n + i) * Nat.nth Nat.Prime (n - i)

/--
Is it true that, for all sufficiently large $n$, there exists some $i<n$ such that
$$
p_n^2 < p_{n+i}p_{n-i},
$$
where $p_k$ is the $k$th prime?

Pomerance proved that the answer is no.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos453.lean"]
theorem erdos_453 : answer(False) ↔ EventuallyHasPrimeWitness := by
  sorry

end Erdos453


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
