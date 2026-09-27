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

A specialized cargo ship is designed with a circular hold divided into 5 storage bays, arranged in a ring and labeled $x_1, x_2, x_3, x_4, x_5$ in clockwise order. Each bay contains a specific tonnage of precious minerals: Bay $x_1$ contains 15 tons, Bay $x_2$ contains 5 tons, Bay $x_3$ contains 20 tons, Bay $x_4$ contains 40 tons, and Bay $x_5$ contains 20 tons.

Two logistics companies, Alpha and Beta, have been contracted to unload the minerals. Alpha goes first and selects any one of the five bays to empty. From then on, the companies take turns selecting a bay to unload, but with a strict structural constraint: every subsequent bay chosen must be immediately adjacent to at least one bay that has already been emptied.

The companies continue alternating turns until all 5 bays are cleared. If the manager of Company Alpha follows a strategy to maximize the total tonnage his company retrieves, what is the total weight of the minerals that Alpha receives?

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
