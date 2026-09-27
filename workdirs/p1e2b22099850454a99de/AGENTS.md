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
# Erdős Problem 847

*References:*
- [erdosproblems.com/847](https://www.erdosproblems.com/847)
- [RRS24] Reiher, Christian and R\"odl, Vojt\v ech and Sales, Marcelo, Colouring versus density in integers and {H}ales-{J}ewett cubes. J. Lond. Math. Soc. (2) (2024)
  [arXiv:2311.08556](https://arxiv.org/abs/2311.08556)
-/

namespace Erdos847

/--
`HasFew3APs A` means that $A \subset \mathbb{N}$ is a set for which there exists some $\epsilon > 0$ such that
in any subset of $A$ of size $n$ there is a subset of size at least $\epsilon n$ which contains no
three-term arithmetic progression.
-/
def HasFew3APs (A : Set ℕ) := ∃ (ε : ℝ), ε > 0 ∧ ∀ (B : Set ℕ), B ⊆ A → Finite B →
  ∃ (C : Set ℕ), C ⊆ B ∧ C.ncard ≥ ε * B.ncard ∧ ThreeAPFree C

/--
Let $A \subset \mathbb{N}$ be an infinite set for which there exists some $\epsilon > 0$ such that
in any subset of $A$ of size $n$ there is a subset of size at least $\epsilon n$ which contains no
three-term arithmetic progression.

Is it true that $A$ is the union of a finite number of sets which contain no three-term arithmetic
progression?

A negative answer was given by Reiher, Rödl, and Sales [RRS24], who proved that, for any
$0<\mu<1/2$, there exists $A\subseteq \mathbb{N}$ such that every finite colouring of $A$ contains
a three-term arithmetic progression, and yet every subset of $A$ of size $n$ contains a subset of
size $\geq \mu n$ without a three-term arithmetic progression.
-/
@[category research solved, AMS 11]
theorem erdos_847 : answer(False) ↔ ∀ (A : Set ℕ), Infinite A → HasFew3APs A →
    ∃ n, ∃ (S : Fin n → Set ℕ), (∀ i, ThreeAPFree (S i)) ∧ A = ⋃ i : Fin n, S i := by
  sorry

end Erdos847


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
