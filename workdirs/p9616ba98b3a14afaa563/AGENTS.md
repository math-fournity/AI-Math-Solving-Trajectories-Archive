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
# Fernandes' conjecture on the 2-generation of even direct product permutation groups

*Reference:* [arxiv/2605.12342](https://arxiv.org/abs/2605.12342)
**Groups of permutations that are even on maximal proper subsets, and related monoids**
by *Vítor H. Fernandes*

For positive integers $m, n \ge 2$, let $\mathrm{S}_m \times \mathrm{S}_n$ be the direct product of
symmetric groups on $[m] = \{1, \dots, m\}$ and $[n'] = \{1', \dots, n'\}$. Define
$$
\Gamma_{m \oplus n} = \{(\sigma_1, \sigma_2) \in \mathrm{S}_m \times \mathrm{S}_n :
  \mathrm{sgn}(\sigma_1) = \mathrm{sgn}(\sigma_2)\}
$$
to be the index-$2$ subgroup of pairs of permutations with equal parity, i.e., those whose
product action on $[m] \cup [n']$ is an even permutation.

It is known that $\mathrm{rank}(\Gamma_{2 \oplus 2}) = 1$, $\mathrm{rank}(\Gamma_{3 \oplus 3}) = 3$,
$\mathrm{rank}(\Gamma_{4 \oplus 3}) = 3$, and $\mathrm{rank}(\Gamma_{4 \oplus 4}) = 3$.

**Conjecture 1 (Fernandes, 2026):** For all integers $m \ge n \ge 2$ such that
$(m, n) \notin \{(2,2), (3,3), (4,3), (4,4)\}$, the group $\Gamma_{m \oplus n}$ has
rank $2$ (i.e., is $2$-generated).
-/

namespace Arxiv.«2605.12342»

open Equiv.Perm

/--
The group homomorphism $(\sigma_1, \sigma_2) \mapsto \mathrm{sgn}(\sigma_1) \cdot \mathrm{sgn}(\sigma_2)^{-1}$
from $\mathrm{S}_m \times \mathrm{S}_n$ to $\{+1, -1\}$.

Its kernel is exactly $\Gamma_{m \oplus n}$.
-/
noncomputable def signDiffHom (m n : ℕ) : Equiv.Perm (Fin m) × Equiv.Perm (Fin n) →* ℤˣ :=
  (sign.comp (MonoidHom.fst _ _)) * (sign.comp (MonoidHom.snd _ _))⁻¹

/--
The subgroup $\Gamma_{m \oplus n} \le \mathrm{S}_m \times \mathrm{S}_n$ consisting of all pairs
$(\sigma_1, \sigma_2)$ of permutations with equal signature, i.e.
$\mathrm{sgn}(\sigma_1) = \mathrm{sgn}(\sigma_2)$.

This is the kernel of the sign-difference homomorphism
$(\sigma_1, \sigma_2) \mapsto \mathrm{sgn}(\sigma_1) \cdot \mathrm{sgn}(\sigma_2)^{-1}$,
and is an index-$2$ subgroup of $\mathrm{S}_m \times \mathrm{S}_n$.
-/
noncomputable def gammaSubgroup (m n : ℕ) : Subgroup (Equiv.Perm (Fin m) × Equiv.Perm (Fin n)) :=
  (signDiffHom m n).ker

/--
**Conjecture 1 (Fernandes, 2026):**
Let $m \ge n \ge 2$ be integers with $(m, n) \notin \{(2,2), (3,3), (4,3), (4,4)\}$.
Then the group
$$
\Gamma_{m \oplus n} = \{(\sigma_1, \sigma_2) \in \mathrm{S}_m \times \mathrm{S}_n :
  \mathrm{sgn}(\sigma_1) = \mathrm{sgn}(\sigma_2)\}
$$
has rank $2$, i.e., minimal generating set of size $2$.

Note: Fernandes states the conjecture for groups of exact rank $2$, which is why $(2,2)$
is in the exception list: $\Gamma_{2 \oplus 2} \cong C_2$ has rank $1$. The formalised
conclusion `∃ g₁ g₂, closure {g₁, g₂} = ⊤` encodes 2-generation (at most $2$ generators),
which $\Gamma_{2 \oplus 2}$ also satisfies. The other three exceptions $(3,3), (4,3), (4,4)$
have rank $3$ and are genuinely not 2-generated.
-/
@[category research open, AMS 20]
theorem conjecture_1 {m n : ℕ} (hm2 : 2 ≤ m) (hn2 : 2 ≤ n) (hmn : n ≤ m)
    (h_except : (m, n) ∉ ({(2, 2), (3, 3), (4, 3), (4, 4)} : Set (ℕ × ℕ))) :
    ∃ g₁ g₂ : gammaSubgroup m n, Subgroup.closure {g₁, g₂} = ⊤ := by
  sorry

/--
It is known that $\Gamma_{2 \oplus 2} \cong C_2$ has rank $1$: it is cyclic, generated by a
single element.
-/
@[category research solved, AMS 20]
theorem conjecture_1.variants.rank_2_2 :
    ∃ g : gammaSubgroup 2 2, Subgroup.closure {g} = ⊤ := by
  sorry

/--
It is known that $\Gamma_{3 \oplus 3}$ has rank $3$: it is not $2$-generated.
-/
@[category research solved, AMS 20]
theorem conjecture_1.variants.rank_3_3 :
    ∀ h₁ h₂ : gammaSubgroup 3 3, Subgroup.closure {h₁, h₂} ≠ ⊤ := by
  sorry

/--
It is known that $\Gamma_{4 \oplus 3}$ has rank $3$: it is not $2$-generated.
-/
@[category research solved, AMS 20]
theorem conjecture_1.variants.rank_4_3 :
    ∀ h₁ h₂ : gammaSubgroup 4 3, Subgroup.closure {h₁, h₂} ≠ ⊤ := by
  sorry

/--
It is known that $\Gamma_{4 \oplus 4}$ has rank $3$: it is not $2$-generated.
-/
@[category research solved, AMS 20]
theorem conjecture_1.variants.rank_4_4 :
    ∀ h₁ h₂ : gammaSubgroup 4 4, Subgroup.closure {h₁, h₂} ≠ ⊤ := by
  sorry

end Arxiv.«2605.12342»


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
