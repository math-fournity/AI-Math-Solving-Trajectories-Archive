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
import FormalConjectures.Wikipedia.HardyLittlewood

/-!
# Erdős Problem 884

*References:*
- [erdosproblems.com/884](https://www.erdosproblems.com/884)
- [Tao25](https://terrytao.wordpress.com/wp-content/uploads/2025/09/erdos-884.pdf)
- [Larsen](https://github.com/Larsen-Daniel/Erdos-884/blob/main/884.pdf)
-/

namespace Erdos884

/--
The sum $\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i}$ over all pairs of
divisors $d_i < d_j$ of $n$.
-/
noncomputable abbrev sumDivisorInvPairwiseDifference (n : ℕ) : ℝ :=
    ∑ j : Fin n.divisors.card, ∑ i : Fin  j,
    (1 : ℚ) / (Nat.nth (· ∣ n) j - Nat.nth (· ∣ n) i )

/--
The sum $\sum_{1 \le i < \tau(n)} \frac{1}{d_{i + 1} - d_i}$ over consecutive
divisors of $n$.
-/
noncomputable abbrev sumDivisorInvConsecutiveDifference (n : ℕ) : ℝ :=
    ∑ i : Fin (n.divisors.card - 1),
    (1 : ℚ) / (Nat.nth (· ∣ n) (i + 1) - Nat.nth (· ∣ n) i)

/--
For a natural number n, let $1 = d_1 < \dotsc < d_{\tau(n)} = n$ denote the divisors of $n$
in increasing order.
Does it hold that
$\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i} \ll 1 + \sum_{1 \le i < \tau(n)}
 \frac{1}{d_{i + 1} - d_i}$
for $n \to \infty`, i.e.
$\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i} \in O \left( 1 + \sum_{1 \le i < \tau(n)}
 \frac{1}{d_{i + 1} - d_i}) \right)$?

This conjecture has been **disproved**:
- In September 2025, Terence Tao gave a conditional _negative_ answer assuming the prime tuples
  conjecture, see `erdos_884_false_of_hardy_littlewood` for this implication.
- Daniel Larsen subsequently gave an unconditional disproof.
-/
def Erdos884Prop : Prop :=
    sumDivisorInvPairwiseDifference ≪ 1 + sumDivisorInvConsecutiveDifference

/--
For a natural number n, let $1 = d_1 < \dotsc < d_{\tau(n)} = n$ denote the divisors of $n$
in increasing order.
Does it hold that
$\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i} \ll 1 + \sum_{1 \le i < \tau(n)}
 \frac{1}{d_{i + 1} - d_i}$
for $n \to \infty`, i.e.
$\sum_{1 \le i < j \le \tau(n)} \frac{1}{d_j - d_i} \in O \left( 1 + \sum_{1 \le i < \tau(n)}
 \frac{1}{d_{i + 1} - d_i}) \right)$?

This conjecture has been **disproved**:
- In September 2025, Terence Tao gave a conditional _negative_ answer assuming the prime tuples
  conjecture, see `erdos_884_false_of_hardy_littlewood` for this implication.
- Daniel Larsen subsequently gave an
  [unconditional disproof](https://github.com/Larsen-Daniel/Erdos-884/blob/main/884.pdf).

*Reference:* [erdosproblems.com/884](https://www.erdosproblems.com/884)
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/884/Erdos884.lean"]
theorem erdos_884 :
    answer(False) ↔ Erdos884Prop := by
  sorry

/--
In September 2025, Terence Tao gave a conditional _negative_ answer to Erdos conjecture 884,
disproving it under the assumption of the *Qualitative Hardy-Littlewood Conjecture*.
See [here](https://terrytao.wordpress.com/wp-content/uploads/2025/09/erdos-884.pdf).
The *qualitative* version of the conjecture only states that there are infinitely many tuples
of primes and does not require any asymptotical bounds and as such is a corollary of the general
form of the Hardy-Littlewood Conjecture.
We state the 'weaker' implication using general Hardy-Littlewood here, since this conjecture is
already formalized.
-/
@[category research solved, AMS 11]
theorem erdos_884_false_of_hardy_littlewood :
    ∀ (k : ℕ) (m : Fin k.succ → ℕ), HardyLittlewood.FirstHardyLittlewoodConjectureFor m
    → ¬Erdos884Prop := by
  sorry

end Erdos884


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
