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

In a cutting-edge laboratory, five specialized optical filter discs are being prepared for a high-security sensor. Each disc is a perfect square of identical dimensions. To facilitate precise orientation, each disc is divided into four identical quadrants by its two diagonals, forming four congruent right-triangular zones.

On each of the five discs, exactly one of these triangular zones has been coated with a unique, light-blocking ceramic film. Each disc uses a different colored film—one Red, one Blue, one Green, one Yellow, and one Purple—ensuring no two discs share the same colored opaque section.

A technician must stack all five discs directly on top of one another, ensuring all edges and vertices are perfectly aligned. A disc can be placed in any of its four possible rotational orientations (0°, 90°, 180°, or 270°) before being added to the stack. The discs are stacked with the coated side facing upward.

The goal is to assemble the stack such that it is completely opaque when viewed from above—meaning that in every one of the four triangular zones, there is at least one opaque colored film blocking the light. 

How many unique configurations of the five-disc stack exist that result in a completely opaque assembly?

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
