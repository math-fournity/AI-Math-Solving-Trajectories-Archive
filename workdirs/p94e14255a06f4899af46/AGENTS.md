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
# Conjectures in Complexity Theory

This file contains formal statements of some of the main open conjectures
in complexity theory, including

- the P vs NP problem
- the NP vs coNP problem

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/P_versus_NP_problem)
- Arora, Sanjeev, and Boaz Barak. Computational complexity: a modern approach.
  Cambridge University Press, 2009.
- [The Clay Institute](https://www.claymath.org/millennium/p-vs-np/)
-/

open Computability Turing

namespace ComplexityTheory

/--
The type of decision problems.

We define these as functions from lists of booleans to booleans,
implicitly assuming the usual encodings.
-/
abbrev DecisionProblem := List Bool → Bool

/--
The type of complexity classes. We define these as sets of decision problems.
-/
abbrev ComplexityClass := Set DecisionProblem

/--
A simple definition to abstract the notion of a poly-time Turing machine into a predicate.
-/
def IsComputableInPolyTime {α β : Type} (ea : FinEncoding α) (eb : FinEncoding β) (f : α → β) :=
  Nonempty (TM2ComputableInPolyTime ea eb f)

/--
The class P is the set of decision problems
decidable in polynomial time by a deterministic Turing machine.
-/
def P : ComplexityClass :=
  { L | IsComputableInPolyTime finEncodingListBool finEncodingBoolBool L }

/--
The class NP is the set of decision problems
such that there exists a polynomial `p` over ℕ and a poly-time Turing machine
where for all `x`, `L x = true` iff there exists a `w` of length at most `p (|x|)`
such that the Turing machine accepts the pair `(x,w)`.

See Definition 2.1 in Arora-Barak (2009).
-/
def NP : ComplexityClass :=
  { L | ∃ (p : Polynomial ℕ), ∃ R : (List Bool × List Bool) → Bool,
      IsComputableInPolyTime finEncodingListBoolProdListBool finEncodingBoolBool R ∧
      ∀ x, L x ↔ ∃ w : List Bool, w.length ≤ p.eval x.length ∧ R (x, w) }

/--
The class coNP is the set of decision problems
whose complements are in NP.
-/
def coNP : ComplexityClass :=
  { L | Lᶜ ∈ NP }

/--
**P ≠ NP**:

The conjecture that the complexity classes P and NP are not equal.
-/
@[category research open, AMS 68]
theorem P_ne_NP : P ≠ NP := by sorry

/--
**NP ≠ coNP**:

The conjecture that the complexity classes NP and coNP are not equal.
-/
@[category research open, AMS 68]
theorem NP_ne_coNP : NP ≠ coNP := by sorry

/--
The theorem that the set of complements of languages in P is itself P.

This can be proven by observing that the boolean negation function is computable in polynomial time,
and that compositions of poly-time computable functions are also poly-time computable.
-/
@[category textbook, AMS 68]
theorem coP_eq_P :
    { L | Lᶜ ∈ P } = P := by
  sorry

/--
The theorem that P is a subset of NP.

This can be proven by observing that for any language in P,
we can construct a verifier that ignores the witness and simply runs the poly-time decider for the
language.
-/
@[category textbook, AMS 68]
theorem P_subset_NP :
    P ⊆ NP := by
  sorry

/--
The theorem that P is a subset of coNP.
-/
@[category textbook, AMS 68]
theorem P_subset_coNP :
    P ⊆ coNP := by
  rw [coNP, ← coP_eq_P]
  simp only [Set.setOf_subset_setOf]
  intros L hL
  exact P_subset_NP hL

end ComplexityTheory


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
