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

In the high-tech logistics hub of Sector 2011, a master computer is programmed to generate encrypted security sequences. A sequence consists of an ordered list of 2011 specific calibration values, denoted as $(a_{1}, a_{2}, \ldots, a_{2011})$. Each individual value $a_i$ must be a positive integer selected from the range $1$ to $2011^2$, inclusive.

The system's integrity depends on whether a "Control Function" $f$ exists that can stabilize these values. For a sequence to be valid, there must exist a polynomial $f$ of degree exactly 4019 that satisfies three strict protocol requirements:
1.  **Integrity Check:** The output $f(n)$ must be an integer whenever the input $n$ is any integer.
2.  **Calibration Alignment:** For every position $i$ from 1 to 2011, the value $f(i)$ must be congruent to the sequence value $a_i$ modulo $2011^2$.
3.  **Cyclic Stability:** For every integer $n$, the difference between the outputs $f(n+2011)$ and $f(n)$ must be exactly divisible by $2011^2$.

Let $N$ be the total number of unique sequences $(a_{1}, a_{2}, \ldots, a_{2011})$ that allow for the existence of such a function $f$.

Find the remainder when $N$ is divided by 1000.

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
