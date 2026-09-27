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

A network architecture consists of $2021$ individual server nodes positioned such that no three nodes are perfectly aligned in a straight line. Physical fiber-optic cables are installed between every possible pair of nodes, resulting in a total of $\binom{2021}{2}$ unique links. 

Each cable requires a signal repeater located exactly at its geographic midpoint. Currently, $k$ of these cables have had their repeaters installed. An engineer, Vikram, needs to install a repeater at the midpoint of one of the remaining unmarked cables. 

Vikram has a high-precision surveying laser (a straightedge) that can only draw straight lines through any two existing points (either server nodes or previously installed repeaters). He can then mark the intersection of any two lines he has drawn. It is a known technical property of this network topology that if at least one repeater is already installed, Vikram can use his laser to find the exact midpoint of any other cable in the system.

What is the minimum value of $k$ such that, regardless of which specific $k$ cables were initially chosen for repeater installation, Vikram is guaranteed to have enough information to construct the midpoint of any of the remaining $\binom{2021}{2} - k$ segments?

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
