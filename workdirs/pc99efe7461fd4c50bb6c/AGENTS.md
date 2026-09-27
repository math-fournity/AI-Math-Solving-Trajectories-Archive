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

In a remote industrial research facility, two chemical reactors, Alpha and Beta, process high-energy isotopes. The energy output of a specific reaction is governed by the structural formula $x^{2} + y^{2} + 3xy$, where $x$ and $y$ represent the integer quantities of two catalysts used in the process.

A series of experimental trials is conducted where the target energy output is defined by the expression $11 \cdot 5^{m} \cdot 3^{n}$. In this setup, $m$ and $n$ are integer power levels regulated by the facility's control system. 

An experimental configuration $(m, n)$ is deemed "stable" if there exist at least one pair of natural numbers $(x, y)$ that satisfy the energy equation. Let $S$ be the set of all such stable configurations within the operational range where both $1 \le m \le 10$ and $1 \le n \le 10$.

For every stable configuration $(m, n)$ in $S$, let $N(m, n)$ represent the total number of distinct pairs of natural numbers $(x, y)$ that can achieve that specific energy output.

Calculate the sum of the value $m + n + N(m, n)$ aggregated over every stable configuration $(m, n)$ found in the set $S$.

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
