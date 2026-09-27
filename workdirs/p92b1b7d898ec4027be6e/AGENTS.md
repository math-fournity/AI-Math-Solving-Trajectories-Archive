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

In a futuristic data-storage facility, an encryption sequence is classified as "Corrupted" if it contains the digit 1 followed immediately by the digit 3 (the substring "13"). If this specific sequence does not appear, the data is classified as "Secure."

A cybersecurity engineer is investigating a strange pattern in the server logs involving a base-10 numerical ID, $n$, and a specific offset value, $a$. She discovers a unique anomaly where the following conditions are met:

1. The initial ID number, $n$, is a positive integer and is Secure.
2. There exists a positive integer increment, $a$, which is strictly less than 100.
3. The final ID in the series, calculated as $n + 10a$, is also Secure.
4. Every single intermediate ID in the progression—specifically $n+a, n+2a, n+3a, n+4a, n+5a, n+6a, n+7a, n+8a$, and $n+9a$—is Corrupted.

Find the smallest possible value of the positive integer $n$ that allows such a sequence to exist.

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
