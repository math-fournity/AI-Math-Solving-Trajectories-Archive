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
# Erdős Problem 202

*References:*
- [erdosproblems.com/202](https://www.erdosproblems.com/202)
- [BFV13] de la Bretèche, Régis and Ford, Kevin and Vandehey, Joseph, *On non-intersecting
  arithmetic progressions*. Acta Arith. (2013), 381-392.
- [Ch05] Chen, Yong-Gao, *On disjoint arithmetic progressions*. Acta Arith. (2005), 143-148.
- [Cr03b] Croot, III, Ernest S., *On non-intersecting arithmetic progressions*. Acta Arith.
  (2003), 233-238.
- [ErSz68] Erdős, P. and Szemerédi, E., *On a problem of P. Erdős and S. Stein*. Acta Arith.
  (1968), 85-90.
- [PaPh24] Park, Jinyoung and Pham, Huy Tuan, *A proof of the Kahn-Kalai conjecture*. J. Amer.
  Math. Soc. (2024), 235-243.
-/

open Filter Real

namespace Erdos202

/--
`f N` is the maximum possible `r` such that there are moduli $n_1<\cdots<n_r\leq N$ with
associated residues $a_i\pmod{n_i}$ whose congruence classes are disjoint.
-/
noncomputable def f (N : ℕ) : ℕ :=
  sSup {r : ℕ | ∃ n : Fin r → ℕ, ∃ a : Fin r → ℤ,
    StrictMono n ∧ (∀ i, 0 < n i ∧ n i ≤ N) ∧
    ∀ m : ℤ, ∀ i j : Fin r, m ≡ a i [ZMOD (n i : ℤ)] → m ≡ a j [ZMOD (n j : ℤ)] → i = j}

/--
Let $n_1<\cdots < n_r\leq N$ with associated $a_i\pmod{n_i}$ such that the congruence classes are
disjoint (that is, every integer is $\equiv a_i\pmod{n_i}$ for at most one $1\leq i\leq r$). How
large can $r$ be in terms of $N$?

Let $f(N)$ be the maximum possible $r$, and let $L(N)=\exp(\sqrt{\log N\log\log N})$.

This was proved by GPT-5.4 Pro (prompted by Ho Boon Suan), using the argument of [BFV13] together
with the resolution of the Kahn-Kalai conjecture by Park and Pham [PaPh24], so that
$$f(N)= N L(N)^{-1+o(1)}.$$
-/
@[category research solved, AMS 5 11, formal_proof using lean4 at "https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos202.lean"]
theorem erdos_202 : ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧
    ∀ᶠ N : ℕ in atTop, (f N : ℝ) = (N : ℝ) * scaleL N ^ (-1 + o N) := by
  sorry

/--
Erdős and Stein conjectured that $f(N)=o(N)$, which was proved by Erdős and Szemerédi [ErSz68].
-/
@[category research solved, AMS 5 11]
theorem erdos_202.variants.erdos_szemeredi :
    (fun N => (f N : ℝ)) =o[atTop] (fun N : ℕ => (N : ℝ)) := by
  sorry

end Erdos202


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
