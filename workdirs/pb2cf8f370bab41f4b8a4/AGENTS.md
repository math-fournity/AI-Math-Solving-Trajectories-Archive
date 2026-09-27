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

In a remote industrial research facility, a circular control console contains 2,018 distinct sensor ports arranged at the vertices of a perfectly regular 2,018-sided polygon. To calibrate the system, a technician must install 2,018 unique microchips, labeled with the serial numbers $1, 2, 3, \dots, 2018$, into these ports such that every port contains exactly one chip.

The facility’s safety protocol requires a specific "balanced load" configuration. Because the ports are arranged in a circle, every port has a direct antipode (the port exactly opposite it across the center of the console). The protocol dictates that for any two adjacent ports on the console, the sum of the serial numbers of the chips installed in them must be exactly equal to the sum of the serial numbers of the chips installed in their two respective antipodal ports.

The console is mounted on a rotating base, and two chip arrangements are considered identical if one can be transformed into the other simply by rotating the console.

Based on these technical constraints, determine the total number of distinct ways the 2,018 microchips can be arranged on the console.

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
