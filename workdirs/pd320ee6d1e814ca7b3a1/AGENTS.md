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

In a futuristic data center, a supercomputer is processing a master archive containing 2014 unique encrypted files. To ensure redundancy, the computer generates every possible "data packet" imaginable from this archive—a total of $2^{2014}$ packets, ranging from the empty packet to the one containing all 2014 files.

Each packet carries a specific "phase shift" value. If a packet contains $k$ files, its phase shift is calculated as the imaginary unit $i$ raised to the power of $k$ (where $i = \sqrt{-1}$). 

The system's total interference level, denoted by the complex number $Z$, is defined as the sum of the phase shifts of all $2^{2014}$ possible packets. This total interference can be expressed in the form $p + qi$, where $p$ and $q$ are integers.

An engineer needs to calculate the "magnitude sum" of the system, defined as the sum of the absolute values of the real and imaginary components, $|p| + |q|$. 

Find the remainder when $|p| + |q|$ is divided by 1000.

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
