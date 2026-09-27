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

In the mountainous region of Triangula, a surveyor is mapping a triangular plot of land designated as Territory $ABC$. The primary surveying station is located at Outpost $A$, where the two straight border paths, $AB$ and $AC$, meet at a precise angle of $60^\circ$.

To divide the land for environmental monitoring, two specialist paths are cleared:
1.  A path starting from Outpost $B$ that perfectly bisects the angle at $B$ until it reaches a monitoring station $P$ on the border $AC$.
2.  A path starting from Outpost $C$ that perfectly bisects the angle at $C$ until it reaches a monitoring station $Q$ on the border $AB$.

The surveyor identifies a sub-sector of the land defined by the triangular area $APQ$. Within these territories, circular conservation zones are established:
- A large circular zone is inscribed within the main Territory $ABC$, having a radius of $r_1$.
- A smaller circular zone is inscribed within the sub-sector $APQ$, having a radius of $r_2$.

The surveyor now needs to establish a circular perimeter fence that passes exactly through the three points $A$, $P$, and $Q$. Determine the radius of this circular perimeter fence in terms of $r_1$ and $r_2$.

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
