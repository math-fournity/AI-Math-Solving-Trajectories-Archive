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

In a sprawling logistics hub, two primary conveyor belt routes, Route Alpha-Echo and Route Delta-Bravo, intersect at a central junction, point $C$. 

The Alpha-Echo route consists of a continuous straight line segment measuring exactly 17 kilometers. This route passes through the junction $C$ in such a way that it perfectly bisects the Delta-Bravo route, splitting it into two equal segments: $DC$ and $CB$.

An engineer measuring the distances between key access points finds that the distance between the starting terminal $A$ and the distribution hub $B$ is 5 kilometers. Furthermore, the length of the conveyor track from the distribution hub $B$ back to the central junction $C$ is exactly 6 kilometers.

Using a precision transit, a surveyor determines that the angle formed between the path from terminal $A$ to hub $B$ and the path from terminal $A$ to the junction $C$ (angle $BAC$) is exactly $78^\circ$.

Based on these structural specifications, what is the measure of the angle formed between the path from the junction $C$ to the terminus $D$ and the path from the terminus $D$ to the end of the first route at $E$ (angle $CDE$)?

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
