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

In a remote digital archipelago, there are 100 isolated server nodes. Connectivity between any two distinct nodes is strictly governed by a dual-protocol system: they are either linked by a Fiber-optic cable, linked by a Satellite link, or have no direct connection at all. No two nodes share both types of connections.

The network architecture is constrained by two strict protocols:
1. If any two nodes are each connected to a common third node via Fiber-optic cables, those two nodes must be directly linked to each other via a Satellite link.
2. If any two nodes are each connected to a common third node via Satellite links, those two nodes must be directly linked to each other via a Fiber-optic cable.

Following a severe solar storm, all Satellite links have been permanently disabled, leaving only the Fiber-optic cables functional. To maintain system integrity, "Master Nodes" must be designated among the 100 servers. A node is considered "covered" if it is either a Master Node itself or if it can reach a Master Node through a path consisting of one or more active Fiber-optic cables.

Determine the minimum number of Master Nodes that must be established to guarantee that every node in the archipelago is covered, regardless of how the connections were originally configured under the protocols.

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
