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
# Erdős Problem 1113

*References:*
- [erdosproblems.com/1113](https://www.erdosproblems.com/1113)
- [ErGr80] Erdős, P. and Graham, R. L., Old and New Problems and Results in Combinatorial
  Number Theory. Monographie de l'Enseignement Mathématique, No. 28 (1980).
- [Si60] Sierpiński, W., Elementary Theory of Numbers. Państwowe Wydawnictwo Naukowe,
  Warsaw (1960).
- [FFK08] Filaseta, M., Finch, C., and Kozek, M., On powers associated with Sierpiński numbers,
  Riesel numbers and Polignac's conjecture. Journal of Number Theory 128 (2008), 1916–1940.

A positive odd integer $k$ is a *Sierpiński number* if $k \cdot 2^n + 1$ is composite for all
$n \geq 0$. A *covering set* for $k$ is a finite set of primes $P$ such that every number of
the form $k \cdot 2^n + 1$ is divisible by at least one prime in $P$.

Sierpiński (1960) proved that infinitely many Sierpiński numbers exist using covering systems.
The smallest known Sierpiński number is 78557 (Selfridge). Erdős and Graham conjectured that
there exist Sierpiński numbers with no finite covering set. A negative answer would imply
infinitely many Fermat primes.

Note: The notion of a covering set for a Sierpiński number is closely related to a
`CoveringSystem` of $\mathbb{Z}$ (see
`FormalConjecturesForMathlib.NumberTheory.CoveringSystem`): a finite covering set of primes
for $k$ works because the exponents $n$ for which each prime divides $k \cdot 2^n + 1$ form
residue classes whose union covers all of $\mathbb{Z}$, i.e. a covering system.

See also Erdős Problems [203](https://www.erdosproblems.com/203) and
[276](https://www.erdosproblems.com/276).
-/

namespace Erdos1113

/--
A *covering set* for a positive odd integer $k$ is a finite set of primes $P$ such that every
number of the form $k \cdot 2^n + 1$ is divisible by at least one prime in $P$.
-/
def HasFinitePrimeCoveringSet (k : ℕ) : Prop :=
  ∃ P : Finset ℕ, (∀ p ∈ P, p.Prime) ∧ ∀ n, ∃ p ∈ P, p ∣ (k * 2 ^ n + 1)

/--
Sierpiński [Si60] proved that there are infinitely many Sierpiński numbers, using covering
systems to construct suitable covering sets for any $k$ satisfying a certain congruence.
-/
@[category research solved, AMS 11]
theorem erdos_1113.variants.infinitely_many_sierpinski :
    Set.Infinite {k : ℕ | k.IsSierpinskiNumber} := by
  sorry

/--
**Erdős Problem 1113.** Do there exist Sierpiński numbers that possess no finite covering set
of primes?

Erdős and Graham [ErGr80] conjectured that the answer is yes. A negative answer would imply
that there are infinitely many Fermat primes.
-/
@[category research open, AMS 11]
theorem erdos_1113 :
    answer(sorry) ↔
      ∃ k, k.IsSierpinskiNumber ∧ ¬ HasFinitePrimeCoveringSet k := by
  sorry

/--
**Filaseta–Finch–Kozek conjecture (2008).** Every Sierpiński number is either a perfect power
or possesses a finite covering set of primes.
-/
@[category research open, AMS 11]
theorem erdos_1113.variants.filaseta_finch_kozek :
    ∀ k, k.IsSierpinskiNumber →
      k.IsPerfectPower ∨ HasFinitePrimeCoveringSet k := by
  sorry

end Erdos1113


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
