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

In a specialized logistics simulation, a researcher is testing the efficiency of two independent automated conveyor systems, System X and System Y. Each system manages 2,024 robotic carriers. 

For System X, the researcher records the progress of each carrier $i$ as a value $x_i$, representing the fraction of its track completed. These values are sorted such that $0 \leq x_1 \leq x_2 \leq \dots \leq x_{2024} \leq 1$.
Similarly, for System Y, the progress of each carrier $i$ is recorded as $y_i$, where $0 \leq y_1 \leq y_2 \leq \dots \leq y_{2024} \leq 1$.

The researcher discovers that for a specific constant $p$ (where $p \leq 1$), the average progress of the carriers in both systems is exactly $p$. Mathematically, this is expressed as:
$$\frac{1}{2024} \sum_{i=1}^{2024} x_i = \frac{1}{2024} \sum_{i=1}^{2024} y_i = p$$

A "Cross-System Friction" value is then calculated by pairing the progress of System X carriers with the incremental progress gaps of System Y carriers in reverse order. Specifically, the total friction is the sum $\sum_{i=1}^{2024} x_i \Delta y_i$, where $\Delta y_i = y_{2025-i} - y_{2024-i}$ (defining $y_0 = 0$).

The researcher wants to find the smallest possible real value of $p$ that guarantees, regardless of the specific progress values chosen for the carriers, the total friction will always be at least $1 - p$. 

Find this minimum value of $p$.

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
