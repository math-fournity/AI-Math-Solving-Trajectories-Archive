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

In a remote territory, three survey outposts—Central Station $C$, Base Camp $B$, and Alpha Station $A$—form a triangular perimeter. Two relay towers, $K$ and $L$, are positioned along the straight supply route connecting $A$ and $B$.

The layout of these towers is precisely calibrated relative to Central Station $C$: the angle formed between the lines to $A$ and $K$ ($\angle ACK$) is exactly equal to the angle between the lines to $K$ and $L$ ($\angle KCL$), which in turn is equal to the angle between the lines to $L$ and $B$ ($\angle LCB$). 

A third relay tower, $M$, is installed on the perimeter path between $B$ and $C$. Its position is fixed such that the line $KM$ perfectly bisects the angle formed by the supply route and the line back to Central Station ($\angle MKC = \angle BKM$). 

Recent data logs confirm that the line connecting relay $M$ to relay $L$ acts as the geometric bisector of the angle formed between relay $K$, relay $M$, and Base Camp $B$ ($\angle KMB$).

Based on this surveying configuration, calculate the exact measure of the angle $\angle MLC$ in degrees.

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
