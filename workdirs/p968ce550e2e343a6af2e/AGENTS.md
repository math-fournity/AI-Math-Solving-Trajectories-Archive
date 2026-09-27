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

In a futuristic city, an automated fabric printer produces a square sheet of smart-material with a side length of $2^n$ meters for some positive integer $n$. To prepare the material for processing, a robotic arm performs a sequence of folding operations: first, it folds the sheet in half from right to left, and then it folds the resulting rectangle in half from bottom to top. This cycle of two folds is repeated until the material forms a small square with a side length of exactly 1 meter.

Once the folding is complete, a single micro-sensor is embedded into the stack at a coordinate exactly $\frac{3}{16}$ meters from the top edge and $\frac{3}{16}$ meters from the left edge of the folded square. After the sensor is placed, the robotic arm completely unfolds the sheet back to its original $2^n \times 2^n$ dimensions.

The unfolding process replicates the sensor into a large rectangular array of points across the sheet. When every adjacent pair of sensors is connected by horizontal and vertical laser lines, a grid is formed consisting of various squares and rectangles.

A nano-bot, $P$, is placed at a random location chosen uniformly from the interior of this grid. There exists a maximum rational constant $L = \frac{p}{q}$ (in lowest terms) such that, regardless of the value of $n$, the probability that the four laser segments surrounding $P$ form a perfect square is at least $L$.

Find the value of $p+q$.

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
