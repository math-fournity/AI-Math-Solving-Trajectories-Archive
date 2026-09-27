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

In a remote digital architecture firm, a designer is tasked with creating "Safety Tilesets" for various rectangular server rooms. Each room is paved with a grid of $m \times n$ tiles. To meet security protocols, every tile must be set to one of two states: **Encrypted (E)** or **Open (O)**.

A configuration is considered "Secure" only if it adheres to these three strict protocols:
1.  **Perimeter Lockdown:** Every tile that touches the outer boundary of the $m \times n$ rectangular room must be set to the **Encrypted** state.
2.  **Uniformity Ban:** No four tiles arranged in a $2 \times 2$ block can all be the same state (they cannot all be Encrypted, nor can they all be Open).
3.  **Checkerboard Ban:** No four tiles arranged in a $2 \times 2$ block can be set in a "checkerboard" pattern (where the top-left and bottom-right are one state, while the top-right and bottom-left are the other).

Let $f(m, n) = 1$ if it is possible to create at least one Secure configuration for a room of dimensions $m \times n$ (where $m, n \ge 3$), and let $f(m, n) = 0$ if no such configuration is possible.

The designer needs to evaluate every possible room size where both the length $m$ and the width $n$ are integers between 3 and 10 inclusive. Calculate the total number of these room dimensions $(m, n)$ for which a Secure configuration exists. In other words, calculate the sum of $f(m, n)$ for all $3 \le m, n \le 10$.

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
