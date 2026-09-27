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

A specialized radar station is situated at the center of a semicircular security perimeter, defined by a straight boundary wall $AB$. A reconnaissance drone flies in a strictly linear path, entering the restricted airspace at point $D$ and exiting the semicircle at point $C$. The drone continues along this same straight line until it reaches a signal tower located at point $E$, which sits on the extension of the boundary wall $AB$ beyond the gate at $B$.

The flight path is characterized by two specific geometric conditions:
1. The direct distance from the gate $B$ to the entry point $D$ is exactly equal to the distance from the gate $B$ to the signal tower $E$.
2. An observer standing at the far end of the wall at point $A$ measures the angle between the wall $AB$ and the drone's entry point $D$ as having an angular spread of $27^\circ$ relative to the exit point $C$ (specifically, $\angle DAC = 27^\circ$).

Find the measure of the angle $\alpha$ formed at the exit point $C$ between the entry point $D$ and the far end of the boundary wall $A$ (the size of $\angle ACD$).

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
