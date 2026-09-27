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

A specialized assembly line consists of $n$ workstations arranged in a straight sequence, labeled from Station 1 to Station $n$. A quality control robot is tasked with testing the connections between these stations. 

The robot's movement protocol is strictly one-way: it starts at Station 1 and moves toward Station $n$. During a single "deployment," the robot can move between any two stations $i$ and $j$ (where $i < j$) in a single leap, but it can never move backward. Once the robot reaches Station $n$, that deployment ends, and it is reset to Station 1 to begin a new deployment.

The facility manager requires the robot to test every possible direct link between any two stations. This means for every possible pair of stations $(i, j)$ such that $1 \leq i < j \leq n$, there must be at least one deployment where the robot travels directly from Station $i$ to Station $j$ in a single jump.

What is the minimum number of deployments required to ensure that every such direct link has been traversed at least once?

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
