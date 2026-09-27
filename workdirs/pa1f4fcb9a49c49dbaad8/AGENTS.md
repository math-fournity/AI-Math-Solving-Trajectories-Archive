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

In a remote industrial automation facility, three sensors—Alpha ($x$), Beta ($y$), and Gamma ($z$)—report continuous real-number values. These sensors are integrated into a processing unit that can perform exactly three types of signal operations:
- **Summation ($x \sqcup y = x + y$):** The signals are added together.
- **Peak-Selection ($x \sharp y = \max\{x, y\}$):** The unit outputs only the highest signal value.
- **Safety-Capping ($x \flat y = \min\{x, y\}$):** The unit outputs only the lowest signal value.

The complexity of a signal-processing function is determined by its construction:
- Raw sensor inputs ($x, y, z$) have a complexity of $0$.
- If two functions $P$ and $Q$ have complexities $p$ and $q$ respectively, then any new function created by combining them using one of the three operations above ($P \sqcup Q$, $P \sharp Q$, or $P \flat Q$) has a complexity of $1 + p + q$.

A design engineer is auditing the system to determine the diversity of logic the unit can implement. Compute the total number of distinct mathematical functions $f: \mathbb{R}^3 \to \mathbb{R}$ that can be generated using these three sensors and the three operations, provided the complexity of the final expression is no greater than $3$.

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
