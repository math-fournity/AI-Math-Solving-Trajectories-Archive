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

In a vast automated warehouse, a technician named Lucky is tasked with managing a single, infinite row of storage bins indexed by every integer on a number line. Initially, every bin contains a single "Active" beacon. Lucky begins his shift standing exactly at bin 0, facing toward the positive direction (increasing bin numbers).

Lucky follows a strict mechanical protocol. At each step of his shift, he inspects the current bin he is standing over and performs one of three actions based on the status of the beacon in that bin:

1.  **If he finds an "Active" beacon:** He toggles it to "Standby" mode, performs a 180-degree turn to face the opposite direction, and walks forward one unit to the next bin.
2.  **If he finds a "Standby" beacon:** He removes the beacon from the bin entirely (leaving the bin empty), maintains his current facing direction, and walks forward one unit to the next bin.
3.  **If he finds an empty bin:** He places a new "Active" beacon into the bin, maintains his current facing direction, and walks forward one unit to the next bin.

Lucky repeats this three-option procedure over and over. The process terminates immediately the moment there are exactly 20 "Standby" beacons existing across the entire warehouse. 

How many total procedures (steps) has Lucky performed when the process finally stops?

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
