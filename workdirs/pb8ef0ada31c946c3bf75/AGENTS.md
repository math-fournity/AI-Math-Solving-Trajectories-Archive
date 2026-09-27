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

A high-security data center consists of a grid of $99 \times 99$ individual server nodes. Each node is identified by its coordinates $(x, y)$, where $1 \le x \le 99$ represents the column and $1 \le y \le 99$ represents the row. Every single node in this grid is managed by a dedicated AI maintenance bot.

There are two types of AI bots: "Sentinels," which are programmed to always provide accurate data, and "Fabricators," which are programmed to always provide false data. It is a known security protocol that within every single row and every single column of the grid, there are at least $k$ Sentinels. 

Deep within the grid, there is one specific node containing a master file called "Knowitall." All $99^2$ bots in the network are programmed with the exact coordinates of the node where "Knowitall" is stored. You are an external auditor trying to locate the "Knowitall" node. You cannot distinguish a Sentinel from a Fabricator by appearance.

To find the file, you can ping any node $(x_1, y_1)$ and ask the resident bot: "What is the network latency distance from your node to the Knowitall node $(x_2, y_2)$?" The network latency distance $\rho$ is defined strictly as $\rho = |x_1 - x_2| + |y_1 - y_2|$. A Sentinel will return the true value of $\rho$, while a Fabricator will return any value other than the true value of $\rho$.

What is the smallest value of $k$ that guarantees you can uniquely identify the location of the "Knowitall" node, regardless of the distribution of the bots or the specific lies told by the Fabricators?

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
