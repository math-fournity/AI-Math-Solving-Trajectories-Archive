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

In a remote digital archipelago, a network architect is testing the resilience of a circular mainframe cluster. The cluster consists of 2013 server nodes arranged in a perfect ring, corresponding to the vertices of a regular 2013-gon. In this network, every pair of adjacent nodes is linked by exactly two independent fiber-optic cables.

An automated "Cleanup Protocol" is initiated starting at a specific node. The protocol operates according to the following rules:
1. Every minute, the protocol checks the current node for any active fiber-optic cables connected to it.
2. If at least one active cable exists at the current node, the protocol selects one such cable uniformly at random, traverses it to the connected adjacent node, and immediately deactivates (deletes) that cable.
3. If no active cables are connected to the current node, the protocol terminates permanently.

The protocol's objective is to traverse and deactivate every single cable in the entire network before it is forced to stop.

The probability that the Cleanup Protocol successfully deactivates all the cables can be expressed as a fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Determine the remainder when $m+n$ is divided by $1000$.

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
