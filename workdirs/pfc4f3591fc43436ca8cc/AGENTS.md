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

In a specialized vertical greenhouse, five distinct plant varieties are arranged in a circular sequence of pots, labeled Pot 1 through Pot 5. A botanist must select a growth height (measured in whole decimeters) for each plant such that the following cultivation rules are strictly followed:

1.  **Height Constraints**: Each plant's height must be a positive integer.
2.  **Symmetry Rule**: To maintain the visual balance of the display, the height of the plant in Pot 1 must be exactly equal to the height of the plant in Pot 5.
3.  **Contrast Rule**: For any two adjacent pots in the sequence (Pot 1 and 2, Pot 2 and 3, Pot 3 and 4, and Pot 4 and 5), the plants must have different heights. 
4.  **Nutrient Limitation**: To prevent soil exhaustion between neighbors, the combined height of plants in any two adjacent pots (Pots $i$ and $i+1$ for $i=1, 2, 3, 4$) must not exceed 6 decimeters.

How many different possible height configurations $(x_1, x_2, x_3, x_4, x_5)$ exist that satisfy these four conditions?

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
