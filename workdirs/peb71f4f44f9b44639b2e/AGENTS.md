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
# Erdős Problem 459

*References:*
- [erdosproblems.com/459](https://www.erdosproblems.com/459)
- [ErGr80] P. Erdős and R. L. Graham, *Old and new problems and results in combinatorial number
  theory*, Monographies de L'Enseignement Mathématique 28 (1980), p.91.
- [OEIS A289280](https://oeis.org/A289280)
-/

namespace Erdos459

/--
The function from the problem, in its equivalent form: `f u` is the smallest `v > u` all of whose
prime factors divide `u`. (Equivalently, `f u` is the largest `v` such that no `m ∈ (u, v)` is
composed entirely of primes dividing `u * v`.)
-/
noncomputable def f (u : ℕ) : ℕ := sInf {v | u < v ∧ v.primeFactors ⊆ u.primeFactors}

/--
Let $f(u)$ be the largest $v$ such that no $m\in (u,v)$ is composed entirely of primes dividing
$uv$. Estimate $f(u)$.

The estimate $u + 2 \le f(u) \le u^2$ holds for every $u \ge 2$. The upper bound is attained
when $u$ is prime, and the lower bound when $u = 2^k - 2$ with $k \ge 2$; Cambie further showed
that $f(n) = (1 + o(1))n$ for almost all $n$.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/Woett/Lean-files/blob/main/ErdosProblem459.lean"]
theorem erdos_459 {u : ℕ} (hu : 2 ≤ u) : u + 2 ≤ f u ∧ f u ≤ u ^ 2 := by
  sorry

/--
The upper bound $f u ≤ u ^ 2$ is attained exactly when `u` is prime: $f p = p ^ 2$.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/Woett/Lean-files/blob/main/ErdosProblem459.lean"]
theorem erdos_459.variants.upper_tight {p : ℕ} (hp : p.Prime) : f p = p ^ 2 := by
  sorry

end Erdos459


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
