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
# Busy Beaver

The Busy Beaver problem asks for the maximum number of steps that an n-state, 2-symbol Turing
machine can take before halting, when started on an empty tape.

*References:*

- [The Busy Beaver Challenge](https://wiki.bbchallenge.org/wiki/Main_Page)
-/

universe u v

open Turing BusyBeaver

namespace BusyBeaver

structure Candidate (n : ℕ) where
  Γ : Type
  Λ : Type
  Γ_fintype : Fintype Γ
  Γ_card : Fintype.card Γ = 2
  Γ_inhabited : Inhabited Γ
  Λ_fintype : Fintype Λ
  Λ_card : Fintype.card Λ = n
  Λ_inhabited : Inhabited Λ
  M : Machine Γ Λ
  M_isHalting : M.IsHalting

instance {n : ℕ} {M : Candidate n} : Fintype M.Γ := M.Γ_fintype
instance {n : ℕ} {M : Candidate n} : Fintype M.Λ := M.Λ_fintype
instance {n : ℕ} {M : Candidate n} : Inhabited M.Γ := M.Γ_inhabited
instance {n : ℕ} {M : Candidate n} : Inhabited M.Λ := M.Λ_inhabited

/--
`BB(n)` is the `n`-th Busy Beaver number.
*This is the maximum shifts function*, not the "number of ones function"
-/
noncomputable def BB (n : ℕ) : ℕ :=
  sSup { N | ∃ C : Candidate n, C.M.haltingNumber = N}

/--
To compute `BB n`, we need only consider machines with states and symbols indexed in `Fin`.
-/
@[category API, AMS 3]
theorem sanity_check (n : ℕ) [NeZero n] :
    BB n = sSup {N | ∃ (M : Machine (Fin 2) (Fin n)) (_ : M.IsHalting),
      M.haltingNumber = N} := by
  sorry

/-- The value of the Busy Beaver function for 1 state is 1. -/
@[category test, AMS 3]
theorem BB_1 : BB 1 = 1 := by
  sorry

/-- The value of the Busy Beaver function for 2 states is 6. -/
@[category textbook, AMS 3]
theorem BB_2 : BB 2 = 6 := by
  sorry

/-- The value of the Busy Beaver function for 3 states is 21. -/
@[category textbook, AMS 3]
theorem BB_3 : BB 3 = 21 := by
  sorry

/-- The value of the Busy Beaver function for 4 states is 107. -/
@[category textbook, AMS 3]
theorem BB_4 : BB 4 = 107 := by
  sorry

/-- The value of the Busy Beaver function for 5 states is 47176870. -/
@[category research solved, AMS 3]
theorem BB_5 : BB 5 = 47176870 := by
  sorry

/--
Determine the value of the Busy Beaver function at n = 6.
-/
@[category research open, AMS 3]
theorem BB_6 : BB 6 = answer(sorry) := by
  sorry

end BusyBeaver


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
