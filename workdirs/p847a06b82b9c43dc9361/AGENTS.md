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

In a remote logistics network, there are 4 regional hubs named Alpha, Bravo, Charlie, and Delta. Each hub contains exactly 2 docking bays, labeled 1 and 2 (for example, hub Alpha has bays $A_1$ and $A_2$). This results in a total of 8 available docking bays across the network.

An automated system is tasked with deploying 3 fiber-optic cables to establish connections. Each cable has two ends, and each end must be plugged into exactly one docking bay. Every docking bay can accommodate at most one cable end. The system assigns the 6 ends of the 3 cables to 6 of the 8 available docking bays completely at random, such that every possible valid configuration of connections is equally likely.

A "Data Loop" is triggered if a sequence of cables forms a path that starts and ends at the same hub. For instance, a single cable connecting $A_1$ to $A_2$ creates a Data Loop. Similarly, if one cable connects $A_1$ to $B_1$, a second connects $B_2$ to $C_1$, and a third connects $A_2$ to $C_2$, a Data Loop is formed through the series of hubs. However, a single cable connecting $A_1$ to $B_1$ does not constitute a loop.

What is the probability that the system creates at least one Data Loop? If the probability is expressed as an irreducible fraction $\frac{a}{b}$, calculate the value of $a + b$.

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
