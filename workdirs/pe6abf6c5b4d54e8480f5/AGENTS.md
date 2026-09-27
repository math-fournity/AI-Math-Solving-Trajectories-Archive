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

A specialized chemical refinery uses a multi-stage synthesis process governed by a reaction function $R(c) = 2c^2 + c - 1$, where $c$ represents the concentration of a specific catalyst. 

The refinery operates in cycles. When a batch of catalyst is processed through the system once, the resulting concentration is $R(c)$. If the output is fed back into the system for a second pass, the concentration becomes $R(R(c))$. This iterative process continues such that for any non-negative integer $n$, the concentration after $n+1$ cycles is defined by $R(R^n(c))$, where $R^0(c)$ is the initial concentration $c$.

The head engineer is looking for "Stability Points": initial real-valued concentrations which, after exactly three complete cycles through the refinery, return to their exact original concentration value.

Mathematically, these are the real values of $c$ that satisfy the equilibrium condition $R^3(c) = c$.

Calculate the total number of distinct real-valued concentrations that serve as Stability Points for this process.

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
