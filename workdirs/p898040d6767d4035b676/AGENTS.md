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
# Erdős Problem 1055

*Reference:* [erdosproblems.com/1055](https://www.erdosproblems.com/1055)
-/

namespace Erdos1055

/-- A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
$2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor. -/
def IsOfClass : ℕ+ → ℕ → Prop := fun r ↦
  PNat.caseStrongInductionOn (p := fun (_ : ℕ+) ↦ ℕ → Prop) r
    (fun p ↦ (p + 1).primeFactors ⊆ {2, 3})
    (fun n H p ↦
      (∀ r ∈ (p + 1).primeFactors,
        ∃ (m : ℕ+) (hm : m ≤ n), H m hm r) ∧
      (∃ r ∈ (p + 1).primeFactors,
        ∀ (m : ℕ+) (hm : m ≤ n), H m hm r → m = n))

/-- A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
$2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
Show that for each $r$ there exists a prime $p$ of class $r$. -/
@[category textbook, AMS 11]
theorem exists_p (r : ℕ+) : ∃ p, p.Prime ∧ IsOfClass r p := by
  sorry


/-- A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
$2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
Let $p_r$ is the least prime in class $r$. -/
noncomputable def p (r : ℕ+) : ℕ :=
  open scoped Classical in
  Nat.find (exists_p r)

/-- A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
$2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
Are there infinitely many primes in each class?-/
@[category research open, AMS 11]
theorem erdos_1055 (r) : {p | p.Prime ∧ IsOfClass r p}.Infinite := by
  sorry

/-- A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
$2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
If $p_r$ is the least prime in class $r$, then how does $p_r^{1/r}$ behave?
Erdos conjectured that this tends to infinity. -/
@[category research open, AMS 11]
theorem erdos_1055.variants.erdos_limit :
    Filter.atTop.Tendsto (fun r ↦ (p r : ℝ) ^ (1 / r : ℝ)) Filter.atTop := by
  sorry

/-- A prime $p$ is in class $1$ if the only prime divisors of $p+1$ are
$2$ or $3$. In general, a prime $p$ is in class $r$ if every prime factor
of $p+1$ is in some class $\leq r-1$, with equality for at least one prime factor.
If $p_r$ is the least prime in class $r$, then how does $p_r^{1/r}$ behave?
Selfridge conjectured that this is bounded. -/
@[category research open, AMS 11]
theorem erdos_1055.variants.selfridge_limit :
    ∃ M, ∀ r, (p r : ℝ) ^ (1 / r : ℝ) ≤ M := by
  sorry

-- TODO(Paul-Lez): formalize the rest of the problems on the page.

end Erdos1055


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
