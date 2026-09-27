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

A high-tech server farm is organized into an $8 \times 8$ grid of data nodes. The system administrator, Jerry, is monitoring a potential security breach. He knows that 3 specific nodes, designated as "R-type," are infected with a virus, and 2 specific nodes, designated as "K-type," are infected with a worm. Additionally, there is exactly one "Hybrid" node that contains both the virus and the worm, but this node has no designation. All other nodes in the grid are clean.

Jerry provides the security team with two structural constraints regarding the grid's layout:
1. In any $6 \times 6$ sub-grid of nodes, there are at least 2 nodes containing the virus (this includes "R-type" nodes and the "Hybrid" node).
2. In any $3 \times 3$ sub-grid of nodes, there is at most one node containing the worm (this includes "K-type" nodes and the "Hybrid" node).

The security team needs to isolate the "Hybrid" node by manually inspecting nodes one by one. What is the minimum number of nodes they must inspect to guarantee they have found the node containing both the virus and the worm?

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
