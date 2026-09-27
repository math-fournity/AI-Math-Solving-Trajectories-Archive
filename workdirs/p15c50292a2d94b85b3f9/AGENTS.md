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

A textile manufacturer is overlaying two rectangular mesh screens to create a specialized filtration pattern. 

The first screen is a large square frame with a side length of 2009 units, featuring a grid of wires spaced exactly 1 unit apart (creating a $2009 \times 2009$ grid of $1 \times 1$ squares). The second screen is a smaller square frame with a side length of 1489 units, also containing a grid of wires spaced 1 unit apart. 

To create the filter, the smaller square frame is "inscribed" within the larger square frame. Specifically, the four vertices of the smaller square are positioned so that they lie exactly on the four outer boundary edges of the larger square. Because the side lengths are not equal, the smaller square is necessarily rotated at a specific angle relative to the larger square to make this fit possible.

The "lattice points" of each screen are the junctions where its internal grid wires intersect, including the points along the boundary edges of that specific square.

Given this configuration, how many precise points in space are occupied by a grid junction from both the larger screen and the smaller screen simultaneously?

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
