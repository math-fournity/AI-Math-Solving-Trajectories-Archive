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
# Lam--Litt conjecture

A conjecture of Lam and Litt on algebraic solutions of algebraic ODEs.

Let $g \in \mathbb{Q}(z, y_0, \dots, y_{n-1})$ be a rational function in
$n + 1$ variables. Let $f$ be a power series over $\mathbb{Q}$ such that
$f^{(n)}(z) = g(z, f(z), f'(z), \dots, f^{(n-1)}(z))$.
Also, assume that $g(0, f(0), f'(0), \dots, f^{(n-1)}(0))$ is defined.
Then the following are equivalent:

1) $f$ is algebraic over $\mathbb{Q}[z]$.
2) There exists $N$ such that for all $n$, the $n$-th coefficient of $f$ is in $\mathbb{Z}[1/N]$.
3) There exists an integer-valued function $\omega$ on the set of primes with
$\lim_{p \to \infty} \omega(p) / p = \infty$ such that, for each prime $p$,
the rational numbers $a_0, a_1, \dots, a_{\omega(p)}$ are in $\mathbb{Z}_{(p)}$.

The implication 1) => 2) is due to Eisenstein, and 2) => 3) is trivial.

*References:*
- [Litt's problem 1](https://www.problemsilike.com/1)
- Yeuk Hay Joshua Lam, Daniel Litt, "Algebraicity and integrality of solutions to differential equations",
  [arxiv/2501.13175](https://arxiv.org/abs/2501.13175)
- Gotthold Eisenstein. "Über eine allgemeine Eigenschaft der Reihen-Entwicklungen aller algebraischen Funktionen",
  Bericht der Königl. Preuss. Akademie der Wissenschaften zu Berlin, 1852

TODO:
- Lam-Litt conjecture implies Grothendieck p-curvature conjecture.
- Examples in Remark 1.1.3 and 1.1.5 on the conditions of the conjecture.
-/

open Real MvPolynomial PowerSeries

namespace LamLitt

/--
A power series $f$ is a solution of an algebraic ODE defined by the rational function
$g \in \mathbb{Q}(z, y_0, \dots, y_{n-1})$ if $f^{(n)}(z) = g(z, f(z), f'(z), \dots, f^{(n-1)}(z))$.
The variable indexed by `0 : Fin (n + 1)` corresponds to $z$, and the variable indexed by
`i.succ` corresponds to $y_i = f^{(i)}(z)$.
-/
def IsSolutionOfAlgebraicODE (n : ℕ) (f : PowerSeries ℚ) (g : MvRatFunc (Fin (n + 1)) ℚ) : Prop :=
  let pt : Fin (n + 1) → PowerSeries ℚ := Fin.cases X (fun i : Fin n ↦ derivativeFun^[i.val] f)
  ∃ p q : MvPolynomial (Fin (n + 1)) ℚ,
    q ≠ 0 ∧
    g = (algebraMap _ _ p) / (algebraMap _ _ q) ∧
    IsDefined (Fin (n + 1)) ℚ g (PowerSeries.constantCoeff ∘ pt) ∧
    derivativeFun^[n] f * MvPolynomial.aeval pt q = MvPolynomial.aeval pt p

def ℤAdjoinInvNat (N : ℕ) : Subalgebra ℤ ℚ := Algebra.adjoin ℤ {(1 / N : ℚ)}

/--
There exists $N$ such that for all $n$, the $n$-th coefficient of $f$ is in $\mathbb{Z}[1/N]$.
-/
def IsCoeffIntegralAdjointInvNat (f : PowerSeries ℚ) (N : ℕ) : Prop :=
  ∀ n : ℕ, coeff n f ∈ ℤAdjoinInvNat N

/--
For an integer-valued function $\omega$ on the set of primes and a sequence $a_n$ of rational
numbers, the condition $\omega$-integrality means that for each prime $p$, the rational numbers
$a_0, a_1, \dots, a_{\omega(p)}$ are in $\mathbb{Z}_{(p)}$, i.e. their denominators are not
divisible by $p$. When $\omega(p) < 0$ the constraint at $p$ is vacuous.
-/
def omegaIntegral (ω : Nat.Primes → ℤ) (a : ℕ → ℚ) : Prop :=
  ∀ p : Nat.Primes, ∀ j : ℕ, (j : ℤ) ≤ ω p → Nat.Coprime (a j).den p

/--
The growth condition on $\omega$: the ratio $\omega(p) / p$ tends to infinity as the prime $p$
tends to infinity, i.e. $\lim_{p \to \infty} \omega(p) / p = \infty$. Here the source filter is
`Filter.atTop` on the primes, obtained by pulling back `Filter.atTop` on $\mathbb{N}$ along the
coercion `Nat.Primes → ℕ`.
-/
def omegaSuperlinear (ω : Nat.Primes → ℤ) : Prop :=
  Filter.Tendsto (fun p : Nat.Primes ↦ (ω p : ℝ) / p)
    (Filter.comap (fun p : Nat.Primes ↦ (p : ℕ)) Filter.atTop) Filter.atTop

/--
Eisenstein's theorem (1852): an algebraic power series over $\mathbb{Q}[z]$ has bounded
denominators, i.e., there exists $N$ such that all coefficients lie in $\mathbb{Z}[1/N]$.
-/
@[category research solved, AMS 12 13]
theorem lam_litt.variants.eisenstein (f : PowerSeries ℚ) (hAlg : IsAlgebraic (Polynomial ℚ) f) :
    ∃ N : ℕ, IsCoeffIntegralAdjointInvNat f N := by
  sorry

/-- Every element of $\mathbb{Z}[1/N]$ has denominator coprime to any prime $p$ not in the
prime factor set of $N$ (vacuously, the case $N = 0$ gives $\mathbb{Z}[1/N] = \mathbb{Z}$). -/
@[category API, AMS 11]
private lemma den_coprime_of_mem_adjoinInvNat {N p : ℕ} (hp : p.Prime)
    (hpN : p ∉ N.primeFactors) {q : ℚ} (hq : q ∈ ℤAdjoinInvNat N) :
    Nat.Coprime q.den p := by
  induction hq using Algebra.adjoin_induction with
  | mem x hx =>
    rw [Set.mem_single

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
