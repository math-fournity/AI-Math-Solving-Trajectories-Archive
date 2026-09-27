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
# Erdős Problem 648

*References:*
- [erdosproblems.com/648](https://www.erdosproblems.com/648)
- [Er95c] Erdős, Paul, *Some problems in number theory*. Octogon Math. Mag. (1995), 3-5.
- [Ca25b] S. Cambie, *On Erdős problem #648*. arXiv:2503.22691 (2025).
-/

open Filter Asymptotics

namespace Erdos648

/-
Divergences from the hosted theorems (details in statements/648/draft.json):
- the sequence range follows the problem text, `2 ≤ a_1 < ⋯ < a_t < n` (`Set.Ico 2 n`);
  both hosted theorems allow `0 < m ≤ n` (`Set.Ioc 0 n`), which admits `1` and `n`.
- `P` is the FC-house `Nat.maxPrimeFac`; the hosted files define
  `P n = (n.primeFactors.max).getD 1`. The two agree on `2 ≤ m`.
- the sequence is a strictly monotone `a : Fin t → ℕ` (FC house shape); the hosted
  theorems use a `List ℕ` with `IsChain`.
-/

/--
`g n` is the largest `t` such that there exist integers `2 ≤ a 0 < a 1 < ⋯ < a (t - 1) < n`
whose greatest prime factors are strictly decreasing. -/
noncomputable def g (n : ℕ) : ℕ :=
  sSup {t | ∃ a : Fin t → ℕ, StrictMono a ∧ (∀ i, a i ∈ Set.Ico 2 n) ∧
    StrictAnti fun i => (a i).maxPrimeFac}

/--
Let $g(n)$ denote the largest $t$ such that there exist integers $2\leq a_1<a_2<\cdots <a_t <n$
such that $$P(a_1)>P(a_2)>\cdots >P(a_t)$$ where $P(m)$ is the greatest prime factor of $m$.
Estimate $g(n)$.

Stijn Cambie has proved [Ca25b] $$g(n) \asymp \left(\frac{n}{\log n}\right)^{1/2}.$$
Cambie further asks whether there exists a constant $c$ such that
$$g(n) \sim c \left(\frac{n}{\log n}\right)^{1/2}.$$
Cambie's proof shows that such a $c$ must satisfy $2\leq c\leq 2\sqrt{2}$.

The sequence $a_1<a_2<\cdots<a_t$ is packaged as a strictly monotone map `a : Fin t → ℕ`
with $2\leq a_i<n$, the greatest prime factor $P$ is `Nat.maxPrimeFac`, and $g(n)$ is the
supremum in `ℕ` of the achievable lengths $t$.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos648.lean"]
theorem erdos_648 :
    (fun n => (g n : ℝ)) =Θ[atTop] fun n => Real.sqrt ((n : ℝ) / Real.log (n : ℝ)) := by
  sorry

end Erdos648


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
