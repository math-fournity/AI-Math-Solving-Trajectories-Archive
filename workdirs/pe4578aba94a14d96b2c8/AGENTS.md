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
# Erdős Problem 464

*References:*
- [erdosproblems.com/464](https://www.erdosproblems.com/464)
- [Er75i] Erdős, P., *Répartition modulo $1$*. (1975), iv+258.
- [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
  number theory*. Monographies de L'Enseignement Mathématique (1980).
- [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
  (1982), 59--79.
- [AkMo04] Akhunzhanov, R. K. and Moshchevitin, N. G., *On the chromatic number of a distance
  graph associated with a lacunary sequence*. Dokl. Akad. Nauk (2004), 295-296.
- [Du06] Dubickas, Artūras, *On the fractional parts of lacunary sequences*. Math. Scand. (2006),
  136-146.
- [Ka01] Katznelson, Y., *Chromatic numbers of Cayley graphs on $\mathbb{Z}$ and recurrence*.
  Combinatorica (2001), 211-219.
- [PeSc10] Peres, Yuval and Schlag, Wilhelm, *Two Erdős problems on lacunary sequences: chromatic
  number and Diophantine approximation*. Bull. Lond. Math. Soc. (2010), 295-300.
- [Po79b] Pollington, A. D., *On the density of sequence $\{n_k\xi\}$*. Illinois J. Math. (1979),
  511-515.
- [dM80] de Mathan, B., *Numbers contravening a condition in density modulo $1$*. Acta Math.
  Acad. Sci. Hungar. (1980), 237-241 (1981).
-/

namespace Erdos464

/- Formalization notes:
- Since every $\|\theta n_k\|$ lies in $[0,1/2]$, the literal reading of "$\{\|\theta n_k\|\}$
  is not dense in $[0,1]$" would be vacuously true. The intended (and solved) content is that
  the sequence $(\theta n_k)$ is not dense modulo one, which is how the conclusion is rendered
  here: `¬ Dense (Set.range fun k => (↑(θ * n k) : AddCircle (1 : ℝ)))`. This matches
  `pollington_de_mathan` in `Problem10_6.lean` of the Bugeaud collection, which formalizes the
  full-Hausdorff-dimension version of the same de Mathan–Pollington theorem. It is implied by
  the $\inf_{k\geq 1}\|\theta n_k\| > 0$ that de Mathan and Pollington prove.
- The lacunarity hypothesis is rendered by the house predicate `IsLacunary`
  ($\exists c > 1$ with $c \cdot n_k < n_{k+1}$ for all sufficiently large $k$), as in
  `erdos_355`; for a strictly increasing sequence of positive integers the problem's condition
  $n_{k+1} \geq (1+\epsilon) n_k$ for all $k$ implies `IsLacunary`, and modifying finitely many
  terms does not affect density modulo one.
-/

/--
Let $A=\{n_1<n_2<\cdots\}\subset \mathbb{N}$ be a lacunary sequence (so there exists some
$\epsilon>0$ with $n_{k+1}\geq (1+\epsilon)n_k$ for all $k$). Must there exist an irrational
$\theta$ such that
$$\{ \|\theta n_k\| : k\geq 1\}$$
is not dense in $[0,1]$ (where $\| x\|$ is the distance to the nearest integer)?

Solved independently by de Mathan [dM80] and Pollington [Po79b], who showed that, given any
such $A$, there exists such a $\theta$, with
$$\inf_{k\geq 1}\| \theta n_k\| \gg \frac{\epsilon^4}{\log(1/\epsilon)}.$$
This bound was improved by Katznelson [Ka01], Akhunzhanov and Moshchevitin [AkMo04], and
Dubickas [Du06], before Peres and Schlag [PeSc10] improved it to
$$\inf_{k\geq 1}\| \theta n_k\| \gg \frac{\epsilon}{\log(1/\epsilon)},$$
and note that the best bound possible here would be $\gg \epsilon$.

This problem has consequences for [894](https://www.erdosproblems.com/894).

The conclusion "$\{\|\theta n_k\|\}$ is not dense in $[0,1]$" is formalized as the sequence
$(\theta n_k)$ not being dense modulo one; see the formalization notes above.
-/
@[category research solved, AMS 11, formal_proof using lean4 at "https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/464/Erdos464.lean"]
theorem erdos_464 : answer(True) ↔
    ∀ n : ℕ → ℕ, StrictMono n → (∀ k, 0 < n k) → IsLacunary n →
      ∃ θ : ℝ, Irrational θ ∧
        ¬ Dense (Set.range fun k => (↑(θ * n k) : AddCircle (1 : ℝ))) := by
  sorry

end Erdos464


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
