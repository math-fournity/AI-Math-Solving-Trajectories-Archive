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
# Erdős Problem 70

*Reference:* [erdosproblems.com/70](https://www.erdosproblems.com/70)

The 3-uniform (triple) partition relation $\mathfrak{c} \to (\beta, n)^3_2$
on the ordinal of the real numbers — the triple analogue of `OrdinalCardinalRamsey`
used in Problems 590–592.
-/

open Cardinal Ordinal
open scoped Cardinal

namespace Erdos70

universe u

/- ### The 3-uniform partition relation -/

/--
`OrdinalCardinalRamsey3 α β c` asserts the 3-uniform ordinal Ramsey property
$\alpha \to (\beta, c)^3_2$.

It states that for any 2-coloring of all 3-element subsets of (the ordinal type) $\alpha$,
one of the following must hold:
* There is a red-monochromatic subset of order type $\beta$: every 3-element sub-subset is
  colored red. (Formally: a set $s \subseteq \alpha$ with $\operatorname{typeLT} s = \beta$
  such that any three distinct elements of $s$ are colored red.)
* There is a blue-monochromatic subset of cardinality $c$: a set $s \subseteq \alpha$ with
  $\#s = c$ such that every three distinct elements of $s$ are colored blue.

The coloring is given as a predicate `isRed : α.ToType → α.ToType → α.ToType → Prop` on
ordered triples of distinct elements; to faithfully encode a coloring of *unordered*
3-element subsets we additionally require `isRed` to be invariant under permutation of
its three (distinct) arguments.
-/
def OrdinalCardinalRamsey3 (α β : Ordinal.{u}) (c : Cardinal.{u}) : Prop :=
  -- For any partition of 3-element subsets into red and blue:
  ∀ (isRed : α.ToType → α.ToType → α.ToType → Prop),
    -- The colouring is well-defined on *unordered* triples of distinct elements:
    (∀ x y z, x ≠ y → y ≠ z → x ≠ z →
      (isRed x y z ↔ isRed y x z) ∧ (isRed x y z ↔ isRed x z y)) →
    -- either there is a red-monochromatic subset of order type β
    (∃ s : Set α.ToType, typeLT s = β ∧ s.Triplewise isRed) ∨
    -- or there is a blue-monochromatic subset of cardinality c
    (∃ s : Set α.ToType, #s = c ∧ s.Triplewise (fun x y z ↦ ¬ isRed x y z))

/- ### The main open problem -/

/--
**Erdős Problem 70**: Let $\mathfrak{c}$ be the cardinality of the continuum,
let $\beta$ be a countable ordinal, and let $2 \le n < \omega$.
Is it true that $\mathfrak{c} \to (\beta, n)^3_2$?

Note: The cases $n \le 3$ are trivially true (see `omega_three`), so the
genuine content of the conjecture begins at $n = 4$.
-/
@[category research open, AMS 3]
theorem erdos_70 :
    answer(sorry) ↔
    ∀ᵉ (β : Ordinal.{0}) (n : ℕ) (_ : β.card ≤ ℵ₀) (_ : 2 ≤ n),
      OrdinalCardinalRamsey3 (𝔠).ord β n := by
  sorry

/- ### Variants -/

namespace erdos_70.variants

/--
**Erdős–Rado partial result**: $\mathfrak{c} \to (\omega + n, 4)^3_2$ for any
$2 \le n < \omega$. Positive partial answer to Problem 70 with $\beta = \omega + n$
and the blue side fixed at $4$.
-/
@[category research solved, AMS 3]
theorem erdos_rado (n : ℕ) (hn : 2 ≤ n) :
    OrdinalCardinalRamsey3 (𝔠).ord (ω + n) 4 := by
  sorry

/--
**First open case beyond Erdős–Rado**: $\mathfrak{c} \to (\omega \cdot 2, 4)^3_2$.

Erdős and Rado proved $\mathfrak{c} \to (\omega + n, 4)^3_2$ for every finite $n \ge 2$
(see `erdos_rado`), which covers all red ordinals below $\omega \cdot 2 = \omega + \omega$.
This variant asks whether the result extends to $\beta = \omega \cdot 2$, the simplest
countable ordinal not covered by their theorem.
-/
@[category research open, AMS 3]
theorem omega_times_two_four :
    answer(sorry) ↔ OrdinalCardinalRamsey3 (𝔠).ord (ω * 2) 4 := by
  sorry

/--
**Trivial boundary case**: $\mathfrak{c} \to (\omega, 3)^3_2$.

This is trivially true because in a 3-uniform hypergraph, a \"blue clique of size 3\"
consists of a single 3-element subset ($\binom{3}{3} = 1$), so the blue alternative
merely asks for one blue triple to exist. The proof splits into two cases:
- If any blue triple exists, it is itself a blue-monochromatic set of cardinality 3.
- If no blue triple exists, all triples are red, and since $\omega \le \mathfrak{c}$,
  any subset of order type $\omega$ is red-monochromatic.

The problem becomes non-trivial only for $n \ge 4$; see `omega_times_two_four` for
the simplest genuinely open case.
-/
@[category research solved, AMS 3, formal_proof using formal_conjectures at
"https://github.com/mo271/formal-conjectures/blob/c024db0fa3ac32c6dddcd6c28d7b0cd994dad580/FormalConjectures/ErdosProblems/70.lean#L126"]
theorem omega_three :
    answ

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
