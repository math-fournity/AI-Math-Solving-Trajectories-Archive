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

A specialized high-tech laboratory contains a solid, uniform prototype sensor housing shaped like a perfect cube. To test its durability against rotational forces, engineers have placed the cube in a vacuum chamber. In a local 3D coordinate system where distances are measured in meters, the cube’s corners are positioned at $O(0, 0, 0)$, $A(1, 0, 0)$, $B(1, 1, 0)$, $C(0, 1, 0)$, $D(0, 0, 1)$, $E(1, 0, 1)$, $F(1, 1, 1)$, and $G(0, 1, 1)$.

The engineers initiate a high-speed test where the cube is spun rapidly around a fixed laser beam that passes exactly through the diagonal line connecting vertex $O$ to the opposite vertex $F$. As the cube rotates $360^\circ$ around this axis $OF$, it sweeps through a specific region of the surrounding space.

Calculate the total volume of the spatial region swept out by the rotating cube.

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
