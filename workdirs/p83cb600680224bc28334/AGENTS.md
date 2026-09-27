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
# Mathoverflow 347178

*Reference:* [mathoverflow/347178](https://mathoverflow.net/questions/347178)
asked by user [*Biagio Ricceri*](https://mathoverflow.net/users/149235/biagio-ricceri)
-/

open Real Set
open scoped EuclideanGeometry

namespace Mathoverflow347178

/--
Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Is it true that
$$\sup_{x \in \mathbb R^n}f(x) = \sup_{x\in \mathbb R^n} f(x+\nabla f(x))$$?

Answer: No. A counterexample in $\mathbb R^2$ is recorded in the linked formal proof.
-/
@[category research solved, AMS 26,
  formal_proof using formal_conjectures at
    "https://github.com/google-deepmind/formal-conjectures/commit/fc20c0b55eab6fc26e2bb5b24fb3005303a0910b"]
theorem mathoverflow_347178 :
    answer(False) ↔ ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (_ : ContDiff ℝ 1 f),
        (BddAbove (range f) ↔ BddAbove (range (fun x ↦ f (x + gradient f x)))) ∧
        (⨆ x, (f x : EReal)) = ⨆ x, (f (x + gradient f x) : EReal) := by
  sorry

/--
Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Is the boundedness of
$\sup_{x \in \mathbb R^n}f(x)$ and $\sup_{x\in \mathbb R^n} f(x+\nabla f(x))$ equivalent?

Answer: No. The same counterexample is recorded in the linked formal proof.
-/
@[category research solved, AMS 26,
  formal_proof using formal_conjectures at
    "https://github.com/google-deepmind/formal-conjectures/commit/fc20c0b55eab6fc26e2bb5b24fb3005303a0910b"]
theorem mathoverflow_347178.variants.bounded_iff :
    answer(False) ↔ ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (_ : ContDiff ℝ 1 f),
        BddAbove (range f) ↔ BddAbove (range fun x ↦ f (x + gradient f x)) := by
  sorry

/--
Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Does the equality
$$\sup_{x \in \mathbb R^n}f(x) = \sup_{x\in \mathbb R^n} f(x+\nabla f(x))$$
hold when both suprema are finite?
-/
@[category research open, AMS 26]
theorem mathoverflow_347178.variants.bounded_only :
    answer(sorry) ↔ ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (hf : ContDiff ℝ 1 f)
        (h : BddAbove (range f)) (h' : BddAbove (range (fun x ↦ f (x + gradient f x)))),
        (⨆ x, f x) = ⨆ x, f (x + gradient f x) := by
  sorry

end Mathoverflow347178


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
