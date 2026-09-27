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
# Mills' Theorem

There exists a real $A > 1$ such that
$\lfloor A^{3^n}\rfloor$ is prime for every positive integer $n$, where $\lfloor\cdot\rfloor$
denotes the floor function.

The least such $A$ is known as *Mills' constant*. It is irrational, and assuming the
Riemann hypothesis it is approximately $1.3063778838\ldots$.

*References:*
- [Wikipedia, Mills' constant](https://en.wikipedia.org/wiki/Mills%27_constant)
- [A prime-representing function](https://www.ams.org/journals/bull/1947-53-06/S0002-9904-1947-08849-2/)
  by *W. H. Mills*, Bull. Amer. Math. Soc. **53** (1947), 604.
- [Mills' constant](https://mathworld.wolfram.com/MillsConstant.html) on Wolfram MathWorld.
- [Mills' constant is irrational](https://doi.org/10.1112/mtk.70027) by *Kota Saito*,
  Mathematika **71** (2025), no. 3, e70027, [arXiv:2404.19461](https://arxiv.org/abs/2404.19461).
- [Determining Mills' Constant ..](https://cs.uwaterloo.ca/journals/JIS/VOL8/Caldwell/caldwell78.pdf)
  by *Chris K. Caldwell and Yuanyou Cheng*, J. Integer Seq. **8** (2005), Article 05.4.1.
- [OEIS A051021](https://oeis.org/A051021) (decimal expansion of Mills' constant)
-/

namespace Mills

/--
Given any real $A$, `IsMills A` encodes the statement that $\lfloor A^{3^n}\rfloor,n > 0$ is prime.
-/
abbrev IsMills (A : ℝ) : Prop := ∀ (n : ℕ+), Prime ⌊A ^ (3 ^ (n : ℕ))⌋₊

/--
**Mills' theorem** (Mills, 1947).
There is a real number $A > 1$ such that $\lfloor A^{3^n}\rfloor$ is prime.
-/
@[category research solved, AMS 11]
theorem exists' : ∃ A > 1, IsMills A := by
  sorry

/--
For a real $A$, `IsMinMills A` is the smallest value satisfying `IsMills A`.
-/
abbrev IsMinMills (A : ℝ) : Prop := IsLeast {x | x > 1 ∧ IsMills x} A

/--
**Mills' constant.**
There is a *least* Mills number.
-/
@[category research solved, AMS 11]
theorem exists_least : ∃ A, IsMinMills A := by
  sorry

/--
**Mills' constant is irrational** (Saito, 2024).
-/
@[category research solved, AMS 11]
theorem irrational {A} (hA : IsMinMills A) :
    Irrational A := by
  sorry

/--
**Mills' constant lower bound** (Caldwell–Cheng, 2005): assuming the Riemann hypothesis,
Mills' constant begins at $1.3063778838\ldots$.
-/
@[category research solved, AMS 11]
theorem lower_bound_of_RH (hRH : RiemannHypothesis) {A} (hA : IsMinMills A) :
    A ∈ Set.Ioo (1.3063778838 : ℝ) 1.3063778839 := by
  sorry

end Mills


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
