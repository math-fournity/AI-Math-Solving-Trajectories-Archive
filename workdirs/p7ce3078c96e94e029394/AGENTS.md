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

A specialized circular particle accelerator is initially calibrated with two primary sensors located at the exact opposite ends of its diameter. Each of these sensors registers a baseline value of 1.

The laboratory follows a specific expansion protocol to install new monitoring nodes over $n$ consecutive stages:

**Stage 1:** Engineers locate the midpoint of the two semicircular paths between existing sensors. At each of these two midpoints, they install a new node with a value equal to the sum of the values of the two sensors at the ends of that semicircle.

**Stage 2:** The circle is now divided into four arcs. Engineers locate the midpoint of each of these four arcs. At each midpoint, they install a new node with a value equal to the sum of the values of the sensors at the ends of that specific arc.

**Subsequent Stages:** This process continues for $n$ total stages. In each stage, every existing arc along the perimeter is bisected, and a new node is placed at the midpoint. The value assigned to a new node is always the sum of the values of the two nodes defining the arc it bisects.

Calculate the total sum of all the numbers written at the new nodes across all $n$ stages (excluding the two original baseline values).

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
