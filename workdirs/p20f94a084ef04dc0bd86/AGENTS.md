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

A metropolitan city grid is organized into 100 horizontal avenues and 100 vertical streets. Within this grid, there are 10,000 intersections. Currently, the city has installed exactly 300 blue security cameras at these intersections, with the specific constraint that every single avenue contains exactly 3 cameras and every single street contains exactly 3 cameras.

The city planning department has decided to upgrade some of these existing blue cameras to advanced red models. They want to select a subset of $k$ blue cameras to be replaced by red ones. However, due to interference issues, it is strictly forbidden to have a configuration where four red cameras form a compact $2 \times 2$ square (i.e., four red cameras located at the intersections of two adjacent avenues and two adjacent streets).

Determine the largest positive integer $k$ such that, regardless of the initial distribution of the 300 blue cameras (as long as the 3-per-row/column rule is satisfied), it is always possible to select and upgrade at least $k$ of them to red without creating any $2 \times 2$ red squares.

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
