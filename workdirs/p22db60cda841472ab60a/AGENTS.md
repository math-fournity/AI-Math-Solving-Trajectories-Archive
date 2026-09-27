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

In a high-security data center, three automated maintenance protocols—codenamed Alpha, Beta, and Gamma—run on fixed, repeating cycles. Protocol Alpha triggers every 7 minutes, Protocol Beta every 11 minutes, and Protocol Gamma every 13 minutes (starting from minute 0).

A security specialist defines a "Vulnerability Window" around these maintenance events. A specific minute $n$ is considered "compromised" if it falls within 2 minutes of a protocol trigger (specifically, if the difference between $n$ and any multiple of the protocol’s cycle is 2 or less). Conversely, a minute is considered "Safe" relative to a protocol if it is not compromised by it.

For example, a minute $n$ is "10-Safe" only if the absolute difference between $n$ and any multiple of 10 is strictly greater than 2. This results in the set of 10-Safe minutes: $\{3, 4, 5, 6, 7, 13, 14, 15, 16, 17, 23, \dots\}$.

The specialist needs to audit the first 10,000 minutes of operation (from $n = 1$ to $n = 10,000$ inclusive). How many of these positive integer minutes are simultaneously 7-Safe, 11-Safe, and 13-Safe?

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
