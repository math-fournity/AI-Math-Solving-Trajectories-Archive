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

A remote weather research station uses a digital atmospheric pressure gauge that tracks a variable integer $n$, where $1 < n \leq 1000$. Two automated protocols, Protocol A and Protocol F, manage the gauge to test system stability. 

Protocol A always acts first in a cycle. It is programmed to attempt to stabilize the system by either adding 4 to the current value $n$, or, if $n$ is currently an even number, dividing it by 2.

Protocol F acts second in the cycle. It attempts to stress the system by either subtracting 2 from the current value $n$, or, if $n$ is currently an odd number, multiplying it by 2.

The outcome of the simulation is determined by the following criteria:
- Protocol A is successful (wins) if the value $n$ reaches 0 or 1.
- Protocol F is successful (wins) if the value $n$ ever exceeds 1000, or if Protocol A fails to reach 0 or 1 within 100 complete cycles (where one cycle consists of both protocols executing their respective moves once).

Let $S$ be the set of all possible starting integers $n \in \{2, 3, \dots, 1000\}$ for which Protocol F has a strategy to guaranteed a win regardless of the choices made by Protocol A. Find the sum of all elements in $S$.

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
