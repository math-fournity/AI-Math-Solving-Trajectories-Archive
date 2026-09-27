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

In a remote desert, three research outposts—Alpha, Bravo, and Charlie—are situated in a perfectly straight line. The distance from Alpha to Bravo is 20 kilometers, and the distance from Bravo to Charlie is 18 kilometers.

At the Bravo outpost, a circular signal jammer with a constant radius $r > 0$ is activated. To secure the perimeter, two long, straight security fences are constructed: Fence 1 passes through Alpha and is perfectly tangent to the circular jamming zone, while Fence 2 passes through Charlie and is also tangent to the jamming zone. These two fences eventually intersect at a central command hub, Point K.

A straight supply road is to be paved connecting a point $X$ on the fence segment between the hub and Alpha to a point $Y$ on the fence segment between the hub and Charlie. To ensure maximum efficiency, the road $XY$ must be parallel to the straight line connecting the outposts and must also be tangent to the circular jamming zone.

As the radius of the jamming zone varies, the length of the supply road $XY$ changes. What is the largest possible integer length, in kilometers, that the supply road $XY$ can achieve?

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
