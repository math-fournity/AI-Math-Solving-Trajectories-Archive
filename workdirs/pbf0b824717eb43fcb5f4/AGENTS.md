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

In a specialized digital circuit, a signal processor manages data streams composed of two types of pulses: Type-Alpha and Type-Beta. The processor operates according to two fundamental transformation protocols:
1. Any single Type-Alpha pulse can be converted into two consecutive Type-Beta pulses.
2. Any single Type-Beta pulse can be converted into two consecutive Type-Alpha pulses.

The processor initializes with a single Type-Alpha pulse. Let $a_n$ represent the total number of distinct pulse sequences of length $n$ (containing exactly $n$ pulses) that can be generated from this initial state through any number of protocol applications. For instance, $a_1 = 1$ because the only sequence of length 1 possible is the starting Type-Alpha pulse.

An engineer needs to calculate the total efficiency of the system, defined by the sum of the infinite series:
$$S = \sum_{n=1}^{\infty} \frac{a_n}{5^n}$$
Given that $S$ can be expressed as a simplified fraction $\frac{m}{n}$ where $m$ and $n$ are coprime positive integers, calculate the value of $100m + n$.

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
