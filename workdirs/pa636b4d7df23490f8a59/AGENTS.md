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
# Decidability of reachability for branching vector addition systems

A *branching vector addition system* (BVAS) of dimension `d` is given by a finite
list of *axioms*, a finite list of *unary rules*, and a finite list of *binary
rules*, each of which is a vector in `ℤ^d`. A *configuration* is a vector in `ℕ^d`,
which here is represented as a vector `v ∈ ℤ^d` subject to `0 ≤ v`. The set of
*reachable* configurations is defined inductively:

* every axiom that is a valid configuration (i.e. lies in `ℕ^d`) is reachable;
* if `v` is a reachable configuration, `r` is a unary rule and `v + r ∈ ℕ^d`, then
  `v + r` is reachable;
* if `v₁, v₂` are both reachable configurations, `r` is a binary rule and
  `v₁ + v₂ + r ∈ ℕ^d`, then `v₁ + v₂ + r` is reachable.

Modelling axioms as vectors in `ℤ^d` and only counting the non-negative ones as
reachable yields the same set of reachable configurations as the usual definition
in which axioms are required to lie in `ℕ^d`.

Branching vector addition systems are distinguished from ordinary vector addition systems (VAS) by allowing binary rules. VAS reachability is known to be decidable.

*References:*
- [The covering and boundedness problems for branching vector addition systems](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2009.2317)
  (*Stéphane Demri, Marcin Jurdziński, Oded Lachish, Ranko Lazić*, FSTTCS 2009)
  Gives a similar definition of BVAS, and compares it to related equivalent definitions.
- [On the Reachability Problem for Two-Dimensional Branching VASS](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.22)
  by *Clotilde Bizière, Thibault Hilaire, Jérôme Leroux, Grégoire Sutre*, MFCS 2025, which
  settles the two-dimensional case and states that "the decidability status of the reachability
  problem for BVASS remains open in higher dimensions".
- [The General Vector Addition System Reachability Problem by Presburger Inductive
  Invariants](https://arxiv.org/abs/1009.1076) by *Jérôme Leroux* (2010), for the decidability
  of reachability for ordinary VAS.
- [Solving the Reachability Problem for Branching Vector Addition Systems via Semilinear
  Inductive Invariants](https://arxiv.org/abs/2607.09558) by *Clotilde Bizière, Jérôme Leroux,
  Grégoire Sutre* (2026), a recent preprint claiming a positive resolution to the conjecture:
  reachability for branching vector addition systems is decidable.
-/

namespace BranchingVAS

/--
A branching vector addition system of dimension `d`.
-/
structure Bvas (d : ℕ) where
  axioms : List (Fin d → ℤ)
  unaryRules : List (Fin d → ℤ)
  binaryRules : List (Fin d → ℤ)

instance {d : ℕ} : Primcodable (Bvas d) :=
  .ofEquiv (List (Fin d → ℤ) × List (Fin d → ℤ) × List (Fin d → ℤ))
    { toFun := fun b => (b.axioms, b.unaryRules, b.binaryRules)
      invFun := fun p => ⟨p.1, p.2.1, p.2.2⟩
      left_inv := fun _ => rfl
      right_inv := fun _ => rfl }

/-- The reachable configurations of a branching vector addition system. -/
inductive Bvas.Reachable {d : ℕ} (b : Bvas d) : (Fin d → ℤ) → Prop
  | base {v : Fin d → ℤ} (hmem : v ∈ b.axioms) (hcfg : 0 ≤ v) : b.Reachable v
  | unary {v r w : Fin d → ℤ} (hv : b.Reachable v) (hr : r ∈ b.unaryRules)
      (hcfg : 0 ≤ w) (hw : w = v + r) : b.Reachable w
  | binary {v₁ v₂ r w : Fin d → ℤ} (hv₁ : b.Reachable v₁) (hv₂ : b.Reachable v₂)
      (hr : r ∈ b.binaryRules) (hcfg : 0 ≤ w) (hw : w = v₁ + v₂ + r) : b.Reachable w

/--
The reachability problem for branching vector addition systems is decidable.

That is, is the predicate taking a branching vector addition system `b` together
with a target vector `t` and returning whether `t` is reachable in `b` is a
computable predicate.

As of August 2026, the solution is quite recently announced and is not
yet peer-reviewed.
-/
@[category research solved, AMS 3 68]
theorem reachability_decidable :
    ∀ {d : ℕ}, ComputablePred fun p : Bvas d × (Fin d → ℤ) => p.1.Reachable p.2 := by
  sorry

/-- Every axiom that is non-negative is reachable. -/
@[category test, AMS 3 68]
theorem reachable_of_mem_axioms {d : ℕ} (b : Bvas d) {v : Fin d → ℤ}
    (hmem : v ∈ b.axioms) (hcfg : 0 ≤ v) : b.Reachable v :=
  .base hmem hcfg

/-- Reachable vectors are always non-negative. -/
@[category test, AMS 3 68]
theorem reachable_imp_pos {d : ℕ} (v : Fin d → ℤ) (b : Bvas d) :
    b.Reachable v → 0 ≤ v := by
  intro h; cases h; all_goals 

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
