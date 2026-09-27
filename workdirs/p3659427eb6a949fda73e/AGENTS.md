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
# Erdős Problem 897

*References:*
- [erdosproblems.com/897](https://www.erdosproblems.com/897)
- [Ar25] Archivara Math Research Agent, [An Additive Counterexample: Erdős Problem 897](https://archivara.org/paper/df04f023-6ef0-4c52-bd12-18cdaa8f0741) (2025)
- [ArWu25] Aristotle, operated mostly by L. Wu, [Lean formalisation of Erdős problem 897](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean) (2025)
- [Wi70] E. Wirsing, A characterization of $\log n$ as an additive arithmetic function.
  Symposia Math. (1970), 45-57.
- [Wi81] E. Wirsing, Additive and completely additive functions with restricted growth.
  Recent progress in analytic number theory, Vol. 2 (Durham, 1979), 231--280 (1981).
-/
-- TODO(lezeau): add `ArithmeticFunction.IsAdditive` to `ForMathlib`

namespace Erdos897

/--
Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
if $(a,b)=1$ such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$.
Is it true that $\limsup_n (f(n+1)−f(n))/ \log n = ∞$?

The answer is no; this follows from a construction of Wirsing [Wi81], rediscovered by
Archivara [Ar25] and formalised in Lean by Aristotle [ArWu25].
-/
@[category research solved, AMS 11, formal_proof using lean4 at
  "https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean"]
theorem erdos_897.parts.i : answer(False) ↔ ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    Filter.atTop.limsup (fun (n : ℕ) => ((f (n+1) - f n) / (n : ℝ).log : EReal)) = ⊤ := by
  sorry

/--
Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
if $(a,b)=1$) such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$.
Is it true that $\limsup_n f(n+1)/ f(n) = ∞$?

The answer is no; the same counterexample is formalised in Lean by Aristotle [ArWu25].
-/
@[category research solved, AMS 11, formal_proof using lean4 at
  "https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos897.lean"]
theorem erdos_897.parts.ii : answer(False) ↔ ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    Filter.atTop.limsup (fun (n : ℕ) => (f (n+1) / f n : EReal)) = ⊤ := by
  sorry

/--
Wirsing [Wi70] proved that if $|f(n+1)−f(n)| ≤ C$ then $f(n) = c \log n + O(1)$ for some constant
$c$.
-/
@[category research solved, AMS 11]
theorem erdos_897.variants.log_growth
    (f : ℕ → ℝ)
    (hf : ∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b)
    (C : ℝ) (hf' : ∀ n, |f (n+1) - f n| ≤ C) :
    ∃ c, ∃ (O : ℕ → ℝ), O =O[Filter.atTop] (1 : ℕ → ℝ) ∧
      ∀ n, f n ≤ c*Real.log n + O n := by
  sorry


/--
Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
if $(a,b)=1$) such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$ and $f(p^k) = f(p)$
or $f(p^k) = kf(p)$.
Is it true that $\limsup_n (f(n+1)−f(n))/ \log n = ∞$?

The known counterexample does not satisfy either of these extra hypotheses, so this variant remains
open.
-/
@[category research open, AMS 11]
theorem erdos_897.variants.parts.i : answer(sorry) ↔ ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    (∀ k p, p.Prime → f (p^k) = f p) ∨ (∀ (k p : ℕ), p.Prime → f (p^k) = k*f p) →
    Filter.atTop.limsup (fun (n : ℕ) => ((f (n+1) - f n) / (n : ℝ).log : EReal)) = ⊤ := by
  sorry

/--
Let $f(n)$ be an additive function (so that $f(ab)=f(a)+f(b)$
if $(a,b)=1$) such that $\limsup_{p,k} f(p^k) / \log(p^k) = ∞$ and $f(p^k) = f(p)$
or $f(p^k) = kf(p)$.
Is it true that $\limsup_n f(n+1)/f(n) = ∞$?

The known counterexample does not satisfy either of these extra hypotheses, so this variant remains
open.
-/
@[category research open, AMS 11]
theorem erdos_897.variants.parts.ii : answer(sorry) ↔ ∀ (f : ℕ → ℝ),
    (∀ᵉ (a > 0) (b > 0), a.Coprime b → f (a * b) = f a + f b) →
    ((Filter.atTop ⊓ Filter.principal {(p, k) : ℕ × ℕ | p.Prime}).limsup
      (fun (p, k) => (f (p^k) / (p^k : ℝ).log : EReal)) = ⊤) →
    (∀ k p, p.Prime → f (p^k) = f p) ∨ (∀ (k p : ℕ), p.Prime → f (p^k) =

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
