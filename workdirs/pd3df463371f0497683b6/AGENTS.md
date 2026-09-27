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

In a remote digital frontier, a System Administrator and a Malicious Script engage in a persistent battle over a server cluster organized as a $2022 \times 2022$ grid of data nodes. Each node represents a storage unit, and two nodes are considered linked if they share a vertex or an edge in the grid layout. Initially, every node contains a data file with a security level of 0.

The conflict proceeds in discrete cycles:
1. First, the Administrator selects a single node to receive a manual security patch. This action increases the security level by 1 for that specific node and all of its linked neighbors (a total of four to nine nodes depending on the position).
2. Second, the Malicious Script targets exactly four nodes. The security level of each targeted node decreases by 1, though it cannot drop below 0.

A node is classified as "Hardened" if its security level reaches at least $10^6$. Despite the script's optimal efforts to weaken the system, the Administrator aims to maximize the number of Hardened nodes within a finite number of cycles.

Find the largest integer $A$ such that the Administrator can guarantee that at least $A$ nodes are Hardened, regardless of the script's targeted deletions.

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
