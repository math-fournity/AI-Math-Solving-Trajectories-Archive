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
# Erdős Problem 594

*References:*
- [erdosproblems.com/594](https://www.erdosproblems.com/594)
- [ErHa66] Erdős, P. and Hajnal, A., On chromatic number of graphs and set-systems.
  Acta Math. Acad. Sci. Hungar. (1966), 61-99.
- [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in
  Graph Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968)
  (1969), 27-35.
- [EHS74] Erdős, P. and Hajnal, A. and Shelah, S., On some general properties of chromatic
  numbers. Topics in topology (Proc. Colloq., Keszthely, 1972) (1974), 243-255.
-/

open Cardinal
open scoped Cardinal

namespace Erdos594

/--
**Erdős Problem 594** (Erdős–Hajnal [ErHa66], [Er69b]):

Does every graph $G$ with chromatic number $\geq \aleph_1$ contain all sufficiently
large odd cycles?

The answer is **Yes**, proved by Erdős, Hajnal, and Shelah [EHS74].

A graph has chromatic number $\geq \aleph_1$ (i.e. uncountable chromatic number)
if and only if it admits no proper colouring with countably many colours; this is
encoded as `IsEmpty (G.Coloring ℕ)`. The conclusion states that there is some
$N$ such that for every $k \geq N$ the graph contains a cycle of odd length $2k + 1$.
-/
@[category research solved, AMS 3 5]
theorem erdos_594 : answer(True) ↔
    ∀ (V : Type) (G : SimpleGraph V), IsEmpty (G.Coloring ℕ) →
      ∃ N : ℕ, ∀ k : ℕ, N ≤ k →
        ∃ (v : V) (w : G.Walk v v), w.IsCycle ∧ w.length = 2 * k + 1 := by
  sorry

/--
The earlier result of Erdős and Hajnal [ErHa66]: every graph with chromatic number
$\geq \aleph_2$ contains all sufficiently large odd cycles.

Chromatic number $\geq \aleph_2$ is encoded as the nonexistence of a proper colouring
with any set of at most $\aleph_1$ colours.
-/
@[category research solved, AMS 3 5]
theorem erdos_594.variants.erdos_hajnal (V : Type) (G : SimpleGraph V)
    (h : ∀ (α : Type), #α ≤ ℵ_ 1 → IsEmpty (G.Coloring α)) :
    ∃ N : ℕ, ∀ k : ℕ, N ≤ k →
      ∃ (v : V) (w : G.Walk v v), w.IsCycle ∧ w.length = 2 * k + 1 := by
  sorry

/--
Sanity check for the encoding of "chromatic number $\geq \aleph_1$": a countably
colourable graph, such as the empty graph on $\mathbb{N}$, does not satisfy the
hypothesis `IsEmpty (G.Coloring ℕ)`.
-/
@[category test, AMS 5]
theorem erdos_594.variants.bot_countably_colorable :
    ¬ IsEmpty ((⊥ : SimpleGraph ℕ).Coloring ℕ) := by
  rw [not_isEmpty_iff]
  exact ⟨SimpleGraph.Coloring.mk (fun _ => 0) (by simp)⟩

end Erdos594


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
