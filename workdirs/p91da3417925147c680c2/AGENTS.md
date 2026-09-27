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

Place the 21 two-digit prime numbers (11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97) into the white squares of a $5 \times 5$ grid such that each prime is used exactly once. 

The white squares are located at the following coordinates $(row, col)$, where $(1,1)$ is the top-left corner:
- Row 1: (1,1), (1,2), (1,3), (1,4), (1,5)
- Row 2: (2,1), (2,3), (2,4), (2,5)
- Row 3: (3,1), (3,3), (3,5)
- Row 4: (4,1), (4,2), (4,3), (4,5)
- Row 5: (5,1), (5,2), (5,3), (5,4), (5,5)

Two white squares sharing a side must contain two numbers with either the same tens digit or the same ones digit. Additionally, the following digits are "given" for specific squares, meaning the prime number in that square must contain that digit:
- (1,1): 3
- (1,3): 3
- (1,5): 8
- (3,1): 9
- (3,3): 9
- (3,5): 9
- (5,1): 6
- (5,3): 1
- (5,5): 4

Find the sum of the five prime numbers located in the first row.

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
