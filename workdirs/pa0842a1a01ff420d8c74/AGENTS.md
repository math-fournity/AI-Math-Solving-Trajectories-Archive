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

A network of 1001 research laboratories, designated $L_1, L_2, \dots, L_{1001}$, is collaborating on a long-term data processing project. At the start of the project, each laboratory $L_k$ is assigned exactly $k$ terabytes of raw data for storage and analysis ($k = 1, 2, \dots, 1001$).

The project progresses through a series of "Data Exchange Operations." In each operation, a coordinator selects an ordered pair of laboratories $(i, j)$ such that $1 \le i < j \le 1001$. The operation must adhere to the following strict protocols:
1. Both laboratories $L_i$ and $L_j$ must currently store at least 1 terabyte of data.
2. The specific ordered pair $(i, j)$ can never be selected more than once throughout the entire project.
3. If laboratory $L_i$ currently holds $a$ terabytes and laboratory $L_j$ holds $b$ terabytes, both laboratories must simultaneously delete exactly $\gcd(a, b)$ terabytes from their respective storage.

The project continues as long as a valid ordered pair $(i, j)$ can be chosen to perform an operation. What is the maximum number of times this operation could be performed?

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
