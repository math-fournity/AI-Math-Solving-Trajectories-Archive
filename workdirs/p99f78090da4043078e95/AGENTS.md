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
# Erdős Problem 337

*References:*
- [erdosproblems.com/337](https://www.erdosproblems.com/337)
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
  theory*. Monographies de L'Enseignement Mathematique (1980).
- [ErGr80b] Erdős, P. and Graham, R. L., *On bases with an exact order*. Acta Arith. (1980),
  201-207.
- [RT85] Ruzsa, I. Z. and Turjányi, S., *A note on additive bases of integers*. Publ. Math.
  Debrecen (1985), 101-104.
- [Tu84] Turjányi, S., *A note on basis sequences*. Topics in classical number theory, Vol. I, II
  (Budapest, 1981) (1984), 1571-1576.
-/

namespace Erdos337

open Filter Set Asymptotics

open scoped Pointwise

/--
Let $A\subseteq \mathbb{N}$ be an additive basis (of any finite order) such that
$\lvert A\cap \{1,\ldots,N\}\rvert=o(N)$. Is it true that
$$
\lim_{N\to \infty}\frac{\lvert (A+A)\cap \{1,\ldots,N\}\rvert}
{\lvert A\cap \{1,\ldots,N\}\rvert}=\infty?
$$

The answer is no, and a counterexample was provided by Turjányi [Tu84]. This was generalised (to
the replacement of $A+A$ by the $h$-fold sumset $hA$ for any $h\geq 2$) by Ruzsa and Turjányi
[RT85].

"Additive basis" is `Set.IsAsymptoticAddBasis`: some finite $h$ has $hA$ containing every
sufficiently large integer. The exact notion `Set.IsAddBasis`, which asks that $hA$ be all of
$\mathbb{N}$, would force $0, 1 \in A$ and is not the class these results are about.

The linked file states the basis hypothesis as `∃ N₀, Set.Ici N₀ ⊆ iterated_sumset A k` and
indexes both counting functions by a real $x$ through $\lfloor x\rfloor$, where the counting
functions here are indexed by $N : \mathbb{N}$.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos337.lean"]
theorem erdos_337 : answer(False) ↔
    ∀ A : Set ℕ, A.IsAsymptoticAddBasis →
      (fun N : ℕ ↦ ((A ∩ Icc 1 N).ncard : ℝ)) =o[atTop] (fun N : ℕ ↦ (N : ℝ)) →
      Tendsto (fun N : ℕ ↦ (((A + A) ∩ Icc 1 N).ncard : ℝ) / ((A ∩ Icc 1 N).ncard : ℝ))
        atTop atTop := by
  sorry

/--
This was generalised (to the replacement of $A+A$ by the $h$-fold sumset $hA$ for any $h\geq 2$)
by Ruzsa and Turjányi [RT85].
-/
@[category research solved, AMS 5 11]
theorem erdos_337.variants.h_fold : ∀ h : ℕ, 2 ≤ h →
    ∃ A : Set ℕ, A.IsAsymptoticAddBasis ∧
      (fun N : ℕ ↦ ((A ∩ Icc 1 N).ncard : ℝ)) =o[atTop] (fun N : ℕ ↦ (N : ℝ)) ∧
      ¬ Tendsto (fun N : ℕ ↦
          ((h • A ∩ Icc 1 N).ncard : ℝ) / ((A ∩ Icc 1 N).ncard : ℝ))
        atTop atTop := by
  sorry

/--
Ruzsa and Turjányi do prove (under the same hypotheses) that
$$
\lim_{N\to \infty}\frac{\lvert (A+A+A)\cap \{1,\ldots,3N\}\rvert}
{\lvert A\cap \{1,\ldots,N\}\rvert}=\infty,
$$
-/
@[category research solved, AMS 5 11]
theorem erdos_337.variants.three_fold :
    ∀ A : Set ℕ, A.IsAsymptoticAddBasis →
      (fun N : ℕ ↦ ((A ∩ Icc 1 N).ncard : ℝ)) =o[atTop] (fun N : ℕ ↦ (N : ℝ)) →
      Tendsto (fun N : ℕ ↦
          (((A + A + A) ∩ Icc 1 (3 * N)).ncard : ℝ) / ((A ∩ Icc 1 N).ncard : ℝ))
        atTop atTop := by
  sorry

/--
Ruzsa and Turjányi do prove (under the same hypotheses) that
$$
\lim_{N\to \infty}\frac{\lvert (A+A+A)\cap \{1,\ldots,3N\}\rvert}
{\lvert A\cap \{1,\ldots,N\}\rvert}=\infty,
$$
and conjecture that the same should be true with $(A+A)\cap \{1,\ldots,2N\}$ in the numerator.
-/
@[category research open, AMS 5 11]
theorem erdos_337.variants.ruzsa_turjanyi :
    ∀ A : Set ℕ, A.IsAsymptoticAddBasis →
      (fun N : ℕ ↦ ((A ∩ Icc 1 N).ncard : ℝ)) =o[atTop] (fun N : ℕ ↦ (N : ℝ)) →
      Tendsto (fun N : ℕ ↦
          (((A + A) ∩ Icc 1 (2 * N)).ncard : ℝ) / ((A ∩ Icc 1 N).ncard : ℝ))
        atTop atTop := by
  sorry

end Erdos337


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
