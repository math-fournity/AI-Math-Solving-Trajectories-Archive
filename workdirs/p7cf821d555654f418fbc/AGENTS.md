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

A high-security data facility uses a cyclic authentication protocol involving 7 distinct server nodes, labeled uniquely with the IDs $\{1, 2, 3, 4, 5, 6, 7\}$. To authorize a system-wide update, an administrator must arrange these 7 IDs into a specific linear sequence $(a_1, a_2, a_3, a_4, a_5, a_6, a_7)$ that uses each ID exactly once.

The security system validates the sequence by calculating a "Cyclic Connectivity Score." This score is the sum of the products of all adjacent IDs in the sequence, including the connection between the final ID and the first ID to complete the circuit:
\[ \text{Score} = (a_1 \times a_2) + (a_2 \times a_3) + (a_3 \times a_4) + (a_4 \times a_5) + (a_5 \times a_6) + (a_6 \times a_7) + (a_7 \times a_1) \]

An arrangement is considered "Stable" if the resulting Connectivity Score is perfectly divisible by 7. 

Let $K$ be the total number of possible Stable arrangements of these 7 IDs. Calculate the value of $K \pmod{49}$.

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
