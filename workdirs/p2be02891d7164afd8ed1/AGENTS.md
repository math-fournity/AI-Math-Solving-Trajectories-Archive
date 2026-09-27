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

In a specialized logistics hub, three cargo drones—X-ray, Yankee, and Zulu—are tasked with transporting high-value micro-components. The efficiency of the operation is measured by a specific performance index.

Let $X$ represent the weight of the payload carried by drone X-ray, $Y$ represent the weight carried by drone Yankee, and $Z$ represent the weight carried by drone Zulu, where all weights are positive real values.

The hub's supervisor calculates the "System Efficiency Ratio" using the following formula:
The numerator is the product of the three payloads: $X \cdot Y \cdot Z$.
The denominator is the product of four specific capacity-adjusted factors:
1. The first factor is $(1 + 3X)$.
2. The second factor is $(X + 8Y)$.
3. The third factor is $(Y + 9Z)$.
4. The fourth factor is $(6 + Z)$.

To optimize the hub's budget for the next quarter, the supervisor needs to determine the theoretical lower bound of this ratio.

Find the minimum value of $\frac{XYZ}{(1+3X)(X+8Y)(Y+9Z)(6+Z)}$ for all positive real numbers $X, Y, Z$.

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
