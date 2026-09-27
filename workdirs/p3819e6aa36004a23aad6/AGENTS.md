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

In a specialized cyber-security simulation, a Data Packet (Agent A) and a Virus (Agent B) inhabit a network of $n > 2$ nodes. Two specific nodes are designated as the Secure Server (Node B) and the Entry Point (Node A). These two nodes are distinct and are not directly linked by a connection. 

At the start of the simulation, Agent A is positioned at the Entry Point and Agent B is at the Secure Server. The simulation operates in synchronized cycles. In every cycle, both agents must act simultaneously:
1. Agent B must move to a node directly connected to its current location.
2. Agent A may either move to a node directly connected to its current location or remain at its current node.

Agent B has full visibility of Agent A’s location at all times, whereas Agent A has no information regarding the location of Agent B. Agent A fails the mission if it ever occupies the same node as Agent B at the end of a cycle. Agent A succeeds and wins the game if it reaches the Secure Server (Node B) without being on the same node as Agent B during that cycle or any previous cycle.

Let $E(n)$ represent the maximum number of edges a connected network of $n$ nodes can have such that Agent A is guaranteed to have a winning strategy, regardless of Agent B’s movements.

Compute the value of $E(10) + E(11)$.

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
