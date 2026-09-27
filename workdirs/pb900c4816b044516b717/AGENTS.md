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

(AUS 2) Given a finite number of angular regions \(A_1, \ldots, A_k\) in a plane, each \(A_i\) being bounded by two half-lines meeting at a vertex and provided with a \(+\) or \(-\) sign, we assign to each point \(P\) of the plane and not on a bounding half-line the number \(k - l\), where \(k\) is the number of \(+\) regions and \(l\) the number of \(-\) regions that contain \(P\). (Note that the boundary of \(A_i\) does not belong to \(A_i\).)\n\nFor instance, in the figure we have two \(+\) regions \(QAP\) and \(RCQ\), and one \(-\) region \(RBP\). Every point inside \(\triangle ABC\) receives the number \(+1\), while every point not inside \(\triangle ABC\) and not on a boundary halfline the number 0. We say that the interior of \(\triangle ABC\) is represented as a sum of the signed angular regions \(QAP\), \(RBP\), and \(RCQ\).\n\n(a) Show how to represent the interior of any convex planar polygon as a sum of signed angular regions.\n\n(b) Show how to represent the interior of a tetrahedron as a sum of signed angular regions, that is, regions bounded by three planes intersecting at a vertex and provided with a \(+\) or \(-\) sign.

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
