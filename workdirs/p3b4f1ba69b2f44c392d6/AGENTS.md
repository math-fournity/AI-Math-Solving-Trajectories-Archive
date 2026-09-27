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

In a remote industrial facility, two automated cargo drones, Unit Alpha and Unit Beta, are positioned at a loading dock designated as "Station 0." The facility features 8 docking stations arranged in a perfect circle, numbered 0 through 7, where Station 0 acts as the primary hub. Both drones begin their mission at Station 0.

To determine their progress through the circuit, a control system generates two random integers between 1 and 6 (simulating two dice) for each cycle. The movement protocol is as follows:

1. If the two integers are identical, the drones remain stationary, and the system generates a new pair of integers. This does not count as a completed cycle.
2. If the integers are different, the drone assigned the higher number advances 2 stations clockwise.
3. Simultaneously, the drone assigned the lower number advances only 1 station clockwise.
4. Each instance where the drones move (following the generation of different integers) is recorded as exactly one "movement cycle."

Because the stations are arranged in a circle, a drone reaching or passing Station 7 continues back to Station 0 to begin a new lap. 

The mission protocol dictates that the operation terminates immediately after a movement cycle if at least one drone lands exactly on Station 0. 
- A "Single Success" occurs if only one drone is at Station 0; the operation ends.
- A "System Draw" occurs if, at the end of a movement cycle, both Unit Alpha and Unit Beta have landed exactly on Station 0.

What is the smallest possible number of movement cycles required for the operation to end in a System Draw? Justify your answer.

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
