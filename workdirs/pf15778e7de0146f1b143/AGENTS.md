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

In a specialized logistics hub, there are 31 distinct types of essential components. Initially, the inventory contains 31 "Basic Kits." Each Basic Kit consists of exactly one unit of a specific component type and zero units of all others. Specifically, for each $i$ from 1 to 31, there is a kit represented by a vector where the $i$-th entry is 1 and all other entries are 0.

The facility operates using a "Combination Protocol." In a single move, technicians select any two kits currently available in the inventory (including those created in previous moves) and combine their contents to create a new, additional kit. The quantities of each of the 31 components in the new kit are the sums of the quantities of the corresponding components in the two selected kits. The original kits used in the move remain in the inventory and can be used again for future combinations.

The goal of the hub is to produce 31 specific "Advanced Kits." Each Advanced Kit must contain exactly zero units of one specific component type and exactly one unit of every other component type. That is, for each $j$ from 1 to 31, there must be a kit in the inventory represented by a vector where the $j$-th entry is 0 and all other 30 entries are 1.

What is the minimum number of moves required to ensure that all 31 Advanced Kits are present in the inventory?

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
