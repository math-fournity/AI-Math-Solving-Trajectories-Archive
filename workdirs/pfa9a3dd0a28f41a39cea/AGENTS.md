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

In a remote digital network, there are $n$ distinct server nodes (where $n \geq 3$). No three nodes are arranged in a linear configuration that would allow a single transmission line to pass through them. Currently, there are $k$ active fiber-optic cables, each connecting a pair of nodes. 

Two hackers, Foma and Erema, engage in a system-control game. Foma begins by selecting any two nodes in the network; he designates one as the "Source" ($A$) and the other as the "Target" ($B$). He then places a data packet at the Source node.

The game proceeds in alternating turns. On each of Erema’s turns, he must move the data packet from its current node to an adjacent node via an existing fiber-optic cable. On each of Foma’s turns, he permanently deletes one fiber-optic cable from the network (the nodes themselves remain intact). 

Erema’s objective is to successfully navigate the packet to the Target node $B$. Foma’s objective is to prune the network such that the packet can never reach $B$, regardless of Erema's maneuvers.

The number of nodes $n$ is a fixed constant. What is the maximum initial number of cables $k$ such that Foma can always guarantee he can prevent the packet from reaching the Target, no matter how the $k$ cables were originally distributed across the $n$ nodes?

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
