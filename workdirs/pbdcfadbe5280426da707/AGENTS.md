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
# Oppermann's Conjecture

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Oppermann%27s_conjecture)
- [Luan Alberto Ferreira, *Real exponential sums over primes and prime gaps*](https://arxiv.org/abs/2307.08725)
-/

open Finset Filter

namespace Oppermann

/--
For every integer $x \ge 2$ there exists a prime between $x(x-1)$ and $x^2$.
-/
@[category research open, AMS 11]
theorem oppermann_conjecture.parts.i (x : ℕ) (hx : 2 ≤ x) :
    ∃ p ∈ Ioo (x * (x - 1)) (x^2), p.Prime := by
  sorry

/--
For every integer $x \ge 2$ there exists a prime between $x^2$ and $x(x+1)$.
-/
@[category research open, AMS 11]
theorem oppermann_conjecture.parts.ii (x : ℕ) (hx : 2 ≤ x) :
    ∃ p ∈ Ioo (x^2) (x * (x + 1)), p.Prime := by
  sorry

/--
**Oppermann's Conjecture**:
For every integer $x \ge 2$, the following hold:
- There exists a prime between $x(x-1)$ and $x^2$.
- There exists a prime between $x^2$ and $x(x+1)$.
-/
@[category research open, AMS 11]
theorem oppermann_conjecture (x : ℕ) (hx : 2 ≤ x) :
    (∃ p ∈ Ioo (x * (x - 1)) (x^2), p.Prime) ∧
    (∃ p ∈ Ioo (x^2) (x * (x + 1)), p.Prime) := by
  sorry

/-- Oppermann's conjecture implies Brocard's conjecture. -/
@[category textbook, AMS 11]
theorem oppermann_implies_brocard (n : ℕ) (hn : 1 ≤ n) (P : type_of% oppermann_conjecture) :
    letI prev := n.nth Nat.Prime
    letI next := (n+1).nth Nat.Prime
    4 ≤ ((Ioo (prev ^ 2) (next ^ 2)).filter Nat.Prime).card := by
  set prev := n.nth Nat.Prime with hprev_def
  set next := (n+1).nth Nat.Prime with hnext_def
  have hprev_prime : prev.Prime := Nat.prime_nth_prime n
  have hnext_prime : next.Prime := Nat.prime_nth_prime (n+1)
  have hprev_ge : 3 ≤ prev := Nat.nth_prime_one_eq_three ▸
    (Nat.nth_le_nth Nat.infinite_setOf_prime).mpr hn
  have hlt : prev < next :=
    Nat.nth_strictMono Nat.infinite_setOf_prime (Nat.lt_succ_self n)
  have hgap : prev + 2 ≤ next := by
    rcases hprev_prime.odd_of_ne_two (by omega) with ⟨k, hk⟩
    rcases hnext_prime.odd_of_ne_two (by omega) with ⟨m, hm⟩
    omega
  obtain ⟨_, p1, hp1mem, hp1p⟩ := P prev (by omega)
  obtain ⟨⟨p2, hp2mem, hp2p⟩, p3, hp3mem, hp3p⟩ := P (prev+1) (by omega)
  obtain ⟨p4, hp4mem, hp4p⟩ := (P (prev+2) (by omega)).1
  simp only [Finset.mem_Ioo, show prev + 1 - 1 = prev from rfl,
    show prev + 2 - 1 = prev + 1 from rfl, show prev + 1 + 1 = prev + 2 from rfl]
    at hp1mem hp2mem hp3mem hp4mem
  have hsq : (prev + 2)^2 ≤ next^2 := Nat.pow_le_pow_left hgap 2
  have hsq1 : (prev + 1)^2 ≤ next^2 := Nat.pow_le_pow_left (by omega) 2
  have hb0 : prev * (prev + 1) < (prev + 1)^2 := by nlinarith
  have hb1 : (prev + 1) * (prev + 2) < (prev + 2)^2 := by nlinarith
  have h12 : p1 < p2 := by linarith [hp1mem.2, hp2mem.1]
  have h23 : p2 < p3 := by linarith [hp2mem.2, hp3mem.1]
  have h34 : p3 < p4 := by linarith [hp3mem.2, hp4mem.1]
  refine ((show ({p1, p2, p3, p4} : Finset ℕ).card = 4 from ?_) ▸
    Finset.card_le_card (s := {p1, p2, p3, p4}) ?_)
  · simp [Finset.card_insert_of_notMem, h12.ne, (h12.trans h23).ne,
      (h12.trans (h23.trans h34)).ne, h23.ne, (h23.trans h34).ne, h34.ne]
  · intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl | rfl | rfl <;>
      refine Finset.mem_filter.mpr ⟨Finset.mem_Ioo.mpr ⟨?_, ?_⟩, by assumption⟩ <;>
      linarith [hp1mem.1, hp1mem.2, hp2mem.1, hp2mem.2, hp3mem.1, hp3mem.2,
        hp4mem.1, hp4mem.2, hb0, hb1, hsq, hsq1]

/-- Oppermann's conjecture implies Legendre's conjecture. -/
@[category textbook, AMS 11]
theorem oppermann_implies_legendre (n : ℕ) (hn : 1 ≤ n) (P : type_of% oppermann_conjecture) :
    ∃ p ∈ Ioo (n ^ 2) ((n + 1) ^ 2), p.Prime := by
  obtain ⟨⟨p, ph⟩, _⟩ := P (n + 1) (by simpa)
  use p
  refine ⟨Finset.Ioo_subset_Ioo_left ?_ ph.1, ph.2⟩
  push_cast [sq, add_one_mul,le_self_add]

/--
Ferreira proved that Oppermann's conjecture is true for sufficiently large x.
-/
@[category research solved, AMS 11]
theorem oppermann_conjecture.ferreira_large_x : ∀ᶠ x in atTop,
    (∃ p ∈ Ioo (x * (x - 1)) (x^2), p.Prime) ∧
    (∃ p ∈ Ioo (x^2) (x * (x + 1)), p.Prime) := by
  sorry

end Oppermann


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
