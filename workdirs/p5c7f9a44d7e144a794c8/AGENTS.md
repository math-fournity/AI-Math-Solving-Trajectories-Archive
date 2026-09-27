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

In a specialized logistics simulation, a network analyst is calculating the "Interference Coefficient" of four distinct delivery drones. Each drone's mission is defined by two spatial coordinates representing its velocity vector:
- Drone 1: $(a, b)$
- Drone 2: $(c, d)$
- Drone 3: $(x, y)$
- Drone 4: $(z, t)$

The total potential energy of the system is defined by the absolute capacity of the fleet, calculated as the square of the sum of the magnitudes of these four vectors:
$\left(\sqrt{a^2+b^2}+\sqrt{c^2+d^2}+\sqrt{x^2+y^2}+\sqrt{z^2+t^2}\right)^2$.

The "Operational Drag" of the system is a value determined by the interaction of these coordinates, calculated as:
$ad-bc+yz-xt+(a+c)(y+t)-(b+d)(x+z)$.

The lead engineer determines that there exists a universal safety constant $k$ such that the Operational Drag never exceeds $k$ times the total potential energy, regardless of what real numbers are assigned to the coordinates $a, b, c, d, x, y, z,$ and $t$.

What is the smallest value of $k$ for which this inequality holds for any 8 real numbers?

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
