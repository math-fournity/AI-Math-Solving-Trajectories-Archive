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

In the futuristic city of Hexagon-Zero, a grid-based automated greenhouse is organized into a $5 \times 5$ layout of planting zones. Currently, $n$ zones are occupied by fragile "Alabaster Orchids," while the remaining zones are empty. Each zone can hold at most one plant.

An agricultural robot is programmed to upgrade these orchids into "Ebony Ferns" one at a time. However, the upgrade process is delicate due to cross-pollination risks. The robot must follow a strict protocol: it picks up one Alabaster Orchid from its current zone, treats it (turning it into an Ebony Fern), and then transplants it into any currently empty zone on the $5 \times 5$ grid. The critical safety constraint is that the newly placed Ebony Fern cannot be located in a zone that is horizontally or vertically adjacent to any remaining Alabaster Orchids. Once an orchid becomes a fern, it no longer restricts the placement of future ferns.

Let $M$ be the maximum number of Alabaster Orchids that can be initially placed on the grid such that the robot can successfully convert all $M$ plants into Ebony Ferns, one by one, without ever violating the safety constraint.

Find $M$.

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
