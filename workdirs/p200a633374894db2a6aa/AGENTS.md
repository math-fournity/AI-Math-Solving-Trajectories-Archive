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
# Littlewood conjectures

*References:*
- [Wikipedia](https://en.wikipedia.org/wiki/Littlewood_conjecture)
- [Bernard Mathan and Olivier Touli´e, *Problem`emes diophantiens simultan´es*][mathantoilie2004]
-/

open Filter

-- TODO(mercuris): This is a norm on ℝ/ℤ, show this?

namespace LittlewoodConjecture


/--
For any two real numbers $\alpha$ and $\beta$,
$$
  \liminf_{n\to\infty} n\||n\alpha\||\||n\beta\|| = 0
$$
where $\||x\|| := \min(|x - \lfloor x \rfloor|, |x - \lceil x \rceil|)$ is the distance
to the nearest integer.
-/
@[category research open, AMS 11]
theorem littlewood_conjecture (α β : ℝ) :
    atTop.liminf (fun (n : ℕ) ↦ n * distToNearestInt (n * α) * distToNearestInt (n * β)) = 0 := by
  sorry

/--
For real number $\alpha$ and prime $p$,
$$
  \liminf_{n \to\infty} n |n|_{p}\||n\alpha\|| = 0
$$
where $\||x\|| := \min(|x - \lfloor x \rfloor|, |x - \lceil x \rceil|)$ is the distance
to the nearest integer, and $|x|_{p}$ is the $p$-adic norm.
-/
@[category research open, AMS 11]
theorem padic_littlewood_conjecture (α : ℝ) (p : ℕ) (hp : p.Prime) :
    atTop.liminf (fun (n : ℕ) ↦ n * padicNorm p n * distToNearestInt (n * α)) = 0 := by
  sorry

end LittlewoodConjecture


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
