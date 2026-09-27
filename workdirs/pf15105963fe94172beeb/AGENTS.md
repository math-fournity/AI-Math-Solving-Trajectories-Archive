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
# Open Quantum Problem 13: Mutually unbiased bases

## Mathematical problem

For each integer $d \ge 2$, determine the maximum number $k$ for which there exist
orthonormal bases $\mathcal{B}_1, \dots, \mathcal{B}_k$ of the complex Hilbert space
$\mathbb{C}^d$ such that any two distinct bases are mutually unbiased.

Concretely, if
$\mathcal{B}_r = \{ e_0^{(r)}, \dots, e_{d-1}^{(r)} \}$
and
$\mathcal{B}_s = \{ e_0^{(s)}, \dots, e_{d-1}^{(s)} \}$,
then $\mathcal{B}_r$ and $\mathcal{B}_s$ are mutually unbiased if for all $i, j$
and all $r \ne s$,
$|\langle e_i^{(r)}, e_j^{(s)} \rangle| = d^{-1/2}$.

The problem is therefore to determine the maximal value
$\mu(d) := \max \{ k : \text{there exist } k \text{ pairwise mutually unbiased
orthonormal bases in } \mathbb{C}^d \}$.

In this file, an orthonormal basis is represented by a unitary matrix whose columns are the
basis vectors. For two such bases `U` and `V`, the matrix `relativeUnitary U V`, which is
$U^\dagger V$, contains all cross-basis overlaps as its entries. Since Lean works more
smoothly with squared norms, we formalize mutual unbiasedness by requiring
$\| (relativeUnitary\ U\ V)_{ij} \|^2 = 1 / d$
for all $i, j$, which is equivalent to
$|\langle e_i^{(r)}, e_j^{(s)} \rangle| = d^{-1/2}$.

## Background

Mutually unbiased bases are a basic structure in finite-dimensional quantum theory.
They arise in quantum state determination, quantum tomography, quantum cryptography,
finite geometry, and combinatorics.

A general upper bound is $\mu(d) \le d + 1$.
Equality is known when $d$ is a prime power, via constructions over finite fields.
For composite dimensions that are not prime powers, the exact value of $\mu(d)$ is in
general open.

The smallest and most famous unresolved case is $d = 6$.
The IQOQI OQP page emphasizes this dimension in particular: although many equivalent
reformulations are known, no construction yielding more than three mutually unbiased bases
in dimension six is known.

## What this file formalizes

This file is organized around the quantity `IsMaxMUBCount d k`, which expresses that
$k$ is the maximum number of mutually unbiased orthonormal bases in dimension $d$.

- the open theorem `mutuallyUnbiasedBases` expresses the full problem for all $d \ge 2$;
- the open theorem `mutuallyUnbiasedBases_dim6` expresses the especially important case
  $d = 6$;
- the solved theorem `mutuallyUnbiasedBases_dim2` proves the qubit case $\mu(2) = 3$.

## References

*Primary source list entry:*
- IQOQI Vienna Open Quantum Problems, problem 13:
  https://oqp.iqoqi.oeaw.ac.at/mutually-unbiased-bases
- Master list of open quantum problems:
  https://oqp.iqoqi.oeaw.ac.at/open-quantum-problems

### Foundational papers
- I. D. Ivanović,
  *Geometrical description of quantal state determination*,
  J. Phys. A 14, 3241-3245 (1981).
- W. K. Wootters and B. D. Fields,
  *Optimal state-determination by mutually unbiased measurements*,
  Ann. Phys. 191, 363-381 (1989).

### General constructions and surveys
- A. Klappenecker and M. Rötteler,
  *Constructions of mutually unbiased bases*,
  in *Finite Fields and Applications*, LNCS 2948 (2004).

### Dimension six and the maximal-number problem
- M. Grassl,
  *On SIC-POVMs and MUBs in Dimension 6*,
  arXiv:quant-ph/0406175 (2004).
- P. Butterley and W. Hall,
  *Numerical evidence for the maximum number of mutually unbiased bases in dimension six*,
  Phys. Lett. A 369, 5-8 (2007),
  arXiv:quant-ph/0701122.
- S. Brierley and S. Weigert,
  *Maximal Sets of Mutually Unbiased Quantum States in Dimension Six*,
  Phys. Rev. A 78, 042312 (2008),
  arXiv:0808.1614.
- P. Raynal, X. Lü, and B.-G. Englert,
  *Mutually unbiased bases in dimension six: The four most distant bases*,
  Phys. Rev. A 83, 062303 (2011),
  arXiv:1103.1025.

## Remark on the status of $d = 6$

The dimension-six case is not known to be solved. At present, the best-known general picture is:
- $3 \le \mu(6) \le 7$,
- complete sets of $7$ MUBs are not known,
- and several analytic and numerical works give strong evidence that one cannot go beyond $3$.

This is why the theorem `mutuallyUnbiasedBases_dim6` is marked as an open research statement.
-/
noncomputable section
namespace OpenQuantumProblem13

/- ## Preliminaries -/

/-- A unitary matrix representing an orthonormal basis of $\mathbb{C}^d$ via its columns. -/
abbrev UMat (d : ℕ) := ↥(Matrix.unitaryGro

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
