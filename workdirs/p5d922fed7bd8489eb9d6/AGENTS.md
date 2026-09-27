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

In the city of Gridville, a specialized maintenance robot travels across a rectangular sensor array. The array is defined by integer coordinates $(x, y)$ where $0 \leq x \leq 11$ and $0 \leq y \leq 9$.

The robot’s path is a sequence of distinct sensor locations $(s_0, s_1, \dots, s_n)$ for any total number of steps $n \geq 2$. The mission must begin with the robot at sensor $s_0 = (0,0)$ and its first move taking it to sensor $s_1 = (1,0)$. 

For every subsequent step $i$ (where $2 \leq i \leq n$), the robot’s next position $s_i$ is determined by its two previous positions. Specifically, $s_i$ must be the result of taking the position $s_{i-2}$ and rotating it clockwise around the current position $s_{i-1}$ by either $90^{\circ}$ or $180^{\circ}$. Every sensor location in the sequence must be unique, and the robot must never move outside the boundaries of the $12 \times 10$ sensor grid.

How many such unique sequences of sensor locations can the robot possibly record?

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
