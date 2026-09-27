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

A specialized textile factory produces a hexagonal "Master Patch" made of a rare fabric with a total surface area of 1 unit. The patch is initially a perfect regular hexagon. To refine the design into more intricate shapes, a tailoring robot performs a sequence of "corner trims."

A single corner trim involves identifying two consecutive edges of the current patch, $AB$ and $BC$, which meet at a corner $B$. The robot marks the exact midpoint $M$ of edge $AB$ and the exact midpoint $N$ of edge $BC$. It then cuts along the straight line $MN$ and discards the small triangular piece $MBN$, effectively replacing the two original edges with three new segments: $AM$, $MN$, and $NC$. This process increases the number of sides of the patch by one.

The robot continues to perform these trims indefinitely, one after another, in any order it chooses, creating a sequence of increasingly complex polygons. The factory needs to determine the absolute "safety floor" for the fabric area. 

Calculate $L$, where $L$ is the largest real number such that the area of the patch remains strictly greater than $L$ after any number of trims, no matter which corners are selected in what order.

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
