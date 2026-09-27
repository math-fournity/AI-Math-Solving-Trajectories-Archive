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

In a specialized logistics hub, two automated sorting systems, System X and System Y, process packages in specific batch sizes. System X handles two consecutive batch sizes, represented by the positive integers $x$ and $x+1$. System Y similarly handles two consecutive batch sizes, $y$ and $y+1$.

The efficiency protocol of the hub requires that the total product of System X's batch sizes, $x(x+1)$, must be a perfect divisor of the total product of System Y's batch sizes, $y(y+1)$. 

However, the internal logic of the machines imposes a "non-overlap" constraint: 
1. The smaller batch size of System X ($x$) is not a divisor of either batch size used by System Y ($y$ or $y+1$).
2. The larger batch size of System X ($x+1$) is also not a divisor of either batch size used by System Y ($y$ or $y+1$).

An engineer is tasked with calibrating these systems to minimize the "Total Power Load," which is defined by the sum of the squares of the primary batch sizes: $x^2 + y^2$.

Find the minimum possible value of $x^2 + y^2$ that satisfies all the operational constraints of the hub.

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
