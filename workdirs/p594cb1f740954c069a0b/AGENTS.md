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

In a remote industrial district, three energy processing plants—Alpha, Beta, and Gamma—operate using three specific fuel grades, measured in units of $a$, $b$, and $c$ respectively ($a, b, c > 0$). 

Each plant runs a specialized efficiency test to determine a global stability constant, $k$. The efficiency rating for each plant is determined by a specific ratio of its resource allocation.

1.  **Plant Alpha's Rating:** The numerator is the sum of $k$ times the square of its primary fuel $a$, plus the squares of the other two fuels ($b^2 + c^2$). This is divided by a denominator consisting of twice the square of its primary fuel ($2a^2$) plus the interaction product of the other two fuels ($bc$).
2.  **Plant Beta's Rating:** The numerator is the sum of $k$ times the square of its primary fuel $b$, plus the squares of $c^2$ and $a^2$. This is divided by twice the square of its primary fuel ($2b^2$) plus the interaction product $ca$.
3.  **Plant Gamma's Rating:** The numerator is the sum of $k$ times the square of its primary fuel $c$, plus the squares of $a^2$ and $b^2$. This is divided by twice the square of its primary fuel ($2c^2$) plus the interaction product $ab$.

The district's total output is the sum of these three individual ratings. For the system to remain economically viable, this total output must always be greater than or equal to the sum of the stability constant $k$ and the integer 2, regardless of the quantities of fuel $a, b,$ and $c$ used.

Find the greatest positive value of the stability constant $k$ that satisfies this requirement.

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
