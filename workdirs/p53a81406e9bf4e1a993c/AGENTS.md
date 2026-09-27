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
# Open Quantum Problem 35: existence of absolutely maximally entangled pure states

**Problem:** For which numbers of parties $n$ and local dimensions $d$ does there
exist a pure absolutely maximally entangled state $\psi$?

A pure state $\psi$ on $n$ parties of local dimension $d$ is called
**absolutely maximally entangled (AME)** if, for every subset of at most half
of the parties, the corresponding reduced density matrix is maximally mixed.

*References:*
- Open Quantum Problems, Problem 35:
  <https://oqp.iqoqi.oeaw.ac.at/existence-of-absolutely-maximally-entangled-pure-states>
- Formal Conjectures issue #3452:
  <https://github.com/google-deepmind/formal-conjectures/issues/3452>
- W. Helwig, W. Cui, A. Riera, J. I. Latorre, and H.-K. Lo,
  *Absolute Maximal Entanglement and Quantum Secret Sharing*,
  Phys. Rev. A 86, 052335 (2012), arXiv:1204.2289.
- D. Goyeneche, D. Alsina, J. I. Latorre, A. Riera, and K. Życzkowski,
  *Absolutely Maximally Entangled states, combinatorial designs and multi-unitary matrices*,
  Phys. Rev. A 92, 032316 (2015), arXiv:1506.08857.
- A. Higuchi and A. Sudbery,
  *How entangled can two couples get?*,
  Phys. Lett. A 273, 213-217 (2000), arXiv:quant-ph/0005013.
- A. J. Scott,
  *Multipartite entanglement, quantum-error-correcting codes, and entangling power of quantum
  evolutions*, Phys. Rev. A 69, 052330 (2004), arXiv:quant-ph/0310137.
- F. Huber, O. Gühne, and J. Siewert,
  *Absolutely maximally entangled states of seven qubits do not exist*,
  Phys. Rev. Lett. 118, 200502 (2017), arXiv:1608.06228.
- F. Huber and M. Grassl,
  *Quantum Codes of Maximal Distance and Highly Entangled Subspaces*,
  Quantum 4, 284 (2020), arXiv:1907.07733.
- S. A. Rather, A. Burchardt, W. Bruzda, G. Rajchel-Mieldzioć,
  A. Lakshminarayan, and K. Życzkowski,
  *Thirty-six entangled officers of Euler: Quantum solution to a classically impossible problem*,
  Phys. Rev. Lett. 128, 080507 (2022), arXiv:2104.05122.
- G. Rajchel-Mieldzioć, R. Bistroń, A. Rico, A. Lakshminarayan,
  and K. Życzkowski,
  *Absolutely maximally entangled pure states of multipartite quantum systems*,
  arXiv:2508.04777 (2025).

This file formalizes the problem of determining for which pairs $(n,d)$ there exists an
absolutely maximally entangled pure state $\mathrm{AME}(n,d)$.

We represent an $n$-partite state of local dimension $d$ by the finite-dimensional Hilbert space
`EuclideanSpace ℂ (Config n d)`, whose coordinates in the computational basis are amplitudes.
The helper `mkStateVector` turns an amplitude function into such a state, and normalization is
imposed explicitly via `IsNormalized`, i.e. via the ambient $L^2$ norm.

The main reusable lemma is `reducedDensityFirst_of_completion`: if a state is a
uniform superposition over the graph of an injective completion function
`completion : Config m d → Config (n - m) d`,
then the reduced state on the first $m$ parties is maximally mixed.

As demonstration, we show that the Bell states with $n=2$ and GHZ states with $n=3$ are
AME states, and the GHZ state with $n=4$ is not an AME state.
-/

open scoped BigOperators

namespace OpenQuantumProblem35

/- ## Basic structures -/

/-- A computational-basis configuration of $n$ parties with local dimension $d$. -/
abbrev Config (n d : ℕ) := Fin n → Fin d

/-- A state vector in the computational basis, viewed as a finite-dimensional Hilbert space. -/
abbrev StateVector (n d : ℕ) := EuclideanSpace ℂ (Config n d)

/-- Build a state vector from its computational-basis amplitudes. -/
abbrev mkStateVector {n d : ℕ} (ψ : Config n d → ℂ) : StateVector n d :=
  WithLp.toLp 2 ψ

/-- A state vector can be evaluated on a computational-basis configuration to read its amplitude. -/
instance {n d : ℕ} : CoeFun (StateVector n d) (fun _ => Config n d → ℂ) where
  coe ψ := ψ.ofLp

/-- A state built from amplitudes has those amplitudes as its coordinates. -/
@[simp, category API, AMS 5 15 81 94]
lemma mkStateVector_apply {n d : ℕ} (ψ : Config n d → ℂ) (x : Config n d) :
    mkStateVector ψ x = ψ x := rfl

/-- A state vector is normalized if it has $L^2$ norm $1$. -/
def IsNormalized {n d : ℕ} (ψ : StateVector n d) : Prop :=
  ‖ψ‖ = 1

/-- A state is normalized iff its squared $L^2$ norm is $1$. -/
@[category API, AMS 5 15 81 94]
lemma isNormalized_iff_norm_sq_eq_one {n d : ℕ} (ψ : StateVector n d) :
    IsNormalized ψ ↔ ‖ψ‖ ^ 2 = 1 := by
  constr

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
