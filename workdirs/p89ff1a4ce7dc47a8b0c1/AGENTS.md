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

In a remote digital archipelago, there are 2009 server nodes arranged in a perfect circle, indexed sequentially from 1 to 2009. A single data packet begins at Node 1. Two network administrators, Alice and Bob, take turns rerouting this packet to different nodes.

Alice always takes the first turn. On her turn, she must move the packet to a node immediately adjacent to its current location (either one step clockwise or one step counter-clockwise). When the packet arrives at a node Alice has moved it to, she installs a permanent security firewall there, provided the node does not already have one.

Bob takes the second turn. On his turn, he must move the packet to one of the two nodes that are geographically furthest from its current position. (In this 2009-node ring, if the packet is at node $i$, the furthest nodes are those located exactly 1004 and 1005 steps away). Bob does not install any firewalls; he only relocates the packet.

The process continues indefinitely until Alice can no longer move the packet to an adjacent node that is not already marked with her firewall. What is the maximum number of nodes Alice can guarantee will be marked with her security firewalls, regardless of the relocation strategy Bob employs?

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
