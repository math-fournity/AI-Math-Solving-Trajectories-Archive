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

In a futuristic automated logistics facility, there is a grid-based storage floor consisting of a $19 \times 19$ arrangement of docking zones. The facility operates using $n$ specialized transport bots, each occupying a single distinct zone.

The facility’s protocol dictates a synchronized operational cycle. In every cycle, every single bot must simultaneously relocate to an adjacent zone (moving exactly one step north, south, east, or west). To prevent collisions, two bots are never permitted to move into the same zone during the same cycle. Additionally, to prevent mechanical wear on the treads, no bot is allowed to move along the same axis in two consecutive cycles; for example, if a bot moves horizontally (east or west) in one cycle, its very next move must be vertical (north or south), and vice versa.

The facility director wants to maximize the number of bots deployed while ensuring that the system can continue these synchronized movements indefinitely without ever violating the collision or directional constraints.

What is the maximum number of bots $n$ that can be placed on the grid such that they can continue to move indefinitely under these rules?

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
