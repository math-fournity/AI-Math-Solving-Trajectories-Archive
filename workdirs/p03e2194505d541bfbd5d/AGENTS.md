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

In the high-tech logistics center of Neo-City, a central processing unit must assign each of $n$ numbered delivery drones (labeled $1, 2, \dots, n$) to exactly one of $n$ available charging docks (also labeled $1, 2, \dots, n$). The system’s configuration protocols impose the following operational constraints on these assignments, denoted by the mapping $f$:

1.  Each drone $k$ can only be assigned to a charging dock with an index no greater than $k+1$. That is, $f(k) \le k+1$ for all $k \in \{1, 2, \dots, n\}$.
2.  For safety reasons, every drone except for the first one is strictly prohibited from being assigned to its own matching dock index. That is, $f(k) \neq k$ for all $k \in \{2, 3, \dots, n\}$. (Note: Drone 1 is permitted to be assigned to Dock 1).

Let $\overline{F_{n}}$ be the set of all valid assignment configurations that satisfy these two protocols. If the system randomly selects one valid configuration $f$ from the set $\overline{F_{n}}$ with equal probability, what is the probability that Drone 1 is not assigned to Dock 1?

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
