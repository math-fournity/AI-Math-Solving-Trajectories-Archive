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

In a remote digital network, there are 18 secure servers. To ensure redundancy, every single server is directly connected to every other server by a single dedicated fiber-optic cable. Each cable is set to one of two modes: "Active" (transmitting data) or "Passive" (idle).

At a specific central server, designated as Server Alpha, the total number of Active cables connected to it is an odd integer. For the remaining 17 servers in the network, the distribution of Active cables is unique to each; that is, no two of these 17 servers have the same number of Active cables connected to them.

An analyst is studying "Data Clusters," which are groups of three servers. Specifically, the analyst identifies two types of clusters:
- Type M: A cluster where all three interconnecting cables between the three servers are "Active."
- Type N: A cluster where exactly two of the interconnecting cables are "Active" and one is "Passive."

Let $m$ be the total number of Type M clusters and $n$ be the total number of Type N clusters found within the entire network of 18 servers. 

Find the value of $m + n$.

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
