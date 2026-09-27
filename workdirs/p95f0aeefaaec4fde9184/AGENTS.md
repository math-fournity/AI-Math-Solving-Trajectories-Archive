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

In the futuristic city of Neoterra, a digital architect is designing a modular skyscraper. He uses two different automated calibration systems, System A and System B, to determine the number of floor stabilizers needed based on the building’s total structural capacity, represented by a natural number $n$.

System A calculates the stabilization requirement by taking the capacity $n$, multiplying it by a factor of 2012/2013, rounding the result down to the nearest whole number (using the floor function), and then adding 1 unit for safety.

System B calculates the requirement by taking the same capacity $n$, multiplying it by a factor of 2013/2014, and rounding the result up to the nearest whole number (using the ceiling function).

The architect seeks to identify all structural capacities $n$ (where $n$ is a positive integer) for which both systems yield the exact same number of stabilizers. 

How many such natural numbers $n$ exist that satisfy the condition:
$1 + \lfloor \frac{2012n}{2013} \rfloor = \lceil \frac{2013n}{2014} \rceil$?

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
