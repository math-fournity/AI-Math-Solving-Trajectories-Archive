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

In a futuristic data center, a massive security network known as the "Hydra-Link" consists of 100 dedicated fiber-optic cables (necks). Each cable connects exactly two distinct server nodes (heads). The network is currently unified, meaning data can travel between any two nodes, potentially through intermediate connections.

An elite cyber-security specialist is tasked with decommissioning the system. The specialist can execute a "Node Reconfiguration" command on any single node $A$. When a node is reconfigured, the following occurs simultaneously:
1. All existing fiber-optic cables currently connected to node $A$ are instantly severed.
2. New fiber-optic cables are immediately generated between node $A$ and every other node in the system to which it was not previously connected.
3. At no point can more than one cable exist between the same two nodes.

The Hydra-Link is considered defeated only when the network is broken into at least two mutually disconnected components (meaning there are at least two nodes between which no path of cables exists).

What is the smallest natural number $N$ such that, regardless of the initial arrangement of the 100 cables, the specialist can defeat the Hydra-Link using no more than $N$ reconfiguration commands?

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
