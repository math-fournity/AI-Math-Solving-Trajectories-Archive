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

import FormalConjecturesUtil.DeclName
import FormalConjectures.Arxiv.«1308.0994».BoxdotConjecture
import FormalConjectures.Arxiv.«1609.08688».sIncreasingrTuples
import FormalConjectures.Arxiv.«2602.05192».FirstProof4
import FormalConjectures.ErdosProblems.«1038»
import FormalConjectures.ErdosProblems.«1052»
import FormalConjectures.ErdosProblems.«1054»
import FormalConjectures.ErdosProblems.«1063»
import FormalConjectures.ErdosProblems.«1067»
import FormalConjectures.ErdosProblems.«1074»
import FormalConjectures.ErdosProblems.«1142»
import FormalConjectures.ErdosProblems.«12»
import FormalConjectures.ErdosProblems.«141»
import FormalConjectures.ErdosProblems.«17»
import FormalConjectures.ErdosProblems.«198»
import FormalConjectures.ErdosProblems.«263»
import FormalConjectures.ErdosProblems.«26»
import FormalConjectures.ErdosProblems.«295»
import FormalConjectures.ErdosProblems.«317»
import FormalConjectures.ErdosProblems.«349»
import FormalConjectures.ErdosProblems.«350»
import FormalConjectures.ErdosProblems.«36»
import FormalConjectures.ErdosProblems.«392»
import FormalConjectures.ErdosProblems.«399»
import FormalConjectures.ErdosProblems.«41»
import FormalConjectures.ErdosProblems.«42»
import FormalConjectures.ErdosProblems.«442»
import FormalConjectures.ErdosProblems.«457»
import FormalConjectures.ErdosProblems.«494»
import FormalConjectures.ErdosProblems.«503»
import FormalConjectures.ErdosProblems.«50»
import FormalConjectures.ErdosProblems.«513»
import FormalConjectures.ErdosProblems.«56»
import FormalConjectures.ErdosProblems.«590»
import FormalConjectures.ErdosProblems.«617»
import FormalConjectures.ErdosProblems.«61»
import FormalConjectures.ErdosProblems.«678»
import FormalConjectures.ErdosProblems.«686»
import FormalConjectures.ErdosProblems.«697»
import FormalConjectures.ErdosProblems.«835»
import FormalConjectures.ErdosProblems.«865»
import FormalConjectures.ErdosProblems.«886»
import FormalConjectures.ErdosProblems.«920»
import FormalConjectures.ErdosProblems.«951»
import FormalConjectures.ErdosProblems.«965»
import FormalConjectures.ErdosProblems.«968»
import FormalConjectures.ErdosProblems.«985»
import FormalConjectures.GreensOpenProblems.«14»
import FormalConjectures.GreensOpenProblems.«29»
import FormalConjectures.GreensOpenProblems.«32»
import FormalConjectures.Mathoverflow.«10799»
import FormalConjectures.Mathoverflow.«75792»
import FormalConjectures.OEIS.«228828»
import FormalConjectures.OEIS.«231201»
import FormalConjectures.OEIS.«232174»
import FormalConjectures.OEIS.«280831»
import FormalConjectures.OEIS.«56777»
import FormalConjectures.OEIS.«63880»
import FormalConjectures.OEIS.«6697»
import FormalConjectures.OEIS.«67720»
import FormalConjectures.OpenQuantumProblems.«13»
import FormalConjectures.OpenQuantumProblems.«23»
import FormalConjectures.OpenQuantumProblems.«35»
import FormalConjectures.Paper.DegreeSequencesTriangleFree
import FormalConjectures.Paper.Gourevitch
import FormalConjectures.Paper.MonochromaticQuantumGraph
import FormalConjectures.Wikipedia.AgohGiuga
import FormalConjectures.Wikipedia.BealConjecture
import FormalConjectures.Wikipedia.BusyBeaver
import FormalConjectures.Wikipedia.CongruentNumber
import FormalConjectures.Wikipedia.Hadamard
import FormalConjectures.Wikipedia.InverseGalois
import FormalConjectures.Wikipedia.Kaplansky
import FormalConjectures.Wikipedia.LychrelNumbers
import FormalConjectures.Wikipedia.Mahler32
import FormalConjectures.Wikipedia.Pell
import FormalConjectures.Wikipedia.RamanujanTau
import FormalConjectures.Wikipedia.RiemannZetaValues
import FormalConjectures.WrittenOnTheWallII.GraphConjecture13
import FormalConjectures.WrittenOnTheWallII.GraphConjecture16
import FormalConjectures.WrittenOnTheWallII.GraphConjecture33
import FormalConjectures.WrittenOnTheWallII.Test

/-!
# FC100SolvedSet1

A random subset of 100 non-open problems, drawn uniformly at random
from all problems without the `category research open` tag
(solved, test, API, etc.).
-/

namespace Subsets.FC100SolvedSet1

open Lean in
def problems : List Name := [
  decl_name% WrittenOnTheWallII.Test.petersen_size,
  decl_name% WrittenOnTheWallII.GraphConjecture13.conjecture13,
  decl_name% OpenQuantumProblem35.ame_3_exists,
  decl_name% LychrelNumbers.eventually_palindrome_base10,
  decl_name% Erdos42.example_maximal_sidon,
  decl_name% Mathoverflow75792.Reachable.complexity,
  decl_name% OeisA280831.a_0,
  decl_

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
