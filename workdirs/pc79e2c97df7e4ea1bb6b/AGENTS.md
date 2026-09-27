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

In a specialized data processing facility, a thermal core operates according to a strict cooling protocol. The core’s energy state is represented by a sequence of positive integers $a_0, a_1, a_2, \dots$.

The initial energy level of the core is calibrated based on a prime-order setting $n$. For a specific stress test, this setting is $n = 2023$. The starting energy level is defined as $a_0 = 2^n - 1$.

The facility uses a "Normalization Protocol" to determine subsequent energy states. For any state $a_k$, the raw output of the next cycle is calculated as $3a_k + 1$. However, the system's hardware automatically filters out all binary instabilities. Mathematically, this means that for any integer $m$, the system extracts its "odd part"—defined as the value $2c+1$ when $m$ is written in the form $2^b(2c+1)$. Thus, the energy level for the next step, $a_{k+1}$, is defined as the odd part of $3a_k + 1$.

If the core is set to $n = 2023$, calculate the energy level of the core at the $n$-th step of the process (find $a_n$).

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
