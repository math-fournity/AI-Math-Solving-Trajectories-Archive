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

In a remote industrial zone, two solar-powered telecommunications arrays are being installed on a triangular plot of land formed by three intersecting maintenance roads. The two roads that meet at the central junction $C$ are perfectly perpendicular to each other, forming the legs of a right triangle. The third road, serving as the hypotenuse $AB$, has a length of $c$ kilometers, where $c$ is an integer.

Two different square foundation designs are proposed for the solar equipment:

1. **The "Alignment" Foundation:** A square foundation with area $S$ is built such that two of its corners lie directly on the hypotenuse road $AB$, one corner lies on road $BC$, and the final corner lies on road $AC$.
2. **The "Corner" Foundation:** A square foundation with area $T$ is built such that one of its corners is exactly at the junction $C$. Of its remaining corners, one lies on road $AC$, one lies on road $BC$, and the fourth lies on the hypotenuse road $AB$.

Engineers define two efficiency metrics, $s$ and $t$, calculated as half the area of the foundations: $s = S/2$ and $t = T/2$. Both $s$ and $t$ must be natural numbers that share no common factors other than 1 (mutually coprime).

Find the smallest possible integer length of the hypotenuse $c$ that allows for the existence of such a triangular plot and foundation layouts.

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
