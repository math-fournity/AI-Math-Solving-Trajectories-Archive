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
# Erdős Problem 540

*References:*
- [erdosproblems.com/540](https://www.erdosproblems.com/540)
- [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
  Modern Mathematics, Vol. III (1965), 196-244.
- [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of combinatorial
  theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971) (1973), 117-138.
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
  theory*. Monographies de L'Enseignement Mathematique (1980).
- [Ol68] Olson, John E., *An addition theorem modulo {$p$}*. J. Combinatorial Theory (1968), 45--52.
- [Ba12] Balandraud, Éric, *An addition theorem and maximal zero-sum free sets in
  $\mathbb{Z}/p\mathbb{Z}$*. Israel J. Math. (2012), 405-429.
- [HaZe96] Hamidoune, Yahya Ould and Zémor, Gilles, *On zero-free subset sums*. Acta Arith. (1996),
  143--152.
- [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
- [ErHe64] Erdős, P. and Heilbronn, H., *On the addition of residue classes
  mod $p$*. Acta Arith. (1964), 149--159.
- [Sz70] Szemerédi, E., *On a conjecture of Erdős and Heilbronn*. Acta Arith.
  (1970), 227-229.
-/

namespace Erdos540

/-- A finite set has a non-empty subset whose sum is zero. -/
def HasZeroSubsetSum {G : Type*} [AddCommMonoid G] (A : Finset G) : Prop :=
  ∃ S : Finset G, S ⊆ A ∧ S.Nonempty ∧ S.sum id = 0

/--
Is it true that if $A\subseteq \mathbb{Z}/N\mathbb{Z}$ has size $\gg N^{1/2}$ then there exists
some non-empty $S\subseteq A$ such that $\sum_{n\in S}n\equiv 0\pmod{N}$?

Szemerédi proved the answer is yes, in fact for arbitrary finite abelian groups.
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos540.lean"]
theorem erdos_540 : answer(True) ↔
    ∃ C : ℝ, 0 < C ∧
      ∀ (N : ℕ), 0 < N → ∀ A : Finset (ZMod N),
        C * Real.sqrt N ≤ A.card →
          HasZeroSubsetSum A := by
  sorry

end Erdos540


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
