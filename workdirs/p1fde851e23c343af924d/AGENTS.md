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

import FormalConjectures.ErdosProblems.«170»
import FormalConjecturesForMathlib.Combinatorics.Additive.DifferenceBasis

/-!
# Sparse Ruler

A sparse ruler of length $L$ is a sequence of marks $0 = a_1 < a_2 < \dots < a_m = L$.
A distance $k \in \mathbb{N}$ can be measured if there are $i, j \in \{1, \dots, m\}$, such that
$k = a_j - a_i$.

One question concerns the structure of *optimal* rulers. Wichmann [Wi63] gave a
parametric family of sparse rulers and conjectured that, beyond a small number of exceptions,
every optimal ruler is of his type. The known exceptions occur at lengths $1, 13, 17, 23, 58$;
the largest of these has $13$ segments, which motivates the bound below.

The asymptotic growth of the minimal number of marks of an optimal ruler of length $L$ — i.e.
the limit of $l(n)^2 / n$, conjectured to lie in $[2.434\ldots, 3]$ — is the subject of
`FormalConjectures.ErdosProblems.«170»` (there phrased via $F(N)/\sqrt{N}$), and is not
restated here.

*References:*
- [Wi63] Wichmann, B. "A note on restricted difference bases." Journal of the London
  Mathematical Society 38 (1963): 465-466.
- [Wikipedia](https://en.wikipedia.org/wiki/Sparse_ruler)
-/

namespace SparseRuler

/-- A ruler is described by its list of *segment lengths* (gaps) `g`, so that its marks are
the partial sums $0 = m_0 < m_1 < \cdots < m_n = L$, where $n$ (`g.length`) is the number of
segments and $L$ (`g.sum`) is the length. -/
def marks (g : List ℕ) : Finset ℕ :=
  (Finset.range (g.length + 1)).image (fun i => (g.take i).sum)

/-- A ruler is *complete* (a perfect ruler) if its marks form a difference basis for
$\{0, 1, \ldots, L\}$, i.e. every distance $k \le L$ is the difference of two marks. This is
`Finset.IsDifferenceBasis` applied to the marks. -/
def IsComplete (g : List ℕ) : Prop :=
  (marks g).IsDifferenceBasis (Finset.range (g.sum + 1))

/-- A complete ruler is *minimal* if no complete ruler of the same length $L$ has fewer marks
(equivalently, fewer segments). -/
def IsMinimal (g : List ℕ) : Prop :=
  IsComplete g ∧ ∀ g' : List ℕ, IsComplete g' → g'.sum = g.sum → g.length ≤ g'.length

/-- A complete ruler is *maximal* if no complete ruler with the same number of marks
(equivalently, the same number of segments) has greater length. -/
def IsMaximal (g : List ℕ) : Prop :=
  IsComplete g ∧ ∀ g' : List ℕ, IsComplete g' → g'.length = g.length → g'.sum ≤ g.sum

/-- A ruler is *optimal* if it is both minimal and maximal. -/
def IsOptimal (g : List ℕ) : Prop := IsMinimal g ∧ IsMaximal g

/-- The *Wichmann ruler* $W(r, s)$ [Wi63], given by its segment-length sequence
$$1^r,\; (r+1),\; (2r+1)^r,\; (4r+3)^s,\; (2r+2)^{r+1},\; 1^r,$$
where $a^b$ denotes $b$ consecutive segments of length $a$. -/
def wichmannGaps (r s : ℕ) : List ℕ :=
  List.replicate r 1 ++ [r + 1] ++ List.replicate r (2 * r + 1) ++
    List.replicate s (4 * r + 3) ++ List.replicate (r + 1) (2 * r + 2) ++ List.replicate r 1

/-- The Wichmann ruler $W(r, s)$ has $4r + s + 2$ segments, hence $4r + s + 3$ marks [Wi63]. -/
@[category API, AMS 5]
lemma wichmannGaps_length (r s : ℕ) : (wichmannGaps r s).length = 4 * r + s + 2 := by
  simp only [wichmannGaps, List.length_append, List.length_replicate, List.length_cons,
    List.length_nil]
  omega

/-- The Wichmann ruler $W(r, s)$ has length $4r(r + s + 2) + 3(s + 1)$ [Wi63]. -/
@[category API, AMS 5]
lemma wichmannGaps_sum (r s : ℕ) :
    (wichmannGaps r s).sum = 4 * r * (r + s + 2) + 3 * (s + 1) := by
  simp only [wichmannGaps, List.sum_append, List.sum_replicate, List.sum_cons, List.sum_nil,
    smul_eq_mul]
  ring

/-- **Wichmann's conjecture on optimal rulers.** Every optimal ruler with more than $13$
segments is a Wichmann ruler $W(r, s)$ (up to reflection, i.e. reversing the segment list).
Posed by Wichmann [Wi63]; the finitely many known exceptions all have at most $13$ segments
(lengths $1, 13, 17, 23, 58$), and no further exceptions are known up to length $213$. -/
@[category research open, AMS 5]
theorem wichmann_conjecture {g : List ℕ} (hopt : IsOptimal g) (hseg : 13 < g.length) :
    ∃ r s : ℕ, g = wichmannGaps r s ∨ g = (wichmannGaps r s).reverse := by
  sorry

end SparseRuler


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
