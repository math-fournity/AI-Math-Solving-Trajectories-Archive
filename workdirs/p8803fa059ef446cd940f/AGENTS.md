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

In a remote industrial facility, three concentric circular tracks are monitored by three robotic inspection arms: the "S-Arm," the "M-Arm," and the "H-Arm." Each arm rotates around the center at a constant, uniform speed. 

The S-Arm is the fastest, completing one full revolution every minute. The M-Arm completes one full revolution every hour. The H-Arm is the slowest, requiring exactly 12 hours to complete a single revolution. 

At the start of a 24-hour observation period (Time 0:00), all three arms are perfectly aligned at the zero-degree mark. 

Throughout the 24-hour duration, there are specific moments when one arm positions itself such that it is exactly 30 degrees away from each of the other two arms (effectively acting as the angle bisector of a 60-degree arc between the other two, or being 30 degrees offset from two arms that are currently overlapping).

During the 24-hour period following the initial alignment, how many times does it occur that one arm forms an angle of exactly 30 degrees with each of the other two?

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
