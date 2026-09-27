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

In a specialized logistics hub, a freight processing system operates on a set of non-negative rational input values, denoted as $Q_{\geq 0}$, and produces an output efficiency rating $f(z)$. The system is governed by three fundamental operational protocols:
1.  **Additive Shift:** Increasing the input load by exactly one unit increases the efficiency rating by exactly one unit ($f(z+1) = f(z) + 1$).
2.  **Reciprocal Symmetry:** For any non-zero input, the system yields the same efficiency rating as it would for the reciprocal of that load ($f(1/z) = f(z)$).
3.  **Baseline:** An input load of zero results in an efficiency rating of zero ($f(0) = 0$).

To determine the specific input for a high-priority stress test, the engineering team uses a recursive sequence $P_n$ to define the dimensions of a gear system. The sequence is defined as follows:
-   The base gear $P_0$ has 0 teeth.
-   The first gear $P_1$ has 1 tooth.
-   Each subsequent gear $P_n$ is manufactured such that its tooth count is equal to twice the tooth count of the previous gear plus the tooth count of the gear before that ($P_n = 2P_{n-1} + P_{n-2}$ for $n \geq 2$).

The engineers decide to run the system with a load $z$ equal to the ratio of the tooth count of the 20th gear to the tooth count of the 24th gear ($z = \frac{P_{20}}{P_{24}}$). Calculate the efficiency rating $f\left(\frac{P_{20}}{P_{24}}\right)$ produced by the system.

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
