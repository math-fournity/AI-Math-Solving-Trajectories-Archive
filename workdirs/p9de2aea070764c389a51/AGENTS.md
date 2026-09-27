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

In a large international logistics hub, a conveyor belt processes a total of 8,080 shipping containers. The manifest confirms that there are exactly 2,020 containers from each of four different companies: Alpha Corp ($A$), Beta Inc ($B$), Gamma Co ($C$), and Delta Ltd ($D$).

The efficiency of the sorting sequence, denoted as $\sigma$, is measured by four specific "flow metrics":
1.  **Metric $f_{AB}$**: The total count of all Beta containers that appear anywhere on the belt after (to the right of) each Alpha container.
2.  **Metric $f_{BC}$**: The total count of all Gamma containers that appear anywhere after each Beta container.
3.  **Metric $f_{CD}$**: The total count of all Delta containers that appear anywhere after each Gamma container.
4.  **Metric $f_{DA}$**: The total count of all Alpha containers that appear anywhere after each Delta container.

For instance, if a small sample sequence was $ACBDBACDCBAD$, the metric $f_{AB}$ would be 4, because the first $A$ is followed by 3 $B$s, the second $A$ is followed by 1 $B$, and the third $A$ is followed by 0 $B$s ($3+1+0=4$).

The facility manager wants to organize the 8,080 containers in a single linear sequence $\sigma$ that maximizes the total throughput, defined as the sum:
$$f_{AB}(\sigma) + f_{BC}(\sigma) + f_{CD}(\sigma) + f_{DA}(\sigma)$$

What is the maximum possible value of this sum?

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
