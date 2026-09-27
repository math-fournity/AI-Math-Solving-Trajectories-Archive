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

In the city of Gridville, a delivery drone must travel from a central hub located at intersection (0,0) to various drop-off stations located at intersections $(n,n)$ for each integer $n$ from 1 to 5. The drone can only travel in 1-unit increments, moving either North (up) or East (right) along the grid lines.

However, the city has implemented "Flow Restriction Zones" at every intermediate coordinate where the Northward and Eastward coordinates are equal and greater than zero—specifically at all points $(a,a)$ where $1 \le a < n$. At these specific intersections, the drone is forbidden from changing its direction. This means if the drone enters such a point $(a,a)$ moving East, it must exit moving East; if it enters moving North, it must exit moving North.

Let $W(n)$ represent the total number of unique valid paths the drone can take from $(0,0)$ to a specific station $(n,n)$ under these restrictions. 

Calculate the sum of the number of paths for all stations from $n=1$ to $n=5$:
$$\sum_{n=1}^{5} W(n)$$

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
