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
# Beal conjecture

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Beal_conjecture)
-/

namespace BealConjecture

def bealConjecture : Prop := ∀ {A B C x y z : ℕ},
    A ≠ 0 → B ≠ 0 → C ≠ 0 → 2 < x → 2 < y → 2 < z →
    A^x + B^y = C^z → 1 < Finset.gcd {A, B, C} id

/--
The **Beal Conjecture**: if we are given positive integers $A, B, C, x, y, z$ such that
$x, y, z > 2$ and $A^x + B^y = C^z$ then $A, B, C$ have a common divisor.
-/
@[category research open, AMS 11]
theorem beal_conjecture : bealConjecture := by
  sorry

/--
The Beal Conjecture implies Fermat's last theorem
-/
@[category textbook, AMS 11]
theorem flt_of_beal_conjecture (H : bealConjecture) :
    FermatLastTheorem := by
  intro n hn x y z hx hy hz
  by_contra h
  apply mul_ne_zero (mul_ne_zero hx hy) hz
  by_contra H''
  obtain ⟨hx, hy, hz⟩ : x ≠ 0 ∧ y ≠ 0 ∧ z ≠ 0 := by aesop
  set G := Finset.gcd {x, y, z} id
  set x' := (x / G : ℕ)
  set y' := (y / G : ℕ)
  set z' := (z / G : ℕ)
  obtain ⟨hGx, hGy, hGz⟩ : G ∣ x ∧ G ∣ y ∧ G ∣ z := by
    refine ⟨?_, ?_, ?_⟩ <;> apply Finset.gcd_dvd (by aesop)
  obtain ⟨hx', hy', hz'⟩ : x' ≠ 0 ∧ y' ≠ 0 ∧ z' ≠ 0 := by
    refine ⟨?_, ?_, ?_⟩ <;>
      apply Nat.div_ne_zero_iff_of_dvd (by assumption) |>.mpr ⟨(by assumption), _⟩ <;> aesop
  have Hxyz' : x'^n + y'^n = z'^n := by
    rwa [Nat.div_pow hGx, Nat.div_pow hGy, Nat.div_pow hGz,
      ←Nat.add_div_of_dvd_right, Nat.div_left_inj (dvd_add _ _)]
    all_goals apply pow_dvd_pow_of_dvd ; assumption
  apply ne_of_lt <| H hx' hy' hz' hn hn hn Hxyz'
  rw [←Finset.gcd_div_id_eq_one (Finset.mem_insert_self x {y, z}) (by trivial),
    Finset.gcd_eq_gcd_image, Finset.image_insert, Finset.image_insert,
    Finset.image_singleton]

end BealConjecture


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
