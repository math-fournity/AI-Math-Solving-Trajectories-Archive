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

A mysterious deep-space probe is programmed to transmit data packets using a specific encryption protocol. The protocol relies on a "Frequency Shift Factor," which is an integer $a$. For any two integer input signals $k$ and $l$, the probe calculates a secondary transmission value using the polynomial function $P(x) = x^5 + ax$.

The system is considered "Stably Decodable" for a network size $n$ ( where $n$ is a natural number) if the following condition holds: whenever the difference between the transmission values $P(k)$ and $P(l)$ is perfectly divisible by $n$, it must necessarily follow that the difference between the original signals $k$ and $l$ is also perfectly divisible by $n$, for all possible integer pairs $(k, l)$.

The probe's hardware constraints dictate that there are only a finite number of network sizes $n$ for which the system is Stably Decodable. It is further known that one of these valid network sizes is exactly $n = 95$.

Find one possible integer value for the Frequency Shift Factor $a$ that satisfies these conditions.

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
