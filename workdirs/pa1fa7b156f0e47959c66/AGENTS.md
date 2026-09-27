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

In the competitive world of high-performance server architecture, a lead engineer is designing a daisy-chained data processing sequence. The system consists of $n$ distinct server towers, indexed $1, 2, \ldots, n$. Each tower is assigned a unique positive integer processing power, denoted as $s_1, s_2, \ldots, s_n$.

The efficiency of the connection between two adjacent towers is calculated by taking the processing power of the transmitting tower and raising it to the power of the receiving tower’s processing power. For the chain to remain synchronized, the energy output of every link in the sequence must be identical. Specifically, the energy of the first link ($s_1$ raised to the power of $s_2$) must equal the energy of the second link ($s_2$ raised to the power of $s_3$), and so on, continuing until the final link ($s_{n-1}$ raised to the power of $s_n$).

Determine the greatest possible number of server towers $n$ that can be included in this chain such that all towers have distinct positive integer processing powers and all $n-1$ energy outputs are perfectly equal.

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
