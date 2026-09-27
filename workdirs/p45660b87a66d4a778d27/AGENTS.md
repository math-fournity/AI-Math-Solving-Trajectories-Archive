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

In a specialized laboratory, three experimental cooling modules—Alpha, Beta, and Gamma—operate under strict thermal equilibrium protocols. The core temperatures of these modules (measured in degrees Celsius relative to a baseline) are represented by the variables $x$, $y$, and $z$, respectively. Due to the unique crystalline structure of the heat sinks, it is physically impossible for any two modules to share the same temperature; thus, $x, y,$ and $z$ are distinct in pairs.

The thermal dynamics of the facility are governed by a specific feedback loop. The engineers have calibrated the system such that the square of the temperature in one module must always equal 2 units more than the linear temperature of the subsequent module in the sequence. Specifically, the system must satisfy the following three operational constraints:
1. The square of Alpha’s temperature is exactly 2 more than Beta’s temperature ($x^2 = 2 + y$).
2. The square of Beta’s temperature is exactly 2 more than Gamma’s temperature ($y^2 = 2 + z$).
3. The square of Gamma’s temperature is exactly 2 more than Alpha’s temperature ($z^2 = 2 + x$).

Let $S$ be the set of all possible values for the total "power-sum" of the system, defined as the sum of the squares of the three temperatures ($x^2 + y^2 + z^2$). Calculate the sum of all elements in $S$.

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
