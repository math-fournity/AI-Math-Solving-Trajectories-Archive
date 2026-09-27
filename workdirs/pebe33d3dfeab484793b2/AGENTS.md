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
# Jacobian conjecture

*Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Jacobian_conjecture)
-/

namespace JacobianConjecture

section Prelims

variable {k : Type*} [CommRing k]
variable {σ τ ι : Type*}

variable (k σ τ) in

/-- The type of regular functions from $k^σ$ to $k^τ$. -/
abbrev RegularFunction := τ → MvPolynomial σ k

namespace RegularFunction

/-- The Jacobian of a vector valued polynomial function, viewed as a polynomial. -/
noncomputable def Jacobian (F : RegularFunction k σ τ) :
    Matrix σ τ (MvPolynomial σ k) :=
  Matrix.of fun i j => MvPolynomial.pderiv i (F j)

/-- The composition of two vector valued polynomial functions. -/
noncomputable def comp
    (F : RegularFunction k σ τ) (G : RegularFunction k τ ι) :
    RegularFunction k σ ι :=
  fun (i : ι) ↦ MvPolynomial.bind₁ F (G i)

variable (k σ) in
noncomputable def id : RegularFunction k σ σ := MvPolynomial.X

/-- The evaluation of a regular function `f` over `k` at some point `a`
with coordinates in some algebra over `k`-/
noncomputable def aeval {σ τ : Type*} {S₁ : Type*} [CommSemiring S₁] [Algebra k S₁]
    (F : RegularFunction k σ τ) : (σ → S₁) → τ → S₁ :=
  fun a t ↦ MvPolynomial.aeval a (F t)

/--`aeval` is compatible with composition of regular functions. -/
@[category API, AMS 14]
lemma comp_aeval
    {σ τ ι : Type*}
    (F : RegularFunction k σ τ) (G : RegularFunction k τ ι)
    (a : σ → k) : (F.comp G).aeval a = G.aeval (F.aeval a) := by
  ext i
  rw [aeval, comp, MvPolynomial.aeval_bind₁, ←aeval]
  rfl

end RegularFunction

end Prelims

section Conjecture

open RegularFunction MvPolynomial

variable (k : Type*)

name_poly_vars X, Y, Z over k

/-- Alpöge/Fable's counterexample: a polynomial self-map of `k³` with Jacobian
determinant `-2` which is not injective. -/
noncomputable abbrev F [CommRing k] : RegularFunction k (Fin 3) (Fin 3) :=
  ![(1 + X * Y)^3 * Z + Y ^ 2 * (1 + X * Y) * (4 + 3 * X * Y),
    Y + 3 * X * (1 + X * Y) ^ 2 * Z + 3 * X * Y ^ 2 * (4 + 3 * X * Y),
    2 * X - 3 * X ^ 2 * Y - X ^ 3 * Z]

/-- A variant of Alpöge/Fable's counterexample: a polynomial self-map of `k³` with Jacobian
determinant `1` which is not injective. -/
noncomputable abbrev G [CommRing k] : RegularFunction k (Fin 3) (Fin 3) :=
  ![(1 + 2 * X * Y) ^ 3 * Z + 4 * Y ^ 2 * (1 + 2 * X * Y) * (2 + 3 * (X * Y)),
    Y + 3 * X * (1 + 2 * X * Y) ^ 2 * Z + 12 * X * Y ^ 2 * (2 + 3 * (X * Y)),
    -X + 3 * X ^ 2 * Y + X ^ 3 * Z]


@[category API, AMS 14]
lemma det_jacobian_F [CommRing k] : (F k).Jacobian.det = -2 := by
  simp only [Jacobian, F, Fin.isValue, ← map_ofNat (C : k →+* MvPolynomial (Fin 3) k),
    Matrix.det_fin_three, Matrix.of_apply, Matrix.cons_val_zero, map_add, Derivation.leibniz,
    pderiv_X, ne_eq, Fin.reduceEq, not_false_eq_true, Pi.single_eq_of_ne, smul_eq_mul, mul_zero,
    Derivation.leibniz_pow, Nat.add_one_sub_one, Derivation.map_one_eq_zero, one_ne_zero,
    Pi.single_eq_same, mul_one, zero_add, nsmul_eq_mul, Nat.cast_ofNat, derivation_C, add_zero,
    pow_one,  Matrix.cons_val_one, zero_ne_one, Matrix.cons_val_two, Nat.succ_eq_add_one,
    Nat.reduceAdd, Matrix.tail_cons, Matrix.head_cons, map_sub, sub_self, zero_sub, mul_neg,
    sub_zero, neg_mul, sub_neg_eq_add]
  simp only [map_ofNat]
  ring

@[category API, AMS 14]
lemma det_jacobian_G [CommRing k] : (G k).Jacobian.det = 1 := by
  simp only [G, Jacobian, ← map_ofNat (C : k →+* MvPolynomial (Fin 3) k), Matrix.det_fin_three,
    Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons, map_add, map_neg, Derivation.map_one_eq_zero, pderiv_mul,
    pderiv_pow, pderiv_C, pderiv_X_self, pderiv_X_of_ne, ne_eq, Fin.reduceEq, not_false_eq_true]
  simp only [map_ofNat]
  ring

/-- `F` identifies the two distinct points `(0, 0, -1/4)` and `(1, -3/2, 13/2)`. -/
@[category API, AMS 14]
lemma aeval_F_eq [Field k] [CharZero k] :
    (F k).aeval ![(0 : k), 0, -1/4] = (F k).aeval ![(1 : k), -3/2, 13/2]  := by
  funext i
  fin_cases i <;> simp [RegularFunction.aeval] <;> grind

/-- `G` identifies the two distinct points `(1, 0, 1)` and `(0, 3, -71)`. -/
@[category API, AMS 14]
lemma aeval_G_eq [CommRing k] :
    (G k).aeval ![1, 0, (1 : k)] = (G k).aeval ![0, 3, -71] := by
  funext i
  fin_cases i <;> simp [RegularFunction.aeval]; grind

/-- The predicate that the Jacobian conjecture holds for a given field and variabl

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
