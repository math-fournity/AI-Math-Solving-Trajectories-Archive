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
# Strong Sensitivity Conjecture (`bs(f) ≤ s(f)^2`)

This file formalizes the *strong* sensitivity conjecture, asserting:

For every Boolean function `f : {0,1}^n → {0,1}`,
`bs(f) ≤ s(f)^2`,
where bs(f) denotes block sensitivity and s(f) denotes sensitivity.

Huang's theorem proves a *quartic* upper bound, `bs(f) ≤ s(f)^4`, thereby
resolving the most widely known form of the sensitivity conjecture.

We now ask whether a stronger upper bound holds. Interestingly, the original
paper of Nisan and Szegedy, where the sensitivity conjecture first appeared,
already speculated that a *quadratic* upper bound might be the correct
relation. On the lower bound side, Rubinstein
(https://link.springer.com/article/10.1007/BF01200762) constructed Boolean functions
exhibiting the first quadratic separation. The best currently
known gap, due to Ambainis and Sun (https://arxiv.org/abs/1108.3494), is
`bs(f) ≥ (2/3)⋅s(f)^2`.

*References:*
* [Induced Subgraphs of Hypercubes and a Proof of the Sensitivity Conjecture](https://arxiv.org/abs/1907.00847)
  by Hao Huang (see Section 3, Concluding Remarks)
* [Variations on the Sensitivity Conjecture](https://arxiv.org/abs/1011.0354)
  by Pooya Hatami, Raghav Kulkarni, and Denis Pankratov (see Question 3.1)
* [On the Degree of Boolean Functions as Real Polynomials](https://link.springer.com/article/10.1007/BF01263419)
  by Noam Nisan, and Mario Szegedy (see Section 4, Open Problems)
-/

namespace StrongSensitivityConjecture

open Finset Function

section Sensitivity

variable {n : ℕ}

/-- Flip operator,
`flip x B` returns input `x` with bits in block `B` inverted. -/
def flip (x : Fin n → Bool) (B : Finset (Fin n)) : Fin n → Bool :=
  fun i => if i ∈ B then !(x i) else x i

/-- Local sensitivity s(f,x),
number of indices where flipping one bit changes the value of `f`. -/
def sensitivityAt (f : (Fin n → Bool) → Bool) (x : Fin n → Bool) : ℕ :=
  #{i | f (flip x {i}) ≠ f x}

/-- Global sensitivity s(f),
maximum sensitivity of `f` over all inputs. -/
def sensitivity (f : (Fin n → Bool) → Bool) : ℕ :=
  univ.sup (sensitivityAt f)

/-- Check validity of block collection (disjoint and sensitive),
A collection of blocks `cB` is valid for `f` at `x` if the blocks are
disjoint and flipping any block changes `f(x)`. -/
def IsValidBlockConfig (f : (Fin n → Bool) → Bool) (x : Fin n → Bool)
    (cB : Finset (Finset (Fin n))) : Prop :=
  (cB : Set (Finset (Fin n))).PairwiseDisjoint id ∧
  ∀ B ∈ cB, f (flip x B) ≠ f x

/-- Local block sensitivity bs(f,x),
maximum size of a collection of sensitive, disjoint blocks for `f` at `x`. -/
noncomputable def blockSensitivityAt (f : (Fin n → Bool) → Bool) (x : Fin n → Bool) : ℕ :=
  open scoped Classical in
  Finset.sup {cB | IsValidBlockConfig f x cB} card

/-- Global block sensitivity of `f`,
maximum block sensitivity of `f` over all inputs. -/
noncomputable def blockSensitivity (f : (Fin n → Bool) → Bool) : ℕ :=
  univ.sup (blockSensitivityAt f)

/-- Strong Sensitivity Conjecture,
for every Boolean function `f : {0,1}^n → {0,1}`,
`bs(f) ≤ s(f)^2`.

We call this the *strong* sensitivity conjecture because the original sensitivity
conjecture only asked for a polynomial bound in terms of `s(f)`. Huang's
celebrated result (often called the sensitivity theorem) gives a quartic bound,
`bs(f) ≤ s(f)^4`, thereby settling the original conjecture. -/
@[category research open, AMS 68]
theorem strong_sensitivity_conjecture {n : ℕ} (f : (Fin n → Bool) → Bool) :
    blockSensitivity f ≤ sensitivity f ^ 2 := by
  sorry


/-- Simple test example.
For multiples of four with $n \ge 12$, this Boolean function has block sensitivity
strictly greater than its sensitivity. Source:
[Nisan1989](https://dl.acm.org/doi/10.1145/73007.73038).

`nisanExample(x) = 1` iff the Hamming weight of $x$ is either
$n/2$ or $n/2 + 1$.
The function is symmetric, so its value only depends on the Hamming weight
of the input. -/
@[category test, AMS 68]
def nisanExample (n : ℕ) (x : Fin n → Bool) : Bool :=
  let w := #{i | x i}
  decide ((w : ℚ) ∈ ({(n / 2 : ℚ), (n / 2 : ℚ) + 1} : Finset ℚ))

/-- Assuming `n` is a positive multiple of 4, the sensitivity of `nisanExample`
is $n/2 + 2$. It is achieved by any $x$ with Hamming weight $n/2 + 2$: flipping
any of its $n/2 + 2$ one-bits moves the input into the accepting layer of weight $n/2 + 1$. -/
@[category test, AMS 68]
lemma nisanExample_sensitivity (

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
