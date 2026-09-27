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

In a bustling coastal region, there are $N$ distinct ports ($N \geq 3$) positioned along a straight trade route, indexed $1, 2, \ldots, N$ according to their distance from the capital. To facilitate trade, the regional governor has decreed that every single pair of ports must have exactly one direct shipping lane between them, always directed from the port with the lower index to the port with the higher index.

The Ministry of Transportation must now assign a logistics contract to each of these shipping lanes. Every lane must be designated as either a "Red Line" (specializing in heavy industrial goods) or a "Blue Line" (specializing in consumer electronics). 

A logistical network is classified as "Efficient" if there is no pair of ports, Port $A$ and Port $B$, such that it is possible to travel from $A$ to $B$ using a sequence of only Red Lines and also possible to travel from $A$ to $B$ using a sequence of only Blue Lines. 

How many different ways can the Ministry assign the Red and Blue designations to all the shipping lanes such that the resulting network remains Efficient?

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
