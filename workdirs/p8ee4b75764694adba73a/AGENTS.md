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

A city council has established a circular network of 2012 specialized maintenance hubs to service a fleet of $N$ autonomous repair drones. To initiate the program, the Fleet Manager (A) must distribute the drones across the hubs such that every hub contains at least one drone.

The system then operates in a repeating cycle of shifts: first a System Shift (B), then a Manager Shift (A), then System, then Manager, and so on.

*   **During every System Shift (B):** The central computer automatically reassigns exactly one drone from every single hub to an adjacent hub. The computer chooses the direction (clockwise or counter-clockwise) for each hub independently.
*   **During every Manager Shift (A):** The Fleet Manager may select any number of drones to move to an adjacent hub. However, she is restricted by two safety protocols: 
    1. She cannot move any drone that was just relocated by the computer in the immediately preceding System Shift.
    2. She cannot select more than one drone from any single hub.

The Manager’s objective is to ensure that, following every one of her shifts, there is at least one drone located in every hub, regardless of the choices made by the computer or the number of shifts that pass.

What is the minimum number of drones $N$ required (where $N \geq 2012$) for the Manager to guarantee she can meet this objective indefinitely?

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
