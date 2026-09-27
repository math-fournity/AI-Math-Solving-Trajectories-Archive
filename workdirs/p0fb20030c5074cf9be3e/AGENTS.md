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

In the remote digital archipelago of Gridlandia, a cyber-security firm has partitioned a massive $100 \times 100$ grid of server units into a total of $20,000$ triangular "data-nodes" (each server unit is a square divided by a diagonal into two equal right-triangular halves).

An unauthorized "Stealth-Virus" has infected a specific contiguous region within this $100 \times 100$ grid. The virus occupies a geometric shape known as a "Trident": a trapezoid with parallel bases of lengths $1$ and $3$ and a height of $1$. This Trident is formed by taking one central $1 \times 1$ square server unit and attaching two triangular data-nodes to its opposite sides. 

The security protocols define the virus’s position according to these strict parameters:
1. The Trident is located entirely within the $100 \times 100$ grid boundaries.
2. The central $1 \times 1$ square of the Trident perfectly aligns with and covers exactly one of the $1 \times 1$ server units in the grid.
3. The Trident can be oriented in any of the four cardinal directions (pointing up, down, left, or right).
4. The virus is invisible; its exact location and orientation are unknown.

To eliminate the virus, the firm must deploy "Data-Pulses." One pulse targets and completely covers exactly one triangular data-node. A pulse is successful if it intersects the interior of the Trident (meaning the intersection of the targeted triangular node and the Trident’s area is greater than zero). To fully "sink" the virus, the firm must ensure at least one pulse successfully hits it.

What is the minimum number of Data-Pulses that must be deployed to guarantee that the Stealth-Virus is hit, regardless of its location or orientation?

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
