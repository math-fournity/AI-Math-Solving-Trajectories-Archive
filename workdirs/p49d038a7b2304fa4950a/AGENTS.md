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

In a specialized artisan workshop, a guild has been commissioned to produce two types of decorative tiles—Azure tiles and Bronze tiles—in exactly equal quantities. To complete this order, they have three distinct categories of crafting stations available for use during a single workday:

1. **Standard Kilns:** There are 3 units available. Each kiln can fire either 10 Azure tiles or 20 Bronze tiles in one day.
2. **Advanced Lathes:** There are 3 units available. Each lathe can glaze either 20 Azure tiles or 30 Bronze tiles in one day.
3. **Master Press:** There is 1 unit available. This press can stamp either 30 Azure tiles or 80 Bronze tiles in one day.

Each individual machine can divide its daily capacity between the two types of tiles (for example, a machine could spend half the day on one type and half on the other, producing half of its daily rate for each).

Under the constraint that the final total number of Azure tiles must equal the final total number of Bronze tiles, what is the maximum possible total number of tiles (the sum of both types) that can be produced across all seven stations in one day?

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
