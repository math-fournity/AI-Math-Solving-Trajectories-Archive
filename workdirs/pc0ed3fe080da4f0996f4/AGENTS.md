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

In the remote digital kingdom of Aetheria, three power hubs—Alpha ($a$), Beta ($b$), and Gamma ($c$)—generate varying levels of positive energy. The network's efficiency is governed by a complex stability protocol.

The primary energy output of the system is calculated by the sum of three directional transmission ratios: the fourth power of Alpha’s energy divided by the square of Beta’s, the fourth power of Beta’s divided by the square of Gamma’s, and the fourth power of Gamma’s divided by the square of Alpha’s.

To maintain network equilibrium, the High Architect adds a stabilization factor. This factor is determined by taking a constant safety coefficient $k$ and multiplying it by the sum of the pairwise energy interactions (Alpha times Beta, Beta times Gamma, and Gamma times Alpha).

The protocol mandates that the combined total of the primary energy output and the stabilization factor must always be greater than or equal to a specific threshold. This threshold is defined as the successor of the safety coefficient $(k+1)$ multiplied by the sum of the squares of the individual energy levels of the three hubs ($a^2 + b^2 + c^2$).

As the Architect, you must determine the highest possible value for the safety coefficient $k$ that ensures this stability inequality remains true for all possible positive energy levels $a, b$, and $c$ across the hubs. What is the maximum value of $k$?

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
