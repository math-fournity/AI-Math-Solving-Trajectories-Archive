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

In a specialized logistics simulation, a technician is testing 1000 different automated inventory configurations. Each configuration is defined by an ordered triple of integer "priority codes" $(a_1, a_2, a_3)$, where each code is selected from the range of 1 to 10 inclusive ($1 \le a_1, a_2, a_3 \le 10$).

The simulation generates a continuous sequence of stock levels, $a_n$, for $n \ge 4$, based on a recursive algorithm. The algorithm dictates that the stock level at any step $n$ is equal to the level of the previous step ($a_{n-1}$) multiplied by the absolute difference between the levels of the two steps preceding that one ($|a_{n-2} - a_{n-3}|$).

The simulation is flagged as "Successful" if the stock level $a_n$ eventually reaches exactly 0 at any point in the sequence. Calculate the total number of initial priority code triples in the set of 1000 possible configurations that result in a Successful simulation.

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
