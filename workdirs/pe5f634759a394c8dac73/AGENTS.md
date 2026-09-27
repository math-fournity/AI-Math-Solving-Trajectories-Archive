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
# Written on the Wall II - Conjecture 291

*Reference:*
[E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

## Definitions

For a vertex $v$ in a graph $G$, **$T(v)$** is the number of triangles (3-cliques)
incident to $v$, i.e., the number of 3-element cliques in $G$ that contain $v$.

The **triangle-frequency of the minimum** is the number of vertices that achieve the
minimum value of $T(v)$.

**$k$** is the **first step in the Havel–Hakimi process at which a zero appears**.
Concretely, starting from the descending degree sequence $s_0$ of $G$, we set
$s_{i+1} = \mathrm{havelHakimiStep}\, s_i$ and let $k$ be the least $i \ge 0$ such
that $s_i$ contains a zero entry (or, vacuously, has been emptied entirely). Since
each step is sorted descending and never increases entries, this is equivalent
to the last (smallest) entry of $s_i$ being $0$, or $s_i$ being $[]$.

This is **strictly weaker** than $n - \mathrm{residue}(G)$: $n - \mathrm{residue}(G)$
is the *total* number of reduction steps until *every* entry is zero, whereas $k$
only requires that *some* entry has hit zero — and a $0$ typically appears well
before the all-zero state is reached.

**Conjecture 291:** For a simple connected graph $G$ with $n > 2$,
$\gamma_t(G) \le k + \mathrm{frequency}(t_{\min}(v))$
where $\gamma_t(G)$ is the total domination number, $k$ is the Havel-Hakimi zero
step, and $\mathrm{frequency}(t_{\min}(v))$ is the number of vertices achieving
the minimum triangle count.
-/

namespace WrittenOnTheWallII.GraphConjecture291

open SimpleGraph

variable {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α]

/-- The minimum number of triangles incident to any vertex, over all vertices of $G$. -/
noncomputable def minTrianglesAtVertex (G : SimpleGraph α) [DecidableRel G.Adj] : ℕ :=
  Finset.univ.inf' Finset.univ_nonempty (numTrianglesAtVertex G)

/-- The number of vertices achieving the minimum triangle count. -/
noncomputable def freqMinTriangles (G : SimpleGraph α) [DecidableRel G.Adj] : ℕ :=
  (Finset.univ.filter (fun v => numTrianglesAtVertex G v = minTrianglesAtVertex G)).card

/-- The descending degree sequence of $G$, used as the starting point of the
Havel-Hakimi reduction.

Uses `Finset.univ.val.map` (multiset, duplicate-preserving) rather than
`Finset.univ.image` (set, deduplicating), so that e.g. $C_4$ produces
$[2, 2, 2, 2]$ rather than $[2]$. -/
noncomputable def descDegreeSequence (G : SimpleGraph α) [DecidableRel G.Adj] : List ℕ :=
  (Finset.univ.val.map (fun v : α => G.degree v)).sort (· ≥ ·)

/-- The Havel-Hakimi sequence of iterates: `s i` is the result of applying
`havelHakimiStep` $i$ times to the descending degree sequence of $G$. -/
noncomputable def havelHakimiIterate (G : SimpleGraph α) [DecidableRel G.Adj] (i : ℕ) :
    List ℕ :=
  (havelHakimiStep)^[i] (descDegreeSequence G)

/-- The first step $i$ (counting from $0$) at which a zero appears in the
Havel-Hakimi reduction of the descending degree sequence of $G$, or in which
the sequence has been emptied. We use `sInf` over the set of such $i$ so the
definition is well-defined for every graph: in particular, when $G$ is a
connected graph with $n \ge 2$ the minimum degree at iteration $0$ is at least
$1$, so the first zero only appears at some $i \ge 1$; and since each step
strictly shortens the list (or empties it), at the latest by $i = n$ the
sequence is empty and the predicate holds vacuously.

This is the WOWII $k$ of Conjecture 291, which is the **first** step at which a
zero appears — typically strictly less than $n - \mathrm{residue}(G)$ (which is
the *total* number of reduction steps to reach the all-zero state). -/
noncomputable def havelHakimiZeroStep (G : SimpleGraph α) [DecidableRel G.Adj] : ℕ :=
  sInf {i | 0 ∈ havelHakimiIterate G i ∨ havelHakimiIterate G i = []}

/--
WOWII [Conjecture 291](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

For a simple connected graph $G$ with $n > 2$,
$\gamma_t(G) \le k + \mathrm{frequency}(t_{\min}(v))$
where:

- $\gamma_t(G)$ is the total domination number,
- $k$ is the first step in which a zero appears in the Havel-Hakimi process,
- $\mathrm{frequency}(t_{\min}(v))$ is the number of vertices achieving the
  minimum triangle count.
-/
@[category research open, AMS 5]
theorem conjecture291 (G : SimpleGraph α) [DecidableRel G.Adj] (

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
