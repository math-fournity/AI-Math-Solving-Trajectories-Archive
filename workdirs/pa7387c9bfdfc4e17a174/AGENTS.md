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

In a global logistics network, $n$ distribution hubs (where $n \ge 3$) are arranged in a large circle. At the start of an optimization cycle, each hub is assigned exactly three unique identification chips from a set numbered $1, 2, \dots, 3n$.

The network operates through synchronized "sorting cycles." During each cycle, every hub simultaneously processes its three chips as follows:
1. The chip with the lowest serial number is sent to the adjacent hub located one position clockwise.
2. The chip with the highest serial number is sent to the adjacent hub located one position counterclockwise.
3. The chip with the median serial number is retained at the current hub.

Let $T_r$ represent the distribution state of all chips across the $n$ hubs after $r$ cycles ($T_0$ being the initial assignment). It has been mathematically proven that for any initial distribution, the system eventually enters a periodic state with a period of exactly $n$ cycles. 

Let $m(n)$ be defined as the minimum number of sorting cycles required to guarantee that the system has entered this periodic state. Specifically, $m(n)$ is the smallest non-negative integer such that $T_{m(n)} = T_{m(n)+n}$ holds true for every possible initial configuration of the $3n$ chips.

Calculate the value of the sum:
$$\sum_{n=3}^{100} m(n)$$

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
