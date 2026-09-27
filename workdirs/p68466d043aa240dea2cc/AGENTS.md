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
# Green's Open Problem 39

*References:*
- [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.39)
- [BJR11] Bollobás, Béla, Svante Janson, and Oliver Riordan. "On covering by translates of a set."
  Random Structures & Algorithms 38.1‐2 (2011): 33-67.
-/

open Filter Topology
open scoped Pointwise

namespace Green39

/--
The proportion of subsets of $\mathbb{Z}/p\mathbb{Z}$ of size $k$ that can cover
$\mathbb{Z}/p\mathbb{Z}$ using at most $c$ translates.

If p = 0 or k > p, return 0 by convention.
-/
def proportionCoverable (p k c : ℕ) : ℚ :=
  if h : p = 0 then 0
  else if k > p then 0
  else
    have : NeZero p := ⟨h⟩
    let S : Finset (Finset (ZMod p)) := Finset.powersetCard k Finset.univ
    let coverable := S.filter (fun A => ∃ T : Finset (ZMod p), T.card ≤ c ∧ A + T = Finset.univ)
    (coverable.card : ℚ) / (S.card : ℚ)

@[category test, AMS 5 60]
theorem proportionCoverable_p_p_1 : proportionCoverable 3 3 1 = 1 := by native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_t_0 : proportionCoverable 5 2 0 = 0 := by native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_2_1_2 : proportionCoverable 2 1 2 = 1 := by native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_3_1_2 : proportionCoverable 3 1 2 = 0 := by native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_a_gt_p : proportionCoverable 3 4 2 = 0 := by native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_7_4_2 :
    proportionCoverable 7 4 2 = (3 : ℚ) / 5 := by
  native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_11_3_4 :
    proportionCoverable 11 3 4 = (1 : ℚ) / 3 := by
  native_decide

@[category test, AMS 5 60]
theorem proportionCoverable_11_4_3 :
    proportionCoverable 11 4 3 = (1 : ℚ) / 6 := by
  native_decide

/--
If $A \subset \mathbb{Z}/p\mathbb{Z}$ is random, $|A| = \sqrt{p}$, can we almost surely cover
$\mathbb{Z}/p\mathbb{Z}$ with $100\sqrt{p}$ translates of $A$? [Gr24]
-/
@[category research open, AMS 5 60]
theorem green_39 : answer(sorry) ↔
    Tendsto
      (fun p : {q : ℕ // q.Prime} ↦
        let k := Nat.sqrt p
        let c := 100 * k
        (proportionCoverable p k c : ℝ))
      atTop (𝓝 1) := by
  sorry

/--
"I do not know how to answer this even with 100 replaced by 1.01." [Gr24]"
-/
@[category research open, AMS 5 60]
theorem green_39.variant_101 : answer(sorry) ↔
    Tendsto
      (fun p : {q : ℕ // q.Prime} ↦
        let k := Nat.sqrt p
        let c := ⌊1.01 * (k : ℝ)⌋₊
        (proportionCoverable p k c : ℝ))
      atTop (𝓝 1) := by
  sorry

/--
Similar questions are interesting with $\sqrt{p}$ replaced by $p^\theta$ for any $\theta \le 1/2$. [Gr24]

NOTE: using $C p^\theta$ translates as stated makes the conjecture trivially false by the pigeonhole
principle. Indeed for a set of size $p^\theta$, we cover at most $C p^{2\theta}$ elements, which is
strictly less than $p$ for $\theta < 1/2$. We interpret the question as asking whether
$O(p^{1-\theta})$ translates suffice. This generalizes the main conjecture where
$\sqrt{p} = p^{1-1/2}$.
-/
@[category research open, AMS 5 60]
theorem green_39.variant_theta : answer(sorry) ↔
    ∀ (θ : ℝ), 0 < θ → θ ≤ 1/2 →
    ∃ C > 1, Tendsto
      (fun p : {q : ℕ // q.Prime} ↦
        let k := ⌊(p : ℝ) ^ θ⌋₊
        let c := ⌊C * (p : ℝ) ^ (1 - θ)⌋₊
        (proportionCoverable p k c : ℝ))
      atTop (𝓝 1) := by
  sorry

end Green39


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
