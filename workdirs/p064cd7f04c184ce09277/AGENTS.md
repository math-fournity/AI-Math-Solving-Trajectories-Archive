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

11.5. In Flower City, there live $99^{2}$ dwarfs. Some of the dwarfs are knights (always tell the truth), while the rest are liars (always lie). The houses in the city are located in the cells of a $99 \times 99$ square (a total of $99^{2}$ houses, arranged in 99 vertical and 99 horizontal streets). Each house is inhabited by exactly one dwarf. The house number is denoted by a pair of numbers $(x ; y)$, where $1 \leqslant x \leqslant 99$ is the number of the vertical street (numbers increase from left to right), and $1 \leqslant y \leqslant 99$ is the number of the horizontal street (numbers increase from bottom to top). The Flower City distance between two houses with numbers $\left(x_{1} ; y_{1}\right)$ and $\left(x_{2} ; y_{2}\right)$ is the number $\rho=\left|x_{1}-x_{2}\right|+\left|y_{1}-y_{2}\right|$. It is known that on each street, whether vertical or horizontal, there live at least $k$ knights. In addition, all dwarfs know which house Knight Knowitall lives in. You want to find his house, but you do not know what Knowitall looks like. You can approach any house and ask the dwarf living there: “What is the Flower City distance from your house to the house of Knowitall?”. For what smallest $k$ can you guarantee to find the house of Knowitall? (V. Novikov)

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
