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

In a vast digital library, there are 1000 specialized data storage cells. Each cell is equipped with a security dial that has four distinct settings: North, East, South, and West. To transition between settings, the dial must be turned 90 degrees clockwise in a specific cycle: from North to East, East to South, South to West, and West back to North. At the start of the day, every dial is set to North.

Each storage cell is assigned a unique identification code of the form $2^x 3^y 5^z$, where $x, y, z \in \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$. This results in 1000 unique codes corresponding to the 1000 cells.

The library technician performs a maintenance protocol consisting of 1000 individual stages. In each stage, the technician selects one of the 1000 cells (ensuring every cell is chosen exactly once by the end of the protocol). When a specific cell $i$ is selected, its dial is advanced one setting clockwise. Simultaneously, the dials of every other cell whose identification code is a divisor of cell $i$’s code are also advanced one setting clockwise.

After the technician has completed all 1000 stages of the protocol, how many storage cells will have their dials pointing North?

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
