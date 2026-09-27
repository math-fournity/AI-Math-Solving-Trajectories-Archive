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

A high-tech manufacturing facility operates 31 specialized fabrication modules. At the start of the production cycle, the central control system generates 31 "Primary Resource Kits." Each kit contains exactly one unit of a unique resource and zero units of all others. Specifically, for each $i$ from 1 to 31, there is a kit represented by a 31-dimensional vector where the $i$-th coordinate is 1 and all other coordinates are 0.

The facility uses a "Combination Protocol" to create new resource kits. In a single operation, a technician selects any two kits currently available in the system's inventory and combines their contents to create a new kit. The quantity of each resource in the new kit is the sum of the quantities of that resource from the two selected kits. The two original kits remain in the inventory and can be reused for future operations.

The goal of the facility is to produce a specific set of 31 "Advanced Composite Kits." Each of these target kits must contain zero units of exactly one resource and exactly one unit of every other resource. Specifically, for each $j$ from 1 to 31, the facility must eventually have a kit in its inventory where the $j$-th coordinate is 0 and all other 30 coordinates are 1.

What is the minimum number of operations required to ensure that all 31 Advanced Composite Kits are present in the facility's inventory?

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
