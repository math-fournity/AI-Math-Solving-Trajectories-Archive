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
# Rational_variety

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Rational_variety)
-/

namespace NoetherProblem

/--
A rational field extension is a field extension `L/K` isomorphic
to a field of rational functions (in some arbitrary number of indeterminates.)
-/
class IsRationalExtension (K L ι : Type*)
    [Field K] [Field L] [Algebra K L] where
  pure_transcendental :
    Nonempty (L ≃ₐ[K] ((FractionRing (MvPolynomial ι K))))

/-- If the index set `ι` is empty, then `IsRationalExtension K L ι` means that
`K, L` are isomorphic as `K` algebras. -/
@[category test, AMS 12]
theorem rationalExtension_empty_index (K L ι : Type*) [Field K] [Field L] [Algebra K L] [IsEmpty ι]
    [IsRationalExtension K L ι] :
    Nonempty (L ≃ₐ[K] K) := by
  set a : L ≃ₐ[K] (FractionRing (MvPolynomial ι K)) :=
    Classical.choice IsRationalExtension.pure_transcendental
  set b : (MvPolynomial ι K) ≃ₐ[K] K := MvPolynomial.isEmptyAlgEquiv K ι
  set c : FractionRing (MvPolynomial ι K) ≃ₐ[K] K :=
    IsFractionRing.fieldEquivOfAlgEquiv K (FractionRing (MvPolynomial ι K)) K b
  apply Nonempty.intro (a.trans c)

/--
We say that a rational extension `L` of `K` has the _Noether Property_
if for any finite subgroup `H` of the Galois group of `L`, the fixed field
`L^H` is also a rational extension.
-/
def HasNoetherProperty (K L ι : Type) [Field K] [Field L] [Fintype ι]
    [Algebra K L] [IsRationalExtension K L ι] : Prop :=
  ∀ H : Subgroup (L ≃ₐ[K] L), Finite H → ∃ ι' : Type,
    IsRationalExtension K (IntermediateField.fixedField H) ι'

/--
The **Noether Problem**: let `L` be the field of rational functions in `n`
indeterminates over `K`. Is it true that `L/K` has the Noether property?

Solution: False.
-/
@[category research solved, AMS 12 14]
theorem noether_problem : answer(False) ↔ ∀ (K L ι G : Type)
    [Field K] [Field L] [Fintype ι] [Algebra K L] [IsRationalExtension K L ι],
    HasNoetherProperty K L ι := by
  sorry

/--
The Noether problem has a positive solution in the two indeterminate case.
-/
@[category research solved, AMS 12 14]
theorem noether_problem.variants.two {K L ι G : Type}
    [Field K] [Field L] [Fintype ι] [Algebra K L]
    [IsRationalExtension K L ι] (hι : Fintype.card ι = 2) :
    HasNoetherProperty K L ι := by
  sorry

/--
The Noether problem has a positive solution in the three indeterminate case.
-/
@[category research solved, AMS 12 14]
theorem noether_problem.variants.three {K L ι G : Type}
    [Field K] [Field L] [Fintype ι] [Algebra K L]
    [IsRationalExtension K L ι] (hι : Fintype.card ι = 3) :
    HasNoetherProperty K L ι := by
  sorry

/--
The Noether problem has a positive solution in the four indeterminate case.
-/
@[category research solved, AMS 12 14]
theorem noether_problem.variants.four {K L ι G : Type}
    [Field K] [Field L] [Fintype ι] [Algebra K L]
    [IsRationalExtension K L ι] (hι : Fintype.card ι = 4) :
    HasNoetherProperty K L ι := by
  sorry

/--
One can find a counterexample to the Noether Problem's claim by considering a
rational function field in 47 indeterminates.
-/
@[category research solved, AMS 12 14]
theorem noether_problem.variants.forty_seven :
    ∃ (K L ι G : Type)
    (_ :  Field K) (_ : Field L) (_ : Fintype ι) (_ : Algebra K L)
    (_ : IsRationalExtension K L ι),
    Fintype.card ι = 47 ∧ ¬ HasNoetherProperty K L ι := by
  sorry

end NoetherProblem


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
