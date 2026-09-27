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

A specialized laser-cutting drone is programmed to navigate the exterior surface of a tetrahedral monument that has been built as a perfect square pyramid. The monument's peak is designated as point $S$, and its four base corners are $A, B, C$, and $D$ in clockwise order. The distance from the peak $S$ to the corner $A$ is exactly 1 kilometer. Each of the four triangular side faces is identical, with the angle between the structural beams $AS$ and $BS$ measuring exactly $30^\circ$.

The drone must perform a continuous perimeter scan starting at corner $A$. It is required to travel across the faces of the pyramid to eventually return to corner $A$. To complete the scan, the drone's path must cross the support beams $BS$, $CS$, and $DS$ (in any order), but it is strictly forbidden from crossing back over the starting beam $AS$ until it reaches the final destination point $A$.

Find the length of the shortest possible path the drone can take to complete this circuit. If the shortest path length is expressed as an irreducible fraction $\frac{a}{b}$, what is the value of $a+b$?

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
