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
# Ben Green's Open Problem 5

*References:*
- [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.5)
- [BaSo85] Babai L, Sós VT. Sidon sets in groups and induced subgraphs of Cayley graphs.
  European Journal of Combinatorics. 1985 Jun 1;6(2):101-14.
- [Ke97] Kedlaya, K. S., *Large product-free subsets of finite groups*, J. Combin. Theory
  Ser. A 77 (1997), no. 2, 339–343.
- [Ke09] Kedlaya, K. S., *Product-free subsets of groups, then and now*, Contemp. Math., 479,
  American Mathematical Society, Providence, RI, 2009, 169–177.
- [Go08] Gowers, W. T., *Quasirandom groups*, Combin. Probab. Comput. 17 (2008), no. 3,
  363–387.
-/

open scoped MatrixGroups

local notation "SL₂" p => SL(2, ZMod p)

namespace Green5

/--
Which finite groups have the smallest biggest product-free sets?

We formalise this as: determine the supremum of exponents $\alpha$ such that every nontrivial
finite group of order $n$ contains a product-free set of size $\geq c n^{\alpha}$ for some
absolute constant $c > 0$. (The trivial group is excluded since its only product-free subset
is empty.) Kedlaya [Ke97] showed that $\alpha = 11/14$ is admissible, and Green suggests this
exponent may well be sharp; the candidate extremal family is the Ree groups ${}^2G_2(q)$,
$q = 3^{2m+1}$.
-/
@[category research open, AMS 5 20]
theorem green_5 :
    IsLUB {α : ℝ | ∃ c > (0 : ℝ), ∀ (G : Type) [Group G] [Fintype G], Nontrivial G →
      ∃ S : Finset G, IsProductFree (S : Set G) ∧
        c * (Fintype.card G : ℝ) ^ α ≤ (S.card : ℝ)}
      answer(sorry) := by
  sorry

/--
Kedlaya [Ke97] observed, refining some work of Babai and Sós [BaSo85], that it follows from the
classification of finite simple groups that every finite group $G$ of order $n$ has a
product-free subset of size $\gg n^{11/14}$.
-/
@[category research solved, AMS 5 20]
theorem green_5.variants.kedlaya :
    ∃ c > (0 : ℝ), ∀ (G : Type) [Group G] [Fintype G], Nontrivial G →
      ∃ S : Finset G, IsProductFree (S : Set G) ∧
        c * (Fintype.card G : ℝ) ^ ((11 : ℝ) / 14) ≤ (S.card : ℝ) := by
  sorry

-- TODO(theebayuser): implement Ree groups variant (candidate sharp example for `green_5`)

/--
A good model problem would be to determine the largest product-free subsets of
$\mathrm{SL}_2(\mathbb{F}_p)$.
-/
@[category research open, AMS 5 20]
theorem green_5.variants.sl_two (p : ℕ) [Fact p.Prime] :
    let S : Finset (SL₂ p) := answer(sorry)
    MaximalFor (IsProductFree (M := SL₂ p)) Set.ncard (S : Set (SL₂ p)) := by
  sorry

/--
For the largest product-free subsets of $\mathrm{SL}_2(\mathbb{F}_p)$ of order $n$, the
best-known upper bound is $O(n^{8/9})$, due to Gowers [Go08].
-/
@[category research solved, AMS 5 20]
theorem green_5.variants.gowers_sl_two :
    ∃ C > (0 : ℝ), ∀ (p : ℕ) [Fact p.Prime], ∀ S : Finset (SL₂ p),
      IsProductFree (S : Set (SL₂ p)) →
      (S.card : ℝ) ≤ C * (Fintype.card (SL₂ p) : ℝ) ^ ((8 : ℝ) / 9) := by
  sorry

end Green5


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
