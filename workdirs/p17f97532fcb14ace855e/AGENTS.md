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

In a vast, uncharted sector of the galaxy, a specialized surveillance network is being deployed to monitor deep-space activity. The network consists of two distinct types of sensor barriers:

First, there are 10 "Spherical Pulse Shields." Each shield is a perfect circular energy field of a different size and centered at a different location. These shields are positioned such that every pair of circles intersects at exactly two points, and no three circles intersect at the same point.

Second, there are 10 "Linear Beams." These are infinitely long, straight laser fences. These beams are positioned such that no two beams are parallel, and no three beams intersect at the same point. 

Furthermore, to ensure maximum coverage density, the engineers have calibrated the layout so that every linear beam intersects every circular shield at exactly two points. No beam is tangent to any circle, and no three components (whether they be three lines, three circles, or a mix of both) ever intersect at the same single coordinate.

The activation of these 20 total barriers partitions the infinite two-dimensional plane of the sector into several distinct, enclosed or open observation zones. 

Based on this configuration, what is the maximum number of distinct zones created in the sector?

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
