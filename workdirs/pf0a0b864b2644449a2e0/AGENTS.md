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

In a specialized nanotechnology lab, a scientist begins with a "Type-0" metallic tile shaped like a capital L, formed by joining three identical square atoms. This specific tile is oriented with its corner in the bottom-left, one arm extending upward and one arm extending to the right.

The lab uses a "Quad-Splitter" device. In a single cycle, this device takes any L-shaped tile and subdivides it into exactly 4 smaller, congruent L-shaped tiles. When the original Type-0 tile is processed through its first cycle, it produces 4 "Type-1" tiles. Due to the geometry of the split, these 4 smaller tiles are arranged such that:
- Two of them are rotated 90 degrees relative to the original.
- One of them is rotated 180 degrees relative to the original.
- One of them maintains the exact same orientation as the original.

The scientist continues this process recursively. In each subsequent cycle, every smaller L-shaped tile produced in the previous step is fed back into the Quad-Splitter. Each tile, regardless of its current orientation, is subdivided into 4 even smaller L-shaped tiles using the same relative geometric rule (where 1 of the 4 new sub-tiles matches the orientation of the tile being split, 2 are rotated 90 degrees relative to it, and 1 is rotated 180 degrees relative to it).

After exactly 2005 successive cycles of subdivision, the original tile has been transformed into a total of $4^{2005}$ tiny L-shaped tiles. Calculate the total number of these final tiles that are in the same orientation as the original "Type-0" tile.

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
