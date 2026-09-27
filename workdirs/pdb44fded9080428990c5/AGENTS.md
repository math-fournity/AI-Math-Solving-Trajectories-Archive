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

In a remote industrial complex, there is a linear sequence of $100$ pressure valves, indexed from $1$ to $100$. Each valve $j$ has a flow setting $x_j$ that can be adjusted anywhere from $0$ (completely closed) to $1$ (completely open).

The safety system monitors the "leakage potential" between adjacent valves. For any two valves $i$ and $i+1$, the leakage potential is defined as the product of the flow setting of the first valve and the remaining capacity of the second valve, calculated as $x_i(1 - x_{i+1})$. The central safety threshold of the entire facility is determined by the maximum leakage potential found between any two consecutive valves in the sequence from $1$ to $99$.

An inspector identifies a "global bypass risk," which is defined as the product of the flow setting of the very first valve and the remaining capacity of the very last valve: $x_1(1 - x_{100})$.

The facility operates under a strict mathematical guarantee: there exists a fixed constant $C$ such that, regardless of how the $100$ flow settings are chosen, the maximum leakage potential between adjacent valves is always at least $C$ times the global bypass risk. 

Find the value of the largest such real number $C$ that makes this inequality hold for all possible configurations of $x_1, x_2, \dots, x_{100}$.

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
