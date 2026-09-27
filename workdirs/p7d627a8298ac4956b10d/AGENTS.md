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

In a specialized logistics hub, there are $p$ automated processing lines that manage the distribution of resources across $q$ different cargo containers, where the number of containers $q$ is exactly twice the number of lines ($q = 2p$). Each line $i$ calculates a total balance by summing the weighted contribution of each container $j$. The weight applied to container $j$ by line $i$, denoted as $a_{ij}$, is restricted to the values $\{-1, 0, 1\}$.

A "Perfect Equilibrium" is reached if every single processing line results in a total sum of exactly zero. The hub manager is searching for a specific configuration of integer cargo loads $(x_1, \dots, x_q)$ to achieve this equilibrium. 

To find a guaranteed solution using the Pigeonhole Principle, the manager considers all possible cargo load vectors where each individual load $x_j$ is an integer restricted to the range $0 \leq x_j \leq q$. By comparing the total number of such potential vectors to the total number of possible outcomes for the $p$ linear balance equations, the manager can guarantee the existence of at least one non-zero integer solution vector where the absolute value of every load $|x_j|$ does not exceed a specific bound $K$. 

Based on this specific Pigeonhole Principle argument, what is the smallest integer value for $K$ that can be guaranteed for any such system?

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
